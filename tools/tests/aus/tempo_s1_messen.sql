-- TEMPO-S1 Messung (erzeugt von tools/tests/tempo_einspielen.py). Nach dem Einspielen in einer NEUEN Transaktion ausführen. Ändert nichts:
-- legt nur Hilfen in pg_temp an und endet immer mit „MESSUNG (nichts geändert): …“ (Fehler = alles zurück).
select set_config('statement_timeout', '300s', true);

-- Hilfen dieser Sitzung (pg_temp, verschwinden mit dem Ende der Transaktion)
create or replace function pg_temp.tempo_zugriff(p_schluessel text, p_lernender bigint) returns bigint language sql as $$ select null::bigint $$;
-- Merkheft-Kopie ohne Zugriffsprüfung (nur zum Vergleichen und Messen); fehlt die Stelle, bleibt der Merkheft-Vergleich aus (wird gemeldet)
create or replace function pg_temp.tempo_merkheft_anlegen() returns text language plpgsql as $f$
declare d text;
begin
  if to_regprocedure('api.schule_merkheft(text, jsonb)') is null then return 'api.schule_merkheft fehlt'; end if;
  d := pg_get_functiondef('api.schule_merkheft(text, jsonb)'::regprocedure);
  if position('schule.zugriff(' in d) = 0 then return 'keine Stelle schule.zugriff( in api.schule_merkheft'; end if;
  d := replace(d, 'CREATE OR REPLACE FUNCTION api.schule_merkheft(', 'CREATE OR REPLACE FUNCTION pg_temp.tempo_merkheft(');
  d := replace(d, 'schule.zugriff(', 'pg_temp.tempo_zugriff(');
  d := replace(d, ' SECURITY DEFINER', '');
  execute d;
  return 'ok';
exception when others then return 'Kopie nicht angelegt: ' || sqlerrm;
end $f$;
-- Ein Lauf: alle Kinder × alle Einheiten (etappen_stand) und je Kind die Merkheft-Kopie; md5 und Laufzeit. Was die Funktionen dabei schreiben
-- (keine bekannt), wird am Ende des Laufs zurückgerollt; die Ergebnisse bleiben in den Variablen.
create or replace function pg_temp.tempo_lauf(p_merk text) returns jsonb language plpgsql as $f$
declare h jsonb; mh jsonb := '{}'; t0 timestamptz; t1 timestamptz; ms_es numeric; ms_mh numeric; je jsonb := '{}'; status text := p_merk; r record; ms numeric;
begin
  begin
    perform setseed(0.5);
    t0 := clock_timestamp();
    select coalesce(jsonb_object_agg(l.id::text || '/' || e.id::text, md5(coalesce(schule.etappen_stand(l.id, e.id)::text, 'NULL'))), '{}') into h
      from schule.lernender l cross join schule.einheit e;
    ms_es := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
    ms_mh := 0;
    if p_merk = 'ok' then
      begin
        for r in select l.id from schule.lernender l order by l.id loop
          perform setseed(0.5);
          t1 := clock_timestamp();
          mh := mh || jsonb_build_object(r.id::text, md5(coalesce(pg_temp.tempo_merkheft(null, jsonb_build_object('lernender_id', r.id))::text, 'NULL')));
          ms := round(extract(epoch from clock_timestamp() - t1) * 1000, 1); ms_mh := ms_mh + ms;
          je := je || jsonb_build_object(r.id::text, ms);
        end loop;
        status := 'verglichen';
      exception when others then status := 'nicht verglichen: ' || sqlerrm; mh := null; je := null;
      end;
    end if;
    raise exception using errcode = 'TP999', message = 'zurueck';
  exception when sqlstate 'TP999' then null;
  end;
  return jsonb_build_object('h', h, 'mh', mh, 'ms_etappen_stand_alle', ms_es, 'ms_merkheft_summe', ms_mh, 'ms_merkheft_je_kind', je, 'merkheft', status);
end $f$;
create or replace function pg_temp.tempo_indizes() returns jsonb language sql as $f$
  select coalesce(jsonb_agg(jsonb_build_object('name', c.relname, 'tabelle', t.relname, 'def', pg_get_indexdef(c.oid), 'indcheckxmin', i.indcheckxmin) order by t.relname, c.relname), '[]')
    from pg_index i join pg_class c on c.oid = i.indexrelid join pg_class t on t.oid = i.indrelid join pg_namespace n on n.oid = t.relnamespace
   where n.nspname = 'schule' and t.relname in ('aufgabe', 'versuch');
$f$;

do $p$
declare m text := pg_temp.tempo_merkheft_anlegen(); x jsonb;
begin
  x := pg_temp.tempo_lauf(m);
  raise exception 'MESSUNG (nichts geändert): %', jsonb_build_object('umgestellt', position('TEMPO-S1' in (select p.prosrc from pg_proc p where p.oid = 'schule.etappen_stand(bigint, bigint)'::regprocedure)) > 0,
    'merkheft', x->>'merkheft', 'ms_etappen_stand_alle', x->'ms_etappen_stand_alle', 'ms_merkheft_summe', x->'ms_merkheft_summe', 'ms_merkheft_je_kind', x->'ms_merkheft_je_kind',
    'indizes', pg_temp.tempo_indizes())::text;
end $p$;
