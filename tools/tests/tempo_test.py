"""Test für TEMPO-S1 (supabase/migrations/20261207_tempo_s1.sql, Pakete aus tools/tests/tempo_einspielen.py) im lokalen NACHBAU
(tools/tests/tempo_nachbau.sql, erfundene Daten – NICHT die echte Datenbank).

Teil 1 (immer): md5 in der Migration = nachgerechneter Repo-Stand; Paket-Dateien unter tools/tests/aus auf dem Stand.
Teil 2 (nur mit lokalem Postgres): leere Instanz, Nachbau mit ALTER etappen_stand (Text aus den Migrationen; md5 im Katalog = erwartet);
  Probelauf meldet „PROBELAUF bestanden“ ohne Abweichung (alle Kinder × Einheiten, Merkheft-Kopie verglichen) und ändert nichts;
  eine veränderte alte Fassung lässt Probe und Einspielen mit „Vorbedingung“ abbrechen; Einspielen läuft, zweimal (wiederholbar);
  danach: neue Fassung gegen gespeicherte alte Antworten für JEDES Kind × JEDE Einheit byte-gleich (jsonb::text), auch mit Zusatzfällen
  (gesetzter Flug, kann wiederholen, Zusatz eingeplant, Regel anwenden_pflicht aus/an); Messung läuft und ändert nichts; Laufzeiten vorher/nachher.
Aufruf: python3 -I tools/tests/tempo_test.py   (endet mit OK; ohne Postgres: Teil 2 übersprungen)
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regelbezug_sql_test as T  # noqa: E402

WURZEL = T.WURZEL
AUS = WURZEL / 'tools/tests/aus'


def py(*args):
    p = subprocess.run([sys.executable, '-I', *args], capture_output=True, text=True, cwd=str(WURZEL))
    return p.returncode, p.stdout, p.stderr


def fehlerzeile(out, stichwort):
    z = [x for x in out.splitlines() if 'ERROR:' in x]
    assert len(z) == 1 and stichwort in z[0], out[-2000:]
    return z[0]


def bericht(zeile):
    return json.loads(zeile[zeile.index('{'):])


def antworten(pg):
    out = pg.sql("\\pset tuples_only on\n\\pset format unaligned\n"
                 "select l.id || '/' || e.id || '\t' || coalesce(schule.etappen_stand(l.id, e.id)::text, 'NULL') from schule.lernender l cross join schule.einheit e order by 1;")
    return dict(z.split('\t', 1) for z in out.strip().splitlines())


ZUSATZ = """
-- Zusatzfälle: Flug gesetzt (kann wiederholen), Zusatz eingeplant, gesetzte Karten, Regel anwenden_pflicht aus
update schule.route set kann_wdh_themen = array[block_id] where lernender_id = 2 and block_id in (11, 13, 15);
update schule.thema set zusatz = '{gym_by}' where id in (21, 23);
update schule.karte_stand set gesetzt_am = now() - interval '5 days', wdh_stufe = 4, sitzt = true, sitzt_am = coalesce(sitzt_am, now() - interval '6 days')
 where lernender_id = 1 and einheit_id between 30 and 40;
update schule.regel set wert = '0' where schluessel = 'anwenden_pflicht';
"""


def main():
    rc, out, err = py('tools/tests/tempo_einspielen.py', '--pruefen')
    assert rc == 0, 'Pakete nicht auf dem Stand: python3 -I tools/tests/tempo_einspielen.py\n' + err
    rc, alt_sql, err = py('tools/tests/tempo_einspielen.py', '--alt-sql')
    assert rc == 0, err
    b = T.pg_bin()
    if not b:
        print('Teil 2 übersprungen (kein Postgres)'); print('OK'); return
    pg = T.PG(b)
    lies = lambda n: (AUS / n).read_text(encoding='utf-8')
    try:
        pg.sql((WURZEL / 'tools/tests/tempo_nachbau.sql').read_text(encoding='utf-8'))
        pg.sql(alt_sql)
        md5 = pg.sql("\\pset tuples_only on\nselect md5(prosrc) from pg_proc where proname = 'etappen_stand';").strip()
        assert md5 == 'bf3152e9a378a1d4e41c98965acf738e', md5
        vorher = antworten(pg)
        n_inhalt = sum(1 for v in vorher.values() if v not in ('{}', 'NULL'))
        assert len(vorher) == 4 * 95 and n_inhalt > 250, (len(vorher), n_inhalt)

        # Probe: besteht, ändert nichts
        z = fehlerzeile(pg.paket(lies('tempo_s1_probe.sql'), erwartet_fehler='PROBELAUF bestanden'), 'PROBELAUF bestanden')
        r = bericht(z)
        assert r['abweichungen_etappen_stand'] == 0 and r['paare_kind_einheit'] == 380 and r['merkheft'] == 'verglichen' and r['merkheft_kinder'] == 4, r
        assert r['abweichungen_merkheft'] == [] and r['umgestellt_nachher'] and not r['schon_umgestellt_vorher'], r
        namen = {i['name'] for i in r['indizes_nachher']}
        assert {'aufgabe_einheit_pool_lz_idx', 'versuch_kind_aufgabe_idx'} <= namen and not ({'aufgabe_einheit_pool_lz_idx', 'versuch_kind_aufgabe_idx'} & {i['name'] for i in r['indizes_vorher']}), r
        print('Probe:', json.dumps({k: r[k] for k in ('ms_vorher', 'ms_nachher')}, ensure_ascii=False))
        nach_probe = pg.sql("\\pset tuples_only on\nselect md5(prosrc) from pg_proc where proname = 'etappen_stand';").strip()
        assert nach_probe == md5 and 'versuch_kind_aufgabe_idx' not in pg.sql("select indexname from pg_indexes where schemaname = 'schule';"), 'Probe hat etwas geändert'

        # Vorbedingung: eine andere alte Fassung → Abbruch, nichts geändert
        pg.sql(alt_sql.replace("'gesamt', z.gesamt,", "'gesamt', z.gesamt, 'extra', 1,"))
        for n in ('tempo_s1_probe.sql', 'tempo_s1_einspielen.sql'):
            fehlerzeile(pg.paket(lies(n), erwartet_fehler='Vorbedingung'), 'etappen_stand weicht vom Repo-Stand ab')
        pg.sql(alt_sql)

        # Zusatzfälle vorher speichern
        pg.sql(ZUSATZ)
        vorher2 = antworten(pg)
        assert vorher2 != vorher, 'Zusatzfälle ohne Wirkung'
        pg.sql("update schule.regel set wert = '1' where schluessel = 'anwenden_pflicht';")
        vorher3 = antworten(pg)
        pg.sql("update schule.regel set wert = '0' where schluessel = 'anwenden_pflicht';")

        # Einspielen zweimal
        for lauf in (1, 2):
            out = pg.paket(lies('tempo_s1_einspielen.sql'))
            h = [x for x in out.splitlines() if 'NOTICE:' in x and 'TEMPO-S1 eingespielt' in x]
            assert len(h) == 1, out[-2000:]
            r = bericht(h[0])
            assert r['abweichungen_etappen_stand'] == 0 and r['merkheft'] == 'verglichen' and r['abweichungen_merkheft'] == [], r
            assert r['schon_umgestellt_vorher'] is (lauf == 2), r
            if lauf == 2: assert any('schon umgestellt' in x for x in out.splitlines()), out[-800:]
            print(f'Einspielen {lauf}:', json.dumps({k: r[k] for k in ('ms_vorher', 'ms_nachher')}, ensure_ascii=False))
        assert 'TEMPO-S1' in pg.sql("\\pset tuples_only on\nselect prosrc from pg_proc where proname = 'etappen_stand';")

        # neue Fassung gegen die gespeicherten alten Antworten (jsonb als Text, also auch Zahlentypen und Schlüssel)
        nachher2 = antworten(pg)
        anders = [k for k in vorher2 if vorher2[k] != nachher2.get(k)]
        assert not anders and len(nachher2) == len(vorher2), anders[:5]
        pg.sql("update schule.regel set wert = '1' where schluessel = 'anwenden_pflicht';")
        nachher3 = antworten(pg)
        anders = [k for k in vorher3 if vorher3[k] != nachher3.get(k)]
        assert not anders, anders[:5]

        # Messung nach dem Einspielen (eigene Transaktion): ändert nichts
        z = fehlerzeile(pg.sql(lies('tempo_s1_messen.sql'), erwartet_fehler='MESSUNG'), 'MESSUNG (nichts geändert)')
        m = bericht(z)
        assert m['umgestellt'] and m['merkheft'] == 'verglichen', m
        print('Messung danach:', json.dumps({k: m[k] for k in ('ms_etappen_stand_alle', 'ms_merkheft_summe', 'ms_merkheft_je_kind')}, ensure_ascii=False))
    finally:
        pg.ende()
    print('OK')


if __name__ == '__main__':
    main()
