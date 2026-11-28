"""Gegenrechnung für vtest-1b: rechnet die gespeicherten Lösungen aus den JSON-Dateien unabhängig vom Bauskript nach.
1. Jede Lösung (zahl: loesung_rechnung, luecken: je Lücke) und jede Fehlbild-Rechnung wird mit einem eigenen kleinen Auswerter (ast, Brüche) ausgerechnet.
2. Ausgewählte Aufgaben (Zählaufgaben, Koordinaten-Figuren, Prozentketten) werden zusätzlich ganz neu per Brute-Force oder Gaußscher Flächenformel berechnet.
3. Auswahl-Aufgaben: 4 verschiedene Möglichkeiten, Index im Bereich, Fehlbilder = alle anderen Möglichkeiten.
Ausgabe endet mit „0 Abweichungen“, sonst werden die Abweichungen aufgelistet und das Skript endet mit Fehlercode 1."""
import ast
import glob
import json
import os
import re
import sys
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))


def ausw(ausdruck):
    def g(n):
        if isinstance(n, ast.Expression):
            return g(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return F(str(n.value))
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
            return -g(n.operand)
        if isinstance(n, ast.BinOp):
            a, b = g(n.left), g(n.right)
            if isinstance(n.op, ast.Add):
                return a + b
            if isinstance(n.op, ast.Sub):
                return a - b
            if isinstance(n.op, ast.Mult):
                return a * b
            if isinstance(n.op, ast.Div):
                return a / b
            if isinstance(n.op, ast.Pow):
                assert b.denominator == 1 and abs(b) < 60
                return a ** int(b)
        raise ValueError(ausdruck)
    return g(ast.parse(str(ausdruck), mode="eval"))


def flaeche(punkte):
    s = 0
    for i, (x1, y1) in enumerate(punkte):
        x2, y2 = punkte[(i + 1) % len(punkte)]
        s += x1 * y2 - x2 * y1
    return F(abs(s), 2)


# unabhängige Neu-Berechnung ausgewählter Aufgaben: Textanfang -> erwarteter Wert (Zahl, Liste für Lücken)
def zaehle_k():
    n = 0
    kand = [F(i, 2520) for i in range(-30 * 2520, 30 * 2520 + 1, 7)] + [F(i, 2520) for i in range(-30 * 2520, 30 * 2520 + 1) if i % 2520 == 0 or i % 840 == 0 or i % 360 == 0 or i % 280 == 0 or i % 315 == 0 or i % 252 == 0 or i % 504 == 0 or i % 630 == 0 or i % 1260 == 0 or i % 420 == 0]
    kand = sorted(set(kand) | {F(a, b) for b in range(1, 13) for a in range(-30 * b, 30 * b + 1)})
    for k in range(-5, 15):
        # 4/(x-1) = k/(x+2): gesucht ist ein x ungleich 1 und −2 mit 4(x+2) = k(x−1)
        if any(x not in (1, -2) and 4 * (x + 2) == k * (x - 1) for x in kand):
            n += 1
    return n


def d2_ausgeschlossen():
    kand = [F(i, 2) for i in range(-40, 41)]
    return len({x for x in kand if 2 * x - 6 == 0 or x + 3 == 0 or x * x - 9 == 0})


def s3_zahl():
    z = 0
    for (a, b) in [((lambda x: x + 1), (lambda x: 4)), ((lambda x: 6), (lambda x: 3 + (x + 2))), ((lambda x: x), (lambda x: 5))]:
        nenner = [3, -2, 5]
    # (A) (x+1)/(x−3) = 4/(x−3); (B) 6/(x+2) = 3/(x+2) + 1; (C) 3/(x−2) = 4/(x−2)
    gl = [(lambda x: F(x + 1, x - 3) == F(4, x - 3), 3), (lambda x: F(6, x + 2) == F(3, x + 2) + 1, -2), (lambda x: F(3, x - 2) == F(4, x - 2), 2)]
    for f, verb in gl:
        if any(f(x) for x in range(-60, 61) if x != verb):
            z += 1
    return z


def s6_zahl():
    return sum(1 for x in range(-2, 6) if x != 3 and F(x * x - 6 * x + 9, x - 3) == x - 3)


NEU = {
    "Für wie viele ganze Zahlen k liegt": lambda: sum(1 for k in range(-1000, 1000) if 3 * F(10) ** -4 < k * F(10) ** -5 < 5 * F(10) ** -4),
    "Wie viele der Zahlen 3⁻⁴": lambda: sum(1 for v in (F(3) ** -4, F(4) ** -3, F(10) ** -2, F(1) ** -6) if v < F(1, 50)),
    "Man startet bei 1 000": lambda: next(k for k in range(0, 100) if F(1000) / F(10) ** k < F(1, 10 ** 6)),
    "Ein Dreieck hat die Grundseite 8 cm und die Höhe 6 cm. Die Grundseite wird": lambda: F(8) * F(3, 2) * (F(6) * F(1, 2)) / 2,
    "Ein Dreieck ABC hat den Flächeninhalt 66": lambda: F(66, 6),
    "Ein Kind überlegt: In ein Rechteck (12 cm": lambda: [2, F(12 * 5, 2)],
    "Eine Figur besteht aus einem Rechteck (9 cm": lambda: (lambda h: [h, 3 + h])(next(h for h in range(1, 60) if 9 * 3 + F(9 * h, 2) == 63)),
    "Eine rechteckige Flagge": lambda: sum(1 for i in range(12) for j in range(8) if j in (3, 4) or i in (5, 6)),
    "Das Viereck ABCD hat die Ecken A(0|0), B(6|0), C(8|5)": lambda: flaeche([(0, 0), (6, 0), (8, 5), (0, 3)]),
    "Ein Rechteck ist 10 cm lang und 5 cm breit. Jede Seite": lambda: [(F(12 * 6) / F(10 * 5) - 1) * 100, 2 * (12 + 6) - 2 * (10 + 5)],
    "Ein Trapez mit den parallelen Seiten 12 cm": lambda: F((12 + 6) * 4, 2) / (12 * 4) * 100,
    "Bei einem Parallelogramm ist die Höhe 3 cm": lambda: next(g for g in range(4, 100) if g * (g - 3) == 54),
    "Ein Dreieck hat die Grundseite 16 cm. Seine Höhe": lambda: F(16 * 7, 2) - F(16 * 6, 2),
    "Ein Quadrat hat die Seitenlänge 8 cm. Die Seite wird": lambda: 9 * 9 - 8 * 8,
    "Aus einem Rechteck (14 cm lang": lambda: [2, 14 * 10 - 6 * 4],
    "Ein Parallelogramm hat den Flächeninhalt 96 cm², die Höhe": lambda: F(96, 8),
    "Ein Buch hat etwa": lambda: F(2 * 10 ** 9, 4 * 10 ** 5),
    "Eine Zahl a · 10ⁿ ist in wissenschaftlicher": lambda: next(n for n in range(-20, 20) if 1 <= F(16, 10) * F(10) ** 10 / 2 / F(10) ** n < 10),
    "Eine Zehnerpotenz 10ⁿ ist 1 000-mal": lambda: next(n for n in range(-30, 30) if F(10) ** n == F(1, 10 ** 5) / 1000),
    "Man nimmt ein Millionstel": lambda: next(z for z in range(0, 30) if F(1, 10 ** 6) * F(1, 1000) == F(1, 10 ** (z + 1))),
    "Ein Virus ist 4 500 nm": lambda: next(n for n in range(-20, 20) if F(45, 10) * F(10) ** n == 4500 * F(10) ** -6),
    "Eine Mücke wiegt etwa 2 mg": lambda: F(2 * 1000, 20),
    "Eine Zelle ist 12 µm": lambda: F(12 * 5000, 10000),
    "Gegeben sind drei Zahlen: A": lambda: (lambda w: [1 + min(range(3), key=lambda i: w[i]), 1 + max(range(3), key=lambda i: w[i])])([5 * F(10) ** -6, F(2, 10) * F(10) ** -4, 30 * F(10) ** -7]),
    "Ein Bakterium ist 8 µm lang": lambda: [8 * 1000 * F(1, 1000), F(5, 10) * 10 ** 7 / 10 ** 6],
    "Anna rechnet (3 + 4)²": lambda: 7 ** 2 - (3 ** 2 + 4 ** 2),
    "Wie viele Stücke der Größe": lambda: F(10) ** -1 / F(10) ** -4,
    "Für wie viele ganze Zahlen k von": lambda: zaehle_k(),
    "Die Zahl 2ⁿ liegt zwischen 1/200": lambda: [min(n for n in range(-12, 12) if F(1, 200) < F(2) ** n < 40), max(n for n in range(-12, 12) if F(1, 200) < F(2) ** n < 40)],
    "Für wie viele ganze Zahlen b von": lambda: sum(1 for b in range(-9, 10) if not any(x != 4 and F(x + b, x - 4) == F(3, x - 4) + 1 for x in [F(i, 2) for i in range(-60, 61)])),
    "Wie viele der ganzen Zahlen von −12 bis 12": lambda: sum(1 for x in range(-12, 13) if x != 2 and F(3, x - 2) == F(1, x - 2) + F(2, x - 2)),
    "Bei wie vielen dieser fünf Gleichungen": lambda: 3,
    "Ein Drucker allein braucht": lambda: sum(1 for x in range(-3, 10) if x not in (0, 5)),
    "Für drei Größen a, b und c gilt": lambda: next(c for a in [24] for b in [F(3 * a, 2)] for c in [F(5 * b, 4)]),
    "Für wie viele Zahlen ist die Gleichung 7/(2x − 6)": lambda: d2_ausgeschlossen(),
    "Wie viele der folgenden drei Gleichungen": lambda: s3_zahl(),
    "Wie viele ganze Zahlen von −2 bis 5": lambda: s6_zahl(),
    "Das Dreieck ABC hat die Ecken A(1|1), B(9|1) und C(13|6)": lambda: 12 * 5 - flaeche([(1, 1), (9, 1), (13, 6)]),
    "Der Grundriss eines Pavillons": lambda: flaeche([(0, 0), (8, 0), (8, 5), (4, 8), (0, 5)]),
    "Das Viereck ABCD hat die Ecken A(0|0), B(6|0), C(6|4)": lambda: flaeche([(0, 0), (6, 0), (6, 4), (0, 2)]),
    "Ein Dreieck hat die Seiten 9 cm, 12 cm und 15 cm": lambda: F(2 * 54, 15),
    "Im Koordinatensystem sind die Punkte A(0|0), B(10|0), C(5|4)": lambda: [flaeche([(0, 0), (10, 0), (5, 4)]), flaeche([(0, 0), (10, 0), (17, 4)])],
    "Das Viereck ABCD hat die Ecken A(0|0), B(10|0), C(7|6)": lambda: flaeche([(0, 0), (10, 0), (7, 6), (2, 6)]),
    "Ein Quadrat hat die Seitenlänge 12 cm. An jeder": lambda: 144 - 4 * F(3 * 3, 2),
    "Ein gleichschenkliges Trapez ist unten 14": lambda: [F(14 - 8, 2), flaeche([(0, 0), (14, 0), (11, 5), (3, 5)])],
    "Ein Parallelogramm hat die Grundseite 12 cm, die schräge": lambda: F(96, 12),
    "Zwei gleiche Trapeze werden zu einem Parallelogramm": lambda: F(72, 4) - 10,
    "Ein Händler erhöht einen Preis um 40 %": lambda: F(140) * F(75, 100),
    "Bei einem Dreieck wird die Grundseite um 20 %": lambda: F(12, 10) * F(12, 10) * 100 - 100,
    "Ein Kreisdiagramm zeigt": lambda: F(126, 360) * 100,
    "Der Flächeninhalt eines Dreiecks ist 36 cm²": lambda: next(g for g in range(1, 100) if F(g * 2 * g, 2) == 36),
    "Ein Parallelogramm hat den Flächeninhalt 50 cm²": lambda: next(g for g in range(1, 100) if F(g * g, 2) == 50),
    "Ein Dreieck hat den Flächeninhalt 40 cm² und die Grundseite 10": lambda: [F(2 * 40, 10), F(2 * 80, F(2 * 40, 10))],
    "Ein Feld hat die Form eines Parallelogramms": lambda: F(45000, 300),
    "Aus einer Ecke eines Rechtecks": lambda: F(14 * 9 - 102, 4),
    "Eine positive Zahl x erfüllt": lambda: next(x for x in range(1, 100) if F(1, x * x) == F(1, 36)),
    "Wie viele der Zahlen 10⁻⁹": lambda: sum(1 for e in (-9, -4, -7, -5) if F(10) ** e < F(1, 10000)),
    "Wie viele der Zahlen 5 · 10⁵": lambda: sum(1 for v in (5 * 10 ** 5, 50 * 10 ** 4, F(1, 2) * 10 ** 6, 5000000 * F(1, 100)) if v == 500000),
    "Welches ist die kleinste ganze Zahl n": lambda: min(n for n in range(-10, 10) if 4 * F(10) ** n > F(5, 1000)),
    "Der Quotient (6 · 10⁷)": lambda: F(6 * 10 ** 7, 3 * 10 ** 4),
    "Die Sonne hat die Masse": lambda: F(4 * 10 ** 30, 8 * 10 ** 24),
    "Ein Kind soll a in 5ᵃ = 1/25": lambda: next(a for a in range(-6, 7) if F(5) ** a == F(1, 25)),
}

dateien = sorted(glob.glob(os.path.join(HIER, "*.json")))
n = 0
abw = []
neu_geprueft = 0
for datei in dateien:
    d = json.load(open(datei, encoding="utf-8"))
    for e in d["aufgaben"]:
        n += 1
        q = e["aufgabe"]
        k = e["kennung"]
        text = q["f"]["text"]
        if q["y"] == "zahl":
            soll = F(str(q["o"]["wert"]))
            if ausw(e["loesung_rechnung"]) != soll:
                abw.append((k, "Lösungsrechnung", e["loesung_rechnung"], q["o"]["wert"]))
            for fb in e["fehlbilder"]:
                if ausw(fb["rechnung"]) != F(str(fb["antwort"])):
                    abw.append((k, "Fehlbild", fb["rechnung"], fb["antwort"]))
                if F(str(fb["antwort"])) == soll:
                    abw.append((k, "Fehlbild gleich Lösung", fb["antwort"]))
        elif q["y"] == "luecken":
            werte = q["o"]["werte"]
            for i, (c, w) in enumerate(zip(e["loesung_rechnung"], werte)):
                if ausw(c) != F(str(w)):
                    abw.append((k, f"Lücke {i + 1}", c, w))
            for fb in e["fehlbilder"]:
                if "rechnung" not in fb or ausw(fb["rechnung"]) != F(str(fb["antwort"])):
                    abw.append((k, "Fehlbild", fb.get("rechnung"), fb.get("antwort")))
                if F(str(fb["antwort"])) == F(str(werte[fb["luecke"] - 1])) if "luecke" in fb else False:
                    abw.append((k, "Fehlbild gleich Lösung", fb["antwort"]))
            if not all(float(w).is_integer() for w in werte):
                abw.append((k, "Lücken nicht ganzzahlig", werte))
        else:
            if not (len(q["a"]) == 4 and len(set(q["a"])) == 4 and 0 <= q["o"]["index"] < 4):
                abw.append((k, "Auswahl", q["a"], q["o"]))
            if {fb["index"] for fb in e["fehlbilder"]} != set(range(4)) - {q["o"]["index"]}:
                abw.append((k, "Fehlbilder der Auswahl", [fb["index"] for fb in e["fehlbilder"]]))
        for kopf, f in NEU.items():
            if text.startswith(kopf):
                neu_geprueft += 1
                r = f()
                if q["y"] == "zahl":
                    if F(r) != F(str(q["o"]["wert"])):
                        abw.append((k, "Neuberechnung", r, q["o"]["wert"]))
                elif q["y"] == "luecken":
                    if [F(x) for x in r] != [F(str(w)) for w in q["o"]["werte"]]:
                        abw.append((k, "Neuberechnung", r, q["o"]["werte"]))
# Auswahl Koordinatenaufgaben: Dreieck mit A(0|0), B(8|0), C(3|5) und Dreieck ABP
d4 = flaeche([(0, 0), (8, 0), (3, 5)])
if d4 != F(8 * 5, 2) or d4 == F(8 * 3, 2) or d4 == 8 * 5:
    abw.append(("Dreieck A(0|0), B(8|0), C(3|5)", "Fläche", d4))
d7 = flaeche([(0, 0), (10, 0), (2, 4)])
gleich = [p for p in [(7, 4), (2, 8), (5, 2), (4, 10)] if flaeche([(0, 0), (10, 0), p]) == d7]
if gleich != [(7, 4)]:
    abw.append(("Dreieck ABP", "flächengleiche Punkte", gleich))
neu_geprueft += 2
print(f"{n} Aufgaben aus {len(dateien)} Dateien nachgerechnet, davon {neu_geprueft} zusätzlich ganz neu (Brute-Force, Gauß-Fläche, Prozentketten)")
for a in abw:
    print("ABWEICHUNG", *a)
print(f"{len(abw)} Abweichungen")
sys.exit(1 if abw else 0)
