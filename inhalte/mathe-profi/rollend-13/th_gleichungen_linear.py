T = "gleichungen.linear"
# ───────── waage ─────────
neu(T, "waage", "anwenden", Z(
    "Eine Balkenwaage ist im Gleichgewicht. Links liegen 4 Äpfel gleicher Masse und Gewichtsstücke mit zusammen 150 g. Rechts liegen 2 dieser Äpfel und Gewichtsstücke mit zusammen 350 g. Wie viel Gramm wiegt ein Apfel?",
    100, "(350 - 150) / (4 - 2)", "(350 - 150) // 2", "Nimm auf beiden Seiten gleich viel weg, damit die Waage im Gleichgewicht bleibt. Entferne zuerst 2 Äpfel.",
    "Die Gleichung ist 4a + 150 = 2a + 350. Nimm links und rechts 2 Äpfel weg: 2a + 150 = 350. Nimm 150 g weg: 2a = 200. Ein Apfel wiegt a = 100 g. Probe: 400 + 150 = 550 und 200 + 350 = 550.",
    [(250, "fb.waage.zeichen_nicht_gedreht", "die Gewichtsstücke addiert statt abgezogen: (350 + 150) : 2", "(350 + 150) / 2"), (200, "fb.waage.nur_ein_summand", "nur die Gewichtsstücke abgezogen und nicht durch 2 geteilt", "350 - 150"), (50, None, "durch 4 statt durch 2 geteilt", "(350 - 150) / 4")], "g"), g="einkleidung", regel="rr.waage")
assert loes("4*x+150 = 2*x+350") == 100
neu(T, "waage", "fehler_detektiv", FD(
    "Kim löst die Gleichung 5x − 12 = 2x + 9.",
    [("Auf beiden Seiten 2x abziehen und 12 addieren: 3x = 9 + 12.", gleichwertig("5*x-12 = 2*x+9", "3*x = 9+12"), True),
     ("Zusammengefasst: 3x = 21.", gleichwertig("3*x = 9+12", "3*x = 21"), True),
     ("Beide Seiten mal 3: x = 63", gleichwertig("3*x = 21", "x = 63"), gleichwertig("3*x = 21", "x = 63"))],
    "Wie wird aus 3x das einzelne x? Probe mit einer kleinen Zahl.",
    "3x bedeutet 3 mal x. Die Umkehrung ist das Teilen durch 3: x = 21 : 3 = 7. Probe: 5 · 7 − 12 = 23 und 2 · 7 + 9 = 23."), regel="rr.waage")
# ───────── beide_seiten ─────────
neu(T, "beide_seiten", "bruecke", Z(
    "Die Zeichnung zeigt die Geraden zu y = 3x − 2 und y = x + 4. Bei welcher Zahl x haben beide Terme denselben Wert? Das ist die Lösung der Gleichung 3x − 2 = x + 4.",
    3, "(4 + 2) / (3 - 1)", "(4 - (-2)) // 2", "Wo schneiden sich die beiden Geraden? Lies die x-Koordinate des Schnittpunkts ab und rechne zur Probe nach.",
    "Die Geraden schneiden sich bei x = 3. Rechnung: 3x − x = 4 + 2, also 2x = 6 und x = 3. Probe: 3 · 3 − 2 = 7 und 3 + 4 = 7.",
    [(7, None, "den y-Wert des Schnittpunkts statt des x-Werts angegeben", "3 * 3 - 2"), (1, None, "die −2 mit falschem Vorzeichen auf die andere Seite gebracht (4 minus 2 statt 4 plus 2)", "(4 - 2) / (3 - 1)"), (-3, None, "beide Zahlen mit dem falschen Vorzeichen auf die andere Seite gebracht", "(-2 - 4) / (3 - 1)")],
    grafik={"typ": "koordinaten", "x": [-1, 5], "y": [-3, 9], "graphen": [{"art": "linear", "m": 3, "t": -2, "name": "y = 3x − 2"}, {"art": "linear", "m": 1, "t": 4, "name": "y = x + 4"}]}), g="darstellung", regel="rr.waage")
neu(T, "beide_seiten", "umkehren", Z(
    "Für welche Zahl a hat die Gleichung 5x + a = 2x + 9 die Lösung x = 4?",
    -3, "2 * 4 + 9 - 5 * 4", "17 - 20", "Setze x = 4 in beide Seiten ein. Dann bleibt eine Gleichung nur mit a.",
    "Links: 5 · 4 + a = 20 + a. Rechts: 2 · 4 + 9 = 17. Aus 20 + a = 17 folgt a = −3. Probe: 5x − 3 = 2x + 9 hat die Lösung x = 4, denn 17 = 17.",
    [(3, None, "20 − 17 gerechnet statt 17 − 20", "20 - 17"), (37, None, "17 und 20 addiert", "17 + 20"), (-11, None, "rechts nur die 9 beachtet, das 2x vergessen: 20 + a = 9", "9 - 20")]), g="rueckwaerts", regel="rr.waage")
assert loes("5*x+(-3) = 2*x+9") == 4
# ───────── klammern ─────────
neu(T, "klammern", "anwenden", Z(
    "Im Kino kostet eine Kinderkarte x €. Eine Erwachsenenkarte kostet 2 € mehr, eine Premiumkarte 9 € mehr als eine Kinderkarte. Gruppe A kauft 3 Erwachsenenkarten und zahlt dazu 5 € für die Garderobe. Gruppe B kauft 2 Premiumkarten. Beide Gruppen zahlen gleich viel. Wie viel Euro kostet eine Kinderkarte?",
    7, "(2 * 9 - 3 * 2 - 5) / (3 - 2)", "7", "Eine Erwachsenenkarte kostet (x + 2) €, eine Premiumkarte (x + 9) €. Stelle für jede Gruppe den Gesamtpreis auf.",
    "Gruppe A: 3(x + 2) + 5. Gruppe B: 2(x + 9). Gleichung: 3(x + 2) + 5 = 2(x + 9). Ausmultiplizieren: 3x + 11 = 2x + 18. Dann x = 7. Probe: 3 · 9 + 5 = 32 und 2 · 16 = 32.",
    [(11, "fb.ausmultiplizieren.nur_erster_summand", "bei der ersten Klammer nur x mit 3 malgenommen: aus 3(x + 2) wird 3x + 2", "(18 - 7) / (3 - 2)"), (-2, "fb.ausmultiplizieren.nur_erster_summand", "bei der zweiten Klammer nur x mit 2 malgenommen: aus 2(x + 9) wird 2x + 9", "(9 - 11) / (3 - 2)"), (17, None, "die Garderobe abgezogen statt addiert: aus +5 wird −5", "(18 - 6 + 5) / (3 - 2)")], "€"), g="einkleidung", regel="rr.tauschen")
assert loes("3*(x+2)+5 = 2*(x+9)") == 7
neu(T, "klammern", "umkehren", Z(
    "Für welche Zahl a hat die Gleichung 4(x − a) = 2x + 6 die Lösung x = 5?",
    1, "5 - (2 * 5 + 6) / 4", "(5 * 4 - 16) / 4", "Setze x = 5 ein. Die rechte Seite lässt sich ausrechnen. Wie groß muss dann die Klammer links sein?",
    "Rechts: 2 · 5 + 6 = 16. Links: 4(5 − a) = 16, also 5 − a = 4 und a = 1. Probe: 4(5 − 1) = 16.",
    [(4, None, "16 : 4 = 4 als a angegeben, ohne 5 − a = 4 zu lösen", "16 / 4"), (-11, None, "den Faktor 4 vergessen: 5 − a = 16", "5 - 16"), (9, None, "die Klammer falsch gelesen: 5 + a = 9 statt 5 − a = 4", "5 + 16 / 4")]), g="rueckwaerts", regel="rr.tauschen")
assert loes("4*(x-1) = 2*x+6") == 5
# ───────── probe ─────────
neu(T, "probe", "zwei_wege", Z(
    "Kim hat die Gleichung 2(x + 5) − 3 = 4x − 7 gelöst und x = 9 erhalten. Weg A: Prüfe das mit einer Probe in der Gleichung, so wie sie dasteht. Weg B: Löse die Gleichung selbst. Welche Zahl ist die Lösung?",
    7, "(7 + 7) / (4 - 2)", "(10 - 3 + 7) / 2", "Setze bei Weg A die Zahl in beide Seiten der Ausgangsgleichung ein. Wenn die Seiten verschieden sind, muss neu gelöst werden.",
    "Weg A: Für x = 9 ist die linke Seite 2 · 14 − 3 = 25, die rechte 4 · 9 − 7 = 29. Die Seiten sind verschieden, also stimmt x = 9 nicht. Weg B: 2x + 10 − 3 = 4x − 7, also 2x + 7 = 4x − 7 und 14 = 2x. Es folgt x = 7. Probe: 2 · 12 − 3 = 21 und 28 − 7 = 21.",
    [(4.5, "fb.ausmultiplizieren.nur_erster_summand", "die 5 in der Klammer nicht mit 2 malgenommen: aus 2(x + 5) wird 2x + 5", "(7 + 2) / 2"), (10, None, "das −3 als +3 gerechnet", "(13 + 7) / 2"), (-7, "fb.waage.zeichen_nicht_gedreht", "beim Umstellen das Vorzeichen vergessen: 2x = −14 statt 2x = 14", "(-7 - 7) / 2")]), g="mehrschritt", regel="id.algebra.gleichung_loesen")
assert loes("2*(x+5)-3 = 4*x-7") == 7
neu(T, "probe", "fehler_detektiv", FD(
    "Kim löst 4(x − 2) = 3x + 1 und macht eine Probe.",
    [("Ausmultiplizieren: 4(x − 2) = 4x − 2, also 4x − 2 = 3x + 1.", gl("4*(x-2)", "4*x-2"), True),
     ("Beide Seiten minus 3x und plus 2: x = 3.", gleichwertig("4*x-2 = 3*x+1", "x = 3"), True),
     ("Probe in der ersten Gleichung: links 4 · 3 − 2 = 10, rechts 3 · 3 + 1 = 10. Also stimmt x = 3.", 4 * 3 - 2 == 10 and 3 * 3 + 1 == 10, True)],
    "Wie lautet die Ausgangsgleichung? Setze x = 3 genau dort ein.",
    "4(x − 2) = 4x − 8, nicht 4x − 2: Die 2 wird auch mit 4 malgenommen. Dann ist 4x − 8 = 3x + 1 und x = 9. Die Probe in Zeile 3 benutzt die schon fehlerhafte erste Gleichung. Eine Probe gehört in die Ausgangsgleichung: 4(3 − 2) = 4, aber 3 · 3 + 1 = 10."), regel="id.algebra.gleichung_loesen")
# ───────── sonderfaelle ─────────
neu(T, "sonderfaelle", "bruecke", W(
    "Die Zeichnung zeigt die Geraden zu y = 2x + 3 und y = 2x + 5. Gesucht sind alle Zahlen x (aus ℚ), für die 2x + 3 = 2x + 5 gilt. Was sagt die Zeichnung über diese Gleichung?",
    "Die Gleichung hat keine Lösung, denn die Geraden sind parallel und haben keinen gemeinsamen Punkt.",
    [("Die Gleichung hat genau eine Lösung, nämlich x = 0, denn dort schneiden die Geraden die y-Achse.", "die Achsenabschnitte 3 und 5 mit einer Lösung verwechselt: bei x = 0 sind die Werte 3 und 5, nicht gleich"),
     ("Jede Zahl ist Lösung, denn beide Geraden haben dieselbe Steigung.", "gleiche Steigung mit gleichen Werten verwechselt: die Geraden liegen 2 Einheiten auseinander")],
    "Wo hätten die Geraden einen gemeinsamen Punkt? Vergleiche die y-Werte bei x = 0 und bei x = 1.",
    "Beide Geraden haben die Steigung 2 und sind parallel. Sie liegen immer 2 Einheiten auseinander und haben keinen gemeinsamen Punkt. Rechnung: 2x + 3 = 2x + 5 führt auf 3 = 5, das ist falsch. Die Lösungsmenge ist leer.",
    lambda: loes("2*x+3 = 2*x+5") == "keine" and loes("2*x+3 = 2*x+3") == "alle",
    grafik={"typ": "koordinaten", "x": [-3, 3], "y": [-2, 12], "graphen": [{"art": "linear", "m": 2, "t": 3, "name": "y = 2x + 3"}, {"art": "linear", "m": 2, "t": 5, "name": "y = 2x + 5"}]}), g="darstellung", regel="id.algebra.gleichung_loesen")
neu(T, "sonderfaelle", "zwei_wege", Z(
    "Es gibt genau eine Zahl k, für die die Gleichung 3(x + 2) = 3x + k für alle Zahlen x wahr ist. Weg A: Klammer ausmultiplizieren und beide Seiten vergleichen. Weg B: eine passende Zahl für x einsetzen, zum Beispiel x = 0, und daraus k bestimmen. Wie groß ist k?",
    6, "3 * (0 + 2) - 3 * 0", "3 * 2", "Bei beiden Wegen musst du am Ende k = ... bestimmen. Welche Zahl steht links, wenn x = 0 ist?",
    "Weg A: 3(x + 2) = 3x + 6. Soll 3x + 6 = 3x + k für alle x gelten, muss k = 6 sein. Weg B: Für x = 0 steht links 3 · 2 = 6 und rechts k. Also k = 6. Probe: 3(x + 2) = 3x + 6 stimmt für jedes x.",
    [(2, "fb.ausmultiplizieren.nur_erster_summand", "die Klammer nicht ausmultipliziert: die 2 aus der Klammer als k genommen", "2"), (5, None, "3 + 2 gerechnet statt 3 · 2", "3 + 2"), (0, None, "x = 0 eingesetzt, aber links nur 3 · 0 gerechnet", "3 * 0")]), g="parameter", regel="id.algebra.gleichung_loesen")
assert loes("3*(x+2) = 3*x+6") == "alle"
# ───────── sach ─────────
neu(T, "sach", "zwei_wege", Z(
    "Zwei Rucksäcke wiegen zusammen 54 kg. Der schwerere ist 8 kg schwerer als der leichtere. Wie schwer ist der schwerere Rucksack? Weg A: Stelle eine Gleichung auf. Weg B: Nimm den Unterschied erst weg, teile den Rest gerecht auf und gib ihn dann wieder dazu. Wie viele Kilogramm wiegt der schwerere Rucksack?",
    31, "(54 + 8) / 2", "(54 - 8) / 2 + 8", "Beide Wege liefern dieselbe Masse. Bei Weg A ist die Masse des leichteren Rucksacks x kg.",
    "Weg A: x + (x + 8) = 54, also 2x = 46 und x = 23. Der schwerere Rucksack wiegt 23 + 8 = 31 kg. Weg B: 54 − 8 = 46, gerecht geteilt 23 kg, dann 8 kg dazu: 31 kg. Probe: 23 + 31 = 54.",
    [(23, None, "die Masse des leichteren Rucksacks angegeben", "(54 - 8) / 2"), (27, None, "nur die Hälfte der Gesamtmasse genommen, den Unterschied nicht beachtet", "54 / 2"), (35, None, "die Hälfte der Gesamtmasse um den ganzen Unterschied erhöht", "54 / 2 + 8")], "kg"), g="mehrschritt", regel="id.algebra.gleichung_loesen")
assert loes("x+(x+8) = 54") == 23
neu(T, "sach", "umkehren", Z(
    "Tom bestellt eine Jacke im Internet. Der Rabatt von 20 % gilt nur für die Jacke. Danach kommen 5 € Versandkosten dazu. Tom zahlt insgesamt 53 €. Wie viel Euro hat die Jacke ohne Rabatt gekostet?",
    60, "(53 - 5) / 0.8", "(53 - 5) * 5 / 4", "Gehe rückwärts: Was hat Tom für die Jacke allein bezahlt? Die Jacke kostet nach dem Rabatt 80 % des ursprünglichen Preises.",
    "Gleichung: 0,8x + 5 = 53. Dann 0,8x = 48 und x = 48 : 0,8 = 60. Die Jacke kostete 60 €. Probe: 20 % von 60 € sind 12 €, 60 − 12 = 48 und 48 + 5 = 53.",
    [(48, None, "nur die Versandkosten abgezogen, den Rabatt nicht rückgängig gemacht", "53 - 5"), (57.6, None, "20 % auf 48 € aufgeschlagen statt durch 0,8 geteilt", "(53 - 5) * 1.2"), (72.5, None, "die Versandkosten addiert statt abgezogen", "(53 + 5) / 0.8")], "€"), g="rueckwaerts", regel="id.algebra.gleichung_loesen")
