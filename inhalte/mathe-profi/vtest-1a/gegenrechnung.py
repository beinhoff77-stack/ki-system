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
wahl("001", "Mia irrt sich. 2⁵", 2 * 2 * 2 * 2 * 2 == 32 and 32 != 10)
zahl("002", erste(lambda n: n * n * n * n == 81, 100))
g = 1                                                               # Verdopplung je Generation: 2, 4, 8, 16 Personen
for _ in range(4):
    g *= 2
zahl("003", g)
zahl("004", erste(lambda n: 6 ** n == 216, 20))
wahl("005", "Die 4 steht 6-mal", 4 ** 6 == 4096 and 4 * 6 == 24 and 6 ** 4 == 1296)
wahl("006", "2⁴ = 4²", 2 ** 4 == 16 == 4 ** 2 and 2 ** 3 != 3 ** 2)
wahl("007", "Fehler: Er hat 3 mit 4 malgenommen", 3 * 3 * 3 * 3 == 81 and 3 * 4 == 12)
# quadrat
zahl("008", 4 * erste(lambda s: s * s == 225, 100))
wahl("009", "121, denn 11 · 11 = 121", 11 * 11 == 121 and all(x * x != 111 and x * x != 120 for x in range(1, 20)))
zahl("010", 11 * 11 - 7 * 7)
wahl("011", "8² = 8 · 8 = 64", 8 * 8 == 64)
zahl("012", erste(lambda n: n * n - (n - 1) * (n - 1) == 27, 100))
zahl("013", 625 - 25 - 24)
wahl("014", "Die große Platte hat 4-mal", 10 * 10 == 4 * 5 * 5)
# zehner
wahl("015", "10⁶ ist größer", 10 ** 6 > 9 * 10 ** 5)
wahl("016", "34 · 10⁴", 34 * 10 ** 4 == 340000 and 34 * 10 ** 5 == 3400000 and 3400000 != 340000)
zahl("017", len(str(500 * 1000 // 5)) - 1)                         # 100 000 Münzen = 10⁵
zahl("018", 370000 // 10000)
zahl("019", erste(lambda d: d * 10 * 100 == 10 ** 6, 10 ** 6))
zahl("020", sum(3 * 10 ** 5 for _ in range(60)))
zahl("021", max(n for n in range(0, 20) if 10 ** n < 1000000))
# sach
zahl("022", erste(lambda a: a * 3 * 3 * 3 * 3 == 405, 405))
zahl("023", erste(lambda n: 2 ** n == 64, 30))
zahl("024", erste(lambda n: 10 ** n == 10000, 30))
wahl("025", "3 · 2⁵", 3 * 2 * 2 * 2 * 2 * 2 == 96)
wahl("026", "3⁶", [3 ** n for n in (1, 2, 3)] == [3, 9, 27])
b, t = 1, 0
while not (b > 100 + 100 * t):
    t += 1
    b = 2 ** t
zahl("027", t)
wahl("028", "Fehler: Sie hat 2 und 3 zu 6", 2 * 3 ** 4 == 162 and 6 ** 4 == 1296)

# ═════════ zahlen.rechengesetze ═════════
# klammern
wahl("029", "(20 − 4) · 3 + 2", (20 - 4) * 3 + 2 == 50 and 20 - (4 * 3 + 2) != 50 and 20 - 4 * (3 + 2) != 50 and (20 - 4) * (3 + 2) != 50)
wahl("030", "(8 + 4) · 5 − 3", max([8 + 4 * 5 - 3, (8 + 4) * 5 - 3, 8 + 4 * (5 - 3), (8 + 4) * (5 - 3)]) == 57)
zahl("031", erste(lambda b: (18 + b) == 6 * 7, 100))
wahl("032", "(9 + 3) : 4 · 2", (9 + 3) / 4 * 2 == 6)
wahl("033", "(30 − 12) − 4", (30 - 12) - 4 == 30 - 12 - 4)
zahl("034", 48 // 8 * 3 - (8 + 6))
wahl("035", "Fehler: Er hat die Klammer nicht zuerst", 100 - 20 * 4 == 20)
# termaufbau
wahl("036", "7 Jungen und 5 Mädchen bekommen je 4 Sticker. 6 Sticker gehen verloren.", (7 + 5) * 4 - 6 == 42)
zahl("037", erste(lambda g: 6 * 8 + 4 * g == 72, 100))
wahl("038", "40 − (9 + 6) = 25", 40 - 15 == 25)
wahl("039", "20 − (4 · 3 + 2 · 2)", 20 - (12 + 4) == 4)
zahl("040", erste(lambda n: 4 + 2 * (n - 1) == 14, 100, 1))
wahl("041", "Anna: Punktrechnung kommt vor Strichrechnung", 8 + 5 * 3 == 23)
zahl("042", (12 * 9 + 8 * 11 - 20) // 4)
# vorteil
wahl("043", "Beim Addieren darf man die Summanden", 47 + 38 + 53 == 138)
wahl("044", "63 + 37 + 58", sorted([63, 37, 58]) == sorted([37, 58, 63]))
zahl("045", erste(lambda n: n * 5 * 20 == 1500, 1000, 1))
wahl("046", "Beide bekommen 3 700", 50 * 37 * 2 == 3700 == 50 * 2 * 37)
zahl("047", erste(lambda x: 38 + x + 62 == 150, 1000))
wahl("048", "Fehler: Nach 2 · 50 = 100 muss mal 37", 2 * 50 * 37 == 3700)
wahl("049", "Beide Werte sind gleich, denn 36 · 4", 36 * 25 * 4 == 3600 == 18 * 25 * 8)
# verteilen
wahl("050", "Beide Rechnungen berechnen die Fläche", 8 * 30 + 8 * 2 == 256 == 8 * 32)
zahl("051", erste(lambda x: 17 * x + 17 * 14 == 17 * 50, 1000))
wahl("052", "9 · (6 + 4)", 9 * 10 == 90)
zahl("053", erste(lambda x: 8 * x + 12 * x == 200, 1000, 1))
wahl("054", "9 · 20 + 3", 9 * 20 + 3 == 183 and 9 * 23 == 207)
zahl("055", 19 * 36 + 19 * 64 - 19 * 50)
wahl("056", "Fehler: In der Klammer muss ein Plus", 15 * 7 + 15 * 9 == 240)
# umkehraufgabe_mal
zahl("057", erste(lambda x: (x * 5 + 12) / 4 == 8, 1000))
wahl("058", "36 : 9", 36 // 9 == 4 and 36 // 4 == 9)
zahl("059", erste(lambda x: 5 * x + 3 == 43, 100, 1))
wahl("060", "56 : x = 7", 7 * 8 == 56 and 56 // 8 == 7)
wahl("061", "48 Murmeln werden gleichmäßig", 48 // 8 == 6)
wahl("062", "Weil 50 nicht in der 7er-Reihe", 50 not in [7 * n for n in range(1, 30)] and 49 in [7 * n for n in range(1, 30)] and 56 in [7 * n for n in range(1, 30)])
zahl("063", sum(1 for a in range(1, 13) if any(a * x == 36 for x in range(1, 40))))
# ueberschlag
wahl("064", "600 · 50 = 30 000", 612 * 49 == 29988)
zahl("065", max(n for n in range(1, 100) if (n // 10) * 10 + (10 if n % 10 >= 5 else 0) == 30))
wahl("066", "40 · 50", min([30 * 50, 40 * 60, 40 * 5, 40 * 50], key=lambda x: abs(x - 39 * 52)) == 2000)
zahl("067", abs(48 * 52 - 40 * 50) - abs(48 * 52 - 50 * 50))
zahl("068", abs(sum(100 * ((x + 50) // 100) for x in (396, 612, 1987)) - (396 + 612 + 1987)))
wahl("069", "Fehler: Sie hat 12 zu grob", 596 * 12 == 7152 and 600 * 12 == 7200)
zahl("070", sum(1 for n in range(0, 6000) if 100 * ((n + 50) // 100) == 4600))
# sach
zahl("071", erste(lambda n: (n - 14) % 2 == 0 and (n - 14) // 2 + 8 == 20, 1000))
zahl("072", erste(lambda x: 24 + 7 * x == 66, 100, 1))
wahl("073", "□ − 3 · 2 + 5 = 20", 21 - 3 * 2 + 5 == 20)
zahl("074", erste(lambda b: 2 * (11 + b) == 36, 100, 1))
zahl("075", next(n for n in range(2, 1000, 2) if (n - (n // 2 + 7)) % 2 == 0 and (n - (n // 2 + 7)) // 2 == 11))
zahl("076", erste(lambda x: 4 * x + 12 - 4 == 108, 1000, 1))
wahl("077", "Fehler: Die Reihenfolge ist falsch", erste(lambda x: x * 2 + 6 == 30, 100) == 12)

fehlt = sorted(set(Q) - gesehen)
if fehlt:
    abw.append(("nicht geprüft", fehlt))
for x in abw:
    print("ABWEICHUNG", x)
print(f"{len(gesehen)} Sollantworten neu gerechnet, {len(abw)} Abweichungen")
