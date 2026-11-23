-- Rauchtest ZP-S (eingeplanter Zusatz-Teil). Alles in einer Transaktion mit Rollback; Änderungen nur am Testkind.
-- Voraussetzung: LZ-S eingespielt. Spielt 20261126_zp_s_zusatz_plan.sql selbst ein (wiederholbar). Ausgabe nur Zahlen.
-- api-Antworten (Übersicht, Plan) als pg_temp-Kopien ohne Schlüssel (nur die Zugriffsprüfung ersetzt, jeder Anker geprüft).
-- Aufruf aus dem Repo-Wurzelverzeichnis: psql -v ON_ERROR_STOP=1 -f supabase/tests/zp_s_rauchtest.sql
begin;

create function pg_temp.zp_kinder_h() returns text language sql as $$
  select md5(coalesce((select string_agg(k::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel) from schule.karte_stand k join schule.lernender l on l.id = k.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(s::text, '|' order by s.lernender_id, s.einheit_id, s.lernziel) from schule.lernziel_stand s join schule.lernender l on l.id = s.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(s::text, '|' order by s.lernender_id, s.thema_id) from schule.lernstand s join schule.lernender l on l.id = s.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(s::text, '|' order by s.id) from schule.sterne s join schule.lernender l on l.id = s.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(f::text, '|' order by f.lernender_id, f.einheit_id) from schule.flug_erstabschluss f join schule.lernender l on l.id = f.lernender_id where not l.ist_test), '')
          || coalesce((select string_agg(r::text, '|' order by r.id) from schule.route r join schule.lernender l on l.id = r.lernender_id where not l.ist_test), ''));
$$;
create temp table zp_rt_vorher on commit drop as
  select pg_temp.zp_kinder_h() h, (select jsonb_object_agg(l.id, schule.reiseoptionen(l.id)) from schule.lernender l where l.aktiv) ro;

-- Test 0 (lesend, vor ZP-S): bliebe ein eingeplanter Zusatz-Teil mit art 'normal' und leerer Pflichtliste für immer offen?
do $$
declare v_x record; v_n int := 0;
begin
  if position('zusatz_geschafft' in pg_get_functiondef('schule.ort_stand(bigint, bigint)'::regprocedure)) > 0 then
    raise notice 'Test 0: ZP-S schon eingespielt – Vorher-Prüfung entfällt'; return; end if;
  for v_x in select r.id, r.lernender_id, bt.thema_id from schule.route r join schule.block_thema bt on bt.block_id = r.block_id join schule.thema t on t.id = bt.thema_id
              where schule.ist_plan(r) and r.status not in ('fertig', 'entfernt') and schule.kind_gruppe(r.lernender_id) = any(t.zusatz) and not (t.id = any(r.ausgelassen)) loop
    v_n := v_n + 1;
    raise notice 'Test 0: Plan-Eintrag % (Kind %, Thema %): Etappen der Regel %, Pflicht-Zeilen %, Ort abschließbar: nein',
      v_x.id, v_x.lernender_id, v_x.thema_id, cardinality(schule.stufe_etappen(v_x.lernender_id, schule.thema_einheit(v_x.thema_id))),
      (select count(*) from schule.lernziel_stand s where s.lernender_id = v_x.lernender_id and s.einheit_id = schule.thema_einheit(v_x.thema_id) and s.pflicht);
  end loop;
  raise notice 'Test 0: % eingeplante Zusatz-Teile mit art normal (ohne ZP-S für immer offen)', v_n;
end $$;

-- bestehende eingeplante Zusatz-Einträge vorher (Platz, Absicht)
create temp table zp_rt_eintrag on commit drop as
  select r.id, r.lernender_id, r.block_id, r.position, r.art, r.status, r.geaendert_von from schule.route r
    join schule.block_thema bt on bt.block_id = r.block_id join schule.thema t on t.id = bt.thema_id
   where schule.ist_plan(r) and r.status <> 'entfernt' and schule.kind_gruppe(r.lernender_id) = any(t.zusatz) and not (t.id = any(r.ausgelassen));

\ir ../migrations/20261126_zp_s_zusatz_plan.sql
\ir ../migrations/20261126_zp_s_zusatz_plan.sql

-- pg_temp-Kopien der api-Antworten ohne Schlüssel
create function pg_temp.zp_ersetzen(d text, a text, n text) returns text language plpgsql as $$
begin
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'ZP-Test: Anker nicht genau einmal: %', left(a, 60); end if;
  return replace(d, a, n);
end $$;
do $$
declare d text;
begin
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  d := pg_temp.zp_ersetzen(d, 'FUNCTION api.schule_uebersicht(', 'FUNCTION pg_temp.zp_uebersicht(');
  d := pg_temp.zp_ersetzen(d, 'v_tn := schule.wer_tn(p_schluessel);', 'v_tn := null;');
  d := pg_temp.zp_ersetzen(d, 'v_leiter := schule.ist_leiter(p_schluessel);', 'v_leiter := true;');
  d := pg_temp.zp_ersetzen(d, 'schule.sieht(p_schluessel, l.id)', 'true');
  execute d;
  d := pg_get_functiondef('api.schule_plan_lesen(text, jsonb)'::regprocedure);
  d := pg_temp.zp_ersetzen(d, 'FUNCTION api.schule_plan_lesen(', 'FUNCTION pg_temp.zp_plan(');
  d := pg_temp.zp_ersetzen(d, 'perform schule.wer_tn(p_schluessel);', '');
  d := pg_temp.zp_ersetzen(d, 'if not schule.ist_leiter(p_schluessel) then', 'if false then');
  execute d;
end $$;

-- Test 1: Einspielen ändert keine Kinderdaten; bestehende Einträge (route 485) behalten Platz und Absicht und werden als „Zusatz · eingeplant“ geführt
do $$
declare v_x record; v_n int := 0; v_ro jsonb; v_k jsonb;
begin
  if pg_temp.zp_kinder_h() is distinct from (select h from zp_rt_vorher) then
    if not exists (select 1 from schule.zusatz_geschafft z join schule.lernender l on l.id = z.lernender_id where not l.ist_test) then
      raise exception 'Test 1: Einspielen verändert Kinderdaten'; end if;
    raise notice 'Test 1: beim Einspielen „Zusatz geschafft“ für einen schon ganz gelandeten Zusatz-Teil gebucht';
  end if;
  for v_x in select * from zp_rt_eintrag loop
    v_n := v_n + 1;
    if (select (r.position, r.art, r.status, r.geaendert_von) from schule.route r where r.id = v_x.id) is distinct from (v_x.position, v_x.art, v_x.status, v_x.geaendert_von) then
      raise exception 'Test 1: Eintrag % verändert', v_x.id; end if;
    if not schule.zusatz_ort(v_x.lernender_id, v_x.block_id) then raise exception 'Test 1: Eintrag % nicht als Zusatz · eingeplant', v_x.id; end if;
    if not exists (select 1 from jsonb_array_elements(pg_temp.zp_plan('', jsonb_build_object('lernender_id', v_x.lernender_id))->'plan') p
                    where (p->>'block_id')::bigint = v_x.block_id and p->>'art' = 'normal' and (p->>'zusatz_eingeplant')::boolean) then
      raise exception 'Test 1: Eintrag % fehlt in der Eltern-Planung', v_x.id; end if;
    select k into v_k from jsonb_array_elements(pg_temp.zp_uebersicht('', null)->'lernende') k where (k->>'id')::bigint = v_x.lernender_id;
    if v_x.status <> 'fertig' and exists (select 1 from jsonb_array_elements(v_k->'route') r where (r->>'block_id')::bigint = v_x.block_id) then
      raise exception 'Test 1: offener Zusatz-Ort % steht in der Kinder-Route (wäre „jetzt“)', v_x.block_id; end if;
    if not exists (select 1 from jsonb_array_elements(v_k->'zusatz_plan') z where (z->>'route_id')::bigint = v_x.id) then raise exception 'Test 1: zusatz_plan ohne Eintrag %', v_x.id; end if;
  end loop;
  -- Reiseoptionen: kein Zusatz-Ort als Weiterflug; nur geändert, wo vorher ein Zusatz-Ort als Weiterflug stand
  for v_x in select l.id from schule.lernender l where l.aktiv loop
    v_ro := schule.reiseoptionen(v_x.id);
    if exists (select 1 from jsonb_array_elements(v_ro->'optionen') o where schule.zusatz_ort(v_x.id, (o->>'ort_id')::bigint)) then
      raise exception 'Test 1: Zusatz-Ort als Weiterflug (Kind %)', v_x.id; end if;
    if v_ro is distinct from (select ro->(v_x.id::text) from zp_rt_vorher)
       and not exists (select 1 from jsonb_array_elements((select ro->(v_x.id::text) from zp_rt_vorher)->'optionen') o where schule.zusatz_ort(v_x.id, (o->>'ort_id')::bigint)) then
      raise exception 'Test 1: Reiseoptionen ohne Grund verändert (Kind %)', v_x.id; end if;
  end loop;
  raise notice 'Test 1 ok: Kinderdaten unverändert; % bestehende Einträge mit Platz und Absicht, in der Eltern-Planung, nicht in der Kinder-Route, im zusatz_plan', v_n;
end $$;

-- Testkind (Gruppe gym_by): Zusatz-Teil A wird eingeplant, B bleibt freiwillig
do $$
declare v_l bigint; v_sa text; v_zw text; v_a record; v_b record; v_lz text[]; v_i int; v_st jsonb; v_s0 int; v_plan jsonb; v_k jsonb; v_f jsonb; v_r schule.route; v_z jsonb;
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
  update schule.karte_stand set sitzt = false, sitzt_am = null, gesetzt_am = null where lernender_id = v_l and einheit_id in (v_a.e, v_b.e);
  update schule.route set status = 'entfernt' where lernender_id = v_l and block_id in (v_a.b, v_b.b) and status <> 'entfernt';
  if exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id in (v_a.e, v_b.e))
     or exists (select 1 from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug in ('block:' || v_a.b, 'block:' || v_b.b)) then
    raise exception 'Test: Testkind hat schon Stempel/Ort-Sterne für die Zusatz-Teile'; end if;
  v_s0 := (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l);
  v_lz := schule.etappen_alle(v_a.e);

  -- Test 2: einplanen wie die App (schule_plan_setzen: bisheriger Plan + A ans Ende), umsortieren (A nach vorn), herausnehmen, wieder einplanen
  select coalesce(jsonb_agg(jsonb_build_object('block_id', r.block_id) order by r.position), '[]') into v_plan
    from schule.route r where r.lernender_id = v_l and schule.ist_plan(r) and r.block_id <> v_a.b;
  perform schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', v_plan || jsonb_build_array(jsonb_build_object('block_id', v_a.b))), 'eltern:Rauchtest');
  select r.* into v_r from schule.route r where r.lernender_id = v_l and r.block_id = v_a.b and r.art = 'normal' order by r.id limit 1;
  if v_r.id is null or v_r.status <> 'offen' or not schule.ist_plan(v_r) then raise exception 'Test 2: Zusatz-Teil nicht im Plan'; end if;
  v_st := schule.thema_stufe(v_l, v_a.id);
  if not coalesce((v_st->>'zusatz_eingeplant')::boolean, false) or (v_st->>'etappen')::int <> cardinality(v_lz) or v_st->>'stufe' <> 'kommt'
     or coalesce((v_st->>'zusatz_geschafft')::boolean, true) then raise exception 'Test 2: Stufe nicht „Zusatz · eingeplant“: %', v_st; end if;
  if not exists (select 1 from jsonb_array_elements(pg_temp.zp_plan('', jsonb_build_object('lernender_id', v_l))->'plan') p
                  where (p->>'block_id')::bigint = v_a.b and p->>'art' = 'normal' and (p->>'zusatz_eingeplant')::boolean) then raise exception 'Test 2: Eltern-Planung ohne Eintrag'; end if;
  perform schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', jsonb_build_array(jsonb_build_object('block_id', v_a.b)) || v_plan), 'eltern:Rauchtest');
  if (select position from schule.route where id = v_r.id) <> 1 or not schule.zusatz_eingeplant(v_l, v_a.id) then raise exception 'Test 2: Umsortieren'; end if;
  perform schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', v_plan), 'eltern:Rauchtest');
  if (select status from schule.route where id = v_r.id) <> 'entfernt' or schule.zusatz_eingeplant(v_l, v_a.id)
     or coalesce((schule.thema_stufe(v_l, v_a.id)->>'zusatz_eingeplant')::boolean, false) then raise exception 'Test 2: Herausnehmen'; end if;
  perform schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', v_plan || jsonb_build_array(jsonb_build_object('block_id', v_a.b))), 'eltern:Rauchtest');
  if (select status from schule.route where id = v_r.id) <> 'offen' or not schule.zusatz_eingeplant(v_l, v_a.id) then raise exception 'Test 2: wieder einplanen'; end if;
  raise notice 'Test 2 ok: eingeplant (art normal, Eltern-Planung mit zusatz_eingeplant), umsortiert, herausgenommen, wieder eingeplant; Stufe „kommt“, % Etappen', cardinality(v_lz);

  -- Test 3: Kinderseite – der offene Zusatz-Ort ist kein Pflicht-Weiterflug, der Flug bleibt sichtbar
  select k into v_k from jsonb_array_elements(pg_temp.zp_uebersicht('', null)->'lernende') k where (k->>'id')::bigint = v_l;
  if exists (select 1 from jsonb_array_elements(v_k->'route') r where (r->>'block_id')::bigint = v_a.b) then raise exception 'Test 3: Zusatz-Ort in der Kinder-Route'; end if;
  if not exists (select 1 from jsonb_array_elements(pg_temp.zp_uebersicht('', null)->'einheiten') e where (e->>'id')::bigint = v_a.e) then raise exception 'Test 3: Flug verschwunden'; end if;
  select z into v_z from jsonb_array_elements(v_k->'zusatz_plan') z where (z->>'thema_id')::bigint = v_a.id;
  if v_z is null or (v_z->>'etappen')::int <> cardinality(v_lz) or (v_z->>'gelandet')::int <> 0 or (v_z->>'geschafft')::boolean then raise exception 'Test 3: zusatz_plan: %', v_z; end if;
  if exists (select 1 from jsonb_array_elements(schule.reiseoptionen(v_l)->'optionen') o where (o->>'ort_id')::bigint = v_a.b) then raise exception 'Test 3: Zusatz-Ort als Weiterflug'; end if;
  if to_regprocedure('schule.naechster_flug(bigint, bigint)') is not null and (schule.naechster_flug(v_l, null)->>'thema_id')::bigint = v_a.id then raise exception 'Test 3: Zusatz als nächster Flug'; end if;
  raise notice 'Test 3 ok: Kinderseite – Zusatz nicht in route, nicht in Reiseoptionen, nicht nächster Flug; Einheit sichtbar; zusatz_plan 0/%', cardinality(v_lz);

  -- Test 4: landen – Fortschritt x/y über alle Etappen, kein Abschluss vor der letzten Etappe, kein Flug-Test, kein Nachtest
  for v_i in 1..cardinality(v_lz) loop
    insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am, richtig) values (v_l, v_a.e, v_lz[v_i], true, now(), 3)
    on conflict (lernender_id, einheit_id, lernziel) do update set sitzt = true, sitzt_am = now(), gesetzt_am = null;
    v_st := schule.thema_stufe(v_l, v_a.id);
    if (v_st->>'gelandet')::int <> v_i then raise exception 'Test 4: Fortschritt % statt %', v_st->>'gelandet', v_i; end if;
    if v_i < cardinality(v_lz) and (exists (select 1 from schule.zusatz_geschafft where lernender_id = v_l and thema_id = v_a.id)
         or exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_a.e)
         or (select status from schule.route where id = v_r.id) = 'fertig') then raise exception 'Test 4: Abschluss vor der letzten Etappe'; end if;
    if v_i = 1 and to_regprocedure('schule.test_starten_intern(bigint, jsonb)') is not null
       and (schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_a.e, 'art', 'blocktest'))->>'grund') is distinct from 'nichts_zu_testen' then
      raise exception 'Test 4: Flug-Test wird verlangt'; end if;
  end loop;
  if (schule.nachtest_stand(v_l, v_a.e)->>'faellig')::boolean or schule.nachtest_stand(v_l, v_a.e)->>'grund' <> 'zusatz' then raise exception 'Test 4: Nachtest'; end if;
  raise notice 'Test 4 ok: Fortschritt 1..% über alle Etappen, kein Flug-Test, kein Nachtest (Grund zusatz)', cardinality(v_lz);

  -- Test 5: „Zusatz geschafft“ – bewusste Buchung: Zeile zusatz_geschafft, Stempel und 100 Sterne je genau einmal, Ort fertig
  if not exists (select 1 from schule.zusatz_geschafft where lernender_id = v_l and thema_id = v_a.id and sterne = schule.sterne_regel('sterne_ort_geschafft')) then raise exception 'Test 5: keine Buchung'; end if;
  if (select count(*) from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_a.e) <> 1 then raise exception 'Test 5: kein Stempel'; end if;
  if (select count(*) from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug = 'block:' || v_a.b) <> 1
     or (select menge from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug = 'block:' || v_a.b) <> schule.sterne_regel('sterne_ort_geschafft') then raise exception 'Test 5: Sterne'; end if;
  if (select status from schule.route where id = v_r.id) <> 'fertig' then raise exception 'Test 5: Ort nicht fertig'; end if;
  v_st := schule.thema_stufe(v_l, v_a.id);
  if not (v_st->>'zusatz_geschafft')::boolean or v_st->>'stufe' not in ('wiederholung', 'komplett') or (v_st->>'test_offen')::boolean then raise exception 'Test 5: Stufe %', v_st; end if;
  -- noch einmal landen, Plan neu speichern, Buchung erneut aufrufen: nichts doppelt
  update schule.karte_stand set sitzt = false where lernender_id = v_l and einheit_id = v_a.e and lernziel = v_lz[1];
  update schule.karte_stand set sitzt = true, sitzt_am = now() where lernender_id = v_l and einheit_id = v_a.e and lernziel = v_lz[1];
  perform schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', v_plan || jsonb_build_array(jsonb_build_object('block_id', v_a.b))), 'eltern:Rauchtest');
  if schule.zusatz_geschafft_buchen(v_l, v_a.id) then raise exception 'Test 5: zweite Buchung'; end if;
  if (select count(*) from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_a.e) <> 1
     or (select count(*) from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug = 'block:' || v_a.b) <> 1 then raise exception 'Test 5: doppelt gebucht'; end if;
  select k into v_k from jsonb_array_elements(pg_temp.zp_uebersicht('', null)->'lernende') k where (k->>'id')::bigint = v_l;
  if not exists (select 1 from jsonb_array_elements(v_k->'route') r where (r->>'block_id')::bigint = v_a.b and r->>'status' = 'fertig') then raise exception 'Test 5: Kinder-Route ohne fertigen Ort'; end if;
  if not exists (select 1 from jsonb_array_elements(v_k->'zusatz_plan') z where (z->>'thema_id')::bigint = v_a.id and (z->>'geschafft')::boolean) then raise exception 'Test 5: zusatz_plan nicht geschafft'; end if;
  raise notice 'Test 5 ok: Zusatz geschafft – ein Stempel, % Sterne genau einmal, Ort fertig, Stufe %', schule.sterne_regel('sterne_ort_geschafft'), v_st->>'stufe';

  -- Test 6: nichts dahinter gesperrt
  if exists (select 1 from schule.voraussetzung_schulart v where v.braucht_id = v_a.id and v.gruppe = 'gym_by' and v.art = 'hart')
     or exists (select 1 from schule.v_ort_visum v where v.braucht_ort_id = v_a.b and v.gruppe = 'gym_by') then raise exception 'Test 6: Zusatz-Teil sperrt etwas'; end if;
  raise notice 'Test 6 ok: kein Visum, keine harte Voraussetzung auf den Zusatz-Teil';

  -- Test 7: Anzeige – Matrix und Reisekarte
  v_k := schule.lehrplan_matrix(array[v_l], true);
  if not coalesce((v_k->'lernstand'->(v_l::text)->(v_a.id::text)->>'zusatz_geschafft')::boolean, false) then raise exception 'Test 7: Matrix ohne zusatz_geschafft'; end if;
  v_k := schule.reise_karte(v_l);
  select f into v_f from jsonb_array_elements(v_k->'kontinente') k, jsonb_array_elements(k->'fluege') f where (f->>'thema_id')::bigint = v_a.id;
  if v_f is not null and (not (v_f->>'zusatz_eingeplant')::boolean or not (v_f->>'zusatz_geschafft')::boolean or not (v_f->>'stempel')::boolean
       or (select count(*) from jsonb_array_elements(v_f->'staedte') s where (s->>'zaehlt')::boolean) <> jsonb_array_length(v_f->'staedte')) then
    raise exception 'Test 7: Reisekarte'; end if;
  if (v_k->'naechster_start'->>'thema_id')::bigint = v_a.id then raise exception 'Test 7: Zusatz als nächster Start'; end if;
  raise notice 'Test 7 ok: Matrix und Reisekarte zeigen „Zusatz · eingeplant/geschafft“; nächster Start bleibt beim Pflicht-Flug';

  -- Test 8: nicht eingeplanter Zusatz B – ganz gelandet, trotzdem keine Buchung
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am, richtig)
  select v_l, v_b.e, x, true, now(), 3 from unnest(schule.etappen_alle(v_b.e)) x
  on conflict (lernender_id, einheit_id, lernziel) do update set sitzt = true, sitzt_am = now(), gesetzt_am = null;
  if exists (select 1 from schule.zusatz_geschafft where lernender_id = v_l and thema_id = v_b.id)
     or exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_b.e)
     or exists (select 1 from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug = 'block:' || v_b.b) then raise exception 'Test 8: freiwilliger Zusatz gebucht'; end if;
  raise notice 'Test 8 ok: nicht eingeplanter Zusatz ohne Stempel und Sterne';

  -- Test 9: Gruppenwechsel – A wird Pflicht → Ort offen, Test steht an; zurück → fertig; nichts doppelt
  if not exists (select 1 from schule.thema where id = v_a.id and 'rs_I' = any(coalesce(zusatz, '{}'))) then
    update schule.lernender set schulart = 'rs_by', zweig = 'rs_I' where id = v_l;
    if (select status from schule.route where id = v_r.id) <> 'offen' then raise exception 'Test 9: Ort nicht wieder offen'; end if;
    v_st := schule.thema_stufe(v_l, v_a.id);
    if coalesce((v_st->>'zusatz_eingeplant')::boolean, false) or not (v_st->>'test_offen')::boolean then raise exception 'Test 9: Pflicht-Regel greift nicht: %', v_st; end if;
    update schule.lernender set schulart = 'gym_by', zweig = null where id = v_l;
    if (select status from schule.route where id = v_r.id) <> 'fertig' then raise exception 'Test 9: Ort nach Rückwechsel nicht fertig'; end if;
    if (select count(*) from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_a.e) <> 1
       or (select count(*) from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug = 'block:' || v_a.b) <> 1 then raise exception 'Test 9: doppelt gebucht'; end if;
    raise notice 'Test 9 ok: Gruppenwechsel – Pflicht: Ort offen, Test steht an; zurück: fertig; nichts doppelt';
  end if;

  -- Test 10: Sterne des Testkinds – nur die 100 für A dazu (Karten direkt gesetzt, keine Übungs-Sterne)
  if (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) <> v_s0 + schule.sterne_regel('sterne_ort_geschafft') then raise exception 'Test 10: Sterne verändert'; end if;
  raise notice 'Test 10 ok: übrige Sterne unverändert';

  -- Test 13 (ChatGPT 966): abgeschlossenen Zusatz-Flug A aus dem Plan nehmen – nichts wird zurückgebucht; wieder einplanen bucht nichts doppelt
  select coalesce(jsonb_agg(jsonb_build_object('block_id', r.block_id) order by r.position), '[]') into v_plan
    from schule.route r where r.lernender_id = v_l and schule.ist_plan(r) and r.block_id <> v_a.b;
  perform schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', v_plan), 'eltern:Rauchtest');
  v_st := schule.thema_stufe(v_l, v_a.id);
  if (select count(*) from schule.zusatz_geschafft where lernender_id = v_l and thema_id = v_a.id) <> 1
     or (select count(*) from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_a.e) <> 1
     or (select count(*) from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug = 'block:' || v_a.b) <> 1
     or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) <> v_s0 + schule.sterne_regel('sterne_ort_geschafft') then
    raise exception 'Test 13: Herausnehmen hat Stempel/Sterne/Abschluss verändert'; end if;
  if exists (select 1 from jsonb_array_elements(schule.zusatz_plan_json(v_l)) z where (z->>'thema_id')::bigint = v_a.id and z->>'status' <> 'fertig') then
    raise exception 'Test 13: herausgenommener Zusatz-Flug noch offen im zusatz_plan'; end if;
  raise notice 'Test 13 ok: abgeschlossener Zusatz herausgenommen – route %, Stufe %, zusatz_eingeplant %, im zusatz_plan %; Stempel, % Sterne und zusatz_geschafft bleiben',
    (select status from schule.route where id = v_r.id), v_st->>'stufe', coalesce(v_st->>'zusatz_eingeplant', 'false'),
    exists (select 1 from jsonb_array_elements(schule.zusatz_plan_json(v_l)) z where (z->>'thema_id')::bigint = v_a.id), schule.sterne_regel('sterne_ort_geschafft');
  perform schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', v_plan || jsonb_build_array(jsonb_build_object('block_id', v_a.b))), 'eltern:Rauchtest');
  perform schule.zusatz_geschafft_buchen(v_l, v_a.id);
  if (select count(*) from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_a.e) <> 1
     or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) <> v_s0 + schule.sterne_regel('sterne_ort_geschafft') then
    raise exception 'Test 13: wieder einplanen bucht doppelt'; end if;
  raise notice 'Test 13 ok: wieder eingeplant – route %, nichts doppelt', (select status from schule.route where id = v_r.id);
  update schule.lernender set schulart = v_sa, zweig = v_zw where id = v_l;
end $$;

-- Test 12 (ChatGPT 966): zwei eingeplante Zusatz-Flüge am selben Ort (heute gibt es keinen solchen Ort – im Test nachgestellt:
-- zwei Themen eines Orts für die Gruppe als Zusatz markiert). Verhalten: je Teil eigener Stempel; 100 Sterne je Ort (bezug block:…) nur einmal.
do $$
declare v_l bigint; v_sa text; v_zw text; v_b bigint; v_t bigint[]; v_e bigint[]; v_plan jsonb; v_s0 int; v_ort int := schule.sterne_regel('sterne_ort_geschafft');
begin
  select id, schulart, zweig into v_l, v_sa, v_zw from schule.lernender where ist_test and aktiv order by id limit 1;
  update schule.lernender set schulart = 'gym_by', zweig = null where id = v_l;
  select bt.block_id, array_agg(bt.thema_id order by bt.reihenfolge), array_agg(schule.thema_einheit(bt.thema_id) order by bt.reihenfolge) into v_b, v_t, v_e
    from schule.block_thema bt
   where schule.thema_einheit(bt.thema_id) is not null
     and not exists (select 1 from schule.block_thema b2 where b2.thema_id = bt.thema_id and b2.block_id <> bt.block_id)
     and not exists (select 1 from schule.flug_erstabschluss f where f.lernender_id = v_l and f.einheit_id = schule.thema_einheit(bt.thema_id))
     and not exists (select 1 from schule.sterne s where s.lernender_id = v_l and s.grund = 'ort' and s.bezug = 'block:' || bt.block_id)
   group by bt.block_id having count(*) = 2 and count(*) = (select count(*) from schule.block_thema b3 where b3.block_id = bt.block_id)
   order by bt.block_id limit 1;
  if v_b is null then raise notice 'Test 12: kein Ort mit zwei Themen frei – übersprungen'; return; end if;
  update schule.thema set zusatz = array(select distinct x from unnest(coalesce(zusatz, '{}') || array['gym_by']) x) where id = any(v_t);
  update schule.karte_stand set sitzt = false, sitzt_am = null, gesetzt_am = null where lernender_id = v_l and einheit_id = any(v_e);
  update schule.route set status = 'entfernt' where lernender_id = v_l and block_id = v_b and status <> 'entfernt';
  select coalesce(jsonb_agg(jsonb_build_object('block_id', r.block_id) order by r.position), '[]') into v_plan from schule.route r where r.lernender_id = v_l and schule.ist_plan(r);
  perform schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', v_plan || jsonb_build_array(jsonb_build_object('block_id', v_b))), 'eltern:Rauchtest');
  if not (schule.zusatz_eingeplant(v_l, v_t[1]) and schule.zusatz_eingeplant(v_l, v_t[2])) then raise exception 'Test 12: nicht beide eingeplant'; end if;
  v_s0 := (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l);
  -- Teil 1 ganz landen
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am, richtig) select v_l, v_e[1], x, true, now(), 3 from unnest(schule.etappen_alle(v_e[1])) x
  on conflict (lernender_id, einheit_id, lernziel) do update set sitzt = true, sitzt_am = now(), gesetzt_am = null;
  if not exists (select 1 from schule.zusatz_geschafft where lernender_id = v_l and thema_id = v_t[1])
     or not exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_e[1])
     or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) <> v_s0 + v_ort then raise exception 'Test 12: Teil 1 nicht gebucht'; end if;
  if (select status from schule.route where lernender_id = v_l and block_id = v_b and status <> 'entfernt' order by id desc limit 1) = 'fertig' then
    raise exception 'Test 12: Ort fertig, obwohl Teil 2 offen'; end if;
  -- Teil 2 ganz landen
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am, richtig) select v_l, v_e[2], x, true, now(), 3 from unnest(schule.etappen_alle(v_e[2])) x
  on conflict (lernender_id, einheit_id, lernziel) do update set sitzt = true, sitzt_am = now(), gesetzt_am = null;
  if not exists (select 1 from schule.zusatz_geschafft where lernender_id = v_l and thema_id = v_t[2])
     or not exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_e[2]) then raise exception 'Test 12: Teil 2 ohne Abschluss/Stempel'; end if;
  if (select count(*) from schule.sterne where lernender_id = v_l and grund = 'ort' and bezug = 'block:' || v_b) <> 1
     or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) <> v_s0 + v_ort then raise exception 'Test 12: Ort-Sterne nicht genau einmal'; end if;
  if (select status from schule.route where lernender_id = v_l and block_id = v_b and status <> 'entfernt' order by id desc limit 1) <> 'fertig' then
    raise exception 'Test 12: Ort nach beiden Teilen nicht fertig'; end if;
  raise notice 'Test 12 ok: zwei Zusatz-Teile am selben Ort – je Teil ein Stempel (2), Ort-Sterne % genau einmal (nicht je Teil), Ort fertig nach dem zweiten; zusatz_geschafft.sterne: Teil 1 %, Teil 2 % (Feld zeigt den Regelwert, gebucht wurde nur einmal)',
    v_ort, (select sterne from schule.zusatz_geschafft where lernender_id = v_l and thema_id = v_t[1]), (select sterne from schule.zusatz_geschafft where lernender_id = v_l and thema_id = v_t[2]);
  update schule.lernender set schulart = v_sa, zweig = v_zw where id = v_l;
end $$;

-- Test 11: Kinderdaten der übrigen Kinder nach allem unverändert
do $$ begin
  if pg_temp.zp_kinder_h() is distinct from (select h from zp_rt_vorher)
     and not exists (select 1 from schule.zusatz_geschafft z join schule.lernender l on l.id = z.lernender_id where not l.ist_test) then
    raise exception 'Test 11: Kinderdaten verändert'; end if;
  raise notice 'Test 11 ok: Karten, Lernstand, Sterne, Stempel und Route der übrigen Kinder unverändert';
end $$;

rollback;
