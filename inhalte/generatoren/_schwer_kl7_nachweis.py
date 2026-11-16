#!/usr/bin/env python3
"""Nachweis für die zehnte Runde: Jede Aufgabe der alten Datei (Stand origin/lernen-app) steht unverändert
in der neuen Datei, und zwar an derselben Stelle; alles außer der Aufgabenliste ist gleich.

Aufruf (im Repository): python3 -I inhalte/generatoren/_schwer_kl7_nachweis.py <thema_schluessel> [<git-ref>]
"""
import collections
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]


def main(schluessel, ref='origin/lernen-app'):
    rel = f'inhalte/themen/{schluessel}.json'
    alt = json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{ref}:{rel}'], capture_output=True, text=True, check=True).stdout)
    neu = json.loads((WURZEL / rel).read_text(encoding='utf-8'))
    fehler = []
    for k in alt:
        if k != 'aufgaben' and alt[k] != neu.get(k): fehler.append(f'Feld „{k}“ geändert')
    if set(neu) - set(alt): fehler.append(f'neue Felder {sorted(set(neu) - set(alt))}')
    A, N = alt['aufgaben'], neu['aufgaben']
    for i, a in enumerate(A):
        if i >= len(N) or N[i] != a: fehler.append(f'alte Aufgabe {i + 1} geändert oder verschoben: {a["f"]["text"][:60]}')
    fehlend = [a for a in A if a not in N]
    zusatz = N[len(A):]
    st3 = collections.Counter(a['l'] for a in N if a['p'] == 'uebung' and a['s'] == 3)
    print(f'{schluessel}: {len(A)} alte Aufgaben, alle unverändert an gleicher Stelle: {"JA" if not fehler else "NEIN"}; '
          f'fehlend: {len(fehlend)}; neu: {len(zusatz)} (alle Übungen: {all(a["p"] == "uebung" for a in zusatz)})')
    for e in neu['inhalt']['etappen']:
        l = e['lernziel']
        z = collections.Counter(a['s'] for a in zusatz if a['l'] == l)
        print(f'  {l:18} neu Stufe 2: {z[2]}, Stufe 3: {z[3]}; Stufe-3-Übungen gesamt: {st3[l]}')
    for f in fehler: print('  FEHLER:', f)
    return 1 if fehler or fehlend else 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
