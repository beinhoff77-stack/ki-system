-- Rauchtest I-5 (thema_stufe sieht den offenen Nachtragstest). Nach 20261120_i5_stufe_nachtragstest.sql ausführen. Rollback, nur Testkind, keine Namen.
-- Fall wie im Betrieb: Flug-Test abgeschlossen, alle Etappen gelandet, eine Pflicht-Etappe in lernziel_stand 'offen' (neu hinzugekommen) → ▶ dran, test_offen.
begin;
do $$
declare v_l bigint; v_e bigint; v_t bigint; r jsonb; s jsonb; v_lz text;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  select e.id, e.thema_id into v_e, v_t from schule.einheit e
   where e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id)
     and (select count(*) from jsonb_array_elements_text(e.inhalt->'bewertung'->'lernziele_pflicht')) >= 2
     and jsonb_array_length(coalesce(e.inhalt->'etappen', '[]'::jsonb)) >= 2
     and exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'test')
     and not exists (select 1 from schule.testsitzung x where x.lernender_id = v_l and x.einheit_id = e.id)
     and not schule.thema_kann_schon(v_l, e.thema_id) and not schule.thema_kann_wdh(v_l, e.thema_id)
   order by e.id limit 1;
  if v_e is null then raise exception 'FEHLER: kein passender Flug'; end if;
  update schule.route set status = 'fertig' where lernender_id = v_l and art = 'rueckreise' and status not in ('fertig', 'entfernt');
  -- alle Etappen gelandet (frisch, nicht sicher)
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel)
  select v_l, v_e, et->>'lernziel' from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') et where e.id = v_e on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '1 day', wdh_stufe = 0, misch_ok_am = null, geoeffnet_am = null
   where lernender_id = v_l and einheit_id = v_e;
  perform schule.lernziele_anlegen(v_l, v_e);
  -- Flug-Test geschrieben
  r := schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_e, 'art', 'blocktest'));
  if not coalesce((r->>'ok')::boolean, false) then raise exception 'FEHLER: Flug-Test startet nicht: %', r; end if;
  update schule.testsitzung set status = 'abgeschlossen', abgeschlossen_am = now() where id = (r->>'sitzung_id')::bigint;
  update schule.lernziel_stand set status = 'nachgewiesen' where lernender_id = v_l and einheit_id = v_e;

  -- 1. alles nachgewiesen → ↻ wiederholung, kein offener Test (wie bisher)
  s := schule.thema_stufe(v_l, v_t);
  if s->>'stufe' <> 'wiederholung' or (s->>'test_offen')::boolean then raise exception 'FEHLER 1: %', s; end if;
  raise notice 'ok 1: Flug-Test geschrieben, alles nachgewiesen → ↻, test_offen false';

  -- 2. eine Pflicht-Etappe neu (offen) und gelandet → ▶ dran, test_offen true
  select s.lernziel into v_lz from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = v_e and s.pflicht
     and s.lernziel in (select k.lernziel from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = v_e) order by s.lernziel limit 1;
  if v_lz is null then raise exception 'FEHLER: keine Pflicht-Etappe mit Karten-Stand'; end if;
  update schule.lernziel_stand set status = 'offen' where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  s := schule.thema_stufe(v_l, v_t);
  if s->>'stufe' <> 'dran' or s->>'zeichen' <> '▶' or not (s->>'test_offen')::boolean then raise exception 'FEHLER 2: %', s; end if;
  raise notice 'ok 2: offener Nachtragstest → ▶ dran, test_offen true';

  -- 3. Nachtragstest startet tatsächlich (dieselbe Bedingung wie in test_starten_intern)
  r := schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_e, 'art', 'blocktest'));
  if not (coalesce((r->>'ok')::boolean, false) or r->>'grund' = 'vorrat_erschoepft') then raise exception 'FEHLER 3: %', r; end if;
  s := schule.thema_stufe(v_l, v_t);
  if s->>'stufe' <> 'dran' or not (s->>'test_offen')::boolean then raise exception 'FEHLER 3b: %', s; end if;
  raise notice 'ok 3: Nachtragstest startbar (%), Stufe bleibt ▶', coalesce(r->>'grund', 'gestartet');

  -- 4. offene Etappe noch nicht gelandet → ▶ dran (begonnen), aber kein Test offen
  update schule.testsitzung set status = 'abgebrochen' where lernender_id = v_l and einheit_id = v_e and status = 'laeuft';
  update schule.karte_stand set sitzt = false where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  s := schule.thema_stufe(v_l, v_t);
  if s->>'stufe' <> 'dran' or (s->>'test_offen')::boolean then raise exception 'FEHLER 4: %', s; end if;
  raise notice 'ok 4: offene Etappe noch nicht gelandet → ▶, test_offen false';
end $$;
rollback;
