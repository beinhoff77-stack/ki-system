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
