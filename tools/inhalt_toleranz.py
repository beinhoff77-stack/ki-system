#!/usr/bin/env python3
"""Trägt bei gerundeten Zahl-Aufgaben die Toleranz nach (Werkstatt #150).
Regel: Rechenausdruck c = round(<ausdruck>, n) und noch keine Toleranz -> toleranz = 10^-n (eine Einheit der letzten Stelle).
Aufruf: python3 -I tools/inhalt_toleranz.py [--schreiben]   (ohne --schreiben nur zählen)"""
import json
import re
import sys
from pathlib import Path

MUSTER = re.compile(r'^round\((.*),\s*(\d)\)$', re.S)
n_ges = 0
for p in sorted((Path(__file__).resolve().parent.parent / 'inhalte' / 'themen').glob('*.json')):
    d = json.loads(p.read_text(encoding='utf-8')); n = 0
    for a in d['aufgaben']:
        m = MUSTER.match(str(a.get('c', ''))) if a.get('y') == 'zahl' else None
        if m and 'toleranz' not in a['o']:
            a['o']['toleranz'] = round(10 ** -int(m.group(2)), int(m.group(2))) if int(m.group(2)) else 1
            n += 1
    if n:
        print(f'{p.name}: {n}'); n_ges += n
        if '--schreiben' in sys.argv: p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8')
print('gesamt', n_ges)
