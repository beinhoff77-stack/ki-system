T = "geometrie.winkel"
WI = "id.geometrie.winkel"
RI = ["Norden", "Osten", "Süden", "Westen"]

# ───────── ergaenzen ─────────
neu(T, "ergaenzen", "zwei_wege", Z(
    "Welcher Winkel ergänzt 62° zu einem gestreckten Winkel? Weg A: Ziehe 62° von 180° ab. Weg B: Ergänze 62° zuerst zu einem rechten Winkel und füge dann noch einen rechten Winkel hinzu.",
    118, "180 - 62", "(90 - 62) + 90", "Ein gestreckter Winkel besteht aus zwei rechten Winkeln.",
    "Weg A: 180° − 62° = 118°. Weg B: 90° − 62° = 28° bis zum rechten Winkel, dazu noch 90°: 28° + 90° = 118°.",
    [(28, None, "nur bis zum rechten Winkel ergänzt", "90 - 62"), (242, None, "62° zu 180° addiert", "180 + 62"), (108, None, "von 170° statt von 180° abgezogen", "170 - 62")], "°"), regel=WI)
neu(T, "ergaenzen", "umkehren", Z(
    "Ein Winkel wird um 35° vergrößert. Der vergrößerte Winkel ergänzt einen Winkel von 48° zu einem gestreckten Winkel. Wie groß war der Winkel vor der Vergrößerung?",
    97, "180 - 48 - 35", "(180 - 35) - 48", "Wie groß ist der vergrößerte Winkel? Mache dann die Vergrößerung rückgängig.",
    "Der vergrößerte Winkel ist 180° − 48° = 132°. Vor der Vergrößerung war er 35° kleiner: 132° − 35° = 97°. Probe: 97° + 35° = 132°, 132° + 48° = 180°.",
    [(132, None, "nur den vergrößerten Winkel angegeben", "180 - 48"), (167, None, "die 35° addiert statt abgezogen", "180 - 48 + 35"), (145, None, "die 48° vergessen: 180° − 35°", "180 - 35")], "°"), g="rueckwaerts", regel=WI)

# ───────── kreuzung ─────────
neu(T, "kreuzung", "anwenden", Z(
    "Zwei gerade Straßen kreuzen sich. Einer der vier Winkel zwischen den Straßen beträgt 38°. Wie groß ist der größte der vier Winkel?",
    142, "180 - 38", "90 + 52", "Je zwei benachbarte Winkel ergeben zusammen einen gestreckten Winkel. Gegenüberliegende Winkel sind gleich groß.",
    "Der Nachbarwinkel von 38° ist 180° − 38° = 142°. Die anderen beiden Winkel sind 38° und 142° (gegenüberliegende Winkel sind gleich). Der größte ist 142°.",
    [(38, None, "den gegebenen Winkel als größten genannt", "38"), (52, None, "zu einem rechten Winkel ergänzt: 90° − 38°", "90 - 38"), (322, None, "von 360° abgezogen", "360 - 38")], "°"), regel=WI)
neu(T, "kreuzung", "zwei_wege", Z(
    "Zwei Geraden schneiden sich. Ein Winkel ist 24° größer als sein Nachbarwinkel. Wie groß ist der größere der beiden Winkel? Weg A: Rechne (180° + 24°) : 2. Weg B: Rechne zuerst den kleineren Winkel mit (180° − 24°) : 2 und addiere dann 24°.",
    102, "(180 + 24) / 2", "(180 - 24) / 2 + 24", "Zwei Nachbarwinkel ergeben zusammen 180°. Der Unterschied ist 24°.",
    "Weg A: (180 + 24) : 2 = 204 : 2 = 102. Weg B: (180 − 24) : 2 = 78 ist der kleinere Winkel, 78 + 24 = 102. Probe: 102° + 78° = 180°.",
    [(204, None, "180° und 24° addiert und nicht halbiert", "180 + 24"), (78, None, "den kleineren Winkel genannt", "(180 - 24) / 2"), (156, None, "24° von 180° abgezogen und nicht halbiert", "180 - 24")], "°"), g="verknuepfen", regel=WI)

# ───────── um_punkt ─────────
neu(T, "um_punkt", "bruecke", Z(
    "Ein Kreisdiagramm zeigt, welches Obst eine Klasse am liebsten mag. Die Tabelle nennt die Winkel von drei Sektoren. Der übrige Teil des Kreises heißt „Sonstiges“. Wie groß ist der Winkel des Sektors „Sonstiges“?",
    105, "360 - (120 + 90 + 45)", "360 - 255", "Alle Sektoren zusammen füllen den Vollwinkel. Wie viel Grad sind schon vergeben?",
    "Die drei genannten Sektoren sind zusammen 120° + 90° + 45° = 255° groß. Der Rest bis 360° ist 360° − 255° = 105°.",
    [(255, None, "die Summe der drei Winkel genannt", "120 + 90 + 45"), (75, None, "von 330° statt von 360° abgezogen", "330 - 255"), (225, None, "von 480° abgezogen", "480 - 255")], "°",
    grafik=TAB(["Obst", "Winkel im Kreisdiagramm"], ["Äpfel", "120°"], ["Bananen", "90°"], ["Trauben", "45°"])), regel=WI)
neu(T, "um_punkt", "anwenden", Z(
    "Eine runde Torte wird so aufgeschnitten: Ein Stück hat an der Spitze 90°, ein Stück hat 60°. Der Rest wird in 5 gleich große Stücke geschnitten. Wie groß ist die Spitze eines dieser Reststücke?",
    42, "(360 - 90 - 60) / 5", "210 / 5", "Wie viel Grad bleiben nach den beiden ersten Stücken übrig? Wie teilst du das auf?",
    "Die ersten beiden Stücke haben 90° + 60° = 150°. Es bleiben 360° − 150° = 210°. Auf 5 Stücke verteilt: 210° : 5 = 42°.",
    [(210, None, "den Rest nicht geteilt", "360 - 90 - 60"), (72, None, "den ganzen Kreis durch 5 geteilt", "360 / 5"), (30, None, "nur 150° durch 5 geteilt", "(90 + 60) / 5")], "°"), g="transfer", regel=WI)

# ───────── uhr ─────────
neu(T, "uhr", "zwei_wege", Z(
    "Um wie viel Grad dreht sich der Minutenzeiger einer Uhr in 25 Minuten? Weg A: Bestimme zuerst, um wie viel Grad er sich in 1 Minute dreht, und rechne dann mal 25. Weg B: Überlege, welchen Bruchteil einer Stunde 25 Minuten ausmachen, und nimm diesen Bruchteil von 360°.",
    150, "360 / 60 * 25", "360 * 25 / 60", "Eine ganze Stunde sind 360° für den Minutenzeiger. Wie viele Minuten hat eine Stunde?",
    "Weg A: In 60 Minuten dreht er sich um 360°, in 1 Minute um 6°. 25 · 6° = 150°. Weg B: 25 Minuten sind 25/60 einer Stunde, 25/60 von 360° sind 150°.",
    [(750, None, "mit 30° pro Minute gerechnet (Stundenabstand statt Minute)", "30 * 25"), (25, None, "die Minuten als Grad angegeben", "25"), (125, None, "mit 5° pro Minute gerechnet", "5 * 25")], "°"), regel=WI)
neu(T, "uhr", "anwenden", Z(
    "Wie groß ist um 3:30 Uhr der kleinere Winkel zwischen Stundenzeiger und Minutenzeiger? Beachte: Der Stundenzeiger dreht sich in einer Stunde um 30°. Um 3:30 Uhr steht er genau in der Mitte zwischen der 3 und der 4.",
    75, "180 - (3 * 30 + 15)", "(4 * 30 - 15) - 30 + 30 - 30", "Wie weit ist der Stundenzeiger von der 12 entfernt gedreht? Der Minutenzeiger steht auf der 6.",
    "Der Minutenzeiger steht bei 180° (auf der 6). Der Stundenzeiger steht bei 3 · 30° + 15° = 105°. Der Unterschied ist 180° − 105° = 75°.",
    [(90, None, "den Stundenzeiger genau auf der 3 angenommen: 180° − 90°", "180 - 90"), (105, None, "den Winkel des Stundenzeigers genannt", "3 * 30 + 15"), (60, None, "den Stundenzeiger bei 120° angenommen", "180 - 120")], "°"), g="transfer", regel=WI)

# ───────── drehungen ─────────
neu(T, "drehungen", "anwenden", W(
    "Ein Roboter schaut nach Norden. Er dreht sich zuerst um 90° im Uhrzeigersinn und danach um 180° gegen den Uhrzeigersinn. In welche Richtung schaut er danach?",
    "Westen",
    [("Osten", "Nur die erste Drehung wurde beachtet."), ("Süden", "Nur die zweite Drehung wurde beachtet."), ("Norden", "Beide Drehungen wurden rückgängig gemacht.")],
    "Zeichne dir eine Windrose. Im Uhrzeigersinn geht es von Norden nach Osten.",
    "Norden, 90° im Uhrzeigersinn: Osten. Von Osten 180° gegen den Uhrzeigersinn: Westen.",
    lambda: RI[(0 + 1) % 4] == "Osten" and RI[(1 - 2) % 4] == "Westen" and RI[1] != "Westen" and RI[(0 - 2) % 4] == "Süden"), regel=WI)
neu(T, "drehungen", "zwei_wege", Z(
    "Ein Schiff dreht sich um 90° nach rechts, dann um 45° nach links und danach um 180° nach rechts. Um wie viel Grad insgesamt hat es sich nach rechts gedreht? Weg A: Bestimme nach jeder Drehung die Gesamtdrehung. Weg B: Addiere alle Drehungen nach rechts und ziehe alle nach links ab.",
    225, "90 - 45 + 180", "(90 + 180) - 45", "Links ist das Gegenteil von rechts. Was passiert mit den 45°?",
    "Weg A: Nach der 1. Drehung 90° rechts, nach der 2. 45° rechts, nach der 3. 225° rechts. Weg B: Rechts: 90° + 180° = 270°, links: 45°. 270° − 45° = 225°.",
    [(315, None, "alle Drehungen addiert", "90 + 45 + 180"), (135, None, "die dritte Drehung nach rechts vergessen: 90° + 45°", "90 + 45"), (45, None, "nur die Drehung nach links genannt", "45")], "°"), g="verknuepfen", regel=WI)

# ───────── figuren ─────────
neu(T, "figuren", "bruecke", Z(
    "Die Diagonale eines Quadrats geht durch eine Ecke und teilt den rechten Winkel dort in zwei gleich große Winkel. Wie groß ist jeder dieser beiden Winkel?",
    45, "90 / 2", "180 / 4", "Wie groß ist ein Eckwinkel im Quadrat? In wie viele gleiche Teile wird er geteilt?",
    "Der Eckwinkel im Quadrat ist 90°. Die Diagonale halbiert ihn: 90° : 2 = 45°.",
    [(90, None, "den Eckwinkel genannt", "90"), (22.5, None, "durch 4 statt durch 2 geteilt", "90 / 4"), (180, None, "mit 2 malgenommen", "90 * 2")], "°"), regel=WI)
neu(T, "figuren", "zwei_wege", Z(
    "In einem Rechteck teilt eine Strecke von einer Ecke aus den rechten Winkel im Verhältnis 2 zu 3. Wie groß ist der größere der beiden Teilwinkel? Weg A: Berechne zuerst den kleineren Teil (zwei Fünftel von 90°) und ziehe ihn von 90° ab. Weg B: Berechne den größeren Teil direkt als drei Fünftel von 90°.",
    54, "90 - 90 / 5 * 2", "90 / 5 * 3", "Das Verhältnis 2 zu 3 teilt den Winkel in 5 gleiche Teile.",
    "Weg A: Der kleinere Teil ist 90° : 5 · 2 = 36°. 90° − 36° = 54°. Weg B: 90° : 5 · 3 = 18° · 3 = 54°.",
    [(36, None, "den kleineren Teil genannt", "90 / 5 * 2"), (18, None, "nur ein Fünftel genannt", "90 / 5"), (60, None, "durch 3 statt durch 5 geteilt und mit 2 malgenommen", "90 / 3 * 2")], "°"), g="verknuepfen", regel=WI)

# ───────── verstehen ─────────
neu(T, "verstehen", "zwei_wege", Z(
    "Wie viele Winkel von je 30° passen zusammen in einen Vollwinkel? Weg A: Teile 360° durch 30°. Weg B: Denke an das Zifferblatt einer Uhr: Zwischen zwei Stundenzeichen liegen 30°.",
    12, "360 / 30", "12", "Wie viele Stundenzeichen hat ein Zifferblatt?",
    "Weg A: 360° : 30° = 12. Weg B: Das Zifferblatt hat 12 Stundenzeichen im Abstand von 30°. Es passen 12 Winkel hinein.",
    [(6, None, "den halben Vollwinkel geteilt", "180 / 30"), (11, None, "eine Stelle zu wenig gezählt", "360 / 30 - 1"), (330, None, "30° von 360° abgezogen", "360 - 30")]), regel=WI)
neu(T, "verstehen", "umkehren", Z(
    "Ein Winkel wird verdoppelt, dann werden 20° dazugezählt. Das Ergebnis ist ein gestreckter Winkel. Wie groß war der Winkel am Anfang?",
    80, "(180 - 20) / 2", "180 / 2 - 10", "Mache die Schritte in umgekehrter Reihenfolge rückgängig. Was war der letzte Schritt?",
    "Rückwärts: Erst 20° abziehen: 180° − 20° = 160°. Dann das Verdoppeln rückgängig machen: 160° : 2 = 80°. Probe: 2 · 80° + 20° = 180°.",
    [(160, None, "nur die 20° abgezogen, das Verdoppeln nicht rückgängig gemacht", "180 - 20"), (90, None, "die 20° vergessen", "180 / 2"), (100, None, "die 20° addiert und halbiert statt abgezogen", "(180 + 20) / 2")], "°"), g="rueckwaerts", regel=WI)
