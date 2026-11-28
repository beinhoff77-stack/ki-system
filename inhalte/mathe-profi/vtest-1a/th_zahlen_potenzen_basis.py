T = "zahlen.potenzen_basis"
P = "rr.potenz"
# ═════════ schreibweise ═════════
neu(T, "schreibweise", "test", "begruenden", W(
    "Lena behauptet: „3² + 2³ = 5⁵.“ Welche Aussage über Lenas Behauptung ist richtig begründet?",
    "Falsch. 3² = 9 und 2³ = 8, zusammen 17. Basen und Hochzahlen darf man nicht einzeln addieren.",
    [("Richtig. Man addiert die Basen (3 + 2 = 5) und die Hochzahlen (2 + 3 = 5) einzeln.", "Basen und Hochzahlen einzeln addiert", 3 ** 2 + 2 ** 3 != 5 ** 5),
     ("Falsch. 3² = 3 · 2 = 6 und 2³ = 2 · 3 = 6, zusammen 12. Man rechnet Basis mal Hochzahl.", "Potenz als Basis mal Hochzahl gerechnet (3 · 2 und 2 · 3)", 3 * 2 + 2 * 3 == 12 and 3 ** 2 + 2 ** 3 != 12),
     ("Falsch. 3² = 3 + 3 = 6 und 2³ = 2 + 2 + 2 = 6, zusammen 12. Man addiert die Basis so oft.", "Die Basis so oft addiert, wie die Hochzahl sagt, statt zu multiplizieren", 3 + 3 + 2 + 2 + 2 == 12 and 3 ** 2 + 2 ** 3 != 12)],
    "3² = 3 · 3 = 9 und 2³ = 2 · 2 · 2 = 8. Zusammen sind das 17. Dagegen ist 5⁵ = 5 · 5 · 5 · 5 · 5 = 3 125. Die Hochzahl sagt, wie oft die Basis als Faktor dasteht; Basen und Hochzahlen dürfen nicht einzeln addiert werden.",
    3 ** 2 + 2 ** 3 == 17 and 5 ** 5 == 3125), regel=P, idee="begruenden_fehlvorstellung")
neu(T, "schreibweise", "korrektur", "darstellung", Z(
    "Aus der Potenz 3⁴ wird die Potenz 3⁵: Die Hochzahl wird um 1 größer, die Basis bleibt. Um wie viel ist 3⁵ größer als 3⁴?",
    162, "3 ** 5 - 3 ** 4", lambda: 3 * 3 * 3 * 3 * 3 - 3 * 3 * 3 * 3,
    "3⁴ = 3 · 3 · 3 · 3 = 81. Bei 3⁵ steht die 3 einmal öfter als Faktor da: 3⁵ = 81 · 3 = 243. Der Unterschied ist 243 − 81 = 162. Ein weiterer Faktor 3 verdreifacht den Wert, es kommt also zweimal der alte Wert dazu.",
    [(1, "Nur die Hochzahlen verglichen: 5 − 4", "5 - 4"), (81, "Nur den alten Wert 3⁴ genannt", "3 ** 4"), (243, "Nur den Wert von 3⁵ genannt", "3 ** 5")]), regel=P, idee="was_waere_wenn")
neu(T, "schreibweise", "korrektur", "darstellung", Z(
    "Du hast 2 Eltern. Jede Person hat wieder 2 Eltern. In der 1. Generation vor dir sind es 2 Personen (Eltern), in der 2. Generation 4 (Großeltern), in der 3. Generation 8 (Urgroßeltern). Wie viele Personen sind es in der 4. Generation (Ururgroßeltern)?",
    16, "2 ** 4", lambda: 8 * 2,
    "In jeder Generation verdoppelt sich die Zahl der Personen, weil jede Person 2 Eltern hat. In der 4. Generation steht der Faktor 2 genau 4-mal da: 2 · 2 · 2 · 2 = 2⁴ = 16.",
    [(64, "Die Nummer der Generation (4) als Basis und die 3 als Hochzahl genommen", "4 ** 3"), (8, "Die Zahl der Generation davor übernommen, nicht weiter verdoppelt", "2 ** 3"), (32, "Eine Generation zu weit gerechnet (5. Generation)", "2 ** 5")], einheit="Personen"), form="bruecke", regel=P, idee="situation_potenz")
neu(T, "schreibweise", "korrektur", "umkehr", Z(
    "In einer Potenz steht die Basis 6. Der Wert der Potenz ist 216. Wie oft steht die 6 als Faktor da?",
    3, "3", lambda: next(n for n in range(1, 10) if 6 ** n == 216),
    "Probiere: 6 · 6 = 36, 6 · 6 · 6 = 216. Die 6 steht 3-mal als Faktor da, also ist die Potenz 6³ und der Exponent 3.",
    [(36, "216 durch 6 geteilt", "216 // 6"), (6, "216 durch 36 geteilt", "216 // 36"), (210, "6 von 216 abgezogen", "216 - 6")]), form="umkehren", regel=P, idee="exponent_suchen")
neu(T, "schreibweise", "sicherung", "darstellung", W(
    "Welche Aussage über die Potenz 4⁶ stimmt?",
    "Die 4 steht 6-mal als Faktor da: 4 · 4 · 4 · 4 · 4 · 4 = 4 096.",
    [("Die 6 steht 4-mal als Faktor da: 6 · 6 · 6 · 6, nur andersherum.", "Basis und Hochzahl vertauscht (6⁴ = 1 296 statt 4⁶ = 4 096)", 6 ** 4 != 4 ** 6),
     ("4⁶ ist das Sechsfache von 4, also 4 · 6 = 24, weil die 6 oben steht.", "Hochzahl als Malnehmer gedeutet (4 · 6 = 24)", 4 * 6 != 4 ** 6),
     ("4⁶ ist 4 + 4 + 4 + 4 + 4 + 4 = 24, weil die 6 oben steht.", "Plus statt Mal (4 + 4 + 4 + 4 + 4 + 4 = 24)", 4 + 4 + 4 + 4 + 4 + 4 == 24 and 4 ** 6 != 24)],
    "In 4⁶ ist 4 die Basis (der Faktor) und 6 der Exponent (die Zahl der Faktoren). 4⁶ = 4 · 4 · 4 · 4 · 4 · 4 = 4 096. Mit 6⁴ = 1 296 oder mit 4 · 6 = 24 kommt etwas ganz anderes heraus.",
    4 ** 6 == 4 * 4 * 4 * 4 * 4 * 4 == 4096), form="bruecke", regel=P, idee="bedeutung_lesen")
neu(T, "schreibweise", "sicherung", "begruenden", W(
    "Man darf Basis und Hochzahl nicht vertauschen: 2³ = 8, aber 3² = 9. Trotzdem gilt 2⁴ = 4². Welche Begründung erklärt das richtig?",
    "Zufall bei diesen Zahlen: 2 · 2 · 2 · 2 = 16 und 4 · 4 = 16. Eine allgemeine Regel gibt es nicht.",
    [("Man darf vertauschen, wenn die Basis eine gerade Zahl ist, denn gerade Zahlen lassen sich teilen.", "Eine Regel erfunden (bei 2³ und 3² klappt es mit der geraden Basis 2 nicht)", 2 ** 3 != 3 ** 2),
     ("Weil 2 + 4 = 4 + 2 ist, darf man auch bei Potenzen vertauschen, denn Plus kann man tauschen.", "Das Tauschen beim Plus auf Potenzen übertragen", 2 ** 3 != 3 ** 2),
     ("Weil 2 · 4 = 4 · 2 ist, darf man auch bei Potenzen vertauschen, denn Mal kann man tauschen.", "Das Tauschen beim Mal auf Potenzen übertragen", 2 ** 3 != 3 ** 2)],
    "2⁴ = 2 · 2 · 2 · 2 = 16 und 4² = 4 · 4 = 16. Das ist ein Zufall dieser beiden Zahlen. Bei 2³ = 8 und 3² = 9 klappt das Vertauschen nicht. Vertauschen darf man bei Potenzen nicht.",
    2 ** 4 == 4 ** 2 and 2 ** 3 != 3 ** 2), regel=P, idee="gleiche_werte_begruenden")
neu(T, "schreibweise", "sicherung", "begruenden", W(
    "Tom rechnet: 2 · 3² = 6² = 36. Welche Aussage über Toms Rechnung stimmt?",
    "Fehler: Die Hochzahl 2 gehört nur zur 3, nicht zur 2. Richtig wäre 2 · 3 · 3 = 18.",
    [("Fehler: Er hätte die Hochzahl mit 2 malnehmen müssen. Richtig wäre 2 · 3 · 2 = 12.", "Die Hochzahl als Malnehmer gedeutet (3 · 2)", 2 * 3 * 2 == 12 and 12 != 18),
     ("Kein Fehler: Zuerst werden 2 und 3 zu 6 zusammengefasst, dann wird 6 quadriert.", "Falsche Reihenfolge bestätigt: das ergibt 36 statt 18", 6 ** 2 != 2 * 3 ** 2),
     ("Fehler: Er hätte addieren müssen. Richtig wäre 2 + 3² = 11.", "Mal mit Plus verwechselt", 2 + 3 ** 2 == 11 and 11 != 18)],
    "Die Hochzahl 2 gehört nur zur Basis 3: 3² = 3 · 3 = 9. Dann kommt das Malnehmen mit 2: 2 · 9 = 18. Tom hat 2 und 3 zuerst zu 6 zusammengefasst und dann 6 quadriert; das ist eine andere Rechnung.",
    2 * 3 ** 2 == 18 and 6 ** 2 == 36), regel=P, idee="fehler_richtigstellen")
neu(T, "quadrat", "test", "rueckwaerts", Z(
    "Ein quadratisches Feld hat 144 m² Fläche. Ein zweites quadratisches Feld hat einen doppelt so langen Umfang. Wie viele m² Fläche hat das zweite Feld?",
    576, "(12 * 4 * 2 // 4) ** 2", lambda: (lambda a: next(s for s in range(1, 500) if 4 * s == 8 * a) ** 2)(next(t for t in range(1, 200) if t * t == 144)),
    "Das erste Feld hat die Seitenlänge 12 m, denn 12 · 12 = 144. Sein Umfang ist 4 · 12 = 48 m. Der doppelte Umfang ist 96 m, also hat das zweite Feld die Seitenlänge 96 : 4 = 24 m. Seine Fläche ist 24 · 24 = 576 m².",
    [(288, "Die Fläche verdoppelt statt die Seitenlänge", "144 * 2"), (24, "Nur die Seitenlänge des zweiten Feldes genannt", "12 * 2"), (96, "Den doppelten Umfang statt der Fläche genannt", "12 * 4 * 2")], einheit="m²"), regel=P, idee="umfang_flaeche")
neu(T, "quadrat", "korrektur", "umkehr", Z(
    "Welche ist die kleinste Quadratzahl, die größer als 150 ist?",
    169, "13 * 13", lambda: next(n * n for n in range(1, 100) if n * n > 150),
    "Probiere: 12 · 12 = 144 ist noch kleiner als 150. 13 · 13 = 169 ist größer als 150. Dazwischen gibt es keine Quadratzahl, weil keine natürliche Zahl zwischen 12 und 13 liegt.",
    [(144, "Die größte Quadratzahl unter 150 genannt", "12 * 12"), (151, "Die nächste Zahl nach 150 genommen", "150 + 1"), (13, "Nur die Seitenlänge des Quadrats genannt", "13")]), regel=P, idee="nachbar_quadratzahlen")
neu(T, "quadrat", "korrektur", "mehrschritt", Z(
    "Bild A hat 7 Reihen mit je 7 Bildpunkten. Bild B hat 11 Reihen mit je 11 Bildpunkten. Ben meint: „Der Unterschied ist 4 · 4, weil 11 − 7 = 4 ist.“ Mia rechnet beide Anzahlen aus und zieht ab. Wie viele Bildpunkte hat Bild B wirklich mehr als Bild A?",
    72, "11 ** 2 - 7 ** 2", lambda: sum(1 for _ in range(11) for _ in range(11)) - sum(1 for _ in range(7) for _ in range(7)),
    "Bild A hat 7 · 7 = 49 Bildpunkte, Bild B hat 11 · 11 = 121 Bildpunkte. Der Unterschied ist 121 − 49 = 72. Ben irrt sich: Der Unterschied der Flächen ist nicht das Quadrat des Unterschieds der Seiten (4 · 4 = 16).",
    [(16, "Wie Ben nur den Unterschied der Seiten quadriert (4 · 4)", "4 * 4"), (4, "Nur den Unterschied der Seiten genannt: 11 − 7", "11 - 7"), (28, "Nur einen Streifen gerechnet: 4 · 7", "4 * 7")], einheit="Bildpunkte"), form="zwei_wege", regel=P, idee="differenz_quadrate")
neu(T, "quadrat", "korrektur", "darstellung", Z(
    "Ein Quadrat hat die Seitenlänge 5 cm + 4 cm. Wie viele cm² Flächeninhalt hat es?",
    81, "(5 + 4) * (5 + 4)", lambda: sum(9 for _ in range(9)),
    "Die Seitenlänge ist 5 cm + 4 cm = 9 cm. Die Fläche ist Seite mal Seite: 9 · 9 = 81 cm². Zwei kleine Quadrate mit den Seiten 5 cm und 4 cm haben zusammen nur 25 + 16 = 41 cm²; das ist weniger.",
    [(41, "Zwei kleine Quadrate (Seiten 5 und 4) addiert statt eines großen Quadrats", "5 * 5 + 4 * 4"), (18, "Den Umfang eines Rechtecks mit den Seiten 5 und 4 gerechnet", "5 + 4 + 5 + 4"), (20, "Nur ein Rechteck aus den beiden Längen berechnet", "5 * 4")], einheit="cm²"), form="bruecke", regel=P, idee="flaeche_aus_termen")
neu(T, "quadrat", "sicherung", "umkehr", Z(
    "Ein quadratischer Obstgarten wird um eine Reihe und eine Spalte erweitert und bleibt dabei quadratisch. Dadurch kommen genau 27 Bäume dazu. Wie viele Reihen hat der Garten nach der Erweiterung?",
    14, "(27 + 1) // 2", lambda: next(n for n in range(1, 100) if n * n - (n - 1) * (n - 1) == 27),
    "Probiere: 13 · 13 = 169 und 14 · 14 = 196. Der Unterschied ist 196 − 169 = 27. Der Garten hat nachher 14 Reihen. (Die neue Reihe hat 14 Bäume, die neue Spalte 13 weitere.)",
    [(13, "27 durch 2 geteilt (ganzzahlig)", "27 // 2"), (28, "1 zu 27 addiert", "27 + 1"), (54, "27 mit 2 malgenommen", "27 * 2")], einheit="Reihen"), form="umkehren", regel=P, idee="reihe_spalte")
neu(T, "quadrat", "sicherung", "begruenden", W(
    "Lisa rechnet: (3 · 4)² = 3² · 4² = 9 · 16 = 144. Welche Aussage über Lisas Rechnung stimmt?",
    "Kein Fehler: Bei einem Produkt darf man die Hochzahl verteilen. 12 · 12 = 144 und 9 · 16 = 144.",
    [("Fehler: Die Hochzahl darf man nie verteilen. Richtig wäre (3 · 4)² = 12 + 2 = 14, denn die 2 wird addiert.", "Die Hochzahl als Summand gedeutet", 12 + 2 == 14 and 14 != 144),
     ("Fehler: Sie hätte 3² + 4² rechnen müssen, denn ein Produkt wird zur Summe. Richtig wäre 9 + 16 = 25.", "Mal mit Plus verwechselt", 9 + 16 == 25 and 25 != 144),
     ("Fehler: Sie müsste 12 · 2 rechnen, denn die Hochzahl 2 heißt „mal 2“. Richtig wäre 24.", "Die Hochzahl als Malnehmer gedeutet", 12 * 2 == 24 and 24 != 144)],
    "Die Klammer zuerst: 3 · 4 = 12 und 12² = 12 · 12 = 144. Lisa rechnet 3² · 4² = 9 · 16 = 144. Das ist dasselbe: Bei einem Produkt darf man das Quadrat auf beide Faktoren verteilen. Bei einer Summe, zum Beispiel (3 + 4)², geht das nicht.",
    (3 * 4) ** 2 == 144 == 3 ** 2 * 4 ** 2), regel=P, idee="aussage_pruefen")
neu(T, "quadrat", "sicherung", "begruenden", W(
    "Eine quadratische Platte hat die Seitenlänge 5 cm. Eine zweite hat die doppelte Seitenlänge, also 10 cm. Wie verhalten sich die Flächen? Wähle die richtige Begründung.",
    "Die große Platte hat 4-mal so viel Fläche: 10 · 10 = 100 cm² und 5 · 5 = 25 cm², also 100 : 25 = 4.",
    [("Die große Platte hat doppelt so viel Fläche, denn die Seite ist doppelt so lang wie bei der kleinen.", "Doppelte Seite für doppelte Fläche gehalten", 10 * 10 != 2 * 5 * 5),
     ("Die große Platte hat 5 cm² mehr Fläche, denn die Seite wird um 5 cm länger als bei der kleinen.", "Zuwachs der Seite als Zuwachs der Fläche gedeutet", 10 * 10 - 5 * 5 != 5),
     ("Die große Platte hat 4-mal so viel Fläche, weil auch der Umfang 4-mal so groß ist wie vorher.", "Richtiges Ergebnis, falsche Begründung (der Umfang wird nur doppelt so groß: 20 cm und 40 cm)", 4 * 10 == 2 * 4 * 5 and 4 * 10 != 4 * 4 * 5)],
    "Fläche der kleinen Platte: 5 · 5 = 25 cm². Fläche der großen Platte: 10 · 10 = 100 cm². 100 : 25 = 4. Der Umfang wächst nur von 20 cm auf 40 cm, also auf das Doppelte. Die Fläche wächst auf das Vierfache.",
    10 * 10 == 4 * 5 * 5), regel=P, idee="was_waere_wenn")
# ═════════ zehner ═════════
neu(T, "zehner", "test", "parameter", Z(
    "Für welche Zahl □ gilt: 10⁶ − 9 · 10⁵ = □ · 10⁵?",
    1, "10 ** 6 // 10 ** 5 - 9", lambda: next(x for x in range(0, 100) if 1000000 - 9 * 100000 == x * 100000),
    "10⁶ = 10 · 10⁵, denn eine Zehnerpotenz mit 1 mehr in der Hochzahl ist das Zehnfache. Dann ist 10⁶ − 9 · 10⁵ = 10 · 10⁵ − 9 · 10⁵ = 1 · 10⁵. Probe: 1 000 000 − 900 000 = 100 000.",
    [(10, "Nur den ersten Term umgeformt und den abgezogenen Teil vergessen", "10"), (9, "Die 9 aus der Aufgabe als Lösung genommen", "9"), (5, "Die Hochzahl genannt", "5")]), regel=P, idee="groessenvergleich")
neu(T, "zehner", "korrektur", "darstellung", W(
    "Eine der vier Schreibweisen hat einen anderen Wert als 56 000 000. Welche?",
    "56 · 10⁵",
    [("56 · 10⁶", "Stimmt: 56 mal eine Million ist 56 000 000", 56 * 10 ** 6 == 56000000),
     ("560 · 10⁵", "Stimmt: 560 mal hunderttausend ist 56 000 000", 560 * 10 ** 5 == 56000000),
     ("5 600 · 10⁴", "Stimmt: 5 600 mal zehntausend ist 56 000 000", 5600 * 10 ** 4 == 56000000)],
    "56 · 10⁶ = 56 · 1 000 000 = 56 000 000. Auch 560 · 10⁵ und 5 600 · 10⁴ ergeben 56 000 000: Bekommt die Zahl vorn eine Null mehr, wird die Hochzahl um 1 kleiner. Dagegen ist 56 · 10⁵ = 5 600 000, das ist zehnmal zu klein.",
    56 * 10 ** 5 == 5600000 != 56000000), form="bruecke", regel=P, idee="schreibweise_erkennen")
neu(T, "zehner", "korrektur", "umkehr", Z(
    "Eine Sammlung von Münzen wiegt zusammen 500 kg. Jede Münze wiegt 5 g (1 kg = 1 000 g). Die Zahl der Münzen lässt sich als 10ⁿ schreiben. Wie groß ist n?",
    5, "5", lambda: next(n for n in range(0, 20) if 10 ** n * 5 == 500 * 1000),
    "500 kg sind 500 · 1 000 g = 500 000 g. Dann gibt es 500 000 : 5 = 100 000 Münzen. 100 000 = 10⁵, denn 100 000 ist eine 1 mit 5 Nullen. Also ist n = 5.",
    [(6, "Die Ziffern der Zahl (6) statt der Nullen gezählt (5 + 1)", "5 + 1"), (4, "Beim Teilen durch 5 eine Null verloren (5 − 1)", "5 - 1"), (2, "Die Umrechnung von kg in g (mal 1 000) vergessen; dann hat die Zahl der Münzen nur zwei Nullen, also 10²", "2")]), form="umkehren", regel=P, idee="umrechnen_potenz")
neu(T, "zehner", "korrektur", "darstellung", W(
    "Anna schreibt die Zahl 4 500 000 als 45 · 10⁵. Ben schreibt sie als 450 · 10⁵. Wer hat recht?",
    "Nur Anna: 45 · 100 000 = 4 500 000. Bei Ben ist der Faktor zehnmal so groß.",
    [("Beide: Die Hochzahl 5 bleibt, nur die Zahl davor hat eine Null mehr, das ist egal.", "Eine Null mehr beim Faktor für egal gehalten (450 · 10⁵ = 45 000 000)", 450 * 10 ** 5 != 4500000),
     ("Nur Ben: 450 · 10⁵ passt, weil 4 500 000 mit 45 beginnt und danach zwei Nullen kommen.", "Die Nullen falsch gezählt (450 · 10⁵ = 45 000 000)", 450 * 10 ** 5 == 45000000),
     ("Beide: Die Zahl vor der Zehnerpotenz darf man beliebig wählen, die Hochzahl bleibt gleich.", "Faktor und Hochzahl für unabhängig gehalten", 45 * 10 ** 5 != 450 * 10 ** 5)],
    "45 · 10⁵ = 45 · 100 000 = 4 500 000. Dagegen ist 450 · 10⁵ = 450 · 100 000 = 45 000 000, das ist zehnmal so viel. Damit Ben recht hätte, müsste er 450 · 10⁴ schreiben: Eine Null mehr beim Faktor heißt eine Hochzahl weniger.",
    45 * 10 ** 5 == 4500000 and 450 * 10 ** 5 == 45000000), regel=P, idee="darstellung_wechseln")
neu(T, "zehner", "sicherung", "umkehr", Z(
    "Ein Land hat 10⁶ Einwohner. Das sind 10²-mal so viele wie in der Stadt. Die Stadt hat 10-mal so viele Einwohner wie das Dorf. Wie viele Einwohner hat das Dorf?",
    1000, "10 ** 6 // 10 ** 2 // 10", lambda: 1000000 // 100 // 10,
    "Land: 10⁶ = 1 000 000. Stadt: 1 000 000 : 10² = 10 000. Dorf: 10 000 : 10 = 1 000. Mit Potenzen: Rückwärts werden die Hochzahlen abgezogen: 6 − 2 − 1 = 3, also 10³.",
    [(10000, "Nur durch 10² geteilt: das Dorf mit der Stadt verwechselt", "10 ** 6 // 10 ** 2"), (100000, "Nur durch 10 geteilt", "10 ** 6 // 10"), (100, "Durch 10³ statt 10² und dann durch 10 geteilt", "10 ** 6 // 10 ** 3 // 10")], einheit="Einwohner"), form="umkehren", regel=P, idee="kette_rueckwaerts")
neu(T, "zehner", "sicherung", "begruenden", W(
    "Tim rechnet: 10³ + 10³ = 10⁶. Welche Aussage über Tims Rechnung stimmt?",
    "Fehler: Er hat die Hochzahlen addiert (3 + 3 = 6). Richtig wäre 2 · 10³ = 2 000.",
    [("Kein Fehler: Beim Addieren von Zehnerpotenzen mit gleicher Basis addiert man die Hochzahlen.", "Falsche Regel bestätigt (1 000 + 1 000 ist nicht 1 000 000)", 10 ** 3 + 10 ** 3 != 10 ** 6),
     ("Fehler: Er hätte 10⁴ rechnen müssen. Richtig wäre 10³ + 10³ = 10⁴ = 10 000.", "Verdoppeln als eine Null mehr gedeutet", 10 ** 3 + 10 ** 3 != 10 ** 4),
     ("Fehler: Er hätte die Basen addieren müssen. Richtig wäre 20³ = 8 000, nicht 10⁶.", "Die Basen addiert und die Hochzahl behalten", 20 ** 3 != 10 ** 3 + 10 ** 3)],
    "10³ = 1 000. Also ist 10³ + 10³ = 1 000 + 1 000 = 2 000 = 2 · 10³. Beim Addieren bleibt die Hochzahl, es wird nur die Zahl davor größer. Die Hochzahlen werden nur beim Malnehmen von Potenzen mit gleicher Basis addiert: 10³ · 10³ = 10⁶.",
    10 ** 3 + 10 ** 3 == 2000 and 10 ** 3 * 10 ** 3 == 10 ** 6), regel=P, idee="fehler_richtigstellen")
neu(T, "zehner", "sicherung", "parameter", Z(
    "Für welche größte natürliche Zahl n ist 10ⁿ kleiner als 5 000 000?",
    6, "6", lambda: max(n for n in range(0, 30) if 10 ** n < 5000000),
    "10⁶ = 1 000 000 ist kleiner als 5 000 000. 10⁷ = 10 000 000 ist größer. Also ist n = 6 die größte passende Zahl.",
    [(7, "Die Ziffern von 5 000 000 gezählt (sieben Stück) statt der Nullen", "6 + 1"), (5, "Eine Hochzahl zu klein (6 − 1)", "6 - 1")]), form="umkehren", regel=P, idee="parameter_groesste_hochzahl")
neu(T, "sach", "test", "rueckwaerts", Z(
    "Eine Wasserpflanze verdreifacht jeden Tag ihre Blattzahl. Nach 4 Tagen hat sie 405 Blätter. Wie viele Blätter hatte sie am Anfang?",
    5, "405 // 3 ** 4", lambda: next(a for a in range(1, 405) if a * 3 * 3 * 3 * 3 == 405),
    "In 4 Tagen wurde 4-mal mit 3 malgenommen, also mit 3⁴ = 81. Rückwärts: 405 : 81 = 5. Probe: 5 → 15 → 45 → 135 → 405.",
    [(135, "Nur einmal durch 3 geteilt", "405 // 3"), (1215, "Weiter verdreifacht statt zurückgerechnet: 405 · 3", "405 * 3"), (401, "Die 4 Tage abgezogen: 405 − 4", "405 - 4")], einheit="Blätter"), form="umkehren", regel=P, idee="wachstum_rueckwaerts")
neu(T, "sach", "korrektur", "umkehr", Z(
    "Ein Papierstreifen wird mehrmals hintereinander in der Mitte gefaltet. Bei jeder Faltung liegen doppelt so viele Lagen übereinander wie vorher. Am Ende liegen 64 Lagen übereinander. Wie oft wurde gefaltet?",
    6, "6", lambda: next(n for n in range(0, 20) if 2 ** n == 64),
    "Am Anfang ist 1 Lage da. Nach jeder Faltung doppelt so viele: 2, 4, 8, 16, 32, 64. Das sind 6 Faltungen, denn 2⁶ = 64.",
    [(32, "64 durch 2 geteilt", "64 // 2"), (62, "2 von 64 abgezogen", "64 - 2"), (16, "64 durch 4 geteilt", "64 // 4")], einheit="Faltungen"), form="umkehren", regel=P, idee="exponent_suchen")
neu(T, "sach", "korrektur", "umkehr", Z(
    "Eine Münze wird 5-mal hintereinander geworfen. Bei jedem Wurf zeigt sie Kopf oder Zahl. Wie viele verschiedene Folgen von Ergebnissen kann es geben?",
    32, "2 ** 5", lambda: len([0 for a in range(2) for b in range(2) for c in range(2) for d in range(2) for e in range(2)]),
    "Beim ersten Wurf gibt es 2 Möglichkeiten, bei jedem weiteren Wurf verdoppelt sich die Zahl der Folgen. Nach 5 Würfen sind das 2 · 2 · 2 · 2 · 2 = 2⁵ = 32 verschiedene Folgen.",
    [(10, "Die Möglichkeiten je Wurf mal Zahl der Würfe: 5 · 2", "5 * 2"), (25, "Würfe mal Würfe gerechnet: 5 · 5", "5 ** 2"), (16, "Einen Wurf zu wenig gezählt: 2⁴", "2 ** 4")]), regel=P, idee="moeglichkeiten_zaehlen")
neu(T, "sach", "sicherung", "mehrschritt", Z(
    "Ein Netzwerk verdreifacht jeden Tag seine Mitgliederzahl. Es startet mit 5 Mitgliedern. Ein zweites Netzwerk verdreifacht sich ebenfalls jeden Tag, startet aber mit 10 Mitgliedern. Nach 4 Tagen hat das zweite Netzwerk wievielmal so viele Mitglieder wie das erste?",
    2, "(10 * 3 ** 4) // (5 * 3 ** 4)", lambda: (lambda a, b: b // a)(5 * 3 * 3 * 3 * 3, 10 * 3 * 3 * 3 * 3),
    "Nach 4 Tagen hat das erste Netzwerk 5 · 3⁴ = 405 Mitglieder, das zweite 10 · 3⁴ = 810. Beide werden mit demselben Faktor 3⁴ malgenommen, deshalb bleibt das Verhältnis wie am Anfang: 10 : 5 = 2.",
    [(16, "Die Hochzahl 4 zu 2⁴ gemacht", "2 ** 4"), (4, "Die Zahl der Tage als Verhältnis genommen", "4"), (81, "Nur den Wachstumsfaktor 3⁴ genannt", "3 ** 4")]), form="zwei_wege", regel=P, idee="was_waere_wenn")
neu(T, "sach", "sicherung", "verknuepfen", Z(
    "Kultur A hat am Anfang (Stunde 0) 100 Zellen und bekommt jede Stunde 100 Zellen dazu. Kultur B hat am Anfang 1 Zelle und verdoppelt sich jede Stunde. Nach wie vielen Stunden hat B zum ersten Mal mehr Zellen als A?",
    11, "11", lambda: next(n for n in range(0, 60) if 2 ** n > 100 + 100 * n),
    "Nach n Stunden hat A genau 100 + 100 · n Zellen, B hat 2ⁿ. Stunde 10: A hat 1 100, B hat 1 024: B ist noch kleiner. Stunde 11: A hat 1 200, B hat 2 048: B ist größer. Also nach 11 Stunden.",
    [(7, "B nur mit der Startzahl 100 von A verglichen: 2⁷ ist die erste Zweierpotenz über 100", "7"),
     (10, "B mit zehn Hundertern verglichen: 2¹⁰ ist die erste Zweierpotenz darüber (Startzahl von A vergessen)", "10")], einheit="Stunden"), form="zwei_wege", regel=P, idee="vergleich_wachstum")
neu(T, "sach", "sicherung", "begruenden", W(
    "Eine Algenart verdreifacht jeden Tag ihre Fläche. Am Anfang bedeckt sie 2 m². Nina rechnet die Fläche nach 4 Tagen so: 2 · 3 = 6, dann 6⁴ = 1 296 m². Welche Aussage über Ninas Rechnung stimmt?",
    "Fehler: Sie hat 2 · 3 = 6 als Basis genommen: 6⁴. Richtig wäre 2 · 3⁴ = 162 m².",
    [("Fehler: Sie hat 2 und 3 zu 6 zusammengefasst. Richtig wäre 2 · 3 · 4 = 24 m².", "Hochzahl als Malnehmer gedeutet (2 · 3 · 4 = 24)", 2 * 3 * 4 != 2 * 3 ** 4),
     ("Fehler: Die Anfangsfläche zählt nicht mit. Richtig wäre 3⁴ = 81 m², ohne den Faktor 2.", "Anfangsfläche weggelassen (3⁴ = 81)", 3 ** 4 != 2 * 3 ** 4),
     ("Kein Fehler: 6⁴ = 1 296 m² ist richtig, denn 2 · 3 = 6.", "Das Zusammenfassen von 2 und 3 für erlaubt gehalten (6⁴ = 1 296)", 6 ** 4 == 1296 and 6 ** 4 != 2 * 3 ** 4)],
    "Nach 4 Tagen wurde 4-mal mit 3 malgenommen: 2 · 3 · 3 · 3 · 3 = 2 · 81 = 162 m². Die 2 gehört nicht unter die Hochzahl: Nur die 3 wird 4-mal malgenommen. 6⁴ würde bedeuten, dass sich die Fläche 4-mal um den Faktor 6 vergrößert.",
    2 * 3 ** 4 == 162), regel=P, idee="fehler_richtigstellen")
neu(T, "sach", "korrektur", "darstellung", W(
    "Eine Zahl verdoppelt sich 5-mal hintereinander. Sie startet bei 3. Welche Rechnung gibt das Ergebnis an?",
    "3 · 2⁵",
    [("(3 · 2)⁵", "Die Startzahl mit in die Hochzahl-Klammer genommen (6⁵ = 7 776)", (3 * 2) ** 5 != 3 * 2 ** 5),
     ("3⁵ · 2", "Basis und Faktor vertauscht (3⁵ · 2 = 486)", 3 ** 5 * 2 != 3 * 2 ** 5),
     ("3 · 2 · 5", "Hochzahl als Malnehmer gedeutet (3 · 2 · 5 = 30)", 3 * 2 * 5 != 3 * 2 ** 5)],
    "Jede Verdopplung heißt: mal 2. Fünfmal verdoppeln heißt 5-mal mit 2 malnehmen: 3 · 2 · 2 · 2 · 2 · 2 = 3 · 2⁵ = 3 · 32 = 96. Die 3 steht nur einmal da, sie gehört nicht unter die Hochzahl.",
    3 * 2 * 2 * 2 * 2 * 2 == 3 * 2 ** 5 == 96), form="bruecke", regel=P, idee="situation_term")
