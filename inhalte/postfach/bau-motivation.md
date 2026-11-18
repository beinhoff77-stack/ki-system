# Postfach bau-motivation (Bau-Chat, Bau-Auftrag G / Werkstatt-Wunsch 176)

Neueste oben.

## 2026-11-18 – FERTIG: Abgleich ohne Expeditionen

Stand von `lernen-app` übernommen (enthält 9d2f9be – dein berichtigter Kommentar in `h_muss` bleibt so).

- **Migration** `supabase/migrations/20261119_abgleich_ohne_expeditionen.sql` (nicht ausgeführt; pglast ok; kein DROP, kein DELETE):
  `schule.einheit_abgleichen` lässt Aufgaben mit `pool = 'expedition'` ganz unberührt – an allen 5 Stellen mit `b.einheit_id = v_e` (Änderungen übernehmen, „schon vorhanden?“, Zählen „nicht mehr in der Datei“, **Sperren**, Löschen bei Entwürfen).
  Die Migration bricht ab, wenn es nicht genau 5 Stellen sind oder die Funktion schon angepasst ist. Expeditions-Teile pflegt nur `expedition_importieren`.
- **Rauchtest** `supabase/tests/abgleich_ohne_expeditionen_rauchtest.sql` (Rollback): baut aus dem Datenbank-Stand die Themendatei eines Flugs mit freigegebenen Expeditions-Teilen (heute z. B. Einheit 1 mit 5 Teilen),
  gleicht mit `'sperren'` ab → Teile bleiben frei, „nicht mehr in der Datei“ = 0, keine neuen Aufgaben; Gegenprobe: eine Übung aus der Datei genommen → genau diese wird gesperrt, die Teile nicht.
  Vor der Migration schlägt der Test mit „FEHLER 2“ fehl (Nachweis des Fehlers).
- **Rauchtest H12b** (`w176_h_sollte_rauchtest.sql`): nimmt jetzt den Schlüssel `8-rauchtest-h12`, den es nicht gibt (prüft das vorab), statt `8-handytarif`. Damit stimmt auch H12d (4 neue Teile).
- Gelesen (nur lesend): heute 90 Expeditions-Teile, davon 0 gesperrt.

## 2026-11-18 – FERTIG: Auftrag H (korrigiert)

**Ursache** „record "v" is not assigned yet“: Im H2-Block von `20261119_w176_h_muss.sql` hieß die Schleifenvariable `v` wie der Tabellen-Alias `schule.versuch v`. Variable heißt jetzt `w`.

**Geprüft mit einem Skript** (Variablen jedes `declare` gegen Tabellen-/Funktions-Aliase im selben Block; erkennt die gemeldeten Fälle in den alten Fassungen):
- `h_sollte`: zweite Kollision gefunden und behoben – in `expedition_importieren` (H12-Prüfungen) liefen `jsonb_array_elements(…) t` / `… v` gegen die Variablen `t`, `v` → Aliase `tt`, `vv`.
- In die Live-Funktionen eingesetzte Stücke (`uebung_pruefen_intern`, `etappen_stand`, `schule_lernstand`, `schule_uebersicht`, `einheit_lesen_intern`, `expeditionen_kind`) gegen deren `declare` geprüft: keine Kollision.
- Danach: keine Treffer mehr in `h8`, `h_muss`, `h_sollte` und allen Rauchtests.
- Nebenbei: Bestandsfüllung H3 nimmt `misch` jetzt mit `coalesce(…, false)`.

**Rauchtests**
- `w176_t4_rauchtest.sql`: „a_ids is not a known variable“ – ein Kommentar stand mitten in der `declare`-Zeile und verschluckte `a_ids` und `v_n` (seit der Umbenennung k → ks). Behoben. Schritt 5 erwartet seit H8 `wdh_fehler = 0` (nur fällig).
- `w176_t3_rauchtest.sql` Schritt 4: erwartet jetzt `wdh_fehler = 0`, `wdh_lerntage = 1`, Etappe gelandet (H8).
- `w176_t1_rauchtest.sql`: an H3 angepasst (6-mal dieselbe Bordkarte → eigene 1, folge 6; Landen mit genug verschiedenen Bordkarten).
- `w176_h_muss_rauchtest.sql`: Variable `a` → `ag` (kollidierte mit `schule.aufgabe a`). `w176_h_sollte_rauchtest.sql`: Aliase `a`, `x` im H13-Teil → `au`, `xa`.
- Reihenfolge Probelauf: `h_muss` → `h_sollte` → Rauchtests `h8`, `t1`, `t3`, `t4`, `gesperrt`, `h_muss`, `h_sollte`.

Fachlich unverändert gegenüber „FERTIG: Auftrag H“; App unverändert (0.79.0).

## 2026-11-18 – FERTIG: Auftrag H (H1–H4, H9–H11 Muss; H5–H7, H12–H15 Sollte) – App 0.79.0

**Migrationen** (nicht ausgeführt; pglast ok; alle Ersetz-Stellen vorher im Live-Text geprüft, Abbruch mit Meldung, falls eine fehlt; kein DROP, kein DELETE; gelandete Etappen bleiben gelandet, Lernstände bleiben).
Reihenfolge: `20261119_w176_h8_misch_fehler_offen_lassen.sql` → `20261119_w176_h_muss.sql` → `20261119_w176_h_sollte.sql`. **App 0.79.0 mit `h_muss` zusammen live nehmen** (sonst zählen Mischkarten der alten App nicht mehr als Misch-Beleg, siehe H10).

**Rauchtests** (Rollback, nur Testkind, keine Namen, über den echten Weg `schule.uebung_pruefen_intern` → Trigger): `supabase/tests/w176_h_muss_rauchtest.sql` (H1, H3, H4, H9, H10, H11),
`supabase/tests/w176_h_sollte_rauchtest.sql` (H6, H12, H13-Server, H14, H15). `w176_t4_rauchtest.sql` Schritt 9 angepasst (ohne Teil b statt d, damit 3 Themen bleiben – H12).
**App-Tests:** lernen 70 von 70 (neu: H1, H3/H6, H4, H7, H13 ×2; erweitert: T3 Mischkarte H10, T4 Expedition H15); Suche: 9 bekannte alte Fehler.

**Zahlen vorher → nachher (gelesen, ohne Namen):**
- Karten-Stände 36, gelandet 34 → 34 (unverändert).
- H1: 1 offene Etappe mit früherer Landung und bestandenem Test – vorher überall „fertig“, nachher „wieder offen“ (Test getrennt sichtbar). Abflugtafel: 22 Flug-Stände, 7 ändern ihre Zahl der fertigen
  Etappen (6 höher, weil gelandete Etappen jetzt zählen, nicht nur bestandene Tests; 1 niedriger = die wieder offene); Summe fertiger Etappen 20 → 32; vollständig 1 → 1.
- H2: 1 offene Zeile aus der Übernahme mit erfundener Folge: `folge` 3 → 5 (nachgerechnet aus 5 eigenen Lösungen in Folge); die andere offene Zeile hat Folge 0 und bleibt. 0 Zeilen seit der Übernahme überschrieben.
- H3: 36 Karten-Stände bekommen die Liste gezählter Aufgaben (131 verschiedene Aufgaben); 0 Karten haben mehr eigene Lösungen als verschiedene Aufgaben → `eigene_loesungen` unverändert.
- H4: „sicher“ 0 → 0; Flug-Nachtest bestanden bei gelandeten Etappen 0; Misch-Belege 0. H9/H11/H15: 0 Expeditionen live.

**Antworten für ChatGPT:**
- **H1** Angenommen. Eine Funktion `schule.etappe_fertig`: fertig = gelandet; ein bestandener Test zählt nur, solange die Etappe nie gelandet war (alte Stände ohne Übungsweg). Gilt in `etappen_stand` (Etappe, Testsperre),
  in der `karte`-Antwort (App übernimmt `fertig` vom Server statt `fertig || sitzt`), in `schule_uebersicht` (Abflugtafel) und bei den Eltern (`wieder_offen`, „wieder offen“). Neu `geoeffnet_am`, `test_nachgewiesen` getrennt.
  Die Reiseroute (Ort/Stempel erreicht) bleibt bewusst testbasiert – ein Rückfall nimmt keinen Ort weg. Test: gelandet + Test → 2 Fehler in der Wiederholung → überall offen → 3 eigene in Folge → gelandet.
- **H2** Angenommen. `folge` offener Etappen nur in Zeilen ohne Übungsversuch seit der Übernahme (17.11. 15:17 UTC) aus den geordneten endgültigen Versuchen nachgerechnet; früher schon gelandete → 0.
- **H3** Angenommen. Für eigene Lösungen, Typen und „schwer“ zählt jede Aufgabe je Lernkarte einmal (`gezaehlt`); für „in Folge“ zählt jede eigene Lösung – sonst könnte eine Lernkarte mit genau 6 Aufgaben
  nach einem Fehler nie wieder landen. Nach dem Wiederöffnen sind eigene Lösungen/Typen/schwer schon erfüllt, es fehlen nur 3 in Folge; dafür zählen bekannte Aufgaben. Eine Regel „nach ≥ 1 Lerntag neu zählen“
  ist deshalb nicht nötig (nicht gebaut). Text „Die kennst du schon – gut wiederholt.“; die App nimmt ungezählte zuerst, gezählte nur, wenn keine ungezählte mehr da ist.
- **H4** Angenommen. „sicher“ verlangt jetzt: Misch-Beleg und im Flug-Nachtest die Aufgabe dieser Lernkarte richtig – beides nach der letzten Landung. Sonst bei den Eltern „Flug-Nachtest bestanden“.
- **H5** Angenommen: beide Rauchtests laufen über `uebung_pruefen_intern` und den Trigger. `api.schule_uebung_pruefen` ruft genau diese Funktion nach der Zugriffsprüfung; ein Zugangsschlüssel gehört nicht in eine Datei.
- **H6** Angenommen (bevorzugte Variante): `heute_selbst` zählt der Server aus bestätigten Versuchen im Tag des Kindes (`lernender.zeitzone`); die App zeigt den Wert und speichert ihn nur noch unter dem Ortstag, nicht UTC.
- **H7** Angenommen. Tipp: „zählt nicht als eigene Lösung; unterbricht deine Folge nicht“. „Punkte“/„Serie“ aus Kinder- und Elterntexten entfernt (auch in der Rückfall-Anzeige alter Server).
- **H8** Erledigt (eigene Meldung unten).
- **H9** Angenommen. Ein Expeditions-Teil wird nur gewertet, wenn alle Voraussetzungen gelandet sind oder die Expedition schon begonnen ist (Rückfall: zu Ende führen ohne Nachteil). `klasse` = nur Einordnung.
- **H10** Angenommen. `schule.misch_gueltig`: Pool Übung, Stufe 2–3, freigegeben, Etappe beim Kind gelandet, nicht die gerade geübte (App schickt `aktuell_einheit`, `aktuell_lernziel`). Sonst normale Buchung ohne Misch-Beleg.
  Negativtests: ohne aktuelle Etappe, aus der aktuellen Etappe, aus nicht gelandeter Etappe.
- **H11** Angenommen. `schule.expedition_etappe` sucht je Kind über `thema_id` + Lernkarte die gelandete Version; Test mit zwei Versionen.
- **H12** Angenommen. Import lehnt vor dem Schreiben ab: nicht 3–5 Teile, doppelte Kennung, fehlender Antworttyp/Frage/Lösung, < 3 Themen, Bezug außerhalb der Voraussetzungen, unbekannte Lernkarte,
  „geprueft/freigegeben“ ohne entsprechend geprüfte/freigegebene Bezugs-Flüge. `tools/inhalt_pruefen.py` prüft „≥ 3 Themen“ ebenfalls.
- **H13** Angenommen. Tests: Klasse 5 jede 6., Klasse 8 jede 4. (Server und App), nie mit nur 2 gelandeten, nie bei gewählter Stufe, alle 8 genau einmal, Lernkarte wechseln/Neustart beginnt neu, nach falscher Mischkarte normal weiter.
- **H14** Angenommen: Expedition (zweimal falsch, dann richtig, geschafft) und gesperrt laufen über `uebung_pruefen_intern`.
- **H15** Angenommen. Expedition meldet getrennt `teile_erledigt` (abgeschlossen) und `teile_selbst` (1. Versuch ohne Tipp); Kind: „x von n Teilen selbst gelöst“, Eltern ebenso. Misch-Beleg zählt für „sicher“ nur nach der letzten Landung.

**README** (`inhalte/README.md`) und Info-Seite (App) ergänzt: einmal zählen je Aufgabe, „Wieder offen“, „sicher“ nach der letzten Landung, Server-Prüfung der Mischkarten, Expeditions-Regeln H9/H11/H12/H15.

## 2026-11-18 – FERTIG: H8 (Fehler in Mischkarte/Expedition öffnet keine gelandete Etappe mehr) – sofort einspielbar

**Migration** `supabase/migrations/20261119_w176_h8_misch_fehler_offen_lassen.sql` (nicht ausgeführt; pglast ok; ersetzt die Live-Fassungen von `misch_buchen` und `expedition_buchen`, vorher gelesen; kein DROP, kein DELETE; keine App-Änderung nötig).
- Neu `schule.karte_faellig_machen(kind, einheit, lernkarte, zeit)`: Etappe am nächsten Lerntag fällig (`wdh_ab = jetzt`, `wdh_lerntage = 1`); `sitzt`, `wdh_stufe`, `wdh_fehler`, `misch_ok_am`, `angewandt_am` und alle übrigen Belege bleiben.
  Ist die Etappe schon fällig, bleibt der frühere Termin.
- `misch_buchen` und `expedition_buchen` rufen bei einem endgültigen Fehler nur noch diese Funktion (nicht mehr `karte_buchen(…, false)`); auch beim 2. und 3. Fehler und bei `wdh_fehler = 1` bleibt die Etappe gelandet.
  Wieder öffnen kann allein die fällige Wiederholung (`karte_buchen`, unverändert). `misch_buchen` zählt den Fehler zusätzlich in `falsch`.
- Hinweis: Wird die durch einen Mischfehler fällige Wiederholung bestanden, rückt die Wiederholungsstufe wie bei jeder bestandenen fälligen Wiederholung um 1 vor (unverändertes Verhalten von `karte_buchen`).

**Zahlen (gelesen vor dem Einspielen, ohne Namen):** 36 Karten-Stände, davon 34 gelandet; 1 Karten-Stand offen mit früherer Landung (nicht durch Mischkarte – es gibt noch 0 Mischkarten-Versuche);
0 Expeditionen, 0 Expeditions-Versuche → keine Etappe ist durch H8 betroffen, keine Reparatur nötig. Nachher erwartet: unverändert 34 von 36 gelandet.

**Rauchtest** `supabase/tests/w176_h8_rauchtest.sql` (Rollback, nur Testkind): Etappe gelandet mit `wdh_fehler = 1` → 2 endgültige Mischkarten-Fehler über den echten Trigger → bleibt gelandet, Belege gleich, fällig ·
Expedition 2 × falsch und gemischt mit Mischkarte → bleibt gelandet · Gegenprobe: 2. Fehler in der fälligen Wiederholung öffnet weiterhin.

**Antwort für ChatGPT (H8):** Angenommen. Mischkarten und Expeditionen haben jetzt einen eigenen Fehlerweg, der nur fällig macht; `sitzt` und Belege ändern sich nie, unabhängig von `wdh_fehler`. Das Öffnen bleibt der fälligen Wiederholung vorbehalten.

## 2026-11-18 – FERTIG: Fehler „Diese Aufgabe ist noch nicht freigegeben“ beim Prüfen; Rauchtest Teil 4 korrigiert – App 0.78.1

**Server – Migration** `supabase/migrations/20261118_w176_a_gesperrt_pruefen.sql` (nicht ausgeführt; pglast ok; Stelle im Live-Text genau einmal vorhanden; kein DROP, kein DELETE):
- `schule.uebung_pruefen_intern`: Eine gesperrte Bordkarte (`freigegeben = false`) wird beim **Prüfen** noch normal gewertet, wenn ihr Flug **geprüft oder freigegeben** ist. Die Sperre greift nur bei der
  **Auswahl** neuer Bordkarten (Übung, Wiederholung, Mischkarten, Knobel, Tests – unverändert). Entwurfs-Flüge bleiben für echte Kinder gesperrt (vorher schon über `einheit_pruefen_sichtbar`;
  gesperrte Bordkarte im Entwurf nur fürs Testkind, wie bisher).
- Die Datei läuft auf dem heutigen Stand **und** vor oder nach W176 Teil 1/3/4 (erkennt beide Fassungen der Stelle, zweimal einspielen schadet nicht). Sie kann sofort und unabhängig von „Live“ eingespielt werden.
- **Geändert in Teil 3** (`20261118_w176_t3_mischkarten.sql`, noch nicht eingespielt): fasst `uebung_pruefen_intern` an dieser Stelle nicht mehr an (sonst hätte Teil 3 die Prüf-Sperre fürs Testkind wieder verschärft
  bzw. die Stelle nicht mehr gefunden). Die beiden Auswahl-Stellen (Flug laden, Wiederholung) bleiben in Teil 3.
- Rauchtest `supabase/tests/w176_gesperrt_rauchtest.sql` (Rollback, ohne Namen): gesperrte Übung in freigegebenem Flug wird gewertet · gesperrte Übung im Entwurf bleibt für echte Kinder gesperrt.

**App 0.78.1** – kommt beim Prüfen trotzdem „… nicht freigegeben“ (z. B. bevor die Migration eingespielt ist): keine rote Meldung. Üben (auch Mischkarten), Wiederholung und Expedition laden still neu
und zeigen die nächste Bordkarte; eine Knobel-Bordkarte schließt sich still; im Test geht es zur nächsten Bordkarte (der Server prüft im Test nicht auf die Sperre – nur zur Sicherheit).
Gewertet wurde nichts, die Checkliste bleibt unverändert. Tests: Üben (neu geladen, keine Meldung, Checkliste gleich), Knobel und Wiederholung.

**Rauchtest Teil 4** `supabase/tests/w176_t4_rauchtest.sql`: Variable `k` → `ks` (kollidierte mit dem Tabellen-Alias `k`). Migration Teil 4 unverändert.

**Tests:** lernen 64 von 64; Suche: 9 bekannte alte Fehler.

## 2026-11-18 – FERTIG: Teil 4 (P3 Expeditionen, Technik) – App 0.78.0 – wartet auf Migration

**Migration** `supabase/migrations/20261118_w176_t4_expeditionen.sql` (nicht ausgeführt; pglast ok; Ersetzungsstellen im Live-Text vorhanden; setzt Teil 1 und Teil 3 voraus; kein DROP von Tabellen/Spalten/Funktionen, kein DELETE).
**Ausnahme wie bei Migration F:** `aufgabe_pool_check` (+ `expedition`) und `sterne_grund_check` (+ `expedition`) werden als „drop constraint + add constraint“ in einem Befehl erweitert.

- **Datenmodell (Entscheidung):** Kopf in neuer Tabelle `schule.expedition` (schluessel, klasse, titel, einleitung, grafik, voraussetzungen mit thema_id, autor, status entwurf/geprueft/freigegeben, version);
  **Teile als Zeilen in `schule.aufgabe`** (pool `expedition`, `expedition_id`, `teil`; einheit_id/variante_gruppe = Etappe des Bezugs). Begründung: Teile sind Bordkarten – Bewertung, zweiter Versuch,
  Lösung und `schule.versuch` (aufgabe_id Pflicht) laufen unverändert; der eigene Pool hält Teile aus Übung, Mischkarten, Wiederholung und Tests heraus. `aufgabe_schutz` nimmt Expeditions-Teile aus
  (sonst wären Teile mit Bezug auf einen freigegebenen Flug nicht abgleichbar).
- **Import/Abgleich:** `schule.expedition_importieren(datei jsonb, status text default null)` – neu anlegen oder nach `schluessel` bzw. Teil-Kennung `k` abgleichen; Teile, die nicht mehr in der Datei stehen,
  werden gesperrt, nichts gelöscht. Neu = `entwurf` (nur Testkind), Status per zweitem Argument.
- **Angebot:** nur wenn **alle** Voraussetzungs-Lernkarten beim Kind gelandet sind (jede Version der Einheit des Themas), Plan-Reihenfolge egal; Entwurf nur Testkind.
- **Ablauf/Belege:** Teil erledigt = richtig oder endgültig (2. Versuch bzw. Lösung gezeigt). Richtig im 1. Versuch ohne Tipp → `karte_stand.angewandt_am` der Bezugs-Etappe (Anzeige mit P5).
  Endgültig falsch → Bezugs-Etappe am nächsten Lerntag fällig (wie eine falsche Mischkarte; gebucht über `karte_buchen` mit einer Übung dieser Etappe). Keine Minuspunkte, zählt nicht für „gelandet“.
- **Sterne/Stempel:** Vorschlag `sterne_expedition_geschafft` = 50 (ein Ort 100) bei „alle Teile erledigt“, je Expedition einmal; jeder richtige Teil wie jede Bordkarte 10. Stempel = `konto.expeditions_stempel`.
- **Felder für die App (keine neue Aktion in lernen-api):** `schule_konto.expeditionen` (angeboten/begonnen/geschafft, mit Teilen; Lösung nur bei erledigten), `konto.expeditions_stempel`;
  `schule_uebung_pruefen` nimmt Teile an und antwortet mit `expedition: {id, teil, erledigt, geschafft, sterne}`; `schule_uebersicht`: je Kind `expeditionen [{id, zustand}]`,
  für Eltern/Lehrer oben `expeditionen` (alle, mit Lösungen).

**App 0.78.0** (ohne Migration: keine Expeditionen sichtbar)
- Kind: Karte „⛰ EXPEDITION“ auf der Abflugtafel (begonnene zuerst), Seite `#/expedition/<kind>-<id>`: Einleitung und Grafik, Teil für Teil mit 2 Versuchen; danach Lösung und Weg,
  „Keine Abzüge – im nächsten Teil geht es mit den richtigen Zahlen weiter.“, „Weiter mit Teil B ›“; erledigte Teile bleiben sichtbar; Abbruch jederzeit (Stand kommt vom Server);
  Abschluss „EXPEDITION GESCHAFFT“ mit Sternen; Reisepass „⛰ Expeditions-Stempel: n“.
- Eltern/Lehrer: Lehrplan-Übersicht → „Expeditionen ansehen“ (`#/expeditionen`, mit Status, Voraussetzungen, Teilen, Lösungen); Lernstand des Kindes: Abschnitt „Expeditionen“ (angeboten/begonnen/geschafft);
  in „Inhalte ansehen“ eines Flugs erscheinen Expeditions-Teile nicht. Info-Seite: „Expeditionen“.
- Grafik: die App zeichnet wie bisher; das Kind liest ab und wählt aus, gezeichnet wird nicht.

**Rauchtest** `supabase/tests/w176_t4_rauchtest.sql` (nach dem Einspielen; Rollback; Testkind; importiert „Handytarif“ als Entwurf): Entwurf nur Testkind · ohne alle Voraussetzungen kein Angebot ·
alle gelandet → angeboten · Teil falsch → erledigt, Bezugs-Etappe fällig · Abbruch verliert nichts · Teil richtig → Beleg · alle Teile → geschafft, Sterne genau einmal · Abgleich ohne Änderung ändert nichts,
entfernter Teil wird gesperrt, nicht gelöscht.
**Tests:** lernen 62 von 62 (neu T4: Angebot und Durchlauf mit Fehler/2. Versuch/Lösung/nächster Teil/Abschluss; Abbruch und kein Angebot; Eltern-Ansichten). Suche: bekannte alte Fehler (diesmal 10, schwankend).
**Nicht geprüft:** Migration gegen echte Daten; die Handytarif-Grafik in der echten App (nur im Test-Mock ohne Grafik).

## 2026-11-18 – FERTIG: IB richtig beschriften (Auftrag 18.11. 03:33, Punkt 2) – in App 0.78.0

- Einheitlich **MYP-Jahr = Klasse − 5** (vorher an einer Stelle Klasse − 4); ein Kind in Klasse 5 steht **vor MYP-Jahr 1** (Stufe 0, Anzeige „vor MYP-Jahr 1“, 0 Flüge). Linienplan unverändert (MYP-Jahr n unter Klasse n + 5).
- Beschriftung überall „MYP-Jahr n“ (Lernstand-Tabelle, Einstieg prüfen, Mini-Linien, Passkarte, Lehrplan-Übersicht „IB MYP-Jahr n“, Flugplan, Vorlage, Stufen-Auswahl), Hinweis „MYP-Jahr 1–5 entspricht etwa Klasse 6–10“
  (Linienplan-Name, IB-Reiter im Lernstand, Lehrplan-Übersicht, Stufen im Flugplan, Info-Seite „Worauf baut die App auf?“ – vorher stand dort „MYP 1–4“).
- Test: Umrechnung (Kl. 5 → 0, Kl. 8 → 3, Kl. 10 → 5, gesetzte Stufe bleibt), Spaltenköpfe „MYP-Jahr 1…5“, Hinweis, Info-Seite, kein „Klasse − 4“ mehr im Quelltext. Punkte 1 und 3 des Auftrags: siehe Eintrag „Teil 3 (korrigiert)“ unten.

## 2026-11-18 – FERTIG: Teil 3 (korrigiert) und Wunsch „Lernen starten“ – App 0.77.1

**Korrektur Migration** `supabase/migrations/20261118_w176_t3_mischkarten.sql` (weiter nicht eingespielt; pglast ok; Stellen im Live-Text vorhanden):
- `schule.mischkarten` nimmt nur noch `a.freigegeben` – gesperrte Aufgaben nie als Mischkarte, auch nicht für das Testkind. Entwurfs-Flüge des Testkinds bleiben über `e.status` erlaubt.
- **Dieselbe Stelle gab es dreimal anderswo** (Live-Text gelesen) – dort gilt jetzt dieselbe Regel (Abschnitt am Ende der Migration):
  `schule.einheit_lesen_intern` (Übungen und Knobel-Bordkarten der Einheit: `a.freigegeben or Testkind` → `a.freigegeben`),
  `api.schule_wiederholung` (`a.freigegeben or v_test` → `a.freigegeben`), `schule.uebung_pruefen_intern` (Testkind durfte gesperrte Aufgaben prüfen → jetzt nicht mehr).
  Folge: Das Testkind sieht beim Üben und in der Wiederholung keine gesperrten Aufgaben mehr; Entwurfs-Flüge sieht es weiter (Status der Einheit). Zahlen heute: in Entwurfs-Flügen
  2 797 freigegebene und 1 500 gesperrte Übungen, in freigegebenen Flügen 11 427 / 3 457 – das Testkind übt also weiter Entwürfe, nur ohne die gesperrten.
  Bitte bewusst mit einspielen; wer das für das Testkind anders will, nimmt den letzten Block heraus (die Mischkarten-Korrektur steht davon getrennt in `schule.mischkarten`).
- Rauchtest `supabase/tests/w176_t3_rauchtest.sql` unverändert; Fall 2 prüft genau diese Bedingung.

**Wunsch 18.11. – „Lernen starten“ an der Kinderkarte** (Eltern/Lehrer-Startseite): erster, hervorgehobener Knopf „Lernen starten ›“ (Akzentfarbe, öffnet `#/reise/<id>`), danach „Lernstand“,
„Was wackelt?“, „Flugplan“; „Lernreise ansehen“ entfällt (gleiches Ziel). Auf dem Handy (≤ 600 px) steht „Lernen starten“ allein über die ganze erste Zeile.
Info-Seite: Absatz „Lernen starten“ oben. Test: Reihenfolge, Hervorhebung, erste Zeile auf 390/820/1280 px (auf 390 px allein), Klick öffnet die Abflugtafel, Info-Satz.

**Tests:** lernen 58 von 58. Suche: die bekannten alten Fehler (diesmal 10 – W80 Nr. 108 schwankt; „PWA …“ und „Lernen Schule: Startkarte …“ scheitern auch ohne diese Änderung). Prüfskript 96 von 96 OK.

## 2026-11-18 – FERTIG: Teil 3 (P2 Mischkarten) – App 0.77.0 – wartet auf Migration

**Migration** `supabase/migrations/20261118_w176_t3_mischkarten.sql` (nicht ausgeführt; pglast ok; Ersetzungsstellen im Live-Text je genau einmal vorhanden; setzt Teil 1 voraus; kein DROP, kein DELETE).
- Neu: `karte_stand.misch_ok_am`, `versuch.misch`, Regeln `misch_jede` = 4, `misch_jede_bis_kl6` = 6, `misch_ab_gelandet` = 3 (Startwerte in `schule.regel`).
- `schule.mischkarten(kind, einheit)`: je gelandeter Etappe des Kindes eine Übung (Pool `uebung`, Stufe 2–3, freigegeben; Entwürfe nur Testkind), am seltensten gesehen;
  Rang: gleicher Flug → gleicher Kontinent → älterer Flug; höchstens 8. Dynamisch je Kind, unabhängig vom Flugplan.
- `schule.misch_buchen` (über den Trigger `versuch_karte`, wenn `versuch.misch`): richtig im 1. Versuch ohne Tipp → `misch_ok_am`; endgültig falsch → wie ein Fehler in der Wiederholung
  (am nächsten Lerntag fällig, zwei hintereinander wie bisher); Tipp/2. Versuch richtig → nichts. Ist die Herkunfts-Etappe nicht gelandet, wird normal gebucht.
- „sicher“ (`karte_sicher`) verlangt jetzt zusätzlich `misch_ok_am`.
- **Keine neue Aktion in lernen-api.** Neue Felder: `schule_einheit_lesen`: `mischkarten[]` (Bordkarte + `einheit_id, lernziel, quelle, etappe, stadt`), `misch_jede`, `misch_ab`;
  `schule_uebung_pruefen` nimmt `misch: true` an und antwortet dann mit `misch: {lernziel, einheit_id, etappe, stadt, ok}` und **ohne** `karte`; `etappen_stand` und `schule_lernstand`: `misch_ok`.

**App 0.77.0** (ohne Migration: keine Mischkarten, alles wie bisher)
- Start, wenn im aktuellen Flug mindestens `misch_ab` (3) Etappen gelandet sind; dann jede `misch_jede`-te Bordkarte (4, bis Klasse 6: 6) eine Mischkarte; nie bei gewählter Stufe.
- Auswahl (`lernMischWahl`): gleicher Flug zuerst, dann Kontinent; jede 3. Mischkarte aus einem älteren Flug; nie die gerade geübte Etappe, nie Knobel-Bordkarten; jede Karte höchstens einmal je Sitzung.
- Anzeige neutral: „BORDKARTE n · AUS DEINER REISE“, „Aus deiner Reise – erkennst du, was gefragt ist?“, kein Link zur Erklärung, kein Etappen-Muster im Detektiv;
  nach der Lösung „Das war: <Etappe> – <Stadt>“. Die Checkliste der aktuellen Etappe bleibt unverändert.
- Eltern: „Was wackelt?“ zeigt „in einer Mischkarte erkannt ✓“. Info-Seite (Mischkarten, „sicher“) und README (Mischkarten; Übungen müssen für sich allein verständlich sein) angepasst.

**Rauchtest** `supabase/tests/w176_t3_rauchtest.sql` (nach dem Einspielen; Rollback; nur Testkind): ohne gelandete Etappe keine Mischkarte · nur gelandete Etappen, Pool uebung, Stufe 2–3, freigegeben ·
richtig → Beleg, Wiederholung unverändert · falsch → am nächsten Lerntag fällig, bleibt gelandet · Versuch mit `misch` angenommen · keine Knobel- oder gesperrten Bordkarten.
**Tests:** lernen 57 von 57 (neu: Auswahlregeln inkl. weniger als 3 gelandet, Dosis jede 6.; Mischkarte beim Üben mit Kennzeichnung, ohne Erklärung, „Das war …“, `misch: true`, aktuelle Etappe unverändert,
kein Knobel). Suche: 9 bekannte alte Fehler.
**Nicht geprüft:** Migration gegen echte Daten (Rauchtest nach dem Einspielen). Die Grenze „höchstens 6 Wiederholungen vor einem Flug“ ist unverändert (Mischkarten sind keine Wiederholungen;
eine falsche Mischkarte macht die Etappe nur fällig).

## 2026-11-18 – FERTIG: Teil 2 (Format für Expeditionen: README, Prüfskript, Beispiel „Handytarif“)

Kein App-Code, keine Migration. Darauf können die Inhalte-Chats für Expeditionen aufsetzen.

- **inhalte/README.md**, neuer Abschnitt „Expeditionen“ (am Ende): Dateien `inhalte/expeditionen/<klasse>-<name>.json` aus `inhalte/generatoren/expedition_<name>.py`;
  Felder `schluessel, klasse, titel, einleitung, grafik?, voraussetzungen[{thema_schluessel, lernziel}], teile[3–5], autor?`;
  je Teil die Felder einer Bordkarte (`k, y, f, a, o, c, w, h?`) und `bezug {thema_schluessel, lernziel}`; Regeln inkl. „kein Folgefehler-Domino“ (jeder Teil nennt seine Werte);
  vollständiges Beispiel im Wortlaut.
- **tools/inhalt_pruefen.py** prüft Expeditionen (erkennt sie am Ordner `expeditionen` oder am Feld `teile`; `--alle` nimmt sie mit): Pflichtfelder, Dateiname = schluessel = `<klasse>-<name>`,
  Voraussetzungen existieren (Thema und Lernkarte in `inhalte/themen/`), Plan-Klasse jedes Voraussetzungs-Themas ≤ Klasse der Expedition, Bezug jedes Teils in den Voraussetzungen
  (ungenutzte Voraussetzung = Hinweis), 3–5 Teile, keine doppelten Fragetexte/Kennungen, Antwortform je Typ wie bei Bordkarten, `c` Pflicht bei `zahl`/`luecken` und nachgerechnet.
  Gegenprobe mit absichtlich falschen Varianten (Klasse 9 als Voraussetzung, falsche Lösung, fremder Bezug, 1 Teil, doppelter Text, unbekanntes Thema) – alle erkannt. `--alle`: 96 von 96 OK.
- **Beispiel** `inhalte/expeditionen/8-handytarif.json` (Generator `inhalte/generatoren/expedition_handytarif.py`), Voraussetzungen funktionen.linear/aufstellen, funktionen.linear/graph_ablesen,
  gleichungen.ungleichungen/sachaufgabe, bruch.prozent_grundwert/vermehrt:
  a) Term für Tarif A in Cent (Lücken `□x + □` → 10x + 500) · b) Welcher Graph gehört zu A? (Koordinatensystem mit 3 Geraden: richtig, Minutenpreis halbiert, Grundgebühr vergessen) ·
  c) Ab wie vielen ganzen Minuten ist B (12 € Flat) günstiger? → 71 · d) B wird 15 % teurer (13,80 €) → 89. Jeder Teil nennt die nötigen Werte.
- **Nicht geprüft:** wie die App die Grafik von Teil b zeichnet (kommt mit Teil 4); dass Folgeteile ohne Vorteil lösbar sind, prüft das Skript nicht mechanisch (Regel in der README).

## 2026-11-17 16:50 – FERTIG: Teil 1 (P1 Punkteregel „gelandet“ ohne Minuspunkte) – App 0.76.0 – wartet auf Migration

**Migration** `supabase/migrations/20261118_w176_t1_punkteregel.sql` (nicht ausgeführt; pglast ok; Ersetzungsstellen im Live-Text je einmal vorhanden; kein DROP, kein DELETE).
- `schule.karte_stand` neu: `eigene_loesungen int`, `typen text[]`, `folge int`, `fehler_folge int`, `stufe_senkung smallint` (alle mit Standardwert, nicht null).
- `schule.karte_buchen` neu gefasst (Regel siehe unten); neue Funktionen `schule.karte_typen_noetig(einheit, lernziel)` und `schule.karte_sicher(karte_stand)`.
- **Entscheidung `serie`:** bleibt als Spalte und wird weiter geschrieben als `least(eigene_loesungen, ziel)`. Die alte App 0.75.1 läuft damit ohne Fehler weiter
  (zeigt Punkte, wird nie weniger). Einziger sichtbarer Unterschied bis zum Wechsel: volle Punkte, aber noch nicht „sitzt“, solange Typen oder Folge fehlen.
- **Bestandsübernahme** (einmalig, nur Zeilen, die noch nicht übernommen sind): `eigene_loesungen = serie`, `folge = least(serie, 3)`, `typen` aus `schule.versuch`
  (richtig, 1. Versuch, ohne Tipp, mit `aufgabe.typ`). `sitzt` wird nicht angefasst → sitzende Etappen bleiben sitzend.
  Zahlen heute (gelesen): 31 Karten-Stände, davon 28 sitzend, Summe `serie` 73. Nach der Migration erwartet: 28 sitzend, Summe `eigene_loesungen` 73 (Rauchtest gibt beide Zahlen aus).

**Regel „gelandet“** (`sitzt = true`): eigene_loesungen ≥ ziel · Typen ≥ `karte_typen_noetig` (2, wenn die Etappe ≥ 2 Typen hat) · `schwer_ok` (Stufe-3-Typ), wenn nötig · `folge ≥ min(3, ziel)`.
Eigene Lösung: +1, folge +1, fehler_folge 0, stufe_senkung −1. Endgültig falsch: folge 0, fehler_folge +1, nach je 2 Fehlern in Folge stufe_senkung +1 (höchstens 2). Tipp/2. Versuch richtig: nichts.
Wiederholung unverändert (1/3/7/14/30 Lerntage); zwei Fehler in der Wiederholung → wieder offen, Belege bleiben, es fehlen wieder 3 in Folge (vorher: Punkte auf 0).
**„sicher“** = gelandet + `wdh_stufe ≥ 4` (Wiederholung nach 14 Lerntagen bestanden) + Nachtest des Flugs bestanden; die Mischkarte kommt mit Teil 3 dazu.

**Neue Felder für die App:** `schule_uebung_pruefen.karte` und `schule_einheit_lesen.etappen_stand[lernziel]`: `eigene_loesungen, folge, folge_ziel, typen_anzahl, typen_noetig, fehler_folge, stufe_senkung, sicher`;
`schule_lernstand.karten[]`: `eigene_loesungen, folge, typen_anzahl, sicher`. Keine neue Aktion in lernen-api.

**App 0.76.0** (läuft ohne Migration wie bisher, mit Punkten):
- Satz „Ein Fehler kostet 2 Punkte“ gestrichen; nach einem Fehler steht „Die nächste zählt wieder voll.“ (beide Gestaltungen).
- Statt Punkten eine Checkliste: „Eigene Lösungen 4/6 · 2 Aufgabentypen ✓ · schwere ✓ · 3 in Folge: 1/3“; daneben „heute X Aufgaben selbst gelöst“ (Zähler je Kind und Tag auf dem Gerät, ohne Bezug zur Schwelle).
- Stufenwahl: nach eigenen Lösungen, minus `stufe_senkung`.
- Landung: „GELANDET“ bleibt, Zusatz „Sicher wird die Etappe, wenn du sie in ein paar Tagen wieder kannst.“; „Sicher!“ beim Üben einer sicheren Etappe.
- Eltern: „Was wackelt?“ zeigt „gelandet“/„sicher“ und je offener Etappe „x eigene Lösungen · y in Folge · z Arten von Bordkarten“; Lernstand-Zellen „gelandet – nach N Bordkarten“.
- Info-Seite („Etappe gelandet“, „Etappe sicher“, Wiederholung) und `inhalte/README.md` (Abschnitt „Lernregel ‚gelandet‘ und ‚sicher‘“). Nirgends mehr „−2“ oder „Punkte verlieren“ (Test prüft den Quelltext).

**Rauchtest** (nach dem Einspielen, Transaktion mit Rollback, nur Testkind): `supabase/tests/w176_t1_rauchtest.sql` – Fälle: 6 richtige mit nur einem Typ → nicht gelandet ·
letzte falsch → nicht gelandet, folge 0, keine Abzüge · Tipp-Treffer zählt nicht und bricht die Folge nicht · danach 3 in Folge → gelandet · 1 Fehler senkt nicht, 2 in Folge senken um 1 ·
Etappen mit wenigen Übungen (Hinweis) · Knobel zählt nicht · Bestandszahlen (sitzend, Summe serie/eigene).

**Tests:** lernen 55 von 55 (neu: Checkliste/„heute“/„Die nächste zählt wieder voll.“, Stufensenkung + kein Minuspunkt-Text, gelandet/sicher für Kind und Eltern). Suche: 9 bekannte alte Fehler.
**Nicht geprüft:** die Migration gegen echte Daten (Rauchtest erst nach dem Einspielen); der Zähler „heute“ zählt nur auf dem Gerät des Kindes.

