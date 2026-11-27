T = "stochastik.grundbegriffe"

# ───────── begriffe: Brücke ─────────
produkte = [a * b for a in (1, 2, 3) for b in (1, 2, 3, 4)]
prim = [p for p in produkte if p in (2, 3, 5, 7, 11)]
assert len(produkte) == 12 and len(prim) == 4 and 12 - 4 == 8 and len([p for p in produkte if p in (1, 2, 3, 5, 7, 11)]) == 5
Z(T, "begriffe", "bruecke",
  "Zwei Glücksräder werden gedreht. Rad A zeigt die Zahlen 1, 2, 3, Rad B zeigt die Zahlen 1, 2, 3, 4. Die Tabelle zeigt für jedes Zahlenpaar das Produkt. Jedes Feld der Tabelle ist ein Ergebnis. "
  "Das Ereignis E lautet: „Das Produkt ist eine Primzahl.“ Wie viele Ergebnisse gehören zum Gegenereignis von E?",
  8, "12 - 4", "12 - (2 + 1 + 1)",
  "Zähle zuerst die Felder, in denen eine Primzahl steht. Eine Primzahl hat genau zwei Teiler. Das Gegenereignis enthält alle übrigen Felder.",
  "Die Tabelle hat 3 · 4 = 12 Felder. Primzahlen als Produkt: 2 (1 · 2), 3 (1 · 3), 2 (2 · 1) und 3 (3 · 1). Das sind 4 Felder. Das Gegenereignis von E enthält die übrigen 12 − 4 = 8 Felder. "
  "Die 1 ist keine Primzahl.",
  [(4, "2 + 1 + 1", "die Ergebnisse von E gezählt statt die des Gegenereignisses"),
   (12, "3 * 4", "alle Ergebnisse gezählt"),
   (7, "12 - 5", "die 1 als Primzahl mitgezählt")],
  "id.daten.anteil", einheit="Ergebnisse",
  grafik={"typ": "tabelle", "kopf": ["Rad A \\ Rad B", "1", "2", "3", "4"],
          "zeilen": [["1", "1", "2", "3", "4"], ["2", "2", "4", "6", "8"], ["3", "3", "6", "9", "12"]]})

# ───────── rel_haeufigkeit: Umkehren ─────────
assert 0.3 * 200 - 0.25 * 80 == 40
Z(T, "rel_haeufigkeit", "umkehren",
  "Ein Glücksrad wird gedreht. Nach 80 Drehungen ist die relative Häufigkeit von Rot 0,25. Das Rad wird weitergedreht. Nach insgesamt 200 Drehungen ist die relative Häufigkeit von Rot 0,3. "
  "Wie oft fiel Rot in den letzten 120 Drehungen?",
  40, "0.3 * 200 - 0.25 * 80", "60 - 20",
  "Wie oft ist Rot nach 80 Drehungen gefallen? Wie oft nach 200 Drehungen? Aus einer relativen Häufigkeit erhältst du die Anzahl durch Malnehmen mit der Zahl der Drehungen.",
  "Nach 80 Drehungen: 0,25 · 80 = 20-mal Rot. Nach 200 Drehungen: 0,3 · 200 = 60-mal Rot. In den letzten 120 Drehungen also 60 − 20 = 40-mal. Probe: 20 + 40 = 60 und 60 : 200 = 0,3.",
  [(60, "0.3 * 200", "die Gesamtzahl der Rot-Treffer genannt"),
   (20, "0.25 * 80", "nur die Rot-Treffer der ersten 80 Drehungen genannt"),
   (36, "0.3 * 120", "die relative Häufigkeit 0,3 auf die letzten 120 Drehungen angewandt")],
  "id.daten.anteil", einheit="mal")

# ───────── darstellen: Anwenden ─────────
assert 28 - (17 + 15 - 6) == 2
Z(T, "darstellen", "anwenden",
  "In einer Klasse mit 28 Kindern gehen 17 Kinder in den Chor und 15 Kinder in die Theater-AG. 6 Kinder gehen in beide Gruppen. Wie viele Kinder gehen in keine der beiden Gruppen? "
  "Eine Vierfeldertafel (Chor ja/nein, Theater ja/nein) hilft.",
  2, "28 - (17 + 15 - 6)", "28 - (11 + 6 + 9)",
  "Fülle die Vierfeldertafel: Wie viele sind nur im Chor, wie viele nur im Theater, wie viele in beiden?",
  "Nur Chor: 17 − 6 = 11. Nur Theater: 15 − 6 = 9. Beide: 6. Zusammen in mindestens einer Gruppe: 11 + 9 + 6 = 26. Keine der beiden Gruppen: 28 − 26 = 2 Kinder.",
  [(-4, "28 - (17 + 15)", "die 6 Kinder in beiden Gruppen doppelt gezählt (ergibt eine negative Zahl)"),
   (6, "6", "die Zahl der Kinder in beiden Gruppen genannt"),
   (11, "28 - 17", "nur die Chorkinder abgezogen")],
  "id.daten.teil_ganzes", einheit="Kinder")
