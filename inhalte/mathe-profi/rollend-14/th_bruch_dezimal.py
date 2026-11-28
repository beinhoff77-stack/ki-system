T = "bruch.dezimal"
# ───────── stellenwerte ─────────
a1(T, "stellenwerte", Z(
    "Eine Dezimalzahl hat 4 Einer, 0 Zehntel, 7 Hundertstel und 5 Tausendstel. Wie viele Tausendstel sind das insgesamt?",
    4075, "4 * 1000 + 7 * 10 + 5", "4000 + 70 + 5", "Wie viele Tausendstel sind 1 Einer? Wie viele Tausendstel sind 1 Hundertstel?",
    "1 Einer sind 1 000 Tausendstel, also 4 Einer sind 4 000 Tausendstel. 1 Hundertstel sind 10 Tausendstel, also 7 Hundertstel sind 70. Dazu 5 Tausendstel: 4 000 + 70 + 5 = 4 075.",
    [B("4 * 100 + 7 * 10 + 5", "die Einer nur als 100 Tausendstel gezählt"), B("4 + 7 + 5", "die Ziffern einfach addiert"), B("4 * 1000 + 7 * 100 + 5", "die Hundertstel als 100 Tausendstel gezählt")]))
a2(T, "stellenwerte", Z(
    "Beim Weitsprung springt Sam 4,58 m. Kim springt 4,5 m. Um wie viele Zentimeter ist Sams Sprung weiter?",
    8, "4.58 * 100 - 4.5 * 100", "458 - 450", "Rechne beide Weiten in Zentimeter um. 1 m sind 100 cm.",
    "4,58 m = 458 cm und 4,5 m = 450 cm. Der Unterschied ist 458 − 450 = 8 cm.",
    [B("4.58 - 4.5", "den Unterschied in Metern als Zentimeter angegeben"), B("4.58 * 1000 - 4.5 * 1000", "in Millimeter statt in Zentimeter umgerechnet"), B("(4.58 - 4.5) * 10", "mit 10 statt mit 100 umgerechnet")], "cm"))
a3(T, "stellenwerte", Z(
    "Aus den Ziffern 2, 5 und 8 wird eine Dezimalzahl gebildet. Jede Ziffer wird genau einmal benutzt, das Komma steht nach der ersten Ziffer. Um wie viele Hundertstel ist die größte solche Zahl größer als die kleinste?",
    594, "(8.52 - 2.58) * 100", "852 - 258", "Welche Ziffer muss vorne stehen, damit die Zahl möglichst groß oder möglichst klein ist? Dann ordnest du die restlichen Ziffern.",
    "Größte Zahl: 8,52. Kleinste Zahl: 2,58. Unterschied: 8,52 − 2,58 = 5,94. Das sind 594 Hundertstel.",
    [B("8.52 - 2.58", "den Unterschied nicht in Hundertstel umgerechnet"), B("(8.52 - 2.85) * 100", "2,85 als kleinste Zahl genommen"), B("(8.52 - 2.58) * 1000", "als Tausendstel statt als Hundertstel angegeben")], "Hundertstel"), g="transfer")
# ───────── vergleichen_ordnen ─────────
a1(T, "vergleichen_ordnen", Z(
    "Vier Schnecken kriechen in einer Stunde 0,36 m, 0,6 m, 0,306 m und 0,63 m weit. Um wie viele Millimeter ist die schnellste Schnecke weiter gekommen als die langsamste?",
    324, "(0.63 - 0.306) * 1000", "630 - 306", "Welche Schnecke ist am weitesten gekommen, welche am wenigsten weit? Fülle mit Endnullen auf: 0,630 und 0,306.",
    "Am weitesten: 0,63 m = 630 mm. Am wenigsten: 0,306 m = 306 mm. Unterschied: 630 − 306 = 324 mm.",
    [B("(0.6 - 0.306) * 1000", "die zweitschnellste statt der schnellsten Schnecke genommen"), B("(0.63 - 0.306) * 100", "mit 100 statt mit 1 000 umgerechnet"), B("(0.63 - 0.36) * 1000", "die zweitlangsamste statt der langsamsten Schnecke genommen")], "mm"))
a2(T, "vergleichen_ordnen", Z(
    "Für wie viele Ziffern □ liegt die Zahl 3,4□ zwischen 3,42 und 3,48? Die Zahlen 3,42 und 3,48 selbst zählen nicht mit.",
    5, "8 - 2 - 1", "7 - 3 + 1", "Welche Ziffern □ machen 3,4□ größer als 3,42? Welche machen es kleiner als 3,48?",
    "Größer als 3,42 ist 3,4□ ab □ = 3. Kleiner als 3,48 ist es bis □ = 7. Möglich sind 3, 4, 5, 6 und 7: das sind 5 Ziffern.",
    [B("8 - 2 + 1", "beide Grenzen 2 und 8 mitgezählt"), B("7 - 2 + 1", "die Ziffer 2 der Grenze 3,42 mitgezählt"), B("10", "alle zehn Ziffern gezählt")]))
a3(T, "vergleichen_ordnen", Z(
    "Eine Zahl hat genau zwei Nachkommastellen und liegt zwischen 3,7 und 3,8. Die Quersumme aller ihrer Ziffern ist 18. Welche Zahl ist es?",
    3.78, "3.7 + (18 - 3 - 7) / 100", "3.78", "Die Zahl sieht so aus: 3,7 und eine letzte Ziffer. Welche Ziffer fehlt, damit die Quersumme 18 ist?",
    "Die Zahl hat die Form 3,7x. Die Quersumme ist 3 + 7 + x = 18, also x = 8. Die Zahl ist 3,78. Sie liegt zwischen 3,70 und 3,80.",
    [B("3.8 + 0.07", "die Ziffern 7 und 8 vertauscht"), B("3.7 + 0.1", "um ein Zehntel weitergezählt"), B("3.7 + 8 / 10", "die 8 als Zehntel zu 3,7 addiert")]), g="transfer")
# ───────── runden ─────────
a1(T, "runden", Z(
    "Ein Wasserzähler zeigt 0,3846 m³. Runde auf Hundertstel. Wie viele Kubikmeter sind das gerundet?",
    0.38, "round(0.3846 * 100) / 100", "0.38", "Die Rundungsstelle ist die zweite Stelle nach dem Komma. Schau auf die Ziffer direkt rechts davon.",
    "Hundertstel: 0,38. Die Ziffer rechts davon ist 4, also wird abgerundet. Ergebnis: 0,38 m³.",
    [B("round(0.3846 * 10) / 10", "auf Zehntel gerundet"), B("round(0.3846 * 1000) / 1000", "auf Tausendstel gerundet"), B("round(0.3846 * 100) / 10", "das Komma beim Runden falsch gesetzt")], "m³"))
a2(T, "runden", Z(
    "Alex tauscht 85 € in Schweizer Franken. Für 1 € bekommt man 0,9432 Franken. Wie viele Franken sind das, auf Rappen genau (zwei Nachkommastellen) gerundet?",
    80.17, "round(85 * 0.9432 * 100) / 100", "8017 / 100", "Rechne zuerst den genauen Betrag aus. Dann rundest du auf Hundertstel.",
    "85 · 0,9432 = 80,172. Auf Hundertstel gerundet: Die Ziffer rechts ist 2, also abrunden. Ergebnis: 80,17 Franken.",
    [B("round(85 * 0.9432 * 10) / 10", "auf Zehntel gerundet"), B("round(85 * 0.9432 * 100 + 0.5) / 100", "aufgerundet statt gerundet"), B("round(85 * 0.94 * 100) / 100", "den Kurs zuerst auf 0,94 gerundet")], "Franken"))
a3(T, "runden", Z(
    "Auf einem Display steht eine Zahl mit genau zwei Nachkommastellen, zum Beispiel 6,00. Sie wird auf eine ganze Zahl gerundet: Hat die Zehntelziffer den Wert 5 oder mehr, wird aufgerundet. Das Ergebnis ist 6. Wie viele verschiedene Anzeigen kann es gewesen sein?",
    100, "649 - 550 + 1", "99 + 1", "Welche ist die kleinste, welche die größte Zahl, die auf 6 gerundet wird? Zähle die Hundertstel von der kleinsten bis zur größten.",
    "Ab 5,50 (Zehntelziffer 5) wird auf 6 aufgerundet, bis 6,49 (Zehntelziffer 4) wird auf 6 abgerundet. Die Zahlen sind 5,50 bis 6,49, also 550 bis 649 Hundertstel. Das sind 649 − 550 + 1 = 100 Zahlen.",
    [B("649 - 551 + 1", "die Zahl 5,50 nicht mitgezählt"), B("599 - 550 + 1", "nur die Zahlen von 5,50 bis 5,99 gezählt"), B("650 - 550 + 1", "auch 6,50 mitgezählt, die schon auf 7 aufgerundet wird")]), g="rueckwaerts")
# ───────── bruch_zu_dezimal ─────────
a1(T, "bruch_zu_dezimal", Z(
    "Kim hat 9/25 des Schulwegs mit dem Rad geschafft. Schreibe den Anteil als Dezimalzahl.",
    0.36, "9 / 25", "36 / 100", "Erweitere 9/25 auf den Nenner 100. Mit welcher Zahl musst du 25 malnehmen?",
    "Erweitern mit 4: 9/25 = 36/100 = 0,36. Probe: 9 : 25 = 0,36.",
    [B("9 / 10", "den Zähler durch 10 geteilt"), B("9 * 4 / 10", "das Komma falsch gesetzt"), B("9 / 40", "mit dem Nenner 40 statt 25 gerechnet")]))
a2(T, "bruch_zu_dezimal", Z(
    "Ein Stab ist 7/20 m lang. Wie viele Zentimeter sind das?",
    35, "7 / 20 * 100", "35", "Erweitere 7/20 auf den Nenner 100. Dann siehst du die Hundertstel.",
    "7/20 = 35/100 = 0,35 m. Das sind 0,35 · 100 = 35 cm.",
    [B("7 / 20", "den Bruch in Metern als Zentimeter angegeben"), B("7 / 20 * 10", "mit 10 statt mit 100 umgerechnet"), B("7 * 20", "Zähler und Nenner malgenommen")], "cm"))
a3(T, "bruch_zu_dezimal", Z(
    "Eine Dezimalzahl d hat denselben Wert wie 13/20. Wie groß ist d + 1/8 + 3/16? Gib das Ergebnis als Dezimalzahl an.",
    0.9625, "13 / 20 + 1 / 8 + 3 / 16", "0.65 + 0.125 + 0.1875", "Schreibe jeden Bruch als Dezimalzahl. Erweitere 1/8 auf Tausendstel und 3/16 auf Zehntausendstel.",
    "13/20 = 65/100 = 0,65. 1/8 = 125/1000 = 0,125. 3/16 = 1875/10000 = 0,1875. Summe: 0,65 + 0,125 + 0,1875 = 0,9625.",
    [B("0.65 + 0.125 + 0.3", "drei Sechzehntel als 0,3 geschrieben"), B("0.65 + 0.8 + 0.1875", "ein Achtel als 0,8 geschrieben"), B("0.65 + 0.125", "den dritten Bruch vergessen")]), g="verknuepfen")
# ───────── dezimal_zu_bruch ─────────
a1(T, "dezimal_zu_bruch", Z(
    "Eine Schnur ist 0,35 m lang. Schreibe 0,35 als vollständig gekürzten Bruch. Welche Zahl steht im Zähler?",
    7, "35 / 5", "7", "0,35 sind 35/100. Kürze mit der größten Zahl, die in 35 und in 100 steckt.",
    "0,35 = 35/100. Der größte gemeinsame Teiler ist 5. Gekürzt: 7/20. Im Zähler steht 7.",
    [B("35", "den Zähler des ungekürzten Bruchs angegeben"), B("20", "den Nenner statt den Zähler angegeben"), B("35 / 7", "nur den Zähler 35 durch 7 geteilt")]))
a2(T, "dezimal_zu_bruch", Z(
    "Ein Rezept braucht 0,625 kg Mehl. Wie viele Achtel Kilogramm sind das?",
    5, "0.625 * 8", "625 / 125", "0,625 sind 625/1 000. Kürze mit 125. Welchen Nenner erhältst du?",
    "0,625 = 625/1000 = 5/8. Das sind 5 Achtel Kilogramm. Probe: 5 · 0,125 = 0,625.",
    [B("625 / 8", "625 durch 8 geteilt"), B("0.625 * 10", "mit 10 malgenommen"), B("0.625 * 1000", "mit 1 000 malgenommen")]))
a3(T, "dezimal_zu_bruch", Z(
    "Kim schreibt: „0,075 = 75/100 = 3/4.“ Kims Kürzung ist richtig, trotzdem stimmt das Ergebnis nicht. Welchen Nenner hat der richtige, vollständig gekürzte Bruch?",
    40, "1000 / 25", "40", "Wie viele Nachkommastellen hat 0,075? Danach richtet sich der Nenner, bevor du kürzt.",
    "Kims Kürzung 75/100 = 3/4 ist richtig. Falsch ist der Nenner 100: 0,075 hat 3 Nachkommastellen, also 75/1000. Kürzen mit 25 ergibt 3/40. Der Nenner ist 40.",
    [B("100 / 25", "den Nenner 4 aus Kims Ergebnis angegeben"), B("1000", "den Nenner des ungekürzten Bruchs angegeben"), B("1000 / 5", "nur mit 5 gekürzt"), B("100", "den Nenner 100 aus Kims erstem Schritt angegeben")]), g="fehler")
# ───────── merkwerte ─────────
a1(T, "merkwerte", Z(
    "Ein Messbecher ist mit 1/8 Liter gefüllt. Wie viele Milliliter sind das?",
    125, "1 / 8 * 1000", "1000 / 8", "Du weißt: 1/8 = 0,125. Ein Liter hat 1 000 ml.",
    "1/8 l = 0,125 l. Das sind 0,125 · 1 000 = 125 ml.",
    [B("1 / 8", "den Bruch als Milliliter angegeben"), B("1 / 8 * 100", "mit 100 statt mit 1 000 umgerechnet"), B("8 * 1000", "mit dem Nenner malgenommen")], "ml"))
a2(T, "merkwerte", Z(
    "Sam hat 3/5 eines Buches mit 250 Seiten gelesen. Wie viele Seiten fehlen noch?",
    100, "250 - 3 / 5 * 250", "2 / 5 * 250", "Du weißt: 1/5 = 0,2. Wie viele Seiten hat Sam gelesen? Dann ziehst du ab.",
    "3/5 = 0,6. Gelesen: 0,6 · 250 = 150 Seiten. Es fehlen 250 − 150 = 100 Seiten.",
    [B("3 / 5 * 250", "die gelesenen statt die fehlenden Seiten angegeben"), B("250 - 0.3 * 250", "drei Fünftel als 0,3 geschrieben"), B("250 - 250 / 5", "nur ein Fünftel abgezogen")]))
a3(T, "merkwerte", Z(
    "Wie viel Prozent sind 1/4 + 0,125 + 3/5 zusammen?",
    97.5, "(1 / 4 + 0.125 + 3 / 5) * 100", "25 + 12.5 + 60", "Schreibe jeden Summanden als Dezimalzahl: 1/4 = 0,25 und 3/5 = 0,6. Addiere. Dann rechnest du in Prozent um.",
    "0,25 + 0,125 + 0,6 = 0,975. In Prozent: 0,975 · 100 = 97,5 %.",
    [B("1 / 4 + 0.125 + 3 / 5", "nicht in Prozent umgerechnet"), B("(1 / 4 + 0.125 + 0.3) * 100", "drei Fünftel als 0,3 geschrieben"), B("(1 / 4 + 0.125 + 3 / 5) * 10", "mit 10 statt mit 100 umgerechnet")], "%"), g="verknuepfen")
# ───────── periodisch ─────────
a1(T, "periodisch", Z(
    "Sam teilt ein 10 m langes Band in 3 gleich lange Stücke. Wie lang ist ein Stück, gerundet auf Zentimeter? Gib die Länge in Metern an.",
    3.33, "round(10 / 3 * 100) / 100", "333 / 100", "Rechne 10 : 3. Die Ziffer 3 wiederholt sich immer wieder. Runde auf Hundertstel.",
    "10 : 3 = 3,3333… Die Ziffer 3 wiederholt sich. Auf Hundertstel gerundet: 3,33 m.",
    [B("round(10 / 3 * 100)", "die Länge in Zentimetern statt in Metern angegeben"), B("round(10 / 3 * 10) / 10", "auf Zehntel gerundet"), B("round(10 / 3)", "auf ganze Meter gerundet")], "m"))
a2(T, "periodisch", Z(
    "Es gilt 4/11 = 0,363636… Die Ziffernfolge 36 wiederholt sich immer weiter. Wie groß ist die Summe aller Ziffern von der 1. bis zur 37. Stelle nach dem Komma?",
    165, "18 * (3 + 6) + 3", "162 + 3", "Wie groß ist die Ziffernsumme einer Wiederholung? Wie viele ganze Wiederholungen passen in 37 Stellen, und welche Ziffer bleibt übrig?",
    "Eine Wiederholung „36“ hat 2 Ziffern und die Ziffernsumme 3 + 6 = 9. In 37 Stellen passen 18 ganze Wiederholungen (36 Stellen): 18 · 9 = 162. Die 37. Stelle ist die erste Ziffer einer neuen Wiederholung, also 3. Summe: 162 + 3 = 165.",
    [B("18 * 9", "die 37. Stelle vergessen"), B("18 * 9 + 6", "die 37. Stelle als 6 statt als 3 gezählt"), B("37 * 9", "jede der 37 Stellen mit der Ziffernsumme 9 gerechnet")]))
a3(T, "periodisch", Z(
    "Es gilt 3/11 = 0,272727… Die Ziffernfolge 27 wiederholt sich immer weiter. Wie oft steht die Ziffer 7 unter den ersten 25 Nachkommastellen?",
    12, "25 // 2", "12", "An welchen Stellen steht die 7? Wie viele gerade Zahlen gibt es bis 25?",
    "Die Ziffern wechseln: 2, 7, 2, 7, … Die 7 steht an jeder zweiten Stelle, nämlich an den Stellen 2, 4, 6, …, 24. Das sind 12 Stellen. Die 25. Stelle ist eine 2.",
    [B("25 // 2 + 1", "die Ziffer 2 gezählt, die an 13 Stellen steht"), B("25", "alle 25 Stellen gezählt"), B("25 // 2 * 2", "bei jeder der 12 Wiederholungen beide Ziffern gezählt")]), g="transfer")
# ───────── verstehen ─────────
a1(T, "verstehen", Z(
    "Sam schätzt 4,98 · 2,02, indem er beide Zahlen auf ganze Zahlen rundet. Er behauptet: „Der Überschlag ist größer als das genaue Ergebnis.“ Prüfe das nach: Um wie viele Zehntausendstel unterscheiden sich der Überschlag und das genaue Ergebnis?",
    596, "498 * 202 - 100000", "100596 - 100000", "Berechne den Überschlag 5 · 2. Rechne das genaue Ergebnis ohne Komma als 498 · 202. Wie viele Zehntausendstel liegen dazwischen?",
    "Überschlag: 5 · 2 = 10 = 100 000 Zehntausendstel. Genau: 4,98 · 2,02 = 10,0596 = 100 596 Zehntausendstel. Der Überschlag ist kleiner als das genaue Ergebnis, Sams Behauptung stimmt also nicht. Unterschied: 100 596 − 100 000 = 596 Zehntausendstel.",
    [B("498 * 202", "das genaue Ergebnis in Zehntausendsteln statt den Unterschied angegeben"), B("(498 * 202 - 100000) / 100", "den Unterschied in Hundertsteln statt in Zehntausendsteln angegeben"), B("600", "den Unterschied auf 0,06 gerundet und in Zehntausendstel umgerechnet")], "Zehntausendstel"))
a2(T, "verstehen", Z(
    "Auf einem Zahlenstrahl liegt der Punkt A bei 4,35 und der Punkt B bei 4,47. M ist der Mittelpunkt der Strecke AB. Wie viele Zahlen mit genau zwei Nachkommastellen liegen zwischen M und B? M und B zählen nicht mit.",
    5, "447 - 441 - 1", "46 - 42 + 1", "Wie weit liegen A und B auseinander? Wo liegt M? Zähle die Hundertstel zwischen M und B.",
    "A = 4,35 sind 435 Hundertstel, B = 4,47 sind 447 Hundertstel. Der Abstand ist 12 Hundertstel, die Hälfte 6: M liegt bei 441 Hundertsteln, also bei 4,41. Zwischen M und B liegen 4,42; 4,43; 4,44; 4,45; 4,46. Das sind 5 Zahlen.",
    [B("447 - 435 - 1", "alle Zahlen zwischen A und B gezählt"), B("447 - 441", "die Zahl B mitgezählt"), B("447 - 441 + 1", "M und B mitgezählt")]))
a3(T, "verstehen", Z(
    "Kim behauptet: „Je mehr Ziffern nach dem Komma, desto größer ist die Zahl.“ Kim vergleicht 0,7 und 0,689. Um wie viele Tausendstel ist die Zahl mit weniger Ziffern größer?",
    11, "(0.7 - 0.689) * 1000", "700 - 689", "Schreibe 0,7 als 0,700 und vergleiche mit 0,689 Stelle für Stelle.",
    "0,7 = 0,700 = 700 Tausendstel. 0,689 sind 689 Tausendstel. Unterschied: 700 − 689 = 11 Tausendstel. Kims Aussage ist falsch.",
    [B("(0.7 - 0.689) * 100", "als Hundertstel statt als Tausendstel angegeben"), B("(0.689 - 0.07) * 1000", "0,07 statt 0,7 verglichen"), B("0.7 * 1000", "nur den Wert von 0,7 in Tausendsteln angegeben")], "Tausendstel"), g="begruenden")
