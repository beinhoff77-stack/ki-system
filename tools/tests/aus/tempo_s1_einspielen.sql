-- TEMPO-S1 Einspiel-Paket (erzeugt von tools/tests/tempo_einspielen.py). Ein Aufruf, EINE Transaktion; Fehler = alles zurück.
-- Ausführung: inhalte/plan/ladezeiten.md, Abschnitt „Einspielen TEMPO-S1“ (statement_timeout und lock_timeout als eigene Anweisungen VOR dem äußeren do).
-- Ablauf: Hilfen → Lauf „alt“ → Funktion ersetzen (Teil 1) → Lauf „neu“ (ohne Sperre an Tabellen) → Indizes (Teil 2, ab hier SHARE auf aufgabe/versuch)
--         → Lauf „endzustand“ (nur Gleichheitsbeweis) → Aufräumen, Bericht.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '300s', true);
do $p$ begin
  if to_regprocedure('schule.etappen_stand(bigint, bigint)') is null or to_regclass('schule.aufgabe') is null or to_regclass('schule.versuch') is null
     or to_regclass('schule.lernender') is null or to_regclass('schule.einheit') is null then
    raise exception 'TEMPO-S1 ABBRUCH, Vorbedingung: schule.etappen_stand / aufgabe / versuch / lernender / einheit fehlt – nichts geändert';
  end if;
end $p$;
create temp table tempo_mig on commit drop as select $tempoteil$-- TEMPO-S1 (Bau-Auftrag Ladezeiten, ENTWURF – nicht eingespielt): schule_merkheft schneller, Ergebnis byte-gleich.
-- Analyse: inhalte/plan/ladezeiten.md. Einspielen NUR über das Paket tools/tests/aus/tempo_s1_einspielen.sql (eine Transaktion, prüft sich selbst:
-- vergleicht vorher/nachher je Kind und Einheit per md5 und bricht bei jeder Abweichung ab); Probe: tools/tests/aus/tempo_s1_probe.sql (rollt alles zurück).
--
-- Befund (live gemessen vom Projektleiter): api.schule_merkheft ruft je Einheit schule.etappen_stand auf, 95 Einheiten ≈ 3,7 s (≈ 39 ms je Einheit).
-- etappen_stand rechnet je Etappe (Lernziel) bis zu zehn Unterabfragen über schule.aufgabe und schule.versuch:
--   gesamt, geloest, karte_ziel (zweimal: ziel und folge_ziel), karte_typen_noetig, karte_schwer_noetig, karte_anwenden_pflicht → karte_anwenden_noetig,
--   karte_bearbeitungen, karte_sicher, dazu flug_nachtest(Kind, Einheit) – das ist je Einheit gleich, wurde aber je Etappe neu gerechnet.
--   Im Repo gibt es keinen Index auf schule.aufgabe(einheit_id …) und keinen auf schule.versuch(lernender_id, aufgabe_id) (live bekannt sind nur die
--   eindeutigen Indizes, supabase/tests/nachbau_live_constraints.sql). Ohne sie ist jede dieser Unterabfragen ein Lauf über die ganze Tabelle.
--
-- WAS:
--  1. Index schule.aufgabe (einheit_id, pool, variante_gruppe) – für alle Etappen-Hilfen (alle filtern einheit_id, pool, variante_gruppe).
--  2. Index schule.versuch (lernender_id, aufgabe_id) – für geloest und karte_bearbeitungen (Versuche eines Kindes zu Aufgaben einer Einheit).
--  3. schule.etappen_stand neu (create or replace), gleiches Ergebnis:
--     - flug_nachtest(Kind, Einheit) einmal je Aufruf statt je Etappe (Unterabfrage mit offset 0, damit der Planer sie nicht je Zeile einsetzt),
--     - karte_ziel einmal je Etappe (für ziel und folge_ziel),
--     - gesamt und geloest je Einheit in EINER gruppierten Abfrage statt je Etappe,
--     - alle übrigen Hilfsfunktionen unverändert dieselben (Regeln bleiben an einer Stelle).
--     Zulässig sind genau zwei Zustände des Funktionstexts: exakt alt (md5 bf3152e9…, nachgerechnet aus den Migrationen 20261114 … 20261203) → ersetzen;
--     exakt neu (md5 3f49198f…) → nichts tun. Alles andere (auch eine alte Fassung mit dem Wort TEMPO-S1) → Abbruch. Danach muss der neue md5 stehen;
--     Signatur, Rückgabe (skalar jsonb, keine Menge), Sprache, STABLE, SECURITY INVOKER, nicht STRICT (NULL-Verhalten) und search_path werden vor und nach
--     dem Ersetzen geprüft (1181: create or replace setzt STRICT zurück – eine STRICT-Altfassung wird deshalb abgelehnt, nicht still umgestellt).
--  4. Nach dem Anlegen der Indizes: unter beiden Namen genau die beabsichtigte Definition (pg_get_indexdef exakt; Kollation und Operatorklasse wie die
--     Spalte bzw. Standard, Sortieroptionen ASC, keine Bedingung/Ausdrücke/Optionen, Standard-Tablespace) und alle Kennzeichen aus pg_index/pg_class
--     (gültig, bereit, lebendig, nicht eindeutig, …) – sonst Abbruch (create index if not exists nimmt einen gleichnamigen anderen Index sonst hin).
-- WAS NICHT: keine Tabelle, keine Spalte, kein Trigger, keine andere Funktion; kein DROP, kein DELETE, kein UPDATE; api.schule_merkheft bleibt, wie sie ist
--   (Antwort unverändert; Vorschlag für eine schlankere Antwort nur in der Analyse). Wiederholbar: ein zweiter Lauf ändert nichts.
-- Sperren: create index hält SHARE auf schule.aufgabe und schule.versuch bis zum Ende der Transaktion (Lesen geht, Schreiben wartet). Das Paket legt die
--   Indizes deshalb erst NACH dem Vergleich mit der neuen Funktion an und vergleicht danach nur noch einmal (Beweis im Endzustand); gemessen wird getrennt
--   (tools/tests/aus/tempo_s1_messen.sql, neue Transaktion, rollt zurück). Ausführungsvorschrift: inhalte/plan/ladezeiten.md, Abschnitt „Einspielen“.

select set_config('lock_timeout', '3s', true);

-- ==== TEMPO-S1 Teil 1: Funktion ====
-- 1. etappen_stand: genau zwei zulässige Zustände des Funktionstexts (prosrc): alt → ersetzen, neu → nichts tun; alles andere → Abbruch.
--    Signatur, Rückgabetyp, Sprache, STABLE, SECURITY INVOKER und search_path müssen vorher und nachher gleich (und wie erwartet) sein.
do $tempo$
declare v_f constant regprocedure := to_regprocedure('schule.etappen_stand(bigint, bigint)');
  v_alt constant text := 'bf3152e9a378a1d4e41c98965acf738e';   -- md5 des Funktionstexts nach 20261203_ft_s_form_takt.sql (tools/tests/tempo_einspielen.py)
  v_neu constant text := '3f49198f8dbf5c822a0be4650a5ebce5';   -- md5 des Funktionstexts unten (TEMPO-S1)
  -- Alle Spalten von pg_proc, die das Verhalten bestimmen, gegen ein festes Soll (1190): prokind | Sprache | procost | prorows | provariadic | prosupport |
  -- SECURITY DEFINER | LEAKPROOF | STRICT | Menge | Volatilität | PARALLEL | Zahl Argumente | Zahl Vorgaben | Rückgabe | Argumente | Argumenttypen |
  -- proallargtypes | proargmodes | proargnames | proargdefaults | protrftypes | probin | prosqlbody | proconfig.
  -- Name/Schema über die Signatur; prosrc über die md5; Besitzer, Rechte (proacl) und Kommentar: vorher = nachher (create or replace behält sie).
  v_art_soll constant text := 'f|sql|100|0|0|0|f|f|f|f|s|u|2|0|jsonb|p_lernender bigint, p_einheit bigint|bigint,bigint|-|-|{p_lernender,p_einheit}|-|-|-|-|{"search_path=\"\""}';
  d text; v_art_vor text; v_art_nach text; v_bes_vor text; v_bes_nach text;
begin
  if v_f is null then raise exception 'TEMPO-S1 ABBRUCH: schule.etappen_stand(bigint, bigint) fehlt – nichts geändert'; end if;
  select p.prosrc, concat_ws('|', p.prokind, l.lanname, p.procost, p.prorows, p.provariadic, p.prosupport::oid, p.prosecdef, p.proleakproof, p.proisstrict, p.proretset, p.provolatile, p.proparallel, p.pronargs, p.pronargdefaults, pg_get_function_result(p.oid), pg_get_function_arguments(p.oid), array_to_string(p.proargtypes::oid[]::regtype[], ','), coalesce(p.proallargtypes::text, '-'), coalesce(p.proargmodes::text, '-'), coalesce(p.proargnames::text, '-'), coalesce(p.proargdefaults::text, '-'), coalesce(p.protrftypes::text, '-'), coalesce(p.probin, '-'), coalesce(p.prosqlbody::text, '-'), coalesce(p.proconfig::text, '-'))
         , concat_ws('|', p.proowner::regrole, coalesce(p.proacl::text, '-'), coalesce(obj_description(p.oid, 'pg_proc'), '-'))
    into d, v_art_vor, v_bes_vor from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = v_f;
  if v_art_vor is distinct from v_art_soll then
    raise exception 'TEMPO-S1 ABBRUCH, Vorbedingung: Eigenschaften von etappen_stand anders als erwartet (%, erwartet %) – nichts geändert', v_art_vor, v_art_soll;
  end if;
  if md5(d) = v_neu then raise notice 'TEMPO-S1: etappen_stand schon umgestellt (md5 %)', v_neu; return; end if;
  if md5(d) <> v_alt then
    raise exception 'TEMPO-S1 ABBRUCH, Vorbedingung: etappen_stand weicht vom Repo-Stand ab (md5 %, erwartet % oder %) – nichts geändert', md5(d), v_alt, v_neu;
  end if;
  execute $neu$
create or replace function schule.etappen_stand(p_lernender bigint, p_einheit bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  -- TEMPO-S1: gleiches Ergebnis wie die Fassung nach FT-S; je Einheit einmal: flug_nachtest, gesamt/geloest (gruppiert); je Etappe einmal: karte_ziel
  select coalesce(jsonb_object_agg(z.lz, jsonb_build_object('geloest', z.geloest, 'gesamt', z.gesamt,
           'serie', coalesce(k.serie, 0), 'ziel', z.ziel, 'sitzt', coalesce(k.sitzt, false), 'schwer_ok', coalesce(k.schwer_ok, false), 'anwenden_noetig', schule.karte_anwenden_pflicht(k, p_einheit, z.lz), 'anwenden_ok', coalesce(schule.karte_anwenden_ok(k), false),
           'bearbeitungen', schule.karte_bearbeitungen(p_lernender, p_einheit, z.lz), 'schwer_noetig', schule.karte_schwer_noetig(p_einheit, z.lz),
           'faellig', coalesce(schule.karte_faellig(k), false), 'wdh_stufe', coalesce(k.wdh_stufe, 0),
           'eigene_loesungen', coalesce(k.eigene_loesungen, 0), 'folge', coalesce(k.folge, 0), 'folge_ziel', least(3, z.ziel),
           'typen_anzahl', coalesce(array_length(k.typen, 1), 0), 'typen_noetig', schule.karte_typen_noetig(p_einheit, z.lz),
           'fehler_folge', coalesce(k.fehler_folge, 0), 'stufe_senkung', coalesce(k.stufe_senkung, 0), 'sicher', coalesce(schule.karte_sicher(k), false), 'misch_ok', k.misch_ok_am is not null and k.misch_ok_am >= coalesce(k.sitzt_am, k.misch_ok_am), 'flug_nachtest', fn.v,
           'fertig', schule.etappe_fertig(k, s.status), 'test_nachgewiesen', coalesce(s.status in ('nachgewiesen','korrigiert','gesichert'), false), 'wieder_offen', not coalesce(k.sitzt, false) and k.sitzt_am is not null, 'gezaehlt', coalesce((select jsonb_agg(x::bigint) from jsonb_object_keys(k.gezaehlt) x), '[]'::jsonb))), '{}'::jsonb)
  from (select y.lz, coalesce(g.gesamt, 0) gesamt, coalesce(v.geloest, 0) geloest, schule.karte_ziel(p_einheit, y.lz) ziel
          from (select e->>'lernziel' lz, o.nr
                  from schule.einheit x, jsonb_array_elements(coalesce(x.inhalt->'etappen', '[]'::jsonb)) with ordinality o(e, nr) where x.id = p_einheit) y
          left join (select a.variante_gruppe lz, count(*) gesamt from schule.aufgabe a
                      where a.einheit_id = p_einheit and a.pool = 'uebung' and a.freigegeben group by a.variante_gruppe) g on g.lz = y.lz
          left join (select a.variante_gruppe lz, count(distinct v.aufgabe_id) geloest from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                      where v.lernender_id = p_lernender and v.richtig and v.testsitzung_id is null and a.einheit_id = p_einheit and a.pool = 'uebung'
                      group by a.variante_gruppe) v on v.lz = y.lz
         order by y.nr) z
  cross join (select schule.flug_nachtest(p_lernender, p_einheit) v offset 0) fn
  left join schule.lernziel_stand s on s.lernender_id = p_lernender and s.einheit_id = p_einheit and s.lernziel = z.lz
  left join schule.karte_stand k on k.lernender_id = p_lernender and k.einheit_id = p_einheit and k.lernziel = z.lz;
$function$
$neu$;
  select p.prosrc, concat_ws('|', p.prokind, l.lanname, p.procost, p.prorows, p.provariadic, p.prosupport::oid, p.prosecdef, p.proleakproof, p.proisstrict, p.proretset, p.provolatile, p.proparallel, p.pronargs, p.pronargdefaults, pg_get_function_result(p.oid), pg_get_function_arguments(p.oid), array_to_string(p.proargtypes::oid[]::regtype[], ','), coalesce(p.proallargtypes::text, '-'), coalesce(p.proargmodes::text, '-'), coalesce(p.proargnames::text, '-'), coalesce(p.proargdefaults::text, '-'), coalesce(p.protrftypes::text, '-'), coalesce(p.probin, '-'), coalesce(p.prosqlbody::text, '-'), coalesce(p.proconfig::text, '-'))
         , concat_ws('|', p.proowner::regrole, coalesce(p.proacl::text, '-'), coalesce(obj_description(p.oid, 'pg_proc'), '-'))
    into d, v_art_nach, v_bes_nach from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = v_f;
  if md5(d) is distinct from v_neu then raise exception 'TEMPO-S1 ABBRUCH: neuer Funktionstext hat md5 %, erwartet %', md5(d), v_neu; end if;
  if v_art_nach is distinct from v_art_vor then raise exception 'TEMPO-S1 ABBRUCH: Eigenschaften von etappen_stand geändert (% → %)', v_art_vor, v_art_nach; end if;
  if v_bes_nach is distinct from v_bes_vor then raise exception 'TEMPO-S1 ABBRUCH: Besitzer/Rechte/Kommentar von etappen_stand geändert (% → %)', v_bes_vor, v_bes_nach; end if;
end $tempo$;

$tempoteil$::text as teil1, $tempoteil$-- ==== TEMPO-S1 Teil 2: Indizes ====
-- 2. Indizes; danach prüfen, dass unter den Zielnamen genau diese gültigen, bereiten B-Bäume liegen (ein gleichnamiger anderer Index → Abbruch)
create index if not exists aufgabe_einheit_pool_lz_idx on schule.aufgabe (einheit_id, pool, variante_gruppe);
create index if not exists versuch_kind_aufgabe_idx on schule.versuch (lernender_id, aufgabe_id);
do $tempoidx$
-- 1190: jede Eigenschaft gegen ein festes Soll – die vollständige Definition (pg_get_indexdef: Methode, Eindeutigkeit, Spalten, Reihenfolge, Kollation,
-- Operatorklasse, Sortieroptionen, INCLUDE, WITH-Optionen, Bedingung, Ausdrücke) exakt wie beabsichtigt; dazu einzeln aus pg_index/pg_class.
declare r record; v jsonb; soll jsonb; abw text;
begin
  for r in select * from (values
      ('aufgabe_einheit_pool_lz_idx', 'aufgabe', 'CREATE INDEX aufgabe_einheit_pool_lz_idx ON schule.aufgabe USING btree (einheit_id, pool, variante_gruppe)', 3),
      ('versuch_kind_aufgabe_idx', 'versuch', 'CREATE INDEX versuch_kind_aufgabe_idx ON schule.versuch USING btree (lernender_id, aufgabe_id)', 2)) x(name, tabelle, def, n) loop
    select jsonb_build_object('def', pg_get_indexdef(c.oid), 'am', am.amname, 'relkind', c.relkind, 'tabelle', t.relname, 'schema_t', nt.nspname,
             'natts', i.indnatts, 'nkeyatts', i.indnkeyatts, 'unique', i.indisunique, 'nulls_not_distinct', i.indnullsnotdistinct, 'primary', i.indisprimary,
             'exclusion', i.indisexclusion, 'immediate', i.indimmediate, 'clustered', i.indisclustered, 'valid', i.indisvalid, 'ready', i.indisready,
             'live', i.indislive, 'replident', i.indisreplident, 'pred', i.indpred is not null, 'exprs', i.indexprs is not null,
             'option', (select coalesce(bool_and(o = 0), true) from unnest(i.indoption::int2[]) o),
             'opclass_default', (select coalesce(bool_and(oc.opcdefault and oc.opcmethod = c.relam), false) from unnest(i.indclass::oid[]) k join pg_opclass oc on oc.oid = k),
             'kollation', (select coalesce(bool_and(k.coll = a.attcollation), false) from unnest(i.indcollation::oid[], i.indkey::int2[]) k(coll, att) join pg_attribute a on a.attrelid = t.oid and a.attnum = k.att),
             'tablespace_standard', c.reltablespace = 0, 'reloptions', c.reloptions is not null, 'persistence', c.relpersistence, 'partition', c.relispartition)
      into v
      from pg_class c join pg_namespace n on n.oid = c.relnamespace and n.nspname = 'schule' join pg_index i on i.indexrelid = c.oid
      join pg_class t on t.oid = i.indrelid join pg_namespace nt on nt.oid = t.relnamespace join pg_am am on am.oid = c.relam
     where c.relname = r.name;
    soll := jsonb_build_object('def', r.def, 'am', 'btree', 'relkind', 'i', 'tabelle', r.tabelle, 'schema_t', 'schule',
             'natts', r.n, 'nkeyatts', r.n, 'unique', false, 'nulls_not_distinct', false, 'primary', false,
             'exclusion', false, 'immediate', true, 'clustered', false, 'valid', true, 'ready', true,
             'live', true, 'replident', false, 'pred', false, 'exprs', false, 'option', true, 'opclass_default', true, 'kollation', true,
             'tablespace_standard', true, 'reloptions', false, 'persistence', 'p', 'partition', false);
    if v is distinct from soll then
      select string_agg(k || ': ' || coalesce(v->>k, '–') || ' statt ' || (soll->>k), '; ' order by k) into abw from jsonb_object_keys(soll) k where v->k is distinct from soll->k;
      raise exception 'TEMPO-S1 ABBRUCH: Index schule.% ist nicht der erwartete Index (Soll: %), Abweichung: % – nichts geändert', r.name, r.def, coalesce(abw, 'kein Index dieses Namens');
    end if;
  end loop;
end $tempoidx$;
$tempoteil$::text as teil2;

-- Hilfen dieser Sitzung (pg_temp). Das Einspiel-Paket entfernt sie am Ende ausdrücklich (auch bei Erfolg); Probe und Messung rollen zurück.
create or replace function pg_temp.tempo_zugriff(p_schluessel text, p_lernender bigint) returns bigint language sql as $$ select null::bigint $$;
-- Merkheft-Kopie ohne Zugriffsprüfung (nur zum Vergleichen und Messen in dieser Sitzung). Jeder Fehler → Abbruch.
create or replace function pg_temp.tempo_merkheft_anlegen() returns text language plpgsql as $f$
declare d text; kopf constant text := 'CREATE OR REPLACE FUNCTION api.schule_merkheft(';
  ziel constant text := 'CREATE OR REPLACE FUNCTION pg_temp.tempo_merkheft('; v_oid oid;
begin
  if to_regprocedure('api.schule_merkheft(text, jsonb)') is null then raise exception 'TEMPO-S1 ABBRUCH: api.schule_merkheft(text, jsonb) fehlt – Merkheft nicht vergleichbar'; end if;
  -- 1181: mit NULL-Schlüssel aufgerufen – eine STRICT-Funktion liefe gar nicht (Ergebnis NULL ohne Körper)
  if (select p.proisstrict or p.proretset from pg_proc p where p.oid = 'api.schule_merkheft(text, jsonb)'::regprocedure) then
    raise exception 'TEMPO-S1 ABBRUCH: api.schule_merkheft ist STRICT bzw. liefert eine Menge – mit NULL-Schlüssel nicht vergleichbar'; end if;
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
  if v_oid is null or (select p.pronamespace <> pg_my_temp_schema() or p.prosecdef or p.proisstrict or p.proretset from pg_proc p where p.oid = v_oid) then
    raise exception 'TEMPO-S1 ABBRUCH: Merkheft-Kopie nicht im temporären Schema, nicht als Invoker oder STRICT'; end if;
  return 'ok';
end $f$;
-- Ein Lauf: alle Kinder × alle Einheiten (etappen_stand) und je Kind die Merkheft-Kopie, md5 und Laufzeit. Was dabei geschrieben würde, rollt der
-- Unterblock zurück; die Ergebnisse bleiben in den Variablen. Jeder Fehler (auch bei einem einzelnen Kind) → Abbruch des ganzen Pakets.
create or replace function pg_temp.tempo_lauf(p_name text) returns jsonb language plpgsql as $f$
declare h jsonb; mh jsonb := '{}'; x jsonb; fertig boolean := false; t0 timestamptz; t1 timestamptz; ms_es numeric; ms_mh numeric := 0; je jsonb := '{}'; r record; ms numeric; kinder jsonb; status text;
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
      x := pg_temp.tempo_merkheft(null, jsonb_build_object('lernender_id', r.id));   -- je Kind EINMAL erfassen, dann Vertrag prüfen (1181)
      if x is null or jsonb_typeof(x) is distinct from 'object' or x->'ok' is distinct from 'true'::jsonb or jsonb_typeof(x->'einheiten') is distinct from 'array' then
        raise exception 'Merkheft-Antwort für Kind % nicht im Vertrag (Objekt, ok = true, einheiten als Array): %', r.id, coalesce(left(x::text, 200), 'SQL-NULL'); end if;
      mh := mh || jsonb_build_object(r.id::text, md5(x::text));
      ms := round(extract(epoch from clock_timestamp() - t1) * 1000, 1); ms_mh := ms_mh + ms;
      je := je || jsonb_build_object(r.id::text, ms);
    end loop;
    status := 'verglichen';
    fertig := true;   -- 1190: nur dieser eigene Abschluss gilt als Rollback-Signal
    raise exception using errcode = 'TP999', message = 'tempo-zurueck';
  exception when sqlstate 'TP999' then
      if not fertig or sqlerrm is distinct from 'tempo-zurueck' then
        raise exception 'TEMPO-S1 ABBRUCH, alles zurückgerollt: Lauf „%“ fehlgeschlagen (fremdes TP999 vor dem Abschluss): %', p_name, sqlerrm; end if;
    when others then raise exception 'TEMPO-S1 ABBRUCH, alles zurückgerollt: Lauf „%“ fehlgeschlagen (Merkheft/etappen_stand nicht für alle verglichen): %', p_name, sqlerrm;
  end;
  if not fertig then raise exception 'TEMPO-S1 ABBRUCH: Lauf „%“ ohne Abschluss', p_name; end if;
  return jsonb_build_object('lauf', p_name, 'merkheft', status, 'einheiten', (select count(*) from schule.einheit), 'je_kind_gemessen', (select count(*) from jsonb_object_keys(je)), 'kinder', kinder, 'paare', (select count(*) from jsonb_object_keys(h)), 'h', h, 'mh', mh,
    'ms_etappen_stand_alle', ms_es, 'ms_merkheft_summe', ms_mh, 'ms_merkheft_je_kind', je);
end $f$;
-- Vergleich zweier Läufe: beide „verglichen“, gleiche vollständige Kinder- und Paarmengen, keine Abweichung – sonst Abbruch
create or replace function pg_temp.tempo_gleich(a jsonb, b jsonb) returns jsonb language plpgsql as $f$
declare abw jsonb; abw_mh jsonb; n_kinder int := jsonb_array_length(a->'kinder');
begin
  if a->>'merkheft' is distinct from 'verglichen' or b->>'merkheft' is distinct from 'verglichen' then
    raise exception 'TEMPO-S1 ABBRUCH: Merkheft nicht verglichen (%: %, %: %)', a->>'lauf', a->>'merkheft', b->>'lauf', b->>'merkheft'; end if;
  if n_kinder = 0 or (select count(*) from schule.einheit) = 0 or coalesce((a->>'paare')::int, 0) = 0 or a->'kinder' is distinct from b->'kinder' then raise exception 'TEMPO-S1 ABBRUCH: Kindermengen leer oder verschieden (% / %)', a->'kinder', b->'kinder'; end if;
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
  select jsonb_build_object('md5', md5(p.prosrc), 'strict', p.proisstrict, 'ergebnis', pg_get_function_result(p.oid), 'menge', p.proretset,
           'kosten', p.procost, 'parallel', p.proparallel, 'leakproof', p.proleakproof,
           'eigenschaften', concat_ws('|', p.prokind, l.lanname, p.procost, p.prorows, p.provariadic, p.prosupport::oid, p.prosecdef, p.proleakproof, p.proisstrict, p.proretset, p.provolatile, p.proparallel, p.pronargs, p.pronargdefaults, pg_get_function_result(p.oid), pg_get_function_arguments(p.oid), array_to_string(p.proargtypes::oid[]::regtype[], ','), coalesce(p.proallargtypes::text, '-'), coalesce(p.proargmodes::text, '-'), coalesce(p.proargnames::text, '-'), coalesce(p.proargdefaults::text, '-'), coalesce(p.protrftypes::text, '-'), coalesce(p.probin, '-'), coalesce(p.prosqlbody::text, '-'), coalesce(p.proconfig::text, '-')),
           'besitz', concat_ws('|', p.proowner::regrole, coalesce(p.proacl::text, '-'), coalesce(obj_description(p.oid, 'pg_proc'), '-')))
    from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = 'schule.etappen_stand(bigint, bigint)'::regprocedure;
$f$;
-- Index-Prüfung wie in der Migration (gleicher Text, Test prüft das): wirft bei Abweichung, sonst 'ok'
create or replace function pg_temp.tempo_index_pruefen() returns text language plpgsql as $tempoidxf$
-- 1190: jede Eigenschaft gegen ein festes Soll – die vollständige Definition (pg_get_indexdef: Methode, Eindeutigkeit, Spalten, Reihenfolge, Kollation,
-- Operatorklasse, Sortieroptionen, INCLUDE, WITH-Optionen, Bedingung, Ausdrücke) exakt wie beabsichtigt; dazu einzeln aus pg_index/pg_class.
declare r record; v jsonb; soll jsonb; abw text;
begin
  for r in select * from (values
      ('aufgabe_einheit_pool_lz_idx', 'aufgabe', 'CREATE INDEX aufgabe_einheit_pool_lz_idx ON schule.aufgabe USING btree (einheit_id, pool, variante_gruppe)', 3),
      ('versuch_kind_aufgabe_idx', 'versuch', 'CREATE INDEX versuch_kind_aufgabe_idx ON schule.versuch USING btree (lernender_id, aufgabe_id)', 2)) x(name, tabelle, def, n) loop
    select jsonb_build_object('def', pg_get_indexdef(c.oid), 'am', am.amname, 'relkind', c.relkind, 'tabelle', t.relname, 'schema_t', nt.nspname,
             'natts', i.indnatts, 'nkeyatts', i.indnkeyatts, 'unique', i.indisunique, 'nulls_not_distinct', i.indnullsnotdistinct, 'primary', i.indisprimary,
             'exclusion', i.indisexclusion, 'immediate', i.indimmediate, 'clustered', i.indisclustered, 'valid', i.indisvalid, 'ready', i.indisready,
             'live', i.indislive, 'replident', i.indisreplident, 'pred', i.indpred is not null, 'exprs', i.indexprs is not null,
             'option', (select coalesce(bool_and(o = 0), true) from unnest(i.indoption::int2[]) o),
             'opclass_default', (select coalesce(bool_and(oc.opcdefault and oc.opcmethod = c.relam), false) from unnest(i.indclass::oid[]) k join pg_opclass oc on oc.oid = k),
             'kollation', (select coalesce(bool_and(k.coll = a.attcollation), false) from unnest(i.indcollation::oid[], i.indkey::int2[]) k(coll, att) join pg_attribute a on a.attrelid = t.oid and a.attnum = k.att),
             'tablespace_standard', c.reltablespace = 0, 'reloptions', c.reloptions is not null, 'persistence', c.relpersistence, 'partition', c.relispartition)
      into v
      from pg_class c join pg_namespace n on n.oid = c.relnamespace and n.nspname = 'schule' join pg_index i on i.indexrelid = c.oid
      join pg_class t on t.oid = i.indrelid join pg_namespace nt on nt.oid = t.relnamespace join pg_am am on am.oid = c.relam
     where c.relname = r.name;
    soll := jsonb_build_object('def', r.def, 'am', 'btree', 'relkind', 'i', 'tabelle', r.tabelle, 'schema_t', 'schule',
             'natts', r.n, 'nkeyatts', r.n, 'unique', false, 'nulls_not_distinct', false, 'primary', false,
             'exclusion', false, 'immediate', true, 'clustered', false, 'valid', true, 'ready', true,
             'live', true, 'replident', false, 'pred', false, 'exprs', false, 'option', true, 'opclass_default', true, 'kollation', true,
             'tablespace_standard', true, 'reloptions', false, 'persistence', 'p', 'partition', false);
    if v is distinct from soll then
      select string_agg(k || ': ' || coalesce(v->>k, '–') || ' statt ' || (soll->>k), '; ' order by k) into abw from jsonb_object_keys(soll) k where v->k is distinct from soll->k;
      raise exception 'TEMPO-S1 ABBRUCH: Index schule.% ist nicht der erwartete Index (Soll: %), Abweichung: % – nichts geändert', r.name, r.def, coalesce(abw, 'kein Index dieses Namens');
    end if;
  end loop;
  return 'ok';
end $tempoidxf$;
-- Hilfen dieser Sitzung im temporären Schema? (vor dem ersten Aufruf geprüft; am Ende: keine mehr)
create or replace function pg_temp.tempo_hilfen() returns jsonb language sql as $f$
  select coalesce(jsonb_agg(p.proname::text order by p.proname), '[]') from pg_proc p where p.pronamespace = pg_my_temp_schema() and p.proname like 'tempo\_%';
$f$;
do $h$ begin
  if (select count(*) from pg_proc p where p.pronamespace = pg_my_temp_schema() and p.proname in
      ('tempo_zugriff', 'tempo_merkheft_anlegen', 'tempo_lauf', 'tempo_gleich', 'tempo_indizes', 'tempo_funktion', 'tempo_hilfen', 'tempo_index_pruefen')) <> 8
  then raise exception 'TEMPO-S1 ABBRUCH: Hilfen nicht im temporären Schema'; end if;
end $h$;

create temp table tempo_bericht (b jsonb) on commit drop;
do $p$
declare f_vor jsonb; f_nach jsonb; idx_vor jsonb; idx_nach jsonb; l_alt jsonb; l_neu jsonb; l_end jsonb; g1 jsonb; g2 jsonb; t_sperre timestamptz; v_art constant text := 'f|sql|100|0|0|0|f|f|f|f|s|u|2|0|jsonb|p_lernender bigint, p_einheit bigint|bigint,bigint|-|-|{p_lernender,p_einheit}|-|-|-|-|{"search_path=\"\""}'; v_neu constant text := '3f49198f8dbf5c822a0be4650a5ebce5';
begin
  f_vor := pg_temp.tempo_funktion(); idx_vor := pg_temp.tempo_indizes();
  -- 1181: Sollzustand vor dem ersten Lauf (skalares jsonb, nicht STRICT, keine Menge, STABLE, Invoker, leerer search_path)
  if f_vor->>'eigenschaften' is distinct from v_art then
    raise exception 'TEMPO-S1 ABBRUCH, Vorbedingung: Eigenschaften von etappen_stand % statt % – nichts geändert', f_vor->>'eigenschaften', v_art; end if;
  perform pg_temp.tempo_merkheft_anlegen();
  l_alt := pg_temp.tempo_lauf('alt');
  execute (select teil1 from tempo_mig);
  l_neu := pg_temp.tempo_lauf('neu');
  g1 := pg_temp.tempo_gleich(l_alt, l_neu);
  t_sperre := clock_timestamp();
  execute (select teil2 from tempo_mig);
  perform pg_temp.tempo_index_pruefen();
  l_end := pg_temp.tempo_lauf('endzustand');
  g2 := pg_temp.tempo_gleich(l_alt, l_end);
  f_nach := pg_temp.tempo_funktion(); idx_nach := pg_temp.tempo_indizes();
  if f_nach->>'md5' is distinct from v_neu then raise exception 'TEMPO-S1 ABBRUCH: Funktionstext am Ende % statt %', f_nach->>'md5', v_neu; end if;
  if f_nach->'eigenschaften' is distinct from f_vor->'eigenschaften' then raise exception 'TEMPO-S1 ABBRUCH: Eigenschaften geändert % → %', f_vor->'eigenschaften', f_nach->'eigenschaften'; end if;
  if f_nach->'besitz' is distinct from f_vor->'besitz' then raise exception 'TEMPO-S1 ABBRUCH: Besitzer/Rechte/Kommentar geändert % → %', f_vor->'besitz', f_nach->'besitz'; end if;
  insert into tempo_bericht select jsonb_build_object(
    'funktion_vorher', f_vor, 'funktion_nachher', f_nach, 'eigenschaften_gleich', f_vor->'eigenschaften' = f_nach->'eigenschaften', 'besitz_gleich', f_vor->'besitz' = f_nach->'besitz',
    'indizes_soll', pg_temp.tempo_index_pruefen(),
    'schon_umgestellt_vorher', f_vor->>'md5' = v_neu,
    'vergleich_alt_neu', g1, 'vergleich_alt_endzustand', g2,
    'laeufe', jsonb_build_object('alt', l_alt - 'h' - 'mh', 'neu', l_neu - 'h' - 'mh', 'endzustand', l_end - 'h' - 'mh'),
    'indizes_vorher', idx_vor, 'indizes_nachher', idx_nach,
    'ms_unter_sperre_bis_vor_aufraeumen', round(extract(epoch from clock_timestamp() - t_sperre) * 1000, 1),
    'hinweis', 'Laufzeiten hier nur zur Orientierung (endzustand evtl. ohne nutzbaren Index, indcheckxmin); maßgeblich tempo_s1_messen.sql in neuer Transaktion');
end $p$;

-- Rückstände entfernen (auch bei Erfolg): Merkheft-Kopie, alle Hilfen, Hilfstabelle
drop function if exists pg_temp.tempo_merkheft(text, jsonb);
drop function if exists pg_temp.tempo_zugriff(text, bigint);
drop function if exists pg_temp.tempo_merkheft_anlegen();
drop function if exists pg_temp.tempo_lauf(text);
drop function if exists pg_temp.tempo_gleich(jsonb, jsonb);
drop function if exists pg_temp.tempo_indizes();
drop function if exists pg_temp.tempo_funktion();
drop function if exists pg_temp.tempo_index_pruefen();
drop table if exists pg_temp.tempo_mig;
do $r$ declare n int := (select count(*) from pg_proc p where p.pronamespace = pg_my_temp_schema() and p.proname like 'tempo\_%' and p.proname <> 'tempo_hilfen');
begin
  if n <> 0 or to_regclass('pg_temp.tempo_mig') is not null then raise exception 'TEMPO-S1 ABBRUCH: Rückstände in pg_temp (% Funktionen)', n; end if;
end $r$;
do $p$ declare b jsonb := (select b from tempo_bericht) || jsonb_build_object('rueckstaende', pg_temp.tempo_hilfen() - 'tempo_hilfen');
begin
  drop table pg_temp.tempo_bericht;
  drop function pg_temp.tempo_hilfen();
  if (select count(*) from pg_proc p where p.pronamespace = pg_my_temp_schema() and p.proname like 'tempo\_%') <> 0 then raise exception 'TEMPO-S1 ABBRUCH: Rückstände in pg_temp'; end if;
  raise notice 'TEMPO-S1 eingespielt: %', b::text;
end $p$;
