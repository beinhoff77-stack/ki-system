"""Gemeinsame Bausteine für rollend-5 (Klasse 5, Kürzel K5). Nur Inhalte, nichts wird eingespielt.

Eine Aufgabe wird mit neu(...) angemeldet. Die Hilfsfunktionen L, Z, W, T, FDZ bauen den Aufgabenteil.
Rechnungen: c = Ausdruck für tools/inhalt_pruefen.py, zweit = zweiter, anders gebauter Weg (wird in bauen.py verglichen).
"""
import itertools
import json
import os
import sys
from fractions import Fraction as F

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
sys.path.insert(0, os.path.join(WURZEL, "tools"))
import inhalt_pruefen as ip      # noqa: E402

KENN = json.load(open(os.path.join(HIER, "..", "regeln-uebersicht", "kennungen.json"), encoding="utf-8"))["kennungen"]
REGELN = {e["kennung"]: e for e in KENN}
FEHLBILD = {f["kennung"]: e["kennung"] for e in KENN for f in e["fehlbilder"]}

# Form -> (Anzeigename, erlaubte Aufgabentypen g, Standard für zaehlt)
FORMEN = {
    "lueckenweg": ("Lückenweg", {"direkt", "erkennen"}, "nein"),
    "fehler_detektiv": ("Fehler-Detektiv", {"fehler"}, "ja"),
    "verfahren_waehlen": ("Verfahren wählen", {"mehrschritt", "erkennen", "begruenden"}, "ja"),
    "zwei_wege": ("Zwei Wege vergleichen", {"mehrschritt"}, "ja"),
    "umkehren": ("Umkehren", {"umkehr", "rueckwaerts"}, "ja"),
    "bruecke": ("Brücke", {"darstellung"}, "ja"),
    "anwenden": ("Anwenden", {"einkleidung", "transfer", "pruefung"}, "ja"),
}
ZAEHLEND = {"umkehren", "zwei_wege", "bruecke", "verfahren_waehlen", "anwenden"}

THEMEN = ["zahlen.natuerlich", "zahlen.rechengesetze", "zahlen.potenzen_basis", "zahlen.ganz", "stochastik.kombinatorik", "messen.koerper_darstellung"]
DATEI = {t: json.load(open(os.path.join(WURZEL, "inhalte", "themen", t + ".json"), encoding="utf-8")) for t in THEMEN}
KARTEN = {t: [e["lernziel"] for e in DATEI[t]["inhalt"]["etappen"]] for t in THEMEN}
TEIL = {}
for _t in THEMEN:
    for _a in DATEI[_t]["aufgaben"]:
        TEIL.setdefault((_t, _a["l"]), _a["t"])

A = []
POSITION = {3: itertools.cycle([1, 0, 2, 2, 0, 1]), 4: itertools.cycle([2, 0, 3, 1, 1, 3, 0, 2])}
K = lambda n: "; ".join(f"{'①②③④⑤'[i]} = □" for i in range(n))
GZ = "Je Lücke eine ganze Zahl (mit Minus, falls negativ)."


def neu(thema, lk, form, g, bau, regel):
    """Meldet eine Aufgabe an. bau = Ergebnis von L, Z, W, T oder FDZ."""
    assert form in FORMEN and g in FORMEN[form][1], (thema, lk, form, g)
    assert regel in REGELN, regel
    assert lk in KARTEN[thema], (thema, lk)
    aufgabe, zweit, fb = bau
    s = ip.STUFE_VON[g]
    A.append(dict(thema=thema, lk=lk, form=form, g=g, regel=regel, zaehlt=FORMEN[form][2], s=s,
                  aufgabe={"l": lk, "t": TEIL[(thema, lk)], "p": "uebung", "s": s, "g": g, **aufgabe}, zweit=zweit, fb=fb))


def wertzahl(r):
    r = F(r)
    if r.denominator == 1:
        return int(r)
    x = float(r)
    assert F(str(x)) == r, ("keine endliche Dezimalzahl", r)
    return x


def mit(d, grafik):
    if grafik:
        d["f"]["grafik"] = grafik
    return d


def L(text, c, zweit, h, w, fb=None, hinweis=GZ, grafik=None):
    """Lückenweg-Form: Lücken ①②③. c: Liste von Ausdrücken, zweit: Liste unabhängiger Ausdrücke.
    fb: {Nummer der Lücke ab 0: [(falscher Wert, Fehlbild-Kennung oder None, Beschreibung)]}"""
    werte = [wertzahl(ip.rechne(x)) for x in c]
    return mit({"y": "luecken", "f": {"text": text, "schablone": K(len(c)), "hinweis": hinweis}, "o": {"werte": werte}, "c": c, "h": h, "w": w}, grafik), zweit, fb or {}


def Z(text, c, zweit, h, w, fb, einheit=None, grafik=None):
    """Zahl. fb: [(falscher Wert, Fehlbild-Kennung oder None, Beschreibung)]"""
    wert = wertzahl(ip.rechne(c))
    return mit({"y": "zahl", "f": {"text": text}, "o": {"wert": wert, **({"einheit": einheit} if einheit else {})}, "c": c, "h": h, "w": w}, grafik), [zweit] if isinstance(zweit, str) else zweit, fb


def W(text, richtig, falsch, h, w, probe, grafik=None):
    """Auswahl. falsch: [(Antwort, Beschreibung)] oder [(Antwort, Beschreibung, Fehlbild-Kennung)]. probe: Wahrheitswert aus Python-Rechnung."""
    n = len(falsch) + 1
    assert n in (3, 4), text
    p = next(POSITION[n])
    antworten = [f[0] for f in falsch]
    antworten.insert(p, richtig)
    fb = {}
    for i, f in enumerate(falsch):
        fb[i if i < p else i + 1] = (f[2] if len(f) > 2 else None, f[1])
    return mit({"y": "auswahl", "f": {"text": text}, "a": antworten, "o": {"index": p}, "h": h, "w": w}, grafik), probe, fb


def T(text, richtig, probe, h, w, fb, grafik=None):
    """Kurze Texteingabe (römische Zahl, Zweierzahl). fb: [(falsche Eingabe, Beschreibung)]. probe: Wahrheitswert."""
    return mit({"y": "text", "f": {"text": text}, "o": {"text": richtig}, "h": h, "w": w}, grafik), probe, [(x[0], None, x[1]) for x in fb]


def FDZ(einleitung, zeilen, h, w, frage="In welcher Zeile passiert der erste Fehler?", grafik=None):
    """Fehler-Detektiv: zeilen = [(Text, stimmt)]; genau eine Zeile darf nicht stimmen (das Programm prüft es)."""
    falsche = [i for i, (_, ok) in enumerate(zeilen) if not ok]
    assert len(falsche) == 1 and 3 <= len(zeilen) <= 4, (einleitung, falsche)
    text = einleitung + " " + " ".join(f"Zeile {i + 1}: {t}" for i, (t, _) in enumerate(zeilen)) + " " + frage
    ant = [f"In Zeile {i + 1}" for i in range(len(zeilen))]
    fb = {i: (None, "diese Zeile ist richtig; der Fehler steckt woanders") for i in range(len(zeilen)) if i != falsche[0]}
    return mit({"y": "auswahl", "f": {"text": text}, "a": ant, "o": {"index": falsche[0]}, "h": h, "w": w}, grafik), True, fb


TAB = lambda kopf, *zeilen: {"typ": "tabelle", "kopf": kopf, "zeilen": [list(z) for z in zeilen]}
