"""Mathe-Profi, Denkpapier Grundregeln: Wo kommt dieselbe Regel in den Klassen 5–8 vor?

Aufruf: python3 -I inhalte/mathe-profi/grundregeln_probe.py

Grobe Zählung über den Aufgabentext (reguläre Ausdrücke, keine Lerndaten). Zeigt nur die Größenordnung:
dieselbe Regel in mehreren Klassen, einmal mit Zahl, einmal mit Buchstabe. Dazu die Rechnungen der Brücke im Papier.
"""
import json
import os
import re
from collections import defaultdict

HIER = os.path.dirname(os.path.abspath(__file__))
THEMEN = os.path.join(HIER, "..", "themen")
liste = json.load(open(os.path.join(HIER, "..", "themenliste.json"), encoding="utf-8"))

OPERAND = r"[\dA-Za-z]"
SUMME = r"\([^()|]*" + OPERAND + r"\s*[+−-]\s*[\dA-Za-z(][^()|]*\)"      # Klammer mit echter Summe oder Differenz, keine Koordinaten
MUSTER = {
    "Minus vor negativer Zahl  a − (−b)": re.compile(r"[−-]\s*\(\s*[−-]\s*\d[\d  ]*(?:[,.]\d+)?\s*\)"),
    "Minus vor Klammer         a − (b ± c)": re.compile(r"[−-]\s*" + SUMME),
    "Faktor vor Klammer        a · (b ± c)": re.compile(r"(?:\d|·\s|(?<![A-Za-zäöüÄÖÜ])[a-z])" + SUMME),
}
BUCHSTABE = re.compile(r"(?<![a-zäöüA-ZÄÖÜ])[a-z](?![a-zäöüA-ZÄÖÜ])")
X = re.compile(r"(?<![A-Za-zäöüÄÖÜ])x(?![A-Za-zäöüÄÖÜ])")
GLEICHUNG = re.compile(r"Löse|Lösung|Gleichung")

zahl = defaultdict(lambda: defaultdict(int))        # Muster → Klasse → Aufgaben
mit_buchstabe = defaultdict(lambda: defaultdict(int))
gesamt = defaultdict(int)
x_einmal, x_mehrfach, kaestchen = defaultdict(int), defaultdict(int), defaultdict(int)
beispiele = {"4 · (□ − 12) = −20": 0, "9 − (−5)": 0}
for th in liste:
    kl = th["klasse"].get("gym_by")
    pfad = os.path.join(THEMEN, th["thema_schluessel"] + ".json")
    if kl not in (5, 6, 7, 8) or not os.path.exists(pfad):
        continue
    for a in json.load(open(pfad, encoding="utf-8"))["aufgaben"]:
        if a["p"] == "bonus":
            continue
        text = a["f"].get("text", "")
        gesamt[kl] += 1
        for b in beispiele:
            beispiele[b] += b in text
        for name, rx in MUSTER.items():
            m = rx.search(text)
            if m:
                zahl[name][kl] += 1
                if BUCHSTABE.search(m.group(0)):
                    mit_buchstabe[name][kl] += 1
        # Gleichungen: Wie oft kommt die Unbekannte in der Gleichung vor?
        stuecke = [t for t in re.split(r"[.?!:„“]\s|\s(?:und|oder)\s", text) if "=" in t]
        if "□" in text and any("□" in t for t in stuecke):
            kaestchen[kl] += 1
        elif GLEICHUNG.search(text) and stuecke:
            n = max(len(X.findall(t)) for t in stuecke)
            if n == 1:
                x_einmal[kl] += 1
            elif n > 1:
                x_mehrfach[kl] += 1

print("Aufgaben je Klasse (Gymnasium Bayern, ohne Bonus):", dict(sorted(gesamt.items())))
print(f"{'Regel im Aufgabentext':48} " + " ".join(f"Kl.{k:>2}" for k in (5, 6, 7, 8)))
for name in MUSTER:
    print(f"{name:48} " + " ".join(f"{zahl[name][k]:5d}" for k in (5, 6, 7, 8)))
    if "Klammer" in name:
        print(f"{'   davon mit Buchstabe in der Klammer':48} " + " ".join(f"{mit_buchstabe[name][k]:5d}" for k in (5, 6, 7, 8)))
for name, d in (("Gleichung mit Kästchen □", kaestchen), ("Gleichung, x kommt einmal vor", x_einmal), ("Gleichung, x kommt mehrfach vor", x_mehrfach)):
    print(f"{name:48} " + " ".join(f"{d[k]:5d}" for k in (5, 6, 7, 8)))
print("Beispiele des Nutzers im Bestand:", beispiele)

# In Klasse 5 sind die Treffer „x mehrfach“ Probe-Aufgaben, bei denen „x = 9“ zusätzlich im Satz steht.

# ── Brücke „Minus vor der Klammer“ (Abschnitt 2 im Papier) ──
assert 20 - (8 - 3) == 15 == 20 - 8 + 3 and 20 - 8 - 3 == 9                      # Stufe 1: nachrechnen
assert 9 - (-5) == 14 and 20 - (8 + (-3)) == 15                                   # Stufe 2: negative Zahl
assert 78 - (49 - 22) == 78 - 49 + 22 == 51 and 3.5 - (1.2 - 0.7) == 3.0 == 3.5 - 1.2 + 0.7                                       # Stufe 3: Lücke 22, ohne auszurechnen
for k in (1, 2, 3, 7):                                                            # Stufe 4: Kästchen kommt zweimal vor
    assert 5 * k - (3 * k - 2) == 2 * k + 2
assert [5 * k - (3 * k - 2) for k in (1, 2, 3)] == [4, 6, 8]
x = 3                                                                             # Stufe 5: Zahlenprobe entlarvt die Fehlbilder
assert 5 * x - (3 * x - 2) == 8 == 2 * x + 2 and 2 * x - 2 == 4 and 8 * x + 2 == 26
assert 5 * 0 - (3 * 0 - 2) == 2 == 8 * 0 + 2                                      # Probe mit x = 0 übersieht das Fehlbild 8x + 2
assert (1 + 4) ** 2 == 25 != 1 + 16 and 1 ** 2 == 1 * 1 == 1                        # Probe mit x = 1 übersieht x² statt x
assert 5 * 5 - (3 * 5 - 2) == 12                                                  # Stufe 6: Gleichung, x = 5
# Kästchen einmal: rückwärts rechnen geht. 4 · (□ − 12) = −20
assert -20 // 4 == -5 and -5 + 12 == 7 and 4 * (7 - 12) == -20
# Kästchen zweimal: rückwärts geht nicht mehr – es gibt keine Kette von Umkehrschritten, erst umformen
assert (12 - 2) / (5 - 3) == 5

# ── Beispiele der Regel-Liste (Abschnitt 1 im Papier): Zahlen, x (an Stichproben), Brüche ──
from fractions import Fraction as F
import statistics
X_WERTE = (2, 3, -4, F(1, 2))                                                     # nie 0 oder 1
gleich = lambda f, g: all(f(x) == g(x) for x in X_WERTE)
# 1 Richtung
assert (-7) + 4 == -3 and 9 - (-5) == 14 and gleich(lambda x: 3 * x - 5 * x, lambda x: -2 * x) and F(1, 4) - F(3, 4) == F(-1, 2)
# 2 Zeichen-Paar
assert (-3) * (-4) == 12 and gleich(lambda x: (-2 * x) * (-3), lambda x: 6 * x) and F(-1, 2) * F(2, 3) == F(-1, 3) and (-5) + (-3) != 8
# 3 Rangfolge
assert 2 + 3 * 4 == 14 != 20 and not gleich(lambda x: 2 + 3 * x, lambda x: 5 * x) and F(1, 2) + F(1, 2) * F(1, 3) == F(2, 3)
# 4 Verteilen
assert 6 * 18 == 6 * 20 - 6 * 2 == 108 and gleich(lambda x: 3 * (x + 2), lambda x: 3 * x + 6) and gleich(lambda x: 6 * x + 9, lambda x: 3 * (2 * x + 3))
assert F(1, 2) * (4 + F(2, 3)) == 2 + F(1, 3) and not gleich(lambda x: (x + 4) ** 2, lambda x: x ** 2 + 16)
# 5 Minusklammer
assert gleich(lambda x: 5 * x - (3 * x - 2), lambda x: 2 * x + 2) and 1 - (F(1, 2) - F(1, 4)) == 1 - F(1, 2) + F(1, 4) == F(3, 4)
# 6 Tauschen und Bündeln
assert 4 * 17 * 25 == 100 * 17 and gleich(lambda x: 3 * x + 5 + 2 * x, lambda x: 5 * x + 5) and not gleich(lambda x: 3 * x + 5 + 2 * x, lambda x: 10 * x)
assert F(1, 3) + F(5, 7) + F(2, 3) == 1 + F(5, 7) and 8 - 3 != 3 - 8
# 7 Waage
assert -4 + 7 == 3 and 2 * 5 + 2 == 12 and F(3, 2) / 3 == F(1, 2)
# 8 Umkehren
assert 4 * (7 - 12) == -20 and 7 ** 2 == (-7) ** 2 == 49 and 6 * F(2, 3) == 4 == 4 / F(2, 3) * F(2, 3)
# 9 Einsetzen und Probe
assert 5 * 3 - (3 * 3 - 2) == 8 == 2 * 3 + 2 and 4 * F(1, 2) + 1 == 3
# 10 Wert bleibt
assert F(12, 18) == F(2, 3) == F(4, 6) and gleich(lambda x: F(6 * x) / (9 * x), lambda x: F(2, 3))
assert gleich(lambda x: F(3 * x + 6) / 3, lambda x: x + 2) and not gleich(lambda x: F(3 * x + 6) / 3, lambda x: 3 * x + 2) and F(12 + 6, 3) == 6 != 4 + 6
# 11 Bruchrechnen
assert F(1, 2) + F(1, 3) == F(5, 6) and 6 / F(1, 2) == 12 and gleich(lambda x: F(1) / x + F(2) / x, lambda x: F(3) / x) and gleich(lambda x: F(x) / 2 + F(x) / 3, lambda x: F(5 * x, 6))
# 12 Potenz
assert 2 ** 3 * 2 ** 2 == 2 ** 5 == 32 and gleich(lambda x: x ** 2 * x ** 3, lambda x: x ** 5) and not gleich(lambda x: x * x, lambda x: 2 * x) and F(2, 3) ** 2 == F(4, 9)
# 13 Stellenwert und Prozent
assert F(15, 100) * 240 == 36 and gleich(lambda x: F(12, 10) * x, lambda x: x + F(20, 100) * x) and F(3, 4) == F(75, 100)
# 14 Verhältnis
assert F(750, 100) / 3 == F(5, 2) and F(2, 3) == F(8, 12)
# 15 Nullprodukt
assert all((x - 2) * (x + 3) == 0 for x in (2, -3)) and (F(1, 2) - F(1, 2)) * F(1, 2) == 0 and 3 * 4 == 12 != 0
# Beispiel Klasse 8 (Abschnitt 3): aus Summen kürzen – an Zahlen nachrechenbar
assert F(12 + 6, 3) == 6 and 12 // 3 + 6 == 10 and (3 * 2 + 6) // 3 == 4 == 2 + 2 and 2 + 6 == 8 and 3 * 2 + 2 == 8
# Flug-Umfang (Abschnitt 6)
et, ue = [], []
for th in liste:
    pfad = os.path.join(THEMEN, th["thema_schluessel"] + ".json")
    if th["klasse"].get("gym_by") in (5, 6, 7, 8) and os.path.exists(pfad):
        d = json.load(open(pfad, encoding="utf-8"))
        et.append(len(d["inhalt"]["etappen"])); ue.append(sum(1 for a in d["aufgaben"] if a["p"] == "uebung"))
print(f"Flüge Klasse 5–8: {len(et)}, Etappen je Flug im Median {statistics.median(et):.0f} ({min(et)}–{max(et)}), Übungen im Median {statistics.median(ue):.0f}")
print("OK")
