-- Rauchtest W177 Nachtragstest. Erst NACH 20261118_w177_nachtragstest.sql ausführen. Transaktion mit Rollback – es bleibt nichts zurück. Keine Namen.
-- Fall: Testkind, Flug mit abgeschlossenem Flugtest, danach zwei Pflicht-Etappen wieder 'offen' (wie neu hinzugekommene).
begin;
do $$
declare v_l bigint; v_e bigint; r jsonb; t jsonb; v_n int; v_lz text[]; v_aid bigint; v_ids bigint[];
begin
  select id into v_l from schule.lernender where ist_test order by id limit 1;
  select e.id into v_e from schule.einheit e where e.status = 'freigegeben'
    and (select count(*) from jsonb_array_elements_text(e.inhalt->'bewertung'->'lernziele_pflicht')) >= 3
    and exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'test')
    and not exists (select 1 from schule.testsitzung x where x.lernender_id = v_l and x.einheit_id = e.id) order by e.id limit 1;
  if v_l is null or v_e is null then raise exception 'kein Testkind oder kein passender Flug'; end if;
  -- 1) normaler Flugtest läuft wie bisher
  r := schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_e, 'art', 'blocktest'));
  if not (r->>'ok')::boolean then raise exception 'FEHLER 1: %', r; end if;
  v_n := jsonb_array_length(r->'aufgaben');
  update schule.testsitzung set status = 'abgeschlossen', abgeschlossen_am = now() where id = (r->>'sitzung_id')::bigint;
  update schule.lernziel_stand set status = 'nachgewiesen' where lernender_id = v_l and einheit_id = v_e and pflicht;
  raise notice 'ok 1: Flugtest wie bisher (% Aufgaben)', v_n;
  -- 2) alles nachgewiesen → weiterhin die alte Meldung
  begin
    perform schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_e, 'art', 'blocktest'));
    raise exception 'FEHLER 2: zweiter Flugtest ohne offene Etappe gestartet';
  exception when sqlstate 'P0001' then
    if sqlerrm like 'FEHLER%' then raise; end if;
    raise notice 'ok 2: ohne offene Etappe bleibt es bei „schon abgeschlossen“';
  end;
  -- 3) zwei Pflicht-Etappen wieder offen → Nachtragstest mit genau zwei Bordkarten aus genau diesen Etappen
  select array_agg(lernziel order by lernziel) into v_lz from (select lernziel from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_e and pflicht order by lernziel limit 2) q;
  update schule.lernziel_stand set status = 'offen' where lernender_id = v_l and einheit_id = v_e and lernziel = any(v_lz);
  r := schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_e, 'art', 'blocktest'));
  if not (r->>'ok')::boolean then raise exception 'FEHLER 3: %', r; end if;
  if jsonb_array_length(r->'aufgaben') <> 2 then raise exception 'FEHLER 3: % statt 2 Aufgaben', jsonb_array_length(r->'aufgaben'); end if;
  v_ids := (select aufgaben from schule.testsitzung where id = (r->>'sitzung_id')::bigint);
  if exists (select 1 from schule.aufgabe a where a.id = any(v_ids) and not (a.variante_gruppe = any(v_lz))) then
    raise exception 'FEHLER 3: Aufgabe aus falscher Etappe'; end if;
  raise notice 'ok 3: Nachtragstest mit 2 Bordkarten (% )', v_lz;
  -- 4) Abschluss: eine richtig, eine leer → nachgewiesen bzw. fehler; andere Etappen unverändert
  select a.id into v_aid from schule.aufgabe a where a.id = any(v_ids) and a.variante_gruppe = v_lz[1];
  insert into schule.versuch(lernender_id, aufgabe_id, testsitzung_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr)
  values (v_l, v_aid, (r->>'sitzung_id')::bigint, 'rauchtest-w177', null, true, 1, 1, 0, 1);
  t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', (r->>'sitzung_id')::bigint));
  if (select status from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[1]) <> 'nachgewiesen'
     or (select status from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[2]) <> 'fehler'
     or exists (select 1 from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_e and pflicht and not (lernziel = any(v_lz)) and status <> 'nachgewiesen')
  then raise exception 'FEHLER 4: Stände falsch'; end if;
  raise notice 'ok 4: Abschluss richtig gewertet, übrige Etappen unverändert';
end $$;
-- Ergänzung Bau-Auftrag I, Teil 2 (W177): Sterne vor/nach, Abbruch und Wiederaufnahme ohne Doppelbuchung, offene und fehlerhafte Pflicht-Etappen zugleich,
-- und was mit der Frist des nächsten Nachtests geschieht (nur beschreiben, nichts ändern). Eigener Block, gleiche Transaktion, eigener Flug.
do $$
declare v_l bigint; v_e bigint; r jsonb; v_sid bigint; v_lz text[]; v_ids bigint[]; v_ag schule.aufgabe; v_st0 int; v_st1 int; v_st2 int; v_ns jsonb; v_n int; v_ende timestamptz;
begin
  select id into v_l from schule.lernender where ist_test order by id limit 1;
  select e.id into v_e from schule.einheit e where e.status = 'freigegeben'
    and (select count(*) from jsonb_array_elements_text(e.inhalt->'bewertung'->'lernziele_pflicht')) >= 3
    and exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'test')
    and exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'korrektur')
    and not exists (select 1 from schule.testsitzung x where x.lernender_id = v_l and x.einheit_id = e.id) order by e.id desc limit 1;
  if v_l is null or v_e is null then raise exception 'kein Testkind oder kein passender Flug'; end if;
  -- Flugtest abgeschlossen (leer abgegeben), dann: eine Pflicht-Etappe offen (neu hinzugekommen), eine mit Fehler, Rest nachgewiesen
  r := schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_e, 'art', 'blocktest'));
  perform schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', (r->>'sitzung_id')::bigint));
  select array_agg(lernziel order by lernziel) into v_lz from (select lernziel from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_e and pflicht order by lernziel limit 2) q;
  update schule.lernziel_stand set status = 'nachgewiesen' where lernender_id = v_l and einheit_id = v_e and pflicht;
  update schule.lernziel_stand set status = 'offen' where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[1];
  update schule.lernziel_stand set status = 'fehler' where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[2];
  if (schule.nachtest_stand(v_l, v_e)->>'grund') <> 'einheit_offen' then raise exception 'FEHLER 5a: %', schule.nachtest_stand(v_l, v_e); end if;
  select coalesce(sum(menge), 0) into v_st0 from schule.sterne where lernender_id = v_l;
  -- Nachtragstest: nur die offene Etappe
  r := schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_e, 'art', 'blocktest'));
  v_sid := (r->>'sitzung_id')::bigint; v_ids := (select aufgaben from schule.testsitzung where id = v_sid);
  if not (r->>'ok')::boolean or exists (select 1 from schule.aufgabe a where a.id = any(v_ids) and a.variante_gruppe <> v_lz[1]) then raise exception 'FEHLER 5b: %', r; end if;
  raise notice 'ok 5: offen + fehler zugleich → Nachtragstest nur für die offene Etappe (% Bordkarte), nachtest_stand „einheit_offen“', cardinality(v_ids);
  -- Korrektur angefragt, während der Nachtragstest läuft → es kommt der laufende Test zurück (heutiges Verhalten)
  r := schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_e, 'art', 'korrektur'));
  raise notice 'Info 5c: Korrektur während des Nachtragstests liefert Sitzung % (Art %) – der laufende Test geht vor', r->>'sitzung_id', r->>'art';
  -- eine Antwort, dann Abbruch und Wiederaufnahme
  select * into v_ag from schule.aufgabe where id = v_ids[1];
  insert into schule.versuch(lernender_id, aufgabe_id, testsitzung_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr)
  values (v_l, v_ag.id, v_sid, 'w177-i2-a', v_ag.loesung, true, 1, 1, 0, 1)
  on conflict (testsitzung_id, aufgabe_id) where testsitzung_id is not null do update set richtig = excluded.richtig;
  r := schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_e, 'art', 'blocktest'));
  if (r->>'sitzung_id')::bigint <> v_sid or not ((r->'beantwortet') @> to_jsonb(v_ag.id)) then raise exception 'FEHLER 6a: Wiederaufnahme %', r; end if;
  insert into schule.versuch(lernender_id, aufgabe_id, testsitzung_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr)
  values (v_l, v_ag.id, v_sid, 'w177-i2-b', v_ag.loesung, true, 1, 1, 0, 1)
  on conflict (testsitzung_id, aufgabe_id) where testsitzung_id is not null do update set richtig = excluded.richtig; -- dieselbe Antwort nach der Wiederaufnahme noch einmal
  select count(*) into v_n from schule.versuch where testsitzung_id = v_sid and aufgabe_id = v_ag.id;
  if v_n <> 1 then raise exception 'FEHLER 6b: % Versuche für eine Aufgabe', v_n; end if;
  -- Abschluss, zweimal abgeschlossen → Sterne einmal
  perform schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_sid));
  select coalesce(sum(menge), 0) into v_st1 from schule.sterne where lernender_id = v_l;
  perform schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_sid));
  select coalesce(sum(menge), 0) into v_st2 from schule.sterne where lernender_id = v_l;
  if v_st2 <> v_st1 or v_st1 - v_st0 <> (select punkte from schule.testsitzung where id = v_sid) * schule.sterne_regel('sterne_test_richtig') then
    raise exception 'FEHLER 6c: Sterne vorher %, nach Abschluss %, nach zweitem Abschluss %', v_st0, v_st1, v_st2; end if;
  raise notice 'ok 6: Sterne vorher % → nachher % (= % richtig × Regel), zweiter Abschluss bucht nichts; Wiederaufnahme liefert dieselbe Sitzung, Antwort einmal gespeichert',
    v_st0, v_st1, (select punkte from schule.testsitzung where id = v_sid);
  -- danach: Etappe 1 nachgewiesen, Etappe 2 weiter fehlerhaft → Korrektur nur für Etappe 2
  if (select status from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[1]) <> 'nachgewiesen'
     or (select status from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[2]) <> 'fehler'
     or (schule.nachtest_stand(v_l, v_e)->>'grund') <> 'erst_korrektur' then raise exception 'FEHLER 7a'; end if;
  r := schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_e, 'art', 'korrektur'));
  v_ids := (select aufgaben from schule.testsitzung where id = (r->>'sitzung_id')::bigint); -- Array erst in die Variable: any((select …)) vergleicht bigint mit bigint[]
  if not (r->>'ok')::boolean or r->>'art' <> 'korrektur' or exists (select 1 from schule.aufgabe a where a.id = any(v_ids) and a.variante_gruppe <> v_lz[2]) then
    raise exception 'FEHLER 7b: %', r; end if;
  raise notice 'ok 7: danach Korrektur nur für die fehlerhafte Etappe';
  -- Frist des ersten Nachtests (nur beschreiben): Anker = letzter abgeschlossener Flugtest/Nachtragstest/Korrektur, solange es noch keinen Nachtest gab
  select max(abgeschlossen_am) into v_ende from schule.testsitzung where lernender_id = v_l and einheit_id = v_e and art in ('blocktest', 'korrektur') and status = 'abgeschlossen';
  perform schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', (r->>'sitzung_id')::bigint));
  update schule.lernziel_stand set status = 'nachgewiesen' where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[2]; -- als hätte die Korrektur geklappt
  v_ns := schule.nachtest_stand(v_l, v_e);
  raise notice 'Info 8: nachtest_stand nach Nachtragstest und Korrektur: Anker %, nötig % Lerntage (Grund %) – die Frist beginnt mit dem letzten Abschluss neu',
    v_ns->>'anker', v_ns->>'lerntage_noetig', v_ns->>'grund';
  if (v_ns->>'anker')::timestamptz < v_ende then raise exception 'FEHLER 8: Anker vor dem Nachtragstest'; end if;
end $$;
rollback;
