#!/usr/bin/env python3
"""Nachweis Fünfzehnte Runde (Zweig nacharbeit): Was hat sich in einer Themendatei gegenüber <git-ref> geändert?

Aufruf: python3 -I inhalte/generatoren/_nacharbeit_nachweis.py <thema_schluessel> [<git-ref>]   (Standard: origin/lernen-app)
Gibt jeden geänderten Pfad außerhalb von „aufgaben“ aus (z. B. inhalt.etappen[kreis_lage].schritte, offen, inhalt.bewertung)
und zählt die Aufgaben: unverändert / geändert (mit Feldern) / neu / entfernt. Entfernte oder umsortierte Aufgaben sind ein Fehler.
"""
import difflib
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]
k = lambda a: json.dumps(a, ensure_ascii=False, sort_keys=True)


def pfade(a, b, p=''):
    """Liste der geänderten Pfade (Etappen werden über ihr Lernziel benannt)."""
    if type(a) is not type(b): return [p or '.']
    if isinstance(a, dict):
        aus = []
        for x in sorted(set(a) | set(b)):
            if x not in a: aus.append(f'{p}.{x} (neu)')
            elif x not in b: aus.append(f'{p}.{x} (entfernt)')
            else: aus += pfade(a[x], b[x], f'{p}.{x}')
        return aus
    if isinstance(a, list):
        if p.endswith('.etappen') and all(isinstance(e, dict) and 'lernziel' in e for e in a + b):
            da, db = {e['lernziel']: e for e in a}, {e['lernziel']: e for e in b}
            if [e['lernziel'] for e in a] != [e['lernziel'] for e in b]: return [f'{p} (Reihenfolge/Menge)']
            aus = []
            for lz in da: aus += pfade(da[lz], db[lz], f'{p}[{lz}]')
            return aus
        return [] if k(a) == k(b) else [p]
    return [] if a == b else [p]


def main(thema, ref='origin/lernen-app'):
    rel = f'inhalte/themen/{thema}.json'
    alt = json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{ref}:{rel}'], capture_output=True, check=True, text=True).stdout)
    neu = json.loads((WURZEL / rel).read_text(encoding='utf-8'))
    ok = True
    geaendert = pfade({x: v for x, v in alt.items() if x != 'aufgaben'}, {x: v for x, v in neu.items() if x != 'aufgaben'})
    for g in geaendert: print('  GEÄNDERT', g.lstrip('.'))
    A, N = alt['aufgaben'], neu['aufgaben']
    sm = difflib.SequenceMatcher(a=[k(a) for a in A], b=[k(a) for a in N], autojunk=False)
    z = {'gleich': sum(b.size for b in sm.get_matching_blocks()), 'geaendert': 0, 'neu': 0, 'entfernt': 0}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal': continue
        if tag == 'insert':
            z['neu'] += j2 - j1
            continue
        if tag == 'replace' and i2 - i1 == j2 - j1:
            for a, b in zip(A[i1:i2], N[j1:j2]):
                z['geaendert'] += 1
                felder = sorted(x for x in set(a) | set(b) if a.get(x) != b.get(x))
                print(f'  AUFGABE  {a["l"]}/{a["p"]} s{a["s"]}: „{a["f"]["text"][:80]}“ Felder {felder}')
            continue
        ok = False
        z['entfernt'] += i2 - i1
        print(f'  FEHLER {tag}: alte Aufgaben {i1}–{i2} → {j1}–{j2}')
    neue = [b for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag == 'insert' for b in N[j1:j2]]
    if any(b['p'] != 'uebung' for b in neue): ok = False; print('  FEHLER: neue Aufgabe außerhalb des Übungs-Pools')
    print(f'{thema}: Aufgaben unverändert {z["gleich"]} von {len(A)}, geändert {z["geaendert"]}, neu {z["neu"]}, entfernt {z["entfernt"]}; '
          f'{len(geaendert)} geänderte Stellen außerhalb der Aufgaben – {"NACHWEIS OK" if ok else "NACHWEIS FEHLER"}')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
