T = "terme.aufstellen"
# ───────── struktur ─────────
neu(T, "struktur", "lueckenweg", L(
    "Die letzte Rechnung bestimmt die Termart. Berechne dazu (3 + a) · 4 − 2 für a = 5 Schritt für Schritt: Die Klammer hat den Wert ①. Mal 4 ergibt ②. Die letzte Rechnung, minus 2, ergibt ③. Der Term ist also eine Differenz.",
    KOMM(3), [8, 32, 30], ["3 + 5", "{1} * 4", "{2} - 2"], ["8", "32", "30"], "Die Klammer wird zuerst gerechnet.",
    "Klammer: 3 + 5 = 8. Mal 4: 8 · 4 = 32. Minus 2: 30.",
    {0: [(15, None, "3 mal 5 gerechnet statt 3 plus 5", "3 * 5")], 1: [(23, None, "die Klammer ignoriert: 3 + 5 · 4", "3 + 5 * 4")], 2: [(34, None, "plus statt minus 2", "{2} + 2")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.algebra.term")
neu(T, "struktur", "verfahren_waehlen", W(
    "Welche Aussage beschreibt den Aufbau des Terms 2 · (x + 5) richtig?",
    "Ein Produkt aus 2 und der Summe x + 5",
    [("Eine Summe aus 2 · x und 5", "die Klammer ignoriert"), ("Eine Summe aus 2 und x + 5", "das Malzeichen übersehen"), ("Eine Differenz aus 2 · x und 5", "ein Minus erfunden")],
    "Welche Rechenart wird zuletzt ausgeführt?",
    "Zuerst wird x + 5 gerechnet (Klammer), zuletzt wird mit 2 malgenommen. Also ein Produkt aus 2 und der Summe x + 5. Probe mit x = 1: 2 · 6 = 12, aber 2 · 1 + 5 = 7.",
    lambda: 2 * (1 + 5) != 2 * 1 + 5), g="mehrschritt", regel="id.algebra.term")
neu(T, "struktur", "fehler_detektiv", FD(
    "Tim berechnet 3 + 4 · a für a = 2.",
    [("Man rechnet zuerst 3 + 4 und dann mal a.", 3 + 4 * 2 == (3 + 4) * 2), ("3 + 4 = 7, also 7 · 2 = 14", (3 + 4) * 2 == 14), ("Der Wert des Terms ist 14.", True)],
    "Welche Rechnung kommt zuerst: Plus oder Mal?", "Punktrechnung geht vor Strichrechnung: 4 · 2 = 8, dann 3 + 8 = 11. Zeile 1 beschreibt eine falsche Reihenfolge, die Folgezeilen rechnen damit richtig weiter.", rueck={1: '3 + 4 = 7 und 7 · 2 = 14 ist für sich richtig gerechnet. Es folgt aber der falschen Reihenfolge aus Zeile 1; dort steht der erste Fehler.', 2: 'Zeile 3 übernimmt nur das Ergebnis aus Zeile 2. Der erste Fehler steht schon in Zeile 1.'}), regel="id.algebra.term")

# ───────── termwert ─────────
neu(T, "termwert", "lueckenweg", L(
    "Berechne 2a² − 3b für a = 4 und b = 5. Zuerst die Potenz a²: ①. Dann 2 mal diese Zahl: ②. Dann 3b: ③. Der Termwert ist ④.",
    KOMM(4), [16, 32, 15, 17], ["4 ** 2", "2 * {1}", "3 * 5", "{2} - {3}"], ["16", "32", "15", "17"], "Die Hochzahl 2 gehört nur zur 4, nicht zur 2 davor.",
    "4² = 16. 2 · 16 = 32. 3 · 5 = 15. 32 − 15 = 17.",
    {0: [(8, None, "Basis mal Hochzahl: 4 · 2", "4 * 2")], 1: [(64, None, "erst 2 · 4 = 8, dann quadriert", "(2 * 4) ** 2")], 2: [(8, None, "3 + 5 gerechnet", "3 + 5")], 3: [(47, None, "plus statt minus", "{2} + {3}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.algebra.term")
neu(T, "termwert", "zwei_wege", Z(
    "Berechne den Wert von 4 · (a + 3) − 2a für a = 5 auf zwei Wegen. Weg A: Setze a = 5 sofort ein. Weg B: Multipliziere die Klammer aus, fasse zusammen und setze dann a = 5 ein. Wie groß ist der Wert des Terms?",
    22, "4 * (5 + 3) - 2 * 5", "2 * 5 + 12", "Beide Wege müssen denselben Wert ergeben.",
    "Weg A: 4 · 8 − 10 = 32 − 10 = 22. Weg B: 4a + 12 − 2a = 2a + 12. Für a = 5: 10 + 12 = 22.",
    [(13, None, "nur 4 · a ausmultipliziert, die 3 vergessen mit 4 zu multiplizieren", "4 * 5 + 3 - 2 * 5"), (42, None, "plus statt minus 2a", "4 * (5 + 3) + 2 * 5")]), g="mehrschritt", regel="id.algebra.term")
neu(T, "termwert", "umkehren", Z(
    "Für welchen Wert von a hat der Term 4a − 3 den Wert 21?",
    6, "(21 + 3) / 4", "24 / 4", "Kehre die Rechenschritte um, beginnend beim letzten.",
    "4a − 3 = 21. Erst 3 addieren: 4a = 24. Dann durch 4 teilen: a = 6. Probe: 4 · 6 − 3 = 21.",
    [(4.5, None, "3 abgezogen statt addiert", "(21 - 3) / 4"), (24, None, "nur 3 addiert, nicht durch 4 geteilt", "21 + 3")]), g="rueckwaerts", regel="id.algebra.term")

# ───────── uebersetzen ─────────
neu(T, "uebersetzen", "lueckenweg", L(
    "Ein Taxi kostet 3 € Grundgebühr und 2 € für jeden gefahrenen Kilometer. Für k Kilometer ergibt das den Term 3 + 2 · k. Setze ein: Eine Fahrt über 7 km kostet ① €. Eine Fahrt über 12 km kostet ② €. Die längere Fahrt ist um ③ € teurer. Zwei Fahrten über je 12 km kosten zusammen ④ €.",
    KOMM(4), [17, 27, 10, 54], ["3 + 2 * 7", "3 + 2 * 12", "{2} - {1}", "2 * {2}"], ["17", "27", "10", "54"], "Die Grundgebühr zahlst du nur einmal je Fahrt.",
    "7 km: 3 € + 2 · 7 € = 17 €. 12 km: 3 € + 2 · 12 € = 27 €. Unterschied: 27 € − 17 € = 10 €. Zwei Fahrten über 12 km: 2 · 27 € = 54 €.",
    {0: [(35, None, "die Grundgebühr mit dazugerechnet: (3 + 2) · 7", "(3 + 2) * 7")], 1: [(36, None, "nur 3 mal 12 gerechnet", "3 * 12")], 2: [(44, None, "addiert statt abgezogen", "{1} + {2}")],
     3: [(27, None, "nur eine der beiden Fahrten gerechnet", "{2}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.algebra.term")
neu(T, "uebersetzen", "bruecke", W(
    "Welcher Term passt zu dem Satz: „Das Doppelte von x, vermindert um 5“?",
    "2x − 5",
    [("2 · (x − 5)", "die Klammer falsch gesetzt: erst 5 abgezogen, dann verdoppelt"), ("x² − 5", "das Doppelte mit dem Quadrat verwechselt"), ("2 + x − 5", "das Doppelte mit „plus 2“ verwechselt")],
    "Was passiert zuerst mit x, was danach?",
    "Das Doppelte von x ist 2x. Davon werden 5 abgezogen: 2x − 5. Probe mit x = 7: Doppeltes 14, minus 5 ergibt 9.",
    lambda: [2 * 7 - 5, 2 * (7 - 5), 7 ** 2 - 5, 2 + 7 - 5] == [9, 4, 44, 4] or len({2 * 7 - 5, 2 * (7 - 5), 7 ** 2 - 5}) == 3), regel="id.algebra.term")
neu(T, "uebersetzen", "anwenden", Z(
    "Alex ist a Jahre alt. Seine Schwester ist 3 Jahre jünger als er. Sein Vater ist dreimal so alt wie Alex und noch 2 Jahre älter. Alex ist 11 Jahre alt. Wie viele Jahre sind die drei zusammen alt?",
    54, "11 + (11 - 3) + (3 * 11 + 2)", "5 * 11 - 1", "Schreibe für jede Person einen Term mit a auf.",
    "Alex: a. Schwester: a − 3. Vater: 3a + 2. Zusammen: a + (a − 3) + (3a + 2) = 5a − 1. Für a = 11: 55 − 1 = 54. Probe: 11 + 8 + 35 = 54.",
    [(52, None, "beim Vater die 2 Jahre vergessen", "11 + 8 + 3 * 11"), (60, None, "die Schwester 3 Jahre älter statt jünger", "11 + (11 + 3) + (3 * 11 + 2)")]), g="transfer", regel="id.algebra.term")

# ───────── sachsituation ─────────
neu(T, "sachsituation", "lueckenweg", L(
    "Im Kino kostet eine Kinderkarte 7 € und eine Erwachsenenkarte 9 €. Eine Familie mit 3 Kindern und 2 Erwachsenen kauft Karten. Die Kinderkarten kosten zusammen ① €. Die Erwachsenenkarten kosten zusammen ② €. Alles zusammen kostet ③ €. Die Familie zahlt mit einem 50-Euro-Schein und bekommt ④ € zurück.",
    KOMM(4), [21, 18, 39, 11], ["7 * 3", "9 * 2", "{1} + {2}", "50 - {3}"], ["21", "18", "39", "11"], "Rechne erst jede Kartenart einzeln, dann zusammen.",
    "Kinder: 7 € · 3 = 21 €. Erwachsene: 9 € · 2 = 18 €. Zusammen: 21 € + 18 € = 39 €. Rückgeld: 50 € − 39 € = 11 €.",
    {0: [(10, None, "7 + 3 gerechnet", "7 + 3")], 1: [(11, None, "9 + 2 gerechnet", "9 + 2")], 2: [(378, None, "malgenommen statt addiert", "{1} * {2}")],
     3: [(89, None, "addiert statt abgezogen", "50 + {3}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.algebra.term")
neu(T, "sachsituation", "anwenden", Z(
    "Am Schulkiosk kostet eine Brezel 0,80 € und ein Apfel 0,60 €. Ein Kind kauft 3 Brezeln und 2 Äpfel und bezahlt mit einem 5-Euro-Schein. Wie viel Euro bekommt es zurück?",
    1.4, "5 - (0.8 * 3 + 0.6 * 2)", "5 - 2.4 - 1.2", "Wie viel kosten die Brezeln, wie viel die Äpfel?",
    "Brezeln: 3 · 0,80 € = 2,40 €. Äpfel: 2 · 0,60 € = 1,20 €. Zusammen 3,60 €. Rückgeld: 5 € − 3,60 € = 1,40 €.",
    [(3.6, None, "den Preis statt des Rückgelds angegeben", "0.8 * 3 + 0.6 * 2"), (1.6, None, "die Stückzahlen vertauscht: 2 Brezeln und 3 Äpfel", "5 - (0.8 * 2 + 0.6 * 3)")], "€"), regel="id.algebra.term")
neu(T, "sachsituation", "zwei_wege", Z(
    "Tarif A kostet 8 € Grundgebühr und 0,05 € je Minute. Tarif B kostet 2 € Grundgebühr und 0,15 € je Minute. Weg A: Lege eine Tabelle mit den Preisen für 10, 20, 30 … Minuten an und suche die Stelle, an der beide Preise gleich sind. Weg B: Teile den Unterschied der Grundgebühren durch den Unterschied der Minutenpreise. Nach wie vielen Minuten kosten beide Tarife gleich viel?",
    60, "(8 - 2) / (0.15 - 0.05)", "60", "Wie viel mehr Grundgebühr zahlt man bei A, wie viel weniger pro Minute?",
    "Weg A: Die Tabelle zeigt bei 60 Minuten für A 8 € + 3 € = 11 € und für B 2 € + 9 € = 11 €. Weg B: 6 € Unterschied bei der Grundgebühr, pro Minute spart A 0,10 €. 6 : 0,10 = 60 Minuten.",
    [(50, None, "die Grundgebühren und die Minutenpreise addiert statt Unterschiede gebildet", "(8 + 2) / (0.15 + 0.05)"), (6, None, "nur den Unterschied der Grundgebühren angegeben", "8 - 2")], "min"), g="verknuepfen", regel="id.algebra.term")
assert 8 + 0.05 * 60 == 2 + 0.15 * 60

# ───────── muster ─────────
neu(T, "muster", "lueckenweg", L(
    "Figur 1 hat 10 Plättchen, Figur 2 hat 14 und Figur 3 hat 18. Bei jeder Figur kommen ① Plättchen dazu. Die Anzahl bei Figur n ist ①n + ②. Figur 20 hat ③ Plättchen.",
    KOMM(3), [4, 6, 86], ["14 - 10", "10 - {1}", "{1} * 20 + {2}"], ["4", "6", "86"], "Wie viele Plättchen kommen von einer Figur zur nächsten dazu?",
    "Von 10 zu 14 zu 18 sind es jedes Mal 4 mehr. Die Figur n hat 4n + 6 Plättchen (Figur 1: 4 + 6 = 10). Figur 20: 4 · 20 + 6 = 86.",
    {0: [(14, None, "das zweite Glied als Zuwachs genommen", "14")], 1: [(10, None, "das erste Glied als Konstante genommen", "10")], 2: [(80, None, "die Konstante vergessen", "{1} * 20")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.algebra.term")
neu(T, "muster", "bruecke", W(
    "Eine Wertetabelle zeigt: n = 1 ergibt 7, n = 2 ergibt 10, n = 3 ergibt 13, n = 4 ergibt 16. Welcher Term gehört zu dieser Tabelle?",
    "3n + 4",
    [("3n + 7", "den ersten Tabellenwert als Konstante genommen"), ("n + 6", "nur die erste Zeile passend gewählt"), ("7n", "mit dem ersten Wert malgenommen")],
    "Wie viel kommt von einer Zeile zur nächsten dazu? Setze dann n = 1 ein.",
    "Von Zeile zu Zeile kommen 3 dazu, also 3n + etwas. Für n = 1: 3 + 4 = 7. Probe n = 4: 3 · 4 + 4 = 16.",
    lambda: all(3 * n + 4 == 7 + 3 * (n - 1) for n in range(1, 5)) and not all(3 * n + 7 == 7 + 3 * (n - 1) for n in range(1, 5)) and not all(n + 6 == 7 + 3 * (n - 1) for n in range(1, 5)) and not all(7 * n == 7 + 3 * (n - 1) for n in range(1, 5))), regel="id.algebra.term")
neu(T, "muster", "umkehren", Z(
    "Figur n eines Musters hat 4n + 3 Plättchen. Bei welcher Figur sind es genau 27 Plättchen?",
    6, "(27 - 3) / 4", "24 / 4", "Kehre die Rechnung um: Was passiert zuletzt mit 4n?",
    "4n + 3 = 27. Erst 3 abziehen: 4n = 24. Dann durch 4 teilen: n = 6. Probe: 4 · 6 + 3 = 27.",
    [(6.75, None, "die 3 vergessen: 27 : 4", "27 / 4"), (7.5, None, "3 addiert statt abgezogen", "(27 + 3) / 4")]), g="rueckwaerts", regel="id.algebra.term")

# ───────── deuten ─────────
neu(T, "deuten", "lueckenweg", L(
    "Das Ausleihen eines Rollers kostet 4x + 15 Euro, wobei x die Zahl der Stunden ist. Für 8 Stunden zahlt man ① €. Für 9 Stunden zahlt man ② €. Für 20 Stunden zahlt man ③ €.",
    KOMM(3), [47, 51, 95], ["4 * 8 + 15", "{1} + 4", "{2} + 4 * 11"], ["47", "51", "95"], "Wie viel Euro kommen mit jeder weiteren Stunde dazu?",
    "8 Stunden: 4 · 8 + 15 = 47. Eine Stunde mehr kostet 4 € mehr: 51 €. Von 9 auf 20 Stunden sind es 11 Stunden mehr, also 11 · 4 € = 44 € mehr: 95 €.",
    {0: [(152, None, "4x + 15 als (4 + 15) · x gerechnet", "(4 + 15) * 8")], 1: [(47, None, "die zusätzliche Stunde nicht gerechnet", "{1}")], 2: [(80, None, "die Grundgebühr vergessen", "4 * 20")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.algebra.term")
neu(T, "deuten", "bruecke", W(
    "Für das Ausleihen eines Rollers gilt: Der Preis in Euro ist 4x + 15, wobei x die Zahl der Stunden ist. Was bedeutet die Rechnung 4 · 6 + 15 = 39?",
    "Für 6 Stunden zahlt man 39 €.",
    [("Für 39 Stunden zahlt man 6 €.", "x und Preis vertauscht"), ("Eine Stunde kostet 39 €.", "den Gesamtpreis mit dem Preis je Stunde verwechselt"), ("Man zahlt 15 Stunden lang je 4 €.", "Zahl der Stunden und Grundgebühr verwechselt")],
    "Was ist x? Was ist das Ergebnis der Rechnung?",
    "x ist die Zahl der Stunden. 4 · 6 steht für 6 Stunden zu je 4 €, die 15 € fallen einmal an. Das Ergebnis 39 ist der Preis in Euro.",
    lambda: 4 * 6 + 15 == 39), regel="id.algebra.term")
neu(T, "deuten", "fehler_detektiv", FD(
    "Nina vereinfacht den Term 4x + 15, der den Preis für das Ausleihen eines Rollers für x Stunden beschreibt.",
    [("Man darf die Zahlen 4 und 15 zusammenzählen: 4x + 15 = 19x.", all(4 * x + 15 == 19 * x for x in (2, 3))), ("Für x = 2 ergibt 19x den Wert 38.", 19 * 2 == 38), ("Also kostet das Ausleihen für 2 Stunden 38 €.", True)],
    "Setze x = 2 in den ursprünglichen Term ein und vergleiche.", "4x + 15 hat für x = 2 den Wert 4 · 2 + 15 = 23. Die 15 gehört nicht zu x, man darf sie nicht mit der 4 zusammenzählen. Die Zeilen 2 und 3 rechnen mit 19x richtig weiter.", rueck={1: 'Für x = 2 ergibt 19x tatsächlich 38. Der Term 19x ist aber durch den Fehler in Zeile 1 entstanden; dort steht der erste Fehler.', 2: 'Zeile 3 übernimmt nur den Wert aus Zeile 2. Der erste Fehler steht schon in Zeile 1.'}), regel="id.algebra.term")
