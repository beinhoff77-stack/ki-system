# Bestands-Berichtigung 1 – Einspielen (Plan, NICHTS eingespielt)

Stand 28.11.2026. Nur mit dem ausdrücklichen Satz des Nutzers ausführen. Nichts hiervon ist live. Das Paket ändert keinen App-Code, keine Quelldatei und keinen Lernstand.

## Was das Paket tut
23 berichtigte Aufgaben (`vorschlag.json`), je Paar: alte Aufgabe erkennen → neue über `schule.aufgaben_einfuegen` einfügen (gleiche Einheit, Lernkarte, Vorrat, Stufe) → Regel und Fehlbilder in `schule.aufgabe_regel` / `schule.aufgabe_fehlbild` → alte Aufgabe sperren (`freigegeben = false`). Entschieden vom Projektleiter: BB1-B2 und BB1-B3 sind drin; Zusatzfunde D1–D6 und die sechs weniger breiten Tabellen (App) sind NICHT in diesem Paket. Entfernt wurde nichts: alle 23 Vorschläge sind über die Aufgabe selbst lösbar (die fünf Beschriftungsfälle sind mit lokalem Chromium vorher/nachher gerendert: `bilder/BB1-C1.png` … `BB1-C5.png`).

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
| `tools/tests/aus/bestand_berichtigung1_probe.sql` | 72182 | `157d1ca36a71e4088f9280f5a66e8df9` |
| `tools/tests/aus/bestand_berichtigung1_einspielen.sql` | 72103 | `0b67964e4dad957e9de6277545003cdc` |

Erzeugt mit `python3 -I tools/bestand_berichtigung1_sql.py --pakete` (Prüfung: `--pakete --pruefen`). Test: `python3 -I tools/tests/bestand_berichtigung1_test.py`.

## Ausführungsregel
Jede Datei ist EIN Aufruf = EINE Transaktion (kein BEGIN/COMMIT, kein psql-Meta). Die Datei beginnt mit `select set_config('lock_timeout','3s',true), set_config('statement_timeout','120s',true);` und dann dem äußeren `do $bb1$ … $bb1$;` – die `set_config`-Zeile muss VOR dem `do` im selben Aufruf stehen (so ist die Datei gebaut; nicht trennen, nicht in zwei Aufrufen laufen lassen). Der Nutzer führt aus; Reihenfolge:

1. **Probelauf** (`…_probe.sql`): erwartet wird FEHLER mit der Meldung `PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): {…}` und im JSON `"neu_eingefuegt": 23, "alte_gesperrt": 23, "schon_berichtigt": 0, "zurueckgestellt": [], "regeln_neu": 14, "fehlbilder_neu": 69, "einheiten_geaendert": 18, "fehler": 0`. Im Bericht stehen außerdem `trigger` (alle Trigger auf einheit/aufgabe/aufgabe_regel/aufgabe_fehlbild der echten Datenbank) und `schreibzeilen_je_tabelle` (erwartet nur aufgabe 46, aufgabe_regel 14, aufgabe_fehlbild 69, einheit 18). Bitte den Bericht dem Entwickler zurückgeben, bevor eingespielt wird.
2. **Einspielen** (`…_einspielen.sql`): Hinweis `BB1 eingespielt: {…}` mit denselben Zahlen; die letzte Zeile der Datei liefert `neu_gueltig = 23, neu_gesamt = 23`.
3. **Nachkontrolle**: Datei nochmals ausführen → `"schon_berichtigt": 23, "neu_eingefuegt": 0, "alte_gesperrt": 0` und nichts ändert sich.

Meldet das Paket `zurueckgestellt` (Paare mit offenem Verweis), ist das kein Fehler: diese Paare bleiben vollständig unberührt (weder neue Aufgabe noch Sperre); nach einigen Stunden (Mischkarte 24 h, Test beendet) dieselbe Datei nochmals ausführen, sie holt genau diese Paare nach.

## Erwartete Zahlen
23 neue Aufgaben (gültig), 23 alte gesperrt, 14 Regeln neu, 69 Fehlbilder neu, 18 Einheiten kurz umgeschaltet und danach Zeile für Zeile gleich. Freigegebene Aufgaben je Einheit/Vorrat/Lernkarte vorher = nachher.

## Erkennung und Zustände (Wiederholbarkeit)
Alte Aufgabe erkannt an: Einheit, Vorrat, Lernkarte, Antworttyp, Frage-JSON (genau), Antworten, Lösung und – bei Runden-Aufgaben – Platz. Zustände je Paar: `neu` (alte gültig, neue fehlt) · `fertig` (alte gesperrt, neue da und gleich dem Soll inkl. Regel/Fehlbilder) · `zurückgestellt` (offener Verweis) · sonst ABBRUCH mit Liste (nicht erkannt; Einheit nicht freigegeben; alte gesperrt aber neue fehlt; Zwischenstand alte+neue beide gültig; Platz belegt; neue steht da, weicht ab).

## Nebenwirkungs-Analyse (wichtigster Teil)
**Wie wird gesperrt?** `aufgabe_schutz` (BEFORE UPDATE OR DELETE auf `schule.aufgabe`, Migration `20261118_w176_t4_expeditionen.sql`) lässt Änderungen an Aufgaben einer FREIGEGEBENEN Einheit nicht zu. Der im Repo belegte Weg (`20261123_tl_s_teilung.sql`: Einheit kurz `geprueft`, ändern, zurück `freigegeben`) wird je Einheit in EINER Transaktion gegangen. Für andere Sitzungen ist der Zwischenstatus nie sichtbar (Transaktionsisolation); die Einheitszeile wird mit `FOR NO KEY UPDATE` gesperrt (blockiert Fremdschlüssel-Einfügungen wie karte_stand/versuch NICHT).
**Trigger im Repo:** auf `schule.einheit` gibt es in den Migrationen keinen Trigger; auf `schule.aufgabe`: `aufgabe_schutz` (liest nur) und `aufgabe_bedingung_schutz` (greift nur bei Typ `bedingung` und geänderter Frage/Lösung – wir ändern nur `freigegeben`). Auf `aufgabe_regel`/`aufgabe_fehlbild`: `regelbezug_schutz` (nur UPDATE/DELETE; Einfügen frei). Auf `versuch`/`karte_stand`/`lernziel_stand`/`route` liegen Trigger (z. B. `karte_expedition_angebot`, `karte_zusatz_abschluss`, `route_zusatz_abschluss`), die durch Aufgaben-/Einheits-Updates NICHT ausgelöst werden. **Nicht im Repo sichtbar:** Live-Trigger auf `schule.einheit` (z. B. ein `einheit_schutz`). Deshalb prüft das Paket selbst: (1) Triggerfunktionen auf einheit/aufgabe/aufgabe_regel/aufgabe_fehlbild werden per Textsuche auf `insert into`, `delete from`, `update … set`, `pg_notify`, `http_`, `dblink`, `truncate` durchsucht – Fund = Abbruch; (2) Trigger-Satz vorher = nachher; (3) in KEINER Tabelle des Schemas `schule` darf eine von dieser Transaktion geschriebene Zeile stehen (Prüfung über `xmin`), außer aufgabe (46), aufgabe_regel, aufgabe_fehlbild, einheit (18) – das fängt auch Nebenwirkungen über versteckte Hilfsfunktionen; (4) die Einheitszeile ist danach `to_jsonb`-gleich (kein `freigegeben_von/am`-Reset, kein `geaendert`-Stempel); (5) die alten Aufgaben unterscheiden sich nur in `freigegeben`. Jede Abweichung = Abbruch, alles zurück (im Test mit drei künstlichen Triggern belegt). Unerkannt bleiben nur Löschungen durch einen Live-Trigger (nicht beobachtbar; die Textsuche (1) deckt das direkt sichtbare ab) – der Probelauf listet alle Live-Trigger im Bericht, das schließt die Lücke vor dem Einspielen.
**Kinder-Lernstände:** `versuch` bleibt (der Versuch hängt an der Aufgaben-ID, die bleibt). `karte_stand` speichert Zähler (`eigene_loesungen`, `typen`, `gezaehlt` {aufgabe_id: Zeit}) fortlaufend, wird nicht neu berechnet → ein Kind, das die alte Aufgabe schon gezählt hat, behält den Zähler und `sitzt`. `karte_ziel` (Zahl freigegebener Übungen je Lernkarte), `karte_typen_noetig`, `karte_schwer_noetig`, `karte_anwenden_noetig` werden je betroffener Lernkarte vor und nach dem Paket verglichen (1 : 1-Ersatz, Stufe/Vorrat/Lernkarte identisch) – gleich, sonst Abbruch. Das Paket verlangt außerdem, dass die neue Aufgabe in Thema/Art/Stufe/Lernkarte/Typ/Vorrat/Punkte/zählt der alten gleicht.
**Verhalten der App bei gesperrter Aufgabe:** neue Auswahlen (Wiederholung `wdh_aufgabe_waehlen`, Mischkarten, Übung, Nachtest-`sicherung`) filtern `freigegeben` → die alte kommt nicht mehr, die neue (noch ohne Versuch, daher bei Wiederholung zuerst gewählt) tritt an ihre Stelle. Eine schon ausgelieferte alte Aufgabe wird weiter bewertet und gebucht (`uebung_pruefen_intern` prüft nur Einheit `geprueft/freigegeben`, `karte_buchen` filtert nicht auf `freigegeben`). Ausnahme: eine Mischkarte (`misch_gueltig` verlangt `freigegeben` und eine offene `misch_ausgabe`) würde nicht als Beleg zählen → dieser Fall ist ein „offener Verweis“.
**Offene Verweise** (Paar wird zurückgestellt, damit nie zwei Aufgaben zugleich zählen und `karte_ziel` nie steigt): ausgegebene, nicht eingelöste, nicht verfallene Mischkarte < 24 h (`misch_ausgabe`); laufende Testsitzung (`testsitzung.aufgaben`, Status ≠ abgeschlossen); falscher 1. Anlauf ohne Folgeversuch < 2 h (der zweite Versuch des Kindes soll noch wie bisher laufen). `wdh_runde_etappe` verweist auf Einheit/Lernziel, nicht auf Aufgaben – kein Verweis.
**Nachtest (`sicherung`, BB1-A2):** zählt `vorhanden/fehlen` je Lernziel – unverändert (1 : 1). Ein Kind, dem die alte A2 schon in einem früheren Test gestellt wurde, kann die neue (fehlerfreie) als „frisch“ bekommen; das ist gewollt.
**Rest-Risiko, ehrlich:** (a) Fenster von Millisekunden zwischen Verweis-Prüfung und Commit, in dem ein Kind eine Mischkarte auf eine alte Aufgabe zieht – deren Antwort zählt dann nicht als Mischkarten-Beleg (24 h, keine Lernstand-Änderung); (b) Live-Trigger, die nur durch Textsuche/xmin nicht sichtbar sind (siehe oben, Probelauf listet sie).
**Ergebnis: kein Blocker.** Der Statuswechsel hat nach Repo-Stand keine Auswirkung auf Lernstände, Karten, Wiederholungen oder Flug-Tests; was live zusätzlich da sein könnte, bricht das Paket selbst ab (alles zurück). Die Gültigkeit am echten Bestand zeigt der Probelauf.

## Lernpause?
**Nein, nicht erforderlich.** Gründe: eine Transaktion von wenigen Sekunden; Lese-Zugriffe der Kinder werden nie blockiert (MVCC); es werden nur Zeilenlocks `FOR NO KEY UPDATE` gehalten, die Fremdschlüssel-Einfügungen (karte_stand, versuch, misch_ausgabe) nicht aufhalten; kein `ALTER TABLE`, keine Tabellensperre; `lock_timeout 3s` bricht sauber ab, falls doch etwas hält. Empfehlung ohne Pflicht: außerhalb der Lernzeit der Kinder einspielen (Rest-Risiko a).

## Nachkontrolle (nach dem Einspielen)
`select count(*) filter (where freigegeben), count(*) from schule.aufgabe where reihenfolge > 90000 and einheit_id in (…18 Einheiten…)` = 23 / 23; die gesperrten alten (`freigegeben = false`) = 23; Einheiten alle `freigegeben`; zweiter Lauf der Einspiel-Datei = 23 „schon berichtigt“.

## Rückweg
Vor dem Commit der Transaktion: jeder Abbruch rollt ALLES zurück (nichts zu tun). Nach dem Einspielen gibt es keinen automatischen Rückweg (aufgabe_schutz: Aufgaben freigegebener Einheiten sind unveränderlich). Wiederherstellung von Hand, falls nötig: je Einheit kurz `geprueft`, `update schule.aufgabe set freigegeben = true where id in (<alte IDs>)`, und die neuen mit `freigegeben = false` sperren (Versuche an neuen Aufgaben bleiben erhalten, es wird nie gelöscht), Einheit zurück `freigegeben`. Die alten IDs stehen im Bericht-Lauf nicht; sie sind über Einheit + Platz (Tabelle oben, „Platz Vorgänger“) bzw. Frage-JSON aus `vorschlag.json` (`ersetzt.alte_frage_json`) eindeutig bestimmbar.
