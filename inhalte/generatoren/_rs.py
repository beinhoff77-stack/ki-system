"""Gemeinsame Hilfen für die Generatoren des Pakets Realschule (Werkstatt #150, vierte Runde).

Wird von inhalte/generatoren/<thema>.py importiert. Enthält nur Formatierung,
Auswahl-Bau und das Zusammensetzen der Themen-Datei – keine Aufgabeninhalte.
"""
import importlib.util
import json
import math
import random
from fractions import Fraction as Fr
from pathlib import Path

HIER = Path(__file__).resolve().parent
THEMEN = HIER.parent / 'themen'
LISTE = HIER.parent / 'themenliste.json'
R = random.Random()
_spec = importlib.util.spec_from_file_location('inhalt_pruefen', HIER.parent.parent / 'tools' / 'inhalt_pruefen.py')
_ip = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ip)
rechne = _ip.rechne
POS = __import__('collections').Counter()

# Je Lernkarte: 18 Übungen (6 je Stufe), 1 Test, 3 Korrektur, 6 Sicherung = 28 Aufgaben.
PLAN = ([('uebung', 1)] * 6 + [('uebung', 2)] * 6 + [('uebung', 3)] * 6
        + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6)


def start(seed):
    R.seed(seed)
    POS.clear()


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
def _toleranz(c):
    """Aus 'round(…, n)' am Ende des Rechenausdrucks die Toleranz (eine Einheit der letzten Stelle) ableiten."""
    import re
    m = re.search(r',\s*(\d+)\)\s*$', c) if c.lstrip().startswith('round(') else None
    if not m: return None
    n = int(m.group(1))
    return 1 if n == 0 else float('0.' + '0' * (n - 1) + '1')


def zahl(text, w, h, wert_, c, einheit=None, t=None, toleranz=None, grafik=None):
    a = {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': wert(wert_)}, 'c': c, 'w': w, 'h': h}
    if einheit: a['o']['einheit'] = einheit
    tol = toleranz if toleranz is not None else _toleranz(c)
    if tol is not None: a['o']['toleranz'] = tol
    if grafik: a['f']['grafik'] = grafik
    if t: a['t'] = t
    return a


def bild(a, g):
    """Grafik an eine Aufgabe hängen (None bleibt None)."""
    if a is not None and g: a['f']['grafik'] = g
    return a


def auswahl(text, richtig, falsche, w, h, t=None):
    richtig = str(richtig)
    opts = []
    for f in falsche:
        f = str(f)
        if f != richtig and f not in opts: opts.append(f)
    if len(opts) < 2: return None
    opts = opts[:3]
    R.shuffle(opts)
    n = len(opts) + 1
    frei = [i for i in range(n) if POS[(n, i)] == min(POS[(n, j)] for j in range(n))]
    i = R.choice(frei)
    POS[(n, i)] += 1
    opts.insert(i, richtig)
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
def _nachrechnen(a):
    if 'c' not in a: 
        assert a['y'] not in ('zahl',), f'c fehlt: {a["f"]["text"]}'
        return
    if a['y'] == 'luecken':
        ist = [rechne(c) for c in a['c']]
        assert ist == [Fr(v) for v in a['o']['werte']], f'Lücken falsch: {a["f"]["text"]} {ist} {a["o"]["werte"]}'
    elif a['y'] == 'zahl':
        assert rechne(a['c']) == Fr(str(a['o']['wert'])), f'Zahl falsch: {a["f"]["text"]} {a["c"]} = {rechne(a["c"])} ≠ {a["o"]["wert"]}'



def _schluessel(a):
    f = a['f']
    return (str(f.get('text', '')).strip() + '|' + json.dumps(sorted(a.get('a') or []), ensure_ascii=False) + '|'
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
            _nachrechnen(a)
            if pool == 'uebung':
                assert a.get('h'), f'Tipp fehlt: {e["lernziel"]}'
            else:
                a.pop('h', None)
            t = a.pop('t', None) or e['lernziel']
            alle.append({'l': e['lernziel'], 't': t, 'p': pool, 's': stufe, **a})
    datei = {
        'thema_schluessel': thema, 'thema_id': meta['thema_id'], 'block_id': meta['block_id'],
        'klasse': meta['klasse'], 'autor': 'Claude (Paket Realschule)',
        'inhalt': {
            'ziel': ziel,
            'merke': merke,
            'abschnitte': [{'titel': t, 'lernziele': l} for t, l in abschnitte],
            'etappen': etappen,
            'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in etappen],
            'bewertung': {'lernziele_pflicht': [x for x in lz if x not in vertiefung],
                          'lernziele_vertiefung': list(vertiefung), 'testaufgaben_je_lernziel': 1},
            'quellen': {'erklaerungen': 'Eigene Fassung (Claude), Aufgaben vom Generator erzeugt und berechnet.',
                        'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern (Realschule, Wahlpflichtfächergruppe I).'},
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


# ---------- Punkte, Vektoren, Vielecke (Geometrie Realschule) ----------
def vek(x, y):
    """Vektor als Text: (3 | −2)"""
    return f'({dz(x)} | {dz(y)})'


def pkt(n, x, y):
    """Punkt als Text: A(3 | −2)"""
    return f'{n}({dz(x)} | {dz(y)})'


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def det_text(a, b):
    """Rechnung 'über Kreuz': 3 · 4 − 1 · (−2)"""
    return f'{kl(a[0])} · {kl(b[1])} − {kl(a[1])} · {kl(b[0])}'


def det_c(a, b):
    return f'({a[0]}) * ({b[1]}) - ({a[1]}) * ({b[0]})'


def konvex_gegen_uhr(punkte):
    """True, wenn die Punkte ein echtes konvexes Vieleck gegen den Uhrzeigersinn bilden."""
    n = len(punkte)
    for i in range(n):
        p, q, r = punkte[i], punkte[(i + 1) % n], punkte[(i + 2) % n]
        if det((q[0] - p[0], q[1] - p[1]), (r[0] - q[0], r[1] - q[1])) <= 0: return False
    return True


def zufalls_vieleck(n, lo=-5, hi=6, start_null=False):
    """Konvexes n-Eck mit ganzzahligen Ecken, gegen den Uhrzeigersinn, erste Ecke unten links."""
    for _ in range(5000):
        ps = [(R.randint(lo, hi), R.randint(lo, hi)) for _ in range(n)]
        if len(set(ps)) < n: continue
        cx = sum(p[0] for p in ps) / n; cy = sum(p[1] for p in ps) / n
        ps.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
        if not konvex_gegen_uhr(ps): continue
        k = min(range(n), key=lambda i: (ps[i][1] + ps[i][0], ps[i][0]))
        ps = ps[k:] + ps[:k]
        if start_null:
            ax, ay = ps[0]
            ps = [(x - ax, y - ay) for x, y in ps]
        return ps
    raise SystemExit('kein Vieleck gefunden')


def koord_bild(punkte, namen, geschlossen=True, extra=None):
    """Koordinatensystem mit benannten Punkten und Verbindungsstrecken."""
    xs = [p[0] for p in punkte] + [0]; ys = [p[1] for p in punkte] + [0]
    b = {'typ': 'koordinaten', 'x': [min(xs) - 1, max(xs) + 1], 'y': [min(ys) - 1, max(ys) + 1], 'schritt_x': 1, 'schritt_y': 1,
         'punkte': [{'x': p[0], 'y': p[1], 'name': n} for p, n in zip(punkte, namen)],
         'strecken': [[punkte[i][0], punkte[i][1], punkte[(i + 1) % len(punkte)][0], punkte[(i + 1) % len(punkte)][1]]
                      for i in range(len(punkte) if geschlossen else len(punkte) - 1)]}
    if extra: b['strecken'] += extra
    return b


def cz(x):
    """Bruch als Python-Ausdruck für "c"."""
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else f'({x.numerator}/{x.denominator})'
