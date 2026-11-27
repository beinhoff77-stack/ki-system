T = "gleichungen.quadratisch"
GL = "id.algebra.gleichung_loesen"
NP = "rr.nullprodukt"
HG = "id.algebra.hoeherer_grad"
# ───────── reinquadratisch ─────────
neu(T, "reinquadratisch", "lueckenweg", L(
    "Löse 3x² − 48 = 0 über ℝ. Zuerst wird x² allein gestellt: x² = ①. Die positive Lösung ist ②. Dann ist die negative Lösung ③. Also liegen die beiden Lösungen ④ Einheiten auseinander.",
    KOMM(4), [16, 4, -4, 8], ["48 // 3", "4", "-{2}", "{2} - {3}"], ["48 / 3", "wz(48 / 3)", "-wz(48 / 3)", "2 * wz(48 / 3)"],
    "Bringe 48 auf die andere Seite und teile durch die Zahl vor x². Danach gibt es zwei Zahlen, die quadriert dasselbe ergeben.",
    "3x² = 48 gibt x² = 16. Die Lösungen sind x = 4 und x = −4. Ihr Abstand ist 4 − (−4) = 8. Probe: 3 · 16 − 48 = 0.",
    {0: [(45, None, "3 abgezogen statt geteilt: 48 − 3", "48 - 3"), (144, None, "mit 3 malgenommen statt geteilt: 48 · 3", "48 * 3")], 2: [(4, "fb.gegenrechnung.zweite_loesung_fehlt", "nur die positive Lösung eingetragen", "{2}")], 3: [(0, None, "beide Lösungen addiert: 4 + (−4)", "{2} + {3}")]}), regel=GL)
neu(T, "reinquadratisch", "bruecke", W(
    "Die Zeichnung zeigt die Parabel y = x² − 9. Welche Gleichung gehört zu ihren Schnittpunkten mit der x-Achse, und welche Lösungen hat sie?",
    "x² − 9 = 0 mit x = 3 und x = −3", [("x² − 9 = 0 mit x = 9 und x = −9", "die Zahl 9 statt ihrer Wurzel als Lösung genommen"), ("x² + 9 = 0 mit x = 3 und x = −3", "das Vorzeichen in der Gleichung verändert: dort gibt es keine Lösung"), ("x² − 9 = 0 mit x = 3", "die zweite Lösung vergessen")],
    "Auf der x-Achse ist y = 0. Setze das in die Gleichung der Parabel ein und vergleiche mit dem Bild.",
    "Auf der x-Achse gilt y = 0, also x² − 9 = 0 und x² = 9. Die Lösungen sind 3 und −3. Im Bild schneidet die Parabel die x-Achse genau bei −3 und 3.",
    lambda: all(x * x - 9 == 0 for x in (3, -3)) and not any(x * x - 9 == 0 for x in (9, -9)) and not any(x * x + 9 == 0 for x in range(-10, 11)),
    grafik=KO([-5, 5], [-10, 8], graphen=[{"art": "poly", "k": [-9, 0, 1], "name": "y = x² − 9"}])), g="darstellung", regel=GL)
neu(T, "reinquadratisch", "umkehren", Z(
    "Die Gleichung 2x² − c = 0 hat die beiden Lösungen x = 6 und x = −6. Wie groß ist c?",
    72, "2 * 6 ** 2", lambda: next(c for c in range(1, 500) if all(2 * x * x - c == 0 for x in (6, -6))),
    "Setze eine der Lösungen in die Gleichung ein und löse nach c.",
    "Mit x = 6 gilt 2 · 6² − c = 0, also c = 2 · 36 = 72. Probe: 2x² = 72 gibt x² = 36 und x = 6 oder x = −6.",
    [(36, None, "den Faktor 2 vergessen: 6²", "6 ** 2"), (12, None, "2 mit 6 malgenommen statt 6 zu quadrieren: 2 · 6", "2 * 6"), (144, None, "erst 2 mit 6 malgenommen und dann das Ergebnis quadriert", "(2 * 6) ** 2")]), g="rueckwaerts", regel=GL)

# ───────── ausklammern ─────────
neu(T, "ausklammern", "lueckenweg", L(
    "Löse 2x² + 12x = 0 über ℝ. Ausklammern gibt 2x · (x + ①) = 0. Die Lösungen sind x = 0 und x = ②. Also liegt die Mitte zwischen den beiden Lösungen bei x = ③.",
    KOMM(3), [6, -6, -3], ["12 // 2", "-{1}", "{2} // 2"], ["12 / 2", "-12 / 2", "-12 / 2 / 2"],
    "Beide Summanden enthalten den Faktor 2x. Ein Produkt ist 0, wenn einer der Faktoren 0 ist.",
    "2x² + 12x = 2x · (x + 6). Ein Faktor 2x = 0 gibt x = 0, der andere x + 6 = 0 gibt x = −6. Die Mitte von 0 und −6 ist −3.",
    {0: [(24, None, "12 mit 2 malgenommen: 12 · 2", "12 * 2")], 1: [(6, "fb.nullprodukt.vorzeichen_der_loesung", "das Vorzeichen der Lösung vergessen", "{1}")], 2: [(-6, None, "die Lösung statt der Mitte angegeben", "{2}")]}), regel=NP)
neu(T, "ausklammern", "zwei_wege", Z(
    "Löse x² = 6x über ℝ auf zwei Wegen. Weg A: Zeichne die Graphen von y = x² und y = 6x (oder lege eine Wertetabelle an) und zähle die Schnittstellen. Weg B: Bringe alles auf eine Seite und klammere x aus. Wie viele Lösungen hat die Gleichung?",
    2, "1 + 1", lambda: len([x for x in range(-50, 50) if x * x == 6 * x]),
    "Beide Wege müssen dieselbe Anzahl ergeben.",
    "Weg B: x² − 6x = 0 gibt x · (x − 6) = 0, also x = 0 oder x = 6. Weg A: Die Parabel und die Gerade schneiden sich bei x = 0 und bei x = 6. Es gibt 2 Lösungen.",
    [(1, "fb.hoeherer_grad.durch_x_geteilt", "durch x geteilt und dabei die Lösung x = 0 verloren", "1"), (3, None, "x = −6 als dritte Lösung dazugezählt, weil x² = 36 zwei Lösungen hat", "3")]), regel=HG)
neu(T, "ausklammern", "fehler_detektiv", FD(
    "Kim löst x² − 9x = 0 über ℝ.",
    [("Umstellen: x² = 9x", all((x * x - 9 * x == 0) == (x * x == 9 * x) for x in range(-3, 12)), None),
     ("Beide Seiten durch x teilen: x = 9", all((x * x == 9 * x) == (x == 9) for x in range(-3, 12)), None),
     ("Also ist L = {9}.", False, True)],
    "Prüfe, ob x = 0 die Gleichung erfüllt. Darf man einfach durch x teilen?",
    "Zeile 1 stimmt. In Zeile 2 wird durch x geteilt. Das geht nur für x ≠ 0, und so geht die Lösung x = 0 verloren. Richtig: x · (x − 9) = 0 gibt x = 0 oder x = 9. Zeile 3 folgt aus Zeile 2."), regel=HG)

# ───────── faktorisieren ─────────
neu(T, "faktorisieren", "lueckenweg", L(
    "Löse x² − 11x + 24 = 0 durch Faktorisieren. Gesucht sind zwei Zahlen mit der Summe 11 und dem Produkt 24. Die kleinere Zahl ist ①. Die größere Zahl ist ②. Dann gilt x² − 11x + 24 = (x − ①)(x − ②), und die beiden Lösungen liegen ③ Einheiten auseinander.",
    KOMM(3), [3, 8, 5], ["3", "8", "{2} - {1}"], [lambda: next(a for a in range(1, 25) if a * (11 - a) == 24 and a < 11 - a), lambda: next(11 - a for a in range(1, 25) if a * (11 - a) == 24 and a < 11 - a), lambda: 8 - 3],
    "Probiere Zahlenpaare mit dem Produkt 24 und prüfe, welches die Summe 11 hat.",
    "3 · 8 = 24 und 3 + 8 = 11. Also x² − 11x + 24 = (x − 3)(x − 8). Die Lösungen sind 3 und 8. Sie liegen 8 − 3 = 5 Einheiten auseinander.",
    {0: [(4, None, "ein Paar mit dem Produkt 24 gewählt, ohne die Summe zu prüfen (die Zahlen 4 und 6)", "4")], 1: [(6, None, "dazu passend 24 : 4", "24 / 4")], 2: [(2, None, "mit dem falschen Paar gerechnet: 6 − 4", "6 - 4")]}), regel=NP)
neu(T, "faktorisieren", "umkehren", Z(
    "Die Gleichung x² + px + q = 0 hat die Lösungen x = 2 und x = 7. Wie groß ist p?",
    -9, "-(2 + 7)", lambda: -(2 + 7),
    "Schreibe zuerst die Gleichung in der Form (x − 2)(x − 7) = 0 und multipliziere aus.",
    "(x − 2)(x − 7) = x² − 9x + 14. Also ist p = −9 und q = 14. Probe: 4 − 18 + 14 = 0 und 49 − 63 + 14 = 0.",
    [(9, "fb.vorzeichen.falsches_zeichen", "das Vorzeichen vergessen: 2 + 7", "2 + 7"), (14, None, "das Produkt statt der Summe genommen: 2 · 7", "2 * 7"), (5, None, "die Zahlen voneinander abgezogen: 7 − 2", "7 - 2")]), g="umkehr", regel=NP)
neu(T, "faktorisieren", "fehler_detektiv", FD(
    "Kim löst x² + 2x − 15 = 0 durch Faktorisieren.",
    [("Gesucht sind zwei Zahlen mit der Summe 2 und dem Produkt −15.", True, None),
     ("Das passt für 5 und −3.", 5 + (-3) == 2 and 5 * (-3) == -15, None),
     ("Also gilt x² + 2x − 15 = (x + 5)(x − 3).", all((x + 5) * (x - 3) == x * x + 2 * x - 15 for x in range(-5, 6)), None),
     ("Also sind die Lösungen x = 5 und x = −3.", False, None)],
    "Setze x = 5 in die Gleichung x² + 2x − 15 = 0 ein.",
    "Die Zeilen 1 bis 3 stimmen. In Zeile 4 stehen die falschen Vorzeichen: (x + 5)(x − 3) = 0 ist null für x = −5 oder x = 3. Probe: 25 − 10 − 15 = 0 und 9 + 6 − 15 = 0."), regel=NP)

# ───────── ergaenzung ─────────
neu(T, "ergaenzung", "lueckenweg", L(
    "Löse x² + 6x − 7 = 0 mit quadratischer Ergänzung. Auf beiden Seiten wird ① addiert, damit links ein Quadrat entsteht. Dann gilt (x + ②)² = ③.",
    KOMM(3), [9, 3, 16], ["(6 // 2) ** 2", "6 // 2", "7 + {1}"], ["(6 / 2) ** 2", "6 / 2", "7 + (6 / 2) ** 2"],
    "Halbiere die Zahl vor x und quadriere das Ergebnis.",
    "x² + 6x + 9 = 7 + 9, links steht (x + 3)², rechts 16. Weiter: x + 3 = 4 oder x + 3 = −4, also x = 1 oder x = −7.",
    {0: [(36, None, "6 nur quadriert statt halbiert und quadriert: 6²", "6 ** 2"), (3, None, "nur halbiert: 6 : 2", "6 // 2")], 2: [(-2, None, "9 abgezogen statt addiert: 7 − 9", "7 - {1}")]}), regel=GL)
neu(T, "ergaenzung", "zwei_wege", Z(
    "Löse x² − 4x − 12 = 0 über ℝ auf zwei Wegen. Weg A: quadratische Ergänzung. Weg B: Faktorisieren mit Summe und Produkt. Wie groß ist die größere Lösung?",
    6, "2 + 4", lambda: max(x for x in range(-50, 50) if x * x - 4 * x - 12 == 0),
    "Beide Wege müssen dieselben Lösungen ergeben.",
    "Weg A: (x − 2)² = 16, also x − 2 = 4 oder x − 2 = −4, x = 6 oder x = −2. Weg B: (x − 6)(x + 2) = 0 mit denselben Lösungen. Die größere ist 6.",
    [(-2, None, "die kleinere Lösung angegeben", "2 - 4"), (8, None, "2 durch 4 ersetzt: 4 + 4", "4 + 4"), (16, None, "die rechte Seite (x − 2)² = 16 als Lösung genommen", "16")]), regel=GL)
neu(T, "ergaenzung", "umkehren", Z(
    "Für welche Zahl q hat die Gleichung x² + 10x + q = 0 genau eine Lösung?",
    25, "(10 // 2) ** 2", lambda: next(q for q in range(0, 200) if 10 * 10 - 4 * q == 0),
    "Genau eine Lösung gibt es, wenn sich links ein vollständiges Quadrat (x + a)² bilden lässt.",
    "(x + 5)² = x² + 10x + 25. Dann ist die Gleichung (x + 5)² = 0 und hat nur die Lösung x = −5. Also q = 25.",
    [(5, None, "nur halbiert: 10 : 2", "10 // 2"), (100, None, "10 nur quadriert: 10²", "10 ** 2"), (50, None, "10 mit 5 malgenommen", "10 * 5")]), g="parameter", regel=GL)

# ───────── loesungsformel ─────────
neu(T, "loesungsformel", "lueckenweg", L(
    "Löse 2x² − 7x − 15 = 0 mit der Lösungsformel (a = 2, b = −7, c = −15). Die Diskriminante b² − 4ac ist ①. Die Wurzel aus der Diskriminante ist ②. Dann ist die größere Lösung x = (7 + ②) geteilt durch 2a gleich ③.",
    KOMM(3), [169, 13, 5], ["(-7) ** 2 - 4 * 2 * (-15)", "13", "(7 + {2}) // (2 * 2)"], ["49 + 120", "wz(49 + 120)", "(7 + wz(169)) / 4"],
    "Setze a, b und c vorsichtig ein. Bei c = −15 wird aus −4ac eine Plus-Rechnung.",
    "D = (−7)² − 4 · 2 · (−15) = 49 + 120 = 169. √169 = 13. Größere Lösung: (7 + 13) : 4 = 5. Die andere Lösung ist (7 − 13) : 4 = −1,5.",
    {0: [(-71, "fb.vorzeichen.falsches_zeichen", "−4ac mit falschem Vorzeichen: 49 − 120", "49 - 120")], 1: [(84.5, "fb.hoch_zurueck.wurzel_halbiert", "169 halbiert statt die Wurzel gezogen", "{1} / 2")], 2: [(10, None, "durch 2 statt durch 2a geteilt: (7 + 13) : 2", "(7 + {2}) // 2")]}), regel=GL)
neu(T, "loesungsformel", "zwei_wege", Z(
    "Löse 2x² − 4x − 6 = 0 über ℝ auf zwei Wegen. Weg A: Lösungsformel direkt. Weg B: Erst beide Seiten durch 2 teilen, dann mit Summe und Produkt faktorisieren. Wie groß ist die größere Lösung?",
    3, "(4 + 8) / 4", lambda: max(x for x in range(-20, 20) if 2 * x * x - 4 * x - 6 == 0),
    "Beide Wege müssen dieselben Lösungen ergeben.",
    "Weg A: D = 16 + 48 = 64, x = (4 ± 8) : 4 gibt 3 oder −1. Weg B: x² − 2x − 3 = 0, (x − 3)(x + 1) = 0, also 3 oder −1. Die größere Lösung ist 3.",
    [(-1, None, "die kleinere Lösung angegeben", "(4 - 8) / 4"), (6, None, "durch 2 statt durch 2a geteilt: (4 + 8) : 2", "(4 + 8) / 2"), (12, None, "gar nicht geteilt: 4 + 8", "4 + 8")]), regel=GL)
neu(T, "loesungsformel", "fehler_detektiv", FD(
    "Kim löst x² + 4x − 5 = 0 mit der Lösungsformel.",
    [("Es ist a = 1, b = 4 und c = 5.", False, None),
     ("Dann ist b² − 4ac = 16 − 20 = −4.", False, 4 ** 2 - 4 * 1 * 5 == -4),
     ("Wegen −4 < 0 hat die Gleichung keine Lösung.", False, -4 < 0)],
    "Lies c in der Gleichung x² + 4x − 5 = 0 noch einmal genau ab. Probiere x = 1.",
    "Zeile 1 enthält den Fehler: c = −5, nicht 5. Die Zeilen 2 und 3 folgen aus Zeile 1 richtig. Richtig ist D = 16 + 20 = 36 und die Lösungen sind x = 1 und x = −5. Probe: 1 + 4 − 5 = 0."), regel=GL)

# ───────── bruchgleichung ─────────
neu(T, "bruchgleichung", "lueckenweg", L(
    "Löse x − 20/x = 1 (x ≠ 0). Multiplikation mit x gibt x² − 20 = x, sortiert x² − x − 20 = 0. Die Diskriminante ist ①. Die größere Lösung ist ②. Dann ist die kleinere Lösung ③.",
    KOMM(3), [81, 5, -4], ["1 + 4 * 20", "5", "1 - {2}"], ["1 + 80", "(1 + wz(81)) / 2", "(1 - wz(81)) / 2"],
    "Die Diskriminante ist b² minus das Vierfache von a mal c, hier mit a = 1, b = −1, c = −20. Die beiden Lösungen haben zusammen den Wert −b.",
    "D = 1 + 80 = 81 und √81 = 9. Lösungen: (1 + 9) : 2 = 5 und (1 − 9) : 2 = −4. Beide sind ungleich 0. Probe: 5 − 20/5 = 1 und −4 − 20/(−4) = −4 + 5 = 1.",
    {0: [(-79, "fb.vorzeichen.falsches_zeichen", "−4ac mit falschem Vorzeichen: 1 − 80", "1 - 80")], 1: [(10, None, "nicht durch 2 geteilt: 1 + 9", "1 + 9")], 2: [(4, "fb.vorzeichen.falsches_zeichen", "das Minus der kleineren Lösung vergessen", "4")]}), regel=GL)
neu(T, "bruchgleichung", "bruecke", W(
    "Die Zeichnung zeigt die Graphen von y = 6/x und y = x − 1. Welche Gleichung gehört zu den Schnittpunkten, und welche Lösungen hat sie?",
    "6/x = x − 1 mit x = 3 und x = −2", [("6/x = x − 1 mit x = 2 und x = −3", "die Vorzeichen der Lösungen vertauscht"), ("6/x = x + 1 mit x = 2 und x = −3", "die Gerade falsch abgelesen"), ("6x = x − 1 mit x = −0,2", "den Bruch durch ein Produkt ersetzt")],
    "Schnittpunkte haben auf beiden Graphen denselben y-Wert. Prüfe die Lösungen im Bild.",
    "An den Schnittstellen gilt 6/x = x − 1. Multipliziert mit x: x² − x − 6 = 0, also x = 3 oder x = −2. Im Bild: Bei x = 3 sind beide y-Werte 2, bei x = −2 beide −3.",
    lambda: all(6 / x == x - 1 for x in (3, -2)) and not any(6 / x == x - 1 for x in (2, -3)) and all(6 / x == x + 1 for x in (2, -3)) and not any(6 / x == x - 1 for x in (2, -3)),
    grafik=KO([-6, 6], [-6, 6], graphen=[{"art": "hyperbel", "a": 6, "b": 0, "c": 0, "name": "y = 6/x"}, {"art": "linear", "m": 1, "t": -1, "name": "y = x − 1"}])), g="darstellung", regel=GL)
neu(T, "bruchgleichung", "anwenden", Z(
    "Zwei Pumpen füllen ein Becken zusammen in 2,4 Stunden. Die zweite Pumpe allein braucht 2 Stunden länger als die erste allein. Beide fördern gleichmäßig. Wie viele Stunden braucht die erste Pumpe allein?",
    4, "(2.8 + 5.2) / 2", lambda: next(x for x in (F(i, 10) for i in range(1, 200)) if 1 / x + 1 / (x + 2) == F(10, 24)),
    "Was schafft jede Pumpe in einer Stunde? Diese Anteile ergeben zusammen den Anteil je Stunde der beiden.",
    "Mit x Stunden gilt 1/x + 1/(x + 2) = 1/2,4. Mit 2,4 · x · (x + 2) multiplizieren: 2,4(x + 2) + 2,4x = x(x + 2), also x² − 2,8x − 4,8 = 0. D = 27,04 = 5,2². Lösungen x = 4 und x = −1,2. Die Zeit ist positiv, also 4 h. Probe: 1/4 + 1/6 = 5/12 = 1/2,4.",
    [(6, None, "die Zeit der zweiten Pumpe angegeben: 4 + 2", "4 + 2"), (-1.2, None, "die negative Lösung angegeben", "(2.8 - 5.2) / 2"), (8, None, "nicht durch 2 geteilt: 2,8 + 5,2", "2.8 + 5.2")], "h"), g="transfer", regel=GL)

# ───────── diskriminante ─────────
neu(T, "diskriminante", "verfahren_waehlen", W(
    "Du willst wissen, wie viele Lösungen 3x² − 5x + 4 = 0 über ℝ hat, ohne sie auszurechnen. Was tust du?",
    "Die Diskriminante b² − 4ac berechnen: 25 − 48 = −23. Sie ist negativ, also gibt es keine Lösung.",
    [("Prüfen, ob 3x² positiv ist. Dann gibt es immer zwei Lösungen.", "den Faktor vor x² mit der Anzahl der Lösungen verwechselt"), ("x = 0 einsetzen: Es kommt 4 heraus, also gibt es keine Lösung.", "ein einziger Einsetzwert sagt nichts über alle Lösungen"), ("a, b und c addieren: 3 − 5 + 4 = 2 ist positiv, also gibt es zwei Lösungen.", "eine Rechnung benutzt, die mit der Anzahl der Lösungen nichts zu tun hat")],
    "Das Vorzeichen eines bestimmten Terms aus a, b und c entscheidet über die Anzahl der Lösungen.",
    "Die Diskriminante D = b² − 4ac entscheidet: D > 0 gibt zwei Lösungen, D = 0 genau eine, D < 0 keine. Hier ist D = (−5)² − 4 · 3 · 4 = 25 − 48 = −23 < 0.",
    lambda: (-5) ** 2 - 4 * 3 * 4 < 0 and all(3 * x * x - 5 * x + 4 != 0 for x in range(-50, 50))), g="erkennen", regel=GL)
neu(T, "diskriminante", "umkehren", Z(
    "Für welche Zahl c hat die Gleichung 2x² − 12x + c = 0 genau eine Lösung?",
    18, "12 ** 2 / (4 * 2)", lambda: next(c for c in range(1, 200) if (-12) ** 2 - 4 * 2 * c == 0),
    "Genau eine Lösung gibt es, wenn die Diskriminante 0 ist. Setze a, b und c ein.",
    "D = (−12)² − 4 · 2 · c = 144 − 8c. D = 0 gibt c = 18. Probe: 2x² − 12x + 18 = 2(x − 3)² hat nur die Lösung x = 3.",
    [(36, None, "a vergessen: 12² : 4", "12 ** 2 / 4"), (72, None, "durch 2 statt durch 8 geteilt: 12² : 2", "12 ** 2 / 2"), (6, None, "nur 12 : 2 gerechnet", "12 / 2")]), g="umkehr", regel=GL)
neu(T, "diskriminante", "umkehren", Z(
    "Die Gleichung x² + kx + 9 = 0 soll über ℝ keine Lösung haben. Für wie viele ganze Zahlen k ist das der Fall?",
    11, "2 * 5 + 1", lambda: sum(1 for k in range(-50, 50) if k * k - 36 < 0),
    "Keine Lösung heißt: Die Diskriminante ist negativ. Stelle eine Ungleichung für k auf.",
    "D = k² − 36 < 0 gilt für −6 < k < 6. Die ganzen Zahlen sind −5, −4, …, 5. Das sind 11 Zahlen. Für k = 6 und k = −6 ist D = 0, dort gibt es eine Lösung.",
    [(5, None, "nur die positiven k gezählt", "5"), (13, None, "die Grenzfälle k = 6 und k = −6 mitgezählt, bei denen D = 0 ist", "2 * 6 + 1")]), g="parameter", regel=GL)

# ───────── sachaufgabe ─────────
neu(T, "sachaufgabe", "lueckenweg", L(
    "Ein Rechteck hat 26 m Umfang und 40 m² Fläche. Die Summe der beiden Seitenlängen ist ① m. Die kürzere Seite x erfüllt x · (① − x) = 40. Sie ist ② m lang. Dann ist die längere Seite ③ m lang.",
    KOMM(3), [13, 5, 8], ["26 // 2", "5", "{1} - {2}"], ["26 / 2", lambda: next(x for x in range(1, 13) if x * (13 - x) == 40 and x < 13 - x), lambda: 13 - next(x for x in range(1, 13) if x * (13 - x) == 40 and x < 13 - x)],
    "Der Umfang besteht aus zwei Längen und zwei Breiten. Probiere für die kürzere Seite ganze Zahlen.",
    "Halber Umfang: 26 : 2 = 13. Aus x · (13 − x) = 40 folgt x² − 13x + 40 = 0 mit den Lösungen 5 und 8. Die kürzere Seite ist 5 m, die längere 13 − 5 = 8 m. Probe: 5 · 8 = 40.",
    {0: [(26, None, "den Umfang statt der Summe der beiden Seiten genommen", "26")], 1: [(8, None, "die längere statt der kürzeren Seite angegeben", "8")], 2: [(18, None, "die Seiten addiert statt abgezogen: 13 + 5", "{1} + {2}")]}), regel=GL)
neu(T, "sachaufgabe", "anwenden", Z(
    "Ein rechteckiger Garten ist 12 m lang und 8 m breit. Ringsum, innerhalb des Gartens, wird ein überall gleich breiter Weg angelegt. Der Rasen in der Mitte soll 32 m² groß bleiben. Wie breit ist der Weg?",
    2, "(10 - 6) / 2", lambda: next(x for x in (F(i, 2) for i in range(1, 12)) if (12 - 2 * x) * (8 - 2 * x) == 32 and 8 - 2 * x > 0),
    "Der Rasen ist ein Rechteck. Wie lang und breit ist es, wenn der Weg x Meter breit ist?",
    "Der Rasen ist (12 − 2x) m lang und (8 − 2x) m breit. (12 − 2x)(8 − 2x) = 32 gibt 96 − 40x + 4x² = 32, also x² − 10x + 16 = 0. Die Lösungen sind x = 2 und x = 8. Bei x = 8 wäre der Rasen negativ breit, also x = 2. Probe: 8 · 4 = 32.",
    [(8, None, "die zweite Lösung genommen: der Rasen wäre negativ breit", "(10 + 6) / 2"), (4, None, "die Wegbreite auf beiden Seiten zusammengezählt: 2 · 2", "2 * 2")], "m"), g="einkleidung", regel=GL)
neu(T, "sachaufgabe", "anwenden", Z(
    "Ein Ball wird von einer 15 m hohen Terrasse nach oben geworfen. Seine Höhe über dem Boden ist h = −5t² + 10t + 15 (h in Metern, t in Sekunden). Nach wie vielen Sekunden trifft der Ball den Boden?",
    3, "(2 + 4) / 2", lambda: next(t for t in range(1, 50) if -5 * t * t + 10 * t + 15 == 0),
    "Am Boden ist h = 0. Teile die Gleichung durch −5.",
    "−5t² + 10t + 15 = 0 gibt t² − 2t − 3 = 0, also (t − 3)(t + 1) = 0. Die Lösungen sind t = 3 und t = −1. Eine negative Zeit gibt es hier nicht, also t = 3 s. Probe: −45 + 30 + 15 = 0.",
    [(-1, None, "die negative Lösung angegeben", "(2 - 4) / 2"), (6, None, "nicht durch 2 geteilt: 2 + 4", "2 + 4"), (15, None, "die Starthöhe als Zeit angegeben", "15")], "s"), g="transfer", regel=GL)
