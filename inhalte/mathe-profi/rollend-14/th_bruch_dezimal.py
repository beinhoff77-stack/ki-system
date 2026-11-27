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
    "Drei Päckchen wiegen 2,35 kg, 2,4 kg und 2,305 kg. Um wie viele Gramm ist das leichteste Päckchen leichter als das schwerste?",
    95, "(2.4 - 2.305) * 1000", "2400 - 2305", "Welches Päckchen ist am schwersten, welches am leichtesten? Fülle mit Endnullen auf: 2,400 und 2,305.",
    "Am schwersten: 2,4 kg = 2 400 g. Am leichtesten: 2,305 kg = 2 305 g. Unterschied: 2 400 − 2 305 = 95 g.",
    [B("(2.4 - 2.35) * 1000", "das mittlere statt das leichteste Päckchen genommen"), B("(2.4 - 2.305) * 100", "mit 100 statt mit 1 000 umgerechnet"), B("(2.35 - 2.305) * 1000", "das mittlere und das leichteste Päckchen verglichen")], "g"))
a2(T, "vergleichen_ordnen", Z(
    "Wie viele Dezimalzahlen mit genau zwei Nachkommastellen liegen zwischen 0,4 und 0,5? Die Zahlen 0,4 und 0,5 selbst zählen nicht mit.",
    9, "(0.5 - 0.4) * 100 - 1", "49 - 41 + 1", "Schreibe 0,4 als 0,40 und 0,5 als 0,50. Zähle die Hundertstel dazwischen.",
    "0,40 sind 40 Hundertstel, 0,50 sind 50 Hundertstel. Dazwischen liegen 41 bis 49, das sind 9 Zahlen.",
    [B("(0.5 - 0.4) * 100", "die Zahl 0,50 mitgezählt"), B("(0.5 - 0.4) * 100 + 1", "beide Grenzen mitgezählt"), B("(0.5 - 0.4) * 1000 - 1", "mit Tausendstel statt mit Hundertsteln gerechnet")]))
a3(T, "vergleichen_ordnen", Z(
    "Welche ist die kleinste Dezimalzahl mit genau zwei Nachkommastellen, die größer als 3,7 ist?",
    3.71, "3.7 + 0.01", "3.71", "Schreibe 3,7 mit zwei Nachkommastellen: 3,70. Welche Zahl mit zwei Nachkommastellen kommt direkt danach?",
    "3,7 = 3,70. Die nächste Zahl mit zwei Nachkommastellen ist 3,71. Sie ist größer als 3,70 und die kleinste solche Zahl.",
    [B("3.7 + 0.1", "um ein Zehntel weitergezählt"), B("3.7 + 0.001", "um ein Tausendstel weitergezählt"), B("3.7 - 0.01", "ein Hundertstel abgezogen statt addiert")]), g="transfer")
# ───────── runden ─────────
a1(T, "runden", Z(
    "Ein Wasserzähler zeigt 0,3846 m³. Runde auf Hundertstel. Wie viele Kubikmeter sind das gerundet?",
    0.38, "round(0.3846 * 100) / 100", "0.38", "Die Rundungsstelle ist die zweite Stelle nach dem Komma. Schau auf die Ziffer direkt rechts davon.",
    "Hundertstel: 0,38. Die Ziffer rechts davon ist 4, also wird abgerundet. Ergebnis: 0,38 m³.",
    [B("round(0.3846 * 10) / 10", "auf Zehntel gerundet"), B("round(0.3846 * 1000) / 1000", "auf Tausendstel gerundet"), B("round(0.3846 * 100) / 10", "das Komma beim Runden falsch gesetzt")], "m³"))
a2(T, "runden", Z(
    "Kim kauft 3 kg Äpfel. Ein Kilogramm kostet 1,748 €. Wie viel Euro kosten die Äpfel, gerundet auf ganze Cent?",
    5.24, "round(3 * 1.748 * 100) / 100", "524 / 100", "Rechne zuerst den genauen Preis aus. Dann rundest du auf Hundertstel.",
    "3 · 1,748 = 5,244. Auf Hundertstel gerundet: Die Ziffer rechts ist 4, also abrunden. Ergebnis: 5,24 €.",
    [B("3 * 1.748", "den Preis nicht gerundet"), B("round(3 * 1.75 * 100) / 100", "den Einzelpreis zuerst auf 1,75 gerundet"), B("round(3 * 1.748 * 10) / 10", "auf Zehntel gerundet")], "€"))
a3(T, "runden", Z(
    "Eine Dezimalzahl mit zwei Nachkommastellen wird auf Zehntel gerundet. Das Ergebnis ist 4,3. Welche ist die größte Zahl, für die das gilt?",
    4.34, "4.3 + 0.04", "4.34", "Bei der Ziffer 0 bis 4 an der Hundertstelstelle wird abgerundet. Welche Ziffer ist dort die größte?",
    "Bis 4,34 wird auf 4,3 abgerundet. Ab 4,35 wird auf 4,4 aufgerundet. Die größte Zahl ist 4,34.",
    [B("4.3 + 0.05", "die Zahl angegeben, die schon auf 4,4 aufgerundet wird"), B("4.3 - 0.05", "die kleinste statt die größte Zahl gesucht"), B("4.3 + 0.4", "ein Zehntel dazugezählt statt ein Hundertstel")]), g="rueckwaerts")
# ───────── bruch_zu_dezimal ─────────
a1(T, "bruch_zu_dezimal", Z(
    "Kim trinkt 3/8 Liter Saft. Schreibe die Menge als Dezimalzahl.",
    0.375, "3 / 8", "375 / 1000", "Erweitere 3/8 auf den Nenner 1 000. Mit welcher Zahl musst du 8 malnehmen?",
    "Erweitern mit 125: 3/8 = 375/1000 = 0,375. Probe: 3 : 8 = 0,375.",
    [B("3 / 10", "den Zähler durch 10 geteilt"), B("3 * 125 / 100", "das Komma falsch gesetzt"), B("3 / 80", "durch 80 statt durch 8 geteilt")], "l"))
a2(T, "bruch_zu_dezimal", Z(
    "Ein Stab ist 7/20 m lang. Wie viele Zentimeter sind das?",
    35, "7 / 20 * 100", "35", "Erweitere 7/20 auf den Nenner 100. Dann siehst du die Hundertstel.",
    "7/20 = 35/100 = 0,35 m. Das sind 0,35 · 100 = 35 cm.",
    [B("7 / 20", "den Bruch in Metern als Zentimeter angegeben"), B("20 / 7 * 100", "den Bruch umgedreht"), B("7 * 20", "Zähler und Nenner malgenommen")], "cm"))
a3(T, "bruch_zu_dezimal", Z(
    "Eine Dezimalzahl d hat denselben Wert wie 13/20. Wie groß ist d + 1/8?",
    0.775, "13 / 20 + 1 / 8", "0.65 + 0.125", "Schreibe beide Brüche als Dezimalzahlen. Erweitere 13/20 auf Hundertstel und 1/8 auf Tausendstel.",
    "13/20 = 65/100 = 0,65. 1/8 = 125/1000 = 0,125. Summe: 0,65 + 0,125 = 0,775.",
    [B("(13 + 1) / (20 + 8)", "Zähler und Nenner einzeln addiert"), B("0.65 + 0.8", "ein Achtel als 0,8 geschrieben"), B("0.65 + 0.18", "ein Achtel als 0,18 geschrieben")]), g="verknuepfen")
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
    "Kim schreibt: „0,075 = 75/100 = 3/4.“ Das ist falsch. Welchen Nenner hat der richtige, vollständig gekürzte Bruch?",
    40, "1000 / 25", "40", "Wie viele Nachkommastellen hat 0,075? Danach richtet sich der Nenner, bevor du kürzt.",
    "0,075 hat 3 Nachkommastellen, also 75/1000. Kürzen mit 25 ergibt 3/40. Der Nenner ist 40.",
    [B("100 / 25", "Kims falschen Nenner angegeben"), B("1000", "den Nenner des ungekürzten Bruchs angegeben"), B("1000 / 5", "nur mit 5 gekürzt")]), g="fehler")
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
    [B("3 / 5 * 250", "die gelesenen statt die fehlenden Seiten angegeben"), B("0.3 * 250", "drei Fünftel als 0,3 geschrieben"), B("5 / 3 * 250", "den Bruch umgedreht")]))
a3(T, "merkwerte", Z(
    "Wie viel Prozent sind 1/4 + 0,125 + 3/5 zusammen?",
    97.5, "(1 / 4 + 0.125 + 3 / 5) * 100", "25 + 12.5 + 60", "Schreibe jeden Summanden als Dezimalzahl: 1/4 = 0,25 und 3/5 = 0,6. Addiere. Dann rechnest du in Prozent um.",
    "0,25 + 0,125 + 0,6 = 0,975. In Prozent: 0,975 · 100 = 97,5 %.",
    [B("1 / 4 + 0.125 + 3 / 5", "nicht in Prozent umgerechnet"), B("(1 / 4 + 0.125 + 0.3) * 100", "drei Fünftel als 0,3 geschrieben"), B("(1 / 4 + 0.125 + 3 / 5) * 10", "mit 10 statt mit 100 umgerechnet")], "%"), g="verknuepfen")
# ───────── periodisch ─────────
a1(T, "periodisch", Z(
    "Sam teilt ein 10 m langes Band in 3 gleich lange Stücke. Wie lang ist ein Stück, gerundet auf Zentimeter?",
    3.33, "round(10 / 3 * 100) / 100", "333 / 100", "Rechne 10 : 3. Die Ziffer 3 wiederholt sich immer wieder. Runde auf Hundertstel.",
    "10 : 3 = 3,3333… Die Ziffer 3 wiederholt sich. Auf Hundertstel gerundet: 3,33 m.",
    [B("10 / 3", "die periodische Zahl nicht gerundet"), B("round(10 / 3 * 10) / 10", "auf Zehntel gerundet"), B("round(10 / 3)", "auf ganze Meter gerundet")], "m"))
a2(T, "periodisch", Z(
    "Es gilt 4/11 = 0,363636… Die Ziffern 3 und 6 wechseln sich immer ab. Welche Ziffer steht an der 20. Stelle nach dem Komma?",
    6, "6 - 3 * (20 % 2)", "6", "An ungeraden Stellen steht 3, an geraden Stellen 6. Ist 20 gerade oder ungerade?",
    "Die 1. Stelle ist 3, die 2. Stelle ist 6, und so weiter. Gerade Stellen haben die Ziffer 6. Die 20. Stelle ist gerade, also steht dort 6.",
    [B("3", "gerade und ungerade Stellen verwechselt"), B("3 + 6", "die beiden Ziffern addiert"), B("20 / 2", "die Zahl der Perioden angegeben")]))
a3(T, "periodisch", Z(
    "Es gilt 2/7 = 0,285714285714… Die Ziffernfolge 285714 wiederholt sich. Auf Tausendstel gerundet: Wie viele Tausendstel sind 2/7?",
    286, "round(2 / 7 * 1000)", "286", "Schau auf die vierte Ziffer nach dem Komma. Sie entscheidet, ob du auf- oder abrundest.",
    "0,2857… Die vierte Stelle ist 7, also wird aufgerundet. 0,286 sind 286 Tausendstel.",
    [B("285", "die Ziffern nur abgeschnitten"), B("round(2 / 7 * 100)", "auf Hundertstel gerundet"), B("2 / 7 * 1000", "nicht gerundet")], "Tausendstel"), g="transfer")
# ───────── verstehen ─────────
a1(T, "verstehen", Z(
    "Sam schätzt das Ergebnis von 4,98 · 2,02. Dazu rundet er auf ganze Zahlen. Welchen Wert erhält er beim Überschlag?",
    10, "5 * 2", "5 * 2", "Runde 4,98 und 2,02 auf ganze Zahlen. Dann multiplizierst du.",
    "4,98 ≈ 5 und 2,02 ≈ 2. Überschlag: 5 · 2 = 10. Das genaue Ergebnis (10,0596) liegt nahe dabei.",
    [B("5 + 2", "die gerundeten Zahlen addiert"), B("4.98 * 2.02", "genau gerechnet statt überschlagen"), B("5 * 0.2", "2,02 als 0,2 gerundet")]))
a2(T, "verstehen", Z(
    "Welche Dezimalzahl liegt genau in der Mitte zwischen 2,4 und 2,5?",
    2.45, "(2.4 + 2.5) / 2", "2.4 + 0.05", "Der Abstand zwischen 2,40 und 2,50 ist 0,10. Die Mitte liegt eine halbe Strecke von 2,40 entfernt.",
    "Der Abstand ist 0,1. Die Hälfte davon ist 0,05. Die Mitte ist 2,4 + 0,05 = 2,45.",
    [B("2.4 + 2.5", "die beiden Zahlen addiert"), B("2.5 - 2.4", "den Abstand statt der Mitte angegeben"), B("2.4 + 0.01", "nur ein Hundertstel weitergezählt")]))
a3(T, "verstehen", Z(
    "Kim behauptet: „Je mehr Ziffern nach dem Komma, desto größer ist die Zahl.“ Kim vergleicht 0,7 und 0,689. Um wie viele Tausendstel ist die Zahl mit weniger Ziffern größer?",
    11, "(0.7 - 0.689) * 1000", "700 - 689", "Schreibe 0,7 als 0,700 und vergleiche mit 0,689 Stelle für Stelle.",
    "0,7 = 0,700 = 700 Tausendstel. 0,689 sind 689 Tausendstel. Unterschied: 700 − 689 = 11 Tausendstel. Kims Aussage ist falsch.",
    [B("(0.7 - 0.689) * 100", "als Hundertstel statt als Tausendstel angegeben"), B("(0.689 - 0.07) * 1000", "0,07 statt 0,7 verglichen"), B("0.7 * 1000", "nur den Wert von 0,7 in Tausendsteln angegeben")], "Tausendstel"), g="begruenden")
