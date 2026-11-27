T = "messen.flaechen"
AL, AR = "id.flaeche_raum.auslegen", "id.flaeche_raum.aus_dem_rechteck"

# ───────── einheitsquadrate ─────────
neu(T, "einheitsquadrate", "zwei_wege", Z(
    "Ein Rechteck besteht aus 6 Reihen mit je 12 Einheitsquadraten. Wie viele Einheitsquadrate sind es? Weg A: Rechne 6 · 12. Weg B: Teile das Rechteck in zwei gleich große Hälften, die jeweils 6 Quadrate breit sind, bestimme die Zahl in einer Hälfte und verdopple.",
    72, "6 * 12", "2 * (6 * 6)", "Wie viele Quadrate sind eine Hälfte breit? Wie viele Reihen hat sie?",
    "Weg A: 6 · 12 = 72. Weg B: Jede Hälfte ist 6 Quadrate breit und hat 6 Reihen: 6 · 6 = 36. Zwei Hälften: 2 · 36 = 72.",
    [(18, None, "6 und 12 addiert", "6 + 12"), (36, None, "nur eine Hälfte gezählt", "6 * 6"), (144, None, "12 · 12 gerechnet", "12 * 12")], "Quadrate"), regel=AL)
neu(T, "einheitsquadrate", "anwenden", Z(
    "Eine Terrasse ist 6 m lang und 4 m breit. Sie wird lückenlos mit quadratischen Platten von 50 cm Seitenlänge belegt. Nur ein rechteckiges Beet von 3 m Länge und 1 m Breite bleibt frei. Wie viele Platten braucht man?",
    84, "(6 * 2) * (4 * 2) - (3 * 2) * (1 * 2)", "(6 * 4 - 3 * 1) * 4", "Welche Einheit müssen Terrasse, Beet und Platte gemeinsam haben? Was wird nicht belegt?",
    "In 1 m passen 2 Platten. Terrasse: 6 · 2 = 12 Platten in der Länge, 4 · 2 = 8 in der Breite, zusammen 12 · 8 = 96 Platten. Beet: 3 · 2 = 6 mal 1 · 2 = 2, also 12 Platten. 96 − 12 = 84 Platten. Kontrolle: 24 m² − 3 m² = 21 m², auf 1 m² passen 4 Platten: 21 · 4 = 84.",
    [(21, None, "in m² gerechnet: 24 − 3", "6 * 4 - 3 * 1"), (96, None, "das Beet nicht abgezogen", "(6 * 2) * (4 * 2)"), (93, None, "das Beet in m² statt in Platten abgezogen: 96 − 3", "(6 * 2) * (4 * 2) - 3 * 1")], "Platten"), g="transfer", regel=AL)

# ───────── rechteck ─────────
neu(T, "rechteck", "bruecke", Z(
    "Die Tabelle zeigt fünf Rechtecke, die alle den Umfang 20 m haben. Wie groß ist der Flächeninhalt des Rechtecks mit der größten Fläche? Gib die Fläche in m² an.",
    25, "5 * 5", "(20 / 4) * (20 / 4)", "Berechne die Fläche jedes Rechtecks aus Länge mal Breite und vergleiche.",
    "Flächen: 9 · 1 = 9, 8 · 2 = 16, 7 · 3 = 21, 6 · 4 = 24, 5 · 5 = 25. Die größte Fläche hat das Quadrat mit 25 m².",
    [(9, None, "nur das erste Rechteck gerechnet", "9 * 1"), (20, "fb.auslegen.umfang_statt_flaeche", "den Umfang statt der Fläche genannt", "20"), (24, None, "das Rechteck 6 m × 4 m für das größte gehalten", "6 * 4")], "m²",
    grafik=TAB(["Länge in m", "Breite in m"], ["9", "1"], ["8", "2"], ["7", "3"], ["6", "4"], ["5", "5"])), regel=AL)
neu(T, "rechteck", "anwenden", Z(
    "Ein rechteckiger Spielplatz hat den Umfang 36 m und ist doppelt so lang wie breit. Wie groß ist seine Fläche in m²?",
    72, "(36 / 2 / 3 * 2) * (36 / 2 / 3)", "12 * 6", "Wie hängen Länge und Breite zusammen? Was sagt der Umfang über Länge plus Breite?",
    "Länge + Breite = 36 : 2 = 18 m. Das sind 3 gleiche Teile (Breite + zweimal Breite), ein Teil ist 6 m. Breite 6 m, Länge 12 m. Fläche: 12 · 6 = 72 m².",
    [(18, "fb.auslegen.umfang_statt_flaeche", "den halben Umfang als Fläche genannt", "36 / 2"), (81, None, "ein Quadrat mit gleichem Umfang angenommen", "9 * 9"), (36, "fb.auslegen.umfang_statt_flaeche", "den Umfang als Fläche genannt", "36")], "m²"), g="transfer", regel=AL)

# ───────── einheiten ─────────
neu(T, "einheiten", "anwenden", Z(
    "Ein Sportplatz hat eine Fläche von 7 200 m². Auf jedes Ar werden 2 kg Dünger gestreut. Wie viele kg Dünger werden gebraucht?",
    144, "7200 / 100 * 2", "72 * 2", "Wie viele m² hat ein Ar? Rechne zuerst die Fläche in Ar um.",
    "1 a = 100 m². 7 200 m² : 100 = 72 a. 72 · 2 kg = 144 kg.",
    [(14400, None, "mit m² statt mit Ar gerechnet", "7200 * 2"), (14.4, None, "durch 1 000 statt durch 100 umgerechnet", "7200 / 1000 * 2"), (72, None, "die Fläche in Ar genannt", "7200 / 100")], "kg"))
neu(T, "einheiten", "zwei_wege", Z(
    "Wie viele m² sind 3 ha? Weg A: Rechne mit 1 ha = 10 000 m². Weg B: Ein Quadrat mit 100 m Seitenlänge hat 1 ha. Berechne die Fläche von 3 solchen Quadraten in m².",
    30000, "3 * 10000", "3 * (100 * 100)", "Wie groß ist die Fläche eines Quadrats mit der Seitenlänge 100 m?",
    "Weg A: 3 · 10 000 m² = 30 000 m². Weg B: Ein Quadrat hat 100 m · 100 m = 10 000 m². Drei Quadrate: 30 000 m².",
    [(3000, None, "mit 1 ha = 1 000 m² gerechnet", "3 * 1000"), (300000, None, "mit 1 ha = 100 000 m² gerechnet", "3 * 100000"), (300, None, "mit 1 ha = 100 m² gerechnet", "3 * 100")], "m²"), g="verknuepfen")

# ───────── kommaschreibweise ─────────
neu(T, "kommaschreibweise", "umkehren", Z(
    "Eine Fläche wurde zuerst in dm² angegeben und dann in m² umgerechnet. Das Ergebnis lautet 8,4 m². Welche Zahl stand vorher in dm²?",
    840, "8.4 * 100", "8.4 * 10 * 10", "Wie viele dm² hat ein m²? Mache die Umrechnung rückgängig.",
    "1 m² = 100 dm². Rückwärts wird mit 100 malgenommen: 8,4 · 100 = 840 dm². Probe: 840 dm² : 100 = 8,4 m².",
    [(84, None, "mit 10 statt mit 100 malgenommen", "8.4 * 10"), (8400, None, "mit 1 000 malgenommen", "8.4 * 1000"), (0.084, None, "durch 100 geteilt statt malgenommen", "8.4 / 100")], "dm²"), g="umkehr")
neu(T, "kommaschreibweise", "fehler_detektiv", FD(
    "Mia berechnet 3,2 m² + 45 dm² und gibt das Ergebnis in m² an.",
    [("1 m² sind 100 dm², also sind 45 dm² gleich 0,45 m².", 45 / 100 == 0.45, True, "Zeile 1 stimmt: 45 dm² : 100 = 0,45 m². Der Fehler steckt später."),
     ("3,2 m² + 0,45 m² = 3,47 m².", round(3.2 + 0.45, 2) == 3.47, True),
     ("Das Ergebnis ist 3,47 m².", True, True, "Zeile 3 übernimmt nur das Ergebnis aus Zeile 2. Der Fehler liegt schon in Zeile 2.")],
    "Prüfe jede Zeile für sich und rechne beim Addieren Komma unter Komma nach. Welche Zeile enthält zuerst einen Fehler?",
    "3,20 + 0,45 = 3,65. Richtig: 3,65 m². Der erste Fehler steht in Zeile 2."))

# ───────── zerlegen ─────────
neu(T, "zerlegen", "anwenden", Z(
    "Ein rechteckiger Garten ist 12 m lang und 9 m breit. In einer Ecke liegt ein rechteckiger Teich, der 5 m lang und 4 m breit ist. Wie groß ist die Fläche des Gartens ohne den Teich?",
    88, "12 * 9 - 5 * 4", "108 - 20", "Berechne die Fläche des ganzen Rechtecks und die des Teichs. Was bleibt?",
    "Ganzer Garten: 12 · 9 = 108 m². Teich: 5 · 4 = 20 m². Rest: 108 − 20 = 88 m².",
    [(108, None, "den Teich nicht abgezogen", "12 * 9"), (128, None, "den Teich dazu addiert", "12 * 9 + 20"), (20, None, "nur die Fläche des Teichs genannt", "5 * 4")], "m²"), regel=AR)
neu(T, "zerlegen", "umkehren", Z(
    "Aus einem Rechteck, das 10 m lang und 8 m breit ist, wird an einer Ecke ein kleineres Rechteck herausgeschnitten. Dieses ist 4 m lang. Die übrige Fläche beträgt 68 m². Wie breit ist das herausgeschnittene Rechteck?",
    3, "(10 * 8 - 68) / 4", "12 / 4", "Welche Fläche hat das ganze Rechteck? Was sagt die übrige Fläche über das herausgeschnittene Stück?",
    "Ganzes Rechteck: 10 · 8 = 80 m². Herausgeschnitten: 80 − 68 = 12 m². Breite: 12 : 4 = 3 m. Probe: 4 · 3 = 12 und 80 − 12 = 68.",
    [(12, None, "die herausgeschnittene Fläche als Breite genannt", "80 - 68"), (17, None, "68 durch 4 geteilt", "68 / 4"), (8, None, "die Breite des ganzen Rechtecks genannt", "8")], "m"), g="rueckwaerts", regel=AR)

# ───────── sachaufgaben ─────────
neu(T, "sachaufgaben", "bruecke", Z(
    "Die Tabelle zeigt drei Bodenbeläge mit ihrem Preis je m². Ein Zimmer ist 6 m lang und 4 m breit. Wie viel Euro kostet der günstigste Belag für das ganze Zimmer?",
    288, "6 * 4 * 12", "24 * 12", "Berechne zuerst die Fläche des Zimmers. Welcher Belag ist je m² am billigsten?",
    "Fläche: 6 · 4 = 24 m². Der günstigste Belag ist Teppich mit 12 € je m². 24 · 12 = 288 €.",
    [(432, None, "mit dem Preis des Laminats gerechnet", "24 * 18"), (840, None, "mit dem Preis des Parketts gerechnet", "24 * 35"), (12, None, "nur den Preis je m² genannt", "12")], "€",
    grafik=TAB(["Belag", "Preis je m²"], ["Laminat", "18 €"], ["Teppich", "12 €"], ["Parkett", "35 €"])))
neu(T, "sachaufgaben", "zwei_wege", Z(
    "Ein Gartenweg ist 6 m lang und 80 cm breit. Er wird lückenlos mit quadratischen Platten von 20 cm Seitenlänge belegt. Wie viele Platten braucht man? Weg A: Teile die Fläche des Wegs durch die Fläche einer Platte (beides in cm²). Weg B: Bestimme, wie viele Platten in der Länge und wie viele in der Breite nebeneinander passen. Gib die Zahl der Platten an.",
    120, "(600 * 80) / (20 * 20)", "(600 / 20) * (80 / 20)", "Rechne alle Maße in cm. Wie viele Platten von 20 cm passen in 6 m?",
    "Weg A: Weg 600 cm · 80 cm = 48 000 cm², Platte 20 · 20 = 400 cm². 48 000 : 400 = 120. Weg B: 600 : 20 = 30 Platten in der Länge, 80 : 20 = 4 in der Breite. 30 · 4 = 120.",
    [(34, None, "Platten in der Länge und in der Breite addiert", "30 + 4"), (4.8, None, "die Fläche in m² als Zahl der Platten genommen", "6 * 0.8"), (480, None, "durch 100 statt durch 400 geteilt", "48000 / 100")], "Platten"), g="verknuepfen", regel=AL)

# ───────── verstehen ─────────
neu(T, "verstehen", "umkehren", Z(
    "Ein Quadrat und ein Rechteck haben denselben Flächeninhalt von 36 cm². Das Rechteck ist 9 cm lang. Wie breit ist das Rechteck?",
    4, "36 / 9", "6 * 6 / 9", "Fläche = Länge mal Breite. Mache das Malnehmen mit 9 rückgängig.",
    "36 cm² = 9 cm · Breite, also Breite = 36 : 9 = 4 cm. Probe: 9 · 4 = 36.",
    [(27, None, "9 von 36 abgezogen", "36 - 9"), (6, None, "die Seite des Quadrats genannt", "6"), (45, None, "36 und 9 addiert", "36 + 9")], "cm"), g="umkehr")
neu(T, "verstehen", "zwei_wege", Z(
    "Bei einem Rechteck mit 5 cm Länge und 7 cm Breite werden Länge und Breite verdoppelt. Wie oft so groß wird dabei der Flächeninhalt und wie oft so groß der Umfang? Weg A: Berechne alte und neue Fläche und alten und neuen Umfang und teile jeweils. Weg B: Überlege, mit welcher Zahl jede Seite malgenommen wird und was das für Fläche und Umfang bedeutet. Gib die Summe der beiden Faktoren an.",
    6, "(10 * 14) / (5 * 7) + (2 * (10 + 14)) / (2 * (5 + 7))", "2 * 2 + 2", "Vergleiche jeweils die neue mit der alten Größe: Wie oft passt die alte in die neue?",
    "Weg A: Fläche 5 · 7 = 35 cm² wird 10 · 14 = 140 cm², das ist 4-mal so viel. Umfang 2 · (5 + 7) = 24 cm wird 2 · (10 + 14) = 48 cm, das ist 2-mal so viel. 4 + 2 = 6. Weg B: Jede Seite wird 2-mal so lang. Der Umfang besteht aus Seiten, er wird 2-mal so groß. Die Fläche ist Länge mal Breite, sie wird 2 · 2 = 4-mal so groß. 4 + 2 = 6.",
    [(4, None, "für Fläche und Umfang jeweils den Faktor 2 genommen: 2 + 2", "2 + 2"), (8, None, "den Faktor der Fläche auch für den Umfang genommen: 4 + 4", "2 * 2 + 2 * 2"), (2, None, "nur den Faktor des Umfangs genannt", "2")]), g="verknuepfen")
