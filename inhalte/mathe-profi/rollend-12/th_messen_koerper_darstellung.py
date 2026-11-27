T = "messen.koerper_darstellung"
HA, AQ = "id.flaeche_raum.haut", "id.flaeche_raum.aus_dem_quader"

# ───────── prisma ─────────
neu(T, "prisma", "bruecke", Z(
    "Die Tabelle zeigt, wie viele Kanten Prismen mit verschiedenen Grundflächen haben. Wie viele Kanten hat ein Prisma mit sechseckiger Grundfläche?",
    18, "3 * 6", "6 + 6 + 6", "Erkenne das Muster: Wie viele Kanten kommen jedes Mal dazu, wenn die Grundfläche eine Ecke mehr hat?",
    "Mit jeder zusätzlichen Ecke kommen 3 Kanten dazu (eine in der Grundfläche, eine in der Deckfläche, eine seitlich). 15 + 3 = 18. Auch: 3 · 6 = 18.",
    [(12, None, "nur die Kanten von Grund- und Deckfläche gezählt: 2 · 6", "2 * 6"), (21, None, "das Muster mit +6 statt +3 fortgesetzt", "15 + 6"), (24, None, "mit 4 · 6 gerechnet", "4 * 6")], "Kanten",
    grafik=TAB(["Grundfläche", "Kanten des Prismas"], ["Dreieck", "9"], ["Viereck", "12"], ["Fünfeck", "15"])))
neu(T, "prisma", "fehler_detektiv", FD(
    "Nico zählt die Flächen eines Prismas mit sechseckiger Grundfläche.",
    [("Das Prisma hat zwei Sechsecke als Grund- und Deckfläche.", True, True, "Zeile 1 stimmt: Grund- und Deckfläche sind zwei Sechsecke. Der Fehler steckt später."),
     ("Die Zahl der Seitenflächen ist doppelt so groß wie die Zahl der Ecken der Grundfläche: 2 · 6 = 12.", 2 * 6 == 6, True),
     ("Insgesamt hat das Prisma 2 + 12 = 14 Flächen.", 2 + 12 == 14, True, "Zeile 3 rechnet 2 + 12 = 14 für sich richtig, benutzt aber die falsche Zahl der Seitenflächen aus Zeile 2. Der Fehler liegt schon in Zeile 2.")],
    "Prüfe jede Zeile für sich und überlege, wie viele Seitenflächen zu den Seiten der Grundfläche gehören. Welche Zeile enthält zuerst einen Fehler?",
    "Zu jeder Seite der Grundfläche gehört eine Seitenfläche, hier also 6. Insgesamt: 2 + 6 = 8 Flächen. Der erste Fehler steht in Zeile 2."))

# ───────── netz ─────────
neu(T, "netz", "anwenden", Z(
    "Eine Würfelschachtel hat die Kantenlänge 5 cm. Sie wird aus einem Netz gefaltet. Wie viele cm² Pappe braucht man für das Netz, wenn man keine Klebelaschen rechnet?",
    150, "6 * (5 * 5)", "6 * 25", "Aus wie vielen Quadraten besteht das Netz eines Würfels? Wie groß ist jedes?",
    "Das Netz besteht aus 6 Quadraten. Jedes hat 5 · 5 = 25 cm². 6 · 25 cm² = 150 cm².",
    [(25, None, "nur ein Quadrat gerechnet", "5 * 5"), (75, "fb.haut.nur_drei_flaechen", "nur drei statt sechs Quadrate gezählt", "3 * 25"), (125, None, "das Volumen berechnet: 5 · 5 · 5", "5 * 5 * 5")], "cm²"), regel=HA)
neu(T, "netz", "zwei_wege", Z(
    "Ein Quader ist 5 cm lang, 4 cm breit und 3 cm hoch. Weg A: Berechne alle sechs Rechtecke einzeln und addiere. Weg B: Berechne die beiden Grundflächen (5 cm × 4 cm) und dazu ein langes Rechteck, dessen Länge der Umfang der Grundfläche und dessen Höhe 3 cm ist. Wie groß ist die Oberfläche seines Netzes?",
    94, "2 * (5 * 4) + 2 * (5 + 4) * 3", "5 * 4 + 5 * 4 + 5 * 3 + 5 * 3 + 4 * 3 + 4 * 3", "Bei Weg B: Wie groß ist der Umfang der Grundfläche 5 cm × 4 cm?",
    "Weg A: 20 + 20 + 15 + 15 + 12 + 12 = 94 cm². Weg B: Zwei Grundflächen 2 · 20 = 40 cm². Umfang der Grundfläche 2 · (5 + 4) = 18 cm, langes Rechteck 18 · 3 = 54 cm². 40 + 54 = 94 cm².",
    [(47, "fb.haut.nur_drei_flaechen", "nur drei statt sechs Rechtecke gezählt", "20 + 15 + 12"), (60, None, "das Volumen berechnet", "5 * 4 * 3")], "cm²"), g="verknuepfen", regel=HA)

# ───────── zylinder ─────────
neu(T, "zylinder", "bruecke", Z(
    "Im Netz eines Zylinders ist das Mantelrechteck 37,68 cm lang und 10 cm hoch. Rechne mit π ≈ 3,14. Wie groß ist der Radius des Grundkreises?",
    6, "37.68 / (2 * 3.14)", "37.68 / 3.14 / 2", "Die Länge des Mantelrechtecks ist genauso lang wie ein Umfang. Welcher Kreis hat diesen Umfang?",
    "Die Länge des Mantelrechtecks ist der Umfang des Grundkreises: u = 37,68 cm. Aus u = 2 · π · r folgt r = 37,68 : (2 · 3,14) = 37,68 : 6,28 = 6 cm.",
    [(12, None, "den Durchmesser statt des Radius angegeben: 37,68 : 3,14", "37.68 / 3.14"), (18.84, None, "den Umfang nur halbiert", "37.68 / 2"), (3.768, None, "durch die Höhe 10 geteilt", "37.68 / 10")], "cm"), regel=HA)
neu(T, "zylinder", "fehler_detektiv", FD(
    "Ein Zylinder hat den Radius 3 cm und die Höhe 10 cm. Tim berechnet die Mantelfläche mit π ≈ 3,14.",
    [("Der Umfang des Grundkreises ist u = 3,14 · 3 = 9,42 cm.", round(3.14 * 3, 2) == round(2 * 3.14 * 3, 2), True),
     ("Die Mantelfläche ist u · h = 9,42 · 10 = 94,2 cm².", round(9.42 * 10, 2) == 94.2, True, "Zeile 2 rechnet 9,42 · 10 = 94,2 für sich richtig, benutzt aber den falschen Umfang aus Zeile 1. Der Fehler liegt schon in Zeile 1."),
     ("Der Mantel des Zylinders hat also etwa 94,2 cm².", True, True, "Zeile 3 übernimmt nur das Ergebnis aus Zeile 2. Der Fehler liegt schon in Zeile 1.")],
    "Prüfe jede Zeile für sich und vergleiche mit der Formel für den Kreisumfang. Welche Zeile enthält zuerst einen Fehler?",
    "Der Umfang ist u = 2 · π · r = 2 · 3,14 · 3 = 18,84 cm. Die Mantelfläche ist 18,84 · 10 = 188,4 cm². Der erste Fehler steht in Zeile 1."), regel=HA)

# ───────── schraegbild ─────────
neu(T, "schraegbild", "umkehren", Z(
    "Die Tiefe eines Quaders wird im Schrägbild (q = 1/2) mit 3,5 cm gezeichnet. Wie tief ist der Quader in Wirklichkeit?",
    7, "3.5 * 2", "3.5 / (1 / 2)", "Beim Schrägbild werden die nach hinten laufenden Kanten auf die Hälfte verkürzt. Mache das rückgängig.",
    "Die gezeichnete Länge ist die Hälfte der wirklichen: 3,5 cm = 1/2 · wirkliche Tiefe. Wirkliche Tiefe: 3,5 · 2 = 7 cm.",
    [(1.75, None, "noch einmal halbiert", "3.5 / 2"), (3.5, None, "die gezeichnete Länge ohne Umrechnung übernommen", "3.5"), (10.5, None, "mit 3 malgenommen", "3.5 * 3")], "cm"), g="umkehr", regel=HA)
neu(T, "schraegbild", "fehler_detektiv", FD(
    "Ein Quader ist 8 cm lang, 4 cm hoch und 6 cm tief. Lena zeichnet ein Schrägbild mit q = 1/2.",
    [("Die Vorderseite (8 cm × 4 cm) wird unverändert gezeichnet.", True, True, "Zeile 1 stimmt: Die Vorderseite liegt in der Zeichenebene und wird in wahrer Größe gezeichnet. Der Fehler steckt später."),
     ("Die nach hinten laufenden Kanten werden mit q = 1/2 verkürzt: 6 · 2 = 12 cm.", 6 * 0.5 == 6 * 2, True),
     ("Die schrägen Kanten werden also 12 cm lang gezeichnet.", True, True, "Zeile 3 übernimmt nur das Ergebnis aus Zeile 2. Der Fehler liegt schon in Zeile 2.")],
    "Prüfe jede Zeile für sich und frage, ob die Rechnung zum Verkürzen passt. Welche Zeile enthält zuerst einen Fehler?",
    "Mit q = 1/2 wird die Tiefe halbiert: 6 · 1/2 = 3 cm. Die schrägen Kanten sind 3 cm lang. Der erste Fehler steht in Zeile 2."), regel=HA)

# ───────── ansichten ─────────
neu(T, "ansichten", "bruecke", Z(
    "Die Tabelle nennt für vier Körper die Vorderansicht und die Draufsicht. Bei wie vielen der vier Körper sind beide Ansichten dieselbe Art von Figur (zum Beispiel beide Rechtecke)?",
    2, "1 + 1", "2", "Vergleiche in jeder Zeile die beiden Figuren.",
    "Zylinder: Rechteck und Kreis (verschieden). Kegel: Dreieck und Kreis (verschieden). Quader: Rechteck und Rechteck (gleich). Würfel: Quadrat und Quadrat (gleich). Das sind 2 Körper.",
    [(1, None, "nur den Würfel gezählt", "1"), (4, None, "alle Körper gezählt", "2 + 2")], "Körper",
    grafik=TAB(["Körper", "Vorderansicht", "Draufsicht"], ["Zylinder", "Rechteck", "Kreis"], ["Kegel", "Dreieck", "Kreis"], ["Quader", "Rechteck", "Rechteck"], ["Würfel", "Quadrat", "Quadrat"])))
neu(T, "ansichten", "umkehren", W(
    "Ein Körper wird von vorn und von der Seite betrachtet. In beiden Fällen sieht man ein Dreieck. Von oben sieht man ein Quadrat. Welcher Körper ist es?",
    "Pyramide mit quadratischer Grundfläche",
    [("Kegel", "Von oben sieht ein Kegel wie ein Kreis aus."), ("Dreiecksprisma (liegend)", "Von oben sieht man ein Rechteck, von der Seite ein Rechteck."), ("Würfel", "Von vorn sieht man ein Quadrat.")],
    "Was verraten dir die Ansichten von vorn und von der Seite über die Form des Körpers nach oben? Und was die Ansicht von oben über die Grundfläche?",
    "Dreieck von vorn und von der Seite heißt: Der Körper läuft nach oben spitz zu. Das Quadrat von oben ist die Grundfläche. Das ist die Pyramide mit quadratischer Grundfläche.",
    lambda: [v == ("Dreieck", "Dreieck", "Quadrat") for v in (("Dreieck", "Dreieck", "Quadrat"), ("Dreieck", "Dreieck", "Kreis"), ("Dreieck", "Rechteck", "Rechteck"), ("Quadrat", "Quadrat", "Quadrat"))] == [True, False, False, False]), g="rueckwaerts")

# ───────── beurteilen ─────────
neu(T, "beurteilen", "zwei_wege", Z(
    "Jan behauptet: „Ein Würfel hat 6 Flächen mit je 4 Kanten, also 24 Kanten.“ Weg A: Zähle die Kanten oben, unten und die senkrechten Kanten. Weg B: Prüfe Jans Rechnung: Jede Kante gehört zu genau zwei Flächen. Gib die wirkliche Zahl der Kanten an.",
    12, "4 + 4 + 4", "6 * 4 / 2", "Jede Kante grenzt an zwei Flächen. Wie oft hat Jan jede Kante gezählt?",
    "Weg A: oben 4, unten 4, senkrecht 4: 4 + 4 + 4 = 12. Weg B: 6 · 4 = 24 Kanten gezählt, aber jede wurde zweimal gezählt: 24 : 2 = 12.",
    [(24, None, "jede Kante doppelt gezählt", "6 * 4"), (8, None, "die Zahl der Ecken genannt", "8"), (6, None, "die Zahl der Flächen genannt", "6")], "Kanten"))
neu(T, "beurteilen", "anwenden", Z(
    "Jan behauptet: „Für ein Kantenmodell aus genau 30 Holzstäben braucht man ein Prisma mit zwölfeckiger Grundfläche.“ Jeder Stab ist eine Kante, alle Stäbe werden gebraucht. Wie viele Ecken hat die Grundfläche des Prismas wirklich?",
    10, "30 / 3", "5 + 5", "Prüfe Jans Behauptung: Wie viele Kanten hat ein Prisma mit zwölfeckiger Grundfläche?",
    "Ein Prisma mit n-eckiger Grundfläche hat n Kanten in der Grundfläche, n in der Deckfläche und n Verbindungskanten, zusammen 3 · n. Bei n = 12 wären es 36 Kanten, nicht 30. Aus 3 · n = 30 folgt n = 10. Das Prisma hat eine zehneckige Grundfläche. Probe: 3 · 10 = 30.",
    [(15, None, "nur Grund- und Deckfläche gezählt: 30 : 2", "30 / 2"), (90, None, "mit 3 malgenommen statt durch 3 geteilt", "30 * 3"), (12, None, "Jans Zahl übernommen", "12")], "Ecken"), g="transfer")
