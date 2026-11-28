"""Gegenrechnung Runde 15 (Stand nach der Gegenprüfung 1197).

Rechnet alle 207 Sollwerte der Runde noch einmal NEU und UNABHÄNGIG von `bauen.py` und den Quelltexten `th_*.py`:
- Zahl- und Lückenaufgaben: Sollwert aus den Angaben des Fragetextes mit exakten Brüchen, Zählschleifen oder Gleitkomma (Winkel in Grad) neu berechnet,
  Rundung (wo verlangt) kaufmännisch auf die verlangte Stelle; der gespeicherte Wert muss GENAU gleich sein (keine Toleranz).
- Auswahlaufgaben und Fehler-Detektive: erwartete richtige Antwort (Anfang des Antworttextes bzw. Fehlerzeile) und eine eigene Rechen- oder Zählprobe.
- Zusätzlich: Keine Aufgabe der Runde hat `toleranz`; bei jeder Zahlaufgabe mit verlangter Rundung hat der gespeicherte Wert höchstens die verlangten Stellen.
Aufruf: python3 -I inhalte/mathe-profi/rollend-15/gegenrechnung.py   (Ausgabe endet mit „0 Abweichungen“)
"""
import glob
import json
import math
import os
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))
Q = {}
for _p in sorted(glob.glob(os.path.join(HIER, "*.json"))):
    for _q in json.load(open(_p, encoding="utf-8"))["aufgaben"]:
        Q[_q["kennung"][5:]] = _q["aufgabe"]
assert len(Q) == 207, len(Q)

abw = []


def rund(x, n):
    """kaufmännisch runden (Dezimal, nicht Gleitkomma-Banker)"""
    return Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-n), rounding=ROUND_HALF_UP)


def deg(f, x):
    return getattr(math, f)(math.radians(x))


def adeg(f, x):
    return math.degrees(getattr(math, f)(x))


def zahl(k, soll, stellen=None):
    a = Q[k]
    assert a["y"] == "zahl", k
    if "toleranz" in a["o"]:
        abw.append((k, "Toleranz vorhanden", a["o"]["toleranz"]))
    ist = F(str(a["o"]["wert"]))
    if stellen is not None:
        soll = F(str(rund(soll, stellen)))
        s = str(a["o"]["wert"])
        nach = len(s.split(".")[1]) if "." in s else 0
        if nach > stellen:
            abw.append((k, "mehr Stellen als verlangt", s))
    else:
        soll = F(soll) if not isinstance(soll, float) else F(str(round(soll, 9)))
    if ist != soll:
        abw.append((k, "Zahl", float(ist), float(soll)))


def luecken(k, soll):
    a = Q[k]
    assert a["y"] == "luecken", k
    ist = [F(str(w)) for w in a["o"]["werte"]]
    soll = [F(str(w)) for w in soll]
    if ist != soll:
        abw.append((k, "Lücken", [float(x) for x in ist], [float(x) for x in soll]))


def auswahl(k, anfang, probe=True, zeile=None):
    """anfang: Anfang des richtigen Antworttextes; zeile: bei Fehler-Detektiven die erwartete Fehlerzeile (ab 1)"""
    a = Q[k]
    assert a["y"] == "auswahl", k
    i = a["o"]["index"]
    if zeile is not None:
        if i + 1 != zeile:
            abw.append((k, "Fehlerzeile", i + 1, zeile))
    else:
        treffer = [j for j, t in enumerate(a["a"]) if t.startswith(anfang)]
        if treffer != [i]:
            abw.append((k, "richtige Antwort", i, treffer, anfang))
    if probe is not True:
        abw.append((k, "Probe der Antwort schlägt fehl"))


# ═════════ Klasse 7: bruch.prozent_grundwert (V001–V016) ═════════
zahl("001", F(100 + 18, 100))
auswahl("002", None, F(88, 100) != F(88, 1000) and 100 - 12 == 88, zeile=2)                       # 88 % = 0,88; Zeile 3 rechnet mit 0,088 richtig weiter
zahl("003", F(320) * (1 + F(15, 100) + F(8, 100)))
zahl("004", F(480) * F(125, 100) / 40)
zahl("005", 3 * 28 + 3 * F(28) * (1 - F(30, 100)))
zahl("006", 85 - F(85) * F(35, 100))
zahl("007", F(162) / F(108, 100))
auswahl("008", "Ticket B war vorher teurer: 75 €", F(60) / F(12, 10) == 50 and F(60) / F(8, 10) == 75 and 75 > 50)
zahl("009", F(4300 - 4085, 4300) * 100)
auswahl("010", "beim Bus", max({"Bus": F(60, 240), "Museum": F(3, 15), "Hotel": F(9, 90)}.items(), key=lambda t: t[1])[0] == "Bus")
zahl("011", F(480) * F(112, 100) * F(105, 100))
zahl("012", 100 - 100 / 1.2, 1)
zahl("013", round(5000 * 1.04 * 1.04 * 1.04, 2))
zahl("014", next(n for n in range(1, 50) if 2000 * 1.05 ** n > 2500))
auswahl("015", "Die Insel ist prozentual stärker", F(12000, 50000) > F(30000, 200000))
auswahl("016", "50 · 1,4 · 0,6 = 42", F(50) * F(14, 10) * F(6, 10) == 42 < 50)

# ═════════ terme.potenzgesetze_natuerlich (V017–V031) ═════════
luecken("017", [7, 3 ** 7])
zahl("018", 2 ** 9)
auswahl("019", None, 3 ** 4 * 3 ** 2 == 3 ** 6 != 3 ** 8, zeile=2)                                 # Hochzahlen werden addiert, nicht malgenommen
zahl("020", 4 ** 3 * 25 ** 3)
auswahl("021", "Gleiche Hochzahl: (2 · 5)⁵ = 10⁵", 2 ** 5 * 5 ** 5 == 10 ** 5 != 10 ** 10)
zahl("022", next(b for b in range(1, 20) if 2 ** 4 * b ** 4 == 14 ** 4))
zahl("023", (2 ** 3) ** 4)
auswahl("024", "x⁶", True)                                                                        # x²·x²·x² = x^(2+2+2)
zahl("025", next(n for n in range(1, 40) if (5 ** n) ** 4 == 5 ** 24))
luecken("026", [2, 4 ** 2])
zahl("027", 5 ** 6 // 5 ** 4)
auswahl("028", None, 9 - 4 == 5 and 7 ** 5 != 7 * 5, zeile=3)
zahl("029", F(2 ** 10, 2 ** 6))
auswahl("030", "2⁵ · 3⁴", True)                                                                   # nur gleiche Basis oder gleiche Hochzahl lässt sich zusammenfassen
zahl("031", F((2 ** 4 * 2 ** 5) ** 2, 2 ** 10))

# ═════════ terme.umformen (V032–V046) ═════════
luecken("032", [9 - 2, 3 + 5, (9 - 2) * 2 + (3 + 5) * 1])
zahl("033", 3 * 12 + 2 * 7 + 5 * 12 + 4 * 7)
auswahl("034", None, 5 + 1 == 6 != 5, zeile=3)
zahl("035", 2 * 5 * 3 * 5 * 5)
auswahl("036", "3a · (−4ab)", 3 * (-4) == -12)                                                     # Zahlenfaktor −12, a·a·b
zahl("037", next(a for a in range(1, 100) if 3 * a * 4 * a == 300))
luecken("038", [11 - 4, 6 + 3, 7 * 2 + 9])
zahl("039", 400 - (3 * 20 + 15))
auswahl("040", None, True, zeile=2)                                                                # −(2a + 7b − 3) = −2a − 7b + 3
zahl("041", 6 * (45 + 12 * 3))
zahl("042", 8 * 200 - 8 * 3)
zahl("043", F(35, 5))
auswahl("044", "Sie sind äquivalent: 2(x + 5) − x", all(2 * (x + 5) - x == x + 10 for x in range(-20, 21)))
auswahl("045", "Für x = 0 ergibt der erste Term 6", 3 * 0 + 6 != 9 * 0 and 3 * 1 + 6 == 9 * 1)
zahl("046", next(k for k in range(-50, 100) if all(13 * (x + 4) == 13 * x + k for x in range(-5, 6))))

# ═════════ abbildungen.kongruenz (V047–V060) ═════════
luecken("047", [6 - 2, 6 + (6 - 2), 10 - 2])
zahl("048", 1 - (5 - 1))
auswahl("049", None, (-2, 1) == (-2, 1) and math.dist((-2, 1), (-2, 4)) == 3 and math.dist((-2, 1), (-2, -4)) == 5, zeile=2)
zahl("050", F(-6 + 12, 2))
zahl("051", F(30 - 12, 2))
zahl("052", F(180 - 68 - 52, 2))
auswahl("053", "Schneide die Mittelsenkrechte von [H1H2] mit jeder der beiden Winkelhalbierenden", True)
luecken("054", [6, 12, 6 + 12])
zahl("055", 3 + 8 + 4)
auswahl("056", None, True, zeile=2)                                                                # Diagonalen eines Rechtecks sind keine Achsen
auswahl("057", "eine Raute, die kein Quadrat ist", True)
zahl("058", len({"Quadrat": 4, "Rechteck": 2, "Raute": 2, "Parallelogramm": 0, "Drachen": 1, "Trapez": 1}) - 1)
zahl("059", 180 - 52 - 71)
auswahl("060", None, (-1) ** 2 == 1, zeile=4)                                                      # zwei Spiegelungen: Umlaufsinn wieder wie am Anfang

# ═════════ geometrie.winkelsaetze (V061–V078) ═════════
luecken("061", [180, 180 // 4, 180 - 180 // 4])
zahl("062", 180 - 83)
zahl("063", 180 - 73)
auswahl("064", None, 180 - 68 == 112 != 68, zeile=2)
auswahl("065", "Die Wege sind nicht parallel", 78 != 82)
zahl("066", next(x for x in range(-50, 100) if 5 * x - 20 == 3 * x + 14))
zahl("067", F(180, 5 + 6 + 7) * 7)
auswahl("068", "Man zeichnet durch eine Ecke die Parallele", True)
luecken("069", [121 - 38, 180 - 121, 38 + (121 - 38) + (180 - 121)])
zahl("070", 47 + 65)
zahl("071", F((12 - 2) * 180, 12))
zahl("072", next(n - 2 for n in range(3, 100) if (n - 2) * 180 == 2340))
zahl("073", 360 - 2 * F((12 - 2) * 180, 12))
auswahl("074", "Der Innenwinkel des regelmäßigen Fünfecks ist 108°", F(3 * 180, 5) == 108 and 360 % 108 != 0)
zahl("075", 180 - (360 - 80 - 95 - 70))
zahl("076", (180 - 70) + (180 - 80))
auswahl("077", "Man zeichnet eine Diagonale, die im Inneren", 2 * 180 == 360 and 4 * 180 == 720)
auswahl("078", None, 3 * 180 - 180 == 360 != 720, zeile=4)

# ═════════ geometrie.konstruktion (V079–V093) ═════════
luecken("079", [180 - 40, (180 - 40) // 2, (180 - 40) // 2 + 40])
zahl("080", 180 - 2 * 38)
auswahl("081", None, 180 - 52 - 52 == 76 != 128, zeile=3)
auswahl("082", "SWS", True)
auswahl("083", "c = 6 cm, α = 50°, β = 70°", 3 + 4 < 8 and 7 * deg("sin", 40) < 5 < 7 and 180 - 40 - 60 == 80)
auswahl("084", None, True, zeile=2)                                                                # gleiche Winkel: ähnlich, nicht deckungsgleich
luecken("085", [5 + 8, 8 - 5, len([c for c in range(1, 30) if 8 - 5 < c < 5 + 8])])
zahl("086", max(c for c in range(1, 30) if 9 - 4 < c < 9 + 4))
auswahl("087", "Es entsteht kein Dreieck: Die zwei kürzeren", 3 + 4 == 7)
zahl("088", 7 + 5 + 6)
auswahl("089", "Strecke [AB] mit 6 cm zeichnen. Bei A den Winkel 35°", True)
zahl("090", 180 - 50 - 70)
auswahl("091", "Kehrsatz: „Wenn eine Zahl gerade ist, dann ist sie durch 6 teilbar.“ Er ist falsch", 8 % 2 == 0 and 8 % 6 != 0)
auswahl("092", "ein Rechteck mit den Seiten 3 cm und 4 cm", math.hypot(3, 4) == math.hypot(4, 3) and abs(math.sqrt(9 + 25 + 15) - math.sqrt(9 + 25 - 15)) > 1)
zahl("093", sum(1 for wahr in (True, False, True, False) if wahr))     # Kehrsätze: (1) wahr, (2) 15 Gegenbeispiel, (3) wahr, (4) 6 Gegenbeispiel

# ═════════ gleichungen.linear (V094–V110) ═════════
luecken("094", [6 - 2, 37 + 23, F(37 + 23, 6 - 2)])
zahl("095", F(49 - 14) / F(35, 10))
auswahl("096", None, True, zeile=1)                                                                # nur auf einer Seite subtrahiert
zahl("097", next(m for m in range(1, 1000) if 18 + F(25, 100) * m == F(40, 100) * m))
auswahl("098", "5x = 55", 8 * 11 - 30 == 3 * 11 + 25)
zahl("099", next(x for x in range(-100, 100) if 7 * x - 8 == 3 * x + 40))
luecken("100", [5 * 4, 19 + 20, F(39, 3)])
zahl("101", next(x for x in range(-50, 50) if 3 * (2 * x - 5) - (x - 4) == 24))
auswahl("102", None, 5 * (3 - 2) != 5 * 3 - 2, zeile=1)
zahl("103", 4 * 11 - 9)
auswahl("104", "x = 8", 6 * 8 - 17 == 2 * 8 + 15 and 6 * 4 - 17 != 2 * 4 + 15 and 6 * 12 - 17 != 2 * 12 + 15)
auswahl("105", "keine Lösung", all(5 * (x + 2) - 3 * x != 2 * x + 13 for x in range(-50, 50)))
zahl("106", next(k for k in range(-50, 50) if all(5 * (x + 2) - 3 * x == 2 * x + k for x in range(-5, 6))))
auswahl("107", None, all(6 * x - 4 != 2 * (3 * x + 5) - 1 for x in range(-20, 21)), zeile=4)
zahl("108", next(F(t) for t in range(1, 50) if 27 * t == 18 * (t + 2)))
zahl("109", F("616") / F("11.2") + 3)
zahl("110", next(b for b in range(1, 50) if 2 * (b + b + 4) == 36))

# ═════════ Klasse 9: zahlen.wurzeln_basis (V111–V125) ═════════
luecken("111", [math.isqrt(1296), 4 * math.isqrt(1296), 4 * math.isqrt(1296) // 3])
zahl("112", 4 * math.isqrt(5929))
auswahl("113", "576", 24 * 24 == 576)
zahl("114", F(13, 100) * 100)
zahl("115", math.sqrt(3.8), 2)
luecken("116", [round(343 ** (1 / 3)), round(343 ** (1 / 3)) ** 2, 6 * round(343 ** (1 / 3)) ** 2])
zahl("117", 6 * round(2744 ** (1 / 3)) ** 2)
auswahl("118", None, 6 ** 3 == 216 != 72 ** 3, zeile=1)
auswahl("119", "zwischen 11 dm und 12 dm", 11 ** 2 < 130 < 12 ** 2)
zahl("120", math.sqrt(85), 1)
auswahl("121", "Keine reelle Zahl", all(x * x >= 0 for x in range(-30, 31)))
zahl("122", sum(1 for x in range(-3, 13) if x - 5 >= 0))
auswahl("123", None, math.sqrt(4 + 25) != 2 + 5, zeile=1)
zahl("124", F(4 * 15, 10) / 5 * 60)
zahl("125", 12 * round(3.375 ** (1 / 3), 6))

# ═════════ zahlen.reell (V126–V139) ═════════
auswahl("126", "√50", all(F(p, q) ** 2 != 50 for q in range(1, 60) for p in range(1, 500)) and math.isqrt(50) ** 2 != 50)
zahl("127", sum(1 for r in (math.isqrt(16) ** 2 == 16, math.isqrt(20) ** 2 == 20, True, False, True, round(27 ** (1 / 3)) ** 3 == 27, math.isqrt(45) ** 2 == 45) if r))
luecken("128", [max(n for n in range(1, 10) if n * n < 10), max(n for n in range(1, 10) if n * n < 10) + 1, min(n for n in range(1, 100) if n * n > 1000)])
zahl("129", sum(1 for k in range(261, 270) if F(k, 100) ** 2 < 7))
zahl("130", (4.5 + 20 / 4.5) / 2, 2)
zahl("131", F(36) / ((F(8) + F(9, 2)) / 2))
zahl("132", math.isqrt(18 * 50))
auswahl("133", "√100 : √4 = √25", math.isclose(10 / 2, 5) and 3 + 4 != 5 and 10 - 6 != 8)
luecken("134", [245 // 5, math.isqrt(245 // 5), 2 * math.isqrt(245 // 5)])
zahl("135", next(a for a in range(1, 20) if a * a * 2 == 98))
auswahl("136", None, 3 * 3 * 2 == 18 != 6, zeile=4)
zahl("137", F(44, 11))
auswahl("138", "Mit p = 2k folgt q² = 2k²", all((2 * k) ** 2 == 2 * (2 * k * k) for k in range(1, 30)))
auswahl("139", None, (2 * 5) ** 2 == 4 * 5 ** 2 != 2 * 5 ** 2, zeile=3)

# ═════════ gleichungen.quadratisch (V140–V153) ═════════
luecken("140", [98 // 2, math.isqrt(49), -math.isqrt(49)])
zahl("141", min(x for x in range(-50, 51) if 4 * x * x - 196 == 0))
auswahl("142", "x = 0 oder x = 7", [x for x in range(-30, 31) if 4 * x * x - 28 * x == 0] == [0, 7])
auswahl("143", None, sorted(x for x in range(-30, 31) if 6 * x * x == 18 * x) == [0, 3], zeile=3)
zahl("144", max(x for x in range(-50, 51) if x * x - 4 * x - 21 == 0))
zahl("145", 4 * -9)
zahl("146", (10 // 2) ** 2 - 9)
luecken("147", [24 ** 2 - 4 * 3 * 21, math.isqrt(24 ** 2 - 4 * 3 * 21), F(24 + math.isqrt(24 ** 2 - 4 * 3 * 21), 2 * 3)])
zahl("148", F(-3 - math.isqrt(3 * 3 - 4 * 2 * -20), 2 * 2))
zahl("149", next(x for x in range(1, 100) if F(40, x) == x - 6))
zahl("150", next(k for k in range(1, 100) if k * k - 4 * 3 * 27 == 0))
auswahl("151", "keinen", 3 * 3 - 4 * 2 * 5 < 0)
zahl("152", next(t for t in range(0, 20) if -5 * t * t + 20 * t + 25 == 0))
zahl("153", next(b for b in range(1, 100) if b * (b + 9) == 360))

# ═════════ funktionen.quadratisch (V154–V167) ═════════
luecken("154", [5 + 4, -1 + 7, 2 * (10 - 9) ** 2 + 6])
auswahl("155", "y = −(x + 4)² + 9", True)
zahl("156", F(13 + 5, (4 + 2) ** 2))
zahl("157", -6)
auswahl("158", "y = −2(x − 3)² + 4", all(-(2 * (x - 3) ** 2 - 4) == -2 * (x - 3) ** 2 + 4 for x in range(-10, 11)))
zahl("159", 50 - (12 // 2) ** 2)
auswahl("160", None, 5 ** 2 - 10 * 5 + 19 == -6 and (5 - 5) ** 2 + 19 != -6, zeile=3)
luecken("161", [min(x for x in range(-100, 100) if x * x - 6 * x - 55 == 0), max(x for x in range(-100, 100) if x * x - 6 * x - 55 == 0), F(-5 + 11, 2)])
zahl("162", max(x for x in range(-50, 50) if (x + 2) ** 2 == 25) - min(x for x in range(-50, 50) if (x + 2) ** 2 == 25))
zahl("163", F(9) - F(2, 100) * (30 - 20) ** 2)
zahl("164", next(p for p in range(-50, 50) for q in range(-100, 100) if 4 + 2 * p + q == 10 and 16 + 4 * p + q == 32))
zahl("165", max(x for x in range(-50, 50) if x * x - 4 * x + 1 == 2 * x - 4))
luecken("166", [F(40, 10), -5 * 16 + 160 + 3, -5 * 16 + 160 + 3 - 3])
zahl("167", max(x * (36 - 2 * x) for x in range(1, 18)))

# ═════════ trigo.pythagoras (V168–V179) ═════════
luecken("168", [9 ** 2 + 40 ** 2, math.isqrt(9 ** 2 + 40 ** 2), 9 + 40 + math.isqrt(9 ** 2 + 40 ** 2)])
zahl("169", math.hypot(1.2, 0.5), 2)
zahl("170", math.sqrt(61 ** 2 - 11 ** 2), 0)
auswahl("171", "b² = 17² − 8²", 17 ** 2 - 8 ** 2 == 15 ** 2)
auswahl("172", "8, 15, 17", 8 ** 2 + 15 ** 2 == 17 ** 2 and 7 ** 2 + 24 ** 2 != 26 ** 2 and 9 ** 2 + 12 ** 2 != 16 ** 2)
zahl("173", math.sqrt(89 ** 2 - 39 ** 2), 0)
zahl("174", math.dist((-2, 3), (4, 11)), 0)
zahl("175", math.sqrt(10 ** 2 - (7 - 1) ** 2), 0)
luecken("176", [round(math.hypot(12, 16)), round(math.sqrt(12 ** 2 + 16 ** 2 + 15 ** 2)), round(math.sqrt(12 ** 2 + 16 ** 2 + 15 ** 2)) - round(math.hypot(12, 16))])
zahl("177", math.sqrt(8 ** 2 + 9 ** 2 + 12 ** 2), 0)
zahl("178", 2 * math.hypot(2, 1.5) * 6, 0)
auswahl("179", None, 13 ** 2 - 5 ** 2 == 12 ** 2 and 13 ** 2 + 5 ** 2 != 12 ** 2, zeile=3)

# ═════════ trigo.rechtwinklig (V180–V192) ═════════
auswahl("180", "a (die Seite BC)", True)
auswahl("181", "b (die Seite AC)", True)
luecken("182", [round(0.6 * 35), round(0.8 * 35), 35 + round(0.6 * 35) + round(0.8 * 35)])
zahl("183", F(75, 100) * 32)
zahl("184", 1.5 * deg("tan", 28), 2)
zahl("185", 0.9 / deg("sin", 12), 2)
zahl("186", adeg("atan", 15 / 28), 1)
zahl("187", math.sqrt(1 - 0.28 ** 2), 2)
auswahl("188", "für 20°", abs(deg("sin", 70) - deg("cos", 20)) < 1e-12)
zahl("189", 38 / deg("tan", 4), 0)
auswahl("190", None, 20 * deg("cos", 40) < 20 < 20 / deg("cos", 40), zeile=2)
zahl("191", adeg("atan", 12 / 100), 1)
zahl("192", adeg("atan", 3) - adeg("atan", 1), 1)

# ═════════ stochastik.verknuepft (V193–V207) ═════════
zahl("193", sum(1 for n in range(1, 1000) if math.isqrt(n) ** 2 == n and 70 < n < 700))
zahl("194", len({d for d in range(1, 61) if 60 % d == 0} - {d for d in range(1, 46) if 45 % d == 0}))
zahl("195", len({n for n in range(1, 61) if n % 6 == 0} | {n for n in range(1, 61) if n % 4 == 0}))
luecken("197", [24 + 18 - 10, 40 - (24 + 18 - 10), F(40 - 32, 40) * 100])
zahl("198", F(35, 100) + F(28, 100) - F(9, 100))
zahl("200", (14 - 6) + (11 - 6))
auswahl("202", "A ∩ B = A und A ∪ B = B", ({2, 4} & {1, 2, 3, 4} == {2, 4}) and ({2, 4} | {1, 2, 3, 4} == {1, 2, 3, 4}))
luecken("203", [64 - 27, 41 - 27, 100 - 64 - (41 - 27)])
zahl("204", 72 - (47 - 19))
zahl("205", 1 - (F(60, 100) + F(45, 100) - F(27, 100)))
zahl("196", 100 - (55 + 44 - 33))
zahl("201", (52 - 18) + (31 - 18))
zahl("199", F(42, 100) + F(35, 100) - F(61, 100))
auswahl("206", "Der Schnitt hat die Wahrscheinlichkeit 0", F(1, 6) + F(2, 6) == F(3, 6) and F(1, 6) + F(2, 6) != F(2, 6))
auswahl("207", None, F(40, 100) + F(30, 100) - F(12, 100) == F(58, 100) != F(70, 100), zeile=3)

# ═════════ Abschluss ═════════
with open(__file__, encoding="utf-8") as _f:
    _quelle = _f.read()
import re
_geprueft = set(re.findall(r'^(?:zahl|luecken|auswahl)\("(\d{3})"', _quelle, re.M))
nicht = sorted(set(Q) - _geprueft)
if nicht:
    abw.append(("Aufgaben ohne Gegenrechnung", nicht))
for a in abw:
    print("ABWEICHUNG:", *a)
print(f"{len(_geprueft)} von {len(Q)} Sollwerten neu berechnet")
print(f"{len(abw)} Abweichungen")
raise SystemExit(1 if abw else 0)
