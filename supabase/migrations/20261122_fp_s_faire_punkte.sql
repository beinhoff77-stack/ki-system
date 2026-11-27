-- Bau-Auftrag FP (22.11.), Teil FP-S: faire Punkte. Entscheidung des Nutzers „Ja“ (inhalte/AUFTRAEGE.md „Bau-Auftrag FP – faire Punkte“).
-- Baut auf WD-S 2/3/4 auf. Reihenfolge beim Einspielen: WD-S 2, WD-S 3, WD-4b, WD-S 4 (20261122_wd_s4_nacharbeit_921.sql), dann diese Datei – in einer Transaktion.
-- Mit WD-S 4: Wiederholung oder Mischkarte mit Tipp / im zweiten Versuch gibt 0 Sterne; die 5 Sterne mit Hilfe (Regel 1) gelten nur beim normalen Üben.
--
-- Regeln:
--   1. Übungsaufgabe richtig im ersten Versuch ohne Tipp: sterne_uebung_richtig (10), je Aufgabe einmal wie bisher. Richtig im zweiten Versuch oder mit
--      Tipp: sterne_uebung_mit_hilfe (5). Je Aufgabe bleibt es bei einer Buchung (die erste richtige Antwort entscheidet). Gilt auch für Mischkarten,
--      die als Übung gebucht werden; Wiederholungen bleiben wie in WD (eigene Sterne, nur selbst gelöst). Knobeln (bonus) unverändert.
--   2. Landungs-Bonus je Kind und Etappe genau einmal, im Moment der Landung (karte_buchen → landung_speichern): ohne Fehler 80, mit 1–2 Fehlern 40,
--      sonst 10 (Regeln sterne_landung_ohne_fehler, sterne_landung_wenig_fehler, sterne_landung_sonst, landung_wenig_fehler_max).
--      Sterne-Grund 'landung', bezug 'landung:<einheit>:<etappe>' (eindeutig → doppelter Aufruf und gleichzeitige Antworten: genau eine Buchung).
--   3. Fehler = endgültig falsche Antworten auf Übungsaufgaben der Etappe bis zur Landung (ohne Tests, Wiederholungen, Mischkarten; ein Tipp ist kein
--      Fehler) – genau der Wert fehler_endgueltig, den landung_zaehlen seit AB-S für die Landungs-Art zählt (seit Beginn bzw. seit „wieder offen“).
--   4. Nachträglich: schule.landung_bonus_nachbuchen() bucht den Bonus für alle schon echt gelandeten Etappen (nicht über „Kann er“ gesetzt:
--      gesetzt_am ist leer); Fehler aus der gespeicherten Landung, sonst neu gezählt. Einmalig (zweiter Lauf bucht nichts). Schon gebuchte Sterne werden
--      nie gekürzt; Regel 1 gilt erst ab Einspielen. Der Haupt-Chat führt die Nachbuchung nach Probelauf aus.
--   Antworten: schule_uebung_pruefen liefert immer sterne (in diesem Aufruf tatsächlich gebucht) und bei der Landung landung.bonus/fehler/stufe
--   ('ohne' | 'wenig' | 'sonst'). schule_konto liefert regeln {…} und landung_nachbuchung {etappen, sterne, am} (für den einmaligen Hinweis der App).
-- Kein DROP einer Tabelle/Spalte, kein DELETE. Bestand: Karten, Lernstände, Sterne unverändert (am Ende geprüft). Wiederholt ausführbar.

create temp table if not exists fp_vorher (t text, s text) on commit drop;
truncate fp_vorher; -- nur die Hilfstabelle dieser Sitzung
insert into fp_vorher
  select 'karte', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x
  union all select 'lernziel', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x
  union all select 'sterne', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x;

insert into schule.regel (schluessel, wert, hinweis) values
  ('sterne_uebung_mit_hilfe', '5', 'FP: Übungsaufgabe richtig im zweiten Versuch oder mit Tipp'),
  ('sterne_landung_ohne_fehler', '80', 'FP: Landungs-Bonus ohne Fehler'),
  ('sterne_landung_wenig_fehler', '40', 'FP: Landungs-Bonus mit 1 bis landung_wenig_fehler_max Fehlern'),
  ('sterne_landung_sonst', '10', 'FP: Landungs-Bonus sonst'),
  ('landung_wenig_fehler_max', '2', 'FP: höchstens so viele Fehler für den mittleren Bonus')
on conflict (schluessel) do nothing;

-- Prüfregel der Sterne-Gründe um 'landung' erweitern (Constraint ersetzen; bestehende Gründe bleiben)
do $mig$
declare d text := (select pg_get_constraintdef(c.oid) from pg_constraint c where c.conrelid = 'schule.sterne'::regclass and c.conname = 'sterne_grund_check');
begin
  if d is not null and position('''landung''' in d) > 0 then return; end if;
  if d is distinct from $a$CHECK ((grund = ANY (ARRAY['uebung'::text, 'test'::text, 'ort'::text, 'einloesung'::text, 'korrektur_hand'::text, 'bonus'::text, 'expedition'::text, 'wdh'::text, 'etappe_abgelegt'::text, 'flug_abgelegt'::text])))$a$ then
    raise exception 'sterne_grund_check unerwartet (%) – ist WD-S 2 eingespielt?', d; end if;
  alter table schule.sterne drop constraint if exists sterne_grund_check;
  alter table schule.sterne add constraint sterne_grund_check check (grund = any (array['uebung', 'test', 'ort', 'einloesung', 'korrektur_hand', 'bonus', 'expedition',
                                                                                       'wdh', 'etappe_abgelegt', 'flug_abgelegt', 'landung']));
end $mig$;

-- Regeln für die App (schule_konto)
create or replace function schule.sterne_regeln()
 returns jsonb language sql stable set search_path to ''
as $function$
  select jsonb_build_object('sterne_uebung_richtig', schule.wd_regel('sterne_uebung_richtig', 10), 'sterne_uebung_mit_hilfe', schule.wd_regel('sterne_uebung_mit_hilfe', 5),
    'sterne_landung_ohne_fehler', schule.wd_regel('sterne_landung_ohne_fehler', 80), 'sterne_landung_wenig_fehler', schule.wd_regel('sterne_landung_wenig_fehler', 40),
    'sterne_landung_sonst', schule.wd_regel('sterne_landung_sonst', 10), 'landung_wenig_fehler_max', schule.wd_regel('landung_wenig_fehler_max', 2),
    'sterne_wdh_richtig', schule.wd_regel('sterne_wdh_richtig', 10), 'sterne_etappe_abgelegt', schule.wd_regel('sterne_etappe_abgelegt', 30),
    'sterne_flug_abgelegt', schule.wd_regel('sterne_flug_abgelegt', 100));
$function$;

-- Landungs-Bonus (einmal je Kind und Etappe); liefert {bonus, fehler, stufe} oder null (schon gebucht, gesetzte Etappe, nicht gelandet)
create or replace function schule.landung_bonus(p_l bigint, p_e bigint, p_lz text, p_landung jsonb default null)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare k schule.karte_stand; v_fehler int; v_stufe text; v_bonus int; v_menge int;
begin
  select * into k from schule.karte_stand where lernender_id = p_l and einheit_id = p_e and lernziel = p_lz;
  if k.lernender_id is null or not k.sitzt or k.gesetzt_am is not null then return null; end if;    -- nur echte Landungen
  v_fehler := coalesce((coalesce(p_landung, k.landung, schule.landung_zaehlen(p_l, p_e, p_lz))->>'fehler_endgueltig')::int, 0);
  v_stufe := case when v_fehler = 0 then 'ohne' when v_fehler <= schule.wd_regel('landung_wenig_fehler_max', 2) then 'wenig' else 'sonst' end;
  v_bonus := case v_stufe when 'ohne' then schule.wd_regel('sterne_landung_ohne_fehler', 80) when 'wenig' then schule.wd_regel('sterne_landung_wenig_fehler', 40)
                          else schule.wd_regel('sterne_landung_sonst', 10) end;
  insert into schule.sterne (lernender_id, menge, grund, bezug) values (p_l, v_bonus, 'landung', 'landung:' || p_e || ':' || p_lz)
  on conflict do nothing returning menge into v_menge;
  if v_menge is null then return null; end if;
  return jsonb_build_object('bonus', v_menge, 'fehler', v_fehler, 'stufe', v_stufe);
end $function$;
revoke all on function schule.landung_bonus(bigint, bigint, text, jsonb) from public, anon, authenticated;

-- Stellen ersetzen (wie WD-S): jede Stelle genau einmal, sonst Abbruch; schon eingespielt → nichts tun
create or replace function pg_temp.fp_ersetzen(p_fn text, p_merkmal text, p_alt text[], p_neu text[])
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

-- Regel 1: 10 nur im ersten Versuch ohne Tipp, sonst 5 (je Aufgabe einmal)
select pg_temp.fp_ersetzen('schule.sterne_aus_versuch()', 'sterne_uebung_mit_hilfe',
  array[$a$      values (new.lernender_id, schule.sterne_regel('sterne_uebung_richtig'), 'uebung', 'aufgabe:' || new.aufgabe_id)$a$],
  array[$a$      values (new.lernender_id, case when coalesce(new.hilfe, 0) = 0 and coalesce(new.anlauf, 1) = 1 then schule.sterne_regel('sterne_uebung_richtig')
                                     else schule.wd_regel('sterne_uebung_mit_hilfe', 5) end, 'uebung', 'aufgabe:' || new.aufgabe_id) -- FP: 10 selbst, sonst 5$a$]);

-- Regel 2: Bonus im Moment der Landung (landung_speichern wird nur bei einer echten Landung aus karte_buchen gerufen)
select pg_temp.fp_ersetzen('schule.landung_speichern(bigint, bigint, text)', 'landung_bonus',
  array[$a$  update schule.karte_stand set landung_art = v->>'landung_art', landung = v
   where lernender_id = p_l and einheit_id = p_e and lernziel = p_lz;$a$],
  array[$a$  update schule.karte_stand set landung_art = v->>'landung_art', landung = v
   where lernender_id = p_l and einheit_id = p_e and lernziel = p_lz;
  perform set_config('schule.landung_ergebnis', coalesce(schule.landung_bonus(p_l, p_e, p_lz, v)::text, ''), true); -- FP: Landungs-Bonus$a$]);

-- Antwort der Übung (wie WD-S 3) + sterne (immer, tatsächlich gebucht) + landung {bonus, fehler, stufe}
create or replace function schule.uebung_pruefen_wd(p_l bigint, p_daten jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_r jsonb; v_w jsonb; v_lb jsonb; v_a schule.aufgabe; v_will boolean := coalesce((p_daten->>'misch')::boolean, false); v_gueltig boolean := false;
  v_s0 bigint := (select coalesce(sum(s.menge), 0) from schule.sterne s where s.lernender_id = p_l); v_gebucht bigint;
begin
  if v_will then
    select * into v_a from schule.aufgabe where id = nullif(p_daten->>'aufgabe_id', '')::bigint;
    v_gueltig := v_a.id is not null and schule.misch_gueltig(p_l, v_a, p_daten);   -- vor dem Speichern prüfen (danach ist die Ausgabe eingelöst)
  end if;
  perform set_config('schule.wdh_ergebnis', '', true);
  perform set_config('schule.landung_ergebnis', '', true);
  perform set_config('schule.kein_wdh', case when v_will and not v_gueltig then '1' else '' end, true);
  v_r := schule.uebung_pruefen_intern(p_l, p_daten);
  perform set_config('schule.kein_wdh', '', true);
  v_w := nullif(current_setting('schule.wdh_ergebnis', true), '')::jsonb;
  v_lb := nullif(current_setting('schule.landung_ergebnis', true), '')::jsonb;
  perform set_config('schule.wdh_ergebnis', '', true);
  perform set_config('schule.landung_ergebnis', '', true);
  v_gebucht := (select coalesce(sum(s.menge), 0) from schule.sterne s where s.lernender_id = p_l) - v_s0;
  if v_w is not null then
    v_r := v_r || jsonb_build_object('wiederholung', jsonb_strip_nulls(jsonb_build_object('bestanden', v_w->'bestanden', 'sterne', v_w->'sterne',
                                       'stufe_neu', v_w->'stufe_neu', 'naechste_in', v_w->'naechste_in', 'mit_hilfe', v_w->'mit_hilfe')))
               || case when v_w ? 'abgelegt' then jsonb_build_object('abgelegt', v_w->'abgelegt') else '{}'::jsonb end;
  end if;
  if v_lb is not null then
    v_r := v_r || jsonb_build_object('landung', coalesce(v_r->'landung', '{}'::jsonb) || v_lb);   -- FP: Bonus zur Landungs-Einblendung
  end if;
  if v_will and coalesce((v_r->>'format_ok')::boolean, false) and not coalesce((v_r->>'nochmal')::boolean, false) and not coalesce((v_r->>'wiederholt')::boolean, false) then
    v_r := v_r || jsonb_build_object('misch', coalesce(v_r->'misch', '{}'::jsonb) || jsonb_build_object('gueltig', v_gueltig, 'sterne', v_gebucht));
  end if;
  if coalesce((v_r->>'format_ok')::boolean, false) and not coalesce((v_r->>'wiederholt')::boolean, false) then
    v_r := v_r || jsonb_build_object('sterne', v_gebucht);                                          -- FP: tatsächlich gebucht (die App rechnet nichts selbst)
  end if;
  return v_r;
end $function$;

-- Hinweis für die App nach der Nachbuchung (je Kind einmal)
create table if not exists schule.landung_nachbuchung (
  lernender_id bigint primary key references schule.lernender(id),
  etappen integer not null, sterne integer not null,
  am timestamptz not null default now()
);
comment on table schule.landung_nachbuchung is 'FP: nachträglich gebuchte Landungs-Boni je Kind (für den einmaligen Hinweis der App)';
alter table schule.landung_nachbuchung enable row level security;
revoke all on table schule.landung_nachbuchung from public, anon, authenticated;

-- Regel 4: Nachbuchung (einmalig; zweiter Lauf bucht nichts). Liefert je Kind die neu gebuchten Etappen und Sterne (nur Nummern).
create or replace function schule.landung_bonus_nachbuchen(p_l bigint default null)
 returns table (lernender_id bigint, etappen integer, sterne integer)
 language plpgsql set search_path to ''
as $function$
declare k record; v jsonb; v_n int; v_s int; v_kind bigint;
begin
  for v_kind in select l.id from schule.lernender l where (p_l is null or l.id = p_l) order by l.id loop
    v_n := 0; v_s := 0;
    for k in select x.einheit_id, x.lernziel from schule.karte_stand x
              where x.lernender_id = v_kind and x.sitzt and x.gesetzt_am is null
                and not exists (select 1 from schule.sterne s where s.lernender_id = x.lernender_id and s.grund = 'landung' and s.bezug = 'landung:' || x.einheit_id || ':' || x.lernziel)
              order by x.einheit_id, x.lernziel loop
      v := schule.landung_bonus(v_kind, k.einheit_id, k.lernziel, null);
      if v is not null then v_n := v_n + 1; v_s := v_s + (v->>'bonus')::int; end if;
    end loop;
    if v_n > 0 then
      insert into schule.landung_nachbuchung (lernender_id, etappen, sterne) values (v_kind, v_n, v_s) on conflict do nothing;
      lernender_id := v_kind; etappen := v_n; sterne := v_s; return next;
    end if;
  end loop;
end $function$;
revoke all on function schule.landung_bonus_nachbuchen(bigint) from public, anon, authenticated;

-- schule_konto: Regeln und Nachbuchungs-Hinweis mitgeben
select pg_temp.fp_ersetzen('api.schule_konto(text, jsonb)', 'sterne_regeln',
  array[$a$'konto', schule.konto_wd(v_l), -- WD-S: + fluege[], orte[].gold$a$],
  array[$a$'konto', schule.konto_wd(v_l), -- WD-S: + fluege[], orte[].gold
    'regeln', schule.sterne_regeln(), -- FP
    'landung_nachbuchung', (select jsonb_build_object('etappen', n.etappen, 'sterne', n.sterne, 'am', n.am) from schule.landung_nachbuchung n where n.lernender_id = v_l), -- FP$a$]);

-- Bestand unverändert?
do $mig$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from fp_vorher v
   where v.s <> (select case v.t
       when 'karte' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x)
       when 'lernziel' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x)
       when 'sterne' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x) end);
  if v_t is not null then raise exception 'FP-S: Bestand verändert (%)', v_t; end if;
  raise notice 'FP-S: Karten, Lernstände, Sterne unverändert (Nachbuchung nicht ausgeführt)';
end $mig$;
