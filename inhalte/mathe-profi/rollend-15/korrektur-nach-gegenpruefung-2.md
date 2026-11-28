# Korrektur nach der zweiten Gegenprüfung (Werkstatt 1207)

Stand: Runde 15 (R15-V001 … V207, 207 Aufgaben, 14 Einheiten), Ausgangsstand 519f8ddc, `origin/lernen-app` eingemischt.
Die Kennungen unten sind die **neuen**; wo sich etwas verschoben hat, steht „alt → neu“.

## Zählbasis für „geändert“

Verglichen wird jeder Datensatz der 14 Einheiten-Dateien (Kennung, `aufgabe`, `fehlbilder`) mit dem Stand 519f8ddc.

| Zählung | Anzahl | Aufgaben |
|---|---|---|
| `aufgabe`-Objekt verändert (Text, Optionen, Tipp, Erklärung oder Etappe; V196, V199, V201 wegen neuer Etappe) | 11 | V014, V053, V054, V083, V126, V188, V196, V199, V201, V202, V206 |
| nur Fehlbilder verändert | 5 | V064, V065, V132, V150, V191 |
| nur Kennung neu vergeben (Folge des Umhängens, Inhalt gleich) | 6 | V197, V198, V200, V203, V204, V205 |
| Datensätze insgesamt verändert | 22 | |

Die frühere Angabe „57 geändert“ (korrektur-nach-gegenpruefung.md) bezog sich auf den Vergleich mit dem ersten Stand 75cfbedb. Gegen 75cfbedb sind es heute 37 Aufgabenobjekte und 64 Datensätze. Die beiden Zahlen sind nicht vergleichbar mit den 22 hier, weil die Basis eine andere ist. Die Textsuche nach „Runde“ in der Korrekturdatei ist kein vollständiger Nachweis; maßgeblich ist der Vergleich der Dateien.

## Punkte aus 1207

| Punkt (alt) | neu | Maßnahme |
|---|---|---|
| 053 | V053 | Richtige Option verlangt beide Winkelhalbierenden und sammelt alle Treffer; Erklärung nennt die Sonderfälle parallel und zusammenfallend (Beispiel x- und y-Achse, Haltestellen (1 \| 0) und (0 \| 1)). |
| 206 | V206 | Richtige Option: „Der Schnitt hat die Wahrscheinlichkeit 0“; Erklärung schließt mit „Mehr folgt aus der Gleichung allein nicht.“ |
| 199 | V202 | Frage „… gilt immer?“; Optionen und Fehlbilder nennen die Sonderfälle (A = B, A leer). |
| 203, 204, 205 | V196, V201, V199 (in dieser Reihenfolge) | Aus den Vorgriff-Etappen „bedingt“ und „rueckschluss“ in die genannten Ziel-Etappen umgehängt: 203 Therme „weder … noch“ (34 %) nach `verknuepfen`, 204 Campingplatz „genau eines“ (47 %) nach `venn`, 205 Verlosung (0,16) nach `additionssatz`. |
| 064 | V064 | Fehlbild zu Zeile 3: Beziehung δ = γ ist richtig, falsch nur der Wert. |
| 065 | V065 | Fehlbild zur Summe: Hier prüft man Gleichheit der Stufenwinkel, nicht die Summe. |
| 014 | V014 | Tipp: Kontostand jedes Jahr mal 1,05 oder 2 000 · 1,05ⁿ. |
| 054 | V054 | Text: ③ ist die Summe der Achsenzahlen der einzelnen Figuren, nicht die Achsen einer zusammengesetzten Figur. |
| 083 | V083 | Erklärung mit Konstruktionsskizze (zwei Kreisschnitte, Abstand etwa 4,5 cm). |
| 126 | V126 | Tipp gibt den Wurzelgrad an. |
| 132 | V132 | Fehlbild „… Wurzel (√68) weggelassen“. |
| 150 | V150 | Fehlbild „mit 2 statt 4a malgenommen (k² = 54) und die Wurzel weggelassen“. |
| 191 | V191 | Fehlbild „12 statt 0,12 in den Arkustangens eingesetzt (arctan 12 ≈ 85,2°)“. |
| (Sonderfallprüfung) | V188 | Frage nennt jetzt „spitzen Winkel“. |

### Neue Kennungen in stochastik.verknuepft (alt → neu)

196 → 197, 197 → 198, 205 → 199, 198 → 200, 204 → 201, 199 → 202, 200 → 203, 201 → 204, 202 → 205, 203 → 196. Unverändert: 193, 194, 195, 206, 207.


### Etappen und Mindestbesetzung

Die Etappen `bedingt` und `rueckschluss` sind leer. Das ist gewollt: Bedingte Wahrscheinlichkeit und Rückschluss gehören im bayerischen Lehrplan zu Jahrgangsstufe 11, die Etappen bleiben als freiwillige Vorschau (Vertiefung) im Bestand, und der Befund verbietet neue Aufgaben dort. In `bauen.py` steht dafür die ausdrückliche Ausnahme `VORGRIFF` (nur diese beiden Etappen); für alle anderen Etappen gilt die Mindestbesetzung unverändert und wird in `bauen.py` geprüft. `vorrat_pruefen` meldet 0 in allen vier Gruppen.

### vorpruefung_rechnen.py

Die Datei trägt jetzt einen Kopfkommentar „HISTORISCHER PRÜFSTAND“ und endet mit einem klaren Hinweis und Status 2, wenn Abweichungen gemeldet werden (statt stillem Status 0). Inhaltlich wurde sie nicht „passend gemacht“, nur gegen die verschobenen Kennungen und die geänderte Struktur robust gemacht (Typprüfung in `gleich()`, Feld `index`). Der letzte Lauf meldet 15 erwartete Abweichungen (Stand vor den Korrekturen). Maßgeblich sind `gegenrechnung.py` (207 von 207 Sollwerten, 0 Abweichungen) und `bauen.py`.

## Sonderfälle geprüft (alle 66 Auswahl-Aufgaben)

Geprüft auf (a) die richtige Option versagt in einem Sonderfall und (b) Feedback oder Fehlbild behauptet mehr, als aus der Aufgabe folgt. „geändert“ steht nur dort, wo etwas gefunden wurde.

- V049: Spiegelung an der y-Achse, konkrete Punkte; Zeile 3 rechnet mit dem falschen C' richtig weiter. Kein Sonderfall offen. In Ordnung.
- V053: geändert. Beide Winkelhalbierenden, parallel und zusammenfallend benannt.
- V056: Rechteck ausdrücklich „kein Quadrat“ (sonst vier Achsen); Diagonalen sind keine Achsen. In Ordnung.
- V057: Raute ausdrücklich „kein Quadrat“, Drachen „keine Raute“; Rechteck und Quadrat scheiden über die Diagonalenlängen aus. In Ordnung.
- V060: Aussage gilt für jedes Dreieck, Umlaufsinn nur von der Zahl der Spiegelungen abhängig. In Ordnung.
- V002: Faktor 0,88 gilt für jeden Preis; Fehler 0,088 eindeutig. In Ordnung.
- V008: Faktor 1,2 und 0,8 gelten für jeden Preis; 50 € und 75 € nachgerechnet. In Ordnung.
- V010: Tabellenwerte Bus 25 %, Museum 20 %, Hotel 10 %; kein Gleichstand. Aussagen der Fehlbilder (Euro größer beim Hotel, Museum +3 €) stimmen. In Ordnung.
- V015: 24 % gegen 15 %; Fehlbilder behaupten nur den Vergleich in Übernachtungen und die Schätzung. In Ordnung.
- V016: Rechnung gilt für jeden Anfangspreis (Faktor 0,84); keine Sonderfälle. In Ordnung.
- V155: Scheitelform, a < 0; Vorzeichen in der Klammer eindeutig, andere Optionen scheiden auch bei a = −1 aus. In Ordnung.
- V158: Spiegelung an der x-Achse kehrt alle y-Werte um; Probe bei x = 5. In Ordnung.
- V160: Fehler liegt eindeutig in Zeile 3 (25 nicht abgezogen), Zeilen 1 und 2 stimmen. In Ordnung.
- V081: 180° − 104° = 76°; Basiswinkel 52° ist spitz, gleichschenklig ohne Sonderfall. In Ordnung.
- V082: SWS nur bei eingeschlossenem Winkel; hier eingeschlossen. In Ordnung.
- V083: Option 1 (WSW) legt das Dreieck fest, Option 3 (SsW mit kleinerer Gegenseite) liefert zwei Dreiecke, Erklärung mit Skizze belegt das; 3 + 4 < 8. In Ordnung (Erklärung ergänzt, siehe oben).
- V084: gleiche Winkel, also ähnlich, nicht kongruent; Zeile 3 ausdrücklich als richtig gekennzeichnet. In Ordnung.
- V087: Grenzfall 3 + 4 = 7 ist der Kern der Aufgabe (Gleichheit am Rand); „länger“ gilt strikt. In Ordnung.
- V089: WSW-Konstruktion, Winkel an den richtigen Ecken; die Winkelsumme 105° lässt einen Schnitt zu. In Ordnung.
- V091: Gegenbeispiel 8 genügt für „falsch“; Fehlbilder behaupten nur Formfehler. In Ordnung.
- V092: Rechteck 3 × 4 ist kein Quadrat, Diagonalen gleich lang; Raute und Parallelogramm 3/5/60° haben verschieden lange Diagonalen (Parallelogramm 7 und etwa 4,36 cm). In Ordnung.
- V064: geändert. Fehlbild zu Zeile 3 sagt nur, dass δ = γ richtig und der Wert falsch ist.
- V065: geändert. Fehlbild zur Summe 160° grenzt auf Stufenwinkel ab; Aussage „nicht parallel“ gilt für jedes Paar ungleicher Stufenwinkel.
- V068: Parallele durch eine Ecke gilt für jedes Dreieck; Messung und gleichseitiger Sonderfall beweisen nichts. In Ordnung.
- V074: 108° teilt 360° nicht (3,33); Fehlbilder behaupten nichts über andere Vielecke. In Ordnung.
- V077: Diagonale „im Inneren“ ausdrücklich verlangt, damit auch nicht konvexe Vierecke gelten. In Ordnung.
- V078: Zeile 4 addiert statt zu subtrahieren; 540° − 180° = 360°. In Ordnung.
- V096: Fehler in Zeile 1 (nur links subtrahiert); Folgezeilen mit x = 7/3 stimmen als Folge. In Ordnung.
- V098: x = 11; die drei Falschoptionen haben die Lösungen 5, −1, 5, also keine gleiche Lösung zufällig. In Ordnung.
- V102: Zeile 1 (nur ersten Summanden multipliziert); Folgezeilen konsistent. In Ordnung.
- V104: x = 8 einzige Lösung unter den drei; Gleichung linear, genau eine Lösung. In Ordnung.
- V105: nach dem Zusammenfassen 10 = 13, also keine Lösung (nicht unendlich viele); Fehlbilder behaupten nur das Zusammenfassen. In Ordnung.
- V107: Zeile 4 falsch (keine Lösung statt x = 0); Zeile 3 benennt eine falsche Aussage. In Ordnung.
- V142: Lösung x = 0 gehört dazu; ein Teilen durch x würde sie verlieren. In Ordnung.
- V143: Faktor 6x übersehen; x = 0 ist Lösung (Probe in der Erklärung). In Ordnung.
- V151: D = −31 < 0, kein Sonderfall (D = 0 ist nicht gegeben). In Ordnung.
- V202: geändert. Frage „gilt immer?“; Sonderfälle A = B und A leer sind in den Optionen und Fehlbildern berücksichtigt.
- V206: geändert. Aus P(A ∪ B) = P(A) + P(B) folgt nur P(A ∩ B) = 0, nicht Unvereinbarkeit im Sinn A ∩ B = ∅.
- V207: Additionssatz, Schnitt abgezogen; Zeile 2 ist als richtig gekennzeichnet und stimmt (0,28). In Ordnung.
- V019: Hochzahlen werden addiert (3⁶); Fehler eindeutig in Zeile 2. In Ordnung.
- V021: Mehrere Wege führen zum Ziel, die Frage verlangt ausdrücklich den geschicktesten; Fehlbild 1 nennt den umständlichen Weg als richtig, aber nicht optimal. In Ordnung.
- V024: (x²)³ = x⁶ für jedes x; kein Sonderfall (x = 0 oder 1 verändern die Hochzahl nicht). In Ordnung.
- V028: 7⁵ = 16 807, Fehler in Zeile 3; Zeilen 1 und 2 stimmen. In Ordnung.
- V030: 2⁵ · 3⁴ ist keine Potenz einer ganzen Zahl (ggT der Hochzahlen 5 und 4 ist 1); die drei anderen lassen sich zusammenfassen. In Ordnung.
- V034: 5y + y = 6y; Ergebnis 4x + 6y. In Ordnung.
- V036: nur ein Produkt ergibt −12a²b (die Vorzeichen- und Variablenvergleiche der anderen nachgerechnet). In Ordnung.
- V040: Vorzeichen der letzten Zahl nicht gewechselt; Ergebnis 7a − 7b + 3. In Ordnung.
- V044: Äquivalenz gilt für alle x durch Umformen; ein Beispiel (x = 0) beweist nichts, so steht es im Fehlbild. In Ordnung.
- V045: x = 0 widerlegt; bei x = 1 sind die Werte gleich, das genügt nicht; Fehlbilder sagen nur das. In Ordnung.
- V171: b² = 17² − 8² gilt für jede Hypotenuse mit bekannter Kathete; Zahlen ergeben b = 15. In Ordnung.
- V172: 8, 15, 17 pythagoreisch; die anderen beiden nachgerechnet (625 ≠ 676, 225 ≠ 256). In Ordnung.
- V179: Fehler in Zeile 3 (Hypotenuse addiert); Zeile 2 benennt den Schenkel als Hypotenuse zu Recht. In Ordnung.
- V180: Gegenkathete a; keine Verwechslung mit Hypotenuse möglich (rechter Winkel bei C ausdrücklich genannt). In Ordnung.
- V181: b ist Gegenkathete von β und Ankathete von α; a und c scheiden aus. In Ordnung.
- V188: geändert. Frage auf „spitzen Winkel“ eingeschränkt; sin 70° = cos 20° gilt nur dort eindeutig, bei 45° wäre es der Sonderfall des gleichen Werts.
- V190: Zeile 2 teilt statt zu multiplizieren (15,3 cm); Zeile 4 benennt den Widerspruch, Zeile 3 rechnet mit dem falschen Wert richtig weiter. In Ordnung.
- V126: √50 irrational, die drei anderen rational (0,9; 4; 7/3); der Tipp nennt jetzt den Wurzelgrad. In Ordnung (Tipp ergänzt, siehe oben).
- V133: √100 : √4 = √25 gilt (10 : 2 = 5); die Plus- und Minus-Varianten sind falsch. In Ordnung.
- V136: Zeile 4 falsch (3√2 = √18); Zeilen 1 bis 3 stimmen. In Ordnung.
- V138: Widerspruch über „beide gerade“; Fehlbild 2 behauptet nur, bei gekürztem Bruch sei q ungerade, und das ist der Kern. In Ordnung.
- V139: Fehler in Zeile 3 ((2k)² = 4k²); nicht beliebig gewählt, positive ganze Zahlen vorausgesetzt. In Ordnung.
- V113: 24² = 576; kein Sonderfall, da die Wurzel nicht negativ ist. In Ordnung.
- V118: Kubikwurzel ist keine Division durch 3; 6 · 6 · 6 = 216. In Ordnung.
- V119: 11² = 121 < 130 < 144 = 12²; Seite liegt streng zwischen den Zahlen, keine Grenzfälle. In Ordnung.
- V121: Gilt nur im Bereich der reellen Zahlen (in der Frage ausdrücklich genannt); Fehlbilder behaupten nichts darüber hinaus. In Ordnung.
- V123: Wurzel ist bei Plus nicht verteilbar; 7 · 7 = 49 ≠ 29 zeigt den Widerspruch. In Ordnung.

Ergebnis der Durchsicht: Funde und Änderungen bei V053, V064, V065, V188, V202, V206 (aus der Sonderfallprüfung) sowie die weiteren Punkte aus 1207 (siehe Tabelle oben). Bei den übrigen 60 Aufgaben wurde kein Sonderfall gefunden, in dem die richtige Option oder ein Fehlbild mehr behauptet, als folgt.

## Werkzeug-Tests auf lernen-app (nur untersucht, nichts unter tools/ geändert)

- `tools/tests/rollend_sql_test.py`: Die Liste `SOLL` kennt nur die Runden 1 bis 14. `rollend_sql.py` nimmt Runde 15 bei „alle“ automatisch mit, die Summe stimmt dann nicht mehr („Summe der Soll-Zahlen“). Nötig: ein Eintrag `15: 207` in `SOLL`. Probe in einer Wegwerfkopie: Mit diesem Eintrag läuft der Test bis „OK“. Das ändert kein Paket.
- `tools/tests/regelbezug_sql_test.py`: Die Meldung „regelbezug-lernkarten.json ist nicht auf dem Stand“ kommt daher, dass die erzeugte Datei `inhalte/plan/regelbezug-lernkarten.json` die Lernkarten-Zählungen ohne Runde 15 enthält. Neu erzeugen mit `python3 -I tools/regelbezug_lernkarten.py` ändert nur Zähler („aufgaben“, „anteil“) in dieser Datei; `tools/tests/rb_ww_pakete.py --pruefen` bleibt danach OK, und die md5-Summen aller 45 Dateien unter `tools/tests/aus/` sind vorher und nachher gleich. Danach scheitert der Test aber an einer weiteren Stelle: `ALLE = tuple(range(1, 14))` und der Vergleich „Aufgaben ohne eingespieltes Gegenstück“ (R15-V047 … sind in der Datenbank noch nicht eingespielt). Dafür braucht es eine Entscheidung zum Einspielen von Runde 15 (Paket `rollend15_einspielen.sql`, Regel-Nachtrag, Soll-Zahlen für Fehlbilder), also neue Pakete und Testanpassung.
- Entscheidung: Ich habe weder den Test noch die erzeugte JSON-Datei im Branch geändert (Auftrag: nur beschreiben, wenn mehr als das Registrieren nötig ist). Die JSON-Datei habe ich zur Probe neu erzeugt und wieder auf den Stand der Datei im Repository zurückgesetzt.

## Nachtrag nach Gegenprüfung 1209 (Paketbau)

Inhaltlich freigegeben; vier kleine Hinweise eingearbeitet:
- V057: Fehlbild nennt „ein Drachen, der keine Raute ist, hat …“.
- V084: Erklärung ergänzt: Aus gleichen Winkeln folgt die Kongruenz nicht, die Dreiecke könnten zufällig deckungsgleich sein, sicher ist es nicht.
- V089: richtige Option und Fehlbild nennen „auf derselben Seite von [AB]“ bei beiden Winkeln; das Fehlbild zur falschen Schrittfolge sagt „In dieser Schrittfolge fehlt die festgelegte Strecke“.
- V202 (und V206): Zeichen ⊆ statt ⊂.

Beim Bau der Pakete aufgefallen und behoben: Fünf Fehlbilder mit nicht abbrechenden Dezimalzahlen (V009, V067, V099, V117, V130; 16 Stellen) verletzten die Prüfbedingung `aufgabe_fehlbild_wert_check` (höchstens 15 Nachkommastellen) und hätten das Aufgaben-Paket abgebrochen. Sie stehen jetzt auf zwei Stellen gerundet (5,26; 25,71; 6,86; 457,33; 4,44), wie ein Kind sie eingeben würde; die Beschreibung sagt „(auf zwei Stellen gerundet)“. Lösungen und Aufgabentexte sind unverändert. `bauen.py` OK, `gegenrechnung.py` 0 Abweichungen.
