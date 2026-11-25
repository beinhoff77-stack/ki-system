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
print("OK")
