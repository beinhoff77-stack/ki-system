"""Mathe-Profi, Auftrag 7: Schritt 1 – neue Aufgaben ohne Bau (nur `zahl`, `auswahl`, `luecken`).

Aufruf: python3 -I inhalte/mathe-profi/schritt1/bauen.py
- rechnet jede Aufgabe auf zwei Wegen nach (Feld `c` mit dem Rechner aus tools/inhalt_pruefen.py; zweiter Weg hier),
- rechnet jedes Fehlbild aus und prüft, dass es eine andere Zahl ergibt als die Lösung,
- schreibt je Thema `<schluessel>.neu.json` (Aufgaben im Format von inhalte/README.md, ohne Zusatzfelder)
  und `etiketten.json` (Grundregel, Fehlbilder, Aufgabentyp der Auswahl, Zählvorschlag – dafür gibt es im Format kein Feld),
- hängt die Aufgaben an eine Kopie der Themen-Datei und lässt tools/inhalt_pruefen.py darüber laufen (vorher/nachher).
Nur Inhalte. Keine Lerndaten. Nichts wird eingespielt.
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
spec = importlib.util.spec_from_file_location("inhalt_pruefen", os.path.join(WURZEL, "tools", "inhalt_pruefen.py"))
ip = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ip)

REGEL = {1: "Richtung", 2: "Zeichen-Paar", 3: "Rangfolge", 4: "Verteilen", 5: "Minusklammer", 6: "Tauschen und Bündeln", 7: "Waage", 8: "Umkehren",
         9: "Einsetzen und Probe", 10: "Wert bleibt", 11: "Bruchrechnen", 12: "Potenz", 13: "Stellenwert", 14: "Verhältnis", 15: "Nullprodukt"}
TYP = {4: "Lückenweg", 12: "Fehler-Detektiv (einfache Form)", 13: "Verfahren wählen (einfache Form)", 14: "Zwei Wege vergleichen", 17: "Formel umkehren", "B": "Brücke: Zahl, aber nicht ausrechnen"}
ZAEHLT = {"nein": "zählt nicht für „gelandet“ (volle Hilfe)", "folge": "zählt nur für „in Folge“, nicht als eigene Lösung (halbe Hilfe)", "ja": "zählt wie jede Übung dieser Stufe"}
A = []          # alle Aufgaben mit Zusatzangaben


def z2(ausdruck):
    """zweiter Rechenweg: eigener Ausdruck, exakt mit Brüchen"""
    genau = re.sub(r"(?<![\w.])(\d+)(?![\w.])", r"F(\1)", ausdruck)       # jede ganze Zahl als Bruch, damit „/“ exakt bleibt
    return F(eval(genau, {"__builtins__": {}}, {"F": F, "abs": abs}))


def neu(thema, kenn, typ, l, t, s, g, regel, zaehlt, aufgabe, zweit, fehlbilder, probe=None):
    aufgabe = {"l": l, "t": t, "p": "uebung", "s": s, "g": g, **aufgabe}
    A.append(dict(thema=thema, kenn=kenn, typ=typ, regel=regel, zaehlt=zaehlt, aufgabe=aufgabe, zweit=zweit, fb=fehlbilder, probe=probe))


def luecken(text, schablone, werte, c, h, w, hinweis="Je Lücke eine ganze Zahl (mit Minus, falls negativ)."):
    return {"y": "luecken", "f": {"text": text, "schablone": schablone, "hinweis": hinweis}, "o": {"werte": werte}, "c": c, "h": h, "w": w}


def zahl(text, wert, c, h, w, einheit=None):
    return {"y": "zahl", "f": {"text": text}, "o": {"wert": wert, **({"einheit": einheit} if einheit else {})}, "c": c, "h": h, "w": w}


def wahl(text, antworten, index, h, w):
    return {"y": "auswahl", "f": {"text": text}, "a": antworten, "o": {"index": index}, "h": h, "w": w}


K = lambda n: "; ".join(f"{'①②③④⑤'[i]} = □" for i in range(n))
ZW = "Zwillingszeilen – nicht ausrechnen, nur umschreiben. "

# ═════════ Klasse 5 · zahlen.rechengesetze ═════════
T = "zahlen.rechengesetze"
neu(T, "RG-01", 4, "mal_ganz", "ganz", 1, "direkt", 3, "nein",
    luecken("Fülle den Rechenweg aus: 25 − 4 · (3 − 8) = 25 − 4 · (①) = 25 − (②) = 25 + ③ = ④", K(4), [-5, -20, 20, 45],
            ["3 - 8", "4 * (3 - 8)", "0 - 4 * (3 - 8)", "25 - 4 * (3 - 8)"], "Jede Zeile ändert nur eine Stelle. Vergleiche sie mit der Zeile davor.",
            "3 − 8 = −5. Dann 4 · (−5) = −20. Minus (−20) heißt plus 20: 25 + 20 = 45."),
    ["-(8-3)", "-(4*5)", "4*5", "25+20"],
    {0: [("8-3", "3 − 8 geht über die Null nach links", 1)], 1: [("4*5", "plus mal minus ist minus", 2)], 2: [("-20", "minus eine negative Zahl heißt plus", 1)],
     3: [("25-20", "das Minus von −20 ist verloren gegangen", 2), ("(25-4)*(3-8)", "25 − 4 zuerst gerechnet", 3)]})
neu(T, "RG-02", 4, "mal_ganz", "ganz", 2, "mehrschritt", 2, "folge",
    luecken("Der erste Schritt ist gemacht. Rechne zu Ende: 30 − 6 · (2 − 7) = 30 − 6 · (−5) = 30 + ① = ②", K(2), [30, 60],
            ["0 - 6 * (2 - 7)", "30 - 6 * (2 - 7)"], "Welches Zeichen hat 6 · (−5)? Und was macht das Minus davor daraus?", "6 · (−5) = −30. Minus (−30) heißt plus 30: 30 + 30 = 60."),
    ["6*5", "30+30"], {0: [("-30", "6 · (−5) ist −30, das Minus davor dreht es um", 2)], 1: [("30-30", "minus mal minus nicht beachtet", 2), ("(30-6)*(2-7)", "30 − 6 zuerst gerechnet", 3)]})
neu(T, "RG-03", 4, "geteilt_ganz", "ganz", 2, "mehrschritt", 2, "folge",
    luecken("Rechne in zwei Zeilen: (−8) · 5 − 36 : (−4) = ① − (②) = ③", K(3), [-40, -9, -31],
            ["(-8) * 5", "36 / (-4)", "(-8) * 5 - 36 / (-4)"], "Rechne erst die beiden Punktrechnungen, jede mit ihrem Zeichen.", "(−8) · 5 = −40 und 36 : (−4) = −9. Dann −40 − (−9) = −40 + 9 = −31."),
    ["-(8*5)", "-(36/4)", "-40+9"], {0: [("8*5", "minus mal plus ist minus", 2)], 1: [("36/4", "plus durch minus ist minus", 2)], 2: [("-40-9", "minus (−9) heißt plus 9", 1)]})
neu(T, "RG-04", "B", "klammern", "vorrang", 2, "darstellung", 5, "ja",
    luecken(ZW + "Zeile 1: 20 − (8 − 3) = 20 − 8 + ①. Zeile 2: 5 000 − (1 734 − 266) = 5 000 − 1 734 + ②.", K(2), [3, 266],
            ["20 - (8 - 3) - (20 - 8)", "5000 - (1734 - 266) - (5000 - 1734)"], "Zeile 1 kannst du nachrechnen. Zeile 2 ist genauso gebaut.",
            "Minus vor der Klammer dreht das Zeichen in der Klammer: aus − 3 wird + 3, aus − 266 wird + 266. Probe Zeile 1: 20 − 5 = 15 und 20 − 8 + 3 = 15."),
    ["3", "266"], {0: [("-3", "das Minus in der Klammer dreht sich um", 5)], 1: [("-266", "das Minus in der Klammer dreht sich um", 5)]})
neu(T, "RG-05", "B", "verteilen", "gesetze", 2, "darstellung", 4, "ja",
    luecken(ZW + "Zeile 1: 7 · 96 = 7 · 100 − 7 · ①. Zeile 2: 7 · 9 996 = 7 · ② − 7 · 4.", K(2), [4, 10000],
            ["100 - 96", "9996 + 4"], "Wie viel fehlt 96 bis zur nächsten glatten Zahl?", "96 = 100 − 4, also 7 · 96 = 7 · 100 − 7 · 4. Genauso 9 996 = 10 000 − 4."),
    ["(7*100-7*96)//7", "(7*9996+7*4)//7"], {0: [("96", "die Klammer heißt (100 − 4), nicht (100 − 96)", 4)], 1: [("9996", "die glatte Zahl gehört in die Lücke", 4), ("1000", "eine Stelle zu wenig", 13)]})
neu(T, "RG-06", 14, "verteilen", "gesetze", 2, "mehrschritt", 4, "ja",
    zahl("Zwei Wege für 7 · 38. Weg A: 7 · 30 + 7 · 8 = 210 + 56. Weg B: 7 · 40 − 7 · 2 = 280 − ?. Welche Zahl wird in Weg B abgezogen?", 14, "7 * 40 - 7 * 38",
         "Was hat Weg B aus der 38 gemacht – und was muss deshalb wieder weg?", "Weg B rechnet 7 · (40 − 2). Abgezogen wird 7 · 2 = 14. Probe: 280 − 14 = 266 und 210 + 56 = 266."),
    ["7*2"], [("56", "Zahl aus Weg A übernommen – Weg B zerlegt die 38 anders", 4), ("2", "der Faktor 7 trifft auch die 2", 4)])
neu(T, "RG-07", 14, "klammern", "vorrang", 2, "mehrschritt", 5, "ja",
    zahl("Zwei Wege für 70 − (25 − 9). Weg A rechnet erst die Klammer: 70 − 16. Weg B löst die Klammer auf: 70 − 25 und dann noch eine Zahl. Welche Zahl kommt in Weg B dazu? (Wird sie abgezogen, tippe sie mit Minus.)",
         9, "(70 - (25 - 9)) - (70 - 25)", "Rechne beide Wege bis zum Ende. Sie müssen dasselbe ergeben.", "Weg A: 70 − 16 = 54. Weg B: 70 − 25 = 45, bis 54 fehlen + 9. Das Minus vor der Klammer dreht − 9 zu + 9."),
    ["54-45"], [("-9", "das Minus in der Klammer dreht sich um", 5), ("16", "Zwischenergebnis aus Weg A übernommen", 5)])
neu(T, "RG-08", 12, "klammern", "vorrang", 3, "fehler", 3, "ja",
    wahl("Jemand rechnet in vier Zeilen: (1) 40 − 5 · (6 − 2) (2) = 35 · (6 − 2) (3) = 35 · 4 (4) = 140. In welcher Zeile passiert der erste Fehler?",
         ["Zeile 3: 6 − 2 ist nicht 4.", "Zeile 2: 40 − 5 wurde zuerst gerechnet. Erst kommt die Klammer, dann Punkt vor Strich.", "Zeile 4: 35 · 4 ist nicht 140.", "Nirgends. 140 stimmt."], 1,
         "Rechne die Aufgabe selbst und vergleiche Zeile für Zeile.", "Richtig: 6 − 2 = 4, dann 5 · 4 = 20, dann 40 − 20 = 20. In Zeile 2 wurde 40 − 5 vorgezogen."),
    None, {0: ("sucht einen Rechenfehler, wo ein Regelfehler ist", 3), 2: ("sucht einen Rechenfehler, wo ein Regelfehler ist", 3), 3: ("von links nach rechts gerechnet", 3)},
    probe=lambda: 40 - 5 * (6 - 2) == 20 and (40 - 5) * (6 - 2) == 140 and 6 - 2 == 4 and 35 * 4 == 140)
neu(T, "RG-09", 12, "mal_ganz", "ganz", 3, "fehler", 2, "ja",
    zahl("Jemand rechnet 24 − 4 · (5 − 8) = 24 − 4 · (−3) = 24 − 12 = 12. In der Rechnung steckt ein Fehler. Was kommt richtig heraus?", 36, "24 - 4 * (5 - 8)",
         "Welches Zeichen hat 4 · (−3)?", "4 · (−3) = −12. Also 24 − (−12) = 24 + 12 = 36. Im Beispiel wurde aus −12 eine 12."),
    ["24+12"], [("24-12", "Fehler übernommen: 4 · (−3) ist −12", 2), ("(24-4)*(5-8)", "24 − 4 zuerst gerechnet", 3)])
neu(T, "RG-10", 13, "kopfrechnen", "gesetze", 1, "erkennen", 6, "ja",
    wahl("Du sollst 25 · 37 · 4 im Kopf rechnen. Welcher Weg ist am geschicktesten?",
         ["Verteilen: 25 · 30 + 25 · 7, dann mal 4", "Tauschen: erst 25 · 4, dann mal 37", "Von links nach rechts: erst 25 · 37", "Runden: 25 · 40 · 4 rechnen"], 1,
         "Welche zwei Zahlen ergeben zusammen eine glatte Zahl?", "25 · 4 = 100, dann 100 · 37 = 3 700. Die anderen Wege sind länger; Runden ändert sogar das Ergebnis."),
    None, {0: ("richtig, aber umständlich: die glatte Zahl nicht gesehen", 6), 2: ("richtig, aber umständlich: die glatte Zahl nicht gesehen", 6), 3: ("Runden ändert das Ergebnis", 13)},
    probe=lambda: 25 * 4 * 37 == 25 * 37 * 4 == (25 * 30 + 25 * 7) * 4 == 3700 != 25 * 40 * 4)
neu(T, "RG-11", 13, "verteilen", "gesetze", 1, "erkennen", 4, "ja",
    wahl("Bei welcher Rechnung hilft Verteilen am meisten?", ["4 · 13 · 25", "125 + 67 + 75", "6 · 198", "480 : 6"], 2,
         "Verteilen braucht eine Zahl, die knapp neben einer glatten Zahl liegt.", "6 · 198 = 6 · 200 − 6 · 2 = 1 200 − 12 = 1 188. Bei den ersten beiden hilft Tauschen, die letzte geht direkt."),
    None, {0: ("hier hilft Tauschen, nicht Verteilen", 6), 1: ("hier hilft Tauschen, nicht Verteilen", 6), 3: ("hier braucht es kein Gesetz", 4)},
    probe=lambda: 6 * 198 == 6 * 200 - 6 * 2 == 1188 and 4 * 25 == 100 and 125 + 75 == 200 and 480 // 6 == 80)
neu(T, "RG-12", "B", "vorteil", "gesetze", 2, "darstellung", 6, "ja",
    luecken("Zwillingszeilen – nicht ausrechnen, nur umstellen. Zeile 1: 37 + 86 + 63 = 86 + (37 + ①). Zeile 2: 3 700 + 8 615 + 6 300 = 8 615 + ②.", K(2), [63, 10000],
            ["37 + 86 + 63 - 86 - 37", "3700 + 6300"], "Welche zwei Zahlen passen zusammen zu einer glatten Zahl?", "37 + 63 = 100, deshalb stellt man sie zusammen. Genauso 3 700 + 6 300 = 10 000."),
    ["63", "3700+8615+6300-8615"], {0: [("86", "86 steht schon vorn", 6)], 1: [("9000", "eine Stelle verrutscht", 13), ("6300", "nur eine der beiden Zahlen eingetragen", 6)]})
neu(T, "RG-13", 4, "klammern", "vorrang", 1, "direkt", 5, "nein",
    luecken("Fülle den Rechenweg aus: 64 − (30 − 6) = 64 − 30 + ① = ② + ① = ③", K(3), [6, 34, 40],
            ["6", "64 - 30", "64 - (30 - 6)"], "Was macht das Minus vor der Klammer mit dem Minus in der Klammer?", "Aus − 6 wird + 6: 64 − 30 + 6 = 34 + 6 = 40. Probe: 64 − 24 = 40."),
    ["30-24", "34", "64-24"], {0: [("-6", "das Minus in der Klammer dreht sich um", 5)], 2: [("64-30-6", "− 6 statt + 6 gerechnet", 5)]})

# ═════════ Klasse 5 · zahlen.ganz ═════════
T = "zahlen.ganz"
neu(T, "GZ-01", 4, "subtrahieren", "subtrahieren", 1, "direkt", 1, "nein",
    luecken("Fülle den Rechenweg aus: (−7) − (−12) = (−7) + ① = ②", K(2), [12, 5], ["0 - (-12)", "(-7) - (-12)"],
            "Eine negative Zahl abziehen heißt: ihre Gegenzahl dazuzählen.", "Minus (−12) heißt plus 12. (−7) + 12 = 5."),
    ["12", "12-7"], {0: [("-12", "Abziehen einer negativen Zahl heißt Gegenzahl dazuzählen", 1)], 1: [("-7-12", "(−12) abgezogen wie 12", 1), ("-5", "von −7 aus zwölf nach rechts geht über die Null", 1)]})
neu(T, "GZ-02", 4, "ketten", "verbinden", 1, "direkt", 1, "nein",
    luecken("Fülle den Rechenweg aus: 15 − 23 − (−6) + (−9) = 15 − 23 + ① − ② = ③ − ④ = ⑤", K(5), [6, 9, 21, 32, -11],
            ["0 - (-6)", "0 - (-9)", "15 + 6", "23 + 9", "15 - 23 - (-6) + (-9)"], "Erst die Klammern auflösen, dann alle Plus-Zahlen und alle Minus-Zahlen sammeln.",
            "Minus (−6) wird + 6, plus (−9) wird − 9. Plus-Zahlen: 15 + 6 = 21. Minus-Zahlen: 23 + 9 = 32. 21 − 32 = −11."),
    ["6", "9", "21", "32", "21-32"], {0: [("-6", "minus eine negative Zahl heißt plus", 1)], 2: [("15", "die 6 gehört zu den Plus-Zahlen", 1)], 4: [("32-21", "kleinere minus größere Zahl ist negativ", 1), ("15-23-6-9", "− (−6) als − 6 gerechnet", 1)]})
neu(T, "GZ-03", 4, "ketten", "verbinden", 2, "mehrschritt", 1, "folge",
    luecken("Der erste Schritt ist gemacht. Rechne zu Ende: (−14) + 9 − (−8) − 20 = (−14) + 9 + 8 − 20 = ① − ② = ③", K(3), [17, 34, -17],
            ["9 + 8", "14 + 20", "(-14) + 9 - (-8) - 20"], "Sammle alle Plus-Zahlen in ① und alle Minus-Zahlen in ②.", "Plus-Zahlen: 9 + 8 = 17. Minus-Zahlen: 14 + 20 = 34. 17 − 34 = −17."),
    ["17", "34", "17-34"], {1: [("20", "auch die 14 ist eine Minus-Zahl", 1)], 2: [("34-17", "kleinere minus größere Zahl ist negativ", 1), ("17-20", "die 14 vergessen", 1)]})
neu(T, "GZ-04", 4, "ketten", "verbinden", 2, "mehrschritt", 1, "folge",
    luecken("Fasse erst die Plus-Zahlen und die Minus-Zahlen zusammen: 30 − 45 + (−12) − (−7) = ① − ② = ③", K(3), [37, 57, -20],
            ["30 + 7", "45 + 12", "30 - 45 + (-12) - (-7)"], "Löse zuerst die beiden Klammern auf: Was wird aus + (−12) und aus − (−7)?", "+ (−12) wird − 12, − (−7) wird + 7. Plus-Zahlen: 30 + 7 = 37. Minus-Zahlen: 45 + 12 = 57. 37 − 57 = −20."),
    ["37", "57", "37-57"], {0: [("30", "− (−7) gehört zu den Plus-Zahlen", 1), ("42", "+ (−12) ist keine Plus-Zahl", 1)], 1: [("45+12+7", "− (−7) ist keine Minus-Zahl", 1)], 2: [("57-37", "kleinere minus größere Zahl ist negativ", 1)]})
neu(T, "GZ-05", "B", "subtrahieren", "subtrahieren", 2, "darstellung", 1, "ja",
    luecken(ZW + "Zeile 1: 9 − (−5) = 9 + ①. Zeile 2: 2 480 − (−1 520) = 2 480 + ②.", K(2), [5, 1520], ["0 - (-5)", "0 - (-1520)"],
            "Zeile 1 kannst du auf der Zahlengeraden prüfen. Zeile 2 ist genauso gebaut.", "Eine negative Zahl abziehen heißt ihre Gegenzahl dazuzählen: 9 + 5 und 2 480 + 1 520."),
    ["9-(-5)-9", "2480-(-1520)-2480"], {0: [("-5", "Gegenzahl nicht gebildet", 1)], 1: [("-1520", "Gegenzahl nicht gebildet", 1)]})
neu(T, "GZ-06", "B", "addieren", "addieren", 2, "darstellung", 1, "ja",
    luecken(ZW + "Zeile 1: (−8) + 3 = 3 − ①. Zeile 2: (−4 750) + 1 200 = 1 200 − ②.", K(2), [8, 4750], ["3 - ((-8) + 3)", "1200 - ((-4750) + 1200)"],
            "Beim Addieren darfst du tauschen. Was wird dann aus + (−8)?", "Tauschen: 3 + (−8). Eine negative Zahl dazuzählen heißt ihren Betrag abziehen: 3 − 8 und 1 200 − 4 750."),
    ["8", "4750"], {0: [("-8", "das Minus steht schon vor der Lücke", 1)], 1: [("-4750", "das Minus steht schon vor der Lücke", 1)]})
neu(T, "GZ-07", 14, "ketten", "verbinden", 2, "umkehr", 6, "ja",
    zahl("Zwei Wege für 12 − 30 + 18 − 5. Weg A rechnet von links nach rechts. Weg B sammelt erst alle Plus-Zahlen, dann alle Minus-Zahlen und rechnet ? − 35. Welche Zahl steht in Weg B vorn?", 30, "12 + 18",
         "Welche Zahlen haben ein Plus vor sich? Die erste Zahl zählt dazu.", "Plus-Zahlen: 12 + 18 = 30. Minus-Zahlen: 30 + 5 = 35. Beide Wege ergeben −5."),
    ["(12-30+18-5)+35"], [("12", "nur die erste Zahl genommen", 6), ("18", "die erste Zahl hat kein Zeichen, zählt aber als Plus", 6), ("60", "die Minus-Zahl 30 mitgezählt", 1)])
neu(T, "GZ-08", 14, "subtrahieren", "subtrahieren", 2, "darstellung", 1, "ja",
    zahl("Zwei Wege für (−6) − 9. Weg A geht auf der Zahlengeraden von −6 aus neun Schritte nach links. Weg B schreibt eine Plus-Aufgabe: (−6) + (?). Welche Zahl gehört in die Klammer?", -9, "((-6) - 9) - (-6)",
         "Abziehen heißt: die Gegenzahl dazuzählen.", "9 abziehen ist dasselbe wie −9 dazuzählen: (−6) + (−9) = −15."),
    ["-9"], [("9", "Gegenzahl nicht gebildet", 1), ("-15", "Ergebnis statt Summand eingetragen", 1)])
neu(T, "GZ-09", 12, "ketten", "verbinden", 3, "fehler", 1, "ja",
    wahl("Jemand rechnet in vier Zeilen: (1) 8 − (−5) − 20 (2) = 8 − 5 − 20 (3) = 3 − 20 (4) = −17. In welcher Zeile passiert der erste Fehler?",
         ["Zeile 3: 8 − 5 ist nicht 3.", "Zeile 4: 3 − 20 ist nicht −17.", "Zeile 2: Aus − (−5) wird + 5, nicht − 5.", "Nirgends. −17 stimmt."], 2,
         "Prüfe jede Zeile gegen die Zeile davor.", "Richtig: 8 + 5 − 20 = 13 − 20 = −7. In Zeile 2 wurde aus − (−5) ein − 5."),
    None, {0: ("sucht einen Rechenfehler, wo ein Regelfehler ist", 1), 1: ("sucht einen Rechenfehler, wo ein Regelfehler ist", 1), 3: ("− (−5) als − 5 gelesen", 1)},
    probe=lambda: 8 - (-5) - 20 == -7 and 8 - 5 == 3 and 3 - 20 == -17)
neu(T, "GZ-10", 12, "subtrahieren", "subtrahieren", 3, "fehler", 1, "ja",
    zahl("Jemand rechnet (−15) − (−9) + 4 = (−15) − 9 + 4 = −20. In der Rechnung steckt ein Fehler. Was kommt richtig heraus?", -2, "(-15) - (-9) + 4",
         "Was wird aus − (−9)?", "− (−9) wird + 9: (−15) + 9 + 4 = (−15) + 13 = −2."),
    ["-15+13"], [("-15-9+4", "Fehler übernommen: − (−9) ist + 9", 1), ("-15+9-4", "auch das + 4 umgedreht", 1)])
neu(T, "GZ-11", 13, "ketten", "verbinden", 1, "erkennen", 6, "ja",
    wahl("Du sollst 47 − 82 + 53 − 18 geschickt rechnen. Welcher erste Schritt hilft am meisten?",
         ["Von links nach rechts: zuerst 47 − 82.", "Erst 82 − 47 rechnen und am Ende das Zeichen umdrehen.", "Plus-Zahlen zusammen (47 + 53) und Minus-Zahlen zusammen (82 + 18).", "Alle vier Zahlen addieren und ein Minus davorsetzen."], 2,
         "Welche Zahlen ergeben zusammen eine glatte Zahl?", "47 + 53 = 100 und 82 + 18 = 100. Also 100 − 100 = 0."),
    None, {0: ("richtig, aber umständlich: die glatten Zahlen nicht gesehen", 6), 1: ("das Zeichen gilt nicht für die ganze Kette", 1), 3: ("Plus-Zahlen werden nicht zu Minus-Zahlen", 1)},
    probe=lambda: 47 - 82 + 53 - 18 == (47 + 53) - (82 + 18) == 0 != -(47 + 82 + 53 + 18))
neu(T, "GZ-12", 13, "umkehraufgabe", "gleichungen", 1, "erkennen", 8, "ja",
    wahl("Mit welcher Rechnung findest du die Zahl in □ − (−7) = −4?", ["(−4) − (−7)", "(−4) + (−7)", "(−4) + 7", "7 − 4"], 1,
         "Welche Rechnung macht „minus (−7)“ rückgängig?", "Die Umkehrung von „(−7) abziehen“ ist „(−7) dazuzählen“: (−4) + (−7) = −11. Probe: (−11) − (−7) = −4."),
    None, {0: ("Abziehen nicht umgekehrt", 8), 2: ("umgekehrt, aber mit der Gegenzahl", 8), 3: ("Zeichen der −4 verloren", 1)},
    probe=lambda: ((-4) + (-7)) - (-7) == -4 and ((-4) - (-7)) - (-7) != -4 and ((-4) + 7) - (-7) != -4 and (7 - 4) - (-7) != -4)
neu(T, "GZ-13", "B", "verstehen", "begruenden", 3, "begruenden", 1, "ja",
    wahl("Ohne auszurechnen: Ist (−4 829) − (−4 830) positiv, negativ oder null?",
         ["Negativ, weil beide Zahlen negativ sind.", "Negativ, weil 4 829 kleiner ist als 4 830.", "Null, weil die Zahlen fast gleich sind.", "Positiv, weil die abgezogene Zahl weiter links liegt."], 3,
         "Probiere dieselbe Frage mit kleinen Zahlen: (−2) − (−3).", "Wer eine Zahl abzieht, die weiter links liegt, landet rechts von null. Mit kleinen Zahlen: (−2) − (−3) = (−2) + 3 = 1."),
    None, {0: ("Zeichen der Zahlen mit dem Zeichen des Ergebnisses verwechselt", 1), 1: ("mit den Beträgen gerechnet", 1), 2: ("geschätzt statt die Richtung bestimmt", 1)},
    probe=lambda: (-4829) - (-4830) == 1 and (-2) - (-3) == 1)

# ═════════ Klasse 8 · terme.potenzgesetze_ganzzahlig ═════════
T = "terme.potenzgesetze_ganzzahlig"
HZ = "Je Lücke eine ganze Zahl (mit Minus, falls negativ)."
neu(T, "PG-01", "B", "gleiche_basis_ganz", "gleiche_basis_ganz", 2, "darstellung", 12, "ja",
    luecken("Zwillingszeilen – nicht ausrechnen, nur die Hochzahl bestimmen. Zeile 1: 2³ · 2⁻⁵ = 2ᵏ. Zeile 2: a⁴ · a⁻⁹ = aⁿ.", "k = □; n = □", [-2, -5], ["3 + (-5)", "4 + (-9)"],
            "Schreibe 2³ · 2⁻⁵ als Bruch aus lauter Zweien und kürze.", "Gleiche Basis: Hochzahlen addieren. 3 + (−5) = −2 und 4 + (−9) = −5.", HZ),
    ["-(5-3)", "-(9-4)"], {0: [("3*(-5)", "Hochzahlen malgenommen statt addiert", 12), ("3-(-5)", "abgezogen statt addiert", 12)], 1: [("4*(-9)", "Hochzahlen malgenommen statt addiert", 12)]},
    probe=lambda: F(2) ** 3 * F(2) ** -5 == F(2) ** -2 and F(3) ** 4 * F(3) ** -9 == F(3) ** -5)
neu(T, "PG-02", "B", "exponent_und_potenz", "exponent_und_potenz", 2, "darstellung", 12, "ja",
    luecken("Zwillingszeilen – nicht ausrechnen, nur die Hochzahl bestimmen. Zeile 1: (5⁻²)³ = 5ᵏ. Zeile 2: (x⁴)⁻² = xⁿ.", "k = □; n = □", [-6, -8], ["(-2) * 3", "4 * (-2)"],
            "(5⁻²)³ heißt: 5⁻² dreimal mit sich malnehmen.", "Potenz einer Potenz: Hochzahlen malnehmen. (−2) · 3 = −6 und 4 · (−2) = −8.", HZ),
    ["-(2*3)", "-(4*2)"], {0: [("-2+3", "Hochzahlen addiert statt malgenommen", 12)], 1: [("4+(-2)", "Hochzahlen addiert statt malgenommen", 12), ("4*2", "Zeichen der Hochzahl verloren", 2)]},
    probe=lambda: (F(5) ** -2) ** 3 == F(5) ** -6 and (F(3) ** 4) ** -2 == F(3) ** -8)
neu(T, "PG-03", 4, "terme_vereinfachen", "terme_vereinfachen", 1, "direkt", 12, "nein",
    luecken("Fülle den Rechenweg aus: (2a⁻³)² · a⁴ = 2ᵏ · aᵐ · a⁴ = c · aⁿ", "k = □; m = □; c = □; n = □", [2, -6, 4, -2], ["2", "(-3) * 2", "2 ** 2", "(-3) * 2 + 4"],
            "Das Quadrat trifft jeden Faktor in der Klammer.", "(2a⁻³)² = 2² · a⁻⁶ = 4a⁻⁶. Dann a⁻⁶ · a⁴ = a⁻².", HZ),
    ["2", "-6", "4", "-6+4"], {1: [("-3+2", "Hochzahlen addiert statt malgenommen", 12)], 2: [("2", "die 2 wird auch quadriert", 12)], 3: [("-6-4", "bei mal werden die Hochzahlen addiert", 12), ("-3+2+4", "Folgefehler aus m", 12)]},
    probe=lambda: (2 * F(3) ** -3) ** 2 * F(3) ** 4 == 4 * F(3) ** -2)
neu(T, "PG-04", 4, "terme_vereinfachen", "terme_vereinfachen", 2, "mehrschritt", 12, "folge",
    luecken("Der erste Schritt ist gemacht. Rechne zu Ende: (3x²)⁻² · x⁵ = 3⁻² · x⁻⁴ · x⁵ = xⁿ : c", "n = □; c = □", [1, 9], ["(-4) + 5", "3 ** 2"],
            "Was bedeutet 3⁻² als Bruch?", "x⁻⁴ · x⁵ = x¹. 3⁻² = 1/9. Zusammen: x : 9.", HZ),
    ["5-4", "9"], {0: [("(-4)*5", "Hochzahlen malgenommen statt addiert", 12)], 1: [("3*2", "3² ist 3 · 3", 12), ("-9", "eine negative Hochzahl macht den Wert nicht negativ", 12)]},
    probe=lambda: (3 * F(2) ** 2) ** -2 * F(2) ** 5 == F(2) / 9)
neu(T, "PG-05", 4, "gleiche_basis_ganz", "gleiche_basis_ganz", 2, "mehrschritt", 12, "folge",
    luecken("Rechne in zwei Schritten: a⁻² · a⁵ : a⁻¹ = aᵏ : a⁻¹ = aⁿ", "k = □; n = □", [3, 4], ["(-2) + 5", "(-2) + 5 - (-1)"],
            "Mal: Hochzahlen addieren. Geteilt: Hochzahl abziehen – auch wenn sie negativ ist.", "−2 + 5 = 3. Dann 3 − (−1) = 4.", HZ),
    ["5-2", "3+1"], {0: [("(-2)*5", "Hochzahlen malgenommen statt addiert", 12)], 1: [("3-1", "minus (−1) heißt plus 1", 1), ("3*(-1)", "Hochzahlen malgenommen statt abgezogen", 12)]},
    probe=lambda: F(3) ** -2 * F(3) ** 5 / F(3) ** -1 == F(3) ** 4)
neu(T, "PG-06", 14, "gleiche_basis_ganz", "gleiche_basis_ganz", 2, "umkehr", 12, "ja",
    zahl("Zwei Wege für 6⁻² · 6⁵ : 6². Weg A rechnet mit den Hochzahlen: −2 + 5 − 2. Weg B schreibt einen Bruch: 6⁵ geteilt durch (6² · 6ᵏ). Welche Hochzahl k steht in Weg B?", 2, "0 - (-2)",
         "Was wird aus 6⁻², wenn es unter den Bruchstrich wandert?", "6⁻² = 1/6². Im Nenner steht deshalb 6² · 6². Beide Wege ergeben 6¹ = 6."),
    ["2"], [("-2", "unter dem Bruchstrich wird aus 6⁻² die Potenz 6²", 12), ("1", "Ergebnis-Hochzahl statt k eingetragen", 12)],
    probe=lambda: F(6) ** -2 * F(6) ** 5 / F(6) ** 2 == F(6) ** 5 / (F(6) ** 2 * F(6) ** 2) == 6)
neu(T, "PG-07", 14, "exponent_und_potenz", "exponent_und_potenz", 2, "mehrschritt", 12, "ja",
    zahl("Zwei Wege für (2⁻³)². Weg A nimmt die Hochzahlen mal: 2⁻⁶ = 1/64. Weg B rechnet erst die Klammer aus: (1/?)² = 1/64. Welche Zahl steht in Weg B unter dem Bruchstrich?", 8, "2 ** 3",
         "Was ist 2⁻³ als Bruch?", "2⁻³ = 1/2³ = 1/8. Und (1/8)² = 1/64 – dasselbe wie Weg A."),
    ["64//8"], [("2*3", "2³ ist 2 · 2 · 2, nicht 2 · 3", 12), ("-8", "eine negative Hochzahl heißt Kehrwert, nicht negative Zahl", 12)],
    probe=lambda: (F(2) ** -3) ** 2 == F(1, 8) ** 2 == F(1, 64))
neu(T, "PG-08", 12, "fehler_ganz", "fehler_ganz", 3, "fehler", 12, "ja",
    wahl("Jemand vereinfacht in drei Zeilen: (1) (3a²)⁻² (2) = 3 · a⁻⁴ (3) = 3/a⁴. In welcher Zeile passiert der erste Fehler?",
         ["Zeile 2: Auch die 3 bekommt die Hochzahl −2.", "Zeile 2: a² hoch −2 ist a⁰, nicht a⁻⁴.", "Zeile 3: a⁻⁴ gehört über den Bruchstrich.", "Nirgends. 3/a⁴ stimmt."], 0,
         "Setze a = 1 ein und rechne beide Seiten aus.", "Die Hochzahl trifft jeden Faktor: (3a²)⁻² = 3⁻² · a⁻⁴ = 1/(9a⁴). Mit a = 1: links 1/9, in Zeile 2 steht 3."),
    None, {1: ("Hochzahlen addiert statt malgenommen", 12), 2: ("negative Hochzahl heißt unter den Bruchstrich", 12), 3: ("die Hochzahl trifft jeden Faktor in der Klammer", 12)},
    probe=lambda: (3 * F(2) ** 2) ** -2 == F(1, 9 * 16) != 3 / F(2) ** 4 and (F(2) ** 2) ** -2 == F(2) ** -4)
neu(T, "PG-09", 12, "fehler_ganz", "fehler_ganz", 3, "fehler", 12, "ja",
    zahl("Jemand rechnet 2⁻³ · 2⁵ = 2⁻¹⁵. In der Rechnung steckt ein Fehler. Welche Zahl kommt richtig heraus?", 4, "2 ** (5 - 3)",
         "Was geschieht mit den Hochzahlen, wenn die Basis gleich ist und malgenommen wird?", "Hochzahlen addieren: −3 + 5 = 2. 2² = 4. Probe: 1/8 · 32 = 4."),
    ["F(32,8)"], [("F(1,4)", "Zeichen der Hochzahl vertauscht", 12), ("2", "Hochzahl statt Wert angegeben", 12)],
    probe=lambda: F(2) ** -3 * F(2) ** 5 == 4)
neu(T, "PG-10", 13, "gleiche_basis_ganz", "gleiche_basis_ganz", 1, "erkennen", 12, "ja",
    wahl("Welchen Term kannst du mit der Regel „gleiche Basis: Hochzahlen addieren“ vereinfachen?", ["a³ + a⁻⁵", "a³ · b⁻⁵", "(a³)⁻⁵", "a³ · a⁻⁵"], 3,
         "Die Regel braucht zwei Dinge: dieselbe Basis und ein Malzeichen.", "Nur a³ · a⁻⁵ ist ein Produkt mit gleicher Basis: a⁻². Eine Summe lässt sich so nicht zusammenfassen."),
    None, {0: ("das ist eine Summe, kein Produkt", 3), 1: ("verschiedene Basen", 12), 2: ("Potenz einer Potenz: dort wird malgenommen", 12)},
    probe=lambda: F(2) ** 3 * F(2) ** -5 == F(2) ** -2 and F(2) ** 3 + F(2) ** -5 != F(2) ** -2 and (F(2) ** 3) ** -5 != F(2) ** -2)
neu(T, "PG-11", 13, "exponent_und_potenz", "exponent_und_potenz", 1, "erkennen", 12, "ja",
    wahl("Du sollst 5⁻² · 2⁻² im Kopf rechnen. Welcher Weg ist richtig und am kürzesten?",
         ["Hochzahlen addieren: 10⁻⁴", "Gleiche Hochzahl: (5 · 2)⁻² = 10⁻²", "Basen addieren: 7⁻²", "Einzeln: 1/25 · 1/4 und dann malnehmen"], 1,
         "Was haben die beiden Potenzen gemeinsam – die Basis oder die Hochzahl?", "Gleiche Hochzahl: Basen malnehmen. (5 · 2)⁻² = 10⁻² = 1/100. Einzeln rechnen stimmt auch, dauert aber länger."),
    None, {0: ("Hochzahlen addieren gilt nur bei gleicher Basis", 12), 2: ("Basen werden malgenommen, nicht addiert", 12), 3: ("richtig, aber umständlich: gleiche Hochzahl nicht gesehen", 12)},
    probe=lambda: F(5) ** -2 * F(2) ** -2 == F(10) ** -2 == F(1, 25) * F(1, 4) != F(10) ** -4 and F(7) ** -2 != F(10) ** -2)
neu(T, "PG-12", 4, "gleiche_basis_ganz", "gleiche_basis_ganz", 1, "direkt", 12, "nein",
    luecken("Fülle den Rechenweg aus: x⁴ : x⁻² = x hoch (4 − (k)) = xⁿ", "k = □; n = □", [-2, 6], ["0 - 2", "4 - (-2)"],
            "Beim Teilen wird die untere Hochzahl abgezogen – mit ihrem Zeichen.", "4 − (−2) = 4 + 2 = 6. Also x⁶.", HZ),
    ["-2", "4+2"], {0: [("2", "Zeichen der Hochzahl vergessen", 12)], 1: [("4-2", "minus (−2) heißt plus 2", 1), ("4*(-2)", "Hochzahlen malgenommen statt abgezogen", 12)]},
    probe=lambda: F(3) ** 4 / F(3) ** -2 == F(3) ** 6)
neu(T, "PG-13", 12, "warum_gilt", "warum_gilt", 3, "fehler", 12, "ja",
    zahl("Jemand sagt: „(−2)⁻² = −4, denn ein Minus in der Hochzahl macht das Ergebnis negativ.“ Das stimmt nicht. Welche Zahl kommt richtig heraus? (Dezimalzahl mit Komma)", 0.25, "1 / ((-2) ** 2)",
         "Eine negative Hochzahl heißt: Kehrwert bilden.", "(−2)⁻² = 1/(−2)² = 1/4 = 0,25. Die Hochzahl −2 sagt „Kehrwert“, nicht „negativ“."),
    ["F(1,4)"], [("-4", "Fehler übernommen: negative Hochzahl heißt Kehrwert", 12), ("-F(1,4)", "(−2)² ist + 4", 2), ("4", "Kehrwert vergessen", 12)],
    probe=lambda: F(-2) ** -2 == F(1, 4))

# ═════════ Klasse 8 · gleichungen.bruch ═════════
T = "gleichungen.bruch"
neu(T, "BG-01", 4, "ueber_kreuz", "ueber_kreuz", 1, "direkt", 14, "nein",
    luecken("Fülle den Rechenweg aus: 5/(x + 3) = 2/(x − 3). Über Kreuz: 5 · (x − ①) = 2 · (x + ①). Ausmultipliziert: 5x − ② = 2x + ③. Geordnet: 3x = ④. Lösung: x = ⑤.", K(5), [3, 15, 6, 21, 7],
            ["3", "5 * 3", "2 * 3", "5 * 3 + 2 * 3", "(5 * 3 + 2 * 3) / (5 - 2)"], "Über Kreuz heißt: Jeder Zähler wird mit dem Nenner der anderen Seite malgenommen.",
            "5 · (x − 3) = 2 · (x + 3) → 5x − 15 = 2x + 6 → 3x = 21 → x = 7. Probe: 5/10 = 2/4."),
    ["3", "15", "6", "15+6", "F(21,3)"], {1: [("3", "die 5 trifft auch die 3", 4)], 2: [("3", "die 2 trifft auch die 3", 4)], 3: [("6-15", "− 15 wird auf der anderen Seite zu + 15", 7)], 4: [("F(6-15,3)", "Folgefehler aus 3x = −9", 7)]},
    probe=lambda: F(5, 7 + 3) == F(2, 7 - 3))
neu(T, "BG-02", 4, "ueber_kreuz", "ueber_kreuz", 2, "mehrschritt", 14, "folge",
    luecken("Der erste Schritt ist gemacht. Rechne zu Ende: 9/(x + 4) = 3/(x − 2). Über Kreuz: 9 · (x − 2) = 3 · (x + 4). Ausmultipliziert: 9x − ① = 3x + ②. Lösung: x = ③.", K(3), [18, 12, 5],
            ["9 * 2", "3 * 4", "(9 * 2 + 3 * 4) / (9 - 3)"], "Multipliziere beide Klammern aus. Bringe dann alle x auf eine Seite.", "9x − 18 = 3x + 12 → 6x = 30 → x = 5. Probe: 9/9 = 3/3."),
    ["18", "12", "F(30,6)"], {0: [("2", "die 9 trifft auch die 2", 4)], 1: [("4", "die 3 trifft auch die 4", 4)], 2: [("F(12-18,6)", "− 18 wird auf der anderen Seite zu + 18", 7)]},
    probe=lambda: F(9, 5 + 4) == F(3, 5 - 2))
neu(T, "BG-03", 4, "hauptnenner", "hauptnenner", 1, "direkt", 7, "nein",
    luecken("Fülle den Rechenweg aus: 3/x + 1/2 = 5/x. Mal 2x auf beiden Seiten: ① + x = ②. Lösung: x = ③.", K(3), [6, 10, 4], ["3 * 2", "5 * 2", "5 * 2 - 3 * 2"],
            "Jeder Summand wird mit 2x malgenommen. Was bleibt von 3/x übrig?", "3/x · 2x = 6, 1/2 · 2x = x, 5/x · 2x = 10. Also 6 + x = 10, x = 4. Probe: 3/4 + 2/4 = 5/4."),
    ["6", "10", "10-6"], {0: [("3", "auch der Faktor 2 bleibt stehen", 7)], 1: [("5", "auch der Faktor 2 bleibt stehen", 7)], 2: [("5-3", "Folgefehler aus 3 + x = 5", 7)]},
    probe=lambda: F(3, 4) + F(1, 2) == F(5, 4))
neu(T, "BG-04", 4, "ein_bruch", "ein_bruch", 2, "mehrschritt", 7, "folge",
    luecken("Rechne zu Ende: 18/(x − 4) = 6. Mal (x − 4): 18 = ①x − ②. Geordnet: ③ = 6x. Lösung: x = ④.", K(4), [6, 24, 42, 7], ["6", "6 * 4", "18 + 6 * 4", "(18 + 6 * 4) / 6"],
            "Rechts steht nach dem Malnehmen 6 · (x − 4). Multipliziere die Klammer aus.", "18 = 6x − 24 → 42 = 6x → x = 7. Probe: 18/3 = 6."),
    ["6", "24", "18+24", "F(42,6)"], {1: [("4", "die 6 trifft auch die 4", 4)], 2: [("18-24", "− 24 wird auf der anderen Seite zu + 24", 7)], 3: [("F(18-24,6)", "Folgefehler aus −6 = 6x", 7)]},
    probe=lambda: F(18, 7 - 4) == 6)
neu(T, "BG-05", 14, "ueber_kreuz", "ueber_kreuz", 2, "darstellung", 10, "ja",
    zahl("Zwei Wege für 5/(x + 3) = 2/(x − 3). Weg A multipliziert über Kreuz: 5 · (x − 3) = 2 · (x + 3). Weg B bildet auf beiden Seiten den Kehrwert: (x + 3)/5 = (x − 3)/?. Welche Zahl steht in Weg B unter dem zweiten Bruchstrich?", 2, "10 / 5",
         "Kehrwert heißt: oben und unten tauschen – auf jeder Seite für sich.", "Aus 2/(x − 3) wird (x − 3)/2. Probe mit der Lösung x = 7: 10/5 = 4/2."),
    ["F(7-3, F(7+3,5))"], [("5", "jede Seite wird für sich umgedreht", 10), ("3", "Zahl aus dem Nenner statt aus dem Zähler genommen", 10)],
    probe=lambda: F(7 + 3, 5) == F(7 - 3, 2))
neu(T, "BG-06", 14, "hauptnenner", "hauptnenner", 2, "umkehr", 7, "ja",
    zahl("Zwei Wege für 2/x + 1/3 = 4/x. Weg A multipliziert mit 3x: 6 + x = 12. Weg B bringt erst 2/x auf die rechte Seite: 1/3 = ?/x. Welche Zahl steht in Weg B über dem Bruchstrich?", 2, "4 - 2",
         "Auf der rechten Seite stehen dann zwei Brüche mit demselben Nenner.", "4/x − 2/x = 2/x. Also 1/3 = 2/x, x = 6 – wie in Weg A."),
    ["F(1,3)*6"], [("4+2", "Hinüberbringen heißt abziehen", 7), ("4", "2/x nicht abgezogen", 7)],
    probe=lambda: F(2, 6) + F(1, 3) == F(4, 6) and 6 + 6 == 12)
neu(T, "BG-07", 12, "hauptnenner", "hauptnenner", 3, "fehler", 7, "ja",
    wahl("Jemand löst in drei Zeilen: (1) 2/x + 3 = 8/x (2) 2 + 3 = 8 (3) Widerspruch, also keine Lösung. In welcher Zeile passiert der erste Fehler?",
         ["Zeile 3: 5 = 8 ist kein Widerspruch.", "Zeile 2: Beim Malnehmen mit x wurde die 3 vergessen.", "Zeile 2: 2/x mal x ist 2x, nicht 2.", "Nirgends. Die Gleichung hat keine Lösung."], 1,
         "Mal x auf beiden Seiten heißt: jeder Summand mal x.", "Richtig: 2 + 3x = 8, also x = 2. Probe: 2/2 + 3 = 4 und 8/2 = 4."),
    None, {0: ("Widerspruch nicht erkannt", 9), 2: ("x im Nenner und x als Faktor heben sich auf", 10), 3: ("nicht jeder Summand wurde malgenommen", 7)},
    probe=lambda: F(2, 2) + 3 == F(8, 2))
neu(T, "BG-08", 12, "hauptnenner", "hauptnenner", 3, "fehler", 7, "ja",
    zahl("Jemand löst 4/x + 2 = 10/x so: 4 + 2 = 10, also keine Lösung. In der Rechnung steckt ein Fehler. Welche Zahl ist die Lösung?", 3, "(10 - 4) / 2",
         "Was wird aus der 2, wenn man beide Seiten mit x malnimmt?", "Richtig: 4 + 2x = 10 → 2x = 6 → x = 3. Probe: 4/3 + 2 = 10/3."),
    ["F(6,2)"], [("10-4", "nicht durch 2 geteilt", 8), ("F(10+4,2)", "4 auf die andere Seite addiert statt abgezogen", 7)],
    probe=lambda: F(4, 3) + 2 == F(10, 3))
neu(T, "BG-09", 13, "ueber_kreuz", "ueber_kreuz", 1, "erkennen", 14, "ja",
    wahl("Welche Gleichung löst du am schnellsten, indem du über Kreuz multiplizierst?", ["7/(x + 1) + 2 = 3/(x − 2)", "7/(x + 1) = 3", "7/(x + 1) = 3/(x − 2)", "x/7 + x/3 = 2"], 2,
         "Über Kreuz geht nur, wenn auf jeder Seite genau ein Bruch steht.", "Nur bei „Bruch = Bruch“ passt über Kreuz. Steht ein Summand daneben, braucht man den Hauptnenner."),
    None, {0: ("der Summand 2 stört: über Kreuz gilt nur für Bruch = Bruch", 14), 1: ("ein Bruch: mal Nenner genügt", 7), 3: ("zwei Brüche auf einer Seite: Hauptnenner", 11)},
    probe=lambda: True)
neu(T, "BG-10", 13, "scheinloesung", "scheinloesung", 1, "erkennen", 9, "ja",
    wahl("Du hast für x/(x − 2) = 2/(x − 2) den Wert x = 2 ausgerechnet. Was ist der nächste Schritt?",
         ["Fertig: L = {2}.", "Prüfen, ob 2 in der Definitionsmenge liegt.", "Zur Sicherheit die Probe mit x = 0 machen.", "Beide Seiten noch einmal mit (x − 2) malnehmen."], 1,
         "Was passiert mit dem Nenner, wenn du deinen Wert einsetzt?", "Für x = 2 wird der Nenner 0. Die 2 ist ausgeschlossen, also hat die Gleichung keine Lösung: L = { }."),
    None, {0: ("Definitionsmenge nicht geprüft", 9), 2: ("Probe gehört an die gefundene Zahl, nicht an eine andere", 9), 3: ("Umformen ersetzt die Prüfung nicht", 9)},
    probe=lambda: 2 - 2 == 0)
neu(T, "BG-11", 17, "ein_bruch", "ein_bruch", 2, "umkehr", 8, "ja",
    zahl("Für die Durchschnittsgeschwindigkeit gilt: Geschwindigkeit = Strecke : Zeit. Ein Zug fährt 150 km mit durchschnittlich 60 km/h. Wie viele Stunden braucht er?", 2.5, "150 / 60",
         "Setze die bekannten Zahlen ein. Die gesuchte Größe steht dann im Nenner.", "60 = 150 : t. Mal t: 60 · t = 150. Durch 60: t = 2,5 Stunden.", einheit="h"),
    ["F(5,2)"], [("150*60", "malgenommen statt geteilt", 8), ("F(60,150)", "Strecke und Geschwindigkeit vertauscht", 14)],
    probe=lambda: 150 / F(5, 2) == 60)
neu(T, "BG-12", 17, "verhaeltnis", "verhaeltnis", 2, "umkehr", 8, "ja",
    zahl("Es gilt: Preis je Kilogramm = Preis : Masse. Kirschen kosten 6,40 € je Kilogramm. Du zahlst 4,80 €. Wie viele Kilogramm hast du gekauft?", 0.75, "480 / 640",
         "Setze ein: Welche Größe steht im Nenner und ist gesucht?", "6,40 = 4,80 : m. Mal m und durch 6,40: m = 4,80 : 6,40 = 0,75 kg.", einheit="kg"),
    ["F(3,4)"], [("F(640*480,10000)", "malgenommen statt geteilt", 8), ("F(640-480,100)", "abgezogen statt das Verhältnis gebildet", 14)],
    probe=lambda: F(480, 100) / F(3, 4) == F(640, 100))
neu(T, "BG-13", "B", "verhaeltnis", "verhaeltnis", 2, "darstellung", 14, "ja",
    luecken("Zwillingszeilen. Zeile 1 mit Zahlen: 2/3 = 8/①. Zeile 2 mit x – nicht lösen, nur über Kreuz schreiben: 2/x = 8/(x + 9) wird zu 2 · (x + 9) = ② · x.", K(2), [12, 8], ["3 * 8 / 2", "8"],
            "In Zeile 1: Womit wurde der Zähler malgenommen?", "Zähler mal 4, also auch Nenner mal 4: 12. In Zeile 2 gehört jeder Zähler zum Nenner der anderen Seite: 2 · (x + 9) = 8 · x."),
    ["F(8, F(2,3))", "F(2*(3+9),3)"], {0: [("3+6", "oben plus 6 heißt nicht unten plus 6", 10), ("3*8", "über Kreuz gerechnet, aber nicht durch 2 geteilt", 8)], 1: [("2", "die 8 gehört zum x", 14)]},
    probe=lambda: F(2, 3) == F(8, 12) and 2 * (3 + 9) == 8 * 3)

# ═════════ Prüfen ═════════
KLASSE = {"zahlen.rechengesetze": 5, "zahlen.ganz": 5, "terme.potenzgesetze_ganzzahlig": 8, "gleichungen.bruch": 8}
assert len(A) == 52 and len({a["kenn"] for a in A}) == 52
etiketten, je_thema = [], {}
for a in A:
    q, kenn = a["aufgabe"], a["kenn"]
    y, o = q["y"], q["o"]
    assert a["regel"] in REGEL and a["zaehlt"] in ZAEHLT and a["typ"] in TYP, kenn
    assert ip.STUFE_VON[q["g"]] == q["s"], kenn
    assert (a["zaehlt"] == "nein") == (a["typ"] == 4 and q["s"] == 1), kenn
    assert len(q["w"]) >= 15 and q["h"], kenn
    eintrag = dict(kennung=kenn, thema=a["thema"], klasse=KLASSE[a["thema"]], lernkarte=q["l"], typ=TYP[a["typ"]], antwortform=y, stufe=q["s"], g=q["g"],
                   regel={"nr": a["regel"], "name": REGEL[a["regel"]]}, zaehlt=a["zaehlt"], frage=q["f"]["text"], fehlbilder=[])
    if a["probe"] is not None:
        assert a["probe"]() is True, kenn
    if y == "zahl":
        soll = F(str(o["wert"]))
        assert ip.rechne(q["c"]) == soll, (kenn, "c")                         # Weg 1
        assert len(a["zweit"]) == 1 and z2(a["zweit"][0]) == soll, (kenn, "zweit")   # Weg 2
        assert a["zweit"][0].replace(" ", "") != q["c"].replace(" ", ""), kenn
        werte = set()
        for ausdruck, name, nr in a["fb"]:
            w = z2(ausdruck)
            assert w != soll and w not in werte and nr in REGEL, (kenn, ausdruck, w)
            werte.add(w)
            assert w.denominator in (1, 2, 4, 5, 10, 20, 25, 50, 100, 10000), (kenn, w)   # als Dezimalzahl eintippbar
            eintrag["fehlbilder"].append({"antwort": float(w) if w.denominator != 1 else int(w), "fehlbild": name, "regel": {"nr": nr, "name": REGEL[nr]}})
        assert len(a["fb"]) >= 2 or kenn in (), kenn
        zahlen_im_tipp = re.findall(r"−?\d+(?:,\d+)?", q["h"])
        assert str(o["wert"]).replace(".", ",").replace("-", "−") not in zahlen_im_tipp, (kenn, "Tipp verrät das Ergebnis")
    elif y == "luecken":
        soll = [F(v) for v in o["werte"]]
        assert q["f"]["schablone"].count("□") == len(soll) and all(isinstance(v, int) for v in o["werte"]), kenn
        assert [ip.rechne(c) for c in q["c"]] == soll, (kenn, "c")
        assert len(a["zweit"]) == len(soll) and [z2(z) for z in a["zweit"]] == soll, (kenn, "zweit")
        assert a["fb"], kenn
        for i, liste in a["fb"].items():
            werte = set()
            for ausdruck, name, nr in liste:
                w = z2(ausdruck)
                assert w != soll[i] and w not in werte and w.denominator == 1 and nr in REGEL, (kenn, i, ausdruck, w)
                werte.add(w)
                eintrag["fehlbilder"].append({"luecke": i + 1, "antwort": int(w), "fehlbild": name, "regel": {"nr": nr, "name": REGEL[nr]}})
    else:
        assert a["probe"] is not None and len(q["a"]) == 4 and len(set(q["a"])) == 4, kenn
        assert set(a["fb"]) == set(range(4)) - {o["index"]}, kenn
        for i, (name, nr) in sorted(a["fb"].items()):
            assert nr in REGEL, kenn
            eintrag["fehlbilder"].append({"index": i, "antwort": q["a"][i], "fehlbild": name, "regel": {"nr": nr, "name": REGEL[nr]}})
    etiketten.append(eintrag)
    je_thema.setdefault(a["thema"], []).append(q)

# Lage der richtigen Antwort bei Auswahl gemischt
lagen = [a["aufgabe"]["o"]["index"] for a in A if a["aufgabe"]["y"] == "auswahl"]
assert len(set(lagen)) == 4, lagen

for thema, liste in je_thema.items():
    assert 12 <= len(liste) <= 16, (thema, len(liste))
    with open(os.path.join(HIER, f"{thema}.neu.json"), "w", encoding="utf-8") as f:
        json.dump(liste, f, ensure_ascii=False, indent=1)
        f.write("\n")
with open(os.path.join(HIER, "etiketten.json"), "w", encoding="utf-8") as f:
    json.dump({"hinweis": "Zusatzangaben je Aufgabe, für die das Aufgabenformat kein Feld hat. Reihenfolge wie in <thema>.neu.json.", "aufgaben": etiketten}, f, ensure_ascii=False, indent=1)
    f.write("\n")


# Lauf mit tools/inhalt_pruefen.py: Themen-Datei kopieren, neue Aufgaben anhängen, vorher/nachher vergleichen
def lauf(pfad):
    r = subprocess.run([sys.executable, "-I", os.path.join(WURZEL, "tools", "inhalt_pruefen.py"), pfad], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


print("Thema                              neu  Typen                                 inhalt_pruefen vorher → nachher")
with tempfile.TemporaryDirectory() as tmp:
    for thema, liste in je_thema.items():
        quelle = os.path.join(WURZEL, "inhalte", "themen", f"{thema}.json")
        d = json.load(open(quelle, encoding="utf-8"))
        lernkarten = {e["lernziel"] for e in d["inhalt"]["etappen"]}
        teile = {t["k"] for t in d["inhalt"]["teilfaehigkeiten"]}
        assert all(q["l"] in lernkarten and q["t"] in teile for q in liste), thema
        alt_texte = {x["f"].get("text") for x in d["aufgaben"]}
        assert not any(q["f"]["text"] in alt_texte for q in liste), thema
        code0, aus0 = lauf(quelle)
        d["aufgaben"] = d["aufgaben"] + liste
        ziel = os.path.join(tmp, f"{thema}.json")
        json.dump(d, open(ziel, "w", encoding="utf-8"), ensure_ascii=False)
        code1, aus1 = lauf(ziel)
        f0 = [z for z in aus0.splitlines() if "FEHLER" in z.upper() or z.strip().startswith("✗")]
        f1 = [z for z in aus1.splitlines() if "FEHLER" in z.upper() or z.strip().startswith("✗")]
        typen = {}
        for a in A:
            if a["thema"] == thema:
                typen[str(a["typ"])] = typen.get(str(a["typ"]), 0) + 1
        print(f"{thema:34} {len(liste):3}  {str(dict(sorted(typen.items()))):38} Code {code0} → {code1}")
        if code1 != 0 or code0 != 0:
            print(aus1[-1500:])
        assert code0 == 0 and code1 == 0, thema
print("52 Aufgaben: zweifach nachgerechnet, Fehlbilder berechnet, inhalt_pruefen ohne Fehler")
print("OK")
