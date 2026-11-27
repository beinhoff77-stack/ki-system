T = "funktionen.linear"
GF = "id.funktionen.gleichung_form"
# ───────── ablesen ─────────
neu(T, "ablesen", "anwenden", Z(
    "Ein Taxi berechnet den Fahrpreis P(x) = 3,5 + 2,2 · x in Euro (x in Kilometern). Um wie viel Euro wird die Fahrt teurer, wenn sie 5 km länger ist?",
    11, "2.2 * 5", "11", "Welche Zahl in P(x) sagt, um wie viel der Preis pro Kilometer steigt? Wie oft kommt sie dazu?",
    "Die Steigung m = 2,2 ist der Preis je Kilometer. Für 5 km mehr kommen 5 · 2,2 = 11 € dazu. Die Grundgebühr 3,5 € fällt nur einmal an und ändert sich nicht.",
    [(2.2, None, "nur den Preis für einen Kilometer angegeben", "2.2"), (14.5, None, "den Gesamtpreis für 5 km statt des Preisunterschieds berechnet", "3.5 + 2.2 * 5"), (5.7, None, "Grundgebühr und Kilometerpreis addiert", "3.5 + 2.2")], "€"), g="einkleidung", regel=GF)
neu(T, "ablesen", "zwei_wege", Z(
    "Wie groß ist die Steigung m der Geraden mit der Gleichung 4x − 2y = 10? Weg A: Löse die Gleichung nach y auf und lies m ab. Weg B: Bestimme zwei Punkte der Geraden (zum Beispiel für x = 0 und für x = 1) und berechne die Steigung aus ihnen.",
    2, "(-4 / -2)", "((4 * 1 - 10) / 2 - (4 * 0 - 10) / 2) / (1 - 0)", "Beide Wege müssen dieselbe Zahl ergeben. Beim Auflösen nach y wird durch −2 geteilt.",
    "Weg A: 4x − 2y = 10 gibt −2y = −4x + 10, also y = 2x − 5. Die Steigung ist m = 2. Weg B: Für x = 0 ist y = −5, für x = 1 ist y = −3. Steigung = (−3 − (−5)) : (1 − 0) = 2.",
    [(4, None, "nicht durch −2 geteilt: nur die Zahl vor x abgelesen", "4"), (-2, None, "4x mit dem falschen Vorzeichen auf die andere Seite gebracht", "4 / (-2)"), (0.5, None, "beim Steigungsdreieck Rechts-Schritt durch Hoch-Schritt geteilt", "1 / 2")]), g="verknuepfen", regel=GF)
assert gl("(4*x-10)/2", "2*x-5")
# ───────── graph_ablesen ─────────
neu(T, "graph_ablesen", "anwenden", Z(
    "Ein Heißluftballon steigt gleichmäßig. Die Zeichnung zeigt seine Höhe h in Metern in Abhängigkeit von der Zeit t in Minuten. Mit welcher Geschwindigkeit steigt der Ballon (in Metern pro Minute)?",
    9, "(56 - 20) / (4 - 0)", 9, "Lies zwei markierte Punkte ab. Wie viel Meter kommen in wie vielen Minuten dazu?",
    "Die markierten Punkte sind (0 | 20) und (4 | 56). In 4 Minuten steigt der Ballon um 56 − 20 = 36 m. Geschwindigkeit: 36 : 4 = 9 Meter pro Minute.",
    [(36, None, "nur den Höhenunterschied angegeben, nicht durch die Zeit geteilt", "56 - 20"), (14, None, "die Höhe am Ende durch die Zeit geteilt", "56 / 4"), (20, None, "die Starthöhe als Geschwindigkeit angegeben", "20")], "m/min",
    grafik={"typ": "koordinaten", "x": [0, 6], "y": [0, 80], "graphen": [{"art": "linear", "m": 9, "t": 20}], "punkte": [{"x": 0, "y": 20}, {"x": 4, "y": 56}], "name_x": "t in min", "name_y": "h in m"}), g="einkleidung", regel=GF)
neu(T, "graph_ablesen", "umkehren", Z(
    "Die Gerade y = 0,75x + t geht durch den Punkt P(4 | 5). Welche Zahl ist t?",
    2, "5 - 0.75 * 4", 2, "Setze die Koordinaten von P in die Geradengleichung ein. Dann bleibt eine Gleichung nur mit t.",
    "Aus 5 = 0,75 · 4 + t folgt 5 = 3 + t, also t = 2. Probe: y = 0,75x + 2 gibt für x = 4 den Wert 5.",
    [(8, None, "3 addiert statt abgezogen", "5 + 0.75 * 4"), (4.25, None, "nur die Steigung abgezogen und nicht 0,75 mal 4", "5 - 0.75"), (5, None, "den y-Wert von P als t genommen", "5")]), g="rueckwaerts", regel=GF)
# ───────── zwei_punkte ─────────
_p = [(1, 5), (4, 11)]
neu(T, "zwei_punkte", "bruecke", W(
    "Die Tabelle zeigt die Koordinaten von zwei Punkten. Eine Gerade geht durch beide Punkte. Welche Gleichung gehört zu dieser Geraden?",
    "y = 2x + 3",
    [("y = 6x − 1", "die Steigung nur als Unterschied der y-Werte 11 − 5 gerechnet, nicht durch den Unterschied der x-Werte geteilt"), ("y = 2x + 5", "die Steigung richtig, aber den y-Wert des ersten Punkts als Achsenabschnitt genommen")],
    "Berechne zuerst die Steigung aus den beiden Punkten. Setze dann einen Punkt ein, um t zu bestimmen.",
    "Steigung: (11 − 5) : (4 − 1) = 6 : 3 = 2. Aus 5 = 2 · 1 + t folgt t = 3. Probe mit dem zweiten Punkt: 2 · 4 + 3 = 11. Bei y = 6x − 1 ergibt x = 4 den Wert 23, bei y = 2x + 5 ergibt x = 1 den Wert 7.",
    lambda: all(2 * x + 3 == y for x, y in _p) and not all(6 * x - 1 == y for x, y in _p) and not all(2 * x + 5 == y for x, y in _p),
    grafik=TAB(["x", "1", "4"], ["y", "5", "11"])), g="darstellung", regel="rr.verhaeltnis")
neu(T, "zwei_punkte", "zwei_wege", Z(
    "Eine Gerade geht durch A(−2 | 1) und B(4 | 7). Welchen y-Wert hat der Punkt der Geraden mit x = 10? Weg A: Bestimme die Gleichung y = m·x + t und setze x = 10 ein. Weg B: Gehe von B aus mit der Steigung weiter: Wie weit musst du nach rechts, und um wie viel geht es dabei nach oben?",
    13, "1 * 10 + 3", "7 + (7 - 1) / (4 + 2) * (10 - 4)", "Beide Wege müssen denselben y-Wert ergeben. Zuerst brauchst du die Steigung aus A und B.",
    "Steigung: (7 − 1) : (4 − (−2)) = 6 : 6 = 1. Weg A: 1 = 1 · (−2) + t gibt t = 3, also y = x + 3 und für x = 10 ist y = 13. Weg B: Von x = 4 bis x = 10 sind es 6 Schritte nach rechts, dabei geht es 6 · 1 = 6 nach oben: 7 + 6 = 13.",
    [(17, None, "die Stelle 10 zum y-Wert von B addiert", "7 + 10"), (11, None, "die Stelle 10 zum y-Wert von A addiert", "1 + 10"), (10, None, "nur m · 10 gerechnet, den Achsenabschnitt vergessen", "1 * 10")]), g="verknuepfen", regel="rr.verhaeltnis")
# ───────── proportional ─────────
neu(T, "proportional", "bruecke", Z(
    "Die Zeichnung zeigt den Graphen einer proportionalen Funktion y = k · x. Der Graph geht durch den markierten Punkt. Wie groß ist k?",
    1.5, "6 / 4", "3 / 2", "Bei einer proportionalen Funktion ist k der Quotient y : x für jeden Punkt des Graphen (außer dem Ursprung).",
    "Der markierte Punkt ist (4 | 6). Dann ist k = y : x = 6 : 4 = 1,5. Probe: y = 1,5 · 4 = 6.",
    [(6, None, "den y-Wert des Punktes als k angegeben", "6"), (4, None, "den x-Wert des Punktes als k angegeben", "4"), (10, None, "die Koordinaten addiert", "4 + 6")],
    grafik={"typ": "koordinaten", "x": [-1, 6], "y": [-1, 9], "graphen": [{"art": "linear", "m": 1.5, "t": 0}], "punkte": [{"x": 4, "y": 6}]}), g="darstellung", regel="rr.verhaeltnis")
neu(T, "proportional", "anwenden", Z(
    "Eine Pumpe fördert gleichmäßig 18 Liter in 4 Minuten. Die geförderte Menge ist proportional zur Zeit. In wie vielen Minuten füllt sie einen Tank mit 108 Litern?",
    24, "108 / (18 / 4)", "108 * 4 / 18", "Wie viele Liter fördert die Pumpe in einer Minute? Wie oft passt diese Menge in 108 Liter?",
    "Pro Minute: 18 : 4 = 4,5 Liter. Für 108 Liter: 108 : 4,5 = 24 Minuten. Probe: 4,5 · 24 = 108.",
    [(486, "fb.verhaeltnis.falsche_richtung", "mit 4,5 malgenommen statt geteilt", "108 * 18 / 4"), (6, None, "nur 108 durch 18 geteilt, die 4 Minuten vergessen", "108 / 18"), (112, None, "108 und 4 addiert", "108 + 4")], "Minuten"), g="transfer", regel="rr.verhaeltnis")
# ───────── aufstellen ─────────
_w = [(0, 400), (1, 550), (2, 700), (3, 850)]
neu(T, "aufstellen", "bruecke", W(
    "Eine Wandergruppe steigt gleichmäßig auf. Die Tabelle zeigt ihre Höhe h in Metern nach t Stunden. Welche Gleichung beschreibt die Höhe in Abhängigkeit von t?",
    "h = 400 + 150t",
    [("h = 150 + 400t", "Anfangshöhe und Zunahme pro Stunde vertauscht: dieser Term ergibt für t = 1 den Wert 550, für t = 2 aber 950 statt 700"), ("h = 550 + 150t", "die Höhe nach einer Stunde als Anfangshöhe genommen: für t = 0 ergibt der Term 550 statt 400")],
    "Welche Höhe gehört zu t = 0? Wie viel kommt von einer Stunde zur nächsten dazu?",
    "Bei t = 0 ist die Höhe 400 m (Anfangshöhe t). Von Stunde zu Stunde kommen 150 m dazu (Steigung m = 150). Also h = 400 + 150t. Probe: t = 3 gibt 400 + 450 = 850.",
    lambda: all(400 + 150 * t == h for t, h in _w) and not all(150 + 400 * t == h for t, h in _w) and not all(550 + 150 * t == h for t, h in _w),
    grafik=TAB(["t in h", "0", "1", "2", "3"], ["h in m", "400", "550", "700", "850"])), g="darstellung", regel="rr.waage")
neu(T, "aufstellen", "umkehren", Z(
    "Eine lineare Funktion f hat f(2) = 7 und f(6) = 19. Wie groß ist f(0)?",
    1, "7 - 2 * ((19 - 7) / (6 - 2))", 1, "Berechne zuerst die Steigung aus den beiden bekannten Werten. Wie viel ändert sich f, wenn x von 2 auf 0 geht?",
    "Steigung: (19 − 7) : (6 − 2) = 12 : 4 = 3. Von x = 2 zurück zu x = 0 sind es 2 Schritte, also 2 · 3 = 6 weniger: f(0) = 7 − 6 = 1. Probe: f(x) = 3x + 1 gibt f(2) = 7 und f(6) = 19.",
    [(-5, None, "mit der falschen Steigung 6 gerechnet: 7 minus 2 mal 6", "7 - 2 * 6"), (3, None, "die Steigung als f(0) angegeben", "(19 - 7) / (6 - 2)"), (13, None, "7 und 6 addiert", "7 + 6")]), g="rueckwaerts", regel="rr.waage")
# ───────── schnittpunkte ─────────
neu(T, "schnittpunkte", "zwei_wege", Z(
    "Wo schneiden sich die Geraden g: y = 2x + 1 und h: y = −x + 7? Gib die x-Koordinate des Schnittpunkts an. Weg A: Lege für x = 0, 1, 2, 3, 4 eine Wertetabelle für beide Geraden an und suche die Spalte mit gleichen y-Werten. Weg B: Setze 2x + 1 = −x + 7 und löse die Gleichung.",
    2, "(7 - 1) / (2 + 1)", "2", "Beide Wege müssen dieselbe Zahl ergeben. Im Schnittpunkt haben beide Geraden denselben y-Wert.",
    "Weg A: g hat die Werte 1, 3, 5, 7, 9 und h hat die Werte 7, 6, 5, 4, 3. Gleich ist die Spalte x = 2 mit y = 5. Weg B: 2x + x = 7 − 1, also 3x = 6 und x = 2. Der Schnittpunkt ist S(2 | 5).",
    [(5, None, "den y-Wert des Schnittpunkts angegeben", "2 * 2 + 1"), (6, None, "2x − x statt 2x + x gerechnet", "(7 - 1) / (2 - 1)"), (-2, None, "die Vorzeichen beim Umstellen vertauscht", "(1 - 7) / (2 + 1)")]), g="mehrschritt", regel="rr.waage")
neu(T, "schnittpunkte", "umkehren", Z(
    "Die Geraden g: y = 2x + 1 und h: y = a·x + 7 schneiden sich an der Stelle x = 2. Welche Zahl ist a?",
    -1, "(2 * 2 + 1 - 7) / 2", -1, "Berechne den y-Wert von g an der Stelle x = 2. Im Schnittpunkt hat h denselben y-Wert.",
    "g(2) = 2 · 2 + 1 = 5. Auch h hat dort den Wert 5: 2a + 7 = 5, also 2a = −2 und a = −1. Probe: h(2) = −2 + 7 = 5.",
    [(6, None, "die 7 mit dem falschen Vorzeichen auf die andere Seite gebracht", "(5 + 7) / 2"), (-2, None, "5 − 7 = −2 nicht durch 2 geteilt", "5 - 7"), (3.5, None, "nur 7 durch 2 geteilt", "7 / 2")]), g="rueckwaerts", regel="rr.waage")
# ───────── lage ─────────
neu(T, "lage", "bruecke", W(
    "Die Zeichnung zeigt die Gerade g. Die Gerade h steht senkrecht auf g und geht durch den Punkt P(0 | 3). Welche Gleichung hat h?",
    "y = −0,5x + 3",
    [("y = −2x + 3", "nur das Vorzeichen der Steigung gewechselt: die Steigungen 2 und −2 ergeben miteinander −4, nicht −1"), ("y = 0,5x + 3", "nur den Kehrwert gebildet: die Steigungen 2 und 0,5 ergeben miteinander 1, nicht −1")],
    "Lies die Steigung von g ab. Bei senkrechten Geraden ist das Produkt der Steigungen −1.",
    "Die Gerade g geht durch (0 | −1) und (1 | 1): Steigung 2. Für die senkrechte Gerade gilt m · 2 = −1, also m = −0,5. Sie geht durch (0 | 3), also t = 3: y = −0,5x + 3.",
    lambda: 2 * (-0.5) == -1 and 2 * (-2) != -1 and 2 * 0.5 != -1,
    grafik={"typ": "koordinaten", "x": [-3, 5], "y": [-4, 6], "graphen": [{"art": "linear", "m": 2, "t": -1, "name": "g"}], "punkte": [{"x": 0, "y": -1}, {"x": 1, "y": 1}, {"x": 0, "y": 3, "name": "P"}]}), g="darstellung", regel=GF)
neu(T, "lage", "anwenden", Z(
    "Im Plan eines Parks (Einheit 1 m) liegt Weg A auf der Geraden y = 0,5x + 2. Im Punkt P(4 | 4) auf Weg A zweigt rechtwinklig ein Weg B ab. Bei welchem y-Wert schneidet Weg B die y-Achse?",
    12, "4 + 2 * 4", "4 - (-2) * 4", "Die Steigungen zweier senkrechter Geraden haben das Produkt −1. Weg B geht durch P.",
    "Steigung von Weg B: m · 0,5 = −1, also m = −2. Durch P(4 | 4): 4 = −2 · 4 + t, also t = 12. Weg B schneidet die y-Achse bei y = 12. Probe: −2 · 4 + 12 = 4.",
    [(-4, None, "die Steigung 2 statt −2 genommen: t = 4 − 2 · 4", "4 - 2 * 4"), (6, None, "nur den Kehrwert −0,5 als Steigung genommen: t = 4 + 0,5 · 4", "4 + 0.5 * 4"), (4, None, "den y-Wert von P als Achsenabschnitt genommen", "4")], "m"), g="transfer", regel=GF)
assert 0.5 * 4 + 2 == 4
# ───────── einsetzen ─────────
neu(T, "einsetzen", "zwei_wege", Z(
    "Gegeben ist die Schar y = (k + 1)·x − 2k. Wie groß ist y für k = 3 und x = 4? Weg A: Setze zuerst k = 3 ein und dann x = 4. Weg B: Schreibe den Term zuerst um in y = k·(x − 2) + x und setze dann beide Zahlen ein.",
    10, "(3 + 1) * 4 - 2 * 3", "3 * (4 - 2) + 4", "Beide Wege müssen dieselbe Zahl ergeben. Beim Umschreiben wird (k + 1)·x zu k·x + x.",
    "Weg A: y = (3 + 1) · 4 − 2 · 3 = 16 − 6 = 10. Weg B: (k + 1)x − 2k = kx + x − 2k = k(x − 2) + x. Für k = 3 und x = 4: 3 · 2 + 4 = 10.",
    [(22, None, "−2k als +2k gerechnet", "(3 + 1) * 4 + 2 * 3"), (1, "fb.reihenfolge.links_nach_rechts", "die Klammer um k + 1 weggelassen: nur die 1 mit x malgenommen und k addiert", "3 + 1 * 4 - 2 * 3"), (16, None, "das Glied −2k vergessen", "(3 + 1) * 4")]), g="mehrschritt", regel=GF)
assert gl("(a+1)*x-2*a", "a*(x-2)+x")
neu(T, "einsetzen", "umkehren", Z(
    "Eine Gerade der Schar y = (k − 2)·x + 2k geht durch den Punkt P(3 | 9). Welche Zahl ist k?",
    3, "(9 + 2 * 3) / (3 + 2)", 3, "Setze die Koordinaten von P ein. Löse die Klammer auf und fasse die k-Glieder zusammen.",
    "Aus 9 = (k − 2) · 3 + 2k folgt 9 = 3k − 6 + 2k = 5k − 6. Also 5k = 15 und k = 3. Probe: y = x + 6 gibt für x = 3 den Wert 9.",
    [(2.2, "fb.ausmultiplizieren.nur_erster_summand", "bei der Klammer nur k mit 3 malgenommen: aus (k − 2)·3 wird 3k − 2", "11 / 5"), (15, None, "das Glied 2k mit dem falschen Vorzeichen übernommen", "15"), (1.5, None, "nur die Zahlen zusammengefasst: 9 durch 6 geteilt", "9 / 6")]), g="rueckwaerts", regel=GF)
# ───────── wirkung ─────────
neu(T, "wirkung", "anwenden", Z(
    "Ein Stromtarif berechnet K(x) = 8 + 0,3x in Euro (x in kWh). Der Preis je kWh steigt von 0,30 € auf 0,40 €, die Grundgebühr von 8 € bleibt gleich. Um wie viel Euro steigt die Rechnung für 50 kWh?",
    5, "(0.4 - 0.3) * 50", "0.4 * 50 - 0.3 * 50", "Was ändert sich: die Grundgebühr oder der Preis je kWh? Wie wirkt sich die Änderung bei 50 kWh aus?",
    "Die Grundgebühr bleibt gleich. Pro kWh kommen 0,40 − 0,30 = 0,10 € dazu. Für 50 kWh sind das 50 · 0,10 = 5 €. Probe: alt 8 + 15 = 23 €, neu 8 + 20 = 28 €.",
    [(0.1, None, "nur die Preisänderung pro kWh angegeben", "0.4 - 0.3"), (28, None, "die neue Rechnung statt der Erhöhung angegeben", "8 + 0.4 * 50"), (20, None, "nur den neuen Verbrauchspreis für 50 kWh berechnet", "0.4 * 50")], "€"), g="einkleidung", regel=GF)
neu(T, "wirkung", "umkehren", Z(
    "Die Gerade y = (k − 1)·x + 3 soll doppelt so steil sein wie die Gerade y = 2x + 3. Welche Zahl ist k?",
    5, "2 * 2 + 1", 5, "Wie groß ist die Steigung der gesuchten Geraden? Wie hängt sie mit k zusammen?",
    "Die Gerade y = 2x + 3 hat die Steigung 2. Doppelt so steil bedeutet die Steigung 4. Es gilt k − 1 = 4, also k = 5. Probe: y = 4x + 3.",
    [(3, None, "die Steigung 2 statt 4 gleichgesetzt: k − 1 = 2", "2 + 1"), (4, None, "die gesuchte Steigung als k angegeben", "2 * 2"), (7, None, "als Steigung 2 plus 4 statt 2 mal 2 genommen", "2 + 4 + 1")]), g="rueckwaerts", regel=GF)
# ───────── bueschel ─────────
neu(T, "bueschel", "bruecke", W(
    "Die Zeichnung zeigt drei Geraden einer Schar. Alle Geraden der Schar gehen durch denselben Punkt. Welche Gleichung beschreibt die Schar (m ist die Steigung der jeweiligen Geraden)?",
    "y = m·(x − 2) + 3",
    [("y = m·(x + 2) + 3", "das Vorzeichen in der Klammer vertauscht: der gemeinsame Punkt wäre (−2 | 3)"), ("y = m·(x − 3) + 2", "x- und y-Koordinate des gemeinsamen Punkts vertauscht: der gemeinsame Punkt wäre (3 | 2)")],
    "Wo schneiden sich die drei Geraden? Welcher Punkt ergibt sich, wenn in y = m·(x − a) + b der Wert x = a eingesetzt wird?",
    "Alle drei Geraden gehen durch den Punkt (2 | 3). In y = m·(x − 2) + 3 verschwindet der Klammerterm für x = 2, und y = 3 gilt für jede Steigung m. Die Geraden in der Zeichnung gehören zu m = −1, m = 0,5 und m = 2.",
    lambda: all(m * (2 - 2) + 3 == 3 for m in (-1, 0.5, 2)) and not all(m * (2 + 2) + 3 == 3 for m in (-1, 0.5, 2)) and not all(m * (2 - 3) + 2 == 3 for m in (-1, 0.5, 2)),
    grafik={"typ": "koordinaten", "x": [-2, 6], "y": [-2, 8], "graphen": [{"art": "linear", "m": -1, "t": 5}, {"art": "linear", "m": 0.5, "t": 2}, {"art": "linear", "m": 2, "t": -1}], "punkte": [{"x": 2, "y": 3}]}), g="darstellung", regel=GF)
neu(T, "bueschel", "anwenden", Z(
    "Zwei Laserstrahlen starten im Punkt P(2 | 3) und verlaufen geradlinig. Strahl A hat die Steigung 0,75, Strahl B hat die Steigung −0,25. Bei x = 6 steht eine senkrechte Wand. Wie viele Einheiten liegen die beiden Treffpunkte an der Wand auseinander?",
    4, "(3 + 0.75 * (6 - 2)) - (3 - 0.25 * (6 - 2))", "6 - 2", "Jeder Strahl liegt auf einer Geraden durch P. Berechne für beide die Höhe bei x = 6.",
    "Strahl A: y = 0,75 · (x − 2) + 3, bei x = 6 ist y = 0,75 · 4 + 3 = 6. Strahl B: y = −0,25 · (x − 2) + 3, bei x = 6 ist y = −1 + 3 = 2. Abstand der Treffpunkte: 6 − 2 = 4 Einheiten.",
    [(6, None, "nur den Treffpunkt von Strahl A angegeben", "3 + 0.75 * (6 - 2)"), (8, None, "die beiden Höhen addiert statt subtrahiert", "(3 + 0.75 * (6 - 2)) + (3 - 0.25 * (6 - 2))"), (1, None, "nur die Steigungen verglichen: 0,75 plus 0,25", "0.75 + 0.25")], "Einheiten"), g="transfer", regel=GF)
# ───────── deuten ─────────
neu(T, "deuten", "anwenden", W(
    "Die Höhe einer Sonnenblume wird durch H(t) = 12 + 1,5·t beschrieben (t in Tagen, H in Zentimetern). Welche Aussage stimmt?",
    "Die Sonnenblume war am Anfang 12 cm hoch und wächst jeden Tag um 1,5 cm.",
    [("Die Sonnenblume war am Anfang 1,5 cm hoch und wächst jeden Tag um 12 cm.", "Anfangshöhe und Wachstum pro Tag vertauscht"), ("Die Sonnenblume ist nach 12 Tagen 1,5 cm hoch.", "die Zahlen als Zeitpunkt und Höhe gelesen statt als Anfangshöhe und Zuwachs")],
    "Welche Höhe gehört zu t = 0? Um wie viel ändert sich H, wenn t um 1 größer wird?",
    "Für t = 0 ist H = 12: Am Anfang ist die Pflanze 12 cm hoch. Jeder Tag bringt 1,5 cm dazu, denn 1,5 steht vor t. Nach 10 Tagen ist H = 27 cm.",
    lambda: 12 + 1.5 * 0 == 12 and (12 + 1.5 * 1) - (12 + 1.5 * 0) == 1.5 and 12 + 1.5 * 12 != 1.5), g="einkleidung", regel="id.funktionen.wachstum")
neu(T, "deuten", "zwei_wege", Z(
    "Tarif A kostet K_A(x) = 5 + 0,2x, Tarif B kostet K_B(x) = 12 + 0,1x (x Minuten Gesprächszeit, Kosten in Euro, abgerechnet wird nur für ganze Minuten). Wie viele ganze Minuten muss man mindestens telefonieren, damit Tarif B billiger ist als Tarif A? Weg A: Löse die Ungleichung 12 + 0,1x < 5 + 0,2x. Weg B: Bestimme die Minute, bei der beide Tarife gleich viel kosten, und überlege mit den Steigungen, welcher Tarif danach billiger ist.",
    71, "(12 - 5) / (0.2 - 0.1) + 1", "70 + 1", "Beide Wege müssen dieselbe Zahl ergeben. Der Tarif mit der größeren Steigung wird mit der Zeit teurer.",
    "Weg A: 12 + 0,1x < 5 + 0,2x gibt 7 < 0,1x, also x > 70. Weg B: Gleich teuer bei 12 + 0,1x = 5 + 0,2x, also x = 70 (beide 19 €). Tarif A hat die größere Steigung, wird also danach teurer. Ab 71 Minuten ist B billiger. Probe: 71 Minuten kosten bei A 19,20 € und bei B 19,10 €.",
    [(70, None, "die Schnittstelle als Antwort angegeben: dort kosten beide gleich viel", "(12 - 5) / (0.2 - 0.1)"), (35, None, "nur durch die Steigung von Tarif A geteilt", "(12 - 5) / 0.2"), (-70, None, "die Zahlen im Nenner vertauscht", "(12 - 5) / (0.1 - 0.2)")], "Minuten"), g="verknuepfen", regel="id.funktionen.wachstum")
