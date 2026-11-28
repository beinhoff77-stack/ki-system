T = "funktionen.quadratisch"
GF = "id.funktionen.gleichung_form"
ZU = "id.funktionen.zuordnung"
OHNE_GS = "Gleichungssystem bzw. Gleichsetzen zweier Funktionsterme: keine Regel des Katalogs trägt den Lösungsweg"
f_ = lambda a, d, e: (lambda x: a * (x - d) ** 2 + e)
# ───────── scheitel ─────────
neu(T, "scheitel", "lueckenweg", L(
    "Die Parabel y = 2(x − 5)² − 1 wird um 4 Einheiten nach rechts und um 7 Einheiten nach oben verschoben. Die neue Parabel hat den Scheitel S(①|②). Für x = 10 hat sie den y-Wert ③.",
    "① = □; ② = □; ③ = □", [9, 6, 8], ["5 + 4", "-1 + 7", "2 * (10 - {1}) ** 2 + {2}"], ["9", "6", "2 * (10 - 9) ** 2 + 6"],
    "Aus y = a(x − d)² + e liest du den Scheitel S(d|e) ab. Verschiebung nach rechts erhöht d, Verschiebung nach oben erhöht e.",
    "Der alte Scheitel ist S(5|−1). Nach 4 nach rechts und 7 nach oben: S(9|6). Die neue Gleichung heißt y = 2(x − 9)² + 6. Für x = 10: y = 2 · 1 + 6 = 8.",
    {0: [(1, None, "nach links statt nach rechts verschoben", "5 - 4")], 1: [(-8, None, "um 7 nach unten statt nach oben verschoben", "-1 - 7")], 2: [(7, None, "den Faktor 2 vor der Klammer vergessen", "(10 - {1}) ** 2 + {2}")]}), regel=GF)
neu(T, "scheitel", "verfahren_waehlen", W(
    "Welche Gleichung gehört zu einer nach unten geöffneten Parabel mit dem Scheitel S(−4|9)?",
    "y = −(x + 4)² + 9", [("y = −(x − 4)² + 9", "das Vorzeichen in der Klammer gleich dem Vorzeichen von −4 gesetzt, die Parabel hat den Scheitel S(4|9)"), ("y = (x + 4)² + 9", "nach oben statt nach unten geöffnet"), ("y = −(x + 4)² − 9", "den y-Wert des Scheitels mit falschem Vorzeichen")],
    "Setze den Scheitel in die Form y = a(x − d)² + e ein. Wann ist die Parabel nach unten geöffnet?",
    "Die Scheitelform ist y = a(x − d)² + e mit d = −4 und e = 9, also (x − (−4))² = (x + 4)². Nach unten geöffnet heißt a < 0, hier a = −1. Die Gleichung heißt y = −(x + 4)² + 9.",
    lambda: all(-(x + 4) ** 2 + 9 <= 9 for x in range(-20, 20)) and -(-4 + 4) ** 2 + 9 == 9 and -(-4 - 4) ** 2 + 9 != 9 and (-4 + 4) ** 2 + 9 == 9 and (-4 + 4) ** 2 - 9 != 9), g="mehrschritt", regel=GF)
# ───────── parameter ─────────
neu(T, "parameter", "umkehren", Z(
    "Die Parabel y = a(x + 2)² − 5 geht durch den Punkt P(4|13). Wie groß ist a?",
    0.5, "18 / 36", 0.5, "Setze die Koordinaten von P für x und y ein und löse nach a. Rechne erst (4 + 2)².",
    "13 = a · (4 + 2)² − 5 = 36a − 5. Also 36a = 18 und a = 0,5. Probe: 0,5 · 36 − 5 = 13.",
    [B("18 / 4", "x + 2 als x − 2 gelesen und dann das Quadrat von 2 genommen"), B("18 / 6", "die Klammer 6 nicht quadriert"), B("18 * 36", "mit 36 malgenommen statt geteilt")]), g="parameter", regel=GF)
# ───────── spiegeln ─────────
neu(T, "spiegeln", "verfahren_waehlen", W(
    "Die Wasseroberfläche (die x-Achse) spiegelt den Bogen y = 2(x − 3)² − 4. Welche Gleichung gehört zum Spiegelbild im Wasser?",
    "y = −2(x − 3)² + 4", [("y = −2(x − 3)² − 4", "nur den Faktor vor der Klammer gespiegelt, die −4 nicht"), ("y = 2(x + 3)² − 4", "an der y-Achse gespiegelt, nicht an der x-Achse")],
    "Beim Spiegeln an der x-Achse wird jeder y-Wert zum Gegenwert. Prüfe einen Punkt, zum Beispiel x = 5.",
    "Bei x = 5 hat die Parabel y = 2 · 4 − 4 = 4. Das Spiegelbild hat dort y = −4. Das passt zu −2(x − 3)² + 4: −2 · 4 + 4 = −4. Alle y-Werte kehren ihr Vorzeichen um, auch die −4.",
    lambda: all(-(f_(2, 3, -4)(x)) == f_(-2, 3, 4)(x) for x in range(-9, 10)) and f_(-2, 3, -4)(5) != -4 and f_(2, -3, -4)(5) != -4), g="pruefung", regel=GF)
neu(T, "spiegeln", "anwenden", Z(
    "Ein Spiegel steht senkrecht an der y-Achse. Die Bahn y = (x − 6)² + 4 erscheint darin gespiegelt. An welcher x-Stelle liegt der tiefste Punkt der Spiegelbahn?",
    -6, "-6", -6, "Der tiefste Punkt der Bahn ist ihr Scheitel S(6|4). Was passiert mit dem x-Wert beim Spiegeln an der y-Achse?",
    "Der Scheitel der Ausgangsparabel ist S(6|4). Spiegeln an der y-Achse wechselt das Vorzeichen der x-Koordinate: S'(−6|4). Die Spiegelbahn hat die Gleichung y = (x + 6)² + 4.",
    [B("6", "die Bahn als unverändert angesehen"), B("-4", "den y-Wert gespiegelt statt den x-Wert"), B("4", "den y-Wert des Scheitels genannt")]), g="mehrschritt", regel=GF)
# ───────── umformen ─────────
neu(T, "umformen", "anwenden", Z(
    "Wie lautet die y-Koordinate des Scheitels der Parabel y = x² + 12x + 50?",
    14, "50 - 36", 14, "Ergänze quadratisch: Die Hälfte von 12 ist 6, ihr Quadrat 36. Wie ändert sich die Zahl hinten?",
    "x² + 12x + 50 = (x² + 12x + 36) + 50 − 36 = (x + 6)² + 14. Der Scheitel ist S(−6|14), die y-Koordinate ist 14.",
    [B("50 + 36", "die Ergänzung addiert statt ausgeglichen"), B("50", "die Zahl hinten nicht verändert"), B("50 - 12", "die 12 statt das Quadrat der Hälfte abgezogen")]), g="mehrschritt", regel=GF)
neu(T, "umformen", "fehler_detektiv", FD(
    "Sam bringt y = x² − 10x + 19 in die Scheitelform:",
    [("Die Hälfte von 10 ist 5, deshalb steht (x − 5)² in der Klammer.", True, True),
     ("Es gilt (x − 5)² = x² − 10x + 25.", gl("(x-5)**2", "x**2-10*x+25"), True),
     ("Also ist y = (x − 5)² + 19 und der Scheitel S(5|19).", False, True)],
    "Setze x = 5 in die Ausgangsgleichung ein. Welchen y-Wert bekommst du?",
    "Zeile 2 sagt, dass (x − 5)² um 25 größer ist als x² − 10x. Beim Übergang muss man die 25 wieder abziehen: y = (x − 5)² + 19 − 25 = (x − 5)² − 6. Der Scheitel ist S(5|−6). Probe: 25 − 50 + 19 = −6. Der Fehler steckt in Zeile 3."), g="fehler", regel=GF)
# ───────── nullstellen ─────────
neu(T, "nullstellen", "lueckenweg", L(
    "Die Parabel y = x² − 6x − 55 hat zwei Nullstellen. Die kleinere ist ①. Die größere ist ②. Der Scheitel liegt genau in der Mitte bei x = ③.",
    "① = □; ② = □; ③ = □", [-5, 11, 3], ["-5", "11", "({1} + {2}) / 2"], ["(6 - sqrt(6 ** 2 + 4 * 55)) / 2", "(6 + sqrt(6 ** 2 + 4 * 55)) / 2", "6 / 2"],
    "Setze y = 0 und löse die Gleichung, zum Beispiel mit der Lösungsformel oder durch Zerlegen. Die Mitte ist der Mittelwert beider Nullstellen.",
    "x² − 6x − 55 = (x − 11)(x + 5) = 0, also x = 11 oder x = −5. Der Scheitel liegt in der Mitte: (−5 + 11) : 2 = 3. Probe: 3² − 18 − 55 = −64 ist der kleinste y-Wert.",
    {0: [(5, None, "aus x + 5 = 0 die Lösung 5 gemacht", "5")], 1: [(55, None, "das Absolutglied als Nullstelle genommen", "55")], 2: [(6, None, "den Beiwert −6 statt seiner Hälfte genommen", "6")]}), regel=ZU,
    zweifel="Nur Teilregel: id.funktionen.zuordnung trägt das Setzen von y = 0, das Lösen der Gleichung (Nullprodukt) steht für diese Einheit nicht im Katalog")
neu(T, "nullstellen", "anwenden", Z(
    "Die Parabel y = (x + 2)² − 25 schneidet die x-Achse zweimal. Wie weit sind die beiden Schnittpunkte voneinander entfernt?",
    10, "3 - -7", 10, "Setze y = 0 und löse nach x. Der Abstand ist der Unterschied der beiden Lösungen.",
    "(x + 2)² = 25, also x + 2 = 5 oder x + 2 = −5. Die Nullstellen sind 3 und −7. Der Abstand ist 3 − (−7) = 10.",
    [B("5", "nur den waagerechten Abstand eines Schnittpunkts zur Symmetrieachse x = −2 genommen"), B("7 - 3", "die Nullstellen ohne Vorzeichen voneinander abgezogen"), B("25", "die rechte Seite als Abstand genommen")]), g="mehrschritt", regel=ZU,
    zweifel="Nur Teilregel: id.funktionen.zuordnung trägt das Setzen von y = 0, das Wurzelziehen mit zwei Lösungen und die Abstandsbildung deckt sie nicht ab")
# ───────── punkte ─────────
neu(T, "punkte", "anwenden", Z(
    "Ein Torbogen in Dubrovnik hat die Höhe h(x) = −0,02(x − 20)² + 9 (in Metern, x in Metern entlang der Straße). Wie hoch ist der Bogen bei x = 30?",
    7, "9 - 0.02 * 100", 7, "Setze x = 30 ein. Rechne erst die Klammer, dann das Quadrat, dann den Faktor −0,02.",
    "h(30) = −0,02 · (30 − 20)² + 9 = −0,02 · 100 + 9 = −2 + 9 = 7. Der Bogen ist dort 7 m hoch.",
    [B("9 - 0.02 * 10", "das Quadrat vergessen"), B("9 - 0.02 * 30 ** 2", "die 30 selbst statt den Abstand zum Scheitel quadriert"), B("9 + 0.02 * 100", "das Vorzeichen von −0,02 nicht beachtet")], einheit="m"), g="einkleidung", regel=ZU)
# ───────── bestimmen ─────────
neu(T, "bestimmen", "umkehren", Z(
    "Die Parabel y = x² + px + q geht durch die Punkte A(2|10) und B(4|32). Wie groß ist p?",
    5, "(32 - 10 - 16 + 4) / 2", 5, "Setze beide Punkte ein. Zwei Gleichungen mit p und q: Subtrahiere sie, dann fällt q weg.",
    "A: 4 + 2p + q = 10. B: 16 + 4p + q = 32. B − A: 12 + 2p = 22, also p = 5. Dann ist q = 10 − 4 − 10 = −4.",
    [B("32 - 10", "nur die y-Werte voneinander abgezogen"), B("(32 - 10) / 2", "den x-Teil 12 ignoriert"), B("4 - 2", "die x-Differenz als p genommen")]), g="rueckwaerts", ohne=OHNE_GS)
# ───────── schnittpunkte ─────────
neu(T, "schnittpunkte", "anwenden", Z(
    "Die Parabel y = x² − 4x + 1 und die Gerade y = 2x − 4 schneiden sich in zwei Punkten. Welche x-Koordinate hat der Schnittpunkt weiter rechts?",
    5, "5", 5, "Setze die beiden Funktionsterme gleich und bringe alles auf eine Seite.",
    "x² − 4x + 1 = 2x − 4 gibt x² − 6x + 5 = 0, also (x − 1)(x − 5) = 0. Die x-Koordinaten sind 1 und 5. Der rechte Schnittpunkt hat x = 5.",
    [B("1", "den linken Schnittpunkt genommen"), B("6", "die Summe der Lösungen genommen"), B("-5", "das Absolutglied mit anderem Vorzeichen genommen")]), g="mehrschritt", ohne=OHNE_GS)
# ───────── extremwert ─────────
neu(T, "extremwert", "anwenden", Z(
    "Sam zäunt am Campingplatz ein Rechteck ein, eine Längsseite liegt an einer Felswand und braucht keinen Zaun. Der Zaun ist 36 m lang. Wie viele Quadratmeter kann die Fläche höchstens haben?",
    162, "9 * 18", 162, "Nenne die Breite x. Wie lang ist dann die Seite an der Wand? Die Fläche hängt dann von x ab.",
    "Breite x, Länge 36 − 2x. Fläche A = x(36 − 2x) = −2x² + 36x. Der Scheitel liegt bei x = 36 : 4 = 9. A = 9 · 18 = 162 m².",
    [B("9", "nur die Breite des besten Rechtecks genannt"), B("18", "nur die Länge genannt"), B("18 * 18", "ein Quadrat mit der halben Zaunlänge angenommen")], einheit="m²"), g="transfer", regel=GF,
    zweifel="Extremwert: Scheitel der Parabel gesucht; gleichung_form trägt das Lesen der Form, das Aufstellen der Zielfunktion hat keine Regel")
neu(T, "extremwert", "lueckenweg", L(
    "Ein Ball fliegt nach h(t) = −5t² + 40t + 3 (Meter, t in Sekunden). Er ist nach ① Sekunden am höchsten, die größte Höhe ist ② Meter. Er steigt dabei um ③ Meter über die Starthöhe.",
    "① = □; ② = □; ③ = □", [4, 83, 80], ["40 / 10", "-5 * {1} ** 2 + 40 * {1} + 3", "{2} - 3"], ["40 / (2 * 5)", "-5 * (40 / 10) ** 2 + 40 * (40 / 10) + 3", "-5 * 4 ** 2 + 40 * 4"],
    "Der höchste Punkt ist der Scheitel. Bei y = at² + bt + c liegt er bei t = −b : (2a).",
    "t = −40 : (2 · (−5)) = 4. h(4) = −5 · 16 + 160 + 3 = 83. Die Starthöhe ist h(0) = 3, der Ball steigt um 83 − 3 = 80 m.",
    {0: [(8, None, "−b : a statt −b : (2a) gerechnet", "40 / 5")], 1: [(243, None, "−5t² mit Plus gerechnet", "5 * {1} ** 2 + 40 * {1} + 3")], 2: [(83, None, "die Höhe als Anstieg genommen", "{2}")]}), regel=GF)
