#!/usr/bin/env python3
"""Nachweis Neunzehnte Runde, Teil A, Klasse 6 (Zweig durchsicht-kl6) gegen origin/lernen-app.

- Kopf, abschnitte, teilfaehigkeiten, bewertung, ziel, merke, quellen: unverändert.
- Lernkarten: Lernziel, Titel, Reihenfolge unverändert; geänderte Karten mit Feldern aufgelistet.
- Aufgaben: wie _befunde_nachweis (Folge-Abgleich): je geänderter Aufgabe Art (stufe = nur s; loesung = o/h/w/c; ersetzt = neue Frage), neue Aufgaben;
  keine Löschung, keine Umsortierung, Lernkarte/Pool je Aufgabe gleich.
- Je Lernkarte mindestens 4 Übungen je Stufe (Auftrag d) – gemeldet, wenn nicht.
Aufruf: python3 -I inhalte/generatoren/_durchsicht_kl6_nachweis.py <thema> [stand]
"""
import collections
import difflib
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]


def main(thema, stand='origin/lernen-app'):
    pfad = f'inhalte/themen/{thema}.json'
    alt = json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{stand}:{pfad}'], capture_output=True, check=True, text=True).stdout)
    neu = json.loads((WURZEL / pfad).read_text(encoding='utf-8'))
    k = lambda a: json.dumps(a, ensure_ascii=False, sort_keys=True)
    F = []
    if k({x: v for x, v in alt.items() if x not in ('aufgaben', 'inhalt')}) != k({x: v for x, v in neu.items() if x not in ('aufgaben', 'inhalt')}):
        F.append('Kopf geändert')
    if k({x: v for x, v in alt['inhalt'].items() if x != 'etappen'}) != k({x: v for x, v in neu['inhalt'].items() if x != 'etappen'}):
        F.append('inhalt außer etappen geändert')
    ea, en = alt['inhalt']['etappen'], neu['inhalt']['etappen']
    if [(e['lernziel'], e['titel']) for e in ea] != [(e['lernziel'], e['titel']) for e in en]:
        F.append('Lernziele/Titel/Reihenfolge geändert')
    geaendert = {}
    for a, b in zip(ea, en):
        d = sorted(x for x in set(a) | set(b) if a.get(x) != b.get(x))
        if d: geaendert[a['lernziel']] = d
    A, N = alt['aufgaben'], neu['aufgaben']
    sm = difflib.SequenceMatcher(a=[k(a) for a in A], b=[k(a) for a in N], autojunk=False)
    z = collections.Counter()
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal': continue
        if tag == 'replace' and i2 - i1 == j2 - j1:
            for a, b in zip(A[i1:i2], N[j1:j2]):
                if (a['l'], a['p'], a['t']) != (b['l'], b['p'], b['t']): F.append(f'Lernkarte/Pool geändert: {a["f"]["text"][:50]}')
                if a['f'] != b['f'] or a.get('a') != b.get('a'): z['ersetzt'] += 1
                else:
                    fe = sorted(x for x in set(a) | set(b) if a.get(x) != b.get(x))
                    if fe == ['s']: z['umgestuft'] += 1
                    elif set(fe) <= {'o', 'h', 'w', 'c', 's'}: z['berichtigt'] += 1
                    else: F.append(f'unerlaubte Felder {fe}: {a["f"]["text"][:50]}')
        elif tag == 'insert':
            for b in N[j1:j2]:
                z['neu'] += 1
                if b['p'] != 'uebung': F.append('neue Aufgabe außerhalb uebung')
        else:
            F.append(f'{tag} {i1}-{i2} → {j1}-{j2}: Löschung oder Umsortierung')
    st = collections.Counter((a['l'], a['s']) for a in N if a['p'] == 'uebung')
    unter = [f'{e["lernziel"]}/S{s}={st[(e["lernziel"], s)]}' for e in en for s in (1, 2, 3) if st[(e['lernziel'], s)] < 4]
    print(f'{thema}: umgestuft {z["umgestuft"]}, berichtigt {z["berichtigt"]}, ersetzt {z["ersetzt"]}, neu {z["neu"]}; Lernkarten geändert: '
          + (', '.join(f'{l} ({"/".join(v)})' for l, v in geaendert.items()) or 'keine'))
    print('  Übungen je Stufe (S1/S2/S3): ' + ', '.join(f'{e["lernziel"]} {st[(e["lernziel"],1)]}/{st[(e["lernziel"],2)]}/{st[(e["lernziel"],3)]}' for e in en))
    if unter: print('  WENIGER ALS 4: ' + ', '.join(unter))
    print('NACHWEIS OK' if not F else 'FEHLER:\n  ' + '\n  '.join(F))
    return 1 if F else 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
