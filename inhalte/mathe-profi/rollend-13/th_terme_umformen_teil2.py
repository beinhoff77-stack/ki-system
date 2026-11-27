T = "terme.umformen_teil2"
# ───────── summe_mal_summe ─────────
neu(T, "summe_mal_summe", "anwenden", Z(
    "Ein quadratischer Spielplatz hat die Seitenlänge x m. Er wird in der einen Richtung um 3 m und in der anderen Richtung um 2 m erweitert, sodass ein Rechteck entsteht. Um wie viele Quadratmeter wächst die Fläche, wenn x = 20 ist?",
    106, "(20 + 3) * (20 + 2) - 20 * 20", "5 * 20 + 6", "Die neue Fläche ist Länge mal Breite des Rechtecks. Ziehe die alte Fläche ab. Jeder Summand der ersten Klammer wird mit jedem der zweiten malgenommen.",
    "Neue Fläche: (x + 3)(x + 2) = x² + 2x + 3x + 6 = x² + 5x + 6. Zuwachs: x² + 5x + 6 − x² = 5x + 6. Für x = 20: 100 + 6 = 106 m². Probe: 23 · 22 = 506, 506 − 400 = 106.",
    [(6, None, "nur x² und das Produkt der Zahlen beachtet: (x + 3)(x + 2) als x² + 6 gerechnet", "(20 * 20 + 3 * 2) - 20 * 20"), (100, None, "das Produkt der beiden Zahlen nicht mitgezählt: nur 5x", "(3 + 2) * 20"), (5, None, "addiert statt ausmultipliziert: x² + 3 + 2", "3 + 2")], "m²"), g="einkleidung", regel="rr.ausmultiplizieren")
assert gl("(x+3)*(x+2)-x*x", "5*x+6")
neu(T, "summe_mal_summe", "umkehren", Z(
    "Für zwei ganze Zahlen a und b mit 0 < a < b gilt (x + a)(x + b) = x² + 7x + 12 für alle Zahlen x. Wie groß ist a?",
    3, "7 - 4", 3, "Beim Ausmultiplizieren entsteht x² + (a + b)x + a · b. Welche zwei Zahlen haben die Summe 7 und das Produkt 12?",
    "(x + a)(x + b) = x² + (a + b)x + ab. Also gilt a + b = 7 und ab = 12. Mit 0 < a < b passt nur a = 3 und b = 4. Probe: (x + 3)(x + 4) = x² + 7x + 12.",
    [(4, None, "die größere der beiden Zahlen angegeben", "7 - 3"), (2, None, "nur das Produkt geprüft: 2 und 6 haben das Produkt 12, aber die Summe 8", "12 // 6"), (1, None, "nur das Produkt geprüft: 1 und 12 haben das Produkt 12, aber die Summe 13", "12 // 12")]), g="rueckwaerts", regel="rr.ausmultiplizieren")
assert gl("(x+3)*(x+4)", "x**2+7*x+12") and [(a, b) for a in range(1, 13) for b in range(a + 1, 13) if a + b == 7 and a * b == 12] == [(3, 4)]
# ───────── ausklammern ─────────
_flaeche = lambda x: 5 * x + 5 * 4
neu(T, "ausklammern", "bruecke", W(
    "Das Rechteck in der Zeichnung ist in zwei Teile geteilt. Die Höhe ist 5 cm. Die Breite des linken Teils ist x cm, die des rechten Teils 4 cm. Welcher Term gibt den Flächeninhalt des ganzen Rechtecks in cm² als Produkt an (Breite mal Höhe)?",
    "5(x + 4)",
    [("4(x + 5)", "Breite und Höhe vertauscht: dieser Term ist 4x + 20, also 4x + 20 statt 5x + 20"), ("x(5 + 4)", "dieser Term ist 9x; die 5 und die 4 wurden nur zusammengezählt")],
    "Wie breit ist das ganze Rechteck? Setze zur Probe x = 1 ein und rechne die Teilflächen einzeln aus.",
    "Gesamtbreite: x + 4. Höhe: 5. Fläche: 5(x + 4) = 5x + 20, das ist die Summe der Teilflächen 5x und 20. Die anderen Terme ergeben 4x + 20 und 9x.",
    lambda: gl("5*(x+4)", "5*x+20") and not gl("4*(x+5)", "5*x+20") and not gl("x*(5+4)", "5*x+20"),
    grafik={"typ": "figur", "punkte": {"A": [0, 0], "B": [9, 0], "C": [9, 5], "D": [0, 5], "E": [5, 0], "F": [5, 5]}, "flaeche": ["A", "B", "C", "D"],
            "linien": [["A", "E", "x cm"], ["E", "B", "4 cm"], ["B", "C", "5 cm"], ["E", "F", "", "gestrichelt"]]}), g="darstellung", regel="rr.ausmultiplizieren")
neu(T, "ausklammern", "fehler_detektiv", FD(
    "Kim klammert in 8a²b + 12ab² den größten gemeinsamen Faktor aus.",
    [("Der größte gemeinsame Teiler von 8 und 12 ist 4. Beide Glieder enthalten a und b. Ausgeklammert wird 4ab.", math.gcd(8, 12) == 4, True),
     ("Teilen durch 4ab: 8a²b : 4ab = 2 und 12ab² : 4ab = 3.", gl("8*a**2*b/(4*a*b)", "2") and gl("12*a*b**2/(4*a*b)", "3"), True),
     ("Also gilt 8a²b + 12ab² = 4ab(2 + 3) = 20ab.", gl("4*a*b*(2+3)", "20*a*b"), True)],
    "Teile 8a²b durch 4ab. Welche Buchstaben bleiben übrig?",
    "8a²b : 4ab = 2a und 12ab² : 4ab = 3b. Richtig: 8a²b + 12ab² = 4ab(2a + 3b). In Zeile 2 sind die Buchstaben verloren gegangen, Zeile 3 rechnet damit nur weiter."), regel="rr.ausmultiplizieren")
# ───────── binomisch ─────────
neu(T, "binomisch", "zwei_wege", Z(
    "Berechne 47² auf zwei Wegen. Weg A: 47 · (40 + 7) mit dem Verteilungsgesetz. Weg B: (50 − 3)² mit der zweiten binomischen Formel. Welchen Wert hat 47²?",
    2209, "47 ** 2", "(50 - 3) ** 2", "Beide Wege müssen dasselbe Ergebnis haben. Die zweite binomische Formel hat in der Mitte einen eigenen Summanden.",
    "Weg A: 47 · 40 + 47 · 7 = 1 880 + 329 = 2 209. Weg B: (50 − 3)² = 50² − 2 · 50 · 3 + 3² = 2 500 − 300 + 9 = 2 209. Beide Wege führen auf 2 209.",
    [(2491, "fb.ausmultiplizieren.hoch_verteilt", "nur die Quadrate 50² und 3² voneinander abgezogen, das doppelte Produkt in der Mitte vergessen", "50 ** 2 - 3 ** 2"), (2509, None, "die Quadrate 50² und 3² addiert, die Mitte vergessen", "50 ** 2 + 3 ** 2"), (2200, None, "das Quadrat 3² am Ende vergessen", "50 ** 2 - 2 * 50 * 3")]), g="mehrschritt", regel="rr.ausmultiplizieren")
neu(T, "binomisch", "fehler_detektiv", FD(
    "Kim multipliziert (3x − 5)² mit der zweiten binomischen Formel aus.",
    [("Setze a = 3x und b = 5. Dann ist a² = 3x².", gl("(3*x)**2", "3*x**2"), True),
     ("Das doppelte Produkt ist 2ab = 2 · 3x · 5 = 30x, und es ist b² = 25.", gl("2*3*x*5", "30*x"), True),
     ("Also gilt (3x − 5)² = 3x² − 30x + 25.", gl("3*x**2-30*x+25", "3*x**2-30*x+25"), True)],
    "Setze x = 1 ein: Was ergibt (3 · 1)²?",
    "Das Quadrat von 3x ist (3x)² = 9x², denn auch die 3 wird quadriert. Richtig: (3x − 5)² = 9x² − 30x + 25. Zeile 2 ist richtig, Zeile 3 übernimmt nur den Fehler der Zeile 1."), regel="rr.ausmultiplizieren")
# ───────── gleichungen_binomisch ─────────
_x = 5
neu(T, "gleichungen_binomisch", "bruecke", W(
    "Ein Quadrat hat die Seitenlänge x cm. Verlängert man jede Seite um 4 cm, so wird die Fläche um 56 cm² größer. Welche Gleichung beschreibt diese Aussage?",
    "(x + 4)² = x² + 56",
    [("x² + 4² = x² + 56", "die Fläche des größeren Quadrats als x² + 4² gerechnet; diese Gleichung hat keine Lösung, weil 16 = 56 nicht stimmt"), ("(x + 4)² = 56", "die neue Fläche mit dem Zuwachs gleichgesetzt; für x = 5 ergibt die linke Seite 81, nicht 56")],
    "Wie groß ist die neue Fläche? Wie groß ist sie, wenn sie um 56 cm² wächst?",
    "Neue Seitenlänge x + 4, neue Fläche (x + 4)². Sie ist um 56 größer als die alte Fläche x². Also (x + 4)² = x² + 56. Ausmultipliziert: 8x + 16 = 56, also x = 5. Probe: 81 = 25 + 56.",
    lambda: ist_loesung("(x+4)**2", "x**2+56", 5) and not any(ist_loesung(l, r, k) for l, r in [("x**2+4**2", "x**2+56"), ("(x+4)**2", "56")] for k in range(-20, 21)),
    ), g="darstellung", regel="id.algebra.gleichung_loesen")
neu(T, "gleichungen_binomisch", "zwei_wege", Z(
    "Löse (2x + 5)² − (2x − 3)² = 80 auf zwei Wegen. Weg A: beide Klammern ausmultiplizieren. Weg B: die Differenz zweier Quadrate als Produkt (a + b)(a − b) schreiben, mit a = 2x + 5 und b = 2x − 3. Welche Zahl ist die Lösung x?",
    2, "(80 - 16) / 32", "(80 / 8 - 2) / 4", "Bei beiden Wegen verschwindet x² und es bleibt eine Gleichung mit x. Setze zur Probe in die Ausgangsgleichung ein.",
    "Weg A: 4x² + 20x + 25 − 4x² + 12x − 9 = 32x + 16 = 80, also x = 2. Weg B: a + b = 4x + 2 und a − b = 8. Dann 8(4x + 2) = 80, also 4x + 2 = 10 und x = 2. Probe: 9² − 1² = 81 − 1 = 80.",
    [(23 / 4, None, "das Minus vor der zweiten Klammer nur bei x² beachtet: 8x + 34 = 80", "(80 - 34) / 8"), (2.5, None, "die Zahl 16 vergessen: 32x = 80", "80 / 32"), (3, None, "16 addiert statt subtrahiert: 32x = 96", "(80 + 16) / 32")]), g="verknuepfen", regel="id.algebra.gleichung_loesen")
assert ist_loesung("(2*x+5)**2-(2*x-3)**2", "80", 2)
