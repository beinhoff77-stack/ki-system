# Eingangsdiagnose auf Papier (diagnose-1)

Zwei Blätter, je 14 kurze Aufgaben, **30 Minuten**, ohne Taschenrechner. Sie prüfen, ob **tragende Ideen aus früheren Klassen** sitzen – nicht den aktuellen Stoff. Hintergrund: Die App prüft nur, was sie selbst unterrichtet hat; was die Route nie anfliegt, kann sie nicht als Lücke finden (Postfach mathe-profi, Punkt 2).

| Datei | Für | Prüft |
|---|---|---|
| `k8-diagnose.html` | Kind 2 (Klasse 8) | Stoff Klasse 5 bis 7, den die Route von Kind 2 nicht mehr anfliegt: ganze Zahlen und Rechenregeln, Stellenwert mit Komma, Größen und Einheiten (auch Flächen), Brüche (Kürzen, Addieren), Prozent, Flächen (L-Figur, Dreieck), Nebenwinkel, Rückwärtsrechnen, Mittelwert |
| `k5-diagnose.html` | Kind 1 (Klasse 5) | Grundlagen für die kommenden Flüge: Stellenwert, schriftlich Plus/Minus/Mal, Einmaleins und Umkehren, Teilen mit Rest, Zahlenstrahl, Größen umrechnen, Fläche, Winkelarten, Bruch als Anteil, Bruchteil von einer Größe, Sachaufgabe mit zwei Schritten |
| `bauen.py` | – | Erzeugt beide Blätter, rechnet jede Lösung auf einem zweiten Weg nach, berechnet die Fehlantworten aus Fehlermodellen, prüft Kennungen, Themen, Flüge und Route. Aufruf: `python3 -I inhalte/mathe-profi/diagnose-1/bauen.py` → endet mit „OK“ |

Jede Aufgabe prüft **genau eine Idee** (Kennung aus `regeln-uebersicht/kennungen.json`, nur im Lösungsteil). Aufgabe 14 bei Kind 1 (Sachaufgabe) gehört zur Arbeitsweise „Ansatz“ und hat keine Kennung. Aufgabe 12 bei Kind 1 nutzt `id.daten.anteil` als nächstliegende Kennung (Vermutung; ein Klasse-5-Beispiel für Bruchanteile gibt es dort nicht).

## Aufbau jeder Datei
Seite 1–2: Blatt für das Kind (ohne Kennungen) · Lösungen mit je zwei häufigen Fehlantworten und Deutung (Vermutung) · Erfassungsbogen · Auswertungshilfe in einfacher Sprache mit Tabelle „Aufgabe · Idee · wenn falsch, dann fehlt vermutlich … · passender Flug“. Für das Kind nur Seiten 1–2 drucken (A4, Ränder „Standard“, Kopf-/Fußzeilen aus).

## Durchführung
1. Ruhiger Platz, Uhr sichtbar, Gerät weg. Keine Hilfe. Wörter erklären ist erlaubt.
2. Nach **30 Minuten „Strich“** sagen. Das Kind wechselt den Stift und arbeitet weiter, bis es fertig ist; Zeit gesamt notieren.
3. Erfassungsbogen: je Aufgabe „✓ bis Strich“ (erster Stift, richtig), „✓ mit Zugabe“ (am Ende richtig) und Kästchen **„nicht angefangen“** (leer, „weiß nicht“ oder nur abgeschrieben – ein anderes Signal als „falsch“). Zwei Wertungen: **Stand nach 30 Minuten** und **Stand mit Zugabe**.
4. Falsche Aufgaben mit dem Kind laut nachsprechen, bevor man eine Lücke annimmt.
5. Der ausgefüllte Bogen kommt nicht ins Repo; Ergebnisse gehen nur an den Nutzer.

## Was das Blatt NICHT kann
- Keine Note, kein Normwert, kein Schwellenwert – nichts davon ist an Kindern getestet. Fehlantworten und Deutungen stammen aus Fehlermodellen, nicht aus Beobachtung.
- Je Idee nur **eine** Aufgabe (K8: Größen zweimal): Eine falsche Antwort ist ein Hinweis, kein Beweis (Flüchtigkeit, Lesefehler).
- Prüft nicht das Verstehen (Begründen, Fehler finden) und nicht den aktuellen Stoff.
- Deckt nicht alles Frühere ab: nur 14 Ideen je Blatt. Nicht geprüft u. a. Potenzen, Teilbarkeit/Primfaktoren (K8), Dezimalzahlen rechnen, Dreisatz, Geometrie-Zeichnen.
- Kein Zwillingsblatt für eine Wiederholung; kein Bau in App oder Datenbank.
- Das Druckbild wurde per Browser-PDF auf Seitenzahl geprüft (Blatt für das Kind: 2 Seiten), nicht auf Papier.
