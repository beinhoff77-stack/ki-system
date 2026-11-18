#!/usr/bin/env python3
"""Nachweis Korrektur neuer Aufgaben Kl. 7 (stufen-kl7): gegenüber origin/lernen-app ändern sich nur neue Aufgaben.

Aufruf: python3 -I inhalte/generatoren/_pruefung_kl7_nachweis.py <thema> [<stand>] [<vorher>]
„neu“ = Pool uebung oder bonus und Fragetext gab es im Stand <vorher> (Standard 4eda8cb, vor der Zwanzigsten Runde) in keiner Themendatei.
Geprüft: alles außerhalb von „aufgaben“ unverändert; jede alte Aufgabe ist Zeichen für Zeichen noch da (Reihenfolge darf sich
innerhalb der Lernkarte ändern); geänderte Aufgaben ersetzen nur neue Aufgaben derselben Lernkarte mit gleichem Pool, Typ g,
Stufe s und Antwortart y; die Zahl der Aufgaben je Lernkarte und Pool bleibt gleich.
"""
import collections
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]


def git(*a):
    return subprocess.run(['git', '-C', str(WURZEL), *a], capture_output=True, check=True, text=True).stdout


def main(thema, stand='origin/lernen-app', vorher='4eda8cb'):
    pfad = f'inhalte/themen/{thema}.json'
    alt = json.loads(git('show', f'{stand}:{pfad}'))
    neu = json.loads((WURZEL / pfad).read_text(encoding='utf-8'))
    texte_vorher = set()
    for f in git('ls-tree', '--name-only', vorher, 'inhalte/themen/').split():
        if f.endswith('.json'):
            texte_vorher |= {a['f']['text'] for a in json.loads(git('show', f'{vorher}:{f}')).get('aufgaben', [])}
    ist_neu = lambda a: a['p'] in ('uebung', 'bonus') and a['f']['text'] not in texte_vorher
    k = lambda a: json.dumps(a, ensure_ascii=False, sort_keys=True)
    F = []
    if k({x: v for x, v in alt.items() if x != 'aufgaben'}) != k({x: v for x, v in neu.items() if x != 'aufgaben'}):
        F.append('Teile außerhalb von „aufgaben“ geändert')
    rest = collections.Counter(k(a) for a in neu['aufgaben'])
    weg = []
    for a in alt['aufgaben']:
        if rest[k(a)]: rest[k(a)] -= 1
        elif ist_neu(a): weg.append(a)
        else: F.append(f'alte Aufgabe geändert oder entfernt: {a["l"]} „{a["f"]["text"][:70]}“')
    dazu = [json.loads(x) for x, n in rest.items() for _ in range(n)]
    sig = lambda a: (a['l'], a['p'], a.get('g'), a['s'], a['y'])
    if collections.Counter(map(sig, weg)) != collections.Counter(map(sig, dazu)):
        F.append(f'geänderte Aufgaben passen nicht (l, p, g, s, y): weg {sorted(map(sig, weg))} / dazu {sorted(map(sig, dazu))}')
    for a in dazu:
        if a['f']['text'] in texte_vorher: F.append(f'geänderte Aufgabe hat Text einer alten Aufgabe: „{a["f"]["text"][:60]}“')
    if F:
        print('NACHWEIS FEHLER:\n  ' + '\n  '.join(F)); sys.exit(1)
    print(f'NACHWEIS OK: {thema} – alte Aufgaben unverändert, {len(dazu)} neue Aufgaben geändert (l, p, g, s, y gleich)')


if __name__ == '__main__':
    main(*sys.argv[1:])
