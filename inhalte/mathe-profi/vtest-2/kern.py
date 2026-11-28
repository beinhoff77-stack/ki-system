"""Bauhilfe Runde 2 (VT2): erzeugt die Aufgaben-JSON je Einheit. Keine Lerndaten, keine Namen echter Personen."""
import json
import re
from pathlib import Path

HIER = Path(__file__).resolve().parent
WURZEL = HIER.parent.parent.parent
RBL = json.loads((WURZEL / 'inhalte/plan/regelbezug-lernkarten.json').read_text(encoding='utf-8'))['themen']
LERNBEREICH = {'finanzen.zinsen': 'M6 3', 'terme.umformen': 'M7 1', 'terme.umformen_teil2': 'M7 1', 'geometrie.kreis': 'M7 5', 'zahlen.natuerlich': 'M5 1'}
KLASSE = {'finanzen.zinsen': 6, 'terme.umformen': 7, 'terme.umformen_teil2': 7, 'geometrie.kreis': 7, 'zahlen.natuerlich': 5}
ZAEHLER = [0]
ERGEBNIS = {}          # einheit -> [Eintrag]
_AKT = {}


def einheit(schluessel):
    _AKT['s'] = schluessel
    ERGEBNIS.setdefault(schluessel, [])


def basis(s):
    return re.sub(r'_teil\d+$', '', s)


def _kopf(lz, pool, typ, form, stufe, lp, abgr, y, fb, loesung=None, runden=None, regel=None):
    s = _AKT['s']
    ZAEHLER[0] += 1
    lk = (RBL.get(basis(s)) or {}).get('lernkarten', {}).get(lz) or {}
    x = {'kennung': f'VT2-{ZAEHLER[0]:03d}', 'thema': s, 'lernkarte': lz, 'pool': pool}
    if pool == 'test': x['ersetzt_test'] = True
    x.update({'typ': typ, 'form': form, 'stufe': stufe, 'zaehlt': 'ja', 'lehrplan': lp})
    r = regel or lk.get('regel')
    if r: x['regel'] = r
    x['abgrenzung'] = abgr
    x['antwortform'] = y
    if loesung is not None: x['loesung_rechnung'] = loesung
    if runden is not None: x['runden'] = runden
    x['fehlbilder'] = fb
    return x


def _fertig(x, lz, pool, stufe, typ, y, f, o, w, opts=None):
    a = {'l': lz, 't': lz, 'p': pool, 's': stufe, 'g': typ, 'y': y, 'f': f}
    if opts is not None: a['a'] = opts
    a['o'] = o
    a['w'] = w
    x['aufgabe'] = a
    ERGEBNIS[_AKT['s']].append(x)
    return x


def fmt(w):
    return str(w)


def Z(lz, pool, typ, form, stufe, lp, text, wert, rech, fb, w, abgr, einheit_=None, runden=None):
    """zahl. fb = [(antwort, rechnung, beschreibung)]"""
    fbl = [{'antwort': a, 'rechnung': r, 'beschreibung': b, 'fehlbild': None, 'regel_des_fehlbilds': None} for a, r, b in fb]
    x = _kopf(lz, pool, typ, form, stufe, lp, abgr, 'zahl', fbl, loesung=rech, runden=runden)
    o = {'wert': wert}
    if einheit_: o['einheit'] = einheit_
    return _fertig(x, lz, pool, stufe, typ, 'zahl', {'text': text}, o, w)


def L(lz, pool, typ, form, stufe, lp, text, schablone, werte, rechs, fb, w, abgr, hinweis='Je Feld eine ganze Zahl.'):
    """luecken. fb = [(luecke(1-basiert), antwort, rechnung, beschreibung)]"""
    fbl = [{'luecke': l, 'antwort': a, 'rechnung': r, 'beschreibung': b, 'fehlbild': None, 'regel_des_fehlbilds': None} for l, a, r, b in fb]
    x = _kopf(lz, pool, typ, form, stufe, lp, abgr, 'luecken', fbl, loesung=rechs)
    f = {'text': text, 'schablone': schablone, 'hinweis': hinweis}
    return _fertig(x, lz, pool, stufe, typ, 'luecken', f, {'werte': werte}, w)


MUSTER = [0, 1, 2, 0, 1, 3, 2, 0, 3, 1, 0, 1, 3, 2]   # Zielplatz der richtigen Möglichkeit (verteilt die Lösung auf alle vier Plätze)
_AUSW = [0]


def A(lz, pool, typ, form, stufe, lp, text, opts, idx, fb, w, abgr, fest=False):
    """auswahl. fb = {index: beschreibung} oder {index: (beschreibung, rechnung)} (Index = Platz in der angegebenen Reihenfolge).
    fest=True: Reihenfolge der Möglichkeiten bleibt (geordnete Zahlen, A-D); sonst werden sie gemischt und die richtige auf einen
    reihum vorgegebenen Platz gesetzt (kein Platz ist auffällig häufig richtig)."""
    opts = list(opts)
    if not fest:
        import random
        rng = random.Random(ZAEHLER[0] + 1)
        ziel = MUSTER[_AUSW[0] % len(MUSTER)]
        _AUSW[0] += 1
        rest = [i for i in range(len(opts)) if i != idx]
        rng.shuffle(rest)
        neu = rest[:ziel] + [idx] + rest[ziel:]       # neu[p] = alter Index auf Platz p
        opts = [opts[i] for i in neu]
        fb = {neu.index(i): v for i, v in fb.items()}
        idx = ziel
    fbl = []
    for i in range(len(opts)):
        if i == idx: continue
        v = fb[i]
        b, r = (v, None) if isinstance(v, str) else v
        e = {'index': i, 'antwort': opts[i], 'beschreibung': b, 'fehlbild': None, 'regel_des_fehlbilds': None}
        if r is not None: e['rechnung'] = r
        fbl.append(e)
    x = _kopf(lz, pool, typ, form, stufe, lp, abgr, 'auswahl', fbl)
    return _fertig(x, lz, pool, stufe, typ, 'auswahl', {'text': text}, {'index': idx}, w, opts=opts)


def schreiben():
    from ideen import IDEEN
    for s, xs in ERGEBNIS.items():
        for x in xs:
            x['idee'] = IDEEN[int(x['kennung'].split('-')[1])]
        d = {'stand': '2026-11-28', 'runde': 'vtest-2', 'kuerzel': 'VT2', 'titel': s, 'klasse': KLASSE[s], 'themen': [s],
             'hinweis': 'Verstehen in Tests, Stufe 1. Nicht eingespielt.', 'aufgaben': xs}
        (HIER / f'{s}.json').write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
