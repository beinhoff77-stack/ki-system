T = "gleichungen.linear"
WG = "rr.waage"
# ───────── waage ─────────
neu(T, "waage", "lueckenweg", L(
    "Du löst 6x − 23 = 2x + 37 mit der Waage. Subtrahiere auf beiden Seiten 2x, dann steht links ① · x − 23. Addiere auf beiden Seiten 23, dann steht rechts die Zahl ②. Zum Schluss ist x = ③.",
    "① = □; ② = □; ③ = □", [4, 60, 15], ["6 - 2", "37 + 23", "{2} / {1}"], ["4", "60", "15"],
    "Was du auf der einen Seite tust, tust du auf der anderen Seite auch. Erst die x-Glieder sammeln, dann die Zahlen.",
    "6x − 2x = 4x. Dann 4x − 23 = 37, nach Addieren von 23 ist 4x = 60. Teilen durch 4 gibt x = 15. Probe: 6 · 15 − 23 = 67 und 2 · 15 + 37 = 67.",
    {0: [(8, None, "die x-Glieder addiert statt subtrahiert", "6 + 2")], 1: [(14, None, "die 23 subtrahiert statt addiert", "37 - 23")], 2: [(240, None, "60 mit 4 malgenommen statt durch 4 geteilt", "{2} * {1}")]}), regel=WG)
neu(T, "waage", "anwenden", Z(
    "Für ein Leihrad am Gardasee zahlt man 14 € Grundgebühr und dazu 3,50 € je Stunde. Alex zahlt insgesamt 49 €. Wie viele Stunden war das Rad geliehen?",
    10, "(49 - 14) / 3.5", "49 / 3.5 - 14 / 3.5", "Beschreibe die Rechnung mit einer Gleichung: 14 + 3,5 · x = 49. Löse sie mit der Waage.",
    "Gleichung: 14 + 3,5x = 49. Subtrahiere 14: 3,5x = 35. Teile durch 3,5: x = 10. Das Rad war 10 Stunden geliehen. Probe: 14 + 3,5 · 10 = 49.",
    [B("49 / 3.5", "die Grundgebühr nicht abgezogen"), B("49 - 14", "nach dem Abziehen der Grundgebühr nicht durch den Preis je Stunde geteilt"), B("(49 + 14) / 3.5", "die Grundgebühr addiert statt abgezogen")], einheit="h"), g="einkleidung", regel=WG)
neu(T, "waage", "fehler_detektiv", FD(
    "Sam löst 4x + 9 = 6x − 5 mit der Waage:",
    [("Auf der linken Seite subtrahiere ich 4x, dann bleibt 9 = 6x − 5.", gleichwertig("4*x+9=6*x-5", "9=6*x-5"), True),
     ("Addiere ich 5, steht dort 14 = 6x.", True, gleichwertig("9=6*x-5", "14=6*x")),
     ("Teile ich durch 6, ist x = 7/3.", True, loes("14=6*x") == F(7, 3))],
    "Prüfe Zeile 1: Auf welchen Seiten wurde 4x subtrahiert? Was steht dann rechts?",
    "Die Waage bleibt nur im Gleichgewicht, wenn man auf beiden Seiten dasselbe tut. In Zeile 1 wurde 4x nur links subtrahiert. Richtig: 9 = 2x − 5, dann 14 = 2x und x = 7. Die Zeilen 2 und 3 rechnen mit dem falschen Ergebnis aus Zeile 1 richtig weiter."), g="fehler", regel=WG)
# ───────── beide_seiten ─────────
neu(T, "beide_seiten", "anwenden", Z(
    "Beim Telefonieren im Ausland hat Tarif A eine Grundgebühr von 18 € und 0,25 € je Minute. Tarif B hat keine Grundgebühr und kostet 0,40 € je Minute. Nach wie vielen Minuten Gesprächszeit kosten beide Tarife gleich viel?",
    120, "18 / (0.40 - 0.25)", "18 / 0.15", "Stelle für beide Tarife den Preis nach x Minuten auf und setze die Preise gleich.",
    "Tarif A: 18 + 0,25x. Tarif B: 0,40x. Gleichsetzen: 18 + 0,25x = 0,40x. Subtrahiere 0,25x: 18 = 0,15x. Teile durch 0,15: x = 120 Minuten. Probe: 18 + 30 = 48 und 0,40 · 120 = 48.",
    [B("18 / 0.25", "nur durch den Minutenpreis von Tarif A geteilt"), B("18 / 0.40", "nur durch den Minutenpreis von Tarif B geteilt"), B("18 * 0.15", "mit dem Unterschied malgenommen statt geteilt")], einheit="min"), g="einkleidung", regel=WG)
neu(T, "beide_seiten", "verfahren_waehlen", W(
    "Welche Gleichung hat dieselbe Lösung wie 8x − 30 = 3x + 25?",
    "5x = 55", [("11x = 55", "3x mit falschem Vorzeichen auf die linke Seite gebracht"), ("5x = −5", "die 30 von der 25 abgezogen statt addiert"), ("5x = 25", "bei der Zahl nur die 30 weggelassen")],
    "Löse die gegebene Gleichung und prüfe, bei welcher Gleichung dieselbe Zahl herauskommt.",
    "8x − 30 = 3x + 25. Subtrahiere 3x: 5x − 30 = 25. Addiere 30: 5x = 55, also x = 11. Die Gleichung 5x = 55 hat ebenfalls die Lösung 11. Die anderen haben die Lösungen 5, −1 und 5.",
    lambda: gleichwertig("8*x-30=3*x+25", "5*x=55") and not any(gleichwertig("8*x-30=3*x+25", e) for e in ("11*x=55", "5*x=-5", "5*x=25"))), g="mehrschritt", regel=WG)
neu(T, "beide_seiten", "umkehren", Z(
    "Für welche Zahl haben die Terme 7x − 8 und 3x + 40 denselben Wert?",
    12, "(40 + 8) / (7 - 3)", int(loes("7*x-8=3*x+40")), "Setze die beiden Terme gleich und löse die Gleichung.",
    "7x − 8 = 3x + 40. Subtrahiere 3x: 4x − 8 = 40. Addiere 8: 4x = 48. Teile durch 4: x = 12. Probe: 7 · 12 − 8 = 76 und 3 · 12 + 40 = 76.",
    [B("(40 - 8) / (7 + 3)", "ein Minus beim Umformen verloren und 3x addiert statt subtrahiert"), B("48 / 7", "3x gar nicht beachtet"), B("(40 - 8) / (7 - 3)", "die 8 abgezogen statt addiert")]), g="rueckwaerts", regel=WG)
# ───────── klammern ─────────
neu(T, "klammern", "lueckenweg", L(
    "Du löst 5(x − 4) = 2x + 19. Nach dem Ausmultiplizieren steht links 5x − ①. Subtrahiere 2x, dann steht links 3x − ①. Addiere ① auf beiden Seiten: 3x = ②. Also ist x = ③.",
    "① = □; ② = □; ③ = □", [20, 39, 13], ["5 * 4", "19 + {1}", "{2} / 3"], ["20", "39", "13"],
    "Der Faktor vor der Klammer wird mit jedem Summanden in der Klammer malgenommen.",
    "5(x − 4) = 5x − 20. Dann 5x − 20 = 2x + 19. Subtrahiere 2x: 3x − 20 = 19. Addiere 20: 3x = 39. Teile durch 3: x = 13. Probe: 5 · 9 = 45 und 2 · 13 + 19 = 45.",
    {0: [(4, None, "die 4 nicht mit dem Faktor 5 malgenommen", "4")], 1: [(-1, None, "19 − 20 gerechnet statt 19 + 20", "19 - {1}")], 2: [(117, None, "mit 3 malgenommen statt durch 3 geteilt", "{2} * 3")]}), regel=WG)
neu(T, "klammern", "anwenden", Z(
    "Kim löst 3(2x − 5) − (x − 4) = 24 und gibt als Lösung x = ? an. Wie lautet sie?",
    7, "(24 + 11) / 5", int(loes("3*(2*x-5)-(x-4)=24")), "Löse zuerst beide Klammern auf, achte auf das Minus vor der zweiten Klammer. Fasse dann zusammen.",
    "3(2x − 5) = 6x − 15 und −(x − 4) = −x + 4. Links: 5x − 11 = 24. Addiere 11: 5x = 35. Teile durch 5: x = 7. Probe: 3 · 9 − 3 = 24.",
    [B("(24 + 15 + 4) / 5", "das Minus nur vor das x gesetzt, die 4 behielt ihr Vorzeichen"), B("(24 - 11) / 5", "die 11 auf der falschen Seite abgezogen"), B("(24 + 15) / 6", "die zweite Klammer ignoriert")]), g="mehrschritt", regel=WG)
neu(T, "klammern", "fehler_detektiv", FD(
    "Noa löst 5(x − 2) = 3x + 6:",
    [("Ausmultiplizieren: 5x − 2 = 3x + 6.", gleichwertig("5*(x-2)=3*x+6", "5*x-2=3*x+6"), True),
     ("Subtrahiere ich 3x, bleibt 2x − 2 = 6.", True, gleichwertig("5*x-2=3*x+6", "2*x-2=6")),
     ("Addiere ich 2, ist 2x = 8, also ist x = 4.", True, loes("2*x-2=6") == 4)],
    "Wie oft wird die 5 beim Ausmultiplizieren verwendet? Prüfe die Klammer Summand für Summand.",
    "Der Faktor 5 gilt für jeden Summanden in der Klammer: 5(x − 2) = 5x − 10. In Zeile 1 wurde die 2 nicht mit 5 malgenommen. Richtig: 5x − 10 = 3x + 6, daraus 2x = 16 und x = 8. Die Zeilen 2 und 3 rechnen mit dem falschen Ergebnis richtig weiter."), g="fehler", regel=WG)
# ───────── probe ─────────
neu(T, "probe", "anwenden", Z(
    "Kim behauptet, die Lösung von 4x − 9 = 2x + 13 ist x = 11. Setzt man 11 ein, so haben beide Seiten denselben Wert. Wie groß ist er?",
    35, "4 * 11 - 9", "2 * 11 + 13", "Setze 11 für x ein: links und rechts. Beide Seiten müssen denselben Wert ergeben.",
    "Links: 4 · 11 − 9 = 44 − 9 = 35. Rechts: 2 · 11 + 13 = 22 + 13 = 35. Beide Seiten sind 35, die Probe stimmt.",
    [B("4 * 11 + 9", "die 9 addiert statt subtrahiert"), B("2 * 11", "die Zahl 13 vergessen"), B("(4 - 2) * 11 - 9 + 13", "die x-Glieder beider Seiten zu 2x zusammengefasst und dann 2 · 11 − 9 + 13 gerechnet")]), g="pruefung", regel=WG)
neu(T, "probe", "verfahren_waehlen", W(
    "Welche dieser Zahlen ist Lösung der Gleichung 6x − 17 = 2x + 15? Prüfe durch Einsetzen.",
    "x = 8", [("x = 4", "links 7, rechts 23: die beiden Seiten sind verschieden"), ("x = 12", "links 55, rechts 39: die beiden Seiten sind verschieden")],
    "Setze jede Zahl links und rechts ein und vergleiche.",
    "x = 8: links 6 · 8 − 17 = 31, rechts 2 · 8 + 15 = 31. Gleich, also ist 8 die Lösung. Bei 4 sind die Seiten 7 und 23, bei 12 sind sie 55 und 39.",
    lambda: ist_loesung("6*x-17", "2*x+15", 8) and not ist_loesung("6*x-17", "2*x+15", 4) and not ist_loesung("6*x-17", "2*x+15", 12)), g="pruefung", regel=WG)
# ───────── sonderfaelle ─────────
neu(T, "sonderfaelle", "verfahren_waehlen", W(
    "Wie viele Lösungen hat die Gleichung 5(x + 2) − 3x = 2x + 13?",
    "keine Lösung", [("genau eine Lösung", "x steht auf beiden Seiten gleich oft, trotzdem bleibt nicht x = Zahl übrig"), ("unendlich viele Lösungen", "nach dem Zusammenfassen stehen links 10 und rechts 13, das ist nie gleich")],
    "Fasse beide Seiten zusammen. Was bleibt nach dem Subtrahieren von 2x übrig?",
    "5(x + 2) − 3x = 5x + 10 − 3x = 2x + 10. Die Gleichung heißt 2x + 10 = 2x + 13. Subtrahiere 2x: 10 = 13. Das ist falsch, egal welche Zahl x ist: keine Lösung.",
    lambda: loes("5*(x+2)-3*x=2*x+13") == "keine"), g="mehrschritt", regel=WG)
neu(T, "sonderfaelle", "umkehren", Z(
    "Für welche Zahl k hat die Gleichung 5(x + 2) − 3x = 2x + k unendlich viele Lösungen?",
    10, "5 * 2", 10, "Fasse die linke Seite zusammen. Wann stehen links und rechts dieselben Terme?",
    "5(x + 2) − 3x = 2x + 10. Die Gleichung heißt 2x + 10 = 2x + k. Sie stimmt für jede Zahl x genau dann, wenn k = 10 ist.",
    [B("5 + 2", "nur die Zahlen in der Klammer addiert"), B("5 * 2 + 3", "zur 10 noch die 3 addiert"), B("5 * 2 - 3 * 2", "die 3x als Zahl eingesetzt")]), g="parameter", regel=WG)
neu(T, "sonderfaelle", "fehler_detektiv", FD(
    "Alex löst 6x − 4 = 2(3x + 5) − 1:",
    [("Rechts ausmultiplizieren und zusammenfassen: 2(3x + 5) − 1 = 6x + 9.", gleichwertig("6*x-4=2*(3*x+5)-1", "6*x-4=6*x+9"), True),
     ("Subtrahiere ich 6x auf beiden Seiten, bleibt links −4 und rechts 9 stehen.", True, True),
     ("Diese Aussage stimmt nicht und enthält kein x mehr.", True, True),
     ("Also ist x = 0 die einzige Lösung.", False, True)],
    "Was bedeutet es, wenn nach dem Umformen eine falsche Aussage ohne x dasteht?",
    "Eine falsche Aussage wie −4 = 9 gilt für jede Zahl x nicht. Die Gleichung hat deshalb keine Lösung. Zeile 4 ist falsch: x = 0 ergibt links −4 und rechts 9."), g="fehler", regel=WG)
# ───────── sach ─────────
neu(T, "sach", "anwenden", Z(
    "Kim startet in Passau mit dem Rad und fährt mit 18 km/h donauabwärts. Alex startet 2 Stunden später am selben Ort mit 27 km/h. Wie viele Stunden nach Alex' Start hat Alex Kim eingeholt?",
    4, "18 * 2 / (27 - 18)", 4, "Beide haben bis zum Treffpunkt dieselbe Strecke zurückgelegt. Wie lange ist Kim unterwegs, wenn Alex x Stunden fährt?",
    "Alex fährt x Stunden, Kim x + 2 Stunden. Gleiche Strecke: 27x = 18(x + 2). Ausmultiplizieren: 27x = 18x + 36. Subtrahiere 18x: 9x = 36. Also x = 4 Stunden.",
    [B("18 * 2 / 18", "nur durch Kims Tempo geteilt"), B("18 * 2 / (27 + 18)", "die beiden Geschwindigkeiten addiert"), B("27 * 2 / (27 - 18)", "Kims Fahrzeit statt Alex' Fahrzeit angegeben")], einheit="h"), g="einkleidung", regel=WG)
neu(T, "sach", "anwenden", Z(
    "In Oslo tauscht Kim Euro in Kronen. Die Wechselstube behält zuerst 3 € Gebühr ein und tauscht den Rest zum Kurs 1 € = 11,2 Kronen. Kim erhält 616 Kronen. Wie viele Euro hat Kim insgesamt abgegeben?",
    58, "616 / 11.2 + 3", "(616 + 3 * 11.2) / 11.2", "Wie viele Euro wurden getauscht? Dazu kommt noch etwas.",
    "Gleichung: (x − 3) · 11,2 = 616. Teile durch 11,2: x − 3 = 55. Addiere 3: x = 58. Probe: (58 − 3) · 11,2 = 616.",
    [B("616 / 11.2", "die Gebühr vergessen"), B("616 / 11.2 - 3", "die Gebühr abgezogen statt addiert"), B("616 / 11.2 + 3 * 11.2", "die Gebühr in Kronen umgerechnet und addiert")], einheit="€"), g="einkleidung", regel=WG)
neu(T, "sach", "umkehren", Z(
    "Sam plant ein rechteckiges Beet. Die Länge soll 4 m größer sein als die Breite. Der Zaun um das Beet ist 36 m lang. Wie breit ist das Beet?",
    7, "(36 / 2 - 4) / 2", 7, "Wähle x für die Breite. Wie lang ist dann die Länge? Der Umfang ist zweimal Länge plus zweimal Breite.",
    "Breite x, Länge x + 4. Umfang: 2x + 2(x + 4) = 36, also 4x + 8 = 36. Subtrahiere 8: 4x = 28. Teile durch 4: x = 7 m. Probe: 7 + 11 = 18 und 2 · 18 = 36.",
    [B("36 / 4", "den Umfang durch 4 geteilt, ohne den Unterschied zu beachten"), B("(36 - 4) / 4", "nur einmal 4 abgezogen"), B("(36 / 2 - 4) / 2 + 4", "die Länge statt der Breite angegeben")], einheit="m"), g="rueckwaerts", regel=WG)
