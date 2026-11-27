T = "bruch.prozent"
# ───────── prozent_bedeutung ─────────
neu(T, "prozent_bedeutung", "lueckenweg", L(
    "Schreibe 45 % als gekürzten Bruch. 45 % sind 45/100. Der ggT von 45 und 100 ist ①. Der Bruch ist dann ②/③.",
    KOMM(3), [5, 9, 20], ["5", "45 / {1}", "100 / {1}"], ["gcd(45, 100)", "9", "20"], "Prozent heißt „von hundert“.",
    "45 % = 45/100. Der ggT ist 5. 45 : 5 = 9 und 100 : 5 = 20. Also 45 % = 9/20.",
    {0: [(1, None, "nur durch 1 gekürzt, das ist nicht der größte gemeinsame Teiler", False)], 1: [(45, None, "den Zähler nicht gekürzt", "45 / 1")], 2: [(100, None, "den Nenner nicht gekürzt", "100 / 1")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.verhaeltnisse.prozent")
neu(T, "prozent_bedeutung", "bruecke", Z(
    "Ein Streifen besteht aus 40 gleich großen Kästchen. 14 Kästchen sind gefärbt. Wie viel Prozent des Streifens sind gefärbt?",
    35, "14 / 40 * 100", "14 * 2.5", "Wie viele Kästchen wären 100 Prozent? Rechne den Anteil in Hundertstel um.",
    "14 von 40 ist 14/40 = 35/100. Das sind 35 %. Probe: 1 % sind 0,4 Kästchen, 0,4 · 35 = 14.",
    [(0.35, None, "den Anteil als Dezimalzahl statt als Prozent angegeben", "14 / 40"), (65, None, "den Anteil der nicht gefärbten Kästchen berechnet", "(40 - 14) / 40 * 100")], "%"), regel="id.verhaeltnisse.prozent")
neu(T, "prozent_bedeutung", "fehler_detektiv", FD(
    "Aysel schreibt 0,6 % als Dezimalzahl.",
    [("0,6 % = 6/100", F(6, 1000) == F(6, 100)), ("6/100 = 0,06", F(6, 100) == F(6, 100)), ("Also ist 0,6 % = 0,06.", True)],
    "Wie viele Hundertstel sind 0,6 Hundertstel? Ein Prozent ist ein Hundertstel.", "0,6 % = 0,6/100 = 6/1000 = 0,006. In Zeile 1 steht 6/100, das wären 6 %. Die Zeilen 2 und 3 rechnen damit richtig weiter.", rueck={1: '6/100 = 0,06 ist für sich richtig. Der erste Fehler steht in Zeile 1, wo 0,6 % mit 6/100 gleichgesetzt wird.', 2: 'Diese Zeile übernimmt nur das Ergebnis aus Zeile 2. Der erste Fehler steht schon in Zeile 1.'}), regel="id.verhaeltnisse.prozent")

# ───────── prozentwert ─────────
neu(T, "prozentwert", "lueckenweg", L(
    "Berechne 15 % von 200 €. Ein Prozent sind ① €. 15 % sind ② €. Nach dem Abziehen dieser 15 % bleiben ③ €.",
    KOMM(3), [2, 30, 170], ["200 / 100", "{1} * 15", "200 - {2}"], ["2", "30", "170"], "Teile zuerst durch 100, um ein Prozent zu erhalten.",
    "200 € : 100 = 2 € ist ein Prozent. 15 · 2 € = 30 €. Es bleiben 200 € − 30 € = 170 €.",
    {0: [(20, None, "durch 10 statt durch 100 geteilt", "200 / 10")], 1: [(17, None, "15 addiert statt malgenommen", "{1} + 15")], 2: [(230, None, "addiert statt abgezogen", "200 + {2}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.verhaeltnisse.prozent")
neu(T, "prozentwert", "zwei_wege", Z(
    "Berechne 35 % von 80 m. Weg A: Rechne 35/100 · 80. Weg B: Zerlege 35 % in 10 % + 10 % + 10 % + 5 % und rechne mit 10 % = ein Zehntel. Wie viele Meter sind es?",
    28, "35 / 100 * 80", "3 * 8 + 4", "Beide Wege liefern dasselbe Ergebnis. Wie viel sind 10 % von 80 m?",
    "Weg A: 80 · 35 : 100 = 28. Weg B: 10 % = 8 m, drei mal 10 % = 24 m, 5 % = 4 m. 24 + 4 = 28 m.",
    [(2800, None, "80 · 35 gerechnet, nicht durch 100 geteilt", "35 * 80"), (45, None, "80 − 35 gerechnet", "80 - 35")], "m"), g="mehrschritt", regel="id.verhaeltnisse.prozent")
neu(T, "prozentwert", "anwenden", Z(
    "Ein Fahrrad kostet 420 €. Beim Kauf zahlt man 15 % Anzahlung. Der Rest wird in 6 gleich hohen Raten bezahlt. Wie hoch ist eine Rate in Euro?",
    59.5, "420 * (1 - 0.15) / 6", "357 / 6", "Wie viel Euro bleiben nach der Anzahlung?",
    "Anzahlung: 15 % von 420 € = 63 €. Rest: 420 € − 63 € = 357 €. Eine Rate: 357 € : 6 = 59,50 €.",
    [(63, None, "nur die Anzahlung angegeben", "420 * 0.15"), (70, None, "die Anzahlung vergessen: 420 : 6", "420 / 6"), (10.5, None, "nur die Anzahlung auf die Raten verteilt", "420 * 0.15 / 6")], "€"), g="transfer", regel="id.verhaeltnisse.prozent")

# ───────── prozentsatz ─────────
neu(T, "prozentsatz", "lueckenweg", L(
    "Von 25 Kindern haben 6 ein Haustier. Erweitere 6/25 auf den Nenner 100. Die Erweiterungszahl ist ①. Der neue Zähler ② ist der Prozentsatz. Die übrigen Kinder machen ③ % aus.",
    KOMM(3), [4, 24, 76], ["100 / 25", "6 * {1}", "100 - {2}"], ["4", "24", "76"], "Mit welcher Zahl wird aus 25 die 100?",
    "100 : 25 = 4. 6 · 4 = 24, also 24 %. Die übrigen Kinder: 100 % − 24 % = 76 %.",
    {0: [(75, None, "100 − 25 gerechnet", "100 - 25")], 1: [(10, None, "6 + 4 gerechnet statt 6 · 4", "6 + {1}")], 2: [(24, None, "den Prozentsatz der Haustierkinder noch einmal angegeben", "{2}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.verhaeltnisse.prozent")
neu(T, "prozentsatz", "anwenden", Z(
    "Ein Verein hat 240 Mitglieder. 54 davon sind jünger als 18 Jahre. Wie viel Prozent der Mitglieder sind jünger als 18 Jahre?",
    22.5, "54 / 240 * 100", "54 * 100 / 240", "Teil durch Ganzes, dann in Prozent umrechnen.",
    "54/240 = 0,225 = 22,5/100. Das sind 22,5 %.",
    [(0.225, None, "den Anteil nicht in Prozent umgerechnet", "54 / 240"), (186, None, "die Zahl der übrigen Mitglieder angegeben", "240 - 54")], "%"), regel="id.verhaeltnisse.prozent")
neu(T, "prozentsatz", "umkehren", Z(
    "Der Preis einer Jacke wird von 80 € auf 100 € erhöht. Um wie viel Prozent muss der neue Preis gesenkt werden, damit die Jacke wieder 80 € kostet?",
    20, "(100 - 80) / 100 * 100", "20 / 100 * 100", "Auf welchen Preis beziehen sich die Prozent bei der Senkung?",
    "Die Senkung beträgt 20 €. Sie bezieht sich auf den neuen Preis 100 €: 20/100 = 20 %.",
    [(25, None, "die 20 € auf den alten Preis 80 € bezogen", "(100 - 80) / 80 * 100"), (0.2, None, "nicht in Prozent umgerechnet", "20 / 100")], "%"), g="rueckwaerts", regel="id.verhaeltnisse.prozent")

# ───────── grundwert ─────────
neu(T, "grundwert", "lueckenweg", L(
    "15 % einer Summe sind 45 €. Dann sind 1 % genau ① €. Die ganze Summe ist ② €. Zur Probe: 10 % der Summe sind ③ €.",
    KOMM(3), [3, 300, 30], ["45 / 15", "{1} * 100", "{2} / 10"], ["3", "300", "30"], "Rechne zuerst auf ein Prozent zurück.",
    "45 € : 15 = 3 € sind 1 %. Das Ganze: 100 · 3 € = 300 €. 10 % davon sind 30 €.",
    {0: [(675, None, "45 mit 15 malgenommen", "45 * 15")], 1: [(103, None, "100 dazugezählt statt malgenommen", "{1} + 100")], 2: [(3000, None, "mit 10 malgenommen statt geteilt", "{2} * 10")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.verhaeltnisse.prozent")
neu(T, "grundwert", "verfahren_waehlen", W(
    "Du weißt: 18 % einer Größe sind 72. Mit welcher Rechnung findest du die ganze Größe?",
    "72 : 18 · 100",
    [("72 · 18 : 100", "den Prozentwert berechnet, als wären 72 der Grundwert"), ("72 · 18", "die Zahlen einfach malgenommen"), ("72 − 18", "die Zahlen voneinander abgezogen")],
    "Erst herausfinden, wie viel ein Prozent ist.",
    "72 : 18 = 4 sind 1 %. Das Ganze sind 100 %: 4 · 100 = 400. Rechnung: 72 : 18 · 100.",
    lambda: F(72, 18) * 100 == 400 and len({F(72, 18) * 100, F(72 * 18, 100), 72 * 18, 72 - 18}) == 4), g="mehrschritt", regel="id.verhaeltnisse.prozent")
neu(T, "grundwert", "anwenden", Z(
    "Ein Händler verkauft ein Spiel mit 8 % Gewinn für 135 €. Das ist der Einkaufspreis plus 8 % davon. Wie viel Euro hat das Spiel im Einkauf gekostet?",
    125, "135 / 1.08", "135 / 108 * 100", "135 € sind wie viel Prozent des Einkaufspreises?",
    "Der Verkaufspreis ist 108 % des Einkaufspreises. 135 € : 108 = 1,25 € sind 1 %. 100 % sind 125 €. Probe: 125 € + 10 € = 135 €.",
    [(145.8, None, "8 % auf 135 € aufgeschlagen", "135 * 1.08"), (124.2, None, "8 % von 135 € abgezogen", "135 - 135 * 0.08")], "€"), g="transfer", regel="id.verhaeltnisse.prozent")

# ───────── rabatt_aufschlag ─────────
neu(T, "rabatt_aufschlag", "lueckenweg", L(
    "Ein Pullover kostet 80 €. Der Preis steigt um 15 %: Der Aufschlag beträgt ① €, der neue Preis ② €. Danach gibt es 25 % Rabatt auf den neuen Preis. Der Preis ist dann ③ €.",
    KOMM(3), [12, 92, 69], ["80 * 15 / 100", "80 + {1}", "{2} * 75 / 100"], ["12", "92", "69"], "Der Aufschlag ist ein Prozentwert vom alten Preis.",
    "15 % von 80 € = 12 €. Neuer Preis: 92 €. 25 % Rabatt heißt: 75 % bleiben. 75 % von 92 € = 69 €.",
    {0: [(1200, None, "80 · 15 gerechnet, nicht durch 100 geteilt", "80 * 15")], 1: [(68, None, "abgezogen statt addiert", "80 - {1}")], 2: [(23, None, "den Rabattbetrag statt des Preises angegeben", "{2} * 25 / 100")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.verhaeltnisse.prozent")
neu(T, "rabatt_aufschlag", "zwei_wege", Z(
    "Ein Mantel kostet 150 €. Es gibt 30 % Rabatt. Weg A: Berechne den Rabatt in Euro und ziehe ihn ab. Weg B: Berechne direkt, wie viel Prozent des Preises noch zu zahlen sind. Was kostet der Mantel jetzt?",
    105, "150 - 150 * 0.3", "150 * 0.7", "Beide Wege liefern denselben Preis.",
    "Weg A: 30 % von 150 € = 45 €. 150 € − 45 € = 105 €. Weg B: 100 % − 30 % = 70 %. 70 % von 150 € = 105 €.",
    [(45, None, "nur den Rabatt angegeben", "150 * 0.3"), (195, None, "den Rabatt aufgeschlagen", "150 + 150 * 0.3")], "€"), g="mehrschritt", regel="id.verhaeltnisse.prozent")
neu(T, "rabatt_aufschlag", "umkehren", Z(
    "Ein Fahrrad kostet nach einem Rabatt von 20 % noch 280 €. Wie viel Euro hat es vor dem Rabatt gekostet?",
    350, "280 / 0.8", "280 / 80 * 100", "280 € sind wie viel Prozent des ursprünglichen Preises?",
    "Nach 20 % Rabatt sind noch 80 % zu zahlen. 280 € : 80 = 3,50 € sind 1 %. 100 % sind 350 €. Probe: 20 % von 350 € = 70 €, 350 € − 70 € = 280 €.",
    [(336, None, "20 % auf 280 € aufgeschlagen", "280 * 1.2"), (224, None, "20 % von 280 € abgezogen", "280 * 0.8")], "€"), g="rueckwaerts", regel="id.verhaeltnisse.prozent")

# ───────── verstehen ─────────
neu(T, "verstehen", "lueckenweg", L(
    "Ein Preis von 100 € steigt um 10 %. Danach sinkt der neue Preis um 10 %. Nach der Erhöhung beträgt der Preis ① €. Nach der Senkung beträgt er ② €. Er liegt dann ③ € unter dem Startpreis.",
    KOMM(3), [110, 99, 1], ["100 * 1.1", "{1} * 0.9", "100 - {2}"], ["110", "99", "1"], "Die zweiten 10 % beziehen sich auf den neuen Preis.",
    "Nach +10 %: 110 €. 10 % von 110 € sind 11 €. 110 € − 11 € = 99 €. Das sind 1 € weniger als am Anfang.",
    {0: [(10, None, "nur den Aufschlag angegeben", "100 * 0.1")], 1: [(100, None, "gedacht, plus und minus 10 % heben sich auf", "100")], 2: [(0, None, "mit 0 € Unterschied gerechnet", "100 - 100")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.verhaeltnisse.prozent")
neu(T, "verstehen", "bruecke", Z(
    "In einem Kreisdiagramm gehört zu 40 % der Gäste der Kuchen. Max sagt: „Der Kreisausschnitt dafür hat 140°.“ Der ganze Kreis hat 360°. Um wie viel Grad ist Max' Angabe zu klein?",
    4, "40 / 100 * 360 - 140", "360 / 100 * 40 - 140", "100 % entsprechen dem ganzen Kreis. Berechne zuerst den richtigen Winkel.",
    "1 % entspricht 3,6°. 40 · 3,6° = 144°. Max' 140° sind 4° zu wenig.",
    [(144, None, "nur den richtigen Winkel angegeben, nicht den Unterschied", "40 / 100 * 360"), (140, None, "Max' Winkel selbst als Unterschied genannt", "140")], "°"), regel="id.verhaeltnisse.prozent")
neu(T, "verstehen", "fehler_detektiv", FD(
    "Mara behauptet: „Steigt ein Preis um 20 % und sinkt danach um 20 %, ist er wieder so hoch wie am Anfang.“ Sie rechnet mit 50 €.",
    [("Erhöhung: 50 · 1,2 = 60 €", 50 * 1.2 == 60), ("Senkung: 60 · 0,8 = 48 €", abs(60 * 0.8 - 48) < 1e-9), ("Also 48 € = 50 €, der Preis ist wieder gleich.", 48 == 50)],
    "Vergleiche die beiden letzten Preise.", "Die zwei Rechnungen stimmen, aber 48 € sind nicht 50 €. Die 20 % der Senkung beziehen sich auf den neuen Preis 60 €, nicht auf 50 €. Der Preis liegt am Ende 2 € unter dem Start.", rueck={}), regel="id.verhaeltnisse.prozent")
