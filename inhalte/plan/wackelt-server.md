# WW-S – „Was wackelt“, Teil Datenbank (zu Entwurf 4)

Stand 27.11.2026, Zweig `helfer-regelbezug`. **Entwurf, nichts eingespielt.** Gegenprüfung: Werkstatt 1129 (Auflagen eingearbeitet). Schrittfolge: `einspiel-reihenfolge-rb-ww.md`. Vorlage: `inhalte/design/wackelt/entwurf4/umsetzung4.md` (vom Nutzer freigegeben), dazu `entwurf3/umsetzung3.md` Abschnitte 2 (Regeln fürs Verschwinden) und 3 (Datenbedarf).

| Datei | Was |
|---|---|
| `supabase/migrations/20261205_ww_s_wackelt.sql` | Tabellen `schule.fehler_erledigt`, `schule.nachueben`, `schule.nachueben_ausgabe`; Analyse; Abhaken; Nachüben mit Tagesgrenze; vier api-Aktionen |
| `supabase/functions/lernen-api/index.ts` | vier Aktionen in `AKTIONEN` ergänzt, Version 0.9.4 – **vorbereitet, nicht ausgeliefert** (vorher mit der ausgelieferten Fassung vergleichen: die Repo-Fassung stand auf 0.9.3) |
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
- **Wann:** als Pflicht-Bordkarten **vorn im Check-in** des nächsten Lerntags. Der Check-in ist der Ort, an dem das Kind schon heute „erst kurz einchecken“ erwartet – keine neue Station auf der Reisekarte.
- **Tagesgrenze (echt):** je Kind und Lerntag höchstens `nachueben_je_tag` = 3 **ausgelieferte** Nachübe-Aufgaben. Lerntag = `schule.heute_tag(kind)` (Kalendertag in der Zeitzone des Kindes – derselbe Tag wie „heute selbst gelöst“ und `schule.lerntag`). Ausgeliefert wird nur, wenn das Kind selbst liest (`schule_nachueben_lesen` mit Kind-Sitzung); jede Auslieferung steht in `schule.nachueben_ausgabe (nachueben_id, tag)`. Am selben Tag rückt nichts nach (auch nicht, wenn eine erledigt ist); ein zweites Gerät bekommt dieselben; nicht Erledigtes kommt am nächsten Lerntag wieder (zählt dann neu). Eltern sehen eine Vorschau ohne Auslieferung (`ausgeliefert: false` bei den wartenden). Test im Nachbau: 4 geschickt → heute 3, zweiter Abruf gleich, nach einer erledigten 2, nächster Tag 3.
- **Richtig nachgeübt:** eine richtige Antwort **derselben Lernkarte** ohne Tipp und nicht im 2. Anlauf nach dem Schicken (Entwurf 3, Regel 4) – gleich, ob es die geschickte Aufgabe war. Dann verschwindet der Fehler von der Lehrer-Seite (unter „Erledigtes ansehen“: `nachgeuebt`) und die Bordkarte aus der Liste des Kindes.
- **Erneuter Fehler:** das Nachüben bleibt liegen und kommt am nächsten Lerntag wieder; die neue falsche Antwort ist ein neuer offener Fehler (Entwurf 3, Regel 5). Abhaken der ursprünglichen Antwort beendet das Nachüben (die Bordkarte kommt nicht mehr) – vom Nutzer so entschieden.

### Nachübe-Antwort an der Karte (Vorschlag des Projektleiters, gebaut: wie jede Übungsantwort)

Eine Nachübe-Aufgabe ist eine normale, zählende Übung; die Antwort läuft durch `schule_uebung_pruefen` → `versuch_karte` → `schule.karte_buchen` (unverändert). Was dort passiert (Live-Fassung laut Repo: `20261119_w176_h_muss.sql` + FT-S-Filter; vom Projektleiter an der Live-Definition bestätigt):

| Zustand der Lernkarte | richtig, ohne Tipp, 1. Anlauf | richtig mit Tipp oder im 2. Anlauf | falsch (endgültig) |
|---|---|---|---|
| noch nicht gelandet | `folge` + 1; neue Aufgabe zählt als eigene Lösung (kann landen lassen) | nur Zähler „richtig“, `folge` bleibt | `folge` 0, `fehler_folge` + 1 (jeder 2. Fehler senkt die Stufe) |
| gelandet, kein offener Wiederholungs-Fehler, nicht fällig | `wdh_fehler` bleibt 0, sonst nichts | wie links | `wdh_fehler` 1, Wiederholungsstufe − 1, **fällig nach 1 Lerntag** |
| gelandet, kein offener Fehler, fällig | Stufe + 1, nächste Fälligkeit (WD-S: bestandene Wiederholung, Sterne) | wie links (`karte_buchen` unterscheidet hier nicht nach Tipp) | wie Zeile darüber |
| gelandet, ein offener Wiederholungs-Fehler (`wdh_fehler` 1) | `wdh_fehler` 0 (bei Fälligkeit Stufe + 1) | wie links | **wieder offen**: `sitzt` false, Stufe 0, es braucht wieder 3 eigene Lösungen in Folge |

Folge für das Nachüben: Die Antwort, zu der nachgeübt wird, war selbst schon ein Fehler an dieser Karte. War die Karte gelandet, steht danach `wdh_fehler` = 1 – **eine falsche Nachübe-Antwort öffnet sie also wieder** („erst beim zweiten Fehler übst du noch einmal von vorn“, die Regel, die die Kinder kennen). Eine richtige setzt den Fehler zurück und erledigt das Nachüben. Ein falscher 1. Anlauf mit zweiter Chance wird wie immer erst nach dem 2. Anlauf bzw. dem Weitergehen gebucht; Aufgaben mit `zaehlt = nein` bucht `karte_buchen` gar nicht (sie werden fürs Nachüben nicht gewählt).
Geprüft: im Nachbau (echtes `karte_buchen` aus dem Repo) und im Probe-Paket an der echten Datenbank – Nachübe-Antwort und normale Übungsantwort derselben Lernkarte vom selben Ausgangsstand ergeben dieselbe Kartenzeile; der Bericht zeigt die beobachteten Zustände nach dem 1. und 2. Fehler.
**Abgegrenzte Stelle zum Ändern:** `schule.nachueben_liegt(kind, aufgabe)` (heute ungenutzt) sagt, ob eine Antwort eine heute ausgelieferte Nachübe-Aufgabe betrifft. Soll eine falsche Nachübe-Antwort eine gelandete, nicht fällige Karte nicht öffnen, genügt in `karte_buchen` im Zweig `if not p_richtig then if k.wdh_fehler >= 1 then` eine vorgeschaltete Zeile `if schule.nachueben_liegt(p_l, p_aufgabe) and not schule.karte_faellig(k) then <nur zählen> else …` (eigener Text-Patch mit Satz des Nutzers).

**Client-Stellen, die davon wissen müssen (nicht geändert):**
- `lernWdhLaden` (`lernen.js` ≈ Z. 1730): zusätzlich `schule_nachueben_lesen` holen.
- `lernWdhStand` (≈ Z. 1736): Nachübe-Bordkarten vor `liste` setzen und in `offen`/`runde` zählen; der Check-in muss auch nach `runde_gemacht` noch einmal erscheinen, solange Nachübe-Karten da sind.
- Check-in-Ansicht (≈ Z. 6698–6720) und die Ansagen „Erst n Bordkarten Check-in“ (≈ Z. 1862, 2048) sowie der Startknopf (≈ Z. 2041): Zahl inklusive Nachüben. `schule_wiederholung_runde_fertig` nur für die Server-Runde aufrufen.
- Antworten wie jede Übung (`schule_uebung_pruefen`, ohne `misch`); Stadt der Bordkarte wie bei Check-in/Mischkarte (≈ Z. 848).
- `lernWaehleBordkarte` (≈ Z. 405) braucht **nichts** zu wissen: Nachüben läuft nur im Check-in.
- Lehrer-Seite: `schule_wackelt_analyse`, `schule_fehler_abhaken`, `schule_nachueben_schicken` (Knöpfe ✓ und ↻, „liegt bereit“ aus `nachueben.geschickt_am`).
- Edge-Funktion `supabase/functions/lernen-api/index.ts`, Liste `AKTIONEN` (im Repo vorbereitet, Version 0.9.4, nicht ausgeliefert): `schule_wackelt_analyse: ['lernender_id', 'tage?', 'erledigt?']`, `schule_fehler_abhaken: ['lernender_id', 'versuch_ids', 'zurueck?']`, `schule_nachueben_schicken: ['lernender_id', 'versuch_ids', 'zurueck?']`, `schule_nachueben_lesen: ['lernender_id']`.

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

`schule_nachueben_lesen {lernender_id}` (Kind: liefert aus und zählt; Eltern: Vorschau) → `{"ok": true, "lernender_id": 2, "tag": "2026-11-28", "aufgaben": [{"nachueben_id": 12, "einheit_id": 31, "thema_id": 29, "lernziel": "minusklammer", "geschickt_am": "…", "ausgeliefert": true, "aufgabe": {"id": 5003, "lernziel": "minusklammer", "stufe": 2, "antworttyp": "zahl", "frage": {"text": "…"}, "tipp": "…", "typ": "direkt"}}]}` – `aufgabe` wie `schule.aufgabe_anzeige` (ohne Lösung).

## Rechte

Analyse, Abhaken, Schicken: `schule.wer_tn` → `schule.ist_leiter` (sonst „Nur Eltern/Lehrer“) → `schule.zugriff` – Muster `api.schule_wackelt_lesen`. Lesen der Nachübe-Liste: `schule.zugriff` (Kind nur sich selbst). Tabellen: RLS, keine Policy, keine Rechte für anon/authenticated; api-Funktionen nur `council_mcp`. Das Kind sieht nur die zusätzlichen Aufgaben (ohne Lösung).
Geprüft (Probe-Paket, an der echten Datenbank mit echten Lern-Sitzungen, die nur in einer zurückgerollten Untertransaktion entstehen; ebenso im Nachbau mit den echten Zugangsfunktionen): Kind → Analyse, Abhaken, Schicken „Nur Eltern/Lehrer“ (auch für sich selbst); Kind liest die eigene Nachübe-Liste; fremdes Kind → Nachübe-Liste „Kein Zugriff“, Analyse abgewiesen; Eltern → Analyse ok; unbekannte Sitzung → abgewiesen.
**Hinweis „Eltern eines anderen Kindes“:** Nach der bestehenden Regel `schule.sieht` sehen Lern-Zugänge mit Rolle `eltern`/`lehrer` **alle** Kinder (Familien-App), Council-Zugänge mit Leitungsrecht ebenso. Eine Einschränkung „nur eigene Kinder“ gibt es nur für Council-Teilnehmer ohne Leitung (`schule.zugang`) – die scheitern schon an `ist_leiter`. Eine eigene Sperre „Eltern von Kind A sehen Kind B nicht“ würde `schule.sieht` für alle Aktionen ändern; nicht Teil von WW-S.

## Reihenfolge der Einspielung

- **WW-S ist unabhängig von RB-S** einspielbar (Voraussetzungen: LW-S, BD-S2, FT-S, WD-S – alle live). Ohne RB-S zeigt die Seite als Fehlerart den groben Grund (bei Auswahl- und vielen Zahlaufgaben: keinen) und „Kommt immer wieder“ gruppiert nur nach diesem Grund – das ist mager, aber richtig; `mit_fehlbild: false` sagt es dem Client. Mit RB-S: Fehlbild-Text und Kennung (für Versuche von vor RB-S nachträglich erkannt).
- Vorschlag: RB-S (Migration + Nachträge) → WW-S → lernen-api (vier Aktionen) → Client (Lehrer-Seite, Check-in).

## Offene Fragen (mit Vorschlag)

1. ~~Beendet Abhaken ein laufendes Nachüben?~~ Entschieden: ja. ~~Nachüben-Regel?~~ Entschieden: wie vorgeschlagen.
2. Nachübe-Antwort an einer gelandeten Karte: wie jede Übung (öffnet nach dem zweiten Fehler) – **dem Nutzer vorlegen** (Tabelle oben); Änderung wäre eine Zeile in `karte_buchen`.
3. Zeitraum-Standard 14 Tage (Entwurf 4) – „Seit Gespräch“ aus Entwurf 1 entfällt? – Vorschlag: ja, 7/14/alles wie im Entwurf.
4. Sollen Eltern nur „ihre“ Kinder sehen (siehe Hinweis oben)? – Vorschlag: nein, Familien-App wie bisher.

## Nicht geprüft (keine Datenbank) – vorab beim Projektleiter

1. Live-Signaturen: `select to_regprocedure(x) from unnest(array['schule.fehler_endgueltig_am(schule.versuch)', 'schule.zugriff(text, bigint)', 'schule.ist_leiter(text)', 'schule.wer_tn(text)', 'schule.lern_ich(text)', 'schule.ist_lern(text)', 'schule.aufgabe_anzeige(schule.aufgabe, boolean)', 'schule.loesung_sicht(schule.aufgabe)', 'schule.aufgabe_zaehlt(schule.aufgabe)', 'schule.wd_regel(text, integer)']) x;` – alle nicht leer; dazu Spalten `schule.lernender.zeitzone`, `schule.lernender.aktiv`, `schule.thema.unterthema`, `schule.versuch.hilfe/anlauf/am`.
2. ~~`karte_buchen`~~ vom Projektleiter gelesen (siehe Tabelle). Für einen genaueren Nachbau: `select pg_get_functiondef(p.oid) from pg_proc p where p.oid in ('schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)'::regprocedure, 'schule.karte_faellig(schule.karte_stand)'::regprocedure, 'schule.versuch_karte()'::regprocedure, 'schule.versuch_hilfe_merken()'::regprocedure);` sowie `select tgname, pg_get_triggerdef(oid) from pg_trigger where tgrelid = 'schule.karte_stand'::regclass and not tgisinternal;` (der WD-S-Trigger an der Karte fehlt im Nachbau).
3. Dauer der Analyse „alles“: misst das Probe-Paket selbst (Testkind und das Kind mit den meisten Versuchen; `laufzeit_ms_*` im Bericht, Warnung über 500 ms).
4. Rolle `council_mcp` vorhanden (die Migration vergibt das Recht nur dann).
5. Im Probelauf: Das Testkind braucht eine Lernkarte mit drei freigegebenen, zählenden Zahl-Aufgaben ohne Einheit im Ergebnis (gibt es nach den rollend-Runden reichlich).
