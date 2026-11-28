"""Test für TEMPO-S1 (supabase/migrations/20261207_tempo_s1.sql, Pakete aus tools/tests/tempo_einspielen.py) im lokalen NACHBAU
(tools/tests/tempo_nachbau.sql, erfundene Daten – NICHT die echte Datenbank). Gegenprüfung: Werkstatt 1175.

Teil 1 (immer): md5 alt/neu in der Migration = nachgerechnete Funktionstexte; Paket-Dateien unter tools/tests/aus auf dem Stand.
Teil 2 (nur mit lokalem Postgres), jeder Lauf wie beim Projektleiter: eine Transaktion, `set local statement_timeout/lock_timeout` vor dem äußeren do:
  - Probe besteht: alle Kind×Einheit-Paare, Merkheft in allen Läufen „verglichen“ für dieselben vollständigen Kinder, 0 Abweichungen, Hash alt → neu,
    Eigenschaften gleich, beide Soll-Indizes gültig; danach Funktionshash und Indexbestand unverändert.
  - Negativfälle (Probe UND Einspielen brechen ab, nichts geändert): ohne api.schule_merkheft; Merkheft ohne Zugriffsstelle; Merkheft scheitert für ein Kind;
    Kommentar-Trick (alte Fassung mit „TEMPO-S1“); Eigenschaft anders (volatile, security definer); gleichnamiger Index auf falscher Spalte / falscher
    Reihenfolge / ungültig.
  - Einspielen zweimal (wiederholbar); in derselben Verbindung danach keine Hilfsfunktion, keine Merkheft-Kopie, keine Hilfstabelle mehr.
  - neue Fassung gegen gespeicherte alte Antworten byte-gleich (auch Zusatzfälle); Messung ändert nichts.
  - Gegenprobe: verdorbene neue Fassungen (mit passend nachgerechnetem md5) und eine verdorbene Indexanlage brechen ab.
Aufruf: python3 -I tools/tests/tempo_test.py   (endet mit OK; ohne Postgres: Teil 2 übersprungen)
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regelbezug_sql_test as T  # noqa: E402
import tempo_einspielen as E  # noqa: E402

WURZEL = T.WURZEL
AUS = WURZEL / 'tools/tests/aus'
ALT, NEU = 'bf3152e9a378a1d4e41c98965acf738e', '3f49198f8dbf5c822a0be4650a5ebce5'
EIGENSCHAFTEN = 'f|sql|100|0|0|0|f|f|f|f|s|u|2|0|jsonb|p_lernender bigint, p_einheit bigint|bigint,bigint|-|-|{p_lernender,p_einheit}|-|-|-|-|{"search_path=\\"\\""}'


def py(*args):
    p = subprocess.run([sys.executable, '-I', *args], capture_output=True, text=True, cwd=str(WURZEL))
    return p.returncode, p.stdout, p.stderr


def lauf(pg, text, erwartet_fehler=None, danach=''):
    """Wie der Projektleiter: eine Transaktion, Zeitgrenzen als eigene Anweisungen, dann der Paketinhalt in EINEM execute (danach optional weitere SQL)."""
    assert '$rbpaketinhalt$' not in text
    return pg.sql("set local statement_timeout = '300s';\nset local lock_timeout = '3s';\n"
                  f'do $rbpaket$ begin execute $rbpaketinhalt${text}$rbpaketinhalt$; end $rbpaket$;\n{danach}', erwartet_fehler)


def fehlerzeile(out, stichwort):
    z = [x for x in out.splitlines() if 'ERROR:' in x]
    assert len(z) == 1 and stichwort in z[0], (stichwort, [x[:700] for x in z], out[-800:])
    return z[0]


def bericht(zeile):
    """Meldung „… KURZ {…} VOLL {…}“ (Probe/Einspielen) bzw. „… {…}“ (Messung): voller Bericht plus Kurzbericht unter 'kurz'."""
    d = json.JSONDecoder()
    if ' KURZ {' in zeile:
        kurz, _ = d.raw_decode(zeile[zeile.index(' KURZ {') + 6:]); voll, _ = d.raw_decode(zeile[zeile.index(' VOLL {') + 6:])
        assert zeile.index(' KURZ {') < zeile.index(' VOLL {') and len(json.dumps(kurz)) < 1200, 'Kurzbericht vorn und kompakt'
        return {**voll, 'kurz': kurz}
    return d.raw_decode(zeile[zeile.index('{'):])[0]


def wert(pg, sql):
    return pg.sql('\\pset tuples_only on\n\\pset format unaligned\n' + sql).strip()


def zustand(pg):
    """Funktionshash und Indexbestand (Nachkontrolle)."""
    return (wert(pg, "select md5(prosrc) from pg_proc where oid = 'schule.etappen_stand(bigint, bigint)'::regprocedure;"),
            wert(pg, "select string_agg(indexname || ':' || indexdef, ' | ' order by indexname) from pg_indexes where schemaname = 'schule' and tablename in ('aufgabe', 'versuch');"))


def antworten(pg):
    out = wert(pg, "select l.id || '/' || e.id || chr(9) || coalesce(schule.etappen_stand(l.id, e.id)::text, 'NULL') from schule.lernender l cross join schule.einheit e order by 1;")
    return dict(z.split('\t', 1) for z in out.splitlines())


def pruefe_bericht(r, *, schon=False):
    for g in ('vergleich_alt_neu', 'vergleich_alt_endzustand'):
        v = r[g]
        assert v['merkheft'] == 'verglichen' and v['kinder'] == [1, 2, 3, 4] and v['paare'] == 380, (g, v)
        assert v['abweichungen_etappen_stand'] == 0 and v['abweichungen_merkheft'] == 0, (g, v)
    for n in ('alt', 'neu', 'endzustand'):
        assert r['laeufe'][n]['merkheft'] == 'verglichen' and r['laeufe'][n]['kinder'] == [1, 2, 3, 4] and r['laeufe'][n]['paare'] == 380, r['laeufe'][n]
    assert r['funktion_vorher']['md5'] == (NEU if schon else ALT) and r['funktion_nachher']['md5'] == NEU and r['eigenschaften_gleich'], r
    assert r['funktion_nachher']['eigenschaften'] == EIGENSCHAFTEN, r['funktion_nachher']
    for f in ('funktion_vorher', 'funktion_nachher'):
        assert r[f]['strict'] is False and r[f]['ergebnis'] == 'jsonb' and r[f]['menge'] is False, r[f]
        assert r[f]['kosten'] == 100 and r[f]['parallel'] == 'u' and r[f]['leakproof'] is False, r[f]
    assert r['besitz_gleich'] is True and r['funktion_vorher']['besitz'] == r['funktion_nachher']['besitz'] and r['indizes_soll'] == 'ok', r
    soll = {'aufgabe_einheit_pool_lz_idx': 'aufgabe (einheit_id, pool, variante_gruppe)', 'versuch_kind_aufgabe_idx': 'versuch (lernender_id, aufgabe_id)'}
    for name, spalten in soll.items():
        x = [i for i in r['indizes_nachher'] if i['name'] == name]
        assert len(x) == 1 and x[0]['gueltig'] and f'ON schule.{spalten.split(" (")[0]} USING btree ({spalten.split(" (")[1]}' in x[0]['def'], (name, x)
    assert r['rueckstaende'] == [], r['rueckstaende']
    k = r['kurz']
    assert k['md5_vor'] == (NEU if schon else ALT) and k['md5_nach'] == NEU and k['eig_gleich'] and k['besitz_gleich'] and k['indizes_soll'] == 'ok', k
    assert k['alt_neu'] == k['alt_end'] == {'merkheft': 'verglichen', 'paare': 380, 'abweichungen_etappen_stand': 0, 'abweichungen_merkheft': 0}, k
    assert k['neue_indizes'] == ([] if schon else ['aufgabe_einheit_pool_lz_idx', 'versuch_kind_aufgabe_idx']) and k['indizes_vorher_gleich'] and k['rueckstaende'] == [], k
    assert isinstance(k['ms_unter_sperre'], (int, float)), k


ZUSATZ = """
-- Zusatzfälle: Flug gesetzt (kann wiederholen), Zusatz eingeplant, gesetzte Karten, Regel anwenden_pflicht aus
update schule.route set kann_wdh_themen = array[block_id] where lernender_id = 2 and block_id in (11, 13, 15);
update schule.thema set zusatz = '{gym_by}' where id in (21, 23);
update schule.karte_stand set gesetzt_am = now() - interval '5 days', wdh_stufe = 4, sitzt = true, sitzt_am = coalesce(sitzt_am, now() - interval '6 days')
 where lernender_id = 1 and einheit_id between 30 and 40;
update schule.regel set wert = '0' where schluessel = 'anwenden_pflicht';
"""
MERKHEFT_ECHT = None


def merkheft_def(pg):
    return wert(pg, "select pg_get_functiondef('api.schule_merkheft(text, jsonb)'::regprocedure);") + ';'


def verdorbene_migrationen(m):
    """Neue Fassung absichtlich falsch (nur im Speicher), v_neu passend nachgerechnet – nur der Vergleich darf sie aufhalten."""
    def mit(alt, neu):
        assert m.count(alt) == 1, alt[:60]
        x = m.replace(alt, neu)
        h = hashlib.md5(E.neuer_text(x).encode('utf-8')).hexdigest()
        return re.sub(r"v_neu constant text := '[0-9a-f]{32}'", f"v_neu constant text := '{h}'", x)
    return {
        'gesamt ohne Freigabe-Filter': mit("where a.einheit_id = p_einheit and a.pool = 'uebung' and a.freigegeben group by a.variante_gruppe) g",
                                           "where a.einheit_id = p_einheit and a.pool = 'uebung' group by a.variante_gruppe) g"),
        'geloest ohne distinct': mit('count(distinct v.aufgabe_id) geloest', 'count(v.aufgabe_id) geloest'),
        'folge_ziel anders': mit("'folge_ziel', least(3, z.ziel)", "'folge_ziel', least(4, z.ziel)"),
        'flug_nachtest fest': mit('cross join (select schule.flug_nachtest(p_lernender, p_einheit) v offset 0) fn', 'cross join (select false v offset 0) fn'),
        'Feld fehlt': mit("'bearbeitungen', schule.karte_bearbeitungen(p_lernender, p_einheit, z.lz), ", ''),
    }


def main():
    rc, out, err = py('tools/tests/tempo_einspielen.py', '--pruefen')
    assert rc == 0, 'Pakete nicht auf dem Stand: python3 -I tools/tests/tempo_einspielen.py\n' + err
    t1, t2, neu, art = E.migration()
    assert art == EIGENSCHAFTEN, art
    # Migration und Pakete prüfen mit demselben Ausdruck (Funktionseigenschaften) bzw. derselben Index-Soll-Liste
    mig = E.MIGRATION.read_text(encoding='utf-8'); pk = (AUS / 'tempo_s1_probe.sql').read_text(encoding='utf-8')
    eig = re.search(r"(concat_ws\('\|', p\.prokind.*?coalesce\(p\.proconfig::text, '-'\)\))", mig).group(1)
    assert mig.count(eig) == 2 and eig in pk and pk.count(eig) >= 2, 'Eigenschafts-Ausdruck verschieden'
    idx = mig[mig.index('  for r in select * from (values', mig.index('do $tempoidx$')):mig.index('end $tempoidx$;')]
    assert idx.replace('  end loop;\n', '') in pk.replace("  end loop;\n  return 'ok';\n", ''), 'Index-Prüfung verschieden'
    assert neu == NEU and hashlib.md5(E.alter_text().encode('utf-8')).hexdigest() == ALT
    alt_sql = E.alter_sql()
    b = T.pg_bin()
    if not b:
        print('Teil 2 übersprungen (kein Postgres)'); print('OK'); return
    pg = T.PG(b)
    lies = lambda n: (AUS / n).read_text(encoding='utf-8')
    probe, einspielen, messen = lies('tempo_s1_probe.sql'), lies('tempo_s1_einspielen.sql'), lies('tempo_s1_messen.sql')
    try:
        pg.sql((WURZEL / 'tools/tests/tempo_nachbau.sql').read_text(encoding='utf-8'))
        pg.sql(alt_sql)
        z0 = zustand(pg)
        assert z0[0] == ALT, z0
        vorher = antworten(pg)
        assert len(vorher) == 4 * 95 and sum(1 for v in vorher.values() if v not in ('{}', 'NULL')) > 250

        # 1. Probe besteht, ändert nichts
        r = bericht(fehlerzeile(lauf(pg, probe, erwartet_fehler='PROBELAUF bestanden'), 'PROBELAUF bestanden'))
        pruefe_bericht(r)
        assert not {'aufgabe_einheit_pool_lz_idx', 'versuch_kind_aufgabe_idx'} & {i['name'] for i in r['indizes_vorher']}
        print('Probe: Sperre', r['ms_unter_sperre_bis_vor_aufraeumen'], 'ms;', json.dumps({k: {x: r['laeufe'][k][x] for x in ('ms_etappen_stand_alle', 'ms_merkheft_summe')} for k in r['laeufe']}))
        assert zustand(pg) == z0, 'Probe hat etwas geändert'

        # 2. Negativfälle: Probe und Einspielen brechen ab, nichts geändert
        mh = merkheft_def(pg)
        faelle = [
            ('ohne api.schule_merkheft', 'alter function api.schule_merkheft(text, jsonb) rename to schule_merkheft_weg;',
             'alter function api.schule_merkheft_weg(text, jsonb) rename to schule_merkheft;', 'api.schule_merkheft(text, jsonb) fehlt'),
            ('Merkheft ohne Zugriffsstelle', mh.replace('perform schule.zugriff(p_schluessel, v_l);', 'perform 1;'), mh, 'keine Stelle schule.zugriff('),
            ('Merkheft scheitert für ein Kind', mh.replace('perform schule.zugriff(p_schluessel, v_l);',
             "perform schule.zugriff(p_schluessel, v_l);\n  if v_l = 4 then raise exception 'kaputt für Kind 4'; end if;"), mh, 'Lauf „alt“ fehlgeschlagen'),
            ('Kommentar-Trick', alt_sql.replace("as $$\n  select", "as $$\n  -- TEMPO-S1\n  select"), alt_sql, 'weicht vom Repo-Stand ab'),
            ('volatile', alt_sql.replace('language sql stable', 'language sql volatile'), alt_sql, 'Eigenschaften von etappen_stand'),
            ('etappen_stand STRICT (gleicher prosrc)', 'alter function schule.etappen_stand(bigint, bigint) strict;', 'alter function schule.etappen_stand(bigint, bigint) called on null input;',
             'Eigenschaften von etappen_stand'),
            ('Merkheft STRICT', 'alter function api.schule_merkheft(text, jsonb) strict;', 'alter function api.schule_merkheft(text, jsonb) called on null input;', 'ist STRICT'),
            ('Merkheft SQL-NULL bei einem Kind', mh.replace('perform schule.zugriff(p_schluessel, v_l);', "perform schule.zugriff(p_schluessel, v_l);\n  if v_l = 3 then return null; end if;"), mh,
             'Merkheft-Antwort für Kind 3 nicht im Vertrag'),
            ('Merkheft ok=false bei einem Kind', mh.replace('perform schule.zugriff(p_schluessel, v_l);', "perform schule.zugriff(p_schluessel, v_l);\n  if v_l = 2 then return jsonb_build_object('ok', false, 'fehler', 'x'); end if;"), mh,
             'Merkheft-Antwort für Kind 2 nicht im Vertrag'),
            ('Merkheft ohne einheiten', mh.replace("return jsonb_build_object('ok', true, 'einheiten',", "return jsonb_build_object('ok', true, 'einheiten_weg',"), mh, 'Merkheft-Antwort für Kind 1 nicht im Vertrag'),
            ('Merkheft JSON-null', mh.replace("return jsonb_build_object('ok', true, 'einheiten',", "return 'null'::jsonb; return jsonb_build_object('ok', true, 'einheiten',"), mh, 'Merkheft-Antwort für Kind 1 nicht im Vertrag'),
            ('security definer', alt_sql.replace("language sql stable set search_path", "language sql stable security definer set search_path"), alt_sql + 'alter function schule.etappen_stand(bigint, bigint) security invoker;', 'Eigenschaften von etappen_stand'),
            ('COST 77', 'alter function schule.etappen_stand(bigint, bigint) cost 77;', 'alter function schule.etappen_stand(bigint, bigint) cost 100;', 'Eigenschaften von etappen_stand'),
            ('PARALLEL RESTRICTED', 'alter function schule.etappen_stand(bigint, bigint) parallel restricted;', 'alter function schule.etappen_stand(bigint, bigint) parallel unsafe;', 'Eigenschaften von etappen_stand'),
            ('LEAKPROOF', 'alter function schule.etappen_stand(bigint, bigint) leakproof;', 'alter function schule.etappen_stand(bigint, bigint) not leakproof;', 'Eigenschaften von etappen_stand'),
            ('ROWS/SET anders', "alter function schule.etappen_stand(bigint, bigint) set work_mem = '8MB';", 'alter function schule.etappen_stand(bigint, bigint) reset work_mem;', 'Eigenschaften von etappen_stand'),
            ('Merkheft wirft TP999', mh.replace('perform schule.zugriff(p_schluessel, v_l);', "perform schule.zugriff(p_schluessel, v_l);\n  if v_l = 2 then raise exception using errcode = 'TP999', message = 'tempo-zurueck'; end if;"), mh, 'fremdes TP999'),
            ('keine Einheiten', 'alter table schule.einheit rename to einheit_weg; create table schule.einheit (like schule.einheit_weg including all);',
             'drop table schule.einheit; alter table schule.einheit_weg rename to einheit;', 'Kindermengen leer'),
            ('Index Kollation C', 'create index aufgabe_einheit_pool_lz_idx on schule.aufgabe (einheit_id, pool, variante_gruppe collate "C");', 'drop index schule.aufgabe_einheit_pool_lz_idx;', 'Index schule.aufgabe_einheit_pool_lz_idx ist nicht'),
            ('Index Kollation C an pool', 'create index aufgabe_einheit_pool_lz_idx on schule.aufgabe (einheit_id, pool collate "C", variante_gruppe);', 'drop index schule.aufgabe_einheit_pool_lz_idx;', 'Index schule.aufgabe_einheit_pool_lz_idx ist nicht'),
            ('Index Operatorklasse', 'create index aufgabe_einheit_pool_lz_idx on schule.aufgabe (einheit_id, pool text_pattern_ops, variante_gruppe);', 'drop index schule.aufgabe_einheit_pool_lz_idx;', 'Index schule.aufgabe_einheit_pool_lz_idx ist nicht'),
            ('Index DESC', 'create index versuch_kind_aufgabe_idx on schule.versuch (lernender_id, aufgabe_id desc);', 'drop index schule.versuch_kind_aufgabe_idx;', 'Index schule.versuch_kind_aufgabe_idx ist nicht'),
            ('Index NULLS FIRST', 'create index versuch_kind_aufgabe_idx on schule.versuch (lernender_id nulls first, aufgabe_id);', 'drop index schule.versuch_kind_aufgabe_idx;', 'Index schule.versuch_kind_aufgabe_idx ist nicht'),
            ('Index mit Bedingung', 'create index versuch_kind_aufgabe_idx on schule.versuch (lernender_id, aufgabe_id) where testsitzung_id is null;', 'drop index schule.versuch_kind_aufgabe_idx;', 'Index schule.versuch_kind_aufgabe_idx ist nicht'),
            ('Index INCLUDE', 'create index versuch_kind_aufgabe_idx on schule.versuch (lernender_id, aufgabe_id) include (richtig);', 'drop index schule.versuch_kind_aufgabe_idx;', 'Index schule.versuch_kind_aufgabe_idx ist nicht'),
            ('Index fillfactor', 'create index versuch_kind_aufgabe_idx on schule.versuch (lernender_id, aufgabe_id) with (fillfactor = 70);', 'drop index schule.versuch_kind_aufgabe_idx;', 'Index schule.versuch_kind_aufgabe_idx ist nicht'),
            ('Index hash', 'create index aufgabe_einheit_pool_lz_idx on schule.aufgabe using hash (einheit_id);', 'drop index schule.aufgabe_einheit_pool_lz_idx;', 'Index schule.aufgabe_einheit_pool_lz_idx ist nicht'),
            ('Index falsche Spalte', 'create index aufgabe_einheit_pool_lz_idx on schule.aufgabe (id);', 'drop index schule.aufgabe_einheit_pool_lz_idx;', 'Index schule.aufgabe_einheit_pool_lz_idx ist nicht'),
            ('Index falsche Reihenfolge', 'create index versuch_kind_aufgabe_idx on schule.versuch (aufgabe_id, lernender_id);', 'drop index schule.versuch_kind_aufgabe_idx;', 'Index schule.versuch_kind_aufgabe_idx ist nicht'),
            ('Index ungültig', "create index versuch_kind_aufgabe_idx on schule.versuch (lernender_id, aufgabe_id); update pg_index set indisvalid = false where indexrelid = 'schule.versuch_kind_aufgabe_idx'::regclass;",
             'drop index schule.versuch_kind_aufgabe_idx;', 'Index schule.versuch_kind_aufgabe_idx ist nicht'),
        ]
        for name, kaputt, heil, stichwort in faelle:
            pg.sql(kaputt); z1 = zustand(pg)
            for paket in (probe, einspielen):
                fehlerzeile(lauf(pg, paket, erwartet_fehler=stichwort), stichwort)
                assert zustand(pg) == z1, (name, 'Abbruch hat etwas geändert')
            pg.sql(heil)
            assert zustand(pg) == z0, (name, 'Rückbau unvollständig')
            print('Abbruch ok:', name)

        # 3. Gegenprobe: verdorbene neue Fassungen und verdorbene Indexanlage
        m = E.MIGRATION.read_text(encoding='utf-8')
        for name, x in verdorbene_migrationen(m).items():
            fehlerzeile(lauf(pg, E.paket(True, x), erwartet_fehler='Ergebnis weicht ab'), 'Ergebnis weicht ab')
            assert zustand(pg) == z0; print('Gegenprobe ok:', name)
        x = m.replace('on schule.aufgabe (einheit_id, pool, variante_gruppe);', 'on schule.aufgabe (pool, einheit_id, variante_gruppe);')
        assert x != m
        fehlerzeile(lauf(pg, E.paket(True, x), erwartet_fehler='ist nicht der erwartete'), 'Index schule.aufgabe_einheit_pool_lz_idx ist nicht')
        assert zustand(pg) == z0; print('Gegenprobe ok: Index in falscher Reihenfolge angelegt')

        # 3b. Mess-Paket vor dem Einspielen: Abbruch (Vorbedingung), keine Messmeldung
        out = pg.sql("set local statement_timeout = '300s';\n" + f'do $rbpaket$ begin execute $rbpaketinhalt${messen}$rbpaketinhalt$; end $rbpaket$;', 'MESSUNG ABBRUCH')
        fehlerzeile(out, 'MESSUNG ABBRUCH, Vorbedingung'); assert not any('MESSUNG (nichts geändert)' in z for z in out.splitlines() if 'ERROR:' in z)
        print('Messung vor dem Einspielen: Abbruch ok')

        # 4. Zusatzfälle vorher speichern
        pg.sql(ZUSATZ)
        vorher2 = antworten(pg)
        assert vorher2 != vorher, 'Zusatzfälle ohne Wirkung'
        pg.sql("update schule.regel set wert = '1' where schluessel = 'anwenden_pflicht';")
        vorher3 = antworten(pg)
        pg.sql("update schule.regel set wert = '0' where schluessel = 'anwenden_pflicht';")

        # 5. Einspielen zweimal; in derselben Verbindung danach keine Rückstände
        rest_sql = ("select 'REST=' || count(*) from pg_proc p where p.pronamespace = pg_my_temp_schema();\n"
                    "select 'TABELLEN=' || count(*) from pg_class c where c.relnamespace = pg_my_temp_schema();\n")
        for nr in (1, 2):
            out = lauf(pg, einspielen, danach=rest_sql)
            h = [z for z in out.splitlines() if 'NOTICE:' in z and 'TEMPO-S1 eingespielt' in z]
            assert len(h) == 1, out[-2500:]
            r = bericht(h[0])
            pruefe_bericht(r, schon=(nr == 2))
            assert 'REST=0' in out and 'TABELLEN=0' in out, out[-600:]
            print(f'Einspielen {nr}: Sperre', r['ms_unter_sperre_bis_vor_aufraeumen'], 'ms')
        z2 = zustand(pg)
        assert z2[0] == NEU and 'aufgabe_einheit_pool_lz_idx' in z2[1] and 'versuch_kind_aufgabe_idx' in z2[1], z2

        # 6. neue Fassung gegen gespeicherte alte Antworten (jsonb als Text)
        nachher2 = antworten(pg)
        anders = [k for k in vorher2 if vorher2[k] != nachher2.get(k)]
        assert not anders and len(nachher2) == len(vorher2), anders[:5]
        pg.sql("update schule.regel set wert = '1' where schluessel = 'anwenden_pflicht';")
        anders = [k for k, v in antworten(pg).items() if vorher3[k] != v]
        assert not anders, anders[:5]

        # 7. Messung: ändert nichts, keine Rückstände (Rollback)
        out = pg.sql("set local statement_timeout = '300s';\n" + f'do $rbpaket$ begin execute $rbpaketinhalt${messen}$rbpaketinhalt$; end $rbpaket$;', 'MESSUNG')
        mz = bericht(fehlerzeile(out, 'MESSUNG (nichts geändert)'))
        assert mz['md5'] == NEU and mz['merkheft'] == 'verglichen' and mz['kinder'] == [1, 2, 3, 4] and mz['je_kind_gemessen'] == 4 and mz['paare'] == 380 and mz['indizes_soll'] == 'ok', mz
        assert zustand(pg) == z2
        pg.sql(mh.replace('perform schule.zugriff(p_schluessel, v_l);', "perform schule.zugriff(p_schluessel, v_l);\n  if v_l = 2 then raise exception using errcode = 'TP999', message = 'tempo-zurueck'; end if;"))
        out = pg.sql("set local statement_timeout = '300s';\n" + f'do $rbpaket$ begin execute $rbpaketinhalt${messen}$rbpaketinhalt$; end $rbpaket$;', 'fremdes TP999')
        fehlerzeile(out, 'fremdes TP999'); assert not any('MESSUNG (nichts geändert)' in z for z in out.splitlines() if 'ERROR:' in z); pg.sql(mh)
        print('Messung mit fremdem TP999: Abbruch ok')
        pg.sql(mh.replace('perform schule.zugriff(p_schluessel, v_l);', "perform schule.zugriff(p_schluessel, v_l);\n  if v_l = 2 then raise exception 'innerer Fehler bei Kind 2'; end if;"))
        out = pg.sql("set local statement_timeout = '300s';\n" + f'do $rbpaket$ begin execute $rbpaketinhalt${messen}$rbpaketinhalt$; end $rbpaket$;', 'innerer Fehler bei Kind 2')
        fehlerzeile(out, 'fehlgeschlagen'); assert not any('MESSUNG (nichts geändert)' in z for z in out.splitlines() if 'ERROR:' in z); pg.sql(mh)
        print('Messung mit innerem Fehler beim zweiten Kind: Abbruch ok')
        print('Messung danach:', json.dumps({k: mz[k] for k in ('ms_etappen_stand_alle', 'ms_merkheft_summe', 'ms_merkheft_je_kind')}))
    finally:
        pg.ende()
    print('OK')


if __name__ == '__main__':
    main()
