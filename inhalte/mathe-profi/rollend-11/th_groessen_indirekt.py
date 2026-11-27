T = "groessen.indirekt"

# ───────── graph: Zwei Wege ─────────
assert 4 * 15 == 60 and 60 / 10 - 60 / 20 == 3
Z(T, "graph", "zwei_wege",
  "Der Punkt P(4 | 15) liegt auf dem Graphen einer indirekten Proportionalität (für x > 0). Die Punkte A(10 | a) und B(20 | b) liegen auf demselben Graphen. Wie groß ist a − b? "
  "Weg A: Bestimme zuerst das Produkt x · y und rechne damit a und b aus. Weg B: Gehe von P aus. Wenn x mit einem Faktor malgenommen wird, wird y durch denselben Faktor geteilt.",
  3, "60 / 10 - 60 / 20", "15 / (10 / 4) - 15 / (20 / 4)",
  "Beide Wege müssen dasselbe ergeben. Bei einer indirekten Proportionalität ist das Produkt x · y für alle Punkte gleich.",
  "Weg A: x · y = 4 · 15 = 60. Also a = 60 : 10 = 6 und b = 60 : 20 = 3. Weg B: x wird von 4 auf 10 mit 2,5 malgenommen, also y = 15 : 2,5 = 6. x wird von 4 auf 20 mit 5 malgenommen, also y = 15 : 5 = 3. "
  "Beide Wege: a = 6, b = 3, a − b = 3.",
  [(9, "60 / 10 + 60 / 20", "die Werte addiert statt voneinander abgezogen"),
   (6, "60 / 10", "nur den y-Wert von A genannt"),
   (37.5, "15 * 20 / 4 - 15 * 10 / 4", "wie bei einer direkten Proportionalität gerechnet (y wächst mit x)")],
  "id.verhaeltnisse.groesse")
