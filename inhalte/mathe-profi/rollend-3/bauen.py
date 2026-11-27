"""Mathe-Profi, Auftrag 19: Aufgaben auf Vorrat, dritte Runde (rollendes System, Stufe 3).

Aufruf: python3 -I inhalte/mathe-profi/rollend-3/bauen.py
Kind 1: ge3, r1, g2. Kind 2: ge4, f2, a6 (Reihenfolge aus lehrplan-kinder/route.md). Je Flug 15 bis 18 Aufgaben in Typen ohne Bau und 5 des Typs „bedingung“.
Geprüft wird wie in rollend-2 (zweifach nachgerechnet, pruefe_aufgabe, inhalt_pruefen an einer Kopie, Brüche eindeutig, Form der Zeichnungen).
Schreibt je Flug eine Datei <flug>.json. Nur Inhalte. Nichts wird eingespielt.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
from fractions import Fraction as F

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
sys.path.insert(0, os.path.join(WURZEL, "tools"))
import inhalt_pruefen as ip      # noqa: E402
import bedingung as bd           # noqa: E402

KENN = json.load(open(os.path.join(HIER, "..", "regeln-uebersicht", "kennungen.json"), encoding="utf-8"))["kennungen"]
REGELN = {e["kennung"]: e for e in KENN}
FEHLBILD = {f["kennung"]: e["kennung"] for e in KENN for f in e["fehlbilder"]}
TYP = {4: "Lückenweg", 12: "Fehler-Detektiv (einfache Form)", 13: "Verfahren wählen (einfache Form)", 14: "Zwei Wege vergleichen", 17: "Umkehren", "B": "Brücke", "A": "Anwenden", "V": "Viele richtige Antworten (bedingung)"}
# Flug: (Titel, Kind, Klasse, Themen-Dateien, Kürzel der Kennung)
FLUG = {
    "ge3": ("Winkel", "Kind 1", 5, ["geometrie.winkel"], "GE3"),
    "r1": ("Umfang und Fläche", "Kind 1", 5, ["messen.flaechen"], "R1"),
    "g2": ("Dreisatz und direkte Proportionalität (Teil 1)", "Kind 1", 5, ["groessen.proportional"], "G2"),
    "ge4": ("Dreiecke, Vierecke und Konstruktion", "Kind 2", 7, ["geometrie.winkelsaetze", "geometrie.konstruktion"], "GE4"),
    "f2": ("Lineare Funktionen", "Kind 2", 8, ["funktionen.linear"], "F2"),
    "a6": ("Gleichungssysteme", "Kind 2", 8, ["gleichungen.lgs2"], "A6"),
}
KARTE = {}       # (Thema, Lernkarte) -> Teilfähigkeit, aus dem Bestand gelesen
for _fl in FLUG.values():
    for _t in _fl[3]:
        for _a in json.load(open(os.path.join(WURZEL, "inhalte", "themen", _t + ".json"), encoding="utf-8"))["aufgaben"]:
            KARTE[(_t, _a["l"])] = _a["t"]
A = []
WAAGE, GEGEN, LOES, MK, PM = "rr.waage", "rr.gegenrechnung", "id.algebra.gleichung_loesen", "rr.minusklammer", "rr.plusminus"
WINK, DECK, AUS, RE = "id.geometrie.winkel", "id.geometrie.deckungsgleich", "id.flaeche_raum.auslegen", "id.flaeche_raum.aus_dem_rechteck"
VERH, GR, SW, WERT = "rr.verhaeltnis", "id.verhaeltnisse.groesse", "rr.stellenwert", "id.verhaeltnisse.wert_fuer_eins"
ZU, WACHS, FORM = "id.funktionen.zuordnung", "id.funktionen.wachstum", "id.funktionen.gleichung_form"


def z2(ausdruck):
    genau = re.sub(r"(?<![\w.])(\d+)(?![\w.])", r"F(\1)", ausdruck)
    return F(eval(genau, {"__builtins__": {}}, {"F": F, "abs": abs}))


def neu(flug, l, typ, s, g, regel, zaehlt, aufgabe, zweit, fb, probe=None):
    themen = [t for t in FLUG[flug][3] if (t, l) in KARTE]
    assert len(themen) == 1, (flug, l)
    A.append(dict(flug=flug, thema=themen[0], typ=typ, regel=regel, zaehlt=zaehlt, aufgabe={"l": l, "t": KARTE[(themen[0], l)], "p": "uebung", "s": s, "g": g, **aufgabe}, zweit=zweit, fb=fb, probe=probe))


def mit(d, grafik):
    if grafik:
        d["f"]["grafik"] = grafik
    return d


def luecken(text, schablone, werte, c, h, w, hinweis="Je Lücke eine ganze Zahl.", grafik=None):
    return mit({"y": "luecken", "f": {"text": text, "schablone": schablone, "hinweis": hinweis}, "o": {"werte": werte}, "c": c, "h": h, "w": w}, grafik)


def zahl(text, wert, c, h, w, einheit=None, grafik=None):
    return mit({"y": "zahl", "f": {"text": text}, "o": {"wert": wert, **({"einheit": einheit} if einheit else {})}, "c": c, "h": h, "w": w}, grafik)


def wahl(text, antworten, index, h, w, grafik=None):
    return mit({"y": "auswahl", "f": {"text": text}, "a": antworten, "o": {"index": index}, "h": h, "w": w}, grafik)


def bed(text, felder, bedingungen, beispiel, gegen, h, w, gut=None):
    """bedingungen: [(name, pruefe, zeige oder None, hinweis)]; gegen: [(werte, name)]"""
    bs = [{"name": n, "pruefe": p, **({"zeige": z} if z is not None else {}), "hinweis": hi} for n, p, z, hi in bedingungen]
    o = {"bedingungen": bs, "beispiel": beispiel, **({"gut": gut} if gut else {}), "gegenbeispiele": [{"werte": we, "verletzt": n} for we, n in gegen]}
    return {"y": "bedingung", "f": {"text": text, "felder": [{"art": a} for a in felder]}, "o": o, "h": h, "w": w}


K = lambda n: "; ".join(f"{'①②③④⑤'[i]} = □" for i in range(n))
UND = lambda *x: ["und", *x]
ODER = lambda *x: ["oder", *x]
G, R = "ganz", "rational"
TAB = lambda kopf, *zeilen: {"typ": "tabelle", "kopf": kopf, "zeilen": [list(z) for z in zeilen]}

KO = lambda x, y, **mehr: {"typ": "koordinaten", "x": x, "y": y, **mehr}
GZ = "Je Lücke eine ganze Zahl (mit Minus, falls negativ)."

import math
WEG = {"g2": {"erkennen", "vervielfachen", "pruefen"}}       # diese drei Lernkarten gehören zu g2-teil2 (rollend-2)


def par(theta, marken):
    """Zwei Parallelen g (oben) und h (unten), geschnitten von k unter dem Winkel theta. marken: [(Punkt 'S' oder 'T', Lage 'RO'|'LO'|'LU'|'RU', Text)].
    Aufbau wie die Zeichnungen im Bestand von geometrie.winkelsaetze."""
    r = math.radians(theta)
    dx, dy = round(1.6 * math.cos(r), 3), round(1.6 * math.sin(r), 3)
    sx = round(2 + 3 / math.tan(r), 3)
    p = {}
    for n, (x, y) in (("S", (sx, 3.0)), ("T", (2.0, 0.0))):
        p[n] = [x, y]
        p[f"_{n}R"], p[f"_{n}L"], p[f"_{n}U"], p[f"_{n}D"] = [round(x + 1.6, 3), y], [round(x - 1.6, 3), y], [round(x + dx, 3), round(y + dy, 3)], [round(x - dx, 3), round(y - dy, 3)]
    lo, hi = min(sx, 2.0) - 3, max(sx, 2.0) + 3
    p.update({"_g1": [lo, 3.0], "_g2": [hi, 3.0], "_h1": [lo, 0.0], "_h2": [hi, 0.0], "_k1": p["_TD"], "_k2": p["_SU"]})
    lage = {"RO": ("R", "U"), "LO": ("U", "L"), "LU": ("L", "D"), "RU": ("D", "R")}
    return {"typ": "figur", "punkte": p, "linien": [["_g1", "_g2", "g"], ["_h1", "_h2", "h"], ["_k1", "_k2", "k"]],
            "winkel": [[n, f"_{n}{lage[l][0]}", f"_{n}{lage[l][1]}", t] for n, l, t in marken]}


def dreieck(alpha, beta, namen=("α", "β", "γ")):
    """Dreieck ABC mit AB waagrecht, Winkel alpha bei A und beta bei B (maßstäblich)."""
    ta, tb = math.tan(math.radians(alpha)), math.tan(math.radians(beta))
    cx = 6 * tb / (ta + tb)
    return {"typ": "figur", "punkte": {"A": [0, 0], "B": [6, 0], "C": [round(cx, 3), round(cx * ta, 3)]}, "linien": [["A", "B"], ["B", "C"], ["C", "A"]],
            "winkel": [w for w in (["A", "B", "C", namen[0]], ["B", "C", "A", namen[1]], ["C", "A", "B", namen[2]]) if w[3]]}


# ═════════════════════ Kind 1 · Flug ge3 · Winkel ═════════════════════
f = "ge3"
neu(f, "ergaenzen", 4, 1, "direkt", WINK, "nein",
    luecken("Ein rechter Winkel wird in zwei Teile geteilt. Ein Teil hat 37°, der andere 90° − 37° = ①°. Ein gestreckter Winkel wird in zwei Teile geteilt. Ein Teil hat 37°, der andere ②°.", K(2), [53, 143], ["90 - 37", "180 - 37"],
            "Das Ganze ist erst 90°, dann 180°.", "90° − 37° = 53°. 180° − 37° = 143°."),
    ["53", "53+90"], {1: [(53, None, "auch beim gestreckten Winkel auf 90° ergänzt"), (323, None, "auf 360° ergänzt")]})
neu(f, "kreuzung", 4, 1, "direkt", WINK, "nein",
    luecken("Zwei Geraden schneiden sich. Ein Winkel hat 65°. Gegenüber liegt ein Winkel von ①°. Jeder der beiden Nachbarwinkel hat ②°. Alle vier zusammen ergeben ③°.", K(3), [65, 115, 360], ["65", "180 - 65", "65 + 115 + 65 + 115"],
            "Gegenüberliegende Winkel sind gleich. Nachbarwinkel ergeben zusammen 180°.", "Gegenüber: 65°. Daneben: 180° − 65° = 115°. Zusammen 360°."),
    ["65", "115", "2*180"], {1: [(65, "fb.winkel.neben_statt_scheitel", "Nachbarwinkel wie den gegenüberliegenden behandelt"), (25, None, "auf 90° ergänzt")]})
neu(f, "ergaenzen", 13, 1, "erkennen", WINK, "ja",
    wahl("Zwei Winkel liegen nebeneinander an einer Geraden und bilden zusammen einen gestreckten Winkel. Einer ist bekannt. Wie findest du den anderen?",
         ["90° minus den bekannten Winkel", "Er ist gleich groß.", "180° minus den bekannten Winkel", "360° minus den bekannten Winkel"], 2,
         "Wie groß ist ein gestreckter Winkel?", "Ein gestreckter Winkel hat 180°. Der fehlende Winkel ist 180° minus der bekannte."),
    lambda: True, {0: (None, "rechter statt gestreckter Winkel"), 1: ("fb.winkel.neben_statt_scheitel", "Nebenwinkel wie Scheitelwinkel behandelt"), 3: (None, "voller Winkel statt gestreckter")})
neu(f, "kreuzung", 12, 1, "erkennen", WINK, "ja",
    wahl("Zwei Geraden schneiden sich. Ein Winkel hat 50°. Ole sagt: „Dann hat der Winkel direkt daneben auch 50°.“ Was stimmt?",
         ["Ole hat recht.", "Der Winkel daneben hat 40°.", "Alle vier Winkel haben 90°.", "Der Winkel daneben hat 130°. 50° hat der gegenüberliegende Winkel."], 3,
         "Welche Winkel an einer Kreuzung sind gleich groß?", "Gleich groß sind die gegenüberliegenden Winkel. Nachbarwinkel ergeben 180°: 180° − 50° = 130°."),
    lambda: 180 - 50 == 130, {0: ("fb.winkel.neben_statt_scheitel", "wie Ole Nachbarwinkel für gleich gehalten"), 1: (None, "auf 90° ergänzt"), 2: (None, "gilt nur, wenn die Geraden senkrecht stehen")})
neu(f, "verstehen", 13, 1, "erkennen", WINK, "ja",
    wahl("Du willst die Behauptung „Gegenüberliegende Winkel an einer Kreuzung sind immer spitz“ widerlegen. Was genügt?",
         ["ein Gegenbeispiel: zwei Geraden, bei denen ein Winkel 120° hat", "viele Beispiele mit spitzen Winkeln", "ein Beispiel mit zwei Winkeln von 40°"], 0,
         "Was braucht man, um „immer“ zu widerlegen?", "Ein einziges Gegenbeispiel genügt: Hat ein Winkel 120°, dann hat der gegenüberliegende auch 120° – und das ist nicht spitz."),
    lambda: 120 > 90, {1: (None, "Beispiele widerlegen nichts"), 2: (None, "ein passendes Beispiel widerlegt nichts")})
neu(f, "um_punkt", 17, 2, "umkehr", WINK, "ja",
    zahl("Um einen Punkt liegen vier Winkel: drei gleich große und einer mit 60°. Wie groß ist jeder der drei gleichen Winkel?", 100, "(360 - 60) // 3",
         "Alle Winkel um einen Punkt ergeben zusammen 360°.", "360° − 60° = 300°. Geteilt durch 3: 100°.", einheit="°"),
    ["300/3"], [(40, None, "mit 180° statt 360° gerechnet"), (120, None, "die 60° nicht abgezogen")])
neu(f, "um_punkt", 14, 2, "mehrschritt", WINK, "ja",
    luecken("Auf einer Seite einer Geraden liegen drei Winkel nebeneinander: 40°, ein unbekannter und 85°. Weg A: 180° − 40° − 85°. Weg B: erst 40° + 85° = ①°, dann 180° − ①° = ②°.", K(2), [125, 55], ["40 + 85", "180 - (40 + 85)"],
            "Beide Wege müssen denselben Winkel ergeben.", "40° + 85° = 125°. 180° − 125° = 55°. Weg A: 180° − 40° = 140°, 140° − 85° = 55°."),
    ["125", "180-40-85"], {1: [(235, None, "auf 360° ergänzt")]})
neu(f, "uhr", 17, 2, "umkehr", WINK, "ja",
    zahl("Der Minutenzeiger einer Uhr hat sich um 150° gedreht. Wie viele Minuten sind vergangen?", 25, "150 // 6",
         "Um wie viel Grad dreht sich der Minutenzeiger in einer Minute?", "In 60 Minuten 360°, also 6° je Minute. 150° : 6° = 25 Minuten.", einheit="min"),
    ["150*60/360"], [(5, None, "durch 30 geteilt: Abstände zwischen den Zahlen statt Minuten"), (900, "fb.verhaeltnis.falsche_richtung", "mal 6 statt geteilt durch 6")])
neu(f, "drehungen", "B", 2, "darstellung", WINK, "ja",
    wahl("Du schaust nach Norden und drehst dich im Uhrzeigersinn um 135°. In welche Richtung schaust du jetzt?", ["Osten", "Südosten", "Süden", "Südwesten"], 1,
         "Zwischen zwei Nachbarrichtungen liegen 45°.", "135° sind drei Schritte von 45°: Nordosten, Osten, Südosten."),
    lambda: 135 // 45 == 3 and ["N", "NO", "O", "SO"][3] == "SO", {0: (None, "nur 90° gedreht"), 2: (None, "180° gedreht"), 3: (None, "einen Schritt zu weit")})
neu(f, "drehungen", 17, 2, "umkehr", WINK, "ja",
    zahl("Du schaust nach Westen und drehst dich auf dem kürzesten Weg nach Nordosten. Um wie viel Grad drehst du dich?", 135, "3 * 45",
         "Zähle die Schritte: Westen, Nordwesten, Norden, Nordosten.", "Drei Schritte von je 45°: 135°.", einheit="°"),
    ["360-225"], [(225, None, "den längeren Weg genommen"), (90, None, "nur bis Norden gedreht"), (180, None, "die Gegenrichtung genommen")])
neu(f, "figuren", "A", 2, "mehrschritt", WINK, "ja",
    zahl("In einem Rechteck teilt die Diagonale eine Ecke in zwei Winkel. Einer hat 28°. Wie groß ist der andere?", 62, "90 - 28",
         "Wie groß ist jede Ecke im Rechteck?", "Jede Ecke hat 90°. 90° − 28° = 62°.", einheit="°"),
    ["31*2"], [(152, None, "auf 180° ergänzt"), (28, None, "beide Teile für gleich gehalten")])
neu(f, "kreuzung", 17, 3, "verknuepfen", WINK, "ja",
    zahl("Zwei Geraden schneiden sich. Ein Winkel ist um 40° größer als sein Nachbarwinkel. Wie groß ist der kleinere der beiden?", 70, "(180 - 40) // 2",
         "Beide zusammen ergeben 180°.", "Kleiner Winkel x, großer x + 40°. Zusammen 2x + 40° = 180°, also x = 70°.", einheit="°"),
    ["140/2"], [(110, None, "den größeren Winkel genannt"), (140, None, "180 − 40 nicht halbiert")])
neu(f, "uhr", 12, 3, "fehler", WINK, "ja",
    zahl("Es ist 3:30 Uhr. Kim sagt: „Der Stundenzeiger steht auf der 3, der Minutenzeiger auf der 6. Der Winkel ist 90°.“ Wie groß ist der Winkel zwischen den Zeigern wirklich?", 75, "90 - 30 // 2",
         "Bleibt der Stundenzeiger eine halbe Stunde lang auf der 3 stehen?", "In 30 Minuten wandert der Stundenzeiger 15° weiter Richtung 4. Der Winkel ist 90° − 15° = 75°.", einheit="°"),
    ["180-(3*30+15)"], [(90, None, "wie Kim: Stundenzeiger auf der 3 festgehalten"), (105, None, "die 15° dazugezählt statt abgezogen")])
neu(f, "figuren", 17, 3, "rueckwaerts", WINK, "ja",
    zahl("Eine Ecke eines Quadrats wird durch zwei Linien in drei Winkel geteilt. Der mittlere ist doppelt so groß wie jeder der beiden äußeren. Wie groß ist der mittlere Winkel?", 45, "90 / 4 * 2",
         "Die drei Teile ergeben zusammen 90°. Wie viele „äußere Winkel“ sind das?", "Äußerer Winkel x, mittlerer 2x: x + 2x + x = 90°, also x = 22,5°. Der mittlere hat 45°.", einheit="°"),
    ["90/2"], [(30, None, "die Ecke in drei gleiche Teile geteilt"), (22.5, None, "den äußeren Winkel genannt")])
neu(f, "verstehen", 12, 3, "begruenden", WINK, "ja",
    wahl("Behauptung: „Zwei Winkel, die zusammen 180° ergeben, sind immer gleich groß.“ Was stimmt?",
         ["Das stimmt immer.", "Das stimmt nie.", "Das stimmt nicht immer: 70° und 110° ergeben 180° und sind verschieden.", "Das stimmt, denn 90° + 90° = 180°."], 2,
         "Suche ein Gegenbeispiel.", "70° + 110° = 180°, aber 70° ist nicht 110°. Ein Gegenbeispiel genügt. Gleich groß sind sie nur bei 90° und 90°."),
    lambda: 70 + 110 == 180, {0: (None, "kein Gegenbeispiel gesucht"), 1: (None, "90° und 90° ist ein Fall, in dem es stimmt"), 3: (None, "ein Beispiel beweist kein „immer“")})
neu(f, "ergaenzen", "V", 1, "direkt", WINK, "ja",
    bed("Nenne zwei verschiedene Winkel (ganze Grad), die zusammen einen rechten Winkel ergeben. Beide sollen größer als 20° sein.", [G, G],
        [("beide größer als 20°", [">", ["min", "$alle"], 20], ["min", "$alle"], "Dein kleinerer Winkel hat {}°."), ("verschieden", ["verschieden", "$alle"], None, "Die zwei Winkel sollen verschieden sein."),
         ("zusammen ein rechter Winkel", ["=", ["summe", "$alle"], 90], ["summe", "$alle"], "Deine Winkel ergeben zusammen {}°.")],
        [30, 60], [([10, 80], "beide größer als 20°"), ([45, 45], "verschieden"), ([30, 70], "zusammen ein rechter Winkel")],
        "Wie groß ist ein rechter Winkel?", "Ein rechter Winkel hat 90°. Zum Beispiel 30° und 60°.", gut=[[21, 69], [50, 40]]), None, None)
neu(f, "kreuzung", "V", 2, "umkehr", WINK, "ja",
    bed("Zwei Geraden schneiden sich. Nenne die vier Winkel der Reihe nach im Kreis herum. Der erste soll stumpf sein.", [G, G, G, G],
        [("erster Winkel stumpf", UND([">", "$1", 90], ["<", "$1", 180]), "$1", "Dein erster Winkel hat {}°."),
         ("gegenüberliegende Winkel passen", UND(["=", "$1", "$3"], ["=", "$2", "$4"]), None, "Bei dir sind gegenüberliegende Winkel nicht gleich groß."),
         ("Nachbarwinkel passen", ["=", ["+", "$1", "$2"], 180], ["+", "$1", "$2"], "Dein erster und dein zweiter Winkel ergeben zusammen {}°.")],
        [120, 60, 120, 60], [([60, 120, 60, 120], "erster Winkel stumpf"), ([120, 60, 110, 70], "gegenüberliegende Winkel passen"), ([120, 70, 120, 70], "Nachbarwinkel passen")],
        "Der erste und der dritte Winkel liegen sich gegenüber.", "Zum Beispiel 120°, 60°, 120°, 60°: Gegenüber gleich, nebeneinander zusammen 180°.", gut=[[91, 89, 91, 89]]), None, None)
ueber = ["anzahl_positiv", ["liste", ["-", "$1", 180], ["-", "$2", 180], ["-", "$3", 180]]]
neu(f, "um_punkt", "V", 2, "mehrschritt", WINK, "ja",
    bed("Nenne drei verschiedene Winkel (ganze Grad), die zusammen genau um einen Punkt herum passen. Einer davon soll überstumpf sein, also größer als 180°.", [G, G, G],
        [("jeder Winkel größer als 0°", [">", ["min", "$alle"], 0], ["min", "$alle"], "Dein kleinster Winkel hat {}°."), ("verschieden", ["verschieden", "$alle"], None, "Die drei Winkel sollen verschieden sein."),
         ("passen genau um einen Punkt", ["=", ["summe", "$alle"], 360], ["summe", "$alle"], "Deine Winkel ergeben zusammen {}°."), ("einer ist überstumpf", ["=", ueber, 1], ["max", "$alle"], "Dein größter Winkel hat {}°.")],
        [200, 100, 60], [([200, 170, -10], "jeder Winkel größer als 0°"), ([200, 80, 80], "verschieden"), ([200, 100, 50], "passen genau um einen Punkt"), ([150, 120, 90], "einer ist überstumpf")],
        "Wie viel Grad hat der volle Winkel?", "Zusammen 360°. Zum Beispiel 200°, 100° und 60°.", gut=[[181, 100, 79]]), None, None)
zeiger = ["min", ["liste", ["*", 30, "$1"], ["-", 360, ["*", 30, "$1"]]]]
neu(f, "uhr", "V", 2, "umkehr", WINK, "ja",
    bed("Nenne eine volle Stunde (1 bis 12), zu der der kleinere Winkel zwischen den beiden Zeigern größer als 90° ist, aber kein gestreckter Winkel.", [G],
        [("volle Stunde von 1 bis 12", UND([">=", "$1", 1], ["<=", "$1", 12]), "$1", "Deine Zahl ist {}."), ("Winkel größer als 90°", [">", zeiger, 90], zeiger, "Zu deiner Uhrzeit ist der Winkel {}°."),
         ("kein gestreckter Winkel", ["!=", zeiger, 180], zeiger, "Zu deiner Uhrzeit ist der Winkel {}° – das ist ein gestreckter Winkel.")],
        [4], [([13], "volle Stunde von 1 bis 12"), ([3], "Winkel größer als 90°"), ([6], "kein gestreckter Winkel"), ([11], "Winkel größer als 90°")],
        "Zwischen zwei Zahlen auf der Uhr liegen 30°.", "Um 4 Uhr sind es 4 · 30° = 120°. Es passen 4, 5, 7 und 8 Uhr.", gut=[[5], [7], [8]]), None, None)
neu(f, "drehungen", "V", 3, "verknuepfen", WINK, "ja",
    bed("Du drehst dich zweimal nacheinander im Uhrzeigersinn. Jede Drehung ist ein Vielfaches von 45°, größer als 0° und kleiner als 360°. Die erste Drehung ist kleiner als die zweite. Am Ende schaust du genau in die Gegenrichtung. Nenne beide Drehungen in Grad.", [G, G],
        [("Vielfache von 45° zwischen 0° und 360°", UND(["teilbar", "$1", 45], ["teilbar", "$2", 45], [">", ["min", "$alle"], 0], ["<", ["max", "$alle"], 360]), None, "Jede Drehung soll ein Vielfaches von 45° sein, größer als 0° und kleiner als 360°."),
         ("erste Drehung kleiner als die zweite", ["<", "$1", "$2"], None, "Deine erste Drehung ist nicht kleiner als die zweite."),
         ("am Ende Gegenrichtung", ODER(["=", ["summe", "$alle"], 180], ["=", ["summe", "$alle"], 540]), ["summe", "$alle"], "Zusammen drehst du dich um {}°.")],
        [45, 135], [([40, 140], "Vielfache von 45° zwischen 0° und 360°"), ([135, 45], "erste Drehung kleiner als die zweite"), ([45, 90], "am Ende Gegenrichtung"), ([90, 90], "erste Drehung kleiner als die zweite")],
        "Um wie viel Grad muss man sich insgesamt drehen, um in die Gegenrichtung zu schauen?", "Insgesamt 180° (oder eine volle Drehung mehr: 540°). Zum Beispiel 45° und 135°.", gut=[[225, 315]]), None, None)

# ═════════════════════ Kind 1 · Flug r1 · Umfang und Fläche ═════════════════════
f = "r1"
neu(f, "einheitsquadrate", 4, 1, "direkt", AUS, "nein",
    luecken("Ein Rechteck ist 6 cm lang und 4 cm hoch. Du legst es mit Quadraten von 1 cm² aus: Es werden ① Reihen mit je ② Quadraten. Fläche: ③ cm².", K(3), [4, 6, 24], ["4", "6", "4 * 6"],
            "Wie viele Quadrate passen in eine Reihe, wie viele Reihen übereinander?", "4 Reihen mit je 6 Quadraten: 4 · 6 = 24 cm²."),
    ["4", "6", "6+6+6+6"], {2: [(20, "fb.auslegen.umfang_statt_flaeche", "den Umfang berechnet"), (10, None, "Länge und Höhe zusammengezählt")]})
neu(f, "einheiten", 4, 1, "direkt", GR, "nein",
    luecken("1 m² = ① dm², also 3 m² = ② dm². Und 500 mm² = ③ cm².", K(3), [100, 300, 5], ["10 * 10", "3 * 100", "500 // 100"],
            "Bei Flächen ist die Umrechnungszahl 100.", "1 m² = 100 dm². 3 m² = 300 dm². 500 mm² = 5 cm²."),
    ["100", "300", "5"], {0: [(10, "fb.groesse.flaeche_mit_zehn", "Umrechnungszahl der Längen genommen")], 1: [(30, "fb.groesse.flaeche_mit_zehn", "mit 10 umgerechnet")], 2: [(50, "fb.groesse.flaeche_mit_zehn", "durch 10 geteilt"), (50000, "fb.groesse.falsche_richtung", "malgenommen statt geteilt")]})
neu(f, "einheitsquadrate", 12, 1, "erkennen", AUS, "ja",
    wahl("Ein Rechteck ist 5 cm lang und 3 cm breit. Pia rechnet 5 + 3 + 5 + 3 = 16 und sagt: „Die Fläche ist 16 cm².“ Was ist falsch?",
         ["Nichts.", "Sie hat sich verrechnet: Es sind 18 cm².", "Sie hat den Umfang berechnet. Die Fläche ist 15 cm².", "Die Fläche ist 8 cm²."], 2,
         "Was misst man, wenn man alle Seiten zusammenzählt?", "Alle Seiten zusammen sind der Umfang: 16 cm. Die Fläche ist 5 · 3 = 15 cm²."),
    lambda: 5 * 3 == 15 and 2 * 5 + 2 * 3 == 16, {0: ("fb.auslegen.umfang_statt_flaeche", "den Fehler nicht bemerkt"), 1: (None, "nicht nachgerechnet"), 3: (None, "nur zwei Seiten zusammengezählt")})
neu(f, "einheiten", 13, 1, "erkennen", GR, "ja",
    wahl("Warum ist die Umrechnungszahl bei Flächen 100 und nicht 10?",
         ["Weil Flächen größer sind als Längen.", "Weil 1 m = 100 cm ist.", "Weil in ein Quadrat mit 1 dm Seitenlänge 10 Reihen mit je 10 Quadraten von 1 cm² passen.", "Das ist nur eine Abmachung."], 2,
         "Lege in Gedanken ein Quadrat von 1 dm² mit Zentimeter-Quadraten aus.", "1 dm = 10 cm. In das Quadrat passen 10 Reihen mit je 10 Quadraten: 100 cm²."),
    lambda: 10 * 10 == 100, {0: (None, "kein Grund"), 1: (None, "Längen-Umrechnung m in cm, nicht der Grund für Flächen"), 3: (None, "es lässt sich begründen")})
neu(f, "sachaufgaben", 13, 1, "erkennen", AUS, "ja",
    wahl("Für welche Aufgabe brauchst du den Umfang?", ["Rasen für einen Garten säen", "Einen Zaun um den Garten bauen", "Farbe für eine Wand kaufen", "Fliesen für den Boden zählen"], 1,
         "Geht es um den Rand oder um das, was innen liegt?", "Der Zaun läuft außen um den Garten herum: Umfang. Rasen, Farbe und Fliesen bedecken eine Fläche."),
    lambda: True, {0: ("fb.auslegen.umfang_statt_flaeche", "Fläche und Umfang verwechselt"), 2: ("fb.auslegen.umfang_statt_flaeche", "Fläche und Umfang verwechselt"), 3: ("fb.auslegen.umfang_statt_flaeche", "Fläche und Umfang verwechselt")})
neu(f, "rechteck", 17, 2, "umkehr", RE, "ja",
    zahl("Ein Rechteck hat die Fläche 48 cm² und ist 8 cm lang. Wie groß ist sein Umfang?", 28, "2 * 8 + 2 * (48 // 8)",
         "Berechne zuerst die Breite.", "Breite: 48 : 8 = 6 cm. Umfang: 2 · 8 + 2 · 6 = 28 cm.", einheit="cm"),
    ["2*(8+6)"], [(6, None, "nur die Breite genannt"), (14, None, "nur Länge plus Breite"), (112, None, "2 · 8 + 2 · 48 gerechnet")])
neu(f, "kommaschreibweise", "B", 2, "darstellung", SW, "ja",
    zahl("Schreibe 4 m² 6 dm² als Kommazahl in m².", 4.06, "4 + 6 / 100",
         "Bei Flächen bekommt jede kleinere Einheit zwei Stellen.", "6 dm² = 0,06 m². Also 4,06 m².", einheit="m²"),
    ["406/100"], [(4.6, "fb.stellenwert.eine_stelle_daneben", "nur eine Stelle für die dm²"), (4.006, "fb.stellenwert.eine_stelle_daneben", "drei Stellen für die dm²")])
neu(f, "kommaschreibweise", "B", 2, "umkehr", SW, "ja",
    luecken("2,35 a = 2 a ① m². Und 0,08 m² = ② dm².", K(2), [35, 8], ["(2.35 - 2) * 100", "0.08 * 100"],
            "Die zwei Stellen hinter dem Komma gehören zur nächstkleineren Einheit.", "2,35 a = 2 a 35 m². 0,08 m² = 8 dm²."),
    ["235-200", "8"], {0: [(350, None, "mit 1 000 gerechnet")], 1: [(80, "fb.stellenwert.eine_stelle_daneben", "eine Stelle daneben")]})
neu(f, "zerlegen", 14, 2, "mehrschritt", RE, "ja",
    luecken("Aus einem Rechteck von 8 m mal 6 m wird an einer Ecke ein Rechteck von 3 m mal 2 m herausgeschnitten. Weg A (ergänzen und abziehen): 48 m² − ① m² = ② m². Weg B (zerlegen): 8 m · 4 m + 5 m · 2 m.", K(2), [6, 42], ["3 * 2", "8 * 6 - 3 * 2"],
            "Beide Wege müssen dieselbe Fläche ergeben.", "Herausgeschnitten: 3 · 2 = 6 m². 48 − 6 = 42 m². Weg B: 32 + 10 = 42 m²."),
    ["6", "8*4+5*2"], {1: [(54, None, "dazugezählt statt abgezogen")]})
neu(f, "sachaufgaben", "A", 2, "einkleidung", RE, "ja",
    zahl("Ein Zimmer ist 5 m lang und 3,5 m breit. Ringsum kommt eine Fußleiste, nur an der 1 m breiten Tür nicht. Wie viele Meter Leiste braucht man?", 16, "2 * 5 + 2 * 3.5 - 1",
         "Die Leiste läuft am Rand entlang.", "Umfang: 2 · 5 m + 2 · 3,5 m = 17 m. Ohne die Tür: 16 m.", einheit="m"),
    ["10+7-1"], [(17, None, "die Tür nicht abgezogen"), (17.5, None, "die Fläche statt des Umfangs berechnet"), (7.5, None, "nur zwei Seiten gerechnet")])
neu(f, "sachaufgaben", "A", 2, "mehrschritt", RE, "ja",
    zahl("Eine Wand ist 5 m lang und 2,4 m hoch. Ein Eimer Farbe reicht für 6 m². Wie viele Eimer braucht man?", 2, "5 * 2.4 / 6",
         "Berechne erst die Fläche der Wand.", "5 m · 2,4 m = 12 m². 12 : 6 = 2 Eimer."),
    ["12/6"], [(12, None, "die Fläche statt der Eimer genannt"), (72, "fb.verhaeltnis.falsche_richtung", "12 · 6 gerechnet")])
neu(f, "rechteck", 17, 3, "rueckwaerts", RE, "ja",
    zahl("Ein Quadrat hat den Umfang 36 cm. Wie groß ist seine Fläche?", 81, "(36 // 4) ** 2",
         "Wie lang ist eine Seite?", "Eine Seite: 36 : 4 = 9 cm. Fläche: 9 · 9 = 81 cm².", einheit="cm²"),
    ["9*9"], [(9, None, "nur die Seitenlänge genannt"), (1296, None, "36 · 36 gerechnet"), (18, "fb.potenz.basis_mal_hochzahl", "9 · 2 statt 9 · 9")])
neu(f, "zerlegen", 12, 3, "fehler", RE, "ja",
    zahl("Ein Bilderrahmen ist außen 10 cm mal 8 cm groß. Innen ist ein Rechteck von 6 cm mal 4 cm ausgeschnitten. Tim rechnet 10 · 8 + 6 · 4. Wie viele cm² hat der Rahmen wirklich?", 56, "10 * 8 - 6 * 4",
         "Gehört das Loch zum Rahmen?", "Das ausgeschnittene Stück wird abgezogen: 80 − 24 = 56 cm².", einheit="cm²"),
    ["80-24"], [(104, None, "wie Tim dazugezählt statt abgezogen"), (24, None, "nur das Loch berechnet")])
neu(f, "verstehen", "B", 3, "verknuepfen", RE, "ja",
    zahl("Zwei Rechtecke haben beide den Umfang 20 cm. Das eine ist 9 cm lang, das andere 5 cm. Um wie viele cm² unterscheiden sich ihre Flächen?", 16, "5 * 5 - 9 * 1",
         "Berechne zu jeder Länge erst die Breite.", "Länge plus Breite ist 10 cm. Erstes: 9 · 1 = 9 cm². Zweites: 5 · 5 = 25 cm². Unterschied: 16 cm².", einheit="cm²"),
    ["25-9"], [(0, None, "gleicher Umfang, also gleiche Fläche angenommen"), (4, None, "nur die Längen verglichen")])
neu(f, "verstehen", 12, 3, "begruenden", RE, "ja",
    wahl("Bei einem Rechteck werden die Länge und die Breite beide verdoppelt. Lars sagt: „Dann ist auch die Fläche doppelt so groß.“ Was stimmt?",
         ["Lars hat recht.", "Die Fläche wird viermal so groß, denn 2a · 2b = 4 · a · b.", "Die Fläche bleibt gleich.", "Die Fläche wird achtmal so groß."], 1,
         "Probiere es mit einem Rechteck von 3 cm mal 2 cm.", "3 · 2 = 6 cm². Verdoppelt: 6 · 4 = 24 cm². Das ist das Vierfache."),
    lambda: (2 * 3) * (2 * 2) == 4 * (3 * 2), {0: ("fb.aehnlich.flaeche_mit_k", "die Fläche wie die Länge wachsen lassen"), 2: (None, "nicht gerechnet"), 3: (None, "mit dem Rauminhalt verwechselt")})
neu(f, "rechteck", "V", 1, "direkt", RE, "ja",
    bed("Nenne Länge und Breite (ganze Zentimeter) eines Rechtecks mit der Fläche 36 cm², das kein Quadrat ist.", [G, G],
        [("beide Seiten größer als 0", [">", ["min", "$alle"], 0], ["min", "$alle"], "Deine kürzere Seite ist {} cm."), ("kein Quadrat", ["verschieden", "$alle"], None, "Dein Rechteck ist ein Quadrat."),
         ("Fläche 36 cm²", ["=", ["produkt", "$alle"], 36], ["produkt", "$alle"], "Dein Rechteck hat {} cm².")],
        [9, 4], [([-6, -6], "beide Seiten größer als 0"), ([6, 6], "kein Quadrat"), ([9, 5], "Fläche 36 cm²")],
        "Länge mal Breite soll 36 ergeben.", "Zum Beispiel 9 cm mal 4 cm, 12 cm mal 3 cm oder 18 cm mal 2 cm.", gut=[[36, 1], [3, 12]]), None, None)
neu(f, "einheiten", "V", 2, "umkehr", GR, "ja",
    bed("Nenne eine Fläche in ganzen dm², die größer als 2,5 m² und kleiner als 2,6 m² ist.", [G],
        [("größer als 2,5 m²", [">", "$1", 250], "$1", "Deine Fläche ist {} dm²."), ("kleiner als 2,6 m²", ["<", "$1", 260], "$1", "Deine Fläche ist {} dm².")],
        [255], [([25], "größer als 2,5 m²"), ([260], "kleiner als 2,6 m²"), ([2550], "kleiner als 2,6 m²"), ([250], "größer als 2,5 m²")],
        "Rechne beide Grenzen in dm² um.", "2,5 m² = 250 dm² und 2,6 m² = 260 dm². Es passt jede Zahl von 251 bis 259.", gut=[[251], [259]]), None, None)
neu(f, "verstehen", "V", 2, "umkehr", RE, "ja",
    bed("Nenne Länge und Breite (ganze Zentimeter) eines Rechtecks mit dem Umfang 24 cm und einer Fläche von weniger als 30 cm².", [G, G],
        [("beide Seiten größer als 0", [">", ["min", "$alle"], 0], ["min", "$alle"], "Deine kürzere Seite ist {} cm."), ("Umfang 24 cm", ["=", ["*", 2, ["summe", "$alle"]], 24], ["*", 2, ["summe", "$alle"]], "Dein Rechteck hat den Umfang {} cm."),
         ("Fläche weniger als 30 cm²", ["<", ["produkt", "$alle"], 30], ["produkt", "$alle"], "Dein Rechteck hat {} cm².")],
        [10, 2], [([0, 12], "beide Seiten größer als 0"), ([10, 3], "Umfang 24 cm"), ([6, 6], "Fläche weniger als 30 cm²"), ([8, 4], "Fläche weniger als 30 cm²")],
        "Länge plus Breite ist der halbe Umfang.", "Länge plus Breite ist 12 cm. Schmale Rechtecke haben wenig Fläche: 10 · 2 = 20 cm², 9 · 3 = 27 cm², 11 · 1 = 11 cm².", gut=[[11, 1], [3, 9]]), None, None)
rest = ["-", 60, ["*", "$1", "$2"]]
neu(f, "zerlegen", "V", 3, "parameter", RE, "ja",
    bed("Aus einem Rechteck von 10 cm mal 6 cm wird an einer Ecke ein kleineres Rechteck herausgeschnitten (ganze Zentimeter). Übrig bleiben genau 48 cm². Nenne Länge und Breite des herausgeschnittenen Stücks.", [G, G],
        [("Stück passt in die Ecke", UND([">=", "$1", 1], ["<", "$1", 10], [">=", "$2", 1], ["<", "$2", 6]), None, "Dein Stück passt nicht in die Ecke: Länge 1 bis 9 cm, Breite 1 bis 5 cm."),
         ("übrig bleiben 48 cm²", ["=", rest, 48], rest, "Bei dir bleiben {} cm² übrig.")],
        [4, 3], [([12, 1], "Stück passt in die Ecke"), ([2, 6], "Stück passt in die Ecke"), ([5, 2], "übrig bleiben 48 cm²")],
        "Wie groß ist die ganze Fläche? Wie viel muss also weg?", "Das ganze Rechteck hat 60 cm². Es müssen 12 cm² weg: 4 cm mal 3 cm, 6 cm mal 2 cm oder 3 cm mal 4 cm.", gut=[[6, 2], [3, 4]]), None, None)
neu(f, "verstehen", "V", 3, "transfer", RE, "ja",
    bed("Nenne zwei Rechtecke (ganze Zentimeter) mit gleicher Fläche, aber verschiedenem Umfang. Reihenfolge der Felder: Länge und Breite des ersten, Länge und Breite des zweiten.", [G, G, G, G],
        [("alle Seiten größer als 0", [">", ["min", "$alle"], 0], ["min", "$alle"], "Deine kürzeste Seite ist {} cm."),
         ("gleiche Fläche", ["=", ["*", "$1", "$2"], ["*", "$3", "$4"]], ["*", "$1", "$2"], "Dein erstes Rechteck hat {} cm², das zweite nicht."),
         ("verschiedener Umfang", ["!=", ["+", "$1", "$2"], ["+", "$3", "$4"]], ["*", 2, ["+", "$1", "$2"]], "Beide Rechtecke haben bei dir den Umfang {} cm.")],
        [6, 2, 4, 3], [([0, 5, 0, 3], "alle Seiten größer als 0"), ([6, 2, 4, 4], "gleiche Fläche"), ([6, 2, 2, 6], "verschiedener Umfang")],
        "Suche zwei verschiedene Malaufgaben mit demselben Ergebnis.", "Zum Beispiel 6 · 2 = 12 und 4 · 3 = 12. Umfang: 16 cm und 14 cm.", gut=[[12, 1, 3, 4]]), None, None)

# ═════════════════════ Kind 1 · Flug g2 · Dreisatz Teil 1 (fünf Lernkarten) ═════════════════════
f = "g2"
neu(f, "einheit", 4, 1, "direkt", WERT, "nein",
    luecken("5 Äpfel kosten 2 €. Rechne in Cent: 200 Cent : ① = ② Cent für einen Apfel.", K(2), [5, 40], ["5", "200 // 5"],
            "Wert durch Anzahl ergibt den Preis für 1 Stück.", "200 Cent : 5 = 40 Cent."),
    ["5", "2*100/5"], {1: [(1000, "fb.verhaeltnis.falsche_richtung", "200 · 5 gerechnet"), (195, None, "abgezogen statt geteilt")]})
neu(f, "dreisatz", 12, 1, "erkennen", VERH, "ja",
    wahl("3 Hefte kosten 4,50 €. Gesucht ist der Preis für 5 Hefte. Emil rechnet: 4,50 € + 2 € = 6,50 €. Was ist falsch?",
         ["Er zählt für 2 Hefte einfach 2 € dazu, statt erst den Preis für 1 Heft zu berechnen.", "Er müsste 4,50 € · 5 rechnen.", "Nichts.", "Er müsste 4,50 € − 2 € rechnen."], 0,
         "Was kostet 1 Heft?", "1 Heft kostet 4,50 € : 3 = 1,50 €. 5 Hefte kosten 5 · 1,50 € = 7,50 €."),
    lambda: F(450, 3) * 5 == 750, {1: (None, "das wäre der Preis für 15 Hefte"), 2: ("fb.verhaeltnis.addiert_statt_malgenommen", "den Fehler nicht bemerkt"), 3: (None, "5 Hefte kosten mehr als 3")})
neu(f, "sach", 13, 1, "erkennen", WERT, "ja",
    wahl("Bei welcher Aufgabe darfst du mit dem Dreisatz rechnen?",
         ["3 kg Kartoffeln kosten 4,50 €. Was kosten 5 kg?", "Ein Kind ist mit 6 Jahren 1,20 m groß. Wie groß ist es mit 12 Jahren?", "Ein Lied dauert 3 Minuten, wenn ein Kind es singt. Wie lange dauert es, wenn 4 Kinder es zusammen singen?"], 0,
         "Prüfe: doppelte Menge, doppelter Wert?", "Doppelt so viele Kartoffeln kosten doppelt so viel. Größe und Liedlänge verdoppeln sich nicht."),
    lambda: True, {1: (None, "Wachstum ist nicht proportional"), 2: (None, "die Dauer hängt nicht von der Zahl der Kinder ab")})
neu(f, "geschickt", 13, 1, "erkennen", VERH, "ja",
    wahl("12 Flaschen kosten 18 €. Gesucht ist der Preis für 8 Flaschen. Welche Zwischenmenge ist geschickt?", ["5 Flaschen", "10 Flaschen", "7 Flaschen", "4 Flaschen"], 3,
         "Die Zwischenmenge soll in 12 und in 8 passen.", "4 passt in beide: 12 : 3 = 4 und 4 · 2 = 8. Also 18 € : 3 = 6 €, dann 6 € · 2 = 12 €."),
    lambda: 12 % 4 == 0 and 8 % 4 == 0 and all(12 % n or 8 % n for n in (5, 10, 7)), {0: (None, "passt in keine der beiden Zahlen"), 1: (None, "passt in keine der beiden Zahlen"), 2: (None, "passt in keine der beiden Zahlen")})
neu(f, "dreisatz", 4, 2, "mehrschritt", VERH, "nein",
    luecken("4 Brötchen kosten 2,40 €. Wie viel kosten 7? Erst auf 1 Brötchen: 240 Cent : 4 = ① Cent. Dann auf 7 Brötchen: ① Cent · 7 = ② Cent.", K(2), [60, 420], ["240 // 4", "240 // 4 * 7"],
            "Erst auf 1 Stück schließen, dann auf das Gesuchte.", "240 : 4 = 60 Cent. 60 · 7 = 420 Cent = 4,20 €."),
    ["60", "7*240/4"], {1: [(540, "fb.verhaeltnis.addiert_statt_malgenommen", "3 Brötchen mehr, also 3 € mehr")]})
neu(f, "dreisatz", "B", 2, "darstellung", VERH, "ja",
    luecken("Ergänze die Dreisatz-Tabelle. Die Preise stehen in Cent.", K(2), [150, 750], ["1200 // 8", "1200 // 8 * 5"],
            "Was du oben tust, tust du auch unten.", "Geteilt durch 8: 1 200 : 8 = 150 Cent. Mal 5: 150 · 5 = 750 Cent.", "Je Lücke ein Preis in Cent.",
            grafik=TAB(["Karten", "8", "1", "5"], ["Preis (Cent)", "1200", "①", "②"])),
    ["150", "5*1200/8"], {0: [(1193, "fb.verhaeltnis.addiert_statt_malgenommen", "7 abgezogen statt durch 8 geteilt")], 1: [(1197, "fb.verhaeltnis.addiert_statt_malgenommen", "3 Karten weniger, also 3 Cent weniger")]})
neu(f, "geschickt", 14, 2, "mehrschritt", VERH, "ja",
    luecken("6 kg kosten 15 €. Gesucht ist der Preis für 9 kg. Weg A über 1 kg: 15 € : 6 = 2,50 €, dann mal 9. Weg B über 3 kg: 3 kg kosten ① Cent, 9 kg kosten ② Cent.", K(2), [750, 2250], ["1500 // 2", "1500 // 2 * 3"],
            "Von 6 nach 3 teilst du durch 2. Von 3 nach 9 nimmst du mal 3.", "3 kg: 15 € : 2 = 7,50 €. 9 kg: 7,50 € · 3 = 22,50 €. Weg A: 2,50 € · 9 = 22,50 €.", "Je Lücke ein Preis in Cent."),
    ["750", "9*250"], {1: [(1800, "fb.verhaeltnis.addiert_statt_malgenommen", "3 kg mehr, also 3 € mehr")]})
neu(f, "einheit", 17, 2, "umkehr", WERT, "ja",
    zahl("Ein Stift kostet 0,80 €. Für wie viele Stifte reichen 12 €?", 15, "1200 // 80",
         "Rechne in Cent. Wie oft passt der Preis für 1 Stift in 12 €?", "1 200 Cent : 80 Cent = 15 Stifte."),
    ["12*10/8"], [(9.6, "fb.verhaeltnis.falsche_richtung", "12 · 0,80 gerechnet"), (150, "fb.stellenwert.eine_stelle_daneben", "0,80 € als 8 Cent")])
neu(f, "einheit", "B", 2, "mehrschritt", WERT, "ja",
    wahl("Packung A: 6 Riegel für 2,40 €. Packung B: 10 Riegel für 3,50 €. Bei welcher Packung ist ein Riegel billiger, und um wie viel?",
         ["bei A, um 5 Cent", "bei B, um 5 Cent", "bei A, um 1,10 €", "bei beiden gleich"], 1,
         "Berechne für jede Packung den Preis für 1 Riegel.", "A: 240 Cent : 6 = 40 Cent. B: 350 Cent : 10 = 35 Cent. Bei B ist ein Riegel 5 Cent billiger."),
    lambda: F(240, 6) - F(350, 10) == 5, {0: (None, "die Packungen vertauscht"), 2: (None, "die Packungspreise statt der Stückpreise verglichen"), 3: (None, "nicht gerechnet")})
neu(f, "dreisatz", 17, 2, "umkehr", VERH, "ja",
    zahl("5 Liter Saft kosten 8 €. Wie viele Liter bekommt man für 20 €?", 12.5, "20 * 5 / 8",
         "Wie viele Liter bekommt man für 1 €? Oder: Wievielmal so viel Geld ist es?", "20 € sind 2,5-mal so viel wie 8 €. Also 2,5 · 5 Liter = 12,5 Liter.", einheit="Liter"),
    ["100/8"], [(32, "fb.verhaeltnis.falsche_richtung", "den Preis für 20 Liter berechnet"), (17, "fb.verhaeltnis.addiert_statt_malgenommen", "12 € mehr, also 12 Liter mehr")])
neu(f, "sach", 12, 2, "einkleidung", WERT, "ja",
    wahl("Ein Maler streicht eine Wand in 3 Stunden. Jule rechnet mit dem Dreisatz: „Dann brauchen 2 Maler 6 Stunden.“ Was stimmt?",
         ["Jule hat recht.", "Zwei Maler brauchen auch 3 Stunden.", "Jule darf den Dreisatz hier nicht nehmen: Mehr Maler brauchen weniger Zeit.", "Zwei Maler brauchen 5 Stunden."], 2,
         "Prüfe zuerst: Gehört zur doppelten Zahl der doppelte Wert?", "Mehr Maler sind schneller fertig. Die Zuordnung ist nicht proportional, also kein Dreisatz."),
    lambda: True, {0: (None, "Proportionalität ungeprüft angenommen"), 1: (None, "zwei arbeiten schneller als einer"), 3: (None, "geraten")})
neu(f, "aenderung", 17, 2, "umkehr", VERH, "ja",
    zahl("Ein Becken verliert gleichmäßig 3 Liter Wasser pro Stunde. Jetzt sind 50 Liter darin. Nach wie vielen Stunden sind es noch 32 Liter?", 6, "(50 - 32) // 3",
         "Wie viele Liter müssen abfließen?", "Es fließen 50 − 32 = 18 Liter ab. 18 : 3 = 6 Stunden.", einheit="h"),
    ["18/3"], [(54, "fb.verhaeltnis.falsche_richtung", "18 · 3 gerechnet"), (15, None, "18 − 3 gerechnet")])
neu(f, "geschickt", 17, 2, "umkehr", VERH, "ja",
    zahl("15 Hefte kosten 9 €. Wie viele Hefte bekommt man für 6 €?", 10, "15 * 6 // 9",
         "Suche einen Zwischenbetrag, der in 9 € und in 6 € passt.", "Für 3 € gibt es 15 : 3 = 5 Hefte. Für 6 € gibt es 2 · 5 = 10 Hefte."),
    ["5*2"], [(3.6, "fb.verhaeltnis.falsche_richtung", "den Preis für 6 Hefte berechnet"), (12, "fb.verhaeltnis.addiert_statt_malgenommen", "3 € weniger, also 3 Hefte weniger")])
neu(f, "aenderung", 12, 3, "fehler", PM, "ja",
    zahl("Die Temperatur fällt in 5 Stunden gleichmäßig von 12 °C auf 2 °C. Nico gibt als Änderungsrate „2 °C pro Stunde“ an. Wie lautet die Änderungsrate richtig? Gib die Zahl mit Vorzeichen an.", -2, "(2 - 12) // 5",
         "Nimmt die Größe zu oder ab?", "Änderung: 2 − 12 = −10 °C. Geteilt durch 5 Stunden: −2 °C pro Stunde. Das Minus zeigt: Es wird kälter."),
    ["(0-10)/5"], [(2, "fb.plusminus.zeichen_des_ergebnisses", "wie Nico ohne Minus"), (-10, None, "die ganze Änderung statt der Rate")])
neu(f, "sach", "A", 3, "verknuepfen", VERH, "ja",
    zahl("Für 4 Personen braucht ein Rezept 300 g Mehl. Im Schrank ist 1 kg Mehl. Für wie viele Personen reicht das höchstens?", 13, "1000 // (300 // 4)",
         "Wie viel Mehl braucht eine Person? Rechne das Kilogramm in Gramm um.", "Eine Person: 300 g : 4 = 75 g. 1 000 g : 75 g = 13, Rest 25 g. Es reicht für 13 Personen."),
    ["(1000-25)/75"], [(14, None, "aufgerundet, obwohl das Mehl nicht reicht"), (12, None, "nur ganze Rezepte gezählt: 3 · 4")])
je = ["/", "$2", "$1"]
neu(f, "einheit", "V", 1, "direkt", WERT, "ja",
    bed("Ein Stück kostet zwischen 30 und 40 Cent. Nenne eine Stückzahl größer als 1 und einen passenden Gesamtpreis in Cent.", [G, G],
        [("mehr als 1 Stück", [">", "$1", 1], "$1", "Deine Stückzahl ist {}."), ("Stückpreis zwischen 30 und 40 Cent", UND([">=", "$2", ["*", 30, "$1"]], ["<=", "$2", ["*", 40, "$1"]]), je, "Bei dir kostet ein Stück {} Cent.")],
        [4, 140], [([1, 35], "mehr als 1 Stück"), ([4, 200], "Stückpreis zwischen 30 und 40 Cent"), ([5, 100], "Stückpreis zwischen 30 und 40 Cent")],
        "Gesamtpreis durch Stückzahl ergibt den Preis für 1 Stück.", "Zum Beispiel 4 Stück für 140 Cent: 140 : 4 = 35 Cent je Stück.", gut=[[2, 60], [10, 400]]), None, None)
neu(f, "dreisatz", "V", 2, "umkehr", VERH, "ja",
    bed("4 kg Äpfel kosten 10 €. Nenne eine andere Menge in kg und ihren Preis in Euro. Der Preis soll keine ganze Zahl sein.", [R, R],
        [("andere Menge, größer als 0", UND([">", "$1", 0], ["!=", "$1", 4]), "$1", "Deine Menge ist {} kg."), ("Preis passt zur Menge", ["=", ["*", 4, "$2"], ["*", 10, "$1"]], je, "Bei dir kostet 1 kg {} €."),
         ("Preis ist keine ganze Zahl", ["nicht", ["ganzzahlig", "$2"]], "$2", "Dein Preis ist {} € – das ist eine ganze Zahl.")],
        [3, "7,5"], [([4, 10], "andere Menge, größer als 0"), ([3, 7], "Preis passt zur Menge"), ([2, 5], "Preis ist keine ganze Zahl")],
        "Was kostet 1 kg?", "1 kg kostet 2,50 €. Zum Beispiel 3 kg für 7,50 € oder 1 kg für 2,50 €.", gut=[[1, "2,5"], [5, "12,5"]]), None, None)
passt = ["/", ["*", 6, "$1"], 9]
neu(f, "geschickt", "V", 2, "umkehr", VERH, "ja",
    bed("9 Hefte kosten 6 €. Nenne eine Stückzahl zwischen 10 und 30, deren Preis ein ganzer Euro-Betrag ist, und diesen Preis.", [G, G],
        [("Stückzahl zwischen 10 und 30", UND([">=", "$1", 10], ["<=", "$1", 30]), "$1", "Deine Stückzahl ist {}."), ("Preis passt zur Stückzahl", ["=", ["*", 9, "$2"], ["*", 6, "$1"]], passt, "Zu deiner Stückzahl gehört der Preis {} €.")],
        [12, 8], [([9, 6], "Stückzahl zwischen 10 und 30"), ([12, 9], "Preis passt zur Stückzahl"), ([10, 7], "Preis passt zur Stückzahl")],
        "3 Hefte kosten 2 €. Welche Stückzahlen lassen sich aus Dreier-Päckchen bauen?", "3 Hefte kosten 2 €. Jede durch 3 teilbare Stückzahl passt: 12 Hefte für 8 €, 15 für 10 €, 30 für 20 €.", gut=[[15, 10], [30, 20]]), None, None)
rate = ["/", ["-", "$2", "$1"], "$3"]
neu(f, "aenderung", "V", 3, "parameter", VERH, "ja",
    bed("Eine Größe ändert sich gleichmäßig. Nenne Startwert, Endwert und Zeitspanne in Stunden so, dass die Änderungsrate genau −4 pro Stunde ist. Die Zeitspanne soll größer als 1 sein.", [G, G, G],
        [("Zeitspanne größer als 1", [">", "$3", 1], "$3", "Deine Zeitspanne ist {} Stunden."), ("Änderungsrate ist −4", ["=", ["-", "$2", "$1"], ["*", -4, "$3"]], rate, "Deine Änderungsrate ist {} pro Stunde.")],
        [20, 8, 3], [([20, 16, 1], "Zeitspanne größer als 1"), ([8, 20, 3], "Änderungsrate ist −4"), ([20, 8, 4], "Änderungsrate ist −4")],
        "Änderungsrate ist Änderung geteilt durch Zeitspanne.", "In 3 Stunden muss die Größe um 12 abnehmen, zum Beispiel von 20 auf 8.", gut=[[0, -8, 2], [100, 60, 10]]), None, None)
bleibt = ["/", ["-", 1000, ["*", 120, "$1"]], 100]
neu(f, "sach", "V", 3, "verknuepfen", VERH, "ja",
    bed("3 Kugeln Eis kosten 3,60 €. Du hast 10 €. Nenne eine Zahl von Kugeln, nach deren Kauf dir mehr als 2 €, aber weniger als 5 € bleiben.", [G],
        [("mindestens 1 Kugel", [">=", "$1", 1], "$1", "Deine Zahl ist {}."), ("es bleiben mehr als 2 €", [">", bleibt, 2], bleibt, "Dir bleiben {} €."), ("es bleiben weniger als 5 €", ["<", bleibt, 5], bleibt, "Dir bleiben {} €.")],
        [5], [([0], "mindestens 1 Kugel"), ([7], "es bleiben mehr als 2 €"), ([4], "es bleiben weniger als 5 €")],
        "Was kostet eine Kugel?", "Eine Kugel kostet 1,20 €. 5 Kugeln kosten 6 €, es bleiben 4 €. Auch 6 Kugeln passen (es bleiben 2,80 €).", gut=[[6]]), None, None)

# ═════════════════════ Kind 2 · Flug ge4 · Dreiecke, Vierecke und Konstruktion (16 Lernkarten) ═════════════════════
f = "ge4"
neu(f, "scheitel_neben", 4, 1, "direkt", WINK, "nein",
    luecken("Zwei Geraden schneiden sich. α = 48°. Der Scheitelwinkel von α hat ①°. Jeder Nebenwinkel von α hat ②°.", K(2), [48, 132], ["48", "180 - 48"],
            "Scheitelwinkel sind gleich groß. Nebenwinkel ergeben zusammen 180°.", "Scheitelwinkel: 48°. Nebenwinkel: 180° − 48° = 132°."),
    ["48", "132"], {1: [(48, "fb.winkel.neben_statt_scheitel", "Nebenwinkel wie Scheitelwinkel behandelt"), (42, None, "auf 90° ergänzt")]})
neu(f, "stufen_wechsel", "B", 1, "direkt", WINK, "ja",
    luecken("g ∥ h. Bei S ist der Winkel rechts oberhalb 70° groß. Wie groß ist sein Stufenwinkel bei T, und wie groß ist der Winkel bei T links oberhalb?", "Stufenwinkel: □°; links oberhalb: □°", [70, 110], ["70", "180 - 70"],
            "Der Stufenwinkel liegt bei T an derselben Stelle wie bei S.", "Stufenwinkel an Parallelen sind gleich: 70°. Der Winkel daneben ist sein Nebenwinkel: 110°.", "Je Lücke ein Winkel in Grad.",
            grafik=par(70, [("S", "RO", "70°"), ("T", "RO", "?"), ("T", "LO", "?")])),
    ["70", "110"], {0: [(110, "fb.winkel.neben_statt_scheitel", "den Nebenwinkel als Stufenwinkel genannt")], 1: [(70, "fb.winkel.neben_statt_scheitel", "Nebenwinkel für gleich groß gehalten")]})
neu(f, "parallel_pruefen", 13, 1, "erkennen", WINK, "ja",
    wahl("Eine Gerade schneidet g unter 64°. Der Stufenwinkel dazu an der Geraden h hat 66°. Was folgt?",
         ["g und h sind parallel.", "g und h sind nicht parallel.", "g und h stehen senkrecht aufeinander.", "Dazu lässt sich nichts sagen."], 1,
         "Was gilt für Stufenwinkel an Parallelen?", "An Parallelen sind Stufenwinkel gleich groß. 64° und 66° sind verschieden, also sind g und h nicht parallel."),
    lambda: 64 != 66, {0: (None, "fast gleich für gleich genommen"), 2: (None, "kein rechter Winkel im Spiel"), 3: (None, "der Kehrsatz der Stufenwinkel entscheidet es")})
neu(f, "parkett", 13, 1, "erkennen", WINK, "ja",
    wahl("Mit welchen Fliesen allein kann man einen Boden NICHT lückenlos auslegen?",
         ["gleichseitige Dreiecke (Innenwinkel 60°)", "Quadrate (90°)", "regelmäßige Fünfecke (108°)", "regelmäßige Sechsecke (120°)"], 2,
         "An einer Ecke müssen die Winkel zusammen 360° ergeben.", "360° ist durch 60°, 90° und 120° teilbar, aber nicht durch 108°. Drei Fünfecke ergeben 324°, vier schon 432°."),
    lambda: 360 % 108 != 0 and all(360 % w == 0 for w in (60, 90, 120)), {0: (None, "6 · 60° = 360° passt"), 1: (None, "4 · 90° = 360° passt"), 3: (None, "3 · 120° = 360° passt")})
neu(f, "kongruenzsatz", 13, 1, "erkennen", DECK, "ja",
    wahl("Von einem Dreieck kennst du a = 5 cm, b = 7 cm und den Winkel γ zwischen diesen beiden Seiten. Welcher Kongruenzsatz sichert, dass das Dreieck eindeutig ist?", ["SSS", "SWS", "WSW", "SsW"], 1,
         "Wo liegt der Winkel: zwischen den Seiten oder einer Seite gegenüber?", "Zwei Seiten und der Winkel dazwischen: SWS."),
    lambda: True, {0: (None, "es sind nur zwei Seiten gegeben"), 2: (None, "es ist nur ein Winkel gegeben"), 3: (None, "bei SsW liegt der Winkel der größeren Seite gegenüber, nicht dazwischen")})
neu(f, "vierecke_konstruieren", "B", 1, "direkt", DECK, "ja",
    zahl("Ein Parallelogramm braucht 3 Bestimmungsstücke. Du kennst eine Seite und einen Winkel. Wie viele Stücke fehlen noch?", 1, "3 - 2",
         "Zähle, was du schon hast.", "Seite und Winkel sind 2 Stücke. Es fehlt 1, zum Beispiel die zweite Seite."),
    ["1"], [(3, None, "die Gesamtzahl genannt"), (2, None, "die vorhandenen Stücke genannt")])
neu(f, "innenwinkelsumme", 17, 2, "umkehr", WINK, "ja",
    zahl("In einem Dreieck ist β doppelt so groß wie α, und γ = 60°. Wie groß ist α?", 40, "(180 - 60) // 3",
         "α und β zusammen sind drei „α“.", "α + 2α + 60° = 180°, also 3α = 120° und α = 40°.", einheit="°"),
    ["120/3"], [(60, None, "120° durch 2 geteilt"), (80, None, "β statt α genannt")])
neu(f, "aussenwinkel", 14, 2, "mehrschritt", WINK, "ja",
    luecken("Dreieck mit α = 50° und β = 65°. Gesucht ist der Außenwinkel bei C. Weg A: γ = 180° − 50° − 65° = ①°, Außenwinkel = 180° − ①° = ②°. Weg B: 50° + 65°.", K(2), [65, 115], ["180 - 50 - 65", "180 - (180 - 50 - 65)"],
            "Der Außenwinkel ist so groß wie die beiden anderen Innenwinkel zusammen.", "γ = 65°. Außenwinkel: 180° − 65° = 115°. Weg B: 50° + 65° = 115°.", grafik=dreieck(50, 65)),
    ["65", "50+65"], {1: [(65, None, "den Innenwinkel statt des Außenwinkels genannt")]})
neu(f, "vieleck", 17, 2, "umkehr", WINK, "ja",
    zahl("Ein Vieleck hat die Winkelsumme 900°. Wie viele Ecken hat es?", 7, "900 // 180 + 2",
         "Die Winkelsumme ist (n − 2) · 180°. Rechne rückwärts.", "900° : 180° = 5. Das ist n − 2, also n = 7."),
    ["(900+360)/180"], [(5, None, "die 2 nicht dazugezählt"), (3, "fb.gegenrechnung.gleiche_rechnung", "noch einmal 2 abgezogen statt dazugezählt")])
neu(f, "parallel_pruefen", 17, 2, "umkehr", WINK, "ja",
    zahl("Eine Gerade schneidet g unter 115°. An der Geraden h wird der Nebenwinkel des zugehörigen Wechselwinkels gemessen. Wie groß muss er sein, damit g und h parallel sind?", 65, "180 - 115",
         "Wie groß muss der Wechselwinkel selbst sein?", "Bei Parallelen ist der Wechselwinkel auch 115°. Sein Nebenwinkel hat 180° − 115° = 65°.", einheit="°"),
    ["13*5"], [(115, "fb.winkel.neben_statt_scheitel", "den Wechselwinkel selbst genannt"), (245, None, "auf 360° ergänzt")])
neu(f, "gleichschenklig", 17, 2, "umkehr", WINK, "ja",
    zahl("In einem gleichschenkligen Dreieck hat ein Basiswinkel 72°. Wie groß ist der Winkel an der Spitze?", 36, "180 - 2 * 72",
         "Es gibt zwei gleich große Basiswinkel.", "Beide Basiswinkel zusammen: 144°. Spitze: 180° − 144° = 36°.", einheit="°"),
    ["180-144"], [(108, None, "nur einen Basiswinkel abgezogen"), (54, None, "72° als Spitzenwinkel genommen: (180 − 72) : 2")])
neu(f, "konstruierbar", 17, 2, "umkehr", DECK, "ja",
    zahl("Zwei Seiten eines Dreiecks sind 4 cm und 9 cm lang. Die dritte Seite ist eine ganze Zahl von Zentimetern. Wie lang muss sie mindestens sein?", 6, "9 - 4 + 1",
         "Die dritte Seite und die 4 cm müssen zusammen länger als 9 cm sein.", "4 cm + x muss größer als 9 cm sein, also x größer als 5 cm. Die kleinste ganze Zahl ist 6.", einheit="cm"),
    ["5+1"], [(5, "fb.gleichung_loesen.grenze_mitgezaehlt", "bei 5 cm liegt alles auf einer Linie: kein Dreieck"), (12, None, "die größte statt der kleinsten Länge genannt")], probe=lambda: 4 + 6 > 9 and not 4 + 5 > 9)
neu(f, "planfigur", 13, 2, "darstellung", DECK, "ja",
    wahl("Du konstruierst ein Dreieck aus c = 6 cm, α = 50° und b = 4 cm (SWS). Welche Reihenfolge führt zum Ziel?",
         ["c zeichnen; Kreis um A mit 4 cm; Kreis um B mit 6 cm", "α zeichnen; c irgendwo anlegen; b messen", "b zeichnen; α im Punkt C antragen; mit B verbinden", "c zeichnen; α im Punkt A antragen; auf dem freien Schenkel 4 cm abtragen; C mit B verbinden"], 3,
         "Beginne mit einer gegebenen Seite. Wo liegt der Winkel α?", "α liegt bei A zwischen c und b. Also: c zeichnen, α in A antragen, 4 cm abtragen ergibt C, dann C mit B verbinden."),
    lambda: True, {0: (None, "Konstruktion nach SSS, die dritte Seite ist aber nicht gegeben"), 1: (None, "ohne festen Anfang"), 2: (None, "α liegt bei A, nicht bei C")})
neu(f, "vierecke", 17, 2, "umkehr", WINK, "ja",
    zahl("In einem Parallelogramm ist ein Winkel um 30° größer als sein Nachbarwinkel. Wie groß ist der größere der beiden?", 105, "(180 + 30) // 2",
         "Benachbarte Winkel im Parallelogramm ergeben 180°.", "x + (x + 30°) = 180°, also x = 75°. Der größere hat 105°.", einheit="°"),
    ["75+30"], [(75, None, "den kleineren Winkel genannt"), (150, None, "180° − 30° nicht halbiert")])
neu(f, "aussenwinkel", 12, 3, "fehler", WINK, "ja",
    zahl("In einem Dreieck ist der Außenwinkel bei C 130° groß, und α = 55°. Mia rechnet: β = 180° − 130° = 50°. Wie groß ist β wirklich?", 75, "130 - 55",
         "Was hat Mia mit 180° − 130° wirklich berechnet?", "180° − 130° = 50° ist der Innenwinkel γ. Der Außenwinkel ist α + β, also β = 130° − 55° = 75°.", einheit="°"),
    ["180-55-50"], [(50, None, "wie Mia den Innenwinkel γ berechnet"), (185, None, "α dazugezählt statt abgezogen")])
neu(f, "figuren", 17, 3, "verknuepfen", WINK, "ja",
    zahl("g ∥ h. Die Gerade k schneidet g in S und h in T. Bei S ist der Winkel links oberhalb 125° groß. Eine zweite Gerade durch T bildet mit h rechts oberhalb von T den Winkel 30°. Wie groß ist der Winkel bei T zwischen dieser zweiten Geraden und k?", 25, "(180 - 125) - 30",
         "Bestimme zuerst den Winkel bei T rechts oberhalb zwischen h und k. Welcher Winkelsatz hilft?", "Bei S rechts oberhalb: 180° − 125° = 55° (Nebenwinkel). Bei T rechts oberhalb ebenfalls 55° (Stufenwinkel). Davon gehen 30° ab: 25°.", einheit="°",
         grafik=par(55, [("S", "LO", "125°")])),
    ["55-30"], [(95, None, "125° − 30° gerechnet: Nebenwinkel vergessen"), (85, None, "55° + 30° gerechnet"), (55, None, "die 30° nicht abgezogen")])
neu(f, "beweisen", 12, 3, "begruenden", WINK, "ja",
    wahl("Beweis der Winkelsumme im Dreieck: Durch C wird die Parallele zu AB gezeichnet. Welcher Satz begründet, dass der Winkel, der dort links neben γ liegt, so groß ist wie α?",
         ["Wechselwinkel an Parallelen sind gleich groß.", "Scheitelwinkel sind gleich groß.", "Nebenwinkel ergeben 180°.", "Die Winkelsumme im Dreieck ist 180°."], 0,
         "Welche zwei Geraden sind parallel, und welche Gerade schneidet beide?", "AB und die Gerade durch C sind parallel, AC schneidet beide. α und der Winkel bei C sind Wechselwinkel."),
    lambda: True, {1: (None, "die Winkel liegen nicht an derselben Kreuzung"), 2: (None, "die Winkel liegen nicht nebeneinander"), 3: (None, "Zirkelschluss: Das soll gerade bewiesen werden")})
neu(f, "satz_kehrsatz", 12, 3, "begruenden", DECK, "ja",
    wahl("Satz: „Wenn ein Viereck ein Quadrat ist, dann hat es vier rechte Winkel.“ Was gilt für den Kehrsatz?",
         ["Der Kehrsatz stimmt auch.", "Der Kehrsatz ist falsch: Ein Rechteck, das kein Quadrat ist, hat auch vier rechte Winkel.", "Der Kehrsatz ist falsch, weil ein Quadrat keine rechten Winkel hat.", "Der Kehrsatz lautet: „Wenn ein Viereck kein Quadrat ist, hat es keine rechten Winkel.“"], 1,
         "Vertausche Wenn und Dann. Suche dann ein Gegenbeispiel.", "Kehrsatz: „Wenn ein Viereck vier rechte Winkel hat, dann ist es ein Quadrat.“ Ein Rechteck mit 3 cm und 5 cm widerlegt ihn."),
    lambda: True, {0: (None, "kein Gegenbeispiel gesucht"), 2: (None, "falsche Aussage über das Quadrat"), 3: (None, "verneint statt vertauscht")})
neu(f, "innenwinkelsumme", "V", 1, "direkt", WINK, "ja",
    bed("Nenne die drei Innenwinkel eines stumpfwinkligen Dreiecks (ganze Grad).", [G, G, G],
        [("jeder Winkel größer als 0°", [">", ["min", "$alle"], 0], ["min", "$alle"], "Dein kleinster Winkel hat {}°."), ("Winkel eines Dreiecks", ["=", ["summe", "$alle"], 180], ["summe", "$alle"], "Deine Winkel ergeben zusammen {}°."),
         ("ein Winkel ist stumpf", [">", ["max", "$alle"], 90], ["max", "$alle"], "Dein größter Winkel hat {}°.")],
        [100, 50, 30], [([100, 90, -10], "jeder Winkel größer als 0°"), ([100, 50, 40], "Winkel eines Dreiecks"), ([60, 60, 60], "ein Winkel ist stumpf"), ([90, 45, 45], "ein Winkel ist stumpf")],
        "Wie groß ist die Winkelsumme im Dreieck? Was heißt stumpf?", "Zusammen 180°, einer größer als 90°. Zum Beispiel 100°, 50° und 30°.", gut=[[91, 88, 1]]), None, None)
neu(f, "gleichschenklig", "V", 2, "mehrschritt", WINK, "ja",
    bed("Nenne die drei Innenwinkel eines gleichschenkligen Dreiecks, das nicht gleichseitig ist. Alle Winkel sollen spitz und ganze Grad sein.", [G, G, G],
        [("alle Winkel spitz", UND([">", ["min", "$alle"], 0], ["<", ["max", "$alle"], 90]), ["max", "$alle"], "Dein größter Winkel hat {}°."), ("Winkel eines Dreiecks", ["=", ["summe", "$alle"], 180], ["summe", "$alle"], "Deine Winkel ergeben zusammen {}°."),
         ("gleichschenklig", ODER(["=", "$1", "$2"], ["=", "$2", "$3"], ["=", "$1", "$3"]), None, "Bei dir sind keine zwei Winkel gleich groß."),
         ("nicht gleichseitig", ["nicht", UND(["=", "$1", "$2"], ["=", "$2", "$3"])], None, "Dein Dreieck ist gleichseitig.")],
        [70, 70, 40], [([100, 40, 40], "alle Winkel spitz"), ([70, 70, 50], "Winkel eines Dreiecks"), ([50, 60, 70], "gleichschenklig"), ([60, 60, 60], "nicht gleichseitig")],
        "Welche Winkel sind im gleichschenkligen Dreieck gleich groß?", "Zwei Basiswinkel sind gleich, zum Beispiel 70° und 70°. Für die Spitze bleiben 40°.", gut=[[50, 80, 50], [89, 2, 89]]), None, None)
neu(f, "konstruierbar", "V", 2, "umkehr", DECK, "ja",
    bed("Zwei Seiten eines Dreiecks sind 5 cm und 8 cm lang. Nenne eine dritte Seitenlänge in cm, mit der sich das Dreieck konstruieren lässt und die länger ist als jede der beiden anderen.", [R],
        [("länger als beide anderen Seiten", [">", "$1", 8], "$1", "Deine Seite ist {} cm lang."), ("Dreieck lässt sich konstruieren", ["<", "$1", 13], "$1", "Deine Seite ist {} cm lang. Die beiden anderen sind zusammen nur 13 cm lang.")],
        [10], [([7], "länger als beide anderen Seiten"), ([13], "Dreieck lässt sich konstruieren"), ([20], "Dreieck lässt sich konstruieren")],
        "Zwei Seiten zusammen müssen länger sein als die dritte.", "5 cm + 8 cm = 13 cm. Die dritte Seite muss kürzer als 13 cm sein und soll länger als 8 cm sein, zum Beispiel 10 cm.", gut=[["8,5"], ["12,9"]]), None, None)
innen = ["/", ["*", ["-", "$1", 2], 180], "$1"]
neu(f, "vieleck", "V", 3, "verknuepfen", WINK, "ja",
    bed("Nenne die Eckenzahl eines regelmäßigen Vielecks, dessen Innenwinkel größer als 130° ist, und diesen Innenwinkel in Grad.", [G, R],
        [("mindestens 3 Ecken", [">=", "$1", 3], "$1", "Deine Eckenzahl ist {}."), ("Innenwinkel passt zur Eckenzahl", ["=", ["*", "$1", "$2"], ["*", ["-", "$1", 2], 180]], innen, "Zu deiner Eckenzahl gehört der Innenwinkel {}°."),
         ("Innenwinkel größer als 130°", [">", "$2", 130], "$2", "Dein Innenwinkel hat {}°.")],
        [8, 135], [([2, 0], "mindestens 3 Ecken"), ([8, 140], "Innenwinkel passt zur Eckenzahl"), ([6, 120], "Innenwinkel größer als 130°")],
        "Winkelsumme (n − 2) · 180°, geteilt durch die Zahl der Ecken.", "Achteck: 6 · 180° = 1 080°, geteilt durch 8 sind 135°. Auch 9 Ecken (140°) oder 10 Ecken (144°) passen.", gut=[[9, 140], [10, 144], [12, 150]]), None, None)
neu(f, "aussenwinkel", "V", 3, "parameter", WINK, "ja",
    bed("Ein Dreieck hat bei C den Außenwinkel 110°. Nenne α und β (beide größer als 0°) so, dass α mehr als doppelt so groß ist wie β.", [R, R],
        [("beide größer als 0°", [">", ["min", "$alle"], 0], ["min", "$alle"], "Dein kleinerer Winkel hat {}°."), ("passt zum Außenwinkel 110°", ["=", ["summe", "$alle"], 110], ["summe", "$alle"], "Dein α und dein β ergeben zusammen {}°."),
         ("α mehr als doppelt so groß wie β", [">", "$1", ["*", 2, "$2"]], ["*", 2, "$2"], "Das Doppelte von deinem β ist {}°.")],
        [80, 30], [([110, 0], "beide größer als 0°"), ([80, 40], "passt zum Außenwinkel 110°"), ([70, 40], "α mehr als doppelt so groß wie β")],
        "Wie hängt der Außenwinkel mit α und β zusammen?", "α + β = 110°. Zum Beispiel α = 80° und β = 30°: 80° ist mehr als 60°.", gut=[[100, 10], ["74,5", "35,5"]]), None, None)

# ═════════════════════ Kind 2 · Flug f2 · Lineare Funktionen (11 Lernkarten) ═════════════════════
f = "f2"
neu(f, "ablesen", "B", 1, "direkt", FORM, "ja",
    luecken("Gib Steigung und Achsenabschnitt der Geraden y = 4 − 3x an.", "m = □; t = □", [-3, 4], ["-3", "4"],
            "m steht vor dem x, t steht allein. Die Reihenfolge im Term spielt keine Rolle.", "Umgestellt: y = −3x + 4. Also m = −3 und t = 4.", GZ),
    ["0-3", "4"], {0: [(4, None, "die erste Zahl für m gehalten"), (3, "fb.plusminus.zeichen_des_ergebnisses", "das Minus nicht mitgenommen")], 1: [(-3, None, "die zweite Zahl für t gehalten")]}, probe=lambda: all(4 - 3 * x == -3 * x + 4 for x in range(-3, 4)))
neu(f, "zwei_punkte", 4, 1, "direkt", VERH, "nein",
    luecken("A(1 | 2) und B(4 | 11) liegen auf einer Geraden. Nach rechts: 4 − 1 = ①. Nach oben: 11 − 2 = ②. Steigung: m = ② : ① = ③.", K(3), [3, 9, 3], ["4 - 1", "11 - 2", "(11 - 2) // (4 - 1)"],
            "Steigung ist „nach oben“ geteilt durch „nach rechts“.", "3 nach rechts, 9 nach oben: m = 9 : 3 = 3."),
    ["3", "9", "9/3"], {})
neu(f, "graph_ablesen", 13, 1, "erkennen", FORM, "ja",
    wahl("Du zeichnest die Gerade y = 2x/3 − 1. Wie gehst du vor?",
         ["−1 auf der y-Achse markieren, dann 3 nach rechts und 2 nach oben", "−1 auf der x-Achse markieren, dann 3 nach rechts und 2 nach oben", "bei (2 | 3) beginnen und 1 nach unten gehen", "−1 auf der y-Achse markieren, dann 2 nach rechts und 3 nach oben"], 0,
         "Erst t auf der y-Achse, dann das Steigungsdreieck.", "t = −1 liegt auf der y-Achse. m = 2/3: 3 nach rechts, 2 nach oben."),
    lambda: F(2, 3) * 3 - 1 == 1, {1: (None, "t auf der falschen Achse"), 2: (None, "Zähler und Nenner als Punkt gelesen"), 3: ("fb.zuordnung.x_und_y_vertauscht", "im Steigungsdreieck rechts und oben vertauscht")})
neu(f, "lage", 13, 1, "erkennen", FORM, "ja",
    wahl("g: y = 2x + 1. Welche Gerade steht senkrecht auf g?", ["y = 2x − 3", "y = −2x + 1", "y = −0,5x + 4", "y = 0,5x + 1"], 2,
         "Das Produkt der beiden Steigungen muss −1 sein.", "2 · (−0,5) = −1. Also steht y = −0,5x + 4 senkrecht auf g."),
    lambda: 2 * F(-1, 2) == -1 and all(2 * m != -1 for m in (2, -2, F(1, 2))), {0: (None, "gleiche Steigung: parallel"), 1: (None, "nur das Vorzeichen gewechselt"), 3: (None, "nur den Kehrwert genommen")})
neu(f, "wirkung", 13, 1, "erkennen", FORM, "ja",
    wahl("y = 2x + k. Was passiert mit der Geraden, wenn k größer wird?", ["Sie wird steiler.", "Sie verschiebt sich nach oben.", "Sie dreht sich um den Ursprung.", "Sie wird flacher."], 1,
         "Wo steht der Parameter: vor dem x oder allein?", "k steht allein, es ist der Achsenabschnitt. Wird k größer, rutscht die ganze Gerade nach oben. Die Steigung 2 bleibt."),
    lambda: True, {0: (None, "k für die Steigung gehalten"), 2: (None, "k für die Steigung gehalten"), 3: (None, "k für die Steigung gehalten")})
neu(f, "einsetzen", "B", 1, "direkt", FORM, "ja",
    luecken("Geradenschar y = k · x + 2k − 1. Welche Gerade gehört zu k = 3? Gib Steigung und Achsenabschnitt an.", "m = □; t = □", [3, 5], ["3", "2 * 3 - 1"],
            "Ersetze jedes k durch 3.", "y = 3x + 2 · 3 − 1 = 3x + 5.", GZ),
    ["3", "6-1"], {1: [(-1, None, "nur das k vor dem x ersetzt"), (6, None, "die −1 vergessen")]})
neu(f, "ablesen", 17, 2, "umkehr", WAAGE, "ja",
    luecken("Die Gerade ist als 2y = 6x − 8 gegeben. Bringe sie in die Form y = m · x + t.", "m = □; t = □", [3, -4], ["6 // 2", "-8 // 2"],
            "Teile beide Seiten durch 2 – jeden Summanden.", "y = 3x − 4. Also m = 3 und t = −4.", GZ),
    ["3", "0-4"], {0: [(6, "fb.waage.nur_ein_summand", "6x nicht mitgeteilt")], 1: [(-8, "fb.waage.nur_ein_summand", "die 8 nicht mitgeteilt"), (4, "fb.plusminus.zeichen_des_ergebnisses", "das Minus verloren")]})
neu(f, "graph_ablesen", "B", 2, "darstellung", FORM, "ja",
    luecken("Lies am Graphen die Steigung m und den Achsenabschnitt t ab.", "m = □; t = □", [-2, 3], ["(1 - 3) // (1 - 0)", "3"],
            "t liest du auf der y-Achse ab. Geh dann 1 nach rechts: Wie weit geht es nach oben oder unten?", "Die Gerade schneidet die y-Achse bei 3. Bei 1 nach rechts geht es 2 nach unten: m = −2.", GZ,
            grafik=KO([-4, 4], [-5, 5], graphen=[{"art": "linear", "m": -2, "t": 3, "name": "g"}])),
    ["0-2", "3"], {0: [(2, "fb.plusminus.zeichen_des_ergebnisses", "fallende Gerade mit positiver Steigung"), (3, None, "m und t vertauscht")], 1: [(-2, None, "m und t vertauscht")]})
neu(f, "proportional", 17, 2, "umkehr", VERH, "ja",
    zahl("Eine Ursprungsgerade geht durch P(4 | 10). Für welches x ist y = 25?", 10, "25 * 4 // 10",
         "Berechne zuerst k als y : x.", "k = 10 : 4 = 2,5. Aus 2,5 · x = 25 folgt x = 10."),
    ["25/(10/4)"], [(62.5, "fb.verhaeltnis.falsche_richtung", "25 · 2,5 gerechnet"), (19, "fb.verhaeltnis.addiert_statt_malgenommen", "15 mehr bei y, also 15 mehr bei x")])
neu(f, "aufstellen", 14, 2, "mehrschritt", WAAGE, "ja",
    luecken("Gerade durch P(2 | 7) mit m = 3. Weg A: Punkt einsetzen: 7 = 3 · 2 + t, also t = ①. Weg B: von P aus 2 nach links gehen: y sinkt dabei um ②, also t = 7 − ②.", K(2), [1, 6], ["7 - 3 * 2", "3 * 2"],
            "Beide Wege müssen dasselbe t ergeben.", "7 = 6 + t, also t = 1. Weg B: 2 nach links heißt 2 · 3 = 6 nach unten: 7 − 6 = 1."),
    ["1", "7-1"], {0: [(13, "fb.gegenrechnung.gleiche_rechnung", "7 + 6 gerechnet")]})
neu(f, "aufstellen", "A", 2, "mehrschritt", WAAGE, "ja",
    luecken("Die Gerade geht durch A(1 | 4) und B(3 | 10). Bestimme m und t.", "m = □; t = □", [3, 1], ["(10 - 4) // (3 - 1)", "4 - 3 * 1"],
            "Erst m aus den zwei Punkten, dann einen Punkt einsetzen.", "m = (10 − 4) : (3 − 1) = 3. Einsetzen von A: 4 = 3 · 1 + t, also t = 1.", GZ),
    ["6/2", "10-3*3"], {0: [(2, None, "nur die x-Differenz genannt")], 1: [(7, "fb.gegenrechnung.gleiche_rechnung", "4 + 3 gerechnet"), (4, None, "die y-Koordinate von A als t genommen")]})
neu(f, "schnittpunkte", 4, 2, "mehrschritt", WAAGE, "nein",
    luecken("Schnittpunkt von g: y = 3x − 2 und h: y = −x + 6. Gleichsetzen: 3x − 2 = −x + 6. Plus x: ①x − 2 = 6. Plus 2: ①x = ②. Also x = ③ und y = ④.", K(4), [4, 8, 2, 4], ["3 + 1", "6 + 2", "(6 + 2) // (3 + 1)", "3 * 2 - 2"],
            "Für den Schnittpunkt setzt du die Terme gleich.", "4x = 8, x = 2. Einsetzen: y = 3 · 2 − 2 = 4. Probe in h: −2 + 6 = 4."),
    ["4", "8", "8/4", "0-2+6"], {0: [(2, None, "x abgezogen statt dazugezählt")]})
neu(f, "schnittpunkte", "B", 2, "umkehr", WAAGE, "ja",
    luecken("g: y = 2x − 6. Wo schneidet g die x-Achse, und wo die y-Achse?", "x-Achse: (□ | 0); y-Achse: (0 | □)", [3, -6], ["6 // 2", "-6"],
            "Auf der x-Achse ist y = 0. Auf der y-Achse ist x = 0.", "y = 0: 2x = 6, x = 3. x = 0: y = −6.", GZ),
    ["3", "2*0-6"], {0: [(-3, "fb.plusminus.zeichen_des_ergebnisses", "Vorzeichen falsch"), (-6, "fb.zuordnung.x_und_y_vertauscht", "die beiden Achsen vertauscht")], 1: [(3, "fb.zuordnung.x_und_y_vertauscht", "die beiden Achsen vertauscht"), (6, "fb.plusminus.zeichen_des_ergebnisses", "das Minus verloren")]})
neu(f, "deuten", "B", 2, "einkleidung", WACHS, "ja",
    wahl("Ein Tank enthält 60 Liter. Pro Minute fließen 4 Liter ab. Welche Gleichung beschreibt den Inhalt y (in Litern) nach x Minuten?", ["y = 4x + 60", "y = 60x − 4", "y = −4x + 60", "y = −60x + 4"], 2,
         "t ist der Start, m die Änderung pro Minute.", "Start 60, pro Minute 4 weniger: y = −4x + 60. Probe: nach 5 Minuten 60 − 20 = 40 Liter."),
    lambda: -4 * 5 + 60 == 40, {0: (None, "Abnahme als Zunahme geschrieben"), 1: (None, "Start und Änderung vertauscht"), 3: (None, "Start und Änderung vertauscht")})
neu(f, "zwei_punkte", 12, 3, "fehler", VERH, "ja",
    zahl("P(−2 | 5) und Q(2 | −3) liegen auf einer Geraden. Jan rechnet m = (5 − 3) : (2 − 2). Wie groß ist die Steigung wirklich?", -2, "(-3 - 5) / (2 - (-2))",
         "Setze die negativen Koordinaten in Klammern.", "m = (−3 − 5) : (2 − (−2)) = −8 : 4 = −2. Jan hat beide Minuszeichen weggelassen."),
    ["(0-8)/4"], [(2, "fb.vorzeichen.falsches_zeichen", "Betrag richtig, Vorzeichen falsch"), (-0.5, "fb.zuordnung.x_und_y_vertauscht", "„nach rechts“ durch „nach oben“ geteilt")])
neu(f, "lage", 17, 3, "parameter", FORM, "ja",
    zahl("Für welches k sind die Geraden y = (k + 1) · x − 2 und y = 4x + 5 parallel?", 3, "4 - 1",
         "Parallele Geraden haben dieselbe Steigung.", "k + 1 = 4, also k = 3."),
    ["3"], [(5, "fb.gegenrechnung.gleiche_rechnung", "4 + 1 gerechnet"), (4, None, "k mit der Steigung gleichgesetzt")], probe=lambda: 3 + 1 == 4)
neu(f, "bueschel", 17, 3, "parameter", FORM, "ja",
    luecken("Alle Geraden y = k · (x − 2) + 3 gehen durch einen gemeinsamen Punkt Z. Gib Z an.", "Z(□ | □)", [2, 3], ["2", "0 * (2 - 2) + 3"],
            "Für welches x hat k keinen Einfluss mehr?", "Für x = 2 ist die Klammer 0. Dann ist y = 3, egal wie groß k ist. Z(2 | 3).", GZ),
    ["2", "3"], {0: [(-2, "fb.gleichung_form.falsche_richtung_verschoben", "das Vorzeichen in der Klammer falsch gelesen"), (0, None, "x = 0 eingesetzt")]}, probe=lambda: all(k * (2 - 2) + 3 == 3 for k in range(-5, 6)))
neu(f, "deuten", 17, 3, "verknuepfen", WACHS, "ja",
    zahl("Tarif A kostet 10 € Grundgebühr und 2 € je Stunde. Tarif B hat keine Grundgebühr und kostet 4,50 € je Stunde. Ab wie vielen ganzen Stunden ist Tarif A billiger?", 5, "10 // 2.5 + 1",
         "Wann sind beide gleich teuer?", "Gleich teuer: 10 + 2x = 4,5x, also x = 4. Bei 4 Stunden kosten beide 18 €. Billiger ist A erst ab 5 Stunden (20 € gegen 22,50 €)."),
    ["4+1"], [(4, "fb.gleichung_loesen.grenze_mitgezaehlt", "bei 4 Stunden sind beide gleich teuer"), (3, None, "10 : 4,5 gerechnet und aufgerundet: die 2 € je Stunde von Tarif A vergessen")], probe=lambda: 10 + 2 * 5 < F("4.5") * 5 and 10 + 2 * 4 == F("4.5") * 4)
neu(f, "ablesen", "V", 1, "direkt", FORM, "ja",
    bed("Nenne m und t einer fallenden Geraden y = m · x + t, die die y-Achse oberhalb von 2 schneidet.", [R, R],
        [("Gerade fällt", ["<", "$1", 0], "$1", "Dein m ist {}."), ("schneidet die y-Achse oberhalb von 2", [">", "$2", 2], "$2", "Dein t ist {}.")],
        [-1, 5], [([1, 5], "Gerade fällt"), ([-1, 2], "schneidet die y-Achse oberhalb von 2"), ([0, 3], "Gerade fällt")],
        "Welche Zahl entscheidet über Steigen oder Fallen, welche über den Schnitt mit der y-Achse?", "Fallend heißt m negativ. Der Schnitt mit der y-Achse ist t. Zum Beispiel m = −1 und t = 5.", gut=[["-0,5", "2,1"]]), None, None)
steig = ["/", ["-", "$4", "$2"], ["-", "$3", "$1"]]
neu(f, "zwei_punkte", "V", 2, "umkehr", VERH, "ja",
    bed("Nenne zwei Punkte mit ganzen Koordinaten und verschiedenen x-Werten, durch die eine Gerade mit der Steigung −3 geht. Reihenfolge der Felder: x und y des ersten Punkts, x und y des zweiten Punkts.", [G, G, G, G],
        [("verschiedene x-Werte", ["!=", "$1", "$3"], None, "Deine beiden Punkte haben denselben x-Wert."), ("Steigung ist −3", ["=", ["-", "$4", "$2"], ["*", -3, ["-", "$3", "$1"]]], steig, "Die Steigung zwischen deinen Punkten ist {}.")],
        [0, 0, 1, -3], [([1, 2, 1, 5], "verschiedene x-Werte"), ([0, 0, 1, 3], "Steigung ist −3"), ([0, 0, 3, -1], "Steigung ist −3")],
        "Was heißt Steigung −3 für einen Schritt nach rechts?", "1 nach rechts, 3 nach unten: zum Beispiel (0 | 0) und (1 | −3).", gut=[[2, 5, 4, -1], [1, 1, -1, 7]]), None, None)
neu(f, "aufstellen", "V", 2, "umkehr", WAAGE, "ja",
    bed("Nenne m und t so, dass die Gerade y = m · x + t durch den Punkt P(2 | 5) geht und nicht waagrecht ist.", [R, R],
        [("nicht waagrecht", ["!=", "$1", 0], None, "Mit m = 0 ist die Gerade waagrecht."), ("geht durch P(2 | 5)", ["=", ["+", ["*", 2, "$1"], "$2"], 5], ["+", ["*", 2, "$1"], "$2"], "Bei x = 2 hat deine Gerade den Wert {}.")],
        [1, 3], [([0, 5], "nicht waagrecht"), ([1, 4], "geht durch P(2 | 5)"), ([2, 2], "geht durch P(2 | 5)")],
        "Setze x = 2 ein. Was muss herauskommen?", "2m + t muss 5 sein. Zum Beispiel m = 1 und t = 3, oder m = 2 und t = 1.", gut=[[2, 1], [-1, 7], ["0,5", 4]]), None, None)
neu(f, "lage", "V", 3, "parameter", FORM, "ja",
    bed("Nenne die Steigungen zweier Geraden, die senkrecht aufeinander stehen. Keine der beiden Steigungen soll 1 oder −1 sein.", [R, R],
        [("keine Steigung ist 1 oder −1", UND(["!=", ["betrag", "$1"], 1], ["!=", ["betrag", "$2"], 1]), None, "Eine deiner Steigungen ist 1 oder −1."),
         ("Geraden stehen senkrecht", ["=", ["*", "$1", "$2"], -1], ["*", "$1", "$2"], "Das Produkt deiner Steigungen ist {}.")],
        [2, "-0,5"], [([1, -1], "keine Steigung ist 1 oder −1"), ([2, "0,5"], "Geraden stehen senkrecht"), ([2, -2], "Geraden stehen senkrecht")],
        "Was gilt für das Produkt der Steigungen senkrechter Geraden?", "Das Produkt muss −1 sein: zum Beispiel 2 und −0,5, oder −4 und 0,25.", gut=[[-4, "0,25"], ["2/3", "-3/2"]]), None, None)
neu(f, "deuten", "V", 3, "transfer", WACHS, "ja",
    bed("Eine Kerze brennt gleichmäßig ab. Ihre Höhe nach x Stunden ist y = m · x + t (in cm). Nenne m und t so, dass die Kerze am Anfang höher als 10 cm ist und nach genau 6 Stunden abgebrannt ist.", [R, R],
        [("am Anfang höher als 10 cm", [">", "$2", 10], "$2", "Am Anfang ist deine Kerze {} cm hoch."), ("nach 6 Stunden abgebrannt", ["=", ["+", ["*", 6, "$1"], "$2"], 0], ["+", ["*", 6, "$1"], "$2"], "Nach 6 Stunden ist deine Kerze {} cm hoch.")],
        [-2, 12], [([-1, 6], "am Anfang höher als 10 cm"), ([-2, 13], "nach 6 Stunden abgebrannt"), ([2, 12], "nach 6 Stunden abgebrannt")],
        "t ist die Höhe am Anfang, m die Änderung pro Stunde. Abgebrannt heißt: Höhe 0.", "6m + t = 0. Zum Beispiel t = 12 und m = −2: Die Kerze verliert 2 cm pro Stunde.", gut=[[-3, 18], ["-2,5", 15]]), None, None)

# ═════════════════════ Kind 2 · Flug a6 · Gleichungssysteme (9 Lernkarten) ═════════════════════
f = "a6"
neu(f, "pruefen", 12, 1, "erkennen", LOES, "ja",
    wahl("Ist das Zahlenpaar (3 | 2) eine Lösung des Systems I: x + y = 5 und II: 2x − y = 5?",
         ["Ja, beide Gleichungen stimmen.", "Nein, nur Gleichung I stimmt.", "Nein, nur Gleichung II stimmt.", "Nein, keine der beiden stimmt."], 1,
         "Setze das Paar in beide Gleichungen ein.", "I: 3 + 2 = 5 stimmt. II: 2 · 3 − 2 = 4, nicht 5. Das Paar löst nur I, also nicht das System."),
    lambda: 3 + 2 == 5 and 2 * 3 - 2 != 5, {0: (None, "nur in Gleichung I eingesetzt"), 2: (None, "die Gleichungen verwechselt"), 3: (None, "falsch eingesetzt")})
neu(f, "grafisch", 13, 1, "erkennen", LOES, "ja",
    wahl("Die zwei Geraden eines Gleichungssystems sind parallel und verschieden. Was heißt das für die Lösung?", ["Es gibt genau eine Lösung.", "Es gibt keine Lösung.", "Es gibt unendlich viele Lösungen."], 1,
         "Die Lösung ist der Schnittpunkt.", "Parallele, verschiedene Geraden haben keinen Schnittpunkt. Das System hat keine Lösung."),
    lambda: True, {0: (None, "Schnittpunkt angenommen"), 2: (None, "gilt nur, wenn die Geraden aufeinanderliegen")})
neu(f, "addition", 13, 1, "erkennen", LOES, "ja",
    wahl("I: 3x + 2y = 12 und II: 5x − 2y = 4. Was entsteht, wenn du beide Gleichungen addierst?", ["8x = 16", "4y = 16", "8x + 4y = 16", "8x = 8"], 0,
         "Was passiert mit +2y und −2y?", "2y und −2y sind Gegenzahlen und fallen weg. Links 3x + 5x = 8x, rechts 12 + 4 = 16."),
    lambda: 3 + 5 == 8 and 2 - 2 == 0 and 12 + 4 == 16, {1: (None, "x statt y wegfallen lassen"), 2: (None, "die Gegenzahlen addiert, als hätten sie gleiches Vorzeichen"), 3: (None, "rechts abgezogen statt addiert")})
neu(f, "verfahren", 13, 1, "erkennen", LOES, "ja",
    wahl("I: y = 4x − 1 und II: y = −x + 9. Welches Verfahren ist hier am geschicktesten?", ["Gleichsetzen", "Addieren", "erst beide Gleichungen mal 2 nehmen"], 0,
         "Schau auf die Form der beiden Gleichungen.", "Zweimal steht y = … da. Also die rechten Seiten gleichsetzen: 4x − 1 = −x + 9."),
    lambda: 4 * 2 - 1 == -2 + 9, {1: (None, "Addieren ließe y nicht wegfallen"), 2: (None, "unnötiger Umweg")})
neu(f, "einsetzen", 4, 2, "mehrschritt", MK, "nein",
    luecken("I: y = 2x − 1 und II: 3x + y = 14. Einsetzen: 3x + (2x − 1) = 14. Zusammenfassen: ①x − 1 = 14. Also ①x = ②, x = ③ und y = ④.", K(4), [5, 15, 3, 5], ["3 + 2", "14 + 1", "(14 + 1) // (3 + 2)", "2 * 3 - 1"],
            "Steht y = … schon da, setzt du diesen Term ein.", "5x − 1 = 14, 5x = 15, x = 3. Dann y = 2 · 3 − 1 = 5. Probe in II: 9 + 5 = 14."),
    ["5", "15", "15/5", "14-3*3"], {1: [(13, "fb.gegenrechnung.gleiche_rechnung", "14 − 1 gerechnet")]})
neu(f, "grafisch", "B", 2, "darstellung", LOES, "ja",
    luecken("Lies die Lösung des Gleichungssystems am Graphen ab.", "x = □; y = □", [1, 2], ["(3 - 1) // (1 + 1)", "1 + 1"],
            "Die Lösung ist der Schnittpunkt der beiden Geraden.", "Die Geraden schneiden sich in (1 | 2). Probe: 1 + 1 = 2 und −1 + 3 = 2.", GZ,
            grafik=KO([-3, 5], [-2, 6], graphen=[{"art": "linear", "m": 1, "t": 1, "name": "g"}, {"art": "linear", "m": -1, "t": 3, "name": "h"}])),
    ["1", "0-1+3"], {0: [(2, "fb.zuordnung.x_und_y_vertauscht", "x und y vertauscht")], 1: [(1, "fb.zuordnung.x_und_y_vertauscht", "x und y vertauscht"), (3, None, "den Achsenabschnitt von h abgelesen")]})
neu(f, "pruefen", 17, 2, "umkehr", LOES, "ja",
    luecken("Das Paar (2 | −1) soll das System I: 3x + y = a und II: x − 2y = b lösen. Bestimme a und b.", "a = □; b = □", [5, 4], ["3 * 2 + (-1)", "2 - 2 * (-1)"],
            "Setze das Paar in beide Gleichungen ein.", "I: 3 · 2 + (−1) = 5. II: 2 − 2 · (−1) = 2 + 2 = 4.", GZ),
    ["6-1", "2+2"], {0: [(7, "fb.plusminus.zeichen_des_ergebnisses", "die −1 als +1 eingesetzt")], 1: [(0, "fb.plusminus.doppelminus_uebersehen", "2 − 2 gerechnet")]})
neu(f, "gleichsetzen", "A", 2, "mehrschritt", WAAGE, "ja",
    luecken("Löse das System I: y = 3x − 5 und II: y = −2x + 10.", "x = □; y = □", [3, 4], ["(10 + 5) // (3 + 2)", "3 * 3 - 5"],
            "Zweimal y = …: Setze die Terme gleich.", "3x − 5 = −2x + 10, also 5x = 15 und x = 3. Dann y = 3 · 3 − 5 = 4.", GZ),
    ["15/5", "0-2*3+10"], {0: [(15, None, "nicht durch 5 geteilt, oder 2x abgezogen statt dazugezählt (x − 5 = 10)"), (1, None, "5 abgezogen statt dazugezählt: 5x = 5")]})
neu(f, "gleichsetzen", 14, 2, "mehrschritt", WAAGE, "ja",
    luecken("I: y = 2x + 3 und II: y = 5x − 6. Gleichsetzen: 2x + 3 = 5x − 6, also 9 = ①x und x = ②. Probe auf zwei Wegen: mit I ist y = ③, mit II ist y = ④.", K(4), [3, 3, 9, 9], ["5 - 2", "(3 + 6) // (5 - 2)", "2 * 3 + 3", "5 * 3 - 6"],
            "Beide Gleichungen müssen dasselbe y liefern.", "9 = 3x, x = 3. I: 2 · 3 + 3 = 9. II: 5 · 3 − 6 = 9. Beide ergeben y = 9."),
    ["3", "9/3", "6+3", "15-6"], {0: [(7, None, "2x dazugezählt statt abgezogen")]})
neu(f, "addition", 17, 2, "umkehr", LOES, "ja",
    zahl("I: 2x + 3y = 13 und II: 4x − y = 5. Mit welcher Zahl nimmst du Gleichung II mal, damit beim Addieren y wegfällt?", 3, "3 // 1",
         "Vor dem y sollen Gegenzahlen stehen.", "In I steht +3y. Aus −y wird mit mal 3 genau −3y. Dann fällt y beim Addieren weg."),
    ["3"], [(-3, None, "dann müsste man subtrahieren statt addieren"), (2, None, "macht nichts gleich"), (-2, None, "lässt x wegfallen, nicht y")], probe=lambda: 3 + 3 * (-1) == 0)
neu(f, "loesbarkeit", 12, 2, "mehrschritt", LOES, "ja",
    wahl("I: 2x + y = 5 und II: 4x + 2y = 10. Wie viele Lösungen hat das System?", ["keine", "genau eine", "unendlich viele"], 2,
         "Vergleiche II mit dem Doppelten von I.", "II ist genau das Doppelte von I. Beide Gleichungen sagen dasselbe; beim Lösen bleibt 0 = 0. Unendlich viele Lösungen."),
    lambda: (2 * 2, 2 * 1, 2 * 5) == (4, 2, 10), {0: (None, "das Doppelte auf der rechten Seite nicht geprüft"), 1: (None, "nicht verglichen")})
neu(f, "sachaufgabe", "B", 2, "einkleidung", LOES, "ja",
    wahl("Im Zoo zahlen 2 Erwachsene und 3 Kinder zusammen 34 €. 1 Erwachsener und 1 Kind zahlen zusammen 14 €. Welches System passt? (e: Preis für einen Erwachsenen, k: Preis für ein Kind)",
         ["2e + 3k = 14 und e + k = 34", "5 · (e + k) = 34 und e + k = 14", "2e · 3k = 34 und e · k = 14", "2e + 3k = 34 und e + k = 14"], 3,
         "Für jede Angabe eine Gleichung.", "Erste Angabe: 2e + 3k = 34. Zweite: e + k = 14. (Lösung: e = 8 €, k = 6 €.)"),
    lambda: 2 * 8 + 3 * 6 == 34 and 8 + 6 == 14, {0: (None, "die Beträge vertauscht"), 1: (None, "alle Personen zum selben Preis gerechnet"), 2: (None, "malgenommen statt zusammengezählt")})
neu(f, "einsetzen", 12, 3, "fehler", MK, "ja",
    zahl("I: y = x + 4 und II: 2x − y = 3. Ben setzt ein und schreibt: 2x − x + 4 = 3. Welchen Wert hat x wirklich?", 7, "3 + 4",
         "Der ganze Term x + 4 wird abgezogen. Was fehlt bei Ben?", "Mit Klammer: 2x − (x + 4) = 3, also 2x − x − 4 = 3 und x = 7. Probe: y = 11, 14 − 11 = 3."),
    ["14-7"], [(-1, "fb.minusklammer.nur_erstes_zeichen", "wie Ben ohne Klammer: x + 4 = 3")], probe=lambda: 2 * 7 - (7 + 4) == 3)
neu(f, "loesbarkeit", 17, 3, "parameter", LOES, "ja",
    zahl("I: 3x − y = 2 und II: 6x − 2y = c. Für welches c hat das System unendlich viele Lösungen?", 4, "2 * 2",
         "II muss dasselbe sagen wie I.", "Das Doppelte von I ist 6x − 2y = 4. Für c = 4 sind beide Gleichungen gleichwertig."),
    ["8/2"], [(2, None, "die rechte Seite nicht verdoppelt"), (0, None, "an 0 = 0 gedacht und c = 0 gesetzt")])
neu(f, "loesung_parameter", 17, 3, "parameter", LOES, "ja",
    zahl("Beim Lösen eines Gleichungssystems bleibt (k − 3) · x = 6 übrig. Für welches k hat das System keine Lösung?", 3, "0 + 3",
         "Wann darfst du nicht durch k − 3 teilen?", "Für k = 3 steht da 0 · x = 6. Das ist für kein x wahr: keine Lösung."),
    ["9/3"], [(-3, "fb.nullprodukt.vorzeichen_der_loesung", "Vorzeichen falsch"), (9, None, "x = 1 gesetzt: k − 3 = 6"), (6, None, "die rechte Seite genannt")], probe=lambda: (3 - 3) * 5 != 6)
neu(f, "sachaufgabe", "A", 3, "verknuepfen", LOES, "ja",
    zahl("In einem Stall sind Hühner und Kaninchen: zusammen 20 Tiere mit 56 Beinen. Wie viele Kaninchen sind es?", 8, "(56 - 2 * 20) // 2",
         "Für jede gesuchte Zahl eine Variable: h Hühner, k Kaninchen.", "h + k = 20 und 2h + 4k = 56. Wären alle Hühner, gäbe es 40 Beine. Die 16 Beine mehr gehören zu 8 Kaninchen."),
    ["(56-40)/2"], [(12, None, "die Hühner statt der Kaninchen genannt"), (14, None, "56 : 4 gerechnet")], probe=lambda: 12 + 8 == 20 and 2 * 12 + 4 * 8 == 56)
neu(f, "pruefen", "V", 1, "direkt", LOES, "ja",
    bed("Nenne ein Zahlenpaar (x | y), das die Gleichung 2x + y = 7 löst, aber die Gleichung x − y = 2 nicht.", [R, R],
        [("löst 2x + y = 7", ["=", ["+", ["*", 2, "$1"], "$2"], 7], ["+", ["*", 2, "$1"], "$2"], "Bei dir ist 2x + y = {}."), ("löst x − y = 2 nicht", ["!=", ["-", "$1", "$2"], 2], None, "Dein Paar löst auch die zweite Gleichung.")],
        [1, 5], [([1, 4], "löst 2x + y = 7"), ([3, 1], "löst x − y = 2 nicht")],
        "Wähle ein x und rechne das passende y aus.", "Zum Beispiel (1 | 5): 2 + 5 = 7, und 1 − 5 = −4 ist nicht 2. Nur (3 | 1) löst beide.", gut=[[0, 7], ["2,5", 2]]), None, None)
neu(f, "sachaufgabe", "V", 2, "einkleidung", LOES, "ja",
    bed("Karten für Erwachsene kosten 6 €, für Kinder 4 €. Eine Gruppe zahlt zusammen genau 40 €. Nenne eine mögliche Zahl von Erwachsenen und von Kindern (jeweils mindestens 1).", [G, G],
        [("jeweils mindestens 1", [">=", ["min", "$alle"], 1], ["min", "$alle"], "Deine kleinere Zahl ist {}."), ("zusammen 40 €", ["=", ["+", ["*", 6, "$1"], ["*", 4, "$2"]], 40], ["+", ["*", 6, "$1"], ["*", 4, "$2"]], "Deine Gruppe zahlt {} €.")],
        [4, 4], [([0, 10], "jeweils mindestens 1"), ([4, 3], "zusammen 40 €"), ([3, 5], "zusammen 40 €")],
        "Stelle eine Gleichung mit zwei Variablen auf.", "6e + 4k = 40. Es passen 2 Erwachsene und 7 Kinder, 4 und 4 oder 6 und 1.", gut=[[2, 7], [6, 1]]), None, None)
neu(f, "loesbarkeit", "V", 2, "umkehr", LOES, "ja",
    bed("Ergänze Gleichung II so, dass das System keine Lösung hat. I: 2x + y = 3, II: 4x + □ · y = □.", [R, R],
        [("nicht genau eine Lösung", ["=", "$1", 2], None, "Mit deiner Zahl vor dem y hat das System genau eine Lösung."), ("nicht unendlich viele Lösungen", ["!=", "$2", 6], None, "Mit deinen Zahlen ist II das Doppelte von I: unendlich viele Lösungen.")],
        [2, 5], [([1, 5], "nicht genau eine Lösung"), ([2, 6], "nicht unendlich viele Lösungen"), ([-2, 6], "nicht genau eine Lösung")],
        "Vergleiche II mit dem Doppelten von I.", "Das Doppelte von I ist 4x + 2y = 6. Steht links dasselbe, rechts aber eine andere Zahl, widersprechen sich die Gleichungen: zum Beispiel 4x + 2y = 5.", gut=[[2, 0], [2, "6,5"]]), None, None)
neu(f, "addition", "V", 3, "parameter", LOES, "ja",
    bed("Baue ein Gleichungssystem mit genau einer Lösung, nämlich (2 | 3). I: x + y = □ und II: □ · x − y = □. Die Zahl vor dem x soll nicht 0 sein.", [R, R, R],
        [("Gleichung I stimmt für (2 | 3)", ["=", "$1", 5], None, "Mit (2 | 3) hat die linke Seite von I den Wert 5."), ("Zahl vor dem x ist nicht 0", ["!=", "$2", 0], None, "Die Zahl vor dem x soll nicht 0 sein."),
         ("Gleichung II stimmt für (2 | 3)", ["=", ["-", ["*", 2, "$2"], 3], "$3"], ["-", ["*", 2, "$2"], 3], "Mit (2 | 3) hat die linke Seite von II den Wert {}."),
         ("genau eine Lösung", ["!=", "$2", -1], None, "Mit dieser Zahl vor dem x hat dein System nicht genau eine Lösung.")],
        [5, 2, 1], [([6, 2, 1], "Gleichung I stimmt für (2 | 3)"), ([5, 0, -3], "Zahl vor dem x ist nicht 0"), ([5, 2, 2], "Gleichung II stimmt für (2 | 3)"), ([5, -1, -5], "genau eine Lösung")],
        "Setze (2 | 3) in beide Gleichungen ein.", "I: 2 + 3 = 5. II: zum Beispiel 2x − y = 1, denn 4 − 3 = 1. Addieren ergibt 3x = 6, also x = 2.", gut=[[5, 1, -1], [5, "0,5", -2]]), None, None)
neu(f, "loesung_parameter", "V", 3, "parameter", LOES, "ja",
    bed("I: y = k · x + 2 und II: y = 3x + c. Nenne k und c so, dass das System genau eine Lösung hat und diese bei x = 1 liegt.", [R, R],
        [("genau eine Lösung", ["!=", "$1", 3], None, "Mit deinem k hat das System nicht genau eine Lösung."), ("Lösung liegt bei x = 1", ["=", ["+", "$1", 2], ["+", 3, "$2"]], ["+", "$1", 2], "Bei x = 1 liefert I den Wert {}. II liefert etwas anderes.")],
        [5, 4], [([3, 2], "genau eine Lösung"), ([5, 3], "Lösung liegt bei x = 1"), ([0, 0], "Lösung liegt bei x = 1")],
        "Setze x = 1 in beide Gleichungen ein. Was muss gelten?", "Bei x = 1 müssen beide dasselbe y liefern: k + 2 = 3 + c. Zum Beispiel k = 5 und c = 4. Für k = 3 wären die Geraden parallel.", gut=[[1, 0], ["-2", "-3"]]), None, None)

# ═════════════════════ Prüfen ═════════════════════
ZWEIDEUTIG = re.compile(r"\d/\d+[a-zA-Z]|/\([^()]*\(|\)\)/")       # 1/2x · /( … ( · )) /


def texte_von(q):
    t = [q["f"]["text"], q["h"], q["w"]] + list(q.get("a", [])) + [q["f"].get("hinweis", "")]
    if q["y"] == "bedingung":
        t += [b["name"] for b in q["o"]["bedingungen"]] + [b.get("hinweis", "") for b in q["o"]["bedingungen"]]
    return t


def grafik_ok(g):
    if g["typ"] == "tabelle":
        return all(len(z) == len(g["kopf"]) and all(isinstance(x, str) for x in z) for z in g["zeilen"]) and all(isinstance(x, str) for x in g["kopf"])
    if g["typ"] in ("saeulen", "kreisdiagramm"):
        return all(set(w) == {"name", "wert"} and len(w["name"]) <= 8 for w in g["werte"]) and (g["typ"] == "saeulen" or sum(w["wert"] for w in g["werte"]) == 100)
    if g["typ"] == "koordinaten":
        return len(g["x"]) == len(g["y"]) == 2 and set(g) <= {"typ", "x", "y", "graphen", "kreise"} and all(gr["art"] in ("linear", "poly") for gr in g.get("graphen", []))
    if g["typ"] == "figur":
        namen = set(g["punkte"])
        return all(l[0] in namen and l[1] in namen for l in g.get("linien", [])) and all(set(w[:3]) <= namen for w in g.get("winkel", [])) and set(g) <= {"typ", "punkte", "linien", "winkel", "flaeche"}
    return False


aus = {fl: [] for fl in FLUG}
je_thema = {}
n_rechnung = n_fb = n_grafik = n_bruch = 0
for a in sorted(A, key=lambda a: (list(FLUG).index(a["flug"]), a["typ"] == "V", a["aufgabe"]["s"])):       # Schwierigkeit aufsteigend, erst ohne Bau, dann „bedingung“
    q = a["aufgabe"]
    n = sum(1 for e in aus[a["flug"]] if (e["antwortform"] == "bedingung") == (a["typ"] == "V")) + 1
    kenn = f"{FLUG[a['flug']][4]}-{'B' + str(n) if a['typ'] == 'V' else format(n, '02d')}"
    assert a["regel"] in REGELN, (kenn, a["regel"])
    assert ip.STUFE_VON[q["g"]] == q["s"], (kenn, q["g"], q["s"])
    assert a["typ"] in TYP and a["zaehlt"] in ("ja", "folge", "nein"), kenn
    for t in texte_von(q):
        assert not ZWEIDEUTIG.search(t), (kenn, "Bruch nicht eindeutig", t)
        n_bruch += bool(re.search(r"\d/[\d(]|\)/\(|[a-z]/\d", t))
    if a["probe"]:
        assert a["probe"]() is True, kenn
    if "grafik" in q["f"]:
        assert grafik_ok(q["f"]["grafik"]), (kenn, "grafik")
        n_grafik += 1
    eintrag = dict(kennung=kenn, thema=a["thema"], lernkarte=q["l"], stufe=q["s"], typ=TYP[a["typ"]], antwortform=q["y"], regel=a["regel"], regel_name=REGELN[a["regel"]]["name"], zaehlt=a["zaehlt"], fehlbilder=[])

    def fb_eintrag(ort, antwort, fbk, text):
        global n_fb
        assert fbk is None or fbk in FEHLBILD, (kenn, fbk)
        n_fb += 1
        eintrag["fehlbilder"].append(dict(**ort, antwort=antwort, fehlbild=fbk, regel_des_fehlbilds=FEHLBILD.get(fbk), beschreibung=text))

    if q["y"] == "zahl":
        soll = ip.rechne(q["c"])
        assert soll == ip.zahlwert(q["o"]["wert"]) == z2(a["zweit"][0]), (kenn, soll, z2(a["zweit"][0]))
        n_rechnung += 1
        werte = set()
        for w, fbk, text in a["fb"]:
            assert w != q["o"]["wert"] and w not in werte, (kenn, w)
            werte.add(w)
            fb_eintrag({}, w, fbk, text)
    elif q["y"] == "luecken":
        soll = [ip.rechne(c) for c in q["c"]]
        assert soll == q["o"]["werte"] == [z2(z) for z in a["zweit"]], (kenn, soll, [z2(z) for z in a["zweit"]])
        assert all(isinstance(w, int) for w in q["o"]["werte"]) and q["f"]["schablone"].count("□") == len(soll), kenn
        n_rechnung += len(soll)
        for i, liste in sorted(a["fb"].items()):
            werte = set()
            for w, fbk, text in liste:
                assert w != soll[i] and w not in werte, (kenn, i, w)
                werte.add(w)
                fb_eintrag({"luecke": i + 1}, w, fbk, text)
    elif q["y"] == "auswahl":
        assert a["zweit"]() is True and len(set(q["a"])) == len(q["a"]) >= 3, kenn
        assert set(a["fb"]) == set(range(len(q["a"]))) - {q["o"]["index"]}, kenn
        for i, (fbk, text) in sorted(a["fb"].items()):
            fb_eintrag({"index": i}, q["a"][i], fbk, text)
    else:
        fehler = bd.pruefe_aufgabe(q)
        assert fehler == [], (kenn, fehler)
        assert 1 <= len(q["f"]["felder"]) <= 4 and all(len(b["name"]) <= 40 for b in q["o"]["bedingungen"]), kenn
        assert {g["verletzt"] for g in q["o"]["gegenbeispiele"]} == {b["name"] for b in q["o"]["bedingungen"]}, kenn      # jede Bedingung hat ein Gegenbeispiel
        for g in [q["o"]["beispiel"]] + q["o"].get("gut", []):          # zweite Probe: jede gute Antwort wird als richtig bewertet
            r = bd.bewerte(q, {"werte": [str(x).replace("-", "−") for x in g]})
            assert r["format_ok"] and r["richtig"], (kenn, g, r)
        for g in q["o"]["gegenbeispiele"]:                             # dritte Probe: jedes Gegenbeispiel scheitert genau an der genannten Bedingung, mit lesbarem Hinweis
            r = bd.bewerte(q, {"werte": [str(x) for x in g["werte"]]})
            assert r["format_ok"] and not r["richtig"] and r["verletzt"] == g["verletzt"] and r.get("hinweis") and "{}" not in r["hinweis"], (kenn, g, r)
        eintrag["hinweis_zu_fehlbildern"] = "Aus einer verletzten Bedingung allein folgt kein Fehlbild (Festlegung 7 im Format)."
    eintrag["aufgabe"] = q
    aus[a["flug"]].append(eintrag)
    je_thema.setdefault(a["thema"], []).append(q)

lagen = {}
for a in A:
    if a["aufgabe"]["y"] == "auswahl":
        lagen.setdefault(len(a["aufgabe"]["a"]), []).append(a["aufgabe"]["o"]["index"])
assert set(lagen[4]) == {0, 1, 2, 3}, lagen
texte = [a["aufgabe"]["f"]["text"] + json.dumps(a["aufgabe"]["f"].get("grafik"), sort_keys=True) for a in A]
assert len(set(texte)) == len(texte)


def lauf(pfad):
    r = subprocess.run([sys.executable, "-I", os.path.join(WURZEL, "tools", "inhalt_pruefen.py"), pfad], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


print("Thema                          neu  inhalt_pruefen vorher → nachher")
with tempfile.TemporaryDirectory() as tmp:
    for thema, liste in je_thema.items():
        quelle = os.path.join(WURZEL, "inhalte", "themen", f"{thema}.json")
        d = json.load(open(quelle, encoding="utf-8"))
        assert all(q["l"] in {e["lernziel"] for e in d["inhalt"]["etappen"]} and q["t"] in {t["k"] for t in d["inhalt"]["teilfaehigkeiten"]} for q in liste), thema
        assert not {x["f"].get("text") for x in d["aufgaben"]} & {q["f"]["text"] for q in liste if "grafik" not in q["f"]}, thema       # keine Aufgabe wörtlich doppelt zum Bestand
        code0, aus0 = lauf(quelle)
        d["aufgaben"] = d["aufgaben"] + liste
        ziel = os.path.join(tmp, f"{thema}.json")
        json.dump(d, open(ziel, "w", encoding="utf-8"), ensure_ascii=False)
        code1, aus1 = lauf(ziel)
        print(f"{thema:30} {len(liste):3}  Code {code0} → {code1}")
        if code1 != 0:
            print(aus1[-2500:])
        assert code0 == 0 and code1 == 0, thema

for flug, liste in aus.items():
    normal = [e for e in liste if e["antwortform"] != "bedingung"]
    viele = [e for e in liste if e["antwortform"] == "bedingung"]
    assert 15 <= len(normal) <= 18 and len(viele) == 5, (flug, len(normal), len(viele))
    titel, kind, klasse = FLUG[flug][:3]
    karten = sorted({e["lernkarte"] for e in liste})
    json.dump({"stand": "2026-11-27", "flug": flug, "titel": titel, "fuer": kind, "klasse": klasse, "themen": FLUG[flug][3],
               "hinweis": "Aufgaben auf Vorrat, rollendes System Stufe 3. Nicht eingespielt. Je Eintrag: Zusatzangaben (Regel-Kennung, Fehlbilder, Typ, Zählvorschlag) und unter „aufgabe“ die Aufgabe im Format von inhalte/README.md. "
                          "Reihenfolge: erst die Aufgaben ohne Bau, dann die des Typs „bedingung“, jeweils mit aufsteigender Stufe.",
               "aufgaben": normal + viele}, open(os.path.join(HIER, f"{flug}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    alle = {l for (t, l) in KARTE if t in FLUG[flug][3]} - WEG.get(flug, set())
    assert set(karten) == alle, (flug, alle - set(karten))
    typen = {}
    for e in normal:
        typen[e["typ"].split(" (")[0]] = typen.get(e["typ"].split(" (")[0], 0) + 1
    print(f"{flug:9} {kind}: {len(normal)} ohne Bau, {len(viele)} bedingung; Stufen {[sum(1 for e in liste if e['stufe'] == s) for s in (1, 2, 3)]}; Lernkarten {len(karten)}; mit Zeichnung {sum(1 for e in liste if 'grafik' in e['aufgabe']['f'])}; {typen}")
print(f"{len(A)} Aufgaben; {n_rechnung} Rechnungen zweifach nachgerechnet; {n_fb} Fehlbilder, davon {sum(1 for fl in aus.values() for e in fl for x in e['fehlbilder'] if x['fehlbild'])} mit Kennung; "
      f"{n_grafik} Aufgaben mit Zeichnung; {n_bruch} Texte mit Bruchstrich, keiner zweideutig")
print("OK")
