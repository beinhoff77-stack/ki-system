T = "zahlen.reell"
HZ = "id.zahlen.hoch_zurueck"
TA = "rr.tauschen"
OHNE_BEW = "Beweis durch Widerspruch (gerade/ungerade, gekürzter Bruch): keine Regel des Katalogs trägt den Lösungsweg"
OHNE_WZ = "Wurzeln zusammenfassen und umschreiben (a√b): keine Regel des Katalogs trägt genau diesen Schritt"
# ───────── zahlarten ─────────
neu(T, "zahlarten", "verfahren_waehlen", W(
    "Welche dieser Zahlen ist irrational?",
    "√50", [("√0,81", "0,9 · 0,9 = 0,81, die Wurzel ist die Dezimalzahl 0,9"), ("∛64", "4 · 4 · 4 = 64, die dritte Wurzel ist die ganze Zahl 4"), ("√(49/9)", "7/3 · 7/3 = 49/9, die Wurzel ist ein Bruch")],
    "Eine Wurzel ist rational, wenn der Radikand das Quadrat (oder die dritte Potenz) einer rationalen Zahl ist. Prüfe jede Zahl.",
    "50 ist keine Quadratzahl (7² = 49 und 8² = 64), und die Wurzel aus einer natürlichen Zahl, die keine Quadratzahl ist, ist nicht als Bruch darstellbar. Also ist √50 irrational. Die anderen sind 0,9, 4 und 7/3, also rational.",
    lambda: 0.9 ** 2 == 0.81 and 4 ** 3 == 64 and F(7, 3) ** 2 == F(49, 9) and all(F(p, q) ** 2 != 50 for q in range(1, 40) for p in range(1, 400))), g="erkennen", regel=HZ,
    zweifel="Rationale und irrationale Zahlen unterscheiden: hoch_zurueck trägt das Zurückrechnen der Wurzel, die Zahlarten selbst hat keine eigene Regel")
liste = [("√16", True), ("√20", False), ("7/3", True), ("π", False), ("√2,25", True), ("∛27", True), ("√45", False)]
neu(T, "zahlarten", "anwenden", Z(
    "Kim sortiert sieben Zahlen: √16, √20, 7/3, π, √(2,25), ∛27 und √45. Wie viele davon sind rational?",
    4, "4", sum(b for _, b in liste), "Prüfe bei jeder Wurzel, ob der Radikand das Quadrat (oder die dritte Potenz) einer Bruchzahl ist. Brüche sind immer rational.",
    "√16 = 4, 7/3, √(2,25) = 1,5 und ∛27 = 3 sind rational. 20 und 45 sind keine Quadratzahlen (4² = 16 < 20 < 25 = 5² und 6² = 36 < 45 < 49 = 7²), und die Wurzel aus einer natürlichen Zahl, die keine Quadratzahl ist, ist irrational. Also sind √20 und √45 irrational, ebenso π. Es sind 4 rationale Zahlen.",
    [B("3", "den Bruch siebendrittel für irrational gehalten"), B("5", "√20 oder √45 für rational gehalten"), B("7", "alle sieben Zahlen für rational gehalten")]), g="mehrschritt", regel=HZ,
    zweifel="Zahlen sortieren: hoch_zurueck trägt das Prüfen der Wurzeln")
# ───────── eingrenzen ─────────
neu(T, "eingrenzen", "lueckenweg", L(
    "Du schachtelst √10 ein. Für positive Zahlen gilt ①² = 9 und ②² = 16, also liegt √10 zwischen ① und ②. Für die Zehntel gilt 31² = 961 < 1000 < ③² = 1024.",
    "① = □; ② = □; ③ = □", [3, 4, 32], ["3", "{1} + 1", "{1} * 10 + 2"], ["round(sqrt(9))", "round(sqrt(16))", "round(sqrt(1024))"],
    "Suche die Quadratzahlen links und rechts von 10. Bei den Zehnteln rechnest du mit 100-mal so großen Zahlen.",
    "3² = 9 < 10 < 16 = 4². Also liegt √10 zwischen 3 und 4. Bei Zehnteln gilt 31² = 961 und 32² = 1024, also liegt √10 zwischen 3,1 und 3,2.",
    {0: [(5, None, "10 durch 2 geteilt statt eine Quadratzahl gesucht", "10 / 2")], 1: [(10, None, "den Radikanden als obere Grenze genommen", "{1} * 3 + 1")], 2: [(31, None, "die untere Grenze der Zehntel statt der oberen genommen", "{1} * 10 + 1")]}, gleich_ok=False), regel=HZ,
    zweifel="Eingrenzen durch Quadrieren: hoch_zurueck trägt das Rückrechnen")
neu(T, "eingrenzen", "anwenden", Z(
    "Kim schachtelt √7 ein: 2,6² = 6,76 und 2,7² = 7,29. Jetzt prüft sie die neun Zahlen 2,61 bis 2,69 mit zwei Nachkommastellen. Wie viele davon sind kleiner als √7?",
    4, "4", sum(1 for k in range(261, 270) if k * k < 7 * 10 ** 4), "Quadriere die Zahlen, bis das Quadrat größer als 7 wird. Ab dann sind alle weiteren Zahlen zu groß.",
    "2,64² = 6,9696 < 7 und 2,65² = 7,0225 > 7. Kleiner als √7 sind also 2,61, 2,62, 2,63 und 2,64: das sind 4 Zahlen. Alle weiteren Zahlen (2,65 bis 2,69) haben ein Quadrat über 7.",
    [B("5", "2,65 mitgezählt, obwohl 2,65² größer als 7 ist"), B("3", "2,61 nicht mitgezählt"), B("9", "alle neun Zahlen gezählt")]), g="mehrschritt", regel=HZ,
    zweifel="Eingrenzen durch Quadrieren: hoch_zurueck trägt das Rückrechnen")
# ───────── heron ─────────
w_h, c_h = rd("(4.5 + 20 / 4.5) / 2", 2)
neu(T, "heron", "anwenden", Z(
    "Beim Heron-Verfahren für √20 startest du mit 4. Der erste Schritt gibt (4 + 20 : 4) : 2 = 4,5. Wie lautet der zweite Wert (4,5 + 20 : 4,5) : 2? Runde auf zwei Dezimalstellen.",
    w_h, c_h, "round((4.5 + 20 / 4.5) / 2, 2)", "Rechne erst 20 : 4,5, addiere dann 4,5 und teile die Summe durch 2.",
    "20 : 4,5 ≈ 4,444. Die Summe 4,5 + 4,444 ≈ 8,944. Halbiert: 4,472, gerundet 4,47. Das ist nahe an √20 ≈ 4,4721.",
    [B("4.5", "nur den ersten Schritt gerechnet"), B("(4.5 + 20) / 2", "20 statt des Quotienten von 20 und 4,5 zu 4,5 addiert und halbiert"), B("20 / 4.5", "nur den Quotienten genommen, ohne den Mittelwert")], einheit=None), g="mehrschritt", ohne="Heron-Verfahren (Mittelwert aus Näherung und Quotient): keine Regel des Katalogs trägt den Rechenschritt")
neu(T, "heron", "umkehren", Z(
    "Ein Rechteck hat die Seiten 8 cm und 4,5 cm, die Fläche ist 36 cm². Man ersetzt die Länge durch den Mittelwert beider Seiten, also 6,25 cm, und passt die Breite so an, dass die Fläche 36 cm² bleibt. Wie breit ist das neue Rechteck in Zentimetern?",
    5.76, "36 / 6.25", "36 / ((8 + 4.5) / 2)", "Die Fläche bleibt gleich: Länge mal Breite = 36. Teile 36 durch die neue Länge.",
    "Die neue Länge ist (8 + 4,5) : 2 = 6,25 cm. Aus 6,25 · b = 36 folgt b = 36 : 6,25 = 5,76 cm. Die Seiten 6,25 und 5,76 liegen näher an √36 = 6.",
    [B("36 / 8", "mit der alten Länge geteilt"), B("6.25 - 4.5", "von der neuen Länge 6,25 die alte Breite 4,5 abgezogen statt 36 durch 6,25 zu teilen"), B("36 * 6.25", "mit der neuen Länge malgenommen statt geteilt")], einheit="cm"), g="umkehr", ohne="Flächenerhaltung beim Rechteck (Länge mal Breite bleibt gleich): keine Regel des Katalogs trägt den Rechenschritt")
# ───────── wurzel_mal ─────────
neu(T, "wurzel_mal", "anwenden", Z(
    "Wie groß ist √18 · √50? Fasse die beiden Wurzeln zu einer zusammen.",
    30, "30", "round(sqrt(18 * 50))", "Beim Malnehmen darf man die Zahlen unter den Wurzeln malnehmen: √a · √b = √(a · b).",
    "√18 · √50 = √(18 · 50) = √900 = 30, denn 30 · 30 = 900.",
    [B("18 + 50", "die Zahlen unter den Wurzeln addiert"), B("18 * 50", "das Produkt nicht wieder unter die Wurzel genommen"), B("900 / 2", "die Wurzel aus 900 wie „geteilt durch 2“ gerechnet", "fb.hoch_zurueck.wurzel_halbiert")]), g="mehrschritt", regel=HZ)
neu(T, "wurzel_mal", "verfahren_waehlen", W(
    "Welche dieser Gleichungen stimmt?",
    "√100 : √4 = √25", [("√9 + √16 = √25", "3 + 4 = 7, aber √25 = 5: Plus unter der Wurzel gilt nicht"), ("√100 − √36 = √64", "10 − 6 = 4, aber √64 = 8: Minus unter der Wurzel gilt nicht")],
    "Rechne beide Seiten jeder Gleichung einzeln aus und vergleiche.",
    "√100 : √4 = 10 : 2 = 5 = √25. Beim Teilen und Malnehmen darf man unter einer Wurzel zusammenfassen, bei Plus und Minus nicht.",
    lambda: math.isclose(math.sqrt(100) / math.sqrt(4), math.sqrt(25)) and not math.isclose(math.sqrt(9) + math.sqrt(16), math.sqrt(25)) and not math.isclose(math.sqrt(100) - math.sqrt(36), math.sqrt(64))), g="pruefung", ohne="Rechengesetze für Wurzeln (Malnehmen und Teilen unter einer Wurzel zusammenfassen): keine Regel des Katalogs trägt genau diesen Schritt")
# ───────── teilweise ─────────
neu(T, "teilweise", "anwenden", Z(
    "Ein quadratisches Beet hat 98 m² Fläche. Seine Seite lässt sich als a · √2 Meter schreiben. Welche ganze Zahl ist a?",
    7, "7", "round(sqrt(98 / 2))", "Zerlege 98 in ein Produkt, bei dem ein Faktor eine Quadratzahl ist.",
    "√98 = √(49 · 2) = √49 · √2 = 7 · √2. Also ist a = 7.",
    [B("49", "die Quadratzahl 49 selbst statt ihre Wurzel genommen"), B("98 / 7", "98 durch 7 geteilt"), B("2", "den Faktor unter der Wurzel als a genommen")]), g="einkleidung", regel=HZ)
neu(T, "teilweise", "lueckenweg", L(
    "Du vereinfachst √245. Es gilt √245 = √(① · 5) = ② · √5. Damit ist 2 · √245 = ③ · √5.",
    "① = □; ② = □; ③ = □", [49, 7, 14], ["49", "7", "2 * {2}"], ["round(245 / 5)", "round(sqrt(49))", "2 * round(sqrt(245 / 5))"],
    "Suche eine Quadratzahl, die 245 teilt. Ziehe aus ihr die Wurzel und lasse den Rest unter der Wurzel.",
    "245 = 49 · 5 und √49 = 7, also √245 = 7 · √5. Das Doppelte ist 2 · 7 · √5 = 14 · √5.",
    {0: [(35, None, "245 durch 7 statt durch 5 geteilt", "245 / 7")], 1: [(49, None, "die Quadratzahl selbst statt ihre Wurzel genommen", "{1}")], 2: [(9, None, "2 zu 7 addiert statt malgenommen", "2 + {2}")]}), regel=HZ)
# ───────── zusammenfassen ─────────
neu(T, "zusammenfassen", "fehler_detektiv", FD(
    "Noa vereinfacht √8 + √2:",
    [("Es gilt √8 = √4 · √2 = 2√2.", True, True),
     ("Damit ist √8 + √2 = 2√2 + √2.", True, True),
     ("Gleiche Wurzeln fasst man zusammen, das ergibt 3√2.", True, True),
     ("Die 3 darf ich unter die Wurzel schreiben, ohne sie zu quadrieren: 3√2 = √6.", False, True)],
    "Was gilt für eine Zahl vor der Wurzel, wenn sie unter die Wurzel wandert?",
    "Eine Zahl vor der Wurzel muss unter der Wurzel quadriert werden: 3√2 = √(9 · 2) = √18. Der Fehler steckt in Zeile 4. Die Zeilen 1 bis 3 sind richtig."), g="fehler", ohne=OHNE_WZ)
# ───────── nenner_rational ─────────
neu(T, "nenner_rational", "anwenden", Z(
    "Der Term 44 : √11 soll ohne Wurzel im Nenner geschrieben werden, und zwar in der Form a · √11. Welche ganze Zahl ist a?",
    4, "44 / 11", "round(44 / sqrt(11) / sqrt(11))", "Erweitere den Bruch mit √11, damit der Nenner eine ganze Zahl wird.",
    "44 / √11 = (44 · √11) / (√11 · √11) = 44√11 / 11 = 4√11. Also ist a = 4.",
    [B("44", "nur den Zähler erweitert und den Nenner stehen lassen"), B("44 / 2", "durch 2 statt durch 11 geteilt"), B("44 * 11", "mit 11 malgenommen statt geteilt")]), g="mehrschritt", ohne="Nenner rational machen (Erweitern mit der Wurzel): keine Regel des Katalogs trägt genau diesen Schritt")
# ───────── irrational_beweis ─────────
neu(T, "irrational_beweis", "verfahren_waehlen", W(
    "Man beweist, dass √2 nicht als gekürzter Bruch p/q geschrieben werden kann. Aus p² = 2q² folgt, dass p gerade ist. Welcher nächste Gedanke führt zum Widerspruch?",
    "Mit p = 2k folgt q² = 2k², also ist auch q gerade. Dann ließe sich der Bruch p/q durch 2 kürzen.",
    [("Mit p = 2k folgt q = k, also ist p/q = 2.", "aus p = 2k folgt nicht q = k, und p/q wäre dann die Zahl 2, nicht √2"), ("Weil p gerade ist, muss q ungerade sein, das ist kein Widerspruch.", "bei gekürztem Bruch wäre q zwar ungerade, aus p = 2k folgt aber q² = 2k², also ist q gerade: genau das ist der Widerspruch")],
    "Setze p = 2k in die Gleichung p² = 2q² ein. Was folgt für q?",
    "Aus p = 2k folgt p² = 4k² = 2q², also q² = 2k². Dann ist q² gerade, also ist q gerade. Damit sind p und q beide gerade, der Bruch ist nicht gekürzt. Das widerspricht der Annahme.",
    lambda: all((2 * k) ** 2 == 2 * (2 * k * k) for k in range(1, 20))), g="begruenden", ohne=OHNE_BEW)
neu(T, "irrational_beweis", "fehler_detektiv", FD(
    "Sam beweist, dass √2 irrational ist. Er nimmt an, dass √2 = p/q ein gekürzter Bruch mit positiven ganzen Zahlen p und q ist:",
    [("Aus √2 = p/q folgt durch Quadrieren 2 = p²/q², also p² = 2q².", True, True),
     ("Weil p² gerade ist, ist auch p gerade, also p = 2k.", True, True),
     ("Dann ist p² = 2k², und mit p² = 2q² folgt k² = q².", False, True),
     ("Also ist k = q, und der Bruch p/q hat die Form 2k/k.", True, True)],
    "Wie lautet p² für p = 2k? Rechne (2k)² nach.",
    "Es gilt (2k)² = 4k², nicht 2k². Aus 4k² = 2q² folgt q² = 2k², also ist q gerade. Der Fehler steckt in Zeile 3. Zeile 4 rechnet mit dem falschen Ergebnis weiter."), g="fehler", ohne=OHNE_BEW)
