T = "zahlen.wurzeln_basis"
HZ = "id.zahlen.hoch_zurueck"
HK = "fb.hoch_zurueck.wurzel_halbiert"
OHNE_VERT = "Wurzel und Summe (Wurzel verteilt sich nicht auf Summanden): keine Regel des Katalogs trägt den Lösungsweg"
# ───────── quadratwurzel ─────────
neu(T, "quadratwurzel", "lueckenweg", L(
    "Ein quadratisches Grundstück hat 1296 m² Fläche. Eine Seite ist ① m lang. Der Zaun um das ganze Grundstück ist ② m lang. Aus Zaunstücken zu je 3 m braucht man ③ Stück.",
    "① = □; ② = □; ③ = □", [36, 144, 48], ["36", "4 * {1}", "{2} / 3"], ["round(sqrt(1296))", "4 * round(sqrt(1296))", "4 * round(sqrt(1296)) / 3"],
    "Die Fläche eines Quadrats ist Seite mal Seite. Welche Zahl mit sich selbst malgenommen ergibt 1296?",
    "36 · 36 = 1296, also ist die Seite √1296 = 36 m lang. Der Umfang ist 4 · 36 = 144 m. Mit 3-m-Stücken braucht man 144 : 3 = 48 Stück.",
    {0: [(648, HK, "die Wurzel wie „geteilt durch 2“ gerechnet", "1296 / 2")], 1: [(72, None, "den Umfang mit 2 statt mit 4 Seiten gerechnet", "{1} * 2")], 2: [(432, None, "mit 3 malgenommen statt durch 3 geteilt", "{2} * 3")]}), regel=HZ)
neu(T, "quadratwurzel", "anwenden", Z(
    "Ein quadratischer Sportplatz hat 5929 m² Fläche. Kim läuft eine Runde am Rand entlang. Wie viele Meter ist eine Runde lang?",
    308, "4 * 77", "4 * round(sqrt(5929))", "Zuerst brauchst du die Seitenlänge. Welche Zahl mit sich selbst malgenommen ergibt 5929?",
    "77 · 77 = 5929, also ist eine Seite 77 m lang. Eine Runde ist der Umfang: 4 · 77 = 308 m.",
    [B("77", "nur die Seitenlänge als Rundenlänge genommen"), B("5929 / 4", "die Fläche durch 4 geteilt statt die Wurzel zu ziehen und das Ergebnis als Rundenlänge genommen"), B("5929 / 2 * 4", "die Wurzel wie „geteilt durch 2“ gerechnet (5929 : 2 = 2964,5) und dann mit 4 malgenommen", HK)], einheit="m"), g="einkleidung", regel=HZ)
neu(T, "quadratwurzel", "umkehren", W(
    "Welche Zahl hat die Quadratwurzel 24?",
    "576", [("48", "die Wurzel mit 2 malgenommen statt 24 mit sich selbst"), ("12", "24 durch 2 geteilt statt 24 mit sich selbst malgenommen")],
    "Quadratwurzel und Quadrat gehören zusammen: Rechne von 24 zurück.",
    "Gesucht ist die Zahl, deren Wurzel 24 ist, also das Quadrat von 24: 24 · 24 = 576. Probe: √576 = 24.",
    lambda: 24 * 24 == 576 and 48 * 48 != 576 and 12 * 12 != 576), g="umkehr", regel=HZ)
# ───────── wurzel_dezimal ─────────
neu(T, "wurzel_dezimal", "anwenden", Z(
    "Eine quadratische Fliese hat die Fläche 0,0169 m². Wie lang ist eine Seite in Zentimetern?",
    13, "0.13 * 100", "round(sqrt(0.0169) * 100)", "Die Wurzel aus 0,0169 ist kleiner als 1. Rechne zuerst in Metern und wechsle dann in Zentimeter.",
    "0,13 · 0,13 = 0,0169, also ist die Seite √0,0169 = 0,13 m lang. Das sind 0,13 · 100 = 13 cm.",
    [B("0.13", "die Seite in Metern angegeben, nicht in Zentimetern"), B("1.3", "mit 10 statt mit 100 in Zentimeter umgerechnet"), B("130", "0,13 m in Millimeter statt in Zentimeter umgerechnet")], einheit="cm"), g="einkleidung", regel=HZ)
w_sp, c_sp = rd("sqrt(3.8)", 2)
neu(T, "wurzel_dezimal", "anwenden", Z(
    "Ein quadratisches Solarpanel hat eine Fläche von 3,8 m². Wie lang ist eine Seite? Runde auf zwei Dezimalstellen.",
    w_sp, c_sp, "round(3.8 ** 0.5, 2)", "Suche die Zahl, die mit sich selbst malgenommen 3,8 ergibt. Probiere mit einer Zahl zwischen 1 und 2.",
    "Die Seite ist √3,8 ≈ 1,95 m lang. Probe: 1,95 · 1,95 = 3,8025, das ist fast 3,8.",
    [(1.9, HK, "3,8 durch 2 geteilt statt die Wurzel gezogen", "round(3.8 / 2, 2)"), (0.95, None, "die Fläche durch 4 geteilt, wie beim Umfang", "round(3.8 / 4, 2)"), (3.8, None, "die Fläche als Seitenlänge genommen", "3.8")], einheit="m"), g="einkleidung", regel=HZ)
# ───────── kubikwurzel ─────────
neu(T, "kubikwurzel", "lueckenweg", L(
    "Ein würfelförmiges Aquarium fasst 343 Liter, das sind 343 dm³. Seine Kante ist ① dm lang, die Bodenfläche ② dm². Die Oberfläche aller sechs Seitenflächen ist ③ dm².",
    "① = □; ② = □; ③ = □", [7, 49, 294], ["7", "{1} * {1}", "6 * {2}"], ["round(343 ** (1 / 3))", "round(343 ** (1 / 3)) ** 2", "6 * round(343 ** (1 / 3)) ** 2"],
    "Beim Würfel ist das Volumen Kante mal Kante mal Kante. Welche Zahl dreimal mit sich malgenommen ergibt 343?",
    "7 · 7 · 7 = 343, also ist die Kante ∛343 = 7 dm lang. Die Bodenfläche ist 7 · 7 = 49 dm². Die sechs Seitenflächen: 6 · 49 = 294 dm².",
    {0: [(18, None, "die Quadratwurzel statt der dritten Wurzel gezogen (√343 ≈ 18,52) und auf 18 abgerundet", "floor(sqrt(343))")], 1: [(14, None, "Kante mal 2 gerechnet statt Kante mal Kante", "{1} * 2")], 2: [(196, None, "nur vier Seitenflächen gezählt", "4 * {2}")]}), regel=HZ)
neu(T, "kubikwurzel", "anwenden", Z(
    "Ein würfelförmiger Container hat das Volumen 2744 dm³. Wie groß ist seine gesamte Oberfläche in Quadratdezimetern?",
    1176, "6 * 14 * 14", "6 * round(2744 ** (1 / 3)) ** 2", "Berechne zuerst die Kantenlänge. Wie viele Seitenflächen hat ein Würfel?",
    "14 · 14 · 14 = 2744, also ist die Kante 14 dm lang. Eine Seitenfläche hat 14 · 14 = 196 dm². Die Oberfläche ist 6 · 196 = 1176 dm².",
    [B("6 * 14", "sechs Kanten statt sechs Flächen berechnet"), B("14 * 14", "nur eine Seitenfläche genommen"), BR("2744 / 6", "das Volumen durch 6 geteilt (auf zwei Stellen gerundet)", stellen=2)], einheit="dm²"), g="mehrschritt", regel=HZ)
neu(T, "kubikwurzel", "fehler_detektiv", FD(
    "Alex bestimmt die Kante eines Würfels mit dem Volumen 216 cm³:",
    [("Die Kante ist die dritte Wurzel aus 216, also 216 geteilt durch 3.", False, True),
     ("Das sind 72 cm.", True, True),
     ("Die Grundfläche wäre dann 72 · 72 = 5184 cm².", True, True)],
    "Die dritte Wurzel fragt: Welche Zahl dreimal mit sich selbst malgenommen ergibt 216? Ist 216 geteilt durch 3 so eine Zahl?",
    "Die dritte Wurzel ist keine Division durch 3. Gesucht ist die Zahl, die dreimal mit sich malgenommen 216 ergibt: 6 · 6 · 6 = 216, die Kante ist 6 cm. Zeile 1 ist der erste Fehler, die Zeilen 2 und 3 rechnen mit dem falschen Wert richtig weiter."), g="fehler", regel=HZ)
# ───────── abschaetzen ─────────
neu(T, "abschaetzen", "verfahren_waehlen", W(
    "Ein quadratischer Teppich hat 130 dm² Fläche. Die Länge seiner Seite liegt in dm zwischen welchen zwei ganzen Zahlen?",
    "zwischen 11 dm und 12 dm", [("zwischen 12 dm und 13 dm", "12² = 144 ist schon größer als 130"), ("zwischen 10 dm und 11 dm", "11² = 121 ist kleiner als 130, also liegt die Seite über 11 dm"), ("zwischen 65 dm und 66 dm", "130 durch 2 geteilt, die Wurzel aber nicht halbiert")],
    "Suche die Quadratzahlen links und rechts von 130.",
    "11² = 121 und 12² = 144. Weil 121 < 130 < 144 gilt, liegt √130 zwischen 11 und 12.",
    lambda: 11 ** 2 < 130 < 12 ** 2), g="mehrschritt", regel=HZ)
w_85, c_85 = rd("sqrt(85)", 1)
neu(T, "abschaetzen", "anwenden", Z(
    "Kim will wissen, wie lang die Seite eines quadratischen Zeltbodens mit 85 m² Fläche ungefähr ist. Wie lang ist sie? Runde auf eine Dezimalstelle.",
    w_85, c_85, "round(85 ** 0.5, 1)", "Die Seite liegt zwischen zwei ganzen Zahlen. Probiere dann Zehntel: Welches Zehntel passt am besten?",
    "9² = 81 und 10² = 100, also liegt √85 zwischen 9 und 10. Es gilt 9,2 · 9,2 = 84,64 und 9,3 · 9,3 = 86,49. Näher an 85 liegt 9,2. Die Seite ist etwa 9,2 m lang.",
    [B("85 / 2", "die Wurzel wie „geteilt durch 2“ gerechnet", HK), B("(9 + 10) / 2", "die Mitte der beiden Nachbarzahlen als Wurzel genommen"), B("9.3", "zu weit gerundet: 9,3² ist 86,49 und liegt weiter von 85 weg")], einheit="m"), g="einkleidung", regel=HZ)
# ───────── wurzel_deuten ─────────
neu(T, "wurzel_deuten", "verfahren_waehlen", W(
    "Warum hat √(−25) im Bereich der reellen Zahlen keinen Wert?",
    "Keine reelle Zahl mit sich selbst malgenommen ergibt eine negative Zahl.",
    [("Weil 25 keine Quadratzahl ist.", "25 ist eine Quadratzahl, 5 · 5 = 25"), ("Weil man nur aus geraden Zahlen die Wurzel ziehen kann.", "das hat mit gerade oder ungerade nichts zu tun")],
    "Prüfe: Was kommt heraus, wenn du eine positive oder eine negative Zahl mit sich selbst malnimmst?",
    "Ein Quadrat ist nie negativ: positiv mal positiv ist positiv, negativ mal negativ ist ebenfalls positiv. Also gibt es keine reelle Zahl, deren Quadrat −25 ist.",
    lambda: all(k * k >= 0 for k in range(-20, 21))), g="begruenden", regel=HZ,
    zweifel="Definitionsbereich der Wurzel: hoch_zurueck trägt (Quadrat nie negativ), die Lernkarte nennt sonst keine Regel")
zaehl_def = sum(1 for x in range(-3, 13) if x - 5 >= 0)
neu(T, "wurzel_deuten", "anwenden", Z(
    "Für wie viele ganze Zahlen x von −3 bis 12 (beide Grenzen eingeschlossen) ist der Ausdruck √(x − 5) im Bereich der reellen Zahlen definiert?",
    8, "5 + 3", zaehl_def, "Der Wert unter der Wurzel darf nicht negativ sein. Ab welchem x ist x − 5 mindestens 0?",
    "Es muss x − 5 ≥ 0 gelten, also x ≥ 5. Die Zahlen 5, 6, 7, 8, 9, 10, 11 und 12 erfüllen das. Das sind 8 Zahlen.",
    [B("12 - 5", "die Zahl 5 nicht mitgezählt"), B("12 + 3 + 1", "alle ganzen Zahlen von −3 bis 12 gezählt"), B("12 - 4 + 1", "schon bei x = 4 begonnen")]), g="parameter", regel=HZ,
    zweifel="Definitionsmenge der Wurzel (Radikand ≥ 0); hoch_zurueck trägt nur teilweise")
neu(T, "wurzel_deuten", "fehler_detektiv", FD(
    "Sam berechnet die Wurzel aus der Summe 4 + 25:",
    [("Die Wurzel kann man auf die Summanden verteilen: √(4 + 25) = √4 + √25.", False, True),
     ("Mit √4 = 2 und √25 = 5 folgt für √29 der Wert 7.", True, True),
     ("Dann müsste 29 gleich 7 mal 7 sein.", True, True)],
    "Berechne 7 · 7. Passt das Ergebnis zu 29?",
    "Bei Plus darf man die Wurzel nicht auf die Summanden verteilen. √29 ist etwa 5,4, nicht 7. Zeile 3 zeigt den Widerspruch: 7 · 7 = 49 und nicht 29. Der Fehler steckt in Zeile 1."), g="fehler", ohne=OHNE_VERT)
# ───────── wurzel_sache ─────────
neu(T, "wurzel_sache", "anwenden", Z(
    "Ein quadratisches Stadtviertel in Lissabon hat eine Fläche von 2,25 km². Kim geht einmal am Rand des Viertels herum, mit 5 km/h. Wie viele Minuten braucht sie?",
    72, "4 * 1.5 / 5 * 60", "4 * sqrt(2.25) / 5 * 60", "Rechne zuerst die Seitenlänge aus. Dann den Weg um das Viertel, dann die Zeit.",
    "1,5 · 1,5 = 2,25, also ist die Seite 1,5 km lang. Der Weg ist 4 · 1,5 = 6 km. Bei 5 km/h dauert das 6 : 5 = 1,2 Stunden, das sind 1,2 · 60 = 72 Minuten.",
    [B("4 * 1.5 / 5", "die Zeit in Stunden angegeben, nicht in Minuten"), B("1.5 / 5 * 60", "nur eine Seite gegangen"), B("2.25 / 5 * 60", "die Fläche statt des Wegs durch die Geschwindigkeit geteilt")], einheit="min"), g="einkleidung", regel=HZ)
neu(T, "wurzel_sache", "anwenden", Z(
    "Eine würfelförmige Kiste hat das Volumen 3,375 m³. Kim klebt ein Band an allen zwölf Kanten entlang. Wie viele Meter Band braucht sie?",
    18, "12 * 1.5", "round(12 * 3.375 ** (1 / 3), 6)", "Wie lang ist eine Kante, wenn dreimal Kante malgenommen 3,375 ergibt?",
    "1,5 · 1,5 · 1,5 = 3,375, also ist eine Kante 1,5 m lang. Ein Würfel hat 12 Kanten: 12 · 1,5 = 18 m.",
    [B("6 * 1.5", "nur sechs Kanten beklebt"), B("12 * 3.375 / 3", "die Kante als Volumen durch 3 berechnet"), B("12 * 1.5 * 1.5", "die Kantenlänge quadriert")], einheit="m"), g="mehrschritt", regel=HZ)
