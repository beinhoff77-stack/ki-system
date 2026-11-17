#!/usr/bin/env python3
"""Nachweis Zwanzigste Runde (stufen-kl7): gegenüber origin/lernen-app ändern sich bei alten Aufgaben nur g und s.

Aufruf: python3 -I inhalte/generatoren/_stufen_nachweis.py <thema> [<stand>]
Geprüft: alles außer „aufgaben“ unverändert; jede alte Aufgabe ist noch da und unterscheidet sich höchstens in g und s;
neue Aufgaben sind Übungen (mit g) oder Knobel-Bordkarten (Pool bonus, g knobel). Die Reihenfolge darf sich innerhalb einer Lernkarte ändern.
"""
import collections
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]


def main(thema, stand='origin/lernen-app'):
    pfad = f'inhalte/themen/{thema}.json'
    alt = json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{stand}:{pfad}'], capture_output=True, check=True, text=True).stdout)
    neu = json.loads((WURZEL / pfad).read_text(encoding='utf-8'))
    k = lambda a: json.dumps({x: v for x, v in a.items() if x not in ('g', 's')}, ensure_ascii=False, sort_keys=True)
    F = []
    if json.dumps({x: v for x, v in alt.items() if x != 'aufgaben'}, sort_keys=True, ensure_ascii=False) != \
       json.dumps({x: v for x, v in neu.items() if x != 'aufgaben'}, sort_keys=True, ensure_ascii=False):
        F.append('Teile außerhalb von „aufgaben“ geändert')
    rest = collections.defaultdict(list)
    for a in neu['aufgaben']: rest[k(a)].append(a)
    z = collections.Counter()
    for a in alt['aufgaben']:
        if not rest[k(a)]: F.append(f'alte Aufgabe fehlt oder ist geändert: {a["l"]} „{a["f"]["text"][:70]}“'); continue
        b = rest[k(a)].pop(0)
        if b['s'] != a['s']: z['umgestuft'] += 1
        if b.get('g') != a.get('g'): z['typ gesetzt'] += 1
    for xs in rest.values():
        for b in xs:
            if b['p'] == 'bonus':
                z['knobel'] += 1
                if b.get('g') != 'knobel': F.append('Bonus ohne Typ knobel')
            elif b['p'] == 'uebung' and b.get('g'): z['neu'] += 1
            else: F.append(f'unerwartete neue Aufgabe: {b["p"]} „{b["f"]["text"][:60]}“')
    print(f'{thema}: alte Aufgaben {len(alt["aufgaben"])} (Typ gesetzt {z["typ gesetzt"]}, umgestuft {z["umgestuft"]}), neue Übungen {z["neu"]}, Knobel {z["knobel"]}')
    if F:
        print('NACHWEIS FEHLGESCHLAGEN:'); [print('  -', f) for f in F[:20]]; return 1
    print('NACHWEIS OK: alte Aufgaben nur in g/s geändert')
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
