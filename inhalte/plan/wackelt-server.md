# WW-S – „Was wackelt“, Teil Datenbank (zu Entwurf 4)

Stand 27.11.2026, Zweig `helfer-regelbezug`. **Entwurf, nichts eingespielt.** Vorlage: `inhalte/design/wackelt/entwurf4/umsetzung4.md` (vom Nutzer freigegeben), dazu `entwurf3/umsetzung3.md` Abschnitte 2 (Regeln fürs Verschwinden) und 3 (Datenbedarf).

| Datei | Was |
|---|---|
| `supabase/migrations/20261205_ww_s_wackelt.sql` | Tabellen `schule.fehler_erledigt`, `schule.nachueben`; Analyse; Abhaken; Nachüben; vier api-Aktionen |
| `tools/tests/wackelt_einspielen.py` | selbstprüfendes Einspiel-Paket; `--probe` rollt alles zurück |
| `tools/tests/wackelt_test.py` | lokal im **Nachbau** (nicht die echte Datenbank): Probe ohne und mit RB-S, Einspielen, Rechte über die api-Aktionen |

Lokale Prüfung (bestanden): `python3 -I tools/tests/wackelt_test.py` → „WW-S im Nachbau bestanden“, OK; `pglast` liest alle 29 Anweisungen.

## Entscheidungen

1. **Regeln an einem Ort: im Server.** Was „offen“ ist (endgültig falsch, Zeitraum, abgehakt, nachgeübt) und die Zahlen der Auswertung rechnet `schule.wackelt_analyse`. Gründe: (a) Abhaken und Nachüben liegen in der Datenbank – „nachgeübt“ hängt an späteren Versuchen, die der Client sonst alle laden müsste; (b) „endgültig falsch“ gibt es schon als Serverregel (`schule.fehler_endgueltig_am`, LW-S 2) – eine zweite Fassung im Client wiche früher oder später ab; (c) testbar mit dem Probe-Paket an echten Daten. Der Client zeigt nur an (Sortierung, höchstens 6 Themen, 5 neueste Fehler, Fazit-Satz, Kurznamen der Fehlerarten aus dem Regel-Universum). Die Regeln R0–R9 aus Entwurf 1 (Gesprächsplan mit Gewichten) gehören zum abgelehnten Entwurf und sind **nicht** gebaut; Entwurf 4 braucht nur „wiederkehrend“ (≥ 2) und „nur einmal“.
2. **Abhaken ohne DELETE**: Rückgängig setzt `zurueckgenommen_am` (die Projektregeln meiden DELETE). Je Versuch höchstens ein gültiger Eintrag. Sammeln (je Thema „alle abhaken“) = Liste von `versuch_ids` – der Client schickt die Versuche, die er gerade zeigt; der Server nimmt nur endgültig falsche Versuche dieses Kindes.
3. **„Nachgeübt“ wird beim Lesen ausgewertet**, nicht beim Antworten (kein neuer Trigger im Antwortweg, wie LW-S). „Danach“ heißt: Versuch-Nummer größer als die höchste Nummer des Kindes beim Schicken (`ab_versuch_id`) – unabhängig von Uhr und Geräten.
4. **Nachüben = eine gespeicherte Aufgabe, beantwortet wie jede Übung.** Kein eigener Antwortweg, keine Änderung an Karte, Wiederholung oder Bordkarten-Auswahl im Server.

## Nachüben – kleinster Eingriff in den Lernablauf

Vorhanden (gelesen): **Nachbessern** (NB-S: wieder offene Etappe wird zuerst vorgelegt; je Etappe, nicht je Aufgabe), **Wieder in die Wiederholung** (ganzer Flug, gestaffelt), **Check-in-Runde** (WD-S: Pflicht-Bordkarten je Lerntag, `schule_wiederholung`), **Mischkarten** (`schule.misch_ausgabe`, vom Server ausgegebene Einzelaufgaben). Eine gezielte Einzelaufgabe vom Lehrer gibt es nicht.

Vorschlag:
- **Welche Aufgabe:** beim Schicken gewählt und gespeichert: dieselbe Lernkarte, freigegeben, zählend, **nicht** die falsche Aufgabe selbst; gleiche Stufe zuerst, dann gleicher Typ, dann eine, die das Kind noch nie bearbeitet hat, und keine, die schon in einem offenen Nachüben liegt. Gibt es keine, die falsche Aufgabe selbst (`dieselbe: true`). Begründung: dieselbe Aufgabe prüft eher das Gedächtnis als das Verfahren.
- **Wann:** als Pflicht-Bordkarten **vorn im Check-in** des nächsten Lerntags (höchstens `nachueben_je_tag` = 3, älteste zuerst; Regel in `schule.regel`). Der Check-in ist der Ort, an dem das Kind schon heute „erst kurz einchecken“ erwartet – keine neue Station auf der Reisekarte.
- **Richtig nachgeübt:** eine richtige Antwort **derselben Lernkarte** ohne Tipp und nicht im 2. Anlauf nach dem Schicken (Entwurf 3, Regel 4) – gleich, ob es die geschickte Aufgabe war. Dann verschwindet der Fehler von der Lehrer-Seite (unter „Erledigtes ansehen“: `nachgeuebt`) und die Bordkarte aus der Liste des Kindes.
- **Erneuter Fehler:** das Nachüben bleibt liegen und kommt am nächsten Lerntag wieder; die neue falsche Antwort ist ein neuer offener Fehler (Entwurf 3, Regel 5). Abhaken der ursprünglichen Antwort beendet das Nachüben (die Bordkarte kommt nicht mehr).

**Client-Stellen, die davon wissen müssen (nicht geändert):**
- `lernWdhLaden` (`lernen.js` ≈ Z. 1730): zusätzlich `schule_nachueben_lesen` holen.
- `lernWdhStand` (≈ Z. 1736): Nachübe-Bordkarten vor `liste` setzen und in `offen`/`runde` zählen; der Check-in muss auch nach `runde_gemacht` noch einmal erscheinen, solange Nachübe-Karten da sind.
- Check-in-Ansicht (≈ Z. 6698–6720) und die Ansagen „Erst n Bordkarten Check-in“ (≈ Z. 1862, 2048) sowie der Startknopf (≈ Z. 2041): Zahl inklusive Nachüben. `schule_wiederholung_runde_fertig` nur für die Server-Runde aufrufen.
- Antworten wie jede Übung (`schule_uebung_pruefen`, ohne `misch`); Stadt der Bordkarte wie bei Check-in/Mischkarte (≈ Z. 848).
- `lernWaehleBordkarte` (≈ Z. 405) braucht **nichts** zu wissen: Nachüben läuft nur im Check-in.
- Lehrer-Seite: `schule_wackelt_analyse`, `schule_fehler_abhaken`, `schule_nachueben_schicken` (Knöpfe ✓ und ↻, „liegt bereit“ aus `nachueben.geschickt_am`).
- Edge-Funktion `supabase/functions/lernen-api/index.ts`, Liste `AKTIONEN` (nicht geändert): `schule_wackelt_analyse: ['lernender_id', 'tage?', 'erledigt?']`, `schule_fehler_abhaken: ['lernender_id', 'versuch_ids', 'zurueck?']`, `schule_nachueben_schicken: ['lernender_id', 'versuch_ids', 'zurueck?']`, `schule_nachueben_lesen: ['lernender_id']`.

## Antwortformen (Beispiele mit erfundenen Daten)

`schule_wackelt_analyse {lernender_id: 2, tage: 14, erledigt: true}` (`tage`: 7, 14 oder 0 = alles; Vorgabe 14):
```json
{"ok": true, "lernender_id": 2, "tage": 14, "seit": "2026-11-13T19:00:00+01:00", "heute": "2026-11-27", "mit_fehlbild": true, "offen_zahl": 10,
 "offen": [
  {"versuch_id": 9001, "am": "2026-11-26T17:25:00+01:00", "tag": "2026-11-26", "thema_id": 29, "thema": "Terme umformen",
   "einheit_id": 31, "lernziel": "minusklammer", "lernkarte": "Minus vor der Klammer",
   "aufgabe": {"id": 5001, "antworttyp": "zahl", "form": "anwenden", "typ": "einkleidung", "stufe": 2,
               "frage": {"text": "Löse: 20 − (x + 4) = 9"}, "loesung": {"wert": 7}, "loesungsweg": "20 − x − 4 = 9, also x = 7."},
   "antwort": {"wert": "15"}, "anlauf": 2, "erst_antwort": {"wert": "13"}, "mit_tipp": false,
   "fehlerart": {"quelle": "fehlbild", "schluessel": "fb:fb.minusklammer.nur_erstes_zeichen", "kennung": "fb.minusklammer.nur_erstes_zeichen",
                 "text": "nur das erste Zeichen in der Klammer gedreht", "regel": "rr.minusklammer", "fehlbild_regel": "rr.minusklammer"},
   "danach_richtig": {"lernkarte_am": "2026-11-27T16:10:00+01:00"},
   "nachueben": {"id": 12, "geschickt_am": "2026-11-26T20:00:00+01:00", "aufgabe_id": 5003}}],
 "auswertung": {"antworten": 64, "richtig": 51,
   "themen": [{"thema_id": 29, "thema": "Terme umformen", "offen": 3, "gesamt": 4}],
   "lerntage": [{"tag": "2026-11-26", "richtig": 7, "falsch": 4}],
   "wiederkehrend": [{"schluessel": "fb:fb.minusklammer.nur_erstes_zeichen", "kennung": "fb.minusklammer.nur_erstes_zeichen",
                      "text": "nur das erste Zeichen in der Klammer gedreht", "anzahl": 4, "offen": 3, "themen": [29, 30]}],
   "einmal": {"lernkarten": 3, "danach_richtig": 2, "themen_danach_richtig": [24, 33]}},
 "erledigt": [{"versuch_id": 8800, "…": "wie offen", "erledigt": {"art": "abgehakt", "am": "2026-11-25T20:05:00+01:00"}}]}
```
- Felder fehlen, wenn leer (`jsonb_strip_nulls`). `offen` höchstens 300, neueste zuerst; `erledigt` nur mit `erledigt: true`, höchstens 200.
- `fehlerart.quelle`: `fehlbild` (RB-S eingespielt und erkannt), `grund` (grober Grund aus `antwort_bewerten`: vorzeichen, komma, vertauscht, gerundet, falsche_einheit), sonst fehlt `fehlerart`. `schluessel` ist der Gruppierschlüssel für „wiederkehrend“: `fb:<Kennung>`, `a:<aufgabe>:<nr>` (Fehlbild ohne Kennung), `g:<grund>`.
- `lerntage`: die letzten 7 Tage mit Antworten (ohne Zeitraum-Grenze), Tag in der Zeitzone des Kindes. `themen`: alle Themen mit Antworten im Zeitraum, nach offenen Fehlern sortiert (Client nimmt 6). Die Lösung kommt über `schule.loesung_sicht` (bei `bedingung` nur Beispiel und Namen).

`schule_fehler_abhaken {lernender_id, versuch_ids: [9001, 9002], zurueck?: false}` → `{"ok": true, "geaendert": 2, "uebersprungen": [{"versuch_id": 9005, "grund": "nicht endgültig falsch"}]}`. Mit `zurueck: true` (Rückgängig, auch „zurückholen“ unter Erledigtes): Eintrag wird zurückgenommen.

`schule_nachueben_schicken {lernender_id, versuch_ids: [9001]}` → `{"ok": true, "geaendert": 1, "geschickt": [{"versuch_id": 9001, "nachueben_id": 12, "aufgabe_id": 5003, "dieselbe": false}], "uebersprungen": []}`; noch einmal → `uebersprungen: [{"grund": "liegt schon bereit"}]`; `zurueck: true` nimmt es zurück.

`schule_nachueben_lesen {lernender_id}` (Kind oder Eltern) → `{"ok": true, "lernender_id": 2, "aufgaben": [{"nachueben_id": 12, "einheit_id": 31, "thema_id": 29, "lernziel": "minusklammer", "geschickt_am": "…", "aufgabe": {"id": 5003, "lernziel": "minusklammer", "stufe": 2, "antworttyp": "zahl", "frage": {"text": "…"}, "tipp": "…", "typ": "direkt"}}]}` – `aufgabe` wie `schule.aufgabe_anzeige` (ohne Lösung).

## Rechte

Analyse, Abhaken, Schicken: `schule.wer_tn` → `schule.ist_leiter` (sonst „Nur Eltern/Lehrer“) → `schule.zugriff` (nur eigene Kinder) – Muster `api.schule_wackelt_lesen`. Lesen der Nachübe-Liste: `schule.zugriff` (Kind nur sich selbst). Tabellen: RLS, keine Policy, keine Rechte für anon/authenticated; api-Funktionen nur `council_mcp`. Das Kind sieht nur die zusätzlichen Aufgaben (ohne Lösung). Im Nachbau geprüft: Kind-Schlüssel → „Nur Eltern/Lehrer“, fremdes Kind → „Kein Zugriff“.

## Reihenfolge der Einspielung

- **WW-S ist unabhängig von RB-S** einspielbar (Voraussetzungen: LW-S, BD-S2, FT-S, WD-S – alle live). Ohne RB-S zeigt die Seite als Fehlerart den groben Grund (bei Auswahl- und vielen Zahlaufgaben: keinen) und „Kommt immer wieder“ gruppiert nur nach diesem Grund – das ist mager, aber richtig; `mit_fehlbild: false` sagt es dem Client. Mit RB-S: Fehlbild-Text und Kennung (für Versuche von vor RB-S nachträglich erkannt).
- Vorschlag: RB-S (Migration + Nachträge) → WW-S → lernen-api (vier Aktionen) → Client (Lehrer-Seite, Check-in).

## Offene Fragen (mit Vorschlag)

1. Beendet Abhaken ein laufendes Nachüben? – **Vorschlag: ja** (so gebaut): Wer abhakt, ist fertig damit; die Bordkarte kommt nicht mehr.
2. Wie viele Nachübe-Karten je Lerntag? – Vorschlag: höchstens 3 (Regel `nachueben_je_tag`), damit der Check-in kurz bleibt; der Rest kommt an den folgenden Tagen.
3. Zählt eine Nachübe-Aufgabe für die Karte wie jede Übung (Folge, „sitzt“, Sterne)? – Vorschlag: ja, ohne Sonderregel; bei einer **sitzenden** Lernkarte prüfen, dass eine falsche Nachübe-Antwort außerhalb der Fälligkeit die Karte nicht wieder öffnet (siehe unten 2).
4. Zeitraum-Standard 14 Tage (Entwurf 4) – „Seit Gespräch“ aus Entwurf 1 entfällt? – Vorschlag: ja, 7/14/alles wie im Entwurf.

## Nicht geprüft (keine Datenbank) – vorab beim Projektleiter

1. Live-Signaturen: `select to_regprocedure(x) from unnest(array['schule.fehler_endgueltig_am(schule.versuch)', 'schule.zugriff(text, bigint)', 'schule.ist_leiter(text)', 'schule.wer_tn(text)', 'schule.lern_ich(text)', 'schule.ist_lern(text)', 'schule.aufgabe_anzeige(schule.aufgabe, boolean)', 'schule.loesung_sicht(schule.aufgabe)', 'schule.aufgabe_zaehlt(schule.aufgabe)', 'schule.wd_regel(text, integer)']) x;` – alle nicht leer; dazu Spalten `schule.lernender.zeitzone`, `schule.lernender.aktiv`, `schule.thema.unterthema`, `schule.versuch.hilfe/anlauf/am`.
2. Wirkung einer Übungsantwort auf eine **sitzende**, nicht fällige Lernkarte (`karte_buchen`): öffnet ein Fehler sie wieder? Lesen: `pg_get_functiondef('schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)'::regprocedure)`.
3. Dauer der Analyse bei „alles“ für ein Kind mit vielen Versuchen: `explain analyze select schule.wackelt_analyse(<kind>, 0, true);` (rollt nichts, schreibt nur Hilfstabellen dieser Sitzung).
4. Rolle `council_mcp` vorhanden (die Migration vergibt das Recht nur dann).
5. Im Probelauf: Das Testkind braucht eine Lernkarte mit drei freigegebenen, zählenden Zahl-Aufgaben ohne Einheit im Ergebnis (gibt es nach den rollend-Runden reichlich).
