# Regel-Universum: Ansicht für Lehrer und Eltern – Vorgabe

Stand 27.11.2026. **Vorgabe des Nutzers:** Der Lehrer muss das Regel-Universum einsehen können, um es zu bewerten und Änderungen zu verlangen. Es muss in der Lehrer-Ansicht verständlich sein und Verweise tragen.
Gehört zum Bau des Regel-Universums (Übersicht A „Sonnensystem“, entschieden am 27.11.), Merkliste Punkt 9. Grundlagen: `inhalte/design/regeln-sonnensystem/umsetzung.md`, `inhalte/plan/regeln-uebersicht-auftrag.md`, `inhalte/mathe-profi/denkpapier-grundregeln.md`.

## Wozu
Das Kind sieht je Regel eine kurze Karte. Ein Lehrer kann damit allein nicht urteilen: Er braucht die fachliche Begründung, die Grenzen der Regel, den Bezug zum Lehrplan und die Stellen in der App, an denen die Regel geübt wird. Und er braucht einen Weg, eine Änderung zu verlangen, der beim Projektleiter ankommt.

## Regeln (verbindlich)
1. **Eigene Seite „Regeln“ im Bereich Eltern und Lehrer**, erreichbar von deren Startseite. Kein Sonnensystem als Pflicht-Einstieg: zuerst eine nüchterne Liste aller Regeln und Arbeitsweisen, gruppiert wie die Planeten. Ein Knopf „So sieht es das Kind“ öffnet die Kinder-Übersicht.
2. **Je Regel ein Blatt mit festen Abschnitten, in dieser Reihenfolge:**
   1. Merksatz, wörtlich wie auf der Karte des Kindes.
   2. Karte des Kindes, vollständig (Beispiel, typischer Fehler, Bild) – der Lehrer sieht genau das, was das Kind sieht.
   3. Fachliche Erklärung: zwei bis drei Sätze, warum die Regel gilt, und **wo sie nicht gilt**. Fachsprache erlaubt, jedes Fachwort einmal erklärt.
   4. **Verweise:**
      - Lehrplan: Schulart, Klasse und Lernbereich, in denen die Regel vorkommt (Quelle mit Stand; „nicht geprüft“ offen ausweisen).
      - Klassen: je ein Beispiel für jede Klasse, in der die Regel wieder auftaucht.
      - In der App: Themen und Lernkarten, die diese Regel üben – jeder Eintrag ist ein Verweis auf die vorhandene Lehrer-Seite des Flugs bzw. der Lernkarte. Dazu bis zu drei Beispielaufgaben mit Lösung.
      - Aufbau: Regeln, auf denen diese aufbaut, und Regeln, die auf ihr aufbauen (gegenseitige Verweise).
      - Typische Fehlbilder, die die App dieser Regel zuordnet (sobald der Server sie liefert).
   5. Stand je Kind (sitzt / in Arbeit / kommt später), sobald der Server ihn liefert; vorher steht dort „Stand folgt“.
3. **Rückmeldung an jeder Stelle, die bewertet werden kann:** Der vorhandene Rückmelde-Knopf der Lehrer-Seiten (`schule_rueckmeldung_geben`) steht am Merksatz, an der Karte, an der Erklärung und an der Zuordnung. Der Bezug nennt die Regel (Kennung) und den Abschnitt, damit der Auftrag ohne Rückfrage bearbeitet werden kann. Arten wie bisher (Fehler, Vorschlag, Frage).
4. **Verständlich ohne Vorwissen:** keine erfundenen Insider-Namen; wo die Kinder-Übersicht einen Kurznamen zeigt, steht auf dem Lehrer-Blatt der Merksatz daneben. Maßstab: `regeln-uebersicht-auftrag.md`.
5. **Eine Quelle:** Texte, Verweise und Zuordnung kommen aus `inhalte/regeln/regeln.json` und `inhalte/regeln/zuordnung.json`. Kinder-Karte und Lehrer-Blatt lesen dieselben Daten; eine Änderung nach einer Rückmeldung ändert beide.
6. **Offenes ehrlich zeigen:** Ist eine Zuordnung oder ein Lehrplan-Bezug unsicher, steht das auf dem Blatt („noch nicht geprüft“), nicht nur in der Ablage.

## Stufen
- **Stufe 1 (ohne Datenbank):** Liste, Blatt mit Abschnitten 1 bis 4 aus den Dateien, Knopf „So sieht es das Kind“. Rückmeldung nur, wenn der vorhandene Rückmelde-Weg einen Bezug ohne Einheit annimmt – sonst erst in Stufe 2.
- **Stufe 2 (mit Datenbank, eigener Satz des Nutzers):** Bezugsfeld „Regel“ für Rückmeldungen, Stand je Kind, Fehlbilder.

## Zu klären beim Bau
- Nimmt `schule_rueckmeldung_geben` heute einen Bezug ohne `einheit_id` an (z. B. nur `bezug` als Text)? Wenn ja, geht die Rückmeldung schon in Stufe 1.
- Lehrplan-Bezug: Welche Quelle liegt im Repo vor (Lehrplan-Matrix)? Nur daraus zitieren, nichts aus dem Gedächtnis.
