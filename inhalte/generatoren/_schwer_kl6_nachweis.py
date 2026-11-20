#!/usr/bin/env python3
"""Nachweis für die Zehnte Runde (schwer-kl6): Alle Aufgaben der alten Themen-Datei (Stand Zweig lernen-app)
stehen unverändert und in derselben Reihenfolge am Anfang der neuen Datei; alles außer den Aufgaben ist gleich;
neu sind nur Übungen. Gibt je Lernkarte die Zahl der neuen Übungen je Stufe aus.

Aufruf: python3 -I inhalte/generatoren/_schwer_kl6_nachweis.py <thema_schluessel> [<git-stand>]
        (git-stand Standard: origin/lernen-app)
"""
import collections
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent


def main(thema, stand='origin/lernen-app'):
    pfad = f'inhalte/themen/{thema}.json'
    alt = json.loads(subprocess.run(['git', 'show', f'{stand}:{pfad}'], cwd=WURZEL, capture_output=True, check=True, text=True).stdout)
    neu = json.loads((WURZEL / pfad).read_text(encoding='utf-8'))
    fehler = []
    if {k: v for k, v in alt.items() if k != 'aufgaben'} != {k: v for k, v in neu.items() if k != 'aufgaben'}:
        fehler.append('Inhalt (Lernkarten, Kopf) hat sich geändert')
    na, nn = len(alt['aufgaben']), len(neu['aufgaben'])
    for i, a in enumerate(alt['aufgaben']):
        if i >= nn or neu['aufgaben'][i] != a:
            fehler.append(f'alte Aufgabe {i + 1} geändert oder fehlt: {a["f"]["text"][:60]}')
    # zusätzlich: jede alte Aufgabe steht irgendwo unverändert in der neuen Datei (unabhängig von der Position)
    neu_menge = {json.dumps(a, sort_keys=True, ensure_ascii=False) for a in neu['aufgaben']}
    fehlt = [a for a in alt['aufgaben'] if json.dumps(a, sort_keys=True, ensure_ascii=False) not in neu_menge]
    if fehlt:
        fehler.append(f'{len(fehlt)} alte Aufgaben nicht wörtlich in der neuen Datei')
    dazu = neu['aufgaben'][na:]
    if any(a['p'] != 'uebung' for a in dazu):
        fehler.append('neue Aufgaben außerhalb des Pools uebung')
    z = collections.Counter((a['l'], a['s']) for a in dazu)
    s3 = collections.Counter((a['l'], a['s']) for a in neu['aufgaben'] if a['p'] == 'uebung')
    print(f'{thema}: alt {na} Aufgaben, neu {nn} Aufgaben, dazu {len(dazu)}')
    for e in neu['inhalt']['etappen']:
        l = e['lernziel']
        print(f'  {l:28s} neu: S1 {z[(l, 1)]}  S2 {z[(l, 2)]}  S3 {z[(l, 3)]}   | Übungen Stufe 3 gesamt: {s3[(l, 3)]}')
    print('UNVERÄNDERT: JA' if not fehler else 'FEHLER:\n  ' + '\n  '.join(fehler))
    return 1 if fehler else 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
