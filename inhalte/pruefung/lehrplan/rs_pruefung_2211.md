# Prüf-Auftrag LP-RS – Realschul-Lehrplan Punkt für Punkt (22.11.2026)

Abruf aller Lehrplanseiten und Zweitquellen am 22.11.2026; Datenbank nur gelesen (Stand 22.11.2026). Nichts eingespielt. Keine Lehrplantexte wörtlich, nur Lernbereichstitel und eigene Kurzbeschreibungen.

Lieferung:
- dieser Bericht,
- `rs_pruefung_2211.json` (je Punkt: Quelle, Lernbereich, Punkt, Eintrag, Zuordnung vorher/Vorschlag, Bezug, Befund),
- `rs_korrektur_2211.sql` (nur INSERT/UPDATE; Probelauf auf einer lokalen Kopie des echten Vorherstands bestanden, zweimal hintereinander, Gegenprobe bricht ab).

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

Die vier im Auftrag genannten fehlenden Zuordnungen sind nach der Korrektur geschlossen: RS 7 Dreiecke → 44, RS 7 Ortslinien → 73/45, RS 8 Daten und Zufall → 61, RS 9 Kreis → 51.

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
| 7 I | [Produktseite 7 I](https://www.ccbuchner.de/produkt/mathe-logo-bayern-7-i-3661) | **offen**: nicht lesbar |
| 7 II/III | [Produktseite 7 II/III](https://www.ccbuchner.de/produkt/mathe-logo-bayern-7-ii-iii-3662) | **offen**: nicht lesbar |
| 8 I | [Stoffverteilungsplan 8 I](https://www.ccbuchner.de/_files_media/mediathek/downloads/15120.pdf) | Stunden aller 7 Lernbereiche gleich; Vierecke, Drehung und Daten und Zufall (Baumdiagramm, Vierfeldertafel) sind Stoff der 8. Reihenfolge abweichend (Daten und Zufall zuerst) – kein Widerspruch |
| 8 II/III | [Stoffverteilungsplan 8 II/III](https://www.ccbuchner.de/_files_media/mediathek/downloads/15117.pdf) | Stunden aller 6 Lernbereiche gleich |
| 9 I | [Stoffverteilungsplan 9 I](https://www.ccbuchner.de/_files_media/mediathek/downloads/15129.pdf) | gleich; Buch teilt LB 7 in quadratische Funktionen (25) und Gleichungen (17) = 42 |
| 9 II/III | [Stoffverteilungsplan 9 II/III](https://www.ccbuchner.de/_files_media/mediathek/downloads/15128.pdf) | gleich |
| 10 I | [Stoffverteilungsplan 10 I](https://www.ccbuchner.de/_files_media/mediathek/downloads/15126.pdf) | gleich; Trigonometrie 17 + 17 + 8 (Skalarprodukt) = 42; zusätzlich ein Kapitel Prüfungsvorbereitung |
| 10 II/III | [Produktseite 10 II/III](https://www.ccbuchner.de/produkt/mathe-logo-bayern-10-ii-iii-4164) | **offen**: nicht lesbar |

Abschlussprüfung (9/10):
- [ISB Infobrief Mathematik 2023](https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Infobriefe/Mathematik/Infobrief_Mathematik_2023.pdf): Für Mathematik I sind Rotationskörper und Potenzfunktionen wieder prüfungsrelevant. Beide sind nach der Korrektur zugeordnet (91/92 und 96/36).
- [Abschlussprüfung 2021 Mathematik I](https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Mathematik/Weiterentwicklung_Abschlusspruefung/Zeichenkatalog/2021_MI_HT.pdf): Die Aufgaben nutzen Abbildungen mit Vektoren/Matrizen, Trigonometrie, Exponentialfunktionen und Raumgeometrie. Alle Bereiche stehen im Lehrplan 9/10 I und haben ein Thema, **außer der Vektorrechnung als eigenem Werkzeug** (siehe Lücken).
- Zusätzlich die [ISB-Jahrgangsstufentests 8 I 2025](https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/2025_JT_Mathematik_8_I_Angabe.pdf) und 8 II/III. Sie prüfen Drehung, Vektor/Mittelpunkt, Determinante und Thaleskreis, also genau die Inhalte der 8. Das bestätigt die Klassenlage.

**Widersprüche Zweitquelle ↔ amtlich:** keine in den lesbaren Plänen. Offen sind 6, 7 I, 7 II/III und 10 II/III, weil die Pläne nicht lesbar sind. Amtlich gilt.

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
| 4 | Größen | 20 | 6/6 | 4 → 6 | – | 25 Größen und Einheiten (neu); 26 Direkte Proportionalität und Dreisatz (vorgezogen) |
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
| 6 | Direkte Proportionalität | 12 | 4/6 | 6 → 6 | – | 24 Prozent- und Zinsrechnung (neu); 26 Direkte Proportionalität und Dreisatz (neu) |
| Σ | | | 32/40 | 30 → 40 | | |

#### Realschule 7 – Gruppe I (Quelle 24)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Potenzen | 10 | 3/3 | 1 → 3 | – | 19 Zehnerpotenzen und wissenschaftliche Schreibweise (neu); 30 Potenzen und negative Exponenten (neu); 102 Potenzgesetze (neu) |
| 2 | Parallelverschiebung | 23 | 7/7 | 3 → 6 | 2/K4 | 46 Kongruenzabbildungen (weitergeführt); 74 Zweireihige Determinanten (neu); 98 Winkelsätze (neu) |
| 3 | Dreiecke | 14 | 4/4 | 0 → 4 | – | 44 Konstruktionen, Kongruenz und Beweise (neu) |
| 4 | Raumgeometrie | 10 | 3/3 | 3 → 3 | – | 91 Schrägbilder und Raumdarstellung (vorgezogen) |
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
| 1 | Vierecke | 12 | 2/2 | 2 → 2 | – | 44 Konstruktionen, Kongruenz und Beweise (weitergeführt); 46 Kongruenzabbildungen (weitergeführt) |
| 2 | Drehung | 6 | 5/5 | 0 → 4 | 2/K5 | 46 Kongruenzabbildungen (weitergeführt) |
| 3 | Raumgeometrie | 13 | 3/3 | 3 → 3 | – | 91 Schrägbilder und Raumdarstellung (neu) |
| 4 | Terme, Gleichungen und Ungleichungen | 40 | 3/3 | 3 → 3 | – | 2 Lineare Gleichungen (weitergeführt); 29 Terme umformen (weitergeführt); 97 Quadratische Terme und Extremwerte (neu) |
| 5 | Bruchterme und Bruchgleichungen | 7 | 2/2 | 2 → 2 | – | 5 Bruch- und Verhältnisgleichungen (neu); 31 Bruchterme (neu) |
| 6 | Funktionen | 26 | 6/6 | 6 → 6 | – | 32 Zuordnung und Funktion (neu); 33 Lineare Funktionen (neu) |
| 7 | Daten und Zufall | 8 | 2/2 | 1 → 2 | – | 61 Zufall und Laplace (vorgezogen) |
| Σ | | | 23/23 | 17 → 22 | | |

#### Realschule 8 – Gruppe II/III (Quelle 26)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Dreiecke und Vierecke | 16 | 5/5 | 2 → 5 | – | 44 Konstruktionen, Kongruenz und Beweise (weitergeführt); 46 Kongruenzabbildungen (weitergeführt) |
| 2 | Raumgeometrie | 7 | 2/2 | 2 → 2 | – | 91 Schrägbilder und Raumdarstellung (neu) |
| 3 | Terme und Gleichungen | 40 | 3/3 | 3 → 3 | – | 2 Lineare Gleichungen (weitergeführt); 29 Terme umformen (weitergeführt); 97 Quadratische Terme und Extremwerte (neu) |
| 4 | Bruchterme und Bruchgleichungen | 5 | 2/2 | 2 → 2 | – | 5 Bruch- und Verhältnisgleichungen (neu); 31 Bruchterme (neu) |
| 5 | Funktionen | 8 | 5/5 | 1 → 5 | – | 32 Zuordnung und Funktion (neu); 33 Lineare Funktionen (neu) |
| 6 | Daten und Zufall | 8 | 2/2 | 1 → 2 | – | 61 Zufall und Laplace (vorgezogen) |
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
| 8 | Daten und Zufall | 9 | 5/5 | 1 → 5 | – | 61 Zufall und Laplace (neu) |
| Σ | | | 38/38 | 30 → 38 | | |

#### Realschule 9 – Gruppe II/III (Quelle 14)

| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |
|---|---|---|---|---|---|---|
| 1 | Reelle Zahlen | 7 | 3/3 | 2 → 3 | – | 8 Quadratische Gleichungen (allgemein) (neu); 20 Wurzeln und reelle Zahlen (neu) |
| 2 | Zentrische Streckung | 13 | 3/3 | 0 → 3 | – | 47 Ähnlichkeit und Strahlensätze (neu) |
| 3 | Rechtwinklige Dreiecke | 20 | 6/6 | 6 → 6 | – | 54 Satz des Pythagoras (neu); 55 Trigonometrie im rechtwinkligen Dreieck (neu) |
| 4 | Kreis | 10 | 2/2 | 0 → 2 | – | 51 Kreisberechnungen (neu) |
| 5 | Lineare Funktionen | 15 | 4/4 | 4 → 4 | – | 33 Lineare Funktionen (weitergeführt) |
| 6 | Systeme linearer Gleichungen | 10 | 1/1 | 1 → 1 | – | 6 Gleichungssysteme mit 2 Unbekannten (neu) |
| 7 | Daten und Zufall | 9 | 5/5 | 1 → 5 | – | 61 Zufall und Laplace (neu) |
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
| 2 | Raumgeometrie | 20 | 5/5 | 5 → 5 | – | 91 Schrägbilder und Raumdarstellung (weitergeführt); 92 Pyramide, Kegel, Kugel (weitergeführt) |
| 3 | Exponentialfunktionen, Logarithmen | 10 | 3/3 | 1 → 3 | – | 10 Exponentialgleichungen (neu); 37 Exponential- und Logarithmusfunktionen (neu) |
| 4 | Quadratische Funktionen und quadratische Gleichungen | 35 | 6/6 | 2 → 6 | – | 8 Quadratische Gleichungen (allgemein) (weitergeführt); 35 Quadratische Funktionen (weitergeführt) |
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

## 4 Klasse je Thema (Realschule, `klasse_fest.rs_by`)

Alle Themen mit `rs_by` kommen im Original vor; alle bis auf die unten genannten in genau der hinterlegten Klasse (erste Klasse mit Hauptbezug).

**Abweichend oder gruppenabhängig (gesichert, Beleg = Lernbereich im Original):**

| Thema | rs_by | laut Original zuerst | Beleg | Bewertung |
|---|---|---|---|---|
| 26 Direkte Proportionalität und Dreisatz | 6 | 5 (Dreisatz) | M5 LB4, M6 LB6 | Dreisatz beginnt in 5, Proportionalität als Zuordnung in 6. Klasse 6 vertretbar; Dreisatz-Etappe gehört nach vorn oder in 25 |
| 61 Zufall und Laplace | 9 | 8 (beide Gruppen) | M8 LB7 (I), M8 LB6 (II/III), M9 LB8/LB7 | **falsch**: Ergebnis, Ereignis, Baumdiagramm und Vierfeldertafel sind Stoff der 8. Vorschlag `rs_by` 8 |
| 44 Konstruktionen, Kongruenz | 7 | I: 7, II/III: 8 | M7 LB3 (I), M8 LB1 (II/III) | Gruppenunterschied, nur mit Klasse je Zweig abbildbar |
| 91 Schrägbilder und Raumdarstellung | 8 | I: 7, II/III: 8 | M7 LB4 (I), M8 LB2 (II/III) | Gruppenunterschied |
| 35 Quadratische Funktionen | 9 | I: 9, II/III: 10 | M9 LB7 (I), M10 LB4 (II/III) | Gruppenunterschied |
| 92 Pyramide, Kegel, Kugel | 9 | I: 9, II/III: 10 | M9 LB5 (I), M10 LB2 (II/III) | Gruppenunterschied |
| 33 Lineare Funktionen | 8 | I: 8; II/III: 8 (nur Ursprungsgeraden), 9 (allgemein) | M8 LB6, M8 LB5 (II/III), M9 LB5 (II/III) | passt; für II/III über zwei Klassen verteilt |

**Nur Nebenbezug, kein eigener Punkt:**
- 9 Potenzgleichungen (10), 43 Mit Winkeln rechnen (5), 63, 64, 68 (9), 69 Intervalle (7), 101 (9) und 103 (7).
- Die Klassen sind plausibel, aber nicht durch einen eigenen Lehrplanpunkt belegt.

**Stillgelegte Themen** 12, 40, 48, 77 und 78 tragen in der DB weiter `rs_by`; 907 b ist noch nicht eingespielt. Das SQL setzt alle Zuordnungen auf sie auf Neben + „klaerungsbedarf“ und löscht nichts.

Das SQL ändert **keine Klasse** (Rauchtest c). `rs_by` für 61 und eine Klasse je Zweig sind Entscheidungen für Sebastian bzw. bau-lehrer.

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

## 6 Vorschlag Datenmodell (für bau-lehrer)

1. **Bezug „neu“/„weitergeführt“ als eigenes Feld.** `schule.zuordnung` bekommt `rolle text check (rolle in ('neu','weitergefuehrt','vorgezogen'))`, getrennt von `bezug` (haupt/neben). Heute steht das nur in `begruendung`. Ableitbar aus Lehrplanklasse und Themenklasse, aber als Feld prüfbar.
2. **Klasse je Zweig.** `klasse_fest` um `rs_by_I` und `rs_by_II_III` ergänzen. `thema_jahrgang` nimmt den Zweig des Kindes; `rs_by` bleibt Rückfallwert. Betrifft 35, 44, 91 und 92 (Abschnitt 4).
3. **Ein Thema über mehrere Klassen.** Kein Kopieren des Themas: Es reichen die Zuordnungen mit Rolle „weitergeführt“ in den späteren Klassen. Die Etappen bekommen optional eine Klasse, ab der sie gelten (z. B. 33: Ursprungsgerade 8, allgemeine Gerade 9 für II/III).
4. **Matrix nach Stunden statt Themenzahl.** Abdeckung je Lernbereich = Summe der Stunden der Punkte mit Hauptbezug / Stunden des Lernbereichs, Stunden anteilig auf die Punkte verteilt. Ansicht `schule.lehrplan_abdeckung(quelle_id, lernbereich, stunden, punkte, punkte_mit_haupt, stunden_abgedeckt, luecken)`. Dann zeigt RS 8 LB4 (40 Std., 3 Punkte, 1 Thema) 100 % statt „nur ein Thema“. Die Themenzahl sagt nichts über die Abdeckung.
5. **Punktgenauigkeit sichern.** Prüfregel: Zahl der Kompetenzpunkte je Lernbereich = Original. Für RS 5/6 und Gym die Teilpunkte entweder zusammenlegen oder als `art = 'unterpunkt'` mit Verweis auf den Originalpunkt führen.

## 7 Korrektur-SQL `rs_korrektur_2211.sql`

- Nur RS 5–10; nur INSERT/UPDATE auf `schule.zuordnung` und `schule.eintrag`; `schule.thema` unverändert; kein DROP, kein DELETE.
- Reihenfolge:
  1. alte Hauptbezüge zuerst auf Neben (eindeutiger Hauptbezug je Eintrag),
  2. 10 Zuordnungen umhängen,
  3. 32 veraltete kennzeichnen,
  4. 10 Nebenbezüge zu Hauptbezügen,
  5. 139 Zuordnungen ergänzen,
  6. 47 Titel,
  7. Prüfstatus „geprueft“ für Lernbereiche und RS-7–10-Punkte.
- Auch 18 Zuordnungen auf Lernbereichsebene werden bereinigt, z. B. Raumgeometrie 6 → 100, 7 I/8 → 91, 9 I/10 II/III → 92.
- Rauchtest (bricht mit Fehler ab, Transaktion rollt zurück):
  - a) alle 440 erwarteten Zuordnungen mit Bezug vorhanden,
  - b) Lücken genau 297, 298, 871, 909, 937,
  - c) `thema_jahrgang` aller Themen unverändert,
  - d) kein Hauptbezug auf stillgelegte Themen.
- Probelauf: auf lokalem Postgres 16 mit dem echten Vorherstand (alle Einträge und Zuordnungen der 10 Quellen, alle Themenklassen; gelesen 22.11.):
  - bestanden; zweiter Lauf ebenfalls (wiederholbar);
  - Gegenprobe mit künstlich geänderter Klasse → Abbruch, nichts geändert.
- Einspielen: `psql -1 -f` bzw. als eine Transaktion. Ohne Transaktion bricht Rauchtest c bewusst ab.

## Gesichert / Annahme / offen

**Gesichert (Original und DB, 22.11.):**
- Stunden aller RS-Lernbereiche.
- Punktzahl RS 7–10.
- Feinere Teilung RS 5/6 und Gym.
- Titelabweichungen.
- Zuordnungsstand vorher. Abgleich gegen DB: 0 Abweichungen zu meinen Vorher-Daten.
- Die Lücken.
- Die Klassen-Befunde 61, 26 und die Gruppenunterschiede.
- Zweitquellen 5, 8 I, 8 II/III, 9 I, 9 II/III, 10 I ohne Widerspruch.

**Annahme:**
- Die Zuordnung Punkt → Thema beruht auf meinem inhaltlichen Urteil (Kurzfassung, Original-Punkt, Etappen des Themas). Vor allem diese Fälle sind diskutierbar:
  - 1/K3 RS 7 (19 statt 30 als Haupt),
  - 53 vs. 99/100 in RS 6,
  - 46 für Vierecke ordnen (8).
- Kurzfassungen „sinngemäß richtig“ ohne Einzelprotokoll.
- „teilweise“ heißt: eine Etappe fehlt, nach Titeln der Etappen beurteilt, nicht nach Aufgaben.

**Offen:**
- Zweitquellen 6, 7 I, 7 II/III, 10 II/III (Pläne nicht lesbar).
- `rs_by` 61 → 8 und Klasse je Zweig (Entscheidung).
- Themen für die 3 Lücken.
- Gym-Korrektur als eigener Auftrag.
- 907 b (Stilllegung) noch nicht eingespielt.

## Quellen (alle abgerufen 22.11.2026)

- LehrplanPLUS Realschule Mathematik:
  - [5](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/5/mathematik/mathe), [6](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/6/mathematik/mathe)
  - 7 [I](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/7/mathematik/wpfg1) / [II/III](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/7/mathematik/wpfg2-3)
  - 8 [I](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/8/mathematik/wpfg1) / [II/III](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/8/mathematik/wpfg2-3)
  - 9 [I](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/9/mathematik/wpfg1) / [II/III](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/9/mathematik/wpfg2-3)
  - 10 [I](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/10/mathematik/wpfg1) / [II/III](https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/10/mathematik/wpfg2-3)
- LehrplanPLUS Gymnasium Mathematik: [7](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik), [8](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/8/mathematik)
- C.C. Buchner Mathe.Logo Bayern: Stoffverteilungspläne und Produktseiten wie in Abschnitt 2.
- ISB:
  - Infobrief Mathematik 2023,
  - Abschlussprüfung 2021 Mathematik I,
  - Jahrgangsstufentests 8 I und 8 II/III 2025.
  - Links in Abschnitt 2.
