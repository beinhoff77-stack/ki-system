T = "gleichungen.bruch"

# ───────── definitionsmenge: Anwenden ─────────
assert 90 / (24 - 6) == 5
Z(T, "definitionsmenge", "anwenden",
  "Ein Boot fährt auf einem Fluss gegen die Strömung. Die Strömung hat 6 km/h. Das Boot schafft in ruhigem Wasser v km/h und kommt gegen die Strömung voran. "
  "Die Fahrzeit für 90 km beträgt 90/(v − 6) Stunden. Die Fahrt dauert 5 Stunden. Wie schnell ist das Boot in ruhigem Wasser?",
  24, "90 / 5 + 6", "6 + 90 / 5",
  "Welche Werte von v sind rechnerisch erlaubt, welche passen zur Sache? Stelle dann die Gleichung auf: Fahrzeit = 5 Stunden.",
  "Rechnerisch muss der Nenner v − 6 von 0 verschieden sein, also v ≠ 6. Sachlich kommt das Boot nur voran, wenn v > 6 ist. Gleichung: 90/(v − 6) = 5. Mit (v − 6) multiplizieren: 90 = 5(v − 6). Dann 90 : 5 = 18 = v − 6, also v = 24 km/h. Die Lösung 24 erfüllt v > 6. Probe: 90 : (24 − 6) = 90 : 18 = 5 Stunden.",
  [(18, "90 / 5", "bei v − 6 stehen geblieben und die Strömung nicht dazugerechnet"),
   (12, "90 / 5 - 6", "die 6 abgezogen statt addiert"),
   (30, "5 * 6", "Fahrzeit mal Strömung gerechnet")],
  "id.algebra.erlaubte_zahlen", einheit="km/h")

# ───────── ein_bruch: Fehler-Detektiv (Bruchgleichung mit x im Nenner) ─────────
def im_def(x):
    return x != 0


def gleichung1(x):          # (6x + 12)/(3x) = 4
    return F(6) * x / (3 * x) + F(12) / (3 * x) == 4


def gleichung2(x):          # (2x + 12)/x = 4
    return (2 * x + 12) / x == 4


loes1 = [x for x in map(F, range(-30, 31)) if im_def(x) and gleichung1(x)]
loes2 = [x for x in map(F, range(-30, 31)) if im_def(x) and gleichung2(x)]
assert loes1 == [2] and loes2 == [6] and 6 != 0
assert not all(F(6) * x / (3 * x) + F(12) / (3 * x) == (2 * x + 12) / x for x in map(F, (1, 2, 3, 5)))       # Zeile 1 ist falsch
assert all((2 * x + 12) == 4 * x for x in loes2) and F(2 * 6 + 12) == 4 * 6          # Zeile 2: mit x multipliziert, 2x + 12 = 4x gibt x = 6
FD(T, "ein_bruch",
   "Kim löst (6x + 12)/(3x) = 4 mit x ≠ 0.",
   [("Ich kürze mit 3: (6x + 12)/(3x) = (2x + 12)/x, die Gleichung lautet also (2x + 12)/x = 4.", all(F(6) * x / (3 * x) + F(12) / (3 * x) == (2 * x + 12) / x for x in map(F, (1, 2, 3, 5)))),
    ("Mit x multiplizieren (x ≠ 0): 2x + 12 = 4x, also 12 = 2x und x = 6.", loes2 == [6] and 2 * 6 + 12 == 4 * 6),
    ("Die Lösung 6 ist erlaubt, denn 6 ≠ 0. Also ist L = {6}.", im_def(F(6)) and loes2 == [6])],
   "Setze die Lösung in die Gleichung am Anfang ein.",
   "Gekürzt werden darf nur, wenn der ganze Zähler durch 3 geteilt wird: (6x + 12)/(3x) = (2x + 4)/x. In Zeile 1 wurde nur 6x durch 3 geteilt, die 12 blieb stehen. "
   "Die Zeilen 2 und 3 rechnen mit der falschen Zeile 1 richtig weiter. Richtig: 2x + 4 = 4x, also x = 2. Probe: (12 + 12)/6 = 4.",
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
   (100, "2 / (2 / 100)", "beim Addieren der Brüche Zähler und Nenner addiert (1/60 + 1/40 = 2/100), also v = 2 : (2/100)"),
   (24, "120 / 5", "den Faktor 2 (Hin- und Rückweg) vergessen: 1/v statt 2/v")],
  None, einheit="km/h")

# ───────── verhaeltnis: Umkehren ─────────
assert 300 * 2 // 5 == 120 and (120 + 120) * 5 == 300 * 4
Z(T, "verhaeltnis", "umkehren",
  "In einer Mischung ist das Verhältnis Mehl : Zucker = 5 : 2. Nach dem Zugeben von 120 g Zucker ist das Verhältnis Mehl : Zucker = 5 : 4. Stelle mit m für die Mehlmenge eine Verhältnisgleichung auf und löse sie. Wie viel Gramm Mehl sind in der Mischung?",
  300, "120 / (4 - 2) * 5", "120 / (4 / 5 - 2 / 5)",
  "Wie viel Gramm Zucker gehören vorher zu m Gramm Mehl? Wie viel Zucker ist es nachher? Nachher gilt Mehl : Zucker = 5 : 4.",
  "Mehl m Gramm. Vorher ist der Zucker 2m/5 Gramm, nachher 2m/5 + 120 Gramm. Verhältnisgleichung: m/(2m/5 + 120) = 5/4. Über Kreuz: 4m = 5 · (2m/5 + 120) = 2m + 600, also 2m = 600 und m = 300 g. "
  "Kontrolle mit Teilen: Dazugekommen sind 4 − 2 = 2 Teile Zucker, das sind 120 g, ein Teil ist 60 g, Mehl 5 · 60 = 300 g. Probe: Zucker vorher 120 g, nachher 240 g; 300 : 240 = 5 : 4.",
  [(240, "4 * 60", "die Zuckermenge nachher (240 g) genannt statt der Mehlmenge"),
   (60, "120 / 2", "nur die Größe eines Teils (60 g) genannt"),
   (600, "5 * 120", "die 120 g als einen Teil genommen")],
  None, einheit="g")

# ───────── graphisch: Umkehren ─────────
assert 12 / -4 + 4 == -3 + 4 == 1 and all(12 / x == x + 1 for x in (3, -4))
Z(T, "graphisch", "umkehren",
  "Die Gerade y = x + b schneidet den Graphen von y = 12/x an der Stelle x = −4. Sie schneidet ihn noch ein zweites Mal bei einer positiven Zahl x. "
  "Bestimme zuerst b. Zeichne dann beide Graphen, lies die positive Schnittstelle ab und kontrolliere sie mit einer Wertetabelle. Wie lautet die x-Koordinate des zweiten Schnittpunkts?",
  3, "4 - 1", "12 / 4",
  "Wie groß ist y = 12/x bei x = −4? Dieser y-Wert muss auch auf der Geraden liegen. Daraus folgt b. Die Schnittstelle liest du dort ab, wo sich beide Graphen treffen.",
  "Bei x = −4 ist y = 12 : (−4) = −3. Auf der Geraden gilt −3 = −4 + b, also b = 1. Die Gerade ist y = x + 1. Zeichnet man y = 12/x und y = x + 1, so treffen sich die Graphen für x > 0 bei x = 3. Kontrolle mit der Wertetabelle: x = 1: 12 und 2, x = 2: 6 und 3, x = 3: 4 und 4. "
  "Einsetzen von x = 3: 12/3 = 4 und 3 + 1 = 4, beide Funktionen haben dort den Wert 4. Der zweite Schnittpunkt liegt bei x = 3.",
  [(1, "-3 + 4", "nur b bestimmt und nicht den zweiten Schnittpunkt"),
   (-4, "-4", "den bekannten ersten Schnittpunkt noch einmal genannt"),
   (-3, "12 / (-4)", "den y-Wert des ersten Schnittpunkts genannt")],
  None)
