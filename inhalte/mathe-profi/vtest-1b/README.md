# vtest-1b – Verstehens-Aufgaben für die Tests (Runde 1b)

Kennungen `VT1B-001` bis `VT1B-119`. Auftrag: `auftrag.md` (Kopie des Auftrags), Auswahl und Begründung: `auswahl.md`. Alles in diesem Ordner ist neu; nichts ist eingespielt, kein App-Code, keine Migration, nichts unter `tools/` geändert.
Je gewähltem Lernziel 7 Aufgaben: 1 **test** (`ersetzt_test: true`, die anspruchsvollste des Lernziels), 3 **korrektur** (Stufe 2) und 3 **sicherung** (gemischt Stufe 2 und 3). Je Lernziel sind die 7 Aufgaben mit 7 verschiedenen `idee`-Einträgen beschriftet; **die Beschriftung ist nicht die Denkfigur.** Von Hand nach Denkfiguren gruppiert (Tabelle unten) kommen je Lernziel 5 bis 7 verschiedene Denkfiguren vor, keine öfter als zweimal. 7 verschiedene Bauarten (Typ, Form, Antwortform) je Lernziel.

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
| `bruch.prozent` | `prozentwert` | 1 | 3 | 3 | 4 / 3 | 3 / 1 / 3 | darstellung 2, einkleidung 1, fehler 1, transfer 2, umkehr 1 | ohne 4, bruecke 1, fehler_detektiv 1, zwei_wege 1 |
| `bruch.prozent` | `grundwert` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | begruenden 1, darstellung 2, fehler 1, transfer 1, umkehr 2 | ohne 5, fehler_detektiv 1, umkehren 1 |
| `bruch.prozent` | `verstehen` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | begruenden 1, darstellung 1, einkleidung 1, fehler 1, transfer 1, umkehr 2 | ohne 4, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `gleichungen.bruch` | `definitionsmenge` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | begruenden 1, darstellung 1, einkleidung 1, fehler 1, transfer 1, umkehr 2 | ohne 3, bruecke 2, fehler_detektiv 1, umkehren 1 |
| `gleichungen.bruch` | `ueber_kreuz` | 1 | 3 | 3 | 4 / 3 | 2 / 4 / 1 | begruenden 1, darstellung 1, einkleidung 1, fehler 1, mehrschritt 1, pruefung 1, umkehr 1 | ohne 5, fehler_detektiv 1, zwei_wege 1 |
| `gleichungen.bruch` | `scheinloesung` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | begruenden 1, darstellung 3, fehler 1, transfer 1, umkehr 1 | ohne 5, fehler_detektiv 1, umkehren 1 |
| `gleichungen.bruch` | `verhaeltnis` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | darstellung 1, fehler 1, mehrschritt 1, transfer 2, umkehr 2 | ohne 3, bruecke 1, fehler_detektiv 1, umkehren 1, zwei_wege 1 |
| `terme.potenzgesetze` | `negativer_exponent` | 1 | 3 | 3 | 4 / 3 | 4 / 2 / 1 | begruenden 1, darstellung 2, parameter 1, transfer 1, umkehr 2 | ohne 6, bruecke 1 |
| `terme.potenzgesetze` | `fehler_finden` | 1 | 3 | 3 | 4 / 3 | 1 / 4 / 2 | begruenden 1, darstellung 1, fehler 2, mehrschritt 1, umkehr 2 | ohne 3, fehler_detektiv 3, zwei_wege 1 |
| `zahlen.potenzen_zehner` | `gross_wissenschaftlich` | 1 | 3 | 3 | 4 / 3 | 3 / 3 / 1 | begruenden 1, darstellung 1, einkleidung 1, fehler 1, mehrschritt 1, transfer 1, umkehr 1 | ohne 4, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `zahlen.potenzen_zehner` | `negativer_exponent` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | darstellung 2, fehler 1, mehrschritt 1, transfer 2, umkehr 1 | ohne 4, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `zahlen.potenzen_zehner` | `vorsilben_klein` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | begruenden 1, darstellung 2, einkleidung 1, fehler 1, transfer 1, umkehr 1 | ohne 3, bruecke 2, fehler_detektiv 1, umkehren 1 |
| `zahlen.potenzen_zehner` | `vergleichen_pruefen` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | begruenden 1, darstellung 2, fehler 1, mehrschritt 1, pruefung 1, umkehr 1 | ohne 6, fehler_detektiv 1 |
| `messen.flaechen_vielecke` | `dreieck` | 1 | 3 | 3 | 4 / 3 | 4 / 1 / 2 | darstellung 2, fehler 1, mehrschritt 1, transfer 2, umkehr 1 | ohne 3, bruecke 1, fehler_detektiv 1, umkehren 1, zwei_wege 1 |
| `messen.flaechen_vielecke` | `rueckwaerts` | 1 | 3 | 3 | 4 / 3 | 3 / 1 / 3 | begruenden 1, darstellung 2, fehler 1, rueckwaerts 1, umkehr 2 | ohne 4, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `messen.flaechen_vielecke` | `zusammengesetzt` | 1 | 3 | 3 | 4 / 3 | 3 / 1 / 3 | darstellung 2, fehler 1, mehrschritt 1, transfer 2, umkehr 1 | ohne 2, bruecke 2, fehler_detektiv 1, umkehren 1, zwei_wege 1 |
| `messen.flaechen_vielecke` | `verstehen` | 1 | 3 | 3 | 4 / 3 | 3 / 3 / 1 | begruenden 1, darstellung 3, fehler 1, rueckwaerts 1, umkehr 1 | ohne 4, bruecke 2, fehler_detektiv 1 |
| Summe | 17 Lernziele | 17 | 51 | 51 | 68 / 51 | 50 / 36 / 33 | | |

Typen insgesamt:

| Typ | Aufgaben | Anteil |
|---|---|---|
| darstellung | 30 | 25 % |
| umkehr | 24 | 20 % |
| transfer | 17 | 14 % |
| fehler | 17 | 14 % |
| begruenden | 12 | 10 % |
| mehrschritt | 8 | 7 % |
| einkleidung | 6 | 5 % |
| pruefung | 2 | 2 % |
| rueckwaerts | 2 | 2 % |
| parameter | 1 | 1 % |

Formen insgesamt:

| Form | Aufgaben | Anteil |
|---|---|---|
| (ohne Form) | 68 | 57 % |
| fehler_detektiv | 18 | 15 % |
| bruecke | 16 | 13 % |
| umkehren | 11 | 9 % |
| zwei_wege | 6 | 5 % |

## Kennungen

| Einheit | Kennungen | Aufgaben |
|---|---|---|
| `bruch.prozent` | VT1B-001 bis VT1B-021 | 21 |
| `gleichungen.bruch` | VT1B-022 bis VT1B-049 | 28 |
| `terme.potenzgesetze` | VT1B-050 bis VT1B-063 | 14 |
| `zahlen.potenzen_zehner` | VT1B-064 bis VT1B-091 | 28 |
| `messen.flaechen_vielecke` | VT1B-092 bis VT1B-119 | 28 |

Fehlbilder: 408 insgesamt; bei Zahl- und Lückenaufgaben trägt jedes Fehlbild eine ausführbare Rechnung (`rechnung`), bei Auswahl steht die falsche Möglichkeit mit der Beschreibung des Denkfehlers.

## Denkfiguren je Lernziel (von Hand gruppiert)

| Lernziel | verschiedene Denkfiguren | Nahe Paare (als eine Figur gezählt) |
|---|---|---|
| bruch.prozent / prozentwert | 6 | Steuer mit Faktor und Bruch↔Prozent |
| bruch.prozent / grundwert | 6 | Grundwert direkt und Fehlbetrag |
| bruch.prozent / verstehen | 6 | Anzahl oder Anteil und zwei verschieden große Ganze |
| gleichungen.bruch / definitionsmenge | 5 | Text zur Gleichung (026, 028); Menge zuordnen und Nenner zerlegen (023, 025) |
| gleichungen.bruch / ueber_kreuz | 6 | Darstellung und Ausmultiplizier-Fehler |
| gleichungen.bruch / scheinloesung | 5 | Kandidaten gegen D und zwei Kandidaten (037, 042) |
| gleichungen.bruch / verhaeltnis | 6 | Unterschied als Teile und rückwärts aufteilen (045, 048) |
| terme.potenzgesetze / negativer_exponent | 6 | – |
| terme.potenzgesetze / fehler_finden | 6 | – |
| zahlen.potenzen_zehner / gross_wissenschaftlich | 6 | – |
| zahlen.potenzen_zehner / negativer_exponent | 6 | – |
| zahlen.potenzen_zehner / vorsilben_klein | 6 | – |
| zahlen.potenzen_zehner / vergleichen_pruefen | 6 | – |
| messen.flaechen_vielecke / dreieck | 6 | Höhe aus Koordinaten (092, 095) |
| messen.flaechen_vielecke / rueckwaerts | 6 | Parallelogramm→Rechteck und Trapez→Parallelogramm (101, 102) |
| messen.flaechen_vielecke / zusammengesetzt | 6 | Trapez über Diagonale und über Rechteck+Dreiecke (108, 109) |
| messen.flaechen_vielecke / verstehen | 6 | – |

Diese Zählung ist meine Handeinschätzung und nicht werkzeuggeprüft.

## Flächen: Formeln erklären statt lernen

Herleitungs-, Zerlegungs- oder Ergänzungsaufgaben je Lernziel: dreieck 3 (092, 093, 094), rueckwaerts 3 (101, 102, 105), zusammengesetzt 5 (106, 108, 109, 111, 112), verstehen 5 (113, 114, 115, 116, 118).

## Regeln dieser Runde (vom Bauskript geprüft)

- Antwortformen nur `zahl`, `luecken` (ganze Zahlen) und `auswahl` mit genau 4 Möglichkeiten und genau einer richtigen; Rundungsregel steht im Text, wo gerundet würde (hier wird nirgends gerundet).
- Fehler-Detektiv nur als Lücken („Fehler in Zeile □, richtig: □“, mindestens 3 Zeilen) oder Auswahl mit mindestens 4 Zeilen, deren Möglichkeiten nach Zeile geordnet sind und jeweils eine Begründung nennen.
- Position der richtigen Möglichkeit gleichmäßig auf die vier Plätze verteilt; die richtige Möglichkeit ist höchstens in 35 % der Fälle die längste und höchstens das 1,3-fache der durchschnittlichen Länge der falschen.
- Auswahl: alle vier Möglichkeiten mit oder alle ohne „denn/weil“, einheitliches Bindewort; Sammeloptionen („Beide“, „Keine“) und Absolutwörter zwischen richtig und falsch ausgeglichen.
- Tests nur als Zahl oder Lücken.
- Zahlen im Text eines Fehlbilds stammen aus der Aufgabe oder aus der Rechnung des Fehlbilds; Lösungen sind zweifach gerechnet; Dopplungsprüfung gegen `inhalte/themen`, `rollend-*` und andere `vtest-*`.
- Geometrie ohne Bild: Figuren sind vollständig durch Maße oder Koordinaten beschrieben (kein `grafik`-Feld).

## Offene Zweifel

- Lehrplanzuordnung: Die Lernbereiche stammen aus `inhalte/themenliste.json` (M6 1, M6 2, M6 3, M8 4). Ob negative Exponenten und wissenschaftliche Schreibweise im Gymnasium der Jahrgangsstufe 6 genau so im Lernbereich M6 1 stehen, ist am Repo nicht zu belegen und sollte geprüft werden.
- `regel` ist je Lernziel gesetzt (`regeln-zuordnung.md`); `fehlbild` und `regel_des_fehlbilds` sind leer, weil die Katalogzuordnung nicht sicher ist.
- Lehrplan, im Zweifel: negative Exponenten (Themenliste des Repos: M6 1, Vorprüfung fand im Repo Widersprüche, Klasse 8); Gleichungen mit Parameter (VT1B-024, 034, 043) gehören nach der Themenliste in M8 4; Prozentpunkte und Rabatt/Aufschlag liegen im `vorrat-folgerunde`, weil die Bestandsdatei sie als Klasse 7 führt.
- Doppelungsprüfung gegen den Bestand: werkzeuggestützt (Kern, mit und ohne Maskierung der Zahlen), je Lernziel mit Stichprobe von Hand; `bestandsvergleich.md` nennt die Grenzen.
- Die Aufgabenanzahl mit „Schema-nahem Rechnen“ (höchstens zwei je Lernziel) ist von Hand eingeschätzt.
- Mehrdeutigkeit: In den Koordinaten- und Maßaufgaben ist jede Seite und jeder Winkel ausdrücklich genannt; bei Aufgaben zu „Höhe liegt außen“ ist die Lage der Spitze im Text angegeben.
