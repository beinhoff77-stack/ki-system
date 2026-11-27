T = "zahlen.potenzen_basis"

# ───────── berechnen: Brücke ─────────
Z(T, "berechnen", "bruecke",
  "Die Tabelle zeigt, wie viele Zellen eine Kultur nach 1, 2, 3 und 4 Stunden hat. Von Stunde zu Stunde wird die Zahl der Zellen jedes Mal mit derselben Zahl malgenommen. Wie viele Zellen sind es nach 7 Stunden?",
  2187, "3 ** 7", "3 * 3 * 3 * 3 * 3 * 3 * 3",
  "Wie entsteht jede Zahl der Tabelle aus der Zahl davor? Schreibe die Zahlen als Potenzen.",
  "Jede Zahl ist dreimal so groß wie die davor: 3 = 3¹, 9 = 3², 27 = 3³, 81 = 3⁴. Nach n Stunden sind es 3ⁿ Zellen. Nach 7 Stunden: 3⁷ = 2 187 Zellen.",
  [(21, "3 * 7", "„mal 7“ statt „hoch 7“ gerechnet: 3 · 7"),
   (729, "3 ** 6", "die Hochzahl um 1 zu klein (3⁶)"),
   (343, "7 ** 3", "Basis und Hochzahl vertauscht: 7³")],
  "id.zahlen.hoch_zurueck", einheit="Zellen",
  grafik={"typ": "tabelle", "kopf": ["Stunden", "1", "2", "3", "4"], "zeilen": [["Zellen", "3", "9", "27", "81"]]})

# ───────── vertauschen: Fehler-Detektiv ─────────
FD(T, "vertauschen",
   "Ein Zahlenschloss hat 4 Rädchen. Jedes Rädchen hat 6 Stellungen. Kim zählt, wie viele Einstellungen es gibt.",
   [("Bei 4 Rädchen mit je 6 Stellungen gibt es 4⁶ Einstellungen (Basis 4, Hochzahl 6).", 4 ** 6 == 6 ** 4),
    ("4⁶ = 4 · 4 · 4 · 4 · 4 · 4 = 4 096.", 4 * 4 * 4 * 4 * 4 * 4 == 4096),
    ("Das Schloss hat also 4 096 Einstellungen.", 4 ** 6 == 4096)],
   "Überlege mit 2 Rädchen: Wie viele Einstellungen gibt es dann?",
   "Mit 2 Rädchen gäbe es 6 · 6 = 36 Einstellungen. Jedes Rädchen bringt den Faktor 6, und es gibt 4 Rädchen: Richtig ist 6⁴ = 1 296. In Zeile 1 sind Basis und Hochzahl vertauscht. "
   "Zeile 2 rechnet 4⁶ richtig aus, Zeile 3 folgt daraus.",
   "id.zahlen.hoch_zurueck", "Basis und Hochzahl vertauscht: 4⁶ statt 6⁴")

# ───────── negativ: Anwenden ─────────
Z(T, "negativ", "anwenden",
  "Bei einem Spiel wird der Punktestand nach jeder Runde mit (−2) malgenommen. Du startest mit 3 Punkten. Wie viele Punkte hast du nach 5 Runden?",
  -96, "3 * (-2) ** 5", "3 * (-2) * (-2) * (-2) * (-2) * (-2)",
  "Schreibe die 5 Runden als Potenz. Wie oft kommt der Faktor (−2) vor, und was bedeutet das für das Vorzeichen?",
  "Nach 5 Runden wurde 5-mal mit (−2) malgenommen: 3 · (−2)⁵. (−2)⁵ = −32, denn bei einer ungeraden Zahl von Faktoren bleibt das Minus stehen. 3 · (−32) = −96 Punkte.",
  [(96, "3 * 2 ** 5", "das Minus vergessen: 3 · 32"),
   (-30, "3 * (-2) * 5", "„hoch 5“ als „mal 5“ gerechnet: 3 · (−2) · 5"),
   (-32, "(-2) ** 5", "den Startwert 3 vergessen")],
  "rr.potenz", einheit="Punkte")
