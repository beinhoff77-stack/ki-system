-- Rauchtest LZ-S (Ladezeit): Antworten vor und nach der Migration 20261126_lz_s_ladezeit.sql inhaltlich gleich (md5), dazu Laufzeiten vorher/nachher.
-- Je echtem Kind und für das Testkind in allen fünf Gruppen: Matrix (Kindsicht), Lernstand, Plan, Reisekarte, thema_stufe aller Themen;
-- dazu Matrix ohne Kind (ohne und mit Testkind) und Übersicht (Leitung). Alles in einer Transaktion mit Rollback; Gruppenwechsel je in einer Untertransaktion.
-- Die api-Funktionen werden ohne Schlüssel als pg_temp-Kopien aufgerufen (Zugriffsprüfung durch feste Werte ersetzt; der übrige Text bleibt wörtlich).
-- Aufruf aus dem Repo-Wurzelverzeichnis: psql -v ON_ERROR_STOP=1 -f supabase/tests/lz_s_rauchtest.sql. Ausgabe nur Zahlen.
begin;

create temp table lz_rt (phase text, zustand text, was text, h text, ms numeric) on commit drop;

create function pg_temp.lz_ersetzen(d text, a text, n text) returns text language plpgsql as $$
begin
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'LZ-Test: Anker nicht genau einmal: %', left(a, 60); end if;
  return replace(d, a, n);
end $$;

do $$
declare d text;
begin
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  d := pg_temp.lz_ersetzen(d, 'FUNCTION api.schule_uebersicht(', 'FUNCTION pg_temp.lz_uebersicht(');
  d := pg_temp.lz_ersetzen(d, 'v_tn := schule.wer_tn(p_schluessel);', 'v_tn := null;');
  d := pg_temp.lz_ersetzen(d, 'v_leiter := schule.ist_leiter(p_schluessel);', 'v_leiter := true;');
  d := pg_temp.lz_ersetzen(d, 'schule.sieht(p_schluessel, l.id)', 'true');
  execute d;
  d := pg_get_functiondef('api.schule_lernstand(text, jsonb)'::regprocedure);
  d := pg_temp.lz_ersetzen(d, 'FUNCTION api.schule_lernstand(', 'FUNCTION pg_temp.lz_lernstand(');
  d := pg_temp.lz_ersetzen(d, 'perform schule.wer_tn(p_schluessel);', '');
  d := pg_temp.lz_ersetzen(d, 'if not schule.ist_leiter(p_schluessel) then', 'if false then');
  execute d;
  d := pg_get_functiondef('api.schule_plan_lesen(text, jsonb)'::regprocedure);
  d := pg_temp.lz_ersetzen(d, 'FUNCTION api.schule_plan_lesen(', 'FUNCTION pg_temp.lz_plan(');
  d := pg_temp.lz_ersetzen(d, 'perform schule.wer_tn(p_schluessel);', '');
  d := pg_temp.lz_ersetzen(d, 'if not schule.ist_leiter(p_schluessel) then', 'if false then');
  execute d;
end $$;

-- Antworten je Kind als [{was, h, ms}]
create function pg_temp.lz_kind(p_l bigint) returns jsonb language plpgsql as $$
declare v_t timestamptz; v_r jsonb := '[]'; v_x text;
begin
  v_t := clock_timestamp(); v_x := md5(schule.lehrplan_matrix_lk(schule.lehrplan_matrix(array[p_l], true), p_l)::text);
  v_r := v_r || jsonb_build_object('was', 'matrix_kind', 'h', v_x, 'ms', extract(epoch from clock_timestamp() - v_t) * 1000);
  v_t := clock_timestamp(); v_x := md5(pg_temp.lz_lernstand('', jsonb_build_object('lernender_id', p_l))::text);
  v_r := v_r || jsonb_build_object('was', 'lernstand', 'h', v_x, 'ms', extract(epoch from clock_timestamp() - v_t) * 1000);
  v_t := clock_timestamp(); v_x := md5(pg_temp.lz_plan('', jsonb_build_object('lernender_id', p_l))::text);
  v_r := v_r || jsonb_build_object('was', 'plan', 'h', v_x, 'ms', extract(epoch from clock_timestamp() - v_t) * 1000);
  v_t := clock_timestamp(); v_x := md5(schule.reise_karte(p_l)::text);
  v_r := v_r || jsonb_build_object('was', 'reise_karte', 'h', v_x, 'ms', extract(epoch from clock_timestamp() - v_t) * 1000);
  v_t := clock_timestamp(); v_x := md5((select string_agg(t.id || ':' || schule.thema_stufe(p_l, t.id)::text, '|' order by t.id) from schule.thema t));
  v_r := v_r || jsonb_build_object('was', 'thema_stufe_alle', 'h', v_x, 'ms', extract(epoch from clock_timestamp() - v_t) * 1000);
  return v_r;
end $$;

create function pg_temp.lz_messen(p_phase text) returns void language plpgsql as $$
declare v_t timestamptz; v_x text; v_k record; v_g record; v_tk bigint; v_r jsonb; v_alle bigint[]; v_echt bigint[];
begin
  select array_agg(id order by id) filter (where not ist_test), array_agg(id order by id) into v_echt, v_alle from schule.lernender where aktiv;
  v_t := clock_timestamp(); v_x := md5(schule.lehrplan_matrix_lk(schule.lehrplan_matrix(coalesce(v_echt, '{}'), false), null)::text);
  insert into lz_rt values (p_phase, 'leitung', 'matrix_ohne_kind', v_x, extract(epoch from clock_timestamp() - v_t) * 1000);
  v_t := clock_timestamp(); v_x := md5(schule.lehrplan_matrix_lk(schule.lehrplan_matrix(coalesce(v_alle, '{}'), false), null)::text);
  insert into lz_rt values (p_phase, 'leitung', 'matrix_mit_testkind', v_x, extract(epoch from clock_timestamp() - v_t) * 1000);
  v_t := clock_timestamp(); v_x := md5(pg_temp.lz_uebersicht('', null)::text);
  insert into lz_rt values (p_phase, 'leitung', 'uebersicht', v_x, extract(epoch from clock_timestamp() - v_t) * 1000);
  for v_k in select id from schule.lernender where aktiv and not ist_test order by id loop
    insert into lz_rt select p_phase, 'kind ' || v_k.id, x->>'was', x->>'h', (x->>'ms')::numeric from jsonb_array_elements(pg_temp.lz_kind(v_k.id)) x;
  end loop;
  select id into v_tk from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_tk is null then return; end if;
  for v_g in select * from (values ('gym_by', null::text, 'gym_by'), ('rs_by', 'rs_I', 'rs_I'), ('rs_by', 'rs_II_III', 'rs_II_III'),
                                   ('ib_myp', 'myp_standard', 'myp_standard'), ('ib_myp', 'myp_extended', 'myp_extended')) g(sa, zw, gruppe) loop
    begin   -- Untertransaktion: Gruppenwechsel (und was er synchronisiert) wird danach zurückgenommen
      update schule.lernender set schulart = v_g.sa, zweig = v_g.zw where id = v_tk;
      if schule.kind_gruppe(v_tk) <> v_g.gruppe then raise exception 'LZ-Test: Gruppe % nicht einstellbar', v_g.gruppe; end if;
      v_r := pg_temp.lz_kind(v_tk) || jsonb_build_array(jsonb_build_object('was', 'uebersicht', 'h', md5(pg_temp.lz_uebersicht('', null)::text), 'ms', 0));
      raise exception using errcode = 'LZ001';
    exception when sqlstate 'LZ001' then null;
    end;
    insert into lz_rt select p_phase, 'testkind ' || v_g.gruppe, x->>'was', x->>'h', (x->>'ms')::numeric from jsonb_array_elements(v_r) x;
  end loop;
end $$;

select pg_temp.lz_messen('vorher');
\ir ../migrations/20261126_lz_s_ladezeit.sql
\ir ../migrations/20261126_lz_s_ladezeit.sql
select pg_temp.lz_messen('nachher');

do $$
declare v_n int; v_x record; v_d text;
begin
  select count(*) into v_n from lz_rt;
  if v_n = 0 or (select count(*) from lz_rt where phase = 'vorher') <> (select count(*) from lz_rt where phase = 'nachher') then raise exception 'LZ-Test: Messung unvollständig'; end if;
  select string_agg(a.zustand || '/' || a.was, ', ') into v_d from lz_rt a join lz_rt b on b.zustand = a.zustand and b.was = a.was and b.phase = 'nachher'
   where a.phase = 'vorher' and a.h is distinct from b.h;
  if v_d is not null then raise exception 'LZ-Test: Antwort verändert: %', v_d; end if;
  raise notice 'LZ-Test ok: % Antworten vorher = nachher (md5)', v_n / 2;
  for v_x in select a.zustand, a.was, round(a.ms) vor, round(b.ms) nach from lz_rt a join lz_rt b on b.zustand = a.zustand and b.was = a.was and b.phase = 'nachher'
              where a.phase = 'vorher' and not (a.zustand like 'testkind%' and a.was = 'uebersicht')
              order by a.zustand, a.was loop
    raise notice 'Laufzeit % / %: % ms → % ms', v_x.zustand, v_x.was, v_x.vor, v_x.nach;
  end loop;
end $$;

rollback;
