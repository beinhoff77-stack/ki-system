# Sonderfälle VT2 (Verstehen in Tests, Stufe 1, Runde 2)

Zu jeder Aufgabe ein Satz: welcher Sonderfall geprüft wurde und wie er behandelt ist.


## finanzen.zinsen / rollen

- VT2-001 (test): Gleicher Betrag bei Kredit und Sparbuch: nur der Unterschied der Zinssätze (4 %) zählt; Gegenprobe über beide Einzelzinsen. Ganzzahlig.
- VT2-002 (korrektur): Kredit hat den höchsten Zinssatz, die Familie bekommt trotzdem netto Zinsen (Guthaben sind größer). Die Eingabe 1 oder 2 ist im Text erklärt.
- VT2-003 (korrektur): Nur Zinsen erhalten, nicht zahlen; Optionen mit Kredit sind durch den Klammerhinweis ausgeschlossen. 40 € passt nur zu 2 000 € bei 2 %.
- VT2-004 (korrektur): Fehler in Zeile 3 (Vorzeichen/Rolle); Zeilen 1 und 2 stimmen, damit ist „erste Fehlerzeile“ eindeutig.
- VT2-005 (sicherung): Rückzahlung 5 150 € enthält Kredit und 3 % Zinsen; 5 150 : 1,03 = 5 000 ist ganzzahlig, Zinsen 150 €. Zinssatz bezieht sich auf den geliehenen Betrag (steht im Text).
- VT2-006 (sicherung): Zinsen werden durch Gegenrechnung gleichgesetzt; Ergebnis 6 000 € ist ganzzahlig, der Zinssatz des Sparbuchs (2 %) ist ausdrücklich genannt.
- VT2-007 (sicherung): Bank sieht die Rollen umgekehrt; Sparzinsen auf alle 200 000 €, Kreditzinsen nur auf 150 000 €. Der Rest im Tresor bleibt unverzinst (steht im Text).

## finanzen.zinsen / jahreszinsen_komma

- VT2-008 (test): Fehler in Zeile 2 (25fache statt 2,5fache); Zeile 4 ist mit dem Fehlergebnis folgerichtig, zählt aber nicht als erster Fehler.
- VT2-009 (korrektur): Drei Zinssätze 1 %, 0,5 %, 0,05 % von 6 000 €; Ergebnisse 60, 30, 3 ganzzahlig, keine Rundung.
- VT2-010 (korrektur): Nur die letzte Zeile ordnet alle drei Zinssätze richtig zu; die Zeilen mit einem richtigen und zwei falschen Paaren sind bewusst gemischt.
- VT2-011 (korrektur): Nur 6 € stimmt; 60 € und 600 € entstehen durch Kommafehler, 0,60 € durch falsche Division durch 1 000.
- VT2-012 (sicherung): Nur 0,25 % liefert 15 € bei 6 000 €; die anderen Optionen unterscheiden sich um Zehnerpotenzen. Optionen aufsteigend geordnet.
- VT2-013 (sicherung): Beide Sparbücher bringen gleich viel (36 €), das ist Absicht und im Lösungsweg erklärt; Lücken nehmen gleiche Werte an.
- VT2-014 (sicherung): Genau eine Rechnung ist falsch (0,03 · 0,005); die anderen sind richtige Zerlegungen. „NICHT“ steht im Text groß.

## finanzen.zinsen / kapital

- VT2-015 (test): 600 € bei 4 % → 15 000 €, bei 2,5 % → 24 000 €; Soll 9 000 € ist weder altes noch neues Kapital (kein Zufallstreffer).
- VT2-016 (korrektur): Proportionalität nur bei gleichem Zinssatz und gleicher Zeit; Option 1 (andere Zinssätze) ist bewusst falsch.
- VT2-017 (korrektur): Platzhalter □ ist das Kapital; Gleichung □ · 0,04 = 52, nicht □ : 0,04.
- VT2-018 (korrektur): Fehler in Zeile 2 (multipliziert statt dividiert); Ergebnis 1 500 € ist ganzzahlig, das Fehlergebnis 2,646 € ist sinnlos klein.
- VT2-019 (sicherung): Vergleich ohne Rechnen: kleinerer Zinssatz heißt mehr Kapital bei gleichen Zinsen; kein Rundungsproblem.
- VT2-020 (sicherung): Zwei Schritte (60 % Teil, dann Ganzes); 54 € bei 3 % ergibt 1 800 €, das sind 60 % von 3 000 €. „Rest unverzinst“ steht im Text.
- VT2-021 (sicherung): Gegenläufigkeit von Kapital und Zinssatz; „größer als 0 %“ schließt Sonderfall 0 aus.

## finanzen.zinsen / zeitanteil

- VT2-022 (test): 3 600 € bei 4 % bringen 144 € im Jahr; 60 € sind 5/12, also genau 5 Monate (ganze Zahl). Monate als Einheit im Text.
- VT2-023 (korrektur): Beide Anlagen bringen 50 €; der höhere Zinssatz wird durch die kürzere Zeit ausgeglichen. Gleiche Lückenwerte sind erlaubt.
- VT2-024 (korrektur): 8 Monate bringen 2 % des Kapitals → Jahreszinssatz 3 %; ganzzahlig. Einheit Prozent.
- VT2-025 (korrektur): Drei Teiljahre (3, 8 und 9 Monate), alle innerhalb eines Jahres; die 18 Monate und damit das Zinseszins-Problem entfallen.
- VT2-026 (sicherung): Nur die Formel mit : 12 und · 5 stimmt; die anderen drehen Zähler und Nenner.
- VT2-027 (sicherung): Zinsen proportional zur Zeit: 75 € : 10 · 4 = 30 €; Kapital und Zinssatz nicht nötig. Einfache Verzinsung innerhalb eines Jahres.
- VT2-028 (sicherung): Proportionalität der Zeit: 9 : 3 = 3; keine Zinsen auf Zinsen.

## terme.umformen / zusammenfassen

- VT2-029 (test): Fehler in Zeile 3 (3 − 7 = −4, nicht 4); Zeile 2 stimmt, Ergebnis des Terms 3x² − 4x + 4.
- VT2-030 (korrektur): k = 8, damit das x-Glied entfällt; Gleichung 9 − 4 = 5 bleibt unberührt. Kein zweites k möglich.
- VT2-031 (korrektur): 3x + 4x² ≠ 7x³: bei x = 0 und 1 stimmt es zufällig, bei x = 2 nicht (22 gegen 56, Unterschied 34).
- VT2-032 (korrektur): Fehler in Zeile 3 (−4y + 5y = y); Zeilen 1 und 2 sind korrekt.
- VT2-033 (sicherung): Lücken 2 und 1; die Rechnung ist eindeutig (5 − □ = 3 und −3 + □ = −2).
- VT2-034 (sicherung): Differenz zweier Terme; U = 4x² + 0x + 4, das mittlere Glied ist 0 (Lücke mit 0 zulässig, Hinweis „ganze Zahl“).
- VT2-035 (sicherung): Differenz Ben − Anna ergibt x + y; für x = 5, y = 2 sind das 7 €. Bens Term steht im Text, beide kaufen dieselben Mengen.

## terme.umformen / minusklammer

- VT2-036 (test): Fehler in Zeile 2 (Vorzeichen vor x); Zeile 1 ist richtig.
- VT2-037 (korrektur): Beim Auflösen von 9 − (x − 4) − (6 − x) fällt x weg, Wert 7 für jedes x.
- VT2-038 (korrektur): k aus x = 1 bestimmt: 10 − k = 5, also k = 5; die Gleichung hat genau eine Lösung.
- VT2-039 (korrektur): Nele hat Unrecht, Gegenbeispiel a = 2 gibt 5 gegen 11; Option 2 vertauscht die Werte, bewusst falsch.
- VT2-040 (sicherung): Bens Wert 1, Annas Ergebnis 0 · x + 1; der Text erlaubt ausdrücklich die Eingabe 0.
- VT2-041 (sicherung): Fehler in Zeile 2 (+(a − 1) = +a − 1); richtig 7a − 4.
- VT2-042 (sicherung): 2 500 − (2 500 − 43) = 43; die Aufgabe nennt keine Variable, Minusklammer wird als Rechenvorteil genutzt.

## terme.umformen / aequivalenz

- VT2-043 (test): Gleicher Wert bei x = 3 beweist keine Gleichwertigkeit; Gegenbeispiel x = 0 liefert −4 und 2.
- VT2-044 (korrektur): Der Unterschied ist für x = 5 und x = 100 jeweils 3, also nie gleich; Terme sind nicht gleichwertig (Lösungsweg erklärt es).
- VT2-045 (korrektur): Nur x = 0 und x = 1 stimmen in −5 bis 5; x² + 3x und 2x² + 2x sind nicht gleichwertig. Gezählt wird nur im angegebenen Bereich.
- VT2-046 (korrektur): Genau eine der vier Optionen ist gleichwertig; die anderen unterscheiden sich im Vorzeichen oder im Koeffizienten.
- VT2-047 (sicherung): Wertetabelle 4, 7, 10 gibt 3x + 4; Term nach Text der Form a · x + b, damit eindeutig (Wert 34 bei x = 10).
- VT2-048 (sicherung): Drei Terme sind 2x + 6, nur D ist 2x − 6; Reihenfolge der Buchstaben ist fest (A bis D).
- VT2-049 (sicherung): a = 4: 3x + ax muss 7x ergeben; konstante Glieder (−6) sind gleich.

## terme.umformen_teil2 / ausklammern

- VT2-050 (test): Genau Nummer 1 ist falsch; Nummer 2 bis 4 sind richtig. Richtige Klammer 3y(3y − 2).
- VT2-051 (korrektur): 6x² + kx = 3x · (2x + 5) = 6x² + 15x; k = 15, kein zweiter Wert.
- VT2-052 (korrektur): Fehler in Zeile 2 (12x : 6x = 2); richtig 6x(3x − 2).
- VT2-053 (korrektur): ggT von 12 und 18 ist 6; „größtmöglich“ im Text, damit sind 3 oder 2 als Faktor ausgeschlossen.
- VT2-054 (sicherung): Kein gemeinsamer Faktor in 6x² + 4x + 5 (5 ist teilerfremd); Teilausklammern (Optionen 1 bis 3) zählt nicht.
- VT2-055 (sicherung): k = 9 (nicht 18, denn dann wäre der Faktor 18x); „positive Zahl kleiner als 20“ macht k eindeutig.
- VT2-056 (sicherung): Breite 4x aus 20x² + 12x = (5x + 3) · 4x; ganzzahlige Koeffizienten, Einheit Meter.

## terme.umformen_teil2 / binomisch

- VT2-057 (test): Fehler in Zeile 2 (gemischtes Glied fehlt); richtig 4x² − 20x + 25.
- VT2-058 (korrektur): (3x + 4)² = 9x² + 24x + 16; k positiv (steht im Text), sonst auch −24.
- VT2-059 (korrektur): Gegenbeispiel mit 3 und 4: 49 gegen 25, Differenz 24 = 2ab.
- VT2-060 (korrektur): Zuwachs 10x + 25 durch (x + 5)² − x²; Einheit cm².
- VT2-061 (sicherung): 50² − 49² = 99; die Aufgabe nennt (50 − 1)² als Hilfe, ohne das Ergebnis zu verraten.
- VT2-062 (sicherung): Fehler in Zeile 2 ((4x)² = 16x²); Zeile 3 ist 24x, damit stimmt die Option „2 · 4x · 3 = 12x“ nicht.
- VT2-063 (sicherung): 9x² + 12x + 4 = (3x + 2)²; Umfang 12x + 8; Einheiten cm.

## geometrie.kreis / umkehrung

- VT2-064 (test): Rechter Winkel bei C (Umkehrung), MC gleich Radius 5 cm; Option „kleiner als 5“ meint stumpfen Winkel.
- VT2-065 (korrektur): Koordinatenaufgabe ohne Wurzel: C liegt über dem Mittelpunkt M(2 | 0) im Abstand 4; zweiter möglicher Punkt (2 | −4) ist durch „positive y-Koordinate“ ausgeschlossen.
- VT2-066 (korrektur): Umkreisradius 6 cm → AB = 12 cm; Voraussetzung rechter Winkel bei C steht im Text.
- VT2-067 (korrektur): Fehler in Zeile 3 (Radius = Hälfte von 10 cm = 5 cm); Zeilen 1 und 2 stimmen.
- VT2-068 (sicherung): Alle Punkte mit rechtem Winkel bilden den Kreis um M mit Radius 3 cm ohne A und B; die Ausnahme steht in der Antwort und im Lösungsweg.
- VT2-069 (sicherung): Umkehrung gilt in jedem rechtwinkligen Dreieck; zwei falsche Optionen haben „Richtig“ mit falscher Begründung.
- VT2-070 (sicherung): Der Text nennt MA = MB = MC nicht mehr; der Weg über die Umkehrung ist nötig. Winkel 40°, 50°, 100°.

## geometrie.kreis / lage

- VT2-071 (test): r aus „genau vier Passanten“: d = 7, 8, 9, 10 → r = 6; r ganzzahlig im Text, d = 0 ist mitgezählt.
- VT2-072 (korrektur): Zwei Schnittpunkte heißt Abstand kleiner als Radius; r = 7 cm wäre Tangente, deshalb nur r > 7 cm.
- VT2-073 (korrektur): Tangentenabstand r: doppelter Radius → 2 Punkte, halber Radius → 0 Punkte.
- VT2-074 (korrektur): Tangente ⊥ Berührradius: Winkel bei B = 90°, bei M = 35°, bei A = 55°. Der Satz steht in der Merke der Einheit.
- VT2-075 (sicherung): 12 cm Abstand − 9 cm Durchmesser = 3 cm Abstand zwischen h und Kreis, keine gemeinsamen Punkte.
- VT2-076 (sicherung): Zwei Kreise, Gesamtzahl der Punkte: bei d = 3 berührt die Gerade den kleinen Kreis (1) und schneidet den großen zweimal (2), also 3.
- VT2-077 (sicherung): Mehr als zwei Punkte gibt es nie; Mias Aussage ist mit „immer mehr“ eindeutig falsch gestellt.

## geometrie.kreis / umkreis_inkreis

- VT2-078 (test): Außen liegt der Mittelpunkt bei stumpfem β oder stumpfem γ: 39 + 39 = 78; rechte Winkel ausgeschlossen.
- VT2-079 (korrektur): Mittelsenkrechte gegen Winkelhalbierende; Ecken gegen Seiten; nur eine Kombination richtig.
- VT2-080 (korrektur): Drei Dreiecke, Winkelsumme 180° jeweils geprüft; B ist der rechtwinklige Sonderfall (Mittelpunkt auf der Seite).
- VT2-081 (korrektur): Zeile 3 ist der erste Fehler (Höhen statt Mittelsenkrechten); Zeilen 1 und 2 stimmen.
- VT2-082 (sicherung): Inkreismittelpunkt liegt in jedem Dreieck innen; die Verwechslung mit dem Umkreis ist als Ablenker gewollt.
- VT2-083 (sicherung): Inkreismittelpunkt liegt auf den Winkelhalbierenden: 25°, 35°, 120°; Winkelsumme 180° geprüft.
- VT2-084 (sicherung): Im gleichseitigen Dreieck fallen Umkreis- und Inkreismittelpunkt zusammen; Begründung über gleiche Geraden.

## zahlen.natuerlich / stellenwert

- VT2-085 (test): Differenz d · 9 000 = 27 000 → d = 3; die andere Ziffer ist 0 (im Text); die Zahlen sind natürlich.
- VT2-086 (korrektur): Ziffer 5 im Tausender und im Einer; 5 000 : 5 = 1 000-mal.
- VT2-087 (korrektur): Volle Einheiten: 360 Hunderter, 3 607 Zehner (nicht 36 072); Reste ignorieren.
- VT2-088 (korrektur): Fehler in Zeile 2 (zweite Stelle von links in 360 482 ist Zehntausender); richtig 60 000.
- VT2-089 (sicherung): Nullen als Platzhalter; Option 3 vergleicht 7 090 mit 79.
- VT2-090 (sicherung): Größte 4 321, kleinste 1 234, Differenz 3 087; jede Ziffer genau einmal.
- VT2-091 (sicherung): Zahl · 10 − Zahl = 9 · Zahl = 4 050, also 450; kein negativer oder zweiter Wert.

## zahlen.natuerlich / ziffern_zu_zahlwort

- VT2-092 (test): 40 300 070 hat acht Stellen, drei davon keine Nullen → 5 Nullen; Zahlwort ohne Milliarden.
- VT2-093 (korrektur): Neue Zahl 30 005 = dreißigtausendfünf; Option „dreißigtausendfünfzig“ meint 30 050.
- VT2-094 (korrektur): Fehler in Zeile 3 (9 steht in der Einerklasse); Zeile 1 und 2 stimmen.
- VT2-095 (korrektur): Klassen: 300 | 300; erste Klasse Tausender. Die falschen Optionen erklären das Lesen nicht über die Klassen.
- VT2-096 (sicherung): Vergleich nach Stellenzahl; Wortlänge hat nichts mit dem Wert zu tun.
- VT2-097 (sicherung): Fehler in Zeile 3 (010 sind zehn Tausender); Zeile 2 stimmt, die Zahl ist zehn Millionen zehntausend einhundert.
- VT2-098 (sicherung): Mal 1 000 verschiebt um drei Stellen; neue Zahl 403 002 000.

## zahlen.natuerlich / strahl_eintragen

- VT2-099 (test): Linearer Zusammenhang (6 cm für 1 200); 3 400 → 17 cm ohne Rundung.
- VT2-100 (korrektur): Skala mit Schritt 250: 800 gehört nicht dazu (750). Nur eine falsche Beschriftung.
- VT2-101 (korrektur): 7 640 liegt näher an 8 000 (Abstand 360); Mitte 7 500 liegt links davon, kein Gleichstand.
- VT2-102 (korrektur): Fehler in Zeile 3 (7,5 · 2 cm = 15 cm); Zeile 2 stimmt.
- VT2-103 (sicherung): Mitte zwischen benachbarten Strichen 4 000 und 4 500 ist 4 250.
- VT2-104 (sicherung): Fünf Striche heißen sechs Abschnitte, vierter Strich 400.
- VT2-105 (sicherung): Gleicher Platz für ungleich große Unterschiede; die richtige Option nennt den Faktor 9.

## zahlen.natuerlich / runden_regel

- VT2-106 (test): 4 750 bis 4 849: genau 100 Zahlen (4 849 rundet ab, 4 850 rundet auf 4 900); natürliche Zahlen, 4 750 und 4 849 mitgezählt.
- VT2-107 (korrektur): 345 bis 354, bei Zehnern rundet 5 auf; Rand 345 mitgezählt.
- VT2-108 (korrektur): Größte Abweichung 50 (bei x950 → aufrunden); 49 und 100 sind Ablenker.
- VT2-109 (korrektur): Fehler in Zeile 2 (4 < 5 heißt abrunden); Zeile 1 ist richtig.
- VT2-110 (sicherung): Je nach Zahl größer, kleiner oder gleich; zu den „immer“-Optionen gibt es Gegenbeispiele.
- VT2-111 (sicherung): Doppeltes Runden führt zu 3 700 statt 3 600; es zählt nur die erste weggelassene Stelle.
- VT2-112 (sicherung): 345–354 → Zehner 350; nur 350–354 → Hunderter 400 (5 Zahlen).

## zahlen.natuerlich / runden_sinnvoll

- VT2-113 (test): 1 234 · 6 = 7 404, 1 200 · 6 = 7 200, Abweichung 204; Einheit €.
- VT2-114 (korrektur): 1 000 : 36 = 27,77… → 27 Trikots (abrunden); ganze Zahlen.
- VT2-115 (korrektur): Zwei Rundungen auf verschiedene Stellen; beide richtig, die erste genauer.
- VT2-116 (korrektur): Erst runden 40 000, erst rechnen 39 480 → 39 000; zwei verschiedene Schätzungen.
- VT2-117 (sicherung): Gerundete Beträge verschleiern 237 € < 249 €; Grobes Runden ist hier unbrauchbar.
- VT2-118 (sicherung): Schätzung 12 000, genau 11 997; Unterschied 3. Tool-Hinweis „runden fehlt“ ist falscher Alarm (Zahl ist ganz).
- VT2-119 (sicherung): Gleich gerichtete Fehler addieren sich (440 bis 480 je Zahl); Summe der Fehler 1 830.

## zahlen.natuerlich / roemisch_schreiben

- VT2-120 (test): Zeile 2 (CCCC statt CD); 1 449 = MCDXLIX hat 7 Zeichen. Regel wird nicht genannt (sie gehört zum Wissen der Klasse 5).
- VT2-121 (korrektur): Regelwerk im Text; nur VC verstößt (V nicht vor C). Optionen CDXC, MCMXC, XLIV sind regelgerecht.
- VT2-122 (korrektur): 3 888 = MMMDCCCLXXXVIII mit 15 Zeichen ist die längste Schreibweise unter 4 000.
- VT2-123 (korrektur): Bausteine M, CM, XL, IV mit Werten 1 000, 900, 40, 4; Summe 1 944.
- VT2-124 (sicherung): Paare IV, IX, XL stehen als Beispiele im Text; 44 und 49 enthalten zwei Paare und werden nur einmal gezählt (10 + 8 = 18).
- VT2-125 (sicherung): MIM verstößt gegen die I-Regel; 1 999 = MCMXCIX.
- VT2-126 (sicherung): Neun Zahlen mit drei Zeichen (3, 7, 12, 14, 16, 19, 21, 25, 30); Aufzählung nachgerechnet.

## zahlen.natuerlich / dualsystem

- VT2-127 (test): Wert 13 → 27 durch Anhängen einer 1 (2 · 13 + 1).
- VT2-128 (korrektur): 1, 2, 4, 8, 16, 32 sind die einzigen Zahlen bis 63 mit genau einer Eins → 6.
- VT2-129 (korrektur): 10001 = 17, 1111 = 15; Stellenzahl entscheidet.
- VT2-130 (korrektur): Fehler in Zeile 2 (Stellenwert 4 steht bei 0, die Einsen sind bei 1, 2 und 8); richtig 11.
- VT2-131 (sicherung): 1 000 000 im Zweiersystem ist 64; Etikett „umkehren“ entfernt, Potenzschreibweise vermieden.
- VT2-132 (sicherung): 32 Zahlen von 0 bis 31, einschließlich 0 (Text).
- VT2-133 (sicherung): 127 hat im Zweiersystem sieben Einsen; Lösungsweg und Fehlbilder ohne Potenzschreibweise.
