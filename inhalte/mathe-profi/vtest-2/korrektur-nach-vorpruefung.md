# Korrektur nach der Vorprüfung (VT2, Zweig `vorpruefer-vt2`, Commit efec082b)

Format: Kennung · Befund (Grad) · alt → neu bzw. warum nicht. „ersetzt“ heißt: neue Aufgabe an derselben Stelle (Kennung, Pool, Lernziel bleiben). Alle Aufgaben sind danach neu gebaut, geprüft (`vtest_pruefen.py --runde 2` ohne Fehler) und gegengerechnet (`gegenrechnung.py`: 0 Abweichungen).

## Befund A

- VT2-025 · 18 Monate mehrdeutig (A) · 18 Monate → 9 Monate (Zeiten 3, 8, 9 Monate, Soll 15/40/45 €); Fehlbild „60 : 3“ durch „60 · 8 : 3 = 160, durch 3 statt durch 12 geteilt“ ersetzt. Kein Zeitraum über einem Jahr mehr in der Runde.

## Befund B (Tabelle der Vorprüfung)

- 001 · Doppelung des Bestands, Stufe überhöht · ersetzt: Kredit 6 000 € zu 5 %, Sparbuch gleicher Höhe zu 1 %; gefragt Nettozinsen und Nettosatz (240 €, 4 %). Denkfigur: nur der Unterschied der Zinssätze zählt. Auswahl → Lücken.
- 002 · Rechnen nach Schema, ≈ rollend-8 · ersetzt: drei Verträge, Kredit hat den höchsten Zinssatz, die Familie bekommt trotzdem netto Zinsen (Eingabe 1/2 und Betrag 90 €).
- 005 · Doppelung, trivial, längste Option · ersetzt: Kredit mit Rückzahlung 5 150 € einschließlich 3 % Zinsen, geliehener Betrag (5 000 €) rückwärts.
- 006 · Schema (Gleichsetzen) · nicht geändert: bleibt als einzige Schema-nahe Aufgabe in „rollen“; Fehlbilder prüfen, dass Rollen und Zinssatz nicht verwechselt werden.
- 007 (Max, Auswahl) · nicht im B-Block, aber Idee ähnlich 001 · ersetzt: Bank sieht die Rollen umgekehrt (zahlt 2 000 €, bekommt 9 000 €).
- 009 · Text verrät Strategie, Doppelung · ersetzt: 1 %, 0,5 %, 0,05 % von 6 000 € (60, 30, 3). Auswahl → Lücken.
- 012 · Schema · ersetzt: Zinssatz aus Zinsbetrag (15 € bei 6 000 € → 0,25 %), Auswahl mit Optionen im Zehnerabstand.
- 014 · zwei_wege nur formal · ersetzt: Auswahl „Welche Rechnung liefert NICHT die Zinsen?“ (Zerlegung des Zinssatzes); Form zwei_wege entfällt.
- 015 · Zufallstreffer 20 000 € = altes Kapital · Zahlen geändert (600 € bei 4 % → 2,5 %): altes Kapital 15 000, neues 24 000, Soll 9 000; Fehlbild „altes Kapital“ aufgenommen.
- 016 · Option 1 widerspricht Voraussetzung, [0] längste · Option 1 ersetzt („viermal so groß, wegen Zeit doppelt“), Option 0 gekürzt.
- 023 · Doppelung (1. März bis 1. September) · ersetzt: zwei Anlagen mit je 4 000 € (3 Monate zu 5 %, 5 Monate zu 3 %), beide 50 €.
- 024 · Doppelung (3 000 € für 8 Monate zu 3 % …) · ersetzt: aus „2 % des Kapitals in 8 Monaten“ den Jahreszinssatz (3 %).
- 027 · Doppelung · ersetzt: 75 € in 10 Monaten → 4 Monate (30 €), ohne Kapital und Zinssatz.
- 029, 031, 033, 035, 042 · zusammenfassen: Rechnen nach Schema · 029 bleibt (Test, Fehlersuche mit Begründung der Vorzeichen), 031 ersetzt (Gegenbeispiel 3x + 4x² ≠ 7x³), 033 ersetzt (fehlende Zahlen rückwärts), 035 ersetzt (Unterschied zweier Terme in einer Sachsituation), 042 (minusklammer) ersetzt (2 500 − (2 500 − 43)). Schema-nah bleiben 029 und 032.
- 034 · Fehlbildtext falsch · Beschreibung zu „von −4 noch einmal 4 abgezogen (−4 − 4)“.
- 038 · Fehlbilder vertauscht, ≈ Bestand · Aufgabe ersetzt durch „x = 1 einsetzen ergibt 5, welches k?“ (k = 5); Fehlbilder neu und passend.
- 040 · zwei_wege formal, Soll 0x + 1 irritiert · Form zwei_wege entfernt (typ transfer), Text „auch die Zahl 0 darfst du eintragen“.
- 043 · gleiche Figur wie 047, Optionen am längsten · Optionen gekürzt, Begründung verkürzt; 047 ersetzt (siehe dort).
- 044 · Doppelung, durch Probieren lösbar · ersetzt: 2(x + 3) und 2x + 3 unterscheiden sich immer um 3 (Unterschied bei x = 5 und x = 100).
- 045 · Parameter, ≈ Bestand · ersetzt: x² + 3x und 2x² + 2x stimmen nur bei zwei Zahlen überein (Zählen im Bereich −5 bis 5).
- 046 · zwei_wege formal · Form zwei_wege entfernt.
- 047 · Antwort aus 043 ablesbar, „drei reichen nicht“ nicht streng · ersetzt: Term der Form a · x + b aus der Wertetabelle (4, 7, 10) erschließen und bei x = 10 auswerten (34).
- 048 · Stufe überhöht · auf Stufe 2 gesetzt.
- 049 · Parameter · bleibt (Stufe 3, einzige Koeffizientenaufgabe nach Ersatz von 045).
- 050 · Test Stufe 2, Rechnen · ersetzt: Test als Lücken (falsche Nummer finden und Klammer berichtigen), Stufe 3.
- 051, 053 · Doppelungen · 051 ersetzt (Parameter k in 6x² + kx = 3x(2x + 5), k = 15); 053 ersetzt (größtmöglichen Faktor in 12x + 18 wählen).
- 054 · Option 3 als einzige ohne Gleichung, „ganzzahlig“ fehlt · Option umformuliert („Kein ganzzahliger Faktor außer 1 …“).
- 055 · „ganze Zahl“ fehlt · „positive ganze Zahl kleiner als 20“.
- 056 · Schema, Fehlbild-Text · ersetzt: Breite aus Fläche und Länge (20x² + 12x durch 5x + 3).
- 058, 061, 063 · Doppelungen · 058 ersetzt (k in 9x² + kx + 16 = (3x + 4)², k = 24); 061 ersetzt („Um wie viel ist 50² größer als 49²?“, 99); 063 ersetzt (Fläche 9x² + 12x + 4, Umfang 12x + 8).
- 065, 068 · nahezu dieselbe Aufgabe · 068 ersetzt: Ortslinie aller Punkte mit rechtem Winkel (Kreis um M mit r = 3 ohne A und B).
- 069 · einzige „Richtig“-Option · zwei Optionen „Richtig, denn …“ mit falscher Begründung, Länge angeglichen.
- 070 · Text liefert die Thales-Folge · „Nach der Umkehrung … gilt MA = MB = MC“ gestrichen.
- 075 · Doppelung, trivial · ersetzt: parallele Geraden g, h mit 12 cm Abstand und Kreis mit Durchmesser 9 cm (Abstand 3 cm).
- 077 · Grenzfall zur Mehrdeutigkeit · Satz „immer mehr gemeinsame Punkte“ (ohne Grenze), richtige Option „Mehr als 2 Punkte gibt es nie“ gekürzt.
- 078, 082 · Antwort ablesbar, Stufe · 078 ersetzt (Test: Werte von β zählen, die den Mittelpunkt außen legen, 78); 082 ersetzt (Inkreismittelpunkt liegt immer innen).
- 081 · Doppelung · ersetzt: Umkreiskonstruktion mit Höhen statt Mittelsenkrechten.
- 085 · Fehlbildtext, Stufe 3 überhöht · ersetzt (Test): Tausch benachbarter Stellen rückwärts (Ziffer 3).
- 097 · Fehlbild „Folgefehler in Zeile 4“ falsch · „Zeile 4 für falsch gehalten, obwohl 100 einhundert heißt“.
- 099 · Doppelung Zahlenstrahl · nicht geändert: bleibt als Test (Stufe 3, Skalenabstand in cm), Ähnlichkeit zu Bestand ist gering (Messgröße cm).
- 100, 101, 104 · Doppelungen · 100 ersetzt (falsch beschriftete Skala), 101 ersetzt (näher an welcher Marke), 104 ersetzt (Striche und Abschnitte).
- 107 · Bereich, ≈ Bestand · bleibt, Zahlen weichen ab (350, Bereich 345 bis 354).
- 112 · fast wortgleich mit Bestand · ersetzt: Zehner 350 und Hunderter 400 gleichzeitig (5 Zahlen).
- 110 · einzige Nicht-Absolutaussage, längste · falsche Optionen auch als Aussagen mit Zusatz, richtige gekürzt.
- 114 · Doppelung · ersetzt: Trikots für 1 000 € (aus Sachgründen abrunden).
- 120 · Test trivial, Regel im Text · ersetzt: Fehler-Detektiv ohne genannte Regel (CCCC statt CD), Lücken.
- 124 · ohne genannte Regeln keine größte Zahl (mehrdeutig) · ersetzt: Zahlen von 1 bis 50 mit Subtraktionspaar IV, IX oder XL zählen (18); Beispiele der Paare stehen im Text.
- 133 · Potenzschreibweise, Fehlbild nicht nachvollziehbar · Lösungsweg ohne Potenzen; Fehlbild „7 − 1“ neu begründet.

## Befund C

- 008, 013, 032, 036, 041 (Gerüst wie Bestand) · 008 bleibt (richtige Option gekürzt), 013 ersetzt, 032/036/041 unverändert (Fehlerzeile jeweils nicht am Ende, Fehler selbst weicht vom Bestand ab).
- 010, 011 · 010 bleibt (Zuordnung, Etikett „Zinssatz als Rechenfaktor schreiben“); 011 Etikett „Ergebnis mit Begründung prüfen“.
- 018 · Fehlbild 2 646 unerreichbar · gestrichen, ersetzt durch „63 als Kapital“.
- 022, 028 · Stufe · 022 ersetzt (Test: Laufzeit aus den Zinsen), 028 auf Stufe 2.
- 030, 037, 046, 071, 072, 073, 074 · 037 ersetzt (Variable fällt weg), 071 ersetzt (Radius aus Zahl der Passanten), 073 ersetzt (Gerade fest, Radius ändert sich), 074 ersetzt (Tangente ⊥ Berührradius); 030, 046, 072 unverändert.
- 052, 057, 059, 060, 062 · 052 Fehlbilder umformuliert, 059 Option gekürzt, 057/060/062 unverändert (Fehler verschieden).
- 064, 066, 067, 069 · eine Figur → 066 ersetzt (Umkreisradius 6 cm → AB = 12 cm), 064 und 067 bleiben.
- 076, 079, 080, 084 · 076 Fehlbild bleibt, 079 unverändert, 084 Option gekürzt.
- 086, 087, 090, 092, 093, 096, 103 · Stufe 2: 090 auf Stufe 2, 092 ersetzt (Test: Nullen bei Zahlwörtern), 096 gekürzt, 086/087/093/103 waren schon Stufe 2.
- 091, 099, 101, 102 · Erklärtexte der Fehlbilder arbiträr · 101 ersetzt; 091, 099, 102 unverändert (je ein weiteres Fehlbild trägt einen echten Fehler).
- 106, 108, 111, 113, 116, 118, 119 · 108 ersetzt (größter Rundungsfehler), 111 und 119 gekürzt, 113 ersetzt (Test: Rundungsfehler beim Weiterrechnen), 116 ersetzt (Runden vor oder nach dem Rechnen), 106 und 118 unverändert.
- 121, 122, 123, 125, 126, 127, 128, 131 · 121/123/126 unverändert, 122 ersetzt (längste Schreibweise 3 888), 125 gekürzt, 127 ersetzt (Test: Ziffer anhängen), 128 ersetzt (Zahlen mit genau einer Eins), 131 Etikett „umkehren“ entfernt.

## Weitere Punkte des Auftrags

- Echtes Verstehen / Denkfiguren: Je Lernziel 7 verschiedene `idee`-Werte, keine öfter als zweimal (feste Prüfung im Bauskript). Schema-nahe Aufgaben je Lernziel höchstens zwei (Einschätzung des Autors, siehe README).
- Test-Aufgaben: alle 19 Stufe 3. Die acht als Stufe 2 gemeldeten (022, 050, 071, 078, 092, 113, 120, 127) wurden alle ersetzt.
- Auswahl: 47 von 133 (35 %), im Test-Pool 4 von 19; die richtige Möglichkeit ist in nur 1 von 47 die eindeutig längste (Bauskript erlaubt höchstens 35 %), Plätze A bis D: 12, 13, 9, 13 (Bauskript erlaubt 16 % bis 34 %). Sammel-Optionen („Beide …“) sind in 4 von 5 Fällen falsch, das ist nicht ganz ausgeglichen (siehe README).
- Lehrplan: Umkehrung des Satzes des Thales gehört laut `inhalte/themen/geometrie.kreis.json` (Merke, Abschnitt „Satz des Thales“) und Themenliste zur Einheit; Passante/Tangente/Sekante steht ebenfalls dort in der Merke und im Abschnitt „Tangenten“ (Lernziel `lage`). Das Gymnasium-Zeilenzitat der Themenliste nennt Tangenten „von einem äußeren Punkt konstruieren“; ob die Lage Gerade-Kreis im Lehrplan schon früher vorkommt, entscheidet die Gegenprüfung (README).
