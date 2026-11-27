T = "bruch.dezimal"
H4 = "Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt."
# ───────── stellenwerte ─────────
neu(T, "stellenwerte", "lueckenweg", L(
    "Die Zahl hat 6 Einer, 2 Zehntel und 15 Tausendstel. Bündele die 15 Tausendstel: Das sind ① Hundertstel und ② Tausendstel. Schreibst du die Zahl als Dezimalzahl und lässt das Komma weg, entsteht die ganze Zahl ③. Auf Hundertstel gerundet sind es ④ Hundertstel.",
    KOMM(4), [1, 5, 6215, 622], ["15 // 10", "15 % 10", "(6 + 2/10 + {1}/100 + {2}/1000) * 1000", "({3} + 5) // 10"], ["1", "5", "6215", "622"],
    "Zehn Tausendstel sind ein Hundertstel.",
    "15 Tausendstel = 1 Hundertstel und 5 Tausendstel. Die Zahl ist 6,215. Ohne Komma: 6215. Auf Hundertstel gerundet: 6,22, das sind 622 Hundertstel.",
    {0: [(15, None, "nicht gebündelt: 15 als Hundertstel genommen", "15")], 1: [(14, None, "beim Bündeln nur 1 statt 10 Tausendstel abgezogen", "15 - {1}")],
     2: [(6251, None, "Hundertstel- und Tausendstelziffer vertauscht: 6,251", "(6 + 2/10 + {2}/100 + {1}/1000) * 1000")],
     3: [(621, None, "abgerundet statt aufgerundet", "{3} // 10")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.stellenwert")
neu(T, "stellenwerte", "anwenden", Z(
    "Die Stoppuhr zeigt 12,07 Sekunden. Wie viele Hundertstelsekunden sind das?",
    1207, "12.07 * 100", "12 * 100 + 7", "Wie viele Hundertstel passen in eine ganze Sekunde?",
    "Eine Sekunde hat 100 Hundertstelsekunden. 12 · 100 = 1200, dazu 7: 1207 Hundertstelsekunden.",
    [(120.7, None, "mit 10 statt mit 100 malgenommen", "12.07 * 10"), (12070, None, "mit 1000 malgenommen", "12.07 * 1000")], "Hundertstelsekunden"), regel="rr.stellenwert")
neu(T, "stellenwerte", "fehler_detektiv", FD(
    "Jonas schreibt „3 Zehntel und 5 Hundertstel“ als Dezimalzahl.",
    [("3 Zehntel = 0,3", F(3, 10) == F(3, 10)), ("5 Hundertstel = 0,5", F(5, 100) == F(5, 10)), ("0,3 + 0,5 = 0,8", F(3, 10) + F(5, 10) == F(8, 10))],
    "Welche Stelle hinter dem Komma gehört zu den Hundertsteln?", "5 Hundertstel sind 0,05. Zusammen: 0,3 + 0,05 = 0,35. In Zeile 2 steht die 5 an der Zehntelstelle. Zeile 3 rechnet damit richtig weiter."), regel="rr.stellenwert")

# ───────── vergleichen_ordnen ─────────
neu(T, "vergleichen_ordnen", "lueckenweg", L(
    "Vergleiche 0,45 und 0,5 als Tausendstel. 0,45 sind ① Tausendstel. 0,5 sind ② Tausendstel. Die größere Zahl ist um ③ Tausendstel größer. Der Unterschied sind ④ Hundertstel.",
    KOMM(4), [450, 500, 50, 5], ["0.45 * 1000", "0.5 * 1000", "{2} - {1}", "{3} / 10"], ["450", "500", "50", "5"], "Wie viele Tausendstel sind ein Zehntel, wie viele ein Hundertstel?",
    "0,45 = 450/1000 und 0,5 = 500/1000. 500 − 450 = 50. Also ist 0,5 größer als 0,45, um 50 Tausendstel. 50 Tausendstel sind 5 Hundertstel.",
    {0: [(45, None, "als Hundertstel statt Tausendstel gezählt", "0.45 * 100")], 1: [(5, None, "als Zehntel statt Tausendstel gezählt", "0.5 * 10")], 2: [(950, None, "die Tausendstel addiert statt abgezogen", "{1} + {2}")],
     3: [(500, None, "mit 10 malgenommen statt durch 10 geteilt", "{3} * 10")]},
    hinweis="Je Lücke eine ganze Zahl."), regel="rr.stellenwert")
neu(T, "vergleichen_ordnen", "verfahren_waehlen", W(
    "Du vergleichst 0,8 und 0,75. Welche Überlegung ist richtig?",
    "0,8 = 0,80. 80 Hundertstel sind mehr als 75 Hundertstel, also ist 0,8 größer.",
    [("75 ist größer als 8, also ist 0,75 größer.", "wie ganze Zahlen verglichen: 75 gegen 8"),
     ("0,8 hat weniger Ziffern, also ist es kleiner.", "die Zahl der Ziffern verglichen"),
     ("Beide sind gleich groß, weil man hinten Nullen anhängen darf.", "aus dem Anhängen von Nullen (0,8 = 0,80) gefolgert, dass auch 0,75 gleich groß ist")],
    "Schreibe beide Zahlen mit gleich vielen Nachkommastellen.",
    "Gleiche Stellenzahl: 0,8 = 0,80 und 0,75. Es ist 80 > 75, also 0,8 > 0,75. Die Länge der Ziffernfolge sagt nichts über die Größe.",
    lambda: F(8, 10) > F(75, 100)), g="mehrschritt", regel="rr.stellenwert")
neu(T, "vergleichen_ordnen", "anwenden", Z(
    "Drei Papierflieger fliegen 4,35 m, 4,5 m und 4,305 m weit. Um wie viele Zentimeter ist der weiteste Flug weiter als der kürzeste?",
    19.5, "(4.5 - 4.305) * 100", "450 - 430.5", "Welcher Sprung ist der weiteste, welcher der kürzeste? Schreibe die Zahlen mit gleich vielen Stellen.",
    "Mit drei Nachkommastellen: 4,350 m, 4,500 m, 4,305 m. Weitester: 4,5 m, kürzester: 4,305 m. Unterschied 0,195 m = 19,5 cm.",
    [(15, None, "den weitesten mit dem mittleren statt mit dem kürzesten Flug verglichen", "(4.5 - 4.35) * 100"), (0.195, None, "in Metern angegeben statt in Zentimetern", "4.5 - 4.305")], "cm"), g="transfer", regel="rr.stellenwert")

# ───────── runden ─────────
neu(T, "runden", "lueckenweg", L(
    "Runde 4,3652 auf Hundertstel. Die Ziffer an der Tausendstelstelle ist ①. Gerundet sind es ② Hundertstel. Die Rundung ändert die Zahl um ③ Zehntausendstel.",
    KOMM(3), [5, 437, 48], ["(43652 // 10) % 10", "436 + {1} // 5", "{2} * 100 - 43652"], ["5", "437", "48"], "Über die Rundung entscheidet die Ziffer direkt hinter der Rundungsstelle.",
    "An der Tausendstelstelle steht 5, es wird aufgerundet: 4,37 sind 437 Hundertstel. 4,37 − 4,3652 = 0,0048, das sind 48 Zehntausendstel.",
    {0: [(6, None, "die Hundertstelziffer statt der Tausendstelziffer genommen", "(43652 // 100) % 10")], 1: [(436, None, "abgerundet statt aufgerundet", "43652 // 100")],
     2: [(52, None, "nach dem Abrunden gerechnet: 4,3652 − 4,36", "43652 - 436 * 100")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.zahlen.buendeln")
neu(T, "runden", "anwenden", Z(
    "Beim Tanken kommen 38,45 Liter in den Tank. Ein Liter kostet 1,759 €. Berechne den Preis und runde auf ganze Cent. Wie viel Euro zahlst du?",
    67.63, "round(38.45 * 1.759, 2)", "round(67.63355, 2)", "Rechne zuerst genau und runde erst am Ende.",
    "38,45 · 1,759 = 67,63355. Auf Cent gerundet: 67,63 €, denn die dritte Nachkommastelle ist 3.",
    [(67.64, None, "aufgerundet statt gerundet", "67.64"), (67.6, None, "nur auf Zehntel gerundet", "round(38.45 * 1.759, 1)")], "€"), regel="id.zahlen.buendeln")
neu(T, "runden", "fehler_detektiv", FD(
    "Mira rundet 3,7449 auf Hundertstel.",
    [("Die Ziffer an der Tausendstelstelle ist 4.", (37449 // 10) % 10 == 4), ("4 ist kleiner als 5, also wird abgerundet.", 4 < 5), ("3,7449 ≈ 3,75", round(3.7449, 2) == 3.75)],
    "Prüfe die Rundung noch einmal mit der Zahl.", "Es wird abgerundet, die Hundertstelziffer bleibt 4: 3,7449 ≈ 3,74. In Zeile 3 steht das Aufrunden trotz richtiger Regel."), regel="id.zahlen.buendeln")

# ───────── bruch_zu_dezimal ─────────
neu(T, "bruch_zu_dezimal", "lueckenweg", L(
    "Schreibe 7/8 als Dezimalzahl. Erweitere auf den Nenner 1000. Die Erweiterungszahl ist ①. Der neue Zähler ist ②. Er gibt die Tausendstel an. Auf Hundertstel gerundet sind es ③ Hundertstel.",
    KOMM(3), [125, 875, 88], ["1000 / 8", "7 * {1}", "({2} + 5) // 10"], ["125", "875", "88"], "Mit welcher Zahl wird aus 8 die 1000?",
    "1000 : 8 = 125. 7 · 125 = 875. Also 7/8 = 875/1000 = 0,875. Auf Hundertstel gerundet: 0,88, das sind 88 Hundertstel.",
    {0: [(992, None, "1000 − 8 gerechnet", "1000 - 8")], 1: [(132, None, "den Zähler addiert statt malgenommen", "7 + {1}")], 2: [(87, None, "abgerundet statt aufgerundet", "{2} // 10")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.zahlen.schreibweisen")
neu(T, "bruch_zu_dezimal", "zwei_wege", Z(
    "Wie viele Zehntausendstel sind 7/16? Weg A: Teile 7 durch 16 schriftlich und lies die Dezimalzahl ab. Weg B: Erweitere 7/16 auf den Nenner 10 000.",
    4375, "7 * 625", "7 / 16 * 10000", "Beide Wege liefern dieselbe Zahl. Mit welcher Zahl wird 16 zu 10 000?",
    "Weg A: 7 : 16 = 0,4375, das sind 4375 Zehntausendstel. Weg B: 10 000 : 16 = 625 und 7 · 625 = 4375. Also 7/16 = 4375/10 000.",
    [(437.5, None, "als Tausendstel statt als Zehntausendstel gezählt", "7 / 16 * 1000"), (625, None, "nur die Erweiterungszahl angegeben", "10000 / 16")]), g="mehrschritt", regel="id.zahlen.schreibweisen")
neu(T, "bruch_zu_dezimal", "umkehren", Z(
    "Der Bruch ?/16 hat den Wert 0,6875. Welche Zahl steht an der Stelle des Fragezeichens?",
    11, "0.6875 * 16", "6875 * 16 / 10000", "Mit welcher Zahl muss man den Wert malnehmen, um den Zähler zu erhalten?",
    "Zähler : 16 = 0,6875. Also ist der Zähler 0,6875 · 16 = 11. Probe: 11 : 16 = 0,6875.",
    [(15.3125, None, "16 − 0,6875 gerechnet", "16 - 0.6875"), (0.04296875, None, "0,6875 durch 16 geteilt", "0.6875 / 16")]), g="rueckwaerts", regel="id.zahlen.schreibweisen")

# ───────── dezimal_zu_bruch ─────────
neu(T, "dezimal_zu_bruch", "lueckenweg", L(
    "Schreibe 0,36 als vollständig gekürzten Bruch. Zuerst 36/100. Der ggT von 36 und 100 ist ①. Gekürzt ist der Bruch ②/③.",
    KOMM(3), [4, 9, 25], ["4", "36 / {1}", "100 / {1}"], ["gcd(36, 100)", "9", "25"], "Welche größte Zahl steckt in 36 und in 100?",
    "36/100: der ggT ist 4. 36 : 4 = 9 und 100 : 4 = 25. Also 0,36 = 9/25.",
    {0: [(2, None, "nur einen gemeinsamen Teiler genommen, nicht den größten", False)], 1: [(18, None, "nur durch 2 gekürzt", "36 / 2")], 2: [(50, None, "nur durch 2 gekürzt", "100 / 2")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.kuerzen")
neu(T, "dezimal_zu_bruch", "bruecke", L(
    "Auf einem Messbecher steht 0,125 Liter. Schreibe 0,125 als vollständig gekürzten Bruch.",
    "□/□", [1, 8], ["125 / 125", "1000 / 125"], ["1", "8"], "0,125 sind 125 Tausendstel. Kürze mit dem ggT von 125 und 1000.",
    "0,125 = 125/1000. Der ggT ist 125. 125 : 125 = 1 und 1000 : 125 = 8. Also 0,125 = 1/8.",
    {0: [(125, None, "den Zähler nicht gekürzt", "125 / 1")], 1: [(1000, None, "den Nenner nicht gekürzt", "1000 / 1")]}, hinweis=H4), regel="id.zahlen.schreibweisen")
neu(T, "dezimal_zu_bruch", "fehler_detektiv", FD(
    "Peter schreibt 0,045 als Bruch.",
    [("0,045 hat drei Nachkommastellen, also ist der Nenner 1000.", True), ("0,045 = 45/100", F(45, 100) == F(45, 1000)), ("45/100 = 9/20", F(45, 100) == F(9, 20))],
    "Wie viele Stellen hat 0,045 hinter dem Komma?", "0,045 = 45/1000 = 9/200. In Zeile 2 steht der Nenner 100 statt 1000, obwohl Zeile 1 es richtig sagt. Zeile 3 kürzt 45/100 richtig."), regel="id.zahlen.schreibweisen")

# ───────── merkwerte ─────────
neu(T, "merkwerte", "lueckenweg", L(
    "Du weißt: 1/5 = 0,2. Also sind 3/5 genau ① Zehntel und 4/5 genau ② Zehntel. Zusammen sind 3/5 + 4/5 genau ③ Zehntel. Als Hundertstel sind das ④ Hundertstel.",
    KOMM(4), [6, 8, 14, 140], ["3 * 2", "4 * 2", "{1} + {2}", "{3} * 10"], ["6", "8", "14", "140"], "Ein Fünftel sind zwei Zehntel.",
    "3/5 = 3 · 0,2 = 0,6, das sind 6 Zehntel. 4/5 sind 8 Zehntel. Zusammen 14 Zehntel, also 1,4. Das sind 140 Hundertstel.",
    {0: [(3, None, "den Zähler als Zehntel genommen", "3")], 1: [(4, None, "den Zähler als Zehntel genommen", "4")], 2: [(48, None, "die Zehntel malgenommen statt addiert", "{1} * {2}")],
     3: [(14, None, "Zehntel nicht in Hundertstel umgerechnet", "{3}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.zahlen.schreibweisen")
neu(T, "merkwerte", "bruecke", Z(
    "Wie viele Tausendstel ist 5/8 größer als 0,62? Rechne 5/8 als Dezimalzahl und vergleiche.",
    5, "5/8 * 1000 - 0.62 * 1000", "625 - 620", "Merke dir 1/8 = 0,125.",
    "5/8 = 5 · 0,125 = 0,625. 0,625 − 0,62 = 0,005, das sind 5 Tausendstel.",
    [(0.005, None, "den Unterschied als Dezimalzahl statt als Tausendstel angegeben", "5/8 - 0.62"), (620, None, "nur 0,62 in Tausendstel angegeben", "0.62 * 1000")]), regel="id.zahlen.schreibweisen")
neu(T, "merkwerte", "zwei_wege", Z(
    "Berechne 0,375 · 48 auf zwei Wegen. Weg A: Multipliziere 0,375 mit 48. Weg B: Nimm 3/8 von 48.",
    18, "0.375 * 48", "48 / 8 * 3", "Beide Wege führen zum selben Ergebnis. Wie viele sind ein Achtel von 48?",
    "Weg A: 0,375 · 48 = 18. Weg B: 0,375 = 3/8. 48 : 8 = 6 und 3 · 6 = 18.",
    [(144, None, "48 mit 3 malgenommen", "48 * 3"), (6, None, "nur ein Achtel berechnet", "48 / 8")]), g="verknuepfen", regel="id.zahlen.schreibweisen")

# ───────── periodisch ─────────
neu(T, "periodisch", "lueckenweg", L(
    "Rechne 5 : 6. Nach dem Komma steht zuerst die Ziffer ①. Danach wiederholt sich immer dieselbe Ziffer ②. Auf Hundertstel gerundet sind das ③ Hundertstel. Auf Tausendstel gerundet sind das ④ Tausendstel.",
    KOMM(4), [8, 3, 83, 833], ["50 // 6", "(50 % 6) * 10 // 6", "{1} * 10 + {2} + {2} // 5", "{1} * 100 + {2} * 10 + {2} + {2} // 5"], ["8", "3", "83", "833"], "Teile 50 durch 6 und achte auf den Rest.",
    "5 : 6 = 0,8333… Die 8 steht einmal, dann wiederholt sich die 3. Gerundet auf Hundertstel: 0,83, das sind 83 Hundertstel (die nächste Ziffer 3 rundet ab). Auf Tausendstel: 0,833, das sind 833 Tausendstel.",
    {0: [(5, None, "den Zähler als erste Nachkommaziffer genommen", "5")], 1: [(8, None, "die erste Ziffer als Periode genommen", "{1}")],
     2: [(84, None, "aufgerundet, obwohl die nächste Ziffer 3 ist", "{1} * 10 + {2} + 1")], 3: [(834, None, "aufgerundet, obwohl die nächste Ziffer 3 ist", "{1} * 100 + {2} * 10 + {2} + 1")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.zahlen.schreibweisen")
neu(T, "periodisch", "bruecke", Z(
    "Die Dezimalzahl 0,272727… (die Ziffern 27 wiederholen sich) ist gleich ?/11. Welche Zahl steht im Zähler?",
    3, "27 / 99 * 11", "3", "Teile für kleine Zähler Z : 11 schriftlich und vergleiche mit 0,2727…",
    "3 : 11 = 0,272727… Also ist 0,272727… = 3/11. Der Zähler ist 3.",
    [(27, None, "die Periode als Zähler genommen", "27"), (9, None, "9 : 11 gerechnet, das ergibt 0,8181…", "9")]), regel="id.zahlen.schreibweisen")
neu(T, "periodisch", "fehler_detektiv", FD(
    "Mia will wissen, ob 7/20 endlich oder periodisch ist.",
    [("Der Nenner ist 20 = 2 · 2 · 3.", 2 * 2 * 3 == 20), ("Der Nenner hat den Primfaktor 3, der nicht in 10 steckt.", True), ("Also ist 7/20 eine periodische Dezimalzahl.", True)],
    "Zerlege 20 noch einmal in Primfaktoren.", "20 = 2 · 2 · 5. Der Nenner hat nur die Primfaktoren 2 und 5, also ist 7/20 = 0,35 endlich. In Zeile 1 steht 3 statt 5."), regel="id.zahlen.schreibweisen")

# ───────── verstehen ─────────
neu(T, "verstehen", "lueckenweg", L(
    "Die Zahl 0,06 sind 6 Hundertstel. In Tausendsteln sind das ① Tausendstel. Der Bruch ①/1000 wird vollständig gekürzt zu ②/③.",
    KOMM(3), [60, 3, 50], ["6 * 10", "{1} / 20", "1000 / ({1} / {2})"], ["60", "3", "50"], "Ein Hundertstel sind zehn Tausendstel.",
    "6 Hundertstel = 60 Tausendstel. 60/1000 wird durch 20 gekürzt: 3/50. Also 0,06 = 3/50.",
    {0: [(600, None, "mit 100 statt mit 10 malgenommen", "6 * 100")], 1: [(60, None, "nicht gekürzt", "{1} / 1")], 2: [(1000, None, "nicht gekürzt", "1000 / 1")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.stellenwert")
neu(T, "verstehen", "verfahren_waehlen", W(
    "Welche Aussage über 0,3 und 0,30 ist richtig?",
    "Sie sind gleich groß, denn 3 Zehntel sind 30 Hundertstel.",
    [("0,30 ist größer, weil die Zahl 30 größer ist als 3.", "wie ganze Zahlen verglichen"),
     ("0,3 ist größer, weil es weniger Stellen hat.", "die Zahl der Stellen verglichen"),
     ("Sie sind verschieden, weil die Schreibweise verschieden ist.", "Schreibweise mit dem Wert verwechselt")],
    "Wie viele Hundertstel sind drei Zehntel?",
    "Ein Zehntel sind 10 Hundertstel. 3 Zehntel sind 30 Hundertstel. Eine Null am Ende einer Dezimalzahl ändert den Wert nicht.",
    lambda: F(3, 10) == F(30, 100)), g="mehrschritt", regel="rr.stellenwert")
neu(T, "verstehen", "umkehren", Z(
    "Eine Dezimalzahl hat 3 Einer, 2 Zehntel und ? Hundertstel und keine weitere Stelle. Auf Zehntel gerundet ist sie 3,3. Welche ist die kleinste Ziffer, die an der Stelle des Fragezeichens stehen kann?",
    5, "10 / 2", "5", "Ab welcher Ziffer wird aufgerundet?",
    "Aufgerundet wird ab der Ziffer 5. 3,25 ≈ 3,3. Mit 4 würde abgerundet: 3,24 ≈ 3,2.",
    [(4, None, "4 gewählt: 3,24 rundet noch ab", "4"), (9, None, "die größte statt der kleinsten Ziffer genommen", "9")]), g="rueckwaerts", regel="rr.stellenwert")
