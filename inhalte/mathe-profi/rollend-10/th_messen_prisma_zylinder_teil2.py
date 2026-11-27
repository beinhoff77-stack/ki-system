T = "messen.prisma_zylinder_teil2"
R = "id.flaeche_raum.aus_dem_rechteck"
neu(T, "cavalieri", "lueckenweg", L(
    "Ein schiefes Prisma hat als Grundfläche ein Rechteck mit den Seiten 4 cm und 5 cm. Seine schräge Seitenkante ist 10 cm lang. Der senkrechte Abstand zwischen Grund- und Deckfläche beträgt 8 cm. Die Grundfläche ist ① cm² groß. Das Volumen des Prismas ist ② cm³. Würde man fälschlich mit der Länge der Seitenkante rechnen, käme ein um ③ cm³ größeres Volumen heraus.",
    "① = □; ② = □; ③ = □", [20, 160, 40], ["4 * 5", "{1} * 8", "{1} * 10 - {2}"], ["20", "20 * 8", "200 - 160"],
    "Nach dem Prinzip von Cavalieri hat ein schiefes Prisma dasselbe Volumen wie ein gerades Prisma mit gleicher Grundfläche und gleicher senkrechter Höhe.",
    "G = 4 · 5 = 20 cm². Mit der senkrechten Höhe: V = 20 · 8 = 160 cm³. Mit der Seitenkante käme 20 · 10 = 200 cm³ heraus, das sind 200 − 160 = 40 cm³ zu viel.",
    {0: [(9, None, "die Seiten addiert: 4 + 5", "4 + 5")], 1: [(200, None, "mit der Länge der Seitenkante statt der senkrechten Höhe gerechnet: 20 · 10", "{1} * 10")], 2: [(160, None, "das Volumen als Unterschied angegeben", "{2}")]}), regel=R)
neu(T, "cavalieri", "anwenden", Z(
    "30 quadratische Holzplatten mit der Kantenlänge 20 cm und der Dicke 1 cm werden zu einem Stapel aufgeschichtet. Jede Platte ist gegen die darunterliegende leicht verschoben, sodass der Stapel schief steht. Alle Platten liegen waagerecht. Wie groß ist das Volumen des Stapels in cm³?",
    12000, "20 * 20 * 30", "30 * (20 * 20 * 1)", "Jede Platte hat dasselbe Volumen, egal wie sie verschoben ist. Wie hoch ist der Stapel senkrecht gemessen?",
    "Der Stapel ist 30 · 1 = 30 cm hoch. Nach Cavalieri ist sein Volumen wie bei einem geraden Stapel: V = 20 · 20 · 30 = 12 000 cm³. Das ist auch 30 Platten mit je 400 cm³.",
    [(400, None, "nur eine Platte gezählt", "20 * 20 * 1"), (600, None, "eine Kantenlänge mal die Höhe gerechnet: 20 · 30", "20 * 30")], "cm³"), g="einkleidung", regel=R)
neu(T, "cavalieri", "umkehren", Z(
    "Ein schiefes Prisma hat als Grundfläche ein Rechteck, das 9 cm lang ist. Der senkrechte Abstand zwischen Grund- und Deckfläche ist 7 cm, die schräge Seitenkante ist 10 cm lang. Das Volumen des Prismas beträgt 252 cm³. Wie breit ist das Rechteck der Grundfläche?",
    4, "252 / 7 / 9", "252 / 63", "Das Volumen eines schiefen Prismas ist Grundfläche mal senkrechte Höhe. Die Grundfläche ist ein Rechteck aus Länge und Breite.",
    "G = V : h = 252 : 7 = 36 cm². Breite = G : Länge = 36 : 9 = 4 cm. Probe: 9 · 4 · 7 = 252. Die Seitenkante von 10 cm ist nicht die Höhe und wird nicht gebraucht.",
    [(2.8, None, "durch die Seitenkante statt durch die senkrechte Höhe geteilt: 252 : 10 : 9", "252 / 10 / 9"), (36, None, "die Grundfläche statt der Breite angegeben", "252 / 7"), (28, None, "die Höhe vergessen: 252 : 9", "252 / 9")], "cm"), g="rueckwaerts", regel=R)
