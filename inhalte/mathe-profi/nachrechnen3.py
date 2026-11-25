"""Mathe-Profi, Auftrag 3: Musterstapel „Weg-Aufgaben“ für den Flug Rechengesetze (Klasse 5) – nur vorhandene Antwortformen.

Aufruf: python3 -I inhalte/mathe-profi/nachrechnen3.py

Jede Aufgabe wird auf zwei Wegen geprüft:
  Weg 1 = hier im Skript von Hand gerechnet (Python-Ganzzahlen),
  Weg 2 = der exakte Rechner des Repos (`rechne` aus tools/inhalt_pruefen.py) wertet die Terme aus dem Aufgabentext aus.
Dazu: Eindeutigkeit (genau eine richtige Auswahl), Musterregeln (M1–M6) und die Antwortform-Prüfung des Repos (`pruefe_antwort`).
Schreibt aufgaben-auftrag3.json und die Aufgabenliste in auftrag3.md. Bricht mit AssertionError ab, wenn etwas nicht stimmt.
"""
import importlib.util
import json
import os
import re
import sys
from fractions import Fraction as F

sys.dont_write_bytecode = True          # tools/__pycache__ ist im Repo – nicht anfassen
ORDNER = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("inhalt_pruefen", os.path.join(ORDNER, "..", "..", "tools", "inhalt_pruefen.py"))
ip = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ip)


def wert(term):
    """Weg 2: Term aus dem Aufgabentext mit dem Rechner des Repos auswerten."""
    t = term.replace("·", "*").replace("−", "-").replace(":", "/").replace(" ", "")
    return ip.rechne(t)


AUFGABEN = []


def neu(nr, muster, l, s, g, y, f, o, h, w, weg1, weg2, falsch, a=None, c=None):
    d = {"nr": nr, "muster": muster, "l": l, "t": l, "p": "uebung", "s": s, "g": g, "y": y, "f": f}
    if a is not None:
        d["a"] = a
    d["o"] = o
    if c is not None:
        d["c"] = c
    d.update({"h": h, "w": w, "weg": True, "probe": {"weg1": weg1, "weg2": weg2}, "falsch": falsch})
    AUFGABEN.append(d)
    return d


def eine_richtige(optionen, ziel):
    """Genau eine Option hat den Zielwert (Weg 2 über den Repo-Rechner). Gibt den Index zurück."""
    werte = [wert(t) for t in optionen]
    treffer = [i for i, v in enumerate(werte) if v == ziel]
    assert len(treffer) == 1, (optionen, werte, ziel)
    return treffer[0], werte


def zeilen_tabelle(zeilen):
    return {"typ": "tabelle", "kopf": ["", "Rechnung"], "zeilen": [[f"Zeile {i + 1}", z] for i, z in enumerate(zeilen)]}


def strahl(start, ende, abschnitte):
    return {"typ": "zahlenstrahl", "start": start, "ende": ende, "abschnitte": abschnitte, "beschriftet": "anfang_ende"}


def naechster_strich(g, v, sinnvoll, fehler):
    """Muster M5: nächster Strich eindeutig, nicht in der Mitte, nicht am Rand; jede sinnvolle Schätzung landet auf
    demselben Strich; typische Fehler landen auf einem anderen."""
    n, schritt = g["abschnitte"], F(g["ende"] - g["start"], g["abschnitte"])
    idx = lambda x: min(range(n + 1), key=lambda i: abs(g["start"] + i * schritt - x))
    i = idx(v)
    assert abs(g["start"] + i * schritt - v) <= F(3, 10) * schritt, "genauer Wert liegt zu nah an der Mitte zweier Striche"
    assert 0 < i < n and 2 * i != n, "Lösung am Rand oder in der Skalenmitte"
    for sch in sinnvoll:
        assert idx(sch) == i and abs(g["start"] + i * schritt - sch) < F(1, 2) * schritt, ("sinnvolle Schätzung trifft anderen Strich", sch)
    for fe in fehler:
        assert g["start"] <= fe <= g["ende"] and idx(fe) != i, ("typischer Fehler nicht unterscheidbar", fe)
    return i


# ───────────── vorteil: tauschen und verbinden ─────────────
# W1 – M1 „Erster Schritt“
fak = [2, 19, 50]
paare = [(0, 1), (1, 2), (0, 2)]
prod = [fak[i] * fak[j] for i, j in paare]
glatt = [k for k, p in enumerate(prod) if p in (10, 100, 1000, 10000)]
assert prod == [38, 950, 100] and glatt == [2]                                        # Weg 1
opt = ["2 · 19", "19 · 50", "2 · 50"]
i, w2 = eine_richtige(opt, 100)                                                        # Weg 2
assert i == 2 and wert("2 · 19 · 50") == 100 * 19 == 1900
neu("W1", "M1", "vorteil", 1, "erkennen", "auswahl",
    {"text": "Du rechnest 2 · 19 · 50 geschickt. Welche zwei Zahlen ergeben malgenommen eine glatte Zahl?"},
    {"index": 2}, "Eine glatte Zahl ist 10, 100 oder 1 000. Probier die Paare im Kopf.",
    "2 · 50 = 100. Dann ist 2 · 19 · 50 = 100 · 19 = 1 900. Die anderen Paare ergeben 38 und 950.",
    "Produkte der drei Paare: 38, 950, 100 – nur 2 · 50 ist glatt.",
    "Repo-Rechner: 2 · 19 = 38, 19 · 50 = 950, 2 · 50 = 100; 2 · 19 · 50 = 1 900.",
    "„2 und 19“ – rechnet von links, sucht kein Paar", a=["2 und 19", "19 und 50", "2 und 50"])

# W2 – M2 „Lücke im faulen Weg“
assert 5 * 20 == 100 and 100 * 43 == 4300 and wert("5 · 43 · 20") == 4300 == wert("100 · 43")
neu("W2", "M2", "vorteil", 2, "umkehr", "luecken",
    {"text": "Rechne faul: Fasse zuerst die zwei Zahlen zusammen, die eine glatte Zahl ergeben.",
     "schablone": "5 · 43 · 20 = □ · 43 = □", "hinweis": "Je Kästchen eine ganze Zahl."},
    {"werte": [100, 4300]}, "Welche zwei der drei Zahlen passen gut zusammen?",
    "5 · 20 = 100. Also 5 · 43 · 20 = 100 · 43 = 4 300.",
    "5 · 20 = 100, 100 · 43 = 4 300.", "Repo-Rechner: 5 · 43 · 20 = 4 300 = 100 · 43; von links: 215 · 20 = 4 300.",
    "215 und 4 300 – rechnet von links und trägt das Zwischenergebnis ein", c=["5 * 20", "5 * 43 * 20"])
assert 5 * 43 == 215 and 215 * 20 == 4300

# W3 – M4 „Fehlerzeile“
z = ["25 · 16 · 4 = 25 · 4 · 16", "= 100 · 16", "= 116"]
assert wert("25 · 16 · 4") == wert("25 · 4 · 16") == wert("100 · 16") == 1600 != 116    # Zeile 1 und 2 stimmen, Zeile 3 nicht
assert 25 * 4 == 100 and 100 + 16 == 116
neu("W3", "M4", "vorteil", 3, "fehler", "auswahl",
    {"text": "Jemand rechnet 25 · 16 · 4 geschickt – und macht einen Fehler. In welcher Zeile?", "grafik": zeilen_tabelle(z)},
    {"index": 2}, "Prüfe jede Zeile für sich: Ist sie gleich viel wert wie die Zeile davor?",
    "Zeile 1 tauscht nur (erlaubt bei mal). Zeile 2: 25 · 4 = 100, stimmt. Zeile 3: 100 · 16 ist 1 600, nicht 116 – dort wurde plus gerechnet.",
    "25 · 4 = 100; 100 · 16 = 1 600; 100 + 16 = 116.", "Repo-Rechner: Zeile 1 links und rechts 1 600, Zeile 2 1 600, Zeile 3 behauptet 116.",
    "„Zeile 1“ – hält das Tauschen für den Fehler", a=["Zeile 1", "Zeile 2", "Zeile 3", "Alles richtig."])

# ───────────── differenz_summe ─────────────
opt = ["83 − (27 + 13)", "83 − (27 − 13)", "(83 − 13) + 27", "27 − 83 − 13"]
ziel = 83 - 27 - 13
i, w2 = eine_richtige(opt, ziel)
assert ziel == 43 and i == 0 and [83 - 40, 83 - 14, 70 + 27, 27 - 83 - 13] == [43, 69, 97, -69] == w2
neu("D1", "M3", "differenz_summe", 3, "begruenden", "auswahl",
    {"text": "83 − 27 − 13 soll geschickt gerechnet werden. Nur eine Umformung hat denselben Wert. Welche?"},
    {"index": 0}, "Zweimal abziehen ist dasselbe wie einmal die Summe abziehen.",
    "27 und 13 werden beide abgezogen, zusammen 40: 83 − (27 + 13) = 83 − 40 = 43. Die anderen ergeben 69, 97 und −69.",
    "83 − 27 − 13 = 43; Optionen: 43, 69, 97, −69.", "Repo-Rechner wertet alle vier Terme aus: nur der erste ergibt 43.",
    "„83 − (27 − 13)“ – setzt die Klammer, ohne das Rechenzeichen in der Klammer zu ändern", a=opt)

# ───────────── verteilen ─────────────
assert 6 * 20 - 6 * 2 == 108 == 6 * 18 == wert("6 · 20 − 6 · 2") and 20 - 18 == 2
neu("V1", "M2", "verteilen", 2, "umkehr", "luecken",
    {"text": "Rechne 6 · 18 so, als wären es 6 · 20.", "schablone": "6 · 18 = 6 · 20 − 6 · □ = □", "hinweis": "Je Kästchen eine ganze Zahl."},
    {"werte": [2, 108]}, "Um wie viel ist 20 größer als 18? Das hast du in jeder der 6 Reihen zu viel.",
    "18 = 20 − 2. Also 6 · 18 = 6 · 20 − 6 · 2 = 120 − 12 = 108.",
    "120 − 12 = 108 = 6 · 18.", "Repo-Rechner: 6 · 20 − 6 · 2 = 108 = 6 · 18.",
    "2 und 118 – zieht nur 2 ab statt 6 · 2", c=["20 - 18", "6 * 18"])
assert 120 - 2 == 118

assert 47 + 53 == 100 and 13 * 100 == 1300 == 13 * 47 + 13 * 53 == wert("13 · 47 + 13 · 53") and 13 * 47 == 611 and 13 * 53 == 689
neu("V2", "M2", "verteilen", 2, "darstellung", "luecken",
    {"text": "Klammere den gemeinsamen Faktor aus.", "schablone": "13 · 47 + 13 · 53 = 13 · □ = □", "hinweis": "Je Kästchen eine ganze Zahl."},
    {"werte": [100, 1300]}, "Beide Produkte haben die 13. Was bleibt in der Klammer?",
    "13 · 47 + 13 · 53 = 13 · (47 + 53) = 13 · 100 = 1 300.",
    "47 + 53 = 100; 13 · 100 = 1 300.", "Repo-Rechner, stur: 611 + 689 = 1 300.",
    "100 und 2 600 – zählt die beiden 13 zusammen", c=["47 + 53", "13 * 47 + 13 * 53"])

opt = ["8 · 100 − 1", "8 · 100 − 8", "8 · 90 + 9", "800 − 99"]
i, w2 = eine_richtige(opt, 8 * 99)
assert i == 1 and 8 * 99 == 792 and w2 == [799, 792, 729, 701]
neu("V3", "M3", "verteilen", 3, "begruenden", "auswahl",
    {"text": "8 · 99 soll im Kopf gerechnet werden. Nur ein Weg stimmt. Welcher?"},
    {"index": 1}, "99 ist 100 − 1. Wie oft wird die 1 abgezogen?",
    "8 · 99 = 8 · 100 − 8 · 1 = 800 − 8 = 792. Die 1 fehlt in jedem der 8 Hunderter.",
    "8 · 99 = 792; Optionen: 799, 792, 729, 701.", "Repo-Rechner wertet alle vier Terme aus: nur „8 · 100 − 8“ ergibt 792.",
    "„8 · 100 − 1“ – zieht die 1 nur einmal ab", a=opt)

z = ["6 · 29 = 6 · 30 − 6 · 1", "= 180 − 1", "= 179"]
assert wert("6 · 29") == wert("6 · 30 − 6 · 1") == 174 and wert("180 − 1") == 179 != 174 and 180 - 6 == 174
neu("V4", "M4", "verteilen", 3, "fehler", "auswahl",
    {"text": "Jemand rechnet 6 · 29 in drei Zeilen. In welcher Zeile entsteht der Fehler?", "grafik": zeilen_tabelle(z)},
    {"index": 1}, "Rechne die beiden Teile der ersten Zeile einzeln aus und vergleiche mit der nächsten Zeile.",
    "Zeile 1 stimmt. In Zeile 2 müsste 180 − 6 stehen, denn 6 · 1 = 6. Zeile 3 rechnet nur mit dem falschen Wert weiter. Richtig: 174.",
    "6 · 30 = 180, 6 · 1 = 6, 180 − 6 = 174.", "Repo-Rechner: Zeile 1 beide Seiten 174; Zeile 2 ergibt 179.",
    "„Zeile 3“ – sucht den Fehler dort, wo er sichtbar wird, nicht wo er entsteht", a=["Zeile 1", "Zeile 2", "Zeile 3", "Alles richtig."])

# ───────────── kopfrechnen ─────────────
assert 15 * 2 == 30 and 24 // 2 == 12 and 30 * 12 == 360 == 15 * 24 == wert("15 · 24")
neu("P1", "M2", "kopfrechnen", 2, "umkehr", "luecken",
    {"text": "Verdopple die eine Zahl und halbiere die andere.", "schablone": "15 · 24 = 30 · □ = □", "hinweis": "Je Kästchen eine ganze Zahl."},
    {"werte": [12, 360]}, "Aus 15 wurde 30. Was muss dann mit der 24 passieren, damit das Ergebnis gleich bleibt?",
    "15 verdoppelt ist 30, also 24 halbieren: 12. 30 · 12 = 360.",
    "30 · 12 = 360.", "Repo-Rechner: 15 · 24 = 360.",
    "24 und 720 – verdoppelt, ohne zu halbieren", c=["24 / 2", "15 * 24"])
assert 30 * 24 == 720

assert 68 // 2 == 34 and 10 * 34 == 340 == 5 * 68 == wert("5 · 68")
neu("P2", "M2", "kopfrechnen", 2, "mehrschritt", "luecken",
    {"text": "Mal 5 geht leicht über mal 10. Fülle die Lücken.", "schablone": "5 · 68 = 10 · □ = □", "hinweis": "Je Kästchen eine ganze Zahl."},
    {"werte": [34, 340]}, "5 ist die Hälfte von 10. Wovon nimmst du dann die Hälfte?",
    "5 · 68 = 10 · 34, denn 68 : 2 = 34. Das sind 340.",
    "68 : 2 = 34; 10 · 34 = 340.", "Repo-Rechner: 5 · 68 = 340.",
    "68 und 680 – nimmt mal 10 und vergisst zu halbieren", c=["68 / 2", "5 * 68"])

opt = ["25 · 4 + 7", "100 · 28", "100 · 7", "25 · 20 + 8"]
i, w2 = eine_richtige(opt, 25 * 28)
assert i == 2 and 25 * 28 == 700 and w2 == [107, 2800, 700, 508] and 28 == 4 * 7
neu("P3", "M3", "kopfrechnen", 3, "begruenden", "auswahl",
    {"text": "25 · 28 soll im Kopf gerechnet werden. Nur ein Weg stimmt. Welcher?"},
    {"index": 2}, "Zerlege 28 in zwei Faktoren. Einer davon passt gut zur 25.",
    "25 · 28 = 25 · 4 · 7 = 100 · 7 = 700.",
    "25 · 28 = 700; Optionen: 107, 2 800, 700, 508.", "Repo-Rechner wertet alle vier Terme aus: nur „100 · 7“ ergibt 700.",
    "„25 · 20 + 8“ – zerlegt die 28, nimmt aber die 8 nicht mal 25", a=opt)

opt = ["6 · 50 − 1", "6 · 40 + 9", "6 · 50 − 6"]
i, w2 = eine_richtige(opt, 6 * 49)
assert i == 2 and 6 * 49 == 294 and w2 == [299, 249, 294]
neu("P4", "M3", "kopfrechnen", 1, "erkennen", "auswahl",
    {"text": "Welche Rechnung hat denselben Wert wie 6 · 49?"},
    {"index": 2}, "49 ist eins weniger als 50 – und zwar in jedem der 6 Päckchen.",
    "6 · 49 = 6 · 50 − 6 · 1 = 300 − 6 = 294.",
    "6 · 49 = 294; Optionen: 299, 249, 294.", "Repo-Rechner wertet alle drei Terme aus: nur „6 · 50 − 6“ ergibt 294.",
    "„6 · 50 − 1“ – zieht die 1 nur einmal ab", a=opt)

# ───────────── ueberschlag ─────────────
g = strahl(0, 15000, 10)
v = 312 * 29
i = naechster_strich(g, v, sinnvoll=[300 * 30, 312 * 30, 300 * 29, 310 * 30], fehler=[900, 312 + 29, 300 * 20])
assert v == 9048 == wert("312 · 29") and i == 6 and 6 * 1500 == 9000
neu("U1", "M5", "ueberschlag", 2, "darstellung", "markierung",
    {"text": "Ohne genau zu rechnen: Tippe den Strich an, der am nächsten an 312 · 29 liegt.", "grafik": g},
    {"index": 6}, "Runde beide Zahlen so, dass du im Kopf malnehmen kannst. Was ist ein Abschnitt wert?",
    "312 ≈ 300 und 29 ≈ 30: etwa 9 000. Ein Abschnitt ist 1 500 wert, 9 000 ist der 6. Strich nach der 0. Genau: 9 048.",
    "300 · 30 = 9 000; Strichwerte 0, 1 500, …; 9 000 = 6 · 1 500.",
    "Repo-Rechner: 312 · 29 = 9 048, Abstand zum 6. Strich 48 (von 1 500). Auch 9 360, 8 700 und 9 300 liegen am 6. Strich.",
    "Strich 1 oder Strich 0 (Ergebnis 900 oder 341) – Stelle verloren oder plus statt mal gerechnet")

g = strahl(0, 1000, 10)
v = F(5580, 18)
i = naechster_strich(g, v, sinnvoll=[F(6000, 20), F(5400, 18), F(5600, 20), F(6000, 18) - 30], fehler=[31])
assert v == 310 == wert("5580 : 18") and i == 3
neu("U2", "M5", "ueberschlag", 2, "einkleidung", "markierung",
    {"text": "5 580 Flaschen werden auf 18 Lastwagen verteilt. Tippe den Strich an, der am nächsten an der Zahl je Lastwagen liegt.", "grafik": g},
    {"index": 3}, "Runde beide Zahlen so, dass das Teilen im Kopf geht. Was ist ein Abschnitt wert?",
    "6 000 : 20 = 300. Ein Abschnitt ist 100 wert, 300 ist der 3. Strich nach der 0. Genau: 5 580 : 18 = 310.",
    "6 000 : 20 = 300; 5 400 : 18 = 300.", "Repo-Rechner: 5 580 : 18 = 310, Abstand zum 3. Strich 10 (von 100).",
    "Strich bei 0 (31) – eine Stelle verloren")

genau, tol = 38 * 52, 300
schaetz = [40 * 50, 38 * 50, 40 * 52, 40 * 55]
assert genau == 1976 == wert("38 · 52") and tol == round(0.15 * genau, -2)
assert all(abs(s - genau) <= tol for s in schaetz)                                    # jede vernünftige Schätzung zählt
assert all(abs(f - genau) > tol for f in (200, 20000, 38 + 52, 30 * 50, 40 * 60))     # Stellenfehler, plus, grobes Runden: falsch
neu("U3", "M6", "ueberschlag", 2, "mehrschritt", "zahl",
    {"text": "Ein Stadionblock hat 38 Reihen mit je 52 Plätzen. Wie viele Plätze sind das ungefähr? Überschlage im Kopf – jede vernünftige Schätzung zählt."},
    {"wert": 1976, "toleranz": 300}, "Runde beide Zahlen auf Zehner.",
    "38 ≈ 40 und 52 ≈ 50: etwa 40 · 50 = 2 000 Plätze. Genau sind es 1 976. Alles von 1 676 bis 2 276 zählt.",
    "40 · 50 = 2 000, liegt 24 neben dem genauen Wert.",
    "Repo-Rechner: 38 · 52 = 1 976. In der Toleranz: 2 000, 1 900, 2 080, 2 200. Außerhalb: 200, 20 000, 90, 1 500, 2 400.",
    "200 – eine Null vergessen (40 · 50 als 4 · 50)", c="38 * 52")

opt = ["50 · 70", "50 · 60", "40 · 60"]
genau = 45 * 65
abst = [abs(wert(t) - genau) for t in opt]
assert genau == 2925 and abst == [575, 75, 525] and abst.index(min(abst)) == 1 and sorted(abst)[0] < sorted(abst)[1]
assert [50 * 70 - 2925, 2925 - 50 * 60 + 150, 2925 - 40 * 60] == [575, 75, 525]
neu("U4", "M3", "ueberschlag", 3, "begruenden", "auswahl",
    {"text": "45 · 65 soll überschlagen werden. Welche Rechnung liegt am nächsten am genauen Ergebnis?"},
    {"index": 1}, "Wenn du beide Zahlen aufrundest, wird das Ergebnis zu groß. Was passiert, wenn du eine auf- und eine abrundest?",
    "Genau sind es 2 925. 50 · 60 = 3 000 liegt nur 75 daneben: eine Zahl rauf, eine runter, die Fehler gleichen sich aus. 50 · 70 = 3 500 und 40 · 60 = 2 400 liegen über 500 daneben.",
    "Abstände zu 2 925: 575, 75, 525.", "Repo-Rechner: 50 · 70 = 3 500, 50 · 60 = 3 000, 40 · 60 = 2 400.",
    "„50 · 70“ – rundet beide nach der Schulregel auf", a=opt)

# ───────────── schriftlich_geteilt ─────────────
def teile(dividend, teiler, fehler_in=None, fehler_rest=None):
    """Schriftliches Teilen Schritt für Schritt. fehler_in: Schritt (ab 0), in dem der Rest falsch notiert wird."""
    zeilen, rest, erg, schritt = [], 0, "", 0
    for zi in str(dividend):
        akt = rest * 10 + int(zi)
        if not erg and akt < teiler:
            rest = akt
            continue
        q = akt // teiler
        r = akt - q * teiler
        if schritt == fehler_in:
            r = fehler_rest
        zeilen.append((akt, q, q * teiler, r))
        erg += str(q)
        rest, schritt = r, schritt + 1
    return int(erg), rest, zeilen


richtig = teile(3888, 16)
falsch = teile(3888, 16, fehler_in=1, fehler_rest=2)
assert richtig[:2] == (243, 0) and 243 * 16 == 3888 == wert("243 · 16")
assert falsch[:2] == (241, 12) and falsch[2] == [(38, 2, 32, 6), (68, 4, 64, 2), (28, 1, 16, 12)] and 68 - 64 == 4
z = [f"{a_} : 16 = {q_}, {q_} · 16 = {m_}, Rest {r_}" for a_, q_, m_, r_ in falsch[2]]
neu("S1", "M4", "schriftlich_geteilt", 3, "fehler", "auswahl",
    {"text": "Jemand rechnet 3 888 : 16 schriftlich und erhält 241 Rest 12. In welcher Zeile entsteht der Fehler?", "grafik": zeilen_tabelle(z)},
    {"index": 1}, "Prüfe in jeder Zeile die Minus-Rechnung: Zahl minus Produkt gleich Rest?",
    "Zeile 2: 68 − 64 = 4, nicht 2. Richtig geht es mit 48 : 16 = 3 weiter, Ergebnis 243. Probe: 243 · 16 = 3 888.",
    "Schritt für Schritt: 38 : 16 = 2 Rest 6; 68 : 16 = 4 Rest 4; 48 : 16 = 3 Rest 0 → 243.",
    "Repo-Rechner, Probe: 243 · 16 = 3 888; die falsche Lösung ergibt 241 · 16 + 12 = 3 868.",
    "„Zeile 3“ – dort sieht die Rechnung fremd aus (28 statt 48), der Fehler entsteht aber davor",
    a=["Zeile 1", "Zeile 2", "Zeile 3", "Alles richtig."])
assert 241 * 16 + 12 == 3868 == wert("241 · 16 + 12")

assert teile(3264, 16)[:2] == (204, 0) and 204 * 16 == 3264 == wert("204 · 16") and 24 * 16 == 384
z = ["32 : 16 = 2, Rest 0", "6 herunterholen: 6 : 16 geht nicht, also gleich die 4 dazuholen", "64 : 16 = 4, Rest 0", "Ergebnis: 24"]
opt = ["In Zeile 1: 32 : 16 ist nicht 2.", "In Zeile 2: Für „geht nicht“ fehlt eine 0 im Ergebnis.", "In Zeile 3: 64 : 16 ist nicht 4.", "Nichts, 24 stimmt."]
neu("S2", "M4", "schriftlich_geteilt", 3, "begruenden", "auswahl",
    {"text": "Jemand rechnet 3 264 : 16 = 24. Was ist schiefgegangen?", "grafik": zeilen_tabelle(z)},
    {"index": 1}, "Mach die Probe im Kopf: Ist 24 · 16 ungefähr 3 000?",
    "Jede heruntergeholte Ziffer gibt eine Ziffer im Ergebnis. 6 : 16 = 0, diese 0 fehlt. Richtig: 204. Probe: 204 · 16 = 3 264, aber 24 · 16 = 384.",
    "Schritt für Schritt: 32 : 16 = 2; 6 : 16 = 0 Rest 6; 64 : 16 = 4 → 204.",
    "Repo-Rechner, Probe: 204 · 16 = 3 264; 24 · 16 = 384.",
    "„Nichts, 24 stimmt.“ – jede Zeile sieht für sich richtig aus", a=opt)
assert 32 // 16 == 2 and 64 // 16 == 4

g = strahl(0, 500, 10)
v = F(8190, 39)
i = naechster_strich(g, v, sinnvoll=[F(8000, 40), F(8200, 40), F(8000, 39)], fehler=[21])
assert v == 210 == wert("8190 : 39") and i == 4 and 39 * 210 == 8190
neu("S3", "M5", "schriftlich_geteilt", 2, "darstellung", "markierung",
    {"text": "Bevor du schriftlich teilst: Tippe den Strich an, der am nächsten an 8 190 : 39 liegt.", "grafik": g},
    {"index": 4}, "Runde beide Zahlen so, dass eine Aufgabe aus dem Einmaleins entsteht.",
    "8 000 : 40 = 200. Ein Abschnitt ist 50 wert, 200 ist der 4. Strich nach der 0. Genau: 210. So weißt du vorher: Das Ergebnis hat drei Stellen.",
    "8 000 : 40 = 200 = 4 · 50.", "Repo-Rechner: 8 190 : 39 = 210, Abstand zum 4. Strich 10 (von 50).",
    "Strich bei 0 (21) – eine Stelle verloren")

q = 7344 // 24
assert q == 306 == wert("7344 : 24") and len(str(q)) == 3                             # Weg 1: ausrechnen
assert 24 * 100 <= 7344 < 24 * 1000                                                    # Weg 2: Schranken, ohne zu teilen
neu("S4", "M6", "schriftlich_geteilt", 2, "umkehr", "zahl",
    {"text": "Ohne zu teilen: Wie viele Stellen hat das Ergebnis von 7 344 : 24?"},
    {"wert": 3}, "Vergleiche 7 344 mit 24 · 100 und mit 24 · 1 000.",
    "24 · 100 = 2 400 ist kleiner als 7 344, 24 · 1 000 = 24 000 ist größer. Das Ergebnis liegt zwischen 100 und 1 000: drei Stellen. (Genau: 306.)",
    "7 344 : 24 = 306, drei Stellen.", "Schranken: 2 400 ≤ 7 344 < 24 000, also 100 ≤ Ergebnis < 1 000.",
    "2 – zählt die Stellen von 7 344 minus die Stellen von 24", c="3")

# ───────────── Prüfungen über alle 20 Aufgaben ─────────────
assert len(AUFGABEN) == 20
STUFE = {"direkt": 1, "erkennen": 1, "mehrschritt": 2, "einkleidung": 2, "umkehr": 2, "darstellung": 2,
         "rueckwaerts": 3, "verknuepfen": 3, "begruenden": 3, "fehler": 3, "transfer": 3, "parameter": 3, "pruefung": 3}
fehler_liste, warn_liste = [], []
for a in AUFGABEN:
    assert STUFE[a["g"]] == a["s"], a["nr"]
    assert a["y"] in ip.TYPEN, a["nr"]                                                  # nur vorhandene Antwortformen
    ip.pruefe_antwort(a["nr"], a, fehler_liste.append, warn_liste.append)               # Antwortform-Prüfung des Repos
    if a["y"] == "auswahl":
        assert a["a"][a["o"]["index"]] not in a["h"]
    for wort in ([str(x) for x in a["o"].get("werte", [])] + ([str(a["o"]["wert"])] if "wert" in a["o"] and a["o"]["wert"] > 9 else [])):
        assert not re.search(rf"(?<![\d ]){re.escape(wort)}(?![\d ])", a["h"].replace(" ", "")), (a["nr"], "Tipp verrät die Lösung")
assert not fehler_liste, fehler_liste
bau = [re.sub(r"\d+", "#", a["f"]["text"] + a["f"].get("schablone", "")) for a in AUFGABEN]
assert max(bau.count(b) for b in bau) <= 2
je_etappe = {}
for a in AUFGABEN:
    je_etappe.setdefault(a["l"], []).append(a["nr"])
# richtige Auswahl steht nicht immer an derselben Stelle
idx = [a["o"]["index"] for a in AUFGABEN if a["y"] == "auswahl"]
assert len(set(idx)) >= 3, idx


def ersetze_block(name, marke, inhalt):
    pfad = os.path.join(ORDNER, name)
    if not os.path.exists(pfad):
        return False
    alt = open(pfad, encoding="utf-8").read()
    an, en = f"<!-- {marke}:ANFANG -->", f"<!-- {marke}:ENDE -->"
    if an not in alt or en not in alt:
        return False
    open(pfad, "w", encoding="utf-8").write(alt[:alt.index(an) + len(an)] + "\n" + inhalt + "\n" + alt[alt.index(en):])
    return True


with open(os.path.join(ORDNER, "aufgaben-auftrag3.json"), "w", encoding="utf-8") as fh:
    fh.write(json.dumps(AUFGABEN, ensure_ascii=False, indent=1) + "\n")

FORM = {"auswahl": "`auswahl`", "luecken": "`luecken`", "markierung": "`markierung`", "zahl": "`zahl`"}
zeilen = []
for l, nrn in je_etappe.items():
    zeilen.append(f"### Etappe `{l}`\n")
    for a in (x for x in AUFGABEN if x["l"] == l):
        f, o = a["f"], a["o"]
        stufe = {1: "leicht", 2: "mittel", 3: "schwer"}[a["s"]]
        zeilen.append(f"**{a['nr']} · Muster {a['muster']} · {stufe} (`{a['g']}`) · {FORM[a['y']]}"
                      + (" + `tabelle`" if f.get("grafik", {}).get("typ") == "tabelle" else "") + "**  ")
        zeilen.append(f"Text: „{f['text']}“" + (f" `{f['schablone']}`" if "schablone" in f else "") + "  ")
        if f.get("grafik", {}).get("typ") == "tabelle":
            zeilen.append("Tabelle: " + " · ".join(f"{z[0]}: {z[1]}" for z in f["grafik"]["zeilen"]) + "  ")
        if f.get("grafik", {}).get("typ") == "zahlenstrahl":
            gg = f["grafik"]
            zeilen.append(f"Zahlenstrahl: {gg['start']} bis " + f"{gg['ende']:,}".replace(",", " ") + f" in {gg['abschnitte']} Abschnitten, nur Anfang und Ende beschriftet  ")
        if a["y"] == "auswahl":
            zeilen.append("Auswahl: " + " | ".join(f"**{t}**" if i == o["index"] else t for i, t in enumerate(a["a"])) + "  ")
        elif a["y"] == "luecken":
            zeilen.append("Lösung: " + "; ".join(f"{v:,}".replace(",", " ") for v in o["werte"]) + "  ")
        elif a["y"] == "markierung":
            zeilen.append(f"Lösung: Strich {o['index']}  ")
        else:
            zeilen.append(f"Lösung: {o['wert']:,}".replace(",", " ") + (f" (Toleranz ± {o['toleranz']})" if "toleranz" in o else "") + "  ")
        zeilen.append(f"Weg 1: {a['probe']['weg1']}  ")
        zeilen.append(f"Weg 2: {a['probe']['weg2']}  ")
        zeilen.append(f"Häufigste falsche Antwort (Annahme): {a['falsch']}  ")
        zeilen.append(f"Tipp: {a['h']}\n")
md_ok = ersetze_block("auftrag3.md", "AUFGABEN", "\n".join(zeilen))

print(f"OK: {len(AUFGABEN)} Weg-Aufgaben zweifach nachgerechnet, Antwortform-Prüfung des Repos ohne Fehler"
      f" ({len(warn_liste)} Hinweise).")
print("je Etappe:", {k: len(v) for k, v in je_etappe.items()})
print("Formen:", {y: sum(1 for a in AUFGABEN if a["y"] == y) for y in FORM})
print(f"geschrieben: aufgaben-auftrag3.json, auftrag3.md {'aktualisiert' if md_ok else '(nicht gefunden)'}")
