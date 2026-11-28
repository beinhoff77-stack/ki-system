#!/usr/bin/env python3
# HISTORISCHER PRÜFSTAND: Stand der Vorprüfung (vor den Korrekturen nach Vorprüfung, Gegenprüfung 1197 und 1207).
# Die Erwartungswerte gehören zu den damaligen Aufgaben; Abweichungen sind erwartet (Aufgaben wurden ersetzt, Kennungen
# der Einheit stochastik.verknuepft haben sich verschoben). Aktuelle Prüfung: gegenrechnung.py.
"""Unabhängige Vorprüfung Runde 15 (eigene Rechnung, übernimmt keine Rechnung des Autors).

Aufruf: python3 -I inhalte/mathe-profi/rollend-15/vorpruefung_rechnen.py
Liest nur die JSON-Dateien der Runde. Ändert nichts.

Teil A: eigene Lösung je Aufgabe (exakte Brüche bzw. Gleitkomma nur dort, wo gerundet wird) gegen die Soll-Antwort.
Teil B: allgemeine Prüfungen (Fehlbilder verschieden und ungleich der Lösung, Fehlbilder außerhalb der Toleranz mit
        exakter Dezimalrechnung wie in der Datenbank (<=), Auswahl-Antworten verschieden, Zähl-Schleifen).
"""
import glob, json, math, os, sys, itertools
from fractions import Fraction as F
from decimal import Decimal as D

HIER = os.path.dirname(os.path.abspath(__file__))
A = {}
for f in sorted(glob.glob(os.path.join(HIER, "*.json"))):
    for a in json.load(open(f, encoding="utf-8"))["aufgaben"]:
        A[a["kennung"].split("-")[1]] = a
assert len(A) == 207, len(A)

deg = math.pi / 180
sin = lambda g: math.sin(g * deg)
cos = lambda g: math.cos(g * deg)
tan = lambda g: math.tan(g * deg)
atan = lambda x: math.atan(x) / deg
asin = lambda x: math.asin(x) / deg
R = lambda x, n=0: round(x + 0.0, n)


def quad(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return []
    w = math.isqrt(int(d)) if d == int(d) else math.sqrt(d)
    return sorted({(-b - w) / (2 * a), (-b + w) / (2 * a)})


def teiler(n):
    return {i for i in range(1, n + 1) if n % i == 0}


# ---------- eigene Lösungen: Kennung -> erwarteter Wert (Zahl, Liste für Lücken, Index für Auswahl) ----------
E = {}
# bruch.prozent_grundwert
E["V001"] = 1.18
E["V003"] = 320 * (1 + .15 + .08)
E["V004"] = 480 * 1.25 / 40
E["V005"] = 3 * 28 + 3 * 28 * .7
E["V006"] = 85 - 85 * .35
E["V007"] = 162 / 1.08
E["V009"] = (4300 - 4085) / 4300 * 100
E["V011"] = 320 * 1.15 * 1.08
E["V012"] = R((1 - 1 / 1.2) * 100, 1)
E["V013"] = 5000 * 1.04 ** 3
E["V014"] = next(n for n in range(1, 50) if 2000 * 1.05 ** n > 2500)
# potenzgesetze
E["V017"] = [7, 3 ** 7]
E["V018"] = 2 ** 9
E["V020"] = 4 ** 3 * 25 ** 3
E["V022"] = next(b for b in range(1, 100) if 2 ** 4 * b ** 4 == 14 ** 4)
E["V023"] = (2 ** 3) ** 4
E["V025"] = next(n for n in range(1, 50) if (5 ** n) ** 4 == 5 ** 24)
E["V026"] = [2, 16]
E["V027"] = 5 ** 6 // 5 ** 4
E["V029"] = 2 ** 10 // 2 ** 6
E["V031"] = (2 ** 4 * 2 ** 5) ** 2 // 2 ** 10
# terme.umformen
E["V032"] = [7, 8, 7 * 2 + 8 * 1]
E["V033"] = 8 * 12 + 6 * 7
E["V035"] = 2 * 5 * 3 * 5 * 5
E["V037"] = next(a for a in range(1, 100) if 3 * a * 4 * a == 300)
E["V038"] = [7, 9, 7 * 2 + 9]
E["V039"] = 400 - (3 * 20 + 15)
E["V041"] = 6 * (45 + 12 * 3)
E["V042"] = 8 * 197
E["V043"] = next(k for k in range(0, 100) if all(5 * (2 * x + k) == 10 * x + 35 for x in range(-5, 6)))
E["V046"] = next(k for k in range(-200, 200) if all(13 * (x + 4) == 13 * x + k for x in range(-5, 6)))
# kongruenz
E["V047"] = [6 - 2, 6 + 4, 8]
E["V048"] = 2 * 1 - 5
E["V050"] = (-6 + 12) / 2
E["V051"] = (30 - 12) / 2
E["V052"] = (180 - 68 - 52) / 2
E["V054"] = [6, 8, 14]
E["V055"] = 3 + 8 + 4
E["V058"] = 5
E["V059"] = 180 - 52 - 71
# winkelsaetze
E["V061"] = [180, 45, 135]
E["V062"] = 180 - 83
E["V063"] = 180 - 73
E["V066"] = next(x for x in range(0, 200) if 5 * x - 20 == 3 * x + 14)
E["V067"] = 180 / 18 * 7
E["V069"] = [121 - 38, 180 - 121, 180]
E["V070"] = 47 + 65
E["V071"] = (12 - 2) * 180 / 12
E["V072"] = 2340 // 180
E["V073"] = 360 - 2 * 150
E["V075"] = 180 - (360 - 80 - 95 - 70)
E["V076"] = (180 - 70) + (180 - 80)
# konstruktion
E["V079"] = [140, 70, 110]
E["V080"] = 180 - 2 * 38
E["V085"] = [13, 3, len([c for c in range(1, 100) if 5 + c > 8 and 5 + 8 > c and 8 + c > 5])]
E["V086"] = max(c for c in range(1, 100) if 4 + 9 > c and 4 + c > 9 and 9 + c > 4)
E["V088"] = 7 + 5 + 6
E["V090"] = 180 - 50 - 70
E["V093"] = 2
# gleichungen.linear
E["V094"] = [4, 60, 15]
E["V095"] = (49 - 14) / 3.5
E["V097"] = 18 / (0.40 - 0.25)
E["V099"] = F(40 + 8, 7 - 3)
E["V100"] = [20, 39, 13]
E["V101"] = F(24 + 11, 5)
E["V103"] = 4 * 11 - 9
E["V106"] = 10
E["V108"] = F(18 * 2, 27 - 18)
E["V109"] = F(616) / F("11.2") + 3
E["V110"] = F(36 // 2 - 4, 2)
# wurzeln_basis
E["V111"] = [36, 144, 48]
E["V112"] = 4 * math.isqrt(5929)
E["V114"] = 0.13 * 100
E["V115"] = R(3.8 ** .5, 2)
E["V116"] = [7, 49, 294]
E["V117"] = 6 * round(2744 ** (1 / 3)) ** 2
E["V120"] = R(85 ** .5, 1)
E["V122"] = len([x for x in range(-3, 13) if x - 5 >= 0])
E["V124"] = 4 * 1.5 / 5 * 60
E["V125"] = 12 * 1.5
# reell
E["V127"] = 4
E["V128"] = [3, 4, 32]
E["V129"] = len([k for k in range(261, 270) if k * k < 7 * 10 ** 4])
E["V130"] = R((4.5 + 20 / 4.5) / 2, 2)
E["V131"] = F(36) / F("6.25")
E["V132"] = math.isqrt(18 * 50)
E["V134"] = [49, 7, 14]
E["V135"] = 7
E["V137"] = F(44, 11)
# quadratisch
E["V140"] = [49, 7, -7]
E["V141"] = min(x for x in range(-50, 51) if 4 * x * x - 196 == 0)
E["V144"] = max(quad(1, -4, -21))
E["V145"] = 4 * -9
E["V146"] = 25 - 9
E["V147"] = [576 - 252, 18, 7]
E["V148"] = min(quad(2, 3, -20))
E["V149"] = max(x for x in range(1, 100) if 40 == x * (x - 6))
E["V150"] = next(k for k in range(1, 100) if k * k - 4 * 3 * 27 == 0)
E["V152"] = max(quad(1, -4, -5))
E["V153"] = max(quad(1, 9, -360))
# funktionen.quadratisch
E["V154"] = [9, 6, 2 * (10 - 9) ** 2 + 6]
E["V156"] = F(13 + 5, 36)
E["V157"] = -6
E["V159"] = 50 - 36
E["V161"] = [-5, 11, 3]
E["V162"] = max(quad(1, 4, -21)) - min(quad(1, 4, -21))
E["V163"] = -0.02 * (30 - 20) ** 2 + 9
E["V164"] = next(p for p in range(-50, 50) if any(4 + 2 * p + q == 10 and 16 + 4 * p + q == 32 for q in range(-100, 100)))
E["V165"] = max(quad(1, -6, 5))
E["V166"] = [4, -5 * 16 + 40 * 4 + 3, -5 * 16 + 40 * 4]
E["V167"] = max(x * (36 - 2 * x) for x in range(1, 18))
# pythagoras
E["V168"] = [81 + 1600, 41, 9 + 40 + 41]
E["V169"] = (1.2 ** 2 + 0.5 ** 2) ** .5
E["V170"] = math.isqrt(61 ** 2 - 11 ** 2)
E["V173"] = math.isqrt(89 ** 2 - 39 ** 2)
E["V174"] = math.hypot(6, 8)
E["V175"] = math.isqrt(10 ** 2 - 6 ** 2)
E["V176"] = [20, 25, 5]
E["V177"] = math.isqrt(8 ** 2 + 9 ** 2 + 12 ** 2)
E["V178"] = 2 * math.hypot(2, 1.5) * 6
# trigo
E["V182"] = [21, 28, 35 + 21 + 28]
E["V183"] = 0.75 * 32
E["V184"] = R(1.5 * tan(28), 2)
E["V185"] = R(0.9 / sin(12), 2)
E["V186"] = R(atan(15 / 28), 1)
E["V187"] = R((1 - 0.28 ** 2) ** .5, 4)
E["V189"] = R(38 / tan(4))
E["V191"] = R(atan(0.12), 1)
E["V192"] = R(atan(3) - 45, 1)
# stochastik
E["V193"] = len([n for n in range(10, 100) if sum(map(int, str(n))) == 9])
E["V194"] = len(teiler(36) & teiler(48))
E["V195"] = len({m for m in range(1, 61) if m % 6 == 0} | {m for m in range(1, 61) if m % 4 == 0})
E["V196"] = [24 + 18 - 10, 40 - 32, 20]
E["V197"] = F(35 + 28 - 9, 100)
E["V198"] = (14 - 6) + (11 - 6)
E["V200"] = [64 - 27, 41 - 27, 100 - 64 - 14]
E["V201"] = 72 - (47 - 19)
E["V202"] = F(100 - (60 + 45 - 27), 100)
E["V203"] = F(24, 60)
E["V204"] = R(6 / 10 * 5 / 9, 3)
E["V205"] = R(8 / 26, 2)

# Auswahl: Index der richtigen Antwort, aus eigener Entscheidung (Begründung im Bericht)
IDX = {
    "V002": 1, "V008": 2, "V010": 1, "V015": 0, "V016": 0, "V019": 1, "V021": 3, "V024": 2, "V028": 2,
    "V030": 1, "V034": 2, "V036": 1, "V040": 1, "V044": 2, "V045": 3, "V049": 0, "V053": 0, "V056": 1,
    "V057": 2, "V060": 3, "V064": 1, "V065": 2, "V068": 0, "V074": 0, "V077": 3, "V078": 3, "V081": 2,
    "V082": 1, "V083": 1, "V084": 1, "V087": 3, "V089": 0, "V091": 2, "V092": 2, "V096": 0, "V098": 0,
    "V102": 0, "V104": 1, "V105": 1, "V107": 3, "V113": 0, "V118": 0, "V119": 3, "V121": 2, "V123": 0,
    "V126": 1, "V133": 2, "V136": 3, "V138": 0, "V139": 2, "V142": 1, "V143": 2, "V151": 1, "V155": 3,
    "V158": 1, "V160": 2, "V171": 0, "V172": 2, "V179": 2, "V180": 2, "V181": 0, "V188": 0, "V190": 1,
    "V199": 2, "V206": 1, "V207": 2,
}

fehler = []


def gleich(a, b):
    if isinstance(a, list) != isinstance(b, list):      # Kennung hat heute einen anderen Aufgabentyp (Kennungen verschoben)
        return False
    if isinstance(a, list):
        return isinstance(b, list) and len(a) == len(b) and all(gleich(x, y) for x, y in zip(a, b))
    return abs(float(a) - float(b)) < 1e-9


# Teil A
for k, v in E.items():
    a = A[k]
    o = a["aufgabe"]["o"]
    soll = o.get("werte") if "werte" in o else o.get("wert", o.get("index"))
    if not gleich(v, soll):
        fehler.append(f"A  R15-{k}: eigene Rechnung {v!r} <> Soll {soll!r}")
for k, i in IDX.items():
    a = A[k]
    if a["aufgabe"]["o"].get("index") != i:
        fehler.append(f"A  R15-{k}: eigener Index {i} <> Soll {a['aufgabe']['o'].get('index')}")
nicht_abgedeckt = [k for k in A if k not in E and k not in IDX]
print("Abgedeckt: Zahl/Lücken", len(E), "| Auswahl", len(IDX), "| nicht abgedeckt:", nicht_abgedeckt)

# Teil B: allgemeine Prüfungen
for k, a in sorted(A.items()):
    o = a["aufgabe"]["o"]
    fbs = a["fehlbilder"]
    if a["aufgabe"]["y"] == "zahl":
        w = D(str(o["wert"]))
        tol = D(str(o.get("toleranz") or 0))
        werte = [D(repr(fb["antwort"])) for fb in fbs]
        if len(set(werte)) != len(werte):
            fehler.append(f"B  R15-{k}: Fehlbild-Werte nicht verschieden {werte}")
        for fb, v in zip(fbs, werte):
            if abs(v - w) <= max(D("1e-9"), tol):
                fehler.append(f"B  R15-{k}: Fehlbild {fb['antwort']} liegt in der Toleranz ({tol}) um {w} (Datenbank: <=) und gälte als richtig")
    elif a["aufgabe"]["y"] == "auswahl":
        ant = a["aufgabe"]["a"]
        if len(set(ant)) != len(ant):
            fehler.append(f"B  R15-{k}: Auswahl-Antworten nicht verschieden")
    elif a["aufgabe"]["y"] == "luecken":
        werte = o["werte"]
        fb_je = {}
        for fb in fbs:
            fb_je.setdefault(fb["luecke"], []).append(fb["antwort"])
        for l, lst in fb_je.items():
            if len(set(lst)) != len(lst):
                fehler.append(f"B  R15-{k}: Lücke {l}: Fehlbild-Werte doppelt")
            if werte[l - 1] in lst:
                fehler.append(f"B  R15-{k}: Lücke {l}: Fehlbild gleich richtigem Wert")
        if len(set(werte)) != len(werte):
            print(f"Hinweis R15-{k}: Lückenwerte nicht alle verschieden {werte}")

# Zusatzprüfungen, die die Soll-Antwort nicht allein belegt
# V083: Option 4 (SsW mit Winkel der kleineren Seite gegenüber) liefert zwei Dreiecke
b1 = math.degrees(math.asin(7 * math.sin(math.radians(40)) / 5))
b2 = 180 - b1
assert 40 + b2 < 180, "V083: zweites Dreieck müsste existieren"
print(f"V083 Option 4: zwei Dreiecke mit beta = {b1:.1f} bzw. {b2:.1f} Grad (beide gültig)")
# V065: kleinster Unterschied genügt nicht (nur Logik)
# V074: 360 / 108
assert 360 % 108 != 0
# V057: Raute, nicht Quadrat: eindeutig
# V058: Symmetrieachsen der sechs Vierecke (Wissen): Q 4, Re 2, Ra 2, Pa 0, Dr 1, gl.Trapez 1
assert sum(1 for n in (4, 2, 2, 0, 1, 1) if n >= 1) == 5
# V093: Kehrsätze (1)-(4) brute force für (2) und (4)
assert any(n % 5 == 0 and n % 10 != 0 for n in range(1, 50))
assert any(n % 2 == 0 and n % 4 != 0 for n in range(1, 50))
# V122/V129 Grenzen
assert [x for x in range(-3, 13) if x >= 5] == list(range(5, 13))
# V195: Grenze 60 ein-/ausgeschlossen
print("V195 mit 60 eingeschlossen:", len({m for m in range(1, 61) if m % 6 == 0} | {m for m in range(1, 61) if m % 4 == 0}),
      "| ohne 60:", len({m for m in range(1, 60) if m % 6 == 0} | {m for m in range(1, 60) if m % 4 == 0}),
      "| mit 0:", len({m for m in range(0, 61) if m % 6 == 0} | {m for m in range(0, 61) if m % 4 == 0}))
# V085: Grenzen
print("V085 ganzzahlige c:", [c for c in range(1, 30) if 5 + c > 8 and 13 > c and 8 + 5 > c])
# V059: Fehlbild 303 = ?
print("V059: 180+52+71 =", 180 + 52 + 71, "; 360-57 =", 360 - 57)
# V031: Fehlbild 2048: (2^(9+2)) : 2^10 = ?
print("V031: 2^11 : 2^10 =", 2 ** 11 // 2 ** 10, "(Fehlbild 2048 = 2^11, ohne die Division)")
# V066: Fehlbild 10
print("V066: x aus 2x = 20:", 20 / 2, "; aus 2x = 14+20 =", (14 + 20) / 2, "; aus 2x = 20-14:", (20 - 14) / 2)
# V085: Fehlbild 10
print("V085: Grenzen 3 und 13 beide mitgezählt:", len(range(3, 14)), "; nur eine Grenze:", len(range(4, 14)), "; 13-3 =", 13 - 3)
# V108: Fehlbild 6
print("V108: Kims Fahrzeit bei Treffen:", 4 + 2, "; Vorsprung 36 km / 27 =", 36 / 27, "; /18 =", 36 / 18)
# V114: Fehlbild 130 und 1.3
print("V114: 0,0169*100 =", 0.0169 * 100, "; 0,13 m in mm =", 0.13 * 1000)
# V116: Fehlbild 18
print("V116: Wurzel aus 343 =", 343 ** .5)
# V153: Fehlbild 12
print("V153: (-9+39)/4 =", 30 / 4, "; Länge-Breite-Probe 12*21 =", 12 * 21, "; 360/30 =", 360 / 30, "; 360/9/... ", 360 / 9 - 12)
for x in (3, 5, 12, 15, 24):
    pass
# V193 Fehlbild 11
print("V193: Zahlen mit Ziffernsumme 9 unter 1000:", [n for n in range(1, 100) if sum(map(int, str(n))) == 9])
# V033 Fehlbild 168
print("V033: 14*12 =", 14 * 12, "; 14*7 =", 14 * 7)
# V031 / V124 usw. weitere Kurzchecks siehe Bericht

# V120: Toleranz und Fehlbild 9.3 (exakt, wie in der Datenbank)
print("V120: |9.3 - 9.2| <= 0.1 ?", abs(D("9.3") - D("9.2")) <= D("0.1"), "(Datenbank rechnet numeric, exakt)")
# V143 Teilen durch 6x
# V140 Reihenfolge ② ③
print("V140: Lösungen", quad(2, 0, -98), "(② = 7, ③ = -7 wird verlangt; Reihenfolge nicht angegeben)")

print()
if fehler:
    print(len(fehler), "Meldungen:")
    for m in fehler:
        print(" ", m)
else:
    print("keine Meldungen")
print()
print("HINWEIS: historischer Prüfstand (Stand vor den Korrekturen). Meldungen oben sind erwartet und kein Fehler der Runde;")
print("         maßgeblich ist gegenrechnung.py (alle 207 Sollwerte neu berechnet) und bauen.py.")
sys.exit(0 if not fehler else 2)
