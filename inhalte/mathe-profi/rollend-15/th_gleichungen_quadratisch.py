T = "gleichungen.quadratisch"
GR = "rr.gegenrechnung"
NP = "rr.nullprodukt"
HG = "id.algebra.hoeherer_grad"
RF = "rr.reihenfolge"
WG = "rr.waage"
# ───────── reinquadratisch ─────────
neu(T, "reinquadratisch", "anwenden", Z(
    "Die Gleichung 4x² − 196 = 0 hat zwei Lösungen. Wie lautet die negative Lösung?",
    -7, "-7", -7, "Bringe zuerst das x² allein auf eine Seite. Welche Zahlen ergeben quadriert dieses Ergebnis?",
    "4x² = 196, also x² = 49. Zwei Zahlen haben das Quadrat 49: 7 und −7. Die negative Lösung ist −7. Probe: 4 · 49 − 196 = 0.",
    [B("7", "nur die positive Lösung genannt", "fb.gegenrechnung.zweite_loesung_fehlt"), B("-49", "das Quadrat als Lösung mit Minuszeichen genommen"), B("-196 / 2", "durch 2 statt durch 4 geteilt und das Minus mitgenommen")]), g="mehrschritt", regel=GR)
neu(T, "reinquadratisch", "lueckenweg", L(
    "Du löst 2x² − 98 = 0. Es folgt x² = ①. ② ist die positive und ③ die negative Lösung.",
    "① = □; ② = □; ③ = □", [49, 7, -7], ["98 / 2", "7", "-{2}"], ["round(98 / 2)", "round(sqrt(49))", "-round(sqrt(49))"],
    "Addiere erst 98 auf beiden Seiten, teile dann durch 2. Zu x² = Zahl gehören zwei Lösungen mit entgegengesetztem Vorzeichen.",
    "2x² = 98, also x² = 49. Die Lösungen sind 7 und −7, denn 7² = 49 und (−7)² = 49.",
    {0: [(96, None, "2 von 98 abgezogen statt durch 2 geteilt", "98 - 2")], 1: [(48, None, "von 49 eins abgezogen statt die Wurzel zu ziehen", "{1} - 1")], 2: [(14, None, "die beiden Lösungen addiert statt gespiegelt", "{2} * 2")]}), regel=GR)
# ───────── ausklammern ─────────
neu(T, "ausklammern", "verfahren_waehlen", W(
    "Welche Lösungsmenge hat die Gleichung 4x² − 28x = 0?",
    "x = 0 oder x = 7", [("nur x = 7", "durch x geteilt, dabei geht die Lösung 0 verloren"), ("x = 7 oder x = −7", "wie bei x² = Zahl gedacht"), ("x = 0 oder x = 28", "nach dem Ausklammern 28 statt 28 : 4 genommen")],
    "Klammere x aus. Ein Produkt ist null, wenn einer der Faktoren null ist.",
    "4x² − 28x = 4x · (x − 7) = 0. Ein Faktor muss null sein: 4x = 0 gibt x = 0, x − 7 = 0 gibt x = 7. Beide Zahlen erfüllen die Gleichung.",
    lambda: all(4 * x * x - 28 * x == 0 for x in (0, 7)) and 4 * 49 - 28 * (-7) != 0 and 4 * 28 * 28 - 28 * 28 != 0), g="mehrschritt", regel=HG)
neu(T, "ausklammern", "fehler_detektiv", FD(
    "Sam löst 6x² = 18x:",
    [("Ich bringe alles auf eine Seite: 6x² − 18x = 0.", True, True),
     ("Ich klammere 6x aus: 6x(x − 3) = 0.", True, True),
     ("Ein Produkt ist null, wenn ein Faktor null ist, also muss hier nur der Faktor x − 3 null sein.", False, True),
     ("Die Gleichung hat deshalb nur die Lösung x = 3.", True, True)],
    "Das Produkt 6x(x − 3) hat zwei Faktoren. Wann ist der erste Faktor null?",
    "Beim Nullprodukt kann jeder Faktor null sein: 6x = 0 gibt x = 0, und x − 3 = 0 gibt x = 3. Sam hat den Faktor 6x übersehen. Probe: Für x = 0 gilt 6 · 0 = 18 · 0. Die Lösungen sind x = 0 und x = 3. Der Fehler steckt in Zeile 3, Zeile 4 folgt daraus."), g="fehler", regel=HG)
# ───────── faktorisieren ─────────
neu(T, "faktorisieren", "umkehren", Z(
    "Eine Wasserrutsche folgt der Linie y = x² + px + q (Meter). Sie liegt bei den Stellen 4 und −9 auf Höhe null. Welchen Wert hat q?",
    -36, "4 * -9", -36, "Schreibe die Gleichung als Produkt (x − Lösung) · (x − Lösung) = 0 und multipliziere aus.",
    "Es gilt (x − 4)(x + 9) = x² + 5x − 36. Also ist p = 5 und q = −36. Probe: 4² + 5 · 4 − 36 = 0.",
    [B("36", "das Vorzeichen des Produkts übersehen"), B("4 - 9", "die Lösungen addiert statt malgenommen"), B("5", "den Beiwert p statt q angegeben")]), g="rueckwaerts", regel=NP,
    zweifel="Zurück von den Lösungen zur Gleichung: Nullprodukt trägt den Weg rückwärts")
neu(T, "faktorisieren", "anwenden", Z(
    "Löse x² − 4x − 21 = 0. Wie lautet die größere Lösung?",
    7, "7", 7, "Suche zwei Zahlen mit dem Produkt −21 und der Summe −4. Dann zerlege in zwei Klammern.",
    "x² − 4x − 21 = (x − 7)(x + 3) = 0. Ein Faktor muss null sein: x = 7 oder x = −3. Die größere Lösung ist 7.",
    [B("-3", "die kleinere Lösung genannt"), B("21", "das Absolutglied als Lösung genommen"), B("3", "aus x + 3 = 0 die Lösung 3 gemacht", "fb.nullprodukt.vorzeichen_der_loesung")]), g="mehrschritt", regel=NP)
# ───────── ergaenzung ─────────
neu(T, "ergaenzung", "anwenden", Z(
    "Mit der quadratischen Ergänzung wird x² + 10x + 9 = 0 zu (x + 5)² = b. Wie groß ist b?",
    16, "25 - 9", 16, "Ergänze die Hälfte von 10 zum Quadrat auf beiden Seiten, die 9 gehört danach auf die andere Seite.",
    "Die Hälfte von 10 ist 5, ihr Quadrat 25. x² + 10x + 25 = 25 − 9, also (x + 5)² = 16. Die Lösungen sind x = −1 und x = −9.",
    [B("25", "die 9 nicht verrechnet"), B("25 + 9", "die 9 addiert statt abgezogen"), B("9", "die Zahl 9 statt der Ergänzung als rechte Seite genommen")]), g="mehrschritt",
    ohne="Quadratische Ergänzung (binomische Formel rückwärts): keine Regel des Katalogs trägt genau diesen Schritt")
# ───────── loesungsformel ─────────
neu(T, "loesungsformel", "lueckenweg", L(
    "Für 3x² − 24x + 21 = 0 gilt a = 3, b = −24, c = 21. Die Diskriminante b² − 4ac ist ①. Ihre Wurzel ist ②. Die größere Lösung x = (24 + ②) : 6 ist ③.",
    "① = □; ② = □; ③ = □", [324, 18, 7], ["576 - 4 * 3 * 21", "18", "(24 + {2}) / 6"], ["24 ** 2 - 4 * 3 * 21", "round(sqrt(324))", "(24 + 18) / 6"],
    "Rechne b² zuerst (576), dann 4 · a · c, dann die Differenz. Beachte: Punkt vor Strich.",
    "b² = 576, 4ac = 4 · 3 · 21 = 252, also 576 − 252 = 324. √324 = 18. Die größere Lösung ist (24 + 18) : 6 = 7. Die andere ist (24 − 18) : 6 = 1.",
    {0: [(828, None, "−4ac mit Plus gerechnet", "576 + 4 * 3 * 21")], 1: [(162, None, "324 durch 2 geteilt statt die Wurzel gezogen", "{1} / 2")], 2: [(14, None, "nur durch a statt durch 2a geteilt", "(24 + {2}) / 3")]}), regel=RF)
neu(T, "loesungsformel", "anwenden", Z(
    "Löse 2x² + 3x − 20 = 0 mit der Lösungsformel. Wie lautet die negative Lösung?",
    -4, "(-3 - 13) / 4", -4, "Berechne zuerst die Diskriminante b² − 4ac. Beachte, dass c negativ ist.",
    "D = 3² − 4 · 2 · (−20) = 9 + 160 = 169, √169 = 13. x = (−3 ± 13) : 4. Die Lösungen sind 2,5 und −4. Die negative Lösung ist −4.",
    [B("(-3 - 13) / 2", "nur durch a statt durch 2a geteilt"), B("(3 - 13) / 4", "das Vorzeichen von b nicht gewechselt"), B("(-3 + 13) / 4", "die positive Lösung genannt")]), g="mehrschritt", regel=RF,
    zweifel="Lösungsformel: tragender Schritt ist die Diskriminante (Klammer, Hoch, Punkt vor Strich); es gibt keine eigene Formelregel im Katalog")
# ───────── bruchgleichung ─────────
neu(T, "bruchgleichung", "anwenden", Z(
    "Für x ≠ 0 gilt die Gleichung 40 : x = x − 6. Wie lautet die positive Lösung?",
    10, "10", 10, "Multipliziere beide Seiten mit x, damit der Bruch verschwindet. Bringe dann alles auf eine Seite.",
    "Mit x multiplizieren: 40 = x² − 6x, also x² − 6x − 40 = 0. Das ist (x − 10)(x + 4) = 0, also x = 10 oder x = −4. Die positive Lösung ist 10. Probe: 40 : 10 = 4 und 10 − 6 = 4.",
    [B("40 + 6", "nur eine Seite mit x multipliziert und 40 = x − 6 gelöst"), B("40 / 2", "40 halbiert"), B("6", "den Summanden 6 als Lösung genommen")]), g="mehrschritt", regel=WG,
    zweifel="Bruchgleichung: Waage (mit x malnehmen), danach Nullprodukt")
# ───────── diskriminante ─────────
neu(T, "diskriminante", "umkehren", Z(
    "Für welchen positiven Wert von k hat die Gleichung 3x² + kx + 27 = 0 genau eine Lösung?",
    18, "18", 18, "Genau eine Lösung gibt es, wenn die Diskriminante k² − 4 · 3 · 27 gleich null ist.",
    "D = k² − 4 · 3 · 27 = k² − 324. D = 0 gilt für k² = 324, also k = 18 (oder −18). Der positive Wert ist 18. Dann ist 3x² + 18x + 27 = 3(x + 3)² = 0 mit der einzigen Lösung −3.",
    [B("324", "k² = 324 nicht zurückgerechnet"), B("27 / 3", "c durch a geteilt"), B("27 * 2", "mit 2 statt mit 4a malgenommen")]), g="parameter", ohne="Diskriminante null (genau eine Lösung): keine Regel des Katalogs trägt genau diesen Schritt")
neu(T, "diskriminante", "verfahren_waehlen", W(
    "Wie viele gemeinsame Punkte hat die Parabel y = 2x² + 3x + 5 mit der x-Achse?",
    "keinen", [("zwei", "−4ac mit Plus gerechnet: 9 + 40 = 49 sieht nach zwei Schnittpunkten aus"), ("genau einen", "die Diskriminante ist nicht null")],
    "Setze y = 0. Berechne die Diskriminante b² − 4ac und vergleiche sie mit 0.",
    "2x² + 3x + 5 = 0 hat D = 3² − 4 · 2 · 5 = 9 − 40 = −31. Die Diskriminante ist negativ, also gibt es keinen Schnittpunkt.",
    lambda: 3 * 3 - 4 * 2 * 5 < 0), g="pruefung", regel=RF,
    zweifel="Diskriminante bestimmen und deuten: tragend ist die Rechenreihenfolge; die Deutung (Vorzeichen) hat keine eigene Regel")
# ───────── sachaufgabe ─────────
neu(T, "sachaufgabe", "anwenden", Z(
    "Ein Stein wird vom Rand einer Klippe in Kroatien nach oben geworfen. Seine Höhe über dem Meer ist h(t) = −5t² + 20t + 25 in Metern, t in Sekunden. Nach wie vielen Sekunden trifft er auf das Wasser (h = 0)?",
    5, "5", 5, "Setze h(t) = 0. Teile durch −5, damit vor t² die 1 steht. Prüfe, welche Lösung zur Frage passt.",
    "−5t² + 20t + 25 = 0 | : (−5) gibt t² − 4t − 5 = 0, also (t − 5)(t + 1) = 0. Es folgt t = 5 oder t = −1. Negative Zeit passt nicht, also nach 5 Sekunden.",
    [B("1", "die negative Lösung ohne Vorzeichen genommen"), B("20 / 5", "nur die beiden mittleren Zahlen dividiert"), B("25", "den Anfangswert 25 als Zeit genommen")], einheit="s"), g="einkleidung", regel=NP,
    zweifel="Sachaufgabe: Nullprodukt nach dem Umformen; Prüfen der Lösung gegen die Sachlage")
neu(T, "sachaufgabe", "anwenden", Z(
    "Ein rechteckiger Campingplatz am Gardasee ist 9 m länger als breit und 360 m² groß. Wie breit ist er?",
    15, "15", 15, "Nenne die Breite x. Wie groß ist dann die Länge? Stelle eine Gleichung für die Fläche auf.",
    "Länge x + 9, Fläche x(x + 9) = 360. Also x² + 9x − 360 = 0. Diskriminante: 81 + 1440 = 1521 = 39². x = (−9 + 39) : 2 = 15. Die andere Lösung −24 passt nicht. Probe: 15 · 24 = 360.",
    [B("360 / 9", "die Fläche durch den Unterschied geteilt"), B("15 + 9", "die Länge statt der Breite angegeben"), B("(9 + 39) / 4", "bei −b das Vorzeichen falsch gesetzt (9 statt −9) und durch 4 geteilt")], einheit="m"), g="mehrschritt", regel=RF,
    zweifel="Sachaufgabe: Lösungsformel (Diskriminante nach Rechenreihenfolge), Prüfen gegen die Sachlage")
