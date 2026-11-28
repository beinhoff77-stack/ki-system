# Bestands-Berichtigung 1 – Einspielen (Plan, NICHTS eingespielt)

Stand 28.11.2026, nach der Gegenprüfung 1182 und der Erweiterung von NF-S um `test_starten_intern` (Probelauf „Ja mit Auflagen“, Einspielen „Muss vorher“). Nur mit dem ausdrücklichen Satz des Nutzers ausführen. Nichts hiervon ist live. Die Pakete ändern keinen App-Code, keine Quelldatei und keinen Lernstand.

## Reihenfolge (verbindlich)
1. **NF-S-Probelauf** (`tools/tests/aus/nf_s_probe.sql`) – erwartet FEHLER mit `PROBELAUF bestanden, ALLES zurückgerollt …`, Bericht zurückgeben.
2. **NF-S einspielen** (`tools/tests/aus/nf_s_einspielen.sql`, = Migration `supabase/migrations/20261208_nf_s_nachtest_freigegeben.sql`, byteidentisch) – Hinweis `NF-S eingespielt: {…}`.
3. **Berichtigungs-Probelauf** (`tools/tests/aus/bestand_berichtigung1_probe.sql`) – bricht mit `BB1 ABBRUCH: erst NF-S einspielen …` ab, solange NF-S fehlt (alle DREI Funktionen müssen exakt die neue Fassung haben); sonst `PROBELAUF bestanden …`. Bericht zurückgeben.
4. **Berichtigung einspielen** (`tools/tests/aus/bestand_berichtigung1_einspielen.sql`) – **in einer Lernpause** (siehe unten).
5. Nachkontrolle (zweiter Lauf von 4 = „schon berichtigt“; NF-S nochmals = `neu -> neu`).

## Was NF-S tut (Voraussetzung, eigener Schritt; drei Funktionen)
Drei Auswahl-/Zählwege berücksichtigten `aufgabe.freigegeben` nicht; NF-S ergänzt in jedem genau `and a.freigegeben` (per `create or replace`; sonst NICHTS: Signatur, Rückgabe, Volatilität, Invoker, nicht STRICT, `search_path = ''`, Rechte, Kommentare):

| Funktion | Stelle | Live-Stand alt (Länge / prosrc-md5) | neu (md5) |
|---|---|---|---|
| `schule.nachtest_auswahl(bigint, bigint, text, integer)` STABLE | Sicherungs-Filter | 1109 / `f25fab1c1599d980752c87b6849d557f` | `ca0c30a1913c27b5de0a5505a76a53e5` |
| `schule.nachtest_stand(bigint, bigint)` STABLE | Vorrat: `left join … a.pool = 'sicherung'` | 3778 / `e73af9b462d741de80d4932d8fa7a38a` | `971ea734cc6cf986e438a29995cb66cf` |
| `schule.test_starten_intern(bigint, jsonb)` VOLATILE | (a) erster Flugtest `… a.pool = 'test'`; (b) Korrektur-Zweig `… a.pool = 'korrektur'` (der Nachtrags-Zweig filtert schon) | 6739 / `b226ac94131e47a507462e9be303ef8f` | `7abcd2918f5042142d8720ae044b36c1` (Länge 6775) |

Je Funktion genau zwei zulässige Zustände (prosrc-md5): alt → ersetzen; neu → nichts; alles andere → Abbruch, nichts geändert. Vorher/nachher werden Volatilität, Definer/Invoker, STRICT, `search_path`, Argumente, Rückgabetyp und Sprache verglichen. Texte: `nachtest_auswahl` aus `20261124_nt_s_nachtest_menge.sql`; `nachtest_stand` und `test_starten_intern` stehen in keiner Migration als Ganzes und liegen als Live-Stand in `tools/tests/nf_nachtest_stand_alt.prosrc.txt` bzw. `tools/tests/nf_test_starten_intern_alt.prosrc.txt` (nur Daten); die vollständige neue Fassung aller drei steht jetzt in der Migration `20261208_nf_s_nachtest_freigegeben.sql`.

**Probe-Bericht (nur Zahlen und Einheiten-IDs, keine Lerndaten):** `nachtest_auswahl` und `nachtest_stand` werden je Kind × Einheit (× Lernziel × Menge 1/2/3/5) vor und nach dem Ersetzen verglichen; Abweichung in einer Einheit OHNE gesperrte Sicherungsaufgabe = Abbruch, MIT gesperrter = gezählt (`auswahl_faelle_geaendert`, `stand_faelle_geaendert`, `stand_vorrat_runden_geaendert`, `stand_vorrat_unter_1_neu`, `stand_nachschub_noetig_neu`). `test_starten_intern` wird NICHT aufgerufen (VOLATILE, schreibt Sitzung/Lernziele); das Paket rechnet stattdessen die Auswahllogik lesend nach und meldet: `flugtest_einheiten_mit_testaufgaben`, `flugtest_einheiten_gekuerzt`, `flugtest_einheiten_nichts_zu_testen` (+ `_ids`), `pflicht_lernziele_ohne_freigegebene_testaufgabe` / `davon_neu_durch_sperre` / `einheiten_mit_solchem_lernziel_durch_sperre` (+ IDs), `korrektur_faelle_status_fehler` / `korrektur_faelle_andere_aufgabe_neu` / `korrektur_faelle_vorrat_leer_neu`, `korrektur_lernziele_ohne_freigegebene_aufgabe_durch_sperre`. Das sind Auswirkungen, kein Fehler: das Paket bricht dafür nicht ab; der Nutzer entscheidet nach dem Bericht.

**Folgen, ausdrücklich** (live gesperrt/gesamt je Pool laut Befund: bonus 82/1421, korrektur 376/2472, sicherung 749/5001, test 125/800, uebung 5233/22633, expedition 0/90):
- *Erster Flugtest wird kürzer*, wenn Test-Aufgaben gesperrt sind (`punkte_max` = Anzahl der Aufgaben). Der Blocktest nimmt alle freigegebenen `test`-Aufgaben der Einheit.
- *Sind in einer Einheit ALLE Test-Aufgaben gesperrt*, liefert der Start `nichts_zu_testen` (kein Test). Die Probe weist die Zahl aus (`flugtest_einheiten_nichts_zu_testen`, IDs).
- *Pflicht-Lernziel ohne freigegebene Test-Aufgabe* (`davon_neu_durch_sperre`): dieses Lernziel kann im ersten Flugtest nicht mehr nachgewiesen werden. **Das ist ein eigener Befund**, kein Fehler von NF-S. Die Flug-Fertig-Prüfung (`flug_erstabschluss_nachtragen`) verlangt für alle Pflicht-Lernziele `nachgewiesen/korrigiert/gesichert`; der Nachtragstest (Test- oder Korrektur-Aufgabe, nur freigegeben) wäre der einzige Weg, fehlt dort auch etwas: `vorrat_erschoepft`. Vor dem Einspielen am echten Bestand ansehen.
- *Korrektur*: je Kind × Lernziel mit Status `fehler` wird die erste freigegebene, ungesehene Korrektur-Aufgabe gewählt; ist keine mehr da → `vorrat_erschoepft` (gezählt in `korrektur_faelle_vorrat_leer_neu`).
- *Bestehensgrenze / Abschluss*: `test_abschliessen_intern` steht NICHT im Repo (nur Patches daran: `20261120_ab_s_abschluss.sql`, `20261120_ab_s_flug_abschluss_einmal.sql`, `20261121_ab_s_flug_geschafft_robust.sql`); `flug_abschluss` rechnet nur Sterne. Ob das Bestehen eine feste Punktzahl oder Anzahl verlangt, ist im Repo deshalb NICHT belegt; belegt ist nur die Bewertung je Lernziel (richtig → `nachgewiesen`, falsch → `fehler`, `20261118_w177_nachtragstest.sql`). Zur Klärung wird der Live-Text von `test_abschliessen_intern` gebraucht (offen).
- *Laufende Sitzungen bleiben unberührt*: `test_starten_intern` gibt eine laufende Sitzung unverändert zurück; die Auswahl wirkt nur bei NEUEN Sitzungen (im Test belegt: ein Kind mit laufendem Flugtest, der eine inzwischen gesperrte ID enthält, bekommt dieselbe Sitzung).

**`schule.nachtest_vorrat` (View, reine Berichtssicht)** bleibt in diesem Schritt bewusst UNVERÄNDERT: Sie zählt gesperrte Sicherungsaufgaben mit (Fehlliste, keine Auswahl). Ein `create or replace view` braucht den vollständigen Live-Text (`pg_get_viewdef`) mit festem Hash; der steht nicht im Repo (nur die Fassung aus `20261124_nt_s_nachtest_menge.sql`), ohne Hash wäre es ein Ersetzen auf Verdacht. Mit dem Live-Text liefere ich es als eigenen kleinen Schritt nach (kein Einfluss auf Kinder).

## Was die Berichtigung tut
23 berichtigte Aufgaben (`vorschlag.json`), je Paar: alte Aufgabe erkennen → neue über `schule.aufgaben_einfuegen` einfügen (gleiche Einheit, Lernkarte, Vorrat, Stufe) → Regel und Fehlbilder in `schule.aufgabe_regel` / `schule.aufgabe_fehlbild` → alte Aufgabe sperren (`freigegeben = false`). Entschieden vom Projektleiter: BB1-B2 und BB1-B3 sind drin; Zusatzfunde D1–D6 und die sechs weniger breiten Tabellen (App) sind NICHT in diesem Paket. Entfernt wurde nichts: alle 23 Vorschläge sind über die Aufgabe selbst lösbar.
Änderungen nach 1182: **K9A-V177** (BB1-T04) – die zwei Fehlbild-Texte passen jetzt zur gedrehten Tabelle (Grenzen 196 < 200 < 225); **K6-V202** (BB1-C5) – Zahl und Feld lassen sich über die Aufgabe selbst nicht zusammenhalten (Beschriftung und Feld sind in `.lern-lueckenzeile` getrennte Flex-Elemente, ein geschütztes Leerzeichen im Aufgabentext erreicht das nicht; betrifft auch andere Mehrfach-Lückenaufgaben, also ein App-Thema). Zusage fallen gelassen; die Aufgabe nutzt nun unbeschriftete Felder (`□ □ □ □`) und ordnet die Zahlen im Hinweis mit ①–④ zu. Bilder vorher/nachher bei 390 px und 320 px: `bilder/BB1-C5_390px.png`, `bilder/BB1-C5_320px.png` (ohne app.js-Fehler; der frühere Fehler kam aus der Test-Seite: Elemente `#btn-back` und `#ver` fehlten im Rahmen, nicht aus der Aufgabe). Übrige Bilder: `bilder/BB1-C1.png` … `BB1-C4.png`.

## Zuordnung BB1-… → endgültige Kennung (Schema der Runde: nächste freie Nummer je Präfix; `abbildung.json`)
Platz neu = `max_r + 90000 + laufende Nummer je Einheit` (frei von den Runden-Blöcken 1000·R; vom Test gegen alle eingespielten Plätze geprüft). Aufgaben ohne Kennung (inhalte/themen) bekommen das Präfix der Runden desselben Themas (zahlen.natuerlich → K5A, bruch.prozent → K6).

| Arbeitskennung | Kennung neu | Einheit | Vorrat | Lernkarte | Platz neu | Vorgänger | Platz Vorgänger | Regel | Fehlbilder |
|---|---|---|---|---|---|---|---|---|---|
| BB1-A1 | `K5A-V175` | 1 | uebung | stellenwert | 90806 | (Themen-Aufgabe, ohne Kennung) | über Inhalt | – | 3 |
| BB1-A2 | `K5A-V176` | 1 | sicherung | stellenwert | 90807 | (Themen-Aufgabe, ohne Kennung) | über Inhalt | – | 3 |
| BB1-B1 | `K6-V199` | 11 | uebung | rabatt_aufschlag | 90622 | K6-V117 | 6636 | id.verhaeltnisse.prozent | 3 |
| BB1-B2 | `K6-V200` | 11 | bonus | rabatt_aufschlag | 90623 | (Themen-Aufgabe, ohne Kennung) | über Inhalt | – | 3 |
| BB1-B3 | `K6-V201` | 11 | uebung | grundwert | 90624 | K6-V114 | 6633 | id.verhaeltnisse.prozent | 3 |
| BB1-C1 | `R8-V133` | 17 | uebung | graph_ablesen | 90778 | R8-V079 | 13780 | id.funktionen.wachstum | 3 |
| BB1-C2 | `R8-V134` | 308 | uebung | punktspiegelung | 90752 | R8-V115 | 13752 | id.geometrie.deckungsgleich | 3 |
| BB1-C3 | `R5-V211` | 49 | uebung | figuren | 90560 | R5-V129 | 12570 | – | 3 |
| BB1-C4 | `R8-V135` | 306 | uebung | vierecke | 90633 | R8-V121 | 13633 | id.geometrie.winkel | 3 |
| BB1-C5 | `K6-V202` | 59 | uebung | struktur | 90535 | K6-V121 | 6535 | id.algebra.term | 5 |
| BB1-T01 | `K9A-V175` | 32 | uebung | regel | 90563 | K9A-V161 | 9567 | id.daten.anteil | 3 |
| BB1-T02 | `K9A-V176` | 33 | uebung | schnitt | 90749 | K9A-V128 | 9753 | – | 3 |
| BB1-T03 | `S3-V061` | 5 | uebung | beide_seiten | 90605 | S3-V038 | 11607 | rr.waage | 3 |
| BB1-T04 | `K9A-V177` | 46 | uebung | abschaetzen | 90570 | K9A-V011 | 9580 | id.zahlen.hoch_zurueck | 2 |
| BB1-T05 | `S3-V062` | 39 | uebung | ordnen | 90790 | S3-V018 | 11791 | id.zahlen.zahlengerade | 3 |
| BB1-T06 | `R8-V136` | 16 | uebung | eindeutig | 90743 | R8-V059 | 13743 | id.funktionen.zuordnung | 3 |
| BB1-T07 | `S3-V063` | 28 | uebung | prisma | 90590 | S3-V027 | 11590 | – | 3 |
| BB1-T08 | `S3-V064` | 94 | uebung | prisma_volumen | 90412 | S3-V058 | 11412 | id.flaeche_raum.aus_dem_quader | 3 |
| BB1-T09 | `K9A-V178` | 33 | uebung | vierfeld | 90750 | K9A-V143 | 9768 | – | 3 |
| BB1-T10 | `K9A-V179` | 33 | uebung | venn | 90751 | K9A-V137 | 9762 | – | 3 |
| BB1-T11 | `R8-V137` | 34 | uebung | definitionsmenge | 90667 | R8-V031 | 13667 | id.algebra.erlaubte_zahlen | 2 |
| BB1-T12 | `S3-V065` | 44 | uebung | klammern | 90891 | S3-V008 | 11891 | rr.reihenfolge | 3 |
| BB1-T13 | `R8-V138` | 310 | uebung | koordinaten | 90583 | R8-V125 | 13583 | – | 3 |

Summe: 23 neue Aufgaben, 14 Regeln, 69 Fehlbilder, 18 Einheiten. Die neuen Aufgaben stehen NICHT in `rollend-*/`-Dateien (dort bleibt alles unverändert, die Pakete unter `tools/tests/aus/` auch); die Quelle der neuen Aufgaben ist `vorschlag.json`. Wird später gewünscht, dass die neuen Kennungen auch in den rollend-Dateien stehen, ist das ein eigener Schritt nach dem Einspielen.

## Dateien
| Datei | Bytes | md5 |
|---|---|---|
| `tools/tests/aus/nf_s_probe.sql` | 27902 | `3bc6ffa70f43297accd51628674f0bba` |
| `tools/tests/aus/nf_s_einspielen.sql` (= Migration `20261208_nf_s_nachtest_freigegeben.sql`) | 27824 | `075f0d4f87f9dff325e5f44ef5f23fa0` |
| `tools/tests/aus/bestand_berichtigung1_probe.sql` | 80112 | `93e737a3ca1b1f0109033b992671d82e` |
| `tools/tests/aus/bestand_berichtigung1_einspielen.sql` | 80033 | `872669ad8b75a160cfc18ce702d0f11a` |

Erzeugt mit `python3 -I tools/tests/nf_einspielen.py` bzw. `python3 -I tools/bestand_berichtigung1_sql.py --pakete` (Prüfung jeweils mit `--pruefen`). Tests: `python3 -I tools/tests/nf_s_test.py` (inkl. Flugtest-/Korrektur-Fälle und Negativfälle der dritten Funktion), `python3 -I tools/tests/bestand_berichtigung1_test.py`.

## Ausführungsregel
Jede Datei ist EIN Aufruf = EINE Transaktion (kein BEGIN/COMMIT, kein psql-Meta). Jede Datei beginnt mit `select set_config('lock_timeout', …, true), set_config('statement_timeout', …, true);` und dann dem äußeren `do $…$ … $…$;` – die `set_config`-Zeile steht VOR dem `do` im selben Aufruf (nicht trennen, nicht in zwei Aufrufen laufen lassen). Der Nutzer führt aus, in der Reihenfolge oben. Erwartung:
- **Proben** enden IMMER mit FEHLER `PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): {…}`; jede andere Meldung (`NF-S ABBRUCH` / `BB1 ABBRUCH`) = nicht einspielen, Meldung zurückgeben.
- NF-S-Bericht: `nachtest_auswahl`/`nachtest_stand`/`test_starten_intern` = `alt -> neu`, `abweichend_unerwartet: 0`, `eigenschaften_gleich: true`, `gesperrte_sicherungsaufgaben_live` und `abweichend_wegen_gesperrter_sicherungsaufgaben` (Zahlen bitte zurückgeben: sie zeigen, wie viele Kinder/Einheiten das Ergebnis ändert).
- BB1-Bericht: `"neu_eingefuegt": 23, "alte_gesperrt": 23, "schon_berichtigt": 0, "zurueckgestellt": [], "regeln_neu": 14, "fehlbilder_neu": 69, "einheiten_geaendert": 18, "sollantworten_richtig": 23, "fehlantworten_gueltig_und_falsch": 69, "lernkarten_regeln_gleich": true, "fingerabdruck_unberuehrter_zeilen_gleich": true, "nf_s_vorhanden": true, "fehler": 0`, dazu `trigger` (alle Live-Trigger auf einheit/aufgabe/aufgabe_regel/aufgabe_fehlbild), `schreibzeilen_je_tabelle` (erwartet nur aufgabe 46, aufgabe_regel 14, aufgabe_fehlbild 69, einheit 18) und `grenzen`.
- Einspielen: `NF-S eingespielt: {…}` bzw. `BB1 eingespielt: {…}` mit denselben Zahlen.
Meldet die Berichtigung `zurueckgestellt` (Paare mit offenem Verweis), ist das kein Fehler: diese Paare bleiben unberührt; später (Mischkarte 24 h, Test beendet) dieselbe Datei nochmals ausführen, sie holt genau diese Paare nach.

## Erwartete Zahlen
23 neue Aufgaben (gültig), 23 alte gesperrt, 14 Regeln, 69 Fehlbilder, 18 Einheiten kurz umgeschaltet und danach Zeile für Zeile gleich. Freigegebene Aufgaben je Einheit/Vorrat/Lernkarte vorher = nachher.

## Erkennung und Zustände (Wiederholbarkeit)
Alte Aufgabe erkannt an: Einheit, Vorrat, Lernkarte, Antworttyp, Frage-JSON (genau), Antworten, Lösung und – bei Runden-Aufgaben – Platz. Zustände je Paar: `neu` (alte gültig, neue fehlt) · `fertig` (alte gesperrt, neue da und GLEICH dem Soll: Form, zählt, Teilfähigkeit, Tipp, Lösungsweg, Regel, Fehlbilder) · `zurückgestellt` (offener Verweis) · sonst ABBRUCH mit Liste (nicht erkannt; Einheit nicht freigegeben; alte gesperrt aber neue fehlt; Zwischenstand beide gültig; Platz belegt; neue steht da, weicht ab). Im zweiten Lauf wird der volle Sollvergleich ebenfalls gemacht.

## Selbstprüfungen der Berichtigung (verschärft nach 1182)
- Verweisprüfung (offene Mischkarte, laufende Testsitzung, falscher 1. Anlauf) mehrfach: nach dem Sperren der Einheitszeile (`FOR NO KEY UPDATE`), und noch einmal unmittelbar vor dem Sperren der alten Aufgabe. Ein Verweis, der dazwischen entsteht, stellt das Paar zurück bzw. bricht ab.
- Die vier Karten-Funktionen (`karte_ziel`, `karte_typen_noetig`, `karte_schwer_noetig`, `karte_anwenden_noetig`) sind PFLICHT (fehlt eine: Abbruch) und werden je betroffener Lernkarte vorher/nachher verglichen.
- Antwortprobe wirklich ausgeführt: je neue Aufgabe die Soll-Antwort über die Bewertungsfunktion = richtig (23), jedes Fehlbild (69) = gültig und falsch.
- Fingerabdruck (md5 über die Zeilen) der UNBERÜHRTEN Zeilen von aufgabe, einheit, aufgabe_regel, aufgabe_fehlbild vorher = nachher.
- Triggerfunktionen-Textsuche, Trigger-Satz vorher = nachher, Einheitszeile `to_jsonb`-gleich, alte Aufgaben unterscheiden sich nur in `freigegeben`, Schreib-Prüfung über `xmin` im ganzen Schema `schule`.
- **Was die `xmin`-Prüfung NICHT sieht** (steht auch im Bericht unter `grenzen`): Löschungen (die Zeile ist weg), Sequenz-Änderungen (`nextval`), externe Effekte (`pg_notify`, HTTP, `dblink`), Schemas außer `schule`, Zeilen aus Untertransaktionen nicht zuverlässig; die Triggertext-Suche sieht delegierte/dynamische Schreibvorgänge nicht; für `versuch`/`karte_stand` gibt es keinen Fingerabdruck (dort läuft die Kinder-Aktivität parallel) – dort gilt nur die `xmin`-Prüfung auf Zeilen DIESER Transaktion; eine Mischkarte, die nach der letzten Verweisprüfung gezogen wird, ist nur durch die Lernpause ausgeschlossen.

## Nebenwirkungs-Analyse
**Wie wird gesperrt?** `aufgabe_schutz` (BEFORE UPDATE OR DELETE auf `schule.aufgabe`, Migration `20261118_w176_t4_expeditionen.sql`) lässt Änderungen an Aufgaben einer FREIGEGEBENEN Einheit nicht zu. Der im Repo belegte Weg (`20261123_tl_s_teilung.sql`: Einheit kurz `geprueft`, ändern, zurück `freigegeben`) wird je Einheit in EINER Transaktion gegangen; für andere Sitzungen ist der Zwischenstatus nie sichtbar.
**Trigger:** Laut Gegenprüfung 1182 liegen live auf den betroffenen Tabellen `einheit_schutz`, `aufgabe_schutz`, `aufgabe_bedingung_schutz`, `aufgabe_regel_schutz`, `aufgabe_fehlbild_schutz`; keiner schreibt Lerndaten. Im Repo sichtbar sind davon nur `aufgabe_schutz`, `aufgabe_bedingung_schutz` (greift nur bei Typ `bedingung` und geänderter Frage/Lösung) und `regelbezug_schutz`; `einheit_schutz` steht in keiner Migration. Das Paket prüft selbst und listet alle Live-Trigger im Probelauf-Bericht (`trigger`); Abweichung zum erwarteten Satz oder Schreib-Verdacht = Abbruch.
**Kinder-Lernstände:** `versuch` bleibt (hängt an der ID). `karte_stand` speichert Zähler (`eigene_loesungen`, `gezaehlt`) fortlaufend und wird nicht neu berechnet; ein Kind, das die alte Aufgabe schon gezählt hat, behält den Zähler.
**Verhalten bei gesperrter Aufgabe:** Auswahl (Übung, Wiederholung, Mischkarten, Knobel, Tests, nach NF-S auch Nachtest) filtert `freigegeben` → die alte kommt nicht mehr, die neue tritt an ihre Stelle. Schon ausgelieferte alte Aufgaben werden weiter bewertet (`20261118_w176_a_gesperrt_pruefen.sql`). Ausnahme: eine Mischkarte (`misch_gueltig` verlangt `freigegeben`) → „offener Verweis“.
**Offene Verweise** (Paar wird zurückgestellt): ausgegebene, nicht eingelöste, nicht verfallene Mischkarte < 24 h; laufende Testsitzung; falscher 1. Anlauf ohne Folgeversuch < 2 h.
**Entscheidung des Projektleiters (1182, Abschnitt 4), bewusst so:** Eine neue Aufgaben-ID gilt für jedes Kind wieder als frisch/ungelöst und darf auch ein eigener Nachweis sein. Das betrifft die 23 Aufgaben; ein Nachteil für ein Kind entsteht nicht (die alte Lösung bleibt in `versuch`, `karte_stand` wird nicht zurückgesetzt, der Nachweis durch die neue Aufgabe kommt dazu). Gilt auch für BB1-A2 (Nachtest-Vorrat): nach NF-S zählt die Ersatzaufgabe genau einmal, die gesperrte nicht mehr.
**Weitere Stellen, die `freigegeben` nicht beachten (Suche in allen Migrationen, jeweils jüngste Fassung):**

| Funktion / Objekt | Auswahl oder Zählung | filtert `freigegeben` | Fundstelle | Folge für BB1 |
|---|---|---|---|---|
| `schule.nachtest_auswahl` | Auswahl Nachtest | ja (NF-S) | `20261208_nf_s_…` | behoben |
| `schule.nachtest_stand` | Zählung Vorrat | ja (NF-S) | `20261208_nf_s_…` | behoben |
| `schule.nachtest_vorrat` (View) | Zählung Sicherungsaufgaben je Gruppe/Etappe (nur Fehlliste/Bericht) | NEIN | `20261124_nt_s_nachtest_menge.sql` Z. 98–100 | zählt gesperrte mit; nur Bericht, keine Auswahl; bewusst nicht geändert (Live-Text fehlt), siehe oben |
| `schule.test_starten_intern`, erster Flugtest (`pool = 'test'`) und Korrektur-Zweig (`pool = 'korrektur'`) | Auswahl Flugtest/Korrektur | ja (NF-S, neu) | Live-Text (Projektleiter), jetzt in `20261208_nf_s_…` | behoben; Nachtrags- und Nachtest-Zweig filterten schon |
| `wdh_aufgabe_waehlen`, `wdh_aufgabe_da`, `etappen_stand`, `etappen_wenig_frisch`, `mischkarten`, `karte_ziel`, `karte_typen_noetig`, `karte_schwer_noetig`, `karte_anwenden_noetig` | Auswahl/Zählung Übung, Wiederholung, Karte | ja | jeweils jüngste Migration | in Ordnung |
| `schule.etappe_heute_beantwortet`, `karte_bearbeitungen`, `karte_sicher`, `karte_buchen`, `landung_zaehlen`, `flug_abschluss`, `heute_selbst`, `heute_tag`, `folge_nachrechnen`, `besprochen_aktiv`, `wackelt_*`, `wdh_fehler`, `fehler_gruende`, `tl_testabdeckung`, `thema_teilen_stand` | zählen BEANTWORTETE Versuche (Verlauf, Joins über `versuch`) | NEIN, gewollt | `20261119_…` bis `20261206_…` | Verlauf soll gesperrte alte Aufgaben weiter mitzählen (Kind verliert nichts) |
| Auswahl der Übungsaufgabe für das Kind, Bonus/Knobel-Zuteilung | Auswahl | nicht im Repo sichtbar (nur live) | – | nicht prüfbar; Probelauf-Bericht und Nachkontrolle am echten Bestand |

Geändert werden nur die drei Funktionen von NF-S; die übrigen Lücken sind gemeldet. Die anderen Auswahlfunktionen hat der Projektleiter nur per Textsuche auf `freigegeben` geprüft, nicht je Zweig.
**Rest-Risiko, ehrlich:** (a) Mischkarte, die nach der letzten Verweisprüfung gezogen wird (nur Lernpause schließt das aus); (b) Live-Trigger/Seiteneffekte, die weder Textsuche noch `xmin` sehen (siehe Grenzen oben; der Probelauf listet alle Live-Trigger); (c) Live-Funktionen, die im Repo fehlen (Übungs-/Bonus-Auswahl, `test_abschliessen_intern`).
**Ergebnis: kein bekannter Blocker**, vorausgesetzt NF-S ist vorher eingespielt; was live zusätzlich da sein könnte, bricht das Paket selbst ab (alles zurück).

## Lernpause: erforderlich (für das echte Einspielen der Berichtigung)
Per Befund 1182 ist eine Lernpause Pflicht: nur so ist das Fenster der Mischkarten ausgeschlossen (eine Mischkarte, die zwischen der letzten Verweisprüfung und dem Commit auf eine alte Aufgabe gezogen wird, zählte nicht als Beleg). Ablauf: Kinder sind nicht in der App (bzw. keine neuen Mischkarten) → Schritt 4 → danach Nachkontrolle → Pause beenden. Für die Probeläufe und für NF-S ist keine Pause nötig (kurze Transaktionen, keine Tabellensperre, `lock_timeout` bricht sauber ab); NF-S ändert nur Lese-Funktionen.

## Nachkontrolle (nach dem Einspielen)
`select count(*) filter (where freigegeben), count(*) from schule.aufgabe where reihenfolge > 90000 and einheit_id in (…18 Einheiten…)` = 23 / 23; die gesperrten alten (`freigegeben = false`) = 23; Einheiten alle `freigegeben`; zweiter Lauf der Einspiel-Datei = 23 „schon berichtigt“; NF-S nochmals ausführen = `neu -> neu`.

## Rückweg
Vor dem Commit der Transaktion: jeder Abbruch rollt ALLES zurück. NF-S zurück: die alten Funktionstexte (md5 oben) per `create or replace` wiederherstellen (`tools/tests/nf_einspielen.py` liefert sie über `auswahl_alt()`/`stand_alt()`/`tsi_alt()`). Berichtigung nach dem Einspielen: kein automatischer Rückweg (aufgabe_schutz). Von Hand, falls nötig: je Einheit kurz `geprueft`, `update schule.aufgabe set freigegeben = true where id in (<alte IDs>)`, neue mit `freigegeben = false` sperren (nie löschen), Einheit zurück `freigegeben`. Die alten IDs sind über Einheit + Platz (Tabelle, „Platz Vorgänger“) bzw. `ersetzt.alte_frage_json` in `vorschlag.json` bestimmbar.
