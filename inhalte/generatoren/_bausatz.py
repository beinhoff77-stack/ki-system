#!/usr/bin/env python3
"""Gemeinsame Hilfen für die Themen-Generatoren (Werkstatt #150, Paket Klasse 8).

Enthält nur Formatierung, Aufgaben-Bausteine und den Zusammenbau einer Themen-Datei.
Jede Zahl-Aufgabe wird beim Bauen mit dem Rechner aus tools/inhalt_pruefen.py nachgerechnet;
weicht die Lösung vom Rechenausdruck "c" ab, bricht der Generator ab.
"""
import importlib.util
import json
import random
from fractions import Fraction as Fr
from pathlib import Path

HIER = Path(__file__).resolve().parent
THEMEN = HIER.parent / 'themen'
_spec = importlib.util.spec_from_file_location('inhalt_pruefen', HIER.parent.parent / 'tools' / 'inhalt_pruefen.py')
_ip = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ip)
rechne = _ip.rechne

PI = '3.141592653589793'          # π als Literal für den Rechenausdruck "c"
PIF = Fr(PI)

# Je Lernkarte: 4 + 4 + 4 Übungen (Stufe 1/2/3), 2 zusätzliche Übungen Stufe 2, 1 Test, 3 Korrektur, 6 Sicherung = 24
PLAN = [('uebung', 1)] * 4 + [('uebung', 2)] * 6 + [('uebung', 3)] * 4 + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6


# ---------- Zahlen schreiben ----------
def _gruppe(s):
    """Tausender mit Leerzeichen gliedern (ab 10 000; vierstellige bleiben zusammen)."""
    if len(s) <= 4: return s
    t = ''
    while len(s) > 3: t, s = ' ' + s[-3:] + t, s[:-3]
    return s + t


def dez(x):
    """Exakte Dezimaldarstellung eines Bruchs, falls endlich – sonst None."""
    x = Fr(x)
    n = x.denominator
    for p in (2, 5):
        while n % p == 0: n //= p
    if n != 1: return None
    neg, x = x < 0, abs(x)
    ganz = x.numerator // x.denominator
    rest = x - ganz
    nach = ''
    while rest:
        rest *= 10
        z = rest.numerator // rest.denominator
        nach += str(z)
        rest -= z
    return ('−' if neg else '') + _gruppe(str(ganz)) + (',' + nach if nach else '')


def zt(x):
    """Zahl deutsch: Minus als −, Dezimalkomma; nicht endliche Brüche als a/b."""
    if isinstance(x, float): x = Fr(str(x))
    d = dez(x)
    return d if d is not None else bruch(x)


def bruch(x):
    x = Fr(x)
    if x.denominator == 1: return zt(x.numerator)
    return ('−' if x < 0 else '') + f'{abs(x.numerator)}/{x.denominator}'


def eur(x):
    """Geldbetrag: ganze Euro ohne Komma, sonst zwei Nachkommastellen."""
    x = Fr(x)
    if x.denominator == 1: return zt(x)
    d = zt(runde(x, 2))
    k = d.split(',')
    return k[0] + ',' + (k[1] + '00')[:2] if len(k) > 1 else d + ',00'


def ca(x, stellen=2):
    """Exakt, wenn endlich – sonst „≈ gerundet“."""
    x = Fr(x)
    return zt(x) if dez(x) is not None and len(dez(x).split(',')[-1]) <= 3 else '≈ ' + zt(runde(x, stellen))


HOCH = {2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶'}


def pot(v, k):
    return v if k == 1 else f'{v}{HOCH[k]}'


def mono(c, e, v='x'):
    """Bruch c·v^e (e auch negativ) gekürzt schreiben, z. B. 2/(3x), 4x²/5, −x."""
    c = Fr(c)
    vz = '−' if c < 0 else ''
    p, q = abs(c.numerator), c.denominator
    zae = (str(p) if p != 1 or e <= 0 else '') + (pot(v, e) if e > 0 else '')
    nen = (str(q) if q != 1 else '') + (pot(v, -e) if e < 0 else '')
    if not nen: return vz + zae
    if q != 1 and e < 0: nen = f'({nen})'
    return vz + zae + '/' + nen


def einsetzen(term, x, var='x'):
    """Zahl x sichtbar in einen Term einsetzen: 3x² − x → 3 · (−2)² − (−2)."""
    v = zt(x)
    out = ''
    for i, ch in enumerate(term):
        if ch != var:
            out += ch; continue
        nach = term[i + 1:i + 2]
        vor = term[i - 1:i] if i else ''
        w = f'({v})' if (Fr(x) < 0 or (nach in HOCH.values() and vor in ('−', ''))) else v
        if vor.isdigit() or vor == ')': w = ' · ' + w
        out += w
    return out


def kl(x):
    """Negative Zahlen in Klammern."""
    s = zt(x)
    return f'({s})' if Fr(str(x) if isinstance(x, float) else x) < 0 else s


def jw(x):
    """JSON-Wert: int oder exakte endliche Dezimalzahl als float."""
    x = Fr(x)
    if x.denominator == 1: return x.numerator
    d = dez(x)
    assert d is not None, f'{x} ist keine endliche Dezimalzahl'
    f = float(d.replace('−', '-').replace(' ', '').replace(',', '.'))
    assert Fr(str(f)) == x
    return f


def cz(x):
    """Bruch als Python-Ausdruck für "c"."""
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else f'({x.numerator}/{x.denominator})'


def koeff(m, var='x', erstes=True):
    """Glied m·var lesbar: 1x -> x, −1x -> −x."""
    m = Fr(m)
    if m == 0: return ''
    b = '' if abs(m) == 1 and var else zt(abs(m))
    if var and abs(m) != 1 and dez(m) is None: b = f'({zt(abs(m))})'
    if erstes: return ('−' if m < 0 else '') + b + var
    return (' − ' if m < 0 else ' + ') + b + var


def lin(m, t, var='x'):
    """m·x + t als Text."""
    m, t = Fr(m), Fr(t)
    s = koeff(m, var) if m else ''
    if t or not s:
        s += (zt(t) if not s else (' − ' if t < 0 else ' + ') + zt(abs(t)))
    return s


def ist_endlich(x):
    return dez(x) is not None


def runde(x, stellen):
    """Rundet wie der Prüfrechner: round(float(x), n). Liefert Fraction."""
    return Fr(str(round(float(Fr(x)), stellen)))


def sicher_rundbar(x, stellen):
    """True, wenn x nicht zu nah an einer Rundungsgrenze liegt."""
    y = Fr(x) * 10 ** stellen
    r = y - (y.numerator // y.denominator)
    return abs(r - Fr(1, 2)) > Fr(1, 200)


# ---------- Aufgaben-Bausteine ----------
def Z(text, wert, c, w, h='', einheit=None):
    ist = rechne(c)
    assert ist == Fr(wert), f'Nachrechnung falsch: {c} = {ist}, Lösung {wert} ({text})'
    o = {'wert': jw(wert)}
    if einheit: o['einheit'] = einheit
    return {'y': 'zahl', 'f': {'text': text}, 'o': o, 'c': c, 'w': w, 'h': h}


def A(R, text, richtig, falsche, w, h=''):
    richtig = str(richtig)
    f = []
    for x in falsche:
        x = str(x)
        if x != richtig and x not in f: f.append(x)
    assert len(f) >= 2, f'zu wenige falsche Antworten: {text} / {richtig} / {falsche}'
    f = f[:3]
    a = f + [richtig]
    R.shuffle(a)
    return {'y': 'auswahl', 'f': {'text': text}, 'a': a, 'o': {'index': a.index(richtig)}, 'w': w, 'h': h}


def L(text, schablone, werte, c, w, h='', hinweis='Tippe den ganzen Term ein, z. B. 3x − 2.'):
    for ci, v in zip(c, werte):
        assert rechne(ci) == Fr(v), f'Lücke falsch: {ci} != {v}'
    return {'y': 'luecken', 'f': {'text': text, 'schablone': schablone, 'hinweis': hinweis},
            'o': {'werte': [int(v) for v in werte]}, 'c': list(c), 'w': w, 'h': h}


def M(text, start, ende, abschnitte, index, w, h=''):
    zahl = Fr(start) + (Fr(ende) - Fr(start)) * index / abschnitte
    return {'y': 'markierung', 'f': {'text': text, 'grafik': {'typ': 'zahlenstrahl', 'start': start, 'ende': ende,
            'abschnitte': abschnitte, 'beschriftet': 'anfang_ende'}}, 'o': {'index': index}, 'zahl': jw(zahl), 'w': w, 'h': h}


# ---------- Zusammenbau ----------
def baue(meta, etappen, gen, abschnitte, ziel, merke, offen=(), plan=PLAN, seed=0, vertiefung=()):
    R = random.Random(seed or meta['thema_id'] * 1000 + 8)
    out = []
    for e in etappen:
        lz = e['lernziel']
        gesehen = {s for s in e['schritte']}
        verbot = e.pop('_verbot', [])
        for pool, stufe in plan:
            for _ in range(3000):
                a = gen[lz](R, stufe)
                text = a['f']['text'] + '|' + '|'.join(sorted(map(str, a.get('a', [])))) + json.dumps(a['f'].get('grafik'), sort_keys=True)
                if a['f']['text'] in e['schritte'] or text in gesehen or any(v in text for v in verbot): continue
                break
            else:
                raise SystemExit(f'zu wenige Varianten für {lz} (Stufe {stufe})')
            gesehen.add(text)
            assert len(a['w']) >= 15, f'Lösungsweg zu kurz: {a}'
            if pool != 'uebung': a.pop('h', None)
            else: assert a.get('h'), f'Tipp fehlt: {lz}'
            if not a.get('h'): a.pop('h', None)
            out.append({'l': lz, 't': lz, 'p': pool, 's': stufe, **a})
    lz_alle = [e['lernziel'] for e in etappen]
    d = {
        'thema_schluessel': meta['thema_schluessel'], 'thema_id': meta['thema_id'], 'block_id': meta['block_id'],
        'klasse': meta['klasse'], 'autor': 'Claude (Paket Klasse 8)',
        'inhalt': {
            'ziel': ziel, 'merke': list(merke),
            'abschnitte': [{'titel': t, 'lernziele': l} for t, l in abschnitte],
            'etappen': etappen,
            'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in etappen],
            'bewertung': {'lernziele_pflicht': [x for x in lz_alle if x not in vertiefung],
                          'lernziele_vertiefung': [x for x in lz_alle if x in vertiefung], 'testaufgaben_je_lernziel': 1},
            'quellen': {'erklaerungen': 'Eigene Fassung (Claude).', 'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern (Gymnasium).'},
        },
        'aufgaben': out,
    }
    if offen: d['offen'] = list(offen)
    THEMEN.mkdir(parents=True, exist_ok=True)
    ziel_pfad = THEMEN / f"{meta['thema_schluessel']}.json"
    ziel_pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{ziel_pfad.name}: {len(etappen)} Lernkarten, {len(out)} Aufgaben')
    return d
