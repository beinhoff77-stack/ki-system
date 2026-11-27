T = "groessen.einheiten"
GR = "id.verhaeltnisse.groesse"

# ───────── schaetzen ─────────
neu(T, "schaetzen", "zwei_wege", Z(
    "Eine Treppenstufe ist etwa 20 cm hoch. Weg A: Rechne 9 m in cm um und teile durch die Höhe einer Stufe. Weg B: Überlege, wie viele Stufen auf 1 m kommen, und rechne damit weiter. Wie viele Stufen braucht eine Treppe für einen Höhenunterschied von 9 m ungefähr?",
    45, "900 / 20", "9 * (100 / 20)", "Wie viele Stufen von 20 cm sind zusammen 1 m hoch?",
    "Weg A: 9 m = 900 cm, 900 : 20 = 45. Weg B: 1 m = 100 cm, das sind 100 : 20 = 5 Stufen. Für 9 m sind es 9 · 5 = 45 Stufen.",
    [(180, None, "9 mal 20 gerechnet", "9 * 20"), (0.45, None, "9 durch 20 geteilt, ohne die Meter in cm umzurechnen", "9 / 20"), (5, None, "nur die Stufen für 1 m genannt", "100 / 20")], "Stufen"), regel=GR)
neu(T, "schaetzen", "umkehren", Z(
    "Ein Kind geht einen 150 m langen Weg in 250 Schritten, ein Erwachsener braucht für denselben Weg 200 Schritte. Um wie viel cm ist ein Schritt des Erwachsenen länger als ein Schritt des Kindes?",
    15, "150 * 100 / 200 - 150 * 100 / 250", "75 - 60", "Was ist bei beiden gleich, was ist verschieden? Was vergleichst du am Ende?",
    "150 m = 15 000 cm. Kind: 15 000 cm : 250 = 60 cm je Schritt. Erwachsener: 15 000 cm : 200 = 75 cm je Schritt. Unterschied: 75 cm − 60 cm = 15 cm. Probe: 200 · 75 cm = 15 000 cm = 150 m.",
    [(75, None, "nur die Schrittlänge des Erwachsenen genannt: 15 000 : 200", "150 * 100 / 200"), (50, None, "die Schrittzahlen statt der Schrittlängen verglichen: 250 − 200", "250 - 200"), (0.15, None, "das Ergebnis in Metern statt in cm angegeben: 0,75 m − 0,6 m", "150 / 200 - 150 / 250")], "cm"), g="rueckwaerts", regel=GR)

# ───────── laenge ─────────
neu(T, "laenge", "umkehren", Z(
    "Ein Band wurde um 135 cm gekürzt. Jetzt ist es 2 m 15 cm lang. Wie lang war es vorher in cm?",
    350, "215 + 135", "200 + 15 + 135", "Mache das Kürzen rückgängig. Rechne zuerst die jetzige Länge in cm.",
    "Jetzt: 2 m 15 cm = 215 cm. Vorher war das Band um 135 cm länger: 215 + 135 = 350 cm.",
    [(80, None, "die gekürzte Länge von der jetzigen abgezogen", "215 - 135"), (2150, None, "2 m 15 cm als 2 015 cm gelesen und 135 cm addiert", "2015 + 135"), (215, None, "nur die jetzige Länge in cm genannt", "215")], "cm"), g="umkehr", regel=GR)
neu(T, "laenge", "zwei_wege", Z(
    "Weg A: Rechne 3 km in m um und addiere 40 m. Weg B: Schreibe die Länge zuerst als Dezimalzahl in km und rechne dann in m um. Wie viele Meter sind 3 km 40 m?",
    3040, "3 * 1000 + 40", "3.04 * 1000", "Wie viele Meter hat 1 km? Wie schreibt man 40 m in km?",
    "Weg A: 3 km = 3 000 m, dazu 40 m: 3 040 m. Weg B: 40 m = 0,04 km, also 3 km 40 m = 3,04 km. 3,04 · 1 000 = 3 040 m.",
    [(340, None, "3 km als 300 m gerechnet", "300 + 40"), (3400, None, "40 m als 400 m gerechnet", "3000 + 400"), (30040, None, "3 km als 30 000 m gerechnet", "30000 + 40")], "m"), g="verknuepfen", regel=GR)

# ───────── masse ─────────
neu(T, "masse", "bruecke", Z(
    "Die Tabelle zeigt die Zutaten für einen Kuchen in verschiedenen Einheiten. Wie viele Kilogramm wiegen alle drei Zutaten zusammen?",
    3.5, "(2500 + 750 + 250) / 1000", "2.5 + 0.75 + 0.25", "Schreibe alle Mengen in derselben Einheit, bevor du addierst.",
    "In g: 2 kg 500 g = 2 500 g, dazu 750 g und 250 g: 2 500 + 750 + 250 = 3 500 g = 3,5 kg.",
    [(3500, None, "in g angegeben statt in kg", "2500 + 750 + 250"), (1002.5, None, "ohne Umrechnung 2,5 + 750 + 250 addiert", "2.5 + 750 + 250"), (3.0, None, "die 500 g bei den 2 kg vergessen", "2 + 0.75 + 0.25")], "kg",
    grafik=TAB(["Zutat", "Menge"], ["Mehl", "2 kg 500 g"], ["Zucker", "750 g"], ["Butter", "250 g"])), regel=GR)
neu(T, "masse", "anwenden", Z(
    "Ein Lastenaufzug trägt höchstens 1 t. Auf ihm stehen schon 7 Kisten zu je 120 kg. Wie viele weitere Kisten zu je 25 kg dürfen höchstens noch dazu gestellt werden?",
    6, "(1000 - 7 * 120) // 25", "160 // 25", "Rechne 1 t in kg um. Wie viele kg sind noch frei?",
    "1 t = 1 000 kg. Schon da: 7 · 120 = 840 kg. Noch frei: 160 kg. 160 : 25 = 6,4, es passen also höchstens 6 Kisten.",
    [(7, None, "auf 7 aufgerundet, obwohl das Limit überschritten würde", "-(-160 // 25)"), (160, None, "die freie Masse in kg genannt", "1000 - 7 * 120"), (40, None, "1 000 durch 25 geteilt, die schon stehenden Kisten vergessen", "1000 / 25")], "Kisten"), g="transfer", regel=GR)

# ───────── zeit ─────────
neu(T, "zeit", "bruecke", Z(
    "Der Fahrplan zeigt Abfahrt und Ankunft eines Zuges. Wie viele Minuten dauert die Fahrt?",
    85, "(10 * 60 + 12) - (8 * 60 + 47)", "13 + 60 + 12", "Wie viele Minuten sind es bis 9:00 Uhr? Dann weiter bis 10:12 Uhr.",
    "Von 8:47 Uhr bis 9:00 Uhr sind es 13 Minuten, von 9:00 Uhr bis 10:12 Uhr sind es 72 Minuten. Zusammen 13 + 72 = 85 Minuten.",
    [(125, None, "1 h 25 min als 125 min gelesen (1 h = 100 min gerechnet)", "1 * 100 + 25"), (35, None, "47 − 12 Minuten gerechnet", "47 - 12"), (155, None, "Stunden und Minuten einzeln voneinander abgezogen, ohne die Minuten über eine Stunde hinweg richtig zu behandeln", "(10 - 8) * 60 + (47 - 12)")], "min",
    grafik=TAB(["Halt", "Uhrzeit"], ["Abfahrt Hauptbahnhof", "8:47 Uhr"], ["Ankunft Altstadt", "10:12 Uhr"])))
neu(T, "zeit", "zwei_wege", Z(
    "Weg A: Ergänze bis zur vollen Stunde und zähle dann weiter. Weg B: Rechne beide Uhrzeiten in Minuten seit Mitternacht um und ziehe ab. Wie viele Minuten liegen zwischen 14:35 Uhr und 17:10 Uhr?",
    155, "(17 * 60 + 10) - (14 * 60 + 35)", "25 + 120 + 10", "Wie viele Minuten sind es von 14:35 Uhr bis 15:00 Uhr?",
    "Weg A: 14:35 bis 15:00 sind 25 min, 15:00 bis 17:00 sind 120 min, 17:00 bis 17:10 sind 10 min: 155 min. Weg B: 17:10 Uhr = 1 030 min, 14:35 Uhr = 875 min. 1 030 − 875 = 155.",
    [(235, None, "1 h = 100 min gerechnet: 2 h 35 min als 2 · 100 + 35", "100 * 2 + 35"), (205, None, "3 h gerechnet und die 25 Minuten addiert statt abgezogen", "3 * 60 + (35 - 10)"), (25, None, "nur bis zur vollen Stunde gerechnet", "60 - 35")], "min"), g="verknuepfen")

# ───────── kommaschreibweise ─────────
neu(T, "kommaschreibweise", "anwenden", Z(
    "Ein Wanderweg ist 12,5 km lang. Marie ist schon 4 800 m gegangen. Wie viele Meter muss sie noch gehen?",
    7700, "12.5 * 1000 - 4800", "12500 - 4800", "Rechne beide Längen in dieselbe Einheit um, bevor du abziehst.",
    "12,5 km = 12 500 m. Noch zu gehen: 12 500 − 4 800 = 7 700 m.",
    [(7.7, None, "das Ergebnis in km statt in m angegeben", "12.5 - 4.8"), (-4787.5, None, "ohne Umrechnung 12,5 − 4 800 gerechnet", "12.5 - 4800"), (8500, None, "nur 4 000 m statt 4 800 m abgezogen", "12500 - 4000")], "m"), regel=GR)
neu(T, "kommaschreibweise", "zwei_wege", Z(
    "Tim rechnet: „3,08 kg sind 3 kg 8 g, also 3 008 g.“ Prüfe seine Umrechnung. Weg A: Rechne 3,08 · 1 000. Weg B: Schreibe 3,08 kg mit drei Stellen hinter dem Komma (3,080 kg) und lies kg und g ab. Wie viele Gramm sind 3,08 kg wirklich?",
    3080, "3.08 * 1000", "3 * 1000 + 80", "Ein Gramm ist ein Tausendstel eines Kilogramms. Welche Stellen hinter dem Komma gehören zu den Gramm?",
    "Weg A: 3,08 · 1 000 = 3 080 g. Weg B: 3,08 kg = 3,080 kg. Vor dem Komma stehen die 3 kg, die drei Stellen dahinter (080) sind die Gramm: 3 kg 80 g = 3 000 g + 80 g = 3 080 g.",
    [(308, None, "mit 100 statt mit 1 000 malgenommen", "3.08 * 100"), (30800, None, "mit 10 000 malgenommen", "3.08 * 10000"), (3008, None, "Tims Fehler: 0,08 kg als 8 g gelesen", "3 * 1000 + 8")], "g"), g="verknuepfen", regel=GR)

# ───────── rechnen ─────────
neu(T, "rechnen", "umkehren", Z(
    "Von einem 5 m langen Seil werden zwei gleich lange Stücke abgeschnitten. Übrig bleibt ein Rest von 1 m 20 cm. Wie lang ist jedes abgeschnittene Stück in cm?",
    190, "(500 - 120) / 2", "380 / 2", "Wie viel Seil wurde insgesamt abgeschnitten? Beide Längen müssen dazu in derselben Einheit stehen.",
    "5 m = 500 cm und 1 m 20 cm = 120 cm. Abgeschnitten wurden 500 cm − 120 cm = 380 cm. Das sind zwei gleich lange Stücke: 380 cm : 2 = 190 cm. Probe: 2 · 190 cm + 120 cm = 500 cm.",
    [(380, None, "nicht durch 2 geteilt", "500 - 120"), (310, None, "den Rest addiert statt abgezogen", "(500 + 120) / 2"), (240, None, "nur 20 cm statt 1 m 20 cm als Rest abgezogen", "(500 - 20) / 2")], "cm"), g="umkehr")
neu(T, "rechnen", "anwenden", Z(
    "Vier Freunde teilen sich die Rechnung von 46,80 € und zusätzlich 2 € Trinkgeld gleichmäßig auf. Wie viel Euro zahlt jeder?",
    12.2, "(46.8 + 2) / 4", "46.8 / 4 + 0.5", "Wie viel kostet alles zusammen? Wie teilst du das auf vier Personen auf?",
    "Insgesamt: 46,80 € + 2 € = 48,80 €. Jeder zahlt 48,80 € : 4 = 12,20 €.",
    [(11.7, None, "das Trinkgeld vergessen", "46.8 / 4"), (13.7, None, "jedem 2 € Trinkgeld aufgerechnet", "46.8 / 4 + 2"), (48.8, None, "nicht durch 4 geteilt", "46.8 + 2")], "€"), g="transfer")

# ───────── massstab ─────────
neu(T, "massstab", "zwei_wege", Z(
    "Auf einer Karte mit dem Maßstab 1 : 25 000 sind zwei Orte 8 cm voneinander entfernt. Weg A: Rechne 8 cm mal 25 000 und wandle um. Weg B: Bestimme zuerst, wie viele Meter 1 cm auf der Karte in Wirklichkeit sind, und rechne damit. Wie viele Kilometer liegen sie in Wirklichkeit auseinander?",
    2, "8 * 25000 / 100 / 1000", "8 * 250 / 1000", "Wie viele cm sind 1 km? Wie viele m sind 25 000 cm?",
    "Weg A: 8 · 25 000 cm = 200 000 cm = 2 000 m = 2 km. Weg B: 1 cm auf der Karte sind 25 000 cm = 250 m. 8 · 250 m = 2 000 m = 2 km.",
    [(200, None, "durch 1 000 statt durch 100 000 umgerechnet", "8 * 25000 / 1000"), (20, None, "durch 10 000 statt durch 100 000 umgerechnet", "8 * 25000 / 10000"), (0.2, None, "durch 1 000 000 umgerechnet", "8 * 25000 / 1000000")], "km"), regel=GR)
neu(T, "massstab", "anwenden", Z(
    "Auf einer Wanderkarte mit dem Maßstab 1 : 50 000 ist der Weg zur Hütte 14 cm lang. Eine Gruppe wandert 4 km pro Stunde. Wie viele Minuten braucht sie für den Weg?",
    105, "14 * 50000 / 100000 / 4 * 60", "7 / 4 * 60", "Welche Größen brauchst du, um aus Weglänge und Tempo eine Zeit zu bekommen? Auf welche Einheiten musst du achten?",
    "14 · 50 000 cm = 700 000 cm = 7 km. 7 km : 4 km/h = 1,75 h. 1,75 h = 105 min.",
    [(7, None, "nur die Länge in km genannt", "14 * 50000 / 100000"), (1.75, None, "die Zeit in Stunden angegeben", "7 / 4"), (420, None, "7 · 60 gerechnet (Geschwindigkeit nicht beachtet)", "7 * 60")], "min"), g="transfer", regel=GR)

# ───────── verstehen ─────────
neu(T, "verstehen", "bruecke", Z(
    "Die Tabelle nennt fünf Beispiele für Gegenstände mit einer Größenangabe. Bei wie vielen Gegenständen ist die Angabe nicht realistisch?",
    2, "2", "1 + 1", "Vergleiche mit etwas, das du kennst: Wie lang ist ein Lineal? Wie schwer ist ein Apfel?",
    "Ein Bleistift mit 5 kg wäre so schwer wie fünf Packungen Zucker, er wiegt nur wenige Gramm. Ein Kind mit 14 m wäre höher als ein Haus. Die anderen Angaben passen: Heft 21 cm, Zimmerhöhe 3 m, Apfel 150 g. Es sind 2 Angaben.",
    [(1, None, "nur eine unrealistische Angabe gefunden", "1"), (3, None, "auch die Höhe des Klassenzimmers (3 m) für unrealistisch gehalten", "2 + 1"), (5, None, "alle Angaben für unrealistisch gehalten", "5")], "Angaben",
    grafik=TAB(["Gegenstand", "Angabe"], ["Schulheft", "21 cm lang"], ["Bleistift", "5 kg schwer"], ["Klassenzimmer", "3 m hoch"], ["Apfel", "150 g schwer"], ["Kind mit 10 Jahren", "14 m groß"])), g="darstellung")
_ab = lambda h, m, dh, dm: ((h * 60 + m - dh * 60 - dm) // 60, (h * 60 + m - dh * 60 - dm) % 60)
neu(T, "verstehen", "umkehren", W(
    "Ein Zug kommt um 15:12 Uhr an. Die Fahrt hat 2,5 Stunden gedauert. Tim sagt: „Er ist um 12:22 Uhr abgefahren.“ Welche Abfahrtszeit ist richtig?",
    "12:42 Uhr",
    [("17:42 Uhr", "Die Fahrzeit wurde addiert statt abgezogen."), ("12:12 Uhr", "Die 2,5 Stunden wurden als 3 Stunden gerechnet."), ("12:22 Uhr", "Das ist Tims Angabe. Er hat 0,5 Stunden als 50 Minuten gerechnet.")],
    "Rechne 2,5 Stunden in Stunden und Minuten um. Gehe dann rückwärts von der Ankunftszeit und prüfe Tims Angabe.",
    "2,5 h = 2 h 30 min. Rückwärts von 15:12 Uhr: 2 h zurück ergibt 13:12 Uhr, weitere 30 min zurück ergibt 12:42 Uhr. Probe: 12:42 Uhr + 2 h 30 min = 15:12 Uhr.",
    lambda: _ab(15, 12, 2, 30) == (12, 42) and _ab(15, 12, -2, -30) == (17, 42) and _ab(15, 12, 3, 0) == (12, 12) and _ab(15, 12, 2, 50) == (12, 22)), g="rueckwaerts")
