"""Gemeinsamer Kern für rollend-7 (Kürzel K8): Hilfsfunktionen zum Schreiben der Aufgaben.
Die Themen-Dateien th_*.py rufen neu(...) auf; bauen.py prüft und schreibt die JSON-Dateien."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
sys.path.insert(0, os.path.join(WURZEL, "tools"))
import inhalt_pruefen as ip      # noqa: E402

# Form -> (Name wie in tools/rollend_sql.py FORM, Standard-g)
FORM = {
    "lueckenweg": ("Lückenweg", "direkt"),
    "fehler_detektiv": ("Fehler-Detektiv (einfache Form)", "fehler"),
    "verfahren_waehlen": ("Verfahren wählen (einfache Form)", "mehrschritt"),
    "zwei_wege": ("Zwei Wege vergleichen", "mehrschritt"),
    "umkehren": ("Umkehren", "umkehr"),
    "bruecke": ("Brücke", "darstellung"),
    "anwenden": ("Anwenden", "einkleidung"),
}
A = []
POSITION = {3: itertools.cycle([1, 0, 2, 2, 0, 1]), 4: itertools.cycle([2, 0, 3, 1, 1, 3, 0, 2])}
PI = math.pi

# ---------- exaktes Nachrechnen von Termen (Brüche statt Kommazahlen) ----------
PUNKTE = [dict(x=F(2), y=F(3), a=F(5), b=F(7), n=F(4)), dict(x=F(-3), y=F(5), a=F(-2), b=F(3), n=F(6)), dict(x=F(7), y=F(-4), a=F(3), b=F(-5), n=F(2)),
          dict(x=F(1, 2), y=F(2), a=F(11), b=F(2), n=F(5)), dict(x=F(5), y=F(7), a=F(-7), b=F(-3), n=F(3)), dict(x=F(-6), y=F(-1), a=F(1, 3), b=F(9), n=F(7))]
ZAHLWORT = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)(?![\w.])")


def _ev(s, env):
    s2 = ZAHLWORT.sub(lambda m: f"F('{m.group(1)}')", s)
    return eval(s2, {"F": F, "__builtins__": {}}, dict(env))


def werte_von(s):
    r = []
    for p in PUNKTE:
        try:
            r.append(_ev(s, p))
        except ZeroDivisionError:
            r.append(None)
    return r


def gl(a, b):
    """Zwei Terme (Python-Schreibweise, Variablen x y a b n) stimmen an sechs Prüfpunkten überein (und sind überall definiert, wo einer es ist)."""
    wa, wb = werte_von(a), werte_von(b)
    return sum(1 for u in wa if u is not None) >= 4 and wa == wb


def z2(ausdruck):
    return F(_ev(ausdruck, {}))


# ---------- Bausteine ----------
def mit(d, grafik):
    if grafik:
        d["f"]["grafik"] = grafik
    return d


def L(text, schablone, werte, c, zweit, h, w, fb=None, hinweis="Je Lücke eine ganze Zahl (mit Minus, falls negativ).", grafik=None):
    """Lücken. fb: {Nummer der Lücke ab 0: [(falscher Wert, Fehlbild-Kennung oder None, Beschreibung)]}"""
    return mit({"y": "luecken", "f": {"text": text, "schablone": schablone, "hinweis": hinweis}, "o": {"werte": werte}, "c": c, "h": h, "w": w}, grafik), zweit, fb or {}


def Z(text, wert, c, zweit, h, w, fb, einheit=None, toleranz=None, grafik=None):
    """Zahl. zweit: Ausdruck (Text) oder Zahl für die zweite, unabhängige Rechnung. fb: [(falscher Wert, Kennung oder None, Beschreibung)]"""
    o = {"wert": wert}
    if einheit:
        o["einheit"] = einheit
    if toleranz is not None:
        o["toleranz"] = toleranz
    return mit({"y": "zahl", "f": {"text": text}, "o": o, "c": c, "h": h, "w": w}, grafik), [zweit] if isinstance(zweit, (str, int, float)) else zweit, fb


def W(text, richtig, falsch, h, w, probe, grafik=None):
    """Auswahl. falsch: [(Antwort, Beschreibung)] oder [(Antwort, Beschreibung, Fehlbild-Kennung)]. probe: Funktion, die True liefert, wenn die richtige Antwort stimmt und die anderen nicht."""
    n = len(falsch) + 1
    assert n in (3, 4), text
    p = next(POSITION[n])
    antworten = [f[0] for f in falsch]
    antworten.insert(p, richtig)
    fb = {}
    for i, f in enumerate(falsch):
        fb[i if i < p else i + 1] = (f[2] if len(f) > 2 else None, f[1])
    return mit({"y": "auswahl", "f": {"text": text}, "a": antworten, "o": {"index": p}, "h": h, "w": w}, grafik), probe, fb


def FD(einleitung, zeilen, h, w, frage="In welcher Zeile steckt der Fehler?", grafik=None):
    """Fehler-Detektiv. zeilen: [(Text, stimmt)] – stimmt wird im Programm berechnet; genau eine Zeile darf nicht stimmen."""
    falsche = [i for i, (_, ok) in enumerate(zeilen) if not ok]
    assert len(falsche) == 1 and 3 <= len(zeilen) <= 4, (einleitung, falsche)
    text = einleitung + " " + " ".join(f"Zeile {i + 1}: {t}" for i, (t, _) in enumerate(zeilen)) + " " + frage
    ant = [f"In Zeile {i + 1}" for i in range(len(zeilen))]
    fb = {i: (None, "diese Zeile ist richtig; der Fehler steckt woanders") for i in range(len(zeilen)) if i != falsche[0]}
    return mit({"y": "auswahl", "f": {"text": text}, "a": ant, "o": {"index": falsche[0]}, "h": h, "w": w}, grafik), lambda: True, fb


def neu(thema, lk, form, bau, g=None, regel="rr.waage", thema_datei=None):
    """form: Schlüssel aus FORM. g: Aufgabentyp (Standard je Form); die Stufe folgt aus g."""
    g = g or FORM[form][1]
    aufgabe, zweit, fb = bau
    A.append(dict(thema=thema, lk=lk, form=form, g=g, regel=regel, zaehlt="nein" if form == "lueckenweg" else "ja", s=ip.STUFE_VON[g], aufgabe=aufgabe, zweit=zweit, fb=fb))


KOMM = lambda n: "; ".join(f"{'①②③④⑤'[i]} = □" for i in range(n))
TAB = lambda kopf, *zeilen: {"typ": "tabelle", "kopf": kopf, "zeilen": [list(z) for z in zeilen]}
KO = lambda x, y, **mehr: {"typ": "koordinaten", "x": x, "y": y, **mehr}
