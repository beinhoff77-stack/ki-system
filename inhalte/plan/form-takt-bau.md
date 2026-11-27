# Form-Takt – Bau Datenbank (FT-S), Bericht

Stand 27.11.2026. Helfer „Bau Server“. **Nur Dateien, nichts eingespielt, keine Datenbank gesehen.** Vorgabe: `inhalte/plan/form-takt.md`.

Dateien:
- `supabase/migrations/20261203_ft_s_form_takt.sql` – Migration
- `tools/tests/form_takt_einspielen.py` – erzeugt das selbstprüfende Einspiel-Paket (`--probe` = Probelauf mit Abbruch am Ende)
- `tools/tests/form_takt_anker.py` – rekonstruiert die heutigen Funktionstexte aus den Migrationsdateien und zählt die Anker
- `tools/rollend_sql.py` – Werkzeug für die Vorrats-Aufgaben (form, zaehlt, `--mit-bedingung`)

## (a) Entwurf in einfachen Worten

- Jede Aufgabe bekommt zwei neue, freiwillige Angaben: **form** (welche neue Form, leer = Bestand) und **zaehlt** (ja/nein, leer = ja). Falsche Werte lehnt die Datenbank ab.
- **Eine kleine Funktion entscheidet überall, ob eine Aufgabe zählt** (`schule.aufgabe_zaehlt`). Eine Aufgabe mit `zaehlt = nein` wird bewertet und gespeichert, aber an der Lernkarte ändert sich gar nichts: keine eigene Lösung, kein Typ, keine schwere Aufgabe, die Folge wird weder länger noch unterbrochen. Wiederholung und Mischkarte ziehen solche Aufgaben nie. Ziel, Typen und „schwer nötig“ rechnen nur mit zählenden Aufgaben.
- **Sachaufgaben-Pflicht:** Eine Lernkarte landet nur, wenn unter ihren gezählten Aufgaben eine Sachaufgabe ist (Typ `einkleidung`, `transfer`, `pruefung`). Die Pflicht gilt nur, wenn die Lernkarte überhaupt eine freigegebene, zählende Sachaufgabe hat, und nur für Karten, die noch **nie** gelandet sind. Was sitzt, bleibt sitzen; auch wieder geöffnete und gesetzte Karten bekommen keine neue Hürde.
- **Takt:** Die Datenbank wählt nichts aus. Sie liefert der App `form`/`zaehlt` je Aufgabe, die Regel `form_jede` (3) und je Lernkarte die Zahl der bisherigen Bearbeitungen. Daraus wählt die App jede dritte Aufgabe in neuer Form.
- Eingebaut wird wie bei BD-S2: neue Hilfsfunktionen neu angelegt, bestehende Funktionen nur an genau gezählten Stellen umgeschrieben (Text-Patch mit drei Zuständen). Ein zweiter Lauf ändert nichts.

### Entscheidung „anwenden erfüllt“: abgeleitet, keine neue Spalte
`schule.karte_anwenden_ok(k)` schaut in `karte_stand.gezaehlt` (die schon vorhandene Liste der Aufgaben, die als eigene Lösung gezählt haben) nach einer Aufgabe der Art „anwenden“, die zählt. Gründe:
- `gezaehlt` ist genau die Menge der gezählten Aufgaben (Regel 6 spricht von „unter den gezählten Aufgaben“). Mit Regel 5 kommt eine Aufgabe mit `zaehlt = nein` dort nie hinein.
- **Nachrechnen:** `folge_nachrechnen` rechnet nur die Folge nach und lässt `gezaehlt` stehen; eine Spalte müsste man mitnachrechnen, die Ableitung nicht.
- **Wiederlandung:** Beim Wiederöffnen bleibt `gezaehlt` erhalten (H3), und für schon einmal gelandete Karten gilt die Pflicht ohnehin nicht (`sitzt_am` gesetzt).
- **Bestand:** Kinder, die schon vor dem Einspielen eine Sachaufgabe gelöst haben, bekommen sie angerechnet. Eine neue Spalte mit Vorgabe false hätte das nicht gekonnt (oder ein Massen-UPDATE gebraucht, das ausgeschlossen ist).
- Kosten: eine kleine Abfrage über die Schlüssel von `gezaehlt` (je Karte höchstens einige Dutzend) bei jeder Buchung und Ausgabe.
- Nachteil: Wird eine Aufgabe später umgetypt oder auf `zaehlt = nein` gesetzt, ändert sich die Ableitung für noch nicht gelandete Karten mit (nie für gelandete).

### Entscheidung Takt: `versuche` genügt nicht, neues Feld `bearbeitungen`
`einheit_lesen_intern` liefert je Übung `versuche` = Zahl der Versuchszeilen. Daraus ist der Platz nicht sauber ableitbar: Zwei Anläufe an derselben Aufgabe sind zwei Zeilen, aber **eine** Bearbeitung; Mischkarten-Versuche an Aufgaben dieser Karte stehen mit drin. Deshalb neu `schule.karte_bearbeitungen(kind, einheit, lernziel)` = Übungsversuche ohne Test, ohne Mischkarte, ohne zweiten Anlauf (`anlauf = 2` zählt nicht extra). Zählt über Sitzungen und Geräte, auch Aufgaben mit `zaehlt = nein` (sie belegen einen Platz), und auch Antworten in der Wiederholung dieser Karte. Geliefert in `etappen_stand[lernziel]` (Flug lesen) und in `karte` (nach jeder Antwort).

## (b) Je Funktion: Quelle der heutigen Fassung und Patches

Rekonstruiert von `tools/tests/form_takt_anker.py` (Einspiel-Reihenfolge am 22.11. nach den Dateiköpfen: WD-S 2, WD-S 3, WD-4b, WD-S 4, FP-S, FP-S 2, FP-S 3; sonst nach Dateiname). „Grundfassung“ = jüngste vollständige `create or replace`.

| Funktion | Grundfassung | danach angewandte Text-Patches (Dateien) | FT-S-Patch |
|---|---|---|---|
| `aufgabe_anzeige` | 20261118_w150_f | – | form, zaehlt in die Ausgabe |
| `aufgaben_einfuegen` | 20261118_w150_f | – | Spalten form, zaehlt aus `x->>'form'`, `x->>'zaehlt'` |
| `karte_buchen` | 20261119_w176_h_muss | ab_s_abschluss (3), lb3_nachbesserung (4) | Rücksprung, wenn die Aufgabe nicht zählt |
| `misch_buchen` | 20261120_i3 | i4, wd_s, wd_s3, fp_s3, fp_s4 | Rücksprung, wenn die Aufgabe nicht zählt |
| `expedition_buchen` | 20261125_ex_s | – | kein `angewandt_am`, kein „fällig machen“ für nicht zählende; Sterne für die geschaffte Expedition unverändert |
| `karte_landet` | 20261120_lb3_nachbesserung | – | Sachaufgaben-Pflicht |
| `karte_ziel` | 20261116_w150_sitzt_regel_6 | – | nur zählende Übungen |
| `karte_typen_noetig` | 20261118_w176_t1 | – | nur zählende Übungen |
| `karte_schwer_noetig` | 20261116_w150_sitzt_regel_6 | – | nur zählende Übungen |
| `folge_nachrechnen` | 20261120_i2 | – | nur zählende Versuche |
| `landung_zaehlen` | 20261120_ab_s | – | beide Abfragen nur zählende Versuche (Landungs-Art, Bonus) |
| `wdh_aufgabe_waehlen` | 20261122_wd_s3 | – | nur zählende Aufgaben (gilt für Wiederholung UND Mischkarte, `mischkarten_waehlen` ruft sie) |
| `wdh_aufgabe_da(bigint, bigint, text)` | 20261122_wd_s4 | – | nur zählende Aufgaben |
| `wdh_aufgabe_da(bigint, text)` | 20261122_wd_s | – | nur zählende Aufgaben |
| `uebung_pruefen_intern` | 20261116_w150_r2 | sitzt_regel_6, w150_f, w176_a, t1, t3, t4, h_muss, h_sollte, ab_s, i2, lb3_nachbesserung, bd_s2 | `karte`: anwenden_noetig, anwenden_ok, bearbeitungen |
| `etappen_stand` | 20261114_w150_lernkarten_meisterschaft | r3, sitzt_regel_6, t1, t3, h_muss | anwenden_noetig, anwenden_ok, bearbeitungen |
| `einheit_lesen_intern` | **nicht im Repo** (Teil-Rekonstruktion aus den Patches lernkarten_meisterschaft, w150_f, t3, h_sollte, ab_s, i2, i3, lb3_kann, lb3_nachbesserung) | – | form_jede |

Neu (create or replace, Rechte entzogen für public, anon, authenticated): `aufgabe_zaehlt(aufgabe)`, `aufgabe_anwenden(aufgabe)`, `karte_anwenden_noetig(bigint, text)`, `karte_anwenden_pflicht(karte_stand, bigint, text)`, `karte_anwenden_ok(karte_stand)`, `karte_bearbeitungen(bigint, bigint, text)`. Für `form_jede` wird das vorhandene `schule.wd_regel` genutzt.

## (c) Tabelle ALLER Anker (zum Zählen gegen die Live-Datenbank)

19 Anker in 17 Funktionen. Gezählt wird im Text von `pg_get_functiondef(...)`, so wie es das Paket tut: `(length(d) - length(replace(d, alt, ''))) / length(alt)`. Erwartet ist der Zustand „alt“; „neu“ muss 0-mal vorkommen. ⏎ = Zeilenumbruch (kommt nicht vor). Erzeugt mit `python3 -I tools/tests/form_takt_anker.py --tabelle`.

| Nr | Funktion (Signatur) | alter Text (wörtlich) | erwartet | Rekonstruktion |
|---|---|---|---|---|
| 1 | `schule.aufgabe_anzeige(schule.aufgabe, boolean)` | `'typ', a.typ, 'bonus'` | 1 | voll (20261118_w150_f_stufen_typ_bonus.sql) |
| 2 | `schule.aufgaben_einfuegen(bigint, jsonb)` | `reihenfolge, pool, typ)` | 1 | voll (20261118_w150_f_stufen_typ_bonus.sql) |
| 3 | `schule.aufgaben_einfuegen(bigint, jsonb)` | `x->>'g' from q` | 1 | voll (20261118_w150_f_stufen_typ_bonus.sql) |
| 4 | `schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)` | `if a.id is null or a.pool <> 'uebung' then return; end if;` | 1 | voll (20261119_w176_h_muss.sql) |
| 5 | `schule.misch_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)` | `if a.id is null or a.pool <> 'uebung' then return; end if;` | 1 | voll (20261120_i3_lernregeln_nachpruefung.sql) |
| 6 | `schule.expedition_buchen(bigint, bigint, boolean, smallint, smallint, timestamp with time zone)` | `coalesce(p_anlauf, 1) = 1 then` | 1 | voll (20261125_ex_s_expedition.sql) |
| 7 | `schule.expedition_buchen(bigint, bigint, boolean, smallint, smallint, timestamp with time zone)` | `a.variante_gruppe, p_zeit); -- H8` | 1 | voll (20261125_ex_s_expedition.sql) |
| 8 | `schule.karte_landet(schule.karte_stand)` | `least(3, schule.karte_ziel(k.einheit_id, k.lernziel));` | 1 | voll (20261120_lb3_nachbesserung.sql) |
| 9 | `schule.karte_ziel(bigint, text)` | `where a.einheit_id = p_einheit and` | 1 | voll (20261116_w150_sitzt_regel_6_mit_schwer.sql) |
| 10 | `schule.karte_typen_noetig(bigint, text)` | `where a.einheit_id = p_einheit and` | 1 | voll (20261118_w176_t1_punkteregel.sql) |
| 11 | `schule.karte_schwer_noetig(bigint, text)` | `where a.einheit_id = p_einheit and` | 1 | voll (20261116_w150_sitzt_regel_6_mit_schwer.sql) |
| 12 | `schule.folge_nachrechnen(bigint, bigint, text, timestamp with time zone)` | `a.variante_gruppe = p_lz and a.pool = 'uebung'` | 1 | voll (20261120_i2_lernregeln.sql) |
| 13 | `schule.landung_zaehlen(bigint, bigint, text)` | `a.variante_gruppe = p_lz and a.pool = 'uebung'` | 2 | voll (20261120_ab_s_abschluss.sql) |
| 14 | `schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)` | `where a.einheit_id = p_e and` | 1 | voll (20261122_wd_s3_frische_aufgaben.sql) |
| 15 | `schule.wdh_aufgabe_da(bigint, bigint, text)` | `where a.einheit_id = p_e and` | 1 | voll (20261122_wd_s4_nacharbeit_921.sql) |
| 16 | `schule.wdh_aufgabe_da(bigint, text)` | `where a.einheit_id = p_e and` | 1 | voll (20261122_wd_s_wiederholungen.sql) |
| 17 | `schule.uebung_pruefen_intern(bigint, jsonb)` | `'schwer_ok', k.schwer_ok, 'schwer_noetig'` | 1 | voll (20261116_w150_r2_fehlermuster_zweiter_versuch.sql) |
| 18 | `schule.etappen_stand(bigint, bigint)` | `'schwer_ok', coalesce(k.schwer_ok, false), 'schwer_noetig'` | 1 | voll (20261114_w150_lernkarten_meisterschaft.sql) |
| 19 | `schule.einheit_lesen_intern(bigint, bigint)` | `'heute_tag', schule.heute_tag(p_lernender), 'heute_bis'` | 1 | TEIL (–) |

Zum Zählen nur lesend, z. B. je Zeile:
`select (length(d) - length(replace(d, '<alt>', ''))) / length('<alt>') from (select pg_get_functiondef('<Signatur>'::regprocedure) d) x;` (einfache Anführungszeichen im alten Text verdoppeln).

## (d) Geprüft und bewusst NICHT geändert

- `versuch_karte`, `versuch_buchen`, `versuch_wertung`, `offene_entscheiden`: Wertung und Nachbuchen bleiben; die Buchung selbst (`karte_buchen`/`misch_buchen`/`expedition_buchen`) filtert. Ein Versuch an einer nicht zählenden Aufgabe entscheidet weiter einen offenen ersten Anlauf einer anderen Aufgabe („weitergegangen“) – wie jede andere Aufgabe.
- `mischkarten_waehlen`, `mischkarten`: ziehen über `wdh_aufgabe_waehlen` (gepatcht); `misch_gueltig` verlangt eine ausgegebene Karte.
- `uebung_pruefen_wd`: nur Hülle um `uebung_pruefen_intern`; nichts zu ändern.
- `karte_sicher`, `flug_wdh_setzen`, `flug_wdh_zuruecknehmen`, `karten_wiederherstellen`: arbeiten mit gelandeten bzw. gesetzten Karten (`sitzt_am` gesetzt) → keine Pflicht, Verhalten unverändert. `karte_sicher` stützt sich auf Wiederholung, Mischkarte und Nachtest, nicht auf gezählte Übungen.
- `landung_speichern`, `landung_bonus`: rechnen aus `landung_zaehlen` (gepatcht).
- `heute_selbst` („heute selbst gelöst“): Tageszähler für die Anzeige, kein Rechenbeleg der Karte – zählt weiter jede selbst gelöste Übung.
- `wackelt_fehler`, `fehler_endgueltig_am` („Was wackelt“): ein Fehler in einer nicht zählenden Aufgabe ist trotzdem ein Fehler für die Eltern-Ansicht.
- `etappen_stand.gesamt`/`geloest`, `etappen_wenig_frisch`: Anzeige- bzw. Lesehilfen; zählen weiter alle freigegebenen Übungen.
- `nachbessern`: nutzt `karte_ziel` (gepatcht).
- Tests: `nachtest_auswahl`, `test_starten_intern`, `test_abschliessen_intern` – Regel 7, unverändert.
- `api.schule_lernstand` (Eltern): bekommt die neuen Felder nicht (Vorgabe nennt nur die App). `api.schule_inhalt_lesen`: liefert form/zaehlt nicht (könnte später ergänzt werden).
- `einheit_abgleichen`, `expedition_importieren`: übernehmen form/zaehlt für vorhandene Aufgaben nicht; neue Aufgaben laufen über `aufgaben_einfuegen` (gepatcht). Expeditionen haben deshalb immer leeres `zaehlt` (= zählt).

## (e) Schnittstelle für den App-Bau

| Wo | Feld | Bedeutung |
|---|---|---|
| jede Bordkarte (`aufgabe_anzeige`: Übungen, Wiederholung, Mischkarte, Knobel, Expedition) | `form` | neue Form (`lueckenweg`, `fehler_detektiv`, `verfahren_waehlen`, `zwei_wege`, `umkehren`, `bruecke`, `anwenden`, `viele_antworten`); fehlt = Bestand |
| dito | `zaehlt` | `ja` / `nein`; fehlt = ja. `nein` = Gerüst, zählt nicht für die Karte |
| `schule_einheit_lesen` | `form_jede` | Regel (Vorgabe 3): Plätze 3, 6, 9 … einer Lernkarte in neuer Form |
| `schule_einheit_lesen.etappen_stand[lernziel]` und `schule_uebung_pruefen.karte` | `bearbeitungen` | bisherige Bearbeitungen des Kindes an dieser Lernkarte (ohne Test, ohne Mischkarte, 2. Anlauf zählt nicht extra). Nächster Platz = `bearbeitungen + 1`; Form-Platz, wenn `(bearbeitungen + 1) % form_jede = 0` |
| dito | `anwenden_noetig` | true = für DIESE Karte gilt die Sachaufgaben-Pflicht (nie gelandet und es gibt eine freigegebene, zählende Sachaufgabe) |
| dito | `anwenden_ok` | true = eine Sachaufgabe ist schon gezählt |

„Sachaufgabe fehlt noch“ zeigen: `anwenden_noetig and not anwenden_ok` und alle übrigen Bedingungen erfüllt (eigene_loesungen ≥ ziel, typen_anzahl ≥ typen_noetig, schwer_ok oder nicht schwer_noetig, folge ≥ folge_ziel). Dann eine ungelöste Übung der Lernkarte mit `typ` in (`einkleidung`, `transfer`, `pruefung`) und `zaehlt` ≠ `nein` vorlegen. Hinweis: `zaehlt` = `nein` ändert an `karte` nichts; existiert für die Lernkarte noch keine Zeile, fehlt `karte` in der Antwort ganz.

## (f) Risiken und was ich NICHT prüfen konnte

- **Keine Live-Fassung gesehen.** Alle 19 Anker sind nur gegen die Rekonstruktion gezählt. `einheit_lesen_intern` ist nur eine Teil-Rekonstruktion (Grundtext nicht im Repo). Vor dem Einspielen: Anker-Tabelle (c) live zählen; das Paket bricht bei jeder Abweichung ohnehin ab.
- **Lokal geprüft** (eigene, leere PostgreSQL-16-Testinstanz mit nachgebauten Tabellen und den rekonstruierten Funktionen, nicht die Projektdatenbank): Migration zweimal durchgelaufen, mit Prüfung der Funktionskörper; 17 Funktionen geändert, zweiter Lauf ohne Änderung, Rechte gleich; Prüfbedingung weist `form = 'quatsch'` ab; Landeregel ohne/mit Sachaufgabe und für gelandete Karten wie erwartet; `perform … where false` führt nichts aus. Die Abschnitte 1 und 2 des Prüfblocks (zweiter Lauf, Rechte, Spalten, Mischstand halb/fremd, Gegenprobe) liefen dort fehlerfrei. Die Syntax aller PL/pgSQL-Blöcke des Pakets ist geprüft.
- **Nicht gelaufen:** Abschnitte 3–8 des Pakets (Bestand, zaehlt-Proben, Pflicht, Wiederholung, Prüfsummen) – sie brauchen die echte Datenbank. Unsicher vor allem: Probe-Lernkarten mit Lernzielen, die es im Flug nicht gibt (`ft-probe-a` …) – Trigger nach einer Landung (z. B. Zusatz-/Plan-Trigger) könnten damit anders umgehen. Daher zuerst `--probe`.
- Das Paket sperrt `schule.aufgabe` (ALTER TABLE) bis zum Ende der Transaktion – nur in einer Nutzungspause.
- Bestand-Vergleich: Die Antwort von `schule_uebung_pruefen` bekommt in `karte` drei neue Felder; verglichen wird ohne diese drei, die Karte selbst Zeichen für Zeichen (md5).
- Größe: Paket 38 877 Zeichen (Probe 39 003). Die Migration ist darin ohne ihre ganzzeiligen Kommentare eingebettet (sonst unverändert).
- `rollend_sql.py`: meldet in der Übersicht OK (142 Aufgaben aus rollend-1/-2; mit `--mit-bedingung` 192). Offen: **drei Aufgaben mit `zaehlt = folge`** (A4-06, GE2-07, GE2-10) – die Übersicht meldet sie als OFFEN, `--sql` bricht ab, bis der Mathe-Profi ja/nein setzt (Inhalte habe ich nicht geändert). Sechs Flüge aus rollend-3 (127 Aufgaben) haben keine Zuordnung in `rollend-einheiten.json` und werden übersprungen. Das erzeugte SQL setzt FT-S voraus und prüft das.
- Takt-Feld `bearbeitungen` zählt auch Antworten in der Wiederholung dieser Karte mit; wenn der Takt nur beim Üben laufen soll, muss die App das wissen (die Vorgabe sagt „Bearbeitungen an der Lernkarte“).
