T = "terme.umformen"
# ───────── zusammenfassen ─────────
neu(T, "zusammenfassen", "lueckenweg", L(
    "Fasse zusammen: 6a + 3b + 5a + 4b. Gleichartige Glieder gehören zusammen. Bei a: 6a + 5a = ①a. Bei b: 3b + 4b = ②b.",
    KOMM(2), [11, 7], ["6 + 5", "3 + 4"], ["5 + 6", "7"], "Zähle nur die Zahlen vor gleichen Buchstaben zusammen.",
    "6 + 5 = 11 und 3 + 4 = 7. Ergebnis: 11a + 7b. a und b bleiben getrennt.",
    {0: [(30, None, "die Zahlen malgenommen statt addiert")], 1: [(12, "fb.tauschen.ungleiches_zusammengefasst", "auch die a-Glieder dazugezählt")]}), regel="rr.tauschen")
neu(T, "zusammenfassen", "fehler_detektiv", FD(
    "Kim fasst 3x² + 5x − x² + 2x zusammen.",
    [("3x² − x² = 2x²", gl("3*x**2-x**2", "2*x**2")), ("5x + 2x = 7x", gl("5*x+2*x", "7*x")), ("Ergebnis: 2x² + 7x = 9x³", gl("2*x**2+7*x", "9*x**3"))],
    "Darf man x² und x zusammenzählen? Prüfe mit x = 2.",
    "x² und x sind nicht gleichartig. Das Ergebnis bleibt 2x² + 7x. Probe mit x = 2: 2 · 4 + 14 = 22, aber 9 · 8 = 72."), regel="rr.tauschen")
neu(T, "zusammenfassen", "anwenden", Z(
    "Ein Rechteck ist (3x + 4) cm lang und (x + 2) cm breit. Fasse den Umfang als Term zusammen. Wie groß ist der Umfang für x = 6?",
    60, "2 * (3 * 6 + 4) + 2 * (6 + 2)", "8 * 6 + 12", "Der Umfang ist 2 · Länge + 2 · Breite. Fasse die x-Glieder und die Zahlen getrennt zusammen.",
    "U = 2(3x + 4) + 2(x + 2) = 6x + 8 + 2x + 4 = 8x + 12. Für x = 6: 8 · 6 + 12 = 60 cm.",
    [(30, None, "nur die halbe Rechnung: Länge plus Breite ohne Verdopplung"), (66, "fb.ausmultiplizieren.nur_erster_summand", "die 2 nur bei den x-Gliedern gerechnet: 2·(3·6) + 4 + 2·6 + 2")], "cm"),
    regel="rr.tauschen")
assert gl("2*(3*x+4)+2*(x+2)", "8*x+12")

# ───────── produkte ─────────
neu(T, "produkte", "lueckenweg", L(
    "Vereinfache (−3a) · 4a · 2b. Die Zahlen werden malgenommen: (−3) · 4 · 2 = ①. Die Variablen a · a · b ergeben a²b. Ergebnis: ①a²b.",
    KOMM(1), [-24], ["(-3) * 4 * 2"], ["-3 * 8"], "Multipliziere die Zahlen von links nach rechts. Achte auf das Vorzeichen.",
    "(−3) · 4 = −12 und −12 · 2 = −24. Ergebnis: −24a²b.",
    {0: [(24, "fb.vorzeichen.falsches_zeichen", "das Minus vergessen"), (3, "fb.tauschen.ungleiches_zusammengefasst", "−3 + 4 + 2 gerechnet")]}), regel="rr.vorzeichen")
neu(T, "produkte", "zwei_wege", Z(
    "Berechne (−2x) · (3x) für x = 4 auf zwei Wegen. Weg A: erst vereinfachen, dann x = 4 einsetzen. Weg B: erst x = 4 einsetzen, dann malnehmen. Welchen Wert erhältst du?",
    -96, "(-2 * 4) * (3 * 4)", "-6 * 4 ** 2", "Beide Wege müssen dasselbe ergeben. Beachte das Vorzeichen.",
    "Weg A: (−2x) · (3x) = −6x². Für x = 4: −6 · 16 = −96. Weg B: (−8) · 12 = −96.",
    [(96, "fb.vorzeichen.falsches_zeichen", "das Minus vergessen"), (-24, "fb.potenz.basis_mal_hochzahl", "x² als 2x gerechnet: −6 · 4")]), regel="rr.vorzeichen")
neu(T, "produkte", "umkehren", Z(
    "Für welche Zahl a gilt (−4x) · (a · x²) = 20x³?",
    -5, "20 / (-4)", -5, "Vergleiche die Zahlen vor x³. Was mal −4 ergibt 20?",
    "Die Zahlen: (−4) · a = 20, also a = 20 : (−4) = −5. Probe: (−4x) · (−5x²) = 20x³.",
    [(5, "fb.vorzeichen.falsches_zeichen", "das Vorzeichen übersehen"), (16, None, "20 − 4 gerechnet"), (-80, None, "20 · (−4) gerechnet")]), regel="rr.vorzeichen")
assert gl("(-4*x)*(-5*x**2)", "20*x**3")

# ───────── minusklammer ─────────
neu(T, "minusklammer", "lueckenweg", L(
    "Löse die Klammer auf: 9x − (4x − 7). Das Minus vor der Klammer kehrt beide Vorzeichen um: 9x − 4x + ①. Zusammengefasst: ②x + ①.",
    KOMM(2), [7, 5], ["7", "9 - 4"], ["-(-7)", "5"], "Aus − (… − 7) wird + 7.",
    "9x − (4x − 7) = 9x − 4x + 7 = 5x + 7.",
    {0: [(-7, "fb.minusklammer.nur_erstes_zeichen", "nur das erste Vorzeichen umgedreht")], 1: [(13, None, "9 + 4 gerechnet")]}), regel="rr.minusklammer")
assert gl("9*x-(4*x-7)", "5*x+7")
neu(T, "minusklammer", "fehler_detektiv", FD(
    "Kim löst die Klammern auf: 6x − (2x + 5) − (x − 3).",
    [("6x − (2x + 5) − (x − 3) = 6x − 2x − 5 − x − 3", gl("6*x-(2*x+5)-(x-3)", "6*x-2*x-5-x-3")),
     ("= (6x − 2x − x) + (−5 − 3)", gl("6*x-2*x-5-x-3", "(6*x-2*x-x)+(-5-3)")), ("= 3x − 8", gl("(6*x-2*x-x)+(-5-3)", "3*x-8"))],
    "Wie ändert das Minus vor der zweiten Klammer das Vorzeichen von −3?",
    "Vor (x − 3) steht ein Minus. Dann wird aus −3 ein +3: 6x − 2x − 5 − x + 3 = 3x − 2.", frage="In welcher Zeile steckt der erste Fehler?"), regel="rr.minusklammer")
neu(T, "minusklammer", "zwei_wege", Z(
    "Berechne den Term 8x − (3x − 5) für x = 4 auf zwei Wegen. Weg A: erst die Klammer auflösen und zusammenfassen, dann x = 4 einsetzen. Weg B: erst x = 4 einsetzen, dann rechnen. Welchen Wert hat der Term?",
    25, "8 * 4 - (3 * 4 - 5)", "5 * 4 + 5", "Beide Wege müssen denselben Wert ergeben. Bei Weg A wird aus − (3x − 5) zuerst −3x + 5.",
    "Weg A: 8x − 3x + 5 = 5x + 5. Für x = 4: 25. Weg B: 8 · 4 = 32, 3 · 4 − 5 = 7, 32 − 7 = 25.",
    [(15, "fb.minusklammer.nur_erstes_zeichen", "−5 statt +5 aufgelöst: 32 − 12 − 5"), (39, None, "32 + 7 gerechnet")]), regel="rr.minusklammer")

# ───────── ausmultiplizieren ─────────
neu(T, "ausmultiplizieren", "lueckenweg", L(
    "Multipliziere aus: 5(2x − 3). Erstes Glied: 5 · 2x = ①x. Zweites Glied: 5 · (−3) = ②. Ergebnis: ①x + ②.",
    KOMM(2), [10, -15], ["5 * 2", "5 * (-3)"], ["10", "-15"], "Der Faktor 5 wird mit jedem Glied in der Klammer malgenommen.",
    "5 · 2x = 10x und 5 · (−3) = −15. Ergebnis: 10x − 15.",
    {1: [(-3, "fb.ausmultiplizieren.nur_erster_summand", "die 5 nur beim ersten Glied verwendet"), (15, "fb.vorzeichen.falsches_zeichen", "das Minus vergessen")]}), regel="rr.ausmultiplizieren")
neu(T, "ausmultiplizieren", "bruecke", W(
    "Die Tabelle zeigt das Ausmultiplizieren. In der Kopfzeile stehen die Glieder der Klammer, links der Faktor, in der Zeile die Teilergebnisse. Welcher Term wurde ausmultipliziert?",
    "3(2x − 5)", [("3(2x + 5)", "das Vorzeichen der 15 übersehen"), ("3 · 2x − 5", "die 3 nur auf das erste Glied bezogen"), ("2(3x − 5)", "Faktor und Glied vertauscht")],
    "Der Faktor links mal jedes Kopfglied ergibt das Feld darunter.",
    "3 · 2x = 6x und 3 · (−5) = −15. Das passt zu 3(2x − 5) = 6x − 15.",
    lambda: gl("3*(2*x-5)", "6*x-15") and not gl("3*(2*x+5)", "6*x-15") and not gl("3*2*x-5", "6*x-15") and not gl("2*(3*x-5)", "6*x-15"),
    grafik=TAB(["·", "2x", "−5"], ["3", "6x", "−15"])), regel="rr.ausmultiplizieren")
neu(T, "ausmultiplizieren", "anwenden", Z(
    "Eine Terrasse ist 3 m breit und (2x + 1) m lang. Ihre Fläche ist 3(2x + 1) m². Die Fläche soll 39 m² groß sein. Wie groß ist x?",
    6, "(39 - 3) / 6", "(39 // 3 - 1) // 2", "Multipliziere zuerst aus. Dann hast du eine Gleichung mit x.",
    "3(2x + 1) = 6x + 3. Aus 6x + 3 = 39 folgt 6x = 36, also x = 6. Die Terrasse ist dann 13 m lang.",
    [(6.5, "fb.ausmultiplizieren.nur_erster_summand", "die +3 nicht berücksichtigt: 39 : 6"), (13, None, "die Länge 2x + 1 statt x angegeben")], ), g="einkleidung", regel="rr.ausmultiplizieren")

# ───────── aequivalenz ─────────
neu(T, "aequivalenz", "lueckenweg", L(
    "Sind 2(x + 3) und 2x + 3 äquivalent? Setze x = 4 ein. Für 2(x + 3) erhältst du 2 · (4 + 3) = ①. Für 2x + 3 erhältst du 2 · 4 + 3 = ②. Die Werte sind verschieden, also sind die Terme nicht äquivalent.",
    KOMM(2), [14, 11], ["2 * (4 + 3)", "2 * 4 + 3"], ["2 * 7", "8 + 3"], "Rechne erst die Klammer, dann das Malnehmen.",
    "2 · 7 = 14 und 8 + 3 = 11. Wären die Terme äquivalent, kämen für jedes x gleiche Werte heraus.",
    {0: [(11, None, "die Klammer wie beim zweiten Term gerechnet")], 1: [(14, None, "die 2 wie bei der Klammer auf die 3 bezogen")]}), regel="id.algebra.term")
neu(T, "aequivalenz", "bruecke", W(
    "Die Tabelle zeigt die Werte eines Terms für x = 1 bis 4. Welcher der Terme hat für alle vier Werte von x dieselben Werte?",
    "3(x + 1) + 2", [("3x + 2", "nur den Anfang der Tabelle nachgeprüft: für x = 1 ist 5, nicht 8"), ("5x + 3", "stimmt für x = 1, aber nicht für x = 2"), ("3(x + 5)", "Klammer falsch ausmultipliziert, ergibt 3x + 15")],
    "Prüfe jeden Term mit zwei Werten von x aus der Tabelle. Ein einziger Wert reicht nicht.",
    "3(x + 1) + 2 = 3x + 5: 8, 11, 14, 17. Das passt in allen vier Spalten. 5x + 3 liefert 8, 13, 18, 23.",
    lambda: gl("3*(x+1)+2", "3*x+5") and [3 * k + 5 for k in (1, 2, 3, 4)] == [8, 11, 14, 17] and not gl("3*x+2", "3*x+5") and not gl("5*x+3", "3*x+5") and not gl("3*(x+5)", "3*x+5"),
    grafik=TAB(["x", "1", "2", "3", "4"], ["Wert", "8", "11", "14", "17"])), regel="id.algebra.term")
neu(T, "aequivalenz", "umkehren", Z(
    "Für welche Zahl a sind die Terme 3(x + a) und 3x + 15 äquivalent?",
    5, "15 / 3", 5, "Multipliziere 3(x + a) aus. Dann vergleiche die Zahlen ohne x.",
    "3(x + a) = 3x + 3a. Es muss 3a = 15 gelten, also a = 5. Probe: 3(x + 5) = 3x + 15.",
    [(15, "fb.ausmultiplizieren.nur_erster_summand", "die 3 vor der Klammer vergessen"), (12, None, "15 − 3 gerechnet")], ), g="umkehr", regel="id.algebra.term")
assert gl("3*(x+5)", "3*x+15")
