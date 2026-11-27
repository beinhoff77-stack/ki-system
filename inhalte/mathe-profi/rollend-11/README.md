# rollend-11: Aufgaben Stufe 3 (Vorrat, nicht eingespielt)

Stand 27.11.2026, Kürzel `S3`, Kennungen S3-V001 bis S3-V060. Zweck: Jede Lernkarte in `rollend-5` und `rollend-7`, die keine Aufgabe der Stufe 3 hat, bekommt genau eine zählende Aufgabe (`zaehlt = ja`, `s` = 3) in einer Form, die in dieser Lernkarte noch fehlt.

## Übersicht je Thema
Spalten: Klasse, Einheit, Lernkarten ohne Stufe 3, neue Aufgaben, Formen (FD Fehler-Detektiv, UM Umkehren, ZW Zwei Wege, BR Brücke, AN Anwenden).

| Kl. | Thema | LK ohne S3 | neu | Formen |
|---|---|---|---|---|
| 5 | messen.koerper_darstellung | 3 | 3 | BR2 UM1 |
| 5 | stochastik.kombinatorik | 4 | 4 | AN1 FD1 UM1 ZW1 |
| 5 | zahlen.ganz | 6 | 6 | BR1 FD2 UM1 ZW2 |
| 5 | zahlen.natuerlich | 7 | 7 | AN2 FD2 UM1 ZW2 |
| 5 | zahlen.potenzen_basis | 3 | 3 | AN1 BR1 FD1 |
| 5 | zahlen.rechengesetze | 6 | 6 | AN1 BR2 FD1 UM2 |
| 8 | gleichungen.bruch | 5 | 5 | AN2 FD1 UM2 |
| 8 | gleichungen.linear | 4 | 4 | AN1 BR1 FD1 UM1 |
| 8 | groessen.indirekt | 1 | 1 | ZW1 |
| 8 | messen.prisma_zylinder | 2 | 2 | BR1 UM1 |
| 8 | stochastik.grundbegriffe | 3 | 3 | AN1 BR1 UM1 |
| 8 | terme.bruchterme | 4 | 4 | BR2 FD1 ZW1 |
| 8 | terme.potenzgesetze_ganzzahlig | 3 | 3 | FD2 ZW1 |
| 8 | terme.potenzgesetze_natuerlich | 2 | 2 | FD1 ZW1 |
| 8 | terme.quadratische_extreme | 1 | 1 | AN1 |
| 8 | terme.umformen | 3 | 3 | AN1 FD1 ZW1 |
| 8 | terme.umformen_teil2 | 3 | 3 | BR1 UM1 ZW1 |

Summe Klasse 5: 29 Lernkarten, 29 Aufgaben (FD 7, UM 6, ZW 5, BR 6, AN 5). Summe Klasse 8: 31 Lernkarten, 31 Aufgaben (FD 7, UM 6, ZW 6, BR 6, AN 6). Fehler-Detektive: 14 von 60, je Klasse höchstens ein Drittel. Kein Lückenweg.

## Aufbau
- Eine JSON-Datei je Thema im Format von `rollend-7`; `th_*.py` sind die Quellen, `kern.py` die Bausteine, `bauen.py` erzeugt die JSON und prüft.
- `g` (Stufe 3): Detektiv `fehler`, Umkehren `rueckwaerts`, Zwei Wege und Brücke `verknuepfen`, Anwenden `transfer`.
- Antworten nur `zahl` oder `auswahl`; Zeichnung nur `tabelle`. `thema` ist die Einheit, `l` die Lernkarte, `t` wie im Bestand.

## Prüfungen
- `python3 -I inhalte/mathe-profi/rollend-11/bauen.py` endet mit OK. Es prüft: Lösung jeder Aufgabe durch Rechnung; jedes Fehlbild mit `rechnung` ergibt die gespeicherte falsche Antwort; Fehler-Detektiv Zeile für Zeile (genau eine falsche Zeile, Rest stimmt); bei Auswahl genau eine richtige Antwort und keine zwei gleichen; Form kommt in der Lernkarte noch nicht vor; `l` und `t` gehören zur Einheit; Fragetext nicht doppelt und nicht der Bestandstext mit anderen Zahlen; Ergebnis ab 10 steht nicht in Text oder Hinweis; Verteilung von Fehlerzeile (1:4, 2:4, 3:4, 4:2) und Lage der richtigen Auswahlantwort.
- `python3 -I tools/inhalt_pruefen.py` an Kopien aller betroffenen Themen mit den neuen Aufgaben: Code 0.
- `python3 -I tools/rollend_sql.py --runden 11`: OK, 60 Aufgaben, 17 Einheiten, `zaehlt` nur ja, 12 mit Tabelle; auch mit `--runden 5,7,11` ohne Fehler. Das Werkzeug wurde nicht geändert.
- Schlussdurchsicht als strenger Gegenprüfer (Liste B: eindeutig, Voraussetzungen, allgemein gültig, Hinweis verrät nichts, Form hält ihr Versprechen): alle 60 durchgerechnet. 15 Aufgaben geändert (14 Hinweise, die Fehler oder Weg verrieten, 1 unklarer Fragetext bei S3-V037).

## Annahmen
- Die Lernkarten ohne Stufe 3 wurden aus `aufgabe.s` in `rollend-5` und `rollend-7` gezählt (29 und 31).
- `tools/vorrat_pruefen.py` erfasst von sich aus nur `rollend-1` bis `-4`; es wurde nicht geändert. `bauen.py` importiert seine vier Prüfungen und wendet sie auf diese Runde an (Vorprüfung).

## Offen
- Fehlbild-Kennungen (`fehlbild`) sind überall `null`; sie müssen bei Bedarf einem Fehlbild-Katalog zugeordnet werden.
- 33 Fehlbilder haben keine `rechnung` (`c` = null): 32 sind die Antworten „In Zeile k“ der 14 Fehler-Detektive (nicht rechnerisch; ihre Wahrheitswerte kommen aus der Rechnung in `th_*.py`), 1 ist V007 (Antwort 1101101, Ziffern als normale Zahl gelesen).
- Anzeige in der App nicht getestet (Tabellen, Index-Antworten).
- Lernkarten, die in `rollend-5/7` später noch Stufe 3 bekommen, würden hier doppelt besetzt.

## Vorprüfung durch zweiten Helfer
Alle 60 Aufgaben vollständig gelesen und von Hand nachgerechnet (Lösung, jede Antwortoption, jedes Fehlbild, jede Detektiv-Zeile samt Folgezeilen). Lösungen und Fehlbild-Rechnungen: keine falsche gefunden. Alle 14 Fehler-Detektive: Fehlerzeile spricht die falsche Behauptung aus, Zeilen davor richtig, Folgezeilen folgen richtig.
- Geändert (12 Aufgaben): V002 (Fehlerbeschreibung „eine Null zu wenig“), V006, V016, V035, V046, V054 (Fehlbild-Beschreibungen so, dass die Rechnung maschinell nachvollziehbar ist), V013 (Tipp zeigte fast die Lösung), V014 (Wachstum ausdrücklich „immer mit derselben Zahl malgenommen“, vorher nicht eindeutig), V018 (Fehlbild-Text unklar), V025 (Nachtisch bei jedem Gericht gleich, vorher mehrdeutig), V032 (Tipp „x für k wegfallen“ führte in die Irre, x = 1 sagt nichts über k), V040 (Tabelle war überflüssig, die Faktorform stand im Text und glich dem Lückenweg derselben Lernkarte; jetzt Brücke: c steht nur in der Tabelle, aus N(0) folgt c = 5, dritte Nullstelle außerhalb), V042 (Weg A war dieselbe Rechnung wie Weg B; jetzt Zahlenvergleich der Nenner bei x = 5).
- `bauen.py` neu: wendet `vorrat_pruefen.py` (i bis iv) auf die Runde an, 4 begründete Restmeldungen (V054 Potenzschreibweise, V036 Parser, V024 und V019: Fehlerzeile mit richtiger Zahlenrechnung, falsch ist die ausgesprochene Rechenart bzw. der Übertrag, steht aber in dieser Zeile); prüft je Detektiv genau eine falsche Zeile = Schlüssel; Übertragskette in V019.
- Fraglich, nicht geändert: V004 (Zeile 2 ist als Aussage richtig, der Fehler ist die Zweitrundung und steht als Behauptung in Zeile 3; ein Kind könnte Zeile 2 wählen). Für Stufe 3 eher leicht in Klasse 8: V039, V044, V055, V057; in Klasse 5: V013, V014, V028. V017 und V060: Weg A und Weg B sind verwandt (beide Zwischenwerte), aber verschiedene Verfahren.

## Nach Gegenprüfung (Werkstatt 1080)
Gegenprüfung: 11 von 60 mit Muss-Befund. Alle Punkte berichtigt, neu gerechnet, `bauen.py` OK.
- Muss: V004 (Frage jetzt „erste Zeile mit einer für sich falschen Aussage“, Rückmeldungen zu Zeile 1 und 2 sagen „richtig“), V011 (Fehlbild-Erklärungen), V017 (Höhenunterschied; Weg A aus den Endhöhen, Weg B aus Anfangsunterschied plus Bewegungen), V020, V028 (Etikett bedeckt den ganzen Mantel), V035 (583 = mit 100² − 3² verwechselt), V041 (Rückmeldung Zeile 2), V045 (neu: Bruchgleichung mit x im Nenner und x ≠ 0, Fehler beim Kürzen), V051 und V054 (kein Malpunkt auf der Grundlinie; auch V053 umgeschrieben), V060 (Falschantwort −37,5).
- Auflagen: V002 und V006 auf die Lernkarten-Richtung (V002 Zahl in Ziffern lesen, V006 Jahr römisch schreiben, jetzt Auswahl), V013 (fehlender Gitterwert), V014 (Zwischenwert aus Stunde 2 und 5), V019 (Regel leer), V030, V032, V034, V038, V039, V044, V055, V057.
- Systematisch: Regel-Kennungen gegen den Katalog gelesen; nur noch gesetzt, wo der Katalog genau passt (u. a. leer: V005, V006, V007, V010, V013, V019, V027, V032, V046 bis V048, V049, V050, V052, V055 bis V057, V060). `fehlbild` bleibt überall leer. Jede Detektiv-Zeile hat eine Rückmeldung; unabhängig richtige Zeilen sagen „richtig“. Letzte Aufforderung im Text ist bei allen Aufgaben die Eingabefrage.
- Fraglich: V047 übt Verhältnisse über Teile, nicht als Verhältnisgleichung; V060 rechnet mit Punkten statt am Graphen.

## Nach zweiter Gegenprüfung (Werkstatt 1091)
Muss berichtigt: V020 (Fehlbild-Erklärung zu 7, in Quelle und JSON; alter Text nicht mehr vorhanden), V047 (Verhältnisgleichung mit m aufstellen und lösen, Teileweg als Kontrolle), V048 (beide Graphen zeichnen, Schnittstelle ablesen, Kontrolle durch Einsetzen von x = 3 in beide Funktionen), V060 (Weg A als Zeichen- und Ableseauftrag auf kariertem Papier, Weg B exakt, Frage nach dem exakten Wert).
Auflagen: V013 (Gitter ohne Randzahlen, fehlendes Feld nur über die Zeilensumme erschließbar), V038 (Hinweis „Wassermengen“), V055 (keine Produkttabelle, geordnete Paare selbst ermitteln), V057 (Schnittmenge nicht genannt, sondern aus „elf Chorkinder nicht im Theater“ zu erschließen).
Die übrigen 52 Aufgaben blieben unverändert. Neu gefasste Aufgaben wie neue geprüft: Lösung, Fehlbilder gegen Fehlwert, Tipp, Eingabefrage am Ende, Ergebnis nicht im Text. Eine begründete Restmeldung mehr in `bauen.py` (V020).
