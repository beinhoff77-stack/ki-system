T = "gleichungen.bruch"

# ───────── definitionsmenge: Anwenden ─────────
assert 90 / (24 - 6) == 5
Z(T, "definitionsmenge", "anwenden",
  "Ein Boot fährt auf einem Fluss gegen die Strömung. Die Strömung hat 6 km/h. Das Boot schafft in ruhigem Wasser v km/h (v ist größer als 6, sonst käme es nicht voran). "
  "Die Fahrzeit für 90 km beträgt 90/(v − 6) Stunden. Die Fahrt dauert 5 Stunden. Wie schnell ist das Boot in ruhigem Wasser?",
  24, "90 / 5 + 6", "6 + 90 / 5",
  "Der Nenner v − 6 darf nicht 0 sein. Multipliziere beide Seiten der Gleichung 90/(v − 6) = 5 mit dem Nenner.",
  "Gleichung: 90/(v − 6) = 5 mit v ≠ 6. Mit (v − 6) multiplizieren: 90 = 5(v − 6). Dann 90 : 5 = 18 = v − 6, also v = 24 km/h. Probe: 90 : (24 − 6) = 90 : 18 = 5 Stunden.",
  [(18, "90 / 5", "bei v − 6 stehen geblieben und die Strömung nicht dazugerechnet"),
   (12, "90 / 5 - 6", "die 6 abgezogen statt addiert"),
   (30, "5 * 6", "Fahrzeit mal Strömung gerechnet")],
  "id.algebra.erlaubte_zahlen", einheit="km/h")

# ───────── ein_bruch: Fehler-Detektiv ─────────
FD(T, "ein_bruch",
   "Kim löst (2x + 6)/2 = 7.",
   [("Ich kürze die 2 im Bruch links: (2x + 6)/2 = x + 6, die Gleichung lautet also x + 6 = 7.", aequi("(2*x+6)/2", "7", "x+6", "7")),
    ("Von beiden Seiten 6 abziehen: x = 7 − 6 = 1.", aequi("x+6", "7", "x", "1")),
    ("Die Lösungsmenge ist L = {1}.", aequi("x", "1", "x", "1"))],
   "Setze die Lösung in die Gleichung am Anfang ein. ",
   "Gekürzt werden darf nur, wenn der ganze Zähler durch 2 geteilt wird: (2x + 6)/2 = x + 3. In Zeile 1 wurde nur die 2x gekürzt, die 6 blieb stehen. "
   "Die Zeilen 2 und 3 rechnen mit der falschen Zeile 1 richtig weiter. Richtig: x + 3 = 7, also x = 4. Probe: (8 + 6)/2 = 7.",
   "rr.kuerzen", "nur aus einem Summanden des Zählers gekürzt (aus einer Summe gekürzt)")

# ───────── hauptnenner: Anwenden ─────────
Z(T, "hauptnenner", "anwenden",
  "Ein Auto fährt eine Strecke hin mit 60 km/h und denselben Weg zurück mit 40 km/h. Die Länge s der einfachen Strecke ist nicht bekannt. "
  "Mit welcher gleichbleibenden Geschwindigkeit v (in km/h) müsste es Hin- und Rückweg fahren, um für beide Wege zusammen genauso lange zu brauchen?",
  48, "240 / 5", "2 / (1 / 60 + 1 / 40)",
  "Zeit = Weg : Geschwindigkeit. Stelle für beide Fahrten die Gesamtzeit auf und setze die Zeiten gleich.",
  "Gleichung: s/60 + s/40 = 2s/v. Durch s teilen: 1/60 + 1/40 = 2/v. Mit 120v multiplizieren: 2v + 3v = 240, also 5v = 240 und v = 48 km/h. "
  "Probe: Mit s = 120 km: hin 2 h, zurück 3 h, zusammen 5 h; 240 km : 5 h = 48 km/h.",
  [(50, "(60 + 40) / 2", "den Mittelwert der beiden Geschwindigkeiten genommen"),
   (100, "2 / (2 / 100)", "beim Addieren der Brüche Zähler und Nenner addiert: 1/60 + 1/40 = 2/100"),
   (24, "120 / 5", "den Faktor 2 (Hin- und Rückweg) vergessen: 1/v statt 2/v")],
  "rr.bruchrechnen", einheit="km/h")

# ───────── verhaeltnis: Umkehren ─────────
assert 300 * 2 // 5 == 120 and (120 + 120) * 5 == 300 * 4
Z(T, "verhaeltnis", "umkehren",
  "In einer Mischung ist das Verhältnis Mehl : Zucker = 5 : 2. Nach dem Zugeben von 120 g Zucker ist das Verhältnis Mehl : Zucker = 5 : 4. Wie viel Gramm Mehl sind in der Mischung?",
  300, "120 / (4 - 2) * 5", "120 / (4 / 5 - 2 / 5)",
  "Wie viele Teile Zucker sind dazugekommen? Wie viel Gramm ist ein Teil?",
  "Vorher 5 Teile Mehl, 2 Teile Zucker, nachher 5 Teile Mehl und 4 Teile Zucker. Dazugekommen sind 4 − 2 = 2 Teile Zucker, und das sind 120 g. Ein Teil ist 60 g. Mehl: 5 · 60 = 300 g. "
  "Probe: Zucker vorher 2 · 60 = 120 g, nachher 240 g; 300 : 240 = 5 : 4.",
  [(240, "4 * 60", "den neuen Zuckeranteil genannt statt der Mehlmenge"),
   (60, "120 / 2", "nur die Größe eines Teils genannt"),
   (600, "5 * 120", "die 120 g als einen Teil genommen")],
  "rr.verhaeltnis", einheit="g")

# ───────── graphisch: Umkehren ─────────
assert 12 / -4 + 4 == -3 + 4 == 1 and all(12 / x == x + 1 for x in (3, -4))
Z(T, "graphisch", "umkehren",
  "Die Gerade y = x + b schneidet den Graphen von y = 12/x an der Stelle x = −4. Sie schneidet ihn noch ein zweites Mal bei einer positiven Zahl x. "
  "Bestimme zuerst b. Suche dann mit einer Wertetabelle von y = 12/x und y = x + b die x-Koordinate des zweiten Schnittpunkts.",
  3, "12 / 4", "4 - 1",
  "Wie groß ist y = 12/x bei x = −4? Dieser y-Wert muss auch auf der Geraden liegen. Daraus folgt b.",
  "Bei x = −4 ist y = 12 : (−4) = −3. Auf der Geraden gilt −3 = −4 + b, also b = 1. Die Gerade ist y = x + 1. Wertetabelle für x > 0: x = 1: 12 und 2, x = 2: 6 und 3, x = 3: 4 und 4. Bei x = 3 sind beide Werte gleich. "
  "Der zweite Schnittpunkt liegt bei x = 3.",
  [(1, "-3 + 4", "nur b bestimmt und nicht den zweiten Schnittpunkt"),
   (-4, "-4", "den bekannten ersten Schnittpunkt noch einmal genannt"),
   (-3, "12 / (-4)", "den y-Wert des ersten Schnittpunkts genannt")],
  "id.funktionen.gleichung_form")
