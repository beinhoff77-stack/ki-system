# Eltern- und Lehrerseite – Prüfbericht (2026-11-16)

Zweig `pruefung-eltern` (von `lernen-app`). Nichts an App, Tests, Datenbank oder Inhalten geändert.

**Grundlage**
- **Code gelesen:** `lernen.js` (`viewLernen`, `viewPlan`, `viewLehrplan`, `viewRueckmeldungen`, `viewZugaenge`), Migration `20261114_w150_lern_zugaenge_plan.sql` (`schule_plan_lesen`/`schule_plan_setzen`).
- **Rundgang nachgestellt:** `rundgang.test.cjs`, Anmeldung als Lehrer auf `/lernen/`. Tablet, Handy und Rechner, mit echter Orte-Struktur (`orte.json`) und einem 12-Orte-Plan (Testdaten).
- **Ergebnisse:** Bilder in `bilder/`, Messwerte in `messung.json`.
- **Entwurf zum Auswählen:** Artifact „Eltern- und Lehrerseite: Heute oder Vorschlag?“.

## Befunde (nachgestellt, außer [Code])

| Nr. | Befund | Schwere |
|---|---|---|
| E1 | **Ungespeicherte Planänderungen gehen ohne Warnung verloren.** Melbourne von Platz 10 nach oben verschoben, Seite verlassen, zurück: wieder Platz 10, kein Hinweis. | hoch |
| E2 | **Umsortieren ist mühsam.** Nur ⤒ ↑ ↓; Platz 10 → 2 = 8 Tipps. Kein Ziehen, keine „an Stelle …“-Eingabe. | hoch |
| E3 | **Plan ist sehr lang.** Jeder Ort ist eine Karte mit allen Flügen und „ansehen“-Links: 500 px (Tablet) bzw. 700 px (Handy) je Ort. 12 Orte = 5 400 / 6 500 px. „Plan speichern“ klebt unten (gut). | mittel |
| E4 | **Nur ganze Orte planbar** [Code]. „Kann es schon“, „Entfernen“ und Reihenfolge gelten für den Ort. Beispiel: „Zehnerpotenzen“ (Gym 6) in Rom lässt sich für ein Kind der Klasse 5 nicht weglassen. | hoch |
| E5 | **Klasse nur fürs Gymnasium.** „Thema hinzufügen“ ist nur nach Gymnasium-Klassen gegliedert, Realschule und IB fehlen als Stufe je Kind. | mittel |
| E6 | **Kein Plan aus dem Lehrplan.** Ein neuer Plan entsteht Ort für Ort. Ohne Plan sieht das Kind alle Themen. | mittel |
| E7 | **Startseite für Lehrer:** 10 gleich große Karten; was zu einem Kind gehört (Lernreise, Lernstand, Themenplan), steht an drei Stellen. | mittel |
| E8 | **Drei Wege für Änderungswünsche:** Rückmeldungen, „✎ Anmerkung“, „Bauen lassen“. Wer sie bearbeitet und was danach passiert, steht nirgends. | mittel |
| E9 | **Keine Erklärung des Systems** (keine Hilfe- oder Info-Seite; Suche nach „Hilfe/Info/Anleitung“ ohne Treffer). | hoch |
| E10 | **Lehrplan-Übersicht sehr lang:** 16 600 px (Tablet) bzw. 22 000 px (Handy). | niedrig |
| – | **Gut:** Plan mit Versionsschutz (`revision`: zwei Lehrer überschreiben sich nicht) [Code], Verlauf der Änderungen, Notizen, „Speichern“ klebt unten, Inhalte mit allen Lösungen ansehbar. | – |

## Vorschläge
Zur Auswahl im Entwurf (je Punkt Heute / A / B):
1. Startseite (A je Kind ein Bereich / B Cockpit „Zu tun“).
2. Reihenfolge (A kompakte Liste zum Ziehen, speichert selbst mit „Rückgängig“ / B zwei Spalten Plan + Lehrplan).
3. Ebene (A Flüge einzeln planbar / B Orte mit abwählbaren Flügen).
4. Plan anlegen (A Vorlage aus dem Lehrplan / B Vorlage + Häkchenliste „kann es schon“).
5. Änderungen beauftragen (A ein Knopf „Ändern lassen“ überall + Auftragsliste / B Anmerkungen sammeln und gebündelt senden).
6. Info-Seite (A Handbuch mit Kapiteln / B Erste Schritte + Fragen).

Text der Info-Seite: `info-seite.md`.
