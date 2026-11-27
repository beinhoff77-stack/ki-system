"""rollend-5 · zahlen.ganz (11 Lernkarten, 33 Aufgaben)."""
from k5basis import *      # noqa: F401,F403

TH = "zahlen.ganz"
PM, VZ, ZGR, GR, BT = "rr.plusminus", "rr.vorzeichen", "id.zahlen.zahlengerade", "rr.gegenrechnung", "id.zahlen.zahlengerade"
ST = "rr.stellenwert"

# ── deuten ──
neu(TH, "deuten", "lueckenweg", "direkt", L(
    "Es sind vier Grad unter null. Man schreibt ① °C. Dann wird es 7 Grad wärmer: ① + 7 = ② °C. Danach sinkt die Temperatur um 9 Grad: ② − 9 = ③ °C.",
    ["-4", "-4+7", "-4+7-9"], ["-4", "3", "-6"], "Unter null schreibst du ein Minus vor die Zahl.", "Vier Grad unter null sind −4 °C. −4 + 7 = 3 °C. 3 − 9 = −6 °C.",
    {0: [(4, None, "das Minus vergessen")], 1: [(11, "fb.plusminus.zeichen_des_ergebnisses", "4 + 7 gerechnet")], 2: [(2, None, "mit 11 weitergerechnet")]}), ZGR)
neu(TH, "deuten", "bruecke", "darstellung", Z(
    "Die Tabelle zeigt die Temperatur an einem Wintertag. Um wie viele Grad ist es um 12 Uhr wärmer als um 6 Uhr?",
    "3-(-5)", "5+3", "Wie weit ist es von −5 bis 0, und wie weit von 0 bis 3?", "Von −5 bis 0 sind es 5 Grad, von 0 bis 3 noch 3 Grad. Zusammen 8 Grad.",
    [(2, "fb.plusminus.zeichen_des_ergebnisses", "−5 und 3 ohne Vorzeichen subtrahiert"), (-8, None, "falsches Vorzeichen")],
    grafik=TAB(["Uhrzeit", "6 Uhr", "12 Uhr", "18 Uhr"], ["Grad", "−5", "3", "−2"])), ZGR)
neu(TH, "deuten", "anwenden", "einkleidung", Z(
    "In einem Hochhaus ist das zweite Kellergeschoss die Etage −2. Ein Aufzug fährt vom Parkdeck in Etage −3 bis in die Etage 4. Wie viele Etagen fährt er?",
    "4-(-3)", "3+4", "Zähle von −3 bis 0 und dann von 0 bis 4.", "Von −3 bis 0 sind es 3 Etagen, von 0 bis 4 noch 4. Zusammen 7 Etagen.",
    [(1, "fb.plusminus.zeichen_des_ergebnisses", "4 − 3 gerechnet"), (4, None, "nur bis zur 0 gezählt")]), ZGR)

# ── zahlengerade ──
neu(TH, "zahlengerade", "fehler_detektiv", "fehler", FDZ(
    "Eine Zahlengerade geht von −10 bis 10 und hat 10 Abschnitte. Der Punkt P liegt 3 Abschnitte links von 0. Kim bestimmt P.",
    [("Ein Abschnitt ist 10 : 10 = 1 wert.", 10 / 10 == (10 - (-10)) / 10), ("P liegt 3 Abschnitte links von 0: 3 · 1 = 3, links also −3.", True), ("Also ist P = −3.", True)],
    "Wie lang ist die ganze Zahlengerade? Nicht nur die rechte Seite zählt.", "Die Gerade ist von −10 bis 10 insgesamt 20 lang. Ein Abschnitt ist 20 : 10 = 2 wert. 3 Abschnitte links von 0 sind −6."), ZGR)
neu(TH, "zahlengerade", "zwei_wege", "mehrschritt", Z(
    "Der Punkt A liegt bei −7, der Punkt B bei 5. Weg A: zähle von −7 bis 0 und von 0 bis 5. Weg B: rechne 5 − (−7). Wie weit sind A und B voneinander entfernt?",
    "5-(-7)", "7+5", "Beide Wege geben dieselbe Zahl.", "Weg A: 7 + 5 = 12. Weg B: 5 − (−7) = 5 + 7 = 12.",
    [(2, "fb.plusminus.zeichen_des_ergebnisses", "7 und 5 abgezogen"), (-12, None, "falsches Vorzeichen")]), ZGR)
neu(TH, "zahlengerade", "bruecke", "darstellung", Z(
    "Die Zahlengerade zeigt die Punkte A und B. Wie viele Einheiten liegt B rechts von A?",
    "4-(-7)", "7+4", "Lies zuerst die beiden Zahlen ab.", "A liegt bei −7, B bei 4. Von −7 bis 0 sind es 7, von 0 bis 4 noch 4: zusammen 11.",
    [(3, "fb.plusminus.zeichen_des_ergebnisses", "7 und 4 abgezogen"), (-11, None, "falsch herum gerechnet")],
    grafik={"typ": "zahlenstrahl", "start": -10, "ende": 10, "abschnitte": 20, "punkte": [{"wert": -7, "name": "A"}, {"wert": 4, "name": "B"}], "beschriftet": "alle"}), ZGR)

# ── ordnen ──
neu(TH, "ordnen", "lueckenweg", "direkt", L(
    "Vergleiche −15 und −6. Die Zahl −15 liegt weiter links, sie ist kleiner. Der Unterschied: (−6) − (−15) = ①. Starte bei −15, gehe ① Schritte nach rechts und dann noch 4 Schritte weiter. Du landest bei ②.",
    ["(-6)-(-15)", "-15+((-6)-(-15))+4"], ["9", "-2"], "Minus minus heißt plus. Rechts ist größer.", "(−6) − (−15) = −6 + 15 = 9. −15 + 9 = −6, dann −6 + 4 = −2.",
    {0: [(21, None, "beide Beträge addiert")], 1: [(-6, None, "die 4 Schritte vergessen"), (-10, None, "−15 + 9 − 4 gerechnet")]}), ZGR)
neu(TH, "ordnen", "umkehren", "umkehr", Z(
    "Eine Zahl ist um 4 größer als die gesuchte Zahl. Sie ist 1. Wie heißt die gesuchte Zahl?",
    "1-4", "-3", "Gehe von 1 vier Schritte nach links.", "Gesucht ist die Zahl, die 4 kleiner ist als 1: 1 − 4 = −3.",
    [(5, None, "nach rechts gezählt"), (3, "fb.plusminus.zeichen_des_ergebnisses", "das Minus vergessen")]), ZGR)
neu(TH, "ordnen", "anwenden", "einkleidung", Z(
    "An drei Morgen wurden diese Temperaturen gemessen: −4 °C, −9 °C und 2 °C. Wie viel Grad wärmer ist der wärmste Morgen als der kälteste?",
    "2-(-9)", "9+2", "Ordne zuerst. Der kälteste Morgen liegt am weitesten links.", "Wärmster: 2 °C, kältester: −9 °C. Unterschied: 2 − (−9) = 11 Grad.",
    [(7, "fb.zahlengerade.nach_betrag_geordnet", "−9 als größte Zahl gesehen"), (5, None, "−9 und −4 verglichen")], einheit="Grad"), ZGR)

# ── betrag ──
neu(TH, "betrag", "fehler_detektiv", "fehler", FDZ(
    "Kim sucht alle ganzen Zahlen, deren Betrag 5 ist.",
    [("|5| = 5.", abs(5) == 5), ("Eine Zahl links von 0 kann nicht den Betrag 5 haben.", not any(abs(x) == 5 for x in range(-10, 0))), ("Es gibt nur eine solche Zahl, nämlich 5.", True)],
    "Der Betrag ist der Abstand zu 0. Gibt es auch links von 0 eine Zahl mit diesem Abstand?", "Der Betrag ist der Abstand zu 0. Auch −5 hat den Abstand 5. Es gibt zwei solche Zahlen: 5 und −5."), BT)
neu(TH, "betrag", "umkehren", "umkehr", Z(
    "Zwei Zahlen sind Gegenzahlen und liegen 18 Einheiten auseinander. Wie heißt die negative der beiden Zahlen?",
    "-18//2", "-9", "Gegenzahlen liegen gleich weit von 0 entfernt, auf beiden Seiten.", "Die 18 Einheiten teilen sich auf beide Seiten von 0: 18 : 2 = 9. Die negative Zahl ist −9.",
    [(9, None, "die positive Zahl genannt"), (-18, None, "den Abstand als Zahl genommen")]), BT)
neu(TH, "betrag", "anwenden", "einkleidung", Z(
    "Ein Taucher ist 14 m unter der Wasseroberfläche (−14 m). Ein Kranhaken hängt 6 m über dem Wasser. Wie weit ist der Taucher vom Haken entfernt?",
    "abs(6-(-14))", "14+6", "Rechne den Abstand: Das Ergebnis darf nicht negativ sein.", "Vom Taucher bis zur Oberfläche sind es 14 m, von dort bis zum Haken 6 m. Zusammen 20 m.",
    [(8, "fb.plusminus.zeichen_des_ergebnisses", "14 − 6 gerechnet"), (-20, None, "negativen Abstand angegeben")], einheit="m"), BT)

# ── schriftlich_plus_minus ──
neu(TH, "schriftlich_plus_minus", "lueckenweg", "direkt", L(
    "Schriftlich 2 746 + 3 585. Einer: 6 + 5 = 11, ich schreibe 1 und merke 1. Zehner: 4 + 8 + 1 = ①. Ich schreibe 3 und merke 1. Hunderter: 7 + 5 + 1 = ②. Ich schreibe 3 und merke 1. Tausender: 2 + 3 + 1 = 6. Das Ergebnis besteht aus der 6 und der Einerziffer von ② und der Einerziffer von ① und der 1 der Einer. Das Ergebnis ist ③.",
    ["4+8+1", "7+5+1", "2746+3585"], ["13", "13", "6331"], "Den Übertrag jedes Mal mitnehmen.", "4 + 8 + 1 = 13, 7 + 5 + 1 = 13, Tausender 6. Ergebnis: 6 331.",
    {2: [(5331, None, "den Übertrag der Hunderter vergessen"), (6231, None, "einen Übertrag vergessen")]}), ST)
neu(TH, "schriftlich_plus_minus", "zwei_wege", "mehrschritt", Z(
    "Berechne 5 000 − 1 876. Weg A: schriftlich subtrahieren mit Tauschen. Weg B: erst 5 000 − 2 000 = 3 000, dann den zu viel abgezogenen Teil wieder addieren. Wie groß ist das Ergebnis?",
    "5000-1876", "3000+(2000-1876)", "Wie viel hast du bei Weg B zu viel abgezogen?", "Weg A: 5 000 − 1 876 = 3 124. Weg B: 2 000 − 1 876 = 124 zu viel. 3 000 + 124 = 3 124.",
    [(2876, None, "den Teil abgezogen statt addiert")]), ST)
neu(TH, "schriftlich_plus_minus", "anwenden", "einkleidung", Z(
    "Ein Flughafen hatte im Mai 1 245 780 Fluggäste und im Juni 1 398 650 Fluggäste. Wie viele Fluggäste kamen im Juni mehr?",
    "1398650-1245780", "152870", "Rechne schriftlich minus und achte auf das Tauschen.", "1 398 650 − 1 245 780 = 152 870 Fluggäste mehr.",
    [(142870, None, "einen Übertrag vergessen"), (2644430, None, "addiert statt abgezogen")]), ST)

# ── addieren ──
neu(TH, "addieren", "fehler_detektiv", "fehler", FDZ(
    "Kim rechnet (−7) + 4.",
    [("Plus bedeutet auf der Zahlengeraden: nach links.", (-7) - 4 == (-7) + 4), ("Ich starte bei −7 und gehe 4 Schritte nach links.", True), ("Ich lande bei −11.", True)],
    "In welche Richtung geht es bei Plus?", "Plus heißt nach rechts. Von −7 vier Schritte nach rechts: −7 + 4 = −3."), PM)
neu(TH, "addieren", "umkehren", "umkehr", Z(
    "Zu einer Zahl wird 9 addiert. Das Ergebnis ist −2. Wie heißt die Zahl?",
    "-2-9", "-11", "Kehre die Addition um: minus 9.", "−2 − 9 = −11. Probe: (−11) + 9 = −2.",
    [(7, "fb.plusminus.zeichen_des_ergebnisses", "−2 + 9 gerechnet"), (11, None, "Vorzeichen vergessen")]), PM)
neu(TH, "addieren", "bruecke", "darstellung", W(
    "Der Sprung auf der Zahlengeraden beginnt bei −6 und endet bei 2. Welche Rechnung gehört dazu?",
    "(−6) + 8 = 2", [("(−6) − 8 = −14", "falsche Richtung"), ("6 + 8 = 14", "das Minus vergessen"), ("(−6) + 2 = −4", "das Ziel als Sprunglänge genommen")],
    "Wie viele Schritte nach rechts sind es von −6 bis 2?", "Von −6 bis 0 sind es 6 Schritte, von 0 bis 2 noch 2: zusammen 8 Schritte nach rechts. (−6) + 8 = 2.",
    -6 + 8 == 2 and -6 - 8 != 2 and 6 + 8 != 2 and -6 + 2 != 2,
    grafik={"typ": "zahlenstrahl", "start": -10, "ende": 10, "abschnitte": 20, "punkte": [{"wert": -6, "name": "Start"}, {"wert": 2, "name": "Ziel"}], "beschriftet": "alle"}), PM)

# ── subtrahieren ──
neu(TH, "subtrahieren", "lueckenweg", "direkt", L(
    "Minus eine Zahl heißt: plus die Gegenzahl. 5 − 13 = 5 + (−13) = ①. Dann ① − (−6) = ① + 6 = ②. Dann ② − (−11) = ② + 11 = ③.",
    ["5-13", "5-13+6", "5-13+6+11"], ["-8", "-2", "9"], "Minus minus wird plus.", "5 − 13 = −8. −8 + 6 = −2. −2 + 11 = 9.",
    {0: [(8, "fb.plusminus.zeichen_des_ergebnisses", "das Minus vergessen")], 1: [(-14, "fb.plusminus.doppelminus_uebersehen", "Doppelminus übersehen: −8 − 6")]}), PM)
neu(TH, "subtrahieren", "zwei_wege", "mehrschritt", Z(
    "Berechne 4 − (−9) − 6. Weg A: von links nach rechts. Weg B: erst 4 − 6 = −2, dann (−2) − (−9). Wie groß ist das Ergebnis?",
    "4-(-9)-6", "(4-6)+9", "Minus minus ist plus. Beide Wege geben dieselbe Zahl.", "Weg A: 4 + 9 = 13, 13 − 6 = 7. Weg B: −2 + 9 = 7.",
    [(-11, "fb.plusminus.doppelminus_uebersehen", "Doppelminus übersehen"), (19, None, "6 addiert statt abgezogen")]), PM)
neu(TH, "subtrahieren", "anwenden", "einkleidung", Z(
    "Ein Taucher ist bei −18 m. Er steigt auf −7 m. Um wie viele Meter ist er gestiegen? Rechne Ende minus Anfang.",
    "-7-(-18)", "18-7", "Ende minus Anfang, also (−7) − (−18). Minus minus ist plus.", "(−7) − (−18) = −7 + 18 = 11. Er ist 11 m gestiegen.",
    [(-25, "fb.plusminus.doppelminus_uebersehen", "Doppelminus übersehen"), (-11, None, "falsch herum gerechnet")], einheit="m"), PM)

# ── umkehraufgabe ──
neu(TH, "umkehraufgabe", "fehler_detektiv", "fehler", FDZ(
    "Kim löst x + 7 = −3.",
    [("Die Umkehraufgabe von „plus 7“ ist „minus 7“.", True), ("Also ist x = −3 − 7.", True), ("Minus und Minus ergibt Plus, also rechne ich −3 + 7.", -3 - 7 == -3 + 7), ("Also ist x = 4.", True)],
    "Hier steht nur ein Minus vor der 7, die −3 ist negativ. Gilt „minus und minus ergibt plus“?", "Hier steht kein Doppelminus: −3 − 7 heißt von −3 sieben Schritte nach links: −10. Probe: (−10) + 7 = −3."), GR)
neu(TH, "umkehraufgabe", "verfahren_waehlen", "mehrschritt", W(
    "Du löst x − 5 = −8. Welcher Weg ist richtig?",
    "x = −8 + 5 = −3", [("x = −8 − 5 = −13", "die Umkehraufgabe nicht benutzt"), ("x = 8 + 5 = 13", "das Vorzeichen von −8 vergessen"), ("x = (−8) : 5", "Teilen statt Umkehren")],
    "Welche Rechnung macht „minus 5“ rückgängig?", "Minus 5 macht man mit plus 5 rückgängig: x = −8 + 5 = −3. Probe: (−3) − 5 = −8.",
    -3 - 5 == -8 and -8 - 5 != -8 + 5 and 8 + 5 != -3), GR)
neu(TH, "umkehraufgabe", "anwenden", "einkleidung", Z(
    "Morgens sind es 5 Grad unter null. Bis mittags steigt die Temperatur um einige Grad. Mittags zeigt das Thermometer 6 °C. Um wie viele Grad ist die Temperatur gestiegen?",
    "6-(-5)", "5+6", "Gesucht ist x in: −5 + x = 6. Kehre um.", "x = 6 − (−5) = 6 + 5 = 11. Probe: −5 + 11 = 6.",
    [(1, "fb.plusminus.doppelminus_uebersehen", "6 − 5 gerechnet"), (-11, None, "Vorzeichen falsch")], einheit="Grad"), GR)

# ── ketten ──
neu(TH, "ketten", "lueckenweg", "direkt", L(
    "Rechne −4 + 9 − (−3) − 10. Das Minus vor der Klammer wird zu plus: − (−3) = + 3. Plus-Zahlen: 9 + 3 = ①. Minus-Zahlen: 4 + 10 = ②. Ergebnis: ① − ② = ③.",
    ["9+3", "4+10", "9+3-(4+10)"], ["12", "14", "-2"], "Sammle erst alle Plus-Zahlen, dann alle Minus-Zahlen.", "Plus: 9 + 3 = 12. Minus: 4 + 10 = 14. 12 − 14 = −2.",
    {2: [(2, "fb.plusminus.zeichen_des_ergebnisses", "das Minus des Ergebnisses vergessen"), (-8, "fb.plusminus.doppelminus_uebersehen", "− (−3) als Minus gerechnet")]}), PM)
neu(TH, "ketten", "zwei_wege", "mehrschritt", Z(
    "Berechne 8 − (−5) + (−12) − 3. Weg A: von links nach rechts. Weg B: erst die Klammern auflösen zu 8 + 5 − 12 − 3. Wie groß ist das Ergebnis?",
    "8-(-5)+(-12)-3", "8+5-12-3", "Beide Wege geben dieselbe Zahl.", "Weg A: 8 + 5 = 13, 13 − 12 = 1, 1 − 3 = −2. Weg B: 13 − 15 = −2.",
    [(2, "fb.plusminus.zeichen_des_ergebnisses", "Vorzeichen des Ergebnisses vergessen"), (-12, "fb.plusminus.doppelminus_uebersehen", "Doppelminus übersehen")]), PM)
neu(TH, "ketten", "anwenden", "einkleidung", Z(
    "Dein Kontostand ist −20 €. Dann kommen 85 € Taschengeld dazu, 30 € werden abgebucht, 15 € werden gutgeschrieben und 40 € werden abgebucht. Wie hoch ist der Kontostand danach?",
    "-20+85-30+15-40", "(85+15)-(20+30+40)", "Sammle alles, was dazukommt, und alles, was abgeht.", "Dazu: 85 + 15 = 100. Weg: 20 + 30 + 40 = 90. 100 − 90 = 10 €.",
    [(-10, "fb.plusminus.zeichen_des_ergebnisses", "Vorzeichen des Ergebnisses falsch"), (30, None, "die Schulden vergessen")], einheit="€"), PM)

# ── verstehen ──
neu(TH, "verstehen", "fehler_detektiv", "fehler", FDZ(
    "Kim prüft die Aussage: „Wenn man etwas abzieht, wird das Ergebnis immer kleiner.“",
    [("Beispiel: 10 − 4 = 6. Das ist kleiner als 10.", 10 - 4 < 10), ("Noch ein Beispiel: 7 − 2 = 5. Das ist kleiner als 7.", 7 - 2 < 7), ("Beide Beispiele stimmen.", True), ("Weil zwei Beispiele stimmen, ist die Aussage bewiesen.", all(a - b < a for a in range(-5, 6) for b in range(-5, 6)))],
    "Probiere eine negative Zahl zum Abziehen, zum Beispiel 10 − (−4).", "Ein Gegenbeispiel widerlegt die Aussage: 10 − (−4) = 14 ist größer als 10. Beispiele allein beweisen nichts."), PM)
neu(TH, "verstehen", "verfahren_waehlen", "mehrschritt", W(
    "Du willst prüfen, ob die Aussage „a + b ist immer größer als a“ stimmt. Was ist der beste Weg?",
    "Ein Gegenbeispiel suchen, zum Beispiel mit negativem b: 5 + (−2) = 3",
    [("Viele Beispiele mit positiven Zahlen sammeln", "Beispiele ohne Gegenbeispiel beweisen nichts"), ("Nur den Fall b = 0 testen", "nur einen Sonderfall geprüft"), ("So lange rechnen, bis es stimmt", "kein Prüfverfahren")],
    "Ein einziges Gegenbeispiel genügt, um eine Aussage zu widerlegen.", "Mit b = −2: 5 + (−2) = 3 ist kleiner als 5. Die Aussage stimmt nicht immer.", 5 + -2 < 5), PM)
neu(TH, "verstehen", "umkehren", "umkehr", Z(
    "Kim behauptet: „a − 7 ist immer negativ.“ Für welche kleinste Zahl a (a = 0, 1, 2, …) stimmt das nicht mehr?",
    "7", str(next(a for a in range(0, 100) if a - 7 >= 0)), "Für welches a ist a − 7 gleich 0 oder größer?", "Für a = 6 ist 6 − 7 = −1. Für a = 7 ist 7 − 7 = 0. Null ist nicht negativ. Das kleinste Gegenbeispiel ist a = 7.",
    [(6, None, "die letzte passende Zahl genannt"), (8, None, "eine Zahl zu weit")]), PM)

# ── sach ──
neu(TH, "sach", "lueckenweg", "direkt", L(
    "Am Morgen sind es −6 °C. Bis mittags wird es 9 Grad wärmer: (−6) + 9 = ①. Am Abend wird es 5 Grad kälter: ① − 5 = ②.",
    ["-6+9", "-6+9-5"], ["3", "-2"], "Wärmer heißt plus, kälter heißt minus.", "−6 + 9 = 3. 3 − 5 = −2. Am Abend sind es −2 °C.",
    {1: [(2, "fb.plusminus.zeichen_des_ergebnisses", "das Minus des Ergebnisses vergessen")]}), PM)
neu(TH, "sach", "umkehren", "umkehr", Z(
    "Ein Taucher steigt 6 m auf und ist danach bei −11 m. Bei welcher Höhe war er vorher?",
    "-11-6", "-17", "Kehre das Aufsteigen um: Er war tiefer.", "Vorher war er 6 m tiefer: −11 − 6 = −17. Probe: −17 + 6 = −11.",
    [(-5, "fb.plusminus.zeichen_des_ergebnisses", "−11 + 6 gerechnet"), (17, None, "das Vorzeichen vergessen")], einheit="m"), PM)
neu(TH, "sach", "anwenden", "einkleidung", Z(
    "Ein Hochhaus hat drei Kellergeschosse (−3, −2, −1). Ein Aufzug startet im untersten Kellergeschoss (−3). Er fährt 8 Etagen hinauf, dann 5 Etagen hinunter und dann 2 Etagen hinauf. In welcher Etage hält er?",
    "-3+8-5+2", "-3+(8+2)-5", "Rechne Schritt für Schritt von der Startetage aus.", "−3 + 8 = 5. 5 − 5 = 0. 0 + 2 = 2. Er hält in Etage 2.",
    [(5, None, "den Start als 0 gerechnet"), (18, None, "alle Zahlen addiert")]), PM)
