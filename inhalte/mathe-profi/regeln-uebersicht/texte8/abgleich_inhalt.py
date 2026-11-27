#!/usr/bin/env python3
"""Gleicht inhalt.json (Designer-Entwurf, nur Texte) mit klassenleiter.json ab: Klassenleitern und regeln[].klassen kommen aus EINER Quelle (klassenleiter.json).
Aufruf: python3 -I inhalte/mathe-profi/regeln-uebersicht/texte8/abgleich_inhalt.py   (idempotent)"""
import json, pathlib, re
hier = pathlib.Path(__file__).resolve().parent; repo = hier.parents[3]
P = repo / 'inhalte/design/gesetzbuch/entwurf/teile/inhalt.json'
d = json.loads(P.read_text(encoding='utf-8'))
orig = P.read_text(encoding='utf-8')
KUERZEL = {'Zahlen': 'zahlen', 'Algebra': 'algebra', 'Geld und Verhältnisse': 'geld', 'Geometrie': 'geo', 'Fläche und Raum': 'fur', 'Funktionen': 'funktionen', 'Daten und Zufall': 'daten'}
kl = json.loads((hier.parent / 'klassenleiter.json').read_text(encoding='utf-8'))['leitern']
n = {}; neu = {}
for L in kl:
    if L['art'] == 'rechenregel': n['R'] = n.get('R', 0) + 1; k = 'R%d' % n['R']
    else: n[L['ort']] = n.get(L['ort'], 0) + 1; k = 'I-%s-%d' % (KUERZEL[L['ort']], n[L['ort']])
    st = []
    for s in L['stufen']:
        if s['kommt_vor']:
            assert [s['text'][a:b] for a, b in s['wirkende_stelle_positionen']] == s['wirkende_stelle']
            st.append({'klasse': s['klasse'], 'art': s['art'], 'thema': s.get('thema'), 'text': s['text'], 'pos': s['wirkende_stelle_positionen']})
        else: st.append({'klasse': s['klasse'], 'grund': re.sub(r'^kommt nicht vor – ', '', s['grund'])})
    neu[k] = {'kennung': L['kennung'], 'markiert': L['in_jeder_zeile_markiert'], 'klassen': L['klassen_mit_beispiel'], 'stufen': st}
assert set(neu) == set(d['leitern'])
d['leitern'] = neu
for r in d['regeln']:
    r['klassen'] = [{'klasse': s['klasse'], 'art': s['art'], 'text': s['text'], 'thema': s['thema']} for s in neu[r['id']]['stufen'] if 'text' in s]
out = json.dumps(d, ensure_ascii=False, indent=1)
P.write_text(out, encoding='utf-8')
print('inhalt.json abgeglichen:', len(neu), 'Leitern')
