"""Gemeinsame Hilfen für die Themen-Generatoren Paket Klasse 5 Rest (Werkstatt #150).

Einbinden im Generator (funktioniert auch mit python3 -I):
    import sys; from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _kl5_rest import *
"""
import json
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

__all__ = ['Fr', 'gcd', 'hoch', 'zt', 'kl', 'wert', 'bruch', 'wahl', 'PLAN', 'aufgaben', 'datei', 'schreibe', 'ja_nein']

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


# Je Lernkarte: 18 Übungen (6 je Stufe), 1 Test, 3 Korrektur, 6 Sicherung = 28 Aufgaben, alle verschieden.
PLAN = [('uebung', 1)] * 6 + [('uebung', 2)] * 6 + [('uebung', 3)] * 6 + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6


def aufgaben(etappen, gen, plan=PLAN, versuche=3000):
    out = []
    gesehen = {s for e in etappen for s in e['schritte']}   # Dubletten über das ganze Thema
    for e in etappen:
        for pool, stufe in plan:
            for _ in range(versuche):
                a = gen[e['lernziel']](stufe)
                schl = a['f']['text'] + json.dumps(a['f'].get('grafik'), sort_keys=True)
                if schl not in gesehen and a['f']['text'] not in gesehen: break
            else:
                raise SystemExit(f'zu wenige Varianten für {e["lernziel"]} (Stufe {stufe})')
            gesehen.add(schl)
            assert a.get('h') and a.get('w'), (e['lernziel'], a)
            if pool != 'uebung': a.pop('h', None)
            out.append({'l': e['lernziel'], 't': e['lernziel'], 'p': pool, 's': stufe, **a})
    return out


def datei(eintrag, ziel, merke, abschnitte, etappen, gen, vertiefung=(), offen=()):
    lz = [e['lernziel'] for e in etappen]
    d = {
        'thema_schluessel': eintrag['thema_schluessel'], 'thema_id': eintrag['thema_id'], 'block_id': eintrag['block_id'],
        'klasse': eintrag['klasse'], 'autor': 'Claude (Opus), Paket Klasse 5 Rest',
        'inhalt': {
            'ziel': ziel, 'merke': merke,
            'abschnitte': [{'titel': t, 'lernziele': l} for t, l in abschnitte],
            'etappen': etappen,
            'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in etappen],
            'bewertung': {'lernziele_pflicht': [x for x in lz if x not in vertiefung],
                          'lernziele_vertiefung': list(vertiefung), 'testaufgaben_je_lernziel': 1},
            'quellen': {'erklaerungen': 'Eigene Fassung (Claude), alle Aufgaben programmgeneriert.',
                        'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern (Gymnasium, Jahrgangsstufe 5).'},
        },
        'aufgaben': aufgaben(etappen, gen),
    }
    if offen: d['offen'] = list(offen)
    return d


def eintrag_laden(schluessel):
    liste = json.loads((Path(__file__).resolve().parent.parent / 'themenliste.json').read_text(encoding='utf-8'))
    return next(e for e in liste if e['thema_schluessel'] == schluessel)


__all__.append('eintrag_laden')


def luecke(werte, text, schablone, hinweis, c, w, h):
    """Lücken-Aufgabe (je Lücke ein Zahlenfeld, ganze Zahlen, auch negativ)."""
    assert schablone.count('□') == len(werte) == len(c)
    assert all(isinstance(v, int) for v in werte)
    return {'y': 'luecken', 'f': {'text': text, 'schablone': schablone, 'hinweis': hinweis}, 'o': {'werte': list(werte)}, 'c': list(c), 'w': w, 'h': h}


def punkt(name, x, y, text, w, h, cx=None, cy=None):
    """Punkt als Lücken-Antwort: P(□ | □)."""
    return luecke([x, y], text, f'{name}(□ | □)', 'Erst die x-Koordinate, dann die y-Koordinate.', [cx or str(x), cy or str(y)], w, h)


__all__ += ['luecke', 'punkt']


def schreibe(d):
    ziel = Path(__file__).resolve().parent.parent / 'themen' / f'{d["thema_schluessel"]}.json'
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{ziel.name}: {len(d["inhalt"]["etappen"])} Lernkarten, {len(d["aufgaben"])} Aufgaben')
