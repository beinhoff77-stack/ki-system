T = "messen.volumen"
# ───────── einheitswuerfel ─────────
neu(T, "einheitswuerfel", "lueckenweg", L(
    "Ein Quader ist aus Einheitswürfeln mit 1 cm Kante gebaut: 6 Würfel in der Länge, 4 in der Breite und 5 Schichten übereinander. Eine Schicht hat ① Würfel. Der ganze Quader hat ② Würfel. Nimmt man die oberste Schicht weg, bleiben ③ Würfel.",
    KOMM(3), [24, 120, 96], ["6 * 4", "{1} * 5", "{2} - {1}"], ["24", "120", "96"], "Zähle zuerst, wie viele Würfel in einer Schicht liegen.",
    "Eine Schicht: 6 · 4 = 24 Würfel. Fünf Schichten: 5 · 24 = 120 Würfel. Ohne die oberste Schicht: 120 − 24 = 96 Würfel.",
    {0: [(10, None, "6 + 4 gerechnet", "6 + 4")], 1: [(15, None, "alle Zahlen addiert: 6 + 4 + 5", "6 + 4 + 5")], 2: [(144, None, "addiert statt abgezogen", "{2} + {1}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "einheitswuerfel", "anwenden", Z(
    "Eine Kiste ist innen 40 cm lang, 30 cm breit und 20 cm hoch. Sie wird mit Würfeln gefüllt, die 10 cm Kantenlänge haben. Wie viele Würfel passen hinein?",
    24, "(40 / 10) * (30 / 10) * (20 / 10)", "4 * 3 * 2", "Wie viele Würfel passen in die Länge, in die Breite und in die Höhe?",
    "In die Länge passen 4 Würfel, in die Breite 3 und in die Höhe 2. 4 · 3 · 2 = 24 Würfel.",
    [(2400, None, "das Kistenvolumen nur durch 10 geteilt", "40 * 30 * 20 / 10"), (9, None, "4 + 3 + 2 gerechnet", "4 + 3 + 2")]), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "einheitswuerfel", "zwei_wege", Z(
    "Ein Quader ist 12 cm lang, 8 cm breit und 6 cm hoch. Er soll mit Würfeln der Kantenlänge 2 cm gefüllt werden. Weg A: Teile das Volumen des Quaders durch das Volumen eines kleinen Würfels. Weg B: Zähle, wie viele kleine Würfel an jeder Kante liegen, und multipliziere. Wie viele kleine Würfel sind es?",
    72, "12 * 8 * 6 / 8", "(12 / 2) * (8 / 2) * (6 / 2)", "Beide Wege müssen dieselbe Anzahl ergeben. Ein kleiner Würfel hat 2 · 2 · 2 cm³.",
    "Weg A: Quader 12 · 8 · 6 = 576 cm³. Ein Würfel 8 cm³. 576 : 8 = 72. Weg B: 6 · 4 · 3 = 72.",
    [(576, None, "nur das Volumen des Quaders in cm³ angegeben", "12 * 8 * 6"), (288, None, "durch die Kantenlänge 2 statt durch das Würfelvolumen 8 geteilt", "12 * 8 * 6 / 2")]), g="verknuepfen", regel="id.flaeche_raum.aus_dem_quader")

# ───────── quader ─────────
neu(T, "quader", "lueckenweg", L(
    "Ein Quader ist 8 cm lang, 5 cm breit und 6 cm hoch. Die Grundfläche ist ① cm². Das Volumen ist ② cm³. Wird der Quader 2 cm höher, wächst das Volumen auf ③ cm³.",
    KOMM(3), [40, 240, 320], ["8 * 5", "{1} * 6", "{2} + {1} * 2"], ["40", "240", "320"], "Volumen = Grundfläche mal Höhe.",
    "Grundfläche: 8 · 5 = 40 cm². Volumen: 40 · 6 = 240 cm³. Zwei Zentimeter mehr Höhe bringen 40 · 2 = 80 cm³ dazu: 320 cm³.",
    {0: [(13, None, "addiert statt malgenommen", "8 + 5")], 1: [(19, None, "alle Maße addiert", "8 + 5 + 6")], 2: [(480, None, "das Volumen verdoppelt statt 2 cm Höhe dazuzurechnen", "{2} * 2")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "quader", "zwei_wege", Z(
    "Ein Quader ist 12 cm lang, 9 cm breit und 5 cm hoch. Weg A: Rechne Länge mal Breite mal Höhe. Weg B: Teile den Quader waagerecht in einen Quader von 2 cm Höhe und einen von 3 cm Höhe und addiere die beiden Volumen. Wie groß ist das Volumen in cm³?",
    540, "12 * 9 * 5", "12 * 9 * 2 + 12 * 9 * 3", "Beide Wege müssen dasselbe Volumen ergeben.",
    "Weg A: 12 · 9 · 5 = 540 cm³. Weg B: 12 · 9 · 2 = 216 cm³ und 12 · 9 · 3 = 324 cm³. 216 + 324 = 540 cm³.",
    [(108, None, "nur die Grundfläche angegeben", "12 * 9"), (540 + 108, None, "die Grundfläche zum Volumen addiert", "12 * 9 * 5 + 12 * 9")], "cm³"), g="mehrschritt", regel="id.flaeche_raum.aus_dem_quader")
neu(T, "quader", "umkehren", Z(
    "Ein Quader hat das Volumen 504 cm³, ist 9 cm lang und 7 cm hoch. Wie breit ist er in Zentimetern?",
    8, "504 / (9 * 7)", "504 / 63", "Wie groß ist das Produkt aus Länge und Höhe?",
    "V = l · b · h. 504 = 9 · b · 7 = 63 · b. Also b = 504 : 63 = 8 cm.",
    [(72, None, "nur durch die Höhe geteilt", "504 / 7"), (56, None, "nur durch die Länge geteilt", "504 / 9"), (488, None, "die Maße abgezogen", "504 - 9 - 7")], "cm"), g="rueckwaerts", regel="id.flaeche_raum.aus_dem_quader")

# ───────── einheiten ─────────
neu(T, "einheiten", "lueckenweg", L(
    "Rechne 2,4 m³ in kleinere Einheiten um. Ein Kubikmeter sind ① dm³. 2,4 m³ sind ② dm³. Das sind ③ cm³.",
    KOMM(3), [1000, 2400, 2400000], ["10 * 10 * 10", "{1} * 2.4", "{2} * 1000"], ["1000", "2400", "2400000"], "Ein Kubikmeter ist ein Würfel mit 10 dm Kante.",
    "1 m³ = 10 · 10 · 10 dm³ = 1000 dm³. 2,4 · 1000 = 2400 dm³. 1 dm³ = 1000 cm³, also 2 400 000 cm³.",
    {0: [(100, None, "nur 10 · 10 gerechnet, die dritte Richtung vergessen", "10 * 10")], 1: [(24, None, "nur mit 10 malgenommen", "2.4 * 10")], 2: [(24000, None, "nur mit 10 statt mit 1000 malgenommen", "{2} * 10")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "einheiten", "bruecke", W(
    "Welche Angabe ist genauso groß wie 3 400 cm³?",
    "3,4 dm³",
    [("34 dm³", "mit 100 statt mit 1000 umgerechnet"), ("0,34 dm³", "mit 10 000 geteilt"), ("3,4 m³", "dm³ mit m³ verwechselt")],
    "Wie viele cm³ hat ein dm³?",
    "1 dm³ = 1000 cm³. 3 400 cm³ : 1000 = 3,4 dm³.",
    lambda: F(3400, 1000) == F(34, 10) and F(3400, 100) == 34 and F(3400, 10000) == F(34, 100) and F(34, 10) * 1000 == 3400 and F(34, 10) != 3400 * 1000), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "einheiten", "anwenden", Z(
    "Ein Schwimmbecken enthält 45 m³ Wasser. Mit einem Eimer, der 12 Liter fasst, soll es leer geschöpft werden. Wie oft muss man den Eimer füllen? (1 m³ sind 1000 Liter)",
    3750, "45 * 1000 / 12", "45000 / 12", "Rechne zuerst die Wassermenge in Liter um.",
    "45 m³ = 45 000 Liter. 45 000 : 12 = 3750. Man muss den Eimer 3750-mal füllen.",
    [(3.75, None, "die Wassermenge nicht in Liter umgerechnet", "45 / 12"), (540, None, "malgenommen statt geteilt", "45 * 12")]), g="transfer", regel="id.flaeche_raum.aus_dem_quader")

# ───────── liter ─────────
neu(T, "liter", "lueckenweg", L(
    "Ein Aquarium ist innen 60 cm lang, 30 cm breit und 40 cm hoch. Sein Volumen ist ① cm³. Das sind ② Liter. Steht das Wasser 5 cm unter dem Rand, sind ③ Liter darin.",
    KOMM(3), [72000, 72, 63], ["60 * 30 * 40", "{1} / 1000", "{2} - 60 * 30 * 5 / 1000"], ["72000", "72", "63"], "Ein Liter ist 1 dm³ = 1000 cm³.",
    "V = 60 · 30 · 40 = 72 000 cm³ = 72 Liter. Die 5 cm unter dem Rand sind 60 · 30 · 5 = 9000 cm³ = 9 Liter. 72 − 9 = 63 Liter.",
    {0: [(130, None, "die Maße addiert", "60 + 30 + 40")], 1: [(720, None, "durch 100 statt durch 1000 geteilt", "{1} / 100")], 2: [(9, None, "nur die fehlende Schicht angegeben", "60 * 30 * 5 / 1000")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "liter", "bruecke", Z(
    "In ein quaderförmiges Becken (50 cm lang, 30 cm breit) wird Wasser eingefüllt. Der Wasserspiegel steigt dabei um 4 cm. Wie viele Liter Wasser wurden eingefüllt?",
    6, "50 * 30 * 4 / 1000", "1500 * 4 / 1000", "Das eingefüllte Wasser bildet einen flachen Quader.",
    "Der flache Quader hat 50 · 30 · 4 = 6000 cm³. 1000 cm³ sind 1 Liter. Also wurden 6 Liter eingefüllt.",
    [(6000, None, "nicht in Liter umgerechnet", "50 * 30 * 4"), (0.6, None, "durch 10 000 geteilt", "50 * 30 * 4 / 10000"), (84, None, "die Maße addiert", "50 + 30 + 4")], "l"), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "liter", "umkehren", Z(
    "Ein quaderförmiger Tank hat eine Grundfläche von 2 m mal 1,5 m und fasst 4 800 Liter. Wie hoch ist der Tank in Metern?",
    1.6, "4.8 / (2 * 1.5)", "4800 / 1000 / 3", "Rechne die Liter zuerst in Kubikmeter um.",
    "4 800 Liter = 4,8 m³. Grundfläche: 2 · 1,5 = 3 m². Höhe = 4,8 : 3 = 1,6 m.",
    [(2.4, None, "nur durch die Länge 2 m geteilt", "4.8 / 2"), (3.2, None, "nur durch die Breite 1,5 m geteilt", "4.8 / 1.5"), (1600, None, "die Liter nicht in m³ umgerechnet", "4800 / 3")], "m"), g="rueckwaerts", regel="id.flaeche_raum.aus_dem_quader")

# ───────── rueckwaerts ─────────
neu(T, "rueckwaerts", "lueckenweg", L(
    "Ein Quader hat das Volumen 360 cm³. Er ist 9 cm lang und 5 cm breit. Die Grundfläche ist ① cm². Die Höhe ist ② cm. Die Oberfläche des Quaders ist ③ cm².",
    KOMM(3), [45, 8, 314], ["9 * 5", "360 / {1}", "2 * ({1} + 9 * {2} + 5 * {2})"], ["45", "8", "314"], "Aus Volumen = Grundfläche · Höhe folgt: Höhe = Volumen : Grundfläche.",
    "Grundfläche: 9 · 5 = 45 cm². Höhe: 360 : 45 = 8 cm. Oberfläche: 2 · (45 + 9 · 8 + 5 · 8) = 2 · (45 + 72 + 40) = 314 cm².",
    {0: [(14, None, "9 + 5 gerechnet", "9 + 5")], 1: [(40, None, "nur durch die Länge geteilt", "360 / 9")], 2: [(157, None, "den Faktor 2 vergessen", "{1} + 9 * {2} + 5 * {2}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "rueckwaerts", "umkehren", Z(
    "Ein Quader hat die Grundfläche 24 cm². Sein Volumen ist genauso groß wie das eines Würfels mit der Kantenlänge 6 cm. Wie hoch ist der Quader in Zentimetern?",
    9, "6 * 6 * 6 / 24", "216 / 24", "Berechne zuerst das Volumen des Würfels.",
    "Würfel: 6 · 6 · 6 = 216 cm³. Quader: 24 · h = 216, also h = 216 : 24 = 9 cm.",
    [(4, None, "Grundfläche durch die Kante geteilt", "24 / 6"), (36, None, "nur die Fläche eines Würfelquadrats angegeben", "6 * 6"), (216, None, "nur das Volumen angegeben", "6 * 6 * 6")], "cm"), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "rueckwaerts", "fehler_detektiv", FD(
    "Lara bestimmt die Breite eines Quaders mit dem Volumen 420 cm³, der Länge 7 cm und der Höhe 5 cm.",
    [("V = l · b · h, also 420 = 7 · b · 5", True), ("7 · 5 = 35, also 420 = 35 · b", 7 * 5 == 35), ("b = 420 : 35 = 12", F(420, 35) == 12), ("Probe: 7 · 12 = 84 und 84 · 5 = 410", 84 * 5 == 410)],
    "Rechne die Probe selbst nach.", "84 · 5 = 420, nicht 410. Die Breite 12 cm war richtig, aber die Probe in Zeile 4 enthält einen Rechenfehler."), regel="id.flaeche_raum.aus_dem_quader")

# ───────── zusammengesetzt ─────────
neu(T, "zusammengesetzt", "lueckenweg", L(
    "Ein Körper besteht aus einem großen Quader (12 cm lang, 5 cm breit, 4 cm hoch). Obendrauf liegt ein kleiner Quader (4 cm lang, 5 cm breit, 3 cm hoch). Der große Quader hat ① cm³. Der kleine hat ② cm³. Zusammen sind es ③ cm³. Der Körper besteht aus Ton, jeder cm³ wiegt 2 g. Der Körper wiegt ④ g.",
    KOMM(4), [240, 60, 300, 600], ["12 * 5 * 4", "4 * 5 * 3", "{1} + {2}", "{3} * 2"], ["240", "60", "300", "600"], "Rechne jeden Quader einzeln und addiere dann.",
    "Großer Quader: 12 · 5 · 4 = 240 cm³. Kleiner Quader: 4 · 5 · 3 = 60 cm³. Zusammen: 300 cm³. Gewicht: 300 · 2 g = 600 g.",
    {0: [(21, None, "die Maße addiert", "12 + 5 + 4")], 1: [(12, None, "die Maße addiert", "4 + 5 + 3")], 2: [(180, None, "abgezogen statt addiert", "{1} - {2}")],
     3: [(300, None, "das Gewicht je cm³ nicht beachtet", "{3}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "zusammengesetzt", "zwei_wege", Z(
    "Aus einem Quader (8 cm lang, 6 cm breit, 5 cm hoch) wird an einer oberen Kante ein Quader von 3 cm Länge, 6 cm Breite und 2 cm Höhe herausgeschnitten. Weg A: Rechne den ganzen Quader minus den herausgeschnittenen Teil. Weg B: Zerlege den Rest in zwei Quader und addiere. Wie groß ist das Volumen des Restkörpers in cm³?",
    204, "8 * 6 * 5 - 3 * 6 * 2", "8 * 6 * 3 + (8 - 3) * 6 * 2", "Beide Wege müssen dasselbe Volumen ergeben.",
    "Weg A: 240 cm³ − 36 cm³ = 204 cm³. Weg B: unten ein Quader 8 · 6 · 3 = 144 cm³, darüber 5 · 6 · 2 = 60 cm³. 144 + 60 = 204 cm³.",
    [(276, None, "den herausgeschnittenen Teil addiert statt abgezogen", "8 * 6 * 5 + 3 * 6 * 2"), (240, None, "den Ausschnitt vergessen", "8 * 6 * 5")], "cm³"), g="mehrschritt", regel="id.flaeche_raum.aus_dem_quader")
neu(T, "zusammengesetzt", "anwenden", Z(
    "Ein Betonsockel besteht aus zwei Quadern. Unten liegt ein Quader von 2 m Länge, 1 m Breite und 0,4 m Höhe. Darauf steht ein Quader von 1 m Länge, 1 m Breite und 0,5 m Höhe. Ein Kubikmeter Beton kostet 90 €. Wie viel Euro kostet der Beton für den Sockel?",
    117, "(2 * 1 * 0.4 + 1 * 1 * 0.5) * 90", "1.3 * 90", "Berechne das Gesamtvolumen in Kubikmetern.",
    "Unterer Quader: 2 · 1 · 0,4 = 0,8 m³. Oberer Quader: 1 · 1 · 0,5 = 0,5 m³. Zusammen 1,3 m³. 1,3 · 90 € = 117 €.",
    [(72, None, "nur den unteren Quader gerechnet", "2 * 1 * 0.4 * 90"), (1.3, None, "nur das Volumen angegeben", "2 * 1 * 0.4 + 1 * 1 * 0.5")], "€"), g="transfer", regel="id.flaeche_raum.aus_dem_quader")

# ───────── verstehen ─────────
neu(T, "verstehen", "lueckenweg", L(
    "Ein Würfel hat die Kantenlänge 5 cm. Sein Volumen ist ① cm³. Wird jede Kante verdoppelt, ist die neue Kantenlänge ② cm und das neue Volumen ③ cm³. Das neue Volumen ist ④-mal so groß wie das alte.",
    KOMM(4), [125, 10, 1000, 8], ["5 ** 3", "5 * 2", "{2} ** 3", "{3} / {1}"], ["125", "10", "1000", "8"], "Bei einem Würfel wird die Kantenlänge dreimal malgenommen.",
    "V = 5 · 5 · 5 = 125 cm³. Neue Kante: 10 cm. Neues Volumen: 10 · 10 · 10 = 1000 cm³. Das Volumen ist 1000 : 125 = 8-mal so groß.",
    {0: [(15, None, "5 · 3 gerechnet", "5 * 3")], 1: [(7, None, "2 addiert statt verdoppelt", "5 + 2")], 2: [(250, None, "das Volumen nur verdoppelt", "{1} * 2")],
     3: [(2, None, "gedacht, mit der Kante verdoppelt sich auch das Volumen", "2"), (4, None, "wie bei der Fläche gerechnet: 2 · 2", "2 * 2")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "verstehen", "umkehren", Z(
    "Ein Würfel hat das Volumen 343 cm³. Wie viele Quadratzentimeter hat eine seiner Seitenflächen?",
    49, "7 * 7", "343 / 7", "Wie lang ist eine Kante? Welche Zahl mal sich selbst mal sich selbst ergibt 343?",
    "7 · 7 · 7 = 343, die Kante ist 7 cm lang. Eine Seitenfläche ist 7 · 7 = 49 cm². Probe: 343 : 7 = 49.",
    [(343, None, "das Volumen angegeben", "343"), (294, None, "die Oberfläche statt einer Seitenfläche angegeben", "6 * 7 * 7"), (7, None, "nur die Kantenlänge angegeben", "7")], "cm²"), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "verstehen", "fehler_detektiv", FD(
    "Tim behauptet: „Verdoppelt man die Kantenlänge eines Würfels, verdoppelt sich das Volumen.“ Er prüft es.",
    [("Kante 2 cm: V = 2 · 2 · 2 = 8 cm³", 2 ** 3 == 8), ("Kante 4 cm: V = 4 · 4 · 4 = 64 cm³", 4 ** 3 == 64), ("64 : 8 = 8", F(64, 8) == 8), ("Also hat sich das Volumen verdoppelt.", F(64, 8) == 2)],
    "Wie oft passt 8 in 64? Ist das dasselbe wie verdoppeln?", "Das Volumen ist 8-mal so groß, nicht 2-mal. Die Zeilen 1 bis 3 stimmen; Zeile 4 zieht aus 64 : 8 = 8 den falschen Schluss."), regel="id.flaeche_raum.aus_dem_quader")
