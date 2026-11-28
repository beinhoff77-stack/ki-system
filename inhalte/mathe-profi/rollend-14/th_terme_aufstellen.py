T = "terme.aufstellen"
# ───────── struktur ─────────
a1(T, "struktur", Z(
    "Kim schreibt vier Terme auf: A: 3 + x · 2, B: (3 + x) · 2, C: 3 · x + 2 · x, D: 12 : (x − 1). Alex bestimmt für jeden Term die zuletzt ausgeführte Rechenart und gibt eine Kennzahl: Summe = 1, Differenz = 2, Produkt = 3, Quotient = 4. Wie groß ist die Summe der vier Kennzahlen?",
    9, "1 + 3 + 1 + 4", "4 + 3 + 1 + 1", "Welche Rechenart wird bei jedem Term zuletzt ausgeführt? Beachte Punkt vor Strich und die Klammern.",
    "A: Erst x · 2, zuletzt wird 3 addiert: Summe (1). B: Erst die Klammer, zuletzt mal 2: Produkt (3). C: Erst 3 · x und 2 · x, zuletzt addiert: Summe (1). D: Erst die Klammer x − 1, zuletzt geteilt: Quotient (4). Zusammen 1 + 3 + 1 + 4 = 9.",
    [B("3 + 3 + 1 + 4", "Term A als Produkt gelesen, weil x · 2 zuerst gerechnet wird"), B("1 + 1 + 1 + 4", "Term B als Summe gelesen, weil in der Klammer zuerst 3 + x steht"), B("1 + 3 + 1 + 3", "Term D als Produkt gelesen, weil Teilen und Malnehmen beides Punktrechnungen sind")]))
a2(T, "struktur", Z(
    "Der Term 36 : (x − 3) + 2 · x wird für x = 9 berechnet. Er ist eine Summe aus zwei Summanden. Wie groß ist der größere Summand?",
    18, "2 * 9", "36 / 2", "Welche zwei Summanden hat der Term? Berechne beide für x = 9.",
    "Die Summe hat zwei Summanden: 36 : (x − 3) und 2 · x. Für x = 9 ist der erste 36 : 6 = 6 und der zweite 2 · 9 = 18. Der größere Summand ist 18.",
    [B("36 / (9 - 3)", "nur den kleineren Summanden angegeben"), B("36 / (9 - 3) + 2 * 9", "den Wert der ganzen Summe statt des größeren Summanden angegeben"), B("(36 / (9 - 3) + 2) * 9", "den Term als Produkt (… + 2) · x gelesen")]))
a3(T, "struktur", Z(
    "Kim bestimmt die Art von vier Termen. (1) 2 + 3 · x ist eine Summe. (2) (2 + 3) · x ist eine Summe. (3) 12 : x − 2 ist ein Quotient. (4) 5 · (x − 2) ist ein Produkt. Einige Aussagen sind falsch. Wie groß ist die Summe der Nummern der falschen Aussagen?",
    5, "2 + 3", "3 + 2", "Bestimme bei jedem Term die Rechenart, die zuletzt ausgeführt wird.",
    "(1) Erst 3 · x, zuletzt +: Summe, richtig. (2) Erst die Klammer 2 + 3, zuletzt mal x: ein Produkt, also falsch. (3) Erst 12 : x, zuletzt − 2: eine Differenz, also falsch. (4) Erst die Klammer, zuletzt mal 5: Produkt, richtig. Falsch sind (2) und (3): 2 + 3 = 5.",
    [B("2", "nur Aussage (2) als falsch erkannt"), B("3", "nur Aussage (3) als falsch erkannt"), B("3 + 4", "die Aussagen (3) und (4) für falsch gehalten")]), g="pruefung")
# ───────── termwert ─────────
a1(T, "termwert", Z(
    "Ein Handyvertrag kostet 5 € Grundgebühr im Monat und 0,05 € für jede Minute. Der Preis in Euro ist 5 + 0,05 · m, wobei m die Zahl der Minuten ist. Wie viel Euro kostet der Vertrag bei m = 120 Minuten?",
    11, "5 + 0.05 * 120", "5 + 6", "Setze m = 120 ein. Rechne Punktrechnung vor Strichrechnung.",
    "5 + 0,05 · 120 = 5 + 6 = 11. Der Vertrag kostet 11 €.",
    [B("(5 + 0.05) * 120", "(5 + 0,05) · 120 gerechnet: Grundgebühr und Minutenpreis zusammen mit den Minuten malgenommen"), B("5 + 0.05 + 120", "alle Zahlen addiert"), B("5 * 120 + 0.05", "nur die Grundgebühr mit 120 malgenommen und 0,05 dazugezählt")], "€"))
a2(T, "termwert", Z(
    "Vor zwei Wochen hatte Alex 50 € auf dem Konto. Seitdem werden jede Woche 4 € abgebucht. Das Guthaben in Euro wird t Wochen ab heute durch den Term 50 − 4 · (t + 2) angegeben. Wie viel Euro sind es nach t = 3 Wochen?",
    30, "50 - 4 * (3 + 2)", "50 - 20", "Die Klammer kommt zuerst. Dann die Multiplikation, zuletzt die Subtraktion.",
    "Klammer: 3 + 2 = 5. Dann 4 · 5 = 20. Dann 50 − 20 = 30. Alex hat 30 €.",
    [B("50 - 4 * 3 + 2", "die Klammer weggelassen"), B("(50 - 4) * (3 + 2)", "zuerst 4 vom Guthaben abgezogen und dann mit der Klammer malgenommen"), B("50 - 4 * 3 - 2", "statt der Klammer 50 − 4 · 3 − 2 gerechnet")], "€"))
a3(T, "termwert", Z(
    "Aus einem Tank laufen Liter ab. Nach t Minuten sind noch 120 − 3 · (2t + 5) Liter im Tank. Nach wie vielen Minuten sind noch genau 63 Liter im Tank?",
    7, "((120 - 63) / 3 - 5) / 2", "(19 - 5) / 2", "Setze den Term gleich 63. Arbeite von außen nach innen rückwärts: Was kommt zuletzt, was zuerst?",
    "Rückwärts rechnen: Von 120 Litern sind 120 − 63 = 57 Liter abgeflossen. Das sind 3 mal etwas: 57 : 3 = 19 ist der Wert der Klammer 2t + 5. Davon 5 abziehen: 19 − 5 = 14 ist 2t, also ist t = 14 : 2 = 7 Minuten. Probe: 2 · 7 + 5 = 19, 3 · 19 = 57, 120 − 57 = 63.",
    [B("(120 - 63) / 3 - 5", "durch 2 nicht geteilt"), B("(120 - 63) / 3 / 2", "die 5 nicht abgezogen"), B("(120 - 63) / 3", "nur durch 3 geteilt")], "Minuten"), g="rueckwaerts")
# ───────── uebersetzen ─────────
a1(T, "uebersetzen", Z(
    "Kim denkt sich die Zahl 8. Sie bildet die Summe aus dem Doppelten dieser Zahl und 7. Welches Ergebnis erhält Kim?",
    23, "2 * 8 + 7", "16 + 7", "Übersetze Wort für Wort: das Doppelte der Zahl heißt 2 mal die Zahl. Dazu kommt 7.",
    "Das Doppelte von 8 ist 2 · 8 = 16. Die Summe aus 16 und 7 ist 23. Als Term: 2x + 7 mit x = 8.",
    [B("2 + 8 + 7", "nur addiert, das Doppelte nicht gerechnet"), B("2 * (8 + 7)", "die Summe verdoppelt statt nur die Zahl"), B("2 * 8 * 7", "malgenommen statt addiert")]))
a2(T, "uebersetzen", Z(
    "Kim übersetzt: „Das Doppelte der Differenz aus x und 4, dazu das Dreifache von x.“ Welchen Wert hat der Term für x = 10?",
    42, "2 * (10 - 4) + 3 * 10", "12 + 30", "Die Differenz aus x und 4 heißt x − 4 (in dieser Reihenfolge). Davon das Doppelte braucht eine Klammer.",
    "Term: 2 · (x − 4) + 3x. Für x = 10: 2 · 6 + 30 = 12 + 30 = 42.",
    [B("2 * 10 - 4 + 3 * 10", "die Klammer weggelassen"), B("2 * (4 - 10) + 3 * 10", "die Differenz in falscher Reihenfolge gebildet"), B("2 * (10 - 4) * 3 * 10", "die beiden Teile malgenommen statt addiert")]))
a3(T, "uebersetzen", Z(
    "Ein Rechteck ist x cm breit. Die Länge ist 5 cm länger als das Doppelte der Breite. Der Umfang beträgt 70 cm. Wie breit ist das Rechteck in Zentimetern?",
    10, "(70 - 10) / 6", "(70 / 2 - 5) / 3", "Rechne mit dem halben Umfang: Breite plus Länge. Wie viele Breiten und wie viele Zentimeter stecken in der Länge? Probiere Breiten aus oder rechne rückwärts.",
    "Der halbe Umfang ist 35 cm: Breite plus Länge. Die Länge ist 2 Breiten und 5 cm. Probiere: Bei 5 cm Breite ist die Länge 15 cm und Breite plus Länge 20 cm (zu wenig). Bei 10 cm Breite ist die Länge 25 cm und Breite plus Länge 35 cm (stimmt). Rückwärts: 35 − 5 = 30 cm sind 3 Breiten, also ist die Breite 30 : 3 = 10 cm. Probe: Umfang 2 · (10 + 25) = 70.",
    [B("(70 - 10) / 3", "vom Umfang 70 nur 10 abgezogen und den Rest 60 durch 3 statt durch 6 geteilt"), B("70 - 10", "vom Umfang 70 nur 10 abgezogen und den Rest 60 als Breite angegeben"), B("70 / 2 - 5", "vom halben Umfang 35 nur 5 abgezogen und den Rest 30 als Breite angegeben")], "cm"), g="rueckwaerts")
# ───────── sachsituation ─────────
a1(T, "sachsituation", Z(
    "Ein Lieferdienst berechnet 2,50 € Liefergebühr und 8 € für jede Pizza. Wie viel Euro kosten 3 Pizzen mit Lieferung?",
    26.5, "2.5 + 8 * 3", "24 + 2.5", "Die Liefergebühr zahlt man nur einmal. Die 8 € zahlt man für jede Pizza.",
    "Die Pizzen kosten 3 · 8 = 24 €. Dazu kommt die Liefergebühr 2,50 €. Zusammen 24 + 2,50 = 26,50 €. Als Term: 2,5 + 8 · x mit x = 3.",
    [B("(2.5 + 8) * 3", "die Liefergebühr dreimal bezahlt"), B("2.5 * 3 + 8", "die Liefergebühr mit 3 malgenommen und nur eine Pizza gerechnet"), B("2.5 + 8 + 3", "alle Zahlen addiert")], "€"))
a2(T, "sachsituation", Z(
    "Auf Kims Sparbuch liegen 120 €. Jede Woche kommen 15 € dazu. Nach der 4. Woche werden einmal 30 € abgehoben. Wie viel Euro sind nach 8 Wochen auf dem Sparbuch?",
    210, "120 + 15 * 8 - 30", "120 + 120 - 30", "Wie oft kommen 15 € dazu? Die 30 € werden nur einmal abgehoben.",
    "Einzahlungen: 8 · 15 = 120 €. Startbetrag 120 €. Eine Abhebung: −30 €. Gesamt: 120 + 120 − 30 = 210 €.",
    [B("120 + 15 * 8", "die Abhebung vergessen"), B("(120 + 15) * 8 - 30", "den Startbetrag mit 8 malgenommen"), B("120 + 15 + 8 - 30", "die Zahlen 120, 15 und 8 addiert und die Abhebung 30 abgezogen")], "€"))
a3(T, "sachsituation", Z(
    "Eine Kletterhalle hat zwei Angebote. Gruppenkarte: 36 € Grundpreis und 4 € je Person. Einzelkarten: 10 € je Person. Ab wie vielen Personen ist die Gruppenkarte günstiger als die Einzelkarten?",
    7, "36 / (10 - 4) + 1", "6 + 1", "Rechne für 5, 6 und 7 Personen aus, was beide Angebote kosten. Wann sind sie gleich teuer, ab wann ist die Gruppenkarte günstiger?",
    "Probiere mit einer Tabelle (Gruppe: 36 + 4 je Person, einzeln: 10 je Person): 5 Personen 56 € und 50 €, 6 Personen 60 € und 60 € (gleich teuer), 7 Personen 64 € und 70 €. Erst ab 7 Personen ist die Gruppenkarte günstiger.",
    [B("36 / (10 - 4)", "die Personenzahl genannt, bei der beide Angebote gleich teuer sind"), B("36 / 4", "nur durch 4 geteilt"), B("36 / (10 - 4) - 1", "eine Person weniger als beim Gleichstand genommen")], "Personen"), g="verknuepfen")
# ───────── muster ─────────
a1(T, "muster", Z(
    "Plättchen werden zu Dreiecken gelegt: Figur 1 hat 1 Plättchen, Figur 2 hat 3 Plättchen, Figur 3 hat 6 Plättchen, Figur 4 hat 10 Plättchen. Von Figur zu Figur kommt unten eine neue Reihe mit einem Plättchen mehr dazu. Wie viele Plättchen hat Figur 10?",
    55, "10 * 11 / 2", "1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10", "Wie viele Plättchen kommen von Figur zu Figur dazu? Figur 10 besteht aus Reihen mit 1, 2, 3, … Plättchen.",
    "Figur n besteht aus Reihen mit 1, 2, 3, …, n Plättchen. Probe: Figur 4 hat 1 + 2 + 3 + 4 = 10. Figur 10 hat 1 + 2 + … + 10 = 55 Plättchen (zehn Reihen, paarweise 1 + 10, 2 + 9, … ergeben je 11, fünfmal).",
    [B("10 * 10", "ein Quadrat aus 10 mal 10 Plättchen gerechnet"), B("10 * 11", "die Summe nicht halbiert"), B("1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9", "die letzte Reihe mit 10 Plättchen vergessen")], "Plättchen"))
a2(T, "muster", Z(
    "Perlenketten wachsen nach einem Muster: Figur 1 hat 7 Perlen, Figur 2 hat 13 Perlen, Figur 3 hat 19 Perlen. So geht es weiter. Ab welcher Figur hat die Kette mehr als 100 Perlen?",
    17, "(100 - 1) // 6 + 1", "17", "Um wie viele Perlen wird die Kette von Figur zu Figur länger? Stelle den Term auf und probiere, wann 100 überschritten wird.",
    "Es kommen immer 6 Perlen dazu. Der Term ist 6n + 1. Probe: n = 1 gibt 7, n = 2 gibt 13, n = 3 gibt 19. Probieren: Figur 16 hat 6 · 16 + 1 = 97 Perlen (zu wenig), Figur 17 hat 6 · 17 + 1 = 103 Perlen. Ab Figur 17 sind es mehr als 100.",
    [B("(100 - 1) // 6", "abgerundet: Figur 16 hat erst 97 Perlen"), B("(100 - 1) / 6", "das Ergebnis der Division nicht auf eine ganze Figur gerundet"), B("6 * 17 + 1", "die Zahl der Perlen von Figur 17 statt der Figurnummer angegeben")]))
a3(T, "muster", Z(
    "Zwei Muster aus Plättchen: Muster A hat bei Figur n genau 4n + 2 Plättchen. Muster B hat bei Figur n genau 6n − 4 Plättchen. Bei welcher Figur haben beide Muster gleich viele Plättchen?",
    3, "(2 + 4) / (6 - 4)", "6 / 2", "Berechne beide Muster für n = 1, 2, 3, … in einer Tabelle. Wo stehen gleiche Zahlen?",
    "Lege eine Tabelle an. Figur 1: Muster A 6, Muster B 2. Figur 2: A 10, B 8. Figur 3: A 14, B 14. Bei Figur 3 sind beide gleich. Danach ist B immer größer, weil B bei jeder Figur 2 Plättchen mehr dazubekommt als A.",
    [B("2 + 4", "den Wert 6 = 2n nicht durch 2 geteilt"), B("6 - 4", "den Unterschied der Zahlen vor n als Lösung genommen"), B("6 + 4", "die Zahlen von Muster B addiert")]), g="pruefung")
# ───────── deuten ─────────
a1(T, "deuten", Z(
    "Der Term 40 − 5t gibt an, wie viele Kilometer noch bis zum Ziel fehlen, wenn eine Wandergruppe t Stunden unterwegs ist. Wie viele Kilometer wandert die Gruppe in jeder Stunde?",
    5, "5", "40 - 35", "Wie ändert sich der Term, wenn t um 1 größer wird? Was bedeutet die Zahl vor dem t?",
    "Wenn t um 1 wächst, wird 5t um 5 größer und der Term um 5 kleiner. Die Zahl vor dem t zählt pro Stunde: Die Gruppe wandert 5 km in jeder Stunde. Die 40 ist die Strecke am Anfang.",
    [B("40", "die Strecke am Anfang als Tempo genommen"), B("40 / 5", "die Dauer der ganzen Wanderung angegeben"), B("40 - 5", "die Zahlen subtrahiert")], "km"))
a2(T, "deuten", Z(
    "Die Wassermenge in einem Tank in Litern ist nach t Minuten 80 − 5t. Wie viele Minuten dauert es länger, bis der Tank ganz leer ist, als bis nur noch 35 Liter im Tank sind?",
    7, "80 / 5 - (80 - 35) / 5", "16 - 9", "Wann ist der Tank leer, wann sind noch 35 Liter darin? Probiere oder rechne rückwärts: Wie viele Liter sind bis dahin abgeflossen?",
    "Leer: 80 Liter sind abgeflossen, bei 5 Litern je Minute nach 80 : 5 = 16 Minuten. Noch 35 Liter: 80 − 35 = 45 Liter sind abgeflossen, nach 45 : 5 = 9 Minuten. Der Unterschied ist 16 − 9 = 7 Minuten.",
    [B("80 / 5", "nur die Zeit bis zur Leere angegeben"), B("(80 - 35) / 5", "nur die Zeit bis zu 35 Litern angegeben"), B("80 / 5 + (80 - 35) / 5", "beide Zeiten addiert statt den Unterschied gebildet")], "Minuten"))
a3(T, "deuten", Z(
    "Kim übersetzt „das Doppelte der Summe aus x und 3“ in den Term 2x + 3. Der richtige Term ist 2 · (x + 3). Um wie viel unterscheiden sich die beiden Werte für x = 5?",
    3, "2 * (5 + 3) - (2 * 5 + 3)", "16 - 13", "Berechne beide Terme einzeln für x = 5. Was wird bei Kims Term nur einmal und was zweimal gerechnet?",
    "Kims Term: 2 · 5 + 3 = 13. Richtiger Term: 2 · (5 + 3) = 16. Unterschied: 16 − 13 = 3. Der Fehler: Im richtigen Term wird auch die 3 verdoppelt, bei Kim nicht.",
    [B("2 * (5 + 3)", "nur den richtigen Wert angegeben"), B("2 * 5 + 3", "nur Kims Wert angegeben"), B("2 * 3", "die Verdopplung der 3 als Unterschied angegeben")]), g="fehler")
