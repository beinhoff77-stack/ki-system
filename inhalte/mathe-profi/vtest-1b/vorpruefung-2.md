# Zweite Vorprüfung vtest-1b (119 Aufgaben, 17 Lernziele)

Stand 28.11.2026. Unabhängig von `vorpruefung.md`, `gegenrechnung.py` und `vorpruefung_rechnen.py`. Werkzeuge dieser Prüfung: `vorpruefung_rechnen_2.py` (eigene exakte Neurechnung aller 119 Aufgaben, jede Auswahl-Möglichkeit einzeln, alle 378 Fehlbilder), `vorpruefung_statistik_2.py` (Auswahl-Statistik). Es wurde nichts an Aufgaben geändert.

## Urteil

**Nach kleiner bis mittlerer Korrektur einspielbar:** Alle 119 Lösungen und alle 378 Fehlbilder rechnen richtig (0 Abweichungen, keine Auswahl mit zwei richtigen Möglichkeiten nach Rechnung), aber 1 wörtliche und mehrere Kern-Doppelungen zum Bestand, 1 mehrdeutige Auswahl, 1 Aufgabe ohne Denkanteil und zwei Lernziele, die fast nur Schema enthalten, müssen vorher behoben werden (6 A-Befunde).

## Was Fakt ist und was Einschätzung ist

- Fakt (nachgerechnet): Lösungen, Fehlbild-Rechnungen, Auswahl-Statistik, Lücken-Abdeckung. Die Probe von 049 ist jetzt richtig (b = 36).
- Fakt (Quelle): Lehrplan Gymnasium Jgst. 6 nennt negative Exponenten nur als Brüche mit Zähler 1 und Zehnerpotenzen (M6 1.4) und Trapez samt Herleitung durch Zerlegen und Ergänzen (M6 2.1), sowie Prozentpunkte (M6 3): https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/6/mathematik
- Einschätzung (von Hand): Schema/Verstehen, Denkfiguren, „Kern gleich“ beim Bestand. Die Bestandssuche war lexikalisch (Wortmenge ohne Zahlen, danach von Hand gelesen), deshalb ist die Liste B1 bis B5 eine Mindestmenge, keine vollständige.

## Befunde A (Muss)

| Kennung | Beleg | Vorschlag |
|---|---|---|
| A1 VT1B-080 | Bestand `zahlen.potenzen_zehner`: „Ein Faden ist 80 µm dick. Wie viele solcher Fäden liegen nebeneinander auf 1 cm?“ (125). Gleiche Zahlen, gleiche Frage, nur Haar statt Faden; das Werkzeug meldete nichts. | Ersetzen (z. B. Dicke gegeben, Anzahl auf Strecke in mm und µm mit anderem Gedanken) oder in ein Verstehens-Format ändern. |
| A2 VT1B-043 (Test) | Bestand `groessen.verhaeltnisse`: „Zwei Zahlen stehen im Verhältnis 3 : 5. Addiert man zu jeder 4, stehen sie im Verhältnis 2 : 3.“ Gleiche Aufgabenart und gleicher Rechenweg (5k, 7k, Außen mal Innen). Die Test-Aufgabe darf kein Bestandsklon sein. | Test ersetzen, z. B. durch 049 mit Zusatzfrage oder eine neue Rückwärts-Aufgabe; 043 als Korrektur behalten. |
| A3 VT1B-060 | Der Text nennt beide Ergebnisse (13 und 25), gefragt ist der Unterschied: 25 − 13 = 12 ohne jede Einsicht, wer recht hat. Antwort steckt im Text, Fehlbilder 13/25 stehen ebenfalls im Text. | Fragen, welche Rechnung richtig ist und um wie viel das falsche Ergebnis abweicht, ohne beide Ergebnisse vorzugeben; oder Gegenbeispiel mit Auswahl. |
| A4 VT1B-105 | Auswahl: Möglichkeit [2] „Es ist ein Rechteck, denn die Fläche 48 ist durch die Grundseite 8 teilbar“ nennt dieselbe richtige Folgerung wie [3]; nur die Begründung ist unsinnig. Die Frage lautet „Welche Aussage stimmt?“, also ist [2] als Aussage zur Hälfte richtig. | [2] so ändern, dass die Folgerung selbst falsch ist (z. B. „Es ist ein schiefes Parallelogramm, denn 48 ist durch 8 teilbar“) oder die Frage auf die Begründung richten. |
| A5 `vorsilben_klein` (078–084) | Schema in 6 von 7 (078, 079, 080, 081, 082, 083): Umrechnen und Sortieren mit vorgegebenen Potenzen; nur 084 prüft eine Einsicht. 079 ist reine Wissensabfrage. Das Lernziel verfehlt den Zweck der Runde. | Mindestens 078 (Test), 080, 081 durch Begründen/Rückwärts/Fehlvorstellung ersetzen (z. B. „Welche Größe ist größer, ohne umzurechnen“, Skalierung, Fehlvorstellung Maßzahl/Einheit wie 084). |
| A6 `zahlen.potenzen_zehner / negativer_exponent` (071–077) | Schema in 5 von 7 (072, 073, 075, 076, 077): Stellen zählen und 10⁻ⁿ ↔ Dezimalzahl, ÷10, Vergleich mit Grenze; 077 heißt „begruenden“, verlangt aber nur die Definition. Denkfigur „Stellen ↔ Exponent“ viermal (071, 072, 076, 077). | 072, 076, 077 durch zwei Aufgaben mit echter Einsicht ersetzen (Muster/Begründung, Darstellungswechsel mit Potenzgesetz, Fehlvorstellung „Minus macht negativ“ als Fehler-Detektiv). |

## Befunde B (Soll)

| Kennung | Beleg | Vorschlag |
|---|---|---|
| B1 Bestand Prozent | 001 (Test): Bestand „60 % Mädchen, 50 % der Mädchen und 25 % der Jungen singen im Chor, wie viel Prozent aller“ und „640 Kinder, 45 % Mädchen, 25 % Fußball“: gleicher Kern (Prozentsätze verschiedener Ganzer). 015 (Test): „Prozent vom Prozent“ wie „640 Kinder“. 009: Bestand „63 Kinder = 45 %, wie viele untersucht“ gleiche Aufgabe mit anderen Zahlen. | 009 ersetzen. 001 und 015: Kern ändern (z. B. Rückwärts: AG-Anteil gegeben, Mädchenanteil gesucht). |
| B2 Bestand Gleichungen/Verhältnis | 039: `rollend-7` „Für welche Zahl a ist x = 3 bei (x + a)/(x − 3) = 7/(x − 3) eine Scheinlösung?“ gleicher Kern und Rechenweg. 045: Bestand „Verhältnis 3 : 5, Differenz 14, kleinere Zahl“. 048: Bestand „Erbe 2 : 3 : 5, kleinster Anteil 4 000 €, Erbe insgesamt“. 049: Bestand „a : b = 2 : 3 und b : c = 4 : 5, gib a : b : c an“ (049 ergänzt nur a = 24). 035: Bestand „60 % Mädchen, 4 Jungen dazu, 50 %“ und „Jungen : Mädchen 4 : 5, 2 Jungen dazu, 1 : 1“. | Je Aufgabe anderen Gedanken wählen; `bestandsvergleich.md` nennt 045/048 gar nicht. |
| B3 Bestand Potenzen | 054: `rollend-7`/`rollend-11`/Bestand „Muster nach rechts, jedes Mal durch die Basis teilen“ (3ⁿ statt 2ⁿ). 056: Bestand „Algenfläche verdoppelt sich, vor 4 Tagen / Tage bis 1/32“. 063: `rollend-8` „Basis 3, Wert 1/27, ganzzahliger Exponent“ (gleiche Aufgabe, 5 und 0,04). | Ersetzen oder in andere Denkfigur ändern. |
| B4 Bestand Zehnerpotenzen | 066: Bestand „4,5 · 10ⁿ hat ausgeschrieben genau 11 Stellen. n?“. 068: Bestand „2,5 · 10ⁿ gleich 0,0025“. 075: Bestand „7 · 10⁻⁴ durch 1 000, Ergebnis 7 · 10ⁿ“. 081: Bestand „Rechne um: 0,35 mm = ? µm“. 067: Bestand „Welche Darstellung von … ist die wissenschaftliche Schreibweise?“ (ca. 15 Aufgaben). 085/087/088: Bestand „Für welche ganzen Zahlen n ist 3 · 10ⁿ größer als 0,02 und kleiner als 0,5“ und „Welche Zahl liegt zwischen 10⁻³ und 10⁻²“. | Siehe A5/A6: ersetzen statt umformulieren. |
| B5 Bestand Flächen | 096: „Jonas … 6 · 8 = 48“ (schräge Seite statt Höhe). 108/109: `rollend-6` „Trapez … Weg B: Zerlege in Rechteck und Dreiecke“. 110: Bestand „Fünfeck aus Rechteck und Dreieck“. 112: Bestand „Die Punkte A(1|1), B(9|1), C(7|5), D(3|5) bilden ein Trapez“. 114/118: Bestand „Rechteck schief gedrückt, Höhe nur noch 1“ bzw. Parallelogramm mit gleicher Höhe und schräger Seite. 115: `rollend-14` „Rechteck 6 × 12, Dreieck gleiche Fläche, Grundseite 16“. 116: Bestand „Parallelogramm und Dreieck, gleiche Grundseite und Fläche, Höhe?“. 117: Bestand „Quadrat, 4-mal so lange Seite, Fläche“. 119: Bestand „Welche Figur ist flächengleich?“. 113: `rollend-14` „Trapez 54 cm², Höhe 6, andere parallele Seite“ (113 hat nur die Verdopplung als Zusatz). | Die Bestandsliste in `bestandsvergleich.md` zu „kein Bestandsfünfeck“ (zusammengesetzt) ist falsch (110, Bestand Fünfeck). Mindestens 110, 112, 115, 116, 119 ersetzen. |
| B6 Doppelung innerhalb der Runde | 022 (Test) und 036 (Test): beide „Gleichung ist auf D immer wahr, zähle ganze Zahlen im Bereich ohne die verbotene“. 037 und 042: „x² = c, ein Kandidat verboten“. 098 und 100: „Höhe doppelt/halb so lang wie Grundseite, Fläche gegeben, g · g“. 050 (Test) und 085 (Test): „2ⁿ bzw. 5 · 10ⁿ, zähle n im Bereich“. 052 und 074: „Wie viele n-tel sind …“. 054 und 062: Muster durch die Basis teilen. 099, 101, 103, 105: viermal h = A : g. | Je Paar eine Seite ändern; bei den Tests (022/036, 050/085) eine Test-Aufgabe ersetzen. |
| B7 Denkfiguren über zweimal | Tabelle unten: grundwert 3×, verstehen 3×, definitionsmenge 4×, scheinloesung 4×, verhaeltnis 3×, negativer_exponent (terme) 3× und 051/053/056/063 viermal „Exponent aus Wert“, gross_wissenschaftlich 4×, negativer_exponent (zehner) 4×, vorsilben_klein 4×, vergleichen_pruefen 3×, rueckwaerts 4×, zusammengesetzt 3×. Die README nennt überall „höchstens zweimal“. | Zusammen mit A5, A6, B1 bis B6 abarbeiten; README-Tabelle neu zählen. |
| B8 Schema über zwei | Tabelle unten: 3 in prozentwert, grundwert, definitionsmenge, ueber_kreuz, verhaeltnis, negativer_exponent (terme), fehler_finden, vergleichen_pruefen; 4 in scheinloesung. | Je Lernziel 1 bis 2 Schema-Aufgaben durch Verstehen ersetzen (siehe Spalte „Schema“). |
| B9 Test nicht anspruchsvollste | 029 (nur Einordnung von fünf Gleichungen, Antwort 0 bis 5), 057 (Fehler ist Bruchaddition Jgst. 5/6, nicht Potenz; Schema), 106 (Quadrat minus vier Dreiecke, einfachste Aufgabe des Lernziels). | 029 durch 034 oder 033 ersetzen (beide anspruchsvoller), 057 durch 061/062/058, 106 durch 107 oder 112. |
| B10 VT1B-029 mehrdeutig | „sofort über Kreuz“: (C) 5/(x + 1) = 2 hat rechts keinen Bruch. Das eigene Fehlbild „2“ ist als Lesart vertretbar. Antwort 3 ist nicht eindeutig. | Fünf Gleichungen so wählen, dass jede Seite eindeutig Bruch oder Summe ist; oder ganze Zahl nicht verwenden. |
| B11 Eindeutigkeit im Text | 035 „In einer Gruppe sind 9 Jungen“ (ob vorher Mädchen da waren, steht nicht da); 066 „Ausgeschrieben hat die Zahl 12 Ziffern“ (1,5 hat 2 Ziffern, also „ganze Zahl“ ergänzen); 099 „Welche y-Koordinate hat D“ (oberhalb oder unterhalb der x-Achse nicht gesagt, −150 möglich). | Je einen Satz ergänzen („Zuerst besteht die Gruppe nur aus 9 Jungen“, „ganze Zahl“, „D liegt oberhalb der x-Achse“). |
| B12 Fehlbilder | 027: Fehlbild 3 („drei Nenner-Gleichungen“, es gibt zwei) und Fehlbild 4 (2 + 1 + 1 = 4, Beschreibung „beider Nenner“ ergibt 3). 042: das typische Fehlbild „2 als Lösung“ (nicht gegen D geprüft) und „−2 als verbotener Kandidat“ fehlen. In 8 Fehler-Detektiven (006, 013, 019, 027, 033, 040, 047, 057) hat die Zeilen-Lücke 1 kein Fehlbild, nur die Wert-Lücke. | Fehlbilder ergänzen/korrigieren; das ändert nichts an den Lösungen. |
| B13 Lösung in Nachbar-Aufgabe | 079 („1 µm = 10⁻⁶ m“ ist die richtige Möglichkeit) steht wörtlich im Text von 078 und 082. 066 und 070 nennen „a von 1 bis unter 10“ und verraten damit die Bedingung aus 067/069. | Definitionen aus den Texten nehmen oder 079 ersetzen (A5). |
| B14 Lernziel-Zuordnung | 062 (5⁰ begründen) und 063 (Exponent aus 0,04) gehören nicht zu `fehler_finden`, es wird kein Fehler gesucht. 057 ist Fehler in Bruchaddition. | 062/063 unter `negativer_exponent` zählen oder durch Fehler-Aufgaben ersetzen. |
| B15 Lehrplan | Jgst. 6 deckt negative Exponenten nur als 1/aⁿ und Zehnerpotenzen (M6 1.4). 053 und 061 (Bruchbasis (2/3)⁻²), 058/059 ((−3)², (−2)⁻¹ mit negativer Zahl) sind aus Jgst. 8/7 (Sicherheit mittel, Quelle: Grundwissen Jgst. 8 ISB/Schulen, nicht der G9-Plan selbst). Parameter 024, 034, 039, 043: kein Beleg gefunden (Sicherheit gering); 034 ist für Jgst. 8 sehr schwer (Fallunterscheidung k = 0, 4). | Feld `lehrplan` bei 053/061 auf „M8“ ändern oder Aufgabe in Etappe verschieben; 034 vereinfachen oder entfernen. |
| B16 VT1B-002 | Der Text gibt Kims Rechnung „70 € − 3,50 €“ vor, die Antwort ist eine Subtraktion; „zwei Wege“ ohne Einsicht. 032: beide „Wege“ sind dieselbe Rechnung (Kreuzprodukt = Hauptnenner). | Zwei echte Wege mit Entscheidung (welcher ist kürzer / warum gleich). |

## Befunde C (Kann)

| Kennung | Beleg | Vorschlag |
|---|---|---|
| C1 | Fehlbild-Beschreibungen stimmen nicht mit der Rechnung: 005 („20 000 = um eine Stelle zu groß: 51 % als ganze Zahl“ wäre 200 000), 031 (Möglichkeit [3]: „links das Doppelte“, es ist das Vierfache), 071 (−7 „vergrößert statt verkleinert“), 109 (Fehlbild 11: Rechnung `14 - 3`, Beschreibung „obere Breite abgezogen, Höhe addiert“). | Texte anpassen. |
| C2 | 090: Fehlbild-Antwort steht als Gleitkommazahl `6e-07` in der JSON. | Als 0.0000006 schreiben. |
| C3 | 087: Möglichkeiten [0] und [2] haben denselben Wert (0,00035). Erlaubt, aber verrät, dass beide falsch sind. | Eine Möglichkeit ändern. |
| C4 | 017 nennt „Prozentpunkte“ im Lösungsweg; Lehrplan M6 3 führt Prozentpunkte. Die Annahme in README („liegt im Vorrat, weil Klasse 7“) ist damit zumindest unsicher. | Entscheidung zu `vorrat-folgerunde` prüfen. |
| C5 | 12 Aufgaben haben als Antwort eine kleine ganze Zahl („Wie viele …“: 022, 023, 026, 029, 034, 036, 038, 050, 073, 078, 085, 086). Ratechance 20 bis 33 %, oft „Anzahl − 1“. Bei Tests sind das 022, 029, 036, 050, 078, 085. | Bei Tests Antwort eine größere Zahl oder Lücke kombinieren (Beispiel 071). |
| C6 | Platzfolge der richtigen Auswahl-Möglichkeit: 20311302310220311130231022031130231; keine einfache Regel, aber Rückkehr bei Abstand 12 in 13 von 23 Fällen (Zufall wäre etwa 6). | Bei Überarbeitung Plätze neu mischen. |
| C7 | 062 Möglichkeit [3] und 091 [1] sind die klar längsten; insgesamt nur 4 von 35 richtige als einzig längste (020, 041, 046, 062), daher unauffällig. | – |
| C8 | 024 (Parameter im Nenner) für Stufe 2 anspruchsvoll. | Prüfen, ob Stufe 3. |

## Schema und Denkfiguren je Lernziel (Handeinschätzung, nicht werkzeuggeprüft)

Schema = Rezept anwenden, Fehler-Detektiv mit Verrechner, reine Umrechnung. Denkfiguren nach Kern gruppiert; „größte Wiederholung“ = wie oft dieselbe Einsicht vorkommt.

| Lernziel | Schema (Anzahl; Kennungen) | verschiedene Denkfiguren | größte Wiederholung |
|---|---|---|---|
| prozentwert | 3 (002, 006, 007) | 7 | 1 |
| grundwert | 3 (009, 013, 014) | 5 | 3 (Grundwert = Teil : Satz: 009, 013, 014) |
| verstehen (Prozent) | 1 (017) | 5 | 3 (verschiedene Ganze: 018, 019, 020) |
| definitionsmenge | 3 (023, 025, 026) | 4 | 4 (Nennernullstellen: 023, 025, 026, 027) |
| ueber_kreuz | 3 (030, 031, 033) | 6 | 2 |
| scheinloesung | 4 (037, 038, 040, 042) | 4 | 4 (Kandidat gegen D: 037, 038, 041, 042) |
| verhaeltnis | 3 (047, 048, 049) | 5 | 3 (Teile: 043, 045, 048) |
| negativer_exponent (terme) | 3 (051, 052, 055) | 5 | 3 (Exponent aus Wert: 051, 053, 056) |
| fehler_finden | 3 (057, 060, 063) | 7 | 1 (aber 062/063 ohne Fehlersuche) |
| gross_wissenschaftlich | 2 (064, 068) | 3 | 4 (Bedingung 1 ≤ a < 10: 064, 067, 069, 070) |
| negativer_exponent (zehner) | 5 (072, 073, 075, 076, 077) | 4 | 4 (Stellen ↔ Exponent) |
| vorsilben_klein | 6 (078, 079, 080, 081, 082, 083) | 4 | 4 (Umrechnen) |
| vergleichen_pruefen | 3 (085, 086, 087) | 5 | 3 (Vergleich mit Grenzen: 085, 087, 088) |
| dreieck | 1 (095) | 6 | 2 (Höhe aus Koordinaten: 092, 095) |
| rueckwaerts | 2 (103, 104) | 4 | 4 (h = A : g: 099, 101, 103, 105) |
| zusammengesetzt | 2 (106, 110) | 4 | 3 (Trapez zerlegen: 108, 109, 112) |
| verstehen (Flächen) | 1 (115) | 6 | 2 (Scherung: 114, 118) |

Grenzfälle, die ich nicht mitgezählt habe: 003 und 065 (Darstellungswechsel, aber Rezept), 050, 090.

## Auswahl-Statistik (35 Aufgaben, 105 falsche Möglichkeiten)

| Merkmal | richtig | falsch | Urteil |
|---|---|---|---|
| Platz 0 / 1 / 2 / 3 | 8 / 10 / 8 / 9 | – | gleichmäßig; Folge siehe C6 |
| einzig längste | 4 von 35 (11 %) | – | gut; mittlere Länge 50,3 gegen 48,6 Zeichen |
| „denn/weil“ | 15 von 35 (43 %) | 45 von 105 (43 %) | ausgeglichen |
| „=“ | 16 von 35 (46 %) | 38 von 105 (36 %) | leicht zugunsten richtig, unauffällig |
| Absolutwörter (immer, nur, genau, alle, beide …) | 6 von 35 (17 %) | 15 von 105 (14 %) | ausgeglichen; die „3 und 9“ der README beruhen auf engerer Wortliste |
| höchstens/mindestens | 0 | 1 | kein Muster |
| Verneinung (nicht, kein) | 1 (3 %) | 11 (10 %) | richtige tragen seltener eine Verneinung: Tendenz „bejahende Möglichkeit = richtig“, 058 und 061 ausgleichen kaum; Bei Überarbeitung 2 bis 3 richtige mit Verneinung formulieren |
| Sammel-Optionen (Beide/Keine/Alle) | 1 | 2 | unauffällig |
| Nebensatz-Marker (, der/die/das/dass) | 2 | 7 | unauffällig |

Fehler-Detektive: 15 als Lücken (Fehlerzeile 1: 3, Zeile 2: 7, Zeile 3: 5; nie Zeile 4 trotz zwei Aufgaben mit vier Zeilen) und 1 als Auswahl (061, Zeile 2). Verteilung brauchbar; Zeile 2 etwas häufig.

**Keine Auswahl unter den 17 Tests:** Das ist gut. Zahl und Lücken lassen keine Ausschlusstaktik und keine Muster-Hinweise (Länge, denn/weil) zu. Preis: 6 von 17 Tests sind Zählaufgaben mit kleiner Antwort und Ratechance (C5), und drei Tests sind zu leicht (B9). Empfehlung: die Auswahl-Aufgaben in Korrektur/Sicherung belassen, Tests als Lücken mit zwei gekoppelten Werten bauen (Muster 071, 092).

## Werkzeug-Hinweise (36) einzeln beurteilt

- 1 Hinweis „Auswahl weicht ab“ (gleichungen.bruch: `verhaeltnis` statt `graphisch`): echt, aber begründet in `auswahl.md` (Graph ohne Bild nicht eindeutig); vertretbar.
- 14 × VT1B-050 bis 063 „rr.potenz ≠ id.zahlen.hoch_zurueck“: Fehlalarm für 050, 052, 054 bis 062; bei 051, 053, 063 (Exponent gesucht) passt die Lernkartenregel tatsächlich besser. Folgenlos fürs Einspielen.
- 7 × VT1B-064 bis 070 „rr.stellenwert ≠ rr.potenz“, 7 × 085 bis 091 „id.zahlen.schreibweisen ≠ rr.potenz“, 7 × 078 bis 084 „id.verhaeltnisse.groesse ≠ id.zahlen.buendeln“: Fehlalarm, Abweichung ist in `regeln-zuordnung.md` begründet.

## Zu Punkt 9: leere `fehlbild`/`regel_des_fehlbilds`, `rueckwaerts`-Abweichung

- `tools/vtest_sql.py` vergleicht und schreibt `fehlbild` und `regel` mit „is not distinct from“ bzw. als NULL; leere Felder behindern das Einspielen nicht. Folge: Das Fehlbild ist nicht mit dem Regelkatalog verknüpft, die Rückmeldung zeigt dann nur Text.
- `rueckwaerts` mit Lernkartenregel statt `rr.gegenrechnung`: richtige Entscheidung, weil das Werkzeug sonst einen Fehler meldet; Hinweis genügt.

## Zu Punkt 8: Lehrplan-Zweifel mit Sicherheit

| Frage | Befund | Sicherheit |
|---|---|---|
| Negative Exponenten in M6 1 | nur als Brüche mit Zähler 1 und Zehnerpotenzen (M6 1.4), Quelle oben | hoch |
| Bruchbasis, negative Basis mit negativem Exponenten | gehört nach Jgst. 8 (Grundwissenkataloge, G8-Lehrplan M 8.3); G9-Plan Jgst. 8 nicht selbst abgerufen | mittel |
| Wissenschaftliche Schreibweise, Vorsilben nano/mikro in M6 1 | auf der abgerufenen Seite keine Kompetenzerwartung dazu gefunden | gering (weder belegt noch widerlegt) |
| Gleichungen mit Parameter (024, 034, 039, 043) | kein Beleg im Lehrplan gefunden; Bruchgleichungen selbst gehören in Jgst. 8 (Grundwissen G9 Jgst. 8) | gering |
| Herleitungen bei Flächen (Zerlegen, Ergänzen, Trapez) | M6 2.1 verlangt genau das | hoch |
| Prozentpunkte | M6 3 | hoch |

## Zählung

A 6, B 16, C 8.
