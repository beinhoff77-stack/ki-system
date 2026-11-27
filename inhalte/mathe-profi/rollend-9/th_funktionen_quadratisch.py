T = "funktionen.quadratisch"
GF = "id.funktionen.gleichung_form"
GL = "id.algebra.gleichung_loesen"
ZU = "id.funktionen.zuordnung"
fq = lambda a, b, c: (lambda x: a * x * x + b * x + c)
# ───────── scheitel ─────────
neu(T, "scheitel", "lueckenweg", L(
    "Gegeben ist f(x) = x² − 8x + 3. Die x-Koordinate des Scheitels ist ①. Dann ist der y-Wert des Scheitels ②. Die andere Stelle x ≠ 1 mit demselben Funktionswert ist ③.",
    KOMM(3), [4, -13, 7], ["8 // 2", "{1} ** 2 - 8 * {1} + 3", "2 * {1} - 1"],
    [lambda: min(range(-50, 50), key=fq(1, -8, 3)), lambda: min(fq(1, -8, 3)(x) for x in range(-50, 50)), lambda: next(x for x in range(-50, 50) if x != 1 and fq(1, -8, 3)(x) == fq(1, -8, 3)(1))],
    "Der Scheitel liegt in der Mitte zwischen den beiden Stellen mit gleichem y-Wert. Die x-Koordinate ist −b : (2a) mit den Zahlen b und a aus f(x) = ax² + bx + c.",
    "x_S = −b : (2a) = 8 : 2 = 4. f(4) = 16 − 32 + 3 = −13. Die Parabel ist symmetrisch zu x = 4: Zu x = 1 (3 links vom Scheitel) gehört x = 4 + 3 = 7. Probe: f(1) = 1 − 8 + 3 = −4 und f(7) = 49 − 56 + 3 = −4.",
    {0: [(-4, None, "die Zahl vor x halbiert (−8 : 2) und das Vorzeichen nicht gewechselt", "-8 / 2"), (8, None, "die Zahl 8 aus der Gleichung genommen", "8")], 1: [(3, None, "den y-Achsenabschnitt als y-Wert des Scheitels genommen", "3")], 2: [(5, None, "1 und 4 addiert statt gespiegelt: 1 + 4", "1 + {1}")]}), regel=GF)
neu(T, "scheitel", "bruecke", W(
    "Die Tabelle zeigt Werte einer Funktion f(x) = (x − d)² + e. Welche Gleichung gehört dazu?",
    "f(x) = (x − 2)² − 1", [("f(x) = (x + 2)² − 1", "das Vorzeichen von d verwechselt"), ("f(x) = (x − 2)² + 1", "das Vorzeichen von e verwechselt"), ("f(x) = (x − 1)² − 2", "Du liest den Scheitel als (1 | −2).")],
    "Der Scheitel ist der Punkt mit dem kleinsten y-Wert. Lies d und e daran ab und prüfe mit einem weiteren Tabellenwert.",
    "Der kleinste y-Wert −1 steht bei x = 2, also S(2 | −1) und f(x) = (x − 2)² − 1. Probe: f(0) = 4 − 1 = 3, f(4) = 4 − 1 = 3, f(1) = 1 − 1 = 0.",
    lambda: all((x - 2) ** 2 - 1 == y for x, y in zip(range(0, 5), (3, 0, -1, 0, 3))) and not all((x + 2) ** 2 - 1 == y for x, y in zip(range(0, 5), (3, 0, -1, 0, 3))) and not all((x - 2) ** 2 + 1 == y for x, y in zip(range(0, 5), (3, 0, -1, 0, 3))) and not all((x - 1) ** 2 - 2 == y for x, y in zip(range(0, 5), (3, 0, -1, 0, 3))),
    grafik=TAB(["x", "0", "1", "2", "3", "4"], ["f(x)", "3", "0", "−1", "0", "3"])), g="darstellung", regel=GF)
neu(T, "scheitel", "fehler_detektiv", FD(
    "Kim liest den Scheitel von f(x) = −2(x + 3)² + 4 ab.",
    [("Aus x + 3 = x − (−3) folgt d = 3 und e = 4.", False, None),
     ("Also ist der Scheitel S(3 | 4).", False, True),
     ("Wegen a = −2 < 0 ist S der höchste Punkt der Parabel.", False, True)],
    "Der Scheitel liegt dort, wo die Klammer null wird. Prüfe diese Stelle.",
    "Zeile 1 enthält den Fehler: x + 3 = x − (−3), also ist d = −3. Der Scheitel ist S(−3 | 4). Zeile 2 folgt aus Zeile 1. Zeile 3 ist als allgemeine Aussage richtig (a < 0: Öffnung nach unten, der Scheitel ist der höchste Punkt); falsch ist nur ihre Anwendung auf S(3 | 4), und das ist ein Folgefehler aus Zeile 1. Probe: f(−3) = 4, und f(3) = −72 + 4 = −68, also liegt S(3 | 4) nicht auf dem Graphen.",
    rueck={2: "Die Aussage selbst stimmt: Wegen a = −2 < 0 ist der Scheitel der höchste Punkt. Falsch ist nur der Punkt S(3 | 4), der aus Zeile 1 stammt; er liegt nicht auf dem Graphen. Der erste Fehler steht früher."}), g="fehler", regel=GF)

# ───────── parameter ─────────
neu(T, "parameter", "lueckenweg", L(
    "Die Parabel y = a · x² geht durch P(2 | 12). Für x = 2 ist x² gleich ①. Also ist a = ②. Dann hat der Punkt der Parabel mit x = 5 den y-Wert ③.",
    KOMM(3), [4, 3, 75], ["2 ** 2", "12 // {1}", "{2} * 5 ** 2"], ["2 * 2", "12 / (2 * 2)", "12 / 4 * 25"],
    "Setze die Koordinaten von P in die Gleichung ein und löse nach a.",
    "Für P gilt 12 = a · 2² = a · 4, also a = 3. Dann ist y = 3 · 5² = 75. Probe: 3 · 4 = 12.",
    {0: [(2, None, "x selbst statt x² genommen", "2")], 1: [(6, None, "durch x statt durch x² geteilt: 12 : 2", "12 // 2")], 2: [(15, None, "5 nicht quadriert: 3 · 5", "{2} * 5")]}), regel=GF)
neu(T, "parameter", "bruecke", W(
    "Die Zeichnung zeigt die Parabel y = x² und eine zweite Parabel y = a · x² durch den markierten Punkt P. Welcher Wert gehört zu a?",
    "a = 0,5", [("a = 2", "den y-Wert von P als a genommen"), ("a = 4", "den quadrierten x-Wert von P als a genommen"), ("a = −0,5", "das Vorzeichen verändert: dann wäre die Parabel nach unten geöffnet")],
    "Lies die Koordinaten von P ab und setze sie in y = a · x² ein.",
    "P hat die Koordinaten (2 | 2). Aus 2 = a · 2² = 4a folgt a = 0,5. Die Parabel ist flacher als y = x², weil 0 < a < 1.",
    lambda: 0.5 * 2 ** 2 == 2 and 2 * 2 ** 2 != 2 and 4 * 2 ** 2 != 2 and -0.5 * 2 ** 2 != 2,
    grafik=KO([-4, 4], [-2, 6], graphen=[{"art": "poly", "k": [0, 0, 1], "name": "y = x²"}, {"art": "poly", "k": [0, 0, 0.5], "name": "y = a · x²"}], punkte=[{"x": 2, "y": 2, "name": "P"}])), g="darstellung", regel=GF)
neu(T, "parameter", "fehler_detektiv", FD(
    "Kim vergleicht die Parabel g(x) = −0,5x² mit der Parabel f(x) = x².",
    [("Der Faktor a = −0,5 hat den Betrag 0,5.", abs(-0.5) == 0.5, None),
     ("Wegen a < 0 ist g nach unten geöffnet.", -0.5 < 0, None),
     ("Der Scheitel von g liegt im Ursprung.", -0.5 * 0 ** 2 == 0, None),
     ("Weil 0,5 kleiner als 1 ist, ist g enger als f.", abs(-0.5 * 2 ** 2) > 2 ** 2, None)],
    "Vergleiche die Beträge der y-Werte von g und f an derselben Stelle, zum Beispiel x = 2.",
    "Die Zeilen 1 bis 3 stimmen. In Zeile 4 steht der Fehler: Bei x = 2 ist g(2) = −2 und f(2) = 4. Die y-Werte von g sind betragsmäßig kleiner, also ist g weiter (flacher) als f. Ein Faktor mit Betrag kleiner als 1 macht die Parabel weiter."), g="fehler", regel=GF)

# ───────── spiegeln ─────────
neu(T, "spiegeln", "lueckenweg", L(
    "Die Parabel f(x) = x² − 6x + 13 hat den Scheitel S(① | ②). Spiegle jeweils die Ausgangsparabel. Spiegelt man an der x-Achse, so hat der neue Scheitel die y-Koordinate ③. Spiegelt man dagegen an der y-Achse, so hat der neue Scheitel die x-Koordinate ④.",
    KOMM(4), [3, 4, -4, -3], ["6 // 2", "{1} ** 2 - 6 * {1} + 13", "-{2}", "-{1}"],
    [lambda: min(range(-50, 50), key=fq(1, -6, 13)), lambda: min(fq(1, -6, 13)(x) for x in range(-50, 50)), lambda: -min(fq(1, -6, 13)(x) for x in range(-50, 50)), lambda: -min(range(-50, 50), key=fq(1, -6, 13))],
    "Spiegeln an der x-Achse ändert die Vorzeichen der y-Werte. Spiegeln an der y-Achse ändert die Vorzeichen der x-Werte.",
    "x_S = 6 : 2 = 3, y_S = 9 − 18 + 13 = 4. An der x-Achse gespiegelt: S′(3 | −4). An der y-Achse gespiegelt: S″(−3 | 4).",
    {0: [(-3, None, "die Zahl vor x halbiert (−6 : 2) und das Vorzeichen nicht gewechselt", "-6 / 2")], 1: [(13, None, "den y-Achsenabschnitt als y-Wert des Scheitels genommen", "13")], 2: [(4, None, "die y-Koordinate beim Spiegeln nicht verändert", "{2}")], 3: [(3, None, "die x-Koordinate beim Spiegeln an der y-Achse nicht verändert", "{1}")]}), regel=GF)
neu(T, "spiegeln", "umkehren", Z(
    "Die Parabel g(x) = −(x − 3)² + 5 entsteht aus der Parabel f durch Spiegelung an der x-Achse. Wie groß ist f(0)?",
    4, "(0 - 3) ** 2 - 5", lambda: -(-(0 - 3) ** 2 + 5),
    "Mache die Spiegelung rückgängig: Beim Spiegeln an der x-Achse wechseln alle y-Werte ihr Vorzeichen.",
    "Zurückgespiegelt gilt f(x) = −g(x) = (x − 3)² − 5. Dann ist f(0) = 9 − 5 = 4. Probe: g(0) = −9 + 5 = −4, und −(−4) = 4.",
    [(-4, None, "g(0) statt f(0) berechnet", "-(0 - 3) ** 2 + 5"), (14, None, "5 addiert statt abgezogen: 9 + 5", "(0 - 3) ** 2 + 5"), (-14, None, "beide Vorzeichen falsch: −9 − 5", "-(0 - 3) ** 2 - 5")]), g="umkehr", regel=GF)
neu(T, "spiegeln", "fehler_detektiv", FD(
    "Kim spiegelt f(x) = (x − 2)² + 3 an der y-Achse.",
    [("Bei der Spiegelung an der y-Achse wird x durch −x ersetzt.", True, None),
     ("Also ist g(x) = f(−x) = (−x − 2)² + 3.", all(fq(1, -4, 7)(-x) == (-x - 2) ** 2 + 3 for x in range(-4, 5)), None),
     ("Es gilt (−x − 2)² = (x + 2)².", all((-x - 2) ** 2 == (x + 2) ** 2 for x in range(-4, 5)), None),
     ("Also ist g(x) = (x + 2)² − 3.", all((x + 2) ** 2 - 3 == (x + 2) ** 2 + 3 for x in range(-4, 5)), None)],
    "Prüfe jede Zeile an einem Punkt. Was bleibt beim Spiegeln an der y-Achse gleich?",
    "Die Zeilen 1 bis 3 stimmen: g(x) = (x + 2)² + 3. In Zeile 4 wurde das Vorzeichen von e verändert. Bei der Spiegelung an der y-Achse bleibt e gleich. Probe: g(0) = 7 = f(0)."), g="fehler", regel=GF)

# ───────── umformen ─────────
neu(T, "umformen", "lueckenweg", L(
    "Bringe f(x) = x² + 6x + 4 auf die Form (x + d)² + e. Die Zahl d ist ①. Für die quadratische Ergänzung addiert und subtrahiert man ②. Dann ist e = ③.",
    KOMM(3), [3, 9, -5], ["6 // 2", "{1} ** 2", "4 - {2}"], ["6 / 2", "(6 / 2) * (6 / 2)", "4 - (6 / 2) ** 2"],
    "Halbiere die Zahl vor x. Das Quadrat dieser Zahl wird addiert und gleichzeitig wieder abgezogen.",
    "d = 6 : 2 = 3. x² + 6x + 9 − 9 + 4 = (x + 3)² − 5. Also ist e = 4 − 9 = −5. Probe: f(0) = 4 und (0 + 3)² − 5 = 4.",
    {0: [(6, None, "die Zahl 6 nicht halbiert", "6")], 1: [(36, None, "6 nur quadriert statt halbiert und quadriert: 6²", "6 ** 2"), (3, None, "nur halbiert: 6 : 2", "{1}")], 2: [(13, None, "9 addiert statt abgezogen: 4 + 9", "4 + {2}")]}), regel=GF)
neu(T, "umformen", "bruecke", W(
    "Welche Scheitelform gehört zu f(x) = x² − 8x + 19?",
    "f(x) = (x − 4)² + 3", [("f(x) = (x + 4)² + 3", "das Vorzeichen von d verwechselt"), ("f(x) = (x − 4)² + 19", "den Wert e nicht angepasst"), ("f(x) = (x − 4)² + 35", "16 addiert statt abgezogen: 19 + 16")],
    "Halbiere die Zahl vor x und gleiche die Ergänzung bei der Konstanten aus. Prüfe mit x = 0.",
    "x² − 8x + 16 − 16 + 19 = (x − 4)² + 3. Probe: f(0) = 19 und (0 − 4)² + 3 = 19.",
    lambda: all(x * x - 8 * x + 19 == (x - 4) ** 2 + 3 for x in range(-5, 6)) and not all(x * x - 8 * x + 19 == (x + 4) ** 2 + 3 for x in range(-5, 6)) and not all(x * x - 8 * x + 19 == (x - 4) ** 2 + 19 for x in range(-5, 6)) and not all(x * x - 8 * x + 19 == (x - 4) ** 2 + 35 for x in range(-5, 6))), g="darstellung", regel=GF)
neu(T, "umformen", "zwei_wege", Z(
    "Bestimme den Scheitel von f(x) = 2x² − 12x + 7 auf zwei Wegen. Weg A: quadratische Ergänzung (erst 2 ausklammern). Weg B: x-Koordinate mit x = −b : (2a) bestimmen und in f einsetzen. Wie groß ist die y-Koordinate des Scheitels?",
    -11, "2 * 3 ** 2 - 12 * 3 + 7", lambda: min(2 * x * x - 12 * x + 7 for x in range(-50, 50)),
    "Beide Wege müssen dieselbe y-Koordinate ergeben.",
    "Weg A: 2(x² − 6x) + 7 = 2((x − 3)² − 9) + 7 = 2(x − 3)² − 18 + 7 = 2(x − 3)² − 11. Weg B: x = 12 : 4 = 3, f(3) = 18 − 36 + 7 = −11. Der Scheitel ist S(3 | −11).",
    [(-2, None, "beim Ausgleichen den Faktor 2 vergessen: −9 + 7", "-9 + 7"), (25, None, "den Ausgleich −2 · 9 mit falschem Vorzeichen addiert: 7 + 2 · 9", "7 + 2 * 9"), (7, None, "den y-Achsenabschnitt als y-Koordinate des Scheitels genommen", "7")]), g="verknuepfen", regel=GF)

# ───────── nullstellen ─────────
neu(T, "nullstellen", "lueckenweg", L(
    "Berechne die Nullstellen von f(x) = 6(x − 3)² − 24. Für f(x) = 0 gilt (x − 3)² = ①. Die größere Nullstelle ist ②. Dann ist die kleinere Nullstelle ③.",
    KOMM(3), [4, 5, 1], ["24 // 6", "5", "6 - {2}"], ["24 / 6", "3 + wz(24 / 6)", "3 - wz(24 / 6)"],
    "Löse f(x) = 0 wie eine Gleichung: erst 24 auf die andere Seite, dann durch den Faktor teilen. Die beiden Nullstellen liegen gleich weit von der Mitte entfernt.",
    "6(x − 3)² = 24 gibt (x − 3)² = 4. Also x − 3 = 2 oder x − 3 = −2, das heißt x = 5 oder x = 1. Probe: 6 · (5 − 3)² − 24 = 0 und 6 · (1 − 3)² − 24 = 0.",
    {0: [(18, None, "24 − 6 gerechnet", "24 - 6"), (144, None, "24 · 6 gerechnet", "24 * 6")], 1: [(2, None, "nur die Wurzel genommen, die 3 vergessen", "2")], 2: [(-5, None, "die Gegenzahl der größeren Nullstelle genommen: −5", "-5")]}), regel=GL)
neu(T, "nullstellen", "zwei_wege", Z(
    "Wie groß ist der Abstand der beiden Nullstellen von f(x) = x² − 2x − 8? Weg A: Lösungsformel. Weg B: Scheitelform aufstellen und die Symmetrie zur Achse nutzen.",
    6, "4 - (-2)", lambda: max(x for x in range(-50, 50) if x * x - 2 * x - 8 == 0) - min(x for x in range(-50, 50) if x * x - 2 * x - 8 == 0),
    "Beide Wege müssen denselben Abstand ergeben.",
    "Weg A: D = 4 + 32 = 36, x = (2 ± 6) : 2 gibt 4 und −2. Abstand 4 − (−2) = 6. Weg B: f(x) = (x − 1)² − 9. Die Nullstellen liegen bei x = 1 ± 3, also 3 links und 3 rechts der Achse. Abstand 6.",
    [(3, None, "nur den Abstand einer Nullstelle zur Symmetrieachse genommen", "3"), (2, None, "die Anzahl der Nullstellen statt ihres Abstands angegeben", "2")]), regel=GL)
neu(T, "nullstellen", "umkehren", Z(
    "Die Parabel y = x² + bx + c hat die Nullstellen x = 3 und x = −5. Wie groß ist c?",
    -15, "3 * (-5)", lambda: next(c for c in range(-100, 100) if all(x * x + (2) * x + c == 0 for x in (3, -5))),
    "Die Nullstellen bestimmen die Faktoren der Parabel. Wie kommst du daraus auf b und c?",
    "(x − 3)(x + 5) = x² + 2x − 15. Also ist b = 2 und c = −15. Probe: 9 + 6 − 15 = 0 und 25 − 10 − 15 = 0.",
    [(15, "fb.vorzeichen.falsches_zeichen", "(−3) · 5 als 3 · 5 gerechnet: das Minus des Produkts vergessen", "3 * 5"), (2, None, "b statt c angegeben: −(3 + (−5))", "-(3 + (-5))"), (-2, None, "die Summe der Nullstellen genommen: 3 + (−5)", "3 + (-5)")]), g="rueckwaerts", regel=GL)

# ───────── punkte ─────────
neu(T, "punkte", "lueckenweg", L(
    "Prüfe, ob P(4 | 12) auf der Parabel y = x² − 5 liegt. Für x = 4 ist x² gleich ①. Dann ist y = ②. Also ist der y-Wert von P um ③ größer als der y-Wert der Parabel.",
    KOMM(3), [16, 11, 1], ["4 ** 2", "{1} - 5", "12 - {2}"], ["4 * 4", "4 * 4 - 5", "12 - (4 * 4 - 5)"],
    "Setze x = 4 in die Gleichung der Parabel ein und vergleiche mit dem y-Wert von P.",
    "4² = 16. Dann ist y = 16 − 5 = 11. Der Punkt P hat y = 12, das ist um 1 mehr. Also liegt P nicht auf der Parabel.",
    {0: [(8, None, "4 mit 2 malgenommen statt quadriert: 4 · 2", "4 * 2")], 1: [(21, None, "5 addiert statt abgezogen: 16 + 5", "{1} + 5")], 2: [(-1, None, "den Unterschied andersherum gerechnet: 11 − 12", "{2} - 12")]}), regel=ZU)
neu(T, "punkte", "umkehren", Z(
    "Der Punkt Q(a | 5) mit a > 0 liegt auf der Parabel y = x² − 4. Wie groß ist a?",
    3, "(5 + 4) / 3", lambda: next(a for a in range(1, 50) if a * a - 4 == 5),
    "Setze y = 5 in die Gleichung der Parabel ein und löse nach x.",
    "5 = a² − 4 gibt a² = 9. Wegen a > 0 ist a = 3. Probe: 3² − 4 = 5.",
    [(1, None, "5 − 4 gerechnet", "5 - 4"), (9, None, "5 + 4 gerechnet, die Wurzel nicht gezogen", "5 + 4")]), g="umkehr", regel=ZU)
neu(T, "punkte", "fehler_detektiv", FD(
    "Kim prüft, ob P(−3 | 14) auf der Parabel f(x) = x² − 2x − 1 liegt.",
    [("Einsetzen: f(−3) = −3² − 2 · (−3) − 1.", fq(1, -2, -1)(-3) == -(3 ** 2) - 2 * (-3) - 1, None),
     ("= −9 + 6 − 1 = −4", False, -9 + 6 - 1 == -4),
     ("Wegen −4 ≠ 14 liegt P nicht auf der Parabel.", False, -4 != 14)],
    "Prüfe, wie Zeile 1 aus f(x) = x² − 2x − 1 durch Einsetzen von x = −3 entsteht.",
    "Zeile 1 enthält den Fehler: (−3)² = 9, aber −3² = −9. Richtig: f(−3) = 9 + 6 − 1 = 14. Also liegt P auf der Parabel. Die Zeilen 2 und 3 rechnen mit dem falschen Wert richtig weiter."), g="fehler", regel=ZU)

# ───────── bestimmen ─────────
neu(T, "bestimmen", "lueckenweg", L(
    "Eine Parabel hat den Scheitel S(1 | −5) und geht durch P(4 | 22). Ihre Gleichung ist f(x) = a · (x − 1)² − 5. Setzt man P ein, gilt a · ① = ②. Dabei ist ① das Quadrat des waagrechten Abstands von P zum Scheitel, und ② ist der senkrechte Abstand von P zum Scheitel. Also ist a = ③.",
    KOMM(3), [9, 27, 3], ["(4 - 1) ** 2", "22 + 5", "{2} // {1}"], ["3 * 3", "22 - (-5)", "27 / 9"],
    "Setze x = 4 und y = 22 in die Gleichung ein und bringe die −5 auf die andere Seite.",
    "22 = a · (4 − 1)² − 5 gibt 27 = 9a, also a = 3. Die Gleichung ist f(x) = 3(x − 1)² − 5. Probe: 3 · 9 − 5 = 22.",
    {0: [(3, None, "den Abstand nicht quadriert: 4 − 1", "4 - 1")], 1: [(17, None, "5 abgezogen statt addiert: 22 − 5", "22 - 5")], 2: [(9, None, "Du hast durch den waagrechten Abstand 3 statt durch sein Quadrat 9 geteilt: 27 : 3 = 9.", "{2} / 3")]}), regel=GF)
neu(T, "bestimmen", "bruecke", W(
    "Die Zeichnung zeigt eine Parabel mit dem Scheitel S und dem Punkt P. Welche Gleichung hat sie?",
    "f(x) = (x − 2)² − 1", [("f(x) = (x + 2)² − 1", "das Vorzeichen von d verwechselt"), ("f(x) = 2(x − 2)² − 1", "einen falschen Faktor a gewählt: P liegt dann nicht auf der Parabel"), ("f(x) = (x − 2)² + 1", "das Vorzeichen von e verwechselt")],
    "Lies den Scheitel ab und setze dann P in die Gleichung ein, um a zu bestimmen.",
    "S(2 | −1) gibt f(x) = a(x − 2)² − 1. Mit P(4 | 3): 3 = a · 4 − 1, also a = 1. Probe: (4 − 2)² − 1 = 3.",
    lambda: (4 - 2) ** 2 - 1 == 3 and 2 * (4 - 2) ** 2 - 1 != 3 and (4 + 2) ** 2 - 1 != 3 and (4 - 2) ** 2 + 1 != 3,
    grafik=KO([-1, 6], [-3, 6], graphen=[{"art": "poly", "k": [3, -4, 1]}], punkte=[{"x": 2, "y": -1, "name": "S"}, {"x": 4, "y": 3, "name": "P"}])), g="darstellung", regel=GF)
neu(T, "bestimmen", "anwenden", Z(
    "Ein parabelförmiger Brückenbogen ist in der Mitte 5 m hoch. Mit x als waagrechtem Abstand von der Mitte (in m) gilt für die Höhe h(x) = a · x² + 5. Am Rand, 10 m von der Mitte entfernt, ist die Höhe 0. Wie hoch ist der Bogen 6 m von der Mitte entfernt?",
    3.2, "-5 / 10 ** 2 * 6 ** 2 + 5", lambda: F(-5, 100) * 6 ** 2 + 5,
    "Eine Angabe der Aufgabe legt a fest. Welche hast du noch nicht benutzt?",
    "Am Rand: 0 = a · 10² + 5, also a = −5 : 100 = −0,05. Dann ist h(6) = −0,05 · 36 + 5 = −1,8 + 5 = 3,2 m.",
    [(1.8, None, "den Höhenverlust statt der Höhe angegeben: 5 − 3,2", "5 - 3.2"), (4.7, None, "den Abstand nicht quadriert: 5 − 0,05 · 6", "5 - 0.05 * 6"), (-1.8, None, "die 5 m Höhe in der Mitte vergessen: −0,05 · 36", "-0.05 * 6 ** 2")], "m"), g="transfer", regel=GF)

# ───────── schnittpunkte ─────────
neu(T, "schnittpunkte", "lueckenweg", L(
    "Die Parabel y = x² und die Gerade y = 2x + 15 schneiden sich. Gleichsetzen und sortieren gibt x² − 2x − 15 = 0. Die größere x-Koordinate der Schnittpunkte ist ①. Dann ist die kleinere x-Koordinate ②. Also hat der rechte Schnittpunkt den y-Wert ③.",
    KOMM(3), [5, -3, 25], ["5", "2 - {1}", "{1} ** 2"], [lambda: max(x for x in range(-50, 50) if x * x == 2 * x + 15), lambda: min(x for x in range(-50, 50) if x * x == 2 * x + 15), lambda: max(x for x in range(-50, 50) if x * x == 2 * x + 15) ** 2],
    "Die beiden Lösungen einer Gleichung x² − 2x − 15 = 0 haben zusammen den Wert 2. Den y-Wert findest du mit der Gleichung der Parabel.",
    "x² − 2x − 15 = (x − 5)(x + 3) = 0 gibt x = 5 oder x = −3. Der rechte Schnittpunkt ist (5 | 25). Probe: 2 · 5 + 15 = 25 und 5² = 25.",
    {0: [(-3, None, "die kleinere Lösung angegeben", "-3"), (15, None, "die Zahl 15 aus der Gleichung abgeschrieben", "15")], 1: [(3, None, "aus x + 3 = 0 die Lösung x = 3 gemacht statt x = −3", "3")], 2: [(10, None, "nur 2 · 5 gerechnet, die 15 vergessen", "2 * {1}")]}), regel=GL)
neu(T, "schnittpunkte", "bruecke", W(
    "Die Zeichnung zeigt die Graphen von y = x² − 4 und y = x − 2. Welche Gleichung gehört zu den Schnittpunkten, und welche Lösungen hat sie?",
    "x² − 4 = x − 2 mit x = 2 und x = −1", [("x² − 4 = x − 2 mit x = −2 und x = 1", "die Vorzeichen der Lösungen vertauscht"), ("x² − 4 = x + 2 mit x = 3 und x = −2", "die Gerade falsch abgelesen"), ("x² − 4 = x − 2 mit x = 2", "die zweite Lösung vergessen")],
    "Schnittpunkte haben auf beiden Graphen denselben y-Wert. Prüfe die Lösungen im Bild.",
    "Gleichsetzen: x² − 4 = x − 2, also x² − x − 2 = 0 und (x − 2)(x + 1) = 0. Die Lösungen sind x = 2 und x = −1. Im Bild: Bei x = 2 sind beide y-Werte 0, bei x = −1 beide −3.",
    lambda: all(x * x - 4 == x - 2 for x in (2, -1)) and not any(x * x - 4 == x - 2 for x in (-2, 1)) and all(x * x - 4 == x + 2 for x in (3, -2)),
    grafik=KO([-4, 4], [-5, 6], graphen=[{"art": "poly", "k": [-4, 0, 1], "name": "y = x² − 4"}, {"art": "linear", "m": 1, "t": -2, "name": "y = x − 2"}])), g="darstellung", regel=GL)
neu(T, "schnittpunkte", "umkehren", Z(
    "Für welchen Wert von c berührt die Gerade y = 2x + c die Parabel y = x² in genau einem Punkt?",
    -1, "-(2 ** 2) / 4", lambda: next(c for c in range(-50, 50) if 4 + 4 * c == 0),
    "Gleichsetzen gibt eine quadratische Gleichung. Überlege, wie viele Lösungen sie bei einem Berührpunkt hat.",
    "x² = 2x + c gibt x² − 2x − c = 0. Genau eine Lösung heißt D = 0: D = 4 + 4c = 0, also c = −1. Probe: x² − 2x + 1 = (x − 1)² hat die einzige Lösung x = 1.",
    [(1, None, "beim Auflösen von 4c = −4 das Minus weggelassen: c = 4 : 4", "4 / 4"), (0, None, "die Gerade durch den Ursprung gewählt", "0")]), g="parameter", regel=GL)

# ───────── extremwert ─────────
neu(T, "extremwert", "lueckenweg", L(
    "Ein Rechteck hat 40 m Umfang. Eine Seite ist x m lang, die andere (20 − x) m. Die Fläche A(x) = x · (20 − x) ist am größten für x = ①. Dann ist die größte Fläche ② m². Also ist die Fläche für x = 8 um ③ m² kleiner.",
    KOMM(3), [10, 100, 4], ["20 // 2", "{1} * (20 - {1})", "{2} - 8 * (20 - 8)"], [lambda: max(range(0, 21), key=lambda x: x * (20 - x)), lambda: max(x * (20 - x) for x in range(0, 21)), lambda: max(x * (20 - x) for x in range(0, 21)) - 96],
    "Die Parabel A(x) hat ihre Nullstellen bei x = 0 und x = 20. Der höchste Punkt liegt genau in der Mitte.",
    "A(x) = −x² + 20x hat den Scheitel bei x = 10. A(10) = 10 · 10 = 100 m². Für x = 8 ist A(8) = 8 · 12 = 96 m². Der Unterschied ist 4 m².",
    {0: [(20, None, "die Zahl 20 aus der Aufgabe genommen", "20")], 1: [(200, None, "10 mit 20 malgenommen", "{1} * 20")], 2: [(96, None, "die Fläche für x = 8 statt des Unterschieds angegeben", "8 * (20 - 8)")]}), regel=GF)
neu(T, "extremwert", "anwenden", Z(
    "Ein Ball wird senkrecht nach oben geworfen. Seine Höhe über dem Boden ist h = −5t² + 30t (h in Metern, t in Sekunden). Wie hoch fliegt der Ball höchstens?",
    45, "-5 * 3 ** 2 + 30 * 3", lambda: max(-5 * t * t + 30 * t for t in range(0, 10)),
    "Der höchste Punkt ist der Scheitel der Parabel. Bestimme zuerst die Zeit t dafür.",
    "Nullstellen bei t = 0 und t = 6, also liegt der Scheitel bei t = 3. h(3) = −45 + 90 = 45 m.",
    [(3, None, "die Zeit statt der Höhe angegeben", "3"), (90, None, "nur 30 · 3 gerechnet, den Abzug vergessen", "30 * 3"), (135, None, "den Abzug addiert: 90 + 45", "30 * 3 + 5 * 3 ** 2")], "m"), g="einkleidung", regel=GF)
neu(T, "extremwert", "fehler_detektiv", FD(
    "Kim sucht die größte Fläche eines Rechtecks mit 36 m Umfang.",
    [("Die Seiten sind x und 18 − x.", True, None),
     ("Die Fläche ist A(x) = x · (18 − x) = −x² + 18x.", all(x * (18 - x) == -x * x + 18 * x for x in range(0, 19)), None),
     ("Die Parabel ist nach oben geöffnet, also ist ihr Scheitel der tiefste Punkt und damit die kleinste Fläche.", False, None),
     ("Die kleinste Fläche ist 81 m² bei x = 9.", False, 9 * (18 - 9) == 81)],
    "Prüfe die Aussage in Zeile 3 an einigen Werten von A(x), zum Beispiel A(5), A(9) und A(13).",
    "Die Zeilen 1 und 2 stimmen. In Zeile 3 steht der Fehler: Die Zahl vor x² ist −1, die Parabel ist nach unten geöffnet. Der Scheitel ist der höchste Punkt, also die größte Fläche. Zeile 4 rechnet richtig mit A(9) = 81 weiter. Richtig: Die größte Fläche ist 81 m²."), g="fehler", regel=GF)
