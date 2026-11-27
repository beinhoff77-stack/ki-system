T = "terme.quadratische_extreme"

# ───────── scheitelform: Anwenden ─────────
assert gl("x**2-12*x+50", "(x-6)**2+14") and (6 ** 2 - 12 * 6 + 50) * 100 == 1400
Z(T, "scheitelform", "anwenden",
  "Ein Hersteller berechnet seine Kosten mit K(x) = x² − 12x + 50. Dabei ist x die Produktmenge in Hundert Stück und K(x) sind die Kosten in Hundert Euro. "
  "Wie viel Euro betragen die kleinsten möglichen Kosten?",
  1400, "(50 - 36) * 100", "(6 ** 2 - 12 * 6 + 50) * 100",
  "Forme K(x) mit quadratischer Ergänzung in die Scheitelform um. Der kleinste Wert steht im Scheitel. Beachte die Einheit „Hundert Euro“.",
  "x² − 12x + 50 = (x − 6)² − 36 + 50 = (x − 6)² + 14. Das Quadrat ist nie negativ, der kleinste Wert ist 14 und wird bei x = 6 erreicht. 14 Hundert Euro sind 1 400 €. Probe: K(6) = 36 − 72 + 50 = 14.",
  [(14, "14", "die Einheit vergessen: 14 statt 14 Hundert Euro"),
   (600, "6 * 100", "den x-Wert des Scheitels genannt statt des Minimalwerts"),
   (8600, "(36 + 50) * 100", "die ergänzte 36 addiert statt abgezogen")],
  "rr.tauschen", einheit="€")
