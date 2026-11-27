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
neu(T, "vierecke_konstruieren", "umkehren", W(
    "Du konstruierst ein Parallelogramm ABCD mit a = AB = 7 cm und α = 60°. Der Umfang soll 24 cm betragen. Gegenüberliegende Seiten sind gleich lang. Du hast AB gezeichnet und in A den Strahl für den Winkel 60° angetragen. Wie geht die Konstruktion richtig weiter?",
    "Auf dem Strahl von A aus AD = 5 cm abtragen. Durch D die Parallele zu AB und durch B die Parallele zu AD zeichnen. Ihr Schnittpunkt ist C.",
    [("Auf dem Strahl von A aus AD = 10 cm abtragen. Durch D die Parallele zu AB und durch B die Parallele zu AD zeichnen. Ihr Schnittpunkt ist C.", "2a vom Umfang abgezogen, aber nicht durch 2 geteilt: 24 − 14 = 10 statt 5"),
     ("Auf dem Strahl von A aus AD = 5 cm abtragen. Durch D und durch B jeweils die Senkrechte zu AB zeichnen. Ihr Schnittpunkt ist C.", "die Länge stimmt, aber Senkrechte statt Parallelen zu AD: so entsteht kein Parallelogramm mit dem Winkel 60°"),
     ("Auf dem Strahl von A aus AD = 8,5 cm abtragen. Durch D die Parallele zu BD und durch B die Parallele zu AB zeichnen. Ihr Schnittpunkt ist C.", "a nur einmal abgezogen: (24 − 7) : 2 = 8,5; außerdem sind die Parallelen nicht zu den gegenüberliegenden Seiten gezeichnet")],
    "Wie viele Seiten haben die Länge a und wie viele die Länge b? Welche Seiten sind zueinander parallel?",
    "Der Umfang ist 2a + 2b = 24. Mit a = 7 ist 14 + 2b = 24, also b = 5. Probe: 2 · 7 + 2 · 5 = 24. Der Winkel 60° ändert den Umfang nicht. D liegt auf dem Strahl im Abstand 5 cm von A. In einem Parallelogramm ist DC parallel zu AB und BC parallel zu AD, deshalb ist C der Schnittpunkt der Parallele durch D zu AB und der Parallele durch B zu AD.",
    lambda: 2 * 7 + 2 * 5 == 24 and 2 * 7 + 2 * 10 != 24 and 2 * 7 + 2 * 8.5 != 24), g="umkehr", regel=None)
neu(T, "vierecke_konstruieren", "anwenden", W(
    "Ein Fliesenleger konstruiert eine Raute ABCD aus nur zwei Angaben: der Seitenlänge 9 cm und dem Winkel α = 60° bei A. Er zeichnet AB = 9 cm und trägt in A den Strahl für den Winkel 60° an. Danach schneidet er die Raute entlang der Diagonale BD in zwei Dreiecke. In einer Raute sind alle vier Seiten gleich lang. Welche Konstruktion und welcher Rand eines der beiden Dreiecke gehören zusammen?",
    "AD = 9 cm auf dem Strahl abtragen; durch D die Parallele zu AB und durch B die Parallele zu AD zeichnen, Schnittpunkt C. Das Dreieck ABD ist gleichseitig, sein Rand ist 27 cm lang.",
    [("AD = 9 cm auf dem Strahl abtragen; durch D und durch B die Senkrechte zu AB zeichnen, Schnittpunkt C. Das Dreieck ABD ist gleichseitig, sein Rand ist 27 cm lang.", "die Länge und der Rand stimmen, aber mit Senkrechten statt Parallelen entsteht keine Raute"),
     ("AD = 9 cm auf dem Strahl abtragen; durch D die Parallele zu AB und durch B die Parallele zu AD zeichnen, Schnittpunkt C. Der Rand des Dreiecks ABD ist 18 cm lang.", "die Diagonale BD vergessen: nur die zwei Raute-Seiten gezählt"),
     ("AD = 4,5 cm auf dem Strahl abtragen; durch D die Parallele zu AB und durch B die Parallele zu AD zeichnen, Schnittpunkt C. Der Rand des Dreiecks ABD ist 22,5 cm lang.", "die Seite AD nur halb so lang abgetragen, obwohl in der Raute alle Seiten 9 cm lang sind")],
    "Welche Länge hat AD, weil in der Raute alle Seiten gleich lang sind? Welche zwei Seiten und welcher Winkel gehören zum Dreieck ABD?",
    "In der Raute ist AD = AB = 9 cm. Die Parallelen durch D und durch B legen C fest, dann ist auch BC = CD = 9 cm. Im Dreieck ABD ist AB = AD = 9 cm und der Winkel bei A ist 60°. Die beiden anderen Winkel sind gleich groß: (180° − 60°) : 2 = 60°. Das Dreieck ist gleichseitig, BD = 9 cm. Der Rand ist 9 + 9 + 9 = 27 cm lang. Senkrechte statt Parallelen ergäben keine Raute.",
    lambda: (180 - 60) / 2 == 60 and 9 + 9 + 9 == 27 and 9 + 9 != 27 and 9 + 9 + 4.5 != 27), g="verknuepfen", regel=DK)
