T = "trigo.pythagoras"
R = "id.geometrie.rechtwinklig"
# ───────── hypotenuse ─────────
neu(T, "hypotenuse", "lueckenweg", L(
    "Ein Dreieck ABC hat bei C einen rechten Winkel. Es gilt AC = 20 cm und BC = 21 cm. Gesucht ist die Länge der Hypotenuse AB. Das Quadrat über AC hat den Flächeninhalt ① cm², das Quadrat über BC hat ② cm². Beide Quadrate zusammen haben ③ cm². Die Hypotenuse AB ist ④ cm lang.",
    "① = □; ② = □; ③ = □; ④ = □", [400, 441, 841, 29], ["20 ** 2", "21 ** 2", "{1} + {2}", "wurzel({3})"], ["400", "441", "400 + 441", "sqrt(841)"],
    "Die Quadrate über den beiden Katheten ergeben zusammen das Quadrat über der Hypotenuse. Die Seitenlänge erhältst du aus dem Flächeninhalt des Quadrats.",
    "AC² = 20² = 400. BC² = 21² = 441. AB² = 400 + 441 = 841. AB = √841 = 29 cm.",
    {0: [(40, "fb.potenz.basis_mal_hochzahl", "20 · 2 statt 20² gerechnet", "20 * 2")], 1: [(42, "fb.potenz.basis_mal_hochzahl", "21 · 2 statt 21² gerechnet", "21 * 2")],
     2: [(41, "fb.rechtwinklig.ohne_quadrate", "die Seitenlängen 20 + 21 statt der Quadrate addiert", "20 + 21")], 3: [(841, None, "die Wurzel nicht gezogen: AB² als Länge angegeben", "{3}")]}), regel=R)

_c, _zw = 5, 12
neu(T, "hypotenuse", "zwei_wege", Z(
    "Ein Dreieck hat bei C einen rechten Winkel. Die Katheten sind 5 cm und 12 cm lang. Berechne die Länge der Hypotenuse auf zwei Wegen. Weg A: Satz des Pythagoras. Weg B: Lege vier Kopien des Dreiecks so um ein Quadrat, dass ein großes Quadrat mit der Seitenlänge 17 cm entsteht (5 cm + 12 cm). In der Mitte bleibt ein Quadrat, dessen Seite die Hypotenuse ist. Seine Fläche ist die Fläche des großen Quadrats minus die Fläche der vier Dreiecke. Wie lang ist die Hypotenuse?",
    13, "wurzel(5 ** 2 + 12 ** 2)", "sqrt((5 + 12) ** 2 - 4 * (5 * 12 / 2))", "Beide Wege müssen dieselbe Länge ergeben. Bei Weg B erhältst du zuerst eine Fläche.",
    "Weg A: c² = 5² + 12² = 25 + 144 = 169, c = 13 cm. Weg B: großes Quadrat 17² = 289 cm², vier Dreiecke 4 · (5 · 12 : 2) = 120 cm². Mittleres Quadrat: 289 − 120 = 169 cm², Seite √169 = 13 cm. Beide Wege führen auf 13 cm.",
    [(169, None, "die Wurzel nicht gezogen: die Fläche 169 cm² als Länge angegeben", "5 ** 2 + 12 ** 2"), (17, "fb.rechtwinklig.ohne_quadrate", "die Katheten addiert: 5 + 12", "5 + 12"), (7, None, "die Katheten subtrahiert: 12 − 5", "12 - 5")], "cm"), regel=R)
wert_tv, c_tv = rd("sqrt(70 ** 2 + 40 ** 2) / 2.54", 0)
neu(T, "hypotenuse", "anwenden", Z(
    "Der rechteckige Bildschirm eines Fernsehers ist 70 cm breit und 40 cm hoch. Die Größe eines Bildschirms wird als Länge seiner Diagonalen in Zoll angegeben. Es gilt 1 Zoll = 2,54 cm. Wie groß ist dieser Bildschirm? Runde auf ganze Zoll.",
    wert_tv, c_tv, "round(sqrt(4900 + 1600) / 2.54, 0)", "Die Diagonale teilt das Rechteck in zwei rechtwinklige Dreiecke. Rechne am Ende von cm in Zoll um.",
    "Diagonale: d² = 70² + 40² = 4 900 + 1 600 = 6 500, d = √6 500 ≈ 80,6 cm. 80,6 : 2,54 ≈ 31,7. Der Bildschirm hat etwa 32 Zoll.",
    [(81, None, "die Diagonale in cm gerundet, die Umrechnung in Zoll vergessen", "round(sqrt(70 ** 2 + 40 ** 2), 0)"), (43, "fb.rechtwinklig.ohne_quadrate", "Breite plus Höhe (110 cm) statt der Diagonalen in Zoll umgerechnet", "round((70 + 40) / 2.54, 0)")], "Zoll"), g="einkleidung", regel=R)
assert wert_tv == 32

# ───────── kathete ─────────
neu(T, "kathete", "lueckenweg", L(
    "Ein Dreieck ABC hat bei C einen rechten Winkel. Die Hypotenuse AB ist 26 cm lang, die Kathete AC ist 10 cm lang. Gesucht ist die Kathete BC. Das Quadrat über AB hat den Flächeninhalt ① cm², das Quadrat über AC hat ② cm². Das Quadrat über BC hat ③ cm². Die Kathete BC ist ④ cm lang.",
    "① = □; ② = □; ③ = □; ④ = □", [676, 100, 576, 24], ["26 ** 2", "10 ** 2", "{1} - {2}", "wurzel({3})"], ["676", "100", "676 - 100", "sqrt(576)"],
    "Die beiden Quadrate über den Katheten ergeben zusammen das Quadrat über der Hypotenuse. Ein Summand fehlt dir.",
    "AB² = 26² = 676. AC² = 10² = 100. BC² = 676 − 100 = 576. BC = √576 = 24 cm.",
    {0: [(52, "fb.potenz.basis_mal_hochzahl", "26 · 2 statt 26² gerechnet", "26 * 2")], 1: [(20, "fb.potenz.basis_mal_hochzahl", "10 · 2 statt 10² gerechnet", "10 * 2")],
     2: [(776, "fb.rechtwinklig.kathete_als_hypotenuse", "addiert statt subtrahiert: 676 + 100", "{1} + {2}")], 3: [(576, None, "die Wurzel nicht gezogen: BC² als Länge angegeben", "{3}")]}), regel=R)
neu(T, "kathete", "bruecke", Z(
    "Über den Seiten eines Dreiecks ABC mit einem rechten Winkel bei C stehen Quadrate. Die Tabelle zeigt die Flächeninhalte von zwei dieser Quadrate. Wie lang ist die Seite AC?",
    16, "wurzel(400 - 144)", "sqrt(20 ** 2 - 12 ** 2)", "Die Quadratfläche über der Hypotenuse ist so groß wie die beiden Quadrate über den Katheten zusammen. Aus der Fläche eines Quadrats erhältst du seine Seitenlänge.",
    "Das Quadrat über AB (Hypotenuse) hat 400 cm². Das Quadrat über AC hat 400 − 144 = 256 cm². Seitenlänge: √256 = 16 cm. Probe: 144 + 256 = 400.",
    [(256, None, "die Quadratfläche 256 cm² als Seitenlänge angegeben", "400 - 144"), (544, "fb.rechtwinklig.kathete_als_hypotenuse", "die Flächen addiert: 400 + 144 (Fläche statt Länge)", "400 + 144"), (8, None, "erst die Wurzeln gezogen, dann subtrahiert: 20 − 12", "wurzel(400) - wurzel(144)")], "cm",
    grafik=TAB(["Seite", "Lage im Dreieck", "Fläche des Quadrats über der Seite"], ["BC", "Kathete", "144 cm²"], ["AB", "Hypotenuse", "400 cm²"])), regel=R)
neu(T, "kathete", "fehler_detektiv", FD(
    "Kim berechnet die Kathete b eines Dreiecks mit einem rechten Winkel. Die Hypotenuse ist c = 17 cm, die andere Kathete ist a = 8 cm.",
    [("c² = 17² = 289 und a² = 8² = 64.", 17 ** 2 == 289 and 8 ** 2 == 64, True),
     ("b² = c² + a² = 289 + 64 = 353.", 289 - 64 == 353, 289 + 64 == 353),
     ("b = √353 ≈ 18,8 cm.", False, round(math.sqrt(353), 1) == 18.8)],
    "Welche Seite ist die längste im rechtwinkligen Dreieck? Welches Quadrat ist die Summe der beiden anderen?",
    "Die Hypotenuse c steht allein: c² = a² + b². Also ist b² = c² − a² = 289 − 64 = 225 und b = 15 cm. Kim hat in Zeile 2 addiert statt subtrahiert."), regel=R)

# ───────── umkehrung ─────────
neu(T, "umkehrung", "lueckenweg", L(
    "Ein Dreieck hat die Seitenlängen 10 cm, 11 cm und 15 cm. Ob es einen rechten Winkel hat, prüfst du mit den Quadraten der Seitenlängen. Das Quadrat der Seite 10 cm ist ① cm², das Quadrat der Seite 11 cm ist ② cm². Beide zusammen sind ③ cm². Das Quadrat der längsten Seite ist ④ cm². Der Unterschied zwischen ④ und ③ ist ⑤. Nur bei einem Unterschied von null wäre das Dreieck rechtwinklig.",
    "① = □; ② = □; ③ = □; ④ = □; ⑤ = □", [100, 121, 221, 225, 4], ["10 ** 2", "11 ** 2", "{1} + {2}", "15 ** 2", "{4} - {3}"], ["100", "121", "100 + 121", "225", "225 - 221"],
    "Die Umkehrung des Satzes von Pythagoras vergleicht zwei Flächen: das Quadrat der längsten Seite und die Summe der Quadrate der beiden kürzeren Seiten.",
    "10² = 100, 11² = 121, Summe 221. 15² = 225. Unterschied 225 − 221 = 4, nicht null. Das Dreieck hat keinen rechten Winkel.",
    {2: [(21, "fb.rechtwinklig.ohne_quadrate", "die Seitenlängen 10 + 11 statt ihrer Quadrate addiert", "10 + 11")], 3: [(15, None, "die längste Seite nicht quadriert", "15")], 4: [(125, None, "das Quadrat der längsten Seite mit nur einem Quadrat verglichen: 225 − 100", "{4} - {1}")]}), regel=R)
neu(T, "umkehrung", "bruecke", W(
    "Über den drei Seiten eines Dreiecks stehen Quadrate. Die Tabelle zeigt ihre Flächeninhalte. Was stimmt?",
    "Das Dreieck hat einen rechten Winkel. Er liegt gegenüber der Seite mit dem Quadrat 85 cm².",
    [("Das Dreieck hat einen rechten Winkel. Er liegt gegenüber der Seite mit dem Quadrat 36 cm².", "die Lage des rechten Winkels verwechselt: er liegt gegenüber der längsten Seite"),
     ("Das Dreieck hat keinen rechten Winkel, denn 85 ist keine Quadratzahl.", "die Seitenlängen müssen nicht ganzzahlig sein"),
     ("Das Dreieck hat keinen rechten Winkel, denn 36 + 85 ist nicht 49.", "die falschen zwei Flächen addiert")],
    "Vergleiche die größte Quadratfläche mit der Summe der beiden anderen.",
    "36 + 49 = 85. Die Summe der beiden kleineren Quadrate ist so groß wie das größte Quadrat. Nach der Umkehrung des Satzes von Pythagoras ist das Dreieck rechtwinklig. Der rechte Winkel liegt der längsten Seite gegenüber, also der Seite mit dem Quadrat 85 cm².",
    lambda: 36 + 49 == 85 and 36 + 85 != 49 and math.sqrt(85) != int(math.sqrt(85)),
    grafik=TAB(["Seite", "Fläche des Quadrats über der Seite"], ["a", "36 cm²"], ["b", "49 cm²"], ["c", "85 cm²"])), regel=R)
neu(T, "umkehrung", "verfahren_waehlen", W(
    "Ein Dreieck hat die Seitenlängen 20 cm, 21 cm und 29 cm. Du willst genau prüfen, ob es einen rechten Winkel hat. Welcher Rechenweg ist richtig?",
    "Das Quadrat der längsten Seite mit der Summe der Quadrate der beiden anderen Seiten vergleichen: 29² und 20² + 21²",
    [("Die längste Seite mit der Summe der beiden anderen Seiten vergleichen: 29 und 20 + 21", "ohne Quadrate gerechnet; das prüft nur, ob ein Dreieck überhaupt möglich ist"),
     ("Das Quadrat der kürzesten Seite mit der Summe der Quadrate der beiden anderen vergleichen: 20² und 21² + 29²", "die falsche Seite als Hypotenuse genommen"),
     ("Alle drei Quadrate addieren und prüfen, ob die Summe eine Quadratzahl ist: 20² + 21² + 29²", "die längste Seite zur Summe gezählt")],
    "Welche Seite liegt dem rechten Winkel gegenüber, wenn es einen gibt?",
    "Der rechte Winkel läge der längsten Seite gegenüber. Also vergleicht man 29² = 841 mit 20² + 21² = 400 + 441 = 841. Beides ist gleich, das Dreieck ist rechtwinklig.",
    lambda: 29 ** 2 == 20 ** 2 + 21 ** 2 and 20 ** 2 != 21 ** 2 + 29 ** 2 and 20 ** 2 + 21 ** 2 + 29 ** 2 == 1682 and math.isqrt(1682) ** 2 != 1682), g="erkennen", regel=R)

# ───────── koordinaten ─────────
neu(T, "koordinaten", "lueckenweg", L(
    "Im Koordinatensystem liegen die Punkte A(−2 | 1) und B(7 | 13). Die Einheit auf beiden Achsen ist 1 cm. Der Unterschied der x-Koordinaten von A und B ist ① cm. Der Unterschied der y-Koordinaten ist ② cm. Diese beiden Unterschiede sind die Katheten eines rechtwinkligen Dreiecks, dessen Hypotenuse die Strecke AB ist. Die Strecke AB ist ③ cm lang.",
    "① = □; ② = □; ③ = □", [9, 12, 15], ["7 - (-2)", "13 - 1", "wurzel({1} ** 2 + {2} ** 2)"], ["9", "12", "sqrt(81 + 144)"],
    "Der Unterschied zweier Koordinaten ist die größere Zahl minus die kleinere Zahl. Vorsicht bei negativen Zahlen.",
    "x: 7 − (−2) = 9. y: 13 − 1 = 12. AB² = 9² + 12² = 81 + 144 = 225, AB = 15 cm.",
    {0: [(5, None, "−2 + 7 gerechnet: das Vorzeichen von −2 nicht beachtet", "-2 + 7")], 1: [(14, None, "13 + 1 gerechnet statt zu subtrahieren", "13 + 1")], 2: [(21, "fb.rechtwinklig.ohne_quadrate", "die beiden Unterschiede addiert: 9 + 12", "{1} + {2}"), (225, None, "die Wurzel nicht gezogen", "{1} ** 2 + {2} ** 2")]}), regel=R)
neu(T, "koordinaten", "umkehren", Z(
    "Die Punkte A(1 | 2) und B(6 | y) haben den Abstand 13 Längeneinheiten voneinander. Es gilt y > 2. Wie groß ist y?",
    14, "2 + wurzel(13 ** 2 - 5 ** 2)", "2 + sqrt(13 ** 2 - (6 - 1) ** 2)", "Der Abstand ist die Hypotenuse. Ein Unterschied der Koordinaten ist bekannt. Der andere Unterschied ist die fehlende Kathete.",
    "Unterschied der x-Koordinaten: 6 − 1 = 5. Dann (y − 2)² = 13² − 5² = 169 − 25 = 144, also y − 2 = 12 (wegen y > 2). y = 14. Probe: Abstand √(5² + 12²) = 13.",
    [(12, None, "nur den Unterschied y − 2 angegeben, nicht y selbst", "wurzel(13 ** 2 - 5 ** 2)"), (-10, None, "in die andere Richtung gerechnet: 2 − 12, obwohl y > 2 verlangt ist", "2 - 12"), (18, None, "Abstand und x-Unterschied addiert: 13 + 5", "13 + 5")]), g="rueckwaerts", regel=R)
wert_dr, c_dr = rd("100 * sqrt(7 ** 2 + 6 ** 2)", 0)
neu(T, "koordinaten", "anwenden", Z(
    "Eine Drohne soll in gerader Linie vom Startpunkt S(3 | 2) zum Landeplatz L(10 | 8) fliegen. Die Punkte stammen aus einem Plan, in dem jede Einheit des Koordinatensystems 100 m in der Wirklichkeit entspricht. Wie lang ist der Flug? Runde auf ganze Meter.",
    wert_dr, c_dr, "round(100 * sqrt((10 - 3) ** 2 + (8 - 2) ** 2), 0)", "Bestimme zuerst die beiden Koordinatenunterschiede. Rechne erst am Schluss in Meter um.",
    "Unterschiede: 10 − 3 = 7 und 8 − 2 = 6. Abstand im Plan: √(49 + 36) = √85 ≈ 9,22 Einheiten. 9,22 · 100 ≈ 922. Der Flug ist etwa 922 m lang.",
    [(1300, None, "die Unterschiede addiert: (7 + 6) · 100", "(7 + 6) * 100"), (8500, None, "die Wurzel nicht gezogen: 85 · 100", "(7 ** 2 + 6 ** 2) * 100"), (9, None, "die Umrechnung in Meter vergessen", "round(sqrt(7 ** 2 + 6 ** 2), 0)")], "m"), g="einkleidung", regel=R)
assert wert_dr == 922

# ───────── raum ─────────
neu(T, "raum", "lueckenweg", L(
    "Ein Quader hat die Kantenlängen 8 cm, 9 cm und 12 cm. Die Diagonale e der Grundfläche (8 cm mal 9 cm) hat das Quadrat e² = ① cm². Die Raumdiagonale d bildet mit e und der Kante der Höhe 12 cm ein rechtwinkliges Dreieck. Das Quadrat der Raumdiagonale ist d² = ② cm². Die Raumdiagonale ist ③ cm lang.",
    "① = □; ② = □; ③ = □", [145, 289, 17], ["8 ** 2 + 9 ** 2", "{1} + 12 ** 2", "wurzel({2})"], ["64 + 81", "145 + 144", "sqrt(289)"],
    "Rechne zuerst in der Grundfläche, dann im zweiten Dreieck. Die Quadrate darfst du stehen lassen, bis du am Ende die Wurzel ziehst.",
    "e² = 8² + 9² = 64 + 81 = 145. d² = e² + 12² = 145 + 144 = 289. d = √289 = 17 cm.",
    {0: [(17, "fb.rechtwinklig.ohne_quadrate", "die Kanten addiert: 8 + 9", "8 + 9")], 1: [(157, None, "die Höhe nicht quadriert: 145 + 12", "{1} + 12")], 2: [(289, None, "die Wurzel nicht gezogen", "{2}")]}), regel=R)
neu(T, "raum", "umkehren", Z(
    "Ein Quader hat eine quadratische Grundfläche mit der Seitenlänge 4 cm. Seine Raumdiagonale ist 9 cm lang. Wie hoch ist der Quader?",
    7, "wurzel(9 ** 2 - 4 ** 2 - 4 ** 2)", "sqrt(81 - 16 - 16)", "Für die Raumdiagonale d gilt: d² ist die Summe der Quadrate der drei Kanten. Hier ist eine Kante unbekannt.",
    "d² = 4² + 4² + h². 81 = 16 + 16 + h², also h² = 49 und h = 7 cm. Probe: 16 + 16 + 49 = 81 = 9².",
    [(49, None, "das Quadrat der Höhe als Höhe angegeben", "9 ** 2 - 4 ** 2 - 4 ** 2"), (5, None, "9 − 4 gerechnet", "9 - 4"), (8, None, "nur eine Grundkante abgezogen und gerundet", "round(sqrt(9 ** 2 - 4 ** 2), 0)")], "cm"), g="rueckwaerts", regel=R)
neu(T, "raum", "fehler_detektiv", FD(
    "Kim berechnet die Raumdiagonale d eines Würfels mit der Kantenlänge 6 cm.",
    [("Diagonale e einer Seitenfläche: e² = 6² + 6² = 72.", 6 ** 2 + 6 ** 2 == 72, True),
     ("Raumdiagonale: d² = e² + 6² = 72 + 36 = 108.", 72 + 6 ** 2 == 108, 72 + 36 == 108),
     ("Also ist d = 108 : 2 = 54 cm.", 54 ** 2 == 108, 108 / 2 == 54)],
    "Wie wird aus einem Quadrat die Seitenlänge?",
    "Aus d² = 108 folgt d = √108 ≈ 10,4 cm, nicht 108 : 2. Probe: 54² = 2 916, nicht 108. Der Fehler steckt in Zeile 3."), regel=R)

# ───────── anwendung ─────────
neu(T, "anwendung", "lueckenweg", L(
    "Eine 5 m lange Leiter lehnt an einer senkrechten Hauswand. Ihr Fuß steht auf waagerechtem Boden und ist 3 m von der Wand entfernt. Das Quadrat der Leiterlänge ist ① m². Das Quadrat des Wandabstands ist ② m². Das Quadrat der Höhe, in der die Leiter die Wand berührt, ist ③ m². Die Leiter berührt die Wand in einer Höhe von ④ m.",
    "① = □; ② = □; ③ = □; ④ = □", [25, 9, 16, 4], ["5 ** 2", "3 ** 2", "{1} - {2}", "wurzel({3})"], ["25", "9", "25 - 9", "sqrt(16)"],
    "Leiter, Wand und Boden bilden ein rechtwinkliges Dreieck. Die Leiter ist die längste Seite.",
    "Leiter: 5² = 25. Abstand: 3² = 9. Höhe²: 25 − 9 = 16. Höhe: √16 = 4 m.",
    {2: [(34, "fb.rechtwinklig.kathete_als_hypotenuse", "addiert statt subtrahiert: 25 + 9", "{1} + {2}")], 3: [(16, None, "die Wurzel nicht gezogen", "{3}")], 0: [(10, "fb.potenz.basis_mal_hochzahl", "5 · 2 statt 5² gerechnet", "5 * 2")]}), regel=R)
neu(T, "anwendung", "zwei_wege", Z(
    "Ein Boot fährt vom Hafen aus 9 km genau nach Osten und dann 12 km genau nach Norden. Wie weit ist es dann in gerader Linie vom Hafen entfernt? Berechne es auf zwei Wegen. Weg A: Satz des Pythagoras. Weg B: Das Dreieck mit den Seiten 9 km und 12 km ist ein Vielfaches des Dreiecks mit den Seiten 3, 4 und 5. Bestimme den Vervielfältigungsfaktor.",
    15, "wurzel(9 ** 2 + 12 ** 2)", "9 / 3 * 5", "Beide Wege müssen dieselbe Entfernung ergeben. Bei Weg B hilft die Frage: Mit welcher Zahl wurde 3 zu 9?",
    "Weg A: 9² + 12² = 81 + 144 = 225, √225 = 15 km. Weg B: 9 = 3 · 3 und 12 = 3 · 4, der Faktor ist 3. Die Hypotenuse ist 3 · 5 = 15 km.",
    [(21, "fb.rechtwinklig.ohne_quadrate", "die Strecken addiert: 9 + 12", "9 + 12"), (225, None, "die Wurzel nicht gezogen", "9 ** 2 + 12 ** 2"), (5, None, "den Faktor vergessen: die Hypotenuse 5 des kleinen Dreiecks genannt", "5")], "km"), regel=R)
neu(T, "anwendung", "anwenden", Z(
    "Ein Satteldach hat zwei gleich große, rechteckige Dachflächen. Das Haus ist 12 m breit, das Dach ist 9 m lang. Der First liegt 4,5 m höher als die Decke und genau über der Mitte des Hauses. Wie viele Quadratmeter Dachfläche hat das Dach insgesamt? Der Dachüberstand wird nicht berücksichtigt.",
    135, "2 * wurzel(6 ** 2 + 4.5 ** 2) * 9", "2 * sqrt(36 + 20.25) * 9", "Die Schräge einer Dachfläche ist die Hypotenuse eines rechtwinkligen Dreiecks. Eine Kathete ist die halbe Hausbreite.",
    "Halbe Breite: 6 m. Schräge: √(6² + 4,5²) = √(36 + 20,25) = √56,25 = 7,5 m. Eine Dachfläche: 7,5 · 9 = 67,5 m². Zwei Dachflächen: 135 m².",
    [(108, None, "mit der halben Breite 6 m statt der Schräge gerechnet: 2 · 6 · 9", "2 * 6 * 9"), (81, None, "mit der Höhe 4,5 m statt der Schräge gerechnet: 2 · 4,5 · 9", "2 * 4.5 * 9"), (67.5, None, "nur eine Dachfläche berechnet", "7.5 * 9")], "m²"), g="einkleidung", regel=R)
