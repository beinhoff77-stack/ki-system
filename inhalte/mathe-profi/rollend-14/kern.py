"""Gemeinsamer Kern für rollend-14 (Kürzel R14, dünne Einheiten auffüllen, Klassen 6 und 8): Hilfsfunktionen zum Schreiben der Aufgaben.
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
    paare = [(u, v) for u, v in zip(werte_von(a), werte_von(b)) if u is not None and v is not None]
    return len(paare) >= 4 and all(u == v for u, v in paare)


MATHE = {"sqrt": math.sqrt, "sin": lambda g: math.sin(math.radians(g)), "cos": lambda g: math.cos(math.radians(g)), "tan": lambda g: math.tan(math.radians(g)),
         "asin": lambda x: math.degrees(math.asin(x)), "acos": lambda x: math.degrees(math.acos(x)), "atan": lambda x: math.degrees(math.atan(x)),
         "pi": math.pi, "round": round, "abs": abs, "min": min, "max": max}   # Winkel immer in Grad


def rechne_mathe(ausdruck):
    """Unabhängige Zweitrechnung mit Gleitkomma (Winkelfunktionen in Grad); gibt int oder float zurück."""
    return eval(str(ausdruck), {"__builtins__": {}}, dict(MATHE))


def z2(ausdruck):
    v = rechne_mathe(ausdruck)
    return F(str(round(v, 9))) if isinstance(v, float) else F(v)


def rd(ausdruck, stellen=0):
    """(gerundeter Wert, Rechenanker) – der Anker ist für tools/inhalt_pruefen.py lesbar (round(Literal, n)). Bricht ab, wenn der Wert zu nah an einer Rundungsgrenze liegt."""
    v = float(rechne_mathe(ausdruck))
    r = v * 10 ** stellen
    assert abs((r - math.floor(r)) - 0.5) > 0.02, (ausdruck, v, "zu nah an der Rundungsgrenze")
    w = round(v, stellen)
    w = int(w) if stellen == 0 else w
    return w, f"round({v!r}, {stellen})"


# ---------- Bausteine ----------
def mit(d, grafik):
    if grafik:
        d["f"]["grafik"] = grafik
    return d


def L(text, schablone, werte, c, zweit, h, w, fb=None, hinweis="Je Lücke eine ganze Zahl (mit Minus, falls negativ).", grafik=None, gleich_ok=False):
    """Lücken. c: ein Rechenausdruck je Lücke; {n} steht für den (richtigen) Wert der n-ten Lücke (ab 1), ggT(a, b) für den größten gemeinsamen Teiler.
    bauen.py setzt die früheren Werte ein und prüft, dass spätere Lücken wirklich von früheren abhängen. zweit: unabhängige Zweitrechnung je Lücke (ohne {n}).
    fb: {Nummer der Lücke ab 0: [(falscher Wert, Fehlbild-Kennung oder None, Beschreibung, Rechnung)]}. Rechnung: Ausdruck (darf {n} enthalten),
    Funktion, die True liefert, oder False, wenn das Fehlbild keine Rechnung ist.
    gleich_ok: gleiche Lückenwerte erlaubt (nur, wenn fachlich nötig)."""
    d = mit({"y": "luecken", "f": {"text": text, "schablone": schablone, "hinweis": hinweis}, "o": {"werte": werte}, "c": c, "h": h, "w": w}, grafik)
    if gleich_ok:
        d["_gleich_ok"] = True
    return d, zweit, fb or {}


def Z(text, wert, c, zweit, h, w, fb, einheit=None, toleranz=None, grafik=None):
    """Zahl. zweit: Ausdruck (Text) oder Zahl für die zweite, unabhängige Rechnung.
    fb: [(falscher Wert, Kennung oder None, Beschreibung, Rechnung)]. Rechnung: Ausdruck, dessen Wert der falsche Wert ist (bei gerundeten Werten auf 2 Stellen gerundet),
    Funktion, die True liefert, oder False, wenn das Fehlbild keine Rechnung ist. toleranz nur, wo fachlich nötig."""
    o = {"wert": wert}
    if einheit:
        o["einheit"] = einheit
    if toleranz is not None:
        o["toleranz"] = toleranz
    return mit({"y": "zahl", "f": {"text": text}, "o": o, "c": c, "h": h, "w": w}, grafik), [zweit] if isinstance(zweit, (str, int, float)) else zweit, fb


def W(text, richtig, falsch, h, w, probe, grafik=None):
    """Auswahl. falsch: [(Antwort, Beschreibung)] oder [(Antwort, Beschreibung, Fehlbild-Kennung)]. probe: Funktion, die True liefert, wenn die richtige Antwort stimmt und die anderen nicht
    (und jede falsche Antwort wirklich aus dem beschriebenen Fehler entsteht, soweit das maschinell geht)."""
    n = len(falsch) + 1
    assert n in (3, 4), text
    p = next(POSITION[n])
    antworten = [f[0] for f in falsch]
    antworten.insert(p, richtig)
    fb = {}
    for i, f in enumerate(falsch):
        fb[i if i < p else i + 1] = (f[2] if len(f) > 2 else None, f[1])
    return mit({"y": "auswahl", "f": {"text": text}, "a": antworten, "o": {"index": p}, "h": h, "w": w}, grafik), probe, fb


def FD(einleitung, zeilen, h, w, frage="In welcher Zeile passiert der erste Fehler?", grafik=None, rueck=None):
    """Fehler-Detektiv. zeilen: [(Text, stimmt, folgt)] – beides wird im Programm berechnet:
    stimmt = die Zeile ist für sich richtig (nur bis zur Fehlerzeile maßgeblich); folgt = die Zeile folgt rechnerisch richtig aus der Zeile davor (bei Zeile 1: True).
    Verlangt: alle Zeilen vor der Fehlerzeile stimmen; die Fehlerzeile stimmt nicht (und folgt richtig aus der Zeile davor oder ist der Fehler selbst);
    jede Zeile nach der Fehlerzeile folgt richtig aus der Zeile davor (kein zweiter unabhängiger Fehler)."""
    assert 3 <= len(zeilen) <= 4, einleitung
    falsche = [i for i, z in enumerate(zeilen) if not z[1]]
    assert falsche, (einleitung, "eine Zeile muss für sich falsch sein")
    f = falsche[0]                      # erste Fehlerzeile; für Zeilen danach zählt nur, dass sie aus der Zeile davor richtig folgen
    assert all(z[2] for z in zeilen[f + 1:]), (einleitung, "Folgezeile folgt nicht richtig aus der Zeile davor")
    text = einleitung + " " + " ".join(f"Zeile {i + 1}: {z[0]}" for i, z in enumerate(zeilen)) + " " + frage
    ant = [f"In Zeile {i + 1}" for i in range(len(zeilen))]
    fb = {i: (None, "diese Zeile ist richtig; der Fehler steckt woanders" if i < f else "diese Zeile ist nur die Folge des ersten Fehlers") for i in range(len(zeilen)) if i != f}
    for i, t in (rueck or {}).items():      # Rückmeldung von Hand, wo eine Zeile nach dem Fehler unabhängig richtig oder nur teilweise Folge ist
        assert i > f, (einleitung, "rueck nur für Zeilen nach der Fehlerzeile")
        fb[i] = (None, t)
    return mit({"y": "auswahl", "f": {"text": text}, "a": ant, "o": {"index": f}, "h": h, "w": w}, grafik), lambda: True, fb


def neu(thema, lk, form, bau, g=None, regel=None, thema_datei=None):
    assert form != "lueckenweg", "Reserve: kein Lückenweg"
    """form: Schlüssel aus FORM. g: Aufgabentyp (Standard je Form); die Stufe folgt aus g.
    rang: Sortierrang für die Kennungen. Er bleibt die Stufe, die der Standard-Typ der Form hatte (Verfahren wählen: 2), damit die Kennungen K8-V… stabil bleiben,
    auch wenn g nach der tatsächlichen Tätigkeit gesetzt wird."""
    g = g or FORM[form][1]
    aufgabe, zweit, fb = bau
    rang = 2 if form == "verfahren_waehlen" else ip.STUFE_VON[g]
    A.append(dict(thema=thema, lk=lk, form=form, g=g, regel=regel, zaehlt="ja", s=ip.STUFE_VON[g], rang=rang, aufgabe=aufgabe, zweit=zweit, fb=fb))


KOMM = lambda n: "; ".join(f"{'①②③④⑤'[i]} = □" for i in range(n))
TAB = lambda kopf, *zeilen: {"typ": "tabelle", "kopf": kopf, "zeilen": [list(z) for z in zeilen]}
KO = lambda x, y, **mehr: {"typ": "koordinaten", "x": x, "y": y, **mehr}


def ist_loesung(links, rechts, wert, var="x"):
    """True, wenn die Gleichung links = rechts für var = wert stimmt (exakt)."""
    env = {"x": F(0), "y": F(0), "a": F(0), "b": F(0), "n": F(0)}
    env[var] = F(str(wert)) if not isinstance(wert, F) else wert
    return _ev(links, env) == _ev(rechts, env)


def undef(s, wert, var="x"):
    """True, wenn der Term s für var = wert nicht definiert ist (Nenner 0)."""
    env = {"x": F(1), "y": F(1), "a": F(1), "b": F(1), "n": F(1)}
    env[var] = F(str(wert))
    try:
        _ev(s, env)
        return False
    except ZeroDivisionError:
        return True


def wert_an(s, wert, var="x"):
    env = {"x": F(1), "y": F(1), "a": F(1), "b": F(1), "n": F(1)}
    env[var] = F(str(wert))
    return _ev(s, env)


def pole(*terme, bereich=range(-9, 10)):
    """Menge der ganzen Zahlen im Bereich, an denen mindestens einer der Terme nicht definiert ist."""
    return {k for k in bereich if any(undef(t, k) for t in terme)}


def loes(gleichung, var="x"):
    """Lösung einer in var linearen Gleichung 'links = rechts' (Python-Schreibweise): Bruch, 'alle' (jede Zahl) oder 'keine'."""
    l, r = gleichung.split("=")
    f = lambda v: _ev(l, {var: F(v)}) - _ev(r, {var: F(v)})
    a = f(1) - f(0)
    if a == 0:
        return "alle" if f(0) == 0 else "keine"
    return -f(0) / a


def gleichwertig(g1, g2, var="x"):
    """Zwei lineare Gleichungen haben dieselbe Lösungsmenge."""
    return loes(g1, var) == loes(g2, var)


# ---------- Runde 14: je Lernkarte drei Sachaufgaben (Stufe 2 leicht, Stufe 2 schwerer, Stufe 3) ----------
def a1(T, lk, z):
    """Stufe 2, Typ einkleidung: eine einfache Sachaufgabe."""
    neu(T, lk, "anwenden", z, g="einkleidung")


def a2(T, lk, z):
    """Stufe 2, Typ mehrschritt: eine Sachaufgabe mit mehreren Schritten."""
    neu(T, lk, "anwenden", z, g="mehrschritt")


def a3(T, lk, z, g="transfer", form="anwenden"):
    """Stufe 3 (transfer, rueckwaerts, verknuepfen, pruefung ...)."""
    assert ip.STUFE_VON[g] == 3, g
    neu(T, lk, form, z, g=g)


def B(ausdruck, beschr, kenn=None):
    """Fehlbild mit Wert aus der Rechnung: (Wert, Kennung, Beschreibung, Rechnung). Der Wert wird exakt berechnet (bauen.py prüft ihn trotzdem gegen die gespeicherte Rechnung)."""
    v = ip.rechne(ausdruck)
    return (int(v) if v.denominator == 1 else float(v), kenn, beschr, ausdruck)
