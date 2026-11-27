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

20 Anker in 17 Funktionen (Nr. 18 ist neu, Nachtrag 1032 – siehe Abschnitt Nachträge). Gezählt wird im Text von `pg_get_functiondef(...)`, so wie es das Paket tut: `(length(d) - length(replace(d, alt, ''))) / length(alt)`. Erwartet ist der Zustand „alt“; „neu“ muss 0-mal vorkommen. ⏎ = Zeilenumbruch (kommt nicht vor). Erzeugt mit `python3 -I tools/tests/form_takt_anker.py --tabelle`.

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
| 18 | `schule.uebung_pruefen_intern(bigint, jsonb)` | `k.lernziel = a.variante_gruppe)));` | 1 | voll (20261116_w150_r2_fehlermuster_zweiter_versuch.sql) |
| 19 | `schule.etappen_stand(bigint, bigint)` | `'schwer_ok', coalesce(k.schwer_ok, false), 'schwer_noetig'` | 1 | voll (20261114_w150_lernkarten_meisterschaft.sql) |
| 20 | `schule.einheit_lesen_intern(bigint, bigint)` | `'heute_tag', schule.heute_tag(p_lernender), 'heute_bis'` | 1 | TEIL (–) |

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

„Sachaufgabe fehlt noch“ zeigen: `anwenden_noetig and not anwenden_ok` und alle übrigen Bedingungen erfüllt (eigene_loesungen ≥ ziel, typen_anzahl ≥ typen_noetig, schwer_ok oder nicht schwer_noetig, folge ≥ folge_ziel). Dann eine ungelöste Übung der Lernkarte mit `typ` in (`einkleidung`, `transfer`, `pruefung`) und `zaehlt` ≠ `nein` vorlegen. Hinweis: `zaehlt` = `nein` ändert an `karte` nichts; existiert für die Lernkarte noch keine Zeile, fehlt `karte` in der Antwort ganz. **Überholt bzw. ergänzt durch die Nachträge unten:** `bearbeitungen` steht jetzt auch außerhalb von `karte`; `anwenden_noetig` ist false, solange der Schalter `anwenden_pflicht` aus ist.

## (f) Risiken und was ich NICHT prüfen konnte

- **Keine Live-Fassung gesehen.** Alle 19 Anker sind nur gegen die Rekonstruktion gezählt. `einheit_lesen_intern` ist nur eine Teil-Rekonstruktion (Grundtext nicht im Repo). Vor dem Einspielen: Anker-Tabelle (c) live zählen; das Paket bricht bei jeder Abweichung ohnehin ab.
- **Lokal geprüft** (eigene, leere PostgreSQL-16-Testinstanz mit nachgebauten Tabellen und den rekonstruierten Funktionen, nicht die Projektdatenbank): Migration zweimal durchgelaufen, mit Prüfung der Funktionskörper; 17 Funktionen geändert, zweiter Lauf ohne Änderung, Rechte gleich; Prüfbedingung weist `form = 'quatsch'` ab; Landeregel ohne/mit Sachaufgabe und für gelandete Karten wie erwartet; `perform … where false` führt nichts aus. Die Abschnitte 1 und 2 des Prüfblocks (zweiter Lauf, Rechte, Spalten, Mischstand halb/fremd, Gegenprobe) liefen dort fehlerfrei. Die Syntax aller PL/pgSQL-Blöcke des Pakets ist geprüft.
- **Nicht gelaufen:** Abschnitte 3–8 des Pakets (Bestand, zaehlt-Proben, Pflicht, Wiederholung, Prüfsummen) – sie brauchen die echte Datenbank. Unsicher vor allem: Probe-Lernkarten mit Lernzielen, die es im Flug nicht gibt (`ft-probe-a` …) – Trigger nach einer Landung (z. B. Zusatz-/Plan-Trigger) könnten damit anders umgehen. Daher zuerst `--probe`.
- Das Paket sperrt `schule.aufgabe` (ALTER TABLE) bis zum Ende der Transaktion – nur in einer Nutzungspause.
- Bestand-Vergleich: Die Antwort von `schule_uebung_pruefen` bekommt in `karte` drei neue Felder; verglichen wird ohne diese drei, die Karte selbst Zeichen für Zeichen (md5).
- Größe: Paket 38 877 Zeichen (Probe 39 003). Die Migration ist darin ohne ihre ganzzeiligen Kommentare eingebettet (sonst unverändert).
- `rollend_sql.py`: meldet in der Übersicht OK (142 Aufgaben aus rollend-1/-2; mit `--mit-bedingung` 192). Offen: **drei Aufgaben mit `zaehlt = folge`** (A4-06, GE2-07, GE2-10) – die Übersicht meldet sie als OFFEN, `--sql` bricht ab, bis der Mathe-Profi ja/nein setzt (Inhalte habe ich nicht geändert). Sechs Flüge aus rollend-3 (127 Aufgaben) haben keine Zuordnung in `rollend-einheiten.json` und werden übersprungen. Das erzeugte SQL setzt FT-S voraus und prüft das.
- Takt-Feld `bearbeitungen` zählt auch Antworten in der Wiederholung dieser Karte mit; wenn der Takt nur beim Üben laufen soll, muss die App das wissen (die Vorgabe sagt „Bearbeitungen an der Lernkarte“).

## Nachträge nach Gegenprüfung 1030/1032

Stand 27.11.2026, Helfer „Bau Server“. Nur Dateien; nichts gegen die Projektdatenbank ausgeführt.

### Was geändert ist
1. **Schalter `anwenden_pflicht`** (Aufgabe C). Neue Regel in `schule.regel`, Wert `0` (aus) beim Einspielen, `on conflict do nothing` – ein zweiter Lauf setzt einen eingeschalteten Schalter nicht zurück. Abgefragt an **einer** Stelle: in der neuen Hilfsfunktion `schule.karte_anwenden_pflicht` (`schule.wd_regel('anwenden_pflicht', 0) = 1 and …`). Diese Funktion nutzen schon `karte_landet` (Landeregel) und beide Ausgaben `anwenden_noetig` (`uebung_pruefen_intern.karte`, `etappen_stand`). Darum war kein weiterer Text-Patch nötig. Das ist kleiner als ein eigener Schalter in `karte_landet` und in beiden Ausgaben (drei Stellen, drei neue Anker).
   - Aus (0): keine Sachaufgaben-Pflicht, `anwenden_noetig` = false überall; `anwenden_ok` wird weiter gemeldet.
   - **Einschalten (ein Befehl, mit der App 0.94.0):** `update schule.regel set wert = '1'::jsonb where schluessel = 'anwenden_pflicht';`
   - Ausschalten entsprechend mit `'0'::jsonb`. Erlaubt sind nur 0 und 1; jeder andere Wert gilt als aus.
2. **`bearbeitungen` außerhalb von `karte`** (Aufgabe B). Antwort: **nein**, vorher kam `bearbeitungen` nur in `karte` mit. Nach der ersten nicht zählenden Aufgabe einer Lernkarte gibt es noch keine Kartenzeile, also fehlte `karte` und mit ihr der Stand. Neu: ein zweiter Text-Patch in `uebung_pruefen_intern`, im letzten `return` (normale Übung mit Lösung) am Ende des Objekts:
   - alt `k.lernziel = a.variante_gruppe)));` (1-mal)
   - neu `k.lernziel = a.variante_gruppe), 'bearbeitungen', schule.karte_bearbeitungen(p_lernender, a.einheit_id, a.variante_gruppe)));`
   - Das ist Anker **Nr. 18** (die Nummern 18/19 von vorher heißen jetzt 19/20). `inhalte/plan/form-takt-anker.json` ist neu erzeugt (`form_takt_anker.py --json`, 20 Einträge). `karte.bearbeitungen` bleibt.
   - Gilt NICHT für: ersten Fehlversuch mit „nochmal“, wiederholte Übertragung (`wiederholt`), Mischkarte, Knobel, Expedition. Diese Antworten haben weiter kein `bearbeitungen` (die nächste Aufgabe ist dort entweder der 2. Anlauf derselben Aufgabe oder liegt außerhalb des Takts).
3. **Prüfpaket** (`tools/tests/form_takt_einspielen.py`): neue Abschnitte 8–12, alter Abschnitt 8 ist jetzt 13. Neue Hilfe `pg_temp.ft_antx` (Antwort mit beliebigen Zusatzfeldern, z. B. `misch`). Abschnitt 6 schaltet den Schalter in seiner Untertransaktion mit genau dem Einschalt-Befehl ein. Bestand-Vergleich (Abschnitt 3) blendet zusätzlich das neue Feld `bearbeitungen` oben aus und verlangt es bei `falsch-2` und `richtig`.

### Was das Paket jetzt zusätzlich nachweist
Alle Proben am Testkind mit im Paket angelegten Aufgaben/Lernkarten (`ft-probe-f` … `ft-probe-l`), jede in einer zurückgerollten Untertransaktion. Jede Abweichung landet in der Fehlerliste; ist sie nicht leer, bricht der Prüfblock mit `raise exception` ab (alles zurück).
- **Abschnitt 1:** Schalter steht nach dem Einspielen auf 0.
- **Abschnitt 4 (Aufgabe B):** erste nicht zählende Aufgabe einer neuen Lernkarte: kein `karte`, aber `bearbeitungen` = 1. Erste zählende danach: `bearbeitungen` = 2 oben und in `karte`.
- **Abschnitt 8 (A1):** sitzende Karte, ausdrücklich fällig gemacht (`karte_faellig` = true geprüft). Aufgabe mit `zaehlt = nein` über `uebung_pruefen_wd`: richtig, endgültig falsch (1. + 2. Anlauf), mit Misch-Wunsch. Nach jeder Antwort ist die **ganze Kartenzeile** (Text der Zeile, damit auch `wdh_stufe`, `faellig_am`, `wdh_ab`, `folge`, `zuletzt`) gleich, keine Antwort enthält `wiederholung`, der Misch-Wunsch ist nicht gültig. `bearbeitungen` steigt um 1, 1, 1 (2. Anlauf zählt nicht extra). Derselbe `client_id` noch einmal: Antwort `wiederholt`, Zahl der Versuche bleibt 4, `bearbeitungen` bleibt, Zeile bleibt.
- **Abschnitt 9 (A2):** Typ `umkehr` nur in einer Aufgabe mit `zaehlt = nein` → `karte_typen_noetig` = 1 (Gegenprobe mit `zaehlt = ja`: 2). Einzige Stufe-3-Aufgabe mit `zaehlt = nein` → `karte_schwer_noetig` = false (Gegenprobe: true). Die Karte landet mit 6 Lösungen eines Typs auf Stufe 1. Folge: richtig, richtig, nicht zählender endgültiger Fehler, richtig → Buchung 3, `folge_nachrechnen` 3 (ohne Filter wäre es 1).
- **Abschnitt 10 (A3):** a) Sachaufgabe aus dem Bestand (`form`/`zaehlt` leer) schon in `gezaehlt`, bevor der Schalter an ist → nach dem Einschalten `karte_anwenden_pflicht` und `karte_anwenden_ok` beide true, die nächste Lösung lässt die Karte landen. b) Karte bei Schalter aus ohne Sachaufgabe gelandet, Schalter an, zwei endgültige Fehler → wieder offen (`sitzt_am` bleibt, `geoeffnet_am` gesetzt, Pflicht false), drei richtige → landet wieder ohne Sachaufgabe.
- **Abschnitt 11 (A4):** offener erster Fehlversuch an einer zählenden Aufgabe, danach eine nicht zählende Aufgabe: der Fehlversuch wird endgültig `falsch` gebucht (Karte `falsch` 1, `fehler_folge` 1), die nicht zählende ändert nichts weiter.
- **Abschnitt 12 (C):** Schalter aus: Karte mit freigegebener, zählender Sachaufgabe landet nach 6 Lösungen ohne sie, `anwenden_noetig` false vorher und nachher. Einschalt-Befehl → Regel 1; ein weiterer vollständiger Lauf der Migration lässt sie auf 1. Danach: keine Probe-Karte und Schalter wieder 0.
- **Abschnitt 13:** wie bisher, die Prüfung „keine sitzende Karte hätte eine Sachaufgaben-Pflicht“ läuft jetzt bei eingeschaltetem Schalter (Untertransaktion), sonst wäre sie leer erfüllt.

### Lokal geprüft (gesichert)
- `python3 -I tools/tests/form_takt_anker.py`: OK, 17 Funktionen, 20 Anker (gegen die Rekonstruktion; `einheit_lesen_intern` weiter nur TEIL).
- Eigene PostgreSQL-16-Instanz unter `/tmp` (nicht die Projektdatenbank): Grundtabellen von Hand nachgebaut, alle Migrationsdateien des Repos nacheinander eingespielt (Fehler an Rand-Teilen wie Reise, Lehrplan, Teilung hingenommen), danach alle 187 vollständig rekonstruierten `schule.*`-Funktionen aus `form_takt_anker.py` darübergelegt; `einheit_lesen_intern` als kleiner Ersatz (nur `uebungen`, `etappen_stand`, `heute_tag`, `heute_bis`). Testdaten: drei Kinder, eine Einheit, zwölf Übungen, zwei fremde Karten.
- Darauf: **Probe-Paket bestanden** (alle Abschnitte 1–13); **Einspiel-Paket** auf einer Kopie bestanden und eingespielt (Schalter 0, `form_jede` 3, keine Probe-Aufgaben übrig).
- Gegenproben (Funktion nach der Migration absichtlich verdorben): ohne Filter in `karte_buchen` schlagen die Abschnitte 4 und 8 an; ohne `bearbeitungen` oben die Abschnitte 4, 8, 11; ohne Filter in `karte_typen_noetig`/`folge_nachrechnen` der Abschnitt 9; Schalter ohne Wirkung → Abschnitte 10b und 12.

### NICHT geprüft / Annahmen
- **Nicht gegen die Live-Datenbank gelaufen.** Anker Nr. 18 ist nur gegen die Rekonstruktion gezählt (er stammt aus `20261116_w150_r2`, derselben Datei wie Anker 17, der live passte). Annahme: Live steht das Ende des letzten `return` genau so. Wenn nicht, bricht das Paket mit „weder im alten noch im fertigen Zustand“ ab – also zuerst wieder `--probe`.
- Die lokale Instanz hat nicht alle Trigger und Tabellen der Live-Datenbank (z. B. Zusatz-Plan, Reise, Teilung, `sterne_aus_versuch` fehlten oder liefen nur teilweise). Die Abschnitte 8–12 erzeugen mehrere Landungen (`ft-probe-f`, `-g`, `-i`, `-j`, `-l`); Trigger nach Landungen sind live wie bei den alten Abschnitten nur über den Probelauf geprüft.
- Abschnitt 8 macht die Karte über ein direktes `update` von `faellig_am`/`wdh_ab` fällig (Testdaten, zurückgerollt); live greift dabei der Trigger `karte_wdh_ereignis` (lokal vorhanden, ohne Wirkung, weil sich `richtig`/`falsch` nicht ändern).
- Abschnitt 9 ändert `zaehlt` von Probe-Aufgaben per `update`, bevor es Versuche an ihnen gibt (der Versionsschutz greift erst bei Aufgaben mit Versuch). Annahme: live kein weiterer Trigger, der das abweist.
- Übergang A3a ist mit einer Bestand-Sachaufgabe (`zaehlt` leer) bei ausgeschaltetem Schalter nachgestellt, nicht mit Daten von vor FT-S. Gleichwertig, weil `karte_buchen` für Aufgaben mit leerem `zaehlt` vor und nach FT-S gleich bucht (einzige Änderung dort: Rücksprung bei `nein`).
- Paketgröße jetzt 57 413 Zeichen (Probe 57 539).

### Schnittstelle App (aktualisiert)
| Wo | Feld | Bedeutung |
|---|---|---|
| Antwort `schule_uebung_pruefen` (normale Übung mit Lösung) | `bearbeitungen` (oben, NEU) | wie `karte.bearbeitungen`, kommt auch, wenn `karte` fehlt (erste nicht zählende Aufgabe einer Lernkarte). Fehlt bei „nochmal“, `wiederholt`, Mischkarte, Knobel, Expedition |
| `karte` und `etappen_stand[lernziel]` | `anwenden_noetig` | true nur, wenn der Schalter an ist UND die Karte nie gelandet ist UND die Lernkarte eine freigegebene, zählende Sachaufgabe hat. Bis zum Einschalten immer false → App 0.94.0 zeigt „Sachaufgabe fehlt noch“ nur bei true, ältere Apps sehen keine Hürde |
| dito | `anwenden_ok` | unverändert (unabhängig vom Schalter) |
| Regel | `anwenden_pflicht` | 0/1; die App muss sie nicht lesen, `anwenden_noetig` enthält sie schon |

