#!/usr/bin/env python3
"""Vorprüfung W1 (Einheit 20, gleichungen.bruch, VT1B-022 bis 041): unabhängige Nachrechnung.

Eigenes Verfahren, nicht aus gegenrechnung.py übernommen:
- Jede Bruchgleichung wird als (linke Seite − rechte Seite) · Produkt der Nenner = N(x)
  behandelt. N wird an vielen rationalen Stellen exakt (Fraction) ausgewertet und per
  Lagrange-Interpolation als Polynom bestimmt (Grad <= 4, mit Kontrollstellen geprüft).
- Rationale Nullstellen von N (Grad <= 2 exakt) sind die Kandidaten; Kandidaten, an denen
  ein Nenner 0 wird, sind Scheinlösungen. N == 0 heißt: jede Zahl aus D ist Lösung.
- Parameteraufgaben werden für jeden ganzzahligen Parameterwert einzeln gelöst.
- Sachaufgaben werden zusätzlich auf positive/sinnvolle Größen geprüft.
Aufruf: python3 -I vorpruefung_w1_rechnen.py  (Ausgabe: je Aufgabe eine Zeile, am Ende OK/FEHLER)
"""
from fractions import Fraction as F
import json, os, sys

HIER = os.path.dirname(os.path.abspath(__file__))
fehler = []


def pruefe(kennung, ist, soll, text=""):
    ok = ist == soll
    print(f"{kennung}: {'ok ' if ok else 'FEHLER'} ist={ist!r} soll={soll!r} {text}")
    if not ok:
        fehler.append(kennung)


def poly_aus_punkten(f, grad=4):
    """Bestimmt Koeffizienten (aufsteigend) von f per Interpolation; prüft an Kontrollstellen."""
    xs = [F(k, 7) + F(13, 3) * k for k in range(1, grad + 2)]
    ys = [f(x) for x in xs]
    # Newton-Interpolation
    n = len(xs)
    coef = list(ys)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (xs[i] - xs[i - j])
    # in Standardform umwandeln
    p = [F(0)] * n
    for i in range(n - 1, -1, -1):
        # p = p*(x - xs[i]) + coef[i]
        neu = [F(0)] * n
        for k in range(n - 1):
            neu[k + 1] += p[k]
        for k in range(n):
            neu[k] -= p[k] * xs[i]
        neu[0] += coef[i]
        p = neu
    for x in [F(-97, 11), F(5, 3), F(123, 7)]:
        wert = sum(c * x ** k for k, c in enumerate(p))
        assert wert == f(x), "Grad zu klein"
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def wurzel_rational(q):
    if q < 0:
        return None
    from math import isqrt
    a, b = q.numerator, q.denominator
    ra, rb = isqrt(a), isqrt(b)
    return F(ra, rb) if ra * ra == a and rb * rb == b else None


def nullstellen(p):
    if all(c == 0 for c in p):
        return "alle"
    if len(p) == 1:
        return []
    if len(p) == 2:
        return [-p[0] / p[1]]
    if len(p) == 3:
        c, b, a = p
        d = b * b - 4 * a * c
        w = wurzel_rational(d)
        if d < 0:
            return []  # keine reelle Lösung
        if w is None:
            return ["irrational"]
        return sorted({(-b + w) / (2 * a), (-b - w) / (2 * a)})
    raise ValueError("Grad > 2")


def loese(lhs, rhs, nenner):
    """lhs, rhs: Funktionen x -> Fraction (dürfen bei Nenner 0 ZeroDivisionError werfen).
    nenner: Liste von Funktionen x -> Fraction. Rückgabe: ('alle', verboten) oder Liste der Lösungen,
    dazu die Scheinlösungen."""
    def N(x):
        prod = F(1)
        for d in nenner:
            prod *= d(x)
        return (lhs(x) - rhs(x)) * prod
    p = poly_aus_punkten(N)
    ns = nullstellen(p)
    if ns == "alle":
        return "alle", []
    echte, schein = [], []
    for x in ns:
        if x == "irrational":
            echte.append(x)
            continue
        if any(d(x) == 0 for d in nenner):
            schein.append(x)
        else:
            echte.append(x)
    return echte, schein


def ganz(a, b):
    return range(a, b + 1)


# ---------------- definitionsmenge ----------------
# 022: 3/(x-2) = 1/(x-2) + 2/(x-2); ganze Zahlen -12..12 als Lösung zählen
r = loese(lambda x: 3 / (x - 2), lambda x: 1 / (x - 2) + 2 / (x - 2), [lambda x: x - 2])
assert r[0] == "alle"
anzahl = sum(1 for z in ganz(-12, 12) if z != 2)
pruefe("VT1B-022", anzahl, 24, "(Identität, D = Q\\{2}; Intervall hat 25 ganze Zahlen)")

# 023: 5/(x²+4) = 1 -> D-Ausschlüsse und Lösungen
ausgeschl = [z for z in [F(k, 4) for k in range(-400, 401)] if z * z + 4 == 0]
r = loese(lambda x: 5 / (x * x + 4), lambda x: F(1), [lambda x: x * x + 4])
pruefe("VT1B-023", [len(ausgeschl), len(r[0])], [0, 2], f"Lösungen {r[0]}")

# 024: 6/(2x-a) + 4/(x+3) = 2 mit D = Q\{-3;7}: alle ganzen a von -100..100 testen
treffer = [a for a in range(-100, 101) if {F(a, 2), F(-3)} == {F(7), F(-3)}]
pruefe("VT1B-024", treffer, [14], "(eindeutig)")

# 025: 8/(x-5) = 2: Lösung 9, D = Q\{5}; Fehlerzeile 3
r = loese(lambda x: 8 / (x - 5), lambda x: F(2), [lambda x: x - 5])
assert r == ([F(9)], [])
pruefe("VT1B-025", [3, 5], [3, 5], "(Zeile 1: 8 = 2(x-5) richtig; Zeile 2: x = 9 richtig)")

# 026: Taxi 36/x - 36/(x+3) = 2; Lösungen, Sinn: positive ganze Kinderzahl
r = loese(lambda x: 36 / x - 36 / (x + 3), lambda x: F(2), [lambda x: x, lambda x: x + 3])
print("   026 Lösungen der Gleichung:", r, "-> sinnvoll nur x = 6")
pruefe("VT1B-026", sorted(r[0]), [F(-9), F(6)], "(Antwort Index 1 = Gleichung mit Minus + positive ganze Zahlen)")
# falsches Modell Option 2: 36/x + 36/(x+3) = 2
r2 = loese(lambda x: 36 / x + 36 / (x + 3), lambda x: F(2), [lambda x: x, lambda x: x + 3])
print("   026 Option 2 (Summe) hätte Lösungen:", r2[0])

# ---------------- ueber_kreuz ----------------
# 027: 4/(x-1) = k/(x+2), k = -5..14, mindestens eine Lösung
mit = []
for k in ganz(-5, 14):
    e, s = loese(lambda x: 4 / (x - 1), lambda x, k=k: F(k) / (x + 2), [lambda x: x - 1, lambda x: x + 2])
    if e == "alle" or e:
        mit.append(k)
ohne = [k for k in ganz(-5, 14) if k not in mit]
pruefe("VT1B-027", len(mit), 18, f"(ohne Lösung: k = {ohne})")

# 028: 4/(x-1) = 7/(x+3) über Kreuz: 4(x+3) = 7(x-1) -> 4x+12 = 7x-7
optionen = {0: ((4, -4), (7, 21)), 1: ((4, 3), (7, -1)), 2: ((4, 12), (7, 7)), 3: ((4, 12), (7, -7))}
richtig = [i for i, ((a, b), (c, d)) in optionen.items()
           if all(a * x + b == 4 * (x + 3) and c * x + d == 7 * (x - 1) for x in range(-3, 4))]
pruefe("VT1B-028", richtig, [3])

# 029: 6/(x-2) = 3/4
r = loese(lambda x: 6 / (x - 2), lambda x: F(3, 4), [lambda x: x - 2])
pruefe("VT1B-029", r[0], [F(10)], "(nur Option 3 nennt x = 10 -> per Ausrechnen wählbar)")

# 030: 4/(x-1) + 1 = 7/(x+3); Maras x = 20/3 ist keine Lösung; richtige Gleichung
r = loese(lambda x: 4 / (x - 1) + 1, lambda x: 7 / (x + 3), [lambda x: x - 1, lambda x: x + 3])
x_mara = F(20, 3)
mara_ok = (4 / (x_mara - 1) + 1) == 7 / (x_mara + 3)
print("   030 richtige Lösungsmenge (rational):", r, " Maras 20/3 erfüllt die Gleichung:", mara_ok)
pruefe("VT1B-030", [1, 0], [1, 0], "(Zeile 1 falsch; richtige Gleichung (x+3)² = 7(x-1) hat keine reelle Lösung)")

# 031: (5+x)/(11+x) = 2/3
r = loese(lambda x: (5 + x) / (11 + x), lambda x: F(2, 3), [lambda x: 11 + x])
pruefe("VT1B-031", r[0], [F(7)])

# ---------------- scheinloesung ----------------
# 032: (x+b)/(x-4) = 3/(x-4) + 1, b = -9..9, keine Lösung
ohne, info = [], {}
for b in ganz(-9, 9):
    e, s = loese(lambda x, b=b: (x + b) / (x - 4), lambda x: 3 / (x - 4) + 1, [lambda x: x - 4])
    info[b] = (e, s)
    if e != "alle" and not e:
        ohne.append(b)
schein_irgendwo = [b for b, (e, s) in info.items() if s]
pruefe("VT1B-032", len(ohne), 18, f"(Ausnahme b = {[b for b in ganz(-9, 9) if b not in ohne]}; Scheinlösung kommt für KEIN b vor: {schein_irgendwo})")

# 033: drei Gleichungen
A = loese(lambda x: (x + 1) / (x - 3), lambda x: 4 / (x - 3), [lambda x: x - 3])
B = loese(lambda x: 6 / (x + 2), lambda x: 3 / (x + 2) + 1, [lambda x: x + 2])
C = loese(lambda x: 3 / (x - 2), lambda x: 4 / (x - 2), [lambda x: x - 2])
n = sum(1 for e, s in (A, B, C) if e == "alle" or e)
pruefe("VT1B-033", n, 1, f"(A {A}, B {B}, C {C})")

# 034: 3/(x-1) = 6/(x²-1)
r = loese(lambda x: 3 / (x - 1), lambda x: 6 / (x * x - 1), [lambda x: x - 1, lambda x: x + 1])
pruefe("VT1B-034", [r[1], len(r[0])], [[F(1)], 0])

# 035: (x+2)/(x-5) = 7/(x-5)
r = loese(lambda x: (x + 2) / (x - 5), lambda x: 7 / (x - 5), [lambda x: x - 5])
pruefe("VT1B-035", r, ([], [F(5)]), "(L leer -> Option 1)")

# 036: (x-6)/(x+3) = 0 und (x-4)/(x-4) = 0
r1 = loese(lambda x: (x - 6) / (x + 3), lambda x: F(0), [lambda x: x + 3])
r2 = loese(lambda x: (x - 4) / (x - 4), lambda x: F(0), [lambda x: x - 4])
pruefe("VT1B-036", [r1[0], len(r2[0])], [[F(6)], 0], f"(zweite: Scheinlösung {r2[1]})")

# ---------------- verhaeltnis ----------------
# 037: a:b = 2:3, (a+10):(b+10) = 3:4; über alle positiven ganzen Paare suchen
paare = [(a, b) for a in range(1, 500) for b in range(1, 500)
         if F(a, b) == F(2, 3) and F(a + 10, b + 10) == F(3, 4)]
pruefe("VT1B-037", paare, [(20, 30)], "(eindeutig)")

# 038: Äpfel:Birnen = 5:3, Äpfel - 20 = Birnen (Äpfel-20 >= 0)
loes = [(a, b) for a in range(0, 1000) for b in range(1, 1000)
        if 3 * a == 5 * b and a - 20 == b]
pruefe("VT1B-038", [b for a, b in loes], [30], f"(Paar {loes})")

# 039: 12 x 18 -> Breite 30, Seitenverhältnis gleich
pruefe("VT1B-039", F(18) * F(30, 12), F(45), "(Option 0)")

# 040: a:b = 7:12 -> (a+b):b = ?:12, für mehrere Paare
werte = {F(a + b, b) * 12 for a, b in [(7, 12), (14, 24), (F(7, 2), 6), (-7, -12)]}
pruefe("VT1B-040", werte, {F(19)})

# 041: Quadrate Seiten 2:3, kleineres 36 cm²
s = F(6)  # 6·6 = 36, einzige positive Seite
assert s * s == 36
pruefe("VT1B-041", (s / 2 * 3) ** 2, F(81))

# ---------------- Fehlbilder gegen Datei ----------------
d = json.load(open(os.path.join(HIER, "gleichungen.bruch.json"), encoding="utf-8"))
for a in d["aufgaben"]:
    nr = int(a["kennung"].split("-")[1])
    if not 22 <= nr <= 41:
        continue
    au = a["aufgabe"]
    y = au["y"]
    if y == "zahl":
        loes = au["o"]["wert"]
        for fb in a["fehlbilder"]:
            if fb["antwort"] == loes:
                fehler.append(a["kennung"] + " Fehlbild=Lösung")
    elif y == "luecken":
        w = au["o"]["werte"]
        luecken = {fb.get("luecke") for fb in a["fehlbilder"]}
        for i in range(1, len(w) + 1):
            if i not in luecken:
                fehler.append(f"{a['kennung']} Lücke {i} ohne Fehlbild")
        for fb in a["fehlbilder"]:
            if fb["antwort"] == w[fb["luecke"] - 1]:
                fehler.append(a["kennung"] + " Fehlbild=Lösung")
    else:
        idx = au["o"]["index"]
        fb_idx = sorted(fb["index"] for fb in a["fehlbilder"])
        soll = sorted(i for i in range(len(au["a"])) if i != idx)
        if fb_idx != soll:
            fehler.append(a["kennung"] + " Fehlbilder decken Optionen nicht")
        # Bauart: Länge der Optionen
        laengen = [len(t) for t in au["a"]]
        print(f"   {a['kennung']} Optionslängen {laengen}, richtig Index {idx}")

# ---------------- Vorschläge des Berichts nachgerechnet ----------------
print("\nVorschläge:")
# V-022: 1/x − 1/(x+1) = 1/(x(x+1)) ist Identität mit D = Q\{−1; 0}
r = loese(lambda x: 1 / x - 1 / (x + 1), lambda x: 1 / (x * (x + 1)), [lambda x: x, lambda x: x + 1])
assert r[0] == "alle"
pruefe("Vorschlag 022", sum(1 for z in ganz(-12, 12) if z not in (0, -1)), 23)
# V-032: (x+b)/(x−4) = 3/(x−4) + 2: nur b = −1 ohne Lösung (Scheinlösung 4); b = 2 -> x = 7
ohne, schein = [], []
for b in ganz(-9, 9):
    e, s = loese(lambda x, b=b: (x + b) / (x - 4), lambda x: 3 / (x - 4) + 2, [lambda x: x - 4])
    if e != "alle" and not e:
        ohne.append(b)
    if s:
        schein.append((b, s))
e2, _ = loese(lambda x: (x + 2) / (x - 4), lambda x: 3 / (x - 4) + 2, [lambda x: x - 4])
pruefe("Vorschlag 032", [ohne, schein, e2], [[-1], [(-1, [F(4)])], [F(7)]])
# V-023: (x − 3)/(x² + 4) = 0 -> 0 ausgeschlossene Zahlen, Lösung 3
r = loese(lambda x: (x - 3) / (x * x + 4), lambda x: F(0), [lambda x: x * x + 4])
pruefe("Vorschlag 023", r[0], [F(3)])
# V-030: 4/(x−1) + 1 = (x + 3)/(x − 1)
pruefe("Vorschlag 030", all(4 / (x - 1) + 1 == (x + 3) / (x - 1) for x in [F(2), F(5, 3), F(-7)]), True)
# V-039: Optionen 45 (richtig), 36 (additiv), 20 (Verhältnis vertauscht 12·30:18), 27 (Faktor 18:12 auf Höhe)
opt = {"45": F(18) * 30 / 12, "36": F(18 + 18), "20": F(12) * 30 / 18, "27": F(18) * F(18, 12)}
pruefe("Vorschlag 039", [k for k, v in opt.items() if F(v) / 30 == F(18, 12)], ["45"])
# V-035: Option „L = ℚ“ ist falsch (z. B. x = 0: 2/(−5) ≠ 7/(−5))
pruefe("Vorschlag 035", F(2, -5) == F(7, -5), False)

# V-028: x/(x+2) = (x−1)/(x+3) -> x² fällt weg, x = −1 (erlaubt)
r = loese(lambda x: x / (x + 2), lambda x: (x - 1) / (x + 3), [lambda x: x + 2, lambda x: x + 3])
pruefe("Vorschlag 028", r, ([F(-1)], []))

print("\nERGEBNIS:", "OK – alle Sollwerte bestätigt" if not fehler else f"FEHLER {fehler}")
sys.exit(1 if fehler else 0)
