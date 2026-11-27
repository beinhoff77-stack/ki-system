T = "geometrie.grundbegriffe"
KO, AB, WI = "id.geometrie.abstand", "id.geometrie.abstand", "id.geometrie.winkel"
_R = ["A", "B", "C", "D"]

# ───────── koordinaten ─────────
neu(T, "koordinaten", "umkehren", W(
    "Ein Punkt wurde um 3 Einheiten nach rechts und um 5 Einheiten nach oben verschoben. Jetzt liegt er bei (1 | 2). Wo lag er vorher?",
    "(−2 | −3)",
    [("(4 | 7)", "Die Verschiebung wurde noch einmal in dieselbe Richtung gerechnet."), ("(−2 | 7)", "Nur die x-Koordinate wurde zurückgerechnet."), ("(4 | −3)", "Nur die y-Koordinate wurde zurückgerechnet.")],
    "Mache die Verschiebung rückgängig: In welche Richtung musst du jetzt gehen?",
    "Rückwärts: 3 nach links und 5 nach unten. x: 1 − 3 = −2, y: 2 − 5 = −3. Der Punkt lag bei (−2 | −3). Probe: (−2 + 3 | −3 + 5) = (1 | 2).",
    lambda: (1 - 3, 2 - 5) == (-2, -3) and (1 + 3, 2 + 5) == (4, 7) and (1 - 3, 2 + 5) == (-2, 7) and (1 + 3, 2 - 5) == (4, -3)), g="umkehr", regel=KO)
neu(T, "koordinaten", "zwei_wege", Z(
    "Ein Roboter steht im Punkt (−3 | 2). Er fährt zuerst 4 Einheiten nach rechts und dann 7 Einheiten nach unten. Wie viele Einheiten ist er danach von der x-Achse entfernt? Weg A: Bestimme zuerst seine neue Position. Weg B: Vergleiche direkt, wie weit er nach unten fährt, mit seinem Abstand zur x-Achse am Start.",
    5, "abs(2 - 7)", "7 - 2", "Wo steht der Roboter am Ende? Der Abstand zur x-Achse hängt nur von der y-Koordinate ab.",
    "Nach 4 nach rechts: (1 | 2). Nach 7 nach unten: (1 | 2 − 7) = (1 | −5). Der Abstand zur x-Achse ist |−5| = 5 Einheiten.",
    [(9, None, "die Beträge 2 und 7 addiert", "2 + 7"), (7, None, "nur die Fahrt nach unten genommen", "7"), (1, None, "den Abstand zur y-Achse genannt", "-3 + 4")], "Einheiten"), g="verknuepfen", regel=KO)

# ───────── strecken ─────────
neu(T, "strecken", "zwei_wege", Z(
    "Ein Weg verläuft waagrecht vom Punkt A(−4 | 1) zum Punkt B(5 | 1). Eine Einheit im Koordinatensystem entspricht 20 m. Wie lang ist der Weg in Metern? Weg A: Rechne mit den Koordinaten 5 − (−4). Weg B: Zähle die Einheiten von A bis zum Nullpunkt und von dort bis B.",
    180, "(5 - (-4)) * 20", "(4 + 5) * 20", "Wie viele Einheiten liegen zwischen x = −4 und x = 5? Denke an den Nullpunkt.",
    "Der Weg ist 5 − (−4) = 9 Einheiten lang. 9 · 20 m = 180 m.",
    [(20, None, "nur die Beträge voneinander abgezogen (das Minus von −4 nicht beachtet)", "(5 - 4) * 20"), (100, None, "nur die x-Koordinate von B genommen", "5 * 20"), (9, None, "die Länge in Einheiten statt in Metern angegeben", "5 + 4")], "m"), regel=AB)
neu(T, "strecken", "bruecke", Z(
    "Die Tabelle nennt drei Strecken, die alle waagrecht oder senkrecht verlaufen. Um wie viele Einheiten ist die längste Strecke länger als die kürzeste?",
    3, "8 - 5", "(1 - (-5)) + 2 - 5", "Berechne zuerst die Länge jeder Strecke. Nur eine Koordinate ändert sich.",
    "[AB]: 4 − (−3) = 7. [CD]: 3 − (−5) = 8. [EF]: −1 − (−6) = 5. Die längste ist 8, die kürzeste 5. 8 − 5 = 3.",
    [(8, None, "die Länge der längsten Strecke genannt", "8"), (1, None, "die längste mit der zweitlängsten verglichen", "8 - 7"), (13, None, "längste und kürzeste addiert", "8 + 5")], "Einheiten",
    grafik=TAB(["Strecke", "Anfangspunkt", "Endpunkt"], ["[AB]", "A(−3 | 2)", "B(4 | 2)"], ["[CD]", "C(1 | −5)", "D(1 | 3)"], ["[EF]", "E(−6 | −1)", "F(−1 | −1)"])), g="verknuepfen", regel=AB)

# ───────── lagebeziehungen ─────────
neu(T, "lagebeziehungen", "umkehren", Z(
    "Die Gerade g geht durch A(2 | 1) und B(2 | 6). Die Gerade h ist parallel zu g, liegt rechts von g und hat von g den Abstand 5. Welche x-Koordinate haben alle Punkte von h?",
    7, "2 + 5", "7", "Wie verläuft g, waagrecht oder senkrecht? Welche Koordinate bleibt bei h für alle Punkte gleich?",
    "g ist senkrecht (x = 2 für alle Punkte). Eine parallele Gerade ist auch senkrecht. Rechts mit Abstand 5: x = 2 + 5 = 7.",
    [(-3, None, "links statt rechts von g gerechnet", "2 - 5"), (5, None, "den Abstand als x-Koordinate genommen", "5"), (3, None, "5 − 2 gerechnet", "5 - 2")]), g="umkehr", regel=AB)
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
    8, "11 - 3", "8", "Der Berührpunkt liegt auf der Geraden und auf derselben Höhe wie M. Wie weit ist das waagrecht von M?",
    "Der Berührpunkt ist (11 | 2). Der Radius ist der waagrechte Abstand von M: 11 − 3 = 8.",
    [(14, None, "11 und 3 addiert", "11 + 3"), (11, None, "die Zahl der Geraden als Radius genommen", "11"), (9, None, "mit der y-Koordinate gerechnet: 11 − 2", "11 - 2")]), g="rueckwaerts", regel=AB)

# ───────── winkelarten ─────────
neu(T, "winkelarten", "bruecke", W(
    "Welche Gradzahl gehört zu einem überstumpfen Winkel, der kleiner als 200° ist?",
    "190°",
    [("170°", "Das ist ein stumpfer Winkel (zwischen 90° und 180°)."), ("200°", "Das ist überstumpf, aber nicht kleiner als 200°."), ("360°", "Das ist ein Vollwinkel.")],
    "Überstumpf heißt: größer als der gestreckte Winkel, aber kleiner als der Vollwinkel.",
    "Überstumpf ist ein Winkel zwischen 180° und 360°. Kleiner als 200° kommt nur 190° in Frage.",
    lambda: 180 < 190 < 200 and not 180 < 170 and not 200 < 200 and not 360 < 360), regel=WI)
neu(T, "winkelarten", "anwenden", Z(
    "Ein Türfeststeller kann eine Tür bei den Winkeln 30°, 90°, 100°, 135° oder 180° festhalten. Wie viele dieser Einstellungen sind stumpfe Winkel?",
    2, "2", "1 + 1", "Ein stumpfer Winkel ist größer als 90° und kleiner als 180°.",
    "Stumpf sind nur 100° und 135°. 30° ist spitz, 90° ist ein rechter Winkel, 180° ist ein gestreckter Winkel. Es sind 2.",
    [(3, None, "den gestreckten Winkel 180° mitgezählt", lambda: sum(90 < w <= 180 for w in (30, 90, 100, 135, 180)) == 3), (4, None, "auch 90° und 180° mitgezählt", lambda: sum(90 <= w <= 180 for w in (30, 90, 100, 135, 180)) == 4)], "Einstellungen"), g="transfer", regel=WI)

# ───────── vierecke ─────────
neu(T, "vierecke", "bruecke", W(
    "Die Tabelle beschreibt vier Vierecke A bis D. Welches Viereck ist eine Raute, die kein Quadrat ist?",
    "Viereck B",
    [("Viereck A", "Alle Seiten gleich lang und vier rechte Winkel: das ist ein Quadrat."), ("Viereck C", "Vier rechte Winkel, aber nicht alle Seiten gleich lang: ein Rechteck."), ("Viereck D", "Weder alle Seiten gleich lang noch rechte Winkel: das ist keine Raute.")],
    "Eine Raute hat vier gleich lange Seiten. Ein Quadrat hat zusätzlich vier rechte Winkel.",
    "Eine Raute hat vier gleich lange Seiten. Ein Quadrat hätte zusätzlich vier rechte Winkel. Gesucht ist also: gleich lange Seiten (ja), rechte Winkel (nein). Das ist Viereck B.",
    lambda: True, grafik=TAB(["Viereck", "Alle vier Seiten gleich lang", "Vier rechte Winkel"], ["A", "ja", "ja"], ["B", "ja", "nein"], ["C", "nein", "ja"], ["D", "nein", "nein"])), regel=WI)
neu(T, "vierecke", "anwenden", Z(
    "Ein Beet hat die Form eines Rechtecks mit den Ecken A(−3 | −2), B(5 | −2), C(5 | 3) und D(−3 | 3). Eine Einheit entspricht 1 m. Wie viele Meter Zaun braucht man rund um das Beet?",
    26, "2 * (8 + 5)", "8 + 5 + 8 + 5", "Wie lang sind die Seiten [AB] und [BC]? Eine Koordinate bleibt jeweils gleich.",
    "[AB] hat die Länge 5 − (−3) = 8 m. [BC] hat die Länge 3 − (−2) = 5 m. Rundherum: 2 · (8 + 5) = 26 m.",
    [(13, None, "nur zwei Seiten gezählt (halber Umfang)", "8 + 5"), (40, None, "den Flächeninhalt statt des Umfangs berechnet", "8 * 5"), (18, None, "eine Seite zu wenig gezählt: 8 + 5 + 5", "8 + 5 + 5")], "m"), g="transfer", regel=AB)

# ───────── verstehen ─────────
neu(T, "verstehen", "bruecke", W(
    "Welcher Punkt liegt rechts von der y-Achse und unter der x-Achse?",
    "(3 | −4)",
    [("(−3 | 4)", "Das ist links von der y-Achse und über der x-Achse."), ("(3 | 4)", "Das ist rechts, aber über der x-Achse."), ("(−3 | −4)", "Das ist unter der x-Achse, aber links von der y-Achse.")],
    "Rechts von der y-Achse heißt: x ist positiv. Unter der x-Achse heißt: y ist negativ.",
    "Rechts von der y-Achse ist x > 0, unter der x-Achse ist y < 0. Das trifft nur auf (3 | −4) zu.",
    lambda: [(x > 0 and y < 0) for x, y in ((3, -4), (-3, 4), (3, 4), (-3, -4))] == [True, False, False, False]), regel=KO)
neu(T, "verstehen", "anwenden", W(
    "Ein Schatz liegt links von der y-Achse und unter der x-Achse. Er ist von beiden Achsen gleich weit entfernt, nämlich 6 Einheiten. Welche Koordinaten hat er?",
    "(−6 | −6)",
    [("(6 | −6)", "Das ist rechts von der y-Achse."), ("(−6 | 6)", "Das ist über der x-Achse."), ("(6 | 6)", "Das ist rechts und über den Achsen.")],
    "Links der y-Achse heißt: x ist negativ. Unter der x-Achse heißt: y ist negativ.",
    "Der Abstand von beiden Achsen ist 6, also |x| = 6 und |y| = 6. Links der y-Achse: x = −6. Unter der x-Achse: y = −6. Der Schatz liegt bei (−6 | −6).",
    lambda: [(x < 0 and y < 0 and abs(x) == 6 and abs(y) == 6) for x, y in ((-6, -6), (6, -6), (-6, 6), (6, 6))] == [True, False, False, False]), g="transfer", regel=KO)
