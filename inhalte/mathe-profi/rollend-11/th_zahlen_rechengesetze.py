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
  "rr.reihenfolge")

# ───────── verteilen: Fehler-Detektiv ─────────
FD(T, "verteilen",
   "Kim rechnet mit dem Verteilungsgesetz.",
   [("(84 + 12) : 6 = 84 : 6 + 12 : 6", (84 + 12) / 6 == 84 / 6 + 12 / 6),
    ("84 : (3 + 4) = 84 : 3 + 84 : 4", 84 / (3 + 4) == 84 / 3 + 84 / 4),
    ("84 : 3 + 84 : 4 = 28 + 21 = 49", 84 / 3 + 84 / 4 == 28 + 21 == 49)],
   "Rechne beide Seiten jeder Gleichung getrennt aus.",
   "Zeile 1 stimmt: Beim Teilen darf man eine Summe im Dividenden verteilen. In Zeile 2 steht die Summe aber im Teiler. Das darf man nicht verteilen: 84 : (3 + 4) = 84 : 7 = 12, aber 28 + 21 = 49. "
   "Zeile 3 rechnet mit der falschen Zeile 2 richtig weiter.",
   "rr.ausmultiplizieren", "die Summe im Teiler wie im Dividenden verteilt")

# ───────── mal_ganz: Anwenden ─────────
Z(T, "mal_ganz", "anwenden",
  "Ein Tauchroboter sinkt gleichmäßig. Seine Höhe ändert sich jede Minute um −4 m (Meeresspiegel = 0 m). Jetzt befindet er sich bei −26 m. In welcher Höhe in Metern war er vor 5 Minuten?",
  -6, "-26 + (-4) * (-5)", "-26 + 20",
  "Vor 5 Minuten heißt: Die Zeit ist −5 Minuten. Wie ändert sich die Höhe in dieser Zeit?",
  "Vor 5 Minuten war die Zeit −5 Minuten. Die Höhenänderung ist (−4) · (−5) = +20 m. Höhe damals: −26 + 20 = −6 m. Probe: Von −6 m sinkt er in 5 Minuten um 20 m auf −26 m.",
  [(-46, "-26 + (-4) * 5", "die Vergangenheit wie die Zukunft gerechnet (5 Minuten später)"),
   (-30, "-26 + (-4)", "nur eine Minute zurückgerechnet"),
   (6, "26 - 20", "das Vorzeichen des Startwerts vergessen")],
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
  "rr.vorzeichen")

# ───────── schriftlich: Brücke ─────────
W(T, "schriftlich", "bruecke",
  "Das Malgitter zeigt die Teilprodukte von 46 · 38. Kim rechnet dieselbe Aufgabe schriftlich. Zuerst rechnet er die Zeile mit der Zehnerziffer 3 (also 46 · 30), dann die Zeile mit der Einerziffer 8 (also 46 · 8). "
  "Welche beiden Felder des Gitters ergeben zusammen Kims erste Zeile 46 · 30?",
  ["1 200 und 180", "1 200 und 320", "320 und 48", "180 und 48"], 0,
  [1200 + 180 == 46 * 30, 1200 + 320 == 46 * 30, 320 + 48 == 46 * 30, 180 + 48 == 46 * 30],
  "In welcher Spalte des Gitters steht der Faktor 30?",
  "Die erste Zeile 46 · 30 = 1 380 gehört zur Spalte mit 30: 40 · 30 = 1 200 und 6 · 30 = 180, zusammen 1 380. "
  "Die zweite Zeile 46 · 8 = 368 gehört zur Spalte mit 8: 320 + 48 = 368. Zusammen 1 380 + 368 = 1 748.",
  {1: ("ein Feld der Spalte 30 mit einem Feld der Spalte 8 gemischt: 1 200 + 320", "1200 + 320"),
   2: ("die Spalte mit 8 genommen (das ist die zweite Zeile 46 · 8 = 368)", "320 + 48"),
   3: ("die untere Zeile des Gitters genommen (6 · 30 und 6 · 8) statt der Spalte 30", "180 + 48")},
  "rr.stellenwert", werte=[1380, 1520, 368, 228],
  grafik={"typ": "tabelle", "kopf": ["·", "30", "8"], "zeilen": [["40", "1 200", "320"], ["6", "180", "48"]]})
