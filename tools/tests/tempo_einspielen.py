"""TEMPO-S1: Pakete für supabase/migrations/20261207_tempo_s1.sql (schule.etappen_stand schneller, Ergebnis byte-gleich; zwei Indizes).
Gegenprüfung: Werkstatt 1175. Ausführung: inhalte/plan/ladezeiten.md, Abschnitt „Einspielen TEMPO-S1“.

Schreibt nach tools/tests/aus/ (je Schritt EINE Datei, in einem `execute` lauffähig: kein psql-Meta, kein eigenes BEGIN/COMMIT):
  tempo_s1_probe.sql      Probelauf: Lauf „alt“ → Funktion ersetzen → Lauf „neu“ → Indizes → Lauf „endzustand“; jeder Lauf: etappen_stand für alle
                          Kinder × Einheiten und je Kind die Merkheft-Kopie (md5). Endet IMMER mit „PROBELAUF bestanden, ALLES zurückgerollt …“
                          oder „TEMPO-S1 ABBRUCH …“ (jede Abweichung, jeder nicht verglichene Lauf/jedes Kind, fehlende Merkheft-API, falscher Index).
  tempo_s1_einspielen.sql dasselbe, bleibt bei Gleichheit eingespielt (Hinweis „TEMPO-S1 eingespielt: …“); entfernt am Ende alle Hilfen in pg_temp.
  tempo_s1_messen.sql     nach dem Einspielen (neue Transaktion): nur Laufzeiten, rollt immer zurück („MESSUNG (nichts geändert): …“).
Die Merkheft-Kopie: api.schule_merkheft liegt nicht im Repo; das Paket legt aus ihrem eingespielten Text eine Kopie im temporären Schema an, deren
Zugriffsprüfung (schule.zugriff) durch eine Funktion ohne Prüfung ersetzt ist (Invoker) – nur zum Vergleichen und Messen in dieser Sitzung.

Aufruf:  python3 -I tools/tests/tempo_einspielen.py             -> schreibt die Dateien, druckt Größe und md5
         python3 -I tools/tests/tempo_einspielen.py --pruefen   -> schreibt nichts; Rückgabe 1, wenn eine Datei nicht dem Stand entspricht
         python3 -I tools/tests/tempo_einspielen.py --alt-sql   -> druckt create-Anweisung der ALTEN etappen_stand (für den lokalen Nachbau)
"""
import hashlib
import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
MIG = WURZEL / 'supabase/migrations'
AUS = WURZEL / 'tools/tests/aus'
MIGRATION = MIG / '20261207_tempo_s1.sql'


def alter_text():
    """Funktionstext (prosrc) von schule.etappen_stand nach allen Migrationen im Repo, in ihrer Reihenfolge nachgerechnet."""
    s = (MIG / '20261114_w150_lernkarten_meisterschaft.sql').read_text(encoding='utf-8')
    i = s.index('create or replace function schule.etappen_stand(')
    j = s.index('as $$', i) + 5
    b = s[j:s.index('$$;', j)]

    def rep(b, alt, neu, datei):
        assert b.count(alt) == 1, (datei, alt[:50])
        return b.replace(alt, neu)
    # 20261116_w150_r3_wiederholung_lerntage.sql
    b = rep(b, 'k.sitzt and k.faellig_am <= now()', 'schule.karte_faellig(k)', '20261116_w150_r3_wiederholung_lerntage.sql')
    # 20261116_w150_sitzt_regel_6_mit_schwer.sql
    b = rep(b, "'sitzt', coalesce(k.sitzt, false),", "'sitzt', coalesce(k.sitzt, false), 'schwer_ok', coalesce(k.schwer_ok, false), 'schwer_noetig', schule.karte_schwer_noetig(p_einheit, z.lz),",
            '20261116_w150_sitzt_regel_6_mit_schwer.sql')
    # 20261118_w176_t1_punkteregel.sql
    b = rep(b, "'wdh_stufe', coalesce(k.wdh_stufe, 0),", """'wdh_stufe', coalesce(k.wdh_stufe, 0),
           'eigene_loesungen', coalesce(k.eigene_loesungen, 0), 'folge', coalesce(k.folge, 0), 'folge_ziel', least(3, schule.karte_ziel(p_einheit, z.lz)),
           'typen_anzahl', coalesce(array_length(k.typen, 1), 0), 'typen_noetig', schule.karte_typen_noetig(p_einheit, z.lz),
           'fehler_folge', coalesce(k.fehler_folge, 0), 'stufe_senkung', coalesce(k.stufe_senkung, 0), 'sicher', coalesce(schule.karte_sicher(k), false),""",
            '20261118_w176_t1_punkteregel.sql')
    # 20261118_w176_t3_mischkarten.sql
    b = rep(b, "'sicher', coalesce(schule.karte_sicher(k), false),", "'sicher', coalesce(schule.karte_sicher(k), false), 'misch_ok', k.misch_ok_am is not null,",
            '20261118_w176_t3_mischkarten.sql')
    # 20261119_w176_h_muss.sql
    b = rep(b, "'fertig', coalesce(k.sitzt, false) or coalesce(s.status in ('nachgewiesen','korrigiert','gesichert'), false)",
            "'fertig', schule.etappe_fertig(k, s.status), 'test_nachgewiesen', coalesce(s.status in ('nachgewiesen','korrigiert','gesichert'), false), 'wieder_offen', not coalesce(k.sitzt, false) and k.sitzt_am is not null, 'gezaehlt', coalesce((select jsonb_agg(x::bigint) from jsonb_object_keys(k.gezaehlt) x), '[]'::jsonb)",
            '20261119_w176_h_muss.sql')
    b = rep(b, "'misch_ok', k.misch_ok_am is not null,",
            "'misch_ok', k.misch_ok_am is not null and k.misch_ok_am >= coalesce(k.sitzt_am, k.misch_ok_am), 'flug_nachtest', schule.flug_nachtest(p_lernender, p_einheit),",
            '20261119_w176_h_muss.sql')
    # 20261203_ft_s_form_takt.sql
    b = rep(b, "'schwer_ok', coalesce(k.schwer_ok, false), 'schwer_noetig'", """'schwer_ok', coalesce(k.schwer_ok, false), 'anwenden_noetig', schule.karte_anwenden_pflicht(k, p_einheit, z.lz), 'anwenden_ok', coalesce(schule.karte_anwenden_ok(k), false),
           'bearbeitungen', schule.karte_bearbeitungen(p_lernender, p_einheit, z.lz), 'schwer_noetig'""", '20261203_ft_s_form_takt.sql')
    return b


def alter_sql():
    return ("create or replace function schule.etappen_stand(p_lernender bigint, p_einheit bigint) returns jsonb\n"
            "language sql stable set search_path to '' as $$" + alter_text() + "$$;\n")


TEIL1 = '-- ==== TEMPO-S1 Teil 1: Funktion ===='
TEIL2 = '-- ==== TEMPO-S1 Teil 2: Indizes ===='


def neuer_text(m=None):
    """Funktionstext (prosrc) der neuen etappen_stand aus der Migration."""
    m = m if m is not None else MIGRATION.read_text(encoding='utf-8')
    i = m.index('as $function$', m.index('execute $neu$')) + len('as $function$')
    return m[i:m.index('$function$', i)]


def migration(m=None):
    """Migration in zwei Teilen (Funktion | Indizes); prüft die beiden md5 im Text gegen die nachgerechneten Funktionstexte."""
    m = m if m is not None else MIGRATION.read_text(encoding='utf-8')
    alt = re.search(r"v_alt constant text := '([0-9a-f]{32})'", m).group(1)
    neu = re.search(r"v_neu constant text := '([0-9a-f]{32})'", m).group(1)
    assert alt == hashlib.md5(alter_text().encode('utf-8')).hexdigest(), f'md5 alt in der Migration ({alt}) passt nicht zum Repo-Stand'
    assert neu == hashlib.md5(neuer_text(m).encode('utf-8')).hexdigest(), f'md5 neu in der Migration ({neu}) passt nicht zum Funktionstext'
    assert m.count(TEIL1) == 1 and m.count(TEIL2) == 1 and m.index(TEIL1) < m.index(TEIL2)
    for marke in ('$tempomig$', '$tempoteil$', '$rbpaket$', '$rbpaketinhalt$'): assert marke not in m, marke
    kopf, rest = m.split(TEIL1)
    t1, t2 = rest.split(TEIL2)
    return kopf + TEIL1 + t1, TEIL2 + t2, neu, re.search(r"v_art_soll constant text := '([^']*)'", m).group(1)


HILFEN = r"""
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
@@INDEXPRUEFUNG@@
-- Hilfen dieser Sitzung im temporären Schema? (vor dem ersten Aufruf geprüft; am Ende: keine mehr)
create or replace function pg_temp.tempo_hilfen() returns jsonb language sql as $f$
  select coalesce(jsonb_agg(p.proname::text order by p.proname), '[]') from pg_proc p where p.pronamespace = pg_my_temp_schema() and p.proname like 'tempo\_%';
$f$;
do $h$ begin
  if (select count(*) from pg_proc p where p.pronamespace = pg_my_temp_schema() and p.proname in
      ('tempo_zugriff', 'tempo_merkheft_anlegen', 'tempo_lauf', 'tempo_gleich', 'tempo_indizes', 'tempo_funktion', 'tempo_hilfen', 'tempo_index_pruefen')) <> 8
  then raise exception 'TEMPO-S1 ABBRUCH: Hilfen nicht im temporären Schema'; end if;
end $h$;
"""

AUFRAEUMEN = r"""
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
"""


def index_pruefung(m=None):
    """Index-Prüfung der Migration (Teil 2) als Hilfsfunktion für Bericht und Mess-Paket – derselbe Text, nur mit „return 'ok'“."""
    m = m if m is not None else MIGRATION.read_text(encoding='utf-8')
    blk = m[m.index('do $tempoidx$') + len('do $tempoidx$'):m.index('end $tempoidx$;')]
    assert blk.count('  end loop;\n') == 1
    return ("create or replace function pg_temp.tempo_index_pruefen() returns text language plpgsql as $tempoidxf$"
            + blk.replace('  end loop;\n', "  end loop;\n  return 'ok';\n") + 'end $tempoidxf$;')


# Kurzbericht vorn (Projektleiter: lange Meldungen werden abgeschnitten) – danach der volle Bericht
KURZ = r"""jsonb_build_object(
    'ms_unter_sperre', b->'ms_unter_sperre_bis_vor_aufraeumen',
    'alt_neu', (b->'vergleich_alt_neu') - 'gegen' - 'kinder', 'alt_end', (b->'vergleich_alt_endzustand') - 'gegen' - 'kinder', 'kinder', b#>'{vergleich_alt_neu,kinder}',
    'md5_vor', b#>>'{funktion_vorher,md5}', 'md5_nach', b#>>'{funktion_nachher,md5}',
    'eig_gleich', b->'eigenschaften_gleich', 'besitz_gleich', b->'besitz_gleich', 'indizes_soll', b->'indizes_soll',
    'neue_indizes', (select coalesce(jsonb_agg(x->>'name' order by x->>'name'), '[]') from jsonb_array_elements(b->'indizes_nachher') x
                      where not exists (select 1 from jsonb_array_elements(b->'indizes_vorher') y where y->>'name' = x->>'name')),
    'indizes_vorher_gleich', (select coalesce(jsonb_agg(y), '[]') from jsonb_array_elements(b->'indizes_vorher') y)
                              <@ (select coalesce(jsonb_agg(x - 'indcheckxmin'), '[]') || coalesce(jsonb_agg(x), '[]') from jsonb_array_elements(b->'indizes_nachher') x),
    'rueckstaende', b->'rueckstaende')"""


def paket(probe, m=None):
    t1, t2, neu, art = migration(m)
    titel = 'Probelauf' if probe else 'Einspiel-Paket'
    kopf = f"""-- TEMPO-S1 {titel} (erzeugt von tools/tests/tempo_einspielen.py). Ein Aufruf, EINE Transaktion; Fehler = alles zurück.
-- Ausführung: inhalte/plan/ladezeiten.md, Abschnitt „Einspielen TEMPO-S1“ (statement_timeout und lock_timeout als eigene Anweisungen VOR dem äußeren do).
-- Ablauf: Hilfen → Lauf „alt“ → Funktion ersetzen (Teil 1) → Lauf „neu“ (ohne Sperre an Tabellen) → Indizes (Teil 2, ab hier SHARE auf aufgabe/versuch)
--         → Lauf „endzustand“ (nur Gleichheitsbeweis) → {'Bericht, Aufräumen, Abschlussfehler (Rollback)' if probe else 'Aufräumen, Bericht'}.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '300s', true);
do $p$ begin
  if to_regprocedure('schule.etappen_stand(bigint, bigint)') is null or to_regclass('schule.aufgabe') is null or to_regclass('schule.versuch') is null
     or to_regclass('schule.lernender') is null or to_regclass('schule.einheit') is null then
    raise exception 'TEMPO-S1 ABBRUCH, Vorbedingung: schule.etappen_stand / aufgabe / versuch / lernender / einheit fehlt – nichts geändert';
  end if;
end $p$;
create temp table tempo_mig on commit drop as select $tempoteil${t1}$tempoteil$::text as teil1, $tempoteil${t2}$tempoteil$::text as teil2;
"""
    haupt = r"""
create temp table tempo_bericht (b jsonb) on commit drop;
do $p$
declare f_vor jsonb; f_nach jsonb; idx_vor jsonb; idx_nach jsonb; l_alt jsonb; l_neu jsonb; l_end jsonb; g1 jsonb; g2 jsonb; t_sperre timestamptz; v_art constant text := '""" + art + r"""'; v_neu constant text := '""" + neu + r"""';
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
"""
    if probe:
        ende = AUFRAEUMEN + r"""do $p$ declare b jsonb := (select b from tempo_bericht) || jsonb_build_object('rueckstaende', pg_temp.tempo_hilfen() - 'tempo_hilfen');
begin
  raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): KURZ % VOLL %', """ + KURZ + r"""::text, b::text;
end $p$;
"""
    else:
        ende = AUFRAEUMEN + r"""do $p$ declare b jsonb := (select b from tempo_bericht) || jsonb_build_object('rueckstaende', pg_temp.tempo_hilfen() - 'tempo_hilfen');
begin
  drop table pg_temp.tempo_bericht;
  drop function pg_temp.tempo_hilfen();
  if (select count(*) from pg_proc p where p.pronamespace = pg_my_temp_schema() and p.proname like 'tempo\_%') <> 0 then raise exception 'TEMPO-S1 ABBRUCH: Rückstände in pg_temp'; end if;
  raise notice 'TEMPO-S1 eingespielt: KURZ % VOLL %', """ + KURZ + r"""::text, b::text;
end $p$;
"""
    return kopf + HILFEN.replace('@@INDEXPRUEFUNG@@', index_pruefung(m)) + haupt + ende


def messen():
    t1, t2, neu, art = migration()
    return """-- TEMPO-S1 Messung (erzeugt von tools/tests/tempo_einspielen.py). Nach dem Einspielen in einer NEUEN Transaktion ausführen. Ändert nichts:
-- legt nur Hilfen in pg_temp an und endet immer mit „MESSUNG (nichts geändert): …“ (Fehler = alles zurück, auch die Hilfen).
select set_config('statement_timeout', '300s', true);
""" + HILFEN.replace('@@INDEXPRUEFUNG@@', index_pruefung()) + r"""
do $p$
declare x jsonb; f jsonb := pg_temp.tempo_funktion(); v_neu constant text := '""" + neu + r"""'; v_art constant text := '""" + art + r"""';
  n_kinder int := (select count(*) from schule.lernender); n_einheiten int := (select count(*) from schule.einheit);
begin
  -- 1190: Vorbedingungen positiv nachweisen (eingespielter Stand), sonst Abbruch statt Messmeldung
  if f->>'md5' is distinct from v_neu or f->>'eigenschaften' is distinct from v_art then
    raise exception 'TEMPO-S1 MESSUNG ABBRUCH, Vorbedingung: etappen_stand nicht im eingespielten Stand (md5 %, Eigenschaften %)', f->>'md5', f->>'eigenschaften'; end if;
  perform pg_temp.tempo_index_pruefen();
  if n_kinder = 0 or n_einheiten = 0 then raise exception 'TEMPO-S1 MESSUNG ABBRUCH: keine Kinder bzw. Einheiten (% / %)', n_kinder, n_einheiten; end if;
  perform pg_temp.tempo_merkheft_anlegen();
  x := pg_temp.tempo_lauf('messung');
  if x->>'merkheft' is distinct from 'verglichen' or jsonb_array_length(x->'kinder') <> n_kinder or (x->>'paare')::int <> n_kinder * n_einheiten
     or (x->>'je_kind_gemessen')::int <> n_kinder or (select count(*) from jsonb_object_keys(x->'mh')) <> n_kinder then
    raise exception 'TEMPO-S1 MESSUNG ABBRUCH: Lauf unvollständig (%)', (x - 'h' - 'mh')::text; end if;
  raise exception 'MESSUNG (nichts geändert): %', jsonb_build_object('md5', f->'md5', 'paare', x->'paare', 'je_kind_gemessen', x->'je_kind_gemessen',
    'merkheft', x->>'merkheft', 'kinder', x->'kinder', 'ms_etappen_stand_alle', x->'ms_etappen_stand_alle', 'ms_merkheft_summe', x->'ms_merkheft_summe',
    'ms_merkheft_je_kind', x->'ms_merkheft_je_kind', 'indizes_soll', 'ok')::text;   -- Indizes geprüft (tempo_index_pruefen oben), Definitionen gleich Soll
end $p$;
"""


def pakete():
    out = [('tempo_s1_probe.sql', paket(True)), ('tempo_s1_einspielen.sql', paket(False)), ('tempo_s1_messen.sql', messen())]
    for marke in ('$tempoteil$',): assert all(t.count(marke) in (0, 4) for _, t in out)
    for name, text in out:
        assert len(text.encode('utf-8')) < 1_500_000, name
        assert not re.search(r'^\s*\\', text, re.M), f'{name}: psql-Meta'
        assert not re.search(r'^\s*(begin|commit|rollback|start transaction)\s*;', text, re.M | re.I), f'{name}: eigenes BEGIN/COMMIT'
        assert '$rbpaket$' not in text, name
    return out


def main():
    if '--alt-sql' in sys.argv:
        sys.stdout.write(alter_sql()); return
    out = pakete()
    if '--pruefen' in sys.argv:
        alt = [n for n, t in out if not (AUS / n).exists() or (AUS / n).read_text(encoding='utf-8') != t]
        if alt: print('nicht auf dem Stand:', ', '.join(alt), file=sys.stderr); sys.exit(1)
        print('OK'); return
    print('| Datei | Bytes | md5 |\n|---|---|---|')
    for n, t in out:
        (AUS / n).write_text(t, encoding='utf-8')
        print(f'| `tools/tests/aus/{n}` | {len(t.encode("utf-8")):,} | `{hashlib.md5(t.encode("utf-8")).hexdigest()}` |'.replace(',', ' '))


if __name__ == '__main__':
    main()
