T = "terme.umformen_teil2"

# ───────── summe_mal_summe: Umkehren ─────────
assert gl("(x+7)*(x-5)", "x**2+2*x-35")
Z(T, "summe_mal_summe", "umkehren",
  "Das Produkt (x + p)(x − 5) ergibt ausgemultipliziert und zusammengefasst x² + 2x − 35, und das gilt für jede Zahl x. Welche Zahl ist p?",
  7, "2 + 5", "(-35) / (-5)",
  "Multipliziere (x + p)(x − 5) allgemein aus. Welche Glieder müssen mit x und welche ohne x übereinstimmen?",
  "(x + p)(x − 5) = x² − 5x + px − 5p = x² + (p − 5)x − 5p. Vergleich mit x² + 2x − 35: p − 5 = 2, also p = 7. Kontrolle am Zahlenglied: −5p = −35 gilt für p = 7.",
  [(-3, "2 - 5", "p − 5 = 2 falsch umgestellt: p = 2 − 5"),
   (-7, "(-35) / 5", "durch +5 statt durch −5 geteilt"),
   (-30, "-35 + 5", "−5p = −35 falsch umgestellt: p = −35 + 5")],
  "rr.ausmultiplizieren")

# ───────── ausklammern: Brücke ─────────
assert gl("10*x**2", "5*x*2*x") and gl("15*x", "5*x*3") and 2 * 4 + 3 == 11
Z(T, "ausklammern", "bruecke",
  "Ein Rechteck besteht aus zwei Teilrechtecken nebeneinander, die dieselbe Höhe h haben. Die Tabelle zeigt ihre Flächeninhalte (x ist eine positive Zahl ohne Einheit, die Flächen sind in cm² angegeben). "
  "Als Höhe h wird der größte gemeinsame Faktor beider Flächeninhalte gewählt (mit Zahl und x). Wie breit ist das ganze Rechteck für x = 4 (in cm)?",
  11, "2 * 4 + 3", "(10 * 4 ** 2 + 15 * 4) / (5 * 4)",
  "Welche Zahl und welche Potenz von x teilt beide Flächeninhalte? Die Breite eines Teils ist Fläche geteilt durch Höhe.",
  "Gemeinsamer Faktor von 10x² und 15x ist 5x. Die Höhe ist 5x cm. Breite links: 10x² : 5x = 2x cm. Breite rechts: 15x : 5x = 3 cm. Gesamtbreite (2x + 3) cm. Für x = 4: 2 · 4 + 3 = 11 cm. "
  "Probe: Fläche 5x(2x + 3) = 20 · 11 = 220 und 10 · 16 + 15 · 4 = 220.",
  [(55, "10 * 4 + 15", "als Höhe nur x gewählt, nicht den größten gemeinsamen Faktor 5x: Breite 10x + 15"),
   (44, "2 * 4 ** 2 + 3 * 4", "als Höhe nur die Zahl 5 gewählt: Breite 2x² + 3x"),
   (20, "2 * 4 + 3 * 4", "15x : 5x als 3x statt als 3 gerechnet")],
  "rr.ausmultiplizieren", einheit="cm",
  grafik={"typ": "tabelle", "kopf": ["Teilrechteck", "links", "rechts"], "zeilen": [["Flächeninhalt", "10x² cm²", "15x cm²"]]})

# ───────── binomisch: Zwei Wege ─────────
assert 97 ** 2 - 96 * 98 == 1
Z(T, "binomisch", "zwei_wege",
  "Berechne 97² − 96 · 98 auf zwei Wegen. Weg A: Rechne 97² mit der zweiten binomischen Formel als (100 − 3)² und 96 · 98 als (100 − 4)(100 − 2) einzeln aus. "
  "Weg B: Schreibe 96 als 97 − 1 und 98 als 97 + 1 und benutze die dritte binomische Formel. Welchen Wert hat der Term?",
  1, "97 ** 2 - 96 * 98", "97 ** 2 - (97 ** 2 - 1)",
  "Beide Wege müssen dasselbe ergeben. Die zweite binomische Formel hat in der Mitte das Glied −2ab.",
  "Weg A: (100 − 3)² = 10 000 − 600 + 9 = 9 409. (100 − 4)(100 − 2) = 10 000 − 200 − 400 + 8 = 9 408. Differenz 9 409 − 9 408 = 1. "
  "Weg B: 96 · 98 = (97 − 1)(97 + 1) = 97² − 1². Also 97² − 96 · 98 = 97² − (97² − 1) = 1.",
  [(583, "9991 - 9408", "(100 − 3)² mit 100² − 3² = 9 991 verwechselt (Quadrat auf beide Zahlen verteilt), dann 9 991 − 9 408 gerechnet"),
   (-1, "9408 - 9409", "die Differenz in falscher Reihenfolge gerechnet"),
   (2, "98 - 96", "die Differenz der beiden Faktoren genannt")],
  "rr.ausmultiplizieren")
