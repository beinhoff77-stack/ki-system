-- TEMPO-S1 Messung (erzeugt von tools/tests/tempo_einspielen.py). Nach dem Einspielen in einer NEUEN Transaktion ausführen. Ändert nichts:
-- legt nur Hilfen in pg_temp an und endet immer mit „MESSUNG (nichts geändert): …“ (Fehler = alles zurück, auch die Hilfen).
select set_config('statement_timeout', '300s', true);

-- Hilfen dieser Sitzung (pg_temp). Das Einspiel-Paket entfernt sie am Ende ausdrücklich (auch bei Erfolg); Probe und Messung rollen zurück.
create or replace function pg_temp.tempo_zugriff(p_schluessel text, p_lernender bigint) returns bigint language sql as $$ select null::bigint $$;
-- Merkheft-Kopie ohne Zugriffsprüfung (nur zum Vergleichen und Messen in dieser Sitzung). Jeder Fehler → Abbruch.
create or replace function pg_temp.tempo_merkheft_anlegen() returns text language plpgsql as $f$
declare d text; kopf constant text := 'CREATE OR REPLACE FUNCTION api.schule_merkheft(';
  ziel constant text := 'CREATE OR REPLACE FUNCTION pg_temp.tempo_merkheft('; v_oid oid;
begin
  if to_regprocedure('api.schule_merkheft(text, jsonb)') is null then raise exception 'TEMPO-S1 ABBRUCH: api.schule_merkheft(text, jsonb) fehlt – Merkheft nicht vergleichbar'; end if;
  d := pg_get_functiondef('api.schule_merkheft(text, jsonb)'::regprocedure);
  if (length(d) - length(replace(d, kopf, ''))) / length(kopf) <> 1 or position(kopf in d) <> 1 then
    raise exception 'TEMPO-S1 ABBRUCH: Kopf von api.schule_merkheft nicht wie erwartet – Merkheft nicht vergleichbar'; end if;
  if position('schule.zugriff(' in d) = 0 then raise exception 'TEMPO-S1 ABBRUCH: keine Stelle schule.zugriff( in api.schule_merkheft – Merkheft nicht vergleichbar'; end if;
  d := replace(replace(replace(d, kopf, ziel), 'schule.zugriff(', 'pg_temp.tempo_zugriff('), ' SECURITY DEFINER', '');
  -- vor dem Ausführen: der Text legt genau eine Funktion an, und zwar im temporären Schema
  if position(ziel in d) <> 1 or position('FUNCTION api.' in d) > 0 or position('SECURITY DEFINER' in upper(d)) > 0 then
    raise exception 'TEMPO-S1 ABBRUCH: Merkheft-Kopie zielt nicht ins temporäre Schema'; end if;
  execute d;
  v_oid := to_regprocedure('pg_temp.tempo_merkheft(text, jsonb)');
  if v_oid is null or (select p.pronamespace <> pg_my_temp_schema() or p.prosecdef from pg_proc p where p.oid = v_oid) then
    raise exception 'TEMPO-S1 ABBRUCH: Merkheft-Kopie nicht im temporären Schema bzw. nicht als Invoker'; end if;
  return 'ok';
end $f$;
-- Ein Lauf: alle Kinder × alle Einheiten (etappen_stand) und je Kind die Merkheft-Kopie, md5 und Laufzeit. Was dabei geschrieben würde, rollt der
-- Unterblock zurück; die Ergebnisse bleiben in den Variablen. Jeder Fehler (auch bei einem einzelnen Kind) → Abbruch des ganzen Pakets.
create or replace function pg_temp.tempo_lauf(p_name text) returns jsonb language plpgsql as $f$
declare h jsonb; mh jsonb := '{}'; t0 timestamptz; t1 timestamptz; ms_es numeric; ms_mh numeric := 0; je jsonb := '{}'; r record; ms numeric; kinder jsonb; status text;
begin
  begin
    perform setseed(0.5);
    select coalesce(jsonb_agg(l.id order by l.id), '[]') into kinder from schule.lernender l;
    t0 := clock_timestamp();
    select coalesce(jsonb_object_agg(l.id::text || '/' || e.id::text, md5(coalesce(schule.etappen_stand(l.id, e.id)::text, 'NULL'))), '{}') into h
      from schule.lernender l cross join schule.einheit e;
    ms_es := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
    for r in select l.id from schule.lernender l order by l.id loop
      perform setseed(0.5);
      t1 := clock_timestamp();
      mh := mh || jsonb_build_object(r.id::text, md5(coalesce(pg_temp.tempo_merkheft(null, jsonb_build_object('lernender_id', r.id))::text, 'NULL')));
      ms := round(extract(epoch from clock_timestamp() - t1) * 1000, 1); ms_mh := ms_mh + ms;
      je := je || jsonb_build_object(r.id::text, ms);
    end loop;
    status := 'verglichen';
    raise exception using errcode = 'TP999', message = 'zurueck';
  exception when sqlstate 'TP999' then null;
    when others then raise exception 'TEMPO-S1 ABBRUCH, alles zurückgerollt: Lauf „%“ fehlgeschlagen (Merkheft/etappen_stand nicht für alle verglichen): %', p_name, sqlerrm;
  end;
  return jsonb_build_object('lauf', p_name, 'merkheft', status, 'kinder', kinder, 'paare', (select count(*) from jsonb_object_keys(h)), 'h', h, 'mh', mh,
    'ms_etappen_stand_alle', ms_es, 'ms_merkheft_summe', ms_mh, 'ms_merkheft_je_kind', je);
end $f$;
-- Vergleich zweier Läufe: beide „verglichen“, gleiche vollständige Kinder- und Paarmengen, keine Abweichung – sonst Abbruch
create or replace function pg_temp.tempo_gleich(a jsonb, b jsonb) returns jsonb language plpgsql as $f$
declare abw jsonb; abw_mh jsonb; n_kinder int := jsonb_array_length(a->'kinder');
begin
  if a->>'merkheft' is distinct from 'verglichen' or b->>'merkheft' is distinct from 'verglichen' then
    raise exception 'TEMPO-S1 ABBRUCH: Merkheft nicht verglichen (%: %, %: %)', a->>'lauf', a->>'merkheft', b->>'lauf', b->>'merkheft'; end if;
  if n_kinder = 0 or a->'kinder' is distinct from b->'kinder' then raise exception 'TEMPO-S1 ABBRUCH: Kindermengen leer oder verschieden (% / %)', a->'kinder', b->'kinder'; end if;
  if (select count(*) from jsonb_object_keys(a->'mh')) <> n_kinder or (select count(*) from jsonb_object_keys(b->'mh')) <> n_kinder
     or exists (select 1 from jsonb_array_elements_text(a->'kinder') k where not (a->'mh') ? k or not (b->'mh') ? k) then
    raise exception 'TEMPO-S1 ABBRUCH: Merkheft nicht für jedes Kind verglichen (% / %)', a->'lauf', b->'lauf'; end if;
  if (a->>'paare')::int <> n_kinder * (select count(*) from schule.einheit) or a->'paare' is distinct from b->'paare' then
    raise exception 'TEMPO-S1 ABBRUCH: nicht alle Kind×Einheit-Paare verglichen (% / %)', a->'paare', b->'paare'; end if;
  select coalesce(jsonb_agg(coalesce(x.key, y.key) order by coalesce(x.key, y.key)), '[]') into abw
    from jsonb_each_text(a->'h') x full join jsonb_each_text(b->'h') y on y.key = x.key where x.value is distinct from y.value;
  select coalesce(jsonb_agg(coalesce(x.key, y.key) order by coalesce(x.key, y.key)), '[]') into abw_mh
    from jsonb_each_text(a->'mh') x full join jsonb_each_text(b->'mh') y on y.key = x.key where x.value is distinct from y.value;
  if jsonb_array_length(abw) > 0 or jsonb_array_length(abw_mh) > 0 then
    raise exception 'TEMPO-S1 ABBRUCH, alles zurückgerollt: Ergebnis weicht ab (% gegen %): etappen_stand % Paare (erste: %), Merkheft Kinder %',
      a->>'lauf', b->>'lauf', jsonb_array_length(abw), abw->0, abw_mh; end if;
  return jsonb_build_object('gegen', (a->>'lauf') || ' / ' || (b->>'lauf'), 'merkheft', 'verglichen', 'kinder', a->'kinder', 'paare', (a->>'paare')::int,
    'abweichungen_etappen_stand', 0, 'abweichungen_merkheft', 0);
end $f$;
create or replace function pg_temp.tempo_indizes() returns jsonb language sql as $f$
  select coalesce(jsonb_agg(jsonb_build_object('name', c.relname, 'tabelle', t.relname, 'def', pg_get_indexdef(c.oid), 'gueltig', i.indisvalid and i.indisready,
           'indcheckxmin', i.indcheckxmin) order by t.relname, c.relname), '[]')
    from pg_index i join pg_class c on c.oid = i.indexrelid join pg_class t on t.oid = i.indrelid join pg_namespace n on n.oid = t.relnamespace
   where n.nspname = 'schule' and t.relname in ('aufgabe', 'versuch');
$f$;
create or replace function pg_temp.tempo_funktion() returns jsonb language sql as $f$
  select jsonb_build_object('md5', md5(p.prosrc), 'eigenschaften', concat_ws('|', pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname, p.provolatile,
           p.prosecdef, coalesce(p.proconfig::text, '')))
    from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = 'schule.etappen_stand(bigint, bigint)'::regprocedure;
$f$;
-- Hilfen dieser Sitzung im temporären Schema? (vor dem ersten Aufruf geprüft; am Ende: keine mehr)
create or replace function pg_temp.tempo_hilfen() returns jsonb language sql as $f$
  select coalesce(jsonb_agg(p.proname::text order by p.proname), '[]') from pg_proc p where p.pronamespace = pg_my_temp_schema() and p.proname like 'tempo\_%';
$f$;
do $h$ begin
  if (select count(*) from pg_proc p where p.pronamespace = pg_my_temp_schema() and p.proname in
      ('tempo_zugriff', 'tempo_merkheft_anlegen', 'tempo_lauf', 'tempo_gleich', 'tempo_indizes', 'tempo_funktion', 'tempo_hilfen')) <> 7
  then raise exception 'TEMPO-S1 ABBRUCH: Hilfen nicht im temporären Schema'; end if;
end $h$;

do $p$
declare x jsonb;
begin
  perform pg_temp.tempo_merkheft_anlegen();
  x := pg_temp.tempo_lauf('messung');
  raise exception 'MESSUNG (nichts geändert): %', jsonb_build_object('funktion', pg_temp.tempo_funktion(),
    'merkheft', x->>'merkheft', 'kinder', x->'kinder', 'ms_etappen_stand_alle', x->'ms_etappen_stand_alle', 'ms_merkheft_summe', x->'ms_merkheft_summe',
    'ms_merkheft_je_kind', x->'ms_merkheft_je_kind', 'indizes', pg_temp.tempo_indizes())::text;
end $p$;
