T = "terme.bruchterme"
# ───────── definitionsmenge ─────────
_tb = {-1: -3, 0: -6, 2: 6, 3: 3}
neu(T, "definitionsmenge", "bruecke", W(
    "Die Tabelle zeigt einige Werte eines Bruchterms T(x). An der Stelle x = 1 ist T nicht definiert. Welcher Term passt zu allen Einträgen der Tabelle?",
    "6/(x − 1)",
    [("6/(x + 1)", "dieser Term ist an der Stelle x = −1 nicht definiert, nicht an der Stelle x = 1; das Vorzeichen der Nullstelle des Nenners ist vertauscht"), ("6/x", "dieser Term ist an der Stelle x = 0 nicht definiert; für x = 2 ergibt er 3 statt 6")],
    "An welcher Stelle wird der Nenner 0? Setze auch x = 2 ein und vergleiche mit der Tabelle.",
    "Für 6/(x − 1) ist der Nenner bei x = 1 gleich 0, dort ist der Term nicht definiert. Die Werte: x = −1 ergibt 6/(−2) = −3, x = 0 ergibt −6, x = 2 ergibt 6, x = 3 ergibt 3. Das passt zur Tabelle.",
    lambda: undef("6/(x-1)", 1) and all(wert_an("6/(x-1)", k) == v for k, v in _tb.items()) and not undef("6/(x+1)", 1) and not undef("6/x", 1) and undef("6/(x+1)", -1) and undef("6/x", 0)
    and wert_an("6/x", 2) == 3,
    grafik=TAB(["x", "−1", "0", "1", "2", "3"], ["T(x)", "−3", "−6", "nicht definiert", "6", "3"])), g="darstellung", regel="id.algebra.erlaubte_zahlen")
neu(T, "definitionsmenge", "fehler_detektiv", FD(
    "Kim bestimmt die Definitionsmenge des Terms (x + 1)/(x² − 9) über ℚ.",
    [("Der Nenner darf nicht 0 sein: x² − 9 ≠ 0.", True, True),
     ("Aus x² = 9 folgt x = 3, also ist nur x = 3 verboten.", [k for k in range(-5, 6) if k * k == 9] == [3], True),
     ("Die Definitionsmenge ist D = ℚ \\ {3}.", False, True)],
    "Welche Zahlen ergeben beim Quadrieren 9? Probiere auch negative Zahlen.",
    "Aus x² = 9 folgen zwei Zahlen: x = 3 und x = −3, denn auch (−3)² = 9. Beide machen den Nenner 0. Richtig: D = ℚ \\ {−3; 3}. Zeile 3 übernimmt nur die unvollständige Zeile 2."), regel="id.algebra.erlaubte_zahlen")
# ───────── termwert ─────────
neu(T, "termwert", "anwenden", Z(
    "Eine Klasse mietet einen Bus. Der Bus kostet 360 € Grundpreis, dazu kommen 6 € Verpflegung je Person. Bei k Personen zahlt jede Person (360 + 6k)/k Euro (k ≥ 1). Wie viel Euro zahlt jede Person bei k = 40?",
    15, "(360 + 6 * 40) / 40", "360 / 40 + 6", "Setze k = 40 im Zähler und im Nenner ein. Rechne den Zähler zuerst aus.",
    "Zähler: 360 + 6 · 40 = 360 + 240 = 600. Nenner: 40. Dann 600 : 40 = 15. Jede Person zahlt 15 €. Probe: 9 € für den Bus plus 6 € Verpflegung.",
    [(366, "fb.kuerzen.aus_summe", "das k in der Summe im Zähler gekürzt: aus (360 + 6k)/k wird 360 + 6", "360 + 6"), (9, None, "nur den Grundpreis durch die Personenzahl geteilt, die 6 € je Person vergessen", "360 / 40"), (240, None, "nur den Verpflegungsanteil im Zähler gerechnet und nicht geteilt", "6 * 40")], "€"), g="einkleidung", regel="id.algebra.erlaubte_zahlen")
neu(T, "termwert", "umkehren", Z(
    "Der Term T(x) = (x + k)/(x − 2) ist für x ≠ 2 definiert. Für welche Zahl k hat er an der Stelle x = 5 den Wert 3?",
    4, "3 * (5 - 2) - 5", "9 - 5", "Rechne zuerst den Nenner an der Stelle x = 5 aus.",
    "Der Nenner ist 5 − 2 = 3. Der Zähler muss 3 · 3 = 9 sein. Also 5 + k = 9 und k = 4. Probe: (5 + 4)/(5 − 2) = 9 : 3 = 3.",
    [(-2, None, "den Nenner vergessen: 5 + k = 3", "3 - 5"), (9, None, "nur 3 · 3 gerechnet und die 5 im Zähler nicht abgezogen", "3 * 3"), (16, None, "den Nenner mit x + 2 statt x − 2 berechnet", "3 * (5 + 2) - 5")]), g="rueckwaerts", regel="id.algebra.erlaubte_zahlen")
# ───────── kuerzen ─────────
neu(T, "kuerzen", "zwei_wege", Z(
    "Berechne den Wert von (x² − 25)/(x² + 5x) für x = 10 auf zwei Wegen (der Term ist für x ≠ 0 und x ≠ −5 definiert). Weg A: Zähler und Nenner in Faktoren zerlegen, kürzen und dann x = 10 einsetzen. Weg B: x = 10 sofort in Zähler und Nenner einsetzen und den Zahlenbruch ausrechnen. Welchen Wert hat der Term?",
    0.5, "(10 ** 2 - 25) / (10 ** 2 + 5 * 10)", "(10 - 5) / 10", "Beide Wege müssen denselben Wert liefern. Der Zähler ist (x − 5)(x + 5), der Nenner ist x(x + 5).",
    "Weg A: Der Zähler ist (x − 5)(x + 5), der Nenner ist x(x + 5). Nach dem Kürzen mit x + 5 bleibt (x − 5)/x. Für x = 10 ist das 5/10 = 0,5. Weg B: Zähler 100 − 25 = 75, Nenner 100 + 50 = 150, und 75 : 150 = 0,5.",
    [(-0.5, "fb.kuerzen.aus_summe", "aus den Summen gekürzt: nur −25 im Zähler und 5x im Nenner übrig gelassen", "-25 / (5 * 10)"), (0.75, None, "im Nenner den Summanden 5x vergessen", "(10 ** 2 - 25) / 10 ** 2"), (2, None, "Zähler und Nenner des gekürzten Terms vertauscht", "10 / (10 - 5)")]), g="mehrschritt", regel="rr.kuerzen")
neu(T, "kuerzen", "anwenden", Z(
    "Ein rechteckiges Grundstück hat den Flächeninhalt (x² − 16) m² und die Länge (x + 4) m (x > 4). Die Breite ist der Quotient aus Fläche und Länge. Wie breit ist das Grundstück in Metern für x = 60?",
    56, "(60 ** 2 - 16) / (60 + 4)", "60 - 4", "Die Breite ist ein Quotient. Vereinfache ihn zuerst, bevor du x einsetzt.",
    "x² − 16 = (x − 4)(x + 4). Breite = (x − 4)(x + 4)/(x + 4) = x − 4. Für x = 60 ist das 56 m. Probe: Fläche 3600 − 16 = 3584 m², Länge 64 m, 3584 : 64 = 56.",
    [(3584, None, "die Fläche selbst als Breite angegeben, nicht durch die Länge geteilt", "60 ** 2 - 16"), (64, None, "die Länge als Breite angegeben", "60 + 4"), (49, None, "x² − 16 falsch als (x − 4)(x − 4) zerlegt: (x − 4)²/(x + 4)", "(60 - 4) ** 2 / (60 + 4)")], "m"), g="transfer", regel="rr.kuerzen")
assert gl("(x**2-16)/(x+4)", "x-4")
# ───────── erweitern ─────────
neu(T, "erweitern", "umkehren", Z(
    "Der Bruchterm 4/(x − 2) wurde so erweitert, dass der neue Nenner x² − 4 ist (x ≠ 2 und x ≠ −2). Welchen Wert hat der neue Zähler für x = 5?",
    28, "4 * (5 + 2)", "28", "Womit musst du x − 2 malnehmen, um x² − 4 zu erhalten? Mit demselben Term wird auch der Zähler malgenommen.",
    "x² − 4 = (x − 2)(x + 2). Es wurde mit x + 2 erweitert. Der neue Zähler ist 4(x + 2). Für x = 5: 4 · 7 = 28. Probe: 4/3 = 28/21.",
    [(7, None, "nur den Erweiterungsfaktor x + 2 berechnet, den Zähler 4 nicht mitgenommen", "5 + 2"), (4, None, "den Zähler nicht mit erweitert", "4"), (22, None, "nur x mit 4 multipliziert, die 2 anschließend addiert", "4 * 5 + 2")]), g="umkehr", regel="rr.kuerzen")
assert gl("4/(x-2)", "4*(x+2)/(x**2-4)")
neu(T, "erweitern", "fehler_detektiv", FD(
    "Kim erweitert 2/(x − 1) so, dass der Nenner x² − 1 wird.",
    [("Es ist x² − 1 = (x − 1)(x + 1), erlaubt sind x ≠ 1 und x ≠ −1. Also wird mit x + 1 erweitert.", gl("x**2-1", "(x-1)*(x+1)"), True),
     ("Der Zähler wird 2 · (x + 1) = 2x + 1.", gl("2*(x+1)", "2*x+1"), True),
     ("Ergebnis: (2x + 1)/(x² − 1) mit x ≠ 1 und x ≠ −1.", gl("(2*x+1)/(x**2-1)", "(2*x+1)/(x**2-1)"), True)],
    "Rechne 2 · (x + 1) einzeln aus. Wird jeder Summand malgenommen?",
    "2 · (x + 1) = 2x + 2, nicht 2x + 1. Beim Erweitern müssen Zähler und Nenner mit demselben ganzen Term malgenommen werden. Richtig: (2x + 2)/(x² − 1). Zeile 3 übernimmt nur den Fehler der Zeile 2."), regel="rr.kuerzen")
# ───────── addieren ─────────
_ta = [(1, F(3, 2)), (2, F(5, 6)), (3, F(7, 12)), (4, F(9, 20))]
neu(T, "addieren", "bruecke", W(
    "Die Tabelle zeigt einige Werte von T(x) = 1/x + 1/(x + 1) (x ≠ 0 und x ≠ −1). Welcher Bruchterm ist zu T(x) gleichwertig, und mit welcher Gegenprobe und Begründung ist das richtig belegt?",
    "(2x + 1)/(x² + x). Gegenprobe: x = 2 ergibt 5/6, das steht in der Tabelle. Begründung: Mit dem Hauptnenner x² + x wird aus 1/x der Bruch (x + 1)/(x² + x) und aus 1/(x + 1) der Bruch x/(x² + x), die Zähler addieren sich zu 2x + 1.",
    [("(2x + 1)/(x² + x). Gegenprobe: x = 2 ergibt 5/6, das steht in der Tabelle. Begründung: Zähler und Nenner werden getrennt addiert, also (1 + 1)/(x + x + 1).", "der Term stimmt, aber die Begründung ist falsch: Zähler und Nenner dürfen nicht getrennt addiert werden; man braucht den Hauptnenner"),
     ("2/(x² + x). Gegenprobe: x = 1 ergibt 1, das stimmt mit der Tabelle überein. Begründung: Mit dem Hauptnenner x² + x werden nur die Nenner malgenommen, die Zähler 1 + 1 ergeben 2.", "nur die Zähler addiert, die Erweiterung der Zähler vergessen; die Gegenprobe zeigt es: für x = 1 ergibt der Term 1, die Tabelle zeigt 3/2")],
    "Setze x = 1 in jeden Term ein und vergleiche mit der Tabelle. Wie kommt man auf den Hauptnenner?",
    "Hauptnenner x(x + 1) = x² + x: 1/x = (x + 1)/(x² + x) und 1/(x + 1) = x/(x² + x). Summe: (2x + 1)/(x² + x). Für x = 1: 3/2, für x = 2: 5/6, für x = 3: 7/12, für x = 4: 9/20. Die Tabelle widerlegt zum Beispiel 2/(x² + x): für x = 1 ergibt es 1 statt 3/2. Der Hauptnenner begründet den richtigen Term für alle x, die Tabelle prüft nur vier Werte.",
    lambda: all(wert_an("(2*x+1)/(x**2+x)", k) == v for k, v in _ta) and gl("1/x+1/(x+1)", "(2*x+1)/(x**2+x)") and not gl("1/x+1/(x+1)", "2/(2*x+1)") and not gl("1/x+1/(x+1)", "2/(x**2+x)") and wert_an("2/(x**2+x)", 1) == 1,
    grafik=TAB(["x", "1", "2", "3", "4"], ["T(x)", "3/2", "5/6", "7/12", "9/20"])), g="darstellung", regel="rr.bruchrechnen")
neu(T, "addieren", "umkehren", Z(
    "Für welche Zahl a gilt 1/x + a/(x + 2) = (3x + 2)/(x² + 2x) für alle Zahlen x mit x ≠ 0 und x ≠ −2?",
    2, "3 - 1", 2, "Bringe die linke Seite auf den Nenner x² + 2x. Vergleiche dann die Zähler: die Zahl vor x und die Zahl ohne x.",
    "Hauptnenner x(x + 2) = x² + 2x. 1/x = (x + 2)/(x² + 2x) und a/(x + 2) = ax/(x² + 2x). Zähler: (x + 2) + ax = (1 + a)x + 2. Das soll 3x + 2 sein, also 1 + a = 3 und a = 2.",
    [(3, None, "die Zahl vor x im Ergebnis direkt als a genommen", "3"), (1, None, "3 − 2 gerechnet: den Zahlenteil 2 vom Ergebnis abgezogen", "3 - 2"), (5, None, "3 + 2 gerechnet", "3 + 2")]), g="rueckwaerts", regel="rr.bruchrechnen")
assert gl("1/x+2/(x+2)", "(3*x+2)/(x**2+2*x)")
# ───────── multiplizieren ─────────
neu(T, "multiplizieren", "zwei_wege", Z(
    "Berechne (x² − 4)/(x + 3) · (x + 3)/(x − 2) für x = 5 auf zwei Wegen (x ≠ −3 und x ≠ 2). Weg A: erst die Brüche multiplizieren, kürzen und vereinfachen, dann x = 5 einsetzen. Weg B: x = 5 sofort in beide Brüche einsetzen und die zwei Zahlenbrüche multiplizieren. Welchen Wert hat das Produkt?",
    7, "(5 ** 2 - 4) / (5 + 3) * ((5 + 3) / (5 - 2))", "5 + 2", "Beide Wege müssen denselben Wert ergeben. Zerlege x² − 4 in zwei Faktoren.",
    "Weg A: (x − 2)(x + 2)/(x + 3) · (x + 3)/(x − 2) = x + 2. Für x = 5 ist das 7. Weg B: 21/8 · 8/3 = 168/24 = 7.",
    [(168, None, "nur die Zähler der beiden Brüche malgenommen", "(5 ** 2 - 4) * (5 + 3)"), (3, None, "x² − 4 falsch als (x − 2)(x − 2) zerlegt, dann bleibt beim Kürzen x − 2", "5 - 2"), (2.625, None, "nur den ersten Bruch ausgerechnet", "(5 ** 2 - 4) / (5 + 3)")]), g="mehrschritt", regel="rr.bruchrechnen")
assert gl("(x**2-4)/(x+3)*(x+3)/(x-2)", "x+2")
neu(T, "multiplizieren", "umkehren", Z(
    "Das Produkt 4x/(x − 2) · (x − 2)/(a · x²) soll für alle Zahlen x mit x ≠ 0 und x ≠ 2 gleich 2/x sein (a ≠ 0). Welche Zahl a ist das?",
    2, "4 / 2", 2, "Kürze gemeinsame, von null verschiedene Faktoren. Vergleiche dann den Rest mit 2/x.",
    "Im Produkt kürzt sich x − 2 weg, und ein x kürzt sich auch. Es bleibt der Bruch 4/(a · x). Das soll 2/x sein, also 4/a = 2 und a = 2. Probe: 4x/(2x²) = 2/x.",
    [(8, None, "4 · 2 gerechnet statt 4 : 2", "4 * 2"), (0.5, None, "2 : 4 gerechnet statt 4 : 2", "2 / 4"), (6, None, "4 + 2 gerechnet", "4 + 2")]), g="rueckwaerts", regel="rr.bruchrechnen")
assert gl("4*x/(x-2)*(x-2)/(2*x**2)", "2/x")
# ───────── fehler_finden ─────────
_f = lambda k: wert_an("(x+6)/(x+2)", k)
neu(T, "fehler_finden", "bruecke", W(
    "Kim behauptet: Es gilt (x + 6)/(x + 2) = 3 für alle Zahlen x ≠ −2. Die Tabelle zeigt beide Seiten für einige Zahlen x. Was folgt aus der Tabelle?",
    "Die Behauptung ist falsch: Zum Beispiel für x = 2 ist der linke Wert 2 und nicht 3.",
    [("Die Behauptung ist richtig, denn für x = 0 stimmen beide Seiten überein.", "von einem einzigen passenden Beispiel auf alle Zahlen geschlossen"), ("Die Behauptung ist falsch, denn für x = 0 sind beide Seiten verschieden.", "die Spalte x = 0 falsch gelesen: dort sind beide Seiten gleich 3")],
    "Eine Behauptung „für alle x“ ist schon falsch, wenn sie für eine einzige Zahl nicht stimmt. Suche eine solche Zahl in der Tabelle.",
    "Für x = 0 ist (0 + 6)/(0 + 2) = 3, die Seiten sind gleich. Für x = 2 ist 8/4 = 2, nicht 3. Ein einziges Gegenbeispiel genügt, um „für alle x“ zu widerlegen. Gekürzt werden darf nicht aus einer Summe.",
    lambda: _f(0) == 3 and _f(2) == 2 and _f(1) == F(7, 3) and _f(4) == F(5, 3),
    grafik=TAB(["x", "0", "1", "2", "4"], ["(x + 6)/(x + 2)", "3", "7/3", "2", "5/3"], ["rechte Seite 3", "3", "3", "3", "3"])), g="darstellung", regel="rr.kuerzen")
neu(T, "fehler_finden", "umkehren", Z(
    "Kim kürzt falsch und behauptet (x² + 9)/(x + 3) = x + 3. Die Behauptung ist für fast alle Zahlen falsch, aber für genau eine Zahl x ≠ −3 stimmt sie zufällig. Für welche Zahl?",
    0, "(9 - 9) / 6", 0, "Für welche Zahlen x sind beide Seiten gleich?",
    "(x² + 9)/(x + 3) = x + 3 bedeutet x² + 9 = (x + 3)² = x² + 6x + 9. Dann 6x = 0, also x = 0. Probe: 9/3 = 3 und 0 + 3 = 3. Für alle anderen Zahlen x ≠ −3 ist die Behauptung falsch, zum Beispiel für x = 1: 10/4 ist nicht 4.",
    [(1.5, None, "die 9 nicht abgezogen: 6x = 9", "9 / 6"), (-1.5, None, "das Vorzeichen vertauscht: 6x = −9", "-9 / 6"), (-3, "fb.erlaubte_zahlen.nullstelle_des_nenners_als_loesung", "die Nullstelle des Nenners als Lösung angegeben", "-3")]), g="rueckwaerts", regel="rr.kuerzen")
assert gl("(x**2+9)/(x+3)", "x+3") is False
