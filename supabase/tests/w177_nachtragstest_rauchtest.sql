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
rollback;
