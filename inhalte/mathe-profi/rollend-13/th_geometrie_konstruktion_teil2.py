T = "geometrie.konstruktion_teil2"
WI = "id.geometrie.winkel"
DK = "id.geometrie.deckungsgleich"
# ───────── vierecke ─────────
neu(T, "vierecke", "bruecke", Z(
    "In der Zeichnung ist ein Parallelogramm ABCD mit seinen Seitenlängen (in cm) zu sehen. Die Seiten sind AB = 9 und BC = x + 2. Im Parallelogramm sind gegenüberliegende Seiten gleich lang. Der Umfang beträgt 34 cm. Welche Zahl ist x?",
    6, "(34 - 2 * 9) / 2 - 2", "34 / 2 - 9 - 2", "Wie viele Seiten haben die Länge AB, wie viele die Länge BC? Stelle den Umfang als Gleichung auf.",
    "Gegenüberliegende Seiten sind gleich lang. Der Umfang ist 2 · 9 + 2 · (x + 2) = 34. Daraus folgt 18 + 2x + 4 = 34, also 2x = 12 und x = 6. Probe: BC = 8 cm, Umfang 2 · 9 + 2 · 8 = 34 cm.",
    [(8, None, "die Seite BC statt x angegeben", "(34 - 2 * 9) / 2"), (23, None, "jede Seitenlänge nur einmal gezählt: nur AB und BC im Umfang", "34 - 9 - 2"), (14, None, "die Differenz zum Umfang minus 2 gerechnet, aber nicht durch 2 geteilt", "34 - 2 * 9 - 2")],
    grafik={"typ": "figur", "punkte": {"A": [0, 0], "B": [6, 0], "C": [8, 3], "D": [2, 3]}, "flaeche": ["A", "B", "C", "D"], "linien": [["A", "B", "9 cm"], ["B", "C", "x + 2 cm"]]}), g="darstellung", regel=WI)
neu(T, "vierecke", "zwei_wege", Z(
    "ABCD ist eine Raute: Alle vier Seiten sind gleich lang. Der Winkel bei A ist α = 50°. Wie groß ist der Winkel zwischen der Seite AB und der Diagonale AC? Weg A: Die Diagonale halbiert den Winkel der Raute. Weg B: Das Dreieck ABC ist gleichschenklig mit AB = BC. Der Winkel β bei B ist der Nachbarwinkel von α. Rechne den Basiswinkel bei A aus.",
    25, "50 / 2", "(180 - (180 - 50)) / 2", "Wie groß ist der Winkel β bei B? Nachbarwinkel im Parallelogramm ergänzen sich.",
    "Weg A: Die Diagonale AC halbiert den Winkel bei A. 50° : 2 = 25°. Weg B: β = 180° − 50° = 130°. Im gleichschenkligen Dreieck ABC sind die Winkel bei A und bei C gleich groß: (180° − 130°) : 2 = 25°. Beide Wege geben 25°.",
    [(50, None, "den ganzen Winkel α der Raute angegeben, nicht die Hälfte", "50"), (65, None, "den Basiswinkel mit α statt mit β als Winkel an der Spitze gerechnet", "(180 - 50) / 2"), (130, None, "den Nachbarwinkel β angegeben", "180 - 50")], "°"), g="verknuepfen", regel=WI)
# ───────── vierecke_konstruieren ─────────
neu(T, "vierecke_konstruieren", "umkehren", Z(
    "Du konstruierst ein Parallelogramm ABCD mit a = AB = 7 cm und α = 60°. Gegenüberliegende Seiten sind gleich lang. Der Umfang soll 24 cm betragen. Wie lang in Zentimetern muss die Seite b = BC sein?",
    5, "24 / 2 - 7", "(24 - 2 * 7) / 2", "Wie viele Seiten haben die Länge a und wie viele die Länge b?",
    "Der Umfang ist 2a + 2b = 24. Mit a = 7 ist 14 + 2b = 24, also 2b = 10 und b = 5. Probe: 2 · 7 + 2 · 5 = 24. Der Winkel 60° ändert den Umfang nicht.",
    [(17, None, "nur a vom Umfang abgezogen", "24 - 7"), (8.5, None, "a nur einmal abgezogen und durch 2 geteilt", "(24 - 7) / 2"), (10, None, "2a vom Umfang abgezogen, aber nicht durch 2 geteilt", "24 - 2 * 7")], "cm"), g="umkehr", regel=DK)
assert 2 * 7 + 2 * 5 == 24
neu(T, "vierecke_konstruieren", "anwenden", Z(
    "Ein Metallrahmen hat die Form einer Raute. Die beiden Diagonalen sind 24 cm und 10 cm lang. In einer Raute halbieren sich die Diagonalen, und sie stehen senkrecht aufeinander. Wie viele Zentimeter Rahmenstab werden für den ganzen Rand der Raute gebraucht?",
    52, "4 * wurzel(12 ** 2 + 5 ** 2)", "4 * 13", "Die Diagonalen teilen die Raute in vier gleiche Dreiecke. Welche Seiten hat jedes Dreieck?",
    "Die halben Diagonalen sind 12 cm und 5 cm lang und stehen senkrecht aufeinander. Die Seite der Raute ist die längste Seite eines rechtwinkligen Dreiecks: s² = 12² + 5² = 169, also s = 13 cm. Der Rand besteht aus 4 gleich langen Seiten: 4 · 13 = 52 cm.",
    [(13, None, "nur eine Seite der Raute angegeben", "wurzel(12 ** 2 + 5 ** 2)"), (34, None, "die beiden ganzen Diagonalen addiert", "24 + 10"), (68, None, "die Seite als Summe der halben Diagonalen gerechnet", "4 * (12 + 5)")], "cm"), g="verknuepfen", regel=DK)
