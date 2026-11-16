# Gesamtauftrag Umbau Lern-App (Stand 2026-11-16, von Sebastian beauftragt; ergänzt um Eltern-/Lehrerseite)

Fasst die vier Prüfrunden zusammen und legt eine Reihenfolge fest. Die Einzelheiten und Prüfpunkte („fertig, wenn …“) stehen in den drei Umsetzungsdateien:

| Runde | Zweig | Datei | Kürzel |
|---|---|---|---|
| Erklärungen | `pruefung-erklaerung-darstellung` | `inhalte/pruefung/erklaerungen/darstellung/umsetzung.md` | A1–A12 (App), U5–UR (Inhalte) |
| Rückmeldung & Lernweg | `pruefung-rueckmeldung-lernweg` | `inhalte/pruefung/rueckmeldung/umsetzung.md` | V1–V12 in Paketen R1–R4 |
| Kinderansicht & Stand | `pruefung-kinderansicht` | `inhalte/pruefung/kinderansicht/umsetzung.md` | K1–K5 (U1–U8) |
| Eltern- und Lehrerseite (ergänzt 16.11.) | `pruefung-eltern` | `inhalte/pruefung/eltern/umsetzung.md` | E-1 bis E-4 |

Diese Prüf-Zweige **nicht** nach `lernen-app` mergen (sie enthalten Bilder und Prüfskripte). Nur lesen: `git show origin/<zweig>:<datei>`.

**Regeln wie immer:**
- Arbeit im Zweig `lernen-app`.
- Datenbank nur nach den Werkstatt-Regeln W1–W7, als neue Migration.
- Kein Merge nach `main` ohne Sebastians „Live“.
- Keine Kinderdaten in Code, Commits oder Nachrichten.

## Übergreifende Festlegungen (gelten für alle drei Runden)

1. **Wörter in allen Texten (Kinder, Eltern, Lehrer):** Reisewörter durchgehend.

   | Sache | Wort |
   |---|---|
   | Thema | Flug |
   | Lernkarte | Etappe |
   | Aufgabe | Bordkarte |
   | Gebiet | Kontinent |
   | Stadt | Ort |

   Das gilt auch für die Texte aus den Umsetzungsdateien „Erklärungen“ und „Rückmeldung“. Beispiele: „Nächste Lernkarte ›“ wird zu „Nächste Etappe ›“; „Die Lernkarte sitzt“ wird zu „Die Etappe sitzt“. Intern (Code, Datenbank, `inhalte/README.md`) bleiben die bisherigen Namen.
2. **Eine Gliederung für alles:** Kontinent → Flug → Etappe. Sie gilt für Merkheft (K2), Übersicht der Etappen im Erklären-Reiter (A1), Mein Weg (K2) und Eltern-Landkarte (K4).
3. **Offene Kleinentscheidungen mit Standard** (Sebastian kann später ändern):
   - Erklärungen Punkt 10 („Kurz gesagt“ in Klasse 7–10): Schalter, Standard **aus**.
   - Rückmeldung V9: höchstens **6** Wiederholungen vor dem Flug.
   - Frühere/höhere Klassen: **wie heute**, nur Fehler B4 beheben.

## Reihenfolge

| Phase | App (Haupt-Chat) | Daten / Inhalte | Warum diese Reihenfolge |
|---|---|---|---|
| **1 – Fehler und kleine Darstellung** | Erklärungen A2, A5–A9, A12 · Rückmeldung R1 (V1 Flächen, V5, V6, V7, V10, V11) · Kinderansicht K1 inkl. Reisewörter · Eltern E-1 (Plan speichert sofort mit Rückgängig, Info-Seite) | **D1:** Klassen-Zuordnung prüfen und je Schulart und Klasse eine Lehrplan-Reihenfolge der Flüge festlegen (Spalte `reihenfolge` in `themenliste.json`, Voraussetzung für E-4). Die 16 Themen ohne `lehrplan_gym` gegen LehrplanPLUS abgleichen, zuerst Winkelsätze und Ortslinien. Liste mit Vorschlag an Sebastian. Inhalts-Chat, nur `inhalte/themenliste.json` und Generatoren. | Behebt falsche Anzeigen sofort für alle 549 Etappen. D1 ist Voraussetzung für Stand und Einstiegs-Check. |
| **2 – Flug-Seite, Mein Weg, Plan** | Erklärungen A1, A3, A4 · Rückmeldung R2 (V3, V2, V8; **nach A9**, gleiche Stelle `zeichneUeben`) · Kinderansicht K2 · Eltern E-2 (Startseite je Kind, Plan in zwei Spalten, Flüge abwählbar) und E-3 („Ändern lassen“ überall + „Meine Aufträge“) | **D2:** nach Sebastians Freigabe zu D1 die 13 Orte neu zuordnen (K5) | Neue Grundstruktur, auf die Phase 3 aufsetzt |
| **3 – Stand und Eltern** | Kinderansicht K3 (Mini-Linien, Stand mit 3 Ebenen, Feld `stufen`) · K4 Eltern-Ansicht · Eltern E-4 (Plan aus Lehrplan-Vorlage, nutzt `stufen`) · Rückmeldung R3 (V9, V12) · Erklärungen A10 (neue Zeichnungen), A11 (Prüfregeln) | – | Braucht korrekte Klassen (D1/D2) und die Gliederung aus Phase 2 |
| **4 – Inhalte umbauen** | – | Erklärungen: Pakete U5 → U8 → U6 → U7 → U9 → U10 → Rest (Inhalts-Chats, Auftragstext in der Umsetzungsdatei Erklärungen, Abschnitt 5) · Rückmeldung R4 (Fehlbilder) erst nach Auswertung echter Fehler | Braucht A3/A4/A10/A11 aus Phase 2/3 |

**Freigaben durch Sebastian:**
- zwischen D1 und D2 (Klassen-Zuordnung);
- vor U6 (Ausprobieren mit den Kindern).

Jede Phase endet mit einer Meldung im Postfach. Danach laufen die Nachprüfungen.

## Nachprüfung (Prüf-Chat)

Nach jeder Phase laufen diese Skripte gegen `lernen-app`:
- `inhalte/pruefung/rueckmeldung/nachstellen.test.cjs`
- `inhalte/pruefung/kinderansicht/rundgang.test.cjs`
- `inhalte/pruefung/eltern/rundgang.test.cjs` (Zweig `pruefung-eltern`)
- die Erklär-Aufnahme `inhalte/pruefung/erklaerungen/darstellung/aufnahme.test.cjs`

Das Ergebnis geht ins Postfach `pruefung-kinderansicht.md`.

**Zusammenspiel Eltern/Kinder:** E-2 (Flüge abwählbar) und K2/K3 (Stand, Mein Weg) müssen dieselbe Regel nutzen: Ein abgewählter Flug zählt für das Kind weder im Plan noch beim Stempel. Für den Stand je Schulart zählt er weiter mit, als „nicht geplant“ grau.
