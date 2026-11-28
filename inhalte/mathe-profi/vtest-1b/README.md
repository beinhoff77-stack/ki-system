# vtest-1b – Verstehens-Aufgaben für die Tests (Runde 1b)

Kennungen `VT1B-001` bis `VT1B-085`. Auftrag: `auftrag.md` (Kopie des Auftrags), Auswahl und Begründung: `auswahl.md`. Alles in diesem Ordner ist neu; nichts ist eingespielt, kein App-Code, keine Migration, nichts unter `tools/` geändert.
Je gewähltem Lernziel 5 Aufgaben: 1 **test** (`ersetzt_test: true`, die anspruchsvollste des Lernziels), 2 **korrektur** (Stufe 2) und 2 **sicherung** (Stufe 2 und 3). Die jeweils schwächste Korrektur- und Sicherungs-Aufgabe liegt in `vorrat-folgerunde/` (Kennungen `VT1B-VRnn`). `tools/vtest_pruefen.py` erwartet noch 1/3/3 und meldet darum je Lernziel Fehler zur Aufgabenzahl; das sind die einzigen Meldungen. Je Lernziel sind die 5 Aufgaben mit 5 verschiedenen `idee`-Einträgen beschriftet; **die Beschriftung ist nicht die Denkfigur.** Von Hand nach Denkfiguren gruppiert (Tabelle unten) kommen je Lernziel 5 verschiedene Denkfiguren vor (mindestens 4 verlangt) und höchstens eine Schema-nahe Aufgabe. 5 verschiedene Bauarten (Typ, Form, Antwortform) je Lernziel.

## Dateien

| Datei | Inhalt |
|---|---|
| `<einheit>.json` | die Aufgaben der Einheit (Format wie `inhalte/mathe-profi/vtest-1/auftrag.md` Abschnitt 9) |
| `th_<einheit>.py` | Quelltext der Aufgaben (Texte, Lösungen, Fehlbilder mit Rechnung, Ideen) |
| `kern.py`, `pruefhilfen.py` | Hilfen für den Bau (Aufgabenformen, Prüfungen, Dopplungsvergleich mit dem Bestand) |
| `bauen.py` | prüft alle Regeln und schreibt die JSON-Dateien, `README.md` und `sonderfaelle.md`; Aufruf `python3 -I inhalte/mathe-profi/vtest-1b/bauen.py`, Ende „OK“ |
| `gegenrechnung.py` | rechnet alle Lösungen und Fehlbilder aus den JSON-Dateien unabhängig nach, 60 Aufgaben zusätzlich ganz neu (Brute-Force, Gauß-Fläche, Zählen); Ende „0 Abweichungen“ |
| `sonderfaelle.md` | Kurzvermerk je Auswahl-Aufgabe |

## Zahlen

| Einheit | Lernziel | test | korrektur | sicherung | Stufe 2 / 3 | Antwortformen (Zahl / Auswahl / Lücken) | Typen | Formen |
|---|---|---|---|---|---|---|---|---|
| Einheit | Lernziel | test | korrektur | sicherung | Stufe 2 / 3 | Antwortformen (Zahl / Auswahl / Lücken) | Typen | Formen |
|---|---|---|---|---|---|---|---|---|
| `bruch.prozent` | `prozentwert` | 1 | 2 | 2 | 3 / 2 | 3 / 1 / 1 | begruenden 1, einkleidung 2, transfer 1, umkehr 1 | ohne 2, bruecke 2, umkehren 1 |
| `bruch.prozent` | `grundwert` | 1 | 2 | 2 | 3 / 2 | 4 / 1 / 0 | begruenden 1, darstellung 1, einkleidung 1, transfer 1, umkehr 1 | ohne 4, bruecke 1 |
| `bruch.prozent` | `verstehen` | 1 | 2 | 2 | 3 / 2 | 4 / 1 / 0 | begruenden 1, darstellung 1, einkleidung 1, parameter 1, umkehr 1 | ohne 3, bruecke 2 |
| `gleichungen.bruch` | `definitionsmenge` | 1 | 2 | 2 | 3 / 2 | 2 / 1 / 2 | begruenden 1, einkleidung 1, fehler 1, umkehr 2 | ohne 2, bruecke 1, fehler_detektiv 1, umkehren 1 |
| `gleichungen.bruch` | `ueber_kreuz` | 1 | 2 | 2 | 3 / 2 | 2 / 2 / 1 | darstellung 2, fehler 1, mehrschritt 1, parameter 1 | ohne 3, fehler_detektiv 1, zwei_wege 1 |
| `gleichungen.bruch` | `scheinloesung` | 1 | 2 | 2 | 3 / 2 | 2 / 1 / 2 | begruenden 1, darstellung 2, transfer 1, umkehr 1 | ohne 5 |
| `gleichungen.bruch` | `verhaeltnis` | 1 | 2 | 2 | 3 / 2 | 3 / 1 / 1 | darstellung 1, mehrschritt 1, transfer 2, umkehr 1 | ohne 2, bruecke 1, umkehren 1, zwei_wege 1 |
| `terme.potenzgesetze` | `negativer_exponent` | 1 | 2 | 2 | 3 / 2 | 2 / 1 / 2 | begruenden 1, darstellung 1, einkleidung 1, parameter 1, umkehr 1 | ohne 2, bruecke 2, umkehren 1 |
| `terme.potenzgesetze` | `fehler_finden` | 1 | 2 | 2 | 3 / 2 | 3 / 1 / 1 | begruenden 1, darstellung 1, einkleidung 1, fehler 1, umkehr 1 | ohne 3, bruecke 1, fehler_detektiv 1 |
| `zahlen.potenzen_zehner` | `gross_wissenschaftlich` | 1 | 2 | 2 | 3 / 2 | 4 / 0 / 1 | einkleidung 1, parameter 1, transfer 1, umkehr 2 | ohne 2, bruecke 2, umkehren 1 |
| `zahlen.potenzen_zehner` | `negativer_exponent` | 1 | 2 | 2 | 3 / 2 | 5 / 0 / 0 | darstellung 2, parameter 1, transfer 1, umkehr 1 | ohne 3, bruecke 1, umkehren 1 |
| `zahlen.potenzen_zehner` | `vorsilben_klein` | 1 | 2 | 2 | 3 / 2 | 3 / 1 / 1 | darstellung 1, einkleidung 1, mehrschritt 1, rueckwaerts 1, transfer 1 | ohne 2, bruecke 3 |
| `zahlen.potenzen_zehner` | `vergleichen_pruefen` | 1 | 2 | 2 | 3 / 2 | 4 / 1 / 0 | einkleidung 1, parameter 1, transfer 1, umkehr 2 | ohne 4, bruecke 1 |
| `messen.flaechen_vielecke` | `dreieck` | 1 | 2 | 2 | 3 / 2 | 4 / 0 / 1 | darstellung 2, fehler 1, mehrschritt 1, transfer 1 | ohne 2, bruecke 2, fehler_detektiv 1 |
| `messen.flaechen_vielecke` | `rueckwaerts` | 1 | 2 | 2 | 3 / 2 | 5 / 0 / 0 | einkleidung 1, parameter 1, rueckwaerts 1, umkehr 2 | ohne 3, bruecke 1, umkehren 1 |
| `messen.flaechen_vielecke` | `zusammengesetzt` | 1 | 2 | 2 | 3 / 2 | 4 / 1 / 0 | darstellung 1, mehrschritt 1, rueckwaerts 1, transfer 1, umkehr 1 | ohne 2, bruecke 2, umkehren 1 |
| `messen.flaechen_vielecke` | `verstehen` | 1 | 2 | 2 | 3 / 2 | 3 / 1 / 1 | begruenden 1, darstellung 1, fehler 1, umkehr 2 | ohne 2, bruecke 1, fehler_detektiv 1, umkehren 1 |
| Summe | 17 Lernziele | 17 | 34 | 34 | 51 / 34 | 57 / 14 / 14 | | |

Typen insgesamt:

| Typ | Aufgaben | Anteil |
|---|---|---|
| umkehr | 19 | 22 % |
| darstellung | 16 | 19 % |
| transfer | 11 | 13 % |
| einkleidung | 11 | 13 % |
| begruenden | 8 | 9 % |
| parameter | 7 | 8 % |
| fehler | 5 | 6 % |
| mehrschritt | 5 | 6 % |
| rueckwaerts | 3 | 4 % |

Formen insgesamt:

| Form | Aufgaben | Anteil |
|---|---|---|
| (ohne Form) | 46 | 54 % |
| bruecke | 23 | 27 % |
| umkehren | 9 | 11 % |
| fehler_detektiv | 5 | 6 % |
| zwei_wege | 2 | 2 % |

## Kennungen

| Einheit | Kennungen | Aufgaben |
|---|---|---|
| `bruch.prozent` | VT1B-001 bis VT1B-015 | 15 |
| `gleichungen.bruch` | VT1B-016 bis VT1B-035 | 20 |
| `terme.potenzgesetze` | VT1B-036 bis VT1B-045 | 10 |
| `zahlen.potenzen_zehner` | VT1B-046 bis VT1B-065 | 20 |
| `messen.flaechen_vielecke` | VT1B-066 bis VT1B-085 | 20 |

Fehlbilder: 377 insgesamt; bei Zahl- und Lückenaufgaben trägt jedes Fehlbild eine ausführbare Rechnung (`rechnung`), bei Auswahl steht die falsche Möglichkeit mit der Beschreibung des Denkfehlers.

## Denkfiguren je Lernziel (von Hand gruppiert)

Gruppiert nach der Einsicht, nicht nach der `idee`-Beschriftung. „Schema“ (streng) ist, was sich mit einem bekannten Verfahren, einer bekannten Regel oder bloßem Rechnen lösen lässt, auch ein Fehler-Detektiv mit bloßem Verrechner und eine Auswahl, die man durch Ausrechnen der Möglichkeiten löst. In jedem Lernziel höchstens eine Schema-Aufgabe und keine Denkfigur doppelt. Die Zeilen zu `gleichungen.bruch` gehören einem anderen Schreiber (Zweig `schreiber-w1-e20`); die Kennungen stehen hier in der Zählung dieses Zweigs (016 bis 035) und können sich beim Zusammenführen verschieben.

| Lernziel | verschiedene Denkfiguren | Schema (streng) |
|---|---|---|
| bruch.prozent / prozentwert | 5: Ganzes wächst (001), Ganzzahligkeit über den gekürzten Bruch (002), gleichbleibender Anteil am Anfangswert (003), Verteilungsgesetz begründen (004), Komma bei Bruchteilen von Prozent (005) | 005 |
| bruch.prozent / grundwert | 5: gleichbleibender Teil bei wechselndem Ganzen (006), Unterschied zweier Anteile (007), Winkel zurück zum Ganzen (008), gleicher Betrag bei doppeltem Prozentsatz (009), Anteil nach Zugabe, Rest bleibt gleich (010) | keine (008 grenzwertig) |
| bruch.prozent / verstehen | 5: verschiedene Ganze (011), Anteil steigt beim kleiner werdenden Ganzen (012), Ganzes wechselt in der Frage (013), Parameter mit zwei Bedingungen (014), „um“ gegen „auf“ (015) | 015 (013 grenzwertig) |
| gleichungen.bruch / definitionsmenge | 5: Identität und D (016), nie null (017), Umkehr D (018), Lösung und Verbot verwechselt (019), Modell aufstellen (020) | 017 |
| gleichungen.bruch / ueber_kreuz | 5: Parameter (021), Umformen (022), zwei Wege (023), Fehler in der Summe (024), Zahl zu Zähler und Nenner (025) | 022 |
| gleichungen.bruch / scheinloesung | 5: Parameter mit Identität (026), Gleichungen vergleichen (027), Scheinlösung durch Kürzen (028), Probe mit Nenner null (029), Bruch gleich null (030) | 027 |
| gleichungen.bruch / verhaeltnis | 5: x in beiden Verhältnissen (031), Abziehen gleich (032), additiv oder multiplikativ (033), Mittelwert und Summe (034), Fläche aus Seitenverhältnis (035) | 032 |
| terme.potenzgesetze / negativer_exponent | 5: Zählen im Bereich (036), Stufen einer Verkleinerung (037), Basis gesucht (038), Längen vergleichen mit Begründung (039), Lage zwischen Zehnerpotenzen (040) | 039 |
| terme.potenzgesetze / fehler_finden | 5: Potenzturm gegen Produkt (041), Potenz im Volumen (042), Vertauschen von Basis und Hochzahl (043), Rechenregel auf Summen (044), Binom mit Begründung (045) | 043 |
| zahlen.potenzen_zehner / gross_wissenschaftlich | 5: Bereich des Exponenten (046), Produkt normieren (047), Ganzzahligkeit von n (048), Rückwärts vom Doppelten (049), Übertrag beim Vervierfachen (050) | 050 |
| zahlen.potenzen_zehner / negativer_exponent | 5: Zehnerpotenzen verketten (051), Teilungen zählen (052), Skalierung rückwärts (053), Mitte der Potenzen (054), Kehrwert und Filter (055) | keine |
| zahlen.potenzen_zehner / vorsilben_klein | 5: Filter entscheiden (056), Fläche und Exponent (057), Licht in Nanosekunden (058), Vorsilbe gesucht (059), Verhältnis (060) | 059 |
| zahlen.potenzen_zehner / vergleichen_pruefen | 5: Raster und Grenzen (061), Faktor rückwärts (062), Größenordnung des Quotienten (063), Parameter k (064), Skalenfaktor (065) | 063 |
| messen.flaechen_vielecke / dreieck | 5: Mittendreieck (066), Teilverhältnis der Grundseite (067), plus und minus mit Ausgleich (068), Höhe teilt nicht gleich (069), zwei Dreiecke zum Parallelogramm (070) | 070 |
| messen.flaechen_vielecke / rueckwaerts | 5: Trapez und Verhältnis (071), Einheit beim Segel (072), Flächenunterschied und Grundseite (073), Gleichung g mal g (074), ganzzahlige Höhe (075) | 073 |
| messen.flaechen_vielecke / zusammengesetzt | 5: Überlappung (076), Rahmenbreite (077), Eck-Dreieck (078), Schnitt und Umfang (079), Viereck über Koordinaten (080) | 079 |
| messen.flaechen_vielecke / verstehen | 5: Höhen ergänzen (081), Differenzpaar (082), Zuwachs beim Quadrat (083), Strecke halbiert nicht (084), Zuwachs beim Dreieck (085) | 085 |

Diese Zählung ist meine Handeinschätzung und nicht werkzeuggeprüft. Beim `messen`-Lernziel dreieck hängt 070 und bei `rueckwaerts` 073 am Standardansatz (Fläche gleich Formel); der Rest ist als Verstehen gebaut.

## Flächen: Formeln erklären statt lernen

Herleitungs-, Zerlegungs- oder Ergänzungsaufgaben je Lernziel (Handzählung): dreieck 3 (066, 069, 070), rueckwaerts 1 (071), zusammengesetzt 3 (076, 078, 079), verstehen 3 (081, 083, 084).

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
- Lehrplan, weiter offen (nicht geraten): (1) wissenschaftliche Schreibweise und die Vorsilben nano und mikro (zahlen.potenzen_zehner) sind am Lehrplantext der Jgst. 6 nicht belegt; (2) Gleichungen mit Parameter (021, 026, 064) und die Prozentrechnung in Flächenaufgaben (068, 073, 081) sind am Lehrplan nicht belegt; Parameterfragen („Für welche Zahl c …“) gibt es im Bestand (`gleichungen.potenz`, `gleichungen.reinquadratisch`, `rollend-7`), dort aber nicht in Jgst. 6. Bitte in der Gegenprüfung gegen den Lehrplantext der Etappe prüfen.
- Doppelungsprüfung gegen den Bestand: werkzeuggestützt (Kern, mit und ohne Maskierung der Zahlen), je Lernziel mit Stichprobe von Hand; `bestandsvergleich.md` nennt die Grenzen.
- Die Aufgabenanzahl mit Schema (höchstens eine je Lernziel) ist von Hand eingeschätzt.
- Mehrdeutigkeit: In den Koordinaten- und Maßaufgaben ist jede Seite und jeder Winkel ausdrücklich genannt; bei Aufgaben zu „Höhe liegt außen“ ist die Lage der Spitze im Text angegeben.

## Hinweise für die Gegenprüfung: gleiche Einsicht wie im Bestand, aber andere Form oder Zahlen

Diese Aufgaben stehen nicht als Doppelung im Sinn „gleicher Kern und gleiche Frage und Zahlen“ (die ist ersetzt), liegen aber nahe an einer Bestandseinsicht. Wenn die Gegenprüfung strenger zählt, sind sie die ersten Kandidaten zum Austausch:

| Aufgabe | Einsicht | nächste Bestandsaufgabe | Unterschied |
|---|---|---|---|
| 008 | Winkel im Kreisdiagramm zurück zum Ganzen | `rollend-6` Nr. 16 | Rückfrage nach dem Ganzen, andere Zahlen |
| 013 | Bezugswechsel beim Prozentsatz | Wachstumsaufgaben in `bruch.prozent` | Ganzes wechselt, Lücken |
| 036 | Zählen im Bereich | „erste Potenz unter 0,01“ | Bereich mit zwei Grenzen, Lücken |
| 041 | Potenzturm | Fehler bei Potenzen von Potenzen | Fehler-Detektiv mit zwei Produkten; ob der Potenzturm in Jgst. 6 steht, ist offen |
| 068 | Plus und minus mit Ausgleich | „Seite verdoppeln“ (Fläche) | zwei gegenläufige Änderungen, Dreieck |
| 082 | Differenzpaar | „a ist 3 cm länger“ | zwei Zahlen aus Summe und Differenz der Flächen |
| 046 bis 065 | Zehnerpotenzen und Umrechnen | viele Umrechnungsaufgaben in `zahlen.potenzen_zehner` | andere Fragerichtung (rückwärts, Zählen, Parameter) |

