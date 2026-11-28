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
| `gegenrechnung.py` | rechnet alle Lösungen und Fehlbilder aus den JSON-Dateien unabhängig nach, 38 Aufgaben zusätzlich ganz neu (Brute-Force, Gauß-Fläche, Zählen); Ende „0 Abweichungen“ |
| `sonderfaelle.md` | Kurzvermerk je Auswahl-Aufgabe |

## Zahlen

| Einheit | Lernziel | test | korrektur | sicherung | Stufe 2 / 3 | Antwortformen (Zahl / Auswahl / Lücken) | Typen | Formen |
|---|---|---|---|---|---|---|---|---|
| Einheit | Lernziel | test | korrektur | sicherung | Stufe 2 / 3 | Antwortformen (Zahl / Auswahl / Lücken) | Typen | Formen |
|---|---|---|---|---|---|---|---|---|
| `bruch.prozent` | `prozentwert` | 1 | 3 | 3 | 4 / 3 | 2 / 3 / 2 | darstellung 1, einkleidung 1, fehler 1, mehrschritt 1, transfer 2, umkehr 1 | ohne 4, bruecke 1, fehler_detektiv 1, zwei_wege 1 |
| `bruch.prozent` | `grundwert` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | begruenden 1, darstellung 2, fehler 1, transfer 1, umkehr 2 | ohne 6, fehler_detektiv 1 |
| `bruch.prozent` | `verstehen` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | begruenden 1, darstellung 1, einkleidung 1, fehler 1, transfer 1, umkehr 2 | ohne 4, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `gleichungen.bruch` | `definitionsmenge` | 1 | 2 | 2 | 3 / 2 | 2 / 1 / 2 | begruenden 1, einkleidung 1, fehler 1, umkehr 2 | ohne 2, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `gleichungen.bruch` | `ueber_kreuz` | 1 | 2 | 2 | 3 / 2 | 2 / 2 / 1 | darstellung 2, fehler 1, mehrschritt 1, parameter 1 | ohne 3, fehler_detektiv 1, zwei_wege 1 |
| `gleichungen.bruch` | `scheinloesung` | 1 | 2 | 2 | 3 / 2 | 2 / 1 / 2 | begruenden 1, darstellung 2, transfer 1, umkehr 1 | ohne 5 |
| `gleichungen.bruch` | `verhaeltnis` | 1 | 2 | 2 | 3 / 2 | 3 / 1 / 1 | darstellung 1, mehrschritt 1, transfer 2, umkehr 1 | ohne 2, bruecke 1, umkehren 1, zwei_wege 1 |
| `terme.potenzgesetze` | `negativer_exponent` | 1 | 3 | 3 | 4 / 3 | 3 / 2 / 2 | begruenden 1, darstellung 2, parameter 1, transfer 1, umkehr 2 | ohne 6, bruecke 1 |
| `terme.potenzgesetze` | `fehler_finden` | 1 | 3 | 3 | 4 / 3 | 1 / 4 / 2 | begruenden 1, darstellung 1, fehler 2, mehrschritt 1, umkehr 2 | ohne 3, fehler_detektiv 3, zwei_wege 1 |
| `zahlen.potenzen_zehner` | `gross_wissenschaftlich` | 1 | 3 | 3 | 4 / 3 | 2 / 3 / 2 | begruenden 1, darstellung 2, fehler 1, transfer 1, umkehr 2 | ohne 4, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `zahlen.potenzen_zehner` | `negativer_exponent` | 1 | 3 | 3 | 4 / 3 | 4 / 1 / 2 | darstellung 2, fehler 1, parameter 1, transfer 1, umkehr 2 | ohne 4, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `zahlen.potenzen_zehner` | `vorsilben_klein` | 1 | 3 | 3 | 4 / 3 | 1 / 4 / 2 | darstellung 2, fehler 1, rueckwaerts 1, transfer 1, umkehr 2 | ohne 4, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `zahlen.potenzen_zehner` | `vergleichen_pruefen` | 1 | 3 | 3 | 4 / 3 | 2 / 3 / 2 | begruenden 1, darstellung 1, fehler 1, transfer 1, umkehr 3 | ohne 4, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `messen.flaechen_vielecke` | `dreieck` | 1 | 3 | 3 | 4 / 3 | 4 / 1 / 2 | begruenden 1, darstellung 3, fehler 1, mehrschritt 1, transfer 1 | ohne 3, bruecke 2, fehler_detektiv 1, zwei_wege 1 |
| `messen.flaechen_vielecke` | `rueckwaerts` | 1 | 3 | 3 | 4 / 3 | 4 / 1 / 2 | begruenden 1, darstellung 2, fehler 1, mehrschritt 1, rueckwaerts 1, umkehr 1 | ohne 3, bruecke 2, fehler_detektiv 1, umkehren 1 |
| `messen.flaechen_vielecke` | `zusammengesetzt` | 1 | 3 | 3 | 4 / 3 | 2 / 2 / 3 | darstellung 3, fehler 1, rueckwaerts 1, transfer 1, umkehr 1 | ohne 4, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `messen.flaechen_vielecke` | `verstehen` | 1 | 3 | 3 | 4 / 3 | 4 / 1 / 2 | begruenden 1, darstellung 2, fehler 1, transfer 1, umkehr 2 | ohne 4, bruecke 1, fehler_detektiv 1, umkehren 1 |
| Summe | 17 Lernziele | 17 | 47 | 47 | 64 / 47 | 44 / 34 / 33 | | |

Typen insgesamt:

| Typ | Aufgaben | Anteil |
|---|---|---|
| darstellung | 29 | 26 % |
| umkehr | 26 | 23 % |
| transfer | 15 | 14 % |
| fehler | 15 | 14 % |
| begruenden | 11 | 10 % |
| mehrschritt | 6 | 5 % |
| einkleidung | 3 | 3 % |
| parameter | 3 | 3 % |
| rueckwaerts | 3 | 3 % |

Formen insgesamt:

| Form | Aufgaben | Anteil |
|---|---|---|
| (ohne Form) | 65 | 59 % |
| fehler_detektiv | 16 | 14 % |
| bruecke | 15 | 14 % |
| umkehren | 10 | 9 % |
| zwei_wege | 5 | 5 % |

## Kennungen

| Einheit | Kennungen | Aufgaben |
|---|---|---|
| `bruch.prozent` | VT1B-001 bis VT1B-021 | 21 |
| `gleichungen.bruch` | VT1B-022 bis VT1B-041 | 20 |
| `terme.potenzgesetze` | VT1B-042 bis VT1B-055 | 14 |
| `zahlen.potenzen_zehner` | VT1B-056 bis VT1B-083 | 28 |
| `messen.flaechen_vielecke` | VT1B-084 bis VT1B-111 | 28 |

Fehlbilder: 408 insgesamt; bei Zahl- und Lückenaufgaben trägt jedes Fehlbild eine ausführbare Rechnung (`rechnung`), bei Auswahl steht die falsche Möglichkeit mit der Beschreibung des Denkfehlers.

## Denkfiguren je Lernziel (von Hand gruppiert)

Gruppiert nach der Einsicht, nicht nach der `idee`-Beschriftung. „Schema-nah“ sind Aufgaben, die man mit dem Rezept der Übungen (einsetzen, umrechnen, Zähler und Nenner vertauschen) lösen kann; ein Fehler-Detektiv mit bloßem Verrechner zählt als Schema, nur ein echter Denkfehler zählt als Verstehen. In jedem Lernziel höchstens zwei Schema-nahe Aufgaben und keine Denkfigur öfter als zweimal.

| Lernziel | verschiedene Denkfiguren | Als eine Figur gezählt (je höchstens 2) | Schema-nah |
|---|---|---|---|
| bruch.prozent / prozentwert | 6 | Darstellungswechsel Winkel und Bruch (003, 007) | 004, 007 |
| bruch.prozent / grundwert | 6 | Grundwert direkt und 1 % (009, 014) | 010, 014 |
| bruch.prozent / verstehen | 6 | verschiedene Ganze (018, 020) | 016, 021 |
| gleichungen.bruch / definitionsmenge | 6 | Text zur Gleichung (026, 028) | 025, 026 |
| gleichungen.bruch / ueber_kreuz | 6 | Darstellung und Ausmultiplizieren (030, 033) | 030, 031 |
| gleichungen.bruch / scheinloesung | 6 | Kandidat gegen D (037, 038) | 038, 042 |
| gleichungen.bruch / verhaeltnis | 5 | Addieren oder Abziehen gegen Mal (045, 046); Teile (044, 048) | 044, 048 |
| terme.potenzgesetze / negativer_exponent | 5 | Vergleich mit Grenze (050, 053); Exponent aus Wert (051, 055) | 052, 055 |
| terme.potenzgesetze / fehler_finden | 6 | Rechenregeln auf Summen (057, 060) | 058 |
| zahlen.potenzen_zehner / gross_wissenschaftlich | 6 | Vorfaktor und Übertrag (066, 070) | 065, 070 |
| zahlen.potenzen_zehner / negativer_exponent | 6 | Stellen und Exponent (071, 076) | 076 |
| zahlen.potenzen_zehner / vorsilben_klein | 5 | Skalieren und vergrößern (078, 083); Maßzahl und Einheit (079, 084) | 080, 082 |
| zahlen.potenzen_zehner / vergleichen_pruefen | 6 | Exponenten angleichen (085, 089) | 086, 090 |
| messen.flaechen_vielecke / dreieck | 6 | Lage der Spitze egal (092, 096) | 093, 095 |
| messen.flaechen_vielecke / rueckwaerts | 6 | Fläche und Grundseite oder Höhe (099, 103); Herleitung (101, 102) | 099, 103 |
| messen.flaechen_vielecke / zusammengesetzt | 6 | Rückwärts aus der Fläche (106, 107) | 108, 111 |
| messen.flaechen_vielecke / verstehen | 5 | Strecken (113, 117); Zuwachs (116, 119) | 114, 119 |

Diese Zählung ist meine Handeinschätzung und nicht werkzeuggeprüft. Die Vorprüfung 2 hat die Zählung der ersten Fassung teilweise anders gruppiert (zum Beispiel „Kandidat gegen D“ viermal in scheinloesung); die neuen Aufgaben sind so gebaut, dass auch bei der strengeren Gruppierung höchstens zwei zusammenfallen.

## Flächen: Formeln erklären statt lernen

Herleitungs-, Zerlegungs- oder Ergänzungsaufgaben je Lernziel (Handzählung): dreieck 3 (093, 094, 097), rueckwaerts 2 (101, 102), zusammengesetzt 5 (106, 108, 110, 111, 112), verstehen 3 (114, 118, 119).

## Regeln dieser Runde (vom Bauskript geprüft)

- Antwortformen nur `zahl`, `luecken` (ganze Zahlen) und `auswahl` mit genau 4 Möglichkeiten und genau einer richtigen; Rundungsregel steht im Text, wo gerundet würde (hier wird nirgends gerundet).
- Fehler-Detektiv nur als Lücken („Fehler in Zeile □, richtig: □“, mindestens 3 Zeilen) oder Auswahl mit mindestens 4 Zeilen, deren Möglichkeiten nach Zeile geordnet sind und jeweils eine Begründung nennen.
- Position der richtigen Möglichkeit gleichmäßig auf die vier Plätze verteilt, in unregelmäßiger Folge ohne Periode (kein Zwölferzyklus mehr, `kern.py`), keine zwei gleichen Plätze hintereinander; die richtige Möglichkeit ist höchstens in 35 % der Fälle die längste und höchstens das 1,3-fache der durchschnittlichen Länge der falschen.
- Auswahl: alle vier Möglichkeiten mit oder alle ohne „denn/weil“, einheitliches Bindewort; Sammeloptionen („Beide“, „Keine“) und Absolutwörter zwischen richtig und falsch ausgeglichen.
- Tests nur als Zahl oder Lücken.
- Zahlen im Text eines Fehlbilds stammen aus der Aufgabe oder aus der Rechnung des Fehlbilds; Lösungen sind zweifach gerechnet; Dopplungsprüfung gegen `inhalte/themen`, `rollend-*` und andere `vtest-*`.
- Geometrie ohne Bild: Figuren sind vollständig durch Maße oder Koordinaten beschrieben (kein `grafik`-Feld).

## Offene Zweifel

- Lehrplanzuordnung: Die Lernbereiche stammen aus `inhalte/themenliste.json` (M6 1, M6 2, M6 3, M8 4). Ob negative Exponenten und wissenschaftliche Schreibweise im Gymnasium der Jahrgangsstufe 6 genau so im Lernbereich M6 1 stehen, ist am Repo nicht zu belegen und sollte geprüft werden.
- `regel` ist je Lernziel gesetzt (`regeln-zuordnung.md`); `fehlbild` und `regel_des_fehlbilds` sind leer, weil die Katalogzuordnung nicht sicher ist.
- Lehrplan, geklärt durch die Vorprüfung 2 (Quelle: LehrplanPLUS Gymnasium Jgst. 6 Mathematik, https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/6/mathematik): Prozentpunkte stehen in M6 3 (Klasse 6), nicht erst in Klasse 7; die Annahme „liegt im Vorrat, weil Klasse 7“ war falsch. Negative Exponenten in Jgst. 6 nur als Brüche mit Zähler 1 und als Zehnerpotenzen (M6 1.4); Trapez und Herleitung durch Zerlegen und Ergänzen stehen in M6 2.1. Folge in dieser Fassung: keine Bruchbasis und keine negative Basis bei negativen Exponenten mehr (053, 058, 059, 061 geändert).
- Lehrplan, weiter offen (nicht geraten): (1) wissenschaftliche Schreibweise und die Vorsilben nano und mikro (zahlen.potenzen_zehner) sind am Lehrplantext der Jgst. 6 nicht belegt; (2) Gleichungen mit Parameter (024, 029, 036, 039) und die Prozentrechnung in Flächenaufgaben (113, 114, 117) sind am Lehrplan nicht belegt; Parameterfragen („Für welche Zahl c …“) gibt es im Bestand (`gleichungen.potenz`, `gleichungen.reinquadratisch`, `rollend-7`), dort aber nicht in Jgst. 6. Bitte in der Gegenprüfung gegen den Lehrplantext der Etappe prüfen.
- Doppelungsprüfung gegen den Bestand: werkzeuggestützt (Kern, mit und ohne Maskierung der Zahlen), je Lernziel mit Stichprobe von Hand; `bestandsvergleich.md` nennt die Grenzen.
- Die Aufgabenanzahl mit „Schema-nahem Rechnen“ (höchstens zwei je Lernziel) ist von Hand eingeschätzt.
- Mehrdeutigkeit: In den Koordinaten- und Maßaufgaben ist jede Seite und jeder Winkel ausdrücklich genannt; bei Aufgaben zu „Höhe liegt außen“ ist die Lage der Spitze im Text angegeben.

## Hinweise für die Gegenprüfung: gleiche Einsicht wie im Bestand, aber andere Form oder Zahlen

Diese Aufgaben stehen nicht als Doppelung im Sinn „gleicher Kern und gleiche Frage und Zahlen“ (die ist ersetzt), tragen aber eine Einsicht, die auch im Bestand vorkommt. Wenn die Gegenprüfung strenger zählt, sind sie die ersten Kandidaten zum Austausch:

| Aufgabe | Einsicht | nächste Bestandsaufgabe | Unterschied |
|---|---|---|---|
| 002 | a % von b gleich b % von a | „30 % von 50 gegen 50 % von 30“ | Zwei Rechenwege mit Entscheidung, anderes Beispiel |
| 018 | Prozentsatz über 100 % | Wachstumsaufgaben in `bruch.prozent` | Rückwärts: Ausgangswert gesucht |
| 049 | gemeinsames Glied zweier Verhältnisse | „Bonbons 2 : 3 : 4“ (`groessen.verhaeltnisse`) | zwei Verhältnisse mit Mittelglied und Zusatzfrage |
| 054 | größere Hochzahl bei negativem Exponenten | „Ben sagt: 10⁻⁴ ist größer als 10⁻², weil 4 größer ist als 2“ | Basis 2, vier Begründungen, die Begründung ist gefragt |
| 062 | Hochzahl 0 | „10⁰ ist 0“ (Stimmt die Aussage) | Begründung über das Muster, Basis 5 |
| 077 | negativer Exponent macht nicht negativ | „10⁻⁵ ist eine negative Zahl“ | Fehler-Detektiv mit Folgerechnung |
| 085 | Zahlen in Potenzform ordnen | „Welche Zahl ist am kleinsten?“ (Vierer-Auswahl) | nicht normierte Vorfaktoren, Nummern statt Auswahl |
| 087 | Verhältnis zweier Zahlen in Potenzform | Virus 1 · 10⁻⁷ gegen Bakterium 2 · 10⁻⁶ | Alltagskontext Salz, Begründung gefragt |
| 089 | Exponenten angleichen | „8 · 10⁻⁵ größer als 2 · 10⁻⁴, weil 8 größer ist als 2“ | anderer Fehler (Richtung beim Angleichen) |
| 056 | Stücke passen | „Blatt 10⁻⁴ m, 1 cm“ | reine Zehnerpotenzen ohne Einheit |
| 092, 096 | Lage der Spitze spielt keine Rolle | „Spitze liegt irgendwo auf der Linie, egal wo“ | Koordinaten (092), Fehler-Detektiv (096) |
| 094 | zwei Dreiecke geben ein Parallelogramm | „Diagonale teilt ein Parallelogramm, ein Dreieck hat 24 cm²“ | Parallelogramm gegeben, Dreieck gesucht |
| 102 | Trapezformel aus zwei Trapezen | „Warum steht in der Trapezformel die Summe a + c?“ | Zahlenbeispiel mit Lücken |
| 105 | Fläche eines Parallelogramms höchstens a · b | „Parallelogramm 8 cm und 5 cm: wie groß höchstens?“ | Ja/Nein-Frage mit Begründung, andere Zahlen |
| 106 | Rechteck plus Dreieck | „Fünfeck aus Rechteck und Dreieck“ | rückwärts: Höhe des Dreiecks aus der Gesamtfläche |
| 109 | Umfang beim Zusammenlegen und Zerschneiden | „Zwei Quadrate aneinander: Umfang“ | Zerschneiden, Fläche und Umfang zugleich |
| 118 | Dreiecksflächen an gegenüberliegenden Seiten | „Punkt P auf der oberen Seite, Dreieck egal wo“ | Punkt im Innern, zwei Dreiecke zusammen |
| 100 | Grundseite aus Fläche und Seitenverhältnis | `gleichungen.reinquadratisch` (98 cm², doppelt so lang wie breit) | Parallelogramm mit halber Höhe |
