T = "terme.umformen_teil2"
# ───────── summe_mal_summe ─────────
a1(T, "summe_mal_summe", Z(
    "Ein Tisch ist (x + 5) dm lang und (x + 3) dm breit. Seine Fläche in dm² ist ausmultipliziert x² + a · x + 15. Wie groß ist die Zahl a?",
    8, "5 + 3", "3 + 5", "Multipliziere jedes Glied der ersten Klammer mit jedem Glied der zweiten. Welche Produkte enthalten x?",
    "(x + 5)(x + 3) = x · x + x · 3 + 5 · x + 5 · 3 = x² + 3x + 5x + 15 = x² + 8x + 15. Also ist a = 8.",
    [(15, None, "nur das Produkt der beiden Zahlen angegeben", "5 * 3"), (2, None, "die Zahlen 5 und 3 subtrahiert statt addiert", "5 - 3"), (5, None, "nur eines der beiden Produkte mit x gezählt", "5")]))
a2(T, "summe_mal_summe", Z(
    "Ein Poster ist (x + 6) cm breit und (x − 2) cm hoch. Seine Fläche in cm² ist ausmultipliziert und zusammengefasst x² + p · x + q. Wie groß ist die Summe p + q?",
    -8, "(6 - 2) + 6 * (-2)", "4 - 12", "Es entstehen vier Produkte. Achte beim Glied −2 auf das Vorzeichen. Fasse die Glieder mit x zusammen.",
    "(x + 6)(x − 2) = x² − 2x + 6x − 12 = x² + 4x − 12. Also ist p = 4 und q = −12. Die Summe ist 4 + (−12) = −8.",
    [(20, None, "das Minuszeichen bei der 2 übersehen: x² + 8x + 12", "8 + 12"), (16, None, "das Vorzeichen des Produkts 6 mal (−2) falsch: x² + 4x + 12", "4 + 12"), (4, None, "nur p angegeben", "4")]))
a3(T, "summe_mal_summe", Z(
    "Eine rechteckige Terrasse hat die Seitenlängen (x + a) m und (x + b) m, dabei sind a und b ganze Zahlen mit 0 < a < b. Ihre Fläche ist x² + 9x + 14 m². Wie lang ist die längere Seite der Terrasse, wenn x = 10 ist?",
    17, "10 + 7", "7 + 10", "Beim Ausmultiplizieren entsteht x² + (a + b) · x + a · b. Welche zwei ganzen Zahlen haben die Summe 9 und das Produkt 14?",
    "Es muss a + b = 9 und a · b = 14 gelten. Das passt zu a = 2 und b = 7. Die Seiten sind (x + 2) und (x + 7). Für x = 10: 12 m und 17 m. Die längere Seite ist 17 m lang. Probe: (x + 2)(x + 7) = x² + 9x + 14.",
    [(12, None, "die kürzere Seite angegeben", "10 + 2"), (19, None, "die Summe 9 als b genommen", "10 + 9"), (24, None, "das Produkt 14 als b genommen", "10 + 14")], "m"), g="rueckwaerts")
# ───────── ausklammern ─────────
a1(T, "ausklammern", Z(
    "Eine Wand hat die Fläche 15x + 20 m². Sie ist ein Rechteck, und eine Seite ist 5 m lang. Wie lang ist die andere Seite, wenn x = 4 ist?",
    16, "(15 * 4 + 20) / 5", "3 * 4 + 4", "Klammere den größten gemeinsamen Faktor aus. Er steht für die Seite, die du schon kennst.",
    "15x + 20 = 5 · (3x + 4). Die eine Seite ist 5 m lang, also ist die andere Seite 3x + 4. Für x = 4: 3 · 4 + 4 = 16 m. Probe: 5 · 16 = 80 und 15 · 4 + 20 = 80.",
    [(80, None, "die Fläche statt der Seitenlänge angegeben", "15 * 4 + 20"), (32, None, "nur das erste Glied durch 5 geteilt: 3x + 20", "3 * 4 + 20"), (64, None, "nur das zweite Glied durch 5 geteilt: 15x + 4", "15 * 4 + 4")], "m"))
a2(T, "ausklammern", Z(
    "Der Gewinn eines Marktstands ist G = 4x² + 28x Euro, wobei x die Zahl der verkauften Kisten ist. Klammert man den größten gemeinsamen Faktor aus, erhält man G = c · x · (x + d). Wie groß ist die Summe c + d?",
    11, "4 + 28 / 4", "4 + 7", "Welche Zahl und welche Potenz von x stecken in beiden Gliedern? Was bleibt in der Klammer?",
    "Der größte gemeinsame Faktor von 4x² und 28x ist 4x. 4x² : 4x = x und 28x : 4x = 7. Also G = 4x · (x + 7), das heißt c = 4 und d = 7. Die Summe ist 11. Probe: 4x · x + 4x · 7 = 4x² + 28x.",
    [(28, None, "c und d malgenommen statt addiert", "4 * 7"), (7, None, "nur d angegeben", "7")]))
a3(T, "ausklammern", Z(
    "Ein Rechteck hat die Fläche 6x² + 9x (in cm²) und eine Seite der Länge 3x cm. Wie groß ist der Umfang des Rechtecks in cm, wenn x = 4 ist?",
    46, "2 * (3 * 4 + (2 * 4 + 3))", "2 * (12 + 11)", "Die Fläche ist Länge mal Breite. Klammere 3x aus, dann erkennst du die andere Seite.",
    "6x² + 9x = 3x · (2x + 3). Die eine Seite ist 3x, die andere 2x + 3. Für x = 4: 12 cm und 11 cm. Umfang = 2 · (12 + 11) = 46 cm. Probe: Fläche 12 · 11 = 132 = 6 · 16 + 9 · 4.",
    [(23, None, "den Umfang nicht verdoppelt: nur beide Seiten addiert", "12 + 11"), (132, None, "die Fläche statt des Umfangs angegeben", "12 * 11")], "cm"), g="verknuepfen")
# ───────── binomisch ─────────
a1(T, "binomisch", Z(
    "Ein quadratischer Teppich hat die Seitenlänge (x + 3) m. Seine Fläche in m² ist ausmultipliziert x² + b · x + 9. Wie groß ist b?",
    6, "2 * 3", "3 + 3", "Das Mittelglied bei (a + b)² ist 2 · a · b. Was ist hier a und was ist b?",
    "(x + 3)² = x² + 2 · x · 3 + 3² = x² + 6x + 9. Also ist b = 6. Das Mittelglied darf man nie vergessen.",
    [(3, None, "nur die Zahl 3 als Mittelglied genommen", "3"), (0, None, "das Mittelglied ganz vergessen: (x + 3)² = x² + 9", "0"), (9, None, "das Quadrat 3² als Mittelglied genommen", "3 ** 2")]))
a2(T, "binomisch", Z(
    "Ein rechteckiges Feld ist 52 m lang und 48 m breit. Wie groß ist seine Fläche in m²? Rechne geschickt mit (50 + 2) · (50 − 2).",
    2496, "50 ** 2 - 2 ** 2", "52 * 48", "Die beiden Klammern unterscheiden sich nur im Vorzeichen. Welche binomische Formel passt?",
    "(50 + 2)(50 − 2) = 50² − 2² = 2 500 − 4 = 2 496. Probe: 52 · 48 = 2 496.",
    [(2500, None, "nur 50² gerechnet, das Quadrat von 2 vergessen", "50 ** 2"), (2504, None, "2² addiert statt subtrahiert", "50 ** 2 + 2 ** 2"), (2400, None, "vom Quadrat 50² das Produkt aus 2 und 50 abgezogen statt 2²", "50 ** 2 - 2 * 50")], "m²"))
a3(T, "binomisch", Z(
    "Ein quadratisches Beet hat die Fläche 4x² + 20x + k (in m²) und die Seitenlänge 2x + m (in m). Dabei sind k und m feste Zahlen. Wie lang ist die Seite des Beets für x = 3?",
    11, "2 * 3 + 20 / (2 * 2)", "6 + 5", "Vergleiche die Fläche mit (2x + m)². Welches Glied bei (2x + m)² enthält m und x?",
    "(2x + m)² = 4x² + 4m · x + m². Der Vergleich mit 4x² + 20x + k gibt 4m = 20, also m = 5 (und k = 25). Die Seite ist 2x + 5. Für x = 3: 2 · 3 + 5 = 11 m. Probe: 11² = 121 = 4 · 9 + 20 · 3 + 25.",
    [(16, None, "m = 10 aus 2m = 20 genommen: Mittelglied falsch gedeutet", "2 * 3 + 10"), (121, None, "die Fläche statt der Seitenlänge angegeben", "11 ** 2"), (9, None, "m = 3 genommen: x selbst statt der Zahl m", "2 * 3 + 3")], "m"), g="rueckwaerts")
# ───────── gleichungen_binomisch ─────────
a1(T, "gleichungen_binomisch", Z(
    "Ein quadratisches Foto hat die Seitenlänge x cm. Ein Rahmen ist ringsum 2 cm breit, der Rahmen allein hat die Fläche 48 cm². Die Außenseite des Rahmens ist x + 4 cm lang. Wie lang ist die Seite des Fotos in cm?",
    4, "(48 - 16) / 8", "(48 / 8) - 2", "Die Rahmenfläche ist das äußere Quadrat minus das Foto. Stelle die Gleichung (x + 4)² − x² = 48 auf.",
    "(x + 4)² − x² = 48 → x² + 8x + 16 − x² = 48 → 8x + 16 = 48 → 8x = 32 → x = 4. Das Foto ist 4 cm lang. Probe: 8² − 4² = 64 − 16 = 48.",
    [(11, None, "den Rahmen nur einmal gerechnet: (x + 2)² − x² = 48", "(48 - 4) / 4"), (6, None, "48 durch 8 geteilt, ohne 16 abzuziehen", "48 / 8"), (8, None, "die Außenseite des Rahmens statt des Fotos angegeben", "4 + 4")], "cm"))
a2(T, "gleichungen_binomisch", Z(
    "Ein quadratisches Feld hat die Seitenlänge x + 5 m, ein zweites quadratisches Feld hat die Seitenlänge x − 3 m. Das erste Feld ist 96 m² größer als das zweite. Wie groß ist x?",
    5, "(96 - 16) / 16", "(96 - 25 + 9) / 16", "Multipliziere beide Klammern mit den binomischen Formeln aus. Was passiert mit x²?",
    "(x + 5)² − (x − 3)² = 96 → x² + 10x + 25 − (x² − 6x + 9) = 96 → 16x + 16 = 96 → 16x = 80 → x = 5. Die Felder sind 10 m und 2 m lang. Probe: 100 − 4 = 96.",
    [(6, None, "16 nicht abgezogen: 96 durch 16 geteilt", "96 / 16"), (8, None, "das Mittelglied der zweiten Klammer vergessen: (x − 3)² = x² + 9", "(96 - 16) / 10")], "m"))
a3(T, "gleichungen_binomisch", Z(
    "Ein quadratisches Grundstück hat die Seitenlänge x + 3 m. Ein rechteckiges Grundstück ist x m breit und x + 7 m lang. Beide Grundstücke sind gleich groß. Wie lang ist die Seite des quadratischen Grundstücks in Metern?",
    12, "9 + 3", "(9 * 16) ** 0.5", "Stelle die Gleichung (x + 3)² = x · (x + 7) auf. Multipliziere beide Seiten aus.",
    "(x + 3)² = x · (x + 7) → x² + 6x + 9 = x² + 7x → 9 = x. Also ist x = 9 und die Seite des Quadrats ist 9 + 3 = 12 m lang. Probe: 12² = 144 und 9 · 16 = 144.",
    [(9, None, "x statt der Seitenlänge x + 3 angegeben", "9"), (16, None, "die längere Seite des Rechtecks angegeben", "9 + 7")], "m"), g="verknuepfen")
