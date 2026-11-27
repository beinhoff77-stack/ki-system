"""Mathe-Profi, Auftrag 14 Teil C: neue Aufgaben für die nächsten Flüge (rollendes System, Stufe 1).

Aufruf: python3 -I inhalte/mathe-profi/rollend-1/bauen.py
Kind 1: ge1, z2. Kind 2: ge2, a4. Je Flug 14 Aufgaben in Typen ohne Bau (zahl, auswahl, luecken) und 5 des Typs „bedingung“.
- jede Rechenaufgabe zweifach nachgerechnet (Feld c mit dem Rechner aus tools/inhalt_pruefen.py; zweiter Weg hier),
- jede Auswahl-Aufgabe mit einer Probe, jedes Fehlbild ergibt eine andere Antwort als die Lösung,
- jede „bedingung“-Aufgabe: tools/bedingung.py pruefe_aufgabe liefert eine leere Fehlerliste,
- Regel und Fehlbild als Kennung aus regeln-uebersicht/kennungen.json (geprüft: Kennung existiert),
- alle Aufgaben an eine Kopie der Themen-Datei gehängt und mit tools/inhalt_pruefen.py geprüft (Fehlerzahl vorher = nachher).
Schreibt je Flug eine Datei <flug>.json. Nur Inhalte. Nichts wird eingespielt.
"""
import importlib.util
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
FLUG = {"ge1": ("Formen und Grundbegriffe", "Kind 1", 5), "z2": ("Teilbarkeit", "Kind 1", 5), "ge2": ("Spiegeln und Symmetrie", "Kind 2", 7), "a4": ("Lineare Ungleichungen", "Kind 2", 8)}
A = []
ABST, WINK, DECK, BAU, LOES = "id.geometrie.abstand", "id.geometrie.winkel", "id.geometrie.deckungsgleich", "id.zahlen.bausteine", "id.algebra.gleichung_loesen"
PM, WAAGE, MK = "rr.plusminus", "rr.waage", "rr.minusklammer"


def z2(ausdruck):
    genau = re.sub(r"(?<![\w.])(\d+)(?![\w.])", r"F(\1)", ausdruck)
    return F(eval(genau, {"__builtins__": {}}, {"F": F, "abs": abs}))


def neu(flug, thema, typ, l, s, g, regel, zaehlt, aufgabe, zweit, fb):
    n = sum(1 for a in A if a["flug"] == flug and (a["typ"] == "V") == (typ == "V")) + 1
    kenn = f"{flug.upper()}-{'B' if typ == 'V' else ''}{n:02d}" if typ != "V" else f"{flug.upper()}-B{n}"
    A.append(dict(flug=flug, thema=thema, kenn=kenn, typ=typ, regel=regel, zaehlt=zaehlt, aufgabe={"l": l, "t": l, "p": "uebung", "s": s, "g": g, **aufgabe}, zweit=zweit, fb=fb))


def luecken(text, schablone, werte, c, h, w, hinweis="Je Lücke eine ganze Zahl (mit Minus, falls negativ)."):
    return {"y": "luecken", "f": {"text": text, "schablone": schablone, "hinweis": hinweis}, "o": {"werte": werte}, "c": c, "h": h, "w": w}


def zahl(text, wert, c, h, w):
    return {"y": "zahl", "f": {"text": text}, "o": {"wert": wert}, "c": c, "h": h, "w": w}


def wahl(text, antworten, index, h, w):
    return {"y": "auswahl", "f": {"text": text}, "a": antworten, "o": {"index": index}, "h": h, "w": w}


def bed(text, felder, bedingungen, beispiel, gegen, h, w, gut=None):
    """bedingungen: [(name, pruefe, zeige oder None, hinweis)]; gegen: [(werte, name)]"""
    bs = [{"name": n, "pruefe": p, **({"zeige": z} if z is not None else {}), "hinweis": hi} for n, p, z, hi in bedingungen]
    o = {"bedingungen": bs, "beispiel": beispiel, **({"gut": gut} if gut else {}), "gegenbeispiele": [{"werte": we, "verletzt": n} for we, n in gegen]}
    return {"y": "bedingung", "f": {"text": text, "felder": [{"art": a} for a in felder]}, "o": o, "h": h, "w": w}


K = lambda n: "; ".join(f"{'①②③④⑤'[i]} = □" for i in range(n))
UND = lambda *x: ["und", *x]
G, R = "ganz", "rational"

# ═════════════════════ Kind 1 · Flug ge1 · Formen und Grundbegriffe (Klasse 5) ═════════════════════
T, O = "geometrie.grundbegriffe", "geometrie.ortslinien"
neu("ge1", T, 4, "koordinaten", 1, "direkt", ABST, "nein",
    luecken("Vom Ursprung zum Punkt P(−4 | 3): erst ① Schritte nach links, dann ② Schritte nach oben.", K(2), [4, 3], ["abs(-4)", "3"],
            "Die erste Zahl sagt rechts oder links, die zweite oben oder unten.", "x = −4: 4 Schritte nach links. y = 3: 3 Schritte nach oben.", "Je Lücke eine Anzahl von Schritten."),
    ["0 - (-4)", "3"], {0: [(3, "fb.abstand.koordinaten_vertauscht", "x und y vertauscht")], 1: [(4, "fb.abstand.koordinaten_vertauscht", "x und y vertauscht")]})
neu("ge1", T, 4, "strecken", 1, "direkt", PM, "nein",
    luecken("A(−3 | 2) und B(5 | 2) liegen auf einer waagrechten Linie. Von A bis zur y-Achse sind es ① Einheiten, von der y-Achse bis B sind es ②. Die Strecke [AB] ist ③ lang.", K(3), [3, 5, 8],
            ["abs(-3)", "5", "5 - (-3)"], "Die Null liegt zwischen den beiden Punkten.", "Links der Achse 3, rechts 5, zusammen 8. Als Rechnung: 5 − (−3) = 8.", "Je Lücke eine Länge."),
    ["3", "5", "3+5"], {2: [(2, "fb.plusminus.doppelminus_uebersehen", "5 − 3 gerechnet: die Null zwischen den Punkten übersehen")]})
neu("ge1", T, 12, "kreis_lage", 1, "erkennen", ABST, "ja",
    wahl("Ein Kreis hat den Radius 4 cm. Sein Mittelpunkt ist 4 cm von der Geraden g entfernt. Was ist g für diesen Kreis?", ["eine Sekante", "eine Tangente", "eine Passante"], 1,
         "Vergleiche den Abstand mit dem Radius.", "Abstand und Radius sind gleich: g berührt den Kreis in genau einem Punkt. Das ist eine Tangente."),
    lambda: 4 == 4, {0: (None, "Abstand kleiner als der Radius angenommen"), 2: (None, "Abstand größer als der Radius angenommen")})
neu("ge1", T, 12, "winkelarten", 1, "erkennen", WINK, "ja",
    wahl("Ein Winkel hat 200°. Welche Winkelart ist das?", ["spitz", "stumpf", "gestreckt", "überstumpf"], 3,
         "Vergleiche mit 90° und mit 180°.", "200° ist größer als 180° und kleiner als 360°: überstumpf."),
    lambda: 180 < 200 < 360, {0: (None, "mit 360° − 200° verwechselt"), 1: (None, "stumpf endet bei 180°"), 2: (None, "gestreckt ist genau 180°")})
neu("ge1", T, 13, "vierecke", 1, "erkennen", DECK, "ja",
    wahl("Ein Viereck hat vier gleich lange Seiten, aber keinen rechten Winkel. Welcher Name ist der genaueste?", ["Quadrat", "Raute", "Rechteck", "Trapez"], 1,
         "Prüfe erst die Seiten, dann die Winkel.", "Vier gleich lange Seiten: Raute. Für ein Quadrat bräuchte es zusätzlich rechte Winkel."),
    lambda: True, {0: (None, "rechte Winkel nicht geprüft"), 2: (None, "ein Rechteck hat rechte Winkel"), 3: (None, "zu allgemein: nicht der genaueste Name")})
neu("ge1", T, 14, "strecken", 2, "mehrschritt", PM, "ja",
    zahl("Zwei Wege für die Länge von [CD] mit C(2 | −6) und D(2 | 9). Weg A: 6 + 9. Weg B: 9 − (−6) = 9 + ?. Welche Zahl steht für das Fragezeichen?", 6, "0 - (-6)",
         "Beide Wege müssen dieselbe Länge ergeben.", "Minus (−6) heißt plus 6. Beide Wege ergeben 15."),
    ["(6+9)-9"], [(-6, "fb.plusminus.doppelminus_uebersehen", "das Minus der −6 stehen gelassen")])
neu("ge1", T, 17, "strecken", 2, "umkehr", PM, "ja",
    zahl("Die Strecke [EF] ist waagrecht und 7 Einheiten lang. E(−2 | 4), und F liegt rechts von E. Welche x-Koordinate hat F?", 5, "-2 + 7",
         "Geh von E aus 7 Schritte nach rechts.", "−2 + 7 = 5, also F(5 | 4)."),
    ["7-2"], [(9, "fb.plusminus.zeichen_des_ergebnisses", "2 + 7 gerechnet: das Minus der −2 übersehen"), (-9, None, "nach links statt nach rechts gegangen")])
neu("ge1", T, "A", "lagebeziehungen", 2, "mehrschritt", ABST, "ja",
    zahl("Die Gerade g ist die waagrechte Linie durch (0 | −2). Welchen Abstand hat der Punkt P(5 | 4) von g?", 6, "4 - (-2)",
         "Der Abstand wird senkrecht gemessen. Welche Koordinate brauchst du?", "Senkrecht von y = 4 hinunter bis y = −2: 4 − (−2) = 6."),
    ["4+2"], [(2, "fb.plusminus.doppelminus_uebersehen", "4 − 2 gerechnet"), (5, "fb.abstand.koordinaten_vertauscht", "die x-Koordinate genommen")])
neu("ge1", T, "A", "winkelarten", 2, "einkleidung", WINK, "ja",
    zahl("Ein Zeiger dreht sich um drei Viertel einer vollen Drehung. Um wie viel Grad hat er sich gedreht?", 270, "360 // 4 * 3",
         "Wie viel Grad hat eine volle Drehung? Und ein Viertel davon?", "Ein Viertel von 360° sind 90°. Drei Viertel sind 270°."),
    ["360-90"], [(90, "fb.winkel.teil_der_drehung", "nur das fehlende Viertel genannt"), (75, None, "mit 100 statt 360 gerechnet")])
neu("ge1", O, "A", "kreislinie", 2, "mehrschritt", ABST, "ja",
    luecken("Welche Punkte auf der waagrechten Linie durch M(−1 | 2) haben von M den Abstand 4? Gib ihre x-Koordinaten an (kleinere zuerst).", "x = □ und x = □", [-5, 3],
            ["(-1) - 4", "(-1) + 4"], "Geh von M aus nach links und nach rechts.", "4 nach links: −5. 4 nach rechts: 3.", "Kleinere Zahl zuerst."),
    ["-(1+4)", "4-1"], {0: [(-4, None, "von 0 statt von M aus gezählt"), (5, "fb.plusminus.zeichen_des_ergebnisses", "Vorzeichen verloren")], 1: [(4, None, "von 0 statt von M aus gezählt")]})
neu("ge1", O, "A", "parallelen", 2, "mehrschritt", ABST, "ja",
    luecken("g ist die waagrechte Linie durch (0 | 1). Alle Punkte mit dem Abstand 3 von g liegen auf zwei Parallelen. Durch welche y-Werte gehen sie (kleinerer zuerst)?", "y = □ und y = □", [-2, 4],
            ["1 - 3", "1 + 3"], "Auf jeder Seite von g liegt eine Parallele.", "3 unter g: 1 − 3 = −2. 3 über g: 1 + 3 = 4.", "Kleinere Zahl zuerst."),
    ["-(3-1)", "3+1"], {0: [(-3, None, "von der x-Achse statt von g aus gemessen"), (2, "fb.plusminus.zeichen_des_ergebnisses", "3 − 1 statt 1 − 3")], 1: [(3, None, "von der x-Achse statt von g aus gemessen")]})
neu("ge1", O, 13, "sachsituationen", 2, "einkleidung", ABST, "ja",
    wahl("Ein Rasensprenger steht fest an einer Stelle und wirft das Wasser in alle Richtungen bis zu 6 m weit. Welche Form hat die nasse Fläche?",
         ["eine Kreislinie mit Radius 6 m", "ein Streifen von 6 m Breite", "eine Kreisfläche mit Radius 6 m", "eine Kreisfläche mit Durchmesser 6 m"], 2,
         "„Bis zu 6 m“ heißt: höchstens 6 m entfernt.", "Alle Punkte, die höchstens 6 m vom Sprenger entfernt sind, bilden eine Kreisfläche mit Radius 6 m."),
    lambda: True, {0: (None, "„genau 6 m“ statt „höchstens 6 m“ gelesen"), 1: (None, "Abstand zu einer Geraden statt zu einem Punkt"), 3: ("fb.aus_dem_rechteck.durchmesser_statt_radius", "Reichweite als Durchmesser genommen")})
neu("ge1", T, 17, "kreis_lage", 3, "rueckwaerts", ABST, "ja",
    zahl("Ein Kreis um M(1 | 3) hat den Radius 5. Die Gerade h verläuft senkrecht (parallel zur y-Achse), liegt rechts von M und ist eine Tangente des Kreises. Durch welchen x-Wert geht h?", 6, "1 + 5",
         "Wie weit ist eine Tangente vom Mittelpunkt entfernt?", "Eine Tangente hat vom Mittelpunkt genau den Abstand r. Rechts von M: 1 + 5 = 6."),
    ["5+1"], [(-4, "fb.abstand.nur_eine_seite", "die Tangente links von M genommen"), (5, None, "von 0 statt von M aus gemessen"), (8, "fb.abstand.koordinaten_vertauscht", "mit der y-Koordinate von M gerechnet")])
neu("ge1", O, "A", "zwei_kreise", 3, "verknuepfen", ABST, "ja",
    zahl("A(0 | 0) und B(8 | 0). Ein Kreis um A und ein Kreis um B haben beide den Radius 5 und schneiden sich in zwei Punkten. Welche x-Koordinate haben beide Schnittpunkte?", 4, "8 // 2",
         "Die Schnittpunkte sind von A und von B gleich weit entfernt.", "Beide Schnittpunkte sind von A und B gleich weit entfernt (je 5). Sie liegen deshalb über und unter der Mitte von [AB]: x = 4."),
    ["(0+8)/2"], [(5, None, "den Radius als x-Koordinate genommen"), (8, None, "die Länge von [AB] genannt"), (3, None, "die y-Koordinate eines Schnittpunkts genannt")])
# viele richtige Antworten
neu("ge1", T, "V", "koordinaten", 1, "direkt", ABST, "ja",
    bed("Nenne einen Punkt P(x | y), der links von der y-Achse und oberhalb der x-Achse liegt.", [G, G],
        [("links von der y-Achse", ["<", "$1", 0], "$1", "Deine x-Koordinate ist {}."), ("oberhalb der x-Achse", [">", "$2", 0], "$2", "Deine y-Koordinate ist {}.")],
        [-3, 2], [([3, 2], "links von der y-Achse"), ([-3, -2], "oberhalb der x-Achse"), ([0, 2], "links von der y-Achse")],
        "Welche Zahl sagt links oder rechts, welche oben oder unten?", "Links heißt: x ist negativ. Oben heißt: y ist positiv.", gut=[[-1, 1], [-20, 7]]), None, None)
neu("ge1", T, "V", "strecken", 2, "umkehr", PM, "ja",
    bed("Nenne zwei Punkte A(x | y) und B(x | y) auf derselben waagrechten Linie. A liegt links von der y-Achse, B rechts davon, und die Strecke [AB] ist genau 6 lang. Reihenfolge der Felder: x von A, y von A, x von B, y von B.", [G, G, G, G],
        [("gleiche Höhe", ["=", "$2", "$4"], None, "Deine beiden Punkte liegen nicht auf derselben waagrechten Linie."),
         ("A links von der y-Achse", ["<", "$1", 0], "$1", "Die x-Koordinate von A ist {}."), ("B rechts von der y-Achse", [">", "$3", 0], "$3", "Die x-Koordinate von B ist {}."),
         ("Länge 6", ["=", ["-", "$3", "$1"], 6], ["-", "$3", "$1"], "Deine Strecke ist {} lang.")],
        [-2, 1, 4, 1], [([-2, 1, 4, 2], "gleiche Höhe"), ([2, 1, 8, 1], "A links von der y-Achse"), ([-8, 1, -2, 1], "B rechts von der y-Achse"), ([-2, 1, 3, 1], "Länge 6")],
        "Die Null liegt zwischen den beiden Punkten.", "Links und rechts der Achse zusammen 6, zum Beispiel 2 links und 4 rechts.", gut=[[-5, 0, 1, 0], [-1, -3, 5, -3]]), None, None)
neu("ge1", O, "V", "parallelen", 2, "umkehr", ABST, "ja",
    bed("g ist die waagrechte Linie durch (0 | 2). Nenne einen Punkt P(x | y), der rechts von der y-Achse liegt und von g genau den Abstand 3 hat.", [G, G],
        [("rechts von der y-Achse", [">", "$1", 0], "$1", "Deine x-Koordinate ist {}."), ("Abstand 3 von g", ["=", ["betrag", ["-", "$2", 2]], 3], ["betrag", ["-", "$2", 2]], "Dein Punkt hat von g den Abstand {}.")],
        [1, 5], [([-1, 5], "rechts von der y-Achse"), ([1, 3], "Abstand 3 von g"), ([1, -3], "Abstand 3 von g")],
        "Der Abstand wird senkrecht gemessen – nach oben oder nach unten.", "3 über g liegt y = 5, 3 unter g liegt y = −1. Die x-Koordinate ist frei, solange sie positiv ist.", gut=[[4, -1]]), None, None)
neu("ge1", T, "V", "koordinaten", 2, "umkehr", ABST, "ja",
    bed("Ein Rechteck hat seine Seiten parallel zu den Achsen und die Ecke A(−2 | 1). Nenne die gegenüberliegende Ecke C(x | y) so, dass das Rechteck 5 breit und 3 hoch ist.", [G, G],
        [("5 breit", ["=", ["betrag", ["-", "$1", -2]], 5], ["betrag", ["-", "$1", -2]], "Dein Rechteck ist {} breit."), ("3 hoch", ["=", ["betrag", ["-", "$2", 1]], 3], ["betrag", ["-", "$2", 1]], "Dein Rechteck ist {} hoch.")],
        [3, 4], [([5, 4], "5 breit"), ([3, 3], "3 hoch")],
        "Von A aus kannst du nach rechts oder links und nach oben oder unten gehen.", "Von x = −2 aus 5 weiter: 3 oder −7. Von y = 1 aus 3 weiter: 4 oder −2. Es gibt vier richtige Ecken.", gut=[[-7, -2], [3, -2], [-7, 4]]), None, None)
neu("ge1", T, "V", "winkelarten", 3, "transfer", WINK, "ja",
    bed("Nenne drei Winkel in Grad: zuerst einen spitzen, dann einen stumpfen, dann einen überstumpfen. Zusammen sollen sie genau 360° ergeben.", [G, G, G],
        [("erster Winkel spitz", UND([">", "$1", 0], ["<", "$1", 90]), "$1", "Dein erster Winkel hat {}°."), ("zweiter Winkel stumpf", UND([">", "$2", 90], ["<", "$2", 180]), "$2", "Dein zweiter Winkel hat {}°."),
         ("dritter Winkel überstumpf", UND([">", "$3", 180], ["<", "$3", 360]), "$3", "Dein dritter Winkel hat {}°."), ("zusammen 360°", ["=", ["summe", "$alle"], 360], ["summe", "$alle"], "Deine Winkel ergeben zusammen {}°.")],
        [30, 120, 210], [([90, 120, 150], "erster Winkel spitz"), ([30, 180, 150], "zweiter Winkel stumpf"), ([30, 120, 180], "dritter Winkel überstumpf"), ([30, 120, 200], "zusammen 360°")],
        "Fang mit dem überstumpfen Winkel an: Wie viel bleibt dann für die beiden anderen?", "Zum Beispiel 30° (spitz), 120° (stumpf), 210° (überstumpf): 30 + 120 + 210 = 360.", gut=[[10, 100, 250], [80, 95, 185]]), None, None)

# ═════════════════════ Kind 1 · Flug z2 · Teilbarkeit (Klasse 5) ═════════════════════
T = "zahlen.teilbarkeit"
neu("z2", T, 4, "teiler", 1, "direkt", BAU, "nein",
    luecken("Alle Teilerpaare von 36: 1 · ①, 2 · ②, 3 · ③, 4 · ④, 6 · ⑤.", K(5), [36, 18, 12, 9, 6], ["36 // 1", "36 // 2", "36 // 3", "36 // 4", "36 // 6"],
            "Teile 36 der Reihe nach durch 1, 2, 3, 4 und 6.", "36 = 1 · 36 = 2 · 18 = 3 · 12 = 4 · 9 = 6 · 6.", "Je Lücke eine Zahl."),
    ["36/1", "36/2", "36/3", "36/4", "36/6"], {})
neu("z2", T, 4, "quersumme", 1, "direkt", BAU, "nein",
    luecken("Ist 5 271 durch 3 teilbar? Quersumme: 5 + 2 + 7 + 1 = ①. Dann ① : 3 = ②, es bleibt kein Rest. Also geht auch 5 271 : 3 auf: ③.", K(3), [15, 5, 1757], ["5 + 2 + 7 + 1", "15 // 3", "5271 // 3"],
            "Die Quersumme ist die Summe der Ziffern.", "Quersumme 15, und 15 : 3 = 5. Also ist 5 271 durch 3 teilbar: 5 271 : 3 = 1 757.", "Je Lücke eine Zahl."),
    ["15", "15/3", "5271/3"], {})
neu("z2", T, 4, "primfaktoren", 1, "direkt", BAU, "nein",
    luecken("Zerlege 84 Schritt für Schritt: 84 = 2 · ① = 2 · 2 · ② = 2 · 2 · 3 · ③.", K(3), [42, 21, 7], ["84 // 2", "42 // 2", "21 // 3"],
            "Teile immer durch die kleinste Primzahl, die passt.", "84 : 2 = 42, 42 : 2 = 21, 21 : 3 = 7. Also 84 = 2 · 2 · 3 · 7.", "Je Lücke eine Zahl."),
    ["84/2", "84/4", "84/12"], {})
neu("z2", T, 12, "endziffer", 1, "erkennen", BAU, "ja",
    wahl("Welche Zahl ist durch 5 teilbar, aber nicht durch 10?", ["4 320", "7 135", "2 551", "9 008"], 1,
         "Schau nur auf die letzte Ziffer.", "Endziffer 5: durch 5 teilbar, aber nicht durch 10. 4 320 endet auf 0 und ist auch durch 10 teilbar."),
    lambda: 7135 % 5 == 0 and 7135 % 10 != 0 and 4320 % 10 == 0 and 2551 % 5 != 0 and 9008 % 5 != 0, {0: (None, "auch durch 10 teilbar"), 2: (None, "die vordere 5 statt der Endziffer angesehen"), 3: (None, "Endziffer 8: weder durch 5 noch durch 10")})
neu("z2", T, 12, "primzahl", 1, "erkennen", BAU, "ja",
    wahl("Welche dieser Zahlen ist eine Primzahl?", ["1", "51", "57", "59"], 3,
         "Prüfe bei den ungeraden Zahlen die Teilbarkeit durch 3.", "59 hat nur die Teiler 1 und 59. 51 = 3 · 17, 57 = 3 · 19, und die 1 ist keine Primzahl."),
    lambda: 51 == 3 * 17 and 57 == 3 * 19 and all(59 % p for p in (2, 3, 5, 7)), {0: ("fb.bausteine.eins_als_primzahl", "die 1 als Primzahl gezählt"), 1: (None, "Teilbarkeit durch 3 nicht geprüft (Quersumme 6)"), 2: (None, "Teilbarkeit durch 3 nicht geprüft (Quersumme 12)")})
neu("z2", T, "A", "teiler", 2, "mehrschritt", BAU, "ja",
    zahl("Wie viele verschiedene Teiler hat die Zahl 36?", 9, "2 * 4 + 1",
         "Schreib die Teilerpaare auf. Achte auf das Paar 6 · 6.", "Paare: 1 · 36, 2 · 18, 3 · 12, 4 · 9, 6 · 6. Das sind 4 Paare mit je zwei Teilern und die 6 nur einmal: 9 Teiler."),
    ["len([1,2,3,4,6,9,12,18,36])"], [(10, None, "die 6 doppelt gezählt"), (5, None, "Paare statt Teiler gezählt"), (8, None, "die 6 ganz weggelassen")])
neu("z2", T, "A", "vielfache", 2, "mehrschritt", BAU, "ja",
    zahl("Welches ist die kleinste Zahl, die sowohl in der Sechserreihe als auch in der Achterreihe vorkommt?", 24, "6 * 8 // 2",
         "Schreib die Achterreihe auf und prüfe jede Zahl auf Teilbarkeit durch 6.", "Achterreihe: 8, 16, 24 … Die 24 ist auch 4 · 6. Kleiner geht es nicht."),
    ["min(24,48)"], [(48, None, "6 · 8 genommen – das ist ein gemeinsames Vielfaches, aber nicht das kleinste"), (2, None, "den größten gemeinsamen Teiler genannt"), (14, None, "6 + 8 gerechnet")])
neu("z2", T, 17, "endziffer", 2, "umkehr", BAU, "ja",
    zahl("Die vierstellige Zahl 473□ soll durch 2 und durch 5 teilbar sein. Welche Ziffer gehört in das Kästchen?", 0, "0",
         "Welche Endziffern passen zur 5? Welche davon ist gerade?", "Durch 5: Endziffer 0 oder 5. Durch 2: gerade. Beides zusammen: nur die 0."),
    ["4730-4730"], [(5, None, "nur die Regel für 5 beachtet"), (2, None, "nur die Regel für 2 beachtet")])
neu("z2", T, 17, "quersumme", 2, "umkehr", BAU, "ja",
    zahl("Welches ist die kleinste Ziffer für das Kästchen, damit 82□4 durch 3 teilbar ist?", 1, "15 - (8 + 2 + 4)",
         "Bilde die Quersumme ohne das Kästchen. Wie viel fehlt bis zur nächsten Zahl der Dreierreihe?", "8 + 2 + 4 = 14. Bis 15 fehlt 1. Probe: 8 214 hat die Quersumme 15."),
    ["15-14"], [(4, None, "bis 18 ergänzt – das passt, ist aber nicht die kleinste Ziffer"), (0, "fb.bausteine.endziffer_statt_quersumme", "nicht mit der Quersumme geprüft"), (2, None, "bis 16 ergänzt")])
neu("z2", T, 17, "neunerregel", 2, "umkehr", BAU, "ja",
    zahl("Welche Ziffer gehört in das Kästchen, damit 4□31 durch 9 teilbar ist?", 1, "9 - (4 + 3 + 1)",
         "Die Quersumme muss in der Neunerreihe liegen.", "4 + 3 + 1 = 8. Bis 9 fehlt 1. Probe: 4 131 hat die Quersumme 9."),
    ["9-8"], [(4, "fb.bausteine.aus_drei_folgt_neun", "auf Quersumme 12 ergänzt: durch 3 teilbar, aber nicht durch 9"), (9, None, "die 9 selbst eingesetzt"), (8, None, "die Quersumme genannt")])
neu("z2", T, "A", "primzahl", 2, "mehrschritt", BAU, "ja",
    zahl("Wie viele Primzahlen liegen zwischen 20 und 40?", 4, "4",
         "Streiche erst alle geraden Zahlen, dann die Vielfachen von 3 und von 5.", "Es bleiben 23, 29, 31 und 37."),
    ["len([p for p in range(21,40) if all(p%q for q in range(2,p))])"], [(5, None, "eine zusammengesetzte Zahl mitgezählt, zum Beispiel 27 oder 39"), (3, None, "eine Primzahl übersehen"), (6, None, "zwei zusammengesetzte Zahlen mitgezählt")])
neu("z2", T, 17, "primfaktoren", 2, "umkehr", BAU, "ja",
    zahl("Eine Zahl hat die Primfaktorzerlegung 2 · 3 · 3 · 5. Welche Zahl ist es?", 90, "2 * 3 * 3 * 5",
         "Nimm die Primfaktoren wieder mal.", "2 · 3 = 6, 6 · 3 = 18, 18 · 5 = 90."),
    ["6*15"], [(13, None, "addiert statt malgenommen"), (30, None, "eine 3 vergessen")])
neu("z2", T, 12, "neunerregel", 3, "fehler", BAU, "ja",
    wahl("Jemand sagt: „7 263 ist durch 3 teilbar, also ist die Zahl auch durch 9 teilbar.“ Was stimmt?",
         ["Die Zahl ist durch 3, aber nicht durch 9 teilbar.", "Die Begründung stimmt: Jede Zahl, die durch 3 teilbar ist, ist auch durch 9 teilbar.",
          "Die Zahl ist durch 9 teilbar, aber die Begründung ist falsch: Aus „durch 3“ folgt nicht „durch 9“.", "Die Zahl ist weder durch 3 noch durch 9 teilbar."], 2,
         "Prüfe zwei Dinge getrennt: die Zahl und die Begründung.", "Quersumme 7 + 2 + 6 + 3 = 18, also ist 7 263 durch 9 teilbar. Die Begründung stimmt trotzdem nicht: 12 ist durch 3 teilbar, aber nicht durch 9."),
    lambda: 7263 % 9 == 0 and 12 % 3 == 0 and 12 % 9 != 0, {0: (None, "Quersumme 18 nicht geprüft"), 1: ("fb.bausteine.aus_drei_folgt_neun", "aus „durch 3“ auf „durch 9“ geschlossen"), 3: (None, "Quersumme falsch gebildet")})
neu("z2", T, 14, "primfaktoren", 3, "verknuepfen", BAU, "ja",
    zahl("Zwei Wege, die Zahl 60 zu zerlegen. Weg A beginnt mit 60 = 6 · 10, Weg B mit 60 = 4 · 15. Beide werden zu Ende geführt, bis nur Primzahlen dastehen. Wie oft kommt die 2 am Ende vor?", 2, "2",
         "Führe beide Wege zu Ende. Vergleiche die Primfaktoren.", "Weg A: 6 · 10 = 2 · 3 · 2 · 5. Weg B: 4 · 15 = 2 · 2 · 3 · 5. Beide Male kommt die 2 zweimal vor."),
    ["sum(1 for p in (2,2,3,5) if p==2)"], [(1, "fb.bausteine.nicht_zu_ende_zerlegt", "die 4 oder die 6 nicht weiter zerlegt"), (3, None, "eine 2 zu viel gezählt")])
neu("z2", T, "V", "teiler", 1, "direkt", BAU, "ja",
    bed("Nenne zwei verschiedene Zahlen, die beide größer als 1 sind und deren Produkt 48 ist.", [G, G],
        [("beide größer als 1", UND([">", "$1", 1], [">", "$2", 1]), None, "Beide Zahlen sollen größer als 1 sein."), ("Produkt ist 48", ["=", ["*", "$1", "$2"], 48], ["*", "$1", "$2"], "Dein Produkt ist {}.")],
        [6, 8], [([1, 48], "beide größer als 1"), ([6, 9], "Produkt ist 48"), ([-6, -8], "beide größer als 1")],
        "Such ein Teilerpaar von 48.", "Teilerpaare von 48 ohne die 1: 2 · 24, 3 · 16, 4 · 12, 6 · 8.", gut=[[2, 24], [16, 3]]), None, None)
neu("z2", T, "V", "quersumme", 2, "umkehr", BAU, "ja",
    bed("Nenne eine dreistellige Zahl, die durch 3, aber nicht durch 9 teilbar ist.", [G],
        [("dreistellig", UND([">=", "$1", 100], ["<=", "$1", 999]), "$1", "Deine Zahl {} ist nicht dreistellig."), ("durch 3 teilbar", ["teilbar", "$1", 3], None, "Deine Zahl lässt beim Teilen durch 3 einen Rest."),
         ("nicht durch 9 teilbar", ["nicht", ["teilbar", "$1", 9]], None, "Deine Zahl ist auch durch 9 teilbar.")],
        [123], [([12], "dreistellig"), ([124], "durch 3 teilbar"), ([126], "nicht durch 9 teilbar")],
        "Was muss für die Quersumme gelten?", "Die Quersumme muss in der Dreierreihe liegen, aber nicht in der Neunerreihe – zum Beispiel 6: 123.", gut=[[102], [996]]), None, None)
neu("z2", T, "V", "vielfache", 2, "umkehr", BAU, "ja",
    bed("Nenne zwei Zahlen zwischen 10 und 50, die beide Vielfache von 6 sind und sich um genau 18 unterscheiden.", [G, G],
        [("zwischen 10 und 50", UND([">", "$1", 10], ["<", "$1", 50], [">", "$2", 10], ["<", "$2", 50]), None, "Beide Zahlen sollen zwischen 10 und 50 liegen."),
         ("Vielfache von 6", UND(["teilbar", "$1", 6], ["teilbar", "$2", 6]), None, "Mindestens eine deiner Zahlen steht nicht in der Sechserreihe."),
         ("Unterschied 18", ["=", ["betrag", ["-", "$1", "$2"]], 18], ["betrag", ["-", "$1", "$2"]], "Deine Zahlen unterscheiden sich um {}.")],
        [12, 30], [([6, 24], "zwischen 10 und 50"), ([12, 31], "Vielfache von 6"), ([12, 24], "Unterschied 18")],
        "Schreib die Sechserreihe zwischen 10 und 50 auf.", "Sechserreihe: 12, 18, 24, 30, 36, 42, 48. Drei Schritte weiter sind 18 mehr: 12 und 30, 18 und 36, 24 und 42, 30 und 48.", gut=[[48, 30], [18, 36]]), None, None)
neu("z2", T, "V", "endziffer", 3, "verknuepfen", BAU, "ja",
    bed("Nenne eine Zahl zwischen 100 und 200, die durch 2, durch 3 und durch 5 teilbar ist.", [G],
        [("zwischen 100 und 200", UND([">", "$1", 100], ["<", "$1", 200]), "$1", "Deine Zahl {} liegt nicht zwischen 100 und 200."), ("durch 2 und durch 5 teilbar", UND(["teilbar", "$1", 2], ["teilbar", "$1", 5]), None, "Schau auf die letzte Ziffer deiner Zahl."),
         ("durch 3 teilbar", ["teilbar", "$1", 3], None, "Schau auf die Quersumme deiner Zahl.")],
        [150], [([90], "zwischen 100 und 200"), ([135], "durch 2 und durch 5 teilbar"), ([140], "durch 3 teilbar")],
        "Welche Endziffer passt zu 2 und zu 5 zugleich?", "Endziffer 0 und eine Quersumme aus der Dreierreihe: 120, 150 oder 180.", gut=[[120], [180]]), None, None)
PRIM = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
ist_prim = lambda feld: ["oder", ["oder", *[["=", feld, p] for p in PRIM[:5]]], ["oder", *[["=", feld, p] for p in PRIM[5:]]]]      # „oder“ nimmt höchstens sechs Glieder
neu("z2", T, "V", "primzahl", 3, "transfer", BAU, "ja",
    bed("Nenne drei verschiedene Primzahlen, deren Summe 30 ist.", [G, G, G],
        [("erste Zahl ist eine Primzahl", ist_prim("$1"), "$1", "Deine erste Zahl {} ist keine Primzahl unter 30."), ("zweite Zahl ist eine Primzahl", ist_prim("$2"), "$2", "Deine zweite Zahl {} ist keine Primzahl unter 30."),
         ("dritte Zahl ist eine Primzahl", ist_prim("$3"), "$3", "Deine dritte Zahl {} ist keine Primzahl unter 30."), ("verschieden", ["verschieden", "$alle"], None, "Die drei Zahlen sollen verschieden sein."),
         ("Summe ist 30", ["=", ["summe", "$alle"], 30], ["summe", "$alle"], "Deine Summe ist {}.")],
        [2, 5, 23], [([1, 6, 23], "erste Zahl ist eine Primzahl"), ([2, 9, 19], "zweite Zahl ist eine Primzahl"), ([2, 7, 21], "dritte Zahl ist eine Primzahl"), ([2, 2, 23], "verschieden"), ([3, 5, 23], "Summe ist 30")],
        "Drei ungerade Zahlen ergeben zusammen eine ungerade Zahl. Was heißt das für die Summe 30?", "Eine der drei Primzahlen muss gerade sein, also die 2. Die beiden anderen ergeben zusammen 28: 5 + 23 oder 11 + 17.", gut=[[11, 2, 17]]), None, None)

# ═════════════════════ Kind 2 · Flug ge2 · Spiegeln und Symmetrie (Klasse 7) ═════════════════════
T = "abbildungen.kongruenz"
neu("ge2", T, 4, "achsenspiegelung", 1, "direkt", DECK, "nein",
    luecken("Spiegle P(5 | 2) an der senkrechten Achse durch (1 | 0). P liegt ① Einheiten rechts von der Achse. Der Bildpunkt liegt gleich weit links davon: x′ = ②. Die Höhe bleibt: y′ = ③.", K(3), [4, -3, 2],
            ["5 - 1", "1 - (5 - 1)", "2"], "Gleich weit auf die andere Seite der Achse.", "5 − 1 = 4. Von der Achse 4 nach links: 1 − 4 = −3. Also P′(−3 | 2)."),
    ["4", "2*1-5", "2"], {1: [(-5, "fb.deckungsgleich.an_koordinatenachse_gespiegelt", "an der y-Achse statt an der genannten Achse gespiegelt"), (-4, None, "von 0 statt von der Achse aus gezählt")], 2: [(-2, "fb.deckungsgleich.falsche_koordinate_gespiegelt", "auch die Höhe gespiegelt")]})
neu("ge2", T, "A", "winkelhalbierende", 1, "direkt", ABST, "ja",
    zahl("Ein Winkel hat 76°. Seine Winkelhalbierende teilt ihn in zwei Teile. Wie viel Grad hat jeder Teil?", 38, "76 // 2",
         "Halbieren heißt: zwei gleich große Teile.", "Die Winkelhalbierende teilt den Winkel in zwei gleich große Teile: 76° : 2 = 38°."), ["76/2"], [(152, "fb.verhaeltnis.falsche_richtung", "verdoppelt statt halbiert")])
neu("ge2", T, 4, "verschiebung", 1, "direkt", DECK, "nein",
    luecken("Verschiebe A(3 | −1) mit dem Vektor (−5 | 4). Bildpunkt A′(① | ②).", "A′(□ | □)", [-2, 3], ["3 + (-5)", "-1 + 4"],
            "Erste Zahl zu x, zweite Zahl zu y.", "3 + (−5) = −2 und −1 + 4 = 3. Also A′(−2 | 3).", "Erst x, dann y."),
    ["3-5", "4-1"], {0: [(8, "fb.plusminus.doppelminus_uebersehen", "3 − (−5) gerechnet: abgezogen statt addiert"), (2, "fb.plusminus.zeichen_des_ergebnisses", "5 − 3 gerechnet")], 1: [(-5, None, "abgezogen statt addiert"), (-3, "fb.plusminus.zeichen_des_ergebnisses", "Vorzeichen des Ergebnisses falsch")]})
neu("ge2", T, 12, "symmetrie", 1, "erkennen", DECK, "ja",
    wahl("Wie viele Symmetrieachsen hat ein Rechteck, das kein Quadrat ist?", ["keine", "2", "4", "1"], 1,
         "Stell dir vor, du faltest das Rechteck. Wann liegen die Hälften genau aufeinander?", "Nur die beiden Mittellinien sind Achsen. Faltet man an einer Diagonale, passen die Hälften nicht aufeinander."),
    lambda: True, {0: (None, "Mittellinien übersehen"), 2: ("fb.deckungsgleich.diagonale_als_achse", "die Diagonalen mitgezählt"), 3: (None, "nur eine Mittellinie gesehen")})
neu("ge2", T, 12, "eigenschaften", 1, "erkennen", DECK, "ja",
    wahl("Ein Dreieck ABC wird an einer Achse gespiegelt. Was ändert sich dabei?", ["die Seitenlängen", "die Winkelgrößen", "der Flächeninhalt", "der Umlaufsinn"], 3,
         "Was bleibt bei jeder Kongruenzabbildung gleich?", "Längen, Winkel und Flächeninhalt bleiben. Nur der Umlaufsinn dreht sich um: A, B, C laufen nach dem Spiegeln andersherum."),
    lambda: True, {0: (None, "Längen bleiben erhalten"), 1: (None, "Winkel bleiben erhalten"), 2: (None, "der Flächeninhalt bleibt erhalten")})
neu("ge2", T, 14, "achsenspiegelung", 2, "mehrschritt", DECK, "ja",
    zahl("P(−3 | 4) wird an der waagrechten Achse durch (0 | 1) gespiegelt. Weg A: P liegt 3 über der Achse, also liegt P′ 3 darunter. Weg B: y′ = 2 · 1 − 4. Welche y-Koordinate hat P′?", -2, "2 * 1 - 4",
         "Rechne beide Wege. Sie müssen dasselbe ergeben.", "Weg A: 1 − 3 = −2. Weg B: 2 − 4 = −2. Also P′(−3 | −2)."),
    ["1-(4-1)"], [(-4, "fb.deckungsgleich.an_koordinatenachse_gespiegelt", "an der x-Achse gespiegelt"), (2, "fb.plusminus.zeichen_des_ergebnisses", "Vorzeichen verloren"), (3, "fb.deckungsgleich.falsche_koordinate_gespiegelt", "die x-Koordinate gespiegelt")])
neu("ge2", T, 4, "punktspiegelung", 2, "mehrschritt", DECK, "folge",
    luecken("Spiegle P(1 | −2) am Punkt Z(4 | 1). Von P zu Z geht es ① nach rechts und ② nach oben. Denselben Weg noch einmal von Z aus: P′(③ | ④).", K(4), [3, 3, 7, 4],
            ["4 - 1", "1 - (-2)", "4 + 3", "1 + 3"], "Z ist die Mitte zwischen P und P′.", "Von P zu Z: 3 nach rechts, 3 nach oben. Von Z weiter: (4 + 3 | 1 + 3) = (7 | 4)."),
    ["3", "1+2", "2*4-1", "2*1+2"], {1: [(-1, "fb.plusminus.doppelminus_uebersehen", "1 − 2 gerechnet"), (1, "fb.plusminus.doppelminus_uebersehen", "Betrag von 1 − 2")], 2: [(-1, "fb.deckungsgleich.an_koordinatenachse_gespiegelt", "am Ursprung statt an Z gespiegelt")], 3: [(2, "fb.deckungsgleich.an_koordinatenachse_gespiegelt", "am Ursprung statt an Z gespiegelt")]})
neu("ge2", T, 17, "punktspiegelung", 2, "umkehr", ABST, "ja",
    zahl("Bei einer Punktspiegelung fällt P(−6 | 3) auf P′(2 | 3). Welche x-Koordinate hat das Zentrum Z?", -2, "(-6 + 2) // 2",
         "Z liegt genau in der Mitte zwischen P und P′.", "Mitte von −6 und 2: (−6 + 2) : 2 = −2."),
    ["-6+(2-(-6))/2"], [(4, "fb.abstand.halbe_laenge_statt_mitte", "die halbe Entfernung genannt"), (-4, "fb.plusminus.zeichen_des_ergebnisses", "(−6 − 2) : 2 gerechnet"), (8, None, "die ganze Entfernung genannt")])
neu("ge2", T, "A", "mittelsenkrechte", 2, "mehrschritt", ABST, "ja",
    zahl("A(−1 | 2) und B(7 | 2). Die Mittelsenkrechte von [AB] ist eine senkrechte Linie. Durch welchen x-Wert geht sie?", 3, "(-1 + 7) // 2",
         "Die Mittelsenkrechte geht durch die Mitte der Strecke.", "Die Strecke ist 8 lang. Von −1 aus 4 weiter: x = 3."),
    ["-1+(7-(-1))/2"], [(4, "fb.abstand.halbe_laenge_statt_mitte", "die halbe Streckenlänge genannt"), (8, None, "die Streckenlänge genannt")])
neu("ge2", T, 17, "gegenvektor", 2, "umkehr", DECK, "folge",
    luecken("Ein Punkt B wurde mit dem Vektor (4 | −7) verschoben und liegt jetzt bei B′(1 | 2). Der Gegenvektor ist (① | ②). Damit kommst du zurück: B(③ | ④).", K(4), [-4, 7, -3, 9],
            ["0 - 4", "0 - (-7)", "1 - 4", "2 - (-7)"], "Der Gegenvektor dreht beide Vorzeichen um.", "Gegenvektor (−4 | 7). Zurück: 1 − 4 = −3 und 2 + 7 = 9. Also B(−3 | 9)."),
    ["-4", "7", "1+(-4)", "2+7"], {1: [(-7, None, "nur das erste Vorzeichen umgedreht")], 2: [(5, None, "noch einmal in dieselbe Richtung verschoben")], 3: [(-5, "fb.plusminus.doppelminus_uebersehen", "noch einmal −7 gerechnet")]})
neu("ge2", T, "A", "drehung", 2, "mehrschritt", DECK, "ja",
    luecken("Drehe P(3 | 1) um den Ursprung um 90° nach links (gegen den Uhrzeigersinn). Bildpunkt P′(□ | □).", "P′(□ | □)", [-1, 3], ["0 - 1", "3"],
            "Aus (x | y) wird (−y | x).", "Aus (3 | 1) wird (−1 | 3). Probe mit einer Skizze: P liegt rechts, P′ liegt oben.", "Erst x, dann y."),
    ["-1", "3"], {0: [(1, "fb.deckungsgleich.drehrichtung", "nach rechts gedreht"), (-3, None, "um 180° gedreht")], 1: [(-3, "fb.deckungsgleich.drehrichtung", "nach rechts gedreht"), (-1, None, "um 180° gedreht")]})
neu("ge2", T, 17, "achsenspiegelung", 3, "rueckwaerts", ABST, "ja",
    zahl("P(2 | 7) wird an einer waagrechten Achse gespiegelt und fällt auf P′(2 | −1). Durch welchen y-Wert geht die Achse?", 3, "(7 + (-1)) // 2",
         "Die Achse liegt genau in der Mitte zwischen P und P′.", "Mitte von 7 und −1: (7 − 1) : 2 = 3. Probe: P liegt 4 darüber, P′ 4 darunter."),
    ["7-(7-(-1))/2"], [(4, "fb.abstand.halbe_laenge_statt_mitte", "den halben Abstand genannt"), (8, None, "den ganzen Abstand genannt"), (0, "fb.deckungsgleich.an_koordinatenachse_gespiegelt", "die x-Achse angenommen")])
neu("ge2", T, 12, "mittelsenkrechte", 3, "begruenden", ABST, "ja",
    wahl("Der Punkt P liegt auf der Mittelsenkrechten von [AB]. Welche Aussage stimmt dann sicher?",
         ["P ist die Mitte von [AB].", "P liegt auf der Strecke [AB].", "P ist von A und von B gleich weit entfernt.", "Das Dreieck ABP hat bei P einen rechten Winkel."], 2,
         "Welche Eigenschaft haben alle Punkte der Mittelsenkrechten?", "Jeder Punkt der Mittelsenkrechten ist von A und B gleich weit entfernt. Die Mitte ist nur einer davon."),
    lambda: 2 ** 2 + 3 ** 2 == (2 - 4) ** 2 + 3 ** 2, {0: (None, "nur einen Punkt der Linie betrachtet"), 1: (None, "nur einen Punkt der Linie betrachtet"), 3: (None, "der rechte Winkel liegt an der Strecke, nicht bei P")})
neu("ge2", T, 13, "vierecke_ordnen", 3, "begruenden", DECK, "ja",
    wahl("Welches Viereck ist immer punktsymmetrisch, hat aber im Allgemeinen keine Symmetrieachse?", ["Parallelogramm", "Drachenviereck", "gleichschenkliges Trapez", "Raute"], 0,
         "Punktsymmetrisch heißt: Nach einer halben Drehung sieht die Figur gleich aus.", "Ein Parallelogramm geht bei einer halben Drehung um seinen Mittelpunkt in sich über. Achsen hat es nur in Sonderfällen (Rechteck, Raute)."),
    lambda: True, {1: (None, "Drachenviereck: eine Achse, nicht punktsymmetrisch"), 2: (None, "gleichschenkliges Trapez: eine Achse, nicht punktsymmetrisch"), 3: (None, "Raute: punktsymmetrisch, hat aber zwei Achsen")})
neu("ge2", T, "V", "achsenspiegelung", 1, "direkt", DECK, "ja",
    bed("Nenne einen Punkt P(x | y), der nicht auf der y-Achse liegt, und sein Spiegelbild P′(x′ | y′) bei der Spiegelung an der y-Achse. Reihenfolge der Felder: x, y, x′, y′.", [G, G, G, G],
        [("P nicht auf der Achse", ["!=", "$1", 0], None, "Dein Punkt P liegt auf der Achse."), ("y′ gehört zum Spiegelbild", ["=", "$2", "$4"], None, "P und P′ liegen bei dir nicht auf gleicher Höhe."),
         ("x′ gehört zum Spiegelbild", ["=", ["+", "$1", "$3"], 0], None, "P′ liegt bei dir nicht gleich weit auf der anderen Seite der Achse.")],
        [3, 2, -3, 2], [([0, 2, 0, 2], "P nicht auf der Achse"), ([3, 2, -3, -2], "y′ gehört zum Spiegelbild"), ([3, 2, 3, 2], "x′ gehört zum Spiegelbild")],
        "Welche Koordinate ändert sich beim Spiegeln an der y-Achse?", "Die y-Koordinate bleibt, die x-Koordinate wechselt das Vorzeichen: zum Beispiel P(3 | 2) und P′(−3 | 2).", gut=[[-5, 0, 5, 0]]), None, None)
neu("ge2", T, "V", "verschiebung", 2, "umkehr", DECK, "ja",
    bed("Nenne einen Vektor (a | b), der den Punkt P(2 | −1) in das Feld links oben verschiebt: Der Bildpunkt soll eine negative x-Koordinate und eine positive y-Koordinate haben. Beide Zahlen des Vektors sollen zwischen −5 und 5 liegen.", [G, G],
        [("zwischen −5 und 5", UND([">=", "$1", -5], ["<=", "$1", 5], [">=", "$2", -5], ["<=", "$2", 5]), None, "Beide Zahlen des Vektors sollen zwischen −5 und 5 liegen."),
         ("Bildpunkt links der y-Achse", ["<", ["+", 2, "$1"], 0], ["+", 2, "$1"], "Dein Bildpunkt hat die x-Koordinate {}."), ("Bildpunkt über der x-Achse", [">", ["+", -1, "$2"], 0], ["+", -1, "$2"], "Dein Bildpunkt hat die y-Koordinate {}.")],
        [-4, 3], [([-9, 3], "zwischen −5 und 5"), ([-2, 3], "Bildpunkt links der y-Achse"), ([-4, 1], "Bildpunkt über der x-Achse")],
        "Wie weit muss P mindestens nach links, wie weit mindestens nach oben?", "Mehr als 2 nach links (a ist −3, −4 oder −5) und mehr als 1 nach oben (b ist 2, 3, 4 oder 5).", gut=[[-3, 2], [-5, 5]]), None, None)
abst2 = lambda x, y, px: ["+", ["hoch", ["-", x, px], 2], ["hoch", y, 2]]
neu("ge2", T, "V", "mittelsenkrechte", 2, "umkehr", ABST, "ja",
    bed("A(0 | 0) und B(6 | 0). Nenne zwei verschiedene Punkte, die von A und von B gleich weit entfernt sind. Reihenfolge der Felder: x und y des ersten Punkts, x und y des zweiten Punkts.", [G, G, G, G],
        [("erster Punkt gleich weit", ["=", abst2("$1", "$2", 0), abst2("$1", "$2", 6)], None, "Dein erster Punkt ist von A und B nicht gleich weit entfernt."),
         ("zweiter Punkt gleich weit", ["=", abst2("$3", "$4", 0), abst2("$3", "$4", 6)], None, "Dein zweiter Punkt ist von A und B nicht gleich weit entfernt."),
         ("verschieden", ["oder", ["!=", "$1", "$3"], ["!=", "$2", "$4"]], None, "Die zwei Punkte sollen verschieden sein.")],
        [3, 1, 3, -2], [([2, 1, 3, -2], "erster Punkt gleich weit"), ([3, 1, 4, 0], "zweiter Punkt gleich weit"), ([3, 1, 3, 1], "verschieden")],
        "Auf welcher Linie liegen alle Punkte, die von A und B gleich weit entfernt sind?", "Alle solchen Punkte liegen auf der Mittelsenkrechten von [AB], also bei x = 3: zum Beispiel (3 | 1) und (3 | −2).", gut=[[3, 0, 3, 100]]), None, None)
neu("ge2", T, "V", "achsenspiegelung", 2, "umkehr", ABST, "ja",
    bed("A(1 | 4) wird an einer senkrechten Achse gespiegelt. Nenne den x-Wert der Achse und den Bildpunkt A′(x′ | y′) so, dass A′ links von der y-Achse liegt. Reihenfolge der Felder: x-Wert der Achse, x′, y′.", [R, G, G],
        [("Bildpunkt links der y-Achse", ["<", "$2", 0], "$2", "Dein x′ ist {}."), ("y′ gehört zum Spiegelbild", ["=", "$3", 4], "$3", "Dein y′ ist {}."),
         ("Achse passt zu A und A′", ["=", ["*", 2, "$1"], ["+", 1, "$2"]], ["/", ["+", 1, "$2"], 2], "Die Mitte zwischen A und deinem A′ liegt bei x = {}.")],
        [-1, -3, 4], [([2, 3, 4], "Bildpunkt links der y-Achse"), ([-1, -3, -4], "y′ gehört zum Spiegelbild"), ([0, -3, 4], "Achse passt zu A und A′")],
        "Wähle zuerst A′. Wo muss dann die Achse liegen?", "Die Achse liegt in der Mitte zwischen A und A′. Zum Beispiel A′(−3 | 4): Mitte von 1 und −3 ist −1.", gut=[["-0,5", -2, 4], [0, -1, 4]]), None, None)
neu("ge2", T, "V", "punktspiegelung", 3, "parameter", ABST, "ja",
    bed("Bei einer Punktspiegelung am Zentrum Z(a | b) fällt der Punkt P(x | y) auf P′(4 | 0). Nenne Z und P so, dass P im Feld links unten liegt (beide Koordinaten negativ). Reihenfolge der Felder: a, b, x, y.", [R, R, G, G],
        [("P links unten", UND(["<", "$3", 0], ["<", "$4", 0]), None, "Dein Punkt P liegt nicht im Feld links unten."),
         ("Z passt zu P und P′ (x-Richtung)", ["=", ["*", 2, "$1"], ["+", "$3", 4]], ["/", ["+", "$3", 4], 2], "Die Mitte zwischen deinem P und P′ liegt bei x = {}."),
         ("Z passt zu P und P′ (y-Richtung)", ["=", ["*", 2, "$2"], "$4"], ["/", "$4", 2], "Die Mitte zwischen deinem P und P′ liegt bei y = {}.")],
        [1, -1, -2, -2], [([1, -1, 2, -2], "P links unten"), ([2, -1, -2, -2], "Z passt zu P und P′ (x-Richtung)"), ([1, 1, -2, -2], "Z passt zu P und P′ (y-Richtung)")],
        "Wähle zuerst P. Das Zentrum liegt dann in der Mitte zwischen P und P′.", "Zum Beispiel P(−2 | −2): Mitte von −2 und 4 ist 1, Mitte von −2 und 0 ist −1. Also Z(1 | −1).", gut=[["1,5", "-0,5", -1, -1]]), None, None)

# ═════════════════════ Kind 2 · Flug a4 · Lineare Ungleichungen (Klasse 8) ═════════════════════
T, I = "gleichungen.ungleichungen", "zahlen.intervalle"
neu("a4", T, 4, "umformen", 1, "direkt", WAAGE, "nein",
    luecken("Löse Schritt für Schritt: 3x − 7 < 11. Plus 7 auf beiden Seiten: 3x < ①. Geteilt durch 3 auf beiden Seiten: x < ②.", K(2), [18, 6], ["11 + 7", "18 // 3"],
            "Wie bei einer Gleichung. Das Zeichen bleibt, weil du durch eine positive Zahl teilst.", "11 + 7 = 18 und 18 : 3 = 6. Also x < 6."),
    ["18", "(11+7)/3"], {0: [(4, "fb.gegenrechnung.gleiche_rechnung", "noch einmal 7 abgezogen statt addiert")], 1: [(15, None, "3 abgezogen statt durch 3 geteilt")]})
neu("a4", T, 4, "umdrehen", 1, "direkt", WAAGE, "nein",
    luecken("Löse: −4x ≥ 20. Geteilt durch −4 auf beiden Seiten; weil −4 negativ ist, dreht sich das Zeichen um: x ≤ ①.", K(1), [-5], ["20 // (-4)"],
            "Plus durch Minus ergibt Minus.", "20 : (−4) = −5. Also x ≤ −5. Probe mit x = −6: −4 · (−6) = 24, und 24 ≥ 20 stimmt."),
    ["-(20/4)"], {0: [(5, "fb.vorzeichen.falsches_zeichen", "20 : (−4) als 5 gerechnet")]})
neu("a4", T, 12, "pruefen", 1, "erkennen", LOES, "ja",
    wahl("Welche dieser Zahlen ist eine Lösung von 2x − 5 > 3?", ["−4", "0", "4", "5"], 3,
         "Setz jede Zahl ein und vergleiche.", "2 · 5 − 5 = 5, und 5 > 3 stimmt. Für x = 4 kommt genau 3 heraus, und 3 > 3 stimmt nicht."),
    lambda: [x for x in (-4, 0, 4, 5) if 2 * x - 5 > 3] == [5], {0: (None, "Vorzeichen beim Einsetzen übersehen"), 1: (None, "nicht eingesetzt"), 2: ("fb.gleichung_loesen.grenze_mitgezaehlt", "die Grenze als Lösung genommen")})
neu("a4", I, 12, "lesen", 1, "direkt", LOES, "ja",
    wahl("Was bedeutet das Intervall [−4; 7[ ?", ["−4 < x ≤ 7", "−4 ≤ x < 7", "−4 ≤ x ≤ 7", "−4 < x < 7"], 1,
         "Zeigt die Klammer zur Zahl hin, gehört die Grenze dazu.", "Links zeigt die Klammer zur −4: Sie gehört dazu. Rechts zeigt sie von der 7 weg: Die 7 gehört nicht dazu."),
    lambda: True, {0: ("fb.gleichung_loesen.klammer_falsch_herum", "beide Klammern verkehrt gelesen"), 2: ("fb.gleichung_loesen.klammer_falsch_herum", "rechte Klammer verkehrt gelesen"), 3: ("fb.gleichung_loesen.klammer_falsch_herum", "linke Klammer verkehrt gelesen")})
neu("a4", T, "A", "umdrehen", 2, "mehrschritt", WAAGE, "ja",
    wahl("Löse die Ungleichung −2x + 6 > 14.", ["x > −4", "x > 4", "x < 4", "x < −4"], 3,
         "Erst die 6 wegbringen. Dann durch die Zahl vor x teilen – achte auf ihr Vorzeichen.", "Minus 6: −2x > 8. Geteilt durch −2, das Zeichen dreht sich um: x < −4."),
    lambda: all((-2 * x + 6 > 14) == (x < -4) for x in range(-20, 20)), {0: ("fb.waage.zeichen_nicht_gedreht", "Zeichen nicht umgedreht"), 1: ("fb.vorzeichen.falsches_zeichen", "8 : (−2) als 4 gerechnet und Zeichen nicht umgedreht"), 2: ("fb.vorzeichen.falsches_zeichen", "8 : (−2) als 4 gerechnet")})
neu("a4", T, 4, "klammern", 2, "mehrschritt", WAAGE, "folge",
    luecken("Löse: 2 · (x − 3) > 5x + 9. Klammer auflösen: 2x − ① > 5x + 9. Minus 5x auf beiden Seiten: ② · x − 6 > 9. Plus 6: −3x > ③. Geteilt durch −3, Zeichen umdrehen: x < ④.", K(4), [6, -3, 15, -5],
            ["2 * 3", "2 - 5", "9 + 6", "15 // (-3)"], "Jede Zeile ändert nur eine Stelle.", "2 · 3 = 6. 2x − 5x = −3x. 9 + 6 = 15. 15 : (−3) = −5. Also x < −5."),
    ["6", "-(5-2)", "15", "-(15/3)"], {0: [(3, "fb.ausmultiplizieren.nur_erster_summand", "die 3 nicht mit 2 malgenommen")], 1: [(3, "fb.plusminus.zeichen_des_ergebnisses", "5 − 2 gerechnet"), (7, None, "5x addiert statt abgezogen")], 2: [(3, "fb.gegenrechnung.gleiche_rechnung", "6 abgezogen statt addiert")], 3: [(5, "fb.vorzeichen.falsches_zeichen", "15 : (−3) als 5 gerechnet")]})
neu("a4", T, "A", "pruefen", 2, "mehrschritt", LOES, "ja",
    zahl("Welche ist die kleinste ganze Zahl, die die Ungleichung 3x + 1 > 16 erfüllt?", 6, "(16 - 1) // 3 + 1",
         "Löse erst die Ungleichung. Gehört die Grenze dazu?", "3x > 15, also x > 5. Die 5 selbst gehört nicht dazu. Die kleinste ganze Zahl ist 6."),
    ["min(x for x in range(-50,50) if 3*x+1>16)"], [(5, "fb.gleichung_loesen.grenze_mitgezaehlt", "die Grenze selbst genannt"), (4, None, "in die falsche Richtung gegangen")])
neu("a4", T, "A", "intervall", 2, "darstellung", LOES, "ja",
    wahl("Löse −x ≤ 2 und gib die Lösungsmenge als Intervall an.", ["]−∞; −2]", "[−2; ∞[", "]−2; ∞[", "]−∞; 2]"], 1,
         "Mal (−1) auf beiden Seiten – was passiert mit dem Zeichen?", "Mal (−1), Zeichen umdrehen: x ≥ −2. Die −2 gehört dazu, nach rechts geht es unbegrenzt: [−2; ∞[."),
    lambda: all((-x <= 2) == (x >= -2) for x in range(-20, 20)), {0: ("fb.waage.zeichen_nicht_gedreht", "Zeichen nicht umgedreht"), 2: ("fb.gleichung_loesen.klammer_falsch_herum", "Grenze ausgeschlossen, obwohl ≤ dasteht"), 3: (None, "nur das Minus vor x weggelassen")})
neu("a4", T, "A", "sachaufgabe", 2, "einkleidung", LOES, "ja",
    zahl("Ein Lastenaufzug trägt höchstens 600 kg. Der leere Transportwagen wiegt 60 kg, jede Kiste 45 kg. Wie viele Kisten dürfen höchstens auf den Wagen?", 12, "(600 - 60) // 45",
         "Stell die Ungleichung auf: Wagen plus Kisten ist höchstens 600.", "60 + 45 · n ≤ 600, also 45 · n ≤ 540 und n ≤ 12. Mit 12 Kisten sind es genau 600 kg – das ist erlaubt."),
    ["max(n for n in range(100) if 60+45*n<=600)"], [(13, None, "den Wagen vergessen: 600 : 45"), (11, "fb.gleichung_loesen.grenze_mitgezaehlt", "die Grenze 12 ausgeschlossen, obwohl „höchstens“ sie erlaubt"), (14, None, "den Wagen addiert statt abgezogen")])
neu("a4", I, "A", "enthalten", 2, "mehrschritt", LOES, "ja",
    zahl("Wie viele ganze Zahlen liegen im Intervall ]−3; 4]?", 7, "4 - (-3)",
         "Welche Grenze gehört dazu? Zähl dann von der kleinsten bis zur größten Zahl.", "−3 gehört nicht dazu, 4 gehört dazu: −2, −1, 0, 1, 2, 3, 4. Das sind 7 Zahlen."),
    ["len([x for x in range(-10,10) if -3<x<=4])"], [(8, "fb.gleichung_loesen.grenze_mitgezaehlt", "beide Grenzen mitgezählt"), (6, None, "beide Grenzen ausgeschlossen"), (1, "fb.plusminus.doppelminus_uebersehen", "4 − 3 gerechnet")])
neu("a4", I, "A", "schreiben", 2, "darstellung", LOES, "ja",
    wahl("x ist mindestens −1 und kleiner als 5. Wie schreibt man das als Intervall?", ["]−1; 5]", "[−1; 5]", "]−1; 5[", "[−1; 5["], 3,
         "„Mindestens“ heißt: Die Grenze gehört dazu.", "Mindestens −1: −1 ≤ x, Klammer zur Zahl. Kleiner als 5: x < 5, Klammer von der Zahl weg. Also [−1; 5[."),
    lambda: True, {0: ("fb.gleichung_loesen.klammer_falsch_herum", "beide Klammern vertauscht"), 1: ("fb.gleichung_loesen.klammer_falsch_herum", "die 5 eingeschlossen"), 2: ("fb.gleichung_loesen.klammer_falsch_herum", "die −1 ausgeschlossen")})
neu("a4", T, 12, "umdrehen", 3, "fehler", WAAGE, "ja",
    wahl("Jemand rechnet in drei Zeilen: (1) 5 − 3x ≤ 17 (2) −3x ≤ 12 (3) x ≤ −4. In welcher Zeile steht der erste Fehler?", ["in Zeile 2", "in Zeile 3", "in keiner Zeile"], 1,
         "Prüfe jeden Schritt: Was wurde auf beiden Seiten getan?", "Zeile 2 stimmt (minus 5). In Zeile 3 wird durch −3 geteilt; das Zeichen muss sich umdrehen: x ≥ −4."),
    lambda: 17 - 5 == 12 and all((5 - 3 * x <= 17) == (x >= -4) for x in range(-20, 20)), {0: (None, "den richtigen Schritt für falsch gehalten"), 2: ("fb.waage.zeichen_nicht_gedreht", "das fehlende Umdrehen nicht bemerkt")})
neu("a4", T, "A", "klammern", 3, "verknuepfen", MK, "ja",
    zahl("Löse 4 − (x + 2) ≤ 3x − 10. Die Lösung hat die Form x ≥ □. Gib die Zahl an.", 3, "(4 - 2 + 10) // (1 + 3)",
         "Lös erst die Klammer auf. Achte auf das Minus davor.", "4 − x − 2 ≤ 3x − 10, also 2 − x ≤ 3x − 10. Plus x, plus 10: 12 ≤ 4x. Geteilt durch 4: x ≥ 3."),
    ["12/4"], [(4, "fb.minusklammer.nur_erstes_zeichen", "4 − x + 2 gerechnet: nur das erste Zeichen gewechselt"), (-3, "fb.vorzeichen.falsches_zeichen", "Vorzeichen der Grenze falsch"), (6, None, "durch 2 statt durch 4 geteilt")])
neu("a4", I, 12, "beurteilen", 3, "begruenden", LOES, "ja",
    wahl("Welche Aussage über das Intervall ]2; 6] stimmt?", ["Die kleinste Zahl im Intervall ist 2.", "Die kleinste Zahl im Intervall ist 3.", "Es gibt keine kleinste Zahl im Intervall.", "Die größte Zahl im Intervall ist kleiner als 6."], 2,
         "Im Intervall liegen nicht nur ganze Zahlen.", "Die 2 gehört nicht dazu. Zu jeder Zahl knapp über 2 gibt es eine, die noch näher an 2 liegt (2,1, dann 2,01 …). Also gibt es keine kleinste."),
    lambda: True, {0: ("fb.gleichung_loesen.grenze_mitgezaehlt", "die ausgeschlossene Grenze mitgezählt"), 1: (None, "nur an ganze Zahlen gedacht"), 3: ("fb.gleichung_loesen.klammer_falsch_herum", "die eingeschlossene Grenze 6 ausgeschlossen")})
links = lambda feld: ["+", ["*", 2, feld], 3]
neu("a4", T, "V", "pruefen", 1, "direkt", LOES, "ja",
    bed("Nenne zwei verschiedene ganze Zahlen, die beide die Ungleichung 2x + 3 < 9 erfüllen. Mindestens eine davon soll negativ sein.", [G, G],
        [("verschieden", ["verschieden", "$alle"], None, "Die zwei Zahlen sollen verschieden sein."), ("erste Zahl erfüllt die Ungleichung", ["<", links("$1"), 9], links("$1"), "Mit deiner ersten Zahl hat die linke Seite den Wert {}."),
         ("zweite Zahl erfüllt die Ungleichung", ["<", links("$2"), 9], links("$2"), "Mit deiner zweiten Zahl hat die linke Seite den Wert {}."), ("mindestens eine negativ", [">=", ["anzahl_negativ", "$alle"], 1], None, "Keine deiner Zahlen ist negativ.")],
        [-2, 1], [([1, 1], "verschieden"), ([3, 1], "erste Zahl erfüllt die Ungleichung"), ([-2, 5], "zweite Zahl erfüllt die Ungleichung"), ([0, 2], "mindestens eine negativ")],
        "Setz deine Zahlen ein und vergleiche mit 9.", "2x < 6, also x < 3. Zum Beispiel −2 und 1.", gut=[[2, -100]]), None, None)
neu("a4", T, "V", "umdrehen", 2, "umkehr", WAAGE, "ja",
    bed("Nenne zuerst eine Zahl, die −3x > 6 erfüllt, und dann eine Zahl, die −3x > 6 nicht erfüllt.", [R, R],
        [("erste Zahl erfüllt die Ungleichung", [">", ["*", -3, "$1"], 6], ["*", -3, "$1"], "Mit deiner ersten Zahl ist −3x gleich {}."),
         ("zweite Zahl erfüllt sie nicht", ["nicht", [">", ["*", -3, "$2"], 6]], ["*", -3, "$2"], "Mit deiner zweiten Zahl ist −3x gleich {} – das ist größer als 6.")],
        [-5, 0], [([3, 0], "erste Zahl erfüllt die Ungleichung"), ([-2, 0], "erste Zahl erfüllt die Ungleichung"), ([-5, -4], "zweite Zahl erfüllt sie nicht")],
        "Rechne −3 mal deine Zahl und vergleiche mit 6.", "−3x > 6 heißt x < −2. Erfüllt: zum Beispiel −5. Nicht erfüllt: zum Beispiel 0 oder die Grenze −2 selbst.", gut=[["-2,5", -2]]), None, None)
neu("a4", I, "V", "enthalten", 2, "umkehr", LOES, "ja",
    bed("Nenne die Grenzen eines Intervalls [a; b] mit ganzen Zahlen a und b: Die 0 soll im Intervall liegen, und das Intervall soll genau fünf ganze Zahlen enthalten.", [G, G],
        [("0 liegt im Intervall", UND(["<=", "$1", 0], [">=", "$2", 0]), None, "Die 0 liegt nicht in deinem Intervall."), ("fünf ganze Zahlen", ["=", ["+", ["-", "$2", "$1"], 1], 5], ["+", ["-", "$2", "$1"], 1], "Dein Intervall enthält {} ganze Zahlen.")],
        [-1, 3], [([1, 5], "0 liegt im Intervall"), ([-1, 4], "fünf ganze Zahlen"), ([-5, 0], "fünf ganze Zahlen")],
        "Beide Grenzen gehören dazu. Zähl sie mit.", "Fünf ganze Zahlen heißt: b ist um 4 größer als a. Mit der 0 darin: [−4; 0], [−3; 1], [−2; 2], [−1; 3] oder [0; 4].", gut=[[-4, 0], [0, 4]]), None, None)
neu("a4", T, "V", "pruefen", 3, "parameter", LOES, "ja",
    bed("Setze für a eine Zahl ein, sodass x = 4 eine Lösung der Ungleichung 3x − a ≤ 5 ist, x = 5 aber keine.", [R],
        [("x = 4 ist eine Lösung", ["<=", ["-", 12, "$1"], 5], ["-", 12, "$1"], "Für x = 4 hat die linke Seite bei dir den Wert {}."), ("x = 5 ist keine Lösung", [">", ["-", 15, "$1"], 5], ["-", 15, "$1"], "Für x = 5 hat die linke Seite bei dir den Wert {}.")],
        [8], [([6], "x = 4 ist eine Lösung"), ([10], "x = 5 ist keine Lösung"), ([11], "x = 5 ist keine Lösung")],
        "Setz erst x = 4 ein, dann x = 5. Was muss jeweils für a gelten?", "x = 4: 12 − a ≤ 5, also a ≥ 7. x = 5: 15 − a > 5, also a < 10. Jede Zahl von 7 bis unter 10 passt.", gut=[[7], ["9,5"]]), None, None)
neu("a4", T, "V", "umdrehen", 3, "parameter", WAAGE, "ja",
    bed("Setze a und b so ein, dass die Ungleichung a · x + b > 0 genau die Lösungen x < 2 hat.", [R, R],
        [("Lösungen haben die Form x < …", ["<", "$1", 0], None, "Mit deinem a haben die Lösungen nicht die Form x < …"), ("Grenze ist 2", ["=", ["+", ["*", 2, "$1"], "$2"], 0], ["/", ["neg", "$2"], "$1"], "Deine Grenze liegt bei x = {}.")],
        [-3, 6], [([3, -6], "Lösungen haben die Form x < …"), ([0, 5], "Lösungen haben die Form x < …"), ([-3, 3], "Grenze ist 2")],
        "Wann dreht sich beim Auflösen nach x das Zeichen um?", "Das Zeichen dreht sich nur um, wenn a negativ ist. Die Grenze 2 muss die Gleichung a · 2 + b = 0 erfüllen, zum Beispiel a = −3 und b = 6.", gut=[[-1, 2], ["-0,5", 1]]), None, None)

# ═════════════════════ Prüfen ═════════════════════
aus = {f: [] for f in FLUG}
je_thema = {}
n_rechnung = n_fb = 0
for a in A:
    q, kenn = a["aufgabe"], a["kenn"]
    assert a["regel"] in REGELN, (kenn, a["regel"])
    assert ip.STUFE_VON[q["g"]] == q["s"], (kenn, q["g"], q["s"])
    assert a["typ"] in TYP and a["zaehlt"] in ("ja", "folge", "nein"), kenn
    eintrag = dict(kennung=kenn, thema=a["thema"], lernkarte=q["l"], stufe=q["s"], typ=TYP[a["typ"]], antwortform=q["y"], regel=a["regel"], regel_name=REGELN[a["regel"]]["name"], zaehlt=a["zaehlt"], fehlbilder=[])

    def fb_eintrag(ort, antwort, fbk, text):
        global n_fb
        assert fbk is None or fbk in FEHLBILD, (kenn, fbk)
        n_fb += 1
        eintrag["fehlbilder"].append(dict(**ort, antwort=antwort, fehlbild=fbk, regel_des_fehlbilds=FEHLBILD.get(fbk), beschreibung=text))

    if q["y"] == "zahl":
        soll = ip.rechne(q["c"])
        assert soll == q["o"]["wert"] == F(eval(a["zweit"][0], {"__builtins__": {"len": len, "min": min, "max": max, "range": range, "all": all, "sum": sum}}, {"F": F})), (kenn, soll)
        n_rechnung += 1
        werte = set()
        for w, fbk, text in a["fb"]:
            assert w != q["o"]["wert"] and w not in werte, (kenn, w)
            werte.add(w)
            fb_eintrag({}, w, fbk, text)
    elif q["y"] == "luecken":
        soll = [ip.rechne(c) for c in q["c"]]
        assert soll == q["o"]["werte"] == [z2(z) for z in a["zweit"]], (kenn, soll, [z2(z) for z in a["zweit"]])
        assert q["f"]["schablone"].count("□") == len(soll), kenn
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
        assert 1 <= len(q["f"]["felder"]) <= 6 and len(q["o"]["gegenbeispiele"]) >= len(q["o"]["bedingungen"]), kenn
        for g in [q["o"]["beispiel"]] + q["o"].get("gut", []):          # zweite Probe: jede gute Antwort wird als richtig bewertet
            r = bd.bewerte(q, {"werte": [str(x).replace("-", "−") for x in g]})
            assert r["format_ok"] and r["richtig"], (kenn, g, r)
        eintrag["hinweis_zu_fehlbildern"] = "Aus einer verletzten Bedingung allein folgt kein Fehlbild (Festlegung 7 im Format)."
    eintrag["aufgabe"] = q
    aus[a["flug"]].append(eintrag)
    je_thema.setdefault(a["thema"], []).append(q)

lagen = {}
for a in A:
    if a["aufgabe"]["y"] == "auswahl":
        lagen.setdefault(len(a["aufgabe"]["a"]), set()).add(a["aufgabe"]["o"]["index"])
assert lagen[4] == {0, 1, 2, 3}, lagen
texte = [a["aufgabe"]["f"]["text"] for a in A]
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
        assert not {x["f"].get("text") for x in d["aufgaben"]} & {q["f"]["text"] for q in liste}, thema       # keine Aufgabe doppelt zum Bestand
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
    assert 12 <= len(normal) <= 15 and 4 <= len(viele) <= 6, (flug, len(normal), len(viele))
    assert [e["stufe"] for e in normal] == sorted(e["stufe"] for e in normal) and [e["stufe"] for e in viele] == sorted(e["stufe"] for e in viele), flug    # Schwierigkeit aufsteigend
    titel, kind, klasse = FLUG[flug]
    json.dump({"stand": "2026-11-26", "flug": flug, "titel": titel, "fuer": kind, "klasse": klasse,
               "hinweis": "Neue Aufgaben, rollendes System Stufe 1. Nicht eingespielt. Je Eintrag: Zusatzangaben (Regel-Kennung, Fehlbilder, Typ, Zählvorschlag) und unter „aufgabe“ die Aufgabe im Format von inhalte/README.md. "
                          "Reihenfolge: erst die Aufgaben ohne Bau, dann die des Typs „bedingung“, jeweils mit aufsteigender Stufe.",
               "aufgaben": normal + viele}, open(os.path.join(HIER, f"{flug}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{flug:4} {kind}: {len(normal)} ohne Bau, {len(viele)} bedingung; Stufen {sorted(set(e['stufe'] for e in liste))}; Regeln {sorted(set(e['regel'] for e in liste))}")
print(f"{len(A)} Aufgaben; {n_rechnung} Rechnungen zweifach nachgerechnet; {n_fb} Fehlbilder, davon {sum(1 for f in aus.values() for e in f for x in e['fehlbilder'] if x['fehlbild'])} mit Kennung")
print("OK")
