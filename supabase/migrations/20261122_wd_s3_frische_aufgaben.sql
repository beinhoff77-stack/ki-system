-- WD-S 3 (22.11.): Ergänzung zu 20261122_wd_s_wiederholungen.sql (WD-S 2) – danach einspielen, in einer Transaktion.
-- Vorgabe: inhalte/AUFTRAEGE.md „Fehler Mischkarten (22.11.)“, Nachtrag „WD-S 3 – frische Aufgaben“ (Entscheidung des Nutzers) und
-- „ChatGPT 919 zu WD-S 2 / WD-4b / Nacharbeit 907“, Teil bau-lehrer.
--
-- 1. Frische Aufgaben (eine Regel für Wiederholung und Mischkarte, schule.wdh_aufgabe_waehlen):
--    Nie eine Aufgabe, die das Kind in den letzten 3 Lerntagen beantwortet hat (heute + die 2 vorigen Lerntage; jede Rolle: Üben, Wiederholung,
--    Mischkarte, Test, Knobeln) – Regel wdh_sperre_lerntage. Wiederholung nach 1, 3, 7 Lerntagen (Stufe 0–2) und jede Mischkarte: zuerst Aufgaben,
--    die das Kind noch nie beantwortet hat (darunter zufällig), sonst die am längsten zurückliegende. Nach 14 und 30 Lerntagen (Stufe 3–4): beliebige,
--    bevorzugt die am längsten zurückliegende (noch nie beantwortet zählt als am längsten zurück). Gibt es keine: an diesem Tag keine Aufgabe dieser
--    Etappe – die Wiederholung bleibt fällig, in der Tagesrunde zählt die Etappe als bearbeitet (wie „gesperrt“).
--    Mischkarten: nie aus einer Etappe, in der das Kind am selben Lerntag schon eine Aufgabe beantwortet hat (auch wenn sie fällig ist).
--    Offene Ausgabe verfällt sofort, wenn dieselbe Aufgabe anders beantwortet wird (Trigger versuch_misch_verfall), und beim nächsten Ausgeben,
--    wenn die Aufgabe schon beantwortet oder die Etappe heute schon dran war.
--    Mischkarte ohne gültige Ausgabe: Antwort misch {gueltig: false, sterne}, wird nicht als Wiederholung gebucht (kein Fortschritt, kein
--    Wiederholungs-Fehler; als normales Üben wie bisher). Gültige Mischkarte: misch.gueltig = true und misch.sterne. sterne = tatsächlich gebuchte Sterne.
-- 2. Bestandene Wiederholung nur richtig im ersten Versuch ohne Tipp (Regel wdh_nur_selbst, Standard true – der Nutzer kann umschalten):
--    gilt für Runde, freiwillige Wiederholung und Mischkarte. Richtig mit Tipp oder im zweiten Versuch: kein Fortschritt, kein Fehler, keine
--    Wiederholungs-Sterne, kein Ablegen; die Etappe kommt am nächsten Lerntag wieder. Endgültig falsch: wie bisher.
--    (Die Hilfe des Versuchs merkt sich ein Trigger vor dem Speichern des Versuchs; uebung_pruefen_intern setzt hilfe ≥ 1 im zweiten Anlauf.)
--    Mischkarte mit Tipp zählt jetzt als Antwort (richtig + 1), damit die Etappe in der Runde als bearbeitet gilt; Beleg gibt es weiter nur ohne Tipp.
-- 3. Reihenfolge: falsche Mischkarte zählt als Wiederholungs-Fehler erst nach endgültiger Wertung (schule.versuch_wertung = 'falsch').
-- 4. Lesend für den Haupt-Chat: schule.etappen_wenig_frisch() – je Kind die gelandeten Etappen mit weniger als 3 frischen Aufgaben der Stufen 2–3.
-- WD-4b (Stau strecken) ist in 20261122_wd_4b_stau_strecken.sql nachgezogen (offene Tagesrunde, belegte Folgetage, Rückweg nur ohne Zwischenübung).
-- sterne_wdh_richtig bleibt 10 bis zu Entscheidung des Nutzers.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE; Bestand unverändert (am Ende geprüft). Wiederholt ausführbar.

create temp table if not exists wd3_vorher (t text, s text) on commit drop;
truncate wd3_vorher; -- nur die Hilfstabelle dieser Sitzung
insert into wd3_vorher
  select 'karte', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x
  union all select 'lernziel', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x
  union all select 'sterne', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x;

insert into schule.regel (schluessel, wert, hinweis) values
  ('wdh_nur_selbst', 'true', 'WD-S 3: Wiederholung bestanden nur richtig im ersten Versuch ohne Tipp (Fortschritt, Wiederholungs-Sterne, Ablegen)'),
  ('wdh_sperre_lerntage', '3', 'WD-S 3: keine Aufgabe, die in den letzten n Lerntagen beantwortet wurde (heute + n-1 vorige Lerntage)')
on conflict (schluessel) do nothing;

-- ab diesem Tag gilt eine Antwort als „in den letzten n Lerntagen“ (heute und die n-1 vorigen Lerntage; Tage ohne Lernen zählen nicht)
create or replace function schule.wdh_sperre_ab(p_l bigint)
 returns date language sql stable set search_path to ''
as $function$
  select coalesce((select min(q.datum) from (select t.datum from schule.lerntag t where t.lernender_id = p_l and t.fach = 'Mathematik' and t.datum < schule.heute_tag(p_l)
                                              order by t.datum desc limit greatest(schule.wd_regel('wdh_sperre_lerntage', 3) - 1, 0)) q), schule.heute_tag(p_l));
$function$;

-- Lerntag (in der Zeitzone des Kindes) eines Zeitpunkts
create or replace function schule.lern_datum(p_l bigint, p_zeit timestamptz)
 returns date language sql stable set search_path to ''
as $function$
  select (p_zeit at time zone coalesce((select l.zeitzone from schule.lernender l where l.id = p_l), 'Europe/Berlin'))::date;
$function$;

-- Aufgabe für eine Wiederholung oder Mischkarte (null = heute keine)
create or replace function schule.wdh_aufgabe_waehlen(p_l bigint, p_e bigint, p_lz text, p_misch boolean)
 returns bigint language sql volatile set search_path to ''  -- volatile: zufällige Wahl, je Aufruf genau einmal ausgewertet
as $function$
  with c as (
    select a.id, coalesce(a.stufe, 2) stufe, (select max(v.am) from schule.versuch v where v.lernender_id = p_l and v.aufgabe_id = a.id) zuletzt
      from schule.aufgabe a
     where a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung' and a.freigegeben and (not p_misch or a.stufe in (2, 3)))
  select c.id from c
   where c.zuletzt is null or schule.lern_datum(p_l, c.zuletzt) < schule.wdh_sperre_ab(p_l)
   order by c.zuletzt nulls first, (c.stufe = 1), random() limit 1;
$function$;

-- Etappe (einer Einheit) heute schon beantwortet?
create or replace function schule.etappe_heute_beantwortet(p_l bigint, p_e bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                  where v.lernender_id = p_l and a.einheit_id = p_e and a.variante_gruppe = p_lz and schule.lern_datum(p_l, v.am) = schule.heute_tag(p_l));
$function$;

-- Hat die Etappe heute eine Aufgabe für die Wiederholung? (sonst zählt sie in der Runde als bearbeitet)
create or replace function schule.wdh_aufgabe_da(p_l bigint, p_e bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.einheit e where e.id = p_e and e.status in ('geprueft', 'freigegeben'))
     and schule.wdh_aufgabe_waehlen(p_l, p_e, p_lz, false) is not null;
$function$;

-- Hilfe des Versuchs merken (für karte_wdh_ereignis: Wiederholung bestanden nur ohne Tipp/zweiten Versuch)
create or replace function schule.versuch_hilfe_merken()
 returns trigger language plpgsql set search_path to ''
as $function$
begin
  perform set_config('schule.antwort_hilfe', coalesce(new.hilfe, 0)::text, true);
  return new;
end $function$;
create or replace trigger versuch_hilfe_merken before insert on schule.versuch for each row execute function schule.versuch_hilfe_merken();

-- Offene Mischkarten-Ausgabe verfällt, sobald dieselbe Aufgabe anders beantwortet wird
create or replace function schule.versuch_misch_verfall()
 returns trigger language plpgsql set search_path to ''
as $function$
begin
  if not coalesce(new.misch, false) then
    update schule.misch_ausgabe set verfallen_am = now()
     where lernender_id = new.lernender_id and aufgabe_id = new.aufgabe_id and eingeloest_am is null and verfallen_am is null;
  end if;
  return new;
end $function$;
create or replace trigger versuch_misch_verfall after insert on schule.versuch for each row execute function schule.versuch_misch_verfall();

-- Reihenfolge: falsche Mischkarte erst nach endgültiger Wertung als Wiederholungs-Fehler
create or replace function schule.wdh_fehler(k schule.karte_stand)
 returns boolean language sql stable set search_path to ''
as $function$
  select coalesce(k.wdh_fehler, 0) > 0
      or exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                  where v.lernender_id = k.lernender_id and coalesce(v.misch, false) and not v.richtig and v.testsitzung_id is null
                    and coalesce(v.wertung_fest, schule.versuch_wertung(v)) = 'falsch'
                    and a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel and v.am >= coalesce(k.wdh_ab, k.sitzt_am, '-infinity'::timestamptz));
$function$;

-- Runde prüfen (wie WD-S 2, „Aufgabe da“ jetzt je Kind und Tag)
create or replace function schule.wdh_runde_pruefen(p_l bigint, p_tag date)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_offen int;
begin
  select count(*) into v_offen from schule.wdh_runde_etappe r
   where r.lernender_id = p_l and r.tag = p_tag and r.bearbeitet_am is null and schule.wdh_aufgabe_da(p_l, r.einheit_id, r.lernziel);
  if v_offen = 0 then
    update schule.wdh_runde set fertig_am = now() where lernender_id = p_l and tag = p_tag and fertig_am is null;
  end if;
  return v_offen;
end $function$;

-- Runde festhalten (wie WD-S 2, „Aufgabe da“ je Kind und Tag)
create or replace function schule.wdh_runde_holen(p_l bigint, p_tag date)
 returns void language plpgsql set search_path to ''
as $function$
declare v_faellig int; v_da int; v_ziel int; v_alt int;
begin
  if exists (select 1 from schule.wdh_runde where lernender_id = p_l and tag = p_tag) then return; end if;
  if to_regclass('pg_temp.wd3_kand') is null then
    create temp table wd3_kand (einheit_id bigint, lernziel text, fehler boolean, faellig_am timestamptz, wdh_stufe int, da boolean) on commit drop;
  end if;
  truncate wd3_kand;  -- nur die Hilfstabelle dieser Sitzung
  insert into wd3_kand select k.einheit_id, k.lernziel, schule.wdh_fehler(k), k.faellig_am, k.wdh_stufe, schule.wdh_aufgabe_da(p_l, k.einheit_id, k.lernziel)
    from schule.karte_stand k where k.lernender_id = p_l and schule.karte_faellig(k);
  select count(*), count(*) filter (where c.da) into v_faellig, v_da from wd3_kand c;
  v_ziel := least(schule.wdh_runde_groesse(p_l, v_faellig), v_da);
  v_alt := ceil(v_ziel / 3.0)::int;                         -- mindestens ein Drittel für die am längsten fälligen
  insert into schule.wdh_runde (lernender_id, tag, ziel, faellig) values (p_l, p_tag, v_ziel, v_faellig) on conflict do nothing;
  if not found then return; end if;                         -- gleichzeitig von einem anderen Gerät angelegt
  insert into schule.wdh_runde_etappe (lernender_id, tag, nr, einheit_id, lernziel)
  with da as (select * from wd3_kand c where c.da),
  alt as (select d.* from da d order by d.faellig_am nulls first, d.wdh_stufe, d.einheit_id, d.lernziel limit v_alt),
  rest as (select d.* from da d where not exists (select 1 from alt x where x.einheit_id = d.einheit_id and x.lernziel = d.lernziel)
            order by d.fehler desc, d.faellig_am nulls first, d.wdh_stufe, d.einheit_id, d.lernziel limit greatest(v_ziel - v_alt, 0)),
  wahl as (select * from alt union all select * from rest)
  select p_l, p_tag, row_number() over (order by w.fehler desc, w.faellig_am nulls first, w.wdh_stufe, w.einheit_id, w.lernziel), w.einheit_id, w.lernziel from wahl w;
  perform schule.wdh_runde_pruefen(p_l, p_tag);
end $function$;

-- schule_wiederholung: Aufgaben nach der Frische-Regel (Felder wie WD-S 2)
create or replace function schule.wiederholung_intern(p_l bigint, p_daten jsonb, p_leiter boolean, p_tag date default null)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_l bigint := p_l; v_n int := least(coalesce(nullif(p_daten->>'anzahl', '')::int, 60), 60); v_tag date := coalesce(p_tag, schule.heute_tag(p_l));
  v_test boolean; v_erg jsonb; v_faellig int; v_r schule.wdh_runde; v_offen int;
begin
  select ist_test into v_test from schule.lernender where id = v_l;
  perform schule.wdh_runde_holen(v_l, v_tag);
  v_offen := schule.wdh_runde_pruefen(v_l, v_tag);
  select * into v_r from schule.wdh_runde where lernender_id = v_l and tag = v_tag;
  select count(*) into v_faellig from schule.karte_stand k where k.lernender_id = v_l and schule.karte_faellig(k);
  select coalesce(jsonb_agg(x.j || jsonb_build_object('pflicht', x.pflicht) order by x.rang, x.nr), '[]'::jsonb) into v_erg from (
    select q.* from (
      select case when r.nr is not null then 0 else 1 end rang,
             coalesce(r.nr, 1000 + row_number() over (order by schule.wdh_fehler(k) desc, k.faellig_am nulls first, k.wdh_stufe, k.einheit_id, k.lernziel)) nr,
             r.nr is not null pflicht,
             schule.aufgabe_anzeige(a, true) || jsonb_build_object('einheit_id', k.einheit_id, 'stadt', b.stadt, 'lernziel', k.lernziel, 'wdh_stufe', k.wdh_stufe,
               'etappe', (select et->>'titel' from jsonb_array_elements(e.inhalt->'etappen') et where et->>'lernziel' = k.lernziel limit 1)) j
        from schule.karte_stand k join schule.einheit e on e.id = k.einheit_id join schule.block b on b.id = e.block_id
        left join schule.wdh_runde_etappe r on r.lernender_id = k.lernender_id and r.tag = v_tag and r.einheit_id = k.einheit_id and r.lernziel = k.lernziel
        cross join lateral (select schule.wdh_aufgabe_waehlen(v_l, k.einheit_id, k.lernziel, false) id) w   -- WD-S 3: frische Aufgabe, sonst keine
        join schule.aufgabe a on a.id = w.id
       where k.lernender_id = v_l
         and ((r.nr is not null and r.bearbeitet_am is null) or (r.nr is null and schule.karte_faellig(k)))
         and (e.status in ('geprueft','freigegeben') or (e.status = 'entwurf' and coalesce(v_test, false) and p_leiter))) q
     order by q.rang, q.nr limit v_n) x;
  return jsonb_build_object('ok', true, 'aufgaben', v_erg, 'faellig', v_faellig, 'runde', coalesce(v_r.ziel, 0),
    'runde_offen', v_offen, 'runde_bearbeitet', greatest(coalesce(v_r.ziel, 0) - v_offen, 0), 'runde_gemacht', v_r.fertig_am is not null,
    'gestaffelt', (select count(*) from schule.karte_stand k where k.lernender_id = v_l and k.sitzt and k.wdh_gesetzt_am is not null and k.wdh_stufe = 0
                     and k.wdh_fehler = 0 and k.wdh_lerntage > 1 and not schule.karte_faellig(k)));
end $function$;

-- Antwort auf eine Etappe (wie WD-S 2) + WD-S 3: ungültige Mischkarte nicht als Wiederholung; mit Tipp/zweitem Versuch kein Fortschritt
create or replace function schule.karte_wdh_ereignis()
 returns trigger language plpgsql set search_path to ''
as $function$
declare v_bestanden boolean; v_sterne int := 0; v_beginn text; v_abgelegt jsonb; v_erg jsonb; v_tag date;
  v_hilfe boolean := coalesce(nullif(current_setting('schule.antwort_hilfe', true), ''), '0')::int > 0;
  v_nur_selbst boolean := coalesce((select (r.wert #>> '{}')::boolean from schule.regel r where r.schluessel = 'wdh_nur_selbst'), true);
begin
  -- Rückfall nach dem Ablegen: kommt eine abgelegte Etappe wieder in den Takt (Fehler beim Üben, falsche Mischkarte, Nachtest), dann mit Stufe 2 am nächsten Lerntag
  if old.sitzt and new.sitzt and old.wdh_ab is null and old.faellig_am is null and old.wdh_lerntage is null and new.wdh_ab is not null
     and exists (select 1 from schule.abgelegt g where g.lernender_id = new.lernender_id and g.bezug = 'etappe:' || new.einheit_id || ':' || new.lernziel) then
    new.wdh_stufe := 2; new.wdh_lerntage := 1; new.faellig_am := new.wdh_ab + interval '1 day';
  end if;
  if new.richtig <= old.richtig and new.falsch <= old.falsch then return new; end if;   -- keine Antwort
  -- WD-2: Antwort auf eine Etappe der heutigen Runde → bearbeitet (richtig oder falsch)
  v_tag := schule.heute_tag(new.lernender_id);
  update schule.wdh_runde_etappe set bearbeitet_am = now()
   where lernender_id = new.lernender_id and tag = v_tag and einheit_id = new.einheit_id and lernziel = new.lernziel and bearbeitet_am is null;
  if found then perform schule.wdh_runde_pruefen(new.lernender_id, v_tag); end if;
  if not old.sitzt or not schule.karte_faellig(old) then return new; end if;               -- keine Wiederholung
  -- WD-S 3: Mischkarte ohne gültige Ausgabe – nicht als Wiederholung buchen (Takt bleibt wie vorher)
  if coalesce(current_setting('schule.kein_wdh', true), '') = '1' then
    new.wdh_stufe := old.wdh_stufe; new.faellig_am := old.faellig_am; new.wdh_ab := old.wdh_ab; new.wdh_lerntage := old.wdh_lerntage;
    new.wdh_fehler := old.wdh_fehler; new.sitzt := old.sitzt; new.geoeffnet_am := old.geoeffnet_am;
    return new;
  end if;
  -- WD-S 3: richtig mit Tipp oder im zweiten Versuch – kein Fortschritt, kein Fehler, am nächsten Lerntag wieder
  if new.richtig > old.richtig and v_hilfe and v_nur_selbst then
    new.wdh_stufe := old.wdh_stufe; new.wdh_fehler := old.wdh_fehler; new.sitzt := old.sitzt;
    new.wdh_ab := now(); new.wdh_lerntage := 1; new.faellig_am := now() + interval '1 day';
    perform set_config('schule.wdh_ergebnis', jsonb_build_object('bestanden', false, 'sterne', 0, 'stufe_neu', new.wdh_stufe, 'naechste_in', 1,
                                                                  'einheit_id', new.einheit_id, 'lernziel', new.lernziel, 'mit_hilfe', true)::text, true);
    return new;
  end if;
  v_bestanden := new.richtig > old.richtig and new.sitzt and new.wdh_fehler = 0 and new.wdh_ab is distinct from old.wdh_ab
                 and new.wdh_stufe = least(old.wdh_stufe + 1, 4);
  if v_bestanden then
    v_beginn := coalesce(extract(epoch from coalesce(old.wdh_ab, old.faellig_am))::bigint::text, 'x');
    insert into schule.sterne (lernender_id, menge, grund, bezug)
    values (new.lernender_id, schule.wd_regel('sterne_wdh_richtig', 10), 'wdh', 'wdh:' || new.einheit_id || ':' || new.lernziel || ':' || v_beginn)
    on conflict do nothing returning menge into v_sterne;
    perform set_config('schule.wdh_karte', new.einheit_id || '/' || new.lernziel, true);  -- sterne_aus_versuch: für diesen Versuch keine 'uebung'-Sterne
    if old.wdh_stufe >= 4 then                                                             -- fünfte Wiederholung (30 Lerntage) bestanden: abgelegt
      new.faellig_am := null; new.wdh_ab := null; new.wdh_lerntage := null;
      v_abgelegt := schule.wdh_ablegen(new.lernender_id, new.einheit_id, new.lernziel);
    end if;
  end if;
  v_erg := jsonb_strip_nulls(jsonb_build_object('bestanden', v_bestanden, 'sterne', coalesce(v_sterne, 0), 'stufe_neu', new.wdh_stufe,
             'naechste_in', case when new.sitzt then new.wdh_lerntage end, 'einheit_id', new.einheit_id, 'lernziel', new.lernziel, 'abgelegt', v_abgelegt));
  perform set_config('schule.wdh_ergebnis', v_erg::text, true);
  return new;
end $function$;

-- Antwort der Übung (wie WD-S 2) + misch {gueltig, sterne}; ungültige Mischkarte wird nicht als Wiederholung gebucht
create or replace function schule.uebung_pruefen_wd(p_l bigint, p_daten jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_r jsonb; v_w jsonb; v_a schule.aufgabe; v_will boolean := coalesce((p_daten->>'misch')::boolean, false); v_gueltig boolean := false;
  v_s0 bigint := (select coalesce(sum(s.menge), 0) from schule.sterne s where s.lernender_id = p_l);
begin
  if v_will then
    select * into v_a from schule.aufgabe where id = nullif(p_daten->>'aufgabe_id', '')::bigint;
    v_gueltig := v_a.id is not null and schule.misch_gueltig(p_l, v_a, p_daten);   -- vor dem Speichern prüfen (danach ist die Ausgabe eingelöst)
  end if;
  perform set_config('schule.wdh_ergebnis', '', true);
  perform set_config('schule.kein_wdh', case when v_will and not v_gueltig then '1' else '' end, true);
  v_r := schule.uebung_pruefen_intern(p_l, p_daten);
  perform set_config('schule.kein_wdh', '', true);
  v_w := nullif(current_setting('schule.wdh_ergebnis', true), '')::jsonb;
  perform set_config('schule.wdh_ergebnis', '', true);
  if v_w is not null then
    v_r := v_r || jsonb_build_object('wiederholung', jsonb_strip_nulls(jsonb_build_object('bestanden', v_w->'bestanden', 'sterne', v_w->'sterne',
                                       'stufe_neu', v_w->'stufe_neu', 'naechste_in', v_w->'naechste_in', 'mit_hilfe', v_w->'mit_hilfe')))
               || case when v_w ? 'abgelegt' then jsonb_build_object('abgelegt', v_w->'abgelegt') else '{}'::jsonb end;
  end if;
  if v_will and coalesce((v_r->>'format_ok')::boolean, false) and not coalesce((v_r->>'nochmal')::boolean, false) and not coalesce((v_r->>'wiederholt')::boolean, false) then
    v_r := v_r || jsonb_build_object('misch', coalesce(v_r->'misch', '{}'::jsonb) || jsonb_build_object('gueltig', v_gueltig,
             'sterne', (select coalesce(sum(s.menge), 0) from schule.sterne s where s.lernender_id = p_l) - v_s0));   -- in diesem Aufruf tatsächlich gebucht
  end if;
  return v_r;
end $function$;

-- Stellen in vorhandenen Funktionen ersetzen (wie WD-S 2): jede Stelle genau einmal, sonst Abbruch; schon eingespielt → nichts tun
create or replace function pg_temp.wd3_ersetzen(p_fn text, p_merkmal text, p_alt text[], p_neu text[])
 returns void language plpgsql as $f$
declare d text := pg_get_functiondef(p_fn::regprocedure); i int;
begin
  if position(p_merkmal in d) > 0 then raise notice '% schon umgebaut', p_fn; return; end if;
  for i in 1 .. cardinality(p_alt) loop
    if (length(d) - length(replace(d, p_alt[i], ''))) / length(p_alt[i]) <> 1 then
      raise exception '%: Stelle % nicht genau einmal gefunden: %', p_fn, i, left(p_alt[i], 80); end if;
    d := replace(d, p_alt[i], p_neu[i]);
  end loop;
  execute d;
end $f$;

-- Mischkarten-Auswahl: frische Aufgabe; nie aus einer Etappe von heute
select pg_temp.wd3_ersetzen('schule.mischkarten_waehlen(bigint, bigint, integer)', 'WD-S 3',
  array[$a$           (select a.id from schule.aufgabe a
             where a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel and a.pool = 'uebung' and a.stufe in (2, 3)
               and a.freigegeben -- gesperrte Aufgaben nie, auch nicht für das Testkind (Korrektur 18.11.); Entwurfs-Flüge des Testkinds über e.status unten
             order by (select count(*) from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id), random() limit 1) aufgabe_id$a$,
        $a$     where k.lernender_id = p_lernender and k.sitzt
       and (e.status in ('geprueft', 'freigegeben') or (e.status = 'entwurf' and (select test from ich))))$a$],
  array[$a$           schule.wdh_aufgabe_waehlen(p_lernender, k.einheit_id, k.lernziel, true) aufgabe_id -- WD-S 3: frisch, nie aus den letzten 3 Lerntagen$a$,
        $a$     where k.lernender_id = p_lernender and k.sitzt
       and not schule.etappe_heute_beantwortet(p_lernender, k.einheit_id, k.lernziel) -- WD-S 3: keine Etappe von heute
       and (e.status in ('geprueft', 'freigegeben') or (e.status = 'entwurf' and (select test from ich))))$a$]);

-- Ausgabe: offene Karten verfallen, wenn die Aufgabe schon beantwortet oder die Etappe heute schon dran war
select pg_temp.wd3_ersetzen('schule.mischkarten(bigint, bigint, integer)', 'WD-S 3',
  array[$a$          or not exists (select 1 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id$a$],
  array[$a$          or exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = m.aufgabe_id) -- WD-S 3: schon beantwortet
          or exists (select 1 from schule.aufgabe a where a.id = m.aufgabe_id and schule.etappe_heute_beantwortet(p_lernender, a.einheit_id, a.variante_gruppe)) -- WD-S 3: Etappe heute schon dran
          or not exists (select 1 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id$a$]);

-- Mischkarte mit Tipp/zweitem Versuch zählt als Antwort (Runde: bearbeitet); kein Beleg, kein Fortschritt
select pg_temp.wd3_ersetzen('schule.misch_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)', 'WD-S 3',
  array[$a$    end if; -- Tipp oder 2. Versuch: kein Beleg, nichts fällig$a$],
  array[$a$    else -- WD-S 3: Tipp oder 2. Versuch: kein Beleg, kein Fortschritt; zählt als Antwort (aus fälliger Etappe: am nächsten Lerntag wieder)
      update schule.karte_stand set richtig = richtig + 1, zuletzt = p_zeit
       where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
    end if;$a$]);

-- Lesend für den Haupt-Chat: gelandete Etappen mit weniger als 3 frischen Aufgaben (Stufe 2–3, nie beantwortet)
create or replace function schule.etappen_wenig_frisch(p_grenze integer default 3)
 returns table (lernender_id bigint, einheit_id bigint, lernziel text, etappe text, frisch integer, gesamt integer)
 language sql stable set search_path to ''
as $function$
  select k.lernender_id, k.einheit_id, k.lernziel,
         (select et->>'titel' from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') et where e.id = k.einheit_id and et->>'lernziel' = k.lernziel limit 1),
         count(a.id) filter (where not exists (select 1 from schule.versuch v where v.lernender_id = k.lernender_id and v.aufgabe_id = a.id))::int,
         count(a.id)::int
    from schule.karte_stand k join schule.lernender l on l.id = k.lernender_id and l.aktiv
    left join schule.aufgabe a on a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3)
   where k.sitzt
   group by k.lernender_id, k.einheit_id, k.lernziel
  having count(a.id) filter (where not exists (select 1 from schule.versuch v where v.lernender_id = k.lernender_id and v.aufgabe_id = a.id)) < p_grenze
   order by 1, 2, 3;
$function$;
revoke all on function schule.etappen_wenig_frisch(integer) from public, anon, authenticated;

-- Bestand unverändert?
do $mig$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from wd3_vorher v
   where v.s <> (select case v.t
       when 'karte' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x)
       when 'lernziel' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x)
       when 'sterne' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x) end);
  if v_t is not null then raise exception 'WD-S 3: Bestand verändert (%)', v_t; end if;
  raise notice 'WD-S 3: Karten, Lernstände, Sterne unverändert';
end $mig$;
