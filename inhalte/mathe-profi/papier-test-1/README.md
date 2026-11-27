# Papier-Test 1 (Auftrag 5, Fassung 2)

Zugeschnittener Papier-Test für beide Kinder: 40 Minuten, 20 Punkte, ohne Tipp, ohne Taschenrechner und Formelsammlung; Geodreieck und Zirkel erlaubt. Kein Bau, keine Einspielung.

**Frage:** Kann das Kind das in der App Geübte auch auf Papier, in Zeit und ohne Tipp – und wie groß ist der Abstand zwischen „wie in der App“ (Teil 1) und „umgedreht, begründet, selbst angesetzt“ (Teil 2)?

## Dateien

| Datei | Inhalt |
|---|---|
| `k5-blatt-a.html` | Klasse 5: Blatt A (Seiten 1–2), Bewertungsschema (3–4), Erfassungsbogen (5) |
| `k5-blatt-b.html` | Klasse 5: Zwilling B – **bis zur Wiederholung in vier bis sechs Wochen nicht zeigen** |
| `k8-blatt-a.html` | Klasse 8: Blatt A, Schema, Bogen |
| `k8-blatt-b.html` | Klasse 8: Zwilling B – nicht zeigen |
| `bauen.py` | rechnet jede Aufgabe auf zwei Wegen nach und schreibt die vier Dateien. Aufruf: `python3 -I inhalte/mathe-profi/papier-test-1/bauen.py` → „OK“ |

**Drucken:** Datei im Browser öffnen, Drucken, A4, Ränder „Standard“, Kopf- und Fußzeilen aus. Für das Kind nur die Seiten 1–2 drucken, Seiten 3–5 für den Erwachsenen.

## Stoff

Nur Themen, die das Kind in den letzten Wochen in der App bearbeitet hat (Versuchsdaten als Summen je Thema gelesen; keine Zahlen hier).

- **Klasse 5:** `zahlen.ganz`, `zahlen.rechengesetze`, `zahlen.natuerlich` (nur Runden). Nicht aufgenommen: römische Zahlen, Zweiersystem, Zahlwörter, `zahlen.potenzen_basis` (erst angefangen).
- **Klasse 8:** `terme.umformen`, `gleichungen.linear`, `terme.bruchterme`, `gleichungen.bruch`, `terme.potenzgesetze_ganzzahlig`. Nicht aufgenommen: Themen mit nur einzelnen Versuchen (`bruch.prozent`, `messen.flaechen_vielecke`, `finanzen.zinsen`, `zahlen.potenzen_zehner`).

## Aufbau (beide Klassen)

| | Punkte | Tätigkeit |
|---|---|---|
| Teil 1 „wie in der App“ | 10 | Rechnen nach Regel, aber mit Rechenweg auf Papier |
| Teil 2 „weiter“ | 10 | Umkehren · Fehler finden und berichtigen · Begründen · Ansatz aus Text · Verfahren wählen |

Themen gemischt: Klasse 5 Aufgabe 8 (`zahlen.ganz` + `zahlen.rechengesetze`), Klasse 8 Aufgabe 9 (`terme.umformen` + `gleichungen.linear`).
Blatt B hat Aufgabe für Aufgabe dasselbe Muster, dieselben Punkte und dieselbe Tätigkeit wie Blatt A, mit anderen Zahlen und anderem Sachtext (das Skript prüft das).

## Tragen 40 Minuten für Klasse 5?

**Einschätzung (Annahme, nicht gemessen): ja, aber knapp.** 13 Teilaufgaben, im Mittel drei Minuten; die Texte haben höchstens drei kurze Sätze. Eng wird es, wenn das Kind in Teil 1 jeden Schritt sehr ausführlich schreibt.
Deshalb: nicht verlängern, sondern im Bogen „bis zu welcher Aufgabe gekommen“ eintragen. Wird das Kind nicht fertig, ist das ein Ergebnis über das Tempo, nicht über den Stoff. Für Blatt B dann dieselbe Zeit.

## Durchführung

1. Ruhiger Platz, Uhr sichtbar, Gerät weg. Keine Hilfe, auch keine Verständnisfragen zur Rechnung (Wörter erklären ist erlaubt; im Bogen vermerken).
2. Nach 40 Minuten einsammeln.
3. Bewerten nach Schema (15–20 Minuten), Bogen ausfüllen. Bewerten kann der Nutzer oder der Lehrer; das Schema setzt keine Mathe-Ausbildung voraus.
4. **Der ausgefüllte Bogen kommt nicht ins Repo.** Ergebnisse gehen nur an den Nutzer.

## Nachgerechnet

Jede Aufgabe auf zwei Wegen (`bauen.py`): Zahlenterme direkt und über einen zweiten Rechenweg; Termumformungen durch Einsetzen an mindestens acht Stellen; Gleichungen über die Koeffizienten und mit Probe; Runden und Klammer-Aufgabe durch Durchprobieren aller Möglichkeiten (genau eine Klammer passt); die offene Umkehraufgabe (Klasse 8, Aufgabe 7) über eine Bedingungs-Prüfung mit zwei falschen Gegenproben.
