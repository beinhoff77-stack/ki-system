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
