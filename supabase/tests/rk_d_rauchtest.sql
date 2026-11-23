-- Rauchtest RK-D (Reisekarte: gesperrt mit Grund, abgelegt – je Flug und je Stadt). Transaktion mit Rollback; Änderungen nur am Testkind.
-- Spielt 20261129_rk_d_karte_felder.sql selbst ein (zweimal). Vergleich der übrigen Felder gegen die Antwort vor dem Einspielen. Ausgabe nur Zahlen.
-- Aufruf aus dem Repo-Wurzelverzeichnis: psql -v ON_ERROR_STOP=1 -f supabase/tests/rk_d_rauchtest.sql
begin;

-- neue Felder entfernen → muss die bisherige Antwort ergeben
create function pg_temp.rk_ohne(p jsonb) returns jsonb language sql as $$
  select p || jsonb_build_object('kontinente', coalesce((select jsonb_agg(k || jsonb_build_object('fluege', coalesce((
      select jsonb_agg((f - 'gesperrt' - 'gesperrt_grund' - 'ab_klasse' - 'visum_fehlt' - 'abgelegt')
                       || jsonb_build_object('staedte', coalesce((select jsonb_agg(c - 'gesperrt' - 'gesperrt_grund' - 'ab_klasse' - 'abgelegt' - 'abgelegt_am' order by co)
                                                                    from jsonb_array_elements(f->'staedte') with ordinality cc(c, co)), '[]'::jsonb)) order by fo)
        from jsonb_array_elements(k->'fluege') with ordinality ff(f, fo)), '[]'::jsonb)) order by ko)
    from jsonb_array_elements(p->'kontinente') with ordinality kk(k, ko)), '[]'::jsonb));
$$;
create temp table rk_vorher on commit drop as select l.id, pg_temp.rk_ohne(schule.reise_karte(l.id)) j from schule.lernender l where l.aktiv;

\ir ../migrations/20261129_rk_d_karte_felder.sql
\ir ../migrations/20261129_rk_d_karte_felder.sql

-- api-Antwort ohne Schlüssel (nur Zugriffsprüfung ersetzt)
do $$
declare d text := pg_get_functiondef('api.schule_reise_karte(text, jsonb)'::regprocedure);
begin
  if position('perform schule.zugriff(p_schluessel, v_l);' in d) = 0 then raise exception 'RK-D-Test: Anker zugriff fehlt'; end if;
  execute replace(replace(d, 'FUNCTION api.schule_reise_karte(', 'FUNCTION pg_temp.rk_api('), 'perform schule.zugriff(p_schluessel, v_l);', '');
end $$;
create function pg_temp.rk_flug(p_l bigint, p_thema bigint) returns jsonb language sql as $$
  select f from jsonb_array_elements(pg_temp.rk_api('', jsonb_build_object('lernender_id', p_l))->'kontinente') k, jsonb_array_elements(k->'fluege') f
   where (f->>'thema_id')::bigint = p_thema;
$$;

-- Test 1: übrige Felder unverändert (md5), alle Flüge und Städte haben die neuen Felder; Dauer
do $$
declare v_l record; v_alt jsonb; v_neu jsonb; t0 timestamptz; v_ms int := 0; v_n int; v_g int; v_s int;
begin
  for v_l in select id from schule.lernender where aktiv order by id loop
    select j into v_alt from rk_vorher where id = v_l.id;
    t0 := clock_timestamp(); v_neu := pg_temp.rk_api('', jsonb_build_object('lernender_id', v_l.id)); v_ms := greatest(v_ms, (extract(epoch from clock_timestamp() - t0) * 1000)::int);
    if md5((pg_temp.rk_ohne(v_neu) - 'ok' - 'lernender_id')::text) <> md5((v_alt)::text) then raise exception 'FEHLER 1: übrige Felder verändert (Kind %)', v_l.id; end if;
    if exists (select 1 from jsonb_array_elements(v_neu->'kontinente') k, jsonb_array_elements(k->'fluege') f
                where not (f ?& array['gesperrt', 'gesperrt_grund', 'ab_klasse', 'visum_fehlt', 'abgelegt'])
                   or exists (select 1 from jsonb_array_elements(f->'staedte') c where not (c ?& array['gesperrt', 'gesperrt_grund', 'ab_klasse', 'abgelegt', 'abgelegt_am']))) then
      raise exception 'FEHLER 1: Felder fehlen (Kind %)', v_l.id; end if;
    select count(*), count(*) filter (where (f->>'gesperrt')::boolean), sum((select count(*) from jsonb_array_elements(f->'staedte') c where (c->>'gesperrt')::boolean))
      into v_n, v_g, v_s from jsonb_array_elements(v_neu->'kontinente') k, jsonb_array_elements(k->'fluege') f;
    raise notice 'Test 1: Kind %: % Flüge, davon gesperrt % (Visum %, Klasse %), gesperrte Städte %', v_l.id, v_n, v_g,
      (select count(*) from jsonb_array_elements(v_neu->'kontinente') k, jsonb_array_elements(k->'fluege') f where f->>'gesperrt_grund' = 'visum'),
      (select count(*) from jsonb_array_elements(v_neu->'kontinente') k, jsonb_array_elements(k->'fluege') f where f->>'gesperrt_grund' = 'klasse'), v_s;
  end loop;
  raise notice 'Test 1: übrige Felder gleich (md5), neue Felder vollständig, Dauer je Kind höchstens % ms: OK', v_ms;
end $$;

-- Test 2: Regeln je Flug/Stadt gegen eine unabhängige Nachrechnung (Grund nur ohne Fortschritt; Stadt nur bei Stand offen)
do $$
declare v_l record; v_f int;
begin
  for v_l in select id, klasse, schulart from schule.lernender where aktiv loop
    select count(*) into v_f from jsonb_array_elements(pg_temp.rk_api('', jsonb_build_object('lernender_id', v_l.id))->'kontinente') k, jsonb_array_elements(k->'fluege') f
     where ((f->>'gesperrt')::boolean is distinct from (f->>'gesperrt_grund' is not null))
        or (f->>'gesperrt_grund' is not null and (coalesce((f->>'stempel')::boolean, false) or f->>'gesetzt' is not null or f->>'stufe' in ('dran', 'wiederholung', 'komplett')))
        or (f->>'gesperrt_grund' = 'visum' and jsonb_array_length(f->'visum_fehlt') = 0)
        or (f->>'gesperrt_grund' = 'klasse' and ((f->>'im_plan')::boolean or (f->>'ab_klasse')::int <= v_l.klasse))
        or (f->>'gesperrt_grund' is null and jsonb_array_length(f->'visum_fehlt') > 0 and not (coalesce((f->>'stempel')::boolean, false) or f->>'gesetzt' is not null
                                                                                               or f->>'stufe' in ('dran', 'wiederholung', 'komplett') or (f->>'golden')::boolean))
        or (f->>'ab_klasse')::int is distinct from (schule.thema_jahrgang((f->>'thema_id')::bigint)->>coalesce(v_l.schulart, 'gym_by'))::int + case when v_l.schulart = 'ib_myp' then 5 else 0 end
        or exists (select 1 from jsonb_array_elements(f->'staedte') c where (c->>'ab_klasse')::int is distinct from (f->>'ab_klasse')::int)
        or exists (select 1 from jsonb_array_elements(f->'staedte') c where (c->>'gesperrt')::boolean and c->>'stand' <> 'offen')
        or exists (select 1 from jsonb_array_elements(f->'staedte') c where (f->>'gesperrt')::boolean and c->>'stand' = 'offen' and c->>'gesperrt_grund' is distinct from f->>'gesperrt_grund');
    if v_f > 0 then raise exception 'FEHLER 2: % Flüge mit widersprüchlichem Sperr-Stand (Kind %)', v_f, v_l.id; end if;
  end loop;
  raise notice 'Test 2: Sperr-Grund nur ohne Fortschritt, Visum mit Liste, Klasse nur außerhalb des Plans (ab_klasse = thema_jahrgang), Städte wie Flug: OK';
end $$;

-- Test 3 (Testkind): Visum fehlt → gesperrt; Voraussetzungs-Ort erledigt → frei. Klasse: nicht im Plan und höher → gesperrt; eingeplant → frei.
-- abgelegt: Etappe und Flug abgelegt → Stadt/Flug abgelegt mit Datum.
do $$
declare v_l bigint; v_kl int; v_sa text; v_zw text; v_t bigint; v_b bigint; v_vor bigint; v_f jsonb; v_e bigint; v_lz text;
begin
  select id, klasse, schulart, zweig into v_l, v_kl, v_sa, v_zw from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise notice 'Test 3: kein Testkind – übersprungen'; return; end if;
  update schule.lernender set schulart = 'gym_by', zweig = null, klasse = 5 where id = v_l;
  -- Visum: Flug, dessen Ort eine harte Voraussetzung hat; Testkind ohne Fortschritt dort
  select f_t, v.ort_id, v.braucht_ort_id into v_t, v_b, v_vor
    from schule.v_ort_visum v cross join lateral (select bt.thema_id f_t from schule.block_thema bt where bt.block_id = v.ort_id order by bt.reihenfolge limit 1) x
   where v.gruppe = 'gym_by' and exists (select 1 from schule.reise_land rl where rl.art = 'flug' and rl.thema_id = x.f_t)
     and schule.thema_einheit(x.f_t) is not null
     and not exists (select 1 from schule.v_ort_visum v2 where v2.ort_id = v.ort_id and v2.gruppe = 'gym_by' and v2.braucht_ort_id <> v.braucht_ort_id)
   order by v.ort_id limit 1;
  if v_t is not null then
    update schule.route set status = 'entfernt' where lernender_id = v_l and block_id in (v_b, v_vor);
    update schule.karte_stand set sitzt = false, sitzt_am = null, richtig = 0, falsch = 0 where lernender_id = v_l and einheit_id = schule.thema_einheit(v_t);
    v_f := pg_temp.rk_flug(v_l, v_t);
    if v_f->>'gesperrt_grund' <> 'visum' or not exists (select 1 from jsonb_array_elements(v_f->'visum_fehlt') x where (x->>'block_id')::bigint = v_vor) then
      raise exception 'FEHLER 3: Visum nicht gesperrt: %', v_f - 'staedte' - 'mitte' - 'hauptstadt'; end if;
    insert into schule.route (lernender_id, block_id, position, art, status, geaendert_von)
      values (v_l, v_vor, (select coalesce(max(position), 0) + 1 from schule.route where lernender_id = v_l), 'normal', 'fertig', 'eltern:Test');
    v_f := pg_temp.rk_flug(v_l, v_t);
    if v_f->>'gesperrt_grund' = 'visum' or jsonb_array_length(v_f->'visum_fehlt') > 0 then raise exception 'FEHLER 3: Visum nach erledigtem Ort noch gesperrt'; end if;
    raise notice 'Test 3a: Visum fehlt → gesperrt (Ort %), Voraussetzung erledigt → kein Visum-Grund: OK', v_vor;
  else
    raise notice 'Test 3a: kein Ort mit genau einer harten Voraussetzung – übersprungen';
  end if;
  -- Klasse: ein Flug ab Klasse > 5, nicht im Plan, ohne Visum-Bedarf
  select (f->>'thema_id')::bigint into v_t from jsonb_array_elements(pg_temp.rk_api('', jsonb_build_object('lernender_id', v_l))->'kontinente') k, jsonb_array_elements(k->'fluege') f
   where f->>'gesperrt_grund' = 'klasse' order by (f->>'ab_klasse')::int desc limit 1;
  if v_t is null then raise exception 'FEHLER 3: kein Flug „ab Klasse“ gesperrt (Testkind Kl. 5)'; end if;
  v_f := pg_temp.rk_flug(v_l, v_t);
  if (v_f->>'ab_klasse')::int <= 5 or exists (select 1 from jsonb_array_elements(v_f->'staedte') c where c->>'stand' = 'offen' and c->>'gesperrt_grund' is distinct from 'klasse') then
    raise exception 'FEHLER 3: Klasse/Städte: %', v_f - 'mitte' - 'hauptstadt'; end if;
  select bt.block_id into v_b from schule.block_thema bt where bt.thema_id = v_t order by bt.block_id limit 1;
  insert into schule.route (lernender_id, block_id, position, art, status, geaendert_von)
    values (v_l, v_b, (select coalesce(max(position), 0) + 1 from schule.route where lernender_id = v_l), 'normal', 'offen', 'eltern:Test');
  v_f := pg_temp.rk_flug(v_l, v_t);
  if (v_f->>'im_plan')::boolean and (v_f->>'gesperrt_grund' = 'klasse' or exists (select 1 from jsonb_array_elements(v_f->'staedte') c where c->>'gesperrt_grund' = 'klasse')) then
    raise exception 'FEHLER 3: eingeplanter Flug noch „ab Klasse“ gesperrt'; end if;
  raise notice 'Test 3b: Flug ab Klasse % bei Kl. 5 gesperrt (Städte auch), eingeplant → frei: OK', v_f->>'ab_klasse';
  -- abgelegt
  v_e := schule.thema_einheit(v_t); v_lz := (select c->>'lernziel' from jsonb_array_elements(v_f->'staedte') c order by (c->>'nr')::int limit 1);
  insert into schule.abgelegt (lernender_id, bezug, art, einheit_id, lernziel, thema_id, block_id, sterne)
    values (v_l, 'etappe:' || v_e || ':' || v_lz, 'etappe', v_e, v_lz, v_t, v_b, 0), (v_l, 'flug:' || v_t, 'flug', v_e, null, v_t, v_b, 0) on conflict do nothing;
  v_f := pg_temp.rk_flug(v_l, v_t);
  if not (v_f->>'abgelegt')::boolean or not exists (select 1 from jsonb_array_elements(v_f->'staedte') c where c->>'lernziel' = v_lz and (c->>'abgelegt')::boolean and c->>'abgelegt_am' is not null)
     or exists (select 1 from jsonb_array_elements(v_f->'staedte') c where c->>'lernziel' <> v_lz and (c->>'abgelegt')::boolean) then
    raise exception 'FEHLER 3: abgelegt nicht richtig'; end if;
  raise notice 'Test 3c: Etappe und Flug abgelegt → Stadt (mit Datum) und Flug abgelegt, andere Städte nicht: OK';
  update schule.lernender set schulart = v_sa, zweig = v_zw, klasse = v_kl where id = v_l;
end $$;

rollback;
