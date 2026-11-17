#!/usr/bin/env python3
"""Nachweis Achtzehnte Runde, Teil B, Klasse 6 (Zweig luecken-kl6): Gegen den Stand origin/lernen-app kam nur Neues dazu.

- Alle alten Aufgaben stehen wörtlich und in derselben Reihenfolge am Anfang; neue Aufgaben gehören nur zu neuen Lernkarten
  oder zu den ausdrücklich erweiterten Lernkarten.
- Alte Lernkarten sind unverändert (Reihenfolge erhalten). Erweiterte Lernkarten: alle alten Felder gleich, nur Schritte eingefügt
  (alte Schritte in alter Reihenfolge vorhanden) und Wörter angehängt.
- abschnitte, teilfaehigkeiten, bewertung: ohne die neuen Lernziele genau wie vorher. Alles andere in der Datei unverändert.

Aufruf: python3 -I inhalte/generatoren/_luecken_kl6_nachweis.py <thema> [erweiterte,lernkarten] [git-stand]
"""
import collections
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent


def teilfolge(alt, neu):
    it = iter(neu)
    return all(any(x == y for y in it) for x in alt)


def main(thema, erweitert='', stand='origin/lernen-app'):
    erw = {x for x in erweitert.split(',') if x}
    pfad = f'inhalte/themen/{thema}.json'
    alt = json.loads(subprocess.run(['git', 'show', f'{stand}:{pfad}'], cwd=WURZEL, capture_output=True, check=True, text=True).stdout)
    neu = json.loads((WURZEL / pfad).read_text(encoding='utf-8'))
    F = []
    if {k: v for k, v in alt.items() if k not in ('inhalt', 'aufgaben')} != {k: v for k, v in neu.items() if k not in ('inhalt', 'aufgaben')}:
        F.append('Kopf der Datei (außer inhalt/aufgaben) geändert')
    ai, ni = alt['inhalt'], neu['inhalt']
    rest = ('etappen', 'abschnitte', 'teilfaehigkeiten', 'bewertung')
    if {k: v for k, v in ai.items() if k not in rest} != {k: v for k, v in ni.items() if k not in rest}:
        F.append('inhalt (ziel, merke, quellen …) geändert')
    alt_lz = [e['lernziel'] for e in ai['etappen']]
    neu_lz = [e['lernziel'] for e in ni['etappen']]
    dazu_lz = [l for l in neu_lz if l not in alt_lz]
    if [l for l in neu_lz if l in alt_lz] != alt_lz:
        F.append('alte Lernkarten fehlen oder sind umsortiert')
    for e in ai['etappen']:
        n = next((x for x in ni['etappen'] if x['lernziel'] == e['lernziel']), None)
        if n is None: continue
        if e['lernziel'] in erw:
            if {k: v for k, v in e.items() if k not in ('schritte', 'woerter')} != {k: v for k, v in n.items() if k not in ('schritte', 'woerter')}:
                F.append(f'erweiterte Karte {e["lernziel"]}: andere Felder als schritte/woerter geändert')
            if not teilfolge(e['schritte'], n['schritte']): F.append(f'erweiterte Karte {e["lernziel"]}: alte Schritte verändert')
            if n.get('woerter', [])[:len(e.get('woerter', []))] != e.get('woerter', []): F.append(f'erweiterte Karte {e["lernziel"]}: alte Wörter verändert')
        elif n != e:
            F.append(f'Karte {e["lernziel"]} verändert')
    ohne = lambda ls: [x for x in ls if x not in dazu_lz]
    if [(a['titel'], a['lernziele']) for a in ai['abschnitte']] != [(a['titel'], ohne(a['lernziele'])) for a in ni['abschnitte']]:
        F.append('abschnitte anders als nur um neue Lernziele ergänzt')
    if ai['teilfaehigkeiten'] != [t for t in ni['teilfaehigkeiten'] if t['k'] not in dazu_lz]:
        F.append('teilfaehigkeiten anders als nur um neue ergänzt')
    if {k: (ohne(v) if isinstance(v, list) else v) for k, v in ni['bewertung'].items()} != ai['bewertung']:
        F.append('bewertung anders als nur um neue Lernziele ergänzt')
    na = len(alt['aufgaben'])
    if neu['aufgaben'][:na] != alt['aufgaben']:
        F.append('alte Aufgaben geändert oder umsortiert')
    neue = neu['aufgaben'][na:]
    fremd = {a['l'] for a in neue} - set(dazu_lz) - erw
    if fremd: F.append(f'neue Aufgaben in nicht beauftragten Karten: {sorted(fremd)}')
    z = collections.Counter((a['l'], a['p'], a['s']) for a in neue)
    print(f'{thema}: alt {na} Aufgaben, neu {len(neu["aufgaben"])}, dazu {len(neue)}; neue Lernkarten {dazu_lz}; erweitert {sorted(erw)}')
    for l in dazu_lz + sorted(erw):
        print(f'  {l:20s} Ü1 {z[(l, "uebung", 1)]} Ü2 {z[(l, "uebung", 2)]} Ü3 {z[(l, "uebung", 3)]} | Test {z[(l, "test", 2)]} '
              f'Korrektur {z[(l, "korrektur", 2)]} Sicherung {z[(l, "sicherung", 2)]}')
    print('NUR NEUES DAZU: JA' if not F else 'FEHLER:\n  ' + '\n  '.join(F))
    return 1 if F else 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
