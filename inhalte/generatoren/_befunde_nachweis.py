#!/usr/bin/env python3
"""Nachweis Dreizehnte Runde: Welche Aufgaben haben sich gegenüber lernen-app geändert?

Aufruf: python3 -I inhalte/generatoren/_befunde_nachweis.py <thema_schluessel> [<stand>]   (Standard-Stand: origin/lernen-app)
Gibt jede geänderte Aufgabe mit den geänderten Feldern aus (Stufe, Lösung, Tipp, Weg, ersetzt) und jede neue Aufgabe.
Prüft außerdem: alles außer „aufgaben“ unverändert; Reihenfolge der übrigen Aufgaben unverändert.
"""
import difflib
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
    if k({x: v for x, v in alt.items() if x != 'aufgaben'}) != k({x: v for x, v in neu.items() if x != 'aufgaben'}):
        ok = False; print('FEHLER: Teile außerhalb von „aufgaben“ geändert')
    A, N = alt['aufgaben'], neu['aufgaben']
    sm = difflib.SequenceMatcher(a=[k(a) for a in A], b=[k(a) for a in N], autojunk=False)
    gleich = sum(b.size for b in sm.get_matching_blocks())
    zaehl = {'stufe': 0, 'loesung': 0, 'ersetzt': 0, 'neu': 0}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal': continue
        if tag == 'replace' and i2 - i1 == j2 - j1:
            for a, b in zip(A[i1:i2], N[j1:j2]):
                if a['f']['text'] != b['f']['text'] or a.get('a') != b.get('a') or a['f'] != b['f']:
                    zaehl['ersetzt'] += 1
                    print(f'  ERSETZT  {a["l"]}/{a["p"]} s{a["s"]}: „{a["f"]["text"]}“\n           → s{b["s"]} „{b["f"]["text"]}“')
                    if (a['l'], a['p'], a['t']) != (b['l'], b['p'], b['t']): ok = False; print('    FEHLER: Lernkarte/Pool geändert')
                else:
                    felder = sorted(x for x in set(a) | set(b) if a.get(x) != b.get(x))
                    art = 'stufe' if felder == ['s'] else 'loesung'
                    zaehl[art] += 1
                    print(f'  {art.upper():8} {a["l"]}/{a["p"]}: „{a["f"]["text"][:90]}“  Felder: {felder}' + (f' ({a["s"]}→{b["s"]})' if 's' in felder else ''))
                    if set(felder) - {'s', 'o', 'h', 'w', 'c'}: ok = False; print('    FEHLER: unerlaubtes Feld geändert')
        elif tag == 'insert':
            for b in N[j1:j2]:
                zaehl['neu'] += 1
                print(f'  NEU      {b["l"]}/{b["p"]} s{b["s"]}: „{b["f"]["text"][:90]}“')
                if b['p'] != 'uebung': ok = False
        else:
            ok = False; print(f'FEHLER: {tag} {i1}-{i2} → {j1}-{j2} (gelöscht oder umsortiert)')
    print(f'{thema}: {len(A)} alt, {len(N)} neu, unverändert {gleich}; geändert: Stufe {zaehl["stufe"]}, Lösung/Tipp/Weg {zaehl["loesung"]}, ersetzt {zaehl["ersetzt"]}, neu {zaehl["neu"]} – '
          f'{"NACHWEIS OK" if ok else "NACHWEIS FEHLER"}')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
