T = "gleichungen.bruch"
# ───────── definitionsmenge ─────────
neu(T, "definitionsmenge", "bruecke", Z(
    "Die Zeichnung zeigt den Graphen von y = 2/(x − 3). Für genau eine Zahl x gibt es auf dem Graphen keinen Punkt. Welche Zahl x darf in der Gleichung 2/(x − 3) = 1 nicht eingesetzt werden?",
    3, "0 + 3", 3, "Bei welcher Zahl x ist der Nenner 0? An dieser Stelle bricht der Graph ab.",
    "Der Nenner x − 3 ist 0 für x = 3. Dort ist der Term nicht definiert, der Graph hat an dieser Stelle eine Lücke. Die Definitionsmenge der Gleichung ist ℚ \\ {3}. (Die Gleichung selbst hat die Lösung x = 5: 2/2 = 1.)",
    [(-3, None, "x + 3 = 0 gelöst: das Vorzeichen der Nullstelle des Nenners verdreht", "-3"), (5, None, "die Lösung der Gleichung berechnet statt der verbotenen Zahl: 2 + 3", "2 + 3"), (1, None, "die rechte Seite der Gleichung als verbotene Zahl genommen", "1")],
    grafik={"typ": "koordinaten", "x": [-2, 8], "y": [-6, 6], "graphen": [{"art": "hyperbel", "a": 2, "b": -3, "c": 0, "name": "y = 2/(x − 3)"}]}), g="darstellung", regel="id.algebra.erlaubte_zahlen")
neu(T, "definitionsmenge", "fehler_detektiv", FD(
    "Kim bestimmt die Definitionsmenge der Gleichung 5/(x + 4) = 2/(x − 1) und stellt sie über Kreuz auf.",
    [("Nenner null setzen: x + 4 = 0 gibt x = 4, und x − 1 = 0 gibt x = 1.", [k for k in range(-9, 10) if k + 4 == 0] == [4] and [k for k in range(-9, 10) if k - 1 == 0] == [1], True),
     ("Also ist D = ℚ \\ {4; 1}.", True, True),
     ("Über Kreuz: 5(x − 1) = 2(x + 4).", wert_an("5/(x+4)", F(13, 3)) == wert_an("2/(x-1)", F(13, 3)) and ist_loesung("5*(x-1)", "2*(x+4)", F(13, 3)), True)],
    "Löse x + 4 = 0 einzeln. Welche Zahl ergibt 0, wenn du 4 addierst?",
    "x + 4 = 0 hat die Lösung x = −4, nicht 4. Richtig: D = ℚ \\ {−4; 1}. Zeile 2 übernimmt den Fehler der Zeile 1, Zeile 3 ist als Rechenschritt richtig."), regel="id.algebra.erlaubte_zahlen")
# ───────── ein_bruch ─────────
neu(T, "ein_bruch", "bruecke", W(
    "Wenn man 36 durch eine Zahl x teilt und zum Ergebnis 5 addiert, erhält man 14. Welche Gleichung gehört zu dieser Aussage (x ≠ 0)?",
    "36/x + 5 = 14",
    [("36/(x + 5) = 14", "die 5 schon im Nenner addiert: die Reihenfolge der Rechenschritte falsch übersetzt"), ("36/x = 14 + 5", "die 5 beim Umstellen mit dem falschen Vorzeichen auf die andere Seite gebracht")],
    "Was passiert zuerst mit der Zahl x, was danach? Setze zur Probe x = 4 ein.",
    "Erst wird 36 durch x geteilt: 36/x. Dann wird 5 addiert: 36/x + 5. Das Ergebnis ist 14. Mit x = 4 gilt 9 + 5 = 14. Die anderen Gleichungen stimmen für x = 4 nicht: 36/9 ist 4, und 36/4 = 9 ist nicht 19.",
    lambda: wert_an("36/x+5", 4) == 14 and wert_an("36/(x+5)", 4) != 14 and wert_an("36/x", 4) != 19), g="darstellung", regel="id.algebra.gleichung_loesen")
neu(T, "ein_bruch", "umkehren", Z(
    "Für welche Zahl a hat die Gleichung a/x + 2 = 5 die Lösung x = 4?",
    12, "(5 - 2) * 4", 12, "Setze x = 4 ein. Welchen Wert muss a/4 haben, damit zusammen mit 2 die Zahl 5 herauskommt?",
    "Mit x = 4: a/4 + 2 = 5. Dann a/4 = 3 und a = 12. Probe: 12/4 + 2 = 3 + 2 = 5.",
    [(3, None, "a/4 = 3 gefunden, aber a = 3 gesetzt", "5 - 2"), (28, None, "5 plus 2 statt 5 minus 2 gerechnet und mit 4 malgenommen", "(5 + 2) * 4"), (20, None, "die 2 vergessen: a/4 = 5", "5 * 4")]), g="rueckwaerts", regel="id.algebra.gleichung_loesen")
# ───────── ueber_kreuz ─────────
neu(T, "ueber_kreuz", "zwei_wege", Z(
    "Löse 3/(x + 2) = 5/(x + 6) auf zwei Wegen (x ≠ −2 und x ≠ −6). Weg A: über Kreuz multiplizieren. Weg B: auf beiden Seiten den Kehrwert bilden und dann beide Seiten mit 15 malnehmen. Welche Zahl ist die Lösung?",
    4, "(5 * 2 - 3 * 6) / (3 - 5)", "(18 - 10) / 2", "Beide Wege führen zu derselben Gleichung ohne Bruch. Mit dem Kehrwert wird aus 3/(x + 2) der Bruch (x + 2)/3.",
    "Weg A: 3(x + 6) = 5(x + 2), also 3x + 18 = 5x + 10 und 8 = 2x. Weg B: (x + 2)/3 = (x + 6)/5. Mal 15: 5(x + 2) = 3(x + 6). Das ist dieselbe Gleichung. x = 4. Probe: 3/6 = 5/10.",
    [(2, "fb.ausmultiplizieren.nur_erster_summand", "in beiden Produkten nur x malgenommen: aus 3(x + 6) wird 3x + 6 und aus 5(x + 2) wird 5x + 2", "(6 - 2) / (5 - 3)"), (-4, None, "beim Umstellen die Vorzeichen vertauscht: −8 durch 2", "-8 / 2"), (8, None, "nur 18 − 10 gerechnet und nicht durch 2 geteilt", "18 - 10")]), g="mehrschritt", regel="rr.waage")
assert ist_loesung("3*(x+6)", "5*(x+2)", 4) and F(3, 4 + 2) == F(5, 4 + 6)
neu(T, "ueber_kreuz", "anwenden", Z(
    "Läufer A läuft 6 km in t Minuten. Läuferin B läuft 9 km und braucht 30 Minuten länger als Läufer A. Beide laufen gleichmäßig und haben dieselbe Durchschnittsgeschwindigkeit. Wie viele Minuten braucht Läufer A für seine 6 km?",
    60, "30 * 6 / (9 - 6)", "180 // 3", "Die Geschwindigkeit ist Strecke durch Zeit. Beide Geschwindigkeiten sind gleich: 6/t und 9/(t + 30) sind gleich groß.",
    "Gleichung: 6/t = 9/(t + 30). Über Kreuz: 6(t + 30) = 9t, also 6t + 180 = 9t und t = 60. Läufer A braucht 60 Minuten, B 90 Minuten. Probe: 6 km in 60 min = 0,1 km/min und 9 km in 90 min = 0,1 km/min.",
    [(10, "fb.ausmultiplizieren.nur_erster_summand", "die 30 nicht mit 6 malgenommen: aus 6(t + 30) wird 6t + 30", "30 / 3"), (90, None, "die Zeit von B statt die von A angegeben", "30 * 6 / (9 - 6) + 30"), (-90, None, "die Strecken den falschen Zeiten zugeordnet: 9/t = 6/(t + 30)", "-270 / 3")], "Minuten"), g="transfer", regel="rr.verhaeltnis")
assert F(6, 60) == F(9, 90)
# ───────── hauptnenner ─────────
neu(T, "hauptnenner", "anwenden", Z(
    "Zwei Pumpen füllen zusammen ein Becken in 4 Stunden. Pumpe B braucht allein doppelt so lange wie Pumpe A allein. Beide pumpen gleichmäßig und stören sich nicht. Wie viele Stunden braucht Pumpe A allein?",
    6, "(4 + 2)", "12 // 2", "Pumpe A braucht x Stunden, Pumpe B 2x Stunden. In einer Stunde schafft A den Teil 1/x des Beckens und B den Teil 1/(2x). Zusammen schaffen sie in einer Stunde ein Viertel.",
    "Gleichung: 1/x + 1/(2x) = 1/4. Beide Seiten mit 4x malnehmen: 4 + 2 = x. Also x = 6. Pumpe A braucht 6 Stunden, Pumpe B 12 Stunden. Probe: 1/6 + 1/12 = 2/12 + 1/12 = 3/12 = 1/4.",
    [(8, None, "den zweiten Bruch falsch mit 4x multipliziert: 4 statt 2", "4 + 4"), (12, None, "die Zeit der langsameren Pumpe B angegeben", "(4 + 2) * 2"), (2, None, "die Gesamtzeit durch die Zahl der Pumpen geteilt", "4 / 2")], "Stunden"), g="einkleidung", regel="rr.bruchrechnen")
assert F(1, 6) + F(1, 12) == F(1, 4)
neu(T, "hauptnenner", "fehler_detektiv", FD(
    "Kim löst 2/x + 3/(2x) = 7/4 (x ≠ 0).",
    [("Hauptnenner 2x: 2/x = 4/(2x).", gl("2/x", "4/(2*x)"), True),
     ("Addieren: 4/(2x) + 3/(2x) = 7/(4x).", gl("4/(2*x)+3/(2*x)", "7/(4*x)"), True),
     ("Also gilt 7/(4x) = 7/4 und damit x = 1.", wert_an("7/(4*x)", 1) == F(7, 4), True)],
    "Wenn Brüche denselben Nenner haben: Was passiert mit dem Nenner beim Addieren?",
    "Beim Addieren gleichnamiger Brüche werden nur die Zähler addiert, der Nenner bleibt: 4/(2x) + 3/(2x) = 7/(2x). Dann ist 7/(2x) = 7/4 und x = 2. Zeile 3 rechnet mit dem falschen Ergebnis der Zeile 2 richtig weiter."), regel="rr.bruchrechnen")
# ───────── scheinloesung ─────────
neu(T, "scheinloesung", "bruecke", W(
    "Die Zeichnung zeigt die Graphen von y = x/(x − 2) und y = 2/(x − 2). Welche Aussage über die Gleichung x/(x − 2) = 2/(x − 2) stimmt?",
    "Die Gleichung hat keine Lösung: Die Graphen haben keinen gemeinsamen Punkt, und die Zahl 2 ist nur eine Scheinlösung.",
    [("Die Gleichung hat genau eine Lösung, nämlich x = 2, denn dort laufen beide Graphen zusammen.", "beim Umformen entsteht x = 2, aber für x = 2 ist der Nenner 0; dort gibt es keinen Punkt auf den Graphen"), ("Die Gleichung hat unendlich viele Lösungen, weil beide Brüche denselben Nenner haben.", "gleiche Nenner machen die Brüche nicht gleich: die Zähler x und 2 sind nur für x = 2 gleich")],
    "Haben die beiden Graphen einen gemeinsamen Punkt? Welche Zahl x ergibt sich beim Umformen, und darf man sie einsetzen?",
    "Mit (x − 2) multipliziert bleibt x = 2. Für x = 2 ist der Nenner 0, die Zahl gehört nicht zur Definitionsmenge. Die Graphen liegen immer 1 Einheit auseinander, denn x/(x − 2) = 1 + 2/(x − 2). Die Lösungsmenge ist leer.",
    lambda: all(wert_an("x/(x-2)", k) != wert_an("2/(x-2)", k) for k in range(-10, 11) if k != 2) and undef("x/(x-2)", 2) and gl("x/(x-2)", "1+2/(x-2)"),
    grafik={"typ": "koordinaten", "x": [-4, 8], "y": [-6, 8], "graphen": [{"art": "hyperbel", "a": 2, "b": -2, "c": 1, "name": "y = x/(x − 2)"}, {"art": "hyperbel", "a": 2, "b": -2, "c": 0, "name": "y = 2/(x − 2)"}]}), g="darstellung", regel="id.algebra.gleichung_loesen")
neu(T, "scheinloesung", "anwenden", W(
    "Pumpe A füllt ein Becken allein in 6 Stunden. Pumpe B füllt es allein in x Stunden. Es wird behauptet, beide zusammen brauchen 9 Stunden. Beide pumpen gleichmäßig. Aus der Gleichung 1/6 + 1/x = 1/9 ergibt sich x = −18. Was bedeutet das für die Behauptung?",
    "Die Behauptung kann nicht stimmen: Eine negative Zeit ist unmöglich, und zusammen müssten die Pumpen schneller sein als A allein.",
    [("Pumpe B braucht allein 18 Stunden.", "das Vorzeichen übersehen: x = −18 ist keine mögliche Zeit"), ("Pumpe B braucht allein 3 Stunden.", "9 − 6 gerechnet: die Zeiten wurden einfach abgezogen statt die Teilarbeiten zu addieren")],
    "Die Zeit von Pumpe B muss eine positive Zahl sein. Wie lange brauchen zwei Pumpen zusammen im Vergleich zu einer allein?",
    "1/x = 1/9 − 1/6 = 2/18 − 3/18 = −1/18, also x = −18. Eine Zeit kann nicht negativ sein. Das passt zur Überlegung: Mit einer zweiten Pumpe geht es schneller als mit A allein, also in weniger als 6 Stunden, nicht in 9. Die Rechnung liefert nur eine Scheinlösung für die Sachaufgabe.",
    lambda: F(1, 9) - F(1, 6) == F(-1, 18) and 1 / (F(1, 9) - F(1, 6)) == -18 and F(1, 6) + F(1, 18) == F(2, 9)), g="transfer", regel="id.algebra.gleichung_loesen")
# ───────── verhaeltnis ─────────
neu(T, "verhaeltnis", "zwei_wege", Z(
    "Sirup und Wasser werden im Verhältnis 3 : 8 gemischt. Wie viel Liter Wasser gehören zu 4,5 Litern Sirup? Weg A: Verhältnisgleichung 3/8 = 4,5/x über Kreuz lösen. Weg B: den Faktor bestimmen, mit dem aus 3 die Zahl 4,5 wird, und 8 mit demselben Faktor malnehmen.",
    12, "4.5 * 8 / 3", "8 * (4.5 / 3)", "Beide Wege müssen dieselbe Zahl ergeben. Bei Weg B rechnest du zuerst 4,5 : 3.",
    "Weg A: 3x = 8 · 4,5 = 36, also x = 12. Weg B: 4,5 : 3 = 1,5; 8 · 1,5 = 12. Es sind 12 Liter Wasser. Probe: 3 : 8 = 4,5 : 12.",
    [(9.5, "fb.verhaeltnis.addiert_statt_malgenommen", "den Unterschied der Zahlen 8 und 3 zu 4,5 addiert", "4.5 + 8 - 3"), (36, None, "nur mit 8 malgenommen und nicht durch 3 geteilt", "4.5 * 8"), (1.5, None, "den Faktor angegeben statt der Wassermenge", "4.5 / 3")], "Liter"), g="mehrschritt", regel="rr.verhaeltnis")
neu(T, "verhaeltnis", "fehler_detektiv", FD(
    "Zucker und Mehl werden für einen Teig im Verhältnis 2 : 7 gemischt. Kim berechnet, wie viel Gramm Mehl zu 8 g Zucker gehören.",
    [("Ansatz: Zucker durch Mehl, also 2/7 = 8/x.", F(2, 7) == F(8, 28), True),
     ("Über Kreuz: 2x = 7 · 8, also 2x = 56.", 7 * 8 == 56, True),
     ("Dann ist x = 56 · 2 = 112 g Mehl.", 56 / 2 == 112, 56 / 2 == 112)],
    "Wie kommt man von 2x = 56 zu x? Mache die Probe: Passt 2 : 7 zu 8 : 112?",
    "2x bedeutet 2 mal x. Man teilt beide Seiten durch 2: x = 56 : 2 = 28 g Mehl. Probe: 2 : 7 = 8 : 28."), regel="rr.verhaeltnis")
# ───────── graphisch ─────────
neu(T, "graphisch", "anwenden", Z(
    "Ein Rechteck hat den Flächeninhalt 12 cm². Eine Seite ist x cm lang (x > 0), die andere Seite ist 12/x cm lang. Die Seite 12/x ist 1 cm länger als die Seite x. Die Zeichnung zeigt die Graphen von y = 12/x und y = x + 1. Wie lang ist die Seite x in Zentimetern?",
    3, "12 / 4", 3, "Wo schneiden sich die beiden Graphen für x > 0? Lies die x-Koordinate des Schnittpunkts ab und prüfe mit dem Flächeninhalt.",
    "Die Gleichung ist 12/x = x + 1. Die Graphen schneiden sich für x > 0 im Punkt (3 | 4). Also ist x = 3 cm und 12/x = 4 cm. Probe: 3 · 4 = 12 und 4 = 3 + 1. (Der zweite Schnittpunkt bei x = −4 passt wegen x > 0 nicht.)",
    [(4, None, "die andere Seite 12/x statt x angegeben", "12 / 3"), (-4, None, "den Schnittpunkt mit negativem x abgelesen, obwohl x > 0 verlangt ist", "-4"), (12, None, "die Fläche als Seitenlänge genommen", "3 * 4")], "cm",
    grafik={"typ": "koordinaten", "x": [-6, 6], "y": [-6, 8], "graphen": [{"art": "hyperbel", "a": 12, "b": 0, "c": 0, "name": "y = 12/x"}, {"art": "linear", "m": 1, "t": 1, "name": "y = x + 1"}]}), g="einkleidung", regel="id.funktionen.zuordnung")
neu(T, "graphisch", "umkehren", Z(
    "Die Hyperbel y = k/x und die Gerade y = 2x − 2 schneiden sich an der Stelle x = 4. Welche Zahl ist k?",
    24, "(2 * 4 - 2) * 4", 24, "Berechne zuerst den y-Wert der Geraden bei x = 4. Der Schnittpunkt liegt auch auf der Hyperbel.",
    "Gerade bei x = 4: y = 2 · 4 − 2 = 6. Der Punkt (4 | 6) liegt auch auf der Hyperbel: 6 = k/4. Also k = 24. Probe: 24/4 = 6.",
    [(6, None, "den y-Wert der Geraden als k genommen", "2 * 4 - 2"), (1.5, None, "6 durch 4 geteilt statt mit 4 malgenommen", "6 / 4"), (10, None, "6 + 4 gerechnet statt 6 · 4", "6 + 4")]), g="rueckwaerts", regel="id.funktionen.zuordnung")
