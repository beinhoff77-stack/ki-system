# Bestandsberichtigung 1 – Befund und Vorschläge (28.11.2026)

Nur Vorschläge. Nichts eingespielt, keine Quelldatei geändert (`git status` auf `inhalte/themen`, `inhalte/mathe-profi`, `tools/tests/aus` sauber; `bauen.py` prüft das). `vorschlag.json` wird von `bauen.py` erzeugt und geprüft: Nachrechnung (`tools/inhalt_pruefen.pruefe_antwort`), kein Fehlbild gleich der richtigen Antwort, Fehlbilder verschieden, Typ passt zur Stufe, Frage nicht schon vorhanden, kein gleicher Satzbau in der Einheit (Teil b).
Alle genannten Aufgaben sind eingespielt: rollend-Kennungen stehen in `tools/tests/aus/rb_nachtrag_r06/09/11/12/13.sql`; die Dateien aus `inhalte/themen` gehören zu Einheiten in `inhalte/plan/rollend-einheiten.json` (Spalte „Einheit“ = Einheit-ID). Ob der genaue Fragetext einer themen-Aufgabe in der Datenbank steht, ist aus dem Repo nicht belegbar (nur dort prüfbar).
Fakten: Zählungen und Zeichencode-Lesungen. Annahmen sind als „Annahme“ markiert. Die neuen Kennungen `BB1-*` sind Platzhalter.

## Teil a – Stellenwert-Aufgaben (Ziffer oder Betrag?)

Gesucht in allen 28 699 Aufgaben (themen + rollend-1…14): Lückentexte mit Stellenwert-Beschriftung (T/H/Z/E, ZT/HT, Zehntel …) und alle Aufgaben mit „Wert der Ziffer“, „Wie viele Tausender/Hunderter …“, „Stellenwert“. **Genau 2 Aufgaben dieser Bauart.** Alle anderen fragen ausdrücklich „Welchen Wert hat …“, „Welche Ziffer steht …“ oder „insgesamt“. Die umgekehrte Bauart (Betrag erwartet, Ziffer naheliegend) kommt nicht vor.

| Vorschlag | Kennung/Platz | Datei | Einheit/Lernkarte | Kl. | eingespielt | Mangel | Vorschlag |
|---|---|---|---|---|---|---|---|
| BB1-A1 | Index 6, Übung St. 2 | themen/zahlen.natuerlich.json | 1 / stellenwert | 5 | ja (Einheit) | „Zerlege 1 097 in Stellenwerte.“ mit □ T + □ H + □ Z + □ E, Lösung 1/0/9/7; Hinweis „Trage in jedes Feld eine Zahl ein“ lässt 1000/0/90/7 zu | Text: „Zerlege 1 097 in Stellenwerte. Trage in jedes Feld die Ziffer ein, die an dieser Stelle steht.“ Hinweis: „… eine Ziffer von 0 bis 9 ein.“ Lösung 1/0/9/7 gleich; Fehlbilder: 1000 (Lücke 1), 90 (Lücke 3), 9 (Lücke 2) |
| BB1-A2 | Index 31, Sicherung St. 2 | dieselbe | dieselbe | 5 | ja (Einheit) | wie oben, „Zerlege 4 114 …“, Lösung 4/1/1/4 | gleicher Zusatz; Fehlbilder 4000, 100, 10 |

Tipp „Lies die Ziffern von links nach rechts ab“ (Index 6) und Lösungsweg stimmen; Lösungsweg um einen Satz ergänzt. Eine Betragsvariante („Schreibe als Summe: … = _ + _ + _ + _“) wird nicht gebraucht; keine der beiden Aufgaben erwartet Beträge.

## Teil b – Klasse-7-Stoff in der Klasse-6-Einheit `bruch.prozent` (Einheit 11)

Befund: `themen/bruch.prozent.json` führt unter „offen“, dass „vermehrter/verminderter Grundwert rückwärts“ und Doppelrabatt als Rechenaufgabe Klasse 7 sind (Einheit `bruch.prozent_grundwert`) und entfernt wurden. Im Bestand stehen trotzdem Aufgaben dieser Art (Fakt, s. Zusatzfunde D1). Quelle der Zuordnung „Händleraufgabe“: `/home/claude/arbeit/befund-rollend14.md` Z. 43 nennt K6-V117 und „eine Aufgabe in themen bruch.prozent (Händler erhöht um 25 % und gibt 20 % Rabatt)“. Annahme: das ist die „Händleraufgabe“. Ich nehme als zweite Händlerfundstelle K6-V114 (Aufschlag → Einkaufspreis) dazu.

| Vorschlag | Kennung/Platz | Datei | Einheit/Lernkarte | Kl. | eingespielt | Mangel | Vorschlag |
|---|---|---|---|---|---|---|---|
| BB1-B1 | K6-V117 | rollend-6/bruch.prozent.json #14 | 11 / rabatt_aufschlag, St. 3 rueckwaerts | 6 | ja (rb_nachtrag_r06) | „Fahrrad nach 20 % Rabatt noch 280 € → Preis vorher“ = Preis nach Rabatt → alter Preis | **ersetzen** (Klasse 6 bleibt): „Ein Fahrrad wird um 20 % billiger. Man spart dabei 70 €. Wie viel Euro kostet das Fahrrad jetzt?“ Lösung 280 € (c `70 / 0.2 - 70`), Typ verknuepfen, Tipp, Lösungsweg und 3 Fehlbilder (350, 14, 420) in `vorschlag.json`. Satzbau weicht von R14-V114 ab. Alternativ: nur sperren (Stufe 3 hat dann noch 9 Übungen) |
| BB1-B2 | themen #232 | themen/bruch.prozent.json | 11 / rabatt_aufschlag, Bonus St. 3 knobel | 6 | ja (Einheit) | Händler: +25 %, dann −20 %, „Wie viel Prozent zahlt der Kunde?“ = Prozentfaktoren hintereinander | **ersetzen** durch Knobel: „Händler … Jacke 25 % Rabatt = 20 €, Pullover 20 % = 30 € … wie viel Euro war der Pullover vorher teurer?“ Lösung 70 € (80 → 150); Fehlbilder 10, 80, 150 |
| BB1-B3 | K6-V114 | rollend-6/bruch.prozent.json #11 | 11 / grundwert, St. 3 transfer | 6 | ja | „Händler: Spiel mit 8 % Gewinn für 135 € → Einkaufspreis“ = vermehrter Grundwert rückwärts | **ersetzen**: „… macht 6 € Gewinn. Das sind 12 % vom Einkaufspreis …“ Lösung 50 €; Fehlbilder 0,72, 56, 72 |

Umhängen nach `bruch.prozent_grundwert` ist nicht nötig: dort liegen schon 40 Übungen der Lernkarten vermehrt/vermindert/zurueck.

## Teil c – Beschriftungsfehler in Zeichnungen

Annahme: Die „fünf Aufgaben“ sind die in `offene-punkte.md` genannten R8-V079, R8-V115, R5-V129, R8-V121, K6-V121 (Sichtprüfung 27.11., `/home/claude/arbeit/sicht3/bericht.md` 2.2). Ursachen sind aus dem Zeichencode (`lernen.js`, nur gelesen) abgeleitet, nicht neu gerendert.

| Vorschlag | Kennung | Datei | Einheit/Lernkarte | Kl. | eingespielt | Mangel | Vorschlag |
|---|---|---|---|---|---|---|---|
| BB1-C1 | R8-V079 | rollend-13/funktionen.linear.json #2 | 17 / graph_ablesen | 8 | ja | x-Achsenname „t in min“ abgeschnitten (rechts der Achse ca. 24 px frei) | `name_x` „t“, `name_y` „h“ (Einheiten stehen im Text) |
| BB1-C2 | R8-V115 | rollend-13/abbildungen.kongruenz_teil3.json #0 | 308 / punktspiegelung | 8 | ja | Punktname P überdeckt Achsenzahl „2“ (P bei x = −1 neben der y-Achse) | P(1 \| 2), Z(4 \| 3), Feld 0…8 / 0…6; Antworten P′(4\|3), **P′(7\|4)**, P′(7\|2), P′(3\|1) |
| BB1-C3 | R5-V129 | rollend-12/geometrie.winkel.json #10 | 49 / figuren | 5 | ja | drei Winkelmarken „25°“, „?“, „30°“ ca. 18 px auseinander, überdecken Linien | Marken α, β, γ, Werte im Text; Lösung 35° |
| BB1-C4 | R8-V121 | rollend-13/geometrie.konstruktion_teil2.json #0 | 306 / vierecke | 8 | ja | lange Marken „(x + 30)°“, „(2x + 30)°“ berühren Linie und Bogen | Marken α, β, Terme im Text; Lösung x = 40 |
| BB1-C5 | K6-V121 | rollend-6/terme.aufstellen.json #0 | 59 / struktur | 6 | ja | Schablone „① = □; ② = □; …“: Zeile 2 beginnt mit „;“ | Schablone ohne Strichpunkte „① = □ ② = □ ③ = □ ④ = □“ |

Nicht an der Aufgabe lösbar: leere Stellenwert-Kacheln „T H Z E“ bei Winkelaufgaben (R5-V129, S3-V013, Klasse ≤ 6) sind ein App-Befund.

### Zu breite Tabellen (Tabelle gedreht: Zeilen statt Spalten, Inhalt und Lösung gleich)

| Vorschlag | Kennung | Einheit/Lernkarte | Spalten | Sichtprüfung | neue Tabelle |
|---|---|---|---|---|---|
| BB1-T01 | K9A-V161 | 32 / regel | 11 | kaputt, gesehen | Ziffer \| Treffer (10 Zeilen) |
| BB1-T02 | K9A-V128 | 33 / schnitt | 9 | kaputt, gesehen | Zahl \| in A \| in B |
| BB1-T03 | S3-V038 | 5 / beide_seiten | 5 | kaputt (Zahlen zerbrechen), gesehen | Minute \| Becken A (l) \| Becken B (l) |
| BB1-T04 | K9A-V011 | 46 / abschaetzen | 7 | gemessen | n \| n²; Tipp „obere/untere Zeile“ → „linke/rechte Spalte“ |
| BB1-T05 | S3-V018 | 39 / ordnen | 6 | gemessen | Person \| Stand in € |
| BB1-T06 | R8-V059 | 16 / eindeutig | 6 | gemessen | Kind \| Hausnummer |
| BB1-T07 | S3-V027 | 28 / prisma | 5 | leichter (5 Zellen) | Grundfläche \| Ecken \| Flächen \| Kanten |
| BB1-T08 | S3-V058 | 94 / prisma_volumen | 5 | leichter | Körperhöhe in cm \| Volumen in cm³ |
| BB1-T09 | K9A-V143 | 33 / vierfeld | 5 | leichter | Gruppe \| Schüler |
| BB1-T10 | K9A-V137 | 33 / venn | 5 | leichter | Bereich \| Kinder |
| BB1-T11 | R8-V031 | 34 / definitionsmenge | 6 | leichter | x \| T(x) |
| BB1-T12 | S3-V008 | 44 / klammern | 6 | leichter | Schritt \| Rechnung |
| BB1-T13 | R8-V125 | 310 / koordinaten | 5 | leichter | Ecke \| Koordinaten |

Nicht auffindbar: nichts. Die „13 leichteren“ sind die in 2.2 des Berichts namentlich genannten (S3-V027, S3-V058, K9A-V143, R8-V031, K9A-V137, K9B-V005, K9B-V050, S3-V008, K9B-V029, K9B-V089, K9B-V008, R5-V115, R8-V125). **Ohne Aufgabenvorschlag** (nur 3–4 Spalten, die Ursache ist die lange Kopfzelle, z. B. „Fläche des Quadrats über der Seite“): K9B-V005, K9B-V050, K9B-V029, K9B-V089, K9B-V008, R5-V115. Besser in der App (Umbruch an Leerzeichen, Spaltenbreite) zu lösen, wo die Reparatur breiter Tabellen ohnehin vorgesehen ist (Zweig `helfer-karte`).

## Zusatzfunde (d) – nur aufgenommen, ohne Vorschlag

- **D1 Klasse-7-Prozentstoff weiter in `themen/bruch.prozent.json`** (Widerspruch zum „offen“-Vermerk): #214 (Nach 20 % Rabatt 64 € → vorher), #227, #229 (rückwärts), #230 (Doppelrabatt gerechnet), #246, Bonus #221, #222, #247. Entscheidung nötig: sperren (Stufe 3 behält dann genug Übungen) oder wie BB1-B1 ersetzen.
- **D2 Expedition `8-schulfest`**: `inhalt_pruefen --alle` meldet 2 FEHLER, Voraussetzung „stochastik.grundbegriffe_teil2“ gibt es nicht in `inhalte/themen` (Teil 2 fehlt oder falsch benannt).
- **D3 Achsenname rechts abgeschnitten, Bauart**: 98 Bestandsaufgaben mit `name_x` länger als 2 Zeichen (z. B. `themen/daten.zweidimensional.json`, „Lernzeit in h“). Annahme: gleiche Abschneidung wie R8-V079; nicht gerendert. Besser in der App (Platz rechts der Achse).
- **D4 Strichpunkt-Umbruch, Bauart K6-V121**: 282 Lückenaufgaben mit vier und mehr Lücken und „; “ (themen 187, rollend 95). Besser in der App lösen.
- **D5 Weitere breite Tabellen (≥ 6 Spalten), nicht gemessen**: 55 Aufgaben außerhalb der Sichtprüfung (Bestand themen, rollend-1…5, 7, 8) – gleiches Muster zu erwarten.
- **D6 K9A-V170** (Säulendiagramm): „Achsentitel ‚Punkte‘ ragt aus der Zeichnung“, nur gemessen. Der Titel steht links oben (x = 4); Ursache unklar, ohne Rendern nicht entscheidbar.
- Geprüft und ohne Befund: Fehlbild gleich richtiger Antwort (0 von allen rollend-Aufgaben), doppelte oder ungültige Auswahlantworten (0), „Cashewkerne“ ist berichtigt.

## Einspielen: der vorgesehene Weg

1. **Schutz**: Trigger `aufgabe_schutz` verbietet UPDATE/DELETE von Aufgaben einer freigegebenen Einheit (Funktion in `supabase/migrations/20261118_w176_t4_expeditionen.sql` Z. 57–66; Hinweis in `20261118_w150_f_stufen_typ_bonus.sql` Z. 16: „dort scheitert ein Abgleich wie bisher“). Einheit-Abgleich (`einheit_abgleichen`, `20261114_w150_einheit_abgleichen.sql`) kann die Texte freigegebener Aufgaben nicht ändern.
2. **Vorgesehen ist: Berichtigung = neue Aufgabe**, Wortlaut in `20261204_rb_s_regelbezug.sql` (Funktion `regelbezug_schutz`: „Berichtigung = neue Aufgabe“; „Einfügen bleibt erlaubt“) und Auftrag in `inhalte/AUFTRAEGE.md` Z. 896–912 („Ersatz-Aufgaben einfügen; die alten Fassungen danach sperren, freigegeben = false“). Einfügen geht über `schule.aufgaben_einfuegen` (`20261118_w150_f_stufen_typ_bonus.sql`; fügt nur ein, was es mit gleicher Frage und gleichen Antworten in der Einheit noch nicht gibt; deshalb ändern alle Vorschläge das Feld `f` bzw. `a`, geprüft in `bauen.py`).
3. **Alte Fassung sperren** ist ein UPDATE (`freigegeben = false`), also durch `aufgabe_schutz` blockiert. Bisheriger Umgehungsweg: Einheit kurz auf `geprueft`, ändern, zurück auf `freigegeben` (`20261123_tl_s_teilung.sql` Z. 10–11 und 495–496, 546–548: „bewusst, nur für diesen Schritt“). Eigener Satz des Nutzers nötig. Gesperrte Aufgaben werden nur noch nicht neu ausgewählt, laufende Prüfungen werden weiter gewertet (`20261118_w176_a_gesperrt_pruefen.sql`); Versuche und Sterne der alten Aufgabe bleiben.
4. **Regel und Fehlbilder** der neuen Aufgaben: `schule.aufgabe_regel` und `schule.aufgabe_fehlbild` nur per INSERT (Nachtrag nach `tools/regelbezug_sql.py`); die Vorschläge tragen `regel`/`fehlbilder` (bei themen-Quellen ohne Regel).
5. **Zu beachten**: Platz (`reihenfolge`) und `form`/`zaehlt` der neuen Aufgabe vergibt das Paket (`tools/rollend_sql.py`-Art, `zaehlt` ja); Kennungen BB1-* gibt es in der Datenbank nicht (Zuordnung dort über Einheit + Reihenfolge). Mindestmengen je Lernkarte prüfen (je Stufe Übungen und Typen, `inhalte/README.md`): alle Ersätze behalten Pool, Stufe und Lernkarte der alten Aufgabe. Doppelt vorhanden sind alte und neue Aufgabe bis zum Sperren. Ein Paket wurde nicht gebaut.
