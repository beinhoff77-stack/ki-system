"""Test für tools/rollend_sql.py: jede Runde einzeln und alle zusammen.

Prüft: Zahl der Aufgaben und Einheiten je Runde, Eindeutigkeit der Kennungen, Eindeutigkeit der Reihenfolge-Nummern je Einheit
(innerhalb eines Pakets, über alle einzeln erzeugten Pakete hinweg und gegen den Bestand max_r), Gleichheit von „einzeln“ und „alle zusammen“,
--ohne, Fehlerfälle (unbekannte Kennung, unbekannte Runde ohne Aufgaben). Altbestand: --mit-bedingung = 633 Aufgaben, 22 Einheiten.
Aufruf: python3 -I tools/tests/rollend_sql_test.py   (endet mit OK)
"""
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
TOOL = WURZEL / 'tools' / 'rollend_sql.py'
PLAN = json.loads((WURZEL / 'inhalte/plan/rollend-einheiten.json').read_text(encoding='utf-8'))
ZEILE = re.compile(r"\((\d+), '([\w.]+)', (\d+), (\d+), \$auf\$(.*?)\$auf\$::jsonb\)", re.S)
SOLL = {1: 76, 2: 116, 3: 127, 4: 314, 5: 174, 7: 183, 8: 156, 10: 108}   # mit --mit-bedingung (Runden 1-4), Stand 27.11.2026


def lauf(*args):
    p = subprocess.run([sys.executable, '-I', str(TOOL), *args], capture_output=True, text=True, cwd=str(WURZEL))
    return p.returncode, p.stdout, p.stderr


def paket(*args):
    rc, out, err = lauf('--sql', *args)
    assert rc == 0, f'{args}: rc={rc}\n{err}'
    teile = ZEILE.findall(out)
    assert teile, f'{args}: keine Einheiten im SQL'
    pak = {}
    for eid, schl, max_r, soll, js in teile:
        rows = json.loads(js)
        assert int(soll) == len(rows), (schl, soll, len(rows))
        assert PLAN['einheiten'][schl]['id'] == int(eid) and PLAN['einheiten'][schl]['max_r'] == int(max_r), schl
        assert schl not in pak
        pak[schl] = rows
    return pak, out


def pruefe_paket(pak, name):
    for schl, rows in pak.items():
        rs = [r['r'] for r in rows]
        assert len(rs) == len(set(rs)), f'{name} {schl}: Reihenfolge-Nummern doppelt'
        assert min(rs) > PLAN['einheiten'][schl]['max_r'], f'{name} {schl}: Nummer nicht hinter max_r'
        assert rs == sorted(rs), f'{name} {schl}: Nummern nicht aufsteigend'
        for r in rows:
            assert r['form'] in ('lueckenweg', 'fehler_detektiv', 'verfahren_waehlen', 'zwei_wege', 'umkehren', 'bruecke', 'anwenden', 'viele_antworten'), r
            assert r['zaehlt'] in ('ja', 'nein'), r
            assert r['p'] == 'uebung'


def main():
    # Altbestand wie bisher (Aufruf ohne --runden)
    rc, out, err = lauf('--mit-bedingung')
    assert rc == 0, err
    assert re.search(r'^OK – 633 Aufgaben für 22 Einheiten; Typ „bedingung“ eingeschlossen', out, re.M), out[-600:]
    pak_alt, _ = paket('--mit-bedingung')
    assert sum(len(v) for v in pak_alt.values()) == 633 and len(pak_alt) == 22
    pak_alt2, _ = paket('--mit-bedingung', '--runden', '1,2,3,4')
    assert pak_alt == pak_alt2, 'Standard ist nicht --runden 1,2,3,4'

    # Jede Runde einzeln; Summe der Altrunden = Altbestand
    einzeln = {}
    for r in SOLL:
        pak, _ = paket('--mit-bedingung', '--runden', str(r))
        pruefe_paket(pak, f'Runde {r}')
        n = sum(len(v) for v in pak.values())
        assert n == SOLL[r], f'Runde {r}: {n} statt {SOLL[r]}'
        einzeln[r] = pak
    assert sum(SOLL[r] for r in (1, 2, 3, 4)) == 633

    # Alle zusammen = Vereinigung der einzelnen Pakete; Nummern je Einheit über alle Pakete eindeutig
    pak_alle, _ = paket('--mit-bedingung', '--runden', 'alle')
    pruefe_paket(pak_alle, 'alle')
    assert sum(len(v) for v in pak_alle.values()) == sum(SOLL.values())
    verein = {}
    for r, pak in einzeln.items():
        for schl, rows in pak.items():
            verein.setdefault(schl, []).extend(rows)
    assert set(verein) == set(pak_alle)
    for schl, rows in verein.items():
        rs = [x['r'] for x in rows]
        assert len(rs) == len(set(rs)), f'{schl}: Nummern der einzelnen Pakete überschneiden sich'
        assert sorted(json.dumps(x, sort_keys=True) for x in rows) == sorted(json.dumps(x, sort_keys=True) for x in pak_alle[schl]), \
            f'{schl}: einzeln und zusammen verschieden (Nummern müssen unabhängig von der Auswahl sein)'
    # Altrunden: Nummern lückenlos max_r+1 .. max_r+n bei vollständiger Auswahl
    for schl, rows in pak_alt.items():
        mr = PLAN['einheiten'][schl]['max_r']
        assert sorted(x['r'] for x in rows) == list(range(mr + 1, mr + 1 + len(rows))), schl

    # Kennungen eindeutig (über alle Runden) und Zahl stimmt
    sys.path.insert(0, str(WURZEL / 'tools'))
    import rollend_sql
    plan, je, fehler, zeichn, spaeter, ohne, folge, stat = rollend_sql.sammeln(True, tuple(SOLL))
    assert not fehler and not folge and not ohne, (fehler[:5], folge, ohne[:3])
    ks = [k for v in je.values() for k, _ in v]
    assert len(ks) == len(set(ks)) == sum(SOLL.values()), (len(ks), len(set(ks)))
    for r in SOLL:
        assert stat[r]['n'] == SOLL[r] and not stat[r]['t_abw'], (r, stat[r]['n'], stat[r]['t_abw'][:5])
        assert sum(stat[r]['form'].values()) == SOLL[r] == sum(stat[r]['zaehlt'].values())
    assert len(set(Counter(k.split('-')[0] for k in ks))) >= 7

    # --ohne nimmt heraus, verschiebt aber keine Nummern
    k0 = next(k for k, _ in je['zahlen.ganz'])
    pak_o, _ = paket('--runden', '5', '--ohne', k0)
    assert sum(len(v) for v in pak_o.values()) == SOLL[5] - 1
    rest = {x['r'] for x in pak_o['zahlen.ganz']}
    assert rest < {x['r'] for x in einzeln[5]['zahlen.ganz']} and len(rest) == len(einzeln[5]['zahlen.ganz']) - 1

    # Fehlerfälle
    rc, _, err = lauf('--runden', '5', '--ohne', 'GIBT-ES-NICHT')
    assert rc == 1 and 'GIBT-ES-NICHT' in err, err
    rc, _, err = lauf('--runden', 'x')
    assert rc != 0
    rc, _, err = lauf('--sql', '--runden', '99')
    assert rc == 1, 'leere Auswahl muss abbrechen'
    # SQL-Rahmen
    _, sql = paket('--runden', '8')
    assert 'reihenfolge <= e.max_r' in sql and 'schon belegt' in sql and sql.count('$auf$') == 2 * len(einzeln[8])
    print('OK')


if __name__ == '__main__':
    main()
