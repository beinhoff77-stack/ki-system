T = "terme.potenzgesetze_ganzzahlig"
# ───────── warum_gilt ─────────
neu(T, "warum_gilt", "lueckenweg", L(
    "Setze das Muster fort: 4⁴ = 256 und 4³ = 64. Bei jedem Schritt nach rechts wird durch 4 geteilt. Dann ist 4² = ① und 4⁰ = ②.",
    KOMM(2), [16, 1], ["64 // 4", "(64 // 4) // 4 // 4"], ["16", "1"], "Teile den Wert immer wieder durch die Basis. Wie oft musst du teilen, bis du bei der Hochzahl 0 bist?",
    "64 : 4 = 16 für 4². Dann 16 : 4 = 4 für 4¹ und 4 : 4 = 1 für 4⁰. Also 4⁰ = 1.",
    {0: [(60, "fb.potenz.basis_mal_hochzahl", "64 − 4 gerechnet")], 1: [(0, "fb.potenz.negative_hochzahl_als_minus", "Hochzahl 0 als Wert 0 gelesen")]}), regel="rr.potenz")
neu(T, "warum_gilt", "bruecke", W(
    "Die Tabelle zeigt das Muster der Potenzen von 2. Bei jedem Schritt nach rechts wird der Wert halbiert. Welcher Wert gehört zu 2⁻²?",
    "1/4", [("−4", "negative Hochzahl als negative Zahl gelesen", "fb.potenz.negative_hochzahl_als_minus"), ("1/2", "mit der Hochzahl −1 verwechselt"), ("−1/4", "negative Hochzahl als Minus vor dem Bruch")],
    "Setze das Halbieren in der Tabelle von rechts nach rechts fort.",
    "2⁰ = 1, 2⁻¹ = 1/2, 2⁻² = 1/4. Bei jedem Schritt nach rechts wird halbiert.",
    lambda: 2 ** -2 == F(1, 4) and F(1, 2) != F(1, 4),
    grafik=TAB(["2³", "2²", "2¹", "2⁰", "2⁻¹", "2⁻²"], ["8", "4", "2", "1", "?", "?"])), regel="rr.potenz")
neu(T, "warum_gilt", "umkehren", Z(
    "Für welche ganze Zahl k gilt 3^k = 1/27?",
    -3, -3, -3, "Schreibe 27 als Potenz von 3. Eine negative Hochzahl bedeutet: Kehrwert.",
    "27 = 3³. Also 1/27 = 1/3³ = 3⁻³. Probe: 3⁻³ = 1/27.",
    [(3, "fb.potenz.negative_hochzahl_als_minus", "das Minus der Hochzahl vergessen"), (-9, None, "27 : 3 mit Minus gerechnet"), (27, None, "27 selbst als Hochzahl genommen")]), g="umkehr", regel="rr.potenz")
assert F(1, 27) == F(3) ** -3

# ───────── gleiche_basis_ganz ─────────
neu(T, "gleiche_basis_ganz", "lueckenweg", L(
    "Vereinfache z⁴ · z⁻⁹ zu z^k. Die Hochzahlen werden addiert: k = ①. Multiplizierst du das Ergebnis noch mit z⁶, ergibt sich die Hochzahl ②.",
    KOMM(2), [-5, 1], ["4 + (-9)", "4 + (-9) + 6"], ["-5", "1"], "Gleiche Basis beim Malnehmen: Hochzahlen addieren. Achte auf das Vorzeichen.",
    "4 + (−9) = −5, also z⁻⁵. Mit z⁶: −5 + 6 = 1, also z¹ = z.",
    {0: [(13, "fb.plusminus.zeichen_des_ergebnisses", "4 + 9 gerechnet"), (5, "fb.plusminus.zeichen_des_ergebnisses", "das Vorzeichen des Ergebnisses vergessen")], 1: [(11, None, "5 + 6 gerechnet")]}), regel="rr.potenz")
neu(T, "gleiche_basis_ganz", "zwei_wege", Z(
    "Berechne 2⁵ · 2⁻² auf zwei Wegen. Weg A: schreibe 2⁻² als Bruch und rechne 32 mal diesen Bruch. Weg B: addiere die Hochzahlen und berechne die Potenz. Welchen Wert hat das Produkt?",
    8, "2 ** (5 + (-2))", "32 * (1 / 4)", "Beide Wege müssen denselben Wert ergeben.",
    "Weg A: 2⁻² = 1/4. 32 · 1/4 = 8. Weg B: 5 + (−2) = 3, also 2³ = 8.",
    [(128, "fb.potenz.negative_hochzahl_als_minus", "5 + 2 gerechnet: 2⁷"), (30, None, "32 − 2 gerechnet")]), regel="rr.potenz")
neu(T, "gleiche_basis_ganz", "anwenden", Z(
    "Ein Haar ist 10⁻⁴ m dick. Eine Zelle ist 10⁻⁶ m breit. Wie viele Zellen passen nebeneinander in die Dicke eines Haars?",
    100, "10 ** -4 / 10 ** -6", "10 ** (-4 - (-6))", "Teile die Dicke des Haars durch die Breite einer Zelle. Subtrahiere die Hochzahlen.",
    "10⁻⁴ : 10⁻⁶ = 10⁻⁴⁻⁽⁻⁶⁾ = 10² = 100. Es passen 100 Zellen nebeneinander.",
    [(0.01, "fb.gegenrechnung.reihenfolge_nicht_umgekehrt", "die Zahlen vertauscht: 10⁻⁶ : 10⁻⁴"), (2, None, "nur die Hochzahl 2 statt der Zahl 10² angegeben")], "Zellen"), g="einkleidung", regel="rr.potenz")

# ───────── exponent_und_potenz ─────────
neu(T, "exponent_und_potenz", "lueckenweg", L(
    "Vereinfache (2⁻³)⁴ zu einer Potenz 2^k. Die Hochzahlen werden verrechnet: k = ①. Der Wert der Potenz ist dann 1/②.",
    KOMM(2), [-12, 4096], ["-3 * 4", "2 ** 12"], ["-12", "4096"], "Eine Potenz wird noch einmal hoch genommen. Was geschieht mit den Hochzahlen?",
    "(2⁻³)⁴ = 2⁻¹². Das ist 1/2¹² = 1/4 096.",
    {0: [(1, "fb.potenz.hochzahlen_malgenommen", "die Hochzahlen addiert: −3 + 4"), (12, "fb.potenz.negative_hochzahl_als_minus", "das Vorzeichen vergessen")], 1: [(48, "fb.potenz.basis_mal_hochzahl", "4 · 12 gerechnet")]}), regel="rr.potenz")
neu(T, "exponent_und_potenz", "umkehren", Z(
    "In der Rechnung (a⁻²)^k = a⁻¹⁰ fehlt die Hochzahl k. Wie groß ist k?",
    5, "-10 // -2", 5, "Beim Hoch-Nehmen werden die Hochzahlen malgenommen. Rechne rückwärts.",
    "(−2) · k = −10, also k = 5. Probe: (a⁻²)⁵ = a⁻¹⁰.",
    [(-5, "fb.vorzeichen.falsches_zeichen", "das Vorzeichen falsch gesetzt"), (-8, "fb.potenz.hochzahlen_malgenommen", "−10 + 2 gerechnet, weil addiert statt malgenommen gedacht")]), g="umkehr", regel="rr.potenz")
neu(T, "exponent_und_potenz", "bruecke", W(
    "Der Bruch 1/(a³) soll mit einer negativen Hochzahl geschrieben werden. Welche Schreibweise ist richtig (a ≠ 0)?",
    "a⁻³", [("−a³", "negative Hochzahl als Minuszeichen gelesen", "fb.potenz.negative_hochzahl_als_minus"), ("(−a)³", "das Minus in die Klammer geschoben"), ("3a⁻¹", "die 3 als Faktor gelesen")],
    "Eine negative Hochzahl bedeutet: Kehrwert.",
    "1/a³ = a⁻³. Probe mit a = 2: 1/8 = 2⁻³.",
    lambda: gl("1/a**3", "a**-3") and not gl("1/a**3", "-a**3") and not gl("1/a**3", "(-a)**3") and not gl("1/a**3", "3*a**-1")), regel="rr.potenz")

# ───────── terme_vereinfachen ─────────
neu(T, "terme_vereinfachen", "fehler_detektiv", FD(
    "Kim vereinfacht (4x⁻²) · (3x⁵) für x ≠ 0.",
    [("Die Zahlen werden malgenommen: 4 · 3 = 12.", True), ("Die Hochzahlen werden addiert: x⁻² · x⁵ = x³.", gl("x**-2*x**5", "x**3")), ("Weil die Hochzahl −2 negativ war, ist das Ergebnis negativ: −12x³.", gl("(4*x**-2)*(3*x**5)", "-12*x**3"))],
    "Was bedeutet eine negative Hochzahl für die Zahl vor x? Probe mit x = 2.",
    "Eine negative Hochzahl macht die Zahl nicht negativ. Das Ergebnis ist 12x³. Probe mit x = 2: (4/4) · 96 = 96 und 12 · 8 = 96."), regel="rr.potenz")
neu(T, "terme_vereinfachen", "anwenden", Z(
    "Eine Bakterie ist 2 · 10⁻⁶ m lang. Wie viele solche Bakterien ergeben hintereinander gelegt 1 mm? Es gilt 1 mm = 10⁻³ m.",
    500, "10 ** -3 / (2 * 10 ** -6)", "10 ** 3 / 2", "Teile 10⁻³ durch 2 · 10⁻⁶. Teile die Zahlen und die Potenzen getrennt.",
    "10⁻³ : (2 · 10⁻⁶) = (1 : 2) · 10⁻³⁺⁶ = 0,5 · 10³ = 500. Es sind 500 Bakterien.",
    [(5000, None, "10³ durch 2 geteilt, dabei eine Null zu viel"), (50, "fb.potenz.basis_mal_hochzahl", "10² statt 10³ gerechnet"), (0.002, "fb.potenz.negative_hochzahl_als_minus", "die Hochzahlen falsch herum subtrahiert")], "Bakterien"), g="transfer", regel="rr.potenz")
neu(T, "terme_vereinfachen", "verfahren_waehlen", W(
    "Du sollst a⁵ : a⁻² vereinfachen (a ≠ 0). Welcher Weg ist richtig?",
    "Hochzahlen subtrahieren: 5 − (−2) = 7, also a⁷.",
    [("Hochzahlen subtrahieren: 5 − 2 = 3, also a³.", "das Minus der Hochzahl −2 übersehen", "fb.plusminus.doppelminus_uebersehen"), ("Hochzahlen addieren: 5 + (−2) = 3, also a³.", "wie beim Malnehmen gerechnet"), ("Hochzahlen malnehmen: 5 · (−2) = −10, also a⁻¹⁰.", "die Hochzahlen malgenommen")],
    "Beim Teilen wird die Hochzahl des Teilers abgezogen. Achte dabei auf das Vorzeichen.",
    "a⁵ : a⁻² = a⁵⁻⁽⁻²⁾ = a⁷. Probe mit a = 2: 32 : 1/4 = 128 = 2⁷.",
    lambda: gl("a**5/a**-2", "a**7") and not gl("a**5/a**-2", "a**3") and not gl("a**5/a**-2", "a**-10")), regel="rr.potenz")

# ───────── fehler_ganz ─────────
neu(T, "fehler_ganz", "fehler_detektiv", FD(
    "Kim vereinfacht 3⁻² · 3⁻³ : 3⁻¹. Die Zeilen bauen aufeinander auf.",
    [("Beim Malnehmen werden die Hochzahlen addiert: −2 + (−3) = −5, also 3⁻⁵.", gl("3**-2*3**-3", "3**-5")), ("Beim Teilen durch 3⁻¹ werden die Hochzahlen subtrahiert: −5 − (−1).", True),
     ("Das ergibt −5 + 1 = −4, also 3⁻⁴.", gl("3**-5/3**-1", "3**-4")), ("Weil die Hochzahl negativ ist, gilt 3⁻⁴ = −81.", gl("3**-4", "-81"))],
    "Was bedeutet eine negative Hochzahl für den Wert der Potenz? Prüfe mit 2⁻¹.",
    "Eine negative Hochzahl bedeutet den Kehrwert, nicht eine negative Zahl. 3⁻⁴ = 1/3⁴ = 1/81. Probe: 2⁻¹ = 1/2."), regel="rr.potenz")
neu(T, "fehler_ganz", "zwei_wege", Z(
    "Berechne 4⁻² : 4⁻⁴ auf zwei Wegen. Weg A: beide Potenzen als Brüche schreiben und teilen. Weg B: die Hochzahlen subtrahieren und die Potenz berechnen. Welchen Wert erhältst du?",
    16, "4 ** (-2 - (-4))", "(1 / 16) / (1 / 256)", "Beide Wege müssen denselben Wert ergeben.",
    "Weg A: (1/16) : (1/256) = 256/16 = 16. Weg B: −2 − (−4) = 2, also 4² = 16.",
    [(0.0625, "fb.gegenrechnung.reihenfolge_nicht_umgekehrt", "die Hochzahlen in der falschen Reihenfolge subtrahiert: 4⁻²"), (256, None, "nur 4⁴ berechnet")]), regel="rr.potenz")
neu(T, "fehler_ganz", "verfahren_waehlen", W(
    "Du sollst 2⁻³ + 2⁻³ berechnen. Welcher Weg ist richtig?",
    "Beide Potenzen als Bruch schreiben: 1/8 + 1/8 = 1/4.",
    [("Die Hochzahlen addieren: 2⁻⁶ = 1/64.", "für die Summe ein Gesetz des Malnehmens benutzt"), ("Die Basen addieren: 4⁻³ = 1/64.", "die Basen addiert, die Hochzahl behalten"), ("Die Hochzahlen malnehmen: 2⁹ = 512.", "die Hochzahlen malgenommen")],
    "Für Plus gibt es kein Potenzgesetz. Schreibe erst jede Potenz als Zahl.",
    "2⁻³ = 1/8. Zwei Achtel sind 2/8 = 1/4.",
    lambda: F(1, 8) + F(1, 8) == F(1, 4) and F(1, 64) != F(1, 4) and 512 != F(1, 4)), regel="rr.potenz")
