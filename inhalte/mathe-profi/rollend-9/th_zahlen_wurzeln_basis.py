T = "zahlen.wurzeln_basis"
HZ = "id.zahlen.hoch_zurueck"
# ───────── quadratwurzel ─────────
neu(T, "quadratwurzel", "lueckenweg", L(
    "Berechne √1764 mit einer Zerlegung. Es gilt 1764 = 4 · 441. Die Wurzel aus einem Produkt ist das Produkt der beiden Wurzeln. Die Wurzel aus 441 ist ①. Die Wurzel aus 4 ist ②. Damit ist √1764 = ③.",
    KOMM(3), [21, 2, 42], ["21", "2", "{1} * {2}"], ["wz(441)", "wz(4)", "wz(441) * wz(4)"],
    "Suche eine Zahl, die mit sich selbst malgenommen 441 ergibt. Die beiden Wurzeln werden am Ende malgenommen.",
    "21 · 21 = 441, also ist die Wurzel aus 441 gleich 21. Die Wurzel aus 4 ist 2. Dann ist √1764 = 21 · 2 = 42. Probe: 42 · 42 = 1764.",
    {1: [(4, None, "die 4 stehen lassen, statt ihre Wurzel zu ziehen", "4")], 2: [(23, None, "die Wurzeln addiert statt malgenommen: 21 + 2", "{1} + {2}")]}), regel=HZ)
neu(T, "quadratwurzel", "umkehren", Z(
    "Für eine Zahl n gilt: √n + 3 = 17. Wie groß ist n?",
    196, "(17 - 3) ** 2", lambda: next(n for n in range(1, 1000) if math.isqrt(n) ** 2 == n and math.isqrt(n) + 3 == 17),
    "Mache zuerst das Addieren rückgängig. Dann das Wurzelziehen.",
    "Rückwärts: Erst 3 abziehen: √n = 17 − 3 = 14. Dann quadrieren: n = 14² = 196. Probe: √196 = 14 und 14 + 3 = 17.",
    [(286, None, "erst quadriert und danach 3 abgezogen", "17 ** 2 - 3"), (400, None, "3 addiert statt abgezogen und dann quadriert", "(17 + 3) ** 2"), (14, None, "nur 3 abgezogen, aber nicht quadriert: 17 − 3", "17 - 3")]), g="umkehr", regel=HZ)
neu(T, "quadratwurzel", "zwei_wege", Z(
    "Berechne √2025 auf zwei Wegen. Weg A: Zerlege 2025 in Primfaktoren (3 · 3 · 3 · 3 · 5 · 5) und bilde Paare. Weg B: Schätze zwischen zwei Quadraten voller Zehner und achte auf die Endziffer. Wie groß ist √2025?",
    45, "3 * 3 * 5", lambda: wz(2025),
    "Beide Wege müssen dasselbe Ergebnis haben.",
    "Weg A: Aus jedem Paar gleicher Faktoren kommt eine Zahl: 3 · 3 und 5. Also 3 · 3 · 5 = 45. Weg B: 40² = 1600 und 50² = 2500, die Wurzel liegt zwischen 40 und 50. Endziffer 5 gibt 45. Probe: 45 · 45 = 2025.",
    [(15, None, "aus den Primfaktoren nur je eine Sorte genommen: 3 · 5", "3 * 5"), (1012.5, "fb.hoch_zurueck.wurzel_halbiert", "2025 halbiert statt die Wurzel gezogen", "2025 / 2"), (405, None, "durch 5 geteilt statt die Wurzel gezogen: 2025 : 5", "2025 / 5")]), regel=HZ)

# ───────── wurzel_dezimal ─────────
neu(T, "wurzel_dezimal", "lueckenweg", L(
    "Berechne √0,0144 mit Brüchen. Es gilt 0,0144 = 144 : 10 000. Die Wurzel aus 144 ist ①. Die Wurzel aus 10 000 ist ②. Also ist √0,0144 genau ① : ② und das sind ③ Tausendstel.",
    KOMM(3), [12, 100, 120], ["12", "100", "{1} * 1000 // {2}"], ["wz(144)", "wz(10000)", "wz(144) / wz(10000) * 1000"],
    "Ziehe die Wurzel aus Zähler und Nenner getrennt. Zum Schluss auf den Nenner 1000 erweitern.",
    "√144 = 12 und √10 000 = 100. Also ist √0,0144 = 12 : 100 = 0,12. Das sind 120 Tausendstel (0,120). Probe: 0,12 · 0,12 = 0,0144.",
    {0: [(72, "fb.hoch_zurueck.wurzel_halbiert", "144 halbiert statt die Wurzel gezogen", "144 / 2")], 1: [(5000, "fb.hoch_zurueck.wurzel_halbiert", "10 000 halbiert statt die Wurzel gezogen", "10000 / 2"), (1000, None, "nur eine Null gestrichen: 10 000 : 10", "10000 / 10")]}), regel=HZ)
neu(T, "wurzel_dezimal", "fehler_detektiv", FD(
    "Kim berechnet √0,0081 ohne Taschenrechner.",
    [("0,0081 = 81 : 10 000", F("0.0081") == F(81, 10000), None),
     ("Die Wurzel aus 81 ist 9 und die Wurzel aus 10 000 ist 100.", wz(81) == 9 and wz(10000) == 100, None),
     ("√0,0081 = 9 : 10 = 0,9", wz(F("0.0081")) == F(9, 10), None)],
    "Quadriere das Ergebnis und vergleiche mit der Zahl unter der Wurzel.",
    "Zeile 1 und 2 stimmen. In Zeile 3 wird durch 10 geteilt, aber die Wurzel aus 10 000 ist 100. Richtig: 9 : 100 = 0,09. Probe: 0,09 · 0,09 = 0,0081."), regel=HZ)
neu(T, "wurzel_dezimal", "bruecke", W(
    "Die Wurzel aus dem Bruch 9/25 soll als Dezimalzahl geschrieben werden. Welche Dezimalzahl ist √(9/25)?",
    "0,6", [("0,36", "den Bruch nur in eine Dezimalzahl umgewandelt, ohne die Wurzel zu ziehen: 9/25", None, "9/25"), ("0,12", "nur aus dem Zähler die Wurzel gezogen: 3/25", None, "3/25"), ("1,8", "nur aus dem Nenner die Wurzel gezogen: 9/5", None, "9/5")],
    "Ziehe die Wurzel aus Zähler und Nenner und wandle dann den Bruch um.",
    "√(9/25) = √9 : √25 = 3/5 = 0,6. Probe: 0,6 · 0,6 = 0,36 = 9/25.",
    lambda: wz(F(9, 25)) == F(3, 5) == F("0.6")), g="darstellung", regel=HZ)

# ───────── kubikwurzel ─────────
neu(T, "kubikwurzel", "lueckenweg", L(
    "Berechne ∛(−343) − ∛27 in Schritten. Die dritte Wurzel aus 343 ist ①. Die dritte Wurzel aus einer negativen Zahl ist negativ. Also ist ∛(−343) gleich ②. Die dritte Wurzel aus 27 ist ③. Das Ergebnis der ganzen Rechnung ist ④.",
    KOMM(4), [7, -7, 3, -10], ["7", "-{1}", "3", "{2} - {3}"], ["kw(343)", "kw(-343)", "kw(27)", "kw(-343) - kw(27)"],
    "Rechne zur Probe: Zahl mal Zahl mal Zahl. Achte auf das Vorzeichen.",
    "7 · 7 · 7 = 343, also ∛343 = 7. Wegen des Minus ist ∛(−343) = −7, denn (−7) · (−7) · (−7) = −343. ∛27 = 3. Dann ist −7 − 3 = −10.",
    {1: [(7, "fb.vorzeichen.falsches_zeichen", "das Minuszeichen vergessen", "{1}")], 3: [(4, None, "mit +7 statt −7 gerechnet: 7 − 3", "{1} - {3}")]}), regel=HZ)
neu(T, "kubikwurzel", "zwei_wege", Z(
    "Berechne ∛1728 auf zwei Wegen. Weg A: Zerlege 1728 = 8 · 216 und ziehe aus beiden Faktoren die dritte Wurzel. Weg B: Schätze zwischen 10³ = 1000 und 20³ = 8000 und achte auf die Endziffer. Wie groß ist ∛1728?",
    12, "2 * 6", lambda: kw(1728),
    "Beide Wege müssen dasselbe Ergebnis haben.",
    "Weg A: ∛8 = 2 und ∛216 = 6, also 2 · 6 = 12. Weg B: Wegen 1000 < 1728 < 8000 liegt die Wurzel zwischen 10 und 20. Eine Kubikzahl mit Endziffer 8 gehört zu einer Zahl mit Endziffer 2: also 12. Probe: 12 · 12 · 12 = 1728.",
    [(8, None, "die beiden Wurzeln addiert statt malgenommen: 2 + 6", "2 + 6"), (576, None, "durch 3 geteilt statt die dritte Wurzel gezogen: 1728 : 3", "1728 / 3"), (864, "fb.hoch_zurueck.wurzel_halbiert", "1728 halbiert statt die dritte Wurzel gezogen", "1728 / 2")]), regel=HZ)
neu(T, "kubikwurzel", "anwenden", Z(
    "Ein würfelförmiger Komposter fasst 343 Liter. Wie viele Zentimeter ist eine Innenkante lang? Es gilt 1 Liter = 1 dm³.",
    70, "343 / 49 * 10", lambda: kw(343) * 10,
    "Zuerst die Kante in dm bestimmen, dann in cm umrechnen.",
    "343 Liter sind 343 dm³. Die Kante ist ∛343 = 7 dm. 1 dm = 10 cm, also 7 · 10 = 70 cm.",
    [(7, None, "in dm stehen geblieben, nicht in cm umgerechnet", "cbrt(343)"), (114.33, None, "durch drei geteilt statt die dritte Wurzel gezogen (auf zwei Stellen gerundet)", "round(343 / 3, 2)"), (700, None, "mit 100 statt mit 10 umgerechnet", "cbrt(343) * 100")], "cm"), g="einkleidung", regel=HZ)

# ───────── abschaetzen ─────────
neu(T, "abschaetzen", "lueckenweg", L(
    "Schätze √300 mit Quadratzahlen. Die größte ganze Zahl a mit a² ≤ 300 ist ①. Das Quadrat der nächsten ganzen Zahl, also (a + 1)², ist ②. Dann liegt es um ③ über 300.",
    KOMM(3), [17, 324, 24], ["17", "({1} + 1) ** 2", "{2} - 300"], ["isq(300)", "18 * 18", "324 - 300"],
    "Quadriere ganze Zahlen, bis du über 300 kommst.",
    "17² = 289 ≤ 300 und 18² = 324 > 300. Also a = 17. Dann ist (a + 1)² = 18² = 324. Der Unterschied zu 300 ist 24. Damit gilt 17 < √300 < 18.",
    {0: [(18, None, "die erste Zahl genommen, deren Quadrat schon über 300 liegt: 17 + 1", "17 + 1")], 1: [(290, None, "nur 1 zum Quadrat der ersten Zahl addiert", "{1} ** 2 + 1"), (35, None, "die beiden Zahlen addiert: 17 + 18", "{1} + ({1} + 1)")]}), regel=HZ)
neu(T, "abschaetzen", "bruecke", W(
    "Die Tabelle zeigt Quadratzahlen. Zwischen welchen aufeinanderfolgenden ganzen Zahlen liegt √200?",
    "zwischen 14 und 15", [("zwischen 13 und 14", "eine Spalte zu weit links abgelesen: 200 liegt über 196, nicht darunter"), ("zwischen 15 und 16", "eine Spalte zu weit rechts abgelesen: 200 liegt unter 225")],
    "Suche in der unteren Zeile die beiden Zahlen, zwischen denen 200 liegt. Die Wurzeln stehen in der oberen Zeile.",
    "196 < 200 < 225. Die Quadratzahlen gehören zu 14 und 15. Also gilt 14 < √200 < 15.",
    lambda: 14 ** 2 < 200 < 15 ** 2 and not 13 ** 2 < 200 < 14 ** 2 and not 15 ** 2 < 200 < 16 ** 2,
    grafik=TAB(["n", "11", "12", "13", "14", "15", "16"], ["n²", "121", "144", "169", "196", "225", "256"])), g="darstellung", regel=HZ)
neu(T, "abschaetzen", "anwenden", Z(
    "Ein quadratisches Beet soll mindestens 40 m² groß sein. Die Seitenlänge ist eine ganze Zahl in Metern. Rundherum soll ein Zaun stehen. Wie viele Meter Zaun braucht man dann mindestens?",
    28, "4 * (6 + 1)", lambda: 4 * next(n for n in range(1, 50) if n * n >= 40),
    "Finde zuerst die kleinste ganze Seitenlänge, deren Quadrat mindestens 40 ist.",
    "6² = 36 ist zu klein, 7² = 49 reicht. Die Seite ist mindestens 7 m lang. Der Zaun ist der Umfang: 4 · 7 = 28 m.",
    [(24, None, "mit der abgerundeten Seite 6 m gerechnet: 4 · 6", "4 * 6"), (160, None, "mit der Fläche statt der Seite gerechnet: 4 · 40", "4 * 40"), (7, None, "nur die Seitenlänge angegeben, nicht den Zaun", "7")], "m"), g="einkleidung", regel=HZ)

# ───────── wurzel_deuten ─────────
neu(T, "wurzel_deuten", "lueckenweg", L(
    "Löse die Gleichung x² = 196. Die positive Lösung ist ①. Die negative Lösung ist ②. Dann liegen die beiden Lösungen auf der Zahlengeraden ③ Einheiten auseinander.",
    KOMM(3), [14, -14, 28], ["14", "-{1}", "{1} - {2}"], ["wz(196)", "-wz(196)", "2 * wz(196)"],
    "Es gibt zwei Zahlen, die quadriert dieselbe Zahl ergeben. Achte auf das Vorzeichen.",
    "14 · 14 = 196 und (−14) · (−14) = 196. Die Lösungen sind 14 und −14. Ihr Abstand ist 14 − (−14) = 28.",
    {1: [(14, "fb.gegenrechnung.zweite_loesung_fehlt", "nur die positive Lösung eingetragen", "{1}")], 2: [(0, None, "die beiden Lösungen addiert: 14 + (−14)", "{1} + {2}")]}), regel=HZ)
neu(T, "wurzel_deuten", "fehler_detektiv", FD(
    "Kim berechnet √((−7)²) + (√9)².",
    [("(−7)² = 49", 49 == (-7) ** 2, None),
     ("√49 = −7, denn Wurzel und Quadrat heben sich auf.", wz(49) == -7, None),
     ("(√9)² = 9, also ist die Summe −7 + 9 = 2.", 7 + 9 == 2, -7 + 9 == 2 and 3 ** 2 == 9)],
    "Was bedeutet √49? Die Wurzel ist nie negativ.",
    "Zeile 1 stimmt. In Zeile 2 steht der Fehler: √49 ist die nicht negative Zahl, deren Quadrat 49 ist, also 7. Zeile 3 rechnet mit −7 richtig weiter. Richtig ist 7 + 9 = 16."), regel=HZ)
neu(T, "wurzel_deuten", "umkehren", Z(
    "Unter einer Wurzel steht der Term x + 5. Die Wurzel hat den Wert 6. Wie groß ist x?",
    31, "6 ** 2 - 5", lambda: next(x for x in range(-5, 200) if math.isqrt(x + 5) ** 2 == x + 5 and math.isqrt(x + 5) == 6),
    "Mache das Wurzelziehen rückgängig. Dann die Addition.",
    "Rückwärts: Erst quadrieren: x + 5 = 6² = 36. Dann 5 abziehen: x = 31. Probe: √(31 + 5) = √36 = 6.",
    [(1, None, "nur 5 abgezogen, nicht quadriert: 6 − 5", "6 - 5"), (41, None, "5 addiert statt abgezogen", "6 ** 2 + 5"), (11, None, "die beiden Zahlen addiert: 6 + 5", "6 + 5")]), g="umkehr", regel=HZ)

# ───────── wurzel_sache ─────────
neu(T, "wurzel_sache", "lueckenweg", L(
    "Ein quadratischer Spielplatz hat 3 600 m² Fläche. Er wird rundherum eingezäunt. Ein Meter Zaun kostet 12 €. Die Seite des Platzes ist ① m lang. Dann ist der Zaun ② m lang. Also kostet der Zaun insgesamt ③ €.",
    KOMM(3), [60, 240, 2880], ["60", "4 * {1}", "{2} * 12"], ["wz(3600)", "4 * wz(3600)", "4 * wz(3600) * 12"],
    "Aus der Fläche folgt die Seite. Der Zaun geht um den ganzen Platz herum.",
    "Die Seite ist √3600 = 60 m. Der Zaun ist so lang wie der Umfang: 4 · 60 = 240 m. Die Kosten sind 240 · 12 = 2 880 €.",
    {0: [(1800, "fb.hoch_zurueck.wurzel_halbiert", "3 600 halbiert statt die Wurzel gezogen", "3600 / 2")], 1: [(120, None, "nur zwei Seiten gezählt: 2 · 60", "2 * {1}")], 2: [(720, None, "mit der Seitenlänge statt mit dem Zaun gerechnet: 60 · 12", "{1} * 12")]}), regel=HZ)
neu(T, "wurzel_sache", "umkehren", Z(
    "Ein quadratisches Feld wird auf jeder Seite um 3 m verlängert. Danach hat es 144 m² Fläche. Wie groß war die Fläche vor der Verlängerung?",
    81, "(12 - 3) ** 2", lambda: (wz(144) - 3) ** 2,
    "Rechne rückwärts: erst von der neuen Fläche zur neuen Seite.",
    "Die neue Seite ist √144 = 12 m. Vorher war sie 12 − 3 = 9 m lang. Die alte Fläche ist 9² = 81 m².",
    [(141, None, "von der Fläche einfach 3 abgezogen: 144 − 3", "144 - 3"), (9, None, "die alte Seitenlänge als Fläche angegeben: 12 − 3", "12 - 3")], "m²"), g="umkehr", regel=HZ)
neu(T, "wurzel_sache", "anwenden", Z(
    "Ein quadratisches Solarfeld soll eine Leistung von 36 kW haben. Ein Quadratmeter der Module liefert 250 W. Es gilt 1 kW = 1 000 W. Wie lang ist eine Seite des Feldes in Metern?",
    12, "144 / 12", lambda: wz(F(36 * 1000, 250)),
    "Teile zuerst die Gesamtleistung durch die Leistung je Quadratmeter. Das ergibt die Fläche.",
    "36 kW sind 36 000 W. Fläche: 36 000 : 250 = 144 m². Seite: √144 = 12 m.",
    [(144, None, "bei der Fläche stehen geblieben: 36 000 : 250", "36000 / 250"), (72, "fb.hoch_zurueck.wurzel_halbiert", "die Fläche halbiert statt die Wurzel gezogen", "144 / 2"), (48, None, "den Umfang statt der Seite angegeben: 4 · 12", "4 * 12")], "m"), g="einkleidung", regel=HZ)
