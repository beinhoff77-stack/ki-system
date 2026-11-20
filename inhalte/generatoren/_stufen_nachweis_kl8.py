"""Nachweis Zwanzigste Runde: gegen origin/lernen-app ändern sich bei alten Aufgaben nur g und s (und die Reihenfolge der Übungen);
alle übrigen Felder der Datei bleiben gleich; neu sind nur Übungen und Bonus-Bordkarten mit Typ.
Aufruf: python3 -I inhalte/generatoren/_stufen_nachweis.py <thema>"""
import collections
import json
import subprocess
import sys
from pathlib import Path

thema = sys.argv[1]
pfad = f'inhalte/themen/{thema}.json'
alt = json.loads(subprocess.run(['git', 'show', f'origin/lernen-app:{pfad}'], capture_output=True, text=True, check=True).stdout)
neu = json.loads(Path(pfad).read_text(encoding='utf-8'))
for k in set(alt) | set(neu):
    if k != 'aufgaben': assert alt.get(k) == neu.get(k), f'Feld {k} geändert'
ohne = lambda a: json.dumps({k: v for k, v in a.items() if k not in ('g', 's')}, ensure_ascii=False, sort_keys=True)
pool = collections.Counter(ohne(a) for a in alt['aufgaben'])
alt_s = {ohne(a): a['s'] for a in alt['aufgaben']}
umgestuft = neue = bonus = 0
for a in neu['aufgaben']:
    k = ohne(a)
    if pool[k] > 0:
        pool[k] -= 1
        if a['s'] != alt_s[k]:
            assert a['p'] == 'uebung', 's nur bei Übungen'
            umgestuft += 1
        if 'g' in a: assert a['p'] == 'uebung'
    else:
        assert a.get('g') and a['p'] in ('uebung', 'bonus'), f'neue Aufgabe ohne Typ oder falscher Pool: {a["f"]["text"][:60]}'
        if a['p'] == 'bonus': bonus += 1
        else: neue += 1
assert sum(pool.values()) == 0, 'alte Aufgabe fehlt oder wurde verändert'
# Reihenfolge der anderen Pools unverändert
for p in ('test', 'korrektur', 'sicherung'):
    assert [ohne(a) for a in alt['aufgaben'] if a['p'] == p] == [ohne(a) for a in neu['aufgaben'] if a['p'] == p], f'Reihenfolge {p} geändert'
print(f'NACHWEIS OK {thema}: umgestuft {umgestuft}, neue Übungen {neue}, Knobel {bonus}')
