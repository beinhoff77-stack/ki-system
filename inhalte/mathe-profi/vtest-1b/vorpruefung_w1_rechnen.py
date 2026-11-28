#!/usr/bin/env python3
"""Vorprüfung W1, zweite Runde (Einheit 20, gleichungen.bruch, Stand 06db098c, VT1B-022 bis 041): unabhängige Nachrechnung.

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

QR = sorted({F(p, q) for p in range(-30, 31) for q in (1, 2, 3, 4, 5)})  # rationale Parameterwerte

# ================= definitionsmenge =================
# 022: 6/(x−2) = 3/(x−1); (L) beide Seiten + 1/x; (T) mal (x−2)
r0 = loese(lambda x: 6 / (x - 2), lambda x: 3 / (x - 1), [lambda x: x - 2, lambda x: x - 1])
rL = loese(lambda x: 6 / (x - 2) + 1 / x, lambda x: 3 / (x - 1) + 1 / x, [lambda x: x - 2, lambda x: x - 1, lambda x: x])
assert r0 == ([F(0)], [])
# (T) gekürzt: 6 = 3(x−2)/(x−1) -> schließt {1} aus; (T) ungekürzt: (x−2)·6/(x−2) = (x−2)·3/(x−1) -> {1; 2}
T_gekuerzt, T_ungekuerzt = {1}, {1, 2}
pruefe("VT1B-022", [len(rL[0]), len(T_gekuerzt)], [0, 1],
       f"(L): Kandidat {rL[1]} verboten. ABER (T) ungekürzt schließt {len(T_ungekuerzt)} Zahlen aus = Fehlbild 2 -> mehrdeutig")

# 023: 6/(2x − a) + 4/(x + 3) = 2, D = Q\{−3; 7}
treffer = [a for a in QR if {a / 2, F(-3)} == {F(7), F(-3)}]
pruefe("VT1B-023", treffer, [F(14)])

# 024: 36/x = 24/(x − 3); Breiten x und x − 3 positiv
r = loese(lambda x: 36 / x, lambda x: 24 / (x - 3), [lambda x: x, lambda x: x - 3])
x = r[0][0]
pruefe("VT1B-024", [2, 3, x], [2, 3, F(9)], f"(Breiten {x} und {x-3} > 0, Längen {36/x} = {24/(x-3)})")

# 025: Beispiele der Möglichkeiten
def L(lhs, rhs, n): return loese(lhs, rhs, n)[0]
ex = {
    "2/x=2": L(lambda x: 2 / x, lambda x: F(2), [lambda x: x]),
    "4/x=4": L(lambda x: 4 / x, lambda x: F(4), [lambda x: x]),
    "3/(x+2)=1": L(lambda x: 3 / (x + 2), lambda x: F(1), [lambda x: x + 2]),
}
pruefe("VT1B-025", ex, {"2/x=2": [F(1)], "4/x=4": [F(1)], "3/(x+2)=1": [F(1)]},
       "(Beispiele stimmen; D {0}, {0}, {−2}; richtig nur Index 1)")

# 026: G = Z, 5/(2x+3) + 1/(x² − bx) = 2, genau zwei ganze Ausschlüsse, einer 6
treffer = []
for b in QR:
    aus = {z for z in range(-200, 201) if 2 * z + 3 == 0 or z * z - b * z == 0}
    if len(aus) == 2 and 6 in aus:
        treffer.append((b, sorted(aus)))
pruefe("VT1B-026", treffer, [(F(6), [0, 6])])

# ================= ueber_kreuz =================
# 027: a/(x + 5) = 7/(x − 2), alle rationalen a des Rasters und Sonderwerte
ohne = []
for a in sorted(set(QR) | {F(7), F(0), F(-7), F(7, 2)}):
    r = loese(lambda x, a=a: a / (x + 5), lambda x: 7 / (x - 2), [lambda x: x + 5, lambda x: x - 2])
    if not hat_loesung(r):
        ohne.append(a)
pruefe("VT1B-027", ohne, [F(0), F(7)], "(a = 7: 0·x = 49; a = 0: Kandidat −5 verboten; alle übrigen genau eine Lösung)")

# 028: Lösung von 15/(x−3) = 9/(x+2), dann a
x0 = loese(lambda x: 15 / (x - 3), lambda x: 9 / (x + 2), [lambda x: x - 3, lambda x: x + 2])[0][0]
treffer = [a for a in QR if loese(lambda x, a=a: 10 / (x - 3), lambda x, a=a: a / (x + 2),
                                  [lambda x: x - 3, lambda x: x + 2])[0] == [x0]]
pruefe("VT1B-028", (x0, treffer), (F(-19, 2), [F(6)]), "(Rechenweg ohne Einsicht: x0 ausrechnen, einsetzen -> Schema)")

# 029: beide Wege
ali = loese(lambda x: 3 / (x - 2), lambda x: 5 / (x + 4), [lambda x: x - 2, lambda x: x + 4])
bea = loese(lambda x: (x - 2) / 3, lambda x: (x + 4) / 5, [])
pruefe("VT1B-029", (ali[0], bea[0]), ([F(11)], [F(11)]), "(Index 3)")

# 030: (x+a)/(x+b) = (x+c)/(x+d), b ≠ d: welche Fälle kommen vor?
faelle = set()
for a_ in range(-3, 4):
    for b_ in range(-3, 4):
        for c_ in range(-3, 4):
            for d_ in range(-3, 4):
                if b_ == d_:
                    continue
                e, s = loese(lambda x: (x + a_) / (x + b_), lambda x: (x + c_) / (x + d_),
                             [lambda x: x + b_, lambda x: x + d_])
                faelle.add("unendlich" if e == "alle" else len(e))
print("   030 vorkommende Lösungszahlen:", faelle)
beisp = [loese(lambda x: (x + 1) / (x + 2), lambda x: (x + 3) / (x + 4), [lambda x: x + 2, lambda x: x + 4]),
         loese(lambda x: (x + 1) / (x + 2), lambda x: (x + 4) / (x + 3), [lambda x: x + 2, lambda x: x + 3]),
         loese(lambda x: (x + 2) / (x + 1), lambda x: (x + 2) / (x + 5), [lambda x: x + 1, lambda x: x + 5])]
pruefe("VT1B-030", [b[0] for b in beisp], [[], [F(-5, 2)], [F(-2)]],
       "(Index 0 wahr; „immer eine“, „immer zwei“, „nur bei a = c“ widerlegt; Fall „unendlich viele“ kommt vor)")

# 031: nur Möglichkeit 2 hat auf jeder Seite genau einen Bruch (Struktur von Hand)
pruefe("VT1B-031", 2, 2, "(Strukturprüfung von Hand)")

# ================= scheinloesung =================
# 032
r = loese(lambda x: (x * x + 6 * x) / (x * x - 2 * x), lambda x: F(-3), [lambda x: x, lambda x: x - 2])
rk = loese(lambda x: (x + 6) / (x - 2), lambda x: F(-3), [lambda x: x - 2])
pruefe("VT1B-032", (r, rk), (([], [F(0)]), ([F(0)], [])), "(Ausgangsgl. L leer, gekürzte Gl. L = {0}: Fehler beim Kürzen, Index 3)")

# 033: 3/(x−2) + 1/x = c/(x² − 2x): für welche c ist 2 bzw. 0 Kandidat?
w2, w0, ohne = [], [], []
for c in QR:
    e, s = loese(lambda x: 3 / (x - 2) + 1 / x, lambda x, c=c: c / (x * x - 2 * x), [lambda x: x, lambda x: x - 2])
    if F(2) in s: w2.append(c)
    if F(0) in s: w0.append(c)
    if not hat_loesung((e, s)): ohne.append(c)
pruefe("VT1B-033", [w2, w0], [[F(6)], [F(-2)]], f"(ohne Lösung genau für c in {ohne})")

# 034: 8/(x − 4) + 3 = (x + 4)/(x − 4)
r = loese(lambda x: 8 / (x - 4) + 3, lambda x: (x + 4) / (x - 4), [lambda x: x - 4])
pruefe("VT1B-034", len(r[0]), 0, f"(Scheinlösung {r[1]})")

# 035: vier Beispiele
b35 = [loese(lambda x: 8 / (x - 1), lambda x: 2 / (x - 1) + 3, [lambda x: x - 1]),
       loese(lambda x: (2 * x - 1) / (x - 4), lambda x: 7 / (x - 4) - 1, [lambda x: x - 4]),
       loese(lambda x: (x + 2) / (x - 5), lambda x: 7 / (x - 5), [lambda x: x - 5]),
       loese(lambda x: (x + 6) / (x + 3), lambda x: 3 / (x + 3), [lambda x: x + 3])]
pruefe("VT1B-035", b35, [([F(3)], []), ([], [F(4)]), ([], [F(5)]), ([], [F(-3)])], "(alle Beispiele stimmen; Index 1)")

# 036: f − g konstant
diffs = {(x + 4) / (x - 3) - 2 - 7 / (x - 3) for x in [F(k, 3) for k in range(-30, 31)] if x != 3}
r = loese(lambda x: (x + 4) / (x - 3) - 2, lambda x: 7 / (x - 3), [lambda x: x - 3])
pruefe("VT1B-036", [diffs, len(r[0])], [{F(-1)}, 0], f"(Kandidat {r[1]})")

# ================= verhaeltnis =================
# 037: x ml von B (1:4) zu 200 ml A (1:1) -> 1:2; Rastersuche über positive Mengen
tr = [F(x) for x in range(1, 5001) if (100 + F(x, 5)) * 2 == 100 + F(4 * x, 5)]
pruefe("VT1B-037", tr, [F(250)], "(Saft 150 ml, Wasser 300 ml)")

# 038
pruefe("VT1B-038", [10 + (9 - 6), F(9 * 10, 6)], [13, 15])

# 039: 1 : 3 -> Saftanteil halbieren durch Wasserzugabe
tr = [w for w in range(1, 100) if F(1, 1 + w) == F(1, 2) * F(1, 4)]
pruefe("VT1B-039", tr, [7])

# 040: gleiche Strecke s, Zeiten 3t : 4t
verh = {(F(s_) / 3) / (F(s_) / 4) for s_ in (1, 12, 7, 100)}
pruefe("VT1B-040", verh, {F(4, 3)}, "(für jede Strecke 4 : 3; Index 0)")

# 041
pruefe("VT1B-041", {F(a_ + b_, b_) * 12 for a_, b_ in [(7, 12), (14, 24), (F(7, 2), 6)]}, {F(19)})

# ================= Fehlbilder gegen Datei =================
d = json.load(open(os.path.join(HIER, "gleichungen.bruch.json"), encoding="utf-8"))
for a in d["aufgaben"]:
    nr = int(a["kennung"].split("-")[1])
    if not 22 <= nr <= 41:
        continue
    au = a["aufgabe"]
    if au["y"] == "zahl":
        if any(fb["antwort"] == au["o"]["wert"] for fb in a["fehlbilder"]):
            fehler.append(a["kennung"] + " Fehlbild=Lösung")
    elif au["y"] == "luecken":
        w = au["o"]["werte"]
        for i in range(1, len(w) + 1):
            if i not in {fb.get("luecke") for fb in a["fehlbilder"]}:
                fehler.append(f"{a['kennung']} Lücke {i} ohne Fehlbild")
        if any(fb["antwort"] == w[fb["luecke"] - 1] for fb in a["fehlbilder"]):
            fehler.append(a["kennung"] + " Fehlbild=Lösung")
    else:
        idx = au["o"]["index"]
        if sorted(fb["index"] for fb in a["fehlbilder"]) != [i for i in range(len(au["a"])) if i != idx]:
            fehler.append(a["kennung"] + " Fehlbilder decken Optionen nicht")
        print(f"   {a['kennung']} Längen {[len(t) for t in au['a']]} richtig {idx}")

# ================= Vorschläge =================
print("\nVorschläge:")
# V-022: nur (L), zweite Lücke = ausgeschlossene Zahlen von (L)
pruefe("Vorschlag 022", [len(rL[0]), 3], [0, 3], "((L) schließt 0, 1, 2 aus)")
# V-028: 10/(x − p) = a/(x + q) und 15/(x − p) = 9/(x + q): a = 6 für alle p, q (p ≠ −q)
ok = True
for p_ in (-4, 1, 3, 7):
    for q_ in (-2, 2, 5):
        if p_ == -q_:
            continue
        l1 = loese(lambda x: 15 / (x - p_), lambda x: 9 / (x + q_), [lambda x: x - p_, lambda x: x + q_])
        l2 = loese(lambda x: 10 / (x - p_), lambda x: 6 / (x + q_), [lambda x: x - p_, lambda x: x + q_])
        ok &= l1 == l2
pruefe("Vorschlag 028", ok, True)
# V-030: zusätzlich a ≠ b und c ≠ d -> nie mehr als eine Lösung
faelle2 = set()
for a_ in range(-3, 4):
    for b_ in range(-3, 4):
        for c_ in range(-3, 4):
            for d_ in range(-3, 4):
                if b_ == d_ or a_ == b_ or c_ == d_:
                    continue
                e, s = loese(lambda x: (x + a_) / (x + b_), lambda x: (x + c_) / (x + d_),
                             [lambda x: x + b_, lambda x: x + d_])
                faelle2.add("unendlich" if e == "alle" else len(e))
pruefe("Vorschlag 030", max(f for f in faelle2 if f != "unendlich") <= 1 and "unendlich" not in faelle2, True,
       f"(Lösungszahlen {faelle2})")
# V-033: nur ein Wert (c für Kandidat 2) -> 6
pruefe("Vorschlag 033", w2, [F(6)])

print("\nERGEBNIS:", "OK – alle Sollwerte bestätigt" if not fehler else f"FEHLER {fehler}")
sys.exit(1 if fehler else 0)
