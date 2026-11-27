# Runde 12 (R5): Reserve Klasse 5

Zwei zählende Aufgaben je Lernkarte (eine auf Stufe 2, eine auf Stufe 3) in Formen, die in den bisherigen Runden fehlen oder selten sind.
Kürzel R5, Kennungen R5-V001 bis R5-V210. Aufgaben stehen in `<thema>.json`, erzeugt aus `th_<thema>.py` durch `bauen.py`.

| Thema | Lernkarten | Aufgaben | Formen zw/um/br/an/fd | zaehlt |
|---|---|---|---|---|
| zahlen.natuerlich | 13 | 26 | 7/5/4/4/6 | ja 26 |
| zahlen.rechengesetze | 14 | 28 | 9/6/2/5/6 | ja 28 |
| zahlen.ganz | 11 | 22 | 5/4/4/3/6 | ja 22 |
| zahlen.potenzen_basis | 7 | 14 | 4/3/2/2/3 | ja 14 |
| zahlen.teilbarkeit | 7 | 14 | 5/2/2/5/0 | ja 14 |
| geometrie.grundbegriffe | 7 | 14 | 2/3/4/5/0 | ja 14 |
| geometrie.winkel | 7 | 14 | 6/2/2/4/0 | ja 14 |
| messen.flaechen | 7 | 14 | 4/3/2/4/1 | ja 14 |
| messen.koerper_darstellung | 6 | 12 | 2/2/3/2/3 | ja 12 |
| daten.darstellen | 6 | 12 | 2/4/2/4/0 | ja 12 |
| stochastik.kombinatorik | 7 | 14 | 5/3/2/4/0 | ja 14 |
| groessen.einheiten | 8 | 16 | 5/4/3/4/0 | ja 16 |
| groessen.proportional | 5 | 10 | 2/2/3/3/0 | ja 10 |
| Summe | 105 | 210 | 58/43/35/49/25 | ja 210 |

Genaue Formverteilung je Thema: `python3 -I inhalte/mathe-profi/rollend-12/bauen.py` (Tabelle am Ende der Ausgabe).
Stufen: 105 Aufgaben auf Stufe 2, 105 auf Stufe 3.

## Wie geprüft
- `bauen.py`: je Lernkarte genau 2 Aufgaben, Stufen 2 und 3, zwei verschiedene Formen, kein Lückenweg, höchstens ein Fehler-Detektiv, je Thema jede der Formen Umkehren, Zwei Wege, Brücke, Anwenden mindestens zweimal.
- Alle Lösungen zweifach nachgerechnet, 576 Fehlbilder (469 mit nachgerechneter Rechnung), Dopplungen gegen den Bestand und andere Runden geprüft.
- `tools/inhalt_pruefen.py` (Code 0) und `tools/vorrat_pruefen.py` ohne Meldungen (i) bis (iii).
- `python3 -I tools/rollend_sql.py --runden 12` läuft ohne Fehler (210 Aufgaben, 13 Einheiten).
- Zum Schluss streng durchgesehen (Checkliste B).

## Offen und Annahmen (nicht abgesichert)
- Meldungen (iv): R5-V030, R5-V064, R5-V148, R5-V154. Die Fehlerzeile enthält nur richtige Rechnungen, der Fehler ist eine falsche Behauptung (Denkfehler); in der Zweitprüfung von Hand gelesen: jede dieser Zeilen spricht die falsche Behauptung selbst aus (V064 jetzt ausdrücklich).
- Auswahlaufgaben (Wähle) haben eine gerechnete Probe; ein reines `lambda: True` gibt es nicht mehr.
- Zeichnungen: Tabelle, Säulen und eine Figur (R5-V129), zusammen 24 Aufgaben. Dafür lässt `bauen.py` jetzt den Typ `figur` zu (Punkte, Linien, Winkel müssen zueinander passen).
- Keine Lernkarte zurückgestellt, bei jeder passte mindestens eine der gesuchten Formen.

## Vorprüfung
Alle 210 Aufgaben einzeln durchgesehen (Lösung neu gerechnet, Annahmen, Fehlbilder, Kennungen, Lernkarte, Stufe, Fehler-Detektiv-Zeilen). Danach in den `th_*.py` berichtigt und neu gebaut; es bleiben 210 Aufgaben, Kennungen R5-V001 bis R5-V210 unverändert.

Gefunden und geändert (Zahl der Aufgaben, einige Aufgaben fallen unter mehrere Arten):
- Aufgabentext oder Aufgabenidee ersetzt, 37 Aufgaben. Gründe: Aufgabe passte nicht zur Lernkarte (zum Beispiel „Stimmt das? Mit Gegenbeispiel prüfen“, „Winkelaussagen prüfen“, „Fläche und Umfang verstehen“, „Aussagen über Körper prüfen“, „Zählaussagen prüfen“, „Warum sind römische Zahlen anders?“, „Große Zahlen schreiben“; die Karte „Teilbar durch 3“ rechnete mit 9), Umkehr-Aufgabe war keine Umkehr, schwacher Zweiter Weg, Bruchrechnung über dem Niveau, Aufgabe doppelte eine Bestandsaufgabe (Teiler, Zahlengerade-Mitte, Punkt rückwärts verschieben, Busfahrplan mit denselben Zahlen), Oberfläche und Volumen eines Würfels mit 6 cm sind beide 216, Fehlerzeile des Fehler-Detektivs war doppelt falsch oder nicht eindeutig (römisch 49, Pizza).
- Fehler-Detektiv, alle 25: Rückmeldung je Zeile jetzt eigens geschrieben (`kern.FD`, 4. Eintrag je Zeile). Zeilen, die für sich richtig gerechnet sind und nur den falschen Wert benutzen, werden so benannt statt pauschal als „Folge“ erklärt. Tipps verraten die Fehlerzeile nicht mehr.
- Regel-Kennung gegen `kennungen.json` geprüft: von 210 behielten 106 eine Kennung, 104 sind jetzt leer, weil keine Idee genau passt (zum Beispiel „Schreibweisen“ bei römischen Zahlen, „Stufen“ bei Teilerzählen, „Gegenrechnung“ ohne Gleichung). Ausnahmen wegen des Textes, nicht der Themenliste, stehen in `bauen.py` (`REGEL_AUSNAHME`): Zählprinzip und Baumdiagramm, Zahlenstrahl, Gegenrechnung bei Umkehr-Aufgaben der Rechengesetze, Vorzeichen bei Potenzen mit negativer Basis. `bauen.py` lässt jetzt leere Kennungen zu und prüft die Themenliste.
- Fehlbild-Kennung: nur noch dort gesetzt, wo das Fehlbild genau dem Text der Kennung entspricht (Fehlbilder mit Kennung: 8 → 25; neu etwa Vorzeichen, Doppelminus, Umfang statt Fläche, nur drei Flächen, Neben- statt Scheitelwinkel, Endziffer statt Quersumme, nicht zu Ende zerlegt).
- Fehlbild-Erklärungen berichtigt oder neu gefasst (zum Beispiel 9 : 2 statt 9 : 20, 1 h = 100 min, Summe falsch herum), 69 Aufgaben betroffen; Tipps, die den Weg verrieten, verallgemeinert, 70 Aufgaben; Erklärungen angepasst, 30.
- Proben von Auswahlaufgaben, die nichts nachrechneten (`lambda: True` oder nur Ungleichungen), sind echte Rechnungen.

Kurz je Kennung der Regel, die geändert wurde: `id.zahlen.schreibweisen` (leer, Karten Zahlwort, römisch, dual), `id.zahlen.zahlengerade` (nur Zahlenstrahl ablesen/eintragen, sonst leer), `rr.stellenwert` (nur Zehner und Stellenwert, nicht Vergleichen), `rr.plusminus` (leer bei schriftlichem Rechnen ohne negative Zahlen), `id.zahlen.bausteine` (nur Primzahl und Primfaktoren), `id.geometrie.abstand` (nur Lage und Kreis), `id.geometrie.winkel` (nur Winkel ergänzen und Kreuzung), `id.flaeche_raum.*` (je Karte geprüft), `id.daten.teil_ganzes` und `id.daten.anteil` (leer, passen nicht zu Häufigkeiten), `id.daten.stufen` (nur Zählprinzip und Baumdiagramm), `id.verhaeltnisse.groesse` (nicht bei Zeitrechnung und Geld).

Nicht sicher zu beurteilen: ob die Fehler-Detektiv-Aufgaben mit einer Denkfehler-Zeile (R5-V030, R5-V064, R5-V148, R5-V154) für Kinder eindeutig genug sind, ob einzelne „Brücke“-Aufgaben ohne Zeichnung die Darstellung wirklich tragen (zum Beispiel R5-V113, R5-V129), ob R5-V109 und R5-V128 genug „Umkehren“ bzw. „zwei Wege“ sind, und die Stufe 3 bei R5-V130/R5-V176 (nur knapp schwerer als Stufe 2).

## Zweitprüfung (zweiter Helfer, der die Runde nicht geschrieben hat)
Geprüft wie neue Aufgaben (Lösung selbst gerechnet, Eindeutigkeit, Fehlbild gegen Fehlwert, Rückmeldung je Zeile, Lernkarte, Stufe, Tipp, Schreibweise, Eingabefrage, Niveau): die 48 Aufgaben, deren Text, Lösung, Form oder Lernkarte sich in der Vorprüfung geändert hat, dazu die 13 als unsicher gemeldeten (davon 3 schon in den 48, 4 sind Fehler-Detektive) und alle 25 Fehler-Detektive Zeile für Zeile. Zusammen 77 verschiedene Aufgaben einzeln gelesen; Kennungen unverändert, weiter 210 Aufgaben.
Geändert wurden 27 Aufgaben (Quellen `th_*.py`, neu gebaut):
- Doppelung mit dem Bestand, Zahlen und Einkleidung geändert: V125 (Minutenzeiger in 25 Minuten, jetzt 20), V126 (Uhrzeit-Winkel wie Bestand, jetzt 2:50 Uhr mit Winkel über 180°), V129 (Quadrat-Diagonale), V130 (Teil „doppelt so groß“), V134 und V144 (Fliesen-Boden, jetzt Terrasse mit Beet und Gartenweg).
- Form hielt nicht, was sie verspricht: V109 (Umkehren, jetzt echte Rückwärts-Verschiebung), V113 und V129 (Brücke ohne Darstellungswechsel: jetzt Drehung am Zifferblatt bzw. Zeichnung mit Winkeln), V199 (Brücke jetzt Tabelle), V103 (Faktorbaum nur im Text, jetzt Teilertabelle), V128 und V131 (zweiter Weg war dieselbe Rechnung: jetzt Windrose in 45°-Schritten bzw. Ergänzen zu 90°), V130 (zwei Wege jetzt Gleichung gegen Ausgleich).
- Lernkarte nicht genau getroffen oder über Niveau: V195 (Division durch Dezimalzahl, jetzt Seil mit m und cm), V199 und V200 (Karte „Größen prüfen“: Realitätscheck bzw. Angabe von Tim prüfen), V194 (Stufe 3 war leichter als Stufe 2: jetzt 3,08 kg).
- Eingabefrage stand nicht am Ende (Weg-B-Text zuletzt): V073, V098, V122, V125, V131, V146, V157, V184, V003 (V003: auch Weg B schärfer).
- Tipp verriet den Lösungsweg oder führte in die Irre (Stufe 3 nicht zur Routine machen): V084, V146, V156, V157, V158, V176.
- Fehlbild: V083 (9 als Hochzahl, Beschreibung stimmte nicht zur Rechnung), V146 (3 war kein plausibler Fehler), V103 (Fehlbild-Kennung „nicht zu Ende zerlegt“ entfällt mit dem neuen Text; Fehlbilder mit Kennung jetzt 24).
- Fehler-Detektiv: alle 25 in Ordnung (Fehlerzeile spricht die falsche Behauptung aus, Zeilen davor richtig, Folgezeilen folgen richtig, Rückmeldung je Zeile stimmt); nur V064 (Fehlerzeile jetzt mit ausdrücklicher Behauptung) und V084 (Tipp) geändert.
Entscheidung zu den Unsicheren: V030, V148, V154 bleiben (Fehlerzeile enthält die falsche Behauptung ausdrücklich: „von links nach rechts“, „doppelt so groß“, „verkürzt: 6 · 2“); V064 geschärft; V109, V113, V128, V129, V130, V134, V144, V126 umgebaut (siehe oben); V176 bleibt Stufe 3 (Paarbildung, schwerer als V175), nur Tipp neutral.
Prüfläufe: `bauen.py` OK, `tools/vorrat_pruefen.py` (i) bis (iii) ohne Meldung, (iv) nur die vier Denkfehler-Zeilen; `tools/rollend_sql.py --runden 12` ohne Fehler, 210 Aufgaben.
Offen: Bei den übrigen Zwei-Wege-Aufgaben (nicht in der Zweitprüfung gelesen) kann der Text noch mit Weg B enden statt mit der Frage; R5-V023 (römische Zahlen umkehren) trifft die Karte „Warum sind römische Zahlen anders?“ nur locker; R5-V008 ist als „Umkehren“ eher ein Rückschluss vom Pfeil auf den Abschnittswert; R5-V048 (Überschlag, Stufe 3) ist nur knapp schwerer als Stufe 2; R5-V093 (Vielfache von 7 zwischen 100 und 200) ähnelt einer Bestandsaufgabe (Vielfache von 6), nicht geändert. Die übrigen Aufgaben außerhalb der Fehler-Detektive wurden in der Zweitprüfung nicht gelesen.

## Nach Gegenprüfung (Werkstatt 1095)
Die Arbeitsliste der Gegenprüfung ist vollständig umgesetzt (Muss und Auflagen); Kennungen unverändert, weiter 210 Aufgaben.
- Neu gefasst und danach wie neue Aufgaben geprüft: V019, V020 (Nachfolger als Gegenstand), V145 (beide Umfänge bei gleicher Fläche), V158 (konkrete Behauptung zu prüfen), V093 (Grenzen mit Mit-/Ausschließen), V048 (Überschlag selbst wählen plus Endziffer), V186 (Schätzvergleich), V194 (falsche Umrechnung prüfen).
- Fehlbild-Beschreibungen berichtigt, wo sie nicht genau die Rechnung des Fehlwerts nannten (unter anderem V001, V013, V039, V053, V071, V078, V082, V085, V089, V103, V128, V165, V171); alle 472 Fehlbilder mit Rechnung noch einmal gegen ihre Beschreibung gelesen.
- Sach-, Text- und Lösungsweg-Korrekturen der Liste: V024, V060, V064, V086, V091, V105 bis V107, V115, V117, V122, V134, V137, V139, V140, V184, V185, V199, V205 sowie die Weg-A- und Weg-B-Ausführungen in V037, V049, V081, V106, V023, V012.
- Bei allen 58 Zwei-Wege-Aufgaben steht der Schlussauftrag hinter den beiden Wegen. `bauen.py` prüft das jetzt: der letzte Satz darf nicht mit „Weg“ beginnen und muss eine Frage oder ein Auftrag (Gib, Berechne, Bestimme, Nenne, Löse, Runde) sein.
- Prüfläufe: `bauen.py` OK, `tools/vorrat_pruefen.py` (i) bis (iii) ohne Meldung, (iv) nur die vier bestätigten Denkfehler-Zeilen; `tools/rollend_sql.py --runden 12` ohne Fehler, 210 Aufgaben.

## Nach Gegenprüfung (Werkstatt 1105)
Zweite Gegenprüfung umgesetzt; Kennungen unverändert, weiter 210 Aufgaben. Geänderte Aufgaben wurden wie neue geprüft, im erzeugten JSON ist in allen Feldern kein alter Text mehr zu finden.
- V019: Weg B zählt von 999 997 drei Schritte weiter. V020 ist jetzt eine Auswahl mit Begründung (allgemeine Begründung gegen Einzelfälle) und prüft damit etwas anderes als V019.
- V139 und V140: Probe und Rückmeldung begründen die Umrechnung mit 100 dm² = 1 m² statt mit einer Division durch 100.
- V023: Auswahl fragt nach dem Grund für CM (kleineres Zeichen vor größerem folgenden Zeichen wird abgezogen). V049, V052, V098: schriftliche Division in Weg A in Teilschritten. V081: zweiter Weg 15 · (20 − 5) = 300 − 75.
- V093, V107, V128, V184: Eingabefrage nur noch am Ende, vor Weg A stehen nur die Bedingungen. V186: „im Durchschnitt“ und ein Überschlag mit Begründung aus den Schrittzahlen. V199: durchgehend „Beispiel“.
- Systematische Suchen: Einheit-durch-100-Umrechnungen in allen Texten, Hinweisen, Lösungen, Proben und Rückmeldungen ohne weiteren Treffer. Doppelte Fragen bei Zwei-Wege-Aufgaben: zusätzlich in V125, V130, V131, V157, V138 und V144 die erste Frage zur Bedingung umgestellt; V146 bleibt (zwei Teilgrößen, Schlussauftrag nennt die Summe).
- Prüfläufe: `bauen.py` OK, `tools/vorrat_pruefen.py` (i) bis (iii) ohne Meldung, (iv) nur die vier bestätigten Denkfehler-Zeilen; `tools/rollend_sql.py --runden 12` ohne Fehler, 210 Aufgaben.

## Nach Gegenprüfung (Werkstatt 1115)
Vier Restauflagen umgesetzt, sonst nichts geändert; der JSON-Vergleich gegen den Stand vor der Änderung und gegen origin/lernen-app zeigt genau vier geänderte Aufgaben (V020, V138, V156, V186), Reihenfolgen anderer Auswahlaufgaben unverändert. Weiter 210 Aufgaben.
- V020: Form von „umkehren“ auf „anwenden“ (die Karte „unendlich“ hat damit zwei_wege und anwenden; Verteilung erfüllt).
- V138: Weg B nennt nur den Zwischenschritt (Fläche eines Quadrats mit 100 m Seitenlänge), Schlussauftrag bleibt.
- V156: Rückmeldung zum liegenden Dreiecksprisma neu gefasst (Ansicht quer zur Längsrichtung).
- V186: Auswahl der Größenordnung (2 cm, 20 cm, 2 m) ist die gewertete Antwort mit grober Begründung über das Viertel mehr Schritte; die exakte Rechnung (15 cm) steht erst im Lösungsweg.
- Prüfläufe: `bauen.py` OK, (i) bis (iii) leer, (iv) nur die vier bestätigten Zeilen; `tools/rollend_sql.py --runden 12` ohne Fehler, 210 Aufgaben.
