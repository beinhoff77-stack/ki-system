"""Gegenrechnung Runde VT1A (Verstehen in Tests, Klasse 5).

Rechnet alle 77 Sollantworten NEU und UNABHÄNGIG von `bauen.py`, `kern.py` und den Quelltexten `th_*.py`:
- Zahlaufgaben: Sollwert aus den Angaben des Fragetextes mit Zählschleifen und Probierverfahren (nicht mit der Formel des Quelltextes) neu bestimmt;
  der gespeicherte Wert muss GENAU gleich sein (keine Toleranz in keiner Aufgabe).
- Auswahlaufgaben: erwartete richtige Antwort (Anfang des Antworttextes) und eine eigene Rechen- oder Zählprobe; ausgewählte falsche
  Möglichkeiten werden zusätzlich auf ihre Fehlerbeschreibung hin nachgerechnet, wo sie eine Rechnung enthalten.
Aufruf: python3 -I inhalte/mathe-profi/vtest-1a/gegenrechnung.py   (Ausgabe endet mit „0 Abweichungen“)
"""
import glob
import json
import os
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))
Q = {}
for _p in sorted(glob.glob(os.path.join(HIER, "*.json"))):
    for _q in json.load(open(_p, encoding="utf-8"))["aufgaben"]:
        Q[_q["kennung"][5:]] = _q["aufgabe"]
assert len(Q) == 77, len(Q)
abw = []
gesehen = set()


def zahl(k, soll):
    a = Q[k]
    gesehen.add(k)
    assert a["y"] == "zahl", k
    if "toleranz" in a["o"]:
        abw.append((k, "Toleranz vorhanden"))
    if F(str(a["o"]["wert"])) != F(soll):
        abw.append((k, "Zahl", a["o"]["wert"], soll))


def wahl(k, anfang, probe=True):
    a = Q[k]
    gesehen.add(k)
    assert a["y"] == "auswahl", k
    if not a["a"][a["o"]["index"]].startswith(anfang):
        abw.append((k, "Antwort", a["a"][a["o"]["index"]][:60], anfang))
    if probe is not True:
        abw.append((k, "Probe", probe))
    if len(set(a["a"])) != len(a["a"]) or len(a["a"]) < 4:
        abw.append((k, "Möglichkeiten"))


def erste(f, bis=100000, ab=0):
    return next(n for n in range(ab, bis) if f(n))


# ═════════ zahlen.potenzen_basis ═════════
# schreibweise
wahl("001", "Falsch. 3² = 9 und 2³ = 8", 3 ** 2 + 2 ** 3 == 17 and 5 ** 5 == 3125 and 3 * 2 + 2 * 3 == 12)
wahl("002", "Der Wert verdoppelt sich", 2 ** 7 == 128 == 2 * 64 and 2 ** 6 == 64)
g = 1                                                               # Verdopplung je Generation: 2, 4, 8, 16 Personen
for _ in range(4):
    g *= 2
zahl("003", g)
zahl("004", erste(lambda n: 6 ** n == 216, 20))
wahl("005", "Die 4 steht 6-mal", 4 ** 6 == 4096 and 4 * 6 == 24 and 6 ** 4 == 1296)
wahl("006", "Das ist bei diesen Zahlen so", 2 ** 4 == 16 == 4 ** 2 and 2 ** 3 == 8 and 3 ** 2 == 9)
wahl("007", "Fehler: Die Hochzahl 2 gehört nur zur 3", 2 * 3 * 3 == 18 and 6 * 6 == 36)
# quadrat
zahl("008", (lambda a: (next(s for s in range(1, 500) if 4 * s == 2 * 4 * a)) ** 2)(next(t for t in range(1, 200) if t * t == 144)))
wahl("009", "Zwischen 144 = 12 · 12 und 169", [n for n in range(1, 30) if n * n < 150 < (n + 1) * (n + 1)] == [12])
zahl("010", 11 * 11 - 7 * 7)
wahl("011", "(3 + 4) · (3 + 4) = 49", (3 + 4) * (3 + 4) == 49 and 3 * 3 + 4 * 4 == 25)
zahl("012", erste(lambda n: n * n - (n - 1) * (n - 1) == 27, 100))
wahl("013", "Fehler: (3 + 4)² ist 7²", 7 * 7 == 49 and 9 + 16 == 25)
wahl("014", "Die große Platte hat 4-mal", 10 * 10 == 4 * 5 * 5)
# zehner
wahl("015", "10⁶ ist größer", 10 ** 6 > 9 * 10 ** 5)
wahl("016", "56 · 10⁵", [x for x in (56 * 10 ** 6, 560 * 10 ** 5, 5600 * 10 ** 4, 56 * 10 ** 5) if x != 56000000] == [5600000])
zahl("017", len(str(500 * 1000 // 5)) - 1)                         # 100 000 Münzen = 10⁵
wahl("018", "Beide: 45 · 100 000", 45 * 100000 == 4500000 == 450 * 10000)
zahl("019", erste(lambda d: d * 10 * 100 == 10 ** 6, 10 ** 6))
wahl("020", "Fehler: Er hat die Hochzahlen addiert", 1000 + 1000 == 2000 and 1000 * 1000 == 10 ** 6)
zahl("021", max(n for n in range(0, 20) if 10 ** n < 5000000))
# sach
zahl("022", erste(lambda a: a * 3 * 3 * 3 * 3 == 405, 405))
zahl("023", erste(lambda n: 2 ** n == 64, 30))
zahl("024", erste(lambda n: 10 ** n == 10000, 30))
wahl("025", "3 · 2⁵", 3 * 2 * 2 * 2 * 2 * 2 == 96)
wahl("026", "4⁵", [4, 16, 64, 256, 1024][4] == 4 ** 5 and 4 * 4 * 4 == 64)
b, t = 1, 0
while not (b > 100 + 100 * t):
    t += 1
    b = 2 ** t
zahl("027", t)
wahl("028", "Fehler: Sie hat 2 und 3 zu 6", 2 * 3 ** 4 == 162 and 6 ** 4 == 1296)

# ═════════ zahlen.rechengesetze ═════════
# klammern
wahl("029", "(20 − 4) · 3 + 2", (20 - 4) * 3 + 2 == 50 and 20 - (4 * 3 + 2) != 50 and 20 - 4 * (3 + 2) != 50 and (20 - 4) * (3 + 2) != 50)
zahl("030", erste(lambda x: (x + 4) * 3 - 5 == 25, 100))
wahl("031", "Addiere 12 und 8, teile die Summe durch 4", 40 - (12 + 8) // 4 == 35)
wahl("032", "(9 + 3) : 4 · 2", (9 + 3) / 4 * 2 == 6)
wahl("033", "(30 − 12) − 4", (30 - 12) - 4 == 30 - 12 - 4)
wahl("034", "3 + 4 · 5 = 23", [(a, b) for a in "+-*" for b in "+-*" if eval("3" + a + "4" + b + "5") == 23] == [("+", "*")])
wahl("035", "Fehler: Er hat die Klammer nicht zuerst", 100 - 20 * 4 == 20)
# termaufbau
wahl("036", "Genau ① und ②", 30 - 6 - 4 == 20 and 30 - (6 + 4) == 20 and 30 - 6 + 4 == 28 and 30 - (6 - 4) == 28)
wahl("037", "(3 + 4) · 5", (3 + 4) * 5 == 35 and 3 + 4 * 5 == 23)
wahl("038", "40 − (9 + 6) = 25", 40 - 15 == 25)
wahl("039", "20 − (4 · 3 + 2 · 2)", 20 - (12 + 4) == 4)
zahl("040", erste(lambda n: 4 + 2 * (n - 1) == 14, 100, 1))
zahl("041", erste(lambda x: 8 + 5 * x == (8 + 5) * x, 100))
wahl("042", "Er wird um 4 kleiner", (12 * 9 + 8 * 11 - 20) // 4 - (12 * 9 + 8 * 11 - 36) // 4 == 4)
# vorteil
wahl("043", "85 − 38 + 53 = 85 + 53 − 38", 85 - 38 + 53 == 100 == 85 + 53 - 38)
wahl("044", "83 + 17 − 29", 83 - 29 + 17 == 71 == 83 + 17 - 29)
wahl("045", "Zuerst 25 · 4 = 100", 25 * 4 * 17 == 1700)
wahl("046", "Beide bekommen 3 700", 50 * 37 * 2 == 3700 == 50 * 2 * 37)
zahl("047", erste(lambda x: 4 * x * 25 == 700, 1000))
wahl("048", "Fehler: Nach 4 · 25 = 100 muss mal 18", 100 * 18 == 1800 == 4 * 18 * 25)
wahl("049", "Beide Werte sind gleich, denn 36 · 4", 36 * 25 * 4 == 3600 == 18 * 25 * 8)
# verteilen
wahl("050", "98 ist 2 weniger als 100", 7 * 98 == 686 == 7 * 100 - 14)
zahl("051", erste(lambda x: 17 * x + 17 * 14 == 17 * 50, 1000))
wahl("052", "9 · (6 + 4)", 9 * 10 == 90)
wahl("053", "Beide haben recht", 4 * 27 == 108 == 4 * 20 + 4 * 7 == 4 * 30 - 4 * 3)
wahl("054", "Sie verdoppelt sich", 16 * 30 + 16 * 2 == 2 * (8 * 30 + 8 * 2))
wahl("055", "Die 19 ausklammern", 19 * (36 + 64 - 50) == 950 == 19 * 36 + 19 * 64 - 19 * 50)
wahl("056", "Fehler: In der Klammer muss ein Plus", 15 * 7 + 15 * 9 == 240)
# umkehraufgabe_mal
zahl("057", erste(lambda x: (x * 5 + 12) / 4 == 8, 1000))
wahl("058", "36 : 9", 36 // 9 == 4 and 36 // 4 == 9)
zahl("059", max(a for a in range(1, 50) for b in range(1, 50) if a * b == 48 and a + b == 14))
wahl("060", "56 : x = 7", 7 * 8 == 56 and 56 // 8 == 7)
wahl("061", "48 Murmeln werden gleichmäßig", 48 // 8 == 6)
wahl("062", "Weil 50 nicht in der 7er-Reihe", 50 not in [7 * n for n in range(1, 30)] and 49 in [7 * n for n in range(1, 30)])
zahl("063", sum(1 for a in range(1, 13) if any(a * x == 36 for x in range(1, 40))))
# ueberschlag
wahl("064", "600 · 50 = 30 000", 612 * 49 == 29988)
zahl("065", max(n for n in range(1, 100) if (n // 10) * 10 + (10 if n % 10 >= 5 else 0) == 30))
wahl("066", "Der genaue Preis liegt unter 600 €", 3 * 198 == 594 < 600)
wahl("067", "Beide Überschläge sind brauchbar", abs(4800 + 3500 - (4812 + 3487)) < abs(5000 + 3000 - (4812 + 3487)))
wahl("068", "Der Überschlag reicht hier nicht", 23 * 48 == 1104 > 1000)
wahl("069", "Fehler: Mias Überschlag ist zu grob", 596 * 12 == 7152 and abs(600 * 12 - 7152) == 48)
zahl("070", min(n for n in range(0, 10000) if 100 * ((n + 50) // 100) == 4600) + max(n for n in range(0, 10000) if 100 * ((n + 50) // 100) == 4600))
# sach
zahl("071", erste(lambda n: (n - 14) % 2 == 0 and (n - 14) // 2 + 8 == 20, 1000))
zahl("072", erste(lambda x: 24 + 7 * x == 66, 100, 1))
wahl("073", "□ − 3 · 2 + 5 = 20", 21 - 3 * 2 + 5 == 20)
zahl("074", (lambda x: 2 * x + 6)(erste(lambda x: (x + 6) * 2 == 30, 100)))
zahl("075", erste(lambda g: 12 + 2 * g == 4 + 4 * g, 100))
zahl("076", erste(lambda x: 4 * x + 12 - 4 == 108, 1000, 1))
wahl("077", "Fehler: Die Reihenfolge ist falsch", erste(lambda x: x * 2 + 6 == 30, 100) == 12)

fehlt = sorted(set(Q) - gesehen)
if fehlt:
    abw.append(("nicht geprüft", fehlt))
for x in abw:
    print("ABWEICHUNG", x)
print(f"{len(gesehen)} Sollantworten neu gerechnet, {len(abw)} Abweichungen")
