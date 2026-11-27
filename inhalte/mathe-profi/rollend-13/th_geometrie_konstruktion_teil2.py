T = "geometrie.konstruktion_teil2"
WI = "id.geometrie.winkel"
DK = "id.geometrie.deckungsgleich"
# ───────── vierecke ─────────
neu(T, "vierecke", "bruecke", Z(
    "In der Zeichnung ist ein Parallelogramm ABCD mit zwei Winkelangaben (in Grad) zu sehen. Benachbarte Winkel im Parallelogramm ergänzen sich zu 180°. Welche Zahl ist x?",
    40, "(180 - 30 - 30) / 3", "(180 - 60) // 3", "Liegen die Ecken A und B nebeneinander oder gegenüber? Was gilt dann für die beiden Winkel?",
    "A und B sind benachbarte Ecken. Benachbarte Winkel ergeben zusammen 180°: (x + 30) + (2x + 30) = 180. Also 3x + 60 = 180, 3x = 120 und x = 40. Probe: 70° + 110° = 180°.",
    [(0, None, "die Winkel gleichgesetzt, als lägen die Ecken gegenüber: x + 30 = 2x + 30", "30 - 30"), (100, None, "die Summe 360° statt 180° genommen: 3x + 60 = 360", "(360 - 60) / 3"), (60, None, "die Zahlen 30 vergessen: x + 2x = 180", "180 / 3")],
    grafik={"typ": "figur", "punkte": {"A": [0, 0], "B": [6, 0], "C": [8, 5.5], "D": [2, 5.5]}, "flaeche": ["A", "B", "C", "D"], "winkel": [["A", "B", "D", "(x + 30)°"], ["B", "C", "A", "(2x + 30)°"]]}), g="darstellung", regel=WI)
assert (40 + 30) + (2 * 40 + 30) == 180
neu(T, "vierecke", "zwei_wege", Z(
    "ABCD ist eine Raute: Alle vier Seiten sind gleich lang. Der Winkel bei A ist α = 50°. Weg A: Die Diagonale halbiert den Winkel der Raute. Weg B: Das Dreieck ABC ist gleichschenklig mit AB = BC. Der Winkel β bei B ist der Nachbarwinkel von α. Rechne den Basiswinkel bei A aus. Wie groß ist der Winkel zwischen der Seite AB und der Diagonale AC?",
    25, "50 / 2", "(180 - (180 - 50)) / 2", "Wie groß ist der Winkel β bei B? Nachbarwinkel im Parallelogramm ergänzen sich.",
    "Weg A: Die Diagonale AC halbiert den Winkel bei A. 50° : 2 = 25°. Weg B: β = 180° − 50° = 130°. Im gleichschenkligen Dreieck ABC sind die Winkel bei A und bei C gleich groß: (180° − 130°) : 2 = 25°. Beide Wege geben 25°.",
    [(50, None, "den ganzen Winkel α der Raute angegeben, nicht die Hälfte", "50"), (65, None, "den Basiswinkel mit α statt mit β als Winkel an der Spitze gerechnet", "(180 - 50) / 2"), (130, None, "den Nachbarwinkel β angegeben", "180 - 50")], "°"), g="verknuepfen", regel=WI)
# ───────── vierecke_konstruieren ─────────
neu(T, "vierecke_konstruieren", "umkehren", Z(
    "Du konstruierst ein Parallelogramm ABCD: Du zeichnest AB mit a = 7 cm, trägst in A den Winkel α = 60° an und trägst auf dem freien Schenkel von A aus die Seite b = AD ab. Durch D zeichnest du die Parallele zu AB und durch B die Parallele zu AD; ihr Schnittpunkt ist C. Gegenüberliegende Seiten sind gleich lang. Der Umfang soll 24 cm betragen. Wie lang in Zentimetern muss die Seite b = AD = BC sein?",
    5, "24 / 2 - 7", "(24 - 2 * 7) / 2", "Wie viele Seiten haben die Länge a und wie viele die Länge b?",
    "Der Umfang ist 2a + 2b = 24. Mit a = 7 ist 14 + 2b = 24, also 2b = 10 und b = 5. Probe: 2 · 7 + 2 · 5 = 24. Der Winkel 60° ändert den Umfang nicht. Mit a, α und b = 5 cm liegen A, B und D fest; C ergibt sich eindeutig als Schnittpunkt der beiden Parallelen.",
    [(17, None, "nur a vom Umfang abgezogen", "24 - 7"), (8.5, None, "a nur einmal abgezogen und durch 2 geteilt", "(24 - 7) / 2"), (10, None, "2a vom Umfang abgezogen, aber nicht durch 2 geteilt", "24 - 2 * 7")], "cm"), g="umkehr", regel=None)
assert 2 * 7 + 2 * 5 == 24
neu(T, "vierecke_konstruieren", "anwenden", Z(
    "Ein Fliesenleger konstruiert eine Raute ABCD aus nur zwei Angaben: der Seitenlänge 9 cm und dem Winkel α = 60° bei A. Er zeichnet AB = 9 cm, trägt in A den Winkel 60° an und trägt auf dem freien Schenkel von A aus 9 cm ab; das ist D. Danach zeichnet er durch D die Parallele zu AB und durch B die Parallele zu AD; ihr Schnittpunkt ist C. Dann schneidet er die Raute entlang der Diagonale BD in zwei Dreiecke. In einer Raute sind alle vier Seiten gleich lang. Wie viele Zentimeter ist der Rand eines der beiden Dreiecke lang?",
    27, "9 + 9 + 9", "3 * 9", "Welche Länge hat AD, weil die Seitenlänge von A aus abgetragen wird? Welche zwei Seiten und welcher Winkel gehören dann zum Dreieck ABD?",
    "Konstruktion: D liegt auf dem freien Schenkel im Abstand 9 cm von A, C liegt auf den beiden Parallelen, also ist auch BC = CD = 9 cm. Im Dreieck ABD ist AB = AD = 9 cm und der Winkel bei A ist 60°. Die beiden anderen Winkel sind gleich groß: (180° − 60°) : 2 = 60°. Alle drei Winkel sind 60°, das Dreieck ist gleichseitig, also ist BD = 9 cm. Der Rand ist 9 + 9 + 9 = 27 cm lang.",
    [(18, None, "die Diagonale BD vergessen: nur die zwei Raute-Seiten gezählt", "9 + 9"), (36, None, "den Umfang der ganzen Raute angegeben", "4 * 9"), (22.5, None, "die Diagonale BD als halb so lang wie die Seite angenommen", "9 + 9 + 9 / 2")], "cm"), g="verknuepfen", regel=DK)
assert (180 - 60) / 2 == 60
