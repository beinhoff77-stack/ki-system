T = "trigo.rechtwinklig"
R = "id.geometrie.rechtwinklig"
GRAD = "Der Taschenrechner steht auf Gradmaß (DEG)."
# ───────── seiten ─────────
neu(T, "seiten", "bruecke", W(
    "Im Dreieck ABC ist der Winkel bei C ein rechter Winkel. Die Tabelle zeigt die Längen der drei Seiten. Wie lang ist die Ankathete des Winkels β bei B?",
    "5 cm", [("12 cm", "die Gegenkathete von β genommen"), ("13 cm", "die Hypotenuse genommen")],
    "Die Ankathete eines Winkels ist die Kathete, die an diesem Winkel anliegt. Welche Seite verbindet B mit dem rechten Winkel?",
    "β liegt bei B. Die Kathete BC liegt an β an, sie ist die Ankathete: 5 cm. AC liegt β gegenüber (Gegenkathete, 12 cm). AB liegt dem rechten Winkel gegenüber (Hypotenuse, 13 cm).",
    lambda: 5 ** 2 + 12 ** 2 == 13 ** 2,
    grafik=TAB(["Seite", "Länge"], ["AB", "13 cm"], ["BC", "5 cm"], ["AC", "12 cm"])), regel=R)
neu(T, "seiten", "anwenden", W(
    "Eine 3,7 m lange Leiter lehnt an einer senkrechten Wand. Sie berührt die Wand in 3,5 m Höhe. Ihr Fuß steht auf waagerechtem Boden 1,2 m von der Wand entfernt. Der Winkel α liegt zwischen der Leiter und dem Boden. Welche Länge ist die Ankathete von α?",
    "1,2 m, der Abstand des Leiterfußes von der Wand", [("3,5 m, die Höhe, in der die Leiter die Wand berührt", "die Gegenkathete von α genommen"), ("3,7 m, die Länge der Leiter", "die Hypotenuse genommen")],
    "Die Ankathete liegt an α an und ist nicht die längste Seite des Dreiecks aus Leiter, Wand und Boden.",
    "Der Winkel α ist der Winkel am Leiterfuß. An ihm liegen der Boden (Strecke Fuß–Wand, 1,2 m) und die Leiter. Die Leiter ist die Hypotenuse, der Boden die Ankathete. Die Wand liegt α gegenüber (Gegenkathete, 3,5 m).",
    lambda: round(3.5 ** 2 + 1.2 ** 2, 6) == round(3.7 ** 2, 6)), g="einkleidung", regel=R)
neu(T, "seiten", "fehler_detektiv", FD(
    "Im Dreieck ABC ist der Winkel bei C ein rechter Winkel. Kim ordnet die Seiten dem Winkel α bei A zu.",
    [("Die Hypotenuse ist AB, denn sie liegt dem rechten Winkel gegenüber.", True, True),
     ("Die Gegenkathete von α ist BC, denn sie liegt α gegenüber.", True, True),
     ("Die Ankathete von α ist AB, denn sie liegt auch an α an.", False, True)],
    "Welche beiden Seiten liegen am Winkel α bei A? Welche davon ist keine Kathete?",
    "Am Winkel α bei A liegen die Seiten AB und AC. AB ist die Hypotenuse. Die Ankathete ist die Kathete, die an α anliegt, also AC. Der Fehler steckt in Zeile 3."), regel=R)

# ───────── verhaeltnisse ─────────
neu(T, "verhaeltnisse", "lueckenweg", L(
    "Ein Dreieck ABC hat bei C einen rechten Winkel. Die Gegenkathete BC von α ist 9 cm lang, die Ankathete AC ist 12 cm lang. Die Hypotenuse ist ① cm lang. Ein anderes Dreieck hat denselben Winkel α und einen rechten Winkel. Seine Hypotenuse ist 30 cm lang. Es entsteht durch Strecken mit dem Faktor ②. Die Gegenkathete von α ist in diesem Dreieck ③ cm lang, die Ankathete ④ cm.",
    "① = □; ② = □; ③ = □; ④ = □", [15, 2, 18, 24], ["wurzel(9 ** 2 + 12 ** 2)", "30 / {1}", "9 * {2}", "12 * {2}"], ["15", "2", "18", "24"],
    "Die Verhältnisse der Seiten hängen nur vom Winkel ab, nicht von der Größe des Dreiecks. Vergleiche zuerst die beiden Hypotenusen.",
    "AB = √(9² + 12²) = √225 = 15 cm. Faktor: 30 : 15 = 2. Gegenkathete: 9 · 2 = 18 cm. Ankathete: 12 · 2 = 24 cm. Das Verhältnis Gegenkathete : Hypotenuse ist in beiden Dreiecken 9 : 15 = 18 : 30.",
    {0: [(21, "fb.rechtwinklig.ohne_quadrate", "die Katheten addiert: 9 + 12", "9 + 12")], 1: [(15, None, "den Unterschied der Hypotenusen genommen: 30 − 15", "30 - {1}")],
     2: [(11, "fb.verhaeltnis.addiert_statt_malgenommen", "den Faktor addiert: 9 + 2", "9 + {2}")], 3: [(14, "fb.verhaeltnis.addiert_statt_malgenommen", "den Faktor addiert: 12 + 2", "12 + {2}")]}), regel=R)
neu(T, "verhaeltnisse", "bruecke", W(
    "Die Tabelle zeigt drei rechtwinklige Dreiecke. Gemessen sind jeweils die Gegenkathete des Winkels α und die Hypotenuse. Bei welchen Dreiecken ist der Winkel α gleich groß?",
    "Bei Dreieck 1 und Dreieck 2", [("Bei Dreieck 2 und Dreieck 3, denn bei beiden unterscheiden sich Hypotenuse und Gegenkathete um 4 cm", "Unterschiede statt Verhältnisse verglichen"), ("Bei allen drei Dreiecken", "Dreieck 3 hat ein anderes Verhältnis"),
                                    ("Bei Dreieck 1 und Dreieck 3, weil sich ihre Hypotenusen um 7 cm unterscheiden", "ein Längenunterschied prüft nicht, ob die Verhältnisse gleich sind")],
    "Der Winkel α ist durch das Verhältnis Gegenkathete : Hypotenuse bestimmt. Berechne es für jede Zeile.",
    "Dreieck 1: 3 : 5 = 0,6. Dreieck 2: 6 : 10 = 0,6. Dreieck 3: 8 : 12 ≈ 0,67. Gleiches Verhältnis heißt gleicher Winkel α: Dreieck 1 und Dreieck 2. Dreieck 3 hat einen größeren Winkel α.",
    lambda: 3 / 5 == 6 / 10 and 8 / 12 != 6 / 10 and 10 - 6 == 12 - 8 and 12 - 5 == 7,
    grafik=TAB(["Dreieck", "Gegenkathete von α", "Hypotenuse"], ["1", "3 cm", "5 cm"], ["2", "6 cm", "10 cm"], ["3", "8 cm", "12 cm"])), regel=R)
neu(T, "verhaeltnisse", "fehler_detektiv", FD(
    "Im Dreieck ABC ist der Winkel bei C ein rechter Winkel. Es gilt BC = 8 cm, AC = 15 cm und AB = 17 cm. Kim berechnet cos α für den Winkel α bei A.",
    [("cos α ist das Verhältnis Gegenkathete : Hypotenuse.", False, True),
     ("Die Gegenkathete von α ist BC = 8 cm, die Hypotenuse ist AB = 17 cm.", True, True),
     ("Also ist cos α = 8 : 17 ≈ 0,47.", False, round(8 / 17, 2) == 0.47)],
    "Welche Kathete liegt an α an? Welches Verhältnis gehört zum Kosinus?",
    "Der Kosinus ist das Verhältnis Ankathete : Hypotenuse. Die Ankathete von α ist AC = 15 cm. cos α = 15 : 17 ≈ 0,88. Das Verhältnis 8 : 17 gehört zum Sinus. Der erste Fehler steht in Zeile 1.",
    rueck={1: "Diese Zeile ist für sich richtig: BC liegt dem Winkel α bei A gegenüber (Gegenkathete) und AB ist die Hypotenuse. Der erste Fehler steht schon in Zeile 1, bei der Erklärung von cos α."}), regel=R)

# ───────── seite ─────────
neu(T, "seite", "lueckenweg", L(
    "Ein Dreieck ABC hat bei C einen rechten Winkel und die Hypotenuse c = 25 cm. Für den Winkel α gilt sin α = 0,8. Die Gegenkathete a ist ① cm lang. Das Quadrat der Ankathete b ist ② cm². Die Ankathete b ist ③ cm lang.",
    "① = □; ② = □; ③ = □", [20, 225, 15], ["25 * 0.8", "25 ** 2 - {1} ** 2", "wurzel({2})"], ["20", "225", "15"],
    "Der Sinus ist das Verhältnis Gegenkathete : Hypotenuse. Stelle um, wenn die Gegenkathete gesucht ist. Die Ankathete bekommst du danach mit dem Satz des Pythagoras.",
    "a = c · sin α = 25 · 0,8 = 20 cm. b² = c² − a² = 625 − 400 = 225. b = √225 = 15 cm. Probe: cos α = 15 : 25 = 0,6 und 0,6² + 0,8² = 1.",
    {0: [(31.25, None, "durch den Sinus geteilt: 25 : 0,8", "25 / 0.8")], 1: [(1025, "fb.rechtwinklig.kathete_als_hypotenuse", "addiert statt subtrahiert: 625 + 400", "25 ** 2 + {1} ** 2")], 2: [(225, None, "die Wurzel nicht gezogen", "{2}")]}), regel=R)
neu(T, "seite", "zwei_wege", Z(
    "Ein Dreieck ABC hat bei C einen rechten Winkel. Die Hypotenuse ist c = 12 cm lang, der Winkel α ist 40° groß. Berechne die Gegenkathete a auf zwei Wegen. Weg A: mit dem Sinus von α. Weg B: zuerst die Ankathete b mit dem Kosinus von α, dann a mit dem Satz des Pythagoras (b auf eine Dezimale gerundet verwenden). Runde das Ergebnis auf eine Dezimale. " + GRAD,
    7.7, rd("12 * sin(40)", 1)[1], "round(sqrt(12 ** 2 - round(12 * cos(40), 1) ** 2), 1)", "Beide Wege dürfen sich höchstens in der Rundung unterscheiden. Bei Weg B brauchst du zuerst b.",
    "Weg A: a = 12 · sin 40° ≈ 7,71 ≈ 7,7 cm. Weg B: b = 12 · cos 40° ≈ 9,19 ≈ 9,2 cm. a² = 12² − 9,2² = 144 − 84,64 = 59,36, a ≈ 7,70 ≈ 7,7 cm.",
    [(9.2, None, "den Kosinus statt des Sinus genommen: 12 · cos 40° (gerundet)", "round(12 * cos(40), 1)"), (18.7, None, "durch den Sinus geteilt statt malgenommen (gerundet)", "round(12 / sin(40), 1)"), (10.1, None, "den Tangens statt des Sinus genommen (gerundet)", "round(12 * tan(40), 1)")], "cm"), regel=R)
wert_ls, c_ls = rd("45 / tan(20)", 0)
neu(T, "seite", "anwenden", Z(
    "Von der Spitze eines 45 m hohen Leuchtturms am Ufer sieht man ein Boot auf dem Wasser unter einem Tiefenwinkel von 20°. Der Tiefenwinkel ist der Winkel zwischen der Waagerechten und der Blickrichtung nach unten. Die Augenhöhe wird nicht beachtet, das Wasser ist eben. Wie weit ist das Boot vom Fußpunkt des Turms entfernt? Runde auf ganze Meter. " + GRAD,
    wert_ls, c_ls, "round(45 / tan(20), 0)", "Zeichne das rechtwinklige Dreieck aus Turm, Wasserlinie und Blickrichtung. Der Winkel 20° liegt auch am Boot (Wechselwinkel).",
    "Am Boot ist der Winkel zwischen Wasserlinie und Blickrichtung ebenfalls 20°. Die Turmhöhe 45 m ist die Gegenkathete, gesucht ist die Ankathete. tan 20° = 45 : d, also d = 45 : tan 20° ≈ 123,6 m. Das Boot ist etwa 124 m entfernt.",
    [(16, None, "den Tangens malgenommen statt geteilt: 45 · tan 20° (gerundet)", "round(45 * tan(20), 0)"), (132, None, "den Sinus statt des Tangens genommen: 45 : sin 20° (gerundet)", "round(45 / sin(20), 0)")], "m"), g="transfer", regel=R)
assert wert_ls == 124

# ───────── winkel ─────────
neu(T, "winkel", "lueckenweg", L(
    "Ein Dreieck ABC hat bei C einen rechten Winkel. Es gilt BC = 6 cm, AC = 8 cm und AB = 10 cm. Der Winkel α bei A liegt der Seite BC gegenüber, und es gilt sin α = 0,6. Mit der Umkehrfunktion des Sinus am Taschenrechner (Gradmaß) ist α auf ganze Grad gerundet ① Grad groß. Der Winkel β bei B ist auf ganze Grad gerundet ② Grad groß.",
    "① = □; ② = □", [37, 53], [rd("asin(0.6)", 0)[1], "90 - {1}"], ["round(asin(0.6), 0)", "round(asin(0.8), 0)"],
    "Der Winkel α ist der Winkel, dessen Sinus 0,6 ist. Die Winkel in einem Dreieck ergeben zusammen 180°, und einer davon ist ein rechter Winkel.",
    "α = sin⁻¹(0,6) ≈ 36,87°, gerundet 37°. β = 90° − α ≈ 90° − 36,87° = 53,13°, gerundet 53°. Probe: cos β = sin α, und sin⁻¹(0,8) ≈ 53,13°.",
    {0: [(53, None, "mit dem falschen Verhältnis 0,8 gerechnet: sin⁻¹(0,8) (gerundet)", "round(asin(0.8), 0)"), (31, None, "den Tangens-Umkehrwert genommen: tan⁻¹(0,6) (gerundet)", "round(atan(0.6), 0)")],
     1: [(143, None, "180° − 37° gerechnet, den rechten Winkel nicht beachtet", "180 - {1}")]}), regel=R)
neu(T, "winkel", "zwei_wege", Z(
    "Ein Dreieck ABC hat bei C einen rechten Winkel. Die Gegenkathete von α ist 5 cm, die Ankathete 12 cm und die Hypotenuse 13 cm lang. Berechne α auf zwei Wegen. Weg A: mit dem Tangens von α. Weg B: mit dem Sinus von α. Runde auf ganze Grad. " + GRAD,
    23, rd("atan(5 / 12)", 0)[1], "round(asin(5 / 13), 0)", "Beide Wege müssen denselben Winkel ergeben. Beim Tangens brauchst du die Ankathete, beim Sinus die Hypotenuse.",
    "Weg A: tan α = 5 : 12, α = tan⁻¹(5 : 12) ≈ 22,62°. Weg B: sin α = 5 : 13, α = sin⁻¹(5 : 13) ≈ 22,62°. Gerundet: 23°.",
    [(67, None, "mit dem Verhältnis Ankathete : Gegenkathete gerechnet: tan⁻¹(12 : 5) (gerundet)", "round(atan(12 / 5), 0)"), (25, None, "Gegenkathete durch Ankathete in den Sinus gesteckt: sin⁻¹(5 : 12) (gerundet)", "round(asin(5 / 12), 0)"), (0.42, None, "ohne Umkehrfunktion: das Verhältnis der Katheten als Winkel angegeben (gerundet)", "round(5 / 12, 2)")], "°"), regel=R)
neu(T, "winkel", "fehler_detektiv", FD(
    "Ein Dreieck ABC hat bei C einen rechten Winkel. Die Gegenkathete von α ist 3 cm, die Ankathete 4 cm lang. Kim berechnet α in Grad.",
    [("tan α = Gegenkathete : Ankathete = 3 : 4 = 0,75.", 3 / 4 == 0.75, True),
     ("Gesucht ist der Winkel, dessen Tangens 0,75 ist, also α = tan⁻¹(0,75).", True, True),
     ("Mit dem Taschenrechner (Bogenmaß, RAD) erhalte ich α ≈ 0,64°.", False, round(math.atan(0.75), 2) == 0.64)],
    "In welcher Einheit soll der Winkel angegeben werden? Auf welche Einstellung muss der Taschenrechner dann stehen?",
    "Der Taschenrechner muss auf Gradmaß (DEG) stehen. Dann ist α = tan⁻¹(0,75) ≈ 36,9°. Der Rechner stand auf RAD: 0,64 rad wurden fälschlich als Grad angegeben. Mit DEG ergibt sich 36,9°, oder man rechnet 0,64 rad mit 180° : π um. Der Fehler steckt in Zeile 3."), regel=R)

# ───────── beziehungen ─────────
neu(T, "beziehungen", "lueckenweg", L(
    "Für einen spitzen Winkel α gilt sin α = 0,6. Das Hundertfache von sin² α ist ①. Das Hundertfache von cos² α ist ②. Das Hundertfache von cos α ist ③.",
    "① = □; ② = □; ③ = □", [36, 64, 80], ["100 * 0.6 ** 2", "100 - {1}", "wurzel(100 * {2})"], ["36", "64", "80"],
    "Zwischen Sinus und Kosinus desselben Winkels gibt es eine Beziehung mit Quadraten. Die Beziehung gilt für sin² α und cos² α, nicht für sin α und cos α.",
    "sin² α = 0,36, also 100 · sin² α = 36. Aus sin² α + cos² α = 1 folgt cos² α = 0,64 und 100 · cos² α = 64. Dann ist (100 · cos α)² = 100 · 64 = 6 400, also 100 · cos α = 80, cos α = 0,8.",
    {0: [(60, None, "nicht quadriert: 100 · 0,6", "100 * 0.6")], 1: [(40, None, "sin α statt sin² α verwendet: 100 · (1 − 0,6)", "100 * (1 - 0.6)")], 2: [(64, None, "cos² α statt cos α genommen", "{2}")]}), regel=R)
neu(T, "beziehungen", "zwei_wege", Z(
    "Für einen spitzen Winkel α gilt sin α = 0,6. Berechne cos α auf zwei Wegen. Weg A: mit der Beziehung sin² α + cos² α = 1. Weg B: berechne zuerst den Winkel α mit der Umkehrfunktion des Sinus, dann cos α mit dem Taschenrechner. Runde auf zwei Dezimalen. " + GRAD,
    0.8, "wurzel(1 - 0.6 ** 2)", "round(cos(asin(0.6)), 2)", "Beide Wege müssen denselben Wert ergeben. Bei Weg A steht am Ende eine Wurzel.",
    "Weg A: cos² α = 1 − 0,36 = 0,64, cos α = √0,64 = 0,8. Weg B: α = sin⁻¹(0,6) ≈ 36,87°, cos 36,87° ≈ 0,80. Beide Wege: 0,8.",
    [(0.4, None, "1 − 0,6 gerechnet: sin α nicht quadriert", "1 - 0.6"), (0.64, None, "die Wurzel nicht gezogen", "1 - 0.6 ** 2"), (36.87, None, "den Winkel statt cos α angegeben (gerundet)", "round(asin(0.6), 2)")]), regel=R)
neu(T, "beziehungen", "fehler_detektiv", FD(
    "Für einen spitzen Winkel α gilt sin α = 0,5. Kim berechnet cos α.",
    [("Es gilt sin² α + cos² α = 1.", True, True),
     ("Also ist cos α = 1 − sin α = 1 − 0,5 = 0,5.", False, 1 - 0.5 == 0.5),
     ("Dann sind sin α und cos α gleich, also ist α = 45°.", False, True)],
    "Welche Größen stehen in der Beziehung zwischen Sinus und Kosinus im Quadrat?",
    "Es gilt cos² α = 1 − sin² α = 1 − 0,25 = 0,75, also cos α = √0,75 ≈ 0,87. Kim hat sin α nicht quadriert. Der Fehler steckt in Zeile 2; Zeile 3 folgt daraus."), regel=R)

# ───────── anwendung ─────────
neu(T, "anwendung", "lueckenweg", L(
    "Ein Drachen hängt an einer 24 m langen, straff gespannten Schnur, die am Boden befestigt ist und mit dem waagerechten Boden einen Winkel von 30° bildet. Es gilt sin 30° = 0,5. Der Drachen ist ① m hoch über dem Boden. Eine 5-mal so lange Schnur bildet denselben Winkel. Dann ist der Drachen ② m hoch. Er ist dann ③ m höher als vorher.",
    "① = □; ② = □; ③ = □", [12, 60, 48], ["24 * 0.5", "5 * {1}", "{2} - {1}"], ["12", "60", "60 - 12"],
    "Die Schnur ist die Hypotenuse, die Höhe die Gegenkathete des Winkels am Boden. Berechne die Gegenkathete aus Hypotenuse und Sinus.",
    "Höhe: 24 · 0,5 = 12 m. Bei der 5-mal so langen Schnur ist die Höhe auch 5-mal so groß: 60 m. Unterschied: 60 − 12 = 48 m.",
    {0: [(48, None, "durch den Sinus geteilt: 24 : 0,5", "24 / 0.5")], 1: [(17, "fb.verhaeltnis.addiert_statt_malgenommen", "5 addiert statt malgenommen: 12 + 5", "{1} + 5")], 2: [(60, None, "die neue Höhe statt des Unterschieds angegeben", "{2}")]}), regel=R)
neu(T, "anwendung", "anwenden", Z(
    "Eine gerade Rampe ist 5 m lang und überwindet einen Höhenunterschied von 0,6 m. Wie groß ist ihr Neigungswinkel gegen die Waagerechte? Runde auf eine Dezimale. " + GRAD,
    rd("asin(0.6 / 5)", 1)[0], rd("asin(0.6 / 5)", 1)[1], "round(asin(0.12), 1)", "Die Länge der Rampe ist die Hypotenuse, der Höhenunterschied die Gegenkathete des Neigungswinkels.",
    "sin α = 0,6 : 5 = 0,12. α = sin⁻¹(0,12) ≈ 6,89°. Der Neigungswinkel ist etwa 6,9°.",
    [(6.8, None, "mit dem Tangens gerechnet, als wäre 5 m die waagerechte Strecke (gerundet)", "round(atan(0.6 / 5), 1)"), (83.1, None, "den Winkel zur Senkrechten berechnet: cos⁻¹(0,12) (gerundet)", "round(acos(0.6 / 5), 1)"), (0.12, None, "ohne Umkehrfunktion: das Verhältnis als Winkel angegeben", "round(0.6 / 5, 2)")], "°"), g="einkleidung", regel=R)
wert_ma, c_ma = rd("(20 - 1.6) / tan(25)", 0)
neu(T, "anwendung", "umkehren", Z(
    "Ein senkrechter Mast ist 20 m hoch und steht auf ebenem Boden. Eine Person, deren Augen 1,6 m über dem Boden liegen, soll die Mastspitze unter einem Höhenwinkel von 25° sehen. Der Höhenwinkel ist der Winkel zwischen der Waagerechten durch die Augen und der Blickrichtung. Wie weit vom Fußpunkt des Mastes muss die Person stehen? Runde auf ganze Meter. " + GRAD,
    wert_ma, c_ma, "round(18.4 / tan(25), 0)", "Zeichne die Waagerechte durch die Augen. Die Gegenkathete des Winkels 25° ist nicht die ganze Masthöhe. Gesucht ist die Ankathete.",
    "Die Spitze liegt 20 − 1,6 = 18,4 m über den Augen. tan 25° = 18,4 : d, also d = 18,4 : tan 25° ≈ 39,459 m, auf ganze Meter gerundet 39 m. Probe: 18,4 : 39 ≈ 0,47 und tan 25° ≈ 0,47.",
    [(43, None, "die Augenhöhe vergessen: 20 : tan 25° (gerundet)", "round(20 / tan(25), 0)"), (46, None, "die Augenhöhe addiert statt abgezogen: 21,6 : tan 25° (gerundet)", "round((20 + 1.6) / tan(25), 0)"), (9, None, "den Tangens malgenommen statt geteilt: 18,4 · tan 25° (gerundet)", "round(18.4 * tan(25), 0)")], "m"), g="rueckwaerts", regel=R)
assert wert_ma == 39

# ───────── schnittwinkel ─────────
neu(T, "schnittwinkel", "lueckenweg", L(
    "Die Gerade g hat die Gleichung y = x − 3, die Gerade h hat die Gleichung y = −x + 5. Winkel werden von der positiven x-Achse aus gegen den Uhrzeigersinn gemessen und liegen zwischen 0° und 180°. Der Winkel von g ist ① Grad. Der Winkel von h ist ② Grad. Der Winkel zwischen den beiden Geraden ist ③ Grad.",
    "① = □; ② = □; ③ = □", [45, 135, 90], ["45", "180 - {1}", "{2} - {1}"], ["round(atan(1), 0)", "180 - round(atan(1), 0)", "round(atan(1), 0) * 2"],
    "Die Steigung ist der Tangens des Winkels zur x-Achse. Bei negativer Steigung ist der Winkel größer als ein rechter Winkel.",
    "tan⁻¹(1) = 45°, also ist der Winkel von g 45°. h hat die Steigung −1: Der Winkel zur x-Achse ist 180° − 45° = 135°. Unterschied: 135° − 45° = 90°. Die Geraden stehen senkrecht aufeinander.",
    {0: [(1, None, "die Steigung 1 als Winkel angegeben", "1")], 1: [(-45, None, "tan⁻¹(−1) = −45° genommen, nicht auf 0° bis 180° umgerechnet", "-{1}")], 2: [(180, None, "die Winkel addiert statt subtrahiert: 135 + 45", "{2} + {1}")]}), regel=R)
neu(T, "schnittwinkel", "bruecke", Z(
    "Die Tabelle zeigt Wertepaare einer linearen Funktion. Ihr Graph ist eine Gerade g. Unter welchem Winkel schneidet g die x-Achse? Gib den Winkel zwischen 0° und 90° an, gerundet auf eine Dezimale. " + GRAD,
    rd("atan(0.5)", 1)[0], rd("atan(0.5)", 1)[1], "round(atan((4 - 1) / (6 - 0)), 1)", "Aus der Tabelle bekommst du die Steigung. Die Steigung ist der Tangens des Winkels zur x-Achse.",
    "Steigung: (y₂ − y₁) : (x₂ − x₁) = (3 − 1) : (4 − 0) = 0,5. tan α = 0,5, α = tan⁻¹(0,5) ≈ 26,57°. Der Winkel ist etwa 26,6°.",
    [(63.4, None, "das Verhältnis umgekehrt (Änderung von x durch Änderung von y): tan⁻¹(2) (gerundet)", "round(atan(2), 1)"), (0.5, None, "die Steigung statt des Winkels angegeben", "0.5")], "°",
    grafik=TAB(["x", "0", "2", "4", "6"], ["y", "1", "2", "3", "4"])), regel=R)
wert_sw, c_sw = rd("2 + 5 * tan(35)", 1)
neu(T, "schnittwinkel", "umkehren", Z(
    "Die Gerade h geht durch den Punkt Q(1 | 2) und steigt von links nach rechts. Sie schneidet die x-Achse unter einem Winkel von 35°. Auch der Punkt P(6 | y) liegt auf h. Wie groß ist y? Runde auf eine Dezimale. " + GRAD,
    wert_sw, c_sw, "round(2 + 5 * tan(35), 1)", "Von Q nach P gehst du 5 Einheiten nach rechts. Die Steigung ist der Tangens des Winkels zur x-Achse.",
    "Steigung m = tan 35° ≈ 0,70. Von Q nach P: 5 Einheiten nach rechts, also 5 · 0,70 ≈ 3,50 nach oben. y = 2 + 3,50 ≈ 5,5. Probe: (5,5 − 2) : 5 = 0,7 und tan 35° ≈ 0,70.",
    [(3.5, None, "nur den Anstieg angegeben, die 2 von Q vergessen: 5 · tan 35° (gerundet)", "round(5 * tan(35), 1)"), (9.1, None, "durch den Tangens geteilt statt mit ihm malgenommen (gerundet)", "round(2 + 5 / tan(35), 1)"), (4.9, None, "den Sinus statt des Tangens genommen (gerundet)", "round(2 + 5 * sin(35), 1)")]), g="rueckwaerts", regel=R)
