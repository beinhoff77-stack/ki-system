"""Mathe-Profi, Auftrag 19: Nachtrag zum Papier-Test 1 – je 6 Aufgaben zu Potenzen (Klasse 5) und binomischen Formeln (Klasse 8).

Aufruf: python3 -I inhalte/mathe-profi/papier-test-1/nachtrag.py
Rechnet jede Lösung nach (Potenzen direkt; binomische Formeln durch Einsetzen von 49 Zahlenpaaren in beide Seiten) und schreibt nachtrag.md.
Nur Inhalt für einen späteren Papier-Test. Nichts wird eingespielt.
"""
import os
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))
P = [F(n, d) for n in (-3, -2, -1, 0, 1, 2, 5) for d in (1,)]
gleich = lambda l, r: all(l(x, y) == r(x, y) for x in P for y in P)

# ---------- Klasse 5: Potenzen ----------
assert 2 * 2 * 2 * 2 * 2 == 2 ** 5 == 32
assert 3 ** 4 == 81 and (-2) ** 5 == -32
assert 4 * 10 ** 5 == 400000 and 7 * 10 ** 4 == 70000
assert 13 ** 2 == 169 and 2 ** 6 == 64
assert 2 ** 5 == 32 != 10 and (-3) ** 2 == 9
assert 2 ** 5 == 32 > 5 ** 2 == 25
K5 = [
    (1, "1", "Schreibe als Potenz und rechne aus: 2 · 2 · 2 · 2 · 2", 1, "2⁵ = 32", "Potenz und Wert richtig: 1 P. Nur eines von beiden: 0 P.", "Potenzen (Schreibweise)"),
    (1, "2", "Rechne aus. Schreibe die Zwischenschritte auf. a) 3⁴   b) (−2)⁵", 2, "a) 3 · 3 · 3 · 3 = 81   b) −32", "Je Teil 1 P. Bei b) +32: 0 P für b).", "Potenzen (ausrechnen, negative Basis)"),
    (1, "3", "a) Schreibe ohne Potenz: 4 · 10⁵   b) Schreibe mit einer Zehnerpotenz: 70 000", 2, "a) 400 000   b) 7 · 10⁴", "Je Teil 1 P.", "Zehnerpotenzen"),
    (2, "4", "Welche natürliche Zahl gehört in das Kästchen? a) □² = 169   b) 2 hoch □ = 64", 2, "a) 13   b) 6", "Je Teil 1 P.", "Umkehren"),
    (2, "5", "Ein Kind hat gerechnet: 2⁵ = 10 und (−3)² = −9. Berichtige beide Ergebnisse und schreibe dazu, was das Kind falsch gemacht hat.", 2,
     "2⁵ = 32 (das Kind hat 2 · 5 gerechnet).   (−3)² = (−3) · (−3) = 9 (Minus mal Minus gibt Plus).", "Je richtiges Ergebnis mit Begründung 1 P. Ergebnis ohne Begründung: je ½ P.", "Fehler finden"),
    (2, "6", "Jemand behauptet: „Basis und Exponent darf man vertauschen, es kommt dasselbe heraus.“ Prüfe das an 2⁵ und 5². Stimmt die Behauptung?", 1,
     "2⁵ = 32, 5² = 25. Die Ergebnisse sind verschieden, die Behauptung stimmt nicht.", "Beide Werte und das Urteil: 1 P.", "Begründen"),
]

# ---------- Klasse 8: binomische Formeln ----------
assert gleich(lambda x, y: (x + 5) ** 2, lambda x, y: x ** 2 + 10 * x + 25)
assert gleich(lambda a, b: (3 * a - 2 * b) ** 2, lambda a, b: 9 * a ** 2 - 12 * a * b + 4 * b ** 2)
assert gleich(lambda x, y: (2 * x + 7) * (2 * x - 7), lambda x, y: 4 * x ** 2 - 49)
assert gleich(lambda x, y: (y - 9) * (y + 9), lambda x, y: y ** 2 - 81)
assert gleich(lambda x, y: x ** 2 - 12 * x + 36, lambda x, y: (x - 6) ** 2)
assert gleich(lambda x, y: 25 * y ** 2 - 16, lambda x, y: (5 * y + 4) * (5 * y - 4))
assert gleich(lambda x, y: (x + 4) ** 2, lambda x, y: x ** 2 + 8 * x + 16) and not gleich(lambda x, y: (x + 4) ** 2, lambda x, y: x ** 2 + 16)
assert gleich(lambda x, y: x ** 2 + 14 * x + 49, lambda x, y: (x + 7) ** 2)
assert 49 * 51 == (50 - 1) * (50 + 1) == 50 ** 2 - 1 == 2499
K8 = [
    (1, "1", "Multipliziere aus: (x + 5)²", 1, "x² + 10x + 25", "Alle drei Glieder richtig: 1 P.", "erste binomische Formel"),
    (1, "2", "Multipliziere aus: (3a − 2b)²", 2, "9a² − 12ab + 4b²", "Quadrate richtig 1 P, gemischtes Glied mit Vorzeichen 1 P.", "zweite binomische Formel"),
    (1, "3", "Multipliziere aus: a) (2x + 7) · (2x − 7)   b) (y − 9) · (y + 9)", 2, "a) 4x² − 49   b) y² − 81", "Je Teil 1 P. Steht ein gemischtes Glied da: 0 P für diesen Teil.", "dritte binomische Formel"),
    (2, "4", "Schreibe als Produkt: a) x² − 12x + 36   b) 25y² − 16", 2, "a) (x − 6)²   b) (5y + 4) · (5y − 4)", "Je Teil 1 P.", "Umkehren (faktorisieren)"),
    (2, "5", "a) Ein Kind schreibt: (x + 4)² = x² + 16. Berichtige und schreibe dazu, was fehlt.   b) Ergänze: x² + 14x + □ = (x + □)²", 2,
     "a) x² + 8x + 16; es fehlt das gemischte Glied 2 · x · 4.   b) 49 und 7", "Je Teil 1 P. Bei b) nur eine Zahl richtig: ½ P.", "Fehler finden, Umkehren"),
    (2, "6", "Rechne 49 · 51 im Kopf mit einer binomischen Formel. Schreibe deinen Weg auf.", 1, "(50 − 1) · (50 + 1) = 50² − 1² = 2 500 − 1 = 2 499", "Ansatz mit der dritten Formel und Ergebnis: 1 P. Nur schriftlich malgenommen: ½ P.", "Verfahren wählen"),
]


def blatt(titel, wer, aufgaben):
    assert len(aufgaben) == 6 and sum(a[3] for a in aufgaben) == 10 and sum(a[3] for a in aufgaben if a[0] == 1) == 5
    z = [f"## {titel}", "", f"Für {wer}. 30 Minuten, 10 Punkte. Ohne Taschenrechner, ohne Formelsammlung, ohne Hilfe. Schreibe deinen Rechenweg auf – er wird mitbewertet.", ""]
    for teil, name in ((1, "Teil 1: Rechnen mit Rechenweg"), (2, "Teil 2: Umdrehen, begründen, Fehler finden")):
        z += [f"**{name}**", ""]
        z += [f"**{a[1]}** {a[2]} *( / {a[3]} P)*\n" for a in aufgaben if a[0] == teil]
    return z


def schema(titel, aufgaben):
    z = [f"## Lösungen und Bewertung – {titel}", "", "| Nr. | Teil | Tätigkeit | Lösung | Punkte | Bewertung |", "|---|---|---|---|---|---|"]
    z += [f"| {a[1]} | {a[0]} | {a[6]} | {a[4]} | {a[3]} | {a[5]} |" for a in aufgaben]
    return z + ["", "Teil 1 „wie in der App“: 5 Punkte. Teil 2 „weiter“: 5 Punkte.", ""]


t5, t8 = "Nachtrag K5-N · Potenzen", "Nachtrag K8-N · Binomische Formeln"
text = ["# Papier-Test 1 – Nachtrag (Auftrag 19)", "",
        "Zwei Gebiete, die im Papier-Test 1 fehlten: Potenzen (Kind 1) und binomische Formeln (Kind 2). Je 6 Aufgaben für einen späteren Papier-Test, gebaut wie die Blätter: Teil 1 „wie in der App“, Teil 2 „weiter“.",
        "Erzeugt und nachgerechnet von `nachtrag.py`. **Für das Kind nur die Seite mit seinen Aufgaben drucken.** Die Lösungen stehen getrennt am Ende.", "", "---", ""]
text += blatt(t5, "Kind 1 (Klasse 5)", K5) + ["---", ""] + blatt(t8, "Kind 2 (Klasse 8)", K8)
text += ["---", "", "# Nur für Erwachsene: Lösungen", ""] + schema(t5, K5) + schema(t8, K8)
text += ["## Nicht geprüft", "", "- Kein Kind hat die Aufgaben gerechnet. Die 30 Minuten sind aus der ersten Durchführung des Papier-Tests hochgerechnet (dort rund 2,6 bis 2,9 Minuten je Punkt), nicht an diesem Nachtrag gemessen.", "- Es gibt keinen Zwilling (Blatt B) zu diesem Nachtrag.",
         "- Ob die beiden Gebiete seit dem ersten Papier-Test weiter geübt wurden, habe ich nicht nachgesehen.", ""]
open(os.path.join(HIER, "nachtrag.md"), "w", encoding="utf-8").write("\n".join(text))
print("12 Aufgaben, alle Lösungen nachgerechnet")
print("OK")
