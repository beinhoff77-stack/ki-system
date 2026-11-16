#!/usr/bin/env python3
"""Unverändert-Nachweis (Zehnte Runde, Zweig schwer-kl8).

Aufruf: python3 -I inhalte/generatoren/_unveraendert_kl8.py <thema_schluessel> [<vergleichsstand>]
Vergleicht inhalte/themen/<thema>.json mit dem Stand auf dem Zweig lernen-app (Standard: origin/lernen-app):
- jede alte Aufgabe steht Zeichen für Zeichen (als JSON) unverändert in der neuen Datei, in derselben Reihenfolge,
- alles außer "aufgaben" (Lernkarten, Zeichnungen, Texte, offen) ist gleich,
- neu sind nur Übungen; Zählung neuer Übungen und Stufe-3-Übungen je Lernkarte.
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
    k = lambda a: json.dumps(a, ensure_ascii=False, sort_keys=True)
    ok = True
    ra, rn = {x: v for x, v in alt.items() if x != 'aufgaben'}, {x: v for x, v in neu.items() if x != 'aufgaben'}
    if k(ra) != k(rn):
        ok = False; print('FEHLER: Teile außerhalb von "aufgaben" geändert:', [x for x in set(ra) | set(rn) if k(ra.get(x)) != k(rn.get(x))])
    nk = [k(a) for a in neu['aufgaben']]
    i = 0
    fehlt = 0
    for a in alt['aufgaben']:
        ka = k(a)
        while i < len(nk) and nk[i] != ka: i += 1
        if i == len(nk): fehlt += 1; i = 0; continue
        i += 1
    if fehlt: ok = False; print(f'FEHLER: {fehlt} alte Aufgaben fehlen oder sind geändert/umsortiert')
    altset = collections.Counter(k(a) for a in alt['aufgaben'])
    rest = collections.Counter(nk) - altset
    if sum((altset - collections.Counter(nk)).values()): ok = False
    zus = [json.loads(x) for x in rest.elements()]
    if any(a['p'] != 'uebung' for a in zus): ok = False; print('FEHLER: neue Aufgaben außerhalb des Pools uebung')
    z = collections.Counter((a['l'], a['s']) for a in zus)
    s3 = collections.Counter(a['l'] for a in neu['aufgaben'] if a['p'] == 'uebung' and a['s'] == 3)
    print(f'{thema}: alt {len(alt["aufgaben"])}, neu {len(neu["aufgaben"])}, dazu {len(zus)} – alle alten Aufgaben unverändert: {"JA" if ok else "NEIN"}')
    for e in neu['inhalt']['etappen']:
        l = e['lernziel']
        print(f'  {l:16} neu S3 {z[(l, 3)]}  neu S2 {z[(l, 2)]}  Stufe-3-Übungen gesamt {s3[l]}' + ('' if z[(l, 3)] >= 4 and z[(l, 2)] >= 2 and s3[l] >= 6 else '  <-- zu wenig'))
        if not (z[(l, 3)] >= 4 and z[(l, 2)] >= 2 and s3[l] >= 6): ok = False
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
