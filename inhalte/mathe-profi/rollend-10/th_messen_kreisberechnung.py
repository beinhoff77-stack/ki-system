T = "messen.kreisberechnung"
R = "id.flaeche_raum.aus_dem_rechteck"
DM = "fb.aus_dem_rechteck.durchmesser_statt_radius"
# ───────── umfang ─────────
neu(T, "umfang", "lueckenweg", L(
    "Ein Rad hat den Durchmesser 50 cm. Rechne mit π ≈ 3,14. Der Umfang des Rades ist ① cm. Bei 4 Umdrehungen rollt das Rad ② cm weit. Um 1 570 cm weit zu rollen, braucht das Rad ③ Umdrehungen.",
    "① = □; ② = □; ③ = □", [157, 628, 10], ["3.14 * 50", "4 * {1}", "1570 / {1}"], ["157", "4 * 157", "1570 // 157"],
    "Der Umfang eines Kreises ist π mal Durchmesser. Eine Umdrehung entspricht genau einem Umfang.",
    "u = 3,14 · 50 = 157 cm. 4 Umdrehungen: 4 · 157 = 628 cm. 1 570 : 157 = 10 Umdrehungen.",
    {0: [(78.5, None, "den Radius statt des Durchmessers in die Formel u = π · d eingesetzt: 3,14 · 25", "3.14 * 25")], 1: [(161, "fb.verhaeltnis.addiert_statt_malgenommen", "4 addiert statt malgenommen: 157 + 4", "{1} + 4")],
     2: [(1413, None, "den Umfang von der Strecke abgezogen: 1 570 − 157", "1570 - {1}")]}), regel=None)
neu(T, "umfang", "zwei_wege", Z(
    "Ein Kreis mit dem Durchmesser 10 cm hat den Umfang 31,4 cm. Wie groß ist der Umfang eines Kreises mit dem Durchmesser 70 cm? Rechne mit π ≈ 3,14. Weg A: mit der Formel u = π · d. Weg B: Der Umfang ist proportional zum Durchmesser. Der zweite Durchmesser ist ein Vielfaches des ersten, der Umfang wächst mit demselben Faktor.",
    219.8, "3.14 * 70", "31.4 * (70 / 10)", "Beide Wege müssen denselben Umfang ergeben. Bei Weg B brauchst du zuerst den Faktor von 10 cm auf 70 cm.",
    "Weg A: u = 3,14 · 70 = 219,8 cm. Weg B: Faktor 70 : 10 = 7. u = 31,4 · 7 = 219,8 cm.",
    [(439.6, DM, "2 · π · d gerechnet, als wäre d der Radius: 2 · 3,14 · 70", "2 * 3.14 * 70"), (91.4, "fb.verhaeltnis.addiert_statt_malgenommen", "den Unterschied der Durchmesser addiert statt den Faktor zu nehmen: 31,4 + 60", "31.4 + (70 - 10)"), (21.98, None, "nur mit dem Faktor 7 und π gerechnet: 3,14 · 7", "3.14 * 7")], "cm"), regel=None)
neu(T, "umfang", "umkehren", Z(
    "Ein Band ist 94,2 cm lang. Es wird straff und ohne Überlappung genau einmal um einen kreisrunden Baumstamm gelegt und passt genau. Rechne mit π ≈ 3,14. Welchen Radius hat der Querschnitt des Stamms?",
    15, "94.2 / (2 * 3.14)", "94.2 / 3.14 / 2", "Das Band ist so lang wie der Umfang des Querschnitts.",
    "u = 2 · π · r, also r = u : (2 · π) = 94,2 : 6,28 = 15 cm. Probe: 2 · 3,14 · 15 = 94,2.",
    [(30, None, "den Durchmesser (94,2 : 3,14) berechnet, aber der Radius ist gefragt", "94.2 / 3.14"), (7.5, None, "zweimal durch 2 geteilt: 94,2 : 3,14 : 4", "94.2 / 3.14 / 4"), (295.788, None, "Du hast U mit π multipliziert. Für den Radius musst du U durch 2π teilen.", "94.2 * 3.14")], "cm"), g="rueckwaerts", regel=None)

# ───────── flaeche ─────────
neu(T, "flaeche", "lueckenweg", L(
    "Ein Kreis hat den Durchmesser 20 cm. Rechne mit π ≈ 3,14. Der Radius ist ① cm. Das Quadrat des Radius ist ② cm². Der Flächeninhalt des Kreises ist ③ cm².",
    "① = □; ② = □; ③ = □", [10, 100, 314], ["20 / 2", "{1} ** 2", "3.14 * {2}"], ["10", "100", "3.14 * 100"],
    "Die Fläche eines Kreises ist π mal Radius mal Radius. Gegeben ist der Durchmesser.",
    "r = 20 : 2 = 10 cm. r² = 100 cm². A = 3,14 · 100 = 314 cm².",
    {0: [(40, None, "den Durchmesser verdoppelt statt halbiert: 20 · 2", "20 * 2")], 1: [(20, "fb.potenz.basis_mal_hochzahl", "10 · 2 statt 10² gerechnet", "{1} * 2")],
     2: [(62.8, None, "den Umfang statt der Fläche gerechnet: 2 · 3,14 · 10", "2 * 3.14 * {1}")]}), regel=R)
neu(T, "flaeche", "zwei_wege", Z(
    "Ein Kreis hat den Radius 10 cm. Rechne mit π ≈ 3,14. Berechne den Flächeninhalt auf zwei Wegen. Weg A: mit der Formel A = π · r². Weg B: Ein Kreis mit dem Radius 1 cm hat den Flächeninhalt 3,14 cm². Der Kreis mit dem Radius 10 cm entsteht daraus durch Vergrößern mit dem Längenfaktor 10. Wende den passenden Flächenfaktor an.",
    314, "3.14 * 10 ** 2", "3.14 * 100", "Beide Wege müssen denselben Flächeninhalt ergeben. Bei Weg B wird nicht nur eine Länge vergrößert.",
    "Weg A: A = 3,14 · 10² = 314 cm². Weg B: Längenfaktor 10, Flächenfaktor 10² = 100. A = 3,14 · 100 = 314 cm².",
    [(31.4, "fb.aehnlich.flaeche_mit_k", "nur mit dem Längenfaktor 10 vervielfacht: 3,14 · 10", "3.14 * 10"), (62.8, None, "nur den Umfang berechnet: 2 · 3,14 · 10", "2 * 3.14 * 10"), (100, None, "nur den Flächenfaktor 100 als Fläche angegeben", "10 ** 2")], "cm²"), regel=R)
neu(T, "flaeche", "fehler_detektiv", FD(
    "Ein Kreis hat den Durchmesser 12 cm. Kim berechnet den Flächeninhalt mit π ≈ 3,14.",
    [("Der Radius ist r = 12 · 2 = 24 cm.", 12 * 2 == 12 / 2, True),
     ("Die Fläche ist A = 3,14 · 24² = 3,14 · 576 = 1 808,64 cm².", True, 24 ** 2 == 576 and round(3.14 * 576, 2) == 1808.64),
     ("Gerundet auf ganze Quadratzentimeter ist das etwa 1 809 cm².", True, round(1808.64) == 1809)],
    "Wie hängen Durchmesser und Radius zusammen?",
    "Der Radius ist halb so groß wie der Durchmesser: r = 12 : 2 = 6 cm. Dann ist A = 3,14 · 36 = 113,04 cm². Der erste Fehler steht in Zeile 1."), regel=R)

# ───────── exakt ─────────
neu(T, "exakt", "lueckenweg", L(
    "Ein Kreisring liegt zwischen zwei Kreisen mit demselben Mittelpunkt. Der äußere Kreis hat den Radius 9 cm, der innere den Radius 5 cm. Der äußere Kreis hat die Fläche ① · π cm². Der innere Kreis hat die Fläche ② · π cm². Der Kreisring hat die Fläche ③ · π cm².",
    "① = □; ② = □; ③ = □", [81, 25, 56], ["9 ** 2", "5 ** 2", "{1} - {2}"], ["81", "25", "81 - 25"],
    "Die Fläche eines Kreises ist π mal Radius zum Quadrat. Den Ring erhältst du durch Abziehen.",
    "Außen: 9² = 81, also 81π cm². Innen: 5² = 25, also 25π cm². Ring: 81π − 25π = 56π cm².",
    {0: [(18, "fb.potenz.basis_mal_hochzahl", "9 · 2 statt 9² gerechnet", "9 * 2")], 1: [(10, "fb.potenz.basis_mal_hochzahl", "5 · 2 statt 5² gerechnet", "5 * 2")], 2: [(16, None, "erst die beiden Radien voneinander abgezogen und dann quadriert", "(9 - 5) ** 2")]}), regel=R)
neu(T, "exakt", "bruecke", W(
    "Ein Kreis hat den Flächeninhalt 49π cm². Welcher Wert ist der Flächeninhalt als Dezimalzahl, wenn man mit π ≈ 3,14 rechnet?",
    "153,86 cm²", [("21,98 cm²", "nur 7 · 3,14 gerechnet: aus 49 die Wurzel gezogen"), ("307,72 cm²", "98 · 3,14 gerechnet, die 49 verdoppelt"), ("52,14 cm²", "49 + 3,14 gerechnet, statt mit π zu multiplizieren")],
    "In 49π steht ein Malzeichen zwischen 49 und π. Setze für π die Näherung ein.",
    "49π bedeutet 49 · π. Mit π ≈ 3,14: 49 · 3,14 = 153,86 cm².",
    lambda: round(49 * 3.14, 2) == 153.86 and round(7 * 3.14, 2) == 21.98 and round(98 * 3.14, 2) == 307.72 and round(49 + 3.14, 2) == 52.14), regel=R)
neu(T, "exakt", "umkehren", Z(
    "Ein Kreisring liegt zwischen zwei Kreisen mit demselben Mittelpunkt. Der äußere Kreis hat den Umfang 20π cm, der innere den Umfang 12π cm. Gib den Flächeninhalt des Kreisrings exakt an: A = □ · π cm². Welche Zahl gehört in das Kästchen?",
    64, "(20 / 2) ** 2 - (12 / 2) ** 2", "10 * 10 - 6 * 6", "Von den Umfängen kommst du zu den Radien. Der Ring ist der Rest, wenn du den inneren Kreis wegnimmst.",
    "u = 2π · r. Außen: 20π = 2π · r, also r = 10 cm. Innen: 12π = 2π · r, also r = 6 cm. Ring: π · 10² − π · 6² = 100π − 36π = 64π cm².",
    [(16, None, "erst die Radien voneinander abgezogen und dann quadriert", "(10 - 6) ** 2"), (256, None, "die Zahlen 20 und 12 statt der Radien quadriert: 20² − 12²", "20 ** 2 - 12 ** 2"), (8, None, "nur den Unterschied der Umfänge genommen: 20 − 12", "20 - 12")]), g="rueckwaerts", regel=R)

# ───────── verstehen ─────────
neu(T, "verstehen", "lueckenweg", L(
    "Ein Kreis hat den Radius 3 cm, ein zweiter Kreis den Radius 6 cm. Der erste Kreis hat die Fläche ① · π cm², der zweite ② · π cm². Die zweite Fläche ist ③-mal so groß wie die erste.",
    "① = □; ② = □; ③ = □", [9, 36, 4], ["3 ** 2", "6 ** 2", "{2} / {1}"], ["9", "36", "36 // 9"],
    "Die Fläche eines Kreises ist π mal Radius zum Quadrat. Vergleiche die beiden Flächen mit einer Division.",
    "A₁ = π · 3² = 9π. A₂ = π · 6² = 36π. 36 : 9 = 4. Der Radius ist 2-mal so groß, die Fläche 4-mal so groß.",
    {0: [(6, "fb.potenz.basis_mal_hochzahl", "3 · 2 statt 3² gerechnet", "3 * 2")], 1: [(12, "fb.potenz.basis_mal_hochzahl", "6 · 2 statt 6² gerechnet", "6 * 2")], 2: [(2, None, "nur die Radien verglichen: 6 : 3", "6 / 3")]}), regel=R)
neu(T, "verstehen", "bruecke", W(
    "Die Tabelle zeigt Umfang und Fläche von drei Kreisen mit den Radien 1 cm, 2 cm und 3 cm (π ≈ 3,14). Der Radius wird von 1 cm auf 2 cm verdoppelt. Was passiert mit Umfang und Fläche?",
    "Der Umfang wird doppelt so groß, die Fläche wird viermal so groß.", [("Der Umfang und die Fläche werden beide doppelt so groß.", "nur den Umfang gelesen und für die Fläche übernommen"), ("Der Umfang wird viermal so groß, die Fläche doppelt so groß.", "Umfang und Fläche vertauscht"),
                                                                      ("Der Umfang und die Fläche werden beide viermal so groß.", "die Fläche gelesen und für den Umfang übernommen")],
    "Teile in der Tabelle den Wert für r = 2 cm durch den Wert für r = 1 cm, einmal beim Umfang und einmal bei der Fläche.",
    "Umfang: 12,56 : 6,28 = 2. Fläche: 12,56 : 3,14 = 4. Der Umfang wächst mit dem Radius (Faktor 2), die Fläche mit dem Quadrat des Radius (Faktor 4).",
    lambda: round(12.56 / 6.28, 6) == 2 and round(12.56 / 3.14, 6) == 4 and round(2 * 3.14 * 2, 2) == 12.56 and round(3.14 * 4, 2) == 12.56,
    grafik=TAB(["Radius", "Umfang", "Fläche"], ["1 cm", "6,28 cm", "3,14 cm²"], ["2 cm", "12,56 cm", "12,56 cm²"], ["3 cm", "18,84 cm", "28,26 cm²"])), regel=R)
neu(T, "verstehen", "fehler_detektiv", FD(
    "Kim untersucht, was mit der Fläche eines Kreises passiert, wenn man den Radius verdoppelt.",
    [("Die Fläche eines Kreises mit dem Radius r ist A = π · r².", True, True),
     ("Mit dem Radius 2r ist die neue Fläche A' = π · (2r)² = π · 2r² = 2πr².", False, True),
     ("Also ist A' doppelt so groß wie A.", False, True)],
    "Was bedeutet (2r)²? Probiere es mit r = 1.",
    "(2r)² = 2r · 2r = 4r². Also ist A' = 4πr², die Fläche wird 4-mal so groß. Probe mit r = 1: A = π, A' = π · 2² = 4π. Der Fehler steckt in Zeile 2."), regel=R)

# ───────── sektor ─────────
neu(T, "sektor", "lueckenweg", L(
    "Ein Kreissektor hat den Radius 12 cm und den Mittelpunktswinkel 90°. Der Sektor ist 1/① des ganzen Kreises. Der ganze Kreis hat die Fläche ② · π cm². Der Sektor hat die Fläche ③ · π cm².",
    "① = □; ② = □; ③ = □", [4, 144, 36], ["360 // 90", "12 ** 2", "{2} / {1}"], ["4", "144", "144 // 4"],
    "Der volle Winkel um einen Punkt ist 360°. Der Sektor hat denselben Anteil an der Fläche wie sein Winkel am vollen Winkel.",
    "360 : 90 = 4, der Sektor ist ein Viertel. Ganzer Kreis: 12² = 144, also 144π cm². Sektor: 144π : 4 = 36π cm².",
    {0: [(270, None, "den Unterschied zum vollen Winkel genommen: 360 − 90", "360 - 90")], 1: [(576, DM, "mit dem Durchmesser statt dem Radius gerechnet: 24²", "(2 * 12) ** 2")], 2: [(144, None, "die Fläche des ganzen Kreises angegeben", "{2}")]}), regel=R)
wert_sc, c_sc = rd("3.14 * 40 ** 2 * 110 / 360", 0)
neu(T, "sektor", "anwenden", Z(
    "Ein Scheibenwischer wird als Strecke vom Drehpunkt bis zum Ende des Wischblatts angenommen und ist 40 cm lang. Er schwenkt um 110° und überstreicht dabei einen Kreissektor. Wie groß ist die überstrichene Fläche? Rechne mit π ≈ 3,14 und runde auf ganze cm².",
    wert_sc, c_sc, "round(3.14 * 1600 * 110 / 360, 0)", "Der Sektor ist ein Anteil des Kreises mit Radius 40 cm. Der Anteil ist Winkel durch 360°.",
    "Kreisfläche: 3,14 · 40² = 5 024 cm². Anteil: 110 : 360. Sektor: 5 024 · 110 : 360 ≈ 1 535,1 cm². Gerundet 1 535 cm².",
    [(5024, None, "die Fläche des ganzen Kreises angegeben", "3.14 * 40 ** 2"), (77, None, "die Bogenlänge statt der Fläche berechnet (gerundet)", "round(2 * 3.14 * 40 * 110 / 360, 0)")], "cm²"), g="einkleidung", regel=R)
assert wert_sc == 1535
neu(T, "sektor", "umkehren", Z(
    "Ein Kreissektor hat den Radius 6 cm und die Bogenlänge 3π cm. Gib seinen Flächeninhalt exakt an: A = □ · π cm². Welche Zahl gehört in das Kästchen?",
    9, "(3 / (2 * 6)) * 6 ** 2", "3 * 6 / 2", "Die Bogenlänge ist ein Anteil des Umfangs des ganzen Kreises. Derselbe Anteil gilt für die Fläche.",
    "Umfang des ganzen Kreises: 2π · 6 = 12π cm. Anteil: 3π : 12π = 1/4. Fläche des ganzen Kreises: 36π cm². Sektor: 36π : 4 = 9π cm². Probe: Bogenlänge · Radius : 2 = 3π · 6 : 2 = 9π.",
    [(18, None, "Bogenlänge mal Radius ohne Halbieren: 3 · 6", "3 * 6"), (36, None, "die Fläche des ganzen Kreises angegeben", "6 ** 2"), (4, None, "nur den Nenner des Anteils angegeben: 12 : 3", "12 / 3")]), g="rueckwaerts", regel=R)

# ───────── zusammengesetzt ─────────
neu(T, "zusammengesetzt", "lueckenweg", L(
    "Eine Fensterform besteht aus einem Rechteck, 8 cm breit und 6 cm hoch. Auf die 8 cm lange Seite ist ein Halbkreis aufgesetzt. Rechne mit π ≈ 3. Das Rechteck hat die Fläche ① cm². Der Halbkreis hat die Fläche ② cm². Die ganze Form hat die Fläche ③ cm².",
    "① = □; ② = □; ③ = □", [48, 24, 72], ["8 * 6", "3 * 4 ** 2 / 2", "{1} + {2}"], ["48", "3 * 16 // 2", "72"],
    "Der Durchmesser des Halbkreises ist die aufgesetzte Seite. Berechne zuerst die Fläche eines ganzen Kreises und nimm davon die Hälfte.",
    "Rechteck: 8 · 6 = 48 cm². Halbkreis: Radius 4 cm, Kreis 3 · 4² = 48, Hälfte 24 cm². Gesamt: 48 + 24 = 72 cm².",
    {0: [(14, None, "die Seiten addiert: 8 + 6", "8 + 6")], 1: [(48, None, "den ganzen Kreis statt des Halbkreises gerechnet", "3 * 4 ** 2")], 2: [(96, None, "den Halbkreis doppelt gezählt: 48 + 2 · 24", "{1} + 2 * {2}")]}), regel=R)
neu(T, "zusammengesetzt", "bruecke", W(
    "Aus einer rechteckigen Platte, 12 cm lang und 8 cm breit, wird in der Mitte ein kreisrundes Loch mit dem Durchmesser 6 cm ausgeschnitten. Das Loch liegt ganz in der Platte. Welcher Term gibt den Flächeninhalt der Platte nach dem Ausschneiden an (in cm²)?",
    "12 · 8 − π · 3²", [("12 · 8 − π · 6²", "mit dem Durchmesser statt dem Radius gerechnet"), ("12 · 8 − 2 · π · 3", "den Umfang statt der Fläche abgezogen"), ("12 · 8 + π · 3²", "die Fläche des Lochs addiert statt abgezogen")],
    "Von der Fläche des Rechtecks wird die Fläche des Lochs abgezogen. Die Fläche des Lochs ist ein Kreis.",
    "Rechteck: 12 · 8. Loch: Radius 6 : 2 = 3 cm, Fläche π · 3². Rest: 12 · 8 − π · 3² ≈ 96 − 28,3 = 67,7 cm².",
    lambda: 6 / 2 == 3 and abs(12 * 8 - math.pi * 9 - 67.7) < 0.05 and 12 * 8 - math.pi * 36 != 12 * 8 - math.pi * 9), regel=R)
neu(T, "zusammengesetzt", "anwenden", Z(
    "Ein Sportplatz besteht aus einem Rechteck, 100 m lang und 60 m breit. An den beiden schmalen Seiten ist je ein Halbkreis mit dem Durchmesser 60 m angesetzt. Die ganze Fläche soll mit Kunstrasen belegt werden. Der Kunstrasen wird in Rollen zu je 20 m² geliefert. Rechne mit π ≈ 3,14. Wie viele Rollen müssen mindestens bestellt werden?",
    442, "(100 * 60 + 3.14 * 30 ** 2 + 19) // 20", "-(-8826 // 20)", "Berechne zuerst die ganze Fläche des Platzes. Eine angefangene Rolle muss ganz bestellt werden.",
    "Rechteck: 100 · 60 = 6 000 m². Die zwei Halbkreise ergeben einen Kreis mit r = 30 m: 3,14 · 30² = 2 826 m². Gesamt: 8 826 m². 8 826 : 20 = 441,3. Es müssen 442 Rollen bestellt werden.",
    [(441, None, "abgerundet statt aufgerundet: 441,3 → 441", "(8826) // 20"), (371, None, "nur einen Halbkreis gezählt und die Rollen aufgerundet", "(7413 + 19) // 20"), (300, None, "nur das Rechteck gerechnet: 6 000 : 20", "6000 / 20")], ), g="transfer", regel=R)
