T = "messen.flaechen_vielecke"
# ───────── parallelogramm ─────────
neu(T, "parallelogramm", "lueckenweg", L(
    "Ein Parallelogramm hat die Grundseite 15 cm und die Höhe 6 cm. Seine Fläche ist ① cm². Nimmt man die schräge Seite mit 9 cm als Grundseite, gehört dazu die Höhe ② cm. Eine Diagonale teilt das Parallelogramm in gleiche Dreiecke; jedes hat ③ cm².",
    KOMM(3), [90, 10, 45], ["15 * 6", "{1} / 9", "{1} / 2"], ["90", "10", "45"], "Fläche = Grundseite mal Höhe. Die Höhe steht senkrecht auf der Grundseite.",
    "A = 15 cm · 6 cm = 90 cm². Mit der Grundseite 9 cm: Höhe = 90 : 9 = 10 cm. Ein Dreieck hat 90 : 2 = 45 cm².",
    {0: [(21, None, "addiert statt malgenommen", "15 + 6")], 1: [(6, None, "durch die erste Grundseite 15 geteilt statt durch 9", "{1} / 15")], 2: [(180, None, "malgenommen statt halbiert", "{1} * 2")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "parallelogramm", "anwenden", Z(
    "Ein Beet hat die Form eines Parallelogramms. Die Grundseite ist 8 m lang. Der Abstand zur gegenüberliegenden Seite beträgt 3,5 m. Ein Kilogramm Rasensamen reicht für 7 m². Wie viele Kilogramm Rasensamen braucht man?",
    4, "8 * 3.5 / 7", "28 / 7", "Berechne zuerst die Fläche des Beets.",
    "A = 8 m · 3,5 m = 28 m². 28 : 7 = 4. Man braucht 4 kg.",
    [(28, None, "nur die Fläche angegeben", "8 * 3.5"), (0.25, None, "falsch herum geteilt: 7 : 28", "7 / 28")], "kg"), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "parallelogramm", "umkehren", Z(
    "Ein Rechteck (12 cm lang, 9 cm breit) und ein Parallelogramm haben denselben Flächeninhalt. Die Grundseite des Parallelogramms ist 18 cm lang. Wie hoch ist das Parallelogramm in Zentimetern?",
    6, "12 * 9 / 18", "108 / 18", "Wie groß ist die Fläche des Rechtecks?",
    "Rechteck: 12 · 9 = 108 cm². Parallelogramm: 18 · h = 108, also h = 108 : 18 = 6 cm.",
    [(108, None, "nur die Fläche angegeben", "12 * 9"), (90, None, "abgezogen statt geteilt: 108 − 18", "12 * 9 - 18")], "cm"), g="rueckwaerts", regel="id.flaeche_raum.aus_dem_rechteck")

# ───────── dreieck ─────────
neu(T, "dreieck", "lueckenweg", L(
    "Ein Dreieck hat die Grundseite 14 cm und die Höhe 9 cm. Das Rechteck mit denselben Maßen hat ① cm². Das Dreieck hat ② cm². Ein zweites Dreieck hat dieselbe Grundseite, ist aber 4 cm höher. Seine Fläche ist ③ cm².",
    KOMM(3), [126, 63, 91], ["14 * 9", "{1} / 2", "{2} + 14 * 4 / 2"], ["126", "63", "91"], "Ein Dreieck füllt nur einen Teil des Rechtecks mit gleicher Grundseite und Höhe.",
    "Rechteck: 14 · 9 = 126 cm². Dreieck: 63 cm². Zweites Dreieck: 14 · 13 : 2 = 91 cm², das sind 28 cm² mehr als 63 cm².",
    {0: [(23, None, "addiert statt malgenommen", "14 + 9")], 1: [(126, None, "nicht halbiert", "{1}")], 2: [(182, None, "beim höheren Dreieck nicht halbiert", "14 * (9 + 4)")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "dreieck", "bruecke", W(
    "Welche Figur gehört zur Rechnung 14 · 9 : 2 = 63?",
    "Ein Dreieck mit der Grundseite 14 cm und der Höhe 9 cm",
    [("Ein Rechteck mit den Seiten 14 cm und 9 cm", "ohne : 2 wäre es das Rechteck"),
     ("Ein Parallelogramm mit der Grundseite 14 cm und der Höhe 9 cm", "Parallelogramm hat die Fläche g · h ohne : 2"),
     ("Ein Dreieck mit den Seiten 14 cm und 9 cm und einer Höhe von 2 cm", "das : 2 als Höhe gelesen")],
    "Was bedeutet das „: 2“ in der Rechnung?",
    "Grundseite mal Höhe ist die Fläche eines Rechtecks oder Parallelogramms. Das Dreieck ist halb so groß: g · h : 2. Also gehört die Rechnung zu einem Dreieck mit g = 14 cm und h = 9 cm.",
    lambda: 14 * 9 // 2 == 63 and 14 * 9 != 63), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "dreieck", "umkehren", Z(
    "Ein Dreieck hat einen Flächeninhalt von 36 cm² und eine Höhe von 8 cm. Wie lang ist die zugehörige Grundseite in Zentimetern?",
    9, "2 * 36 / 8", "36 / 8 * 2", "Das Dreieck ist halb so groß wie das Rechteck aus Grundseite und Höhe.",
    "A = g · h : 2. Also g · 8 = 72 und g = 72 : 8 = 9 cm. Probe: 9 · 8 : 2 = 36.",
    [(4.5, None, "den Flächeninhalt nicht verdoppelt: 36 : 8", "36 / 8"), (288, None, "malgenommen statt geteilt: 36 · 8", "36 * 8")], "cm"), g="rueckwaerts", regel="id.flaeche_raum.aus_dem_rechteck")

# ───────── trapez ─────────
neu(T, "trapez", "lueckenweg", L(
    "Ein Trapez hat die parallelen Seiten 9 cm und 5 cm und die Höhe 6 cm. Die Summe der parallelen Seiten ist ① cm. Die Fläche ist ② cm². Ein Rechteck mit derselben Fläche und der Breite 6 cm ist ③ cm lang.",
    KOMM(3), [14, 42, 7], ["9 + 5", "{1} * 6 / 2", "{2} / 6"], ["14", "42", "7"], "Fläche = (a + c) mal Höhe durch 2.",
    "9 + 5 = 14. A = 14 · 6 : 2 = 42 cm². Rechteck: 42 : 6 = 7 cm lang. Das ist die mittlere Länge der parallelen Seiten.",
    {0: [(45, None, "malgenommen statt addiert", "9 * 5")], 1: [(84, None, "nicht durch 2 geteilt", "{1} * 6")], 2: [(14, None, "die Summe der parallelen Seiten statt ihrer Hälfte angegeben", "{1}"), (42, None, "die Fläche statt der Länge angegeben: nicht durch 6 geteilt", "{2}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "trapez", "zwei_wege", Z(
    "Ein Trapez hat die parallelen Seiten 12 cm und 8 cm und die Höhe 5 cm. Weg A: Rechne mit der Trapezformel. Weg B: Zerlege das Trapez in ein Rechteck mit der kurzen Seite und zwei Dreiecke, die zusammen die Grundseite 12 − 8 = 4 cm haben. Wie groß ist die Fläche in cm²?",
    50, "(12 + 8) * 5 / 2", "8 * 5 + 4 * 5 / 2", "Beide Wege müssen dieselbe Fläche ergeben.",
    "Weg A: (12 + 8) · 5 : 2 = 50 cm². Weg B: Rechteck 8 · 5 = 40 cm². Die beiden Dreiecke haben zusammen die Grundseite 4 cm und die Höhe 5 cm: 4 · 5 : 2 = 10 cm². 40 + 10 = 50 cm².",
    [(100, None, "nicht durch 2 geteilt", "(12 + 8) * 5"), (40, None, "nur das Rechteck gerechnet", "8 * 5"), (60, None, "mit der langen Seite als Rechteck", "12 * 5")], "cm²"), g="mehrschritt", regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "trapez", "anwenden", Z(
    "Ein Garten hat die Form eines Trapezes. Die parallelen Seiten sind 30 m (zur Straße) und 22 m lang. Der Abstand zwischen ihnen beträgt 15 m. Rollrasen kostet 3,20 € je Quadratmeter. Wie viel Euro kostet der Rasen für den ganzen Garten?",
    1248, "(30 + 22) * 15 / 2 * 3.2", "390 * 3.2", "Berechne zuerst die Fläche des Gartens.",
    "A = (30 + 22) · 15 : 2 = 390 m². 390 · 3,20 € = 1248 €.",
    [(2496, None, "bei der Fläche nicht durch 2 geteilt", "(30 + 22) * 15 * 3.2"), (390, None, "nur die Fläche angegeben", "(30 + 22) * 15 / 2")], "€"), g="transfer", regel="id.flaeche_raum.aus_dem_rechteck")

# ───────── rueckwaerts ─────────
neu(T, "rueckwaerts", "lueckenweg", L(
    "Ein Trapez hat die Fläche 84 cm². Die parallelen Seiten sind 10 cm und 14 cm lang. Die Summe der parallelen Seiten ist ① cm. Zweimal die Fläche ist ② cm². Die Höhe ist ③ cm. Das sind ④ Millimeter.",
    KOMM(4), [24, 168, 7, 70], ["10 + 14", "84 * 2", "{2} / {1}", "{3} * 10"], ["24", "168", "7", "70"], "Stelle die Formel A = (a + c) · h : 2 nach h um.",
    "Aus 84 = 24 · h : 2 folgt 168 = 24 · h. Also h = 168 : 24 = 7 cm = 70 mm.",
    {0: [(4, None, "Unterschied statt Summe der parallelen Seiten", "14 - 10")], 1: [(42, None, "durch 2 statt mal 2", "84 / 2")], 2: [(144, None, "abgezogen statt geteilt", "{2} - {1}")],
     3: [(7, None, "nicht in Millimeter umgerechnet", "{3}"), (700, None, "mit 100 statt mit 10 malgenommen", "{3} * 100")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "rueckwaerts", "umkehren", Z(
    "Ein Parallelogramm und ein Dreieck haben beide den Flächeninhalt 60 cm² und beide die Höhe 6 cm. Um wie viele Zentimeter ist die Grundseite des Dreiecks länger als die des Parallelogramms?",
    10, "2 * 60 / 6 - 60 / 6", "20 - 10", "Berechne beide Grundseiten mit den umgestellten Formeln.",
    "Parallelogramm: g = 60 : 6 = 10 cm. Dreieck: g = 2 · 60 : 6 = 20 cm. Unterschied: 20 cm − 10 cm = 10 cm.",
    [(20, None, "nur die Grundseite des Dreiecks angegeben", "2 * 60 / 6"), (5, None, "beim Dreieck nicht verdoppelt: 10 : 2", "60 / 6 / 2")], "cm"), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "rueckwaerts", "fehler_detektiv", FD(
    "Mira bestimmt die Höhe eines Dreiecks mit dem Flächeninhalt 45 cm² und der Grundseite 15 cm.",
    [("Dreieck: A = g · h : 2", True), ("45 = 15 · h : 2", True), ("45 · 2 = 90, also 15 · h = 90", 45 * 2 == 90), ("h = 90 · 15 = 1350", F(90, 15) == 90 * 15)],
    "Wie rechnet man, wenn eine Zahl mit g malgenommen wurde?", "Aus 15 · h = 90 folgt h = 90 : 15 = 6 cm. In Zeile 4 wurde malgenommen statt geteilt."), regel="id.flaeche_raum.aus_dem_rechteck")

# ───────── zusammengesetzt ─────────
neu(T, "zusammengesetzt", "lueckenweg", L(
    "Ein Haus hat vorn die Form eines Fünfecks: ein Rechteck (10 m breit, 6 m hoch) und darüber ein Dreieck als Giebel (Grundseite 10 m, Höhe 4 m). Das Rechteck hat ① m². Der Giebel hat ② m². Zusammen sind es ③ m². Der Giebel ist um ④ m² kleiner als das Rechteck.",
    KOMM(4), [60, 20, 80, 40], ["10 * 6", "10 * 4 / 2", "{1} + {2}", "{1} - {2}"], ["60", "20", "80", "40"], "Zerlege die Figur in ein Rechteck und ein Dreieck.",
    "Rechteck: 10 · 6 = 60 m². Dreieck: 10 · 4 : 2 = 20 m². Zusammen 80 m². Unterschied: 60 m² − 20 m² = 40 m².",
    {0: [(32, None, "Umfang statt Fläche gerechnet", "2 * (10 + 6)")], 1: [(40, None, "das Dreieck nicht halbiert", "10 * 4")], 2: [(100, None, "den Giebel nicht halbiert: 60 + 40", "{1} + 10 * 4")],
     3: [(80, None, "die Summe statt des Unterschieds angegeben", "{1} + {2}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.auslegen")
neu(T, "zusammengesetzt", "zwei_wege", Z(
    "Ein L-förmiges Grundstück entsteht aus einem Rechteck (20 m lang, 12 m breit), aus dem an einer Ecke ein Rechteck (8 m lang, 5 m breit) herausgeschnitten ist. Weg A: Rechne großes Rechteck minus herausgeschnittenes Rechteck. Weg B: Zerlege das Grundstück in zwei Rechtecke. Wie groß ist das Grundstück in m²?",
    200, "20 * 12 - 8 * 5", "(20 - 8) * 12 + 8 * (12 - 5)", "Beide Wege müssen dieselbe Fläche ergeben.",
    "Weg A: 240 m² − 40 m² = 200 m². Weg B: ein Teil ist (20 − 8) · 12 = 144 m², der andere 8 · (12 − 5) = 56 m². 144 + 56 = 200 m².",
    [(280, None, "das herausgeschnittene Rechteck addiert statt abgezogen", "20 * 12 + 8 * 5"), (240, None, "den Ausschnitt vergessen", "20 * 12")], "m²"), g="mehrschritt", regel="id.flaeche_raum.auslegen")
neu(T, "zusammengesetzt", "anwenden", Z(
    "Ein Flur ist L-förmig. Er entsteht aus einem Rechteck von 9 m mal 6 m, aus dem an einer Ecke ein Rechteck von 4 m mal 3 m herausgeschnitten ist. Der Boden wird gefliest. Ein Quadratmeter Fliesen kostet 18 €. Wie viel Euro kosten die Fliesen?",
    756, "(9 * 6 - 4 * 3) * 18", "42 * 18", "Berechne zuerst die Fläche des Flurs.",
    "Fläche: 9 · 6 − 4 · 3 = 54 − 12 = 42 m². 42 · 18 € = 756 €.",
    [(972, None, "den herausgeschnittenen Teil vergessen", "9 * 6 * 18"), (1188, None, "den Ausschnitt addiert statt abgezogen", "(9 * 6 + 4 * 3) * 18")], "€"), g="transfer", regel="id.flaeche_raum.auslegen")

# ───────── oberflaeche ─────────
neu(T, "oberflaeche", "lueckenweg", L(
    "Ein dreiseitiges Prisma ist 20 cm lang. Seine Grundfläche ist ein rechtwinkliges Dreieck mit den Seiten 9 cm, 12 cm und 15 cm. Die beiden Dreiecke haben zusammen ① cm². Die drei Rechtecke (Mantel) haben zusammen ② cm². Die Oberfläche ist ③ cm². Der Mantel ist um ④ cm² größer als die beiden Dreiecke zusammen.",
    KOMM(4), [108, 720, 828, 612], ["2 * 9 * 12 / 2", "(9 + 12 + 15) * 20", "{1} + {2}", "{2} - {1}"], ["108", "720", "828", "612"], "Der Mantel ist ein Rechteck: Umfang des Dreiecks mal Länge.",
    "Dreiecke: 2 · (9 · 12 : 2) = 108 cm². Mantel: (9 + 12 + 15) · 20 = 720 cm². Oberfläche: 108 + 720 = 828 cm². Unterschied: 720 cm² − 108 cm² = 612 cm².",
    {0: [(54, None, "nur ein Dreieck gerechnet", "9 * 12 / 2")], 1: [(420, None, "nur die Seiten 9 cm und 12 cm als Mantel", "(9 + 12) * 20")], 2: [(720, None, "die Dreiecke vergessen", "{2}")],
     3: [(828, None, "die Summe statt des Unterschieds angegeben", "{1} + {2}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.haut")
neu(T, "oberflaeche", "anwenden", Z(
    "Ein Festzelt hat die Form eines liegenden Dreiecksprismas. Vorn und hinten sind gleichschenklige Dreiecke mit der Grundseite 6 m, der Höhe 4 m und den Schenkeln von je 5 m. Das Zelt ist 8 m lang. Wie viel Quadratmeter Stoff braucht man für die beiden Giebel und die beiden Dachflächen (ohne Boden)?",
    104, "2 * 6 * 4 / 2 + 2 * 5 * 8", "24 + 80", "Die Dachflächen sind Rechtecke: Schenkellänge mal Zeltlänge.",
    "Giebel: 2 · (6 · 4 : 2) = 24 m². Dachflächen: 2 · (5 · 8) = 80 m². Zusammen 104 m².",
    [(64, None, "nur eine Dachfläche gerechnet", "2 * 6 * 4 / 2 + 5 * 8"), (80, None, "die Giebel vergessen", "2 * 5 * 8"), (152, None, "den Boden mitgerechnet", "2 * 6 * 4 / 2 + 2 * 5 * 8 + 6 * 8")], "m²"), regel="id.flaeche_raum.haut")
neu(T, "oberflaeche", "umkehren", Z(
    "Ein Prisma hat als Grundfläche ein rechtwinkliges Dreieck mit den Seiten 5 cm, 12 cm und 13 cm. Die Oberfläche des Prismas beträgt 480 cm². Wie lang ist das Prisma in Zentimetern?",
    14, "(480 - 2 * 5 * 12 / 2) / (5 + 12 + 13)", "(480 - 60) / 30", "Ziehe zuerst die beiden Dreiecke von der Oberfläche ab.",
    "Dreiecke: 2 · (5 · 12 : 2) = 60 cm². Mantel: 480 − 60 = 420 cm². Der Umfang ist 30 cm, also Länge = 420 : 30 = 14 cm.",
    [(16, None, "die Oberfläche durch den Umfang geteilt: 480 : 30", "480 / 30"), (8, None, "die Oberfläche durch die Dreiecksflächen geteilt: 480 : 60", "480 / 60"), (420, None, "nur den Mantel angegeben", "480 - 60")], "cm"), g="rueckwaerts", regel="id.flaeche_raum.haut")

# ───────── verstehen ─────────
neu(T, "verstehen", "lueckenweg", L(
    "Ein Parallelogramm hat die Grundseite 16 cm und die Höhe 5 cm. Man schneidet an einer Seite ein Dreieck ab und setzt es auf der anderen Seite an. So entsteht ein Rechteck mit ① cm². Ein Dreieck mit derselben Grundseite und derselben Höhe hat ② cm². Ein Rechteck mit derselben Fläche wie das Parallelogramm und der Breite 8 cm ist ③ cm lang.",
    KOMM(3), [80, 40, 10], ["16 * 5", "{1} / 2", "{1} / 8"], ["80", "40", "10"], "Beim Umlegen bleibt die Fläche gleich.",
    "Das Rechteck hat 16 · 5 = 80 cm², genau wie das Parallelogramm. Ein Dreieck mit g = 16 cm und h = 5 cm hat 40 cm². Das Rechteck mit der Breite 8 cm ist 80 : 8 = 10 cm lang.",
    {0: [(21, None, "addiert statt malgenommen", "16 + 5")], 1: [(80, None, "das Dreieck nicht verkleinert", "{1}")], 2: [(640, None, "malgenommen statt geteilt", "{1} * 8")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "verstehen", "umkehren", Z(
    "Ein Trapez hat die Fläche 56 cm², die Höhe 7 cm und eine parallele Seite von 5 cm. Wie lang ist die andere parallele Seite in Zentimetern?",
    11, "2 * 56 / 7 - 5", "16 - 5", "Die Summe der beiden parallelen Seiten ergibt sich aus 2 · A : h.",
    "(a + 5) · 7 : 2 = 56. Also (a + 5) · 7 = 112 und a + 5 = 16. Damit ist a = 11 cm.",
    [(3, None, "die Fläche nicht verdoppelt: 56 : 7 − 5", "56 / 7 - 5"), (13, None, "5 addiert statt abgezogen: 56 : 7 + 5", "56 / 7 + 5"), (16, None, "die Summe der parallelen Seiten angegeben", "2 * 56 / 7")], "cm"), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "verstehen", "fehler_detektiv", FD(
    "Ben behauptet: „Wenn man bei einem Dreieck Grundseite und Höhe verdoppelt, verdoppelt sich die Fläche.“ Er prüft es mit g = 4 cm und h = 3 cm.",
    [("Vorher: 4 · 3 : 2 = 6 cm²", F(4 * 3, 2) == 6), ("Nachher mit g = 8 cm und h = 6 cm: 8 · 6 : 2 = 24 cm²", F(8 * 6, 2) == 24), ("24 : 6 = 4", F(24, 6) == 4), ("Die Fläche hat sich also verdoppelt.", F(24, 6) == 2)],
    "Wie oft passt 6 in 24? Wie oft sind die Maße größer geworden?", "Die Fläche ist 4-mal so groß: g wird 2-mal so groß und h auch, also 2 · 2 = 4. Zeile 4 zieht aus 24 : 6 = 4 den falschen Schluss."), regel="id.flaeche_raum.aus_dem_rechteck")

# ───────── drachen_raute ─────────
neu(T, "drachen_raute", "lueckenweg", L(
    "Eine Raute hat die Diagonalen e = 16 cm und f = 12 cm. Das Rechteck, das die Raute genau umschließt, hat ① cm². Die Raute hat ② cm². Wird jede Diagonale halbiert, hat die kleinere Raute ③ cm².",
    KOMM(3), [192, 96, 24], ["16 * 12", "{1} / 2", "{2} / 4"], ["192", "96", "24"], "Die Raute füllt genau die Hälfte des umschließenden Rechtecks.",
    "Rechteck: 16 · 12 = 192 cm². Raute: 192 : 2 = 96 cm². Formel: A = e · f : 2. Halbe Diagonalen: 8 · 6 : 2 = 24 cm², das ist ein Viertel von 96 cm².",
    {0: [(28, None, "addiert statt malgenommen", "16 + 12")], 1: [(192, None, "nicht halbiert", "{1}")], 2: [(48, None, "durch 2 statt durch 4 geteilt: nur eine Diagonale halbiert", "{2} / 2")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "drachen_raute", "bruecke", Z(
    "Eine Raute liegt so in einem Rechteck (14 cm lang, 8 cm breit), dass ihre Ecken genau in den Mitten der Rechteckseiten liegen. Wie groß ist die Fläche der Raute in cm²?",
    56, "14 * 8 / 2", "14 * 8 / 2", "Wo liegen die beiden Diagonalen der Raute im Rechteck?",
    "Die Diagonalen der Raute sind 14 cm und 8 cm lang. A = e · f : 2 = 14 · 8 : 2 = 56 cm². Das ist die Hälfte der Rechteckfläche 112 cm².",
    [(112, None, "die Fläche des Rechtecks angegeben", "14 * 8"), (22, None, "addiert statt malgenommen", "14 + 8")], "cm²"), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "drachen_raute", "zwei_wege", Z(
    "Eine Raute hat die Diagonalen 10 cm und 24 cm. Weg A: Rechne mit der Formel e · f : 2. Weg B: Die Diagonalen teilen die Raute in vier gleiche rechtwinklige Dreiecke mit den Katheten 5 cm und 12 cm. Rechne ein Dreieck aus und nimm es mal 4. Wie groß ist die Raute in cm²?",
    120, "10 * 24 / 2", "4 * (5 * 12 / 2)", "Beide Wege müssen dieselbe Fläche ergeben.",
    "Weg A: 10 · 24 : 2 = 120 cm². Weg B: Ein Dreieck hat 5 · 12 : 2 = 30 cm². Vier Dreiecke: 4 · 30 = 120 cm².",
    [(240, None, "nicht durch 2 geteilt", "10 * 24"), (30, None, "nur ein Dreieck angegeben", "5 * 12 / 2"), (60, None, "nur zwei der vier Dreiecke genommen", "2 * (5 * 12 / 2)")], "cm²"), g="verknuepfen", regel="id.flaeche_raum.aus_dem_rechteck")
