"""Mathe-Profi, Denkpapier Methoden: Rechnungen zu den drei Stufen (Antippen, Lückenweg, Heft mit Stichprobe).

Aufruf: python3 -I inhalte/mathe-profi/methoden_probe.py
Nur Rechnungen, keine Lerndaten.
"""
from fractions import Fraction as F

# ── Beispiel des Projektleiters: I: 2x + y = 11, II: x − y = 1 ──
x, y = 4, 3
assert 2 * x + y == 11 and x - y == 1
# Drei Verfahren, jedes kommt an einer Gleichung mit nur einer Unbekannten vorbei (Wegmarke)
assert (2 + 1, 11 + 1) == (3, 12)                    # Addition I + II: 3x = 12
assert (2 + 1, 11 - 2) == (3, 9)                     # Einsetzen x = y + 1 in I: 2(y + 1) + y = 11 → 3y = 9
assert (11 + 1, 2 + 1) == (12, 3)                    # Gleichsetzen: 11 − 2x = x − 1 → 12 = 3x
# „I − II“ ist nicht falsch, nur nutzlos: x + 2y = 10 gilt für die Lösung, y fällt aber nicht weg
assert (2 - 1) * x + (1 - (-1)) * y == 11 - 1 == 10
# „3x = 10“ ist falsch: rechts nicht addiert
assert 3 * x != 10


def stichprobe(a, unbekannte, b):
    """Referenz: Zeile a · [x|y] = b. Gleichwertig zur Lösung? „1 · x = 4“ ist schon die Lösung."""
    wert = {"x": x, "y": y}[unbekannte]
    if a == 0:
        return "unsinn"
    if a == 1:
        return "schon die Lösung"
    return "gleichwertig" if F(b, a) == wert else "nicht gleichwertig"


assert stichprobe(3, "x", 12) == stichprobe(6, "x", 24) == stichprobe(3, "y", 9) == "gleichwertig"
assert stichprobe(1, "x", 4) == "schon die Lösung" and stichprobe(3, "x", 10) == "nicht gleichwertig"
# Schwäche: Wer die Lösung hat (auch geraten), kann eine Zeile erfinden – jede Vervielfachung gilt
assert all(stichprobe(a, "x", a * x) == "gleichwertig" for a in (2, 5, 7, -3))
# Raten ist bei kleinen ganzen Lösungen leicht: Paare von 0 bis 9, die II erfüllen und I erfüllen
assert [(a, b) for a in range(10) for b in range(10) if 2 * a + b == 11 and a - b == 1] == [(4, 3)]
assert len([(a, b) for a in range(10) for b in range(10) if a - b == 1]) == 9          # nur 9 Paare zum Durchprobieren

# Stufe 1: drei Möglichkeiten je Schritt, zweiter Versuch erlaubt
p_zwei = F(1, 3) + F(2, 3) * F(1, 2)
assert p_zwei == F(2, 3) and F(1, 3) ** 4 == F(1, 81)                                    # 4 Schritte im ersten Versuch geraten: 1 von 81

# ── Klasse 5: 18 − 3 · (4 − 9) ──
assert 4 - 9 == -5 and 3 * (-5) == -15 and 18 - (-15) == 33 == 18 - 3 * (4 - 9)
fehlbilder5 = {"Klammer: größere minus kleinere": 18 - 3 * 5, "von links: 18 − 3 zuerst": (18 - 3) * (4 - 9),
               "Faktor nur zum ersten Glied": 18 - 3 * 4 - 9, "Produkt +15 statt −15, dann abgezogen": 18 - 15,
               "Minus-Minus übersehen": 18 - 15, "Ergebnis mit falschem Vorzeichen": -33}
assert fehlbilder5 == {"Klammer: größere minus kleinere": 3, "von links: 18 − 3 zuerst": -75, "Faktor nur zum ersten Glied": -3,
                       "Produkt +15 statt −15, dann abgezogen": 3, "Minus-Minus übersehen": 3, "Ergebnis mit falschem Vorzeichen": -33}
# Drei verschiedene Denkfehler liefern 3 – das Ergebnis trennt sie nicht, der Teilterm-Wert schon:
assert (3 * 5, 3 * (-5)) == (15, -15)                # Klammer falsch → Produkt 15; Produkt richtig (−15) → Fehler danach
# Der Wert eines Teilterms hängt nicht vom Weg ab: auch wer verteilt, bekommt für 3 · (4 − 9) den Wert −15
assert 3 * 4 - 3 * 9 == -15 and 18 - 12 + 27 == 33

# ── Klasse 8, keine Gleichung: Gerade durch P(−2 | 5) und Q(4 | 2) ──
m = F(2 - 5, 4 - (-2))
t = 5 - m * (-2)
assert (m, t) == (F(-1, 2), 4) and m * 4 + t == 2 and m * (-2) + t == 5
fehl_m = {"Kehrwert (Δx : Δy)": F(4 - (-2), 2 - 5), "Reihenfolge gemischt": F(5 - 2, 4 - (-2)), "Minus-Minus im Nenner übersehen": F(2 - 5, 4 - 2)}
assert fehl_m == {"Kehrwert (Δx : Δy)": -2, "Reihenfolge gemischt": F(1, 2), "Minus-Minus im Nenner übersehen": F(-3, 2)}
assert len(set(fehl_m.values()) | {m}) == 4          # alle Fehlbilder verschieden: Trennaufgabe
fehl_t = {"Zeichen-Paar: −½ · (−2) = −1": 5 - (-1), "t = y-Wert des Punkts": 5, "beim Umstellen addiert statt abgezogen": 5 + 1}
assert fehl_t == {"Zeichen-Paar: −½ · (−2) = −1": 6, "t = y-Wert des Punkts": 5, "beim Umstellen addiert statt abgezogen": 6}
assert F(2 - 5, 4 + 2) == F(5 - 2, -2 - 4)           # beide Reihenfolgen richtig, solange oben und unten gleich
print("OK")
