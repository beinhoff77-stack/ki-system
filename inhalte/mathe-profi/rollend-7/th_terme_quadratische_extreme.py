T = "terme.quadratische_extreme"
# ───────── ergaenzen ─────────
neu(T, "ergaenzen", "lueckenweg", L(
    "Ergänze x² − 10x zu einem vollständigen Quadrat der Form (x + ①)². Dafür musst du zuerst ② addieren. Es gilt dann x² − 10x + ② = (x + ①)².",
    KOMM(2), [-5, 25], ["-10 // 2", "{1} ** 2"], ["-5", "25"], "Nimm die Hälfte der Zahl vor x. Die Ergänzung ist deren Quadrat.",
    "Die Hälfte von −10 ist −5. (−5)² = 25. Also x² − 10x + 25 = (x − 5)².",
    {0: [(5, "fb.vorzeichen.falsches_zeichen", "das Minus der Hälfte vergessen", "10 // 2"), (-10, None, "nicht halbiert", "-10")], 1: [(-25, "fb.reihenfolge.minus_ins_quadrat", "(−5)² als −5² gerechnet, also −25", "-(5 ** 2)"), (10, None, "die Zahl 10 selbst statt der Ergänzung genommen", "10")]}), regel="rr.potenz")
neu(T, "ergaenzen", "fehler_detektiv", FD(
    "Kim bringt T(x) = x² + 8x + 3 in die Scheitelform.",
    [("Die Hälfte von 8 ist 4, und 4² = 16.", True), ("x² + 8x + 16 = (x + 4)²", gl("x**2+8*x+16", "(x+4)**2")), ("Also ist T(x) = (x + 4)² + 3.", gl("x**2+8*x+3", "(x+4)**2+3")), ("Der Scheitel ist S(−4 | 3).", True)],
    "Du hast 16 addiert. Was musst du dann tun, damit der Term derselbe bleibt? Prüfe mit x = 0.",
    "Die addierte 16 muss wieder abgezogen werden: T(x) = (x + 4)² + 3 − 16 = (x + 4)² − 13. Probe mit x = 0: 16 − 13 = 3."), regel="rr.potenz")
neu(T, "ergaenzen", "umkehren", Z(
    "Für welche positive Zahl b gilt x² + bx + 36 = (x + c)² für alle Zahlen x, mit einem positiven c?",
    12, "2 * 6", 12, "Zerlege 36 als Quadrat: c · c = 36. Das mittlere Glied ist das doppelte Produkt.",
    "c² = 36, also c = 6. Dann ist b = 2 · 6 = 12. Probe: (x + 6)² = x² + 12x + 36.",
    [(6, None, "die 2 im doppelten Produkt vergessen: nur 6", "6"), (18, None, "36 : 2 gerechnet", "36 / 2"), (72, None, "2 · 36 gerechnet", "2 * 36")]), g="umkehr", regel="rr.potenz")
assert gl("x**2+12*x+36", "(x+6)**2")

# ───────── scheitelform ─────────
neu(T, "scheitelform", "lueckenweg", L(
    "Bringe x² + 6x + 4 mit quadratischer Ergänzung in die Form (x + ①)² − ②. Du addierst eine Zahl und ziehst sie wieder ab.",
    KOMM(2), [3, 5], ["6 // 2", "{1} ** 2 - 4"], ["3", "9 - 4"], "Die Zahl in der Klammer ist die Hälfte der Zahl vor x. Das Quadrat davon wird addiert und abgezogen.",
    "x² + 6x + 9 − 9 + 4 = (x + 3)² − 5. Probe mit x = 0: 9 − 5 = 4.",
    {0: [(6, None, "nicht halbiert", "6")], 1: [(13, "fb.vorzeichen.falsches_zeichen", "9 + 4 gerechnet statt 9 − 4", "{1} ** 2 + 4")]}), regel="rr.potenz")
assert gl("x**2+6*x+4", "(x+3)**2-5")
neu(T, "scheitelform", "bruecke", W(
    "Die Tabelle zeigt einige Werte von T(x) = x² − 6x + 5. Welche Scheitelform gehört zu diesem Term?",
    "(x − 3)² − 4", [("(x − 3)² + 4", "das Vorzeichen der Zahl hinter der Klammer vertauscht"), ("(x + 3)² − 4", "das Vorzeichen in der Klammer vertauscht"), ("(x − 5)² − 4", "die Zahl 5 aus dem Term als Scheitelstelle genommen")],
    "Der tiefste Wert der Tabelle liegt in der Mitte. Seine x-Stelle steht in der Klammer, sein Wert dahinter.",
    "Der kleinste Wert −4 steht bei x = 3. Die Scheitelform ist (x − 3)² − 4. Probe: (x − 3)² − 4 = x² − 6x + 9 − 4 = x² − 6x + 5.",
    lambda: gl("x**2-6*x+5", "(x-3)**2-4") and not gl("x**2-6*x+5", "(x-3)**2+4") and not gl("x**2-6*x+5", "(x+3)**2-4") and not gl("x**2-6*x+5", "(x-5)**2-4"),
    grafik=TAB(["x", "1", "2", "3", "4", "5"], ["T(x)", "0", "−3", "−4", "−3", "0"])), regel="id.funktionen.gleichung_form")
neu(T, "scheitelform", "zwei_wege", Z(
    "Berechne T(7) für T(x) = x² − 6x + 5 auf zwei Wegen. Weg A: x = 7 direkt einsetzen. Weg B: zuerst in die Scheitelform (x − 3)² − 4 umformen, dann x = 7 einsetzen. Welchen Wert erhältst du?",
    12, "7 ** 2 - 6 * 7 + 5", "(7 - 3) ** 2 - 4", "Beide Wege müssen denselben Wert ergeben.",
    "Weg A: 49 − 42 + 5 = 12. Weg B: (7 − 3)² − 4 = 16 − 4 = 12.",
    [(16, None, "bei Weg B das − 4 vergessen", "(7 - 3) ** 2"), (96, "fb.vorzeichen.falsches_zeichen", "(7 + 3)² − 4 gerechnet", "(7 + 3) ** 2 - 4")]), regel="id.funktionen.gleichung_form")

# ───────── extremwert ─────────
neu(T, "extremwert", "lueckenweg", L(
    "Bestimme das Minimum von T(x) = x² − 8x + 19. Die Scheitelform lautet (x − ①)² + ②. Setzt du x = 6 in diese Form ein, erhältst du den Wert ③.",
    KOMM(3), [4, 3, 7], ["8 // 2", "19 - {1} ** 2", "(6 - {1}) ** 2 + {2}"], ["4", "3", "4 + 3"], "Halbiere die Zahl vor x. Das Quadrat davon ziehst du von 19 ab.",
    "x² − 8x + 16 − 16 + 19 = (x − 4)² + 3. Das Minimum 3 liegt bei x = 4. Für x = 6: 4 + 3 = 7.",
    {1: [(35, "fb.vorzeichen.falsches_zeichen", "16 + 19 gerechnet statt 19 − 16", "{1} ** 2 + 19")], 0: [(8, None, "nicht halbiert", "8")]}), regel="id.funktionen.gleichung_form")
assert gl("x**2-8*x+19", "(x-4)**2+3")
neu(T, "extremwert", "anwenden", Z(
    "Ein Ball wird geworfen. Seine Höhe in Metern nach t Sekunden ist h(t) = −t² + 6t + 1 (für t von 0 bis 6). Wie hoch kommt der Ball höchstens?",
    10, "-(3) ** 2 + 6 * 3 + 1", 10, "Bringe h(t) in die Scheitelform. Wegen des Minuszeichens vor t² ist der Scheitel ein Maximum.",
    "−t² + 6t + 1 = −(t − 3)² + 10. Das Maximum 10 liegt bei t = 3. Der Ball kommt höchstens 10 m hoch.",
    [(1, None, "die Höhe zu Beginn genommen: h(0)", "-(0) ** 2 + 6 * 0 + 1"), (3, None, "die Zeit des Maximums statt der Höhe angegeben", "6 // 2"), (6, None, "die Zahl vor t genommen", "6")], "m"), g="einkleidung", regel="id.funktionen.gleichung_form")
assert gl("-t**2+6*t+1".replace("t", "x"), "-(x-3)**2+10")
neu(T, "extremwert", "umkehren", Z(
    "Die Funktion T(x) = (x − 3)² + c hat das Minimum 7. Welchen Wert hat T(5)?",
    11, "(5 - 3) ** 2 + 7", 11, "Das Minimum von (x − 3)² + c ist c. Wo liegt das Minimum?",
    "Das Minimum ist c = 7. Dann ist T(5) = (5 − 3)² + 7 = 4 + 7 = 11.",
    [(7, None, "das Minimum statt T(5) genommen", "7"), (9, "fb.potenz.basis_mal_hochzahl", "(5 − 3) nicht quadriert: 2 + 7", "(5 - 3) + 7"), (-3, "fb.vorzeichen.falsches_zeichen", "4 − 7 statt 4 + 7 gerechnet", "(5 - 3) ** 2 - 7")]), g="rueckwaerts", regel="id.funktionen.gleichung_form")

# ───────── mit_faktor ─────────
neu(T, "mit_faktor", "lueckenweg", L(
    "Bestimme das Minimum von T(x) = 2x² − 12x + 22. Klammere 2 bei den ersten beiden Gliedern aus: 2(x² − ①x) + 22. Ergänze in der Klammer: 2(x − ②)² − ③ + 22. Das Minimum ist ④.",
    KOMM(4), [6, 3, 18, 4], ["12 // 2", "{1} // 2", "2 * {2} ** 2", "22 - {3}"], ["6", "3", "18", "4"], "Die ergänzte Zahl steht in der Klammer und wird mit dem Faktor vor der Klammer malgenommen.",
    "2x² − 12x = 2(x² − 6x) = 2((x − 3)² − 9) = 2(x − 3)² − 18. Dazu 22: 2(x − 3)² + 4. Das Minimum ist 4 bei x = 3.",
    {2: [(9, None, "den Faktor vor der Klammer vergessen", "{2} ** 2")], 3: [(13, None, "22 − 9 gerechnet, den Faktor 2 vergessen", "22 - {2} ** 2")], 0: [(12, None, "nicht durch den Faktor geteilt", "12")]}), regel="id.funktionen.gleichung_form")
assert gl("2*x**2-12*x+22", "2*(x-3)**2+4")
neu(T, "mit_faktor", "fehler_detektiv", FD(
    "Kim bestimmt das Minimum von T(x) = 3x² + 12x + 5.",
    [("3x² + 12x + 5 = 3(x² + 4x) + 5", gl("3*x**2+12*x+5", "3*(x**2+4*x)+5")), ("Die Hälfte von 4 ist 2: 3((x + 2)² − 4) + 5", gl("3*(x**2+4*x)+5", "3*((x+2)**2-4)+5")),
     ("Klammer auflösen: 3(x + 2)² − 12 + 5 = 3(x + 2)² − 7", gl("3*((x+2)**2-4)+5", "3*(x+2)**2-7")), ("Das Minimum ist −7 bei x = 2.", False)],
    "Die Klammer heißt (x + 2)². Bei welchem x ist sie 0?",
    "Aus (x + 2)² = 0 folgt x = −2. Das Minimum −7 liegt bei x = −2. Probe: T(−2) = 12 − 24 + 5 = −7."), regel="id.funktionen.gleichung_form")
neu(T, "mit_faktor", "zwei_wege", Z(
    "Bestimme das Minimum von T(x) = 2x² − 12x + 22 auf zwei Wegen. Weg A: Faktor ausklammern und quadratisch ergänzen. Weg B: T(2), T(3) und T(4) ausrechnen. Weil T(2) und T(4) gleich sind, liegt die Symmetrieachse der Parabel in der Mitte bei x = 3. Die Parabel öffnet sich nach oben, weil vor x² die positive Zahl 2 steht. Also ist der kleinste dieser drei Werte das Minimum. Wie groß ist das Minimum?",
    4, "22 - 2 * 3 ** 2", "2 * 3 ** 2 - 12 * 3 + 22", "Beide Wege müssen dasselbe Minimum ergeben.",
    "Weg A: 2(x − 3)² + 4, Minimum 4. Weg B: T(2) = 6, T(3) = 4, T(4) = 6. Wegen T(2) = T(4) liegt die Symmetrieachse bei x = 3. Die Parabel öffnet sich nach oben (Faktor 2 vor x² ist positiv), also ist 4 der kleinste Funktionswert, der Minimalwert von T für alle x. Der tiefste Punkt der Parabel ist (3|4).",
    [(6, None, "den Wert am Rand der Tabelle T(2) als Minimum genommen", "2 * 2 ** 2 - 12 * 2 + 22"), (22, None, "den Wert bei x = 0 genommen", "2 * 0 ** 2 - 12 * 0 + 22"), (3, None, "die Stelle des Minimums statt seines Werts genommen", "6 // 2")]), regel="id.funktionen.gleichung_form")

# ───────── optimierung ─────────
neu(T, "optimierung", "lueckenweg", L(
    "Ein Rechteck hat den Umfang 20 m. Eine Seite ist x lang. Die andere Seite ist ① − x. Die Fläche A(x) = x · (① − x) ist am größten bei x = ②. Dann ist die Fläche ③ m².",
    KOMM(3), [10, 5, 25], ["20 // 2", "{1} // 2", "{2} * ({1} - {2})"], ["10", "5", "25"], "Die beiden Seiten zusammen sind der halbe Umfang. Die Fläche ist am größten, wenn beide Seiten gleich lang sind.",
    "Halber Umfang 10. Andere Seite 10 − x. A(x) = −x² + 10x = −(x − 5)² + 25. Maximum bei x = 5, Fläche 25 m².",
    {0: [(20, None, "den Umfang statt des halben Umfangs genommen", "20")], 2: [(50, None, "5 · 10 gerechnet statt 5 · 5", "{2} * {1}")]}), regel="id.funktionen.gleichung_form")
neu(T, "optimierung", "bruecke", W(
    "Ein Bauer hat 24 m Zaun. Er umzäunt ein Rechteck an einer Hauswand, sodass nur drei Seiten Zaun brauchen. Die Wand ist länger als der Zaun. Die beiden Seiten senkrecht zur Wand sind je x lang. Welcher Term gibt die Fläche des Rechtecks an?",
    "x(24 − 2x)", [("x(24 − x)", "nur eine Seite x vom Zaun abgezogen"), ("x(24 − 4x)", "vier Seiten x abgezogen, als gäbe es keine Wand"), ("2x + (24 − 2x)", "die Seiten addiert statt Länge mal Breite")],
    "Die Seite parallel zur Wand ist der Rest des Zauns nach Abzug der beiden Seiten x.",
    "Die Seite an der Wand ist 24 − 2x lang. Fläche: A = x · (24 − 2x) = −2x² + 24x.",
    lambda: all(wert_an("x*(24-2*x)", k) == 24 * k - 2 * k * k for k in (1, 3, 5)) and not gl("x*(24-2*x)", "x*(24-x)") and not gl("x*(24-2*x)", "x*(24-4*x)") and not gl("x*(24-2*x)", "2*x+(24-2*x)")), regel="id.funktionen.gleichung_form")
neu(T, "optimierung", "anwenden", Z(
    "Eine Schülerfirma verkauft Kerzen. Bei dem Preis von p Euro je Kerze werden 80 − 10p Kerzen in der Woche verkauft (p liegt zwischen 0 und 8). Die Wocheneinnahmen sind p · (80 − 10p). Bei welchem Preis in Euro sind die Einnahmen am größten?",
    4, "80 / (2 * 10)", 4, "Multipliziere aus: −10p² + 80p. Klammere −10 aus und ergänze quadratisch.",
    "p(80 − 10p) = −10p² + 80p = −10(p − 4)² + 160. Das Maximum liegt bei p = 4. Dann sind die Einnahmen 160 €.",
    [(8, None, "den größten möglichen Preis genommen", "80 // 10"), (160, None, "die größten Einnahmen statt des Preises angegeben", "4 * (80 - 10 * 4)"), (40, None, "80 : 2 gerechnet", "80 / 2")], "€"), g="transfer", regel="id.funktionen.gleichung_form")
assert gl("p*(80-10*p)".replace("p", "x"), "-10*(x-4)**2+160")
