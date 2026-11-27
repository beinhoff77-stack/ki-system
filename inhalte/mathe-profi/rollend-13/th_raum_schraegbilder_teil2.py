T = "raum.schraegbilder_teil2"
HA = "id.flaeche_raum.haut"
# ───────── koordinaten ─────────
neu(T, "koordinaten", "bruecke", Z(
    "Ein Quader hat vier Ecken mit den Koordinaten aus der Tabelle. A liegt im Ursprung. B, D und E sind die drei Nachbarecken von A. Die Kanten des Quaders verlaufen parallel zu den Achsen. Wie viele Volumeneinheiten hat der Quader?",
    72, "6 * 4 * 3", "3 * (4 * 6)", "Welche Länge hat die Kante AB, welche AD und welche AE?",
    "Die Kanten von A aus sind AB = 6 (x-Richtung), AD = 4 (y-Richtung) und AE = 3 (z-Richtung). Volumen = Länge mal Breite mal Höhe = 6 · 4 · 3 = 72 Volumeneinheiten.",
    [(13, None, "die drei Kantenlängen addiert", "6 + 4 + 3"), (24, None, "nur die Grundfläche 6 mal 4 gerechnet", "6 * 4"), (18, None, "nur 6 mal 3 gerechnet: die Kante in y-Richtung vergessen", "6 * 3")],
    grafik=TAB(["Ecke", "A", "B", "D", "E"], ["Koordinaten", "(0 | 0 | 0)", "(6 | 0 | 0)", "(0 | 4 | 0)", "(0 | 0 | 3)"])), g="darstellung", regel=HA)
neu(T, "koordinaten", "zwei_wege", Z(
    "Ein Quader hat die Ecken A(0 | 0 | 0), C(6 | 4 | 0), E(0 | 0 | 3) und G(6 | 4 | 3). Seine Kanten verlaufen parallel zu den Achsen. Grundfläche ist ABCD, Deckfläche ist EFGH, E liegt über A und G liegt über C. M ist der Mittelpunkt der Deckfläche. Wie groß ist die Summe der drei Koordinaten von M? Weg A: M ist die Mitte der Strecke von E nach G. Weg B: M liegt senkrecht über dem Mittelpunkt N der Grundfläche ABCD.",
    8, "(0 + 6) / 2 + (0 + 4) / 2 + 3", "(3 + 2 + 0) + 3", "Welche Koordinate ändert sich zwischen E und G nicht?",
    "Weg A: Mitte von E(0 | 0 | 3) und G(6 | 4 | 3): M(3 | 2 | 3). Weg B: N ist die Mitte von A und C, also N(3 | 2 | 0). M liegt 3 Einheiten senkrecht darüber: M(3 | 2 | 3). Beide Wege geben M(3 | 2 | 3). Summe: 3 + 2 + 3 = 8.",
    [(13, None, "die Summe der Koordinaten der Ecke G angegeben", "6 + 4 + 3"), (5, None, "den Mittelpunkt der Grundfläche statt der Deckfläche genommen", "3 + 2 + 0"), (3, None, "nur die z-Koordinate von M angegeben", "3")]), g="verknuepfen", regel=HA)
# ───────── rotation ─────────
neu(T, "rotation", "umkehren", Z(
    "Ein Rechteck mit den Seiten 4 cm und h cm dreht sich um die Seite mit der Länge h. Der entstehende Zylinder hat das Volumen 80π cm³. Wie lang ist h in Zentimetern?",
    5, "80 / 4 ** 2", "80 / 16", "Welche Seite liegt auf der Drehachse? Welche Seite wird beim Drehen zum Radius?",
    "Die Seite h liegt auf der Achse und wird die Höhe des Zylinders. Die andere Seite, 4 cm, wird der Radius. V = π · r² · h = π · 16 · h = 80π, also 16h = 80 und h = 5. Probe: π · 16 · 5 = 80π.",
    [(20, None, "durch den Radius 4 statt durch sein Quadrat geteilt", "80 / 4"), (10, None, "durch 2 mal den Radius geteilt", "80 / 8"), (1280, None, "mit dem Quadrat des Radius malgenommen statt geteilt", "80 * 16")], "cm"), g="umkehr", regel=HA)
_r_kim, _h_kim = 5, 3
neu(T, "rotation", "fehler_detektiv", FD(
    "Ein Rechteck mit den Seiten 3 cm und 5 cm dreht sich um die 5-cm-Seite. Kim bestimmt den entstehenden Körper und sein Volumen.",
    [("Es entsteht ein Zylinder mit dem Radius 5 cm und der Höhe 3 cm.", (_r_kim, _h_kim) == (3, 5), True),
     ("Das Volumen ist V = π · r² · h = π · 25 · 3, also V = 75π cm³.", 25 * 3 == 75, 5 ** 2 * 3 == 75),
     ("Die Grundfläche des Zylinders ist ein Kreis mit dem Durchmesser 10 cm.", 2 * _r_kim == 10, 2 * _r_kim == 10)],
    "Fertige eine Skizze an. Welche Seite liegt beim Drehen auf der Drehachse?",
    "Die 5-cm-Seite liegt auf der Achse und wird die Höhe. Die andere Seite, 3 cm, wird der Radius. Zeile 1 vertauscht Radius und Höhe. Richtig ist V = π · 3² · 5 = 45π cm³. Die Zeilen 2 und 3 rechnen mit dem falschen Radius 5 cm."), g="fehler", regel=HA)
# ───────── axialschnitt ─────────
neu(T, "axialschnitt", "umkehren", Z(
    "Der Axialschnitt eines Zylinders ist ein Rechteck mit dem Flächeninhalt 60 cm². Der Zylinder ist 6 cm hoch. Wie groß ist sein Radius in Zentimetern?",
    5, "60 / (2 * 6)", "60 / 6 / 2", "Wie breit ist das Schnittrechteck im Vergleich zum Radius?",
    "Der Axialschnitt ist ein Rechteck. Seine Breite ist der Durchmesser 2r, seine Höhe ist 6 cm. Aus 2r · 6 = 60 folgt 12r = 60 und r = 5. Probe: Durchmesser 10 cm, 10 · 6 = 60.",
    [(10, None, "den Durchmesser statt des Radius angegeben", "60 / 6"), (2.5, None, "durch 4 mal die Höhe geteilt", "60 / (4 * 6)"), (30, None, "die Fläche nur durch 2 geteilt", "60 / 2")], "cm"), g="umkehr", regel=HA)
neu(T, "axialschnitt", "bruecke", Z(
    "Die Zeichnung zeigt den Axialschnitt eines Zylinders. Die Breite des Rechtecks ist der Durchmesser der Grundfläche, seine Höhe ist die Höhe des Zylinders. Das Volumen ist V = n · π cm³. Welche Zahl ist n?",
    180, "6 ** 2 * 5", "36 * 5", "Aus der Breite im Schnitt erhältst du zuerst den Radius.",
    "Die Breite 12 cm ist der Durchmesser, also ist r = 6 cm. Die Höhe ist 5 cm. V = π · r² · h = π · 36 · 5 = 180π cm³. Also ist n = 180.",
    [(60, None, "die Fläche des Axialschnitts als Faktor von π angegeben", "12 * 5"), (720, None, "den Durchmesser statt des Radius quadriert", "12 ** 2 * 5"), (36, None, "die Höhe vergessen", "6 ** 2")],
    grafik={"typ": "figur", "punkte": {"A": [0, 0], "B": [6, 0], "C": [6, 2.5], "D": [0, 2.5]}, "flaeche": ["A", "B", "C", "D"], "linien": [["A", "B", "12 cm"], ["B", "C", "5 cm"]]}), g="verknuepfen", regel=HA)
# ───────── koerper_symmetrie ─────────
neu(T, "koerper_symmetrie", "anwenden", Z(
    "Ein Schuhkarton hat die Form eines Quaders. Alle drei Kantenlängen (Länge, Breite, Höhe) sind verschieden. Wie viele Symmetrieebenen hat der Karton?",
    3, "3", "1 + 1 + 1", "Jede Symmetrieebene halbiert eine Kantenrichtung. Wie viele Kantenrichtungen gibt es?",
    "Der Quader hat drei Kantenrichtungen. Je eine Ebene geht durch die Mitte und steht senkrecht zu einer Richtung. Das sind 3 Symmetrieebenen. Andere Ebenen, etwa durch gegenüberliegende Kanten, bilden den Quader nicht auf sich ab, weil die Kanten verschieden lang sind.",
    [(9, None, "die Zahl der Symmetrieebenen eines Würfels genannt", "9"), (5, None, "die Zahl der Symmetrieebenen eines Quaders mit quadratischer Grundfläche genannt", "5"), (6, None, "die sechs Flächen gezählt statt der Symmetrieebenen", "6")]), g="einkleidung", regel=HA)
neu(T, "koerper_symmetrie", "fehler_detektiv", FD(
    "Kim zählt die Symmetrieebenen einer geraden Pyramide, deren Grundfläche ein regelmäßiges Sechseck ist.",
    [("Die Spitze liegt senkrecht über dem Mittelpunkt des Sechsecks.", True, True),
     ("Jede Symmetrieebene der Pyramide enthält die Höhe, denn sonst würde die Spitze verschoben.", True, True),
     ("Ein regelmäßiges Sechseck hat 6 Symmetrieachsen und die Pyramide hat zusätzlich die Grundfläche als Ebene. Das sind 7 Symmetrieebenen.", 6 + 1 == 6, 6 + 1 == 7)],
    "Wird die Pyramide an der Ebene der Grundfläche auf sich selbst abgebildet? Wo liegt die Spitze nach dem Spiegeln?",
    "Die Zeilen 1 und 2 stimmen. In Zeile 3 ist die Grundfläche keine Symmetrieebene: Die Spitze würde unter die Grundfläche gespiegelt und die Pyramide fiele nicht auf sich. Jede der 6 Achsen des Sechsecks gibt zusammen mit der Höhe eine Symmetrieebene. Es gibt also 6 Symmetrieebenen, nicht 7."), g="fehler", regel=HA)
