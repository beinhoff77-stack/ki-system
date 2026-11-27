T = "zahlen.rechengesetze"

# ───────── klammern: Brücke ─────────
m = 20
m += 10
m *= 3
m -= 15
m //= 5            # Rechenmaschine Schritt für Schritt
W(T, "klammern", "bruecke",
  "Die Tabelle beschreibt eine Rechenmaschine. Sie führt die Schritte nacheinander aus, jeweils mit dem Ergebnis des Schritts davor. Welcher Term gibt genau das Ergebnis der Maschine an?",
  ["20 + 10 · 3 − 15 : 5", "(20 + 10) · 3 − 15 : 5", "((20 + 10) · 3 − 15) : 5", "20 + 10 · (3 − 15 : 5)"], 2,
  [20 + 10 * 3 - 15 / 5 == m, (20 + 10) * 3 - 15 / 5 == m, ((20 + 10) * 3 - 15) / 5 == m, 20 + 10 * (3 - 15 / 5) == m],
  "Rechne zuerst die Maschine Schritt für Schritt aus. Prüfe dann, welcher Term durch seine Klammern dieselbe Reihenfolge erzwingt.",
  "Die Maschine rechnet: 20 + 10 = 30; 30 · 3 = 90; 90 − 15 = 75; 75 : 5 = 15. Der Term ((20 + 10) · 3 − 15) : 5 hat dieselbe Reihenfolge und ergibt 15. "
  "Ohne Klammern gilt Punkt vor Strich, dann ändert sich die Reihenfolge.",
  {0: ("ohne Klammern gerechnet: Punkt vor Strich ergibt 20 + 30 − 3", "20 + 10 * 3 - 15 / 5"),
   1: ("nur die ersten beiden Schritte geklammert, das Teilen durch 5 trifft dann nur die 15", "(20 + 10) * 3 - 15 / 5"),
   3: ("die Klammer um die falschen Schritte gesetzt", "20 + 10 * (3 - 15 / 5)")},
  "rr.reihenfolge", werte=[47, 87, 15, 20],
  grafik={"typ": "tabelle", "kopf": ["Schritt", "1", "2", "3", "4", "5"], "zeilen": [["Rechnung", "Start mit 20", "plus 10", "mal 3", "minus 15", "geteilt durch 5"]]})

# ───────── vorteil: Umkehren ─────────
Z(T, "vorteil", "umkehren",
  "Ich denke mir eine Zahl. Ich multipliziere sie mit 25, dann mit 4 und addiere zum Schluss 17. Das Ergebnis ist 2 317. Welche Zahl habe ich mir gedacht?",
  23, "(2317 - 17) / 4 / 25", "(2317 - 17) / 100",
  "Mache die Schritte in umgekehrter Reihenfolge rückgängig.",
  "Rückwärts: 2 317 − 17 = 2 300. Das Malnehmen mit 25 und mit 4 ist zusammen ein Malnehmen mit 100. Also 2 300 : 100 = 23. Probe: 23 · 25 = 575, 575 · 4 = 2 300, 2 300 + 17 = 2 317.",
  [(575, "(2317 - 17) / 4", "nur das Malnehmen mit 4 rückgängig gemacht"),
   (92, "(2317 - 17) / 25", "nur das Malnehmen mit 25 rückgängig gemacht"),
   (2300, "2317 - 17", "nur das Addieren von 17 rückgängig gemacht")],
  "rr.tauschen")

# ───────── verteilen: Fehler-Detektiv ─────────
FD(T, "verteilen",
   "Kim rechnet mit dem Verteilungsgesetz.",
   [("(84 + 12) : 6 = 84 : 6 + 12 : 6", (84 + 12) / 6 == 84 / 6 + 12 / 6),
    ("84 : (3 + 4) = 84 : 3 + 84 : 4", 84 / (3 + 4) == 84 / 3 + 84 / 4),
    ("84 : 3 + 84 : 4 = 28 + 21 = 49", 84 / 3 + 84 / 4 == 28 + 21 == 49)],
   "Rechne beide Seiten jeder Gleichung getrennt aus.",
   "Zeile 1 stimmt: Beim Teilen darf man eine Summe im Dividenden verteilen. In Zeile 2 steht die Summe aber im Teiler. Das darf man nicht verteilen: 84 : (3 + 4) = 84 : 7 = 12, aber 28 + 21 = 49. "
   "Zeile 3 rechnet mit der falschen Zeile 2 richtig weiter.",
   None, "die Summe im Teiler wie im Dividenden verteilt")

# ───────── mal_ganz: Anwenden ─────────
Z(T, "mal_ganz", "anwenden",
  "Ein Tauchroboter sinkt gleichmäßig. Seine Höhe ändert sich jede Minute um −4 m (Meeresspiegel = 0 m). Jetzt befindet er sich bei −26 m. In welcher Höhe in Metern war er vor 5 Minuten?",
  -6, "-26 + (-4) * (-5)", "-26 + 20",
  "Vor 5 Minuten heißt: Die Zeit ist −5 Minuten. Wie ändert sich die Höhe in dieser Zeit?",
  "Vor 5 Minuten war die Zeit −5 Minuten. Die Höhenänderung ist (−4) · (−5) = +20 m. Höhe damals: −26 + 20 = −6 m. Probe: Von −6 m sinkt er in 5 Minuten um 20 m auf −26 m.",
  [(-46, "-26 + (-4) * 5", "die Vergangenheit wie die Zukunft gerechnet (5 Minuten später)"),
   (-30, "-26 + (-4)", "nur eine Minute gerechnet, und zwar vorwärts statt zurück: −26 + (−4)"),
   (6, "26 - 20", "beide Vorzeichen umgekehrt: statt −26 + 20 gerechnet 26 − 20")],
  "rr.vorzeichen", einheit="m")

# ───────── umkehraufgabe_mal: Umkehren ─────────
Z(T, "umkehraufgabe_mal", "umkehren",
  "Ich denke mir eine ganze Zahl. Ich multipliziere sie mit (−6) und ziehe 15 ab. Dann teile ich durch (−3). Ich erhalte 11. Welche Zahl habe ich mir gedacht?",
  3, "(11 * (-3) + 15) / (-6)", "((11 * (-3)) + 15) / (-6)",
  "Beginne mit dem letzten Schritt und kehre jeden Schritt um. Was ist die Umkehrung von „geteilt durch −3“?",
  "Rückwärts: Die Umkehrung von „: (−3)“ ist „· (−3)“: 11 · (−3) = −33. Die Umkehrung von „− 15“ ist „+ 15“: −33 + 15 = −18. Die Umkehrung von „· (−6)“ ist „: (−6)“: (−18) : (−6) = 3. "
  "Probe: 3 · (−6) = −18; −18 − 15 = −33; (−33) : (−3) = 11.",
  [(8, "(11 * (-3) - 15) / (-6)", "das Abziehen von 15 falsch rückgängig gemacht (noch einmal abgezogen)"),
   (-3, "(11 * (-3) + 15) / 6", "beim letzten Schritt das Vorzeichen von −6 vergessen"),
   (-18, "11 * (-3) + 15", "den Faktor (−6) nicht rückgängig gemacht")],
  "rr.gegenrechnung")

# ───────── schriftlich: Brücke (fehlenden Gitterwert nur über die Teilzeilensumme erschließen) ─────────
assert 46 * 30 == 1380 and 40 * 30 == 1200 and 1380 - 1200 == 180
Z(T, "schriftlich", "bruecke",
  "Das Malgitter gehört zu einer schriftlichen Multiplikation. Die Zahlen am Rand fehlen. Die linke Spalte gehört zur Zehnerziffer des zweiten Faktors, die rechte Spalte zur Einerziffer. "
  "Kim rechnet dieselbe Aufgabe schriftlich. Seine erste Zeile (die Multiplikation mit der Zehnerziffer) ergibt 1 380. Welche Zahl gehört in das Feld mit dem Fragezeichen?",
  180, "1380 - 1200", "1380 - 1200 + 0",
  "Welche Felder des Gitters gehören zu Kims erster Zeile? Was muss ihre Summe ergeben?",
  "Kims erste Zeile ist die Summe der Felder der linken Spalte: 1 200 + ? = 1 380. Also ist ? = 1 380 − 1 200 = 180. "
  "Die rechte Spalte (320 und 48) gehört zur zweiten Zeile, der Multiplikation mit der Einerziffer.",
  [(1380, "1380", "die ganze erste Zeile genannt statt des einen Feldes"),
   (2580, "1380 + 1200", "1 200 zu 1 380 dazugezählt statt abgezogen"),
   (1060, "1380 - 320", "ein Feld der rechten Spalte (320) statt des Feldes 1 200 abgezogen")],
  None,
  grafik={"typ": "tabelle", "kopf": ["Feld", "linke Spalte", "rechte Spalte"], "zeilen": [["oben", "1 200", "320"], ["unten", "?", "48"]]})
