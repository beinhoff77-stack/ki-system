#!/usr/bin/env python3
"""Nachweis Achtzehnte Runde, Teil B: Gegenüber dem Stand (Standard origin/lernen-app) kam nur Neues dazu.

Aufruf: python3 -I inhalte/generatoren/_luecken_nachweis.py <thema_schluessel> [--erweitert lz1,lz2] [--stand REF]
Prüft:
- alle Felder außerhalb von inhalt/aufgaben gleich; inhalt.ziel, merke, quellen gleich;
- jede alte Lernkarte Zeichen für Zeichen gleich – außer den mit --erweitert genannten; dort ist nur genau ein Schritt dazugekommen;
- teilfaehigkeiten, abschnitte, bewertung: alte Einträge gleich und in gleicher Reihenfolge, nur neue Lernziele dazu;
- alle alten Aufgaben unverändert und in derselben Reihenfolge vorne; neue Aufgaben gehören nur zu neuen oder erweiterten Karten.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]
k = lambda x: json.dumps(x, ensure_ascii=False, sort_keys=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('thema')
    ap.add_argument('--erweitert', default='')
    ap.add_argument('--stand', default='origin/lernen-app')
    arg = ap.parse_args()
    pfad = f'inhalte/themen/{arg.thema}.json'
    alt = json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{arg.stand}:{pfad}'], capture_output=True, check=True, text=True).stdout)
    neu = json.loads((WURZEL / pfad).read_text(encoding='utf-8'))
    erw = [x for x in arg.erweitert.split(',') if x]
    fehler = []
    F = fehler.append
    for x in set(alt) | set(neu):
        if x not in ('inhalt', 'aufgaben') and k(alt.get(x)) != k(neu.get(x)): F(f'Feld {x} geändert')
    ia, iN = alt['inhalt'], neu['inhalt']
    for x in set(ia) | set(iN):
        if x not in ('etappen', 'teilfaehigkeiten', 'abschnitte', 'bewertung') and k(ia.get(x)) != k(iN.get(x)): F(f'inhalt.{x} geändert')
    alt_lz = [e['lernziel'] for e in ia['etappen']]
    neu_lz = [e['lernziel'] for e in iN['etappen'] if e['lernziel'] not in alt_lz]
    rest = [e for e in iN['etappen'] if e['lernziel'] in alt_lz]
    if [e['lernziel'] for e in rest] != alt_lz: F('Reihenfolge der alten Lernkarten geändert')
    for ea, en in zip(ia['etappen'], rest):
        if k(ea) == k(en): continue
        if ea['lernziel'] not in erw: F(f'Lernkarte {ea["lernziel"]} geändert'); continue
        sa, sn = ea['schritte'], en['schritte']
        ohne = {x: v for x, v in en.items() if x != 'schritte'}
        if k(ohne) != k({x: v for x, v in ea.items() if x != 'schritte'}): F(f'Lernkarte {ea["lernziel"]}: mehr als die Schritte geändert')
        if len(sn) != len(sa) + 1 or not any(k(sn[:i] + sn[i + 1:]) == k(sa) for i in range(len(sn))):
            F(f'Lernkarte {ea["lernziel"]}: nicht genau ein Schritt eingefügt')
    tn = [t for t in iN['teilfaehigkeiten'] if t['k'] not in neu_lz]
    if k(tn) != k(ia['teilfaehigkeiten']): F('teilfaehigkeiten: alte Einträge geändert')
    if [a['titel'] for a in ia['abschnitte']] != [a['titel'] for a in iN['abschnitte']]: F('abschnitte: Titel geändert')
    for aa, an in zip(ia['abschnitte'], iN['abschnitte']):
        if [x for x in an['lernziele'] if x not in neu_lz] != aa['lernziele']: F(f'abschnitt {aa["titel"]}: alte Lernziele geändert')
    ba, bn = ia['bewertung'], iN['bewertung']
    for x in set(ba) | set(bn):
        va, vn = ba.get(x), bn.get(x)
        if isinstance(va, list): vn = [y for y in (vn or []) if y not in neu_lz]
        if k(va) != k(vn): F(f'bewertung.{x}: alte Einträge geändert')
    A, N = alt['aufgaben'], neu['aufgaben']
    if [k(a) for a in N[:len(A)]] != [k(a) for a in A]: F('alte Aufgaben nicht unverändert vorne')
    dazu = N[len(A):]
    for a in dazu:
        if a['l'] not in neu_lz + erw: F(f'neue Aufgabe zu alter, nicht erweiterter Karte: {a["l"]}')
    from collections import Counter
    z = Counter((a['l'], a['p'], a['s']) for a in dazu)
    print(f'{arg.thema}: alte Karten {len(alt_lz)}, neue Karten {neu_lz}, erweitert {erw}; alte Aufgaben {len(A)} unverändert vorne, neue {len(dazu)}')
    for lz in neu_lz + erw:
        print(f'  {lz}: ' + ', '.join(f'{p} s{s}: {n}' for (l, p, s), n in sorted(z.items()) if l == lz))
    print('NACHWEIS OK' if not fehler else 'NACHWEIS FEHLER:\n  ' + '\n  '.join(fehler))
    sys.exit(1 if fehler else 0)


if __name__ == '__main__':
    main()
