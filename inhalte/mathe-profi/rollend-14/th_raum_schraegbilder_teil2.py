T = "raum.schraegbilder_teil2"
# ───────── koordinaten ─────────
a1(T, "koordinaten", Z(
    "Ein Zimmer hat die Form eines Quaders. Die Ecke A liegt im Ursprung (0 | 0 | 0). Das Zimmer ist 6 m lang (x-Richtung), 3 m breit (y-Richtung) und 4 m hoch (z-Richtung). Die Ecke G liegt A genau gegenüber, an der Decke. Wie groß ist die Summe der drei Koordinaten von G?",
    13, "6 + 3 + 4", "4 + 3 + 6", "Wie weit ist G von A entfernt, in x-, in y- und in z-Richtung?",
    "G liegt 6 m in x-Richtung, 3 m in y-Richtung und 4 m in z-Richtung von A entfernt. Also G(6 | 3 | 4). Die Summe ist 6 + 3 + 4 = 13.",
    [(9, None, "die z-Koordinate vergessen: nur 6 und 3 addiert", "6 + 3"), (72, None, "das Volumen des Zimmers statt der Koordinatensumme angegeben", "6 * 3 * 4"), (22, None, "die Längen in x- und y-Richtung malgenommen und die Höhe addiert", "6 * 3 + 4")]))
a2(T, "koordinaten", Z(
    "Ein Quader ABCDEFGH hat die Ecken A(1 | 2 | 0), B(7 | 2 | 0), D(1 | 5 | 0) und E(1 | 2 | 4). Seine Kanten verlaufen parallel zu den Achsen. M ist der Mittelpunkt des ganzen Quaders. Wie groß ist die Summe der drei Koordinaten von M? Gib das Ergebnis als Dezimalzahl an.",
    9.5, "(1 + 7) / 2 + (2 + 5) / 2 + (0 + 4) / 2", "4 + 3.5 + 2", "Der Mittelpunkt liegt in jeder Richtung genau in der Mitte zwischen der kleinsten und der größten Koordinate. Welche Ecke liegt A gegenüber?",
    "Die Ecke G liegt A gegenüber: G(7 | 5 | 4). M ist die Mitte von A und G: x = (1 + 7) : 2 = 4, y = (2 + 5) : 2 = 3,5, z = (0 + 4) : 2 = 2. Also M(4 | 3,5 | 2). Die Summe ist 4 + 3,5 + 2 = 9,5.",
    [(7.5, None, "den Mittelpunkt der Grundfläche genommen: z-Koordinate 0", "4 + 3.5 + 0"), (16, None, "die Ecke G statt des Mittelpunkts genommen", "7 + 5 + 4"), (6.5, None, "die Verschiebung von A vergessen: Mitte der Kantenlängen 3, 1,5 und 2", "3 + 1.5 + 2")]))
a3(T, "koordinaten", Z(
    "Ein Quader steht auf dem Boden (der xy-Ebene) mit der Ecke A im Ursprung und ragt nach oben. Seine Kanten verlaufen parallel zu den Achsen. Die Ecke G, die A gegenüberliegt, hat die Koordinaten (8 | 6 | h). Das Volumen ist 240 Volumeneinheiten. Ein zweiter Quader hat dieselbe Grundfläche, ist aber doppelt so hoch. Wie groß ist die Summe der drei Koordinaten seiner Ecke G′, die A gegenüberliegt?",
    24, "8 + 6 + 2 * (240 / (8 * 6))", "14 + 10", "Berechne zuerst h aus dem Volumen. Die Koordinaten von G′ sind die Kantenlängen des zweiten Quaders.",
    "Die Kanten sind 8, 6 und h lang. Das Volumen ist 8 · 6 · h = 240, also h = 5. Der zweite Quader ist 2 · 5 = 10 hoch, also G′(8 | 6 | 10). Die Summe ist 8 + 6 + 10 = 24.",
    [(19, None, "die Höhe des ersten Quaders statt der doppelten Höhe genommen", "8 + 6 + 240 / (8 * 6)"), (38, None, "alle drei Koordinaten des ersten Quaders verdoppelt", "2 * (8 + 6 + 240 / (8 * 6))"), (74, None, "das Volumen nur durch 8 geteilt und verdoppelt", "8 + 6 + 2 * 240 / 8")]), g="rueckwaerts")
# ───────── rotation ─────────
a1(T, "rotation", Z(
    "Ein Töpfer stellt sich vor, dass ein Rechteck mit den Seiten 4 cm und 9 cm um die 9-cm-Seite rotiert. Es entsteht ein Zylinder. Wie groß ist sein Volumen in cm³? Rechne mit π ≈ 3,14.",
    452.16, "3.14 * 4 ** 2 * 9", "3.14 * 144", "Welche Seite liegt auf der Drehachse? Die andere Seite wird zum Radius des Kreises.",
    "Die 9-cm-Seite liegt auf der Achse und wird die Höhe, die 4-cm-Seite wird der Radius. V = π · r² · h ≈ 3,14 · 16 · 9 = 452,16 cm³.",
    [(1017.36, None, "Radius und Höhe vertauscht: r = 9 cm und h = 4 cm", "3.14 * 9 ** 2 * 4"), (1808.64, None, "den Durchmesser 8 cm statt des Radius 4 cm quadriert", "3.14 * 8 ** 2 * 9"), (113.04, None, "den Radius nicht quadriert", "3.14 * 4 * 9")], "cm³"))
a2(T, "rotation", Z(
    "Ein Rechteck mit den Seiten 5 cm und 8 cm dreht sich einmal um die 8-cm-Seite und einmal um die 5-cm-Seite. So entstehen zwei verschiedene Zylinder. Um wie viele Kubikzentimeter ist der größere Zylinder größer als der kleinere? Rechne mit π ≈ 3,14.",
    376.8, "3.14 * 8 ** 2 * 5 - 3.14 * 5 ** 2 * 8", "3.14 * 120", "Berechne beide Volumina. Beachte, welche Seite jeweils zum Radius und welche zur Höhe wird.",
    "Um die 8-cm-Seite: r = 5 cm, h = 8 cm, V = 3,14 · 25 · 8 = 628 cm³. Um die 5-cm-Seite: r = 8 cm, h = 5 cm, V = 3,14 · 64 · 5 = 1 004,8 cm³. Unterschied: 1 004,8 − 628 = 376,8 cm³.",
    [(628, None, "nur das Volumen des kleineren Zylinders angegeben", "3.14 * 5 ** 2 * 8"), (1004.8, None, "nur das Volumen des größeren Zylinders angegeben", "3.14 * 8 ** 2 * 5"), (1632.8, None, "beide Volumina addiert statt den Unterschied zu bilden", "3.14 * 8 ** 2 * 5 + 3.14 * 5 ** 2 * 8")], "cm³"))
a3(T, "rotation", Z(
    "Ein Rechteck dreht sich um eine Seite, die 8 cm lang ist. Der entstehende Zylinder hat das Volumen 226,08 cm³. Rechne mit π ≈ 3,14. Wie breit ist das Rechteck in Zentimetern?",
    3, "wurzel(226.08 / 3.14 / 8)", "3", "Die gesuchte Breite wird beim Drehen zum Radius. Stelle die Volumenformel nach r² um.",
    "Die 8-cm-Seite wird die Höhe, die gesuchte Breite wird der Radius r. Aus 3,14 · r² · 8 = 226,08 folgt r² = 226,08 : 25,12 = 9. Also ist r = 3 cm. Probe: 3,14 · 9 · 8 = 226,08.",
    [(9, None, "die Wurzel nicht gezogen: r² als Breite angegeben", "226.08 / 3.14 / 8"), (28.26, None, "das Volumen nur durch die Höhe geteilt", "226.08 / 8"), (72, None, "das Volumen nur durch 3,14 geteilt", "226.08 / 3.14")], "cm"), g="rueckwaerts")
# ───────── axialschnitt ─────────
a1(T, "axialschnitt", Z(
    "Eine Eiswaffel hat die Form eines Kegels mit dem Radius 3 cm und der Höhe 12 cm. Sam schneidet sie der Länge nach genau durch die Achse. Wie groß ist die Fläche der Schnittfläche in cm²?",
    36, "6 * 12 / 2", "3 * 12", "Der Axialschnitt eines Kegels ist ein Dreieck. Wie lang ist seine Grundseite, und wie hoch ist es?",
    "Der Axialschnitt ist ein gleichschenkliges Dreieck. Die Grundseite ist der Durchmesser 2 · 3 = 6 cm, die Höhe ist 12 cm. A = 6 · 12 : 2 = 36 cm².",
    [(72, None, "das Dreieck wie ein Rechteck berechnet: Durchmesser mal Höhe", "6 * 12"), (18, None, "mit dem Radius 3 cm statt des Durchmessers als Grundseite gerechnet", "3 * 12 / 2"), (24, None, "durch 3 statt durch 2 geteilt, wie bei einem Volumen", "6 * 12 / 3")], "cm²"))
a2(T, "axialschnitt", Z(
    "Eine Holzkugel wird genau durch ihren Mittelpunkt in zwei Hälften gesägt. Der Umfang der Schnittfläche ist 62,8 cm. Rechne mit π ≈ 3,14. Wie groß ist die Fläche der Schnittfläche in cm²?",
    314, "3.14 * (62.8 / (2 * 3.14)) ** 2", "3.14 * 10 * 10", "Die Schnittfläche ist ein Kreis mit dem Radius der Kugel. Berechne zuerst den Radius aus dem Umfang.",
    "Der Schnitt ist ein Kreis mit dem Radius r der Kugel. Aus dem Umfang 2 · 3,14 · r = 62,8 folgt r = 62,8 : 6,28 = 10 cm. Die Fläche ist 3,14 · 10 · 10 = 314 cm².",
    [(100, None, "den Radius quadriert, aber nicht mit π malgenommen", "10 ** 2"), (628, None, "Umfang mal Radius gerechnet", "62.8 * 10"), (62.8, None, "den Umfang als Fläche angegeben", "62.8")], "cm²"))
a3(T, "axialschnitt", Z(
    "Der Axialschnitt eines Zylinders ist ein Quadrat mit dem Umfang 48 cm. Rechne mit π ≈ 3,14. Wie groß ist das Volumen des Zylinders in cm³?",
    1356.48, "3.14 * (48 / 4 / 2) ** 2 * (48 / 4)", "3.14 * 36 * 12", "Wie lang ist die Seite des Quadrats? Welche Seite des Quadrats ist der Durchmesser, welche die Höhe des Zylinders?",
    "Die Seite des Quadrats ist 48 : 4 = 12 cm. Sie ist zugleich der Durchmesser und die Höhe. Also ist r = 6 cm und h = 12 cm. V = 3,14 · 36 · 12 = 1 356,48 cm³.",
    [(5425.92, None, "die Seite 12 cm als Radius genommen", "3.14 * 12 ** 2 * 12"), (10851.84, None, "den Umfang nur durch 2 geteilt: Seite 24 cm", "3.14 * 12 ** 2 * 24"), (678.24, None, "die Höhe 6 cm statt 12 cm genommen", "3.14 * 6 * 6 * 6")], "cm³"), g="transfer")
# ───────── koerper_symmetrie ─────────
a1(T, "koerper_symmetrie", Z(
    "Eine Pralinenschachtel hat die Form eines Quaders. Ihre Grundfläche ist ein Quadrat, die Höhe ist aber nicht gleich der Länge der Grundseite. Wie viele Symmetrieebenen hat die Schachtel?",
    5, "4 + 1", "2 + 2 + 1", "Zähle erst die Ebenen, die die Höhe enthalten (Symmetrieachsen des Quadrats). Dann die Ebene parallel zur Grundfläche.",
    "Ebenen durch die Höhe: Sie entsprechen den 4 Symmetrieachsen des Quadrats (2 Mittellinien, 2 Diagonalen). Dazu kommt die Ebene in halber Höhe, parallel zur Grundfläche. Zusammen 4 + 1 = 5 Symmetrieebenen.",
    [(3, None, "wie bei einem Quader mit lauter verschiedenen Kanten gezählt", "3"), (9, None, "wie beim Würfel gezählt", "9"), (4, None, "die Ebene in halber Höhe vergessen", "4")]))
a2(T, "koerper_symmetrie", Z(
    "Ein Spielzeughändler hat drei Körper: einen Würfel, eine gerade Pyramide mit quadratischer Grundfläche und ein gerades Prisma, dessen Grundfläche ein gleichseitiges Dreieck ist. Wie viele Symmetrieebenen haben die drei Körper zusammen?",
    17, "9 + 4 + (3 + 1)", "9 + 4 + 4", "Der Würfel hat 9 Ebenen. Für Pyramide und Prisma zählst du erst die Symmetrieachsen der Grundfläche. Beim Prisma kommt noch eine Ebene dazu.",
    "Würfel: 9 Ebenen. Gerade Pyramide über dem Quadrat: 4 Ebenen (eine je Symmetrieachse des Quadrats). Gerades Prisma über dem gleichseitigen Dreieck: 3 Ebenen durch die Achsen des Dreiecks und 1 Ebene in halber Höhe, also 4. Zusammen 9 + 4 + 4 = 17.",
    [(16, None, "beim Prisma die Ebene in halber Höhe vergessen", "9 + 4 + 3"), (18, None, "bei der Pyramide eine Ebene in halber Höhe dazugezählt", "9 + 5 + 4"), (13, None, "den Würfel mit 5 Ebenen gezählt", "5 + 4 + 4")], "Ebenen"))
a3(T, "koerper_symmetrie", Z(
    "Ein gerades Prisma hat als Grundfläche ein regelmäßiges Vieleck mit n Ecken und genau 7 Symmetrieebenen. Wie viele Kanten hat das Prisma?",
    18, "3 * (7 - 1)", "6 * 3", "Wie hängt die Zahl der Symmetrieebenen eines geraden Prismas mit der Eckenzahl n der Grundfläche zusammen? Wie viele Kanten hat ein Prisma mit n-Eck?",
    "Ein gerades Prisma über einem regelmäßigen n-Eck hat n + 1 Symmetrieebenen. Aus n + 1 = 7 folgt n = 6. Ein Prisma über einem Sechseck hat 6 Kanten unten, 6 oben und 6 senkrechte: 3 · 6 = 18 Kanten.",
    [(21, None, "n = 7 genommen: die Zahl der Ebenen als Eckenzahl", "3 * 7"), (12, None, "nur die Kanten der Grund- und der Deckfläche gezählt", "2 * 6"), (6, None, "die Eckenzahl der Grundfläche als Kantenzahl angegeben", "6")], "Kanten"), g="rueckwaerts")
