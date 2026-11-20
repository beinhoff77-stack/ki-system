#!/usr/bin/env python3
"""Gemeinsame Hilfen der Achtzehnten Runde, Teil A (Zweig luecken-neu): messen.flaechen_vielecke, messen.volumen, messen.prisma_zylinder.

Enthält: Aufgaben-Bausteine (Z, A, L) mit Nachrechnung, Zeichnungen (Vielecke, Schrägbilder von Prismen und Zylindern, Netze),
eine Maßstabsprüfung (angeschriebene Längen = gezeichnete Längen, Tiefenkanten im Schrägbild halb so lang unter 45°)
und den Zusammenbau einer Themen-Datei mit 18 Übungen (4/6/8), 1 Test, 3 Korrektur, 6 Sicherung je Lernkarte.
"""
import collections
import json
import math
import re
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.dont_write_bytecode = True
HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
from _bausatz import PI, jw, rechne, runde, zt  # noqa: E402,F401

P, K = 'pruefung', 'knobel'
ARTEN = {}  # Fragetext → Art (pruefung/knobel); nur zum Nachschlagen für die Zwanzigste Runde, ändert keine Ausgabe
PLAN = [('uebung', 1)] * 4 + [('uebung', 2)] * 6 + [('uebung', 3)] * 8 + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6


# ---------- Zahlen und Einheiten ----------
def z(x):
    """Zahl deutsch, auch Tausender ab 1 000 mit Leerzeichen."""
    x = Fr(x) if not isinstance(x, Fr) else x
    t = zt(x)
    ganz = t.split(',')[0].replace('−', '')
    if len(ganz) == 4 and ' ' not in ganz:
        t = t.replace(ganz, ganz[0] + ' ' + ganz[1:], 1)
    return t


def gr(x, e):
    """Größe: Zahl + Einheit."""
    return f'{z(x)} {e}'


def d(x):
    """Dezimalzahl als Python-Literal für "c"."""
    x = Fr(x)
    if x.denominator == 1: return str(x.numerator)
    return repr(jw(x))


# ---------- Aufgaben-Bausteine ----------
_POS = collections.Counter()
_WAHL = collections.Counter()


def Z(text, wert, c, w, h='', einheit=None, art=None, grafik=None, toleranz=None):
    ist = rechne(c)
    assert ist == Fr(wert), f'Nachrechnung falsch: {c} = {ist}, Lösung {wert} ({text})'
    a = {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': jw(Fr(wert))}, 'c': c, 'w': w, 'h': h}
    if einheit: a['o']['einheit'] = einheit
    if toleranz is not None: a['o']['toleranz'] = toleranz
    if grafik: a['f']['grafik'] = grafik
    if art: a['_art'] = art; ARTEN[a['f']['text']] = art
    return a


def A(R, text, richtig, falsche, w, h='', art=None, grafik=None):
    richtig = str(richtig)
    f = []
    for x in map(str, falsche):
        if x != richtig and x not in f: f.append(x)
    assert len(f) >= 2, (text, f)
    f = f[:3]
    R.shuffle(f)
    n = len(f) + 1
    frei = [i for i in range(n) if _POS[(n, i)] == min(_POS[(n, j)] for j in range(n))]
    i = R.choice(frei)
    _POS[(n, i)] += 1
    f.insert(i, richtig)
    a = {'y': 'auswahl', 'f': {'text': text}, 'a': f, 'o': {'index': i}, 'w': w, 'h': h}
    if grafik: a['f']['grafik'] = grafik
    if art: a['_art'] = art; ARTEN[a['f']['text']] = art
    return a


def L(text, schablone, werte, c, w, h, hinweis, art=None, grafik=None):
    for ci, v in zip(c, werte): assert rechne(ci) == Fr(v), (ci, v)
    a = {'y': 'luecken', 'f': {'text': text, 'schablone': schablone, 'hinweis': hinweis}, 'o': {'werte': [int(v) for v in werte]}, 'c': list(c), 'w': w, 'h': h}
    if grafik: a['f']['grafik'] = grafik
    if art: a['_art'] = art; ARTEN[a['f']['text']] = art
    return a


def wahl(R, schluessel, arten):
    """Abwechslung: wählt zufällig unter den bisher am seltensten gewählten Arten."""
    m = min(_WAHL[(schluessel, x)] for x in arten)
    art = R.choice([x for x in arten if _WAHL[(schluessel, x)] == m])
    _WAHL[(schluessel, art)] += 1
    return art


def toleranz_pi(wert, stellen=0):
    """Toleranz bei π-Aufgaben: eine Einheit der letzten Stelle, mindestens so viel, wie π ≈ 3,14 statt π-Taste ausmacht."""
    t = Fr(1, 10 ** stellen)
    while abs(Fr(wert)) * Fr(6, 10000) > t: t *= 2
    return jw(t)


# ---------- Zeichnungen ----------
def _r(v):
    return round(float(v), 3)


def fig(punkte, linien, flaeche=None, rechte=None, kreise=None, winkel=None):
    f = {'typ': 'figur', 'punkte': {k: [_r(p[0]), _r(p[1])] for k, p in punkte.items()}, 'linien': [list(x) for x in linien]}
    if flaeche: f['flaeche'] = list(flaeche)
    if rechte: f['rechter_winkel'] = [list(x) for x in rechte]
    if kreise: f['kreise'] = kreise
    if winkel: f['winkel'] = winkel
    return f


def L_(wert, e, name=None):
    """Beschriftung einer Strecke: „g = 6 cm“ oder „6 cm“."""
    return f'{name} = {gr(wert, e)}' if name else gr(wert, e)


def _lab(w, e, name):
    """Beschriftung: None → leer; kurzer Name (g, h, a, c) → „g = 6 cm“; sonst eigener Text."""
    if name is None: return ''
    return L_(w, e, name) if len(name) <= 2 else name


ZEICHEN_BREITE = 8.6   # Breite eines Zeichens der Beschriftung in Bildpunkten (Bild 340 breit, Ränder 72)


def _skala(punkte):
    xs = [float(p[0]) for p in punkte.values()]; ys = [float(p[1]) for p in punkte.values()]
    return min(196 / max(max(xs) - min(xs), 1e-9), 220 / max(max(ys) - min(ys), 1e-9))


def _rand(poly, y):
    """x-Werte, an denen die waagrechte Linie in Höhe y die Seiten des Vielecks schneidet."""
    xs = []
    n = len(poly)
    for i in range(n):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % n]
        if (y1 - y) * (y2 - y) < 0 or (y1 == y and y2 != y):
            xs.append(x1 + (x2 - x1) * (y - y1) / (y2 - y1) if y2 != y1 else x1)
    return sorted(xs)


def hoehe_text(pk, lin, x, y0, y1, text, poly):
    """Senkrechte Höhe von (x|y0) nach (x|y1), gestrichelt. Die Beschriftung steht frei neben der Höhe (Hilfspunkt _ht mit Strecke der Länge 0),
    auf der Seite mit mehr Platz im Vieleck, damit sie keine Seite überdeckt. Passt die volle Beschriftung nicht, steht nur „h“ da."""
    x, y0, y1 = float(x), float(y0), float(y1)
    pk['_F'], pk['_H'] = (x, y0), (x, y1)
    lin.append(['_F', '_H', '', 'gestrichelt'])
    if not text: return
    f = _skala({**pk})
    ym = (y0 + y1) / 2
    xs = [float(v) for v in _rand([tuple(map(float, p)) for p in poly], ym)]
    xl = max([v for v in xs if v < x - 1e-9] or [x - 99]); xr = min([v for v in xs if v > x + 1e-9] or [x + 99])
    xs_alle = [float(p[0]) for p in pk.values()]
    xr = min(xr, max(xs_alle) + 64 / f); xl = max(xl, min(xs_alle) - 64 / f)     # Text muss im Bild bleiben (Rand 72 Bildpunkte)
    for t in (text, text.split(' =')[0]):
        w = (len(t) * ZEICHEN_BREITE + 8) / f
        rechts, links = xr - x, x - xl
        if rechts >= w + 6 / f or links >= w + 6 / f:
            seite = 1 if rechts >= w + 6 / f else -1
            pk['_ht'] = (x + seite * (w / 2 + 5 / f), ym)
            lin.append(['_ht', '_ht', t, 'gestrichelt'])
            return
    pk['_ht'] = (x + (w / 2 + 5 / f) * (1 if xr - x >= x - xl else -1), ym)
    lin.append(['_ht', '_ht', text.split(' =')[0], 'gestrichelt'])


def parallelogramm(g, h, v, e='cm', lg='g', lh='h', namen='ABCD', flaeche=True, seite=None, hx=None):
    """A(0|0), B(g|0), C(g+v|h), D(v|h). Bei 0 < v < g steht die Höhe innen (rechts von D), sonst von D aus mit gestrichelter Verlängerung von [AB]."""
    A_, B_, C_, D_ = namen
    pk = {A_: (0, 0), B_: (g, 0), C_: (g + v, h), D_: (v, h)}
    lin = [[A_, B_, _lab(g, e, lg)], [B_, C_], [C_, D_], [D_, A_, seite or '']]
    if 0 < v < g:
        x = float(v) + (float(g) - float(v)) * 0.6 if hx is None else float(hx)
        hoehe_text(pk, lin, round(x, 3), 0, h, _lab(h, e, lh), [pk[A_], pk[B_], pk[C_], pk[D_]])
        rw = [['_F', '_H', B_]]
    else:
        pk['_F'] = (v, 0)
        lin.append(['_F', D_, _lab(h, e, lh), 'gestrichelt'])
        if v < 0: lin.append(['_F', A_, '', 'gestrichelt'])
        if v > g: lin.append([B_, '_F', '', 'gestrichelt'])
        rw = [['_F', D_, B_ if v < g else A_]]
    return fig(pk, lin, [A_, B_, C_, D_] if flaeche else None, rw)


def dreieck(g, h, xc, e='cm', lg='g', lh='h', namen='ABC', flaeche=True):
    """A(0|0), B(g|0), C(xc|h); Höhe von C auf [AB] (Fußpunkt F), bei stumpfem Winkel außen mit gestrichelter Verlängerung."""
    A_, B_, C_ = namen
    pk = {A_: (0, 0), B_: (g, 0), C_: (xc, h)}
    lin = [[A_, B_, _lab(g, e, lg)], [B_, C_], [C_, A_]]
    if 0 < xc < g:
        hoehe_text(pk, lin, xc, 0, h, _lab(h, e, lh), [pk[A_], pk[B_], pk[C_]])
        rw = [['_F', '_H', B_]]
    elif xc in (0, g):
        hoehe_text(pk, lin, xc, 0, h, _lab(h, e, lh), [pk[A_], pk[B_], pk[C_]])
        rw = [[A_ if xc == 0 else B_, C_, B_ if xc == 0 else A_]]
    else:
        hoehe_text(pk, lin, xc, 0, h, _lab(h, e, lh), [pk[A_], pk[B_], pk[C_]])
        lin.append([A_, '_F', '', 'gestrichelt'] if xc < 0 else [B_, '_F', '', 'gestrichelt'])
        rw = [['_F', '_H', B_ if xc < g else A_]]
    return fig(pk, lin, [A_, B_, C_] if flaeche else None, rw)


def trapez(a, c, h, xd, e='cm', la='a', lc='c', lh='h', namen='ABCD', flaeche=True):
    """A(0|0), B(a|0), C(xd+c|h), D(xd|h); AB ∥ DC. Höhe innen (wo oben und unten Figur ist) oder als Seite [DA] beim rechtwinkligen Trapez."""
    A_, B_, C_, D_ = namen
    pk = {A_: (0, 0), B_: (a, 0), C_: (xd + c, h), D_: (xd, h)}
    lin = [[A_, B_, _lab(a, e, la)], [B_, C_], [C_, D_, _lab(c, e, lc)], [D_, A_]]
    if xd == 0:
        hoehe_text(pk, lin, 0, 0, h, _lab(h, e, lh), [pk[A_], pk[B_], pk[C_], pk[D_]])
        rw = [[A_, B_, D_]]
    else:
        lo, hi = max(0.0, float(xd)), min(float(a), float(xd + c))
        x = round(lo + (hi - lo) * 0.6, 3)
        hoehe_text(pk, lin, x, 0, h, _lab(h, e, lh), [pk[A_], pk[B_], pk[C_], pk[D_]])
        rw = [['_F', '_H', B_]]
    return fig(pk, lin, [A_, B_, C_, D_] if flaeche else None, rw)


def vieleck(punkte, kanten=None, flaeche=True, extra=(), rechte=()):
    """Vieleck aus benannten Punkten (Reihenfolge = Umlauf). kanten: {(P, Q): Text}."""
    namen = list(punkte)
    lin = []
    for i, p in enumerate(namen):
        q = namen[(i + 1) % len(namen)]
        lin.append([p, q, (kanten or {}).get((p, q), (kanten or {}).get((q, p), ''))])
    return fig(punkte, lin + [list(x) for x in extra], namen if flaeche else None, list(rechte))


def schraeg_prisma(front, tiefe, e='cm', labels=None, tiefe_text=True, q=0.5):
    """Schrägbild eines geraden Prismas: Grundfläche front (Liste von (x, y), gegen den Uhrzeigersinn) in wahrer Größe vorn,
    Tiefe unter 45° mit Faktor q. Verdeckte Kanten gestrichelt (Sichtbarkeit über die Außennormalen der Seitenflächen).
    labels: {i: Text} für die Kante front[i] → front[i+1]. Gedacht für konvexe Grundflächen und Treppenformen (Stufen nach rechts unten)."""
    n = len(front)
    flaeche2 = sum(front[i][0] * front[(i + 1) % n][1] - front[(i + 1) % n][0] * front[i][1] for i in range(n))
    assert flaeche2 > 0, 'front gegen den Uhrzeigersinn angeben'
    dd = float(tiefe) * q / math.sqrt(2)
    pk = {}
    for i, (x, y) in enumerate(front):
        pk[f'_v{i}'] = (x, y)
        pk[f'_h{i}'] = (float(x) + dd, float(y) + dd)
    sicht = []
    for i in range(n):
        (x1, y1), (x2, y2) = front[i], front[(i + 1) % n]
        nx, ny = (y2 - y1), -(x2 - x1)          # Außennormale bei Umlauf gegen den Uhrzeigersinn
        sicht.append(nx + ny > 1e-9)
    lin = []
    for i in range(n):
        lin.append([f'_v{i}', f'_v{(i + 1) % n}', (labels or {}).get(i, '')])
    for i in range(n):
        lin.append([f'_h{i}', f'_h{(i + 1) % n}', ''] + ([] if sicht[i] else ['gestrichelt']))
    tl = None
    for i in range(n):
        vis = sicht[i] or sicht[i - 1]
        lin.append([f'_v{i}', f'_h{i}', ''] + ([] if vis else ['gestrichelt']))
        if vis and tl is None and tiefe_text: tl = len(lin) - 1
    if tiefe_text:
        # Tiefe an der sichtbaren Verbindungskante ganz rechts unten beschriften
        kand = [k for k in range(n) if sicht[k] or sicht[k - 1]]
        k = max(kand, key=lambda i: (front[i][0] - front[i][1], front[i][0]))
        idx = 2 * n + k
        lin[idx][2] = tiefe_text if isinstance(tiefe_text, str) else gr(tiefe, e)
    return fig(pk, lin, [f'_v{i}' for i in range(n)])


def schraeg_quader(a, b, c, e='cm', la=True, lb=True, lc=True, gitter=False):
    """Quader: Breite a (vorn), Tiefe b (45°, halb), Höhe c. gitter: Einheitswürfel auf den sichtbaren Flächen."""
    f = schraeg_prisma([(0, 0), (a, 0), (a, c), (0, c)], b, e, labels={0: gr(a, e) if la is True else (la or ''), 3: gr(c, e) if lc is True else (lc or '')},
                       tiefe_text=(gr(b, e) if lb is True else (lb or False)))
    if gitter:
        dd = 0.5 / math.sqrt(2)
        pk, lin = f['punkte'], f['linien']
        for i in range(1, int(a)):
            pk[f'_ga{i}'] = [i, 0]; pk[f'_gb{i}'] = [i, c]; pk[f'_gc{i}'] = [_r(i + b * dd), _r(c + b * dd)]
            lin += [[f'_ga{i}', f'_gb{i}'], [f'_gb{i}', f'_gc{i}']]
        for j in range(1, int(c)):
            pk[f'_gd{j}'] = [0, j]; pk[f'_ge{j}'] = [a, j]; pk[f'_gf{j}'] = [_r(a + b * dd), _r(j + b * dd)]
            lin += [[f'_gd{j}', f'_ge{j}'], [f'_ge{j}', f'_gf{j}']]
        for k in range(1, int(b)):
            pk[f'_gg{k}'] = [_r(k * dd), _r(c + k * dd)]; pk[f'_gh{k}'] = [_r(a + k * dd), _r(c + k * dd)]; pk[f'_gi{k}'] = [_r(a + k * dd), _r(k * dd)]
            lin += [[f'_gg{k}', f'_gh{k}'], [f'_gh{k}', f'_gi{k}']]
    return f


def schraeg_zylinder(r, h, e='cm', lr=True, lh=True, q=0.5):
    """Liegender Zylinder im Schrägbild: vordere Grundfläche als Kreis in wahrer Größe, Achse unter 45° mit Faktor q."""
    dd = float(h) * q / math.sqrt(2)
    s = 1 / math.sqrt(2)
    pk = {'_M': (0, 0), '_N': (dd, dd), '_P': (-r * s, r * s), '_Q': (r * s, -r * s), '_P2': (-r * s + dd, r * s + dd), '_Q2': (r * s + dd, -r * s + dd),
          '_R': (0, -r)}
    lin = [['_P', '_P2'], ['_Q', '_Q2', gr(h, e) if lh is True else (lh or '')], ['_M', '_N', '', 'gestrichelt']]
    if lr: lin.append(['_M', '_R', gr(r, e) if lr is True else lr])
    return fig(pk, lin, kreise=[{'m': '_M', 'r': float(r)}, {'m': '_N', 'r': float(r)}])


def netz_rechtecke(breiten, hoehe, e='cm', oben=None, unten=None, lb=True, lh=True, lage=None):
    """Streifen aus Rechtecken nebeneinander (Mantel), dazu Vielecke oben/unten an einem Rechteck: (index, [(x, y) relativ zur Ecke links], Texte).
    lage: je Rechteck 'u' (Breite unten anschreiben), 'o' (oben) oder None; Standard: unten."""
    lage = lage or ['u'] * len(breiten)
    pk, lin, x = {}, [], 0
    pk['_u0'] = (0, 0); pk['_o0'] = (0, hoehe)
    for i, b in enumerate(breiten):
        x += b
        pk[f'_u{i + 1}'] = (x, 0); pk[f'_o{i + 1}'] = (x, hoehe)
        lin.append([f'_u{i}', f'_u{i + 1}', gr(b, e) if (lb and lage[i] == 'u') else ''])
        lin.append([f'_o{i}', f'_o{i + 1}', gr(b, e) if (lb and lage[i] == 'o') else ''])
        lin.append([f'_u{i + 1}', f'_o{i + 1}', gr(hoehe, e) if (lh and i == len(breiten) - 1) else ''])
    lin.append(['_u0', '_o0'])
    for nr, (idx, pts, txt) in enumerate(oben or []):
        x0 = sum(breiten[:idx])
        namen = []
        for j, (px, py) in enumerate(pts):
            k = f'_t{nr}_{j}'; pk[k] = (x0 + px, hoehe + py); namen.append(k)
        kette = [f'_o{idx}'] + namen + [f'_o{idx + 1}']
        for j in range(len(kette) - 1): lin.append([kette[j], kette[j + 1], txt.get(j, '') if txt else ''])
    for nr, (idx, pts, txt) in enumerate(unten or []):
        x0 = sum(breiten[:idx])
        namen = []
        for j, (px, py) in enumerate(pts):
            k = f'_b{nr}_{j}'; pk[k] = (x0 + px, py); namen.append(k)
        kette = [f'_u{idx}'] + namen + [f'_u{idx + 1}']
        for j in range(len(kette) - 1): lin.append([kette[j], kette[j + 1], txt.get(j, '') if txt else ''])
    return fig(pk, lin)


def netz_keil(p, q, r, l, e='cm'):
    """Netz eines Keils (rechtwinkliges Dreieck p, q, r als Stirnfläche, Länge l): Streifen p | q | r, ein Dreieck oben am Rechteck p,
    eins unten an der langen Seite r (rechter Winkel gegenüber)."""
    return netz_rechtecke([p, q, r], l, e, oben=[(0, [(0, q)], None)], unten=[(2, [(Fr(q * q, r), -Fr(p * q, r))], None)], lage=['u', 'u', 'o'])


# ---------- Maßstabsprüfung ----------
FAKTOR = {'mm': Fr(1, 10), 'cm': 1, 'dm': 10, 'm': 100, 'km': 100000}
_MASS = re.compile(r'(?:^|=|≈|\s)\s*(\d[\d ]*(?:,\d+)?)\s*(mm|cm|dm|km|m)(?![²³\w])')


def _laenge_aus_text(t):
    if not t or '?' in t: return None
    m = _MASS.search(t)
    if not m: return None
    return Fr(m.group(1).replace(' ', '').replace(',', '.')) * FAKTOR[m.group(2)]


def masstab(bild):
    """Gibt eine Fehlerliste zurück: alle beschrifteten Strecken müssen im gleichen Maßstab gezeichnet sein (Tiefenkanten unter 45°: halber Maßstab)."""
    if not bild or bild.get('typ') != 'figur': return []
    P = bild['punkte']
    voll, halb, fehler = [], [], []
    for lin in bild.get('linien', []):
        t = lin[2] if len(lin) > 2 else ''
        soll = _laenge_aus_text(t)
        if soll is None: continue
        a, b = P[lin[0]], P[lin[1]]
        ist = math.hypot(b[0] - a[0], b[1] - a[1])
        if ist < 1e-9: continue      # freie Beschriftung (Strecke der Länge 0)
        dx, dy = b[0] - a[0], b[1] - a[1]
        tief = abs(abs(dx) - abs(dy)) < 1e-2 and abs(dx) > 1e-6 and dx * dy > 0
        (halb if tief else voll).append((ist / float(soll), t))
    for (r1, t1) in voll:
        for (r2, t2) in voll:
            if abs(r1 / r2 - 1) > 0.015: fehler.append(f'Maßstab: „{t1}“ und „{t2}“ passen nicht zusammen ({r1:.4f} / {r2:.4f})')
    if voll:
        s = voll[0][0]
        for r, t in halb:
            if abs(r / s - 0.5) > 0.015 and abs(r / s - 1) > 0.015: fehler.append(f'Maßstab Tiefe: „{t}“ ({r:.4f} statt {s / 2:.4f})')
    for rw in bild.get('rechter_winkel', []):
        s, q1, q2 = (P[k] for k in rw[:3])
        u, v = (q1[0] - s[0], q1[1] - s[1]), (q2[0] - s[0], q2[1] - s[1])
        if abs(u[0] * v[0] + u[1] * v[1]) > 1e-2 * math.hypot(*u) * math.hypot(*v): fehler.append(f'rechter Winkel bei {rw[0]} ist keiner')
    return fehler


def _merge(zustand, b):
    if not b: return zustand
    if not zustand or (b.get('typ') and b.get('typ') != zustand.get('typ')): return b
    return {**zustand, **b}


def alle_bilder(datei):
    """(Ort, Bild) für Kartenbilder, Schrittzustände, fehler_bild und Aufgabengrafiken."""
    for e in datei['inhalt']['etappen']:
        zs = e.get('bild')
        yield f'{e["lernziel"]}/Karte', zs
        for i, s in enumerate(e.get('schritte') or []):
            if isinstance(s, dict) and s.get('bild'): zs = _merge(zs, s['bild'])
            yield f'{e["lernziel"]}/Schritt {i + 1}', zs
        if e.get('fehler_bild'): yield f'{e["lernziel"]}/fehler_bild', _merge(zs, e['fehler_bild'])
    for i, a in enumerate(datei['aufgaben']):
        if a['f'].get('grafik'): yield f'Aufgabe {i + 1} ({a["l"]})', a['f']['grafik']


# ---------- Zusammenbau ----------
def aufgaben(etappen, gen, feste, seed):
    import random
    R = random.Random(seed)
    F = feste(R)
    out, gesehen = [], set()
    beispiele = {s['text'] if isinstance(s, dict) else s for e in etappen for s in e['schritte']}
    anz = collections.Counter()
    for e in etappen:
        lz = e['lernziel']
        f = list(F[lz])
        assert sum(1 for a in f if a['_art'] == P) >= 2 and sum(1 for a in f if a['_art'] == K) >= 1, lz
        assert len(f) <= 8
        for pool, st in PLAN:
            if pool == 'uebung' and st == 3 and f:
                a = f.pop(0)
            else:
                for _ in range(4000):
                    a = gen[lz](R, st)
                    if a['f']['text'] not in beispiele and a['f']['text'] not in gesehen: break
                else:
                    raise SystemExit(f'zu wenige Varianten: {lz} Stufe {st}')
            assert a['f']['text'] not in gesehen, a['f']['text']
            gesehen.add(a['f']['text'])
            art = a.pop('_art', None)
            if art: anz[(lz, art)] += 1
            assert len(a['w']) >= 15 and a['h'], a
            if pool != 'uebung': a.pop('h')
            out.append({'l': lz, 't': lz, 'p': pool, 's': st, **a})
    return out, anz


def schreiben(ziel, datei, anz):
    fehler = [f'{wo}: {f}' for wo, b in alle_bilder(datei) for f in masstab(b)]
    if fehler: raise SystemExit('Maßstab:\n' + '\n'.join(fehler[:30]))
    ziel.write_text(json.dumps(datei, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{ziel.name}: {len(datei["inhalt"]["etappen"])} Lernkarten, {len(datei["aufgaben"])} Aufgaben, Maßstab geprüft')
    for e in datei['inhalt']['etappen']:
        l = e['lernziel']
        print(f'  {l:22} Prüfungsvorbild: {anz[(l, P)]}  Knobel: {anz[(l, K)]}')
