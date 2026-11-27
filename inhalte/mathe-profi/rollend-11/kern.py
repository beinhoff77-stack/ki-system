"""Gemeinsamer Kern für rollend-11 (Kürzel S3): Bausteine zum Schreiben der Stufe-3-Aufgaben.
Die Dateien th_*.py rufen Z, W oder FD auf; bauen.py prüft alles und schreibt die JSON-Dateien."""
import os
import sys
from fractions import Fraction as F

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
sys.path.insert(0, os.path.join(WURZEL, "tools"))
import inhalt_pruefen as ip      # noqa: E402

# Form -> (Name wie in tools/rollend_sql.py, Standard-g auf Stufe 3)
FORM = {
    "fehler_detektiv": ("Fehler-Detektiv (einfache Form)", "fehler"),
    "umkehren": ("Umkehren", "rueckwaerts"),
    "zwei_wege": ("Zwei Wege vergleichen", "verknuepfen"),
    "bruecke": ("Brücke", "verknuepfen"),
    "anwenden": ("Anwenden", "transfer"),
}
A = []


def _neu(thema, lk, form, g, regel, kern):
    g = g or FORM[form][1]
    assert form in FORM and ip.STUFE_VON[g] == 3, (thema, lk, form, g)
    A.append(dict(thema=thema, lk=lk, form=form, g=g, regel=regel, **kern))


def Z(thema, lk, form, text, wert, c, zweit, h, w, fb, regel, einheit=None, g=None, grafik=None):
    """Zahlantwort. c: Rechenausdruck (tools/inhalt_pruefen.py), zweit: zweiter, anders gebauter Ausdruck.
    fb: [(falsche Antwort, Rechnung als Ausdruck oder None, Beschreibung)] – die Rechnung muss die falsche Antwort ergeben."""
    _neu(thema, lk, form, g, regel, dict(y="zahl", text=text, wert=wert, c=c, zweit=zweit, h=h, w=w, fb=fb, einheit=einheit, grafik=grafik))


def W(thema, lk, form, text, antworten, richtig, wahr, h, w, fb, regel, werte=None, g=None, grafik=None):
    """Auswahl. wahr: je Antwort ein Wahrheitswert (im Programm berechnet, genau einer True, an der Stelle richtig).
    fb: {Nummer der falschen Antwort: (Beschreibung, Rechnung oder None)}. werte: Zahlenwert je Antwort, wenn die Antworten Zahlen sind (dann wird die Rechnung geprüft)."""
    _neu(thema, lk, form, g, regel, dict(y="auswahl", text=text, a=antworten, richtig=richtig, wahr=wahr, h=h, w=w, fb=fb, werte=werte, grafik=grafik))


def FD(thema, lk, einleitung, zeilen, h, w, regel, fb_text, g=None):
    """Fehler-Detektiv. zeilen: [(Text, stimmt)]. stimmt wird im Programm berechnet (True/False aus einer Python-Rechnung):
    vor der Fehlerzeile True, Fehlerzeile False, danach True (die Folgezeile rechnet mit dem Fehler richtig weiter).
    fb_text: Beschreibung des Fehlers in der Fehlerzeile (für die Rückmeldung)."""
    _neu(thema, lk, "fehler_detektiv", g, regel, dict(y="fd", einleitung=einleitung, zeilen=zeilen, h=h, w=w, fb_text=fb_text))


# ---------- Termgleichheit (exakt, an mehreren Stellen) ----------
PUNKTE = [dict(x=F(2), y=F(3), a=F(5), b=F(7), n=F(4)), dict(x=F(-3), y=F(5), a=F(-2), b=F(3), n=F(6)), dict(x=F(7), y=F(-4), a=F(3), b=F(-5), n=F(2)),
          dict(x=F(1, 2), y=F(2), a=F(11), b=F(2), n=F(5)), dict(x=F(5), y=F(7), a=F(-7), b=F(-3), n=F(3)), dict(x=F(-6), y=F(-1), a=F(1, 3), b=F(9), n=F(7))]


def _ev(s, env):
    import re
    s2 = re.sub(r"(?<![\w.])(\d+(?:\.\d+)?)(?![\w.])", lambda m: f"F('{m.group(1)}')", s)
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
    """Zwei Terme (Python-Schreibweise, Variablen x y a b n) stimmen an sechs Prüfpunkten überein (Punkte mit Nenner 0 in beiden Termen zählen nicht)."""
    wa, wb = werte_von(a), werte_von(b)
    return wa == wb and any(v is not None for v in wa)
