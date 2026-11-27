"""Mathe-Profi, Auftrag 18: Aufgaben auf Vorrat für die übernächsten Flüge (rollendes System, Stufe 2).

Aufruf: python3 -I inhalte/mathe-profi/rollend-2/bauen.py
Kind 1: a1, d1, g1. Kind 2: g8, g2-teil2, f1. Je Flug 13 bis 15 Aufgaben in Typen ohne Bau (zahl, auswahl, luecken) und 5 des Typs „bedingung“.
Geprüft wird wie in rollend-1, dazu:
- Brüche im Text nur in den Schreibweisen, die die App eindeutig stapeln kann (kein 1/2x, keine verschachtelten Klammern im Bruch),
- Zeichnungen (f.grafik) nur in Arten, die die App schon zeichnet (tabelle, saeulen, kreisdiagramm, koordinaten); Form hier nachgesehen,
- Namen der Bedingungen: keiner ist länger als 40 Zeichen; ob ein Name den Weg verrät, ist von Hand gelesen (README).
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
# Flug: (Titel, Kind, Klasse, Themen-Datei, Kürzel der Kennung, Lernkarte -> Teilfähigkeit oder None für „gleich“)
FLUG = {
    "a1": ("Einfache Gleichungen", "Kind 1", 5, "gleichungen.einfach", "A1", {"waage": "verstehen", "zwei_schritte": "umkehren", "probe": "verstehen", "aufstellen": "anwenden", "ohne_loesung": "loesbarkeit"}),
    "d1": ("Daten darstellen", "Kind 1", 5, "daten.darstellen", "D1", None),
    "g1": ("Größen und Einheiten", "Kind 1", 5, "groessen.einheiten", "G1", None),
    "g8": ("Prozent mit verändertem Grundwert", "Kind 2", 7, "bruch.prozent_grundwert", "G8", None),
    "g2-teil2": ("Dreisatz · Teil 2", "Kind 2", 5, "groessen.proportional", "G2T2", {"erkennen": "begriff", "vervielfachen": "tabelle", "pruefen": "begriff"}),
    "f1": ("Funktionsbegriff", "Kind 2", 8, "funktionen.grundbegriffe", "F1", None),
}
A = []
WAAGE, GEGEN, LOES, TERM, REIH = "rr.waage", "rr.gegenrechnung", "id.algebra.gleichung_loesen", "id.algebra.term", "rr.reihenfolge"
ANTEIL, KENNZ, VERH, GR, SW = "id.daten.anteil", "id.daten.kennzahl", "rr.verhaeltnis", "id.verhaeltnisse.groesse", "rr.stellenwert"
PROZ, WERT, ZU, ERL = "id.verhaeltnisse.prozent", "id.verhaeltnisse.wert_fuer_eins", "id.funktionen.zuordnung", "id.algebra.erlaubte_zahlen"


def z2(ausdruck):
    genau = re.sub(r"(?<![\w.])(\d+)(?![\w.])", r"F(\1)", ausdruck)
    return F(eval(genau, {"__builtins__": {}}, {"F": F, "abs": abs}))


def neu(flug, l, typ, s, g, regel, zaehlt, aufgabe, zweit, fb, probe=None):
    tf = FLUG[flug][5]
    A.append(dict(flug=flug, thema=FLUG[flug][3], typ=typ, regel=regel, zaehlt=zaehlt, aufgabe={"l": l, "t": tf[l] if tf else l, "p": "uebung", "s": s, "g": g, **aufgabe}, zweit=zweit, fb=fb, probe=probe))


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

# ═════════════════════ Kind 1 · Flug a1 · Einfache Gleichungen (Klasse 5, gerechnet wird in ℕ) ═════════════════════
f = "a1"
neu(f, "waage", 4, 1, "direkt", WAAGE, "nein",
    luecken("x + 8 = 21 als Waage: Links bleibt nur x übrig, wenn du ① wegnimmst. Dasselbe nimmst du rechts weg. Rechts bleiben dann ②.", K(2), [8, 13], ["8", "21 - 8"],
            "Was du links wegnimmst, nimmst du auch rechts weg.", "Auf beiden Seiten 8 weg: links bleibt x, rechts 21 − 8 = 13. Also x = 13."),
    ["21-13", "13"], {1: [(29, "fb.gegenrechnung.gleiche_rechnung", "8 dazugezählt statt weggenommen"), (21, "fb.waage.nur_eine_seite", "rechts nichts weggenommen")]})
neu(f, "zwei_schritte", 4, 1, "direkt", GEGEN, "nein",
    luecken("Löse 4 · x + 7 = 31 rückwärts. Erst 31 − 7 = ①. Dann ① : 4 = ②. Also x = ②.", K(2), [24, 6], ["31 - 7", "(31 - 7) // 4"],
            "Der letzte Schritt war „+ 7“. Den machst du zuerst rückgängig.", "31 − 7 = 24, dann 24 : 4 = 6. Probe: 4 · 6 + 7 = 31."),
    ["4*6", "(31-7)/4"], {0: [(38, "fb.gegenrechnung.gleiche_rechnung", "31 + 7 gerechnet")]})
neu(f, "zwei_schritte", 12, 1, "erkennen", GEGEN, "ja",
    wahl("Jemand löst 5 · x − 3 = 32 so: Schritt 1: 32 : 5. Schritt 2: Ergebnis + 3. Was ist falsch?",
         ["Es müsste − 3 statt + 3 heißen.", "Es müsste · 5 statt : 5 heißen.", "Nichts, der Weg stimmt.", "Die Reihenfolge: erst + 3, dann : 5."], 3,
         "Welcher Schritt kam in der Gleichung zuletzt?", "Zuletzt wurde 3 abgezogen. Das wird zuerst rückgängig gemacht: 32 + 3 = 35, dann 35 : 5 = 7."),
    lambda: (32 + 3) % 5 == 0 and 5 * 7 - 3 == 32, {0: ("fb.gegenrechnung.gleiche_rechnung", "dieselbe Rechnung statt der Gegenrechnung"), 1: ("fb.gegenrechnung.gleiche_rechnung", "dieselbe Rechnung statt der Gegenrechnung"), 2: ("fb.gegenrechnung.reihenfolge_nicht_umgekehrt", "den Fehler in der Reihenfolge nicht bemerkt")})
neu(f, "probe", 13, 1, "erkennen", LOES, "ja",
    wahl("Du willst prüfen, ob x = 9 die Gleichung 6 · x − 14 = 40 löst. Was tust du?",
         ["40 für x einsetzen", "9 für x einsetzen und beide Seiten vergleichen", "9 und 40 zusammenzählen", "die Gleichung noch einmal auf demselben Weg lösen"], 1,
         "Eine Lösung macht beide Seiten gleich.", "Einsetzen: 6 · 9 − 14 = 40. Beide Seiten sind gleich, also ist 9 die Lösung."),
    lambda: 6 * 9 - 14 == 40, {0: (None, "das Ergebnis statt der Lösung eingesetzt"), 2: (None, "kein Bezug zur Gleichung"), 3: (None, "derselbe Weg wiederholt auch denselben Fehler")})
neu(f, "ohne_loesung", 13, 1, "erkennen", LOES, "ja",
    wahl("Woran erkennst du, dass 6 · x + 20 = 14 in ℕ keine Lösung hat?",
         ["14 ist nicht durch 6 teilbar.", "Rückwärts müsstest du 14 − 20 rechnen. Das geht in ℕ nicht.", "20 ist größer als 6.", "Links steht ein Plus."], 1,
         "Rechne den ersten Schritt rückwärts.", "Rückwärts: 14 − 20. Das Ergebnis läge unter 0. In ℕ gibt es deshalb keine Lösung."),
    lambda: 14 - 20 < 0 and (14 - 2) % 6 == 0, {0: (None, "falscher Grund: 6 · x + 2 = 14 hat die Lösung 2, obwohl 14 nicht durch 6 teilbar ist"), 2: (None, "Vergleich ohne Bedeutung"), 3: (None, "Vergleich ohne Bedeutung")})
neu(f, "zwei_schritte", 17, 2, "umkehr", GEGEN, "ja",
    zahl("Ich denke mir eine Zahl, nehme sie mal 6 und ziehe 12 ab. Ich erhalte 48. Welche Zahl habe ich mir gedacht?", 10, "(48 + 12) // 6",
         "Rechne rückwärts. Was kam zuletzt?", "Zuletzt wurde 12 abgezogen: 48 + 12 = 60. Davor mal 6: 60 : 6 = 10."),
    ["60/6"], [(6, "fb.gegenrechnung.gleiche_rechnung", "48 − 12 gerechnet, dann : 6"), (20, "fb.gegenrechnung.reihenfolge_nicht_umgekehrt", "erst : 6, dann + 12")])
neu(f, "waage", 14, 2, "mehrschritt", WAAGE, "ja",
    zahl("Zwei Wege für 3 · x + 12 = 30. Weg A: erst − 12, dann : 3. Weg B: erst beide Seiten durch 3 teilen. Dann steht da x + ? = 10. Welche Zahl steht für das Fragezeichen?", 4, "12 // 3",
         "Beim Teilen wird links jeder Summand geteilt.", "Geteilt durch 3: aus 3 · x wird x, aus 12 wird 4, aus 30 wird 10. Also x + 4 = 10 und x = 6 – wie bei Weg A."),
    ["10 - (30-12)/3"], [(12, "fb.waage.nur_ein_summand", "die 12 nicht mitgeteilt")])
neu(f, "waage", "B", 2, "darstellung", WAAGE, "ja",
    luecken("Links liegen drei gleiche Säckchen mit je x Kugeln und 4 einzelne Kugeln. Rechts liegen 19 Kugeln. Die Waage ist im Gleichgewicht. Schreibe die Gleichung und löse sie.", "□ · x + □ = □; x = □", [3, 4, 19, 5],
            ["3", "4", "19", "(19 - 4) // 3"], "Säckchen sind das x. Einzelne Kugeln sind Zahlen.", "3 · x + 4 = 19. Auf beiden Seiten 4 weg: 3 · x = 15. Geteilt durch 3: x = 5."),
    ["3", "4", "19", "15/3"], {3: [(15, None, "nur die 4 weggenommen, nicht geteilt")]})
neu(f, "aufstellen", "B", 2, "einkleidung", TERM, "ja",
    wahl("„Das Vierfache einer Zahl, vermindert um 5, ergibt 23.“ Welche Gleichung passt?", ["4 · (x − 5) = 23", "5 − 4 · x = 23", "4 · x − 5 = 23", "x : 4 − 5 = 23"], 2,
         "Übersetze Stück für Stück: erst „das Vierfache“, dann „vermindert um 5“.", "Das Vierfache: 4 · x. Vermindert um 5: 4 · x − 5. Ergibt 23: 4 · x − 5 = 23. (Lösung: x = 7.)"),
    lambda: 4 * 7 - 5 == 23, {0: (None, "„vermindert um 5“ auf die Zahl statt auf das Vierfache bezogen"), 1: ("fb.tauschen.minus_getauscht", "beim Minus die Reihenfolge getauscht"), 3: (None, "„das Vierfache“ als geteilt durch 4 gelesen")})
neu(f, "aufstellen", 17, 2, "umkehr", TERM, "ja",
    wahl("Welcher Satz passt zur Gleichung (x + 6) · 3 = 27?",
         ["Das Dreifache einer Zahl, vermehrt um 6, ergibt 27.", "Zu einer Zahl wird 6 addiert. Das Dreifache dieser Summe ist 27.", "Eine Zahl wird durch 3 geteilt und um 6 vermehrt. Das ergibt 27."], 1,
         "Was passiert wegen der Klammer zuerst?", "Die Klammer kommt zuerst: x + 6. Dann mal 3. Der erste Satz gehört zu 3 · x + 6 = 27."),
    lambda: (3 + 6) * 3 == 27 and 3 * 7 + 6 == 27, {0: (None, "die Klammer nicht beachtet"), 2: (None, "mal 3 als geteilt durch 3 gelesen")})
neu(f, "probe", 12, 2, "mehrschritt", LOES, "ja",
    luecken("Nora löst 8 · x − 6 = 50 und erhält x = 6. Mach die Probe: Mit x = 6 ergibt die linke Seite ①. Das ist nicht 50. Die richtige Lösung ist x = ②.", K(2), [42, 7],
            ["8 * 6 - 6", "(50 + 6) // 8"], "Setze 6 ein. Löse dann selbst rückwärts.", "8 · 6 − 6 = 42, also stimmt 6 nicht. Rückwärts: 50 + 6 = 56, 56 : 8 = 7."),
    ["48-6", "56/8"], {0: [(48, None, "die 6 nicht abgezogen")], 1: [(6, None, "Noras falsche Lösung übernommen")]})
neu(f, "probe", 17, 3, "parameter", LOES, "ja",
    zahl("Die Gleichung 4 · x + □ = 26 soll die Lösung x = 5 haben. Welche Zahl gehört in das Kästchen?", 6, "26 - 4 * 5",
         "Setze 5 für x ein.", "4 · 5 = 20. Bis 26 fehlen 6."),
    ["26-20"], [(46, "fb.gegenrechnung.gleiche_rechnung", "26 + 20 gerechnet"), (21, None, "nur 5 abgezogen, das Malnehmen vergessen")])
neu(f, "zwei_schritte", 17, 3, "rueckwaerts", GEGEN, "ja",
    zahl("(x : 3 + 4) · 2 = 20. Rechne rückwärts: Welche Zahl ist x?", 18, "(20 // 2 - 4) * 3",
         "Drei Schritte. Der letzte war „· 2“.", "20 : 2 = 10. Dann 10 − 4 = 6. Dann 6 · 3 = 18. Probe: 18 : 3 + 4 = 10, mal 2 ist 20."),
    ["(10-4)*3"], [(28, "fb.gegenrechnung.reihenfolge_nicht_umgekehrt", "in der Reihenfolge der Gleichung zurückgerechnet: · 3, − 4, : 2"), (6, None, "nach dem zweiten Schritt aufgehört")])
neu(f, "ohne_loesung", 12, 3, "begruenden", LOES, "ja",
    wahl("Tom sagt: „7 · x + 3 = 40 hat in ℕ keine Lösung.“ Stimmt das?",
         ["Ja: 40 − 3 = 37, und 37 lässt sich nicht ohne Rest durch 7 teilen.", "Nein: x = 5 ist eine Lösung.", "Nein: Jede Gleichung hat eine Lösung.", "Ja: weil 3 kleiner ist als 7."], 0,
         "Rechne rückwärts und schau, ob das Teilen aufgeht.", "40 − 3 = 37. 37 : 7 geht nicht auf (7 · 5 = 35, 7 · 6 = 42). In ℕ gibt es keine Lösung."),
    lambda: 37 % 7 != 0 and 7 * 5 + 3 != 40, {1: (None, "nicht nachgerechnet: 7 · 5 + 3 = 38"), 2: (None, "die Regel der Lernkarte nicht beachtet"), 3: (None, "richtiges Urteil, falscher Grund")})
neu(f, "aufstellen", "A", 3, "verknuepfen", GEGEN, "ja",
    zahl("Drei Freunde kaufen zusammen ein Geschenk für 31 €. Jeder zahlt gleich viel. Die fehlenden 4 € kommen aus der Klassenkasse. Wie viel Euro zahlt jeder?", 9, "(31 - 4) // 3",
         "Nenne den Betrag eines Freundes x und stelle eine Gleichung auf.", "3 · x + 4 = 31. Rückwärts: 31 − 4 = 27, 27 : 3 = 9.", einheit="€"),
    ["27/3"], [(27, None, "nur die 4 € abgezogen"), (35, "fb.gegenrechnung.gleiche_rechnung", "die 4 € dazugezählt")])
term = lambda feld: ["+", ["*", 3, feld], 2]
neu(f, "probe", "V", 1, "direkt", LOES, "ja",
    bed("Nenne eine natürliche Zahl x, für die 3 · x + 2 größer als 20 und kleiner als 30 ist.", [G],
        [("größer als 20", [">", term("$1"), 20], term("$1"), "Mit deiner Zahl hat 3 · x + 2 den Wert {}."), ("kleiner als 30", ["<", term("$1"), 30], term("$1"), "Mit deiner Zahl hat 3 · x + 2 den Wert {}.")],
        [7], [([6], "größer als 20"), ([10], "kleiner als 30"), ([0], "größer als 20")],
        "Setze eine Zahl ein und rechne aus.", "Es passen 7, 8 und 9: Sie ergeben 23, 26 und 29.", gut=[[8], [9]]), None, None)
neu(f, "aufstellen", "V", 2, "umkehr", GEGEN, "ja",
    bed("Erfinde ein Zahlenrätsel zur gedachten Zahl 7: „Ich nehme meine Zahl mal □ und zähle □ dazu. Ich erhalte □.“ Die erste Zahl soll größer als 1 sein, die zweite größer als 0.", [G, G, G],
        [("erste Zahl größer als 1", [">", "$1", 1], "$1", "Deine erste Zahl ist {}."), ("zweite Zahl größer als 0", [">", "$2", 0], "$2", "Deine zweite Zahl ist {}."),
         ("das Rätsel stimmt für die 7", ["=", ["+", ["*", "$1", 7], "$2"], "$3"], ["+", ["*", "$1", 7], "$2"], "Mit der 7 kommt bei deinem Rätsel {} heraus.")],
        [3, 4, 25], [([1, 4, 11], "erste Zahl größer als 1"), ([3, 0, 21], "zweite Zahl größer als 0"), ([3, 4, 24], "das Rätsel stimmt für die 7")],
        "Rechne dein Rätsel mit der 7 durch.", "Zum Beispiel mal 3 und plus 4: 7 · 3 + 4 = 25.", gut=[[2, 1, 15]]), None, None)
neu(f, "waage", "V", 2, "darstellung", WAAGE, "ja",
    bed("Links liegen einige gleiche Säckchen und 2 einzelne Kugeln, rechts 20 Kugeln. Die Waage ist im Gleichgewicht. Nenne eine mögliche Zahl der Säckchen und die Zahl der Kugeln in jedem Säckchen. Beide Zahlen sollen größer als 1 sein.", [G, G],
        [("beide größer als 1", [">", ["min", "$alle"], 1], ["min", "$alle"], "Deine kleinere Zahl ist {}."),
         ("Waage im Gleichgewicht", ["=", ["+", ["*", "$1", "$2"], 2], 20], ["+", ["*", "$1", "$2"], 2], "Links liegen bei dir {} Kugeln.")],
        [3, 6], [([1, 18], "beide größer als 1"), ([3, 5], "Waage im Gleichgewicht"), ([4, 5], "Waage im Gleichgewicht")],
        "Wie viele Kugeln müssen in allen Säckchen zusammen sein?", "In den Säckchen sind zusammen 18 Kugeln. Es passen 2 Säckchen mit 9, 3 mit 6, 6 mit 3 oder 9 mit 2.", gut=[[2, 9], [9, 2]]), None, None)
neu(f, "ohne_loesung", "V", 3, "parameter", LOES, "ja",
    bed("Setze eine Zahl zwischen 1 und 19 ein, sodass die Gleichung 3 · x + □ = 20 in ℕ keine Lösung hat.", [G],
        [("zwischen 1 und 19", UND([">=", "$1", 1], ["<=", "$1", 19]), "$1", "Deine Zahl ist {}."),
         ("keine Lösung in ℕ", ["nicht", ["teilbar", ["-", 20, "$1"], 3]], ["/", ["-", 20, "$1"], 3], "Mit deiner Zahl ist x = {} eine Lösung.")],
        [4], [([25], "zwischen 1 und 19"), ([2], "keine Lösung in ℕ"), ([0], "zwischen 1 und 19"), ([17], "keine Lösung in ℕ")],
        "Rechne rückwärts: Was muss sich dann durch 3 teilen lassen?", "Rückwärts bleibt 20 minus deine Zahl. Lässt sich das nicht ohne Rest durch 3 teilen, gibt es keine Lösung. Zum Beispiel 4: 16 : 3 geht nicht auf.", gut=[[1], [19]]), None, None)
neu(f, "zwei_schritte", "V", 3, "parameter", GEGEN, "ja",
    bed("Baue eine Gleichung der Form □ · x − □ = □ mit der Lösung x = 6. Die drei Zahlen sollen verschieden und alle größer als 1 sein.", [G, G, G],
        [("alle größer als 1", [">", ["min", "$alle"], 1], ["min", "$alle"], "Deine kleinste Zahl ist {}."), ("verschieden", ["verschieden", "$alle"], None, "Die drei Zahlen sollen verschieden sein."),
         ("x = 6 ist die Lösung", ["=", ["-", ["*", "$1", 6], "$2"], "$3"], ["-", ["*", "$1", 6], "$2"], "Mit x = 6 hat deine linke Seite den Wert {}.")],
        [3, 4, 14], [([2, 1, 11], "alle größer als 1"), ([3, 3, 15], "verschieden"), ([3, 4, 15], "x = 6 ist die Lösung")],
        "Wähle die ersten zwei Zahlen und rechne mit x = 6 die linke Seite aus.", "Zum Beispiel 3 · x − 4 = 14, denn 3 · 6 − 4 = 14.", gut=[[2, 3, 9], [5, 10, 20]]), None, None)

# ═════════════════════ Kind 1 · Flug d1 · Daten darstellen ═════════════════════
f = "d1"
WUERFE = [3, 5, 3, 6, 1, 3, 5, 2, 6, 3]
neu(f, "absolute_haeufigkeit", 4, 1, "direkt", KENNZ, "nein",
    luecken("Würfe: " + ", ".join(map(str, WUERFE)) + ". Die 3 kommt ①-mal vor, die 5 kommt ②-mal vor. Alle Würfe zusammen: ③.", K(3), [4, 2, 10], ["1 + 1 + 1 + 1", "1 + 1", "4 + 2 + 2 + 1 + 1"],
            "Streiche jede gezählte Zahl ab.", "Die 3 steht viermal da, die 5 zweimal. Zusammen sind es 10 Würfe."),
    [str(WUERFE.count(3)), str(WUERFE.count(5)), str(len(WUERFE))], {2: [(6, None, "die verschiedenen Augenzahlen statt der Würfe gezählt")]})
neu(f, "relative_haeufigkeit", 4, 1, "direkt", ANTEIL, "nein",
    luecken("Von 20 Kindern kommen 5 mit dem Rad. Anteil: ① von ②. Gekürzt ist das 1 von ③. In Prozent: ④ %.", "① = □; ② = □; ③ = □; ④ = □", [5, 20, 4, 25], ["5", "20", "20 // 5", "5 * 100 // 20"],
            "Relative Häufigkeit ist Anzahl durch Gesamtzahl.", "5 von 20, gekürzt 1 von 4. Ein Viertel sind 25 %."),
    ["5", "20", "4", "100/4"], {3: [(5, None, "die Anzahl als Prozent genommen"), (4, None, "den Nenner als Prozent genommen")]})
neu(f, "relative_haeufigkeit", 12, 1, "erkennen", ANTEIL, "ja",
    wahl("In einer Klasse sind 12 Mädchen und 18 Jungen. Tim rechnet für den Anteil der Mädchen 12/18. Was ist falsch?",
         ["Er müsste 18/12 rechnen.", "Er müsste 12 + 18 rechnen.", "Er teilt durch die Zahl der Jungen statt durch alle 30 Kinder.", "Nichts, 12/18 stimmt."], 2,
         "Wodurch wird bei der relativen Häufigkeit geteilt?", "Geteilt wird durch die Gesamtzahl: 12 + 18 = 30. Der Anteil ist 12/30 = 2/5, das sind 40 %."),
    lambda: F(12, 30) == F(2, 5), {0: (None, "Zähler und Nenner getauscht"), 1: (None, "die Gesamtzahl für den Anteil gehalten"), 3: ("fb.anteil.guenstig_durch_unguenstig", "den Fehler nicht bemerkt: Teil durch den anderen Teil")})
neu(f, "kreisdiagramm", 13, 1, "erkennen", ANTEIL, "ja",
    wahl("Ein Anteil von 25 % soll im Kreisdiagramm gezeichnet werden. Wie findest du den Winkel?", ["25 · 360° rechnen", "ein Viertel von 360° nehmen", "25° abtragen", "360° : 25 rechnen"], 1,
         "25 % sind welcher Bruchteil?", "25 % sind ein Viertel. Ein Viertel von 360° sind 90°."),
    lambda: F(25, 100) * 360 == 90, {0: (None, "25 statt 25 Hundertstel genommen"), 2: (None, "Prozent als Grad genommen"), 3: (None, "geteilt statt den Anteil genommen")})
neu(f, "tabelle_auswerten", "B", 2, "darstellung", ANTEIL, "ja",
    zahl("Die Tabelle zeigt, wie die Kinder einer Schule zur Schule kommen. Wie viel Prozent kommen mit dem Bus?", 40, "16 * 100 // (8 + 10 + 16 + 6)",
         "Bilde zuerst die Summe aller Anzahlen.", "Zusammen 8 + 10 + 16 + 6 = 40 Kinder. Bus: 16 von 40, das sind 40 %.", einheit="%",
         grafik=TAB(["Weg", "zu Fuß", "Rad", "Bus", "Auto"], ["Anzahl", "8", "10", "16", "6"])),
    ["16/40*100"], [(16, None, "die Anzahl statt des Anteils genannt"), (2.5, "fb.verhaeltnis.falsche_richtung", "40 : 16 gerechnet")])
neu(f, "relative_haeufigkeit", 17, 2, "umkehr", ANTEIL, "ja",
    zahl("25 % der befragten Kinder nennen „Hund“ als Lieblingstier. Das sind 7 Kinder. Wie viele Kinder wurden befragt?", 28, "7 * 4",
         "25 % sind ein Viertel. Wie viele Viertel hat das Ganze?", "7 Kinder sind ein Viertel. Alle Kinder sind vier Viertel: 4 · 7 = 28."),
    ["7*100/25"], [(1.75, "fb.verhaeltnis.falsche_richtung", "7 : 4 gerechnet"), (32, None, "7 + 25 gerechnet")])
neu(f, "absolute_haeufigkeit", 17, 2, "umkehr", KENNZ, "ja",
    zahl("Bei 30 Würfen fiel die 6 genau 4-mal. Die 1 fiel doppelt so oft wie die 6. Wie oft fielen die anderen vier Zahlen zusammen?", 18, "30 - 4 - 2 * 4",
         "Alle Häufigkeiten zusammen ergeben die Zahl der Würfe.", "Die 6 viermal, die 1 achtmal. Für die anderen bleiben 30 − 4 − 8 = 18 Würfe."),
    ["30-12"], [(22, None, "die 1 nur viermal gezählt"), (26, None, "nur die 6 abgezogen")])
neu(f, "saeulendiagramm", 17, 2, "umkehr", VERH, "ja",
    zahl("In einem Säulendiagramm steht 1 cm für 4 Kinder. Eine Säule ist 3,5 cm hoch. Für wie viele Kinder steht sie?", 14, "3.5 * 4",
         "Jeder Zentimeter steht für 4 Kinder.", "3,5 · 4 = 14 Kinder."),
    ["7*2"], [(0.875, "fb.verhaeltnis.falsche_richtung", "3,5 : 4 gerechnet"), (7.5, "fb.verhaeltnis.addiert_statt_malgenommen", "3,5 + 4 gerechnet")])
neu(f, "saeulendiagramm", "B", 2, "darstellung", KENNZ, "ja",
    zahl("Das Diagramm zeigt die Lieblingstiere einer Klasse. Wie viele Kinder wurden insgesamt befragt?", 24, "9 + 7 + 5 + 3",
         "Lies jede Säule an der Achse ab.", "Hund 9, Katze 7, Pferd 5, Hase 3. Zusammen 24 Kinder.",
         grafik={"typ": "saeulen", "einheit": "Kinder", "werte": [{"name": "Hund", "wert": 9}, {"name": "Katze", "wert": 7}, {"name": "Pferd", "wert": 5}, {"name": "Hase", "wert": 3}], "y_start": 0, "zahlen": False}),
    ["(9+3)+(7+5)"], [(9, None, "nur die höchste Säule abgelesen"), (4, None, "die Säulen gezählt")])
neu(f, "kreisdiagramm", 14, 2, "mehrschritt", ANTEIL, "ja",
    luecken("Von 24 Kindern spielen 6 Fußball. Zwei Wege zum Winkel im Kreisdiagramm. Weg A: 6 von 24 ist ein Viertel, also ein Viertel von 360°. Weg B: Auf ein Kind kommen 360° : 24 = ①°, auf 6 Kinder ②°.", K(2), [15, 90],
            ["360 // 24", "360 // 24 * 6"], "Beide Wege müssen denselben Winkel ergeben.", "360° : 24 = 15° je Kind. 6 · 15° = 90°. Weg A: ein Viertel von 360° sind auch 90°."),
    ["15", "360/4"], {1: [(25, None, "25 % als 25° genommen"), (60, None, "6 · 10 gerechnet")]})
neu(f, "irrefuehrend", 12, 2, "darstellung", KENNZ, "ja",
    wahl("Das Diagramm zeigt die Besucher eines Schwimmbads. Die Säule für Juli ist doppelt so hoch wie die für Juni. Was stimmt?",
         ["Im Juli kamen doppelt so viele Besucher wie im Juni.", "Im Juli kamen 20 Besucher mehr. Die Achse beginnt erst bei 500.", "Im Juli kamen 40 Besucher mehr.", "Die Zahlen im Diagramm sind falsch."], 1,
         "Lies Achse und Zahlen. Wo beginnt die Achse?", "Juni 520, Juli 540: nur 20 Besucher mehr. Weil die Achse bei 500 beginnt, sind die Säulen 20 und 40 hoch – das sieht nach „doppelt“ aus."),
    lambda: (540 - 500) == 2 * (520 - 500) and 540 - 520 == 20, {0: (None, "nur die Säulenhöhen verglichen"), 2: (None, "die Höhe der Säule über 500 als Unterschied genommen"), 3: (None, "die Zahlen stimmen, nur der Eindruck täuscht")},
    probe=None)
A[-1]["aufgabe"]["f"]["grafik"] = {"typ": "saeulen", "einheit": "Besucher", "werte": [{"name": "Juni", "wert": 520}, {"name": "Juli", "wert": 540}], "y_start": 500, "zahlen": True}
neu(f, "irrefuehrend", 14, 3, "begruenden", KENNZ, "ja",
    wahl("Zwei Diagramme zeigen dieselben Zahlen: 48 und 52 Stimmen. Bei Diagramm A beginnt die Achse bei 0, bei Diagramm B bei 46. Was stimmt?",
         ["In A wirkt der Unterschied größer: Dort ist die zweite Säule 3-mal so hoch.", "In beiden wirkt der Unterschied gleich groß.", "In B wirkt der Unterschied größer: Dort ist die zweite Säule doppelt so hoch.", "In B wirkt der Unterschied größer: Dort ist die zweite Säule 3-mal so hoch."], 3,
         "Wie hoch sind die Säulen in B? Zieh den Achsenanfang ab.", "In B sind die Säulen 48 − 46 = 2 und 52 − 46 = 6 hoch. 6 ist das Dreifache von 2. In A sind sie fast gleich hoch."),
    lambda: (52 - 46) == 3 * (48 - 46), {0: (None, "die beiden Diagramme verwechselt"), 1: (None, "den Achsenanfang nicht beachtet"), 2: (None, "Säulenhöhen in B falsch gerechnet")})
neu(f, "tabelle_auswerten", 17, 3, "rueckwaerts", ANTEIL, "ja",
    zahl("In der Tabelle fehlen zwei Zahlen. Zusammen wurden 50 Stimmen abgegeben, und „Blau“ hat 30 % aller Stimmen. Wie viele Stimmen hat „Grün“?", 14, "50 - 12 - 50 * 30 // 100 - 9",
         "Rechne zuerst die Stimmen für Blau aus.", "Blau: 30 % von 50 sind 15. Grün: 50 − 12 − 15 − 9 = 14.",
         grafik=TAB(["Farbe", "Rot", "Blau", "Grün", "Gelb"], ["Stimmen", "12", "?", "?", "9"])),
    ["50-(12+15+9)"], [(29, None, "die Stimmen für Blau nicht abgezogen"), (15, None, "die Stimmen für Blau genannt")])
neu(f, "kreisdiagramm", "A", 3, "verknuepfen", ANTEIL, "ja",
    zahl("Das Kreisdiagramm zeigt, wie 60 Kinder ihre Pause verbringen. Wie viele Kinder spielen Fangen?", 21, "60 * 35 // 100",
         "Der Anteil steht im Diagramm. Das Ganze sind 60 Kinder.", "35 % von 60: 10 % sind 6, 5 % sind 3. Zusammen 3 · 6 + 3 = 21 Kinder.",
         grafik={"typ": "kreisdiagramm", "einheit": " %", "werte": [{"name": "Fangen", "wert": 35}, {"name": "Reden", "wert": 40}, {"name": "Ball", "wert": 25}], "zahlen": True}),
    ["60/20*7"], [(35, None, "die Prozentzahl als Anzahl genommen"), (126, None, "35 % von 360 gerechnet")])
neu(f, "relative_haeufigkeit", "V", 1, "direkt", ANTEIL, "ja",
    bed("In einer Klasse sind zwischen 20 und 30 Kinder. Genau ein Viertel von ihnen trägt eine Brille. Nenne eine mögliche Zahl der Kinder und die Zahl der Kinder mit Brille.", [G, G],
        [("zwischen 20 und 30 Kinder", UND([">=", "$1", 20], ["<=", "$1", 30]), "$1", "Deine Klasse hat {} Kinder."),
         ("ein Viertel trägt eine Brille", ["=", ["*", 4, "$2"], "$1"], ["*", 4, "$2"], "Das Vierfache deiner Brillen-Zahl ist {}.")],
        [24, 6], [([32, 8], "zwischen 20 und 30 Kinder"), ([24, 8], "ein Viertel trägt eine Brille"), ([22, 5], "ein Viertel trägt eine Brille")],
        "Ein Viertel heißt: Viermal so viele Kinder sind die ganze Klasse.", "Die Kinderzahl muss durch 4 teilbar sein: 20 und 5, 24 und 6 oder 28 und 7.", gut=[[20, 5], [28, 7]]), None, None)
neu(f, "absolute_haeufigkeit", "V", 2, "mehrschritt", KENNZ, "ja",
    bed("Ein Glücksrad mit vier Farben wird 20-mal gedreht. Erfinde ein mögliches Ergebnis: Wie oft kam Rot, Blau, Grün, Gelb? Jede Farbe soll mindestens einmal vorkommen, und Rot soll öfter vorkommen als jede andere Farbe.", [G, G, G, G],
        [("jede Farbe mindestens einmal", [">=", ["min", "$alle"], 1], ["min", "$alle"], "Deine kleinste Anzahl ist {}."), ("zusammen 20 Drehungen", ["=", ["summe", "$alle"], 20], ["summe", "$alle"], "Zusammen sind es bei dir {} Drehungen."),
         ("Rot am häufigsten", UND([">", "$1", "$2"], [">", "$1", "$3"], [">", "$1", "$4"]), "$1", "Rot kam bei dir {}-mal. Eine andere Farbe kam genauso oft oder öfter.")],
        [8, 5, 4, 3], [([10, 0, 5, 5], "jede Farbe mindestens einmal"), ([8, 5, 4, 4], "zusammen 20 Drehungen"), ([5, 5, 5, 5], "Rot am häufigsten")],
        "Alle vier Häufigkeiten zusammen ergeben die Zahl der Drehungen.", "Zum Beispiel 8, 5, 4 und 3: zusammen 20, und die 8 ist am größten.", gut=[[17, 1, 1, 1], [6, 5, 5, 4]]), None, None)
neu(f, "kreisdiagramm", "V", 2, "umkehr", ANTEIL, "ja",
    bed("Ein Kreisdiagramm hat drei Teile. Nenne drei verschiedene Winkel in Grad, die zusammen ein Kreisdiagramm ergeben. Der größte Teil soll genau die Hälfte des Kreises sein.", [G, G, G],
        [("jeder Winkel größer als 0", [">", ["min", "$alle"], 0], ["min", "$alle"], "Dein kleinster Winkel hat {}°."), ("verschieden", ["verschieden", "$alle"], None, "Die drei Winkel sollen verschieden sein."),
         ("zusammen ein voller Kreis", ["=", ["summe", "$alle"], 360], ["summe", "$alle"], "Deine Winkel ergeben zusammen {}°."), ("größter Teil ist die Hälfte", ["=", ["max", "$alle"], 180], ["max", "$alle"], "Dein größter Winkel hat {}°.")],
        [180, 100, 80], [([180, 200, -20], "jeder Winkel größer als 0"), ([180, 90, 90], "verschieden"), ([180, 100, 70], "zusammen ein voller Kreis"), ([200, 100, 60], "größter Teil ist die Hälfte")],
        "Wie viel Grad hat der ganze Kreis, wie viel die Hälfte?", "Die Hälfte sind 180°. Die anderen beiden Winkel ergeben zusammen 180° und sind verschieden, zum Beispiel 100° und 80°.", gut=[[1, 179, 180]]), None, None)
neu(f, "saeulendiagramm", "V", 3, "parameter", VERH, "ja",
    bed("Zwei Säulen stehen für 12 und für 30 Kinder. Wähle einen Maßstab: 1 cm steht für □ Kinder. Beide Säulen sollen eine ganze Zahl von Zentimetern hoch sein, und die höhere Säule soll höchstens 10 cm hoch werden.", [G],
        [("mindestens 1 Kind je Zentimeter", [">=", "$1", 1], "$1", "Deine Zahl ist {}."),
         ("beide Höhen in ganzen Zentimetern", UND(["teilbar", 12, "$1"], ["teilbar", 30, "$1"]), ["/", 12, "$1"], "Die Säule für 12 Kinder wird bei dir {} cm hoch. Prüfe auch die andere."),
         ("höhere Säule höchstens 10 cm", ["<=", ["/", 30, "$1"], 10], ["/", 30, "$1"], "Deine höhere Säule wird {} cm hoch.")],
        [3], [([0], "mindestens 1 Kind je Zentimeter"), ([5], "beide Höhen in ganzen Zentimetern"), ([2], "höhere Säule höchstens 10 cm"), ([4], "beide Höhen in ganzen Zentimetern")],
        "Säulenhöhe ist Anzahl durch Maßstab.", "Die Zahl muss 12 und 30 teilen: 1, 2, 3 oder 6. Bei 1 und 2 wird die höhere Säule zu hoch (30 cm, 15 cm). Es passen 3 und 6.", gut=[[6]]), None, None)
hoch = lambda n: ["-", n, "$1"]
neu(f, "irrefuehrend", "V", 3, "transfer", KENNZ, "ja",
    bed("Zwei Säulen zeigen 40 und 50 Punkte. Bei welchem Achsenanfang (ganze Zahl von 0 bis 39) sieht die zweite Säule mindestens dreimal so hoch aus wie die erste?", [G],
        [("Achsenanfang von 0 bis 39", UND([">=", "$1", 0], ["<=", "$1", 39]), "$1", "Dein Achsenanfang ist {}."),
         ("zweite Säule mindestens dreimal so hoch", [">=", hoch(50), ["*", 3, hoch(40)]], ["/", hoch(50), hoch(40)], "Bei dir ist die zweite Säule {}-mal so hoch wie die erste.")],
        [35], [([40], "Achsenanfang von 0 bis 39"), ([30], "zweite Säule mindestens dreimal so hoch"), ([0], "zweite Säule mindestens dreimal so hoch")],
        "Die sichtbare Höhe ist der Wert minus der Achsenanfang.", "Beginnt die Achse bei 35, sind die Säulen 5 und 15 hoch – das Dreifache. Jeder Anfang von 35 bis 39 passt.", gut=[[39], [36]]), None, None)

# ═════════════════════ Kind 1 · Flug g1 · Größen und Einheiten ═════════════════════
f = "g1"
neu(f, "laenge", 4, 1, "direkt", GR, "nein",
    luecken("3,4 km in Meter: 1 km = ① m, also 3,4 km = ② m.", K(2), [1000, 3400], ["1000", "3.4 * 1000"],
            "In die kleinere Einheit nimmst du mal.", "1 km = 1 000 m. 3,4 · 1 000 = 3 400 m."),
    ["1000", "34*100"], {1: [(340, "fb.stellenwert.eine_stelle_daneben", "mit 100 statt mit 1 000 gerechnet"), (3004, None, "als 3 km und 4 m gelesen")]})
neu(f, "zeit", 4, 1, "direkt", GR, "nein",
    luecken("Von 9:40 Uhr bis 11:15 Uhr: Bis 10:00 Uhr sind es ① min. Von 10:00 Uhr bis 11:15 Uhr sind es ② min. Zusammen: ③ min.", K(3), [20, 75, 95], ["60 - 40", "60 + 15", "60 - 40 + 60 + 15"],
            "Rechne erst bis zur vollen Stunde.", "Bis 10:00 Uhr 20 min, dann 1 h 15 min = 75 min. Zusammen 95 min."),
    ["20", "75", "(11*60+15)-(9*60+40)"], {2: [(175, None, "wie mit Kommazahlen gerechnet: 11,15 − 9,40 = 1,75"), (135, None, "1 h 35 min als 135 min geschrieben")]})
neu(f, "schaetzen", 13, 1, "erkennen", GR, "ja",
    wahl("Du sollst die Höhe eines Zimmers schätzen. Welche Bezugsgröße hilft dir?", ["eine Tür (etwa 2 m hoch)", "eine Tafel Schokolade (100 g)", "eine Schulstunde (45 min)", "eine Packung Milch (1 Liter)"], 0,
         "Die Bezugsgröße muss dieselbe Art von Größe sein.", "Die Höhe ist eine Länge. Die Tür ist etwa 2 m hoch; das Zimmer ist etwas höher, etwa 2,50 m."),
    lambda: True, {1: (None, "Masse statt Länge"), 2: (None, "Zeit statt Länge"), 3: (None, "Rauminhalt statt Länge")})
neu(f, "kommaschreibweise", 12, 1, "erkennen", SW, "ja",
    wahl("Mia schreibt: 4 m 7 cm = 4,7 m. Was stimmt?", ["Mia hat recht.", "Richtig ist 47 m.", "Richtig ist 4,007 m.", "7 cm sind 0,07 m. Richtig ist 4,07 m."], 3,
         "Bei m und cm gibt es zwei Stellen hinter dem Komma.", "1 cm ist ein Hundertstel Meter. 7 cm = 0,07 m, also 4,07 m. 4,7 m wären 4 m 70 cm."),
    lambda: F(4) + F(7, 100) == F("4.07"), {0: ("fb.stellenwert.eine_stelle_daneben", "7 cm als 0,7 m: eine Stelle daneben"), 1: (None, "das Komma weggelassen"), 2: (None, "drei Stellen wie bei kg und g")})
neu(f, "rechnen", 13, 1, "erkennen", GR, "ja",
    wahl("Du sollst 2,5 kg + 750 g rechnen. Was tust du zuerst?", ["2,5 + 750 rechnen", "750 durch 2,5 teilen", "das Komma weglassen", "beide Größen in dieselbe Einheit bringen"], 3,
         "Vor plus und minus brauchen beide Größen dieselbe Einheit.", "Erst umrechnen: 2,5 kg = 2 500 g. Dann 2 500 g + 750 g = 3 250 g."),
    lambda: F("2.5") * 1000 + 750 == 3250, {0: (None, "verschiedene Einheiten zusammengezählt"), 1: (None, "falsche Rechenart"), 2: (None, "Weglassen des Kommas ist kein Umrechnen")})
neu(f, "masse", 17, 2, "umkehr", GR, "ja",
    zahl("□ g + 350 g = 1,2 kg. Welche Zahl gehört in das Kästchen?", 850, "1.2 * 1000 - 350",
         "Bring erst alles auf Gramm.", "1,2 kg = 1 200 g. 1 200 − 350 = 850.", einheit="g"),
    ["1200-350"], [(1550, "fb.gegenrechnung.gleiche_rechnung", "350 dazugezählt statt abgezogen"), (-230, "fb.stellenwert.eine_stelle_daneben", "1,2 kg als 120 g")])
neu(f, "rechnen", 14, 2, "mehrschritt", GR, "ja",
    luecken("1,5 m − 85 cm auf zwei Wegen. Weg A in cm: 150 cm − 85 cm = ① cm. Weg B in m: 1,50 m − 0,85 m = 0,② m.", K(2), [65, 65], ["150 - 85", "(1.5 - 0.85) * 100"],
            "Beide Wege müssen dieselbe Länge ergeben.", "150 − 85 = 65 cm. In Metern: 1,50 − 0,85 = 0,65 m. Das ist dasselbe."),
    ["65", "150-85"], {0: [(235, None, "dazugezählt statt abgezogen")]})
neu(f, "kommaschreibweise", "B", 2, "darstellung", SW, "ja",
    zahl("Schreibe 3 kg 40 g als Kommazahl in Kilogramm.", 3.04, "3 + 40 / 1000",
         "Bei kg und g gibt es drei Stellen hinter dem Komma.", "40 g = 0,040 kg. Also 3,040 kg = 3,04 kg.", einheit="kg"),
    ["3040/1000"], [(3.4, "fb.stellenwert.eine_stelle_daneben", "40 g als 0,4 kg"), (3.004, "fb.stellenwert.eine_stelle_daneben", "40 g als 0,004 kg")])
neu(f, "laenge", "B", 2, "mehrschritt", GR, "ja",
    wahl("Welche Länge ist am größten?", ["0,5 km", "480 m", "51 000 cm", "5 300 dm"], 3,
         "Rechne alle vier in dieselbe Einheit um.", "In Metern: 500 m, 480 m, 510 m und 530 m. Am größten sind 5 300 dm."),
    lambda: max((500, 0), (480, 1), (F(51000, 100), 2), (F(5300, 10), 3))[1] == 3, {0: (None, "die größte Einheit gewählt"), 1: (None, "nicht umgerechnet"), 2: (None, "nur die Maßzahl verglichen")})
neu(f, "laenge", "A", 2, "mehrschritt", GR, "ja",
    zahl("Von einem 1,2 m langen Band werden Stücke von je 15 cm abgeschnitten. Wie viele Stücke werden es?", 8, "120 // 15",
         "Bring beide Längen auf dieselbe Einheit.", "1,2 m = 120 cm. 120 : 15 = 8 Stücke."),
    ["1200/150"], [(0.08, None, "1,2 : 15 ohne Umrechnen"), (80, "fb.stellenwert.eine_stelle_daneben", "1,2 m als 1 200 cm")])
neu(f, "massstab", 17, 2, "umkehr", VERH, "ja",
    zahl("Zwei Orte liegen 4 km auseinander. Wie viele Zentimeter sind das auf einer Karte im Maßstab 1 : 50 000?", 8, "4 * 100000 // 50000",
         "Rechne die 4 km erst in Zentimeter um. Auf der Karte ist alles 50 000-mal kleiner.", "4 km = 400 000 cm. 400 000 : 50 000 = 8 cm."),
    ["400000/50000"], [(0.8, "fb.stellenwert.eine_stelle_daneben", "4 km als 40 000 cm"), (200000, "fb.verhaeltnis.falsche_richtung", "4 · 50 000 gerechnet")])
neu(f, "verstehen", "A", 2, "einkleidung", GR, "ja",
    wahl("Auf einem Schild steht: „Brücke bis 3,5 t“. Ein Lieferwagen wiegt 2 800 kg und hat 900 kg geladen. Darf er über die Brücke fahren?",
         ["Ja, 3 700 kg sind weniger als 35 000 kg.", "Nein, er wiegt zusammen 3 700 kg. Erlaubt sind 3 500 kg.", "Ja, 2 800 kg sind weniger als 3,5 t.", "Nein, er wiegt 37 t."], 1,
         "Bring beide Angaben auf dieselbe Einheit.", "2 800 kg + 900 kg = 3 700 kg. 3,5 t = 3 500 kg. Der Wagen ist 200 kg zu schwer."),
    lambda: 2800 + 900 > F("3.5") * 1000, {0: ("fb.stellenwert.eine_stelle_daneben", "3,5 t als 35 000 kg"), 2: (None, "die Ladung vergessen"), 3: ("fb.stellenwert.eine_stelle_daneben", "3 700 kg als 37 t")})
neu(f, "massstab", 12, 3, "fehler", VERH, "ja",
    zahl("Ein Käfer ist in einem Buch im Maßstab 5 : 1 abgebildet und dort 6 cm lang. Jan sagt: „In Wirklichkeit ist er 30 cm lang.“ Wie viele Millimeter ist der Käfer wirklich lang?", 12, "6 * 10 // 5",
         "5 : 1 heißt: Das Bild ist 5-mal so groß wie der Käfer.", "Das Bild ist vergrößert. Wirklich: 6 cm : 5 = 1,2 cm = 12 mm.", einheit="mm"),
    ["60/5"], [(300, "fb.verhaeltnis.falsche_richtung", "wie Jan vergrößert statt verkleinert"), (1.2, None, "in Zentimetern angegeben")])
neu(f, "zeit", 17, 3, "rueckwaerts", GR, "ja",
    luecken("Ein Film dauert 1 h 50 min und endet um 21:15 Uhr. Wann hat er begonnen?", "□:□ Uhr", [19, 25], ["(21 * 60 + 15 - 110) // 60", "(21 * 60 + 15 - 110) % 60"],
            "Geh erst 2 Stunden zurück und dann 10 Minuten wieder vor.", "2 Stunden vor 21:15 Uhr ist 19:15 Uhr. Der Film ist 10 Minuten kürzer, also begann er um 19:25 Uhr.", "Erst die Stunde, dann die Minuten."),
    ["(21*60+15-110-25)/60", "(21*60+15-110)-19*60"], {0: [(20, None, "nur die volle Stunde abgezogen")], 1: [(35, None, "50 − 15 gerechnet, statt über die volle Stunde zu gehen"), (5, None, "10 Minuten in die falsche Richtung")]})
neu(f, "laenge", "V", 1, "direkt", GR, "ja",
    bed("Nenne eine Länge in ganzen Zentimetern, die größer als 1,2 m und kleiner als 1,3 m ist.", [G],
        [("größer als 1,2 m", [">", "$1", 120], "$1", "Deine Länge ist {} cm."), ("kleiner als 1,3 m", ["<", "$1", 130], "$1", "Deine Länge ist {} cm.")],
        [125], [([12], "größer als 1,2 m"), ([130], "kleiner als 1,3 m"), ([1250], "kleiner als 1,3 m"), ([120], "größer als 1,2 m")],
        "Rechne beide Grenzen in Zentimeter um.", "1,2 m = 120 cm und 1,3 m = 130 cm. Es passt jede Zahl von 121 bis 129.", gut=[[121], [129]]), None, None)
neu(f, "masse", "V", 2, "umkehr", GR, "ja",
    bed("Zwei Pakete wiegen zusammen genau 2 kg. Das erste ist schwerer als 1,2 kg. Nenne beide Gewichte in Gramm.", [G, G],
        [("zusammen 2 kg", ["=", ["summe", "$alle"], 2000], ["summe", "$alle"], "Zusammen wiegen deine Pakete {} g."), ("erstes Paket schwerer als 1,2 kg", [">", "$1", 1200], "$1", "Dein erstes Paket wiegt {} g."),
         ("jedes Paket wiegt mehr als 0 g", [">", "$2", 0], "$2", "Dein zweites Paket wiegt {} g.")],
        [1500, 500], [([1500, 600], "zusammen 2 kg"), ([1200, 800], "erstes Paket schwerer als 1,2 kg"), ([2000, 0], "jedes Paket wiegt mehr als 0 g"), ([2, 0], "zusammen 2 kg")],
        "Rechne die Kilogramm-Angaben in Gramm um.", "2 kg = 2 000 g. Das erste Paket wiegt mehr als 1 200 g, das zweite den Rest, zum Beispiel 1 500 g und 500 g.", gut=[[1201, 799], [1999, 1]]), None, None)
bis12 = ["-", 720, ["+", ["*", 60, "$1"], "$2"]]
neu(f, "zeit", "V", 2, "mehrschritt", GR, "ja",
    bed("Nenne eine Uhrzeit am Vormittag (Stunde und Minute). Von ihr bis 12:00 Uhr sollen es mehr als 90 Minuten sein, aber weniger als 2 Stunden.", [G, G],
        [("Uhrzeit am Vormittag", UND([">=", "$1", 0], ["<=", "$1", 11], [">=", "$2", 0], ["<=", "$2", 59]), None, "Das ist keine Uhrzeit am Vormittag. Stunde von 0 bis 11, Minute von 0 bis 59."),
         ("mehr als 90 Minuten bis 12:00 Uhr", [">", bis12, 90], bis12, "Von deiner Uhrzeit bis 12:00 Uhr sind es {} Minuten."), ("weniger als 2 Stunden bis 12:00 Uhr", ["<", bis12, 120], bis12, "Von deiner Uhrzeit bis 12:00 Uhr sind es {} Minuten.")],
        [10, 15], [([10, 75], "Uhrzeit am Vormittag"), ([10, 30], "mehr als 90 Minuten bis 12:00 Uhr"), ([10, 0], "weniger als 2 Stunden bis 12:00 Uhr"), ([9, 45], "weniger als 2 Stunden bis 12:00 Uhr")],
        "90 Minuten sind 1 h 30 min. Geh von 12:00 Uhr aus zurück.", "2 Stunden vor 12:00 Uhr ist 10:00 Uhr, 90 Minuten davor ist 10:30 Uhr. Es passt jede Uhrzeit von 10:01 Uhr bis 10:29 Uhr.", gut=[[10, 1], [10, 29]]), None, None)
neu(f, "rechnen", "V", 2, "mehrschritt", GR, "ja",
    bed("Nenne drei verschiedene Längen in ganzen Zentimetern, die zusammen genau 2,5 m ergeben. Jede soll länger als ein halber Meter sein.", [G, G, G],
        [("verschieden", ["verschieden", "$alle"], None, "Die drei Längen sollen verschieden sein."), ("jede länger als ein halber Meter", [">", ["min", "$alle"], 50], ["min", "$alle"], "Deine kürzeste Länge ist {} cm."),
         ("zusammen 2,5 m", ["=", ["summe", "$alle"], 250], ["summe", "$alle"], "Zusammen sind es bei dir {} cm.")],
        [60, 90, 100], [([80, 80, 90], "verschieden"), ([50, 90, 110], "jede länger als ein halber Meter"), ([60, 90, 110], "zusammen 2,5 m")],
        "Rechne 2,5 m und den halben Meter in Zentimeter um.", "2,5 m = 250 cm, ein halber Meter = 50 cm. Zum Beispiel 60 cm, 90 cm und 100 cm.", gut=[[51, 52, 147]]), None, None)
plan = ["/", 400, "$1"]
neu(f, "massstab", "V", 3, "parameter", VERH, "ja",
    bed("Ein Zimmer ist 4 m lang. Wähle einen Maßstab 1 : □ (ganze Zahl), bei dem das Zimmer auf dem Plan länger als 5 cm, aber kürzer als 12 cm ist.", [G],
        [("Maßstabszahl größer als 0", [">", "$1", 0], "$1", "Deine Zahl ist {}."), ("auf dem Plan länger als 5 cm", [">", plan, 5], plan, "Auf deinem Plan ist das Zimmer {} cm lang."),
         ("auf dem Plan kürzer als 12 cm", ["<", plan, 12], plan, "Auf deinem Plan ist das Zimmer {} cm lang.")],
        [50], [([0], "Maßstabszahl größer als 0"), ([100], "auf dem Plan länger als 5 cm"), ([20], "auf dem Plan kürzer als 12 cm"), ([80], "auf dem Plan länger als 5 cm")],
        "Planlänge ist wirkliche Länge durch Maßstabszahl. Rechne die 4 m erst in Zentimeter um.", "4 m = 400 cm. Bei 1 : 50 sind es 8 cm. Es passt jede Zahl von 34 bis 79.", gut=[[40], [34], [79]]), None, None)

# ═════════════════════ Kind 2 · Flug g8 · Prozent mit verändertem Grundwert (Klasse 7) ═════════════════════
f = "g8"
neu(f, "faktor", 4, 1, "direkt", PROZ, "nein",
    luecken("Ein Preis sinkt um 35 %. Es bleiben ① % des alten Preises. Der Faktor ist 0,②.", K(2), [65, 65], ["100 - 35", "100 - 35"],
            "Rechne erst 100 % minus den Rabatt.", "100 % − 35 % = 65 %. Als Faktor: 0,65."),
    ["65", "130/2"], {1: [(35, None, "den Rabatt selbst als Faktor genommen")]})
neu(f, "faktor", 13, 1, "erkennen", PROZ, "ja",
    wahl("Ein Wert soll um 4 % erhöht werden. Mit welchem Faktor rechnest du?", ["1,4", "0,04", "1,04", "4"], 2,
         "Rechne erst 100 % plus 4 %.", "100 % + 4 % = 104 % = 1,04."),
    lambda: F(104, 100) == F("1.04"), {0: ("fb.stellenwert.eine_stelle_daneben", "4 % als 0,4"), 1: (None, "nur den Zuwachs genommen"), 3: (None, "die Prozentzahl als Faktor")})
neu(f, "prozentsatz", "B", 1, "direkt", PROZ, "ja",
    zahl("Nach einer Änderung ist ein Wert das 0,85-Fache des alten Werts. Um wie viel Prozent hat er abgenommen?", 15, "100 - 85",
         "Schreibe den Faktor in Prozent und vergleiche mit 100 %.", "0,85 = 85 %. Bis 100 % fehlen 15 %.", einheit="%"),
    ["(1-85/100)*100"], [(85, None, "den Rest statt der Abnahme genannt"), (0.15, None, "als Dezimalzahl statt in Prozent")])
neu(f, "zurueck", 4, 2, "mehrschritt", GEGEN, "nein",
    luecken("Nach 20 % Rabatt kostet eine Jacke 64 €. Der Faktor war 0,①. Zurück zum alten Preis: 64 € : 0,① = ② €.", K(2), [8, 80], ["(100 - 20) // 10", "64 * 10 // 8"],
            "Teilen macht das Malnehmen rückgängig.", "Faktor 0,8. 64 € : 0,8 = 80 €. Probe: 80 € · 0,8 = 64 €."),
    ["8", "640/8"], {1: [(76.8, "fb.prozent.falscher_grundwert", "20 % von 64 € aufgeschlagen")]})
neu(f, "vermindert", 14, 2, "mehrschritt", PROZ, "ja",
    luecken("Ein Pullover kostet 60 €, es gibt 30 % Rabatt. Weg A: Rabatt ausrechnen und abziehen: 60 € − ① € = ② €. Weg B: 60 € · 0,7.", K(2), [18, 42], ["60 * 30 // 100", "60 - 60 * 30 // 100"],
            "Beide Wege müssen denselben Preis ergeben.", "30 % von 60 € sind 18 €. 60 € − 18 € = 42 €. Weg B: 60 · 0,7 = 42."),
    ["18", "60*7/10"], {1: [(18, None, "den Rabatt statt des neuen Preises genannt"), (30, None, "30 € statt 30 % abgezogen")]})
neu(f, "vermehrt", 17, 2, "umkehr", PROZ, "ja",
    zahl("Ein Preis von 250 € wird erhöht und beträgt danach 265 €. Mit welchem Faktor wurde er malgenommen?", 1.06, "265 / 250",
         "Teile neu durch alt.", "265 : 250 = 1,06. Das ist eine Erhöhung um 6 %."),
    ["530/500"], [(15, None, "den Unterschied in Euro genannt"), (6, None, "den Prozentsatz statt des Faktors genannt"), (1.6, "fb.stellenwert.eine_stelle_daneben", "6 % als 0,6")])
neu(f, "vermehrt", "B", 2, "darstellung", PROZ, "ja",
    wahl("Die Tabelle zeigt alte und neue Preise. Bei welchem Artikel wurde der Preis mit dem Faktor 1,2 malgenommen?", ["Heft", "Mappe", "Stift"], 1,
         "Rechne für jede Zeile neu durch alt.", "Mappe: 6 : 5 = 1,2. Heft: 2,20 : 2 = 1,1. Stift: 1,65 : 1,50 = 1,1.",
         grafik=TAB(["Artikel", "alt", "neu"], ["Heft", "2,00 €", "2,20 €"], ["Mappe", "5,00 €", "6,00 €"], ["Stift", "1,50 €", "1,65 €"])),
    lambda: F(6, 5) == F("1.2") and F(220, 200) == F(165, 150) == F("1.1"), {0: (None, "20 Cent mehr mit 20 % verwechselt"), 2: (None, "nicht nachgerechnet")})
neu(f, "mehrfach", 12, 2, "mehrschritt", PROZ, "ja",
    wahl("Ein Preis steigt erst um 20 % und sinkt dann um 20 %. Was gilt für den Endpreis?",
         ["Er ist wieder so hoch wie am Anfang.", "Er ist 4 % höher als am Anfang.", "Er ist 40 % niedriger als am Anfang.", "Er ist 4 % niedriger als am Anfang."], 3,
         "Nimm die beiden Faktoren mal.", "1,2 · 0,8 = 0,96. Der Endpreis liegt 4 % unter dem Anfangspreis: Die 20 % Rabatt beziehen sich auf den höheren Preis."),
    lambda: F(12, 10) * F(8, 10) == F(96, 100), {0: ("fb.prozent.prozente_addiert", "plus 20 % und minus 20 % zu 0 % addiert"), 1: (None, "Richtung der Änderung verwechselt"), 2: (None, "die Prozentsätze zusammengezählt")})
neu(f, "mehrfach", 14, 2, "mehrschritt", PROZ, "ja",
    zahl("Erst 10 % Rabatt, dann noch einmal 10 % Rabatt auf den neuen Preis. Mit welchem einen Faktor kommst du direkt vom alten Preis zum Endpreis?", 0.81, "0.9 * 0.9",
         "Bei mehreren Änderungen nimmst du die Faktoren mal.", "0,9 · 0,9 = 0,81. Das sind zusammen 19 % Rabatt, nicht 20 %."),
    ["81/100"], [(0.8, "fb.prozent.prozente_addiert", "10 % + 10 % = 20 % gerechnet"), (0.9, None, "nur einen Rabatt beachtet")])
neu(f, "formel", "A", 2, "mehrschritt", PROZ, "ja",
    zahl("500 € werden zu 2 % Zinsen im Jahr angelegt. Die Zinsen bleiben auf dem Konto. Wie viel Euro sind es nach 2 Jahren?", 520.2, "500 * 1.02 ** 2",
         "Jedes Jahr mal 1,02.", "500 € · 1,02 = 510 €. 510 € · 1,02 = 520,20 €.", einheit="€"),
    ["500*102*102/10000"], [(520, "fb.wachstum.plus_statt_mal", "zweimal 10 € dazugezählt"), (510, None, "nur ein Jahr gerechnet")])
neu(f, "zurueck", 12, 3, "fehler", PROZ, "ja",
    zahl("Ein Fahrrad kostet nach einer Preiserhöhung um 25 % jetzt 500 €. Ben rechnet: 500 € − 25 % = 375 €. Wie viel Euro kostete das Rad vorher wirklich?", 400, "500 * 100 // 125",
         "Die 25 % beziehen sich auf den alten Preis, nicht auf 500 €.", "Alter Preis · 1,25 = 500 €. Also 500 € : 1,25 = 400 €. Probe: 400 € + 100 € = 500 €.", einheit="€"),
    ["500/5*4"], [(375, "fb.prozent.falscher_grundwert", "wie Ben: 25 % vom neuen Preis abgezogen"), (625, None, "noch einmal erhöht")])
neu(f, "prozentsatz", 12, 3, "fehler", PROZ, "ja",
    zahl("Ein Preis fällt von 50 € auf 40 €. Anna sagt: „Er ist um 25 % gefallen, denn 10 € sind 25 % von 40 €.“ Um wie viel Prozent ist er wirklich gefallen?", 20, "(50 - 40) * 100 // 50",
         "Worauf bezieht sich die Änderung: auf alt oder auf neu?", "Verglichen wird mit dem alten Preis: 10 € von 50 € sind 20 %.", einheit="%"),
    ["10/50*100"], [(25, "fb.prozent.falscher_grundwert", "wie Anna auf den neuen Preis bezogen"), (10, None, "Euro als Prozent genommen")])
neu(f, "mehrfach", 17, 3, "rueckwaerts", PROZ, "ja",
    zahl("Ein Preis wurde um 25 % erhöht. Um wie viel Prozent muss der neue Preis sinken, damit wieder der alte Preis gilt?", 20, "100 - 100 * 100 // 125",
         "Mit welchem Faktor kommst du von 1,25 zurück zur 1?", "1 : 1,25 = 0,8. Der neue Preis muss um 20 % sinken. Beispiel: 100 € → 125 € → 100 €; 25 € von 125 € sind 20 %.", einheit="%"),
    ["(1-4/5)*100"], [(25, "fb.prozent.falscher_grundwert", "dieselben 25 % genommen")])
neu(f, "formel", 17, 3, "parameter", PROZ, "ja",
    zahl("Ein Kapital wächst in 2 Jahren von 400 € auf 484 €, jedes Jahr mit demselben Faktor. Wie viel Prozent Zinsen gibt es im Jahr?", 10, "(1.1 - 1) * 100",
         "Welcher Faktor ergibt zweimal hintereinander 1,21?", "484 : 400 = 1,21. Gesucht ist q mit q · q = 1,21: q = 1,1. Das sind 10 % im Jahr.", einheit="%"),
    ["110-100"], [(21, None, "den ganzen Zuwachs als Jahreszins genommen"), (10.5, "fb.prozent.prozente_addiert", "21 % durch 2 geteilt")], probe=lambda: 400 * F(11, 10) ** 2 == 484)
neu(f, "argumente", 12, 3, "begruenden", PROZ, "ja",
    wahl("Ein Laden wirbt: „Erst 50 % Rabatt, dann noch einmal 50 % – also geschenkt!“ Welche Rechnung zeigt, was wirklich gilt?",
         ["0,5 · 0,5 = 0,25: Ein Viertel des Preises ist noch zu zahlen.", "50 % + 50 % = 100 %: Es stimmt, die Ware ist geschenkt.", "0,5 + 0,5 = 1: Der Preis bleibt gleich.", "50 · 50 = 2 500: Der Rabatt ist noch größer."], 0,
         "Der zweite Rabatt bezieht sich auf den schon halbierten Preis.", "Die Faktoren werden malgenommen: 0,5 · 0,5 = 0,25. Es bleiben 25 % des Preises zu zahlen."),
    lambda: F(1, 2) * F(1, 2) == F(1, 4), {1: ("fb.prozent.prozente_addiert", "die Prozentsätze addiert"), 2: (None, "Faktoren addiert statt malgenommen"), 3: (None, "Prozentzahlen malgenommen")})
neu(f, "faktor", "V", 1, "direkt", PROZ, "ja",
    bed("Nenne einen Faktor, der einen Wert um mehr als 10 %, aber um weniger als 20 % verkleinert.", [R],
        [("verkleinert um mehr als 10 %", ["<", "$1", "0,9"], ["*", "$1", 100], "Mit deinem Faktor bleiben {} % des Werts."), ("verkleinert um weniger als 20 %", [">", "$1", "0,8"], ["*", "$1", 100], "Mit deinem Faktor bleiben {} % des Werts.")],
        ["0,85"], [(["0,95"], "verkleinert um mehr als 10 %"), (["0,8"], "verkleinert um weniger als 20 %"), (["1,15"], "verkleinert um mehr als 10 %"), ([15], "verkleinert um mehr als 10 %")],
        "Wie viel Prozent bleiben nach dem Verkleinern?", "Es bleiben zwischen 80 % und 90 %. Der Faktor liegt zwischen 0,8 und 0,9, zum Beispiel 0,85.", gut=[["0,82"], ["7/8"]]), None, None)
nachher = ["/", ["*", "$1", ["-", 100, "$2"]], 100]
neu(f, "vermindert", "V", 2, "umkehr", PROZ, "ja",
    bed("Ein Artikel kostet nach einem Rabatt genau 60 €. Nenne einen möglichen alten Preis in Euro und den Rabatt in Prozent. Der Rabatt soll mindestens 10 % betragen.", [R, R],
        [("Rabatt mindestens 10 %", UND([">=", "$2", 10], ["<", "$2", 100]), "$2", "Dein Rabatt ist {} %."), ("neuer Preis ist 60 €", ["=", nachher, 60], nachher, "Mit deinen Zahlen kostet der Artikel danach {} €.")],
        [75, 20], [([63, 5], "Rabatt mindestens 10 %"), ([70, 20], "neuer Preis ist 60 €"), ([60, 100], "Rabatt mindestens 10 %")],
        "Alter Preis mal Faktor ergibt 60 €.", "Zum Beispiel 75 € mit 20 % Rabatt: 75 · 0,8 = 60. Oder 80 € mit 25 %, 100 € mit 40 %, 120 € mit 50 %.", gut=[[80, 25], [100, 40], [120, 50]]), None, None)
neu(f, "mehrfach", "V", 2, "umkehr", PROZ, "ja",
    bed("Nenne zwei positive Faktoren, die nacheinander angewendet einen Wert genau halbieren. Keiner der beiden Faktoren soll 0,5 oder 1 sein.", [R, R],
        [("beide Faktoren positiv", [">", ["min", "$alle"], 0], ["min", "$alle"], "Dein kleinerer Faktor ist {}."),
         ("kein Faktor ist 0,5 oder 1", UND(["!=", "$1", "0,5"], ["!=", "$1", 1], ["!=", "$2", "0,5"], ["!=", "$2", 1]), None, "Einer deiner Faktoren ist 0,5 oder 1."),
         ("zusammen wird halbiert", ["=", ["*", "$1", "$2"], "0,5"], ["*", "$1", "$2"], "Nacheinander ergeben deine Faktoren den Faktor {}.")],
        ["0,8", "0,625"], [([-1, "-0,5"], "beide Faktoren positiv"), ([1, "0,5"], "kein Faktor ist 0,5 oder 1"), (["0,8", "0,6"], "zusammen wird halbiert"), (["0,25", "0,25"], "zusammen wird halbiert")],
        "Was machst du mit zwei Faktoren, die nacheinander wirken?", "Die Faktoren werden malgenommen und müssen 0,5 ergeben, zum Beispiel 0,8 · 0,625 oder 2 · 0,25.", gut=[[2, "0,25"], ["1,25", "0,4"]]), None, None)
ende = ["/", ["*", ["+", 100, "$1"], ["-", 100, "$2"]], 100]
neu(f, "zurueck", "V", 3, "parameter", PROZ, "ja",
    bed("Ein Preis wird erst um p % erhöht und danach um q % gesenkt. Am Ende ist er genau so hoch wie am Anfang. Nenne p und q. Beide sollen größer als 0 sein.", [R, R],
        [("beide größer als 0", [">", ["min", "$alle"], 0], ["min", "$alle"], "Deine kleinere Zahl ist {}."), ("Endpreis gleich Anfangspreis", ["=", ende, 100], ende, "Aus 100 € werden mit deinen Zahlen am Ende {} €.")],
        [25, 20], [([0, 0], "beide größer als 0"), ([20, 20], "Endpreis gleich Anfangspreis"), ([25, 25], "Endpreis gleich Anfangspreis")],
        "Die beiden Faktoren müssen malgenommen 1 ergeben.", "Zum Beispiel plus 25 % und minus 20 %: 1,25 · 0,8 = 1. Oder plus 100 % und minus 50 %: 2 · 0,5 = 1.", gut=[[100, 50], [60, "37,5"]]), None, None)
konto = ["/", ["hoch", ["+", 100, "$1"], 2], 10]
neu(f, "formel", "V", 3, "transfer", PROZ, "ja",
    bed("1 000 € werden zwei Jahre lang mit demselben Zinssatz verzinst; die Zinsen bleiben auf dem Konto. Nenne einen Zinssatz in Prozent, bei dem am Ende mehr als 1 100 €, aber weniger als 1 200 € auf dem Konto sind.", [R],
        [("Zinssatz größer als 0", [">", "$1", 0], "$1", "Dein Zinssatz ist {} %."), ("am Ende mehr als 1 100 €", [">", konto, 1100], konto, "Nach zwei Jahren sind es bei dir {} €."),
         ("am Ende weniger als 1 200 €", ["<", konto, 1200], konto, "Nach zwei Jahren sind es bei dir {} €.")],
        [5], [([-205], "Zinssatz größer als 0"), ([4], "am Ende mehr als 1 100 €"), ([10], "am Ende weniger als 1 200 €")],
        "Rechne mit Kₙ = K₀ · qⁿ und probiere einen Zinssatz aus.", "Bei 5 %: 1 000 € · 1,05 · 1,05 = 1 102,50 €. Es passen die Zinssätze von 5 % bis 9 %; bei 10 % sind es schon 1 210 €.", gut=[[9], ["7,5"]]), None, None)

# ═════════════════════ Kind 2 · Flug g2-teil2 · Dreisatz Teil 2 (drei Lernkarten: erkennen, vervielfachen, pruefen) ═════════════════════
f = "g2-teil2"
neu(f, "vervielfachen", 4, 1, "direkt", WERT, "nein",
    luecken("4 Hefte kosten 6 €. 8 Hefte sind ①-mal so viele; sie kosten ② €. 2 Hefte kosten ③ €.", K(3), [2, 12, 3], ["8 // 4", "6 * 2", "6 // 2"],
            "Was du mit der Menge tust, tust du auch mit dem Preis.", "Doppelte Menge, doppelter Preis: 12 €. Halbe Menge, halber Preis: 3 €."),
    ["2", "8*6/4", "2*6/4"], {1: [(10, "fb.verhaeltnis.addiert_statt_malgenommen", "4 Hefte mehr, also 4 € mehr")], 2: [(4, "fb.verhaeltnis.addiert_statt_malgenommen", "2 Hefte weniger, also 2 € weniger")]})
neu(f, "pruefen", 4, 1, "direkt", WERT, "nein",
    luecken("Ist die Preisliste proportional? 2 kg kosten 5 €, 6 kg kosten 15 €, 10 kg kosten 24 €. Rechne jeweils den Preis für 1 kg in Cent: ①, ②, ③.", K(3), [250, 250, 240], ["500 // 2", "1500 // 6", "2400 // 10"],
            "Teile jeden Preis durch seine Menge.", "5 € : 2 = 2,50 €. 15 € : 6 = 2,50 €. 24 € : 10 = 2,40 €. Der letzte Wert weicht ab: nicht proportional.", "Je Lücke ein Preis in Cent."),
    ["5*100/2", "15*100/6", "24*100/10"], {})
neu(f, "erkennen", 13, 1, "erkennen", WERT, "ja",
    wahl("Bei welcher dieser vier Zuordnungen gehört zur doppelten Menge immer der doppelte Wert?", ["Alter → Körpergröße", "Anzahl der Arbeiter → Dauer der Arbeit", "Anzahl gleicher Brötchen → Preis", "Uhrzeit → Temperatur"], 2,
         "Prüfe: Gehört zur doppelten Menge der doppelte Wert?", "Doppelt so viele Brötchen kosten doppelt so viel. Bei den anderen stimmt das nicht."),
    lambda: True, {0: (None, "„wächst mit“ für proportional gehalten"), 1: (None, "je mehr, desto weniger: nicht proportional"), 3: (None, "kein fester Zusammenhang")})
neu(f, "erkennen", 12, 1, "erkennen", WERT, "ja",
    wahl("Ein Kind ist mit 5 Jahren 110 cm groß. Lina sagt: „Dann ist es mit 10 Jahren 220 cm groß.“ Was ist falsch?",
         ["Die Zuordnung Alter → Größe ist nicht proportional.", "Lina hat falsch verdoppelt.", "Nichts: doppeltes Alter, doppelte Größe.", "Lina müsste 110 + 5 rechnen."], 0,
         "Darf man hier überhaupt verdoppeln?", "Menschen wachsen nicht gleichmäßig weiter. Die Zuordnung ist nicht proportional, also gilt „doppelt – doppelt“ nicht."),
    lambda: 2 * 110 == 220, {1: (None, "die Rechnung 2 · 110 = 220 stimmt; falsch ist die Annahme"), 2: (None, "Proportionalität ungeprüft angenommen"), 3: ("fb.verhaeltnis.addiert_statt_malgenommen", "addiert statt geprüft")})
neu(f, "pruefen", "B", 1, "direkt", WERT, "ja",
    zahl("In einer proportionalen Tabelle gehört zu 4 Stück der Preis 10 €. Welche Zahl kommt in jeder Spalte bei „Preis : Menge“ heraus?", 2.5, "10 / 4",
         "Rechne Preis geteilt durch Menge.", "10 : 4 = 2,5. In einer proportionalen Tabelle ist dieser Wert in jeder Spalte gleich."),
    ["5/2"], [(0.4, "fb.verhaeltnis.falsche_richtung", "Menge : Preis gerechnet"), (6, None, "abgezogen statt geteilt"), (40, None, "malgenommen statt geteilt")])
neu(f, "pruefen", 12, 2, "darstellung", WERT, "ja",
    wahl("Die Tabelle soll proportional sein. Ein Preis ist falsch. Welcher?", ["der Preis bei 2 kg", "der Preis bei 3 kg", "der Preis bei 5 kg", "der Preis bei 8 kg"], 2,
         "Rechne für jede Spalte Preis : Menge.", "7 : 2 = 3,5. 10,50 : 3 = 3,5. 28 : 8 = 3,5. Aber 18 : 5 = 3,6. Richtig wären 17,50 €.",
         grafik=TAB(["Menge (kg)", "2", "3", "5", "8"], ["Preis (€)", "7", "10,50", "18", "28"])),
    lambda: F(7, 2) == F(21, 6) == F(28, 8) != F(18, 5), {0: (None, "nicht für jede Spalte gerechnet"), 1: (None, "die Kommazahl für den Fehler gehalten"), 3: (None, "nicht für jede Spalte gerechnet")})
neu(f, "vervielfachen", 17, 2, "umkehr", VERH, "ja",
    zahl("Die Tabelle ist proportional. Welche Zahl fehlt?", 14, "21 * 4 // 6",
         "Wie kommst du von 6 € zu 21 €? Dasselbe tust du mit den Litern.", "1 Liter kostet 6 € : 4 = 1,50 €. 21 € : 1,50 € = 14 Liter.", einheit="Liter",
         grafik=TAB(["Liter", "4", "?"], ["Preis (€)", "6", "21"])),
    ["21/(6/4)"], [(19, "fb.verhaeltnis.addiert_statt_malgenommen", "15 € mehr, also 15 Liter mehr"), (31.5, "fb.verhaeltnis.falsche_richtung", "mal 1,5 statt geteilt durch 1,5")])
neu(f, "vervielfachen", 14, 2, "mehrschritt", VERH, "ja",
    luecken("6 Flaschen kosten 9 €. Gesucht ist der Preis für 10 Flaschen. Weg A über 1 Flasche: 9 € : 6 = 1,50 €, dann mal 10. Weg B über 2 Flaschen: 2 Flaschen kosten ① €, 10 Flaschen kosten ② €.", K(2), [3, 15],
            ["9 // 3", "9 // 3 * 5"], "Von 6 nach 2 teilst du durch 3. Von 2 nach 10 nimmst du mal 5.", "2 Flaschen: 9 € : 3 = 3 €. 10 Flaschen: 3 € · 5 = 15 €. Weg A: 1,50 € · 10 = 15 €."),
    ["3", "10*9/6"], {1: [(13, "fb.verhaeltnis.addiert_statt_malgenommen", "4 Flaschen mehr, also 4 € mehr")]})
neu(f, "erkennen", 12, 2, "einkleidung", WERT, "ja",
    wahl("Ein Taxi kostet 4 € Grundpreis und dazu 2 € je Kilometer. Ist die Zuordnung Kilometer → Preis proportional?",
         ["Ja, jeder Kilometer kostet gleich viel.", "Nein, zu 0 km gehören schon 4 €.", "Ja, der Preis steigt gleichmäßig.", "Nein, weil der Preis nicht steigt."], 1,
         "Was gehört zu 0 km? Und kostet die doppelte Strecke das Doppelte?", "1 km kostet 6 €, 2 km kosten 8 € – nicht das Doppelte. Bei proportional gehört zu 0 die 0."),
    lambda: (4 + 2 * 2) != 2 * (4 + 2 * 1), {0: (None, "gleichmäßig steigend mit proportional verwechselt"), 2: (None, "gleichmäßig steigend mit proportional verwechselt"), 3: (None, "der Preis steigt sehr wohl")})
neu(f, "pruefen", 17, 2, "umkehr", WERT, "ja",
    zahl("Die Paare (3 | 12), (5 | 20) und (8 | □) sollen zu einer proportionalen Zuordnung gehören. Welche Zahl fehlt?", 32, "12 // 3 * 8",
         "Welche Zahl kommt bei „Wert : Menge“ heraus?", "12 : 3 = 4 und 20 : 5 = 4. Also 8 · 4 = 32."),
    ["8*20/5"], [(23, "fb.verhaeltnis.addiert_statt_malgenommen", "von 5 nach 8 sind es 3 mehr: 20 + 3"), (28, "fb.verhaeltnis.addiert_statt_malgenommen", "wie von 12 nach 20 um 8 erhöht")])
neu(f, "vervielfachen", 12, 3, "fehler", VERH, "ja",
    zahl("5 Karten kosten 8 €. Paul rechnet für 15 Karten: „10 Karten mehr, also 10 € mehr: 18 €.“ Wie viel Euro kosten 15 Karten wirklich?", 24, "8 * 3",
         "15 Karten sind wievielmal so viele wie 5?", "15 ist das Dreifache von 5. Also auch der dreifache Preis: 3 · 8 € = 24 €.", einheit="€"),
    ["15*8/5"], [(18, "fb.verhaeltnis.addiert_statt_malgenommen", "wie Paul einen festen Betrag dazugezählt")])
neu(f, "pruefen", 13, 3, "begruenden", WERT, "ja",
    wahl("Ein Boot kostet für 2 Stunden 14 €, für 3 Stunden 21 € und für 5 Stunden 30 €. Welche Begründung stimmt?",
         ["Proportional, denn der Preis steigt mit der Zeit.", "Proportional, denn 2 + 3 = 5.", "Nicht proportional, weil 5 Stunden keine Verdopplung sind.", "Nicht proportional: 14 : 2 und 21 : 3 ergeben 7, aber 30 : 5 ergibt 6."], 3,
         "Rechne für jedes Paar Preis : Stunden.", "Zweimal kommt 7 heraus, einmal 6. Die Zuordnung ist nicht proportional (für 5 Stunden gibt es Rabatt)."),
    lambda: F(14, 2) == F(21, 3) == 7 and F(30, 5) == 6, {0: (None, "„steigt mit“ für proportional gehalten"), 1: (None, "Rechnung ohne Bezug zu den Preisen"), 2: (None, "richtiges Urteil, falscher Grund")})
neu(f, "vervielfachen", "A", 3, "verknuepfen", VERH, "ja",
    zahl("Ein Wasserhahn füllt gleichmäßig 12 Liter in 3 Minuten. Eine Wanne fasst 140 Liter; 20 Liter sind schon darin. Nach wie vielen Minuten ist sie voll?", 30, "(140 - 20) // (12 // 3)",
         "Wie viele Liter fehlen noch? Wie viele Liter kommen in einer Minute?", "Es fehlen 120 Liter. In 1 Minute kommen 4 Liter. 120 : 4 = 30 Minuten.", einheit="min"),
    ["120/4"], [(35, None, "die 20 Liter nicht abgezogen"), (10, None, "120 : 12 gerechnet, ohne auf 1 Minute zu schließen")])
neu(f, "vervielfachen", "V", 1, "direkt", WERT, "ja",
    bed("3 Kugeln Eis kosten 4,50 €. Jede Kugel kostet gleich viel. Nenne eine andere Anzahl von Kugeln und den passenden Preis in Euro.", [G, R],
        [("andere Anzahl, mindestens 1", UND(["!=", "$1", 3], [">=", "$1", 1]), "$1", "Deine Anzahl ist {}."),
         ("Preis passt zur Anzahl", ["=", ["*", "$2", 3], ["*", "$1", "4,5"]], ["/", "$2", "$1"], "Bei dir kostet eine Kugel {} €.")],
        [6, 9], [([3, "4,5"], "andere Anzahl, mindestens 1"), ([6, "7,5"], "Preis passt zur Anzahl"), ([0, 0], "andere Anzahl, mindestens 1")],
        "Was du mit der Anzahl tust, tust du auch mit dem Preis.", "Zum Beispiel doppelt so viele: 6 Kugeln für 9 €. Oder 1 Kugel für 1,50 €.", gut=[[1, "1,5"], [2, 3], [10, 15]]), None, None)
neu(f, "erkennen", "V", 2, "umkehr", WERT, "ja",
    bed("Erfinde eine Preisliste, die NICHT proportional ist: Preis für 1 Stück, für 2 Stück und für 4 Stück (in Euro). Die Preise sollen größer als 0 sein und von links nach rechts steigen.", [R, R, R],
        [("Preise größer als 0 und steigend", UND([">", "$1", 0], [">", "$2", "$1"], [">", "$3", "$2"]), None, "Deine Preise sind nicht alle größer als 0, oder sie steigen nicht."),
         ("nicht proportional", ODER(["!=", "$2", ["*", 2, "$1"]], ["!=", "$3", ["*", 4, "$1"]]), ["/", "$3", 4], "Deine Liste ist proportional: Jedes Stück kostet immer {} €.")],
        [2, "3,5", 6], [([2, 2, 4], "Preise größer als 0 und steigend"), ([2, 4, 8], "nicht proportional"), (["1,5", 3, 6], "nicht proportional")],
        "Was müsste bei einer proportionalen Liste zur doppelten Menge gehören?", "Proportional wäre zum Beispiel 2 €, 4 €, 8 €. Sobald ein Preis davon abweicht (etwa Mengenrabatt: 2 €, 3,50 €, 6 €), ist die Liste nicht proportional.", gut=[[2, 4, 7], [1, 3, 4]]), None, None)
neu(f, "pruefen", "V", 2, "umkehr", WERT, "ja",
    bed("In einer proportionalen Tabelle gehört zur Menge 4 der Wert 10. Nenne zwei weitere Paare aus Menge und Wert. Die beiden Mengen sollen größer als 0, verschieden und nicht 4 sein. Reihenfolge der Felder: erste Menge, ihr Wert, zweite Menge, ihr Wert.", [R, R, R, R],
        [("Mengen verschieden und nicht 4", UND(["!=", "$1", "$3"], ["!=", "$1", 4], ["!=", "$3", 4]), None, "Deine Mengen sollen verschieden und nicht 4 sein."), ("Mengen größer als 0", UND([">", "$1", 0], [">", "$3", 0]), None, "Beide Mengen sollen größer als 0 sein."),
         ("erstes Paar passt zur Tabelle", ["=", ["*", "$2", 4], ["*", "$1", 10]], ["/", "$2", "$1"], "Bei deinem ersten Paar ist Wert : Menge = {}."),
         ("zweites Paar passt zur Tabelle", ["=", ["*", "$4", 4], ["*", "$3", 10]], ["/", "$4", "$3"], "Bei deinem zweiten Paar ist Wert : Menge = {}.")],
        [2, 5, 6, 15], [([4, 10, 6, 15], "Mengen verschieden und nicht 4"), ([0, 0, 6, 15], "Mengen größer als 0"), ([2, 6, 6, 15], "erstes Paar passt zur Tabelle"), ([2, 5, 6, 16], "zweites Paar passt zur Tabelle")],
        "Rechne für das gegebene Paar Wert : Menge.", "10 : 4 = 2,5. Jedes Paar braucht denselben Wert, zum Beispiel 2 und 5 oder 6 und 15.", gut=[[1, "2,5", 8, 20]]), None, None)
neu(f, "pruefen", "V", 3, "parameter", WERT, "ja",
    bed("Die Paare (2 | a) und (5 | b) gehören zu einer proportionalen Zuordnung. a und b sind ganze Zahlen größer als 0, und b ist kleiner als 40. Nenne a und b.", [G, G],
        [("beide größer als 0", [">", ["min", "$alle"], 0], ["min", "$alle"], "Deine kleinere Zahl ist {}."), ("b kleiner als 40", ["<", "$2", 40], "$2", "Dein b ist {}."),
         ("die Paare sind proportional", ["=", ["*", 5, "$1"], ["*", 2, "$2"]], ["/", ["*", 5, "$1"], 2], "Zu deinem a würde bei 5 der Wert {} gehören.")],
        [4, 10], [([0, 0], "beide größer als 0"), ([16, 40], "b kleiner als 40"), ([4, 9], "die Paare sind proportional"), ([3, 7], "die Paare sind proportional")],
        "Bei beiden Paaren muss „Wert : Menge“ dasselbe ergeben.", "a : 2 muss gleich b : 5 sein. Zum Beispiel a = 4 und b = 10 (beide Male 2) oder a = 6 und b = 15 (beide Male 3).", gut=[[2, 5], [14, 35]]), None, None)
zus = ["/", ["*", ["+", "$1", "$2"], 40], 100]
neu(f, "vervielfachen", "V", 3, "verknuepfen", VERH, "ja",
    bed("12 Brötchen kosten 4,80 €. Zwei Kinder kaufen verschieden viele Brötchen und zahlen zusammen genau 3,20 €. Nenne die beiden Anzahlen. Jedes Kind kauft mindestens ein Brötchen.", [G, G],
        [("jedes Kind mindestens ein Brötchen", [">=", ["min", "$alle"], 1], ["min", "$alle"], "Deine kleinere Anzahl ist {}."), ("verschieden viele", ["verschieden", "$alle"], None, "Die beiden Kinder sollen verschieden viele Brötchen kaufen."),
         ("zusammen 3,20 €", ["=", zus, "3,2"], zus, "Zusammen kosten deine Brötchen {} €.")],
        [3, 5], [([0, 8], "jedes Kind mindestens ein Brötchen"), ([4, 4], "verschieden viele"), ([3, 6], "zusammen 3,20 €")],
        "Was kostet ein Brötchen?", "Ein Brötchen kostet 4,80 € : 12 = 0,40 €. Für 3,20 € gibt es 8 Brötchen, zum Beispiel 3 und 5.", gut=[[1, 7], [6, 2]]), None, None)

# ═════════════════════ Kind 2 · Flug f1 · Funktionsbegriff (Klasse 8) ═════════════════════
f = "f1"
KO = lambda x, y, **mehr: {"typ": "koordinaten", "x": x, "y": y, **mehr}
neu(f, "funktionswert", 4, 1, "direkt", REIH, "nein",
    luecken("f(x) = x² − 3x. Berechne f(−2) in Schritten: (−2)² = ①. −3 · (−2) = ②. Zusammen: f(−2) = ③.", K(3), [4, 6, 10], ["(-2) ** 2", "-3 * (-2)", "(-2) ** 2 - 3 * (-2)"],
            "Setze −2 in Klammern ein.", "(−2)² = 4. −3 · (−2) = 6. Zusammen 4 + 6 = 10.", "Je Lücke eine ganze Zahl (mit Minus, falls negativ)."),
    ["4", "6", "4+6"], {0: [(-4, None, "(−2)² als −4 gerechnet")], 1: [(-6, "fb.vorzeichen.falsches_zeichen", "Minus mal Minus als Minus")], 2: [(-2, "fb.vorzeichen.falsches_zeichen", "4 − 6 gerechnet"), (-10, None, "beide Vorzeichen falsch")]})
neu(f, "eindeutig", 12, 1, "erkennen", ZU, "ja",
    wahl("Jeder Person wird ihre Telefonnummer zugeordnet. Herr Kim hat zwei Nummern. Ist diese Zuordnung eine Funktion?",
         ["Ja, jede Nummer gehört zu genau einer Person.", "Nein, zu Herrn Kim gehören zwei verschiedene Ausgaben.", "Ja, es gibt mehr Nummern als Personen.", "Nein, weil man mit Telefonnummern nicht rechnet."], 1,
         "Was ist hier die Eingabe, was die Ausgabe?", "Eingabe ist die Person, Ausgabe die Nummer. Herr Kim hat zwei Ausgaben – also keine Funktion."),
    lambda: True, {0: ("fb.zuordnung.x_und_y_vertauscht", "Eingabe und Ausgabe vertauscht"), 2: (None, "Anzahl statt Eindeutigkeit geprüft"), 3: (None, "richtiges Urteil, falscher Grund")})
neu(f, "stelle", 13, 1, "erkennen", ZU, "ja",
    wahl("f(x) = 2x + 1. Gesucht ist das x mit f(x) = 9. Was tust du?", ["2x + 1 = 9 nach x auflösen", "9 für x einsetzen", "f(0) berechnen"], 0,
         "Die 9 ist das Ergebnis, nicht die Eingabe.", "Das Ergebnis ist gegeben. Du löst 2x + 1 = 9: x = 4."),
    lambda: 2 * 4 + 1 == 9, {1: ("fb.zuordnung.x_und_y_vertauscht", "das Ergebnis für x eingesetzt"), 2: (None, "kein Bezug zur 9")})
neu(f, "stelle", 4, 2, "mehrschritt", GEGEN, "nein",
    luecken("f(x) = 4x − 6. Für welches x ist f(x) = 14? Gleichung: 4x − 6 = ①. Plus 6: 4x = ②. Geteilt durch 4: x = ③.", K(3), [14, 20, 5], ["14", "14 + 6", "(14 + 6) // 4"],
            "Das Ergebnis 14 steht rechts vom Gleichheitszeichen.", "4x − 6 = 14. Plus 6: 4x = 20. Geteilt durch 4: x = 5."),
    ["4*5-6", "4*5", "20/4"], {2: [(50, "fb.zuordnung.x_und_y_vertauscht", "14 für x eingesetzt: f(14) = 50"), (2, "fb.gegenrechnung.gleiche_rechnung", "14 − 6 gerechnet")]})
neu(f, "wertetabelle", "B", 2, "darstellung", ZU, "ja",
    luecken("Die Wertetabelle gehört zu einer Funktion der Form f(x) = a · x + b. Bestimme a und b.", "a = □; b = □", [3, -4], ["(-1) - (-4)", "-4"],
            "b steht bei x = 0. a ist der Schritt von einer Spalte zur nächsten.", "Bei x = 0 steht −4, also b = −4. Von Spalte zu Spalte kommen 3 dazu, also a = 3. Probe: 3 · 3 − 4 = 5.", "Je Lücke eine ganze Zahl (mit Minus, falls negativ).",
            grafik=TAB(["x", "0", "1", "2", "3"], ["f(x)", "−4", "−1", "2", "5"])),
    ["5-2", "2-3*2"], {0: [(-4, None, "a und b vertauscht")], 1: [(4, "fb.plusminus.zeichen_des_ergebnisses", "das Minus verloren"), (3, None, "a und b vertauscht")]},
    probe=lambda: [3 * x - 4 for x in range(4)] == [-4, -1, 2, 5])
neu(f, "wertetabelle", 17, 2, "umkehr", ZU, "ja",
    zahl("f(x) = 10 − 3x. In der Wertetabelle steht unter einem x der Wert −5. Welches x ist das?", 5, "(10 - (-5)) // 3",
         "Der Wert −5 ist das Ergebnis. Löse 10 − 3x = −5.", "10 − 3x = −5. Minus 10: −3x = −15. Geteilt durch −3: x = 5."),
    ["15/3"], [(25, "fb.zuordnung.x_und_y_vertauscht", "−5 für x eingesetzt"), (-5, "fb.vorzeichen.falsches_zeichen", "Vorzeichen beim Teilen falsch")])
neu(f, "graph_lesen", 17, 2, "umkehr", ZU, "ja",
    zahl("Lies am Graphen ab: Für welches x gilt f(x) = 3?", 2, "(3 + 1) // 2",
         "Geh von der 3 auf der y-Achse waagrecht zum Graphen, dann senkrecht zur x-Achse.", "Auf der Höhe y = 3 trifft man den Graphen bei x = 2.",
         grafik=KO([-4, 4], [-5, 5], graphen=[{"art": "linear", "m": 2, "t": -1, "name": "f"}])),
    ["4/2"], [(5, "fb.zuordnung.x_und_y_vertauscht", "f(3) abgelesen statt die Stelle zu y = 3")], probe=lambda: 2 * 2 - 1 == 3)
neu(f, "graph_lesen", "B", 2, "darstellung", ZU, "ja",
    zahl("Wie viele x-Werte gehören am Graphen zum y-Wert 1?", 2, "1 + 1",
         "Zieh in Gedanken eine waagrechte Linie auf der Höhe y = 1.", "Die waagrechte Linie bei y = 1 trifft den Graphen zweimal: bei x = −2 und bei x = 2.",
         grafik=KO([-4, 4], [-4, 6], graphen=[{"art": "poly", "k": [-3, 0, 1], "name": "f"}])),
    ["2"], [(1, "fb.gegenrechnung.zweite_loesung_fehlt", "nur die Stelle rechts gesehen"), (-2, None, "f(1) abgelesen")], probe=lambda: {x for x in range(-4, 5) if x * x - 3 == 1} == {-2, 2})
neu(f, "nullstellen", 14, 2, "mehrschritt", ZU, "ja",
    luecken("Nullstelle von f(x) = 3x − 12 auf zwei Wegen. Weg A: 3x − 12 = 0 lösen. Weg B: Werte ausrechnen – f(3) = ①, f(4) = ②. Die Nullstelle ist x = ③.", K(3), [-3, 0, 4], ["3 * 3 - 12", "3 * 4 - 12", "12 // 3"],
            "An der Nullstelle ist der Funktionswert 0.", "f(3) = −3, f(4) = 0. Die Nullstelle ist x = 4. Weg A: 3x = 12, x = 4.", "Je Lücke eine ganze Zahl (mit Minus, falls negativ)."),
    ["9-12", "12-12", "(0+12)/3"], {2: [(-12, None, "f(0) statt der Nullstelle genannt"), (-4, "fb.plusminus.zeichen_des_ergebnisses", "Vorzeichen der Lösung falsch")]})
neu(f, "mengen", 17, 2, "umkehr", ZU, "ja",
    luecken("f(x) = 2x + 1 hat die Wertemenge W = {3; 7; 11}. Aus welchen drei Zahlen besteht die Definitionsmenge? Kleinste zuerst.", "D = {□; □; □}", [1, 3, 5], ["(3 - 1) // 2", "(7 - 1) // 2", "(11 - 1) // 2"],
            "Zu jedem Wert aus W suchst du das x. Löse 2x + 1 = 3 und so weiter.", "2x + 1 = 3 gibt x = 1. 2x + 1 = 7 gibt x = 3. 2x + 1 = 11 gibt x = 5.", "Kleinste Zahl zuerst."),
    ["2/2", "6/2", "10/2"], {0: [(7, "fb.zuordnung.x_und_y_vertauscht", "die 3 eingesetzt statt zurückgerechnet")], 2: [(23, "fb.zuordnung.x_und_y_vertauscht", "die 11 eingesetzt statt zurückgerechnet")]},
    probe=lambda: [2 * x + 1 for x in (1, 3, 5)] == [3, 7, 11])
neu(f, "sachzusammenhang", "B", 2, "einkleidung", ZU, "ja",
    wahl("Ein Schwimmbad kostet 3 € Eintritt und dazu 2 € je Stunde. Welcher Term gibt den Preis für x Stunden an?", ["3x + 2", "5x", "2 · (x + 3)", "2x + 3"], 3,
         "Erst die feste Größe, dann die Änderung je Stunde.", "Fest sind 3 €. Je Stunde kommen 2 € dazu: 2x + 3. Probe für 4 Stunden: 2 · 4 + 3 = 11 €."),
    lambda: 2 * 4 + 3 == 3 + 2 + 2 + 2 + 2, {0: (None, "fest und je Stunde vertauscht"), 1: (None, "beide Zahlen zusammengezählt"), 2: (None, "den Eintritt mitvervielfacht")})
neu(f, "punkt_graph", 12, 3, "fehler", REIH, "ja",
    wahl("Liegt P(−2 | 7) auf dem Graphen von f(x) = x² + 3? Mia rechnet: −2² + 3 = −4 + 3 = −1 und sagt Nein. Was stimmt?",
         ["Mia hat recht: P liegt nicht auf dem Graphen.", "P liegt nicht auf dem Graphen, denn (−2)² + 3 = 1.", "Das lässt sich ohne Zeichnung nicht entscheiden.", "P liegt auf dem Graphen, denn (−2)² + 3 = 7."], 3,
         "Wie setzt man eine negative Zahl ein?", "Negative Zahlen werden in Klammern eingesetzt: (−2)² = 4. Also f(−2) = 4 + 3 = 7. P liegt auf dem Graphen."),
    lambda: (-2) ** 2 + 3 == 7, {0: (None, "wie Mia die Klammer um −2 weggelassen"), 1: (None, "(−2)² falsch ausgerechnet"), 2: (None, "Einsetzen genügt; eine Zeichnung ist nicht nötig")})
neu(f, "punkt_graph", 17, 3, "parameter", GEGEN, "ja",
    zahl("Für welches t liegt der Punkt P(2 | 9) auf dem Graphen von f(x) = 3x + t?", 3, "9 - 3 * 2",
         "Setze x = 2 ein. Das Ergebnis soll 9 sein.", "3 · 2 + t = 9, also 6 + t = 9 und t = 3."),
    ["9-6"], [(15, "fb.gegenrechnung.gleiche_rechnung", "9 + 6 gerechnet"), (-3, "fb.plusminus.zeichen_des_ergebnisses", "6 − 9 gerechnet"), (-25, "fb.zuordnung.x_und_y_vertauscht", "9 für x eingesetzt und 2 als Ergebnis genommen")])
neu(f, "sachzusammenhang", 17, 3, "verknuepfen", ZU, "ja",
    zahl("Eine Kerze ist am Anfang 18 cm hoch und brennt gleichmäßig ab. Nach 4 Stunden ist sie noch 12 cm hoch. Nach wie vielen Stunden (vom Anfang an) ist sie ganz abgebrannt?", 12, "18 * 4 // (18 - 12)",
         "Wie viele Zentimeter brennen in einer Stunde ab? Wann ist die Höhe 0?", "In 4 Stunden 6 cm, also 1,5 cm je Stunde. Höhe: 18 − 1,5x. Null bei 18 : 1,5 = 12 Stunden.", einheit="h"),
    ["18/(6/4)"], [(8, None, "nur die Zeit ab der 12-cm-Marke gerechnet"), (3, None, "18 : 6 gerechnet, ohne die 4 Stunden")])
neu(f, "eindeutig", 12, 3, "begruenden", ZU, "ja",
    wahl("Im Koordinatensystem ist ein Kreis gezeichnet. Ist das der Graph einer Funktion?",
         ["Nein, zu x = 0 gehören zwei y-Werte: 3 und −3.", "Ja, zu jedem y gehört ein x.", "Ja, die Linie ist geschlossen.", "Nein, weil ein Kreis keine Gleichung hat."], 0,
         "Geh von einem x aus senkrecht nach oben und unten. Wie oft triffst du die Linie?", "Über x = 0 liegen zwei Punkte der Linie: (0 | 3) und (0 | −3). Eine Eingabe mit zwei Ausgaben – keine Funktion.",
         grafik=KO([-4, 4], [-4, 4], kreise=[{"m": [0, 0], "r": 3, "name": "k"}])),
    lambda: 0 ** 2 + 3 ** 2 == 0 ** 2 + (-3) ** 2 == 3 ** 2, {1: ("fb.zuordnung.x_und_y_vertauscht", "von y aus statt von x aus geprüft"), 2: (None, "Form der Linie statt Eindeutigkeit"), 3: (None, "richtiges Urteil, falscher Grund")})
fx = lambda feld: ["-", ["*", 2, feld], 7]
neu(f, "funktionswert", "V", 1, "direkt", ZU, "ja",
    bed("f(x) = 2x − 7. Nenne zuerst ein x, für das f(x) negativ ist, und dann ein x, für das f(x) größer als 10 ist.", [R, R],
        [("erstes x: f(x) ist negativ", ["<", fx("$1"), 0], fx("$1"), "Für dein erstes x ist f(x) = {}."), ("zweites x: f(x) ist größer als 10", [">", fx("$2"), 10], fx("$2"), "Für dein zweites x ist f(x) = {}.")],
        [0, 10], [([4, 10], "erstes x: f(x) ist negativ"), ([0, 8], "zweites x: f(x) ist größer als 10"), (["3,5", 10], "erstes x: f(x) ist negativ")],
        "Setze dein x ein und rechne aus.", "f(0) = −7 ist negativ. f(10) = 13 ist größer als 10.", gut=[[-5, 9], [3, "8,6"]]), None, None)
par = lambda feld: ["-", ["hoch", feld, 2], 4]
neu(f, "punkt_graph", "V", 2, "umkehr", ZU, "ja",
    bed("Nenne zwei verschiedene Punkte auf dem Graphen von f(x) = x² − 4. Mindestens einer soll unterhalb der x-Achse liegen. Reihenfolge der Felder: x und y des ersten Punkts, x und y des zweiten Punkts.", [R, R, R, R],
        [("erster Punkt liegt auf dem Graphen", ["=", "$2", par("$1")], par("$1"), "Für dein erstes x ist f(x) = {}."), ("zweiter Punkt liegt auf dem Graphen", ["=", "$4", par("$3")], par("$3"), "Für dein zweites x ist f(x) = {}."),
         ("verschiedene Punkte", ["!=", "$1", "$3"], None, "Du hast zweimal denselben Punkt genannt."), ("einer unterhalb der x-Achse", ODER(["<", "$2", 0], ["<", "$4", 0]), None, "Keiner deiner Punkte liegt unterhalb der x-Achse.")],
        [0, -4, 3, 5], [([0, 4, 3, 5], "erster Punkt liegt auf dem Graphen"), ([0, -4, 3, 6], "zweiter Punkt liegt auf dem Graphen"), ([3, 5, 3, 5], "verschiedene Punkte"), ([3, 5, -3, 5], "einer unterhalb der x-Achse")],
        "Wähle ein x und rechne y = x² − 4 aus.", "Zum Beispiel (0 | −4) und (3 | 5): 0² − 4 = −4 und 3² − 4 = 5. Unterhalb der x-Achse liegt ein Punkt, wenn y negativ ist.", gut=[[1, -3, -1, -3], ["0,5", "-3,75", 2, 0]]), None, None)
neu(f, "eindeutig", "V", 2, "umkehr", ZU, "ja",
    bed("Eine Tabelle enthält die Paare (1 | 4) und (2 | 5). Nenne ein drittes Paar (x | y), mit dem die Tabelle KEINE Funktion mehr beschreibt.", [G, G],
        [("mit dem Paar ist es keine Funktion", ODER(UND(["=", "$1", 1], ["!=", "$2", 4]), UND(["=", "$1", 2], ["!=", "$2", 5])), None, "Mit deinem Paar hat immer noch jede Eingabe genau eine Ausgabe.")],
        [1, 7], [([3, 4], "mit dem Paar ist es keine Funktion"), ([1, 4], "mit dem Paar ist es keine Funktion"), ([4, 1], "mit dem Paar ist es keine Funktion")],
        "Wann ist eine Zuordnung keine Funktion?", "Eine Eingabe braucht zwei verschiedene Ausgaben: zum Beispiel (1 | 7) neben (1 | 4).", gut=[[2, 0], [1, -4]]), None, None)
neu(f, "nullstellen", "V", 3, "parameter", ZU, "ja",
    bed("Setze m und t so ein, dass f(x) = m · x + t die Nullstelle x = 3 hat und f(0) positiv ist.", [R, R],
        [("f(0) ist positiv", [">", "$2", 0], "$2", "Bei dir ist f(0) = {}."), ("Nullstelle bei x = 3", ["=", ["+", ["*", 3, "$1"], "$2"], 0], ["+", ["*", 3, "$1"], "$2"], "Bei dir ist f(3) = {}.")],
        [-2, 6], [([2, -6], "f(0) ist positiv"), ([-2, 5], "Nullstelle bei x = 3"), ([2, 6], "Nullstelle bei x = 3")],
        "Was bedeutet Nullstelle? Setze x = 3 ein.", "f(3) = 3m + t muss 0 sein, und t = f(0) muss positiv sein. Zum Beispiel m = −2 und t = 6.", gut=[[-1, 3], ["-0,5", "1,5"]]), None, None)
neu(f, "mengen", "V", 3, "verknuepfen", ERL, "ja",
    bed("f(x) = 12/(x − a). Wähle eine negative Zahl a und ein x so, dass f(x) = 4 ist. Reihenfolge der Felder: a, x.", [R, R],
        [("a ist negativ", ["<", "$1", 0], "$1", "Dein a ist {}."), ("Term ist für dein x definiert", ["!=", "$2", "$1"], None, "Für dein x ist der Nenner null. Der Term ist dort nicht definiert."),
         ("f(x) = 4", ["=", 12, ["*", 4, ["-", "$2", "$1"]]], ["/", 12, ["-", "$2", "$1"]], "Bei dir ist f(x) = {}.")],
        [-1, 2], [([1, 4], "a ist negativ"), ([-1, -1], "Term ist für dein x definiert"), ([-1, 3], "f(x) = 4"), ([-3, 3], "f(x) = 4")],
        "Welchen Wert muss der Nenner haben, damit 12 durch ihn 4 ergibt?", "Der Nenner x − a muss 3 sein. Mit a = −1 ist x = 2: 12/(2 + 1) = 4.", gut=[[-3, 0], ["-0,5", "2,5"]]), None, None)

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
    assert 12 <= len(normal) <= 15 and 4 <= len(viele) <= 6, (flug, len(normal), len(viele))
    titel, kind, klasse = FLUG[flug][:3]
    karten = sorted({e["lernkarte"] for e in liste})
    json.dump({"stand": "2026-11-27", "flug": flug, "titel": titel, "fuer": kind, "klasse": klasse, "thema": FLUG[flug][3],
               "hinweis": "Aufgaben auf Vorrat, rollendes System Stufe 2. Nicht eingespielt. Je Eintrag: Zusatzangaben (Regel-Kennung, Fehlbilder, Typ, Zählvorschlag) und unter „aufgabe“ die Aufgabe im Format von inhalte/README.md. "
                          "Reihenfolge: erst die Aufgaben ohne Bau, dann die des Typs „bedingung“, jeweils mit aufsteigender Stufe.",
               "aufgaben": normal + viele}, open(os.path.join(HIER, f"{flug}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    typen = {}
    for e in normal:
        typen[e["typ"].split(" (")[0]] = typen.get(e["typ"].split(" (")[0], 0) + 1
    print(f"{flug:9} {kind}: {len(normal)} ohne Bau, {len(viele)} bedingung; Stufen {[sum(1 for e in liste if e['stufe'] == s) for s in (1, 2, 3)]}; Lernkarten {len(karten)}; mit Zeichnung {sum(1 for e in liste if 'grafik' in e['aufgabe']['f'])}; {typen}")
print(f"{len(A)} Aufgaben; {n_rechnung} Rechnungen zweifach nachgerechnet; {n_fb} Fehlbilder, davon {sum(1 for fl in aus.values() for e in fl for x in e['fehlbilder'] if x['fehlbild'])} mit Kennung; "
      f"{n_grafik} Aufgaben mit Zeichnung; {n_bruch} Texte mit Bruchstrich, keiner zweideutig")
print("OK")
