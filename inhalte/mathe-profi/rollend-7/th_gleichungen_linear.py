T = "gleichungen.linear"
# ───────── waage ─────────
neu(T, "waage", "lueckenweg", L(
    "Löse 4x + 9 = 33. Auf beiden Seiten 9 abziehen: 4x = ①. Auf beiden Seiten durch 4 teilen: x = ②.",
    KOMM(2), [24, 6], ["33 - 9", "(33 - 9) / 4"], ["24", "24 // 4"], "Mache auf beiden Seiten dasselbe.",
    "33 − 9 = 24. 24 : 4 = 6. Probe: 4 · 6 + 9 = 33.",
    {0: [(42, "fb.waage.zeichen_nicht_gedreht", "die 9 addiert statt abgezogen")], 1: [(20, None, "24 − 4 gerechnet statt 24 : 4")]}), regel="rr.waage")
neu(T, "waage", "bruecke", W(
    "Eine Waage ist im Gleichgewicht. Links liegen 4 gleiche Dosen mit je x g Inhalt und ein Gewicht von 30 g. Rechts liegen 2 solche Dosen und ein Gewicht von 90 g. Welche Gleichung gehört zur Waage?",
    "4x + 30 = 2x + 90", [("4x + 2x = 30 + 90", "alle Dosen auf eine Seite gelegt, aber die Gewichte nicht getauscht"), ("x + 30 = x + 90", "die Zahl der Dosen vergessen"), ("4x − 30 = 2x − 90", "Gewichte als Abzug gelesen")],
    "Auf jeder Seite stehen: Dosen mal x, plus das Gewicht.",
    "Links: 4x + 30. Rechts: 2x + 90. Gleichgewicht heißt: 4x + 30 = 2x + 90. Daraus folgt x = 30.",
    lambda: ist_loesung("4*x+30", "2*x+90", 30) and not ist_loesung("4*x+2*x", "30+90", 30) and not ist_loesung("x+30", "x+90", 30) and not ist_loesung("4*x-30", "2*x-90", 30)), regel="rr.waage")
neu(T, "waage", "umkehren", Z(
    "Die Gleichung a · x + 4 = 28 hat die Lösung x = 6. Wie groß ist die Zahl a?",
    4, "(28 - 4) / 6", 4, "Setze x = 6 ein. Was muss a mal 6 ergeben?",
    "Für x = 6 gilt a · 6 + 4 = 28. Also a · 6 = 24 und a = 4. Probe: 4 · 6 + 4 = 28.",
    [(24, "fb.waage.nur_ein_summand", "nur 28 − 4 gerechnet, nicht durch 6 geteilt"), (10, None, "6 + 4 gerechnet")]), g="umkehr", regel="rr.waage")

# ───────── beide_seiten ─────────
neu(T, "beide_seiten", "lueckenweg", L(
    "Löse 6x − 5 = 2x + 15. Auf beiden Seiten 2x abziehen: 4x − 5 = 15. Auf beiden Seiten 5 addieren: 4x = ①. Durch 4 teilen: x = ②.",
    KOMM(2), [20, 5], ["15 + 5", "(15 + 5) / 4"], ["20", "20 // 4"], "Die 5 steht mit Minus. Sie wird durch Addieren weggeschafft.",
    "15 + 5 = 20. 20 : 4 = 5. Probe: 6 · 5 − 5 = 25 und 2 · 5 + 15 = 25.",
    {0: [(10, "fb.waage.zeichen_nicht_gedreht", "5 abgezogen statt addiert")], 1: [(2.5, None, "10 : 4 gerechnet")]}), regel="rr.waage")
neu(T, "beide_seiten", "zwei_wege", Z(
    "Löse 5x − 8 = 2x + 13 auf zwei Wegen. Weg A: erst 2x abziehen, sodass das x links steht. Weg B: erst 5x abziehen, sodass das x rechts steht. Welche Lösung erhältst du?",
    7, "(13 + 8) / (5 - 2)", "(8 + 13) / (5 - 2)", "Beide Wege führen zur selben Lösung. Bei Weg B ist das x-Glied am Ende negativ.",
    "Weg A: 3x − 8 = 13, 3x = 21, x = 7. Weg B: −8 = −3x + 13, −21 = −3x, x = 7. Probe: 27 = 27.",
    [(3, "fb.waage.zeichen_nicht_gedreht", "2x addiert statt abgezogen: 7x = 21"), (21, "fb.waage.nur_eine_seite", "nur 13 + 8 gerechnet, nicht durch 3 geteilt")]), regel="rr.waage")
neu(T, "beide_seiten", "anwenden", Z(
    "Tarif A kostet 6 € Grundgebühr im Monat und dazu 0,10 € je Minute. Tarif B hat keine Grundgebühr und kostet 0,16 € je Minute. Bei wie vielen Minuten im Monat kosten beide Tarife gleich viel?",
    100, "6 / (0.16 - 0.10)", "600 / 6", "Stelle für jeden Tarif einen Term mit der Minutenzahl x auf. Setze beide gleich.",
    "A: 6 + 0,10x. B: 0,16x. Gleichsetzen: 6 + 0,10x = 0,16x, also 6 = 0,06x und x = 100. Probe: A 16 €, B 16 €.",
    [(60, None, "nur durch 0,10 geteilt"), (37.5, None, "nur durch 0,16 geteilt")], "min"), g="einkleidung", regel="id.algebra.gleichung_loesen")

# ───────── klammern ─────────
neu(T, "klammern", "lueckenweg", L(
    "Löse 3(x − 2) = x + 8. Klammer auflösen: 3x − ① = x + 8. Auf beiden Seiten x abziehen: 2x − ① = 8. Auf beiden Seiten ① addieren: 2x = ②. Dann ist x = ③.",
    KOMM(3), [6, 14, 7], ["3 * 2", "8 + 6", "(8 + 6) / 2"], ["6", "14", "7"], "Die 3 vor der Klammer gilt für jedes Glied in der Klammer.",
    "3 · 2 = 6. 8 + 6 = 14. 14 : 2 = 7. Probe: 3 · 5 = 15 und 7 + 8 = 15.",
    {0: [(2, "fb.ausmultiplizieren.nur_erster_summand", "die 3 nur bei x gerechnet")], 2: [(1, "fb.waage.zeichen_nicht_gedreht", "8 − 6 statt 8 + 6 gerechnet: 2 : 2")]}), regel="rr.waage")
neu(T, "klammern", "fehler_detektiv", FD(
    "Kim löst die Gleichung 2(x + 5) − 3(x − 1) = 4.",
    [("2x + 10 − 3x − 3 = 4", gl("2*(x+5)-3*(x-1)", "2*x+10-3*x-3")), ("−x + 7 = 4", gl("2*x+10-3*x-3", "-x+7")), ("−x = −3, also x = 3", ist_loesung("-x+7", "4", 3))],
    "Wie ändert das Minus vor der zweiten Klammer das Vorzeichen von −1 in (x − 1)?",
    "−3 · (−1) = +3. Also: 2x + 10 − 3x + 3 = 4, das ergibt −x + 13 = 4 und x = 9. Probe: 28 − 24 = 4."), regel="rr.minusklammer")
neu(T, "klammern", "zwei_wege", Z(
    "Löse 4(x − 3) = 2(x + 5) auf zwei Wegen. Weg A: beide Klammern gleich ausmultiplizieren. Weg B: erst beide Seiten durch 2 teilen, dann ausmultiplizieren. Wie groß ist x?",
    11, "(10 + 12) / 2", 11, "Beide Wege müssen dasselbe x ergeben.",
    "Weg A: 4x − 12 = 2x + 10, 2x = 22, x = 11. Weg B: 2(x − 3) = x + 5, 2x − 6 = x + 5, x = 11. Probe: 32 = 32.",
    [(-1, "fb.vorzeichen.falsches_zeichen", "10 − 12 gerechnet"), (22, "fb.waage.nur_eine_seite", "2x = 22 nicht durch 2 geteilt")]), regel="rr.waage")
assert ist_loesung("4*(x-3)", "2*(x+5)", 11) and ist_loesung("2*(x-3)", "x+5", 11)

# ───────── probe ─────────
neu(T, "probe", "lueckenweg", L(
    "Prüfe, ob x = 4 die Gleichung 5x − 4 = 2x + 5 löst. Links: 5 · 4 − 4 = ①. Rechts: 2 · 4 + 5 = ②. Die beiden Seiten sind verschieden. Also ist x = 4 keine Lösung.",
    KOMM(2), [16, 13], ["5 * 4 - 4", "2 * 4 + 5"], ["20 - 4", "8 + 5"], "Setze für x überall die 4 ein. Rechne Punkt vor Strich.",
    "Links: 20 − 4 = 16. Rechts: 8 + 5 = 13. 16 ≠ 13. Die Lösung ist x = 3: 11 = 11.",
    {0: [(5, None, "nur den Teil 5 − 4 gerechnet, ohne die 4 einzusetzen")], 1: [(18, None, "2 · (4 + 5) gerechnet, falsch geklammert")]}), regel="id.algebra.gleichung_loesen")
neu(T, "probe", "bruecke", W(
    "Die Tabelle zeigt die Werte der beiden Seiten der Gleichung 3x − 2 = x + 6 für einige Zahlen x. Welche Zahl ist die Lösung?",
    "x = 4", [("x = 10", "den gemeinsamen Wert der Seiten als Lösung gelesen"), ("x = 2", "eine Spalte geraten, in der rechts mehr steht als links"), ("x = 5", "eine Spalte geraten, in der links mehr steht als rechts")],
    "Suche die Spalte, in der links und rechts denselben Wert haben. Die Lösung ist die Zahl x in dieser Spalte.",
    "Für x = 4 sind beide Seiten 10: 3 · 4 − 2 = 10 und 4 + 6 = 10. Der Wert 10 ist nicht die Lösung. Gesucht ist das x: 4.",
    lambda: ist_loesung("3*x-2", "x+6", 4) and not ist_loesung("3*x-2", "x+6", 10) and not ist_loesung("3*x-2", "x+6", 2) and not ist_loesung("3*x-2", "x+6", 5),
    grafik=TAB(["x", "1", "2", "3", "4", "5"], ["3x − 2", "1", "4", "7", "10", "13"], ["x + 6", "7", "8", "9", "10", "11"])), regel="id.algebra.gleichung_loesen")
neu(T, "probe", "umkehren", Z(
    "Die Zahl 4 ist eine Lösung der Gleichung 5x − a = 2x + 6. Wie groß ist die Zahl a?",
    6, "5 * 4 - (2 * 4 + 6)", 6, "Setze x = 4 ein. Dann bleibt eine Gleichung nur mit a.",
    "Für x = 4: 20 − a = 14. Also a = 20 − 14 = 6. Probe: 5 · 4 − 6 = 14 und 2 · 4 + 6 = 14.",
    [(14, None, "nur die rechte Seite ausgerechnet"), (34, "fb.waage.zeichen_nicht_gedreht", "20 + 14 gerechnet statt 20 − 14")]), g="umkehr", regel="id.algebra.gleichung_loesen")

# ───────── sonderfaelle ─────────
neu(T, "sonderfaelle", "lueckenweg", L(
    "Wie viele Lösungen hat 2(x + 3) = 2x + 7? Klammer auflösen: 2x + ① = 2x + 7. Auf beiden Seiten 2x abziehen: ① = 7. Diese Aussage stimmt für kein x. Die Gleichung hat ② Lösungen.",
    KOMM(2), [6, 0], ["2 * 3", "0"], ["6", "1 - 1"], "2 mal 3 ergibt das Zahlglied der Klammer.",
    "2(x + 3) = 2x + 6. Aus 6 = 7 wird eine falsche Aussage. Dann gibt es keine Lösung.",
    {1: [(1, None, "eine Lösung genannt, obwohl x herausfällt")]}), regel="id.algebra.gleichung_loesen")
neu(T, "sonderfaelle", "fehler_detektiv", FD(
    "Kim löst die Gleichung 3(x − 2) + 6 = 3x.",
    [("3x − 6 + 6 = 3x", gl("3*(x-2)+6", "3*x-6+6")), ("3x = 3x, also 0 = 0", gl("3*x-6+6", "3*x")),
     ("Das stimmt nur für x = 0. Die Gleichung hat genau eine Lösung.", not ist_loesung("3*(x-2)+6", "3*x", 5))],
    "Setze zur Probe x = 5 ein. Was fällt auf?",
    "Aus 0 = 0 folgt: Die Gleichung stimmt für jedes x. Sie hat unendlich viele Lösungen. Probe mit x = 5: 15 = 15."), regel="id.algebra.gleichung_loesen")
neu(T, "sonderfaelle", "umkehren", Z(
    "Für welche Zahl a gilt die Gleichung 2(3x − 1) = 6x + a für jede Zahl x?",
    -2, "2 * (-1)", -2, "Multipliziere die linke Seite aus. Dann muss die Zahl ohne x auf beiden Seiten gleich sein.",
    "2(3x − 1) = 6x − 2. Damit beide Seiten gleich sind, muss a = −2 sein.",
    [(2, "fb.vorzeichen.falsches_zeichen", "das Minus vergessen"), (-1, "fb.ausmultiplizieren.nur_erster_summand", "die 2 vor der Klammer vergessen")]), g="rueckwaerts", regel="id.algebra.gleichung_loesen")
assert ist_loesung("2*(3*x-1)", "6*x-2", 5) and ist_loesung("2*(3*x-1)", "6*x-2", -3)

# ───────── sach ─────────
neu(T, "sach", "lueckenweg", L(
    "Ben hat 50 € und spart jede Woche 5 €. Mia hat 20 € und spart jede Woche 10 €. Nach w Wochen haben beide gleich viel: 50 + 5w = 20 + 10w. Auf beiden Seiten 5w abziehen: 50 = 20 + ①w. Dann 20 abziehen: ② = ①w. Also ist w = ③.",
    KOMM(3), [5, 30, 6], ["10 - 5", "50 - 20", "(50 - 20) / (10 - 5)"], ["5", "30", "6"], "Auf jeder Seite wird derselbe Term abgezogen.",
    "10w − 5w = 5w. 50 − 20 = 30. 30 : 5 = 6. Nach 6 Wochen haben beide 80 €.",
    {0: [(15, None, "10 + 5 gerechnet")], 2: [(10, None, "30 : 3 gerechnet")]}), regel="id.algebra.gleichung_loesen")
neu(T, "sach", "bruecke", W(
    "Ein Handwerker verlangt 35 € für die Anfahrt und 42 € für jede Stunde Arbeit. Die Rechnung beträgt 245 €. Mit x sind die Arbeitsstunden gemeint. Welche Gleichung gehört zur Rechnung?",
    "35 + 42x = 245", [("35x + 42 = 245", "Anfahrt und Stundenlohn vertauscht"), ("(35 + 42)x = 245", "die Anfahrt mit der Stundenzahl malgenommen"), ("35 + 42 + x = 245", "x einfach dazugezählt")],
    "Die Anfahrt zahlst du einmal. Der Stundenlohn gilt für jede Stunde.",
    "Anfahrt 35 € plus x Stunden zu 42 €: 35 + 42x = 245. Daraus folgt 42x = 210 und x = 5 Stunden.",
    lambda: ist_loesung("35+42*x", "245", 5) and not ist_loesung("35*x+42", "245", 5) and not ist_loesung("(35+42)*x", "245", 5) and not ist_loesung("35+42+x", "245", 5)), regel="id.algebra.gleichung_loesen")
neu(T, "sach", "anwenden", Z(
    "Eine Kerze ist 30 cm hoch und brennt 2 cm in jeder Stunde ab. Eine zweite Kerze ist 24 cm hoch und brennt 1 cm in jeder Stunde ab. Beide werden gleichzeitig angezündet. Nach wie vielen Stunden sind beide Kerzen gleich hoch?",
    6, "(30 - 24) / (2 - 1)", 6, "Stelle für jede Kerze einen Term mit der Stundenzahl x auf. Beide Höhen sollen gleich sein.",
    "Kerze 1: 30 − 2x. Kerze 2: 24 − x. Gleichsetzen: 30 − 2x = 24 − x, also 6 = x. Nach 6 Stunden sind beide 18 cm hoch.",
    [(54, "fb.waage.zeichen_nicht_gedreht", "30 + 24 gerechnet"), (3, None, "30 − 24 durch 2 geteilt")], "Stunden"), g="einkleidung", regel="id.algebra.gleichung_loesen")
