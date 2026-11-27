"""rollend-5 · zahlen.rechengesetze (14 Lernkarten, 42 Aufgaben)."""
import ast
from k5basis import *      # noqa: F401,F403

TH = "zahlen.rechengesetze"
RF, TA, TS, AM, VZ, GR, BN, SW = "rr.reihenfolge", "id.algebra.term", "rr.tauschen", "rr.ausmultiplizieren", "rr.vorzeichen", "rr.gegenrechnung", "id.zahlen.buendeln", "rr.stellenwert"
oberste = lambda s: type(ast.parse(s, mode="eval").body.op)

# ── punkt_strich ──
neu(TH, "punkt_strich", "fehler_detektiv", "fehler", FDZ(
    "Kim rechnet 4 + 6 · 3 − 2.",
    [("Ich rechne von links nach rechts: 4 + 6 = 10.", 4 + 6 * 3 - 2 == (4 + 6) * 3 - 2), ("Dann 10 · 3 = 30.", 10 * 3 == 30), ("Dann 30 − 2 = 28.", 30 - 2 == 28)],
    "Welche Rechenart hat Vorrang?", "Punkt vor Strich: Zuerst 6 · 3 = 18. Dann 4 + 18 = 22 und 22 − 2 = 20."), RF)
neu(TH, "punkt_strich", "verfahren_waehlen", "mehrschritt", W(
    "Du rechnest 36 − 12 : 4 + 5. Welche Reihenfolge der Schritte ist richtig?",
    "12 : 4 = 3; dann 36 − 3 = 33; dann 33 + 5 = 38",
    [("36 − 12 = 24; dann 24 : 4 = 6; dann 6 + 5 = 11", "stur von links nach rechts"), ("12 : 4 = 3; dann 3 + 5 = 8; dann 36 − 8 = 28", "Plus vor Minus gerechnet"), ("4 + 5 = 9; dann 12 : 9; dann 36 − das Ergebnis", "die Rechnung falsch zusammengesetzt")],
    "Welches Zeichen hat Vorrang: Geteilt oder Minus?", "Zuerst die Punktrechnung: 12 : 4 = 3. Dann von links: 36 − 3 = 33, 33 + 5 = 38.",
    36 - 12 / 4 + 5 == 38 and (36 - 12) / 4 + 5 != 38 and 36 - (3 + 5) != 38), RF)
neu(TH, "punkt_strich", "anwenden", "einkleidung", Z(
    "Auf einem Flohmarkt verkaufst du 6 Bücher zu je 3 € und 4 Spiele zu je 5 €. Du musst 8 € Standgebühr zahlen. Wie viel Euro bleiben dir?",
    "6*3+4*5-8", "18+20-8", "Rechne erst die Einnahmen aus, dann die Gebühr.", "Bücher: 6 · 3 = 18. Spiele: 4 · 5 = 20. Einnahmen: 38. Davon 8 abziehen: 30 €.",
    [(38, None, "Standgebühr vergessen"), (46, None, "Standgebühr addiert")], einheit="€"), RF)

# ── klammern ──
neu(TH, "klammern", "lueckenweg", "direkt", L(
    "Du rechnest (14 − 6) · 3 + 5. Die Klammer zuerst: 14 − 6 = ①. Dann mal 3: ① · 3 = ②. Zuletzt plus 5: ② + 5 = ③.",
    ["14-6", "(14-6)*3", "(14-6)*3+5"], ["8", "24", "29"], "Erst die Klammer, dann Punkt, dann Strich.", "14 − 6 = 8; 8 · 3 = 24; 24 + 5 = 29.",
    {0: [(20, None, "14 + 6 gerechnet")], 2: [(19, None, "5 abgezogen statt addiert: 24 − 5")]}), RF)
neu(TH, "klammern", "umkehren", "umkehr", Z(
    "Welche Zahl muss an der Stelle des Fragezeichens stehen? 3 · (? + 4) = 27",
    "27//3-4", "9-4", "Mach zuerst die Umkehrung des Malnehmens: Was steht in der Klammer?", "3 · Klammer = 27, also Klammer = 27 : 3 = 9. Dann ? + 4 = 9, also ? = 5.",
    [(9, None, "nur die Klammer berechnet"), (23, None, "27 − 4 gerechnet")]), RF)
neu(TH, "klammern", "anwenden", "einkleidung", Z(
    "Eine Klasse mit 24 Kindern besucht den Zoo. Jedes Kind zahlt 4 € Eintritt und 3 € für die Führung. Die Schule übernimmt davon 50 €. Wie viel Euro zahlen die Kinder zusammen?",
    "24*(4+3)-50", "24*4+24*3-50", "Was zahlt ein Kind insgesamt? Das steht in einer Klammer.", "Ein Kind: 4 + 3 = 7 €. 24 Kinder: 24 · 7 = 168 €. Abzüglich 50 €: 118 €.",
    [(49, None, "Klammer vergessen: 24 · 4 + 3 − 50"), (168, None, "die 50 € vergessen")], einheit="€"), RF)

# ── termaufbau ──
neu(TH, "termaufbau", "fehler_detektiv", "fehler", FDZ(
    "Kim benennt den Term 3 · (5 + 2).",
    [("Ich rechne zuerst die Klammer: 5 + 2 = 7.", 5 + 2 == 7), ("Dann bleibt 3 · 7 übrig.", True), ("Die letzte Rechnung ist das Plus aus der Klammer.", oberste("3*(5+2)") is ast.Add), ("Darum ist der Term eine Summe.", True)],
    "Nach welcher Rechnung richtet sich der Name des Terms?", "Der Name richtet sich nach der letzten Rechnung. Das ist das Malnehmen mit 3. Der Term ist ein Produkt."), TA)
neu(TH, "termaufbau", "bruecke", "darstellung", W(
    "Welcher Term passt zum Text: „Vom Fünffachen von 4 werden 3 abgezogen“?",
    "5 · 4 − 3", [("5 · (4 − 3)", "Klammer gesetzt, die im Text nicht vorkommt"), ("5 − 4 · 3", "Zahlen in falscher Reihenfolge"), ("(5 + 4) · 3", "Mal und Plus verwechselt")],
    "Das Fünffache von 4 ist eine Rechnung für sich.", "Das Fünffache von 4 ist 5 · 4. Davon werden 3 abgezogen: 5 · 4 − 3 = 17.",
    5 * 4 - 3 == 17 and 5 * (4 - 3) != 17 and 5 - 4 * 3 != 17 and (5 + 4) * 3 != 17), TA)
neu(TH, "termaufbau", "anwenden", "einkleidung", Z(
    "Für ein Fest kaufst du 4 Packungen Saft zu je 3 € und 2 Kuchen zu je 6 €. Du bezahlst mit einem 50-€-Schein. Wie viel Euro Rückgeld bekommst du?",
    "50-(4*3+2*6)", "50-24", "Stelle den Term auf: 50 minus alles, was du kaufst.", "Saft: 4 · 3 = 12 €. Kuchen: 2 · 6 = 12 €. Zusammen 24 €. 50 − 24 = 26 €.",
    [(38, None, "nur den Saft abgezogen"), (74, None, "alle Ausgaben zu 50 addiert")], einheit="€"), TA)

# ── vorteil ──
neu(TH, "vorteil", "lueckenweg", "direkt", L(
    "Du rechnest 25 · 17 · 4 geschickt. Beim Malnehmen darfst du die Reihenfolge tauschen. Stelle das Paar nach vorn, das zusammen eine glatte Zahl ergibt: Das Paar ergibt ①. Die dritte Zahl ist 17: ① · 17 = ②.",
    ["25*4", "25*4*17"], ["100", "1700"], "Bei Mal darfst du tauschen. Suche ein glattes Paar.", "25 · 4 = 100. 100 · 17 = 1 700.",
    {0: [(425, None, "nicht das glatte Paar gewählt, sondern 25 · 17")], 1: [(170, None, "eine Null verloren")]}), TS)
neu(TH, "vorteil", "zwei_wege", "mehrschritt", Z(
    "Berechne 37 + 48 + 63 + 52. Weg A rechnet von links nach rechts. Weg B fasst 37 + 63 und 48 + 52 zusammen. Wie groß ist die Summe?",
    "37+48+63+52", "100+100", "Beide Wege geben dieselbe Zahl. Welcher geht schneller?", "Weg A: 37 + 48 = 85, 85 + 63 = 148, 148 + 52 = 200. Weg B: 100 + 100 = 200.",
    [(100, None, "nur ein Paar gerechnet")]), TS)
neu(TH, "vorteil", "anwenden", "einkleidung", Z(
    "Eine Bäckerei liefert an 13 Schulen je 4 Kisten mit je 25 Brötchen. Wie viele Brötchen sind das insgesamt?",
    "13*4*25", "13*100", "25 und 4 passen gut zusammen.", "4 · 25 = 100 Brötchen je Schule. 13 · 100 = 1 300.",
    [(130, None, "eine Null verloren"), (42, None, "alles addiert")]), TS)

# ── differenz_summe ──
neu(TH, "differenz_summe", "fehler_detektiv", "fehler", FDZ(
    "Kim rechnet 52 − 17 + 8 geschickt.",
    [("Das Minus gehört zur 17, das Plus gehört zur 8.", True), ("Ich tausche die Plätze von 17 und 8. Die Zeichen lasse ich an ihrem Platz stehen: 52 − 8 + 17.", 52 - 17 + 8 == 52 - 8 + 17), ("52 − 8 = 44 und 44 + 17 = 61.", 52 - 8 + 17 == 61)],
    "Was passiert mit dem Zeichen, wenn eine Zahl den Platz wechselt?", "Beim Tauschen nimmt jede Zahl ihr Zeichen mit: 52 + 8 − 17 = 60 − 17 = 43."), TS)
neu(TH, "differenz_summe", "zwei_wege", "mehrschritt", Z(
    "Berechne 90 − 38 + 18. Weg A rechnet von links nach rechts. Weg B tauscht zu 90 + 18 − 38. Wie groß ist das Ergebnis?",
    "90-38+18", "108-38", "Die Zahl nimmt ihr Zeichen mit, wenn du tauschst.", "Weg A: 90 − 38 = 52, 52 + 18 = 70. Weg B: 90 + 18 = 108, 108 − 38 = 70.",
    [(34, None, "Zeichen der 18 gewechselt"), (110, None, "die Zeichen von 38 und 18 vertauscht")]), TS)
neu(TH, "differenz_summe", "umkehren", "umkehr", Z(
    "Zu 37 wird eine Zahl addiert. Danach werden 15 abgezogen. Das Ergebnis ist 60. Welche Zahl wurde addiert?",
    "60+15-37", "75-37", "Beginne beim Ergebnis und kehre die Schritte um, den letzten zuerst.", "Rückwärts: 60 + 15 = 75. Dann 75 − 37 = 38. Probe: 37 + 38 − 15 = 60.",
    [(23, None, "nur 60 − 37 gerechnet"), (8, None, "die 15 abgezogen statt addiert")]), TS)

# ── verteilen ──
neu(TH, "verteilen", "lueckenweg", "direkt", L(
    "Du rechnest 6 · 48 geschickt als 6 · (50 − 2). Es ist 6 · 50 = ①. Es ist 6 · 2 = ②. Ergebnis: ① − ② = ③.",
    ["6*50", "6*2", "6*50-6*2"], ["300", "12", "288"], "Die 6 wird mit jedem Teil in der Klammer malgenommen.", "6 · 50 = 300, 6 · 2 = 12, 300 − 12 = 288.",
    {1: [(2, None, "die 6 nur mit dem ersten Teil malgenommen")], 2: [(312, None, "300 + 12 gerechnet")]}), AM)
neu(TH, "verteilen", "bruecke", "darstellung", W(
    "Die Tabelle beschreibt zwei Teile eines Rechtecks, die nebeneinander liegen. Welcher Term gibt die ganze Fläche?",
    "7 · 40 + 7 · 3", [("7 · 40 + 3", "die Breite nur beim ersten Teil benutzt"), ("7 + 40 · 3", "Längen und Breiten gemischt"), ("7 · 40 · 3", "alles malgenommen")],
    "Fläche jedes Teils: Länge mal Breite. Dann zusammenzählen.", "Links: 40 · 7, rechts: 3 · 7. Zusammen 7 · 40 + 7 · 3 = 280 + 21 = 301 m². Das ist auch 7 · 43.",
    7 * 40 + 7 * 3 == 7 * 43 == 301 and 7 * 40 + 3 != 301 and 7 + 40 * 3 != 301 and 7 * 40 * 3 != 301,
    grafik=TAB(["Teil", "Länge", "Breite"], ["links", "40 m", "7 m"], ["rechts", "3 m", "7 m"])), AM)
neu(TH, "verteilen", "anwenden", "einkleidung", Z(
    "Ein Gärtner pflanzt 9 Reihen mit je 98 Tulpen. Wie viele Tulpen sind das insgesamt?",
    "9*(100-2)", "9*98", "98 ist fast 100. Rechne mit 100 − 2.", "9 · 100 = 900. 9 · 2 = 18. 900 − 18 = 882 Tulpen.",
    [(898, None, "die 9 nur mit der 100 malgenommen"), (918, None, "18 addiert statt abgezogen")]), AM)

# ── kopfrechnen ──
neu(TH, "kopfrechnen", "fehler_detektiv", "fehler", FDZ(
    "Kim rechnet 7 · 38 im Kopf.",
    [("Ich zerlege 38 = 40 − 2.", 38 == 40 - 2), ("7 · 40 = 280.", 7 * 40 == 280), ("7 · 2 = 14.", 7 * 2 == 14), ("Also 7 · 38 = 280 + 14 = 294.", 7 * 38 == 294)],
    "Ist 38 größer oder kleiner als 40? Was heißt das für das Ergebnis?", "38 ist kleiner als 40, also muss 14 abgezogen werden: 280 − 14 = 266."), AM)
neu(TH, "kopfrechnen", "zwei_wege", "mehrschritt", Z(
    "Berechne 15 · 18. Weg A: 15 · 20 − 15 · 2. Weg B: 10 · 18 + 5 · 18. Wie groß ist das Ergebnis?",
    "15*18", "15*20-15*2", "Beide Wege führen zum gleichen Ergebnis.", "Weg A: 300 − 30 = 270. Weg B: 180 + 90 = 270.",
    [(330, None, "30 addiert statt abgezogen"), (180, None, "nur 10 · 18 gerechnet")]), AM)
neu(TH, "kopfrechnen", "anwenden", "einkleidung", Z(
    "Ein Zug hat 12 Wagen mit je 48 Sitzplätzen. Wie viele Sitzplätze sind das? Rechne geschickt im Kopf.",
    "12*48", "10*48+2*48", "Zerlege die 12 in 10 + 2.", "10 · 48 = 480, 2 · 48 = 96. 480 + 96 = 576 Plätze.",
    [(528, None, "nur 11 Wagen gerechnet"), (96, None, "nur den zweiten Teil genommen")]), AM)

# ── mal_ganz ──
neu(TH, "mal_ganz", "lueckenweg", "direkt", L(
    "Du rechnest (−6) · 7. Ohne Vorzeichen: 6 · 7 = ①. Die Vorzeichen sind verschieden, also hat das Ergebnis den Betrag ① mit dem passenden Vorzeichen: ②. Bei (−6) · (−7) sind die Vorzeichen gleich. Dieses Ergebnis ist um ③ größer als ②.",
    ["6*7", "(-6)*7", "(-6)*(-7)-(-6)*7"], ["42", "-42", "84"], "Verschiedene Vorzeichen: minus. Gleiche Vorzeichen: plus.", "6 · 7 = 42. (−6) · 7 = −42. (−6) · (−7) = 42. 42 − (−42) = 84.",
    {1: [(42, "fb.vorzeichen.falsches_zeichen", "Vorzeichen vergessen")], 2: [(0, "fb.vorzeichen.falsches_zeichen", "zwei Minus als Minus gerechnet: beide Ergebnisse gleich")]}), VZ)
neu(TH, "mal_ganz", "umkehren", "umkehr", Z(
    "Welche Zahl mal (−5) ergibt 40?",
    "40//(-5)", "-8", "Rechne mit der Umkehraufgabe. Achte auf das Vorzeichen.", "40 : (−5) = −8. Probe: (−8) · (−5) = 40.",
    [(8, "fb.vorzeichen.falsches_zeichen", "Vorzeichen vergessen"), (-200, None, "malgenommen statt geteilt")]), VZ)
neu(TH, "mal_ganz", "bruecke", "darstellung", W(
    "Dein Kontostand sinkt an 5 Tagen um je 12 €. Welche Rechnung gibt die Änderung insgesamt?",
    "5 · (−12)", [("5 + (−12)", "addiert statt malgenommen"), ("(−5) · (−12)", "auch die Tage negativ gemacht"), ("(−12) : 5", "geteilt statt malgenommen")],
    "5-mal dieselbe Änderung heißt: malnehmen. Sinken heißt: minus.", "Jeden Tag −12 €, an 5 Tagen: 5 · (−12) = −60 €.",
    5 * -12 == -60 and 5 + -12 != -60 and (-5) * (-12) != -60 and (-12) / 5 != -60 and len({5 + -12, (-5) * (-12), (-12) / 5}) == 3), VZ)

# ── geteilt_ganz ──
neu(TH, "geteilt_ganz", "fehler_detektiv", "fehler", FDZ(
    "Kim rechnet (−72) : (−9).",
    [("Beide Zahlen sind negativ.", True), ("Zwei Minuszeichen ergeben beim Teilen wieder ein Minus.", (-72) / (-9) < 0), ("Also ist (−72) : (−9) = −8.", True)],
    "Was ergeben gleiche Vorzeichen beim Teilen: Plus oder Minus?", "Gleiche Vorzeichen ergeben Plus. (−72) : (−9) = 8. Probe: 8 · (−9) = −72."), VZ)
neu(TH, "geteilt_ganz", "umkehren", "umkehr", Z(
    "Eine Zahl geteilt durch (−6) ergibt 7. Welche Zahl ist es?",
    "7*(-6)", "-42", "Kehre das Teilen um. Beachte das Vorzeichen.", "Zahl : (−6) = 7, also Zahl = 7 · (−6) = −42. Probe: (−42) : (−6) = 7.",
    [(42, "fb.vorzeichen.falsches_zeichen", "Vorzeichen vergessen")]), VZ)
neu(TH, "geteilt_ganz", "anwenden", "einkleidung", Z(
    "Ein Taucher sinkt in 8 Minuten gleichmäßig von 0 m auf −96 m. Wie ändert sich seine Höhe in jeder Minute (in Meter, mit Vorzeichen)?",
    "(-96)//8", "-12", "Teile die gesamte Änderung durch die Zahl der Minuten.", "−96 m : 8 = −12 m. Er sinkt jede Minute um 12 m.",
    [(12, "fb.vorzeichen.falsches_zeichen", "Vorzeichen vergessen"), (-768, None, "malgenommen statt geteilt")], einheit="m"), VZ)

# ── umkehraufgabe_mal ──
neu(TH, "umkehraufgabe_mal", "lueckenweg", "direkt", L(
    "Löse 6 · x = −84. Die Umkehraufgabe zu Mal ist Geteilt: x = (−84) : 6 = ①. Nun sei y : 5 = ①. Die Umkehraufgabe zu Geteilt ist Mal: y = ① · 5 = ②.",
    ["(-84)//6", "(-84)//6*5"], ["-14", "-70"], "Mal kehrst du mit Geteilt um, Geteilt mit Mal.", "(−84) : 6 = −14. (−14) · 5 = −70.",
    {0: [(14, "fb.vorzeichen.falsches_zeichen", "Vorzeichen vergessen")], 1: [(70, "fb.vorzeichen.falsches_zeichen", "mit 14 statt −14 weitergerechnet")]}), GR)
neu(TH, "umkehraufgabe_mal", "verfahren_waehlen", "erkennen", W(
    "Du sollst x : 4 = −9 lösen. Welcher Weg ist richtig?",
    "x = (−9) · 4 = −36", [("x = (−9) : 4", "das Teilen nicht umgekehrt"), ("x = 4 : (−9)", "Zahlen vertauscht"), ("x = (−9) + 4 = −5", "Plus statt Mal")],
    "Welche Rechnung macht das Teilen durch 4 rückgängig?", "Teilen durch 4 kehrst du mit Malnehmen um: x = (−9) · 4 = −36. Probe: (−36) : 4 = −9.",
    -36 / 4 == -9 and -9 / 4 != -9 and 4 / -9 != -9 and -9 + 4 != -36), GR)
neu(TH, "umkehraufgabe_mal", "anwenden", "einkleidung", Z(
    "Ein Konto verliert jeden Monat denselben Betrag. Die Änderung nach 7 Monaten ist −133 €. Wie ändert sich das Konto pro Monat (in Euro, mit Vorzeichen)?",
    "(-133)//7", "-19", "7 gleiche Änderungen ergeben −133. Was machst du, um eine zu finden?", "−133 € : 7 = −19 €. Probe: 7 · (−19) = −133.",
    [(19, "fb.vorzeichen.falsches_zeichen", "Vorzeichen vergessen"), (-931, None, "malgenommen statt geteilt")], einheit="€"), GR)

# ── ueberschlag ──
neu(TH, "ueberschlag", "fehler_detektiv", "fehler", FDZ(
    "Kim überschlägt 4 987 · 21. Das genaue Ergebnis ist 104 727.",
    [("Ich runde 4 987 auf Tausender: 4 000.", round(4987, -3) == 4000), ("Ich runde 21 auf Zehner: 20.", round(21, -1) == 20), ("Überschlag: 4 000 · 20 = 80 000.", 4000 * 20 == 80000)],
    "Auf welche Zahl rundest du 4 987 auf Tausender? Schau auf die Hunderterziffer.", "4 987 rundet man auf 5 000, denn die Hunderterziffer 9 ist 5 oder mehr. Überschlag: 5 000 · 20 = 100 000. Das passt zum genauen Ergebnis."), BN)
neu(TH, "ueberschlag", "zwei_wege", "mehrschritt", Z(
    "Überschlage 612 + 349 + 98. Weg A rundet auf Hunderter und addiert. Weg B rundet auf Zehner und addiert. Um wie viel ist der Überschlag von Weg B größer als der von Weg A?",
    "(610+350+100)-(600+300+100)", "60", "Runde in jedem Weg alle drei Zahlen, dann addiere.", "Weg A: 600 + 300 + 100 = 1 000. Weg B: 610 + 350 + 100 = 1 060. Unterschied: 60.",
    [(0, None, "beide Überschläge als gleich angenommen")]), BN)
neu(TH, "ueberschlag", "anwenden", "einkleidung", Z(
    "Eine Schule bestellt 28 Pakete Papier mit je 312 Blatt. Sie braucht 10 000 Blatt. Wie viele Blatt fehlen noch? (Überschlag zur Kontrolle: 30 · 300 ist etwa 9 000.)",
    "10000-28*312", "10000-8736", "Rechne die Zahl der Blätter genau aus. Dein Überschlag sagt etwa 1 000.", "28 · 312 = 8 736. 10 000 − 8 736 = 1 264 Blatt fehlen.",
    [(1600, None, "nur 28 · 300 = 8 400 gerechnet: Zehner und Einer von 312 vergessen"), (1000, None, "nur den Überschlag genommen")]), BN)

# ── schriftlich ──
neu(TH, "schriftlich", "lueckenweg", "direkt", L(
    "Schriftlich 123 · 45. Erst mit der Einerziffer 5: 123 · 5 = ①. Dann mit der Zehnerziffer 4: Sie steht an der Zehnerstelle, du rechnest also mit ihrem Wert. Das Teilergebnis ist ②. Beides addieren: ① + ② = ③.",
    ["123*5", "123*40", "123*5+123*40"], ["615", "4920", "5535"], "Bei der Zehnerziffer wandert das Ergebnis eine Stelle nach links.", "123 · 5 = 615. 123 · 40 = 4 920. 615 + 4 920 = 5 535.",
    {1: [(492, "fb.stellenwert.null_angehaengt", "die Null für die Zehnerstelle vergessen")], 2: [(1107, None, "mit 492 weitergerechnet")]}), SW)
neu(TH, "schriftlich", "umkehren", "umkehr", Z(
    "Eine Zahl mal 36 ergibt 1 692. Welche Zahl ist es? Rechne schriftlich geteilt.",
    "1692//36", "47", "Kehre das Malnehmen mit Teilen um.", "1 692 : 36 = 47. Probe: 47 · 36 = 1 692.",
    [(1728, None, "addiert statt geteilt")]), SW)
neu(TH, "schriftlich", "anwenden", "einkleidung", Z(
    "Ein Lastwagen bringt 24 Kisten mit je 135 Flaschen. Die Flaschen werden gleichmäßig auf 15 Tische verteilt. Wie viele Flaschen liegen auf einem Tisch?",
    "24*135//15", "3240//15", "Erst alle Flaschen ausrechnen, dann teilen.", "24 · 135 = 3 240 Flaschen. 3 240 : 15 = 216 Flaschen je Tisch.",
    [(3240, None, "nur malgenommen"), (21, None, "beim Teilen eine Ziffer vergessen")]), SW)

# ── schriftlich_geteilt ──
neu(TH, "schriftlich_geteilt", "fehler_detektiv", "fehler", FDZ(
    "Kim rechnet 7 308 : 18 schriftlich.",
    [("Die 7 ist zu klein, ich nehme 73. Es gilt 73 = 4 · 18 + 1. Ich schreibe 4 ins Ergebnis und merke den Rest 1.", 73 == 4 * 18 + 1), ("Ich hole die 0 herunter. 10 : 18 geht nicht, also schreibe ich nichts ins Ergebnis.", 7308 // 18 == 46), ("Ich hole die 8 herunter: 108 : 18 = 6.", 108 // 18 == 6), ("Ergebnis: 46.", True)],
    "Jede heruntergeholte Ziffer bringt eine Ziffer ins Ergebnis. Was schreibst du, wenn der Teiler nicht passt?", "Passt der Teiler nicht, schreibst du eine 0 ins Ergebnis. 7 308 : 18 = 406. Probe: 406 · 18 = 7 308."), SW)
neu(TH, "schriftlich_geteilt", "verfahren_waehlen", "erkennen", W(
    "Du teilst 5 472 durch 24 schriftlich. Was hilft dir dabei am meisten?",
    "Die Vielfachen von 24 aufschreiben: 24, 48, 72, 96, …",
    [("24 durch 5 472 teilen", "Teiler und Zahl vertauscht"), ("Die Ziffern von 5 472 addieren und durch 24 teilen", "Quersumme statt der Zahl benutzt"), ("Nur 5 : 24 rechnen und Nullen anhängen", "nur eine Ziffer beachtet")],
    "Welche Hilfsliste zeigt dir, wie oft 24 hineinpasst?", "Mit den Vielfachen von 24 siehst du schnell, wie oft 24 in 54, 67 und 192 passt. Ergebnis: 5 472 : 24 = 228.",
    5472 % 24 == 0 and 5472 // 24 == 228 and 24 / 5472 != 228), SW)
neu(TH, "schriftlich_geteilt", "umkehren", "umkehr", Z(
    "Eine Zahl geteilt durch 25 ergibt 328. Welche Zahl ist es?",
    "328*25", "8200", "Kehre das Teilen mit Malnehmen um. Rechne schriftlich.", "328 · 25 = 8 200. Probe: 8 200 : 25 = 328.",
    [(7872, None, "328 · 24 gerechnet")]), SW)

# ── sach ──
neu(TH, "sach", "lueckenweg", "direkt", L(
    "Ich denke mir eine Zahl. Ich addiere 12 und multipliziere die Summe mit 4. Dann erhalte ich 120. Rückwärts kehrst du zuerst den letzten Schritt um: Das ergibt ①. Danach kehrst du den ersten Schritt um: ① wird zu ②. Die gedachte Zahl ist ②.",
    ["120//4", "120//4-12"], ["30", "18"], "Beginne am Ende und kehre den letzten Schritt zuerst um.", "120 : 4 = 30. 30 − 12 = 18. Probe: (18 + 12) · 4 = 120.",
    {0: [(108, None, "erst 12 abgezogen statt durch 4 geteilt: Reihenfolge nicht umgekehrt")], 1: [(42, None, "12 addiert statt abgezogen")]}), GR)
neu(TH, "sach", "umkehren", "rueckwaerts", Z(
    "Von einem Betrag werden erst 35 € abgezogen. Der Rest wird durch 3 geteilt. Es bleiben 24 €. Wie groß war der Betrag?",
    "24*3+35", "72+35", "Beginne beim Rest und kehre den letzten Schritt zuerst um.", "Rückwärts: 24 · 3 = 72. Dann 72 + 35 = 107. Probe: (107 − 35) : 3 = 24.",
    [(59, None, "Schritte nicht umgekehrt: 24 + 35"), (27, None, "35 − 24 : 3 gerechnet")], einheit="€"), GR)
neu(TH, "sach", "bruecke", "darstellung", Z(
    "Die Tabelle zeigt drei Schritte, die nacheinander gerechnet werden. Am Ende kommt 41 heraus. Mit welcher Zahl wurde begonnen?",
    "((41+4)//5)-8", "9-8", "Lies die Tabelle von rechts nach links und kehre jeden Schritt um.", "Rückwärts: 41 + 4 = 45. 45 : 5 = 9. 9 − 8 = 1. Probe: ((1 + 8) · 5) − 4 = 41.",
    [(37, None, "Schritte nicht umgekehrt"), (9, None, "nur zwei Schritte umgekehrt")],
    grafik=TAB(["Schritt", "1", "2", "3"], ["Rechnung", "+ 8", "· 5", "− 4"])), GR)
