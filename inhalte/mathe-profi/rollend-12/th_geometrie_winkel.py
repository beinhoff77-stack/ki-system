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
    97, "180 - 48 - 35", "(180 - 35) - 48", "Welcher Winkel hängt direkt mit den 48° zusammen? Welcher Schritt kam zuletzt?",
    "Der vergrößerte Winkel ist 180° − 48° = 132°. Vor der Vergrößerung war er 35° kleiner: 132° − 35° = 97°. Probe: 97° + 35° = 132°, 132° + 48° = 180°.",
    [(132, None, "nur den vergrößerten Winkel angegeben", "180 - 48"), (167, None, "die 35° addiert statt abgezogen", "180 - 48 + 35"), (145, None, "die 48° vergessen: 180° − 35°", "180 - 35")], "°"), g="rueckwaerts", regel=WI)

# ───────── kreuzung ─────────
neu(T, "kreuzung", "anwenden", Z(
    "Zwei gerade Straßen kreuzen sich. Einer der vier Winkel zwischen den Straßen beträgt 38°. Wie groß ist der größte der vier Winkel?",
    142, "180 - 38", "90 + 52", "Je zwei benachbarte Winkel ergeben zusammen einen gestreckten Winkel. Gegenüberliegende Winkel sind gleich groß.",
    "Der Nachbarwinkel von 38° ist 180° − 38° = 142°. Die anderen beiden Winkel sind 38° und 142° (gegenüberliegende Winkel sind gleich). Der größte ist 142°.",
    [(38, "fb.winkel.neben_statt_scheitel", "den gegebenen Winkel als größten genannt (Scheitelwinkel statt Nebenwinkel genommen)", "38"), (52, None, "zu einem rechten Winkel ergänzt: 90° − 38°", "90 - 38"), (322, "fb.winkel.teil_der_drehung", "von 360° abgezogen (den falschen Teil der vollen Drehung genommen)", "360 - 38")], "°"), regel=WI)
neu(T, "kreuzung", "zwei_wege", Z(
    "Zwei Geraden schneiden sich. Ein Winkel ist 24° größer als sein Nachbarwinkel. Wie groß ist der größere der beiden Winkel? Weg A: Nenne den kleineren Winkel w und löse w + (w + 24°) = 180°. Weg B: Wären beide Winkel gleich groß, hätte jeder 90°. Überlege, wie viel Grad vom einen zum anderen wandern müssen, damit der Unterschied 24° beträgt.",
    102, "(180 + 24) / 2", "90 + 24 / 2", "Wie groß ist die Summe zweier Nachbarwinkel? Was geschieht mit dem Unterschied, wenn ein Winkel um 12° kleiner und der andere um 12° größer wird?",
    "Weg A: 2w + 24° = 180°, also 2w = 156°, w = 78°. Der größere Winkel ist 78° + 24° = 102°. Weg B: Von 90° und 90° wandern 12° vom einen zum anderen: 78° und 102°. Der Unterschied ist 24°. Probe: 102° + 78° = 180°.",
    [(204, None, "180° und 24° addiert und nicht halbiert", "180 + 24"), (78, None, "den kleineren Winkel genannt", "(180 - 24) / 2"), (156, None, "24° von 180° abgezogen und nicht halbiert", "180 - 24")], "°"), g="verknuepfen", regel=WI)

# ───────── um_punkt ─────────
neu(T, "um_punkt", "bruecke", Z(
    "Ein Kreisdiagramm zeigt, welches Obst eine Klasse am liebsten mag. Die Tabelle nennt die Winkel von drei Sektoren. Der übrige Teil des Kreises heißt „Sonstiges“. Wie groß ist der Winkel des Sektors „Sonstiges“?",
    105, "360 - (120 + 90 + 45)", "360 - 255", "Alle Sektoren zusammen füllen den Vollwinkel. Wie viel Grad sind schon vergeben?",
    "Die drei genannten Sektoren sind zusammen 120° + 90° + 45° = 255° groß. Der Rest bis 360° ist 360° − 255° = 105°.",
    [(255, None, "die Summe der drei Winkel genannt", "120 + 90 + 45"), (150, None, "den Sektor der Trauben vergessen: 360° − 120° − 90°", "360 - 120 - 90"), (195, None, "den Sektor der Bananen vergessen: 360° − 120° − 45°", "360 - 120 - 45")], "°",
    grafik=TAB(["Obst", "Winkel im Kreisdiagramm"], ["Äpfel", "120°"], ["Bananen", "90°"], ["Trauben", "45°"])))
neu(T, "um_punkt", "anwenden", Z(
    "Eine runde Torte wird so aufgeschnitten: Ein Stück hat an der Spitze 90°, ein Stück hat 60°. Der Rest wird in 5 gleich große Stücke geschnitten. Wie groß ist die Spitze eines dieser Reststücke?",
    42, "(360 - 90 - 60) / 5", "210 / 5", "Wie viel Grad bleiben nach den beiden ersten Stücken übrig? Wie teilst du das auf?",
    "Die ersten beiden Stücke haben 90° + 60° = 150°. Es bleiben 360° − 150° = 210°. Auf 5 Stücke verteilt: 210° : 5 = 42°.",
    [(210, None, "den Rest nicht geteilt", "360 - 90 - 60"), (72, None, "den ganzen Kreis durch 5 geteilt", "360 / 5"), (30, None, "nur 150° durch 5 geteilt", "(90 + 60) / 5")], "°"), g="transfer")

# ───────── uhr ─────────
neu(T, "uhr", "zwei_wege", Z(
    "Um wie viel Grad dreht sich der Minutenzeiger einer Uhr in 25 Minuten? Weg A: Bestimme zuerst, um wie viel Grad er sich in 1 Minute dreht, und rechne dann mal 25. Weg B: Zwischen zwei Zahlen auf dem Zifferblatt liegen 5 Minuten. Bestimme den Winkel zwischen zwei Zahlen und überlege, wie oft 5 Minuten in 25 Minuten passen.",
    150, "360 / 60 * 25", "25 / 5 * 30", "Eine ganze Stunde sind 360° für den Minutenzeiger. Wie viele Minuten hat eine Stunde, wie viele Zahlen das Zifferblatt?",
    "Weg A: In 60 Minuten dreht er sich um 360°, in 1 Minute um 6°. 25 · 6° = 150°. Weg B: Zwischen zwei Zahlen liegen 5 Minuten und 360° : 12 = 30°. 25 Minuten sind 5 solche Schritte, 5 · 30° = 150°.",
    [(750, None, "mit 30° pro Minute gerechnet (Stundenabstand statt Minute)", "30 * 25"), (25, None, "die Minuten als Grad angegeben", "25"), (125, None, "mit 5° pro Minute gerechnet", "5 * 25")], "°"))
neu(T, "uhr", "anwenden", Z(
    "Wie groß ist um 7:20 Uhr der kleinere Winkel zwischen Stundenzeiger und Minutenzeiger? Der Stundenzeiger dreht sich in einer Stunde um 30°, der Minutenzeiger in einer Stunde um 360°.",
    100, "(7 * 30 + 20 / 2) - 20 * 6", "220 - 120", "Wo steht der Minutenzeiger, gemessen von der 12 aus? Wie weit ist der Stundenzeiger schon über die 7 hinaus?",
    "Der Minutenzeiger hat nach 20 Minuten 20 · 6° = 120° zurückgelegt. Der Stundenzeiger hat 7 · 30° = 210° und in 20 Minuten noch 20 · 0,5° = 10° mehr, also 220°. Der Unterschied ist 220° − 120° = 100°. Das ist der kleinere Winkel, weil er kleiner als 180° ist.",
    [(90, None, "den Stundenzeiger genau auf der 7 angenommen: 210° − 120°", "7 * 30 - 120"), (110, None, "den Stundenzeiger in den 20 Minuten um 20° statt um 10° weitergedreht: 230° − 120°", "7 * 30 + 20 - 120"), (120, None, "nur den Weg des Minutenzeigers genannt", "20 * 6")], "°"), g="transfer")

# ───────── drehungen ─────────
neu(T, "drehungen", "anwenden", W(
    "Ein Roboter schaut nach Norden. Er dreht sich zuerst um 90° im Uhrzeigersinn und danach um 180° gegen den Uhrzeigersinn. In welche Richtung schaut er danach?",
    "Westen",
    [("Osten", "Nur die erste Drehung wurde beachtet."), ("Süden", "Nur die zweite Drehung wurde beachtet."), ("Norden", "Die beiden Drehungen wurden als gleich groß angesehen und gegeneinander aufgehoben.")],
    "Zeichne dir eine Windrose. Im Uhrzeigersinn geht es von Norden nach Osten.",
    "Norden, 90° im Uhrzeigersinn: Osten. Von Osten 180° gegen den Uhrzeigersinn: Westen.",
    lambda: RI[(0 + 1) % 4] == "Osten" and RI[(1 - 2) % 4] == "Westen" and RI[1] != "Westen" and RI[(0 - 2) % 4] == "Süden"))
neu(T, "drehungen", "zwei_wege", Z(
    "Ein Schiff dreht sich um 90° nach rechts, dann um 45° nach links und danach um 180° nach rechts. Um wie viel Grad insgesamt hat es sich nach rechts gedreht? Weg A: Bestimme nach jeder Drehung die Gesamtdrehung. Weg B: Addiere alle Drehungen nach rechts und ziehe alle nach links ab.",
    225, "90 - 45 + 180", "(90 + 180) - 45", "Links ist das Gegenteil von rechts. Was passiert mit den 45°?",
    "Weg A: Nach der 1. Drehung 90° rechts, nach der 2. 45° rechts, nach der 3. 225° rechts. Weg B: Rechts: 90° + 180° = 270°, links: 45°. 270° − 45° = 225°.",
    [(315, None, "alle Drehungen addiert", "90 + 45 + 180"), (135, None, "die dritte Drehung nach rechts vergessen: 90° + 45°", "90 + 45"), (45, None, "nur die Drehung nach links genannt", "45")], "°"), g="verknuepfen")

# ───────── figuren ─────────
neu(T, "figuren", "bruecke", Z(
    "Die Diagonale eines Quadrats geht durch eine Ecke und teilt den rechten Winkel dort in zwei gleich große Winkel. Wie groß ist jeder dieser beiden Winkel?",
    45, "90 / 2", "180 / 4", "Wie groß ist ein Eckwinkel im Quadrat? In wie viele gleiche Teile wird er geteilt?",
    "Der Eckwinkel im Quadrat ist 90°. Die Diagonale halbiert ihn: 90° : 2 = 45°.",
    [(90, None, "den Eckwinkel genannt", "90"), (22.5, None, "durch 4 statt durch 2 geteilt", "90 / 4"), (180, None, "mit 2 malgenommen", "90 * 2")], "°"))
neu(T, "figuren", "zwei_wege", Z(
    "In einem Rechteck teilt eine Strecke von einer Ecke aus den rechten Winkel in zwei Teile. Der größere Teil ist doppelt so groß wie der kleinere. Wie groß ist der größere Teil? Weg A: Nenne den kleineren Teil w und löse w + 2 · w = 90°. Weg B: Teile den rechten Winkel in 3 gleich große Stücke. Der kleinere Teil ist ein Stück, der größere sind zwei Stücke.",
    60, "90 / 3 * 2", "90 - 90 / 3", "Wie viele gleich große Stücke ergeben zusammen den rechten Winkel? Wie viele davon gehören zum größeren Teil?",
    "Weg A: 3 · w = 90°, also w = 30°. Der größere Teil ist 2 · 30° = 60°. Weg B: Ein Stück ist 90° : 3 = 30° groß, der größere Teil hat zwei Stücke: 60°. Probe: 30° + 60° = 90°.",
    [(30, None, "den kleineren Teil genannt", "90 / 3"), (45, None, "den rechten Winkel nur halbiert", "90 / 2"), (180, None, "mit 2 malgenommen", "90 * 2")], "°"), g="verknuepfen")

# ───────── verstehen ─────────
neu(T, "verstehen", "zwei_wege", Z(
    "Tim behauptet: „Addiert man zwei spitze Winkel, ist die Summe immer ein stumpfer Winkel.“ Bei wie vielen der Paare 20° + 40°, 50° + 60°, 80° + 70°, 30° + 30°, 60° + 85° und 45° + 45° stimmt die Behauptung? Weg A: Rechne jede Summe aus und ordne sie ein. Weg B: Schätze jede Summe und vergleiche sie mit 90° und 180°.",
    3, "3", "1 + 1 + 1", "Ein stumpfer Winkel ist größer als 90° und kleiner als 180°. Ist 90° selbst stumpf?",
    "Weg A: Die Summen sind 60°, 110°, 150°, 60°, 145° und 90°. Stumpf, also größer als 90° und kleiner als 180°, sind 110°, 150° und 145°. Die Summe 90° ist ein rechter Winkel, 60° ist spitz. Weg B: Die Summe zweier Winkel unter 90° ist immer kleiner als 180°, entscheidend ist nur, ob sie über 90° liegt. Es sind 3 Paare.",
    [(4, None, "den rechten Winkel 90° als stumpf mitgezählt", lambda: sum(a + b >= 90 for a, b in ((20, 40), (50, 60), (80, 70), (30, 30), (60, 85), (45, 45))) == 4), (6, None, "alle Paare gezählt, weil die Summe immer größer als jeder Summand ist", "3 + 3")], "Paare"))
neu(T, "verstehen", "umkehren", Z(
    "Tim behauptet: „Wenn man einen Winkel verdoppelt und dann 20° dazuzählt, entsteht ein gestreckter Winkel.“ Für welchen Winkel stimmt Tims Aussage?",
    80, "(180 - 20) / 2", "180 / 2 - 10", "Wie ist der gestreckte Winkel entstanden? Welcher Schritt war der letzte?",
    "Rückwärts: Erst 20° abziehen: 180° − 20° = 160°. Dann das Verdoppeln rückgängig machen: 160° : 2 = 80°. Probe: 2 · 80° + 20° = 180°.",
    [(160, None, "nur die 20° abgezogen, das Verdoppeln nicht rückgängig gemacht", "180 - 20"), (90, None, "die 20° vergessen", "180 / 2"), (100, None, "die 20° addiert und halbiert statt abgezogen", "(180 + 20) / 2")], "°"), g="rueckwaerts")
