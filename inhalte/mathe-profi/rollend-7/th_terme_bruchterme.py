T = "terme.bruchterme"
# ───────── definitionsmenge ─────────
neu(T, "definitionsmenge", "lueckenweg", L(
    "Bestimme die Definitionsmenge von 9/(2x − 6). Der Term ist nicht definiert, wenn der Nenner 0 ist: 2x − 6 = 0. Dann ist 2x = ① und damit x = ②. Die Definitionsmenge ist ℚ \\ {②}.",
    KOMM(2), [6, 3], ["6", "6 // 2"], ["0 + 6", "3"], "Löse die Gleichung 2x − 6 = 0 wie eine Waage.",
    "2x − 6 = 0 ergibt 2x = 6 und x = 3. Für x = 3 wäre der Nenner 0. D = ℚ \\ {3}.",
    {1: [(6, None, "durch 2 nicht geteilt")]}), regel="id.algebra.erlaubte_zahlen")
neu(T, "definitionsmenge", "umkehren", W(
    "Welcher dieser Terme hat die Definitionsmenge ℚ \\ {−3}?",
    "5/(x + 3)", [("5/(x − 3)", "das Vorzeichen der Nullstelle vertauscht", "fb.erlaubte_zahlen.nullstelle_des_nenners_als_loesung"), ("(x + 3)/5", "den Zähler mit dem Nenner verwechselt"), ("5/(3x)", "die 3 als verbotene Zahl gelesen")],
    "Für welche Zahl wird der Nenner 0? Das ist die ausgeschlossene Zahl.",
    "Bei 5/(x + 3) ist der Nenner 0, wenn x = −3 ist. Nur dort ist der Term nicht definiert.",
    lambda: undef("5/(x+3)", -3) and not undef("5/(x-3)", -3) and not undef("(x+3)/5", -3) and not undef("5/(3*x)", -3)), g="umkehr", regel="id.algebra.erlaubte_zahlen")
neu(T, "definitionsmenge", "anwenden", L(
    "Eine Klasse mietet einen Bus für 504 €. Zwei Schüler zahlen nichts. Bei n Schülern in der Klasse zahlt jeder der anderen 504/(n − 2) €. Der Term ist nicht definiert für n = ①. Hat die Klasse 30 Schüler, zahlt jeder ② €.",
    KOMM(2), [2, 18], ["2", "504 // (30 - 2)"], ["1 + 1", "18"], "Wann ist der Nenner n − 2 gleich 0? Für 30 Schüler setzt du n = 30 ein.",
    "n − 2 = 0 gilt für n = 2. Für n = 30: 504 : 28 = 18. Jeder zahlt 18 €.",
    {1: [(28, None, "nur den Nenner 30 − 2 ausgerechnet")]}), g="einkleidung", regel="id.algebra.erlaubte_zahlen")

# ───────── termwert ─────────
neu(T, "termwert", "lueckenweg", L(
    "Berechne T(3) für T(x) = (2x + 4)/(x + 2). Zähler: 2 · 3 + 4 = ①. Nenner: 3 + 2 = ②. Der Wert ist ①/② = ③.",
    KOMM(3), [10, 5, 2], ["2 * 3 + 4", "3 + 2", "10 // 5"], ["6 + 4", "5", "2"], "Setze für x überall 3 ein.",
    "Zähler 10, Nenner 5. 10 : 5 = 2. Also T(3) = 2.",
    {0: [(14, "fb.reihenfolge.links_nach_rechts", "Zähler falsch geklammert: 2 · (3 + 4)")]}), regel="rr.bruchrechnen")
neu(T, "termwert", "zwei_wege", Z(
    "Berechne T(5) für T(x) = (x² − 9)/(x − 3) auf zwei Wegen. Weg A: erst x = 5 einsetzen, dann ausrechnen. Weg B: erst kürzen (x² − 9 ist (x − 3)(x + 3)), dann x = 5 einsetzen. Welchen Wert hat T(5)?",
    8, "(5 ** 2 - 9) / (5 - 3)", "5 + 3", "Beide Wege müssen denselben Wert ergeben.",
    "Weg A: (25 − 9) : (5 − 3) = 16 : 2 = 8. Weg B: Nach dem Kürzen bleibt x + 3 = 8.",
    [(16, "fb.reihenfolge.mal_vor_hoch", "den Nenner vergessen"), (0.5, "fb.potenz.basis_mal_hochzahl", "5² als 10 gerechnet: (10 − 9) : (5 − 3)")]), regel="rr.bruchrechnen")
neu(T, "termwert", "bruecke", W(
    "Die Tabelle zeigt einige Werte eines Terms T(x). Welcher Term passt zu allen Werten der Tabelle?",
    "12/(x + 1)", [("12/x", "nur den Anfang des Terms erkannt: für x = 1 ist der Wert 12, nicht 6"), ("6/x", "für x = 1 richtig, für x = 2 aber 3 statt 4"), ("12/(x + 2)", "für x = 1 ist der Wert 4, nicht 6")],
    "Setze die x-Werte aus der Tabelle in die Terme ein und vergleiche.",
    "12/(1 + 1) = 6, 12/(2 + 1) = 4, 12/(3 + 1) = 3, 12/(5 + 1) = 2. Das passt zur Tabelle.",
    lambda: all(wert_an("12/(x+1)", k) == v for k, v in [(1, 6), (2, 4), (3, 3), (5, 2)]) and not all(wert_an("12/x", k) == v for k, v in [(1, 6), (2, 4), (3, 3), (5, 2)])
    and not all(wert_an("6/x", k) == v for k, v in [(1, 6), (2, 4), (3, 3), (5, 2)]) and not all(wert_an("12/(x+2)", k) == v for k, v in [(1, 6), (2, 4), (3, 3), (5, 2)]),
    grafik=TAB(["x", "1", "2", "3", "5"], ["T(x)", "6", "4", "3", "2"])), regel="rr.bruchrechnen")

# ───────── kuerzen ─────────
neu(T, "kuerzen", "lueckenweg", L(
    "Kürze (6x + 12)/(9x + 18). Klammere im Zähler aus: 6x + 12 = ①(x + 2). Klammere im Nenner aus: 9x + 18 = ②(x + 2). Kürze (x + 2). Übrig bleibt ①/②. Kürze diesen Bruch mit ③.",
    KOMM(3), [6, 9, 3], ["6", "9", "3"], ["12 // 2", "18 // 2", "6 // 2"], "Der Faktor vor (x + 2) ist der gemeinsame Faktor in beiden Gliedern.",
    "6x + 12 = 6(x + 2) und 9x + 18 = 9(x + 2). Dann 6/9 = 2/3 (gekürzt mit 3).",
    {0: [(12, "fb.kuerzen.aus_summe", "nur die Zahl ohne x betrachtet")], 2: [(2, None, "nicht den größten gemeinsamen Teiler genommen, 6/9 durch 2 nicht teilbar")]}), regel="rr.kuerzen")
neu(T, "kuerzen", "fehler_detektiv", FD(
    "Kim kürzt den Bruch (x² + 4x)/(x² + 2x).",
    [("Zähler x(x + 4), Nenner x(x + 2).", gl("x**2+4*x", "x*(x+4)") and gl("x**2+2*x", "x*(x+2)")), ("Mit x gekürzt: (x + 4)/(x + 2).", gl("(x**2+4*x)/(x**2+2*x)", "(x+4)/(x+2)")),
     ("Mit x gekürzt: 4/2 = 2.", gl("(x+4)/(x+2)", "2"))],
    "Darf man aus einer Summe kürzen? Probe mit x = 2.",
    "Aus Summen darf man nicht kürzen. (x + 4)/(x + 2) bleibt stehen. Probe mit x = 2: 6/4, nicht 2."), regel="rr.kuerzen")
neu(T, "kuerzen", "umkehren", Z(
    "Der Bruch (x² − 25)/(x + a) lässt sich zu x − 5 kürzen. Welche Zahl ist a?",
    5, 5, 5, "Zerlege x² − 25 in zwei Klammern. Eine davon muss im Nenner stehen.",
    "x² − 25 = (x − 5)(x + 5). Zum Kürzen muss der Nenner x + 5 sein, also a = 5. Probe: (x − 5)(x + 5) : (x + 5) = x − 5.",
    [(-5, "fb.vorzeichen.falsches_zeichen", "das Vorzeichen aus der Klammer übernommen"), (25, None, "die Zahl 25 aus dem Zähler genommen")]), g="rueckwaerts", regel="rr.kuerzen")
assert gl("(x**2-25)/(x+5)", "x-5")

# ───────── erweitern ─────────
neu(T, "erweitern", "lueckenweg", L(
    "Erweitere 3/(2x) so, dass der Nenner 10x² wird. Der Nenner 2x wird mit ①x malgenommen: 2x · ①x = 10x². Der Zähler 3 wird mit demselben Faktor malgenommen: der neue Zähler ist ②x.",
    KOMM(2), [5, 15], ["10 // 2", "3 * 5"], ["5", "15"], "Welche Zahl mal 2 ergibt 10? Und welche Variable fehlt zu x²?",
    "Der Faktor ist 5x, denn 2x · 5x = 10x². Neuer Zähler: 3 · 5x = 15x. Der Bruch ist 15x/(10x²).",
    {0: [(8, "fb.kuerzen.nur_zaehler_oder_nenner", "10 − 2 gerechnet")], 1: [(3, "fb.kuerzen.nur_zaehler_oder_nenner", "den Zähler nicht mit erweitert")]}), regel="rr.kuerzen")
neu(T, "erweitern", "bruecke", W(
    "Die Tabelle zeigt einen Bruch vor und nach dem Erweitern. Womit wurde der Bruch erweitert?",
    "mit 3x", [("mit 3", "nur die Zahlen beachtet; der Nenner wäre dann 6x, nicht 6x²"), ("mit x", "nur die Variable beachtet; der Zähler wäre dann 5x, nicht 15x"), ("mit 3x²", "die Hochzahl des Nenners übernommen")],
    "Teile den neuen Zähler durch den alten. Prüfe dann den Nenner.",
    "15x : 5 = 3x und 6x² : 2x = 3x. Der Bruch wurde mit 3x erweitert.",
    lambda: all(wert_an(f"5*{f}", 2) == wert_an("15*x", 2) for f in ["(3*x)"]) and wert_an("2*x*(3*x)", 2) == wert_an("6*x**2", 2)
    and wert_an("5*3", 2) != wert_an("15*x", 2) and wert_an("5*x", 2) != wert_an("15*x", 2) and wert_an("2*x*(3*x**2)", 2) != wert_an("6*x**2", 2),
    grafik=TAB(["", "Zähler", "Nenner"], ["vorher", "5", "2x"], ["nachher", "15x", "6x²"])), regel="rr.kuerzen")
neu(T, "erweitern", "verfahren_waehlen", W(
    "Die Brüche 2/(x + 1) und 3/(x − 1) sollen gleiche Nenner bekommen. Welcher Weg ist richtig?",
    "Den ersten Bruch mit (x − 1) erweitern, den zweiten mit (x + 1). Beide Nenner sind dann (x + 1)(x − 1).",
    [("Beide Brüche mit (x + 1) erweitern. Dann sind beide Nenner gleich.", "der zweite Nenner wird (x − 1)(x + 1), der erste (x + 1)², also verschieden"), ("Die Nenner addieren: 2x ist der gemeinsame Nenner.", "Nenner dürfen nicht addiert werden"), ("Nur den ersten Bruch mit (x − 1) erweitern.", "dann hat der zweite Bruch noch den Nenner (x − 1)")],
    "Jeder Bruch braucht den Nenner des anderen zusätzlich. Mit was musst du also jeweils erweitern?",
    "Erster Bruch: Zähler 2(x − 1), Nenner (x + 1)(x − 1). Zweiter Bruch: Zähler 3(x + 1), Nenner (x + 1)(x − 1). Jetzt stimmen die Nenner überein.",
    lambda: gl("2/(x+1)", "2*(x-1)/((x+1)*(x-1))") and gl("3/(x-1)", "3*(x+1)/((x+1)*(x-1))") and not gl("(x+1)*(x+1)", "(x-1)*(x+1)")), regel="rr.kuerzen")

# ───────── addieren ─────────
neu(T, "addieren", "lueckenweg", L(
    "Fasse zusammen: 2/x + 3/(2x). Der Hauptnenner ist ①x. Erweitere den ersten Bruch: 2/x = ②/(①x). Dann ist ②/(①x) + 3/(①x) = ③/(①x).",
    KOMM(3), [2, 4, 7], ["2", "2 * 2", "4 + 3"], ["1 + 1", "4", "7"], "Der Nenner 2x enthält schon x. Was fehlt dem Nenner x?",
    "Hauptnenner 2x. 2/x = 4/(2x). 4/(2x) + 3/(2x) = 7/(2x).",
    {1: [(2, "fb.kuerzen.nur_zaehler_oder_nenner", "den Zähler nicht mit erweitert")], 2: [(5, "fb.bruchrechnen.zaehler_und_nenner_addiert", "2 + 3 gerechnet")]}), regel="rr.bruchrechnen")
neu(T, "addieren", "zwei_wege", Z(
    "Berechne T(2) für T(x) = 12/x + 6/(x + 1) auf zwei Wegen. Weg A: erst x = 2 einsetzen, dann beide Brüche addieren. Weg B: erst zu einem Bruch zusammenfassen, dann x = 2 einsetzen. Welchen Wert hat T(2)?",
    8, "12 / 2 + 6 / (2 + 1)", "(18 * 2 + 12) / (2 ** 2 + 2)", "Beide Wege müssen dasselbe ergeben. Weg A ist kürzer.",
    "Weg A: 12/2 + 6/3 = 6 + 2 = 8. Weg B: (18x + 12)/(x² + x) = 48/6 = 8.",
    [(3.6, "fb.bruchrechnen.zaehler_und_nenner_addiert", "Zähler und Nenner einzeln addiert: 18/5"), (6, None, "nur den ersten Bruch berechnet")]), regel="rr.bruchrechnen")
assert gl("12/x+6/(x+1)", "(18*x+12)/(x**2+x)")
neu(T, "addieren", "anwenden", L(
    "Ein Radfahrer fährt 24 km mit v km/h hin und 24 km mit (v + 4) km/h zurück. Die Gesamtzeit ist 24/v + 24/(v + 4) Stunden. Fasse zu einem Bruch mit dem Nenner v² + 4v zusammen. Der Zähler lautet ①v + ②.",
    KOMM(2), [48, 96], ["24 + 24", "24 * 4"], ["2 * 24", "96"], "Erweitere den ersten Bruch mit (v + 4) und den zweiten mit v. Fasse dann die Zähler zusammen.",
    "24(v + 4) + 24v = 24v + 96 + 24v = 48v + 96. Die Gesamtzeit ist (48v + 96)/(v² + 4v).",
    {0: [(24, "fb.tauschen.ungleiches_zusammengefasst", "nur ein v-Glied gezählt")], 1: [(24, None, "nur 24 · 1 statt 24 · 4")]}), g="einkleidung", regel="rr.bruchrechnen")
assert gl("24/x+24/(x+4)", "(48*x+96)/(x**2+4*x)")

# ───────── multiplizieren ─────────
neu(T, "multiplizieren", "lueckenweg", L(
    "Berechne und kürze: (4x/9) · (3/(8x)). Zähler mal Zähler: 4x · 3 = ①x. Nenner mal Nenner: 9 · 8x = ②x. Kürze mit ③x. Es bleibt 1/6.",
    KOMM(3), [12, 72, 12], ["4 * 3", "9 * 8", "12"], ["12", "72", "12"], "Multipliziere oben mit oben und unten mit unten.",
    "12x/(72x). Der gemeinsame Faktor ist 12x. 12x : 12x = 1 und 72x : 12x = 6. Ergebnis: 1/6.",
    {0: [(7, "fb.bruchrechnen.zaehler_und_nenner_addiert", "4 + 3 gerechnet")]}), regel="rr.bruchrechnen")
neu(T, "multiplizieren", "verfahren_waehlen", W(
    "Du sollst (x + 2)/5 · 10/(x + 2) berechnen. Welcher Weg führt zum richtigen Ergebnis?",
    "Gleiche Faktoren kürzen: (x + 2) mit (x + 2) und 10 mit 5. Ergebnis: 2.",
    [("Zähler addieren und Nenner multiplizieren: (x + 12)/(5x + 10).", "die Regel für Addition mit der für Multiplikation vermischt"), ("Mit dem Kehrwert des zweiten Bruchs malnehmen: (x + 2)²/50.", "wie beim Dividieren den Kehrwert benutzt"), ("Nur die Zahlen kürzen: 10/5 = 2. Ergebnis: 2(x + 2)/(x + 2)².", "den Faktor (x + 2) nicht gekürzt, unvollständig")],
    "Beim Malnehmen darf man jeden Faktor aus dem Zähler mit jedem aus dem Nenner kürzen.",
    "(x + 2)/5 · 10/(x + 2): Die Faktoren (x + 2) kürzen sich, 10 : 5 = 2. Ergebnis 2.",
    lambda: gl("(x+2)/5*10/(x+2)", "2") and not gl("(x+2)/5*10/(x+2)", "(x+12)/(5*x+10)") and not gl("(x+2)/5*10/(x+2)", "(x+2)**2/50") and not gl("(x+2)/5*10/(x+2)", "2*(x+2)/(x+2)**2")), regel="rr.bruchrechnen")
neu(T, "multiplizieren", "fehler_detektiv", FD(
    "Kim berechnet (6/x) · (x²/3).",
    [("Ich nehme den Kehrwert des zweiten Bruchs: (6/x) · (3/x²)", gl("6/x*(x**2/3)", "6/x*(3/x**2)")), ("Zähler mal Zähler: 6 · 3 = 18. Nenner mal Nenner: x · x² = x³", gl("6/x*(3/x**2)", "18/x**3")), ("Ergebnis: 18/x³", True)],
    "Wann nimmt man den Kehrwert? Prüfe mit x = 3.",
    "Beim Malnehmen gibt es keinen Kehrwert. Richtig: Zähler 6 · x² = 6x², Nenner x · 3 = 3x, also 6x²/(3x) = 2x. Probe mit x = 3: (6/3) · (9/3) = 6 und 2x = 6."), regel="rr.bruchrechnen")

# ───────── fehler_finden ─────────
neu(T, "fehler_finden", "fehler_detektiv", FD(
    "Kim behauptet, dass vier Umformungen für alle erlaubten Zahlen stimmen. Die Zeilen sind unabhängig voneinander.",
    [("(5x + 10)/5 = x + 2", gl("(5*x+10)/5", "x+2")), ("(x² − 9)/(x − 3) = x + 3", gl("(x**2-9)/(x-3)", "x+3")), ("6/x + 3/x = 9/x", gl("6/x+3/x", "9/x")), ("(x + 4)/(x + 6) = 4/6", gl("(x+4)/(x+6)", "4/6"))],
    "Prüfe Zeile für Zeile mit einer Zahl, zum Beispiel x = 2.",
    "Bei (x + 4)/(x + 6) darf man x nicht streichen, denn x steht in einer Summe. Für x = 2 ist der Wert 6/8, aber 4/6 ist etwas anderes."), regel="rr.kuerzen")
neu(T, "fehler_finden", "verfahren_waehlen", W(
    "Wie prüfst du am besten, ob die Umformung (x + 3)/(x + 5) = 3/5 stimmt?",
    "Eine Zahl einsetzen, zum Beispiel x = 1: links 4/6, rechts 3/5. Die Werte sind verschieden, also ist die Umformung falsch.",
    [("Das x streichen. Es bleibt 3/5 übrig, also stimmt die Umformung.", "aus einer Summe gekürzt"), ("Nur x = 0 einsetzen: links 3/5, rechts 3/5. Die Werte sind gleich, also stimmt die Umformung immer.", "ein einziger gleicher Wert beweist nichts"), ("Zähler und Nenner jeweils durch 3 teilen. Dann stimmt es.", "x + 3 geteilt durch 3 ist nicht x")],
    "Ein Gegenbeispiel reicht, um eine Umformung zu widerlegen. Ein einziges passendes Beispiel beweist aber noch nichts.",
    "Für x = 1 ist (1 + 3)/(1 + 5) = 4/6 und 3/5 ist etwas anderes. Damit ist die Umformung widerlegt. x = 0 war zufällig ein Fall, in dem beide Seiten gleich sind.",
    lambda: wert_an("(x+3)/(x+5)", 1) != wert_an("3/5", 1) and wert_an("(x+3)/(x+5)", 0) == wert_an("3/5", 0) and wert_an("(x+3)/(x+5)", 3) != wert_an("3/5", 3)), regel="rr.kuerzen")
neu(T, "fehler_finden", "zwei_wege", Z(
    "Wie groß ist T(7) für T(x) = (4x + 12)/(x + 3)? Rechne auf zwei Wegen. Weg A: x = 7 gleich einsetzen. Weg B: erst im Zähler 4 ausklammern, mit (x + 3) kürzen und dann x = 7 einsetzen.",
    4, "(4 * 7 + 12) / (7 + 3)", 4, "Beide Wege müssen dasselbe ergeben.",
    "Weg A: (28 + 12)/(7 + 3) = 40/10 = 4. Weg B: 4(x + 3)/(x + 3) = 4. Der Term ist immer 4, solange x ≠ −3 ist.",
    [(28, "fb.kuerzen.nur_zaehler_oder_nenner", "nur den Zähler berechnet"), (10, None, "nur den Nenner berechnet")]), regel="rr.kuerzen")
assert gl("(4*x+12)/(x+3)", "4")
