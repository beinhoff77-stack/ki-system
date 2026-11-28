# Auftrag an die Aufgabenschreiber „Verstehen in Tests" (vom Projektleiter, 28.11.2026) – darf sinngemäß ins Repo, enthält keine Lerndaten

## Ziel
Der Auftraggeber will, dass Tests (Flugtest, Korrekturtest, Nachtest) in der Mathe-Lern-App generell schwieriger werden und VERSTEHEN prüfen – wie eine echte Schulaufgabe am bayerischen Gymnasium (G9, LehrplanPLUS). Die Hälfte der Etappen (Lernziele) einer Einheit bekommt im Test eine Verstehens-Aufgabe STATT der bisherigen Rechen-Aufgabe. Der Test bleibt gleich lang (eine Aufgabe je Etappe).

## Was du schreibst
Je Einheit: Wähle die HÄLFTE der Pflicht-Lernziele (bei ungerader Zahl aufrunden), möglichst abwechselnd in der Reihenfolge der Etappen, bevorzugt die, deren Inhalt echtes Verstehen hergibt. Schreib die Auswahl mit einem Satz Begründung je Lernziel in `auswahl.md`, BEVOR du Aufgaben schreibst (und committe sie zuerst).
Je gewähltem Lernziel genau 6 neue Aufgaben:
- 1 für Pool `test` (ersetzt später die bisherige Test-Aufgabe dieses Lernziels),
- 2 für Pool `korrektur`,
- 3 für Pool `sicherung` (Nachtest, Wochen später).
Die 6 Aufgaben eines Lernziels prüfen dieselbe Einsicht auf verschiedene Weise (nicht dieselbe Aufgabe mit anderen Zahlen): verschiedene Bauarten, verschiedene Einkleidung.

## Was „Verstehen" heißt (mindestens eines davon je Aufgabe)
umkehren/rückwärts denken · begründen (aus vorgegebenen Begründungen die tragfähige wählen, mindestens 4 Optionen, Ablenker = echte Fehlvorstellungen) · Fehler finden UND richtigstellen · Verfahren wählen und anwenden · zwei Wege vergleichen · übertragen auf eine neue Situation (Transfer/Sachzusammenhang, der nicht nach Schema geht) · Darstellung wechseln · Parameter/Was-wäre-wenn · verknüpfen mit früherem Stoff der Klasse.
Nicht erlaubt in Tests: Lückenweg (Hilfsgerüst); reine Reproduktion/Einsetzen in eine Formel; Auswahl mit weniger als 4 Optionen; Fehler-Detektiv, bei dem nur eine von 3–4 Zeilen angekreuzt wird (Ratechance) – stattdessen: Zeile nennen UND das richtige Ergebnis angeben (Lücken/Zahl) oder Auswahl aus mindestens 4 vollständigen Aussagen „Fehler ist … und richtig wäre …"; Tipps (im Test gibt es keine); „alles oder nichts"-Fragen ohne eindeutige Antwort.
Kein Schutz „Bauart muss vorher geübt sein": Im Test darf jede Bauart kommen.

## Schwierigkeit
Stufe 2 oder 3, keine Stufe 1. Je Lernziel: Test Stufe 2–3, Korrektur Stufe 2, Sicherung gemischt 2 und 3. Lösbar in 2–4 Minuten ohne Taschenrechner (außer der Stoff verlangt ihn ausdrücklich), Kopf und Papier.

## Qualität (aus den Fehlern der letzten Runden)
- Eigene Aufgaben; nichts wörtlich aus Schulbüchern oder Prüfungen. Keine Namen echter Personen aus dem Projekt; neutrale Vornamen/Orte sind erlaubt.
- Jede Soll-Antwort zweifach nachrechnen (eigenes Prüfskript `gegenrechnung.py`, das am Ende „0 Abweichungen" meldet).
- Genau EINE richtige Antwort; Definitionsmenge, zweite Lösungen, Einheiten, Vorzeichen, Grenzen („einschließlich") ausdrücklich im Text.
- Jedes Fehlbild ist eine echte Fehlrechnung als AUSFÜHRBARE Rechnung im Bauskript, die genau den gespeicherten Fehlwert ergibt; der Erklärtext nennt genau diese Rechnung. Kein Fehlbild gleich der Soll-Antwort, keine zwei gleichen.
- Keine `toleranz`. Bei verlangter Rundung steht die Rundungsvorschrift im Text („auf Zehntel gerundet", „abgerundet").
- Lösungsweg vollständig, in Sprache der Klassenstufe.
- Lehrplan: je Aufgabe den LehrplanPLUS-Lernbereich nennen (z. B. „M5 1.2"); nichts aus späteren Klassen. Unsicherheit ehrlich markieren.
- Nicht ähnlich zu den Übungsaufgaben derselben Etappe im Repo (andere Zahlen UND andere Fragestellung) und nicht zu den anderen fünf des Lernziels.
- Felder je Aufgabe wie in der Runde `inhalte/mathe-profi/rollend-15/` (dort Format, Antworttypen, Fehlbilder, `bauen.py` ansehen), zusätzlich: `pool` (test|korrektur|sicherung), `typ` (einer der 13 Bestands-Typen: mehrschritt, direkt, erkennen, einkleidung, verknuepfen, transfer, umkehr, fehler, begruenden, darstellung, rueckwaerts, pruefung, parameter – `direkt` und `erkennen` sind hier NICHT erlaubt), `form` (optional: anwenden, umkehren, verfahren_waehlen, fehler_detektiv, bruecke, zwei_wege, viele_antworten – kein lueckenweg), `stufe` 2|3, `zaehlt` ja, `lehrplan`, `ersetzt_test` (nur bei der Test-Aufgabe: true).
- `bauen.py` der Runde prüft all das automatisch (Verbote, Anzahlen 1/2/3 je Lernziel, Stufen, Fehlbild-Rechnungen, Eindeutigkeit der Kennungen) und endet mit OK.
