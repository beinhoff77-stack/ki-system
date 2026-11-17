#!/usr/bin/env python3
"""Nachweis Neunzehnte Runde (durchsicht-kl7): Was hat sich gegenüber origin/lernen-app geändert?

Aufruf: python3 -I inhalte/generatoren/_durchsicht_nachweis.py <thema> [<stand>]
Erlaubt: in inhalt.etappen nur Felder einstieg/woerter/schritte/fehler/fehler_bild/regel/probe/bild (Lernziel, Titel, Reihenfolge gleich);
in aufgaben nur Stufe (s), Lösung/Tipp/Weg (o/h/w/c), ersetzte Aufgaben (gleiche Lernkarte, gleicher Pool, gleiche Stelle) und neue Übungen.
Alles andere muss Zeichen für Zeichen gleich sein. Gibt jede Änderung aus.
"""
import collections
import difflib
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]
ERLAUBT_KARTE = {'einstieg', 'woerter', 'schritte', 'fehler', 'fehler_bild', 'regel', 'probe', 'bild'}


def main(thema, stand='origin/lernen-app'):
    pfad = f'inhalte/themen/{thema}.json'
    alt = json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{stand}:{pfad}'], capture_output=True, check=True, text=True).stdout)
    neu = json.loads((WURZEL / pfad).read_text(encoding='utf-8'))
    k = lambda a: json.dumps(a, ensure_ascii=False, sort_keys=True)
    F = []
    for x in set(alt) | set(neu):
        if x in ('aufgaben', 'inhalt'): continue
        if k(alt.get(x)) != k(neu.get(x)): F.append(f'Feld {x} geändert')
    for x in set(alt['inhalt']) | set(neu['inhalt']):
        if x == 'etappen': continue
        if k(alt['inhalt'].get(x)) != k(neu['inhalt'].get(x)): F.append(f'inhalt.{x} geändert')
    ea, en = alt['inhalt']['etappen'], neu['inhalt']['etappen']
    if [(e['lernziel'], e['titel']) for e in ea] != [(e['lernziel'], e['titel']) for e in en]: F.append('Lernkarten: Lernziel/Titel/Reihenfolge geändert')
    karten = 0
    for a, b in zip(ea, en):
        felder = sorted(x for x in set(a) | set(b) if k(a.get(x)) != k(b.get(x)))
        if felder:
            karten += 1
            print(f'  LERNKARTE {a["lernziel"]}: geändert {", ".join(felder)}')
            if set(felder) - ERLAUBT_KARTE: F.append(f'Lernkarte {a["lernziel"]}: unerlaubte Felder {set(felder) - ERLAUBT_KARTE}')
    A, N = alt['aufgaben'], neu['aufgaben']
    sm = difflib.SequenceMatcher(a=[k(a) for a in A], b=[k(a) for a in N], autojunk=False)
    z = collections.Counter()
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal': continue
        if tag == 'insert':
            for b in N[j1:j2]:
                z['neu'] += 1
                if b['p'] != 'uebung': F.append('neue Aufgabe nicht im Pool uebung')
            continue
        if tag != 'replace' or i2 - i1 != j2 - j1:
            F.append(f'Aufgaben gelöscht/umsortiert bei {i1}–{i2} → {j1}–{j2}'); continue
        for a, b in zip(A[i1:i2], N[j1:j2]):
            if (a['l'], a['p'], a['t']) != (b['l'], b['p'], b['t']): F.append(f'Lernkarte/Pool geändert: {a["f"]["text"][:50]}')
            if a['f']['text'] != b['f']['text'] or a.get('a') != b.get('a') or a['f'] != b['f'] or a['y'] != b['y']:
                z['ersetzt'] += 1
                print(f'  ERSETZT  {a["l"]}/{a["p"]} s{a["s"]}: „{a["f"]["text"][:90]}“ → s{b["s"]} „{b["f"]["text"][:90]}“')
            else:
                felder = sorted(x for x in set(a) | set(b) if a.get(x) != b.get(x))
                if felder == ['s']: z['umgestuft'] += 1
                elif set(felder) <= {'o', 'h', 'w', 'c', 's'}: z['berichtigt'] += 1
                else: F.append(f'unerlaubte Änderung {felder}: {a["f"]["text"][:50]}')
    st = collections.Counter((a['l'], a['s']) for a in N if a['p'] == 'uebung')
    for e in en:
        for s in (1, 2, 3):
            if st[(e['lernziel'], s)] < 3: F.append(f'{e["lernziel"]}: nur {st[(e["lernziel"], s)]} Übungen auf Stufe {s}')
    print(f'{thema}: Lernkarten geändert {karten}, umgestuft {z["umgestuft"]}, berichtigt {z["berichtigt"]}, ersetzt {z["ersetzt"]}, neu {z["neu"]}; '
          f'unverändert {sum(b.size for b in sm.get_matching_blocks())} von {len(A)} alten Aufgaben')
    if F:
        print('NACHWEIS FEHLGESCHLAGEN:'); [print('  -', f) for f in F]; return 1
    print('NACHWEIS OK')
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
