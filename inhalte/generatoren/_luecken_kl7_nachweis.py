#!/usr/bin/env python3
"""Nachweis (luecken-kl7): Gegenüber origin/lernen-app wurde nur Neues ergänzt.

Aufruf: python3 -I inhalte/generatoren/_luecken_kl7_nachweis.py <thema_schluessel> [<basis-ref>]
Geprüft wird:
- alle bisherigen Lernkarten sind Zeichen für Zeichen gleich und stehen in derselben Reihenfolge,
- alle bisherigen Aufgaben sind Zeichen für Zeichen gleich, in derselben Reihenfolge und vorn (neue nur hinten),
- abschnitte, teilfaehigkeiten und bewertung unterscheiden sich nur durch die neuen Lernziele,
- ziel, merke und alle übrigen Felder sind gleich; quellen und offen nur ergänzt (alte Einträge gleich),
- jede neue Aufgabe gehört zu einer neuen Lernkarte.
"""
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]


def ohne(liste, neu):
    return [x for x in liste if x not in neu]


def main(schluessel, basis='origin/lernen-app'):
    pfad = f'inhalte/themen/{schluessel}.json'
    alt = json.loads(subprocess.run(['git', 'show', f'{basis}:{pfad}'], cwd=WURZEL, capture_output=True, text=True, check=True).stdout)
    neu = json.loads((WURZEL / pfad).read_text(encoding='utf-8'))
    s = lambda x: json.dumps(x, ensure_ascii=False, sort_keys=True)
    F = []
    lz_alt = [e['lernziel'] for e in alt['inhalt']['etappen']]
    lz_neu = [e['lernziel'] for e in neu['inhalt']['etappen']]
    dazu = [l for l in lz_neu if l not in lz_alt]
    if ohne(lz_neu, dazu) != lz_alt: F.append('Lernkarten fehlen oder sind umsortiert')
    alte_karten = [e for e in neu['inhalt']['etappen'] if e['lernziel'] not in dazu]
    for a, b in zip(alt['inhalt']['etappen'], alte_karten):
        if s(a) != s(b): F.append(f'Lernkarte {a["lernziel"]} geändert')
    for k in set(alt) | set(neu):
        if k in ('inhalt', 'aufgaben', 'offen'): continue
        if s(alt.get(k)) != s(neu.get(k)): F.append(f'Feld {k} geändert')
    oa, on = alt.get('offen', []), neu.get('offen', [])
    if on[:len(oa)] != oa: F.append('alte Einträge unter „offen“ geändert')
    for k in set(alt['inhalt']) | set(neu['inhalt']):
        a, b = alt['inhalt'].get(k), neu['inhalt'].get(k)
        if k == 'etappen': continue
        if k == 'abschnitte':
            b = [{**x, 'lernziele': ohne(x['lernziele'], dazu)} for x in b]
        elif k == 'teilfaehigkeiten':
            b = [x for x in b if not set(x['lernziele']) <= set(dazu)]
        elif k == 'bewertung':
            b = {kk: (ohne(v, dazu) if isinstance(v, list) else v) for kk, v in b.items()}
        elif k == 'quellen':
            b = {kk: v for kk, v in (b or {}).items() if kk in (a or {})}
        if s(a) != s(b): F.append(f'inhalt.{k} geändert')
    n = len(alt['aufgaben'])
    for i, (a, b) in enumerate(zip(alt['aufgaben'], neu['aufgaben'][:n])):
        if s(a) != s(b): F.append(f'Aufgabe {i + 1} geändert: {a["f"]["text"][:60]}')
    if len(neu['aufgaben']) < n: F.append('Aufgaben fehlen')
    fremd = [a for a in neu['aufgaben'][n:] if a['l'] not in dazu]
    if fremd: F.append(f'{len(fremd)} neue Aufgaben gehören zu alten Lernkarten')
    # Textvergleich: jede alte Aufgabe steht wörtlich (gleiche Zeilen) in der neuen Datei
    roh_neu = (WURZEL / pfad).read_text(encoding='utf-8')
    for a in alt['aufgaben']:
        if json.dumps(a, ensure_ascii=False, indent=1).replace('\n', '\n  ') not in roh_neu: F.append(f'Aufgabe nicht wörtlich gefunden: {a["f"]["text"][:60]}'); break
    print(f'{schluessel}: {len(lz_alt)} alte Karten unverändert, neu: {", ".join(dazu) or "–"}; '
          f'{n} alte Aufgaben unverändert vorn, {len(neu["aufgaben"]) - n} neue hinten')
    if F:
        print('NACHWEIS FEHLGESCHLAGEN:'); [print('  -', f) for f in F]; return 1
    print('NACHWEIS OK: nur Neues ergänzt')
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
