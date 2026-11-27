"""rollend-5 · messen.koerper_darstellung (6 Lernkarten, 18 Aufgaben)."""
from k5basis import *      # noqa: F401,F403

TH = "messen.koerper_darstellung"
HA, AQ = "id.flaeche_raum.haut", "id.flaeche_raum.aus_dem_quader"

# ── prisma ──
neu(TH, "prisma", "lueckenweg", "direkt", L(
    "Ein Prisma hat ein Sechseck als Grundfläche. Grund- und Deckfläche haben je 6 Ecken, zusammen ①. An jeder Ecke treffen sich 3 Kanten, und jede Kante hat 2 Ecken. Die Zahl der Kanten ist deshalb ① · 3 : 2 = ②.",
    ["2*6", "2*6*3//2"], ["12", "18"], "Zähle die Ecken von Grund- und Deckfläche zusammen.", "Ecken: 6 + 6 = 12. Kanten: 12 · 3 : 2 = 18. Das ist auch 3 · 6.",
    {0: [(6, None, "nur die Grundfläche gezählt")], 1: [(36, None, "nicht durch 2 geteilt")]}), HA)
neu(TH, "prisma", "zwei_wege", "mehrschritt", Z(
    "Ein Prisma hat ein Siebeneck als Grundfläche. Wie viele Kanten hat es? Weg A zählt die Ecken des Prismas. An jeder Ecke treffen sich 3 Kanten, und jede Kante hat 2 Ecken. Weg B zählt die Kanten der Grundfläche, die der Deckfläche und die Seitenkanten einzeln.",
    "14*3//2", "7+7+7", "Beide Wege geben dieselbe Zahl.", "Weg A: Ecken 7 + 7 = 14. Kanten 14 · 3 : 2 = 21. Weg B: 7 + 7 + 7 = 21 Kanten.",
    [(14, None, "die Seitenkanten vergessen"), (9, None, "7 + 2 gerechnet"), (42, None, "nicht durch 2 geteilt")]), HA)
neu(TH, "prisma", "anwenden", "einkleidung", Z(
    "Eine Schachtel hat die Form eines Prismas mit einem Fünfeck als Grundfläche. Auf jede Fläche, auch Grund- und Deckfläche, kommt ein Aufkleber. Eine Packung enthält 15 Aufkleber. Wie viele Packungen braucht man mindestens für 6 Schachteln?",
    "-(-7*6//15)", "(7*6+14)//15", "Wie viele Flächen hat das Prisma? Danach: Mit angebrochenen Packungen kommst du nicht aus.", "Flächen: 5 Seitenflächen + 2 = 7. 6 Schachteln: 42 Aufkleber. 42 : 15 = 2,8, also 3 Packungen.",
    [(2, None, "abgerundet: es fehlen Aufkleber"), (4, None, "mit 8 Flächen gerechnet: 48 Aufkleber, also 4 Packungen")]), HA)

# ── netz ──
neu(TH, "netz", "fehler_detektiv", "fehler", FDZ(
    "Ein Quader ist 6 cm lang, 2 cm breit und 3 cm hoch. Kim berechnet die Fläche seines Netzes.",
    [("Das Netz besteht aus 6 Rechtecken, je zwei gleiche.", True), ("Die drei verschiedenen Rechtecke haben die Flächen 6 · 2 = 12, 6 · 3 = 18 und 2 · 3 = 6 cm².", 6 * 2 == 12 and 6 * 3 == 18 and 2 * 3 == 6), ("Ich zähle jede der drei Flächen nur einmal: 12 + 18 + 6 = 36 cm².", 2 * (12 + 18 + 6) == 36), ("Das Netz hat 36 cm² Fläche.", True)],
    "Wie viele Rechtecke hat das Netz? Wie oft kommt jede Fläche vor?", "Jedes der drei Rechtecke kommt zweimal vor: 2 · (12 + 18 + 6) = 72 cm²."), HA)
assert 6 * 5 * 5 == 150
neu(TH, "netz", "umkehren", "umkehr", Z(
    "Ein Würfelnetz besteht aus 6 gleichen Quadraten und hat zusammen 150 cm² Fläche. Wie lang ist eine Würfelkante in cm?",
    "5", str(next(a for a in range(1, 30) if 6 * a * a == 150)), "Wie groß ist ein einzelnes Quadrat? Welche Zahl mal sich selbst gibt diese Fläche?", "150 : 6 = 25 cm² für ein Quadrat. 5 · 5 = 25, also ist die Kante 5 cm lang.",
    [(25, None, "die Fläche eines Quadrats als Kante genommen"), (30, None, "150 : 5 gerechnet")], einheit="cm"), HA)
neu(TH, "netz", "bruecke", "darstellung", Z(
    "Die Tabelle beschreibt die Rechtecke im Netz eines Quaders. Wie groß ist die ganze Netzfläche in cm²?",
    "2*5*3+2*5*4+2*3*4", "2*(15+20+12)", "Rechne erst jede Rechteckfläche, dann mal Anzahl, dann alles addieren.", "Boden und Deckel: 2 · 15 = 30. Vorder- und Rückseite: 2 · 20 = 40. Seiten: 2 · 12 = 24. Zusammen 94 cm².",
    [(47, None, "jede Fläche nur einmal gezählt"), (60, None, "das Volumen 5 · 3 · 4 genommen")],
    grafik=TAB(["Fläche", "Maße in cm", "Anzahl"], ["Boden", "5 × 3", "2"], ["Vorderseite", "5 × 4", "2"], ["Seite", "3 × 4", "2"]), einheit="cm²"), HA)

# ── zylinder ──
neu(TH, "zylinder", "lueckenweg", "direkt", L(
    "Eine zylindrische Dose ist 12 cm hoch. Der Umfang ihrer Grundfläche ist 30 cm. Der Mantel ist ein Rechteck: Länge = Umfang, Breite = Höhe. Die Mantelfläche einer Dose ist 30 · 12 = ①. Fünf solche Dosen sollen nur außen am Mantel gestrichen werden, ohne Boden und Deckel: Mantelfläche aller fünf Dosen ① · 5 = ②. Ein Eimer Farbe reicht für 600 cm². Man braucht ② : 600 = ③ Eimer.",
    ["30*12", "30*12*5", "30*12*5//600"], ["360", "1800", "3"], "Der Mantel ist so lang wie der Umfang, nicht wie der Durchmesser.", "30 · 12 = 360 cm². 360 · 5 = 1 800 cm². 1 800 : 600 = 3 Eimer.",
    {0: [(42, None, "30 + 12 gerechnet")], 1: [(210, None, "mit 42 weitergerechnet")]}), HA)
neu(TH, "zylinder", "umkehren", "umkehr", Z(
    "Das Mantel-Rechteck einer Dose hat die Fläche 420 cm². Der Umfang der Grundfläche beträgt 28 cm. Wie hoch ist die Dose?",
    "420//28", "15", "Fläche = Umfang mal Höhe. Welche Rechnung macht das Malnehmen rückgängig?", "420 : 28 = 15. Probe: 28 · 15 = 420. Die Dose ist 15 cm hoch.",
    [(448, None, "28 + 420 gerechnet"), (11760, None, "malgenommen statt geteilt")], einheit="cm"), HA)
neu(TH, "zylinder", "anwenden", "einkleidung", Z(
    "Für jede Dose braucht man ein Etikett: ein Rechteck, 24 cm lang und 10 cm hoch. Du hast ein Papierband, das 10 cm breit und 1 000 cm lang ist. Die Etiketten werden nacheinander in einer Reihe aus dem Band geschnitten, jedes mit der 24-cm-Seite längs des Bandes. Wie viele ganze Etiketten bekommst du aus dem Band?",
    "1000//24", "41", "Das Band ist so breit wie ein Etikett hoch. Wie oft passt die Länge 24 cm in 1 000 cm? Ein Rest zählt nicht.", "1 000 : 24 = 41 Rest 16. Es passen 41 ganze Etiketten. Für ein 42. Etikett fehlen 8 cm.",
    [(42, None, "aufgerundet: das 42. Etikett passt nicht mehr ganz auf das Band"), (100, None, "nur durch die Höhe 10 cm geteilt")]), HA)

# ── schraegbild ──
neu(TH, "schraegbild", "zwei_wege", "mehrschritt", Z(
    "Ein Quader ist 8 cm breit, 6 cm hoch und 10 cm tief. Im Schrägbild wird nur die Tiefe halb so lang gezeichnet. Wie lang sind alle zwölf Kanten des Schrägbilds zusammen? Weg A addiert die vier Kanten jeder Richtung, so wie sie gezeichnet werden. Weg B rechnet zuerst alle zwölf Kanten des echten Quaders und zieht dann ab, was die vier Tiefenkanten im Schrägbild kürzer sind.",
    "4*8+4*6+4*(10//2)", "4*(8+6+10)-4*(10-10//2)", "Die vier Kanten jeder Richtung sind gleich lang.", "Weg A: Gezeichnet werden 8 cm, 6 cm und 5 cm. 32 + 24 + 20 = 76. Weg B: Der echte Quader hat 4 · 24 = 96. Die vier Tiefenkanten sind je 5 cm kürzer: 96 − 20 = 76.",
    [(96, None, "die Tiefe nicht halbiert"), (24, None, "nur die Maße 8 + 6 + 10 addiert: weder mal 4 noch die Tiefe halbiert"), (19, None, "nur die gezeichneten Längen 8 + 6 + 5 addiert, das Mal 4 vergessen")], einheit="cm"), AQ)
neu(TH, "schraegbild", "bruecke", "darstellung", W(
    "Die Tabelle zeigt die wahren Maße eines Quaders. Im Schrägbild wird nur die Kante nach hinten halbiert. Welche Längen zeichnest du für Breite, Höhe und Tiefe?",
    "8 cm, 6 cm, 5 cm", [("4 cm, 3 cm, 5 cm", "alle Kanten halbiert"), ("8 cm, 6 cm, 10 cm", "nichts verkürzt"), ("8 cm, 3 cm, 10 cm", "die falsche Kante halbiert")],
    "Nur eine Richtung wird verkürzt. Welche?", "Breite und Höhe liegen vorn und bleiben in wahrer Größe. Nur die Tiefe nach hinten wird halbiert: 10 : 2 = 5 cm.",
    10 // 2 == 5 and 8 // 2 != 8, grafik=TAB(["", "Breite", "Höhe", "Tiefe"], ["wahr", "8 cm", "6 cm", "10 cm"])), AQ)
neu(TH, "schraegbild", "anwenden", "einkleidung", Z(
    "Du zeichnest ein Schrägbild eines Schranks. Er ist 90 cm breit, 200 cm hoch und 60 cm tief. Dein Maßstab ist 1 : 10, in der Zeichnung steht also 1 cm für 10 cm. Die Tiefe wird zusätzlich halb so lang gezeichnet. Wie viele Zentimeter lang zeichnest du die Kante nach hinten?",
    "60//10//2", "3", "Erst den Maßstab anwenden, dann die Tiefe halbieren.", "Im Maßstab 1 : 10 sind 60 cm nur 6 cm. Nach hinten wird halbiert: 3 cm.",
    [(6, None, "die Tiefe nicht halbiert"), (30, None, "den Maßstab vergessen")], einheit="cm"), AQ)

# ── ansichten ──
neu(TH, "ansichten", "fehler_detektiv", "fehler", FDZ(
    "Kim beschreibt die drei Ansichten einer stehenden zylinderförmigen Dose.",
    [("Von vorn sieht man ein Rechteck.", True), ("Von der Seite sieht man ebenfalls ein Rechteck.", True), ("Von oben sieht man nur den Deckel.", True), ("Der Deckel ist ein Rechteck.", False)],
    "Welche Form hat der Deckel einer zylinderförmigen Dose?", "Der Deckel ist ein Kreis. Von oben sieht man deshalb einen Kreis."), HA)
neu(TH, "ansichten", "verfahren_waehlen", "erkennen", W(
    "Ein Körper sieht von vorn aus wie ein Rechteck, von der Seite auch wie ein Rechteck und von oben wie ein Kreis. Welcher Körper ist es?",
    "ein stehender Zylinder: oben ein Kreis, vorn und von der Seite je ein Rechteck",
    [("ein Quader, denn er hat überall Rechtecke", "von oben sieht ein Quader nie rund aus"), ("ein Kegel, denn er hat einen Kreis", "von vorn sieht ein Kegel wie ein Dreieck aus"), ("eine Kugel, denn sie ist rund", "von vorn und von der Seite ist eine Kugel ein Kreis")],
    "Prüfe jeden Körper mit allen drei Ansichten.", "Nur beim Zylinder passt alles: vorn und seitlich ein Rechteck, oben ein Kreis.", True), HA)
neu(TH, "ansichten", "anwenden", "einkleidung", Z(
    "Ein Architekt zeichnet ein Haus, das die Form eines Quaders hat: 10 m breit, 6 m tief und 5 m hoch. Wie groß ist die Fläche der Ansicht von oben in m²?",
    "10*6", "60", "Von oben sieht man Breite und Tiefe, nicht die Höhe.", "Die Ansicht von oben ist ein Rechteck mit 10 m und 6 m: 10 · 6 = 60 m².",
    [(50, None, "Breite mal Höhe genommen"), (300, None, "das Volumen genommen")], einheit="m²"), HA)

# ── beurteilen ──
neu(TH, "beurteilen", "verfahren_waehlen", "begruenden", W(
    "Kim behauptet: „Jeder Körper mit lauter ebenen Flächen ist ein Prisma.“ Wie widerlegst du das am besten?",
    "Mit einem Gegenbeispiel: Eine Pyramide hat lauter ebene Flächen, aber keine zwei parallelen Grundflächen",
    [("Mit vielen Prismen, die ebene Flächen haben", "Beispiele beweisen nichts"), ("Mit einer Kugel, denn sie hat keine ebenen Flächen", "passt nicht zur Behauptung"), ("Mit dem Zählen der Kanten eines Würfels", "ein Würfel ist ein Prisma")],
    "Ein einziges Beispiel, das die Behauptung nicht erfüllt, genügt.", "Die Pyramide hat nur ebene Flächen. Sie ist aber kein Prisma, weil die zweite parallele Grundfläche fehlt.", True), HA)
neu(TH, "beurteilen", "umkehren", "umkehr", Z(
    "Du baust ein Prisma aus Strohhalmen. Du brauchst genau 9 Halme als Kanten. Wie viele Ecken hat dann seine Grundfläche?",
    "9//3", "3", "Ein Prisma mit einem n-Eck als Grundfläche hat 3 · n Kanten.", "3 · n = 9, also n = 9 : 3 = 3. Die Grundfläche ist ein Dreieck.",
    [(6, None, "Zahl der Ecken des ganzen Körpers genannt"), (4, None, "von einem Quader ausgegangen")]), HA)
neu(TH, "beurteilen", "anwenden", "einkleidung", Z(
    "Ein Schmuckkästchen hat die Form eines Prismas mit einem Siebeneck als Grundfläche. Wie viele Ecken, Kanten und Flächen hat es zusammen?",
    "2*7+3*7+7+2", "14+21+9", "Ecken: 2n, Kanten: 3n, Flächen: n + 2. Dann alles addieren.", "Ecken: 14. Kanten: 21. Flächen: 7 + 2 = 9. Zusammen 14 + 21 + 9 = 44.",
    [(35, None, "die Flächen vergessen"), (42, None, "die zwei Grundflächen als Flächen vergessen: 14 + 21 + 7")]), HA)
