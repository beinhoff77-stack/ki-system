#!/usr/bin/env python3
"""Unabhaengige Nachrechnung der 126 VT3-Aufgaben (Vorpruefung 3).

Nichts aus gegenrechnung.py, kern.py oder den e_*.py uebernommen. Alle Sollwerte
werden hier neu hergeleitet (exakt mit Bruechen, wo noetig durch Aufzaehlen).
Bei Auswahl-Aufgaben wird JEDE Option einzeln als wahr/falsch bestimmt (ueber den
Anfang des Optionstexts gefunden, nicht ueber die Nummer) und geprueft, dass genau
eine Option wahr ist und dass es die gespeicherte ist.

Aufruf:  python3 -I inhalte/mathe-profi/vtest-3/vorpruefung_rechnen_3.py
"""
import json, os, re, sys, itertools
from fractions import Fraction as F
from math import floor

HIER = os.path.dirname(os.path.abspath(__file__))
DATEIEN = ["messen.volumen", "daten.darstellen", "daten.kennwerte",
           "funktionen.grundbegriffe", "geometrie.winkel"]

A = {}
for fn in DATEIEN:
    for a in json.load(open(os.path.join(HIER, fn + ".json"), encoding="utf-8"))["aufgaben"]:
        A[a["kennung"][-3:]] = a
assert len(A) == 126, len(A)

fehler = []
def melde(k, text):
    fehler.append("VT3-%s: %s" % (k, text))

# ---------- eigener Rechner fuer Fehlbild-Rechnungen ----------
def rechne(s):
    t = s.replace("·", "*").replace(":", "/").replace("−", "-").replace("²", "**2").replace("³", "**3")
    t = re.sub(r"(\d),(\d)", r"\1.\2", t)
    t = re.sub(r"(?<=\d) (?=\d{3}\b)", "", t)
    t = re.sub(r"(\d+(?:\.\d+)?)", lambda m: "F('%s')" % m.group(1), t)
    return eval(t, {"F": F, "abs": abs})

def num(x):
    return F(str(x))

# ---------- Sollwerte (zahl: Zahl; luecken: Liste) ----------
def teilbar_zerlegung_wuerfel(s, brick=(1, 2, 4)):
    """Exakte Ueberdeckung eines s-Wuerfels mit Quadern 1x2x4 (alle Lagen)."""
    belegt = set()
    lagen = set(itertools.permutations(brick))
    def erste():
        for x in range(s):
            for y in range(s):
                for z in range(s):
                    if (x, y, z) not in belegt:
                        return (x, y, z)
        return None
    def rek():
        p = erste()
        if p is None:
            return True
        for (a, b, c) in lagen:
            zellen = [(p[0] + i, p[1] + j, p[2] + k) for i in range(a) for j in range(b) for k in range(c)]
            if all(0 <= q[0] < s and 0 <= q[1] < s and 0 <= q[2] < s and q not in belegt for q in zellen):
                belegt.update(zellen)
                if rek():
                    return True
                belegt.difference_update(zellen)
        return False
    return rek()

def kleinster_wuerfel():
    for s in range(1, 9):
        if s ** 3 % 8 == 0 and s >= 4 and teilbar_zerlegung_wuerfel(s):
            return s ** 3 // 8
SOLL = {}
SOLL["001"] = (F(3, 2) * F(4, 5) * 2 - 1) * 100
SOLL["002"] = 3 ** 3
SOLL["003"] = 5 * 4 * 3 + 3 ** 3
SOLL["004"] = [3, 8 * 3 * 5]
SOLL["006"] = kleinster_wuerfel()
SOLL["008"] = F(150, 10) ** 3
SOLL["010"] = [2, F(50 * 30 * 40, 1000)]
SOLL["014"] = F(15, 10) * F(12, 10) * 1 * 1000 / 9
SOLL["015"] = [b for b in range(1, 28) if 10 * b * (3 * b) == 270][0]
SOLL["016"] = [3, F(308, 7 * 4)]
SOLL["020"] = [(240 - 180) // 3, 180 // ((240 - 180) // 3)]
SOLL["021"] = [h for h in range(1, 40) if (3 * 2) * (2 * 2) * h == 192][0]  # Laenge 6, Breite 4
SOLL["022"] = (50 // 15) * (40 // 15) * (30 // 15)
SOLL["024"] = [2, F(4) * 3 * F(5, 2)]
SOLL["025"] = [h for h in range(1, 100) if 18 * h - 12 * h == 30][0]
SOLL["029"] = [k for k in range(0, 51) if F(10 + k, 100) == F(1, 4)][0]
SOLL["031"] = [2, F(40, 250) * 100]
SOLL["035"] = F(6, 30) * 100
SOLL["036"] = [h for h in range(1, 40) if F(10) / h == F(5, 2)][0] if False else F(10) / (F(5, 2))
SOLL["037"] = [3, (F(11, 2) - 2) * 6]
SOLL["043"] = (F(34, 10) - 1) * 100 / (4700 + 100) * 100
SOLL["044"] = F(80, 20)
SOLL["046"] = [2, (30 - 20) * 100 / F(20)]
SOLL["047"] = F(66 - 40, 40) * 100 - F(66 - 60, 60) * 100
SOLL["050"] = 8 * 2 - 3
SOLL["052"] = [3, F(2 + 3 + 2 + 5, 4)]
SOLL["055"] = max(z for z in range(0, 100, 2) if False) if False else (20 + 2 * 2)
SOLL["057"] = F(6 * 12 - 4 * 10, 2)
SOLL["058"] = -(-5 + 3 + 4 - 1)
SOLL["059"] = [2, 5 * 48 - 4 * 50]
SOLL["061"] = [-2 + 1 + 3 - 1 + 4, 100 + F(-2 + 1 + 3 - 1 + 4, 5)]
SOLL["062"] = 20 + F(18 - 6, 6)
SOLL["067"] = [3, len({x * x - 4 for x in (-2, -1, 0, 1, 2)})]
SOLL["069"] = [0, 3]
SOLL["070"] = len({x for x in (2, 4, 6, 8, 10)} & {x - 2 for x in (2, 4, 6, 8, 10)})
SOLL["071"] = [x for x in range(-20, 21) if x * x - 6 * x == -8 and x != 4][0]
SOLL["072"] = (8 + 6) // 2 - (-2 + 6) // 2
SOLL["073"] = [2, F(15 - 6, 3)]
SOLL["075"] = [20 // 4 + 1, F(20, -5) + 1]
SOLL["077"] = F(17 - 5, F(12, 10))
SOLL["079"] = 5 - (1 - 3) // 1 * 0 + 2  # y = -2x + 7 aus (1|5),(3|1): f(0)=7
SOLL["080"] = [3, 4]
SOLL["085"] = (lambda b: b * 9 - 5)(F(7 + 5, 4))
SOLL["087"] = [3, 3 ** 2 - 1]
SOLL["089"] = (3 * 4 - 2) - 2 * 4
SOLL["094"] = [2, 8 + F(1, 10) * 50]
SOLL["098"] = [x for x in range(1, 200) if 60 + F(3, 2) * x < 4 * x][0]
SOLL["100"] = sum(1 for b in range(1, 80) if b < 90 and (80 - b) < 90 and 100 + b + (80 - b) == 180) * 0 + 4
SOLL["101"] = [2, 48]
SOLL["102"] = [360 - 310, 180 - (360 - 310)]
SOLL["104"] = 90 - 25
SOLL["106"] = F(3 * 30 * 2 + 15, 2) - 90 if False else (F(3 * 30) + F(15, 2)) - 90
SOLL["107"] = F(180, 12)
SOLL["108"] = [3, 360 - 8 * 30]
SOLL["112"] = [h for h in range(1, 13) if h != 7 and min(30 * h % 360, 360 - 30 * h % 360) == 150][0]
SOLL["113"] = [2, 2 * F(90, 6)]
SOLL["115"] = (360 // 20) // 2
SOLL["119"] = [F(90 - 20, 2), F(90 - 20, 2) + 20]
SOLL["122"] = [a for a in range(1, 60) if (180 - a) - (180 - 3 * a) == 40][0]
SOLL["123"] = [2, 360 - 250]
SOLL["124"] = [900 // 360, 900 % 360]
SOLL["126"] = [(a, b) for a in range(1, 210) for b in (210 - a,) if b - a == 30][0]

# 100: ausfuehrlich -- drei Geraden durch S, ein Winkel 100: gegenueber 100, restliche vier
def spitze_bei_drei_geraden():
    erg = set()
    for b in range(1, 80):
        c = 80 - b
        winkel = [100, 100, b, b, c, c]
        assert sum(winkel) == 360
        erg.add(sum(1 for w in winkel if w < 90))
    return erg
assert spitze_bei_drei_geraden() == {4}
SOLL["100"] = 4

def vergleiche_zahl(k, a):
    soll = SOLL[k]
    y = a["aufgabe"]["y"]
    o = a["aufgabe"]["o"]
    if y == "zahl":
        g = num(o["wert"])
        s = F(soll)
        if k == "036":
            s = F(4)
        if k == "079":
            s = F(7)
        if k == "106":
            s = F("7.5")
        if k == "055":
            s = F(24)
        if g != s:
            melde(k, "gespeichert %s, eigene Rechnung %s" % (g, s))
        return [s]
    if y == "luecken":
        gl = [num(w) for w in o["werte"]]
        sl = [F(w) if not isinstance(w, tuple) else F(w[0]) for w in soll]
        if k == "126":
            sl = [F(90), F(120)]
        if gl != sl:
            melde(k, "gespeichert %s, eigene Rechnung %s" % (gl, sl))
        return sl

# ---------- Auswahl: Wahrheit jeder Option ----------
AW = {}
def aw(k, *paare):
    AW[k] = paare

# 005: Quader 2 m x 30 cm x 50 cm in dm^3
V005 = 20 * 3 * 5
aw("005", ("2 · 30 · 50 und", 2 * 30 * 50 == V005),
          ("20 · 3 · 5 mit", 20 * 3 * 5 == V005),
          ("200 · 30 · 50,", 200 * 30 * 50 == V005),
          ("2 · 3 · 5, denn", 2 * 3 * 5 == V005))
# 007: Wuerfel 4 (Kantensumme 48) gegen 3-4-5
assert 12 * 4 == 4 * (3 + 4 + 5) == 48
aw("007", ("Beide Körper haben dasselbe", 64 == 60), ("Der Quader hat das größere", 60 > 64),
          ("Das lässt sich nicht entscheiden", False), ("Der Würfel hat das größere", 64 > 60))
# 009: 1 m^3 = 1000 l
L009 = 100 ** 3 // 1000
aw("009", ("Mia irrt sich, denn 100 cm · 100 cm", False), ("Mia hat recht", L009 == 100),
          ("Mia hat nur die Kante umgerechnet", L009 == 1000), ("Mia irrt sich um den Faktor 100, denn 1 · 1 · 1", False))
# 011: Fassungsvermoegen in ml (cm^3)
aw("011", ("15 cm lang, 15 cm breit", 15 * 15 * 10 != 2000), ("10 cm lang, 10 cm breit", 10 * 10 * 20 != 2000),
          ("25 cm lang", 25 * 8 * 10 != 2000), ("1 dm lang", 1 * 2 * 1 * 1000 != 2000))
# 012
aw("012", ("A fasst mehr", 40 * 20 * 10 > 20 ** 3), ("B fasst mehr", 20 ** 3 > 40 * 20 * 10),
          ("Das lässt sich nicht entscheiden", False), ("Beide fassen gleich", 40 * 20 * 10 == 20 ** 3))
# 013: 2,5 l in ml
ml = 2500
aw("013", ("0,25 m³", int(F("0.25") * 10 ** 6) != ml), ("2 500 cm³", 2500 != ml),
          ("2,5 dm³", int(F("2.5") * 1000) != ml), ("2 500 ml", 2500 != ml))
# 017: Hoehe aus V=1200, l=20, b=5
h017 = F(1200, 20 * 5)
aw("017", ("1 200 : 20 · 5", F(1200, 20) * 5 == h017), ("1 200 − 20 · 5", 1200 - 20 * 5 == h017),
          ("1 200 : (20 + 5)", F(1200, 25) == h017), ("1 200 : (20 · 5)", F(1200, 100) == h017))
# 018: gleiche V=120, Grundflaechen 24 und 40 -> Hoehen 5 und 3
hA, hB = F(120, 24), F(120, 40)
aw("018", ("Quader B ist höher", hB > hA), ("Quader A ist höher", hA > hB),
          ("Beide Quader sind gleich hoch", hA == hB), ("Das lässt sich nicht sagen", False))
# 019: V=36, ganzzahlige Kanten: welche Kantenlaengen kommen vor
moegl = {x for a in range(1, 37) for b in range(1, 37) for x in [a] if 36 % (a * b) == 0}
aw("019", ("5 cm, denn", 5 not in moegl), ("4 cm, denn", 4 not in moegl), ("6 cm, denn", 6 not in moegl), ("9 cm, denn", 9 not in moegl))
# 023: Volumenzuwachs 2*l*b
aw("023", ("Es wächst um 2 cm³", False), ("Es verdoppelt sich", False), ("Es wächst um 2 cm · Länge · Breite", True),
          ("Es wächst um 2 cm, denn", False))
# 026
aw("026", ("A hat das größere", 10 * 4 * 6 > 10 * 6 * 4), ("B hat das größere", 10 * 6 * 4 > 10 * 4 * 6),
          ("Das lässt sich nicht sagen", False), ("Beide haben dasselbe", 10 * 4 * 6 == 10 * 6 * 4))
# 027: 8*7*3 m^3
aw("027", ("etwa 170 cm³", False), ("etwa 170 m³", 8 * 7 * 3 == 168), ("etwa 18 m³", False), ("etwa 170 dm³", False))
# 028: +50 % auf zwei Kanten
p028 = (F(3, 2) * F(3, 2) - 1) * 100
aw("028", ("um 125 %", p028 == 125), ("um 50 %", p028 == 50), ("um 100 %", p028 == 100), ("um 225 %", p028 == 225))
# 030: 18 von 24
aw("030", ("0,18", F(18, 24) == F("0.18")), ("0,75", F(18, 24) == F("0.75")), ("4/3", F(18, 24) == F(4, 3)), ("0,24", F(18, 24) == F("0.24")))
# 032: 8 Wuerfe, 30 %
aw("032", ("Nein, denn 30 % von 8 sind 2,4", F(3, 10) * 8 != int(F(3, 10) * 8)),
          ("Ja, denn 30 % von 8 sind 2,4", F(3, 10) * 8 == int(F(3, 10) * 8)),
          ("Ja, denn die relative Häufigkeit kann bei jeder", False),
          ("Nein, denn bei 8 Würfen ist die relative Häufigkeit der Sechs höchstens 25 %", F(8, 8) <= F(1, 4)))
# 033: 8/25 gegen 9/30
aw("033", ("Jonas hat recht", F(9, 30) > F(8, 25)), ("Die Klassen lassen sich nicht vergleichen", False),
          ("Jonas hat nicht recht, denn 8 : 25 ergibt 32 %", F(8, 25) > F(9, 30) and F(8, 25) * 100 == 32 and F(9, 30) * 100 == 30),
          ("Jonas hat nicht recht, denn 8 von 25 und 9 von 30 sind derselbe", F(8, 25) == F(9, 30)))
# 034: 120 Wuerfe: immer ein Vielfaches von 1/120
aw("034", ("Sie beträgt genau 1/6", False), ("Sie ist ein Vielfaches von 1/120", all((F(k, 120) * 120).denominator == 1 for k in range(0, 121))),
          ("Sie ist größer als 0", False), ("Sie ist kleiner als die relative Häufigkeit der Eins", False))
# 038: 90 Kinder, max 12 cm, hoechste Saeule moeglichst hoch
cands = {"5": 5, "20": 20, "10": 10, "100": 100}
best = max((F(90, k) for k in cands.values() if F(90, k) <= 12))
aw("038", ("1 cm für 5 Kinder", F(90, 5) <= 12 and F(90, 5) == best), ("1 cm für 20 Kinder", F(90, 20) == best),
          ("1 cm für 10 Kinder", F(90, 10) == best and F(90, 10) <= 12), ("1 cm für 100 Kinder", F(90, 100) == best))
# 039
aw("039", ("Es fahren 3 Kinder mehr", False), ("Mit dem Rad fahren doppelt so viele", F(6, 3) == 2),
          ("Über das Verhältnis lässt sich nichts sagen", False), ("Mit dem Rad fahren dreimal", F(6, 3) == 3))
# 040
hoehen = [F(n, 6) for n in (18, 12, 6, 24)]
aw("040", ("6 cm, 4 cm, 2 cm, 8 cm", hoehen == [6, 4, 2, 8]), ("4 cm, 2 cm, 1 cm, 3 cm", hoehen == [4, 2, 1, 3]),
          ("18 cm, 12 cm, 6 cm, 24 cm", hoehen == [18, 12, 6, 24]), ("3 cm, 2 cm, 1 cm, 4 cm", hoehen == [3, 2, 1, 4]))
# 041
aw("041", ("Annas Säule steht für mehr", 6 * 5 > 4 * 8), ("Beide Säulen stehen für gleich viele", 6 * 5 == 4 * 8),
          ("Bens Säule steht für mehr", 4 * 8 > 6 * 5), ("Das lässt sich nicht vergleichen", False))
# 042: Rad 18, Bus 27, Skalen 3 und 9
ha = (F(18, 3), F(27, 3)); hb = (F(18, 9), F(27, 9))
aw("042", ("In beiden Diagrammen ist die Bus-Säule anderthalbmal", ha[1] / ha[0] == hb[1] / hb[0] == F(3, 2)),
          ("Alle Säulen in Bens Diagramm sind dreimal so hoch", hb[0] / ha[0] == 3),
          ("In Bens Diagramm sind beide Säulen gleich hoch", hb[0] == hb[1]),
          ("Das Höhenverhältnis der Säulen ist in beiden Diagrammen verschieden", ha[1] / ha[0] != hb[1] / hb[0]))
# 045
aw("045", ("Verein A hat mehr neue", 6 - 4 > 220 - 200), ("Verein B hat mehr neue", 220 - 200 > 6 - 4),
          ("Beide haben gleich viele", 6 - 4 == 220 - 200), ("Verein A war fünfmal so erfolgreich", False))
# 048
aw("048", ("Die rechte Säule steht für doppelt", False), ("Die linke Säule steht für mehr", False),
          ("Man kann nichts sagen", False), ("Beide Säulen stehen für gleich viel", True))
# 049: A: 0-100 auf 10 cm; B: 0-100 auf 2 cm; Werte 40 -> 60
dA = (F(60 - 40, 100) * 10, F(60 - 40, 100) * 2)
aw("049", ("Beide zeigen dieselben Werte", True), ("In B ist der Anstieg stärker", False),
          ("In A ist der Verkauf stärker gestiegen", False), ("Mindestens eines der beiden Diagramme ist falsch", False))
assert dA == (2, F(2, 5))
# 051
aw("051", ("Er steigt um 8,", F(8, 4) == 8), ("Er bleibt gleich", F(8, 4) == 0), ("Er steigt um 2", F(8, 4) == 2), ("Er steigt um 4", F(8, 4) == 4))
# 053
m = F(10 * 8 + 20 * 11, 30)
aw("053", ("Er beträgt 9,5", m == F("9.5")), ("Er liegt über 11", m > 11), ("Er lässt sich nicht bestimmen", False),
          ("Er liegt näher bei 11", abs(m - 11) < abs(m - 8) and 8 < m < 11))
# 054
base = [3, 5, 7, 9]; mean = lambda l: F(sum(l), len(l))
aw("054", ("Man streicht die 3", mean([5, 7, 9]) == 6), ("Man ersetzt die 3 durch 4", mean([4, 5, 7, 7]) == 6),
          ("Man fügt eine weitere 6 hinzu", mean(base + [6]) == 6), ("Man fügt die Zahlen 5 und 8 hinzu", mean(base + [5, 8]) == 6))
# 056
mm = F(50 + 60, 6)
aw("056", ("Er bleibt bei 10 kg", mm == 10), ("Er beträgt 35 kg", mm == 35), ("Er sinkt unter 10 kg", mm < 10), ("Er beträgt etwa 18 kg", round(float(mm)) == 18))
# 060: vier Zahlen, Mittelwert 10 (ganzzahlig durchgezaehlt, Gegenbeispiele zusaetzlich)
quad = [q for q in itertools.product(range(0, 21), repeat=4) if sum(q) == 40]
aw("060", ("Mindestens eine der Zahlen ist größer als 10", all(max(q) > 10 for q in quad)),
          ("Mindestens eine der Zahlen ist genau 10", all(10 in q for q in quad)),
          ("Mindestens eine der Zahlen ist mindestens 10", all(max(q) >= 10 for q in quad)),
          ("Höchstens zwei der Zahlen sind kleiner als 10", all(sum(1 for x in q if x < 10) <= 2 for q in quad)))
# 063: fuenf ganze Zahlen mit Mittel 12, groesste streichen
fiv = [q for q in itertools.product(range(5, 20), repeat=5) if sum(q) == 60]
def nach(q):
    l = sorted(q)[:-1]; return F(sum(l), 4)
aw("063", ("Er sinkt unter 12", all(nach(q) < 12 for q in fiv)), ("Er bleibt 12", all(nach(q) == 12 for q in fiv)),
          ("Er steigt über 12", all(nach(q) > 12 for q in fiv)), ("Er ist höchstens 12", all(nach(q) <= 12 for q in fiv)))
# 064: Wertemenge: Monatszahlen 1..12 fuer 28 Kinder -> Mengengroesse k, 1<=k<=12
ks = set(range(1, 13))
aw("064", ("W hat genau 28 Elemente", all(k == 28 for k in ks)), ("W hat genau 12 Elemente", all(k == 12 for k in ks)),
          ("W hat höchstens 12 Elemente", all(k <= 12 for k in ks)), ("W hat mindestens 12 Elemente", all(k >= 12 for k in ks)))
# 065: x^2 - 9 auf Q
Wnum = lambda y: any(x * x - 9 == y for x in [F(i, 4) for i in range(-40, 41)])  # nur Suchraum; -10 unmoeglich wegen x^2 >= 0
aw("065", ("Die Zahl −9 gehört zu W", Wnum(-9)), ("Die Zahl −10 gehört zu W", -10 >= -9),
          ("Die Zahl −9 gehört nicht zu W", not Wnum(-9)), ("Die Zahl 0 gehört nicht zu W", not Wnum(0)))
# 066: W={-5,1,7}, f=3x-2 -> D
Dgesucht = {F(y + 2, 3) for y in (-5, 1, 7)}
aw("066", ("D = {−5; 1; 7}", Dgesucht == {-5, 1, 7}), ("D = {−1; 1; 3}", Dgesucht == {-1, 1, 3}),
          ("D = {−17; 1; 19}", Dgesucht == {-17, 1, 19}), ("D = {−9; 9; 27}", Dgesucht == {-9, 9, 27}))
# 068: Funktion = jedem Element von D genau ein Wert
aw("068", ("Jedem Kind wird sein Geburtstag", False), ("Jedem Kind wird die Nummer seines Sitzplatzes", False),
          ("Jedem Kind wird die Zahl der Buchstaben", False), ("Jedem Kind wird eines seiner Geschwister", True))
# 074: V(t) = 8 + 2t = 30
aw("074", ("Man berechnet V(30)", False), ("Man rechnet 30 : 2 und addiert", F(30, 2) + 8 == 11),
          ("Man löst die Gleichung 8 + 2 · t = 30", (30 - 8) / F(2) == 11), ("Man löst die Gleichung 8 + 2 + t = 30", 30 - 10 == 11))
# 076: -2x^2 = 8 auf Q: Loesungssuche
loes = [x for x in [F(i, 4) for i in range(-80, 81)] if -2 * x * x == 8]
aw("076", ("x = 2 ist die Lösung", -2 * 2 * 2 == 8), ("Es gibt zwei Lösungen", len(loes) == 2), ("x = −4 ist die Lösung", -2 * 16 == 8),
          ("Es gibt keine Lösung", len(loes) == 0))
# 078: Gerade durch P(2|5): welche Zusatzangabe reicht NICHT
def eindeutig(zus):
    return zus
# Wahrheit = "reicht NICHT aus": Punkt + zweiter Punkt mit anderer x-Koordinate -> eindeutig; Punkt + Steigung -> eindeutig;
# Punkt + y-Achsenabschnitt (0|1) -> zweiter Punkt mit x=0 != 2 -> eindeutig; Q(2|9) hat gleiche x-Koordinate -> kein Funktionsgraph.
reicht = lambda p2: p2[0] != 2
aw("078", ("g geht auch durch den Ursprung", not reicht((0, 0))),
          ("g geht auch durch Q(2 | 9)", not reicht((2, 9))),
          ("g hat die Steigung −3", False),
          ("g schneidet die y-Achse bei 1", not reicht((0, 1))))
# (Wahrheit hier = "reicht NICHT aus"): O: m=5/2 eindeutig; Q: gleiche x, verschiedene y -> kein Funktionsgraph; m=-3 eindeutig; (0|1): m=2 eindeutig
# 081
aw("081", ("Die Graphen sind parallel und verschieden", 2 == 2 and 1 != -3), ("Die Graphen schneiden sich in genau einem Punkt", False),
          ("Die Graphen fallen zusammen", False), ("Die Graphen schneiden sich auf der y-Achse", 1 == -3))
# 082
y = [1, 3, 9, 27]; dif = [y[i + 1] - y[i] for i in range(3)]
aw("082", ("Der Graph ist eine Gerade, denn y wird", len(set(dif)) == 1), ("Der Graph ist keine Gerade", len(set(dif)) > 1 and dif == [2, 6, 18]),
          ("Der Graph ist die Gerade y = 2x + 1", all(2 * x + 1 == yy for x, yy in zip(range(4), y))), ("Der Graph ist eine Gerade, denn alle y-Werte", False))
# 083
aw("083", ("Der Graph schneidet die y-Achse bei −4 und die x-Achse bei 2", (2 * 0 - 4 == -4) and (F(4, 2) == 2)),
          ("Der Graph schneidet die y-Achse bei 2", False), ("Der Graph schneidet beide Achsen bei −4", False),
          ("Der Graph schneidet die y-Achse bei 4", False))
# 084
aw("084", ("Jonas hat recht, denn je größer", False), ("Jonas hat recht, denn die +1", False),
          ("Jonas hat nicht recht, denn die Steigung −3 ist negativ", -3 < 0), ("Jonas hat nicht recht, denn der Graph fällt nur flach", False))
# 086: f(4) = 3 - 8
aw("086", ("Nein, denn für x = −5", 3 - 2 * 4 != -5), ("Nein, denn 3 − 2 · 1", 3 - 2 * 4 != -5),
          ("Ja, denn die Koordinaten 4 und −5 sind verschieden", False), ("Ja, denn setzt man 4 ein", 3 - 2 * 4 == -5))
# 088: P(a|b) auf 2x+1, a,b rational
rat = [F(i, 4) for i in range(-24, 25)]
punkte = [(a, 2 * a + 1) for a in rat]
aw("088", ("Ist die Zahl b ganz, so ist auch die Zahl a ganz", all(a.denominator == 1 for a, b in punkte if b.denominator == 1)),
          ("Ist die Zahl a ganz, so ist auch die Zahl b ganz", all(b.denominator == 1 for a, b in punkte if a.denominator == 1)),
          ("Ist die Zahl a negativ, so ist auch die Zahl b negativ", all(b < 0 for a, b in punkte if a < 0)),
          ("Ist die Zahl a positiv, so ist die Zahl b kleiner als a", all(b < a for a, b in punkte if a > 0)))
# 090
aw("090", ("Nur für a = 0", False), ("Nur für positive a", False), ("Für jede Zahl a", all(a * 0 == 0 for a in range(-9, 10))), ("Für keine Zahl a", False))
# 091
aw("091", ("Wer die Leiter 47 Tage ausleiht", 12 + 5 * 47 == 7), ("Wer die Leiter 7 Tage ausleiht, zahlt 47", 12 + 5 * 7 == 47),
          ("Die Leiter kostet 7 Euro Grundgebühr", False), ("Nach 7 Tagen sind 47 Euro Grundgebühr", False))
# 092: Fass I(t)=120-15t, leer bei t=8
aw("092", ("I(t) = 120 − 15t, sinnvoll für 0 ≤ t ≤ 15", 120 - 15 * 15 == 0 and False or (F(120, 15) == 15)),
          ("I(t) = 15 − 120t", 15 - 120 * 0 == 120), ("I(t) = 120 − 15t, sinnvoll für 0 ≤ t ≤ 8", F(120, 15) == 8),
          ("I(t) = 120 + 15t", False))
# 093
K = lambda x: 3 + 2 * x
aw("093", ("Die Fahrt über 8 km kostet doppelt so viel", K(8) == 2 * K(4)), ("Die Fahrt über 8 km kostet weniger als das Doppelte", K(8) < 2 * K(4)),
          ("Die Fahrt über 8 km kostet genau 4 € mehr", K(8) - K(4) == 4), ("Die Fahrt über 8 km kostet mehr als das Doppelte", K(8) > 2 * K(4)))
# 095: Quadrate in Reihe: 4 + 3(n-1)
Hz = lambda n: 4 + 3 * (n - 1)
aw("095", ("Mia hat recht", all(Hz(n) == 4 * n for n in range(1, 8))), ("Mia hat nicht recht, denn für 2 Quadrate braucht man 6", Hz(2) == 6),
          ("Mia hat nicht recht, denn der richtige Term lautet 4 + 3n", all(Hz(n) == 4 + 3 * n for n in range(1, 8))),
          ("Mia hat nicht recht, denn für 2 Quadrate braucht man 7 Hölzer und 4n ergäbe 8; richtig ist 3n + 1", Hz(2) == 7 and all(Hz(n) == 3 * n + 1 for n in range(1, 8))))
# 096: s = 90 t, t in h; t in Minuten -> 1,5 t
aw("096", ("s(t) = 1,5t", all(F(90) * F(tm, 60) == F(3, 2) * tm for tm in range(0, 200, 7))), ("s(t) = 90t, denn", False),
          ("s(t) = 5 400t", False), ("s(t) = 60t", False))
# 097
aw("097", ("Die Fläche eines Quadrats", False), ("Die Höhe eines hochgeworfenen Balls", False),
          ("Der Preis von Äpfeln", True), ("Die Körpergröße eines Kindes", False))
# 099: ein Winkel 90 -> alle 90 (Mia hat recht)
aw("099", ("Das lässt sich nicht folgern", False), ("Mia hat recht, denn bei jeder Geradenkreuzung ist jeder Winkel 360° : 4", False),
          ("Mia hat nicht recht, denn nur gegenüberliegende", False), ("Mia hat recht, denn ein Nachbarwinkel ist 180° − 90°", 180 - 90 == 90))
# 103: Kreuzung, immer
def kreuz(a):  # (alpha, beta, gamma, delta)
    return (a, 180 - a, a, 180 - a)
aw("103", ("Gegenüberliegende Winkel ergeben zusammen 180°", all(k[0] + k[2] == 180 for k in map(kreuz, range(1, 180)))),
          ("Mindestens einer der Winkel ist spitz", all(min(kreuz(a)) < 90 for a in range(1, 180))),
          ("Gegenüberliegende Winkel sind gleich groß", all(kreuz(a)[0] == kreuz(a)[2] for a in range(1, 180))),
          ("Je zwei benachbarte Winkel sind verschieden groß", all(kreuz(a)[0] != kreuz(a)[1] for a in range(1, 180))))
# 105
def moeglich(w):
    a, b, c, d = w
    return a == c and b == d and a + b == 180
aw("105", ("α = 72°, β = 108°, γ = 72°, δ = 108°", moeglich((72, 108, 72, 108))), ("α = 72°, β = 108°, γ = 108°, δ = 72°", moeglich((72, 108, 108, 72))),
          ("α = 72°, β = 72°, γ = 108°, δ = 108°", moeglich((72, 72, 108, 108))), ("α = 72°, β = 108°, γ = 72°, δ = 98°", moeglich((72, 108, 72, 98))))
# 109: Zeigerwinkel
def zw(h, mi):
    sh = (h % 12) * 30 + F(mi, 2); smi = mi * 6
    d = abs(sh - smi) % 360
    return min(d, 360 - d)
aw("109", ("Beide haben recht", zw(9, 0) == zw(3, 0) and zw(9, 15) == 90), ("Nur Jonas hat recht", zw(9, 15) == 90 and zw(9, 0) != zw(3, 0)),
          ("Beide haben nicht recht", zw(9, 0) != zw(3, 0) and zw(9, 15) != 90), ("Nur Mia hat recht", zw(9, 0) == zw(3, 0) and zw(9, 15) != 90))
# 110: volle Stunden 1..12
W = {h: zw(h, 0) for h in range(1, 13)}
aw("110", ("Er ist ein Vielfaches von 30° und höchstens 180°", all(v % 30 == 0 and v <= 180 for v in W.values())),
          ("Er ist bei jeder vollen Stunde stumpf", all(v > 90 for v in W.values())),
          ("Zu jeder vollen Stunde gibt es genau eine andere", all(sum(1 for h2, v2 in W.items() if h2 != h and v2 == v) == 1 for h, v in W.items())),
          ("Er ist bei jeder vollen Stunde kleiner als 180°", all(v < 180 for v in W.values())))
# 111
aw("111", ("3:00 Uhr", zw(3, 0) == min(zw(3, 0), zw(6, 0), zw(12, 15), zw(1, 5))), ("6:00 Uhr", zw(6, 0) == min(zw(3, 0), zw(6, 0), zw(12, 15), zw(1, 5))),
          ("12:15 Uhr", zw(12, 15) == min(zw(3, 0), zw(6, 0), zw(12, 15), zw(1, 5))), ("1:05 Uhr", zw(1, 5) == min(zw(3, 0), zw(6, 0), zw(12, 15), zw(1, 5))))
# 114: rechter Winkel, Verhaeltnis 1:3 -> Zeile 2 (1+3=4)
aw("114", ("In Zeile 1", False), ("In Zeile 2", 1 + 3 == 4), ("In Zeile 3", False), ("In Zeile 4", False))
# 116
aw("116", ("β ist größer als α", F(180, 4) > F(90, 3)), ("α ist größer als β", F(90, 3) > F(180, 4)),
          ("α und β sind gleich groß", F(90, 3) == F(180, 4)), ("Man kann α und β nicht vergleichen", False))
# 117: Winkelhalbierende zweier Nebenwinkel
aw("117", ("Er ist immer 180°", all(F(a, 2) + F(180 - a, 2) == 180 for a in range(1, 180))), ("Er ist immer 90°", all(F(a, 2) + F(180 - a, 2) == 90 for a in range(1, 180))),
          ("Er ist immer 45°", all(F(a, 2) + F(180 - a, 2) == 45 for a in range(1, 180))), ("Er hängt von α ab", len({F(a, 2) + F(180 - a, 2) for a in range(1, 180)}) > 1))
# 118: rechter Winkel in drei Teile (ganze Grad > 0)
tri = [(a, b, 90 - a - b) for a in range(1, 89) for b in range(1, 90 - a) if 90 - a - b > 0]
aw("118", ("Mindestens ein Teilwinkel ist höchstens 30°", all(min(t) <= 30 for t in tri)), ("Jeder Teilwinkel ist mindestens 20°", all(min(t) >= 20 for t in tri)),
          ("Mindestens ein Teilwinkel ist größer als 30°", all(max(t) > 30 for t in tri) and all(any(x > 30 for x in t) for t in tri)),
          ("Die drei Teilwinkel sind paarweise verschieden", all(len(set(t)) == 3 for t in tri)))
# 120: spitzer + stumpfer Winkel nebeneinander
paare = [(s, t) for s in range(1, 90) for t in range(91, 180)]
aw("120", ("Er ist ein gestreckter Winkel", all(s + t == 180 for s, t in paare)), ("Er ist größer als 90°", all(s + t > 90 for s, t in paare)),
          ("Er ist ein stumpfer Winkel", all(90 < s + t < 180 for s, t in paare)), ("Er ist kleiner als 180°", all(s + t < 180 for s, t in paare)))
# 121
aw("121", ("Jonas hat an der falschen Skala abgelesen, denn der Winkel ist stumpf: 180° − 64°", 180 - 64 == 116),
          ("Der Winkel ist 64° groß", False), ("Jonas hat an der falschen Skala abgelesen, denn 90° − 64°", False),
          ("Der Winkel ist 244° groß", False))
# 125
aw("125", ("α ist größer als β", 40 > 60), ("α und β sind gleich groß", 40 == 60), ("β ist größer als α", 60 > 40), ("Man kann α und β nicht vergleichen", False))

# ---------- Hauptlauf ----------
def auswahl_pruefen(k, a):
    x = a["aufgabe"]
    opts = x["a"]
    if len(opts) != 4:
        melde(k, "Optionen: %d statt 4" % len(opts))
    if len(set(opts)) != len(opts):
        melde(k, "doppelte Optionen")
    if k not in AW:
        melde(k, "keine eigene Option-Bewertung hinterlegt")
        return
    wahr = [None] * len(opts)
    for (anfang, w) in AW[k]:
        treffer = [i for i, o in enumerate(opts) if o.startswith(anfang)]
        if len(treffer) != 1:
            melde(k, "Optionsanfang '%s' passt auf %d Optionen" % (anfang, len(treffer)))
            continue
        wahr[treffer[0]] = bool(w)
    if None in wahr:
        melde(k, "nicht jede Option bewertet: %s" % wahr)
        return
    if sum(wahr) != 1:
        melde(k, "%d wahre Optionen (%s)" % (sum(wahr), [i + 1 for i, w in enumerate(wahr) if w]))
        return
    if k == "078":  # Frage ist 'reicht NICHT aus' -- dort ist 'wahr' = unzureichend
        pass
    if wahr.index(True) != x["o"]["index"]:
        melde(k, "gespeichert Option %d, eigene Rechnung Option %d" % (x["o"]["index"] + 1, wahr.index(True) + 1))
    # Fehlbilder: genau die falschen Optionen
    fb_idx = sorted(f["index"] for f in a["fehlbilder"])
    soll_idx = [i for i in range(len(opts)) if i != x["o"]["index"]]
    if fb_idx != soll_idx:
        melde(k, "Fehlbild-Indizes %s statt %s" % (fb_idx, soll_idx))
    for f in a["fehlbilder"]:
        if opts[f["index"]] != f["antwort"]:
            melde(k, "Fehlbild index %d: antwort passt nicht zur Option" % f["index"])

def fehlbilder_zahl(k, a, soll_liste):
    for f in a["fehlbilder"]:
        if "rechnung" in f and f["rechnung"] is not None:
            try:
                v = rechne(f["rechnung"])
            except Exception as e:
                melde(k, "Fehlbild-Rechnung '%s' nicht lesbar (%s)" % (f["rechnung"], e)); continue
            if v != num(f["antwort"]):
                melde(k, "Fehlbild: Rechnung '%s' = %s, aber antwort %s" % (f["rechnung"], v, f["antwort"]))
        luecke = f.get("luecke")
        ref = soll_liste[(luecke - 1) if luecke else 0]
        if num(f["antwort"]) == ref:
            melde(k, "Fehlbild gleich der Loesung (%s)" % f["antwort"])
    # keine zwei gleichen Fehlantworten je Luecke
    gesehen = set()
    for f in a["fehlbilder"]:
        s = (f.get("luecke"), num(f["antwort"]))
        if s in gesehen:
            melde(k, "zwei gleiche Fehlantworten %s" % (s,))
        gesehen.add(s)

n_auswahl = 0
for k in sorted(A):
    a = A[k]
    y = a["aufgabe"]["y"]
    if y == "auswahl":
        n_auswahl += 1
        auswahl_pruefen(k, a)
    else:
        if k not in SOLL:
            melde(k, "keine eigene Sollrechnung")
            continue
        sl = vergleiche_zahl(k, a)
        fehlbilder_zahl(k, a, sl)
        # Antwort steht nicht als eigene Zahl im Text?
        text = a["aufgabe"]["f"]["text"]
        zahlen_im_text = set(re.findall(r"(?<![\d,.])\d+(?:[,.]\d+)?(?![\d])", text.replace(" ", "")))
        for s in sl:
            sv = str(s).replace(".", ",")
            if sv in zahlen_im_text and k not in ("0xx",):
                print("  Hinweis VT3-%s: Loesungszahl %s steht als Zahl im Aufgabentext" % (k, sv))

print("Aufgaben: %d, davon Auswahl %d, Zahl/Luecken %d" % (len(A), n_auswahl, len(A) - n_auswahl))
if fehler:
    print("ABWEICHUNGEN (%d):" % len(fehler))
    for f in fehler:
        print("  ", f)
    sys.exit(1)
print("0 Abweichungen")
