T = "abbildungen.kongruenz_teil3"
# ───────── punktspiegelung ─────────
a1(T, "punktspiegelung", Z(
    "Auf einem Spielfeld mit Koordinaten liegt die Mitte bei Z(2 | 3). Eine Spielfigur steht auf P(5 | 7). Eine zweite Figur steht genau gegenüber, sodass Z die Mitte der Strecke zwischen den beiden Figuren ist. Welche y-Koordinate hat die zweite Figur?",
    -1, "2 * 3 - 7", "3 - (7 - 3)", "Von P(5 | 7) nach Z(2 | 3) ändert sich die y-Koordinate um einen bestimmten Betrag. Gehe denselben Weg von Z aus noch einmal.",
    "In y-Richtung geht man von P nach Z um 7 − 3 = 4 nach unten. Von Z aus noch einmal 4 nach unten: 3 − 4 = −1. Oder: y′ = 2 · 3 − 7 = −1. Die zweite Figur hat die y-Koordinate −1.",
    [(4, None, "nur den Abstand der y-Koordinaten von P und Z angegeben", "7 - 3"), (10, None, "die y-Koordinaten von Z und P addiert", "3 + 7"), (11, None, "zweimal die y-Koordinate von P genommen und die y-Koordinate von Z abgezogen", "2 * 7 - 3")]))
a2(T, "punktspiegelung", Z(
    "Eine Drohne fliegt in gerader Linie von R(−4 | 6) über eine Landeplatte bei S(2 | 3) hinweg und genau so weit dahinter weiter. S liegt also in der Mitte ihres Flugwegs. Wie groß ist die Summe der beiden Koordinaten ihres Zielpunkts?",
    8, "(2 * 2 - (-4)) + (2 * 3 - 6)", "(8) + (0)", "Wie weit geht es von R nach S in x-Richtung und wie weit in y-Richtung? Gehe denselben Weg von S noch einmal.",
    "Von R nach S: x ändert sich um 2 − (−4) = 6, y um 3 − 6 = −3. Von S noch einmal: x = 2 + 6 = 8, y = 3 − 3 = 0. Der Zielpunkt ist (8 | 0). Die Summe der Koordinaten ist 8 + 0 = 8.",
    [(7, None, "die Koordinaten von R und S addiert", "-4 + 2 + 6 + 3"), (-2, None, "am Ursprung statt an S gespiegelt: Zielpunkt (4 | −6)", "4 - 6"), (14, None, "den Weg nur in x-Richtung verdoppelt, in y-Richtung gar nicht verändert: (8 | 6)", "8 + 6")]))
a3(T, "punktspiegelung", Z(
    "Der Punkt P(4 | −3) wird an einem Punkt Z gespiegelt. Der Bildpunkt P′ liegt auf der y-Achse und hat die y-Koordinate 11. Wie groß ist die Summe der beiden Koordinaten von Z?",
    6, "(4 + 0) / 2 + (-3 + 11) / 2", "2 + 4", "Wo liegen Punkte auf der y-Achse? Z ist die Mitte der Strecke von P nach P′.",
    "Ein Punkt auf der y-Achse hat die x-Koordinate 0, also ist P′(0 | 11). Z ist die Mitte von P und P′: x = (4 + 0) : 2 = 2 und y = (−3 + 11) : 2 = 4. Also Z(2 | 4) und die Summe ist 6. Probe: Von P nach Z geht es 2 nach links und 7 nach oben, von Z nach P′ noch einmal.",
    [(12, None, "die vier Koordinaten addiert und nicht halbiert", "4 + 0 + (-3) + 11"), (4, None, "nur die y-Koordinate von Z angegeben", "(-3 + 11) / 2"), (2, None, "nur die x-Koordinate von Z angegeben", "(4 + 0) / 2")]), g="rueckwaerts")
# ───────── drehung ─────────
a1(T, "drehung", Z(
    "Auf einem Spielbrett mit Koordinatensystem steht eine Figur auf P(4 | 1). Sie wird um den Ursprung O(0 | 0) um 90° gegen den Uhrzeigersinn gedreht. Dabei wird aus (x | y) der Punkt (−y | x). Welche x-Koordinate hat die Figur danach?",
    -1, "-1", "0 - 1", "Setze x = 4 und y = 1 in die Regel (x | y) → (−y | x) ein. Welche Zahl steht an erster Stelle?",
    "Aus (4 | 1) wird (−1 | 4). Die x-Koordinate ist −1 (das Gegenteil der alten y-Koordinate 1).",
    [(4, None, "die x-Koordinate 4 unverändert übernommen (nicht gedreht)", "4"), (1, None, "im Uhrzeigersinn statt dagegen gedreht", "1"), (-4, None, "das Vorzeichen der alten x-Koordinate geändert statt der y-Koordinate", "-4")]))
a2(T, "drehung", Z(
    "Der Ausleger eines Krans dreht sich um den Mast bei Z(3 | −2) um 90° gegen den Uhrzeigersinn. Seine Spitze steht zuerst bei P(7 | 1). Aus einem Vektor (a | b) wird bei dieser Drehung der Vektor (−b | a). Wie groß ist die Summe der beiden Koordinaten der Spitze nach der Drehung?",
    2, "(3 + (-(1 - (-2)))) + (-2 + (7 - 3))", "0 + 2", "Rechne zuerst den Vektor von Z nach P. Drehe diesen Vektor. Trage ihn danach wieder bei Z an.",
    "Vektor von Z nach P: (7 − 3 | 1 − (−2)) = (4 | 3). Gedreht: (−3 | 4). Von Z aus: (3 + (−3) | −2 + 4) = (0 | 2). Die Summe der Koordinaten ist 0 + 2 = 2.",
    [(6, None, "um den Ursprung statt um Z gedreht: (−1 | 7)", "-1 + 7"), (1, None, "den gedrehten Vektor nicht an Z angesetzt: (−3 | 4)", "-3 + 4"), (0, None, "im Uhrzeigersinn statt dagegen gedreht: (6 | −6)", "6 - 6")]))
a3(T, "drehung", Z(
    "Eine Figur wurde um Z(2 | 1) um 90° gegen den Uhrzeigersinn gedreht. Dabei wird aus einem Vektor (a | b) der Vektor (−b | a). Nach der Drehung steht die Figur bei P′(−2 | 7). Wie groß ist die Summe der beiden Koordinaten des Punktes P, an dem sie vorher stand?",
    13, "(2 + (7 - 1)) + (1 + (2 - (-2)))", "8 + 5", "Rechne den Vektor von Z nach P′. Welcher Vektor (a | b) wird durch die Drehung zu diesem Vektor?",
    "Vektor von Z nach P′: (−2 − 2 | 7 − 1) = (−4 | 6). Er ist das Bild von (a | b) mit −b = −4 und a = 6, also b = 4. Der ursprüngliche Vektor ist (6 | 4). Von Z aus: P = (2 + 6 | 1 + 4) = (8 | 5). Die Summe ist 13. Probe: (6 | 4) wird zu (−4 | 6).",
    [(10, None, "den Vektor zurückgedreht, aber nicht an Z angesetzt: (6 | 4)", "6 + 4"), (-7, None, "noch einmal um 90° weitergedreht statt zurückgedreht: (−4 | −3)", "-4 - 3"), (5, None, "die Summe der Koordinaten von P′ angegeben", "-2 + 7")]), g="rueckwaerts")
# ───────── vektor_drehen ─────────
a1(T, "vektor_drehen", Z(
    "Eine Drohne fliegt auf einer Karte (x zeigt nach Osten, y nach Norden) den Vektor (5 | 2). Dann dreht sie sich um 90° nach rechts, also im Uhrzeigersinn, und fliegt gleich weit. Dabei wird aus (x | y) der Vektor (y | −x). Welche y-Koordinate hat der zweite Flugvektor?",
    -5, "-5", "0 - 5", "Setze x = 5 und y = 2 in die Regel (x | y) → (y | −x) ein. Welche Zahl steht an zweiter Stelle?",
    "Aus (5 | 2) wird (2 | −5). Die zweite Koordinate ist −x = −5.",
    [(5, None, "gegen den Uhrzeigersinn gedreht: (−2 | 5)", "5"), (2, None, "die erste Koordinate des gedrehten Vektors angegeben statt der zweiten", "2"), (-2, None, "die zweite Koordinate als −y statt als −x genommen", "0 - 2")]))
a2(T, "vektor_drehen", Z(
    "Ein Wanderer geht auf einer Karte von A(−2 | 3) nach B(4 | 5). Der Vektor AB wird um 90° gegen den Uhrzeigersinn gedreht (aus (x | y) wird (−y | x)) und bei B angesetzt. Er endet in C. Welche y-Koordinate hat C?",
    11, "5 + (4 - (-2))", "5 + 6", "Berechne zuerst den Vektor AB. Drehe ihn, dann gehe vom Punkt B aus weiter.",
    "AB = (4 − (−2) | 5 − 3) = (6 | 2). Gedreht: (−2 | 6). Von B(4 | 5) aus: C = (4 − 2 | 5 + 6) = (2 | 11). Die y-Koordinate ist 11.",
    [(6, None, "den gedrehten Vektor nicht bei B angesetzt", "6"), (-1, None, "im Uhrzeigersinn gedreht: (2 | −6) an B angesetzt", "5 - 6"), (3, None, "um 180° statt um 90° gedreht: (−6 | −2) an B angesetzt", "5 - 2")]))
a3(T, "vektor_drehen", Z(
    "Ein Vektor v wird nacheinander um +90°, um 180° und um −90° gedreht. Das Ergebnis ist der Vektor (−3 | 7). Dabei gilt: +90°: (x | y) → (−y | x); −90°: (x | y) → (y | −x); 180°: (x | y) → (−x | −y). Wie groß ist die Summe der beiden Koordinaten von v?",
    -4, "3 + (-7)", "-(-3 + 7)", "Wie viel wird insgesamt gedreht? Fasse die drei Drehungen zu einer zusammen.",
    "Insgesamt wird um 90° + 180° − 90° = 180° gedreht. Eine Drehung um 180° macht aus v = (x | y) den Vektor (−x | −y) = (−3 | 7). Also ist v = (3 | −7). Die Summe ist 3 + (−7) = −4.",
    [(4, None, "den Ergebnisvektor als v genommen und die Koordinaten addiert", "-3 + 7"), (10, None, "die Beträge der Koordinaten addiert", "3 + 7"), (-10, None, "beide Vorzeichen vertauscht: v = (−3 | −7)", "-3 - 7")]), g="verknuepfen")
