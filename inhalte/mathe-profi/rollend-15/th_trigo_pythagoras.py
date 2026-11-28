T = "trigo.pythagoras"
RW = "id.geometrie.rechtwinklig"
OP = "fb.rechtwinklig.ohne_quadrate"
KH = "fb.rechtwinklig.kathete_als_hypotenuse"
# ───────── hypotenuse ─────────
neu(T, "hypotenuse", "lueckenweg", L(
    "Ein rechtwinkliges Dreieck hat die Katheten 9 cm und 40 cm. Die Summe der Kathetenquadrate ist ①. Die Hypotenuse ist ② cm lang. Der Umfang des Dreiecks ist ③ cm.",
    "① = □; ② = □; ③ = □", [1681, 41, 90], ["81 + 1600", "41", "9 + 40 + {2}"], ["9 ** 2 + 40 ** 2", "round(sqrt(9 ** 2 + 40 ** 2))", "9 + 40 + 41"],
    "Im rechtwinkligen Dreieck gilt: Kathete im Quadrat plus Kathete im Quadrat ist Hypotenuse im Quadrat.",
    "9² = 81 und 40² = 1600, die Summe ist 1681. Weil 41 · 41 = 1681 gilt, ist die Hypotenuse 41 cm lang. Umfang: 9 + 40 + 41 = 90 cm.",
    {0: [(49, OP, "die Längen 9 und 40 addiert statt ihre Quadrate", "9 + 40")], 1: [(840, None, "1681 durch 2 geteilt statt die Wurzel gezogen (840,5) und auf 840 abgerundet", "round({1} / 2)")], 2: [(49, None, "die Hypotenuse im Umfang vergessen", "9 + 40")]}), regel=RW)
neu(T, "hypotenuse", "anwenden", Z(
    "Eine Seilbahn überwindet einen waagerechten Abstand von 1,2 km und einen Höhenunterschied von 0,5 km. Wie lang ist das Seil in Kilometern, wenn man es als gerade Strecke ansieht?",
    1.3, "1.3", "round(sqrt(1.2 ** 2 + 0.5 ** 2), 6)", "Waagerechter Abstand, Höhenunterschied und Seil bilden ein rechtwinkliges Dreieck. Welche Seite ist die längste?",
    "Das Seil ist die Hypotenuse: 1,2² + 0,5² = 1,44 + 0,25 = 1,69. Die Wurzel aus 1,69 ist 1,3, denn 1,3 · 1,3 = 1,69. Das Seil ist 1,3 km lang.",
    [B("1.2 + 0.5", "die Längen addiert statt ihre Quadrate", OP), B("1.2 ** 2 + 0.5 ** 2", "die Wurzel nicht gezogen"), B("1.2 - 0.5", "den Unterschied der Längen genommen")], einheit="km"), g="einkleidung", regel=RW)
# ───────── kathete ─────────
w_k, c_k = rd("sqrt(61 ** 2 + 11 ** 2)", 0)
neu(T, "kathete", "anwenden", Z(
    "Ein 61 m langes Stahlseil spannt von der Spitze eines senkrechten Funkmasts zu einem Punkt am Boden, der 11 m vom Fuß des Masts entfernt ist. Wie hoch ist der Mast in Metern?",
    60, "60", "round(sqrt(61 ** 2 - 11 ** 2))", "Das Seil ist die längste Seite im Dreieck. Welche Seite suchst du, und wie rechnest du dann?",
    "Das Seil ist die Hypotenuse (61 m), der Abstand 11 m eine Kathete, der Mast die andere. h² = 61² − 11² = 3721 − 121 = 3600, also h = 60 m.",
    [(w_k, KH, "das Seil wie eine Kathete behandelt, die Quadrate addiert und die Wurzel (≈ 61,98) auf 62 gerundet", c_k), B("61 - 11", "die Längen ohne Quadrate voneinander abgezogen", OP), B("61 + 11", "die Längen addiert")], einheit="m"), g="mehrschritt", regel=RW)
neu(T, "kathete", "verfahren_waehlen", W(
    "Ein rechtwinkliges Dreieck hat die Hypotenuse c = 17 cm und die Kathete a = 8 cm. Welche Gleichung liefert die zweite Kathete b?",
    "b² = 17² − 8²", [("b² = 17² + 8²", "die Hypotenuse wie eine Kathete behandelt", KH), ("b = 17 − 8", "die Längen ohne Quadrate subtrahiert", OP)],
    "Welche der drei Seiten ist die längste? Sie steht auf der anderen Seite der Gleichung a² + b² = c².",
    "Nach dem Satz des Pythagoras gilt a² + b² = c². Umgestellt: b² = c² − a² = 289 − 64 = 225. Also ist b = 15 cm.",
    lambda: 17 ** 2 - 8 ** 2 == 15 ** 2), g="mehrschritt", regel=RW)
# ───────── umkehrung ─────────
neu(T, "umkehrung", "verfahren_waehlen", W(
    "Welches Dreieck mit den angegebenen Seitenlängen (in cm) ist rechtwinklig?",
    "8, 15, 17", [("7, 24, 26", "49 + 576 = 625 ist nicht 676 = 26²"), ("9, 12, 16", "81 + 144 = 225 ist nicht 256 = 16²")],
    "Quadriere die zwei kürzeren Seiten, addiere und vergleiche mit dem Quadrat der längsten Seite.",
    "8² + 15² = 64 + 225 = 289 = 17². Dann ist das Dreieck nach der Umkehrung des Satzes des Pythagoras rechtwinklig. Bei 7, 24, 26 ist 625 ≠ 676, bei 9, 12, 16 ist 225 ≠ 256.",
    lambda: 8 ** 2 + 15 ** 2 == 17 ** 2 and 7 ** 2 + 24 ** 2 != 26 ** 2 and 9 ** 2 + 12 ** 2 != 16 ** 2), g="pruefung", regel=RW)
neu(T, "umkehrung", "umkehren", Z(
    "Ein Dreieck hat die Seiten 39 cm, 89 cm und x cm, wobei 89 cm die längste Seite ist. Für welche Zahl x ist es rechtwinklig?",
    80, "80", "round(sqrt(89 ** 2 - 39 ** 2))", "Die längste Seite ist die Hypotenuse. Wie lautet die Gleichung, wenn x eine Kathete ist?",
    "x² + 39² = 89², also x² = 7921 − 1521 = 6400. Weil 80 · 80 = 6400 ist, gilt x = 80. Das Dreieck mit 39, 80, 89 ist rechtwinklig.",
    [B("89 - 39", "die Längen ohne Quadrate subtrahiert", OP), B("89 + 39", "die beiden Längen addiert"), B("6400", "die Wurzel nicht gezogen")], einheit="cm"), g="rueckwaerts", regel=RW)
# ───────── koordinaten ─────────
w_ko, c_ko = rd("sqrt(2 ** 2 + 8 ** 2)", 1)
neu(T, "koordinaten", "anwenden", Z(
    "Im Koordinatensystem liegen die Punkte A(−2|3) und B(4|11). Wie lang ist die Strecke [AB]?",
    10, "10", "round(sqrt((4 + 2) ** 2 + (11 - 3) ** 2))", "Zeichne ein rechtwinkliges Dreieck mit [AB] als Hypotenuse. Wie lang sind die beiden Katheten?",
    "Waagerechter Unterschied: 4 − (−2) = 6. Senkrechter Unterschied: 11 − 3 = 8. AB² = 6² + 8² = 36 + 64 = 100, also AB = 10.",
    [B("6 + 8", "die Katheten addiert", OP), (w_ko, None, "das Minus bei −2 übersehen: waagerechter Unterschied 2 statt 6, also √(2² + 8²) ≈ 8,246, auf eine Dezimalstelle 8,2", c_ko), B("6 * 8", "die Katheten malgenommen")], einheit="LE"), g="mehrschritt", regel=RW)
neu(T, "koordinaten", "umkehren", Z(
    "Der Punkt P(x|7) mit x > 0 hat von A(0|1) den Abstand 10. Welchen Wert hat x?",
    8, "8", "round(sqrt(10 ** 2 - (7 - 1) ** 2))", "Zeichne die Strecke [AP] als Hypotenuse. Der senkrechte Unterschied ist eine Kathete, der waagerechte Unterschied x die andere.",
    "Senkrechter Unterschied: 7 − 1 = 6. Es gilt x² + 6² = 10², also x² = 100 − 36 = 64 und x = 8.",
    [B("10 - 6", "die Längen ohne Quadrate subtrahiert", OP), B("100 - 36", "die Wurzel nicht gezogen"), B("10 + 6", "die Längen addiert")]), g="rueckwaerts", regel=RW)
# ───────── raum ─────────
neu(T, "raum", "anwenden", Z(
    "Ein Koffer ist 8 dm lang, 9 dm breit und 12 dm hoch. Wie lang ist der längste gerade Stab, der hineinpasst (Raumdiagonale)?",
    17, "17", "round(sqrt(8 ** 2 + 9 ** 2 + 12 ** 2))", "Rechne zuerst die Diagonale der Grundfläche. Sie ist eine Kathete in einem zweiten rechtwinkligen Dreieck.",
    "Grundfläche (8 und 9): d² = 64 + 81 = 145. Raumdiagonale: D² = 145 + 12² = 145 + 144 = 289. D = 17 dm.",
    [B("8 + 9 + 12", "die drei Kanten addiert", OP), B("8 ** 2 + 9 ** 2 + 12 ** 2", "die Wurzel nicht gezogen"), B("12 + 9", "nur zwei Kanten addiert")], einheit="dm"), g="mehrschritt", regel=RW)
neu(T, "raum", "lueckenweg", L(
    "Ein Quader hat die Kanten 12 cm, 16 cm und 15 cm. Die Diagonale der Grundfläche (12 cm und 16 cm) ist ① cm lang. Die Raumdiagonale ist ② cm lang. Sie ist ③ cm länger als die Diagonale der Grundfläche.",
    "① = □; ② = □; ③ = □", [20, 25, 5], ["20", "25", "{2} - {1}"], ["round(sqrt(12 ** 2 + 16 ** 2))", "round(sqrt(12 ** 2 + 16 ** 2 + 15 ** 2))", "25 - 20"],
    "Die Diagonale der Grundfläche ist eine Kathete in einem zweiten rechtwinkligen Dreieck mit der Höhe 15 cm.",
    "d² = 144 + 256 = 400, also d = 20. D² = 20² + 15² = 400 + 225 = 625, also D = 25. Unterschied: 25 − 20 = 5.",
    {0: [(28, OP, "die Kanten 12 und 16 addiert", "12 + 16")], 1: [(35, OP, "die Diagonale 20 und die Höhe 15 addiert", "{1} + 15")], 2: [(45, None, "die Raumdiagonale und die Diagonale der Grundfläche addiert", "{2} + {1}")]}), regel=RW)
# ───────── anwendung ─────────
neu(T, "anwendung", "anwenden", Z(
    "Ein Zelt hat zwei gleiche rechteckige Dachflächen. Es ist am Boden 4 m breit, der First ist 1,5 m hoch, und die Dachflächen sind 6 m lang. Wie viele Quadratmeter Stoff haben die beiden Dachflächen zusammen?",
    30, "2 * 2.5 * 6", "2 * round(sqrt(2 ** 2 + 1.5 ** 2), 6) * 6", "Die Breite einer Dachfläche ist die Schräge im Querschnitt. Der Querschnitt ist ein gleichschenkliges Dreieck: Zerlege es in zwei rechtwinklige.",
    "Halbe Breite 2 m, Höhe 1,5 m. Schräge: s² = 2² + 1,5² = 4 + 2,25 = 6,25, also s = 2,5 m. Eine Dachfläche: 2,5 · 6 = 15 m². Zwei: 30 m².",
    [B("2 * 2 * 6", "die halbe Breite als Schräge genommen"), B("2 * 3.5 * 6", "halbe Breite und Höhe addiert", OP), B("2.5 * 6", "nur eine Dachfläche gerechnet")], einheit="m²"), g="einkleidung", regel=RW)
neu(T, "anwendung", "fehler_detektiv", FD(
    "Alex berechnet die Höhe eines gleichschenkligen Dreiecks mit der Basis 10 cm und den Schenkeln 13 cm:",
    [("Die Höhe halbiert die Basis, die halbe Basis ist 5 cm lang.", True, True),
     ("Höhe, halbe Basis und Schenkel bilden ein rechtwinkliges Dreieck, der Schenkel ist die Hypotenuse.", True, True),
     ("Daraus folgt h² = 13² + 5², also ist h² größer als 169.", False, True),
     ("Die Höhe ist deshalb etwa 14 cm lang.", True, True)],
    "Welche Seite ist im kleinen rechtwinkligen Dreieck die längste? Wie lautet dann die Gleichung?",
    "Weil der Schenkel die Hypotenuse ist, gilt h² + 5² = 13², also h² = 169 − 25 = 144 und h = 12 cm. In Zeile 3 wurde die Hypotenuse wie eine Kathete addiert. Zeile 4 folgt aus dem falschen Wert."), g="fehler", regel=RW)
