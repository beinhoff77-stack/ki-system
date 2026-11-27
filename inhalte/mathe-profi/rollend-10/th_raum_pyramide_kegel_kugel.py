T = "raum.pyramide_kegel_kugel"
R = "id.flaeche_raum.aus_dem_quader"
DR = "fb.aus_dem_quader.drittel_vergessen"
DM = "fb.aus_dem_rechteck.durchmesser_statt_radius"
# ───────── pyr_volumen ─────────
neu(T, "pyr_volumen", "lueckenweg", L(
    "Eine gerade Pyramide hat als Grundfläche ein Quadrat mit der Kantenlänge 6 cm. Die Pyramide ist 8 cm hoch. Die Grundfläche ist ① cm² groß. Grundfläche mal Höhe ergibt ② cm³. Das Volumen der Pyramide ist ③ cm³.",
    "① = □; ② = □; ③ = □", [36, 288, 96], ["6 * 6", "{1} * 8", "{2} / 3"], ["36", "36 * 8", "288 // 3"],
    "Das Volumen einer Pyramide ist nur ein Teil des Volumens eines Prismas mit gleicher Grundfläche und gleicher Höhe.",
    "G = 6 · 6 = 36 cm². G · h = 36 · 8 = 288 cm³. Eine Pyramide fasst ein Drittel davon: V = 288 : 3 = 96 cm³.",
    {0: [(12, None, "die Kantenlänge verdoppelt statt quadriert: 6 · 2", "6 * 2")], 1: [(44, None, "Grundfläche und Höhe addiert statt malgenommen: 36 + 8", "{1} + 8")],
     2: [(288, DR, "den Faktor ein Drittel vergessen", "{2}"), (864, None, "mit 3 malgenommen statt durch 3 geteilt", "{2} * 3")]}), regel=R)
neu(T, "pyr_volumen", "anwenden", Z(
    "Ein Zelt hat die Form einer geraden Pyramide mit quadratischer Grundfläche. Die Grundkante ist 3 m lang, die Zeltspitze liegt 2,4 m über dem Boden. Wie viele Kubikmeter Luft sind im Zelt?",
    7.2, "3 * 3 * 2.4 / 3", "9 * 2.4 / 3", "Die Grundfläche ist ein Quadrat. Die Höhe der Spitze über dem Boden ist die Körperhöhe.",
    "G = 3 · 3 = 9 m². V = 9 · 2,4 : 3 = 7,2 m³. Im Zelt sind 7,2 m³ Luft.",
    [(21.6, DR, "den Faktor ein Drittel vergessen: 9 · 2,4", "3 * 3 * 2.4"), (2.4, None, "die Kantenlänge statt der Grundfläche genommen: 3 · 2,4 : 3", "3 * 2.4 / 3")], "m³"), g="einkleidung", regel=R)
neu(T, "pyr_volumen", "umkehren", Z(
    "Eine gerade Pyramide hat eine quadratische Grundfläche. Ihr Volumen beträgt 108 cm³ und ihre Höhe 9 cm. Wie lang ist eine Kante der Grundfläche?",
    6, "wurzel(3 * 108 / 9)", "sqrt(3 * 108 / 9)", "Das Volumen hängt von Grundfläche und Höhe ab. Überlege, wie du von V zurück zur Kantenlänge kommst.",
    "G = 3 · V : h = 3 · 108 : 9 = 36 cm². Kante: √36 = 6 cm. Probe: 36 · 9 : 3 = 108.",
    [(36, None, "die Grundfläche statt der Kantenlänge angegeben", "3 * 108 / 9"), (3.5, DR, "den Faktor 3 vergessen und aus der so erhaltenen Grundfläche die Wurzel gezogen (gerundet)", "round(sqrt(108 / 9), 1)")], "cm"), g="rueckwaerts", regel=R)

# ───────── pyr_oberflaeche ─────────
neu(T, "pyr_oberflaeche", "lueckenweg", L(
    "Eine gerade Pyramide hat als Grundfläche ein Quadrat mit der Kantenlänge 10 cm. Die vier Seitenflächen sind gleich große Dreiecke. Die Höhe eines solchen Dreiecks, gemessen von der Grundkante bis zur Spitze, ist 13 cm. Die Grundfläche ist ① cm² groß. Ein Seitendreieck hat ② cm². Die vier Seitendreiecke zusammen haben ③ cm². Die Oberfläche ist ④ cm².",
    "① = □; ② = □; ③ = □; ④ = □", [100, 65, 260, 360], ["10 * 10", "10 * 13 / 2", "4 * {2}", "{1} + {3}"], ["100", "65", "260", "360"],
    "Die Oberfläche besteht aus der Grundfläche und dem Mantel. Der Mantel besteht aus allen Seitendreiecken.",
    "G = 100 cm². Ein Dreieck: 10 · 13 : 2 = 65 cm². Vier Dreiecke: 4 · 65 = 260 cm². O = 100 + 260 = 360 cm².",
    {1: [(130, "fb.aus_dem_rechteck.halbieren_vergessen", "das Halbieren vergessen: 10 · 13", "10 * 13")], 2: [(195, None, "nur drei Seitendreiecke gezählt: 3 · 65", "3 * {2}")], 3: [(260, None, "die Grundfläche vergessen", "{3}")]}), regel="id.flaeche_raum.haut")
neu(T, "pyr_oberflaeche", "bruecke", W(
    "Die Tabelle zeigt alle Teile des Netzes einer geraden Pyramide mit quadratischer Grundfläche. Wie groß ist die Oberfläche der Pyramide?",
    "224 cm²", [("104 cm²", "nur ein Seitendreieck gezählt: 64 + 40"), ("160 cm²", "nur den Mantel gezählt, die Grundfläche vergessen"), ("384 cm²", "die vier Dreiecke doppelt gezählt: 64 + 8 · 40")],
    "Rechne für jede Zeile Anzahl mal Fläche je Stück und addiere.",
    "Quadrat: 1 · 64 = 64 cm². Dreiecke: 4 · 40 = 160 cm². O = 64 + 160 = 224 cm².",
    lambda: 1 * 64 + 4 * 40 == 224 and 64 + 40 == 104 and 4 * 40 == 160 and 64 + 8 * 40 == 384,
    grafik=TAB(["Teil des Netzes", "Anzahl", "Fläche je Stück"], ["Quadrat (Grundfläche)", "1", "64 cm²"], ["Dreieck (Seitenfläche)", "4", "40 cm²"])), regel="id.flaeche_raum.haut")
neu(T, "pyr_oberflaeche", "fehler_detektiv", FD(
    "Eine gerade Pyramide hat ein Quadrat mit der Kantenlänge 6 cm als Grundfläche. Die Höhe eines Seitendreiecks (von der Grundkante bis zur Spitze) ist 5 cm. Kim berechnet die Oberfläche.",
    [("Grundfläche: 6 · 6 = 36 cm².", 6 * 6 == 36, True),
     ("Ein Seitendreieck: 6 · 5 : 2 = 15 cm².", 6 * 5 / 2 == 15, True),
     ("Oberfläche: Grundfläche plus ein Seitendreieck, also 36 + 15 = 51 cm².", 36 + 4 * 15 == 51, 36 + 15 == 51)],
    "Wie viele Seitendreiecke hat eine Pyramide mit quadratischer Grundfläche?",
    "Die Pyramide hat vier Seitendreiecke. O = 36 + 4 · 15 = 36 + 60 = 96 cm². Der Fehler steckt in Zeile 3."), regel="id.flaeche_raum.haut")

# ───────── kegel_volumen ─────────
neu(T, "kegel_volumen", "lueckenweg", L(
    "Ein gerader Kegel hat den Radius 3 cm und die Höhe 10 cm. Die Grundfläche ist ① · π cm² groß. Ein Zylinder mit derselben Grundfläche und derselben Höhe hat das Volumen ② · π cm³. Das Volumen des Kegels ist ③ · π cm³.",
    "① = □; ② = □; ③ = □", [9, 90, 30], ["3 ** 2", "{1} * 10", "{2} / 3"], ["9", "90", "90 // 3"],
    "Die Grundfläche ist ein Kreis. Ein Kegel fasst nur einen Teil von dem Zylinder mit gleicher Grundfläche und Höhe.",
    "G = π · 3² = 9π cm². Zylinder: 9π · 10 = 90π cm³. Kegel: ein Drittel davon, 90π : 3 = 30π cm³.",
    {0: [(6, "fb.potenz.basis_mal_hochzahl", "3 · 2 statt 3² gerechnet", "3 * 2")], 1: [(19, None, "Du hast den π-Koeffizienten 9 zur Höhenmaßzahl 10 addiert. Für den gesuchten Volumenkoeffizienten musst du 9 · 10 rechnen.", "{1} + 10")], 2: [(90, DR, "den Faktor ein Drittel vergessen", "{2}"), (270, None, "mit 3 malgenommen statt durch 3 geteilt", "{2} * 3")]}), regel=R)
neu(T, "kegel_volumen", "anwenden", Z(
    "Ein Sandhaufen hat die Form eines geraden Kegels. Sein Durchmesser am Boden ist 3 m, seine Höhe ist 1,2 m. Rechne mit π ≈ 3,14. Wie viele Kubikmeter Sand sind das? Gib das Ergebnis ohne Rundung an.",
    2.826, "3.14 * 1.5 ** 2 * 1.2 / 3", "3.14 * 2.25 * 0.4", "Der Radius ist halb so groß wie der Durchmesser.",
    "r = 3 : 2 = 1,5 m. V = 3,14 · 1,5² · 1,2 : 3 = 3,14 · 2,25 · 0,4 = 2,826 m³.",
    [(11.304, DM, "den Durchmesser 3 m als Radius genommen", "3.14 * 3 ** 2 * 1.2 / 3"), (8.478, DR, "den Faktor ein Drittel vergessen", "3.14 * 1.5 ** 2 * 1.2")], "m³"), g="einkleidung", regel=R)
neu(T, "kegel_volumen", "umkehren", Z(
    "Ein gerader Kegel ist 12 cm hoch und hat das Volumen 113,04 cm³. Rechne mit π ≈ 3,14. Wie groß ist der Radius seiner Grundfläche?",
    3, "wurzel(113.04 * 3 / (3.14 * 12))", "sqrt(113.04 * 3 / (3.14 * 12))", "Das Volumen hängt von Radius und Höhe ab. Überlege, welche Größe gesucht ist und wie du von V dorthin zurückkommst.",
    "r² = 3 · V : (π · h) = 339,12 : 37,68 = 9. Also r = 3 cm. Probe: 3,14 · 9 · 12 : 3 = 113,04.",
    [(9, None, "r² statt r angegeben", "113.04 * 3 / (3.14 * 12)"), (1.7, DR, "den Faktor 3 vergessen und die Wurzel gezogen (gerundet)", "round(sqrt(113.04 / (3.14 * 12)), 1)")], "cm"), g="rueckwaerts", regel=R)

# ───────── kegel_mantel ─────────
neu(T, "kegel_mantel", "lueckenweg", L(
    "Ein gerader Kegel hat den Radius 5 cm und die Höhe 12 cm. Das Quadrat der Mantellinie s ist ① cm². Die Mantellinie s ist ② cm lang. Die Mantelfläche ist ③ · π cm² groß.",
    "① = □; ② = □; ③ = □", [169, 13, 65], ["5 ** 2 + 12 ** 2", "wurzel({1})", "5 * {2}"], ["169", "13", "65"],
    "Radius, Höhe und Mantellinie bilden ein rechtwinkliges Dreieck. Die Mantelfläche ist π mal Radius mal Mantellinie.",
    "s² = 5² + 12² = 25 + 144 = 169. s = 13 cm. M = π · r · s = π · 5 · 13 = 65π cm².",
    {0: [(17, "fb.rechtwinklig.ohne_quadrate", "Radius und Höhe addiert: 5 + 12", "5 + 12")], 1: [(169, None, "die Wurzel nicht gezogen", "{1}")], 2: [(156, None, "mit der Höhe statt mit dem Radius gerechnet: 12 · 13", "12 * {2}")]}), regel="id.flaeche_raum.haut")
neu(T, "kegel_mantel", "zwei_wege", Z(
    "Ein gerader Kegel hat den Radius 3 cm und die Mantellinie 5 cm. Gib die Mantelfläche in der Form M = □ · π cm² an. Welche Zahl gehört in das Kästchen? Rechne auf zwei Wegen. Weg A: mit der Formel M = π · r · s. Weg B: Der abgewickelte Mantel ist ein Kreissektor mit dem Radius s. Seine Bogenlänge ist der Umfang des Grundkreises. Die Fläche des Sektors ist Bogenlänge mal Radius geteilt durch 2.",
    15, "3 * 5", "(2 * 3) * 5 / 2", "Beide Wege müssen dieselbe Zahl ergeben. Bei Weg B ist die Bogenlänge ein Vielfaches von π.",
    "Weg A: M = π · 3 · 5 = 15π cm². Weg B: Bogenlänge = 2π · 3 = 6π cm. Sektorfläche = 6π · 5 : 2 = 15π cm². Beide Wege: 15.",
    [(30, None, "den Sektor nicht halbiert: Bogenlänge mal Radius, 6 · 5", "2 * 3 * 5"), (9, None, "die Grundfläche statt des Mantels angegeben: 3²", "3 ** 2"), (8, None, "Radius und Mantellinie addiert: 3 + 5", "3 + 5")]), regel="id.flaeche_raum.haut")
neu(T, "kegel_mantel", "fehler_detektiv", FD(
    "Ein gerader Kegel hat den Radius 6 cm und die Höhe 8 cm. Kim berechnet die Oberfläche des Kegels, also Mantel und Grundfläche.",
    [("Mantellinie: s² = 6² + 8² = 100, also s = 10 cm.", 6 ** 2 + 8 ** 2 == 100, True),
     ("Mantel: M = π · r · s = π · 6 · 10 = 60π cm².", 6 * 10 == 60, True),
     ("Oberfläche: O = M + G = 60π + π · 6 · 2 = 72π cm².", 36 == 6 * 2, 60 + 6 * 2 == 72)],
    "Wie berechnet man die Fläche eines Kreises mit dem Radius 6 cm?",
    "Die Grundfläche ist π · r² = π · 36 = 36π cm², nicht π · 6 · 2. O = 60π + 36π = 96π cm². Der Fehler steckt in Zeile 3."), regel="id.flaeche_raum.haut")

# ───────── kugel ─────────
neu(T, "kugel", "lueckenweg", L(
    "Eine Kugel hat den Radius 6 cm. Das Quadrat des Radius ist ① cm². Die Oberfläche ist ② · π cm². Das Volumen ist ③ · π cm³.",
    "① = □; ② = □; ③ = □", [36, 144, 288], ["6 ** 2", "4 * {1}", "{2} * 6 / 3"], ["36", "4 * 36", "4 * 6 ** 3 // 3"],
    "Die Oberfläche einer Kugel ist 4 mal π mal Radius zum Quadrat. Das Volumen ist vier Drittel mal π mal Radius hoch drei. Mit der Oberfläche geht es kürzer: V = O · r : 3.",
    "r² = 36. O = 4π · 36 = 144π cm². V = 4/3 · π · 6³ = 4/3 · 216π = 288π cm³. Kontrolle: 144π · 6 : 3 = 288π.",
    {0: [(12, "fb.potenz.basis_mal_hochzahl", "6 · 2 statt 6² gerechnet", "6 * 2")], 1: [(72, None, "2 mal statt 4 mal gerechnet: 2 · 36", "2 * {1}")], 2: [(864, None, "bei der Kugel das Volumen als O · r statt O · r : 3 gerechnet", "4 * 6 ** 3")]}), regel=None)
neu(T, "kugel", "zwei_wege", Z(
    "Eine Kugel hat den Radius 3 cm. Gib ihr Volumen in der Form V = □ · π cm³ an. Welche Zahl gehört in das Kästchen? Rechne auf zwei Wegen. Weg A: mit der Formel V = 4/3 · π · r³. Weg B: Berechne das Volumen eines Zylinders mit dem Radius 3 cm und der Höhe 6 cm. Ziehe davon die Volumina von zwei Kegeln ab. Beide Kegel haben den Radius 3 cm und die Höhe 3 cm, ihre Spitzen liegen im Mittelpunkt des Zylinders, ihre Grundflächen sind Boden und Deckel. Der Rest hat dasselbe Volumen wie die Kugel, weil in jeder Höhe der Querschnitt des Rests (ein Kreisring) denselben Flächeninhalt hat wie der Querschnitt der Kugel (eine Kreisscheibe).",
    36, "4 * 3 ** 3 / 3", "2 * 3 ** 3 - 2 * (3 ** 2 * 3 / 3)", "Beide Wege müssen dieselbe Zahl ergeben. Bei Weg B rechnest du das Volumen des Zylinders und das der beiden Kegel jeweils in Vielfachen von π.",
    "Weg A: V = 4/3 · π · 27 = 36π cm³. Weg B: Zylinder: π · 3² · 6 = 54π. Ein Kegel: π · 3² · 3 : 3 = 9π, zwei Kegel 18π. Rest: 54π − 18π = 36π cm³. Beide Wege: 36.",
    [(108, None, "den Faktor 1/3 der Kugelformel vergessen: 4 · 27", "4 * 27"), (12, None, "r² statt r³ genommen: 4 · 3² : 3", "4 * 9 / 3"), (54, None, "nur das Volumen des Zylinders angegeben", "2 * 27")]), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "kugel", "umkehren", Z(
    "Eine Kugel hat die Oberfläche 324π cm². Gib ihr Volumen in der Form V = □ · π cm³ an. Welche Zahl gehört in das Kästchen?",
    972, "4 * wurzel(324 / 4) ** 3 / 3", "4 / 3 * 9 ** 3", "Welche Größe der Kugel kannst du aus der Oberfläche bestimmen? Was brauchst du dann für das Volumen?",
    "4 · r² = 324, also r² = 81 und r = 9 cm. V = 4/3 · π · 9³ = 4/3 · 729π = 972π cm³.",
    [(729, None, "nur r³ gerechnet: der ganze Faktor vier Drittel fehlt", "9 ** 3"), (108, None, "r² statt r³ genommen", "4 * 9 ** 2 / 3"), (324, None, "die Oberfläche als Volumen angegeben", "324")]), g="rueckwaerts", regel=None)

# ───────── sachkontext ─────────
neu(T, "sachkontext", "lueckenweg", L(
    "Eine Eiswaffel hat die Form eines geraden Kegels mit dem Radius 3 cm und der Höhe 9 cm. Auf der Öffnung liegt eine halbe Eiskugel mit demselben Radius. Rechne mit π ≈ 3. Das Volumen des Kegels ist ① cm³. Das Volumen der halben Kugel ist ② cm³. Zusammen sind das ③ cm³.",
    "① = □; ② = □; ③ = □", [81, 54, 135], ["3 * 3 ** 2 * 9 / 3", "4 * 3 * 3 ** 3 / 3 / 2", "{1} + {2}"], ["3 * 9 * 9 // 3", "2 * 3 * 27 // 3", "81 + 54"],
    "Das Volumen der Waffel ist das Volumen eines Kegels. Eine halbe Kugel ist die Hälfte einer ganzen Kugel.",
    "Kegel: V = 3 · 3² · 9 : 3 = 81 cm³. Ganze Kugel: 4/3 · 3 · 3³ = 108 cm³, halbe Kugel: 54 cm³. Zusammen: 81 + 54 = 135 cm³.",
    {0: [(243, DR, "den Faktor ein Drittel vergessen: 3 · 9 · 9", "3 * 3 ** 2 * 9")], 1: [(108, None, "die ganze Kugel statt der halben gerechnet", "4 * 3 * 3 ** 3 / 3")], 2: [(81, None, "nur den Kegel gezählt", "{1}")]}), regel=R)
neu(T, "sachkontext", "anwenden", Z(
    "Ein kugelförmiger Wassertank hat den Innendurchmesser 2 m. Wie groß ist das Fassungsvermögen des Tanks in Litern? Rechne mit π ≈ 3,14 und 1 m³ = 1 000 Liter. Runde das Ergebnis auf ganze Liter.",
    4187, "round(4 * 3.14 * 1 ** 3 / 3 * 1000, 0)", "round(4 / 3 * 3.14 * 1000, 0)", "Der Radius ist halb so groß wie der Durchmesser. Rechne das Volumen zuerst in m³, dann in Liter.",
    "r = 1 m. V = 4/3 · 3,14 · 1³ ≈ 4,1867 m³. In Liter: 4,1867 · 1 000 ≈ 4 187 l. Es passen etwa 4 187 Liter hinein.",
    [(12560, None, "den Faktor 1/3 der Kugelformel vergessen: 4 · 3,14 · 1 000", "4 * 3.14 * 1000"), (33493, None, "den Durchmesser 2 m als Radius genommen (gerundet)", "round(4 / 3 * 3.14 * 2 ** 3 * 1000, 0)")], "Liter"), g="einkleidung", regel=None)
neu(T, "sachkontext", "umkehren", Z(
    "Eine Wachskugel mit dem Radius 6 cm wird vollständig eingeschmolzen. Aus dem Wachs wird ein gerader Kegel mit dem Radius 6 cm gegossen. Das Volumen bleibt dabei gleich. Wie hoch ist der Kegel?",
    24, "4 * 6 ** 3 / 3 * 3 / 6 ** 2", "(4 / 3 * 6 ** 3) / (6 ** 2 / 3)", "Beim Einschmelzen und Neugießen ändert sich das Volumen nicht.",
    "Kugel: V = 4/3 · π · 6³ = 288π cm³. Kegel: π · 6² · h : 3 = 12π · h. Aus 12π · h = 288π folgt h = 24 cm.",
    [(8, DR, "bei der Höhe den Faktor 3 vergessen: 288 : 36", "288 / 36"), (4, None, "für die Kugel r² statt r³ genommen: 4/3 · 36 = 48, dann 48 · 3 : 36", "4 * 6 ** 2 / 3 * 3 / 6 ** 2")], "cm"), g="rueckwaerts", regel=R)

# ───────── verstehen ─────────
neu(T, "verstehen", "lueckenweg", L(
    "Eine gerade Pyramide hat als Grundfläche ein Quadrat mit der Kantenlänge 3 cm und ist 6 cm hoch. Ihr Volumen ist ① cm³. Eine zweite Pyramide hat dieselbe Höhe, aber ein Quadrat mit der Kantenlänge 6 cm als Grundfläche. Ihr Volumen ist ② cm³. Das Volumen der zweiten Pyramide ist ③-mal so groß wie das der ersten.",
    "① = □; ② = □; ③ = □", [18, 72, 4], ["3 * 3 * 6 / 3", "6 * 6 * 6 / 3", "{2} / {1}"], ["18", "72", "72 // 18"],
    "Rechne beide Volumina aus und vergleiche sie mit einer Division. Die Grundkante wird bei der Grundfläche quadriert.",
    "V₁ = 3 · 3 · 6 : 3 = 18 cm³. V₂ = 6 · 6 · 6 : 3 = 72 cm³. 72 : 18 = 4. Die Kante wurde verdoppelt, das Volumen wurde 4-mal so groß.",
    {0: [(54, DR, "den Faktor ein Drittel vergessen: 3 · 3 · 6", "3 * 3 * 6")], 1: [(36, None, "nur doppeltes Volumen angenommen: 2 · 18", "2 * {1}")], 2: [(2, None, "nur die Kanten verglichen: 6 : 3", "6 / 3")]}), regel=R)
neu(T, "verstehen", "bruecke", W(
    "Die Tabelle zeigt das Volumen von drei Kugeln (mit dem genauen Wert von π berechnet und auf zwei Dezimalstellen gerundet). Wie hängt das Volumen vom Radius ab?",
    "Verdoppelt man den Radius, wird das Volumen 8-mal so groß.", [("Verdoppelt man den Radius, wird das Volumen doppelt so groß.", "nur die Radien verglichen"), ("Verdoppelt man den Radius, wird das Volumen 4-mal so groß.", "wie bei der Fläche gerechnet"),
                                                          ("Verdoppelt man den Radius, wird das Volumen 6-mal so groß.", "den Faktor 3 mit 2 malgenommen")],
    "Teile das Volumen bei r = 2 cm durch das Volumen bei r = 1 cm. Teile auch das Volumen bei r = 3 cm durch das bei r = 1 cm.",
    "33,51 : 4,19 ≈ 8 und 113,10 : 4,19 ≈ 27. Die Faktoren sind 2³ und 3³. Das Volumen wächst mit der dritten Potenz des Radius.",
    lambda: abs(33.51 / 4.19 - 8) < 0.05 and abs(113.10 / 4.19 - 27) < 0.1 and round(4 / 3 * math.pi * 8, 2) == 33.51 and round(4 / 3 * math.pi, 2) == 4.19 and round(4 / 3 * math.pi * 27, 2) == 113.10,
    grafik=TAB(["Radius", "Volumen"], ["1 cm", "4,19 cm³"], ["2 cm", "33,51 cm³"], ["3 cm", "113,10 cm³"])), regel=None)
neu(T, "verstehen", "fehler_detektiv", FD(
    "Kim vergleicht einen geraden Kegel mit einem geraden Zylinder. Beide haben denselben Radius und dieselbe Höhe. Der Zylinder hat den Radius 3 cm und die Höhe 5 cm.",
    [("Der Kegel hat die Hälfte des Volumens des Zylinders.", False, True),
     ("Das Volumen des Zylinders ist V = π · 3² · 5 = 45π cm³.", 3 ** 2 * 5 == 45, True),
     ("Also hat der Kegel das Volumen 22,5π cm³.", True, 45 / 2 == 22.5)],
    "Wie viele Kegel mit gleichem Radius und gleicher Höhe passen in Volumen genau in einen Zylinder?",
    "Der Kegel hat ein Drittel des Volumens des Zylinders, nicht die Hälfte: 45π : 3 = 15π cm³. Der erste Fehler steht in Zeile 1.",
    rueck={1: "Diese Zeile ist für sich richtig: V = π · 3² · 5 = 45π cm³. Der erste Fehler steht schon in Zeile 1, bei der Aussage über den Kegel."}), regel=R)
