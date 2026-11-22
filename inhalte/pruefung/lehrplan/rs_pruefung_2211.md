# Prüf-Auftrag LP-RS – Realschul-Lehrplan Punkt für Punkt (22.11.2026)

Abruf aller Lehrplanseiten und Zweitquellen am 22.11.2026 (13:00, Nachtrag nach Gegenprobe ChatGPT 927/928/930 um 13:30; Korrektur-SQL nach Entscheidung „Maßstab Gruppe I“ von 13:45); Datenbank nur gelesen (Stand 22.11.2026). Nichts eingespielt. Keine Lehrplantexte wörtlich, nur Lernbereichstitel und eigene Kurzbeschreibungen.

Lieferung:
- dieser Bericht,
- `rs_pruefung_2211.json` (beide Gruppen; je Punkt: Quelle, Lernbereich, Punkt, Eintrag, Zuordnung vorher/Vorschlag, Bezug, Befund),
- `rs_korrektur_2211.sql` (nur Gruppe I und RS 5/6; nur INSERT/UPDATE; Probelauf auf einer lokalen Kopie des echten Stands nach dem Live bestanden, zweimal hintereinander, Gegenprobe bricht ab).

## Kurzergebnis

| | Realschule 5–10 (10 Quellen) |
|---|---|
| Lehrplan-Punkte Original / in der DB | 282 / 297 (RS 5 und 6 in der DB feiner geteilt) |
| Punkte mit Hauptthema vorher (ohne stillgelegte Themen) | 183 |
| Punkte mit Hauptthema nach Korrektur | 292 |
| echte Lücken (kein Thema vorhanden) | 5 Punkte, 3 Inhalte |
| teilweise abgedeckt (Thema da, Etappe fehlt) | 4 Punkte |
| Stunden je Lernbereich | alle 64 stimmen |
| Punktzahl je Lernbereich RS 7–10 | alle 52 stimmen |
| Lernbereichstitel RS 7–10 | 47 von 52 weichen vom Original ab, 17 davon fälschlich als „originaltitel“ markiert |

Deine Zweifel waren berechtigt. Die Lehrplan-Daten selbst (Stunden, Zahl der Punkte) stimmen. Falsch bzw. lückenhaft waren drei Dinge:
- Zuordnungen: 114 Punkte hatten kein gültiges Hauptthema (97 gar keine Zuordnung, 17 nur Neben- oder stillgelegte Themen). 26 hingen am falschen Thema, meist am stillgelegten Thema 48 (Vektoren/Abbildungen) oder an 43/44 statt 98/46.
- Titel: die meisten Lernbereichstitel sind umbenannt.
- Die Klasse 8 sah leer aus, weil die Punkte von Vierecke, Drehung und Daten und Zufall an Themen anderer Klassen hingen. Diese Themen sind 44 und 46 (Klasse 7 bzw. 6), das stillgelegte 48 und 61 (Klasse 9). Nach der Korrektur hat jeder Punkt in Klasse 8 ein Thema, bis auf „Vektoren drehen“.

Die Gruppen I und II/III unterscheiden sich in Stunden (7: 112/84, 8: 112/84, 9: 140/84, 10: 120/96) und in der Klassenlage (Dreiecke, lineare und quadratische Funktionen, Körperberechnungen, Raumgeometrie). Ein `rs_by` je Thema kann das nicht abbilden; Datenmodell je Gruppe × Klasse × Lernbereich × Punkt in Abschnitt 6.

Die vier im Auftrag genannten fehlenden Zuordnungen sind nach der Korrektur geschlossen: RS 7 Dreiecke → 44, RS 7 Ortslinien → 73/45, RS 8 Daten und Zufall → 61, RS 9 Kreis → 51.

## 0 Nachtrag 13:30 – Gegenprobe ChatGPT 927/928/930, selbst nachgeprüft

Neu abgerufen bzw. gegen meinen Abruf von 13:00 und die DB gehalten, 22.11.2026:

| Aussage ChatGPT | Ergebnis meiner Prüfung | Stand |
|---|---|---|
| Stundensummen 7 I 112 / II–III 84; 8 I 112 / 84; 9 I 140 / 84; 10 I 120 / 96 | bestätigt. Je Lernbereich: 7 I 10+23+14+10+12+22+12+9; 7 II/III 10+21+10+22+12+9; 8 I 12+6+13+40+7+26+8; 8 II/III 16+7+40+5+8+8; 9 I 10+17+20+10+20+12+42+9; 9 II/III 7+13+20+10+15+10+9; 10 I 42+30+16+22+10; 10 II/III 21+20+10+35+10. DB gleich | gesichert |
| Dreiecke I 7 ↔ II/III 8 | bestätigt (M7 I LB3; M8 II/III LB1) | gesichert |
| lineare Funktionen I 8 ↔ II/III 8 (y = mx) und 9 (y = mx + t) | bestätigt (M8 I LB6 mit y = mx + t; M8 II/III LB5 nur Ursprungsgerade; M9 II/III LB5) | gesichert |
| quadratische Funktionen/Gleichungen I 9 ↔ II/III 10 | bestätigt (M9 I LB7; M10 II/III LB4). Ergänzung: rein quadratische Gleichungen schon M9 II/III LB1 | gesichert |
| Körperberechnungen I 9 ↔ II/III 10 | bestätigt (M9 I LB5; M10 II/III LB2) | gesichert |
| Matrizen-Abbildungen und Potenzfunktionen nur 10 I | bestätigt: 10 II/III hat keinen Lernbereich dazu. Ergänzung: Wurzel- und trigonometrische Gleichungen ebenfalls nur Gruppe I | gesichert |
| Extremwerte quadratischer Terme in beiden Gruppen in 8 | bestätigt (M8 I LB4, M8 II/III LB3; beide → 97) | gesichert |
| Schrägbilder 7 I und 8 II/III | bestätigt (M7 I LB4, M8 II/III LB2) | gesichert |
| Determinanten auch 7 II/III | bestätigt (M7 II/III LB2 → 74) | gesichert |
| Baumdiagramm/Vierfeldertafel 8, Laplace 9, Pfadregeln 10 | bestätigt. **Damit war meine 13:00-Empfehlung „61 nach Klasse 8“ falsch**; berichtigt in Abschnitt 4 | gesichert |
| 48 und 78 ohne RS-Klasse trotz RS-Lernbereich | bestätigt für `themenliste.json` und, seit dem Live, für die DB (`klasse_fest` null). Nur die Themendateien tragen noch `rs_by` 7 bzw. 8. Beide Themen sind stillgelegt; ihre Zuordnungen in Gruppe I setzt das SQL auf „klaerungsbedarf“ | gesichert |
| 91 bei RS 8, beschreibt aber auch 7 I | bestätigt; außerdem Rotationskörper 10 II/III | gesichert |
| 46 (RS 6) enthält Drehung (8 I) | bestätigt (Etappe „Um einen Punkt drehen“); II/III hat keine Drehung | gesichert |
| 33 mischt y = mx und y = mx + t | bestätigt | gesichert |

**Zusätzlich gefunden:**
- Die Klassen in den Themendateien und in `themenliste.json` passen bei 61, 44, 91, 101, 99 und 100 nicht zusammen (Abschnitt 4).
- 33 in 8 II/III enthält schon die Orthogonalität (m₁·m₂ = −1), nicht nur y = mx.

**Folgen für die Lieferung:**
- Die Zuordnungen von 13:00 bleiben. Kein Punkt wechselt sein Thema; Rauchtest und Lücken bleiben gleich.
- Geändert:
  1. Das Etikett neu/weitergeführt wird je Gruppe berechnet, mit „neu (Etappen …)“ für Punkte, die neue Etappen bringen.
  2. Abschnitt 4 zeigt die Lage je Gruppe.
  3. Abschnitt 6 enthält das verbindliche Datenmodell.
  4. Die JSON hat neu `lage_je_gruppe` und `neue_etappen`.
  5. Die Begründungstexte im SQL sind angepasst.
- Nach der Entscheidung von 13:45 („Maßstab Gruppe I“) gilt das Korrektur-SQL nur noch für Gruppe I und RS 5/6, und Thema 91 bekommt `rs_by` 7. II/III steht nur im Bericht (Abschnitt 7).
- Probelauf auf dem echten Stand nach dem Live bestanden, zweimal hintereinander.

## 1 Lernbereiche: Original gegen DB

**Gesichert (Abruf 22.11.):**
- RS 7–10, beide Gruppen: Nummer, Stunden und Zahl der Punkte stimmen in allen 52 Lernbereichen.
- RS 5 und 6: Stunden stimmen. Die Punktzahl weicht ab, weil die DB mehrere Punkte des Originals in Teilpunkte zerlegt hat:
  - RS 5: 38 Punkte im Original, 45 in der DB (1.2: 1/2, 1.4: 1/2, 2: 5/7, 3: 6/9).
  - RS 6: 32 im Original, 40 in der DB (1: 10/12, 3: 4/6, 4: 2/4, 6: 4/6).
  - Inhaltlich fehlt nichts; die DB enthält aber Teilpunkte, die es im Original so nicht gibt.
- Titel: 47 der 52 Lernbereichstitel RS 7–10 sind in der DB nicht der Originaltitel. 17 davon sind trotzdem als „originaltitel“ gekennzeichnet (falsch), 30 als „zusammenfassung_eigene_worte“. Beispiele: „Verschiebungen“ statt Parallelverschiebung, „Rotationen“ statt Drehung, „Zufallsversuche“ statt Daten und Zufall. Richtig sind nur Proportionalitäten (7 I, 7 II/III), Funktionen (8 I, 8 II/III) und Trigonometrie (10 II/III). RS 5, RS 6 und Gymnasium 7/8 tragen die Originaltitel. Die Korrektur setzt die Originaltitel (Schritt 6 im SQL).

**Kurzfassungen:**
- Beim Zuordnen habe ich jede Kurzfassung RS 7–10 neben den Original-Punkt an derselben Stelle gelegt. Reihenfolge und Inhalt passen; sinnwidrige Kurzfassungen sind mir nicht aufgefallen. Das ist ein Ergebnis des Lesens, kein Einzelprotokoll je Punkt (**Annahme-Ebene**).
- RS 5/6: Wegen der feineren Teilung ist ein 1:1-Vergleich nur je Lernbereich möglich. Diese Punkte setzt das SQL deshalb nicht auf „geprüft“.
- Kein Lehrplantext wurde übernommen.

## 2 Zweitquellen je Klasse und Gruppe

Mathe.Logo Bayern (C.C. Buchner, für Bayern zugelassen), Stoffverteilungspläne, abgerufen 22.11.2026:

| Klasse/Gruppe | Quelle | Befund |
|---|---|---|
| 5 | [Stoffverteilungsplan 5](https://www.ccbuchner.de/_files_media/mediathek/downloads/15108.pdf) | bestätigt alle Lernbereiche inkl. Dualsystem/römische Zahlen, Kombinieren, Maßstab |
| 6 | [Produktseite 6](https://www.ccbuchner.de/produkt/mathe-logo-bayern-6-3660) | **offen**: Plan nur als Binärdatei, nicht lesbar |
| 7 I | [Westermann Mathematik 7, Wpfg. I, Inhaltsverzeichnis](https://www.kapiert.de/fileadmin/redakteure/Lehrwerke/Mathematik/Inhaltsverzeichnis/314_123623_72_dpi_gesamt.pdf.pdf) (Mathe.Logo 7 I nicht lesbar) | bestätigt: Potenzen, Parallelverschiebung mit Vektoren, Winkel an Parallelen, Terme/Gleichungen/Ungleichungen, Ortslinien inkl. Thaleskreis, Dreiecke/Kongruenz, Proportionalität, Daten, Raumgeometrie mit Schrägbildern – alles in 7 I. Bundesland steht nicht im Verzeichnis (Annahme Bayern, wegen Wpfg. I). Determinanten nicht als Kapitel; vermutlich unter „Flächen im Koordinatensystem“ (Annahme) |
| 7 II/III | [Produktseite 7 II/III](https://www.ccbuchner.de/produkt/mathe-logo-bayern-7-ii-iii-3662) | **offen**: nicht lesbar |
| 8 I | [Stoffverteilungsplan 8 I](https://www.ccbuchner.de/_files_media/mediathek/downloads/15120.pdf) | Stunden aller 7 Lernbereiche gleich; Vierecke, Drehung und Daten und Zufall (Baumdiagramm, Vierfeldertafel) sind Stoff der 8. Reihenfolge abweichend (Daten und Zufall zuerst) – kein Widerspruch |
| 8 II/III | [Stoffverteilungsplan 8 II/III](https://www.ccbuchner.de/_files_media/mediathek/downloads/15117.pdf) | Stunden aller 6 Lernbereiche gleich |
| 9 I | [Stoffverteilungsplan 9 I](https://www.ccbuchner.de/_files_media/mediathek/downloads/15129.pdf) | gleich; Buch teilt LB 7 in quadratische Funktionen (25) und Gleichungen (17) = 42 |
| 9 II/III | [Stoffverteilungsplan 9 II/III](https://www.ccbuchner.de/_files_media/mediathek/downloads/15128.pdf) | gleich |
| 10 I | [Stoffverteilungsplan 10 I](https://www.ccbuchner.de/_files_media/mediathek/downloads/15126.pdf) | gleich; Trigonometrie 17 + 17 + 8 (Skalarprodukt) = 42; zusätzlich ein Kapitel Prüfungsvorbereitung |
| 10 II/III | [Produktseite 10 II/III](https://www.ccbuchner.de/produkt/mathe-logo-bayern-10-ii-iii-4164) | **offen**: nicht lesbar |

Abschlussprüfung (9/10):
- [Abschlussprüfung 2026 Mathematik I](https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2026/2026_mi_ht.pdf): u. a. Vektoren mit Ortskurve, Trigonometrie mit Sinussatz, Rotationskörper, Exponential- und gebrochenrationale Funktionen, Pfadregeln – alles Gruppe-I-Stoff 9/10 mit Thema.
- [Abschlussprüfung 2026 Mathematik II/III](https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2026/2026_mii_ht.pdf): Parabeln mit Geraden, Rotationskörper aus Kegel/Zylinder/Kugel, Strahlensatz, Trigonometrie, Pfadregeln; **keine Vektoren, Matrizen oder Potenzfunktionen** – bestätigt die Gruppentrennung.
- [ISB Infobrief Mathematik 2023](https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Infobriefe/Mathematik/Infobrief_Mathematik_2023.pdf): Für Mathematik I sind Rotationskörper und Potenzfunktionen wieder prüfungsrelevant. Beide sind nach der Korrektur zugeordnet (91/92 und 96/36).
- [Abschlussprüfung 2021 Mathematik I](https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Mathematik/Weiterentwicklung_Abschlusspruefung/Zeichenkatalog/2021_MI_HT.pdf): Die Aufgaben nutzen Abbildungen mit Vektoren/Matrizen, Trigonometrie, Exponentialfunktionen und Raumgeometrie. Alle Bereiche stehen im Lehrplan 9/10 I und haben ein Thema, **außer der Vektorrechnung als eigenem Werkzeug** (siehe Lücken).
- Zusätzlich die [ISB-Jahrgangsstufentests 8 I 2025](https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/2025_JT_Mathematik_8_I_Angabe.pdf) und 8 II/III. Sie prüfen Drehung, Vektor/Mittelpunkt, Determinante und Thaleskreis, also genau die Inhalte der 8. Das bestätigt die Klassenlage.

**Widersprüche Zweitquelle ↔ amtlich:** keine in den lesbaren Plänen. Offen sind 6, 7 II/III und 10 II/III (Pläne nicht lesbar). Die von ChatGPT genannte Kapitelübersicht 8 II/III (braille.bildung.hessen.de) und die ISB-Leistungsaufgaben 9 habe ich nicht gefunden bzw. nicht gelesen. Amtlich gilt.

## 3 Jeder Punkt: Thema oder Lücke

Legende für die Themenspalte:
- (neu): Die Klasse des Themas (`rs_by`) ist die Lehrplanklasse.
- (weitergeführt): Das Thema stammt aus einer früheren Klasse.
- (vorgezogen): Der Lehrplan bringt den Stoff vor der Klasse des Themas (Klassen-Befund, Abschnitt 4).

„zugeordnet vorher“ zählt nur Hauptbezüge auf nicht stillgelegte Themen. Je Punkt steht alles in der JSON.

#### Realschule 5 (Quelle 7)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1.1 | Natürliche Zahlen im Dezimalsystem | – | 4/4 | 0 → 4 | – | 15 Natürliche Zahlen (neu) |
| 1.2 | Andere Zahlensysteme | – | 1/2 | 0 → 0 | 1.2/k1, 1.2/k2 |  |
| 1.3 | Grundrechenarten und Rechengesetze | – | 6/6 | 6 → 6 | – | 17 Teilbarkeit (neu); 18 Grundrechenarten und Rechengesetze (neu); 67 Potenzen als Schreibweise (neu) |
| 1.4 | Kombinatorik | – | 1/2 | 0 → 2 | – | 60 Zählen und Kombinatorik (neu) |
| 2 | Ganze Zahlen | 20 | 5/7 | 0 → 7 | – | 16 Ganze Zahlen (neu) |
| 3 | Geometrische Grundvorstellungen und Grundbegriffe | 30 | 6/9 | 9 → 9 | – | 42 Grundbegriffe und Figuren (neu); 52 Körper darstellen (neu) |
| 4 | Größen | 20 | 6/6 | 4 → 6 | – | 25 Größen und Einheiten (neu); 26 Direkte Proportionalität und Dreisatz (neu) |
| 5 | Umfang und Flächeninhalt ebener Figuren | 15 | 6/6 | 0 → 6 | – | 50 Umfang und Flächeninhalt (neu) |
| 6 | Auswertung von Daten | 5 | 3/3 | 0 → 3 | – | 57 Daten erfassen und darstellen (neu) |
| Σ | | | 38/45 | 19 → 43 | | |

#### Realschule 6 (Quelle 8)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Rationale Zahlen | 68 | 10/12 | 12 → 12 | – | 21 Brüche und Anteile (neu); 22 Dezimalzahlen (neu); 23 Rechnen mit rationalen Zahlen (neu) |
| 2 | Achsenspiegelung und Symmetrie | 13 | 5/5 | 4 → 5 | – | 46 Kongruenzabbildungen (neu) |
| 3 | Flächeninhalt ebener Figuren | 18 | 4/6 | 1 → 6 | – | 53 Volumen und Oberfläche (neu); 99 Flächen von Parallelogramm, Dreieck und Trapez (neu) |
| 4 | Raumgeometrie | 14 | 2/4 | 0 → 4 | – | 100 Volumen (neu) |
| 5 | Terme und Gleichungen | 15 | 7/7 | 7 → 7 | – | 1 Einfache Gleichungen (neu); 28 Terme aufstellen und deuten (neu) |
| 6 | Direkte Proportionalität | 12 | 4/6 | 6 → 6 | – | 24 Prozent- und Zinsrechnung (neu); 26 Direkte Proportionalität und Dreisatz (weitergeführt) |
| Σ | | | 32/40 | 30 → 40 | | |

#### Realschule 7 – Gruppe I (Quelle 24)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Potenzen | 10 | 3/3 | 1 → 3 | – | 19 Zehnerpotenzen und wissenschaftliche Schreibweise (neu); 30 Potenzen und negative Exponenten (neu); 102 Potenzgesetze (neu) |
| 2 | Parallelverschiebung | 23 | 7/7 | 3 → 6 | 2/K4 | 46 Kongruenzabbildungen (weitergeführt); 74 Zweireihige Determinanten (neu); 98 Winkelsätze (neu) |
| 3 | Dreiecke | 14 | 4/4 | 0 → 4 | – | 44 Konstruktionen, Kongruenz und Beweise (neu) |
| 4 | Raumgeometrie | 10 | 3/3 | 3 → 3 | – | 91 Schrägbilder und Raumdarstellung (neu) |
| 5 | Geometrische Ortslinien und Ortsbereiche | 12 | 5/5 | 0 → 5 | – | 45 Kreis und Tangenten (neu); 73 Ortslinien und Ortsbereiche (neu) |
| 6 | Terme, Gleichungen und Ungleichungen | 22 | 4/4 | 3 → 4 | – | 2 Lineare Gleichungen (neu); 3 Lineare Ungleichungen (neu); 29 Terme umformen (neu) |
| 7 | Proportionalitäten | 12 | 5/5 | 5 → 5 | – | 71 Zinsen (neu); 93 Indirekte Proportionalität (neu); 94 Vermehrter und verminderter Grundwert (neu) |
| 8 | Auswertung von Daten | 9 | 4/4 | 3 → 4 | – | 57 Daten erfassen und darstellen (weitergeführt); 58 Mittelwert und Häufigkeiten (neu); 81 Stichproben und Aussagekraft (neu); 95 Median, Quartile, Boxplot (neu) |
| Σ | | | 35/35 | 18 → 34 | | |

#### Realschule 7 – Gruppe II/III (Quelle 25)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Potenzen | 10 | 3/3 | 2 → 3 | – | 19 Zehnerpotenzen und wissenschaftliche Schreibweise (neu); 30 Potenzen und negative Exponenten (neu); 102 Potenzgesetze (neu) |
| 2 | Parallelverschiebung | 21 | 7/7 | 3 → 6 | 2/K4 | 46 Kongruenzabbildungen (weitergeführt); 74 Zweireihige Determinanten (neu); 98 Winkelsätze (neu) |
| 3 | Geometrische Ortslinien und Ortsbereiche | 10 | 4/4 | 0 → 4 | – | 45 Kreis und Tangenten (neu); 73 Ortslinien und Ortsbereiche (neu) |
| 4 | Terme, Gleichungen und Ungleichungen | 22 | 4/4 | 3 → 4 | – | 2 Lineare Gleichungen (neu); 3 Lineare Ungleichungen (neu); 29 Terme umformen (neu) |
| 5 | Proportionalitäten | 12 | 5/5 | 5 → 5 | – | 71 Zinsen (neu); 93 Indirekte Proportionalität (neu); 94 Vermehrter und verminderter Grundwert (neu) |
| 6 | Auswertung von Daten | 9 | 4/4 | 3 → 4 | – | 57 Daten erfassen und darstellen (weitergeführt); 58 Mittelwert und Häufigkeiten (neu); 81 Stichproben und Aussagekraft (neu); 95 Median, Quartile, Boxplot (neu) |
| Σ | | | 27/27 | 16 → 26 | | |

#### Realschule 8 – Gruppe I (Quelle 12)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Vierecke | 12 | 2/2 | 2 → 2 | – | 44 Konstruktionen, Kongruenz und Beweise (neu: neue Etappen); 46 Kongruenzabbildungen (weitergeführt) |
| 2 | Drehung | 6 | 5/5 | 0 → 4 | 2/K5 | 46 Kongruenzabbildungen (neu: neue Etappen) |
| 3 | Raumgeometrie | 13 | 3/3 | 3 → 3 | – | 91 Schrägbilder und Raumdarstellung (weitergeführt) |
| 4 | Terme, Gleichungen und Ungleichungen | 40 | 3/3 | 3 → 3 | – | 2 Lineare Gleichungen (weitergeführt); 29 Terme umformen (weitergeführt); 97 Quadratische Terme und Extremwerte (neu) |
| 5 | Bruchterme und Bruchgleichungen | 7 | 2/2 | 2 → 2 | – | 5 Bruch- und Verhältnisgleichungen (neu); 31 Bruchterme (neu) |
| 6 | Funktionen | 26 | 6/6 | 6 → 6 | – | 32 Zuordnung und Funktion (neu); 33 Lineare Funktionen (neu) |
| 7 | Daten und Zufall | 8 | 2/2 | 1 → 2 | – | 61 Zufall und Laplace (neu) |
| Σ | | | 23/23 | 17 → 22 | | |

#### Realschule 8 – Gruppe II/III (Quelle 26)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Dreiecke und Vierecke | 16 | 5/5 | 2 → 5 | – | 44 Konstruktionen, Kongruenz und Beweise (neu); 46 Kongruenzabbildungen (weitergeführt) |
| 2 | Raumgeometrie | 7 | 2/2 | 2 → 2 | – | 91 Schrägbilder und Raumdarstellung (neu) |
| 3 | Terme und Gleichungen | 40 | 3/3 | 3 → 3 | – | 2 Lineare Gleichungen (weitergeführt); 29 Terme umformen (weitergeführt); 97 Quadratische Terme und Extremwerte (neu) |
| 4 | Bruchterme und Bruchgleichungen | 5 | 2/2 | 2 → 2 | – | 5 Bruch- und Verhältnisgleichungen (neu); 31 Bruchterme (neu) |
| 5 | Funktionen | 8 | 5/5 | 1 → 5 | – | 32 Zuordnung und Funktion (neu); 33 Lineare Funktionen (neu) |
| 6 | Daten und Zufall | 8 | 2/2 | 1 → 2 | – | 61 Zufall und Laplace (neu) |
| Σ | | | 19/19 | 11 → 19 | | |

#### Realschule 9 – Gruppe I (Quelle 13)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Reelle Zahlen | 10 | 3/3 | 2 → 3 | – | 8 Quadratische Gleichungen (allgemein) (neu); 20 Wurzeln und reelle Zahlen (neu) |
| 2 | Zentrische Streckung | 17 | 8/8 | 7 → 8 | – | 47 Ähnlichkeit und Strahlensätze (neu) |
| 3 | Rechtwinklige Dreiecke | 20 | 6/6 | 6 → 6 | – | 54 Satz des Pythagoras (neu); 55 Trigonometrie im rechtwinkligen Dreieck (neu) |
| 4 | Kreis | 10 | 2/2 | 0 → 2 | – | 51 Kreisberechnungen (neu) |
| 5 | Raumgeometrie | 20 | 4/4 | 4 → 4 | – | 92 Pyramide, Kegel, Kugel (neu) |
| 6 | Systeme linearer Gleichungen | 12 | 1/1 | 1 → 1 | – | 6 Gleichungssysteme mit 2 Unbekannten (neu) |
| 7 | Quadratische Funktionen und quadratische Gleichungen | 42 | 9/9 | 9 → 9 | – | 8 Quadratische Gleichungen (allgemein) (neu); 13 Wurzelgleichungen (neu); 35 Quadratische Funktionen (neu) |
| 8 | Daten und Zufall | 9 | 5/5 | 1 → 5 | – | 61 Zufall und Laplace (neu: neue Etappen) |
| Σ | | | 38/38 | 30 → 38 | | |

#### Realschule 9 – Gruppe II/III (Quelle 14)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Reelle Zahlen | 7 | 3/3 | 2 → 3 | – | 8 Quadratische Gleichungen (allgemein) (neu); 20 Wurzeln und reelle Zahlen (neu) |
| 2 | Zentrische Streckung | 13 | 3/3 | 0 → 3 | – | 47 Ähnlichkeit und Strahlensätze (neu) |
| 3 | Rechtwinklige Dreiecke | 20 | 6/6 | 6 → 6 | – | 54 Satz des Pythagoras (neu); 55 Trigonometrie im rechtwinkligen Dreieck (neu) |
| 4 | Kreis | 10 | 2/2 | 0 → 2 | – | 51 Kreisberechnungen (neu) |
| 5 | Lineare Funktionen | 15 | 4/4 | 4 → 4 | – | 33 Lineare Funktionen (neu: neue Etappen) |
| 6 | Systeme linearer Gleichungen | 10 | 1/1 | 1 → 1 | – | 6 Gleichungssysteme mit 2 Unbekannten (neu) |
| 7 | Daten und Zufall | 9 | 5/5 | 1 → 5 | – | 61 Zufall und Laplace (neu: neue Etappen) |
| Σ | | | 24/24 | 14 → 24 | | |

#### Realschule 10 – Gruppe I (Quelle 15)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Trigonometrie | 42 | 11/11 | 11 → 11 | – | 14 Trigonometrische Gleichungen (neu); 38 Sinus- und Kosinusfunktion (neu); 49 Matrizen und Abbildungen mit Matrizen (neu); 56 Allgemeine Trigonometrie (neu) |
| 2 | Abbildungen | 30 | 4/4 | 0 → 4 | – | 37 Exponential- und Logarithmusfunktionen (neu); 49 Matrizen und Abbildungen mit Matrizen (neu) |
| 3 | Potenzen und Potenzfunktionen | 16 | 4/4 | 3 → 4 | – | 36 Potenzfunktionen (neu); 96 Rationale Exponenten und n-te Wurzel (neu) |
| 4 | Exponentialfunktionen, Logarithmen und Logarithmusfunktionen | 22 | 3/3 | 2 → 3 | – | 10 Exponentialgleichungen (neu); 37 Exponential- und Logarithmusfunktionen (neu) |
| 5 | Daten und Zufall | 10 | 2/2 | 0 → 2 | – | 62 Mehrstufige Zufallsexperimente (neu) |
| Σ | | | 24/24 | 16 → 24 | | |

#### Realschule 10 – Gruppe II/III (Quelle 16)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Trigonometrie | 21 | 6/6 | 4 → 6 | – | 38 Sinus- und Kosinusfunktion (neu); 56 Allgemeine Trigonometrie (neu) |
| 2 | Raumgeometrie | 20 | 5/5 | 5 → 5 | – | 91 Schrägbilder und Raumdarstellung (neu: neue Etappen); 92 Pyramide, Kegel, Kugel (neu) |
| 3 | Exponentialfunktionen, Logarithmen | 10 | 3/3 | 1 → 3 | – | 10 Exponentialgleichungen (neu); 37 Exponential- und Logarithmusfunktionen (neu) |
| 4 | Quadratische Funktionen und quadratische Gleichungen | 35 | 6/6 | 2 → 6 | – | 8 Quadratische Gleichungen (allgemein) (weitergeführt); 35 Quadratische Funktionen (neu) |
| 5 | Daten und Zufall | 10 | 2/2 | 0 → 2 | – | 62 Mehrstufige Zufallsexperimente (neu) |
| Σ | | | 22/22 | 12 → 22 | | |

#### Gymnasium 7 (Quelle 3)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Terme mit Variablen | 37 | 0/0 | 0 → 0 | – |  |
| 1.1 | Aufstellen und Interpretieren von Termen | 13 | 4/4 | 0 → 4 | – | 28 Terme aufstellen und deuten (neu) |
| 1.2 | Umformen von Termen | 24 | 5/6 | 1 → 6 | – | 29 Terme umformen (neu); 102 Potenzgesetze (neu) |
| 2 | Geometrische Figuren: Symmetrie und Winkel | 21 | 0/0 | 0 → 0 | – |  |
| 2.1 | Achsen- und punktsymmetrische Figuren | 12 | 3/5 | 0 → 5 | – | 46 Kongruenzabbildungen (neu) |
| 2.2 | Winkelbetrachtungen an Figuren | 9 | 4/5 | 0 → 5 | – | 98 Winkelsätze (neu) |
| 3 | Lineare Gleichungen und Vertiefung der Prozentrechnung | 17 | 4/6 | 6 → 6 | – | 2 Lineare Gleichungen (neu); 94 Vermehrter und verminderter Grundwert (neu) |
| 4 | Kenngrößen von Daten | 8 | 3/4 | 4 → 4 | – | 95 Median, Quartile, Boxplot (neu) |
| 5 | Kongruenz, besondere Dreiecke und Dreieckskonstruktionen | 29 | 9/9 | 3 → 9 | – | 44 Konstruktionen, Kongruenz und Beweise (neu); 45 Kreis und Tangenten (neu) |
| Σ | | | 32/39 | 14 → 39 | | |

#### Gymnasium 8 (Quelle 4)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Funktion und Term | 8 | 3/6 | 0 → 6 | – | 32 Zuordnung und Funktion (neu) |
| 2 | Lineare Funktionen | 16 | 5/8 | 8 → 8 | – | 3 Lineare Ungleichungen (neu); 33 Lineare Funktionen (neu) |
| 3 | Elementare gebrochen-rationale Funktionen | 13 | 3/4 | 4 → 4 | – | 34 Gebrochen-rationale Funktionen (neu); 93 Indirekte Proportionalität (neu) |
| 4 | Bruchterme und Bruchgleichungen | 13 | 5/5 | 5 → 5 | – | 4 Formeln umstellen (neu); 5 Bruch- und Verhältnisgleichungen (neu); 31 Bruchterme (neu); 103 Potenzgesetze mit ganzzahligen Exponenten (neu) |
| 5 | Laplace-Experimente | 14 | 4/5 | 1 → 5 | – | 61 Zufall und Laplace (neu) |
| 6 | Lineare Gleichungssysteme | 10 | 3/4 | 4 → 4 | – | 6 Gleichungssysteme mit 2 Unbekannten (neu) |
| 7 | Kreis und Zylinder | 10 | 4/7 | 1 → 7 | – | 51 Kreisberechnungen (neu); 52 Körper darstellen (neu); 101 Prismen und Zylinder (neu) |
| Σ | | | 27/39 | 23 → 39 | | |

### Lücken (kein passendes Thema)

| Punkt | Inhalt (eigene Worte) | Vorschlag |
|---|---|---|
| RS 5 1.2 (zwei DB-Teilpunkte) | andere Zahlensysteme: Zweiersystem, römische Zahlen, Vergleich mit dem Zehnersystem | neues kleines Thema in Klasse 5 oder Etappe in Thema 15 |
| RS 7 I und 7 II/III, LB 2 jeweils letzter Vektorpunkt | Verschiebung mit Koordinaten eines Vektors beschreiben und berechnen | Thema „Vektoren in Koordinaten“ (Kl. 7), ersetzt den Teil von 48 |
| RS 8 I LB 2 letzter Punkt | Drehung von Vektoren um den Ursprung (rechnerisch) | Etappe im selben Vektor-Thema oder in 46; 49 ist erst Kl. 10 |

**Teilweise** (Thema vorhanden, Etappe fehlt):
- RS 6 3/k2: Drachenviereck und Raute in 99.
- RS 7 I 4/K3: wahre Größe in 91.
- RS 8 I 1/K2 und 8 II/III 1/K5: Vierecke konstruieren. 44 behandelt nur Dreiecke.
- RS 9 I 2/K5: Vektorrechnung bei der Streckung; nur teilweise in 47.

Lücken sind ein Auftrag an die Inhalte-Seite. Das SQL legt keine Themen an.

## 4 Klasse je Thema und Wahlpflichtfächergruppe (Nachtrag 13:30)

Ein einziges `klasse_fest.rs_by` je Thema reicht nicht, und zwar aus zwei Gründen:
- Die Gruppen I und II/III legen denselben Stoff in verschiedene Klassen.
- Mehrere Themen verteilen ihre Etappen über zwei oder drei Klassen.

Die Tabelle zeigt die Klassen mit Hauptbezug laut Original, je Gruppe. RS 5/6 zählen für beide Gruppen. Vollständig für alle Themen steht das in der JSON unter `lage_je_gruppe`.

**Gruppe I und II/III unterscheiden sich (gesichert, Beleg = Lernbereich im Original):**

| Thema | rs_by heute | Gruppe I | Gruppe II/III | Beleg |
|---|---|---|---|---|
| 44 Konstruktionen, Kongruenz (Dreiecke) | 7 | 7 (Dreiecke), 8 (Vierecke) | 8 | M7 I LB3, M8 I LB1, M8 II/III LB1 |
| 33 Lineare Funktionen | 8 | 8 (y = mx + t vollständig) | 8 nur y = mx, 9 y = mx + t | M8 I LB6; M8 II/III LB5; M9 II/III LB5 |
| 35 Quadratische Funktionen | 9 | 9 | 10 | M9 I LB7, M10 II/III LB4 |
| 8 Quadratische Gleichungen (allgemein) | 9 | 9 | 9 (rein quadratisch), 10 | M9 I LB7; M9 II/III LB1, M10 II/III LB4 |
| 92 Pyramide, Kegel, Kugel | 9 | 9 | 10 | M9 I LB5, M10 II/III LB2 |
| 101 Prismen und Zylinder (nur Nebenbezug) | 9 | 9 | 10 | ebenda |
| 91 Schrägbilder und Raumdarstellung | 8 | 7, 8 | 8; Rotationskörper/Axialschnitte 10 | M7 I LB4, M8 I LB3; M8 II/III LB2, M10 II/III LB2 |
| 49 Matrizen und Abbildungen | 10 | 10 | – (kein Lernbereich) | nur M10 I LB2 |
| 36 Potenzfunktionen, 96 rationale Exponenten | 10 | 10 | – | nur M10 I LB3 |
| 13 Wurzelgleichungen, 14 trigonometrische Gleichungen | 9 / 10 | 9 / 10 | – | nur Gruppe I |
| 46 Kongruenzabbildungen: Etappe Drehung | 6 | 8 | – (keine Drehung in II/III) | nur M8 I LB2 |

**Gleich in beiden Gruppen, nicht pauschal verschieben (gesichert):**
- 97 Extremwerte quadratischer Terme: 8 in beiden Gruppen (M8 I LB4, M8 II/III LB3).
- 74 Zweireihige Determinanten: 7 in beiden Gruppen (M7 I und M7 II/III, jeweils LB2), weitergeführt in 8 (Funktionen) und 9 II/III.
- Stochastik in beiden Gruppen gleich:
  - 8: Ergebnis/Ereignis, Baumdiagramm und Vierfeldertafel als Darstellung, Häufigkeiten.
  - 9: Laplace, Ergebnisraum, Gegenereignis, Gesetz der großen Zahlen.
  - 10: Pfadregeln (62).
- 26 Dreisatz beginnt in beiden Gruppen in 5 (M5 LB4), die Proportionalität in 6.

**Berichtigung meiner Meldung von 13:00:**
- Ich hatte vorgeschlagen, Thema 61 nach Klasse 8 zu legen. Das war zu grob.
- 61 erstreckt sich über zwei Klassen: Die Etappen *Ergebnis, Ergebnisraum, Ereignis* und *Relative Häufigkeit* gehören in 8. *Laplace*, *Laplace prüfen*, *Gegenereignis* und *Gesetz der großen Zahlen* gehören in 9.
- Die Zuordnungen selbst bleiben richtig; nur das Etikett ändert sich: In 9 heißt es jetzt „neu (Etappen …)“ statt „weitergeführt“.
- Die Klasse von 61 bleibt im SQL unverändert.

**Widersprüche im Repo (gesichert, Stand `lernen-app` b3591695):**
- Die Themendateien `inhalte/themen/*.json` und `themenliste.json` nennen verschiedene RS-Klassen:
  - 61: Datei 8, Liste und DB 9.
  - 44: Datei 6, Liste und DB 7.
  - 91: Datei 5, Liste und DB 8.
  - 101: Datei ohne RS-Klasse, Liste und DB 9.
  - 99 und 100: Datei ohne RS-Klasse, Liste und DB 6.
- 48 und 78 (stillgelegt) haben in der Liste und in der DB keine Klasse mehr, in den Themendateien noch (7 bzw. 8).
- Etappen, die in eine andere Klasse gehören:
  - 46 (RS 6) enthält Drehung und Punktspiegelung, die zu 8 I gehören.
  - 33 enthält Ursprungsgerade (8) und allgemeine Gerade mit Parametern (9 für II/III).
  - 91 enthält Raumlage (7 I / 8 II/III) und Rotationskörper (10 II/III).

**Bezug neu/weitergeführt:**
- Bisher hing das Etikett an `rs_by`. Jetzt berechne ich es je Gruppe aus der ersten Klasse mit Hauptbezug:
  - „neu“: das Thema kommt in dieser Gruppe zum ersten Mal.
  - „weitergeführt“: das Thema kam in einer früheren Klasse schon vor.
  - „neu (Etappen …)“: das Thema ist bekannt, aber der Punkt bringt neue Etappen (Liste `neue_etappen` in der JSON).
- Damit heißt z. B. 44 in 8 II/III jetzt „neu“, nicht „weitergeführt“.

Seit der Entscheidung „Maßstab Gruppe I“ (13:45) ändert das SQL genau eine Klasse: 91 → 7. Alle anderen `rs_by` stimmen mit der ersten Gruppe-I-Klasse überein oder hängen an Etappen (26, 61). Mit `rs_by` allein lässt sich die Lage von Gruppe II/III nicht abbilden; das leistet das Datenmodell in Abschnitt 6.

## 5 Stichprobe Gymnasium 7 und 8 (nur Bericht, kein SQL)

| | Gym 7 | Gym 8 |
|---|---|---|
| Stunden je Lernbereich | alle gleich | alle gleich |
| Punkte Original / DB | 32 / 39 | 27 / 39 |
| Punkte mit Hauptthema vorher → Vorschlag | 14 → 39 | 23 → 39 |
| falsches Hauptthema | 1.2/k1: Potenzgesetze hängen an 30 statt 102 | 4/k3: ganzzahlige Exponenten an 30 statt 103 |
| Lücken | keine | keine |

- Auch im Gymnasium teilt die DB feiner als das Original. Die Zuordnungslücken sind dort ähnlich groß wie in RS 7. Das betrifft die echten Kinder (Gym).
- Eine Korrektur wäre ein eigener Auftrag. Der Vorschlag je Punkt steht in der JSON (`korrektur_sql: false`).
- Klassen Gym passen; 93 und 51 liegen im Gymnasium in 8, in der Realschule in 7 bzw. 9. `gym_by` ist dafür getrennt hinterlegt.

## 6 Datenmodell: Gruppe × Klasse × Lernbereich × Punkt → Thema/Etappe (für bau-lehrer, verbindlich laut Nachtrag)

Entwurf, nicht eingespielt. Die Namen sind Vorschläge; die Grundsätze sind fest.

**Grundsätze**
1. Der Lehrplan beschreibt, *wann* etwas dran ist: Gruppe × Klasse × Lernbereich × Punkt. Das Thema beschreibt, *was* gelernt wird (Etappen). Die Zuordnung verbindet beides.
2. Der Lernstand hängt nur an Thema und Etappe, nie an Gruppe, Klasse oder Lehrplanpunkt. Kommt ein Thema in 8 und 9 vor, gibt es **einen** Lernstand und **einen** Satz Sterne.
3. Die Klasse eines Themas wird für das Kind aus seiner Gruppe abgeleitet. `klasse_fest` bleibt nur als Ausnahme (Sebastians harte Entscheidungen, z. B. 102 ← 30).

**Struktur (ist schon fast da)**

| Ebene | heute | Ergänzung |
|---|---|---|
| Gruppe × Klasse | `schule.quelle` (zweig `rs_I`/`rs_II_III`, `jahr_von`) | RS 5/6 haben schon zweig `allgemein` (gilt für beide Gruppen) |
| Lernbereich, Punkt | `schule.eintrag` (art lernbereich/kompetenz, Stunden am Lernbereich) | Prüfregel: Zahl der Punkte je Lernbereich = Original; Teilpunkte nur als `art = 'teilpunkt'` mit Verweis auf den Originalpunkt |
| Punkt → Thema | `schule.zuordnung` (bezug haupt/neben) | Felder `rolle` und `etappen`, s. u. |
| Punkt → Etappe | – | `etappen text[]` (Lernziel-Schlüssel aus `inhalte/themen`), leer = ganzes Thema |

```sql
-- Entwurf, nicht einspielen
alter table schule.zuordnung
  add column rolle text check (rolle in ('neu', 'weitergefuehrt')),
  add column etappen text[];          -- lernziel-Schlüssel; null = alle Etappen des Themas
alter table schule.lernender
  add column zweig text check (zweig in ('rs_I', 'rs_II_III'));   -- nur für schulart rs_by; Vorgabe rs_I (Entscheidung 22.11.)

-- Lage je Thema (und Etappe) und Gruppe, abgeleitet, nicht gepflegt
create view schule.thema_lage as
select q.schulart, q.zweig,   -- 'allgemein' (RS 5/6) gilt für rs_I und rs_II_III z.thema_id, et.lernziel,
       min(q.jahr_von) filter (where z.bezug = 'haupt') as klasse_ab,
       array_agg(distinct q.jahr_von order by q.jahr_von) as klassen
from schule.zuordnung z
join schule.eintrag e on e.id = z.eintrag_id and not e.archiviert
join schule.quelle q on q.id = e.quelle_id and q.aktiv
left join lateral unnest(z.etappen) as et(lernziel) on true
group by 1, 2, 3, 4;

-- Abdeckung nach Stunden statt nach Themenzahl
create view schule.lehrplan_abdeckung as
select lb.quelle_id, lb.pfad, lb.text as lernbereich, lb.stunden,
       count(k.id) as punkte,
       count(k.id) filter (where exists (select 1 from schule.zuordnung z where z.eintrag_id = k.id and z.bezug = 'haupt')) as punkte_mit_thema,
       round(lb.stunden * count(k.id) filter (where exists (select 1 from schule.zuordnung z where z.eintrag_id = k.id and z.bezug = 'haupt'))::numeric
             / nullif(count(k.id), 0), 1) as stunden_abgedeckt
from schule.eintrag lb
join schule.eintrag k on k.pfad like lb.pfad || '/%' and k.quelle_id = lb.quelle_id and k.art = 'kompetenz' and not k.archiviert
where lb.art = 'lernbereich'
group by lb.id;
```

**Regeln für die App**
- Die Klasse für ein Kind ist `thema_lage.klasse_ab` für Schulart und Zweig des Kindes. RS 5/6 gelten für beide Gruppen; `klasse_fest` gewinnt nur, wenn es gesetzt ist.
- Etappen mit späterer `klasse_ab` werden erst ab dieser Klasse verlangt, z. B. 61 Laplace ab 9 und 33 allgemeine Gerade ab 9 für II/III. Vorher sind sie freiwillig („schon können“). Nichts wird doppelt gezählt.
- Themen ohne Lehrplanpunkt in der Gruppe des Kindes sind dort kein Pflichtstoff, z. B. 49, 36 und 96 für II/III.
- Die Matrix zeigt je Lernbereich die abgedeckten Stunden statt der Zahl der Themen. RS 8 I LB4 (40 Std., 3 Punkte, 1 Thema) steht dann bei 100 %.

**Befüllung:**
- `rolle` und `etappen` je Punkt liefert die JSON (`zuordnung_vorschlag[].klasse_bezug`, `neue_etappen`). Das Korrektur-SQL schreibt die Rolle bisher nur in `begruendung` der geänderten Zuordnungen. Die Felder selbst kann bau-lehrer nach dem Schemaschritt aus der JSON füllen.
- Entschieden (22.11., 13:45): Maßstab ist Gruppe I. Das Modell führt trotzdem beide Gruppen. Bis `lernender.zweig` existiert, gilt für jedes RS-Kind `rs_I`. Echte RS-Kinder gibt es derzeit nicht.

## 7 Korrektur-SQL `rs_korrektur_2211.sql` (Maßstab Gruppe I)

Grundlage ist die Entscheidung von Sebastian vom 22.11., 13:45 (AUFTRAEGE, `lernen-app` 01caab63): Gruppe I ist der Maßstab der App.

- **Umfang:** RS 5 und 6 (gelten für beide Gruppen) und 7 I, 8 I, 9 I, 10 I, also die Quellen 7, 8, 24, 12, 13 und 15.
- **Gruppe II/III** (25, 26, 14, 16) wird nicht angefasst. Der Vorschlag je Punkt steht in der JSON (`korrektur_sql: false`).
- **Erlaubte Befehle:** nur INSERT/UPDATE auf `schule.zuordnung`, `schule.eintrag` und `schule.thema`; kein DROP, kein DELETE.
- **Reihenfolge:**
  1. 31 alte Hauptbezüge zuerst auf Neben (eindeutiger Hauptbezug je Eintrag),
  2. 6 Zuordnungen umhängen,
  3. 27 veraltete kennzeichnen (Neben + „klaerungsbedarf“),
  4. 8 Nebenbezüge zu Hauptbezügen,
  5. 87 Zuordnungen ergänzen,
  6. 26 Lernbereichstitel,
  7. Prüfstatus „geprueft“ für die Lernbereiche und die Punkte 7–10 I,
  8. **Klasse: Thema 91 `rs_by` 8 → 7.** In Gruppe I stehen Schrägbilder und Raumlage in 7 (M7 I LB4). Die übrigen Abweichungen bei Gruppe I ändern keine Klasse:
     - 26: Dreisatz 5, Proportionalität 6.
     - 61: Etappen in 8 und 9.
     - Beides bleibt, bis es Etappenklassen gibt (Abschnitt 6).
- Auch die Zuordnungen auf Lernbereichsebene werden bereinigt (z. B. Raumgeometrie 6 → 100, 8 I → 91, 9 I → 92). Die Lernbereiche von II/III bleiben, wie sie sind.
- **Rauchtest** (bricht mit Fehler ab, die Transaktion rollt zurück):
  - a) alle 305 erwarteten Zuordnungen mit Bezug vorhanden,
  - b) Lücken in Gruppe I genau 297, 298, 871, 937,
  - c) `thema_jahrgang` aller Themen unverändert außer 91 (nur `rs_by` → 7),
  - d) kein Hauptbezug auf stillgelegte Themen in den Gruppe-I-Quellen.
- **Probelauf auf lokalem Postgres 16** mit dem echten Stand **nach dem Live von 13:45**. Ich habe die DB nach dem Live neu gelesen: Zuordnungen und Einträge sind unverändert. Die zehn stillgelegten Themen haben jetzt `klasse_fest` = null, die Stilllegung ist also wirksam.
  - Die Testkopie liefert für alle Themen dieselbe `rs_by` wie die DB.
  - Der Probelauf ist bestanden, der zweite Lauf ebenfalls (wiederholbar).
  - Gegenprobe mit einer künstlich geänderten Klasse (Thema 100): Abbruch bei Rauchtest c, nichts geändert.
- **Einspielen:** `psql -1 -f` bzw. als eine Transaktion. Ohne Transaktion bricht Rauchtest c bewusst ab.
- **Danach im Repo nachziehen:** `inhalte/themenliste.json` und `inhalte/themen/raum.schraegbilder.json` auf `rs_by` 7. Die Themendatei steht heute auf 5.
- Die Rolle neu/weitergeführt schreibt das SQL nur in `begruendung` der geänderten Zuordnungen. Für alle Punkte steht sie in der JSON.

## Gesichert / Annahme / offen

**Gesichert (Original und DB, 22.11.):**
- Stunden aller RS-Lernbereiche.
- Punktzahl RS 7–10.
- Feinere Teilung RS 5/6 und Gym.
- Titelabweichungen.
- Zuordnungsstand vorher. Abgleich gegen DB: 0 Abweichungen zu meinen Vorher-Daten.
- Die Lücken.
- Die Gruppenlage je Thema (Abschnitt 4), von ChatGPT 927/928/930 unabhängig bestätigt.
- Die Widersprüche zwischen Themendateien und `themenliste.json` bei 61, 44, 91, 99, 100 und 101.
- Zweitquellen 5, 7 I (Westermann), 8 I, 8 II/III, 9 I, 9 II/III, 10 I und die Abschlussprüfungen 2026 I und II/III ohne Widerspruch.

**Annahme:**
- Die Zuordnung Punkt → Thema beruht auf meinem inhaltlichen Urteil (Kurzfassung, Original-Punkt, Etappen des Themas). Vor allem diese Fälle sind diskutierbar:
  - 1/K3 RS 7 (19 statt 30 als Haupt),
  - 53 vs. 99/100 in RS 6,
  - 46 für Vierecke ordnen (8).
- Kurzfassungen „sinngemäß richtig“ ohne Einzelprotokoll.
- Etappen-Etiketten in `neue_etappen` nach Etappentiteln der Themendateien beurteilt.
- „teilweise“ heißt: eine Etappe fehlt, nach Titeln der Etappen beurteilt, nicht nach Aufgaben.

**Offen:**
- Zweitquellen 6, 7 II/III und 10 II/III (Pläne nicht lesbar).
- Gruppe II/III: Korrektur nur als Vorschlag in der JSON, kein SQL (Entscheidung Gruppe I).
- Repo nachziehen: Klasse 91 in `themenliste.json` und in der Themendatei.
- Schemaschritt `rolle`/`etappen`/`lernender.zweig` (bau-lehrer).
- Die Etappenzuordnung je Punkt ist erst für die Themen mit Klassenwechsel gemacht (`neue_etappen`), noch nicht für alle Punkte.
- Themen für die 3 Lücken.
- Gym-Korrektur als eigener Auftrag.

## Quellen (alle abgerufen 22.11.2026)

- LehrplanPLUS Realschule Mathematik:
  - [5](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/5/mathematik/mathe), [6](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/6/mathematik/mathe)
  - 7 [I](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/7/mathematik/wpfg1) / [II/III](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/7/mathematik/wpfg2-3)
  - 8 [I](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/8/mathematik/wpfg1) / [II/III](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/8/mathematik/wpfg2-3)
  - 9 [I](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/9/mathematik/wpfg1) / [II/III](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/9/mathematik/wpfg2-3)
  - 10 [I](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/10/mathematik/wpfg1) / [II/III](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/10/mathematik/wpfg2-3)
- LehrplanPLUS Gymnasium Mathematik: [7](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik), [8](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/8/mathematik)
- C.C. Buchner Mathe.Logo Bayern: Stoffverteilungspläne und Produktseiten wie in Abschnitt 2.
- Westermann Mathematik 7 Wpfg. I, Inhaltsverzeichnis (kapiert.de), Link in Abschnitt 2.
- ISB:
  - Infobrief Mathematik 2023,
  - Abschlussprüfung 2026 Mathematik I und II/III,
  - Abschlussprüfung 2021 Mathematik I,
  - Jahrgangsstufentests 8 I und 8 II/III 2025.
  - Links in Abschnitt 2.
