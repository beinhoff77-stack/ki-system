# Postfach mathe-profi

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


## 2026-11-26 (Berlin) – FERTIG: Auftrag 6 (Gegenprüfung der Auswahl)
Zweig `mathe-profi`, auf Stand `lernen-app` b2e51cd0 gebracht. Abgelegt mit Commit c82d6f19.

**Geliefert** unter `inhalte/mathe-profi/`:
- `gegenpruefung-auswahl.md` – sechs Fragen, Angriff auf Pakete A–F mit Gegenvorschlag, Prüfregel für Paket A mit 20 Musteraufgaben, Typ 3 mit Prüfregel und drei Musteraufgaben.
- `gegenpruefung_probe.py` – `pruefe2` (Erweiterung von `pruefe`), `pruefe_weg` (Typ 3), alle 23 Aufgaben mit guten und schlechten Antworten. Lauf „OK“.

**Kernaussagen**
1. **Widerspruch zur Entscheidung des Nutzers vom 25.11.:** Dort war `punkte` Bau 1 und Mehrfach-Auswahl Bau 2. Der Paket-Vorschlag stellt `punkte` ans Ende (F) und nennt die Mehrfach-Auswahl nicht. Bitte dem Nutzer vorlegen.
2. **Drei Bausteine fehlen im Plan:** Term-Rechner am Server (gebraucht von 6, 7, 8, 15, 10, 12, 3, 2, 11), zwei Antworten in einer Karte (12, 13, 15, 19 – meine Frage aus Auftrag 2 dazu ist offen), Mehrfach-Auswahl (9, 16).
3. **Paket A ist nicht „klein“:** Bedingungen müssen als Daten in der Aufgabe stehen, nicht als Programm. `pruefe` trägt 6, 7, 8 unverändert; 15 braucht die Feldart Wahl, 9 die Feldart Menge mit Grundmenge und Obergrenze. Typ 9 gehört zu 16, nicht zu A.
4. **Typ 3:** Falsche Karten reichen nicht. Regel: je Stufe eine Karte, jede Karte mit Lücke, jede Karte kann richtig oder falsch werden, Gleichwertigkeit wird gerechnet, mindestens zwei Wege.
5. **Reihenfolge (Meinung):** Papier-Test · Typen ohne Bau (4, 14, 17, einfache 12/13) · Fundament (Term-Rechner, Doppel-Karte) · 6, 7, 8, 15 · Typ 2 · `punkte` mit 18, 19 · Mehrfach-Auswahl mit 9, 16 · 10, 3, Schalter 1 · 11, 20, 21.
6. **Typ 1:** Handy-Modus ersetzt das Heft bei mehrschrittigen Rechnungen nicht. Der Nutzer hat am 26.11. drei Tisch-Sitzungen je Woche festgelegt (Stand 817e917f; mein Vorschlag „zwei“ ist überholt). Zusatz von mir: „gelandet“ bei Rechenweg-Etappen nur mit einem bestandenen Heft-Beleg; offen ist die Regel für Wochen ohne Tisch.

**Offen**
- Entscheidung des Nutzers zu Punkt 1.
- Antwort des Projektleiters: Aufwand „zwei Antworten in einer Karte“; ob Typ 21 die vorhandene Wiederholung ersetzt oder ergänzt; ob Diagramme erzeugt werden können.
- Auftrag 5 (Papier-Test) ist fertig abgelegt und wartet auf das Startwort des Nutzers.

**Nicht geprüft:** Lehrplan-Stellen für Variable, Mittelwert, Median in Klasse 5; Bedienung am Handy; Bau-Aufwand nur aus den mir bekannten Teilen des Codes beurteilt; Musteraufgaben nicht mit `tools/inhalt_pruefen.py`.
**Annahmen:** „naheliegend falsche“ Zahlen aus Fehlbildern, nicht aus Versuchsdaten.

## 2026-11-25 12:20 (Berlin) – AUFTRAG 6 vom Projektleiter: Gegenprüfung der Auswahl des Nutzers
Der Nutzer hat 20 von 21 Aufgabentypen gewählt („Schritt antippen“ zurückgestellt) und eine eigene Idee ergänzt: Schalter „am Tisch / nur Handy“. Alles steht in `inhalte/plan/aufgabentypen-auswahl.md` (Zweig `lernen-app`).

Bitte:
1. Beantworte die sechs Fragen am Ende der Datei, kurz, mit [G]/[A]/[M].
2. Greife meinen Paket-Vorschlag A–F an: Reihenfolge, Zuschnitt, vergessene Abhängigkeiten.
3. Für Paket A: Bestätige, dass deine Prüfregel (`pruefe` in `massstab_probe.py`) die Typen 6, 7, 8, 9 und 15 trägt, oder nenne, was fehlt. Schlage je Typ zwei Musteraufgaben für Klasse 5 und zwei für Klasse 8 vor, nachgerechnet.
4. Für Typ 3 „Rechenweg zusammenbauen“: eine Prüfregel und drei Musteraufgaben, die nicht durch Wiedererkennen lösbar sind.

Ablage: `inhalte/mathe-profi/gegenpruefung-auswahl.md` auf deinem Zweig, Rückmeldung hier. Kein Bau. Auftrag 5 (Papier-Test) bleibt bestehen und startet erst, wenn der Nutzer es sagt.


## 2026-11-25 (Berlin) – FERTIG: Auftrag 5, Fassung 2 (Papier-Test 1 für beide Kinder)
Zweig `mathe-profi`, auf Stand `lernen-app` 2ff0ffe2 gebracht. Abgelegt mit Commit ce33a3d5.

**Geliefert** unter `inhalte/mathe-profi/papier-test-1/`:
- `k5-blatt-a.html`, `k5-blatt-b.html`, `k8-blatt-a.html`, `k8-blatt-b.html` – je Datei: Blatt (Seiten 1–2), Bewertungsschema (3–4), Erfassungsbogen (5). Druckt als A4 auf fünf Seiten (geprüft als PDF).
- `bauen.py` – rechnet jede Aufgabe auf zwei Wegen nach, prüft Zwilling (gleiche Muster, Punkte, Tätigkeit; andere Zahlen) und schreibt die vier Dateien. Lauf „OK“.
- `README.md` – Stoff, Aufbau, Durchführung, Druckhinweis.

**Zuschnitt**
- Klasse 5: `zahlen.ganz`, `zahlen.rechengesetze`, `zahlen.natuerlich` (nur Runden). 13 Teilaufgaben, 20 Punkte.
- Klasse 8: `terme.umformen`, `gleichungen.linear`, `terme.bruchterme`, `gleichungen.bruch`, `terme.potenzgesetze_ganzzahlig`. 11 Teilaufgaben, 20 Punkte.
- Je 10 Punkte Teil 1 (Rechnen mit Rechenweg) und Teil 2 (Umkehren, Fehler finden, Begründen, Ansatz aus Text, Verfahren wählen). Themen-Mischung: Klasse 5 Aufgabe 8, Klasse 8 Aufgabe 9.
- Schema: Lösung, Punktevergabe, Folgefehler-Regel, je Teilaufgabe „Wenn falsch, dann vermutlich Regel …“. Für Nutzer oder Lehrer gleich nutzbar.

**40 Minuten für Klasse 5:** nach meiner Einschätzung tragfähig, aber knapp (im Mittel drei Minuten je Teilaufgabe). Nicht verlängern; der Bogen erfasst, bis wohin das Kind kam.

**Offen**
- Wer bewertet (Nutzer oder Lehrer).
- Blatt B liegt im öffentlichen Repo. Wer es vor der Wiederholung nicht sehen soll, darf den Ordner nicht öffnen; sonst Blatt B erst später ablegen (Entscheidung Projektleiter).

**Nicht geprüft**
- Bearbeitungszeit: nicht mit einem Kind gemessen.
- Ob die Aufgaben von Teil 1 den zuletzt gesehenen App-Aufgaben in der Schwierigkeit genau entsprechen – abgeglichen mit den Etappen-Regeln der Themen, nicht mit einzelnen Aufgaben.
- Ausdruck auf Papier (nur PDF am Bildschirm, Chrome).
- Schema nicht von einer fachfremden Person erprobt.

**Annahmen**
- Je Klasse lernt genau ein Kind; die Summen je Thema habe ich je Klasse gelesen.
- Themen mit nur einzelnen Versuchen gelten als „nicht gelernt“ und fehlen im Test.
- Alle „typischen Fehler“ im Schema sind Vermutungen aus den Fehlbildern, nicht aus Versuchsdaten.
- Versuchsdaten gesichtet; nichts davon steht im Repo.

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

## 2026-11-25 (Berlin) – FERTIG: Nachtrag Denkaufträge 3 und 4 (nach Lektüre der Recherche-Berichte)
Zweig `mathe-profi`, auf Stand `lernen-app` e8a373f gebracht. Abgelegt mit Commit b9271b7a.

**Geliefert** unter `inhalte/mathe-profi/`:
- `denkpapier-massstab.md` – neuer Abschnitt „Nachtrag“ am Ende (jetzt fünf Seiten bei 10 pt).
- `denkpapier-methoden.md` – neuer Abschnitt „Nachtrag“ am Ende (jetzt fünf Seiten).
- `recherche_stichprobe.py` – Erfolgsquoten 2023–2025 nach meiner Zuordnung, zwölf Helfer-Beispiele nachgerechnet, Kästchengröße im Gitter. Lauf „OK“.

**Kernaussagen**
- Erfolgsquoten je Teilaufgabe aus `tief-5` ergeben genau die Gesamtquoten der drei Jahre. Über drei Jahre: nur Regeln 54 %, mit Geometrie-Formel 43 %, Übertragen 33 %, Begründen 37 % (Geometrie 34 %). Meine 16 % für Übertragen galten nur für 2025 – berichtigt.
- Vier-Wochen-Fassung: erste und letzte Papier-Runde des älteren Kindes als ganzer amtlicher Test (Eich-Plan `tief-5`, 7a).
- „Erst knobeln“ für das jüngere Kind gestrichen (`tief-8`).
- Stichprobe aus Stufe 3 in zwei Bauarten geteilt: Heft-Beleg (nur nach richtiger Lösung, Aufgabe verdeckt) und Fehlersuche (nur nach falscher Lösung).
- Neue Zwischenstufe: nach falscher Lösung Zeilen eintippen, Prüfer „erste falsche Zeile“ (`tief-4`).
- „Verfahren wählen“ rückt in meine Top fünf.

**Zweifel an Helfer-Befunden**
- `tief-8` „Schritt-Systeme 0,76 gegen 0,31 als wichtigster Befund“ – steht gegen die in `tief-7` berichtete Studie mit schrittweiser Eingabe ohne inhaltliche Rückmeldung (nie besser, im Behaltenstest schlechter).
- `tief-10` „34 px je Kästchen“ – im vorhandenen Bild 26 Einheiten, am Handy 23 px.
- `tief-10` Umfang der Erklärung (10–18 Eingaben) – Belege großteils nicht aus der Altersgruppe (meine Annahme).
- `tief-7` Kontrollzahl als Auswahl aus vier Werten – zeigt die falschen Werte und lässt raten.
- `tief-3` „15–30 Stunden Etikettieren“ – Schätzung ohne Probe.
- `tief-12` Rangliste gewichtet Reiz höher als Nutzen für den Maßstab; „Welche passt nicht?“ ist nicht prüfbar.
- Die Prüfskripte der Helfer liegen nicht im Repo.

**Offen:** Volltext von Denkauftrag 4 ab Frage 6. Entscheidungen des Nutzers zu den übrigen Methoden.
**Nicht geprüft:** Quellen der Berichte nicht an der Quelle nachgeschlagen; Berichte nur in den Kernteilen gelesen, nicht jede Zeile; `sucher-a` bis `-d`, `tief-1`, `-9`, `-11` nicht gelesen; von den 61 Mustern nur Übersicht, Bau-Formate und Rangliste.
**Annahmen:** Die Quoten in `tief-5` sind richtig abgelesen (gestützt durch die passenden Gesamtquoten, nicht durch eigenen Blick in die Berichte).

## 2026-11-25 10:41 (Berlin) – FERTIG: Denkpapier Methoden (Denkauftrag 4) – Auftragstext kam abgeschnitten an
Zweig `mathe-profi`, Stand `lernen-app` dc9673c. Abgelegt mit Commit 07d72328.

**Vorbehalt:** Der Text von Denkauftrag 4 endet bei mir mitten in Frage 6 („Reihenfolge innerhalb eines Themas: Ansatz, d“). Weitere Fragen und die Angaben zur Lieferung fehlen. Ich habe Frage 6 nach meiner Lesart beantwortet, Dateiname und Umfang wie bei Denkauftrag 3 gewählt. Bitte den Rest nachreichen, ich ergänze.

**Geliefert** unter `inhalte/mathe-profi/`:
- `denkpapier-methoden.md` – vier Seiten (A4 bei 10 pt), Fragen 1–6, gesichert / Annahme / Meinung getrennt.
- `methoden_probe.py` – Rechnungen zu den drei Stufen (Gleichungssystem, Term Klasse 5, Geradengleichung Klasse 8), Referenz der Stichprobe „gleichwertige Zeile“. Lauf „OK“.

**Kernaussagen**
1. Die drei Stufen tragen für Verfahren mit mindestens drei Zeilen und einer **Wegmarke, an der jeder richtige Weg vorbeikommt** (beim Gleichungssystem: Gleichung mit einer Unbekannten – alle drei Verfahren kommen dort vorbei). Sie brechen bei Begriffen, Begründen, Konstruieren, offenen Sachaufgaben und Einzeilern.
2. Einwände: „I − II“ ist nicht falsch, nur nutzlos – „ungeschickt“ und „falsch“ trennen. Stufe 1 hat mit zweitem Versuch 2/3 Rate-Chance je Schritt. Die Stichprobe lässt sich fälschen (wer x = 4 hat, tippt 2 · x = 8) und kleine ganze Lösungen lassen sich erraten.
3. Vorschlag: **Stufe 3 zuerst** – eine Heft-Aufgabe als Einstieg; Stufe 1 und 2 nur für den Teil, an dem es hakt.
4. Zwei Themen ausgebaut, je Zeile mit typischen Fehlern und Regel: Klasse 5 „18 − 3 · (4 − 9)“ (drei Denkfehler liefern dasselbe Ergebnis 3 – die Stichprobe „Wert des Teilterms“ trennt sie); Klasse 8 „Gerade durch zwei Punkte“ (keine Stichprobe nötig, m und t sind die Wegmarken).
5. Wertvollste fünf: Ansatz aufstellen · Bedingung statt Musterlösung (Aufgabe erfinden, Datensatz bauen) · Fehler-Detektiv mit Berichtigen · zwei Wege vergleichen · Heft-Kette (späte Stichprobe, Foto, Schema). Überschätzt: „App rechnet“ (Scheinverständnis), Werkzeug nach jeder Zeile (Bedienlast), Balkenmodell in Klasse 8, „Welche passt nicht?“ mit eigenem Grund, neun Bildschirme Erklärung.
6. Abgleich mit meinen Papieren: das meiste doppelt; hier besser ist die Stichprobe (gleichwertige Zeile, Lösung zurückweisen, vor/nach) und die Vielfachen-Regel bei „Aufgabe erfinden“; neu und gut sind strukturierte Päckchen, ein Bild – viele Terme, Diagramm-Lügendetektor. Bei mir weiter: Fehlbild-Rechnung, Trennaufgaben, Vorgabe `punkte`, Bedingungs-Prüfung.
7. Es fehlen: Verfahren wählen, Sonderfälle, Probe als Pflichtzeile, Darstellung, Sachaufgabe bis zum Antwortsatz, Voraussetzungs-Check, Wiederholung über Wochen, Bedienlast, Rolle des Erwachsenen.
8. Reihenfolge im Thema: Einstiegstest · kleine Sachlage ohne Verfahren · Verfahren (Stufe 1, 2) · Heft · prüfen und vergleichen · Ansatz selbst · umkehren und erfinden · mischen. Der Ansatz kommt zweimal: klein am Anfang, ganz am Ende.

**Offen:** Rest des Auftragstexts; Befunde der vier Helfer aus Denkauftrag 3.

**Nicht geprüft:** die 61 Muster und 30 Reise-Aufgaben des Helfers (nur die genannte Spitze); der Bericht „Erklären“; Bedien-Aufwand; Bau-Aufwand der Kachel-Eingabe.

**Annahmen:** typische Fehler je Zeile (Fachwissen, keine Lerndaten); Selbstbewertung zu milde; Fehlerbeispiele erst nach erstem Können.

## 2026-11-25 09:11 (Berlin) – FERTIG: Denkpapier Maßstab (Denkauftrag 3 + Ergänzung, Fragen 1–14)
Zweig `mathe-profi`, Stand `lernen-app` dc9673c. Abgelegt mit Commit ead16b5b.

**Geliefert** unter `inhalte/mathe-profi/`:
- `denkpapier-massstab.md` – vier Seiten (A4 bei 10 pt; erlaubt waren sechs), 14 Fragen, gesichert / Annahme / Meinung / Helfer-Angabe getrennt.
- `massstab_probe.py` – eigene Zuordnung der 48 Teilaufgaben (63 BE) der Tests 2023–2025 nach Tätigkeit und Inhalt, Noten-Rechnung, Erfolgsquoten 2025; Referenz der Prüfregel für zehn offene Umkehr-Muster (45 Antworten, je 8 Unsinn-Eingaben); Stichprobe 3 × 20 Übungen. Lauf „OK“.

**Kernaussagen**
1. **Zuordnung:** nur die 15 Regeln 32 % der BE, Regel plus Geometrie-Formel 10 %, Übertragen/Umkehren 19 %, Begründen 24 % (9 von 15 BE in Geometrie), Zeichnen 6 %, Ablesen 6 %, Deuten 3 %. Inhalt: Zahlen/Algebra 37 %, Geometrie/Raum 33 %, Prozent/Verhältnis/Größen 17 %, Daten 13 %.
2. **Noten:** nur Regeln → 6 / 8 / 6 BE = Note 5 / 4 / 5; mit Formeln Note 4; mit Übertragen Note 2 / 3 / 2. Erfolgsquote 2025: Regel-Aufgaben 49 %, Übertragen 16 %, Begründen 42 %.
3. **Abweichung von den Helfern:** „49 % außerhalb“ überdehnt (10 % sind Regel plus Formel); Begründen größer (24 statt 19 %); „Regeln = Note 4“ nur mit Formeln und fehlerfrei.
4. **Sechs Stränge** neben den Regeln: Formel-Koffer, Übertragen/Umkehren, Begründen, Zeichnen/Konstruieren, Daten lesen, Sachansatz. Tabellenkalkulation ist kein eigener Strang (Rangfolge und Einsetzen).
5. **Offene Umkehraufgaben:** je fünf Muster Klasse 5 und 8 mit Bedingungs-Prüfung; kleiner Bau am Server, Eingabe mit `zahl`/`luecken`.
6. **Fehler-Katalog:** fünf Prüfungen vor Übernahme; sinnvoll 55–85 Einträge statt 114.
7. **Vier Wochen:** Papier-Runde je Woche, tägliche Fünf, Heft mit Stichprobe – mit Messgrößen.
8. **Erklärungen:** zwei vorhandene (Flächeneinheiten Klasse 5, Laplace Klasse 8) umgeschrieben; es fehlen Frage vorab, Gegensatz, zweite Richtung, Probe, Mini-Aufgabe.
9. **Üben:** „gelandet“ erst mit zweitem Tag; zwei Stufe-3-Aufgaben; bei Auswahl kein zweiter Versuch; Tipp in zwei Stufen.
10. **Formen-Rangliste:** Gitterpunkte, Bedingung statt Lösung, Mehrfach-Antippen, Papier mit Kontrollzahl, Term aufstellen, im Diagramm handeln, Balken beschriften.
11. **Qualität (60 Aufgaben):** Stufen, Vielfalt, Kontexte und Distraktoren gut; schwach sind Formen (95–100 % Zahl oder Auswahl), Tipps, die die Formel nennen (8 von 20 bei Kennwerten), 7 von 60 ohne Typ, nur ein Lösungsweg.

**Hinweis an den Projektleiter (Stichprobe „nichts wörtlich“):** Im Flug `daten.kennwerte`, Etappe `mittelwert`, fragt eine Stufe-3-Auswahl-Übung nach der richtigen Rechnung für den Mittelwert zweier Zahlen und benutzt dieselben zwei Zahlen wie eine Teilaufgabe des Tests 2025. Bitte prüfen und Zahlen ändern.

**Offen**
- Befunde der vier weiteren Helfer (Lernforschung, Motivation, Erklären, Bedienung) lagen nicht vor; ich ergänze, wenn sie kommen.
- Entscheidung: vier-Wochen-Fassung so starten? Papier-Runden würde ich als Nächstes schreiben.

**Nicht geprüft**
- Ergebnisberichte 2023 und 2024 (Abruf wurde nicht freigegeben, Nutzer war nicht erreichbar); Erfolgsquoten nur 2025, aus dem Diagramm gelesen, Summe stimmt mit dem Bericht.
- Arbeitszeit, Hilfsmittel, Anteil Ankreuzen; alle Helfer-Befunde außer KI-Tutor-Studie und Lernzentrum-Studie.
- Lehrplan-Passung der zehn Umkehr-Muster; Bau-Aufwand der Formen.

**Annahmen**
- Was andere Lehrwerke besser machen (eigene Kenntnis, nicht nachgeschlagen).
- Zuordnung einzelner Teilaufgaben an Grenzen (z. B. Prozent mit Bedeutungswechsel als „Übertragen“).

## 2026-11-25 08:11 (Berlin) – FERTIG: Denkpapier Grundregeln, Fassung 2 (Denkauftrag 2 + Ergänzung)
Zweig `mathe-profi`, Stand `lernen-app` dc9673c. Abgelegt mit Commit 26348b13. **Ersetzt die Fassung von 06:56** (die kannte nur die Ergänzung; der Vorbehalt dort ist damit erledigt).

**Geliefert** unter `inhalte/mathe-profi/`:
- `denkpapier-grundregeln.md` – vier Seiten (A4 bei 10 pt), Fragen 1–10 in einem Papier, gesichert / Annahme / Meinung getrennt, je ein durchgespieltes Beispiel Klasse 5 und Klasse 8.
- `grundregeln_probe.py` – rechnet alle Beispiele der Regel-Liste nach (Zahlen, x an Stichproben, Brüche), zählt die Regeln im Aufgabentext je Klasse und den Umfang der Flüge. Lauf „OK“.

**Antworten in Kürze**
1. **Liste:** 15 Regeln für Klasse 5–10, jede mit Kindernamen, einem Satz, ihrer Grenze („gilt nicht bei …“) und Beispielen mit Zahlen, x und Brüchen: Richtung, Zeichen-Paar, Rangfolge, Verteilen, Minusklammer, Tauschen und Bündeln, Waage, Umkehren, Einsetzen und Probe, Wert bleibt, Bruchrechnen, Potenz, Stellenwert, Verhältnis, Nullprodukt. Binomische Formeln, Lösungsformel, Dreisatz sind bewusst keine eigenen Regeln.
2. **Über Algebra hinaus:** voll bei Zahlen, Algebra, Geld; gut bei Funktionen; halb bei Geometrie, Raum, Daten (Rechnen ja, Sehen und Konstruieren nein); gar nicht bei Sachaufgaben und Begründen. Quer wirken Einsetzen und Probe, Umkehren, Verhältnis, Stellenwert, Zerlegen. Vorschlag: zwei Fächer – Regeln und Arbeitsweisen.
3. **Übertrag Zahl → Variable:** Der Schritt liegt nicht beim Buchstaben, sondern bei Abschluss, mehrfacher Unbekannter, Gleichheitszeichen und Kontrolle. Zeigen mit Zwillingszeilen (Zahlen nicht ausgerechnet), Wertetabelle, Rechteck, Zahlenprobe. Im Bestand fehlt die Brücke (Minus vor Klammer an Zahlen: 8 / 0 Aufgaben in Klasse 5 / 6).
4. **Fehlbilder ↔ Regeln:** 7 von 9 zeigen auf eine Regel, 2 davon als „richtige Regel am falschen Ort“. Übrig bleiben Bedeutungsfehler (Prozent wovon? Was ist das Ganze?). Buchung auf die Regel nur bei erkanntem Fehlbild.
5. **Sichtbar:** ja, sparsam – Koffer auf Abruf mit zwei Zuständen, keine Zahlen; Etikett an der Aufgabe erst sichtbar, dann Frage, dann weg.
6. **Rollendes System:** je Flug vom Ziel her – Papier-Runde, Regel-Etiketten, Fehlbilder, Trennaufgaben, Erklärungen, Einstieg „Das kennst du schon“, Prüftor. Vor dem Flug fertig: die ersten drei und das Prüftor. Auf Vorrat lohnt nur das Regel-Paket (einmal je Regel statt je Flug).
7. **Was fehlt:** Eingangscheck Werkzeuge, tägliche Fünf (gemischt, ohne Etikett), Strang Sachaufgaben, Musterlösung im Heft-Format, Eichung von außen zweimal im Jahr, Tischkarte für den Erwachsenen.
8.–10. wie in der ersten Fassung, gekürzt: Brücke „Zahl, aber nicht ausrechnen“; „fest genug“ nach sechs Merkmalen; älteres Kind erklärt nur als freiwilliges Angebot mit Gegenrolle.

**Offen:** Entscheidungen von Nutzer und Projektleiter – Liste so übernehmen? Sichtbarkeit? Regel-Paket als erster Auftrag?

**Nicht geprüft**
- LehrplanPLUS je Regel, besonders Klasse 9 und 10; Vollständigkeit der Liste.
- Aufwand je Flug (Schätzung, nicht gemessen).
- Die Textzählung erfasst Regeln im Rechenweg nicht.
- Ob die Bruch-Zeichen (½, ⅔) in der App sauber dargestellt würden – im Papier nur zur Kürze.

**Annahmen**
- Welche Fehler typisch sind; Anteil der Regel-Fehler (aus 9 Fehlbildern dreier Flüge hochgerechnet).
- „Fest ab Klasse“ nach dem Bestand, nicht nach dem Lehrplan.

## 2026-11-25 06:56 (Berlin) – FERTIG: Denkpapier Grundregeln
Zweig `mathe-profi`, vorher mit `lernen-app` dc9673c zusammengeführt. Abgelegt mit Commit 630836d4.

**Vorbehalt:** Der Text von Denkauftrag 2 (Fragen 1–7) hat den Mathe-Profi-Chat nicht erreicht – nur die Ergänzung mit den Fragen 8–10. Grundlage für den Rest ist der Protokoll-Eintrag „Grundregeln schweben über den Themen“ in `inhalte/AUFTRAEGE.md`. Falls die Fragen 1–7 anderes verlangen: bitte nachreichen, ich ergänze.

**Geliefert** unter `inhalte/mathe-profi/`:
- `denkpapier-grundregeln.md` – drei Seiten (A4 bei 10 pt), gesichert / Annahme / Meinung getrennt; eine Regel („Minus vor der Klammer“) durchgehend von Klasse 5 bis 8.
- `grundregeln_probe.py` – Zählung im Aufgabentext je Klasse und die Rechnungen der Brücke. Lauf „OK“.

**Kernaussagen**
1. Die Regeln sind dieselben; der Schritt liegt nicht beim Buchstaben (Klasse 5 rechnet im Flug „Einfache Gleichungen“ schon mit x). Er hat drei Teile: Am Ende bleibt ein Ausdruck stehen; die Unbekannte kommt mehrfach vor, Rückwärtsrechnen geht nicht mehr; „=“ heißt „gleich viel wert“. Dazu fällt das Nachrechnen weg, Ersatz ist die Zahlenprobe.
2. Brücke: „Zahl, aber nicht ausrechnen“, in sechs Stufen. Im Bestand fehlt sie: Minus vor Klammer an Zahlen 8 Aufgaben in Klasse 5, 0 in Klasse 6, dann 38 mit Buchstaben in Klasse 7; Faktor vor Klammer 14 / 0 / 128.
3. Korrektur am Beispielpaar: 9 − (−5) trägt das Vorzeichen; das Fundament der Minusklammer ist „eine Differenz abziehen“, 20 − (8 − 3).
4. 13 Grundregeln für Klasse 5 und 6, jede mit ihrer Grenze („gilt nicht bei …“). „Fest genug“ nach sechs Merkmalen (erster Versuch, gemischt, verteilt, Brückenform, ohne Regel-Fehlbild, auf Papier); der Stand kann wieder fallen.
5. Älteres Kind erklärt: als fester Baustein nein, als freiwilliges Angebot ja – Erklär-Karte an Zahlen, Gegenrolle „Zahlenprüfer“ für das jüngere Kind, Hinweis an den Erwachsenen für den passenden Moment.

**Mögliche Folgearbeit (Meinung, kein Auftrag):** Brücken-Aufgaben der Stufe 3 für Klasse 5 und 6 mit den vorhandenen Formen (Muster M2 und M3 aus `auftrag3.md`); Regel-Etikett am Aufgabenmuster im Generator.

**Offen:** Text von Denkauftrag 2; Entscheidung des Nutzers, ob Regeln für die Kinder sichtbar werden.

**Nicht geprüft**
- LehrplanPLUS je Regel; Vollständigkeit der Regel-Liste.
- Ob Klasse 6 im Unterricht die Klammerregeln an Brüchen übt.
- Die Zählung liest nur den Aufgabentext, nicht den Rechenweg.

**Annahmen**
- Welche Fehler typisch sind (Fachwissen, nicht aus Lerndaten).
- Zuordnung der Regeln zu Klassen nach dem Bestand.

## 2026-11-25 05:15 (Berlin) – FERTIG: Denkpapier Diagnose
Zweig `mathe-profi`, vorher mit `lernen-app` edb6b86 zusammengeführt (enthält d00cf04). Abgelegt mit Commit 5bedf8a.

**Geliefert** unter `inhalte/mathe-profi/`:
- `denkpapier-diagnose.md` – drei Seiten (A4 bei 10 pt), sechs Fragen, gesichert / Annahme / Meinung getrennt, je ein durchgespieltes Beispiel Klasse 5 und Klasse 8.
- `fehlbild_probe.py` – Nachweis zu Frage 1 an den vorhandenen Aufgaben (nur Inhalte). Lauf „OK“.

**Kernaussagen**
1. Fehlbilder (das Ergebnis, das ein bestimmter Denkfehler liefert) lassen sich je Muster mitberechnen: Ganze Zahlen ± 49 von 59 Aufgaben mit eindeutigem Fehlbild, Prozent 93 von 93. 69 % aller Aufgaben haben schon `c`; es fehlt eine Liste `fehlbilder` je Muster.
2. Ein Fehlbild ist noch keine Diagnose. Regel: dasselbe Fehlbild bei 2 von 3 Trennaufgaben.
3. Rückfrage „Wie hast du gerechnet?“ taugt nur als zweites Mittel. Besser: Kontrollzahlen (Zwischenergebnis nach der Rechnung im Heft abfragen, mit der vorhandenen Lücken-Form).
4. Erklär-Leiter in fünf Stufen; zurück zur Voraussetzung erst nach erneut 2 von 3 falschen Trennaufgaben, über einen Zeiger je Fehlbild auf eine Etappe.
5. Beste Formen für den Übertrag auf Papier: Lückenweg mit abnehmender Hilfe, Heft mit Punkteschema plus Kontrollzahlen, Papier-Runde in Zeit.
6. Dauer trennt „geraten“ von „versucht“ und „flüssig“ von „mühsam“, sagt aber nichts über Verstehen.
7. Zu optimistisch ist die These bei: Fehler = Denkfehler, „einfacher erklären“ ohne Boden, 80/89 % als Maßstab, Darstellung in Schulaufgaben, Rückmeldung der Kinder, zwei Kinder als Datenbasis.

**Vorgeschlagene Reihenfolge (Meinung):** Papier-Runde in Zeit · Fehlbilder mit Trennaufgaben für drei Flüge · Kontrollzahlen · Erklär-Leiter Stufen 0–2 · Dauer speichern.

**Offen:** Entscheidung von Nutzer und Projektleiter, ob und in welcher Reihenfolge daraus Aufträge werden.

**Nicht geprüft**
- Bayerische Korrekturpraxis und Punkteschemata; das neue Prüfmaterial im Repo.
- Vollständigkeit der Denkfehler-Listen.
- Die Probe zählt „eindeutig“ nur unter den aufgeschriebenen Denkfehlern.

**Annahmen**
- Welche Denkfehler typisch sind (Fachwissen, nicht aus Lerndaten).
- Abfall der Trefferquote auf Papier; milde Selbstbewertung; Grenzen der Handschrift-Auswertung ohne Netz.

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
