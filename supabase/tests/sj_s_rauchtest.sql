-- Rauchtest SJ-S („Wie viel ist noch?“ je Schuljahr). Alles in einer Transaktion mit Rollback; Änderungen nur am Testkind.
-- Voraussetzung: LZ-S eingespielt. Spielt ZP-S und SJ-S selbst ein (beide wiederholbar). Ausgabe nur Zahlen.
-- Gegenrechnung unabhängig von SJ-S: Ring-Regel der App (lernLwRing) auf den Daten von schule.lehrplan_matrix (jahrgang, pflicht, ohne_flug,
-- etappen_anzahl, lernstand = thema_stufe), Zusatz-Teile der Gruppe des Kindes abgezogen.
-- Aufruf aus dem Repo-Wurzelverzeichnis: psql -v ON_ERROR_STOP=1 -f supabase/tests/sj_s_rauchtest.sql
begin;

create function pg_temp.sj_h() returns text language sql as $$
  select md5(coalesce((select string_agg(k::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel) from schule.karte_stand k), '')
          || coalesce((select string_agg(s::text, '|' order by s.id) from schule.sterne s), '')
          || coalesce((select string_agg(f::text, '|' order by f.lernender_id, f.einheit_id) from schule.flug_erstabschluss f), '')
          || coalesce((select string_agg(r::text, '|' order by r.id) from schule.route r), ''));
$$;
create temp table sj_rt_vorher on commit drop as select pg_temp.sj_h() h;

\ir ../migrations/20261126_zp_s_zusatz_plan.sql
\ir ../migrations/20261127_sj_s_schuljahr.sql
\ir ../migrations/20261127_sj_s_schuljahr.sql

create function pg_temp.sj_ersetzen(d text, a text, n text) returns text language plpgsql as $$
begin
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'SJ-Test: Anker nicht genau einmal: %', left(a, 60); end if;
  return replace(d, a, n);
end $$;
do $$
declare d text;
begin
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  d := pg_temp.sj_ersetzen(d, 'FUNCTION api.schule_uebersicht(', 'FUNCTION pg_temp.sj_uebersicht(');
  d := pg_temp.sj_ersetzen(d, 'v_tn := schule.wer_tn(p_schluessel);', 'v_tn := null;');
  d := pg_temp.sj_ersetzen(d, 'v_leiter := schule.ist_leiter(p_schluessel);', 'v_leiter := true;');
  d := pg_temp.sj_ersetzen(d, 'schule.sieht(p_schluessel, l.id)', 'true');
  execute d;
  d := pg_get_functiondef('api.schule_konto(text, jsonb)'::regprocedure);
  d := pg_temp.sj_ersetzen(d, 'FUNCTION api.schule_konto(', 'FUNCTION pg_temp.sj_konto(');
  d := pg_temp.sj_ersetzen(d, 'perform schule.zugriff(p_schluessel, v_l);', '');
  execute d;
end $$;

-- Gegenrechnung je Kind und Klasse aus der Lehrplan-Matrix (wie lernLwRing): Pflicht-Flüge, fertig, Etappen, gelandet, Prozent, Ring-Teile
create function pg_temp.sj_ring(p_l bigint) returns jsonb language sql as $$
  with l as (select coalesce(l.schulart, 'gym_by') sa, l.klasse kl, schule.kind_gruppe(l.id) gr from schule.lernender l where l.id = p_l),
  m as (select schule.lehrplan_matrix(array[p_l], false) j),
  t as (select (x->>'thema_id')::bigint id, (x->'jahrgang'->>l.sa)::int + case when l.sa = 'ib_myp' then 5 else 0 end k,
               coalesce(nullif((x->>'etappen_anzahl')::int, 0), nullif((s->>'etappen')::int, 0), 1) n, coalesce(s->>'stufe', 'nicht_im_plan') st, coalesce((s->>'gelandet')::int, 0) gel,
               (l.sa = 'ib_myp' or coalesce(x->'pflicht' ? l.sa, false)) and not coalesce((x->>'ohne_flug')::boolean, false)
                 and not exists (select 1 from schule.thema th where th.id = (x->>'thema_id')::bigint and l.gr = any(coalesce(th.zusatz, '{}'))) pfl
          from l, m, jsonb_array_elements(m.j->'themen') x
          left join lateral (select schule.thema_stufe(p_l, (x->>'thema_id')::bigint) s) s on true),
  r as (select t.k, count(*) n, count(*) filter (where t.st in ('komplett', 'wiederholung')) f, sum(t.n) e,
               sum(case when t.st in ('komplett', 'wiederholung') then t.n else least(t.n, t.gel) end) g,
               coalesce(sum(t.n) filter (where t.st = 'komplett'), 0) kann, coalesce(sum(t.n) filter (where t.st = 'wiederholung'), 0) wdh
          from t, l where t.pfl and t.k between greatest(l.kl - 1, 5) and least(l.kl + 1, 10) group by t.k)
  select coalesce(jsonb_agg(jsonb_build_object('klasse', r.k, 'n', r.n, 'f', r.f, 'e', r.e, 'g', r.g, 'kann', r.kann, 'wdh', r.wdh,
                                               'pz', case when r.e > 0 then round(100.0 * r.g / r.e)::int end) order by r.k), '[]'::jsonb) from r;
$$;
create function pg_temp.sj_kurz(p jsonb) returns jsonb language sql as $$
  select coalesce(jsonb_agg(jsonb_build_object('klasse', (k->>'klasse')::int, 'n', (k->'fluege'->>'gesamt')::int, 'f', (k->'fluege'->>'fertig')::int,
           'e', (k->'etappen'->>'gesamt')::int, 'g', (k->'etappen'->>'gelandet')::int, 'kann', (k->'ring'->>'kann')::int, 'wdh', (k->'ring'->>'wdh')::int,
           'pz', (k->>'prozent')::int) order by (k->>'klasse')::int), '[]'::jsonb)
    from jsonb_array_elements(p->'klassen') k where (k->'fluege'->>'gesamt')::int > 0;
$$;

-- Test 1: Einspielen ändert nichts; je Kind Klassen −1/Haupt/+1; Zahlen = Gegenrechnung (Ring); offen = gesamt − fertig/gelandet; Konto/Übersicht gleich
do $$
declare v_l record; v jsonb; v_k jsonb; t0 timestamptz; v_ms int := 0;
begin
  if pg_temp.sj_h() is distinct from (select h from sj_rt_vorher) then raise exception 'FEHLER 1: Einspielen hat Daten verändert'; end if;
  for v_l in select id, klasse, coalesce(schulart, 'gym_by') sa from schule.lernender where aktiv order by id loop
    t0 := clock_timestamp(); v := schule.schuljahr_stand(v_l.id); v_ms := greatest(v_ms, (extract(epoch from clock_timestamp() - t0) * 1000)::int);
    if pg_temp.sj_kurz(v) is distinct from pg_temp.sj_ring(v_l.id) then
      raise exception 'FEHLER 1: Kind % weicht von der Ring-Rechnung ab: % gegen %', v_l.id, pg_temp.sj_kurz(v), pg_temp.sj_ring(v_l.id); end if;
    if exists (select 1 from jsonb_array_elements(v->'klassen') k where (k->>'klasse')::int not between v_l.klasse - 1 and v_l.klasse + 1
                  or (k->>'haupt')::boolean <> ((k->>'klasse')::int = v_l.klasse)
                  or (k->'fluege'->>'offen')::int <> (k->'fluege'->>'gesamt')::int - (k->'fluege'->>'fertig')::int
                  or (k->'etappen'->>'offen')::int <> (k->'etappen'->>'gesamt')::int - (k->'etappen'->>'gelandet')::int
                  or (k->'ring'->>'an')::int < 0) then raise exception 'FEHLER 1: Kind % Klassen/Haupt/offen falsch: %', v_l.id, v; end if;
    if pg_temp.sj_konto('', jsonb_build_object('lernender_id', v_l.id))->'schuljahr_stand' is distinct from v then raise exception 'FEHLER 1: schule_konto Kind % weicht ab', v_l.id; end if;
    select k into v_k from jsonb_array_elements(pg_temp.sj_uebersicht('', null)->'lernende') k where (k->>'id')::bigint = v_l.id;
    if v_k->'schuljahr_stand' is distinct from v then raise exception 'FEHLER 1: schule_uebersicht Kind % weicht ab', v_l.id; end if;
    raise notice 'Test 1: Kind % (Kl. %): %', v_l.id, v_l.klasse,
      (select string_agg(format('Kl. %s%s: Flüge %s/%s fertig, Etappen %s/%s gelandet, %s %%, Zusatz %s Flüge',
              k->>'klasse', case when (k->>'haupt')::boolean then '*' else '' end, k->'fluege'->>'fertig', k->'fluege'->>'gesamt',
              k->'etappen'->>'gelandet', k->'etappen'->>'gesamt', coalesce(k->>'prozent', '–'), k->'zusatz'->'fluege'->>'gesamt'), ' · ' order by (k->>'klasse')::int)
         from jsonb_array_elements(v->'klassen') k);
  end loop;
  raise notice 'Test 1: alle Kinder = Ring-Rechnung, offen stimmt, Konto/Übersicht gleich, Dauer je Kind höchstens % ms: OK', v_ms;
end $$;

-- Test 2: Zusatz getrennt – kein Pflicht-Flug ist Zusatz der Gruppe; Zusatz-Zahlen = übrige Themen der Klasse
do $$
declare v_l record; v_n int;
begin
  for v_l in select id from schule.lernender where aktiv loop
    if exists (select 1 from schule.schuljahr_fluege(v_l.id) x join schule.thema t on t.id = x.thema_id
                where x.pflicht and schule.kind_gruppe(v_l.id) = any(coalesce(t.zusatz, '{}'))) then raise exception 'FEHLER 2: Zusatz als Pflicht gezählt (Kind %)', v_l.id; end if;
    select count(*) into v_n from jsonb_array_elements(schule.schuljahr_stand(v_l.id)->'klassen') k
     where (k->'zusatz'->'fluege'->>'gesamt')::int <> (select count(*) from schule.schuljahr_fluege(v_l.id) x where x.klasse = (k->>'klasse')::int and not x.pflicht);
    if v_n > 0 then raise exception 'FEHLER 2: Zusatz-Zahlen falsch (Kind %)', v_l.id; end if;
  end loop;
  raise notice 'Test 2: Zusatz nicht in Pflicht, getrennt ausgewiesen: OK';
end $$;

-- Test 4 (SJ-S 2, vorbereitet): Pflicht-Etappen der Gruppe = thema_stufe.etappen/gelandet der Pflicht-Flüge (fertig: alle); Kür = Rest der Etappen
do $$
declare v_l record; v_k jsonb; v_e record;
begin
  for v_l in select id from schule.lernender where aktiv order by id loop
    for v_k in select k from jsonb_array_elements(schule.schuljahr_stand(v_l.id)->'klassen') k loop
      select coalesce(sum((s->>'etappen')::int), 0) e, coalesce(sum(case when s->>'stufe' in ('komplett', 'wiederholung') then (s->>'etappen')::int else (s->>'gelandet')::int end), 0) g
        into v_e from schule.schuljahr_fluege(v_l.id) x cross join lateral (select schule.thema_stufe(v_l.id, x.thema_id) s) st
       where x.pflicht and x.klasse = (v_k->>'klasse')::int;
      if (v_k->'etappen_pflicht'->>'gesamt')::int <> v_e.e or (v_k->'etappen_pflicht'->>'gelandet')::int <> v_e.g
         or (v_k->'etappen_pflicht'->>'offen')::int <> v_e.e - v_e.g
         or (v_k->'etappen_pflicht'->>'gesamt')::int + (v_k->'kuer'->>'gesamt')::int <> (v_k->'etappen'->>'gesamt')::int
         or (v_k->'kuer'->>'offen')::int <> (v_k->'kuer'->>'gesamt')::int - (v_k->'kuer'->>'gelandet')::int
         or (v_k->'kuer'->>'gelandet')::int < 0 or (v_k->'kuer'->>'offen')::int < 0
         or (v_k->>'prozent_pflicht')::int is distinct from (case when v_e.e > 0 then round(100.0 * v_e.g / v_e.e)::int end) then
        raise exception 'FEHLER 4: Kind % Kl. % Pflicht/Kür falsch: % / % gegen thema_stufe %/%', v_l.id, v_k->>'klasse', v_k->'etappen_pflicht', v_k->'kuer', v_e.e, v_e.g; end if;
    end loop;
    raise notice 'Test 4: Kind %: %', v_l.id, (select string_agg(format('Kl. %s: Pflicht-Etappen %s/%s (%s %%), Kür %s/%s', k->>'klasse',
        k->'etappen_pflicht'->>'gelandet', k->'etappen_pflicht'->>'gesamt', coalesce(k->>'prozent_pflicht', '–'), k->'kuer'->>'gelandet', k->'kuer'->>'gesamt'), ' · ' order by (k->>'klasse')::int)
      from jsonb_array_elements(schule.schuljahr_stand(v_l.id)->'klassen') k);
  end loop;
  raise notice 'Test 4: etappen_pflicht = thema_stufe, Pflicht + Kür = alle Etappen: OK';
end $$;

-- Test 3 (Testkind): „kann er komplett“ zählt mit allen Etappen; eingeplanter Zusatz ändert Pflicht-Zahlen nicht
create temp table sj_t on commit drop as
  select l.id l, l.klasse kl,
    (select x.thema_id from schule.schuljahr_fluege(l.id) x join schule.block_thema bt on bt.thema_id = x.thema_id
      where x.pflicht and x.klasse = l.klasse and not x.fertig and not exists (select 1 from schule.route r where r.lernender_id = l.id and r.block_id = bt.block_id)
      order by x.etappen desc, x.thema_id limit 1) pfl,
    (select x.thema_id from schule.schuljahr_fluege(l.id) x join schule.block_thema bt on bt.thema_id = x.thema_id
      where not x.pflicht and not exists (select 1 from schule.route r where r.lernender_id = l.id and r.block_id = bt.block_id)
        and exists (select 1 from schule.thema t where t.id = x.thema_id and schule.kind_gruppe(l.id) = any(coalesce(t.zusatz, '{}')))
      order by x.thema_id limit 1) zus
  from schule.lernender l where l.ist_test and l.aktiv order by l.id limit 1;
do $$
declare t record; v0 jsonb; v1 jsonb; v_n int; v_b bigint;
begin
  select * into t from sj_t;
  if t.l is null or t.pfl is null then raise notice 'Test 3: kein Testkind oder kein offener Pflicht-Flug – übersprungen'; return; end if;
  v0 := (select k from jsonb_array_elements(schule.schuljahr_stand(t.l)->'klassen') k where (k->>'haupt')::boolean);
  select etappen into v_n from schule.schuljahr_fluege(t.l) where thema_id = t.pfl;
  select block_id into v_b from schule.block_thema where thema_id = t.pfl order by block_id limit 1;
  insert into schule.route(lernender_id, block_id, position, art, status, kann_schon, geaendert_von)
    values (t.l, v_b, (select coalesce(max(position), 0) + 1 from schule.route where lernender_id = t.l), 'normal', 'offen', true, 'eltern:Test');
  v1 := (select k from jsonb_array_elements(schule.schuljahr_stand(t.l)->'klassen') k where (k->>'haupt')::boolean);
  if (v1->'fluege'->>'fertig')::int <> (v0->'fluege'->>'fertig')::int + 1 or (v1->'ring'->>'kann')::int < (v0->'ring'->>'kann')::int + v_n
     or (v1->'etappen'->>'gesamt') <> (v0->'etappen'->>'gesamt') then
    raise exception 'FEHLER 3: „kann er“ nicht mit allen Etappen: vorher %, nachher %', v0->'fluege', v1->'fluege'; end if;
  if pg_temp.sj_kurz(schule.schuljahr_stand(t.l)) is distinct from pg_temp.sj_ring(t.l) then raise exception 'FEHLER 3: Ring-Rechnung weicht ab'; end if;
  if t.zus is not null then
    select block_id into v_b from schule.block_thema where thema_id = t.zus order by block_id limit 1;
    insert into schule.route(lernender_id, block_id, position, art, status, geaendert_von)
      values (t.l, v_b, (select coalesce(max(position), 0) + 1 from schule.route where lernender_id = t.l), 'normal', 'offen', 'eltern:Test');
    if not exists (select 1 from schule.schuljahr_fluege(t.l) x where x.thema_id = t.zus and x.eingeplant and not x.pflicht) then
      raise exception 'FEHLER 3: eingeplanter Zusatz nicht als eingeplant ausgewiesen'; end if;
    if (select sum((k->'zusatz'->'fluege'->>'eingeplant')::int) from jsonb_array_elements(schule.schuljahr_stand(t.l)->'klassen') k) < 1 then
      raise exception 'FEHLER 3: Zusatz eingeplant fehlt im Feld'; end if;
    if (select (k->'fluege'->>'gesamt')::int from jsonb_array_elements(schule.schuljahr_stand(t.l)->'klassen') k where (k->>'haupt')::boolean) <> (v1->'fluege'->>'gesamt')::int then
      raise exception 'FEHLER 3: eingeplanter Zusatz verändert Pflicht-Flüge'; end if;
    raise notice 'Test 3: Zusatz-Teil % eingeplant → nur unter zusatz (eingeplant), Pflicht unverändert: OK', t.zus;
  else
    raise notice 'Test 3: kein Zusatz-Teil für die Gruppe des Testkinds – Teil übersprungen';
  end if;
  raise notice 'Test 3: „kann er komplett“ → +1 fertig, alle % Etappen gelandet; gleich der Ring-Rechnung: OK', v_n;
end $$;

rollback;
