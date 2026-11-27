T = "terme.quadratische_extreme"
GF = "id.funktionen.gleichung_form"
# ───────── ergaenzen ─────────
neu(T, "ergaenzen", "anwenden", Z(
    "Ein Quadrat hat die Seitenlänge x m. An zwei benachbarten Seiten wird je ein Streifen der Breite 3 m angelegt. Quadrat und beide Streifen haben zusammen die Fläche x² + 6x. An der Ecke fehlt noch ein kleines Quadrat, damit ein großes Quadrat entsteht. Wie lang ist die Seite des großen Quadrats in Metern, wenn x = 7 ist?",
    10, "7 + 3", "7 + 6 / 2", "Das große Quadrat besteht aus dem Quadrat mit Seite x, zwei Streifen und dem kleinen Eckquadrat. Welche Länge hat jede Seite des großen Quadrats?",
    "Das kleine Eckquadrat hat die Seitenlänge 3 m und die Fläche 9 m². Das große Quadrat hat die Fläche x² + 6x + 9 = (x + 3)². Seine Seite ist x + 3. Für x = 7 ist das 10 m.",
    [(13, None, "die Streifenbreite 6 statt 3 zur Seite addiert", "7 + 6"), (7, None, "nur die Seitenlänge x des kleinen Quadrats angegeben", "7"), (16, None, "die Streifenbreite dreimal addiert", "7 + 3 * 3")], "m"), g="einkleidung", regel="rr.potenz")
assert gl("x**2+6*x+9", "(x+3)**2")
neu(T, "ergaenzen", "zwei_wege", Z(
    "Die Funktion f(x) = x² + 8x + 5 soll in die Form (x + a)² + b gebracht werden. Welche Zahl ist b? Weg A: quadratische Ergänzung. Weg B: (x + a)² + b ausmultiplizieren und die Zahlen vor x sowie die Zahlen ohne x vergleichen.",
    -11, "5 - 4 ** 2", "5 - 8 ** 2 / 4", "Beide Wege müssen dieselbe Zahl b ergeben. Aus der Zahl vor x erhältst du zuerst a.",
    "Weg A: x² + 8x + 16 − 16 + 5 = (x + 4)² − 11. Weg B: (x + a)² + b = x² + 2ax + a² + b. Aus 2a = 8 folgt a = 4. Aus a² + b = 5 folgt 16 + b = 5, also b = −11. Probe: (x + 4)² − 11 = x² + 8x + 5.",
    [(-16, None, "nur den Ausgleich −16 angegeben, die Zahl 5 vergessen", "-(4 ** 2)"), (21, None, "16 addiert statt abgezogen", "16 + 5"), (-3, None, "5 minus 8 gerechnet", "5 - 8")]), g="verknuepfen", regel="rr.potenz")
assert gl("x**2+8*x+5", "(x+4)**2-11")
# ───────── scheitelform ─────────
neu(T, "scheitelform", "anwenden", Z(
    "Ein Springbrunnenstrahl verläuft auf der Parabel h(x) = −0,5·(x − 3)² + 4,5 (x ist der waagerechte Abstand von der Düse in Metern, h die Höhe in Metern). Um wie viele Meter liegt der höchste Punkt des Strahls höher als der Strahl bei x = 1?",
    2, "4.5 - (-0.5 * (1 - 3) ** 2 + 4.5)", "0.5 * 4", "Lies aus der Scheitelform die größte Höhe ab. Berechne dann h(1).",
    "Der Scheitel liegt bei (3 | 4,5): Der Strahl ist höchstens 4,5 m hoch. h(1) = −0,5 · (−2)² + 4,5 = −2 + 4,5 = 2,5. Unterschied: 4,5 − 2,5 = 2 m.",
    [(2.5, None, "nur die Höhe bei x = 1 angegeben", "-0.5 * (1 - 3) ** 2 + 4.5"), (4.5, None, "nur die größte Höhe angegeben", "4.5"), (8, "fb.gleichung_form.falsche_richtung_verschoben", "die Klammer mit Plus statt mit Minus gelesen und h bei x = 1 falsch berechnet", "4.5 - (-0.5 * (1 + 3) ** 2 + 4.5)")], "m"), g="einkleidung", regel=GF)
neu(T, "scheitelform", "umkehren", Z(
    "Die Parabel y = a·(x − 2)² + 1 geht durch den Punkt P(4 | 9). Welche Zahl ist a?",
    2, "(9 - 1) / (4 - 2) ** 2", 2, "Setze die Koordinaten von P ein. Rechne zuerst die Klammer und das Quadrat aus.",
    "Aus 9 = a · (4 − 2)² + 1 folgt 9 = 4a + 1, also 4a = 8 und a = 2. Probe: y = 2(x − 2)² + 1 gibt für x = 4 den Wert 2 · 4 + 1 = 9.",
    [(8, None, "9 − 1 gerechnet und nicht durch 4 geteilt", "9 - 1"), (4, "fb.potenz.basis_mal_hochzahl", "das Quadrat der Klammer nicht gebildet", "(9 - 1) / 2"), (2.25, None, "die 1 nicht abgezogen: 9 durch 4 geteilt", "9 / 4")]), g="rueckwaerts", regel=GF)
# ───────── extremwert ─────────
neu(T, "extremwert", "bruecke", Z(
    "Die Funktion f(x) = x² + bx + c hat die Nullstellen 1 und 5. Welchen kleinsten Funktionswert hat f für alle reellen Zahlen x?",
    -4, "(3 - 1) * (3 - 5)", "3 ** 2 - 6 * 3 + 5", "Der Scheitel einer Parabel liegt auf ihrer Symmetrieachse.",
    "Die Parabel ist nach oben geöffnet und hat die Form f(x) = (x − 1)(x − 5). Der Scheitel liegt in der Mitte der beiden Nullstellen, also bei x = 3. Dort ist f(3) = 2 · (−2) = −4. Probe: f(x) = x² − 6x + 5 gibt f(3) = 9 − 18 + 5 = −4.",
    [(3, None, "die Stelle des Scheitels statt den Funktionswert angegeben", "3"), (4, None, "das Vorzeichen übersehen: Betrag des Funktionswerts angegeben", "(3 - 1) * (5 - 3)"), (-3, None, "die Mitte falsch bei 4 statt bei 3 gesetzt und dort eingesetzt", "(4 - 1) * (4 - 5)")]), g="darstellung", regel=GF)
assert gl("x**2-6*x+5", "(x-1)*(x-5)")
neu(T, "extremwert", "fehler_detektiv", FD(
    "Kim sucht den größten Wert von g(x) = −x² + 6x − 2 für alle reellen Zahlen x.",
    [("Ausklammern von −1 bei den ersten beiden Gliedern: g(x) = −(x² − 6x) − 2.", gl("-x**2+6*x-2", "-(x**2-6*x)-2"), True),
     ("Ergänzen mit 9 und −9: g(x) = −((x − 3)² − 9) − 2.", gl("-x**2+6*x-2", "-((x-3)**2-9)-2"), True),
     ("Zusammengefasst: g(x) = −(x − 3)² + 7.", gl("-x**2+6*x-2", "-(x-3)**2+7"), True),
     ("Der größte Wert ist 7. Er wird bei x = 7 angenommen.", -(7 ** 2) + 6 * 7 - 2 == 7, -(7 ** 2) + 6 * 7 - 2 == 7)],
    "Wo ist (x − 3)² gleich null? Setze diese Stelle in g ein.",
    "Der größte Wert 7 stimmt. Aber (x − 3)² ist null bei x = 3 und nicht bei x = 7. Probe: g(3) = −9 + 18 − 2 = 7, aber g(7) = −49 + 42 − 2 = −9. Der größte Wert 7 wird bei x = 3 angenommen."), g="fehler", regel=GF)
# ───────── mit_faktor ─────────
neu(T, "mit_faktor", "umkehren", Z(
    "Die Funktion f(x) = a·x² − 12x + 5 mit a ≠ 0 hat ihren Scheitel bei x = 3. Welche Zahl ist a?",
    2, "12 / (2 * 3)", "6 / 3", "Klammere a bei den Gliedern mit x aus und ergänze dann in der Klammer quadratisch. Was steht dann in der Klammer neben x?",
    "f(x) = a(x² − (12/a)·x) + 5. Die Klammer wird zu (x − 6/a)² − 36/a². Der Scheitel liegt also bei x = 6/a. Aus 6/a = 3 folgt a = 2. Probe: f(x) = 2x² − 12x + 5 = 2(x − 3)² − 13, der Scheitel liegt bei x = 3.",
    [(6, None, "die Zahl 12 durch 2 geteilt und die Stelle 3 nicht benutzt", "12 / 2"), (4, None, "die Zahl 12 durch die Stelle 3 geteilt, ohne zu halbieren", "12 / 3"), (0.5, None, "den Bruch verkehrt herum gerechnet: Stelle durch 6", "3 / 6")]), g="umkehr", regel=GF)
assert gl("2*x**2-12*x+5", "2*(x-3)**2-13")
neu(T, "mit_faktor", "anwenden", Z(
    "Ein Laden verkauft einen Artikel zum Preis p (in Euro). Der Gewinn pro Tag beträgt G(p) = −2p² + 20p − 30 Euro. Dieses Modell gilt nur für Preise mit 3 ≤ p ≤ 4. Wie groß ist der größte Gewinn pro Tag in Euro, den der Laden mit einem Preis aus diesem Bereich erreichen kann?",
    18, "-2 * 4 ** 2 + 20 * 4 - 30", "-2 * (4 - 5) ** 2 + 20", "Prüfe, ob die Stelle des größten Wertes der ganzen Parabel im erlaubten Preisbereich liegt.",
    "G(p) = −2(p − 5)² + 20. Der größte Wert der ganzen Parabel liegt bei p = 5, aber der Preis darf nur zwischen 3 und 4 liegen. In diesem Bereich wächst G, denn der Scheitel liegt weiter rechts. Der größte Gewinn ist bei p = 4: G(4) = −32 + 80 − 30 = 18.",
    [(20, None, "den größten Wert der ganzen Parabel genommen, obwohl der Preis höchstens 4 betragen darf", "-2 * (5 - 5) ** 2 + 20"), (5, None, "den Preis des Scheitels statt des Gewinns angegeben", "5"), (34, None, "beim Einsetzen den Faktor 2 vor p² weggelassen", "-4 ** 2 + 20 * 4 - 30")], "€"), g="transfer", regel=GF)
assert gl("-2*x**2+20*x-30", "-2*(x-5)**2+20")
# ───────── optimierung ─────────
neu(T, "optimierung", "umkehren", Z(
    "Mit einem Zaun der Länge L wird ein Rechteck vollständig umzäunt. Der ganze Zaun wird verbaut. Die größte Fläche, die man so umzäunen kann, ist 100 m². Wie lang ist der Zaun in Metern?",
    40, "4 * 10", "16 * 100 / 40", "Schreibe die Fläche mit einer Seite b als Funktion und suche ihren größten Wert.",
    "Die andere Seite ist L/2 − b. Die Fläche ist A(b) = b(L/2 − b). Ihr größter Wert liegt in der Mitte der Nullstellen 0 und L/2, bei b = L/4. Dort ist A = (L/4)² = L²/16. Aus L²/16 = 100 folgt L² = 1600 und L = 40 (L > 0). Probe: Quadrat mit Seite 10 hat Umfang 40 und Fläche 100.",
    [(10, None, "nur die Seite des besten Rechtecks angegeben", "10"), (25, None, "die Fläche durch 4 geteilt, ohne Wurzel zu ziehen", "100 / 4"), (400, None, "die Fläche mit 4 malgenommen", "4 * 100")], "m"), g="umkehr", regel=GF)
neu(T, "optimierung", "zwei_wege", Z(
    "Ein Landwirt zäunt an einer langen Mauer ein Rechteck ab. Die Mauer ist eine Seite. Für die drei anderen Seiten hat er 40 m Zaun, der ganz verbaut wird. Wie groß ist die größte Fläche in Quadratmetern? Weg A: Funktion der Fläche in Scheitelform umschreiben. Weg B: Nullstellen der Funktion bestimmen und die Symmetrie der Parabel nutzen.",
    200, "10 * (40 - 2 * 10)", "40 ** 2 / 8", "Die Seite senkrecht zur Mauer sei b. Wie lang ist dann die Seite parallel zur Mauer?",
    "Die Seite parallel zur Mauer ist 40 − 2b lang. Fläche: A(b) = b(40 − 2b) = −2b² + 40b. Weg A: A(b) = −2(b − 10)² + 200, der größte Wert ist 200. Weg B: A(b) = 0 für b = 0 und b = 20. Der Scheitel liegt in der Mitte, bei b = 10, und dort ist A = 10 · 20 = 200. Beide Wege geben 200 m².",
    [(100, None, "die Mauer nicht berücksichtigt: Rechteck mit allen vier Seiten aus Zaun gerechnet", "(40 / 4) ** 2"), (10, None, "nur die Seite des Scheitels angegeben", "10"), (20, None, "die Länge der Seite parallel zur Mauer angegeben", "40 - 2 * 10")], "m²"), g="verknuepfen", regel=GF)
assert gl("x*(40-2*x)", "-2*(x-10)**2+200")
