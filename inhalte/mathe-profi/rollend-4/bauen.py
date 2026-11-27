"""Mathe-Profi, Auftrag „Vorrat in neuer Form“ (Aufgaben-Ersteller): rollend-4.

Aufruf: python3 -I inhalte/mathe-profi/rollend-4/bauen.py
Füllt je Lernkarte der 16 Flüge aus rollend-1, rollend-2 und rollend-3 den Vorrat an Aufgaben in neuer Form auf mindestens DREI
(Lückenweg, Fehler-Detektiv, Verfahren wählen, Zwei Wege vergleichen, Brücke; Antwortformen zahl, auswahl, luecken – keine „bedingung“).
Zählt zuerst den Bestand (rollend-1 bis rollend-3), schreibt je Flug eine Datei <flug>.json und endet mit „OK“, wenn alles stimmt.
Nur Inhalte. Nichts wird eingespielt.
"""
import itertools
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from fractions import Fraction as F

sys.dont_write_bytecode = True
if "--ueberschreiben" not in sys.argv:
    sys.exit("Nicht ausgeführt: Die Dateien <flug>.json sind seit 27.11. von Hand geändert (6 neue ge1-Aufgaben, 5 umgewandelte Aufgaben, siehe README). "
             "Dieses Programm würde sie überschreiben. Nur mit --ueberschreiben, dann gehen die Handänderungen verloren.")
HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
sys.path.insert(0, os.path.join(WURZEL, "tools"))
import inhalt_pruefen as ip      # noqa: E402

KENN = json.load(open(os.path.join(HIER, "..", "regeln-uebersicht", "kennungen.json"), encoding="utf-8"))["kennungen"]
REGELN = {e["kennung"]: e for e in KENN}
FEHLBILD = {f["kennung"]: e["kennung"] for e in KENN for f in e["fehlbilder"]}
PLAN = json.load(open(os.path.join(WURZEL, "inhalte", "plan", "rollend-einheiten.json"), encoding="utf-8"))

# kurz → Typ-Name wie in rollend-3 (die Zählung geht über den Anfang des Namens)
TYP = {"LW": "Lückenweg", "FD": "Fehler-Detektiv (einfache Form)", "VW": "Verfahren wählen (einfache Form)", "ZW": "Zwei Wege vergleichen", "BR": "Brücke"}
FORMEN = ["Lückenweg", "Fehler-Detektiv", "Verfahren wählen", "Zwei Wege vergleichen", "Brücke"]
STANDARD_G = {"LW": "direkt", "FD": "fehler", "VW": "mehrschritt", "ZW": "mehrschritt", "BR": "darstellung"}
# Flug: (Titel, Kind, Klasse, Runde, Themen-Dateien, Kürzel der Kennung, Lernkarten, die zu einem anderen Flug gehören)
FLUG = {
    "ge1": ("Formen und Grundbegriffe", "Kind 1", 5, 1, ["geometrie.grundbegriffe", "geometrie.ortslinien"], "GE1", set()),
    "z2": ("Teilbarkeit", "Kind 1", 5, 1, ["zahlen.teilbarkeit"], "Z2", set()),
    "ge2": ("Spiegeln und Symmetrie", "Kind 2", 7, 1, ["abbildungen.kongruenz"], "GE2", set()),
    "a4": ("Lineare Ungleichungen", "Kind 2", 8, 1, ["gleichungen.ungleichungen", "zahlen.intervalle"], "A4", set()),
    "a1": ("Einfache Gleichungen", "Kind 1", 5, 2, ["gleichungen.einfach"], "A1", set()),
    "d1": ("Daten darstellen", "Kind 1", 5, 2, ["daten.darstellen"], "D1", set()),
    "g1": ("Größen und Einheiten", "Kind 1", 5, 2, ["groessen.einheiten"], "G1", set()),
    "g8": ("Prozent mit verändertem Grundwert", "Kind 2", 7, 2, ["bruch.prozent_grundwert"], "G8", set()),
    "g2-teil2": ("Dreisatz · Teil 2", "Kind 2", 5, 2, ["groessen.proportional"], "G2T2", {"einheit", "dreisatz", "geschickt", "sach", "aenderung"}),
    "f1": ("Funktionsbegriff", "Kind 2", 8, 2, ["funktionen.grundbegriffe"], "F1", set()),
    "ge3": ("Winkel", "Kind 1", 5, 3, ["geometrie.winkel"], "GE3", set()),
    "r1": ("Umfang und Fläche", "Kind 1", 5, 3, ["messen.flaechen"], "R1", set()),
    "g2": ("Dreisatz und direkte Proportionalität (Teil 1)", "Kind 1", 5, 3, ["groessen.proportional"], "G2", {"erkennen", "vervielfachen", "pruefen"}),
    "ge4": ("Dreiecke, Vierecke und Konstruktion", "Kind 2", 7, 3, ["geometrie.winkelsaetze", "geometrie.konstruktion"], "GE4", set()),
    "f2": ("Lineare Funktionen", "Kind 2", 8, 3, ["funktionen.linear"], "F2", set()),
    "a6": ("Gleichungssysteme", "Kind 2", 8, 3, ["gleichungen.lgs2"], "A6", set()),
}
# Lernkarten, die die Zuordnung Lernziel → Einheit der Datenbank nicht eindeutig lösen kann (gleiches Lernziel in zwei Einheiten des Flugs)
ZURUECKGESTELLT = {("ge1", "geometrie.grundbegriffe", "verstehen"), ("ge1", "geometrie.ortslinien", "verstehen")}

THEMA = {}       # Thema -> Datei
KARTE = {}       # (Thema, Lernkarte) -> Teilfähigkeit
BESTAND_TEXT = defaultdict(set)    # Thema -> Fragetexte des Bestands
BESTAND_BAU = defaultdict(set)     # Thema -> Fragetexte ohne Zahlen
ZAHL = re.compile(r"[−-]?\d+(?:[  ]\d{3})*(?:[,.]\d+)?")
bau_ohne_zahl = lambda t: re.sub(r"\s+", " ", ZAHL.sub("#", t)).strip()
for _fl in FLUG.values():
    for _t in _fl[4]:
        THEMA[_t] = json.load(open(os.path.join(WURZEL, "inhalte", "themen", _t + ".json"), encoding="utf-8"))
        for _a in THEMA[_t]["aufgaben"]:
            KARTE.setdefault((_t, _a["l"]), _a["t"])
            BESTAND_TEXT[_t].add(_a["f"].get("text", ""))
            BESTAND_BAU[_t].add(bau_ohne_zahl(_a["f"].get("text", "")))


def karten_von(flug):
    return [(t, e["lernziel"]) for t in FLUG[flug][4] for e in THEMA[t]["inhalt"]["etappen"] if e["lernziel"] not in FLUG[flug][6]]


VORHANDEN = {}       # Flug -> Liste der Einträge aus rollend-1 bis rollend-3
for _f, _fl in FLUG.items():
    _d = json.load(open(os.path.join(HIER, "..", f"rollend-{_fl[3]}", f"{_f}.json"), encoding="utf-8"))
    VORHANDEN[_f] = _d["aufgaben"]

A = []
POSITION = {3: itertools.cycle([1, 0, 2, 2, 0, 1]), 4: itertools.cycle([2, 0, 3, 1, 1, 3, 0, 2])}


def z2(ausdruck):
    genau = re.sub(r"(?<![\w.])(\d+)(?![\w.])", r"F(\1)", ausdruck)
    return F(eval(genau, {"__builtins__": {}}, {"F": F, "abs": abs, "min": min, "max": max}))


def neu(flug, l, typ, bau, g=None, regel=None, thema=None):
    """typ: LW, FD, VW, ZW, BR. g: Aufgabentyp (Standard je Typ); die Stufe folgt aus g. regel: Standard = die Regel, die der Bestand des Flugs für diese Lernkarte nutzt."""
    themen = [t for t in FLUG[flug][4] if (t, l) in KARTE and (thema is None or t == thema)]
    assert len(themen) == 1, (flug, l, themen)
    if regel is None:
        regel = Counter(e["regel"] for e in VORHANDEN[flug] if e["aufgabe"]["l"] == l).most_common(1)[0][0]
    g = g or STANDARD_G[typ]
    aufgabe, zweit, fb = bau
    A.append(dict(flug=flug, thema=themen[0], typ=typ, regel=regel, zaehlt="nein" if typ == "LW" else "ja", s=ip.STUFE_VON[g],
                  aufgabe={"l": l, "t": KARTE[(themen[0], l)], "p": "uebung", "s": ip.STUFE_VON[g], "g": g, **aufgabe}, zweit=zweit, fb=fb))


def mit(d, grafik):
    if grafik:
        d["f"]["grafik"] = grafik
    return d


def L(text, schablone, werte, c, zweit, h, w, fb=None, hinweis="Je Lücke eine ganze Zahl.", grafik=None):
    """Lücken. fb: {Nummer der Lücke ab 0: [(falscher Wert, Fehlbild-Kennung oder None, Beschreibung)]}"""
    return mit({"y": "luecken", "f": {"text": text, "schablone": schablone, "hinweis": hinweis}, "o": {"werte": werte}, "c": c, "h": h, "w": w}, grafik), zweit, fb or {}


def Z(text, wert, c, zweit, h, w, fb, einheit=None, grafik=None):
    """Zahl. fb: [(falscher Wert, Fehlbild-Kennung oder None, Beschreibung)]"""
    return mit({"y": "zahl", "f": {"text": text}, "o": {"wert": wert, **({"einheit": einheit} if einheit else {})}, "c": c, "h": h, "w": w}, grafik), [zweit] if isinstance(zweit, str) else zweit, fb


def W(text, richtig, falsch, h, w, probe, grafik=None):
    """Auswahl. falsch: [(Antwort, Beschreibung)] oder [(Antwort, Beschreibung, Fehlbild-Kennung)]. Die richtige Antwort wandert reihum an andere Plätze."""
    n = len(falsch) + 1
    assert n in (3, 4), text
    p = next(POSITION[n])
    antworten = [f[0] for f in falsch]
    antworten.insert(p, richtig)
    fb = {}
    for i, f in enumerate(falsch):
        fb[i if i < p else i + 1] = (f[2] if len(f) > 2 else None, f[1])
    return mit({"y": "auswahl", "f": {"text": text}, "a": antworten, "o": {"index": p}, "h": h, "w": w}, grafik), probe, fb


K = lambda n: "; ".join(f"{'①②③④⑤'[i]} = □" for i in range(n))
TAB = lambda kopf, *zeilen: {"typ": "tabelle", "kopf": kopf, "zeilen": [list(z) for z in zeilen]}
KO = lambda x, y, **mehr: {"typ": "koordinaten", "x": x, "y": y, **mehr}
GZ = "Je Lücke eine ganze Zahl (mit Minus, falls negativ)."


def FDZ(einleitung, zeilen, h, w, frage="In welcher Zeile steckt der Fehler?", grafik=None):
    """Fehler-Detektiv mit Zeilen. zeilen: [(Text, stimmt)] – das Programm prüft, dass genau eine Zeile nicht stimmt. Die Antworten stehen in der Reihenfolge der Zeilen."""
    falsche = [i for i, (_, ok) in enumerate(zeilen) if not ok]
    assert len(falsche) == 1 and 3 <= len(zeilen) <= 4, (einleitung, falsche)
    text = einleitung + " " + " ".join(f"Zeile {i + 1}: {t}" for i, (t, _) in enumerate(zeilen)) + " " + frage
    ant = [f"In Zeile {i + 1}" for i in range(len(zeilen))]
    fb = {i: (None, "diese Zeile ist richtig; der Fehler steckt woanders") for i in range(len(zeilen)) if i != falsche[0]}
    return mit({"y": "auswahl", "f": {"text": text}, "a": ant, "o": {"index": falsche[0]}, "h": h, "w": w}, grafik), lambda: True, fb

# ═════════════════════ Kind 1 · Flug ge1 · Formen und Grundbegriffe ═════════════════════
f = "ge1"
ABST, WINK, DECK, RW = "id.geometrie.abstand", "id.geometrie.winkel", "id.geometrie.deckungsgleich", "id.geometrie.rechtwinklig"
# koordinaten
neu(f, "koordinaten", "FD", FDZ("Kim soll den Punkt P(−3 | 5) im Koordinatensystem finden.",
    [("Sie startet im Ursprung (0 | 0).", True), ("Die erste Zahl ist −3. Sie geht 3 Einheiten nach rechts.", -3 > 0), ("Die zweite Zahl ist 5. Sie geht 5 Einheiten nach oben.", 5 > 0)],
    "Eine negative erste Zahl heißt: in welche Richtung?", "Die erste Zahl ist −3, also negativ. Negativ heißt links. Richtig: 3 Einheiten nach links."))
neu(f, "koordinaten", "VW", W("Der Punkt A hat die Koordinaten (2 | 1). Der Punkt R liegt 3 Einheiten rechts von A und 4 Einheiten unter A. Welche Rechnung gibt die Koordinaten von R?",
    "x: 2 + 3 = 5 und y: 1 − 4 = −3, also R(5 | −3)",
    [("x: 2 − 3 = −1 und y: 1 + 4 = 5, also R(−1 | 5)", "rechts mit links und oben mit unten verwechselt"), ("x: 3 + 4 = 7 und y: 2 + 1 = 3, also R(7 | 3)", "alle Zahlen vermischt"), ("x: 1 − 4 = −3 und y: 2 + 3 = 5, also R(−3 | 5)", "x und y vertauscht")],
    "Rechts verändert die erste Zahl, oben und unten die zweite.", "Rechts: x wird größer, 2 + 3 = 5. Unten: y wird kleiner, 1 − 4 = −3. R(5 | −3).",
    lambda: (2 + 3, 1 - 4) == (5, -3) and (2 - 3, 1 + 4) != (5, -3) and (3 + 4, 2 + 1) != (5, -3) and (1 - 4, 2 + 3) != (5, -3)), g="mehrschritt")
# strecken
neu(f, "strecken", "FD", FDZ("Kim berechnet die Länge der Strecke [AB] mit A(−4 | 3) und B(5 | 3).",
    [("A und B haben beide y = 3. Die Strecke liegt waagrecht.", True), ("Die y-Achse liegt zwischen A und B. Kim rechnet 5 − 4 = 1.", 5 - 4 == 4 + 5), ("Die Strecke [AB] ist 1 Einheit lang.", True)],
    "Liegt die 0 zwischen den Punkten, was musst du dann tun?", "Die y-Achse liegt zwischen A und B. Dann addierst du die Teile: 4 + 5 = 9. Richtig: 9 Einheiten."))
# lagebeziehungen
neu(f, "lagebeziehungen", "LW", L("Die senkrechte Linie g geht durch (4 | 0). Der Punkt P(9 | 2) hat von g den Abstand 9 − 4 = ① Einheiten. Die senkrechte Linie h geht durch (−1 | 0). Von P bis h sind es 9 − (−1) = ② Einheiten.",
    K(2), [5, 10], ["9 - 4", "9 - (-1)"], ["abs(4 - 9)", "9 + 1"], "Rechne die x-Koordinaten gegeneinander. Minus minus bedeutet plus.", "9 − 4 = 5. 9 − (−1) = 9 + 1 = 10.",
    {1: [(8, "fb.plusminus.zeichen_des_ergebnisses", "bei „minus minus“ das Vorzeichen übersehen")]}, hinweis=GZ))
neu(f, "lagebeziehungen", "FD", FDZ("Kim soll den Abstand des Punktes P(2 | 7) von der waagrechten Linie g durch (0 | 3) bestimmen.",
    [("Der Abstand ist die Länge des Lots von P auf g.", True), ("Das Lot steht senkrecht auf g. Es verläuft also in y-Richtung.", True), ("Kim rechnet 2 − 3 = −1. Ein Abstand ist nie negativ, also ist er 1.", 2 - 3 == 7 - 3)],
    "Welche Koordinate von P gehört zur Höhe?", "Das Lot verläuft in y-Richtung, also zählen die y-Werte: 7 und 3. Abstand: 7 − 3 = 4."))
neu(f, "lagebeziehungen", "VW", W("Der Punkt P(−3 | 4) und die senkrechte Linie g durch (5 | 0) sind gegeben. Welche Rechnung gibt den Abstand von P zu g?",
    "5 − (−3) = 8",
    [("5 − 3 = 2", "das Minus bei −3 übersehen", "fb.plusminus.zeichen_des_ergebnisses"), ("5 + 4 = 9", "x-Wert von g mit y-Wert von P gerechnet"), ("4 − 0 = 4", "die y-Werte statt der x-Werte genommen")],
    "g ist senkrecht. In welche Richtung misst du dann den Abstand?", "Das Lot auf eine senkrechte Linie verläuft waagrecht. Es zählen die x-Werte: 5 − (−3) = 8.",
    lambda: abs(5 - (-3)) == 8 and 5 - 3 != 8 and 5 + 4 != 8 and 4 - 0 != 8), g="mehrschritt")
# kreis_lage
neu(f, "kreis_lage", "LW", L("Ein Kreis hat den Radius 5 cm. Die Gerade g hat vom Mittelpunkt den Abstand 3 cm. Das ist kleiner als der Radius: g und der Kreis haben ① gemeinsame Punkte. Bei dem Abstand 5 cm wären es ② Punkt. Bei dem Abstand 8 cm wären es ③ Punkte.",
    K(3), [2, 1, 0], ["2", "1", "0"], ["1 + 1", "3 - 2", "5 - 5"], "Sekante, Tangente, Passante: Wie viele gemeinsame Punkte hat jede?", "Sekante: 2 Punkte. Tangente: 1 Punkt. Passante: 0 Punkte.",
    {0: [(1, None, "mit einer Tangente verwechselt")], 2: [(2, None, "eine Passante für eine Sekante gehalten")]}, hinweis=GZ), regel=ABST)
neu(f, "kreis_lage", "FD", FDZ("Ein Kreis hat den Radius 4 cm. Die Gerade g ist 7 cm vom Mittelpunkt entfernt. Kim sagt, was g für den Kreis ist.",
    [("Ich vergleiche den Abstand 7 cm mit dem Radius 4 cm.", True), ("7 ist größer als 4.", 7 > 4), ("Also ist g eine Sekante und hat 2 Punkte mit dem Kreis gemeinsam.", 7 < 4)],
    "Ist der Abstand größer als der Radius, erreicht g den Kreis?", "7 cm ist größer als 4 cm: g erreicht den Kreis nicht. g ist eine Passante und hat 0 gemeinsame Punkte."))
# winkelarten
neu(f, "winkelarten", "LW", L("Ein Winkel hat 250°. Ein gestreckter Winkel hat ①°. Der Winkel ist ②° größer als ein gestreckter Winkel. Deshalb heißt er überstumpf.",
    K(2), [180, 70], ["180", "250 - 180"], ["90 * 2", "250 - 90 - 90"], "Ein gestreckter Winkel ist eine gerade Linie.", "Gestreckt: 180°. 250° − 180° = 70°. Größer als 180° heißt überstumpf.",
    {0: [(90, None, "mit einem rechten Winkel verwechselt"), (360, None, "mit dem Vollwinkel verwechselt")]}, hinweis=GZ), regel=WINK)
neu(f, "winkelarten", "FD", FDZ("Kim ordnet Winkel nach ihrer Art.",
    [("90° ist ein rechter Winkel.", True), ("135° ist stumpf, denn er liegt zwischen 90° und 180°.", 90 < 135 < 180), ("300° ist stumpf, denn er ist größer als 90°.", 300 < 180)],
    "Wo hört „stumpf“ auf?", "Stumpf sind Winkel zwischen 90° und 180°. 300° ist größer als 180°, also überstumpf."))
# vierecke
neu(f, "vierecke", "LW", L("Ein Parallelogramm hat zwei Paare gleich langer Gegenseiten: 9 cm und 5 cm. Alle vier Seiten zusammen: 2 · 9 + 2 · 5 = ① cm. Ein Rechteck hat ② rechte Winkel.",
    K(2), [28, 4], ["2 * 9 + 2 * 5", "4"], ["9 + 5 + 9 + 5", "2 + 2"], "Jede Länge kommt zweimal vor.", "18 + 10 = 28 cm. Ein Rechteck hat vier rechte Winkel.",
    {0: [(14, None, "jede Länge nur einmal gezählt")], 1: [(2, None, "nur zwei rechte Winkel gezählt")]}, hinweis=GZ), regel=DECK)
def _rechteck_ist_quadrat(a, b):
    return a == b
neu(f, "vierecke", "FD", FDZ("Kim sortiert Vierecke.",
    [("Ein Quadrat hat vier gleich lange Seiten und vier rechte Winkel.", True), ("Jedes Quadrat hat vier rechte Winkel, also ist jedes Quadrat auch ein Rechteck.", True),
     ("Jedes Rechteck hat vier rechte Winkel, also ist jedes Rechteck auch ein Quadrat.", _rechteck_ist_quadrat(8, 3)), ("Eine Raute hat vier gleich lange Seiten.", True)],
    "Denk an ein Rechteck, das 8 cm lang und 3 cm breit ist.", "Ein Rechteck von 8 cm mal 3 cm hat vier rechte Winkel, aber keine vier gleich langen Seiten. Es ist kein Quadrat."))
# kreislinie (Ortslinien)
neu(f, "kreislinie", "LW", L("Ein Kreis hat den Mittelpunkt M(1 | 3) und den Radius 4. Der Punkt P(1 | 10) liegt senkrecht über M. Sein Abstand zu M ist 10 − 3 = ①. Der Punkt Q(1 | 5) liegt auch senkrecht über M. Sein Abstand zu M ist 5 − 3 = ②.",
    K(2), [7, 2], ["10 - 3", "5 - 3"], ["3 + 4", "7 - 5"], "Beide Punkte haben dieselbe x-Koordinate wie M. Es zählt nur die Höhe.", "10 − 3 = 7: P liegt außerhalb (7 > 4). 5 − 3 = 2: Q liegt innerhalb (2 < 4).",
    {0: [(13, None, "die Höhen addiert")]}, hinweis=GZ))
neu(f, "kreislinie", "FD", FDZ("Gesucht sind alle Punkte auf der x-Achse, die von M(2 | 0) den Abstand 5 haben. Kim rechnet.",
    [("Es gibt zwei Punkte: einen rechts von M und einen links von M.", True), ("Rechts: x = 2 + 5 = 7.", 2 + 5 == 7), ("Links: x = 5 − 2 = 3.", 5 - 2 == 2 - 5)],
    "Links von M wird der x-Wert kleiner. Von welcher Zahl gehst du aus?", "Links von M geht es von 2 aus nach links: x = 2 − 5 = −3. Kim hat die Zahlen vertauscht."))
neu(f, "kreislinie", "VW", W("Ein Kreis um M(2 | 2) hat den Radius 5. Wie findest du heraus, ob der Punkt P(7 | 2) auf der Kreislinie liegt?",
    "Abstand 7 − 2 = 5 berechnen: gleich dem Radius, also auf der Kreislinie",
    [("7 + 2 = 9 rechnen: 9 ist größer als 5, also außerhalb", "die Koordinaten addiert statt den Abstand zu bilden"), ("7 − 5 = 2 rechnen: gleich der y-Koordinate, also innerhalb", "Radius vom x-Wert abgezogen und mit y verglichen"), ("2 + 2 = 4 rechnen: 4 ist kleiner als 5, also innerhalb", "nur die Koordinaten von M benutzt")],
    "P und M haben dieselbe Höhe. Wie groß ist ihr Abstand?", "P und M liegen auf einer Höhe. Der Abstand ist 7 − 2 = 5. Das ist gleich dem Radius: P liegt auf der Kreislinie.",
    lambda: 7 - 2 == 5 and 7 + 2 != 5 and 2 + 2 < 5), g="mehrschritt")
# parallelen
neu(f, "parallelen", "LW", L("Die waagrechte Linie g geht durch (0 | 4). Alle Punkte mit dem Abstand 3 von g liegen auf zwei Parallelen. Die obere geht durch y = 4 + 3 = ①. Die untere geht durch y = 4 − 3 = ②.",
    K(2), [7, 1], ["4 + 3", "4 - 3"], ["10 - 3", "2 - 1"], "Eine Parallele liegt über g, eine unter g.", "Oben: 4 + 3 = 7. Unten: 4 − 3 = 1.",
    {1: [(12, None, "3 mit 4 multipliziert")]}, hinweis=GZ))
neu(f, "parallelen", "FD", FDZ("g ist die senkrechte Linie durch (5 | 0). Gesucht sind alle Punkte mit dem Abstand 2 von g. Kim rechnet.",
    [("Die Punkte liegen auf zwei senkrechten Parallelen zu g.", True), ("Die rechte Parallele geht durch x = 5 + 2 = 7.", 5 + 2 == 7), ("Die linke Parallele geht durch x = 5 + 2 = 3.", 5 + 2 == 3)],
    "Die linke Parallele liegt links von g. Wird x dort größer oder kleiner?", "Links wird x kleiner: x = 5 − 2 = 3. Kim hat plus statt minus gerechnet."))
neu(f, "parallelen", "VW", W("Die waagrechte Linie g geht durch (0 | 2). Welche Punkte haben von g höchstens den Abstand 3?",
    "alle Punkte mit y von −1 bis 5 (ein Streifen um g)",
    [("nur die Punkte mit y = −1 oder y = 5 (zwei Linien)", "„genau“ statt „höchstens“ gelesen"), ("alle Punkte mit y von 2 bis 5 (nur über g)", "nur eine Seite von g gedacht"), ("alle Punkte mit y von −3 bis 3", "vom Ursprung statt von g gemessen")],
    "„Höchstens 3“ heißt: 3 oder weniger. Auf beiden Seiten von g.", "Von g aus 3 nach oben (2 + 3 = 5) und 3 nach unten (2 − 3 = −1): der Streifen von y = −1 bis y = 5.",
    lambda: (2 - 3, 2 + 3) == (-1, 5) and all(abs(y - 2) <= 3 for y in range(-1, 6)) and abs(-3 - 2) > 3), g="mehrschritt")
# zwei_kreise
neu(f, "zwei_kreise", "LW", L("Ein Kreis um A(1 | 0) hat den Radius 4. Ein Kreis um B(9 | 0) hat den Radius 6. Der Abstand AB ist 9 − 1 = ①. Die beiden Radien zusammen: 4 + 6 = ②. Der Abstand AB ist kleiner als die Radien zusammen und größer als ihr Unterschied. Die Kreise schneiden sich in ③ Punkten.",
    K(3), [8, 10, 2], ["9 - 1", "4 + 6", "2"], ["9 + 1 - 2", "5 * 2", "1 + 1"], "Zähle die Schnittpunkte von zwei Kreislinien, die sich durchdringen.", "AB = 8, Radiensumme 10. Dazwischen schneiden sich die Kreise in zwei Punkten.",
    {0: [(10, "fb.plusminus.zeichen_des_ergebnisses", "die Koordinaten addiert")], 2: [(1, None, "mit einer Berührung verwechselt")]}, hinweis=GZ))
neu(f, "zwei_kreise", "FD", FDZ("Ein Kreis um A(0 | 0) hat den Radius 2. Ein Kreis um B(10 | 0) hat den Radius 3. Kim prüft, ob sie sich schneiden.",
    [("Der Abstand AB ist 10.", True), ("Die beiden Radien zusammen sind 2 + 3 = 5.", 2 + 3 == 5), ("5 ist kleiner als 10, also schneiden sich die Kreise in 2 Punkten.", 5 >= 10)],
    "Reichen die beiden Radien zusammen von A bis B?", "Die Radien reichen zusammen nur 5 weit, der Abstand ist 10. Die Kreise erreichen sich nicht: 0 Schnittpunkte."))
neu(f, "zwei_kreise", "VW", W("Zwei Kreise haben die Radien 3 cm und 4 cm. Wie weit sind die Mittelpunkte voneinander entfernt, wenn sich die Kreise von außen in genau einem Punkt berühren?",
    "7 cm (3 + 4)",
    [("1 cm (4 − 3)", "den Fall „einer liegt im anderen“ erwischt"), ("12 cm (3 · 4)", "die Radien multipliziert"), ("3,5 cm (der Mittelwert)", "den Mittelwert statt der Summe genommen")],
    "Bei einer Berührung von außen liegen die Kreise nebeneinander. Wie lang ist der Weg von Mittelpunkt zu Mittelpunkt?", "Von M₁ bis zum Berührpunkt sind es 3 cm, von dort bis M₂ weitere 4 cm: 3 + 4 = 7 cm.",
    lambda: 3 + 4 == 7 and 4 - 3 != 7 and 3 * 4 != 7 and (3 + 4) / 2 != 7), g="mehrschritt")
# verknuepfen
neu(f, "verknuepfen", "LW", L("Ein Kreis hat den Mittelpunkt M(1 | 7) und den Radius 5. Die senkrechte Linie g geht durch x = 4. Ihr Abstand zu M ist 4 − 1 = ①. Das ist kleiner als der Radius. Also hat g mit dem Kreis ② gemeinsame Punkte. Die senkrechte Linie h geht durch x = 10. Ihr Abstand zu M ist 10 − 1 = ③. Das ist größer als der Radius. Also hat h mit dem Kreis ④ gemeinsame Punkte.",
    K(4), [3, 2, 9, 0], ["4 - 1", "2", "10 - 1", "0"], ["1 + 2", "1 + 1", "3 * 3", "5 - 5"], "Abstand kleiner als der Radius: zwei Punkte. Größer: kein Punkt.", "4 − 1 = 3 < 5: zwei Punkte. 10 − 1 = 9 > 5: kein Punkt.",
    {1: [(1, None, "mit einer Tangente verwechselt")], 3: [(2, None, "auch bei großem Abstand zwei Punkte gezählt")]}, hinweis=GZ), regel=ABST)
neu(f, "verknuepfen", "FD", FDZ("Der Kreis um M(3 | 0) hat den Radius 2. Gesucht sind die Schnittpunkte mit der x-Achse (y = 0). Kim rechnet.",
    [("Die x-Achse geht durch M. Es gibt also zwei Schnittpunkte.", True), ("Der eine liegt 2 Einheiten rechts von M: x = 3 + 2 = 5.", 3 + 2 == 5), ("Der andere liegt 2 Einheiten links von M: x = 2 − 3 = −1.", 2 - 3 == 3 - 2)],
    "Links von M geht es von 3 aus um 2 nach links.", "Links von M: x = 3 − 2 = 1. Kim hat 2 − 3 gerechnet und die Zahlen vertauscht."), regel=ABST)
neu(f, "verknuepfen", "VW", W("Der Kreis um M(0 | 0) hat den Radius 5. Die senkrechte Linie g geht durch (5 | 0). Wie viele Punkte haben Kreis und g gemeinsam?",
    "genau einen: der Abstand von M zu g ist 5, gleich dem Radius",
    [("zwei: g geht durch den Kreis hindurch", "Tangente für eine Sekante gehalten"), ("keinen: g ist größer als der Radius", "den Abstand 5 für „zu weit“ gehalten"), ("unendlich viele: g und der Kreis liegen übereinander", "Gerade und Kreis verwechselt")],
    "Wie weit ist g von M entfernt? Vergleiche mit dem Radius.", "Abstand von M zu g: 5. Radius: 5. Gleich: g berührt den Kreis in genau einem Punkt, (5 | 0).",
    lambda: [(5, y) for y in range(-6, 7) if 5 ** 2 + y ** 2 == 5 ** 2] == [(5, 0)]), g="mehrschritt", regel=ABST)
# sachsituationen
neu(f, "sachsituationen", "LW", L("Ein Hund ist mit einer 4 m langen Leine an einen Pfahl gebunden. Der Pfahl steht 10 m von der Straße entfernt. Der Hund kommt bis auf 10 − 4 = ① m an die Straße heran. Wäre die Leine 12 m lang, ragte der Kreis 12 − 10 = ② m über die Straße hinaus.",
    K(2), [6, 2], ["10 - 4", "12 - 10"], ["4 + 2", "1 + 1"], "Die Leine ist der Radius des Kreises.", "10 − 4 = 6 m bleiben bis zur Straße. 12 − 10 = 2 m zu viel.",
    {0: [(14, None, "Leine und Abstand addiert")]}, hinweis=GZ))
neu(f, "sachsituationen", "FD", FDZ("Ein Rasensprenger steht 5 m von einem Zaun entfernt. Er spritzt 3 m weit. Kim fragt, ob der Zaun nass wird.",
    [("Die nasse Fläche ist ein Kreis um den Sprenger mit dem Radius 3 m.", True), ("Der Zaun ist 5 m entfernt. Das ist mehr als 3 m.", 5 > 3), ("Also wird der Zaun nass.", 5 <= 3)],
    "Wie weit reicht das Wasser höchstens?", "Das Wasser reicht höchstens 3 m weit, der Zaun ist 5 m weg. Der Zaun bleibt trocken."))

# ═════════════════════ Kind 1 · Flug z2 · Teilbarkeit ═════════════════════
f = "z2"
prim = lambda n: n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
teiler = lambda n: [d for d in range(1, n + 1) if n % d == 0]
# teiler
neu(f, "teiler", "FD", FDZ("Kim prüft, ob 7 ein Teiler von 52 ist.",
    [("Ich rechne 52 : 7.", True), ("Es ist 7 · 7 = 49 und 7 · 8 = 56.", 7 * 7 == 49 and 7 * 8 == 56), ("Es bleibt kein Rest, also ist 7 ein Teiler von 52.", 52 % 7 == 0)],
    "Liegt 52 genau auf einem Ergebnis der Siebenerreihe?", "52 liegt zwischen 49 und 56, ist also kein Vielfaches von 7. Es bleibt der Rest 3. 7 ist kein Teiler von 52."))
neu(f, "teiler", "VW", W("Wie findest du alle Teiler von 28 sicher?",
    "Teilerpaare suchen: 1 · 28, 2 · 14, 4 · 7. Teiler: 1, 2, 4, 7, 14, 28",
    [("Nur bis 7 probieren. Teiler: 1, 2, 4, 7", "die großen Partner der Paare vergessen"), ("28 immer durch 2 teilen: 14, 7. Teiler: 14, 7", "Halbieren findet nicht alle Teiler"), ("Die Siebenerreihe aufschreiben: 7, 14, 21, 28. Teiler: 7, 14, 21, 28", "Vielfache statt Teiler")],
    "Zu jedem Teiler gehört ein Partner mit dem Produkt 28.", "Paare mit dem Produkt 28: 1 · 28, 2 · 14, 4 · 7. Das gibt sechs Teiler.",
    lambda: teiler(28) == [1, 2, 4, 7, 14, 28] and [1, 2, 4, 7] != teiler(28) and [14, 7] != teiler(28) and [7, 14, 21, 28] != teiler(28)), g="mehrschritt")
# vielfache
neu(f, "vielfache", "LW", L("Die ersten Vielfachen von 6 sind 6, 12 und 18. Das vierte Vielfache ist 4 · 6 = ①. Das siebte Vielfache ist 7 · 6 = ②. Das zehnte Vielfache ist 10 · 6 = ③.",
    K(3), [24, 42, 60], ["4 * 6", "7 * 6", "10 * 6"], ["18 + 6", "6 * 6 + 6", "6 * 5 * 2"], "Das n-te Vielfache von 6 ist n · 6.", "4 · 6 = 24, 7 · 6 = 42, 10 · 6 = 60.",
    {0: [(10, None, "4 + 6 gerechnet")], 2: [(16, None, "10 + 6 gerechnet")]}, hinweis=GZ))
gem = [x for x in range(1, 40) if x % 4 == 0 and x % 6 == 0]
neu(f, "vielfache", "FD", FDZ("Kim sucht die kleinste Zahl, die in der Viererreihe und in der Sechserreihe vorkommt.",
    [("Viererreihe: 4, 8, 12, 16, 20, 24.", [4 * k for k in range(1, 7)] == [4, 8, 12, 16, 20, 24]), ("Sechserreihe: 6, 12, 18, 24.", [6 * k for k in range(1, 5)] == [6, 12, 18, 24]), ("Die erste Zahl, die in beiden Reihen steht, ist 24.", gem[0] == 24)],
    "Schau von links: Welche Zahl kommt zuerst in beiden Reihen vor?", "In beiden Reihen steht schon die 12: 4 · 3 = 12 und 6 · 2 = 12. Die gesuchte Zahl ist 12."))
neu(f, "vielfache", "VW", W("Bus A fährt alle 12 Minuten, Bus B alle 18 Minuten. Um 8:00 Uhr fahren beide gleichzeitig ab. Wie findest du, nach wie vielen Minuten sie zum ersten Mal wieder gleichzeitig abfahren?",
    "Beide Reihen aufschreiben (12, 24, 36 und 18, 36): die erste gemeinsame Zahl ist 36",
    [("12 + 18 = 30 rechnen", "die beiden Zeiten addiert"), ("12 · 18 = 216 rechnen", "ein gemeinsames Vielfaches, aber nicht das erste"), ("18 − 12 = 6 rechnen", "den Unterschied der Zeiten genommen")],
    "Suche eine Zahl, die in der Zwölferreihe und in der Achtzehnerreihe steht – die kleinste.", "Zwölferreihe: 12, 24, 36. Achtzehnerreihe: 18, 36. Zuerst gemeinsam: 36. Nach 36 Minuten fahren beide wieder zusammen ab.",
    lambda: min(x for x in range(1, 400) if x % 12 == 0 and x % 18 == 0) == 36 and 12 + 18 != 36 and 12 * 18 != 36 and 18 - 12 != 36), g="einkleidung")
# endziffer
neu(f, "endziffer", "LW", L("Die Zahl 4 730 hat die Endziffer ①. Sie ist durch 10 teilbar: 4 730 : 10 = ②. Die Zahl 4 736 ist durch 2 teilbar, weil ihre Endziffer ③ gerade ist.",
    K(3), [0, 473, 6], ["4730 % 10", "4730 // 10", "4736 % 10"], ["0", "473 * 10 // 10", "4736 - 4730"], "Die Endziffer ist die letzte Ziffer der Zahl.", "Endziffer von 4 730: 0. 4 730 : 10 = 473. Endziffer von 4 736: 6.",
    {1: [(47, None, "zwei Stellen abgestrichen")]}, hinweis=GZ))
neu(f, "endziffer", "FD", FDZ("Kim prüft die Zahl 2 450.",
    [("Die Endziffer ist 0.", 2450 % 10 == 0), ("Die Endziffer 0 heißt: Die Zahl ist durch 10 teilbar.", 2450 % 10 == 0), ("2 450 ist durch 10 teilbar, aber nicht durch 5.", 2450 % 10 == 0 and 2450 % 5 != 0)],
    "Jede Zahl, die durch 10 teilbar ist, ist auch durch 5 teilbar. Warum?", "10 = 2 · 5. Was durch 10 geht, geht auch durch 5. 2 450 ist durch 10 und durch 5 teilbar."))
# quersumme
neu(f, "quersumme", "FD", FDZ("Kim prüft, ob 4 281 durch 3 teilbar ist.",
    [("Quersumme: 4 + 2 + 8 + 1 = 15.", 4 + 2 + 8 + 1 == 15), ("15 : 3 = 5, es bleibt kein Rest.", 15 % 3 == 0), ("Also ist 4 281 nicht durch 3 teilbar.", 4281 % 3 != 0)],
    "Was folgt, wenn die Quersumme durch 3 teilbar ist?", "Die Quersumme 15 ist durch 3 teilbar. Dann ist auch 4 281 durch 3 teilbar: 4 281 : 3 = 1 427."))
neu(f, "quersumme", "VW", W("Du willst wissen, ob 7 428 durch 3 teilbar ist. Welcher Weg führt sicher zum Ziel?",
    "Quersumme 7 + 4 + 2 + 8 = 21 bilden. 21 ist durch 3 teilbar, also auch 7 428",
    [("Die Endziffer 8 ansehen. 8 ist nicht durch 3 teilbar, also auch 7 428 nicht", "die Endziffer-Regel von 2 und 5 auf die 3 übertragen"), ("Die Ziffern zählen: Es sind 4. 4 ist nicht durch 3 teilbar, also auch 7 428 nicht", "die Anzahl der Ziffern statt ihrer Summe benutzt"), ("Die erste Ziffer 7 ansehen. 7 ist nicht durch 3 teilbar, also auch 7 428 nicht", "nur eine Ziffer angesehen")],
    "Zähle alle Ziffern zusammen, nicht nur eine.", "Die Quersumme 21 ist durch 3 teilbar, also ist 7 428 durch 3 teilbar: 7 428 : 3 = 2 476. Die anderen Wege schließen auf „nicht teilbar“ – das ist falsch.",
    lambda: 7428 % 3 == 0 and sum(map(int, "7428")) == 21 and 8 % 3 != 0 and 7 % 3 != 0 and 4 % 3 != 0), g="mehrschritt")
# neunerregel
neu(f, "neunerregel", "LW", L("Prüfe 5 481 auf Teilbarkeit durch 9. Quersumme: 5 + 4 + 8 + 1 = ①. Dann ① : 9 = ② ohne Rest. Also ist 5 481 durch 9 teilbar, und 5 481 : 9 = ③.",
    K(3), [18, 2, 609], ["5 + 4 + 8 + 1", "(5 + 4 + 8 + 1) // 9", "5481 // 9"], ["10 + 8", "36 // 18", "5400 // 9 + 9"], "Zähle alle Ziffern zusammen und teile dann durch 9.", "5 + 4 + 8 + 1 = 18. 18 : 9 = 2. 5 481 : 9 = 609.",
    {2: [(69, None, "bei 54 : 9 die Null vergessen")]}, hinweis=GZ))
neu(f, "neunerregel", "VW", W("Wie entscheidest du, ob 7 235 durch 9 teilbar ist?",
    "Quersumme 7 + 2 + 3 + 5 = 17 bilden. 17 ist nicht durch 9 teilbar, also ist 7 235 nicht durch 9 teilbar",
    [("Quersumme 7 + 2 + 3 + 5 = 17 bilden. 17 ist durch 3 teilbar, also ist 7 235 durch 9 teilbar", "17 ist gar nicht durch 3 teilbar"), ("Die letzten zwei Ziffern 35 ansehen. 35 ist durch 9 teilbar, also ist 7 235 durch 9 teilbar", "35 ist nicht durch 9 teilbar"), ("Die erste Ziffer 7 ansehen. 7 ist nicht durch 9 teilbar, also ist 7 235 durch 9 teilbar", "falscher Schluss aus einer einzelnen Ziffer")],
    "Bei der Neunerregel zählt die Quersumme, nicht eine einzelne Ziffer.", "Quersumme: 7 + 2 + 3 + 5 = 17. 17 ist nicht durch 9 teilbar, also ist auch 7 235 nicht durch 9 teilbar.",
    lambda: sum(map(int, "7235")) == 17 and 7235 % 9 != 0 and 17 % 3 != 0 and 35 % 9 != 0), g="mehrschritt")
# primzahl
neu(f, "primzahl", "LW", L("Prüfe, ob 39 eine Primzahl ist. 39 : 3 = ①. Neben 1, 3 und 39 ist auch ① ein Teiler. 39 hat also genau ② Teiler. Eine Primzahl hat nur ③ Teiler.",
    K(3), [13, 4, 2], ["39 // 3", "4", "2"], ["3 * 13 // 3", str(len(teiler(39))), "1 + 1"], "Zähle alle Teiler von 39 mit ihren Partnern.", "39 : 3 = 13. Teiler: 1, 3, 13, 39. Das sind vier, also keine Primzahl. Eine Primzahl hat genau zwei Teiler.",
    {1: [(2, None, "nur 1 und 39 gezählt"), (3, None, "einen Partner vergessen")]}, hinweis=GZ))
neu(f, "primzahl", "FD", FDZ("Kim prüft, ob 51 eine Primzahl ist.",
    [("51 ist ungerade, also nicht durch 2 teilbar.", 51 % 2 != 0), ("51 endet nicht auf 0 oder 5, also nicht durch 5 teilbar.", 51 % 5 != 0), ("Mehr Teiler muss ich nicht suchen: 51 ist eine Primzahl.", prim(51))],
    "Prüfe auch die Quersumme: Ist 5 + 1 durch 3 teilbar?", "Die Quersumme 5 + 1 = 6 ist durch 3 teilbar. Also ist 51 = 3 · 17 und keine Primzahl."))
# primfaktoren
neu(f, "primfaktoren", "VW", W("Welche Zerlegung ist die Primfaktorzerlegung von 90?",
    "90 = 2 · 3 · 3 · 5",
    [("90 = 9 · 10", "nicht bis zu Primzahlen zerlegt"), ("90 = 2 · 5 · 9", "9 ist keine Primzahl"), ("90 = 2 · 3 · 3 · 3", "falsch gerechnet: das Produkt ist 54")],
    "Zerlege so lange, bis nur noch Primzahlen dastehen.", "90 = 2 · 45 = 2 · 3 · 15 = 2 · 3 · 3 · 5. Alle Faktoren sind Primzahlen, und 2 · 3 · 3 · 5 = 90.",
    lambda: 2 * 3 * 3 * 5 == 90 and all(prim(x) for x in (2, 3, 3, 5)) and not prim(9) and 2 * 3 * 3 * 3 != 90), g="mehrschritt")

# ═════════════════════ Kind 2 · Flug ge2 · Spiegeln und Symmetrie (12 Lernkarten) ═════════════════════
f = "ge2"
rot90 = lambda v: (-v[1], v[0])            # +90°, gegen den Uhrzeigersinn
rotm90 = lambda v: (v[1], -v[0])           # −90°
punkt_sp = lambda p, z: (2 * z[0] - p[0], 2 * z[1] - p[1])
# achsenspiegelung
neu(f, "achsenspiegelung", "FD", FDZ("Kim spiegelt den Punkt P(4 | −3) an der y-Achse.",
    [("Bei der Spiegelung an der y-Achse bleibt die Höhe (y-Wert) gleich.", True), ("Der x-Wert wechselt das Vorzeichen: Aus 4 wird −4.", True), ("Das Bild ist P'(−4 | 3).", (-4, 3) == (-4, -3))],
    "Die y-Achse ist senkrecht. Was passiert mit der Höhe eines Punktes?", "Zeile 1 sagt es selbst: Die Höhe bleibt gleich, also y = −3. Richtig: P'(−4 | −3)."))
# punktspiegelung
neu(f, "punktspiegelung", "FD", FDZ("Kim spiegelt P(6 | 3) am Punkt Z(2 | 1).",
    [("Von P nach Z geht man 4 nach links und 2 nach unten.", (2 - 6, 1 - 3) == (-4, -2)), ("Von Z aus geht man denselben Weg weiter: x: 2 − 4 = −2 und y: 1 + 2 = 3.", (2 - 4, 1 + 2) == punkt_sp((6, 3), (2, 1))), ("Das Bild ist P'(−2 | 3).", True)],
    "„Nach unten“ heißt, dass y kleiner wird. Das gilt auch beim zweiten Teil des Weges.", "Von Z aus geht es 2 nach unten: y = 1 − 2 = −1. Richtig: P'(−2 | −1)."))
neu(f, "punktspiegelung", "VW", W("Der Punkt P(7 | −2) wird am Punkt Z(3 | 4) gespiegelt. Welche Rechnung liefert den Bildpunkt P'?",
    "x: 2 · 3 − 7 = −1 und y: 2 · 4 − (−2) = 10, also P'(−1 | 10)",
    [("x: 7 − 3 = 4 und y: −2 − 4 = −6, also P'(4 | −6)", "nur den Vektor von Z nach P ausgerechnet"), ("x: −7 und y: 2, also P'(−7 | 2)", "am Ursprung statt an Z gespiegelt"), ("x: 3 − 7 = −4 und y: 4 − (−2) = 6, also P'(−4 | 6)", "nur den Vektor von P nach Z ausgerechnet")],
    "Z ist die Mitte von P und P'. Zum Doppelten von Z gehört noch etwas dazu.", "Z ist die Mitte: P' = 2 · Z − P. x: 6 − 7 = −1. y: 8 + 2 = 10.",
    lambda: punkt_sp((7, -2), (3, 4)) == (-1, 10) and (4, -6) != (-1, 10) and (-7, 2) != (-1, 10) and (-4, 6) != (-1, 10)), g="mehrschritt")
# mittelsenkrechte
neu(f, "mittelsenkrechte", "LW", L("A(2 | 3) und B(10 | 3) liegen auf einer waagrechten Linie. Die Mitte von [AB] hat die x-Koordinate (2 + 10) : 2 = ①. Die Mittelsenkrechte ist die senkrechte Linie durch diese Stelle. Sie hat von A den Abstand ① − 2 = ②.",
    K(2), [6, 4], ["(2 + 10) // 2", "(2 + 10) // 2 - 2"], ["12 / 2", "(10 - 2) / 2"], "Die Mitte liegt genau zwischen den beiden x-Werten.", "(2 + 10) : 2 = 6. Abstand zu A: 6 − 2 = 4.",
    {0: [(12, None, "die x-Werte nicht halbiert")], 1: [(8, None, "die ganze Strecke statt der Hälfte")]}, hinweis=GZ))
neu(f, "mittelsenkrechte", "VW", W("Die Punkte A(1 | 4) und B(9 | 4) liegen auf einer waagrechten Linie. Welche Linie ist die Mittelsenkrechte von [AB]?",
    "die senkrechte Linie durch x = 5", [("die senkrechte Linie durch x = 8", "den Abstand AB statt der Mitte genommen"), ("die waagrechte Linie durch y = 4", "die Linie AB selbst genannt"), ("die senkrechte Linie durch x = 4", "den y-Wert für den x-Wert gehalten")],
    "Die Mittelsenkrechte steht senkrecht auf [AB] und geht durch die Mitte.", "Die Mitte hat x = (1 + 9) : 2 = 5. Senkrecht zur waagrechten Strecke: senkrechte Linie durch x = 5.",
    lambda: (1 + 9) / 2 == 5 and 9 - 1 != 5 and 4 != 5), g="mehrschritt")
# winkelhalbierende
neu(f, "winkelhalbierende", "LW", L("Ein Winkel hat 70°. Die Winkelhalbierende teilt ihn in zwei Winkel von je 70° : 2 = ①. Ein Winkel von 100° wird in zwei Winkel von je ② geteilt. Zwei Teilwinkel von je 15° ergeben zusammen einen Winkel von ③°.",
    K(3), [35, 50, 30], ["70 // 2", "100 // 2", "15 * 2"], ["35", "50", "15 + 15"], "Halbieren heißt durch 2 teilen. Zwei Hälften ergeben wieder das Ganze.", "70° : 2 = 35°. 100° : 2 = 50°. 15° + 15° = 30°.",
    {0: [(140, None, "mit 2 multipliziert statt geteilt")], 2: [(7, None, "durch 2 geteilt statt verdoppelt")]}, hinweis=GZ))
neu(f, "winkelhalbierende", "FD", FDZ("Ein Winkel hat 84°. Kim berechnet, wie groß die beiden Winkel sind, in die ihn die Winkelhalbierende teilt.",
    [("Die Winkelhalbierende teilt den Winkel in zwei gleich große Teile.", True), ("Jeder Teil hat 84° − 2 = 82°.", 84 - 2 == 84 / 2), ("Die Winkelhalbierende liegt also 82° vom Schenkel entfernt.", True)],
    "Zwei gleich große Teile ergeben zusammen wieder 84°.", "Jeder Teil ist die Hälfte: 84° : 2 = 42°. Zusammen 42° + 42° = 84°."))
neu(f, "winkelhalbierende", "VW", W("Ein Punkt liegt auf der Winkelhalbierenden eines Winkels. Er ist vom einen Schenkel 3 cm entfernt. Wie weit ist er vom anderen Schenkel entfernt?",
    "3 cm, denn auf der Winkelhalbierenden ist der Abstand zu beiden Schenkeln gleich",
    [("1,5 cm, denn die Winkelhalbierende halbiert", "Halbieren des Winkels mit Halbieren des Abstands verwechselt"), ("6 cm, denn der andere Schenkel liegt auf der anderen Seite", "die beiden Abstände addiert"), ("Das lässt sich nicht sagen. Der Abstand kann beliebig sein", "die Eigenschaft der Winkelhalbierenden nicht gekannt")],
    "Welche Eigenschaft haben alle Punkte auf der Winkelhalbierenden?", "Alle Punkte auf der Winkelhalbierenden haben von beiden Schenkeln denselben Abstand: 3 cm.",
    lambda: 3 == 3 and 3 / 2 != 3 and 3 + 3 != 3), g="mehrschritt")
# verschiebung
neu(f, "verschiebung", "FD", FDZ("Kim verschiebt P(3 | −2) mit dem Vektor v = (−5 | 4).",
    [("Die erste Zahl −5 gehört zu x: x = 3 + (−5) = −2.", 3 + (-5) == -2), ("Die zweite Zahl 4 gehört zu y: y = −2 + 4 = 2.", -2 + 4 == 2), ("Das Bild ist P'(2 | −2).", (2, -2) == (-2, 2))],
    "Zuerst kommt x, dann y. Wie steht es in den Zeilen davor?", "Zeile 1 gibt x = −2, Zeile 2 gibt y = 2. Richtig: P'(−2 | 2). Kim hat x und y vertauscht."))
neu(f, "verschiebung", "VW", W("Eine Verschiebung bringt A(2 | 5) nach A'(−1 | 9). Wohin kommt B(4 | 0) bei derselben Verschiebung, und wie berechnest du das?",
    "v = (−1 − 2 | 9 − 5) = (−3 | 4), also B'(4 − 3 | 0 + 4) = (1 | 4)",
    [("v = (2 − (−1) | 5 − 9) = (3 | −4), also B'(4 + 3 | 0 − 4) = (7 | −4)", "den Vektor rückwärts (A' nach A) gebildet"), ("v = (−1 | 9), also B'(4 − 1 | 0 + 9) = (3 | 9)", "den Bildpunkt als Vektor genommen"), ("v = (−3 | 4), also B'(4 | 0) bleibt, weil B nicht auf A liegt", "nur A wird verschoben")],
    "Der Vektor zeigt von A nach A'. Ende minus Anfang.", "v = A' − A = (−3 | 4). Dann B' = B + v = (1 | 4).",
    lambda: (-1 - 2, 9 - 5) == (-3, 4) and (4 - 3, 0 + 4) == (1, 4) and (7, -4) != (1, 4) and (3, 9) != (1, 4) and (4, 0) != (1, 4)), g="mehrschritt")
# gegenvektor
neu(f, "gegenvektor", "LW", L("Die Verschiebung mit v = (3 | −5) bringt P nach P'(5 | −1). Der Gegenvektor ist −v = (−3 | 5). Mit ihm geht P' zurück: P = (5 + (−3) | −1 + 5) = (① | ②).",
    K(2), [2, 4], ["5 + (-3)", "-1 + 5"], ["5 - 3", "5 - 1"], "Rechne Zahl für Zahl: erst x, dann y.", "5 + (−3) = 2 und −1 + 5 = 4. Der Urpunkt ist P(2 | 4).",
    {0: [(8, None, "v statt −v addiert")], 1: [(-6, None, "v statt −v addiert")]}, hinweis=GZ), regel=DECK)
neu(f, "gegenvektor", "FD", FDZ("Der Punkt P'(1 | −4) entstand durch die Verschiebung mit v = (6 | −2). Kim sucht den Urpunkt P.",
    [("Der Gegenvektor ist −v = (−6 | −2).", (-6, -2) == (-6, 2)), ("Neue x-Zahl: 1 + (−6) = −5.", 1 + (-6) == -5), ("Neue y-Zahl: −4 + (−2) = −6.", -4 + (-2) == -6)],
    "Beim Gegenvektor ändern sich beide Vorzeichen.", "Aus (6 | −2) wird (−6 | 2). Dann y: −4 + 2 = −2. Richtig: P(−5 | −2)."))
neu(f, "gegenvektor", "VW", W("Ein Punkt wurde mit v = (4 | −3) verschoben und liegt jetzt bei Q'(2 | 7). Wie findest du den Urpunkt Q?",
    "Q' − v rechnen: (2 − 4 | 7 − (−3)) = (−2 | 10)",
    [("Q' + v rechnen: (2 + 4 | 7 + (−3)) = (6 | 4)", "noch einmal verschoben statt zurück"), ("v − Q' rechnen: (4 − 2 | −3 − 7) = (2 | −10)", "die Reihenfolge der Subtraktion vertauscht"), ("x und y tauschen: (7 − 4 | 2 − (−3)) = (3 | 5)", "x- und y-Zahl vermischt")],
    "Der Weg zurück ist der Gegenvektor.", "Q' − v = (2 − 4 | 7 + 3) = (−2 | 10). Probe: (−2 + 4 | 10 − 3) = (2 | 7).",
    lambda: (2 - 4, 7 + 3) == (-2, 10) and (-2 + 4, 10 + (-3)) == (2, 7) and (6, 4) != (-2, 10) and (2, -10) != (-2, 10) and (3, 5) != (-2, 10)), g="mehrschritt")
# drehung
neu(f, "drehung", "LW", L("P(9 | 6) wird um Z(2 | 1) um 90° gegen den Uhrzeigersinn gedreht. Zuerst der Vektor von Z nach P: (9 − 2 | 6 − 1) = (① | ②). Die Drehung macht aus (a | b) den Vektor (−b | a). Der Bildpunkt ist Z plus dieser Vektor: P'(③ | ④).",
    K(4), [7, 5, -3, 8], ["9 - 2", "6 - 1", "2 + (-(6 - 1))", "1 + (9 - 2)"], ["7", "5", "2 - 5", "1 + 7"], "Der gedrehte Vektor ist (−5 | 7).", "(9 − 2 | 6 − 1) = (7 | 5). Gedreht: (−5 | 7). P' = (2 − 5 | 1 + 7) = (−3 | 8).",
    {2: [(7, None, "um O statt um Z gedreht")]}, hinweis=GZ))
neu(f, "drehung", "FD", FDZ("Kim dreht P(4 | 1) um O(0 | 0) um 180°.",
    [("Bei 180° wird aus (x | y) der Punkt (−x | −y).", True), ("Aus x = 4 wird −4.", -4 == -4), ("Aus y = 1 wird 1. Das Bild ist P'(−4 | 1).", 1 == -1)],
    "Bei 180° wechseln beide Zahlen das Vorzeichen.", "Aus y = 1 wird −1. Richtig: P'(−4 | −1)."))
neu(f, "drehung", "VW", W("Der Punkt P(3 | 5) wird um O(0 | 0) um 90° im Uhrzeigersinn gedreht. Welche Rechnung ist richtig?",
    "(x | y) wird (y | −x), also P'(5 | −3)",
    [("(x | y) wird (−y | x), also P'(−5 | 3)", "gegen den Uhrzeigersinn gedreht"), ("(x | y) wird (−x | −y), also P'(−3 | −5)", "um 180° gedreht"), ("(x | y) wird (y | x), also P'(5 | 3)", "an der Winkelhalbierenden gespiegelt statt gedreht")],
    "Im Uhrzeigersinn ist die Gegenrichtung zu „gegen den Uhrzeigersinn“.", "Im Uhrzeigersinn um 90°: (x | y) wird (y | −x). Aus (3 | 5) wird (5 | −3).",
    lambda: rotm90((3, 5)) == (5, -3) and rot90((3, 5)) == (-5, 3) and (-3, -5) != (5, -3) and (5, 3) != (5, -3)), g="mehrschritt")
# symmetrie
neu(f, "symmetrie", "LW", L("Ein Quadrat hat ① Symmetrieachsen. Ein Rechteck, das kein Quadrat ist, hat ② Symmetrieachsen. Ein gleichseitiges Dreieck hat ③ Symmetrieachsen.",
    K(3), [4, 2, 3], ["4", "2", "3"], ["2 + 2", "1 + 1", "6 // 2"], "Falte in Gedanken: Wo passt alles genau aufeinander?", "Quadrat: 4 (2 durch die Seitenmitten, 2 durch die Ecken). Rechteck: 2. Gleichseitiges Dreieck: 3.",
    {0: [(2, None, "die Diagonalen vergessen")], 1: [(4, None, "das Rechteck wie ein Quadrat gezählt")]}, hinweis=GZ))
ACHSEN = {"Quadrat": 4, "Rechteck": 2, "Raute": 2}
neu(f, "symmetrie", "FD", FDZ("Kim zählt die Symmetrieachsen von Vierecken, die kein Quadrat sind.",
    [("Ein Quadrat hat 4 Achsen.", ACHSEN["Quadrat"] == 4), ("Ein Rechteck hat 2 Achsen.", ACHSEN["Rechteck"] == 2), ("Eine Raute hat 4 Achsen.", ACHSEN["Raute"] == 4)],
    "Eine Raute lässt sich nur an ihren beiden Diagonalen falten.", "Die Raute hat nur 2 Achsen: ihre beiden Diagonalen. Die Seitenmitten-Linien sind keine Achsen."))
# vierecke_ordnen
neu(f, "vierecke_ordnen", "LW", L("Im Haus der Vierecke haben die Vierecke Eigenschaften. Ein Parallelogramm hat ① Paare paralleler Seiten. Ein Trapez hat mindestens ② Paar paralleler Seiten. Ein Drachenviereck hat ③ Paare gleich langer Nachbarseiten.",
    K(3), [2, 1, 2], ["2", "1", "2"], ["1 + 1", "3 - 2", "4 // 2"], "Ein Paar sind immer zwei Seiten.", "Parallelogramm: 2 Paare. Trapez: mindestens 1 Paar. Drachenviereck: 2 Paare.",
    {0: [(1, None, "mit dem Trapez verwechselt")], 2: [(1, None, "nur ein Paar gezählt")]}, hinweis=GZ))
neu(f, "vierecke_ordnen", "ZW", Z("Zwei Wege: Weg A prüft jedes der sechs Vierecke einzeln. Weg B sucht nur die Vierecke, die das nicht haben, und zieht von 6 ab. Wie viele der Vierecke Quadrat, Rechteck, Raute, Parallelogramm, Trapez und Drachenviereck haben immer mindestens ein Paar paralleler Seiten?",
    5, "6 - 1", "1 + 1 + 1 + 1 + 1", "Beim Drachenviereck gibt es keine Garantie für parallele Seiten.", "Quadrat, Rechteck, Raute, Parallelogramm und Trapez haben immer ein Paar paralleler Seiten. Das Drachenviereck nicht immer. 6 − 1 = 5.",
    [(6, None, "das Drachenviereck mitgezählt"), (4, None, "das Trapez nicht mitgezählt")]), g="mehrschritt")
# eigenschaften
neu(f, "eigenschaften", "LW", L("Ein Dreieck hat die Seiten 7 cm, 9 cm und 11 cm. Sein Umfang ist 7 + 9 + 11 = ① cm. Das Dreieck wird gespiegelt. Der Umfang des Bildes ist ② cm. Die drei Winkel des Bildes ergeben zusammen ③°.",
    K(3), [27, 27, 180], ["7 + 9 + 11", "7 + 9 + 11", "180"], ["27", "9 * 3", "90 * 2"], "Eine Spiegelung ändert keine Längen und keine Winkel.", "7 + 9 + 11 = 27. Das Bild hat denselben Umfang. Die Winkelsumme im Dreieck ist 180°.",
    {2: [(360, None, "mit der Winkelsumme im Viereck verwechselt")]}, hinweis=GZ))
neu(f, "eigenschaften", "FD", FDZ("Kim sagt etwas über ein Dreieck, das um 90° gedreht wird.",
    [("Die Seitenlängen bleiben gleich.", True), ("Die Winkel bleiben gleich.", True), ("Der Umlaufsinn ändert sich bei jeder Drehung.", False)],
    "Nur eine Abbildung dreht den Umlaufsinn um. Welche?", "Der Umlaufsinn ändert sich nur bei der Achsenspiegelung. Bei einer Drehung bleibt er gleich."))
# vektor_koordinaten
neu(f, "vektor_koordinaten", "LW", L("Der Vektor v zeigt von A(1 | 6) nach B(8 | 2): v = (8 − 1 | 2 − 6) = (① | ②). Addiert man v zu C(3 | 9), erhält man C'(③ | ④).",
    K(4), [7, -4, 10, 5], ["8 - 1", "2 - 6", "3 + (8 - 1)", "9 + (2 - 6)"], ["7", "-4", "10", "5"], "Ende minus Anfang. Dann C plus v.", "v = (7 | −4). C' = (3 + 7 | 9 − 4) = (10 | 5).",
    {1: [(4, "fb.plusminus.zeichen_des_ergebnisses", "6 − 2 statt 2 − 6 gerechnet")]}, hinweis=GZ), regel=DECK)
neu(f, "vektor_koordinaten", "FD", FDZ("Kim berechnet den Vektor von A(5 | −2) nach B(1 | 4).",
    [("Regel: Ende minus Anfang.", True), ("Erste Zahl: 1 − 5 = −4.", 1 - 5 == -4), ("Zweite Zahl: 4 − (−2) = 4 − 2 = 2.", 4 - (-2) == 2)],
    "Minus minus 2: Was wird daraus?", "4 − (−2) = 4 + 2 = 6. Der Vektor ist (−4 | 6)."), regel=DECK)
neu(f, "vektor_koordinaten", "VW", W("Der Vektor v zeigt von A(1 | 2) nach B(6 | 5). Vom Punkt B aus gehst du noch einmal um v weiter und kommst zu C. Welche Rechnung ist richtig?",
    "v = (6 − 1 | 5 − 2) = (5 | 3), also C(6 + 5 | 5 + 3) = (11 | 8)",
    [("C(6 + 1 | 5 + 2) = (7 | 7)", "die Koordinaten von A statt des Vektors addiert"), ("v = (1 − 6 | 2 − 5) = (−5 | −3), also C(6 − 5 | 5 − 3) = (1 | 2)", "den Rückweg gerechnet: das ist wieder A"), ("C(6 · 2 | 5 · 2) = (12 | 10)", "die Koordinaten von B verdoppelt")],
    "Erst v ausrechnen, dann zu B addieren.", "v = (5 | 3). C = B + v = (11 | 8).",
    lambda: (6 + (6 - 1), 5 + (5 - 2)) == (11, 8) and (7, 7) != (11, 8) and (1, 2) != (11, 8) and (12, 10) != (11, 8)), g="mehrschritt", regel=DECK)
# vektor_drehen
neu(f, "vektor_drehen", "LW", L("Der Vektor v zeigt von A(1 | 2) nach B(5 | 9): v = (5 − 1 | 9 − 2) = (① | ②). Eine Drehung um +90° macht aus (x | y) den Vektor (−y | x). Gedreht ist v also (③ | ④).",
    K(4), [4, 7, -7, 4], ["5 - 1", "9 - 2", "-(9 - 2)", "5 - 1"], ["4", "7", "-7", "2 * 2"], "Die zweite Zahl wird zur ersten, mit anderem Vorzeichen.", "v = (4 | 7). Gedreht um +90°: (−7 | 4).",
    {2: [(7, None, "das Minus vergessen")]}, hinweis=GZ), regel=DECK)
neu(f, "vektor_drehen", "FD", FDZ("Kim dreht den Vektor v = (6 | −2) um −90°. Die Regel lautet: Aus (x | y) wird (y | −x).",
    [("x = 6 und y = −2.", True), ("Die neue erste Zahl ist y = −2.", True), ("Die neue zweite Zahl ist x = 6.", 6 == -6)],
    "In der Regel steht bei der zweiten Zahl ein Minus.", "Die zweite Zahl ist −x = −6. Richtig: (−2 | −6)."), regel=DECK)
neu(f, "vektor_drehen", "VW", W("Der Vektor v = (2 | 5) wird zweimal hintereinander um +90° gedreht. Welcher Vektor entsteht?",
    "(−2 | −5), denn zweimal 90° sind zusammen 180°",
    [("(−5 | 2)", "nur einmal gedreht"), ("(5 | −2)", "um −90° gedreht"), ("(2 | −5)", "an der x-Achse gespiegelt statt gedreht")],
    "Zweimal 90° ergibt eine Drehung um wie viel Grad?", "Erst (2 | 5) → (−5 | 2), dann (−5 | 2) → (−2 | −5). Das ist eine Drehung um 180°.",
    lambda: rot90(rot90((2, 5))) == (-2, -5) and rot90((2, 5)) != (-2, -5) and rotm90((2, 5)) != (-2, -5) and (2, -5) != (-2, -5)), g="mehrschritt", regel=DECK)

# ═════════════════════ Kind 2 · Flug a4 · Lineare Ungleichungen und Intervalle ═════════════════════
f = "a4"
UNG, INT = "gleichungen.ungleichungen", "zahlen.intervalle"
loesung = lambda bed, lo=-40, hi=40: [x for x in range(lo, hi + 1) if bed(x)]
# umformen
neu(f, "umformen", "FD", FDZ("Kim löst 5x + 8 > 33.",
    [("Auf beiden Seiten 8 abziehen: 5x > 25.", 33 - 8 == 25), ("Durch 5 teilen: x > 5.", 25 / 5 == 5), ("Die Lösung sind alle Zahlen kleiner als 5.", all((5 * x + 8 > 33) == (x < 5) for x in range(-20, 21)))],
    "Das Zeichen bleibt beim Teilen durch eine positive Zahl, wie es ist.", "Aus x > 5 folgt: alle Zahlen größer als 5. Kim hat das Ergebnis falsch gelesen."))
neu(f, "umformen", "VW", W("Wie löst du 4x − 9 ≥ 15 richtig?",
    "Auf beiden Seiten 9 addieren: 4x ≥ 24. Durch 4 teilen: x ≥ 6",
    [("Auf beiden Seiten 9 abziehen: 4x ≥ 6. Durch 4 teilen: x ≥ 1,5", "bei der Gegenrechnung addiert statt subtrahiert"), ("Nur 4x durch 4 teilen: x − 9 ≥ 15. Dann 9 addieren: x ≥ 24", "nur einen Term geteilt"), ("Beide Seiten durch 4 teilen: x − 9 ≥ 3. Dann 9 addieren: x ≥ 12", "die 9 nicht mitgeteilt")],
    "Erst die Zahl ohne x auf die andere Seite bringen. Dann teilen.", "4x − 9 ≥ 15, also 4x ≥ 24 und x ≥ 6. Probe: x = 6: 4 · 6 − 9 = 15.",
    lambda: loesung(lambda x: 4 * x - 9 >= 15)[0] == 6 and loesung(lambda x: 4 * x - 9 >= 15, 1, 1) == [] and 6 != 1.5 and 6 != 24 and 6 != 12), g="mehrschritt")
# umdrehen
neu(f, "umdrehen", "VW", W("Löse −3x + 4 > 19. Welcher Weg ist richtig?",
    "4 abziehen: −3x > 15. Durch −3 teilen und das Zeichen umdrehen: x < −5",
    [("4 abziehen: −3x > 15. Durch −3 teilen, aber das Zeichen lassen: x > −5", "Zeichen nicht umgedreht"), ("4 abziehen: −3x > 15. Durch 3 teilen: x > 5", "das Minus vor der 3 ignoriert"), ("4 abziehen: −3x > 15. Durch −3 teilen und das Zeichen umdrehen: x < 5", "15 : (−3) falsch vorzeichenbehaftet gerechnet")],
    "Beim Teilen durch eine negative Zahl dreht sich das Zeichen um.", "−3x > 15. Durch −3 teilen: x < −5. Probe: x = −6: −3 · (−6) + 4 = 22 > 19.",
    lambda: all((-3 * x + 4 > 19) == (x < -5) for x in range(-30, 31)) and not all((-3 * x + 4 > 19) == (x > -5) for x in range(-30, 31)) and not all((-3 * x + 4 > 19) == (x > 5) for x in range(-30, 31)) and not all((-3 * x + 4 > 19) == (x < 5) for x in range(-30, 31))), g="mehrschritt")
# klammern
neu(f, "klammern", "FD", FDZ("Kim löst 2(x − 3) < x + 5.",
    [("Klammer auflösen: 2x − 3 < x + 5.", all(2 * (x - 3) == 2 * x - 3 for x in range(-5, 6))), ("Auf beiden Seiten x abziehen: x − 3 < 5.", True), ("Auf beiden Seiten 3 addieren: x < 8.", True)],
    "Beim Auflösen der Klammer wird jede Zahl in der Klammer mit 2 multipliziert.", "2(x − 3) = 2x − 6, nicht 2x − 3. Richtig: 2x − 6 < x + 5, also x < 11."))
neu(f, "klammern", "VW", W("Löse 3(x + 2) ≥ 5x − 4. Welche Lösung stimmt?",
    "Klammer auflösen: 3x + 6 ≥ 5x − 4. Daraus folgt x ≤ 5",
    [("Klammer auflösen: 3x + 6 ≥ 5x − 4. Daraus folgt x ≥ 5", "beim Teilen durch −2 das Zeichen nicht umgedreht"), ("Klammer auflösen: 3x + 2 ≥ 5x − 4. Daraus folgt x ≤ 3", "die 2 in der Klammer nicht mit 3 multipliziert"), ("Klammer auflösen: 3x + 6 ≥ 5x − 4. Daraus folgt x ≥ −5", "Vorzeichen beim Umstellen verloren")],
    "Ordne: x-Terme auf eine Seite, Zahlen auf die andere. Beachte das Vorzeichen von x am Ende.", "3x + 6 ≥ 5x − 4 → 10 ≥ 2x → x ≤ 5. Probe: x = 5: 3 · 7 = 21 ≥ 21.",
    lambda: all((3 * (x + 2) >= 5 * x - 4) == (x <= 5) for x in range(-30, 31)) and not all((3 * (x + 2) >= 5 * x - 4) == (x >= 5) for x in range(-30, 31)) and not all((3 * (x + 2) >= 5 * x - 4) == (x <= 3) for x in range(-30, 31)) and not all((3 * (x + 2) >= 5 * x - 4) == (x >= -5) for x in range(-30, 31))), g="mehrschritt")
# intervall
neu(f, "intervall", "LW", L("Löse 2x + 6 ≥ 14. Auf beiden Seiten 6 abziehen: 2x ≥ ①. Durch 2 teilen: x ≥ ②. Die Lösungsmenge ist das Intervall [②; ∞[.",
    K(2), [8, 4], ["14 - 6", "(14 - 6) // 2"], ["2 * 4", "8 / 2"], "Die Grenze gehört dazu, weil „≥“ dasteht.", "2x ≥ 8, also x ≥ 4. L = [4; ∞[.",
    {0: [(20, None, "6 addiert statt abgezogen")]}, hinweis=GZ), regel="id.algebra.gleichung_loesen", thema=UNG)
neu(f, "intervall", "FD", FDZ("Kim löst −2x ≤ 10 und schreibt die Lösung als Intervall.",
    [("Durch −2 teilen und das Zeichen umdrehen: x ≥ −5.", all((-2 * x <= 10) == (x >= -5) for x in range(-20, 21))), ("Die Grenze −5 gehört dazu, die Klammer zeigt zur Zahl hin: [−5.", True), ("Es geht unbegrenzt nach rechts: L = [−5; ∞].", False)],
    "Bei ∞ zeigt die Klammer immer nach außen.", "∞ ist keine Zahl und gehört nie dazu. Richtig: L = [−5; ∞[."), thema=UNG)
neu(f, "intervall", "VW", W("Löse 5 − x < 2 und gib die Lösungsmenge als Intervall an. Welche Antwort stimmt?",
    "−x < −3, durch −1 teilen und das Zeichen umdrehen: x > 3, also L = ]3; ∞[",
    [("−x < −3, daraus folgt x < 3, also L = ]−∞; 3[", "Zeichen nicht umgedreht"), ("−x < −3, durch −1 teilen und das Zeichen umdrehen: x > 3, also L = [3; ∞[", "Klammer bei „>“ falsch gesetzt"), ("−x < −3, daraus folgt x > −3, also L = ]−3; ∞[", "das Vorzeichen der Zahl nicht geteilt")],
    "Auch bei −x dreht sich das Zeichen um, denn du teilst durch −1.", "5 − x < 2 → −x < −3 → x > 3. Die 3 gehört nicht dazu: L = ]3; ∞[.",
    lambda: all((5 - x < 2) == (x > 3) for x in range(-20, 21)) and not (5 - 3 < 2) and not all((5 - x < 2) == (x < 3) for x in range(-20, 21)) and not all((5 - x < 2) == (x > -3) for x in range(-20, 21))), g="mehrschritt", thema=UNG)
# pruefen
neu(f, "pruefen", "LW", L("Prüfe, ob x = 5 die Ungleichung 2x + 3 ≤ 11 löst. Einsetzen: 2 · 5 + 3 = ①. Das ist größer als 11, also ist 5 keine Lösung. Prüfe x = 3: 2 · 3 + 3 = ②. Das ist kleiner als 11, also ist 3 eine Lösung.",
    K(2), [13, 9], ["2 * 5 + 3", "2 * 3 + 3"], ["10 + 3", "6 + 3"], "Erst mal, dann plus.", "2 · 5 + 3 = 13 > 11. 2 · 3 + 3 = 9 ≤ 11.",
    {0: [(16, None, "erst 5 + 3, dann mal 2 gerechnet")]}, hinweis=GZ), thema=UNG)
neu(f, "pruefen", "FD", FDZ("Kim löst −2x + 1 > 7 und prüft das Ergebnis.",
    [("1 abziehen: −2x > 6.", 7 - 1 == 6), ("Durch −2 teilen: x > −3.", all((-2 * x + 1 > 7) == (x > -3) for x in range(-20, 21))), ("Probe mit x = 0: −2 · 0 + 1 = 1, und 1 > 7 stimmt nicht.", not (1 > 7))],
    "Die Probe zeigt: 0 ist größer als −3 und trotzdem keine Lösung.", "Durch −2 teilen dreht das Zeichen um: x < −3. Die Probe mit x = 0 deckt den Fehler auf."), thema=UNG)
# grafisch
neu(f, "grafisch", "LW", L("Die Geraden f(x) = 2x + 1 und g(x) = x + 4 schneiden sich dort, wo 2x + 1 = x + 4 gilt: bei x = ①. An der Stelle x = 5 ist f(5) = ② und g(5) = ③. Dort liegt f über g.",
    K(3), [3, 11, 9], ["(4 - 1) // (2 - 1)", "2 * 5 + 1", "5 + 4"], ["3", "10 + 1", "4 + 5"], "Beim Schnittpunkt sind beide Funktionswerte gleich.", "x + 1 = 4, also x = 3. f(5) = 11, g(5) = 9.",
    {0: [(5, None, "die Zahlen 1 und 4 addiert")]}, hinweis=GZ), regel="id.algebra.gleichung_loesen", thema=UNG)
neu(f, "grafisch", "FD", FDZ("Die Geraden f(x) = x + 2 und g(x) = 3x − 4 schneiden sich bei x = 3. Kim löst f(x) < g(x) mit den Graphen.",
    [("Links von x = 3 liegt g unter f.", (3 * 2 - 4) < (2 + 2)), ("Rechts von x = 3 liegt g über f.", (3 * 5 - 4) > (5 + 2)), ("f(x) < g(x) gilt also für alle x < 3.", all((x + 2 < 3 * x - 4) == (x < 3) for x in range(-20, 21)))],
    "f(x) < g(x) heißt: f liegt unter g. Wo ist das der Fall?", "f liegt unter g rechts vom Schnittpunkt. Richtig: x > 3."), regel="id.algebra.gleichung_loesen", thema=UNG)
neu(f, "grafisch", "VW", W("Die Geraden f(x) = −x + 6 und g(x) = 2x schneiden sich bei x = 2. Für welche x gilt f(x) ≥ g(x)?",
    "für x ≤ 2, denn links vom Schnittpunkt liegt f über g", [("für x ≥ 2, denn rechts vom Schnittpunkt liegt f über g", "links und rechts verwechselt"), ("für x ≤ 6, denn bei x = 6 ist f(x) = 0", "die Nullstelle von f für den Schnittpunkt gehalten"), ("für x ≥ 6, denn dort ist g größer", "Nullstelle genommen und Richtung falsch")],
    "Setze eine Zahl links vom Schnittpunkt ein, zum Beispiel x = 0.", "f(0) = 6 und g(0) = 0: links liegt f über g. Also f(x) ≥ g(x) für x ≤ 2.",
    lambda: all((-x + 6 >= 2 * x) == (x <= 2) for x in range(-20, 21)) and -2 + 6 == 2 * 2 and not all((-x + 6 >= 2 * x) == (x >= 2) for x in range(-20, 21))), g="mehrschritt", regel="id.algebra.gleichung_loesen", thema=UNG)
# sachaufgabe
neu(f, "sachaufgabe", "LW", L("Ein Lastenaufzug darf höchstens 500 kg tragen. Ein Rollwagen wiegt 30 kg. Jede Kiste darauf wiegt 40 kg. Für k Kisten muss gelten: 30 + 40 · k ≤ 500. Also ist 40 · k ≤ ①. Die größte ganze Zahl k, die passt, ist ②.",
    K(2), [470, 11], ["500 - 30", "(500 - 30) // 40"], ["470", str(max(k for k in range(0, 40) if 30 + 40 * k <= 500))], "Teile durch 40 und lass die Nachkommastellen weg: Man kann keine halbe Kiste laden.", "40 · k ≤ 470, also k ≤ 11,75. Ganze Kisten: höchstens 11.",
    {1: [(12, None, "aufgerundet statt abgerundet")]}, hinweis=GZ), thema=UNG)
neu(f, "sachaufgabe", "FD", FDZ("Ein Verein verlangt 8 € Grundgebühr und 3 € für jeden Besuch. Kim hat höchstens 50 € zur Verfügung und will wissen, wie oft er kommen kann.",
    [("Ansatz: 8 + 3x ≥ 50.", False), ("8 abziehen: 3x ≥ 42.", 50 - 8 == 42), ("Durch 3 teilen: x ≥ 14.", 42 // 3 == 14)],
    "Welches Zeichen gehört zu „höchstens“?", "„Höchstens 50 €“ heißt: Die Kosten sind kleiner oder gleich 50. Richtig: 8 + 3x ≤ 50, also x ≤ 14."), thema=UNG)
neu(f, "sachaufgabe", "VW", W("Ein Taxi kostet 3 € Grundpreis und 2 € je Kilometer. Du hast 25 €. Wie viele Kilometer kannst du höchstens fahren? Welcher Ansatz passt?",
    "3 + 2x ≤ 25, also x ≤ 11: höchstens 11 km",
    [("3 + 2x ≥ 25, also x ≥ 11: mindestens 11 km", "„höchstens“ als „≥“ gelesen"), ("2 + 3x ≤ 25, also x ≤ 7: höchstens 7 km", "Grundpreis und Kilometerpreis vertauscht"), ("2x ≤ 25, also x ≤ 12: höchstens 12 km", "den Grundpreis vergessen")],
    "Gesamtkosten = Grundpreis + Preis je km mal Kilometer. Sie dürfen 25 € nicht übersteigen.", "3 + 2x ≤ 25 → 2x ≤ 22 → x ≤ 11. Bei 11 km zahlst du genau 25 €.",
    lambda: max(x for x in range(0, 40) if 3 + 2 * x <= 25) == 11 and max(x for x in range(0, 40) if 2 + 3 * x <= 25) == 7 and max(x for x in range(0, 40) if 2 * x <= 25) == 12), g="einkleidung", thema=UNG)
# lesen (zahlen.intervalle)
neu(f, "lesen", "LW", L("Das Intervall ]−3; 5[ enthält alle Zahlen zwischen −3 und 5, ohne die Grenzen. Die kleinste ganze Zahl darin ist ①. Die größte ganze Zahl darin ist ②. Insgesamt liegen ③ ganze Zahlen darin.",
    K(3), [-2, 4, 7], ["-3 + 1", "5 - 1", "4 - (-2) + 1"], ["-2", "4", str(len([x for x in range(-3, 6) if -3 < x < 5]))], "Die Grenzen selbst gehören nicht dazu.", "Ohne die Grenzen: −2 bis 4. Das sind −2, −1, 0, 1, 2, 3, 4: sieben Zahlen.",
    {0: [(-3, None, "die Grenze mitgezählt")], 1: [(5, None, "die Grenze mitgezählt")]}, hinweis=GZ), thema=INT)
neu(f, "lesen", "FD", FDZ("Kim liest das Intervall [2; 7[.",
    [("Die 2 gehört dazu, weil die Klammer zur Zahl hin zeigt.", True), ("Die 7 gehört nicht dazu, weil die Klammer von der Zahl weg zeigt.", True), ("Also sind alle Zahlen x mit 2 ≤ x ≤ 7 gemeint.", False)],
    "Gehört die 7 dazu? Dann darf in der Ungleichung kein ≤ stehen.", "Die 7 gehört nicht dazu. Richtig: 2 ≤ x < 7."), thema=INT)
# schreiben
neu(f, "schreiben", "LW", L("x + 3 ≥ 9 ergibt x ≥ ①. x − 2 < 5 ergibt x < ②. Beides zusammen: ① ≤ x < ②. Als Intervall schreibst du das so: L = [①; ②[.",
    K(2), [6, 7], ["9 - 3", "5 + 2"], ["3 * 2", "10 - 3"], "Erst beide Ungleichungen einzeln lösen.", "x ≥ 6 und x < 7. Das Intervall ist [6; 7[.",
    {0: [(12, None, "3 addiert statt abgezogen")]}, hinweis=GZ), thema=INT)
neu(f, "schreiben", "FD", FDZ("Kim schreibt „alle Zahlen größer als −1 und höchstens 4“ als Intervall.",
    [("Die untere Grenze −1: „größer als“, also gehört −1 nicht dazu. Die Klammer zeigt weg: ]−1.", True), ("Die obere Grenze 4: „höchstens“, also gehört 4 dazu. Die Klammer zeigt zur Zahl: 4].", True), ("Zusammen: L = ]−1; 4[.", False)],
    "Gehört die 4 dazu? Dann muss die Klammer zur 4 hin zeigen.", "Zeile 2 sagt: 4 gehört dazu. Also L = ]−1; 4]."), thema=INT)
neu(f, "schreiben", "VW", W("Ein Paket darf mindestens 2 kg und höchstens 9 kg wiegen. Wie schreibst du die erlaubten Gewichte als Intervall?",
    "[2; 9], denn beide Grenzen gehören dazu",
    [("]2; 9[", "beide Grenzen ausgeschlossen"), ("[2; 9[", "„höchstens“ als „kleiner als“ gelesen"), ("]2; 9]", "„mindestens“ als „größer als“ gelesen")],
    "„Mindestens“ und „höchstens“ lassen die Grenze zu.", "Mindestens 2 heißt: 2 gehört dazu. Höchstens 9 heißt: 9 gehört dazu. L = [2; 9].",
    lambda: (2 >= 2 and 9 <= 9) and not (2 > 2) and not (9 < 9)), g="einkleidung", thema=INT)
# enthalten
neu(f, "enthalten", "LW", L("Das Intervall [−1; 4[ enthält die ganzen Zahlen −1, 0, 1, 2 und ①. Die Zahl 4 gehört nicht dazu. Insgesamt sind es ② ganze Zahlen.",
    K(2), [3, 5], ["4 - 1", "4 - (-1)"], ["2 + 1", str(len([x for x in range(-1, 4)]))], "Zähle von der unteren Grenze bis kurz vor der oberen.", "−1, 0, 1, 2, 3: fünf Zahlen.",
    {1: [(6, None, "die Grenze 4 mitgezählt")]}, hinweis=GZ), thema=INT)
neu(f, "enthalten", "FD", FDZ("Kim prüft, welche der Zahlen −2, 0, 3 und 7 zum Intervall ]−2; 7] gehören.",
    [("−2 ist die Grenze. Die Klammer zeigt weg, also gehört −2 nicht dazu.", not (-2 > -2)), ("0 und 3 liegen zwischen −2 und 7, also gehören sie dazu.", -2 < 0 <= 7 and -2 < 3 <= 7), ("7 ist die Grenze. Die Klammer zeigt weg, also gehört 7 nicht dazu.", not (-2 < 7 <= 7))],
    "Welche Seite der 7 ist die Klammer, die „]“ oder „[“?", "Am Ende steht „]“. Das ist die Klammer zur Zahl hin: 7 gehört dazu."), thema=INT)
neu(f, "enthalten", "VW", W("Wie viele ganze Zahlen liegen im Intervall [−3; 4]? Welche Rechnung ist richtig?",
    "4 − (−3) + 1 = 8, denn beide Grenzen gehören dazu",
    [("4 − (−3) = 7", "den Abstand gerechnet, aber eine Grenze nicht mitgezählt"), ("4 − (−3) − 1 = 6", "beide Grenzen nicht mitgezählt"), ("4 − 3 + 1 = 2", "das Minus bei −3 übersehen")],
    "Nimm als Beispiel [1; 3]: Wie viele ganze Zahlen sind das?", "Beide Grenzen zählen mit: −3, −2, −1, 0, 1, 2, 3, 4 sind 8 Zahlen. Rechnung: 4 + 3 + 1 = 8.",
    lambda: len([x for x in range(-3, 5)]) == 8 and 4 - (-3) != 8 and 4 - (-3) - 1 != 8 and 4 - 3 + 1 != 8), g="mehrschritt", thema=INT)
# beurteilen
neu(f, "beurteilen", "LW", L("Kim sagt: „]1; 6[ und [2; 5] enthalten dieselben ganzen Zahlen.“ In ]1; 6[ liegen ① ganze Zahlen. In [2; 5] liegen ② ganze Zahlen. Kims Aussage stimmt, wenn beide Zahlen gleich sind.",
    K(2), [4, 4], ["6 - 1 - 1", "5 - 2 + 1"], ["2 + 2", str(len([x for x in range(2, 6)]))], "Schreibe die ganzen Zahlen beider Intervalle auf.", "In ]1; 6[ liegen 2, 3, 4, 5. In [2; 5] liegen 2, 3, 4, 5. Beide Mengen sind gleich.",
    {0: [(5, None, "eine Grenze mitgezählt")]}, hinweis=GZ), thema=INT)
neu(f, "beurteilen", "VW", W("Kim sagt: „Jede Zahl im Intervall [0; 5] liegt auch im Intervall ]0; 6[.“ Wie prüfst du das?",
    "Es stimmt nicht: 0 liegt in [0; 5], aber nicht in ]0; 6[",
    [("Es stimmt, denn 5 ist kleiner als 6", "nur die obere Grenze verglichen"), ("Es stimmt, denn beide Intervalle beginnen bei 0", "die Klammern übersehen"), ("Es stimmt nicht: 5 liegt in [0; 5], aber nicht in ]0; 6[", "5 gehört zu ]0; 6[")],
    "Prüfe die Grenzen einzeln, besonders die Klammern.", "0 gehört zu [0; 5], aber nicht zu ]0; 6[. Ein Gegenbeispiel genügt: Die Aussage ist falsch.",
    lambda: (0 <= 0 <= 5) and not (0 < 0 < 6) and (0 < 5 < 6)), g="mehrschritt", thema=INT)

# ═════════════════════ Kind 1 · Flug a1 · Einfache Gleichungen ═════════════════════
f = "a1"
neu(f, "zwei_schritte", "FD", FDZ("Kim löst 2 · x − 5 = 17.",
    [("Erst 5 abziehen: 2 · x = 12.", 17 - 5 == 17 + 5), ("Dann durch 2 teilen: x = 6.", 12 // 2 == 6), ("Die Lösung ist x = 6.", True)],
    "Der letzte Schritt war „minus 5“. Wie machst du ihn rückgängig?", "Minus 5 macht man mit plus 5 rückgängig: 2 · x = 22, also x = 11. Probe: 2 · 11 − 5 = 17."))
neu(f, "probe", "LW", L("Kim meint, dass x = 7 die Gleichung 4 · x − 5 = 19 löst. Probe: 4 · 7 = ①. Dann ① − 5 = ②. Das ist nicht 19, also hat Kim sich geirrt. Rückwärts: 19 + 5 = 24 und 24 : 4 = ③.",
    K(3), [28, 23, 6], ["4 * 7", "4 * 7 - 5", "(19 + 5) // 4"], ["7 * 4", "28 - 5", "24 / 4"], "Setze erst x ein, rechne dann Mal vor Minus.", "4 · 7 = 28, 28 − 5 = 23. Das ist nicht 19. Richtig ist x = 6.",
    {1: [(33, None, "5 addiert statt abgezogen")]}, hinweis=GZ))
neu(f, "aufstellen", "LW", L("Ich denke mir eine Zahl x. Das Dreifache von x, vermindert um 4, ergibt 17. Gleichung: 3 · x − 4 = 17. Rückwärts: 17 + 4 = ①. Dann ① : 3 = ②. Die gedachte Zahl ist ②.",
    K(2), [21, 7], ["17 + 4", "(17 + 4) // 3"], ["20 + 1", "7"], "Kehre die Schritte in umgekehrter Reihenfolge um.", "17 + 4 = 21. 21 : 3 = 7. Probe: 3 · 7 − 4 = 17.",
    {1: [(13, None, "erst durch 3 geteilt, dann 4 addiert")]}, hinweis=GZ))
neu(f, "aufstellen", "FD", FDZ("Das Vierfache einer Zahl, um 6 vermehrt, ergibt 30. Kim sucht die Zahl.",
    [("Die gesuchte Zahl heißt x.", True), ("Das Vierfache ist 4 · x, um 6 vermehrt: 4 · x + 6 = 30.", True), ("Rückwärts: 30 − 6 = 24 und 24 : 4 = 6. Die Zahl ist 24.", 24 // 4 == 24)],
    "Was hast du am Ende ausgerechnet: x oder 4 · x?", "24 ist 4 · x. Danach hat Kim noch durch 4 geteilt: x = 6. Die gesuchte Zahl ist 6."))
neu(f, "ohne_loesung", "LW", L("Hat 5 · x = 22 eine Lösung in den natürlichen Zahlen? Rechne 22 : 5 = ① Rest ②. Weil ein Rest bleibt, geht die Teilung nicht auf. Es gibt keine Lösung.",
    K(2), [4, 2], ["22 // 5", "22 % 5"], ["20 // 5", "22 - 20"], "Wie oft passt die 5 ganz in die 22?", "5 passt 4-mal in 22. 4 · 5 = 20, es bleibt der Rest 2.",
    {0: [(5, None, "aufgerundet statt abgerundet")]}, hinweis=GZ))

# ═════════════════════ Kind 1 · Flug d1 · Daten darstellen ═════════════════════
f = "d1"
neu(f, "absolute_haeufigkeit", "FD", FDZ("Kim hat 20-mal gewürfelt. Seine Strichliste: Augenzahl 1 dreimal, 2 fünfmal, 3 viermal, 4 zweimal, 5 viermal, 6 dreimal.",
    [("Alle Häufigkeiten zusammen müssen 20 ergeben.", True), ("3 + 5 + 4 + 2 + 4 + 3 = 20.", 3 + 5 + 4 + 2 + 4 + 3 == 20), ("Die Strichliste passt also zu 20 Würfen.", True)],
    "Rechne die Summe der sechs Anzahlen selbst nach.", "3 + 5 + 4 + 2 + 4 + 3 = 21. Die Liste hat einen Strich zu viel."))
neu(f, "absolute_haeufigkeit", "VW", W("25 Kinder werden nach ihrem Haustier gefragt: 9 haben einen Hund, 7 eine Katze, 4 einen Fisch. Alle anderen haben kein Tier. Wie findest du die Zahl der Kinder ohne Tier?",
    "25 − (9 + 7 + 4) = 5", [("9 + 7 + 4 = 20", "die Kinder mit Tier gezählt"), ("25 − 9 = 16", "nur eine Tierart abgezogen"), ("25 + 20 = 45", "addiert statt abgezogen")],
    "Alle Gruppen zusammen sind die Gesamtzahl.", "Kinder mit Tier: 9 + 7 + 4 = 20. Ohne Tier: 25 − 20 = 5.",
    lambda: 25 - (9 + 7 + 4) == 5 and 9 + 7 + 4 != 5 and 25 - 9 != 5 and 25 + 20 != 5), g="einkleidung")
neu(f, "relative_haeufigkeit", "FD", FDZ("Bei 40 Würfen fällt 12-mal die Sechs. Kim berechnet die relative Häufigkeit.",
    [("Relative Häufigkeit = Anzahl : Gesamtzahl.", True), ("12 : 40 = 0,3.", 12 / 40 == 0.3), ("0,3 sind 3 %.", 0.3 == 0.03)],
    "0,3 sind 30 Hundertstel. Wie viel Prozent ist das?", "0,3 = 30/100 = 30 %. Kim hat die Prozentzahl um eine Stelle verschoben."))
neu(f, "tabelle_auswerten", "LW", L("In einer Tabelle stehen die Anzahlen Rot 6, Blau 9 und Grün 5. Summe: 6 + 9 + 5 = ①. Der Anteil von Blau ist 9 von ①. In Prozent sind das ② %.",
    K(2), [20, 45], ["6 + 9 + 5", "9 * 100 // (6 + 9 + 5)"], ["2 * 10", "9 * 5"], "Zähle zuerst alle Anzahlen zusammen. Dann erweiterst du den Bruch auf Hundertstel.", "9/20 = 45/100 = 45 %.",
    {1: [(9, None, "die Anzahl als Prozentzahl genommen")]}, hinweis=GZ))
neu(f, "tabelle_auswerten", "FD", FDZ("Eine Tabelle zeigt, wie 30 Kinder zur Schule kommen: Bus 12, Rad 8, zu Fuß 10.",
    [("Summe: 12 + 8 + 10 = 30.", 12 + 8 + 10 == 30), ("Der Anteil Bus ist 12 von 30, also 12 : 30 = 0,4 = 40 %.", 12 / 30 == 0.4), ("Der Anteil zu Fuß ist 10 von 12.", 12 == 30)],
    "Durch welche Zahl teilt man, um einen Anteil zu bekommen?", "Man teilt immer durch die Summe aller Anzahlen: 10 von 30 sind etwa 33 %."))
neu(f, "saeulendiagramm", "LW", L("In einem Säulendiagramm steht 1 cm Höhe für 5 Kinder. Eine Säule ist 6 cm hoch. Sie gehört zu 6 · 5 = ① Kindern. Eine andere Säule gehört zu 35 Kindern. Sie ist 35 : 5 = ② cm hoch.",
    K(2), [30, 7], ["6 * 5", "35 // 5"], ["5 * 6", "30 + 5 - 35 + 7"], "Höhe mal Maßstab gibt die Anzahl.", "6 · 5 = 30 Kinder. 35 : 5 = 7 cm.",
    {1: [(175, None, "mal 5 statt geteilt durch 5")]}, hinweis=GZ))
neu(f, "saeulendiagramm", "FD", FDZ("Im Säulendiagramm steht 1 cm Höhe für 4 Kinder. Eine Säule ist 7 cm hoch. Kim liest sie ab.",
    [("Jeder Zentimeter steht für 4 Kinder.", True), ("Die Säule gehört also zu 7 : 4 Kindern, das sind weniger als 2 Kinder.", 7 // 4 >= 28), ("Eine Säule für 12 Kinder wäre 12 : 4 = 3 cm hoch.", 12 // 4 == 3)],
    "Aus der Höhe in cm bekommst du die Anzahl mit mal oder mit geteilt?", "Höhe mal Maßstab: 7 · 4 = 28 Kinder."))
neu(f, "kreisdiagramm", "LW", L("Ein Kreis hat 360°. 10 % davon sind 360° : 10 = ①°. 30 % sind dreimal so viel: ②°.",
    K(2), [36, 108], ["360 // 10", "3 * (360 // 10)"], ["36", "360 * 30 // 100"], "30 % sind dreimal 10 %.", "10 % sind 36°. 30 % sind 3 · 36° = 108°.",
    {0: [(3600, None, "mal 10 statt geteilt durch 10")]}, hinweis=GZ))
neu(f, "irrefuehrend", "LW", L("Die Achse eines Säulendiagramms beginnt bei 40 statt bei 0. Säule A reicht bis 50, Säule B bis 100. Die sichtbare Höhe von B ist (100 − 40) : (50 − 40) = ①-mal so groß wie die von A. In Wahrheit ist B nur 100 : 50 = ②-mal so hoch.",
    K(2), [6, 2], ["(100 - 40) // (50 - 40)", "100 // 50"], ["60 / 10", "50 * 2 // 50"], "Zieh bei der gekürzten Achse erst 40 ab.", "Sichtbar: 60 und 10, also 6-mal so groß. In Wahrheit: 100 : 50 = 2.",
    {0: [(2, None, "den Achsenanfang nicht beachtet")]}, hinweis=GZ))

# ═════════════════════ Kind 1 · Flug g1 · Größen und Einheiten ═════════════════════
f = "g1"
neu(f, "schaetzen", "LW", L("Eine Tür ist etwa 2 m hoch. Eine Schokoladentafel wiegt etwa 100 g. 10 Tafeln wiegen ① g. Das sind ② kg.",
    K(2), [1000, 1], ["10 * 100", "10 * 100 // 1000"], ["100 * 10", "1000 // 1000"], "10 mal 100, dann in kg umrechnen.", "10 · 100 g = 1 000 g = 1 kg.",
    {1: [(1000, None, "nicht umgerechnet")]}, hinweis=GZ))
neu(f, "schaetzen", "FD", FDZ("Kim soll schätzen, wie hoch sein Klassenzimmer ist.",
    [("Bezugsgröße: Eine Tür ist etwa 2 m hoch.", True), ("Das Zimmer ist etwa so hoch wie zwei Türen übereinander.", True), ("Es ist also etwa 2 · 2 = 4 cm hoch.", False)],
    "Eine Tür ist 2 m hoch. In welcher Einheit rechnest du weiter?", "2 · 2 m = 4 m. Bei einer Größe gehört immer die richtige Einheit zur Zahl."))
neu(f, "laenge", "FD", FDZ("Kim rechnet 3 km 40 m in Meter um.",
    [("1 km = 1 000 m.", True), ("3 km = 3 000 m.", 3 * 1000 == 3000), ("3 000 m + 40 m = 3 400 m.", 3000 + 40 == 3400)],
    "Wie viele Stellen hat 3 040 im Vergleich zu 3 400?", "3 000 + 40 = 3 040. Also 3 km 40 m = 3 040 m."))
neu(f, "masse", "LW", L("2 kg 350 g sind 2 · 1 000 g + 350 g = ① g. 4 500 g sind 4 kg und ② g.",
    K(2), [2350, 500], ["2 * 1000 + 350", "4500 - 4 * 1000"], ["2000 + 350", "4500 % 1000"], "1 kg sind 1 000 g.", "2 000 g + 350 g = 2 350 g. 4 500 g − 4 000 g = 500 g.",
    {0: [(2035, "fb.stellenwert.eine_stelle_daneben", "350 als 35 behandelt")]}, hinweis=GZ))
neu(f, "masse", "FD", FDZ("Kim rechnet 7,5 kg in Gramm um.",
    [("1 kg = 1 000 g.", True), ("7 kg = 7 000 g.", 7 * 1000 == 7000), ("0,5 kg = 50 g.", 0.5 * 1000 == 50), ("Zusammen sind es 7 050 g.", 7000 + 50 == 7050)],
    "Eine halbe Tonne? Nein, ein halbes Kilogramm: Wie viel ist das?", "Ein halbes Kilogramm sind 500 g. Zusammen 7 000 g + 500 g = 7 500 g."))
neu(f, "masse", "VW", W("Ein Paket wiegt 2 kg 400 g. Drei solche Pakete werden verschickt. Wie rechnest du das Gesamtgewicht richtig?",
    "Alles in g umrechnen: 2 400 g · 3 = 7 200 g, das sind 7 kg 200 g",
    [("2 kg · 3 + 400 g = 6 kg 400 g", "nur die kg verdreifacht"), ("2 kg 400 g + 3 = 2 kg 403 g", "3 einfach addiert"), ("2 400 · 3 = 7 200 kg", "die Einheit falsch gesetzt")],
    "Rechne beide Teile des Pakets mit dem Faktor 3.", "2 400 g · 3 = 7 200 g = 7 kg 200 g.",
    lambda: 2400 * 3 == 7200 and 2 * 3 * 1000 + 400 != 7200 and 2400 + 3 != 7200), g="einkleidung")
neu(f, "zeit", "FD", FDZ("Ein Film beginnt um 17:45 Uhr und dauert 2 h 30 min. Kim berechnet das Ende.",
    [("17:45 Uhr plus 15 min ist 18:00 Uhr.", True), ("Dann bleiben noch 2 h 30 min − 15 min = 2 h 25 min.", 30 - 15 == 25), ("18:00 Uhr plus 2 h 25 min ist 20:25 Uhr.", True)],
    "Rechne 30 min − 15 min noch einmal nach.", "30 min − 15 min = 15 min. Es bleiben 2 h 15 min, der Film endet um 20:15 Uhr."))
neu(f, "zeit", "VW", W("Ein Zug fährt um 9:50 Uhr ab und kommt um 12:20 Uhr an. Wie rechnest du die Fahrzeit richtig?",
    "Bis zur vollen Stunde: 10 min bis 10:00, 2 h bis 12:00, 20 min bis 12:20. Das sind 2 h 30 min",
    [("12 − 9 = 3 h und 50 − 20 = 30 min. Das sind 3 h 30 min", "Stunden und Minuten einzeln abgezogen und falsch herum"), ("12,20 − 9,50 = 2,70. Das sind 2 h 70 min", "mit Dezimalzahlen statt mit Zeit gerechnet"), ("12:20 − 10:00 = 2 h 20 min", "die Minuten bis 10:00 vergessen")],
    "Gehe erst bis zur vollen Stunde, dann weiter.", "10 min + 2 h + 20 min = 2 h 30 min. Probe: 9:50 + 2 h 30 min = 12:20.",
    lambda: (12 * 60 + 20) - (9 * 60 + 50) == 150 and 150 == 2 * 60 + 30 and 3 * 60 + 30 != 150 and 2 * 60 + 70 != 150 and 140 != 150), g="mehrschritt")
neu(f, "kommaschreibweise", "LW", L("Hinter dem Komma bekommt jede kleinere Einheit ihre Stellen. 2,35 m sind 2 m 35 cm. Das sind insgesamt ① cm. 7,04 m sind 7 m ② cm.",
    K(2), [235, 4], ["2 * 100 + 35", "704 - 700"], ["200 + 35", "4"], "Bei m und cm sind es zwei Stellen hinter dem Komma.", "2 m = 200 cm, dazu 35 cm: 235 cm. 7,04 m = 7 m 04 cm = 7 m 4 cm.",
    {1: [(40, "fb.stellenwert.eine_stelle_daneben", "04 als 40 gelesen")]}, hinweis=GZ))
neu(f, "rechnen", "LW", L("Ein Seil ist 3 m 20 cm lang, ein zweites 85 cm. In cm: 3 m 20 cm = ① cm. Zusammen sind die Seile ① cm + 85 cm = ② cm lang.",
    K(2), [320, 405], ["3 * 100 + 20", "3 * 100 + 20 + 85"], ["300 + 20", "320 + 85"], "Beide Längen in dieselbe Einheit bringen.", "3 m 20 cm = 320 cm. 320 cm + 85 cm = 405 cm.",
    {1: [(328, None, "nur 8 cm dazugezählt")]}, hinweis=GZ))
neu(f, "massstab", "LW", L("Eine Karte hat den Maßstab 1 : 50 000. Auf der Karte sind es 4 cm. In Wirklichkeit sind es 4 · 50 000 = ① cm. Das sind ② m und ③ km.",
    K(3), [200000, 2000, 2], ["4 * 50000", "4 * 50000 // 100", "4 * 50000 // 100000"], ["50000 * 2 * 2", "4 * 500", "4 // 2"], "100 cm sind 1 m. 1 000 m sind 1 km.", "4 · 50 000 = 200 000 cm = 2 000 m = 2 km.",
    {1: [(20000, None, "nur durch 10 geteilt")]}, hinweis=GZ))
neu(f, "massstab", "VW", W("Auf einer Karte 1 : 25 000 sind zwei Orte 6 cm voneinander entfernt. Wie weit sind sie in Wirklichkeit entfernt?",
    "6 · 25 000 cm = 150 000 cm = 1 500 m, also 1,5 km",
    [("6 · 25 000 = 150 000 m, also 150 km", "die Einheit cm nicht umgerechnet"), ("6 · 25 = 150 m", "Nullen des Maßstabs weggelassen"), ("25 000 : 6 ≈ 4 167 cm", "geteilt statt malgenommen")],
    "Wirklichkeit = Kartenlänge mal Maßstabszahl. Die Einheit bleibt zunächst cm.", "6 cm · 25 000 = 150 000 cm. 100 cm = 1 m: 1 500 m. 1 000 m = 1 km: 1,5 km.",
    lambda: 6 * 25000 // 100 == 1500 and 6 * 25 != 1500 and 6 * 25000 // 1000 != 1500 and 25000 // 6 != 6 * 25000), g="mehrschritt")
neu(f, "verstehen", "LW", L("Ein Schulbus ist etwa 12 m lang. Das sind ① cm. Ein Schulweg ist 2 km lang. Das sind ② m.",
    K(2), [1200, 2000], ["12 * 100", "2 * 1000"], ["120 * 10", "2000"], "1 m sind 100 cm und 1 km sind 1 000 m.", "12 · 100 cm = 1 200 cm. 2 · 1 000 m = 2 000 m.",
    {0: [(120, None, "mit 10 statt mit 100 umgerechnet")]}, hinweis=GZ))
neu(f, "verstehen", "FD", FDZ("Kim behauptet: „Ein Bleistift ist 19 m lang.“ Er prüft die Angabe.",
    [("Eine Tür ist etwa 2 m hoch.", True), ("19 m sind fast zehn Türen übereinander.", abs(19 / 2 - 10) < 1), ("Das passt zu einem Bleistift.", False)],
    "Passt ein Bleistift neben eine Tür, die so hoch ist wie zehn Türen?", "Ein Bleistift ist etwa 19 cm lang, nicht 19 m. Die Einheit war falsch."))
neu(f, "verstehen", "VW", W("Kim sagt: „Ein Buch wiegt 500 kg.“ Wie prüfst du das?",
    "Ein Mensch wiegt etwa 50 kg. 500 kg wären zehn Menschen. Das passt nicht zu einem Buch",
    [("Eine Schokoladentafel wiegt 100 g. 500 kg sind etwa 5 Tafeln. Das passt zu einem Buch", "kg und g nicht umgerechnet"), ("500 kg sind 500 000 g. Das ist nur eine große Zahl, also passt es", "kein Vergleich mit einer Bezugsgröße"), ("Ein Buch hat Seiten und kg ist eine Einheit für Gewicht, also passt es", "nur auf die Einheit geschaut")],
    "Vergleiche mit etwas, dessen Gewicht du kennst.", "500 : 50 = 10: Das wären zehn Menschen. Ein Buch wiegt eher 500 g. Die Einheit war falsch.",
    lambda: 500 / 50 == 10 and 500 / 0.1 != 5), g="mehrschritt")

# ═════════════════════ Kind 2 · Flug g8 · Prozent mit verändertem Grundwert ═════════════════════
f = "g8"
neu(f, "faktor", "FD", FDZ("Kim bestimmt den Wachstumsfaktor für 15 % Rabatt.",
    [("Beim Rabatt zahlt man noch 100 % − 15 % = 85 %.", 100 - 15 == 85), ("85 % sind 0,85.", 85 / 100 == 0.85), ("Der Faktor ist also 1,15.", 1.15 == 0.85)],
    "Bei einem Rabatt wird der Preis kleiner. Ist der Faktor dann größer oder kleiner als 1?", "Beim Rabatt ist der Faktor 0,85. 1,15 wäre ein Aufschlag von 15 %."))
neu(f, "vermehrt", "LW", L("Ein Preis von 80 € steigt um 25 %. Der Wachstumsfaktor ist 1,25. 25 % von 80 € sind ① €. Neuer Preis: 80 € + ① € = ② €.",
    K(2), [20, 100], ["80 * 25 // 100", "80 + 80 * 25 // 100"], ["80 // 4", "80 * 125 // 100"], "25 % sind ein Viertel.", "25 % von 80 € = 20 €. 80 € + 20 € = 100 €. Mit Faktor: 80 · 1,25 = 100.",
    {1: [(105, "fb.prozent.prozente_addiert", "25 € statt 25 % dazugezählt")]}, hinweis=GZ))
neu(f, "vermehrt", "FD", FDZ("Ein Fahrrad kostet 200 €. Der Preis steigt um 10 %. Kim berechnet den neuen Preis.",
    [("Der Wachstumsfaktor ist 1,10.", 100 + 10 == 110), ("200 · 1,10 = 22.", 200 * 1.1 == 22), ("Das Fahrrad kostet jetzt 22 €.", True)],
    "Ein Preis, der um 10 % steigt, wird nicht kleiner als vorher.", "200 · 1,10 = 220. Das Fahrrad kostet jetzt 220 €."))
neu(f, "vermindert", "LW", L("Eine Jacke kostet 60 €. Sie wird um 20 % billiger. 20 % von 60 € sind ① €. Neuer Preis: 60 € − ① € = ② €.",
    K(2), [12, 48], ["60 * 20 // 100", "60 - 60 * 20 // 100"], ["60 // 5", "60 * 80 // 100"], "20 % sind ein Fünftel.", "20 % von 60 € = 12 €. 60 € − 12 € = 48 €. Mit Faktor: 60 · 0,8 = 48.",
    {1: [(72, "fb.prozent.prozente_addiert", "aufgeschlagen statt abgezogen")]}, hinweis=GZ))
neu(f, "vermindert", "FD", FDZ("Ein Spiel kostet 50 €. Es gibt 30 % Rabatt. Kim berechnet den neuen Preis.",
    [("Man zahlt noch 100 % − 30 % = 70 %.", 100 - 30 == 70), ("Der Faktor ist 0,7.", 70 / 100 == 0.7), ("50 · 0,7 = 30, also kostet das Spiel 30 €.", 50 * 0.7 == 30)],
    "Rechne 50 · 0,7 noch einmal: 5 · 7 = 35.", "50 · 0,7 = 35. Das Spiel kostet 35 €."))
neu(f, "zurueck", "VW", W("Nach 20 % Rabatt kostet ein Schal 48 €. Wie findest du den alten Preis?",
    "48 : 0,8 = 60 €, denn der neue Preis ist 80 % vom alten",
    [("48 · 1,2 = 57,60 €", "20 % auf den neuen Preis aufgeschlagen"), ("48 + 20 = 68 €", "die Prozentzahl als Euro addiert"), ("48 : 0,2 = 240 €", "durch den Rabatt-Anteil statt den Rest-Anteil geteilt")],
    "Nach 20 % Rabatt sind noch wie viel Prozent vom alten Preis übrig?", "Der neue Preis ist 80 % des alten: 0,8 · alt = 48. Also alt = 48 : 0,8 = 60.",
    lambda: 48 / 0.8 == 60 and 48 * 1.2 != 60 and 48 + 20 != 60 and 48 / 0.2 != 60 and 60 * 0.8 == 48), g="umkehr")
neu(f, "prozentsatz", "LW", L("Ein Preis sinkt von 80 € auf 60 €. Die Änderung ist 80 − 60 = ① €. Bezogen auf den alten Preis sind ① von 80 genau ② %.",
    K(2), [20, 25], ["80 - 60", "(80 - 60) * 100 // 80"], ["10 + 10", "80 // 4 + 5"], "Teile die Änderung durch den alten Preis.", "20 : 80 = 1/4 = 25 %.",
    {1: [(33, None, "durch den neuen Preis geteilt")]}, hinweis=GZ))
neu(f, "mehrfach", "LW", L("Ein Preis von 200 € steigt erst um 10 % und dann noch einmal um 10 %. 10 % von 200 € sind ① €. Nach dem ersten Mal kostet es ② €. 10 % von ② € sind ③ €. Nach dem zweiten Mal kostet es ④ €.",
    K(4), [20, 220, 22, 242], ["200 * 10 // 100", "200 + 200 * 10 // 100", "(200 + 200 * 10 // 100) * 10 // 100", "200 * 110 * 110 // 10000"], ["200 // 10", "220", "22", "200 * 121 // 100"], "Beim zweiten Mal gehören die 10 % zum neuen Preis.", "200 + 20 = 220. 10 % von 220 sind 22. 220 + 22 = 242. Nicht 240!",
    {3: [(240, "fb.prozent.prozente_addiert", "zweimal 20 € dazugezählt")]}, hinweis=GZ))
neu(f, "formel", "LW", L("Ein Wert verdoppelt sich jedes Jahr, also ist q = 2. Am Anfang sind es 300 €. Nach 3 Jahren: K = 300 · 2³. Es ist 2³ = ①. Also ist K = 300 · ① = ② €.",
    K(2), [8, 2400], ["2 ** 3", "300 * 2 ** 3"], ["2 * 2 * 2", "300 * 8"], "2³ heißt 2 · 2 · 2.", "2³ = 8. 300 · 8 = 2 400 €.",
    {0: [(6, "fb.potenz.basis_mal_hochzahl", "2 · 3 gerechnet")]}, hinweis=GZ))
neu(f, "formel", "FD", FDZ("Kim berechnet, wie viel 2 000 € bei 5 % Zinsen nach 2 Jahren wert sind.",
    [("Der Faktor ist q = 1,05.", True), ("K₂ = 2 000 · 1,05 · 2 = 4 200.", 2000 * 1.05 ** 2 == 2000 * 1.05 * 2), ("Das Kapital beträgt nach 2 Jahren also 4 200 €.", True)],
    "Die Hochzahl n gehört an den Faktor q.", "K₂ = 2 000 · 1,05² = 2 205. Kim hat den Faktor mit 2 multipliziert statt ihn zu quadrieren."))
neu(f, "formel", "VW", W("500 € werden 3 Jahre lang mit 4 % verzinst. Welche Rechnung gibt das Kapital am Ende?",
    "500 · 1,04³ ≈ 562,43 €",
    [("500 · 1,04 · 3 = 1 560 €", "den Faktor mit 3 multipliziert statt hoch 3"), ("500 · 1,12 = 560 €", "die Prozentsätze addiert"), ("500 · 0,04³ ≈ 0,03 €", "mit dem Zinssatz statt dem Wachstumsfaktor gerechnet")],
    "Der Wachstumsfaktor bei 4 % ist 1,04. Er wird dreimal angewendet.", "K₃ = 500 · 1,04³ = 500 · 1,124864 ≈ 562,43 €.",
    lambda: round(500 * 1.04 ** 3, 2) == 562.43 and 500 * 1.04 * 3 != 562.43 and 500 * 1.12 != 562.43 and round(500 * 0.04 ** 3, 2) == 0.03), g="mehrschritt")
neu(f, "argumente", "LW", L("Behauptung: „Erst 50 % mehr, dann 50 % weniger ergibt wieder den Anfangswert.“ Prüfe mit 200 €. 50 % von 200 € sind ① €. Nach dem Aufschlag sind es ② €. 50 % von ② € sind ③ €. Nach dem Abschlag sind es ④ €. Das ist nicht 200 €.",
    K(4), [100, 300, 150, 150], ["200 * 50 // 100", "200 + 200 * 50 // 100", "(200 + 200 * 50 // 100) * 50 // 100", "200 + 200 * 50 // 100 - (200 + 200 * 50 // 100) * 50 // 100"], ["200 // 2", "200 * 3 // 2", "300 // 2", "200 * 3 * 1 // (2 * 2)"], "Der Abschlag bezieht sich auf den neuen, größeren Wert.", "200 + 100 = 300. 50 % von 300 sind 150. 300 − 150 = 150, nicht 200.",
    {3: [(200, None, "den Abschlag auf 200 € statt auf 300 € bezogen")]}, hinweis=GZ))
neu(f, "argumente", "VW", W("Kim sagt: „Wenn ein Preis erst um 10 % steigt und dann um 10 % sinkt, ist er danach wieder wie am Anfang.“ Wie prüfst du das?",
    "Mit 100 € rechnen: 100 · 1,1 = 110, dann 110 · 0,9 = 99. Das sind nicht 100 €: Die Aussage ist falsch",
    [("Es stimmt, denn +10 % und −10 % heben sich auf", "Prozentsätze wie Zahlen addiert"), ("Es stimmt, denn 1,1 · 0,9 = 1", "den Faktor falsch ausgerechnet"), ("Die Aussage ist falsch, denn 1,1 · 0,9 = 1,1", "den Faktor falsch ausgerechnet, aber das Urteil getroffen")],
    "Wähle eine einfache Startzahl und rechne beide Schritte mit Faktoren.", "100 € · 1,1 = 110 €. 110 € · 0,9 = 99 €. Die 10 % beziehen sich auf verschiedene Grundwerte.",
    lambda: abs(100 * 1.1 * 0.9 - 99) < 1e-9 and abs(1.1 * 0.9 - 1) > 0.001 and abs(1.1 * 0.9 - 1.1) > 0.001), g="mehrschritt")

# ═════════════════════ Kind 2 · Flug f1 · Funktionsbegriff ═════════════════════
f = "f1"
neu(f, "eindeutig", "LW", L("Die Zuordnung x ↦ x² ordnet der Zahl 3 den Wert ① zu. Der Zahl −3 ordnet sie den Wert ② zu. Jede Eingabe hat genau einen Wert. Also ist die Zuordnung eine Funktion.",
    K(2), [9, 9], ["3 ** 2", "(-3) ** 2"], ["3 * 3", "(-3) * (-3)"], "Quadrieren heißt: mit sich selbst malnehmen.", "3² = 9 und (−3)² = (−3) · (−3) = 9. Zwei Eingaben dürfen denselben Wert haben.",
    {1: [(-9, "fb.reihenfolge.minus_ins_quadrat", "das Minus nicht mitquadriert")]}, hinweis=GZ))
neu(f, "mengen", "LW", L("Die Funktion f(x) = 12 : (x − 5) ist nicht für jede Zahl erlaubt. Für x = 7 ist der Nenner 7 − 5 = ①. Also ist f(7) = 12 : ① = ②. Für x = 5 wäre der Nenner 0. Dann darf man nicht teilen.",
    K(2), [2, 6], ["7 - 5", "12 // (7 - 5)"], ["1 + 1", "3 * 2"], "Rechne erst die Klammer aus.", "7 − 5 = 2. 12 : 2 = 6.",
    {1: [(5, None, "x − 5 mit 12 : 7 verwechselt")]}, hinweis=GZ))
neu(f, "mengen", "FD", FDZ("Kim bestimmt die Definitionsmenge von f(x) = 6 : (x + 2).",
    [("Man darf nicht durch 0 teilen.", True), ("x + 2 = 0 gilt für x = 2.", 2 + 2 == 0), ("Also ist D = ℝ ohne {2}.", True)],
    "Setze x = 2 in den Nenner ein: Kommt 0 heraus?", "x + 2 = 0 gilt für x = −2. Richtig: D = ℝ ohne {−2}."))
neu(f, "mengen", "VW", W("Welche Zahl darf man in g(x) = 10 : (2x − 6) nicht einsetzen?",
    "x = 3, denn dann ist der Nenner 2 · 3 − 6 = 0", [("x = 6", "die Zahl aus dem Nenner übernommen"), ("x = −3", "das Vorzeichen vertauscht"), ("x = 5", "10 : 2 gerechnet")],
    "Der Nenner darf nicht 0 sein. Wann ist 2x − 6 gleich 0?", "2x − 6 = 0 ergibt 2x = 6 und x = 3. Nur dort ist der Nenner 0.",
    lambda: 2 * 3 - 6 == 0 and 2 * 6 - 6 != 0 and 2 * (-3) - 6 != 0 and 2 * 5 - 6 != 0), g="mehrschritt")
neu(f, "funktionswert", "FD", FDZ("Kim berechnet f(−2) für f(x) = x² − 3x.",
    [("Einsetzen: (−2)² − 3 · (−2).", True), ("(−2)² = −4 und −3 · (−2) = 6.", (-2) ** 2 == -4), ("Zusammen: −4 + 6 = 2.", -4 + 6 == 2)],
    "Eine Zahl mal sich selbst: Kann das Ergebnis negativ sein, wenn die Zahl negativ ist?", "(−2)² = (−2) · (−2) = 4. Dann 4 + 6 = 10."))
neu(f, "funktionswert", "VW", W("Für f(x) = 2x² + 1 soll f(−3) berechnet werden. Welche Rechnung ist richtig?",
    "2 · (−3)² + 1 = 2 · 9 + 1 = 19",
    [("2 · (−3)² + 1 = 2 · (−9) + 1 = −17", "das Minus nicht mitquadriert"), ("(2 · (−3))² + 1 = (−6)² + 1 = 37", "die 2 mit quadriert"), ("2 · 3 + 1 = 7", "x² mit x verwechselt")],
    "Quadrieren kommt vor dem Malnehmen mit 2.", "(−3)² = 9. Dann 2 · 9 = 18 und 18 + 1 = 19.",
    lambda: 2 * (-3) ** 2 + 1 == 19 and 2 * (-9) + 1 != 19 and (2 * -3) ** 2 + 1 != 19 and 2 * 3 + 1 != 19), g="mehrschritt")
neu(f, "stelle", "FD", FDZ("Für f(x) = 3x − 4 wird die Zahl x gesucht, bei der f(x) = 11 gilt. Kim rechnet.",
    [("Gesucht ist x mit f(x) = 11.", True), ("Ich setze 11 für x ein: f(11) = 3 · 11 − 4 = 29.", False), ("Also ist x = 29.", True)],
    "11 ist das Ergebnis, nicht die Eingabe. Was löst du stattdessen?", "Du löst 3x − 4 = 11: 3x = 15, also x = 5. Probe: 3 · 5 − 4 = 11."))
neu(f, "wertetabelle", "LW", L("Zur Funktion f(x) = 2x + 3 gibt es eine Wertetabelle. Oben steht x, darunter f(x). Für x = 4 ist f(4) = ①. Für x = 10 ist f(10) = ②.",
    K(2), [11, 23], ["2 * 4 + 3", "2 * 10 + 3"], ["8 + 3", "20 + 3"], "Erst mal, dann plus.", "f(4) = 2 · 4 + 3 = 11. f(10) = 2 · 10 + 3 = 23.",
    {0: [(20, "fb.reihenfolge.links_nach_rechts", "2 · (4 + 3) gerechnet")]}, hinweis=GZ))
neu(f, "wertetabelle", "FD", FDZ("Eine Wertetabelle zeigt x = 1, 2, 3, 4 und f(x) = 5, 7, 9, 11. Kim sucht den Term.",
    [("f(x) wächst bei jedem Schritt von x um 2.", True), ("Also hat der Term die Form f(x) = 2x + c.", True), ("Für x = 1 muss 5 herauskommen: 2 · 1 + c = 5, also c = 2. Der Term ist f(x) = 2x + 2.", 2 * 1 + 2 == 5)],
    "Setze zur Probe x = 2 in 2x + 2 ein. Kommt 7 heraus?", "2 · 1 + c = 5 ergibt c = 3. Richtig: f(x) = 2x + 3. Probe: f(2) = 7."))
neu(f, "graph_lesen", "LW", L("Am Graphen von f liest du ab: Bei x = 2 liegt der Graph bei y = 4, bei x = 5 bei y = 13. Von x = 2 bis x = 5 sind es 5 − 2 = ① Schritte nach rechts. Der Graph steigt um 13 − 4 = ②. Pro Schritt steigt er um ② : ① = ③.",
    K(3), [3, 9, 3], ["5 - 2", "13 - 4", "(13 - 4) // (5 - 2)"], ["1 + 1 + 1", "10 - 1", "9 // 3"], "Steigung: Anstieg geteilt durch Schritte.", "5 − 2 = 3. 13 − 4 = 9. 9 : 3 = 3.",
    {2: [(27, None, "mal statt geteilt")]}, hinweis=GZ))
neu(f, "graph_lesen", "FD", FDZ("Der Graph von f steigt gleichmäßig. Er geht durch die Punkte (1 | 3), (2 | 5) und (4 | 9). Kim liest f(3) ab.",
    [("Von (1 | 3) nach (2 | 5) steigt der Graph um 2.", 5 - 3 == 2), ("Bei x = 3 liegt der Graph also zwischen 5 und 9.", 5 < 7 < 9), ("Dort liest Kim f(3) = 8 ab.", 2 * 3 + 1 == 8)],
    "Von (2 | 5) aus geht es um 2 nach oben.", "f(3) = 5 + 2 = 7. Probe: Von (3 | 7) nach (4 | 9) sind es wieder 2."))
neu(f, "nullstellen", "LW", L("Die Nullstelle von f(x) = 2x + 10 ist die Stelle, an der f(x) = 0 gilt. Aus 2x + 10 = 0 folgt x = ①. Der Graph schneidet die x-Achse also im Punkt (① | 0).",
    K(1), [-5], ["-10 // 2"], ["(0 - 10) / 2"], "Bringe erst die 10 auf die andere Seite.", "2x = −10, also x = −5. Der Punkt ist (−5 | 0).",
    {0: [(5, "fb.plusminus.zeichen_des_ergebnisses", "das Minus vergessen")]}, hinweis=GZ))
neu(f, "nullstellen", "FD", FDZ("Kim berechnet die Nullstelle von f(x) = x − 6.",
    [("Ich rechne f(0) = 0 − 6 = −6.", 0 - 6 == -6), ("Also ist die Nullstelle bei x = −6.", False), ("Der Graph schneidet die x-Achse bei (−6 | 0).", True)],
    "Die Nullstelle ist die Stelle x, bei der der Funktionswert 0 ist, nicht umgekehrt.", "Du löst f(x) = 0: x − 6 = 0, also x = 6. f(0) = −6 ist der Schnittpunkt mit der y-Achse."))
neu(f, "punkt_graph", "LW", L("Liegt P(3 | 8) auf dem Graphen von f(x) = 2x + 1? Setze x = 3 ein: f(3) = 2 · 3 + 1 = ①. Der y-Wert von P ist 8, und ① ist nicht 8. Also liegt P nicht auf dem Graphen.",
    K(1), [7], ["2 * 3 + 1"], ["6 + 1"], "Setze die erste Zahl des Punktes in den Term ein.", "f(3) = 6 + 1 = 7. Der Graph geht durch (3 | 7), nicht durch (3 | 8).",
    {0: [(8, None, "den y-Wert des Punktes übernommen")]}, hinweis=GZ))
neu(f, "punkt_graph", "VW", W("Wie prüfst du, ob Q(−2 | 9) auf dem Graphen von f(x) = x² + 5 liegt?",
    "x = −2 einsetzen: (−2)² + 5 = 9. Das ist der y-Wert, also liegt Q auf dem Graphen",
    [("y = 9 einsetzen: 9² + 5 = 86. Das ist nicht −2, also liegt Q nicht auf dem Graphen", "den y-Wert für x eingesetzt"), ("x = −2 einsetzen: −2² + 5 = 1. Das ist nicht 9, also liegt Q nicht auf dem Graphen", "das Minus beim Quadrieren nicht mitgenommen"), ("Nur x² = 4 ansehen: 4 ist nicht 9, also liegt Q nicht auf dem Graphen", "die 5 vergessen")],
    "Setze x aus dem Punkt in den Term ein und vergleiche mit y.", "(−2)² + 5 = 4 + 5 = 9. Der Punkt Q(−2 | 9) liegt auf dem Graphen.",
    lambda: (-2) ** 2 + 5 == 9 and 9 ** 2 + 5 != -2 and -(2 ** 2) + 5 != 9 and 4 + 5 == 9), g="mehrschritt")
neu(f, "sachzusammenhang", "LW", L("Ein Handytarif kostet 5 € Grundgebühr und 2 € je Gigabyte (GB). Für 4 GB zahlt man 5 + 2 · 4 = ① €. Für 10 GB zahlt man 5 + 2 · 10 = ② €.",
    K(2), [13, 25], ["5 + 2 * 4", "5 + 2 * 10"], ["5 + 8", "25"], "Erst malnehmen, dann die Grundgebühr dazu.", "5 + 8 = 13 €. 5 + 20 = 25 €.",
    {0: [(28, "fb.reihenfolge.links_nach_rechts", "(5 + 2) · 4 gerechnet")]}, hinweis=GZ))
neu(f, "sachzusammenhang", "FD", FDZ("Eine Kerze ist 30 cm lang und brennt in jeder Stunde 2 cm ab. Kim stellt den Term für die Länge L(t) nach t Stunden auf.",
    [("Feste Größe am Anfang: 30 cm.", True), ("Änderung pro Stunde: −2 cm.", True), ("Term: L(t) = 2 − 30 · t.", False)],
    "Die feste Größe steht allein, die Änderung steht beim t.", "Die Länge am Anfang ist 30, pro Stunde kommt −2 dazu: L(t) = 30 − 2 · t."))

# ═════════════════════ Kind 1 · Flug ge3 · Winkel ═════════════════════
f = "ge3"
neu(f, "ergaenzen", "FD", FDZ("Neben einem Winkel von 65° liegt an einer Geraden ein zweiter Winkel. Kim berechnet ihn.",
    [("Beide zusammen ergeben einen gestreckten Winkel.", True), ("Ein gestreckter Winkel hat 90°.", 90 == 180), ("Der zweite Winkel hat 90° − 65° = 25°.", True)],
    "Wie viel Grad hat eine gerade Linie als Winkel?", "Ein gestreckter Winkel hat 180°. Der zweite Winkel hat 180° − 65° = 115°."))
neu(f, "kreuzung", "FD", FDZ("Zwei Geraden schneiden sich. Ein Winkel hat 50°. Kim berechnet die anderen.",
    [("Der gegenüberliegende Winkel hat auch 50°.", True), ("Die beiden Nachbarwinkel haben je 180° − 50° = 130°.", 180 - 50 == 130), ("Alle vier Winkel zusammen: 50° + 50° + 130° + 130° = 350°.", 50 + 50 + 130 + 130 == 350)],
    "Rechne die vier Winkel noch einmal zusammen.", "50 + 50 + 130 + 130 = 360. Um einen Punkt herum sind es immer 360°."))
neu(f, "um_punkt", "LW", L("Um einen Punkt liegen drei Winkel: 100°, 140° und ein dritter. Alle zusammen ergeben ①°. Die ersten beiden zusammen haben 100° + 140° = ②°. Der dritte Winkel hat ① − ② = ③°.",
    K(3), [360, 240, 120], ["360", "100 + 140", "360 - (100 + 140)"], ["2 * 180", "140 + 100", "360 // 3"], "Um einen Punkt herum ist ein voller Winkel.", "360° − 240° = 120°.",
    {0: [(180, None, "mit dem gestreckten Winkel verwechselt")]}, hinweis=GZ))
neu(f, "um_punkt", "FD", FDZ("Um einen Punkt liegen vier gleich große Winkel. Kim berechnet einen von ihnen.",
    [("Alle Winkel um einen Punkt ergeben 360°.", True), ("Jeder der vier Winkel hat 360° : 4 = 80°.", 360 // 4 == 80), ("Ein Winkel hat also 80°.", True)],
    "Rechne 4 · 80° als Probe.", "360° : 4 = 90°. Probe: 4 · 90° = 360°."))
neu(f, "uhr", "LW", L("Der Minutenzeiger dreht sich in 60 Minuten um 360°. In 1 Minute dreht er sich um 360° : 60 = ①°. In 15 Minuten dreht er sich um 15 · ① = ②°.",
    K(2), [6, 90], ["360 // 60", "15 * (360 // 60)"], ["30 // 5", "360 // 4"], "Eine Viertelstunde ist ein Viertel einer ganzen Drehung.", "360° : 60 = 6°. 15 · 6° = 90°.",
    {0: [(60, None, "durch 6 statt durch 60 geteilt")]}, hinweis=GZ))
neu(f, "uhr", "VW", W("Der Stundenzeiger läuft 2 Stunden. Um wie viel Grad dreht er sich? Welche Rechnung stimmt?",
    "In 12 Stunden dreht er sich um 360°, also in 1 Stunde um 30°. Zwei Stunden: 2 · 30° = 60°",
    [("In 1 Minute dreht er sich um 6°. Zwei Stunden: 2 · 6° = 12°", "den Minutenzeiger genommen"), ("In 1 Stunde dreht er sich um 360°. Zwei Stunden: 2 · 360° = 720°", "mit der Drehung des Minutenzeigers gerechnet"), ("Zwei Stunden sind die Hälfte: 360° : 2 = 180°", "Stunden und Teile einer Drehung verwechselt")],
    "Wie lange braucht der Stundenzeiger für eine ganze Drehung?", "Eine ganze Drehung dauert 12 Stunden. 360° : 12 = 30° je Stunde. 2 · 30° = 60°.",
    lambda: 360 // 12 == 30 and 2 * 30 == 60 and 2 * 6 != 60 and 2 * 360 != 60 and 360 // 2 != 60), g="mehrschritt")
neu(f, "drehungen", "LW", L("Du drehst dich im Uhrzeigersinn um 270°. Eine Vierteldrehung sind ①°. 270° sind also ② Vierteldrehungen. Eine ganze Drehung sind ③ Vierteldrehungen.",
    K(3), [90, 3, 4], ["360 // 4", "270 // 90", "4"], ["90", "3 * 90 // 90", "360 // 90"], "Eine ganze Drehung hat 360°.", "360° : 4 = 90°. 270° : 90° = 3. Vier Vierteldrehungen sind eine ganze Drehung.",
    {1: [(2, None, "halbe Drehungen gezählt")]}, hinweis=GZ))
neu(f, "drehungen", "FD", FDZ("Du schaust nach Osten und drehst dich um 90° im Uhrzeigersinn. Kim sagt, wohin du dann schaust.",
    [("90° sind eine Vierteldrehung.", True), ("Im Uhrzeigersinn geht es von Osten nach Süden.", True), ("Du schaust danach nach Norden.", False)],
    "Zwischen zwei Himmelsrichtungen, die direkt nebeneinander liegen, sind 90°. Welche kommt nach Osten?", "Von Osten aus ist im Uhrzeigersinn Süden die nächste Himmelsrichtung. Du schaust nach Süden."))
neu(f, "figuren", "LW", L("Die Diagonale eines Rechtecks teilt eine Ecke in zwei Teile. Ein Teil hat 32°. Jede Ecke des Rechtecks hat ①°. Der andere Teil hat ① − 32 = ②°.",
    K(2), [90, 58], ["90", "90 - 32"], ["180 // 2", "32 + 58 - 32"], "Jede Ecke eines Rechtecks ist ein rechter Winkel.", "90° − 32° = 58°.",
    {1: [(148, None, "von 180° statt von 90° abgezogen")]}, hinweis=GZ))
neu(f, "figuren", "FD", FDZ("In einem Quadrat teilen zwei Linien aus einer Ecke den rechten Winkel in drei gleich große Teile. Kim berechnet zwei der Teile zusammen.",
    [("Ein Quadrat hat in jeder Ecke 90°.", True), ("Jeder der drei Teile hat 90° : 3 = 30°.", 90 // 3 == 30), ("Zwei der Teile zusammen haben 30° + 30° = 90°.", 30 + 30 == 90)],
    "Rechne 30 + 30 noch einmal nach.", "30° + 30° = 60°. Alle drei Teile zusammen sind 90°."))
neu(f, "figuren", "VW", W("Eine Ecke eines Rechtecks wird durch zwei Linien in drei Teile geteilt. Zwei Teile haben 25° und 30°. Wie berechnest du den dritten Teil?",
    "90° − 25° − 30° = 35°",
    [("180° − 25° − 30° = 125°", "von 180° statt von 90° abgezogen"), ("25° + 30° = 55°", "die beiden Teile zusammengezählt"), ("90° − 25° = 65°", "nur einen Teil abgezogen")],
    "Die drei Teile ergeben zusammen eine Ecke des Rechtecks.", "Ecke 90°. 90° − 25° = 65°. 65° − 30° = 35°.",
    lambda: 90 - 25 - 30 == 35 and 180 - 25 - 30 != 35 and 25 + 30 != 35 and 90 - 25 != 35), g="mehrschritt")
neu(f, "verstehen", "LW", L("Kim sagt: „Zwei Winkel, die zusammen 180° ergeben, sind immer gleich groß.“ Gegenbeispiel: Ein Winkel hat 70°. Der andere hat 180° − 70° = ①°. ① ist nicht 70. Also ist die Behauptung falsch.",
    K(1), [110], ["180 - 70"], ["100 + 10"], "Ein einziges Beispiel genügt, um „immer“ zu widerlegen.", "180° − 70° = 110°. 110° ist nicht gleich 70°.",
    {0: [(70, None, "den bekannten Winkel wiederholt")]}, hinweis=GZ))

# ═════════════════════ Kind 1 · Flug r1 · Umfang und Fläche ═════════════════════
f = "r1"
neu(f, "einheitsquadrate", "FD", FDZ("Ein Rechteck wird mit Quadraten von 1 cm² ausgelegt. Es passen 5 Reihen mit je 7 Quadraten. Kim bestimmt die Fläche.",
    [("Die Zahl der Quadrate ist 5 · 7.", True), ("5 · 7 = 35.", 5 * 7 == 35), ("Die Fläche ist 35 cm.", False)],
    "Eine Fläche misst man in Quadraten. Wie schreibt man die Einheit?", "Die Fläche ist 35 cm². Die Einheit der Fläche hat die kleine Zwei."))
neu(f, "rechteck", "LW", L("Ein Rechteck ist 9 m lang und 4 m breit. Die Fläche ist 9 · 4 = ① m². Der Umfang ist 2 · 9 + 2 · 4 = ② m.",
    K(2), [36, 26], ["9 * 4", "2 * 9 + 2 * 4"], ["4 * 9", "(9 + 4) * 2"], "Fläche: Länge mal Breite. Umfang: alle Seiten zusammen.", "9 · 4 = 36 m². 18 + 8 = 26 m.",
    {1: [(36, "fb.auslegen.umfang_statt_flaeche", "die Fläche statt des Umfangs genannt")]}, hinweis=GZ))
neu(f, "rechteck", "FD", FDZ("Ein Rechteck hat die Fläche 60 cm² und ist 12 cm lang. Kim berechnet die Breite.",
    [("Es gilt A = a · b, also 60 = 12 · b.", True), ("Dann ist b = 12 · 60 = 720.", 12 * 60 == 60 // 12), ("Die Breite ist 720 cm.", True)],
    "Aus A = a · b folgt b = A : a. Wann musst du teilen?", "Die Breite ist die Fläche geteilt durch die Länge: b = 60 : 12 = 5 cm."))
neu(f, "rechteck", "VW", W("Ein Garten ist 12 m lang und 8 m breit. Du willst wissen, wie viel Zaun du um den ganzen Garten brauchst. Welche Rechnung passt?",
    "2 · 12 + 2 · 8 = 40 m (Umfang)", [("12 · 8 = 96 m (Fläche)", "Fläche statt Umfang"), ("12 + 8 = 20 m", "nur zwei Seiten gezählt"), ("12 + 8 + 12 = 32 m", "eine Seite vergessen")],
    "Der Zaun läuft einmal um den ganzen Garten herum.", "Der Zaun geht um alle vier Seiten: 12 + 8 + 12 + 8 = 40 m.",
    lambda: 2 * 12 + 2 * 8 == 40 and 12 * 8 != 40 and 12 + 8 != 40 and 12 + 8 + 12 != 40), g="einkleidung")
neu(f, "einheiten", "FD", FDZ("Kim rechnet 4 m² in dm² um.",
    [("Bei Flächen ist die Umrechnungszahl 100.", True), ("1 m² = 100 dm².", 10 * 10 == 100), ("4 m² = 4 · 10 = 40 dm².", 4 * 10 == 4 * 100)],
    "Welche Zahl hast du in Zeile 1 und 2 für die Umrechnung genannt?", "Die Umrechnungszahl ist 100: 4 · 100 = 400 dm²."))
neu(f, "kommaschreibweise", "LW", L("Bei Flächen bekommt jede kleinere Einheit hinter dem Komma zwei Stellen. 3,25 m² sind 3 m² 25 dm². Das sind insgesamt ① dm². 2,05 m² sind 2 m² ② dm².",
    K(2), [325, 5], ["3 * 100 + 25", "205 - 200"], ["300 + 25", "5"], "1 m² sind 100 dm².", "3 m² = 300 dm², dazu 25 dm²: 325 dm². 2,05 m² = 2 m² 05 dm² = 2 m² 5 dm².",
    {1: [(50, "fb.stellenwert.eine_stelle_daneben", "05 als 50 gelesen")]}, hinweis=GZ))
neu(f, "zerlegen", "LW", L("Eine L-förmige Fläche wird in zwei Rechtecke zerlegt: eines ist 6 m mal 3 m, das andere 2 m mal 4 m. Die Flächen sind 6 · 3 = ① m² und 2 · 4 = ② m². Zusammen sind es ③ m².",
    K(3), [18, 8, 26], ["6 * 3", "2 * 4", "6 * 3 + 2 * 4"], ["3 * 6", "4 * 2", "18 + 8"], "Rechne beide Rechtecke einzeln und addiere.", "18 m² + 8 m² = 26 m².",
    {2: [(24, None, "die beiden Flächen nicht richtig addiert")]}, hinweis=GZ))
neu(f, "sachaufgaben", "LW", L("Ein Zimmer ist 5 m lang und 4 m breit. Der Boden wird mit Fliesen belegt. Das ist eine Fläche: 5 · 4 = ① m². Für die Leiste an der Wand brauchst du den Umfang: 2 · 5 + 2 · 4 = ② m.",
    K(2), [20, 18], ["5 * 4", "2 * 5 + 2 * 4"], ["4 * 5", "5 + 4 + 5 + 4"], "Boden: Fläche. Wand: Umfang.", "5 · 4 = 20 m². 10 + 8 = 18 m.",
    {1: [(20, "fb.auslegen.umfang_statt_flaeche", "die Fläche statt des Umfangs genannt")]}, hinweis=GZ))
neu(f, "sachaufgaben", "FD", FDZ("Ein Beet ist 3 m lang und 2 m breit. Kim will einen Zaun um das ganze Beet kaufen.",
    [("Der Zaun läuft am Rand, also brauche ich den Umfang.", True), ("Umfang: 3 · 2 = 6.", 3 * 2 == 2 * 3 + 2 * 2), ("Ich brauche 6 m Zaun.", True)],
    "Der Umfang ist die Summe aller vier Seiten.", "Umfang: 3 + 2 + 3 + 2 = 10 m. 3 · 2 = 6 wäre die Fläche in m²."))
neu(f, "verstehen", "LW", L("Ein Rechteck ist 5 cm lang und 2 cm breit. Seine Fläche ist ① cm². Verdoppelt man Länge und Breite, ist die neue Fläche (2 · 5) · (2 · 2) = ② cm². Die neue Fläche ist ③-mal so groß wie die alte.",
    K(3), [10, 40, 4], ["5 * 2", "(2 * 5) * (2 * 2)", "40 // 10"], ["2 * 5", "10 * 4", "2 * 2"], "Verdopple beide Seiten, nicht nur eine.", "Alt: 10 cm². Neu: 10 · 4 = 40 cm². 40 : 10 = 4.",
    {2: [(2, None, "nur mit 2 gerechnet")]}, hinweis=GZ))

# ═════════════════════ Kind 1 · Flug g2 · Dreisatz (Teil 1) ═════════════════════
f = "g2"
neu(f, "einheit", "FD", FDZ("6 Brötchen kosten 3,60 €. Kim berechnet den Preis für 1 Brötchen in Cent.",
    [("Preis durch Anzahl: 360 ct : 6.", True), ("360 ct : 6 = 6 ct.", 360 // 6 == 6), ("Ein Brötchen kostet also 6 ct.", True)],
    "Rechne 6 mal den Preis für ein Brötchen. Kommt 360 ct heraus?", "360 : 6 = 60. Ein Brötchen kostet 60 ct. Probe: 6 · 60 ct = 360 ct."))
neu(f, "geschickt", "LW", L("Jedes Heft kostet gleich viel. 4 Hefte kosten 6 €. Von 4 Heften zu 12 Heften: 12 : 4 = ①. Der Preis wird auch ①-mal so groß: 6 € · ① = ② €.",
    K(2), [3, 18], ["12 // 4", "6 * (12 // 4)"], ["4 - 1", "6 * 3"], "Wie oft passen 4 Hefte in 12 Hefte?", "12 : 4 = 3. 6 € · 3 = 18 €.",
    {1: [(9, None, "3 € dazugezählt statt malgenommen")]}, hinweis=GZ))
neu(f, "sach", "LW", L("Ein Auto verbraucht auf jedem Kilometer gleich viel. Auf 100 km braucht es 6 l Benzin. Für 300 km braucht es 300 : 100 = ① mal so viel. Das sind 6 l · ① = ② l.",
    K(2), [3, 18], ["300 // 100", "6 * (300 // 100)"], ["1 + 1 + 1", "6 + 6 + 6"], "300 km sind mehrere Stücke von je 100 km.", "300 : 100 = 3. 3 · 6 l = 18 l.",
    {1: [(306, None, "6 l und 300 km vermischt")]}, hinweis=GZ))
neu(f, "aenderung", "LW", L("Ein Becken wird leer gepumpt. Nach 2 Minuten sind es noch 90 l Wasser, nach 5 Minuten noch 60 l. Änderung des Wassers: 60 − 90 = ① l. Zeitspanne: 5 − 2 = ② min. Rate: ① : ② = ③ l je Minute.",
    K(3), [-30, 3, -10], ["60 - 90", "5 - 2", "(60 - 90) // (5 - 2)"], ["-(90 - 60)", "1 + 2", "-30 // 3"], "Das Wasser wird weniger. Die Rate hat ein Minus.", "−30 l in 3 min: −30 : 3 = −10 l je Minute.",
    {0: [(30, "fb.plusminus.zeichen_des_ergebnisses", "das Minus vergessen")]}, hinweis=GZ))
neu(f, "aenderung", "VW", W("Eine Pflanze war nach 2 Wochen 14 cm hoch und nach 6 Wochen 30 cm. Wie berechnest du, wie viel sie pro Woche wächst?",
    "(30 − 14) : (6 − 2) = 4 cm pro Woche",
    [("30 : 6 = 5 cm pro Woche", "die Anfangshöhe ignoriert"), ("30 − 14 = 16 cm pro Woche", "nicht durch die Zeitspanne geteilt"), ("(30 + 14) : (6 + 2) = 5,5 cm pro Woche", "die Werte addiert statt der Änderungen")],
    "Änderungsrate = Änderung : Zeitspanne.", "Die Höhe ändert sich um 16 cm in 4 Wochen: 16 : 4 = 4 cm je Woche.",
    lambda: (30 - 14) / (6 - 2) == 4 and 30 / 6 != 4 and 30 - 14 != 4 and (30 + 14) / (6 + 2) != 4), g="mehrschritt")

# ═════════════════════ Kind 2 · Flug ge4 · Dreiecke, Vierecke und Konstruktion ═════════════════════
f = "ge4"
neu(f, "scheitel_neben", "FD", FDZ("Zwei Geraden schneiden sich. Ein Winkel α hat 52°. Kim berechnet die anderen drei Winkel.",
    [("Der Scheitelwinkel von α ist genauso groß: 52°.", True), ("Ein Nebenwinkel von α hat 180° − 52° = 128°.", 180 - 52 == 128), ("Der andere Nebenwinkel von α hat 52°.", False)],
    "Die vier Winkel bilden zwei Paare gleich großer Winkel. Welche Paare sind es?", "Der andere Nebenwinkel ist der Scheitelwinkel des ersten Nebenwinkels. Er hat auch 128°."))
neu(f, "scheitel_neben", "VW", W("Zwei Geraden schneiden sich. Ein Winkel hat 65°. Welche Rechnung gibt den Nebenwinkel?",
    "180° − 65° = 115°", [("Der Nebenwinkel hat auch 65°", "mit dem Scheitelwinkel verwechselt"), ("90° − 65° = 25°", "von 90° statt von 180° abgezogen"), ("360° − 65° = 295°", "von einem vollen Winkel abgezogen")],
    "Ein Winkel und sein Nebenwinkel bilden zusammen eine gerade Linie.", "Eine gerade Linie hat 180°. 180° − 65° = 115°.",
    lambda: 180 - 65 == 115 and 65 != 115 and 90 - 65 != 115 and 360 - 65 != 115))
neu(f, "stufen_wechsel", "FD", FDZ("Die Geraden g und h sind parallel. Eine dritte Gerade schneidet beide. Bei S ist ein Winkel 110° groß. Kim sucht Winkel bei T.",
    [("Der Stufenwinkel bei T ist gleich groß: 110°.", True), ("Der Nebenwinkel dieses Stufenwinkels hat 180° − 110° = 70°.", 180 - 110 == 70), ("Der Nebenwinkel dieses Stufenwinkels hat auch 110°.", False)],
    "Stufenwinkel sind gleich. Nebenwinkel sind es nur, wenn beide 90° haben.", "Der Nebenwinkel hat 180° − 110° = 70°."))
neu(f, "stufen_wechsel", "VW", W("g ∥ h. Eine Gerade schneidet g in S und h in T. Der Winkel bei S oberhalb von g und rechts von der Geraden hat 75°. Wie groß ist sein Wechselwinkel bei T (unterhalb von h und links von der Geraden)?",
    "75°, denn Wechselwinkel an Parallelen sind gleich groß", [("105°, denn Wechselwinkel ergeben zusammen 180°", "Wechselwinkel mit Nebenwinkeln verwechselt"), ("15°, denn 90° − 75°", "von 90° abgezogen"), ("285°, denn 360° − 75°", "von einem vollen Winkel abgezogen")],
    "Wechselwinkel liegen auf verschiedenen Seiten der Geraden und an verschiedenen Parallelen.", "Wechselwinkel an Parallelen sind gleich: 75°.",
    lambda: 75 == 75 and 180 - 75 != 75 and 90 - 75 != 75 and 360 - 75 != 75))
neu(f, "parallel_pruefen", "FD", FDZ("Eine Gerade schneidet g und h. Die zugehörigen Stufenwinkel sind 80° und 100° groß. Kim prüft, ob g ∥ h gilt.",
    [("Die Stufenwinkel sind 80° und 100°.", True), ("Bei Parallelen müssten die Stufenwinkel gleich groß sein.", True), ("80° + 100° = 180°, also sind g und h parallel.", False)],
    "Welche Winkel sind bei Parallelen gleich groß, und welche ergeben zusammen 180°?", "Die Summe 180° gilt für Nebenwinkel. Stufenwinkel müssen gleich sein. 80° ist nicht 100°, also sind g und h nicht parallel."))
neu(f, "parallel_pruefen", "LW", L("g ∥ h. Eine Gerade schneidet beide. Bei S gibt es einen Winkel von 72°. Sein Stufenwinkel bei T ist genauso groß. Beide zusammen haben ①°. Der Nebenwinkel bei T hat ②°.",
    K(2), [144, 108], ["72 + 72", "180 - 72"], ["2 * 72", "108"], "Der Nebenwinkel ergänzt den Stufenwinkel zu einer geraden Linie.", "72° + 72° = 144°. 180° − 72° = 108°.",
    {0: [(72, None, "nur einen Winkel genannt")], 1: [(72, None, "Nebenwinkel mit Stufenwinkel verwechselt")]}, hinweis=GZ))
neu(f, "innenwinkelsumme", "LW", L("Im Dreieck ist α = 48° und β = 77°. Dann ist γ = 180° − 48° − 77° = ①°. Ein Viereck hat die Winkel 95°, 100° und 85° und δ = ②°.",
    K(2), [55, 80], ["180 - 48 - 77", "360 - 95 - 100 - 85"], ["180 - (48 + 77)", "360 - (95 + 100 + 85)"], "Im Dreieck sind es 180°, im Viereck 360°.", "γ = 55°. δ = 360° − 280° = 80°.",
    {0: [(125, None, "nur α abgezogen")], 1: [(100, None, "von 180° statt von 360° abgezogen")]}, hinweis=GZ))
neu(f, "innenwinkelsumme", "FD", FDZ("Im Dreieck ist α = 40° und β = 75°. Kim berechnet γ.",
    [("Die Winkelsumme im Dreieck beträgt 180°.", True), ("α + β = 40° + 75° = 115°.", 40 + 75 == 115), ("γ = 180° − 115° = 75°.", 180 - 115 == 75)],
    "Rechne 180 − 115 noch einmal.", "180° − 115° = 65°. γ = 65°."))
neu(f, "innenwinkelsumme", "VW", W("Ein Dreieck hat α = 35° und β = 70°. Welche Rechnung gibt γ?",
    "180° − 35° − 70° = 75°", [("360° − 35° − 70° = 255°", "die Winkelsumme des Vierecks benutzt"), ("35° + 70° = 105°", "nur die beiden Winkel addiert"), ("180° − 70° = 110°", "nur einen Winkel abgezogen")],
    "Alle drei Winkel eines Dreiecks ergeben zusammen eine feste Summe.", "180° − 35° = 145°. 145° − 70° = 75°.",
    lambda: 180 - 35 - 70 == 75 and 360 - 35 - 70 != 75 and 35 + 70 != 75 and 180 - 70 != 75))
neu(f, "aussenwinkel", "VW", W("Ein Dreieck hat α = 62° und β = 48°. Wie groß ist der Außenwinkel bei C?",
    "62° + 48° = 110°", [("180° − 62° − 48° = 70°", "den Innenwinkel γ berechnet"), ("180° − 62° = 118°", "nur α abgezogen"), ("360° − 62° − 48° = 250°", "von 360° abgezogen")],
    "Der Außenwinkel und γ ergeben zusammen eine gerade Linie.", "γ = 70°. Außenwinkel = 180° − 70° = 110°. Das ist auch α + β.",
    lambda: 62 + 48 == 110 == 180 - (180 - 62 - 48) and 180 - 62 - 48 != 110 and 180 - 62 != 110 and 360 - 62 - 48 != 110))
neu(f, "vieleck", "LW", L("Ein Fünfeck zerlegt man von einer Ecke aus in 3 Dreiecke. Die Winkelsumme ist 3 · 180° = ①°. Ein Sechseck hat die Winkelsumme (6 − 2) · 180° = ②°.",
    K(2), [540, 720], ["3 * 180", "(6 - 2) * 180"], ["540", "4 * 180"], "Ein n-Eck zerlegt man in n − 2 Dreiecke.", "3 · 180° = 540°. 4 · 180° = 720°.",
    {0: [(900, None, "5 Dreiecke gezählt")], 1: [(1080, None, "6 Dreiecke statt 4 gerechnet")]}, hinweis=GZ))
neu(f, "vieleck", "FD", FDZ("Kim berechnet die Winkelsumme eines Achtecks.",
    [("Von einer Ecke aus zerlegt man ein n-Eck in n − 2 Dreiecke.", True), ("Beim Achteck sind das 8 − 2 = 6 Dreiecke.", 8 - 2 == 6), ("Die Winkelsumme ist 6 · 180° = 960°.", 6 * 180 == 960)],
    "Rechne 6 · 180 noch einmal.", "6 · 180° = 1080°."))
neu(f, "vieleck", "VW", W("Wie groß ist jeder Innenwinkel eines regelmäßigen Sechsecks?",
    "(6 − 2) · 180° : 6 = 120°", [("180° : 6 = 30°", "die Winkelsumme des Dreiecks genommen"), ("360° : 6 = 60°", "den Außenwinkel berechnet"), ("(6 − 2) · 180° = 720°", "nicht durch die Eckenzahl geteilt")],
    "Rechne erst die Winkelsumme aus, dann teile durch die Zahl der Ecken.", "Winkelsumme: 4 · 180° = 720°. 720° : 6 = 120°.",
    lambda: (6 - 2) * 180 // 6 == 120 and 180 // 6 != 120 and 360 // 6 != 120 and (6 - 2) * 180 != 120))
neu(f, "parkett", "FD", FDZ("Kim prüft, ob regelmäßige Fünfecke einen Boden lückenlos bedecken können.",
    [("Die Winkelsumme im Fünfeck ist 3 · 180° = 540°.", 3 * 180 == 540), ("Jeder Innenwinkel hat 540° : 5 = 108°.", 540 // 5 == 108), ("An einem Punkt treffen sich 360° : 108° = 3 Fünfecke. Das geht ohne Lücke auf.", 360 % 108 == 0)],
    "Geht 360 durch 108 ohne Rest?", "360° : 108° ist ungefähr 3,3. Es bleibt eine Lücke. Regelmäßige Fünfecke bedecken den Boden nicht lückenlos."))
neu(f, "parkett", "VW", W("Ein Boden wird mit regelmäßigen Sechsecken ausgelegt. Wie viele Sechsecke stoßen an einer Ecke zusammen?",
    "3, denn 3 · 120° = 360°", [("4, denn 4 · 90° = 360°", "das gilt für Quadrate"), ("2, denn 2 · 180° = 360°", "mit dem gestreckten Winkel gerechnet"), ("6, denn ein Sechseck hat 6 Ecken", "mit der Eckenzahl verwechselt")],
    "Alle Winkel an einem Punkt ergeben 360°. Wie groß ist ein Innenwinkel des Sechsecks?", "Ein Innenwinkel hat 120°. 360° : 120° = 3.",
    lambda: 3 * 120 == 360 and 4 * 120 != 360 and 2 * 120 != 360 and 6 * 120 != 360))
neu(f, "figuren", "LW", L("Im gleichschenkligen Dreieck hat der Winkel an der Spitze 40°. Ein Basiswinkel hat (180° − 40°) : 2 = ①°. Der Nebenwinkel eines Basiswinkels hat 180° − ①° = ②°.",
    K(2), [70, 110], ["(180 - 40) // 2", "180 - (180 - 40) // 2"], ["70", "110"], "Beide Basiswinkel sind gleich groß.", "140° : 2 = 70°. 180° − 70° = 110°.",
    {0: [(140, None, "nicht durch 2 geteilt")], 1: [(70, None, "Basiswinkel und Nebenwinkel verwechselt")]}, hinweis=GZ))
neu(f, "figuren", "FD", FDZ("Im Parallelogramm ABCD ist α = 70°. Kim berechnet die anderen Winkel.",
    [("Gegenüberliegende Winkel sind gleich groß: γ = 70°.", True), ("Nachbarwinkel ergeben 180°: β = 180° − 70° = 110°.", 180 - 70 == 110), ("δ = 360° − 70° − 70° − 110° = 100°.", 360 - 70 - 70 - 110 == 100)],
    "δ liegt gegenüber von β.", "δ = 360° − 250° = 110°. Es ist gleich β, denn die Winkel gegenüber sind gleich."))
neu(f, "figuren", "VW", W("Ein gestreckter Winkel wird durch eine Linie in zwei Teile geteilt. Ein Teil ist fünfmal so groß wie der andere. Welche Rechnung gibt den kleineren Teil?",
    "180° : (1 + 5) = 30°", [("180° : 5 = 36°", "nur durch 5 geteilt"), ("180° : 2 = 90°", "in zwei gleiche Teile geteilt"), ("180° − 5° = 175°", "5° statt das Fünffache abgezogen")],
    "Zähle die Teile: Der kleine Teil ist ein Teil, der große sind fünf Teile.", "Es sind 1 + 5 = 6 gleiche Teile. 180° : 6 = 30°. Der große Teil hat 150°.",
    lambda: 180 // (1 + 5) * 5 + 180 // 6 == 180 and 180 // 5 != 30 and 180 // 2 != 30 and 180 - 5 != 30))
neu(f, "beweisen", "FD", FDZ("Kim beweist: „Ein Außenwinkel eines Dreiecks ist so groß wie die beiden nicht anliegenden Innenwinkel zusammen.“ Es geht um den Außenwinkel bei C.",
    [("Außenwinkel bei C und γ sind Nebenwinkel: Außenwinkel + γ = 180°.", True), ("Die Winkelsumme im Dreieck ist α + β + γ = 180°.", True), ("Aus beiden Gleichungen folgt: Außenwinkel = α + γ.", False)],
    "Vergleiche beide Gleichungen: Was steht auf beiden Seiten gleich da?", "In beiden Gleichungen kommt γ vor. Zieht man γ ab, folgt: Außenwinkel = α + β."))
neu(f, "beweisen", "VW", W("Du willst beweisen, dass die Winkel in jedem Dreieck zusammen 180° ergeben. Womit beginnst du?",
    "Mit der Parallelen zu AB durch C, damit du Wechselwinkel nutzen kannst", [("Mit dem Messen der Winkel in einem gezeichneten Dreieck", "ein Beispiel beweist nicht für alle Dreiecke"), ("Mit der Annahme, dass alle drei Winkel gleich sind", "nur für das gleichseitige Dreieck"), ("Mit einem Dreieck mit den Winkeln 60°, 60° und 60°", "ein einzelnes Beispiel")],
    "Ein Beweis muss für jedes Dreieck gelten, nicht nur für ein gezeichnetes.", "Die Parallele zu AB durch C liefert zwei Wechselwinkel. Mit γ bilden sie eine gerade Linie von 180°.",
    lambda: 60 + 60 + 60 == 180), g="begruenden")
neu(f, "gleichschenklig", "LW", L("Ein gleichschenkliges Dreieck hat an der Spitze 50°. Ein Basiswinkel hat (180° − 50°) : 2 = ①°. Ein anderes hat die Basiswinkel 35°. Dann hat die Spitze 180° − 2 · 35° = ②°.",
    K(2), [65, 110], ["(180 - 50) // 2", "180 - 2 * 35"], ["130 / 2", "180 - 70"], "Es gibt zwei gleich große Basiswinkel.", "130° : 2 = 65°. 180° − 70° = 110°.",
    {0: [(130, None, "nicht durch 2 geteilt")], 1: [(145, None, "nur einen Basiswinkel abgezogen")]}, hinweis=GZ))
neu(f, "gleichschenklig", "FD", FDZ("Ein gleichschenkliges Dreieck hat die Basiswinkel 55°. Kim berechnet den Winkel an der Spitze.",
    [("Die beiden Basiswinkel sind gleich groß.", True), ("Beide zusammen: 55° + 55° = 110°.", 55 + 55 == 110), ("Die Spitze: 180° − 110° = 80°.", 180 - 110 == 80)],
    "Rechne 180 − 110 noch einmal.", "180° − 110° = 70°. Der Winkel an der Spitze hat 70°."))
neu(f, "gleichschenklig", "VW", W("Ein gleichschenkliges Dreieck hat an der Spitze 30°. Welche Rechnung gibt einen Basiswinkel?",
    "(180° − 30°) : 2 = 75°", [("180° − 30° = 150°", "nicht durch 2 geteilt"), ("180° : 2 − 30° = 60°", "erst geteilt, dann abgezogen"), ("(180° − 30°) · 2 = 300°", "mit 2 multipliziert")],
    "Die beiden Basiswinkel zusammen sind die Winkelsumme ohne die Spitze.", "Die Basiswinkel haben zusammen 150°. Jeder hat 75°.",
    lambda: (180 - 30) // 2 == 75 and 180 - 30 != 75 and 180 // 2 - 30 != 75 and (180 - 30) * 2 != 75))
neu(f, "kongruenzsatz", "FD", FDZ("Dreieck 1 hat die Seiten a = 4 cm, b = 5 cm und den Winkel γ = 40° zwischen ihnen. Dreieck 2 hat auch a = 4 cm, b = 5 cm und 40°, aber dieser Winkel liegt der Seite a gegenüber. Kim prüft, ob sie kongruent sind.",
    [("Beide Dreiecke stimmen in zwei Seiten und einem Winkel überein.", True), ("Bei Dreieck 1 liegt der Winkel zwischen den Seiten, bei Dreieck 2 nicht.", True), ("Also gilt SWS, und die Dreiecke sind kongruent.", False)],
    "Bei SWS muss der Winkel zwischen den beiden gegebenen Seiten liegen.", "Bei Dreieck 2 liegt der Winkel nicht zwischen den Seiten. SWS gilt nicht, und man kann nicht auf Kongruenz schließen."))
neu(f, "kongruenzsatz", "VW", W("Zwei Dreiecke stimmen in einer Seite von 6 cm und in den beiden Winkeln an dieser Seite überein. Welcher Satz zeigt, dass sie kongruent sind?",
    "WSW", [("SWS", "der Winkel liegt nicht zwischen zwei Seiten"), ("SSS", "nur eine Seite ist gegeben"), ("WWW", "Dieser Satz gilt nicht, gleiche Winkel geben nur ähnliche Dreiecke")],
    "Zähle, wie viele Seiten und wie viele Winkel gegeben sind.", "Eine Seite und die beiden Winkel an ihr: Winkel, Seite, Winkel (WSW).",
    lambda: True), g="erkennen")
neu(f, "konstruierbar", "LW", L("Zwei Seiten eines Dreiecks sind 6 cm und 10 cm lang. Die dritte Seite muss kürzer sein als 6 + 10 = ① cm. Sie muss länger sein als 10 − 6 = ② cm.",
    K(2), [16, 4], ["6 + 10", "10 - 6"], ["10 + 6", "4"], "Zwei Seiten zusammen müssen länger sein als die dritte.", "6 + 10 = 16. 10 − 6 = 4.",
    {1: [(6, None, "die kürzere Seite genommen")]}, hinweis=GZ))
neu(f, "konstruierbar", "FD", FDZ("Kim prüft, ob es ein Dreieck mit den Seiten 3 cm, 4 cm und 8 cm gibt.",
    [("Die Summe zweier Seiten muss größer sein als die dritte Seite.", True), ("3 + 4 = 7, und 7 ist kleiner als 8.", 3 + 4 < 8), ("Das Dreieck lässt sich konstruieren, weil 8 die längste Seite ist.", False)],
    "Prüfe, ob die beiden kürzeren Seiten zusammen die längste überbrücken.", "Die beiden kurzen Seiten sind zusammen nur 7 cm lang. Sie erreichen sich nicht. Das Dreieck gibt es nicht."))
neu(f, "konstruierbar", "VW", W("Aus welchen drei Längen lässt sich ein Dreieck konstruieren?",
    "5 cm, 6 cm, 10 cm", [("2 cm, 3 cm, 6 cm", "2 + 3 ist kleiner als 6"), ("4 cm, 4 cm, 8 cm", "4 + 4 ist nur gleich 8, die Seiten liegen flach aufeinander"), ("1 cm, 5 cm, 7 cm", "1 + 5 ist kleiner als 7")],
    "Prüfe bei jeder Auswahl, ob die zwei kürzeren Seiten zusammen länger sind als die längste.", "5 + 6 = 11 ist größer als 10. Bei den anderen reicht die Summe der zwei kürzeren Seiten nicht.",
    lambda: 5 + 6 > 10 and 2 + 3 <= 6 and 4 + 4 <= 8 and 1 + 5 <= 7), g="erkennen")
neu(f, "planfigur", "FD", FDZ("Kim konstruiert ein Dreieck aus c = 6 cm, α = 50° und b = 4 cm. Er beschreibt seine Schritte.",
    [("Zeichne zuerst die Strecke AB = 6 cm.", True), ("Trage bei A den Winkel 50° an.", True), ("Markiere C auf dem freien Schenkel im Abstand 4 cm von B.", False)],
    "Welche Ecke liegt am Anfang der Seite b?", "Die Seite b liegt zwischen A und C. C hat also den Abstand 4 cm von A."))
neu(f, "planfigur", "VW", W("Du konstruierst ein Dreieck mit c = 7 cm, b = 6 cm und a = 5 cm. Du zeichnest AB = 7 cm. Wie findest du C?",
    "Kreisbogen um A mit 6 cm und um B mit 5 cm; sie schneiden sich in C", [("Kreisbogen um A und um B mit je 5 cm", "b wäre dann auch 5 cm"), ("Kreisbogen um A und um B mit je 6 cm", "a wäre dann auch 6 cm"), ("Kreisbogen um A mit 7 cm und um B mit 5 cm", "AC wäre dann 7 cm statt 6 cm")],
    "Die Seite b liegt an der Ecke A, die Seite a an der Ecke B.", "AC = b = 6 cm, also ein Kreisbogen um A mit 6 cm. BC = a = 5 cm, also ein Kreisbogen um B mit 5 cm.",
    lambda: sorted((7, 6, 5)) == [5, 6, 7] and sorted((7, 5, 5)) != [5, 6, 7] and sorted((7, 6, 6)) != [5, 6, 7] and sorted((7, 7, 5)) != [5, 6, 7])
    , g="darstellung")
neu(f, "vierecke", "LW", L("Im Parallelogramm ABCD ist α = 65°. Alle vier Winkel zusammen haben ①°. Der Nachbarwinkel β hat ②°.",
    K(2), [360, 115], ["360", "180 - 65"], ["2 * 180", "115"], "Nachbarwinkel im Parallelogramm ergeben zusammen eine gerade Linie.", "Die Winkelsumme im Viereck ist 360°. β = 180° − 65° = 115°.",
    {0: [(180, None, "mit der Winkelsumme im Dreieck verwechselt")], 1: [(65, None, "mit dem gegenüberliegenden Winkel verwechselt")]}, hinweis=GZ))
neu(f, "vierecke", "FD", FDZ("Eine Raute hat einen Winkel von 40°. Kim berechnet den Nachbarwinkel.",
    [("Eine Raute ist ein Parallelogramm.", True), ("Nachbarwinkel im Parallelogramm ergeben zusammen 180°.", True), ("Der Nachbarwinkel hat 180° − 40° = 120°.", 180 - 40 == 120)],
    "Rechne 180 − 40 noch einmal.", "180° − 40° = 140°. Der Nachbarwinkel hat 140°."))
neu(f, "vierecke", "VW", W("Ein Viereck hat die Winkel 85°, 95° und 100°. Welche Rechnung gibt den vierten Winkel?",
    "360° − 85° − 95° − 100° = 80°", [("180° − 85° − 95° − 100° = −100°", "die Winkelsumme des Dreiecks benutzt"), ("85° + 95° + 100° = 280°", "nur addiert"), ("360° − 85° − 95° = 180°", "einen Winkel nicht abgezogen")],
    "Ein Viereck hat eine feste Winkelsumme.", "Die drei Winkel haben zusammen 280°. 360° − 280° = 80°.",
    lambda: 360 - 85 - 95 - 100 == 80 and 180 - 85 - 95 - 100 != 80 and 85 + 95 + 100 != 80 and 360 - 85 - 95 != 80))
neu(f, "satz_kehrsatz", "FD", FDZ("Satz: „Wenn ein Dreieck gleichseitig ist, dann hat es drei gleich große Winkel.“ Kim bildet den Kehrsatz.",
    [("Der Satz hat die Form: Wenn A, dann B.", True), ("Den Kehrsatz bildet man, indem man A und B vertauscht.", True), ("Er lautet: Wenn ein Dreieck gleichseitig ist, dann hat es drei gleich große Winkel.", False)],
    "Vergleiche den Kehrsatz mit dem Satz. Was hat sich geändert?", "Das ist der Satz selbst. Der Kehrsatz lautet: Wenn ein Dreieck drei gleich große Winkel hat, dann ist es gleichseitig."))
neu(f, "satz_kehrsatz", "VW", W("Satz: „Wenn eine Zahl durch 6 teilbar ist, dann ist sie durch 3 teilbar.“ Was gilt für den Kehrsatz?",
    "Der Kehrsatz ist falsch. Gegenbeispiel: 9 ist durch 3 teilbar, aber nicht durch 6", [("Der Kehrsatz ist wahr, denn der Satz ist wahr", "einen wahren Satz mit seinem Kehrsatz gleichgesetzt"), ("Der Kehrsatz ist falsch. Gegenbeispiel: 12", "12 ist durch 6 teilbar, also kein Gegenbeispiel"), ("Der Kehrsatz ist wahr, weil 3 ein Teiler von 6 ist", "der Teiler macht den Kehrsatz nicht wahr")],
    "Der Kehrsatz lautet: Wenn eine Zahl durch 3 teilbar ist, dann ist sie durch 6 teilbar. Suche eine Zahl, die nicht passt.", "9 : 3 = 3, aber 9 ist nicht durch 6 teilbar. Ein Gegenbeispiel genügt.",
    lambda: 9 % 3 == 0 and 9 % 6 != 0 and 12 % 3 == 0 and 12 % 6 == 0), g="begruenden")
neu(f, "vierecke_konstruieren", "LW", L("Du konstruierst ein Parallelogramm ABCD mit a = 6 cm, b = 4 cm und α = 70°. Der Winkel β bei B hat ①°. Alle vier Winkel zusammen haben ②°.",
    K(2), [110, 360], ["180 - 70", "360"], ["110", "2 * 180"], "Nachbarwinkel im Parallelogramm ergänzen sich zu 180°.", "β = 180° − 70° = 110°. Die vier Winkel ergeben 360°.",
    {0: [(70, None, "mit dem gegenüberliegenden Winkel verwechselt")], 1: [(180, None, "mit der Winkelsumme im Dreieck verwechselt")]}, hinweis=GZ))
neu(f, "vierecke_konstruieren", "FD", FDZ("Kim konstruiert ein Parallelogramm ABCD aus a = 6 cm, b = 4 cm und α = 70°.",
    [("Zeichne AB = 6 cm und trage bei A den Winkel 70° an.", True), ("Auf dem freien Schenkel liegt D mit AD = 4 cm.", True), ("C erhältst du mit BC = 6 cm und CD = 4 cm.", False)],
    "Gegenüberliegende Seiten im Parallelogramm sind gleich lang. Welche Seite liegt gegenüber von AB?", "BC liegt gegenüber von AD, also BC = 4 cm. CD liegt gegenüber von AB, also CD = 6 cm."))

# ═════════════════════ Kind 2 · Flug f2 · Lineare Funktionen ═════════════════════
f = "f2"
FORM = "id.funktionen.gleichung_form"
neu(f, "ablesen", "LW", L("Die Gleichung 2y = 6x + 8 wird durch 2 geteilt. Dann ist y = ①x + ②. Die Steigung ist ① und der Achsenabschnitt ist ②.",
    K(2), [3, 4], ["6 // 2", "8 // 2"], ["6 / 2", "8 / 2"], "Teile beide Zahlen rechts durch 2, nicht nur eine.", "6x : 2 = 3x und 8 : 2 = 4. Also y = 3x + 4.",
    {0: [(6, None, "nur die rechte Seite von y = nicht geteilt")], 1: [(8, None, "nur 6x geteilt")]}, hinweis=GZ))
neu(f, "ablesen", "FD", FDZ("Kim liest bei y = 4 − 3x Steigung und Achsenabschnitt ab.",
    [("Die Steigung m ist die erste Zahl: m = 4.", False), ("Der Achsenabschnitt t ist die Zahl ohne x: t = −3.", True), ("Die Gerade geht also durch den Punkt (0 | −3).", True)],
    "m steht vor dem x, nicht am Anfang der Gleichung.", "m = −3, denn −3 steht vor dem x. t = 4 ist die Zahl ohne x. Die Gerade geht durch (0 | 4)."))
neu(f, "graph_ablesen", "LW", L("Die Gerade y = 3x − 5 geht durch die Punkte (2 | ①) und (4 | ②). Zwischen den beiden Punkten steigt sie um ② − ① = ③.",
    K(3), [1, 7, 6], ["3 * 2 - 5", "3 * 4 - 5", "(3 * 4 - 5) - (3 * 2 - 5)"], ["6 - 5", "12 - 5", "3 * 2"], "Setze erst x ein, rechne dann mal, dann minus.", "y(2) = 6 − 5 = 1. y(4) = 12 − 5 = 7. 7 − 1 = 6, also 2 Schritte mal Steigung 3.",
    {2: [(2, None, "nur die Schrittweite genommen")]}, hinweis=GZ))
neu(f, "zwei_punkte", "VW", W("Eine Gerade geht durch A(2 | 1) und B(5 | 13). Welche Rechnung gibt die Steigung?",
    "(13 − 1) : (5 − 2) = 4", [("(5 − 2) : (13 − 1) = 1/4", "nach rechts durch nach oben gerechnet"), ("(13 + 1) : (5 + 2) = 2", "die Koordinaten addiert"), ("13 − 1 = 12", "nicht durch den Schritt nach rechts geteilt")],
    "Steigung = nach oben geteilt durch nach rechts.", "Nach oben: 13 − 1 = 12. Nach rechts: 5 − 2 = 3. Steigung 12 : 3 = 4.",
    lambda: (13 - 1) / (5 - 2) == 4 and (5 - 2) / (13 - 1) != 4 and (13 + 1) / (5 + 2) != 4 and 13 - 1 != 4), g="mehrschritt")
neu(f, "proportional", "LW", L("Bei einer proportionalen Zuordnung y = k · x gehört zu x = 4 der Wert y = 20. Dann ist k = 20 : 4 = ①. Zu x = 7 gehört dann y = ① · 7 = ②.",
    K(2), [5, 35], ["20 // 4", "(20 // 4) * 7"], ["5", "20 // 4 * 7"], "k ist der Wert für x = 1.", "k = 5. y = 5 · 7 = 35.",
    {1: [(27, "fb.verhaeltnis.addiert_statt_malgenommen", "den Unterschied addiert statt mit k gerechnet")]}, hinweis=GZ), regel="rr.verhaeltnis")
neu(f, "proportional", "FD", FDZ("Eine Tabelle zeigt x = 2, 4, 6 und y = 6, 12, 20. Kim prüft, ob die Zuordnung proportional ist.",
    [("Für x = 2: y : x = 6 : 2 = 3.", 6 / 2 == 3), ("Für x = 4: y : x = 12 : 4 = 3.", 12 / 4 == 3), ("Für x = 6: y : x = 20 : 6 ist ungefähr 3. Also ist die Zuordnung proportional.", 20 / 6 == 3)],
    "Für proportional muss in jeder Spalte genau dieselbe Zahl herauskommen.", "20 : 6 ist nicht 3, sondern ungefähr 3,33. Die Zuordnung ist nicht proportional."), regel="rr.verhaeltnis")
def prop(xs, ys):
    return len({F(y) / F(x) for x, y in zip(xs, ys)}) == 1 and all(x != 0 for x in xs)
neu(f, "proportional", "VW", W("Welche Wertetabelle gehört zu einer proportionalen Zuordnung?",
    "x: 1, 2, 5 und y: 3, 6, 15",
    [("x: 1, 2, 5 und y: 3, 5, 8", "gleiche Schritte nach oben statt gleicher Faktor"), ("x: 1, 2, 4 und y: 8, 4, 2", "Doppeltes x gibt halbes y"), ("x: 1, 2, 3 und y: 4, 6, 8", "y wächst gleichmäßig, aber zu x = 0 gehörte 2")],
    "Bei Proportionalität ist y : x überall gleich.", "3 : 1 = 6 : 2 = 15 : 5 = 3. In den anderen Tabellen ändert sich y : x.",
    lambda: prop([1, 2, 5], [3, 6, 15]) and not prop([1, 2, 5], [3, 5, 8]) and not prop([1, 2, 4], [8, 4, 2]) and not prop([1, 2, 3], [4, 6, 8])), g="mehrschritt", regel="rr.verhaeltnis")
neu(f, "aufstellen", "LW", L("Eine Gerade hat die Steigung 2 und geht durch P(3 | 11). Ansatz: y = 2x + t. Einsetzen: 11 = 2 · 3 + t, also t = 11 − ① = ②.",
    K(2), [6, 5], ["2 * 3", "11 - 2 * 3"], ["3 + 3", "10 - 5"], "Rechne erst 2 · 3 aus.", "2 · 3 = 6. t = 11 − 6 = 5. Die Gerade ist y = 2x + 5.",
    {1: [(17, None, "6 addiert statt abgezogen")]}, hinweis=GZ))
neu(f, "aufstellen", "FD", FDZ("Eine Gerade geht durch A(1 | 4) und B(3 | 10). Kim stellt die Gleichung auf.",
    [("Steigung: m = (10 − 4) : (3 − 1) = 3.", (10 - 4) / (3 - 1) == 3), ("A einsetzen in y = 3x + t: 4 = 3 · 1 + t, also t = 4 + 3 = 7.", 4 + 3 == 4 - 3), ("Die Gerade ist y = 3x + 7.", True)],
    "Aus 4 = 3 + t folgt t, wenn du auf beiden Seiten 3 abziehst.", "t = 4 − 3 = 1. Die Gerade ist y = 3x + 1. Probe mit B: 3 · 3 + 1 = 10."))
neu(f, "schnittpunkte", "FD", FDZ("Die Geraden y = 2x + 1 und y = −x + 7 schneiden sich. Kim bestimmt den Schnittpunkt.",
    [("Gleichsetzen: 2x + 1 = −x + 7.", True), ("x auf die linke Seite bringen: x + 1 = 7, also x = 6.", 2 - 1 == 2 + 1), ("Dann ist y = 2 · 6 + 1 = 13.", 2 * 6 + 1 == 13)],
    "Wenn du −x auf die linke Seite bringst, wird daraus +x. Wie viele x stehen dann links?", "2x + x = 3x. Also 3x + 1 = 7, x = 2 und y = 5. Der Schnittpunkt ist (2 | 5)."))
neu(f, "lage", "LW", L("Die Gerade g hat die Gleichung y = −x + 3. Eine Gerade parallel zu g hat die Steigung ①. Für eine Gerade senkrecht zu g muss das Produkt der beiden Steigungen minus eins sein. Ihre Steigung ist also ②.",
    K(2), [-1, 1], ["-1", "1"], ["-2 + 1", "(-1) * (-1)"], "Parallel heißt: dieselbe Steigung.", "Parallel: −1. Senkrecht: (−1) · m = −1, also m = 1.",
    {1: [(-1, None, "dieselbe Steigung genommen")]}, hinweis=GZ), regel=FORM)
neu(f, "lage", "FD", FDZ("Die Geraden y = 2x + 5 und y = −2x + 5 sollen untersucht werden. Kim prüft ihre Lage.",
    [("Die Steigungen sind 2 und −2.", True), ("Das Produkt der Steigungen ist 2 · (−2) = −4.", 2 * (-2) == -4), ("Das Produkt ist −4, also stehen die Geraden senkrecht aufeinander.", 2 * (-2) == -1)],
    "Senkrecht heißt: Das Produkt der Steigungen ist genau minus eins.", "Das Produkt −4 ist nicht −1, und die Steigungen sind verschieden. Die Geraden sind weder parallel noch senkrecht."), regel=FORM)
neu(f, "einsetzen", "LW", L("Die Geradenschar y = k · x + 2 enthält für k = 5 die Gerade y = 5x + 2. Für k = 5 und x = 3 ist y = ①. Für k = −4 und x = 3 ist y = ②.",
    K(2), [17, -10], ["5 * 3 + 2", "-4 * 3 + 2"], ["15 + 2", "2 - 12"], "Ersetze nur k, alles andere bleibt.", "5 · 3 + 2 = 17. (−4) · 3 + 2 = −12 + 2 = −10.",
    {1: [(-14, None, "2 abgezogen statt addiert")]}, hinweis=GZ))
neu(f, "einsetzen", "FD", FDZ("Die Schar y = (k − 2) · x + 3 hat für k = 5 eine bestimmte Gerade. Kim setzt k = 5 ein.",
    [("Die Klammer wird zu 5 + 2 = 7.", 5 + 2 == 5 - 2), ("Die Gerade ist also y = 7x + 3.", True), ("Für x = 2 ist y = 7 · 2 + 3 = 17.", 7 * 2 + 3 == 17)],
    "In der Klammer steht k − 2. Was ist 5 − 2?", "5 − 2 = 3. Die Gerade ist y = 3x + 3. Für x = 2 ist y = 9."))
neu(f, "wirkung", "LW", L("In y = a · x + b verschiebt b die Gerade nach oben oder unten. Wird b von 2 auf 8 erhöht, wandert die Gerade um 8 − 2 = ① nach oben. Wird a von 1 auf 5 erhöht, liegt die Gerade bei x = 3 um (5 − 1) · 3 = ② höher.",
    K(2), [6, 12], ["8 - 2", "(5 - 1) * 3"], ["2 * 3", "4 * 3"], "a wirkt bei jedem x. b wirkt immer gleich.", "b: 8 − 2 = 6. a: (5 − 1) · 3 = 12.",
    {1: [(4, None, "nur die Änderung von a genommen")]}, hinweis=GZ), regel=FORM)
neu(f, "wirkung", "FD", FDZ("Kim untersucht die Geraden y = a · x + 3 für verschiedene a.",
    [("a steht vor x, es ändert also die Steigung.", True), ("Bei jedem a geht die Gerade durch den Punkt (0 | 3).", 0 * 7 + 3 == 3), ("Wird a größer, verschiebt sich die Gerade nach oben, ohne dass sich die Steigung ändert.", False)],
    "Der Parameter a steht vor x. Was bewirkt das?", "Wird a größer, wird die Gerade steiler. Sie dreht sich um (0 | 3), sie verschiebt sich nicht."), regel=FORM)
neu(f, "bueschel", "LW", L("Alle Geraden y = k · (x − 3) + 7 gehen durch einen Punkt Z. Für x = 3 ist x − 3 gleich ①. Dann spielt k keine Rolle mehr. Für k = 2 und x = 5 ist y = 2 · (5 − 3) + 7 = ②.",
    K(2), [0, 11], ["3 - 3", "2 * (5 - 3) + 7"], ["0", "4 + 7"], "Welche Zahl macht die Klammer zu 0?", "3 − 3 = 0. 2 · 2 + 7 = 11.",
    {1: [(14, None, "5 − 3 mit 5 verwechselt")]}, hinweis=GZ), regel=FORM)
neu(f, "bueschel", "FD", FDZ("Alle Geraden y = k · (x + 2) + 4 gehen durch einen Punkt Z. Kim bestimmt Z.",
    [("Z liegt dort, wo k keinen Einfluss hat.", True), ("Das ist bei x + 2 = 0, also bei x = 2.", 2 + 2 == 0), ("Dort ist y = 4. Also ist Z(2 | 4).", True)],
    "Welche Zahl macht x + 2 gleich 0?", "x + 2 = 0 gilt für x = −2. Der Punkt ist Z(−2 | 4)."), regel=FORM)
neu(f, "bueschel", "VW", W("Alle Geraden y = k · x + 3 gehen durch denselben Punkt. Welcher ist es?",
    "(0 | 3), denn für x = 0 fällt k weg", [("(3 | 0)", "x und y vertauscht"), ("(1 | 3)", "x = 1 statt x = 0 gewählt"), ("(0 | 0)", "den Achsenabschnitt vergessen")],
    "Wo hat k keinen Einfluss auf y?", "Bei x = 0 ist k · 0 = 0, also y = 3 für jedes k. Der Punkt ist (0 | 3).",
    lambda: len({k * 0 + 3 for k in range(-5, 6)}) == 1 and len({k * 1 + 3 for k in range(-5, 6)}) > 1 and len({k * 3 + 3 for k in range(-5, 6)}) > 1), g="mehrschritt", regel=FORM)
neu(f, "deuten", "LW", L("Ein Behälter enthält am Anfang 45 l Wasser. Jede Minute fließen 3 l ab. Nach 5 Minuten sind es noch 45 − 3 · 5 = ① l. Leer ist der Behälter, wenn 3 · t = 45 gilt, also nach ② Minuten.",
    K(2), [30, 15], ["45 - 3 * 5", "45 // 3"], ["45 - 15", "5 * 3"], "Die Rate ist negativ: Es wird weniger.", "45 − 15 = 30 l. 45 : 3 = 15 Minuten.",
    {0: [(210, "fb.reihenfolge.links_nach_rechts", "(45 − 3) · 5 gerechnet")]}, hinweis=GZ))
neu(f, "deuten", "FD", FDZ("Ein Taxi kostet 3 € Grundpreis und 2 € je Kilometer: K(x) = 2x + 3. Kim deutet die Zahlen.",
    [("Der Grundpreis ist das Glied ohne x: 3 €.", True), ("Die Zahl vor dem x ist der Preis je Kilometer: 2 €.", True), ("Bei 0 km kostet die Fahrt 2 €.", 2 * 0 + 3 == 2)],
    "Setze x = 0 in den Term ein.", "K(0) = 2 · 0 + 3 = 3. Auch bei 0 km zahlt man den Grundpreis 3 €."))

# ═════════════════════ Kind 2 · Flug a6 · Gleichungssysteme ═════════════════════
f = "a6"
LG = "id.algebra.gleichung_loesen"
neu(f, "pruefen", "LW", L("Prüfe, ob (6 | 1) das System I: x + y = 9 und II: x − y = 1 löst. Einsetzen in I: 6 + 1 = ①. Das ist nicht 9. Einsetzen in II: 6 − 1 = ②. Das ist nicht 1. Also ist (6 | 1) keine Lösung.",
    K(2), [7, 5], ["6 + 1", "6 - 1"], ["1 + 6", "10 - 5"], "Setze x = 6 und y = 1 in die linke Seite ein.", "6 + 1 = 7 und 6 − 1 = 5. Keine Gleichung stimmt.",
    {1: [(7, None, "in II plus gerechnet")]}, hinweis=GZ))
neu(f, "pruefen", "FD", FDZ("Prüfe das Paar (5 | 1) im System I: 2x + y = 11 und II: x − y = 1. Kim prüft.",
    [("In I: 2 · 5 + 1 = 11. Das stimmt.", 2 * 5 + 1 == 11), ("In II: 5 − 1 = 4. Das ist nicht 1.", 5 - 1 == 4), ("Eine Gleichung stimmt, also ist (5 | 1) eine Lösung des Systems.", False)],
    "Ein Paar ist eine Lösung des Systems, wenn es zu beiden Gleichungen passt.", "Gleichung II stimmt nicht. (5 | 1) ist keine Lösung des Systems."))
neu(f, "grafisch", "LW", L("Die Geraden y = x + 1 und y = −x + 5 sollen sich schneiden. Für x = 2 ist x + 1 = ① und −x + 5 = ②. Beide Werte sind gleich. Der Schnittpunkt ist also S(2 | ①).",
    K(2), [3, 3], ["2 + 1", "-2 + 5"], ["1 + 2", "5 - 2"], "Setze für x die Zahl 2 ein.", "2 + 1 = 3 und −2 + 5 = 3. Beide Geraden gehen durch (2 | 3).",
    {1: [(7, "fb.plusminus.zeichen_des_ergebnisses", "5 + 2 gerechnet")]}, hinweis=GZ))
neu(f, "einsetzen", "VW", W("Im System I: y = 2x − 1 und II: 4x − y = 7 soll y aus I in II eingesetzt werden. Welche Rechnung ist richtig?",
    "4x − (2x − 1) = 7, also 2x + 1 = 7 und x = 3",
    [("4x − 2x − 1 = 7, also 2x = 8 und x = 4", "die Klammer fehlt: das Minus wirkt nur auf die erste Zahl"), ("4x − (2x − 1) = 7, also 2x − 1 = 7 und x = 4", "beim Auflösen der Klammer 2x − 1 behalten"), ("4x − (2x − 1) = 7, also 2x + 1 = 7 und x = 8", "nach dem Auflösen nicht durch 2 geteilt")],
    "Setze für y den ganzen Term in Klammern ein.", "4x − (2x − 1) = 4x − 2x + 1 = 2x + 1. 2x + 1 = 7 ergibt x = 3. Dann y = 2 · 3 − 1 = 5.",
    lambda: 4 * 3 - (2 * 3 - 1) == 7 and 4 * 4 - (2 * 4 - 1) != 7 and 4 * 8 - (2 * 8 - 1) != 7 and 4 * 4 - 2 * 4 - 1 != 4 * 4 - (2 * 4 - 1)), g="mehrschritt", regel="rr.minusklammer")
neu(f, "gleichsetzen", "LW", L("Bei I: y = 2x + 1 und II: y = 6x − 11 steht zweimal y = …. Gleichsetzen: 2x + 1 = 6x − 11. Auf beiden Seiten 2x abziehen: 1 = 4x − 11. 11 addieren: ① = 4x. Also ist x = ②.",
    K(2), [12, 3], ["1 + 11", "(1 + 11) // 4"], ["2 * 6", "9 // 3"], "Die Zahl 11 steht mit Minus auf der rechten Seite.", "1 + 11 = 12. 12 : 4 = 3. Probe: y = 2 · 3 + 1 = 7 und y = 6 · 3 − 11 = 7.",
    {0: [(-10, "fb.plusminus.zeichen_des_ergebnisses", "1 − 11 gerechnet")]}, hinweis=GZ), regel="rr.waage")
neu(f, "gleichsetzen", "FD", FDZ("Das System I: y = 3x − 2 und II: y = x + 6 wird durch Gleichsetzen gelöst. Kim rechnet.",
    [("Gleichsetzen: 3x − 2 = x + 6.", True), ("x abziehen: 2x − 2 = 6.", 3 - 1 == 2), ("2 abziehen: 2x = 4, also x = 2.", 6 - 2 == 6 + 2)],
    "Die −2 wird auf der anderen Seite zu +2.", "2x − 2 = 6 ergibt 2x = 8 und x = 4. Dann y = 4 + 6 = 10."), regel="rr.waage")
neu(f, "addition", "LW", L("I: x + y = 12 und II: 3x − y = 8. Addiert man I und II, fällt y weg: 4x = ①. Also ist x = ②. Einsetzen in I: ② + y = 12, also y = ③.",
    K(3), [20, 5, 7], ["12 + 8", "(12 + 8) // 4", "12 - (12 + 8) // 4"], ["10 + 10", "20 / 4", "12 - 5"], "Rechne die rechten Seiten zusammen: 12 + 8.", "4x = 20, x = 5. y = 12 − 5 = 7. Probe in II: 15 − 7 = 8.",
    {0: [(4, None, "die rechten Seiten abgezogen")]}, hinweis=GZ))
neu(f, "addition", "FD", FDZ("System: I: 3x + 2y = 17 und II: 5x − 2y = 7. Kim löst es mit dem Additionsverfahren.",
    [("Die y-Terme +2y und −2y sind Gegenzahlen.", True), ("Addieren: 8x = 24, also x = 3.", 17 + 7 == 24 and 24 // 8 == 3), ("x in I einsetzen: 3 · 3 + 2y = 17, also 2y = 17 + 9 = 26 und y = 13.", 17 + 9 == 17 - 9)],
    "Aus 9 + 2y = 17 folgt 2y, wenn du auf beiden Seiten 9 abziehst.", "2y = 17 − 9 = 8, also y = 4. Probe in II: 5 · 3 − 2 · 4 = 7."))
neu(f, "verfahren", "LW", L("Bei I: y = 4x + 1 und II: y = 2x + 11 steht zweimal y = …. Das Gleichsetzen ist hier geschickt: 4x + 1 = 2x + 11. Dann ist 2x = ①. Also ist x = ②.",
    K(2), [10, 5], ["11 - 1", "(11 - 1) // 2"], ["20 / 2", "10 // 2"], "Auf beiden Seiten 2x abziehen, dann 1 abziehen.", "4x − 2x = 2x und 11 − 1 = 10. x = 5.",
    {1: [(10, None, "nicht durch 2 geteilt")]}, hinweis=GZ), regel="rr.waage")
neu(f, "verfahren", "FD", FDZ("System: I: x + y = 10 und II: x − y = 4. Kim wählt das Additionsverfahren.",
    [("In I und II stehen +y und −y. Das sind Gegenzahlen.", True), ("Darum ist das Additionsverfahren geschickt.", True), ("Addiert man beide Gleichungen, so ist 2x = 6, also x = 3.", 10 + 4 == 6)],
    "Rechne 10 + 4 noch einmal.", "10 + 4 = 14. Also 2x = 14 und x = 7."))
neu(f, "loesbarkeit", "LW", L("I: y = 2x + 1 und II: y = 2x + 5. Gleichsetzen: 2x + 1 = 2x + 5. Auf beiden Seiten 2x abziehen: 1 = 5. Das ist falsch. Beide Geraden haben dieselbe Steigung und schneiden sich nie. Das System hat ① Lösungen.",
    K(1), [0], ["0"], ["1 - 1"], "Eine falsche Aussage heißt: Es passt keine Zahl.", "1 = 5 ist falsch: keine Lösung.",
    {0: [(1, None, "mit genau einer Lösung verwechselt")]}, hinweis=GZ))
neu(f, "loesbarkeit", "FD", FDZ("System: I: y = 3x − 2 und II: 2y = 6x − 4. Kim untersucht, wie viele Lösungen es gibt.",
    [("Teile II durch 2: y = 3x − 2.", 6 // 2 == 3 and 4 // 2 == 2), ("Beide Gleichungen sind gleich.", True), ("Also hat das System keine Lösung.", False)],
    "Wenn beide Gleichungen dieselbe Gerade beschreiben, wie viele Punkte haben sie gemeinsam?", "Beide Gleichungen beschreiben dieselbe Gerade. Jeder ihrer Punkte ist eine Lösung: unendlich viele."))
neu(f, "loesung_parameter", "LW", L("I: x + y = 6 und II: x − y = k. Addiert man I und II, so ist 2x = 6 + k. Für x = 5 muss also 2 · 5 = ① gelten, nämlich 6 + k = ①. Daraus folgt k = ②.",
    K(2), [10, 4], ["2 * 5", "2 * 5 - 6"], ["5 + 5", "10 - 6"], "Setze x = 5 in 2x = 6 + k ein.", "2 · 5 = 10 = 6 + k, also k = 4.",
    {1: [(16, None, "6 addiert statt abgezogen")]}, hinweis=GZ))
neu(f, "loesung_parameter", "FD", FDZ("System: I: y = a · x und II: y = 2x + 6. Kim untersucht, für welches a es keine Lösung gibt.",
    [("Gleichsetzen: a · x = 2x + 6.", True), ("Umstellen: (a − 2) · x = 6.", True), ("Für a = 2 ist 0 · x = 6. Das System hat dann unendlich viele Lösungen.", 0 * 7 == 6)],
    "Gibt es ein x, für das 0 · x = 6 gilt?", "0 · x ist immer 0, nie 6. Für a = 2 gibt es keine Lösung."))
neu(f, "loesung_parameter", "VW", W("System: I: y = k · x und II: y = 3x + 4. Für welches k hat das System keine Lösung?",
    "k = 3: gleiche Steigung, aber verschiedene Achsenabschnitte",
    [("k = 4", "den Achsenabschnitt als Steigung genommen"), ("k = 0", "k = 0 für „keine Lösung“ gehalten"), ("k = −3", "das Vorzeichen der Steigung gedreht")],
    "Gleichsetzen: (k − 3) · x = 4. Wann kann man nicht nach x auflösen?", "Für k = 3 ist 0 · x = 4. Das geht nie. Für jedes andere k gilt x = 4 : (k − 3).",
    lambda: all(((k - 3) * x == 4) for k in range(-6, 7) if k != 3 for x in [F(4, k - 3)]) and not any((3 - 3) * x == 4 for x in range(-50, 51))), g="mehrschritt")
neu(f, "sachaufgabe", "LW", L("Zwei Zahlen haben die Summe 20 und die Differenz 6. Addiert man x + y = 20 und x − y = 6, so ist 2x = ①. Die größere Zahl ist x = ②. Die kleinere Zahl ist y = ③.",
    K(3), [26, 13, 7], ["20 + 6", "(20 + 6) // 2", "20 - (20 + 6) // 2"], ["13 * 2", "26 / 2", "13 - 6"], "Das y fällt beim Addieren weg.", "2x = 26, x = 13. y = 20 − 13 = 7.",
    {2: [(19, None, "x und y verwechselt")]}, hinweis=GZ))
neu(f, "sachaufgabe", "FD", FDZ("Ein Kino verkauft 100 Karten. Erwachsene zahlen 8 €, Kinder 5 €. Die Einnahmen sind 620 €. Kim stellt die Gleichungen auf. x ist die Zahl der Erwachsenen, y die der Kinder.",
    [("Karten: x + y = 100.", True), ("Einnahmen: 8y + 5x = 620.", False), ("Aus der ersten Gleichung folgt y = 100 − x.", 100 - 3 - (100 - 3) == 0)],
    "Wer zahlt 8 €? Zu welcher Unbekannten gehört die 8?", "Erwachsene (x) zahlen 8 €, Kinder (y) zahlen 5 €: 8x + 5y = 620."))

# ═════════════════════ Prüfen ═════════════════════
KOMMA_LUECKE = re.compile(r"\d\s*,\s*[①②③④⑤□]")          # Lücke unmittelbar hinter dem Komma: wäre eine Ziffernfolge, keine Zahl (Auftrag 20)
KOMMA_NEBEN = re.compile(r"[①②③④⑤□],|,[①②③④⑤□]")      # Komma direkt neben einem Lückenzeichen
ZWEIDEUTIG = re.compile(r"\d/\d+[a-zA-Z]|/\([^()]*\(|\)\)/")       # 1/2x · /( … ( · )) /


def texte_von(q):
    return [q["f"]["text"], q["h"], q["w"]] + list(q.get("a", [])) + [q["f"].get("hinweis", "")]


def zahlen_im(text):
    r = set()
    for m in ZAHL.findall(text):
        s = re.sub(r"[  ]", "", m).replace("−", "").replace("-", "").replace(",", ".")
        r.add(F(s))
    return r


def grafik_ok(g):
    if g["typ"] == "tabelle":
        return all(len(z) == len(g["kopf"]) and all(isinstance(x, str) for x in z) for z in g["zeilen"]) and all(isinstance(x, str) for x in g["kopf"])
    if g["typ"] in ("saeulen", "kreisdiagramm"):
        return all(set(w) == {"name", "wert"} and len(w["name"]) <= 8 for w in g["werte"]) and (g["typ"] == "saeulen" or sum(w["wert"] for w in g["werte"]) == 100)
    if g["typ"] == "koordinaten":
        return len(g["x"]) == len(g["y"]) == 2 and set(g) <= {"typ", "x", "y", "graphen", "kreise", "punkte", "schritt_x", "schritt_y", "name_x", "name_y"}
    if g["typ"] == "figur":
        namen = set(g["punkte"])
        return all(l[0] in namen and l[1] in namen for l in g.get("linien", [])) and all(set(w[:3]) <= namen for w in g.get("winkel", [])) and set(g) <= {"typ", "punkte", "linien", "winkel", "flaeche"}
    if g["typ"] == "zahlenstrahl":
        return g["start"] < g["ende"]
    return False


def zaehle(eintraege):
    """(Thema, Lernkarte) -> Zähler der Stufen, nur die fünf neuen Formen in alten Antwortformen."""
    c = defaultdict(Counter)
    for e in eintraege:
        if e["antwortform"] != "bedingung" and any(e["typ"].startswith(x) for x in FORMEN):
            c[(e["thema"], e["aufgabe"]["l"])][e["stufe"]] += 1
    return c


aus = {fl: [] for fl in FLUG}
n_rechnung = n_fb = n_grafik = n_bruch = 0
alle_texte = set()
bau_je_flug = defaultdict(set)
for fl, liste in VORHANDEN.items():
    for e in liste:
        alle_texte.add(e["aufgabe"]["f"]["text"])
        bau_je_flug[fl].add(bau_ohne_zahl(e["aufgabe"]["f"]["text"]))
for a in sorted(A, key=lambda a: (list(FLUG).index(a["flug"]), a["s"])):          # Schwierigkeit aufsteigend, bei gleicher Stufe in der Reihenfolge des Programms
    q = a["aufgabe"]
    kenn = f"{FLUG[a['flug']][5]}-V{len(aus[a['flug']]) + 1:02d}"
    assert a["regel"] in REGELN, (kenn, a["regel"])
    assert ip.STUFE_VON[q["g"]] == q["s"], (kenn, q["g"], q["s"])
    assert q["y"] in ("zahl", "auswahl", "luecken") and q["p"] == "uebung", kenn
    assert a["typ"] != "LW" or q["y"] == "luecken", (kenn, "Lückenweg nur mit Lücken")
    assert a["zaehlt"] == ("nein" if a["typ"] == "LW" else "ja"), kenn
    text = q["f"]["text"]
    for t in texte_von(q):
        assert not ZWEIDEUTIG.search(t), (kenn, "Bruch nicht eindeutig", t)
        assert "Leo" not in re.findall(r"\w+", t) and "Rosa" not in re.findall(r"\w+", t), (kenn, "Name")
        n_bruch += bool(re.search(r"\d/[\d(]|\)/\(|[a-z]/\d", t))
    assert text not in alle_texte and text not in BESTAND_TEXT[a["thema"]], (kenn, "Fragetext schon vorhanden")
    b = bau_ohne_zahl(text)
    assert b not in bau_je_flug[a["flug"]] and b not in BESTAND_BAU[a["thema"]], (kenn, "Fragetext nur mit anderen Zahlen schon vorhanden", b)
    if "grafik" in q["f"]:
        assert grafik_ok(q["f"]["grafik"]), (kenn, "grafik")
        n_grafik += 1
    alle_texte.add(text)
    bau_je_flug[a["flug"]].add(b)
    eintrag = dict(kennung=kenn, thema=a["thema"], lernkarte=q["l"], stufe=q["s"], typ=TYP[a["typ"]], antwortform=q["y"], regel=a["regel"], regel_name=REGELN[a["regel"]]["name"], zaehlt=a["zaehlt"], fehlbilder=[])

    def fb_eintrag(ort, antwort, fbk, beschr):
        global n_fb
        assert fbk is None or fbk in FEHLBILD, (kenn, fbk)
        n_fb += 1
        eintrag["fehlbilder"].append(dict(**ort, antwort=antwort, fehlbild=fbk, regel_des_fehlbilds=FEHLBILD.get(fbk), beschreibung=beschr))

    if q["y"] == "zahl":
        soll = ip.rechne(q["c"])
        assert soll == ip.zahlwert(q["o"]["wert"]) == z2(a["zweit"][0]), (kenn, soll, z2(a["zweit"][0]))
        n_rechnung += 1
        if abs(soll) >= 10:
            assert abs(soll) not in zahlen_im(text), (kenn, "Ergebnis steht schon im Text")
            assert abs(soll) not in zahlen_im(q["h"]), (kenn, "Tipp verrät das Ergebnis")
        werte = set()
        for w, fbk, beschr in a["fb"]:
            assert w != q["o"]["wert"] and w not in werte, (kenn, w)
            werte.add(w)
            fb_eintrag({}, w, fbk, beschr)
    elif q["y"] == "luecken":
        assert not KOMMA_LUECKE.search(text + " " + q["f"]["schablone"]), (kenn, "Lücke hinter dem Komma – Ziffernfolge")
        assert not KOMMA_NEBEN.search(text + " " + q["f"]["schablone"]), (kenn, "Komma direkt neben einer Lücke")
        soll = [ip.rechne(c) for c in q["c"]]
        assert soll == q["o"]["werte"] == [z2(z) for z in a["zweit"]], (kenn, soll, [z2(z) for z in a["zweit"]])
        assert all(isinstance(w, int) for w in q["o"]["werte"]) and q["f"]["schablone"].count("□") == len(soll), kenn
        im_text, im_tipp = zahlen_im(text), zahlen_im(q["h"])
        for v in soll:
            assert abs(v) not in im_text, (kenn, v, "die gesuchte Zahl steht schon im Text")
            assert abs(v) < 10 or abs(v) not in im_tipp, (kenn, v, "Tipp verrät die Zahl")
        n_rechnung += len(soll)
        for i, liste in sorted(a["fb"].items()):
            werte = set()
            for w, fbk, beschr in liste:
                assert w != soll[i] and w not in werte, (kenn, i, w)
                werte.add(w)
                fb_eintrag({"luecke": i + 1}, w, fbk, beschr)
    else:
        assert a["zweit"]() is True and len(set(q["a"])) == len(q["a"]) >= 3, kenn
        assert set(a["fb"]) == set(range(len(q["a"]))) - {q["o"]["index"]}, kenn
        for i, (fbk, beschr) in sorted(a["fb"].items()):
            fb_eintrag({"index": i}, q["a"][i], fbk, beschr)
    eintrag["aufgabe"] = q
    aus[a["flug"]].append(eintrag)

lagen = defaultdict(list)
for a in A:
    if a["aufgabe"]["y"] == "auswahl":
        lagen[len(a["aufgabe"]["a"])].append(a["aufgabe"]["o"]["index"])
assert set(lagen[4]) == {0, 1, 2, 3}, lagen


def lauf(pfad):
    r = subprocess.run([sys.executable, "-I", os.path.join(WURZEL, "tools", "inhalt_pruefen.py"), pfad], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


je_thema = defaultdict(list)
for e_liste in aus.values():
    for e in e_liste:
        je_thema[e["thema"]].append(e["aufgabe"])
print("Thema                          neu  inhalt_pruefen vorher → nachher")
with tempfile.TemporaryDirectory() as tmp:
    for thema, liste in je_thema.items():
        quelle = os.path.join(WURZEL, "inhalte", "themen", f"{thema}.json")
        d = json.load(open(quelle, encoding="utf-8"))
        assert all(q["l"] in {e["lernziel"] for e in d["inhalt"]["etappen"]} and q["t"] in {t["k"] for t in d["inhalt"]["teilfaehigkeiten"]} for q in liste), thema
        code0, aus0 = lauf(quelle)
        d["aufgaben"] = d["aufgaben"] + liste
        ziel = os.path.join(tmp, f"{thema}.json")
        json.dump(d, open(ziel, "w", encoding="utf-8"), ensure_ascii=False)
        code1, aus1 = lauf(ziel)
        print(f"{thema:30} {len(liste):3}  Code {code0} → {code1}")
        if code1 != 0:
            print(aus1[-2500:])
        assert code0 == 0 and code1 == 0, thema

# ═════════════════════ Zählen und Dateien schreiben ═════════════════════
tabelle = []
formen_summe = Counter()
offen = []
for flug, (titel, kind, klasse, runde, themen, kuerzel, _) in FLUG.items():
    vor = zaehle(VORHANDEN[flug])
    neu_e = aus[flug]
    nach = zaehle(VORHANDEN[flug] + neu_e)
    karten = [k for k in karten_von(flug) if (flug,) + k not in ZURUECKGESTELLT]
    v3 = sum(1 for k in karten if sum(vor[k].values()) >= 3)
    n3 = sum(1 for k in karten if sum(nach[k].values()) >= 3)
    fehl_vor = sum(max(0, 3 - sum(vor[k].values())) for k in karten)
    fehl_nach = sum(max(0, 3 - sum(nach[k].values())) for k in karten)
    for k in karten:
        if sum(nach[k].values()) < 3:
            offen.append((flug, k[1], 3 - sum(nach[k].values())))
    for e in neu_e:
        formen_summe[(e["typ"].split(" (")[0], e["stufe"])] += 1
    tabelle.append((flug, len(karten), v3, fehl_vor, len(neu_e), n3, fehl_nach, runde))
    if neu_e:
        assert fehl_nach == 0, (flug, [o for o in offen if o[0] == flug])
        assert {e["lernkarte"] for e in neu_e} <= {k[1] for k in karten}, flug
        json.dump({"stand": "2026-11-27", "flug": flug, "titel": titel, "fuer": kind, "klasse": klasse, "themen": themen,
                   "hinweis": "Aufgaben auf Vorrat in neuer Form (Lückenweg, Fehler-Detektiv, Verfahren wählen, Zwei Wege vergleichen, Brücke), rollend-4. Nicht eingespielt. Je Eintrag: Zusatzangaben (Regel-Kennung, Fehlbilder, Typ, Zählvorschlag ja/nein) "
                              "und unter „aufgabe“ die Aufgabe im Format von inhalte/README.md. Reihenfolge: Stufe aufsteigend.",
                   "aufgaben": neu_e}, open(os.path.join(HIER, f"{flug}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        typen = Counter(e["typ"].split(" (")[0] for e in neu_e)
        print(f"{flug:9} {kind}: {len(neu_e)} neu; Stufen {[sum(1 for e in neu_e if e['stufe'] == s) for s in (1, 2, 3)]}; Lernkarten {len(karten)}; mit Zeichnung {sum(1 for e in neu_e if 'grafik' in e['aufgabe']['f'])}; {dict(typen)}")
print()
print("Flug      Lernkarten  vorher≥3  Fehlbedarf  neu  jetzt≥3  Rest")
for t in tabelle:
    print(f"{t[0]:9} {t[1]:10} {t[2]:9} {t[3]:11} {t[4]:4} {t[5]:8} {t[6]:5}")
print("Summe     ", sum(t[1] for t in tabelle), sum(t[2] for t in tabelle), sum(t[3] for t in tabelle), sum(t[4] for t in tabelle), sum(t[5] for t in tabelle), sum(t[6] for t in tabelle))
print("nach Form und Stufe:", dict(sorted(formen_summe.items())))
if offen:
    print("noch offen (Aufgaben fehlen noch):", {fl: sum(o[2] for o in offen if o[0] == fl) for fl in dict.fromkeys(o[0] for o in offen)})
print(f"{len(A)} Aufgaben; {n_rechnung} Rechnungen zweifach nachgerechnet; {n_fb} Fehlbilder, davon {sum(1 for fl in aus.values() for e in fl for x in e['fehlbilder'] if x['fehlbild'])} mit Kennung; "
      f"{n_grafik} Aufgaben mit Zeichnung; {n_bruch} Texte mit Bruchstrich, keiner zweideutig")
print("OK")
