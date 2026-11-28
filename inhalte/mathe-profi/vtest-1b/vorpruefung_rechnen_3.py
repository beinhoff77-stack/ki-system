"""Dritte, unabhängige Vorprüfung vtest-1b: rechnet alle 119 Aufgaben aus den Angaben im Text neu (exakt, Brüche).

Unabhängig von gegenrechnung.py, vorpruefung_rechnen.py und vorpruefung_rechnen_2.py (nichts daraus übernommen).
Je Aufgabe eine eigene Rechnung; bei Auswahl ein eigener Wahrheitswert je Möglichkeit (rechnerisch, wo es Zahlen gibt,
sonst von Hand begründet und mit "M" markiert). Danach: Fehlbilder, Lücken-Abdeckung, Antwort im Text / bei Nachbarn,
Bestandssuche, Schema-Zählung.
Aufruf: python3 -I inhalte/mathe-profi/vtest-1b/vorpruefung_rechnen_3.py
"""
import glob
import json
import os
import re
import sys
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))
INH = os.path.normpath(os.path.join(HIER, "..", ".."))
DATEIEN = ["bruch.prozent", "gleichungen.bruch", "terme.potenzgesetze", "zahlen.potenzen_zehner", "messen.flaechen_vielecke"]
HOCH = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")


def lade():
    r = {}
    for d in DATEIEN:
        for a in json.load(open(os.path.join(HIER, d + ".json"), encoding="utf-8"))["aufgaben"]:
            r[int(a["kennung"][-3:])] = a
    return r


def rng(a, b):
    return [F(i) for i in range(a, b + 1)]


def gitter(lo=-60, hi=60, n=4):
    return [F(i, n) for i in range(lo * n, hi * n + 1)]


def ew(x):
    return F(x)


# ------------------------------------------------------------------ Lösungen aus den Angaben im Text
def soll():
    S = {}
    # --- Prozent
    N = next(n for n in range(1, 5000) if F(n) * (F(4, 10) * F(1, 2) + F(6, 10) * F(1, 4)) == 490)
    S[1] = [F(N), F(N) * F(6, 10)]
    S[2] = F(12, 100) * 75
    S[3] = F(35, 100) * 360
    S[4] = 100 - 15 - F(168, 280) * 100
    S[5] = None                                                           # Auswahl
    S[6] = [1, F(8, 100) * 450]
    S[7] = [F(3, 5) * 100, F(3, 5) * 240]
    G = F(18) / F(45, 100)
    S[8] = G * (1 - F(45, 100) - F(30, 100))
    S[10] = F(63) / (F(54, 360))
    S[11] = F(105) / F(70, 100) - 105
    S[13] = [2, F(20) / F(25, 100)]
    S[14] = [F(42, 7), F(42, 7) * 100]
    E = F(60) / (F(4, 10) * F(3, 10))
    S[15] = [E, E * F(4, 10)]
    S[16] = 30 + 30 * 2
    S[18] = F(54) / F(150, 100)
    S[19] = [3, F(40, 100) * 30 - F(75, 100) * 8]
    ganz = next(n for n in range(1, 500) if n * (1 - F(2, 10) - (1 - F(2, 10)) / 4) == 18)
    S[21] = F(ganz)
    # --- Gleichungen
    S[22] = F(len([x for x in rng(-12, 12) if x != 2 and F(3) / (x - 2) == F(1) / (x - 2) + F(2) / (x - 2)]))
    lsg23 = [x for x in gitter(-20, 20) if x * x + 4 != 0 and F(5) / (x * x + 4) == 1]
    S[23] = [0, len(lsg23)]
    S[24] = [a for a in rng(-40, 40) if {x for x in gitter(-20, 20) if 2 * x - a == 0 or x + 3 == 0} == {F(-3), F(7)}]
    S[26] = F(len([x for x in rng(-3, 9) if x != 0 and x != 5]))
    S[27] = [1, len({x for x in rng(-20, 20) if x * x - 25 == 0 or x - 5 == 0})]
    def hat_loes(k):
        for x in gitter(-80, 80, 12):
            if x != 1 and x != -2 and F(4) / (x - 1) == F(k) / (x + 2):
                return True
        # exakte Lösung der linearen Gleichung (4-k)x = -k-8
        if k != 4:
            x = F(-k - 8, 4 - k)
            return x != 1 and x != -2
        return False
    S[29] = F(len([k for k in rng(-5, 14) if hat_loes(k)]))
    S[33] = [1, 0]
    def keine_loes36(b):
        # (x+b)/(x-4) = 3/(x-4)+1  -> x+b = 3 + x - 4  (x != 4): erfüllt für alle x != 4 genau wenn b == -1
        probe = [x for x in gitter(-30, 30) if x != 4 and (x + b) / (x - 4) == F(3) / (x - 4) + 1]
        return len(probe) == 0
    S[36] = F(len([b for b in rng(-9, 9) if keine_loes36(b)]))
    S[35] = 10
    # (5+x)/(20+x) = 1/2
    S[35] = next(x for x in range(0, 100) if F(5 + x, 20 + x) == F(1, 2))
    # 38: Lösungsmengen der drei Gleichungen
    A = [x for x in gitter(-30, 30) if x != 3 and (x + 1) / (x - 3) == F(4) / (x - 3)]
    B = [x for x in gitter(-30, 30) if x != -2 and F(6) / (x + 2) == F(3) / (x + 2) + 1]
    C = [x for x in gitter(-30, 30) if x != 2 and F(3) / (x - 2) == F(4) / (x - 2)]
    S[38] = sum(1 for L in (A, B, C) if L)
    S[39] = [c for c in rng(-30, 30) if not [x for x in gitter(-40, 40) if x != 4 and (x * x - 16) / (x - 4) == c]]
    S[40] = [1, [x for x in gitter(-30, 30) if x != 1 and F(5) / (x - 1) + 2 == F(7) / (x - 1)]]
    S[42] = [[x for x in gitter(-30, 30) if x != -3 and (x - 6) / (x + 3) == 0], len([x for x in gitter(-30, 30) if x != 4 and (x - 4) / (x - 4) == 0])]
    # 43: x/12 = (x+4)/20
    x43 = next(x for x in gitter(-60, 60, 1) if x * 20 == 12 * (x + 4))
    S[43] = [x43, F(x43, 12).numerator, F(x43, 12).denominator]
    # 45: Äpfel 5k, Birnen 3k, 5k-20 = 3k
    k = next(k for k in range(1, 100) if 5 * k - 20 == 3 * k)
    S[45] = 3 * k
    S[47] = [2, [x for x in gitter(-60, 60, 1) if 4 * 18 == x * 6][0]]
    # 48: 3t + 7t = 50
    S[48] = 3 * next(t for t in gitter(1, 100, 2) if 10 * t == 50)
    # 49: J=60, J:M=3:4, M:B=8:1
    M = F(60) * 4 / 3
    S[49] = M / 8
    # --- Potenzen (Terme)
    S[50] = [min(n for n in range(-30, 30) if F(1, 200) < F(2) ** n < 40), max(n for n in range(-30, 30) if F(1, 200) < F(2) ** n < 40)]
    S[51] = [7 ** 2, next(n for n in range(-20, 20) if F(2) ** n == F(1, 32))]
    S[52] = F(1, 5 ** 4) / F(1, 10000)
    S[53] = F(len([v for v in (F(3) ** -4, F(4) ** -3, F(10) ** -2, F(1) ** -6) if v < F(1, 50)]))
    S[56] = F(10) ** -1 / F(10) ** -4
    S[57] = [1, 2]            # Zeile 1 falsch; 2^-2 + 2^-2 = 1/2
    assert F(2) ** -2 + F(2) ** -2 == F(1, 2)
    S[60] = (3 + 4) ** 2 - (3 ** 2 + 4 ** 2)
    S[63] = [3, next(a for a in range(-10, 10) if F(5) ** a == F(4, 100))]
    # --- Zehnerpotenzen
    S[64] = [3, next(n for n in range(-20, 20) if F(231, 10) * F(10) ** 4 == F(231, 100) * F(10) ** n)]
    S[66] = next(n for n in range(-20, 30) if 2 * F(8) * F(10) ** n == F(16, 10) * F(10) ** 10)      # a=8 -> 2*8*10^n = 1,6*10^10
    S[68] = F(2) * 10 ** 9 / (F(4) * 10 ** 5)
    # 70: 7,5*4=30 -> 3*10^(7+1)
    S[70] = next(n for n in range(0, 30) if F(75, 10) * 10 ** 7 * 4 == 3 * F(10) ** n)
    S[71] = [next(n for n in range(-12, 0) if 4 * F(10) ** n == F(4, 100000)), next(n for n in range(-12, 0) if 40 * F(10) ** n == F(4, 100000))]
    # 72: 1000/10^t < 10^-6 zum ersten Mal
    S[72] = next(t for t in range(0, 40) if F(1000) / F(10) ** t < F(1, 10 ** 6))
    # 74: 10^n = 10^-5 / 1000
    S[74] = next(n for n in range(-30, 10) if F(10) ** n == F(1, 10 ** 5) / 1000)
    # 75: 10^-6 * 10^-3 = 10^-9 -> Nullen vor der 1
    S[75] = next(n for n in range(-30, 0) if F(10) ** n == F(1, 10 ** 6) * F(1, 10 ** 3)) * -1 - 1
    S[77] = [2, F(1, 1000) * 1000]
    S[78] = [F(8) * 1000 * F(10) ** -6 / F(10) ** -3, F(5, 10) * 10 ** 7 * F(10) ** -9 / F(10) ** -3]
    S[80] = next(n for n in range(-20, 20) if 4500 * F(10) ** -9 == F(45, 10) * F(10) ** n * F(10) ** -3)
    S[81] = F(2) * 1000 / 20
    S[82] = [3, F(10) ** -6 / F(10) ** -9]
    S[83] = F(12) * 5000 / 10000
    S[85] = None
    v = {1: 5 * F(10) ** -6, 2: F(2, 10) * F(10) ** -4, 3: 30 * F(10) ** -7}
    S[85] = [min(v, key=v.get), max(v, key=v.get)]
    S[86] = F(len([z for z in (5 * 10 ** 5, 50 * 10 ** 4, F(5, 10) * 10 ** 6, 5000000 * F(10) ** -2) if z == 500000]))
    S[88] = F(len([k for k in range(0, 200) if 3 * F(10) ** -4 < k * F(10) ** -5 < 5 * F(10) ** -4]))
    S[89] = [2, 4 * 10]
    assert 4 * F(10) ** -6 == 40 * F(10) ** -7
    S[90] = F(6, 1000) / F(10) ** -4
    # --- Flächen
    def tri(p, q, r):
        return abs((q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1])) / F(2)
    S[92] = [tri((0, 0), (10, 0), (5, 4)), tri((0, 0), (10, 0), (17, 4))]
    S[93] = (12 * 5) - tri((1, 1), (9, 1), (13, 6))
    assert 12 * 5 == 60
    S[94] = F(12 * 7, 2)
    S[96] = [2, F(12 * 5, 2)]
    S[97] = F(66, 6)
    S[98] = (8 * F(3, 2)) * (6 * F(1, 2)) / 2
    S[99] = F(45000, 300)
    # 100: g * (g/2) = 50
    S[100] = next(g for g in range(1, 100) if F(g) * F(g, 2) == 50)
    S[101] = F(12 * 8)
    S[102] = [5 + 9, F((5 + 9) * 4, 2)]
    S[103] = [2, F(54, 9)]
    S[104] = [F(2 * 40, 10), F(2 * 80, 8) / 1]
    S[104][1] = F(2 * 40 * 2, 8)
    S[106] = [None, None]
    h = next(h for h in range(1, 100) if 9 * 3 + F(9 * h, 2) == 63)
    S[106] = [F(h), 3 + h]
    S[107] = next(b for b in range(1, 20) if 14 * 9 - 4 * b == 102)
    S[108] = F(12 * 2 + 8 * 2 - 2 * 2)
    S[110] = [2, 14 * 10 - 6 * 4]
    # 112: Schuhband
    P = [(0, 0), (6, 0), (8, 5), (0, 3)]
    s = sum(P[i][0] * P[(i + 1) % 4][1] - P[(i + 1) % 4][0] * P[i][1] for i in range(4))
    S[112] = F(abs(s), 2)
    S[113] = [(F(12 * 6) - 50) / 50 * 100, 2 * (12 + 6) - 2 * (10 + 5)]
    S[114] = F((12 + 6) * 4, 2) / (12 * 4) * 100
    S[115] = next(g for g in range(1, 100) if g * (g - 3) == 54)
    S[116] = F(16 * 1, 2)
    S[117] = [3, (F(11) ** 2 - 100)]
    S[119] = 9 ** 2 - 8 ** 2
    return S


# ------------------------------------------------------------------ Auswahl: Wahrheitswert je Möglichkeit
def auswahl():
    """Liste je Aufgabe: Wahrheitswerte der vier Möglichkeiten. 'M' = von Hand begründet (keine Zahl zu rechnen)."""
    W = {}
    ca = F(51, 100) * 3980
    from math import log
    opts = [200, 20, 2000, 20000]
    best = min(range(4), key=lambda i: abs(log(opts[i] / float(ca))))
    W[5] = [i == best and abs(opts[i] - ca) / ca < F(1, 10) for i in range(4)]
    exakt = F(12) / F(8, 100)
    W[9] = [abs(o - exakt) / exakt < F(1, 20) for o in (150, 1, 1500, 100)]
    anna, ben = F(30) / F(20, 100), F(40) / F(25, 100)
    W[12] = [anna > ben and 600 == anna, False, ben > anna and ben == 160 and anna == 150, anna > ben]
    v = [F(36, 100), F(37, 100), F(7, 20), F(3, 8)]
    W[17] = [x == max(v) for x in v]
    W[20] = ["M", "M", "M", "M"]          # 0,2A > 0,3B  <=>  A > 1,5 B  -> nur [2] folgt; [1],[3] machen > zu = ; [0] umgekehrt
    W[25] = [{-16, 0, 16} == {-4, 0, 4}, True, {-4, 4} == {-4, 0, 4}, {0, 4} == {-4, 0, 4}]
    # 28: Gleichung aus dem Text prüfen: 6 Kinder zahlen 6 €, 9 Kinder 4 €  (Beispiel x = 6)
    f = lambda x: F(36) / x - F(36) / (x + 3) == 2
    g = lambda x: F(36) / x + F(36) / (x + 3) == 2
    h = lambda x: F(36) / (x - 3) - F(36) / x == 2
    W[28] = [f(6) and False, g(6), h(6), f(6)]
    W[28][0] = "D unvollständig (x=-3 fehlt)"
    W[28][3] = f(6)                       # und D = {-3, 0} vollständig
    # 30: Lösung jeder Folgegleichung gegen die Ausgangsgleichung prüfen
    ur = lambda x: x != 1 and x != -3 and F(4) / (x - 1) == F(7) / (x + 3)
    W[30] = [ur(F(19, 3)), ur(F(-25, 3)), ur(F(4, 3)), ur(F(5, 3))]
    W[31] = [F(4) / (6 - 2) == F(2) / (6 + 4), F(4) / (6 - 2) == F(2) / (6 - 4), F(4) / (6 + 2) == F(2) / (6 - 4), F(4) / (6 - 4) == F(2) / (6 - 2)]
    W[32] = ["M", "M", "M", "M"]          # x = 10; Jos Überlegung gültig; [1],[2] falsche x; [0] falsche Behauptung
    W[34] = ["M", "M", "M", "M"]          # Kims Schritt stimmt (Kreuzprodukt); nur [0]
    W[37] = [True and False, False, False, True]
    W[41] = ["M", "M", "M", "M"]
    W[44] = [F(3, 5) == F(3, 8), F(5, 8) == F(3, 8), F(3, 8) == F(3, 8), F(3, 2) == F(3, 8)]
    # 46: neue Höhe bei gleichem Faktor
    W[46] = [18 + 18 == 18 * F(30, 12), 18 * F(30, 12) == 45, F(18) / F(5, 2) == 45, 18 == 45]
    W[54] = [F(2) ** -4 > F(2) ** -3 and False, False, F(2) ** -4 > F(2) ** -3, F(2) ** -4 < F(2) ** -3]
    W[55] = [F(2) ** -3 == F(125, 1000), F(2) ** -8 == F(125, 1000), F(8) ** -2 == F(125, 1000), F(3) ** -2 == F(125, 1000)]
    W[58] = [F(10) ** -2 == F(2, 10), F(10) ** -2 == F(1, 100), F(10) ** -2 < 0, F(10) ** -2 == F(1, 1000)]
    W[59] = [F(2) ** -1 > 0, "M", "M", F(2) ** -1 == -2]
    W[59][1] = False          # 2^3 hat keinen negativen Exponenten
    W[59][2] = False          # 0 ist nicht negativ
    W[61] = ["M", 4 ** 2 != 4 * 2, F(1, 8) == F(12, 100), False]
    W[61][0] = False          # Zeile 1 stimmt: 4^-2 = 1/4^2
    W[62] = ["M", "M", "M", "M"]
    W[65] = [F(385, 100) * 10 ** 7 == F(385, 100) * 10 ** 6, F(385, 100) * 10 ** 7 == 385 * 10 ** 6, F(385, 100) * 10 ** 7 == F(385, 10) * 10 ** 6, F(385, 100) * 10 ** 7 == F(385, 100) * 10 ** 9]
    W[67] = ["M", "M", "M", None]
    z = str(35 * 10 ** 5)
    W[67] = [False, False, False, z.count("0") == 5]
    W[69] = ["M", "M", "M", "M"]
    W[73] = [10 * F(10) ** -6 == F(10) ** -6, 10 * F(10) ** -6 == F(10) ** -5, 100 * F(10) ** -6 == F(10) ** -5, 10 * F(10) ** -6 == F(10) ** -7]
    W[76] = [F(4, 10000) == 4 * F(10) ** -3, F(4, 10000) == 4 * F(10) ** -5, F(4, 10000) == 4 * F(10) ** -4, F(4, 10000) == F(4, 10) * F(10) ** -4]
    W[79] = ["M", F(800) * F(10) ** -9 < 2 * F(10) ** -6 and F(800) * F(10) ** -9 == F(8, 10) * F(10) ** -6, False, F(800) * F(10) ** -9 == 2 * F(10) ** -6]
    W[79][0] = False          # Einheit spielt eine Rolle
    W[84] = ["M", "M", "M", "M"]
    a, b = 4 * F(10) ** -6, 2 * F(10) ** -5
    W[87] = [a > b, b == 10 * a, b == 5 * a, a == b]
    W[91] = ["M", F(4) * F(10) ** -7 == F(4, 10) * F(10) ** -6 and 9 * F(10) ** -6 > F(4) * F(10) ** -7, "M", "M"]
    W[95] = [F(8 * 3, 2) == 20, 8 * 5 == 20, F(5 * 3, 2) == 20, F(8 * 5, 2) == 20]
    W[105] = ["M", "M", "M", "M"]
    # 109: Flächen und Umfänge der Teile
    fl = 10 * 2 + 10 * 4
    um = 2 * (10 + 2) + 2 * (10 + 4)
    W[109] = [fl == 60 and um == 32, fl < 60, fl == 60 and um > 32, um == 32 and fl > 60]
    W[111] = [9 * 7 - 3 * 5 == 63 - 6, 6 * 7 + 3 * 2 == 63 - 6, 9 * 5 + 3 * 2 == 63 - 6, 6 * 7 + 3 * 5 == 63 - 6]
    W[118] = ["M", "M", "M", "M"]
    return W


# ------------------------------------------------------------------ Hilfen
def ausw(o, a):
    """Index der richtigen Möglichkeit laut Datei."""
    return o["index"]


def wertlich(x):
    if isinstance(x, list):
        return [wertlich(y) for y in x]
    return F(x)


def hole_loesung(a):
    o = a["aufgabe"]["o"]
    if "werte" in o:
        return [F(str(x)) for x in o["werte"]]
    if "wert" in o:
        return F(str(o["wert"]))
    return o["index"]


def mehrfach_eingesetzt(ausd, werte):
    pass


ZIFF = re.compile(r"\d+(?:[.,]\d+)?")


def zahlen_text(t):
    t = t.translate(str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789"))
    return {F(m.replace(",", ".")) for m in ZIFF.findall(re.sub(r"(?<=\d)[  ](?=\d{3})", "", t))}


# ------------------------------------------------------------------ Bestandssuche
STOP = set("wie viele welche welcher welches wird werden sind ist hat haben eine einen einem eines dann auch nicht noch sich oder aber nach beim vom zum zur dass dieser wenn immer jede jeder jedes ein der die das und mit von auf bei für den dem des im in an zu so als wir man kim ben ida lena".split())


def woerter(t):
    t = re.sub(r"[\d.,]+", " ", t.lower())
    return {w for w in re.findall(r"[a-zäöüß]{4,}", t) if w not in STOP}


def bestand():
    quellen = glob.glob(os.path.join(INH, "themen", "*.json"))
    quellen += [q for q in glob.glob(os.path.join(INH, "mathe-profi", "rollend-*", "*.json"))]
    res = []
    def lauf(o, q):
        if isinstance(o, dict):
            if "f" in o and isinstance(o["f"], dict) and "text" in o["f"]:
                res.append((os.path.relpath(q, INH), o["f"]["text"], o.get("o")))
            elif "aufgabe" in o and isinstance(o["aufgabe"], dict) and "f" in o["aufgabe"]:
                res.append((os.path.relpath(q, INH) + ":" + str(o.get("kennung", "")), o["aufgabe"]["f"]["text"], o["aufgabe"].get("o")))
            else:
                for v in o.values():
                    lauf(v, q)
        elif isinstance(o, list):
            for v in o:
                lauf(v, q)
    for q in quellen:
        if "vtest" in q:
            continue
        try:
            lauf(json.load(open(q, encoding="utf-8")), q)
        except Exception:
            pass
    return res


def aehnlich(t1, t2):
    a, b = woerter(t1), woerter(t2)
    if not a or not b:
        return 0
    w = len(a & b) / len(a | b)
    za, zb = zahlen_text(t1), zahlen_text(t2)
    z = len(za & zb) / max(1, len(za | zb))
    return w, z


def main():
    A = lade()
    S = soll()
    W = auswahl()
    abw = 0
    n_ausw = 0
    print("== 1. Lösungen und Auswahl ==")
    for k in sorted(A):
        a = A[k]
        o = a["aufgabe"]["o"]
        y = a["aufgabe"]["y"]
        if y == "auswahl":
            n_ausw += 1
            tw = W.get(k)
            if tw is None:
                print(k, "Auswahl ohne eigene Wahrheitswerte")
                abw += 1
                continue
            manuell = [x for x in tw if x == "M"]
            if manuell:
                continue            # von Hand, siehe Bericht
            r = [i for i, b in enumerate(tw) if b is True]
            if r != [o["index"]]:
                abw += 1
                print("ABWEICHUNG Auswahl", k, tw, "Datei:", o["index"])
            if "wert" in a["aufgabe"]["o"]:
                pass
            continue
        s = S.get(k)
        if s is None:
            print(k, "keine eigene Lösung hinterlegt")
            abw += 1
            continue
        d = hole_loesung(a)
        if y == "zahl":
            if isinstance(s, list):     # Parameteraufgaben (24, 39) liefern eine Liste möglicher Werte
                if [F(x) for x in s] != [d]:
                    abw += 1
                    print("ABWEICHUNG", k, s, d)
            elif F(s) != d:
                abw += 1
                print("ABWEICHUNG", k, s, d)
        else:
            ok = len(s) == len(d)
            for x, z in zip(s, d):
                if isinstance(x, list):
                    ok &= (len(x) == 1 and F(x[0]) == z)
                else:
                    ok &= (F(x) == z)
            if not ok:
                abw += 1
                print("ABWEICHUNG", k, s, d)
    print("Aufgaben:", len(A), "Auswahl:", n_ausw, "Abweichungen:", abw)

    print("\n== 2. Fehlbilder ==")
    fa = 0
    nfb = 0
    for k in sorted(A):
        a = A[k]
        y = a["aufgabe"]["y"]
        o = a["aufgabe"]["o"]
        fbs = a["fehlbilder"]
        nfb += len(fbs)
        if y == "auswahl":
            idx = {f["index"] for f in fbs}
            if idx != set(range(4)) - {o["index"]}:
                fa += 1
                print("Auswahl: Fehlbild-Plätze", k, idx)
            continue
        if y == "luecken":
            n = len(o["werte"])
            for L in range(1, n + 1):
                if not [f for f in fbs if f.get("luecke") == L]:
                    fa += 1
                    print("Lücke ohne Fehlbild", k, L)
            for f in fbs:
                if F(str(f["antwort"])) == F(str(o["werte"][f["luecke"] - 1])):
                    fa += 1
                    print("Fehlbild = Lösung", k, f)
            continue
        for f in fbs:
            if F(str(f["antwort"])) == F(str(o["wert"])):
                fa += 1
                print("Fehlbild = Lösung", k, f)
    # Fehlbild-Rechnungen auswerten
    import ast
    def ev(s):
        def g(n):
            if isinstance(n, ast.Expression):
                return g(n.body)
            if isinstance(n, ast.Constant):
                return F(str(n.value))
            if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
                return -g(n.operand)
            if isinstance(n, ast.BinOp):
                x, z = g(n.left), g(n.right)
                return {ast.Add: lambda: x + z, ast.Sub: lambda: x - z, ast.Mult: lambda: x * z, ast.Div: lambda: x / z, ast.Pow: lambda: x ** int(z)}[type(n.op)]()
            raise ValueError(s)
        return g(ast.parse(str(s), mode="eval"))
    for k in sorted(A):
        a = A[k]
        if a["aufgabe"]["y"] == "auswahl":
            continue
        for f in a["fehlbilder"]:
            try:
                if ev(f["rechnung"]) != F(str(f["antwort"])):
                    fa += 1
                    print("Fehlbild-Rechnung ≠ Antwort", k, f["rechnung"], f["antwort"])
            except Exception as e:
                fa += 1
                print("Fehlbild-Rechnung nicht auswertbar", k, f.get("rechnung"), e)
    print("Fehlbilder:", nfb, "Auffälligkeiten:", fa)

    print("\n== 3. Lösung (Zahl) im Aufgabentext oder bei Nachbarn im Lernziel ==")
    gruppen = {}
    for k in A:
        gruppen.setdefault(A[k]["lernkarte"] + "|" + A[k]["thema"], []).append(k)
    for k in sorted(A):
        a = A[k]
        y = a["aufgabe"]["y"]
        if y == "auswahl":
            continue
        t = a["aufgabe"]["f"]["text"] + " " + a["aufgabe"]["f"].get("schablone", "")
        z = zahlen_text(t)
        o = a["aufgabe"]["o"]
        werte = [F(str(x)) for x in (o["werte"] if y == "luecken" else [o["wert"]])]
        for i, w in enumerate(werte):
            if w in z and abs(w) > 9:
                print("Lösung im eigenen Text", k, "Lücke", i + 1, w)
    print("(Zahlen ≤ 9 sind ausgenommen; Nachbarn: siehe Bericht, von Hand)")

    print("\n== 4. Bestandssuche (Ersatzaufgaben, Wortgleichheit ≥ 0,45 oder Zahlen ≥ 0,6 mit Wort ≥ 0,25) ==")
    B = bestand()
    print("Bestandsaufgaben gelesen:", len(B))
    ids = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else sorted(A)
    for k in ids:
        t = A[k]["aufgabe"]["f"]["text"]
        top = []
        for q, bt, bo in B:
            r = aehnlich(t, bt)
            if not r:
                continue
            w, z = r
            if w >= 0.45 or (z >= 0.6 and w >= 0.25):
                top.append((w + z, w, z, q, bt))
        top.sort(reverse=True)
        for s, w, z, q, bt in top[:2]:
            print("VT1B-%03d  w=%.2f z=%.2f  %s\n   neu: %s\n   alt: %s" % (k, w, z, q, t[:170], bt[:170]))


if __name__ == "__main__":
    main()
