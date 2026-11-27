# WW-S2 – „Was wackelt“, Teil Datenbank (zu Entwurf 4), schlanke Fassung

Stand 27.11.2026, Zweig `helfer-ww2`. **Entwurf, nichts eingespielt.** Schrittfolge: `einspiel-reihenfolge-rb-ww.md`. Vorlage: `inhalte/design/wackelt/entwurf4/umsetzung4.md` (vom Nutzer freigegeben), dazu `entwurf3/umsetzung3.md` Abschnitte 2 (Regeln fürs Verschwinden) und 3 (Datenbedarf).

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
| Meldung „Rückgängig“ (5 s) | `schule_fehler_abhaken {lernender_id, versuch_ids, zurueck: true}` | `geaendert` |
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
