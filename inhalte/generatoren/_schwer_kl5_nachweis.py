#!/usr/bin/env python3
"""Nachweis (Zehnte Runde, schwer-kl5): Jede Aufgabe der alten Themen-Datei (Stand Zweig lernen-app) steht unverändert
und an derselben Stelle in der neuen Datei; Lernkarten (inhalt) sind unverändert; neu sind nur angehängte Übungen.

Aufruf: python3 -I inhalte/generatoren/_schwer_kl5_nachweis.py <thema_schluessel> [...]   (aus der Wurzel des Repositorys)
"""
import collections
import json
import subprocess
import sys
from pathlib import Path


def pruefe(thema, ref='origin/lernen-app'):
    pfad = f'inhalte/themen/{thema}.json'
    alt = json.loads(subprocess.run(['git', 'show', f'{ref}:{pfad}'], capture_output=True, text=True, check=True).stdout)
    neu = json.loads(Path(pfad).read_text(encoding='utf-8'))
    fehler = []
    if alt['inhalt'] != neu['inhalt']: fehler.append('inhalt (Lernkarten/Abschnitte/Bewertung) geändert')
    for k in alt:
        if k not in ('aufgaben', 'inhalt') and alt[k] != neu.get(k): fehler.append(f'Feld {k} geändert')
    na = len(alt['aufgaben'])
    for i, a in enumerate(alt['aufgaben']):
        if i >= len(neu['aufgaben']) or neu['aufgaben'][i] != a: fehler.append(f'alte Aufgabe {i + 1} geändert/fehlt'); break
    dazu = neu['aufgaben'][na:]
    if any(a['p'] != 'uebung' for a in dazu): fehler.append('neue Aufgaben außerhalb des Pools uebung')
    z = collections.Counter((a['l'], a['s']) for a in dazu)
    s3 = collections.Counter((a['l'], a['s']) for a in neu['aufgaben'] if a['p'] == 'uebung' and a['s'] == 3)
    print(f'== {thema}: {na} alte Aufgaben unverändert: {"JA" if not fehler else "NEIN"}; neu: {len(dazu)}')
    for e in neu['inhalt']['etappen']:
        l = e['lernziel']
        print(f'   {l:18} neu Stufe 2: {z[(l, 2)]}  Stufe 3: {z[(l, 3)]}  -> Stufe-3-Übungen gesamt: {s3[(l, 3)]}')
    for f in fehler: print('   FEHLER', f)
    return not fehler


if __name__ == '__main__':
    ok = all(pruefe(t) for t in sys.argv[1:])
    sys.exit(0 if ok else 1)
