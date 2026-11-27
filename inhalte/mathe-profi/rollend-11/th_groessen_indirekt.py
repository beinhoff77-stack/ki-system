T = "groessen.indirekt"

# ───────── graph: Zwei Wege ─────────
assert 4 * 15 == 60 and 60 / 10 - 60 / 20 == 3
Z(T, "graph", "zwei_wege",
  "Der Punkt P(4 | 15) liegt auf dem Graphen einer indirekten Proportionalität (für x > 0). Die Punkte A(10 | a) und B(20 | b) liegen auf demselben Graphen. "
  "Weg A: Zeichne auf kariertem Papier P und weitere Punkte des Graphen ein (bestimme dazu das Produkt x · y), skizziere den Ast und lies a und b bei x = 10 und x = 20 ungefähr ab. "
  "Weg B: Rechne a und b exakt aus. Wie groß ist a − b (exakter Wert)?",
  3, "60 / 10 - 60 / 20", "15 / (10 / 4) - 15 / (20 / 4)",
  "Beide Wege müssen ungefähr dasselbe ergeben. Bei einer indirekten Proportionalität ist das Produkt x · y für alle Punkte gleich.",
  "Weg A: x · y = 4 · 15 = 60. Punkte des Graphen: (2 | 30), (3 | 20), (4 | 15), (5 | 12), (6 | 10), (12 | 5), (15 | 4). Man zeichnet sie, verbindet sie zu einem Ast und liest bei x = 10 etwa a ≈ 6 und bei x = 20 etwa b ≈ 3 ab. "
  "Weg B: exakt a = 60 : 10 = 6 und b = 60 : 20 = 3. Also a − b = 3.",
  [(9, "60 / 10 + 60 / 20", "die Werte addiert statt voneinander abgezogen"),
   (6, "60 / 10", "nur den y-Wert von A genannt"),
   (-37.5, "15 * 10 / 4 - 15 * 20 / 4", "wie bei einer direkten Proportionalität gerechnet (y wächst mit x): a = 37,5 und b = 75, also a − b = −37,5")],
  None)
