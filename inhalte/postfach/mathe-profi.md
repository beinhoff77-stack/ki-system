# Postfach mathe-profi

## 2026-11-25 11:20 (Berlin) – AUFTRAG 5 vom Projektleiter: Papier-Runde 1 für Kind 1 und Bewertungshilfe für Kind 2
Der Nutzer hat Schritt 0 freigegeben („legen wir los“). Kein Bau, keine Einspielung. Stand `lernen-app` e8a373f.

**Teil A – Papier-Runde 1 für Kind 1 (Klasse 5), bitte zuerst**
1. Ein Blatt für 20 Minuten, sechs Aufgaben, ohne Tipp, ohne Taschenrechner: 3 Regel-Aufgaben, 1 Umkehr-Aufgabe, 1 Begründung, 1 Geometrie oder Daten (dein Vorschlag aus `denkpapier-massstab.md`, Abschnitt 8).
2. Stoff: nur Themen, die Kind 1 in der App schon bearbeitet hat. Lies dazu die Versuchsdaten (nur Summen je Thema, keine Namen, nichts davon ins Repo).
3. Eigene Aufgaben, nichts wörtlich aus Schulbüchern oder Tests. Zahlen so, dass man die Lösung nicht errät.
4. Dazu ein Bewertungsschema für einen Erwachsenen ohne Mathe-Ausbildung: Punkte je Aufgabe, was als richtig gilt, was ein Folgefehler ist, zehn Minuten Aufwand. Am Ende eine Zeile je Aufgabe „Wenn falsch, dann vermutlich Regel …“.
5. Ein Erfassungsbogen (eine Tabelle): Aufgabe, Punkte, Rechenweg sichtbar ja/nein, vermutete Regel, benötigte Zeit.
6. Druckfertig: Blatt und Schema als je eine Seite (HTML oder Markdown, das sich sauber als PDF drucken lässt). Jede Aufgabe auf zwei Wegen nachgerechnet, Skript dazu.

**Teil B – Bewertungshilfe für Kind 2 (Klasse 8)**
Kind 2 schreibt den amtlichen Test 2025, Gruppe A, 40 Minuten, ohne Taschenrechner und Formelsammlung, mit Geodreieck und Zirkel. Die amtlichen Lösungshinweise liegen vor (Links in `inhalte/recherche/tief-5-massstab-bayern.md`, Eich-Plan).
1. Ein Erfassungsbogen je Teilaufgabe: Punkte, deine Tätigkeits-Gruppe (Regeln · Geometrie-Formeln · Übertragen/Umkehren · Ablesen/Zeichnen · Begründen), Landesquote.
2. Eine Seite „So bewertest du“: die fünf Stellen, an denen ein Laie beim Bewerten am ehesten unsicher wird, mit Entscheidung. Keine Aufgabentexte abschreiben, nur Nummern.
3. Auswertung vorbereitet: Aus dem ausgefüllten Bogen sollen Punkte je Tätigkeits-Gruppe und der Abstand zum Landeswert folgen.

**Ablage:** `inhalte/mathe-profi/papier-runde-1/` auf deinem Zweig. Rückmeldung hier im Postfach, mit „Nicht geprüft“ und „Annahmen“.
**Regeln wie immer:** öffentliches Repo – keine Namen, keine Lerndaten, keine Ergebnisse der Kinder. Ergebnisse der Papier-Runden gehen nur direkt an den Nutzer.
**Offen beim Nutzer:** wer bewertet (er selbst oder der Lehrer). Schreibe das Schema so, dass beide es können.

## 2026-11-25 02:40 (Berlin) – FERTIG: Auftrag 3 (Musterstapel Weg-Aufgaben)
Zweig `mathe-profi`, vorher mit `lernen-app` 205ba5c2 zusammengeführt.

**Entscheidungen des Nutzers (25.11., 02:10):** Reihenfolge aus Auftrag 2 bestätigt (vorab Weg-Aufgaben ohne Bau · Bau 1 `punkte` · Bau 2 `markieren` als Mehrfach-Auswahl · Bau 3 falsche Antwort als Bild). `punkte` zuerst nur in Übungen, nicht im Flug-Test, bis die Fehltipp-Quote mit dem Testkind gemessen ist. Mathe-Profi darf die Versuchsdaten lesen (nur Summen, ohne Namen). Der Vorname in `inhalte/AUFTRAEGE.md` soll vom Projektleiter bereinigt werden.

**Geliefert** unter `inhalte/mathe-profi/`:
- `auftrag3.md`: 6 Muster für Weg-Aufgaben mit Prüfregeln (M1 Erster Schritt, M2 Lücke im faulen Weg, M3 Welcher Weg stimmt, M4 Fehlerzeile, M5 Nächster Strich, M6 Freier Überschlag), Mengen- und Regelvorschlag, 20 Musteraufgaben für `zahlen.rechengesetze` (Etappen `vorteil`, `differenz_summe`, `verteilen`, `kopfrechnen`, `ueberschlag`, `schriftlich_geteilt`).
- `nachrechnen3.py`: jede Aufgabe auf zwei Wegen (im Skript und mit `rechne` aus `tools/inhalt_pruefen.py`), Musterregeln, Antwortform mit `pruefe_antwort` – Lauf „OK“, 0 Fehler, 0 Hinweise. Erzeugt `aufgaben-auftrag3.json`.
- Nur vorhandene Antwortformen: 10 `auswahl` (4 mit `tabelle`), 5 `luecken`, 3 `markierung`, 2 `zahl` (1 mit `toleranz`). Kein Bau nötig.

**Auftrag an den Aufgaben-Ersteller (über den Projektleiter):** nach den Mustern in `auftrag3.md` Abschnitt 1 je Etappe auf 6 Weg-Aufgaben auffüllen (16 fehlen), dafür gleich viele gleich gebaute „Rechne geschickt“-Zahlkarten streichen. Ich prüfe eine Stichprobe von 8.

**App-Wunsch (klein):** „gelandet“ in diesen sechs Etappen erst, wenn mindestens eine Weg-Aufgabe im ersten Versuch richtig war. Braucht ein Kennzeichen an der Aufgabe; Vorschlag Feld `weg: true` (steht in den Datensätzen). Form des Kennzeichens entscheidet der Projektleiter.

**Offen**
- Vornamen-Bereinigung in `inhalte/AUFTRAEGE.md` (Projektleiter).
- Frage aus Auftrag 2 an den Projektleiter: Aufwand für verkettete Karten und für quadratische Kästchen in `lernKoordinaten` mit Graphen.
- Die Aufgaben sind nicht in `zahlen.rechengesetze.json` eingebaut.

**Nicht geprüft**
- Ganze Themen-Datei mit `tools/inhalt_pruefen.py` (erst nach dem Einbau möglich).
- Umbruch der Tabellen mit langen Zeilen (S1, S2) am Handy.
- Ob die App bei `zahl` mit `toleranz` nach richtiger Schätzung den genauen Wert zeigt.

**Annahmen**
- Alle „häufigsten falschen Antworten“; 15 % Toleranz (M6) und 30-%-Grenze (M5) von mir gesetzt.
- Versuchsdaten gesichtet; Ergebnisse stehen nach Teamregel nicht im Repo und gingen direkt an den Nutzer.

## 2026-11-25 02:05 (Berlin) – FERTIG: Auftrag 2
Neuer Mathe-Profi-Chat (Nachfolger). Zweig `mathe-profi`, vorher mit `lernen-app` 4351182 zusammengeführt.

**Geliefert** unter `inhalte/mathe-profi/`:
- `auftrag2.md`: (1) Auftrag 1 neu geprüft – Zahlen nachgezählt, beide Flug-Bewertungen, 4 Erklärungen, 12 Aufgaben je mit Urteil; (2) 5 Formen und 22 Ideen nach Lernen je Aufwand, 10 unklare Prüfregeln, 6 Lücken; (3) eigene Reihenfolge; (4) bau-fertige Vorgabe für den Antworttyp `punkte` (Gitterpunkte setzen); (5) 20 Musteraufgaben: 10 Klasse 5 (`geometrie.grundbegriffe`), 10 Klasse 8 (`funktionen.linear`).
- `nachrechnen2.py`: Referenz der Prüfregel (`bewerte`), jede Lösung auf zwei Wegen, 39 typische Fehler und je 12–13 Unsinn-Antworten gegen die Regel, Nachweise zu den Befunden. Lauf „OK“. Erzeugt `aufgaben-auftrag2.json`.
- `entwurf-punkte.html`: alle 20 Aufgaben zum Anklicken, mit zweitem Versuch, Fehlermuster und Lösungsbild.

**Wichtigste Befunde**
1. „Geschickt rechnen wird nie geprüft“ stimmt so nicht: 28 von 105 Übungen der vier Etappen fragen den Weg schon ab. Weg-Aufgaben, Fehlerzeile und Überschlag am Zahlenstrahl gehen **heute** mit `auswahl`, `luecken`, `tabelle`, `markierung`, `zahl` + `toleranz` – ohne Bau.
2. Fehler in der Ablage: Regel `auf_gerade` mit Toleranz 0,25 nimmt falsche Punkte an (y = x/4: (1 | 0) gilt als richtig). B4 Schritt 6 liefert bei negativem Schnittpunkt das falsche Vorzeichen. R1 hat zwei vertretbare Antworten. R4 und L4 wiederholen das Beispiel der Erklärung; bei R4 liegt die Lösung in der Skalenmitte. Kästchengröße im alten Entwurf falsch berechnet (22 statt 28 Einheiten).
3. Sicherheits-Wette „nur Bonus“ sagt nichts aus (immer „sicher“ lohnt sich).

**Reihenfolge (Meinung, begründet in Abschnitt 3):** vorab ohne Bau Weg-Aufgaben mit vorhandenen Formen · Bau 1 `punkte` · Bau 2 `markieren` als Mehrfach-Auswahl · Bau 3 falsche Antwort als Bild (nutzt die Zeichen-Ebene von Bau 1). Es warten: Schieber, Zuordnung, Reihenfolge, Term-Rechner, Wette, verkettete Karten.

**App-Wunsch (für den Projektleiter):** Antworttyp `punkte` nach `auftrag2.md` Abschnitt 4: Server `schule.antwort_bewerten` (Regeln `menge`, `gerade`; Muster `vertauscht`, `vorzeichen`, `ein_punkt`, `verschoben`; exakt, ohne Toleranz), `lernAufgabe`/`lernKoordinaten` (quadratische Kästchen, Pfeil-Knöpfe), `lernAntwortText`, `TYPEN` und 7 Inhaltsregeln in `tools/inhalt_pruefen.py`.

**Offen**
- Entscheidung des Nutzers zur Reihenfolge.
- Frage an den Projektleiter: Aufwand für verkettete Karten (zwei Antworten in einer Karte) und für quadratische Kästchen in `lernKoordinaten` mit Graphen.
- Muster für die Weg-Aufgaben ohne Bau (Platz 0) sind benannt (R2, R6, A6, „nächster Strich“), aber noch nicht als eigener Stapel ausgearbeitet.

**Nicht geprüft**
- Datenbank (Stand der Aufgaben, Versuche der Kinder).
- Die 20 Aufgaben mit `tools/inhalt_pruefen.py` (kennt `punkte` nicht).
- Entwurf nur im Programm-Browser (360/820/1280 px, hell/dunkel, alle 20 Aufgaben durchgespielt), nicht mit echtem Finger.
- Lehrplan-Passung von K7 (Lot auf schräge Gerade) und K9 (schräges Quadrat) als Stufe 3 in Klasse 5.

**Annahmen**
- Alle „häufigsten falschen Antworten“ (keine Versuchsdaten).
- Kartenbreite am Handy etwa 300 px → 23 px je Kästchen bei 10 Rasterschritten.
- Kein Council-Vorgang nötig für Ablage-Dateien im eigenen Ordner.

**Hinweis:** `inhalte/AUFTRAEGE.md` auf `lernen-app` enthält den Vornamen des Nutzers (181 Stellen), der alte Commit 39545b4 auf `mathe-profi` einmal im Postfach. Das Repo ist laut `inhalte/rollen/README.md` öffentlich. Nicht meine Datei – nur gemeldet.

## 2026-11-25 (Adelaide) – FERTIG: Ideen-Sammlung
Geliefert: `inhalte/mathe-profi/ideen.md` – 22 Ideen in vier Gruppen (7 Aufgabenformen, 8 Aufgabenarten, 4 Rückmeldungs-Ideen, 3 Motivation/Lehrer), je mit Beispiel, Lerngewinn, Prüfregel und Aufwand; Übersichtstabelle, Umsetzungs-Reihenfolge (Meinung), verworfene Ideen, 4 Fragen zur Besprechung.
Offen: Besprechung mit dem Nutzer, was umgesetzt wird. Nichts beauftragt.
Nicht geprüft: Ausgearbeitet mit Datensätzen sind nur F1–F5 (`auftrag1.md` D). Die übrigen Ideen haben nur je ein Beispiel; deren Lösungen sind per Programm nachgerechnet (Mach 100, Zahlen-Steckbrief, Wertetabelle, Rundungsbereich), Prüfregeln aber nicht in Code umgesetzt.
Korrektur: Das Chat-Beispiel „3, 5, 7, 8 → 100“ vom 24.11. hat keine Lösung; ersetzt durch 3, 4, 5, 8.

## 2026-11-24 19:30 (Adelaide) – FERTIG: Auftrag 1
Geliefert unter `inhalte/mathe-profi/` (Zweig `mathe-profi`, von `lernen-app` 8b0b83b2):
- `auftrag1.md`: Liste der heutigen Antwortformen (zahl, auswahl, luecken, markierung, text; nur 10,7 % der Aufgaben mit Bild, in keinem kann das Kind etwas tun) · Bewertung A von Kl. 5 „Rechengesetze“ (Rom, 548 Bordkarten) und Kl. 8 „Lineare Funktionen“ (445) · 4 Erklärungen (B) · 12 Aufgaben (C), davon 8 ohne reines Zahl-Tippen · 5 neue Aufgabenformen (D) mit Beispiel-Datensätzen und Prüfregeln: markieren, schieber, punkte, zuordnung, reihenfolge · Top 3 Änderungen.
- `nachrechnen.py`: alle Lösungen zweifach nachgerechnet (Lauf „OK“); erzeugt beim Lauf `aufgaben-auftrag1.json` mit den 12 Datensätzen.
- `entwurf-formen.html`: alle 5 Formen zum Anklicken, nur Antippen, getestet bei 360 und 820 px.
- `rolle.md`.

Wichtigste Befunde: (1) „Geschickt rechnen“ wird in Rom nur über das Ergebnis geprüft (79 Zahl-Aufgaben). (2) In „Lineare Funktionen“ zeichnet das Kind nie eine Gerade. (3) 19 von 46 Lage-Aufgaben sind derselbe Vierer – Raten lohnt.

Offen / App-Wunsch: neue Antworttypen D1–D5 brauchen Server (`schule.antwort_bewerten`), `lernAufgabe`/`lernAntwortText`, `tools/inhalt_pruefen.py` (TYPEN), `v_y` der Expeditionen. Empfohlene Reihenfolge: D1, D2, D3, D4, D5.
Nicht geprüft: Datenbank-Stand (nach Teilung), `inhalt_pruefen.py` für die neuen Aufgaben, Lehrplan-Zuordnung der Geradenscharen; „häufigste falsche Antwort“ ist Annahme, nicht aus Versuchsdaten.
