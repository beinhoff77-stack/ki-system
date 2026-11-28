T = "bruch.prozent_grundwert"
P = "id.verhaeltnisse.prozent"
GEG = "rr.gegenrechnung"
# ───────── faktor ─────────
neu(T, "faktor", "anwenden", Z(
    "Ein Hostel in Lissabon verlangt in der Hauptsaison 18 % mehr als in der Nebensaison. Ein Gast will den Hauptsaison-Preis aus dem Nebensaison-Preis ausrechnen: Preis · Faktor. Welchen Faktor setzt er ein?",
    1.18, "1 + 18 / 100", "118 / 100", "Der alte Preis bleibt voll erhalten (100 %). Dazu kommen die 18 %.",
    "Der alte Preis ist 100 %. Dazu kommen 18 %: 100 % + 18 % = 118 %. Als Faktor schreibt man 118 : 100 = 1,18.",
    [B("18 / 100", "nur die 18 % als Faktor geschrieben (die 100 % vom alten Preis vergessen)"), B("1 - 18 / 100", "den Faktor einer Abnahme genommen statt den einer Zunahme"), B("1 + 18 / 1000", "18 % als 0,018 geschrieben")]), g="einkleidung", regel=P)
neu(T, "faktor", "fehler_detektiv", FD(
    "Ein Reiseveranstalter senkt den Preis einer Tour um 12 %. Kim bestimmt den Faktor und rechnet damit einen Preis aus.",
    [("Bei 12 % weniger bleiben 100 % − 12 % = 88 % übrig.", 100 - 12 == 88, True),
     ("88 % sind der Faktor 0,088.", 88 / 100 == 0.088, True),
     ("Eine Tour, die vorher 450 € kostete, kostet jetzt 450 · 0,088 = 39,60 €.", round(450 * 0.088, 2) == 39.6, round(450 * 0.088, 2) == 39.6)],
    "Wie viele Hundertstel sind 88 %? Schreibe 88 : 100 als Dezimalzahl.",
    "88 % sind 88 : 100 = 0,88, nicht 0,088. Der Fehler steckt in Zeile 2. Zeile 3 rechnet mit dem falschen Faktor richtig weiter. Richtig ist 450 · 0,88 = 396 €."), g="fehler", regel=P)
# ───────── vermehrt ─────────
neu(T, "vermehrt", "anwenden", Z(
    "Der Grundpreis für einen Mietwagen auf Sizilien beträgt 320 € für die Woche. Für einen Zusatzfahrer kommen 15 % des Grundpreises dazu, für die Vollkasko-Versicherung noch einmal 8 % des Grundpreises. Wie viel Euro kostet der Wagen insgesamt?",
    393.6, "320 * (1 + 15 / 100 + 8 / 100)", "320 + 320 * 0.15 + 320 * 0.08", "Beide Zuschläge sind Prozente vom Grundpreis (320 €), nicht vom schon erhöhten Preis.",
    "Beide Zuschläge beziehen sich auf 320 €: 15 % von 320 € sind 48 €, 8 % von 320 € sind 25,60 €. Zusammen: 320 + 48 + 25,60 = 393,60 €. Mit Faktor: 320 · 1,23 = 393,60 €.",
    [B("320 * 1.15 * 1.08", "die zweite Erhöhung auf den schon erhöhten Preis gerechnet"), B("320 * 1.15", "nur den ersten Zuschlag gerechnet"), B("320 + 15 + 8", "die Prozentzahlen als Euro addiert")], einheit="€"), g="mehrschritt", regel=P)
neu(T, "vermehrt", "anwenden", Z(
    "Auf einem Markt in Istanbul nennt ein Händler für einen Teppich 480 Lira. Für Touristen schlägt er 25 % auf. Kim rechnet mit dem Kurs 1 € = 40 Lira. Wie viel Euro muss Kim mit dem Touristen-Aufschlag zahlen?",
    15, "480 * 1.25 / 40", "(480 + 480 * 25 / 100) / 40", "Rechne zuerst in Lira, dann in Euro um.",
    "Der Preis mit Aufschlag ist 480 · 1,25 = 600 Lira. Bei 40 Lira je Euro sind das 600 : 40 = 15 €.",
    [B("480 / 40", "den Aufschlag vergessen"), B("480 * 1.25", "nicht in Euro umgerechnet"), B("480 * 1.25 * 40", "beim Umrechnen malgenommen statt geteilt")], einheit="€"), g="verknuepfen", regel=P)
# ───────── vermindert ─────────
neu(T, "vermindert", "anwenden", Z(
    "Ein Skiverleih berechnet 28 € je Tag. Ab dem vierten Tag gibt es 30 % Nachlass auf den Tagespreis. Familie Berger leiht die Ausrüstung für 6 Tage. Wie viel Euro zahlt sie insgesamt?",
    142.8, "3 * 28 + 3 * 28 * 0.7", "6 * 28 - 3 * 28 * 30 / 100", "Drei Tage kosten den vollen Preis. Für die anderen Tage gilt der Rest-Anteil von 70 %.",
    "Tage 1 bis 3: 3 · 28 € = 84 €. Ab Tag 4 zahlt man 70 % von 28 €, das sind 19,60 € je Tag. Für 3 Tage: 58,80 €. Zusammen: 84 + 58,80 = 142,80 €.",
    [B("6 * 28 * 0.7", "den Nachlass auf alle 6 Tage gerechnet"), B("3 * 28 * 0.7", "nur die ermäßigten Tage gerechnet"), B("6 * 28 - 30", "30 € statt 30 % abgezogen")], einheit="€"), g="mehrschritt", regel=P)
neu(T, "vermindert", "zwei_wege", Z(
    "Ein Rucksack kostet 85 € und wird um 35 % reduziert. Berechne den neuen Preis auf zwei Wegen. Weg A: Rabatt in Euro ausrechnen und abziehen. Weg B: den Preis mit dem Rest-Anteil malnehmen. Wie viel Euro kostet der Rucksack jetzt?",
    55.25, "85 * 0.65", "85 - 85 * 35 / 100", "Weg B: Wie viel Prozent vom alten Preis bleiben nach 35 % Rabatt übrig?",
    "Weg A: 35 % von 85 € sind 29,75 €. 85 − 29,75 = 55,25 €. Weg B: 100 % − 35 % = 65 %, also 85 · 0,65 = 55,25 €. Beide Wege ergeben 55,25 €.",
    [B("85 * 0.35", "den Rabatt als neuen Preis genommen"), B("85 * 1.35", "35 % aufgeschlagen statt abgezogen"), B("85 - 35", "35 € statt 35 % abgezogen")], einheit="€"), g="mehrschritt", regel=P)
# ───────── zurueck ─────────
neu(T, "zurueck", "umkehren", Z(
    "In einem Hotel in Split kostet ein Zimmer inklusive 8 % Ortstaxen-Zuschlag 162 € je Nacht. Wie viel Euro kostet das Zimmer ohne den Zuschlag?",
    150, "162 / 1.08", "162 * 100 / 108", "Der Preis mit Zuschlag ist 108 % vom Preis ohne Zuschlag. Wie kommst du von 108 % zurück auf 100 %?",
    "Der Preis mit Zuschlag ist 108 % des ursprünglichen Preises, also Preis · 1,08 = 162 €. Zurück geht es durch Teilen: 162 : 1,08 = 150 €.",
    [B("162 * 0.92", "8 % vom Endpreis abgezogen"), B("162 - 8", "8 € statt 8 % abgezogen"), B("162 * 1.08", "noch einmal 8 % aufgeschlagen")], einheit="€"), g="umkehr", regel=GEG,
    zweifel="Rückwärts durch den Faktor teilen: rr.gegenrechnung (Umkehr des Malnehmens); id.verhaeltnisse.prozent wäre ebenfalls vertretbar")
neu(T, "zurueck", "anwenden", W(
    "Ticket A kostet nach einem Aufschlag von 20 % jetzt 60 €. Ticket B kostet nach einem Rabatt von 20 % jetzt 60 €. Welche Aussage stimmt?",
    "Ticket B war vorher teurer: 75 € gegenüber 50 €.",
    [("Ticket A war vorher teurer: 75 € gegenüber 50 €.", "Aufschlag und Rabatt vertauscht"), ("Beide Tickets kosteten vorher gleich viel, denn 20 % mehr und 20 % weniger gleichen sich aus.", "die Prozente einfach gegeneinander aufgerechnet"),
     ("Ticket B war vorher teurer: 72 € gegenüber 48 €.", "20 % vom Endpreis statt durch den Faktor zurückgerechnet")],
    "Zum Zurückrechnen brauchst du jeweils den Faktor: nach Aufschlag und nach Rabatt ist er verschieden.",
    "Ticket A: Preis · 1,2 = 60 €, also Preis = 60 : 1,2 = 50 €. Ticket B: Preis · 0,8 = 60 €, also Preis = 60 : 0,8 = 75 €. B war vorher teurer.",
    lambda: 60 / 1.2 == 50 and 60 / 0.8 == 75 and 60 + 60 * 0.2 == 72 and 60 - 60 * 0.2 == 48), g="transfer", regel=GEG,
    zweifel="Rückwärts durch den Faktor teilen: rr.gegenrechnung; id.verhaeltnisse.prozent wäre ebenfalls vertretbar")
# ───────── prozentsatz ─────────
neu(T, "prozentsatz", "anwenden", Z(
    "Im Mai bekam man für 100 € auf einer Reise 4 300 Baht. Im Juli waren es nur noch 4 085 Baht. Um wie viel Prozent ist der Baht-Betrag für 100 € gesunken?",
    5, "(4300 - 4085) / 4300 * 100", "100 - 4085 / 4300 * 100", "Vergleiche die Änderung mit dem Wert vom Mai, nicht mit dem vom Juli.",
    "Die Änderung ist 4 300 − 4 085 = 215 Baht. Bezogen auf den alten Wert: 215 : 4 300 = 0,05 = 5 %. Der Betrag ist um 5 % gesunken.",
    [B("(4300 - 4085) / 4085 * 100", "die Änderung auf den neuen statt auf den alten Wert bezogen", "fb.prozent.falscher_grundwert"), B("4300 - 4085", "den Unterschied in Baht als Prozent angegeben"), B("4085 / 4300 * 100", "den neuen Wert in Prozent des alten angegeben (95 %)")], einheit="%"), g="einkleidung", regel=P)
neu(T, "prozentsatz", "bruecke", W(
    "In der Tabelle stehen alter und neuer Preis von drei Angeboten auf einer Reise. Bei welchem Angebot ist die Preiserhöhung in Prozent am größten?",
    "beim Bus", [("beim Hotel, weil dort die Erhöhung in Euro am größten ist", "den Unterschied in Euro statt in Prozent verglichen"), ("beim Museum, weil es mit 3 € mehr steigt als der Bus (0,60 €) und im Verhältnis zum Preis mehr als das Hotel", "Bus und Museum nur in Euro verglichen und das Verhältnis zum alten Preis beim Bus nicht berechnet")],
    "Berechne für jede Zeile: Änderung geteilt durch den alten Preis.",
    "Bus: 0,60 : 2,40 = 25 %. Museum: 3 : 15 = 20 %. Hotel: 9 : 90 = 10 %. Die größte Erhöhung in Prozent hat der Bus, auch wenn sie in Euro am kleinsten ist.",
    lambda: round(0.6 / 2.4, 4) == 0.25 and 3 / 15 == 0.2 and 9 / 90 == 0.1 and 9 > 3 > 0.6,
    grafik=TAB(["Angebot", "alter Preis", "neuer Preis"], ["Bus", "2,40 €", "3,00 €"], ["Museum", "15 €", "18 €"], ["Hotel", "90 €", "99 €"])), g="verknuepfen", regel=P)
# ───────── mehrfach ─────────
neu(T, "mehrfach", "anwenden", Z(
    "Die Fähre nach Sardinien kostet für das Auto 480 €. Wegen der Hochsaison steigt der Preis zuerst um 12 %. Auf diesen neuen Preis kommen für die Stornoversicherung noch einmal 5 %. Wie viel Euro kostet die Überfahrt insgesamt?",
    564.48, "480 * 1.12 * 1.05", "480 * 1.12 + 480 * 1.12 * 0.05", "Die zweite Erhöhung bezieht sich auf den schon erhöhten Preis. Nimm beide Faktoren mal.",
    "Nach der ersten Erhöhung: 480 · 1,12 = 537,60 €. Darauf 5 %: 537,60 · 1,05 = 564,48 €. Man darf die Prozente nicht addieren (17 % wären nur 561,60 €).",
    [B("480 * 1.17", "die Prozentsätze 12 und 5 addiert, obwohl die zweite Erhöhung vom neuen Preis gilt", "fb.prozent.prozente_addiert"), B("480 * 1.12", "nur die erste Erhöhung gerechnet"), B("537.6 + 5", "5 € statt 5 % aufgeschlagen")], einheit="€"), g="mehrschritt", regel=P)
wert_mf, c_mf = rd("(1 - 1 / 1.2) * 100", 1)
neu(T, "mehrfach", "umkehren", Z(
    "Ein Preis steigt zuerst um 20 %. Danach soll er um einen Prozentsatz sinken, sodass er wieder genau so hoch ist wie am Anfang. Um wie viel Prozent muss er sinken? Runde auf eine Dezimalstelle.",
    wert_mf, c_mf, "round(100 - 100 / 1.2, 1)", "Nach der Erhöhung ist der Preis das 1,2-Fache. Mit welchem Faktor kommst du von 1,2 zurück auf 1?",
    "Nach der Erhöhung gilt: Preis · 1,2. Gesucht ist der Faktor q mit 1,2 · q = 1, also q = 1 : 1,2 ≈ 0,8333. Das ist eine Abnahme um 1 − 0,8333 = 0,1667, also etwa 16,7 %.",
    [B("20", "angenommen, dieselben 20 % machen die Erhöhung wieder rückgängig", "fb.prozent.prozente_addiert"), (83.3, None, "den verbleibenden Anteil (83,3 %) statt der Abnahme angegeben", "round(100 / 1.2, 1)"), (1.2, None, "den Faktor 1,2 als Prozentsatz gelesen", "1.2")], einheit="%"), g="rueckwaerts", regel=P)
# ───────── formel ─────────
neu(T, "formel", "zwei_wege", Z(
    "Kim legt 5 000 € für 3 Jahre zu 4 % Zinsen im Jahr an. Die Zinsen bleiben auf dem Konto und werden mitverzinst. Berechne das Guthaben nach 3 Jahren auf zwei Wegen. Weg A: Jahr für Jahr mit 1,04 malnehmen. Weg B: mit 1,04³. Runde auf Cent. Wie viel Euro sind es?",
    5624.32, "5000 * 1.04 ** 3", "round(5000 * 1.04 * 1.04 * 1.04, 2)", "Weg A und Weg B müssen dasselbe ergeben. Wie oft kommt der Faktor 1,04 vor?",
    "Weg A: 5 000 · 1,04 = 5 200; 5 200 · 1,04 = 5 408; 5 408 · 1,04 = 5 624,32. Weg B: 5 000 · 1,04³ = 5 000 · 1,124864 = 5 624,32 €.",
    [B("5000 * 1.12", "die Zinssätze der drei Jahre addiert statt dreimal mit 1,04 malgenommen"), B("5000 * 1.04 * 3", "den Faktor 1,04 mit 3 malgenommen statt hoch 3"), B("5000 * 1.4 ** 3", "4 % als Faktor 1,4 geschrieben")], einheit="€"), g="mehrschritt", regel=P)
n_j = next(n for n in range(1, 40) if 2000 * 1.05 ** n > 2500)
neu(T, "formel", "umkehren", Z(
    "Ein Guthaben von 2 000 € wird mit 5 % Zinseszins im Jahr angelegt. Nach wie vielen vollen Jahren ist das Guthaben zum ersten Mal höher als 2 500 €?",
    n_j, "5", n_j, "Probiere die Jahre nacheinander aus: 2 000 · 1,05, dann · 1,05², und so weiter. Wann liegt das Ergebnis erstmals über 2 500?",
    "Nach 4 Jahren: 2 000 · 1,05⁴ ≈ 2 431,01 €, das reicht noch nicht. Nach 5 Jahren: 2 000 · 1,05⁵ ≈ 2 552,56 €. Das ist höher als 2 500 €. Es sind 5 Jahre.",
    [B("4", "schon nach 4 Jahren gestoppt: dann sind es erst etwa 2 431 €"), B("6", "ohne Zinseszins gerechnet (nur 100 € Zinsen je Jahr): nach 5 Jahren sind es dann erst genau 2 500 €")], einheit="Jahre"), g="rueckwaerts", regel=P)
# ───────── argumente ─────────
neu(T, "argumente", "anwenden", W(
    "Eine Stadt am Mittelmeer hatte im Vorjahr 200 000 Übernachtungen und dieses Jahr 230 000. Eine kleine Insel hatte im Vorjahr 50 000 und dieses Jahr 62 000. Welche Aussage vergleicht das relative Wachstum (den prozentualen Zuwachs) von Stadt und Insel richtig?",
    "Die Insel ist prozentual stärker gewachsen: 12 000 : 50 000 = 24 %, in der Stadt sind es 30 000 : 200 000 = 15 %.",
    [("Die Stadt ist stärker gewachsen, denn 30 000 ist mehr als 12 000.", "den Zuwachs in Übernachtungen statt in Prozent verglichen"), ("Beide sind gleich stark gewachsen, denn jeweils kamen etwa ein Fünftel mehr Übernachtungen dazu.", "ungefähr geschätzt statt gerechnet")],
    "Ein Vergleich in Prozent braucht jeweils den Zuwachs geteilt durch den Wert des Vorjahrs.",
    "Stadt: 230 000 − 200 000 = 30 000, das sind 30 000 : 200 000 = 15 %. Insel: 62 000 − 50 000 = 12 000, das sind 12 000 : 50 000 = 24 %. Die Insel ist prozentual stärker gewachsen.",
    lambda: 30000 / 200000 == 0.15 and 12000 / 50000 == 0.24), g="pruefung", regel=P)
neu(T, "argumente", "verfahren_waehlen", W(
    "Ein Ticket kostet 50 €. Der Preis steigt um 40 % und sinkt später um 40 %. Ein Reiseblogger schreibt: „Dann ist es wieder so billig wie am Anfang.“ Welche Rechnung prüft die Aussage richtig?",
    "50 · 1,4 · 0,6 = 42, also kostet das Ticket am Ende weniger als am Anfang.",
    [("50 + 40 − 40 = 50, also stimmt die Aussage.", "Prozente wie Euro addiert und subtrahiert"), ("50 · 1,4 · 1,4 = 98, also kostet das Ticket am Ende mehr.", "beide Male mit dem Faktor einer Zunahme gerechnet"), ("50 · 0,4 · 0,4 = 8, also kostet das Ticket nur noch 8 €.", "mit den Prozentwerten statt mit den Faktoren gerechnet")],
    "Prüfe die Aussage mit einer Rechnung: Die zweite Änderung gilt für den neuen, nicht für den alten Preis.",
    "Nach +40 % kostet es 50 · 1,4 = 70 €. Nach −40 % davon: 70 · 0,6 = 42 €. Das ist weniger als 50 €. Die Aussage ist falsch, weil sich die 40 % auf verschiedene Grundwerte beziehen.",
    lambda: round(50 * 1.4 * 0.6, 6) == 42 and 50 + 40 - 40 == 50 and round(50 * 1.4 * 1.4, 6) == 98 and round(50 * 0.4 * 0.4, 6) == 8), g="pruefung", regel=P)
