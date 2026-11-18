# Lehrer-Gesamtansicht – Durchspielprobe (lernen-app 0.78.1, 2026-11-18)

Stand `origin/lernen-app` 3621724. Testdaten (Mock), keine Kinderdaten. Skripte: `rundgang.test.cjs` (alle Seiten), `szenarien.test.cjs` (Aufgaben durchgespielt, Tablet 820 px und Handy 390 px). Messwerte: `messung.json`, `szenarien.json`.

## Durchgespielt (Tablet)

| Aufgabe | Weg | Tipps | Ergebnis |
|---|---|---|---|
| Hat Kind B diese Woche gelernt? | Start → „Was wackelt?“ | 1 | steht nicht auf der Startseite, nur auf „Was wackelt?“ |
| Wo hakt es bei Kind A, welche falsche Antwort? | Start → „Was wackelt?“ → „Letzte falsche Antworten“ aufklappen | 2 | Startseite zeigt nicht, ob etwas wackelt; Regeltext „Was kommt wann wieder?“ steht davor |
| Kind A kann Teilbarkeit (Athen) schon | Start → Flugplan → Athen → „kann es schon“ | 3 | gut |
| Kind A kann „Ganze Zahlen“ (ein Flug in Rom) schon | Flugplan → Rom | – | **geht nicht**: „kann es schon“ nur für den ganzen Ort; je Flug nur „im Plan“ (abwählen) |
| Melbourne vor Kairo | Flugplan → ↑ | 6 (oder 1× Ziehen) | geht |
| Stufe je Schulart setzen | Flugplan, ganz unten | – | bei y ≈ 1 990 von 2 690 px; Hinweis darauf nur auf „Alle Kinder im Vergleich“ |
| Wo steht Kind A in Zahlen Kl. 5? | Start → Lernstand → Feld | 2 | gut (Flüge mit Stand und Etappen) |
| Einstieg Kl. 6 prüfen | Lernstand → „Kl. 6“ | 1 | gut („2 von 14 … Noch deutliche Lücken“, Liste „fehlen (12)“) |
| Bordkarte ändern lassen | Lehrplan → Inhalte ansehen → ✎ | 2 | gut |

## Befunde

- **L1 Startseite zeigt nicht, wo es hakt.** Kein „wackelt“, kein Lerntag, keine Rückreise (Kind B hat eine offene automatische Rückreise Delhi; Startseite: „Jetzt: Delhi · Lineare Gleichungen (0/6)“). „Alle Kinder im Vergleich“ zeigt „2 wackelt“, die Startseite nicht.
- **L2 „Lernen starten“ ist der größte Knopf je Kind** – für den Lehrer die unwichtigste Handlung.
- **L3 Drei Stand-Ansichten** (Startseite-Balken x/n, Vergleich x/n, Lernstand %) mit verschiedenen Zahlenformen. IB bei Klasse 5: „vor MYP-Jahr 1 · –“ / „0/0“.
- **L4 Einstellungen verstreut:** Reihenfolge, Flüge, „kann schon“, Vorlage, Klasse, Stufen, Notizen, Verlauf alle auf der Flugplan-Seite (2 690 px), Stufen ganz unten. Plan und Lehrplan auf dem Tablet untereinander; Lehrplan zeigt nur fehlende Orte, Auswahllisten statt Reiter.
- **L5 „kann schon“ fehlt je Flug.** Abwählen ist kein Ersatz: abgewählt zählt im Stand als „nicht geplant“, nicht als gelandet.
- **L6 Geschafftes wird nicht abgelegt.** Geschaffte Orte bleiben im Plan an ihrem Platz (grau, z. B. Toronto auf Platz 2). Es gibt keine Liste „Geschafft“ mit Datum; Geschafftes steht nur als Farbe im Lernstand und als Chip in der 16 700 px langen Lehrplan-Übersicht.
- **L7 Zu viel Text an Arbeitsstellen:** „Was wackelt?“ beginnt mit Kennzahlen und dem Regelblock „Was kommt wann wieder?“; die falschen Antworten sind zugeklappt. Regeln gehören auf „So funktioniert’s“.
- **L8 Lehrplan-Übersicht** 91 Flüge als große Karten, 16 700 px (Tablet). Als Nachschlagewerk ok, als Arbeitsseite zu lang (Liste/Tabelle, Filter oben vorbelegt auf Klasse des Kindes).
- **L9 Ort mit Flug einer höheren Klasse:** Rom (Gym 5) enthält „Zehnerpotenzen · Gym 6“ ohne Hinweis; der Hinweis kommt nur, wenn *alle* Flüge eines Ortes höher liegen.

Nicht belegt: Inhalt unter „Letzte falsche Antworten“ war im Test leer (Testdaten). Zugänge-Seite: Fehler nur mit Testdaten (Seite ist nur für Eltern verlinkt).
