"""Nachweis Zwanzigste Runde (stufen-kl5): gegen origin/lernen-app ändern sich bei alten Aufgaben nur g und s.

Aufruf: python3 -I inhalte/generatoren/_stufen_kl5_nachweis.py <thema>
Prüft: alle alten Aufgaben sind genau einmal da; außer g und s ist nichts an ihnen geändert; Reihenfolge der Pools
test/korrektur/sicherung unverändert; alles außerhalb von „aufgaben“ unverändert; neue Aufgaben haben g und sind uebung oder bonus.
"""
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent


def schluessel(a):
    f = a['f']
    return json.dumps([a['l'], a['p'], f.get('text'), a.get('a'), f.get('schablone'), f.get('grafik')], ensure_ascii=False, sort_keys=True)


def main(thema):
    pfad = f'inhalte/themen/{thema}.json'
    alt = json.loads(subprocess.run(['git', 'show', f'origin/lernen-app:{pfad}'], cwd=WURZEL, capture_output=True, check=True, text=True).stdout)
    neu = json.loads((WURZEL / pfad).read_text())
    fehler = []
    for k in set(alt) | set(neu):
        if k != 'aufgaben' and alt.get(k) != neu.get(k): fehler.append(f'Feld {k} außerhalb der Aufgaben geändert')
    nk = {}
    for a in neu['aufgaben']: nk.setdefault(schluessel(a), []).append(a)
    geaendert = {'g': 0, 's': 0}
    for a in alt['aufgaben']:
        xs = nk.get(schluessel(a), [])
        if len(xs) != 1: fehler.append(f'{len(xs)} Treffer für alte Aufgabe „{a["f"]["text"][:60]}“'); continue
        b = xs.pop()
        for k in set(a) | set(b):
            if k in ('g', 's'):
                if a.get(k) != b.get(k): geaendert[k] += 1
            elif a.get(k) != b.get(k): fehler.append(f'Feld {k} geändert: „{a["f"]["text"][:60]}“')
    rest = [a for xs in nk.values() for a in xs]
    for a in rest:
        if a['p'] not in ('uebung', 'bonus') or not a.get('g'): fehler.append(f'neue Aufgabe ohne g oder im falschen Pool: „{a["f"]["text"][:60]}“')
    for p in ('test', 'korrektur', 'sicherung'):
        if [schluessel(a) for a in alt['aufgaben'] if a['p'] == p] != [schluessel(a) for a in neu['aufgaben'] if a['p'] == p]:
            fehler.append(f'Pool {p}: Reihenfolge geändert')
    ue = sum(1 for a in rest if a['p'] == 'uebung'); bo = sum(1 for a in rest if a['p'] == 'bonus')
    print(f'{thema}: alte Aufgaben {len(alt["aufgaben"])} (davon g gesetzt {geaendert["g"]}, s geändert {geaendert["s"]}), '
          f'neu {ue} Übungen + {bo} Knobel – ' + ('NACHWEIS OK' if not fehler else f'{len(fehler)} FEHLER'))
    for f in fehler[:20]: print('  ' + f)
    return 1 if fehler else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
