# Bauauftrag LB: Lehrplan nach Klasse, 4 Stufen, Lehrpläne RS/IB (Sebastian, 2026-11-20)

Geprüft an App 0.81.1 (`origin/lernen-app`), Themenliste und Datenbank (nur Lehrstoff-Struktur).
Entwurf zum Ansehen: `entwurf/lehrplan-klasse-4-stufen.html` (echte Themen, Beispiel-Lernstand). Bilder: `bilder/lehrplan-klasse-gym8.png`, `bilder/lehrplan-klasse-rs7.png`.
Gilt für die Lehrer- und Elternansicht. Die Kinderansicht bleibt bei Orten.

## Befund (0.81.1, nachgestellt)

1. „Nach Klasse (Lehrplan)“ zeigt **Orte**, nicht Themen. Ein Ort erscheint, sobald einer seiner Flüge in der Klasse liegt; die Zeile zeigt dann alle Flüge mit anderen Klassen (5 Orte mischen Gym-Klassen). Das Kästchen zeigt immer die Gymnasium-Klasse, auch bei Realschule/IB → bei „RS 7“ stehen Kästchen 5, 6, 7, 8 untereinander.
2. Reihenfolge: erst „nicht im Plan“, dann „im Plan“ (grau, unten), innerhalb nach Klasse – **nicht** nach Lehrplan. Bei Gym 8 steht Lehrplan-Nr. 13/14 oben. Vermutung zu Sebastians Beobachtung „bei RS nur die Zusatzthemen“: Die gemeinsamen Themen sind bei seinem Kind schon im Plan oder geschafft und stehen grau ganz unten; oben stehen nur die RS-Zusatzthemen mit „+“. (In der Datenbank hat RS 7 18 Themen, 15 davon gemeinsam mit Gym.)
3. Zählung „Klasse 8: 9 von 14 Flügen“ zählt Flüge, die Liste zeigt Orte.
4. Lehrplan-Bezug (z. B. „M8 1 Funktion und Term“) steht in der Themenliste (`lehrplan_gym`), wird aber nicht angezeigt.
5. Lehrplan-Reihenfolge gibt es nur für das Gymnasium (71 Themen, `reihenfolge.gym_by`). Für Realschule und IB MYP fehlt sie ganz; RS-/IB-Bezüge nur bei 27 Themen (`lehrplan_andere`).
6. Aus dem Lehrplan heraus geht nur „+“. Entfernen, „kann er“ oder „kann er, aber wiederholen“ gehen nicht.
7. Keine Ansicht zeigt einheitlich, was das Kind komplett kann, was in der Wiederholung ist, was gerade dran ist und was noch kommt.

## Die 4 Stufen (gilt in allen Lehrer-/Eltern-Ansichten)

| Zeichen | Stufe | Regel (Flug = Thema) |
|---|---|---|
| ◉ dunkelgrün | **Kann er komplett** | alle Etappen „sicher“ – oder vom Lehrer „Kann er komplett“ gesetzt (heute: „kann schon“) |
| ↻ hellgrün | **Kann er, in Wiederholung** | alle Etappen gelandet, noch nicht alle sicher – oder vom Lehrer „Kann er – aber wiederholen“ gesetzt. Zusatz: „Wdh 3 von 5 · nächste in 4 Lerntagen“ (kleinste Stufe/nächste Fälligkeit der Etappen) |
| ▶ gelb | **Gerade dran** | mindestens eine Etappe begonnen, nicht alle gelandet – oder eine Etappe „wieder offen“, Rückreise oder Test/Verbessern offen. Zusatz: „3 von 7 Etappen“ bzw. „wieder offen“ |
| ○ grau | **Kommt noch** | im Plan, noch nichts begonnen |
| + gestrichelt | **Nicht im Plan** | fehlt, antippen zum Einplanen |

Begriffe wie in „So funktioniert’s“: gelandet, sicher (Wiederholung nach 14 Lerntagen bestanden + Mischkarte richtig + Bordkarte im Flug-Nachtest richtig), wieder offen (zwei Fehler in einer fälligen Wiederholung).
Für „Kann er – aber wiederholen“ gilt „sicher“ ohne Flug-Nachtest: Wiederholung nach 14 Lerntagen bestanden (+ Mischkarte, wenn eine kam) → ◉.

Keine Zählung je Stufe und kein Filter nach Stufe (Sebastian: braucht niemand). Oben bleibt nur eine Zeile „Gym 8: 12 von 14 Themen im Plan oder schon gekonnt“ mit Balken.

## Pakete

### LB-1 Lehrplan „Nach Klasse“ neu (Haupt-Chat, App)

- **Eine Zeile = ein Thema (Flug).** Überschrift = Thementitel, darunter „Gebiet · andere Schularten“ (z. B. „Algebra · RS 7 · MYP 4“).
- **Filter streng:** nur Themen mit genau dieser Klasse in der gewählten Schulart. Gemeinsame und Zusatzthemen gemischt in Lehrplan-Reihenfolge; Themen nur dieser Schulart unter „Nur RS“ / „Nur MYP“ am Ende, solange es keine eigene Reihenfolge gibt.
- **Kästchen/Farbe** zeigt die Klasse der gewählten Schulart (nicht immer Gymnasium) – oder entfällt in dieser Ansicht, weil ohnehin nur eine Klasse gezeigt wird; die Zeile trägt stattdessen die Stufenfarbe.
- **Reihenfolge = Lehrplan** der gewählten Schulart, Zwischenüberschrift je Lernbereich (z. B. „M8 1 Funktion und Term“). Eingeplante und gekonnte Themen bleiben an ihrem Platz (nicht nach unten schieben).
- **Stufe je Zeile** (Zeichen, Farbe am linken Rand, Wort + Zusatz rechts).
- **Aufklappen:** Lehrplan-Bezug, Kurzbeschreibung (`umfang`), Etappen mit Stand, „Inhalte ansehen ›“ und 4 Knöpfe:
  1. **Lernen** (bzw. „+ In den Plan“): normal üben mit Test, Wiederholung, Nachtests.
  2. **Kann er – aber wiederholen:** siehe LB-3.
  3. **Kann er komplett:** wie heute „kann schon“ je Flug; keine Übung, keine Wiederholung.
  4. **Aus dem Plan nehmen:** Flug abwählen (gibt es als „ausgelassen“); sind alle Flüge eines Ortes abgewählt, verschwindet der Ort aus dem Plan. Fortschritt bleibt gespeichert.
- **„+ In den Plan“** nimmt den Ort auf, aber nur mit diesem Flug; die anderen Flüge des Ortes werden abgewählt (ausgelassen) und stehen in ihrer eigenen Klasse weiter mit „+“.
- Alles speichert sofort, mit „Rückgängig“.

### LB-2 Die 4 Stufen überall (Haupt-Chat, App)

Gleiche Zeichen, Farben und Wörter in:
- Lehrplan „Nach Themengebiet“ (LA-8): Stufe statt nur „✓ im Plan“; Aufklappen mit denselben 4 Knöpfen.
- Plan (linke Spalte): je Ort die Stufe; aufgeklappt je Flug die Stufe und die 4 Knöpfe (ersetzt „im Plan“-Häkchen und „kann schon“-Häkchen).
- Lehrplan-Übersicht (`#/lehrplan`): Spalte je Kind zeigt die Stufe; gleiche Zeilen-Darstellung wie LB-1, ohne „+“; Spalte „Ort“ entfällt.
- Überblick des Kindes: „Zuletzt geschafft“ mit ◉/↻.

### LB-3 „Kann er – aber wiederholen“ (Haupt-Chat, Datenbank nach W1–W7 + App)

Von Sebastian bestätigt (2026-11-20): ohne Vortest, die Wiederholungsregeln prüfen selbst. Typische Nutzung: ein Kind in Klasse 8 bekommt mehrere Themen aus Klasse 7 nur zur Wiederholung; schafft es die Durchläufe, wird das Thema wieder abgelegt (◉).
- Setzt alle Etappen des Flugs auf **gelandet** und startet die Wiederholung bei Stufe 1 (fällig nach 1 Lerntag, dann 3, 7, 14, 30).
- Es gelten die bestehenden Regeln: höchstens 6 Wiederholungen vor einem Flug; ein Fehler → am nächsten Lerntag wieder; zwei Fehler hintereinander → **wieder offen**, das Kind übt die Etappe (braucht 3 richtige in Folge). So fällt ein falsch eingeschätztes Thema von selbst zurück auf ▶.
- Zählt im Stand als gelandet. Mischkarten und Expeditionen dürfen daraus entstehen.
- Für diese Flüge kein Flug-Test und keine Flug-Nachtests; „sicher“ siehe oben.
- Neues Feld je Kind + Flug (z. B. `route.kann_wdh_themen bigint[]` analog `kann_schon_themen`) und Buchung in `karte_stand` (sitzt = true, Wiederholungsstufe 1, Herkunft „gesetzt“) – genaue Umsetzung Haupt-Chat. Rückgängig: Einträge aus „gesetzt“ wieder entfernen, eigene Lösungen des Kindes bleiben.
- Bei den Eltern sichtbar als „gesetzt: kann er, wird wiederholt“.
- **Auch für abgelegte Themen (◉):** Knopf „Wieder in die Wiederholung“ – alle Etappen starten erneut bei Wiederholungsstufe 1 (bisherige Belege bleiben als Verlauf), Stufe ↻, nach bestandener Wiederholung am 14. Lerntag wieder ◉. Gilt für selbst geschaffte und für „Kann er komplett“ gesetzte Themen.
- **Mehrere auf einmal:** Auswahlmodus (Häkchen je Thema) mit Sammelaktion „Kann er – aber wiederholen“, „Kann er komplett“, „Lernen“, „Aus dem Plan nehmen“; z. B. 6 Themen aus Gym 7 mit einem Schritt.

### LB-4 Lehrpläne Realschule und IB MYP, Lernbereiche Gymnasium (Inhalts-Chat)

Je Thema in `inhalte/themenliste.json` (und in der Datenbank, Übernahme durch Haupt-Chat):
- `reihenfolge.rs_by` und `reihenfolge.ib_myp`: Lehrplan-Reihenfolge innerhalb der Klasse (LehrplanPLUS Realschule Bayern, Wahlpflichtfächergruppe I; IB MYP Mathematik Jahr 1–5).
- `lernbereich: { gym_by, rs_by, ib_myp }`: Lernbereich/Kapitel als Text, z. B. „M8 1 Funktion und Term“ – für die Zwischenüberschriften. Für Gym aus `lehrplan_gym` ableiten und prüfen (heute lassen sich Lernbereiche nur grob ableiten).
- `lehrplan_rs` und `lehrplan_ib`: Kompetenzerwartungen wie `lehrplan_gym` (ersetzt `lehrplan_andere`).
- Klassen-Zuordnung je Schulart prüfen (ein Thema = eine Klasse je Schulart).
Quelle immer angeben (Lehrplan-Link/Abschnitt). Bis das fertig ist, zeigt LB-1 bei RS/IB den Hinweis „Reihenfolge vorläufig wie Gymnasium“.

### LB-5 Plan = Cockpit des Lehrers (Haupt-Chat, App)

Der Reiter „Plan“ ist der Hauptarbeitsplatz: hier wird unser individueller Lehrplan mit allen Funktionen bearbeitet. Andere Seiten (Lehrplan-Übersicht) sind nur Nachschlagen.
- **Links „Unser Lehrplan“** nach Stufen gegliedert: ▶ Gerade dran · ○ Kommt noch (Reihenfolge ziehen/↑↓ wie heute) · ↻ In Wiederholung (mit „Wdh x von 5 · nächste in n Lerntagen“) · ◉ Kann er komplett (zugeklappt, mit Datum). Ersetzt den Block „Geschafft“.
- Jede Zeile (Ort bzw. aufgeklappt je Flug) mit Stufe und denselben Knöpfen wie LB-1: Lernen · Kann er – aber wiederholen · Kann er komplett · Aus dem Plan nehmen; bei ◉ zusätzlich „Wieder in die Wiederholung“.
- Auswahlmodus mit Sammelaktionen (LB-3) links und rechts.
- **Rechts der Lehrplan** wie LA-8/LB-1 (Nach Themengebiet | Nach Klasse) mit Stufen und denselben Knöpfen – Themen lassen sich direkt von dort setzen, ohne den Plan zu verlassen.
- Kopf: „Gymnasium Kl. 8 · 3 ▶ · 9 ○ · 6 ↻ · 14 ◉ · Gespeichert · ↶ Rückgängig“ (eine Zeile, kein Filter).

## Wer macht was

| Paket | Wer | hängt ab von |
|---|---|---|
| LB-1 Lehrplan nach Klasse | Haupt-Chat (bau-lehrer) | – (RS/IB-Reihenfolge später aus LB-4) |
| LB-2 4 Stufen überall | Haupt-Chat (bau-lehrer) | LB-1 (gleiche Zeile), LB-3 für ↻ „gesetzt“ |
| LB-3 Kann er – aber wiederholen | Haupt-Chat, Datenbank (W1–W7) | – (bestätigt) |
| LB-4 Lehrpläne RS/IB, Lernbereiche | Inhalts-Chat | – |
| LB-5 Plan als Cockpit | Haupt-Chat (bau-lehrer) | LB-1, LB-2, LB-3 |

## Fertig, wenn

- „Realschule Kl. 7“ zeigt genau die 18 Themen mit RS 7, gemeinsame und Zusatzthemen, keine anderen Klassen.
- Gym 8 steht in Lehrplan-Reihenfolge mit Lernbereich-Überschriften; Eingeplantes bleibt an seinem Platz.
- Jede Themenzeile in Lehrplan (beide Ansichten), Plan und Lehrplan-Übersicht zeigt eine der Stufen ◉ ↻ ▶ ○ +.
- Aus jeder Themenzeile heraus gehen mit einem Aufklappen: Lernen · Kann er – aber wiederholen · Kann er komplett · Aus dem Plan nehmen.
- „Kann er – aber wiederholen“ erzeugt am nächsten Lerntag eine Wiederholung; zwei Fehler machen die Etappe wieder offen (▶).
- Themenliste hat Reihenfolge und Lernbereich für alle drei Schularten.
- Ein ◉-Thema lässt sich mit „Wieder in die Wiederholung“ zurückholen (↻, Wiederholung am nächsten Lerntag).
- 6 Themen aus Gym 7 lassen sich in einem Schritt auf „Kann er – aber wiederholen“ setzen.
- Der Plan zeigt links alle vier Stufen; alle Knöpfe sind im Plan erreichbar.
