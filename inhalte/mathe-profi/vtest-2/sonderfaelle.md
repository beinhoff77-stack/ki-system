# Sonderfälle VT2 (Verstehen in Tests, Stufe 1, Runde 2)

Zu jeder Aufgabe ein Satz: welcher Sonderfall geprüft wurde und wie er behandelt ist.


## finanzen.zinsen / rollen

- VT2-001 (test): Gleiches Kapital bei Kredit und Guthaben; Verwechslung „gleich hoch heißt gleich verzinst“ ist als Option 2/3 ausgeschlossen. Nettobetrag 120 € ist eindeutig, Zinssätze sind echte Prozentwerte.
- VT2-002 (korrektur): Drei Verträge, Rollen getrennt; Summe der Guthabenzinsen (50 + 60) und Kreditzinsen (400) nicht vermischbar. Kein Rundungsproblem.
- VT2-003 (korrektur): Nur Zinsen erhalten, nicht zahlen; Optionen mit Kredit sind durch den Klammerhinweis ausgeschlossen. 40 € passt nur zu 2 000 € bei 2 %.
- VT2-004 (korrektur): Fehler in Zeile 3 (Vorzeichen/Rolle); Zeilen 1 und 2 stimmen, damit ist „erste Fehlerzeile“ eindeutig.
- VT2-005 (sicherung): Rückzahlung 8 480 € enthält das Kapital; Zinsen sind nur die Differenz 480 €. Rolle (Kreditnehmerin zahlt) steht im Text.
- VT2-006 (sicherung): Zinsen werden durch Gegenrechnung gleichgesetzt; Ergebnis 6 000 € ist ganzzahlig, der Zinssatz des Sparbuchs (2 %) ist ausdrücklich genannt.
- VT2-007 (sicherung): Kredit und Anlage über denselben Betrag; „Gewinn“ nur bei höherem Anlagezins. Verlust 100 € eindeutig.

## finanzen.zinsen / jahreszinsen_komma

- VT2-008 (test): Fehler in Zeile 2 (25fache statt 2,5fache); Zeile 4 ist mit dem Fehlergebnis folgerichtig, zählt aber nicht als erster Fehler.
- VT2-009 (korrektur): Nur eine der vier Zahlen ist 150; Kommaverschiebungen unterscheiden sich um Zehnerpotenzen, keine zweite Lesart.
- VT2-010 (korrektur): Nur die letzte Zeile ordnet alle drei Zinssätze richtig zu; die Zeilen mit einem richtigen und zwei falschen Paaren sind bewusst gemischt.
- VT2-011 (korrektur): Nur 6 € stimmt; 60 € und 600 € entstehen durch Kommafehler, 0,60 € durch falsche Division durch 1 000.
- VT2-012 (sicherung): Drei verschiedene Zinssätze, ganze Eurobeträge (12, 60, 600); 25 % ist absichtlich ungewöhnlich, aber kein Sonderfall der Rechnung.
- VT2-013 (sicherung): Fehler in Zeile 2 (0,008 · 1 500 = 12, nicht 120); Zeile 3 folgt konsequent weiter.
- VT2-014 (sicherung): Zwei Rechenwege geben dasselbe (63 €); 0,5 % von 1 800 € = 9 €, ganzzahlig.

## finanzen.zinsen / kapital

- VT2-015 (test): Zwei Kapitale (20 000 € und 40 000 €); gefragt ist die Differenz 20 000 €, nicht eines der Kapitale. Zinssatz sinkt, Kapital steigt.
- VT2-016 (korrektur): Proportionalität nur bei gleichem Zinssatz und gleicher Zeit; Option 1 (andere Zinssätze) ist bewusst falsch.
- VT2-017 (korrektur): Platzhalter □ ist das Kapital; Gleichung □ · 0,04 = 52, nicht □ : 0,04.
- VT2-018 (korrektur): Fehler in Zeile 2 (multipliziert statt dividiert); Ergebnis 1 500 € ist ganzzahlig, das Fehlergebnis 2,646 € ist sinnlos klein.
- VT2-019 (sicherung): Vergleich ohne Rechnen: kleinerer Zinssatz heißt mehr Kapital bei gleichen Zinsen; kein Rundungsproblem.
- VT2-020 (sicherung): Zwei Schritte (60 % Teil, dann Ganzes); 54 € bei 3 % ergibt 1 800 €, das sind 60 % von 3 000 €. „Rest unverzinst“ steht im Text.
- VT2-021 (sicherung): Gegenläufigkeit von Kapital und Zinssatz; „größer als 0 %“ schließt Sonderfall 0 aus.

## finanzen.zinsen / zeitanteil

- VT2-022 (test): Monate als Bruchteil des Jahres; 4 Monate · 6 % : 12 = 2 % ist glatt. Einheit Prozent, nicht Euro.
- VT2-023 (korrektur): Zinsmonate 1. April bis 30. September = genau 6 Monate; „volle Monate“ im Text, keine Tageszählung (30/360 gehört nicht in diese Stufe).
- VT2-024 (korrektur): Nur Bank B bringt 2,25 %, die anderen genau 2 %; kein Gleichstand an der Spitze.
- VT2-025 (korrektur): Teiljahre 3, 8 und 18 Monate; 18 Monate überschreiten ein Jahr (einfache Verzinsung ohne Zinseszins), das steht nicht im Text und ist als Sonderfall zu prüfen: Rechnung bleibt linear 60 € · 1,5 = 90 €.
- VT2-026 (sicherung): Nur die Formel mit : 12 und · 5 stimmt; die anderen drehen Zähler und Nenner.
- VT2-027 (sicherung): Zwei Teilergebnisse hängen aneinander (Jahreszins 72 €, Kapital 2 400 €); Zeitanteil 8/12 ganzzahlig auflösbar.
- VT2-028 (sicherung): Proportionalität der Zeit: 9 : 3 = 3; keine Zinsen auf Zinsen.

## terme.umformen / zusammenfassen

- VT2-029 (test): Fehler in Zeile 3 (3 − 7 = −4, nicht 4); Zeile 2 stimmt, Ergebnis des Terms 3x² − 4x + 4.
- VT2-030 (korrektur): k = 8, damit das x-Glied entfällt; Gleichung 9 − 4 = 5 bleibt unberührt. Kein zweites k möglich.
- VT2-031 (korrektur): Umfang als Summe dreier Seiten, Zusammenfassen ergibt 9a + 5; kein Fehlerrisiko durch Minuszeichen.
- VT2-032 (korrektur): Fehler in Zeile 3 (−4y + 5y = y); Zeilen 1 und 2 sind korrekt.
- VT2-033 (sicherung): Nur Option 1 ergibt 3x² − 2x; die anderen drei unterscheiden sich in je einem Vorzeichen oder Exponent.
- VT2-034 (sicherung): Differenz zweier Terme; U = 4x² + 0x + 4, das mittlere Glied ist 0 (Lücke mit 0 zulässig, Hinweis „ganze Zahl“).
- VT2-035 (sicherung): Rabatt 6 € wird abgezogen; Brötchen- und Getränkepreis aus dem Text, Ergebnis 7x + 5y − 6, Konstante negativ.

## terme.umformen / minusklammer

- VT2-036 (test): Fehler in Zeile 2 (Vorzeichen vor x); Zeile 1 ist richtig.
- VT2-037 (korrektur): Differenz ist für x = 0 und x = 4 gleich (10); das ist Absicht, deshalb eindeutig. Ausgangsterm 17 − 3x, Jonas 7 − 3x.
- VT2-038 (korrektur): k = 5 durch Koeffizientenvergleich; Konstanten +3 und +3 stimmen automatisch.
- VT2-039 (korrektur): Nele hat Unrecht, Gegenbeispiel a = 2 gibt 5 gegen 11; Option 2 vertauscht die Werte, bewusst falsch.
- VT2-040 (sicherung): Bens Einsetzung x = 0 gibt 1; Annas Term ist 0x + 1, also hat x den Faktor 0 (Lücke mit 0 zulässig).
- VT2-041 (sicherung): Fehler in Zeile 2 (+(a − 1) = +a − 1); richtig 7a − 4.
- VT2-042 (sicherung): Zwei Teile werden abgesägt; Restlatte 3x + 3 cm, beide Klammern mit Minus.

## terme.umformen / aequivalenz

- VT2-043 (test): Gleicher Wert bei x = 3 beweist keine Gleichwertigkeit; Gegenbeispiel x = 0 liefert −4 und 2.
- VT2-044 (korrektur): Genau ein x (x = 4) mit gleichem Wert; Optionen sind geordnet (2, 3, 4, 5).
- VT2-045 (korrektur): a = 6 durch Ausmultiplizieren von 2(x + 3); kein zweites a.
- VT2-046 (korrektur): Genau eine der vier Optionen ist gleichwertig; die anderen unterscheiden sich im Vorzeichen oder im Koeffizienten.
- VT2-047 (sicherung): Mehrere gleiche Werte sind kein Beweis; Option 2 enthält beide Teilaussagen (ein Gegenbeispiel widerlegt, Beispiele beweisen nicht).
- VT2-048 (sicherung): Drei Terme sind 2x + 6, nur D ist 2x − 6; Reihenfolge der Buchstaben ist fest (A bis D).
- VT2-049 (sicherung): a = 4: 3x + ax muss 7x ergeben; konstante Glieder (−6) sind gleich.

## terme.umformen_teil2 / ausklammern

- VT2-050 (test): Genau eine Umformung ist falsch (9y² − 6y = 3y(3y − 2)); Probe durch Ausmultiplizieren führt zu einer eindeutigen Antwort.
- VT2-051 (korrektur): Fläche geteilt durch Seite 5x; Ergebnis 3x + 2 (ganze Zahlen).
- VT2-052 (korrektur): Fehler in Zeile 2 (12x : 6x = 2); richtig 6x(3x − 2).
- VT2-053 (korrektur): 37 · 100 = 3 700 durch Ausklammern; Ergebnis ist ohne Taschenrechner leicht.
- VT2-054 (sicherung): Kein gemeinsamer Faktor in 6x² + 4x + 5 (5 ist teilerfremd); Teilausklammern (Optionen 1 bis 3) zählt nicht.
- VT2-055 (sicherung): k = 9 (nicht 18, denn dann wäre der Faktor 18x); „positive Zahl kleiner als 20“ macht k eindeutig.
- VT2-056 (sicherung): Gesamtlänge 5x + 3, Breite 4x; Einheit Meter, keine Zusatzrechnung.

## terme.umformen_teil2 / binomisch

- VT2-057 (test): Fehler in Zeile 2 (gemischtes Glied fehlt); richtig 4x² − 20x + 25.
- VT2-058 (korrektur): Beide Zahlen positiv: 14 und 7; mit negativen Zahlen gäbe es −14 und −7 (durch den Text ausgeschlossen).
- VT2-059 (korrektur): Gegenbeispiel mit 3 und 4: 49 gegen 25, Differenz 24 = 2ab.
- VT2-060 (korrektur): Zuwachs 10x + 25 durch (x + 5)² − x²; Einheit cm².
- VT2-061 (sicherung): (50 − 1)² = 2 500 − 100 + 1 = 2 401; zweite binomische Formel, Kopfrechnung.
- VT2-062 (sicherung): Fehler in Zeile 2 ((4x)² = 16x²); Zeile 3 ist 24x, damit stimmt die Option „2 · 4x · 3 = 12x“ nicht.
- VT2-063 (sicherung): Seite 2x + 5, Umfang 8x + 20; Quadrat wird nur über die binomische Formel gefunden.

## geometrie.kreis / umkehrung

- VT2-064 (test): Rechter Winkel bei C (Umkehrung), MC gleich Radius 5 cm; Option „kleiner als 5“ meint stumpfen Winkel.
- VT2-065 (korrektur): Koordinatenaufgabe ohne Wurzel: C liegt über dem Mittelpunkt M(2 | 0) im Abstand 4; zweiter möglicher Punkt (2 | −4) ist durch „positive y-Koordinate“ ausgeschlossen.
- VT2-066 (korrektur): Alle Punkte auf dem Kreis um M mit Radius 4 cm; Katheten werden nicht vorgegeben.
- VT2-067 (korrektur): Fehler in Zeile 3 (Radius = Hälfte von 10 cm = 5 cm); Zeilen 1 und 2 stimmen.
- VT2-068 (sicherung): C muss die Abstandsbedingung zum Mittelpunkt M(4 | 0) erfüllen: nur (4 | 4); die anderen Punkte liegen innen oder außen.
- VT2-069 (sicherung): Behauptung stimmt für jedes rechtwinklige Dreieck, nicht nur gleichschenklig; Umkreis fällt mit Thaleskreis zusammen.
- VT2-070 (sicherung): Gleichschenklige Teildreiecke ACM und MCB; Winkel 40°, 50°, 100°.

## geometrie.kreis / lage

- VT2-071 (test): Elf ganzzahlige Abstände 0 bis 10: Sekante 6 (0 bis 5), Tangente 1 (d = 6), Passante 4 (7 bis 10).
- VT2-072 (korrektur): Zwei Schnittpunkte heißt Abstand kleiner als Radius; r = 7 cm wäre Tangente, deshalb nur r > 7 cm.
- VT2-073 (korrektur): Radius ganzzahlig und kleiner als 3 cm; r = 3 wäre Tangente (trifft die Gerade), deshalb höchstens 2 cm.
- VT2-074 (korrektur): Abstand 4 cm gegen Radius 3, 4, 5: 0, 1, 2 gemeinsame Punkte; „Punkt(e)“ im Schablonentext.
- VT2-075 (sicherung): Tangente bei d = r = 4,5 cm; Durchmesser 9 cm, nicht Radius.
- VT2-076 (sicherung): Zwei Kreise, Gesamtzahl der Punkte: bei d = 3 berührt die Gerade den kleinen Kreis (1) und schneidet den großen zweimal (2), also 3.
- VT2-077 (sicherung): Anzahl der Punkte steigt nicht ständig: 0, 1, dann immer 2; Option 3 beschreibt den Verlauf.

## geometrie.kreis / umkreis_inkreis

- VT2-078 (test): Stumpfer Winkel (100°) gibt Mittelpunkt außerhalb; 90° gibt Mittelpunkt auf der Hypotenuse, 50/60/70 innen.
- VT2-079 (korrektur): Mittelsenkrechte gegen Winkelhalbierende; Ecken gegen Seiten; nur eine Kombination richtig.
- VT2-080 (korrektur): Drei Dreiecke, Winkelsumme 180° jeweils geprüft; B ist der rechtwinklige Sonderfall (Mittelpunkt auf der Seite).
- VT2-081 (korrektur): Fehler in Zeile 2 (Mittelsenkrechten statt Winkelhalbierenden); Zeile 1 ist richtig.
- VT2-082 (sicherung): Aussage ist nur manchmal richtig; Sonderfall rechtwinkliges Dreieck wird mitgenannt.
- VT2-083 (sicherung): β von 1 bis 139, γ = 140° − β; spitzwinklig für β von 51 bis 89, das sind 39 Werte. Rechtwinklig (β = 50, 90) ist ausgeschlossen.
- VT2-084 (sicherung): Im gleichseitigen Dreieck fallen Umkreis- und Inkreismittelpunkt zusammen; Begründung über gleiche Geraden.

## zahlen.natuerlich / stellenwert

- VT2-085 (test): Zahl mit 0 an einer Stelle; Differenz 63 000 ist größer als 0 und glatt.
- VT2-086 (korrektur): Ziffer 5 im Tausender und im Einer; 5 000 : 5 = 1 000-mal.
- VT2-087 (korrektur): Volle Einheiten: 360 Hunderter, 3 607 Zehner (nicht 36 072); Reste ignorieren.
- VT2-088 (korrektur): Fehler in Zeile 2 (zweite Stelle von links in 360 482 ist Zehntausender); richtig 60 000.
- VT2-089 (sicherung): Nullen als Platzhalter; Option 3 vergleicht 7 090 mit 79.
- VT2-090 (sicherung): Größte 4 321, kleinste 1 234, Differenz 3 087; jede Ziffer genau einmal.
- VT2-091 (sicherung): Zahl · 10 − Zahl = 9 · Zahl = 4 050, also 450; kein negativer oder zweiter Wert.

## zahlen.natuerlich / ziffern_zu_zahlwort

- VT2-092 (test): Nullen in der Zahl lassen Wörter weg; Optionen unterscheiden sich in Klassen (Millionen, Tausend, Einer).
- VT2-093 (korrektur): Neue Zahl 30 005 = dreißigtausendfünf; Option „dreißigtausendfünfzig“ meint 30 050.
- VT2-094 (korrektur): Fehler in Zeile 3 (9 steht in der Einerklasse); Zeile 1 und 2 stimmen.
- VT2-095 (korrektur): Klassen: 300 | 300; erste Klasse Tausender. Die falschen Optionen erklären das Lesen nicht über die Klassen.
- VT2-096 (sicherung): Vergleich nach Stellenzahl; Wortlänge hat nichts mit dem Wert zu tun.
- VT2-097 (sicherung): Fehler in Zeile 3 (010 sind zehn Tausender); Zeile 2 stimmt, die Zahl ist zehn Millionen zehntausend einhundert.
- VT2-098 (sicherung): Mal 1 000 verschiebt um drei Stellen; neue Zahl 403 002 000.

## zahlen.natuerlich / strahl_eintragen

- VT2-099 (test): Linearer Zusammenhang (6 cm für 1 200); 3 400 → 17 cm ohne Rundung.
- VT2-100 (korrektur): Fünf gleich lange Abschnitte (nicht vier Teilstriche); zweiter Teilstrich nach 3 000 ist 3 240.
- VT2-101 (korrektur): Drei Abschnitte, Schritt 10 000; beide Werte ganz.
- VT2-102 (korrektur): Fehler in Zeile 3 (7,5 · 2 cm = 15 cm); Zeile 2 stimmt.
- VT2-103 (sicherung): Mitte zwischen benachbarten Strichen 4 000 und 4 500 ist 4 250.
- VT2-104 (sicherung): Zählung von links: dritter Strich 2 400, sechster 3 000, Schritt 200; zehnter Strich 3 800 (nicht der neunte).
- VT2-105 (sicherung): Gleicher Platz für ungleich große Unterschiede; die richtige Option nennt den Faktor 9.

## zahlen.natuerlich / runden_regel

- VT2-106 (test): 4 750 bis 4 849: genau 100 Zahlen (4 849 rundet ab, 4 850 rundet auf 4 900); natürliche Zahlen, 4 750 und 4 849 mitgezählt.
- VT2-107 (korrektur): 345 bis 354, bei Zehnern rundet 5 auf; Rand 345 mitgezählt.
- VT2-108 (korrektur): 11 500 rundet auf 12 000 (Aufrundungsregel), 12 500 rundet auf 13 000; nur eine Option passt.
- VT2-109 (korrektur): Fehler in Zeile 2 (4 < 5 heißt abrunden); Zeile 1 ist richtig.
- VT2-110 (sicherung): Je nach Zahl größer, kleiner oder gleich; zu den „immer“-Optionen gibt es Gegenbeispiele.
- VT2-111 (sicherung): Doppeltes Runden führt zu 3 700 statt 3 600; es zählt nur die erste weggelassene Stelle.
- VT2-112 (sicherung): Gleiche Rundung auf 8 000 gibt 7 500 bis 8 499; größter Unterschied 999.

## zahlen.natuerlich / runden_sinnvoll

- VT2-113 (test): Kontonummern sind Bezeichner, keine Mengen; andere Optionen nennen falsche Gründe.
- VT2-114 (korrektur): Aufrunden aus Sachgründen: 130 : 48 ≈ 2,7, also 3 Busse; Abrunden auf 2 reicht nicht.
- VT2-115 (korrektur): Zwei Rundungen auf verschiedene Stellen; beide richtig, die erste genauer.
- VT2-116 (korrektur): Erst runden (10 000), dann mal 4; Ergebnis 40 000 (Schätzung), der exakte Wert 39 480 ist nicht gefragt.
- VT2-117 (sicherung): Gerundete Beträge verschleiern 237 € < 249 €; Grobes Runden ist hier unbrauchbar.
- VT2-118 (sicherung): Schätzung 12 000, genau 11 997; Unterschied 3. Tool-Hinweis „runden fehlt“ ist falscher Alarm (Zahl ist ganz).
- VT2-119 (sicherung): Gleich gerichtete Fehler addieren sich (440 bis 480 je Zahl); Summe der Fehler 1 830.

## zahlen.natuerlich / roemisch_schreiben

- VT2-120 (test): Fehler in Zeile 2 (DCCCC verletzt die Viererregel); Zeilen 3 und 4 passen zu den Regeln.
- VT2-121 (korrektur): Regelwerk im Text; nur VC verstößt (V nicht vor C). Optionen CDXC, MCMXC, XLIV sind regelgerecht.
- VT2-122 (korrektur): 1 888 = MDCCCLXXXVIII, 13 Zeichen (höchste Zeichenzahl unter 4 000).
- VT2-123 (korrektur): Bausteine M, CM, XL, IV mit Werten 1 000, 900, 40, 4; Summe 1 944.
- VT2-124 (sicherung): Größte Zahl mit X und I ist 39 (XXXIX); XL = 40 braucht L.
- VT2-125 (sicherung): MIM verstößt gegen die I-Regel; 1 999 = MCMXCIX.
- VT2-126 (sicherung): Neun Zahlen mit drei Zeichen (3, 7, 12, 14, 16, 19, 21, 25, 30); Aufzählung nachgerechnet.

## zahlen.natuerlich / dualsystem

- VT2-127 (test): Anhängen einer 0 im Zweiersystem verdoppelt; im Zehnersystem wäre es das Zehnfache.
- VT2-128 (korrektur): 37 = 32 + 4 + 1; Lücken 0 oder 1 sind eindeutig (Zweiersystem hat eindeutige Darstellung).
- VT2-129 (korrektur): 10001 = 17, 1111 = 15; Stellenzahl entscheidet.
- VT2-130 (korrektur): Fehler in Zeile 2 (Stellenwert 4 steht bei 0, die Einsen sind bei 1, 2 und 8); richtig 11.
- VT2-131 (sicherung): 1 gefolgt von sechs Nullen ist 2⁶ = 64.
- VT2-132 (sicherung): 32 Zahlen von 0 bis 31, einschließlich 0 (Text).
- VT2-133 (sicherung): 127 = 2⁷ − 1, also sieben Einsen; Zahl 8 Ziffern wäre 255.
