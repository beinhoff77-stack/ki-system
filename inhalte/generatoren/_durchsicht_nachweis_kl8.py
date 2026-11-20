#!/usr/bin/env python3
"""Nachweis Neunzehnte Runde, Teil A: Gegenüber dem Stand (Standard origin/lernen-app) ist nur das Gemeldete geändert.

Aufruf: python3 -I inhalte/generatoren/_durchsicht_nachweis.py <thema_schluessel> [--stand REF]
- Alles außerhalb von inhalt.etappen und aufgaben gleich; Lernkarten: gleiche lernziel/titel/Reihenfolge, geänderte Karten werden genannt.
- Aufgaben: die ersten N (N = alte Anzahl) stehen an derselben Stelle; jede ist gleich, nur umgestuft (s), nur berichtigt (o/h/w/c)
  oder ersetzt (gleiche Lernkarte und gleicher Pool, neue Frage). Danach folgen nur neue Übungen.
"""
import argparse
import collections
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]
k = lambda x: json.dumps(x, ensure_ascii=False, sort_keys=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('thema')
    ap.add_argument('--stand', default='origin/lernen-app')
    arg = ap.parse_args()
    pfad = f'inhalte/themen/{arg.thema}.json'
    alt = json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{arg.stand}:{pfad}'], capture_output=True, check=True, text=True).stdout)
    neu = json.loads((WURZEL / pfad).read_text(encoding='utf-8'))
    F = []
    for x in set(alt) | set(neu):
        if x not in ('inhalt', 'aufgaben') and k(alt.get(x)) != k(neu.get(x)): F.append(f'Feld {x} geändert')
    for x in set(alt['inhalt']) | set(neu['inhalt']):
        if x != 'etappen' and k(alt['inhalt'].get(x)) != k(neu['inhalt'].get(x)): F.append(f'inhalt.{x} geändert')
    ea, en = alt['inhalt']['etappen'], neu['inhalt']['etappen']
    if [(e['lernziel'], e['titel']) for e in ea] != [(e['lernziel'], e['titel']) for e in en]: F.append('Lernkarten: Schlüssel, Titel oder Reihenfolge geändert')
    karten = [b['lernziel'] for a, b in zip(ea, en) if k(a) != k(b)]
    A, N = alt['aufgaben'], neu['aufgaben']
    z = collections.Counter()
    ersetzt = []
    for a, b in zip(A, N[:len(A)]):
        if k(a) == k(b): z['gleich'] += 1; continue
        if (a['l'], a['t'], a['p']) != (b['l'], b['t'], b['p']): F.append(f'Lernkarte/Pool geändert: {a["f"]["text"][:60]}'); continue
        diff = {x for x in set(a) | set(b) if k(a.get(x)) != k(b.get(x))}
        if diff == {'s'}: z['umgestuft'] += 1
        elif diff <= {'o', 'h', 'w', 'c', 's'} and 'f' not in diff: z['berichtigt'] += 1
        else:
            z['ersetzt'] += 1
            ersetzt.append(a['f']['text'])
            if a['f']['text'] == b['f']['text']: F.append(f'„ersetzt“ mit gleichem Fragetext: {a["f"]["text"][:60]}')
    for b in N[len(A):]:
        z['neu'] += 1
        if b['p'] != 'uebung': F.append('neue Aufgabe außerhalb des Übungspools')
    st = collections.Counter((a['l'], a['s']) for a in N if a['p'] == 'uebung')
    for e in en:
        for s in (1, 2, 3):
            if st[(e['lernziel'], s)] < 3: F.append(f'{e["lernziel"]}: nur {st[(e["lernziel"], s)]} Übungen auf Stufe {s}')
    print(f'{arg.thema}: {dict(z)}; Lernkarten geändert: {karten}')
    for t in ersetzt: print(f'  ersetzt: „{t}“')
    print('NACHWEIS OK' if not F else 'NACHWEIS FEHLER:\n  ' + '\n  '.join(F))
    sys.exit(1 if F else 0)


if __name__ == '__main__':
    main()
