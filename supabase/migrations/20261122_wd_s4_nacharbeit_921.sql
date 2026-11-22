-- WD-S 4 (22.11.): Nacharbeit aus ChatGPT 921 (inhalte/AUFTRAEGE.md „Nachtrag WD-S 4 – Rückläufer ChatGPT 921“, Teil „An bau-lehrer“).
-- Nach 20261122_wd_s_wiederholungen.sql, 20261122_wd_s3_frische_aufgaben.sql und 20261122_wd_4b_stau_strecken.sql einspielen (eine Transaktion);
-- vor 20261122_fp_s_faire_punkte.sql. Die schon gelieferten Migrationen bleiben unverändert.
--   1. Mischkarte beim Einlösen prüfen: misch_gueltig verlangt zusätzlich, dass seit der Ausgabe keine ANDERE Aufgabe derselben Etappe beantwortet wurde
--      (der zweite Anlauf derselben Mischkarte bleibt möglich). Sonst: misch.gueltig = false, keine Wiederholung (WD-S 3).
--   2. Wiederholung oder Mischkarte mit Tipp / im zweiten Versuch: 0 Sterne – auch keine Übungssterne. Fällige Wiederholung: karte_wdh_ereignis setzt
--      dafür die Markierung, die sterne_aus_versuch schon für bestandene Wiederholungen nutzt; Mischkarte (gültig): sterne_aus_versuch prüft Hilfe/Anlauf.
--      Ungültige Mischkarte zählt als normales Üben (wie bisher). Antwort und Konto stimmen überein (beide lesen schule.sterne).
--   3. Runden-Abschluss serialisiert: wdh_runde_pruefen sperrt die Runden-Zeile vor dem Zählen.
--   4. wdh_staffel_strecken / wdh_staffel_zurueck sperren die Karten in fester Reihenfolge (for update) und prüfen/schreiben unter der Sperre.
--   5. wdh_aufgabe_da als deterministisches EXISTS (ohne Zufallswahl).
--   6. Rechte: alle schule.*-Helfer aus WD-S 2/3/4 ohne Rechte für public, anon, authenticated.
-- Kein DROP einer Tabelle/Spalte, kein DELETE. Bestand: Karten, Lernstände, Sterne unverändert (am Ende geprüft). Wiederholt ausführbar.

create temp table if not exists wd4_vorher (t text, s text) on commit drop;
truncate wd4_vorher; -- nur die Hilfstabelle dieser Sitzung
insert into wd4_vorher
  select 'karte', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x
  union all select 'lernziel', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x
  union all select 'sterne', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x;

create or replace function pg_temp.wd4_ersetzen(p_fn text, p_merkmal text, p_alt text[], p_neu text[])
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

-- 1. Mischkarte beim Einlösen prüfen
select pg_temp.wd4_ersetzen('schule.misch_gueltig(bigint, schule.aufgabe, jsonb)', 'WD-S 4',
  array[$a$                   and m.ausgegeben_am >= now() - interval '24 hours'$a$],
  array[$a$                   and m.ausgegeben_am >= now() - interval '24 hours'
                   and not exists (select 1 from schule.versuch v join schule.aufgabe b on b.id = v.aufgabe_id -- WD-S 4: seit der Ausgabe eine andere Aufgabe der Etappe
                                    where v.lernender_id = p_lernender and b.einheit_id = a.einheit_id and b.variante_gruppe = a.variante_gruppe
                                      and v.aufgabe_id <> a.id and v.am > m.ausgegeben_am)$a$]);

-- 2. Mischkarte mit Tipp / im zweiten Versuch: keine Übungssterne
select pg_temp.wd4_ersetzen('schule.sterne_aus_versuch()', 'WD-S 4',
  array[$a$    elsif v_wdh <> '' and v_wdh = (select a.einheit_id || '/' || a.variante_gruppe from schule.aufgabe a where a.id = new.aufgabe_id) then$a$],
  array[$a$    elsif (v_wdh <> '' and v_wdh = (select a.einheit_id || '/' || a.variante_gruppe from schule.aufgabe a where a.id = new.aufgabe_id))
       or (coalesce(new.misch, false) and (coalesce(new.hilfe, 0) > 0 or coalesce(new.anlauf, 1) = 2)) then -- WD-S 4: Mischkarte mit Hilfe 0 Sterne$a$]);

-- 2. Fällige Wiederholung mit Tipp / im zweiten Versuch: 0 Sterne
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
  -- WD-S 3/4: richtig mit Tipp oder im zweiten Versuch – kein Fortschritt, kein Fehler, keine Sterne, am nächsten Lerntag wieder
  if new.richtig > old.richtig and v_hilfe and v_nur_selbst then
    new.wdh_stufe := old.wdh_stufe; new.wdh_fehler := old.wdh_fehler; new.sitzt := old.sitzt;
    new.wdh_ab := now(); new.wdh_lerntage := 1; new.faellig_am := now() + interval '1 day';
    perform set_config('schule.wdh_ergebnis', jsonb_build_object('bestanden', false, 'sterne', 0, 'stufe_neu', new.wdh_stufe, 'naechste_in', 1,
                                                                  'einheit_id', new.einheit_id, 'lernziel', new.lernziel, 'mit_hilfe', true)::text, true);
    perform set_config('schule.wdh_karte', new.einheit_id || '/' || new.lernziel, true);  -- WD-S 4: mit Hilfe 0 Sterne (auch keine Übungssterne)
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

-- 3. Runden-Abschluss unter Sperre
create or replace function schule.wdh_runde_pruefen(p_l bigint, p_tag date)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_offen int;
begin
  -- WD-S 4: Abschluss je Kind und Tag serialisieren – erst die Runden-Zeile sperren, dann zählen (gleichzeitige letzte Antworten sehen einander)
  perform 1 from schule.wdh_runde w where w.lernender_id = p_l and w.tag = p_tag for update;
  select count(*) into v_offen from schule.wdh_runde_etappe r
   where r.lernender_id = p_l and r.tag = p_tag and r.bearbeitet_am is null and schule.wdh_aufgabe_da(p_l, r.einheit_id, r.lernziel);
  if v_offen = 0 then
    update schule.wdh_runde set fertig_am = now() where lernender_id = p_l and tag = p_tag and fertig_am is null;
  end if;
  return v_offen;
end $function$;

-- 4. Staffel-Funktionen unter Sperre
create or replace function schule.wdh_staffel_strecken(p_l bigint default null)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_je int := greatest(schule.wd_regel('wdh_gesetzt_je_lerntag', 6), 1); v_kind bigint; k record; v_belegt int[]; v_heute int; d int; v_n int := 0;
begin
  for v_kind in select l.id from schule.lernender l where (p_l is null or l.id = p_l) order by l.id loop
    -- WD-S 4: alle Karten des Kindes in fester Reihenfolge sperren; unter der Sperre prüfen und schreiben
    perform 1 from schule.karte_stand x where x.lernender_id = v_kind order by x.einheit_id, x.lernziel for update;
    -- schon geplante erste Wiederholungen gesetzter Etappen je künftigem Lerntag (1 = nächster Lerntag)
    select coalesce(array_agg(schule.karte_wdh_in(x)), '{}') into v_belegt from schule.karte_stand x
     where x.lernender_id = v_kind and x.sitzt and x.wdh_gesetzt_am is not null and x.wdh_stufe = 0 and x.wdh_fehler = 0 and not schule.karte_faellig(x);
    -- heute belegt: gesetzte fällige Etappen in der offenen Runde von heute
    select count(*) into v_heute from schule.karte_stand x
      join schule.wdh_runde_etappe r on r.lernender_id = x.lernender_id and r.einheit_id = x.einheit_id and r.lernziel = x.lernziel and r.tag = schule.heute_tag(v_kind)
      join schule.wdh_runde w on w.lernender_id = r.lernender_id and w.tag = r.tag and w.fertig_am is null
     where x.lernender_id = v_kind and x.sitzt and x.wdh_gesetzt_am is not null and x.wdh_stufe = 0 and x.wdh_fehler = 0 and schule.karte_faellig(x);
    for k in
      select x.einheit_id, x.lernziel, x.faellig_am, x.wdh_ab, x.wdh_lerntage, x.richtig, x.falsch
        from schule.karte_stand x join schule.einheit e on e.id = x.einheit_id
       where x.lernender_id = v_kind and x.sitzt and x.wdh_gesetzt_am is not null and x.wdh_stufe = 0 and x.wdh_fehler = 0 and schule.karte_faellig(x)
         and not exists (select 1 from schule.wdh_runde_etappe r join schule.wdh_runde w on w.lernender_id = r.lernender_id and w.tag = r.tag and w.fertig_am is null
                          where r.lernender_id = x.lernender_id and r.tag = schule.heute_tag(v_kind) and r.einheit_id = x.einheit_id and r.lernziel = x.lernziel)
       order by coalesce((select min(ro.position) from schule.route ro where ro.lernender_id = x.lernender_id and ro.block_id = e.block_id and ro.art = 'normal'), 2147483647),
                e.id, coalesce((select et.nr from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality et(y, nr) where et.y->>'lernziel' = x.lernziel), 999),
                x.lernziel loop
      if v_heute < v_je then v_heute := v_heute + 1; continue; end if;      -- bleibt heute fällig
      d := 1;
      while (select count(*) from unnest(v_belegt) b where b = d) >= v_je loop d := d + 1; end loop;
      v_belegt := v_belegt || d;
      insert into schule.wdh_staffel_sicherung (lernender_id, einheit_id, lernziel, faellig_am, wdh_ab, wdh_lerntage, richtig, falsch, wdh_ab_neu)
      values (v_kind, k.einheit_id, k.lernziel, k.faellig_am, k.wdh_ab, k.wdh_lerntage, k.richtig, k.falsch, now())
      on conflict do nothing;
      update schule.karte_stand set wdh_ab = now(), wdh_lerntage = d, faellig_am = now() + d * interval '1 day'
       where lernender_id = v_kind and einheit_id = k.einheit_id and lernziel = k.lernziel;
      v_n := v_n + 1;
    end loop;
  end loop;
  return v_n;
end $function$;

create or replace function schule.wdh_staffel_zurueck(p_l bigint default null)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_geuebt int; v_n int;
begin
  -- WD-S 4: betroffene Karten (und Sicherungen) in fester Reihenfolge sperren; unter der Sperre prüfen und schreiben
  perform 1 from schule.karte_stand k join schule.wdh_staffel_sicherung s on s.lernender_id = k.lernender_id and s.einheit_id = k.einheit_id and s.lernziel = k.lernziel
   where s.zurueck_am is null and (p_l is null or s.lernender_id = p_l) order by k.lernender_id, k.einheit_id, k.lernziel for update of k, s;
  select count(*) into v_geuebt from schule.wdh_staffel_sicherung s join schule.karte_stand k
      on k.lernender_id = s.lernender_id and k.einheit_id = s.einheit_id and k.lernziel = s.lernziel
   where s.zurueck_am is null and (p_l is null or s.lernender_id = p_l)
     and (k.richtig is distinct from s.richtig or k.falsch is distinct from s.falsch or k.wdh_ab is distinct from s.wdh_ab_neu);
  if v_geuebt > 0 then
    raise exception 'WD-4b Rückweg abgelehnt: % gestreckte Etappen wurden inzwischen geübt', v_geuebt using errcode = 'P0001';
  end if;
  update schule.karte_stand k set faellig_am = s.faellig_am, wdh_ab = s.wdh_ab, wdh_lerntage = s.wdh_lerntage
    from schule.wdh_staffel_sicherung s
   where s.lernender_id = k.lernender_id and s.einheit_id = k.einheit_id and s.lernziel = k.lernziel and s.zurueck_am is null and (p_l is null or s.lernender_id = p_l);
  get diagnostics v_n = row_count;
  update schule.wdh_staffel_sicherung set zurueck_am = now() where zurueck_am is null and (p_l is null or lernender_id = p_l);
  return v_n;
end $function$;

-- 5. deterministisch: gibt es heute eine wählbare Aufgabe? (dieselbe Bedingung wie wdh_aufgabe_waehlen, ohne Zufall)
create or replace function schule.wdh_aufgabe_da(p_l bigint, p_e bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.einheit e where e.id = p_e and e.status in ('geprueft', 'freigegeben'))
     and exists (select 1 from schule.aufgabe a
                  where a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung' and a.freigegeben
                    and not exists (select 1 from schule.versuch v where v.lernender_id = p_l and v.aufgabe_id = a.id
                                      and schule.lern_datum(p_l, v.am) >= schule.wdh_sperre_ab(p_l)));
$function$;

-- 6. Rechte der Helfer
do $mig$
declare f text;
begin
  foreach f in array array[
    'schule.wd_regel(text, integer)', 'schule.wdh_runde_groesse(bigint, integer)', 'schule.wdh_staffel_tag(bigint)', 'schule.wdh_ablegen(bigint, bigint, text)',
    'schule.karte_wdh_ereignis()', 'schule.lernziel_rueckfall()', 'schule.wdh_aufgabe_da(bigint, bigint, text)', 'schule.wdh_aufgabe_da(bigint, text)',
    'schule.wdh_runde_pruefen(bigint, date)', 'schule.wdh_fehler(schule.karte_stand)', 'schule.wdh_runde_holen(bigint, date)',
    'schule.wiederholung_intern(bigint, jsonb, boolean, date)', 'schule.wiederholung_intern(bigint, jsonb, boolean)', 'schule.wdh_runde_fertig(bigint, date)',
    'schule.wdh_runde_fertig(bigint)', 'schule.uebung_pruefen_wd(bigint, jsonb)', 'schule.konto_wd(bigint)', 'schule.wdh_sperre_ab(bigint)',
    'schule.lern_datum(bigint, timestamp with time zone)', 'schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)',
    'schule.etappe_heute_beantwortet(bigint, bigint, text)', 'schule.versuch_hilfe_merken()', 'schule.versuch_misch_verfall()',
    'schule.etappen_wenig_frisch(integer)', 'schule.wdh_staffel_strecken(bigint)', 'schule.wdh_staffel_zurueck(bigint)'] loop
    if to_regprocedure(f) is not null then
      execute format('revoke all on function %s from public, anon, authenticated', f);
    end if;
  end loop;
end $mig$;

-- Bestand unverändert?
do $mig$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from wd4_vorher v
   where v.s <> (select case v.t
       when 'karte' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x)
       when 'lernziel' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x)
       when 'sterne' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x) end);
  if v_t is not null then raise exception 'WD-S 4: Bestand verändert (%)', v_t; end if;
  raise notice 'WD-S 4: Karten, Lernstände, Sterne unverändert';
end $mig$;
