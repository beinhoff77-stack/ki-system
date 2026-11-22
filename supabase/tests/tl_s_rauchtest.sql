-- Rauchtest TL-S (Teilung 7 Themen → 15 Teile, 8 neue Flüge) mit LW-Rest, Kür je Gruppe (TL-S 5: fünf Gruppen, leere Pflichtliste, Ein-Etappen-Flug). Reihenfolge: … LK-S → LK-D Einspiel → TL-S.
-- Voraussetzung: LK-S und LW-S/LW-S 2 sind eingespielt. Aufruf: psql -v ON_ERROR_STOP=1 -f supabase/tests/tl_s_rauchtest.sql (aus dem Repo-Wurzelverzeichnis).
-- Unabhängig vom Bestand: alte Antworten werden vor dem Teilen erfasst und danach gegen die Teile geprüft; die Besprochen-Regression nutzt nur das Testkind.
-- Keine Namen, keine Kinderdaten in der Ausgabe (nur Zahlen).
begin;

-- B3b: alte Antworten vorher erfassen (Antwort → Etappe → altes Thema) und „Was wackelt“-Fehler je Kind und altem Thema
create temp table tl_rt_versuch on commit drop as
  select v.id, v.lernender_id, case when a.pool = 'expedition' then null else a.variante_gruppe end lz, coalesce((to_jsonb(t)->>'teil_stamm')::bigint, t.id) stamm
    from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id join schule.einheit e on e.id = a.einheit_id join schule.thema t on t.id = e.thema_id
   where coalesce((to_jsonb(t)->>'teil_stamm')::bigint, t.id) in (26, 29, 44, 46, 61, 91, 101);
create temp table tl_rt_wackelt on commit drop as
  select l.id lernender_id, s.stamm, (select sum(f.anzahl) from schule.thema t2, schule.wackelt_fehler(l.id, t2.id, null::bigint, null::text) f
                                       where coalesce((to_jsonb(t2)->>'teil_stamm')::bigint, t2.id) = s.stamm) fehler
    from schule.lernender l cross join (values (26), (29), (44), (46), (61), (91), (101)) s(stamm);

-- TL-S 3: Setzung, Plan und Rückreise je Kind und altem Thema vorher (Fälle: gesetzt komplett, gesetzt mit Wiederholung, im Plan nicht begonnen, Rückreise)
create temp table tl_rt_stufe on commit drop as
  select l.id lernender_id, s.stamm, schule.thema_stufe(l.id, s.stamm) st
    from schule.lernender l cross join (values (26), (29), (44), (46), (61), (91), (101)) s(stamm)
   where coalesce((select (to_jsonb(t)->>'teil_nr')::int from schule.thema t where t.id = s.stamm), 1) = 1;

-- TL-S 7 (A1) Negativfälle vor der Teilung, nur Testkind: a) Thema 26 – alle Karten selbst gelandet, Lernziele „nachgewiesen“, aber kein alter Flug-Test;
--   b) Thema 61 – alter Flug-Test abgeschlossen, aber nur mit Aufgabe zu einer Etappe (laplace). Erwartet: kein Abschluss, keine Sterne für die neuen Teile.
do $$
declare v_l bigint; v_e bigint; v_s bigint;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if to_regclass('schule.visum_uebergang') is not null then return; end if;   -- schon geteilt: Fälle entfallen
  foreach v_e in array array[(select schule.thema_einheit(26)), (select schule.thema_einheit(61))] loop
    insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am)
    select v_l, v_e, x->>'lernziel', true, now() - interval '30 days' from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = v_e
    on conflict (lernender_id, einheit_id, lernziel) do update set sitzt = true, sitzt_am = excluded.sitzt_am, gesetzt_am = null;
    insert into schule.lernziel_stand (lernender_id, einheit_id, lernziel, pflicht, status)
    select v_l, v_e, x->>'lernziel', true, 'nachgewiesen' from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = v_e
    on conflict (lernender_id, einheit_id, lernziel) do update set status = 'nachgewiesen';
  end loop;
  v_e := schule.thema_einheit(61);
  insert into schule.testsitzung (lernender_id, art, einheit_id, thema_id, aufgaben, status, gestartet_am, abgeschlossen_am)
  values (v_l, 'blocktest', v_e, 61, array(select a.id from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = 'laplace' and a.pool = 'test' limit 1),
          'abgeschlossen', now() - interval '20 days', now() - interval '20 days') returning id into v_s;
  insert into schule.versuch (lernender_id, aufgabe_id, testsitzung_id, client_id, richtig, punkte, punkte_max, hilfe, versuch_nr, am)
  select v_l, x, v_s, 'tl-rt-a1-' || x, true, 1, 1, 0, 1, now() - interval '20 days' from unnest((select aufgaben from schule.testsitzung where id = v_s)) x;
end $$;
create temp table tl_rt_a1 on commit drop as
  select (select id from schule.lernender where ist_test and aktiv order by id limit 1) l, (select count(*) from schule.sterne s where s.lernender_id =
          (select id from schule.lernender where ist_test and aktiv order by id limit 1)) sterne;

\ir ../migrations/20261123_tl_s_teilung.sql

do $$
declare v_n int; v_t text; v_l bigint; v_e bigint; v_lz text; v_a bigint; v_a2 bigint; v_b schule.besprochen; v_lz2 text;
  v_sa text; v_sa2 text; v_et text[]; v_st0 bigint; v_k0 bigint;
begin
  -- 1 Zahl: 15 Teile, 8 neue Flüge, je Thema Teile 1..n lückenlos, Titel „– Teil k von n“, Untertitel gesetzt
  select count(*) into v_n from schule.thema where teil_stamm in (26, 29, 44, 46, 61, 91, 101);
  if v_n <> 15 then raise exception 'FEHLER 1: % Teile statt 15', v_n; end if;
  select count(*) into v_n from schule.thema where teil_stamm in (26, 29, 44, 46, 61, 91, 101) and teil_nr > 1;
  if v_n <> 8 then raise exception 'FEHLER 1: % neue Flüge statt 8', v_n; end if;
  select string_agg(id::text, ',') into v_t from schule.thema
   where teil_stamm in (26, 29, 44, 46, 61, 91, 101) and (unterthema not like '% – Teil ' || teil_nr || ' von ' || teil_von or coalesce(untertitel, '') = '');
  if v_t is not null then raise exception 'FEHLER 1: Titel/Untertitel falsch bei Thema %', v_t; end if;
  if (select count(*) from schule.thema where teil_stamm = 46) <> 3 then raise exception 'FEHLER 1: Thema 46 hat nicht 3 Teile'; end if;

  -- 2 Katalog: jede Etappe in genau einem Teil; jeder Teil freigegeben mit eigener Einheit, eigenem Ort und Test-Aufgaben
  select string_agg(x.lz, ',') into v_t from (
    select q->>'lernziel' lz, t.teil_stamm from schule.thema t join schule.einheit e on e.thema_id = t.id, jsonb_array_elements(e.inhalt->'etappen') q
     where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101) group by 1, 2 having count(*) > 1) x;
  if v_t is not null then raise exception 'FEHLER 2: Etappe in mehreren Teilen: %', v_t; end if;
  -- leere Hüllen (Etappen noch nicht in der Datenbank, z. B. 101 Teil 2): Entwurf, in keinem Plan
  select string_agg(t.id::text, ',') into v_t from schule.thema t join schule.einheit e on e.thema_id = t.id
   where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101) and jsonb_array_length(coalesce(e.inhalt->'etappen', '[]'::jsonb)) = 0
     and (e.status = 'freigegeben' or exists (select 1 from schule.route r join schule.block_thema bt on bt.block_id = r.block_id and bt.thema_id = t.id));
  if v_t is not null then raise exception 'FEHLER 2: leerer Teil freigegeben oder im Plan: %', v_t; end if;
  -- T4: Reihenfolge LK-D Einspiel vor TL-S → kein Teil ohne Etappen
  select string_agg(t.id::text, ',') into v_t from schule.thema t join schule.einheit e on e.thema_id = t.id
   where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101) and jsonb_array_length(coalesce(e.inhalt->'etappen', '[]'::jsonb)) = 0;
  if v_t is not null then raise exception 'FEHLER 2 (T4): Teil ohne Etappen – LK-D Einspiel vor TL-S fehlt: %', v_t; end if;
  raise notice 'TL-S Rauchtest 2: leere Teile (warten auf Etappen): %', (select count(*) from schule.thema t join schule.einheit e on e.thema_id = t.id
     where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101) and jsonb_array_length(coalesce(e.inhalt->'etappen', '[]'::jsonb)) = 0);
  select string_agg(t.id::text, ',') into v_t from schule.thema t
   where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101)
     and not exists (select 1 from schule.einheit e where e.thema_id = t.id and jsonb_array_length(coalesce(e.inhalt->'etappen', '[]'::jsonb)) = 0)
     and (schule.thema_einheit(t.id) is null
          or not exists (select 1 from schule.einheit e where e.id = schule.thema_einheit(t.id) and e.status = 'freigegeben')
          or not exists (select 1 from schule.block_thema bt where bt.thema_id = t.id)
          or not exists (select 1 from schule.aufgabe a where a.einheit_id = schule.thema_einheit(t.id) and a.pool = 'test'));
  if v_t is not null then raise exception 'FEHLER 2: Teil ohne freigegebene Einheit, Ort oder Test-Aufgaben: %', v_t; end if;
  -- Aufgaben einer Etappe liegen in der Einheit, die die Etappe führt
  select string_agg(a.id::text, ',') into v_t from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id join schule.thema t on t.id = e.thema_id
   where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101) and a.pool <> 'expedition'   -- Expeditionen bleiben bei Teil 1 (Annahme, siehe Meldung)
     and exists (select 1 from schule.thema t2 join schule.einheit e2 on e2.thema_id = t2.id, jsonb_array_elements(e2.inhalt->'etappen') q
                  where t2.teil_stamm = t.teil_stamm and q->>'lernziel' = a.variante_gruppe and e2.id <> e.id);
  if v_t is not null then raise exception 'FEHLER 2: Aufgaben im falschen Teil: %', v_t; end if;
  select count(*) into v_n from schule.thema t join schule.einheit e on e.thema_id = t.id, jsonb_array_elements(e.inhalt->'etappen') q
   where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101)
     and not exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'test' and a.variante_gruppe = q->>'lernziel');
  raise notice 'TL-S Rauchtest 2: Etappen der Teile ohne eigene Test-Aufgabe: %', v_n;
  -- gültiger Testpfad: jede Pflicht-Etappe (lernziele_pflicht oder eine Liste je Schulart) eines freigegebenen Teils hat eine Test-Aufgabe
  select string_agg(e.id || ':' || q, ',') into v_t from schule.thema t join schule.einheit e on e.thema_id = t.id and e.status = 'freigegeben',
         lateral (select jsonb_array_elements_text(e.inhalt#>'{bewertung,lernziele_pflicht}') q
                  union select jsonb_array_elements_text(x.value) from jsonb_each(coalesce(e.inhalt#>'{bewertung,pflicht_je_schulart}', '{}'::jsonb)) x) p
   where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101)
     and not exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'test' and a.variante_gruppe = p.q);
  if v_t is not null then raise exception 'FEHLER 2: Pflicht-Etappe ohne Test-Aufgabe (kein Testpfad): %', v_t; end if;

  -- 14 T5: echte Pflichtlisten aus LK-D 4 (lk_teilung_2211.json) in den Teilen
  if (select inhalt#>'{bewertung,pflicht_je_schulart,gym_by}' from schule.einheit where id = schule.thema_einheit(schule.tl_knoten(29, 2)))
       is distinct from '["summe_mal_summe", "ausklammern", "binomisch"]'::jsonb
     or not ((select inhalt#>'{bewertung,pflicht_je_schulart,rs_I}' from schule.einheit where id = schule.thema_einheit(schule.tl_knoten(29, 2))) ? 'gleichungen_binomisch')
     or (select inhalt#>'{bewertung,pflicht_je_schulart,rs_II_III}' from schule.einheit where id = schule.thema_einheit(schule.tl_knoten(46, 3))) is distinct from '[]'::jsonb
     or (select inhalt#>'{bewertung,pflicht_je_schulart,myp_standard}' from schule.einheit where id = schule.thema_einheit(91)) is distinct from '[]'::jsonb
     or (select jsonb_array_length(inhalt#>'{bewertung,pflicht_je_schulart,myp_extended}') from schule.einheit where id = schule.thema_einheit(91)) < 1
     or (select inhalt#>'{bewertung,pflicht_je_schulart,gym_by}' from schule.einheit where id = schule.thema_einheit(schule.tl_knoten(44, 2))) is distinct from '[]'::jsonb
     or (select inhalt#>'{bewertung,pflicht_je_schulart,gym_by}' from schule.einheit where id = schule.thema_einheit(schule.tl_knoten(46, 2))) is distinct from '[]'::jsonb
     or (select inhalt#>'{bewertung,pflicht_je_schulart,gym_by}' from schule.einheit where id = schule.thema_einheit(schule.tl_knoten(101, 2))) is distinct from '["cavalieri"]'::jsonb then
    raise exception 'FEHLER 14: Pflichtlisten nicht wie LK-D 4'; end if;

  -- 3 B3b: jede alte Antwort erscheint beim richtigen Teil (Antwort → Aufgabe → Einheit des Teils, der ihre Etappe führt; sonst Teil 1)
  select count(*) into v_n from tl_rt_versuch r join schule.versuch v on v.id = r.id join schule.aufgabe a on a.id = v.aufgabe_id
    join schule.einheit e on e.id = a.einheit_id join schule.thema t on t.id = e.thema_id
   where coalesce(t.teil_stamm, t.id) <> r.stamm
      or (exists (select 1 from schule.thema t2 join schule.einheit e2 on e2.thema_id = t2.id, jsonb_array_elements(e2.inhalt->'etappen') q
                   where t2.teil_stamm = r.stamm and q->>'lernziel' = r.lz)
          and not exists (select 1 from jsonb_array_elements(e.inhalt->'etappen') q where q->>'lernziel' = r.lz))
      or (not exists (select 1 from schule.thema t2 join schule.einheit e2 on e2.thema_id = t2.id, jsonb_array_elements(e2.inhalt->'etappen') q
                       where t2.teil_stamm = r.stamm and q->>'lernziel' = r.lz)
          and t.teil_nr <> 1);
  if v_n > 0 then raise exception 'FEHLER 3: % alte Antworten beim falschen Teil', v_n; end if;
  if (select count(*) from tl_rt_versuch) <> (select count(*) from tl_rt_versuch r join schule.versuch v on v.id = r.id) then
    raise exception 'FEHLER 3: alte Antworten verloren'; end if;
  -- „Was wackelt“: Fehler je Kind über alle Teile = vorher
  select count(*) into v_n from tl_rt_wackelt w
   where w.fehler is distinct from (select sum(f.anzahl) from schule.thema t2, schule.wackelt_fehler(w.lernender_id, t2.id, null::bigint, null::text) f
                                     where coalesce(t2.teil_stamm, t2.id) = w.stamm);
  if v_n > 0 then raise exception 'FEHLER 3: „Was wackelt“-Fehler nach dem Teilen anders (% Kind/Thema-Paare)', v_n; end if;
  raise notice 'TL-S Rauchtest 3: % alte Antworten geprüft', (select count(*) from tl_rt_versuch);

  -- 4 B3a: Voraussetzungen nach den Kanten (Beispiele aus ChatGPT 939/940) und Teil k ← Teil k−1
  if exists (select 1 from (values (31), (8), (97)) x(t) where not exists (select 1 from schule.voraussetzung v
              where v.thema_id = x.t and v.braucht_id = schule.tl_knoten(29, 2))) then raise exception 'FEHLER 4: 31/8/97 ← 29 Teil 2 fehlt'; end if;
  if exists (select 1 from (values (62), (64)) x(t) where not exists (select 1 from schule.voraussetzung v
              where v.thema_id = x.t and v.braucht_id = schule.tl_knoten(61, 2))) then raise exception 'FEHLER 4: 62/64 ← 61 Teil 2 fehlt'; end if;
  if exists (select 1 from schule.voraussetzung v where v.braucht_id in (29, 61) and v.thema_id in (31, 8, 97, 62, 64)) then
    raise exception 'FEHLER 4: alte Kante auf Teil 1 statt Teil 2 übrig'; end if;
  select string_agg(t.id::text, ',') into v_t from schule.thema t where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101) and t.teil_nr > 1
     and not exists (select 1 from schule.voraussetzung v where v.thema_id = t.id and v.braucht_id = schule.tl_knoten(t.teil_stamm, t.teil_nr - 1));
  if v_t is not null then raise exception 'FEHLER 4: Teil ohne Kante zum Teil davor: %', v_t; end if;

  -- 5 B3c: Zusatz je Schulart – Gymnasium: 46 T3 ← T2 nur empfohlen, ← T1 hart; 44 T2 und 46 T2 Zusatz; Visum folgt der Schulart
  if not coalesce((select 'gym_by' = any(zusatz) from schule.thema where id = schule.tl_knoten(44, 2)), false)
     or not coalesce((select 'gym_by' = any(zusatz) from schule.thema where id = schule.tl_knoten(46, 2)), false) then raise exception 'FEHLER 5: Zusatz-Kennung fehlt'; end if;
  if not exists (select 1 from schule.voraussetzung_schulart where thema_id = schule.tl_knoten(46, 3) and braucht_id = schule.tl_knoten(46, 2) and gruppe = 'gym_by' and art = 'empfohlen')
     or not exists (select 1 from schule.voraussetzung_schulart where thema_id = schule.tl_knoten(46, 3) and braucht_id = 46 and gruppe = 'gym_by' and art = 'hart') then
    raise exception 'FEHLER 5: Abweichung Gymnasium für 46 Teil 3 fehlt'; end if;
  if exists (select 1 from schule.v_ort_visum v join schule.block_thema a on a.block_id = v.ort_id and a.thema_id = schule.tl_knoten(46, 3)
              join schule.block_thema b on b.block_id = v.braucht_ort_id and b.thema_id = schule.tl_knoten(46, 2) where v.gruppe = 'gym_by') then
    raise exception 'FEHLER 5: Zusatz-Teil sperrt im Gymnasium'; end if;
  if not exists (select 1 from schule.v_ort_visum v join schule.block_thema a on a.block_id = v.ort_id and a.thema_id = schule.tl_knoten(46, 3)
                  join schule.block_thema b on b.block_id = v.braucht_ort_id and b.thema_id = schule.tl_knoten(46, 2) where v.gruppe = 'rs_I') then
    raise exception 'FEHLER 5: in der Realschule fehlt 46 Teil 3 ← Teil 2'; end if;
  if exists (select 1 from schule.v_ort_visum v join schule.block_thema b on b.block_id = v.braucht_ort_id join schule.thema t on t.id = b.thema_id
              where v.gruppe = any(t.zusatz)) then raise exception 'FEHLER 5: ein Zusatz-Teil ist irgendwo Visum'; end if;
  -- Zusatz-Teile stehen im Plan eines Kindes dieser Schulart nur als „zusatz“
  if exists (select 1 from schule.route r join schule.block_thema bt on bt.block_id = r.block_id join schule.thema t on t.id = bt.thema_id
              join schule.lernender l on l.id = r.lernender_id
              where schule.kind_gruppe(l.id) = any(t.zusatz) and r.art = 'normal' and r.status not in ('fertig', 'entfernt')) then
    raise exception 'FEHLER 5: offener Zusatz-Teil als Pflicht im Plan'; end if;

  -- 6 vollständig übernommene Teile: Stempel, Ort fertig, 100 Ort-Sterne genau einmal, Flug-Test gilt
  select count(*) into v_n from schule.flug_erstabschluss f join schule.einheit e on e.id = f.einheit_id join schule.thema t on t.id = e.thema_id
   where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101) and t.teil_nr > 1
     and (not exists (select 1 from schule.route r join schule.block_thema bt on bt.block_id = r.block_id and bt.thema_id = t.id
                       where r.lernender_id = f.lernender_id and r.status = 'fertig')
          or (select count(*) from schule.sterne s join schule.block_thema bt on s.bezug = 'block:' || bt.block_id and bt.thema_id = t.id
               where s.lernender_id = f.lernender_id and s.grund = 'ort') <> 1
          or not exists (select 1 from schule.testsitzung ts where ts.lernender_id = f.lernender_id and ts.einheit_id = e.id and ts.art = 'blocktest' and ts.status = 'abgeschlossen')
          or schule.thema_stufe(f.lernender_id, t.id)->>'test_offen' = 'true');
  if v_n > 0 then raise exception 'FEHLER 6: % vollständige Teile ohne Stempel/Ort/Sterne/Test', v_n; end if;
  raise notice 'TL-S Rauchtest 6: vollständig übernommene neue Teile: %', (select count(*) from schule.flug_erstabschluss f join schule.einheit e on e.id = f.einheit_id
     join schule.thema t on t.id = e.thema_id where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101) and t.teil_nr > 1);

  -- 6b TL-S 6 (Befund 1): Stempel, Sterne und Stufe passen zusammen – ein vollständig übernommener Teil steht nicht auf „dran“
  --    (Kür-Etappen wie 29 Teil 2 gleichungen_binomisch im Gymnasium zählen für die Stufe nicht)
  select string_agg(f.lernender_id || ':' || t.id || ':' || (schule.thema_stufe(f.lernender_id, t.id)->>'stufe'), ', ') into v_t
    from schule.flug_erstabschluss f join schule.einheit e on e.id = f.einheit_id join schule.thema t on t.id = e.thema_id
   where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101) and t.teil_nr > 1
     and schule.thema_stufe(f.lernender_id, t.id)->>'stufe' not in ('wiederholung', 'komplett')
     and coalesce((schule.thema_stufe(f.lernender_id, t.id)->>'wieder_offen')::int, 0) = 0 and not coalesce((schule.thema_stufe(f.lernender_id, t.id)->>'rueckreise')::boolean, false);
  if v_t is not null then raise exception 'FEHLER 6b: Stempel gebucht, Stufe passt nicht (Kind:Teil:Stufe): %', v_t; end if;

  -- 7 Lehrplan: keine Zuordnung mit Etappen, die ihr Teil nicht führt
  select count(*) into v_n from schule.zuordnung z join schule.thema t on t.id = z.thema_id
   where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101) and z.etappen is not null and not ('*' = any(z.etappen))
     and exists (select 1 from unnest(z.etappen) x where not exists (select 1 from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') q
                                                                   where e.id = schule.thema_einheit(t.id) and q->>'lernziel' = x));
  if v_n > 0 then raise exception 'FEHLER 7: % Zuordnungen mit fremden Etappen', v_n; end if;

  -- 8 LW-Rest: alte Besprochen-Markierung + danach endgültiger erster Fehlversuch → wieder offen; ohne neuen Fehler bleibt sie
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER 8: kein Testkind'; end if;
  select e.id, q1.lz, q1.a, q2.lz, q2.a into v_e, v_lz, v_a, v_lz2, v_a2
    from schule.thema t join schule.einheit e on e.id = schule.thema_einheit(t.id)
    cross join lateral (select a.variante_gruppe lz, min(a.id) a from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'uebung' group by 1 order by 1 limit 1) q1
    cross join lateral (select a.variante_gruppe lz, min(a.id) a from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'uebung' and a.variante_gruppe > q1.lz
                         group by 1 order by 1 limit 1) q2
   where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101) and t.teil_nr > 1
     and not exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id where v.lernender_id = v_l and a.einheit_id = e.id)
     and not exists (select 1 from schule.besprochen b where b.lernender_id = v_l and b.einheit_id = e.id)
   order by t.id limit 1;
  if v_e is null then raise exception 'FEHLER 8 Vorbereitung: kein neuer Teil mit zwei Übungs-Etappen ohne Antworten des Testkinds'; end if;
  insert into schule.besprochen (lernender_id, einheit_id, lernziel, von, am) values
    (v_l, v_e, v_lz, 'rauchtest', now() - interval '3 hours'), (v_l, v_e, v_lz2, 'rauchtest', now() - interval '3 hours');
  -- erster Anlauf falsch, danach weitergegangen (andere Aufgabe): endgültig falsch beim Weitergehen
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, richtig, anlauf, am) values
    (v_l, v_a, 'tl-rt-1', false, 1, now() - interval '2 hours'),
    (v_l, v_a2, 'tl-rt-2', true, 1, now() - interval '110 minutes');
  v_b := schule.besprochen_aktiv(v_l, v_e, v_lz);
  if v_b.lernender_id is not null then raise exception 'FEHLER 8: Besprochen bleibt trotz endgültigem ersten Fehlversuch'; end if;
  v_b := schule.besprochen_aktiv(v_l, v_e, v_lz2);
  if v_b.lernender_id is null then raise exception 'FEHLER 8: Besprochen ohne neuen Fehler verloren'; end if;
  -- erster Anlauf falsch, noch offen (gerade eben, nicht weitergegangen): zählt noch nicht
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, richtig, anlauf, am) values (v_l, v_a2, 'tl-rt-3', false, 1, now());
  v_b := schule.besprochen_aktiv(v_l, v_e, v_lz2);
  if v_b.lernender_id is null then raise exception 'FEHLER 8: offener erster Anlauf hebt Besprochen schon auf'; end if;

  -- 10 Kür je Schulart: Liste für die Schulart des Testkinds → Kür-Etappe ist dort nicht Pflicht (Flug-Wertung, Flug-Abschluss, Flug abgelegt);
  --    ohne Liste bleibt alles wie bisher
  select e.id, q1.lz, q2.lz into v_e, v_lz, v_lz2
    from schule.einheit e
    cross join lateral (select x->>'lernziel' lz from jsonb_array_elements(e.inhalt->'etappen') x order by 1 limit 1) q1
    cross join lateral (select x->>'lernziel' lz from jsonb_array_elements(e.inhalt->'etappen') x where x->>'lernziel' > q1.lz order by 1 limit 1) q2
   where e.status = 'freigegeben' and jsonb_typeof(e.inhalt#>'{bewertung,pflicht_je_schulart}') is null   -- Einheit ohne Listen je Gruppe (nicht die Teile)
     and not exists (select 1 from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = e.id)
     and not exists (select 1 from schule.abgelegt g where g.lernender_id = v_l and g.einheit_id = e.id)
   order by e.id limit 1;
  if v_e is null then raise exception 'FEHLER 10 Vorbereitung: keine passende Einheit'; end if;
  -- ohne Liste: Pflicht wie lernziele_pflicht
  if schule.pflicht_lernziele(v_l, v_e) is distinct from array(select jsonb_array_elements_text(coalesce((select inhalt#>'{bewertung,lernziele_pflicht}' from schule.einheit where id = v_e), '[]'))) then
    raise exception 'FEHLER 10: ohne Liste weicht die Pflicht ab'; end if;
  update schule.einheit set status = 'geprueft' where id = v_e;   -- Schutz nur für den Test (Rollback)
  update schule.einheit set inhalt = jsonb_set(inhalt, '{bewertung,pflicht_je_schulart}',
           jsonb_build_object(schule.kind_gruppe(v_l), jsonb_build_array(v_lz))) where id = v_e;
  update schule.einheit set status = 'freigegeben' where id = v_e;
  perform schule.lernziele_anlegen(v_l, v_e);
  if not (select pflicht from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz)
     or (select pflicht from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz2) then
    raise exception 'FEHLER 10: Pflicht/Kür je Schulart nicht übernommen'; end if;
  -- andere Schulart: Liste gilt nicht
  if exists (select 1 from schule.lernender l where l.id <> v_l and schule.kind_gruppe(l.id) <> schule.kind_gruppe(v_l)
               and schule.pflicht_lernziele(l.id, v_e) = array[v_lz]) then raise exception 'FEHLER 10: Liste gilt für fremde Schulart'; end if;
  -- Flug „abgelegt“ braucht nur die Pflicht-Etappe des Kindes
  perform schule.wdh_ablegen(v_l, v_e, v_lz);
  if not exists (select 1 from schule.abgelegt g where g.lernender_id = v_l and g.art = 'flug' and g.einheit_id = v_e) then
    raise exception 'FEHLER 10: Flug nicht abgelegt, obwohl die einzige Pflicht-Etappe abgelegt ist'; end if;
  -- Liste wieder weg: bestehende Zeilen bleiben (kein Rückbau ohne Liste)
  update schule.einheit set status = 'geprueft' where id = v_e;
  update schule.einheit set inhalt = inhalt #- '{bewertung,pflicht_je_schulart}' where id = v_e;
  update schule.einheit set status = 'freigegeben' where id = v_e;
  perform schule.lernziele_anlegen(v_l, v_e);
  if (select pflicht from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz2) then
    raise exception 'FEHLER 10: ohne Liste wurde eine bestehende Zeile geändert'; end if;

  -- 7b Ein Hauptbezug je Punkt; Nebenbezüge von Geschwister-Teilen geben dem Teil seine Klassen (thema_lage_klasse)
  if exists (select 1 from schule.zuordnung where bezug = 'haupt' group by eintrag_id having count(*) > 1) then raise exception 'FEHLER 7b: Punkt mit zwei Hauptbezügen'; end if;
  select string_agg(z.thema_id::text, ',') into v_t from schule.zuordnung z join schule.thema t on t.id = z.thema_id
    join schule.eintrag e on e.id = z.eintrag_id join schule.lehrplan_zweig lz on lz.quelle_id = e.quelle_id
   where z.bezug = 'neben' and z.begruendung like 'TL-S%Hauptbezug bei Teil%' and z.pruefstatus <> 'klaerungsbedarf'
     and not exists (select 1 from schule.thema_lage_klasse k where k.thema_id = z.thema_id and k.schulart = lz.schulart);
  if v_t is not null then raise exception 'FEHLER 7b: Teil ohne Lehrplan-Lage trotz Nebenbezug: %', v_t; end if;

  -- 11 B2/B3: eine Regel Pflicht/Kür je Kind; Schulartwechsel öffnet neue Pflicht-Etappen, Rückwechsel macht sie wieder zur Kür; nichts gelöscht, nichts doppelt
  select coalesce(schulart, 'gym_by') into v_sa from schule.lernender where id = v_l;
  v_sa2 := case when v_sa = 'rs_by' then 'gym_by' else 'rs_by' end;
  select e.id, array(select x->>'lernziel' from jsonb_array_elements(e.inhalt->'etappen') x) into v_e, v_et
    from schule.einheit e join schule.thema t on t.id = e.thema_id
   where t.teil_stamm in (26, 44, 61) and t.teil_nr = 1 and e.status = 'freigegeben' and jsonb_array_length(e.inhalt->'etappen') >= 2   -- nicht die Teile der Prüfungen 14–18
     and not exists (select 1 from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = e.id)
   order by e.id limit 1;
  if v_e is null then raise exception 'FEHLER 11 Vorbereitung: kein Teil'; end if;
  update schule.einheit set status = 'geprueft' where id = v_e;
  -- wie 29 Teil 2: in der Schulart des Testkinds alle außer der letzten Etappe Pflicht (letzte = Kür), in der anderen alle Pflicht
  update schule.einheit set inhalt = jsonb_set(inhalt, '{bewertung,pflicht_je_schulart}',
           jsonb_build_object(case v_sa when 'rs_by' then 'rs_I' else v_sa end, to_jsonb(v_et[1:cardinality(v_et) - 1]),
                              case v_sa2 when 'rs_by' then 'rs_I' else v_sa2 end, to_jsonb(v_et))) where id = v_e;
  update schule.einheit set status = 'freigegeben' where id = v_e;
  perform schule.lernziele_anlegen(v_l, v_e);
  update schule.lernziel_stand set status = 'nachgewiesen' where lernender_id = v_l and einheit_id = v_e and pflicht;
  select count(*) into v_st0 from schule.sterne where lernender_id = v_l;
  select count(*) into v_k0 from schule.lernziel_stand where lernender_id = v_l;
  create temp table tl_rt_lz on commit drop as select einheit_id, lernziel, status, sicherungen, fehler_anzahl from schule.lernziel_stand where lernender_id = v_l;
  if exists (select 1 from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = v_e and s.pflicht and s.status not in ('nachgewiesen', 'korrigiert', 'gesichert')) then
    raise exception 'FEHLER 11: Schulart % – alle Pflicht-Etappen nachgewiesen, Flug trotzdem offen', v_sa; end if;
  update schule.lernender set schulart = v_sa2, zweig = null where id = v_l;   -- Wechsel
  if not exists (select 1 from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = v_e and s.lernziel = v_et[cardinality(v_et)] and s.pflicht and s.status = 'offen') then
    raise exception 'FEHLER 11: nach dem Wechsel ist die neue Pflicht-Etappe nicht offen'; end if;
  update schule.lernender set schulart = v_sa, zweig = null where id = v_l;      -- Rückwechsel
  if exists (select 1 from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = v_e and s.pflicht and s.status not in ('nachgewiesen', 'korrigiert', 'gesichert')) then
    raise exception 'FEHLER 11: nach dem Rückwechsel ist die Etappe nicht wieder Kür'; end if;
  -- TL-S 6 (Befund 2): Der Wechsel darf neue Pflicht-Etappen als „offen“ anlegen (z. B. 29 Teil 2 gleichungen_binomisch in der Realschule) –
  -- aber nichts löschen, keinen Stand ändern und keine Sterne buchen
  if (select count(*) from schule.sterne where lernender_id = v_l) <> v_st0
     or exists (select 1 from tl_rt_lz a where not exists (select 1 from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = a.einheit_id
                  and s.lernziel = a.lernziel and s.status = a.status and s.sicherungen = a.sicherungen and s.fehler_anzahl = a.fehler_anzahl))
     or exists (select 1 from schule.lernziel_stand s where s.lernender_id = v_l and s.status <> 'offen'
                  and not exists (select 1 from tl_rt_lz a where a.einheit_id = s.einheit_id and a.lernziel = s.lernziel)) then
    raise exception 'FEHLER 11: Wechsel hat Sterne gebucht oder Lernstand gelöscht/verändert'; end if;
  raise notice 'TL-S Rauchtest 11: Wechsel und Rückwechsel – % neue offene Lernstand-Zeilen, keine gelöscht oder verändert, Sterne unverändert',
    (select count(*) from schule.lernziel_stand where lernender_id = v_l) - v_k0;
  -- Teil ohne Pflicht-Etappe für das Kind: kein Zwangstest
  update schule.einheit set status = 'geprueft' where id = v_e;
  update schule.einheit set inhalt = jsonb_set(inhalt, array['bewertung', 'pflicht_je_schulart', case v_sa when 'rs_by' then 'rs_I' else v_sa end], '[]'::jsonb) where id = v_e;
  update schule.einheit set status = 'freigegeben' where id = v_e;
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am)
  select v_l, v_e, x, true, now() from unnest(v_et) x on conflict do nothing;
  if (schule.thema_stufe(v_l, (select thema_id from schule.einheit where id = v_e))->>'test_offen')::boolean then
    raise exception 'FEHLER 11: Teil ohne Pflicht-Etappe verlangt einen Test'; end if;

  -- 12 TL-S 6 (Entscheidung 20:20): Teil 1 behält Setzung, Plan-Platz und Rückreise des Themas; neue Teile erben nichts –
  --    nicht gesetzt, keine Rückreise, im Plan nur als selbst geschaffter Teil („fertig“); Visum-Übergang für geschaffte/gesetzte alte Themen
  select string_agg(v.lernender_id || ':' || t.id || ':' || f, ', ') into v_t
    from tl_rt_stufe v join schule.thema t on t.teil_stamm = v.stamm and t.teil_nr = 1
    cross join lateral (select schule.thema_stufe(v.lernender_id, t.id) n) x
    cross join unnest(array['gesetzt', 'rueckreise', 'im_plan']) f
   where (x.n->f) is distinct from (v.st->f);
  if v_t is not null then raise exception 'FEHLER 12: Teil 1 nicht wie das Thema vorher (Kind:Teil:Feld): %', v_t; end if;
  select string_agg(v.lernender_id || ':' || t.id, ', ') into v_t
    from tl_rt_stufe v join schule.thema t on t.teil_stamm = v.stamm and t.teil_nr > 1
    cross join lateral (select schule.thema_stufe(v.lernender_id, t.id) n) x
   where x.n->>'gesetzt' is not null or coalesce((x.n->>'rueckreise')::boolean, false)
      or coalesce((x.n->>'im_plan')::boolean, false) is distinct from exists (select 1 from schule.flug_erstabschluss f join schule.einheit e on e.id = f.einheit_id
                                                                             where f.lernender_id = v.lernender_id and e.thema_id = t.id);
  if v_t is not null then raise exception 'FEHLER 12: neuer Teil erbt Setzung/Plan/Rückreise oder fehlt trotz eigener Leistung (Kind:Teil): %', v_t; end if;
  select string_agg(v.lernender_id || ':' || t.id, ', ') into v_t
    from tl_rt_stufe v join schule.thema t on t.teil_stamm = v.stamm and t.teil_nr > 1 join schule.block_thema bt on bt.thema_id = t.id
   where (v.st->>'gesetzt' = 'komplett' or exists (select 1 from schule.route r join schule.block_thema b1 on b1.block_id = r.block_id and b1.thema_id = v.stamm
                                                     where r.lernender_id = v.lernender_id and r.art = 'normal' and r.status = 'fertig'))
     and not exists (select 1 from schule.visum_uebergang u where u.lernender_id = v.lernender_id and u.block_id = bt.block_id);
  if v_t is not null then raise exception 'FEHLER 12: Visum-Übergang fehlt (Kind:Teil): %', v_t; end if;
  raise notice 'TL-S Rauchtest 12: gesetzt komplett %, gesetzt wiederholen %, Rückreise %, im Plan % (Teil 1 wie vorher, neue Teile ohne Vererbung)',
    (select count(*) from tl_rt_stufe where st->>'gesetzt' = 'komplett'), (select count(*) from tl_rt_stufe where st->>'gesetzt' = 'wiederholen'),
    (select count(*) from tl_rt_stufe where (st->>'rueckreise')::boolean), (select count(*) from tl_rt_stufe where (st->>'im_plan')::boolean);

  -- 13 TL-S 4: harte Kanten bleiben je Schulart hart, außer die Voraussetzung ist dort Zusatz (z. B. 102 ← 30, 29 ← 102 in allen Schularten)
  select string_agg(o.thema_id || '←' || o.braucht_id || ':' || o.gruppe, ', ') into v_t
    from schule.voraussetzung_schulart o join schule.voraussetzung v on v.thema_id = o.thema_id and v.braucht_id = o.braucht_id join schule.thema b on b.id = o.braucht_id
   where v.art = 'hart' and o.art <> 'hart' and not (o.gruppe = any(coalesce(b.zusatz, '{}')));
  if v_t is not null then raise exception 'FEHLER 13: harte Kante je Schulart abgeschwächt: %', v_t; end if;
  if exists (select 1 from (values (102, 30), (29, 102)) x(a, b) cross join (values ('gym_by'), ('rs_I'), ('rs_II_III'), ('myp_standard'), ('myp_extended')) s(sa)
              where not exists (select 1 from schule.voraussetzung v left join schule.voraussetzung_schulart o on o.thema_id = v.thema_id and o.braucht_id = v.braucht_id and o.gruppe = s.sa
                                 where v.thema_id = x.a and v.braucht_id = x.b and coalesce(o.art, v.art) = 'hart')) then
    raise exception 'FEHLER 13: 102 ← 30 oder 29 ← 102 nicht in jeder Schulart hart'; end if;

  -- 15 T1 Gruppen: dieselbe Regel für Zusatz, Pflicht und Visum je Kind + Gruppe (RS I gegen II/III bei 46 Teil 3, IB Standard gegen Extended bei 91)
  if schule.tl_knoten(46, 3) is null or (select zusatz from schule.thema where id = schule.tl_knoten(46, 3)) is distinct from '{rs_II_III}'
     or (select zusatz from schule.thema where id = 91) is distinct from '{myp_standard}' then raise exception 'FEHLER 15: Zusatz je Gruppe falsch'; end if;
  update schule.lernender set schulart = 'rs_by', zweig = 'rs_II_III' where id = v_l;
  if schule.kind_gruppe(v_l) <> 'rs_II_III' or schule.pflicht_lernziele(v_l, schule.thema_einheit(schule.tl_knoten(46, 3))) <> '{}'::text[] then raise exception 'FEHLER 15: RS II/III 46 Teil 3 nicht Zusatz ohne Pflicht'; end if;
  update schule.lernender set zweig = 'rs_I' where id = v_l;
  if cardinality(schule.pflicht_lernziele(v_l, schule.thema_einheit(schule.tl_knoten(46, 3)))) < 1 then raise exception 'FEHLER 15: RS I 46 Teil 3 ohne Pflicht'; end if;
  update schule.lernender set schulart = 'ib_myp', zweig = null where id = v_l;
  if schule.kind_gruppe(v_l) <> 'myp_standard' or schule.pflicht_lernziele(v_l, schule.thema_einheit(91)) <> '{}'::text[] then raise exception 'FEHLER 15: IB Standard 91 nicht ohne Pflicht'; end if;
  update schule.lernender set zweig = 'myp_extended' where id = v_l;
  if cardinality(schule.pflicht_lernziele(v_l, schule.thema_einheit(91))) < 1 then raise exception 'FEHLER 15: IB Extended 91 ohne Pflicht'; end if;
  -- Visum: Zusatz-Teil sperrt in seiner Gruppe nichts (in keiner Gruppe ist ein Zusatz-Teil Voraussetzung mit „hart“)
  if exists (select 1 from schule.v_ort_visum v join schule.block_thema b on b.block_id = v.braucht_ort_id join schule.thema t on t.id = b.thema_id
              where v.gruppe = any(t.zusatz) and not exists (select 1 from schule.block_thema b2 where b2.block_id = b.block_id and b2.thema_id <> t.id)) then
    raise exception 'FEHLER 15: Zusatz-Teil ist in seiner Gruppe Visum'; end if;
  update schule.lernender set schulart = v_sa, zweig = null where id = v_l;

  -- 16 T2: ausdrücklich leere Pflichtliste (Gym 44 Teil 2) = freiwilliger Zusatz – kein Zwangstest, kein Stempel, kein Ort-Abschluss, kein „Flug abgelegt“
  select schule.thema_einheit(schule.tl_knoten(44, 2)) into v_e;
  update schule.lernender set schulart = 'gym_by', zweig = null where id = v_l;
  if schule.pflicht_lernziele(v_l, v_e) <> '{}'::text[] then raise exception 'FEHLER 16 Vorbereitung: 44 Teil 2 im Gym nicht ohne Pflicht'; end if;
  perform schule.lernziele_anlegen(v_l, v_e);
  if exists (select 1 from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_e and pflicht) then raise exception 'FEHLER 16: Pflicht-Zeile trotz leerer Liste'; end if;
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am)
  select v_l, v_e, x->>'lernziel', true, now() from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = v_e on conflict do nothing;
  if coalesce((schule.thema_stufe(v_l, schule.tl_knoten(44, 2))->>'test_offen')::boolean, false) then raise exception 'FEHLER 16: Zwangstest bei 0 Pflicht'; end if;
  insert into schule.testsitzung (lernender_id, art, thema_id, einheit_id, block_id, aufgaben, status, gestartet_am)
  select v_l, 'blocktest', schule.tl_knoten(44, 2), v_e, (select bt.block_id from schule.block_thema bt where bt.thema_id = schule.tl_knoten(44, 2) limit 1),
         array(select a.id from schule.aufgabe a where a.einheit_id = v_e and a.pool = 'test'), 'laeuft', now() returning id into v_a;
  insert into schule.versuch (lernender_id, aufgabe_id, testsitzung_id, client_id, richtig, punkte, punkte_max, hilfe, versuch_nr)
  select v_l, x, v_a, 'tl-rt-16-' || x, true, 1, 1, 0, 1 from unnest((select aufgaben from schule.testsitzung where id = v_a)) x;
  perform schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_a));
  if exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_e) then raise exception 'FEHLER 16: Stempel allein durch Kür'; end if;
  if (schule.ort_stand(v_l, (select bt.block_id from schule.block_thema bt where bt.thema_id = schule.tl_knoten(44, 2) limit 1))->>'abgeschlossen')::boolean then
    raise exception 'FEHLER 16: Ort (100 Sterne) allein durch Kür'; end if;
  perform schule.wdh_ablegen(v_l, v_e, x->>'lernziel') from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = v_e;
  if exists (select 1 from schule.abgelegt where lernender_id = v_l and art = 'flug' and einheit_id = v_e) then raise exception 'FEHLER 16: Flug abgelegt allein durch Kür'; end if;
  -- ohne festgelegte Liste fällt die Regel wie bisher auf alle Etappen zurück (wdh_ablegen/konto_wd): pflicht_lernziele = null
  if schule.pflicht_lernziele(v_l, v_e) is null then raise exception 'FEHLER 16: leer und „nicht festgelegt“ verwechselt'; end if;

  -- 17 T4: Ein-Etappen-Flug 101 Teil 2 – Test, Korrektur, Stempel
  select schule.thema_einheit(schule.tl_knoten(101, 2)) into v_e;
  if (select status from schule.einheit where id = v_e) <> 'freigegeben'
     or not exists (select 1 from schule.aufgabe where einheit_id = v_e and variante_gruppe = 'cavalieri' and pool = 'test')
     or not exists (select 1 from schule.aufgabe where einheit_id = v_e and variante_gruppe = 'cavalieri' and pool = 'korrektur')
     or (select count(*) from schule.aufgabe where einheit_id = v_e and variante_gruppe = 'cavalieri' and pool = 'sicherung') < 1 then
    raise exception 'FEHLER 17: 101 Teil 2 ohne freigegebene Einheit oder Test/Korrektur/Sicherung'; end if;
  perform schule.lernziele_anlegen(v_l, v_e);
  insert into schule.testsitzung (lernender_id, art, thema_id, einheit_id, block_id, aufgaben, status, gestartet_am)
  values (v_l, 'blocktest', schule.tl_knoten(101, 2), v_e, (select bt.block_id from schule.block_thema bt where bt.thema_id = schule.tl_knoten(101, 2) limit 1),
          array(select a.id from schule.aufgabe a where a.einheit_id = v_e and a.pool = 'test' order by a.id), 'laeuft', now()) returning id into v_a;
  insert into schule.versuch (lernender_id, aufgabe_id, testsitzung_id, client_id, richtig, punkte, punkte_max, hilfe, versuch_nr)
  select v_l, x, v_a, 'tl-rt-17-' || x, false, 0, 1, 0, 1 from unnest((select aufgaben from schule.testsitzung where id = v_a)) x;
  perform schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_a));
  if (select status from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_e and lernziel = 'cavalieri') <> 'fehler'
     or exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_e) then raise exception 'FEHLER 17: Fehler im Flug-Test nicht gewertet'; end if;
  insert into schule.testsitzung (lernender_id, art, thema_id, einheit_id, block_id, aufgaben, status, gestartet_am)
  values (v_l, 'korrektur', schule.tl_knoten(101, 2), v_e, (select bt.block_id from schule.block_thema bt where bt.thema_id = schule.tl_knoten(101, 2) limit 1),
          array(select a.id from schule.aufgabe a where a.einheit_id = v_e and a.pool = 'korrektur' order by a.id limit 1), 'laeuft', now()) returning id into v_a2;
  insert into schule.versuch (lernender_id, aufgabe_id, testsitzung_id, client_id, richtig, punkte, punkte_max, hilfe, versuch_nr)
  select v_l, x, v_a2, 'tl-rt-17k-' || x, true, 1, 1, 0, 1 from unnest((select aufgaben from schule.testsitzung where id = v_a2)) x;
  perform schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_a2));
  if not exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_e) then raise exception 'FEHLER 17: kein Stempel nach Korrektur'; end if;
  update schule.lernender set schulart = v_sa, zweig = null where id = v_l;

  -- 18 TL-S 7 (A1): ohne Testabdeckung kein Abschluss – a) 26 Teil 2 (Karten gelandet, kein alter Flug-Test), b) 61 Teil 2 (Flug-Test nur mit laplace)
  if exists (select 1 from tl_rt_a1 a, schule.flug_erstabschluss f join schule.einheit e on e.id = f.einheit_id
              where f.lernender_id = a.l and e.thema_id in (schule.tl_knoten(26, 2), schule.tl_knoten(61, 2))) then
    raise exception 'FEHLER 18: Erstabschluss ohne Testabdeckung'; end if;
  if exists (select 1 from tl_rt_a1 a, schule.sterne s where s.lernender_id = a.l and s.grund = 'ort'
              and s.bezug in (select 'block:' || bt.block_id from schule.block_thema bt where bt.thema_id in (schule.tl_knoten(26, 2), schule.tl_knoten(61, 2)))) then
    raise exception 'FEHLER 18: Ort-Sterne ohne Testabdeckung'; end if;
  if exists (select 1 from tl_rt_a1 a join schule.tl_teile_je_kind k on k.lernender_id = a.l
              where k.thema_id in (schule.tl_knoten(26, 2), schule.tl_knoten(61, 2)) and (k.im_plan or k.zustand = 'selbst geschafft')) then
    raise exception 'FEHLER 18: Teil ohne Testabdeckung im Plan oder als geschafft gelistet'; end if;

  -- 9 nur einmal teilen: zweites Einspielen ändert nichts
  if (select count(*) from schule.thema t where t.teil_stamm in (26, 29, 44, 46, 61, 91, 101)) <> 15 then raise exception 'FEHLER 9'; end if;

  raise notice 'TL-S Rauchtest: alles grün';
end $$;

rollback;
