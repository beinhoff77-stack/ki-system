T = "zahlen.rechengesetze"
RF, TA, AM, GR = "rr.reihenfolge", "rr.tauschen", "rr.ausmultiplizieren", "rr.gegenrechnung"

# ───────── punkt_strich ─────────
neu(T, "punkt_strich", "bruecke", W(
    "Zu 20 wird das Produkt aus 6 und 4 addiert. Danach wird 8 abgezogen. Welcher Term beschreibt das richtig?",
    "20 + 6 · 4 − 8",
    [("(20 + 6) · 4 − 8", "Zuerst 20 und 6 addiert, dann mit 4 malgenommen."), ("20 + 6 · (4 − 8)", "Die 8 wird von der 4 statt vom Ergebnis abgezogen."), ("20 + 6 + 4 − 8", "Das Produkt wurde durch eine Summe ersetzt.")],
    "Das Produkt aus 6 und 4 ist ein eigener Rechenschritt. Schreibe es ohne Klammern auf.",
    "„Produkt aus 6 und 4“ ist 6 · 4. Dazu 20 addieren: 20 + 6 · 4. Dann 8 abziehen: 20 + 6 · 4 − 8. Punkt vor Strich passt hier ohne Klammern: 20 + 24 − 8 = 36.",
    lambda: 20 + 6 * 4 - 8 == 36 and (20 + 6) * 4 - 8 == 96 and 20 + 6 * (4 - 8) == -4 and 20 + 6 + 4 - 8 == 22), regel=RF)
neu(T, "punkt_strich", "umkehren", Z(
    "Welche Zahl muss im Kästchen stehen, damit die Gleichung stimmt? 5 + □ · 4 = 49",
    11, "(49 - 5) / 4", "49 / 4 - 5 / 4 + 0", "Gehe die Rechnung rückwärts. Was passiert zuletzt, was musst du also zuerst rückgängig machen?",
    "Zuletzt wird 5 addiert, also zuerst 5 abziehen: 49 − 5 = 44. Dann das Malnehmen mit 4 rückgängig machen: 44 : 4 = 11. Probe: 5 + 11 · 4 = 5 + 44 = 49.",
    [(44, None, "nur 5 abgezogen, das Malnehmen mit 4 nicht rückgängig gemacht", "49 - 5"), (40, None, "erst 5 und dann 4 abgezogen", "49 - 5 - 4")]), g="rueckwaerts", regel=RF)

# ───────── klammern ─────────
neu(T, "klammern", "zwei_wege", Z(
    "Berechne (48 − 12) : 6 auf zwei Wegen. Weg A: Rechne zuerst die Klammer aus. Weg B: Teile beide Zahlen in der Klammer einzeln durch 6 und ziehe die Ergebnisse voneinander ab.",
    6, "(48 - 12) / 6", "48 / 6 - 12 / 6", "Bei Weg B teilst du jede Zahl in der Klammer durch 6.",
    "Weg A: 48 − 12 = 36, 36 : 6 = 6. Weg B: 48 : 6 = 8 und 12 : 6 = 2, 8 − 2 = 6. Beide Wege geben 6.",
    [(46, None, "die Klammer ignoriert: 48 − 12 : 6", "48 - 12 / 6"), (10, None, "beide Teilergebnisse addiert statt voneinander abgezogen", "48 / 6 + 12 / 6")]), regel=RF)
neu(T, "klammern", "fehler_detektiv", FD(
    "Jan berechnet (30 − 6) · 3 − 4 · 2.",
    [("Zuerst die Klammer: 30 − 6 = 24.", 30 - 6 == 24, True),
     ("Dann 24 · 3 = 72, also ist der Term gleich 72 − 4 · 2.", (30 - 6) * 3 - 4 * 2 == 72 - 4 * 2, True),
     ("Von links nach rechts: 72 − 4 = 68, und 68 · 2 = 136.", 72 - 4 * 2 == 136, True)],
    "Welche Rechenart wird zuerst ausgeführt: Minus oder Mal?",
    "Punkt vor Strich: 4 · 2 = 8 muss vor dem Abziehen gerechnet werden. 72 − 8 = 64. Der erste Fehler steht in Zeile 3."), regel=RF)

# ───────── termaufbau ─────────
neu(T, "termaufbau", "umkehren", Z(
    "Der Term 3 · (□ + 4) hat den Wert 27. Welche Zahl gehört in das Kästchen?",
    5, "27 / 3 - 4", "(27 - 12) / 3", "Das Kästchen steht in einer Klammer. Mache die Rechenschritte von außen nach innen rückgängig.",
    "3 · (□ + 4) = 27, also □ + 4 = 27 : 3 = 9 und □ = 9 − 4 = 5. Probe: 3 · (5 + 4) = 3 · 9 = 27.",
    [(9, None, "nur durch 3 geteilt, die 4 nicht abgezogen", "27 / 3"), (23, None, "nur die 4 abgezogen, nicht durch 3 geteilt", "27 - 4"), (20, None, "erst 3, dann 4 von 27 abgezogen", "27 - 3 - 4")]), g="umkehr", regel=GR)
neu(T, "termaufbau", "zwei_wege", Z(
    "Term A ist 6 + 4 · 5, Term B ist (6 + 4) · 5. Um wie viel ist B größer als A? Weg A: Berechne beide Terme und bilde den Unterschied. Weg B: Schreibe B als 6 · 5 + 4 · 5 und vergleiche mit A, ohne beide ganz auszurechnen.",
    24, "(6 + 4) * 5 - (6 + 4 * 5)", "6 * 5 - 6", "Bei B steht 4 · 5 schon im Term, bei A auch. Was unterscheidet die beiden Terme noch?",
    "Weg A: A = 6 + 20 = 26, B = 10 · 5 = 50, 50 − 26 = 24. Weg B: B = 6 · 5 + 4 · 5, A = 6 + 4 · 5. Der Unterschied ist 6 · 5 − 6 = 30 − 6 = 24.",
    [(50, None, "nur den Wert von B genannt", "(6 + 4) * 5"), (26, None, "nur den Wert von A genannt", "6 + 4 * 5"), (30, None, "nur 6 · 5 als Unterschied genommen", "6 * 5")]), g="verknuepfen", regel=RF)

# ───────── vorteil ─────────
neu(T, "vorteil", "umkehren", Z(
    "Welche Zahl muss im Kästchen stehen? 25 · □ = 1 700. Tipp für den Weg: 25 · 4 = 100.",
    68, "1700 / 25", "1700 / 100 * 4", "Wie viele 25er passen in 100? Wie viele Hunderter stecken in 1 700?",
    "In 1 700 stecken 17 Hunderter. In jedem Hunderter stecken 4 · 25. Also ist □ = 17 · 4 = 68. Probe: 25 · 68 = 1 700.",
    [(17, None, "nur die Hunderter gezählt, ohne mit 4 zu malnehmen", "1700 / 100"), (1675, None, "25 abgezogen statt geteilt", "1700 - 25"), (42500, None, "multipliziert statt geteilt", "1700 * 25")]), g="umkehr", regel=GR)
neu(T, "vorteil", "fehler_detektiv", FD(
    "Eva berechnet 4 · 37 · 25 geschickt.",
    [("Man darf die Faktoren vertauschen: 4 · 37 · 25 = 4 · 25 · 37.", 4 * 37 * 25 == 4 * 25 * 37, True),
     ("4 · 25 = 100.", 4 * 25 == 100, True),
     ("100 · 37 = 3 070.", 100 * 37 == 3070, True)],
    "Rechne 100 · 37 nach. Wie viele Nullen hängst du an 37 an?",
    "100 · 37 = 3 700, nicht 3 070. Richtig: 4 · 37 · 25 = 100 · 37 = 3 700. Der erste Fehler steht in Zeile 3."), regel=TA)

# ───────── differenz_summe ─────────
neu(T, "differenz_summe", "bruecke", W(
    "Mia hat 80 €. Sie gibt 25 € aus, bekommt dann 15 € geschenkt und gibt am Ende noch 35 € aus. Welche Rechnung gibt an, wie viel Geld sie am Ende hat?",
    "80 − 25 + 15 − 35",
    [("80 − (25 + 15 − 35)", "Das Geschenk und die zweite Ausgabe stehen in einer Klammer, die abgezogen wird."), ("80 − 25 − (15 + 35)", "Das Geschenk wird wie eine Ausgabe abgezogen."), ("80 + 25 − 15 + 35", "Ausgaben und Einnahmen vertauscht.")],
    "Jeder Schritt der Geschichte ist ein Plus oder Minus. Schreibe sie der Reihe nach auf.",
    "Start 80, dann „ausgegeben“ (−25), „geschenkt“ (+15), „ausgegeben“ (−35): 80 − 25 + 15 − 35 = 35.",
    lambda: 80 - 25 + 15 - 35 == 35 and 80 - (25 + 15 - 35) == 75 and 80 - 25 - (15 + 35) == 5 and 80 + 25 - 15 + 35 == 125), regel=TA)
neu(T, "differenz_summe", "anwenden", Z(
    "Auf einem Konto sind 540 €. Es werden 175 € abgehoben, dann 25 € eingezahlt und danach 125 € abgehoben. Wie viel Euro sind danach auf dem Konto? Rechne geschickt: Fasse die beiden Abhebungen zusammen.",
    265, "540 - (175 + 125) + 25", "540 - 300 + 25", "Die beiden Abhebungen darfst du zuerst zusammenzählen. Wie viel ist das?",
    "Abhebungen: 175 + 125 = 300. Einzahlung: 25. 540 − 300 + 25 = 265 €.",
    [(215, None, "die Einzahlung auch abgezogen", "540 - 175 - 25 - 125"), (240, None, "die Einzahlung vergessen", "540 - 175 - 125"), (865, None, "alle Beträge addiert", "540 + 300 + 25")], "€"), g="transfer", regel=TA)

# ───────── verteilen ─────────
neu(T, "verteilen", "zwei_wege", Z(
    "Berechne 8 · 27. Weg A: Rechne die Malaufgabe schriftlich. Weg B: Zerlege 27 in 20 + 7 und rechne 8 · 20 + 8 · 7.",
    216, "8 * 27", "8 * 20 + 8 * 7", "Bei Weg B rechnest du zwei einfache Malaufgaben und addierst.",
    "Weg A: 8 · 27 = 216. Weg B: 8 · 20 = 160, 8 · 7 = 56, 160 + 56 = 216.",
    [(167, None, "nur die erste Zahl der Zerlegung malgenommen: 8 · 20 + 7", "8 * 20 + 7"), (160, None, "nur 8 · 20 gerechnet", "8 * 20"), (56, None, "nur 8 · 7 gerechnet", "8 * 7")]), regel=AM)
neu(T, "verteilen", "fehler_detektiv", FD(
    "Nina berechnet 6 · 43 mit dem Verteilungsgesetz.",
    [("43 = 40 + 3, also ist 6 · 43 = 6 · (40 + 3).", 6 * 43 == 6 * (40 + 3), True),
     ("Verteilt: 6 · (40 + 3) = 6 · 40 + 3.", 6 * (40 + 3) == 6 * 40 + 3, True),
     ("6 · 40 + 3 = 240 + 3 = 243.", 6 * 40 + 3 == 243, True)],
    "Wird beim Verteilen jeder Summand in der Klammer mit 6 malgenommen?",
    "Beide Summanden müssen mit 6 malgenommen werden: 6 · (40 + 3) = 6 · 40 + 6 · 3 = 240 + 18 = 258. Der erste Fehler steht in Zeile 2."), regel=AM)

# ───────── kopfrechnen ─────────
neu(T, "kopfrechnen", "umkehren", Z(
    "Welche Zahl ergibt mit 99 malgenommen 1 188? Tipp: 99 ist fast 100.",
    12, "1188 / 99", "1188 / 11 / 9", "Mit 100 malzunehmen ist leicht. Wie weit ist 1 188 von einem Vielfachen von 100 entfernt?",
    "1 188 liegt knapp unter 1 200. 99 · 12 = 100 · 12 − 12 = 1 200 − 12 = 1 188. Die gesuchte Zahl ist 12.",
    [(1089, None, "99 abgezogen statt geteilt", "1188 - 99"), (1287, None, "99 addiert statt geteilt", "1188 + 99"), (11, None, "mit 1 100 statt 1 200 verglichen", "1100 / 100")]), g="umkehr", regel=GR)
neu(T, "kopfrechnen", "anwenden", Z(
    "Ein Hausmeister kauft 199 Schrauben. Jede Schraube kostet 6 Cent. Wie viele Cent kosten alle Schrauben zusammen? Rechne im Kopf mit 200 Schrauben und korrigiere.",
    1194, "200 * 6 - 6", "199 * 6", "200 Schrauben sind eine Schraube zu viel. Was muss man dann vom Preis abziehen?",
    "200 · 6 = 1 200 Cent. Eine Schraube weniger: 1 200 − 6 = 1 194 Cent.",
    [(1206, None, "die Korrektur in die falsche Richtung gerechnet: 1 200 + 6", "200 * 6 + 6"), (1200, None, "nur mit 200 Schrauben gerechnet", "200 * 6"), (1188, None, "zwei Schrauben abgezogen: 1 200 − 12", "200 * 6 - 12")], "Cent"), g="transfer", regel=TA)

# ───────── mal_ganz ─────────
neu(T, "mal_ganz", "anwenden", Z(
    "Ein Taucher sinkt jede Minute um 4 Meter. Um wie viele Meter hat sich seine Höhe nach 6 Minuten verändert? Gib die Veränderung mit Vorzeichen an (sinken ist negativ).",
    -24, "6 * (-4)", "-(6 * 4)", "Eine Minute bedeutet −4 Meter. Wie oft geschieht das?",
    "Jede Minute ändert sich die Höhe um −4 m. Nach 6 Minuten: 6 · (−4) = −24 m.",
    [(24, None, "das Vorzeichen vergessen (die Veränderung ist negativ)", "6 * 4"), (-10, None, "addiert statt malgenommen: −4 − 6", "-4 - 6"), (2, None, "6 und −4 addiert", "6 + (-4)")], "m"), regel="rr.vorzeichen")
neu(T, "mal_ganz", "zwei_wege", Z(
    "Berechne (−2) · (−5) · (−3) · 4 auf zwei Wegen. Weg A: Rechne von links nach rechts Schritt für Schritt. Weg B: Zähle die negativen Faktoren, bestimme so das Vorzeichen und multipliziere dann die Beträge.",
    -120, "(-2) * (-5) * (-3) * 4", "-(2 * 5 * 3 * 4)", "Bei Weg B: Ein negativer Faktor kehrt das Vorzeichen um. Wie oft passiert das?",
    "Weg A: (−2) · (−5) = 10, 10 · (−3) = −30, −30 · 4 = −120. Weg B: Drei Faktoren sind negativ, das Ergebnis ist negativ. 2 · 5 · 3 · 4 = 120, also −120.",
    [(120, None, "das Vorzeichen falsch: bei drei negativen Faktoren wurde ein positives Ergebnis angenommen", "2 * 5 * 3 * 4"), (-30, None, "den letzten Faktor 4 vergessen", "(-2) * (-5) * (-3)"), (-6, None, "addiert statt multipliziert: −2 − 5 − 3 + 4", "-2 - 5 - 3 + 4")]), g="verknuepfen", regel="rr.vorzeichen")

# ───────── geteilt_ganz ─────────
neu(T, "geteilt_ganz", "zwei_wege", Z(
    "Berechne (−84) : (−4) : 3 auf zwei Wegen. Weg A: Rechne von links nach rechts. Weg B: Rechne zuerst (−4) · 3 und teile dann −84 durch das Ergebnis.",
    7, "(-84) / (-4) / 3", "(-84) / ((-4) * 3)", "Bei Weg B ist der Teiler das Produkt aus (−4) und 3.",
    "Weg A: (−84) : (−4) = 21, 21 : 3 = 7. Weg B: (−4) · 3 = −12, (−84) : (−12) = 7.",
    [(21, None, "nur die erste Division ausgerechnet", "(-84) / (-4)"), (-7, None, "das Vorzeichen falsch: minus durch minus ergibt plus", "(-84) / 4 / 3 * (-1) * (-1)")]), regel="rr.vorzeichen")
neu(T, "geteilt_ganz", "umkehren", Z(
    "Durch welche ganze Zahl muss man −72 teilen, um 9 zu erhalten?",
    -8, "-72 / 9", "-(72 / 9)", "Das Ergebnis 9 ist positiv, die Zahl −72 ist negativ. Welches Vorzeichen muss der Teiler haben?",
    "Aus −72 : □ = 9 folgt □ = (−72) : 9 = −8. Probe: (−72) : (−8) = 9.",
    [(8, None, "das Vorzeichen vergessen: 72 : 9", "72 / 9"), (-648, None, "multipliziert statt geteilt", "-72 * 9"), (-81, None, "9 von −72 abgezogen", "-72 - 9")]), g="rueckwaerts", regel="rr.vorzeichen")

# ───────── umkehraufgabe_mal ─────────
neu(T, "umkehraufgabe_mal", "zwei_wege", Z(
    "Welche Zahl ergibt mit 12 malgenommen −156? Weg A: Teile −156 durch 12. Weg B: Zerlege −156 in −120 und −36 und überlege, womit man 12 jeweils malnehmen muss.",
    -13, "-156 / 12", "-10 - 3", "Bei Weg B: Womit musst du 12 malnehmen, um −120 zu erhalten? Und für −36?",
    "Weg A: −156 : 12 = −13. Weg B: 12 · (−10) = −120, 12 · (−3) = −36. Zusammen 12 · (−13) = −156.",
    [(13, None, "das Vorzeichen vergessen", "156 / 12"), (-1872, None, "multipliziert statt geteilt", "-156 * 12"), (-144, None, "12 addiert statt geteilt", "-156 + 12")]), regel=GR)
neu(T, "umkehraufgabe_mal", "fehler_detektiv", FD(
    "Kim löst □ · (−5) = 40.",
    [("Die Umkehraufgabe heißt □ = 40 · (−5).", (40 * -5) * -5 == 40, True),
     ("Also ist □ = −200.", 40 * -5 == -200, True),
     ("Die gesuchte Zahl ist −200.", True, True)],
    "Welche Rechenart macht das Malnehmen mit (−5) rückgängig?",
    "Malnehmen mit (−5) macht man durch Teilen durch (−5) rückgängig: □ = 40 : (−5) = −8. Probe: (−8) · (−5) = 40. Der erste Fehler steht in Zeile 1."), regel=GR)

# ───────── ueberschlag ─────────
neu(T, "ueberschlag", "umkehren", Z(
    "Bei einem Überschlag wird der erste Faktor 78 auf Zehner gerundet. Der Überschlag ergibt 6 000. Welche Zahl wurde für den zweiten Faktor eingesetzt?",
    75, "6000 / 80", "6000 / 8 / 10", "Auf Zehner gerundet wird 78 zu einer glatten Zahl. Was musst du mit ihr malnehmen, um 6 000 zu erhalten?",
    "78 wird zu 80 gerundet. 80 · □ = 6 000, also □ = 6 000 : 80 = 75.",
    [(480000, None, "malgenommen statt geteilt", "6000 * 80"), (5922, None, "78 von 6 000 abgezogen", "6000 - 78")]), g="umkehr", regel=RF)
neu(T, "ueberschlag", "anwenden", W(
    "Maja rechnet 487 · 62. Ihr Taschenrechner zeigt eine Zahl an. Maja überschlägt mit 500 · 60. Welches Ergebnis des Taschenrechners passt zu ihrem Überschlag?",
    "30 194",
    [("3 019", "Eine Stelle zu klein: Ein Überschlag nahe 30 000 passt nicht zu 3 019."), ("301 940", "Eine Stelle zu groß: Ein Überschlag nahe 30 000 passt nicht zu 301 940.")],
    "Rechne 500 · 60 aus. Welche Zahl liegt in dieser Größenordnung?",
    "500 · 60 = 30 000. Nur 30 194 liegt in der Nähe. Genau gerechnet: 487 · 62 = 30 194. Wäre 3 019 oder 301 940 herausgekommen, hätte sich Maja verrechnet.",
    lambda: 487 * 62 == 30194 and 500 * 60 == 30000), g="pruefung", regel=RF)

# ───────── schriftlich ─────────
neu(T, "schriftlich", "zwei_wege", Z(
    "Berechne 728 : 14. Weg A: Teile schriftlich. Weg B: Zerlege 728 in 700 + 28 und teile beide Teile einzeln durch 14.",
    52, "728 / 14", "700 / 14 + 28 / 14", "Bei Weg B: Wie oft passt 14 in 700? Wie oft in 28?",
    "Weg A: 728 : 14 = 52. Weg B: 700 : 14 = 50 und 28 : 14 = 2, zusammen 52. Probe: 52 · 14 = 728.",
    [(50, None, "nur 700 : 14 gerechnet", "700 / 14"), (2, None, "nur 28 : 14 gerechnet", "28 / 14")]), regel=GR)
neu(T, "schriftlich", "fehler_detektiv", FD(
    "Tom rechnet schriftlich 346 · 27 und zerlegt: 27 = 20 + 7.",
    [("346 · 20 = 692.", 346 * 20 == 692, True),
     ("346 · 7 = 2 422.", 346 * 7 == 2422, True),
     ("692 + 2 422 = 3 114.", 692 + 2422 == 3114, True)],
    "Wie viele Nullen hat das Ergebnis von 346 · 20 mindestens am Ende?",
    "346 · 20 = 6 920 (346 · 2 = 692, dann eine Null anhängen). Richtig: 6 920 + 2 422 = 9 342. Der erste Fehler steht in Zeile 1."), regel=AM)

# ───────── schriftlich_geteilt ─────────
neu(T, "schriftlich_geteilt", "anwenden", Z(
    "275 Kinder sollen in Gruppen zu je 12 Kindern eingeteilt werden. Es werden so viele volle Gruppen gebildet wie möglich. Wie viele Kinder bleiben übrig?",
    11, "275 % 12", "275 - 22 * 12", "Teile schriftlich. Was bleibt am Ende als Rest?",
    "275 : 12 = 22 Rest 11, denn 22 · 12 = 264 und 275 − 264 = 11. Es bleiben 11 Kinder übrig.",
    [(22, None, "die Zahl der Gruppen statt des Rests", "275 // 12"), (23, None, "eine Gruppe mehr gezählt (aufgerundet)", "275 // 12 + 1")], "Kinder"), regel=GR)
neu(T, "schriftlich_geteilt", "zwei_wege", Z(
    "Wie groß ist der Rest bei 3 128 : 24? Weg A: Teile schriftlich. Weg B: Ziehe von 3 128 zuerst 24 · 100 ab, dann so oft 24, wie es geht.",
    8, "3128 % 24", "3128 - 2400 - 30 * 24", "Bei Weg B: Nach 24 · 100 bleibt eine Zahl übrig. Wie viele 24er passen noch hinein?",
    "Weg A: 3 128 : 24 = 130 Rest 8. Weg B: 3 128 − 2 400 = 728. 728 − 30 · 24 = 728 − 720 = 8.",
    [(130, None, "den Quotienten statt des Rests genannt", "3128 // 24"), (128, None, "3 128 − 3 000 gerechnet", "3128 - 3000")]), g="verknuepfen", regel=GR)

# ───────── sach ─────────
neu(T, "sach", "zwei_wege", Z(
    "Eine Klasse mit 24 Kindern kauft ein Geschenk für 85 €. Jedes Kind gibt 3 €, die Schule gibt 20 € dazu. Wie viel Geld bleibt übrig? Weg A: Rechne aus, wie viel Geld insgesamt zusammenkommt, und ziehe den Preis ab. Weg B: Rechne zuerst aus, wie viel die Kinder zahlen müssten, wenn die Schule 20 € gibt, und vergleiche mit dem, was sie zahlen.",
    7, "24 * 3 + 20 - 85", "24 * 3 - (85 - 20)", "Bei Weg B: Wie viel muss von den Kindern kommen, wenn die Schule schon 20 € gibt?",
    "Weg A: 24 · 3 = 72, 72 + 20 = 92, 92 − 85 = 7. Weg B: 85 − 20 = 65 müssen die Kinder zahlen, sie zahlen 72. 72 − 65 = 7. Es bleiben 7 € übrig.",
    [(65, None, "nur den Preis minus den Zuschuss der Schule genannt", "85 - 20"), (92, None, "den Preis nicht abgezogen", "24 * 3 + 20"), (-13, None, "den Zuschuss der Schule nicht beachtet: 72 − 85", "24 * 3 - 85")], "€"), regel=RF)
neu(T, "sach", "fehler_detektiv", FD(
    "Im Zug sitzen 245 Fahrgäste. In A steigen 87 aus und 64 ein. In B steigen 120 aus. Pia berechnet, wie viele noch im Zug sitzen.",
    [("245 − 87 = 168.", 245 - 87 == 168, True),
     ("168 + 64 = 232.", 168 + 64 == 232, True),
     ("232 − 120 = 112.", 232 - 120 == 112, True)],
    "Rechne 245 − 87 nach: Stimmt die Zehnerziffer?",
    "245 − 87 = 158. Weiter: 158 + 64 = 222, 222 − 120 = 102. Es sitzen 102 Fahrgäste im Zug. Der erste Fehler steht in Zeile 1."), regel=TA)
