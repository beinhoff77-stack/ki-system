# Postfach aufloesen (Vierundzwanzigste Runde, 18.11.)

Neueste Meldung oben.

## 2026-11-18 – FERTIG: Realschul-/IB-Themen aufgelöst, fünf neue Karten, Dualsystem

Zweig `aufloesen` (von `lernen-app`, Commit 879fbf7). Ein Zielthema = ein Commit, alle gepusht. Kein Merge, keine Datenbank, kein App-Code, keine Tests.

### Kurz
- **24 Lernkarten umgezogen** (alle B- und C-Karten der 10 aufgelösten Themen) in **12 Zielthemen**; **33 A-Lernkarten entfallen**; `gleichungen.reinquadratisch` hat nur A-Karten, dort zieht nichts um.
- **6 neue Lernkarten** (Teil B): 5 aus `doppelt-rsib.md` Teil 3a und das Dualsystem.
- **Teil C:** `funktionen.quadratisch` – `umformen` und `extremwert` sind jetzt Wiederholungen des Flugs `terme.quadratische_extreme` (Kl. 8); 24 Übungen entfernt (Liste unten, bitte sperren).
- **Pflicht neu** nur in 4 Flügen: `zahlen.natuerlich` (dualsystem), `abbildungen.kongruenz` (gegenvektor), `funktionen.reihen` (3 Folgen-Karten), `abbildungen.matrizen` (abstand). Alles andere ist Vertiefung.
- **Prüfskript:** alle 17 geänderten Themen OK, 0 Gruppen „gleich gebaut hintereinander“; `--alle` (116 Dateien) OK. Jeder Generator baut seine Datei reproduzierbar (zweiter Lauf ohne Änderung).
- **Nachweis gegen `lernen-app` (Tatsache, per Skript):** In allen 17 Zielthemen steht jede alte Aufgabe Zeichen für Zeichen gleich darin – außer den 24 absichtlich entfernten in `funktionen.quadratisch`. Alte Lernkarten unverändert – außer `umformen`/`extremwert` (Titel, Einstieg). Die 11 aufgelösten Themendateien sind unverändert.

### Werkzeug
- `inhalte/generatoren/_aufloesen.py`: Abschnitt AUFLOESEN am Ende jedes Zielgenerators; nutzt die Bausteine der Einundzwanzigsten Runde (`_bereinigen.anwenden`: karte_her, karte_neu, neu, knobel, pool, karte, weg, ersetze, umschreiben). Quelle ist die Themendatei des aufgelösten Themas **ohne überzählige Übungen** (Übungen ohne `g` werden nicht übernommen). Prüft danach die Regeln der Zwanzigsten Runde je geänderter Karte, das Prüfskript und den Nachweis „alte Aufgaben gleich“.
- `_af_plan.py` (Schritte je Zielthema), `_af_neu.py` (die sechs neuen Karten; alle Lösungen werden beim Bauen nachgerechnet).

### Umzugstabelle (Teil A)
Klasse = `themenliste.json` des Zielthemas. Zahl = Aufgaben in der Zielkarte (Ü Übungen, K Knobel, Test/Korrektur/Sicherung).

| altes Thema / Lernkarte | Zielthema / Lernkarte (Stelle) | Pflicht/Vertiefung | Klasse | Aufgaben |
|---|---|---|---|---|
| `groessen.verhaeltnisse`/`kuerzen` | `bruch.brueche`/`verhaeltnis_kuerzen` (nach `kuerzen`) | Vertiefung | Gym 6 | 35 (23 Ü, 2 K, 1/3/6); 3 überzählige nicht übernommen |
| `groessen.verhaeltnisse`/`gleichwertig` | `bruch.brueche`/`gleichwertig` (nach `verhaeltnis_kuerzen`) | Vertiefung | Gym 6 | 32 (20 Ü, 2 K, 1/3/6); 7 überzählig |
| `groessen.verhaeltnisse`/`aenderung` | `groessen.proportional`/`aenderung` (nach `sach`) | Vertiefung | Gym 5 | 33 (21 Ü, 2 K, 1/3/6); 7 überzählig |
| `mengen.grundbegriffe`/`elemente` | `stochastik.verknuepft`/`elemente` (vor `verknuepfen`) | Vertiefung | Gym 9 | 36 (24 Ü, 2 K, 1/3/6); 2 überzählig |
| `mengen.grundbegriffe`/`schnitt` | `stochastik.verknuepft`/`schnitt` (nach `elemente`) | Vertiefung | Gym 9 | 38 (26 Ü, 2 K, 1/3/6) |
| `mengen.grundbegriffe`/`venn` | `stochastik.verknuepft`/`venn` (nach `additionssatz`) | Vertiefung | Gym 9 | 40 (28 Ü, 2 K, 1/3/6) |
| `mengen.grundbegriffe`/`verstehen` | `stochastik.verknuepft`/`mengen_verstehen` (nach `venn`) | Vertiefung | Gym 9 | 33 (21 Ü, 2 K, 1/3/6); 5 überzählig |
| `abbildungen.vektoren`/`gegenvektor` | `abbildungen.kongruenz`/`gegenvektor` (nach `verschiebung`) | **Pflicht** | Gym 7 (Plan 6) | 31 (19 Ü, 2 K, 1/3/6); 9 überzählig |
| `funktionen.scharen`/`einsetzen` | `funktionen.linear`/`einsetzen` (nach `lage`) | Vertiefung | Gym 8 | 35 (23 Ü, 2 K, 1/3/6); 4 überzählig |
| `funktionen.scharen`/`wirkung` | `funktionen.linear`/`wirkung` (nach `einsetzen`) | Vertiefung | Gym 8 | 35 (23 Ü, 2 K, 1/3/6); 1 überzählig |
| `funktionen.scharen`/`bueschel` | `funktionen.linear`/`bueschel` (nach `wirkung`) | Vertiefung | Gym 8 | 34 (22 Ü, 2 K, 1/3/6); 2 überzählig |
| `funktionen.scharen`/`loesung_parameter` | `gleichungen.lgs2`/`loesung_parameter` (nach `loesbarkeit`) | Vertiefung | Gym 8 | 33 (21 Ü, 2 K, 1/3/6); 4 überzählig |
| `funktionen.folgen`/`rekursiv` | `funktionen.reihen`/`rekursiv` (Anfang) | **Pflicht** (im freiwilligen Flug) | IB 5 | 36 (24 Ü, 2 K, 1/3/6) |
| `funktionen.folgen`/`arithmetisch` | `funktionen.reihen`/`arithmetisch` (nach `rekursiv`) | **Pflicht** (im freiwilligen Flug) | IB 5 | 34 (22 Ü, 2 K, 1/3/6); 2 überzählig |
| `funktionen.folgen`/`geometrisch` | `funktionen.reihen`/`geometrisch` (nach `arithmetisch`) | **Pflicht** (im freiwilligen Flug) | IB 5 | 34 (22 Ü, 2 K, 1/3/6); 1 überzählig |
| `finanzen.zinseszins`/`formel` | `bruch.prozent_grundwert`/`formel` (nach `mehrfach`) | Vertiefung | Gym 7 | 30 (18 Ü, 2 K, 1/3/6); 10 überzählig |
| `funktionen.transformation`/`spiegeln` | `funktionen.quadratisch`/`spiegeln` (nach `parameter`) | Vertiefung | Gym 9 | 34 (22 Ü, 2 K, 1/3/6); 2 überzählig |
| `funktionen.transformation`/`punkte` | `funktionen.exponential_log`/`punkte` (nach `graph`) | Vertiefung | Gym 10 | 33 (21 Ü, 2 K, 1/3/6); 3 überzählig |
| `funktionen.umkehr`/`umkehrbar` | `funktionen.potenz`/`umkehrbar` (nach `negativ`) | Vertiefung | Gym 9 | 34 (22 Ü, 2 K, 1/3/6); 2 überzählig |
| `funktionen.umkehr`/`linear` | `funktionen.potenz`/`linear` (nach `umkehrbar`) | Vertiefung | Gym 9 | 35 (23 Ü, 2 K, 1/3/6); 5 überzählig |
| `funktionen.umkehr`/`quadratisch` | `funktionen.potenz`/`quadratisch` (nach `wurzelfunktion`) | Vertiefung | Gym 9 | 32 (20 Ü, 2 K, 1/3/6); 3 überzählig |
| `funktionen.umkehr`/`spiegeln` | `funktionen.potenz`/`spiegeln` (nach `quadratisch`) | Vertiefung | Gym 9 | 31 (19 Ü, 2 K, 1/3/6); 7 überzählig |
| `stochastik.bedingt`/`unabhaengig` | `stochastik.mehrstufig`/`unabhaengig` (nach `ohne_zuruecklegen`) | Vertiefung | Gym 10 | 31 (19 Ü, 2 K, 1/3/6); 5 überzählig |
| `stochastik.bedingt`/`rueckschluss` | `stochastik.verknuepft`/`rueckschluss` (nach `bedingt`) | Vertiefung | Gym 9 | 35 (23 Ü, 2 K, 1/3/6) |

Neue Bereichstitel: `stochastik.verknuepft` „Mengen und Ereignisse verknüpfen“, `funktionen.reihen` „Folgen und Schreibweise“.

### Entfallene A-Lernkarten (33) mit Gym-Gegenstück (laut `doppelt-rsib.md` Teil 2)
- `groessen.verhaeltnisse`: `aufteilen` → `gleichungen.bruch`/verhaeltnis · `proportion` → `groessen.proportional`/sach · `einheitsrate` → `groessen.proportional`/einheit
- `mengen.grundbegriffe`: `vereinigung` → `stochastik.verknuepft`/vierfeld (Zählform in additionssatz)
- `abbildungen.vektoren`: `vektor_bestimmen`, `bildpunkt`, `addition` → `abbildungen.kongruenz`/verschiebung · `punkt_berechnen` → `geometrie.grundbegriffe`/vierecke · `eigenschaften` → `abbildungen.kongruenz`/eigenschaften
- `funktionen.scharen`: `parallelenschar` → `funktionen.linear`/aufstellen · `sachaufgabe` → `funktionen.linear`/deuten
- `funktionen.folgen`: `explizit` → `terme.aufstellen`/muster · `erkennen` → `funktionen.exponential_log`/linear_oder_exponentiell
- `finanzen.zinseszins`: `jahr` → `bruch.prozent_grundwert`/vermehrt · `faktor` → `bruch.prozent_grundwert`/mehrfach · `rueck` → `gleichungen.potenz`/sachaufgabe · `vergleich` → `gleichungen.exponential`/wachstum
- `gleichungen.reinquadratisch`: `schaetzen` → `zahlen.wurzeln_basis`/abschaetzen · `grundform`, `umformen`, `klammer` → `gleichungen.quadratisch`/reinquadratisch · `gerundet` → `gleichungen.potenz`/gerade · `sachaufgabe` → `zahlen.wurzeln_basis`/wurzel_sache
- `funktionen.transformation`: `nach_oben`, `nach_rechts`, `strecken` → `funktionen.quadratisch`/parameter · `kombiniert` → `funktionen.quadratisch`/scheitel
- `funktionen.umkehr`: `werte` → `funktionen.grundbegriffe`/stelle · `exp_log` → `funktionen.exponential_log`/logfunktion
- `stochastik.bedingt`: `tafel`, `formel`, `verstehen` → `stochastik.verknuepft`/bedingt · `baum` → `stochastik.mehrstufig`/ohne_zuruecklegen

Aufgaben aus A-Karten habe ich **nicht** in Gym-Karten verschoben (der Auftrag erlaubt es, verlangt es nicht; jede Gym-Karte erfüllt die Mindestmengen schon).

### Neue Lernkarten (Teil B)
| Zielthema / Lernkarte (Stelle) | Inhalt | Pflicht/Vertiefung | Klasse | Aufgaben |
|---|---|---|---|---|
| `zahlen.natuerlich`/`dualsystem` (nach `roemisch_system`) | Zahlen im Zweiersystem lesen und schreiben (ohne Potenzschreibweise, Umrechnen durch Abziehen der Stellenwerte) | **Pflicht** | Gym 5 | 30 (18 Ü, 2 K, 1/3/6) |
| `abbildungen.aehnlichkeit`/`bildgerade` (nach `streckung`) | Bildgerade und Bildparabel bei Streckung an O | Vertiefung | Gym 9 | 30 |
| `abbildungen.aehnlichkeit`/`schwerpunkt` (nach `bildgerade`) | Schwerpunkt eines Dreiecks mit Koordinaten, Teilung 2 : 1 | Vertiefung | Gym 9 | 30 |
| `trigo.rechtwinklig`/`schnittwinkel` (nach `anwendung`) | Steigungs- und Schnittwinkel zweier Geraden | Vertiefung | Gym 9 | 30 |
| `trigo.allgemein`/`additionstheoreme` (nach `einheitskreis`) | sin(α + β), cos(α + β); Werte aus 3-4-5- und 7-24-25-Dreiecken | Vertiefung | Gym 9 | 30 |
| `abbildungen.matrizen`/`abstand` (nach `skalarprodukt`) | Abstand Punkt–Gerade über den Lotfußpunkt ((P − F) · u = 0) | **Pflicht** im RS-Flug | RS 10 | 30 |

Je Karte: Stufe 1/2/3 = 4/6/8 Übungen mit 2/4/6 Typen (dualsystem 2/4/5; verlangt 2/3/4), 2 Knobel, Test 1, Korrektur 3, Sicherung 6. Alle Felder nach der Vorgabe vom 16.11. (einstieg, woerter, bild, schritte, fehler, regel).
Geprüft (Tatsache): jede Lösung beim Bauen nachgerechnet (c bzw. Lückenausdrücke); Lösungswege selbst gelesen; keine Buchstaben als Unbekannte vor ihrem Stoff (Dualsystem Kl. 5: keine; Potenzen dort vermieden); Antwortoptionen ohne falsche Rechnungen.

### Lesarten und Abweichungen (bitte prüfen)
1. **B-Karten als ganze Karten.** Der Auftrag sagt „B- und C-Lernkarten ziehen als Lernkarte …“. `doppelt-rsib.md` hatte für die meisten B-Karten nur „3–4 Aufgaben“ vorgeschlagen. Ich bin dem Auftrag gefolgt. Folge: deutlich mehr Stoff in den Gym-Flügen (alles Vertiefung außer gegenvektor).
2. **Pflicht nur bei „RS alle Zweige“** (so in `doppelt-rsib.md` vermerkt): nur `abbildungen.vektoren` → gegenvektor. `scharen` und `transformation` sind dort „RS Gruppe I (II/III ein Jahr später)“ → Vertiefung.
3. **gegenvektor (Pflicht) hängt an verschiebung (Vertiefung).** Das ist ein Widerspruch im Flug: Ein Gym-Kind muss die Rückweg-Karte lernen, die Grundkarte aber nicht. **Für den Nutzer:** entweder `verschiebung` (und `drehung`, RS M8) Pflicht machen oder gegenvektor Vertiefung. Meinung: verschiebung Pflicht, wenn der RS-Mindeststand gelten soll (Entscheidung 3 in `doppelt-rsib.md`).
4. **Dualsystem Pflicht für alle.** Der Gym-Lehrplan M5 1.1 nennt kein Zweiersystem (Tatsache, lehrplanplus.bayern.de, Gymnasium M5, Abruf 18.11.: nur Zehnersystem im Vergleich zum römischen System). Die App kennt Pflicht nur je Thema, nicht je Schulart. Da die Kinder den RS-Mindeststand mitlernen (Entscheidung 2: RS-alle-Zweige-Flüge sind Pflicht), habe ich Pflicht gesetzt. Für ein reines Gym-Kind wäre es Vertiefung → braucht eine Pflicht-Kennung je Schulart (App-Frage).
5. **funktionen.reihen:** die drei Folgen-Karten sind Pflicht **innerhalb** des Flugs (der ganze Flug ist freiwillig; arith/geom bauen darauf auf). Titel „Folgen und Reihen“ steht nur in `doppelt-rsib.md` – `themenliste.json` habe ich nicht geändert (Haupt-Chat).
6. **Stellen:** Mengen: elemente, schnitt vor `verknuepfen` (Einstieg), venn und mengen_verstehen nach `additionssatz` (dort ist ∪ aus verknuepfen bekannt). Umkehr: umkehrbar, linear vor `wurzelfunktion` (wie vorgeschlagen), quadratisch und spiegeln danach (das Beispiel braucht √x). rueckschluss nach `bedingt`.
7. **Vorwissen – geänderte umgezogene Aufgaben (alle mit gleichem Typ und gleicher Stufe):**
   - `bruch.brueche`: 40 %-Aufgabe ersetzt (Prozent erst später in Kl. 6); 4 Lösungswege ohne Gleichungen mit Buchstaben (lineare Gleichungen erst Kl. 7).
   - `groessen.proportional`: Prozentpunkte-Aufgabe und Ungleichung „r > 5“ ersetzt; 1 Knobel-Lösungsweg ohne Gleichung.
   - `abbildungen.kongruenz`: Knobel mit „2 · v = …“ ersetzt; Wort „Vektor“ ergänzt (führte nur die entfallene Karte ein).
   - `funktionen.potenz`: 6 Aufgaben mit 2ˣ/0,5ˣ/3ˣ ersetzt (Exponentialfunktionen erst Kl. 10), Beispiel von spiegeln auf y = x² / √x umgestellt; Wörter „Umkehrfunktion“, „f⁻¹“ in linear.
   - Wörter ergänzt, weil die einführende A-Karte entfällt: reihen/rekursiv („Folge“, aₙ), reihen/arithmetisch („explizite Formel“), prozent_grundwert/formel („Zinseszins“, q), verknuepft/mengen_verstehen (n(A)), verknuepft/rueckschluss und mehrstufig/unabhaengig (P(A | B) = P_B(A)).
   - **Bewusst gelassen (Meinung):** linear/wirkung fragt „Für welche k fallen die Geraden?“ (k − 4 < 0). Das ist Vorzeichen-Denken; formal kommt `gleichungen.ungleichungen` zwei Flüge später. Ebenso Dezimalzahlen in Größen bei den Verhältnis-Karten (Kommaschreibweise bei Größen ist Kl. 5).
8. **Teil C:** gekürzt sind `umformen` (Titel „Wiederholung: Scheitelform bestimmen“) und `extremwert` („Wiederholung: Extremwertprobleme“); Einstieg verweist auf den Flug „Quadratische Terme und Extremwerte“ (Klasse 8). Beispiel, Merksatz, Fehler, Bild unverändert. Behalten: alles über Kl. 8 hinaus (Parabel, −b/(2a), Faktor vor x², alle Stufe-3-Aufgaben, Knobel, Test/Korrektur/Sicherung). `scheitel` (Scheitel ablesen am Graphen) und `terme.umformen`/binomisch (Kl. 7) habe ich nicht gekürzt – sie gehören zur Parabellehre bzw. liegen vor Kl. 8.
9. **klasse:** Die Generatoren von `funktionen.reihen` und `abbildungen.matrizen` schreiben `ib_myp` 5 (aus `themenliste.json`), in der Datei stand 4. Jetzt wieder gleich der Themenliste.
10. Prüfskript-Hinweise, die bleiben: additionstheoreme – Merksatz 38 Wörter (beide Formeln nötig); dualsystem – „große Zahl ohne Leerzeichen“ bei Zweierzahlen (gewollt; Zweierzahlen als Antworttyp `text`, damit die App sie nicht als „10 100“ zeigt).

### Für den Haupt-Chat: 24 entfernte Übungen in `funktionen.quadratisch` (sperren)
- `umformen` S1: „Bestimme den Scheitel von y = x² − 4x + 7.“ · „… x² + 14x + 55.“ · „… x² + 14x + 42.“ · „Bei y = x² + 10x + 29 liegt der Scheitel bei x = −b/(2a). Berechne die x-Koordinate des Scheitels.“ · überzählig: „… x² − 4x + 4.“ · „… x² − 14x + 42.“
- `umformen` S2: „Bestimme den Scheitel von y = −x² − 2x + 1.“ · „… −x² + 14x − 47.“ · „… −x² − 8x − 16.“ · „… −x² + 2x + 5.“ · „… 3x² − 36x + 113.“ · „… −2x² + 12x − 17.“ · „… 2x² − 8x.“ · „… −x² + 2x − 10.“ · „… 2x² + 4x + 7.“
- `extremwert` S1: „Welchen kleinsten Wert nimmt f(x) = x² + 4x an?“ · „Welchen größten Wert nimmt f(x) = −2x² − 8x − 2 an?“ · „Welchen kleinsten Wert nimmt f(x) = x² − 4x + 4 an?“ · „Welchen größten Wert nimmt f(x) = −x² − 6x − 4 an?“
- `extremwert` S2: „Ein rechteckiges Gehege soll mit 108 m Zaun umgeben werden. Welchen größten Flächeninhalt kann es haben?“ · überzählig: „Zwei Zahlen haben die Summe 36. …“ · „Ein rechteckiges Gehege soll mit 12 m Zaun …“ · „An einer Hauswand … 76 m Zaun …“; S3 überzählig: „An einer Hauswand … 96 m Zaun …“

### Was sich für ein Kind ändert, das den Zielflug schon abgeschlossen hat
Regel (README): Vertiefung zählt nicht für den Stempel; eine neue Pflicht-Lernkarte macht den Flug wieder offen. Lernstände habe ich nicht gelesen – „betrifft“ ist eine Annahme aus den Plan-Klassen.
- **Wieder offen (neue Pflicht-Karte):**
  - `zahlen.natuerlich` (+ dualsystem, Kl. 5) – betrifft vermutlich **beide Kinder** (erster Flug der Kl. 5).
  - `abbildungen.kongruenz` (+ gegenvektor, Plan Kl. 6) – betrifft vermutlich **Kind B**; Kind A später.
  - `funktionen.reihen` (+ 3 Karten, Plan Kl. 10, freiwillig) und `abbildungen.matrizen` (+ abstand, RS Kl. 10, freiwillig) – nur, falls schon geflogen (unwahrscheinlich).
- **Nicht wieder offen, nur neue freiwillige Etappen:** `bruch.brueche`, `groessen.proportional`, `stochastik.verknuepft`, `funktionen.linear`, `gleichungen.lgs2`, `bruch.prozent_grundwert`, `funktionen.exponential_log`, `funktionen.potenz`, `stochastik.mehrstufig`, `abbildungen.aehnlichkeit`, `trigo.rechtwinklig`, `trigo.allgemein`.
- **`funktionen.quadratisch`:** neue Vertiefung spiegeln; umformen/extremwert kürzer. Nichts wird wieder offen. Wer an den 24 entfernten Übungen Lösungen hat, behält sie (wenn gesperrt statt gelöscht – Annahme).

### Nicht geprüft
- Datenbank (Lernstände, Status) – nicht gelesen.
- Darstellung in der App: Stellentafel mit Stellen „32 … 1“ statt H/Z/E, Antworttyp `text` mit Zweierzahlen, Koordinatensystem mit `wurzel` und `bereich` (spiegeln-Beispiel).
- Von den umgezogenen Karten habe ich Erklärung, alle Fragetexte und den Anfang der Lösungswege auf Vorwissen gelesen, nicht jede Antwortoption und jeden Tipp einzeln. Die alten Aufgaben selbst habe ich nicht neu nachgerechnet (das Prüfskript rechnet die Zahl-Aufgaben nach: OK).
- Gym-Lehrplan zu Umkehrfunktionen, Graphenabbildung, Schwerpunkt, Additionstheoremen (für Pflicht/Vertiefung nur die Zuordnung aus `doppelt-rsib.md`).
- Expeditionen: keine verweist auf ein aufgelöstes Thema (per Skript geprüft).

### Commits (Zweig `aufloesen`)
bruch.brueche · groessen.proportional · stochastik.verknuepft · abbildungen.kongruenz · funktionen.linear · gleichungen.lgs2 · funktionen.reihen · bruch.prozent_grundwert · funktionen.quadratisch · funktionen.exponential_log · funktionen.potenz · stochastik.mehrstufig · zahlen.natuerlich (2 Commits + Generator) · abbildungen.aehnlichkeit · trigo.rechtwinklig · trigo.allgemein · abbildungen.matrizen · Postfach.
