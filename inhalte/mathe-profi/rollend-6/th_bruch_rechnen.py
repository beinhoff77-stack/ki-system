T = "bruch.rechnen"
H4 = "Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt."
# ───────── brueche_plus_minus ─────────
neu(T, "brueche_plus_minus", "lueckenweg", L(
    "Berechne 3/4 + 5/6. Der Hauptnenner ist ①. Die Summe hat dann den Zähler ②. Als gemischte Zahl ist die Summe 1 ③/①.",
    KOMM(3), [12, 19, 7], ["12", "3 * {1} / 4 + 5 * {1} / 6", "{2} - {1}"], ["lcm(4, 6)", "19", "7"], "Suche das kleinste gemeinsame Vielfache der beiden Nenner.",
    "Hauptnenner 12: 3/4 = 9/12 und 5/6 = 10/12. Summe: 19/12. Davon ist 12/12 ein Ganzes, es bleiben 7/12. Also 1 7/12.",
    {0: [(24, None, "die Nenner malgenommen", "4 * 6")], 1: [(8, None, "Zähler und Nenner einzeln addiert: 3 + 5", "3 + 5")], 2: [(19, None, "den Zähler 19 nicht in Ganze und Rest zerlegt", "{2}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.bruchrechnen")
neu(T, "brueche_plus_minus", "zwei_wege", Z(
    "Berechne 3 1/4 − 1 5/6. Weg A: Wandle beide Zahlen in unechte Brüche um. Weg B: Rechne die Ganzen und die Brüche getrennt und entbündle bei Bedarf. Wie viele Zwölftel ist das Ergebnis?",
    17, "(13/4 - 11/6) * 12", "(3 * 12 + 3) - (1 * 12 + 10)", "Beide Wege führen zu demselben Ergebnis. Der Hauptnenner ist 12.",
    "Weg A: 3 1/4 = 13/4 = 39/12 und 1 5/6 = 11/6 = 22/12. 39/12 − 22/12 = 17/12. Weg B: 3 3/12 − 1 10/12 = 2 15/12 − 1 10/12 = 1 5/12 = 17/12.",
    [(31, None, "Ganze und Brüche getrennt gerechnet, aber den kleineren Bruch vom größeren abgezogen: (3 − 1) + (5/6 − 1/4)", "((3 - 1) + (5/6 - 1/4)) * 12"),
     (61, None, "addiert statt subtrahiert", "(3 + 1/4 + 1 + 5/6) * 12")]), g="mehrschritt", regel="rr.bruchrechnen")
neu(T, "brueche_plus_minus", "anwenden", L(
    "Ein Wasserbehälter ist zu 2/3 gefüllt. Morgens wird 1/4 des Behälters entnommen, abends wird 1/6 des Behälters aufgefüllt. Welcher Bruchteil des Behälters ist danach gefüllt?",
    "□/□", [7, 12], ["(2/3 - 1/4 + 1/6) * 12", "12"], ["7", "12"], "Bringe alle Brüche auf einen Nenner.",
    "Hauptnenner 12: 2/3 = 8/12, 1/4 = 3/12, 1/6 = 2/12. 8/12 − 3/12 + 2/12 = 7/12.",
    {0: [(3, None, "auch das Auffüllen abgezogen: 8/12 − 3/12 − 2/12", "(2/3 - 1/4 - 1/6) * 12")]}, hinweis=H4), g="transfer", regel="rr.bruchrechnen")

# ───────── dezimal_plus_minus ─────────
neu(T, "dezimal_plus_minus", "lueckenweg", L(
    "Berechne 12,4 + 3,85 − 7,6 in Hundertsteln. 12,4 sind ① Hundertstel. Die Summe 12,4 + 3,85 sind ② Hundertstel. Nach dem Abziehen von 7,6 bleiben ③ Hundertstel.",
    KOMM(3), [1240, 1625, 865], ["12.4 * 100", "{1} + 385", "{2} - 760"], ["1240", "1625", "865"], "Schreibe 12,4 als 12,40.",
    "12,4 = 1240 Hundertstel. 1240 + 385 = 1625. 7,6 = 760 Hundertstel. 1625 − 760 = 865, also 8,65.",
    {0: [(124, None, "als Zehntel statt als Hundertstel gezählt", "12.4 * 10")], 1: [(509, None, "Komma nicht beachtet: 124 + 385", "124 + 385")], 2: [(2385, None, "addiert statt abgezogen", "{2} + 760")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.plusminus")
neu(T, "dezimal_plus_minus", "anwenden", Z(
    "Beim Einkauf kosten Brot 3,49 €, Käse 12,80 € und Saft 0,99 €. Du bezahlst mit einem 20-Euro-Schein. Wie viel Euro bekommst du zurück?",
    2.72, "20 - (3.49 + 12.80 + 0.99)", "20 - 17.28", "Addiere zuerst alle drei Preise.",
    "3,49 + 12,80 + 0,99 = 17,28. 20 − 17,28 = 2,72. Du bekommst 2,72 € zurück.",
    [(17.28, None, "nur die Summe der Preise angegeben", "3.49 + 12.80 + 0.99"), (3.71, None, "den Saft vergessen", "20 - (3.49 + 12.80)")], "€"), regel="rr.plusminus")
neu(T, "dezimal_plus_minus", "umkehren", Z(
    "Denke dir eine Zahl x. Addierst du 2,75 und ziehst dann 4,6 ab, erhältst du 3,05. Welche Zahl war x?",
    4.9, "3.05 + 4.6 - 2.75", "3.05 - 2.75 + 4.6", "Rechne rückwärts: Kehre jeden Schritt um, beginnend beim letzten.",
    "Letzter Schritt „− 4,6“ umkehren: 3,05 + 4,6 = 7,65. Davor „+ 2,75“ umkehren: 7,65 − 2,75 = 4,9. Probe: 4,9 + 2,75 − 4,6 = 3,05.",
    [(10.4, None, "alle Zahlen addiert", "3.05 + 2.75 + 4.6"), (1.2, None, "die Schritte nicht umgekehrt: 3,05 − 4,6 + 2,75", "3.05 - 4.6 + 2.75")]), g="rueckwaerts", regel="rr.plusminus")

# ───────── vorzeichen ─────────
neu(T, "vorzeichen", "lueckenweg", L(
    "Berechne (−12) − (−7) + (−9). Minus eine negative Zahl ist Plus: (−12) − (−7) = ①. Dann ① + (−9) = ②. Der Abstand des Ergebnisses von der Null ist ③.",
    KOMM(3), [-5, -14, 14], ["-12 + 7", "{1} - 9", "abs({2})"], ["-5", "-14", "14"], "Minus mal Minus ergibt Plus. Beim Abziehen einer negativen Zahl gehst du nach rechts.",
    "(−12) − (−7) = −12 + 7 = −5. Dann −5 + (−9) = −14. Der Abstand von der Null ist 14.",
    {0: [(-19, None, "„minus minus“ als Minus gerechnet: −12 − 7", "-12 - 7")], 1: [(4, None, "−5 + 9 gerechnet, Vorzeichen der −9 übersehen", "{1} + 9")], 2: [(-14, None, "den Abstand mit Vorzeichen angegeben", "{2}")]}, hinweis="Je Lücke eine ganze Zahl (mit Minus, falls negativ)."), regel="rr.plusminus")
neu(T, "vorzeichen", "bruecke", Z(
    "Auf der Zahlengeraden startest du bei −4,5. Du gehst 3,2 Einheiten nach links und danach 6,8 Einheiten nach rechts. Bei welcher Zahl landest du?",
    -0.9, "-4.5 - 3.2 + 6.8", "6.8 - 7.7", "Schreibe den Weg als Rechnung auf: Links ist minus, rechts ist plus.",
    "Als Rechnung: −4,5 − 3,2 + 6,8 = −7,7 + 6,8 = −0,9. Du landest bei −0,9.",
    [(-14.5, None, "auch den Weg nach rechts als Minus gerechnet", "-4.5 - 3.2 - 6.8"), (5.5, None, "den Weg nach links als Plus gerechnet", "-4.5 + 3.2 + 6.8")]), regel="rr.plusminus")
neu(T, "vorzeichen", "fehler_detektiv", FD(
    "Tom rechnet (−3,2) − (−0,5).",
    [("(−3,2) − (−0,5) = (−3,2) + 0,5", F(-32, 10) - F(-5, 10) == F(-32, 10) + F(5, 10)), ("(−3,2) + 0,5 = −3,7", F(-32, 10) + F(5, 10) == F(-37, 10)), ("Das Ergebnis ist −3,7.", True)],
    "Rechne (−3,2) + 0,5 auf der Zahlengeraden: in welche Richtung gehst du?", "Plus 0,5 heißt 0,5 nach rechts: −3,2 + 0,5 = −2,7. In Zeile 2 wurde 0,5 nach links gegangen."), regel="rr.plusminus")

# ───────── brueche_mal ─────────
neu(T, "brueche_mal", "lueckenweg", L(
    "Berechne 10/21 · 9/25. Kürze vor dem Malnehmen über Kreuz: 10 und 25 durch ① und 9 und 21 durch ②. Das Ergebnis ist dann ③/④.",
    KOMM(4), [5, 3, 6, 35], ["5", "3", "(10 / {1}) * (9 / {2})", "(21 / {2}) * (25 / {1})"], ["gcd(10, 25)", "gcd(9, 21)", "6", "35"], "Welche größte Zahl teilt 10 und 25? Welche teilt 9 und 21?",
    "10 : 5 = 2 und 25 : 5 = 5. 9 : 3 = 3 und 21 : 3 = 7. Dann: 2/7 · 3/5 = 6/35.",
    {0: [(1, None, "gar nicht gekürzt: nur durch 1 geteilt", False)], 2: [(90, None, "nicht gekürzt: Zähler 10 · 9", "10 * 9")], 3: [(525, None, "nicht gekürzt: Nenner 21 · 25", "21 * 25")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.bruchrechnen")
neu(T, "brueche_mal", "verfahren_waehlen", W(
    "Du sollst 8/15 · 5/12 berechnen. Welcher Weg ist richtig und geschickt?",
    "Vor dem Malnehmen über Kreuz kürzen: 2/3 · 1/3 = 2/9",
    [("Zähler und Nenner einzeln addieren: 13/27", "addiert statt malgenommen"),
     ("Mit dem Kehrwert von 5/12 malnehmen: 8/15 · 12/5 = 32/25", "falsch geteilt statt malgenommen"),
     ("Nur die Zähler malnehmen, den Nenner 15 behalten: 40/15", "den Nenner nicht mit malgenommen")],
    "Beim Malnehmen von Brüchen braucht man keinen gemeinsamen Nenner.",
    "Zähler mal Zähler und Nenner mal Nenner. Vorher kürzen: 8 und 12 durch 4, 5 und 15 durch 5. So bleibt 2/3 · 1/3 = 2/9. Probe: 8/15 · 5/12 = 40/180 = 2/9.",
    lambda: F(8, 15) * F(5, 12) == F(2, 9) and F(13, 27) != F(2, 9) and F(32, 25) != F(2, 9) and F(40, 15) != F(2, 9) and F(8 + 5, 15 + 12) == F(13, 27) and F(8, 15) * F(12, 5) == F(32, 25) and F(8 * 5, 15) == F(40, 15)), g="mehrschritt", regel="rr.bruchrechnen")
neu(T, "brueche_mal", "anwenden", L(
    "Von einer Torte sind noch 3/4 da. Anna isst davon 2/3. Vom Rest, der dann noch da ist, isst Ben 1/3. Welcher Bruchteil der ganzen Torte bleibt am Ende?",
    "□/□", [1, 6], ["(3/4 * (1 - 2/3) * (1 - 1/3)) * 6", "6"], ["1", "6"], "Rechne mit dem Rest, der nach jedem Essen noch da ist.",
    "Nach Anna: 3/4 · 1/3 = 1/4 der Torte bleibt. Ben isst 1/3 davon, es bleiben 2/3 von 1/4. 2/3 · 1/4 = 2/12 = 1/6.",
    {1: [(4, None, "nach Anna aufgehört: 1/4 der Torte bleibt", "1 / (3/4 * (1 - 2/3))")]}, hinweis=H4), g="transfer", regel="rr.bruchrechnen")

# ───────── brueche_geteilt ─────────
neu(T, "brueche_geteilt", "lueckenweg", L(
    "Berechne 7/12 : 21/16 als Malaufgabe mit dem Kehrwert: 7/12 · 16/21 = ①/②. Gekürzt ist das Ergebnis ③/④.",
    KOMM(4), [112, 252, 4, 9], ["7 * 16", "12 * 21", "{1} / 28", "{2} / 28"], ["112", "252", "4", "9"], "Beim Teilen durch einen Bruch malnimmst du mit seinem Kehrwert.",
    "7 · 16 = 112 und 12 · 21 = 252. 112/252 wird durch 28 gekürzt: 4/9.",
    {0: [(147, None, "nicht mit dem Kehrwert gerechnet: 7 · 21", "7 * 21")], 1: [(192, None, "nicht mit dem Kehrwert gerechnet: 12 · 16", "12 * 16")], 2: [(112, None, "nicht gekürzt", "{1} / 1")], 3: [(252, None, "nicht gekürzt", "{2} / 1")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.bruchrechnen")
neu(T, "brueche_geteilt", "anwenden", Z(
    "Aus einem Krug mit 3/4 Liter Saft sollen kleine Gläser mit je 1/8 Liter gefüllt werden. Wie viele Gläser werden voll?",
    6, "(3/4) / (1/8)", "3 * 2", "Wie oft passt 1/8 in 3/4?",
    "3/4 : 1/8 = 3/4 · 8 = 6. In 3/4 Liter passen 6 Gläser zu je 1/8 Liter. Probe: 6 · 1/8 = 3/4.",
    [(0.09375, None, "malgenommen statt geteilt", "3/4 * 1/8"), (0.625, None, "abgezogen statt geteilt: 3/4 − 1/8", "3/4 - 1/8")]), regel="rr.bruchrechnen")
neu(T, "brueche_geteilt", "umkehren", L(
    "Der Bruch 3/4 wird durch einen Bruch geteilt. Das Ergebnis ist 9/8. Durch welchen Bruch wurde geteilt? Schreibe ihn gekürzt.",
    "□/□", [2, 3], ["(3/4 / (9/8)) * 3", "3"], ["2", "3"], "Wenn a : b = c ist, dann ist b = a : c.",
    "Gesucht ist x mit 3/4 : x = 9/8. Dann ist x = 3/4 : 9/8 = 3/4 · 8/9 = 24/36 = 2/3. Probe: 3/4 : 2/3 = 3/4 · 3/2 = 9/8.",
    {0: [(3, None, "falsch herum geteilt: 9/8 : 3/4 = 3/2", "(9/8 / (3/4)) * 2")], 1: [(2, None, "falsch herum geteilt: 9/8 : 3/4 = 3/2", "2")]}, hinweis=H4), g="rueckwaerts", regel="rr.bruchrechnen")

# ───────── dezimal_mal ─────────
neu(T, "dezimal_mal", "lueckenweg", L(
    "Berechne 3,6 · 0,25. Rechne zuerst ohne Komma: 36 · 25 = ①. Die beiden Faktoren haben zusammen ② Nachkommastellen. Das Ergebnis hat dann ③ Zehntel. Es ist um ④ Hundertstel kleiner als 1.",
    KOMM(4), [900, 3, 9, 10], ["36 * 25", "1 + 2", "{1} / 10 ** {2} * 10", "100 - {3} * 10"], ["900", "3", "9", "10"], "Zähle die Stellen hinter dem Komma bei beiden Faktoren.",
    "36 · 25 = 900. 3,6 hat 1 und 0,25 hat 2 Nachkommastellen, zusammen 3. 900 mit 3 Nachkommastellen ist 0,900 = 0,9, das sind 9 Zehntel. 0,9 sind 90 Hundertstel, bis 1 fehlen 100 − 90 = 10 Hundertstel.",
    {0: [(61, None, "addiert statt malgenommen", "36 + 25")], 1: [(2, None, "nur die Stellen des zweiten Faktors gezählt", "2")], 2: [(90, None, "nur zwei Stellen abgetrennt: 9,00", "{1} / 10 ** 2 * 10")],
     3: [(90, None, "das Ergebnis selbst statt des Unterschieds zu 1 angegeben", "{3} * 10")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.stellenwert")
neu(T, "dezimal_mal", "zwei_wege", Z(
    "Berechne 0,4 · 0,35 auf zwei Wegen. Weg A: Rechne 4 · 35 und setze das Komma nach den Nachkommastellen. Weg B: Schreibe beide Zahlen als Bruch und multipliziere. Wie lautet das Ergebnis?",
    0.14, "4 * 35 / 1000", "0.4 * 0.35", "Wie viele Nachkommastellen haben beide Faktoren zusammen?",
    "Weg A: 4 · 35 = 140, drei Nachkommastellen: 0,140 = 0,14. Weg B: 4/10 · 35/100 = 140/1000 = 14/100 = 0,14.",
    [(1.4, None, "zwei statt drei Nachkommastellen abgetrennt", "4 * 35 / 100"), (14, None, "nur eine Nachkommastelle abgetrennt: 14,0", "4 * 35 / 10"), (140, None, "das Komma gar nicht gesetzt: 4 · 35", "4 * 35")]), g="mehrschritt", regel="rr.stellenwert")
neu(T, "dezimal_mal", "anwenden", Z(
    "Ein Kilogramm Birnen kostet 2,40 €. Mia kauft 1,4 kg. An der Kasse bekommt sie 0,50 € Rabatt auf den Gesamtbetrag. Wie viel Euro zahlt sie?",
    2.86, "1.4 * 2.4 - 0.5", "3.36 - 0.5", "Berechne zuerst den Preis für die Birnen.",
    "1,4 · 2,40 = 3,36. Dann der Rabatt: 3,36 − 0,50 = 2,86. Mia zahlt 2,86 €.",
    [(3.36, None, "den Rabatt vergessen", "1.4 * 2.4"), (3.3, None, "addiert statt malgenommen: 1,4 + 2,4 − 0,5", "1.4 + 2.4 - 0.5")], "€"), g="transfer", regel="rr.stellenwert")

# ───────── dezimal_geteilt ─────────
neu(T, "dezimal_geteilt", "lueckenweg", L(
    "Berechne 4,8 : 0,06. Erweitere beide Zahlen mit 100: ① : 6. Das Ergebnis ist ②. Das sind ③ Zehner.",
    KOMM(3), [480, 80, 8], ["4.8 * 100", "{1} / 6", "{2} / 10"], ["480", "80", "8"], "Erweitere so, dass der Teiler eine ganze Zahl wird.",
    "4,8 · 100 = 480 und 0,06 · 100 = 6. 480 : 6 = 80. 80 sind 8 Zehner.",
    {0: [(48, None, "nur mit 10 erweitert", "4.8 * 10")], 1: [(8, None, "durch 60 statt durch 6 geteilt", "{1} / 60")], 2: [(800, None, "mit 10 malgenommen statt geteilt", "{2} * 10")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.stellenwert")
neu(T, "dezimal_geteilt", "anwenden", Z(
    "Ein Seil ist 7,2 m lang. Daraus werden Stücke von je 0,35 m geschnitten. Wie viele ganze Stücke ergibt das?",
    20, "7.2 // 0.35", "720 // 35", "Teile die Länge des Seils durch die Länge eines Stücks.",
    "7,2 : 0,35 = 720 : 35 = 20 Rest 20. Es gibt 20 ganze Stücke, ein Rest von 0,2 m bleibt übrig.",
    [(21, None, "aufgerundet, obwohl das letzte Stück nicht ganz ist", "7.2 // 0.35 + 1"), (0.2, None, "den Rest in Metern statt der Zahl der Stücke angegeben", "7.2 - 20 * 0.35")]), regel="rr.stellenwert")
neu(T, "dezimal_geteilt", "fehler_detektiv", FD(
    "Eva rechnet 1,35 : 0,9.",
    [("1,35 : 0,9 = 135 : 9", F(135, 100) / F(9, 10) == F(135, 9)), ("135 : 9 = 15", F(135, 9) == 15), ("Also ist 1,35 : 0,9 = 15.", True)],
    "Mit welcher Zahl musst du beide Zahlen malnehmen, damit der Teiler 9 wird? Ändert das auch die erste Zahl um dasselbe?", "Erweiterst du beide Zahlen mit 10, steht 13,5 : 9 = 1,5. Wer 1,35 mit 100 und 0,9 mit 10 erweitert, ändert die Aufgabe. Die Zeilen 2 und 3 rechnen mit 135 : 9 richtig weiter."), regel="rr.stellenwert")

# ───────── potenzen ─────────
neu(T, "potenzen", "lueckenweg", L(
    "Berechne (2/5)³. Der Zähler ist 2³ = ①. Der Nenner ist 5³ = ②. Als Dezimalzahl sind das ③ Tausendstel. Auf Hundertstel gerundet sind es ④ Hundertstel.",
    KOMM(4), [8, 125, 64, 6], ["2 ** 3", "5 ** 3", "{1} * 1000 / {2}", "({3} + 5) // 10"], ["8", "125", "64", "6"], "Beim Potenzieren von Brüchen wird Zähler und Nenner potenziert.",
    "2³ = 8 und 5³ = 125. (2/5)³ = 8/125. Erweitern mit 8 gibt 64/1000, also 0,064, das sind 64 Tausendstel. Auf Hundertstel gerundet: 0,06, das sind 6 Hundertstel.",
    {0: [(6, None, "Basis mal Hochzahl gerechnet: 2 · 3", "2 * 3")], 1: [(15, None, "Basis mal Hochzahl gerechnet: 5 · 3", "5 * 3")], 2: [(640, None, "mit 10 000 statt mit 1000 erweitert", "{1} * 10000 / {2}")],
     3: [(7, None, "aufgerundet statt abgerundet", "{3} // 10 + 1")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.potenz")
neu(T, "potenzen", "anwenden", Z(
    "Eine quadratische Teppichfliese hat die Seitenlänge 2/5 m. Wie groß ist seine Fläche in Quadratdezimetern? (1 m² = 100 dm²)",
    16, "(2/5) ** 2 * 100", "4 / 25 * 100", "Die Fläche eines Quadrats ist Seite mal Seite.",
    "Fläche = (2/5 m)² = 4/25 m² = 0,16 m². Mal 100: 16 dm².",
    [(80, None, "die Seite mit 2 malgenommen statt quadriert", "2/5 * 2 * 100"), (0.16, None, "in m² statt in dm² angegeben", "(2/5) ** 2")], "dm²"), regel="rr.potenz")
neu(T, "potenzen", "umkehren", L(
    "Eine Zahl a/b hoch 3 ergibt 27/64. Wie heißt die Zahl? Schreibe sie als Bruch.",
    "□/□", [3, 4], ["3", "4"], ["3", "4"], "Welche Zahl mal sich selbst mal sich selbst ergibt 27, welche 64?",
    "3 · 3 · 3 = 27 und 4 · 4 · 4 = 64. Also (3/4)³ = 27/64. Die Zahl ist 3/4.",
    {0: [(9, None, "den Zähler 27 durch 3 geteilt", "27 / 3")], 1: [(16, None, "den Nenner 64 durch 4 geteilt", "64 / 4")]}, hinweis=H4), g="rueckwaerts", regel="rr.potenz")

# ───────── rechenvorteile ─────────
neu(T, "rechenvorteile", "lueckenweg", L(
    "Berechne 4 · 3,7 · 25 geschickt. Zuerst tauschst du die Faktoren und rechnest 4 · 25 = ①. Dann ① · 3,7 = ②. Das sind ③ Zehntel.",
    KOMM(3), [100, 370, 3700], ["4 * 25", "{1} * 3.7", "{2} * 10"], ["100", "370", "3700"], "Welche zwei Faktoren ergeben zusammen eine runde Zahl?",
    "4 · 25 = 100. 100 · 3,7 = 370. Das sind 3700 Zehntel.",
    {0: [(29, None, "addiert statt malgenommen", "4 + 25")], 1: [(3700, None, "das Komma vergessen: 100 · 37", "{1} * 37")], 2: [(37, None, "durch 10 geteilt statt malgenommen", "{2} / 10")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.tauschen")
neu(T, "rechenvorteile", "zwei_wege", Z(
    "Berechne 98 · 7 auf zwei Wegen. Weg A: Schreibe 98 als 100 − 2 und rechne 100 · 7 − 2 · 7. Weg B: Multipliziere 98 mit 7 schriftlich.",
    686, "100 * 7 - 2 * 7", "98 * 7", "Beide Wege müssen dasselbe Ergebnis liefern.",
    "Weg A: 100 · 7 = 700 und 2 · 7 = 14. 700 − 14 = 686. Weg B: 98 · 7 = 686.",
    [(714, None, "plus statt minus: 100 · 7 + 2 · 7", "100 * 7 + 2 * 7"), (698, None, "nur 2 abgezogen statt 2 · 7", "100 * 7 - 2")]), g="mehrschritt", regel="rr.tauschen")
neu(T, "rechenvorteile", "anwenden", Z(
    "Ein Lager enthält 25 Kisten. In jeder Kiste stehen 4 Kartons. Jeder Karton wiegt 3,6 kg. Wie viel Kilogramm wiegt alles zusammen?",
    360, "25 * 4 * 3.6", "100 * 3.6", "Welche beiden Zahlen kannst du zuerst malnehmen, um eine runde Zahl zu erhalten?",
    "25 · 4 = 100 Kartons. 100 · 3,6 kg = 360 kg.",
    [(90, None, "nur 25 Kisten mit 3,6 kg gerechnet, die Kartons vergessen", "25 * 3.6"), (3600, None, "das Komma falsch gesetzt: 25 · 4 · 36", "25 * 4 * 36")], "kg"), g="transfer", regel="rr.tauschen")

# ───────── gemischt ─────────
neu(T, "gemischt", "lueckenweg", L(
    "Berechne 8/9 − 3/4 · 2/9. Punkt vor Strich: Das Produkt ist ①/② (noch nicht gekürzt). Das Ergebnis der ganzen Aufgabe ist ③/④ (gekürzt).",
    KOMM(4), [6, 36, 13, 18], ["3 * 2", "4 * 9", "(8/9 - {1} / {2}) * 18", "{2} / 2"], ["6", "36", "13", "18"], "Rechne zuerst das Mal. Dann bringe beide Brüche auf einen Nenner.",
    "3/4 · 2/9 = 6/36 = 1/6. 8/9 = 16/18 und 1/6 = 3/18. 16/18 − 3/18 = 13/18.",
    {0: [(5, None, "addiert statt malgenommen", "3 + 2")], 1: [(13, None, "addiert statt malgenommen", "4 + 9")],
     2: [(5, None, "von links nach rechts gerechnet: (8/9 − 3/4) · 2/9 = 5/162", "(8/9 - 3/4) * 2/9 * 162")], 3: [(162, None, "von links nach rechts gerechnet: (8/9 − 3/4) · 2/9 = 5/162", "36 * 9 / 2")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.reihenfolge")
neu(T, "gemischt", "bruecke", W(
    "Welcher Term passt zu dem Satz: „Von 7/8 wird das Produkt aus 1/2 und 3/4 abgezogen“?",
    "7/8 − 1/2 · 3/4",
    [("(7/8 − 1/2) · 3/4", "die Differenz mit 3/4 malgenommen statt des Produkts abgezogen"),
     ("7/8 − 1/2 − 3/4", "beide Zahlen einzeln abgezogen"),
     ("7/8 · 1/2 − 3/4", "7/8 mit 1/2 malgenommen")],
    "Was wird abgezogen? Es ist ein Produkt aus zwei Zahlen.",
    "Das Produkt aus 1/2 und 3/4 ist 1/2 · 3/4. Dieses Produkt wird von 7/8 abgezogen: 7/8 − 1/2 · 3/4 = 7/8 − 3/8 = 1/2.",
    lambda: F(7, 8) - F(1, 2) * F(3, 4) == F(1, 2) and len({F(7, 8) - F(1, 2) * F(3, 4), (F(7, 8) - F(1, 2)) * F(3, 4), F(7, 8) - F(1, 2) - F(3, 4), F(7, 8) * F(1, 2) - F(3, 4)}) == 4), regel="rr.reihenfolge")
neu(T, "gemischt", "anwenden", Z(
    "Aus 60 Litern Saft werden 1/3 in Flaschen gefüllt. Vom Rest werden 3/4 in Kanister gefüllt. Wie viele Liter bleiben übrig?",
    10, "60 * (1 - 1/3) * (1 - 3/4)", "60 - 20 - 30", "Welcher Rest bleibt nach dem Abfüllen in Flaschen?",
    "Flaschen: 60 l : 3 = 20 l. Rest: 40 l. Kanister: 40 l : 4 · 3 = 30 l. Übrig: 40 l − 30 l = 10 l.",
    [(20, None, "nur die Menge für die Flaschen angegeben", "60 / 3"), (30, None, "die Menge für die Kanister statt des Rests angegeben", "60 * (1 - 1/3) * 3/4")], "l"), g="transfer", regel="rr.reihenfolge")

# ───────── fehler_finden ─────────
neu(T, "fehler_finden", "lueckenweg", L(
    "Ein Kind rechnet 7/8 + 5/6 = 12/14, weil es Zähler und Nenner einzeln addiert. Richtig ist: Der Hauptnenner ist ①. Die Summe hat dann den Zähler ②. Als gemischte Zahl ist die Summe 1 ③/①.",
    KOMM(3), [24, 41, 17], ["24", "7 * {1} / 8 + 5 * {1} / 6", "{2} - {1}"], ["lcm(8, 6)", "41", "17"], "Brüche mit verschiedenen Nennern muss man erst gleichnamig machen.",
    "Hauptnenner 24: 7/8 = 21/24 und 5/6 = 20/24. 21 + 20 = 41. Die Summe ist 41/24 = 1 17/24.",
    {0: [(48, None, "die Nenner malgenommen: 8 · 6", "8 * 6")], 1: [(12, None, "die Zähler addiert: 7 + 5", "7 + 5")], 2: [(41, None, "den Zähler nicht in Ganze und Rest zerlegt", "{2}")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.bruchrechnen")
neu(T, "fehler_finden", "verfahren_waehlen", W(
    "Eine dieser vier Rechnungen ist falsch. Welche?",
    "0,2 · 0,3 = 0,6",
    [("3/5 · 10 = 6", "diese Rechnung stimmt"), ("2/3 : 4 = 1/6", "diese Rechnung stimmt"), ("1,5 + 0,25 = 1,75", "diese Rechnung stimmt")],
    "Rechne jede Aufgabe kurz nach. Bei Kommazahlen hilft die Zahl der Nachkommastellen.",
    "0,2 · 0,3 = 0,06, denn 2 · 3 = 6 und es gibt zwei Nachkommastellen. Die anderen stimmen: 3/5 · 10 = 6, 2/3 : 4 = 2/12 = 1/6, 1,5 + 0,25 = 1,75.",
    lambda: F(2, 10) * F(3, 10) != F(6, 10) and F(3, 5) * 10 == 6 and F(2, 3) / 4 == F(1, 6) and F(15, 10) + F(25, 100) == F(175, 100)), g="mehrschritt", regel="rr.bruchrechnen")
neu(T, "fehler_finden", "fehler_detektiv", FD(
    "Karl rechnet 2/3 : 4/9.",
    [("2/3 : 4/9 = 2/3 · 9/4", F(2, 3) / F(4, 9) == F(2, 3) * F(9, 4)), ("= 18/12", F(2, 3) * F(9, 4) == F(18, 12)), ("Gekürzt ist das 2/3.", F(18, 12) == F(2, 3))],
    "Kürze 18/12 noch einmal. Durch welche Zahl teilst du?", "18/12 wird durch 6 gekürzt: 3/2 = 1 1/2. In Zeile 3 stehen Zähler und Nenner vertauscht."), regel="rr.bruchrechnen")

# ───────── sach ─────────
neu(T, "sach", "lueckenweg", L(
    "Ein Rezept für 6 Portionen braucht 3/4 Liter Milch. Für eine Portion braucht man ①/② Liter (gekürzt). Für 10 Portionen braucht man ③/4 Liter. Das sind ④ Milliliter.",
    KOMM(4), [1, 8, 5, 1250], ["3/4 * 8/6", "6 * 4 / 3", "10 * {1} / {2} * 4", "{3} * 1000 / 4"], ["1", "8", "5", "1250"], "Teile die Milchmenge durch die Zahl der Portionen.",
    "3/4 l : 6 = 3/24 l = 1/8 l. Für 10 Portionen: 10 · 1/8 l = 10/8 l = 5/4 l. Das sind 5/4 · 1000 ml = 1250 ml.",
    {0: [(3, None, "den Zähler 3 nicht geteilt", "3")], 1: [(24, None, "nicht gekürzt: 4 · 6", "6 * 4")], 2: [(10, None, "die Portionszahl 10 als Zähler übernommen", "10")],
     3: [(5000, None, "den Bruch 5/4 nicht beachtet: Zähler 5 mal 1000", "{3} * 1000"), (12500, None, "mit 10 000 statt mit 1000 malgenommen", "{3} * 10000 / 4")]}, hinweis="Je Lücke eine ganze Zahl."), regel="rr.bruchrechnen")
neu(T, "sach", "anwenden", Z(
    "Svens Taschengeld im Monat beträgt 12,50 €. Er gibt 3/5 davon aus. Von dem, was übrig bleibt, kauft er ein Heft für 4,25 €. Wie viel Euro bleiben ihm?",
    0.75, "12.5 * (1 - 3/5) - 4.25", "5 - 4.25", "Wie viel Euro hat er nach den 3/5 noch?",
    "3/5 von 12,50 € sind 7,50 €. Übrig: 12,50 € − 7,50 € = 5 €. Nach dem Heft: 5 € − 4,25 € = 0,75 €.",
    [(7.5, None, "den ausgegebenen Betrag statt des Rests genommen", "12.5 * 3/5"), (8.25, None, "die 3/5 vergessen", "12.5 - 4.25")], "€"), regel="rr.bruchrechnen")
neu(T, "sach", "umkehren", Z(
    "Ein Becken ist zu 3/5 gefüllt. Nach dem Einfüllen von 1,2 m³ Wasser ist es zu 4/5 gefüllt. Wie viele Kubikmeter Wasser passen in das ganze Becken?",
    6, "1.2 / (4/5 - 3/5)", "1.2 * 5", "Welcher Bruchteil des Beckens sind die 1,2 m³?",
    "Hinzugekommen sind 4/5 − 3/5 = 1/5 des Beckens. 1/5 sind 1,2 m³, also ist das ganze Becken 5 · 1,2 m³ = 6 m³.",
    [(1.5, None, "die 1,2 m³ als 4/5 des Beckens angesehen", "1.2 / (4/5)"), (0.24, None, "malgenommen statt geteilt", "1.2 * (4/5 - 3/5)")], "m³"), g="rueckwaerts", regel="rr.bruchrechnen")
