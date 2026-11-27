import itertools

T = "stochastik.kombinatorik"

# ───────── systematisch: Zwei Wege ─────────
ziffern = [1, 2, 3, 4, 5]
paare = [(a, b) for a in ziffern for b in ziffern if a != b and (a + b) % 2 == 0]
assert len(paare) == 8      # Weg A: alle zweistelligen Zahlen aufgelistet
Z(T, "systematisch", "zwei_wege",
  "Aus den Ziffern 1, 2, 3, 4 und 5 werden zweistellige Zahlen mit zwei verschiedenen Ziffern gebildet. "
  "Weg A: Schreibe alle diese Zahlen systematisch auf und zähle die passenden. Weg B: Zähle getrennt die Zahlen mit zwei ungeraden Ziffern und die Zahlen mit zwei geraden Ziffern. Wie viele der Zahlen haben eine gerade Quersumme?",
  8, "3 * 2 + 2 * 1", "6 + 2",
  "Beide Wege müssen dieselbe Anzahl ergeben. Welche der Ziffern sind gerade, welche ungerade?",
  "Weg A: Passend sind 13, 15, 31, 35, 51, 53 (zwei ungerade Ziffern) und 24, 42 (zwei gerade Ziffern): 8 Zahlen. "
  "Weg B: Zwei ungerade Ziffern aus 1, 3, 5: 3 · 2 = 6 Zahlen. Zwei gerade Ziffern aus 2, 4: 2 · 1 = 2 Zahlen. Zusammen 6 + 2 = 8. "
  "Bei einer geraden und einer ungeraden Ziffer ist die Quersumme ungerade.",
  [(20, "5 * 4", "alle Zahlen mit verschiedenen Ziffern gezählt, ohne die Bedingung zu beachten"),
   (13, "3 * 3 + 2 * 2", "gleiche Ziffern wie 11, 33, 55, 22, 44 mitgezählt, obwohl die Ziffern verschieden sein sollen"),
   (6, "3 * 2", "nur die Zahlen mit zwei ungeraden Ziffern gezählt")],
  "id.daten.stufen")

# ───────── reihenfolgen: Fehler-Detektiv ─────────
echte = {p for p in itertools.permutations(range(5)) if set(p[:3]) == {0, 1, 2}}      # Mädchen 0, 1, 2 vorn, Jungen 3, 4 hinten
assert len(echte) == 12
FD(T, "reihenfolgen",
   "Fünf verschiedene Kinder stellen sich in einer Reihe auf. Die 3 Mädchen stehen auf den Plätzen 1 bis 3, die 2 Jungen auf den Plätzen 4 und 5. Kim zählt die möglichen Reihenfolgen.",
   [("Für die Mädchen gibt es auf den Plätzen 1 bis 3 genau 3 · 2 · 1 = 6 Möglichkeiten.", 3 * 2 * 1 == 6 == len({p[:3] for p in echte})),
    ("Für die Jungen gibt es auf den Plätzen 4 und 5 genau 2 · 1 = 2 Möglichkeiten.", 2 * 1 == 2 == len({p[3:] for p in echte})),
    ("Zu jeder der 6 Anordnungen der Mädchen gibt es alle 2 Anordnungen der Jungen.", len(echte) == 6 * 2),
    ("Die Möglichkeiten der Mädchen und der Jungen werden zusammengezählt: 6 + 2 = 8 Reihenfolgen.", 6 + 2 == len(echte))],
   "Prüfe jede Zeile einzeln. Passt die Rechenart zur Frage?",
   "Zeile 1 bis 3 stimmen. Weil zu jeder der 6 Anordnungen der Mädchen jede der 2 Anordnungen der Jungen passt, muss man malnehmen: 6 · 2 = 12 Reihenfolgen. In Zeile 4 wird stattdessen 6 + 2 = 8 gerechnet.",
   "id.daten.stufen", "die Möglichkeiten addiert statt malgenommen")

# ───────── baumdiagramm: Anwenden ─────────
menues = sum(1 for haupt, soessen in (("Nudeln", 3), ("Reis", 2), ("Kartoffeln", 4)) for _ in range(soessen) for _ in range(2))
assert menues == 18
Z(T, "baumdiagramm", "anwenden",
  "Bei einem Schulfest wählt jedes Kind zuerst ein Hauptgericht. Zur Wahl stehen Nudeln (dazu 3 Soßen zur Wahl), Reis (dazu 2 Soßen) und Kartoffeln (dazu 4 Soßen). "
  "Danach wählt jedes Kind noch einen Nachtisch aus 2 Sorten, bei jedem Hauptgericht dieselben zwei. Ein Menü besteht aus Hauptgericht, Soße und Nachtisch. Wie viele verschiedene Menüs sind möglich?",
  18, "(3 + 2 + 4) * 2", "3 * 2 + 2 * 2 + 4 * 2",
  "Zeichne die Äste für das Hauptgericht. Bei den Soßen ist die Zahl der Äste nicht bei jedem Ast gleich.",
  "Baumdiagramm: Nudeln hat 3 Soßen, Reis 2, Kartoffeln 4. Das sind 3 + 2 + 4 = 9 Wege bis zur Soße. Jeder dieser Wege teilt sich in 2 Nachtische: 9 · 2 = 18 Menüs. "
  "Man kann auch rechnen: 3 · 2 + 2 · 2 + 4 · 2 = 6 + 4 + 8 = 18.",
  [(24, "3 * 4 * 2", "bei jedem Hauptgericht 4 Soßen angenommen: 3 · 4 · 2"),
   (9, "3 + 2 + 4", "die Wege bis zur Soße gezählt und den Nachtisch vergessen"),
   (12, "3 * 2 * 2", "bei jedem Hauptgericht nur 2 Soßen angenommen: 3 · 2 · 2")],
  "id.daten.stufen", einheit="Menüs")

# ───────── bedingungen: Umkehren ─────────
assert 9 * 10 ** (5 - 1) == 90000 and 9 * 10 ** (4 - 1) != 90000
Z(T, "bedingungen", "umkehren",
  "Ein Zahlencode besteht nur aus Ziffern von 0 bis 9. Die erste Ziffer darf nicht 0 sein, die übrigen Ziffern sind beliebig und dürfen sich wiederholen. "
  "Alle Codes sind gleich lang. Es gibt insgesamt 90 000 mögliche Codes. Wie viele Ziffern hat ein Code?",
  5, "4 + 1", "1 + 4",
  "Wie viele Möglichkeiten hat die erste Ziffer? Wie viele hat jede weitere Ziffer?",
  "Für die erste Ziffer gibt es 9 Möglichkeiten (1 bis 9). 90 000 : 9 = 10 000 = 10 · 10 · 10 · 10: Die übrigen Ziffern haben je 10 Möglichkeiten, und es sind 4 solche Stellen. "
  "Zusammen mit der ersten Ziffer hat der Code 5 Ziffern. Probe: 9 · 10 · 10 · 10 · 10 = 90 000.",
  [(4, "5 - 1", "nur die vier Stellen mit 10 Möglichkeiten gezählt und die erste Ziffer vergessen"),
   (6, "5 + 1", "eine Stelle zu viel gezählt: 10 000 hat 5 Ziffern"),
   (9, "90000 / 10000", "die Zahl der Möglichkeiten der ersten Ziffer genannt statt der Zahl der Ziffern")],
  "id.daten.stufen")
