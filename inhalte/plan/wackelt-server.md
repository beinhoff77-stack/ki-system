# WW-S2 – „Was wackelt“, Teil Datenbank (zu Entwurf 4), schlanke Fassung

Stand 28.11.2026. **WW-S2 ist seit 27.11. in der echten Datenbank eingespielt** (Edge-Funktion 0.9.5 und Client nicht ausgeliefert). **WW-S3** (Folgemigration, Zweig `helfer-ww3`, nicht eingespielt) steht im Abschnitt [WW-S3](#ww-s3--folgemigration-zu-ww-s2-nicht-eingespielt) unten; die Abschnitte bis dorthin beschreiben WW-S2. Schrittfolge: `einspiel-reihenfolge-rb-ww.md`. Vorlage: `inhalte/design/wackelt/entwurf4/umsetzung4.md` (vom Nutzer freigegeben), dazu `entwurf3/umsetzung3.md` Abschnitte 2 (Regeln fürs Verschwinden) und 3 (Datenbedarf).

**Entscheidung des Nutzers (27.11.):** Kein „Nachüben schicken“. Es bleibt bei den Wiederholungs- und Mischkarten, wie sie eingestellt sind; Logik und Ablauf bleiben gleich. Deshalb ist WW-S zu **WW-S2** verschlankt: nur (a) Analyse für Eltern/Lehrer und (b) Abhaken / Abhaken zurücknehmen. Alles zum Nachüben (Tabellen `schule.nachueben`, `schule.nachueben_ausgabe`, Regel `nachueben_je_tag`, Funktionen `nachueben_schicken`, `nachueben_gueltig`, `nachueben_liste`, `nachueben_liegt`, Aktionen `schule_nachueben_schicken`, `schule_nachueben_lesen`, Tagesgrenze, Karten-Vergleich, Client-Stellen im Check-in) ist entfernt. Weil nichts eingespielt war, ist die Migration direkt geändert (kein DROP für nie Angelegtes).

| Datei | Was |
|---|---|
| `supabase/migrations/20261205_ww_s_wackelt.sql` | Tabelle `schule.fehler_erledigt`; Analyse; Abhaken; zwei api-Aktionen |
| `supabase/functions/lernen-api/index.ts` | zwei Aktionen in `AKTIONEN`, Version 0.9.5 – **vorbereitet, nicht ausgeliefert** (ausgeliefert ist 0.9.3; 0.9.4 war der nie ausgelieferte Entwurf mit Nachüben) |
| `tools/tests/wackelt_einspielen.py` | selbstprüfendes Einspiel-Paket mit Nachweis „berührt die Lernlogik nicht“; `--probe` rollt alles zurück |
| `tools/tests/wackelt_test.py` | lokal im **Nachbau** (nicht die echte Datenbank): Probe ohne und mit RB-S, Einspielen zweimal, Rechte über die api-Aktionen, Edge-Liste |
| `tools/tests/wackelt_gegenprobe.py` | lokal im Nachbau: sechs absichtlich verdorbene Fassungen der Migration – das Probe-Paket muss jede mit „WW-S ABBRUCH“ abweisen |

Lokale Prüfung (bestanden, 27.11.): `wackelt_test.py` → „WW-S2 im Nachbau bestanden“; `wackelt_gegenprobe.py` → 6 von 6 Eingriffen erkannt; `rb_ww_pakete.py --pruefen` → OK; `regelbezug_sql_test.py` → bestanden; `pglast` liest alle 19 Anweisungen der Migration.

## Entscheidungen

1. **Regeln an einem Ort: im Server.** Was „offen“ ist (endgültig falsch, im Zeitraum, nicht abgehakt) und die Zahlen der Auswertung rechnet `schule.wackelt_analyse`. Gründe: „endgültig falsch“ gibt es schon als Serverregel (`schule.fehler_endgueltig_am`, LW-S 2); das Abhaken liegt in der Datenbank; testbar mit dem Probe-Paket an echten Daten. Der Client zeigt nur an (Sortierung, höchstens 6 Themen, 5 neueste Fehler, Fazit-Satz, Kurznamen der Fehlerarten).
2. **Abhaken ohne DELETE**: Rückgängig setzt `zurueckgenommen_am`. Je Versuch höchstens ein gültiger Eintrag. Sammeln (je Thema „alle abhaken“) = Liste von `versuch_ids`; der Server nimmt nur endgültig falsche Versuche dieses Kindes.
3. **Abhaken ist nur eine Markierung für die Lehrer-Seite.** Es nimmt die Antwort aus „offen“ und der Auswertung der Seite – sonst nichts (siehe nächster Abschnitt).
4. **Ohne Fremdschlüssel auf bestehende Tabellen.** Ein `references schule.versuch` legte interne Trigger an `schule.versuch` an und sperrte die Tabelle beim Anlegen. Die Zugehörigkeit (Versuch gehört dem Kind, endgültig falsch) prüft `schule.ww_versuche` vor jedem Eintrag; Versuche werden nie gelöscht (im Repo gibt es kein `delete from schule.versuch`).
5. „Danach richtig gelöst“ (✓ in der Fehlerart-Spalte) ist eine **Anzeige**, beim Lesen aus späteren Versuchen ausgewertet; es lässt nichts verschwinden.

## Berührt die Lernlogik nicht

**Liest** (nur lesend, keine dieser Tabellen/Funktionen wird geändert):
- Tabellen: `schule.versuch`, `schule.aufgabe`, `schule.einheit` (Titel der Lernkarte aus `inhalt.etappen`), `schule.thema`, `schule.lernender` (`zeitzone`, `aktiv`), die eigene `schule.fehler_erledigt`; mit RB-S zusätzlich `schule.aufgabe_regel`, `schule.aufgabe_fehlbild`. Für die Rechte: `schule.lern_sitzung`, `schule.lern_login`, `council.zugaenge`, `schule.zugang`.
- Funktionen (alle bestehend, unverändert, `stable`/`immutable` bis auf `zugriff`, das nur prüft und abweist): `schule.fehler_endgueltig_am` → `schule.versuch_wertung`; `schule.antwort_bewerten` (immutable); `schule.versuch_regelbezug` → `schule.fehlbild_finden` (nur wenn RB-S eingespielt); `schule.loesung_sicht`; `schule.wer_tn`, `schule.lern_ich`, `schule.ist_lern`, `schule.ist_leiter`, `schule.sieht`, `schule.zugriff`.

**Schreibt** ausschließlich:
- `schule.fehler_erledigt` (Abhaken = insert, Zurücknehmen = update von `zurueckgenommen_am/_von`),
- Hilfstabellen der eigenen Sitzung `pg_temp.ww_v`, `pg_temp.ww_f` (on commit drop) in der Analyse.

**Schreibt und ändert nicht** – weder die Migration noch eine ihrer Funktionen:
- `schule.versuch` (kein insert/update/delete, kein neuer Trigger, kein Fremdschlüssel und damit auch kein interner Trigger),
- Karte und Wiederholung: `schule.karte_stand`, `schule.wdh_runde`, `schule.wdh_runde_etappe`, `schule.abgelegt`, `schule.lerntag`; Mischkarten: `schule.misch_ausgabe`; `schule.sterne`; `schule.regel` (keine neue Regel); LW-S `schule.wackelt_status`;
- die Trigger am Antwortweg (`versuch_hilfe_merken`, `versuch_karte`, `versuch_lerntag`, `versuch_misch_verfall`, `versuch_sterne`, mit RB-S `versuch_fehlbild`) und die Funktionen der Lernlogik (`karte_buchen`, `karte_faellig`, `misch_buchen`, `mischkarten`, `misch_gueltig`, `wiederholung_intern`, `wdh_runde_fertig`, `uebung_pruefen_*`, Auswahl der nächsten Aufgabe/Bordkarte). WW-S2 legt nur neue Funktionen an (`ww_fehlerart`, `ww_von`, `wackelt_analyse`, `ww_versuche`, `fehler_abhaken`, `api.schule_wackelt_analyse`, `api.schule_fehler_abhaken`).

**Abhaken hat keine Auswirkung auf Wiederholungs- und Mischkarten:** `schule.fehler_erledigt` ist neu und wird von keiner bestehenden Funktion gelesen (im Repo kommt der Name nur in der WW-S-Migration, ihren Paketen/Tests und den Plänen vor). Die Lernlogik liest weiter nur `schule.versuch` und `schule.karte_stand` – beides bleibt beim Abhaken unberührt. Ein abgehakter Fehler bleibt also für Karte, „sitzt“, Punkte, Wiederholung, Check-in und Mischkarten genau so wirksam wie vorher; er verschwindet nur von der Lehrer-Seite.

**Maschinell belegt** (im Probe-Paket, also auch an der echten Datenbank, alles zurückgerollt):
1. Fingerabdruck vor und nach der Migration (beide Läufe): alle bestehenden Funktionen in `schule`/`api` (volle Definition), **alle Trigger an Tabellen in `schule` einschließlich interner**, alle Spalten – gleich (`schema_bestehend_gleich: true`).
2. Fingerabdruck **aller Daten im Schema `schule`** außer `fehler_erledigt` (jede Tabelle, jede Zeile): gleich während Analyse, Abhaken, zweitem Abhaken, Rückgängig (`bestand_gleich_beim_abhaken: true`), während der api-Aufrufe mit echten Sitzungen, und nach dem ganzen Paket wie vorher (`bestand_gleich: true`).
3. Sitzende, nicht fällige Lernkarte: nach dem 1. Fehler Abhaken → Kartenzeile unverändert; ein 2. Fehler wirkt mit und ohne Abhaken gleich (beobachtet im Nachbau: nach dem 1. Fehler `sitzt` true, `wdh_fehler` 1; nach dem 2. `sitzt` false, wieder geöffnet – in beiden Läufen; Bericht `karte_abhaken_ohne_wirkung`).
4. Keine Funktion mit `nachueb` im Namen; keine Fremdschlüssel an `fehler_erledigt`.
5. Gegenprobe (`wackelt_gegenprobe.py`): eine Fassung, die beim Abhaken die Karte ändert, in der Analyse eine bestehende Tabelle beschreibt, eine bestehende Funktion ersetzt, einen Trigger an `schule.versuch` anlegt, einen Fremdschlüssel setzt oder `ist_leiter` weglässt, wird jeweils abgewiesen.

## Antwortformen (Beispiele mit erfundenen Daten)

`schule_wackelt_analyse {lernender_id: 2, tage: 14, erledigt: true}` (`tage`: 7, 14 oder 0 = alles; Vorgabe 14; `erledigt` Vorgabe false):
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
   "danach_richtig": {"lernkarte_am": "2026-11-27T16:10:00+01:00"}}],
 "auswertung": {"antworten": 64, "richtig": 51,
   "themen": [{"thema_id": 29, "thema": "Terme umformen", "offen": 3, "gesamt": 4}],
   "lerntage": [{"tag": "2026-11-26", "richtig": 7, "falsch": 4}],
   "wiederkehrend": [{"schluessel": "fb:fb.minusklammer.nur_erstes_zeichen", "kennung": "fb.minusklammer.nur_erstes_zeichen",
                      "text": "nur das erste Zeichen in der Klammer gedreht", "anzahl": 4, "offen": 3, "themen": [29, 30]}],
   "einmal": {"lernkarten": 3, "danach_richtig": 2, "themen_danach_richtig": [24, 33]}},
 "erledigt": [{"versuch_id": 8800, "…": "wie offen", "erledigt": {"art": "abgehakt", "am": "2026-11-25T20:05:00+01:00"}}]}
```
- **Ab WW-S3 anders:** `danach_richtig` ist dann `true` oder fehlt (Zeitpunkte in `danach_richtig_am`), dazu `stand: 3`, `erledigt.id`, `erledigt.tag`, `themen[].besprochen`; **Zurücknehmen über `versuch_ids` gibt es ab WW-S3 nicht mehr** (nur `markierung_ids`) – siehe Abschnitt WW-S3.
- Felder fehlen, wenn leer (`jsonb_strip_nulls`). `offen` höchstens 300, neueste zuerst; `erledigt` nur mit `erledigt: true`, höchstens 200, zuletzt abgehakt zuerst; `erledigt.art` ist immer `abgehakt`.
- `fehlerart.quelle`: `fehlbild` (RB-S eingespielt und erkannt), `grund` (grober Grund aus `antwort_bewerten`: vorzeichen, komma, vertauscht, gerundet, falsche_einheit), sonst fehlt `fehlerart`. `schluessel` ist der Gruppierschlüssel für „wiederkehrend“: `fb:<Kennung>`, `a:<aufgabe>:<nr>` (Fehlbild ohne Kennung), `g:<grund>`.
- `lerntage`: die letzten 7 Tage mit Antworten (ohne Zeitraum-Grenze), Tag in der Zeitzone des Kindes. `themen`: alle Themen mit Antworten im Zeitraum, nach offenen Fehlern sortiert (Client nimmt 6). Lösung über `schule.loesung_sicht` (bei `bedingung` nur Beispiel und Namen).

`schule_fehler_abhaken {lernender_id, versuch_ids: [9001, 9002], zurueck?: false}` → `{"ok": true, "geaendert": 2, "uebersprungen": [{"versuch_id": 9005, "grund": "nicht endgültig falsch"}]}`. `grund` sonst `nicht gefunden` (auch: Versuch eines anderen Kindes) oder `richtig`. Mit `zurueck: true` (Rückgängig, auch „zurückholen“ unter Erledigtes): Eintrag wird zurückgenommen, `geaendert` zählt die zurückgenommenen. Zweites Abhaken derselben Antwort: `geaendert: 0`. `versuch_ids`: 1 bis 200 ganze Zahlen, sonst Fehler „versuch_ids: …“.

## Rechte

Beide Aktionen: `schule.wer_tn` (unbekannte/abgelaufene Sitzung → „Nicht angemeldet“) → `schule.ist_leiter` (sonst „Nur Eltern/Lehrer“) → `schule.zugriff` (sonst „Kein Zugriff auf diesen Lernenden“) → Kind aktiv – Muster `api.schule_wackelt_lesen`, unverändert streng. Das Kind sieht und ändert nichts davon (auch nicht für sich selbst). Tabelle: RLS, keine Policy, keine Rechte für anon/authenticated; api-Funktionen nur `council_mcp`; die Edge-Funktion meldet ohne gültige Sitzung 401, bevor die Datenbank gefragt wird.
Geprüft (Probe-Paket mit echten Lern-Sitzungen, die nur in einer zurückgerollten Untertransaktion entstehen; ebenso im Nachbau): Kind → Analyse und Abhaken „Nur Eltern/Lehrer“; fremdes Kind → abgewiesen; Eltern → Analyse und Abhaken ok (`von` = „eltern:<Name des Zugangs>“); Lehrer → Analyse und Zurücknehmen ok; unbekannte Sitzung → abgewiesen; `tage: 3` → abgewiesen.
**Hinweis „Eltern eines anderen Kindes“:** Nach der bestehenden Regel `schule.sieht` sehen Lern-Zugänge mit Rolle `eltern`/`lehrer` **alle** Kinder (Familien-App), Council-Zugänge mit Leitungsrecht ebenso. Eine Einschränkung „nur eigene Kinder“ gibt es nur für Council-Teilnehmer ohne Leitung (`schule.zugang`) – die scheitern schon an `ist_leiter`. Eine eigene Sperre würde `schule.sieht` für alle Aktionen ändern; nicht Teil von WW-S2.

## Client-Einbindung (noch zu bauen)

Seite „Was wackelt“ nach Entwurf 4; der Knopf „↻ Nachüben schicken“, „liegt bereit“ und „alle nachüben“ **entfallen**. Alles über `POST /lernen-api/aktion` `{aktion, daten}` → `{ok, ergebnis}` (Fehler: `{ok: false, fehler}` mit dem Text der Datenbank).

| Wo auf der Seite | Aufruf | genutzt aus der Antwort |
|---|---|---|
| Laden, Zeitraum-Umschalter 7 Tage / 14 Tage / Alles, Kind-Umschalter | `schule_wackelt_analyse {lernender_id, tage: 7 \| 14 \| 0}` | ganze Antwort (Form oben) |
| Kachel „Fehler je Thema“ (Balken „3 von 4“, Quote fett, höchstens 6) | – (aus derselben Antwort) | `auswertung.themen[]`: `thema_id`, `thema`, `offen`, `gesamt` |
| Kachel „Letzte Lerntage“ (Säulen) | – | `auswertung.lerntage[]`: `tag`, `richtig`, `falsch` |
| Kachel „Kommt immer wieder“ (höchstens 3) | – | `auswertung.wiederkehrend[]`: `text` bzw. `grund`, `anzahl`, `offen`, `themen[]` |
| Kachel „Nur einmal passiert“ | – | `auswertung.einmal`: `lernkarten`, `danach_richtig`, `themen_danach_richtig[]` |
| Fazit-Satz / Leer-Zustand („Alles abgearbeitet …“) | – | `offen_zahl`, `auswertung.antworten`, `auswertung.richtig`, `wiederkehrend[0]`, `themen` |
| Tabelle „Letzte Fehler“ (5 neueste) | – | `offen[0..4]`: `tag`, `thema` › `lernkarte`, `aufgabe.frage`, `antwort`, `aufgabe.loesung`, `fehlerart` (✓ wenn `danach_richtig`), `versuch_id` |
| Aufklappen einer Zeile | – | `aufgabe` (Text, Tabelle/Zeichnung, `loesungsweg`), `fehlerart.text`, `anlauf`/`erst_antwort`, `mit_tipp`, `danach_richtig` |
| Tabelle „Nach Themen“ (Thema → Lernkarte → Aufgaben) | – | `offen[]` gruppiert nach `thema_id`, dann `einheit_id`+`lernziel` |
| Knopf „✓ Abhaken“ (Zeile) | `schule_fehler_abhaken {lernender_id, versuch_ids: [id]}` | `geaendert`, `uebersprungen[]`; danach Analyse neu laden |
| „alle abhaken“ (Thema) | `schule_fehler_abhaken {lernender_id, versuch_ids: [alle gezeigten des Themas]}` | wie oben |
| Meldung „Rückgängig“ (5 s) | `schule_fehler_abhaken {lernender_id, versuch_ids, zurueck: true}` – **nur WW-S2; ab WW-S3 abgewiesen, dort `markierung_ids`** | `geaendert` |
| „Erledigtes ansehen“ mit „zurückholen“ | `schule_wackelt_analyse {…, erledigt: true}`; zurückholen = `schule_fehler_abhaken {…, zurueck: true}` | `erledigt[]` (wie `offen`, plus `erledigt.am`) |

Edge-Funktion `supabase/functions/lernen-api/index.ts`, Liste `AKTIONEN` (Version 0.9.5, nicht ausgeliefert): `schule_wackelt_analyse: ['lernender_id', 'tage?', 'erledigt?']`, `schule_fehler_abhaken: ['lernender_id', 'versuch_ids', 'zurueck?']`. Kinder-Seiten, Check-in, Bordkarten und Mischkarten bleiben unverändert – sie brauchen nichts davon zu wissen.

## Reihenfolge der Einspielung

- **WW-S2 ist unabhängig von RB-S** einspielbar (Voraussetzungen: LW-S, BD-S2, Lern-Zugänge – alle live). Ohne RB-S zeigt die Seite als Fehlerart den groben Grund (bei Auswahl- und vielen Zahlaufgaben: keinen); `mit_fehlbild: false` sagt es dem Client. Mit RB-S: Fehlbild-Text und Kennung (auch für Versuche von vor RB-S nachträglich erkannt).
- Vorschlag: RB-S (Migration + Nachträge) → WW-S2 → lernen-api 0.9.5 → Client (Lehrer-Seite).

## Offene Fragen (mit Vorschlag)

1. Zeitraum-Standard 14 Tage (Entwurf 4) – „Seit Gespräch“ aus Entwurf 1 entfällt? – Vorschlag: ja, 7/14/alles wie im Entwurf.
2. Sollen Eltern nur „ihre“ Kinder sehen (siehe Hinweis oben)? – Vorschlag: nein, Familien-App wie bisher.
3. Entwurf 4 (`umsetzung4.md`, Bilder) zeigt noch die Nachüben-Knöpfe – beim Bau einfach weglassen; den Entwurf selbst nicht ändern (freigegebene Vorlage).

## Nicht geprüft (keine Datenbank) – vorab beim Projektleiter

1. Live-Signaturen: `select to_regprocedure(x) from unnest(array['schule.fehler_endgueltig_am(schule.versuch)', 'schule.zugriff(text, bigint)', 'schule.ist_leiter(text)', 'schule.wer_tn(text)', 'schule.lern_ich(text)', 'schule.ist_lern(text)', 'schule.loesung_sicht(schule.aufgabe)', 'schule.antwort_bewerten(schule.aufgabe, jsonb)', 'schule.uebung_pruefen_wd(bigint, jsonb)']) x;` – alle nicht leer; dazu Spalten `schule.lernender.zeitzone`, `schule.lernender.aktiv`, `schule.thema.unterthema`, `schule.versuch.hilfe/anlauf/am/client_id`.
2. Dauer der Analyse „alles“: misst das Probe-Paket selbst (Testkind und das Kind mit den meisten Versuchen; `laufzeit_ms_*` im Bericht, Warnung über 500 ms). Ebenso die Dauer der Fingerabdrücke über alle `schule`-Tabellen (Zeitgrenze des Pakets 120 s).
3. Rolle `council_mcp` vorhanden (die Migration vergibt das Recht nur dann); die Rolle braucht wie bisher das Recht, Hilfstabellen (`temp`) anzulegen – das nutzt die Analyse.
4. Im Probelauf: Das Testkind braucht eine Lernkarte mit drei freigegebenen, zählenden Zahl-Aufgaben ohne Einheit im Ergebnis (gibt es nach den rollend-Runden reichlich).

---

## WW-S3 – Folgemigration zu WW-S2 (nicht eingespielt)

Stand 28.11.2026, Zweig `helfer-ww3`. Anlass: Gegenprüfung der Client-Seite „Besprochen je Thema“ (Auflagen aus Werkstatt 1162) – zwei Fehler, die nur am Server lösbar sind, dazu Ergänzungen für den Client. Die WW-S2-Datei bleibt unverändert (eingespielt); WW-S3 ersetzt nur WW-Funktionen per `create or replace` und legt eine neue an.

| Datei | Was |
|---|---|
| `supabase/migrations/20261206_ww_s3_wackelt.sql` | `schule.wackelt_analyse` (nullsicher, `erledigt.id/tag`, `besprochen` je Thema, feste Typen, `stand: 3`), `schule.fehler_abhaken` (Antwort mit `geaendert_ids`, `markierung_ids`), **neu** `schule.fehler_zurueckholen`, `api.schule_fehler_abhaken` (`markierung_ids`) |
| `supabase/functions/lernen-api/index.ts` | Version 0.9.6: `schule_fehler_abhaken` in zwei Formen (Markieren / Zurückholen), `GET /hilfe` mit Feld `hinweis` – **vorbereitet, nicht ausgeliefert** |
| `tools/tests/wackelt_einspielen.py --ww3 [--probe]` | Pakete `tools/tests/aus/ww_s3_probe.sql` / `ww_s3_einspielen.sql` (die Ausgabe ohne `--ww3` ist unverändert) |
| `tools/tests/wackelt_test.py`, `wackelt_gegenprobe.py` | lokal im Nachbau (keine Verbindung zur echten Datenbank) |

### Was sich ändert

1. **Einheiten ohne Thema** (Fehler 1): `auswertung.themen[].offen` verglich `o.thema_id = v.thema_id` – bei NULL nie wahr, also `offen: 0`; lagen diese Fehler jenseits der 300 neuesten in `offen[]`, fehlte das Thema in der Zählung des Clients (Beispiel der Gegenprüfung: 319 offene Fehler in sechs Themen, gezählt fünf). Jetzt überall nullsicher (`is not distinct from`): `themen[].offen`, `themen[].besprochen`, `neu_seit`, dazu „danach richtig“ an der Lernkarte (`lernziel` leer). Unverändert: `thema_id` fehlt im Eintrag (strip_nulls); in `wiederkehrend[].themen` und `einmal.themen_danach_richtig` steht `null`.
2. **Zurückholen trifft genau die gemeinte Markierung** (Fehler 2): WW-S2 nahm beim Zurückholen über `versuch_ids` **jede** gültige Markierung des Versuchs zurück. Wurde ein Fehler inzwischen zurückgeholt und neu markiert (andere Sitzung, zweites Gerät), entfernte ein Klick auf den veralteten Eintrag die neue Markierung. Jetzt: Die Analyse liefert je besprochenem Eintrag `erledigt.id` (= `schule.fehler_erledigt.id`); `schule_fehler_abhaken {zurueck: true, markierung_ids}` nimmt in **einer** UPDATE-Anweisung genau diese noch gültigen Markierungen dieses Kindes zurück. Überholte, unbekannte und fremde IDs werden übersprungen und gemeldet. Gleichzeitige Aufrufe: die zweite Anweisung wartet auf die Zeilensperre und sieht die Zeile dann als zurückgeholt (`schon zurückgeholt`).
3. **Antwort von `schule_fehler_abhaken`**: zusätzlich `stand: 3`, `geaendert_ids` (was dieser Aufruf wirklich geändert hat: `versuch_ids` beim Markieren, `markierung_ids` beim Zurückholen), beim Markieren `markierung_ids` der neu angelegten Zeilen. `geaendert` und `uebersprungen` bleiben.
3a. **Alter Rückholweg entfernt** (Auflagen aus Werkstatt 1165): `{zurueck: true, versuch_ids}` konnte nach „überholt“ für die alte Markierung die **neue** Markierung desselben Versuchs zurücknehmen. Jetzt weist `api.schule_fehler_abhaken` jede Rücknahme ohne `markierung_ids` ab („Zurückholen nur mit markierung_ids“), und der interne Helfer `schule.fehler_abhaken` hat keinen Rücknahmezweig mehr (mit `p_zurueck = true` bricht er mit derselben Meldung ab; Signatur von WW-S2 bleibt). Markieren über `versuch_ids` ist unverändert.
4. **Besprochen je Thema ohne 200er-Grenze**: `auswertung.themen[].besprochen = {zuletzt, zuletzt_tag, tage, fehler, neu_seit}`, nur wenn das Thema eine **gültige** (nicht zurückgeholte) Markierung hat; zurückgeholte Markierungen zählen nicht. `zuletzt` = späteste Markierung; `zuletzt_tag` = deren Kalendertag in der Zeitzone des Kindes (gleiche Berechnung wie `erledigt.tag`; der Client nimmt nie den Gerätetag – die Familie reist durch Zeitzonen); `fehler` = Zahl der aktuell gültig markierten Fehler des Themas insgesamt (ohne 200er-Grenze; ist `erledigt[]` voll, sieht der Client daran, ob Einträge des Themas fehlen); `tage` = Zahl verschiedener Kalendertage der Markierungen in der Zeitzone des Kindes (`schule.lernender.zeitzone`, sonst Europe/Berlin); `neu_seit` = endgültig falsche Antworten des Themas mit `am > zuletzt`, die nicht markiert sind – **unabhängig vom gewählten Zeitraum**. `themen[]` enthält weiter nur Themen mit Antworten im Zeitraum; vollständig ist die Übersicht also mit `tage: 0` (jedes besprochene Thema hat Antworten).
5. **Feste Typen** (Vertrag, im Probe-Paket geprüft): siehe Tabelle unten.
6. **Versionsfeld** `stand: 3` in der Analyse und in jeder Antwort von `schule_fehler_abhaken`. Es gibt **einen** Vertrag: mit `stand: 3` die neue Seite, ohne die alte Ansicht (siehe Client-Einbindung).

### Antwortformen WW-S3 (Beispiele mit erfundenen Daten)

`schule_wackelt_analyse {lernender_id: 2, tage: 0, erledigt: true}`:
```json
{"ok": true, "stand": 3, "lernender_id": 2, "tage": 0, "heute": "2026-11-28", "mit_fehlbild": true, "offen_zahl": 2,
 "offen": [
  {"versuch_id": 9007, "am": "2026-11-28T09:12:00+01:00", "tag": "2026-11-28", "einheit_id": 77, "lernziel": "runden",
   "aufgabe": {"id": 6100, "antworttyp": "zahl", "frage": {"text": "Runde 4,56 auf Zehntel."}, "loesung": {"wert": 4.6}},
   "antwort": {"wert": "4,5"}, "anlauf": 2, "erst_antwort": {"wert": "4,4"}, "mit_tipp": false,
   "fehlerart": {"quelle": "grund", "schluessel": "g:gerundet", "grund": "gerundet"}},
  {"versuch_id": 9002, "am": "2026-11-26T17:30:00+01:00", "tag": "2026-11-26", "thema_id": 29, "thema": "Terme umformen", "einheit_id": 31,
   "lernziel": "minusklammer", "lernkarte": "Minus vor der Klammer", "aufgabe": {"…": "wie WW-S2"}, "antwort": {"wert": "15"}, "anlauf": 2, "mit_tipp": true,
   "danach_richtig": true, "danach_richtig_am": {"lernkarte_am": "2026-11-27T16:10:00+01:00"}}],
 "auswertung": {"antworten": 140, "richtig": 117,
   "themen": [
     {"offen": 1, "gesamt": 6},
     {"thema_id": 29, "thema": "Terme umformen", "offen": 1, "gesamt": 22,
      "besprochen": {"zuletzt": "2026-11-27T19:40:00+01:00", "zuletzt_tag": "2026-11-27", "tage": 2, "fehler": 3, "neu_seit": 1}},
     {"thema_id": 24, "thema": "Brüche addieren", "offen": 0, "gesamt": 15,
      "besprochen": {"zuletzt": "2026-11-20T18:00:00+01:00", "zuletzt_tag": "2026-11-20", "tage": 1, "fehler": 4, "neu_seit": 0}}],
   "lerntage": [{"tag": "2026-11-28", "richtig": 5, "falsch": 1}],
   "wiederkehrend": [], "einmal": {"lernkarten": 2, "danach_richtig": 1, "themen_danach_richtig": [29]}},
 "erledigt": [
  {"versuch_id": 9001, "am": "2026-11-26T17:25:00+01:00", "tag": "2026-11-26", "thema_id": 29, "thema": "Terme umformen", "…": "wie offen",
   "mit_tipp": false, "erledigt": {"art": "abgehakt", "id": 412, "am": "2026-11-27T19:40:00+01:00", "tag": "2026-11-27"}}]}
```
(Der erste Eintrag in `themen` ist „Ohne Thema“: kein `thema_id`, kein `thema`.)

`schule_fehler_abhaken {lernender_id: 2, versuch_ids: [9001, 9002, 9005]}` (Markieren):
```json
{"ok": true, "stand": 3, "geaendert": 1, "geaendert_ids": [9002], "markierung_ids": [413],
 "uebersprungen": [{"versuch_id": 9005, "grund": "nicht endgültig falsch"}]}
```
(9001 war schon markiert: weder in `geaendert_ids` noch in `uebersprungen`. `geaendert_ids` ist aufsteigend; `markierung_ids[i]` ist die neue Markierung von `geaendert_ids[i]` (gleiche Länge = `geaendert`).)

`schule_fehler_abhaken {lernender_id: 2, zurueck: true, markierung_ids: [412, 398, 77, 5]}` (Zurückholen):
```json
{"ok": true, "stand": 3, "geaendert": 1, "geaendert_ids": [412],
 "uebersprungen": [{"markierung_id": 5, "grund": "nicht gefunden"},
                   {"markierung_id": 77, "versuch_id": 8800, "grund": "schon zurückgeholt"},
                   {"markierung_id": 398, "versuch_id": 9001, "grund": "überholt"}]}
```
- `grund`: `überholt` = diese Markierung ist schon zurückgeholt **und** der Versuch hat inzwischen eine neue gültige Markierung (die bleibt); `schon zurückgeholt` = zurückgeholt, keine neue; `nicht gefunden` = unbekannt **oder** Markierung eines anderen Kindes (dann ohne `versuch_id` – es wird nichts über fremde Daten verraten).
- Fehlermeldungen: `markierung_ids`: 1 bis 200 ganze Zahlen, sonst „markierung_ids: Liste mit 1 bis 200 Einträgen“ bzw. „markierung_ids: nur Zahlen“; `markierung_ids` ohne `zurueck: true` → „markierung_ids nur mit zurueck: true“; zusammen mit `versuch_ids` → „entweder versuch_ids oder markierung_ids“; `zurueck: true` ohne `markierung_ids` (auch mit `versuch_ids`) → „Zurückholen nur mit markierung_ids“; `versuch_ids` beim Markieren wie WW-S2 („versuch_ids: …“).
- **Vertrag Zurückholen:** Jede angefragte `markierung_id` steht in der Antwort GENAU EINMAL – entweder in `geaendert_ids` oder (als `markierung_id`) in `uebersprungen[]`. Doppelt angefragte IDs werden zusammengefasst (sie zählen wie eine und erscheinen einmal). `geaendert` = Länge von `geaendert_ids`.
- **Vertrag Markieren:** Jede angefragte `versuch_id` steht höchstens einmal in `uebersprungen[]` und höchstens einmal in `geaendert_ids`, nie in beiden; doppelt angefragte `versuch_ids` werden zusammengefasst. Eine schon markierte `versuch_id` steht in keiner der beiden Listen. `geaendert` = Länge von `geaendert_ids` = Länge von `markierung_ids`.
- Beide Sätze prüft das Probe-Paket bei **jedem** Markier- und Zurückholaufruf (`pg_temp.ww3_mk`, `pg_temp.ww3_zh`), auch mit doppelt genannten IDs; die Migration garantiert sie, weil `ww_versuche` bzw. `fehler_zurueckholen` die Liste zuerst eindeutig macht (`distinct`) und `uebersprungen` genau die eindeutigen IDs ohne die geänderten sind.
- **Kein Altweg:** `{zurueck: true, versuch_ids}` wird abgewiesen (früher: „bleibt aus Verträglichkeit“ – mit den Auflagen aus Werkstatt 1165 gestrichen, weil er die neue Markierung zurücknehmen konnte; kein ausgelieferter Client nutzt ihn, ausgeliefert ist lernen-api 0.9.3).

### Typen (Vertrag, damit der Client streng prüfen kann)

| Feld | Typ |
|---|---|
| `stand` (Analyse, Abhaken, Zurückholen) | Zahl `3` |
| `offen[].mit_tipp`, `erledigt[].mit_tipp` | Boolean, **immer vorhanden** |
| `offen[].danach_richtig`, `erledigt[].danach_richtig` | Boolean `true` **oder fehlt** (nie Objekt, nie Text) |
| `…danach_richtig_am` | Objekt `{aufgabe_am?, lernkarte_am?}` (Zeitpunkte als Text) oder fehlt |
| `erledigt[].erledigt` | `{art: "abgehakt", id: Zahl, am: Zeitpunkt, tag: "JJJJ-MM-TT"}` |
| `auswertung.themen[].besprochen` | fehlt (Thema nie bzw. nicht mehr gültig besprochen) oder – dann **alle Felder Pflicht** – `{zuletzt: Zeitpunkt (Text), zuletzt_tag: "JJJJ-MM-TT" (Zeitzone des Kindes), tage: ganze Zahl ≥ 1, fehler: ganze Zahl ≥ 1, neu_seit: ganze Zahl ≥ 0}` |
| `geaendert` | Zahl ≥ 0; `geaendert_ids`, `markierung_ids`: Listen ganzer Zahlen; `uebersprungen`: Liste von Objekten |

Das Probe-Paket prüft für jede Analyse-Antwort (`pg_temp.ww3_typen`), dass `mit_tipp` und `danach_richtig` nie als Text oder Objekt kommen und `besprochen` vollständig mit diesen Typen und Grenzen ist. Zeitzone: Prüffall mit einem Kind in `Pacific/Auckland` und einer Markierung um 00:05 Ortszeit (in UTC noch der Vortag) – `zuletzt_tag` und `erledigt.tag` sind der Ortstag.

### Berührt die Lernlogik nicht (WW-S3)

- **Liest** dieselben Tabellen und Funktionen wie WW-S2 (siehe oben), nichts Neues.
- **Schreibt** ausschließlich `schule.fehler_erledigt` (Markieren = insert, Zurücknehmen/Zurückholen = update von `zurueckgenommen_am/_von`) und Hilfstabellen der eigenen Sitzung (`pg_temp.ww3_v`, `pg_temp.ww3_f`, on commit drop; eigene Namen, damit eine WW-S2-Hilfstabelle derselben Transaktion nicht stört).
- **Ändert nicht**: keine Tabelle, keine Spalte, kein Index, kein Trigger, kein Fremdschlüssel (auch nicht an `fehler_erledigt`); keine Funktion außerhalb von WW-S2/WW-S3 – auch die übrigen WW-S2-Funktionen `ww_fehlerart`, `ww_von`, `ww_versuche`, `api.schule_wackelt_analyse` bleiben bytegleich. Ersetzt werden nur `schule.wackelt_analyse`, `schule.fehler_abhaken`, `api.schule_fehler_abhaken`; neu ist `schule.fehler_zurueckholen`. Kein DELETE, kein DROP, keine Datenänderung an Bestandszeilen von `fehler_erledigt` durch die Migration.
- `schule.fehler_erledigt` wird weiter von keiner Funktion der Lernlogik gelesen (Karte, Wiederholung, Check-in, Mischkarten, Sterne, Auswahl der nächsten Aufgabe).
- **Maschinell belegt** im Probe-Paket `ww_s3_probe.sql` (an der echten Datenbank, alles zurückgerollt): Fingerabdruck aller Funktionen in `schule`/`api` außer den vier von WW-S3 (Definition und Rechte), aller Trigger (auch interne) und Indizes an Tabellen in `schule` und aller Spalten vor/nach beiden Läufen gleich (`schema_bestehend_gleich`); Aufbau und Zeilen von `fehler_erledigt` durch die Migration unverändert (`fehler_erledigt_gleich`); alle Daten in `schule` außer `fehler_erledigt` gleich während Markieren/Zurückholen/api-Aufrufen und nach dem Paket (`bestand_gleich_beim_markieren`, `bestand_gleich`); Karte: Markieren → Zurückholen → neu Markieren an einer sitzenden Lernkarte ändert die Kartenzeile nicht, ein weiterer Fehler wirkt mit und ohne Markierung gleich (`karte_markierung_ohne_wirkung`). Gegenprobe: zehn verdorbene Fassungen werden abgewiesen (unten).

### Prüfung (lokal, Nachbau – keine Verbindung zur echten Datenbank), 28.11.

- `wackelt_test.py` → „WW-S2 im Nachbau bestanden“, „WW-S3 im Nachbau bestanden“: WW-S3-Probe vor WW-S2 → Abbruch „Vorbedingung“; nach WW-S2 ohne RB-S und mit RB-S „PROBELAUF bestanden“ (`fehler: 0`); Einspielen zweimal; Probe noch einmal auf dem Stand „WW-S3 eingespielt“ (`stand_vorher: 3`); Antwortformen und Rechte über die api-Aktionen.
- `wackelt_gegenprobe.py` → WW-S2 6 von 6, **WW-S3 14 von 14** (Nachträge 28.11.: `zuletzt_tag` in UTC, `besprochen` ohne `fehler`; Auflagen aus Werkstatt 1165: „Altweg wieder offen“, „Zurückholen meldet doppelte IDs zweimal“): Zurückholen ohne ID-Bindung (Parallelfall), nicht nullsicherer Vergleich (ohne Thema), Zurückholen schreibt außerhalb `fehler_erledigt`, fremde Markierung zurückholbar, `mit_tipp` als Text, besprochen zählt zurückgeholte Markierungen, Zurückholen ohne `ist_leiter`, Migration ändert eine übrige WW-S2-Funktion, Migration ändert eine Funktion außerhalb von WW, falsche `markierung_ids`, `zuletzt_tag` in UTC, `besprochen` ohne `fehler`, Altweg wieder offen, doppelte IDs zweimal gemeldet.
- `rb_ww_pakete.py --pruefen` → OK (alle rb- und WW-S2-Pakete byteidentisch); `regelbezug_sql_test.py` → bestanden; `pglast` liest die 10 Anweisungen der Migration und die 22 der Pakete.
- Probe-Fälle im Einzelnen: Typen; Markieren zweier Fehler (`geaendert_ids`, `markierung_ids` = die neuen Zeilen); zweites Markieren ändert nichts; `erledigt.id/tag`; besprochen mit zwei Gesprächstagen und einem neuen Fehler danach – gegen eine unabhängige Nachrechnung direkt aus den Tabellen (`pg_temp.ww3_bespr`), auch nach dem Zurückholen; Zurückholen über `markierung_ids`; **Parallelfall** (zurückgeholt und neu markiert → veralteter Eintrag `überholt`, neue Markierung bleibt, Fehler bleibt besprochen); doppelte IDs; `schon zurückgeholt`; fremde und unbekannte Markierung (`nicht gefunden`, ohne `versuch_id`, nichts geändert); Eingabeprüfung (leer, Komma, Text, kein Feld, 201); alter Weg; **ohne Thema** mit zwei offenen Fehlern und nach 300 neueren (beide jenseits der 300, Thema trotzdem mit `offen ≥ 2`, Summe `themen[].offen` = `offen_zahl`); Rechte (Kind, fremdes Kind, Eltern, Lehrer, unbekannte Sitzung; `von`/`zurueckgenommen_von`); Karte; Laufzeit.
- **Negativprobe Altweg** (Auflagen aus Werkstatt 1165; ersetzt den früheren positiven Altweg-Test): Versuch zurückgeholt und neu markiert → Zurückholen der alten Markierungs-ID meldet „überholt“ → danach `zurueck` + `versuch_ids` (und `zurueck` ohne Liste) → abgewiesen „Zurückholen nur mit markierung_ids“, auch beim internen Aufruf `schule.fehler_abhaken(…, true, …)`; die neue Markierung bleibt gültig. Im Probe-Paket (direkt und über die api mit Eltern-/Lehrer-Sitzung) und in `wackelt_test.py`.
- Laufzeit im Nachbau: Analyse „alles“ mit über 300 offenen Fehlern ≈ 45 ms. An der echten Datenbank misst das Probe-Paket `laufzeit_ms_testkind`, `laufzeit_ms_groesstes_kind` und `ohne_thema.laufzeit_ms_300` (Warnung über 500 ms im Bericht: `warnung` bzw. `warnung_300`).
- **Ohne Thema an der echten Datenbank:** Gibt es keine Einheit ohne Thema, stellt die Probe eine Einheit nur in ihrer zurückgerollten Untertransaktion ohne Thema (`ohne_thema.weg: "vorübergehend ohne Thema"`); lehnt die Datenbank das ab (z. B. weil `thema_id` dort Pflicht ist – dann kann der Fall live gar nicht entstehen), steht `weg: "übersprungen: …"` im Bericht, und der Fall ist nur im Nachbau belegt.

### Client-Einbindung WW-S3 (was der Client ändern muss)

| Stelle | Bisher (WW-S2) | Mit WW-S3 |
|---|---|---|
| Erkennen | – | `r.stand === 3` in der Analyse-Antwort → neue Seite. Sonst (Server ohne WW-S3, Aktion unbekannt oder Antwort unvollständig) → **alte Ansicht** (bisherige Arbeitsliste über `schule_wackelt_lesen`), keine Zwischenform. |
| „Besprochen“-Übersicht je Thema (zuletzt, Zahl der Gesprächstage, „seitdem N neue Fehler“) | aus `erledigt[]` (höchstens 200) im Client gezählt, Tag in der Zeitzone des Geräts | aus `auswertung.themen[].besprochen` der Analyse mit `tage: 0` – ohne 200er-Grenze; „besprochen am …“ aus `zuletzt_tag` (Zeitzone des Kindes, **nie** der Gerätetag – auch wenn der passende Eintrag in `erledigt[]` fehlt); `neu_seit` statt eigener Zählung |
| Vollständigkeit des Abschnitts „Besprochen“ | `erledigt[]` voll (200) → unklar, ob Einträge fehlen | je Thema: Zahl der Einträge des Themas in `erledigt[]` < `besprochen.fehler` → ältere Einträge fehlen (Hinweis zeigen; Zurückholen nur für die gezeigten) |
| Zurückholen „je Thema und Tag“ im Abschnitt „Besprochen“ | `{zurueck: true, versuch_ids}` | **nur** `{zurueck: true, markierung_ids: [erledigt.id …]}` aus `erledigt[]` (Gruppe nach Thema und `erledigt.tag`); `uebersprungen[].grund` `überholt` als „inzwischen neu besprochen – bleibt“ zeigen. `versuch_ids` beim Zurückholen weist der Server ab. |
| Bestätigung eines Pakets | `geaendert`, `uebersprungen` | zusätzlich `geaendert_ids` und beim Markieren `markierung_ids` (beide Länge = `geaendert`); Zurückholen gilt als bestätigt, wenn jede gesendete (eindeutige) `markierung_id` genau einmal in `geaendert_ids` oder `uebersprungen[].markierung_id` steht; Markieren, wenn jede `versuch_id` höchstens einmal vorkommt und keine fremde ID auftaucht |
| „Rückgängig“ direkt nach dem Markieren (bisher wegen Auflage aus Werkstatt 1158 abgeschaltet) | nicht möglich (Server nannte die geänderten IDs nicht) | möglich und sicher: `{zurueck: true, markierung_ids: <markierung_ids der Antwort>}` nimmt genau die eben gesetzten Markierungen zurück, sonst nichts |
| Formprüfung | `danach_richtig` nur als „wahr/falsch“ gelesen | streng: `mit_tipp` Boolean (Pflicht ab `stand: 3`), `danach_richtig` Boolean oder fehlt, `erledigt.id` ganze Zahl, `besprochen` wie in der Typen-Tabelle |
| Ohne Thema | – | unverändert „Ohne Thema“ (kein `thema_id`); `themen[].offen` stimmt jetzt auch dort |

**Nur ein Vertrag:** Die neue Seite gibt es ausschließlich mit `stand: 3`. Ohne `stand: 3` zeigt der Client die alte Ansicht – es gibt keinen Rückfall auf WW-S2-Formen (kein Zurückholen über `versuch_ids`, kein Lesen von `danach_richtig` als Objekt). Deshalb ist die Auslieferungsreihenfolge **fest** (unten).

Edge-Funktion `lernen-api` 0.9.6: `schule_fehler_abhaken: ['lernender_id', 'versuch_ids?', 'zurueck?', 'markierung_ids?']` und in `GET /hilfe` zusätzlich `hinweis`: „Markieren: lernender_id, versuch_ids. Zurückholen: lernender_id, zurueck = true, markierung_ids (ohne versuch_ids).“ (Die Liste prüft keine Parameter – das tut die Datenbank.)

### Reihenfolge

**Fest:** WW-S3-Probe → WW-S3 einspielen → lernen-api 0.9.6 ausliefern → App ausliefern. Keine andere Reihenfolge (die App setzt `stand: 3` voraus, lernen-api 0.9.6 setzt WW-S3 voraus). Voraussetzung: WW-S2 eingespielt (erfüllt). Unabhängig von RB-S. Schritte und Ausführungsvorschrift in `einspiel-reihenfolge-rb-ww.md` (Schritte 8–11).
