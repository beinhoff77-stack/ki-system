"""Gemeinsame Hilfen für die Themen-Generatoren Klasse 6 (Werkstatt #150).

Einbinden im Generator (funktioniert auch mit python3 -I):
    import sys; from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _basis import *
"""
import json
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

__all__ = ['Fr', 'gcd', 'hoch', 'zt', 'kl', 'wert', 'bruch', 'wahl', 'PLAN', 'aufgaben', 'datei', 'schreibe', 'ja_nein',
           'streifen', 'raster', 'kreisteile', 'saeulen', 'kreisdiagramm', 'tabelle']

_HOCH = str.maketrans('0123456789-', '⁰¹²³⁴⁵⁶⁷⁸⁹⁻')


def hoch(n):
    """Exponent hochgestellt: 3 -> ³, -4 -> ⁻⁴."""
    return str(n).translate(_HOCH)


def _fr(x):
    if isinstance(x, Fr): return x
    if isinstance(x, float): return Fr(str(x))
    return Fr(x)


def zt(x):
    """Zahl deutsch schreiben: Minus −, Tausender mit Leerzeichen, Dezimalkomma. Nur endliche Dezimalzahlen."""
    x = _fr(x)
    neg, x = x < 0, abs(x)
    k = 0
    while (x * 10 ** k).denominator != 1:
        k += 1
        if k > 15: raise ValueError(f'{x} ist keine endliche Dezimalzahl')
    n = int(x * 10 ** k)
    ganz, nach = divmod(n, 10 ** k)
    s = f'{ganz:,}'.replace(',', ' ')
    if k: s += ',' + str(nach).rjust(k, '0')
    return ('−' if neg else '') + s


def kl(x):
    """Negative Zahl in Klammern."""
    return f'({zt(x)})' if _fr(x) < 0 else zt(x)


def wert(x):
    """Lösungswert für o.wert: int oder exakte Dezimalzahl als float."""
    x = _fr(x)
    if x.denominator == 1: return int(x)
    zt(x)  # prüft: endlich
    f = float(x)
    assert Fr(str(f)) == x, x
    return f


def bruch(x):
    """Bruch als Text, z. B. 3/4, −5/2, 7 (ganz)."""
    x = _fr(x)
    if x.denominator == 1: return zt(x.numerator)
    return ('−' if x < 0 else '') + f'{abs(x.numerator)}/{x.denominator}'


def wahl(R, richtig, falsche, n=4):
    """Auswahl-Aufgabe: richtige Antwort + Fehlantworten (aus typischen Fehlern), gemischt."""
    opts = [richtig]
    for f in falsche:
        if f not in opts: opts.append(f)
        if len(opts) == n: break
    if len(opts) < 3: raise ValueError(f'zu wenige verschiedene Antworten: {opts}')
    R.shuffle(opts)
    return {'y': 'auswahl', 'a': opts, 'o': {'index': opts.index(richtig)}}


def ja_nein(R, stimmt, grund_ja, grund_nein, extra):
    """Aussage beurteilen: 3 Antworten, eine davon richtig."""
    richtig = grund_ja if stimmt else grund_nein
    falsch = [grund_nein if stimmt else grund_ja, extra]
    return wahl(R, richtig, falsch, 3)


# ---------- Zeichnungen (Format: inhalte/README.md, Abschnitt „Zeichnungen“) ----------
def _r(x): return round(x, 4)


def streifen(n, k, unten=None, oben=None, dx=1.5, label=None):
    """Streifen (Rechteck) in n gleiche Teile, die ersten k gefärbt. unten/oben: Beschriftung ganzer Streifen / gefärbter Teil."""
    P = {}
    for i in range(n + 1):
        P[f'_{i}_0'] = [_r(i * dx), 0.0]; P[f'_{i}_1'] = [_r(i * dx), 1.0]
    L = [[f'_{i}_0', f'_{i}_1'] for i in range(n + 1)] + [['_0_0', f'_{n}_0'], ['_0_1', f'_{n}_1']]
    if unten: L.append(['_0_0', f'_{n}_0', unten])
    if oben: L.append(['_0_1', f'_{k}_1', oben])
    b = {'typ': 'figur', 'punkte': P, 'linien': L}
    if k: b['flaeche'] = ['_0_0', f'_{k}_0', f'_{k}_1', '_0_1']
    if label: b['label'] = label
    return b


def raster(sp, ze, k, label=None):
    """Rechteck aus sp Spalten und ze Zeilen gleicher Kästchen; k Kästchen gefärbt (spaltenweise von links, von unten)."""
    P = {}
    for i in range(sp + 1):
        P[f'_{i}_0'] = [float(i), 0.0]; P[f'_{i}_{ze}'] = [float(i), float(ze)]
    for j in range(1, ze):
        P[f'_0_{j}'] = [0.0, float(j)]; P[f'_{sp}_{j}'] = [float(sp), float(j)]
    L = [[f'_{i}_0', f'_{i}_{ze}'] for i in range(sp + 1)] + [[f'_0_{j}', f'_{sp}_{j}'] for j in range(ze + 1)]
    b = {'typ': 'figur', 'punkte': P, 'linien': L}
    c, r = divmod(k, ze)
    if k:
        if r == 0:
            b['flaeche'] = ['_0_0', f'_{c}_0', f'_{c}_{ze}', f'_0_{ze}']
        else:
            P['_t1'] = [float(c + 1), 0.0]; P['_t2'] = [float(c + 1), float(r)]; P['_t3'] = [float(c), float(r)]
            b['flaeche'] = ['_0_0', '_t1', '_t2', '_t3'] + ([f'_{c}_{ze}', f'_0_{ze}'] if c else [])
    if label: b['label'] = label
    return b


def kreisteile(n, k, label=None):
    """Kreis in n gleiche Teile (Tortenstücke), die ersten k ab 12 Uhr im Uhrzeigersinn gefärbt."""
    from math import cos, sin, pi
    P = {'_M': [0.0, 0.0]}
    for i in range(n):
        a = pi / 2 - 2 * pi * i / n
        P[f'_r{i}'] = [_r(cos(a)), _r(sin(a))]
    L = [['_M', f'_r{i}'] for i in range(n)] if n > 1 else []
    b = {'typ': 'figur', 'punkte': P, 'linien': L, 'kreise': [{'m': '_M', 'r': 1}]}
    if k:
        fl, m = ['_M'], 8 * k
        for j in range(m + 1):
            a = pi / 2 - 2 * pi * (k / n) * j / m
            P[f'_b{j}'] = [_r(cos(a)), _r(sin(a))]; fl.append(f'_b{j}')
        b['flaeche'] = fl
    if label: b['label'] = label
    return b


def saeulen(werte, einheit=None, zahlen=True, y_start=None):
    b = {'typ': 'saeulen', 'werte': [{'name': n, 'wert': w} for n, w in werte], 'zahlen': zahlen}
    if einheit: b['einheit'] = einheit
    if y_start is not None: b['y_start'] = y_start
    return b


def kreisdiagramm(werte, einheit=None, zahlen=True):
    b = {'typ': 'kreisdiagramm', 'werte': [{'name': n, 'wert': w} for n, w in werte], 'zahlen': zahlen}
    if einheit: b['einheit'] = einheit
    return b


def tabelle(kopf, zeilen):
    return {'typ': 'tabelle', 'kopf': [str(k) for k in kopf], 'zeilen': [[str(c) for c in z] for z in zeilen]}


# Je Lernkarte: 18 Übungen (6 je Stufe), 1 Test, 3 Korrektur, 6 Sicherung = 28 Aufgaben, alle verschieden.
PLAN = [('uebung', 1)] * 6 + [('uebung', 2)] * 6 + [('uebung', 3)] * 6 + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6


def _schluessel(a):
    """Themenweit eindeutig: gleicher Fragetext nur mit anderem Bild oder anderer Schablone (Antwort-Reihenfolge zählt nicht)."""
    f = a['f']
    return f['text'].strip() + '|' + json.dumps(f.get('schablone'), ensure_ascii=False) + '|' + json.dumps(f.get('grafik'), sort_keys=True)


def aufgaben(etappen, gen, plan=PLAN, versuche=3000):
    out, alle = [], set()
    for e in etappen:
        beispiele = set(e['schritte'])
        for pool, stufe in plan:
            for _ in range(versuche):
                a = gen[e['lernziel']](stufe)
                if a['f']['text'] in beispiele: continue
                schl = _schluessel(a)
                if schl not in alle: break
            else:
                raise SystemExit(f'zu wenige Varianten für {e["lernziel"]} (Stufe {stufe})')
            alle.add(schl)
            assert a.get('h') and a.get('w'), (e['lernziel'], a)
            if pool != 'uebung': a.pop('h', None)
            out.append({'l': e['lernziel'], 't': e['lernziel'], 'p': pool, 's': stufe, **a})
    return out


def datei(eintrag, ziel, merke, abschnitte, etappen, gen, vertiefung=(), offen=()):
    lz = [e['lernziel'] for e in etappen]
    d = {
        'thema_schluessel': eintrag['thema_schluessel'], 'thema_id': eintrag['thema_id'], 'block_id': eintrag['block_id'],
        'klasse': eintrag['klasse'], 'autor': 'Claude (Opus), Paket Klasse 6',
        'inhalt': {
            'ziel': ziel, 'merke': merke,
            'abschnitte': [{'titel': t, 'lernziele': l} for t, l in abschnitte],
            'etappen': etappen,
            'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in etappen],
            'bewertung': {'lernziele_pflicht': [x for x in lz if x not in vertiefung],
                          'lernziele_vertiefung': list(vertiefung), 'testaufgaben_je_lernziel': 1},
            'quellen': {'erklaerungen': 'Eigene Fassung (Claude), alle Aufgaben programmgeneriert.',
                        'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern (Gymnasium, Jahrgangsstufe 6).'},
        },
        'aufgaben': aufgaben(etappen, gen),
    }
    if offen: d['offen'] = list(offen)
    return d


def eintrag_laden(schluessel):
    liste = json.loads((Path(__file__).resolve().parent.parent / 'themenliste.json').read_text(encoding='utf-8'))
    return next(e for e in liste if e['thema_schluessel'] == schluessel)


__all__.append('eintrag_laden')


def schreibe(d):
    ziel = Path(__file__).resolve().parent.parent / 'themen' / f'{d["thema_schluessel"]}.json'
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{ziel.name}: {len(d["inhalt"]["etappen"])} Lernkarten, {len(d["aufgaben"])} Aufgaben')
