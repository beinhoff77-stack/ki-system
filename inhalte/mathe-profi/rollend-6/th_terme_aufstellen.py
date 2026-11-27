T = "terme.aufstellen"
# ───────── struktur ─────────
neu(T, "struktur", "lueckenweg", L(
    "Die letzte Rechnung bestimmt die Termart. Beim Term (3 + a) · 4 − 2 wird zuletzt etwas abgezogen. Setze a = 5 ein. Die Klammer hat den Wert ①. Der Teil vor dem letzten Rechenzeichen, (3 + a) · 4, hat den Wert ②. Der ganze Term hat den Wert ③.",
    KOMM(3), [8, 32, 30], ["3 + 5", "{1} * 4", "{2} - 2"], ["8", "32", "30"], "Die Klammer wird zuerst gerechnet.",
    "Klammer: 3 + 5 = 8. Der Teil vor dem Abziehen: 8 · 4 = 32. Zuletzt minus 2: 30.",
    {0: [(15, None, "3 mal 5 gerechnet statt 3 plus 5", "3 * 5")], 1: [(23, None, "die Klammer ignoriert: 3 + 5 · 4", "3 + 5 * 4")], 2: [(34, None, "plus statt minus 2", "{2} + 2")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.algebra.term")
neu(T, "struktur", "verfahren_waehlen", W(
    "Du sollst die Termart von 2 · (x + 5) bestimmen. Welcher Weg führt sicher zum Ziel?",
    "Ein Zahlenbeispiel (x = 1) in der richtigen Reihenfolge durchrechnen (Klammer 6, dann mal 2) und die letzte Rechnung benennen: ein Produkt.",
    [("Von links nach rechts rechnen: zuerst 2 · x, dann + 5. Also eine Summe.", "die Klammer ignoriert"),
     ("Die Klammer weglassen, denn Klammern ändern die Termart nicht: eine Summe aus 2 · x und 5.", "Klammern als unwichtig behandelt"),
     ("Den Term in Wörter fassen: zwei plus x plus fünf. Also eine Summe.", "das Malzeichen und die Klammer übersehen")],
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
    "Berechne den Wert von 4 · (a + 3) − 2a für a = 5 auf zwei Wegen. Weg A: Setze a = 5 sofort ein. Weg B: Multipliziere die Klammer aus (jedes Glied in der Klammer mal 4), fasse gleiche Buchstabenteile zusammen und setze dann a = 5 ein. Wie groß ist der Wert des Terms?",
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
    "Ein Taxi berechnet eine feste Grundgebühr und dazu einen festen Preis je Kilometer. Eine Fahrt über 4 km kostet 11 €, eine Fahrt über 5 km kostet 13 €. Jeder Kilometer kostet ① €. Die Grundgebühr beträgt ② €. Der Preis für k Kilometer ist der Term ② + ① · k. Eine Fahrt über 12 km kostet ③ €. Eine Hin- und Rückfahrt über je 12 km kostet zusammen ④ €.",
    KOMM(4), [2, 3, 27, 54], ["13 - 11", "11 - 4 * {1}", "{2} + {1} * 12", "2 * {3}"], ["2", "3", "27", "54"], "Was kommt von 4 km auf 5 km dazu?",
    "Ein Kilometer mehr kostet 13 € − 11 € = 2 €. Für 4 km zahlt man 4 · 2 € = 8 €, die restlichen 3 € sind die Grundgebühr. Term: 3 + 2 · k. 12 km: 3 + 2 · 12 = 27 €. Hin und zurück: 2 · 27 € = 54 €.",
    {0: [(24, None, "die beiden Preise addiert: 11 + 13", "11 + 13")], 1: [(7, None, "vom Preis der 4-km-Fahrt nur 4 abgezogen: 11 − 4", "11 - 4")],
     2: [(24, None, "nur den Kilometerpreis mal 12 gerechnet, die Grundgebühr vergessen: 12 · Kilometerpreis", "12 * {1}")], 3: [(27, None, "nur eine der beiden Fahrten gerechnet", "{3}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.algebra.term")
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
    "Im Kino kostet eine Kinderkarte 7 € und eine Erwachsenenkarte 9 €. Eine Familie kauft Karten für k Kinder und 2 Erwachsene. Der Preis in Euro ist der Term 7 · k + ①. Für 3 Kinder zahlt die Familie ② €. Mit einem 50-Euro-Schein bekommt sie dann ③ € zurück. Für 4 Kinder zahlt sie ④ €.",
    KOMM(4), [18, 39, 11, 46], ["9 * 2", "7 * 3 + {1}", "50 - {2}", "7 * 4 + {1}"], ["18", "39", "11", "46"], "Der feste Teil des Preises hängt nicht von k ab.",
    "Die Erwachsenenkarten kosten 2 · 9 € = 18 €, unabhängig von k. 3 Kinder: 7 · 3 + 18 = 39 €. Rückgeld: 50 € − 39 € = 11 €. 4 Kinder: 7 · 4 + 18 = 46 €.",
    {0: [(9, None, "nur eine Erwachsenenkarte gerechnet", "9"), (14, None, "die Erwachsenen mit dem Kinderpreis gerechnet: 2 · 7", "2 * 7")], 1: [(21, None, "den festen Teil vergessen: 7 · 3", "7 * 3")],
     2: [(39, None, "den Preis statt des Rückgelds angegeben", "{2}")], 3: [(28, None, "den festen Teil vergessen: 7 · 4", "7 * 4")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.algebra.term")
neu(T, "sachsituation", "anwenden", W(
    "Am Schulkiosk kostet eine Brezel 0,80 € und ein Apfel 0,60 €. Ein Kind kauft b Brezeln und 2 Äpfel und bezahlt mit einem 5-Euro-Schein. Welcher Term gibt an, wie viel Euro es zurückbekommt?",
    "5 − (0,80 · b + 2 · 0,60)",
    [("5 − 0,80 · b + 2 · 0,60", "Klammer vergessen: die Äpfel werden zum Rückgeld addiert statt abgezogen"),
     ("5 − 0,80 · (b + 2) − 0,60", "den Preis für 2 Äpfel mit dem Brezelpreis gerechnet"),
     ("(5 − 0,80) · b − 2 · 0,60", "den Schein mit b malgenommen")],
    "Was kosten alle Brezeln und alle Äpfel zusammen? Das Rückgeld ist der Rest vom Schein.",
    "b Brezeln kosten 0,80 · b €, 2 Äpfel kosten 2 · 0,60 €. Zusammen 0,80 · b + 2 · 0,60. Das Rückgeld ist 5 − (0,80 · b + 2 · 0,60). Probe b = 3: 5 − (2,40 + 1,20) = 1,40 €.",
    lambda: all(F(5) - (F(8, 10) * b + 2 * F(6, 10)) != F(5) - F(8, 10) * b + 2 * F(6, 10) and F(5) - (F(8, 10) * b + 2 * F(6, 10)) != F(5) - F(8, 10) * (b + 2) - F(6, 10) and F(5) - (F(8, 10) * b + 2 * F(6, 10)) != (F(5) - F(8, 10)) * b - 2 * F(6, 10) for b in (3, 4))), regel="id.algebra.term")
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
    "Das Ausleihen eines Rollers kostet 4x + 15 Euro, wobei x die Zahl der Stunden ist. Für 8 Stunden zahlt man ① €. Verlängert man um 3 Stunden, zahlt man für 11 Stunden ② €. Mit einem 100-Euro-Schein bekommt man dafür ③ € zurück.",
    KOMM(3), [47, 59, 41], ["4 * 8 + 15", "{1} + 4 * 3", "100 - {2}"], ["47", "59", "41"], "Wie viel Euro kommen mit jeder weiteren Stunde dazu?",
    "8 Stunden: 4 · 8 + 15 = 47. Jede weitere Stunde kostet 4 € mehr, 3 Stunden also 12 € mehr: 59 €. Probe: 4 · 11 + 15 = 59. Rückgeld: 100 € − 59 € = 41 €.",
    {0: [(152, None, "4x + 15 als (4 + 15) · x gerechnet: 19 · 8", "(4 + 15) * 8")], 1: [(62, None, "die Grundgebühr noch einmal dazugerechnet: 47 + 15", "{1} + 15"), (50, None, "nur 3 € statt 3 · 4 € dazugerechnet: 47 + 3", "{1} + 3")],
     2: [(53, None, "nur den 8-Stunden-Preis vom Schein abgezogen: 100 − 47", "100 - {1}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="id.algebra.term")
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
