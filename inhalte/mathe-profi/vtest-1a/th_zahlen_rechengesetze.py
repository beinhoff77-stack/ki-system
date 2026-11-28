T = "zahlen.rechengesetze"
RR, RT, RA, RG, RB = "rr.reihenfolge", "rr.tauschen", "rr.ausmultiplizieren", "rr.gegenrechnung", "id.zahlen.buendeln"
# ═════════ klammern ═════════
OU = "Kein Eintrag im Regelkatalog trägt das Überschlagen und Runden (id.zahlen.buendeln betrifft den Stellenwert, nicht den Überschlag)."
neu(T, "klammern", "test", "rueckwaerts", W(
    "In der Rechnung 20 − 4 · 3 + 2 darf genau ein Klammerpaar gesetzt werden. Danach soll das Ergebnis 50 sein. Welche Rechnung ist richtig?",
    "(20 − 4) · 3 + 2",
    [("20 − (4 · 3 + 2)", "Klammer um 4 · 3 + 2: Wert 6", 20 - (4 * 3 + 2) != 50),
     ("20 − 4 · (3 + 2)", "Klammer um 3 + 2: Wert 0", 20 - 4 * (3 + 2) != 50),
     ("(20 − 4 · 3) + 2", "Klammer um 20 − 4 · 3: ändert nichts, Wert 10", (20 - 4 * 3) + 2 != 50),
     ("(20 − 4) · (3 + 2)", "Zwei Klammerpaare, Wert 80", (20 - 4) * (3 + 2) != 50)],
    "Probiere die Klammern. (20 − 4) · 3 + 2 = 16 · 3 + 2 = 48 + 2 = 50. Bei 20 − (4 · 3 + 2) kommt 20 − 14 = 6 heraus, bei 20 − 4 · (3 + 2) kommt 20 − 20 = 0 heraus. (20 − 4 · 3) + 2 ist 8 + 2 = 10: Diese Klammer ändert nichts. (20 − 4) · (3 + 2) ist 16 · 5 = 80 und hat zwei Klammerpaare.",
    (20 - 4) * 3 + 2 == 50), form="umkehren", regel=RR, idee="ziel_herstellen")
neu(T, "klammern", "korrektur", "umkehr", Z(
    "Welche Zahl muss im Kästchen stehen? (□ + 4) · 3 − 5 = 25",
    6, "(25 + 5) // 3 - 4", lambda: next(x for x in range(0, 100) if (x + 4) * 3 - 5 == 25),
    "Rückwärts: Zuletzt wurde 5 abgezogen, also war es vorher 25 + 5 = 30. Davor wurde mit 3 malgenommen: 30 : 3 = 10. In der Klammer steht □ + 4 = 10, also ist □ = 6. Probe: (6 + 4) · 3 − 5 = 30 − 5 = 25.",
    [(10, "Nur bis zur Klammer zurückgerechnet und die 4 nicht abgezogen", "(25 + 5) // 3"), (18, "Die Klammer nicht beachtet und die Gleichung anders gelesen", "25 + 5 - 4 * 3")]), form="umkehren", regel=RR, idee="klammer_luecke")
neu(T, "klammern", "korrektur", "darstellung", W(
    "Welche Beschreibung passt zum Term 40 − (12 + 8) : 4?",
    "Addiere 12 und 8, teile die Summe durch 4 und ziehe das Ergebnis von 40 ab.",
    [("Ziehe 12 von 40 ab, addiere 8 und teile das Ergebnis durch 4.", "Die Klammer nicht beachtet, von links nach rechts gerechnet", (40 - 12 + 8) / 4 != 40 - (12 + 8) / 4),
     ("Ziehe die Summe aus 12 und 8 von 40 ab und teile das Ergebnis durch 4.", "Erst abgezogen und dann geteilt statt erst geteilt und dann abgezogen", (40 - (12 + 8)) / 4 != 40 - (12 + 8) / 4),
     ("Teile 12 durch 4, addiere 8 und ziehe das Ergebnis von 40 ab.", "Die Klammer falsch gesetzt: nur die 12 geteilt", 40 - (12 / 4 + 8) != 40 - (12 + 8) / 4)],
    "In der Klammer steht 12 + 8 = 20. Diese Summe wird durch 4 geteilt: 20 : 4 = 5. Das Ergebnis wird von 40 abgezogen: 40 − 5 = 35. Die Beschreibung muss genau diese Reihenfolge nennen.",
    40 - (12 + 8) / 4 == 35), form="bruecke", regel=RR, idee="darstellung_term_text")
neu(T, "klammern", "korrektur", "darstellung", W(
    "Welcher Term passt zu: „Teile die Summe aus 9 und 3 durch 4 und multipliziere das Ergebnis mit 2“?",
    "(9 + 3) : 4 · 2",
    [("9 + 3 : 4 · 2", "Klammer fehlt: dann wird zuerst 3 : 4 · 2 gerechnet (Punkt vor Strich)", (9 + 3) / 4 * 2 != 9 + 3 / 4 * 2),
     ("(9 + 3) : (4 · 2)", "Durch das Produkt 4 · 2 geteilt statt durch 4 und dann mal 2", (9 + 3) / 4 * 2 != (9 + 3) / (4 * 2)),
     ("9 + 3 : (4 · 2)", "Nur die 3 durch das Produkt 4 · 2 geteilt und dann 9 addiert", (9 + 3) / 4 * 2 != 9 + 3 / (4 * 2))],
    "Zuerst die Summe: (9 + 3). Diese Summe wird durch 4 geteilt: (9 + 3) : 4. Das Ergebnis wird mit 2 malgenommen: (9 + 3) : 4 · 2 = 12 : 4 · 2 = 3 · 2 = 6. Ohne Klammer würde nur 3 : 4 · 2 zuerst gerechnet; bei (9 + 3) : (4 · 2) würde durch 8 geteilt.",
    (9 + 3) / 4 * 2 == 6), form="bruecke", regel=RR, idee="darstellung_term_text")
neu(T, "klammern", "sicherung", "parameter", W(
    "Bei welchem Term darf man die Klammern weglassen, ohne dass sich der Wert ändert?",
    "(30 − 12) − 4",
    [("30 − (12 − 4)", "Mit Klammer 22, ohne Klammer 14: der Wert ändert sich", 30 - (12 - 4) != 30 - 12 - 4),
     ("2 · (3 + 4)", "Mit Klammer 14, ohne Klammer 10: der Wert ändert sich", 2 * (3 + 4) != 2 * 3 + 4),
     ("20 : (4 · 5)", "Mit Klammer 1, ohne Klammer 25: der Wert ändert sich", 20 // (4 * 5) != 20 // 4 * 5)],
    "Rechne mit und ohne Klammern. (30 − 12) − 4 = 18 − 4 = 14 und 30 − 12 − 4 = 14: gleich, denn von links nach rechts wird sowieso so gerechnet. 30 − (12 − 4) = 22, aber 30 − 12 − 4 = 14. 2 · (3 + 4) = 14, aber 2 · 3 + 4 = 10. 20 : (4 · 5) = 1, aber 20 : 4 · 5 = 25.",
    (30 - 12) - 4 == 30 - 12 - 4 == 14), regel=RR, idee="klammer_weglassen")
neu(T, "klammern", "sicherung", "umkehr", W(
    "In 3 □ 4 □ 5 = 23 stehen zwei Kästchen für Rechenzeichen aus +, −, · und :. Welche Rechenzeichen machen die Gleichung wahr?",
    "3 + 4 · 5 = 23, also + und ·",
    [("3 · 4 + 5 = 23, also · und +", "Die Zeichen vertauscht (3 · 4 + 5 = 17)", 3 * 4 + 5 != 23),
     ("3 + 4 + 5 = 23, also + und +", "Nur Plus eingesetzt (3 + 4 + 5 = 12)", 3 + 4 + 5 != 23),
     ("3 · 4 · 5 = 23, also · und ·", "Nur Mal eingesetzt (3 · 4 · 5 = 60)", 3 * 4 * 5 != 23)],
    "Punkt vor Strich: Bei 3 + 4 · 5 wird zuerst 4 · 5 = 20 gerechnet, dann 3 + 20 = 23. Die anderen Zeichen geben 17, 12 und 60. Mit Minus oder Geteilt kommt keine passende natürliche Zahl heraus.",
    3 + 4 * 5 == 23), form="umkehren", regel=RR, idee="ziel_herstellen")
neu(T, "klammern", "sicherung", "begruenden", W(
    "Jonas rechnet 100 − (12 + 8) · 4 von links nach rechts: 100 − 12 = 88, dann 88 + 8 = 96, dann 96 · 4 = 384. Welche Aussage über Jonas’ Rechnung stimmt?",
    "Fehler: Er hat die Klammer nicht zuerst gerechnet. Richtig wäre 100 − 20 · 4 = 100 − 80 = 20.",
    [("Fehler: Er hat die Klammer nicht zuerst gerechnet. Richtig wäre (100 − 20) · 4 = 320.", "Klammer um die ganze Differenz gesetzt: (100 − 20) · 4 = 320", (100 - 20) * 4 != 100 - (12 + 8) * 4),
     ("Fehler: Die Klammer spielt keine Rolle, nur Punkt vor Strich. Richtig wäre 100 − 12 + 8 · 4 = 120.", "Klammer ignoriert: 100 − 12 + 8 · 4 = 120", 100 - 12 + 8 * 4 != 100 - (12 + 8) * 4),
     ("Kein Fehler: Bei einer Rechnung mit Klammer rechnet man immer von links nach rechts.", "Falsche Regel bestätigt: von links nach rechts ergibt 384", 384 != 100 - (12 + 8) * 4)],
    "Die Klammer wird zuerst gerechnet: 12 + 8 = 20. Dann Punkt vor Strich: 20 · 4 = 80. Zuletzt 100 − 80 = 20. Jonas hat von links nach rechts gerechnet und dadurch 384 statt 20 bekommen.",
    100 - (12 + 8) * 4 == 20), regel=RR, idee="fehler_richtigstellen")
# ═════════ termaufbau ═════════
neu(T, "termaufbau", "test", "transfer", W(
    "Eine Geschichte: „Im Bus sitzen 30 Kinder. An der ersten Haltestelle steigen 6 Kinder aus, an der zweiten steigen 4 Kinder aus.“ Vier Terme stehen zur Wahl: ① 30 − 6 − 4  ② 30 − (6 + 4)  ③ 30 − 6 + 4  ④ 30 − (6 − 4). Welche Terme passen zur Geschichte?",
    "Genau ① und ②: Beide ziehen insgesamt 10 Kinder ab, einmal in zwei Schritten, einmal auf einmal.",
    [("Nur ①: Eine Klammer darf bei einer Geschichte nicht vorkommen.", "Klammer als nicht erlaubt gedeutet (② gibt denselben Wert 20)", 30 - (6 + 4) == 30 - 6 - 4),
     ("Genau ① und ③: Beim zweiten Halt muss man 4 addieren, weil die 4 zuletzt dasteht.", "Das Minus vor der 4 übersehen (③ ergibt 28)", 30 - 6 + 4 != 30 - 6 - 4),
     ("Genau ② und ④: Die Klammer fasst beide Halte zusammen, also werden 6 und 4 abgezogen.", "④ zieht nur 2 Kinder ab (④ ergibt 28)", 30 - (6 - 4) != 30 - (6 + 4))],
    "Insgesamt steigen 6 + 4 = 10 Kinder aus, im Bus bleiben 30 − 10 = 20 Kinder. Term ① zieht nacheinander 6 und 4 ab: 24, dann 20. Term ② zieht 6 + 4 = 10 auf einmal ab: 20. Term ③ addiert 4 und ergibt 28, Term ④ zieht nur 6 − 4 = 2 ab und ergibt 28.",
    30 - 6 - 4 == 20 == 30 - (6 + 4) and 30 - 6 + 4 == 28 == 30 - (6 - 4)), regel=RR, idee="terme_zur_geschichte")
neu(T, "termaufbau", "korrektur", "darstellung", W(
    "Bei welchem Term ist der letzte Rechenschritt ein Malnehmen?",
    "(3 + 4) · 5",
    [("3 + 4 · 5", "Zuerst wird 4 · 5 gerechnet, der letzte Schritt ist die Addition (3 + 20)", 3 + 4 * 5 == 23),
     ("3 · 4 − 5", "Der letzte Schritt ist die Subtraktion (12 − 5)", 3 * 4 - 5 == 7),
     ("20 : 4 + 5", "Der letzte Schritt ist die Addition (5 + 5)", 20 // 4 + 5 == 10)],
    "Der Term (3 + 4) · 5 rechnet zuerst die Klammer: 3 + 4 = 7. Der letzte Schritt ist 7 · 5 = 35. Bei den anderen Termen steht am Ende ein Plus oder Minus: Punktrechnungen wie 4 · 5 werden vorher gerechnet.",
    (3 + 4) * 5 == 35), form="bruecke", regel=RR, idee="term_struktur")
neu(T, "termaufbau", "korrektur", "darstellung", W(
    "Ein Kind schreibt: „Von 40 ziehe ich die Summe aus 9 und 6 ab.“ Welcher Term gehört dazu, und wie groß ist sein Wert?",
    "40 − (9 + 6) = 25",
    [("40 − 9 + 6 = 37", "Klammer weggelassen: 9 wird abgezogen, 6 addiert", 40 - 9 + 6 != 40 - (9 + 6)),
     ("(40 − 9) · 6 = 186", "Mal statt Summe gelesen und anders geklammert", (40 - 9) * 6 != 40 - (9 + 6)),
     ("40 + 9 − 6 = 43", "Plus und Minus vertauscht", 40 + 9 - 6 != 40 - (9 + 6))],
    "„Die Summe aus 9 und 6“ ist 9 + 6 = 15. Sie wird von 40 abgezogen: 40 − (9 + 6) = 40 − 15 = 25. Ohne Klammer, 40 − 9 + 6, würde man nur 9 abziehen und 6 addieren: 37.",
    40 - (9 + 6) == 25), form="bruecke", regel=RR, idee="term_aufstellen")
neu(T, "termaufbau", "korrektur", "darstellung", W(
    "Mia hat 20 €. Sie kauft 4 Hefte zu je 3 € und 2 Stifte zu je 2 €. Welcher Term gibt an, wie viel Geld ihr bleibt?",
    "20 − (4 · 3 + 2 · 2)",
    [("20 − 4 · 3 + 2 · 2", "Die Stifte addiert statt bezahlt: Wert 12", 20 - 4 * 3 + 2 * 2 != 20 - (4 * 3 + 2 * 2)),
     ("(20 − 4) · 3 − 2 · 2", "4 Hefte von den 20 € abgezogen: Wert 44", (20 - 4) * 3 - 2 * 2 != 20 - (4 * 3 + 2 * 2)),
     ("20 : 4 · 3 − 2 · 2", "Geteilt statt abgezogen: Wert 11", 20 // 4 * 3 - 2 * 2 != 20 - (4 * 3 + 2 * 2))],
    "Die Hefte kosten 4 · 3 € = 12 €, die Stifte 2 · 2 € = 4 €. Zusammen sind das 12 + 4 = 16 €. Es bleiben 20 − 16 = 4 €. Als Term: 20 − (4 · 3 + 2 · 2). Die Klammer fasst beide Ausgaben zusammen: Sie werden gemeinsam von den 20 € abgezogen. Ohne Klammer müsste man 20 − 4 · 3 − 2 · 2 schreiben.",
    20 - (4 * 3 + 2 * 2) == 4), form="bruecke", regel=RR, idee="term_aufstellen")
neu(T, "termaufbau", "sicherung", "umkehr", Z(
    "Ein Parkhaus verlangt für die erste Stunde 4 € und für jede weitere volle Stunde 2 €. Es wird nur für volle Stunden bezahlt. Auf der Rechnung steht 14 €. Für wie viele Stunden wurde bezahlt?",
    6, "(14 - 4) // 2 + 1", lambda: next(n for n in range(1, 40) if 4 + 2 * (n - 1) == 14),
    "Die erste Stunde kostet 4 €. Die weiteren Stunden kosten zusammen 14 − 4 = 10 €. Das sind 10 : 2 = 5 weitere Stunden. Zusammen 5 + 1 = 6 Stunden. Probe: 4 + 5 · 2 = 14.",
    [(7, "14 durch 2 geteilt: die erste Stunde wie alle anderen gerechnet", "14 // 2"), (5, "Nur die weiteren Stunden gezählt (14 − 4) : 2", "(14 - 4) // 2"), (10, "Nur 14 − 4 gerechnet", "14 - 4")], einheit="Stunden"), form="umkehren", regel=RR, idee="umkehr_tarif")
neu(T, "termaufbau", "sicherung", "parameter", Z(
    "Für genau eine natürliche Zahl □ haben die Terme 8 + 5 · □ und (8 + 5) · □ denselben Wert. Welche Zahl ist das?",
    1, "8 // (13 - 5)", lambda: next(x for x in range(0, 100) if 8 + 5 * x == (8 + 5) * x),
    "Der Term (8 + 5) · □ ist 13 · □. Der Term 8 + 5 · □ ist 8 plus 5 · □. Beide sind gleich, wenn die fehlenden 8 · □ genau 8 ergeben, also □ = 1. Probe: 8 + 5 · 1 = 13 und 13 · 1 = 13.",
    [(0, "Mit 0 probiert: links 8, rechts 0", "0"), (8, "Die 8 aus dem Term als Lösung genommen", "8"), (13, "Die Summe 8 + 5 als Lösung genommen", "8 + 5")]), regel=RR, idee="parameter_gleich")
neu(T, "termaufbau", "sicherung", "transfer", W(
    "Im Term (12 · 9 + 8 · 11 − 20) : 4 steht die 20 für einen Rabatt in Euro. Der Rabatt wird auf 36 € erhöht. Wie verändert sich der Wert des Terms?",
    "Er wird um 4 kleiner, denn 16 € mehr Rabatt werden durch 4 geteilt.",
    [("Er wird um 16 kleiner, denn der Rabatt wird um 16 größer.", "Das Teilen durch 4 vergessen", (36 - 20) / 4 != 16),
     ("Er wird um 4 größer, denn ein größerer Rabatt bedeutet mehr.", "Die Richtung der Änderung falsch gedeutet", (12 * 9 + 8 * 11 - 36) / 4 < (12 * 9 + 8 * 11 - 20) / 4),
     ("Er wird um 36 kleiner, denn jetzt wird 36 statt 20 abgezogen.", "Den neuen Rabatt statt der Änderung genommen", (36 - 20) / 4 != 36)],
    "Vorher: (108 + 88 − 20) : 4 = 176 : 4 = 44. Nachher: (108 + 88 − 36) : 4 = 160 : 4 = 40. Der Wert wird um 4 kleiner. Der Rabatt ist um 16 gewachsen, aber alles wird durch 4 geteilt, deshalb sind es 16 : 4 = 4.",
    (12 * 9 + 8 * 11 - 20) / 4 == 44 and (12 * 9 + 8 * 11 - 36) / 4 == 40), regel=RR, idee="was_waere_wenn")
neu(T, "vorteil", "test", "begruenden", W(
    "Welche Umformung von 85 − 38 + 53 ist erlaubt und richtig begründet?",
    "85 − 38 + 53 = 85 + 53 − 38. Jede Zahl nimmt ihr Rechenzeichen mit.",
    [("85 − 38 + 53 = 85 − 53 + 38. Beim Tauschen bleiben die Zeichen an ihrem Platz.", "Zahlen getauscht, aber die Zeichen nicht mitgenommen (der Wert wird 70 statt 100)", 85 - 53 + 38 != 85 - 38 + 53),
     ("100 − 47 − 38 = 100 − (47 − 38). Man darf eine Klammer um die beiden letzten Zahlen setzen.", "Eine Klammer ändert die Subtraktion", 100 - (47 - 38) != 100 - 47 - 38),
     ("64 : 8 : 2 = 64 : (8 : 2). Beim Teilen darf man wie beim Plus Klammern setzen.", "Teilen wie Plus behandelt", 64 // (8 // 2) != 64 // 8 // 2)],
    "Beim Umstellen nimmt jede Zahl ihr Rechenzeichen mit: 85 − 38 + 53 = 85 + 53 − 38 = 100. Bei 85 − 53 + 38 wäre der Wert 70. Eine Klammer um die letzten zwei Zahlen ändert die Subtraktion (100 − 47 − 38 = 15, aber 100 − (47 − 38) = 91), und beim Teilen gilt das auch nicht.",
    85 - 38 + 53 == 85 + 53 - 38 == 100), regel=RT, idee="erlaubte_umformung")
neu(T, "vorteil", "korrektur", "darstellung", W(
    "Ohne auszurechnen: Welcher Term hat denselben Wert wie 83 − 29 + 17?",
    "83 + 17 − 29",
    [("83 − 29 − 17", "Das Plus vor der 17 wurde zum Minus", 83 - 29 - 17 != 83 - 29 + 17),
     ("83 + 29 − 17", "Die Zeichen vor 29 und 17 vertauscht", 83 + 29 - 17 != 83 - 29 + 17),
     ("83 − (29 + 17)", "Eine Klammer um 29 + 17 gesetzt, das ändert den Wert", 83 - (29 + 17) != 83 - 29 + 17)],
    "Beim Umstellen nimmt jede Zahl ihr Rechenzeichen mit. Aus 83 − 29 + 17 wird 83 + 17 − 29 = 100 − 29 = 71. Die anderen Terme haben die Werte 37, 95 und 37.",
    83 - 29 + 17 == 83 + 17 - 29 == 71), regel=RT, idee="umstellen_gleicher_wert")
neu(T, "vorteil", "korrektur", "mehrschritt", W(
    "Du sollst 25 · 17 · 4 ausrechnen. Welcher erste Schritt ist am geschicktesten, und warum?",
    "Zuerst 25 · 4 = 100 rechnen, weil man beim Malnehmen die Reihenfolge ändern darf und 100 leicht mit 17 zu multiplizieren ist.",
    [("Zuerst 25 · 17 = 425 rechnen, weil man immer von links nach rechts rechnen muss.", "Die Reihenfolge für verpflichtend gehalten (der Weg wird nur schwerer)", 25 * 17 * 4 == 425 * 4),
     ("Zuerst 17 · 4 = 68 rechnen, weil die beiden kleinsten Zahlen am leichtesten sind.", "Nach der Größe der Zahlen gewählt statt nach dem leichten Paar", 25 * 68 == 25 * 17 * 4),
     ("Zuerst 25 + 17 + 4 = 46 rechnen, weil man bei Mal wie bei Plus zusammenzählt.", "Mal mit Plus verwechselt", 25 + 17 + 4 == 46 and 46 != 25 * 17 * 4)],
    "Beim Malnehmen darf man die Faktoren tauschen: 25 · 17 · 4 = 25 · 4 · 17. Dann ist 25 · 4 = 100 und 100 · 17 = 1 700. Das ist viel leichter als 425 · 4 oder 25 · 68, obwohl alle Wege dasselbe Ergebnis liefern.",
    25 * 17 * 4 == 1700 == 25 * 4 * 17), form="verfahren_waehlen", regel=RT, idee="geschickten_weg_waehlen")
neu(T, "vorteil", "korrektur", "mehrschritt", W(
    "Mia und Tim rechnen 50 · 37 · 2. Mia rechnet zuerst 50 · 37. Tim rechnet zuerst 50 · 2. Welche Aussage stimmt?",
    "Beide bekommen 3 700. Tims Weg ist bequemer, weil 50 · 2 = 100 ist.",
    [("Mia bekommt ein anderes Ergebnis, weil sie die Reihenfolge der Faktoren nicht geändert hat.", "Reihenfolge für das Ergebnis entscheidend gehalten", 50 * 37 * 2 == 50 * 2 * 37),
     ("Tim bekommt ein anderes Ergebnis, weil er die Faktoren vertauscht hat.", "Vertauschen beim Malnehmen für verboten gehalten", 50 * 2 * 37 == 50 * 37 * 2),
     ("Beide bekommen dasselbe, aber nur, weil 37 eine ungerade Zahl ist.", "Falsche Begründung: es gilt für alle Zahlen", 50 * 38 * 2 == 50 * 2 * 38)],
    "Beim Malnehmen darf man die Faktoren tauschen. Mia: 50 · 37 = 1 850, dann 1 850 · 2 = 3 700. Tim: 50 · 2 = 100, dann 100 · 37 = 3 700. Beide bekommen 3 700, bei Tim ist die Rechnung leichter. Es gilt für alle Zahlen, nicht nur für ungerade.",
    50 * 37 * 2 == 3700 == 50 * 2 * 37), form="zwei_wege", regel=RT, idee="zwei_wege_vergleichen")
neu(T, "vorteil", "sicherung", "umkehr", Z(
    "Bestimme die Zahl im Kästchen möglichst geschickt: 4 · □ · 25 = 700.",
    7, "700 // (4 * 25)", lambda: next(x for x in range(0, 200) if 4 * x * 25 == 700),
    "Fasse zuerst 4 · 25 = 100 zusammen. Dann muss 100 · □ = 700 gelten, also □ = 700 : 100 = 7. Probe: 4 · 7 · 25 = 28 · 25 = 700.",
    [(175, "Nur durch 4 geteilt: 700 : 4", "700 // 4"), (28, "Nur durch 25 geteilt: 700 : 25", "700 // 25"), (671, "4 und 25 von 700 abgezogen", "700 - 4 - 25")]), form="umkehren", regel=RT, idee="luecke_rechenvorteil")
neu(T, "vorteil", "sicherung", "begruenden", W(
    "Ben rechnet 4 · 18 · 25 so: 4 · 25 = 100, dann 100 + 18 = 118. Welche Aussage über Bens Rechnung stimmt?",
    "Fehler: Nach 4 · 25 = 100 muss mal 18 gerechnet werden, nicht plus. Richtig wäre 100 · 18 = 1 800.",
    [("Fehler: Er darf 25 und 18 nicht vertauschen. Richtig wäre 4 · 18 · 25 = 72 · 25 = 1 800.", "Das Vertauschen für verboten gehalten (der Wert 1 800 bleibt gleich)", 72 * 25 == 1800),
     ("Kein Fehler: Nach dem Vertauschen wird addiert, also 100 + 18 = 118.", "Aus dem Malzeichen ein Pluszeichen gemacht", 100 + 18 != 4 * 18 * 25),
     ("Fehler: Er hätte 4 + 18 + 25 rechnen müssen. Richtig wäre 47.", "Mal und Plus verwechselt", 4 + 18 + 25 == 47 and 47 != 1800)],
    "Die Faktoren darf man tauschen: 4 · 18 · 25 = 4 · 25 · 18. Dann 4 · 25 = 100 und 100 · 18 = 1 800. Ben hat nach dem Tauschen aus dem Mal ein Plus gemacht (100 + 18 = 118). Vertauschen war erlaubt, nur das Rechenzeichen danach war falsch.",
    100 * 18 == 1800 == 4 * 18 * 25), regel=RT, idee="fehler_richtigstellen")
neu(T, "vorteil", "sicherung", "pruefung", W(
    "Welche Aussage über die Werte von 36 · 25 · 4 und 18 · 25 · 8 ist richtig begründet?",
    "Beide Werte sind gleich, denn 36 · 4 = 144 und 18 · 8 = 144, und beim Malnehmen darf man die Faktoren tauschen.",
    [("18 · 25 · 8 ist größer, weil 8 größer als 4 ist.", "Nur zwei Faktoren verglichen (8 gegen 4)", 36 * 25 * 4 == 18 * 25 * 8),
     ("36 · 25 · 4 ist größer, weil 36 größer als 18 ist.", "Nur zwei Faktoren verglichen (36 gegen 18)", 36 * 25 * 4 == 18 * 25 * 8),
     ("Beide Werte sind gleich, weil in beiden Termen 25 vorkommt.", "Falsche Begründung: mit 18 · 25 · 9 wäre der Wert anders", 36 * 25 * 4 != 18 * 25 * 9)],
    "Tausche die Faktoren: 36 · 25 · 4 = 36 · 4 · 25 = 144 · 25 und 18 · 25 · 8 = 18 · 8 · 25 = 144 · 25. Beide Werte sind 3 600. Dass 25 in beiden Termen vorkommt, ist kein Grund: Mit 18 · 25 · 9 wäre der Wert 4 050.",
    36 * 25 * 4 == 18 * 25 * 8 == 3600), form="zwei_wege", regel=RT, idee="gleicher_wert_begruenden")
# ═════════ verteilen ═════════
neu(T, "verteilen", "test", "begruenden", W(
    "Mia rechnet 7 · 98 so: 7 · 100 − 7 · 2 = 700 − 14 = 686. Welche Begründung zeigt, warum das erlaubt ist?",
    "98 ist 2 weniger als 100. Von 7 Hundertern werden deshalb 7 Zweier abgezogen: 7 · 98 = 7 · (100 − 2).",
    [("Weil man beim Malnehmen die Zahlen vertauschen darf, kann man 98 durch 100 ersetzen.", "Tauschen mit Verteilen verwechselt", 7 * 100 != 7 * 98),
     ("Weil 98 fast 100 ist, darf man 7 · 100 − 2 = 698 nehmen.", "Nur eine 2 abgezogen statt siebenmal die 2", 7 * 100 - 2 != 7 * 98),
     ("Weil man bei einem Produkt die Klammer weglassen darf: 7 · (100 − 2) = 7 · 100 − 2.", "Die Klammer falsch aufgelöst (nur der erste Teil wird mit 7 malgenommen)", 7 * 100 - 2 != 7 * (100 - 2))],
    "98 = 100 − 2. Also ist 7 · 98 = 7 · (100 − 2). Jeder Teil der Klammer wird mit 7 malgenommen: 7 · 100 − 7 · 2 = 700 − 14 = 686. Man zieht nicht nur 2, sondern siebenmal 2 ab.",
    7 * 98 == 686 == 7 * 100 - 7 * 2), regel=RA, idee="begruenden_geschickt")
neu(T, "verteilen", "korrektur", "umkehr", Z(
    "Das Ergebnis von 17 · □ + 17 · 14 ist so groß wie 17 · 50. Welche Zahl steht im Kästchen?",
    36, "50 - 14", lambda: next(x for x in range(0, 100) if 17 * x + 17 * 14 == 17 * 50),
    "Klammere 17 aus: 17 · (□ + 14) = 17 · 50. Dann muss □ + 14 = 50 gelten, also □ = 50 − 14 = 36. Probe: 17 · 36 + 17 · 14 = 612 + 238 = 850 = 17 · 50.",
    [(64, "14 addiert statt abgezogen: 50 + 14", "50 + 14"), (700, "50 mit 14 malgenommen", "50 * 14"), (850, "17 · 50 als Zahl im Kästchen genannt", "17 * 50")]), form="umkehren", regel=RA, idee="luecke_ausklammern")
neu(T, "verteilen", "korrektur", "darstellung", W(
    "In einem Beet gibt es 9 Reihen. In jeder Reihe stehen erst 6 rote und dann 4 gelbe Blumen. Welche Rechnung gibt die Zahl aller Blumen an?",
    "9 · (6 + 4)",
    [("9 · 6 + 4", "Nur die roten Blumen mit 9 malgenommen: Wert 58", 9 * 6 + 4 != 9 * (6 + 4)),
     ("9 + 6 · 4", "Plus und Mal vertauscht: Wert 33", 9 + 6 * 4 != 9 * (6 + 4)),
     ("(9 + 6) · 4", "Falsch geklammert: Wert 60", (9 + 6) * 4 != 9 * (6 + 4))],
    "Jede Reihe hat 6 + 4 = 10 Blumen. Bei 9 Reihen sind das 9 · (6 + 4) = 9 · 10 = 90 Blumen. Man kann auch 9 · 6 + 9 · 4 = 54 + 36 rechnen. Bei 9 · 6 + 4 würden die gelben Blumen nur einmal gezählt.",
    9 * (6 + 4) == 90 == 9 * 6 + 9 * 4), form="bruecke", regel=RA, idee="situation_zu_term")
neu(T, "verteilen", "korrektur", "mehrschritt", W(
    "Anna rechnet 4 · 27 so: 4 · 20 + 4 · 7. Ben rechnet 4 · 27 so: 4 · 30 − 4 · 3. Welche Aussage stimmt?",
    "Beide haben recht: 27 = 20 + 7 und 27 = 30 − 3, und jeder Teil wird mit 4 malgenommen. Es kommt 108 heraus.",
    [("Nur Anna: Beim Minus darf man das Verteilen nicht anwenden.", "Das Verteilen nur für Plus für erlaubt gehalten (Bens Weg ergibt auch 108)", 4 * 30 - 4 * 3 == 4 * 27),
     ("Nur Ben: 30 ist eine glatte Zahl, deshalb ist nur sein Weg erlaubt.", "Die Erlaubnis an glatte Zahlen gebunden (Annas Weg ergibt auch 108)", 4 * 20 + 4 * 7 == 4 * 27),
     ("Keiner: Man müsste 4 · 20 + 7 und 4 · 30 − 3 rechnen.", "Den Faktor 4 nur an den ersten Teil gesetzt", 4 * 20 + 7 != 4 * 27)],
    "Anna: 27 = 20 + 7, also 4 · 27 = 4 · 20 + 4 · 7 = 80 + 28 = 108. Ben: 27 = 30 − 3, also 4 · 27 = 4 · 30 − 4 · 3 = 120 − 12 = 108. Das Verteilen klappt bei Plus und bei Minus, und es muss jeder Teil mit 4 malgenommen werden.",
    4 * 20 + 4 * 7 == 108 == 4 * 30 - 4 * 3), form="zwei_wege", regel=RA, idee="zwei_wege_vergleichen")
neu(T, "verteilen", "sicherung", "transfer", W(
    "Ein Rechteck ist 8 cm hoch und aus zwei Teilen mit den Breiten 30 cm und 2 cm zusammengesetzt. Die Höhe wird auf 16 cm verdoppelt, die Breiten bleiben. Wie verändert sich die Gesamtfläche 8 · 30 + 8 · 2?",
    "Sie verdoppelt sich, denn beide Teilflächen werden doppelt so groß.",
    [("Sie wird um 8 cm² größer, weil die Höhe um 8 cm wächst.", "Den Zuwachs der Höhe als Zuwachs der Fläche gedeutet", 16 * 30 + 16 * 2 != 8 * 30 + 8 * 2 + 8),
     ("Nur die erste Teilfläche verdoppelt sich, die zweite bleibt gleich.", "Nur den ersten Summanden verändert", 16 * 30 + 8 * 2 != 16 * 30 + 16 * 2),
     ("Sie wird 16-mal so groß, weil die neue Höhe 16 cm ist.", "Die neue Höhe als Faktor gedeutet", 16 * 32 != 16 * (8 * 32))],
    "Vorher: 8 · 30 + 8 · 2 = 8 · 32 = 256 cm². Nachher: 16 · 30 + 16 · 2 = 16 · 32 = 512 cm². Das ist das Doppelte. Die Höhe 8 kommt in beiden Teilflächen als Faktor vor, deshalb verdoppeln sich beide.",
    16 * 32 == 512 == 2 * 8 * 32), regel=RA, idee="was_waere_wenn")
neu(T, "verteilen", "sicherung", "mehrschritt", W(
    "Wie rechnet man 19 · 36 + 19 · 64 − 19 · 50 am geschicktesten, und warum?",
    "Die 19 ausklammern: 19 · (36 + 64 − 50). In der Klammer steht 50, und 19 · 50 = 950 ist leicht.",
    [("Jedes Produkt einzeln ausrechnen, weil 19 eine kleine Zahl ist.", "Keinen Rechenvorteil genutzt (richtig, aber umständlich)", 19 * 36 + 19 * 64 - 19 * 50 == 950),
     ("Die Zahlen 36, 64 und 50 addieren und dann mit 19 malnehmen.", "Das Minus wie ein Plus behandelt", (36 + 64 + 50) * 19 != 950),
     ("Die 19 abziehen: 36 + 64 − 50 − 19.", "Das Malnehmen mit 19 weggelassen", 36 + 64 - 50 - 19 != 950)],
    "Alle drei Teile haben den Faktor 19. Ausklammern: 19 · (36 + 64 − 50) = 19 · (100 − 50) = 19 · 50 = 950. Die Zahlen in der Klammer sind so gewählt, dass 36 + 64 = 100 ergibt. Einzeln ausgerechnet kommt dasselbe heraus, aber mit mehr Aufwand.",
    19 * (36 + 64 - 50) == 950), form="verfahren_waehlen", regel=RA, idee="geschickten_weg_waehlen")
neu(T, "verteilen", "sicherung", "begruenden", W(
    "Tom klammert aus: 15 · 7 + 15 · 9 = 15 · (7 · 9) = 945. Welche Aussage über Toms Rechnung stimmt?",
    "Fehler: In der Klammer muss ein Plus stehen, kein Mal. Richtig wäre 15 · (7 + 9) = 240.",
    [("Fehler: Die 15 darf man nicht ausklammern. Richtig wäre 15 · 7 + 9 = 114.", "Ausklammern für verboten gehalten: 15 · 7 + 9 = 114", 15 * 7 + 9 != 15 * 7 + 15 * 9),
     ("Fehler: Die 15 muss in der Klammer noch einmal mit 7 und 9 malgenommen werden: 15 · (15 · 7 + 15 · 9) = 3 600.", "Die 15 doppelt verwendet: 3 600", 15 * (15 * 7 + 15 * 9) != 15 * 7 + 15 * 9),
     ("Kein Fehler: Beim Ausklammern wird aus Plus ein Mal.", "Falsche Regel bestätigt (945)", 15 * 7 * 9 != 15 * 7 + 15 * 9)],
    "15 · 7 + 15 · 9 = 15 · (7 + 9) = 15 · 16 = 240. Beim Ausklammern bleibt das Rechenzeichen zwischen den Summanden ein Plus. Tom hat 7 · 9 = 63 und 15 · 63 = 945 gerechnet.",
    15 * (7 + 9) == 240 == 15 * 7 + 15 * 9), regel=RA, idee="fehler_richtigstellen")
# ═════════ umkehraufgabe_mal ═════════
neu(T, "umkehraufgabe_mal", "test", "rueckwaerts", Z(
    "Eine Rechenmaschine macht mit jeder eingegebenen Zahl nacheinander drei Schritte: mal 5, plus 12, geteilt durch 4. Am Ende zeigt sie 8 an. Welche Zahl wurde eingegeben?",
    4, "(8 * 4 - 12) // 5", lambda: next(x for x in range(0, 100) if (x * 5 + 12) / 4 == 8),
    "Rückwärts, der letzte Schritt zuerst: Geteilt durch 4 kehrt man mit Mal 4 um: 8 · 4 = 32. Plus 12 kehrt man mit Minus 12 um: 32 − 12 = 20. Mal 5 kehrt man mit Geteilt durch 5 um: 20 : 5 = 4. Probe: 4 · 5 = 20, 20 + 12 = 32, 32 : 4 = 8.",
    [(20, "Das Teilen durch 5 vergessen: 8 · 4 − 12", "8 * 4 - 12"), (44, "Plus statt Minus bei der Umkehrung: 8 · 4 + 12", "8 * 4 + 12"), (32, "Nur das Teilen durch 4 umgekehrt: 8 · 4", "8 * 4")]), form="umkehren", regel=RG, idee="kette_rueckwaerts")
neu(T, "umkehraufgabe_mal", "korrektur", "umkehr", W(
    "Bei 36 : □ = 9 suchst du die Zahl im Kästchen. Welche Rechnung führt zu ihr?",
    "36 : 9",
    [("36 · 9", "Mal statt geteilt: 324", 36 * 9 != 4),
     ("36 − 9", "Minus statt geteilt: 27", 36 - 9 != 4),
     ("9 : 36", "Die Zahlen vertauscht: 9 : 36 ist keine natürliche Zahl", 9 % 36 != 0)],
    "Gesucht ist die Zahl, durch die man 36 teilen muss, um 9 zu erhalten. Das ist 36 : 9 = 4. Probe: 36 : 4 = 9. Mit 36 · 9 = 324 und 36 − 9 = 27 würde die Probe nicht stimmen.",
    36 // 9 == 4 and 36 // 4 == 9), form="umkehren", regel=RG, idee="gleichung_waehlen")
neu(T, "umkehraufgabe_mal", "korrektur", "umkehr", Z(
    "Zwei natürliche Zahlen haben das Produkt 48 und die Summe 14. Welche ist die größere der beiden Zahlen?",
    8, "8", lambda: max(a for a in range(1, 50) for b in range(1, 50) if a * b == 48 and a + b == 14),
    "Suche zwei Zahlen mit dem Produkt 48: 1 und 48, 2 und 24, 3 und 16, 4 und 12, 6 und 8. Nur bei 6 und 8 ist die Summe 14. Die größere Zahl ist 8. Probe: 6 · 8 = 48 und 6 + 8 = 14.",
    [(6, "Die kleinere Zahl genannt", "14 - 8"), (7, "Die Hälfte der Summe genommen", "14 // 2"), (24, "Die Hälfte des Produkts genommen", "48 // 2")]), form="umkehren", regel=RG, idee="zahlen_suchen")
neu(T, "umkehraufgabe_mal", "korrektur", "umkehr", W(
    "Welche Gleichung hat dieselbe Lösung wie 7 · x = 56?",
    "56 : x = 7",
    [("x : 7 = 56", "Geteilt statt mal: Lösung wäre 392", 56 * 7 != 8),
     ("x · 56 = 7", "Die Zahlen vertauscht: keine natürliche Lösung", 7 % 56 != 0),
     ("x : 8 = 56", "Die Lösung 8 mit der 56 verwechselt: Lösung wäre 448", 56 * 8 != 8)],
    "Aus 7 · x = 56 folgt x = 56 : 7 = 8. Bei 56 : x = 7 ist x = 56 : 7 = 8 ebenfalls. Bei x : 7 = 56 wäre x = 56 · 7 = 392, bei x · 56 = 7 gibt es keine natürliche Lösung, bei x : 8 = 56 wäre x = 448.",
    7 * 8 == 56 and 56 // 8 == 7), form="umkehren", regel=RG, idee="gleichung_waehlen")
neu(T, "umkehraufgabe_mal", "sicherung", "darstellung", W(
    "Zu welcher Geschichte gehört die Gleichung 48 : x = 6?",
    "48 Murmeln werden gleichmäßig auf einige Kinder verteilt. Jedes Kind bekommt 6. Wie viele Kinder sind es?",
    [("Jedes Kind bekommt 48 Murmeln. Es gibt 6 Kinder. Wie viele Murmeln sind es?", "Mal statt geteilt: 48 · 6", 48 * 6 != 48 // 6),
     ("Ein Kind hat 48 Murmeln und verliert 6. Wie viele bleiben?", "Minus statt geteilt: 48 − 6", 48 - 6 != 48 // 6),
     ("6 Kinder teilen sich eine Zahl von Murmeln. Jedes bekommt 48. Wie viele Murmeln sind es?", "Zahlen vertauscht: x : 6 = 48", 48 * 6 != 48 // 6)],
    "48 : x = 6 heißt: 48 wird durch x geteilt, jeder Teil ist 6. Das passt zu 48 Murmeln, die gleichmäßig verteilt werden, wobei jedes Kind 6 bekommt. x = 48 : 6 = 8 Kinder. Die anderen Geschichten gehören zu 48 · 6, 48 − 6 und x : 6 = 48.",
    48 // 8 == 6), form="bruecke", regel=RG, idee="geschichte_zu_gleichung")
neu(T, "umkehraufgabe_mal", "sicherung", "begruenden", W(
    "Warum hat die Gleichung 7 · x = 50 keine Lösung unter den natürlichen Zahlen? Wähle die richtige Begründung.",
    "Weil 50 nicht in der 7er-Reihe steht: 49 und 56 liegen links und rechts davon.",
    [("Weil 50 gerade und 7 ungerade ist.", "Gerade Ergebnisse sind möglich: 7 · 2 = 14", 7 * 2 == 14),
     ("Weil 7 eine Primzahl ist.", "Primzahl mit Unlösbarkeit verwechselt (7 · 7 = 49 hat eine Lösung)", 7 * 7 == 49),
     ("Weil x größer als 50 sein müsste.", "x wäre kleiner als 50, nicht größer", 50 // 7 < 50)],
    "Die 7er-Reihe lautet 7, 14, 21, 28, 35, 42, 49, 56. Die 50 steht nicht darin. 50 : 7 geht nicht ohne Rest auf (7 · 7 = 49, Rest 1). Gerade und ungerade Zahlen spielen keine Rolle, und auch bei einer Primzahl wie 7 gibt es Lösungen, zum Beispiel 7 · 7 = 49.",
    7 * 7 == 49 and 7 * 8 == 56), regel=RG, idee="begruenden_loesbarkeit")
neu(T, "umkehraufgabe_mal", "sicherung", "parameter", Z(
    "Für wie viele natürliche Zahlen a von 1 bis 12 (beide Grenzen eingeschlossen) hat die Gleichung a · x = 36 eine Lösung in den natürlichen Zahlen?",
    7, "7", lambda: sum(1 for a in range(1, 13) if 36 % a == 0),
    "Die Gleichung hat genau dann eine Lösung, wenn 36 in der a-er-Reihe steht, also wenn a ein Teiler von 36 ist. Die Teiler von 36 bis 12 sind 1, 2, 3, 4, 6, 9 und 12. Das sind 7 Zahlen.",
    [(6, "Den Teiler 12 nicht mitgezählt (die Grenze gilt einschließlich): 7 − 1", "7 - 1"), (12, "Alle Zahlen von 1 bis 12 gezählt: 13 − 1", "13 - 1")]), form="umkehren", regel=RG, idee="parameter_teiler")
# ═════════ ueberschlag ═════════
neu(T, "ueberschlag", "test", "begruenden", W(
    "Tim hat 612 · 49 ausgerechnet und 2 998 erhalten. Welcher Überschlag zeigt am schnellsten, dass das nicht stimmen kann, und warum?",
    "600 · 50 = 30 000. Das ist rund zehnmal so viel wie 2 998. Tim hat sich um eine Stelle verrechnet.",
    [("Die letzten Ziffern: 2 · 9 = 18, das Ergebnis muss auf 8 enden. 2 998 endet auf 8, also stimmt es.", "Endziffer passt, aber das ist nur eine notwendige Bedingung (2 998 ist trotzdem falsch)", 612 * 49 != 2998),
     ("600 + 50 = 650, also muss das Ergebnis ungefähr 650 sein.", "Plus statt Mal überschlagen", 612 * 49 != 650),
     ("Ein Überschlag kann nie zeigen, dass ein Ergebnis falsch ist. Dafür muss man genau nachrechnen.", "Überschlag für nutzlos gehalten, dabei ist 30 000 weit weg von 2 998", abs(600 * 50 - 2998) > 10000)],
    "Runde die Faktoren: 612 ≈ 600 und 49 ≈ 50. 600 · 50 = 30 000. Das genaue Ergebnis muss nahe bei 30 000 liegen (es ist 29 988). Tims 2 998 ist zehnmal zu klein. Die Endziffer 8 passt zwar, beweist aber nichts. Mit 600 + 50 wurde falsch gerechnet.",
    600 * 50 == 30000 and 612 * 49 == 29988), regel=None, ohne=OU, idee="kontrolle_ueberschlag")
neu(T, "ueberschlag", "korrektur", "umkehr", Z(
    "Eine Lehrerin überschlägt die Kosten für den Museumsbesuch ihrer Klasse: Sie rundet die Kinderzahl auf Zehner (ab 5 wird aufgerundet) und rechnet mit 7 € Eintritt je Kind. Ihr Überschlag ergibt 210 €. Wie viele Kinder kann die Klasse höchstens haben?",
    34, "30 + 4", lambda: max(n for n in range(1, 200) if (n + 5) // 10 * 10 * 7 == 210),
    "210 : 7 = 30. Die Kinderzahl wurde also auf 30 gerundet. Auf 30 runden alle Zahlen von 25 bis 34. Die größte ist 34 Kinder (35 würde auf 40 aufgerundet).",
    [(30, "Die gerundete Zahl genannt: 210 : 7", "210 // 7"), (35, "Eine zu viel: 30 + 5, aber 35 wird schon aufgerundet", "30 + 5"), (29, "Eine Zahl unter der gerundeten Zahl genannt (30 − 1); aber die größte Zahl, die noch auf 30 rundet, liegt höher", "30 - 1")], einheit="Kinder"), form="umkehren", regel=None, ohne=OU, idee="rundungsfenster")
neu(T, "ueberschlag", "korrektur", "darstellung", W(
    "Ein Kind überschlägt den Preis von 3 Jacken zu je 198 € mit 3 · 200 € = 600 €. Welche Aussage über den genauen Preis ist richtig?",
    "Der genaue Preis liegt unter 600 €, weil 198 € weniger als 200 € sind.",
    [("Der genaue Preis liegt über 600 €, weil man beim Überschlag immer abrundet.", "Eine falsche Regel zum Runden", 3 * 198 < 600),
     ("Der genaue Preis ist genau 600 €, weil ein Überschlag das Ergebnis liefert.", "Überschlag und genaues Ergebnis verwechselt", 3 * 198 != 600),
     ("Über den genauen Preis kann man nichts sagen, weil ein Überschlag nur geschätzt ist.", "Den Überschlag für nutzlos gehalten", 3 * 198 < 600)],
    "198 wurde auf 200 aufgerundet, also ist der Überschlag zu groß. Der genaue Preis ist 3 · 198 = 594 €, das ist weniger als 600 €. Man kann also schon beim Überschlag sagen, in welche Richtung der Fehler geht.",
    3 * 198 == 594 < 600), regel=None, ohne=OU, idee="richtung_ueberschlag")
neu(T, "ueberschlag", "korrektur", "mehrschritt", W(
    "Zwei Kinder überschlagen 4 812 + 3 487. Kind A rundet auf Tausender: 5 000 + 3 000. Kind B rundet auf Hunderter: 4 800 + 3 500. Das genaue Ergebnis ist 8 299. Welche Aussage stimmt?",
    "Beide Überschläge sind brauchbar, aber B liegt viel näher am genauen Ergebnis, weil feiner gerundet wurde.",
    [("A ist besser, weil Tausender einfacher zu rechnen sind und das Ergebnis dann genauer ist.", "Einfach mit genau verwechselt (A ergibt 8 000)", abs(8000 - 8299) > abs(8300 - 8299)),
     ("Beide sind gleich gut, weil beide auf volle Hunderter oder Tausender gerundet haben.", "Die Rundungsstelle nicht verglichen", abs(8000 - 8299) != abs(8300 - 8299)),
     ("B ist falsch, weil man bei einer Summe nur auf Tausender runden darf.", "Eine falsche Rundungsregel erfunden", 4800 + 3500 == 8300)],
    "A ergibt 5 000 + 3 000 = 8 000, B ergibt 4 800 + 3 500 = 8 300. Das genaue Ergebnis ist 4 812 + 3 487 = 8 299. B ist nur um 1 daneben, A um 299. Je feiner man rundet, desto genauer wird der Überschlag, aber desto mehr muss man rechnen.",
    4812 + 3487 == 8299 and abs(8300 - 8299) < abs(8000 - 8299)), form="zwei_wege", regel=None, ohne=OU, idee="zwei_ueberschlaege_vergleichen")
neu(T, "ueberschlag", "sicherung", "transfer", W(
    "Ein Lager fasst höchstens 1 000 Flaschen. Es sollen 23 Kisten mit je 48 Flaschen hinein. Mia überschlägt 20 · 50 = 1 000 und sagt: „Das passt genau.“ Welche Aussage ist richtig?",
    "Der Überschlag reicht hier nicht: Es sind 23 · 48 = 1 104 Flaschen, also zu viele. Mia hat 23 zu stark auf 20 abgerundet.",
    [("Mia hat recht: Ein Überschlag zeigt immer das genaue Ergebnis.", "Überschlag und genaues Ergebnis verwechselt", 20 * 50 == 1000 and 23 * 48 != 1000),
     ("Es passt sicher, denn 20 ist kleiner als 23 und 50 ist größer als 48.", "Gegenläufige Rundungen als sich aufhebend gehalten (es sind 1 104)", 23 * 48 > 1000),
     ("Es passt, denn 23 · 48 ist genau 1 000.", "Falsch gerechnet: 23 · 48 ist nicht 1 000", 23 * 48 != 1000)],
    "Genau gerechnet: 23 · 48 = 1 104. Das ist mehr als 1 000, es passt also nicht. Beim Überschlag wurde 23 auf 20 abgerundet (dadurch fehlen 3 · 48 = 144 Flaschen) und 48 auf 50 aufgerundet (das bringt nur 23 · 2 = 46 dazu). Wenn es um eine Grenze geht, sollte man vorsichtig runden.",
    23 * 48 == 1104 > 1000), regel=None, ohne=OU, idee="ueberschlag_entscheidung")
neu(T, "ueberschlag", "sicherung", "begruenden", W(
    "Mia hat 596 · 12 = 7 152 gerechnet. Zur Kontrolle überschlägt sie 600 · 10 = 6 000 und sagt: „Das passt nicht, 7 152 ist falsch.“ Welche Aussage über Mias Kontrolle stimmt?",
    "Fehler: Mias Überschlag ist zu grob, um 7 152 abzulehnen. Richtig wäre: Mit 600 · 12 = 7 200 liegt der Überschlag ganz in der Nähe, also ist 7 152 glaubwürdig.",
    [("Kein Fehler: Der Überschlag 6 000 zeigt, dass 7 152 nicht stimmen kann.", "Überschlag und Ergebnis verglichen, ohne die grobe Rundung zu beachten", 596 * 12 == 7152),
     ("Fehler: Ein Überschlag darf nur eine Zahl runden. Richtig wäre 596 · 10 = 5 960.", "Eine falsche Regel erfunden (auch dieser Wert ist weit weg)", abs(596 * 10 - 7152) > abs(600 * 12 - 7152)),
     ("Fehler: Überschläge sind nutzlos, man muss das Ergebnis schriftlich noch einmal berechnen. Richtig wäre das Nachrechnen.", "Den Überschlag für nutzlos gehalten (er hilft, sobald er fein genug ist)", abs(600 * 12 - 7152) < 100)],
    "Beim Überschlag wurde 12 auf 10 gerundet, das ist ein großer Sprung und macht das Ergebnis zu klein. Mit 600 · 12 = 7 200 liegt der Überschlag nahe an 7 152. Tatsächlich ist 596 · 12 = 7 152 richtig. Ein Überschlag, der weit weg liegt, zeigt nur dann einen Fehler, wenn er nicht zu grob gerundet ist.",
    596 * 12 == 7152 and 600 * 12 == 7200), regel=None, ohne=OU, idee="fehler_richtigstellen")
neu(T, "ueberschlag", "sicherung", "umkehr", Z(
    "Eine natürliche Zahl wird auf Hunderter gerundet (ab 50 wird aufgerundet) und ergibt 4 600. Wie groß ist die Summe aus der kleinsten und der größten natürlichen Zahl, für die das gilt?",
    9199, "4550 + 4649", lambda: min(n for n in range(0, 10000) if (n + 50) // 100 * 100 == 4600) + max(n for n in range(0, 10000) if (n + 50) // 100 * 100 == 4600),
    "Auf 4 600 runden alle Zahlen von 4 550 bis 4 649. 4 550 wird noch aufgerundet, 4 649 noch abgerundet. Die Summe ist 4 550 + 4 649 = 9 199.",
    [(9200, "Die gerundete Zahl verdoppelt: 4 600 · 2", "4600 * 2"), (9299, "Die größte Zahl falsch bestimmt: 4 650 wird schon aufgerundet", "4650 + 4649"), (9100, "Die kleinste Zahl doppelt genommen", "4550 + 4550")]), form="umkehren", regel=None, ohne=OU, idee="rundungsfenster")
neu(T, "sach", "test", "rueckwaerts", Z(
    "In einem Zug steigen an der ersten Haltestelle 14 Fahrgäste aus. An der zweiten Haltestelle steigt die Hälfte der übrigen Fahrgäste aus. An der dritten steigen 8 Fahrgäste ein. Danach sind 20 Fahrgäste im Zug. Wie viele Fahrgäste waren vor der ersten Haltestelle im Zug?",
    38, "(20 - 8) * 2 + 14", lambda: next(n for n in range(1, 200) if (n - 14) % 2 == 0 and (n - 14) // 2 + 8 == 20),
    "Rückwärts, der letzte Schritt zuerst. Vor der dritten Haltestelle: 20 − 8 = 12 Fahrgäste. Nach der ersten waren es doppelt so viele wie nach der zweiten: 12 · 2 = 24. Vor der ersten: 24 + 14 = 38. Probe: 38 − 14 = 24, die Hälfte steigt aus: 12, dann +8 = 20.",
    [(26, "Das Halbieren nicht umgekehrt: 20 − 8 + 14", "20 - 8 + 14"), (70, "Die 8 addiert statt abgezogen: (20 + 8) · 2 + 14", "(20 + 8) * 2 + 14"), (34, "Nur 20 + 14 gerechnet", "20 + 14")], einheit="Fahrgäste"), form="umkehren", regel=RG, idee="kette_rueckwaerts")
neu(T, "sach", "korrektur", "umkehr", Z(
    "Zoe hat 24 € in ihrer Spardose. Sie legt 7 Wochen lang jede Woche denselben Betrag hinein. Danach sind 66 € in der Dose. Wie viel Euro legt sie pro Woche hinein?",
    6, "(66 - 24) // 7", lambda: next(x for x in range(1, 50) if 24 + 7 * x == 66),
    "Gespart hat sie 66 − 24 = 42 €. Das verteilt sich auf 7 Wochen: 42 : 7 = 6. Probe: 24 + 7 · 6 = 66.",
    [(42, "Das Teilen durch 7 vergessen: 66 − 24", "66 - 24"), (90, "Die 24 € addiert statt abgezogen: 66 + 24", "66 + 24"), (9, "Nur 66 durch 7 geteilt (ganzzahlig)", "66 // 7")], einheit="€"), form="umkehren", regel=RG, idee="gesamt_teil_anzahl")
neu(T, "sach", "korrektur", "darstellung", W(
    "Ein Kind hat am Anfang einen Betrag □. Es kauft 3 Eis zu je 2 €. Dann bekommt es 5 € geschenkt. Jetzt hat es 20 €. Welche Gleichung beschreibt die Geschichte?",
    "□ − 3 · 2 + 5 = 20",
    [("□ − 3 · (2 + 5) = 20", "Das Geschenk in die Klammer gezogen: Lösung wäre 41", 41 - 3 * (2 + 5) == 20 and 21 - 3 * (2 + 5) != 20),
     ("□ + 3 · 2 − 5 = 20", "Plus und Minus vertauscht: Lösung wäre 19", 19 + 3 * 2 - 5 == 20 and 21 + 3 * 2 - 5 != 20),
     ("(□ − 3) · 2 + 5 = 20", "Falsch geklammert: Die Gleichung hat keine natürliche Lösung", (21 - 3) * 2 + 5 != 20)],
    "Am Anfang □. Die Eis kosten 3 · 2 €: □ − 3 · 2. Dann kommen 5 € dazu: □ − 3 · 2 + 5. Jetzt sind es 20 €. Die Lösung ist □ = 21, denn 21 − 6 + 5 = 20. Bei den anderen Gleichungen kommt mit 21 nicht 20 heraus.",
    21 - 3 * 2 + 5 == 20), form="bruecke", regel=RG, idee="gleichung_aufstellen")
neu(T, "sach", "korrektur", "umkehr", Z(
    "Mia denkt sich eine Zahl, addiert 6 und verdoppelt das Ergebnis. Sie erhält 30. Tom nimmt dieselbe Zahl, verdoppelt sie aber zuerst und addiert dann 6. Welches Ergebnis erhält Tom?",
    24, "(30 // 2 - 6) * 2 + 6", lambda: (lambda x: x * 2 + 6)(next(x for x in range(0, 100) if (x + 6) * 2 == 30)),
    "Mias Zahl: Zuletzt wurde verdoppelt, also war es vorher 30 : 2 = 15. Davor wurde 6 addiert: 15 − 6 = 9. Tom rechnet mit 9: erst verdoppeln, 9 · 2 = 18, dann 6 addieren: 18 + 6 = 24.",
    [(30, "Dasselbe Ergebnis wie Mia genommen: die Reihenfolge für egal gehalten", "30"), (36, "Mias Zahl falsch bestimmt: die 6 nicht abgezogen", "30 // 2 * 2 + 6"), (9, "Nur Mias gedachte Zahl genannt", "30 // 2 - 6")]), form="umkehren", regel=RG, idee="reihenfolge_vertauschen")
neu(T, "sach", "sicherung", "verknuepfen", Z(
    "Tarif A kostet 12 € Grundgebühr und 2 € für jedes Gigabyte. Tarif B kostet 4 € Grundgebühr und 4 € für jedes Gigabyte. Bei wie vielen Gigabyte kosten beide Tarife gleich viel?",
    4, "(12 - 4) // (4 - 2)", lambda: next(g for g in range(0, 100) if 12 + 2 * g == 4 + 4 * g),
    "B ist am Anfang 12 − 4 = 8 € billiger, aber jedes Gigabyte kostet bei B 4 − 2 = 2 € mehr. Nach 8 : 2 = 4 Gigabyte ist der Unterschied aufgebraucht. Probe: A: 12 + 4 · 2 = 20 €, B: 4 + 4 · 4 = 20 €.",
    [(8, "Nur die Grundgebühren verglichen: 12 − 4", "12 - 4"), (2, "Nur die Preise je Gigabyte verglichen: 4 − 2", "4 - 2"), (6, "Die Grundgebühr von A durch den Preis je Gigabyte von A geteilt: 12 : 2", "12 // 2")], einheit="Gigabyte"), form="zwei_wege", regel=RG, idee="gleichsetzen")
neu(T, "sach", "sicherung", "umkehr", Z(
    "Vier Gruppen sammeln jede gleich viele Flaschen. Dazu kommen 12 Flaschen vom Hausmeister. 4 Flaschen gehen kaputt. Dann sind es 108 Flaschen. Wie viele Flaschen hat jede Gruppe gesammelt?",
    25, "(108 - 12 + 4) // 4", lambda: next(x for x in range(1, 100) if 4 * x + 12 - 4 == 108),
    "Rückwärts: Die 4 kaputten Flaschen waren vorher noch da: 108 + 4 = 112. Die 12 vom Hausmeister gehören nicht zu den Gruppen: 112 − 12 = 100. Auf 4 Gruppen verteilt: 100 : 4 = 25. Probe: 4 · 25 + 12 − 4 = 108.",
    [(23, "Die kaputten Flaschen falsch herum gerechnet: (108 − 12 − 4) : 4", "(108 - 12 - 4) // 4"), (31, "Beide Mengen addiert: (108 + 12 + 4) : 4", "(108 + 12 + 4) // 4"), (100, "Das Teilen durch 4 vergessen: 108 − 12 + 4", "108 - 12 + 4")], einheit="Flaschen"), form="umkehren", regel=RG, idee="gesamt_teil_anzahl")
neu(T, "sach", "sicherung", "begruenden", W(
    "Ich denke mir eine Zahl, verdopple sie und addiere 6. Ich erhalte 30. Ben rechnet rückwärts: 30 : 2 = 15, dann 15 − 6 = 9. Welche Aussage über Bens Rechnung stimmt?",
    "Fehler: Die Reihenfolge ist falsch. Zuerst muss 6 abgezogen werden, dann wird halbiert. Richtig wäre (30 − 6) : 2 = 12.",
    [("Fehler: Er hätte malnehmen müssen. Richtig wäre 30 · 2 − 6 = 54.", "Mal statt geteilt umgekehrt: 30 · 2 − 6 = 54", 54 * 2 + 6 != 30),
     ("Fehler: Er hätte 6 addieren müssen. Richtig wäre 30 : 2 + 6 = 21.", "Plus statt Minus bei der Umkehrung: 30 : 2 + 6 = 21", 21 * 2 + 6 != 30),
     ("Kein Fehler: Man kehrt die Schritte in derselben Reihenfolge um, in der man sie gemacht hat.", "Falsche Regel bestätigt: 9 verdoppelt plus 6 ist 24, nicht 30", 9 * 2 + 6 != 30)],
    "Der letzte Schritt (plus 6) wird zuerst umgekehrt: 30 − 6 = 24. Dann der erste Schritt (verdoppeln) mit Geteilt durch 2: 24 : 2 = 12. Probe: 12 · 2 + 6 = 30. Bens 9 würde nur 24 ergeben.",
    12 * 2 + 6 == 30), regel=RG, idee="fehler_richtigstellen")
