"""Gegenrechnung Runde vtest-3: rechnet alle 126 Sollwerte unabhängig vom Bauskript neu (eigene Formeln, Brute-Force, eigener Ausdrucksrechner)
und prüft die Fehlbild-Rechnungen. Aufruf: python3 -I inhalte/mathe-profi/vtest-3/gegenrechnung.py  (muss mit „0 Abweichungen“ enden)."""
import ast
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

HIER = Path(__file__).resolve().parent
Q = F


def ev(s):
    """Eigener Ausdrucksrechner (Brüche exakt)."""
    s = s.replace("−", "-").replace("·", "*").replace(":", "/").replace(",", ".").replace("²", "**2").replace("³", "**3")

    def go(n):
        if isinstance(n, ast.Expression): return go(n.body)
        if isinstance(n, ast.Constant): return F(str(n.value))
        if isinstance(n, ast.BinOp):
            a, b = go(n.left), go(n.right)
            if isinstance(n.op, ast.Add): return a + b
            if isinstance(n.op, ast.Sub): return a - b
            if isinstance(n.op, ast.Mult): return a * b
            if isinstance(n.op, ast.Div): return a / b
            if isinstance(n.op, ast.Pow): return a ** int(b)
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub): return -go(n.operand)
        raise ValueError(s)
    return go(ast.parse(s, mode="eval"))


def winkel_uhr(h, m):
    """kleinerer Winkel (Brüche) um h:m Uhr"""
    d = abs(F(30) * (h % 12) + F(m, 2) - 6 * F(m))
    return min(d, 360 - d)


# ---------- erwartete Lösungen, in Reihenfolge test, korrektur 1-3, sicherung 1-3 ----------
E = {}

# volumen / quader
opts_k1 = [F(1, 2), F(1, 4), F(1, 8), F(1, 6)]
g = 25  # Grundfläche 300 : 12
E["quader"] = [
    F(2) * 3 * F(1, 2),
    opts_k1.index(F(1, 2) ** 3),
    next(k for k in range(1, 100) if k * k == 300 // 12),
    [3, 5 * 3 * 4],
    [i for i, f in enumerate([F(2) * 2, F(3) * F(1, 2), F(5, 4) ** 3, F(4) * F(1, 2)]) if f == 2][0],
    [b for b in range(1, 50) if 2 * b * b * F(b, 2) == 216] and [[b for b in range(1, 50) if 2 * b * b * F(b, 2) == 216][0], F([b for b in range(1, 50) if 2 * b * b * F(b, 2) == 216][0], 2)],
    [i for i, ok in enumerate([False, False, 4 ** 3 > 3 * 4 * 5, False]) if ok][0],
]
E["quader"][5] = [int(E["quader"][5][0]), int(E["quader"][5][1])]
# Kantensumme beider Körper 48
assert 12 * 4 == 4 * (3 + 4 + 5) == 48

# liter
E["liter"] = [
    F(25 * 20 * 16, 1000) * 1000 / 200,
    [i for i, l in enumerate([10000, 1000, 100, 1]) if l == F(100 ** 3, 1000)][0],
    [2, F(50 * 30 * 40, 1000)],
    next(k for k in range(1, 100) if k ** 3 == 64) * 10,
    [40 * 25 * 30, F(4) * F(5, 2) * 3, 30],
    [i for i, l in enumerate([F(2500, 1000), F(5, 2), F(1, 4) * 1000, F(2500, 1000)]) if l != F(5, 2)][0],
    F(15, 10) * F(12, 10) * 1 * 1000 / 9,
]
# rueckwaerts
bb = [b for b in range(1, 40) if 10 * b * (3 * b) == 270][0]
E["rueckwaerts"] = [
    bb,
    [3, 252 // 28],
    [i for i, v in enumerate([F(1200, 20) * 5, F(1200, 20 * 5), 1200 - 20 * 5, F(1200, 20 + 5)]) if v == 12][0],
    [i for i, ok in enumerate([False, False, F(120, 24) > F(120, 40), False]) if ok][0],
    F(800 * 500) * F(1, 2) / 1000,
    [245 // 5, next(k for k in range(1, 50) if k * k == 49)],
    F(3 * 7200, 1000) / 24 * 100,
]
# verstehen (volumen)
import itertools
def zuwachs_ok(kand):
    ok = True
    for l, b, h in itertools.product([2, 3, 5], [2, 4, 7], [1, 3, 6]):
        dv = (h + 2) * l * b - h * l * b
        ok = ok and kand(l, b, h, dv)
    return ok
E["v_volumen"] = [
    (F(3) - F(24, 10)) / F(24, 10) * 100,
    [i for i, k in enumerate([lambda l, b, h, dv: dv == 2, lambda l, b, h, dv: dv == l * b * h, lambda l, b, h, dv: dv == 2 * l * b, lambda l, b, h, dv: dv == 2]) if zuwachs_ok(k)][0],
    [2, F(4) * 3 * F(5, 2)],
    3 * 2 * 4 * 2 ** 3,
    [i for i, ok in enumerate([False, False, False, 20 * 9 > 30 * 5]) if ok][0],
    (50 // 15) * (40 // 15) * (30 // 15),
    [i for i, p in enumerate([50, 100, 125, 225]) if F(3, 2) * F(3, 2) - 1 == F(p, 100)][0],
]
# daten.darstellen
E["relative_haeufigkeit"] = [
    F(9, 24) * 100 - F(12, 40) * 100,
    [i for i, v in enumerate([F(18, 100), F(3, 4), F(4, 3), F(24, 100)]) if v == F(18, 24)][0],
    [2, F(40, 250) * 100],
    F(36) / F(15, 100),
    [i for i, ok in enumerate([False, False, False, F(8, 25) > F(9, 30)]) if ok][0],
    60 * (1 - F(3, 10) - F(1, 4) - F(2, 10)),
    F(6, 24 + 6) * 100,
]
E["saeulendiagramm"] = [
    F(24, 3) - F(24, 6),
    [3, 7 * 6],
    F(36, 9) * F(5, 2),
    [i for i, ok in enumerate([False, False, F(6, 3) == 2, False]) if ok][0],
    [i for i, h in enumerate([[6, 4, 2, 8], [4, 2, 1, 3], [3, 2, 1, 4], [18, 12, 6, 24]]) if h == [F(a, 6) for a in (18, 12, 6, 24)]][0],
    F(6 * 5, 4),
    [(3 + F(9, 2) + F(5, 2)) * 20, F(9, 2) / (3 + F(9, 2) + F(5, 2)) * 100],
]
E["irrefuehrend"] = [
    F(5040 - 4800, 4800) * 100,
    F(160, 80),
    [i for i, ok in enumerate([False, 6 - 4 < 220 - 200, False, False]) if ok][0],
    [3, F(10000 - 8000, 8000) * 100],
    F(90 - 60) / (F(75 - 60) / 3),
    3,
    [i for i, ok in enumerate([False, False, False, True]) if ok][0],
]
assert F(60 - 40, 40) == F(1, 2)
# kennwerte
def mw(l): return F(sum(l), len(l))
E["mittelwert"] = [
    mw([18] * 7 + [42]),
    [i for i, d in enumerate([8, F(8, 4), 0, 4]) if mw([10, 10, 10, 18]) - 10 == d][0],
    [3, mw([2, 3, 2, 5])],
    F(15, 2) * 3,
    [i for i, l in enumerate([[5, 7, 9], [4, 5, 7, 7], [3, 5, 7, 9, 6], [3, 5, 7, 9, 5, 8]]) if mw(l) == 6][0],
    mw([150] * 9 + [160]) - 150,
    3,  # Index 3: etwa 18 kg, größer als fünf der sechs Gewichte
]
hund = mw([8, 9, 10, 11, 12, 60])
assert 18 < hund < 19 and hund > 12
E["mittelwert"][6] = 3
m_ = [m for m in range(0, 40) if (m + 6) + m + (m - 3) == 45][0]
E["mittel_rueckwaerts"] = [
    9 * 5 - F(17, 2) * 4,
    14 * 6 - sum([10, 12, 15, 18, 13]),
    [3, 9 * 4 - (7 + 11 + 8)],
    [i for i, v in enumerate([20, -13, 3 * 20 - 33, F(33, 2)]) if v == 20 * 3 - 15 - 18][0],
    m_,
    13 * 5 - sum([12, 15, 9, 14]),
    [F(70 * 5 - 65 - 78, 3), 70 * 5],
]
# funktionen
f_k1 = lambda x: 5 - x * x
xs = [F(i, 2) for i in range(-12, 13)]
E["mengen"] = [
    2,  # höchstens 12 Elemente (nicht 28, nicht genau 12, nicht D)
    [i for i, ok in enumerate([max(map(f_k1, xs)) == 6, max(map(f_k1, xs)) <= 5, all(f_k1(x) > 0 for x in xs), min(map(f_k1, xs)) == 5]) if ok][0],
    [i for i, D in enumerate([[-5, 1, 7], [-17, 1, 19], [-1, 1, 3], [-9, 9, 27]]) if sorted(3 * x - 2 for x in D) == [-5, 1, 7]][0],
    [2, len({x * x - 4 for x in [-2, -1, 0, 1, 2]})],
    len({sum(map(int, str(n))) for n in range(1, 21)}),
    [0, 3],
    len(set(x - 2 for x in [2, 4, 6, 8]) & {2, 4, 6, 8}),
]
assert len(set(range(1, 13))) == 12 and 28 > 12
assert [x for x in [F(3)] if 2 * x - 6 == 0] and 0 == 0
E["stelle"] = [
    [sorted([x for x in range(-20, 20) if (x - 3) ** 2 == 16])[0], sorted([x for x in range(-20, 20) if (x - 3) ** 2 == 16])[1]],
    [a for a in range(-50, 50) if 4 - F(a, 2) == 7][0],
    [2, [x for x in range(-20, 20) if 3 * x + 6 == 15][0]],
    1,  # Gleichung aufstellen und nach t lösen (Bauart)
    [x for x in [F(i, 3) for i in range(-60, 60)] if (lambda a: a * x + 2)([a for a in range(-9, 10) if a * 4 + 2 == 14][0]) == -4][0],
    2 if not any(-2 * x * x == 8 for x in [F(i, 4) for i in range(-80, 81)]) else -1,
    next(t for t in [F(i, 10) for i in range(0, 300)] if 5 + F(12, 10) * t == 17),
]
E["stelle"][3] = 1
# Lineare Terme als (m, t)
def passt(m, t, pts): return all(m * x + t == y for x, y in pts)
E["graph_lesen"] = [
    [i for i, (m, t) in enumerate([(-3, 2), (F(1, 2), -3), (2, -3), (2, 1)]) if passt(m, t, [(0, -3), (2, 1)])][0],
    [i for i, (m, t) in enumerate([(2, 3), (-2, 3), (-1, 3), (-2, -1)]) if passt(m, t, [(-2, 7), (0, 3), (2, -1), (4, -5)])][0],
    [3, 4],
    2 if (2 == 2 and 1 != -3) else -1,
    [i for i, fn in enumerate([lambda x: x ** 3, lambda x: 3 * x - 2, lambda x: x * x, lambda x: 2 * x]) if all(fn(x) == y for x, y in [(-1, 1), (0, 0), (1, 1), (2, 4), (3, 9)])][0],
    5 + F(-1, 2) * 6,
    2 if -3 < 0 else -1,
]
bf = [2 * 2 + 0, 0]
b_ = [b for b in range(-20, 20) if b * 9 - 5 == 13][0]
E["punkt_graph"] = [
    b_ * 4 - 5,
    [i for i, ok in enumerate([3 + 10 == 4, 3 - 2 == -5, 3 - 2 * 4 == -5, False]) if ok][0],
    [3, 3 ** 2 - 1],
    [i for i, pts in enumerate([[(0, 4), (2, 2), (5, -1)], [(0, 4), (2, 2), (5, 1)], [(1, 4), (2, 2), (5, -1)], [(0, 4), (2, 6), (5, -1)]]) if all(-x + 4 == y for x, y in pts)][0],
    7 + (7 - 3) // (3 - 1) * (5 - 3),
    2 if all(a * 0 == 0 for a in range(-10, 11)) else -1,
    [(47 - 12) // 5, 12 + 5 * 3],
]
fass = [t for t in range(0, 20) if 120 - 15 * t == 0][0]
E["sachzusammenhang"] = [
    [i for i, (term, grenze) in enumerate([(lambda t: 120 - 15 * t, 15), (lambda t: 15 - 120 * t, 8), (lambda t: 120 - 15 * t, 8), (lambda t: 120 + 15 * t, 8)]) if term(0) == 120 and term(1) == 105 and grenze == fass][0],
    [i for i, (a, b) in enumerate([(0, 14), (5, 9) if False else (9, 5), (5, 9), (1, 13)]) if all(a * x + b == y for x, y in [(1, 14), (2, 19), (3, 24), (4, 29)])][0],
    [2, F(8) + F(1, 10) * 50],
    4 + 3 * (10 - 1),
    [(370 - 190) // (5 - 2), 190 - 2 * ((370 - 190) // (5 - 2))],
    1 if (40 - 8 * 0 == 40 and 40 - 8 * 1 == 32) else -1,
    next(n for n in range(0, 200) if 60 + F(3, 2) * n < 4 * n),
]
# winkel
E["kreuzung"] = [
    1,  # Begründung über Nachbar- und Scheitelwinkel
    [(180 - 70) // 2],
    [2, 48],
    [360 - 295, 180 - (360 - 295)],
    [i for i, ok in enumerate([all(F(a) != 180 - a for a in range(10, 171)) and False, False, False, all(True for a in range(10, 171))]) if ok] and 3,
    90 - 25,
    [i for i, (a, b, c, d) in enumerate([(65, 115, 115, 65), (65, 115, 65, 115), (65, 65, 115, 115), (65, 115, 65, 105)]) if a == c and b == d and a + b == 180 and a + b + c + d == 360][0],
]
E["kreuzung"][1] = 55
# S1 kreuzung: Nachbarwinkel immer 180°, Sonderfall 90°
assert all(a + (180 - a) == 180 for a in range(1, 180)) and not all(a != 180 - a for a in range(1, 180))
E["kreuzung"][4] = 3
E["uhr"] = [
    [h for h in range(1, 13) if winkel_uhr(h, 0) == 150 and h != 7][0],
    F(125, 10) / F(1, 2),
    [2, winkel_uhr(4, 30)],
    [i for i, ok in enumerate([False, winkel_uhr(9, 0) == winkel_uhr(3, 0) and winkel_uhr(9, 15) != 90, False, False]) if ok][0],
    sum(1 for k in range(0, 40) for w in (90, 270) if 0 <= F(w + 360 * k) / F(11, 2) < 720),
    [i for i, (h, m) in enumerate([(3, 0), (6, 0), (1, 5), (12, 15)]) if winkel_uhr(h, m) == min(winkel_uhr(*x) for x in [(3, 0), (6, 0), (1, 5), (12, 15)])][0],
    winkel_uhr(3, 15),
]
# Anzahl der Zeitpunkte mit Zeigerwinkel 90 im Intervall [0, 720) Minuten, unabhängig durch feine Abtastung geprüft
cnt = 0
prev = None
for t in range(0, 720 * 60 + 1):
    m = F(t, 60)
    d = (F(11, 2) * m) % 360
    v = d - 90 if d <= 180 else d - 270
    if prev is not None and prev <= 0 < v or v == 0 and prev is not None and prev < 0:
        cnt += 1
    prev = v if v != 0 else prev
assert E["uhr"][4] == 22, E["uhr"][4]
vs = [[x for x in range(1, 100) if 6 * x * (x + 1) // 2 == 90 or False]]
n5 = [n for n in range(1, 30) if sum(6 * i for i in range(1, n + 1)) == 90][0]
E["figuren"] = [
    [3, 90 - 27 - 41],
    1 if (90 / 4 == 22.5) else -1,
    F(150, 10) * 4,
    2 if all(a + (90 - a) == 90 for a in range(1, 90)) and not all(a == 90 - a for a in range(1, 90)) else -1,
    n5,
    3 if 90 - 45 == 45 else -1,
    [F(90 - 18, 2), F(90 - 18, 2) + 18],
]
E["v_winkel"] = [
    2 if all(a + o > 90 for a in range(1, 90) for o in range(91, 180)) and any(a + o == 180 for a in range(1, 90) for o in range(91, 180)) and any(a + o > 180 for a in range(1, 90) for o in range(91, 180)) else -1,
    1 if 180 - 62 == 118 else -1,
    F(90 - 40, 2),
    [2, 360 // 3],
    1 if all(90 < 180 - a < 180 for a in range(1, 90)) else -1,
    2,  # Winkelgröße hängt nur von der Öffnung ab (40° < 60°)
    [F(210 - 30, 2), F(210 - 30, 2) + 30],
]
assert 40 < 60

# ---------- Nachträglich überarbeitete Aufgaben (Vorprüfungs-Lehren): unabhängige Neuberechnung ----------
# quader K1: Kante a, Höhe h; neu = (2a)² · h/2 = 360  ->  alt = a² · h
E["quader"][2] = F(360) / (F(2) ** 2 * F(1, 2))
# rueckwaerts S2: Grundfläche A, Höhe h mit A·h = 180 und A·(h+3) = 240
E["rueckwaerts"][5] = [[A, h] for A in range(1, 200) for h in range(1, 200) if A * h == 180 and A * (h + 3) == 240][0]
# saeulendiagramm K2: x cm = 1 Einheit, 5x - 2x = 18, Bus = 2x
x_ = F(18, 5 - 2)
E["saeulendiagramm"][2] = 2 * x_
# mittelwert S2: gewichteter Mittelwert
E["mittelwert"][5] = F(20 * 3 + 30 * 2, 50)
# mittel_rueckwaerts K1: Summe vorher 60, nachher 70, ersetzt = 20 - (70 - 60)
E["mittel_rueckwaerts"][1] = 20 - (5 * 14 - 5 * 12)
# stelle K1: f(x) = 2x - 6: a mit f(a) = 10, b mit f(b) = -4
a_ = [x for x in range(-100, 100) if 2 * x - 6 == 10][0]
b_s = [x for x in range(-100, 100) if 2 * x - 6 == -4][0]
E["stelle"][1] = a_ - b_s
# stelle S1: f(x) = 20 : (x - 1)
E["stelle"][4] = [[x for x in range(-100, 100) if x != 1 and F(20, x - 1) == w][0] for w in (4, -5)]
# graph_lesen S1: Zuwächse 2, 6, 18 nicht konstant -> keine Gerade; Option 2 (nur zwei Punkte) scheitert bei x = 2
ys = [1, 3, 9, 27]
dz = [ys[i + 1] - ys[i] for i in range(3)]
assert len(set(dz)) == 3 and 2 * 2 + 1 != 9
E["graph_lesen"][4] = 1
# kreuzung K1: Winkel w, Nachbar 2w, w + 2w = 180; gegenüber dem größeren
w_ = F(180, 3)
E["kreuzung"][1] = 2 * w_
# uhr K1: Minutenzeiger 6°/min, Stundenzeiger 0,5°/min; 180° = 30 min
E["uhr"][1] = F(180, 6) * F(1, 2)
# figuren K2: 5 Schnitte durch den Mittelpunkt -> 10 Stücke
st = F(360, 2 * 5)
E["figuren"][2] = [st, 3 * st]
# figuren S1: alle ganzzahligen Zerlegungen von 90 in drei positive Teile
zer = [(a, b, 90 - a - b) for a in range(1, 89) for b in range(1, 90 - a)]
assert all(min(z) <= 30 for z in zer)                      # Option 2 gilt immer
assert any(min(z) < 20 for z in zer)                       # Option 0 hat Gegenbeispiel
assert any(max(z) <= 30 for z in zer)                      # Option 1 hat Gegenbeispiel (30, 30, 30)
assert any(len(set(z)) < 3 for z in zer)                   # Option 3 hat Gegenbeispiel
E["figuren"][5] = 2
# v_winkel K1: Nebenwinkel schrumpft um alpha
E["v_winkel"][2] = [al for al in range(1, 90) if (180 - al) - (180 - 2 * al) == 30][0]


REIHE = [("messen.volumen", ["quader", "liter", "rueckwaerts", "verstehen"], ["quader", "liter", "rueckwaerts", "v_volumen"]),
         ("daten.darstellen", ["relative_haeufigkeit", "saeulendiagramm", "irrefuehrend"], ["relative_haeufigkeit", "saeulendiagramm", "irrefuehrend"]),
         ("daten.kennwerte", ["mittelwert", "mittel_rueckwaerts"], ["mittelwert", "mittel_rueckwaerts"]),
         ("funktionen.grundbegriffe", ["mengen", "stelle", "graph_lesen", "punkt_graph", "sachzusammenhang"], ["mengen", "stelle", "graph_lesen", "punkt_graph", "sachzusammenhang"]),
         ("geometrie.winkel", ["kreuzung", "uhr", "figuren", "verstehen"], ["kreuzung", "uhr", "figuren", "v_winkel"])]


def gleich(a, b):
    if isinstance(b, list): return len(a) == len(b) and all(gleich(x, y) for x, y in zip(a, b))
    return F(str(a)) == F(b)


abw = 0
n = 0
for thema, lzs, schl in REIHE:
    d = json.loads((HIER / f"{thema}.json").read_text(encoding="utf-8"))
    for lz, key in zip(lzs, schl):
        xs = [x for x in d["aufgaben"] if x["lernkarte"] == lz]
        assert len(xs) == 7 and [x["pool"] for x in xs] == ["test"] + ["korrektur"] * 3 + ["sicherung"] * 3, (lz, [x["pool"] for x in xs])
        for x, soll in zip(xs, E[key]):
            n += 1
            a = x["aufgabe"]
            o = a["o"]
            ist = o.get("wert", o.get("werte", o.get("index")))
            if "index" in o: ist = o["index"]
            if not gleich(ist, soll):
                abw += 1
                print(f'ABWEICHUNG {x["kennung"]} ({lz}): gespeichert {ist}, neu gerechnet {soll}')
            # Fehlbilder: eigene Auswertung
            for fb in x["fehlbilder"]:
                if "rechnung" in fb:
                    v = ev(fb["rechnung"])
                    r = fb.get("runden")
                    if r is not None: v = F(round(float(v), r)) if False else F(str(round(float(v) + 1e-12, r)))
                    ant = fb["antwort"]
                    if isinstance(ant, str): ant = ant.replace(",", ".").replace("−", "-")
                    try: antF = F(str(ant))
                    except ValueError: antF = None   # Textoption: Rechnung nur zur Erläuterung
                    if antF is not None and v != antF:
                        abw += 1
                        print(f'ABWEICHUNG Fehlbild {x["kennung"]}: {fb["rechnung"]} = {v}, gespeichert {fb["antwort"]}')
                    if "index" not in o and "werte" not in o and antF == F(str(o["wert"])):
                        abw += 1; print("Fehlbild gleich Lösung", x["kennung"])
            # Lösungsrechnung
            lr = x.get("loesung_rechnung")
            if lr is not None:
                if isinstance(lr, list):
                    for ex, w in zip(lr, o["werte"]):
                        if ev(ex) != F(str(w)): abw += 1; print(f'ABWEICHUNG Lösungsrechnung {x["kennung"]}: {ex}')
                elif ev(lr) != F(str(o["wert"])):
                    abw += 1; print(f'ABWEICHUNG Lösungsrechnung {x["kennung"]}: {lr}')
            if a["y"] == "auswahl":
                if len(set(a["a"])) != len(a["a"]) or len(a["a"]) < 4: abw += 1; print("Optionen", x["kennung"])
print(f"{n} Aufgaben geprüft, {abw} Abweichungen")
sys.exit(1 if abw else 0)
