T = "geometrie.winkel"
WI = "id.geometrie.winkel"
RI = ["Norden", "Osten", "Süden", "Westen"]

# ───────── ergaenzen ─────────
neu(T, "ergaenzen", "zwei_wege", Z(
    "Weg A: Ziehe 62° von 180° ab. Weg B: Ergänze 62° zuerst zu einem rechten Winkel und füge dann noch einen rechten Winkel hinzu. Welcher Winkel ergänzt 62° zu einem gestreckten Winkel?",
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
    "Zwei Geraden schneiden sich. Ein Winkel ist 24° größer als sein Nachbarwinkel. Weg A: Nenne den kleineren Winkel w und löse w + (w + 24°) = 180°. Weg B: Wären beide Winkel gleich groß, hätte jeder 90°. Überlege, wie viel Grad vom einen zum anderen wandern müssen, damit der Unterschied 24° beträgt. Wie groß ist der größere Winkel?",
    102, "(180 + 24) / 2", "90 + 24 / 2", "Wie groß ist die Summe zweier Nachbarwinkel? Was geschieht mit dem Unterschied, wenn ein Winkel kleiner und der andere um genauso viel größer wird?",
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
    "Betrachte den Minutenzeiger einer Uhr und eine Zeitspanne von 20 Minuten. Weg A: Bestimme zuerst, um wie viel Grad er sich in 1 Minute dreht, und rechne dann mal 20. Weg B: Zwischen zwei Zahlen auf dem Zifferblatt liegen 5 Minuten. Bestimme den Winkel zwischen zwei Zahlen und überlege, wie oft 5 Minuten in 20 Minuten passen. Gib an, um wie viel Grad sich der Minutenzeiger in 20 Minuten dreht.",
    120, "360 / 60 * 20", "20 / 5 * 30", "Eine ganze Stunde sind 360° für den Minutenzeiger. Wie viele Minuten hat eine Stunde, wie viele Zahlen das Zifferblatt?",
    "Weg A: In 60 Minuten dreht er sich um 360°, in 1 Minute um 6°. 20 · 6° = 120°. Weg B: Zwischen zwei Zahlen liegen 5 Minuten und 360° : 12 = 30°. 20 Minuten sind 4 solche Schritte, 4 · 30° = 120°.",
    [(600, None, "mit 30° pro Minute gerechnet (Stundenabstand statt Minute)", "30 * 20"), (20, None, "die Minuten als Grad angegeben", "20"), (100, None, "mit 5° pro Minute gerechnet", "5 * 20")], "°"))
neu(T, "uhr", "anwenden", Z(
    "Die Uhr am Bahnhof zeigt 2:50 Uhr. Der Stundenzeiger dreht sich in einer Stunde um 30°, der Minutenzeiger in einer Stunde um 360°. Beide Zeiger starten um 12:00 Uhr bei der 12. Wie groß ist der kleinere Winkel zwischen Stundenzeiger und Minutenzeiger?",
    145, "360 - (50 * 6 - (2 * 30 + 50 / 2))", "360 - 215", "Beide Zeiger bewegen sich weiter, auch der kurze. Rechne für jeden Zeiger den Winkel von der 12 aus.",
    "Der Minutenzeiger hat nach 50 Minuten 50 · 6° = 300° zurückgelegt. Der Stundenzeiger hat 2 · 30° = 60° und in 50 Minuten noch 50 · 0,5° = 25° mehr, also 85°. Der Unterschied ist 300° − 85° = 215°. Das ist größer als 180°, der kleinere Winkel ist 360° − 215° = 145°.",
    [(120, None, "den Stundenzeiger genau auf der 2 angenommen: 300° − 60° = 240°, kleinerer Winkel 360° − 240°", "360 - (300 - 60)"), (170, None, "den Stundenzeiger in den 50 Minuten um 50° statt um 25° weitergedreht: 300° − 110° = 190°, kleinerer Winkel 360° − 190°", "360 - (300 - 110)"), (215, None, "den größeren statt den kleineren Winkel genommen: 300° − 85°", "300 - 85")], "°"), g="transfer")

# ───────── drehungen ─────────
neu(T, "drehungen", "anwenden", W(
    "Ein Roboter schaut nach Norden. Er dreht sich zuerst um 90° im Uhrzeigersinn und danach um 180° gegen den Uhrzeigersinn. In welche Richtung schaut er danach?",
    "Westen",
    [("Osten", "Nur die erste Drehung wurde beachtet."), ("Süden", "Nur die zweite Drehung wurde beachtet."), ("Norden", "Die beiden Drehungen wurden als gleich groß angesehen und gegeneinander aufgehoben.")],
    "Zeichne dir eine Windrose. Im Uhrzeigersinn geht es von Norden nach Osten.",
    "Norden, 90° im Uhrzeigersinn: Osten. Von Osten 180° gegen den Uhrzeigersinn: Westen.",
    lambda: RI[(0 + 1) % 4] == "Osten" and RI[(1 - 2) % 4] == "Westen" and RI[1] != "Westen" and RI[(0 - 2) % 4] == "Süden"))
neu(T, "drehungen", "zwei_wege", Z(
    "Ein Schiff dreht sich um 90° nach rechts, dann um 45° nach links und danach um 180° nach rechts. Weg A: Rechne mit Grad: Bestimme nach jeder Drehung die Gesamtdrehung. Weg B: Zähle auf der Windrose in Schritten von 45° (Abstand zweier Nachbarrichtungen): Wie viele Schritte sind es nach rechts, wie viele nach links? Gib die resultierende Drehung (netto nach rechts) in Grad an.",
    225, "90 - 45 + 180", "(2 - 1 + 4) * 45", "Eine Drehung nach links macht eine Drehung nach rechts zum Teil rückgängig.",
    "Weg A: Nach der 1. Drehung 90° rechts, nach der 2. 45° rechts, nach der 3. 225° rechts. Weg B: 90° sind 2 Schritte nach rechts, 45° ist 1 Schritt nach links, 180° sind 4 Schritte nach rechts. Insgesamt 2 − 1 + 4 = 5 Schritte nach rechts. 5 · 45° = 225°.",
    [(315, None, "alle Drehungen addiert", "90 + 45 + 180"), (135, None, "die letzte Drehung weggelassen und die Linksdrehung addiert: 90° + 45°", "90 + 45"), (45, None, "nur die Drehung nach links genannt", "45")], "°"), g="verknuepfen")

# ───────── figuren ─────────
FIG = {"typ": "figur", "punkte": {"A": [0, 0], "B": [7, 0], "C": [7, 7], "D": [0, 7], "E": [7, 3.264], "F": [4.041, 7]}, "flaeche": ["A", "B", "C", "D"],
       "linien": [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"], ["A", "E"], ["A", "F"]], "winkel": [["A", "B", "E", "25°"], ["A", "F", "D", "30°"], ["A", "E", "F", "?"]]}
neu(T, "figuren", "bruecke", Z(
    "Die Zeichnung zeigt ein Rechteck ABCD. Von der Ecke A gehen die Strecken [AE] und [AF] aus. Eingetragen sind ∠BAE = 25° und ∠FAD = 30°. Wie groß ist ∠EAF?",
    35, "90 - 25 - 30", "90 - (25 + 30)", "Wie groß ist der Winkel bei A im Rechteck? Welche drei Winkel füllen ihn zusammen aus?",
    "Der Eckwinkel des Rechtecks bei A ist 90°. Er besteht aus ∠BAE = 25°, ∠EAF und ∠FAD = 30°. Also ∠EAF = 90° − 25° − 30° = 35°. Probe: 25° + 35° + 30° = 90°.",
    [(55, None, "die beiden gegebenen Winkel addiert: 25° + 30°", "25 + 30"), (65, None, "nur die 25° von 90° abgezogen", "90 - 25"), (60, None, "nur die 30° von 90° abgezogen", "90 - 30")], "°", grafik=FIG))
neu(T, "figuren", "zwei_wege", Z(
    "In einem Rechteck gehen von einer Ecke aus zwei Strecken, die den rechten Winkel in drei Teile teilen. Der mittlere Teil ist 10° größer als der kleinste, der größte Teil ist 10° größer als der mittlere. Weg A: Nenne den kleinsten Teil k und löse k + (k + 10°) + (k + 20°) = 90°. Weg B: Wären alle drei Teile gleich groß, hätte jeder 30°. Überlege, wie der mittlere Teil dazu liegt und wie viel der größte Teil mehr hat. Gib die Größe des größten Teils an.",
    40, "90 / 3 + 10", "(90 - 30) / 3 + 20", "Wie groß wäre jeder Teil bei gleich großen Teilen? Was passiert mit den Unterschieden von 10° nach unten und nach oben?",
    "Weg A: 3k + 30° = 90°, also 3k = 60° und k = 20°. Die Teile sind 20°, 30° und 40°. Der größte Teil ist 40°. Weg B: Der kleinste Teil ist 10° kleiner als der mittlere, der größte 10° größer. Die Unterschiede gleichen sich aus, der mittlere Teil ist also 90° : 3 = 30° groß und der größte 30° + 10° = 40°. Probe: 20° + 30° + 40° = 90°.",
    [(30, None, "den mittleren Teil genannt", "90 / 3"), (20, None, "den kleinsten Teil genannt", "90 / 3 - 10"), (50, None, "den größten Teil um 20° statt um 10° größer als den mittleren genommen", "90 / 3 + 20")], "°"), g="verknuepfen")

# ───────── verstehen ─────────
neu(T, "verstehen", "zwei_wege", Z(
    "Tim behauptet: „Addiert man zwei spitze Winkel, ist die Summe immer ein stumpfer Winkel.“ Betrachte die Paare 20° + 40°, 50° + 60°, 80° + 70°, 30° + 30°, 60° + 85° und 45° + 45°. Weg A: Rechne jede Summe aus und ordne sie ein. Weg B: Ergänze den ersten Winkel zu 90° und vergleiche mit dem zweiten Winkel. Gib die Zahl der Paare an, bei denen die Behauptung stimmt.",
    3, "3", "1 + 1 + 1", "Ein stumpfer Winkel ist größer als 90° und kleiner als 180°. Ist 90° selbst stumpf?",
    "Weg A: Die Summen sind 60°, 110°, 150°, 60°, 145° und 90°. Stumpf, also größer als 90° und kleiner als 180°, sind 110°, 150° und 145°. Die Summe 90° ist ein rechter Winkel, 60° ist spitz. Weg B: Bei 20° fehlen 70° bis 90° und 40° ist weniger, die Summe bleibt unter 90°. Bei 50° fehlen 40° und 60° ist mehr: stumpf. Bei 80° fehlen 10° und 70° ist mehr: stumpf. Bei 30° fehlen 60° und 30° ist weniger: spitz. Bei 60° fehlen 30° und 85° ist mehr: stumpf. Bei 45° fehlen 45° und 45° ist genau so viel: rechter Winkel. Zwei spitze Winkel ergeben immer weniger als 180°. Es sind 3 Paare.",
    [(4, None, "den rechten Winkel 90° als stumpf mitgezählt", lambda: sum(a + b >= 90 for a, b in ((20, 40), (50, 60), (80, 70), (30, 30), (60, 85), (45, 45))) == 4), (6, None, "alle Paare gezählt, weil die Summe immer größer als jeder Summand ist", "3 + 3")], "Paare"))
neu(T, "verstehen", "umkehren", Z(
    "Tim behauptet: „Wenn man einen Winkel verdoppelt und dann 20° dazuzählt, entsteht ein gestreckter Winkel.“ Für welchen Winkel stimmt Tims Aussage?",
    80, "(180 - 20) / 2", "180 / 2 - 10", "Wie ist der gestreckte Winkel entstanden? Welcher Schritt war der letzte?",
    "Rückwärts: Erst 20° abziehen: 180° − 20° = 160°. Dann das Verdoppeln rückgängig machen: 160° : 2 = 80°. Probe: 2 · 80° + 20° = 180°.",
    [(160, None, "nur die 20° abgezogen, das Verdoppeln nicht rückgängig gemacht", "180 - 20"), (90, None, "die 20° vergessen", "180 / 2"), (100, None, "die 20° addiert und halbiert statt abgezogen", "(180 + 20) / 2")], "°"), g="rueckwaerts")
