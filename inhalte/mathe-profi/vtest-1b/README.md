# vtest-1b – Verstehens-Aufgaben für die Tests (Runde 1b)

Kennungen `VT1B-001` bis `VT1B-119`. Auftrag: `auftrag.md` (Kopie des Auftrags), Auswahl und Begründung: `auswahl.md`. Alles in diesem Ordner ist neu; nichts ist eingespielt, kein App-Code, keine Migration, nichts unter `tools/` geändert.
Je gewähltem Lernziel 7 Aufgaben: 1 **test** (`ersetzt_test: true`, die anspruchsvollste des Lernziels), 3 **korrektur** (Stufe 2) und 3 **sicherung** (gemischt Stufe 2 und 3). Je Lernziel mindestens 5 verschiedene Ideen (Feld `idee`), keine Idee öfter als zweimal, 7 verschiedene Bauarten (Typ, Form, Antwortform).

## Dateien

| Datei | Inhalt |
|---|---|
| `<einheit>.json` | die Aufgaben der Einheit (Format wie `inhalte/mathe-profi/vtest-1/auftrag.md` Abschnitt 9) |
| `th_<einheit>.py` | Quelltext der Aufgaben (Texte, Lösungen, Fehlbilder mit Rechnung, Ideen) |
| `kern.py`, `pruefhilfen.py` | Hilfen für den Bau (Aufgabenformen, Prüfungen, Dopplungsvergleich mit dem Bestand) |
| `bauen.py` | prüft alle Regeln und schreibt die JSON-Dateien, `README.md` und `sonderfaelle.md`; Aufruf `python3 -I inhalte/mathe-profi/vtest-1b/bauen.py`, Ende „OK“ |
| `gegenrechnung.py` | rechnet alle Lösungen und Fehlbilder aus den JSON-Dateien unabhängig nach, 24 Aufgaben zusätzlich ganz neu (Brute-Force, Gauß-Fläche); Ende „0 Abweichungen“ |
| `sonderfaelle.md` | Kurzvermerk je Auswahl-Aufgabe |

## Zahlen

| Einheit | Lernziel | test | korrektur | sicherung | Stufe 2 / 3 | Antwortformen (Zahl / Auswahl / Lücken) | Typen | Formen |
|---|---|---|---|---|---|---|---|---|
| Einheit | Lernziel | test | korrektur | sicherung | Stufe 2 / 3 | Antwortformen (Zahl / Auswahl / Lücken) | Typen | Formen |
|---|---|---|---|---|---|---|---|---|
| `bruch.prozent` | `prozentsatz` | 1 | 3 | 3 | 4 / 3 | 4 / 2 / 1 | begruenden 1, darstellung 2, einkleidung 1, fehler 1, transfer 1, umkehr 1 | ohne 3, bruecke 2, fehler_detektiv 1, umkehren 1 |
| `bruch.prozent` | `rabatt_aufschlag` | 1 | 3 | 3 | 4 / 3 | 5 / 1 / 1 | darstellung 2, fehler 1, mehrschritt 1, transfer 1, umkehr 1, verknuepfen 1 | ohne 2, bruecke 2, fehler_detektiv 1, umkehren 1, zwei_wege 1 |
| `bruch.prozent` | `verstehen` | 1 | 3 | 3 | 4 / 3 | 4 / 2 / 1 | begruenden 1, darstellung 1, einkleidung 1, fehler 1, mehrschritt 1, transfer 1, umkehr 1 | ohne 2, bruecke 3, fehler_detektiv 1, umkehren 1 |
| `gleichungen.bruch` | `definitionsmenge` | 1 | 3 | 3 | 4 / 3 | 3 / 3 / 1 | begruenden 1, darstellung 2, einkleidung 1, fehler 1, transfer 1, umkehr 1 | ohne 2, bruecke 3, fehler_detektiv 1, umkehren 1 |
| `gleichungen.bruch` | `ueber_kreuz` | 1 | 3 | 3 | 4 / 3 | 3 / 3 / 1 | darstellung 1, einkleidung 1, fehler 1, mehrschritt 1, parameter 1, pruefung 1, umkehr 1 | ohne 1, bruecke 2, fehler_detektiv 1, umkehren 1, verfahren_waehlen 1, zwei_wege 1 |
| `gleichungen.bruch` | `scheinloesung` | 1 | 3 | 3 | 4 / 3 | 4 / 2 / 1 | begruenden 1, darstellung 2, fehler 1, parameter 1, umkehr 2 | ohne 4, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `gleichungen.bruch` | `verhaeltnis` | 1 | 3 | 3 | 4 / 3 | 4 / 2 / 1 | darstellung 1, einkleidung 1, fehler 1, mehrschritt 1, parameter 1, transfer 1, umkehr 1 | ohne 1, bruecke 4, fehler_detektiv 1, umkehren 1 |
| `terme.potenzgesetze` | `negativer_exponent` | 1 | 3 | 3 | 4 / 3 | 4 / 2 / 1 | begruenden 1, darstellung 2, parameter 1, transfer 1, umkehr 2 | ohne 3, anwenden 1, bruecke 2, umkehren 1 |
| `terme.potenzgesetze` | `fehler_finden` | 1 | 3 | 3 | 4 / 3 | 2 / 4 / 1 | begruenden 1, darstellung 1, einkleidung 1, fehler 2, umkehr 2 | ohne 4, bruecke 1, fehler_detektiv 2 |
| `zahlen.potenzen_zehner` | `gross_wissenschaftlich` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | begruenden 1, darstellung 2, fehler 1, transfer 1, umkehr 2 | ohne 3, anwenden 1, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `zahlen.potenzen_zehner` | `negativer_exponent` | 1 | 3 | 3 | 4 / 3 | 4 / 2 / 1 | begruenden 1, darstellung 3, parameter 1, transfer 1, umkehr 1 | ohne 3, anwenden 1, bruecke 2, umkehren 1 |
| `zahlen.potenzen_zehner` | `vorsilben_klein` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | begruenden 1, darstellung 3, fehler 1, transfer 1, umkehr 1 | ohne 2, anwenden 1, bruecke 2, fehler_detektiv 1, umkehren 1 |
| `zahlen.potenzen_zehner` | `vergleichen_pruefen` | 1 | 3 | 3 | 4 / 3 | 4 / 2 / 1 | begruenden 1, darstellung 3, fehler 1, transfer 1, umkehr 1 | ohne 2, anwenden 1, bruecke 2, fehler_detektiv 1, umkehren 1 |
| `messen.flaechen_vielecke` | `dreieck` | 1 | 3 | 3 | 4 / 3 | 3 / 3 / 1 | begruenden 1, darstellung 2, fehler 1, mehrschritt 1, transfer 1, umkehr 1 | ohne 2, anwenden 1, bruecke 1, fehler_detektiv 1, umkehren 1, zwei_wege 1 |
| `messen.flaechen_vielecke` | `rueckwaerts` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | begruenden 1, darstellung 1, fehler 1, transfer 1, umkehr 3 | ohne 2, anwenden 1, bruecke 2, fehler_detektiv 1, umkehren 1 |
| `messen.flaechen_vielecke` | `zusammengesetzt` | 1 | 3 | 3 | 4 / 3 | 4 / 2 / 1 | begruenden 1, darstellung 2, fehler 1, mehrschritt 1, transfer 1, umkehr 1 | ohne 2, anwenden 1, bruecke 1, fehler_detektiv 1, umkehren 1, zwei_wege 1 |
| `messen.flaechen_vielecke` | `verstehen` | 1 | 3 | 3 | 4 / 3 | 4 / 2 / 1 | begruenden 1, darstellung 3, fehler 1, parameter 1, umkehr 1 | ohne 3, bruecke 2, fehler_detektiv 1, umkehren 1 |
| Summe | 17 Lernziele | 17 | 51 | 51 | 68 / 51 | 61 / 38 / 20 | | |

Typen insgesamt:

| Typ | Aufgaben | Anteil |
|---|---|---|
| darstellung | 33 | 28 % |
| umkehr | 23 | 19 % |
| fehler | 16 | 13 % |
| begruenden | 14 | 12 % |
| transfer | 13 | 11 % |
| einkleidung | 6 | 5 % |
| mehrschritt | 6 | 5 % |
| parameter | 6 | 5 % |
| verknuepfen | 1 | 1 % |
| pruefung | 1 | 1 % |

Formen insgesamt:

| Form | Aufgaben | Anteil |
|---|---|---|
| (ohne Form) | 41 | 34 % |
| bruecke | 33 | 28 % |
| umkehren | 16 | 13 % |
| fehler_detektiv | 16 | 13 % |
| anwenden | 8 | 7 % |
| zwei_wege | 4 | 3 % |
| verfahren_waehlen | 1 | 1 % |

## Kennungen

| Einheit | Kennungen | Aufgaben |
|---|---|---|
| `bruch.prozent` | VT1B-001 bis VT1B-021 | 21 |
| `gleichungen.bruch` | VT1B-022 bis VT1B-049 | 28 |
| `terme.potenzgesetze` | VT1B-050 bis VT1B-063 | 14 |
| `zahlen.potenzen_zehner` | VT1B-064 bis VT1B-091 | 28 |
| `messen.flaechen_vielecke` | VT1B-092 bis VT1B-119 | 28 |

Fehlbilder: 366 insgesamt; bei Zahl- und Lückenaufgaben trägt jedes Fehlbild eine ausführbare Rechnung (`rechnung`), bei Auswahl steht die falsche Möglichkeit mit der Beschreibung des Denkfehlers.

## Regeln dieser Runde (vom Bauskript geprüft)

- Antwortformen nur `zahl`, `luecken` (ganze Zahlen) und `auswahl` mit genau 4 Möglichkeiten und genau einer richtigen; Rundungsregel steht im Text, wo gerundet würde (hier wird nirgends gerundet).
- Fehler-Detektiv nur als Lücken („Fehler in Zeile □, richtig: □“, mindestens 3 Zeilen) oder Auswahl mit mindestens 4 Zeilen, deren Möglichkeiten nach Zeile geordnet sind und jeweils eine Begründung nennen.
- Position der richtigen Möglichkeit gleichmäßig auf die vier Plätze verteilt; die richtige Möglichkeit ist höchstens in 35 % der Fälle die längste.
- Zahlen im Text eines Fehlbilds stammen aus der Aufgabe oder aus der Rechnung des Fehlbilds; Lösungen sind zweifach gerechnet; Dopplungsprüfung gegen `inhalte/themen`, `rollend-*` und andere `vtest-*`.
- Geometrie ohne Bild: Figuren sind vollständig durch Maße oder Koordinaten beschrieben (kein `grafik`-Feld).

## Offene Zweifel

- Lehrplanzuordnung: Die Lernbereiche stammen aus `inhalte/themenliste.json` (M6 1, M6 2, M6 3, M8 4). Ob negative Exponenten und wissenschaftliche Schreibweise im Gymnasium der Jahrgangsstufe 6 genau so im Lernbereich M6 1 stehen, ist am Repo nicht zu belegen und sollte geprüft werden.
- `regel` ist nicht gesetzt (je Aufgabe nur eine Lernkarten-Regel wäre geraten), daher meldet `tools/vtest_pruefen.py` dafür Hinweise; eine `regeln-zuordnung.md` gibt es deshalb nicht.
- Mehrdeutigkeit: In den Koordinaten- und Maßaufgaben ist jede Seite und jeder Winkel ausdrücklich genannt; bei Aufgaben zu „Höhe liegt außen“ ist die Lage der Spitze im Text angegeben.
