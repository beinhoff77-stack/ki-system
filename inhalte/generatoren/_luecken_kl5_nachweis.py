#!/usr/bin/env python3
"""Nachweis Achtzehnte Runde, Teil B (Zweig luecken-kl5): Gegenüber <git-ref> (Standard origin/lernen-app) kam nur Neues dazu.

Aufruf (aus der Wurzel des Repositorys):
    python3 -I inhalte/generatoren/_luecken_kl5_nachweis.py <thema_schluessel> [--erweitert lz1,lz2] [--ref <git-ref>]

Geprüft wird:
  1. Jede alte Aufgabe steht unverändert und an derselben Stelle; neue Aufgaben hängen nur hinten an.
  2. Jede alte Lernkarte ist Zeichen für Zeichen gleich (über das Lernziel gesucht), ihre Reihenfolge untereinander bleibt.
  3. Neue Aufgaben gehören zu neuen Lernkarten – oder zu Karten, die mit --erweitert ausdrücklich erweitert werden.
  4. abschnitte, teilfaehigkeiten, bewertung: Jeder alte Eintrag bleibt (Titel/Text gleich, alte Lernziele in alter Reihenfolge);
     hinzu kommen nur die neuen Lernziele oder neue Einträge mit ausschließlich neuen Lernzielen.
  5. Alle übrigen Felder (thema_schluessel, klasse, ziel, merke, quellen, offen …) sind unverändert.
"""
import collections
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]


def main(thema, erweitert=(), ref='origin/lernen-app'):
    rel = f'inhalte/themen/{thema}.json'
    alt = json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{ref}:{rel}'], capture_output=True, check=True, text=True).stdout)
    neu = json.loads((WURZEL / rel).read_text(encoding='utf-8'))
    F = []
    # 5. übrige Felder
    for k in set(alt) | set(neu):
        if k in ('aufgaben', 'inhalt'): continue
        if alt.get(k) != neu.get(k): F.append(f'Feld {k} geändert')
    ai, ni = alt['inhalt'], neu['inhalt']
    for k in set(ai) | set(ni):
        if k in ('etappen', 'abschnitte', 'teilfaehigkeiten', 'bewertung'): continue
        if ai.get(k) != ni.get(k): F.append(f'inhalt.{k} geändert')
    # 2. Lernkarten
    alt_lz = [e['lernziel'] for e in ai['etappen']]
    neu_e = {e['lernziel']: e for e in ni['etappen']}
    neu_lz = [e['lernziel'] for e in ni['etappen']]
    for e in ai['etappen']:
        if neu_e.get(e['lernziel']) != e: F.append(f'Lernkarte {e["lernziel"]} geändert oder fehlt')
    if [x for x in neu_lz if x in alt_lz] != alt_lz: F.append('Reihenfolge der alten Lernkarten geändert')
    dazu_lz = [x for x in neu_lz if x not in alt_lz]
    # 4. abschnitte / teilfaehigkeiten / bewertung
    def liste_ok(name, alt_l, neu_l, schl):
        na = {x[schl]: x for x in neu_l}
        for x in alt_l:
            y = na.get(x[schl])
            if y is None: F.append(f'{name} „{x[schl]}“ fehlt'); continue
            if {k: v for k, v in x.items() if k != 'lernziele'} != {k: v for k, v in y.items() if k != 'lernziele'}: F.append(f'{name} „{x[schl]}“: Text geändert')
            if [z for z in y['lernziele'] if z in alt_lz] != x['lernziele']: F.append(f'{name} „{x[schl]}“: alte Lernziele geändert')
            if any(z not in alt_lz and z not in dazu_lz for z in y['lernziele']): F.append(f'{name} „{x[schl]}“: unbekanntes Lernziel')
        for y in neu_l:
            if y[schl] not in {x[schl] for x in alt_l} and any(z in alt_lz for z in y['lernziele']):
                F.append(f'neuer Eintrag {name} „{y[schl]}“ enthält alte Lernziele')
        if [x[schl] for x in neu_l if x[schl] in {a[schl] for a in alt_l}] != [x[schl] for x in alt_l]: F.append(f'{name}: Reihenfolge geändert')
    liste_ok('Abschnitt', ai['abschnitte'], ni['abschnitte'], 'titel')
    liste_ok('Teilfähigkeit', ai['teilfaehigkeiten'], ni['teilfaehigkeiten'], 'k')
    ab, nb = ai['bewertung'], ni['bewertung']
    for k in set(ab) | set(nb):
        if k.startswith('lernziele_'):
            if [z for z in nb.get(k, []) if z in alt_lz] != ab.get(k, []): F.append(f'bewertung.{k}: alte Einträge geändert')
        elif ab.get(k) != nb.get(k): F.append(f'bewertung.{k} geändert')
    # 1./3. Aufgaben
    A, N = alt['aufgaben'], neu['aufgaben']
    if N[:len(A)] != A:
        i = next(i for i, (a, b) in enumerate(zip(A, N)) if a != b) if any(a != b for a, b in zip(A, N)) else len(N)
        F.append(f'alte Aufgabe {i + 1} geändert oder fehlt')
    dazu = N[len(A):]
    for b in dazu:
        if b['l'] not in dazu_lz and b['l'] not in erweitert: F.append(f'neue Aufgabe in alter Karte {b["l"]}: {b["f"]["text"][:60]}')
    for lz in erweitert:
        if lz not in alt_lz: F.append(f'--erweitert {lz}: keine alte Karte')
    z = collections.Counter((b['l'], b['p'], b['s']) for b in dazu)
    print(f'== {thema} (gegen {ref})')
    print(f'   alte Aufgaben: {len(A)}, davon unverändert an gleicher Stelle: {"alle" if N[:len(A)] == A else "NEIN"}; neu angehängt: {len(dazu)}')
    print(f'   alte Lernkarten unverändert: {sum(neu_e.get(e["lernziel"]) == e for e in ai["etappen"])} von {len(alt_lz)}; neue Lernkarten: {dazu_lz}')
    for lz in dazu_lz + list(erweitert):
        print(f'   {lz:24} Übung s1/s2/s3: {z[(lz, "uebung", 1)]}/{z[(lz, "uebung", 2)]}/{z[(lz, "uebung", 3)]}  Test {z[(lz, "test", 2)]}  '
              f'Korrektur {z[(lz, "korrektur", 2)]}  Sicherung {z[(lz, "sicherung", 2)]}  Stelle {neu_lz.index(lz) + 1}/{len(neu_lz)}')
    for f in F: print('   FEHLER', f)
    print('   NACHWEIS OK' if not F else '   NACHWEIS FEHLER')
    return 0 if not F else 1


if __name__ == '__main__':
    args = sys.argv[1:]
    erw, ref = (), 'origin/lernen-app'
    if '--erweitert' in args:
        i = args.index('--erweitert'); erw = tuple(args[i + 1].split(',')); del args[i:i + 2]
    if '--ref' in args:
        i = args.index('--ref'); ref = args[i + 1]; del args[i:i + 2]
    sys.exit(max(main(t, erw, ref) for t in args))
