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
- Meldungen (iv): R5-V030, R5-V064, R5-V148, R5-V154. Die Fehlerzeile enthält nur richtige Rechnungen, der Fehler ist eine falsche Behauptung (Denkfehler); von Hand geprüft.
- Auswahlaufgaben (Wähle) haben eine gerechnete Probe; ein reines `lambda: True` gibt es nicht mehr.
- Zeichnungen nur als Tabelle oder Säulen (20 Aufgaben).
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
