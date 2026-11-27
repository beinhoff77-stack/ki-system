# Regel-Universum: Inhalt für den Bau (Übersicht A „Sonnensystem“)

Helfer-Lieferung, 27.11.2026, Zweig `helfer-regeln`. Kein App-Code, keine Datenbank, keine Namen, keine Lerndaten.
**[G]** gesichert (maschinell geprüft) · **[A]** Annahme · **[M]** Meinung.

## Geliefert
- `regeln.json`: 6 Planeten, 15 Regeln, 5 Arbeitsweisen, dazu Texte der Oberfläche (Knöpfe, Legende, Fehlerkasten). Je Regel: Karte des Kindes (Satz, Bild, drei Gewand-Zeilen, Grenze, Probe, Satz für Weg b) und Lehrer-Teil (`merksatz`, `genau_gesagt`, `erklaerung_lehrer`, `gilt_nicht`, `klassen`, `lehrplan`, `baut_auf`, `grundlage_fuer`, `fehlbilder`).
- `zuordnung.json`: Regel → Themen und Lernkarten, `sicher` (ja/teilweise/nein) mit Begründung, `vielleicht` (zählt nicht), je Regel bis zu drei Beispielaufgaben als Verweis (Datei + Stelle).
- `tools/regeln_pruefen.py`: Prüfskript (`python3 -I tools/regeln_pruefen.py`, Exit 0 = in Ordnung).

## Gesichert [G] (vom Skript geprüft)
- 15 Regeln, 5 Arbeitsweisen, Pflichtfelder, Textlängen, Kennungen (klein, ohne Umlaute), Planeten-Zuordnung wie Abschnitt 3.1.
- Regel 4 und 5: Texte und Probe-Ergebnisse wie umsetzung.md 6.2/6.3. Die 13 anderen sind neu nach demselben Muster.
- Nachgerechnet: 45 Gewand-Zeilen (Gleichungen mit „→“ prüft das Skript als gleiche Lösungsmenge), 15 Grenzen (Zeile 2 = Werte von Zeile 1), 15 Proben für x = 2, 3, 4, 50 von 80 Klassen-Beispielen. Die übrigen 30 (Wurzeln, Brüche mit ½, □, Hochzahlen mit Minus) kann das Skript nicht lesen; sie stammen vom Mathe-Profi (`klassenleiter.json`, dort „nachgerechnet“).
- Gegenseitigkeit `baut_auf` / `grundlage_fuer`, keine Kreise. Jedes Thema und jede Lernkarte der Zuordnung gibt es in `inhalte/themen/`; Beispielaufgaben passen zur Lernkarte.

## Annahmen und offen [A]
- **Namen:** „Zeichen-Paar“, „Wert bleibt“ usw. stehen wie in der Vorgabe (`name`). Der Nutzer hat erfundene Insider-Namen abgelehnt (`regeln-uebersicht-auftrag.md`); `name_fachlich` und `merksatz` tragen die sachlichen Namen und Sätze des Mathe-Profis. Welcher Name auf der Karte steht, muss der Nutzer entscheiden.
- **15 gegen 14:** Das Regel-Universum der Mathe-Profis hat 14 Rechenregeln; „Einsetzen und Probe“ ist dort eine Arbeitsweise. Regel 9 (Merksatz, Erklärung, Fehlbilder, Klassen) ist mein Entwurf, nicht vom Mathe-Profi geprüft; Fehlbild-Kennungen `fb.probe.*` sind Vorschläge.
- `umsetzung.md` trägt oben den Vermerk „ABGELEHNT 26.11.“ (RS-H). Die Merkliste (Punkt 9) sagt, am 27.11. sei Übersicht A entschieden. Ich habe der Merkliste und deiner Vorgabe gefolgt; bitte den Vermerk klären.
- Aus den Kinder-Sätzen (`satz`) und den Merksätzen des Mathe-Profis (`merksatz`) können zwei verschiedene Sätze je Regel werden; die Lehrer-Vorgabe will „derselbe Satz“. Entscheidung offen.
- `fest_ab_klasse` stammt aus dem Denkpapier [M], nicht aus dem Lehrplan. `orte` („Diese Regel brauchst du in …“) liefert der Server, nicht diese Datei.
- Zuordnung: nach Regeltext und Titel der Karten, nicht nach den Aufgaben; vom Mathe-Profi nicht geprüft. Der Abgleich mit seiner Themenliste steht je Regel im Feld `abgleich_mathe_profi` (er nennt mehr Themen als ich; ich zähle nur Karten, die die Regel selbst üben). `sicher`: 13 ja, 2 teilweise (5 Minusklammer: keine Karte für Klasse 5/6; 13 Stellenwert: keine Karte „Komma wandert“), 0 nein; keine Regel ohne Karte.
- Regel 15 hat erst Karten ab Klasse 9: für beide Kinder heute „kommt später“.
- Die „sitzt“-Rechnung (alle Karten in `lernkarten` gesetzt?) ist Vorschlag; die Entscheidung liegt beim Mathe-Profi (Denkpapier: sechs Bedingungen).

## Lehrer-Ansicht (Vorgabe `inhalte/plan/regeln-lehrer.md`)
Geliefert: alle Felder der Abschnitte 2.1 bis 2.4 aus diesen zwei Dateien; Lehrplan-Bezug nur aus Dateien im Repo (`themenliste.json`, Lehrplan-Kopie der App vom 27.11.). Offen: Lehrplan nur bis zum Thema geprüft, nicht bis zur Regel, nicht gegen LehrplanPLUS; Regel 9: „nicht geprüft“; Stand je Kind: Server; Fehlbilder der App: Server.
**Rückmeldung:** `api.schule_rueckmeldung_geben` (Migration `20261117_w150_e3_auftraege_bezug.sql`) nimmt einen Aufruf ohne `einheit_id` an (auch `aufgabe_id`, `block_id`, `lernziel` sind frei). Pflicht sind nur `art` (eine von thema_fehlt, zu_ungenau, mehr_aufgaben, schwieriger, leichter, fehler, erklaerung, sonstiges; sonst „sonstiges“) und `text` (1 bis 4000 Zeichen). Aber: `bezug` darf nur erklaerung, etappe, bordkarte, flug, plan, allgemein sein; „regel“ gäbe den Fehler „Unbekannter Bezug“. Stufe 1 geht also mit `bezug` „allgemein“ und `text` „[Regel waage / Abschnitt Merksatz] …“ (Kennung und Abschnitt im Text). Ein eigenes Bezugsfeld braucht eine Migration (Stufe 2) [G, aus den Migrationsdateien gelesen; nicht gegen die laufende Datenbank geprüft].

## Vorschlag Bau in zwei Stufen
- **Stufe 1, ohne Server:** `regeln.json` fest mit der App ausliefern (Abschnitt 7: geht dann auch ohne Netz). Übersicht A im Zustand „ohne Stand“ (alle Monde als Punkt, keine Legende), Sonne mit Liste der 15, Gürtel mit 5 Arbeitsweisen, Regel-Karten, Weg a (Knopf „Regeln“ auf der Reisekarte, Aufstieg, Erde zurück). Fuß der Karte: „Drei Aufgaben …“ erst ab Stufe 2, bis dahin ohne Knopf. Lehrer-Seite „Regeln“ mit Rückmeldung wie oben.
- **Stufe 2, mit Server** (eigener Einspiel-Satz des Nutzers): Stand je Regel (`sitzt`/`in_arbeit`/`spaeter`, nur diese drei Werte, aus `zuordnung.json` und `karte_stand`), Weg b (Regel-Kennung zur falschen Antwort, aus den Fehlbild-Kennungen), Weg c (Regel und zwei Zwillingszeilen je Etappe), Orte je Regel.
- **Der Server muss liefern:** (1) Stand je Regel und Kind; (2) Regel-Kennung zu einer Antwort (Fehlbild) sowie zu einer Etappe; (3) je Regel bis zu vier Orte (Ort, Flug, Klasse); (4) Rückmelde-Bezug „regel“ mit Kennung und Abschnitt; (5) die Zuordnung Regel → Karten als Tabelle statt Datei (oder die Datei per Stand-Funktion lesen).
