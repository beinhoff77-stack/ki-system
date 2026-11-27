T = "bruch.brueche"
# ───────── bruchteil_von ─────────
neu(T, "bruchteil_von", "lueckenweg", L(
    "Berechne 3/8 von 56 kg. Zuerst teilst du durch den Nenner: Ein Achtel sind ① kg. Dann nimmst du so viele Teile, wie der Zähler sagt: 3/8 sind ② kg.",
    KOMM(2), [7, 21], ["56 / 8", "{1} * 3"], ["7", "21"], "Der Nenner sagt, in wie viele gleiche Teile du das Ganze teilst.",
    "56 kg : 8 = 7 kg ist ein Achtel. Drei Achtel sind 3 · 7 kg = 21 kg.",
    {0: [(448, None, "mit dem Nenner malgenommen statt durch ihn geteilt", "56 * 8")], 1: [(10, None, "den Zähler dazugezählt statt malgenommen", "{1} + 3")]}), regel="rr.bruchrechnen")
neu(T, "bruchteil_von", "umkehren", Z(
    "Von einer 72 m langen Schnur wird ein Stück abgeschnitten. Es ist ?/8 der Schnur und 45 m lang. Welche Zahl steht an der Stelle des Fragezeichens?",
    5, "45 / (72 / 8)", "45 * 8 / 72", "Wie lang ist ein Achtel der ganzen Schnur?",
    "Ein Achtel der Schnur sind 72 m : 8 = 9 m. Das Stück hat 45 m. 45 m : 9 m = 5. Probe: 5/8 von 72 m = 45 m.",
    [(9, None, "nur ein Achtel berechnet und den Zähler vergessen", "72 / 8"), (360, None, "45 mit dem Nenner 8 malgenommen", "45 * 8")]), regel="rr.bruchrechnen")
neu(T, "bruchteil_von", "anwenden", Z(
    "Ein Wanderweg ist 24 km lang. Am ersten Tag geht die Gruppe 3/8 des ganzen Weges, am zweiten Tag 1/4 des ganzen Weges. Wie viele Kilometer bleiben für den dritten Tag?",
    9, "24 * (1 - 3/8 - 1/4)", "24 - 9 - 6", "Rechne beide Tagesstrecken aus. Was bleibt vom ganzen Weg übrig?",
    "Erster Tag: 24 km : 8 · 3 = 9 km. Zweiter Tag: 24 km : 4 = 6 km. Rest: 24 km − 9 km − 6 km = 9 km.",
    [(15, None, "die schon gegangene Strecke statt des Rests angegeben", "24 * (3/8 + 1/4)"), (3.75, None, "1/4 vom Rest (15 km) statt vom ganzen Weg genommen", "(24 - 24 * 3/8) / 4")], "km"), g="transfer", regel="rr.bruchrechnen")

# ───────── anteil_bestimmen ─────────
neu(T, "anteil_bestimmen", "lueckenweg", L(
    "In einer Gruppe sind 36 Kinder, 15 davon spielen Fußball. Der Anteil ist 15/36. Kürze mit dem größten gemeinsamen Teiler ①. Der gekürzte Anteil ist dann ②/③.",
    KOMM(3), [3, 5, 12], ["3", "15 / {1}", "36 / {1}"], ["3", "5", "12"], "Suche die größte Zahl, die in 15 und in 36 steckt.",
    "Der größte gemeinsame Teiler von 15 und 36 ist 3. 15 : 3 = 5 und 36 : 3 = 12. Der Anteil ist 5/12.",
    {0: [(1, None, "nur mit 1 gekürzt: das verändert den Bruch nicht, 1 ist nicht der größte gemeinsame Teiler", False)],
     1: [(12, None, "den Nenner statt des Zählers durch den Teiler geteilt", "36 / {1}")], 2: [(5, None, "den Zähler noch einmal durch den Teiler geteilt", "15 / {1}")]}), regel="rr.kuerzen")
neu(T, "anteil_bestimmen", "zwei_wege", L(
    "In einer Klasse sind 28 Kinder, 21 davon kommen mit dem Rad. Weg A: Kürze 21/28 direkt. Weg B: Die 7 Kinder ohne Rad sind ein gekürzter Anteil; ziehe ihn von 1 ab. Beide Wege müssen denselben vollständig gekürzten Anteil ergeben.",
    "□/□", [3, 4], ["21 / 7", "28 / 7"], ["3", "4"], "Prüfe, ob beide Wege am Ende dasselbe ergeben.",
    "Weg A: 21/28 = 3/4 (durch 7 gekürzt). Weg B: 7/28 = 1/4, dann 1 − 1/4 = 3/4. Beide Wege führen zu 3/4.",
    {0: [(1, None, "nur den Anteil der Kinder ohne Rad gekürzt (7/28 = 1/4) und dessen Zähler angegeben", "7 / 7")]},
    hinweis="Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt."), regel="rr.kuerzen")
neu(T, "anteil_bestimmen", "fehler_detektiv", FD(
    "Mia bestimmt, welcher Anteil der 45 Schüler in der AG ist. 18 Schüler sind in der AG.",
    [("Anteil = Ganzes : Teil = 45/18", F(45, 18) == F(18, 45)), ("45/18 = 5/2 (durch 9 gekürzt)", F(45, 18) == F(5, 2)), ("45/18 = 2 1/2", 2 + F(1, 2) == F(5, 2))],
    "Was kommt in den Zähler, was in den Nenner?", "Der Teil (18) kommt in den Zähler, das Ganze (45) in den Nenner: 18/45 = 2/5. Zeile 1 hat Teil und Ganzes vertauscht; die späteren Zeilen rechnen damit richtig weiter."), regel="rr.kuerzen")

# ───────── ganzes_bestimmen ─────────
neu(T, "ganzes_bestimmen", "lueckenweg", L(
    "3/5 einer Strecke sind 27 km lang. Zuerst bestimmst du, wie lang ein Fünftel ist: ① km. Dann bekommst du die ganze Strecke: ② km.",
    KOMM(2), [9, 45], ["27 / 3", "{1} * 5"], ["9", "45"], "Teile zuerst durch den Zähler, um ein Teil zu erhalten.",
    "27 km : 3 = 9 km ist ein Fünftel. Das Ganze sind 5 Fünftel: 5 · 9 km = 45 km.",
    {0: [(81, None, "den Zähler mit 27 malgenommen statt geteilt", "27 * 3")], 1: [(27, None, "mit dem Zähler statt dem Nenner malgenommen", "{1} * 3")]}), regel="rr.bruchrechnen")
neu(T, "ganzes_bestimmen", "anwenden", Z(
    "Ein Händler verkauft am Montag 2/5 seiner Äpfel. Das sind 18 kg. Wie viele Kilogramm Äpfel hatte er vorher?",
    45, "18 / 2 * 5", "18 * 5 / 2", "Wie viel kg sind ein Fünftel?",
    "18 kg : 2 = 9 kg ist ein Fünftel. Alle 5 Fünftel: 5 · 9 kg = 45 kg.",
    [(7.2, None, "mit dem Zähler malgenommen und durch den Nenner geteilt, als wären 18 kg das Ganze", "18 * 2 / 5"), (90, None, "18 mit dem Nenner 5 malgenommen", "18 * 5")], "kg"), regel="rr.bruchrechnen")
neu(T, "ganzes_bestimmen", "umkehren", Z(
    "Ein Behälter ist zu 3/8 gefüllt. Man gießt 12 l hinzu. Jetzt ist er zu 3/4 gefüllt. Wie viele Liter passen in den ganzen Behälter?",
    32, "12 / (3/4 - 3/8)", "12 * 8 / 3", "Welcher Bruchteil des Behälters sind die 12 l?",
    "Hinzugekommen sind 3/4 − 3/8 = 3/8 des Behälters. 3/8 sind 12 l, also 1/8 = 4 l und 8/8 = 32 l.",
    [(16, None, "12 l als 3/4 des Behälters angesehen", "12 / (3/4)"), (96, None, "12 l mit dem Nenner 8 malgenommen", "12 * 8")], "l"), g="rueckwaerts", regel="rr.bruchrechnen")

# ───────── erweitern ─────────
neu(T, "erweitern", "lueckenweg", L(
    "Erweitere 5/6 auf den Nenner 42. Wie oft passt der alte Nenner in den neuen? Die Erweiterungszahl ist ①. Der neue Zähler ist ②.",
    KOMM(2), [7, 35], ["42 / 6", "5 * {1}"], ["7", "35"], "Mit welcher Zahl wird aus dem Nenner 6 der Nenner 42?",
    "42 : 6 = 7. Zähler und Nenner werden mit 7 malgenommen: 5 · 7 = 35. Also 5/6 = 35/42.",
    {0: [(36, None, "42 − 6 gerechnet statt zu teilen", "42 - 6")], 1: [(12, None, "die Erweiterungszahl zum Zähler addiert statt malgenommen", "5 + {1}")]}), regel="rr.kuerzen")
neu(T, "erweitern", "umkehren", Z(
    "Der Bruch 7/9 wurde erweitert. Es entstand 63/81. Mit welcher Zahl wurde erweitert?",
    9, "63 / 7", "81 / 9", "Wie oft passt der alte Zähler in den neuen?",
    "63 : 7 = 9 und 81 : 9 = 9. Es wurde mit 9 erweitert.",
    [(7, None, "63 durch den alten Nenner 9 geteilt", "63 / 9"), (18, None, "81 − 63 gerechnet", "81 - 63")]), regel="rr.kuerzen")
neu(T, "erweitern", "anwenden", Z(
    "Eine Pizza ist in 8 gleiche Stücke geschnitten. Tim isst 3 Stücke. Eine zweite, gleich große Pizza ist in 24 gleiche Stücke geschnitten. Wie viele von diesen kleinen Stücken muss Ben essen, um genauso viel Pizza zu essen wie Tim?",
    9, "3 * (24 / 8)", "24 * 3 / 8", "Wie viele kleine Stücke ergeben ein großes Stück?",
    "Ein großes Stück sind 24 : 8 = 3 kleine. Tim isst 3 große Stücke, das sind 3 · 3 = 9 kleine. 3/8 = 9/24.",
    [(3, None, "dieselbe Stückzahl wie Tim angegeben", "3"), (19, None, "den Unterschied der Stückzahlen (24 − 8 = 16) zu 3 addiert", "3 + 24 - 8")]), g="transfer", regel="rr.kuerzen")

# ───────── ggt ─────────
teiler = lambda n: [d for d in range(1, n + 1) if n % d == 0]
gem = [d for d in teiler(36) if d in teiler(60)]
neu(T, "ggt", "lueckenweg", L(
    "Bestimme den ggT von 48 und 180 mit dem Teilen mit Rest. 180 geteilt durch 48 lässt den Rest ①. Dann teilst du 48 durch ①; der Rest ist ②. Dieser Rest teilt ① ohne Rest und ist der ggT. Kürzt du 48/180 damit, ist der neue Nenner ③.",
    KOMM(3), [36, 12, 15], ["180 % 48", "48 % {1}", "180 / {2}"], ["180 - 3 * 48", "48 - 36", "gcd(48, 180) * 15 / 12"],
    "Teile mit Rest: Welcher Rest bleibt, wenn du die größere Zahl durch die kleinere teilst?",
    "180 : 48 = 3 Rest 36. 48 : 36 = 1 Rest 12. 36 : 12 geht ohne Rest, also ist der ggT 12. 180 : 12 = 15, der neue Nenner ist 15 (48/180 = 4/15).",
    {0: [(132, None, "nur einmal abgezogen: 180 − 48", "180 - 48")], 1: [(1, None, "gedacht, 48 und der erste Rest hätten keinen gemeinsamen Teiler", False)],
     2: [(5, None, "mit dem ersten Rest 36 statt mit dem ggT gekürzt", "180 / {1}")]}), regel="id.zahlen.bausteine")
neu(T, "ggt", "anwenden", Z(
    "Eine Fläche von 24 cm mal 36 cm soll ohne Lücken mit gleich großen Quadraten ausgelegt werden. Die Quadrate sollen so groß wie möglich sein. Wie lang ist die Seite eines Quadrats in Zentimetern?",
    12, "2 * 2 * 3", "gcd(24, 36)", "Die Seitenlänge muss in 24 und in 36 ohne Rest passen.",
    "Gesucht ist der größte gemeinsame Teiler von 24 und 36. 24 = 2 · 2 · 2 · 3 und 36 = 2 · 2 · 3 · 3. Gemeinsam: 2 · 2 · 3 = 12. Das Quadrat hat 12 cm Seitenlänge.",
    [(72, None, "das kleinste gemeinsame Vielfache statt des größten gemeinsamen Teilers", "2 * 2 * 2 * 3 * 3"), (6, None, "nur einen gemeinsamen Teiler genommen, nicht den größten", "24 / 4")], "cm"), regel="id.zahlen.bausteine")
neu(T, "ggt", "fehler_detektiv", FD(
    "Jan bestimmt den größten gemeinsamen Teiler von 36 und 60.",
    [("Teiler von 36: 1, 2, 3, 4, 6, 9, 12, 18, 36", teiler(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]),
     ("Teiler von 60: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60", teiler(60) == [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]),
     ("Gemeinsame Teiler: 1, 2, 3, 4, 6, 12", gem == [1, 2, 3, 4, 6, 12]),
     ("Der ggT ist der kleinste gemeinsame Teiler, also 1", max(gem) == 1)],
    "Was heißt „größter“ gemeinsamer Teiler?", "Die Zeilen 1 bis 3 stimmen. In Zeile 4 wurde der kleinste statt der größte gemeinsame Teiler genommen: richtig ist 12."), regel="id.zahlen.bausteine")

# ───────── kuerzen ─────────
neu(T, "kuerzen", "lueckenweg", L(
    "Kürze 84/126 vollständig. Zuerst durch 6: ①/②. Dann durch 7: ③/3.",
    KOMM(3), [14, 21, 2], ["84 / 6", "126 / 6", "{1} / 7"], ["14", "21", "2"], "Teile Zähler und Nenner durch dieselbe Zahl.",
    "84 : 6 = 14 und 126 : 6 = 21. Dann durch 7: 14 : 7 = 2 und 21 : 7 = 3. Also 84/126 = 2/3.",
    {0: [(78, None, "6 abgezogen statt geteilt", "84 - 6")], 1: [(120, None, "6 abgezogen statt geteilt", "126 - 6")], 2: [(7, None, "durch 2 statt durch 7 geteilt", "{1} / 2")]}), regel="rr.kuerzen")
neu(T, "kuerzen", "bruecke", L(
    "Ein Rabatt von 35 % soll als vollständig gekürzter Bruch geschrieben werden. 35 % bedeutet 35/100. Schreibe den Bruch gekürzt.",
    "□/□", [7, 20], ["35 / 5", "100 / 5"], ["7", "20"], "Prozent heißt „von hundert“. Kürze dann mit dem ggT von 35 und 100.",
    "35 % = 35/100. Der ggT von 35 und 100 ist 5. 35 : 5 = 7 und 100 : 5 = 20. Also 35 % = 7/20.",
    {0: [(35, None, "nicht gekürzt: Zähler 35 stehen gelassen", "35 / 1")], 1: [(100, None, "nicht gekürzt: Nenner 100 stehen gelassen", "100 / 1")]},
    hinweis="Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt."), regel="rr.kuerzen")
neu(T, "kuerzen", "umkehren", Z(
    "Ein Bruch mit dem Nenner 45 wurde vollständig auf 4/9 gekürzt. Welchen Zähler hatte er vorher?",
    20, "4 * 45 / 9", "4 * 5", "Mit welcher Zahl wurde gekürzt? Vergleiche die Nenner.",
    "Der Nenner wurde von 45 auf 9 gekürzt, also durch 5. Der Zähler war 4 · 5 = 20. Probe: 20/45 = 4/9.",
    [(5, None, "nur den Kürzungsfaktor 45 : 9 angegeben", "45 / 9"), (180, None, "4 mit dem Nenner 45 malgenommen", "4 * 45")]), g="rueckwaerts", regel="rr.kuerzen")

# ───────── verhaeltnis_kuerzen ─────────
neu(T, "verhaeltnis_kuerzen", "lueckenweg", L(
    "Kürze das Verhältnis 72 : 120 vollständig. Teile beide Zahlen durch 12: ① : ②. Teile dann durch 2: ③ : 5.",
    KOMM(3), [6, 10, 3], ["72 / 12", "120 / 12", "{1} / 2"], ["6", "10", "3"], "Du teilst beide Zahlen des Verhältnisses durch dieselbe Zahl.",
    "72 : 12 = 6 und 120 : 12 = 10. Dann durch 2: 3 : 5. Das Verhältnis ist 3 : 5.",
    {0: [(60, None, "12 abgezogen statt geteilt", "72 - 12")], 1: [(108, None, "12 abgezogen statt geteilt", "120 - 12")], 2: [(4, None, "2 abgezogen statt geteilt", "{1} - 2")]}), regel="id.verhaeltnisse.groesse")
neu(T, "verhaeltnis_kuerzen", "anwenden", Z(
    "Ein Müsli besteht aus 450 g Haferflocken und 270 g Nüssen. Das Verhältnis Haferflocken : Nüsse wird vollständig gekürzt und als a : b geschrieben. Wie groß ist a + b?",
    8, "450 / 90 + 270 / 90", "5 + 3", "Kürze mit dem ggT von 450 und 270.",
    "Der ggT von 450 und 270 ist 90. 450 : 90 = 5 und 270 : 90 = 3. Das Verhältnis ist 5 : 3, also a + b = 8.",
    [(720, None, "die Gramm-Zahlen addiert, ohne zu kürzen", "450 + 270"), (16, None, "nur durch 45 gekürzt (10 : 6), nicht vollständig", "450 / 45 + 270 / 45")]), regel="id.verhaeltnisse.groesse")
neu(T, "verhaeltnis_kuerzen", "fehler_detektiv", FD(
    "Kim kürzt das Verhältnis 56 : 98 : 70.",
    [("Der ggT von 56, 98 und 70 ist 14.", math.gcd(math.gcd(56, 98), 70) == 14),
     ("56 : 14 = 4, 98 : 14 = 6, 70 : 14 = 5", (56 // 14, 98 // 14, 70 // 14) == (4, 6, 5)),
     ("Das gekürzte Verhältnis ist 4 : 6 : 5.", (4, 6, 5) == (4, 6, 5))],
    "Rechne jede Teilung nach.", "98 : 14 = 7, nicht 6. Richtig ist 4 : 7 : 5. Zeile 3 übernimmt nur das Ergebnis aus Zeile 2."), regel="id.verhaeltnisse.groesse")

# ───────── gleichwertig ─────────
neu(T, "gleichwertig", "lueckenweg", L(
    "Das Verhältnis 24 : ? soll gleichwertig zu 6 : 8 sein. Die Erweiterungszahl ist ①. Die gesuchte Zahl ist ②.",
    KOMM(2), [4, 32], ["24 / 6", "8 * {1}"], ["4", "32"], "Mit welcher Zahl wird aus der 6 die 24?",
    "24 : 6 = 4. Beide Zahlen werden mit 4 malgenommen: 8 · 4 = 32. 24 : 32 ist gleichwertig zu 6 : 8.",
    {0: [(18, None, "24 − 6 gerechnet statt zu teilen", "24 - 6")], 1: [(12, None, "8 + 4 gerechnet statt 8 · 4", "8 + {1}")]}), regel="id.verhaeltnisse.groesse")
neu(T, "gleichwertig", "bruecke", L(
    "Wasser und Sirup werden im Verhältnis 5 : 3 gemischt. Welcher Bruchteil der Mischung ist Sirup? Schreibe ihn als Bruch.",
    "□/□", [3, 8], ["3", "5 + 3"], ["3", "8"], "Wie viele gleiche Teile hat die ganze Mischung?",
    "5 Teile Wasser und 3 Teile Sirup sind zusammen 8 Teile. Sirup ist 3/8 der Mischung.",
    {0: [(5, None, "den Wasseranteil als Zähler genommen", "5")], 1: [(5, None, "den anderen Teil statt des Ganzen als Nenner genommen", "5")]},
    hinweis="Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt."), regel="id.verhaeltnisse.groesse")
neu(T, "gleichwertig", "anwenden", Z(
    "Auf einer Karte entsprechen 3 cm in Wirklichkeit 12 km. Zwei Orte sind auf der Karte 8,5 cm voneinander entfernt. Wie weit sind sie in Wirklichkeit voneinander entfernt, in Kilometern?",
    34, "8.5 * 12 / 3", "8.5 * 4", "Wie viele Kilometer entsprechen 1 cm auf der Karte?",
    "3 cm : 12 km ist gleichwertig zu 1 cm : 4 km. 8,5 cm entsprechen 8,5 · 4 km = 34 km.",
    [(25.5, None, "8,5 mit 3 malgenommen", "8.5 * 3"), (2.125, None, "8,5 · 3 : 12 gerechnet, falsche Richtung", "8.5 * 3 / 12")], "km"), g="transfer", regel="id.verhaeltnisse.groesse")

# ───────── gemischte_zahlen ─────────
neu(T, "gemischte_zahlen", "lueckenweg", L(
    "Schreibe 47/6 als gemischte Zahl. Die 6 passt ganz ① Mal in 47. Der Rest ist ②. Also ist 47/6 = ① ②/6.",
    KOMM(2), [7, 5], ["47 // 6", "47 - 6 * {1}"], ["7", "5"], "Wie oft passt der Nenner ganz in den Zähler?",
    "47 : 6 = 7 Rest 5. Die gemischte Zahl ist 7 5/6.",
    {0: [(8, None, "aufgerundet statt abgerundet", "47 // 6 + 1")], 1: [(11, None, "den Rest mit nur 6 Ganzen berechnet: 47 − 6 · 6", "47 - 6 * 6")]}), regel="id.zahlen.schreibweisen")
neu(T, "gemischte_zahlen", "anwenden", Z(
    "Ein Brett ist 2 3/4 m lang. Daraus werden Stücke von je 1/4 m Länge gesägt. Wie viele Stücke ergibt das?",
    11, "(2 + 3/4) / (1/4)", "2 * 4 + 3", "Wie viele Viertelmeter sind ein ganzer Meter?",
    "Ein Meter hat 4 Viertel. 2 m sind 8 Viertel, dazu 3 Viertel: 8 + 3 = 11 Stücke.",
    [(8, None, "nur die 2 ganzen Meter in Viertel umgerechnet", "2 * 4"), (12, None, "Zähler mal Nenner gerechnet", "3 * 4")]), regel="id.zahlen.schreibweisen")
neu(T, "gemischte_zahlen", "fehler_detektiv", FD(
    "Tina rechnet 2 1/3 + 1 5/6.",
    [("2 1/3 + 1 5/6 = 2 2/6 + 1 5/6", 2 + F(1, 3) + 1 + F(5, 6) == (2 + F(2, 6)) + (1 + F(5, 6))),
     ("= 3 7/6", (2 + F(2, 6)) + (1 + F(5, 6)) == 3 + F(7, 6)),
     ("= 3 1/6", 3 + F(7, 6) == 3 + F(1, 6))],
    "Was passiert, wenn der Bruchteil größer als ein Ganzes ist?", "7/6 = 1 1/6. Man muss das Ganze zu den 3 dazuzählen: 3 + 1 1/6 = 4 1/6. In Zeile 3 ging das Ganze verloren."), regel="id.zahlen.schreibweisen")

# ───────── kgv ─────────
neu(T, "kgv", "lueckenweg", L(
    "Bestimme den Hauptnenner von 5/6 und 3/8. Das kleinste gemeinsame Vielfache von 6 und 8 ist ①. Erweiterst du 5/6 darauf, ist der neue Zähler ②. Erweiterst du 3/8 darauf, ist der neue Zähler ③.",
    KOMM(3), [24, 20, 9], ["24", "5 * {1} / 6", "3 * {1} / 8"], ["lcm(6, 8)", "20", "9"], "Schreibe die Vielfachen von 8 auf, bis eines auch in der 6er-Reihe steht.",
    "Vielfache von 8: 8, 16, 24. 24 steht auch in der 6er-Reihe. 5/6 = 20/24 (mit 4 erweitert) und 3/8 = 9/24 (mit 3 erweitert).",
    {0: [(48, None, "die beiden Nenner malgenommen, das ist nicht das kleinste gemeinsame Vielfache", "6 * 8")],
     1: [(5, None, "den Zähler beim Erweitern nicht mit verändert", "5")], 2: [(3, None, "den Zähler beim Erweitern nicht mit verändert", "3")]}), regel="id.zahlen.bausteine")
neu(T, "kgv", "anwenden", Z(
    "Zwei Busse starten um 8:00 Uhr gemeinsam an der Haltestelle. Der eine Bus fährt alle 12 Minuten ab, der andere alle 18 Minuten. Nach wie vielen Minuten fahren beide zum ersten Mal wieder gleichzeitig ab?",
    36, "2 * 2 * 3 * 3", "lcm(12, 18)", "Gesucht ist eine Zahl, die in der 12er- und der 18er-Reihe vorkommt.",
    "Vielfache von 18: 18, 36. 36 ist auch ein Vielfaches von 12 (3 · 12). Nach 36 Minuten fahren beide wieder gleichzeitig ab.",
    [(6, None, "den ggT statt des kgV genommen", "2 * 3"), (216, None, "die beiden Zahlen malgenommen", "12 * 18")], "min"), regel="id.zahlen.bausteine")
neu(T, "kgv", "fehler_detektiv", FD(
    "Ben bringt 4/15 und 3/10 auf einen gemeinsamen Nenner.",
    [("Vielfache von 15: 15, 30, 45", [15 * k for k in range(1, 4)] == [15, 30, 45]),
     ("Vielfache von 10: 10, 20, 30", [10 * k for k in range(1, 4)] == [10, 20, 30]),
     ("Der Hauptnenner ist 15 · 10 = 150", 15 * 10 == math.lcm(15, 10)),
     ("4/15 = 40/150 und 3/10 = 45/150", F(4, 15) == F(40, 150) and F(3, 10) == F(45, 150))],
    "In welchen beiden Reihen taucht die erste gemeinsame Zahl auf?", "Das kleinste gemeinsame Vielfache steht schon in Zeile 1 und 2: 30. 150 ist zwar ein gemeinsames Vielfaches, aber nicht das kleinste. Zeile 4 rechnet mit 150 richtig weiter."), regel="id.zahlen.bausteine")

# ───────── vergleichen ─────────
neu(T, "vergleichen", "lueckenweg", L(
    "Vergleiche 5/6 und 7/9. Der Hauptnenner ist ①. Dann ist 5/6 = ②/① und 7/9 = ③/①. Der Bruch mit dem größeren Zähler ist der größere.",
    KOMM(3), [18, 15, 14], ["18", "5 * {1} / 6", "7 * {1} / 9"], ["lcm(6, 9)", "15", "14"], "Suche das kleinste gemeinsame Vielfache von 6 und 9.",
    "Hauptnenner 18. 5/6 = 15/18 und 7/9 = 14/18. 15 ist größer als 14, also ist 5/6 größer als 7/9.",
    {0: [(54, None, "die Nenner malgenommen", "6 * 9")], 1: [(10, None, "mit dem Nenner 9 statt 6 erweitert", "5 * {1} / 9")], 2: [(21, None, "mit dem Nenner 6 statt 9 erweitert", "7 * {1} / 6")]}), regel="rr.bruchrechnen")
neu(T, "vergleichen", "zwei_wege", Z(
    "Vergleiche 11/12 und 13/14. Weg A: Erweitere beide Brüche auf den Nenner 84. Weg B: Prüfe, wie viel jedem Bruch bis zum Ganzen fehlt (1/12 und 1/14). Um wie viele Vierundachtzigstel ist der größere Bruch größer als der kleinere?",
    1, "13 * 6 - 11 * 7", "(1/12 - 1/14) * 84", "Wie viele 84stel sind ein Zwölftel, wie viele ein Vierzehntel?",
    "Weg A: 11/12 = 77/84 und 13/14 = 78/84. Unterschied: 1/84. Weg B: Es fehlen 7/84 und 6/84; 13/14 fehlt weniger, ist also um 1/84 größer.",
    [(6, None, "nur ein Vierzehntel in 84stel umgerechnet", "84 / 14"), (7, None, "nur ein Zwölftel in 84stel umgerechnet", "84 / 12")]), regel="rr.bruchrechnen")
neu(T, "vergleichen", "anwenden", Z(
    "Alex und Bea hatten beide 48 € Taschengeld. Alex gibt 3/8 davon für Eis aus, Bea gibt 5/12 davon aus. Wie viel Euro hat Bea mehr ausgegeben als Alex?",
    2, "48 * 5/12 - 48 * 3/8", "20 - 18", "Rechne beide Beträge aus und vergleiche sie.",
    "Alex: 48 € : 8 · 3 = 18 €. Bea: 48 € : 12 · 5 = 20 €. Unterschied: 20 € − 18 € = 2 €.",
    [(20, None, "nur Beas Betrag angegeben", "48 * 5/12"), (18, None, "nur Alex' Betrag angegeben", "48 * 3/8")], "€"), g="transfer", regel="rr.bruchrechnen")

# ───────── zahlenstrahl ─────────
neu(T, "zahlenstrahl", "lueckenweg", L(
    "Die Strecke von 0 bis 1 ist in 15 gleiche Abschnitte geteilt. Der Punkt P liegt nach 10 Abschnitten, also bei 10/15. Der ggT von 10 und 15 ist ①. Gekürzt liegt P bei ②/③.",
    KOMM(3), [5, 2, 3], ["5", "10 / {1}", "15 / {1}"], ["gcd(10, 15)", "2", "3"], "Welche größte Zahl steckt in 10 und in 15?",
    "Der ggT von 10 und 15 ist 5. 10 : 5 = 2 und 15 : 5 = 3. P liegt bei 2/3.",
    {0: [(1, None, "nur durch 1 gekürzt: das ist ein gemeinsamer Teiler, aber nicht der größte", False)],
     1: [(10, None, "den Zähler nicht gekürzt", "10 / 1")], 2: [(15, None, "den Nenner nicht gekürzt", "15 / 1")]}), regel="id.zahlen.zahlengerade")
neu(T, "zahlenstrahl", "bruecke", Z(
    "Ein Zahlenstrahl geht von 0 bis 2. Er ist in 16 gleich lange Abschnitte geteilt. Der Punkt P liegt nach 6 Abschnitten. Welche Dezimalzahl gehört zu P?",
    0.75, "2 * 6 / 16", "6 * 0.125", "Wie lang ist ein Abschnitt?",
    "Ein Abschnitt ist 2 : 16 = 0,125 lang. Sechs Abschnitte sind 6 · 0,125 = 0,75.",
    [(0.375, None, "die Strecke als 1 statt 2 gerechnet: 6 von 16 Teilen", "6 / 16"), (12, None, "6 · 2 gerechnet", "6 * 2")]), regel="id.zahlen.zahlengerade")
neu(T, "zahlenstrahl", "umkehren", L(
    "Auf dem Zahlenstrahl liegt B bei 5/6. Der Punkt M bei 1/2 ist die Mitte der Strecke von A bis B. Wo liegt A? Schreibe A als Bruch.",
    "□/□", [1, 6], ["(2 * (1/2) - 5/6) * 6", "6"], ["1", "6"], "Von A bis M ist der Weg genauso lang wie von M bis B.",
    "Von M bis B sind es 5/6 − 1/2 = 1/3. A liegt genauso weit links von M: 1/2 − 1/3 = 1/6.",
    {0: [(-1, None, "1/2 − 5/6 gerechnet, das ergibt −1/3", "(1/2 - 5/6) * 3")], 1: [(3, None, "den Nenner von −1/3 übernommen", "3")]},
    hinweis="Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt."), g="rueckwaerts", regel="id.zahlen.zahlengerade")

# ───────── zahlbereiche ─────────
neu(T, "zahlbereiche", "lueckenweg", L(
    "Zähle die ganzen Zahlen, die größer als −6 und kleiner als 3 sind. Negative Zahlen: ①. Positive Zahlen: ②. Dazu kommt noch die Null. Insgesamt sind es ③ ganze Zahlen.",
    KOMM(3), [5, 2, 8], ["6 - 1", "3 - 1", "{1} + {2} + 1"], ["5", "2", "8"], "Die Grenzen selbst gehören nicht dazu.",
    "Negativ: −5, −4, −3, −2, −1 (5 Zahlen). Positiv: 1, 2 (2 Zahlen). Dazu die 0: 5 + 2 + 1 = 8.",
    {0: [(6, None, "die Grenze −6 mitgezählt", "6")], 1: [(3, None, "die Grenze 3 mitgezählt", "3")], 2: [(7, None, "die Null vergessen", "{1} + {2}")]},
    hinweis="Je Lücke eine ganze Zahl."), regel="id.zahlen.zahlengerade")
neu(T, "zahlbereiche", "bruecke", Z(
    "Die ganze Zahl −3 soll als Bruch mit dem Nenner 4 geschrieben werden: −3 = ?/4. Welche Zahl steht im Zähler?",
    -12, "-3 * 4", "-12", "Du kannst −3 als −3/1 schreiben und dann erweitern.",
    "−3 = −3/1. Erweitern mit 4 ergibt −12/4. Der Zähler ist −12.",
    [(12, None, "das Vorzeichen vergessen", "3 * 4"), (-7, None, "4 abgezogen statt erweitert", "-3 - 4"), (-0.75, None, "−3 durch 4 geteilt", "-3 / 4")]), regel="id.zahlen.schreibweisen")
neu(T, "zahlbereiche", "anwenden", Z(
    "Die Temperatur liegt bei −3 1/2 °C und sinkt dann um 2 3/4 Grad. Wie viel °C sind es danach?",
    -6.25, "-(3 + 1/2) - (2 + 3/4)", "-3.5 - 2.75", "Beim Sinken wird die Temperatur kleiner.",
    "−3,5 − 2,75 = −6,25. Die Temperatur beträgt −6,25 °C.",
    [(-0.75, None, "−3,5 + 2,75 gerechnet, als wäre es gestiegen", "-3.5 + 2.75"), (6.25, None, "das Minuszeichen vergessen", "3.5 + 2.75")], "°C"), g="transfer", regel="id.zahlen.zahlengerade")

# ───────── verstehen ─────────
neu(T, "verstehen", "lueckenweg", L(
    "Der Bruch 3/5 wird erweitert, bis er den Nenner 40 hat. Die Erweiterungszahl ist ①. Der neue Zähler ist ②. Bis zum Ganzen fehlen dem Bruch dann ③ Vierzigstel.",
    KOMM(3), [8, 24, 16], ["40 / 5", "3 * {1}", "40 - {2}"], ["8", "24", "16"], "Mit welcher Zahl wird aus 5 die 40?",
    "40 : 5 = 8. 3 · 8 = 24, also 3/5 = 24/40. Das Ganze sind 40/40, es fehlen 40 − 24 = 16 Vierzigstel.",
    {0: [(35, None, "40 − 5 gerechnet statt zu teilen", "40 - 5")], 1: [(11, None, "die Erweiterungszahl addiert statt malgenommen", "3 + {1}")],
     2: [(24, None, "den Zähler selbst als fehlenden Teil angegeben", "{2}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.kuerzen")
neu(T, "verstehen", "verfahren_waehlen", W(
    "Du willst prüfen, ob 14/21 und 2/3 gleich groß sind. Welcher Weg zeigt es sicher?",
    "14/21 durch 7 kürzen und das Ergebnis mit 2/3 vergleichen",
    [("Prüfen, ob sich Zähler und Nenner um dieselbe Zahl unterscheiden (14 − 2 und 21 − 3)", "additive Regel statt Erweitern und Kürzen"),
     ("Prüfen, ob 14 größer ist als 2", "nur die Zähler verglichen"),
     ("Prüfen, ob 14 + 21 so groß ist wie 2 + 3", "Zähler und Nenner addiert")],
    "Erweitern und Kürzen ändern den Wert nicht.",
    "Beim Kürzen werden Zähler und Nenner durch dieselbe Zahl geteilt: 14 : 7 = 2 und 21 : 7 = 3. Das ergibt 2/3. Differenzen oder Summen sagen nichts über den Wert.",
    lambda: F(14, 21) == F(2, 3) and 14 - 2 != 21 - 3), g="mehrschritt", regel="rr.kuerzen")
neu(T, "verstehen", "fehler_detektiv", FD(
    "Lena vergleicht 3/8 und 3/5.",
    [("Beide Brüche haben den Zähler 3.", True),
     ("Je größer der Nenner, desto größer der Bruch.", (F(3, 8) > F(3, 5)) == (8 > 5)),
     ("Also ist 3/8 größer als 3/5.", 8 > 5)],
    "Was passiert mit den Teilen, wenn man das Ganze in mehr Teile teilt?",
    "Je mehr Teile das Ganze hat, desto kleiner ist jedes Teil. Bei gleichem Zähler ist der Bruch mit dem größeren Nenner kleiner: 3/5 ist größer als 3/8."), regel="rr.bruchrechnen")
