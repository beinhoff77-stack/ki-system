T = "zahlen.reell"
HZ = "id.zahlen.hoch_zurueck"
# ───────── zahlarten ─────────
neu(T, "zahlarten", "verfahren_waehlen", W(
    "Du sollst entscheiden, ob √50 eine rationale Zahl ist. Welcher Weg führt sicher zum Ziel?",
    "Prüfen, ob 50 eine Quadratzahl ist. Wegen 7² = 49 und 8² = 64 ist 50 keine Quadratzahl. Also ist √50 irrational.",
    [("Den Taschenrechner benutzen. Die Anzeige 7,0710678 hört irgendwo auf, also ist √50 rational.", "eine endliche Anzeige für das Ende der Dezimalzahl gehalten"),
     ("Zerlegen: √50 = 5 · √2. Weil 5 rational ist, ist auch 5 · √2 rational.", "Produkt mit einer rationalen Zahl für rational gehalten"),
     ("Prüfen, ob 50 gerade ist. Weil 50 gerade ist, ist √50 rational.", "gerade Zahl unter der Wurzel mit rationalem Ergebnis verwechselt")],
    "Frage dich: Für welche natürlichen Zahlen n ist √n rational?",
    "Für natürliche Zahlen n gilt: √n ist nur dann rational, wenn n eine Quadratzahl ist. 7² = 49 < 50 < 64 = 8², also ist 50 keine Quadratzahl und √50 ist irrational. Eine endliche Taschenrechner-Anzeige beweist nichts, und 5 · √2 ist ebenfalls irrational.",
    lambda: math.isqrt(50) ** 2 != 50), g="erkennen", regel=HZ)
neu(T, "zahlarten", "umkehren", Z(
    "Eine natürliche Zahl x liegt zwischen 60 und 80. Außerdem ist √x eine rationale Zahl. Wie groß ist x?",
    64, "8 ** 2", lambda: next(x for x in range(61, 80) if math.isqrt(x) ** 2 == x),
    "Welche Quadratzahlen liegen zwischen 60 und 80?",
    "√x ist für natürliche x nur rational, wenn x eine Quadratzahl ist. Zwischen 60 und 80 liegt nur 8² = 64 (denn 7² = 49 ist zu klein, 9² = 81 zu groß). Also ist x = 64.",
    [(8, None, "die Wurzel statt der Zahl x angegeben", "8"), (70, None, "die Mitte des Bereichs genommen: (60 + 80) : 2", "(60 + 80) / 2")]), g="umkehr", regel=HZ)
neu(T, "zahlarten", "fehler_detektiv", FD(
    "Kim ordnet die Zahl −√36 in die Zahlenmengen ein.",
    [("Eine Wurzel ist immer irrational.", wz(36).denominator != 0 and wz(36) in (F(6),) and False, None),
     ("Also ist auch −√36 irrational.", False, True),
     ("Darum gehört −√36 nicht zu ℚ, sondern nur zu ℝ.", False, True)],
    "Rechne √36 aus. Ist das Ergebnis eine rationale Zahl?",
    "Zeile 1 ist falsch: √36 = 6 ist rational. Die Wurzel aus einer Quadratzahl ist rational. Die Zeilen 2 und 3 folgen aus Zeile 1 richtig. Richtig: −√36 = −6 gehört zu ℤ, ℚ und ℝ."), regel=HZ)

# ───────── eingrenzen ─────────
neu(T, "eingrenzen", "lueckenweg", L(
    "Grenze √90 auf eine Nachkommastelle ein. Dazu werden 94 und 95 quadriert und mit 90 · 100 verglichen. Es ist 94² = ①. Dann ist 95² = ②. Also liegt 95² um ③ über 90 · 100.",
    KOMM(3), [8836, 9025, 25], ["8836", "{1} + 2 * 94 + 1", "{2} - 9000"], ["94 * 94", "95 * 95", "95 * 95 - 90 * 100"],
    "Rechne 94 · 94 als 90 · 94 plus 4 · 94. Vergleichen musst du mit 90 · 100, nicht mit 90.",
    "94² = 8 836 und 95² = 9 025. Die Vergleichszahl ist 90 · 100 = 9 000. Es gilt 8 836 < 9 000 < 9 025, also 9,4 < √90 < 9,5. 95² liegt um 9 025 − 9 000 = 25 über 9 000.",
    {0: [(188, None, "94 verdoppelt statt quadriert: 94 · 2", "94 * 2")], 2: [(8935, None, "mit 90 statt mit 9 000 verglichen: 9 025 − 90", "{2} - 90")]}), regel=HZ)
neu(T, "eingrenzen", "bruecke", W(
    "Die Tabelle zeigt Quadrate von Zahlen mit einer Nachkommastelle. Zwischen welchen beiden Zahlen der oberen Zeile liegt √7?",
    "zwischen 2,6 und 2,7", [("zwischen 2,7 und 2,8", "die Zeile mit 7,29 als untere Grenze genommen: 7,29 liegt über 7"), ("zwischen 2,5 und 2,6", "zu weit links abgelesen: 6,76 ist schon näher an 7"), ("zwischen 6,76 und 7,29", "die Quadrate aus der unteren Zeile als Grenzen der Wurzel genommen")],
    "In der unteren Zeile suchst du zwei Quadrate, zwischen denen 7 liegt. Die Wurzel steht darüber.",
    "6,76 < 7 < 7,29. Die Quadrate gehören zu 2,6 und 2,7. Also gilt 2,6 < √7 < 2,7.",
    lambda: F("2.6") ** 2 < 7 < F("2.7") ** 2 and not F("2.7") ** 2 < 7 < F("2.8") ** 2 and not F("2.5") ** 2 < 7 < F("2.6") ** 2,
    grafik=TAB(["x", "2,5", "2,6", "2,7", "2,8"], ["x²", "6,25", "6,76", "7,29", "7,84"])), g="darstellung", regel=HZ)
neu(T, "eingrenzen", "anwenden", Z(
    "Eine quadratische Holzplatte hat 7 m² Fläche. Wie lang ist eine Seite in Zentimetern? Runde auf ganze Zentimeter.",
    265, RC(math.sqrt(70000), 0), lambda: dwurzel(70000, 0),
    "Rechne erst die Fläche in cm² um: 1 m² = 10 000 cm².",
    "7 m² = 70 000 cm². Die Seite ist √70 000 ≈ 264,58 cm. Gerundet auf ganze Zentimeter: 265 cm. Probe: 265 · 265 = 70 225, das ist nahe an 70 000.",
    [(2.65, None, "in Metern stehen geblieben (auf zwei Stellen gerundet)", "round(sqrt(7), 2)"), (264, None, "abgeschnitten statt gerundet", "floor(sqrt(70000))"), (3.5, "fb.hoch_zurueck.wurzel_halbiert", "7 halbiert statt die Wurzel gezogen", "7 / 2")], "cm"), g="transfer", regel=HZ)

# ───────── heron ─────────
neu(T, "heron", "lueckenweg", L(
    "Heron-Verfahren für √45 mit dem Startwert 9. Das Rechteck mit der Fläche 45 und der Seite 9 hat die andere Seite ①. Dann ist der neue Näherungswert, der Mittelwert der beiden Seiten, gleich ②. Das Quadrat dieses Werts ist ③. Also liegt es um ④ über 45.",
    KOMM(4), [5, 7, 49, 4], ["45 // 9", "(9 + {1}) // 2", "{2} ** 2", "{3} - 45"], ["45 / 9", "(9 + 45 / 9) / 2", "((9 + 45 / 9) / 2) ** 2", "((9 + 45 / 9) / 2) ** 2 - 45"],
    "Die andere Seite ist die Fläche geteilt durch die bekannte Seite. Der Mittelwert zweier Zahlen ist ihre Summe geteilt durch die Anzahl der Zahlen.",
    "45 : 9 = 5. Mittelwert: (9 + 5) : 2 = 7. Das Quadrat ist 7² = 49. Es liegt um 49 − 45 = 4 über 45. Der neue Wert 7 ist besser als 9, denn 9² = 81 liegt um 36 über 45.",
    {0: [(405, None, "mit 9 malgenommen statt geteilt: 45 · 9", "45 * 9")], 1: [(14, None, "die Summe nicht halbiert: 9 + 5", "9 + {1}")]}), regel=HZ)
neu(T, "heron", "zwei_wege", Z(
    "Bestimme √12 auf zwei Nachkommastellen gerundet auf zwei Wegen. Weg A: Intervallschachtelung mit Zehntelzahlen, dann mit Hundertstelzahlen, und die Mitte der letzten Schachtel prüfen. Weg B: Heron-Verfahren mit dem Startwert 3,5 und zwei Schritten. Wie lautet der gerundete Wert?",
    3.46, RC(math.sqrt(12), 2), lambda: dwurzel(12, 2),
    "Beide Wege müssen denselben gerundeten Wert ergeben.",
    "Weg A: 3,4² = 11,56 < 12 < 12,25 = 3,5². Dann 3,46² = 11,9716 < 12 < 12,0409 = 3,47². Die Mitte 3,465² = 12,006… ist größer als 12, also liegt √12 unter 3,465 und wird zu 3,46 gerundet. Weg B: x₁ = (3,5 + 12 : 3,5) : 2 ≈ 3,4643, x₂ ≈ 3,4641. Gerundet 3,46.",
    [(3.47, None, "die obere Grenze der Schachtel genommen statt zu runden", "3.47"), (3.5, None, "nur auf eine Nachkommastelle gerundet", "round(sqrt(12), 1)"), (6, "fb.hoch_zurueck.wurzel_halbiert", "12 halbiert statt die Wurzel gezogen", "12 / 2")]), g="verknuepfen", regel=HZ)
neu(T, "heron", "anwenden", Z(
    "Ein quadratisches Beet soll 10 m² Fläche haben. Als Startwert für die Seite wird 3 m genommen. Wie groß ist der neue Näherungswert für die Seite nach einem Schritt des Heron-Verfahrens? Runde auf drei Nachkommastellen.",
    3.167, RC((3 + 10 / 3) / 2, 3), lambda: F(str(round(float((F(3) + F(10, 3)) / 2), 3))),
    "Das Rechteck mit der Fläche 10 und der Seite 3 hat eine zweite Seite. Dann wird der Mittelwert gebildet.",
    "Die andere Seite ist 10 : 3 ≈ 3,3333. Der Mittelwert ist (3 + 3,3333) : 2 ≈ 3,1667. Gerundet: 3,167 m. Zum Vergleich: √10 ≈ 3,1623.",
    [(3.333, None, "nur die andere Seite genommen, nicht gemittelt", "round(10 / 3, 3)"), (6.333, None, "die Summe der beiden Seiten nicht halbiert", "round(3 + 10 / 3, 3)")], "m"), g="einkleidung", regel=HZ)

# ───────── wurzel_mal ─────────
neu(T, "wurzel_mal", "lueckenweg", L(
    "Berechne √18 · √8 − √25. Beide Wurzeln werden zu einer Wurzel zusammengefasst. Unter der Wurzel steht dann ①. Die Wurzel daraus ist ②. Dann ist das Ergebnis der ganzen Rechnung ③.",
    KOMM(3), [144, 12, 7], ["18 * 8", "12", "{2} - 5"], ["18 * 8", "wz(18 * 8)", "wz(18 * 8) - wz(25)"],
    "Es gilt √a · √b = √(a · b). Zum Schluss nicht vergessen, √25 zu berechnen.",
    "√18 · √8 = √(18 · 8) = √144 = 12. Dann ist 12 − √25 = 12 − 5 = 7.",
    {0: [(26, None, "unter der Wurzel addiert: 18 + 8", "18 + 8")], 1: [(72, "fb.hoch_zurueck.wurzel_halbiert", "144 halbiert statt die Wurzel gezogen", "{1} / 2")], 2: [(-13, None, "25 statt √25 abgezogen: 12 − 25", "{2} - 25")]}), regel=HZ)
neu(T, "wurzel_mal", "fehler_detektiv", FD(
    "Kim vereinfacht √(5x) · √(20x) für x ≥ 0.",
    [("√(5x) · √(20x) = √(5x · 20x)", all(abs(math.sqrt(5 * x) * math.sqrt(20 * x) - math.sqrt(5 * x * 20 * x)) < 1e-9 for x in (1, 2, 7)), None),
     ("= √(25x)", all(abs(5 * x * 20 * x - 25 * x) < 1e-9 for x in (1, 2, 7)), None),
     ("= 5 · √x", all(abs(math.sqrt(25 * x) - 5 * math.sqrt(x)) < 1e-9 for x in (1, 2, 7)), True)],
    "Rechne 5x · 20x für x = 2 aus und vergleiche mit der Zeile.",
    "Zeile 1 stimmt. In Zeile 2 wurde 5x · 20x falsch berechnet: 5 · 20 = 100 und x · x = x², also √(100x²) = 10x. Zeile 3 rechnet mit √(25x) richtig weiter: √(25x) = 5 · √x."), regel=HZ)
neu(T, "wurzel_mal", "umkehren", Z(
    "Für eine positive Zahl a gilt √a · √12 = 18. Wie groß ist a?",
    27, "18 ** 2 / 12", lambda: next(a for a in range(1, 1000) if abs(math.sqrt(a) * math.sqrt(12) - 18) < 1e-9),
    "Fasse beide Wurzeln zu einer Wurzel zusammen. Dann machst du das Wurzelziehen rückgängig.",
    "√a · √12 = √(12a) = 18. Quadrieren: 12a = 324. Also a = 324 : 12 = 27. Probe: √27 · √12 = √324 = 18.",
    [(324, None, "nur quadriert, nicht durch 12 geteilt", "18 ** 2"), (6, None, "die Zahlen voneinander abgezogen: 18 − 12", "18 - 12"), (216, None, "18 mit 12 malgenommen: 18 · 12", "18 * 12")]), g="umkehr", regel=HZ)

# ───────── teilweise ─────────
neu(T, "teilweise", "lueckenweg", L(
    "Schreibe √288 als a · √b mit möglichst kleiner Zahl b. Es gilt 288 = 144 · b. Die Zahl b ist ①. Die Wurzel aus 144 ist ②. Dann ist a gleich ②. Also ist a + b gleich ③.",
    KOMM(3), [2, 12, 14], ["288 // 144", "12", "{1} + {2}"], ["288 / 144", "wz(144)", "wz(144) + 288 / 144"],
    "Welche Zahl mal 144 ergibt 288? Zum Schluss werden die beiden Zahlen addiert.",
    "b = 288 : 144 = 2 und a = √144 = 12. Also √288 = 12 · √2. Die Summe ist a + b = 12 + 2 = 14.",
    {0: [(144, None, "288 − 144 gerechnet", "288 - 144")], 1: [(72, "fb.hoch_zurueck.wurzel_halbiert", "144 halbiert statt die Wurzel gezogen", "144 / 2")], 2: [(24, None, "a mal b statt a plus b: 12 · 2", "{1} * {2}")]}), regel=HZ)
neu(T, "teilweise", "bruecke", W(
    "Schreibe 6√2 als eine einzige Wurzel. Welche Wurzel ist es?",
    "√72", [("√12", "die Zahlen 6 und 2 unter der Wurzel malgenommen, die 6 aber nicht quadriert: 6 · 2", None, "6 * 2"), ("√8", "die Zahlen 6 und 2 addiert: 6 + 2", None, "6 + 2"), ("√38", "6 quadriert, aber 2 addiert statt malgenommen: 6² + 2", None, "6 ** 2 + 2")],
    "Die 6 muss in die Wurzel hinein. Dafür wird sie quadriert: √36 = 6.",
    "6 = √36. Also 6√2 = √36 · √2 = √(36 · 2) = √72. Probe: √72 = √(36 · 2) = 6√2.",
    lambda: 6 ** 2 * 2 == 72 and 6 ** 2 * 2 not in (12, 8, 38)), g="darstellung", regel=HZ)
neu(T, "teilweise", "zwei_wege", Z(
    "Ziehe aus √1800 teilweise die Wurzel, bis √2 übrig bleibt: √1800 = a · √2. Weg A: Spalte die größte passende Quadratzahl als Faktor ab. Weg B: Zerlege 1800 in Primfaktoren (2 · 2 · 2 · 3 · 3 · 5 · 5) und bilde Paare. Wie groß ist a?",
    30, "2 * 3 * 5", lambda: next(a for a in range(1, 100) if a * a * 2 == 1800),
    "Beide Wege müssen dasselbe a ergeben.",
    "Weg A: 1800 = 900 · 2 und √900 = 30. Weg B: Paare 2 · 2, 3 · 3 und 5 · 5. Aus jedem Paar kommt eine Zahl vor die Wurzel: 2 · 3 · 5 = 30. Die einzelne 2 bleibt unter der Wurzel. Also √1800 = 30 · √2.",
    [(900, "fb.hoch_zurueck.wurzel_halbiert", "1800 halbiert statt die Wurzel gezogen", "1800 / 2"), (15, None, "das Paar aus den Zweien vergessen: 3 · 5", "3 * 5"), (180, None, "durch 10 geteilt statt die Wurzel gezogen: 1800 : 10", "1800 / 10")]), g="verknuepfen", regel=HZ)

# ───────── zusammenfassen ─────────
neu(T, "zusammenfassen", "lueckenweg", L(
    "Fasse zusammen: √54 + √96 − √24. Jede Wurzel wird als Vielfaches von √6 geschrieben. Es gilt √54 = ①·√6. Es gilt √96 = ②·√6. Es gilt √24 = ③·√6. Also ist √54 + √96 − √24 = ④·√6.",
    KOMM(4), [3, 4, 2, 5], ["3", "4", "2", "{1} + {2} - {3}"], ["wz(54 / 6)", "wz(96 / 6)", "wz(24 / 6)", "wz(54 / 6) + wz(96 / 6) - wz(24 / 6)"],
    "Zerlege jede Zahl unter der Wurzel in eine Quadratzahl mal die gemeinsame Zahl. Am Ende werden nur die Vorfaktoren verrechnet.",
    "54 = 9 · 6, also √54 = 3√6. 96 = 16 · 6, also √96 = 4√6. 24 = 4 · 6, also √24 = 2√6. Dann 3 + 4 − 2 = 5. Ergebnis: 5√6.",
    {0: [(9, None, "54 : 6 = 9 stehen geblieben, die Wurzel nicht gezogen", "54 / 6")], 3: [(9, None, "alle Vorfaktoren addiert: 3 + 4 + 2", "{1} + {2} + {3}"), (1, None, "falsch verrechnet: 3 − 4 + 2", "{1} - {2} + {3}")]}), regel=HZ)
neu(T, "zusammenfassen", "fehler_detektiv", FD(
    "Kim fasst √12 + √27 zusammen.",
    [("Die Wurzel aus 12 ist gleich 2√3.", abs(math.sqrt(12) - 2 * math.sqrt(3)) < 1e-9, None),
     ("Die Wurzel aus 27 ist gleich 3√3.", abs(math.sqrt(27) - 3 * math.sqrt(3)) < 1e-9, None),
     ("2√3 + 3√3 = 5√6", abs(2 * math.sqrt(3) + 3 * math.sqrt(3) - 5 * math.sqrt(6)) < 1e-9, None),
     ("5√6 ≈ 12,25", False, abs(5 * math.sqrt(6) - 12.25) < 0.005)],
    "Bei gleichen Wurzeln werden nur die Zahlen vor der Wurzel zusammengefasst. Prüfe, was dabei mit der Zahl unter der Wurzel passiert.",
    "Zeile 1 und 2 stimmen. In Zeile 3 wurde die Zahl unter der Wurzel verändert. Richtig: 2√3 + 3√3 = 5√3. Zeile 4 rechnet mit dem falschen Wert richtig weiter. Richtig: 5√3 ≈ 8,66.", ), regel=HZ)
neu(T, "zusammenfassen", "anwenden", Z(
    "Ein rechteckiger Bilderrahmen hat die Seitenlängen √18 dm und √8 dm. Wie lang ist sein Umfang? Runde auf eine Nachkommastelle.",
    14.1, RC(2 * (math.sqrt(18) + math.sqrt(8)), 1), lambda: dwurzel(200, 1),
    "Vereinfache zuerst beide Wurzeln. Dann kannst du zusammenfassen.",
    "√18 = 3√2 und √8 = 2√2. Umfang = 2 · (3√2 + 2√2) = 10√2 ≈ 14,142 dm. Gerundet: 14,1 dm.",
    [(10.2, None, "die Zahlen unter den Wurzeln addiert: 2 · √26", "round(2 * sqrt(26), 1)"), (7.1, None, "den Umfang nur als Summe zweier Seiten gerechnet", "round(sqrt(18) + sqrt(8), 1)"), (17, None, "alle vier Seiten so lang wie die längere Seite gerechnet", "round(4 * sqrt(18), 1)")], "dm"), g="einkleidung", regel=HZ)

# ───────── nenner_rational ─────────
neu(T, "nenner_rational", "lueckenweg", L(
    "Mache den Nenner rational: 28/(6√7). Dazu wird der Bruch mit √7 erweitert. Der neue Nenner (ohne Wurzel) ist ①. Der größte gemeinsame Teiler von 28 und ① ist ②. Also ist das Ergebnis nach dem Kürzen ③ · √7 geteilt durch ④.",
    KOMM(4), [42, 14, 2, 3], ["6 * 7", "ggT(28, {1})", "28 // {2}", "{1} // {2}"], ["6 * 7", "14", "28 / 14", "42 / 14"],
    "Beim Erweitern mit √7 gilt √7 · √7 = 7. Der Faktor vor der Wurzel im Nenner bleibt erhalten.",
    "Der Nenner wird 6 · √7 · √7 = 6 · 7 = 42. Der Zähler wird 28√7. Der größte gemeinsame Teiler von 28 und 42 ist 14. Kürzen: 28√7/42 = (2 · √7)/3.",
    {0: [(7, None, "den Faktor 6 vergessen: nur √7 · √7", "7"), (13, None, "6 + 7 gerechnet", "6 + 7")], 3: [(42, None, "nicht gekürzt, den Nenner stehen lassen", "{1}")]}), regel=HZ)
neu(T, "nenner_rational", "zwei_wege", Z(
    "Schreibe 30/√6 als a · √6 auf zwei Wegen. Weg A: Erweitere den Bruch mit √6. Weg B: Schreibe 30 als 5 · 6 = 5 · √6 · √6 und kürze mit √6. Wie groß ist a?",
    5, "30 / 6", lambda: next(a for a in range(1, 100) if abs(30 / math.sqrt(6) - a * math.sqrt(6)) < 1e-9),
    "Beide Wege müssen dasselbe a ergeben.",
    "Weg A: 30/√6 = (30 · √6)/(√6 · √6) = 30√6/6 = 5√6. Weg B: 30/√6 = (5 · √6 · √6)/√6 = 5√6. Also a = 5.",
    [(30, None, "nach dem Erweitern nicht durch 6 gekürzt", "30"), (180, None, "mit 6 statt durch 6 gerechnet: 30 · 6", "30 * 6"), (24, None, "6 abgezogen statt geteilt: 30 − 6", "30 - 6")]), g="mehrschritt", regel=HZ)
neu(T, "nenner_rational", "umkehren", Z(
    "Der Bruch a/(2√5) hat denselben Wert wie 3√5. Wie groß ist a?",
    30, "3 * 2 * 5", lambda: next(a for a in range(1, 200) if abs(a / (2 * math.sqrt(5)) - 3 * math.sqrt(5)) < 1e-9),
    "Multipliziere beide Seiten mit dem Nenner 2√5. Dann gilt √5 · √5 = 5.",
    "Aus a/(2√5) = 3√5 folgt a = 3√5 · 2√5 = 3 · 2 · 5 = 30. Probe: 30/(2√5) = 15/√5 = 15√5/5 = 3√5.",
    [(6, None, "die Wurzeln vergessen: 3 · 2", "3 * 2"), (15, None, "den Faktor 2 aus dem Nenner vergessen: 3 · 5", "3 * 5"), (150, None, "√5 · √5 zweimal gerechnet: 3 · 2 · 5 · 5", "3 * 2 * 5 * 5")]), g="rueckwaerts", regel=HZ)

# ───────── irrational_beweis ─────────
neu(T, "irrational_beweis", "verfahren_waehlen", W(
    "Du sollst beweisen, dass √5 irrational ist. Welcher Weg führt zum Ziel?",
    "Annahme: √5 = p/q mit teilerfremden ganzen Zahlen p und q. Quadrieren gibt p² = 5q². Dann folgt, dass p und q beide durch 5 teilbar wären. Das ist ein Widerspruch.",
    [("√5 mit dem Taschenrechner auf 20 Stellen ausrechnen und prüfen, dass sich keine Ziffernfolge wiederholt.", "endlich viele Stellen können nichts beweisen"),
     ("Zeigen, dass √5 keine ganze Zahl ist: 2² = 4 und 3² = 9.", "damit ist nur gezeigt, dass √5 nicht ganz ist, nicht dass es kein Bruch ist"),
     ("Annahme: √5 ist irrational. Dann einen Widerspruch suchen.", "die Annahme steht verkehrt herum: man nimmt das Gegenteil dessen an, was man zeigen will")],
    "Beim indirekten Beweis nimmt man das Gegenteil der Behauptung an.",
    "Ein indirekter Beweis nimmt das Gegenteil an: √5 ist rational, also ein gekürzter Bruch p/q. Quadrieren gibt p² = 5q². Dann ist p durch 5 teilbar, und mit p = 5r auch q. Das widerspricht der Kürzung. Zahlenbeispiele oder Taschenrechner beweisen nichts.",
    lambda: True), g="erkennen", regel=HZ)
neu(T, "irrational_beweis", "fehler_detektiv", FD(
    "Kim beweist, dass √3 irrational ist.",
    [("Annahme: √3 = p/q mit teilerfremden p und q.", True, None),
     ("Quadrieren: p² = 3q².", all(abs((q * math.sqrt(3)) ** 2 - 3 * q * q) < 1e-9 for q in (1, 5, 7)), None),
     ("Dann ist p² durch 3 teilbar, also ist p durch 9 teilbar.", (6 ** 2 % 3 != 0) or (6 % 9 == 0), None),
     ("Mit p = 9r folgt 81r² = 3q², also q² = 27r². Dann ist auch q durch 3 teilbar.", False, all(81 * r * r // 3 == 27 * r * r for r in (1, 2, 5)) and all((27 * r * r) % 3 == 0 for r in (1, 2, 5)))],
    "Wenn p² durch 3 teilbar ist: Durch welche Zahl muss p dann teilbar sein? Probiere p = 6.",
    "Zeile 1 und 2 stimmen. In Zeile 3 steht der Fehler: Aus „p² ist durch 3 teilbar“ folgt nur „p ist durch 3 teilbar“ (zum Beispiel p = 6, aber 6 ist nicht durch 9 teilbar). Richtig: p = 3r. Zeile 4 rechnet mit p = 9r richtig weiter."), regel=HZ)
neu(T, "irrational_beweis", "umkehren", W(
    "Ein Beweis endet so: „Aus p² = 3q² folgt, dass p durch 3 teilbar ist. Dann ist auch q durch 3 teilbar. Das widerspricht der Kürzung.“ Für welche Zahl wurde bewiesen, dass sie irrational ist?",
    "√3", [("√2", "den Faktor 2 statt 3 genommen"), ("√6", "6 = 2 · 3 genommen; dann stünde p² = 6q² da"), ("√9", "9 = 3 · 3 genommen; √9 = 3 ist aber rational")],
    "Welche Gleichung für p² steht am Anfang des Beweises? Sie verrät die Zahl unter der Wurzel.",
    "Aus √x = p/q folgt p² = x · q². Im Beweis steht p² = 3q², also ist x = 3. Der Beweis zeigt: √3 ist irrational. Bei √9 wäre der Satz unsinnig, denn √9 = 3 ist rational.",
    lambda: 3 * 1 == 3 and wz(9) == 3), g="umkehr", regel=HZ)
