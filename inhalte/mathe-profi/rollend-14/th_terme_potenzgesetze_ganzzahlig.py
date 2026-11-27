T = "terme.potenzgesetze_ganzzahlig"
# ───────── warum_gilt ─────────
a1(T, "warum_gilt", Z(
    "Die Menge eines Wirkstoffs im Blut halbiert sich jede Stunde. Zu Beginn sind es 160 mg. Nach n Stunden sind es 160 · 2⁻ⁿ mg. Wie viel Milligramm sind es nach 5 Stunden?",
    5, "160 / 2 ** 5", "160 * (1 / 2) ** 5", "2⁻ⁿ bedeutet: n-mal halbieren. Schreibe 2⁻⁵ als Bruch.",
    "2⁻⁵ ist der Bruch 1/2⁵ = 1/32. Also sind es nach 5 Stunden 160 · 1/32 = 160 : 32 = 5 mg. Probe: 160, 80, 40, 20, 10, 5 – fünfmal halbiert.",
    [(5120, None, "das Vorzeichen der Hochzahl übersehen und mit 2⁵ statt 2⁻⁵ gerechnet", "160 * 2 ** 5"), (32, None, "nur die Potenz 2⁵ als Menge angegeben", "2 ** 5"), (800, None, "160 · 5 gerechnet statt 5-mal zu halbieren", "160 * 5")], "mg"))
a2(T, "warum_gilt", Z(
    "Kim schneidet von einem 1 m langen Seil zuerst die Hälfte ab. Vom Rest schneidet Kim wieder die Hälfte ab, und danach noch einmal die Hälfte vom neuen Rest. Die drei abgeschnittenen Stücke sind 2⁻¹ m, 2⁻² m und 2⁻³ m lang. Wie viele Meter sind die drei Stücke zusammen lang? Gib das Ergebnis als Dezimalzahl an.",
    0.875, "1 / 2 + 1 / 4 + 1 / 8", "1 - 1 / 8", "Schreibe jedes Stück als Bruch. Was bedeutet 2⁻³?",
    "2⁻¹ = 1/2, 2⁻² = 1/4, 2⁻³ = 1/8. Zusammen: 1/2 + 1/4 + 1/8 = 4/8 + 2/8 + 1/8 = 7/8 = 0,875 m. Probe: Das Seil hat noch 1/8 m übrig, und 1 − 1/8 = 7/8.",
    [(0.125, None, "nur das dritte Stück angegeben", "1 / 8"), (1.5, None, "alle drei Stücke als halbe Meter gezählt", "3 * 1 / 2"), (0.375, None, "das erste Stück (die Hälfte) vergessen", "1 / 4 + 1 / 8")], "m"))
a3(T, "warum_gilt", Z(
    "Eine Substanz zerfällt so, dass ihre Menge jede Stunde auf die Hälfte sinkt. Jetzt sind 3 g da. Die Formel M(t) = 3 · 2⁻ᵗ gibt die Menge in Gramm t Stunden nach jetzt an. Für t = −2 liefert die Formel die Menge von vor 2 Stunden. Wie viel Gramm waren es vor 2 Stunden?",
    12, "3 * 2 ** 2", "3 * 2 * 2", "Setze t = −2 ein. Was bedeutet 2 hoch (−(−2))? Was passiert mit der Menge, wenn man zwei Stunden zurückgeht?",
    "Für t = −2 ist 2⁻ᵗ = 2²= 4. Also M(−2) = 3 · 4 = 12 g. Das passt: Von vor 2 Stunden bis jetzt wurde die Menge zweimal halbiert, 12 → 6 → 3.",
    [(0.75, None, "t = 2 statt t = −2 eingesetzt, also mit 2⁻² statt 2² gerechnet", "3 / 2 ** 2"), (6, None, "nur eine Stunde zurückgerechnet: 3 · 2", "3 * 2"), (1.5, None, "die Menge halbiert statt verdoppelt", "3 / 2")], "g"), g="transfer")
# ───────── gleiche_basis_ganz ─────────
a1(T, "gleiche_basis_ganz", Z(
    "Ein Staubkorn ist 10⁻⁵ m dick. Ein Blatt Papier ist 10⁻⁴ m dick. 50 Blätter liegen aufeinander. Wie viele Staubkörner müsste man aufeinanderlegen, um dieselbe Dicke zu erreichen?",
    500, "50 / 10 ** 4 * 10 ** 5", "50 * 10", "Wie viele Staubkörner sind so dick wie ein Blatt? Teile 10⁻⁴ durch 10⁻⁵.",
    "Ein Blatt: 10⁻⁴ : 10⁻⁵ = 10⁻⁴⁻⁽⁻⁵⁾ = 10¹ = 10 Staubkörner. Bei 50 Blättern sind es 50 · 10 = 500 Staubkörner.",
    [(5, None, "Staubkorn durch Blatt geteilt: 10⁻⁵ : 10⁻⁴ = 10⁻¹, also 50 · 0,1", "50 / 10"), (50, None, "nur die Zahl der Blätter angegeben", "50"), (5000, None, "10² statt 10¹ Staubkörner je Blatt gerechnet", "50 * 10 ** 2")], "Staubkörner"))
a2(T, "gleiche_basis_ganz", Z(
    "Ein Transistor auf einem Chip ist 5 · 10⁻⁹ m breit. Ein Streifen auf dem Chip ist 2 · 10⁻⁵ m lang. Auf dem Streifen sollen Transistoren lückenlos nebeneinander liegen. Wie viele Transistoren passen auf den Streifen?",
    4000, "2 / 10 ** 5 / (5 / 10 ** 9)", "20000 / 5", "Teile die Länge des Streifens durch die Breite eines Transistors. Rechne Zahlen und Zehnerpotenzen getrennt.",
    "Anzahl = (2 · 10⁻⁵) : (5 · 10⁻⁹) = (2 : 5) · 10⁻⁵⁻⁽⁻⁹⁾ = 0,4 · 10⁴ = 4 000. Es passen 4 000 Transistoren.",
    [(400, None, "die Hochzahlen falsch subtrahiert: 10³ statt 10⁴", "2 * 10 ** 3 / 5"), (25000, None, "die Zahlenfaktoren vertauscht (5 durch 2 statt 2 durch 5)", "5 * 10 ** 4 / 2"), (40000, None, "die Hochzahl 5 statt 4 gerechnet", "2 * 10 ** 5 / 5")], "Transistoren"))
a3(T, "gleiche_basis_ganz", Z(
    "Ein Kristall wiegt 10⁻³ g. Ein Päckchen enthält 10ᵏ solche Kristalle und wiegt zusammen 10² g. Welche ganze Zahl ist k?",
    5, "2 - (-3)", "5", "Gesamtgewicht = Gewicht eines Kristalls mal Anzahl. Die Hochzahlen der Zehnerpotenzen werden dabei addiert.",
    "Es gilt 10⁻³ · 10ᵏ = 10², also 10⁻³⁺ᵏ = 10². Daraus folgt −3 + k = 2 und k = 5. Probe: 10⁻³ · 10⁵ = 10² = 100 g.",
    [(-1, None, "−3 und 2 addiert statt k aus −3 + k = 2 zu bestimmen", "-3 + 2"), (-5, None, "das Vorzeichen von k falsch bestimmt", "-(2 + 3)")]), g="rueckwaerts")
# ───────── exponent_und_potenz ─────────
a1(T, "exponent_und_potenz", Z(
    "Ein quadratisches Pixel auf einem Bildschirm hat die Seitenlänge 2⁻³ mm. Wie groß ist die Fläche des Pixels in mm²? Gib sie als Dezimalzahl an.",
    0.015625, "1 / 2 ** 6", "(1 / 8) ** 2", "Fläche eines Quadrats = Seite mal Seite. Welche Hochzahl hat (2⁻³)²?",
    "A = (2⁻³)² = 2⁻³˙² = 2⁻⁶ = 1/64 = 0,015625 mm². Probe: 1/8 · 1/8 = 1/64.",
    [(0.125, None, "nur die Seitenlänge 2⁻³ als Fläche angegeben", "1 / 8"), (64, None, "das Vorzeichen der Hochzahl vergessen: 2⁶", "2 ** 6"), (0.0625, None, "die Fläche als 2⁻⁴ gerechnet (−3 + (−1))", "1 / 2 ** 4")], "mm²"))
a2(T, "exponent_und_potenz", Z(
    "Ein würfelförmiger Behälter hat die Kantenlänge 5⁻¹ m. Wie viele Liter fasst er? Es gilt 1 m³ = 1 000 Liter.",
    8, "1000 / 5 ** 3", "1000 * 0.2 ** 3", "Das Volumen eines Würfels ist Kante mal Kante mal Kante. Rechne zuerst in m³, dann in Liter.",
    "V = (5⁻¹)³ m³ = 5⁻³ m³ = 1/125 m³. Das sind 1 000 : 125 = 8 Liter. Probe: Die Kante ist 0,2 m = 2 dm, und 2 dm · 2 dm · 2 dm = 8 dm³ = 8 Liter.",
    [(125000, None, "das Vorzeichen der Hochzahl vergessen: 5³ m³ = 125 m³ in Liter", "1000 * 5 ** 3"), (0.008, None, "das Volumen in m³ nicht in Liter umgerechnet", "1 / 5 ** 3"), (200, None, "die Kantenlänge 0,2 m mal 1 000 gerechnet", "1000 / 5")], "l"))
a3(T, "exponent_und_potenz", Z(
    "Alex hat ein Zahlenrätsel gestellt: Es gibt genau eine ganze Zahl k, für die (3⁻²)ᵏ · 3⁷ = 3 gilt. Welche Zahl ist k?",
    3, "(7 - 1) / 2", "3", "Fasse die linke Seite zu einer einzigen Potenz von 3 zusammen. Welche Hochzahl hat (3⁻²)ᵏ?",
    "(3⁻²)ᵏ = 3⁻²ᵏ. Dann ist 3⁻²ᵏ · 3⁷ = 3⁻²ᵏ⁺⁷. Das soll 3¹ sein, also −2k + 7 = 1, 2k = 6 und k = 3. Probe: (3⁻²)³ · 3⁷ = 3⁻⁶ · 3⁷ = 3.",
    [(4, None, "7 plus 1 statt 7 minus 1 gerechnet", "(7 + 1) / 2"), (-3, None, "das Vorzeichen von k falsch bestimmt", "-(7 - 1) / 2"), (6, None, "die Hochzahl 6 aus −2k + 7 = 1 nicht durch 2 geteilt", "7 - 1")]), g="rueckwaerts")
# ───────── terme_vereinfachen ─────────
a1(T, "terme_vereinfachen", Z(
    "Ein Rechteck hat den Flächeninhalt 6x⁴ cm². Eine Seite ist 2x⁶ cm lang. Dabei ist x = 2. Wie lang ist die andere Seite in Zentimetern?",
    0.75, "6 * 2 ** 4 / (2 * 2 ** 6)", "3 / 4", "Länge der anderen Seite = Fläche : bekannte Seite. Vereinfache den Bruch zuerst, setze x = 2 zuletzt ein.",
    "Andere Seite = 6x⁴ : (2x⁶) = 3 · x⁴⁻⁶ = 3x⁻² = 3/x². Für x = 2: 3/4 = 0,75 cm. Probe: 2 · 2⁶ = 128 cm mal 0,75 cm = 96 cm², und 6 · 2⁴ = 96.",
    [(12, None, "x⁻² als x² gedeutet", "3 * 2 ** 2"), (3, None, "x⁻² vergessen", "3"), (1.5, None, "x⁻² als x⁻¹ gerechnet: 3 : 2", "3 / 2")], "cm"))
a2(T, "terme_vereinfachen", Z(
    "Der Preis für ein Bastelset (in Euro) wird durch K(x) = 20x⁵ : (4x⁷) beschrieben. Dabei ist x die Zahl der gekauften Hunderterpackungen. Wie viel Euro kostet ein Set bei x = 5?",
    0.2, "20 * 5 ** 5 / (4 * 5 ** 7)", "5 / 25", "Vereinfache K(x) zuerst: Zahlen für sich, Potenzen von x für sich. Danach setzt du x = 5 ein.",
    "K(x) = (20 : 4) · x⁵⁻⁷ = 5x⁻² = 5/x². Für x = 5: 5/25 = 0,2. Ein Set kostet 0,20 €.",
    [(125, None, "x⁻² als x² gedeutet", "5 * 5 ** 2"), (5, None, "x⁻² vergessen", "5"), (1, None, "x⁻² als x⁻¹ gerechnet: 5 : 5", "5 / 5")], "€"))
a3(T, "terme_vereinfachen", Z(
    "Alex vereinfacht den Term (6x⁻³ · x⁵) : (3x⁻¹) zu einem Produkt c · xⁿ. Danach setzt er x = 2 ein. Welchen Wert erhält er?",
    16, "6 / 2 ** 3 * 2 ** 5 / (3 / 2)", "2 * 2 ** 3", "Fasse Zähler und Nenner getrennt zusammen. Beim Teilen durch x⁻¹ wird die Hochzahl −1 abgezogen.",
    "Zähler: 6x⁻³ · x⁵ = 6x². Dann 6x² : (3x⁻¹) = 2 · x²⁻⁽⁻¹⁾ = 2x³. Für x = 2: 2 · 8 = 16. Probe mit dem Ausgangsterm: 6 · 2⁻³ · 2⁵ = 24 und 3 · 2⁻¹ = 1,5, und 24 : 1,5 = 16.",
    [(4, None, "beim Teilen durch x⁻¹ die Hochzahl 1 abgezogen statt −1, also 2x¹", "2 * 2"), (8, None, "den Faktor 2 aus der Teilung der Zahlen vergessen, also x³", "2 ** 3"), (32, None, "die Hochzahl 4 statt 3 gerechnet: 2x⁴", "2 * 2 ** 4")]), g="verknuepfen")
# ───────── fehler_ganz ─────────
a1(T, "fehler_ganz", Z(
    "Kim behauptet: 4⁻¹ + 4⁻¹ = 4⁻². Mit einer Zahlenprobe kann man das prüfen. Um wie viel ist die linke Seite größer als die rechte Seite? Gib das Ergebnis als Dezimalzahl an.",
    0.4375, "1 / 4 + 1 / 4 - 1 / 16", "0.5 - 0.0625", "Berechne beide Seiten einzeln als Bruch oder als Dezimalzahl. Dann bildest du die Differenz.",
    "Linke Seite: 4⁻¹ + 4⁻¹ = 1/4 + 1/4 = 1/2 = 0,5. Rechte Seite: 4⁻² = 1/16 = 0,0625. Die Behauptung stimmt nicht. Unterschied: 0,5 − 0,0625 = 0,4375. Beim Addieren gleicher Potenzen werden die Hochzahlen nicht addiert.",
    [(0.5, None, "nur die linke Seite angegeben", "1 / 4 + 1 / 4"), (0.0625, None, "nur die rechte Seite angegeben", "1 / 16")]))
a2(T, "fehler_ganz", Z(
    "Kim berechnet 10⁻² · 10⁵ : 10⁻¹ und erhält 100. Die Zahlenprobe zeigt: Das stimmt nicht. Wie groß ist der richtige Wert?",
    10000, "10 ** 5 / 10 ** 2 * 10", "0.01 * 100000 / 0.1", "Kim hat beim Teilen durch 10⁻¹ vermutlich die Hochzahl falsch abgezogen. Rechne mit Brüchen nach.",
    "Beim Malnehmen addiert man: −2 + 5 = 3, also 10³. Beim Teilen durch 10⁻¹ zieht man −1 ab: 3 − (−1) = 4, also 10⁴ = 10 000. Probe mit Zahlen: 0,01 · 100 000 = 1 000, und 1 000 : 0,1 = 10 000.",
    [(1000, None, "das Teilen durch 10⁻¹ nicht beachtet", "10 ** 3"), (100, None, "statt −1 die Hochzahl 1 abgezogen, also 10² statt 10⁴", "10 ** 2")]))
a3(T, "fehler_ganz", Z(
    "Kim behauptet für a ≠ 0: (a⁻²)³ · a⁵ = a. Wie groß ist die linke Seite für a = 2, wenn man richtig rechnet?",
    0.5, "1 / 2 ** 6 * 2 ** 5", "2 ** (-6 + 5)", "Berechne zuerst (a⁻²)³ mit der Regel für Potenz einer Potenz. Danach multiplizierst du mit a⁵.",
    "(a⁻²)³ = a⁻⁶. Dann a⁻⁶ · a⁵ = a⁻¹ = 1/a. Für a = 2 ist das 1/2 = 0,5. Kims Rechnung bricht bei −6 + 5 ab, das ist −1 und nicht 1. Probe: 2⁻⁶ · 2⁵ = 32/64 = 0,5.",
    [(2, None, "die Hochzahlen −6 und 5 so verrechnet, dass 1 statt −1 herauskommt (a¹)", "2 ** 1"), (0.015625, None, "das Produkt mit a⁵ vergessen", "1 / 2 ** 6"), (32, None, "nur a⁵ berechnet", "2 ** 5")]), g="pruefung")
