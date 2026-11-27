"""Gemeinsamer Kern für rollend-6 (Kürzel K6, Klasse 6): Hilfsfunktionen zum Schreiben der Aufgaben.
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

ZAHLWORT = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)(?![\w.])")


def z2(ausdruck):
    """Zweitrechnung mit exakten Brüchen (Ausdruck als Text)."""
    if "round(" in str(ausdruck):
        return F(ip.rechne(ausdruck))
    s = ZAHLWORT.sub(lambda m: f"F('{m.group(1)}')", str(ausdruck))
    return F(eval(s, {"F": F, "gcd": lambda *x: F(math.gcd(*[int(i) for i in x])), "lcm": lambda a, b: F(math.lcm(int(a), int(b))), "__builtins__": {}}, {}))


def mit(d, grafik):
    if grafik:
        d["f"]["grafik"] = grafik
    return d


def L(text, schablone, werte, c, zweit, h, w, fb=None, hinweis="Je Lücke eine ganze Zahl (mit Minus, falls negativ).", gleich_ok=False):
    """Lücken. c: ein Rechenausdruck je Lücke; {n} steht für den (richtigen) Wert der n-ten Lücke (ab 1).
    zweit: unabhängige Zweitrechnung je Lücke (ohne {n}).
    fb: {Nummer der Lücke ab 0: [(falscher Wert, Fehlbild-Kennung oder None, Beschreibung, Rechnung)]}. Rechnung: Ausdruck (darf {n} enthalten),
    Funktion, die True liefert, oder False, wenn das Fehlbild keine Rechnung ist."""
    d = {"y": "luecken", "f": {"text": text, "schablone": schablone, "hinweis": hinweis}, "o": {"werte": werte}, "c": c, "h": h, "w": w}
    if gleich_ok:
        d["_gleich_ok"] = True
    return d, zweit, fb or {}


def Z(text, wert, c, zweit, h, w, fb, einheit=None, toleranz=None):
    """Zahl. zweit: Ausdruck (Text) oder Zahl für die zweite, unabhängige Rechnung.
    fb: [(falscher Wert, Kennung oder None, Beschreibung, Rechnung)]."""
    o = {"wert": wert}
    if einheit:
        o["einheit"] = einheit
    if toleranz is not None:
        o["toleranz"] = toleranz
    return {"y": "zahl", "f": {"text": text}, "o": o, "c": c, "h": h, "w": w}, [zweit] if isinstance(zweit, (str, int, float)) else zweit, fb


def W(text, richtig, falsch, h, w, probe):
    """Auswahl. falsch: [(Antwort, Beschreibung, Kennung=None, Rechnung=None)]. Rechnung: Ausdruck, dessen Wert die (Zahl-)Antwort ist.
    probe: Funktion, die True liefert, wenn die richtige Antwort stimmt und die anderen nicht."""
    n = len(falsch) + 1
    assert n in (3, 4), text
    p = next(POSITION[n])
    antworten = [f[0] for f in falsch]
    antworten.insert(p, richtig)
    fb = {}
    for i, f in enumerate(falsch):
        fb[i if i < p else i + 1] = (f[2] if len(f) > 2 else None, f[1], f[3] if len(f) > 3 else None)
    return {"y": "auswahl", "f": {"text": text}, "a": antworten, "o": {"index": p}, "h": h, "w": w}, probe, fb


def FD(einleitung, zeilen, h, w, frage="In welcher Zeile passiert der erste Fehler?"):
    """Fehler-Detektiv. zeilen: [(Text, stimmt)] – stimmt ist ein im Programm berechneter Wahrheitswert:
    „diese Zeile folgt rechnerisch richtig aus der Zeile davor (bzw. aus der Aufgabe)“. Genau eine Zeile darf nicht stimmen."""
    assert all(isinstance(ok, bool) for _, ok in zeilen), einleitung
    falsche = [i for i, (_, ok) in enumerate(zeilen) if not ok]
    assert len(falsche) == 1 and 3 <= len(zeilen) <= 4, (einleitung, falsche)
    text = einleitung + " " + " ".join(f"Zeile {i + 1}: {t}" for i, (t, _) in enumerate(zeilen)) + " " + frage
    ant = [f"In Zeile {i + 1}" for i in range(len(zeilen))]
    fb = {i: (None, "diese Zeile ist richtig; der Fehler steckt woanders", None) for i in range(len(zeilen)) if i != falsche[0]}
    return {"y": "auswahl", "f": {"text": text}, "a": ant, "o": {"index": falsche[0]}, "h": h, "w": w}, lambda: True, fb


def neu(thema, lk, form, bau, g=None, regel="rr.bruchrechnen"):
    """form: Schlüssel aus FORM. g: Aufgabentyp (Standard je Form); die Stufe folgt aus g.
    rang: Sortierrang für die Kennungen (stabil, auch wenn g nach der Tätigkeit gesetzt wird)."""
    g = g or FORM[form][1]
    aufgabe, zweit, fb = bau
    rang = 2 if form in ("verfahren_waehlen",) else ip.STUFE_VON[g]
    A.append(dict(thema=thema, lk=lk, form=form, g=g, regel=regel, zaehlt="nein" if form == "lueckenweg" else "ja", s=ip.STUFE_VON[g], rang=rang, aufgabe=aufgabe, zweit=zweit, fb=fb))


KOMM = lambda n: "; ".join(f"{'①②③④⑤'[i]} = □" for i in range(n))
