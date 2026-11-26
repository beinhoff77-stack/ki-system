"""Mathe-Profi, Denkpapier Diagnose: Lassen sich typische falsche Ergebnisse je Aufgabenmuster mitberechnen?

Aufruf: python3 -I inhalte/mathe-profi/fehlbild_probe.py

Nimmt aus den Themen-Dateien die Zahl-Aufgaben, deren Rechenausdruck `c` ein einfaches Muster hat, berechnet je Denkfehler
das Ergebnis, das dieser Denkfehler liefert, und zählt: Bei wie vielen Aufgaben ist ein Fehlbild eindeutig (anders als die
richtige Lösung und anders als jedes andere Fehlbild)? Liest nur Inhalte, keine Lerndaten.
"""
import json
import os
import re
from collections import Counter
from fractions import Fraction as F

WURZEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "themen")
Z = r"\(?(-?\d+(?:\.\d+)?)\)?"


def lade(thema, etappen):
    d = json.load(open(os.path.join(WURZEL, thema + ".json"), encoding="utf-8"))
    return [a for a in d["aufgaben"] if a["l"] in etappen and a["y"] == "zahl" and isinstance(a.get("c"), str)]


def ganz(a):
    m = re.fullmatch(rf"{Z} ([+-]) {Z}", a["c"])
    if not m:
        return None
    x, op, y = int(m.group(1)), m.group(2), int(m.group(3))
    r = x + y if op == "+" else x - y
    b = {}
    if op == "+" and x * y < 0:                       # verschiedene Vorzeichen
        b["Beträge addiert, Minus davor"] = -(abs(x) + abs(y))
        b["Beträge addiert, Minus vergessen"] = abs(x) + abs(y)
        b["Unterschied richtig, Vorzeichen der ersten Zahl"] = (1 if x > 0 else -1) * abs(abs(x) - abs(y))
    if op == "+" and x < 0 and y < 0:
        b["Minus und Minus gibt Plus"] = abs(x) + abs(y)
        b["Beträge abgezogen"] = -abs(abs(x) - abs(y))
    if op == "-" and y < 0:
        b["Minus-Minus übersehen (abgezogen statt dazugezählt)"] = x - abs(y)
        if x < 0:
            b["Beträge addiert, Minus davor"] = -(abs(x) + abs(y))
    if op == "-" and y > 0 and x < 0:
        b["Minus und Minus gibt Plus"] = abs(x) + y
        b["Beträge abgezogen (Unterschied statt weiter nach links)"] = -abs(abs(x) - y)
    if op == "-" and y > 0 and 0 <= x < y:
        b["Größere minus kleinere, Minus vergessen"] = y - x
    return r, {k: v for k, v in b.items() if v != r}


def prozent(a):
    c = a["c"]
    for muster, art in ((rf"{Z} \* {Z} / 100", "W"), (rf"{Z} / {Z} \* 100", "G"), (rf"{Z} / \({Z} / 100\)", "G"),
                        (rf"{Z} \* \(100 ([+-]) {Z}\) / 100", "N")):
        m = re.fullmatch(muster, c)
        if not m:
            continue
        if art == "W":
            g, p = F(m.group(1)), F(m.group(2)); r = g * p / 100
            b = {"durch den Prozentsatz geteilt": g / p, "durch 100 vergessen": g * p, "Komma: durch 10 statt 100": g * p / 10,
                 "Prozent als Einheit abgezogen": g - p, "Formel für den Grundwert": g * 100 / p}
        elif art == "G":
            w, p = F(m.group(1)), F(m.group(2)); r = w * 100 / p
            b = {"Prozentwert gerechnet (das Ganze wird kleiner)": w * p / 100, "nur durch den Prozentsatz geteilt": w / p,
                 "mal Prozentsatz ohne durch 100": w * p, "Prozent dazugezählt": w + p}
        else:
            g, vz, p = F(m.group(1)), m.group(2), F(m.group(3)); s = 1 if vz == "+" else -1
            r = g * (100 + s * p) / 100
            b = {"nur die Änderung angegeben": g * p / 100, "Prozent als Euro gerechnet": g + s * p, "falsche Richtung": g * (100 - s * p) / 100,
                 "durch 100 vergessen": g + s * g * p}
        return r, {k: v for k, v in b.items() if v != r}
    return None


def zaehle(titel, aufgaben, regel):
    n = eindeutig = kein = gleich = 0
    je = Counter()
    for a in aufgaben:
        erg = regel(a)
        if erg is None:
            continue
        r, b = erg
        assert F(str(a["o"]["wert"])) == r, (a["c"], a["o"], r)            # Muster richtig gelesen: Lösung stimmt
        n += 1
        if not b:
            kein += 1
            continue
        haeuf = Counter(b.values())
        klar = [k for k, v in b.items() if haeuf[v] == 1]
        eindeutig += bool(klar)
        gleich += any(v > 1 for v in haeuf.values())
        je.update(klar)
    print(f"{titel}: {n} Aufgaben mit lesbarem Muster (von {len(aufgaben)} Zahl-Aufgaben mit c)")
    print(f"  mindestens ein eindeutiges Fehlbild: {eindeutig} · zwei Denkfehler mit gleichem Ergebnis: {gleich} · kein Fehlbild: {kein}")
    for k, v in je.most_common():
        print(f"    {v:3d} × eindeutig: {k}")
    return n, eindeutig, gleich, kein


a = zaehle("Ganze Zahlen (addieren, subtrahieren)", lade("zahlen.ganz", ("addieren", "subtrahieren")), ganz)
b = zaehle("Prozent (Prozentwert, Grundwert, Rabatt/Aufschlag)", lade("bruch.prozent", ("prozentwert", "grundwert", "rabatt_aufschlag")), prozent)
assert a[0] >= 40 and b[0] >= 60
# Beispiel aus dem Papier: (−7) + 4
r, fb = ganz({"c": "(-7) + (4)"})
assert r == -3 and fb == {"Beträge addiert, Minus davor": -11, "Beträge addiert, Minus vergessen": 11}
# Beispiel Klasse 8 aus dem Papier: 5x − (3x − 2) → richtig 2x + 2; Fehlbilder
assert (5 - 3, -(-2)) == (2, 2) and (5 - 3, -2) == (2, -2) and (5 + 3, 2) == (8, 2)
# Klasse 8, Gleichung 5x − (3x − 2) = 12: zwei verschiedene Denkfehler, dasselbe falsche Ergebnis
richtig = F(12 - 2, 5 - 3)                      # 2x + 2 = 12
klammer = F(12 + 2, 5 - 3)                      # Fehler in der Minusklammer: 2x − 2 = 12
umformen = F(12 + 2, 5 - 3)                     # Klammer richtig, dann 2x = 12 + 2 statt 12 − 2
assert (richtig, klammer, umformen) == (5, 7, 7)
assert 5 * 5 - (3 * 5 - 2) == 12 and 5 * 7 - (3 * 7 - 2) == 16
# Kontrollzahlen nach dem Auflösen der Klammer (□x + □ = 12) trennen die beiden: (2, −2) gegen (2, 2)
assert (5 - 3, -2) != (5 - 3, 2)
print("OK")
