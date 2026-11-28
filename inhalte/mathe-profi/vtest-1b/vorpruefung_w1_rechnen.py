#!/usr/bin/env python3
"""Vorprüfung W1, dritte Runde (Einheit 20, gleichungen.bruch, Stand 1f365ffc, VT1B-022 bis 041): unabhängige Nachrechnung.

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


def hat_loesung(r):
    e, s = r
    return e == "alle" or bool(e)

QR = sorted({F(p, q) for p in range(-30, 31) for q in (1, 2, 3, 4, 5)})

# 022: Leas Gleichung
rL = loese(lambda x: 6 / (x - 2) + 1 / x, lambda x: 3 / (x - 1) + 1 / x, [lambda x: x - 2, lambda x: x - 1, lambda x: x])
pruefe("VT1B-022", [len(rL[0]), 3], [0, 3], f"(Kandidat {rL[1]} verboten; D ohne 0, 1, 2)")
# 023 unverändert
pruefe("VT1B-023", [a for a in QR if {a / 2, F(-3)} == {F(7), F(-3)}], [F(14)])
# 024
r = loese(lambda x: 36 / x, lambda x: 24 / (x - 3), [lambda x: x, lambda x: x - 3])
pruefe("VT1B-024", [2, 3, r[0][0]], [2, 3, F(9)], "(Breiten 9 und 6 positiv)")
# 026: 5/(2x+3) + 1/(x(x−6)): Nullstellen
null = [F(-3, 2), F(0), F(6)]
assert all(2 * z + 3 == 0 or z * (z - 6) == 0 for z in null)
pruefe("VT1B-026", [sum(1 for z in null if z.denominator == 1), len(null)], [2, 3])
# 027: a ≠ 0
ohne = []
for a in sorted(set(QR) | {F(7), F(14)}):
    if a == 0:
        continue
    if not hat_loesung(loese(lambda x, a=a: a / (x + 5), lambda x: 7 / (x - 2), [lambda x: x + 5, lambda x: x - 2])):
        ohne.append(a)
l14 = loese(lambda x: 14 / (x + 5), lambda x: 7 / (x - 2), [lambda x: x + 5, lambda x: x - 2])[0]
pruefe("VT1B-027", [ohne, l14], [[F(7)], [F(9)]])
# 028: für alle p ≠ −q dieselbe Lösung nur für a = 6; Sonderlagen
pq = [(p, q) for p in range(-5, 6) for q in range(-5, 6) if p != -q]
sonder = []
for p, q in pq:
    r15 = loese(lambda x: F(15) / (x - p), lambda x: F(9) / (x + q), [lambda x: x - p, lambda x: x + q])
    if r15[0] == "alle" or len(r15[0]) != 1 or r15[1]:
        sonder.append((p, q, r15))
gut = []
for a in sorted(set(QR) | {F(6), F(10)}):
    if all(loese(lambda x, a=a: F(10) / (x - p), lambda x, a=a: a / (x + q), [lambda x: x - p, lambda x: x + q])
           == loese(lambda x: F(15) / (x - p), lambda x: F(9) / (x + q), [lambda x: x - p, lambda x: x + q])
           for p, q in pq[::7]):
        gut.append(a)
pruefe("VT1B-028", [gut, sonder], [[F(6)], []], f"({len(pq)} Paare: zweite Gleichung hat stets genau eine Lösung, keine Scheinlösung)")
# 029
pruefe("VT1B-029", loese(lambda x: 3 / (x - 2), lambda x: 5 / (x + 4), [lambda x: x - 2, lambda x: x + 4])[0], [F(11)])
# 030: alle a,b,c,d in −4..4 mit a≠b, c≠d, b≠d
faelle = {}
for a_ in range(-4, 5):
    for b_ in range(-4, 5):
        for c_ in range(-4, 5):
            for d_ in range(-4, 5):
                if a_ == b_ or c_ == d_ or b_ == d_:
                    continue
                e, s = loese(lambda x: (x + a_) / (x + b_), lambda x: (x + c_) / (x + d_), [lambda x: x + b_, lambda x: x + d_])
                k = "unendlich" if e == "alle" else len(e)
                faelle[k] = faelle.get(k, 0) + 1
pruefe("VT1B-030", sorted(faelle), [0, 1], f"(Anzahl Gleichungen je Fall {faelle}: „nie mehr als eine“ wahr, „immer eine“ und „nie eine“ falsch, „zwei“ nie)")
# 032
rA = loese(lambda x: (x * x + 4 * x) / (x * x - 4 * x), lambda x: F(-1), [lambda x: x, lambda x: x - 4])
rT = loese(lambda x: (x + 4) / (x - 4), lambda x: F(-1), [lambda x: x - 4])
pruefe("VT1B-032", [len(rT[0]), len(rA[0]), 2], [1, 0, 2], f"(Scheinlösung der Ausgangsgl. {rA[1]})")
# 033
w4 = [c for c in QR + [F(28)] if F(4) in loese(lambda x: 7 / (x - 4) + 2 / x, lambda x, c=c: c / (x * x - 4 * x), [lambda x: x, lambda x: x - 4])[1]]
pruefe("VT1B-033", sorted(set(w4)), [F(28)])
# 034
r = loese(lambda x: 2 / (x - 2) + 3 / (x + 3), lambda x: 10 / ((x - 2) * (x + 3)), [lambda x: x - 2, lambda x: x + 3])
pruefe("VT1B-034", len(r[0]), 0, f"(Scheinlösung {r[1]})")
# 035
r = loese(lambda x: 5 / (x - 4) + 2 / x, lambda x: (x + 16) / (x * x - 4 * x), [lambda x: x, lambda x: x - 4])
z1 = (5 * 4 + 2 * 0, 4 + 16)
pruefe("VT1B-035", [len(r[0]), z1[0] == z1[1]], [0, True], "(Zeile 3 ist als Rechnung wahr – erste FALSCHE Aussage steht erst in Zeile 4)")
# 036: für jedes c: L(Bruchgl.) == L(5x+2=c mit Bedingungen)
def L36(c): 
    e, s = loese(lambda x: 4 / (x + 2) + 1 / x, lambda x: c / (x * x + 2 * x), [lambda x: x, lambda x: x + 2]); return e
opt = {0: set(), 1: {F(-2), F(0)}, 2: {F(0)}, 3: {F(2), F(0)}}
richtig = [i for i, verb in opt.items() if all(L36(c) == [x for x in [(c - 2) / 5] if x not in verb] for c in QR)]
pruefe("VT1B-036", richtig, [1])
# 037
tr = [x for x in range(1, 5001) if (100 + F(x, 4)) * 2 == 100 + F(3 * x, 4)]
pruefe("VT1B-037", tr, [400], "(Saft 200, Wasser 400)")
# 041
pruefe("VT1B-041", {(F(b_) - a_) / a_ * 100 for a_, b_ in [(4, 5), (40, 50), (F(4, 3), F(5, 3))]}, {F(25)})

# Fehlbilder gegen Datei
d = json.load(open(os.path.join(HIER, "gleichungen.bruch.json"), encoding="utf-8"))
for a in d["aufgaben"]:
    nr = int(a["kennung"].split("-")[1])
    if not 22 <= nr <= 41:
        continue
    au = a["aufgabe"]
    if au["y"] == "zahl":
        if any(fb["antwort"] == au["o"]["wert"] for fb in a["fehlbilder"]): fehler.append(a["kennung"] + " Fehlbild=Lösung")
    elif au["y"] == "luecken":
        w = au["o"]["werte"]
        for i in range(1, len(w) + 1):
            if i not in {fb.get("luecke") for fb in a["fehlbilder"]}: fehler.append(f"{a['kennung']} Lücke {i} ohne Fehlbild")
        if any(fb["antwort"] == w[fb["luecke"] - 1] for fb in a["fehlbilder"]): fehler.append(a["kennung"] + " Fehlbild=Lösung")
    else:
        idx = au["o"]["index"]
        if sorted(fb["index"] for fb in a["fehlbilder"]) != [i for i in range(len(au["a"])) if i != idx]:
            fehler.append(a["kennung"] + " Fehlbilder decken Optionen nicht")

print("\nERGEBNIS:", "OK – alle Sollwerte bestätigt" if not fehler else f"FEHLER {fehler}")
sys.exit(1 if fehler else 0)
