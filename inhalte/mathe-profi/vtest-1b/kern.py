"""Gemeinsamer Kern für vtest-1b (Kürzel VT1B, Runde „Verstehen in Tests“, Teil 1b): Bausteine zum Schreiben der Aufgaben.
Die Themen-Dateien th_*.py rufen neu(...) auf; bauen.py prüft und schreibt die JSON-Dateien. Format wie rollend-15 (Fehlbilder als Rechnung),
dazu Felder pool, typ (= Aufgabentyp g), form, lehrplan, ersetzt_test. Keine Tipps (h), keine Toleranz."""
import itertools
import os
import sys
from fractions import Fraction as F

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
sys.path.insert(0, os.path.join(WURZEL, "tools"))
import inhalt_pruefen as ip      # noqa: E402

G2 = ("mehrschritt", "einkleidung", "umkehr", "darstellung")
G3 = ("rueckwaerts", "verknuepfen", "begruenden", "fehler", "transfer", "parameter", "pruefung")
FORMEN = ("anwenden", "umkehren", "verfahren_waehlen", "fehler_detektiv", "bruecke", "zwei_wege", "viele_antworten")
POOLS = ("test", "korrektur", "sicherung")
A = []
ABG = {}      # (Einheit, Lernziel) -> Satz „was ist anders als in den Übungen“
POSITION4 = itertools.cycle([2, 0, 3, 1, 1, 3, 0, 2, 3, 1, 0, 2])


def Z(text, wert, c, zweit, w, fb, einheit=None):
    """Zahl. c: Rechenausdruck (exakt, für inhalt_pruefen); zweit: unabhängige zweite Rechnung (Ausdruck als Text oder Zahl).
    fb: [(falscher Wert, Beschreibung, Rechnung)]: die Rechnung ist ein Ausdruck, der genau den falschen Wert ergibt."""
    o = {"wert": wert}
    if einheit:
        o["einheit"] = einheit
    return {"y": "zahl", "f": {"text": text}, "o": o, "c": c, "w": w}, [zweit], fb


def L(text, schablone, werte, c, zweit, w, fb=None, hinweis="Je Lücke eine ganze Zahl (mit Minus, falls negativ)."):
    """Lücken (z. B. Bruch □/□ oder Zeile □ und Ergebnis □). c, zweit: je Lücke ein Ausdruck; fb: {Nummer der Lücke ab 0: [(Wert, Beschreibung, Rechnung)]}."""
    return {"y": "luecken", "f": {"text": text, "schablone": schablone, "hinweis": hinweis}, "o": {"werte": werte}, "c": c, "w": w}, zweit, fb or {}


def W(text, richtig, falsch, w, probe):
    """Auswahl mit genau 4 Antworten (1 richtig, 3 falsch). falsch: [(Antwort, Beschreibung des Fehlers)]. probe: Funktion, die True liefert, wenn die richtige
    Antwort wirklich stimmt und jede falsche wirklich falsch ist (im Bauskript gerechnet)."""
    assert len(falsch) == 3, text
    p = next(POSITION4)
    antworten = [f[0] for f in falsch]
    antworten.insert(p, richtig)
    fb = {}
    for i, f in enumerate(falsch):
        fb[i if i < p else i + 1] = (None, f[1])
    return {"y": "auswahl", "f": {"text": text}, "a": antworten, "o": {"index": p}, "w": w}, probe, fb


def neu(thema, lk, pool, g, bau, form=None, lp=None):
    """pool: test | korrektur | sicherung. g: Aufgabentyp (Stufe folgt daraus). form: optional (anwenden, umkehren, verfahren_waehlen, fehler_detektiv, bruecke, zwei_wege, viele_antworten)."""
    assert pool in POOLS and (g in G2 or g in G3) and (form is None or form in FORMEN), (thema, lk, pool, g, form)
    assert lp, (thema, lk, "Lehrplan-Bezug fehlt")
    aufgabe, zweit, fb = bau
    A.append(dict(thema=thema, lk=lk, pool=pool, g=g, form=form, s=ip.STUFE_VON[g], lp=lp, aufgabe=aufgabe, zweit=zweit, fb=fb, nr=len(A)))


def B(ausdruck, beschr):
    """Fehlbild mit Wert aus der Rechnung: (Wert, Beschreibung, Rechnung)."""
    v = ip.rechne(ausdruck)
    return (int(v) if v.denominator == 1 else float(v), beschr, ausdruck)


import math  # noqa: E402
MATHE = {"sqrt": math.sqrt, "pi": math.pi, "floor": math.floor, "round": round, "abs": abs, "min": min, "max": max}


def rechne_mathe(ausdruck):
    return eval(str(ausdruck), {"__builtins__": {}}, dict(MATHE))
