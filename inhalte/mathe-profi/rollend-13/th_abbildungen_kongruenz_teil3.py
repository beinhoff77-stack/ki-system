T = "abbildungen.kongruenz_teil3"
AB = "id.geometrie.abstand"
DK = "id.geometrie.deckungsgleich"
_dreh = lambda x, y: (-y, x)                      # 90 Grad gegen den Uhrzeigersinn um den Ursprung
# ───────── punktspiegelung ─────────
_P, _Z = (-1, 1), (2, 3)
neu(T, "punktspiegelung", "bruecke", W(
    "In der Zeichnung sind der Punkt P und das Zentrum Z eingetragen. P wird am Punkt Z gespiegelt. Welche Koordinaten hat der Bildpunkt P′?",
    "P′(5 | 5)",
    [("P′(2 | 3)", "das Zentrum selbst als Bildpunkt genannt: der Weg von P nach Z wurde nicht noch einmal gegangen"),
     ("P′(5 | 1)", "nur in x-Richtung weitergegangen und die y-Koordinate von P übernommen"),
     ("P′(3 | 2)", "den Vektor von P nach Z als Koordinaten des Bildpunkts genommen")],
    "Lies zuerst die Koordinaten von P und Z ab. Wie viele Schritte geht man von P nach Z in x- und in y-Richtung?",
    "P hat die Koordinaten (−1 | 1), Z hat (2 | 3). Von P nach Z sind es 3 Schritte nach rechts und 2 nach oben. Derselbe Weg noch einmal von Z aus führt zu (2 + 3 | 3 + 2) = (5 | 5). Z ist die Mitte der Strecke von P bis P′.",
    lambda: (2 * _Z[0] - _P[0], 2 * _Z[1] - _P[1]) == (5, 5) and (2 * _Z[0] - _P[0], _P[1]) == (5, 1) and (_Z[0] - _P[0], _Z[1] - _P[1]) == (3, 2) and _Z != (5, 5),
    grafik={"typ": "koordinaten", "x": [-3, 7], "y": [-1, 7], "punkte": [{"x": -1, "y": 1, "name": "P"}, {"x": 2, "y": 3, "name": "Z"}]}), g="darstellung", regel=AB)
neu(T, "punktspiegelung", "zwei_wege", Z(
    "Der Punkt P(−4 | 3) wird am Punkt Z(1 | −3) gespiegelt. Wie groß ist die Summe der beiden Koordinaten des Bildpunkts P′? Weg A: Gehe den Weg von P nach Z noch einmal von Z aus. Weg B: Z ist die Mitte der Strecke von P bis P′. Rechne jede Koordinate von P′ aus den Koordinaten von P und Z.",
    -3, "(2 * 1 - (-4)) + (2 * (-3) - 3)", "(1 + 5) + (-3 - 6)", "Wie groß ist der Schritt von P nach Z in x-Richtung und wie groß in y-Richtung?",
    "Weg A: Von P nach Z sind es 5 Schritte nach rechts und 6 nach unten. Von Z aus noch einmal: P′(1 + 5 | −3 − 6) = (6 | −9). Weg B: Z ist die Mitte, also ist x von Z gleich (−4 + x′) : 2. Daraus folgt x′ = 2 · 1 + 4 = 6 und genauso y′ = 2 · (−3) − 3 = −9. Beide Wege geben P′(6 | −9). Die Summe der Koordinaten ist 6 + (−9) = −3.",
    [(-2, None, "nur bis zum Zentrum gerechnet: die Summe der Koordinaten von Z angegeben", "1 - 3"), (-1, None, "von Z aus in die falsche Richtung gegangen und so wieder P erhalten: die Summe der Koordinaten von P", "-4 + 3"), (9, None, "den Schritt in y-Richtung von Z aus nach oben statt nach unten gemacht", "(1 + 5) + (-3 + 6)")]), g="verknuepfen", regel=AB)
# ───────── drehung ─────────
neu(T, "drehung", "umkehren", Z(
    "Der Punkt P wird um den Ursprung O(0 | 0) um 90° gegen den Uhrzeigersinn gedreht. Dabei wird aus (x | y) der Punkt (−y | x). Das Bild ist P′(−3 | 8). Wie groß ist die Summe der beiden Koordinaten von P?",
    11, "8 + 3", "3 + 8", "Welche Koordinate von P wird zur ersten Koordinate von P′? Welche zur zweiten?",
    "Aus P(x | y) wird P′(−y | x). Also ist −y = −3 und x = 8. Daraus folgt y = 3 und P(8 | 3). Probe: (x | y) = (8 | 3) wird zu (−3 | 8). Summe der Koordinaten von P: 8 + 3 = 11.",
    [(-11, None, "das Bild noch einmal gedreht statt zurückgedreht", "-8 + -3"), (5, None, "die Summe der Koordinaten von P′ angegeben", "-3 + 8"), (-5, None, "die Koordinaten von P′ vertauscht und das Minus an die falsche Stelle gesetzt", "3 + -8")]), g="umkehr", regel=DK)
assert _dreh(8, 3) == (-3, 8)
neu(T, "drehung", "zwei_wege", Z(
    "Der Punkt P(6 | 2) wird um Z(2 | −1) um 180° gedreht. Wie groß ist die Summe der beiden Koordinaten von P′? Weg A: Der Vektor von Z nach P wird zweimal um 90° gegen den Uhrzeigersinn gedreht (aus (a | b) wird (−b | a)), dann wird er an Z angesetzt. Weg B: Z ist die Mitte der Strecke von P bis P′. Rechne jede Koordinate von P′ aus den Koordinaten von P und Z.",
    -6, "(2 * 2 - 6) + (2 * (-1) - 2)", "(2 + (-4)) + (-1 + (-3))", "Wie lautet der Vektor von Z nach P?",
    "Weg A: Der Vektor von Z nach P ist (4 | 3). Nach 90° ist er (−3 | 4), nach nochmals 90° ist er (−4 | −3). Dann ist P′(2 − 4 | −1 − 3) = (−2 | −4). Weg B: x′ = 2 · 2 − 6 = −2 und y′ = 2 · (−1) − 2 = −4. Beide Wege geben P′(−2 | −4). Summe: −6.",
    [(8, None, "gar nicht gedreht: die Summe der Koordinaten von P angegeben", "6 + 2"), (2, None, "nur einmal um 90° gedreht", "(2 - 3) + (-1 + 4)"), (-8, None, "um den Ursprung statt um Z gedreht", "-6 + -2")]), g="verknuepfen", regel=DK)
assert _dreh(*_dreh(4, 3)) == (-4, -3)
# ───────── vektor_drehen ─────────
_A, _B = (1, 1), (4, 3)
_v = (_B[0] - _A[0], _B[1] - _A[1])
neu(T, "vektor_drehen", "bruecke", W(
    "In der Zeichnung sind die Punkte A und B eingetragen. Der Vektor von A nach B wird um 90° gegen den Uhrzeigersinn gedreht. Dabei wird aus (x | y) der Vektor (−y | x). Welcher Vektor entsteht?",
    "(−2 | 3)",
    [("(2 | −3)", "im Uhrzeigersinn gedreht statt gegen den Uhrzeigersinn"), ("(−3 | 2)", "nur das Vorzeichen der ersten Koordinate geändert, nicht gedreht"), ("(−3 | −2)", "den Vektor mit −1 malgenommen: das ist eine Drehung um 180°")],
    "Lies die Koordinaten von A und B ab. Wie lautet der Vektor von A nach B?",
    "A(1 | 1) und B(4 | 3): Der Vektor von A nach B ist (4 − 1 | 3 − 1) = (3 | 2). Mit der Regel wird aus (x | y) der Vektor (−y | x), also (−2 | 3).",
    lambda: _v == (3, 2) and _dreh(*_v) == (-2, 3) and (_v[1], -_v[0]) == (2, -3) and (-_v[0], _v[1]) == (-3, 2) and (-_v[0], -_v[1]) == (-3, -2),
    grafik={"typ": "koordinaten", "x": [-1, 6], "y": [-1, 6], "punkte": [{"x": 1, "y": 1, "name": "A"}, {"x": 4, "y": 3, "name": "B"}]}), g="darstellung", regel=DK)
neu(T, "vektor_drehen", "anwenden", Z(
    "Ein Roboter fährt auf einer Karte von oben gesehen (x zeigt nach Osten, y nach Norden). Er startet im Ursprung und fährt den Vektor (3 | 4). Dort dreht er sich um 90° nach links, also gegen den Uhrzeigersinn. Er fährt eine zweite Strecke, die genauso lang ist wie die erste. Der Vektor der zweiten Fahrt entsteht aus dem Vektor der ersten Fahrt durch diese Drehung. Welche x-Koordinate hat der Roboter am Ende? Eine Zahl mit Minus bedeutet: westlich vom Start.",
    -1, "3 + (-4)", "3 - 4", "Welchen Vektor hat die zweite Fahrt? Dreh den Vektor der ersten Fahrt mit der Regel aus (x | y) wird (−y | x).",
    "Der Vektor der ersten Fahrt ist (3 | 4). Nach einer Linksdrehung um 90° ist er (−4 | 3). Der Roboter steht am Ende bei (3 − 4 | 4 + 3) = (−1 | 7). Die x-Koordinate ist −1.",
    [(6, None, "nicht gedreht: nochmal geradeaus mit demselben Vektor gefahren", "3 + 3"), (7, None, "nach rechts statt nach links gedreht", "3 + 4"), (-4, None, "nur die x-Koordinate des Vektors der zweiten Fahrt angegeben", "-4")]), g="transfer", regel=DK)
