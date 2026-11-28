T = "bruch.prozent"
LP = "M6 3 Prozentrechnung (Prozentsatz, Prozentwert, Grundwert; Rabatt und Aufschlag)"
ABG[(T, "prozentsatz")] = "Die Übungen berechnen einen Prozentsatz vorwärts; hier muss entschieden werden, worauf sich die Prozente beziehen (Grundwert) oder der Ansatz umgekehrt gelesen werden."
ABG[(T, "rabatt_aufschlag")] = "Die Übungen rechnen Rabatt oder Aufschlag in einem Schritt; hier geht es um den Bezugswert, hintereinander ausgeführte Änderungen und das Rückwärtsrechnen auf den alten Preis."
ABG[(T, "verstehen")] = "Die Übungen rechnen mit Prozenten; hier wird begründet, warum Prozentzahlen nur Anteile vergleichen und Auf- und Abstieg nicht dieselbe Prozentzahl haben."
IDEEN[(T, "prozentsatz")] = ['begruenden_ablenker', 'umkehr', 'groessenvergleich', 'darstellung_wechseln', 'fehler_finden_richtigstellen', 'modell_aufstellen', 'darstellung_wechseln']
IDEEN[(T, "rabatt_aufschlag")] = ['fehler_finden_richtigstellen', 'umkehr', 'modell_aufstellen', 'darstellung_wechseln', 'zwei_wege', 'bezugswert_erkennen', 'hintereinander_ausfuehren']
IDEEN[(T, "verstehen")] = ['begruenden_ablenker', 'prozent_vs_faktor', 'darstellung_wechseln', 'anteil_von_anteil', 'gegenbeispiel', 'modell_aufstellen', 'umkehr']
# ───────── prozentsatz ─────────
neu(T, "prozentsatz", "test", "begruenden", W(
    "Ein Verein hatte letztes Jahr 40 Mitglieder, dieses Jahr sind es 50. Welche Aussage über die Prozentzahlen ist richtig?",
    "Die Mitgliederzahl ist um 25 % gestiegen (10 von 40). Wäre sie umgekehrt von 50 auf 40 gesunken, wäre das ein Rückgang um 20 % (10 von 50).",
    [("Die Mitgliederzahl ist um 25 % gestiegen (10 von 40). Wäre sie umgekehrt von 50 auf 40 gesunken, wäre das ebenfalls ein Rückgang um 25 %, denn es sind wieder 10 Mitglieder.",
      "den Grundwert nicht gewechselt: Beim Rückgang von 50 auf 40 ist der Grundwert 50, nicht 40"),
     ("Die Mitgliederzahl ist um 20 % gestiegen, denn 10 der jetzt 50 Mitglieder sind neu (10 von 50).",
      "den neuen Wert 50 als Grundwert genommen; die Änderung bezieht sich auf die 40 Mitglieder vom letzten Jahr"),
     ("Die Mitgliederzahl ist um 10 % gestiegen, denn es sind 10 Mitglieder mehr.",
      "die 10 Mitglieder mehr als Prozentzahl gelesen, ohne sie ins Verhältnis zum Grundwert zu setzen")],
    "Eine prozentuale Änderung bezieht sich immer auf den Ausgangswert, also den Wert vor der Änderung (den Grundwert). Hinweg: Die Zunahme ist 10 Mitglieder, der Grundwert 40, also 10 : 40 = 0,25 = 25 %. "
    "Rückweg: Bei einer Abnahme von 50 auf 40 ist der Ausgangswert 50, also 10 : 50 = 0,2 = 20 %. Die Änderung ist beide Male 10 Mitglieder, aber der Grundwert ist ein anderer; deshalb sind die Prozentsätze verschieden.",
    lambda: F(50 - 40, 40) == F(1, 4) and F(50 - 40, 50) == F(1, 5) and F(10, 50) != F(1, 4) and F(10, 100) != F(10, 40)), lp=LP)
neu(T, "prozentsatz", "korrektur", "umkehr", Z(
    "Für ein Sportabzeichen muss man bei einem Quiz mit 40 Fragen mindestens 85 % der Fragen richtig beantworten. Wie viele Fragen müssen es mindestens sein?",
    34, "0.85 * 40", "40 - 40 * 15 / 100",
    "Gesucht ist der Prozentwert zu 85 % von 40 Fragen: 85 % = 0,85 und 0,85 · 40 = 34. Probe: 34 von 40 sind 34 : 40 = 0,85 = 85 %. Weil genau 85 % herauskommen, reichen 34 Fragen; mit 33 Fragen wären es nur 82,5 %.",
    [B("15 / 100 * 40", "15 % von 40 gerechnet, also die erlaubten Fehler statt der richtigen Antworten"),
     B("0.85 * 40 + 1", "34 + 1 gerechnet, weil »mindestens« mit »mehr als« verwechselt wurde"),
     B("85 / 40", "85 durch 40 geteilt, statt 85 % von 40 zu bilden")], einheit="Fragen"), form="umkehren", lp=LP)
neu(T, "prozentsatz", "korrektur", "einkleidung", Z(
    "Im Mai-Test löst Tom 18 von 24 Aufgaben richtig, im Juni-Test 27 von 30 Aufgaben. Um wie viele Prozentpunkte ist sein Anteil richtiger Aufgaben im Juni höher als im Mai? (Prozentpunkte: der Unterschied der beiden Prozentzahlen.)",
    15, "27 / 30 * 100 - 18 / 24 * 100", "90 - 75",
    "Mai: 18 : 24 = 0,75 = 75 %. Juni: 27 : 30 = 0,9 = 90 %. Der Unterschied der Prozentzahlen ist 90 − 75 = 15 Prozentpunkte. Die richtigen Aufgaben allein (27 gegen 18) sagen nichts, weil die Tests verschieden lang waren.",
    [B("27 - 18", "die Anzahlen richtiger Aufgaben statt der Anteile verglichen: 27 − 18"),
     B("18 / 24 * 100 + 27 / 30 * 100", "die beiden Prozentzahlen addiert, statt ihren Unterschied zu bilden"),
     B("27 / 30 - 18 / 24", "die Anteile als Dezimalzahlen abgezogen und nicht in Prozent umgewandelt: 0,9 − 0,75")], einheit="Prozentpunkte"), form="bruecke", lp=LP)
neu(T, "prozentsatz", "sicherung", "darstellung", W(
    "Von 40 befragten Kindern lesen 14 jeden Tag. Drei der folgenden vier Angaben beschreiben genau diesen Anteil. Welche Angabe beschreibt einen anderen Anteil?",
    "14 %",
    [("7/20", "7/20 ist 14/40 gekürzt und beschreibt denselben Anteil wie 14 von 40; gesucht ist aber die Ausnahme"),
     ("0,35", "0,35 ist 14 : 40 als Dezimalzahl und beschreibt denselben Anteil; gesucht ist aber die Ausnahme"),
     ("35 %", "35 % ist 14 : 40 = 0,35 in Prozent und beschreibt denselben Anteil; gesucht ist aber die Ausnahme")],
    "Der Anteil ist 14 von 40, also 14 : 40 = 0,35 = 35 %. Als Bruch 14/40 = 7/20. Damit beschreiben 7/20, 0,35 und 35 % den Anteil. Die Angabe 14 % ist 14/100 und damit nur ein kleinerer Anteil: Die Zahl 14 der Kinder darf nicht ohne Bezug auf die 40 Kinder zur Prozentzahl gemacht werden.",
    lambda: F(14, 40) == F(7, 20) == F(35, 100) == F("0.35") != F(14, 100)), form="bruecke", lp=LP)
neu(T, "prozentsatz", "sicherung", "fehler", L(
    "Anna soll berechnen, wie viel Prozent der 25 Kinder einer Klasse ein Haustier haben; 20 Kinder haben eines. Sie schreibt: Zeile 1: Das Ganze sind 25 Kinder, der Teil sind 20 Kinder. Zeile 2: Prozentsatz = Ganzes : Teil = 25 : 20 = 1,25. Zeile 3: Also haben 125 % der Kinder ein Haustier. In welcher Zeile steckt der erste Fehler, und wie viel Prozent der Kinder haben richtig ein Haustier?",
    "Fehler in Zeile □, richtig: □ %", [2, 80], ["2", "20 / 25 * 100"], ["3 - 1", "4 * 20"],
    "Der Prozentsatz ist Teil durch Ganzes, nicht Ganzes durch Teil. Zeile 1 ist richtig (Ganzes 25, Teil 20). In Zeile 2 sind Ganzes und Teil vertauscht: richtig ist 20 : 25 = 0,8 = 80 %. Das Ergebnis 125 % ist ein Warnzeichen, denn ein Anteil an der Klasse kann nicht über 100 % liegen.",
    {1: [(125, "wie Anna Ganzes durch Teil gerechnet: 25 : 20 · 100", "25 / 20 * 100"), (20, "die 5 Kinder ohne Haustier genommen: 5 : 25 · 100", "5 / 25 * 100"), (5, "den Unterschied 25 − 20 als Prozentzahl gelesen", "25 - 20")]}), form="fehler_detektiv", lp=LP)
neu(T, "prozentsatz", "sicherung", "transfer", Z(
    "In einer Gruppe sind 18 von 30 Kindern Mädchen. Es kommen noch 10 Kinder dazu. Wie viele dieser 10 Kinder müssen Mädchen sein, damit der Anteil der Mädchen in der Gruppe genau gleich bleibt?",
    6, "18 / 30 * (30 + 10) - 18", "10 * 18 / 30",
    "Der Mädchenanteil ist 18 von 30, das sind 60 %. Nach dem Zuzug sind es 40 Kinder, und 60 % von 40 sind 24 Mädchen. Es waren schon 18, also müssen 24 − 18 = 6 Mädchen dazukommen. Kürzer: 60 % von den 10 neuen Kindern sind 6.",
    [B("18 / 30 * (30 + 10)", "60 % von 40 gerechnet, aber die 18 Mädchen nicht abgezogen"),
     B("(1 - 18 / 30) * 10", "40 % von 10 gerechnet, also den Anteil der Jungen statt der Mädchen"),
     B("18 / 30 * 10 + 18 / 30 * 10", "den Anteil 60 % von 10 zweimal gezählt")], einheit="Mädchen"), lp=LP)
# ───────── rabatt_aufschlag ─────────
neu(T, "rabatt_aufschlag", "test", "fehler", L(
    "Auf einem Schild steht: „Jetzt 25 % billiger – nur noch 150 €!“ Ben will den alten Preis ausrechnen und schreibt: Zeile 1: Der alte Preis wurde um 25 % gesenkt. Zeile 2: Also ist der alte Preis der neue Preis plus 25 % davon, also 150 · 1,25. Zeile 3: 150 · 1,25 = 187,5, der alte Preis war 187,50 €. In welcher Zeile steckt der erste Fehler, und wie viel Euro kostete der Artikel vorher richtig?",
    "Fehler in Zeile □, richtig: □ €", [2, 200], ["2", "150 / 0.75"], ["3 - 1", "150 * 4 / 3"],
    "Der alte Preis ist der Grundwert (100 %). Nach 25 % Rabatt zahlt man noch 75 %, also sind 150 € = 75 % des alten Preises: 1 % sind 2 €, 100 % sind 200 €. Zeile 1 ist richtig. Zeile 2 ist der Fehler: Die 25 % gelten vom alten Preis, nicht vom neuen Preis 150 €. "
    "Zeile 3 rechnet mit dem falschen Ansatz richtig weiter. Probe: 25 % von 200 € sind 50 €, und 200 € − 50 € = 150 €.",
    {1: [(187.5, "wie Ben 25 % auf den neuen Preis aufgeschlagen: 150 · 1,25", "150 * 1.25"), (112.5, "den Rabatt noch einmal vom neuen Preis abgezogen: 150 · 0,75", "150 * 0.75"), (175, "die 25 % als 25 € gelesen und addiert: 150 + 25", "150 + 25")]}), form="fehler_detektiv", lp=LP)
neu(T, "rabatt_aufschlag", "korrektur", "umkehr", Z(
    "Zum Saisonende wird ein Zelt um 35 % billiger. Es kostet jetzt 117 €. Wie viel Euro kostete es vorher?",
    180, "117 / 0.65", "117 / 65 * 100",
    "Das Zelt kostet nach 35 % Rabatt noch 100 % − 35 % = 65 % des alten Preises. 65 % sind 117 €, also ist 1 % gleich 117 € : 65 = 1,80 € und 100 % sind 180 €. Probe: 35 % von 180 € sind 63 €, und 180 € − 63 € = 117 €.",
    [B("117 * 1.35", "35 % auf den neuen Preis aufgeschlagen, obwohl die 35 % vom alten Preis gelten"),
     B("117 + 35", "die 35 % als 35 € gelesen und zum neuen Preis addiert"),
     B("117 * 0.65", "noch einmal 35 % abgezogen, statt den alten Preis zu suchen")], einheit="€"), form="umkehren", lp=LP)
neu(T, "rabatt_aufschlag", "korrektur", "mehrschritt", Z(
    "Ein Sofa kostet bei Barzahlung 840 €. Beim Ratenkauf kommen 12 % Aufschlag auf den Preis dazu, und man zahlt in 6 gleich hohen Monatsraten. Wie hoch ist eine Monatsrate in Euro?",
    156.8, "840 * 1.12 / 6", "(840 + 840 * 12 / 100) / 6",
    "Aufschlag: 12 % von 840 € sind 100,80 €. Der Gesamtpreis beim Ratenkauf ist 840 € + 100,80 € = 940,80 € (112 % von 840 €). Verteilt auf 6 Raten: 940,80 € : 6 = 156,80 €.",
    [B("840 * 1.12", "den Gesamtpreis 940,80 € angegeben und nicht auf 6 Raten verteilt"),
     B("840 / 6", "ohne den Aufschlag gerechnet: 840 : 6"),
     B("840 * 12 / 100 / 6", "nur den Aufschlag (100,80 €) auf die 6 Raten verteilt")], einheit="€"), form="bruecke", lp=LP)
neu(T, "rabatt_aufschlag", "sicherung", "darstellung", W(
    "Ein Händler schreibt auf ein Plakat: „Alle Preise werden mit dem Faktor 0,92 malgenommen.“ Was bedeutet das für die Kunden?",
    "Alle Waren werden um 8 % billiger (92 % des alten Preises).",
    [("Alle Waren werden um 92 % billiger.", "den Faktor als Rabatt gelesen: 0,92 sind 92 % des Preises, die man noch zahlt, nicht der Rabatt"),
     ("Alle Waren werden um 8 % teurer.", "Faktor kleiner als 1 mit Aufschlag verwechselt; ein Faktor unter 1 verkleinert den Preis"),
     ("Von jedem Preis werden 0,92 € abgezogen.", "den Faktor als Eurobetrag gelesen; er wird mit dem Preis malgenommen, nicht abgezogen")],
    "Der Faktor 0,92 sind 92 %. Man zahlt also noch 92 % des alten Preises, das heißt, der Preis sinkt um 100 % − 92 % = 8 %. Beispiel: 100 € · 0,92 = 92 €, also 8 € billiger. Ein Faktor unter 1 bedeutet Rabatt, ein Faktor über 1 Aufschlag.",
    lambda: 100 * F(92, 100) == 92 and 100 - 92 == 8 and F("0.92") < 1), form="bruecke", lp=LP)
neu(T, "rabatt_aufschlag", "sicherung", "verknuepfen", Z(
    "Für denselben Fernseher verlangt Laden A 600 € und gibt darauf 20 % Rabatt. Laden B verlangt 620 €, aber man zahlt nur 3/4 des Preises. Um wie viel Euro ist das günstigere Angebot billiger?",
    15, "600 * 0.8 - 620 * 3 / 4", "480 - 465",
    "Laden A: 20 % Rabatt, man zahlt 80 % von 600 € = 480 €. Laden B: 3/4 sind 75 %, also 25 % Rabatt; man zahlt 3/4 von 620 € = 465 €. Laden B ist günstiger, und zwar um 480 € − 465 € = 15 €. Der höhere Listenpreis von B täuscht.",
    [B("620 - 600", "nur die Listenpreise verglichen: 620 − 600"),
     B("600 * 0.2", "nur den Rabatt von Laden A (20 % von 600 €) genommen"),
     B("620 * 0.25", "nur den Rabatt von Laden B (25 % von 620 €) genommen")], einheit="€"), form="zwei_wege", lp=LP)
neu(T, "rabatt_aufschlag", "sicherung", "transfer", Z(
    "Ein Händler kauft Skier für 96 € ein und verkauft sie für 120 €. Wie viel Prozent Aufschlag hat er auf den Einkaufspreis genommen?",
    25, "(120 - 96) / 96 * 100", "120 / 96 * 100 - 100",
    "Der Einkaufspreis 96 € ist der Grundwert. Der Aufschlag ist 120 € − 96 € = 24 €. Der Prozentsatz ist 24 : 96 = 0,25 = 25 %. Probe: 25 % von 96 € sind 24 €.",
    [B("(120 - 96) / 120 * 100", "den Aufschlag auf den Verkaufspreis 120 € bezogen statt auf den Einkaufspreis"),
     B("120 - 96", "den Aufschlag in Euro (24) als Prozentzahl hingeschrieben"),
     B("120 / 96 * 100", "den Verkaufspreis als Prozentsatz vom Einkaufspreis genommen (125 %), ohne die 100 % abzuziehen")], einheit="%"), lp=LP)
# ───────── verstehen ─────────
neu(T, "verstehen", "test", "begruenden", W(
    "Ein Händler A wirbt: „Bei uns sind alle Preise 50 % niedriger als bei Händler B.“ Welche Aussage folgt daraus?",
    "Die Preise bei Händler B sind 100 % höher als bei A (B verlangt das Doppelte).",
    [("Die Preise bei Händler B sind 50 % höher als bei A.", "den Grundwert nicht gewechselt: Bei der Aussage über B ist der Preis von A der Grundwert, und der Unterschied ist so groß wie A selbst"),
     ("Die Preise bei Händler B sind 150 % höher als bei A.", "100 % + 50 % gerechnet; der Unterschied zwischen B und A ist so groß wie der Preis von A, also 100 % von A"),
     ("Die Preise bei Händler B sind 200 % höher als bei A.", "„das Doppelte“ mit „um 200 % höher“ gleichgesetzt; das Doppelte sind 200 % des Preises von A, aber nur 100 % mehr")],
    "Beispiel: Kostet ein Artikel bei B 100 €, dann bei A 50 % weniger, also 50 €. Gegenüber A kostet er bei B 50 € mehr. Der Grundwert ist jetzt der Preis bei A (50 €): 50 € von 50 € sind 100 %. "
    "Also ist B um 100 % teurer als A: B verlangt das Doppelte, das sind 200 % von A, aber nur 100 % mehr.",
    lambda: 100 - F(50, 100) * 100 == 50 and F(100 - 50, 50) == 1 and F(100, 50) == 2 and F(100 - 50, 100) == F(1, 2)), lp=LP)
neu(T, "verstehen", "korrektur", "einkleidung", Z(
    "Der Eintritt für ein Schwimmbad kostete 30 €. Nach dem Umbau steigt der Preis um 200 %. Wie viel Euro kostet der Eintritt danach?",
    90, "30 + 30 * 200 / 100", "30 * 3",
    "200 % von 30 € sind 2 · 30 € = 60 €. Der Preis steigt um 60 €, also kostet der Eintritt danach 30 € + 60 € = 90 €. Das ist das Dreifache (300 % des alten Preises). „Um 200 % steigen“ heißt nicht „auf 200 % steigen“.",
    [B("2 * 30", "„um 200 % steigen“ als „auf 200 % steigen“ gelesen: nur 2 · 30"),
     B("30 + 200", "die 200 % als 200 € gelesen und zum alten Preis addiert"),
     B("30 * 200", "mit der Prozentzahl 200 malgenommen, ohne sie in einen Anteil umzuwandeln")], einheit="€"), form="bruecke", lp=LP)
neu(T, "verstehen", "korrektur", "darstellung", W(
    "In einer Stadt hat sich die Zahl der Radfahrer im Vergleich zum Vorjahr verdoppelt. Welche Angabe beschreibt dasselbe?",
    "Die Zahl der Radfahrer ist um 100 % gestiegen.",
    [("Die Zahl der Radfahrer ist um 200 % gestiegen.", "„verdoppelt“ mit „um 200 % gestiegen“ gleichgesetzt; um 200 % wäre das Dreifache"),
     ("Die Zahl der Radfahrer ist um 50 % gestiegen.", "die Hälfte der neuen Zahl als Zunahme genommen; die Zunahme ist aber so groß wie die alte Zahl"),
     ("Die Zahl der Radfahrer hat sich auf 100 % des Vorjahres erhöht.", "„auf 100 %“ bedeutet unverändert; verdoppelt wäre „auf 200 %“")],
    "Verdoppelt heißt: neue Zahl = 2 · alte Zahl. Die Zunahme ist dann so groß wie die alte Zahl selbst, also 100 % der alten Zahl. Man sagt: um 100 % gestiegen, auf 200 % des Vorjahres gestiegen. „Um 200 %“ wäre das Dreifache, „auf 100 %“ wäre unverändert.",
    lambda: 2 * 100 - 100 == 100 and 3 * 100 - 100 == 200 and 1.5 * 100 - 100 == 50), form="bruecke", lp=LP)
neu(T, "verstehen", "sicherung", "mehrschritt", Z(
    "In einer Schule mit 200 Kindern spielen 30 % ein Instrument. Von diesen Kindern spielen 40 % Gitarre. Wie viel Prozent aller 200 Kinder spielen Gitarre?",
    12, "0.3 * 0.4 * 100", "30 * 40 / 100",
    "30 % von 200 sind 60 Kinder mit Instrument. 40 % von diesen 60 Kindern sind 24 Gitarrenspieler. 24 von 200 sind 24 : 200 = 0,12 = 12 %. Der Grundwert der 40 % sind die 60 Kinder, nicht alle 200.",
    [B("30 + 40", "die beiden Prozentsätze addiert, obwohl sie sich auf verschiedene Grundwerte beziehen"),
     B("40 - 30", "die beiden Prozentsätze abgezogen"),
     B("30 * 40", "die beiden Prozentzahlen einfach malgenommen, ohne sie in Anteile umzuwandeln")], einheit="%"), form="bruecke", lp=LP)
neu(T, "verstehen", "sicherung", "fehler", L(
    "Zwei Klassen stellen fest: Zeile 1: In Klasse A haben 80 % der Kinder die Hausaufgabe gemacht, in Klasse B nur 60 %. Zeile 2: 80 % sind mehr als 60 %, also ist der Anteil in A größer. Zeile 3: Also haben in A mehr Kinder die Hausaufgabe gemacht. In welcher Zeile steckt der erste Fehler? Probe an einem Beispiel: Klasse A hat 5 Kinder, Klasse B hat 30 Kinder. Wie viele Kinder mehr haben in B die Hausaufgabe gemacht als in A?",
    "Fehler in Zeile □, Unterschied in B: □ Kinder", [3, 14], ["3", "0.6 * 30 - 0.8 * 5"], ["6 / 2", "18 - 4"],
    "Prozentzahlen vergleichen Anteile, nicht Anzahlen. Zeile 1 und 2 sind richtig. Zeile 3 schließt falsch auf die Anzahl der Kinder. Beispiel: In A haben 80 % von 5 = 4 Kinder die Hausaufgabe gemacht, in B 60 % von 30 = 18 Kinder. In B sind es 18 − 4 = 14 Kinder mehr, obwohl der Anteil dort kleiner ist.",
    {1: [(-14, "die Differenz andersherum gebildet: 4 − 18 (A minus B)", "0.8 * 5 - 0.6 * 30"), (18, "nur die Kinder aus Klasse B gezählt: 60 % von 30", "0.6 * 30"), (20, "den Unterschied der Prozentzahlen 80 − 60 als Zahl der Kinder gelesen", "80 - 60")]}), form="fehler_detektiv", lp=LP)
neu(T, "verstehen", "sicherung", "transfer", Z(
    "200 kg frische Trauben bestehen zu 90 % aus Wasser. Sie werden zu Rosinen getrocknet, die nur noch zu 80 % aus Wasser bestehen. Wie viel Kilogramm wiegen die Rosinen? (Beim Trocknen geht nur Wasser verloren.)",
    100, "0.1 * 200 / 0.2", "200 * 10 / 100 * 100 / 20",
    "Das Wasser verdunstet, die Trockenmasse bleibt gleich: 10 % von 200 kg = 20 kg. In den Rosinen bestehen 100 % − 80 % = 20 % aus Trockenmasse. Diese 20 kg sind also 20 % des neuen Gewichts: 20 kg : 0,2 = 100 kg. Das Ganze (der Grundwert) hat sich geändert.",
    [B("200 - 0.2 * 200", "20 % des alten Gewichts abgezogen: 200 − 40"),
     B("0.2 * 200", "20 % von 200 kg als neues Gewicht genommen"),
     B("200 - 0.1 * 200", "10 Prozentpunkte weniger Wasser als 10 % des alten Gewichts abgezogen: 200 − 20")], einheit="kg"), lp=LP)
# ───────── dritte Korrektur-Aufgabe je Lernziel ─────────
neu(T, "prozentsatz", "korrektur", "darstellung", Z(
    "Ein Kreisdiagramm zeigt, wie Kinder zur Schule kommen. Der Kreis hat 360° im Ganzen; der Sektor „Fahrrad“ hat den Mittelpunktswinkel 126°. Wie viel Prozent der Kinder kommen mit dem Fahrrad?",
    35, "126 / 360 * 100", "126 * 100 / 360",
    "Der volle Kreis (360°) entspricht 100 %. Der Anteil ist 126 : 360 = 0,35 = 35 %. Probe: 35 % von 360° sind 0,35 · 360° = 126°.",
    [B("126 / 180 * 100", "den Halbkreis (180°) als Ganzes genommen statt des vollen Kreises"),
     B("126 / 100", "den Winkel durch 100 geteilt, ohne ihn zum vollen Kreis ins Verhältnis zu setzen"),
     B("126 - 100", "den Winkel 126° minus 100 gerechnet")], einheit="%"), lp=LP)
neu(T, "rabatt_aufschlag", "korrektur", "darstellung", Z(
    "Ein Händler erhöht einen Preis um 40 %. Danach gibt er auf den erhöhten Preis 25 % Rabatt. Wie viel Prozent des ursprünglichen Preises muss man am Ende zahlen?",
    105, "1.4 * 0.75 * 100", "(140 - 140 * 25 / 100)",
    "Der ursprüngliche Preis ist 100 %. Nach 40 % Aufschlag sind es 140 %. Der Rabatt von 25 % bezieht sich auf 140 %: 25 % von 140 % sind 35 %. Es bleiben 140 % − 35 % = 105 %. Der Faktor ist 1,4 · 0,75 = 1,05.",
    [B("100 + 40 - 25", "die Prozentzahlen 40 und 25 einfach verrechnet statt die Faktoren zu multiplizieren"),
     B("100 + 40 + 25", "beide Änderungen als Aufschlag addiert"),
     B("100 - 40 + 25", "Aufschlag und Rabatt mit vertauschten Vorzeichen verrechnet")], einheit="%"), lp=LP)
neu(T, "verstehen", "korrektur", "umkehr", Z(
    "Ein Kleid wurde um 50 % reduziert und kostet jetzt 40 €. Wie viel Euro hat es vorher gekostet?",
    80, "40 / 0.5", "40 + 40",
    "Nach 50 % Abzug zahlt man noch 50 % vom alten Preis. 40 € sind also 50 % des alten Preises (des Grundwerts), der alte Preis ist das Doppelte: 80 €. Probe: 50 % von 80 € sind 40 €.",
    [B("40 * 1.5", "50 % auf den neuen Preis aufgeschlagen, obwohl sich die 50 % auf den alten Preis beziehen"),
     B("40 / 2", "den neuen Preis halbiert, statt den Grundwert zu bestimmen"),
     B("40 + 50", "die Zahl 50 als 50 € gelesen und addiert")], einheit="€"), form="umkehren", lp=LP)
