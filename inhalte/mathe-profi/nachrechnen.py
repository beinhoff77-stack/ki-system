"""Mathe-Profi, Auftrag 1: rechnet jede Musterlösung auf zwei verschiedenen Wegen nach
und schreibt die Aufgaben als Datensätze nach aufgaben-auftrag1.json.

Aufruf: python3 -I inhalte/mathe-profi/nachrechnen.py
Bricht mit AssertionError ab, wenn zwei Wege nicht übereinstimmen.
"""
import json
import os
from fractions import Fraction as F
from itertools import combinations

AUFGABEN = []


def neu(**k):
    AUFGABEN.append(k)


# ---------------- Flug Klasse 5: zahlen.rechengesetze ----------------

# R1 vorteil – Faktorpaar antippen (neue Form „markieren“)
fak = [4, 17, 25, 3]
glatt = [p for p in combinations(range(4), 2) if (fak[p[0]] * fak[p[1]]) % 100 == 0]
assert glatt == [(0, 2)], glatt                       # eindeutig: nur 4 · 25 ist glatt
weg1 = (4 * 25) * (17 * 3)                            # Paar zuerst
weg2 = ((4 * 17) * 25) * 3                            # stur von links
assert weg1 == weg2 == 5100
neu(nr="R1", l="vorteil", p="uebung", s=1, g="erkennen", y="markieren",
    f={"text": "Rechne 4 · 17 · 25 · 3 geschickt. Tippe die zwei Faktoren an, die du zuerst malnimmst.",
       "felder": ["4", "17", "25", "3"], "anzahl": 2, "anzeige": "term"},
    o={"menge": [0, 2]},
    h="Welche zwei Zahlen ergeben zusammen eine Zahl mit Nullen am Ende?",
    w="4 · 25 = 100. Dann 100 · 17 · 3 = 100 · 51 = 5 100.",
    c="4 * 25", probe={"weg1": weg1, "weg2": weg2})

# R2 verteilen – ausklammern (vorhandene Form luecken)
a, b, k = 23, 77, 17
w1 = k * (a + b)                                      # ausklammern
w2 = k * a + k * b                                    # stur: 391 + 1 309
assert w1 == w2 == 1700 and k * a == 391 and k * b == 1309
neu(nr="R2", l="verteilen", p="uebung", s=2, g="umkehr", y="luecken",
    f={"text": "Rechne faul: Klammere die 17 aus.", "schablone": "17 · 23 + 17 · 77 = 17 · □ = □",
       "hinweis": "Je Kästchen eine ganze Zahl."},
    o={"werte": [100, 1700]},
    h="Beide Produkte haben einen Faktor gemeinsam. Was bleibt in der Klammer?",
    w="17 · 23 + 17 · 77 = 17 · (23 + 77) = 17 · 100 = 1 700.",
    c=["23 + 77", "17 * (23 + 77)"], probe={"weg1": w1, "weg2": w2})

# R3 klammern – Klammer setzen (vorhandene Form auswahl)
opts = {"(3 + 4) · 5 − 2": (3 + 4) * 5 - 2, "3 + 4 · (5 − 2)": 3 + 4 * (5 - 2),
        "3 + (4 · 5 − 2)": 3 + (4 * 5 - 2), "3 + 4 · 5 − 2": 3 + 4 * 5 - 2}
treffer = [t for t, v in opts.items() if v == 33]
assert treffer == ["(3 + 4) · 5 − 2"], opts          # eindeutig
assert 7 * 5 - 2 == 33                               # zweiter Weg: rückwärts 33 + 2 = 35 = 7 · 5
assert (33 + 2) % 5 == 0 and (33 + 2) // 5 == 3 + 4
neu(nr="R3", l="klammern", p="uebung", s=3, g="parameter", y="auswahl",
    f={"text": "Wo muss die Klammer hin, damit 33 herauskommt?  3 + 4 · 5 − 2"},
    a=["3 + 4 · (5 − 2)", "(3 + 4) · 5 − 2", "3 + (4 · 5 − 2)", "Ohne Klammer kommt schon 33 heraus."],
    o={"index": 1},
    h="Rechne rückwärts: Was muss vor dem „− 2“ stehen?",
    w="(3 + 4) · 5 − 2 = 7 · 5 − 2 = 35 − 2 = 33. Rückwärts: 33 + 2 = 35 = 7 · 5, und 7 = 3 + 4.",
    probe={"werte": opts})

# R4 ueberschlag – schätzen am Zahlenstrahl (neue Form „schieber“)
genau = 487 * 21
assert genau == 487 * 20 + 487 == 10227
ueber = 500 * 20
assert ueber == 10000
von, bis = 8000, 12000
assert von <= genau <= bis and von <= ueber <= bis
for falsch in (1000, 100000):                        # Stelle verrutscht -> außerhalb
    assert not (von <= falsch <= bis)
neu(nr="R4", l="ueberschlag", p="uebung", s=2, g="darstellung", y="schieber",
    f={"text": "Ohne genau zu rechnen: Wo liegt 487 · 21? Schieb den Pfeil an die Stelle.",
       "grafik": {"typ": "zahlenstrahl", "start": 0, "ende": 20000, "abschnitte": 10,
                  "beschriftet": "anfang_ende"},
       "schieber": {"start": 0, "ende": 20000, "schritt": 100, "anfang": None}},
    o={"von": von, "bis": bis, "wert": genau},
    h="Runde beide Zahlen so, dass du im Kopf malnehmen kannst.",
    w="487 ≈ 500 und 21 ≈ 20, also etwa 500 · 20 = 10 000. Genau: 487 · 20 + 487 = 9 740 + 487 = 10 227.",
    c="487 * 21", probe={"genau": genau, "ueberschlag": ueber})

# R5 sach – Rückwärts-Schritte ordnen (neue Form „reihenfolge“)
def vor(x):
    return ((x * 4) - 30) / 2


start = 25
st1 = start * 2          # :2 umkehren
st2 = st1 + 30           # −30 umkehren
st3 = st2 / 4            # ·4 umkehren
assert st3 == 20 and vor(20) == 25                    # Probe vorwärts
# zweiter Weg: Gleichung (4x − 30) : 2 = 25  ->  4x − 30 = 50  ->  x = 20
x = F(25 * 2 + 30, 4)
assert x == 20
neu(nr="R5", l="sach", p="uebung", s=3, g="rueckwaerts", y="reihenfolge",
    f={"text": "Eine Zahl wird mit 4 malgenommen, dann wird 30 abgezogen, dann durch 2 geteilt. "
               "Es kommt 25 heraus. Leg die Schritte zum Rückwärtsrechnen in die richtige Reihenfolge. "
               "Zwei Bausteine brauchst du nicht.",
       "bausteine": [{"id": "plus30", "text": "+ 30"}, {"id": "mal2", "text": "· 2"},
                     {"id": "durch4", "text": ": 4"}, {"id": "minus30", "text": "− 30"},
                     {"id": "durch2", "text": ": 2"}],
       "plaetze": 3, "start_text": "25"},
    o={"folge": ["mal2", "plus30", "durch4"]},
    h="Den letzten Schritt machst du zuerst rückgängig.",
    w="25 · 2 = 50, 50 + 30 = 80, 80 : 4 = 20. Probe: 20 · 4 = 80, 80 − 30 = 50, 50 : 2 = 25.",
    probe={"ergebnis": 20})

# R6 schriftlich_geteilt – Fehlerzeile finden (vorhandene Form auswahl + tabelle)
dvd, dvs = 2976, 12
assert dvd // dvs == 248 and dvd % dvs == 0
z1 = (29 // 12, 29 - 12 * (29 // 12))                # (2, 5) richtig
z2_falsch_rest = 7
z2_richtig_rest = 57 - 4 * 12
assert z1 == (2, 5) and z2_richtig_rest == 9 != z2_falsch_rest
z3 = (76 // 12, 76 - 12 * (76 // 12))                # Folgezeile aus dem falschen Rest
assert z3 == (6, 4)
assert 246 * 12 + 4 == 2956 != dvd                   # Probe deckt den Fehler auf
assert 248 * 12 == dvd                               # zweiter Weg: Probe der richtigen Lösung
neu(nr="R6", l="schriftlich_geteilt", p="uebung", s=3, g="fehler", y="auswahl",
    f={"text": "Jemand rechnet 2 976 : 12 und erhält 246 Rest 4. In welcher Zeile steckt der Fehler?",
       "grafik": {"typ": "tabelle", "kopf": ["", "teilen", "mal", "Rest"],
                  "zeilen": [["Zeile 1", "29 : 12 = 2", "2 · 12 = 24", "5"],
                             ["Zeile 2", "57 : 12 = 4", "4 · 12 = 48", "7"],
                             ["Zeile 3", "76 : 12 = 6", "6 · 12 = 72", "4"]]}},
    a=["Zeile 1", "Zeile 2", "Zeile 3", "Alles richtig, 246 Rest 4 stimmt."],
    o={"index": 1},
    h="Prüfe in jeder Zeile die Minus-Rechnung.",
    w="Zeile 2: 57 − 48 = 9, nicht 7. Richtig geht es mit 96 : 12 = 8 weiter: 248. Probe: 248 · 12 = 2 976.",
    probe={"richtig": 248})

# ---------------- Flug Klasse 8: funktionen.linear ----------------

# L1 graph_ablesen – Gerade durch zwei Gitterpunkte zeichnen (neue Form „punkte“)
m, t = F(-2, 3), F(2)
gitter = [(x, y) for x in range(-5, 7) for y in range(-4, 6) if m * x + t == y]
assert set(gitter) == {(-3, 4), (0, 2), (3, 0), (6, -2)}, gitter
# zweiter Weg: Steigungsdreieck 3 nach rechts, 2 nach unten ab (0|2)
assert (0 + 3, 2 - 2) in gitter and (0 - 3, 2 + 2) in gitter
neu(nr="L1", l="graph_ablesen", p="uebung", s=1, g="direkt", y="punkte",
    f={"text": "Zeichne die Gerade y = −(2/3)x + 2. Setze dazu zwei Punkte auf Gitterpunkte.",
       "grafik": {"typ": "koordinaten", "x": [-5, 6], "y": [-4, 5]},
       "setzen": {"anzahl": 2, "raster": 1, "linie": "gerade"}},
    o={"regel": "auf_gerade", "m": [-2, 3], "t": [2, 1], "verschieden": True, "toleranz": 0.25},
    h="Starte bei t auf der y-Achse. m = −2/3 heißt: 3 nach rechts, 2 nach unten.",
    w="Start (0 | 2). 3 nach rechts, 2 nach unten: (3 | 0). Gültig sind alle Gitterpunkte der Geraden: (−3 | 4), (0 | 2), (3 | 0), (6 | −2).",
    probe={"gitterpunkte": [list(p) for p in gitter]})

# L2 wirkung – Parameter am Schieberegler einstellen (neue Form „schieber“, Graph läuft mit)
k1 = F(-1 - 1, 4)                                    # aus −1 = 4k + 1
k2 = F(-1 - 1, 4 - 0)                                 # Steigung von (0|1) nach (4|−1)
assert k1 == k2 == F(-1, 2)
neu(nr="L2", l="wirkung", p="uebung", s=2, g="darstellung", y="schieber",
    f={"text": "Alle Geraden y = k · x + 1 gehen durch (0 | 1). Stell k so ein, dass die Gerade durch P(4 | −1) geht.",
       "grafik": {"typ": "koordinaten", "x": [-2, 6], "y": [-4, 5], "punkte": [{"x": 4, "y": -1, "name": "P"}],
                  "graphen": [{"art": "linear", "m": "k", "t": 1}]},
       "schieber": {"name": "k", "start": -3, "ende": 3, "schritt": 0.25, "anfang": 1}},
    o={"wert": -0.5, "toleranz": 0.125},
    h="Von (0 | 1) nach P: wie weit nach rechts, wie weit nach unten?",
    w="Von (0 | 1) nach (4 | −1): 4 nach rechts, 2 nach unten. k = −2 : 4 = −0,5. Probe: −0,5 · 4 + 1 = −1.",
    c="(-1 - 1) / 4", probe={"weg1": str(k1), "weg2": str(k2)})

# L3 zwei_punkte – Steigung aus Wertetabelle (vorhandene Form luecken)
xs, ys = [0, 3, 6, 9], [7, 5, 3, 1]
s1 = F(ys[-1] - ys[0], xs[-1] - xs[0])               # ganze Tabelle
s2 = F(ys[1] - ys[0], xs[1] - xs[0])                 # ein Schritt
assert s1 == s2 == F(-2, 3)
assert all(F(ys[i + 1] - ys[i], xs[i + 1] - xs[i]) == s2 for i in range(3))   # wirklich linear
neu(nr="L3", l="zwei_punkte", p="uebung", s=2, g="darstellung", y="luecken",
    f={"text": "Die Tabelle gehört zu einer Geraden. Gib ihre Steigung als gekürzten Bruch an.",
       "grafik": {"typ": "tabelle", "kopf": ["x", "0", "3", "6", "9"], "zeilen": [["y", "7", "5", "3", "1"]]},
       "schablone": "m = □/□", "hinweis": "Minus gehört in den Zähler."},
    o={"werte": [-2, 3]},
    h="Schau nur auf einen Schritt der Tabelle: um wie viel ändert sich x, um wie viel y?",
    w="Ein Schritt: x + 3, y − 2. Also m = −2/3. Ganze Tabelle: (1 − 7) : (9 − 0) = −6/9 = −2/3.",
    c=["-2", "3"], probe={"weg1": str(s1), "weg2": str(s2)})

# L4 schnittpunkte – Tarife (vorhandene Form zahl)
xa = F(8 - 2, F(25, 100) - F(10, 100))               # gleichsetzen
xb = F(6) / F(15, 100)                               # Vorsprung : Aufholtempo
assert xa == xb == 40
assert 8 + F(10, 100) * 40 == 2 + F(25, 100) * 40 == 12
neu(nr="L4", l="schnittpunkte", p="uebung", s=3, g="transfer", y="zahl",
    f={"text": "Tarif A: 8 € im Monat plus 0,10 € pro Minute. Tarif B: 2 € im Monat plus 0,25 € pro Minute. "
               "Bei wie vielen Minuten kosten beide gleich viel?"},
    o={"wert": 40, "einheit": "min"},
    h="B ist am Anfang 6 € billiger. Wie viel holt A pro Minute auf?",
    w="Faul: B startet 6 € billiger, A holt pro Minute 0,15 € auf. 6 : 0,15 = 40. "
      "Probe: 8 + 4 = 12 und 2 + 10 = 12.",
    c="(8 - 2) / (0.25 - 0.10)", probe={"weg1": str(xa), "weg2": str(xb)})

# L5 lage – Paare zuordnen (neue Form „zuordnung“)
def lage(m1, t1, m2, t2):
    if m1 == m2:
        return "identisch" if t1 == t2 else "parallel"
    return "senkrecht" if m1 * m2 == -1 else "schneiden"


paare = [("y = 3x + 1  und  y = 3x − 2", (3, 1, 3, -2)),
         ("y = 3x + 1  und  y = −(1/3)x", (3, 1, F(-1, 3), 0)),
         ("y = 2x + 4  und  2y = 4x + 8", (2, 4, F(4, 2), F(8, 2))),   # zweite umgeformt
         ("y = x + 1  und  y = 2x + 1", (1, 1, 2, 1)),
         ("y = −2x + 3  und  y = 0,5x − 1", (-2, 3, F(1, 2), -1))]
ziele = ["parallel", "senkrecht", "identisch", "schneiden"]
soll = [ziele.index(lage(*p[1])) for p in paare]
assert soll == [0, 1, 2, 3, 1], soll   # 5 Paare, 4 Ziele: kein Rest durch Ausschluss
# zweiter Weg: Richtungsvektoren (1|m): Skalarprodukt 0 -> senkrecht; Kreuzprodukt 0 -> gleiche Richtung,
# dann identisch, wenn (0|t1) auf der zweiten Geraden liegt
def lage2(m1, t1, m2, t2):
    kreuz, skalar = m2 - m1, 1 + m1 * m2
    if kreuz == 0:
        return "identisch" if m2 * 0 + t2 == t1 else "parallel"
    return "senkrecht" if skalar == 0 else "schneiden"


assert [ziele.index(lage2(*p[1])) for p in paare] == soll
neu(nr="L5", l="lage", p="uebung", s=2, g="erkennen", y="zuordnung",
    f={"text": "Ordne jedem Geradenpaar zu, wie die Geraden liegen.",
       "links": [p[0] for p in paare],
       "rechts": ["parallel", "senkrecht", "identisch", "schneiden sich, nicht senkrecht"], "mehrfach": True},
    o={"paare": soll},
    h="Vergleiche zuerst die Steigungen. Bei 2y = … erst nach y auflösen.",
    w="3 = 3, t verschieden: parallel. 3 · (−1/3) = −1: senkrecht. 2y = 4x + 8 heißt y = 2x + 4: identisch. 1 · 2 = 2: schneiden sich, nicht senkrecht. (−2) · 0,5 = −1: senkrecht.",
    probe={"soll": soll})

# L6 schnittpunkte/aufstellen – verknüpfen (vorhandene Form zahl)
sx = F(5 + 1, 2)                                    # x − 1 = −x + 5
sy = sx - 1
assert (sx, sy) == (3, 2) and -sx + 5 == sy
t1 = sy - F(1, 2) * sx                               # einsetzen
# zweiter Weg: Gerade mit m = 0,5 durch S; vom Punkt S 3 nach links, 1,5 nach unten zur y-Achse
t2 = sy - F(1, 2) * 3
assert t1 == t2 == F(1, 2)
neu(nr="L6", l="schnittpunkte", p="uebung", s=3, g="verknuepfen", y="zahl",
    f={"text": "g: y = x − 1 und h: y = −x + 5 schneiden sich im Punkt S. Für welches t geht y = 0,5x + t durch S?"},
    o={"wert": 0.5},
    h="Erst S bestimmen, dann S einsetzen.",
    w="x − 1 = −x + 5 ⇒ x = 3, y = 2, also S(3 | 2). 2 = 0,5 · 3 + t ⇒ t = 0,5.",
    c="2 - 0.5 * 3", probe={"S": [3, 2], "weg1": str(t1), "weg2": str(t2)})

# ---------------- Beispiele zu den neuen Aufgabenformen (D) ----------------
BEISPIELE_D = {}
# D1 markieren
t3 = [51, 62, 75, 88, 111, 124]
BEISPIELE_D["D1b"] = [i for i, z in enumerate(t3) if z % 3 == 0]
assert BEISPIELE_D["D1b"] == [i for i, z in enumerate(t3) if sum(map(int, str(z))) % 3 == 0] == [0, 2, 4]
assert F(3, 4) * 8 == 6 and 8 - 2 == 6                      # D1c: 6 von 8 Feldern
BEISPIELE_D["D1c"] = 6
# D2 schieber
g = F(198, 10) * F(49, 10)
assert g == F(9702, 100) and abs(20 * 5 - g) < 5             # Überschlag 20 · 5 = 100
assert 80 <= g <= 120 and not 80 <= g / 10 <= 120 and not 80 <= g * 10 <= 120
BEISPIELE_D["D2c"] = float(g)
# D3 punkte
dreieck = {"A": (1, 1), "B": (4, 1), "C": (1, 3)}
bild = {k + "'": (-x, y) for k, (x, y) in dreieck.items()}
assert list(bild.values()) == [(-1, 1), (-4, 1), (-1, 3)]
assert all((x2 + x1) / 2 == 0 and y1 == y2 for (x1, y1), (x2, y2) in zip(dreieck.values(), bild.values()))
assert -2 * 9 + 18 == 0 and F(18, 2) == 9                    # Kerze
# D4 zuordnung
namen = {"3 + 4 · 5": "Summe", "(3 + 4) · 5": "Produkt", "20 − 12 : 4": "Differenz", "(20 − 12) : 4": "Quotient"}
assert (3 + 4 * 5, (3 + 4) * 5, 20 - 12 // 4, (20 - 12) // 4) == (23, 35, 17, 2)
graphen = {"g": (2, -1), "h": (F(-1, 2), 2), "k": (F(1, 2), -1)}
rechts = [(2, -1), (F(1, 2), -1), (F(-1, 2), 2)]
BEISPIELE_D["D4c"] = [rechts.index(v) for v in graphen.values()]
assert BEISPIELE_D["D4c"] == [0, 2, 1]
# D5 reihenfolge
assert 6 + 2 == 8 and 8 * 5 == 40 and 48 - 40 == 8 == 48 - (6 + 2) * 5
mm = F(-1 - 1, 6 - 2)
tt = 1 - mm * 2
assert (mm, tt) == (F(-1, 2), 2) and mm * 6 + tt == -1           # Probe mit Q
ziel = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aufgaben-auftrag1.json")
with open(ziel, "w", encoding="utf-8") as fh:
    json.dump(AUFGABEN, fh, ensure_ascii=False, indent=1, default=str)
print(f"OK: {len(AUFGABEN)} Aufgaben, alle zweifach nachgerechnet -> {ziel}")
