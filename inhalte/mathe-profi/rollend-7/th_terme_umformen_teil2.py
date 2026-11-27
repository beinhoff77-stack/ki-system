T = "terme.umformen_teil2"
# ───────── summe_mal_summe ─────────
neu(T, "summe_mal_summe", "lueckenweg", L(
    "Multipliziere aus: (x + 5)(x + 3). Jedes Glied der ersten Klammer mal jedes Glied der zweiten. x · x = x². x · 3 = ①x. 5 · x = ②x. 5 · 3 = ③.",
    KOMM(3), [3, 5, 15], ["1 * 3", "5 * 1", "5 * 3"], ["3", "5", "15"], "Es entstehen vier Produkte. Die beiden mit x kannst du danach zusammenfassen.",
    "x² + 3x + 5x + 15 = x² + 8x + 15.",
    {2: [(8, "fb.tauschen.ungleiches_zusammengefasst", "5 + 3 gerechnet statt 5 · 3")]}), regel="rr.ausmultiplizieren")
neu(T, "summe_mal_summe", "zwei_wege", Z(
    "Berechne (x + 3)(x − 2) für x = 5 auf zwei Wegen. Weg A: erst ausmultiplizieren (das gibt x² + x − 6), dann x = 5 einsetzen. Weg B: erst x = 5 in beide Klammern einsetzen, dann malnehmen. Welchen Wert erhältst du?",
    24, "(5 + 3) * (5 - 2)", "5 ** 2 + 5 - 6", "Beide Wege müssen denselben Wert ergeben.",
    "Weg A: 25 + 5 − 6 = 24. Weg B: 8 · 3 = 24.",
    [(19, None, "das Glied x vergessen: 25 − 6"), (36, "fb.vorzeichen.falsches_zeichen", "−6 als +6 gerechnet")]), regel="rr.ausmultiplizieren")
assert gl("(x+3)*(x-2)", "x**2+x-6")
neu(T, "summe_mal_summe", "bruecke", W(
    "Die Tabelle zerlegt ein Rechteck in vier Teilflächen. Oben stehen die beiden Teile der Länge, links die der Breite. Welches Produkt gibt die ganze Fläche?",
    "(x + 5)(x + 2)", [("(x + 5)(x + 10)", "die Teilfläche 10 als Seitenlänge genommen"), ("(x + 7)(x + 3)", "Summen aus den Teilflächen gebildet"), ("x(x + 2) + 5", "nur ein Teil der Fläche")],
    "Länge mal Breite: Welche zwei Teile bilden die Länge, welche die Breite?",
    "Länge: x + 2. Breite: x + 5. Fläche: (x + 5)(x + 2) = x² + 2x + 5x + 10 = x² + 7x + 10.",
    lambda: gl("x*x+2*x+5*x+10", "(x+5)*(x+2)") and not gl("x*x+2*x+5*x+10", "(x+5)*(x+10)") and not gl("x*x+2*x+5*x+10", "(x+7)*(x+3)") and not gl("x*x+2*x+5*x+10", "x*(x+2)+5"),
    grafik=TAB(["·", "x", "+2"], ["x", "x²", "2x"], ["+5", "5x", "10"])), regel="rr.ausmultiplizieren")

# ───────── ausklammern ─────────
neu(T, "ausklammern", "lueckenweg", L(
    "Klammere aus: 12x + 18. Der größte gemeinsame Faktor von 12 und 18 ist ①. 12x : ① = ②x und 18 : ① = ③. Ergebnis: ①(②x + ③).",
    KOMM(3), [6, 2, 3], ["6", "12 // 6", "18 // 6"], ["2 * 3", "2", "18 // 6"], "Welche größte Zahl teilt 12 und 18 ohne Rest?",
    "Der größte gemeinsame Teiler von 12 und 18 ist 6. 12x : 6 = 2x und 18 : 6 = 3. Probe: 6(2x + 3) = 12x + 18.",
    {0: [(2, None, "einen gemeinsamen Teiler genommen, aber nicht den größten"), (3, None, "einen gemeinsamen Teiler genommen, aber nicht den größten")]}), regel="rr.ausmultiplizieren")
neu(T, "ausklammern", "zwei_wege", Z(
    "Berechne 6 · 17 + 6 · 13 auf zwei Wegen. Weg A: beide Produkte einzeln ausrechnen und addieren. Weg B: den Faktor 6 ausklammern und die Summe in der Klammer bilden. Was kommt heraus?",
    180, "6 * (17 + 13)", "102 + 78", "Beide Wege müssen dasselbe ergeben. Welcher ist kürzer?",
    "Weg A: 102 + 78 = 180. Weg B: 6 · (17 + 13) = 6 · 30 = 180.",
    [(30, None, "nur die Klammer 17 + 13 ausgerechnet"), (115, None, "die 6 nur bei 17 gerechnet: 102 + 13")]), regel="rr.ausmultiplizieren")
neu(T, "ausklammern", "anwenden", Z(
    "Ein Verein bestellt 25 T-Shirts zu 8,50 € das Stück und 25 Mützen zu 6,50 € das Stück. Wie viel Euro kostet die ganze Bestellung? Klammere geschickt aus.",
    375, "25 * (8.5 + 6.5)", "25 * 8.5 + 25 * 6.5", "Beide Posten haben dieselbe Anzahl. Was kannst du ausklammern?",
    "25 · 8,50 + 25 · 6,50 = 25 · (8,50 + 6,50) = 25 · 15 = 375. Die Bestellung kostet 375 €.",
    [(212.5, None, "nur die T-Shirts gerechnet"), (15, None, "nur die Klammer 8,50 + 6,50 gerechnet")], "€"), g="einkleidung", regel="rr.ausmultiplizieren")

# ───────── binomisch ─────────
neu(T, "binomisch", "lueckenweg", L(
    "Multipliziere mit der 2. binomischen Formel aus: (2a − 3)². Das Quadrat des ersten Gliedes: (2a)² = ①a². Das doppelte Produkt: 2 · 2a · 3 = ②a (mit Minus). Das Quadrat des zweiten Gliedes: 3² = ③.",
    KOMM(3), [4, 12, 9], ["2 ** 2", "2 * 2 * 3", "3 ** 2"], ["2 * 2", "12", "9"], "Die Zahl 2 in (2a)² wird mitquadriert.",
    "(2a)² = 4a². 2 · 2a · 3 = 12a. 3² = 9. Ergebnis: 4a² − 12a + 9.",
    {0: [(2, "fb.potenz.basis_mal_hochzahl", "2 · 2 statt 2² gerechnet")], 2: [(6, "fb.potenz.basis_mal_hochzahl", "3 · 2 statt 3² gerechnet")]}), regel="rr.ausmultiplizieren")
assert gl("(2*a-3)**2", "4*a**2-12*a+9")
neu(T, "binomisch", "umkehren", Z(
    "Für welche Zahl b gilt 9x² + bx + 25 = (3x + 5)²?",
    30, "2 * 3 * 5", 30, "Multipliziere (3x + 5)² aus. Das mittlere Glied ist das doppelte Produkt.",
    "(3x + 5)² = 9x² + 2 · 3x · 5 + 25 = 9x² + 30x + 25. Also ist b = 30.",
    [(15, "fb.ausmultiplizieren.nur_erster_summand", "die 2 im doppelten Produkt vergessen"), (8, None, "3 + 5 gerechnet"), (-30, "fb.vorzeichen.falsches_zeichen", "ein Minus eingefügt")]), g="umkehr", regel="rr.ausmultiplizieren")
assert gl("(3*x+5)**2", "9*x**2+30*x+25")
neu(T, "binomisch", "bruecke", W(
    "Die Tabelle zerlegt ein Quadrat mit der Seitenlänge a + 3 in vier Teilflächen. Welcher Term gibt die Gesamtfläche an?",
    "a² + 6a + 9", [("a² + 9", "das Mischglied vergessen"), ("a² + 3a + 9", "nur eine der beiden Teilflächen 3a gezählt"), ("a² + 6a + 6", "3 · 2 statt 3² gerechnet")],
    "Zähle alle vier Teilflächen zusammen.",
    "a² + 3a + 3a + 9 = a² + 6a + 9. Das ist (a + 3)².",
    lambda: gl("a**2+3*a+3*a+9", "(a+3)**2") and not gl("a**2+9", "(a+3)**2") and not gl("a**2+3*a+9", "(a+3)**2") and not gl("a**2+6*a+6", "(a+3)**2"),
    grafik=TAB(["·", "a", "+3"], ["a", "a²", "3a"], ["+3", "3a", "9"])), regel="rr.ausmultiplizieren")

# ───────── gleichungen_binomisch ─────────
neu(T, "gleichungen_binomisch", "fehler_detektiv", FD(
    "Kim löst die Gleichung (x + 4)² = x² + 40.",
    [("(x + 4)² = x² + 8x + 16, also x² + 8x + 16 = x² + 40", gl("(x+4)**2", "x**2+8*x+16")),
     ("x² auf beiden Seiten abziehen: 8x + 16 = 40", (8 * 3 + 16 == 40) and ((3 + 4) ** 2 == 3 ** 2 + 40)),
     ("8x = 40 + 16 = 56, also x = 7", (7 + 4) ** 2 == 7 ** 2 + 40)],
    "Wie bringst du die 16 auf die rechte Seite? Mach die Probe mit x = 7.",
    "Die 16 muss abgezogen werden: 8x = 40 − 16 = 24, also x = 3. Probe: 7² = 49 und 9 + 40 = 49.", frage="In welcher Zeile steckt der Fehler?"), regel="rr.waage")
neu(T, "gleichungen_binomisch", "anwenden", Z(
    "Bei einem quadratischen Platz wird jede Seite um 3 m länger. Dadurch wächst die Fläche um 51 m². Wie lang war eine Seite vorher?",
    7, "(51 - 9) / 6", 7, "Die alte Seite ist a. Die neue Fläche ist (a + 3)². Die Zunahme ist (a + 3)² − a².",
    "(a + 3)² − a² = 6a + 9. Aus 6a + 9 = 51 folgt 6a = 42, also a = 7. Probe: 10² − 7² = 100 − 49 = 51.",
    [(8.5, None, "51 : 6 gerechnet, die 9 vergessen"), (17, None, "das Mischglied nicht beachtet: 51 : 3")], "m"), g="transfer", regel="id.algebra.gleichung_loesen")
assert (7 + 3) ** 2 - 7 ** 2 == 51
neu(T, "gleichungen_binomisch", "umkehren", Z(
    "Die Gleichung (x + 3)² = x² + 4x + a hat die Lösung x = 4. Wie groß ist die Zahl a?",
    17, "(4 + 3) ** 2 - 4 ** 2 - 4 * 4", "49 - 32", "Setze x = 4 in beide Seiten ein.",
    "Links: (4 + 3)² = 49. Rechts: 16 + 16 + a = 32 + a. Aus 49 = 32 + a folgt a = 17.",
    [(9, None, "nur das letzte Glied 3² genommen"), (33, None, "das Glied 4x vergessen: 49 − 16")]), g="rueckwaerts", regel="id.algebra.gleichung_loesen")
