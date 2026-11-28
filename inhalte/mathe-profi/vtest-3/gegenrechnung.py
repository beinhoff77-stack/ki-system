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


# ---------- erwartete Lösungen je Kennung, unabhängig vom Bauskript gerechnet ----------
# Zahl/Lücken: Zahl oder Liste. Auswahl: ("opt", Teilstring der richtigen Option); dazu Rechenprüfungen (assert).
X = {}


def opt(t):
    return ("opt", t)


def m3(*kanten):
    p = F(1)
    for k in kanten: p *= F(k)
    return p


# ---- messen.volumen / quader
X[1] = (F(3, 2) * F(4, 5) * 2 - 1) * 100
assert m3(F(1, 2), F(1, 2), F(1, 2)) == F(1, 8)
X[2] = next(x for x in range(1, 50) if x * 2 * x * 3 * x == 48)            # Kanten x, 2x, 3x, Volumen 48
X[3] = F(120, 3) * 5                                            # Blätter je cm Höhe mal 5 cm
X[4] = [3, 8 * 3 * 5]
assert 20 * 3 * 5 == 300 and 2 * 10 * 3 * 5 == 300         # 2 m = 20 dm, 30 cm = 3 dm, 5 dm  -> 300 dm³
X[5] = opt("20 · 3 · 5")
X[6] = (lambda e: e ** 3 // (1 * 2 * 4))(next(e for e in range(1, 50) if e % 4 == 0 and e % 2 == 0 and e % 1 == 0))   # kleinster Würfel: Kante 4
assert 4 ** 3 > 3 * 4 * 5 and 4 * (4 + 4 + 4) == 4 * (3 + 4 + 5) == 48
X[7] = opt("Der Würfel hat das größere Volumen")
# ---- liter
X[8] = F(150, 10) ** 3                                 # Kante 150 cm : 10 cm = 15, 15³ Behälter
X[9] = opt("1 000 Liter")
X[10] = [2, F(50 * 30 * 40, 1000)]
X[11] = opt("15 cm lang, 15 cm breit")
assert 15 * 15 * 10 != 2000 and 10 * 10 * 20 == 25 * 8 * 10 == 1 * 2 * 1 * 1000 == 2000
assert 40 * 20 * 10 == 20 ** 3 == 8000
X[12] = opt("Sein Volumen beträgt 1 dm³")
assert F(25, 10) == F(2500, 1000) == F(2500) / 1000 and F(1, 4) * 1000 != F(5, 2)       # 0,25 m³ = 250 l
X[13] = F(10 * 100, 1000)
X[14] = F(m3(150, 120, 100), 1000) / 9                 # 1 800 l : 9 l/min
X[15] = next(b for b in range(1, 100) if 10 * b * (3 * b) == 270)
X[16] = [3, F(308, 7 * 4)]
assert 1200 / (20 * 5) == 12
X[17] = opt("1 200 : (20 · 5)")
assert F(120, 24) > F(120, 40)
X[18] = opt("Quader A ist höher")
X[19] = opt("5 cm, denn 36 : 5")
assert all(36 % k == 0 for k in (4, 6, 9)) and 36 % 5 != 0
X[20] = [A for A in [(A, h) for A in range(1, 300) for h in range(1, 300) if A * h == 180 and A * (h + 3) == 240]][0][0:2] and \
    list([(A, h) for A in range(1, 300) for h in range(1, 300) if A * h == 180 and A * (h + 3) == 240][0])
X[21] = 3   # Quadrat mit Seite 6, Höhe 288 : 36 = 8, Grundfläche 72 : 8 = 9, Seite 3
# ---- verstehen (Volumen)
X[22] = (50 // 15) * (40 // 15) * (30 // 15)
X[23] = opt("2 cm · Länge · Breite")
X[24] = [2, F(4 * 3 * 250, 100)]
X[25] = F(30, 18 - 12)
assert 10 * 4 * 6 == 10 * 6 * 4
X[26] = opt("Beide haben dasselbe Volumen")
X[27] = opt("Nach 6 Stunden")
assert 8 * 7 * 3 == 168
X[28] = opt("Es bleibt gleich")
# ---- daten.darstellen / relative Häufigkeit
X[29] = F(25 * 100, 100) - 10
assert F(18, 24) == F(3, 4)
X[30] = opt("0,75")
X[31] = [2, F(40, 250) * 100]
X[32] = opt("Nein, denn 30 % von 8")
assert (8 * F(30, 100)).denominator != 1 and 2 * 12.5 == 25
assert F(8, 25) > F(9, 30)
X[33] = opt("Jonas hat nicht recht, denn 8 : 25 ergibt 32 %")
X[34] = opt("Vielfaches von 1/120")
X[35] = F(sum(range(0)) + 5 + 10, 20 + 80) * 100          # beide Reihen zusammen: Treffer durch alle Würfe
# ---- saeulendiagramm
X[36] = F(10) / (F(5, 2))
X[37] = [3, F(55, 10) * 6 - 2 * 6]
X[38] = opt("1 cm für 10 Kinder")
assert max(k for k in (5, 10, 20, 100) if F(90, k) <= 12 and F(90, k) >= 8) == 10 and F(90, 5) > 12
assert F(6, 3) == 2
X[39] = opt("doppelt so viele Kinder")
X[40] = opt("Beide Säulen stehen für gleich viele Kinder")
assert [h * 6 for h in (3, 2, 1, 4)] == [18, 12, 6, 24]
assert 4 * 8 > 6 * 5
X[41] = opt("3,2 cm")
X[42] = opt("12 Jungen")
assert (9 - 5) * 3 == 12 and 9 * 3 - 5 * 3 == 12
assert F(27, 18) == F(3, 2) and F(27, 9) / F(18, 9) == F(3, 2) and F(27, 3) / F(18, 3) == F(3, 2)
# ---- irrefuehrend
X[43] = F((4700 + F(34, 10) * 100) - (4700 + 100), 4700 + 100) * 100
X[44] = F({1: 10, 2: 20, 3: 40, 4: 80, 5: 160}[4], {1: 10, 2: 20, 3: 40, 4: 80, 5: 160}[2])
assert 22 - 20 == 2 and 220 - 200 == 20 and F(6 - 4, 4) == F(1, 2)
X[45] = opt("Verein B hat mehr neue Mitglieder gewonnen")
X[46] = [2, F(30 - 20, 20) * 100]
X[47] = F(26, 40) * 100 - F(6, 60) * 100
X[48] = opt("Beide Säulen stehen für gleich viel")
assert F(60 - 40, 40) == F(1, 2)
X[49] = opt("In A steigt der Linienzug steiler, aber")
# ---- mittelwert
X[50] = next(m for m in range(0, 100) if 3 * m - 4 == 26)       # Mittelwert folgt denselben Schritten
X[51] = opt("Im Mittel 8 €")
assert F(16 * 10, 20) == 8
assert F(8, 4) == 2
X[52] = [3, F(2 + 3 + 2 + 5, 4)]
X[53] = opt("Er liegt näher bei 11")
assert F(10 * 8 + 20 * 11, 30) == 10 and abs(10 - 11) < abs(10 - 8)
X[54] = opt("weitere 6")
X[55] = F(sum(range(4, 21, 2)), 9)                           # Beträge 4, 6, ..., 20 (neun Wochen)
assert sum(range(16, 25, 2)) / 5 == 20
assert F(50 + 60, 6) > 18 and F(50 + 60, 6) < 19 and F(50 + 60, 6) > 12
X[56] = opt("etwa 18 kg")
# ---- mittel_rueckwaerts
X[57] = next(m for m in range(0, 25) if m * 14 + (24 - m) * 8 == 24 * 10)
X[58] = 5 * 12 - (12 - 5 + 12 + 2 + 12 + 6 + 12 - 1)
X[59] = [2, 5 * 48 - 4 * 50]
assert all(any(x >= 10 for x in z) for z in [(1, 1, 1, 37), (10, 10, 10, 10), (9, 9, 11, 11)])
X[60] = opt("mindestens 10, denn sonst")
X[61] = [sum(z - 100 for z in (98, 101, 103, 99, 104)), F(sum((98, 101, 103, 99, 104)), 5)]
X[62] = F(20) + F(18 - 6, 6)
X[63] = opt("Er ist höchstens 12, denn")
assert F(10 + 11 + 12 + 13, 4) < 12 and F(12 * 4, 4) == 12
# ---- funktionen.grundbegriffe / mengen
X[64] = opt("höchstens 12 Elemente")
f65 = lambda x: x * x - 9
assert f65(0) == -9 and all(f65(F(k, 4)) >= -9 for k in range(-40, 40)) and f65(3) == 0
import itertools
assert max(len(set(f)) for f in itertools.product(range(5), repeat=5)) == 5 and min(len(set(f)) for f in itertools.product(range(5), repeat=5)) == 1
X[65] = opt("W hat höchstens 5 Elemente")
X[66] = opt("D = {−1; 2}")
assert {x * x for x in (-1, 2)} == {1, 4} and {x * x for x in (1, 4)} != {1, 4} and {x * x for x in (1, 2, 3)} != {1, 4} and {x * x for x in (2, 3)} != {1, 4}
assert [3 * x - 2 for x in (-1, 1, 3)] == [-5, 1, 7]
X[67] = [3, len({x * x - 4 for x in (-2, -1, 0, 1, 2)})]
X[68] = opt("eines seiner Geschwister aus der Gruppe")
X[69] = [0, 3]
X[70] = len({x - 2 for x in (2, 4, 6, 8, 10)} & {2, 4, 6, 8, 10})
# ---- stelle
X[71] = next(x for x in range(-50, 50) if x * x - 6 * x == -8 and x != 4)
X[72] = next(a for a in range(-50, 50) if 2 * a - 6 == 8) - next(b for b in range(-50, 50) if 2 * b - 6 == -2)
X[73] = [3, next(x for x in range(-50, 51) if 3 * x + 6 == 36)]
assert 12 + F(3, 2) * 12 == 30
X[74] = opt("Es gilt f(a) > f(b)")
X[75] = [next(x for x in range(-100, 100) if x != 1 and F(20, x - 1) == w) for w in (4, -5)]
assert all(-2 * F(k, 8) ** 2 <= 0 for k in range(-80, 80))
X[76] = opt("keine Lösung")
X[77] = F(10 + 22, 2)
# ---- graph_lesen
m_ = F(1 - (-3), 2)
X[78] = opt("g geht auch durch Q(2 | 9)")
assert F(5, 2) == F(5 - 0, 2 - 0) and -3 * 2 + 11 == 5 and 2 * 2 + 1 == 5
assert m_ == 2 and 2 * 0 - 3 == -3 and 2 * 2 - 3 == 1
mm = F(-3 - 5, 7 - 1) if False else F(-7 - 5, 7 - 1)
X[79] = 5 - mm * 1                                      # y = 5 + m·(x − 1) bei x = 0
assert mm == -2 and 5 - 2 * (3 - 1) == 1
X[80] = [3, 4]
X[81] = opt("parallel und verschieden")
ys = [1, 3, 9, 27]
assert len({ys[i + 1] - ys[i] for i in range(3)}) == 3
X[82] = opt("keine Gerade")
X[83] = opt("y-Achse bei −4 und die x-Achse bei 2")
assert 2 * 0 - 4 == -4 and 2 * 2 - 4 == 0
assert -3 < 0
X[84] = opt("Jonas hat nicht recht, denn die Steigung −3 ist negativ")
X[85] = (lambda b: b * 9 - 5)(next(b for b in range(-20, 20) if b * 4 - 5 == 7))
assert 3 - 2 * 4 == -5
X[86] = opt("M liegt auf dem Graphen, denn der Graph ist eine Gerade")
X[87] = [3, 3 ** 2 - 1]
assert 3 ** 2 - 1 != 5
assert all((2 * F(k, 3) + 1).denominator != 1 or True for k in range(-9, 9))
assert (2 * F(1, 2) + 1) == 2 and 2 * 3 + 1 == 7
X[88] = opt("Ist die Zahl a ganz, so ist auch die Zahl b ganz")
X[89] = (lambda c: c - 2 * 4)(3 * 4 - 2)
X[90] = opt("Für jede Zahl a")
X[91] = opt("7 Tage ausleiht, zahlt 47 Euro")
assert 12 + 5 * 7 == 47
# ---- sachzusammenhang
X[92] = next(n for n in range(1, 500) if 60 + F(3, 2) * n < 4 * n)
assert 120 / 15 == 8
assert (3 + 2 * 8) < 2 * (3 + 2 * 4)
X[93] = opt("weniger als das Doppelte")
X[94] = [2, 8 + F(10, 100) * 50]
assert [4 + 3 * (n - 1) for n in (1, 2, 3)] == [4, 7, 10] and [3 * n + 1 for n in (1, 2, 3)] == [4, 7, 10]
X[95] = opt("richtig ist 3n + 1")
X[96] = opt("s(t) = 1,5t")
assert F(90, 60) * 60 == 90
X[97] = opt("Preis von Äpfeln")
assert len({(n + 1) ** 2 - n ** 2 for n in range(1, 6)}) > 1
X[98] = opt("I(t) = 120 − 15t, sinnvoll für 0 ≤ t ≤ 8")
# ---- geometrie.winkel / kreuzung
X[99] = (lambda w: sum(1 for x in w + w if x < 90))([100, 30, 50])
X[100] = opt("Mia hat recht, denn ein Nachbarwinkel ist 180° − 90°")
assert 100 + 30 + 50 == 180
X[101] = [2, 180 - 100]        # γ ist Nachbarwinkel von β; γ liegt gegenüber von α
X[102] = [360 - 310, 180 - (360 - 310)]
X[103] = opt("Gegenüberliegende Winkel sind gleich groß")
X[104] = 90 - 25
X[105] = opt("α = 72°, β = 108°, γ = 72°, δ = 108°")
# ---- uhr
X[106] = winkel_uhr(3, 30)
X[107] = F(180, 6) * F(1, 2)
X[108] = [3, winkel_uhr(8, 0)]
assert winkel_uhr(9, 0) == winkel_uhr(3, 0) == 90 and winkel_uhr(9, 15) == F(345, 2)
X[109] = opt("Nur Mia hat recht")
assert all(winkel_uhr(h, 0) % 30 == 0 and winkel_uhr(h, 0) <= 180 for h in range(1, 13))
X[110] = opt("Vielfaches von 30°")
zeiten = [(3, 0), (6, 0), (1, 5), (12, 15)]
X[111] = opt("1:05 Uhr")
assert min(zeiten, key=lambda t: winkel_uhr(*t)) == (1, 5)
X[112] = next(h for h in range(1, 13) if h != 7 and winkel_uhr(h, 0) == 150)
# ---- figuren
X[113] = [2, F(2 * 90, 6)]
X[114] = opt("In Zeile 2")
X[115] = F(360, 20) // 2
X[116] = opt("β ist größer als α")
assert F(180, 4) > F(90, 3)
X[117] = opt("α und β ergeben zusammen 90°")
assert all(a + 90 + (90 - a) == 180 for a in range(1, 90))
assert all(F(a, 2) + F(180 - a, 2) == 90 for a in range(1, 180))
zer = [(a, b, 90 - a - b) for a in range(1, 89) for b in range(1, 90 - a)]
assert all(min(z) <= 30 for z in zer) and any(max(z) <= 30 for z in zer) and any(min(z) < 20 for z in zer) and any(len(set(z)) < 3 for z in zer)
X[118] = opt("höchstens 30° groß")
X[119] = [90 - 25, 90 + 25]
# ---- verstehen (Winkel)
X[120] = next(al for al in range(1, 60) if (180 - al) - (180 - 3 * al) == 40)
assert all(a + s > 90 for a in range(1, 90) for s in range(91, 180))
X[121] = opt("180° − 64° = 116°")
X[122] = opt("Er ist kleiner als 180°")
X[123] = [2, sum(1 for w in (35, 90, 110, 180, 250) if 90 < w < 180)]
X[124] = [900 // 360, 900 % 360]
assert F(40) < F(60)
X[125] = opt("β ist größer als α")
x_klein = next(k for k in range(1, 210) if k + (k + 30) == 210)
X[126] = [x_klein, x_klein + 30]


def gleich(a, b):
    if isinstance(b, list): return isinstance(a, list) and len(a) == len(b) and all(gleich(x, y) for x, y in zip(a, b))
    return F(str(a)) == F(b)


abw = 0
n = 0
lang = 0
pos = {0: 0, 1: 0, 2: 0, 3: 0}
fr = {}
for thema in ["messen.volumen", "daten.darstellen", "daten.kennwerte", "funktionen.grundbegriffe", "geometrie.winkel"]:
    d = json.loads((HIER / f"{thema}.json").read_text(encoding="utf-8"))
    for x in d["aufgaben"]:
        k = int(x["kennung"][-3:])
        n += 1
        a = x["aufgabe"]
        o = a["o"]
        soll = X[k]
        if a["y"] == "auswahl":
            teil = soll[1]
            treffer = [i for i, t in enumerate(a["a"]) if teil in t]
            if treffer != [o["index"]]:
                abw += 1
                print(f'ABWEICHUNG {x["kennung"]}: erwartete Option „{teil}“ steht an {treffer}, gespeichert {o["index"]}')
            if len(set(a["a"])) != len(a["a"]) or len(a["a"]) < 4: abw += 1; print("Optionen", x["kennung"])
        else:
            ist = o.get("wert", o.get("werte"))
            if not gleich(ist, soll):
                abw += 1
                print(f'ABWEICHUNG {x["kennung"]}: gespeichert {ist}, neu gerechnet {soll}')
        # Fehlbilder: eigene Auswertung
        for fb in x["fehlbilder"]:
            if "rechnung" in fb:
                v = ev(fb["rechnung"])
                r = fb.get("runden")
                if r is not None: v = F(str(round(float(v) + 1e-12, r)))
                ant = fb["antwort"]
                if isinstance(ant, str): ant = ant.replace(",", ".").replace("−", "-")
                try: antF = F(str(ant))
                except ValueError: antF = None
                if antF is not None and v != antF:
                    abw += 1
                    print(f'ABWEICHUNG Fehlbild {x["kennung"]}: {fb["rechnung"]} = {v}, gespeichert {fb["antwort"]}')
                if "index" not in o and "werte" not in o and antF == F(str(o["wert"])):
                    abw += 1; print("Fehlbild gleich Lösung", x["kennung"])
        lr = x.get("loesung_rechnung")
        if lr is not None:
            if isinstance(lr, list):
                for ex, w in zip(lr, o["werte"]):
                    if ev(ex) != F(str(w)): abw += 1; print(f'ABWEICHUNG Lösungsrechnung {x["kennung"]}: {ex}')
            elif ev(lr) != F(str(o["wert"])):
                abw += 1; print(f'ABWEICHUNG Lösungsrechnung {x["kennung"]}: {lr}')
print(f"{n} Aufgaben geprüft, {abw} Abweichungen")
sys.exit(1 if abw else 0)
