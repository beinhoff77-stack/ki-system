-- Rauchtest LA-4/LA-5 („kann schon“ je Flug, Lerntage bis zur Wiederholung). Nach 20261119_la_4_kann_schon_fluege.sql ausführen. Rollback, nur Testkind, keine Namen.
begin;
do $$
declare v_l bigint; v_b bigint; v_t1 bigint; v_t2 bigint; v_n int; v_k int; ks schule.karte_stand;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  -- ein Ort mit mindestens zwei Flügen, den das Testkind noch nicht abgeschlossen hat
  select bt.block_id into v_b from schule.block_thema bt join schule.block b on b.id = bt.block_id and b.fach = 'Mathematik'
   group by 1 having count(*) >= 2 order by 1 limit 1;
  select min(thema_id), max(thema_id) into v_t1, v_t2 from schule.block_thema where block_id = v_b;
  select count(*) into v_k from schule.karte_stand where lernender_id = v_l;
  insert into schule.route(lernender_id, block_id, position, art, status, kann_schon, ausgelassen, kann_schon_themen, revision, geaendert_von, geaendert_am)
  select v_l, v_b, 999999, 'normal', 'offen', false, '{}', '{}', 1, 'test', now()
   where not exists (select 1 from schule.route where lernender_id = v_l and block_id = v_b and art = 'normal');
  update schule.route set status = 'offen', kann_schon = false, ausgelassen = '{}', kann_schon_themen = array[v_t1] where lernender_id = v_l and block_id = v_b and art = 'normal';
  if schule.thema_stand(v_l, v_t1) <> 'erledigt' or not schule.thema_kann_schon(v_l, v_t1) then raise exception 'FEHLER 1: kann schon zählt nicht'; end if;
  if schule.thema_kann_schon(v_l, v_t2) then raise exception 'FEHLER 1b: falscher Flug'; end if;
  raise notice 'ok 1: „kann schon“ je Flug zählt in thema_stand als erledigt, nur für diesen Flug';
  -- alle Flüge „kann schon“ → Ort abgeschlossen; keine Karten entstanden
  update schule.route set kann_schon_themen = (select array_agg(thema_id) from schule.block_thema where block_id = v_b) where lernender_id = v_l and block_id = v_b and art = 'normal';
  if not (schule.ort_stand(v_l, v_b)->>'abgeschlossen')::boolean then raise exception 'FEHLER 2: Ort nicht abgeschlossen: %', schule.ort_stand(v_l, v_b); end if;
  select count(*) into v_n from schule.karte_stand where lernender_id = v_l;
  if v_n <> v_k then raise exception 'FEHLER 3: „kann schon“ hat Karten angelegt'; end if;
  raise notice 'ok 2–3: alle Flüge „kann schon“ → Ort abgeschlossen; keine Karte (also keine Mischkarten, Wiederholungen, Expeditionen)';
  -- rückgängig ohne Verlust
  update schule.route set kann_schon_themen = '{}' where lernender_id = v_l and block_id = v_b and art = 'normal';
  if schule.thema_kann_schon(v_l, v_t1) then raise exception 'FEHLER 4'; end if;
  raise notice 'ok 4: zurückgenommen → wieder wie vorher';
  -- LA-5: wdh_in
  select * into ks from schule.karte_stand where lernender_id = v_l and sitzt limit 1;
  if ks.lernender_id is not null then raise notice 'ok 5: Lerntage bis zur Wiederholung: %', schule.karte_wdh_in(ks);
  else raise notice 'ok 5: (Testkind ohne gelandete Etappe – wdh_in nicht geprüft)'; end if;
end $$;
rollback;
