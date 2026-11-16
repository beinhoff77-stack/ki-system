# Eltern- und Lehrerseite – Umsetzung (Stand 2026-11-16, nach Sebastians Auswahl)

Grundlage: `bericht.md` (E1–E10), Entwurf „Eltern- und Lehrerseite: Heute oder Vorschlag?“ (Artifact), Text `info-seite.md`.
Alles im Zweig `lernen-app`. Datenbank nur nach Werkstatt-Regeln W1–W7 (neue Migration). Kein Merge nach `main` ohne Sebastians „Live“.
Wörter in allen Texten für Kinder **und** Eltern/Lehrer wie im Gesamtauftrag: Flug = Thema, Etappe = Lernkarte, Bordkarte = Aufgabe, Kontinent = Gebiet, Ort.

## Entschieden

| Punkt | Entscheidung |
|---|---|
| Startseite | **Je Kind ein Bereich:** Name, Klasse, Stand in drei Schularten (Mini-Balken), „Jetzt: …“, Knöpfe Lernstand · Themenplan · Lernreise ansehen. Darunter „Für alle Kinder“: Lehrplan · Aufträge · So funktioniert’s. Oben rechts immer „ⓘ So funktioniert’s“. |
| Plan: Reihenfolge | **Zwei Spalten:** links der Plan als kompakte Liste (eine Zeile je Ort, ziehen am Griff ⠿, zusätzlich ↑ ↓), rechts der Lehrplan nach Schulart und Klasse; Orte von rechts nach links ziehen oder „+“ fügt sie ein. Handy: untereinander. |
| Plan: Ebene | **Orte bleiben, Flüge darin abwählbar:** aufgeklappt hat jeder Flug ein Häkchen „im Plan“. Die Reihenfolge der Flüge im Ort bleibt fest (Lehrplan-Reihenfolge). Stempel, wenn alle *geplanten* Flüge des Ortes geschafft sind. |
| Plan anlegen | **Vorlage aus dem Lehrplan:** 1. Schulart (Hauptziel), 2. Klasse, 3. Stufen in den anderen Schularten (vorbelegt: gleiche Klasse; IB MYP = Klasse − 4). Die App schlägt die Orte der Klasse in Lehrplan-Reihenfolge vor; Geschafftes ist abgehakt. Danach frei anpassen. |
| Änderungen beauftragen | **Ein Knopf „✎ Ändern lassen“ überall** (Erklärung, Etappe, Bordkarte, Flug, Plan). Das Formular kennt den Bezug, bietet Art (Erklärung · Bordkarten · Fehler · neuer Flug) und Vorlagen-Chips und fragt nur „Was soll anders sein?“. Liste **„Meine Aufträge“** mit Status (offen · in Arbeit · erledigt · nicht umgesetzt) und Antwort. Neue Antworten erscheinen auf der Startseite. Ersetzt „Rückmeldungen an die Entwicklung“, „✎ Anmerkung“ und „Bauen lassen“. |
| Info-Seite | **Erste Schritte + Fragen:** oben vier Karten (Plan prüfen · Lernstand lesen · Inhalte ansehen · Ändern lassen), darunter die 7 Kapitel aus `info-seite.md` als aufklappbare Fragen. |

## Muss unabhängig von der Auswahl

- **E1:** Planänderungen dürfen nicht verloren gehen. Jede Änderung speichert sofort (`schule_plan_setzen` mit `revision`). Unten erscheint „Gespeichert · Rückgängig“. Bei einem Versionskonflikt erscheint „Plan wurde inzwischen geändert – neu laden“. Der Knopf „Plan speichern“ entfällt.
- **Info-Seite pflegen:** Ändert sich eine Regel aus Kapitel 3 (Etappe sitzt, Wiederholung, Tests), wird die Info-Seite im selben Schritt angepasst.

## Pakete

| Paket | Inhalt | Fertig, wenn … |
|---|---|---|
| **E-1** (Phase 1) | Sofort-Speichern mit Rückgängig (E1) · Info-Seite „So funktioniert’s“ mit Erste Schritte + Fragen, Text aus `info-seite.md` in Reisewörtern, verlinkt oben rechts auf der Startseite und im Themenplan | `inhalte/pruefung/eltern/rundgang.test.cjs`: Ort verschieben, Seite verlassen, zurück → Änderung ist da. Die Info-Seite ist von der Startseite und vom Plan mit einem Tipp erreichbar. |
| **E-2** (Phase 2) | Startseite je Kind · Plan in zwei Spalten mit Ziehen (Maus und Finger) und ↑ ↓ · Flüge im Ort abwählbar (Datenbank: je Plan-Eintrag eine Liste ausgelassener Einheiten; Kind sieht ausgelassene Flüge nicht; Stempel zählt nur geplante Flüge) | Platz 10 → 2 mit einer Ziehbewegung. Pro Ort auf dem Tablet höchstens 72 px zugeklappt. 12 Orte passen auf einen Tablet-Bildschirm. Ein abgewählter Flug fehlt in der Kinderansicht. |
| **E-3** (Phase 2) | „Ändern lassen“ überall + „Meine Aufträge“ (bestehende `schule_rueckmeldung_geben` mit Bezugsfeldern nutzen; Arten bei Bedarf in der Datenbank ergänzen) · Antworten auf der Startseite | An Erklärung, Bordkarte, Flug und Plan derselbe Knopf. Der Auftrag trägt den Bezug automatisch. Status und Antwort sind in „Meine Aufträge“ sichtbar. |
| **E-4** (Phase 3, nach D1/D2 und K3) | Plan anlegen aus Lehrplan-Vorlage: Schulart, Klasse, Stufen je Schulart (gleiches Feld `stufen` wie K3) | Neuer Plan für Gymnasium Klasse 5 entsteht mit drei Tipps. Die Vorlage enthält genau die Orte der Klasse in Lehrplan-Reihenfolge. |

**Voraussetzung für E-4:** Je Schulart und Klasse braucht es eine **Lehrplan-Reihenfolge** der Flüge. Sie kommt aus dem Inhalts-Auftrag D1 als zusätzliche Spalte in `inhalte/themenliste.json`, z. B. `reihenfolge: {gym_by: 3, rs_by: 5, ib_myp: 2}`.
