#!/usr/bin/env python3
"""Hilfen für die fünfte Runde (Nachbau gleichungen.einfach, groessen.indirekt, gleichungen.linear).

Formatierung und Aufgaben-Bausteine (A, Z, L, zt, kl, lin …) kommen unverändert aus _bausatz.py.
Hier neu: Zusammenbau mit Dublettenprüfung über das ganze Thema, Waage-Bild, Tabellen-Bild.
"""
import json
import random
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.dont_write_bytecode = True
HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
import _bausatz as _b  # noqa: E402
from _bausatz import A, L, M, Z, bruch, cz, dez, eur, jw, kl, koeff, lin, mit_bild, rechne, zt  # noqa: E402,F401

THEMEN = HIER.parent / 'themen'
# Je Lernkarte: 5 + 7 + 5 Übungen, 1 Test, 3 Korrektur, 6 Sicherung = 27 Aufgaben
PLAN = [('uebung', 1)] * 5 + [('uebung', 2)] * 7 + [('uebung', 3)] * 5 + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6


def waage(links, rechts):
    """Balkenwaage im Gleichgewicht als Figur: links/rechts sind kurze Beschriftungen der Schalen."""
    return {'typ': 'figur', 'label': f'Waage im Gleichgewicht: links {links}, rechts {rechts}',
            'punkte': {'_A': [1.5, 2], '_B': [8.5, 2], '_S': [5, 2], '_F1': [4, 0], '_F2': [6, 0],
                       '_L1': [-0.5, 2.6], '_L2': [3.5, 2.6], '_R1': [6.5, 2.6], '_R2': [10.5, 2.6],
                       '_LA': [1.5, 2.6], '_RA': [8.5, 2.6]},
            'flaeche': ['_S', '_F1', '_F2'],
            'linien': [['_A', '_B'], ['_A', '_LA'], ['_B', '_RA'], ['_L1', '_L2', links], ['_R1', '_R2', rechts]]}


def tabelle(kopf, zeilen):
    return {'typ': 'tabelle', 'kopf': [str(k) for k in kopf], 'zeilen': [[str(z) for z in r] for r in zeilen]}


def gl(a, b, var='x'):
    """Text a·x + b mit deutschem Mal-Punkt: 3 · x + 4 (für Klasse 5)."""
    s = var if a == 1 else f'{zt(a)} · {var}'
    if b: s += f' {"+" if b > 0 else "−"} {zt(abs(b))}'
    return s


def baue(meta, etappen, gen, abschnitte, ziel, merke, offen=(), plan=PLAN, seed=0, vertiefung=(), teil=None):
    R = random.Random(seed or meta['thema_id'] * 1000 + 5)
    _b.POS.clear()
    out, gesehen = [], set()
    beispiele = {s for e in etappen for s in e['schritte']}
    for e in etappen:
        lz = e['lernziel']
        verbot = e.pop('_verbot', [])
        for pool, stufe in plan:
            for _ in range(4000):
                a = gen[lz](R, stufe)
                k = a['f']['text'] + '|' + json.dumps(sorted(map(str, a.get('a', []))), ensure_ascii=False) + '|' + \
                    json.dumps(a['f'].get('grafik'), sort_keys=True) + '|' + json.dumps(a['f'].get('schablone'), ensure_ascii=False)
                if a['f']['text'] in beispiele or k in gesehen or any(v in a['f']['text'] for v in verbot): continue
                break
            else:
                raise SystemExit(f'zu wenige Varianten für {lz} (Stufe {stufe})')
            gesehen.add(k)
            assert len(a['w']) >= 15, f'Lösungsweg zu kurz: {a}'
            if pool != 'uebung': a.pop('h', None)
            else: assert a.get('h'), f'Tipp fehlt: {lz}'
            if not a.get('h'): a.pop('h', None)
            if a['y'] == 'zahl': assert rechne(a['c']) == Fr(str(a['o']['wert'])), a
            out.append({'l': lz, 't': (teil or {}).get(lz, lz), 'p': pool, 's': stufe, **a})
    lz_alle = [e['lernziel'] for e in etappen]
    if teil:
        tf = []
        for k, text in teil['_texte']:
            tf.append({'k': k, 'text': text, 'lernziele': [x for x in lz_alle if teil[x] == k]})
    else:
        tf = [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in etappen]
    d = {
        'thema_schluessel': meta['thema_schluessel'], 'thema_id': meta['thema_id'], 'block_id': meta['block_id'],
        'klasse': meta['klasse'], 'autor': f'Claude (Nachbau Runde 5, Generator {meta["thema_schluessel"].replace(".", "_")}.py)',
        'inhalt': {
            'ziel': ziel, 'merke': list(merke),
            'abschnitte': [{'titel': t, 'lernziele': l} for t, l in abschnitte],
            'etappen': etappen,
            'teilfaehigkeiten': tf,
            'bewertung': {'lernziele_pflicht': [x for x in lz_alle if x not in vertiefung],
                          'lernziele_vertiefung': [x for x in lz_alle if x in vertiefung], 'testaufgaben_je_lernziel': 1,
                          'hilfen_im_test': False},
            'quellen': {'erklaerungen': 'Eigene Fassung (Claude).', 'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern (Gymnasium).'},
        },
        'aufgaben': out,
    }
    if offen: d['offen'] = list(offen)
    THEMEN.mkdir(parents=True, exist_ok=True)
    pfad = THEMEN / f"{meta['thema_schluessel']}.json"
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{pfad.name}: {len(etappen)} Lernkarten, {len(out)} Aufgaben')
    return d
