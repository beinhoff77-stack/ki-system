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
    "Alex misst Körpergrößen in Metern mit zwei Nachkommastellen. Wie viele verschiedene Werte liegen zwischen 1,20 m und 1,50 m? Die beiden Grenzen zählen nicht mit.",
    29, "(1.5 - 1.2) * 100 - 1", "149 - 121 + 1", "Schreibe 1,2 als 1,20 und 1,5 als 1,50. Zähle die Hundertstel dazwischen.",
    "1,20 sind 120 Hundertstel, 1,50 sind 150 Hundertstel. Dazwischen liegen 121 bis 149, das sind 29 Werte.",
    [B("(1.5 - 1.2) * 100", "die Grenze 1,50 mitgezählt"), B("(1.5 - 1.2) * 100 + 1", "beide Grenzen mitgezählt"), B("(1.5 - 1.2) * 1000 - 1", "mit Tausendsteln statt mit Hundertsteln gerechnet")]))
a3(T, "vergleichen_ordnen", Z(
    "Eine Zahl hat genau zwei Nachkommastellen und liegt zwischen 3,7 und 3,8. Die Quersumme aller ihrer Ziffern ist 18. Welche Zahl ist es?",
    3.78, "3.7 + (18 - 3 - 7) / 100", "3.78", "Die Zahl sieht so aus: 3,7 und eine letzte Ziffer. Welche Ziffer fehlt, damit die Quersumme 18 ist?",
    "Die Zahl hat die Form 3,7x. Die Quersumme ist 3 + 7 + x = 18, also x = 8. Die Zahl ist 3,78. Sie liegt zwischen 3,70 und 3,80.",
    [B("3.8 + 0.07", "die Ziffern 7 und 8 vertauscht"), B("3.7 + 0.1", "um ein Zehntel weitergezählt"), B("3.7 + 8 / 10", "die 8 als Zehntel angehängt")]), g="transfer")
# ───────── runden ─────────
a1(T, "runden", Z(
    "Ein Wasserzähler zeigt 0,3846 m³. Runde auf Hundertstel. Wie viele Kubikmeter sind das gerundet?",
    0.38, "round(0.3846 * 100) / 100", "0.38", "Die Rundungsstelle ist die zweite Stelle nach dem Komma. Schau auf die Ziffer direkt rechts davon.",
    "Hundertstel: 0,38. Die Ziffer rechts davon ist 4, also wird abgerundet. Ergebnis: 0,38 m³.",
    [B("round(0.3846 * 10) / 10", "auf Zehntel gerundet"), B("round(0.3846 * 1000) / 1000", "auf Tausendstel gerundet"), B("round(0.3846 * 100) / 10", "das Komma beim Runden falsch gesetzt")], "m³"))
a2(T, "runden", Z(
    "Kim tankt 34 Liter Benzin. Ein Liter kostet 1,748 €. Wie viel Euro kostet die Tankfüllung, gerundet auf ganze Cent?",
    59.43, "round(34 * 1.748 * 100) / 100", "5943 / 100", "Rechne zuerst den genauen Preis aus. Dann rundest du auf Hundertstel.",
    "34 · 1,748 = 59,432. Auf Hundertstel gerundet: Die Ziffer rechts ist 2, also abrunden. Ergebnis: 59,43 €.",
    [B("34 * 1.748", "den Preis nicht gerundet"), B("round(34 * 1.75 * 100) / 100", "den Literpreis zuerst auf 1,75 gerundet"), B("round(34 * 1.748 * 10) / 10", "auf Zehntel gerundet")], "€"))
a3(T, "runden", Z(
    "Eine Dezimalzahl mit genau zwei Nachkommastellen wird auf Zehntel gerundet. Das Ergebnis ist 5,8. Wie viele solche Zahlen gibt es?",
    10, "(5.84 - 5.75) * 100 + 1", "584 - 575 + 1", "Welche ist die kleinste, welche die größte Zahl, die auf 5,8 gerundet wird? Zähle die Hundertstel von der kleinsten bis zur größten.",
    "Ab 5,75 wird auf 5,8 aufgerundet, bis 5,84 wird auf 5,8 abgerundet. Die Zahlen sind 5,75 bis 5,84, also 575 bis 584 Hundertstel. Das sind 584 − 575 + 1 = 10 Zahlen.",
    [B("(5.84 - 5.76) * 100 + 1", "die Zahl 5,75 nicht mitgezählt"), B("(5.84 - 5.80) * 100 + 1", "nur die Zahlen von 5,80 bis 5,84 gezählt"), B("(5.85 - 5.75) * 100 + 1", "auch 5,85 mitgezählt, die schon auf 5,9 aufgerundet wird")]), g="rueckwaerts")
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
    [B("35", "den Zähler des ungekürzten Bruchs angegeben"), B("100 / 5", "den Nenner statt den Zähler angegeben"), B("35 / 7", "durch 7 statt durch 5 gekürzt")]))
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
    [B("3 / 5 * 250", "die gelesenen statt die fehlenden Seiten angegeben"), B("0.3 * 250", "drei Fünftel als 0,3 geschrieben"), B("250 - 250 / 5", "nur ein Fünftel abgezogen")]))
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
    "Es gilt 4/11 = 0,363636… Die Ziffernfolge wiederholt sich immer weiter. Welche Ziffer steht an der 37. Stelle nach dem Komma?",
    3, "(4 * 10 ** 37 // 11) % 10", "3", "Welche Ziffern wiederholen sich? Wie viele Ziffern hat eine Wiederholung? Wo liegt die 37. Stelle in einer Wiederholung?",
    "Die Ziffern 3 und 6 wiederholen sich, eine Wiederholung hat 2 Ziffern. Die 1. Stelle ist 3, die 2. Stelle ist 6, die 3. Stelle ist wieder 3, und so weiter. Ungerade Stellen haben die Ziffer 3. Die 37. Stelle ist ungerade, also steht dort 3.",
    [B("6", "gerade und ungerade Stellen verwechselt"), B("3 + 6", "die beiden Ziffern addiert"), B("37 // 2", "die Zahl der vollen Wiederholungen angegeben")]))
a3(T, "periodisch", Z(
    "Es gilt 2/7 = 0,285714285714… Die Ziffernfolge 285714 wiederholt sich immer weiter. Welche Ziffer steht an der 50. Stelle nach dem Komma?",
    8, "(2 * 10 ** 50 // 7) % 10", "8", "Eine Wiederholung hat 6 Ziffern. Teile 50 durch 6 mit Rest. Der Rest sagt dir, die wievielte Ziffer der Wiederholung gemeint ist.",
    "50 : 6 = 8 Rest 2. Nach 8 vollen Wiederholungen (48 Stellen) kommt die 2. Ziffer einer neuen Wiederholung. Die Folge 285714 hat an zweiter Stelle die 8. Die 50. Stelle ist also 8.",
    [B("2", "die erste Ziffer der Wiederholung genommen"), B("4", "die letzte Ziffer der Wiederholung genommen"), B("5", "die dritte Ziffer der Wiederholung genommen")]), g="transfer")
# ───────── verstehen ─────────
a1(T, "verstehen", Z(
    "Sam schätzt das Ergebnis von 4,98 · 2,02. Dazu rundet er auf ganze Zahlen. Welchen Wert erhält er beim Überschlag?",
    10, "5 * 2", "5 * 2", "Runde 4,98 und 2,02 auf ganze Zahlen. Dann multiplizierst du.",
    "4,98 ≈ 5 und 2,02 ≈ 2. Überschlag: 5 · 2 = 10. Das genaue Ergebnis (10,0596) liegt nahe dabei.",
    [B("5 + 2", "die gerundeten Zahlen addiert"), B("4.98 * 2.02", "genau gerechnet statt überschlagen"), B("5 * 0.2", "2,02 als 0,2 gerundet")]))
a2(T, "verstehen", Z(
    "Auf einem Zahlenstrahl liegt der Punkt A bei 4,35 und der Punkt B bei 4,41. Welche Zahl liegt genau in der Mitte zwischen A und B?",
    4.38, "(4.35 + 4.41) / 2", "4.35 + 0.03", "Wie weit liegen A und B auseinander? Die Mitte liegt eine halbe Strecke von A entfernt.",
    "Der Abstand ist 4,41 − 4,35 = 0,06. Die Hälfte davon ist 0,03. Die Mitte ist 4,35 + 0,03 = 4,38.",
    [B("4.35 + 4.41", "die beiden Zahlen addiert"), B("4.41 - 4.35", "den Abstand statt der Mitte angegeben"), B("4.35 + 0.01", "nur ein Hundertstel weitergezählt")]))
a3(T, "verstehen", Z(
    "Kim behauptet: „Je mehr Ziffern nach dem Komma, desto größer ist die Zahl.“ Kim vergleicht 0,7 und 0,689. Um wie viele Tausendstel ist die Zahl mit weniger Ziffern größer?",
    11, "(0.7 - 0.689) * 1000", "700 - 689", "Schreibe 0,7 als 0,700 und vergleiche mit 0,689 Stelle für Stelle.",
    "0,7 = 0,700 = 700 Tausendstel. 0,689 sind 689 Tausendstel. Unterschied: 700 − 689 = 11 Tausendstel. Kims Aussage ist falsch.",
    [B("(0.7 - 0.689) * 100", "als Hundertstel statt als Tausendstel angegeben"), B("(0.689 - 0.07) * 1000", "0,07 statt 0,7 verglichen"), B("0.7 * 1000", "nur den Wert von 0,7 in Tausendsteln angegeben")], "Tausendstel"), g="begruenden")
