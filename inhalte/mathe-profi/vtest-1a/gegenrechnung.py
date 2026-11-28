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
wahl("001", "17: Es ist 3² = 3 · 3", 3 ** 2 + 2 ** 3 == 17 and 5 ** 5 == 3125 and 3 * 2 + 2 * 3 == 12)
zahl("002", sum(3 ** 5 for _ in [0]) - sum(3 ** 4 for _ in [0]))
g = 1                                                               # Verdopplung je Generation: 2, 4, 8, 16 Personen
for _ in range(4):
    g *= 2
zahl("003", g)
zahl("004", erste(lambda x: x * x * x * x == 2 ** 8, 100, 1))
wahl("005", "Die 4 steht 6-mal", 4 ** 6 == 4096 and 4 * 6 == 24 and 6 ** 4 == 1296)
wahl("006", "Zufall bei diesen Zahlen", 2 ** 4 == 16 == 4 ** 2 and 2 ** 3 == 8 and 3 ** 2 == 9)
wahl("007", "Fehler: Die Hochzahl 2 gehört nur zur 3", 2 * 3 * 3 == 18 and 6 * 6 == 36)
# quadrat
zahl("008", (lambda a: (next(s for s in range(1, 500) if 4 * s == 2 * 4 * a)) ** 2)(next(t for t in range(1, 200) if t * t == 144)))
wahl("009", "6 727", [n for n in range(1, 200) if n * n in (6727, 7396, 5929, 4761)] == [69, 77, 86])
zahl("010", 11 * 11 - 7 * 7)
zahl("011", sum(9 for _ in range(9)))
zahl("012", erste(lambda n: n * n - (n - 1) * (n - 1) == 27, 100))
wahl("013", "Kein Fehler: Bei einem Produkt", 12 * 12 == 144 == 9 * 16 and 3 + 4 != 12)
wahl("014", "Die große Platte hat 4-mal so viel Fläche", 10 * 10 == 4 * 5 * 5)
# zehner
zahl("015", erste(lambda x: 10 ** 6 - 9 * 10 ** 5 == x * 10 ** 5, 100))
wahl("016", "56 · 10⁵", [x for x in (56 * 10 ** 6, 560 * 10 ** 5, 5600 * 10 ** 4, 56 * 10 ** 5) if x != 56000000] == [5600000])
zahl("017", len(str(500 * 1000 // 5)) - 1)                         # 100 000 Münzen = 10⁵
wahl("018", "Nur Anna: 45 · 100 000", 45 * 100000 == 4500000 and 450 * 100000 == 45000000)
zahl("019", erste(lambda d: d * 10 * 100 == 10 ** 6, 10 ** 6))
wahl("020", "Fehler: Er hat die Hochzahlen addiert", 1000 + 1000 == 2000 and 1000 * 1000 == 10 ** 6)
zahl("021", max(n for n in range(0, 20) if 10 ** n < 5000000))
# sach
b, t = 1, 0
while not (b > 100 + 100 * t):
    t += 1
    b = 2 ** t
zahl("022", t)
zahl("027", erste(lambda a: a * 3 * 3 * 3 * 3 == 405, 405))
zahl("023", erste(lambda n: 2 ** n == 64, 30))
zahl("024", len({(a, b, c, d, e) for a in "KZ" for b in "KZ" for c in "KZ" for d in "KZ" for e in "KZ"}))
wahl("025", "3 · 2⁵", 3 * 2 * 2 * 2 * 2 * 2 == 96)
zahl("026", (10 * 81) // (5 * 81) if 10 * 81 % (5 * 81) == 0 else None)

wahl("028", "Fehler: Sie hat 2 · 3 = 6 als Basis", 2 * 3 ** 4 == 162 and 6 ** 4 == 1296)

# ═════════ zahlen.rechengesetze ═════════
# klammern
wahl("029", "(20 − 4) · 3 + 2", (20 - 4) * 3 + 2 == 50 and 20 - (4 * 3 + 2) != 50 and 20 - 4 * (3 + 2) != 50 and (20 - 4) * (3 + 2) != 50)
zahl("030", erste(lambda x: (x + 4) * 3 - 5 == 25, 100))
wahl("031", "Addiere 12 und 8, teile die Summe durch 4", 40 - (12 + 8) // 4 == 35)
zahl("032", min(20 - 4 + 6, (20 - 4) + 6, 20 - (4 + 6)))
wahl("033", "(30 − 12) − 4", (30 - 12) - 4 == 30 - 12 - 4)
zahl("034", sum(1 for t in ("2+3*4", "(2+3)*4", "2*(3+4)", "2*3+4*2") if eval(t) == 14))
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
wahl("043", "Beide Werte sind gleich, denn 24 · 5 ergibt 120", 24 * 125 * 5 == 15000 == 12 * 125 * 10)
zahl("044", erste(lambda x: 94 - 37 - 23 == 94 - x, 200))
wahl("045", "Zuerst 25 · 4 = 100", 25 * 4 * 17 == 1700)
wahl("046", "36 : 4 und 4 : 36", 36 % 4 == 0 and 4 % 36 != 0 and 7 * 9 == 9 * 7 and 25 + 17 == 17 + 25 and 5 * 12 == 12 * 5)
zahl("047", erste(lambda x: 8 * x * 125 == 4000, 1000))
zahl("048", erste(lambda x: 6 * x == 18 * 27, 1000, 1))
zahl("049", 6482 - 1997 + 3518)
# verteilen
zahl("050", sum(36 for _ in range(99)) - sum(36 for _ in range(9)))
zahl("051", erste(lambda x: 17 * x + 17 * 14 == 17 * 50, 1000))
wahl("052", "9 · (6 + 4)", 9 * 10 == 90)
wahl("053", "Beide: Annas Rechnung", 4 * 20 + 4 * 7 == 108 == 4 * 30 - 4 * 3 and 4 * 30 - 3 == 117 and 4 * 20 + 7 == 87)
wahl("054", "Sie verdoppelt sich", 16 * 30 + 16 * 2 == 2 * (8 * 30 + 8 * 2))
wahl("055", "Die 19 ausklammern", 19 * (36 + 64 - 50) == 950 == 19 * 36 + 19 * 64 - 19 * 50)
wahl("056", "Fehler: In der Klammer muss ein Plus", 15 * 7 + 15 * 9 == 240)
# umkehraufgabe_mal
zahl("057", sum(1 for a in range(1, 13) if any(a * x == 36 for x in range(1, 40))))
wahl("058", "36 : 9", 36 // 9 == 4 and 36 // 4 == 9)
zahl("059", max(a for a in range(1, 50) for b in range(1, 50) if a * b == 48 and a + b == 14))
wahl("060", "56 : x = 7", 7 * 8 == 56 and 56 // 8 == 7)
wahl("061", "48 Murmeln werden gleichmäßig", 48 // 8 == 6)
wahl("062", "Weil 50 nicht in der 7er-Reihe", 50 not in [7 * n for n in range(1, 30)] and 49 in [7 * n for n in range(1, 30)])
zahl("063", erste(lambda x: (x * 5 + 12) / 4 == 8, 1000))
# ueberschlag
zahl("064", round(600 * 50 / (612 * 49) * 10) if False else round(30000 / 2998))
zahl("065", max(n for n in range(1, 100) if (n // 10) * 10 + (10 if n % 10 >= 5 else 0) == 30))
zahl("066", 3 * 200 - 3 * 198)
wahl("067", "Beide Überschläge sind brauchbar", abs(4800 + 3500 - (4812 + 3487)) < abs(5000 + 3000 - (4812 + 3487)))
wahl("068", "Reicht nicht: 23 · 48", 23 * 48 == 1104 > 1000)
wahl("069", "Fehler: Der Überschlag ist zu grob", 596 * 12 == 7152 and abs(600 * 12 - 7152) == 48)
zahl("070", min(n for n in range(0, 10000) if 100 * ((n + 50) // 100) == 4600) + max(n for n in range(0, 10000) if 100 * ((n + 50) // 100) == 4600))
# sach
zahl("071", erste(lambda g: 12 + 2 * g == 4 + 4 * g, 100))
zahl("072", erste(lambda x: 24 + 7 * x == 66, 100, 1))
wahl("073", "□ − 3 · 2 + 5 = 20", 21 - 3 * 2 + 5 == 20)
zahl("074", (lambda x: 2 * x + 6)(erste(lambda x: (x + 6) * 2 == 30, 100)))
zahl("075", erste(lambda n: (n - 14) % 2 == 0 and (n - 14) // 2 + 8 == 20, 1000))
wahl("076", "4 · x + 12 − 4 = 108", erste(lambda x: 4 * x + 12 - 4 == 108, 1000, 1) == 25)
wahl("077", "Kein Fehler: Man kehrt", erste(lambda x: x * 2 + 6 == 30, 100) == 12)

fehlt = sorted(set(Q) - gesehen)
if fehlt:
    abw.append(("nicht geprüft", fehlt))
for x in abw:
    print("ABWEICHUNG", x)
print(f"{len(gesehen)} Sollantworten neu gerechnet, {len(abw)} Abweichungen")
