T = "terme.umformen"
# ───────── zusammenfassen ─────────
neu(T, "zusammenfassen", "lueckenweg", L(
    "Fasse zusammen: 6a + 3b + 5a + 4b. Zuerst die a-Glieder, dann die b-Glieder. Das Ergebnis lautet ①a + ②b. Setzt du in dieses Ergebnis a = 2 und b = 1 ein, erhältst du ③.",
    KOMM(3), [11, 7, 29], ["6 + 5", "3 + 4", "{1} * 2 + {2} * 1"], ["5 + 6", "7", "22 + 7"], "Zähle nur die Zahlen vor gleichen Buchstaben zusammen.",
    "6 + 5 = 11 und 3 + 4 = 7. Ergebnis: 11a + 7b. Für a = 2 und b = 1: 22 + 7 = 29.",
    {0: [(30, None, "die Zahlen malgenommen statt addiert", "6 * 5")], 1: [(12, "fb.tauschen.ungleiches_zusammengefasst", "auch die a-Glieder dazugezählt: 3 + 4 + 5", "3 + 4 + 5")]}), regel="rr.tauschen")
neu(T, "zusammenfassen", "fehler_detektiv", FD(
    "Kim fasst 3x² + 5x − x² + 2x zusammen.",
    [("Sortieren: 3x² + 5x − x² + 2x = 3x² − x² + 5x + 2x", gl("3*x**2+5*x-x**2+2*x", "3*x**2-x**2+5*x+2*x")),
     ("Gleichartige Glieder zusammenfassen: 3x² − x² = 2x² und 5x + 2x = 7x²", gl("5*x+2*x", "7*x**2")),
     ("Ergebnis: 2x² + 7x² = 9x²", gl("2*x**2+7*x**2", "9*x**2"))],
    "Welche Glieder sind wirklich gleichartig? Prüfe mit x = 2.",
    "5x + 2x = 7x, nicht 7x². Beim Zusammenfassen ändert sich die Hochzahl nicht. Richtig: 2x² + 7x. Probe mit x = 2: 8 + 14 = 22, aber 2x² + 7x² = 36 ist etwas anderes."), regel="rr.tauschen")
neu(T, "zusammenfassen", "anwenden", Z(
    "Ein Rechteck ist (3x + 4) cm lang und (x + 2) cm breit. Fasse den Umfang zuerst zu einem Term der Form ax + b zusammen und setze dann x = 6 ein. Wie viele Zentimeter beträgt der Umfang?",
    60, "2 * (3 * 6 + 4) + 2 * (6 + 2)", "8 * 6 + 12", "Der Umfang ist 2 · Länge + 2 · Breite. Fasse die x-Glieder und die Zahlen getrennt zusammen.",
    "U = 2(3x + 4) + 2(x + 2) = 6x + 8 + 2x + 4 = 8x + 12. Für x = 6: 8 · 6 + 12 = 60 cm.",
    [(30, None, "nur die halbe Rechnung: Länge plus Breite ohne Verdopplung", "(3 * 6 + 4) + (6 + 2)"), (54, "fb.ausmultiplizieren.nur_erster_summand", "die 2 nur bei den x-Gliedern gerechnet: 2 · 3 · 6 + 4 + 2 · 6 + 2", "2 * 3 * 6 + 4 + 2 * 6 + 2")], "cm"),
    regel="rr.tauschen")
assert gl("2*(3*x+4)+2*(x+2)", "8*x+12")

# ───────── produkte ─────────
neu(T, "produkte", "lueckenweg", L(
    "Vereinfache (−3a) · 4a · 2b. Das Ergebnis lautet ①a²b. Setzt du in dieses Ergebnis a = 1 und b = 2 ein, erhältst du ②.",
    KOMM(2), [-24, -48], ["(-3) * 4 * 2", "{1} * 1 * 2"], ["-3 * 8", "-24 * 2"], "Multipliziere zuerst alle Zahlen. Achte auf das Vorzeichen.",
    "(−3) · 4 · 2 = −24. Ergebnis: −24a²b. Für a = 1 und b = 2: −24 · 1 · 2 = −48.",
    {0: [(24, "fb.vorzeichen.falsches_zeichen", "das Minus vergessen", "3 * 4 * 2"), (3, "fb.tauschen.ungleiches_zusammengefasst", "−3 + 4 + 2 gerechnet", "-3 + 4 + 2")]}), regel="rr.vorzeichen")
neu(T, "produkte", "zwei_wege", Z(
    "Berechne (−2x) · (3x) für x = 4 auf zwei Wegen. Weg A: erst vereinfachen, dann x = 4 einsetzen. Weg B: erst x = 4 einsetzen, dann malnehmen. Welchen Wert erhältst du?",
    -96, "(-2 * 4) * (3 * 4)", "-6 * 4 ** 2", "Beide Wege müssen dasselbe ergeben. Beachte das Vorzeichen.",
    "Weg A: (−2x) · (3x) = −6x². Für x = 4: −6 · 16 = −96. Weg B: (−8) · 12 = −96.",
    [(96, "fb.vorzeichen.falsches_zeichen", "das Minus vergessen", "2 * 4 * 3 * 4"), (-24, "fb.potenz.basis_mal_hochzahl", "x² als x gerechnet: −6 · 4", "-6 * 4")]), regel="rr.vorzeichen")
neu(T, "produkte", "umkehren", Z(
    "Für welche Zahl a gilt (−4x) · (a · x²) = 20x³ für alle Zahlen x?",
    -5, "20 / (-4)", -5, "Vergleiche die Zahlen vor x³. Was mal −4 ergibt 20?",
    "Die Zahlen: (−4) · a = 20, also a = 20 : (−4) = −5. Die Hochzahlen passen für jedes x: x · x² = x³. Probe: (−4x) · (−5x²) = 20x³.",
    [(5, "fb.vorzeichen.falsches_zeichen", "das Vorzeichen übersehen", "20 / 4"), (16, None, "20 − 4 gerechnet", "20 - 4"), (-80, None, "20 · (−4) gerechnet", "20 * (-4)")]), regel="rr.vorzeichen")
assert gl("(-4*x)*(-5*x**2)", "20*x**3")

# ───────── minusklammer ─────────
neu(T, "minusklammer", "lueckenweg", L(
    "Löse die Klammer auf und fasse zusammen: 9x − (4x − 7) + 3. Das Ergebnis lautet ①x + ②. Setzt du in dieses Ergebnis x = 3 ein, erhältst du ③.",
    KOMM(3), [5, 10, 25], ["9 - 4", "7 + 3", "{1} * 3 + {2}"], ["5", "10", "15 + 10"], "Das Minus vor der Klammer kehrt beide Vorzeichen in der Klammer um.",
    "9x − 4x + 7 + 3 = 5x + 10. Für x = 3: 15 + 10 = 25.",
    {1: [(-4, "fb.minusklammer.nur_erstes_zeichen", "nur das erste Vorzeichen umgedreht: −7 + 3", "-7 + 3")], 0: [(13, None, "9 + 4 gerechnet", "9 + 4")]}), regel="rr.minusklammer")
assert gl("9*x-(4*x-7)+3", "5*x+10")
neu(T, "minusklammer", "fehler_detektiv", FD(
    "Kim löst die Klammern auf und fasst zusammen: 6x − (2x + 5) − (x − 3).",
    [("6x − (2x + 5) − (x − 3) = 6x − 2x − 5 − x − 3", gl("6*x-(2*x+5)-(x-3)", "6*x-2*x-5-x-3")),
     ("= (6x − 2x − x) + (−5 − 3)", gl("6*x-2*x-5-x-3", "(6*x-2*x-x)+(-5-3)")), ("= 3x − 8", gl("(6*x-2*x-x)+(-5-3)", "3*x-8"))],
    "Wie ändert das Minus vor der zweiten Klammer das Vorzeichen von −3?",
    "Vor (x − 3) steht ein Minus. Dann wird aus −3 ein +3: 6x − 2x − 5 − x + 3 = 3x − 2."), regel="rr.minusklammer")
neu(T, "minusklammer", "zwei_wege", Z(
    "Berechne den Term 8x − (3x − 5) für x = 4 auf zwei Wegen. Weg A: erst die Klammer auflösen und zusammenfassen, dann x = 4 einsetzen. Weg B: erst x = 4 einsetzen, dann rechnen. Welchen Wert hat der Term?",
    25, "8 * 4 - (3 * 4 - 5)", "5 * 4 + 5", "Beide Wege müssen denselben Wert ergeben. Bei Weg A wird aus − (3x − 5) zuerst −3x + 5.",
    "Weg A: 8x − 3x + 5 = 5x + 5. Für x = 4: 25. Weg B: 8 · 4 = 32, 3 · 4 − 5 = 7, 32 − 7 = 25.",
    [(15, "fb.minusklammer.nur_erstes_zeichen", "−5 statt +5 aufgelöst: 32 − 12 − 5", "32 - 12 - 5"), (39, None, "32 + 7 gerechnet", "32 + 7")]), regel="rr.minusklammer")

# ───────── ausmultiplizieren ─────────
neu(T, "ausmultiplizieren", "lueckenweg", L(
    "Multipliziere aus: 5(2x − 3). Das Ergebnis lautet ①x + ②. Setzt du in dieses Ergebnis x = 4 ein, erhältst du ③.",
    KOMM(3), [10, -15, 25], ["5 * 2", "5 * (-3)", "{1} * 4 + {2}"], ["10", "-15", "40 - 15"], "Der Faktor vor der Klammer wird mit jedem Glied in der Klammer malgenommen.",
    "5 · 2x = 10x und 5 · (−3) = −15. Für x = 4: 40 − 15 = 25.",
    {1: [(-3, "fb.ausmultiplizieren.nur_erster_summand", "die Zahl vor der Klammer nur beim ersten Glied verwendet", "-3"), (15, "fb.vorzeichen.falsches_zeichen", "das Minus vergessen", "5 * 3")]}), regel="rr.ausmultiplizieren")
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
    [(6.5, "fb.ausmultiplizieren.nur_erster_summand", "die +3 nicht berücksichtigt: 39 : 6", "39 / 6"), (13, None, "die Länge 2x + 1 statt x angegeben", "2 * 6 + 1")], ), g="einkleidung", regel="rr.ausmultiplizieren")

# ───────── aequivalenz ─────────
neu(T, "aequivalenz", "lueckenweg", L(
    "Sind 4(x + 2) und 4x + 2 äquivalent? Setze x = 3 ein. Der erste Term hat dann den Wert ① und der zweite den Wert ②. Die beiden Werte unterscheiden sich um ③. Also sind die Terme nicht äquivalent.",
    KOMM(3), [20, 14, 6], ["4 * (3 + 2)", "4 * 3 + 2", "{1} - {2}"], ["4 * 5", "12 + 2", "20 - 14"], "Rechne die Klammer zuerst aus. Dann erst malnehmen.",
    "4 · 5 = 20 und 12 + 2 = 14. Der Unterschied ist 6. Wären die Terme äquivalent, kämen für jedes x gleiche Werte heraus.",
    {0: [(14, None, "die 4 nur auf die 3 bezogen, die Klammer nicht beachtet: 4 · 3 + 2", "4 * 3 + 2")], 1: [(20, None, "die 4 auch auf die 2 bezogen: 4 · (3 + 2)", "4 * (3 + 2)")]}), regel="id.algebra.term")
neu(T, "aequivalenz", "bruecke", W(
    "Die Tabelle zeigt die Werte eines Terms für x = 1 bis 4. Welcher der Terme hat für alle vier Werte von x dieselben Werte?",
    "3(x + 1) + 2", [("3x + 2", "beim Ausmultiplizieren 3 · 1 vergessen: schon für x = 1 ist der Wert 5, nicht 8"), ("5x + 3", "nur die erste Spalte stimmt: für x = 1 ist der Wert 8, für x = 2 aber 13 statt 11"), ("3(x + 5)", "Klammer falsch ausmultipliziert, ergibt 3x + 15")],
    "Prüfe jeden Term mit zwei Werten von x aus der Tabelle. Ein einziger Wert reicht nicht.",
    "3(x + 1) + 2 = 3x + 5: 8, 11, 14, 17. Das passt in allen vier Spalten. 5x + 3 liefert 8, 13, 18, 23.",
    lambda: gl("3*(x+1)+2", "3*x+5") and [3 * k + 5 for k in (1, 2, 3, 4)] == [8, 11, 14, 17] and not gl("3*x+2", "3*x+5") and not gl("5*x+3", "3*x+5") and not gl("3*(x+5)", "3*x+5")
    and wert_an("3*x+2", 1) == 5 and wert_an("5*x+3", 1) == 8 and wert_an("5*x+3", 2) == 13 and wert_an("3*(x+5)", 1) == 18,
    grafik=TAB(["x", "1", "2", "3", "4"], ["Wert", "8", "11", "14", "17"])), regel="id.algebra.term")
neu(T, "aequivalenz", "umkehren", Z(
    "Für welche Zahl a haben die Terme 3(x + a) und 3x + 15 für jede Zahl x denselben Wert?",
    5, "15 / 3", 5, "Multipliziere 3(x + a) aus. Dann vergleiche die Zahlen ohne x.",
    "3(x + a) = 3x + 3a. Es muss 3a = 15 gelten, also a = 5. Probe: 3(x + 5) = 3x + 15.",
    [(15, None, "die 3 vor der Klammer nicht beachtet: a gleich 15 gesetzt", "15"), (12, None, "15 − 3 gerechnet", "15 - 3")], ), g="umkehr", regel="id.algebra.term")
assert gl("3*(x+5)", "3*x+15")
