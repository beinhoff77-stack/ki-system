T = "messen.prisma_zylinder"
# ───────── prisma_volumen ─────────
a1(T, "prisma_volumen", Z(
    "Für eine Wasserleitung wird ein Graben ausgehoben. Sein Querschnitt ist ein Trapez: oben 3 m breit, unten 1 m breit und 2 m tief. Der Graben ist 25 m lang. Wie viele Kubikmeter Erde werden ausgehoben?",
    100, "(3 + 1) / 2 * 2 * 25", "4 * 25", "Der Graben ist ein Prisma. Die Grundfläche ist der trapezförmige Querschnitt. Berechne zuerst seine Fläche.",
    "Querschnitt: (3 + 1) : 2 · 2 = 4 m². Volumen = Grundfläche · Länge = 4 · 25 = 100 m³.",
    [B("4", "nur die Fläche des Querschnitts angegeben"), B("(3 + 1) * 2 * 25", "beim Trapez nicht durch 2 geteilt"), B("3 * 2 * 25", "den Querschnitt als Rechteck oben mal tief gerechnet")], "m³"))
a2(T, "prisma_volumen", Z(
    "Ein Betonprofil ist 2 m lang. Sein Querschnitt hat die Form eines L: Der Fuß ist 30 cm breit und 10 cm hoch. Darauf steht ein Steg, der 10 cm breit und 30 cm hoch ist. Fuß und Steg überlappen sich nicht. Wie viele Kubikdezimeter Beton enthält das Profil?",
    120, "(30 * 10 + 10 * 30) * 200 / 1000", "(3 * 1 + 1 * 3) * 20", "Rechne die Fläche des Querschnitts aus zwei Rechtecken. Achte auf die Einheiten: 1 dm³ = 1 000 cm³.",
    "Querschnitt: 30 · 10 + 10 · 30 = 600 cm². Länge: 2 m = 200 cm. Volumen: 600 · 200 = 120 000 cm³ = 120 dm³. Probe in dm: Querschnitt 6 dm², Länge 20 dm, 6 · 20 = 120.",
    [B("(30 * 10 + 10 * 30) * 200", "das Volumen in cm³ angegeben und nicht in dm³ umgerechnet"), B("(30 * 10 + 10 * 30) * 2 / 1000", "die Länge 2 m als 2 cm genommen"), B("30 * 10 * 200 / 1000", "nur den Fuß gerechnet")], "dm³"))
a3(T, "prisma_volumen", Z(
    "Ein Dreiecksprisma hat als Grundfläche ein Dreieck mit der Grundseite 9 cm und der Höhe 6 cm. Sein Volumen ist genauso groß wie das Volumen eines Würfels mit der Kantenlänge 6 cm. Wie hoch ist das Prisma?",
    8, "6 ** 3 / (9 * 6 / 2)", "216 / 27", "Berechne zuerst das Volumen des Würfels und die Grundfläche des Dreiecks. Danach brauchst du die fehlende Größe des Prismas.",
    "Würfel: 6³ = 216 cm³. Dreieck: 9 · 6 : 2 = 27 cm². V = G · h, also h = 216 : 27 = 8 cm.",
    [B("6 ** 3 / (9 * 6)", "die Dreiecksfläche nicht durch 2 geteilt"), B("6 ** 3 / 6", "das Würfelvolumen durch die Kantenlänge geteilt"), B("6 * 6 * 6 / 9", "durch die Grundseite 9 cm statt durch die Grundfläche geteilt")], "cm"), g="verknuepfen")
# ───────── prisma_oberflaeche ─────────
a1(T, "prisma_oberflaeche", Z(
    "Ein Holzprisma wird komplett lackiert. Seine Grundfläche ist ein rechtwinkliges Dreieck mit den Seiten 6 cm, 8 cm und 10 cm. Das Prisma ist 15 cm hoch. Wie viele Quadratzentimeter müssen lackiert werden?",
    408, "2 * (6 * 8 / 2) + (6 + 8 + 10) * 15", "48 + 24 * 15", "Die Oberfläche besteht aus zwei Grundflächen und dem Mantel. Der Mantel ist ein Rechteck: Umfang der Grundfläche mal Höhe.",
    "Grundfläche: 6 · 8 : 2 = 24 cm². Zwei Grundflächen: 48 cm². Umfang: 6 + 8 + 10 = 24 cm. Mantel: 24 · 15 = 360 cm². O = 48 + 360 = 408 cm².",
    [B("6 * 8 / 2 + (6 + 8 + 10) * 15", "nur eine Grundfläche gezählt"), B("2 * (6 * 8 / 2) + (6 + 8) * 15", "die Hypotenuse beim Umfang vergessen"), B("(6 + 8 + 10) * 15", "nur den Mantel angegeben")], "cm²"))
a2(T, "prisma_oberflaeche", Z(
    "Ein Pralinenkarton hat die Form eines geraden Prismas mit einem Quadrat als Grundfläche. Die Grundkante ist 6 cm lang. Die ganze Oberfläche des Kartons ist 192 cm² groß. Wie hoch ist der Karton?",
    5, "(192 - 2 * 6 * 6) / (4 * 6)", "120 / 24", "Ziehe von der Oberfläche zuerst die beiden Grundflächen ab. Der Rest ist der Mantel, ein Rechteck mit Umfang mal Höhe.",
    "Zwei Quadrate: 2 · 36 = 72 cm². Mantel: 192 − 72 = 120 cm². Der Umfang der Grundfläche ist 4 · 6 = 24 cm. Also ist die Höhe 120 : 24 = 5 cm. Probe: 72 + 24 · 5 = 192.",
    [B("(192 - 6 * 6) / (4 * 6)", "nur eine Grundfläche abgezogen: Höhe 6,5 cm"), B("192 / (4 * 6)", "die Grundflächen nicht abgezogen"), B("(192 - 2 * 6 * 6) / 6", "den Mantel nur durch die Grundkante geteilt")], "cm"))
a3(T, "prisma_oberflaeche", Z(
    "Ein Blumenkasten ist 100 cm lang. Sein Querschnitt ist ein gleichschenkliges Trapez: unten (Boden) 40 cm breit, oben (offen) 70 cm breit, 20 cm hoch, die schrägen Seiten sind je 25 cm lang. Die obere Seite ist offen, es gibt dort keinen Deckel. Wie viele Quadratzentimeter Blech braucht man für Boden, beide Seitenwände und beide Stirnseiten?",
    11200, "2 * ((40 + 70) / 2 * 20) + 40 * 100 + 2 * 25 * 100", "2200 + 4000 + 5000", "Die Stirnseiten sind die beiden Trapeze. Die Länge 100 cm gilt für Boden und beide schräge Seitenwände. Die Höhe 20 cm ist nicht die Länge der schrägen Seite.",
    "Ein Trapez: (40 + 70) : 2 · 20 = 1 100 cm², zwei Stirnseiten: 2 200 cm². Boden: 40 · 100 = 4 000 cm². Schräge Seitenwände: 2 · 25 · 100 = 5 000 cm². Zusammen: 2 200 + 4 000 + 5 000 = 11 200 cm².",
    [B("2 * ((40 + 70) / 2 * 20) + 40 * 100 + 2 * 25 * 100 + 70 * 100", "den offenen Deckel mit 70 cm Breite mitgezählt"), B("40 * 100 + 2 * 25 * 100", "die beiden Stirnseiten vergessen"), B("2 * ((40 + 70) / 2 * 20) + 40 * 100 + 2 * 20 * 100", "für die schrägen Seitenwände die Höhe 20 cm statt der Seitenlänge 25 cm genommen")], "cm²"), g="transfer")
# ───────── prisma_umstellen ─────────
a1(T, "prisma_umstellen", Z(
    "Ein Sandkasten hat eine rechteckige Grundfläche von 4 m². Es sind 1,6 m³ Sand eingefüllt, und der Sand liegt überall gleich hoch. Wie hoch liegt der Sand in Zentimetern?",
    40, "1.6 / 4 * 100", "160 / 4", "Die Höhe ist das Volumen geteilt durch die Grundfläche. Am Ende musst du in Zentimeter umrechnen.",
    "h = V : G = 1,6 m³ : 4 m² = 0,4 m = 40 cm. Probe: 4 m² · 0,4 m = 1,6 m³.",
    [B("1.6 / 4", "das Ergebnis in Metern angegeben, nicht in Zentimetern"), B("4 / 1.6 * 100", "Grundfläche durch Volumen geteilt"), B("1.6 * 4 * 100", "Volumen mit der Grundfläche malgenommen")], "cm"))
a2(T, "prisma_umstellen", Z(
    "Ein Becken hat die Form eines Prismas. Seine Grundfläche ist ein Trapez mit den parallelen Seiten 40 cm und 60 cm und dem Abstand 25 cm. In das Becken passen genau 25 Liter. Wie hoch ist das Prisma in Zentimetern?",
    20, "25 * 1000 / ((40 + 60) / 2 * 25)", "25000 / 1250", "Berechne zuerst die Trapezfläche. Rechne die Liter in cm³ um: 1 Liter = 1 000 cm³.",
    "Grundfläche: (40 + 60) : 2 · 25 = 1 250 cm². Volumen: 25 l = 25 000 cm³. Höhe: 25 000 : 1 250 = 20 cm.",
    [B("25 / ((40 + 60) / 2 * 25)", "die 25 Liter nicht in cm³ umgerechnet"), B("25 * 1000 / ((40 + 60) * 25)", "beim Trapez nicht durch 2 geteilt"), B("25 * 1000 / (40 + 60)", "als Grundfläche nur die Summe der parallelen Seiten genommen")], "cm"))
a3(T, "prisma_umstellen", Z(
    "In einem Quader-Gefäß mit der Grundfläche 20 cm mal 15 cm steht Saft 12 cm hoch. Der ganze Saft wird in ein Dreiecksprisma-Gefäß gegossen, das 40 cm hoch ist. Seine Grundfläche ist ein Dreieck mit der Grundseite 24 cm und der Höhe 10 cm. Wie hoch steht der Saft im zweiten Gefäß in Zentimetern?",
    30, "20 * 15 * 12 / (24 * 10 / 2)", "3600 / 120", "Das Volumen des Safts bleibt beim Umgießen gleich. Berechne die Grundfläche des zweiten Gefäßes.",
    "Volumen: 20 · 15 · 12 = 3 600 cm³. Grundfläche des Dreiecks: 24 · 10 : 2 = 120 cm². Füllhöhe: 3 600 : 120 = 30 cm. Das ist weniger als die Gefäßhöhe 40 cm.",
    [B("20 * 15 * 12 / (24 * 10)", "die Dreiecksfläche nicht durch 2 geteilt"), B("40 - 30", "die freie Höhe statt der Füllhöhe angegeben"), B("20 * 15 * 12 / 24", "durch die Grundseite statt durch die Grundfläche geteilt")], "cm"), g="verknuepfen")
# ───────── zylinder_volumen ─────────
a1(T, "zylinder_volumen", Z(
    "Ein Baumstamm hat die Form eines Zylinders mit dem Durchmesser 40 cm und der Länge 3 m. Wie viele Kubikdezimeter Holz sind das? Rechne mit π ≈ 3,14.",
    376.8, "3.14 * 2 ** 2 * 30", "3.14 * 4 * 30", "Rechne alle Maße in dm um. Aus dem Durchmesser bekommst du den Radius.",
    "r = 40 cm : 2 = 20 cm = 2 dm, Länge = 3 m = 30 dm. V = π · r² · h ≈ 3,14 · 4 · 30 = 376,8 dm³.",
    [B("3.14 * 4 ** 2 * 30", "den Durchmesser 4 dm statt des Radius genommen"), B("3.14 * 20 ** 2 * 300", "in cm gerechnet: das Ergebnis ist in cm³, nicht in dm³"), B("3.14 * 2 * 30", "den Radius nicht quadriert")], "dm³"))
a2(T, "zylinder_volumen", Z(
    "Ein Betonrohr ist 2 m lang. Der äußere Radius ist 30 cm, der innere Radius ist 20 cm. Wie viele Kubikdezimeter Beton enthält das Rohr? Rechne mit π ≈ 3,14.",
    314, "3.14 * (3 ** 2 - 2 ** 2) * 20", "3.14 * 5 * 20", "Das Rohr ist ein großer Zylinder, aus dem ein kleiner Zylinder herausgeschnitten ist. Rechne in dm.",
    "Rechne in dm: R = 3 dm, r = 2 dm, Länge 20 dm. V = (π · R² − π · r²) · h = 3,14 · (9 − 4) · 20 = 3,14 · 100 = 314 dm³.",
    [B("3.14 * 3 ** 2 * 20", "nur den großen Zylinder gerechnet"), B("3.14 * (3 - 2) ** 2 * 20", "erst die Radien subtrahiert und dann quadriert"), B("3.14 * (30 ** 2 - 20 ** 2) * 200", "in cm gerechnet: Ergebnis in cm³")], "dm³"))
a3(T, "zylinder_volumen", Z(
    "Ein Zylinder A hat den Radius 10 cm. Er ist 30 cm hoch mit Wasser gefüllt. Das ganze Wasser wird in einen Zylinder B mit dem Radius 5 cm gegossen. B ist hoch genug. Wie hoch steht das Wasser in B in Zentimetern?",
    120, "30 * (10 / 5) ** 2", "30 * 4", "Das Volumen bleibt gleich. Wie viel kleiner ist die Grundfläche von B als die von A? Denke an r².",
    "Die Grundfläche ist π · r². A: π · 100, B: π · 25. B hat nur ein Viertel der Grundfläche von A. Bei gleichem Volumen steht das Wasser viermal so hoch: 4 · 30 = 120 cm. Probe: π · 100 · 30 = π · 25 · 120.",
    [B("30 * (10 / 5)", "das Verhältnis der Radien 2 nicht quadriert"), B("30 / (10 / 5) ** 2", "die Höhe durch 4 geteilt statt mit 4 malgenommen"), B("30 / (10 / 5)", "die Höhe durch das Verhältnis der Radien geteilt")], "cm"), g="transfer")
# ───────── zylinder_oberflaeche ─────────
a1(T, "zylinder_oberflaeche", Z(
    "Ein zylinderförmiger Blecheimer ist oben offen. Er hat den Radius 15 cm und die Höhe 30 cm. Wie viele Quadratzentimeter Blech braucht man für Boden und Mantel? Rechne mit π ≈ 3,14.",
    3532.5, "3.14 * 15 ** 2 + 2 * 3.14 * 15 * 30", "706.5 + 2826", "Der Eimer hat keinen Deckel. Der Mantel ist ein Rechteck: Kreisumfang mal Höhe.",
    "Boden: π · r² ≈ 3,14 · 225 = 706,5 cm². Mantel: 2 · π · r · h ≈ 2 · 3,14 · 15 · 30 = 2 826 cm². Zusammen: 706,5 + 2 826 = 3 532,5 cm².",
    [B("2 * 3.14 * 15 ** 2 + 2 * 3.14 * 15 * 30", "auch den Deckel mitgezählt"), B("2 * 3.14 * 15 * 30", "nur den Mantel angegeben"), B("3.14 * 30 ** 2 + 2 * 3.14 * 30 * 30", "den Durchmesser 30 cm als Radius genommen")], "cm²"))
a2(T, "zylinder_oberflaeche", Z(
    "Ein Wassertank ist ein geschlossener Zylinder mit dem Durchmesser 2 m und der Höhe 3 m. Er wird außen zweimal gestrichen. Ein Liter Farbe reicht für einen Anstrich von 4 m². Wie viele Liter Farbe braucht man für die beiden Anstriche? Rechne mit π ≈ 3,14.",
    12.56, "(2 * 3.14 * 1 ** 2 + 2 * 3.14 * 1 * 3) * 2 / 4", "25.12 * 2 / 4", "Berechne zuerst die ganze Oberfläche (Boden, Deckel, Mantel) in m². Der Radius ist die Hälfte des Durchmessers.",
    "r = 1 m. Boden und Deckel: 2 · 3,14 · 1 = 6,28 m². Mantel: 2 · 3,14 · 1 · 3 = 18,84 m². Oberfläche: 25,12 m². Zwei Anstriche: 50,24 m². Farbe: 50,24 : 4 = 12,56 Liter.",
    [B("(2 * 3.14 * 1 ** 2 + 2 * 3.14 * 1 * 3) / 4", "nur einen Anstrich gerechnet"), B("2 * 3.14 * 1 * 3 * 2 / 4", "nur den Mantel gestrichen"), B("(2 * 3.14 * 2 ** 2 + 2 * 3.14 * 2 * 3) * 2 / 4", "den Durchmesser 2 m als Radius genommen")], "l"))
a3(T, "zylinder_oberflaeche", Z(
    "Eine geschlossene Blechdose hat die Form eines Zylinders mit dem Radius 4 cm. Für die ganze Dose (Boden, Deckel und Mantel) werden 326,56 cm² Blech gebraucht. Rechne mit π ≈ 3,14. Wie hoch ist die Dose in Zentimetern?",
    9, "(326.56 - 2 * 3.14 * 4 ** 2) / (2 * 3.14 * 4)", "226.08 / 25.12", "Ziehe zuerst Boden und Deckel ab. Der Rest ist der Mantel: Umfang mal Höhe.",
    "Boden und Deckel: 2 · 3,14 · 16 = 100,48 cm². Mantel: 326,56 − 100,48 = 226,08 cm². Der Kreisumfang ist 2 · 3,14 · 4 = 25,12 cm. Höhe: 226,08 : 25,12 = 9 cm.",
    [B("326.56 / (2 * 3.14 * 4)", "Boden und Deckel nicht abgezogen"), B("(326.56 - 3.14 * 4 ** 2) / (2 * 3.14 * 4)", "nur eine Kreisfläche abgezogen"), B("(326.56 - 2 * 3.14 * 4 ** 2) / (3.14 * 4)", "mit dem halben Umfang gerechnet")], "cm"), g="rueckwaerts")
# ───────── sach ─────────
a1(T, "sach", Z(
    "Ein zylinderförmiger Wassertank hat den Durchmesser 2 m und ist 3 m hoch. Wie viele Liter fasst er? Rechne mit π ≈ 3,14. Es gilt 1 m³ = 1 000 Liter.",
    9420, "3.14 * 1 ** 2 * 3 * 1000", "3.14 * 3 * 1000", "Aus dem Durchmesser bekommst du den Radius. Rechne zuerst das Volumen in m³ aus.",
    "r = 1 m. V = 3,14 · 1² · 3 = 9,42 m³. Das sind 9,42 · 1 000 = 9 420 Liter.",
    [B("3.14 * 1 ** 2 * 3", "das Volumen in m³ nicht in Liter umgerechnet"), B("3.14 * 2 ** 2 * 3 * 1000", "den Durchmesser 2 m als Radius genommen"), B("3.14 * 1 ** 2 * 3 * 100", "mit 1 m³ = 100 Liter gerechnet")], "l"))
a2(T, "sach", Z(
    "Eine Lagerhalle ist 20 m lang. Ihr Querschnitt besteht aus einem Rechteck (10 m breit, 4 m hoch) und einem Dreieck als Dach darüber (10 m breit, 3 m hoch). Wie groß ist der umbaute Raum der Halle in m³?",
    1100, "(10 * 4 + 10 * 3 / 2) * 20", "40 * 20 + 15 * 20", "Die Halle ist ein Prisma. Bestimme erst die Fläche des Querschnitts aus Rechteck und Dreieck.",
    "Querschnitt: Rechteck 10 · 4 = 40 m², Dreieck 10 · 3 : 2 = 15 m². Zusammen 55 m². Volumen: 55 · 20 = 1 100 m³.",
    [B("10 * 4 * 20", "das Dach vergessen"), B("(10 * 4 + 10 * 3) * 20", "das Dreieck nicht durch 2 geteilt"), B("(10 * 4 + 10 * 3 / 2) * 10", "die Breite 10 m statt der Länge 20 m als Höhe des Prismas genommen")], "m³"))
a3(T, "sach", Z(
    "Ein zylinderförmiges Gefäß hat den Radius 20 cm. Es ist 50 cm hoch mit Wasser gefüllt. Das ganze Wasser wird in einen sehr hohen quaderförmigen Behälter mit der Grundfläche 40 cm mal 25 cm umgefüllt. Wie viele Zentimeter hoch steht das Wasser dann im Quader? Rechne mit π ≈ 3,14.",
    62.8, "3.14 * 20 ** 2 * 50 / (40 * 25)", "62800 / 1000", "Berechne zuerst das Volumen des Wassers im Zylinder. Beim Quader teilst du das Volumen durch die Grundfläche.",
    "Wasser im Zylinder: 3,14 · 400 · 50 = 62 800 cm³. Grundfläche des Quaders: 40 · 25 = 1 000 cm². Höhe: 62 800 : 1 000 = 62,8 cm.",
    [B("3.14 * 40 ** 2 * 50 / (40 * 25)", "den Durchmesser 40 cm als Radius genommen"), B("20 * 20 * 50 / (40 * 25)", "die Zahl π vergessen"), B("3.14 * 20 ** 2 * 50 / 40", "nur durch eine Seite des Quaders geteilt")], "cm"), g="rueckwaerts")
# ───────── verstehen ─────────
a1(T, "verstehen", Z(
    "Becher A fasst 120 ml und ist ein Zylinder. Becher B ist genauso hoch, hat aber den doppelten Radius. Wie viele Milliliter fasst Becher B?",
    480, "120 * 2 ** 2", "120 * 4", "Die Höhe bleibt gleich. Wie ändert sich die Grundfläche π · r², wenn der Radius doppelt so groß wird?",
    "Mit dem doppelten Radius wird r² viermal so groß, also auch die Grundfläche. Bei gleicher Höhe ist das Volumen viermal so groß: 4 · 120 = 480 ml.",
    [B("120 * 2", "das Volumen nur verdoppelt"), B("120 * 2 ** 3", "mit 2³ gerechnet, als wäre auch die Höhe verdoppelt"), B("120 * 3", "mit 3 statt mit 4 malgenommen")], "ml"))
a2(T, "verstehen", Z(
    "Dose A ist ein Zylinder mit dem Radius 4 cm und der Höhe 6 cm. Dose B ist ein Zylinder mit dem Radius 6 cm und der Höhe 4 cm. Das Volumen von Dose B ist um n · π cm³ größer als das von Dose A. Welche Zahl ist n?",
    48, "6 ** 2 * 4 - 4 ** 2 * 6", "144 - 96", "Berechne beide Volumina als Vielfache von π. Beachte, welche Größe quadriert wird.",
    "A: π · 4² · 6 = 96π cm³. B: π · 6² · 4 = 144π cm³. Unterschied: 144π − 96π = 48π. Also ist n = 48. Die Dose mit dem größeren Radius ist größer, obwohl sie niedriger ist.",
    [B("6 ** 2 * 4", "nur das Volumen von Dose B angegeben"), B("4 ** 2 * 6", "nur das Volumen von Dose A angegeben"), B("6 ** 2 * 4 + 4 ** 2 * 6", "die beiden Volumina addiert")]))
a3(T, "verstehen", Z(
    "Ein Stapel aus 10 runden Pappscheiben steht gerade. Jede Scheibe hat den Radius 3 cm und ist 1 cm dick. Dann wird der Stapel seitlich verschoben, sodass er schief steht. Dabei ändert sich keine Scheibe. Wie groß ist das Volumen des schiefen Stapels in cm³? Rechne mit π ≈ 3,14.",
    282.6, "10 * 3.14 * 3 ** 2 * 1", "3.14 * 9 * 10", "Jede Scheibe hat dasselbe Volumen wie vorher. Wie viele Scheiben gibt es?",
    "Das Volumen einer Scheibe ist 3,14 · 3² · 1 = 28,26 cm³. Beim Verschieben ändert sich keine Scheibe, also bleibt auch die Summe gleich: 10 · 28,26 = 282,6 cm³. Ein schiefer Zylinder hat dasselbe Volumen wie der gerade mit gleicher Grundfläche und Höhe.",
    [B("10 * 3.14 * 3 * 1", "den Radius nicht quadriert"), B("10 * 3.14 * 3 ** 2 * 1 / 2", "das Volumen halbiert, weil der Stapel schief steht"), B("10 * 3.14 * 3 ** 2 * 2", "mit dem Durchmesser als Dicke gerechnet")], "cm³"), g="begruenden")
