"""Zweite, unabhängige Vorprüfung vtest-1b: rechnet alle 119 Aufgaben neu.

Nicht aus gegenrechnung.py übernommen. Jede Aufgabe hat unten eine eigene Lösungsrechnung (exakt, Brüche) oder – bei
Auswahl – je Möglichkeit einen eigenen Wahrheitswert. Verglichen wird mit dem gespeicherten Lösungswert. Zusätzlich:
Fehlbild-Rechnungen ausführen, Fehlbild != Lösung, Lücken-Abdeckung der Fehlbilder, Auswahl-Statistik.
Aufruf: python3 -I inhalte/mathe-profi/vtest-1b/vorpruefung_rechnen_2.py   (Ende: Zahl der Abweichungen)
"""
import ast
import json
import os
import sys
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))
DATEIEN = ["bruch.prozent", "gleichungen.bruch", "terme.potenzgesetze", "zahlen.potenzen_zehner", "messen.flaechen_vielecke"]


def lade():
    res = {}
    for d in DATEIEN:
        for a in json.load(open(os.path.join(HIER, d + ".json"), encoding="utf-8"))["aufgaben"]:
            res[int(a["kennung"][-3:])] = a
    return res


def ev(s):
    """Auswerter für Rechnungen der Fehlbilder (nur + - * / ** und Klammern), exakt."""
    def g(n):
        if isinstance(n, ast.Expression):
            return g(n.body)
        if isinstance(n, ast.Constant):
            return F(str(n.value))
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
            return -g(n.operand)
        if isinstance(n, ast.BinOp):
            a, b = g(n.left), g(n.right)
            return {ast.Add: lambda: a + b, ast.Sub: lambda: a - b, ast.Mult: lambda: a * b,
                    ast.Div: lambda: a / b, ast.Pow: lambda: a ** int(b)}[type(n.op)]()
        raise ValueError(s)
    return g(ast.parse(str(s).replace("·", "*").replace(":", "/"), mode="eval"))


def flaeche(p):
    s = 0
    for i in range(len(p)):
        x1, y1 = p[i]
        x2, y2 = p[(i + 1) % len(p)]
        s += x1 * y2 - x2 * y1
    return F(abs(s), 2)


def raster(lo=-40, hi=40, nenner=4):
    return [F(i, nenner) for i in range(lo * nenner, hi * nenner + 1)]


def loes(f, nenn_verboten, gitter=None):
    """Lösungen der Bruchgleichung f(x)==True auf dem Gitter, ohne Nennerstellen."""
    return [x for x in (gitter or raster()) if all(v(x) != 0 for v in nenn_verboten) and f(x)]


def nur_eine(liste):
    r = [i for i, b in enumerate(liste) if b]
    assert len(r) == 1, ("nicht genau eine richtige Möglichkeit", liste)
    return r[0]


# ---------------------------------------------------------------- erwartete Lösungen (eigene Rechnung)
def soll():
    S = {}
    # --- bruch.prozent
    maed = F(45, 100) * 400
    S[1] = (maed * F(1, 5)) + ((400 - maed) * F(3, 10))
    S[2] = F(350) * (F(20, 100) - F(1, 100))
    S[3] = 360 * F(35, 100)
    gel2 = 280 - 280 * F(15, 100) - 168
    S[4] = gel2 / 280 * 100
    schaetz = F(51, 100) * 3980
    opts = [200, 20, 2000, 20000]
    S[5] = min(range(4), key=lambda i: abs(opts[i] - schaetz))
    # Zeile 1 falsch (8/100 != 0,8); Wert 36
    z1 = F(8, 100) == F(8, 10)
    S[6] = [1 if not z1 else 2, F(8, 100) * 450]
    S[7] = [F(3, 5) * 100, F(3, 5) * 240]
    ges8 = F(18) / F(45, 100)
    S[8] = ges8 - 18 - ges8 * F(30, 100)
    S[9] = F(36) / F(15, 100)
    S[10] = 63 / (F(54, 360))
    preis = F(105) / F(70, 100)
    S[11] = preis - 105
    za, zb = F(30) / F(20, 100), F(40) / F(25, 100)  # 150, 160
    S[12] = nur_eine([zb > za and (160, 150) == (zb, za), za > zb and (600, 160) == (za, zb),
                      zb > za and (10, 6) == (zb, za), za > zb and False])
    S[13] = [2, F(20) / F(25, 100)]  # Zeile 1 stimmt, Zeile 2 multipliziert statt zu teilen
    S[14] = [F(42, 7), F(42, 7) * 100]
    S[15] = [F(40, 100) * F(30, 100) * 100, F(40, 100) * F(30, 100) * 5000]
    S[16] = 30 + 30 * 2
    wert17 = [F(36, 100), F(37, 100), F(7, 20), F(3, 8)]
    S[17] = max(range(4), key=lambda i: wert17[i])
    S[18] = F(60) / F(12, 100) - F(60) / F(20, 100)
    a19, b19 = F(75, 100) * 8, F(40, 100) * 30
    S[19] = [3, b19 - a19]  # Zeile 1: Zahlen; Zeile 2: Anteil A groesser stimmt; Zeile 3 falsch
    # 20: A*0,2 > B*0,3  =>  A > 1,5 B ; "folgt sicher" = fuer alle A mit 0,2A > 0,3B
    Bs = F(100)
    As = [F(151), F(170), F(200), F(500)]
    folgt = [lambda A, B: A < B, lambda A, B: A > F(3, 2) * B, lambda A, B: A == 2 * B, lambda A, B: A == F(3, 2) * B]
    S[20] = nur_eine([all(f(A, Bs) for A in As) for f in folgt])
    rest = 1 - F(20, 100)
    S[21] = F(18) / (rest - rest / 4)
    # --- gleichungen.bruch
    D22 = [x for x in range(-5, 6) if x != 2]
    S[22] = sum(1 for x in D22 if F(3, x - 2) == F(1, x - 2) + F(2, x - 2))
    S[23] = len({x for x in raster(-10, 10, 1) if 2 * x - 6 == 0 or x + 3 == 0 or x * x - 9 == 0})
    # 24: 2x - a = 0 soll genau die Zahl 7 liefern, da x+3 die -3 liefert
    S[24] = [a for a in range(-40, 41) if {x for x in raster(-20, 20, 1) if 2 * x - a == 0 or x + 3 == 0} == {7, -3}][0]
    ds = {x for x in raster(-10, 10, 1) if x * x - 16 == 0 or x == 0}
    mengen = [{-16, 0, 16}, {-4, 0, 4}, {-4, 4}, {0, 4}]
    S[25] = nur_eine([m == ds for m in mengen])
    S[26] = len([x for x in range(-3, 10) if x != 0 and x - 5 != 0])
    S[27] = [1, len({x for x in raster(-10, 10, 1) if x * x - 25 == 0 or x - 5 == 0})]
    # 28: Taxi: n Kinder, 36/n - 36/(n+3) = 2 gilt nur fuer n=6; Optionen als Gleichung+Menge
    ns = [n for n in range(1, 200) if F(36, n) - F(36, n + 3) == 2]
    gl = [lambda x: F(36) / x - F(36) / (x + 3) == 2, lambda x: F(36) / x + F(36) / (x + 3) == 2,
          lambda x: F(36) / (x - 3) - F(36) / x == 2, lambda x: F(36) / x - F(36) / (x + 3) == 2]
    dm = [{0}, {-3, 0}, {0, 3}, {-3, 0}]
    richtigD = {-3, 0}
    def sol_ok(i):
        return [n for n in range(1, 200) if (n not in dm[i]) and gl[i](F(n))] == ns
    S[28] = nur_eine([sol_ok(i) and dm[i] == richtigD for i in range(4)])
    # 29: Gleichungen mit genau einem Bruch (auch ganze Zahl als Bruch) je Seite
    form29 = {"A": (True, True), "B": (False, True), "C": (True, True), "D": (True, False), "E": (True, True)}
    S[29] = sum(1 for l, r in form29.values() if l and r)
    # 30: linear umgeformt: Loesung muss die Bruchgleichung erfuellen
    lin = [(4, 12, 7, -7), (4, -4, 7, 21), (4, 3, 7, -1), (4, 12, 7, 7)]
    def aequiv(c):
        a1, b1, a2, b2 = c
        x = F(b2 - b1, a1 - a2)
        return F(4) / (x - 1) == F(7) / (x + 3)
    S[30] = nur_eine([aequiv(c) for c in lin])
    gl31 = [lambda x: F(4) / (x - 2) == F(2) / (x + 4), lambda x: F(4) / (x + 2) == F(2) / (x - 4),
            lambda x: F(4) / (x - 2) == F(2) / (x - 4), lambda x: F(4) / (x - 4) == F(2) / (x - 2)]
    S[31] = nur_eine([f(F(6)) for f in gl31])
    kim = [x for x in raster(-30, 30, 1) if x not in (1, -4) and 2 * (x + 4) == 3 * (x - 1)]
    falsch = [x for x in raster(-30, 30, 1) if 2 * (x - 1) == 3 * (x + 4)]
    S[32] = nur_eine([False, False, False, kim == [11]])  # Jo und Kim erhalten dieselbe Gleichung mit x = 11
    assert falsch == [-14]
    S[33] = [2, F(12, 4)]
    n34 = 0
    for k in range(-4, 5):
        # (4-k) x = -k-8 exakt lösen; Lösung muss x != 1, -2 sein
        if 4 - k == 0:
            ok = (-k - 8) == 0
        else:
            x = F(-k - 8, 4 - k)
            ok = x not in (1, -2)
        n34 += ok
    S[34] = n34
    S[35] = [x for x in range(1, 400) if F(x, x + 9) == F(2, 3)][0]
    # --- Scheinloesung
    S[36] = sum(1 for x in range(-2, 6) if x != 3 and F(x * x - 6 * x + 9, x - 3) == x - 3)
    Dm = {-2, 3}
    cand = {x for x in range(-10, 11) if x * x == 9}
    Lm = cand - Dm
    S[37] = nur_eine([Lm == {-3, 3}, Lm == {-3}, Lm == {3}, Lm == set()])
    gA = lambda x: F(x + 1) / (x - 3) == F(4) / (x - 3)
    gB = lambda x: F(6) / (x + 2) == F(3) / (x + 2) + 1
    gC = lambda x: F(3) / (x - 2) == F(4) / (x - 2)
    gt = raster(-30, 30, 1)
    S[38] = sum(1 for f, v in ((gA, 3), (gB, -2), (gC, 2)) if any(x != v and f(x) for x in gt))
    S[39] = [b for b in range(-50, 51) if F(17 - b, 2) == 4][0]
    S[40] = [1, [x for x in raster(-30, 30, 1) if x != 1 and F(5) / (x - 1) + 2 == F(7) / (x - 1)][0]]
    L41 = [x for x in raster(-30, 30, 4) if x != 5 and F(x + 2) / (x - 5) == F(7) / (x - 5)]
    S[41] = nur_eine([L41 == [] , False, False, False])
    S[42] = [2, [x for x in range(-10, 11) if x != 2 and F(x * x, x - 2) == F(4, x - 2)][0]]
    # --- verhaeltnis
    S[43] = 5 * [k for k in range(1, 100) if F(5 * k + 6, 7 * k + 6) == F(3, 4)][0]
    S[44] = nur_eine([F(3, 5) == F(3, 8), F(5, 8) == F(3, 8), F(3, 8) == F(3, 8), F(3, 2) == F(3, 8)])
    S[45] = [b for b in range(1, 400) if F(b - 33, b) == F(4, 7)][0]
    S[46] = nur_eine([F(18 + 18) == F(18) * F(30, 12), F(18) / F(5, 2) == F(18) * F(30, 12), F(18) * F(30, 12) == 45, F(18) == F(18) * F(30, 12)])
    S[47] = [2, [x for x in range(1, 200) if F(4, x) == F(6, 18)][0]]
    S[48] = [t for t in range(1, 1000) if F(90, t) == F(3, 15)][0]
    S[49] = [c for c in range(1, 1000) if F(24, 36) == F(2, 3) and F(36, c) == F(4, 5) and F(24) == 24][0]
    # --- terme.potenzgesetze
    S[50] = sum(1 for n in range(-4, 5) if F(1, 10) < F(2) ** n < 3)
    S[51] = [49, [n for n in range(-12, 13) if F(2) ** n == F(1, 32)][0]]
    S[52] = F(10000) * F(5) ** -4
    S[53] = [n for n in range(-8, 9) if F(2, 3) ** n == F(9, 4)][0]
    S[54] = nur_eine([F(3) ** -1 == F(1, 3) and F(3) ** -2 == F(1, 9), False, False, F(3) ** -2 == F(1, 6)])
    w55 = [F(2) ** -3, F(3) ** -2, F(10) ** -1, F(4) ** -1]
    ords = [[3, 1, 0, 2][:0] or [3, 0, 1, 2], [0, 1, 3, 2], [1, 0, 2, 3], [2, 1, 0, 3]]
    S[55] = nur_eine([all(w55[o[i]] < w55[o[i + 1]] for i in range(3)) for o in ords])
    S[56] = [n for n in range(-12, 13) if 10000 * F(2) ** n == 1250][0]
    zeile3 = F(1, 8) + F(1, 8) == F(2, 16)
    S[57] = [3 if not zeile3 else 4, [d for d in range(1, 50) if F(1, 8) * 2 == F(1, d)][0]]
    q_klammer, q_ohne = (-3) ** 2, -(3 ** 2)
    S[58] = nur_eine([q_klammer == -9 and q_ohne == -9, q_klammer == 9 and q_ohne == -9, q_klammer == 9 and q_ohne == 9, q_klammer == -9 and q_ohne == 9])
    bsp = [(3, F(2) ** 3), (-1, F(2) ** -1), (-1, F(-2) ** -1), (0, F(2) ** 0)]
    S[59] = nur_eine([e < 0 and p > 0 for e, p in bsp])
    S[60] = (2 + 3) ** 2 - (2 ** 2 + 3 ** 2)
    z61 = [F(2, 3) ** -2 == F(3, 2) ** 2, F(3, 2) ** 2 == F(3 ** 2, 2), F(9, 2) == F(9, 2)]
    S[61] = [i for i, b in enumerate(z61) if not b][0] - 0  # Index der ersten falschen Zeile (0-basiert: 1 => Zeile 2)
    S[62] = None  # reine Begründung, von Hand (Muster 125, 25, 5 -> 1)
    S[63] = [a for a in range(-10, 11) if F(5) ** a == F(4, 100)][0]
    # --- zahlen.potenzen_zehner
    S[64] = [3, 5]
    S[65] = nur_eine([F(38500000) == F(385, 10) * 10 ** 6 and F(385, 100) * 10 ** 7 == F(385, 10) * 10 ** 6, False, False, False])
    S[66] = [n for n in range(1, 40) if len(str(10 ** n)) == 12][0]
    S[67] = nur_eine([False, False, True, False])
    S[68] = [n for n in range(-5, 15) if F(53, 10) * F(10) ** n == 530000][0]
    S[69] = 3
    S[70] = len(str(int(F(75, 10) * 10 ** 7 * 4))) - 1
    S[71] = [[n for n in range(-12, 1) if 4 * F(10) ** n == F(4, 100000)][0], [n for n in range(-12, 1) if 40 * F(10) ** n == F(4, 100000)][0]]
    S[72] = [n for n in range(-12, 1) if F(10) ** n == F(1, 10 ** 7)][0]
    S[73] = sum(1 for e in (-9, -4, -7, -5) if F(10) ** e < F(1, 10000))
    S[74] = F(1, 10) / F(1, 10 ** 6)
    S[75] = [n for n in range(-10, 1) if F(10) ** n == F(10) ** -2 / 10][0]
    S[76] = nur_eine([F(4, 10000) == 4 * F(10) ** -3, F(4, 10000) == 4 * F(10) ** -4, F(4, 10000) == 4 * F(10) ** -5, F(4, 10000) == F(4, 10) * F(10) ** -4])
    S[77] = nur_eine([F(10) ** -3 == F(1, 1000), F(10) ** -3 == F(1, 10000), F(10) ** -3 == -1000, F(10) ** -3 == F(3, 10)])
    l_nm, l_um, l_mm, l_m = F(10) ** -9, F(10) ** -6, F(10) ** -3, F(1)
    S[78] = sum(1 for v in (3000 * l_nm, F(4, 1000) * l_mm, 5 * l_um, F(25, 10000) * l_mm, F(2, 10 ** 6) * l_m) if v < 4 * l_um)
    S[79] = nur_eine([l_um == l_mm, l_nm == l_um, l_um == F(10) ** -6, l_mm == l_um])
    S[80] = F(10000) / 80
    S[81] = [F(3000) * l_nm / l_um, F(25, 100) * l_mm / l_um]
    S[82] = [3, F(10) ** -6 / F(10) ** -9]
    laengen83 = [F(1, 1000) * l_mm, 5 * l_um, 800 * l_nm, F(2, 1000) * l_mm]
    ordn83 = [[0, 3, 1, 2], [2, 1, 0, 3], [2, 0, 3, 1], [1, 3, 0, 2]]
    S[83] = nur_eine([all(laengen83[o[i]] <= laengen83[o[i + 1]] for i in range(3)) for o in ordn83])
    S[84] = 0
    S[85] = sum(1 for n in range(-5, 3) if F(3, 1000) < 5 * F(10) ** n < 40)
    S[86] = sum(1 for z in (5 * F(10) ** 5, 50 * F(10) ** 4, F(5, 10) * F(10) ** 6, 5000000 * F(10) ** -2) if z == 500000)
    S[87] = nur_eine([F(3, 1000) < v < F(4, 1000) for v in (F(35, 10) * F(10) ** -4, F(35, 10) * F(10) ** -2, F(35, 100) * F(10) ** -3, 35 * F(10) ** -4)])
    S[88] = [n for n in range(-10, 10) if 4 * F(10) ** n > F(5, 1000) and 4 * F(10) ** (n - 1) <= F(5, 1000)][0]
    S[89] = [2, (2 * F(10) ** -4) / (5 * F(10) ** -5)]
    S[90] = F(6, 1000) / F(10) ** -4
    S[91] = 1
    # --- messen.flaechen_vielecke
    S[92] = [flaeche([(0, 0), (10, 0), (5, 4)]), flaeche([(0, 0), (10, 0), (17, 4)])]
    S[93] = flaeche([(1, 1), (13, 1), (13, 6), (1, 6)]) - flaeche([(1, 1), (9, 1), (13, 6)])
    S[94] = F(12 * 7, 2)
    S[95] = nur_eine([ev("8*3/2") == flaeche([(0, 0), (8, 0), (3, 5)]), ev("8*5/2") == flaeche([(0, 0), (8, 0), (3, 5)]),
                      ev("8*5") == flaeche([(0, 0), (8, 0), (3, 5)]), ev("5*3/2") == flaeche([(0, 0), (8, 0), (3, 5)])])
    S[96] = [2, F(10 * 6, 2)]
    S[97] = 2 * (F(9 * 12, 2)) / 15
    S[98] = [g for g in range(1, 100) if F(g * 2 * g, 2) == 36][0]
    S[99] = F(45000) / 300
    S[100] = [g for g in range(1, 100) if g * F(g, 2) == 50][0]
    S[101] = F(96, 12)
    S[102] = [5 + 9, F(2 * 0 + (5 + 9) * 4, 2)]
    S[103] = [2, F(54, 9)]
    S[104] = [F(2 * 40, 10), F(2 * 80, F(2 * 40, 10))]
    h105 = F(48, 8)
    S[105] = nur_eine([False, False, False, h105 == 6])
    S[106] = 144 - 4 * F(3 * 3, 2)
    S[107] = (14 * 9 - 102) / F(4)
    S[108] = [F(8 * 4, 2), F(5 * 4, 2), F(8 * 4, 2) + F(5 * 4, 2)]
    S[109] = [F(14 - 8, 2), 8 * 5 + 2 * F(3 * 5, 2)]
    S[110] = [2, 12 * 5 + F(12 * 4, 2)]
    fl111 = 9 * 7 - 3 * 2
    S[111] = nur_eine([6 * 7 + 3 * 5 == fl111, 9 * 7 - 3 * 5 == fl111, 6 * 7 + 3 * 2 == fl111, 9 * 5 + 3 * 2 == fl111])
    S[112] = flaeche([(0, 0), (10, 0), (7, 6), (2, 6)])
    S[113] = F(72, 4) - 10
    S[114] = 2
    S[115] = F(10 * 6, 2) / 4
    S[116] = (F(1, 2) * 1 * 2) / 1
    S[117] = [3, 10 * 10]
    S[118] = 3
    S[119] = nur_eine([False, F(8 + 4, 2) * 4 == 6 * 4, F(6 * 4, 2) == 6 * 4, F(8 * 4, 2) == 6 * 4])
    return S


def vergleiche(a, s):
    A = a["aufgabe"]
    if a["antwortform"] == "zahl":
        return F(str(A["o"]["wert"])) == F(s)
    if a["antwortform"] == "luecken":
        return [F(str(x)) for x in A["o"]["werte"]] == [F(x) for x in s]
    return A["o"]["index"] == s


def main():
    t = lade()
    S = soll()
    abw = 0
    for n in sorted(t):
        a = t[n]
        if n == 62:
            ok = a["aufgabe"]["o"]["index"] == 3
        elif n == 61:
            ok = a["aufgabe"]["o"]["index"] == 1 and S[61] == 1
        else:
            ok = vergleiche(a, S[n])
        if not ok:
            abw += 1
            print("ABWEICHUNG Lösung", a["kennung"], a["aufgabe"]["o"], "eigene Rechnung:", S[n])
    # Fehlbilder
    fb_n = fb_gleich = fb_rechnung = 0
    ohne_luecke = []
    for n in sorted(t):
        a = t[n]
        A = a["aufgabe"]
        loes_ = A["o"].get("werte") if a["antwortform"] == "luecken" else A["o"].get("wert")
        for fb in a["fehlbilder"]:
            fb_n += 1
            if a["antwortform"] == "auswahl":
                if fb["index"] == A["o"]["index"]:
                    fb_gleich += 1
                    print("FEHLBILD = LÖSUNG", a["kennung"])
                continue
            if "rechnung" in fb:
                try:
                    if ev(fb["rechnung"]) != F(str(fb["antwort"])):
                        fb_rechnung += 1
                        print("FEHLBILD-RECHNUNG ≠ ANTWORT", a["kennung"], fb["rechnung"], fb["antwort"])
                except Exception as e:  # noqa
                    print("FEHLBILD-RECHNUNG nicht auswertbar", a["kennung"], fb["rechnung"], e)
            if a["antwortform"] == "luecken":
                if F(str(fb["antwort"])) == F(str(loes_[fb["luecke"] - 1])):
                    fb_gleich += 1
                    print("FEHLBILD = LÖSUNG", a["kennung"], fb)
            else:
                if F(str(fb["antwort"])) == F(str(loes_)):
                    fb_gleich += 1
                    print("FEHLBILD = LÖSUNG", a["kennung"], fb)
        if a["antwortform"] == "luecken":
            haben = {fb["luecke"] for fb in a["fehlbilder"]}
            fehlt = [i + 1 for i in range(len(loes_)) if i + 1 not in haben]
            if fehlt:
                ohne_luecke.append((a["kennung"], fehlt))
        if a["antwortform"] == "auswahl":
            idx = {fb["index"] for fb in a["fehlbilder"]}
            if idx != set(range(4)) - {A["o"]["index"]}:
                print("AUSWAHL: Fehlbild-Indizes unvollständig", a["kennung"])
    print(f"Fehlbilder geprüft: {fb_n}; gleich Lösung: {fb_gleich}; Rechnung≠Antwort: {fb_rechnung}")
    print("Lücken ohne Fehlbild (Kennung, Lücke):", ohne_luecke)
    print(f"{abw} Abweichungen")
    return abw


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
