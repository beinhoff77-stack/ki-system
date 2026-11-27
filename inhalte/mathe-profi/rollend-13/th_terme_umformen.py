T = "terme.umformen"
# ───────── zusammenfassen ─────────
_tab = [(1, 6), (2, 11), (3, 16), (4, 21)]
neu(T, "zusammenfassen", "bruecke", W(
    "Die Tabelle zeigt, welche Werte ein Term T(x) für die Zahlen x = 1, 2, 3 und 4 annimmt. Welcher der drei Terme hat für alle vier Zahlen diese Werte?",
    "3x + 2 + 2x − 1",
    [("3x + 2 − 2x + 1", "dieser Term lässt sich zu x + 3 zusammenfassen; für x = 1 ergibt er 4 statt 6"),
     ("3x + 2 + 2x + 1", "dieser Term lässt sich zu 5x + 3 zusammenfassen; für x = 1 ergibt er 8 statt 6")],
    "Fasse jeden Term zusammen oder setze x = 1 ein und vergleiche mit der ersten Spalte.",
    "3x + 2 + 2x − 1 = 5x + 1. Für x = 1, 2, 3, 4 ergibt das 6, 11, 16, 21. Das passt zur Tabelle. Die anderen Terme sind zu x + 3 und 5x + 3 zusammenfassbar und haben schon bei x = 1 einen anderen Wert.",
    lambda: all(wert_an("3*x+2+2*x-1", k) == v for k, v in _tab) and not all(wert_an("3*x+2-2*x+1", k) == v for k, v in _tab) and not all(wert_an("3*x+2+2*x+1", k) == v for k, v in _tab)
    and gl("3*x+2+2*x-1", "5*x+1") and gl("3*x+2-2*x+1", "x+3") and gl("3*x+2+2*x+1", "5*x+3"),
    grafik=TAB(["x", "1", "2", "3", "4"], ["T(x)", "6", "11", "16", "21"])), g="darstellung", regel="rr.tauschen")
neu(T, "zusammenfassen", "umkehren", Z(
    "Für welche Zahl k gilt 7x + 3 − kx + 2x − 8 = 4x − 5 für alle Zahlen x?",
    5, "7 + 2 - 4", "9 - 4", "Fasse links zuerst die x-Glieder und die Zahlen getrennt zusammen. Links und rechts muss bei x dieselbe Zahl stehen.",
    "Links: 7x + 2x − kx = (9 − k)x und 3 − 8 = −5. Es muss 9 − k = 4 gelten, also k = 5. Probe: 7x + 3 − 5x + 2x − 8 = 4x − 5.",
    [(13, None, "alle Zahlen vor x addiert: 7 + 2 + 4", "7 + 2 + 4"), (-5, None, "die Differenz in der falschen Richtung gebildet: 4 − 9", "4 - 9"), (3, None, "das Glied 2x vergessen: 7 − 4", "7 - 4")]), g="rueckwaerts", regel="rr.tauschen")
assert gl("7*x+3-5*x+2*x-8", "4*x-5")

# ───────── produkte ─────────
neu(T, "produkte", "anwenden", Z(
    "Aus einem Tank fließt Wasser ab. Pro Minute ändert sich die Füllmenge um (−4a) Liter. Das Ventil bleibt 3b Minuten offen. Dabei ist a = 5 und b = 2. Eine Abnahme zählt als negative Zahl. Um wie viele Liter ändert sich die Füllmenge insgesamt?",
    -120, "(-4 * 5) * (3 * 2)", "-4 * 3 * 5 * 2", "Die gesamte Änderung ist die Änderung pro Minute mal die Zahl der Minuten. Vereinfache zuerst (−4a)·(3b).",
    "(−4a)·(3b) = −12ab. Für a = 5 und b = 2 ist das −12 · 5 · 2 = −120. Die Füllmenge nimmt um 120 Liter ab.",
    [(120, "fb.vorzeichen.falsches_zeichen", "das Minus vergessen: 4 · 5 · 3 · 2", "4 * 5 * 3 * 2"), (-14, None, "addiert statt malgenommen: −4 · 5 + 3 · 2", "-4 * 5 + 3 * 2"), (-60, None, "das b nicht eingesetzt: der Faktor 3 statt 3b", "(-4 * 5) * 3")], "Liter"), g="einkleidung", regel="rr.vorzeichen")
neu(T, "produkte", "fehler_detektiv", FD(
    "Kim vereinfacht (−2a²) · (−3a) · (5b).",
    [("Ordnen: (−2a²) · (−3a) · (5b) = (−2) · (−3) · 5 · a² · a · b", gl("(-2*a**2)*(-3*a)*(5*b)", "(-2)*(-3)*5*a**2*a*b"), True),
     ("Zahlen: (−2) · (−3) · 5 = −30. Potenzen: a² · a = a³.", (-2) * (-3) * 5 == -30 and gl("a**2*a", "a**3"), True),
     ("Ergebnis: −30a³b", gl("-30*a**3*b", "-30*a**3*b"), True)],
    "Welches Vorzeichen hat (−2) · (−3)?",
    "Zwei negative Faktoren ergeben ein positives Produkt: (−2) · (−3) = 6 und 6 · 5 = 30. Richtig ist 30a³b. Zeile 3 übernimmt nur das Ergebnis der Zeile 2."), regel="rr.vorzeichen")
# ───────── minusklammer ─────────
neu(T, "minusklammer", "anwenden", Z(
    "Ein Wasserbecken enthält (6x + 40) Liter. Dann werden (2x − 15) Liter entnommen. Wie viele Liter bleiben im Becken, wenn x = 10 ist?",
    95, "(6 * 10 + 40) - (2 * 10 - 15)", "4 * 10 + 55", "Du ziehst die ganze entnommene Menge ab. Setze sie in eine Klammer, bevor du das Minus anwendest.",
    "(6x + 40) − (2x − 15) = 6x + 40 − 2x + 15 = 4x + 55. Für x = 10: 40 + 55 = 95 Liter. Probe: 100 − 5 = 95.",
    [(65, "fb.minusklammer.nur_erstes_zeichen", "nur das erste Zeichen der Klammer umgedreht: aus −(2x − 15) wird −2x − 15", "4 * 10 + 25"), (105, None, "das Minus vor der Klammer ignoriert: aus −(2x − 15) wird +2x − 15", "8 * 10 + 25"), (40, None, "nur die x-Glieder berechnet, die Zahlen 40 und 15 vergessen", "6 * 10 - 2 * 10")], "Liter"), g="einkleidung", regel="rr.minusklammer")
assert gl("(6*x+40)-(2*x-15)", "4*x+55")
neu(T, "minusklammer", "umkehren", Z(
    "Für welche Zahl b gilt 5x − (2x + b) − (x − 3) = 2x − 1 für alle Zahlen x?",
    4, "3 - (-1)", 4, "Löse beide Klammern auf. Sammle dann die x-Glieder und die Zahlen getrennt. Die Zahlen links müssen −1 ergeben.",
    "5x − 2x − b − x + 3 = 2x + (3 − b). Es muss 3 − b = −1 gelten, also b = 4. Probe: 5x − (2x + 4) − (x − 3) = 2x − 1.",
    [(2, None, "−1 + 3 gerechnet statt 3 − (−1)", "-1 + 3"), (-4, None, "−1 − 3 gerechnet", "-1 - 3"), (-2, "fb.minusklammer.nur_erstes_zeichen", "bei der zweiten Klammer nur das erste Zeichen gedreht (−x − 3): −b − 3 = −1", "-(-1 + 3)")]), g="rueckwaerts", regel="rr.minusklammer")
assert gl("5*x-(2*x+4)-(x-3)", "2*x-1")
# ───────── ausmultiplizieren ─────────
neu(T, "ausmultiplizieren", "zwei_wege", Z(
    "In einem Saal stehen 17 Reihen mit je 24 Stühlen. Berechne die Zahl der Stühle im Kopf mit dem Verteilungsgesetz auf zwei Wegen. Weg A: 17 · (20 + 4). Weg B: (10 + 7) · 24. Wie viele Stühle sind es?",
    408, "17 * (20 + 4)", "(10 + 7) * 24", "Beide Wege müssen dasselbe Ergebnis haben. Jeder Summand in der Klammer wird mit dem anderen Faktor malgenommen.",
    "Weg A: 17 · 20 + 17 · 4 = 340 + 68 = 408. Weg B: 10 · 24 + 7 · 24 = 240 + 168 = 408. Beide Wege führen auf 408 Stühle.",
    [(344, "fb.ausmultiplizieren.nur_erster_summand", "Weg A: nur die 20 mit 17 malgenommen, die 4 nur addiert", "17 * 20 + 4"), (178, None, "Weg B: nur die 7 mit 24 malgenommen, die 10 nur addiert", "10 + 7 * 24"), (68, None, "nur den zweiten Summanden berücksichtigt: 17 · 4", "17 * 4")], "Stühle"), g="mehrschritt", regel="rr.ausmultiplizieren")
neu(T, "ausmultiplizieren", "fehler_detektiv", FD(
    "Kim löst die Klammer auf und fasst zusammen: −2x(3x − 4) + 5x.",
    [("−2x(3x − 4) = −6x² − 8x", gl("-2*x*(3*x-4)", "-6*x**2-8*x"), True),
     ("Dazu 5x: −6x² − 8x + 5x = −6x² − 3x", gl("-6*x**2-8*x+5*x", "-6*x**2-3*x"), True),
     ("Ergebnis: −6x² − 3x", True, True)],
    "Rechne −2x · (−4) einzeln. Welches Vorzeichen hat das Ergebnis?",
    "−2x · (−4) = +8x, nicht −8x. Richtig: −2x(3x − 4) = −6x² + 8x. Dann −6x² + 8x + 5x = −6x² + 13x. Die Zeilen 2 und 3 folgen richtig aus dem Fehler der Zeile 1."), regel="rr.ausmultiplizieren")
# ───────── aequivalenz ─────────
neu(T, "aequivalenz", "anwenden", Z(
    "Für ein Fest kauft ein Verein n Brezeln zu je 2 € und n Getränke zu je 1 €. Dazu kommt ein Plakat für 8 €. Der Gesamtpreis in Euro ist 3n + 8. Ein Helfer schreibt ihn auf drei andere Arten auf: (1) 2(n + 4) + n, (2) 3(n + 8), (3) 8 + 2n + n. Wie viele dieser drei Terme geben für jede Zahl n denselben Preis wie 3n + 8?",
    2, "2", 2, "Fasse jeden Term zusammen. Oder setze n = 0 und n = 1 ein.",
    "(1) 2n + 8 + n = 3n + 8. Gleich. (2) 3n + 24. Nicht gleich, schon bei n = 0 ist es 24 statt 8. (3) 8 + 3n. Gleich. Es sind 2 Terme.",
    [(3, None, "alle drei Terme für gleich gehalten, ohne (2) auszumultiplizieren", lambda: 3 == len(["2*(n+4)+n", "3*(n+8)", "8+2*n+n"])),
     (1, None, "nur den Term mit gleicher Reihenfolge der Glieder erkannt, (1) wegen der Klammer verworfen", lambda: gl("2*(n+4)+n", "3*n+8") and not gl("3*(n+8)", "3*n+8"))]), g="einkleidung", regel="id.algebra.term")
assert sum(gl(t, "3*n+8") for t in ["2*(n+4)+n", "3*(n+8)", "8+2*n+n"]) == 2
neu(T, "aequivalenz", "fehler_detektiv", FD(
    "Kim prüft, ob die Terme x² + 2 und 3x für alle Zahlen x denselben Wert haben.",
    [("x = 1: 1² + 2 = 3 und 3 · 1 = 3. Die Werte sind gleich.", 1 ** 2 + 2 == 3 * 1, True),
     ("x = 2: 2² + 2 = 6 und 3 · 2 = 6. Die Werte sind gleich.", 2 ** 2 + 2 == 3 * 2, True),
     ("Zwei Beispiele stimmen, also haben die Terme für alle Zahlen x denselben Wert.", gl("x**2+2", "3*x"), True)],
    "Probiere auch x = 3 und x = 0 aus.",
    "Für x = 3 ist x² + 2 = 11, aber 3x = 9. Die Terme sind nicht gleichwertig. Passende Beispiele beweisen nichts; ein einziges Gegenbeispiel genügt zum Widerlegen."), regel="id.algebra.term")
