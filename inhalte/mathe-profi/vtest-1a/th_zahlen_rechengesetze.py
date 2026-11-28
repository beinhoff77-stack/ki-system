T = "zahlen.rechengesetze"
RR, RT, RA, RG, RB = "rr.reihenfolge", "rr.tauschen", "rr.ausmultiplizieren", "rr.gegenrechnung", "id.zahlen.buendeln"
# ═════════ klammern ═════════
neu(T, "klammern", "test", "rueckwaerts", W(
    "In der Rechnung 20 − 4 · 3 + 2 darf genau ein Klammerpaar gesetzt werden. Danach soll das Ergebnis 50 sein. Welche Rechnung ist richtig?",
    "(20 − 4) · 3 + 2",
    [("20 − (4 · 3 + 2)", "Klammer um 4 · 3 + 2: Wert 6", 20 - (4 * 3 + 2) != 50),
     ("20 − 4 · (3 + 2)", "Klammer um 3 + 2: Wert 0", 20 - 4 * (3 + 2) != 50),
     ("(20 − 4 · 3) + 2", "Klammer um 20 − 4 · 3: ändert nichts, Wert 10", (20 - 4 * 3) + 2 != 50),
     ("(20 − 4) · (3 + 2)", "Zwei Klammerpaare, Wert 80", (20 - 4) * (3 + 2) != 50)],
    "Probiere die Klammern. (20 − 4) · 3 + 2 = 16 · 3 + 2 = 48 + 2 = 50. Bei 20 − (4 · 3 + 2) kommt 20 − 14 = 6 heraus, bei 20 − 4 · (3 + 2) kommt 20 − 20 = 0 heraus. (20 − 4 · 3) + 2 ist 8 + 2 = 10: Diese Klammer ändert nichts. (20 − 4) · (3 + 2) ist 16 · 5 = 80 und hat zwei Klammerpaare.",
    (20 - 4) * 3 + 2 == 50), form="umkehren", regel=RR)
neu(T, "klammern", "korrektur", "mehrschritt", W(
    "Vier Terme haben dieselben Zahlen, nur die Klammern stehen verschieden. Welcher Term hat den größten Wert?",
    "(8 + 4) · 5 − 3",
    [("8 + 4 · 5 − 3", "Ohne Klammer: Punkt vor Strich, Wert 25", 8 + 4 * 5 - 3 < (8 + 4) * 5 - 3),
     ("8 + 4 · (5 − 3)", "Klammer um 5 − 3: Wert 16", 8 + 4 * (5 - 3) < (8 + 4) * 5 - 3),
     ("(8 + 4) · (5 − 3)", "Zwei Klammern: Wert 24", (8 + 4) * (5 - 3) < (8 + 4) * 5 - 3)],
    "Rechne alle vier Terme aus. 8 + 4 · 5 − 3 = 8 + 20 − 3 = 25. (8 + 4) · 5 − 3 = 12 · 5 − 3 = 57. 8 + 4 · (5 − 3) = 8 + 8 = 16. (8 + 4) · (5 − 3) = 12 · 2 = 24. Der größte Wert ist 57.",
    (8 + 4) * 5 - 3 == 57), form="zwei_wege", regel=RR)
neu(T, "klammern", "korrektur", "umkehr", Z(
    "Klasse A hat 18 Kinder. Klasse B hat einige Kinder. Zusammen fahren beide Klassen mit 6 gleich vollen Bussen, in jedem Bus sitzen 7 Kinder. Wie viele Kinder hat Klasse B?",
    24, "6 * 7 - 18", lambda: sum(7 for _ in range(6)) - 18,
    "In den 6 Bussen sitzen 6 · 7 = 42 Kinder. Davon gehören 18 zu Klasse A. Also hat Klasse B 42 − 18 = 24 Kinder. Probe: (18 + 24) : 6 = 42 : 6 = 7.",
    [(42, "Nur 6 · 7 gerechnet: alle Kinder statt Klasse B", "6 * 7"), (60, "18 addiert statt abgezogen: 6 · 7 + 18", "6 * 7 + 18"), (3, "Nur Klasse A durch 6 geteilt: 18 : 6", "18 // 6")], einheit="Kinder"), form="umkehren", regel=RR)
neu(T, "klammern", "korrektur", "darstellung", W(
    "Welcher Term passt zu: „Teile die Summe aus 9 und 3 durch 4 und multipliziere das Ergebnis mit 2“?",
    "(9 + 3) : 4 · 2",
    [("9 + 3 : 4 · 2", "Klammer fehlt: dann wird zuerst 3 : 4 · 2 gerechnet (Punkt vor Strich)", (9 + 3) / 4 * 2 != 9 + 3 / 4 * 2),
     ("(9 + 3) : (4 · 2)", "Durch das Produkt 4 · 2 geteilt statt durch 4 und dann mal 2", (9 + 3) / 4 * 2 != (9 + 3) / (4 * 2)),
     ("9 + 3 : (4 · 2)", "Nur 3 geteilt und Summe zuletzt: falsche Reihenfolge", (9 + 3) / 4 * 2 != 9 + 3 / (4 * 2))],
    "Zuerst die Summe: (9 + 3). Diese Summe wird durch 4 geteilt: (9 + 3) : 4. Das Ergebnis wird mit 2 malgenommen: (9 + 3) : 4 · 2 = 12 : 4 · 2 = 3 · 2 = 6. Ohne Klammer würde nur 3 : 4 · 2 zuerst gerechnet; bei (9 + 3) : (4 · 2) würde durch 8 geteilt.",
    (9 + 3) / 4 * 2 == 6), form="bruecke", regel=RR)
neu(T, "klammern", "sicherung", "parameter", W(
    "Bei welchem Term darf man die Klammern weglassen, ohne dass sich der Wert ändert?",
    "(30 − 12) − 4",
    [("30 − (12 − 4)", "Mit Klammer 22, ohne Klammer 14: der Wert ändert sich", 30 - (12 - 4) != 30 - 12 - 4),
     ("2 · (3 + 4)", "Mit Klammer 14, ohne Klammer 10: der Wert ändert sich", 2 * (3 + 4) != 2 * 3 + 4),
     ("20 : (4 · 5)", "Mit Klammer 1, ohne Klammer 25: der Wert ändert sich", 20 // (4 * 5) != 20 // 4 * 5)],
    "Rechne mit und ohne Klammern. (30 − 12) − 4 = 18 − 4 = 14 und 30 − 12 − 4 = 14: gleich, denn von links nach rechts wird sowieso so gerechnet. 30 − (12 − 4) = 22, aber 30 − 12 − 4 = 14. 2 · (3 + 4) = 14, aber 2 · 3 + 4 = 10. 20 : (4 · 5) = 1, aber 20 : 4 · 5 = 25.",
    (30 - 12) - 4 == 30 - 12 - 4 == 14), regel=RR)
neu(T, "klammern", "sicherung", "mehrschritt", Z(
    "Zwei Terme haben dieselben Zahlen: 48 : (6 + 2) · 3 und 48 : 6 + 2 · 3. Um wie viel unterscheiden sich ihre Werte?",
    4, "48 // (6 + 2) * 3 - (48 // 6 + 2 * 3)", lambda: 18 - 14,
    "Erster Term: Klammer zuerst, 6 + 2 = 8. Dann von links: 48 : 8 = 6 und 6 · 3 = 18. Zweiter Term: Punkt vor Strich, 48 : 6 = 8 und 2 · 3 = 6, dann 8 + 6 = 14. Der Unterschied ist 18 − 14 = 4.",
    [(18, "Nur den ersten Term berechnet", "48 // (6 + 2) * 3"), (14, "Nur den zweiten Term berechnet", "48 // 6 + 2 * 3"), (32, "Beide Werte addiert statt abgezogen", "48 // (6 + 2) * 3 + 48 // 6 + 2 * 3")]), form="zwei_wege", regel=RR)
neu(T, "klammern", "sicherung", "begruenden", W(
    "Jonas rechnet 100 − (12 + 8) · 4 von links nach rechts: 100 − 12 = 88, dann 88 + 8 = 96, dann 96 · 4 = 384. Welche Aussage über Jonas’ Rechnung stimmt?",
    "Fehler: Er hat die Klammer nicht zuerst gerechnet. Richtig wäre 100 − 20 · 4 = 100 − 80 = 20.",
    [("Fehler: Er hat die Klammer nicht zuerst gerechnet. Richtig wäre (100 − 20) · 4 = 320.", "Klammer um die ganze Differenz gesetzt: (100 − 20) · 4 = 320", (100 - 20) * 4 != 100 - (12 + 8) * 4),
     ("Fehler: Die Klammer spielt keine Rolle, nur Punkt vor Strich. Richtig wäre 100 − 12 + 8 · 4 = 120.", "Klammer ignoriert: 100 − 12 + 8 · 4 = 120", 100 - 12 + 8 * 4 != 100 - (12 + 8) * 4),
     ("Kein Fehler: Bei einer Rechnung mit Klammer rechnet man immer von links nach rechts.", "Falsche Regel bestätigt: von links nach rechts ergibt 384", 384 != 100 - (12 + 8) * 4)],
    "Die Klammer wird zuerst gerechnet: 12 + 8 = 20. Dann Punkt vor Strich: 20 · 4 = 80. Zuletzt 100 − 80 = 20. Jonas hat von links nach rechts gerechnet und dadurch 384 statt 20 bekommen.",
    100 - (12 + 8) * 4 == 20), regel=RR)
# ═════════ termaufbau ═════════
neu(T, "termaufbau", "test", "transfer", W(
    "Der Term (7 + 5) · 4 − 6 beschreibt eine Geschichte. Welche Geschichte passt?",
    "7 Jungen und 5 Mädchen bekommen je 4 Sticker. 6 Sticker gehen verloren.",
    [("7 Jungen und 5 Mädchen bekommen je 4 Sticker. Dazu kommen noch 6 Sticker.", "Plus statt Minus: (7 + 5) · 4 + 6 = 54", (7 + 5) * 4 + 6 != (7 + 5) * 4 - 6),
     ("7 Jungen bekommen je 4 Sticker und 5 Mädchen bekommen je 6 Sticker.", "Zwei verschiedene Produkte: 7 · 4 + 5 · 6 = 58", 7 * 4 + 5 * 6 != (7 + 5) * 4 - 6),
     ("Es gibt 7 Jungen, 5 Mädchen und 4 Sticker. 6 Sticker gehen verloren.", "Nur zusammengezählt: 7 + 5 + 4 − 6 = 10", 7 + 5 + 4 - 6 != (7 + 5) * 4 - 6)],
    "Die Klammer (7 + 5) sind die 7 Jungen und 5 Mädchen zusammen: 12 Kinder. Sie bekommen je 4 Sticker: (7 + 5) · 4 = 48. Dann gehen 6 Sticker verloren: 48 − 6 = 42. Die anderen Geschichten gehören zu anderen Termen.",
    (7 + 5) * 4 - 6 == 42), form="anwenden", regel=RR)
neu(T, "termaufbau", "korrektur", "umkehr", Z(
    "Auf einem Fest stehen 6 Tische mit je 8 Gästen und 4 Tische mit gleich vielen Gästen. Insgesamt sind 72 Gäste da. Wie viele Gäste sitzen an einem der 4 Tische?",
    6, "(72 - 6 * 8) // 4", lambda: next(g for g in range(1, 50) if 6 * 8 + 4 * g == 72),
    "An den 6 Tischen sitzen 6 · 8 = 48 Gäste. Für die 4 anderen Tische bleiben 72 − 48 = 24 Gäste. Das sind 24 : 4 = 6 Gäste je Tisch. Probe: 6 · 8 + 4 · 6 = 48 + 24 = 72.",
    [(24, "Nur 72 − 6 · 8 gerechnet: alle vier Tische zusammen", "72 - 6 * 8"), (120, "48 addiert statt abgezogen: 72 + 6 · 8", "72 + 6 * 8"), (9, "72 durch 8 geteilt", "72 // 8")], einheit="Gäste"), form="umkehren", regel=RR)
neu(T, "termaufbau", "korrektur", "darstellung", W(
    "Ein Kind schreibt: „Von 40 ziehe ich die Summe aus 9 und 6 ab.“ Welcher Term gehört dazu, und wie groß ist sein Wert?",
    "40 − (9 + 6) = 25",
    [("40 − 9 + 6 = 37", "Klammer weggelassen: 9 wird abgezogen, 6 addiert", 40 - 9 + 6 != 40 - (9 + 6)),
     ("(40 − 9) · 6 = 186", "Mal statt Summe gelesen und anders geklammert", (40 - 9) * 6 != 40 - (9 + 6)),
     ("40 + 9 − 6 = 43", "Plus und Minus vertauscht", 40 + 9 - 6 != 40 - (9 + 6))],
    "„Die Summe aus 9 und 6“ ist 9 + 6 = 15. Sie wird von 40 abgezogen: 40 − (9 + 6) = 40 − 15 = 25. Ohne Klammer, 40 − 9 + 6, würde man nur 9 abziehen und 6 addieren: 37.",
    40 - (9 + 6) == 25), form="bruecke", regel=RR)
neu(T, "termaufbau", "korrektur", "darstellung", W(
    "Mia hat 20 €. Sie kauft 4 Hefte zu je 3 € und 2 Stifte zu je 2 €. Welcher Term gibt an, wie viel Geld ihr bleibt?",
    "20 − (4 · 3 + 2 · 2)",
    [("20 − 4 · 3 + 2 · 2", "Die Stifte addiert statt bezahlt: Wert 12", 20 - 4 * 3 + 2 * 2 != 20 - (4 * 3 + 2 * 2)),
     ("(20 − 4) · 3 − 2 · 2", "4 Hefte von den 20 € abgezogen: Wert 44", (20 - 4) * 3 - 2 * 2 != 20 - (4 * 3 + 2 * 2)),
     ("20 : 4 · 3 − 2 · 2", "Geteilt statt abgezogen: Wert 11", 20 // 4 * 3 - 2 * 2 != 20 - (4 * 3 + 2 * 2))],
    "Die Hefte kosten 4 · 3 € = 12 €, die Stifte 2 · 2 € = 4 €. Zusammen sind das 12 + 4 = 16 €. Es bleiben 20 − 16 = 4 €. Als Term: 20 − (4 · 3 + 2 · 2). Die Klammer braucht man, weil beide Beträge abgezogen werden.",
    20 - (4 * 3 + 2 * 2) == 4), form="bruecke", regel=RR)
neu(T, "termaufbau", "sicherung", "umkehr", Z(
    "Im Parkhaus kostet die erste Stunde 4 €, jede weitere Stunde 2 €. Für ein Auto steht 14 € auf der Rechnung. Wie viele ganze Stunden hat es geparkt?",
    6, "(14 - 4) // 2 + 1", lambda: next(n for n in range(1, 40) if 4 + 2 * (n - 1) == 14),
    "Die erste Stunde kostet 4 €. Die weiteren Stunden kosten zusammen 14 − 4 = 10 €. Das sind 10 : 2 = 5 weitere Stunden. Zusammen 5 + 1 = 6 Stunden. Probe: 4 + 5 · 2 = 14.",
    [(7, "14 durch 2 geteilt: die erste Stunde wie alle anderen gerechnet", "14 // 2"), (5, "Nur die weiteren Stunden gezählt (14 − 4) : 2", "(14 - 4) // 2"), (10, "Nur 14 − 4 gerechnet", "14 - 4")], einheit="Stunden"), form="umkehren", regel=RR)
neu(T, "termaufbau", "sicherung", "begruenden", W(
    "Zum Term 8 + 5 · 3 sagt Maxi: „Ich rechne zuerst 8 + 5, weil das Plus links steht.“ Anna sagt: „Ich rechne zuerst 5 · 3.“ Wer hat recht? Wähle die richtige Begründung.",
    "Anna: Punktrechnung kommt vor Strichrechnung. 5 · 3 = 15, dann 8 + 15 = 23.",
    [("Maxi: Man rechnet immer von links nach rechts. 8 + 5 = 13, dann 13 · 3 = 39.", "Strich vor Punkt gerechnet, weil das Plus links steht (39)", (8 + 5) * 3 != 8 + 5 * 3),
     ("Beide: Die Reihenfolge ist egal, es kommt immer dasselbe heraus.", "Reihenfolge für beliebig gehalten (23 gegen 39)", (8 + 5) * 3 != 8 + 5 * 3),
     ("Anna: Man rechnet immer zuerst die größeren Zahlen.", "Nicht die Größe der Zahlen entscheidet: in 20 + 2 · 3 wird 2 · 3 zuerst gerechnet", 20 + 2 * 3 == 26)],
    "Punktrechnung (mal, geteilt) wird vor Strichrechnung (plus, minus) gerechnet. Also 5 · 3 = 15 und danach 8 + 15 = 23. Maxi bekommt mit seiner Reihenfolge 39, das ist falsch. Die Größe der Zahlen spielt keine Rolle: In 20 + 2 · 3 rechnet man auch zuerst 2 · 3.",
    8 + 5 * 3 == 23), regel=RR)
neu(T, "termaufbau", "sicherung", "transfer", Z(
    "Ein Verein bestellt 12 T-Shirts zu je 9 € und 8 T-Shirts zu je 11 €. Auf die ganze Rechnung gibt es 20 € Rabatt. Vier Freunde teilen den Rechnungsbetrag gleichmäßig. Wie viel Euro zahlt jeder?",
    44, "(12 * 9 + 8 * 11 - 20) // 4", lambda: (sum([9] * 12) + sum([11] * 8) - 20) / 4,
    "Erste Sorte: 12 · 9 = 108 €. Zweite Sorte: 8 · 11 = 88 €. Zusammen 108 + 88 = 196 €. Nach dem Rabatt: 196 − 20 = 176 €. Geteilt durch 4: 44 €. Als Term: (12 · 9 + 8 · 11 − 20) : 4.",
    [(191, "Nur den Rabatt durch 4 geteilt: 12 · 9 + 8 · 11 − 20 : 4", "12 * 9 + 8 * 11 - 20 // 4"), (29, "Erst den Betrag durch 4 geteilt, dann 20 € abgezogen", "(12 * 9 + 8 * 11) // 4 - 20"), (176, "Nach dem Rabatt nicht durch die Zahl der Freunde geteilt", "12 * 9 + 8 * 11 - 20")], einheit="€"), form="anwenden", regel=RR)
# ═════════ vorteil ═════════
neu(T, "vorteil", "test", "begruenden", W(
    "Du sollst 47 + 38 + 53 ausrechnen. Du rechnest erst 47 + 53 = 100 und dann 100 + 38. Welche Begründung zeigt, warum das erlaubt ist?",
    "Beim Addieren darf man die Summanden vertauschen und neu zusammenfassen. Die Summe bleibt gleich.",
    [("Das geht nur, weil 47 + 53 genau 100 ergibt. Bei anderen Zahlen darf man nicht umstellen.", "Erlaubnis an glatte Zahlen gebunden (41 + 38 + 59 = 41 + 59 + 38 geht auch)", 41 + 38 + 59 == 41 + 59 + 38),
     ("Klammern werden immer zuerst gerechnet, auch wenn gar keine da sind.", "Falsche Regel: hier steht keine Klammer, und die Reihenfolge der Summanden ist das Thema", None),
     ("Beim Addieren wird immer von rechts nach links gerechnet.", "Falsche Regel über die Richtung des Rechnens", None)],
    "In einer Summe dürfen die Summanden getauscht und anders zusammengefasst werden: 47 + 38 + 53 = 47 + 53 + 38 = 100 + 38 = 138. Das gilt für alle Zahlen, nicht nur für glatte. Glatte Zahlen wie 47 + 53 = 100 machen die Rechnung nur leichter.",
    47 + 38 + 53 == 47 + 53 + 38 == 138), regel=RT)
neu(T, "vorteil", "korrektur", "mehrschritt", W(
    "Ohne auszurechnen: Welcher Term hat denselben Wert wie 37 + 58 + 63?",
    "63 + 37 + 58",
    [("58 − 37 + 63", "Das Minus gehört nicht dorthin: Wert 84 statt 158", 58 - 37 + 63 != 37 + 58 + 63),
     ("37 + 63 − 58", "Das Plus vor 58 zum Minus geworden: Wert 42", 37 + 63 - 58 != 37 + 58 + 63),
     ("37 + 58 − 63", "Das Plus vor 63 zum Minus geworden: Wert 32", 37 + 58 - 63 != 37 + 58 + 63)],
    "Bei einer reinen Plus-Rechnung darf man die Summanden tauschen, jeder nimmt sein Plus mit: 63 + 37 + 58 = 158 = 37 + 58 + 63. In den anderen Termen steht ein Minus, das den Wert ändert.",
    63 + 37 + 58 == 37 + 58 + 63), form="verfahren_waehlen", regel=RT)
neu(T, "vorteil", "korrektur", "umkehr", Z(
    "Eine Schachtel enthält 20 Pralinen. 5 Schachteln kommen in ein Paket. Ein Händler erhält Pakete mit zusammen 1 500 Pralinen. Wie viele Pakete sind das?",
    15, "1500 // (20 * 5)", lambda: next(n for n in range(1, 100) if n * 5 * 20 == 1500),
    "Ein Paket enthält 5 · 20 = 100 Pralinen. 1 500 : 100 = 15. Es sind 15 Pakete. Geschickt: erst 20 · 5 = 100 zusammenfassen, dann teilen.",
    [(75, "Nur durch 20 geteilt: das sind Schachteln, nicht Pakete", "1500 // 20"), (300, "Nur durch 5 geteilt", "1500 // 5"), (1475, "20 und 5 abgezogen", "1500 - 20 - 5")], einheit="Pakete"), form="umkehren", regel=RT)
neu(T, "vorteil", "korrektur", "mehrschritt", W(
    "Mia und Tim rechnen 50 · 37 · 2. Mia rechnet zuerst 50 · 37. Tim rechnet zuerst 50 · 2. Welche Aussage stimmt?",
    "Beide bekommen 3 700. Tims Weg ist bequemer, weil 50 · 2 = 100 ist.",
    [("Mia bekommt ein anderes Ergebnis, weil sie die Reihenfolge der Faktoren nicht geändert hat.", "Reihenfolge für das Ergebnis entscheidend gehalten", 50 * 37 * 2 == 50 * 2 * 37),
     ("Tim bekommt ein anderes Ergebnis, weil er die Faktoren vertauscht hat.", "Vertauschen beim Malnehmen für verboten gehalten", 50 * 2 * 37 == 50 * 37 * 2),
     ("Beide bekommen dasselbe, aber nur, weil 37 eine ungerade Zahl ist.", "Falsche Begründung: es gilt für alle Zahlen", 50 * 38 * 2 == 50 * 2 * 38)],
    "Beim Malnehmen darf man die Faktoren tauschen. Mia: 50 · 37 = 1 850, dann 1 850 · 2 = 3 700. Tim: 50 · 2 = 100, dann 100 · 37 = 3 700. Beide bekommen 3 700, bei Tim ist die Rechnung leichter. Es gilt für alle Zahlen, nicht nur für ungerade.",
    50 * 37 * 2 == 3700 == 50 * 2 * 37), form="zwei_wege", regel=RT)
neu(T, "vorteil", "sicherung", "umkehr", Z(
    "Jule rechnet geschickt: 38 + □ + 62 = 150. Welche Zahl steht im Kästchen?",
    50, "150 - (38 + 62)", lambda: next(x for x in range(0, 200) if 38 + x + 62 == 150),
    "Fasse zuerst 38 + 62 = 100 zusammen. Dann muss □ + 100 = 150 gelten, also □ = 150 − 100 = 50. Probe: 38 + 50 + 62 = 150.",
    [(88, "Nur 62 abgezogen: 150 − 62", "150 - 62"), (112, "Nur 38 abgezogen: 150 − 38", "150 - 38"), (188, "38 addiert statt abgezogen: 150 + 38", "150 + 38")]), form="umkehren", regel=RT)
neu(T, "vorteil", "sicherung", "begruenden", W(
    "Ben rechnet 2 · 37 · 50 so: 2 · 50 · 37 = 100 + 37 = 137. Welche Aussage über Bens Rechnung stimmt?",
    "Fehler: Nach 2 · 50 = 100 muss mal 37 gerechnet werden, nicht plus. Richtig wäre 100 · 37 = 3 700.",
    [("Fehler: Er darf 37 und 50 nicht vertauschen. Richtig wäre 2 · 37 · 50 = 74 · 50 = 3 800.", "Vertauschen für verboten gehalten; außerdem 74 · 50 falsch (3 700)", 74 * 50 != 3800),
     ("Kein Fehler: Nach dem Vertauschen wird addiert, also 100 + 37 = 137.", "Aus dem Malzeichen ein Pluszeichen gemacht", 100 + 37 != 2 * 37 * 50),
     ("Fehler: Er hätte 2 + 37 + 50 rechnen müssen. Richtig wäre 89.", "Mal und Plus verwechselt (2 + 37 + 50 = 89)", 2 + 37 + 50 != 2 * 37 * 50)],
    "Die Faktoren darf man tauschen: 2 · 37 · 50 = 2 · 50 · 37. Dann 2 · 50 = 100 und 100 · 37 = 3 700. Ben hat nach dem Tauschen aus dem Mal ein Plus gemacht (100 + 37 = 137).",
    100 * 37 == 3700 == 2 * 37 * 50), regel=RT)
neu(T, "vorteil", "sicherung", "pruefung", W(
    "Welche Aussage über die Werte von 36 · 25 · 4 und 18 · 25 · 8 stimmt?",
    "Beide Werte sind gleich, denn 36 · 4 = 144 und 18 · 8 = 144, und beim Malnehmen darf man die Faktoren tauschen.",
    [("18 · 25 · 8 ist größer, weil 8 größer als 4 ist.", "Nur zwei Faktoren verglichen (8 gegen 4)", 36 * 25 * 4 == 18 * 25 * 8),
     ("36 · 25 · 4 ist größer, weil 36 größer als 18 ist.", "Nur zwei Faktoren verglichen (36 gegen 18)", 36 * 25 * 4 == 18 * 25 * 8),
     ("Beide Werte sind gleich, weil in beiden Termen 25 vorkommt.", "Falsche Begründung: mit 18 · 25 · 9 wäre der Wert anders", 36 * 25 * 4 != 18 * 25 * 9)],
    "Tausche die Faktoren: 36 · 25 · 4 = 36 · 4 · 25 = 144 · 25 und 18 · 25 · 8 = 18 · 8 · 25 = 144 · 25. Beide Werte sind 3 600. Dass 25 in beiden Termen vorkommt, ist kein Grund: Mit 18 · 25 · 9 wäre der Wert 4 050.",
    36 * 25 * 4 == 18 * 25 * 8 == 3600), form="zwei_wege", regel=RT)
# ═════════ verteilen ═════════
neu(T, "verteilen", "test", "begruenden", W(
    "Ein Rechteck ist 8 cm hoch. Es ist in zwei Teile geteilt, die 30 cm und 2 cm breit sind. Anna rechnet 8 · 30 + 8 · 2. Ben rechnet 8 · 32. Beide kommen auf dasselbe Ergebnis. Welche Begründung ist richtig?",
    "Beide Rechnungen berechnen die Fläche desselben Rechtecks: Anna addiert die zwei Teilflächen, Ben rechnet die ganze Fläche.",
    [("Weil 8 · 30 + 2 dasselbe ist wie 8 · 32.", "Nur die 30 mit 8 malgenommen: 8 · 30 + 2 = 242, nicht 256", 8 * 30 + 2 != 8 * 32),
     ("Das stimmt nur zufällig bei 30 und 2. Mit 31 und 1 kommt etwas anderes heraus.", "Zufall behauptet; mit 31 und 1 kommt dasselbe heraus", 8 * 31 + 8 * 1 == 8 * 32),
     ("Weil 242 und 256 ungefähr gleich groß sind.", "Unterschied für klein gehalten, die Werte sind aber verschieden", 242 != 256)],
    "Die ganze Fläche ist 8 · 32 = 256 cm². Die Teilflächen sind 8 · 30 = 240 cm² und 8 · 2 = 16 cm². 240 + 16 = 256. Es ist dasselbe Rechteck, einmal als Ganzes und einmal in zwei Teilen gerechnet. Das gilt für jede Zerlegung der Breite.",
    8 * 30 + 8 * 2 == 8 * 32 == 256), regel=RA)
neu(T, "verteilen", "korrektur", "umkehr", Z(
    "Das Ergebnis von 17 · □ + 17 · 14 ist so groß wie 17 · 50. Welche Zahl steht im Kästchen?",
    36, "50 - 14", lambda: next(x for x in range(0, 100) if 17 * x + 17 * 14 == 17 * 50),
    "Klammere 17 aus: 17 · (□ + 14) = 17 · 50. Dann muss □ + 14 = 50 gelten, also □ = 50 − 14 = 36. Probe: 17 · 36 + 17 · 14 = 612 + 238 = 850 = 17 · 50.",
    [(64, "14 addiert statt abgezogen: 50 + 14", "50 + 14"), (700, "50 mit 14 malgenommen", "50 * 14"), (850, "17 · 50 als Zahl im Kästchen genannt", "17 * 50")]), form="umkehren", regel=RA)
neu(T, "verteilen", "korrektur", "darstellung", W(
    "In einem Beet gibt es 9 Reihen. In jeder Reihe stehen erst 6 rote und dann 4 gelbe Blumen. Welche Rechnung gibt die Zahl aller Blumen an?",
    "9 · (6 + 4)",
    [("9 · 6 + 4", "Nur die roten Blumen mit 9 malgenommen: Wert 58", 9 * 6 + 4 != 9 * (6 + 4)),
     ("9 + 6 · 4", "Plus und Mal vertauscht: Wert 33", 9 + 6 * 4 != 9 * (6 + 4)),
     ("(9 + 6) · 4", "Falsch geklammert: Wert 60", (9 + 6) * 4 != 9 * (6 + 4))],
    "Jede Reihe hat 6 + 4 = 10 Blumen. Bei 9 Reihen sind das 9 · (6 + 4) = 9 · 10 = 90 Blumen. Man kann auch 9 · 6 + 9 · 4 = 54 + 36 rechnen. Bei 9 · 6 + 4 würden die gelben Blumen nur einmal gezählt.",
    9 * (6 + 4) == 90 == 9 * 6 + 9 * 4), form="bruecke", regel=RA)
neu(T, "verteilen", "korrektur", "umkehr", Z(
    "Eine Zahl wird mit 8 malgenommen. Dieselbe Zahl wird mit 12 malgenommen. Beide Ergebnisse zusammen sind 200. Welche Zahl ist es?",
    10, "200 // (8 + 12)", lambda: next(x for x in range(1, 200) if 8 * x + 12 * x == 200),
    "8 · □ + 12 · □ = (8 + 12) · □ = 20 · □. Es muss 20 · □ = 200 gelten, also □ = 200 : 20 = 10. Probe: 80 + 120 = 200.",
    [(25, "Nur durch 8 geteilt", "200 // 8"), (16, "Nur durch 12 geteilt", "200 // 12"), (180, "20 von 200 abgezogen", "200 - (8 + 12)")]), form="umkehren", regel=RA)
neu(T, "verteilen", "sicherung", "darstellung", W(
    "Ein Rechteck hat die Höhe 9 cm. Es ist in zwei Teile mit den Breiten 20 cm und 3 cm geteilt. Welche Rechnung gibt die Gesamtfläche NICHT richtig an?",
    "9 · 20 + 3",
    [("9 · 23", "Ganze Breite 23 cm mit der Höhe malgenommen: stimmt (207)", 9 * 23 == 9 * 20 + 9 * 3),
     ("9 · 20 + 9 · 3", "Beide Teilflächen addiert: stimmt (207)", 9 * 20 + 9 * 3 == 9 * 23),
     ("180 + 27", "Teilflächen schon ausgerechnet und addiert: stimmt (207)", 180 + 27 == 9 * 23)],
    "Die Gesamtfläche ist 9 · 23 = 207 cm². Die Teilflächen sind 9 · 20 = 180 cm² und 9 · 3 = 27 cm²: 180 + 27 = 207. Bei 9 · 20 + 3 wird die 9 nur mit 20 malgenommen. Das ergibt 183 und ist falsch.",
    9 * 20 + 3 == 183 != 207), form="bruecke", regel=RA)
neu(T, "verteilen", "sicherung", "transfer", Z(
    "Berechne mit einem Rechenvorteil: 19 · 36 + 19 · 64 − 19 · 50.",
    950, "19 * (36 + 64 - 50)", lambda: 19 * 100 // 2,
    "Alle drei Teile haben den Faktor 19. Ausklammern: 19 · (36 + 64 − 50) = 19 · 50 = 950.",
    [(1850, "Beim letzten Teil die 19 vergessen: 19 · 36 + 19 · 64 − 50", "19 * 36 + 19 * 64 - 50"), (698, "Nur beim ersten Teil mit 19 malgenommen", "19 * 36 + 64 - 50"), (50, "Die 19 ganz vergessen: 36 + 64 − 50", "36 + 64 - 50")]), form="anwenden", regel=RA)
neu(T, "verteilen", "sicherung", "begruenden", W(
    "Tom klammert aus: 15 · 7 + 15 · 9 = 15 · (7 · 9) = 945. Welche Aussage über Toms Rechnung stimmt?",
    "Fehler: In der Klammer muss ein Plus stehen, kein Mal. Richtig wäre 15 · (7 + 9) = 240.",
    [("Fehler: Die 15 darf man nicht ausklammern. Richtig wäre 15 · 7 + 9 = 114.", "Ausklammern für verboten gehalten: 15 · 7 + 9 = 114", 15 * 7 + 9 != 15 * 7 + 15 * 9),
     ("Fehler: Die 15 muss in der Klammer noch einmal mit 7 und 9 malgenommen werden: 15 · (15 · 7 + 15 · 9) = 3 600.", "Die 15 doppelt verwendet: 3 600", 15 * (15 * 7 + 15 * 9) != 15 * 7 + 15 * 9),
     ("Kein Fehler: Beim Ausklammern wird aus Plus ein Mal.", "Falsche Regel bestätigt (945)", 15 * 7 * 9 != 15 * 7 + 15 * 9)],
    "15 · 7 + 15 · 9 = 15 · (7 + 9) = 15 · 16 = 240. Beim Ausklammern bleibt das Rechenzeichen zwischen den Summanden ein Plus. Tom hat 7 · 9 = 63 und 15 · 63 = 945 gerechnet.",
    15 * (7 + 9) == 240 == 15 * 7 + 15 * 9), regel=RA)
# ═════════ umkehraufgabe_mal ═════════
neu(T, "umkehraufgabe_mal", "test", "rueckwaerts", Z(
    "Eine Rechenmaschine macht mit jeder eingegebenen Zahl nacheinander drei Schritte: mal 5, plus 12, geteilt durch 4. Am Ende zeigt sie 8 an. Welche Zahl wurde eingegeben?",
    4, "(8 * 4 - 12) // 5", lambda: next(x for x in range(0, 100) if (x * 5 + 12) / 4 == 8),
    "Rückwärts, der letzte Schritt zuerst: Geteilt durch 4 kehrt man mit Mal 4 um: 8 · 4 = 32. Plus 12 kehrt man mit Minus 12 um: 32 − 12 = 20. Mal 5 kehrt man mit Geteilt durch 5 um: 20 : 5 = 4. Probe: 4 · 5 = 20, 20 + 12 = 32, 32 : 4 = 8.",
    [(20, "Das Teilen durch 5 vergessen: 8 · 4 − 12", "8 * 4 - 12"), (44, "Plus statt Minus bei der Umkehrung: 8 · 4 + 12", "8 * 4 + 12"), (32, "Nur das Teilen durch 4 umgekehrt: 8 · 4", "8 * 4")]), form="umkehren", regel=RG)
neu(T, "umkehraufgabe_mal", "korrektur", "umkehr", W(
    "Bei 36 : □ = 9 suchst du die Zahl im Kästchen. Welche Rechnung führt zu ihr?",
    "36 : 9",
    [("36 · 9", "Mal statt geteilt: 324", 36 * 9 != 4),
     ("36 − 9", "Minus statt geteilt: 27", 36 - 9 != 4),
     ("9 : 36", "Die Zahlen vertauscht: 9 : 36 ist keine natürliche Zahl", 9 % 36 != 0)],
    "Gesucht ist die Zahl, durch die man 36 teilen muss, um 9 zu erhalten. Das ist 36 : 9 = 4. Probe: 36 : 4 = 9. Mit 36 · 9 = 324 und 36 − 9 = 27 würde die Probe nicht stimmen.",
    36 // 9 == 4 and 36 // 4 == 9), form="umkehren", regel=RG)
neu(T, "umkehraufgabe_mal", "korrektur", "umkehr", Z(
    "Beim Sportfest laufen 5 Staffeln mit gleich vielen Kindern. Dazu kommen 3 Ersatzkinder. Insgesamt sind 43 Kinder da. Wie viele Kinder laufen in einer Staffel?",
    8, "(43 - 3) // 5", lambda: next(x for x in range(1, 50) if 5 * x + 3 == 43),
    "Ohne die 3 Ersatzkinder sind es 43 − 3 = 40 Kinder. Sie verteilen sich auf 5 Staffeln: 40 : 5 = 8. Probe: 5 · 8 + 3 = 43.",
    [(40, "Das Teilen durch 5 vergessen: 43 − 3", "43 - 3"), (46, "Die Ersatzkinder addiert statt abgezogen: 43 + 3", "43 + 3"), (9, "Nur 43 durch 5 geteilt und aufgerundet", "(43 + 4) // 5")], einheit="Kinder"), form="umkehren", regel=RG)
neu(T, "umkehraufgabe_mal", "korrektur", "umkehr", W(
    "Welche Gleichung hat dieselbe Lösung wie 7 · x = 56?",
    "56 : x = 7",
    [("x : 7 = 56", "Geteilt statt mal: Lösung wäre 392", 56 * 7 != 8),
     ("x · 56 = 7", "Die Zahlen vertauscht: keine natürliche Lösung", 7 % 56 != 0),
     ("x : 8 = 56", "Die Lösung 8 mit der 56 verwechselt: Lösung wäre 448", 56 * 8 != 8)],
    "Aus 7 · x = 56 folgt x = 56 : 7 = 8. Bei 56 : x = 7 ist x = 56 : 7 = 8 ebenfalls. Bei x : 7 = 56 wäre x = 56 · 7 = 392, bei x · 56 = 7 gibt es keine natürliche Lösung, bei x : 8 = 56 wäre x = 448.",
    7 * 8 == 56 and 56 // 8 == 7), form="umkehren", regel=RG)
neu(T, "umkehraufgabe_mal", "sicherung", "darstellung", W(
    "Zu welcher Geschichte gehört die Gleichung 48 : x = 6?",
    "48 Murmeln werden gleichmäßig auf einige Kinder verteilt. Jedes Kind bekommt 6. Wie viele Kinder sind es?",
    [("Jedes Kind bekommt 48 Murmeln. Es gibt 6 Kinder. Wie viele Murmeln sind es?", "Mal statt geteilt: 48 · 6", 48 * 6 != 48 // 6),
     ("Ein Kind hat 48 Murmeln und verliert 6. Wie viele bleiben?", "Minus statt geteilt: 48 − 6", 48 - 6 != 48 // 6),
     ("6 Kinder teilen sich eine Zahl von Murmeln. Jedes bekommt 48. Wie viele Murmeln sind es?", "Zahlen vertauscht: x : 6 = 48", 48 * 6 != 48 // 6)],
    "48 : x = 6 heißt: 48 wird durch x geteilt, jeder Teil ist 6. Das passt zu 48 Murmeln, die gleichmäßig verteilt werden, wobei jedes Kind 6 bekommt. x = 48 : 6 = 8 Kinder. Die anderen Geschichten gehören zu 48 · 6, 48 − 6 und x : 6 = 48.",
    48 // 8 == 6), form="bruecke", regel=RG)
neu(T, "umkehraufgabe_mal", "sicherung", "begruenden", W(
    "Warum hat die Gleichung 7 · x = 50 keine Lösung unter den natürlichen Zahlen? Wähle die richtige Begründung.",
    "Weil 50 nicht in der 7er-Reihe steht: 49 und 56 liegen links und rechts davon.",
    [("Weil 50 gerade und 7 ungerade ist.", "Gerade Ergebnisse sind möglich: 7 · 2 = 14", 7 * 2 == 14),
     ("Weil man 50 nicht durch 7 teilen darf.", "Teilen durch 7 ist erlaubt, es geht nur nicht auf", 50 % 7 == 1),
     ("Weil x größer als 50 sein müsste.", "x wäre kleiner als 50, nicht größer", 50 // 7 < 50)],
    "Die 7er-Reihe lautet 7, 14, 21, 28, 35, 42, 49, 56. Die 50 steht nicht darin. 50 : 7 geht nicht ohne Rest auf (7 · 7 = 49, Rest 1). Gerade und ungerade Zahlen spielen keine Rolle, und durch 7 teilen darf man.",
    7 * 7 == 49 and 7 * 8 == 56), regel=RG)
neu(T, "umkehraufgabe_mal", "sicherung", "parameter", Z(
    "Für wie viele natürliche Zahlen a von 1 bis 12 (beide Grenzen eingeschlossen) hat die Gleichung a · x = 36 eine Lösung in den natürlichen Zahlen?",
    7, "7", lambda: sum(1 for a in range(1, 13) if 36 % a == 0),
    "Die Gleichung hat genau dann eine Lösung, wenn 36 in der a-er-Reihe steht, also wenn a ein Teiler von 36 ist. Die Teiler von 36 bis 12 sind 1, 2, 3, 4, 6, 9 und 12. Das sind 7 Zahlen.",
    [(6, "Den Teiler 12 nicht mitgezählt (die Grenze gilt einschließlich): 7 − 1", "7 - 1"), (12, "Alle Zahlen von 1 bis 12 gezählt: 13 − 1", "13 - 1")]), form="umkehren", regel=RG)
# ═════════ ueberschlag ═════════
neu(T, "ueberschlag", "test", "begruenden", W(
    "Tim hat 612 · 49 ausgerechnet und 2 998 erhalten. Welcher Überschlag zeigt am schnellsten, dass das nicht stimmen kann, und warum?",
    "600 · 50 = 30 000. Das ist rund zehnmal so viel wie 2 998. Tim hat sich um eine Stelle verrechnet.",
    [("Die letzten Ziffern: 2 · 9 = 18, das Ergebnis muss auf 8 enden. 2 998 endet auf 8, also stimmt es.", "Endziffer passt, aber das ist nur eine notwendige Bedingung (2 998 ist trotzdem falsch)", 612 * 49 != 2998),
     ("600 + 50 = 650, also muss das Ergebnis ungefähr 650 sein.", "Plus statt Mal überschlagen", 612 * 49 != 650),
     ("Ein Überschlag kann nie zeigen, dass ein Ergebnis falsch ist. Dafür muss man genau nachrechnen.", "Überschlag für nutzlos gehalten, dabei ist 30 000 weit weg von 2 998", abs(600 * 50 - 2998) > 10000)],
    "Runde die Faktoren: 612 ≈ 600 und 49 ≈ 50. 600 · 50 = 30 000. Das genaue Ergebnis muss nahe bei 30 000 liegen (es ist 29 988). Tims 2 998 ist zehnmal zu klein. Die Endziffer 8 passt zwar, beweist aber nichts. Mit 600 + 50 wurde falsch gerechnet.",
    600 * 50 == 30000 and 612 * 49 == 29988), regel=RB)
neu(T, "ueberschlag", "korrektur", "umkehr", Z(
    "Eine Lehrerin überschlägt die Kosten für den Museumsbesuch ihrer Klasse: Sie rundet die Kinderzahl auf Zehner (ab 5 wird aufgerundet) und rechnet mit 7 € Eintritt je Kind. Ihr Überschlag ergibt 210 €. Wie viele Kinder kann die Klasse höchstens haben?",
    34, "30 + 4", lambda: max(n for n in range(1, 200) if (n + 5) // 10 * 10 * 7 == 210),
    "210 : 7 = 30. Die Kinderzahl wurde also auf 30 gerundet. Auf 30 runden alle Zahlen von 25 bis 34. Die größte ist 34 Kinder (35 würde auf 40 aufgerundet).",
    [(30, "Die gerundete Zahl genannt: 210 : 7", "210 // 7"), (35, "Eine zu viel: 30 + 5, aber 35 wird schon aufgerundet", "30 + 5"), (29, "Eine zu wenig als gerundete Zahl: 30 − 1", "30 - 1")], einheit="Kinder"), form="umkehren", regel=RB)
neu(T, "ueberschlag", "korrektur", "mehrschritt", W(
    "Welcher Überschlag liegt am nächsten am genauen Ergebnis von 39 · 52?",
    "40 · 50",
    [("30 · 50", "Beide Zahlen abgerundet, 39 zu stark: weit unter dem genauen Ergebnis", abs(30 * 50 - 39 * 52) > abs(40 * 50 - 39 * 52)),
     ("40 · 60", "52 auf 60 statt auf 50 gerundet", abs(40 * 60 - 39 * 52) > abs(40 * 50 - 39 * 52)),
     ("40 · 5", "Eine Null vergessen: weit entfernt", abs(40 * 5 - 39 * 52) > abs(40 * 50 - 39 * 52))],
    "Runde auf Zehner: 39 ≈ 40 und 52 ≈ 50. 40 · 50 = 2 000. Das genaue Ergebnis ist 2 028, der Abstand ist 28. Bei 30 · 50 = 1 500 ist der Abstand 528, bei 40 · 60 = 2 400 ist er 372, bei 40 · 5 = 200 ist er 1 828.",
    39 * 52 == 2028 and abs(40 * 50 - 2028) == 28), form="verfahren_waehlen", regel=RB)
neu(T, "ueberschlag", "korrektur", "mehrschritt", Z(
    "Mia überschlägt 48 · 52 mit 50 · 50. Tom überschlägt mit 40 · 50. Das genaue Ergebnis ist größer als Toms Überschlag, aber kleiner als Mias. Um wie viel liegt Toms Überschlag weiter vom genauen Ergebnis entfernt als Mias?",
    492, "(52 * 48 - 40 * 50) - (50 * 50 - 52 * 48)", lambda: abs(2496 - 2000) - abs(2500 - 2496),
    "Genau: 48 · 52 = 2 496. Mia: 50 · 50 = 2 500, Abstand 4. Tom: 40 · 50 = 2 000, Abstand 496. Der Unterschied der Abstände ist 496 − 4 = 492.",
    [(496, "Nur Toms Abstand angegeben: 2 496 − 2 000", "52 * 48 - 40 * 50"), (4, "Nur Mias Abstand angegeben: 2 500 − 2 496", "50 * 50 - 52 * 48"), (500, "Die beiden Überschläge verglichen: 2 500 − 2 000", "50 * 50 - 40 * 50")]), form="zwei_wege", regel=RB)
neu(T, "ueberschlag", "sicherung", "mehrschritt", Z(
    "Die Summe 396 + 612 + 1 987 wird überschlagen: Jede Zahl wird auf Hunderter gerundet. Um wie viel weicht der Überschlag vom genauen Ergebnis ab?",
    5, "(400 + 600 + 2000) - (396 + 612 + 1987)", lambda: abs((400 + 600 + 2000) - sum([396, 612, 1987])),
    "Überschlag: 400 + 600 + 2 000 = 3 000. Genau: 396 + 612 + 1 987 = 2 995. Der Unterschied ist 5. Die Rundungen gleichen sich teilweise aus: 4 zu viel, 12 zu wenig, 13 zu viel.",
    [(3000, "Nur den Überschlag genannt", "400 + 600 + 2000"), (2995, "Nur das genaue Ergebnis genannt", "396 + 612 + 1987"), (29, "Die Abweichungen der drei Zahlen ohne Vorzeichen addiert", "4 + 12 + 13")]), form="zwei_wege", regel=RB)
neu(T, "ueberschlag", "sicherung", "begruenden", W(
    "Mia hat 596 · 12 = 7 152 gerechnet. Zur Kontrolle überschlägt sie 600 · 10 = 6 000 und sagt: „Das passt nicht, 7 152 ist falsch.“ Welche Aussage über Mias Kontrolle stimmt?",
    "Fehler: Sie hat 12 zu grob auf 10 gerundet. Richtig wäre 600 · 12 = 7 200, und das passt zu 7 152.",
    [("Fehler: Sie hätte 596 auf 500 runden müssen. Dann wäre 500 · 12 = 6 000 der richtige Überschlag.", "Zu grob gerundet (500 statt 600)", abs(500 * 12 - 7152) > abs(600 * 12 - 7152)),
     ("Kein Fehler: Der Überschlag 6 000 zeigt, dass 7 152 nicht stimmen kann.", "Unterschied zwischen Überschlag und Ergebnis nicht auf die grobe Rundung bezogen", 596 * 12 == 7152),
     ("Fehler: Beim Überschlag darf man nur eine Zahl runden. Dann ist 596 · 10 = 5 960 richtig.", "Falsche Regel: auch eine einzelne grobe Rundung bleibt grob", abs(596 * 10 - 7152) > abs(600 * 12 - 7152))],
    "Ein guter Überschlag liegt nahe am genauen Ergebnis. 12 auf 10 zu runden ist zu grob (zwei von zwölf sind 17 % Abweichung). Mit 600 · 12 = 7 200 liegt der Überschlag nahe bei 7 152. Tatsächlich ist 596 · 12 = 7 152 richtig.",
    596 * 12 == 7152 and 600 * 12 == 7200), regel=RB)
neu(T, "ueberschlag", "sicherung", "parameter", Z(
    "Eine natürliche Zahl wird kaufmännisch auf Hunderter gerundet (ab 50 wird aufgerundet) und ergibt 4 600. Wie viele natürliche Zahlen kommen dafür infrage?",
    100, "4649 - 4550 + 1", lambda: sum(1 for n in range(0, 10000) if (n + 50) // 100 * 100 == 4600),
    "Auf 4 600 runden alle Zahlen von 4 550 bis 4 649 (4 550 wird noch aufgerundet, 4 650 schon auf 4 700). Das sind 4 649 − 4 550 + 1 = 100 Zahlen.",
    [(99, "Eine zu wenig: 4 649 − 4 550 ohne die erste Zahl mitzuzählen", "4649 - 4550"), (50, "Nur die Zahlen von 4 550 bis 4 599 gezählt", "4599 - 4550 + 1"), (101, "Eine zu viel: auch 4 650 mitgezählt", "4650 - 4550 + 1")]), form="umkehren", regel=RB)
# ═════════ sach ═════════
neu(T, "sach", "test", "rueckwaerts", Z(
    "In einem Zug steigen an der ersten Haltestelle 14 Fahrgäste aus. An der zweiten Haltestelle steigt die Hälfte der übrigen Fahrgäste aus. An der dritten steigen 8 Fahrgäste ein. Danach sind 20 Fahrgäste im Zug. Wie viele Fahrgäste waren vor der ersten Haltestelle im Zug?",
    38, "(20 - 8) * 2 + 14", lambda: next(n for n in range(1, 200) if (n - 14) % 2 == 0 and (n - 14) // 2 + 8 == 20),
    "Rückwärts, der letzte Schritt zuerst. Vor der dritten Haltestelle: 20 − 8 = 12 Fahrgäste. Nach der ersten waren es doppelt so viele wie nach der zweiten: 12 · 2 = 24. Vor der ersten: 24 + 14 = 38. Probe: 38 − 14 = 24, die Hälfte steigt aus: 12, dann +8 = 20.",
    [(26, "Das Halbieren nicht umgekehrt: 20 − 8 + 14", "20 - 8 + 14"), (70, "Die 8 addiert statt abgezogen: (20 + 8) · 2 + 14", "(20 + 8) * 2 + 14"), (34, "Nur 20 + 14 gerechnet", "20 + 14")], einheit="Fahrgäste"), form="umkehren", regel=RG)
neu(T, "sach", "korrektur", "umkehr", Z(
    "Zoe hat 24 € in ihrer Spardose. Sie legt 7 Wochen lang jede Woche denselben Betrag hinein. Danach sind 66 € in der Dose. Wie viel Euro legt sie pro Woche hinein?",
    6, "(66 - 24) // 7", lambda: next(x for x in range(1, 50) if 24 + 7 * x == 66),
    "Gespart hat sie 66 − 24 = 42 €. Das verteilt sich auf 7 Wochen: 42 : 7 = 6. Probe: 24 + 7 · 6 = 66.",
    [(42, "Das Teilen durch 7 vergessen: 66 − 24", "66 - 24"), (90, "Die 24 € addiert statt abgezogen: 66 + 24", "66 + 24"), (9, "Nur 66 durch 7 geteilt (ganzzahlig)", "66 // 7")], einheit="€"), form="umkehren", regel=RG)
neu(T, "sach", "korrektur", "darstellung", W(
    "Ein Kind hat am Anfang einen Betrag □. Es kauft 3 Eis zu je 2 €. Dann bekommt es 5 € geschenkt. Jetzt hat es 20 €. Welche Gleichung beschreibt die Geschichte?",
    "□ − 3 · 2 + 5 = 20",
    [("□ − 3 · (2 + 5) = 20", "Das Geschenk in die Klammer gezogen: Lösung wäre 41", 41 - 3 * (2 + 5) == 20 and 21 - 3 * (2 + 5) != 20),
     ("□ + 3 · 2 − 5 = 20", "Plus und Minus vertauscht: Lösung wäre 19", 19 + 3 * 2 - 5 == 20 and 21 + 3 * 2 - 5 != 20),
     ("(□ − 3) · 2 + 5 = 20", "Falsch geklammert: Lösung wäre 10,5", (21 - 3) * 2 + 5 != 20)],
    "Am Anfang □. Die Eis kosten 3 · 2 €: □ − 3 · 2. Dann kommen 5 € dazu: □ − 3 · 2 + 5. Jetzt sind es 20 €. Die Lösung ist □ = 21, denn 21 − 6 + 5 = 20. Bei den anderen Gleichungen kommt mit 21 nicht 20 heraus.",
    21 - 3 * 2 + 5 == 20), form="bruecke", regel=RG)
neu(T, "sach", "korrektur", "umkehr", Z(
    "Ein Rechteck hat den Umfang 36 m. Eine Seite ist 11 m lang. Wie lang ist die andere Seite?",
    7, "36 // 2 - 11", lambda: next(b for b in range(1, 40) if 2 * (11 + b) == 36),
    "Der Umfang ist 2 · (Länge + Breite). Länge plus Breite sind also 36 : 2 = 18 m. Die andere Seite ist 18 − 11 = 7 m lang. Probe: 2 · (11 + 7) = 36.",
    [(14, "Nur die eine Seite doppelt abgezogen: 36 − 2 · 11", "36 - 2 * 11"), (25, "Nur 11 vom Umfang abgezogen: 36 − 11", "36 - 11"), (18, "Nur 36 durch 2 geteilt", "36 // 2")], einheit="m"), form="umkehren", regel=RG)
neu(T, "sach", "sicherung", "rueckwaerts", Z(
    "Ein Bäcker verkauft morgens die Hälfte seiner Brötchen und noch 7 dazu. Mittags verkauft er die Hälfte der übrigen Brötchen. Danach sind noch 11 Brötchen übrig. Wie viele Brötchen hatte er am Morgen?",
    58, "(11 * 2 + 7) * 2", lambda: next(n for n in range(2, 500, 2) if (n - (n // 2 + 7)) % 2 == 0 and (n - (n // 2 + 7)) // 2 == 11),
    "Rückwärts: Nach dem Mittag sind 11 übrig, das ist die Hälfte. Vorher waren es 11 · 2 = 22. Davor wurden morgens 7 mehr als die Hälfte verkauft: 22 + 7 = 29 ist die Hälfte der Brötchen. Am Morgen waren es 29 · 2 = 58. Probe: 58 : 2 = 29, 29 + 7 = 36 verkauft, 22 übrig, die Hälfte davon 11.",
    [(22, "Nur 11 verdoppelt: 11 · 2", "11 * 2"), (29, "Nach dem Addieren der 7 nicht verdoppelt: 11 · 2 + 7", "11 * 2 + 7"), (36, "Erst 7 addiert, dann verdoppelt: (11 + 7) · 2", "(11 + 7) * 2")], einheit="Brötchen"), form="umkehren", regel=RG)
neu(T, "sach", "sicherung", "umkehr", Z(
    "Vier Gruppen sammeln jede gleich viele Flaschen. Dazu kommen 12 Flaschen vom Hausmeister. 4 Flaschen gehen kaputt. Dann sind es 108 Flaschen. Wie viele Flaschen hat jede Gruppe gesammelt?",
    25, "(108 - 12 + 4) // 4", lambda: next(x for x in range(1, 100) if 4 * x + 12 - 4 == 108),
    "Rückwärts: Die 4 kaputten Flaschen waren vorher noch da: 108 + 4 = 112. Die 12 vom Hausmeister gehören nicht zu den Gruppen: 112 − 12 = 100. Auf 4 Gruppen verteilt: 100 : 4 = 25. Probe: 4 · 25 + 12 − 4 = 108.",
    [(23, "Die kaputten Flaschen falsch herum gerechnet: (108 − 12 − 4) : 4", "(108 - 12 - 4) // 4"), (31, "Beide Mengen addiert: (108 + 12 + 4) : 4", "(108 + 12 + 4) // 4"), (100, "Das Teilen durch 4 vergessen: 108 − 12 + 4", "108 - 12 + 4")], einheit="Flaschen"), form="umkehren", regel=RG)
neu(T, "sach", "sicherung", "begruenden", W(
    "Ich denke mir eine Zahl, verdopple sie und addiere 6. Ich erhalte 30. Ben rechnet rückwärts: 30 : 2 = 15, dann 15 − 6 = 9. Welche Aussage über Bens Rechnung stimmt?",
    "Fehler: Die Reihenfolge ist falsch. Zuerst muss 6 abgezogen werden, dann wird halbiert. Richtig wäre (30 − 6) : 2 = 12.",
    [("Fehler: Er hätte malnehmen müssen. Richtig wäre 30 · 2 − 6 = 54.", "Mal statt geteilt umgekehrt: 30 · 2 − 6 = 54", 54 * 2 + 6 != 30),
     ("Fehler: Er hätte 6 addieren müssen. Richtig wäre 30 : 2 + 6 = 21.", "Plus statt Minus bei der Umkehrung: 30 : 2 + 6 = 21", 21 * 2 + 6 != 30),
     ("Kein Fehler: Man kehrt die Schritte in derselben Reihenfolge um, in der man sie gemacht hat.", "Falsche Regel bestätigt: 9 verdoppelt plus 6 ist 24, nicht 30", 9 * 2 + 6 != 30)],
    "Der letzte Schritt (plus 6) wird zuerst umgekehrt: 30 − 6 = 24. Dann der erste Schritt (verdoppeln) mit Geteilt durch 2: 24 : 2 = 12. Probe: 12 · 2 + 6 = 30. Bens 9 würde nur 24 ergeben.",
    12 * 2 + 6 == 30), regel=RG)
