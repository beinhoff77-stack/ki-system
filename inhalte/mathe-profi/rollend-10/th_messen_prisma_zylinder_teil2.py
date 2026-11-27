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
    "Ein schiefes Prisma hat das Volumen 84 cm³ und die Grundfläche 12 cm². Seine schräge Seitenkante ist 10 cm lang. Wie groß ist der senkrechte Abstand zwischen Grund- und Deckfläche?",
    7, "84 / 12", "84 // 12", "Das Volumen eines schiefen Prismas ist Grundfläche mal senkrechte Höhe. Die Seitenkante wird nicht gebraucht.",
    "V = G · h, also h = V : G = 84 : 12 = 7 cm. Die Seitenkante von 10 cm ist länger als die Höhe und nicht nötig.",
    [(8.4, None, "durch die Seitenkante statt durch die Grundfläche geteilt: 84 : 10", "84 / 10"), (10, None, "die Länge der Seitenkante als Höhe angegeben", "10")], "cm"), g="rueckwaerts", regel=R)
