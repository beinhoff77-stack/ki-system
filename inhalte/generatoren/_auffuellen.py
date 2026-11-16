#!/usr/bin/env python3
"""Hilfen für die neunte Runde (Aufgaben auffüllen: terme.umformen, zahlen.teilbarkeit, finanzen.zinsen).

Die Lernkarten (einstieg, woerter, bild, schritte, fehler, fehler_bild, regel, probe) kommen unverändert aus der Überlagerung
inhalte/klar/<thema>.json; Lernziele, Reihenfolge und Titel wie in inhalte/klar/quelle.md. Neu sind nur die Aufgaben.
Formatierung und Bausteine (A, Z, L, zt, kl …) kommen aus _bausatz.py; jede Zahl-Aufgabe und jede Lücke wird beim Bauen nachgerechnet.
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
from _bausatz import A, L, Z, bruch, cz, dez, eur, jw, kl, mit_bild, rechne, zt  # noqa: E402,F401

THEMEN = HIER.parent / 'themen'
KLAR = HIER.parent / 'klar'
# Je Lernkarte: 4 + 5 + 4 Übungen (Stufe 1/2/3), 1 Test, 3 Korrektur, 6 Sicherung = 23 Aufgaben
PLAN = [('uebung', 1)] * 4 + [('uebung', 2)] * 5 + [('uebung', 3)] * 4 + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6
FELDER = ('einstieg', 'woerter', 'bild', 'schritte', 'fehler', 'fehler_bild', 'regel', 'probe')


def etappen_aus_klar(thema, titel):
    """titel: Liste (lernziel, titel) in der Reihenfolge aus quelle.md. Erklärfelder unverändert aus der Überlagerung."""
    karten = json.loads((KLAR / f'{thema}.json').read_text(encoding='utf-8'))['karten']
    assert [lz for lz, _ in titel] == list(karten), ('Lernziele/Reihenfolge weichen von der Überlagerung ab', list(karten))
    et = []
    for lz, t in titel:
        e = {'lernziel': lz, 'titel': t}
        e.update({k: karten[lz][k] for k in FELDER if k in karten[lz]})
        assert e.get('bild'), f'Kartenbild fehlt: {lz}'
        et.append(e)
    return et


def g4(x):
    """Zahl wie auf den Lernkarten dieser Themen: schon ab 1 000 mit Leerzeichen gegliedert (3 470, 2 000 €)."""
    t = zt(x) if not isinstance(x, str) else x
    vz, t = ('−', t[1:]) if t.startswith('−') else ('', t)
    ganz, *rest = t.replace(' ', '').split(',')
    if len(ganz) >= 4:
        g = ''
        while len(ganz) > 3: g, ganz = ' ' + ganz[-3:] + g, ganz[:-3]
        ganz += g
    return vz + ganz + (',' + rest[0] if rest else '')


def term(glieder):
    """Glieder [(Koeffizient, 'x²'), (k, 'x'), (k, '')] als Text: 3x² − x + 5. Nullglieder fallen weg."""
    s = ''
    for c, v in glieder:
        c = Fr(c)
        if c == 0: continue
        b = zt(abs(c)) if (abs(c) != 1 or not v) else ''
        if not s: s = ('−' if c < 0 else '') + b + v
        else: s += (' − ' if c < 0 else ' + ') + b + v
    return s or '0'


def faktor(c, v=''):
    """Einzelnes Glied als Faktor, negativ in Klammern: (−2x)."""
    t = term([(c, v)])
    return f'({t})' if Fr(c) < 0 else t


def baue(meta, etappen, gen, abschnitte, ziel, merke, verbot=None, offen=(), plan=PLAN, seed=0, vertiefung=()):
    R = random.Random(seed or meta['thema_id'] * 1000 + 9)
    _b.POS.clear()
    verbot = verbot or {}
    out, gesehen = [], set()
    beispiele = {(s['text'] if isinstance(s, dict) else s) for e in etappen for s in e['schritte']}
    for e in etappen:
        lz = e['lernziel']
        for pool, stufe in plan:
            for _ in range(5000):
                a = gen[lz](R, stufe)
                k = a['f']['text'] + '|' + json.dumps(sorted(map(str, a.get('a', []))), ensure_ascii=False) + '|' + \
                    json.dumps(a['f'].get('grafik'), sort_keys=True) + '|' + json.dumps(a['f'].get('schablone'), ensure_ascii=False)
                if a['f']['text'] in beispiele or k in gesehen or any(v in a['f']['text'] for v in verbot.get(lz, ())): continue
                break
            else:
                raise SystemExit(f'zu wenige Varianten für {lz} (Stufe {stufe})')
            gesehen.add(k)
            assert len(a['w']) >= 15, f'Lösungsweg zu kurz: {a}'
            if pool != 'uebung': a.pop('h', None)
            else: assert a.get('h'), f'Tipp fehlt: {lz}'
            if not a.get('h'): a.pop('h', None)
            if a['y'] == 'zahl': assert rechne(a['c']) == Fr(str(a['o']['wert'])), a
            out.append({'l': lz, 't': lz, 'p': pool, 's': stufe, **a})
    lz_alle = [e['lernziel'] for e in etappen]
    d = {
        'thema_schluessel': meta['thema_schluessel'], 'thema_id': meta['thema_id'], 'block_id': meta['block_id'],
        'klasse': meta['klasse'], 'autor': f'Claude (Runde 9, Generator {meta["thema_schluessel"].replace(".", "_")}.py)',
        'inhalt': {
            'ziel': ziel, 'merke': list(merke),
            'abschnitte': [{'titel': t, 'lernziele': l} for t, l in abschnitte],
            'etappen': etappen,
            'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in etappen],
            'bewertung': {'lernziele_pflicht': [x for x in lz_alle if x not in vertiefung],
                          'lernziele_vertiefung': [x for x in lz_alle if x in vertiefung], 'testaufgaben_je_lernziel': 1},
            'quellen': {'erklaerungen': 'Überlagerung inhalte/klar (Runde 7b/8), unverändert übernommen.',
                        'aufgaben': 'Vom Generator erzeugt und berechnet (Runde 9).',
                        'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern (Gymnasium).'},
        },
        'aufgaben': out,
    }
    if offen: d['offen'] = list(offen)
    THEMEN.mkdir(parents=True, exist_ok=True)
    pfad = THEMEN / f"{meta['thema_schluessel']}.json"
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{pfad.name}: {len(etappen)} Lernkarten, {len(out)} Aufgaben')
    return d
