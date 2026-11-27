T = "terme.umformen"

# ───────── produkte: Anwenden ─────────
assert 6 * 2 ** 3 == 48 and 3 * 2 == 6
Z(T, "produkte", "anwenden",
  "Ein quaderförmiges Aquarium ist 3a dm lang, 2a dm breit und a dm hoch (a ist eine positive ganze Zahl). Es fasst 48 Liter (1 dm³ ist 1 Liter). Wie viele Dezimeter ist das Aquarium lang?",
  6, "3 * 2", "216 / 36",
  "Fasse die drei Kantenlängen zu einem Term für das Volumen zusammen. Welchen Wert hat a³? Welche positive ganze Zahl ergibt hoch drei diesen Wert?",
  "Volumen = 3a · 2a · a = 6a³ dm³. 6a³ = 48 ergibt a³ = 8, also a = 2 (denn 2 · 2 · 2 = 8). Die Länge ist 3a = 3 · 2 = 6 dm. Probe: 6 dm · 4 dm · 2 dm = 48 dm³.",
  [(2, "2", "nur a bestimmt und nicht die Länge 3a"),
   (24, "3 * 8", "aus a³ = 8 fälschlich a = 8 geschlossen: Länge 3 · 8"),
   (16, "48 / 3", "das Volumen einfach durch den Faktor 3 vor dem a geteilt")],
  "rr.tauschen", einheit="dm")

# ───────── ausmultiplizieren: Fehler-Detektiv ─────────
FD(T, "ausmultiplizieren",
   "Kim vereinfacht 4(2x − 3) − 3(x − 5) − 2(5 − x) in Schritten.",
   [("4(2x − 3) = 8x − 12", gl("4*(2*x-3)", "8*x-12")),
    ("−3(x − 5) = −3x + 15", gl("-3*(x-5)", "-3*x+15")),
    ("−2(5 − x) = −10 − 2x", gl("-2*(5-x)", "-10-2*x")),
    ("Zusammen: 8x − 12 − 3x + 15 − 10 − 2x = 3x − 7", gl("8*x-12-3*x+15-10-2*x", "3*x-7"))],
   "Prüfe jede Zeile mit einer Zahl für x, zum Beispiel x = 1.",
   "Zeile 1 und 2 stimmen. In Zeile 3 wird −2 mit 5 und mit (−x) multipliziert: −2 · 5 = −10 und −2 · (−x) = +2x. Richtig ist also −10 + 2x. Zeile 4 rechnet mit dem falschen Ergebnis richtig weiter. "
   "Mit dem richtigen Wert ergibt sich 7x − 7.",
   "rr.ausmultiplizieren", "−2 · (−x) als −2x gerechnet (Vorzeichen in der Klammer nicht beachtet)")

# ───────── aequivalenz: Zwei Wege ─────────
assert gl("4*(x+3)-2*(x-1)", "2*x+14") and not gl("4*(x+3)-3*(x-1)", "2*x+14")
Z(T, "aequivalenz", "zwei_wege",
  "Die Terme 4(x + 3) − k(x − 1) und 2x + 14 haben für jede Zahl x denselben Wert. "
  "Weg A: Multipliziere den ersten Term aus und vergleiche die Glieder mit x und die Zahlen. Weg B: Setze für x zwei geschickt gewählte Zahlen ein. Welche Zahl ist k?",
  2, "14 - 12", "(4 - 2)",
  "Beide Wege müssen dasselbe k ergeben. Welche Zahl für x macht die Rechnung besonders einfach? Prüfe das Ergebnis mit einer zweiten Zahl.",
  "Weg A: 4(x + 3) − k(x − 1) = 4x + 12 − kx + k = (4 − k)x + (12 + k). Vergleich mit 2x + 14: 4 − k = 2 und 12 + k = 14, beides gibt k = 2. "
  "Weg B: Für x = 0 ist 12 + k = 14, also k = 2. Zur Kontrolle x = 2: 4 · 5 − 2 · 1 = 18 und 2 · 2 + 14 = 18. Zwei Proben genügen hier, weil beide Terme für ein festes k in x linear sind: Stimmen sie an zwei verschiedenen Stellen überein, dann an jeder.",
  [(-2, "2 - 4", "bei den Gliedern mit x das Vorzeichen von −k(x − 1) übersehen: 4 + k = 2"),
   (14, "14", "das Zahlenglied 12 vergessen und k = 14 gesetzt"),
   (10, "14 - 4", "für die 12 fälschlich 4 genommen: 14 − 4")],
  None)
