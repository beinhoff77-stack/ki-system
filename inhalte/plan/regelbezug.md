# RB-S – Regelbezug (Teil Datenbank): Regel und Fehlbild zu jeder Fehlantwort

Stand 27.11.2026, Zweig `helfer-regelbezug`. **Entwurf, nichts eingespielt.** Eingespielt wird nur nach Gegenprüfung und dem ausdrücklichen Satz des Nutzers.
Gegenprüfung: Werkstatt 1129 (Auflagen eingearbeitet, siehe Abschnitt „Nach der Gegenprüfung“). Schrittfolge zum Einspielen: `einspiel-reihenfolge-rb-ww.md`.

Anlass: Ein Kind gibt bei einer Zinseszins-Aufgabe (1 000 € zu 10 % über zwei Jahre) 1 200 statt 1 210 ein. Die Rückmeldung zeigt Lösung und Lösungsweg, aber keinen Weg zur passenden Regelkarte und keine Erklärung, *welcher* Fehler das war. Die 2 028 neuen Aufgaben tragen beides in den Dateien (`regel`, `fehlbilder`), es kam aber nie in die Datenbank.

## Lieferung

| Datei | Was |
|---|---|
| `supabase/migrations/20261204_rb_s_regelbezug.sql` | Migration (Tabellen, Erkennen, Rückmeldung, Versuch, Text-Patch) |
| `tools/tests/regelbezug_einspielen.py` | selbstprüfendes Einspiel-Paket der Migration; `--probe` rollt am Ende alles zurück |
| `tools/regelbezug_sql.py` | Nachtrags-Pakete (je Runde) für die 2 028 schon eingespielten Aufgaben; Übersicht und Abweichungsliste |
| `tools/rollend_sql.py` | künftige Runden bringen Regel/Fehlbilder gleich mit (zweiter Block; `--ohne-regelbezug` nur bis RB-S eingespielt ist) |
| `tools/regelbezug_lernkarten.py` → `inhalte/plan/regelbezug-lernkarten.json` | Zuordnung Lernkarte → Regel (Erklärkarte und Rückfall) |
| `tools/tests/regelbezug_sql_test.py`, `tools/tests/regelbezug_nachbau.sql` | Test: Zuordnung und Zählungen; dazu lokal mit leerem Postgres ein **Nachbau** (nicht die echte Datenbank) mit allen eingespielten Aufgaben: Probelauf, Einspielen, alle Nachträge zweimal, Abbruch bei veränderter Aufgabe |

Lokale Prüfungen (bestanden): `python3 -I tools/tests/rollend_sql_test.py` → OK (Sollzahlen unverändert); `python3 -I tools/tests/regelbezug_sql_test.py` → „Teil 2 (lokaler Nachbau) bestanden“, OK. SQL-Syntax: `pglast` (alle Anweisungen der Migration) und vollständige Ausführung im Nachbau unter Postgres 16 – auch die plpgsql-Rümpfe.

## Entwurfsentscheidungen

1. **Eigene Tabellen statt Spalten an `schule.aufgabe`.** `schule.aufgabe_regel (aufgabe_id PK)` und `schule.aufgabe_fehlbild (aufgabe_id, nr)`. Begründung: Alle 2 028 Aufgaben liegen in freigegebenen Einheiten; `aufgabe_schutz` verbietet dort UPDATE. Mit eigenen Tabellen wird der Aufgaben-Datensatz nicht angefasst, der Schutz bleibt ohne Ausnahme, und ein Nachtrag ist reines INSERT. Spalten hätten eine Lücke im Schutz gebraucht (und das Umschreiben einer Tabelle, die jede Übung liest). Für die eigenen Tabellen gilt derselbe Schutz (`schule.regelbezug_schutz`: kein UPDATE/DELETE bei freigegebener Einheit; Einfügen erlaubt). Berichtigung = neue Aufgabe, wie bisher.
2. **Nur eindeutig erkennbare Fehlbilder werden gespeichert.** Je Aufgabe ist (art, Lücke, Wert) eindeutig (Index). Nicht übernommen wird, was der Lösung gleicht, doppelt ist oder nie eingegeben werden kann. `nr` = Platz in der Liste der Datei (stabil, Verweis zurück auf die Datei).
3. **Erkennen (`schule.fehlbild_finden`)** normiert die Antwort wie `schule.antwort_bewerten`: Zahl innerhalb der Toleranz, Auswahl über den Index, Text ohne Leerzeichen/Groß-Klein. **Lücken: nur die erste falsche Lücke zählt** – spätere Lücken sind meist Folgefehler; ein Fehlbild an Lücke 3 wird nur erkannt, wenn Lücke 1 und 2 stimmen. Kein Treffer oder mehr als einer → nichts. Ein Fehler in der Suche ergibt „nichts“, nie eine abgewiesene Antwort.
4. **Rückmeldung nur bei endgültig falscher Antwort voll.** Beim ersten Fehlversuch (zweite Chance) nur `regel`: 56 von 2 175 Beschreibungen bei Zahl-Aufgaben enthalten die Lösungszahl, viele nennen Zwischenergebnisse („mit dem Nenner malgenommen: 56 · 8“). Nach der endgültigen Antwort kommt die Lösung ohnehin.
5. **Erkanntes Fehlbild im Versuch** über einen BEFORE-INSERT-Trigger auf `schule.versuch` (`fehlbild_nr`, `fehlbild`). So deckt ein Ort alle Schreibwege ab (Übung, Mischkarte, Expedition, Test), ohne die Einfüge-Befehle in vielen Funktionen zu patchen. Alte Versuche werden nicht nachgetragen (kein UPDATE); `schule.versuch_regelbezug(v)` rechnet sie beim Lesen nach (`nachtraeglich: true`).
6. **Zuordnung Lernkarte → Regel als statische Datei, nicht in der Datenbank.** Die Regel-Kennungen sind Inhalt wie `daten/regeln-universum.json`, ändern sich mit dem Universum, nicht mit dem Lernen. Als Datei: kein Datenbank-Schritt, kann vor RB-S live gehen, wirkt für Erklärkarte und Rückmeldung gleich, offline verfügbar. Die Datenbank hält nur, was an der *einzelnen Aufgabe* hängt (Regel der Aufgabe, Fehlbilder). Der Client nimmt `regelbezug.regel`, sonst die Hauptregel der Lernkarte aus der Datei.
7. **Text-Patch statt Neufassung von `uebung_pruefen_intern`** (Live-Definition ist das Ergebnis vieler Migrationen und steht so nicht im Repo). Vier Stellen, alle von BD-S2 hinterlassen und damit bekannt; drei Zustände (alt/fertig/sonst Abbruch), halb umgestellt = Abbruch – wie BD-S2 und FT-S.

## Datenfluss

```
Aufgaben-Datei (regel, fehlbilder)
  └─ tools/regelbezug_sql.py (Nachtrag) bzw. tools/rollend_sql.py (neue Runde)
       └─ schule.aufgabe_regel / schule.aufgabe_fehlbild   (nur Server; RLS, keine Rechte für App-Rollen)
Kind antwortet → api → uebung_pruefen_wd → uebung_pruefen_intern
  ├─ antwort_bewerten (wie bisher)
  ├─ INSERT schule.versuch → Trigger versuch_fehlbild setzt fehlbild_nr, fehlbild
  └─ Antwort + Feld „regelbezug“ (regelbezug_antwort → fehlbild_finden)
Client: Rückmeldung (Beschreibung), Knopf zur Regelkarte (regel bzw. Rückfall aus regelbezug-lernkarten.json)
„Was wackelt“ (Stufe 2): versuch.fehlbild / versuch_regelbezug(v) → Fehlvorstellung je Kennung über Themen hinweg
```

## Was der Client später braucht

Feld **`regelbezug`** in der Antwort von `schule_uebung_pruefen` (fehlt, wenn richtig oder ohne Daten):

| Feld | Typ | wann |
|---|---|---|
| `regel` | Kennung (`rr.…`/`id.…`) der Aufgabe | jede falsche Antwort, auch 1. Fehlversuch (`nochmal`) |
| `fehlbild` | Kennung `fb.…` | endgültig falsch und erkannt, wenn das Fehlbild eine Kennung hat (478 von 5 047) |
| `fehlbild_nr` | Zahl | endgültig falsch und erkannt |
| `fehlbild_regel` | Kennung | wenn in der Datei `regel_des_fehlbilds` steht |
| `text` | Beschreibung fürs Kind | endgültig falsch und erkannt |

Beispiel (2. Anlauf, Werte zusammengesetzt): `"regelbezug": {"regel": "rr.waage", "fehlbild": "fb.gleichung_loesen.grenze_mitgezaehlt", "fehlbild_nr": 2, "fehlbild_regel": "id.algebra.gleichung_loesen", "text": "die Grenze selbst genannt"}`. Wiederholte Übertragung (gleiche `client_id`) antwortet gleich.
Rückfall im Client: kein `regel` → `regelbezug-lernkarten.json` → `themen[<thema ohne _teilN>].lernkarten[<lernziel>].regel` (bei `quelle: offen` keine Regel, kein Knopf). Adresse der Regelkarte: über die Kennung im Regel-Universum (`kennungen.json` → R-Nummer bzw. Idee). Der Client muss außerdem `regelbezug-lernkarten.json` laden (oder `tools/regeln_bauen.cjs` übernimmt sie in `daten/regeln-universum.json` – Vorschlag, Client-Sache, Cache-Liste in `sw.js`).

## Zuordnung Repo-Aufgabe → Datenbank-Aufgabe (Nachtrag)

- Es gibt keine Kennung in der Datenbank. Schlüssel: **Einheit + Pool `uebung` + Reihenfolge-Nummer**. `rollend_sql.sammeln` rechnet die Nummer wie beim Einspielen: Runden 1–4 `max_r` + Platz unter allen Aufgaben der Einheit in den Runden 1–4 (Runde, Dateireihenfolge; auch herausgenommene zählen mit, deshalb bekamen die sieben Restaufgaben ihre alten Plätze); Runde R ≥ 5 `max_r + 1000·R + Platz`. `max_r` in `rollend-einheiten.json` hat sich zwischen den Fassungen nie geändert (alle vier Stände verglichen).
- Eindeutigkeit: In der Datenbank gibt es keinen eindeutigen Index auf (Einheit, Pool, Reihenfolge). Neue Aufgaben liegen in eigenen Bereichen über `max_r` und sind durch das Einspiel-SQL („Nummern noch frei“) eindeutig; **ob danach etwas anderes dort eingefügt wurde, prüft das Paket** (genau eine Aufgabe, sonst Abbruch).
- Abgleich gegen das, was wirklich eingespielt wurde: die Pakete `tools/tests/aus/rollend*_einspielen.sql` (14 Pakete, zusammen 2 028 Zeilen, kein Platz doppelt). Stimmt die Datei an diesem Platz nicht, sucht das Werkzeug in der Einheit genau eine Zeile mit gleichem Fragetext (verschobene Plätze) – heute nicht nötig.
- In der Datenbank je Aufgabe: md5 von `frage->>'text'` = md5 des **eingespielten** Texts, Antworttyp und Lernkarte gleich, bei Auswahl md5 der Optionsliste gleich, **die Lösung (`loesung`: Wert/Index/Lückenwerte, Einheit, Toleranz) gleich der eingespielten** (jsonb-Gleichheit, Meldung „Lösung … statt … wie eingespielt“). Jede Abweichung bricht das ganze Paket ab. Nach dem Einfügen wird jedes Fehlbild als Antwort nachgebaut (`fehlbild_probeantwort`): `antwort_bewerten` muss „gültig, falsch“ sagen, `fehlbild_finden` genau dieses Fehlbild finden.
- **Abweichungsliste heute: 1** – `Z2-02` (Einheit 4, Platz 660): Frage und Lösung nach dem Einspielen im Repo berichtigt. Regel wird übernommen, die 6 Fehlbilder nicht (sie gehören zur berichtigten Fassung). Kommt mit dem eigenen Schritt „Z2-02 ersetzen“.
- Pakete: `python3 -I tools/regelbezug_sql.py --runden <R> --sql` je Runde 1–13 (40–160 KB); `--probe` rollt zurück. Ein zweiter Lauf fügt nichts ein (Meldung „0 Regeln neu, 0 Fehlbilder neu“); steht etwas anders da → Abbruch.

## Zählungen (2 028 eingespielte Aufgaben, Runden 1–13)

- Mit `regel`: **1 795**; ohne: 233 (Runden 6, 9, 10, 11, 12, 13).
- Fehlbilder in den Dateien: **5 061**, davon mit Kennung **479**. Übernehmbar: **5 047** (mit Kennung 478). Nicht übernommen: 8 (Lücken-Fehlbild mit Dezimalzahl – Lücken nehmen nur ganze Zahlen), 6 (Z2-02).
- Eindeutig einer Antwort zuordenbar je Antworttyp:

| Antworttyp | Aufgaben | Fehlbilder | eindeutig zuordenbar |
|---|---|---|---|
| zahl | 879 | 2 175 | 2 175 |
| auswahl | 636 | 1 635 | 1 635 (Index gültig, Optionstext passt überall) |
| luecken | 431 | 1 247 | 1 233 (8 Dezimal, 6 Z2-02) |
| text | 2 | 4 | 4 |
| bedingung | 80 | 0 | – |

- Je Runde (Aufgaben / mit Regel / Fehlbilder / übernommen / mit Kennung): 1: 76/76/165/159/50 · 2: 116/116/214/214/63 · 3: 127/127/241/241/56 · 4: 314/314/777/777/13 · 5: 174/174/381/381/38 · 6: 198/142/534/534/0 · 7: 183/183/464/464/140 · 8: 156/156/350/349/0 · 9: 174/149/524/521/18 · 10: 108/98/300/296/54 · 11: 60/42/170/170/0 · 12: 210/106/575/575/24 · 13: 132/112/366/366/22.

## Lernkarte → Regel (Erklärkarte und Rückfall für Aufgaben ohne Regel)

Datei `inhalte/plan/regelbezug-lernkarten.json` (erzeugt, `--pruefen` im Test). Regel, erste greifende gewinnt; nichts wird geraten:
1. **aufgaben**: mindestens 2 neue Aufgaben der Lernkarte tragen eine Regel und die häufigste hat mindestens 2/3 davon → Hauptregel; weitere (≤ 2): andere Regeln mit mindestens 2 Aufgaben.
2. **thema**: das Thema steht in der Themenliste (`kennungen.json` → `themen`) genau einer Kennung und keine Aufgabe der Lernkarte trägt eine andere → diese Regel.
3. **offen**: sonst keine Regel; Eintrag in `redaktion` mit Grund und Kandidaten.

| | Lernkarten | aus Aufgaben | aus Thema | offen |
|---|---|---|---|---|
| Klasse 5 (gym_by) | 112 | 107 | 0 | 5 |
| Klasse 8 (gym_by) | 103 | 83 | 0 | 20 |
| übrige | 460 | 226 | 133 | 101 |
| **gesamt** | **675** | **416** | **133** | **126** |

Themen (97) nach Themenliste: 49 bei genau einer Regel, 44 bei mehreren, 4 bei keiner. Auf die Bestandsaufgaben in `inhalte/themen/*.json` umgelegt (26 458): 16 244 bekommen eine Regel über „aufgaben“, 5 213 über „thema“, 5 001 keine. Weitere Regeln: nur 9 Lernkarten haben eine zweite. Gründe für „offen“: Thema bei 2–8 Regeln ohne genug Aufgaben (82), Aufgaben uneinig (23), Thema in keiner Themenliste (20), Widerspruch (1).

## Risiken

- **Live-Definition von `uebung_pruefen_intern` unbekannt.** Der Patch erwartet die BD-S2-Stellen genau 4/1/1/1-mal; sonst Abbruch (nichts passiert). Ob jede der vier endgültigen Rückgaben `p_daten->'antwort'` bewertet hat (Mischkarte/Expedition/Bonus), ist nicht gesehen – der Probelauf prüft nur den normalen Übungsweg.
- **Sperre:** `alter table schule.versuch` hält die Tabelle bis zum Ende der Transaktion – Nutzungspause, `lock_timeout 3s`.
- **„thema“-Quelle ist schwach:** Die Themenlisten von `kennungen.json` sind „Themen der Beispiele“; eine einzige Regel am Thema heißt nicht, dass jede Lernkarte dazu gehört (133 Lernkarten). Klasse 5/8 betrifft das nicht.
- **Lücken-Regel „erste falsche Lücke“** übersieht ein Fehlbild an einer späteren Lücke, wenn davor schon etwas falsch ist (bewusst: lieber keins als ein falsches).
- Die Beschreibungen sind für Lehrer geschrieben, nicht immer kindgerecht („Fehler-Detektiv“-Zeilen sind Erklärungen, keine Vorwürfe – gut; einige sind sehr knapp: „150 : 5 gerechnet“).

## Nach der Gegenprüfung (Werkstatt 1129)

- **Entschieden vom Nutzer:** Fehlbild-Text erst nach der endgültigen Antwort (so gebaut).
- **Lösungsvergleich** im Nachtrag ergänzt (siehe Zuordnung); Test im Nachbau: veränderte Toleranz bei gleichem Text → Abbruch mit Kennung. Auf der Repo-Seite steht eine Lösungs-Abweichung (Feld `o`) ohnehin in der Abweichungsliste (heute nur Z2-02).
- **Trigger auf `schule.versuch`** (live laut Vorprüfung: `versuch_hilfe_merken` BEFORE INSERT; `versuch_karte`, `versuch_lerntag`, `versuch_misch_verfall`, `versuch_sterne` AFTER INSERT): `versuch_fehlbild` läuft als erster BEFORE-Trigger (Namensreihenfolge f < h) und liest nur `richtig`, `aufgabe_id`, `antwort` – nichts, was `versuch_hilfe_merken` setzt. Das Probe-Paket prüft die Reihenfolge, dass alle übrigen Trigger auf `versuch`/`aufgabe` unverändert sind, und vergleicht vor/nach der Migration die gespeicherten Versuch-Zeilen (ohne id/am/fehlbild), die Karte und die Sterne des Testkinds an derselben Aufgabe.
- **Gegenprobe mit `set local role authenticated`:** `authenticated` hat live kein `usage` auf `schule`; die Probe gibt es in einer zurückgerollten Untertransaktion vorübergehend und verlangt dann den Fehler an der **Tabelle** (nicht am Schema) – sonst bestünde sie aus dem falschen Grund.
- Lesende Vorprüfung live: Patch-Stellen 4/1/1/1, Spalten von `schule.versuch` wie erwartet (ohne `fehlbild*`), keine Default-ACL, `council_mcp` vorhanden. Der doppelte Platz (Einheit 61, Reihenfolge 107) liegt im Alt-Bestand einer Einheit, die kein Paket berührt.

## Offene Fragen (mit Vorschlag)

1. ~~Fehlbild-Text schon beim ersten Fehlversuch?~~ Entschieden: nein.
2. Regel auch bei **richtiger** Antwort mitschicken (Knopf „Regel dazu“ immer)? – Vorschlag: nein im Server; der Client kennt die Regel der Lernkarte aus der Datei und kann den Knopf ohnehin zeigen.
3. Rückfall „thema“ (133 Lernkarten außerhalb Klasse 5/8) verwenden oder nur „aufgaben“? – Vorschlag: verwenden, aber die 126 „offen“ und die 133 „thema“ vom Mathe-Profi in einem Durchgang bestätigen lassen (Liste `redaktion`).
4. Die 8 Lücken-Fehlbilder mit Dezimalzahl: Daten- oder Formfehler? – Vorschlag: an den Mathe-Profi (K9A-V073, K9A-V046, K9A-V121, K9B-V025, K9B-V067, K9B-V070, K9B-V052, K7-V139); bis dahin weggelassen.
5. Einspiel-Reihenfolge: erst Migration (Nutzungspause), dann die 13 Nachträge, dann Client. – Vorschlag: so; der Client kann vorher schon die Datei-Zuordnung für die Erklärkarte nutzen.

## Nicht geprüft (keine Datenbank) – vorab beim Projektleiter laufen lassen

1. Stellen in der Live-Funktion: `select (length(d) - length(replace(d, x, ''))) / length(x) from (select pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure) d) f, unnest(array[$a$'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'loesung', schule.loesung_sicht(a)$a$, $a$'richtig', false, 'nochmal', true, 'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis'));$a$, $a$'wiederholt', true) || jsonb_strip_nulls(jsonb_build_object('verletzt', b->>'verletzt', 'hinweis', b->>'hinweis'));$a$, $a$'nochmal', true, 'wiederholt', true, 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis'));$a$]) x;` → erwartet **4, 1, 1, 1**. Dazu ansehen, ob die vier endgültigen Rückgaben `b` aus `p_daten->'antwort'` haben.
2. Spalten: `select attname, format_type(atttypid, atttypmod) from pg_attribute where attrelid = 'schule.versuch'::regclass and attnum > 0 and not attisdropped;` – `antwort jsonb`, `richtig boolean`, `aufgabe_id bigint`; keine Spalte `fehlbild*` vorhanden. Ebenso für `schule.aufgabe`: `antworttyp, frage, antworten, loesung, reihenfolge, pool, variante_gruppe, einheit_id`.
3. Trigger auf `schule.versuch` und `schule.aufgabe`: `select tgrelid::regclass, tgname, pg_get_triggerdef(oid) from pg_trigger where tgrelid in ('schule.versuch'::regclass, 'schule.aufgabe'::regclass) and not tgisinternal;` – kein Trigger, der INSERT auf `versuch` umschreibt; `aufgabe_schutz` nur UPDATE/DELETE.
4. Eindeutigkeit des Schlüssels: `select einheit_id, reihenfolge, count(*) from schule.aufgabe where pool = 'uebung' group by 1, 2 having count(*) > 1;` – für die Plätze der Pakete muss es leer sein (das Paket prüft es ohnehin).
5. Rollen und Standardrechte im Schema `schule`: `select has_schema_privilege('authenticated', 'schule', 'usage'), (select count(*) from pg_default_acl where defaclnamespace = 'schule'::regnamespace);` – die Migration entzieht Rechte ausdrücklich; die Gegenprobe mit `set local role authenticated` braucht, dass der ausführende Benutzer diese Rolle setzen darf.
6. Dauer: ein Nachtrag macht je Aufgabe einige Abfragen und je Fehlbild zwei Bewertungen – Runde 4 (314 Aufgaben, 777 Fehlbilder) zuerst mit `--probe` messen.
