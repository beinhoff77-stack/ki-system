# Einspielen RB-S und WW-S2 – Schrittfolge für den Projektleiter

Stand 28.11.2026. **WW-S2 (Schritte 4–5) ist seit 27.11. eingespielt**; neu sind die Schritte 8–10 für **WW-S3** (Zweig `helfer-ww3`, nicht eingespielt; Plan: `wackelt-server.md`, Abschnitt WW-S3). Ursprünglich Zweig `helfer-ww2`. Gegenprüfung RB-S: Werkstatt 1129. **WW-S2** = WW-S ohne Nachüben (Entscheidung des Nutzers 27.11.: Wiederholungs- und Mischkarten bleiben, wie sie sind) – nur Analyse und Abhaken, siehe `wackelt-server.md`; die WW-Dateien unten sind neu erzeugt, die RB-S-Dateien byteidentisch. **Jeder echte Schritt nur mit dem ausdrücklichen Satz des Nutzers.** Vorher `werkstatt_sperre`, nachher `werkstatt_aenderung`.

Technik: Jede Datei unter `tools/tests/aus/` ist **ein** Schritt – eine SQL-Datei, in **einem** `execute` lauffähig (kein psql-Meta, kein eigenes BEGIN/COMMIT, alle unter 1,5 MB). Holen per `net.http_get` von raw.githubusercontent.com (Zweig `helfer-ww2`, nach dem Merge `lernen-app`), md5 gegen die Tabelle unten prüfen, im `do`-Block per `execute` ausführen. Probe = derselbe Block mit `raise exception` am Ende; für die beiden Migrationen gibt es zusätzlich eigene Probe-Dateien (`*_probe.sql`), die selbst zurückrollen und einen Bericht melden. Im lokalen Nachbau sind alle Dateien genau so gelaufen (Test `regelbezug_sql_test.py`, `wackelt_test.py`: Inhalt in `do $…$ begin execute …; end $…$;`).
Die Dateien erzeugt `python3 -I tools/tests/rb_ww_pakete.py` (der Test prüft, dass sie auf dem Stand sind). Ändert sich eine Aufgaben-Datei oder Migration, ändern sich Dateien und md5 – dann diese Tabelle neu erzeugen.

## Schritte

| Nr | Schritt | Datei | Erwartet | Abbruch, wenn |
|---|---|---|---|---|
| 0 | Nutzungspause prüfen | – | `select count(*) from schule.versuch where am > now() - interval '15 minutes';` = 0, kein Kind angemeldet (`select count(*) from schule.lern_sitzung where zuletzt > now() - interval '15 minutes';`) | ein Kind übt gerade |
| 1 | Probe RB-S | `rb_s_probe.sql` | Fehler „PROBELAUF bestanden, ALLES zurückgerollt …“ mit `"fehler": 0`, `"bestand_gleich": true`, `trigger_versuch` beginnt mit `versuch_fehlbild`, `versuch_hilfe_merken` dahinter | jede andere Meldung („RB-S ABBRUCH …“, „weder im alten noch im fertigen Zustand“, Sperre nach 3 s) |
| 2 | RB-S echt | `rb_s_einspielen.sql` | Hinweis „RB-S eingespielt: …“, `"fehler": 0`; danach `select to_regclass('schule.aufgabe_fehlbild'), (select count(*) from schule.aufgabe_fehlbild);` = Tabelle, 0 | jede Ausnahme (dann ist nichts geändert) |
| 3 | Nachträge rundenweise, je erst Probe (Block + `raise exception`), dann echt | `rb_nachtrag_r01.sql` … `rb_nachtrag_r13.sql` (Reihenfolge egal) | Hinweis „RB-S Regelbezug: N Aufgaben, R Regeln neu, F Fehlbilder neu“ mit den Zahlen der Tabelle unten; ein zweiter Lauf: „0 Regeln neu, 0 Fehlbilder neu“ | „RB-S Regelbezug ABBRUCH …“ (Liste der Kennungen: Platz leer/doppelt, Text/Typ/Lernkarte/Optionen oder **Lösung** anders als eingespielt, Fehlbild nicht wiedererkannt) – Liste an den Helfer, nicht von Hand berichtigen |
| 4 | Probe WW-S2 | `ww_s_probe.sql` | „PROBELAUF bestanden …“ mit `"fehler": 0`, `"schema_bestehend_gleich": true`, `"bestand_gleich": true`, `"bestand_gleich_beim_abhaken": true`, `karte_abhaken_ohne_wirkung` (mit und ohne Abhaken gleiche Zustände), `laufzeit_ms_testkind`, `laufzeit_ms_groesstes_kind` (Warnung im Bericht, wenn über 500 ms – dann vor Schritt 5 melden) | „WW-S ABBRUCH …“ |
| 5 | WW-S2 echt | `ww_s_einspielen.sql` | Hinweis „WW-S eingespielt: …“, `"fehler": 0`, `"bestand_gleich": true`; danach `select to_regclass('schule.fehler_erledigt'), (select count(*) from schule.fehler_erledigt), to_regclass('schule.nachueben');` = Tabelle, 0, leer | jede Ausnahme |
| 6 | Edge-Funktion `lernen-api` 0.9.5 | `supabase/functions/lernen-api/index.ts` (zwei Einträge in `AKTIONEN`: `schule_wackelt_analyse`, `schule_fehler_abhaken`) | vorher mit der ausgelieferten Fassung 0.9.3 vergleichen; nach dem Ausliefern `GET /lernen-api/hilfe` meldet 0.9.5 und listet die zwei Aktionen, keine `schule_nachueben_*` | Unterschied zur ausgelieferten Fassung außer den zwei Zeilen, den Kopfkommentaren und der Version |
| 7 | App | Client-Stellen: `regelbezug.md` („Was der Client später braucht“), `wackelt-server.md` („Client-Einbindung (noch zu bauen)“) | – | – |
| 8 | Probe WW-S3 (Pause wie Schritt 0) | `ww_s3_probe.sql` | „PROBELAUF bestanden …“ mit `"fehler": 0`, `"stand_vorher": 2`, `"schema_bestehend_gleich": true`, `"fehler_erledigt_gleich": true`, `"bestand_gleich": true`, `"bestand_gleich_beim_markieren": true`, `"typen_ok": true`, `parallelfall.antwort.uebersprungen[0].grund` = „überholt“, `ohne_thema` (`weg`, `offen_ohne_thema ≥ 2`, `jenseits_300: true`), `besprochen_beispiel` (`tage: 2`, `fehler: 2`, `zuletzt_tag`), `zeitzone` (`zuletzt_tag` = Ortstag, ≠ `utc_tag`), `karte_markierung_ohne_wirkung` (mit und ohne gleich), Laufzeiten; kein `warnung`/`warnung_300` (sonst vor Schritt 9 melden). Hinweise `hinweis_*` melden (kein Abbruch) | „WW-S3 ABBRUCH …“ (auch „Vorbedingung: WW-S2 ist nicht eingespielt“) |
| 9 | WW-S3 echt | `ww_s3_einspielen.sql` | Hinweis „WW-S3 eingespielt: …“, `"fehler": 0`, `"bestand_gleich": true`, `"fehler_erledigt_gleich": true`; danach `select to_regprocedure('schule.fehler_zurueckholen(bigint, jsonb, text)'), (schule.wackelt_analyse((select id from schule.lernender where ist_test order by id limit 1), 0, false))->'stand';` = Funktion, 3 | jede Ausnahme (dann ist nichts geändert) |
| 10 | Edge-Funktion `lernen-api` 0.9.6 (statt 0.9.5; 0.9.5 nie ausgeliefert) | `supabase/functions/lernen-api/index.ts` | gegenüber der ausgelieferten 0.9.3: die zwei Einträge `schule_wackelt_analyse`, `schule_fehler_abhaken` (mit `markierung_ids?`), Kopfkommentare, Version; `GET /lernen-api/hilfe` meldet 0.9.6 | weiterer Unterschied |
| 11 | App | `wackelt-server.md` („Client-Einbindung WW-S3“) | – | – |

WW-S2 ist unabhängig von RB-S (Schritte 4–5 gehen auch vor 1–3; ohne RB-S meldet die Analyse `mit_fehlbild: false`). Die Nachträge (Schritt 3) brauchen RB-S (Schritt 2), sonst bricht jede Datei mit „erst die Migration … einspielen“ ab.
Ein Nachtrag sperrt nur die neuen Tabellen (Einfügen) – keine Nutzungspause nötig. Schritt 2 ändert `schule.versuch` (sperrt die Tabelle bis zum Ende der Transaktion) – nur in der Pause. Schritt 5 legt nur `schule.fehler_erledigt` und neue Funktionen an (kein Fremdschlüssel, keine Sperre an `schule.versuch`); die Fingerabdrücke lesen aber alle `schule`-Tabellen – trotzdem in der Pause, damit `bestand_gleich` nicht an einer gleichzeitigen Antwort scheitert.

## Dateien, md5 und erwartete Zahlen

| Datei | Bytes | md5 | erwartet |
|---|---|---|---|
| `tools/tests/aus/rb_s_probe.sql` | 42 397 | `4891c0306ea947f4029e5d745dd1a400` | Meldung „PROBELAUF bestanden …“ mit "fehler": 0 |
| `tools/tests/aus/rb_s_einspielen.sql` | 42 340 | `531e23d9790ccc68d8aba3a00d2d06ff` | Hinweis „RB-S eingespielt: …“, "fehler": 0 |
| `tools/tests/aus/rb_nachtrag_r01.sql` | 56 397 | `591ece09fa7f2c402c2be2751f625f56` | 76 Aufgaben, 76 Regeln neu, 159 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/rb_nachtrag_r02.sql` | 78 070 | `2fb440ef88de115075c6ac692df499bb` | 116 Aufgaben, 116 Regeln neu, 214 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/rb_nachtrag_r03.sql` | 82 758 | `171022193c6bb7e6ea8aeadc3ead33cb` | 127 Aufgaben, 127 Regeln neu, 241 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/rb_nachtrag_r04.sql` | 173 831 | `bde4a0d9d92647369947b71a65132ade` | 314 Aufgaben, 314 Regeln neu, 777 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/rb_nachtrag_r05.sql` | 88 381 | `70ea693476f0b3c545a5667a3025f764` | 174 Aufgaben, 174 Regeln neu, 381 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/rb_nachtrag_r06.sql` | 117 204 | `137fae481001e20974bfa434f4d5e7a7` | 198 Aufgaben, 142 Regeln neu, 534 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/rb_nachtrag_r07.sql` | 108 477 | `5b58fb7f44ea9040549329276c0a2cbb` | 183 Aufgaben, 183 Regeln neu, 464 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/rb_nachtrag_r08.sql` | 84 238 | `5c090084e4c71e612ad487e89aaacfa3` | 156 Aufgaben, 156 Regeln neu, 349 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/rb_nachtrag_r09.sql` | 115 602 | `30b9208be7c01f1111aefdacbcb3420a` | 174 Aufgaben, 149 Regeln neu, 521 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/rb_nachtrag_r10.sql` | 72 410 | `974a130ff2b8852ecfa8df26c1956645` | 108 Aufgaben, 98 Regeln neu, 296 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/rb_nachtrag_r11.sql` | 43 108 | `d3744a23f62258a7a92b70585ae6db67` | 60 Aufgaben, 42 Regeln neu, 170 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/rb_nachtrag_r12.sql` | 127 142 | `c54e233eb300ded02d40f95b889ff7b3` | 210 Aufgaben, 106 Regeln neu, 575 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/rb_nachtrag_r13.sql` | 87 423 | `05600fafc761fbb3d8682109dc67b13d` | 132 Aufgaben, 112 Regeln neu, 366 Fehlbilder neu (zweiter Lauf: 0 und 0) |
| `tools/tests/aus/ww_s_probe.sql` | 43 993 | `634a542eb3f3f2e5b1515555c7495bf8` | Meldung „PROBELAUF bestanden …“ mit "fehler": 0 |
| `tools/tests/aus/ww_s_einspielen.sql` | 43 936 | `6f8d5357c97e3a5761c9c0f437f8afea` | Hinweis „WW-S eingespielt: …“, "fehler": 0 |
| `tools/tests/aus/ww_s3_probe.sql` | 66 412 | `fd0982dd7500d995a7fa91378dff171a` | Meldung „PROBELAUF bestanden …“ mit "fehler": 0 |
| `tools/tests/aus/ww_s3_einspielen.sql` | 66 356 | `8095a4acc4483732a2dace549a5f5a5e` | Hinweis „WW-S3 eingespielt: …“, "fehler": 0 |

Alle Zeilen bis `ww_s_einspielen.sql` sind gegenüber dem Stand vom 27.11. **byteidentisch** (gleiche Bytes und md5; `rb_ww_pakete.py --pruefen` → OK). Quelle von WW-S3: `supabase/migrations/20261206_ww_s3_wackelt.sql` (18 660 Bytes, md5 `750003ec99d49901a4b4f1c532f019cb`; Nachtrag 28.11.: `besprochen.zuletzt_tag` und `besprochen.fehler`).
WW-S3 sperrt nichts an `schule.versuch` (nur `create or replace` von Funktionen); wie bei Schritt 5 trotzdem in der Nutzungspause, weil die Probe Antworten des Testkinds anlegt (zurückgerollt) und die Fingerabdrücke alle `schule`-Tabellen lesen. Die Probe legt in ihrer Untertransaktion bis zu 302 falsche Antworten des Testkinds an (für „ohne Thema jenseits der 300“) – alles zurückgerollt; die Dauer steht im Bericht nicht einzeln, die Zeitgrenze des Pakets ist 120 s.

Zusammen nach Schritt 3: **1 795 Regeln, 5 047 Fehlbilder** an 2 028 Aufgaben (Z2-02: Regel ja, Fehlbilder nein – Abweichung Datei/eingespielt).
Prüfabfrage danach: `select (select count(*) from schule.aufgabe_regel), (select count(*) from schule.aufgabe_fehlbild), (select count(*) from schule.aufgabe_fehlbild where fehlbild is not null);` → 1795, 5047, 478.
