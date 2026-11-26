# Postfach mathe-profi

## 2026-11-26 05:15 (Berlin) – AUFTRAG 9 vom Projektleiter: Lehrplan nachbessern nach Gegenprüfung
Der Nutzer hat deinen Lehrplan angenommen (alle fünf Punkte, siehe `inhalte/plan/lehrplan-kinder-entscheidung.md`). ChatGPT hat gegen die Live-Tabellen `voraussetzung` und `voraussetzung_schulart` geprüft (Werkstatt-Nachricht 998): pädagogisch tragfähig, **aber noch keine Freigabe zum Einstellen**. Bitte nachbessern:

1. **Kind 2, `g7` braucht laut App zwingend `g2-teil2`.** Der steht außerhalb deiner Route und ist in der App offen, ohne „kann schon“; `plan.py` behandelt ihn als gekonnt. Entscheide fachlich: vorher einplanen oder begründet als gekonnt setzen.
2. **Kind 2, `ge3` (Winkel)** ist offen; die App empfiehlt Winkel für `ge4` und Spiegeln (`ge2`, bei dir Platz 17) für Konstruktion. Der Nutzer hat die Eingangsdiagnose (amtlicher Test Klasse 8) beschlossen. Lege fest, was bis zum Ergebnis gilt und was je Ergebnis geschieht, so dass ich ohne Rückfrage einstellen kann.
3. **Auslassungen stimmen bei drei Flügen nicht mit der App überein:** `ge9` (App: Determinanten ausgelassen, Plan: Vektoren), `f4` (App: quadratische Funktion ausgelassen, Plan: Transformation – „Parabeln“ muss im sichtbaren Inhalt ankommen), `a7` (App: allgemeine quadratische Gleichung ausgelassen, Liste nennt bedingt die reinquadratische, Route zählt beide). Lege je Flug ausdrücklich fest, welche Themen drin sind.
4. **Vollständige Soll-Liste je Kind statt Änderungsliste:** Die Plan-Funktion der App ersetzt die ganze normale Route; weggelassene Einträge werden entfernt, und bei `z6`, `g3`, `d1`, `d3`, `r7`, `g4` von Kind 2 würden gesetzte Wiederholungen zurückgenommen. Liefere je Kind die vollständige Liste aller Einträge, die nach dem Einstellen in der Route stehen sollen, mit Art (normal / Kür / kann schon / kann – wiederholen) und ausgelassenen Themen.
5. Prüfe die Route gegen die Tabellen `voraussetzung` und `voraussetzung_schulart` der App (lesend), nicht nur aus eigener Kenntnis, und lass `plan.py` das mitprüfen.
6. „Kür“ und „Klasse 9 erst nach Abschluss Klasse 8“ kann die Plan-Funktion nicht als Feld setzen. Schlage vor, wie das mit den vorhandenen Mitteln abgebildet wird (z. B. Abschnitt 5 erst später einstellen).

Ablage wie bisher unter `inhalte/mathe-profi/lehrplan-kinder/`, Meldung hier. Kein Einstellen. Danach mache ich den Probelauf mit Rollback.


## 2026-11-26 04:15 (Berlin) – AUFTRAG 8 vom Projektleiter: individueller Lehrplan für beide Kinder – **vor Auftrag 7**
Der Lehrer ist derzeit nicht erreichbar. Der Nutzer will für beide Kinder einen sinnvollen Lehrplan und überlässt dir die Gestaltung: „Wie der individuelle Lehrplan bezüglich Klassen aussieht, bin ich flexibel. Er soll ihn so gestalten, dass es sinnvoll ist.“ Der Projektleiter stellt den Plan danach in der App ein (erst nach Gegenprüfung und ausdrücklichem Satz des Nutzers).

**Vorgaben des Nutzers**
- Kind 1 ist in Klasse 5. Kind 2 ist in Klasse 8 und hat eventuell noch Stoff aus Klasse 7 nachzuholen.
- **Beide lernen den Stoff aller drei Schulen:** Gymnasium, Realschule (Wahlpflichtfächergruppe I), IB. Frühere Festlegungen dazu gelten weiter: Gymnasium ist die Basis; hat die Realschule ein Thema früher, kommt es früher; IB läuft nebenbei, sinnvoll verteilt; nach Klasse 8 sollen die Kinder den Stand aller drei haben. Zielschule offen.
- Keine Zeitvorgaben in Wochen: Auf Reisen wird manche Woche viel, manche gar nicht gelernt. Jahrgang ist Maßstab für Schwierigkeit und Mindeststand, nicht Fahrplan; Vorgriff ist erlaubt.
- Kind 2 hat mit dem Lehrer zuletzt in dieser Reihenfolge gearbeitet: Terme vereinfachen, binomische Formeln, Bruchterme, Textgleichungen. Die Anfangs-Flüge der Klasse 5 holt Kind 2 nicht nach.
- Der Nutzer will den Überblick: wie viele Flüge und Etappen je Schuljahr offen sind (Kind 1: aktuelles Jahr und eines weiter; Kind 2: vor allem Klasse 8, dazu 7 und 9).

**Was du lieferst**
1. **Je Kind eine geordnete Route** (Flüge in Reihenfolge, mit Themen-Kürzel aus `themenliste.json`), gegliedert in Abschnitte von je vier bis sechs Flügen. Je Flug: warum an dieser Stelle (Voraussetzung, Regel, Lücke), welche Schulart ihn verlangt, Pflicht oder Kür.
2. **Kind 2, Klasse 7:** Was davon ist echte Lücke und kommt vor den Klasse-8-Stoff, was läuft als „kann er – wiederholen“ nebenher, was kann warten? Nutze den Stand in der App (lesend) – im Repo nur das Ergebnis der Einordnung, keine Quoten.
3. **Grundsatz der Reihenfolge**, begründet: am Stück durch ein Gebiet oder im Wechsel? Bedenke Voraussetzungen (was baut aufeinander auf), die 15 Grundregeln (Regel an Zahlen vor Regel mit x; wo liegt die Brücke), Abwechslung zwischen Rechnen und Geometrie/Daten, und dass Wiederholungen schon mitlaufen.
4. **Kreuzungen beider Kinder:** Stellen, an denen beide dieselbe Regel in verschiedenem Gewand haben – für die gemeinsame Tischzeit.
5. **Prüfpunkte:** nach welchem Abschnitt ein Papier-Test sinnvoll ist (Blatt B aus Auftrag 5 einplanen).
6. **Umfang ehrlich:** Zahl der Flüge und Etappen je Abschnitt und je Schuljahr; eine Einschätzung in Lerntagen statt Wochen, mit Annahme zur Menge je Lerntag.
7. **Eine Seite für den Nutzer** in einfacher Sprache: der Plan je Kind als Liste, drei Sätze Begründung, was er entscheiden muss.
8. **Einstell-Liste für den Projektleiter:** je Kind die Flüge mit Status (neu im Plan / bleibt / herausnehmen / „kann – wiederholen“), so dass ich sie ohne Rückfrage einstellen kann. Was sich gegenüber dem heutigen Plan ändert, eigens markiert.

**Zusammenhang mit Auftrag 7:** Die „laufenden Themen“ für die neuen Aufgaben sind danach die ersten zwei Flüge dieser Route je Kind. Deshalb zuerst Auftrag 8, dann 7.

**Regeln wie immer:** öffentliches Repo – keine Namen, keine Lerndaten, keine Ergebnisse. Lehrplan-Zuordnungen, an denen du zweifelst (der Nutzer misstraut vor allem den Realschul-Zuordnungen), nenne ausdrücklich. Ablage `inhalte/mathe-profi/lehrplan-kinder/`, Meldung hier mit „Nicht geprüft“ und „Annahmen“.


## 2026-11-26 04:05 (Berlin) – AUFTRAG 7 vom Projektleiter: Schritt 1 – neue Aufgaben ohne Bau
Der Nutzer hat deine Reihenfolge bestätigt (Stand `inhalte/plan/aufgabentypen-auswahl.md`, Abschnitt „Entscheidungen vom 26.11.“). `punkte` rückt auf Schritt 5; die Festlegung vom 25.11. ist aufgehoben. Der Schalter Tisch/Handy kommt in einfacher Form nach Schritt 3. Antworten auf deine drei offenen Fragen stehen in `inhalte/plan/bauplan-fundament.md` (Doppel-Karte als Feldart `wahl` im neuen Typ; Typ 21 ist eine Einstellung des vorhandenen Check-ins; Säulen mit abgeschnittener Achse gibt es schon).

**Auftrag: Inhalt für Schritt 1, nur mit den heutigen Antwortformen (`zahl`, `auswahl`, `luecken`).**
1. Für **zwei laufende Themen je Kind** (nach den Versuchsdaten, nur Summen, nichts davon ins Repo): je Thema 12 bis 16 neue Aufgaben, verteilt auf
   - Typ 4 Lückenweg (mit Abbau der Hilfe von hinten),
   - Typ 14 Zwei Wege vergleichen (Antwort eine Zahl: „Welche Zahl in Weg B entspricht der 12 in Weg A?“),
   - Typ 17 Formel umkehren, wo das Thema eine Formel hat,
   - Typ 12 und 13 in einfacher Form,
   - **Brücken-Aufgaben „Zahl, aber nicht ausrechnen“** (Zwillingszeilen), wo das Thema eine Regel in neuem Gewand bringt.
2. **Jede Aufgabe trägt:** die Grundregel (Nummer und Name aus `denkpapier-grundregeln.md`), und je falscher Antwort das Fehlbild mit Regel. Das ist die Grundlage für „Hier hat die Minusklammer geklemmt“ und für die Regel-Übersicht.
3. Format wie in `inhalte/README.md`; Lauf mit `tools/inhalt_pruefen.py`; jede Aufgabe auf zwei Wegen nachgerechnet, Skript dazu. Tipps verraten nicht die Formel.
4. Schlage vor, **wo im Thema** die neuen Aufgaben stehen (welche Etappe, welche Stufe) und ob sie für „gelandet“ zählen (deine Zählregel: Typ 4 mit voller Hilfe zählt nicht).
5. Wenn ein Feld für Regel und Fehlbild im Aufgabenformat fehlt: nicht erfinden, sondern den Bedarf nennen – ich kläre den Bau.

**Nicht Teil des Auftrags:** Einspielen. Das geschieht erst nach Gegenprüfung durch ChatGPT und einem ausdrücklichen Satz des Nutzers.
Ablage: `inhalte/mathe-profi/schritt1/` auf deinem Zweig, Meldung hier mit „Nicht geprüft“ und „Annahmen“. Auftrag 5 (Papier-Test) wartet weiter auf das Startwort des Nutzers.


## 2026-11-25 12:20 (Berlin) – AUFTRAG 6 vom Projektleiter: Gegenprüfung der Auswahl des Nutzers
Der Nutzer hat 20 von 21 Aufgabentypen gewählt („Schritt antippen“ zurückgestellt) und eine eigene Idee ergänzt: Schalter „am Tisch / nur Handy“. Alles steht in `inhalte/plan/aufgabentypen-auswahl.md` (Zweig `lernen-app`).

Bitte:
1. Beantworte die sechs Fragen am Ende der Datei, kurz, mit [G]/[A]/[M].
2. Greife meinen Paket-Vorschlag A–F an: Reihenfolge, Zuschnitt, vergessene Abhängigkeiten.
3. Für Paket A: Bestätige, dass deine Prüfregel (`pruefe` in `massstab_probe.py`) die Typen 6, 7, 8, 9 und 15 trägt, oder nenne, was fehlt. Schlage je Typ zwei Musteraufgaben für Klasse 5 und zwei für Klasse 8 vor, nachgerechnet.
4. Für Typ 3 „Rechenweg zusammenbauen“: eine Prüfregel und drei Musteraufgaben, die nicht durch Wiedererkennen lösbar sind.

Ablage: `inhalte/mathe-profi/gegenpruefung-auswahl.md` auf deinem Zweig, Rückmeldung hier. Kein Bau. Auftrag 5 (Papier-Test) bleibt bestehen und startet erst, wenn der Nutzer es sagt.


## 2026-11-25 11:25 (Berlin) – AUFTRAG 5 vom Projektleiter (Fassung 2): zugeschnittener Papier-Test für beide Kinder
Fassung 1 von 11:20 ist ersetzt. Entscheidung des Nutzers: Der Test muss zu dem passen, was die Kinder zuletzt in der App gelernt haben, und darf 40 Minuten dauern. Der amtliche Test entfällt vorerst. Kein Bau, keine Einspielung.

**Frage, die der Test beantworten soll:** Kann das Kind das, was es in der App geübt hat, auch auf Papier, in Zeit und ohne Tipp – und wie groß ist der Abstand zwischen „wie in der App“ und „umgedreht, begründet, selbst angesetzt“?

**Für jedes Kind ein eigenes Blatt (Kind 1 Klasse 5, Kind 2 Klasse 8)**
1. **Stoff:** nur Themen, die das Kind in den letzten Wochen in der App bearbeitet hat. Lies dazu die Versuchsdaten (nur Summen je Thema, keine Namen, nichts davon ins Repo). Nenne im Schema die Themen-Kürzel, nicht die Quoten.
2. **Umfang:** 40 Minuten, ohne Tipp, ohne Taschenrechner und Formelsammlung, Geodreieck und Zirkel erlaubt. Rund 20 Punkte, Rechenweg wird verlangt und bewertet.
3. **Aufbau, je zur Hälfte der Punkte:**
   - Teil 1 „wie in der App“: Aufgaben in der Art, die das Kind geübt hat, aber mit Rechenweg auf Papier.
   - Teil 2 „weiter“: zum selben Stoff Umkehren, Begründen, Ansatz aus Text aufstellen, Fehler finden und berichtigen, Verfahren wählen. Dazu mindestens eine Aufgabe, die zwei der Themen mischt.
4. Eigene Aufgaben, nichts wörtlich aus Schulbüchern oder Tests. Zahlen so, dass man die Lösung nicht errät. Für Kind 1 Sprache und Länge der Texte an Klasse 5 anpassen; prüfe selbst, ob 40 Minuten für Klasse 5 tragen, und sag es, wenn nicht.
5. **Bewertungsschema** für einen Erwachsenen ohne Mathe-Ausbildung: Punkte je Teilaufgabe, was als richtig gilt, Folgefehler, höchstens 20 Minuten Aufwand. Je Teilaufgabe eine Zeile „Wenn falsch, dann vermutlich Regel …“.
6. **Erfassungsbogen:** Teilaufgabe, Punkte, Teil 1 oder 2, Tätigkeits-Gruppe, Rechenweg sichtbar ja/nein, vermutete Regel.
7. **Zwilling:** Baue zu jedem Blatt gleich ein zweites, gleich schweres Blatt B (gleiche Muster, andere Zahlen und Kontexte) für die Wiederholung in vier bis sechs Wochen. Blatt B bleibt bis dahin ungesehen.
8. Druckfertig: Blatt, Schema und Bogen je als eigene Seiten (HTML oder Markdown, das sauber als PDF druckt). Jede Aufgabe auf zwei Wegen nachgerechnet, Skript dazu.

**Ablage:** `inhalte/mathe-profi/papier-test-1/` auf deinem Zweig. Rückmeldung hier im Postfach, mit „Nicht geprüft“ und „Annahmen“.
**Regeln wie immer:** öffentliches Repo – keine Namen, keine Lerndaten, keine Ergebnisse der Kinder. Ergebnisse gehen nur direkt an den Nutzer.
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
