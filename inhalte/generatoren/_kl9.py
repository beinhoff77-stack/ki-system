"""Gemeinsame Hilfen für die Generatoren des Pakets Klasse 9 (Werkstatt #150).

Wird von inhalte/generatoren/<thema>.py importiert. Enthält nur Formatierung,
Auswahl-Bau und das Zusammensetzen der Themen-Datei – keine Aufgabeninhalte.
"""
import json
import math
import random
from fractions import Fraction as Fr
from pathlib import Path

HIER = Path(__file__).resolve().parent
THEMEN = HIER.parent / 'themen'
LISTE = HIER.parent / 'themenliste.json'
R = random.Random()

# Je Lernkarte: 18 Übungen (6 je Stufe), 1 Test, 3 Korrektur, 6 Sicherung = 28 Aufgaben.
PLAN = ([('uebung', 1)] * 6 + [('uebung', 2)] * 6 + [('uebung', 3)] * 6
        + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6)


def start(seed):
    R.seed(seed)


# ---------- Zahlen deutsch schreiben ----------
def _gruppe(s):
    """Ganzzahlteil ab 5 Stellen mit Leerzeichen gliedern (auch 4 Stellen, wie in der Vorlage)."""
    neg = s.startswith('-')
    s = s.lstrip('-')
    if len(s) >= 4:
        s = f'{int(s):,}'.replace(',', ' ')
    return ('−' if neg else '') + s


def dz(x):
    """Zahl als deutscher Text: int, Fraction (nur endliche Dezimalzahl) oder float."""
    if isinstance(x, Fr):
        if x.denominator == 1:
            x = int(x)
        else:
            d = x.denominator
            while d % 2 == 0: d //= 2
            while d % 5 == 0: d //= 5
            if d != 1: raise ValueError(f'{x} ist keine endliche Dezimalzahl')
            x = float(x)
    if isinstance(x, bool): raise ValueError('bool')
    if isinstance(x, int):
        return _gruppe(str(x))
    s = ('%.10f' % x).rstrip('0').rstrip('.')
    if s in ('-0', ''): s = '0'
    ganz, _, rest = s.partition('.')
    return _gruppe(ganz) + (',' + rest if rest else '')


def kl(x):
    """Negative Zahlen in Rechnungen klammern."""
    return f'({dz(x)})' if x < 0 else dz(x)


def br(x):
    """Bruch als Text, z. B. 3/4 oder −3/4; ganze Zahlen ohne Nenner."""
    x = Fr(x)
    if x.denominator == 1: return dz(int(x))
    return ('−' if x < 0 else '') + f'{abs(x.numerator)}/{x.denominator}'


def wert(x):
    """Zahl für das JSON-Feld o.wert (int oder exakte Dezimalzahl)."""
    if isinstance(x, Fr):
        if x.denominator == 1: return int(x)
        dz(x)  # wirft, wenn nicht endlich
        return float(x)
    if isinstance(x, float) and x.is_integer(): return int(x)
    return x


def endlich(x):
    """True, wenn der Bruch eine endliche Dezimalzahl ist."""
    d = Fr(x).denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    return d == 1


def K(x):
    """Konstante (z. B. Sinuswert) mit 12 Nachkommastellen für den Rechenausdruck c."""
    return format(x, '.12f')


def gerundet(wahr, nd):
    """Gerundeter Wert; None, wenn der Wert zu nah an einer Rundungsgrenze liegt."""
    t = wahr * 10 ** nd
    if abs((t - math.floor(t)) - 0.5) < 1e-6: return None
    v = round(wahr, nd)
    return int(v) if nd == 0 else v


def sin(g): return math.sin(math.radians(g))
def cos(g): return math.cos(math.radians(g))
def tan(g): return math.tan(math.radians(g))
def asin(x): return math.degrees(math.asin(x))
def acos(x): return math.degrees(math.acos(x))
def atan(x): return math.degrees(math.atan(x))


def wahl(*xs):
    return R.choice(xs)


# ---------- Bausteine für Aufgaben ----------
def zahl(text, w, h, wert_, c, einheit=None, t=None):
    a = {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': wert(wert_)}, 'c': c, 'w': w, 'h': h}
    if einheit: a['o']['einheit'] = einheit
    if t: a['t'] = t
    return a


def auswahl(text, richtig, falsche, w, h, t=None):
    richtig = str(richtig)
    opts = []
    for f in falsche:
        f = str(f)
        if f != richtig and f not in opts: opts.append(f)
    if len(opts) < 2: return None
    opts = opts[:3] + [richtig]
    R.shuffle(opts)
    a = {'y': 'auswahl', 'f': {'text': text}, 'a': opts, 'o': {'index': opts.index(richtig)}, 'w': w, 'h': h}
    if t: a['t'] = t
    return a


def luecken(text, schablone, hinweis, werte, w, h, c=None, t=None):
    a = {'y': 'luecken', 'f': {'text': text, 'schablone': schablone, 'hinweis': hinweis},
         'o': {'werte': [int(v) for v in werte]}, 'w': w, 'h': h}
    if c is not None: a['c'] = c
    if t: a['t'] = t
    return a


# ---------- Themen-Datei bauen ----------
def _schluessel(a):
    f = a['f']
    return (str(f.get('text', '')).strip() + '|' + json.dumps(a.get('a'), ensure_ascii=False) + '|'
            + json.dumps(f.get('schablone'), ensure_ascii=False) + '|' + json.dumps(f.get('grafik'), sort_keys=True))


def bauen(thema, ziel, merke, abschnitte, etappen, gen, offen=(), vertiefung=(), plan=PLAN, meiden=None):
    """meiden: {lernziel: [Textstücke]} – Aufgaben mit den Zahlen des vorgerechneten Beispiels auslassen."""
    meiden = meiden or {}
    meta = next(t for t in json.loads(LISTE.read_text(encoding='utf-8')) if t['thema_schluessel'] == thema)
    lz = [e['lernziel'] for e in etappen]
    for e in etappen:
        assert len(e['titel']) <= 40, e['titel']
    alle, gesehen = [], set()
    for e in etappen:
        beispiele = set(e['schritte'])
        for pool, stufe in plan:
            for _ in range(3000):
                a = gen[e['lernziel']](stufe)
                if a is None: continue
                k = _schluessel(a)
                if a['f']['text'].strip() in beispiele or k in gesehen: continue
                if any(m in a['f']['text'] for m in meiden.get(e['lernziel'], ())): continue
                break
            else:
                raise SystemExit(f'{thema}: zu wenige verschiedene Aufgaben für {e["lernziel"]} (Stufe {stufe})')
            gesehen.add(k)
            if pool == 'uebung':
                assert a.get('h'), f'Tipp fehlt: {e["lernziel"]}'
            else:
                a.pop('h', None)
            t = a.pop('t', None) or e['lernziel']
            alle.append({'l': e['lernziel'], 't': t, 'p': pool, 's': stufe, **a})
    datei = {
        'thema_schluessel': thema, 'thema_id': meta['thema_id'], 'block_id': meta['block_id'],
        'klasse': meta['klasse'], 'autor': 'Claude (Paket Klasse 9)',
        'inhalt': {
            'ziel': ziel,
            'merke': merke,
            'abschnitte': [{'titel': t, 'lernziele': l} for t, l in abschnitte],
            'etappen': etappen,
            'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in etappen],
            'bewertung': {'lernziele_pflicht': [x for x in lz if x not in vertiefung],
                          'lernziele_vertiefung': list(vertiefung), 'testaufgaben_je_lernziel': 1},
            'quellen': {'erklaerungen': 'Eigene Fassung (Claude), Aufgaben vom Generator erzeugt und berechnet.',
                        'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern.'},
        },
        'aufgaben': alle,
    }
    if offen: datei['offen'] = list(offen)
    ziel_pfad = THEMEN / f'{thema}.json'
    ziel_pfad.parent.mkdir(parents=True, exist_ok=True)
    ziel_pfad.write_text(json.dumps(datei, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'{ziel_pfad.name}: {len(etappen)} Lernkarten, {len(alle)} Aufgaben')
    return datei


HOCHZ = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')


def poly(*k, v='x'):
    """Polynom aus Koeffizienten (höchster Grad zuerst) als Text, z. B. poly(2, -3, 1) = '2x² − 3x + 1'."""
    n = len(k) - 1
    teile = []
    for i, c in enumerate(k):
        g = n - i
        if c == 0: continue
        c = Fr(c)
        bet = abs(c)
        if g == 0:
            zt_ = dz(bet) if endlich(bet) else br(bet)
        else:
            zt_ = '' if bet == 1 else (dz(bet) if endlich(bet) else br(bet))
            zt_ += v + ('' if g == 1 else str(g).translate(HOCHZ))
        if not teile:
            teile.append(('−' if c < 0 else '') + zt_)
        else:
            teile.append(('− ' if c < 0 else '+ ') + zt_)
    return ' '.join(teile) if teile else '0'


def plus(x):
    """'+ 3' oder '− 3' für Term-Anschlüsse"""
    return f'+ {dz(x)}' if x >= 0 else f'− {dz(-x)}'


def plus_v(c, v='x'):
    """'+ 3x', '− x' (Koeffizient vor Variable)"""
    if c == 0: return ''
    b = '' if abs(c) == 1 else dz(abs(c))
    return f'{"+" if c > 0 else "−"} {b}{v}'


def minus_klammer(p, v='x'):
    """(x − p) bzw. (x + |p|)"""
    if p == 0: return v
    return f'({v} − {dz(p)})' if p > 0 else f'({v} + {dz(-p)})'
