T = "abbildungen.aehnlichkeit"
R = "id.geometrie.aehnlich"
K6 = "① = □; ② = □; ③ = □; ④ = □; ⑤ = □; ⑥ = □"
# ───────── streckung ─────────
neu(T, "streckung", "lueckenweg", L(
    "Eine zentrische Streckung hat das Zentrum Z(1 | −2) und den Streckfaktor k = 3. Der Punkt P(6 | 2) wird abgebildet. Der Pfeil von Z nach P geht ① Einheiten nach rechts und ② Einheiten nach oben. Der Pfeil von Z zum Bildpunkt P' ist k-mal so lang: Er geht ③ Einheiten nach rechts und ④ Einheiten nach oben. Der Bildpunkt hat die Koordinaten P'(⑤ | ⑥).",
    K6, [5, 4, 15, 12, 16, 10], ["6 - 1", "2 - (-2)", "3 * {1}", "3 * {2}", "1 + {3}", "-2 + {4}"], ["5", "4", "15", "12", "16", "10"],
    "Der Bildpunkt liegt auf dem Strahl von Z durch P. Gemessen wird immer vom Zentrum Z aus, nicht vom Ursprung.",
    "Pfeil ZP: (6 − 1 | 2 − (−2)) = (5 | 4). Pfeil ZP': 3 · (5 | 4) = (15 | 12). P' = Z + (15 | 12) = (1 + 15 | −2 + 12) = (16 | 10).",
    {0: [(7, None, "6 + 1 gerechnet: das Zentrum nicht abgezogen, sondern addiert", "6 + 1")], 1: [(0, None, "die y-Koordinaten addiert statt subtrahiert: 2 + (−2)", "2 + (-2)")],
     2: [(8, "fb.verhaeltnis.addiert_statt_malgenommen", "den Faktor addiert statt malgenommen: 5 + 3", "{1} + 3")],
     4: [(18, None, "vom Ursprung statt von Z aus gestreckt: 3 · 6", "3 * 6")], 5: [(6, None, "vom Ursprung statt von Z aus gestreckt: 3 · 2", "3 * 2")]}), regel=R)
neu(T, "streckung", "umkehren", Z(
    "Eine zentrische Streckung hat das Zentrum Z(2 | 1). Sie bildet den Punkt P(5 | 3) auf den Punkt P'(14 | 9) ab. Welchen Streckfaktor k hat diese Streckung?",
    4, "(14 - 2) / (5 - 2)", "(9 - 1) / (3 - 1)", "Vergleiche den Pfeil von Z nach P mit dem Pfeil von Z nach P'.",
    "Pfeil ZP: (5 − 2 | 3 − 1) = (3 | 2). Pfeil ZP': (14 − 2 | 9 − 1) = (12 | 8). Es ist 12 : 3 = 4 und 8 : 2 = 4. Also k = 4. Probe: Z + 4 · (3 | 2) = (14 | 9).",
    [(2.8, None, "ohne das Zentrum geteilt: 14 : 5", "14 / 5"), (9, None, "die Pfeilkomponenten subtrahiert: 12 − 3", "12 - 3")]), g="umkehr", regel=R)
neu(T, "streckung", "fehler_detektiv", FD(
    "Der Punkt P(4 | 3) wird zentrisch gestreckt, mit dem Zentrum Z(1 | 1) und dem Faktor k = 2. Kim berechnet den Bildpunkt P'.",
    [("Pfeil von Z nach P: (4 + 1 | 3 + 1) = (5 | 4).", 4 - 1 == 5 and 3 - 1 == 4, True),
     ("Mit k = 2 wird der Pfeil zu (10 | 8).", True, 2 * 5 == 10 and 2 * 4 == 8),
     ("Bildpunkt P' = Z + (10 | 8) = (1 + 10 | 1 + 8) = (11 | 9).", True, 1 + 10 == 11 and 1 + 8 == 9)],
    "Wie bekommt man den Pfeil von einem Punkt Z zu einem Punkt P?",
    "Der Pfeil von Z nach P ist P − Z = (4 − 1 | 3 − 1) = (3 | 2). Dann ist ZP' = (6 | 4) und P' = (1 + 6 | 1 + 4) = (7 | 5). Der erste Fehler steht in Zeile 1: Kim hat addiert statt subtrahiert."), regel=R)

# ───────── bildgerade ─────────
neu(T, "bildgerade", "lueckenweg", L(
    "Die Gerade g: y = 3x + 2 wird mit dem Zentrum O(0 | 0) und dem Faktor k = 5 gestreckt. Der Punkt A(0 | 2) liegt auf g. Sein Bildpunkt A' hat die y-Koordinate ①. Der Punkt B(1 | 5) liegt auf g. Sein Bildpunkt B' hat die y-Koordinate ②. Die Bildgerade g' geht durch A' und B'. Für x = 6 hat g' den y-Wert ③.",
    "① = □; ② = □; ③ = □", [10, 25, 28], ["2 * 5", "5 * 5", "{1} + ({2} - {1}) / (5 - 0) * 6"], ["10", "25", "10 + 3 * 6"],
    "Beide Koordinaten des Punktes werden mit dem Faktor multipliziert. Für die Bildgerade brauchst du die Steigung zwischen A' und B'.",
    "A' = (0 | 10). B' = (5 | 25). Steigung von g': (25 − 10) : (5 − 0) = 3. g': y = 3x + 10. Für x = 6: 3 · 6 + 10 = 28.",
    {0: [(7, "fb.verhaeltnis.addiert_statt_malgenommen", "2 + 5 gerechnet statt 2 · 5", "2 + 5")], 1: [(10, "fb.verhaeltnis.addiert_statt_malgenommen", "5 + 5 gerechnet statt 5 · 5", "5 + 5")],
     2: [(20, None, "mit der Geraden g statt mit g' gerechnet: 3 · 6 + 2", "3 * 6 + 2")]}), regel=R)
neu(T, "bildgerade", "zwei_wege", Z(
    "Die Gerade g: y = 2x + 5 wird mit dem Zentrum O(0 | 0) und dem Faktor k = 3 gestreckt. Wie groß ist der y-Achsenabschnitt der Bildgeraden g'? Rechne auf zwei Wegen. Weg A: Strecke den Punkt (0 | 5) von g und lies den y-Achsenabschnitt ab. Weg B: Strecke zwei andere Punkte von g, zum Beispiel die mit x = 1 und x = 2, und bestimme die Gerade durch die beiden Bildpunkte.",
    15, "5 * 3", "(2 * 1 + 5) * 3 - (((2 * 2 + 5) * 3) - ((2 * 1 + 5) * 3)) / (2 * 3 - 1 * 3) * (1 * 3)", "Beide Wege müssen dasselbe ergeben. Bei Weg B ist ein Bildpunkt (3 | 21).",
    "Weg A: (0 | 5) wird zu (0 | 15), der Achsenabschnitt ist 15. Weg B: (1 | 7) wird zu (3 | 21), (2 | 9) wird zu (6 | 27). Steigung: (27 − 21) : (6 − 3) = 2. Dann 21 − 2 · 3 = 15. Beide Wege: 15.",
    [(5, None, "den y-Achsenabschnitt von g übernommen", "5"), (8, "fb.verhaeltnis.addiert_statt_malgenommen", "5 + 3 gerechnet statt 5 · 3", "5 + 3"), (6, None, "die Steigung 2 mit dem Faktor 3 vervielfacht: 2 · 3", "2 * 3")]), regel=R)
neu(T, "bildgerade", "fehler_detektiv", FD(
    "Die Gerade g: y = −x + 4 wird mit dem Zentrum O(0 | 0) und dem Faktor k = 2 gestreckt. Kim bestimmt die Bildgerade g'.",
    [("g hat die Steigung −1 und den y-Achsenabschnitt 4.", True, True),
     ("Die Streckung verdoppelt auch die Steigung: g' hat die Steigung −2.", False, True),
     ("Der y-Achsenabschnitt wird verdoppelt auf 8. Also ist g': y = −2x + 8.", False, 2 * 4 == 8)],
    "Bei einer Streckung mit dem Zentrum O ist das Bild einer Geraden parallel zu ihr (wenn sie nicht durch O geht). Was heißt das für die Steigung?",
    "Eine Gerade und ihre Bildgerade sind parallel, die Steigung bleibt −1. Nur der Achsenabschnitt wird verdoppelt. g': y = −x + 8. Der erste Fehler steht in Zeile 2."), regel=R)

# ───────── schwerpunkt ─────────
neu(T, "schwerpunkt", "lueckenweg", L(
    "Ein Dreieck hat die Eckpunkte A(1 | 2), B(8 | 3) und C(3 | 10). Die x-Koordinaten der drei Eckpunkte ergeben zusammen ①. Die y-Koordinaten ergeben zusammen ②. Der Schwerpunkt S hat die Koordinaten S(③ | ④).",
    "① = □; ② = □; ③ = □; ④ = □", [12, 15, 4, 5], ["1 + 8 + 3", "2 + 3 + 10", "{1} / 3", "{2} / 3"], ["12", "15", "12 // 3", "15 // 3"],
    "Der Schwerpunkt eines Dreiecks hat als Koordinaten den Mittelwert der drei x-Koordinaten und den Mittelwert der drei y-Koordinaten.",
    "x: 1 + 8 + 3 = 12. y: 2 + 3 + 10 = 15. S = (12 : 3 | 15 : 3) = (4 | 5).",
    {2: [(6, None, "durch 2 statt durch 3 geteilt: 12 : 2", "{1} / 2")], 3: [(7.5, None, "durch 2 statt durch 3 geteilt: 15 : 2", "{2} / 2")]}), regel=R)
neu(T, "schwerpunkt", "umkehren", Z(
    "Ein Dreieck ABC hat den Schwerpunkt S(3 | 2). Es gilt A(1 | 0) und B(6 | 1). Wie groß ist die y-Koordinate von C?",
    5, "3 * 2 - 0 - 1", "2 * 3 - (0 + 1)", "Die y-Koordinate von S ist der Mittelwert der drei y-Koordinaten. Stelle die Gleichung nach der unbekannten Zahl um.",
    "Es gilt (0 + 1 + y) : 3 = 2. Also 0 + 1 + y = 6 und y = 6 − 1 = 5. Probe: (0 + 1 + 5) : 3 = 2.",
    [(1, None, "2 − 0 − 1 gerechnet: den Faktor 3 vergessen", "2 - 0 - 1"), (7, None, "die y-Koordinaten von A und B addiert statt abgezogen: 3 · 2 + 0 + 1", "3 * 2 + 0 + 1")], "")
, g="rueckwaerts", regel=R)
neu(T, "schwerpunkt", "anwenden", Z(
    "Eine dünne Platte hat überall die gleiche Dicke und die Form eines Dreiecks ABC mit A(0 | 0), B(12 | 0) und C(3 | 9). Die Maße sind in cm. Die Platte soll waagerecht auf einer Spitze balancieren. Wie weit ist der Auflagepunkt von der Seite AB entfernt? Gib den Abstand in cm an.",
    3, "(0 + 0 + 9) / 3", "9 / 3", "Der Auflagepunkt ist der Schwerpunkt des Dreiecks. Gefragt ist nur sein Abstand von der Seite AB, also die y-Koordinate.",
    "S = ((0 + 12 + 3) : 3 | (0 + 0 + 9) : 3) = (5 | 3). Die Seite AB liegt auf der x-Achse, der Abstand ist die y-Koordinate 3 cm.",
    [(4.5, None, "die halbe Höhe genommen: 9 : 2", "9 / 2"), (6, None, "zwei Drittel der Höhe genommen: 2 · 9 : 3", "2 * 9 / 3"), (9, None, "die Höhe von C angegeben", "9")], "cm"), g="einkleidung", regel=R)

# ───────── aehnlich ─────────
neu(T, "aehnlich", "lueckenweg", L(
    "Das Dreieck B ist ähnlich zum Dreieck A. Das Dreieck A hat die Seiten 4 cm, 6 cm und 8 cm. Die kürzeste Seite von B ist 12 cm lang. Der Streckfaktor von A nach B ist ①. Die mittlere Seite von B ist ② cm lang, die längste Seite ③ cm. Der Umfang von B ist ④ cm.",
    "① = □; ② = □; ③ = □; ④ = □", [3, 18, 24, 54], ["12 / 4", "6 * {1}", "8 * {1}", "12 + {2} + {3}"], ["3", "18", "24", "12 + 18 + 24"],
    "Bei ähnlichen Dreiecken werden alle Seiten mit demselben Faktor vervielfacht. Vergleiche zuerst zwei entsprechende Seiten.",
    "k = 12 : 4 = 3. Mittlere Seite: 6 · 3 = 18 cm. Längste Seite: 8 · 3 = 24 cm. Umfang: 12 + 18 + 24 = 54 cm.",
    {0: [(8, None, "12 − 4 gerechnet statt 12 : 4", "12 - 4")], 1: [(14, None, "den Unterschied 8 zu 6 addiert: 6 + 8", "6 + (12 - 4)")], 2: [(16, None, "den Unterschied 8 zu 8 addiert: 8 + 8", "8 + (12 - 4)")],
     3: [(18, None, "den Umfang von A statt von B angegeben", "4 + 6 + 8")]}), regel=R)
neu(T, "aehnlich", "fehler_detektiv", FD(
    "Das Dreieck B ist ähnlich zum Dreieck A. A hat die Seiten 4 cm, 6 cm und 8 cm. Die kürzeste Seite von B ist 12 cm lang. Kim berechnet die mittlere Seite von B und prüft sie.",
    [("Streckfaktor von A nach B: 12 : 4 = 3.", 12 / 4 == 3, True),
     ("Mittlere Seite von B: 6 + 3 = 9 cm.", 6 + 3 == 6 * 3, 6 + 3 == 9),
     ("Damit ist das Verhältnis der mittleren Seiten von B und A gleich 9 : 6 = 1,5.", True, 9 / 6 == 1.5)],
    "Wie wirkt ein Streckfaktor auf eine Seitenlänge: addieren oder multiplizieren?",
    "Eine Seite wird mit dem Streckfaktor multipliziert: 6 · 3 = 18 cm. Kim hat 3 addiert. Außerdem müsste das Verhältnis der mittleren Seiten wieder 3 sein, nicht 1,5. Der erste Fehler steht in Zeile 2."), regel=R)
neu(T, "aehnlich", "bruecke", W(
    "Die Tabelle zeigt die Seitenlängen von drei Dreiecken, jeweils von der kürzesten zur längsten Seite. Welche zwei Dreiecke sind zueinander ähnlich?",
    "A und C", [("A und B", "nur die kürzesten Seiten verglichen: sie sind im Verhältnis 1 : 2, die längsten aber 6 : 9"), ("B und C", "die ersten beiden Seiten stimmen im Verhältnis, die längsten nicht: 9 : 18"), ("Alle drei Dreiecke", "es passen nur zwei Dreiecke zusammen")],
    "Teile für zwei Dreiecke jeweils entsprechende Seiten durcheinander. Alle drei Quotienten müssen gleich sein.",
    "A → C: 9 : 3 = 3, 12 : 4 = 3, 18 : 6 = 3. Alle Quotienten sind gleich. A → B: 2, 2 und 1,5, also nicht ähnlich. B → C: 1,5, 1,5 und 2, also nicht ähnlich.",
    lambda: (9 / 3 == 12 / 4 == 18 / 6) and not (6 / 3 == 8 / 4 == 9 / 6) and not (9 / 6 == 12 / 8 == 18 / 9),
    grafik=TAB(["Dreieck", "kürzeste Seite", "mittlere Seite", "längste Seite"], ["A", "3 cm", "4 cm", "6 cm"], ["B", "6 cm", "8 cm", "9 cm"], ["C", "9 cm", "12 cm", "18 cm"])), regel=R)

# ───────── strahlensatz1 ─────────
neu(T, "strahlensatz1", "lueckenweg", L(
    "Zwei Strahlen mit dem gemeinsamen Anfangspunkt S werden von zwei parallelen Geraden geschnitten, die nicht durch S gehen. Die erste Gerade schneidet die Strahlen in A und B, die zweite in A' und B'. A und A' liegen auf dem einen Strahl, B und B' auf dem anderen, A und B liegen näher bei S. Es gilt SA = 4 cm, SA' = 12 cm und SB = 5 cm. Das Verhältnis SA' : SA ist ①. Die Strecke SB' ist ② cm lang. Die Strecke BB' ist ③ cm lang.",
    "① = □; ② = □; ③ = □", [3, 15, 10], ["12 / 4", "5 * {1}", "{2} - 5"], ["3", "15", "15 - 5"],
    "Nach dem 1. Strahlensatz haben die Verhältnisse SA' : SA und SB' : SB denselben Wert. BB' ist der Teil von SB', der nicht zu SB gehört.",
    "SA' : SA = 12 : 4 = 3. SB' = 3 · 5 = 15 cm. BB' = SB' − SB = 15 − 5 = 10 cm.",
    {0: [(8, None, "12 − 4 gerechnet statt 12 : 4", "12 - 4")], 1: [(8, "fb.verhaeltnis.addiert_statt_malgenommen", "5 + 3 gerechnet statt 5 · 3", "5 + {1}")], 2: [(15, None, "die ganze Strecke SB' statt des Stücks BB' angegeben", "{2}")]}), regel=R)
neu(T, "strahlensatz1", "anwenden", Z(
    "Die Sonnenstrahlen sind zueinander parallel. Ein senkrechter Stab ist 1,5 m hoch und wirft auf dem waagerechten Boden einen 2 m langen Schatten. Im selben Moment wirft ein senkrechter Turm einen 28 m langen Schatten. Wie hoch ist der Turm?",
    21, "28 * 1.5 / 2", "28 / 2 * 1.5", "Stab mit Schatten und Turm mit Schatten bilden zwei Dreiecke mit demselben Verhältnis Höhe : Schattenlänge.",
    "Höhe : Schatten ist beim Stab 1,5 : 2 = 0,75. Beim Turm gilt dasselbe Verhältnis: Höhe = 0,75 · 28 = 21 m.",
    [(37.33, "fb.verhaeltnis.falsche_richtung", "das Verhältnis umgekehrt (Schatten durch Höhe statt Höhe durch Schatten), auf zwei Stellen gerundet", "28 * 2 / 1.5"), (27.5, None, "den Unterschied von Stabhöhe und Schatten (0,5 m) vom Turmschatten abgezogen", "28 - (2 - 1.5)")], "m"), g="einkleidung", regel=R)
neu(T, "strahlensatz1", "fehler_detektiv", FD(
    "Zwei Strahlen mit dem Anfangspunkt S werden von zwei parallelen Geraden geschnitten. Die erste schneidet in A und B, die zweite in A' und B'. A und A' liegen auf dem einen Strahl, B und B' auf dem anderen, A und B liegen näher bei S. Es gilt SA = 3 cm, SA' = 9 cm und SB = 4 cm. Kim berechnet die Strecke BB'.",
    [("1. Strahlensatz: SA' : SA = SB' : SB, also 9 : 3 = SB' : 4.", True, True),
     ("Das Verhältnis 9 : 3 ist 3. Also ist SB' = 3 · 4 = 12 cm.", 9 / 3 * 4 == 12, 9 / 3 == 3 and 3 * 4 == 12),
     ("Dann ist BB' = SB' + SB = 12 + 4 = 16 cm.", 12 - 4 == 16, 12 + 4 == 16)],
    "BB' ist ein Stück der Strecke SB'. Wie bekommt man dieses Stück?",
    "SB' = SB + BB', also BB' = SB' − SB = 12 − 4 = 8 cm. Kim hat in Zeile 3 addiert. Zeile 1 und 2 sind richtig."), regel=R)

# ───────── strahlensatz2 ─────────
neu(T, "strahlensatz2", "lueckenweg", L(
    "Zwei Strahlen mit dem gemeinsamen Anfangspunkt S werden von zwei parallelen Geraden geschnitten, die nicht durch S gehen. Die erste Gerade schneidet die Strahlen in A und B, die zweite in A' und B'. A und A' liegen auf dem einen Strahl, B und B' auf dem anderen, A und B liegen näher bei S. Es gilt SA = 5 cm, SA' = 15 cm und AB = 4 cm. Nach dem 2. Strahlensatz ist das Verhältnis A'B' : AB so groß wie SA' : SA. Dieses Verhältnis ist ①. Die Strecke A'B' ist ② cm lang. Sie ist um ③ cm länger als AB.",
    "① = □; ② = □; ③ = □", [3, 12, 8], ["15 / 5", "4 * {1}", "{2} - 4"], ["3", "12", "12 - 4"],
    "Das Verhältnis der Strecken auf den Strahlen ist so groß wie das Verhältnis der Parallelstrecken A'B' und AB.",
    "SA' : SA = 15 : 5 = 3. A'B' = 3 · 4 = 12 cm. Unterschied: 12 − 4 = 8 cm.",
    {0: [(10, None, "15 − 5 gerechnet statt 15 : 5", "15 - 5")], 1: [(7, "fb.verhaeltnis.addiert_statt_malgenommen", "4 + 3 gerechnet statt 4 · 3", "4 + {1}")], 2: [(16, None, "A'B' und AB addiert statt abgezogen: 12 + 4", "{2} + 4")]}), regel=R)
neu(T, "strahlensatz2", "umkehren", Z(
    "Zwei Strahlen mit dem Anfangspunkt S werden von zwei parallelen Geraden geschnitten. Die erste schneidet in A und B, die zweite in A' und B'. A und A' liegen auf dem einen Strahl, B und B' auf dem anderen, A liegt zwischen S und A'. Es gilt A'B' : AB = 5 : 2 und SA = 8 cm. Wie lang ist die Strecke AA'?",
    12, "8 * 5 / 2 - 8", "8 * (5 / 2 - 1)", "Zuerst brauchst du SA'. Dann ist AA' das Stück von SA', das nicht zu SA gehört.",
    "Nach dem 2. Strahlensatz ist SA' : SA = A'B' : AB = 5 : 2. Also SA' = 8 · 5 : 2 = 20 cm. AA' = SA' − SA = 20 − 8 = 12 cm.",
    [(20, None, "SA' statt AA' angegeben", "8 * 5 / 2"), (3.2, "fb.verhaeltnis.falsche_richtung", "das Verhältnis umgekehrt: 8 · 2 : 5", "8 * 2 / 5")], "cm"), g="umkehr", regel=R)
neu(T, "strahlensatz2", "fehler_detektiv", FD(
    "Zwei Strahlen mit dem Anfangspunkt S werden von zwei parallelen Geraden geschnitten. Die erste schneidet in A und B, die zweite in A' und B'. A und A' liegen auf dem einen Strahl, B und B' auf dem anderen. Es gilt SA = 5 cm, SA' = 8 cm und AB = 10 cm. Kim berechnet A'B'.",
    [("2. Strahlensatz: A'B' : AB = SA : SA'.", False, True),
     ("Also A'B' : 10 = 5 : 8 und A'B' = 10 · 5 : 8 = 6,25 cm.", False, 10 * 5 / 8 == 6.25),
     ("A'B' ist also kürzer als AB.", False, 6.25 < 10)],
    "A' liegt weiter von S entfernt als A. Wird die Parallelstrecke dann länger oder kürzer?",
    "Es gilt A'B' : AB = SA' : SA = 8 : 5. Also A'B' = 10 · 8 : 5 = 16 cm. Zeile 1 hat die Verhältnisse vertauscht, die Folgezeilen rechnen daraus richtig weiter."), regel=R)

# ───────── flaeche_volumen ─────────
neu(T, "flaeche_volumen", "lueckenweg", L(
    "Zwei Würfel sind zueinander ähnlich. Der kleine Würfel hat die Kantenlänge 2 cm und das Volumen 8 Kubikzentimeter. Der große Würfel hat die Kantenlänge 6 cm. Der Streckfaktor von klein nach groß ist ①. Die Oberfläche wird mit dem Faktor ② vervielfacht, das Volumen mit dem Faktor ③. Das Volumen des großen Würfels ist ④ Kubikzentimeter.",
    "① = □; ② = □; ③ = □; ④ = □", [3, 9, 27, 216], ["6 / 2", "{1} ** 2", "{1} ** 3", "8 * {3}"], ["3", "9", "27", "6 * 6 * 6"],
    "Längen werden mit k vervielfacht. Für Flächen und Rauminhalte gilt eine andere Regel: Zähle die Richtungen, in denen gestreckt wird.",
    "k = 6 : 2 = 3. Flächenfaktor 3² = 9. Volumenfaktor 3³ = 27. Volumen: 8 · 27 = 216 cm³. Probe: 6 · 6 · 6 = 216.",
    {0: [(4, None, "6 − 2 gerechnet statt 6 : 2", "6 - 2")], 1: [(6, None, "3 · 2 statt 3² gerechnet", "{1} * 2")], 2: [(9, None, "3² statt 3³ gerechnet", "{1} ** 2")], 3: [(24, "fb.aehnlich.flaeche_mit_k", "das Volumen nur mit k vervielfacht: 8 · 3", "8 * {1}")]}), regel=R)
neu(T, "flaeche_volumen", "zwei_wege", Z(
    "Ein kleines Dreieck hat die Grundseite 4 cm und den Flächeninhalt 12 cm². Ein dazu ähnliches großes Dreieck hat die Grundseite 10 cm. Wie groß ist der Flächeninhalt des großen Dreiecks in cm²? Rechne auf zwei Wegen. Weg A: mit dem Streckfaktor der Längen und dem Flächenfaktor. Weg B: berechne die Höhe des kleinen Dreiecks, dann die Höhe des großen Dreiecks, dann seine Fläche.",
    75, "12 * (10 / 4) ** 2", "10 * (2 * 12 / 4 * (10 / 4)) / 2", "Beide Wege müssen dasselbe ergeben. Der Streckfaktor der Längen ist 10 : 4.",
    "Weg A: k = 10 : 4 = 2,5. Flächenfaktor 2,5² = 6,25. Fläche: 12 · 6,25 = 75 cm². Weg B: Höhe klein: 2 · 12 : 4 = 6 cm. Höhe groß: 6 · 2,5 = 15 cm. Fläche: 10 · 15 : 2 = 75 cm².",
    [(30, "fb.aehnlich.flaeche_mit_k", "die Fläche nur mit k vervielfacht: 12 · 2,5", "12 * 2.5"), (18, None, "den Unterschied der Grundseiten addiert: 12 + 6", "12 + (10 - 4)")], "cm²"), regel=R)
neu(T, "flaeche_volumen", "anwenden", Z(
    "Ein Modellschiff ist eine genaue Verkleinerung eines echten Schiffs im Maßstab 1 : 25. Der Rumpf des Modells fasst 2 Liter Wasser. Wie viele Liter fasst der Rumpf des echten Schiffs?",
    31250, "2 * 25 ** 3", "2 * 25 * 25 * 25", "Der Maßstab 1 : 25 gilt für Längen. Rauminhalte wachsen anders.",
    "Alle Längen sind 25-mal so groß, der Rauminhalt ist 25³ = 15 625-mal so groß. 2 · 15 625 = 31 250 Liter.",
    [(50, "fb.aehnlich.flaeche_mit_k", "nur mit dem Längenfaktor 25 vervielfacht: 2 · 25", "2 * 25"), (1250, None, "mit dem Flächenfaktor 625 statt dem Rauminhaltsfaktor vervielfacht: 2 · 625", "2 * 25 ** 2")], "Liter"), g="transfer", regel=R)

# ───────── anwendung ─────────
neu(T, "anwendung", "lueckenweg", L(
    "Ein rechteckiges Foto ist 9 cm breit und 6 cm hoch. Es wird zu einem ähnlichen Poster vergrößert, das 45 cm breit ist. Der Vergrößerungsfaktor ist ①. Das Poster ist ② cm hoch. Der Flächeninhalt des Posters ist ③ cm².",
    "① = □; ② = □; ③ = □", [5, 30, 1350], ["45 / 9", "6 * {1}", "45 * {2}"], ["5", "30", "45 * 30"],
    "Bei einer ähnlichen Vergrößerung werden Breite und Höhe mit demselben Faktor vervielfacht. Die Fläche rechnest du am Schluss aus den neuen Seiten.",
    "k = 45 : 9 = 5. Höhe: 6 · 5 = 30 cm. Fläche: 45 · 30 = 1 350 cm².",
    {0: [(36, None, "45 − 9 gerechnet statt 45 : 9", "45 - 9")], 1: [(42, None, "den Unterschied 36 zur Höhe addiert: 6 + 36", "6 + (45 - 9)")], 2: [(270, "fb.aehnlich.flaeche_mit_k", "die Fläche des Fotos nur mit k vervielfacht: 9 · 6 · 5", "9 * 6 * {1}")]}), regel=R)
neu(T, "anwendung", "anwenden", Z(
    "Eine Lochkamera ist ein Kasten mit einem winzigen Loch in der Vorderwand. Ein Baum, 1,8 m hoch, steht senkrecht 6 m vor dem Loch. Die Rückwand des Kastens ist 12 cm vom Loch entfernt. Der Baum erscheint auf der Rückwand als umgekehrtes Bild. Wie hoch ist dieses Bild in cm?",
    3.6, "180 * 12 / 600", "1.8 * 12 / 6", "Die Lichtstrahlen laufen durch das Loch. Vor und hinter dem Loch entstehen zwei Dreiecke mit gleichem Verhältnis Höhe : Abstand. Rechne in einer Einheit.",
    "Höhe : Abstand ist beim Baum 1,8 m : 6 m = 0,3. Beim Bild gilt dasselbe Verhältnis: Bildhöhe = 0,3 · 12 cm = 3,6 cm.",
    [(360, None, "Meter und Zentimeter gemischt: 180 · 12 : 6", "180 * 12 / 6"), (0.036, None, "Ergebnis in Meter statt in cm angegeben", "1.8 * 0.12 / 6"), (21.6, None, "nur 1,8 · 12 gerechnet, nicht durch 6 geteilt", "1.8 * 12")], "cm"), g="einkleidung", regel=R)
neu(T, "anwendung", "fehler_detektiv", FD(
    "Ein senkrechter Stab ist 1,2 m hoch und wirft einen 0,8 m langen Schatten. Im selben Moment wirft eine senkrechte Fichte auf dem waagerechten Boden einen 10 m langen Schatten. Kim berechnet die Höhe der Fichte.",
    [("Beim Stab ist Höhe : Schatten = 1,2 : 0,8 = 1,5.", round(1.2 / 0.8, 9) == 1.5, True),
     ("Bei der Fichte ist das Verhältnis Höhe : Schatten dasselbe, also 1,5.", True, True),
     ("Die Höhe der Fichte ist also 10 : 1,5 ≈ 6,7 m.", 10 * 1.5 == 10 / 1.5, round(10 / 1.5, 1) == 6.7)],
    "Das Verhältnis Höhe : Schatten ist 1,5. Wie bekommt man daraus die Höhe, wenn der Schatten 10 m lang ist?",
    "Höhe = Verhältnis · Schatten = 1,5 · 10 = 15 m. Kim hat geteilt statt malgenommen. Eine Fichte, die niedriger ist als ihr Schatten, passt auch nicht zu einem Stab, der höher ist als sein Schatten."), regel=R)

# ───────── streckung_vektor ─────────
neu(T, "streckung_vektor", "lueckenweg", L(
    "Eine zentrische Streckung hat das Zentrum Z(2 | 1) und den Faktor k = −3. Der Punkt P(7 | 4) wird zu P' abgebildet. Der Vektor von Z nach P hat die Komponenten (5 | 3). Der Vektor von Z nach P' hat die Komponenten (① | ②). Der Bildpunkt hat die Koordinaten P'(③ | ④).",
    "① = □; ② = □; ③ = □; ④ = □", [-15, -9, -13, -8], ["-3 * 5", "-3 * 3", "2 + {1}", "1 + {2}"], ["-15", "-9", "2 - 15", "1 - 9"],
    "Der Vektor ZP' ist k-mal der Vektor ZP. Ein negativer Faktor dreht die Richtung um. Der Bildpunkt entsteht, wenn du den Vektor ZP' an Z anlegst.",
    "ZP' = −3 · (5 | 3) = (−15 | −9). P' = Z + ZP' = (2 − 15 | 1 − 9) = (−13 | −8).",
    {0: [(15, None, "das Vorzeichen von k vergessen: 3 · 5", "3 * 5")], 1: [(9, None, "das Vorzeichen von k vergessen: 3 · 3", "3 * 3")], 2: [(-15, None, "den Vektor ZP' als Bildpunkt angegeben, Z nicht addiert", "{1}")], 3: [(-9, None, "den Vektor ZP' als Bildpunkt angegeben, Z nicht addiert", "{2}")]}), regel=R)
neu(T, "streckung_vektor", "bruecke", W(
    "Die Tabelle zeigt, wie weit man von dem Zentrum Z der Streckung nach rechts und nach oben gehen muss, um zu P und zu dem Bildpunkt P' zu kommen. Negative Zahlen bedeuten nach links oder nach unten. Welche Aussage passt?",
    "Der Streckfaktor ist k = −2. P' liegt auf der anderen Seite von Z als P und doppelt so weit von Z entfernt.",
    [("Der Streckfaktor ist k = 2. P' liegt auf derselben Seite von Z wie P und doppelt so weit von Z entfernt.", "das Vorzeichen übersehen"),
     ("Der Streckfaktor ist k = −2. P' liegt auf derselben Seite von Z wie P.", "bei negativem k liegt das Bild auf der anderen Seite von Z"),
     ("Der Streckfaktor ist k = −0,5. P' liegt auf der anderen Seite von Z und halb so weit von Z entfernt.", "das Verhältnis umgekehrt: Der Pfeil zu P' ist doppelt so lang, nicht halb so lang")],
    "Vergleiche den Pfeil zu P' mit dem Pfeil zu P: Mit welcher Zahl wird jede Komponente vervielfacht?",
    "Pfeil zu P: (2 | 1). Pfeil zu P': (−4 | −2) = −2 · (2 | 1). Also k = −2. Das Minuszeichen heißt: andere Seite von Z. Der Betrag 2 heißt: doppelt so weit entfernt.",
    lambda: (-4 == -2 * 2) and (-2 == -2 * 1),
    grafik=TAB(["", "nach rechts", "nach oben"], ["von Z zu P", "2", "1"], ["von Z zu P'", "−4", "−2"])), regel=R)
neu(T, "streckung_vektor", "umkehren", Z(
    "Eine zentrische Streckung hat den Faktor k = −2. Sie bildet den Punkt P(7 | 3) auf den Punkt P'(−2 | −3) ab. Wie groß ist die x-Koordinate des Zentrums Z?",
    4, "(7 * (-2) - (-2)) / (-2 - 1)", "(-2 - (-2) * 7) / (1 - (-2))", "Für das Bild gilt: P' = Z + k · (P − Z). Setze die x-Koordinaten ein und löse nach der x-Koordinate von Z auf.",
    "Mit x für die x-Koordinate von Z: −2 = x + (−2) · (7 − x) = x − 14 + 2x = 3x − 14. Also 3x = 12 und x = 4. Probe: 4 + (−2) · (7 − 4) = 4 − 6 = −2.",
    [(2.5, None, "den Mittelpunkt von P und P' genommen: (7 + (−2)) : 2", "(7 + (-2)) / 2"), (-9, None, "die Differenz der x-Koordinaten genommen: −2 − 7", "-2 - 7")]), g="rueckwaerts", regel=R)
