T = "zahlen.ganz"
PM, ZG, VZ = "rr.plusminus", "id.zahlen.zahlengerade", "rr.vorzeichen"

# ───────── deuten ─────────
neu(T, "deuten", "zwei_wege", Z(
    "Eine Höhle liegt 12 m unter dem Meeresspiegel (−12 m). Ein Aussichtspunkt liegt 7 m über dem Meeresspiegel (7 m). Wie viele Meter liegt der Aussichtspunkt höher als die Höhle? Weg A: Zähle auf der Zahlengeraden von −12 bis 0 und dann weiter bis 7. Weg B: Rechne 7 − (−12).",
    19, "7 - (-12)", "12 + 7", "Der Meeresspiegel ist die Null. Wie weit ist es von der Höhle bis dorthin?",
    "Weg A: Von −12 bis 0 sind es 12 Meter, von 0 bis 7 weitere 7 Meter: 12 + 7 = 19. Weg B: 7 − (−12) = 7 + 12 = 19. Der Aussichtspunkt liegt 19 m höher.",
    [(5, None, "die beiden Beträge voneinander abgezogen: 12 − 7", "12 - 7"), (84, None, "die beiden Beträge malgenommen", "12 * 7"), (-5, None, "7 − 12 gerechnet", "7 - 12")], "m"))
neu(T, "deuten", "fehler_detektiv", FD(
    "Ein Konto steht auf −45 €. Dann werden 60 € eingezahlt. Tim überlegt, was auf dem Konto steht.",
    [("Der Stand −45 € bedeutet, dass 45 € Guthaben auf dem Konto sind.", -45 > 0, True),
     ("Nach der Einzahlung sind es 45 + 60 = 105 € Guthaben.", 45 + 60 == 105, True, "Zeile 2 rechnet 45 + 60 = 105 für sich richtig, geht aber schon von den falsch gedeuteten 45 € Guthaben aus."),
     ("Das Konto zeigt jetzt 105 €.", True, True, "Zeile 3 übernimmt nur das Ergebnis aus Zeile 2. Der Fehler liegt schon in Zeile 1.")],
    "Prüfe jede Zeile für sich und frage, was die Vorzeichen im Alltag bedeuten. Welche Zeile enthält zuerst einen Fehler?",
    "Ein negativer Kontostand bedeutet Schulden. Aus −45 € werden mit 60 € Einzahlung −45 + 60 = 15 €. Der erste Fehler steht in Zeile 1."))

# ───────── zahlengerade ─────────
neu(T, "zahlengerade", "umkehren", Z(
    "Von einer Zahl springt man auf der Zahlengeraden zuerst 9 Schritte nach links und dann 4 Schritte nach rechts. Man landet bei −2. Bei welcher Zahl ist man gestartet?",
    3, "-2 - (-9 + 4)", "-2 + 9 - 4", "Welche Gesamtbewegung ergeben die beiden Sprünge? Was musst du damit rückwärts tun?",
    "Die beiden Sprünge ergeben zusammen −9 + 4 = −5, also 5 Schritte nach links. Rückwärts geht man von −2 aus 5 Schritte nach rechts: −2 + 5 = 3. Probe: 3 − 9 + 4 = −2.",
    [(-7, None, "die Sprünge nicht rückgängig gemacht, sondern noch einmal ausgeführt", "-2 + (-9) + 4"), (-15, None, "beide Sprünge als Sprünge nach links gerechnet", "-2 - 9 - 4"), (-6, None, "nur den Sprung nach rechts rückgängig gemacht", "-2 - 4")]), g="umkehr", regel=ZG)
neu(T, "zahlengerade", "anwenden", Z(
    "Ein Seil hängt von einer Plattform in 8 m Höhe bis zu einem Anker in 16 m Tiefe. Die Höhe 0 m ist die Wasseroberfläche. Ein Knoten soll genau in der Mitte des Seils befestigt werden. In welcher Höhe in Metern, mit Vorzeichen, ist das?",
    -4, "(8 + (-16)) / 2", "8 - (8 + 16) / 2", "Welche Zahlen auf der Zahlengeraden gehören zu den beiden Enden des Seils?",
    "Die Enden liegen bei 8 m und −16 m. Die Mitte ist (8 + (−16)) : 2 = −8 : 2 = −4 m, also 4 m unter der Wasseroberfläche. Probe: Von −4 nach oben und nach unten sind es 12 m.",
    [(4, None, "das Vorzeichen vergessen", "-(8 + (-16)) / 2"), (12, None, "mit den Beträgen gerechnet: (8 + 16) : 2", "(8 + 16) / 2"), (-8, None, "nur die Tiefe halbiert", "-16 / 2")], "m"), g="transfer", regel=ZG)

# ───────── ordnen ─────────
_TEMP = [-8, 2, -3, -12, 0, -5]
neu(T, "ordnen", "bruecke", Z(
    "Die Tabelle zeigt die Temperaturen von sechs Orten in einer Winternacht. An wie vielen Orten ist es kälter als −3 °C?",
    3, "3", "1 + 1 + 1", "Kälter heißt: weiter links auf der Zahlengeraden als −3.",
    "Kälter als −3 °C sind −8 °C, −12 °C und −5 °C. 0 °C, 2 °C und −3 °C selbst sind nicht kälter. Es sind 3 Orte.",
    [(4, None, "−3 °C selbst mitgezählt", lambda: sum(t <= -3 for t in _TEMP) == 4), (2, None, "nur die beiden kältesten Orte gezählt", lambda: sum(t <= -8 for t in _TEMP) == 2)], "Orte",
    grafik=TAB(["Ort", "Temperatur in °C"], ["Alm", "−8"], ["Brunn", "2"], ["Cella", "−3"], ["Dorn", "−12"], ["Egg", "0"], ["Furt", "−5"])), regel=ZG)
neu(T, "ordnen", "fehler_detektiv", FD(
    "Mia ordnet die Zahlen −7, 3, −2 und −10 vom kleinsten zum größten.",
    [("Unter den negativen Zahlen ist −2 die kleinste, weil 2 die kleinste Ziffer ist.", -2 < -7, True),
     ("Danach kommen −7 und −10, zuletzt kommt 3.", True, True, "Zeile 2 folgt aus der Ordnung in Zeile 1: die Reihe ist dann −2, −7, −10 und zuletzt 3. Der Fehler liegt schon in Zeile 1."),
     ("Die Reihenfolge ist also −2, −7, −10, 3.", True, True, "Zeile 3 fasst Zeile 1 und 2 richtig zusammen. Der Fehler liegt schon in Zeile 1.")],
    "Prüfe jede Zeile für sich und zeichne die Zahlen in Gedanken auf die Zahlengerade. Welche Zeile enthält zuerst einen Fehler?",
    "Je weiter links, desto kleiner. Am weitesten links liegt −10, dann −7, dann −2, dann 3. Richtig: −10, −7, −2, 3. Der erste Fehler steht in Zeile 1."), regel=ZG)

# ───────── betrag ─────────
neu(T, "betrag", "bruecke", Z(
    "Auf der Zahlengeraden liegen zwei Zahlen, die beide genau 7 Schritte vom Nullpunkt entfernt sind, aber auf verschiedenen Seiten. Wie viele Schritte sind die beiden Zahlen voneinander entfernt?",
    14, "7 + 7", "7 - (-7)", "Wie heißen die beiden Zahlen? Zeichne dir den Weg von der einen zur anderen.",
    "Die beiden Zahlen sind −7 und 7. Von −7 bis 0 sind es 7 Schritte, von 0 bis 7 noch einmal 7. Zusammen sind es 14 Schritte.",
    [(7, None, "nur den Abstand zum Nullpunkt angegeben", "7"), (0, None, "7 und −7 addiert", "7 + (-7)")], "Schritte"))
neu(T, "betrag", "zwei_wege", Z(
    "Wie viele ganze Zahlen x erfüllen |x| < 4? Weg A: Schreibe alle diese Zahlen auf und zähle. Weg B: Überlege, wie weit man vom Nullpunkt nach rechts und nach links gehen darf, und rechne.",
    7, "2 * 3 + 1", "(4 - 1) + (4 - 1) + 1", "Zähle die Null mit. Welche Zahlen haben einen Abstand kleiner als 4 von der Null?",
    "Weg A: −3, −2, −1, 0, 1, 2, 3 sind 7 Zahlen. Weg B: nach rechts 3 Zahlen, nach links 3 Zahlen und die Null: 3 + 3 + 1 = 7.",
    [(3, None, "nur die positiven Zahlen gezählt", "3"), (6, None, "die Null vergessen", "2 * 3"), (9, None, "auch −4 und 4 mitgezählt", "2 * 4 + 1")], "Zahlen"), g="verknuepfen")

# ───────── schriftlich_plus_minus ─────────
neu(T, "schriftlich_plus_minus", "umkehren", Z(
    "Welche Zahl musst du zu 4 507 addieren, um 10 000 zu erhalten? Rechne schriftlich.",
    5493, "10000 - 4507", "5000 + 493", "Rechne rückwärts: Was musst du von 10 000 abziehen? Achte beim Abziehen auf das Borgen.",
    "Die gesuchte Zahl ist 10 000 − 4 507 = 5 493. Probe: 4 507 + 5 493 = 10 000.",
    [(14507, None, "addiert statt abgezogen", "10000 + 4507"), (5593, None, "beim Abziehen den Übertrag falsch gemerkt (Hunderter um 1 zu groß)", "10000 - 4407")]), g="umkehr")
neu(T, "schriftlich_plus_minus", "fehler_detektiv", FD(
    "Eva rechnet schriftlich 7 214 − 3 586 und beginnt bei den Einern. Dabei borgt sie immer 10 vom nächsten Stellenwert.",
    [("Einer: 4 − 6 geht nicht, also 14 − 6 = 8. Ich borge 1.", 14 - 6 == 8, True, "Zeile 1 stimmt: 14 − 6 = 8, und die geborgte 1 wird weitergegeben. Der Fehler steckt später."),
     ("Zehner: 1 + 10 − 8 − 1 = 2. Ich borge 1.", 1 + 10 - 8 - 1 == 2, True, "Zeile 2 stimmt: Die geborgte 1 wird abgezogen, 11 − 8 − 1 = 2, und wieder wird 1 geborgt. Der Fehler steckt später."),
     ("Hunderter: 2 + 10 − 5 − 1 = 6. Ich borge 1.", 2 + 10 - 5 - 1 == 6, True, "Zeile 3 stimmt: 12 − 5 − 1 = 6, und wieder wird 1 geborgt. Der Fehler steckt später."),
     ("Tausender: 7 − 3 = 4. Das Ergebnis ist 4 628.", 7 - 3 - 1 == 4, True)],
    "Prüfe jede Zeile für sich und mache zum Schluss die Probe mit der Addition. Welche Zeile enthält zuerst einen Fehler?",
    "Beim Tausender muss das geborgte 1 noch abgezogen werden: 7 − 3 − 1 = 3. Richtig: 7 214 − 3 586 = 3 628. Der erste Fehler steht in Zeile 4."))

# ───────── addieren ─────────
neu(T, "addieren", "zwei_wege", Z(
    "Berechne (−47) + 38 + 47 + 15 auf zwei Wegen. Weg A: Rechne von links nach rechts. Weg B: Vertausche die Summanden so, dass sich zwei Zahlen aufheben.",
    53, "(-47) + 38 + 47 + 15", "(-47) + 47 + 38 + 15", "Welche zwei Zahlen ergeben zusammen null?",
    "Weg A: (−47) + 38 = −9, −9 + 47 = 38, 38 + 15 = 53. Weg B: (−47) + 47 = 0, dann 38 + 15 = 53.",
    [(-41, None, "die 47 als minus gerechnet", "(-47) + 38 - 47 + 15"), (-9, None, "nur die ersten beiden Zahlen addiert", "(-47) + 38")]), regel=PM)
neu(T, "addieren", "anwenden", Z(
    "Bei einem Spiel gibt es Plus- und Minuspunkte. Jule hat in Runde 1 genau −4 Punkte gemacht, in Runde 2 genau +7 und in Runde 3 genau −13. Sie möchte nach Runde 4 insgesamt genau 5 Punkte haben. Wie viele Punkte muss sie in Runde 4 bekommen?",
    15, "5 - (-4 + 7 - 13)", "5 + 10", "Wie viele Punkte hat Jule nach drei Runden zusammen? Wie weit ist das von 5 entfernt?",
    "Nach drei Runden: −4 + 7 − 13 = −10. Bis 5 fehlen 5 − (−10) = 15. In Runde 4 braucht sie 15 Punkte. Probe: −10 + 15 = 5.",
    [(-5, None, "den Stand nach drei Runden mit falschem Vorzeichen zu 5 addiert", "5 + (-4 + 7 - 13)"), (10, None, "nur den Betrag des Stands nach drei Runden genannt", "4 - 7 + 13"), (18, None, "den Stand der Runden 1 und 2 vergessen", "5 - (-13)")], "Punkte"), g="transfer", regel=PM)

# ───────── subtrahieren ─────────
neu(T, "subtrahieren", "bruecke", Z(
    "Berechne −5 − (−12). Der Wert ist die Zahl der Schritte, die man auf der Zahlengeraden von −12 bis −5 nach rechts geht. Wie viele Schritte sind das?",
    7, "-5 - (-12)", "12 - 5", "Wo liegen −12 und −5 auf der Zahlengeraden? Welche liegt weiter rechts?",
    "Von −12 bis −5 sind es 12 − 5 = 7 Schritte nach rechts. Auch gerechnet: −5 − (−12) = −5 + 12 = 7.",
    [(-17, "fb.plusminus.doppelminus_uebersehen", "„minus minus“ als Minus gerechnet: −5 − 12", "-5 - 12"), (-7, None, "die Richtung falsch gezählt", "-(12 - 5)"), (17, None, "die Beträge addiert", "5 + 12")], "Schritte"), regel=PM)
neu(T, "subtrahieren", "fehler_detektiv", FD(
    "Lea berechnet 7 − (−4) − 9.",
    [("7 − (−4) = 7 − 4.", 7 - (-4) == 7 - 4, True),
     ("7 − 4 = 3.", 7 - 4 == 3, True, "Zeile 2 rechnet 7 − 4 = 3 für sich richtig, benutzt aber schon den falschen Ansatz aus Zeile 1."),
     ("3 − 9 = −6.", 3 - 9 == -6, True, "Zeile 3 rechnet 3 − 9 = −6 für sich richtig. Der Fehler liegt schon in Zeile 1.")],
    "Prüfe jede Zeile für sich und überlege, wie man eine negative Zahl abzieht. Welche Zeile enthält zuerst einen Fehler?",
    "Minus (−4) ist dasselbe wie plus 4: 7 − (−4) = 7 + 4 = 11. Dann 11 − 9 = 2. Der erste Fehler steht in Zeile 1."), regel=PM)

# ───────── umkehraufgabe ─────────
neu(T, "umkehraufgabe", "bruecke", Z(
    "Auf der Zahlengeraden springt man von einer Zahl x aus 17 Schritte nach rechts und landet bei −9. Welche Zahl ist x?",
    -26, "-9 - 17", "-9 + (-17)", "Gehe den Sprung rückwärts: von −9 aus 17 Schritte in die andere Richtung.",
    "Der Sprung heißt x + 17 = −9. Rückwärts: x = −9 − 17 = −26. Probe: −26 + 17 = −9.",
    [(8, None, "die Sprungweite in die falsche Richtung gerechnet: −9 + 17", "-9 + 17"), (26, None, "das Vorzeichen vergessen", "9 + 17")]), regel=PM)
neu(T, "umkehraufgabe", "anwenden", Z(
    "Ein Konto wurde um 35 € belastet (Abbuchung) und steht danach auf −12 €. Welchen Kontostand hatte es vorher?",
    23, "-12 + 35", "35 - 12", "Die Abbuchung hat den Stand um 35 kleiner gemacht. Mache das rückgängig.",
    "Gleichung: x − 35 = −12. Rückwärts: x = −12 + 35 = 23 €. Probe: 23 − 35 = −12.",
    [(-47, None, "die Abbuchung noch einmal abgezogen", "-12 - 35"), (-23, None, "das Vorzeichen des Ergebnisses falsch", "-(35 - 12)")], "€"), g="transfer", regel=PM)

# ───────── ketten ─────────
neu(T, "ketten", "umkehren", Z(
    "Welche ganze Zahl muss im Kästchen stehen, damit die Gleichung stimmt? −2 + □ − 7 + 3 = −14",
    -8, "-14 + 2 + 7 - 3", "-14 - (-2 - 7 + 3)", "Fasse die bekannten Zahlen zusammen: −2 − 7 + 3. Was muss □ dann ergeben?",
    "−2 − 7 + 3 = −6. Also □ + (−6) = −14 und □ = −14 + 6 = −8. Probe: −2 + (−8) − 7 + 3 = −14.",
    [(-12, None, "die Zahlen mit falschem Vorzeichen auf die andere Seite gebracht", "-14 - 2 + 7 - 3"), (-26, None, "alle Zahlen subtrahiert", "-14 - 2 - 7 - 3")]), g="umkehr", regel=PM)
neu(T, "ketten", "fehler_detektiv", FD(
    "Ben berechnet −14 + 20 − 9 − (−6).",
    [("−14 + 20 = 6.", -14 + 20 == 6, True, "Zeile 1 stimmt: −14 + 20 = 6. Der Fehler steckt später."),
     ("6 − 9 = −2.", 6 - 9 == -2, True),
     ("−2 − (−6) = −2 + 6 = 4.", -2 - (-6) == 4, True, "Zeile 3 rechnet −2 − (−6) = −2 + 6 = 4 für sich richtig, benutzt aber das falsche Ergebnis aus Zeile 2. Der Fehler liegt schon in Zeile 2.")],
    "Prüfe jede Zeile für sich und gehe auf der Zahlengeraden mit. Welche Zeile enthält zuerst einen Fehler?",
    "6 − 9 = −3. Weiter: −3 − (−6) = −3 + 6 = 3. Der erste Fehler steht in Zeile 2."), regel=PM)

# ───────── verstehen ─────────
neu(T, "verstehen", "zwei_wege", Z(
    "Lena behauptet: „Wenn ich von 5 eine Zahl abziehe, wird das Ergebnis immer kleiner als 5.“ Bei wie vielen der Zahlen −2, 3, −4, 6, −1, 2 und 7 stimmt die Behauptung nicht? Weg A: Rechne 5 − b für jede Zahl b aus und vergleiche mit 5. Weg B: Überlege nur mit dem Vorzeichen von b, was beim Abziehen passiert.",
    3, "3", "1 + 1 + 1", "Was passiert mit 5, wenn man eine negative Zahl abzieht?",
    "Weg A: 5 − (−2) = 7, 5 − 3 = 2, 5 − (−4) = 9, 5 − 6 = −1, 5 − (−1) = 6, 5 − 2 = 3, 5 − 7 = −2. Größer als 5 wird es bei −2, −4 und −1. Weg B: Das Abziehen einer negativen Zahl macht größer, also sind alle drei negativen Zahlen Gegenbeispiele.",
    [(4, None, "die Zahlen gezählt, bei denen die Behauptung stimmt", "7 - 3"), (7, None, "alle Zahlen gezählt", "7"), (2, None, "die Zahl −1 übersehen", "3 - 1")], "Zahlen"))
neu(T, "verstehen", "umkehren", Z(
    "Tom behauptet: „Wenn man etwas abzieht, wird das Ergebnis immer kleiner.“ Anna findet ein Gegenbeispiel. Sie zieht eine Zahl b von 4 ab und erhält 11. Welche Zahl hat Anna abgezogen?",
    -7, "4 - 11", "-(11 - 4)", "Muss b größer oder kleiner als null sein, damit 4 − b größer als 4 wird?",
    "Aus 4 − b = 11 folgt b = 4 − 11 = −7. Probe: 4 − (−7) = 4 + 7 = 11. Das Abziehen einer negativen Zahl macht größer, deshalb widerlegt dieses Beispiel die Behauptung.",
    [(7, None, "das Vorzeichen vergessen: 11 − 4", "11 - 4"), (15, None, "4 und 11 addiert", "4 + 11"), (-15, None, "4 und 11 addiert und mit Minus versehen", "-(4 + 11)")]), g="rueckwaerts")

# ───────── sach ─────────
neu(T, "sach", "zwei_wege", Z(
    "Ein Spielkonto steht am Anfang auf −20 Punkten. Dann gibt es Gewinne von 50 und 10 Punkten und einen Verlust von 35 Punkten. Welchen Stand hat das Spielkonto am Ende? Weg A: Rechne die Änderungen der Reihe nach. Weg B: Fasse Gewinne und Verlust zusammen und rechne dann mit dem Anfangsstand.",
    5, "-20 + 50 + 10 - 35", "-20 + (50 + 10 - 35)", "Bei Weg B: Wie viel ist es insgesamt, wenn du 50 und 10 gewinnst und 35 verlierst?",
    "Weg A: −20 + 50 = 30, 30 + 10 = 40, 40 − 35 = 5. Weg B: Gewinne und Verlust zusammen: 50 + 10 − 35 = 25. Dann −20 + 25 = 5.",
    [(25, None, "den Anfangsstand vergessen", "50 + 10 - 35"), (-115, None, "alle Änderungen abgezogen", "-20 - 50 - 10 - 35")], "Punkte"), regel=PM)
neu(T, "sach", "fehler_detektiv", FD(
    "Ein Taucher ist auf −18 m. Er steigt 7 m, sinkt dann 12 m und steigt dann 5 m. Paul berechnet, wo er jetzt ist.",
    [("Nach dem Aufsteigen: −18 + 7 = −11.", -18 + 7 == -11, True, "Zeile 1 stimmt: −18 + 7 = −11. Der Fehler steckt später."),
     ("Nach dem Sinken: −11 − 12 = −23.", -11 - 12 == -23, True, "Zeile 2 stimmt: −11 − 12 = −23. Der Fehler steckt später."),
     ("Nach dem Aufsteigen: −23 + 5 = −28.", -23 + 5 == -28, True),
     ("Der Taucher ist bei −28 m.", True, True, "Zeile 4 übernimmt nur das Ergebnis aus Zeile 3. Der Fehler liegt schon davor.")],
    "Prüfe jede Zeile für sich und überlege, ob die Höhe beim Steigen größer oder kleiner wird. Welche Zeile enthält zuerst einen Fehler?",
    "−23 + 5 = −18, denn man geht 5 Schritte nach rechts. Der Taucher ist bei −18 m. Der erste Fehler steht in Zeile 3."), regel=PM)
