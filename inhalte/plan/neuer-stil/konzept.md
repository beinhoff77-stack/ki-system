# Neuer Stil – Teil 3: Konzept (drei Varianten, Empfehlung B)

Stand 28.11.2026. Kennzeichen: **[B]** belegt (Fundstellen in `bestand.md`) · **[R]** Repo gezählt · **[L]** Lage-Zahl Projektleiter · **[A]** Annahme · **[S]** Schätzung · **[M]** Meinung.
„V“/„R“ = Verstehens-/Rechen-Aufgabe nach der Klasse in `didaktik.md` Abschnitt 2 (aus `form` **oder** `typ` abgeleitet – also nicht nur an `form` festgemacht).

## Überblick

| | A „Ohne Umbau“ | **B „Je Etappe Rechnen und Verstehen“ (empfohlen)** | C „Verstehen zuerst“ |
|---|---|---|---|
| Üben | wie heute (jede 3. Bearbeitung Form); Schalter Sachaufgabe an | wie heute + „sitzt“ braucht 1 gezählte V; Form-Platz darf Nachbarstufe nehmen | jede 2. Bearbeitung V; „sitzt“ braucht 2 V |
| Flugtest | je Etappe 1 R + 1 V (V-Aufgaben einfach in Pool `test`) | je Etappe 1 R + 1 V, beide nötig | je Etappe nur 1 V (R entfällt, Rechnen gilt durch „sitzt“ als gezeigt) |
| Korrektur | nächste freie Aufgabe (R oder V, wie die Reihenfolge fällt) | gleiche Art wie die falsche | immer V |
| Nachtest | V gemischt nach Reihenfolge | je Etappe abwechselnd: Runde 1 V, 2 R, 3 V (kleine Flüge halb/halb) | zwei Drittel V |
| „gesichert“ | wie heute | wie heute + mindestens einmal V und einmal R richtig | wie heute |
| Anteil V in Tests [S] | Flugtest 50 %, sonst langsam steigend | Flugtest 50 %, Korrektur gezielt, Nachtest ≈ 2/3 | Flugtest 100 %, Nachtest 2/3 |
| Code | keiner an App/Server (nur Werkzeug + 3 Texte) | Server 5 Stellen, App 3, Werkzeug | wie B + mehr |
| Risiko | Korrektur weicht dem Verstehen aus; ungewohnte Form im Nachtest | mittel, schrittweise | Kl. 5 scheitert an Form; Rechnen wird im Test nicht mehr geprüft |

**[M] Empfehlung B**, eingeführt in drei Stufen (Abschnitt 6). Stufe 1 von B ist fast identisch mit A – A ist also kein Gegenentwurf, sondern der erste Schritt.

---

## 1. Üben

**Zielanteil je Etappe (6 Bearbeitungen, fehlerfreies Kind)** [M]: mindestens **2 V**, davon mindestens 1 in neuer **Form**; dazu 1 Sachaufgabe (Schalter `anwenden_pflicht`).
- Heute schon erreicht, wenn die Formen in der passenden Stufe da sind [B]: Platz 3 (Stufe 2) und 6 (Stufe 3) sind Form-Plätze; die übrigen bringen über den Typ-Wechsel (`lernWaehleKern`, `neuTyp`) häufig weitere V-`typ`.
- **Welche Form wann** [M], passt zur vorhandenen Stufenverteilung [R]: früh (Stufe 1–2) Brücke, Zwei Wege, nach Fehlern Lückenweg (Verstehen aufbauen); spät (Stufe 3) Umkehren, Fehler-Detektiv, Verfahren wählen, Anwenden (Verstehen prüfen). Kein Fehler-Detektiv direkt nach eigenem Fehler (gilt schon, `lernTaktErlaubt`).

**Regel „sitzt“ (B)** [M]: zusätzlich zu den heutigen Bedingungen **mindestens eine gezählte V-Aufgabe** – gebaut wie die Sachaufgaben-Pflicht (FT-S Regel 6): Schalter `verstehen_pflicht`, gilt nur für Karten, die noch nie gelandet sind, nur wenn die Lernkarte eine freigegebene, zählende V-Übung hat, abgeleitet aus `karte_stand.gezaehlt` (keine neue Spalte). App zeigt „Noch eine Verstehens-Aufgabe“ und legt eine vor (wie `lernAnwendenFehlt`).

**Form-Platz ohne passende Stufe** [M]: ungelöste Form der Nachbarstufe nehmen (Stufe ±1, zählend) statt einer normalen Aufgabe. **Hinweis:** Am 27.11. hat der Nutzer entschieden, die App hier *nicht* zu lockern, sondern Stufe-3-Formen schreiben zu lassen (`offene-punkte.md` Z. 51). Mit Runde 11/12/13 haben heute fast alle Lernkarten Kl. 5/8 eine Stufe-3-Form [R] – die Lockerung ist daher **nur noch eine Rückfallregel**, Frage 5 in `entscheidung.md`.

**Etappen ohne Form-Aufgaben (Rückfall)** [M]:
1. V wird auch über den `typ` erkannt → fast jede Lernkarte hat V (29 % der Übungen nach Profi-Tabelle [L]).
2. Hat eine Lernkarte gar keine zählende V-Übung, entfällt die Pflicht (wie „schwer nötig“ heute). Kein Kind bleibt hängen.
3. Einheiten ohne jede Form (Kl. 8: `funktionen.gebrochen`, `gleichungen.formeln` [R]) zuerst mit Übungsformen beliefern, bevor dort Test-V kommt.

## 2. Tests

| Testart | B: Zusammenstellung | Bewertung | Begründung |
|---|---|---|---|
| **Flugtest** | je Pflicht-Etappe 1 R (Bestand) + 1 V (neu, Pool `test`) | Etappe nachgewiesen, wenn beide richtig (= heutige Regel bool_and) | Leitsatz: verstehen *und* können; Raten hilft nur bei einer Hälfte |
| **Nachtragstest** | 1 Aufgabe je offene Etappe wie heute (R zuerst, weil Pool `test` nach Reihenfolge) | wie heute | [M] neu hinzugekommene Etappen nicht schwerer machen als andere |
| **Korrektur** | je Etappe „noch üben“ **eine Aufgabe der Art, die falsch war** (beide falsch → V) | wie heute | sonst kann ein Kind „Verstehen falsch“ mit einer Rechenaufgabe „korrigieren“ |
| **Nachtest** | Menge je Etappe wie heute (⌈5/Etappen⌉); bei 1 je Etappe: Runde 1 V, Runde 2 R, Runde 3 V; bei mehreren je Etappe: Hälfte V (aufgerundet); fehlt V → R (nie „Vorrat erschöpft“ wegen der Art) | Quote wie heute (0,8/0,6) | Profi: Langzeit trägt Verstehen (`verhaeltnis.md` Z. 52) |
| **„gesichert“** | – | zusätzlich: in den Nachtests mindestens einmal V und einmal R richtig | sonst „gesichert“ ohne je Verstehen gezeigt |

**„Rechnen richtig, Verstehen falsch“**: Etappe „noch üben“; Ergebnisanzeige „Rechnen ✓ · Verstehen ✗ – übe noch einmal eine Verstehens-Aufgabe“; Korrektur stellt eine neue V. Im Üben bleibt die Karte gelandet (keine Rücknahme).
**Form-Bekanntheit**: V im Test nur in Bauarten, die das Kind im Üben schon ≥ 2-mal bearbeitet hat (`didaktik.md` 6.1); sonst V in Bauart Umkehren/Zwei Wege/Anwenden (`zahl`) oder R.

## 3. Was es an AUFGABEN kostet

Bedarf je Pflicht-Lernziel (B) [S]:
| Pool | neue V | Begründung |
|---|---|---|
| test | **1** | Flugtest und Nachtragstest (heute genau 1 R je Lernziel [R]) |
| korrektur | **2** | Korrektur zieht nur ungesehene; zweiter Fehlschlag braucht eine frische; R-Korrektur: Bestand 3–4 [R] reicht |
| sicherung | **3** | Runden 1 und 3 bei 1 je Etappe + 1 Reserve für „wiederholen“/Folgerunde; kleine Flüge (≤ 4 Etappen, 2–5 je Etappe) brauchen mehr (bis 6) |
| **zusammen** | **≈ 6** | |

- Varianten: A ≈ 4 (1 test + 1 korrektur + 2 sicherung), C ≈ 7.
- **Gesamt** [S]: 675 Lernziele [R] × 6 ≈ **4 000 Aufgaben** (B); davon Pflicht-Lernziele weniger (Kür nicht nötig) – realistisch 3 000–4 000. Das ist die Größenordnung des ganzen heutigen Sicherungs-Vorrats (4 252 [L]).
- **Erste Stufe nur für die beiden Kinder** [A: je Kind 8 Einheiten]: Kl. 5 im Mittel 7,5 Lernziele je Einheit, Kl. 8 6,1 [R] → 8 × 7,5 + 8 × 6,1 ≈ **110 Lernziele** → **≈ 660 Aufgaben** (B), ≈ 440 (A). Dazu für Kind 2, falls `funktionen.gebrochen`/`gleichungen.formeln` dabei sind, 30–50 Übungsformen.
- Schreibtakt [B]: Runden 150–210 Aufgaben; Gegenprüfung beanstandete 30–60 % je Runde (`offene-punkte.md`, „Qualität der Schreiber“) → **3–4 Runden** für Stufe 1, je Runde mit Vorprüfung und Gegenprüfung.
- **Reihenfolge des Schreibens** [M]: (1) `test` für die Einheiten, deren Flugtest als Nächstes kommt; (2) `korrektur`; (3) `sicherung` für Einheiten mit Nachtest in den nächsten 10 Lerntagen.

**Liste, die der Projektleiter liefern muss** (lesend, nur IDs und Zahlen, nichts Personenbezogenes ins Repo):
1. je Kind: aktueller Flug + die nächsten Flüge der Route (bis 8): `einheit_id`, `thema_schluessel`, Pflicht-Lernziele, Stand (Üben / Flugtest offen / Flugtest fertig, Nachtest-Runde, nächster Nachtest in Lerntagen);
2. je solcher Einheit und Pool `test`/`korrektur`/`sicherung`: freigegebene Aufgaben je Lernziel, min/max `reihenfolge` je Pool, ungestellte je Kind;
3. je Kind: welche `form` schon bearbeitet (Anzahl, richtig) – für die Form-Bekanntheit;
4. Testsitzungen mit Status `laeuft` (dürfen nicht berührt werden).

## 4. Was es an SERVER und APP kostet

Schritte (B), Aufwand reine Bauzeit [S] ohne Gegenprüfungs-Wartezeit; jeder Serverschritt als selbstprüfendes Paket mit Probelauf nach dem Muster NF-S/FT-S (zwei zulässige Zustände, md5, Vorher/Nachher).

| Nr | Was | Fundstelle | Aufwand |
|---|---|---|---|
| E | **Einordnung der 7 023 Test-Aufgaben**: neue Tabelle `schule.aufgabe_einordnung(aufgabe_id, art R/V/A, quelle, am)` + Hilfsfunktion `schule.aufgabe_art(a)` = Tabelle, sonst aus `form`/`typ` (`didaktik.md` 2). Grund: freigegebene Aufgaben sind per Trigger unveränderlich [B]. Einordnung zuerst maschinell (Stichworte, Antworttyp), dann Stichprobe 10 % vom Mathe-Profi; nur „V sicher“ zählt als V | neu | 4 h + Einordnung 6–10 h |
| W1 | `tools/rollend_sql.py`: Pools test/korrektur/sicherung, `max_r` je Pool, Sperren (kein Lückenweg, `zaehlt` ja, Pflicht-Etappe, keine Übung gleicher Bauart), `typ` Pflicht | Z. 120, 140–145, 228 | 4–6 h |
| W2 | `tools/vorrat_pruefen.py`: beliebige Runden; Test-Regeln (Auswahl ≥ 4, Detektiv gekoppelt, Ähnlichkeit zu Übungen) | Z. 24–25 | 3 h |
| T | App-Texte „Eine Bordkarte je Etappe“ → „Zwei Bordkarten je Etappe: rechnen und verstehen“ | `lernen.js` 5152, 5154, 5157 | 0,5 h |
| S1 | Korrektur gleiche Art: Zweig `korrektur` in `test_starten_intern` – Art der falschen Aufgabe(n) der letzten Sitzung dieser Etappe, `order by (aufgabe_art = gesucht) desc, reihenfolge` | nf_s Z. 178–186 (Grundfassung NF-S, md5 7abcd291…) | 3–4 h |
| S2 | Nachtest abwechselnd: `nachtest_auswahl` ordnet Ungestellte nach gewünschter Art (aus Zahl der schon gestellten V/R dieser Etappe), Rückfall R; `nachtest_stand` Vorrat je Art melden | nf_s Z. 57–70, 76–118 | 4–5 h |
| S3 | Form-Bekanntheit: `schule.form_bekannt(kind, form)`; im Flugtest V-Aufgabe in unbekannter Bauart durch freie V bekannter Bauart ersetzen (sonst nur R) – braucht Auswahl je Etappe statt „alle Pool-test“ | nf_s Z. 157 | 4–6 h |
| A1 | Test-Ergebnis je Etappe „Rechnen ✓ · Verstehen ✗“ (Server: `art` in `ergebnisse` von `test_abschliessen_intern` – **Grundfassung nicht im Repo**, erst live lesen) | `lernen.js` 5225 ff.; Server unbekannt | 2 h + 2–3 h |
| S4 | Üben „sitzt“ mit 1 V: Schalter `verstehen_pflicht`, `karte_verstehen_ok`, Patch `karte_landet`, Ausgaben in `etappen_stand` und `uebung_pruefen_intern` – **nach TEMPO-S1** (das ersetzt `etappen_stand` mit md5-Zuständen) | FT-S-Muster | 6–8 h |
| A2 | App: „Noch eine Verstehens-Aufgabe“ + Auswahl; Form-Platz mit Nachbarstufe (falls Frage 5 = ja); Tests `tests/lernen-takt.test.cjs` | `lernen.js` 466, 476–505 | 3–4 h |
| S5 | „gesichert“ braucht V und R: `test_abschliessen_intern` (Grundfassung fehlt) | unbekannt | 4–6 h |

Summe B ≈ **45–65 h** Bauzeit [S], dazu Gegenprüfungen und Probeläufe.

**Was ohne Änderung an App und Server sofort geht** [B, geprüft am Code]:
- Neue V-Aufgaben in die Pools `test`, `korrektur`, `sicherung` einspielen: `aufgaben_einfuegen` nimmt jeden Pool, Anzeige und Bewertung im Test können alle sechs Antworttypen (`bestand.md` c)). **Nur das Werkzeug** `rollend_sql.py` sperrt heute (W1).
- Wirkung dann: **Flugtest** zieht *alle* Aufgaben des Pools `test` → automatisch 1 R + 1 V je Etappe, beide nötig (bool_and). **Korrektur** und **Nachtest** ziehen die neuen erst, wenn sie in der Reihenfolge vorn stehen (Korrektur `order by reihenfolge limit 1`; Nachtest: ungestellte, dann `reihenfolge`) → Reihenfolge-Nummern bewusst setzen (niedriger als der Bestand, falls der Projektleiter freie Nummern bestätigt) – sonst erst nach Verbrauch der alten.
- Schalter `anwenden_pflicht = 1` (fertig gebaut, wartet auf Satz des Nutzers).
- Grenzen ohne Code: Korrektur trifft nicht gezielt die falsche Art; keine Form-Bekanntheit; Test-Texte nennen „eine Bordkarte je Etappe“ (Textänderung T = kleinster App-Eingriff).
- `form_jede` von 3 auf 2 (nur Regelwert) **[M] nicht empfohlen**: Plätze 2/4/6 treffen Soll-Stufe 1/2/3, auf Stufe 1 gibt es kaum zählende Formen [R] → bringt wenig.

**Risiken für laufende Lernstände**
| Risiko | Bewertung | Gegenmaßnahme |
|---|---|---|
| laufende Testsitzungen | keins: Aufgaben werden beim Start fest in `testsitzung.aufgaben` geschrieben [B nf_s Z. 192] | Einspielen trotzdem in Nutzungspause |
| schon bestandene Flugtests | nicht berührt (Flugtest einmal je Einheit) [B] | – |
| Fairness Alt-Etappen | Nachtest bringt V-Aufgaben in Etappen, die ohne Formen geübt wurden | Form-Bekanntheit (S3); bis dahin in `sicherung` nur V in `zahl`-Bauarten (Umkehren, Zwei Wege, Anwenden-transfer) |
| „sitzt“-Stände | V-Pflicht nur für nie gelandete Karten (Muster FT-S) | Schalter, erst nach App |
| Flugtest-Länge | bis 28 Karten in großen Kl.-5-Flügen [R: bis 14 Etappen] | Unterbrechen geht; Hinweis im Text; Frage 2 |
| mehr Korrekturen | bool_and über 2 Aufgaben | erwünscht; messen (Abschnitt 7) |
| Vorrat erschöpft | strengere Auswahl darf nie blockieren | immer Rückfall auf R |
| gleichzeitige Umbauten | TEMPO-S1 (`etappen_stand`), NF-S (md5-Zustände von `test_starten_intern`/`nachtest_*`) | S1–S3 auf NF-S-Stand aufsetzen, S4 nach TEMPO-S1 |

## 5. Variante A und C im Detail (kurz)

- **A**: nur E (optional), W1, W2, T + Aufgaben (≈ 4 je Lernziel). ≈ 10–15 h + Inhalte. Schwäche: Korrektur kann Verstehen umgehen; kein Schutz vor ungewohnter Form im Nachtest.
- **C**: Flugtest wählt je Etappe nur V (Server-Umbau Zweig blocktest, wie S3), `form_jede` 2 + Nachbarstufe, „sitzt“ 2 V. ≈ 60–80 h. [M] Für Klasse 5 zu streng; Rechnen wird nur noch im Üben belegt, das vergessen Kinder aber zuerst wieder.

## 6. Stufenplan (B)

| Stufe | Inhalt | Nutzen | Aufwand [S] | Voraussetzung |
|---|---|---|---|---|
| **1 schnell** | W1, W2, T; Schalter `anwenden_pflicht = 1`; ≈ 110 V-Test-Aufgaben + ≈ 220 Korrektur-V + ≈ 330 Sicherungs-V für die 16 Einheiten der Kinder (Reihenfolge: test → korrektur → sicherung) | Flugtest prüft ab sofort Verstehen je Etappe; Nachtest bekommt V | Bau 8–10 h; Inhalte 3–4 Runden | Liste des Projektleiters; Mathe-Profi bestätigt Klasse V; Gegenprüfung; Satz des Nutzers |
| **2** | E (Einordnung), S1, S2, S3, A1 | Korrektur trifft die falsche Art, Nachtest abwechselnd, kein Scheitern an fremder Form, Eltern sehen R/V getrennt | 25–35 h | Stufe 1 live, 2 Wochen Messung |
| **3** | S4 + A2 (Üben „sitzt“ mit V), S5 („gesichert“ mit V+R), übrige Klassen beliefern (≈ 3 000 Aufgaben) | Regel gilt überall | 15–25 h + viele Runden | TEMPO-S1 eingespielt; Stufe 2 bewährt |

## 7. Messung nach vier Wochen

Alles lesend aus der Datenbank, getrennt je Kind, verglichen mit den vier Wochen davor. [M] Bei zwei Kindern ist das ein Trend, kein Beweis.

| Frage | Zahl | Tabellen |
|---|---|---|
| Kommt der neue Stil an? | Anteil Bearbeitungen mit V (Übung: `testsitzung_id is null`, ohne Misch) je Woche; Anteil V-Versuche in Tests | `schule.versuch` ⋈ `schule.aufgabe` (`form`, `typ`, `pool`) bzw. `aufgabe_einordnung` |
| Können sie es? | Quote richtig im 1. Anlauf R vs. V, je Form; im Test R vs. V je Testart | `versuch` (`richtig`, `anlauf`, `testsitzung_id`) ⋈ `testsitzung` (`art`) |
| Wird es zu schwer? | Anteil Etappen „noch üben“ nach Flugtest (vorher/nachher); Bearbeitungen bis „sitzt“ (`karte_bearbeitungen` bei `sitzt_am`); Zeit je Aufgabe (Tempo-Daten, sobald da) | `lernziel_stand` (`status`), `karte_stand` (`sitzt_am`), `versuch` (`am`) |
| Hält es länger? | Nachtest-Ergebnis (bestanden/wiederholen/Rückreise) und Quote; wieder geöffnete Karten (`geoeffnet_am`), `wdh_fehler` | `testsitzung` (`ergebnis`, `punkte`), `karte_stand` |
| Wo hakt es? | Fehlbilder in V-Aufgaben, Häufung je Form | „Was wackelt“ (`wackelt_analyse`), `aufgabe_fehlbild` |
| Vorrat | `nachtest_stand.vorrat_runden`, „Vorrat erschöpft“-Antworten | `nachtest_stand`, App-Meldung |

Wirkt, wenn [M]: V-Quote im Nachtest höchstens 10 Prozentpunkte unter R-Quote, Korrekturanteil höchstens doppelt so hoch wie vorher, Bearbeitungen bis „sitzt“ höchstens + 30 %, und das Kind kann eine Lösung **laut erklären** (Stichprobe der Eltern, je Woche zwei Aufgaben).
