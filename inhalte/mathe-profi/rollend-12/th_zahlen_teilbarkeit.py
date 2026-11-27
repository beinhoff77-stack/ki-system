T = "zahlen.teilbarkeit"
BA = "id.zahlen.bausteine"
_teiler = lambda n: sum(n % k == 0 for k in range(1, n + 1))

# ───────── teiler ─────────
neu(T, "teiler", "bruecke", Z(
    "Aus quadratischen Fliesen soll ein Rechteck mit der Fläche 36 Fliesen gelegt werden, beide Seitenlängen sind ganze Zahlen. Ein Rechteck 4 × 9 und ein Rechteck 9 × 4 gelten als dasselbe Rechteck. Wie viele verschiedene Rechtecke gibt es?",
    5, "5", "1 + 1 + 1 + 1 + 1", "Zu jeder Seitenlänge, die 36 teilt, gehört genau eine andere. Welche Zahlen teilen 36?",
    "Die Teiler von 36 sind 1, 2, 3, 4, 6, 9, 12, 18, 36. Paare: 1 × 36, 2 × 18, 3 × 12, 4 × 9, 6 × 6. Das sind 5 Rechtecke (6 × 6 ist ein Quadrat und zählt einmal).",
    [(9, None, "das Rechteck mit den Seiten 4 und 9 und das mit den Seiten 9 und 4 als verschieden gezählt, also alle Teiler von 36 gezählt", lambda: _teiler(36) == 9), (6, None, "das Quadrat mit Seite 6 doppelt gezählt", "5 + 1"), (4, None, "das Rechteck mit zwei gleich langen Seiten vergessen", "5 - 1")], "Rechtecke"))
neu(T, "teiler", "umkehren", Z(
    "Eine Zahl kleiner als 50 hat genau 3 Teiler. Es gibt mehrere solche Zahlen. Wie heißt die größte davon?",
    49, "7 * 7", "49", "Eine Zahl mit genau 3 Teilern hat die Teiler 1, eine Zahl a und sich selbst. Wie hängen a und die Zahl zusammen?",
    "Die Teiler sind 1, a und die Zahl selbst. Das geht nur, wenn die Zahl a · a ist und a eine Primzahl ist. Solche Zahlen unter 50 sind 4, 9, 25 und 49. Die größte ist 49 = 7 · 7 mit den Teilern 1, 7 und 49.",
    [(47, None, "die größte Primzahl unter 50 genommen (sie hat nur 2 Teiler)", lambda: _teiler(47) == 2), (36, None, "die Quadratzahl 36 genommen (sie hat 9 Teiler)", lambda: _teiler(36) == 9), (25, None, "nicht die größte, sondern die nächstkleinere Zahl mit 3 Teilern genommen", lambda: _teiler(25) == 3 and _teiler(49) == 3)]), g="rueckwaerts")

# ───────── vielfache ─────────
neu(T, "vielfache", "zwei_wege", Z(
    "Wie viele Vielfache von 7 liegen zwischen 100 und 200? Weg A: Schreibe sie der Reihe nach auf und zähle. Weg B: Überlege, wie viele Vielfache von 7 es bis 200 und wie viele es bis 100 gibt.",
    14, "200 // 7 - 100 // 7", "28 - 15 + 1", "Das erste Vielfache über 100 ist 105. Welches ist das letzte unter 200?",
    "Weg A: 105, 112, …, 196 sind 14 Zahlen. Weg B: Bis 200 gibt es 200 : 7 = 28 Rest 4, also 28 Vielfache (7 bis 196). Bis 100 gibt es 14 (7 bis 98). 28 − 14 = 14.",
    [(15, None, "ein Vielfaches zu viel gezählt: 28 − 14 + 1", "28 - 14 + 1"), (28, None, "alle Vielfache bis 200 gezählt", "200 // 7"), (13, None, "ein Vielfaches zu wenig gezählt", "28 - 14 - 1")], "Vielfache"))
neu(T, "vielfache", "anwenden", Z(
    "Ein Bus der Linie A fährt alle 15 Minuten, ein Bus der Linie B alle 20 Minuten. Um 8:00 Uhr fahren beide gleichzeitig ab. Nach wie vielen Minuten fahren beide zum ersten Mal wieder gleichzeitig ab?",
    60, "60", "15 * 4", "Wann sind beide Busse gleichzeitig an der Haltestelle? Was haben die Abfahrtszeiten mit Vielfachen zu tun?",
    "Vielfache von 15: 15, 30, 45, 60, … Vielfache von 20: 20, 40, 60, … Die erste gemeinsame Zahl ist 60. Nach 60 Minuten fahren beide wieder gleichzeitig ab.",
    [(5, None, "den größten gemeinsamen Teiler genommen", "5"), (300, None, "beide Zahlen malgenommen", "15 * 20"), (35, None, "beide Zahlen addiert", "15 + 20")], "Minuten"), g="transfer")

# ───────── endziffer ─────────
neu(T, "endziffer", "anwenden", W(
    "Eine Kasse hat nur 5-Euro-Scheine und 10-Euro-Scheine. Welcher Betrag kann damit nicht genau bezahlt werden?",
    "4 902 €",
    [("275 €", "Endziffer 5: durch 5 teilbar, also mit 5-Euro-Scheinen zahlbar."), ("340 €", "Endziffer 0: durch 5 teilbar, also zahlbar."), ("1 205 €", "Endziffer 5: durch 5 teilbar, also zahlbar.")],
    "Alle Beträge, die man mit 5-Euro-Scheinen zahlen kann, sind Vielfache von 5. Woran erkennt man Vielfache von 5?",
    "Vielfache von 5 enden auf 0 oder 5. 275, 340 und 1 205 enden auf 5 oder 0. 4 902 endet auf 2, ist also kein Vielfaches von 5 und lässt sich mit 5-€- und 10-€-Scheinen nicht genau zahlen.",
    lambda: [n % 5 for n in (4902, 275, 340, 1205)] == [2, 0, 0, 0]))
neu(T, "endziffer", "zwei_wege", Z(
    "Wie viele Zahlen von 100 bis 150 (beide Grenzen eingeschlossen) sind durch 5 teilbar? Weg A: Prüfe die Endziffern. Weg B: Überlege, wie viele Vielfache von 5 es bis 150 und wie viele es unter 100 gibt.",
    11, "150 // 5 - 99 // 5", "30 - 20 + 1", "Bis 99 gibt es 19 Vielfache von 5 (5 bis 95). Wie viele sind es bis 150?",
    "Weg A: Endziffer 0 oder 5: 100, 105, …, 150 sind 11 Zahlen. Weg B: Bis 150 gibt es 30 Vielfache, bis 99 gibt es 19. 30 − 19 = 11.",
    [(10, None, "die Zahl 100 nicht mitgezählt", "150 // 5 - 100 // 5"), (30, None, "alle Vielfache bis 150 gezählt", "150 // 5"), (51, None, "alle Zahlen von 100 bis 150 gezählt", "150 - 100 + 1")], "Zahlen"), g="verknuepfen")

# ───────── quersumme ─────────
neu(T, "quersumme", "anwenden", W(
    "Bei einer Tombola gewinnt jedes Los, dessen Nummer durch 3 teilbar ist. Welches dieser Lose gewinnt?",
    "Los 1 245",
    [("Los 2 378", "Quersumme 20, nicht durch 3 teilbar."), ("Los 4 123", "Quersumme 10, nicht durch 3 teilbar."), ("Los 5 606", "Quersumme 17, nicht durch 3 teilbar.")],
    "Eine Zahl ist durch 3 teilbar, wenn ihre Quersumme durch 3 teilbar ist.",
    "Quersummen: 1 245 → 12 (durch 3 teilbar), 2 378 → 20, 4 123 → 10, 5 606 → 17. Nur 12 ist durch 3 teilbar, es gewinnt Los 1 245.",
    lambda: [n % 3 for n in (1245, 2378, 4123, 5606)] == [0, 2, 1, 2]))
neu(T, "quersumme", "zwei_wege", Z(
    "Welchen Rest lässt 2 749 bei der Division durch 3? Weg A: Dividiere schriftlich. Weg B: Bilde die Quersumme und bestimme ihren Rest bei der Division durch 3. Welchen Rest lässt 2 749 bei der Division durch 3?",
    1, "2749 % 3", "(2 + 7 + 4 + 9) % 3", "Bei Weg B zählst du zuerst die Ziffern zusammen.",
    "Weg A: 2 749 : 3 = 916 Rest 1. Weg B: Quersumme 2 + 7 + 4 + 9 = 22, 22 : 3 = 7 Rest 1. Beide Wege geben Rest 1.",
    [(22, None, "die Quersumme selbst als Rest genannt", "2 + 7 + 4 + 9"), (7, None, "den Quotienten der Quersumme genannt", "22 // 3"), (0, "fb.bausteine.endziffer_statt_quersumme", "nur die Endziffer 9 angesehen: Sie ist durch 3 teilbar, also Rest 0", "9 % 3")]), g="verknuepfen")

# ───────── neunerregel ─────────
neu(T, "neunerregel", "anwenden", Z(
    "Eine Fabrik verpackt 5 873 Stifte in Packungen zu je 9 Stück. Wie viele Stifte bleiben übrig, wenn so viele volle Packungen wie möglich gefüllt werden?",
    5, "5873 % 9", "(5 + 8 + 7 + 3) % 9", "Womit kannst du den Rest bei Division durch 9 finden, ohne zu dividieren?",
    "Quersumme: 5 + 8 + 7 + 3 = 23. 23 : 9 = 2 Rest 5. Also bleibt Rest 5. Kontrolle: 5 873 = 9 · 652 + 5.",
    [(23, None, "die Quersumme als Rest genannt", "5 + 8 + 7 + 3"), (2, None, "den Quotienten der Quersumme genannt", "23 // 9"), (4, None, "mit der Quersumme 22 gerechnet (eine Ziffer falsch addiert)", "22 % 9")], "Stifte"))
neu(T, "neunerregel", "zwei_wege", Z(
    "Wie viele Zahlen von 100 bis 130 sind durch 9 teilbar? Weg A: Prüfe bei jeder Zahl die Quersumme. Weg B: Überlege, wie viele Vielfache von 9 es bis 130 und wie viele es bis 99 gibt.",
    3, "130 // 9 - 99 // 9", "(126 - 108) / 9 + 1", "Bis 99 sind es 11 Vielfache von 9 (9 bis 99). Bis 130?",
    "Weg A: Quersumme durch 9 teilbar nur bei 108, 117 und 126. Weg B: Bis 130: 130 : 9 = 14 Rest 4, also 14 Vielfache. Bis 99: 11. 14 − 11 = 3.",
    [(4, None, "ein Vielfaches zu viel gezählt", "14 - 11 + 1"), (14, None, "alle Vielfache bis 130 gezählt", "130 // 9"), (2, None, "126 vergessen", "3 - 1")], "Zahlen"), g="verknuepfen")

# ───────── primzahl ─────────
neu(T, "primzahl", "umkehren", Z(
    "Die Summe zweier Primzahlen ist 20. Eine der beiden Zahlen ist 3. Wie heißt die andere Zahl?",
    17, "20 - 3", "10 + 7", "Mache die Addition rückgängig. Prüfe dann, ob das Ergebnis eine Primzahl ist.",
    "20 − 3 = 17. 17 ist eine Primzahl, denn sie hat nur die Teiler 1 und 17. Probe: 3 + 17 = 20.",
    [(23, None, "addiert statt abgezogen", "20 + 3"), (10, None, "die Summe 20 halbiert statt 3 abzuziehen", "20 / 2")]), g="umkehr", regel=BA)
neu(T, "primzahl", "zwei_wege", Z(
    "Wie viele Primzahlen liegen zwischen 30 und 50? Weg A: Prüfe jede Zahl auf Teiler. Weg B: Schreibe alle Zahlen von 31 bis 49 auf und streiche alle Vielfachen von 2, 3, 5 und 7.",
    5, "5", "1 + 1 + 1 + 1 + 1", "Primzahlen sind größer als 1 und haben nur zwei Teiler. Gerade Zahlen über 2 fallen sofort weg.",
    "Es bleiben 31, 37, 41, 43 und 47. Bei 49 = 7 · 7 ist 7 ein Teiler. Bei Weg B werden Vielfache von 2, 3, 5 und 7 gestrichen, denn 11 · 11 ist schon größer als 50.",
    [(6, None, "49 als Primzahl mitgezählt", lambda: len([n for n in range(31, 50) if n % 2 and n % 3 and n % 5]) == 6), (10, None, "alle ungeraden Zahlen gezählt", lambda: len([n for n in range(31, 50) if n % 2]) == 10)], "Primzahlen"), g="verknuepfen", regel=BA)

# ───────── primfaktoren ─────────
neu(T, "primfaktoren", "bruecke", W(
    "Die Tabelle zeigt, wie 180 durch Teilen zerlegt wurde: Jedes Mal wurde die Zahl durch die kleinste passende Primzahl geteilt, bis 1 übrig blieb. Welche Primfaktorzerlegung von 180 steht in der Tabelle?",
    "2 · 2 · 3 · 3 · 5",
    [("2 · 2 · 3 · 3 · 5 · 5", "Der Rest 5 aus der vorletzten Zeile wurde zusätzlich als Faktor genommen."), ("2 · 3 · 5", "Jede Primzahl wurde nur einmal genommen, obwohl sie mehrfach als Teiler vorkommt.")],
    "Welche Spalte der Tabelle enthält die Primzahlen, durch die geteilt wurde?",
    "Die Teiler in der Tabelle sind 2, 2, 3, 3 und 5. Es sind alles Primzahlen und das Produkt ist 2 · 2 · 3 · 3 · 5 = 180.",
    lambda: 2 * 2 * 3 * 3 * 5 == 180 and 2 * 2 * 3 * 3 * 5 * 5 == 900 and 2 * 3 * 5 == 30,
    grafik=TAB(["Zahl", "geteilt durch", "Ergebnis"], ["180", "2", "90"], ["90", "2", "45"], ["45", "3", "15"], ["15", "3", "5"], ["5", "5", "1"])), regel=BA)
neu(T, "primfaktoren", "anwenden", Z(
    "Ein Boden ist 84 cm lang und 126 cm breit. Er soll lückenlos mit möglichst großen quadratischen Platten belegt werden, ohne dass eine Platte zerschnitten wird. Wie lang ist eine Seite einer Platte?",
    42, "2 * 3 * 7", "126 - 84", "Welche Eigenschaft muss die Seitenlänge der Platten für 84 cm und für 126 cm haben?",
    "84 = 2 · 2 · 3 · 7 und 126 = 2 · 3 · 3 · 7. Gemeinsam sind 2, 3 und 7. 2 · 3 · 7 = 42. Die Platten sind 42 cm lang. Probe: 84 : 42 = 2 und 126 : 42 = 3.",
    [(6, None, "nur die gemeinsamen Faktoren 2 und 3 genommen", "2 * 3"), (252, None, "alle Faktoren in der größeren Anzahl genommen (kleinstes gemeinsames Vielfaches)", "2 * 2 * 3 * 3 * 7"), (21, None, "einen Faktor 2 vergessen", "3 * 7")], "cm"), g="transfer", regel=BA)
