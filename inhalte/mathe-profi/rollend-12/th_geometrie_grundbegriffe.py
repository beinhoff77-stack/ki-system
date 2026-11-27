T = "geometrie.grundbegriffe"
KO, AB, WI = "id.geometrie.abstand", "id.geometrie.abstand", "id.geometrie.winkel"
_R = ["A", "B", "C", "D"]

# ───────── koordinaten ─────────
neu(T, "koordinaten", "umkehren", W(
    "Ein Punkt wird zweimal hintereinander um dieselbe Verschiebung bewegt: jedes Mal 2 Einheiten nach rechts und 3 Einheiten nach unten. Danach liegt er bei (3 | −4). Wo lag er am Anfang?",
    "(−1 | 2)",
    [("(1 | −1)", "Es wurde nur eine der beiden Verschiebungen rückgängig gemacht."), ("(7 | −10)", "Die beiden Verschiebungen wurden noch einmal in dieselbe Richtung gerechnet statt zurück."), ("(−1 | −10)", "Die x-Koordinate wurde zurückgerechnet, die y-Koordinate aber noch einmal nach unten.")],
    "Welche Gesamtverschiebung ergeben die beiden Schritte? Wie kommst du von der Endlage zurück?",
    "Zweimal 2 nach rechts und 3 nach unten sind zusammen 4 nach rechts und 6 nach unten. Rückwärts: 4 nach links und 6 nach oben. x: 3 − 4 = −1, y: −4 + 6 = 2. Der Punkt lag bei (−1 | 2). Probe: (−1 + 4 | 2 − 6) = (3 | −4).",
    lambda: (3 - 4, -4 + 6) == (-1, 2) and (3 - 2, -4 + 3) == (1, -1) and (3 + 4, -4 - 6) == (7, -10) and (3 - 4, -4 - 6) == (-1, -10)), g="umkehr")
neu(T, "koordinaten", "zwei_wege", Z(
    "Ein Roboter steht im Punkt (−3 | 2). Er fährt zuerst 4 Einheiten nach rechts und dann 7 Einheiten nach unten. Wie viele Einheiten ist er danach von der x-Achse entfernt? Weg A: Bestimme zuerst seine neue Position. Weg B: Vergleiche direkt, wie weit er nach unten fährt, mit seinem Abstand zur x-Achse am Start.",
    5, "abs(2 - 7)", "7 - 2", "Welche Koordinate bestimmt den Abstand eines Punktes zur x-Achse? Wie ändert sie sich bei der Fahrt?",
    "Nach 4 nach rechts: (1 | 2). Nach 7 nach unten: (1 | 2 − 7) = (1 | −5). Der Abstand zur x-Achse ist |−5| = 5 Einheiten.",
    [(9, None, "die Beträge 2 und 7 addiert", "2 + 7"), (7, None, "nur die Fahrt nach unten genommen", "7"), (1, None, "den Abstand zur y-Achse genannt", "-3 + 4")], "Einheiten"), g="verknuepfen")

# ───────── strecken ─────────
neu(T, "strecken", "zwei_wege", Z(
    "Ein Weg verläuft waagrecht vom Punkt A(−4 | 1) zum Punkt B(5 | 1). Eine Einheit im Koordinatensystem entspricht 20 m. Wie lang ist der Weg in Metern? Weg A: Rechne mit den Koordinaten 5 − (−4). Weg B: Zähle die Einheiten von A bis zum Nullpunkt und von dort bis B.",
    180, "(5 - (-4)) * 20", "(4 + 5) * 20", "Wie viele Einheiten liegen zwischen x = −4 und x = 5? Denke an den Nullpunkt.",
    "Der Weg ist 5 − (−4) = 9 Einheiten lang. 9 · 20 m = 180 m.",
    [(20, None, "nur die Beträge voneinander abgezogen (das Minus von −4 nicht beachtet)", "(5 - 4) * 20"), (100, None, "nur die x-Koordinate von B genommen", "5 * 20"), (9, None, "die Länge in Einheiten statt in Metern angegeben", "5 + 4")], "m"))
neu(T, "strecken", "bruecke", Z(
    "Die Tabelle nennt drei Strecken, die alle waagrecht oder senkrecht verlaufen. Um wie viele Einheiten ist die längste Strecke länger als die kürzeste?",
    3, "8 - 5", "(3 + 5) - (-1 + 6)", "Berechne zuerst die Länge jeder Strecke. Nur eine Koordinate ändert sich.",
    "[AB]: 4 − (−3) = 7. [CD]: 3 − (−5) = 8. [EF]: −1 − (−6) = 5. Die längste ist 8, die kürzeste 5. 8 − 5 = 3.",
    [(8, None, "die Länge der längsten Strecke genannt", "8"), (1, None, "die längste mit der zweitlängsten verglichen", "8 - 7"), (13, None, "längste und kürzeste Strecke addiert", "8 + 5")], "Einheiten",
    grafik=TAB(["Strecke", "Anfangspunkt", "Endpunkt"], ["[AB]", "A(−3 | 2)", "B(4 | 2)"], ["[CD]", "C(1 | −5)", "D(1 | 3)"], ["[EF]", "E(−6 | −1)", "F(−1 | −1)"])), g="verknuepfen")

# ───────── lagebeziehungen ─────────
neu(T, "lagebeziehungen", "umkehren", Z(
    "Eine Gerade g verläuft von oben nach unten (parallel zur y-Achse). Sie wird um 5 Einheiten nach rechts verschoben und heißt danach h. Die Geraden g und h sind also parallel und haben den Abstand 5. Die Gerade h geht durch den Punkt (7 | 3). Welche x-Koordinate haben alle Punkte von g?",
    2, "7 - 5", "2", "Um wie viel und in welche Richtung wurde g verschoben? Wie kommst du von h zu g zurück?",
    "Alle Punkte von h haben die x-Koordinate 7, denn h geht durch (7 | 3) und verläuft von oben nach unten. g wurde um 5 nach rechts verschoben, also muss man um 5 nach links zurück: x = 7 − 5 = 2. Probe: 2 + 5 = 7, der Abstand von g und h ist 5.",
    [(12, None, "noch einmal um 5 nach rechts statt zurück nach links gerechnet", "7 + 5"), (5, None, "den Abstand als x-Koordinate genommen", "5"), (3, None, "die y-Koordinate des Punktes genommen", "3")]), g="umkehr", regel=AB)
neu(T, "lagebeziehungen", "anwenden", Z(
    "Eine waagrechte Hauptstraße liegt auf y = 2. Zwei Nebenstraßen stehen senkrecht auf ihr. Die eine geht durch den Punkt (5 | 2), die andere durch den Punkt (−3 | 2). Wie viele Einheiten sind die beiden Nebenstraßen voneinander entfernt?",
    8, "5 - (-3)", "5 + 3", "Beide Nebenstraßen sind senkrecht. Welche Koordinate legt ihre Lage fest?",
    "Die Nebenstraßen liegen bei x = 5 und x = −3 und sind parallel. Ihr Abstand ist 5 − (−3) = 8 Einheiten.",
    [(2, None, "5 − 3 gerechnet, das Vorzeichen übersehen", "5 - 3"), (4, None, "den Abstand halbiert", "(5 - (-3)) / 2"), (15, None, "5 · 3 gerechnet", "5 * 3")], "Einheiten"), g="transfer", regel=AB)

# ───────── kreis_lage ─────────
neu(T, "kreis_lage", "anwenden", Z(
    "Ein Funkmast steht im Punkt M(2 | 3) und erreicht alle Orte, die höchstens 4 Einheiten von M entfernt sind. Wie viele der vier Häuser P(2 | 6), Q(7 | 3), R(−1 | 3) und S(2 | −2) werden erreicht? (Alle Häuser liegen auf einer waagrechten oder senkrechten Linie durch M.)",
    2, "2", "1 + 1", "Bestimme für jedes Haus den Abstand zu M. Nur eine Koordinate ist anders.",
    "P: 6 − 3 = 3 ≤ 4, erreicht. Q: 7 − 2 = 5 > 4, nicht erreicht. R: 2 − (−1) = 3 ≤ 4, erreicht. S: 3 − (−2) = 5 > 4, nicht erreicht. Es sind 2 Häuser.",
    [(4, None, "alle Häuser gezählt", "2 + 2"), (3, None, "bei Haus Q die y-Koordinate von M statt der x-Koordinate abgezogen, so wird Q mitgezählt", lambda: abs(7 - 3) == 4)], "Häuser"), regel=AB)
neu(T, "kreis_lage", "umkehren", Z(
    "Ein Kreis um M(3 | 2) berührt von links die senkrechte Gerade x = 11. Welchen Radius hat der Kreis?",
    8, "11 - 3", "8", "Welcher Punkt des Kreises liegt auf der Geraden? Wo liegt er im Vergleich zu M?",
    "Der Berührpunkt ist (11 | 2). Der Radius ist der waagrechte Abstand von M: 11 − 3 = 8.",
    [(14, None, "11 und 3 addiert", "11 + 3"), (11, None, "die Zahl der Geraden als Radius genommen", "11"), (9, None, "mit der y-Koordinate gerechnet: 11 − 2", "11 - 2")]), g="rueckwaerts", regel=AB)

# ───────── winkelarten ─────────
neu(T, "winkelarten", "bruecke", W(
    "Der Minutenzeiger einer Uhr startet bei der 12 und dreht sich im Uhrzeigersinn bis zu einer Zahl auf dem Zifferblatt. Bis zu welcher Zahl hat er einen überstumpfen Winkel überstrichen?",
    "Bis zur 9",
    [("Bis zur 3", "Eine Vierteldrehung ist ein rechter Winkel (90°)."), ("Bis zur 6", "Eine halbe Drehung ist ein gestreckter Winkel (180°)."), ("Bis zur 12 nach einer ganzen Runde", "Eine ganze Drehung ist ein Vollwinkel (360°).")],
    "Welcher Teil einer ganzen Runde ist bis zur Zahl geschafft? Überstumpf liegt zwischen gestreckt und Vollwinkel.",
    "Von der 12 bis zur 3 ist es eine Vierteldrehung: 90°, ein rechter Winkel. Bis zur 6: halbe Drehung, 180°, gestreckt. Bis zur 9: Dreivierteldrehung, 270°, überstumpf. Bis zur 12 nach einer ganzen Runde: 360°, Vollwinkel.",
    lambda: [180 < 90 * k < 360 for k in (1, 2, 3, 4)] == [False, False, True, False]))
neu(T, "winkelarten", "anwenden", Z(
    "Eine Tür lässt sich von 0° bis 180° öffnen. Ein Feststeller hält sie bei jedem Vielfachen von 15° fest (0°, 15°, 30°, … bis 180°). Bei wie vielen dieser Einstellungen ist der Öffnungswinkel ein stumpfer Winkel?",
    5, "(165 - 105) / 15 + 1", "5", "Zwischen welchen beiden Gradzahlen liegen stumpfe Winkel? Welche Einstellungen des Feststellers fallen in diesen Bereich?",
    "Stumpf heißt: größer als 90° und kleiner als 180°. Das trifft auf 105°, 120°, 135°, 150° und 165° zu, also 5 Einstellungen. 90° ist ein rechter Winkel, 180° ein gestreckter.",
    [(6, None, "den gestreckten Winkel 180° mitgezählt", lambda: sum(90 < w <= 180 for w in range(0, 181, 15)) == 6), (7, None, "den rechten Winkel 90° und den gestreckten Winkel 180° mitgezählt", lambda: sum(90 <= w <= 180 for w in range(0, 181, 15)) == 7)], "Einstellungen"), g="transfer")

# ───────── vierecke ─────────
neu(T, "vierecke", "bruecke", W(
    "Die Tabelle beschreibt vier Vierecke A bis D. Welches Viereck ist eine Raute, die kein Quadrat ist?",
    "Viereck B",
    [("Viereck A", "Alle Seiten gleich lang und vier rechte Winkel: das ist ein Quadrat."), ("Viereck C", "Vier rechte Winkel, aber nicht alle Seiten gleich lang: ein Rechteck."), ("Viereck D", "Weder alle Seiten gleich lang noch rechte Winkel: das ist keine Raute.")],
    "Eine Raute hat vier gleich lange Seiten. Ein Quadrat hat zusätzlich vier rechte Winkel.",
    "Eine Raute hat vier gleich lange Seiten. Ein Quadrat hätte zusätzlich vier rechte Winkel. Gesucht ist also: gleich lange Seiten (ja), rechte Winkel (nein). Das ist Viereck B.",
    lambda: [(s and not r) for s, r in ((True, True), (True, False), (False, True), (False, False))] == [False, True, False, False], grafik=TAB(["Viereck", "Alle vier Seiten gleich lang", "Vier rechte Winkel"], ["A", "ja", "ja"], ["B", "ja", "nein"], ["C", "nein", "ja"], ["D", "nein", "nein"])))
neu(T, "vierecke", "anwenden", Z(
    "Ein Beet hat die Form eines Rechtecks mit den Ecken A(−3 | −2), B(5 | −2), C(5 | 3) und D(−3 | 3). Eine Einheit entspricht 1 m. Wie viele Meter Zaun braucht man rund um das Beet?",
    26, "2 * (8 + 5)", "8 + 5 + 8 + 5", "Wie lang sind die Seiten [AB] und [BC]? Eine Koordinate bleibt jeweils gleich.",
    "[AB] hat die Länge 5 − (−3) = 8 m. [BC] hat die Länge 3 − (−2) = 5 m. Rundherum: 2 · (8 + 5) = 26 m.",
    [(13, None, "nur zwei Seiten gezählt (halber Umfang)", "8 + 5"), (40, None, "den Flächeninhalt statt des Umfangs berechnet", "8 * 5"), (18, None, "eine Seite zu wenig gezählt: 8 + 5 + 5", "8 + 5 + 5")], "m"), g="transfer")

# ───────── verstehen ─────────
neu(T, "verstehen", "bruecke", Z(
    "Mia behauptet: „Jeder Punkt mit negativer x-Koordinate liegt unter der x-Achse.“ In der Tabelle stehen sechs Punkte. Bei wie vielen von ihnen zeigt sich, dass die Behauptung nicht stimmt?",
    2, "2", "1 + 1", "Zu einem Gegenbeispiel gehört eine negative x-Koordinate, aber ein Punkt, der nicht unter der x-Achse liegt. Welche Punkte der Tabelle sind das?",
    "Ein Gegenbeispiel hat x < 0 und liegt über der x-Achse (y > 0). Das gilt für A(−3 | 4) und D(−6 | 2). B(−2 | −1) und F(−4 | −5) bestätigen die Behauptung, C(5 | −2) und E(1 | 3) haben ein positives x. Es sind 2 Punkte.",
    [(3, None, "alle Punkte über der x-Achse gezählt, auch E mit positivem x", lambda: sum(y > 0 for x, y in ((-3, 4), (-2, -1), (5, -2), (-6, 2), (1, 3), (-4, -5))) == 3), (4, None, "alle Punkte mit negativem x gezählt", lambda: sum(x < 0 for x, y in ((-3, 4), (-2, -1), (5, -2), (-6, 2), (1, 3), (-4, -5))) == 4)], "Punkte",
    grafik=TAB(["Punkt", "x-Koordinate", "y-Koordinate"], ["A", "−3", "4"], ["B", "−2", "−1"], ["C", "5", "−2"], ["D", "−6", "2"], ["E", "1", "3"], ["F", "−4", "−5"])))
neu(T, "verstehen", "anwenden", W(
    "Tom behauptet: „Jedes Viereck mit vier gleich langen Seiten ist ein Quadrat.“ Welche Figur zeigt, dass Tom nicht recht hat?",
    "Eine Raute mit 5 cm Seitenlänge und den Winkeln 60° und 120°",
    [("Ein Quadrat mit 5 cm Seitenlänge", "Das Quadrat passt zu Toms Aussage und widerlegt sie nicht."), ("Ein Rechteck mit den Seiten 3 cm und 5 cm", "Dieses Viereck hat keine vier gleich langen Seiten, es sagt über Toms Aussage nichts."), ("Ein Parallelogramm mit den Seiten 4 cm und 6 cm", "Auch hier sind nicht alle vier Seiten gleich lang, es ist also kein Gegenbeispiel.")],
    "Ein Gegenbeispiel muss die Voraussetzung (vier gleich lange Seiten) erfüllen, aber trotzdem kein Quadrat sein.",
    "Gesucht ist ein Viereck mit vier gleich langen Seiten, das kein Quadrat ist: Die Raute mit den Winkeln 60° und 120° hat vier gleich lange Seiten, aber keine rechten Winkel.",
    lambda: [(len(set(s)) == 1 and not all(w == 90 for w in ws)) for s, ws in (((5, 5, 5, 5), (60, 120, 60, 120)), ((5, 5, 5, 5), (90, 90, 90, 90)), ((3, 5, 3, 5), (90, 90, 90, 90)), ((4, 6, 4, 6), (70, 110, 70, 110)))] == [True, False, False, False]), g="transfer")
