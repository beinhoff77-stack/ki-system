-- Rauchtest ZP-S (eingeplanter Zusatz-Teil). Alles in einer Transaktion mit Rollback; Änderungen nur am Testkind.
-- Voraussetzung: LZ-S eingespielt. Spielt 20261126_zp_s_zusatz_plan.sql selbst ein (wiederholbar). Ausgabe nur Zahlen.
-- Aufruf aus dem Repo-Wurzelverzeichnis: psql -v ON_ERROR_STOP=1 -f supabase/tests/zp_s_rauchtest.sql
begin;

-- Kinderdaten außer Testkind vorher (Karten, Lernziel-Stände, Lernstand, Sterne, Stempel, Route)
create temp table zp_rt_vorher on commit drop as
  select md5(coalesce((select string_agg(k::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel) from schule.karte_stand k join schule.lernender l on l.id = k.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(s::text, '|' order by s.lernender_id, s.einheit_id, s.lernziel) from schule.lernziel_stand s join schule.lernender l on l.id = s.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(s::text, '|' order by s.lernender_id, s.thema_id) from schule.lernstand s join schule.lernender l on l.id = s.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(s::text, '|' order by s.id) from schule.sterne s join schule.lernender l on l.id = s.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(f::text, '|' order by f.lernender_id, f.einheit_id) from schule.flug_erstabschluss f join schule.lernender l on l.id = f.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(r::text, '|' order by r.id) from schule.route r join schule.lernender l on l.id = r.lernender_id where not l.ist_test), '')) h,
         (select jsonb_object_agg(l.id, schule.reiseoptionen(l.id)) from schule.lernender l where l.aktiv) ro;

-- Test 0 (lesend, vor ZP-S): eingeplanter Zusatz-Teil mit art 'normal' und leerer Pflichtliste – kann er heute fertig werden?
do $$
declare v_x record; v_n int := 0;
begin
  if position('ZP-S' in pg_get_functiondef('schule.ort_stand(bigint, bigint)'::regprocedure)) > 0 then raise notice 'Test 0: ZP-S schon eingespielt – Vorher-Prüfung entfällt'; return; end if;
  for v_x in select r.id, r.lernender_id, bt.thema_id, r.block_id from schule.route r join schule.block_thema bt on bt.block_id = r.block_id join schule.thema t on t.id = bt.thema_id
              where schule.ist_plan(r) and r.status not in ('fertig', 'entfernt') and schule.kind_gruppe(r.lernender_id) = any(t.zusatz) and not (t.id = any(r.ausgelassen)) loop
    v_n := v_n + 1;
    raise notice 'Test 0: Plan-Eintrag % (Kind %, Thema %): Etappen der Regel %, Ort abgeschlossen möglich: nein (ort_stand verlangt eine Pflicht-Etappe)',
      v_x.id, v_x.lernender_id, v_x.thema_id, cardinality(schule.stufe_etappen(v_x.lernender_id, schule.thema_einheit(v_x.thema_id)));
  end loop;
  raise notice 'Test 0: % eingeplante Zusatz-Teile mit art normal', v_n;
end $$;

\ir ../migrations/20261126_zp_s_zusatz_plan.sql
\ir ../migrations/20261126_zp_s_zusatz_plan.sql

-- Test 1: Einspielen ändert keine Kinderdaten; bestehende eingeplante Zusatz-Teile werden als „Zusatz · eingeplant“ geführt
do $$
declare v_x record; v_n int := 0; v_h text;
begin
  v_h := md5(coalesce((select string_agg(k::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel) from schule.karte_stand k join schule.lernender l on l.id = k.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(s::text, '|' order by s.lernender_id, s.einheit_id, s.lernziel) from schule.lernziel_stand s join schule.lernender l on l.id = s.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(s::text, '|' order by s.lernender_id, s.thema_id) from schule.lernstand s join schule.lernender l on l.id = s.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(s::text, '|' order by s.id) from schule.sterne s join schule.lernender l on l.id = s.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(f::text, '|' order by f.lernender_id, f.einheit_id) from schule.flug_erstabschluss f join schule.lernender l on l.id = f.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(r::text, '|' order by r.id) from schule.route r join schule.lernender l on l.id = r.lernender_id where not l.ist_test), ''));
  if v_h is distinct from (select h from zp_rt_vorher) then
    -- erlaubt nur, wenn ein eingeplanter Zusatz-Teil schon vor dem Einspielen ganz selbst gelandet war (dann Abschluss beim Einspielen)
    if not exists (select 1 from schule.route r join schule.block_thema bt on bt.block_id = r.block_id join schule.lernender l on l.id = r.lernender_id
                    where not l.ist_test and schule.zusatz_eingeplant(r.lernender_id, bt.thema_id) and schule.zusatz_gelandet(r.lernender_id, schule.thema_einheit(bt.thema_id))) then
      raise exception 'Test 1: Einspielen verändert Kinderdaten'; end if;
    raise notice 'Test 1: beim Einspielen eingeplanten, ganz gelandeten Zusatz-Teil abgeschlossen';
  end if;
  if (select ro from zp_rt_vorher) is distinct from (select jsonb_object_agg(l.id, schule.reiseoptionen(l.id)) from schule.lernender l where l.aktiv) then
    raise exception 'Test 1: Reiseoptionen verändert'; end if;
  for v_x in select r.id, r.lernender_id, bt.thema_id from schule.route r join schule.block_thema bt on bt.block_id = r.block_id join schule.thema t on t.id = bt.thema_id
              where schule.ist_plan(r) and r.status not in ('entfernt') and schule.kind_gruppe(r.lernender_id) = any(t.zusatz) and not (t.id = any(r.ausgelassen)) loop
    v_n := v_n + 1;
    if not coalesce((schule.thema_stufe(v_x.lernender_id, v_x.thema_id)->>'zusatz_eingeplant')::boolean, false)
       or (schule.thema_stufe(v_x.lernender_id, v_x.thema_id)->>'etappen')::int <> cardinality(schule.etappen_alle(schule.thema_einheit(v_x.thema_id))) then
      raise exception 'Test 1: Plan-Eintrag % nicht als Zusatz · eingeplant geführt', v_x.id; end if;
  end loop;
  raise notice 'Test 1 ok: Kinderdaten und Reiseoptionen unverändert; % bestehende eingeplante Zusatz-Teile als „Zusatz · eingeplant“ mit allen Etappen', v_n;
end $$;

-- Testkind (Gruppe gym_by): zwei Zusatz-Teile der Gruppe – A wird eingeplant, B bleibt freiwillig
do $$
declare v_l bigint; v_sa text; v_zw text; v_a record; v_b record; v_lz text[]; v_i int; v_st jsonb; v_n int; v_s0 int; v_ro text; v_plan jsonb; v_k jsonb; v_f jsonb; v_r schule.route;
begin
  select id, schulart, zweig into v_l, v_sa, v_zw from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'kein Testkind'; end if;
  update schule.lernender set schulart = 'gym_by', zweig = null where id = v_l;
  select t.id, schule.thema_einheit(t.id) e, (select bt.block_id from schule.block_thema bt where bt.thema_id = t.id order by bt.block_id limit 1) b into v_a
    from schule.thema t where 'gym_by' = any(t.zusatz) and schule.thema_einheit(t.id) is not null
     and (select count(*) from schule.block_thema bt where bt.thema_id = t.id) = 1 order by t.teil_stamm, t.teil_nr limit 1;
  select t.id, schule.thema_einheit(t.id) e, (select bt.block_id from schule.block_thema bt where bt.thema_id = t.id order by bt.block_id limit 1) b into v_b
    from schule.thema t where 'gym_by' = any(t.zusatz) and schule.thema_einheit(t.id) is not null and t.id <> v_a.id
     and (select count(*) from schule.block_thema bt where bt.thema_id = t.id) = 1 order by t.teil_stamm, t.teil_nr limit 1;
  if v_a.id is null or v_b.id is null then raise exception 'Test: zwei Zusatz-Teile im Gymnasium nötig'; end if;
  -- Ausgang: keine Karten, kein Plan-Eintrag, kein Stempel für A und B beim Testkind
  update schule.karte_stand set sitzt = false, sitzt_am = null, gesetzt_am = null where lernender_id = v_l and einheit_id in (v_a.e, v_b.e);
  update schule.route set status = 'entfernt' where lernender_id = v_l and block_id in (v_a.b, v_b.b) and status <> 'entfernt';
  if exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id in (v_a.e, v_b.e))
     or exists (select 1 from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug in ('block:' || v_a.b, 'block:' || v_b.b)) then
    raise exception 'Test: Testkind hat schon Stempel/Ort-Sterne für die Zusatz-Teile'; end if;
  v_s0 := (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l and grund = 'ort');
  v_ro := md5(schule.reiseoptionen(v_l)::text);

  -- Test 2: einplanen (wie die App über schule_plan_setzen: bisheriger Plan + Ort A)
  if to_regprocedure('schule.plan_setzen_intern(bigint, jsonb, text)') is not null then
    select jsonb_agg(jsonb_build_object('block_id', x.block_id) order by x.o) into v_plan from (
      select r.block_id, r.position o from schule.route r where r.lernender_id = v_l and schule.ist_plan(r) and r.block_id <> v_a.b
      union all select v_a.b, 2147483647) x;
    perform schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', v_plan), 'eltern:Rauchtest');
  else   -- Nachbau ohne plan_setzen_intern: Eintrag wie plan_setzen ihn neu anlegt
    insert into schule.route (lernender_id, block_id, position, art, status, kann_schon, ausgelassen, kann_schon_themen, kann_wdh_themen, revision, geaendert_von, geaendert_am)
    values (v_l, v_a.b, (select coalesce(max(position), 0) + 1 from schule.route where lernender_id = v_l and position < 1000000), 'normal', 'offen', false, '{}', '{}', '{}', 1, 'eltern:Rauchtest', now());
  end if;
  select r.* into v_r from schule.route r where r.lernender_id = v_l and r.block_id = v_a.b and schule.ist_plan(r) order by r.id limit 1;
  if v_r.id is null or v_r.art <> 'normal' or v_r.status <> 'offen' then raise exception 'Test 2: Zusatz-Teil nicht im Plan'; end if;
  v_st := schule.thema_stufe(v_l, v_a.id);
  v_lz := schule.etappen_alle(v_a.e);
  if not coalesce((v_st->>'zusatz_eingeplant')::boolean, false) or (v_st->>'etappen')::int <> cardinality(v_lz) or v_st->>'stufe' <> 'kommt' then
    raise exception 'Test 2: Stufe nicht „Zusatz · eingeplant“: %', v_st; end if;
  if coalesce((schule.thema_stufe(v_l, v_b.id)->>'zusatz_eingeplant')::boolean, false) then raise exception 'Test 2: nicht eingeplanter Zusatz als eingeplant'; end if;
  raise notice 'Test 2 ok: Zusatz-Teil eingeplant (art normal), Stufe „kommt“, zusatz_eingeplant, % Etappen', cardinality(v_lz);

  -- Test 3: landen – Fortschritt über alle Etappen, kein Abschluss vor der letzten Etappe, kein Flug-Test
  for v_i in 1..cardinality(v_lz) loop
    insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am, richtig) values (v_l, v_a.e, v_lz[v_i], true, now(), 3)
    on conflict (lernender_id, einheit_id, lernziel) do update set sitzt = true, sitzt_am = now(), gesetzt_am = null;
    v_st := schule.thema_stufe(v_l, v_a.id);
    if (v_st->>'gelandet')::int <> v_i then raise exception 'Test 3: Fortschritt % statt %', v_st->>'gelandet', v_i; end if;
    if v_i < cardinality(v_lz) and (exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_a.e)
         or (select status from schule.route where id = v_r.id) = 'fertig') then raise exception 'Test 3: Abschluss vor der letzten Etappe'; end if;
  end loop;
  if v_st->>'stufe' not in ('wiederholung', 'komplett') or (v_st->>'test_offen')::boolean then raise exception 'Test 3: Stufe nach allen Landungen: %', v_st; end if;
  if to_regprocedure('schule.test_starten_intern(bigint, jsonb)') is not null
     and (schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_a.e, 'art', 'blocktest'))->>'grund') is distinct from 'nichts_zu_testen' then
    raise exception 'Test 3: Flug-Test wird verlangt'; end if;
  if (schule.nachtest_stand(v_l, v_a.e)->>'faellig')::boolean then raise exception 'Test 3: Nachtest verlangt'; end if;
  raise notice 'Test 3 ok: Fortschritt 1..% über alle Etappen, Stufe %, kein Flug-Test, kein Nachtest (Grund %)', cardinality(v_lz), v_st->>'stufe', schule.nachtest_stand(v_l, v_a.e)->>'grund';

  -- Test 4: Abschluss mit Stempel und 100 Sternen genau einmal
  if (select status from schule.route where id = v_r.id) <> 'fertig' then raise exception 'Test 4: Ort nicht fertig'; end if;
  if (select count(*) from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_a.e) <> 1 then raise exception 'Test 4: kein Stempel'; end if;
  if (select count(*) from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug = 'block:' || v_a.b) <> 1
     or (select menge from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug = 'block:' || v_a.b) <> schule.sterne_regel('sterne_ort_geschafft') then
    raise exception 'Test 4: Ort-Sterne nicht genau einmal'; end if;
  -- noch einmal landen, Plan neu speichern: nichts doppelt
  update schule.karte_stand set sitzt = false where lernender_id = v_l and einheit_id = v_a.e and lernziel = v_lz[1];
  update schule.karte_stand set sitzt = true, sitzt_am = now() where lernender_id = v_l and einheit_id = v_a.e and lernziel = v_lz[1];
  perform schule.zusatz_plan_abgleich(v_l);
  if (select count(*) from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_a.e) <> 1
     or (select count(*) from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug = 'block:' || v_a.b) <> 1 then raise exception 'Test 4: doppelt gebucht'; end if;
  raise notice 'Test 4 ok: Ort fertig, ein Stempel, % Sterne genau einmal', schule.sterne_regel('sterne_ort_geschafft');

  -- Test 5: nichts dahinter gesperrt – keine harte Voraussetzung und kein Visum der Gruppe auf A
  if exists (select 1 from schule.voraussetzung_schulart v where v.braucht_id = v_a.id and v.gruppe = 'gym_by' and v.art = 'hart')
     or exists (select 1 from schule.v_ort_visum v where v.braucht_ort_id = v_a.b and v.gruppe = 'gym_by') then raise exception 'Test 5: Zusatz-Teil sperrt etwas'; end if;
  raise notice 'Test 5 ok: kein Visum, keine harte Voraussetzung auf den Zusatz-Teil';

  -- Test 6: Anzeige – Matrix, Plan (Stufe je Thema), Reisekarte
  v_k := schule.lehrplan_matrix(array[v_l], true);
  if not coalesce((v_k->'lernstand'->(v_l::text)->(v_a.id::text)->>'zusatz_eingeplant')::boolean, false) then raise exception 'Test 6: Matrix ohne zusatz_eingeplant'; end if;
  v_k := schule.reise_karte(v_l);
  select f into v_f from jsonb_array_elements(v_k->'kontinente') k, jsonb_array_elements(k->'fluege') f where (f->>'thema_id')::bigint = v_a.id;
  if v_f is not null and (not (v_f->>'zusatz_eingeplant')::boolean or not (v_f->>'stempel')::boolean
       or (select count(*) from jsonb_array_elements(v_f->'staedte') s where (s->>'zaehlt')::boolean) <> jsonb_array_length(v_f->'staedte')) then
    raise exception 'Test 6: Reisekarte ohne Zusatz · eingeplant'; end if;
  raise notice 'Test 6 ok: Matrix und Reisekarte zeigen „Zusatz · eingeplant“%', case when v_f is null then ' (Reisekarte: Teil ohne Land)' else '' end;

  -- Test 7: nicht eingeplanter Zusatz B – ganz gelandet, trotzdem kein Stempel und keine Ort-Sterne
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am, richtig)
  select v_l, v_b.e, x, true, now(), 3 from unnest(schule.etappen_alle(v_b.e)) x
  on conflict (lernender_id, einheit_id, lernziel) do update set sitzt = true, sitzt_am = now(), gesetzt_am = null;
  if exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_b.e)
     or exists (select 1 from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug = 'block:' || v_b.b)
     or coalesce((schule.thema_stufe(v_l, v_b.id)->>'zusatz_eingeplant')::boolean, false) then raise exception 'Test 7: freiwilliger Zusatz bekommt Stempel/Sterne'; end if;
  raise notice 'Test 7 ok: nicht eingeplanter Zusatz ohne Stempel und Ort-Sterne';

  -- Test 8: Gruppenwechsel – A wird Pflicht → Ort wieder offen, Flug-Test steht an; zurück → wieder fertig; nichts doppelt
  if exists (select 1 from schule.thema where id = v_a.id and not ('rs_I' = any(zusatz))) then
    update schule.lernender set schulart = 'rs_by', zweig = 'rs_I' where id = v_l;
    if (select status from schule.route where id = v_r.id) <> 'offen' then raise exception 'Test 8: Ort nach Wechsel zu Pflicht nicht wieder offen'; end if;
    v_st := schule.thema_stufe(v_l, v_a.id);
    if coalesce((v_st->>'zusatz_eingeplant')::boolean, false) or not (v_st->>'test_offen')::boolean then raise exception 'Test 8: Pflicht-Regel greift nicht: %', v_st; end if;
    update schule.lernender set schulart = 'gym_by', zweig = null where id = v_l;
    if (select status from schule.route where id = v_r.id) <> 'fertig' then raise exception 'Test 8: Ort nach Rückwechsel nicht fertig'; end if;
    if (select count(*) from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_a.e) <> 1
       or (select count(*) from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug = 'block:' || v_a.b) <> 1 then raise exception 'Test 8: doppelt gebucht'; end if;
    raise notice 'Test 8 ok: Gruppenwechsel – Pflicht: Ort offen, Test steht an; zurück: fertig; Stempel und Sterne einmal';
  end if;

  -- Test 9: übrige Ort-Sterne des Testkinds unverändert (nur A dazu)
  if (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l and grund = 'ort') <> v_s0 + schule.sterne_regel('sterne_ort_geschafft') then
    raise exception 'Test 9: Ort-Sterne verändert'; end if;
  raise notice 'Test 9 ok: Ort-Sterne nur für den eingeplanten Zusatz-Teil';
  update schule.lernender set schulart = v_sa, zweig = v_zw where id = v_l;
end $$;

rollback;
