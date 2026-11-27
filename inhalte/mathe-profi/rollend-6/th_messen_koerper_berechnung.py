T = "messen.koerper_berechnung"
# ───────── quader ─────────
neu(T, "quader", "lueckenweg", L(
    "Ein Quader ist 15 cm lang, 4 cm breit und 6 cm hoch. Seine Grundfläche ist ① cm². Sein Volumen ist ② cm³. Wird die Breite verdoppelt, ist das Volumen ③ cm³.",
    KOMM(3), [60, 360, 720], ["15 * 4", "{1} * 6", "{2} * 2"], ["60", "360", "720"], "Volumen = Grundfläche mal Höhe.",
    "Grundfläche: 15 · 4 = 60 cm². Volumen: 60 · 6 = 360 cm³. Bei doppelter Breite verdoppelt sich das Volumen: 720 cm³.",
    {0: [(19, None, "addiert statt malgenommen", "15 + 4")], 1: [(25, None, "alle Maße addiert", "15 + 4 + 6")], 2: [(364, None, "die Breite addiert statt verdoppelt", "{2} + 4")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "quader", "bruecke", Z(
    "Das Netz eines Quaders besteht aus sechs Rechtecken: zwei Rechtecke mit 6 cm mal 4 cm, zwei mit 6 cm mal 3 cm und zwei mit 4 cm mal 3 cm. Wie groß ist das Volumen des Quaders in cm³?",
    72, "6 * 4 * 3", "24 * 3", "Aus den Rechtecken kannst du die drei Kantenlängen des Quaders ablesen.",
    "Die Kanten sind 6 cm, 4 cm und 3 cm lang. V = 6 · 4 · 3 = 72 cm³.",
    [(108, None, "die Oberfläche statt des Volumens berechnet", "2 * (6 * 4 + 6 * 3 + 4 * 3)"), (13, None, "die Kanten addiert", "6 + 4 + 3"), (54, None, "nur die Summe der drei verschiedenen Rechtecke", "6 * 4 + 6 * 3 + 4 * 3")], "cm³"), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "quader", "umkehren", Z(
    "Ein Quader mit quadratischer Grundfläche (Seitenlänge 5 cm) hat das Volumen 200 cm³. Zwei solche Quader werden aufeinandergestellt. Wie hoch ist der Turm in Zentimetern?",
    16, "2 * 200 / (5 * 5)", "2 * 8", "Berechne zuerst die Höhe eines Quaders.",
    "Ein Quader: 5 · 5 · h = 200, also h = 200 : 25 = 8 cm. Zwei Quader: 2 · 8 cm = 16 cm.",
    [(8, None, "nur die Höhe eines Quaders angegeben", "200 / 25"), (80, None, "durch die Seitenlänge 5 statt durch die Grundfläche geteilt, dann verdoppelt", "2 * 200 / 5")], "cm"), g="rueckwaerts", regel="id.flaeche_raum.aus_dem_quader")

# ───────── oberflaeche ─────────
neu(T, "oberflaeche", "lueckenweg", L(
    "Ein Quader ist 10 cm lang, 6 cm breit und 4 cm hoch. Boden und Deckel zusammen haben ① cm². Vorder- und Rückseite zusammen haben ② cm². Die beiden Seitenflächen zusammen haben ③ cm². Die Oberfläche ist ④ cm².",
    KOMM(4), [120, 80, 48, 248], ["2 * 10 * 6", "2 * 10 * 4", "2 * 6 * 4", "{1} + {2} + {3}"], ["120", "80", "48", "248"], "Jede Fläche kommt zweimal vor.",
    "Boden und Deckel: 2 · 10 · 6 = 120 cm². Vorn und hinten: 2 · 10 · 4 = 80 cm². Seiten: 2 · 6 · 4 = 48 cm². Zusammen 248 cm².",
    {0: [(60, None, "nur eine Fläche gerechnet", "10 * 6")], 1: [(40, None, "nur eine Fläche gerechnet", "10 * 4")], 2: [(24, None, "nur eine Fläche gerechnet", "6 * 4")], 3: [(124, None, "jede Fläche nur einmal gezählt", "10 * 6 + 10 * 4 + 6 * 4")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.haut")
neu(T, "oberflaeche", "anwenden", Z(
    "Ein offener Karton (ohne Deckel) ist 40 cm lang, 30 cm breit und 20 cm hoch. Ein Quadratmeter Pappe kostet 6 €. Wie viel Euro kostet die Pappe für einen Karton?",
    2.4, "(40 * 30 + 2 * 40 * 20 + 2 * 30 * 20) / 10000 * 6", "4000 / 10000 * 6", "Rechne die Fläche zuerst in Quadratzentimetern und dann in Quadratmetern. 1 m² = 10 000 cm².",
    "Boden: 40 · 30 = 1200 cm². Vier Wände: 2 · 40 · 20 + 2 · 30 · 20 = 2800 cm². Zusammen 4000 cm² = 0,4 m². 0,4 · 6 € = 2,40 €.",
    [(3.12, None, "den Deckel mitgerechnet", "(2 * 40 * 30 + 2 * 40 * 20 + 2 * 30 * 20) / 10000 * 6"), (0.4, None, "nur die Fläche in m² angegeben", "4000 / 10000")], "€"), regel="id.flaeche_raum.haut")
neu(T, "oberflaeche", "umkehren", Z(
    "Ein Würfel hat die Oberfläche 150 cm². Wie lang ist eine Kante in Zentimetern?",
    5, "150 / 6 / 5", "25 / 5", "Wie groß ist eine einzelne Seitenfläche? Welche Zahl mal sich selbst ergibt diese Fläche?",
    "Ein Würfel hat 6 gleiche Flächen. 150 : 6 = 25 cm². Eine Fläche ist a · a = 25, also a = 5 cm. Probe: 6 · 25 = 150.",
    [(25, None, "nur die Fläche einer Seite angegeben", "150 / 6"), (30, None, "durch 5 statt durch 6 geteilt", "150 / 5"), (75, None, "150 durch 2 geteilt", "150 / 2")], "cm"), g="rueckwaerts", regel="id.flaeche_raum.haut")

# ───────── sachaufgaben ─────────
neu(T, "sachaufgaben", "lueckenweg", L(
    "Ein Zimmer ist 5 m lang, 4 m breit und 2,5 m hoch. Die vier Wände und die Decke werden gestrichen, der Boden nicht. Die vier Wände haben zusammen ① m². Die Decke hat ② m². Zusammen sind das ③ m².",
    KOMM(3), [45, 20, 65], ["2 * (5 + 4) * 2.5", "5 * 4", "{1} + {2}"], ["45", "20", "65"], "Die Wände bilden zusammen einen Streifen: Umfang des Bodens mal Höhe.",
    "Wände: Umfang 2 · (5 + 4) = 18 m, mal 2,5 m = 45 m². Decke: 5 · 4 = 20 m². Zusammen 65 m².",
    {0: [(22.5, None, "nur zwei Wände gerechnet", "(5 + 4) * 2.5")], 1: [(9, None, "5 + 4 gerechnet", "5 + 4")], 2: [(25, None, "abgezogen statt addiert", "{1} - {2}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.haut")
neu(T, "sachaufgaben", "zwei_wege", Z(
    "Eine Schachtel ist 20 cm lang, 10 cm breit und 5 cm hoch. Weg A: Berechne die sechs Seitenflächen einzeln. Weg B: Berechne den Mantel (Umfang des Bodens mal Höhe) und addiere Boden und Deckel. Wie viel Quadratzentimeter Pappe braucht man für die ganze Schachtel?",
    700, "2 * (20 * 10 + 20 * 5 + 10 * 5)", "2 * (20 + 10) * 5 + 2 * 20 * 10", "Beide Wege müssen dieselbe Fläche ergeben.",
    "Weg A: 2 · (200 + 100 + 50) = 700 cm². Weg B: Mantel: 2 · (20 + 10) · 5 = 300 cm². Boden und Deckel: 2 · 200 = 400 cm². 300 + 400 = 700 cm².",
    [(350, None, "jede Fläche nur einmal gezählt", "20 * 10 + 20 * 5 + 10 * 5"), (1000, None, "das Volumen statt der Oberfläche berechnet", "20 * 10 * 5"), (500, None, "den Deckel vergessen", "2 * (20 + 10) * 5 + 20 * 10")], "cm²"), g="mehrschritt", regel="id.flaeche_raum.haut")
neu(T, "sachaufgaben", "anwenden", Z(
    "Ein Aquarium ohne Deckel ist 100 cm lang, 40 cm breit und 50 cm hoch. Es wird aus Glas gebaut. Ein Quadratmeter Glas kostet 6 €. Wie viel Euro kostet das Glas?",
    10.8, "(100 * 40 + 2 * 100 * 50 + 2 * 40 * 50) / 10000 * 6", "18000 / 10000 * 6", "Welche Flächen aus Glas gibt es? Der Deckel gehört nicht dazu.",
    "Boden: 100 · 40 = 4000 cm². Vorder- und Rückwand: 2 · 100 · 50 = 10 000 cm². Seitenwände: 2 · 40 · 50 = 4000 cm². Zusammen 18 000 cm² = 1,8 m². 1,8 · 6 € = 10,80 €.",
    [(13.2, None, "den Deckel mitgerechnet", "(2 * 100 * 40 + 2 * 100 * 50 + 2 * 40 * 50) / 10000 * 6"), (18000, None, "in cm² angegeben statt den Preis berechnet", "100 * 40 + 2 * 100 * 50 + 2 * 40 * 50")], "€"), g="transfer", regel="id.flaeche_raum.haut")

# ───────── zusammengesetzt ─────────
neu(T, "zusammengesetzt", "lueckenweg", L(
    "Zwei Würfel mit je 4 cm Kante werden mit je einer Fläche aneinandergeklebt. Ein einzelner Würfel hat ① cm² Oberfläche. Beide einzeln zusammen haben ② cm². Die aufeinanderliegenden Flächen sind zusammen ③ cm² groß. Die Oberfläche des neuen Körpers ist ④ cm².",
    KOMM(4), [96, 192, 32, 160], ["6 * 4 * 4", "2 * {1}", "2 * 4 * 4", "{2} - {3}"], ["96", "192", "32", "160"], "Die verklebten Flächen liegen innen und gehören nicht mehr zur Oberfläche.",
    "Ein Würfel: 6 · 4 · 4 = 96 cm². Beide: 192 cm². Zwei verklebte Flächen: 2 · 16 = 32 cm². 192 − 32 = 160 cm².",
    {0: [(24, None, "nur eine Fläche gerechnet", "6 * 4")], 1: [(96, None, "nur einen Würfel gerechnet", "{1}")], 2: [(16, None, "nur eine verklebte Fläche abgezogen", "4 * 4")], 3: [(224, None, "die verklebten Flächen addiert statt abgezogen", "{2} + {3}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.haut")
neu(T, "zusammengesetzt", "zwei_wege", Z(
    "Fünf Würfel mit je 2 cm Kante liegen so zusammengeklebt: Vier Würfel bilden eine gerade Reihe, ein fünfter Würfel ist an der Seite des ersten Würfels der Reihe angeklebt. Alles liegt auf einer Ebene. Weg A: Zähle alle Würfelflächen (5 · 6) und ziehe die verdeckten Flächen ab (jede Klebestelle verdeckt 2 Flächen). Weg B: Zähle die sichtbaren Flächen von oben, unten, vorn, hinten, links und rechts. Wie groß ist die Oberfläche in cm²?",
    88, "(5 * 6 - 2 * 4) * 4", "(5 + 5 + 4 + 4 + 2 + 2) * 2 * 2", "Eine Würfelfläche hat 4 cm². Beide Wege müssen 22 Flächen ergeben.",
    "Weg A: 30 Flächen. Es gibt 4 Klebestellen, die 8 Flächen verdecken. 22 Flächen. Weg B: oben 5, unten 5, vorn 4, hinten 4, links 2, rechts 2: ebenfalls 22 Flächen. 22 · 4 cm² = 88 cm².",
    [(120, None, "alle Flächen gezählt, nichts abgezogen", "5 * 6 * 4"), (22, None, "nur die Zahl der Flächen angegeben", "5 * 6 - 2 * 4"), (96, None, "nur drei Klebestellen abgezogen", "(5 * 6 - 2 * 3) * 4")], "cm²"), g="mehrschritt", regel="id.flaeche_raum.haut")
neu(T, "zusammengesetzt", "umkehren", Z(
    "Zwei gleiche Würfel werden mit je einer Fläche aufeinandergeklebt. Der entstandene Quader hat die Oberfläche 160 cm². Wie lang ist die Kante eines Würfels in Zentimetern?",
    4, "160 / 10 / 4", "16 / 4", "Aus wie vielen Würfelflächen besteht die Oberfläche des Quaders?",
    "Zwei Würfel haben 12 Flächen, zwei davon sind verdeckt: 10 Flächen bleiben. 160 : 10 = 16 cm² je Fläche. Eine Fläche ist a · a = 16, also a = 4 cm.",
    [(16, None, "nur die Fläche einer Würfelseite angegeben", "160 / 10"), (13.33, None, "durch 12 statt durch 10 Flächen geteilt", "160 / 12"), (20, None, "durch 8 geteilt", "160 / 8")], "cm"), g="rueckwaerts", regel="id.flaeche_raum.haut")

# ───────── verstehen ─────────
neu(T, "verstehen", "lueckenweg", L(
    "Ein Würfel hat die Kantenlänge 5 cm. Seine Oberfläche ist ① cm². Wird jede Kante verdoppelt, ist die neue Kante ② cm lang. Die neue Oberfläche ist dann ③ cm².",
    KOMM(3), [150, 10, 600], ["6 * 5 * 5", "5 * 2", "6 * {2} * {2}"], ["150", "10", "600"], "Ein Würfel hat sechs gleiche Flächen.",
    "Oberfläche: 6 · 5 · 5 = 150 cm². Neue Kante: 10 cm. Neue Oberfläche: 6 · 10 · 10 = 600 cm². Das ist das Vierfache.",
    {0: [(30, None, "6 · 5 gerechnet", "6 * 5")], 1: [(7, None, "2 addiert statt verdoppelt", "5 + 2")], 2: [(300, None, "die Oberfläche nur verdoppelt", "{1} * 2")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.flaeche_raum.haut")
neu(T, "verstehen", "bruecke", W(
    "Welche Aussage passt zur Rechnung 2 · (5 · 4 + 5 · 3 + 4 · 3) = 94? Die Maße sind in cm angegeben.",
    "Oberfläche eines Quaders mit den Kanten 5 cm, 4 cm und 3 cm: 94 cm²",
    [("Volumen eines Quaders mit den Kanten 5 cm, 4 cm und 3 cm: 94 cm³", "Volumen und Oberfläche verwechselt"),
     ("Summe aller Kanten eines Quaders mit 5 cm, 4 cm und 3 cm: 94 cm", "Kantensumme und Oberfläche verwechselt"),
     ("Oberfläche eines Würfels mit der Kante 5 cm: 94 cm²", "den Körper falsch erkannt: ein Würfel hätte 150 cm²")],
    "Wie viele Flächen hat ein Quader, und wie viele davon sind gleich groß?",
    "In der Klammer stehen die drei verschiedenen Flächen 5 · 4, 5 · 3 und 4 · 3. Jede kommt zweimal vor, deshalb der Faktor 2. Das ist die Oberfläche: 2 · 47 = 94 cm².",
    lambda: 2 * (5 * 4 + 5 * 3 + 4 * 3) == 94 and 5 * 4 * 3 != 94 and 6 * 25 != 94), regel="id.flaeche_raum.haut")
neu(T, "verstehen", "fehler_detektiv", FD(
    "Mara behauptet: „Haben zwei Quader dasselbe Volumen, dann haben sie auch dieselbe Oberfläche.“ Sie vergleicht Quader A (4 cm · 3 cm · 2 cm) und Quader B (6 cm · 4 cm · 1 cm).",
    [("Volumen A: 4 · 3 · 2 = 24 cm³; Volumen B: 6 · 4 · 1 = 24 cm³", 4 * 3 * 2 == 24 and 6 * 4 * 1 == 24), ("Oberfläche A: 2 · (12 + 8 + 6) = 52 cm²", 2 * (12 + 8 + 6) == 52), ("Oberfläche B: 2 · (24 + 6 + 4) = 68 cm²", 2 * (24 + 6 + 4) == 68), ("Also haben beide Quader dieselbe Oberfläche.", 52 == 68)],
    "Vergleiche die Oberflächen in Zeile 2 und 3.", "Die Volumen sind gleich (24 cm³), aber die Oberflächen sind 52 cm² und 68 cm². Zeile 4 widerspricht den Zeilen 2 und 3. Die Behauptung ist falsch."), regel="id.flaeche_raum.haut")
