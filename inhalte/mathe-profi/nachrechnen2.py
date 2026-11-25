"""Mathe-Profi, Auftrag 2: Aufgabenform „punkte“ (Gitterpunkte setzen).

Aufruf: python3 -I inhalte/mathe-profi/nachrechnen2.py

Was das Skript tut
1. Referenz der Prüfregel (`bewerte`) – so soll der Server rechnen (exakt, ohne Gleitkomma).
2. 20 Musteraufgaben (10 Klasse 5 „Grundbegriffe und Figuren“, 10 Klasse 8 „Lineare Funktionen“).
   Jede Lösung auf zwei Wegen:
     Weg 1 = Rechnung (Formel/Konstruktion),
     Weg 2 = unabhängig: alle Rasterpunkte des Bildes durchsuchen (Eindeutigkeit!) oder im Gitter laufen.
3. Jede Lösung und jede typische falsche Antwort läuft durch `bewerte`.
4. Unsinn-Antworten laufen durch `bewerte` (dürfen nie als Fehler zählen).
5. Nachweise zu den Befunden über die Arbeit des Vorgängers (Abschnitt „Befunde“).
6. Schreibt aufgaben-auftrag2.json, die Daten in entwurf-punkte.html und die Aufgabenliste in auftrag2.md.

Bricht mit AssertionError ab, wenn etwas nicht übereinstimmt.
"""
import json
import os
import re
from fractions import Fraction as F
from itertools import combinations, permutations, product

ORDNER = os.path.dirname(os.path.abspath(__file__))
MAX_SCHRITTE = 10          # Rasterschritte je Achse (siehe auftrag2.md, „Kleinste Breite“)


# ───────────────────────── Referenz der Prüfregel ─────────────────────────

def bruch(v):
    """Zahl exakt als Bruch; alles andere (Text, None, True, NaN) ist Unsinn."""
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        raise ValueError
    if v != v or v in (float("inf"), float("-inf")):
        raise ValueError
    return F(str(v))


def kreuz(a, b, p):
    """0 genau dann, wenn p auf der Geraden durch a und b liegt."""
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])


def bewerte(aufgabe, antwort):
    """Gibt {format_ok, richtig, grund, hinweis} zurück – gleiche Felder wie schule.antwort_bewerten."""
    f, o = aufgabe["f"], aufgabe["o"]
    n, raster = f["setzen"]["anzahl"], F(str(f["setzen"].get("raster", 1)))
    (x0, x1), (y0, y1) = f["grafik"]["x"], f["grafik"]["y"]
    roh = antwort.get("punkte") if isinstance(antwort, dict) else None
    if not isinstance(roh, list) or len(roh) < n:
        fehlt = n - (len(roh) if isinstance(roh, list) else 0)
        return {"format_ok": False, "hinweis": "Setze noch einen Punkt." if fehlt == 1 else f"Setze noch {fehlt} Punkte."}
    unsinn = {"format_ok": False, "hinweis": "Das hat nicht geklappt. Setze die Punkte bitte neu."}
    if len(roh) > n:
        return unsinn
    pkt = []
    for p in roh:
        if not isinstance(p, list) or len(p) != 2:
            return unsinn
        try:
            x, y = bruch(p[0]), bruch(p[1])
        except ValueError:
            return unsinn
        if (x / raster).denominator != 1 or (y / raster).denominator != 1:   # nicht auf dem Raster
            return unsinn
        if not (x0 <= x <= x1 and y0 <= y <= y1):                             # außerhalb des Bildes
            return unsinn
        pkt.append((x, y))
    if len(set(pkt)) != n:                                                     # derselbe Punkt zweimal
        return unsinn

    if o["regel"] == "menge":
        mengen = [frozenset((F(str(x)), F(str(y))) for x, y in m) for m in (o.get("mengen") or [o["punkte"]])]
        ist = frozenset(pkt)
        if ist in mengen:
            return {"format_ok": True, "richtig": True}
        grund = None
        if frozenset((y, x) for x, y in ist) in mengen:
            grund = "vertauscht"
        elif any(sorted((abs(x), abs(y)) for x, y in ist) == sorted((abs(x), abs(y)) for x, y in m) for m in mengen):
            grund = "vorzeichen"
        return {"format_ok": True, "richtig": False, "grund": grund}

    if o["regel"] == "gerade":
        a, b = [(F(str(x)), F(str(y))) for x, y in o["durch"]]
        drauf = [kreuz(a, b, p) == 0 for p in pkt]
        if all(drauf):
            return {"format_ok": True, "richtig": True}
        grund = None
        if n == 2:
            p, q = pkt
            if sum(drauf) == 1:
                grund = "ein_punkt"                                            # ein Punkt stimmt: Richtung falsch
            elif (b[0] - a[0]) * (q[1] - p[1]) == (b[1] - a[1]) * (q[0] - p[0]):
                grund = "verschoben"                                           # Richtung stimmt, Lage falsch
        return {"format_ok": True, "richtig": False, "grund": grund}
    raise AssertionError("unbekannte Regel")


# ───────────────────────── Hilfen zum Nachrechnen ─────────────────────────

def raster_punkte(grafik, raster=1):
    (x0, x1), (y0, y1) = grafik["x"], grafik["y"]
    r = F(str(raster))
    xs = [x0 + i * r for i in range(int((x1 - x0) / r) + 1)]
    ys = [y0 + i * r for i in range(int((y1 - y0) / r) + 1)]
    glatt = lambda v: int(v) if v.denominator == 1 else float(v)
    return [(glatt(x), glatt(y)) for x in xs for y in ys]


def laufen(start, schritt, grafik):
    """Vom Startpunkt in Schritten (dx, dy) in beide Richtungen laufen, solange man im Bild bleibt."""
    (x0, x1), (y0, y1) = grafik["x"], grafik["y"]
    erg, k = set(), 0
    while x0 <= start[0] + k * schritt[0] <= x1 and y0 <= start[1] + k * schritt[1] <= y1:
        erg.add((start[0] + k * schritt[0], start[1] + k * schritt[1])); k += 1
    k = -1
    while x0 <= start[0] + k * schritt[0] <= x1 and y0 <= start[1] + k * schritt[1] <= y1:
        erg.add((start[0] + k * schritt[0], start[1] + k * schritt[1])); k -= 1
    return erg


def koord(x0, x1, y0, y1, **mehr):
    return {"typ": "koordinaten", "x": [x0, x1], "y": [y0, y1], **mehr}


AUFGABEN = []


def neu(nr, klasse, l, s, g, text, grafik, setzen, o, h, w, weg1, weg2, falsch, kern):
    """falsch: Liste (Antwort-Punkte, erwarteter grund, was der Fehler verrät). kern: Lösung in Kurzform für den Bericht."""
    a = {"nr": nr, "klasse": klasse, "l": l, "p": "uebung", "s": s, "g": g, "y": "punkte",
         "f": {"text": text, "grafik": grafik, "setzen": setzen}, "o": o, "h": h, "w": w,
         "probe": {"weg1": weg1, "weg2": weg2},
         "falsch": [{"punkte": [list(p) for p in pk], "grund": gr, "verraet": vr} for pk, gr, vr in falsch],
         "kern": kern}
    AUFGABEN.append(a)
    return a


def pruef_menge(a, loesungen, bedingung):
    """Weg 2 für Regel „menge“ mit einem Punkt: alle Rasterpunkte durchsuchen – genau die Lösungen erfüllen die Bedingung."""
    alle = raster_punkte(a["f"]["grafik"], a["f"]["setzen"].get("raster", 1))
    treffer = {p for p in alle if bedingung(*p)}
    assert treffer == set(loesungen), (a["nr"], treffer, loesungen)


def pruef_gerade(a, gleichung, start, schritt):
    """Weg 1: Gleichung auf allen Rasterpunkten. Weg 2: vom Startpunkt im Steigungsdreieck laufen. Beides gleich, mind. 3 Punkte."""
    gr = a["f"]["grafik"]
    per_gleichung = {p for p in raster_punkte(gr) if gleichung(*p)}
    per_laufen = laufen(start, schritt, gr)
    assert per_gleichung == per_laufen, (a["nr"], sorted(per_gleichung), sorted(per_laufen))
    assert len(per_gleichung) >= 3, (a["nr"], "zu wenige Gitterpunkte im Bild")
    d = a["o"]["durch"]
    assert tuple(d[0]) in per_gleichung and tuple(d[1]) in per_gleichung and d[0] != d[1]
    for p, q in combinations(sorted(per_gleichung), 2):          # jedes Paar von Gitterpunkten der Geraden gilt
        assert bewerte(a, {"punkte": [list(p), list(q)]}).get("richtig") is True
    return sorted(per_gleichung)


# ───────────────────────── Flug Klasse 5: geometrie.grundbegriffe (Kairo) ─────────────────────────
G5 = lambda **m: koord(-5, 5, -5, 5, **m)

# K1 – Punkt eintragen
a = neu("K1", 5, "koordinaten", 1, "direkt",
        "Trage den Punkt P(−3 | 2) ein.", G5(), {"anzahl": 1, "namen": ["P"]},
        {"regel": "menge", "punkte": [[-3, 2]]},
        "Erste Zahl: nach links oder rechts. Zweite Zahl: nach oben oder unten.",
        "−3 heißt 3 nach links, 2 heißt 2 nach oben. P liegt links oben.",
        "Vom Ursprung 3 nach links, 2 nach oben: (0 − 3 | 0 + 2) = (−3 | 2).",
        "Alle 121 Gitterpunkte durchsucht: nur einer liegt 3 links der y-Achse und 2 über der x-Achse.",
        [([(2, -3)], "vertauscht", "x und y vertauscht"), ([(3, 2)], "vorzeichen", "Minus übersehen: rechts statt links")],
        "P(−3 | 2)")
assert (0 - 3, 0 + 2) == (-3, 2)
pruef_menge(a, [(-3, 2)], lambda x, y: x < 0 and abs(x) == 3 and y > 0 and abs(y) == 2)

# K2 – Lage beschreiben → Punkt
a = neu("K2", 5, "koordinaten", 1, "erkennen",
        "Ein Punkt liegt 4 Einheiten unter der x-Achse und 2 Einheiten links von der y-Achse. Setze ihn.",
        G5(), {"anzahl": 1},
        {"regel": "menge", "punkte": [[-2, -4]]},
        "Links von der y-Achse: Die x-Koordinate ist negativ. Unter der x-Achse: Die y-Koordinate ist negativ.",
        "2 nach links: x = −2. 4 nach unten: y = −4. Der Punkt ist (−2 | −4).",
        "links ⇒ x = −2, unten ⇒ y = −4.",
        "Alle Gitterpunkte durchsucht: nur (−2 | −4) hat Abstand 2 zur y-Achse (links) und 4 zur x-Achse (unten).",
        [([(-4, -2)], "vertauscht", "„unter der x-Achse“ als x-Koordinate gelesen"), ([(2, -4)], "vorzeichen", "links und rechts verwechselt")],
        "(−2 | −4)")
pruef_menge(a, [(-2, -4)], lambda x, y: x < 0 and -x == 2 and y < 0 and -y == 4)

# K3 – Schatzkarte (Verschiebung in einer Sachsituation)
a = neu("K3", 5, "koordinaten", 2, "einkleidung",
        "Schatzkarte: Du startest bei S(−4 | 1). Geh 6 Kästchen nach Osten (rechts) und 3 nach Süden (unten). Setze das Kreuz dorthin.",
        G5(punkte=[{"x": -4, "y": 1, "name": "S"}]), {"anzahl": 1, "namen": ["✕"]},
        {"regel": "menge", "punkte": [[2, -2]]},
        "Rechts ändert nur die erste Zahl, unten nur die zweite.",
        "x: −4 + 6 = 2. y: 1 − 3 = −2. Das Kreuz liegt bei (2 | −2).",
        "(−4 + 6 | 1 − 3) = (2 | −2).",
        "Alle Gitterpunkte durchsucht: nur von (2 | −2) kommt man mit 6 nach links und 3 nach oben zurück zu S.",
        [([(2, 4)], None, "nach Norden statt nach Süden gegangen"), ([(-1, -5)], None, "die Schritte vertauscht: 3 nach rechts, 6 nach unten")],
        "(2 | −2)")
assert (-4 + 6, 1 - 3) == (2, -2) and (-4 + 3, 1 - 6) == (-1, -5)
pruef_menge(a, [(2, -2)], lambda x, y: (x - 6, y + 3) == (-4, 1))

# K4 – Strecke mit gegebener Länge (zwei richtige Punkte: o.mengen)
a = neu("K4", 5, "strecken", 1, "direkt",
        "A(−1 | 2) ist gegeben. Setze B so, dass die Strecke [AB] waagrecht liegt und 3 Einheiten lang ist. Es gibt zwei passende Punkte, einer genügt.",
        G5(punkte=[{"x": -1, "y": 2, "name": "A"}]), {"anzahl": 1, "namen": ["B"], "verbinden": "strecke", "mit": [[-1, 2]]},
        {"regel": "menge", "mengen": [[[2, 2]], [[-4, 2]]]},
        "Waagrecht heißt: A und B haben dieselbe y-Koordinate.",
        "Waagrecht: y bleibt 2. 3 nach rechts: B(2 | 2). 3 nach links geht auch: B(−4 | 2).",
        "−1 + 3 = 2 und −1 − 3 = −4, y = 2.",
        "Alle Gitterpunkte durchsucht: genau (2 | 2) und (−4 | 2) liegen auf Höhe 2 im Abstand 3 von A.",
        [([(-1, 5)], None, "senkrecht statt waagrecht"), ([(3, 2)], None, "bis zur x-Koordinate 3 gegangen statt 3 Einheiten weit")],
        "B(2 | 2) oder B(−4 | 2)")
pruef_menge(a, [(2, 2), (-4, 2)], lambda x, y: y == 2 and abs(x - (-1)) == 3)

# K5 – Mittelpunkt: von A über M weiterlaufen
A_, M_ = (-2, -3), (1, -1)
B_ = (2 * M_[0] - A_[0], 2 * M_[1] - A_[1])
assert B_ == (4, 1)
a = neu("K5", 5, "strecken", 2, "mehrschritt",
        "M(1 | −1) ist der Mittelpunkt der Strecke [AB]. A(−2 | −3) ist gegeben. Setze B.",
        G5(punkte=[{"x": -2, "y": -3, "name": "A"}, {"x": 1, "y": -1, "name": "M"}]), {"anzahl": 1, "namen": ["B"]},
        {"regel": "menge", "punkte": [list(B_)]},
        "Wie kommst du von A nach M? Denselben Weg gehst du von M aus noch einmal.",
        "Von A nach M: 3 nach rechts, 2 nach oben. Von M noch einmal: (1 + 3 | −1 + 2) = (4 | 1).",
        "B = M + (M − A) = (1 + 3 | −1 + 2) = (4 | 1).",
        "Alle Gitterpunkte durchsucht: nur für (4 | 1) ist die Mitte von A und B genau M (Summe der Koordinaten = 2 · M).",
        [([(-5, -5)], None, "von A aus in die falsche Richtung gelaufen (M − A abgezogen statt dazugezählt)"),
         ([(4, -1)], "vorzeichen", "nur die x-Koordinate weitergeführt, y auf der Höhe von M gelassen")],
        "B(4 | 1)")
assert (A_[0] - 3, A_[1] - 2) == (-5, -5)
pruef_menge(a, [B_], lambda x, y: (x + A_[0], y + A_[1]) == (2 * M_[0], 2 * M_[1]))

# K6 – Parallele durch P (Regel „gerade“)
a = neu("K6", 5, "lagebeziehungen", 2, "darstellung",
        "g geht durch A(−4 | −1) und B(2 | 2). Zeichne die Parallele zu g durch P(−2 | 3): Setze zwei Gitterpunkte der Parallelen.",
        G5(graphen=[{"art": "linear", "m": 0.5, "t": 1, "name": "g"}],
           punkte=[{"x": -4, "y": -1, "name": "A"}, {"x": 2, "y": 2, "name": "B"}, {"x": -2, "y": 3, "name": "P"}]),
        {"anzahl": 2, "verbinden": "gerade"},
        {"regel": "gerade", "durch": [[-2, 3], [0, 4]]},
        "Wie läuft g von Gitterpunkt zu Gitterpunkt? Dieselbe Treppe startest du bei P.",
        "g läuft 2 nach rechts, 1 nach oben. Dieselbe Treppe ab P(−2 | 3): (0 | 4), (2 | 5) – oder rückwärts (−4 | 2).",
        "Parallele: y = 0,5x + 4 (Steigung von g: 3 : 6 = 0,5; durch P: 3 = −1 + 4).",
        "Ab P in Schritten (2 | 1) laufen: (−4 | 2), (−2 | 3), (0 | 4), (2 | 5) – dieselben Punkte wie aus der Gleichung.",
        [([(-2, 3), (-1, 5)], "ein_punkt", "Treppe gekippt: 1 nach rechts, 2 nach oben"),
         ([(-4, 0), (-2, 1)], "verschoben", "richtige Richtung, aber nicht durch P")],
        "y = 0,5x + 4")
assert F(2 - (-1), 2 - (-4)) == F(1, 2) and F(1, 2) * (-4) + 1 == -1 and F(1, 2) * 2 + 1 == 2     # g im Bild stimmt
K6_PUNKTE = pruef_gerade(a, lambda x, y: 2 * y == x + 8, (-2, 3), (2, 1))

# K7 – Lot auf eine schräge Gerade (Treppe drehen)
gA, gB, P_ = (-3, -2), (1, 0), (-1, 4)
ri = (gB[0] - gA[0], gB[1] - gA[1])                       # Richtung von g: (4 | 2) = 2 · (2 | 1)
auf_g = [p for p in raster_punkte(G5()) if kreuz(gA, gB, p) == 0]
fuss = [p for p in auf_g if (P_[0] - p[0]) * ri[0] + (P_[1] - p[1]) * ri[1] == 0]      # Weg 1: Skalarprodukt 0
assert fuss == [(1, 0)]
naechster = min(auf_g, key=lambda p: (P_[0] - p[0]) ** 2 + (P_[1] - p[1]) ** 2)        # Weg 2: kürzester Abstand
assert naechster == (1, 0)
# und exakt (nicht nur unter Gitterpunkten): Projektion von P auf g
t_ = F((P_[0] - gA[0]) * ri[0] + (P_[1] - gA[1]) * ri[1], ri[0] ** 2 + ri[1] ** 2)
assert (gA[0] + t_ * ri[0], gA[1] + t_ * ri[1]) == (1, 0)
a = neu("K7", 5, "lagebeziehungen", 3, "verknuepfen",
        "Fälle das Lot von P(−1 | 4) auf die Gerade g. Setze den Punkt, in dem das Lot g trifft.",
        G5(graphen=[{"art": "linear", "m": 0.5, "t": -0.5, "name": "g"}], punkte=[{"x": -1, "y": 4, "name": "P"}]),
        {"anzahl": 1, "namen": ["F"], "verbinden": "strecke", "mit": [[-1, 4]]},
        {"regel": "menge", "punkte": [[1, 0]]},
        "g läuft 2 nach rechts, 1 nach oben. Dreh diese Treppe um eine Vierteldrehung: 1 nach rechts, 2 nach unten.",
        "Senkrecht zu „2 rechts, 1 hoch“ ist „1 rechts, 2 runter“. Ab P: (0 | 2), dann (1 | 0) – der liegt auf g.",
        "Skalarprodukt: (P − F) · Richtung von g = (−2 | 4) · (2 | 1) = −4 + 4 = 0, F(1 | 0) liegt auf g.",
        "Unter allen Gitterpunkten von g hat (1 | 0) den kleinsten Abstand zu P; die exakte Projektion von P auf g ist ebenfalls (1 | 0).",
        [([(-1, -1)], None, "Lot als „senkrecht nach unten“ verstanden statt senkrecht zu g"),
         ([(3, 1)], None, "auf g einen Gitterpunkt gewählt, aber nicht im rechten Winkel")],
        "F(1 | 0)")
assert F(1, 2) * (-3) - F(1, 2) == -2 and F(1, 2) * 1 - F(1, 2) == 0                    # g im Bild stimmt
pruef_menge(a, [(1, 0)], lambda x, y: kreuz(gA, gB, (x, y)) == 0 and (P_[0] - x) * ri[0] + (P_[1] - y) * ri[1] == 0)

# K8 – vierte Ecke eines Parallelogramms
A_, B_, C_ = (-4, -2), (1, -2), (3, 2)
D_ = (A_[0] + C_[0] - B_[0], A_[1] + C_[1] - B_[1])
assert D_ == (-2, 2)
a = neu("K8", 5, "vierecke", 2, "umkehr",
        "ABCD ist ein Parallelogramm mit A(−4 | −2), B(1 | −2) und C(3 | 2). Setze die Ecke D.",
        G5(punkte=[{"x": -4, "y": -2, "name": "A"}, {"x": 1, "y": -2, "name": "B"}, {"x": 3, "y": 2, "name": "C"}],
           strecken=[[-4, -2, 1, -2], [1, -2, 3, 2]]),
        {"anzahl": 1, "namen": ["D"], "verbinden": "vieleck", "mit": [[-4, -2], [1, -2], [3, 2]]},
        {"regel": "menge", "punkte": [list(D_)]},
        "Wie kommst du von B nach C? Genauso kommst du von A nach D.",
        "Von B nach C: 2 nach rechts, 4 nach oben. Von A genauso: (−4 + 2 | −2 + 4) = (−2 | 2).",
        "D = A + (C − B) = (−4 + 2 | −2 + 4) = (−2 | 2).",
        "Alle Gitterpunkte durchsucht: nur für (−2 | 2) haben die Diagonalen [AC] und [BD] denselben Mittelpunkt.",
        [([(-4, 2)], None, "D senkrecht über A gesetzt (an ein Rechteck gedacht)"),
         ([(-2, -2 + 2)], None, "nur 2 nach oben statt 4")],
        "D(−2 | 2)")
pruef_menge(a, [D_], lambda x, y: (A_[0] + C_[0], A_[1] + C_[1]) == (B_[0] + x, B_[1] + y))

# K9 – schräges Quadrat
A_, B_, C_ = (0, -3), (3, 0), (0, 3)
q = lambda p, r: (p[0] - r[0]) ** 2 + (p[1] - r[1]) ** 2
D_ = (A_[0] + C_[0] - B_[0], A_[1] + C_[1] - B_[1])
assert D_ == (-3, 0)
a = neu("K9", 5, "vierecke", 3, "transfer",
        "A, B und C sind drei Ecken eines Quadrats ABCD. Setze die vierte Ecke D.",
        G5(punkte=[{"x": 0, "y": -3, "name": "A"}, {"x": 3, "y": 0, "name": "B"}, {"x": 0, "y": 3, "name": "C"}],
           strecken=[[0, -3, 3, 0], [3, 0, 0, 3]]),
        {"anzahl": 1, "namen": ["D"], "verbinden": "vieleck", "mit": [[0, -3], [3, 0], [0, 3]]},
        {"regel": "menge", "punkte": [list(D_)]},
        "Das Quadrat steht auf der Spitze. Von B nach C geht es 3 nach links und 3 nach oben – genauso von A nach D.",
        "Von B nach C: 3 nach links, 3 nach oben. Von A genauso: (0 − 3 | −3 + 3) = (−3 | 0). Alle vier Seiten sind gleich lang, die Diagonalen auch.",
        "D = A + (C − B) = (−3 | 0).",
        "Alle Gitterpunkte durchsucht: nur für (−3 | 0) sind alle vier Seiten gleich lang und beide Diagonalen gleich lang.",
        [([(-3, 3)], None, "an ein Quadrat mit waagrechten Seiten gedacht"),
         ([(0, 0)], None, "die Mitte des Quadrats gesetzt")],
        "D(−3 | 0)")
pruef_menge(a, [D_], lambda x, y: q(A_, B_) == q(B_, C_) == q(C_, (x, y)) == q((x, y), A_) and q(A_, C_) == q(B_, (x, y)))

# K10 – rückwärts verschieben
Q_ = (-1, 2)
a = neu("K10", 5, "koordinaten", 3, "rueckwaerts",
        "Ein Punkt wurde erst um 3 nach links und dann um 2 nach oben verschoben. Jetzt liegt er bei Q(−1 | 2). Setze den Punkt dorthin, wo er am Anfang lag.",
        G5(punkte=[{"x": -1, "y": 2, "name": "Q"}]), {"anzahl": 1},
        {"regel": "menge", "punkte": [[2, 0]]},
        "Geh den Weg von Q aus zurück: Aus links wird rechts, aus oben wird unten.",
        "Zurück: 3 nach rechts, 2 nach unten. (−1 + 3 | 2 − 2) = (2 | 0). Probe: (2 − 3 | 0 + 2) = (−1 | 2).",
        "Rückwärts von Q: (−1 + 3 | 2 − 2) = (2 | 0).",
        "Alle Gitterpunkte durchsucht: nur (2 | 0) landet nach „3 links, 2 hoch“ auf Q.",
        [([(-4, 4)], None, "die Verschiebung noch einmal in dieselbe Richtung ausgeführt"),
         ([(2, 4)], None, "nur den ersten Schritt umgekehrt")],
        "(2 | 0)")
assert (Q_[0] + 3, Q_[1] - 2) == (2, 0)
pruef_menge(a, [(2, 0)], lambda x, y: (x - 3, y + 2) == Q_)

# ───────────────────────── Flug Klasse 8: funktionen.linear (Neumayer-Station III) ─────────────────────────

# G1 – Gerade zeichnen, m = 1/2
a = neu("G1", 8, "graph_ablesen", 1, "direkt",
        "Zeichne die Gerade y = (1/2)x − 1. Setze zwei Gitterpunkte der Geraden.",
        koord(-4, 6, -5, 5), {"anzahl": 2, "verbinden": "gerade"},
        {"regel": "gerade", "durch": [[0, -1], [2, 0]]},
        "Starte bei t auf der y-Achse. m = 1/2 heißt: 2 nach rechts, 1 nach oben.",
        "Start (0 | −1). 2 nach rechts, 1 nach oben: (2 | 0). Jeder weitere Schritt gibt wieder einen Gitterpunkt.",
        "Einsetzen: x = 0 ⇒ y = −1; x = 2 ⇒ y = 1 − 1 = 0.",
        "Ab (0 | −1) im Steigungsdreieck (2 | 1) laufen: (−4 | −3), (−2 | −2), (0 | −1), (2 | 0), (4 | 1), (6 | 2).",
        [([(0, -1), (1, 1)], "ein_punkt", "Steigungsdreieck gekippt: 1 nach rechts, 2 nach oben"),
         ([(0, 1), (2, 2)], "verschoben", "Vorzeichen von t übersehen: bei +1 gestartet")],
        "durch (0 | −1) und (2 | 0)")
pruef_gerade(a, lambda x, y: 2 * y == x - 2, (0, -1), (2, 1))

# G2 – am Graphen rückwärts ablesen
a = neu("G2", 8, "graph_ablesen", 1, "erkennen",
        "Der Graph von f ist gezeichnet. Setze den Punkt des Graphen, der die y-Koordinate −3 hat.",
        koord(-4, 6, -5, 5, graphen=[{"art": "linear", "m": -1.5, "t": 3, "name": "f"}]), {"anzahl": 1},
        {"regel": "menge", "punkte": [[4, -3]]},
        "Such auf der y-Achse die −3 und geh waagrecht bis zum Graphen.",
        "Auf Höhe −3 trifft die waagrechte Linie den Graphen bei x = 4: (4 | −3).",
        "f(x) = −1,5x + 3 = −3 ⇒ −1,5x = −6 ⇒ x = 4.",
        "Alle Gitterpunkte durchsucht: nur (4 | −3) liegt auf dem Graphen und hat y = −3. Gelaufen: von (0 | 3) drei Dreiecke „2 rechts, 3 runter“: (2 | 0), (4 | −3).",
        [([(2, 0)], None, "die Nullstelle gesetzt (y = 0 statt y = −3)"),
         ([(-3, 4)], "vertauscht", "−3 als x-Koordinate gelesen und den Punkt daneben gesetzt")],
        "(4 | −3)")
assert (0 + 2 * 2, 3 - 2 * 3) == (4, -3)
pruef_menge(a, [(4, -3)], lambda x, y: y == -3 and 2 * y == -3 * x + 6)

# G3 – erst nach y auflösen
a = neu("G3", 8, "graph_ablesen", 2, "mehrschritt",
        "Zeichne die Gerade 3x + 2y = 8. Setze zwei Gitterpunkte der Geraden.",
        koord(-3, 7, -5, 5), {"anzahl": 2, "verbinden": "gerade"},
        {"regel": "gerade", "durch": [[0, 4], [2, 1]]},
        "Löse zuerst nach y auf. Oder such zwei Punkte, bei denen die Rechnung aufgeht, zum Beispiel x = 0.",
        "2y = −3x + 8, also y = −1,5x + 4. Start (0 | 4), dann 2 nach rechts und 3 nach unten: (2 | 1), (4 | −2), (6 | −5).",
        "Auflösen: y = −(3/2)x + 4; ab (0 | 4) im Dreieck „2 rechts, 3 runter“ laufen.",
        "Alle Gitterpunkte in 3x + 2y = 8 eingesetzt: (0 | 4), (2 | 1), (4 | −2), (6 | −5) – dieselben Punkte.",
        [([(0, 4), (3, 2)], "ein_punkt", "Steigungsdreieck gekippt: 3 nach rechts, 2 nach unten"),
         ([(0, 4), (2, 7)], None, "liegt außerhalb des Bildes – kann nicht gesetzt werden")],
        "y = −1,5x + 4")
a["falsch"].pop()                                           # (2 | 7) liegt nicht im Bild; nur zur Dokumentation oben
pruef_gerade(a, lambda x, y: 3 * x + 2 * y == 8, (0, 4), (2, -3))

# G4 – zurück zur y-Achse laufen (Punkt und Steigung gegeben)
a = neu("G4", 8, "aufstellen", 2, "umkehr",
        "Eine Gerade hat die Steigung 2 und geht durch P(2 | 3). Setze den Punkt, in dem sie die y-Achse schneidet.",
        koord(-5, 5, -3, 7, punkte=[{"x": 2, "y": 3, "name": "P"}]), {"anzahl": 1, "verbinden": "gerade", "mit": [[2, 3]]},
        {"regel": "menge", "punkte": [[0, -1]]},
        "Von P zur y-Achse sind es 2 Schritte nach links. Wie weit geht es dabei nach unten?",
        "2 nach links, dabei 2 · 2 = 4 nach unten: 3 − 4 = −1. Die Gerade trifft die y-Achse in (0 | −1), also y = 2x − 1.",
        "Einsetzen: 3 = 2 · 2 + t ⇒ t = −1.",
        "Alle Gitterpunkte durchsucht: nur (0 | −1) liegt auf der y-Achse und hat zu P die Steigung 2. Gelaufen: (2 | 3) → (1 | 1) → (0 | −1).",
        [([(0, 7)], None, "nach links gegangen und dabei nach oben gezählt (3 + 4)"),
         ([(0, 3)], None, "waagrecht zur y-Achse gegangen: Steigung nicht benutzt")],
        "(0 | −1)")
assert 3 - 2 * 2 == -1 and 3 + 2 * 2 == 7
pruef_menge(a, [(0, -1)], lambda x, y: x == 0 and (3 - y) == 2 * (2 - x))

# G5 – Parallele
a = neu("G5", 8, "lage", 2, "darstellung",
        "g: y = (1/2)x + 1 ist gezeichnet. Zeichne die Parallele zu g durch P(2 | −2): Setze zwei Gitterpunkte.",
        koord(-4, 6, -5, 5, graphen=[{"art": "linear", "m": 0.5, "t": 1, "name": "g"}], punkte=[{"x": 2, "y": -2, "name": "P"}]),
        {"anzahl": 2, "verbinden": "gerade"},
        {"regel": "gerade", "durch": [[2, -2], [4, -1]]},
        "Parallel heißt: gleiche Steigung. Nimm das Steigungsdreieck von g und starte bei P.",
        "Gleiche Steigung 1/2: ab P 2 nach rechts, 1 nach oben: (4 | −1), (6 | 0). Gleichung: y = 0,5x − 3.",
        "t = y − m · x = −2 − 0,5 · 2 = −3, also y = 0,5x − 3.",
        "Ab P im Dreieck (2 | 1) laufen: (−4 | −5), (−2 | −4), (0 | −3), (2 | −2), (4 | −1), (6 | 0).",
        [([(2, -2), (3, 0)], "ein_punkt", "Steigung 2 statt 1/2 (Dreieck gekippt)"),
         ([(0, -1), (2, 0)], "verschoben", "parallel, aber nicht durch P")],
        "y = 0,5x − 3")
pruef_gerade(a, lambda x, y: 2 * y == x - 6, (2, -2), (2, 1))

# G6 – Sachsituation: Guthaben
tage = [F(9) - F(3, 2) * d for d in range(0, 11)]
assert tage.index(0) == 6 and F(9) / F(3, 2) == 6                      # Weg 2 (Tabelle) und Weg 1 (Division)
a = neu("G6", 8, "deuten", 2, "einkleidung",
        "Mia hat 9 € Guthaben. Jeden Tag werden 1,50 € abgebucht. Setze den Startpunkt und den Punkt, an dem das Guthaben aufgebraucht ist.",
        koord(0, 10, 0, 10, name_x="Tage", name_y="€"), {"anzahl": 2, "verbinden": "strecke"},
        {"regel": "menge", "punkte": [[0, 9], [6, 0]]},
        "Start: Tag 0. Aufgebraucht heißt: Guthaben 0 €. Nach wie vielen Tagen ist das?",
        "Start (0 | 9). 9 : 1,5 = 6 Tage, also (6 | 0). Dazwischen fällt die Strecke gleichmäßig: y = −1,5x + 9.",
        "9 − 1,5x = 0 ⇒ x = 9 : 1,5 = 6.",
        "Tag für Tag: 9 · 7,50 · 6 · 4,50 · 3 · 1,50 · 0 – nach 6 Tagen leer.",
        [([(9, 0), (0, 6)], "vertauscht", "Tage und Euro vertauscht (Achsen verwechselt)"),
         ([(0, 9), (9, 0)], None, "mit 1 € pro Tag gerechnet")],
        "(0 | 9) und (6 | 0)")
alle = raster_punkte(a["f"]["grafik"])
assert {p for p in alle if p[0] == 0 and p[1] == 9} == {(0, 9)}
assert {p for p in alle if p[1] == 0 and 2 * 9 - 3 * p[0] == 0} == {(6, 0)}

# G7 – Senkrechte
a = neu("G7", 8, "lage", 3, "verknuepfen",
        "g: y = 2x − 3 ist gezeichnet. Zeichne die Senkrechte zu g durch P(4 | 0): Setze zwei Gitterpunkte.",
        koord(-4, 6, -5, 5, graphen=[{"art": "linear", "m": 2, "t": -3, "name": "g"}], punkte=[{"x": 4, "y": 0, "name": "P"}]),
        {"anzahl": 2, "verbinden": "gerade"},
        {"regel": "gerade", "durch": [[4, 0], [2, 1]]},
        "Senkrecht: Die Steigungen ergeben malgenommen −1. Oder: Dreh das Steigungsdreieck von g um eine Vierteldrehung.",
        "m von g ist 2, also m = −1/2: 2 nach rechts, 1 nach unten. Ab P rückwärts: (2 | 1), (0 | 2). Gleichung: y = −0,5x + 2.",
        "m₂ = −1 : 2 = −0,5; t = 0 + 0,5 · 4 = 2.",
        "Richtungen (1 | 2) und (2 | −1): 1 · 2 + 2 · (−1) = 0, also rechter Winkel. Gelaufen ab P: (−4 | 4), (−2 | 3), (0 | 2), (2 | 1), (4 | 0), (6 | −1).",
        [([(4, 0), (5, -2)], "ein_punkt", "nur das Vorzeichen gedreht: Steigung −2"),
         ([(4, 0), (2, -1)], "ein_punkt", "nur den Kehrwert genommen: Steigung +1/2")],
        "y = −0,5x + 2")
assert 2 * F(-1, 2) == -1 and 1 * 2 + 2 * (-1) == 0
pruef_gerade(a, lambda x, y: 2 * y == -x + 4, (4, 0), (2, -1))

# G8 – Tarife: gleich teuer
x_s = F(3 - 1) / (F(1) - F(1, 2))
assert x_s == 4 and 3 + F(1, 2) * 4 == 1 + 4 == 5                     # Weg 1: Vorsprung : Aufholen, Probe
a = neu("G8", 8, "schnittpunkte", 3, "transfer",
        "Roller A kostet 3 € Grundpreis und 0,50 € pro Kilometer. Roller B kostet 1 € Grundpreis und 1 € pro Kilometer. Setze den Punkt, bei dem beide gleich viel kosten.",
        koord(0, 10, 0, 10, name_x="km", name_y="€"), {"anzahl": 1},
        {"regel": "menge", "punkte": [[4, 5]]},
        "B ist am Anfang 2 € billiger. Um wie viel holt A pro Kilometer auf?",
        "Vorsprung 2 €, A holt je km 0,50 € auf: 2 : 0,5 = 4 km. Preis: 3 + 2 = 5 € (und 1 + 4 = 5 €). Punkt (4 | 5).",
        "Vorsprung : Aufholen = (3 − 1) : (1 − 0,5) = 4; Preis 5 €.",
        "Alle Gitterpunkte durchsucht: nur (4 | 5) erfüllt beide Preisgleichungen y = 3 + 0,5x und y = 1 + x.",
        [([(2, 3)], None, "Vorsprung nur durch den Preis von B geteilt (2 : 1)"),
         ([(5, 4)], "vertauscht", "Kilometer und Euro vertauscht")],
        "(4 | 5)")
pruef_menge(a, [(4, 5)], lambda x, y: 2 * y == 6 + x and y == 1 + x)

# G9 – von der Nullstelle zurück
a = neu("G9", 8, "zwei_punkte", 3, "rueckwaerts",
        "Eine Gerade schneidet die x-Achse bei x = 6 und hat die Steigung −1/2. Zeichne sie: Setze zwei Gitterpunkte.",
        koord(-3, 7, -3, 7), {"anzahl": 2, "verbinden": "gerade"},
        {"regel": "gerade", "durch": [[6, 0], [0, 3]]},
        "Starte bei (6 | 0). Geh rückwärts: 2 nach links – geht es dann nach oben oder nach unten?",
        "Fallende Gerade: nach links geht es nach oben. Ab (6 | 0): (4 | 1), (2 | 2), (0 | 3). Also y = −0,5x + 3.",
        "0 = −0,5 · 6 + t ⇒ t = 3; y = −0,5x + 3.",
        "Ab (6 | 0) im Dreieck (−2 | +1) laufen: (4 | 1), (2 | 2), (0 | 3), (−2 | 4) – dieselben Punkte wie aus der Gleichung.",
        [([(6, 0), (0, -3)], "ein_punkt", "nach links gegangen und nach unten gezählt (Vorzeichen der Steigung)"),
         ([(0, 6), (2, 5)], "verschoben", "die 6 auf die y-Achse gesetzt")],
        "y = −0,5x + 3")
pruef_gerade(a, lambda x, y: 2 * y == -x + 6, (6, 0), (-2, 1))

# G10 – Parameter t bestimmen, dann zeichnen
a = neu("G10", 8, "aufstellen", 3, "parameter",
        "Für welches t geht die Gerade y = −x + t durch P(2 | 3)? Zeichne diese Gerade: Setze zwei Gitterpunkte.",
        koord(-3, 7, -3, 7, punkte=[{"x": 2, "y": 3, "name": "P"}]), {"anzahl": 2, "verbinden": "gerade"},
        {"regel": "gerade", "durch": [[0, 5], [5, 0]]},
        "Von P zur y-Achse: 2 nach links. Bei Steigung −1 geht es dabei 2 nach oben.",
        "Zurück zur y-Achse: 3 + 2 = 5, also t = 5 und y = −x + 5. Punkte zum Beispiel (0 | 5) und (5 | 0).",
        "3 = −2 + t ⇒ t = 5.",
        "Ab P im Dreieck (1 | −1) laufen: … (0 | 5), (1 | 4), (2 | 3), (3 | 2) … – bei allen ist x + y = 5.",
        [([(0, 1), (1, 0)], "verschoben", "t = 3 − 2 = 1 gerechnet (Vorzeichen beim Auflösen)"),
         ([(2, 3), (3, 4)], "ein_punkt", "Steigung +1 statt −1")],
        "y = −x + 5")
pruef_gerade(a, lambda x, y: x + y == 5, (2, 3), (1, -1))

# ───────────────────────── Prüfungen über alle 20 Aufgaben ─────────────────────────
assert len(AUFGABEN) == 20 and [a["klasse"] for a in AUFGABEN] == [5] * 10 + [8] * 10
STUFE = {"direkt": 1, "erkennen": 1, "mehrschritt": 2, "einkleidung": 2, "umkehr": 2, "darstellung": 2,
         "rueckwaerts": 3, "verknuepfen": 3, "begruenden": 3, "fehler": 3, "transfer": 3, "parameter": 3, "pruefung": 3}
for a in AUFGABEN:
    gr, sz, o = a["f"]["grafik"], a["f"]["setzen"], a["o"]
    assert STUFE[a["g"]] == a["s"], a["nr"]
    assert gr["x"][1] - gr["x"][0] <= MAX_SCHRITTE and gr["y"][1] - gr["y"][0] <= MAX_SCHRITTE, a["nr"]
    assert gr["x"][1] - gr["x"][0] == gr["y"][1] - gr["y"][0], (a["nr"], "Kästchen müssen quadratisch sein")
    # Lösung wird angenommen
    if o["regel"] == "menge":
        for m in (o.get("mengen") or [o["punkte"]]):
            assert len(m) == sz["anzahl"]
            assert bewerte(a, {"punkte": m}) == {"format_ok": True, "richtig": True}, a["nr"]
            assert bewerte(a, {"punkte": m[::-1]}) == {"format_ok": True, "richtig": True}       # Reihenfolge egal
    else:
        assert bewerte(a, {"punkte": o["durch"]}) == {"format_ok": True, "richtig": True}, a["nr"]
    # typische Fehler: werden abgelehnt, mit dem erwarteten Fehlermuster
    assert len(a["falsch"]) >= 1
    for fa in a["falsch"]:
        r = bewerte(a, {"punkte": fa["punkte"]})
        assert r["format_ok"] and r["richtig"] is False and r.get("grund") == fa["grund"], (a["nr"], fa, r)
    # Unsinn zählt nie als Fehler
    ok = (o.get("mengen") or [o.get("punkte")])[0] if o["regel"] == "menge" else o["durch"]
    unsinn = [None, {}, {"punkte": "x"}, {"punkte": []}, {"punkte": ok[:-1]}, {"punkte": ok + [[0, 0]]},
              {"punkte": [[0.3, 1]] * sz["anzahl"]}, {"punkte": [[99, 99]] + ok[1:]}, {"punkte": [["a", 1]] + ok[1:]},
              {"punkte": [[1]] + ok[1:]}, {"punkte": [[True, 1]] + ok[1:]}, {"punkte": [[float("nan"), 1]] + ok[1:]}]
    if sz["anzahl"] == 2:
        unsinn.append({"punkte": [ok[0], ok[0]]})
    for u in unsinn:
        assert bewerte(a, u)["format_ok"] is False, (a["nr"], u)
    # Regel „menge“: Die Lösung ist im Bild nicht schon als Punkt eingezeichnet
    if o["regel"] == "menge":
        gegeben = {(q["x"], q["y"]) for q in gr.get("punkte", [])}
        assert not gegeben & {tuple(p) for m in (o.get("mengen") or [o["punkte"]]) for p in m}, (a["nr"], "Lösung ist eingezeichnet")
    # typische Fehler liegen im Bild (sonst kann das Kind sie nicht setzen und die App sie nicht erkennen)
    for fa in a["falsch"]:
        assert all(gr["x"][0] <= x <= gr["x"][1] and gr["y"][0] <= y <= gr["y"][1] for x, y in fa["punkte"]), a["nr"]
    # Tipp verrät die Lösung nicht (keine Lösungskoordinate im Tipp)
    for m in ((o.get("mengen") or [o.get("punkte")]) if o["regel"] == "menge" else []):
        for x, y in m:
            assert f"({x} | {y})".replace("-", "−") not in a["h"], (a["nr"], "Tipp verrät die Lösung")
# keine zwei Aufgaben mit gleichem Satzbau (Zahlen ersetzt)
bau = [re.sub(r"[−-]?\d+([,/]\d+)?", "#", a["f"]["text"]) for a in AUFGABEN]
assert max(bau.count(b) for b in bau) <= 2, "gleicher Satzbau mehr als zweimal"
# Rate-Chance bei einem Punkt: 1 von 121
assert len(raster_punkte(G5())) == 121

# ───────────────────────── Befunde zur Arbeit des Vorgängers (Nachweise) ─────────────────────────
BEFUNDE = {}
# (1) D3-Regel „auf_gerade“ mit Toleranz 0,25: nimmt bei flachen Geraden falsche Gitterpunkte an.
m, t = F(1, 4), F(0)
falsch_angenommen = [(x, y) for x in range(-4, 5) for y in range(-4, 5) if 0 < abs(m * x + t - y) <= F(1, 4)]
assert (1, 0) in falsch_angenommen and len(falsch_angenommen) == 4
BEFUNDE["toleranz_0_25"] = f"y = x/4: {len(falsch_angenommen)} falsche Gitterpunkte gelten als richtig, z. B. (1 | 0)"
# (2) B4 Schritt 6 „x = Unterschied der t : Unterschied der m“ ohne Reihenfolge: falsches Vorzeichen.
m1, t1, m2, t2 = 2, 3, 1, 1                      # y = 2x + 3 und y = x + 1
x_richtig = F(t2 - t1, m1 - m2)
assert x_richtig == -2 and abs(t1 - t2) / abs(m1 - m2) == 2 and m1 * 2 + t1 != m2 * 2 + t2
BEFUNDE["b4_vorzeichen"] = "y = 2x + 3 und y = x + 1 schneiden sich bei x = −2; „Unterschied : Unterschied“ liefert 2"
# (3) R1: „Welche zwei Faktoren zuerst?“ – auch 17 · 3 zuerst führt zum geschickten Weg.
assert (17 * 3) * (4 * 25) == (4 * 25) * (17 * 3) == 5100
BEFUNDE["r1_zweite_loesung"] = "17 · 3 = 51 zuerst und dann 51 · 100 ist derselbe geschickte Weg – die Frage hat zwei vertretbare Antworten"
# (4) R4: Die Lösung liegt genau in der Mitte der Skala; R4 und L4 benutzen die Zahlen der Erklärung.
assert (0 + 20000) / 2 == 500 * 20 and 8000 <= 10000 <= 12000 and F(12000 - 8000, 20000) == F(1, 5)
BEFUNDE["r4_mitte"] = "Skalenmitte 10 000 = Überschlag; der richtige Bereich ist 1/5 der Skala"
# (5) Auswahl mit 4 Antworten und zweitem Versuch: Rate-Chance.
assert F(1, 4) + F(3, 4) * F(1, 3) == F(1, 2)
BEFUNDE["auswahl_raten"] = "1/4 + 3/4 · 1/3 = 1/2 (zählt im 2. Versuch nicht für die Serie, kostet aber auch nichts)"
# (6) Überschlag am Zahlenstrahl geht schon heute mit „markierung“: nächster Strich ist eindeutig.
striche = [i * 2000 for i in range(11)]
naechst = min(range(11), key=lambda i: abs(striche[i] - 487 * 21))
assert naechst == 5 and abs(striche[5] - 487 * 21) == 227 < 0.3 * 2000
BEFUNDE["markierung_heute"] = "487 · 21 = 10 227: nächster Strich Nr. 5 (10 000), Abstand 227 von 2 000 – eindeutig"
# (7) R4 Sicherheits-Wette „nur Bonus“: „sicher“ ist immer mindestens so gut wie jede andere Angabe.
for p_richtig in (F(1, 10), F(1, 2), F(9, 10)):
    assert p_richtig * 1 >= p_richtig * 0                      # Erwartungswert Bonus bei „sicher“ ≥ bei „geraten“
BEFUNDE["wette"] = "Bonus ohne Preis: „sicher“ anzugeben lohnt sich immer – die Angabe sagt dann nichts"

# ───────────────────────── Ausgabe ─────────────────────────
def schreibe(name, text):
    with open(os.path.join(ORDNER, name), "w", encoding="utf-8") as fh:
        fh.write(text)


def ersetze_block(name, marke, inhalt):
    pfad = os.path.join(ORDNER, name)
    if not os.path.exists(pfad):
        return False
    with open(pfad, encoding="utf-8") as fh:
        alt = fh.read()
    a, e = f"<!-- {marke}:ANFANG -->", f"<!-- {marke}:ENDE -->"
    if a not in alt or e not in alt:
        return False
    neu_text = alt[:alt.index(a) + len(a)] + "\n" + inhalt + "\n" + alt[alt.index(e):]
    with open(pfad, "w", encoding="utf-8") as fh:
        fh.write(neu_text)
    return True


schreibe("aufgaben-auftrag2.json", json.dumps(AUFGABEN, ensure_ascii=False, indent=1) + "\n")

# Entwurf: dieselben 20 Datensätze (ohne Zusatzfelder des Berichts)
daten = [{k: a[k] for k in ("nr", "klasse", "l", "s", "g", "f", "o", "h", "w")} for a in AUFGABEN]
html_ok = ersetze_block("entwurf-punkte.html", "DATEN",
                        "<script>const AUFGABEN = " + json.dumps(daten, ensure_ascii=False) + ";</script>")


def pk(punkte):
    return ", ".join(f"({x} | {y})".replace("-", "−") for x, y in punkte)


zeilen = []
for kl, titel in ((5, "Flug Klasse 5 – „Grundbegriffe und Figuren“ (`geometrie.grundbegriffe`, Kairo)"),
                  (8, "Flug Klasse 8 – „Lineare Funktionen“ (`funktionen.linear`, Neumayer-Station III)")):
    zeilen.append(f"### {titel}\n")
    for a in (x for x in AUFGABEN if x["klasse"] == kl):
        o, sz = a["o"], a["f"]["setzen"]
        stufe = {1: "leicht", 2: "mittel", 3: "schwer"}[a["s"]]
        if o["regel"] == "menge":
            regel = "`menge`"
        else:
            regel = "`gerade`"
        zeilen.append(f"**{a['nr']} · `{a['l']}` · {stufe} (`{a['g']}`) · Regel {regel}**  ")
        zeilen.append(f"Text: „{a['f']['text']}“  ")
        zeilen.append(f"Lösung: {a['kern']}" + ("" if o["regel"] == "menge" else " – je zwei verschiedene Gitterpunkte dieser Geraden") + "  ")
        zeilen.append(f"Weg 1: {a['probe']['weg1']}  ")
        zeilen.append(f"Weg 2: {a['probe']['weg2']}  ")
        fa = a["falsch"][0]
        zeilen.append(f"Häufigste falsche Antwort (Annahme): {pk(fa['punkte'])} – verrät: {fa['verraet']}"
                      + (f" (Fehlermuster `{fa['grund']}`)" if fa["grund"] else "") + "  ")
        zeilen.append(f"Tipp: {a['h']}\n")
md_ok = ersetze_block("auftrag2.md", "AUFGABEN", "\n".join(zeilen))
bsp = [json.dumps({k: a[k] for k in ("l", "p", "s", "g", "y", "f", "o", "h", "w")}, ensure_ascii=False)
       for a in AUFGABEN if a["nr"] in ("K4", "K8", "G1")]
ersetze_block("auftrag2.md", "BEISPIELE", "```json\n" + "\n".join(bsp) + "\n```")

print(f"OK: {len(AUFGABEN)} Aufgaben zweifach nachgerechnet, Prüfregel getestet "
      f"({sum(len(a['falsch']) for a in AUFGABEN)} typische Fehler, je 12–13 Unsinn-Antworten).")
print("Befunde:")
for k, v in BEFUNDE.items():
    print(f"  {k}: {v}")
print(f"geschrieben: aufgaben-auftrag2.json, entwurf-punkte.html {'aktualisiert' if html_ok else '(nicht gefunden)'}, "
      f"auftrag2.md {'aktualisiert' if md_ok else '(nicht gefunden)'}")
