# Postfach bau-lehrer (Bau-Chat, Bau-Auftrag LA – Lehrer-Aufbau)

Neueste oben. Zweig `bau-lehrer` von `lernen-app` (b8f910e). Kein Merge.

## 2026-11-23 – FERTIG: WD-5

Stand `lernen-app` e2a8fcd übernommen. Nur Dateien, nichts eingespielt, kein DROP/DELETE, kein App-Code.
- neu: `supabase/migrations/20261128_wd5_staffel_drosseln.sql`, `supabase/tests/wd5_rauchtest.sql`
- angepasst: `supabase/tests/wd_s_rauchtest.sql`, `supabase/tests/wd_s3_rauchtest.sql`. Beide merken sich den Regelwert und stellen ihn wieder her, statt fest „6“ zu setzen.
- **Einspielen:** nach WD-S, WD-4b, WD-S 4 (alle echt vorhanden). Einmalig: Ein zweiter Lauf tut nichts.

**Umsetzung**
1. **Regel:** `wdh_gesetzt_je_lerntag` = 3. Neu gesetzte Etappen kommen damit zu 3 je Lerntag (`wdh_staffel_tag` liest die Regel), ebenso `wdh_staffel_strecken`.
2. **Neuverteilung `schule.wdh_staffel_drosseln`:**
   - **Betroffen:** alle gesetzten Etappen in erster Wiederholung (`wdh_gesetzt_am` gesetzt, Stufe 0, kein Fehler, nicht abgelegt), heute fällige und schon eingeplante.
   - **Reihenfolge:** Plan-Reihenfolge (Platz, Einheit, Etappe), höchstens 3 je Lerntag ab heute.
   - **Offene Runde von heute:** bleibt und belegt heutige Plätze.
   - **Geändert:** nur `faellig_am`, `wdh_ab`, `wdh_lerntage`, und nur bei geändertem Lerntag. Alles andere wird am Ende geprüft, sonst Abbruch.
3. **Sicherung:** in `schule.wdh_staffel_sicherung` mit neuer Spalte `lauf = 'wd5'`.
   - Für 28 der verschobenen Etappen steht dort schon eine WD-4b-Sicherung. Sie wird in der neuen Spalte `frueher` aufbewahrt und beim Rückweg wiederhergestellt.
   - **Rückweg:** `select schule.wdh_drosseln_zurueck();` (oder je Kind). Abgelehnt, sobald eine verschobene Etappe geübt wurde; die Regel bleibt dann 3.
   - `wdh_staffel_zurueck` (WD-4b) fasst nur noch WD-4b-Sicherungen an.
   - **Auf dem echten Stand gilt:** Die 28 WD-4b-Sicherungen sind noch unberührt (lesend geprüft).

**Vorher/Nachher (echter Stand 23.11. lesend; Lauf der Migration auf einer lokalen Kopie dieser Daten – gleiche Zahlen)**
- **Kind 1:** keine gesetzten Erst-Wiederholungen, unverändert. Fällig je Lerntag 0–13: 0 6 4 6 6 4 2 0 0 0 0 0 0 0.
- **Kind 2:** 42 gesetzte Erst-Wiederholungen, keine offene Runde heute (die heutige ist fertig). 39 werden verschoben, 3 bleiben heute fällig.

| Lerntag | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vorher fällig | 23 | 11 | 11 | 12 | 6 | 9 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| davon gesetzt | 10 | 6 | 6 | 6 | 6 | 6 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| nachher fällig | 16 | 8 | 8 | 9 | 3 | 6 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| davon gesetzt | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |

**Hochrechnung Rückstau (fällig nach der Runde) je Lerntag, Kind 2**
- **Annahmen:** eine Runde je Lerntag, alle richtig im ersten Versuch, älteste zuerst, keine neuen Landungen oder Setzungen. Bestanden heißt nächste Stufe nach 3/7/14/30 Lerntagen. Lerntag 0: Runde schon gemacht.

| Lerntag | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 12 | 14 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| heute (6/Tag, Runde ÷5) | 23 | 27 | 30 | 33 | 32 | 36 | 37 | 33 | 35 | 34 | 33 | 33 | 27 | 18 |
| WD-5 (3/Tag, Runde ÷5) | 16 | 18 | 20 | 23 | 21 | 23 | 24 | 24 | 28 | 30 | 29 | 29 | 30 | 21 |
| WD-5 + Runde bis 12 | 16 | 12 | 8 | 5 | **0** | 2 | 0 | 0 | 3 | 1 | 2 | 0 | 0 | 0 |
| nur Runde bis 12 (6/Tag) | 23 | 22 | 21 | 21 | 18 | 26 | 24 | 18 | 21 | 17 | 15 | 5 | 0 | 0 |

- **Befund:** 3 je Lerntag allein löst den Stau **nicht** auf (er pendelt um 20–30). Grund: Die Runde (Rückstau ÷ 5, mindestens 6) ist meist 6. Das ist kaum mehr als der Zulauf aus 3 neuen und den zurückkommenden Wiederholungen.
- **Vorschlag (nur Regelwert, kein Code):** `wdh_runde_teiler` 5 → 1. Die Runde ist dann alle fälligen, höchstens 12 (bis Kl. 6 höchstens 10).
  - Mit WD-5 ist der Stau nach etwa 4 Lerntagen weg und bleibt danach bei 0–4.
  - Ohne WD-5 dauert es etwa 13 Lerntage.
  - **Preis:** bis zu 12 Wiederholungen je Lerntag statt 6, also etwa doppelte Wiederholungszeit, bis der Stau weg ist.
  - **Milder:** Teiler 2 – Rückstau 16 → 12 → 10 → 9 → 7 → 9 → 9 → 7, auch nach 14 Lerntagen noch um 10; erst nach rund 20 Lerntagen bei 0.
  - Entscheidung Sebastian. `update schule.regel set wert = '1' where schluessel = 'wdh_runde_teiler'` ginge jederzeit und ohne Migration.

**Rauchtest `wd5`** (Transaktion, Rollback; spielt WD-5 zweimal ein)
1. Regel 3, höchstens 3 gesetzte Erst-Wiederholungen je Lerntag.
2. Reihenfolge nach Plan.
3. Nur die Fälligkeit gesetzter Erst-Wiederholungen ist geändert. Offene Runde, übrige Etappen, höhere Stufen, Lernstände, Plan und Sterne sind unverändert.
4. Rückweg echter Bestand: alles zurück, WD-4b-Sicherungen wieder da. Erneut drosseln ergibt die gleiche Verteilung.
5. Testkind:
   - 2 Etappen in der offenen Runde bleiben und belegen heute; 1 weitere bleibt heute, dann 3 / 2.
   - Höhere Stufe und nicht gesetzte Etappe bleiben.
   - Neu Gesetzte (`wdh_staffel_tag`) kommen ab Lerntag 2.
   - Rückweg nach Zwischenübung abgelehnt, sonst zurück. WD-4b-Rückweg fasst WD-5 nicht an.

**Lokal gelaufen** (Kopien wie echt; zusätzlich Kopie mit den echten Karten, Lerntagen, Runden, Plänen und Sicherungen der Kinder):
- `wd5` grün vor und nach dem Einspielen. `wd_s3` und `fp_s` grün vor und nach (Regel jetzt 3).
- `wd_s` lokal schon vor WD-5 rot (fehlende Auszüge, FEHLER 2), Ergebnis vor und nach gleich.
- `wd_s3` auf der Kopie mit echten Karten rot bei FEHLER 3, ebenfalls vor und nach gleich (Mischkarten-Verlauf nicht mitkopiert).
- `nb_s, zp_s` weiter grün.
- **Lesend auf dem echten Stand nachvollzogen:** Funktionen (`karte_wdh_in`, `wdh_staffel_zurueck` md5-gleich mit lokal), Regeln, Runden, Sicherungen, Verteilung. Das Testkind hat heute keine Runde. Die Tests selbst schreiben (Rollback) und sind deshalb nur lokal gelaufen.

## 2026-11-23 – FERTIG: NB-S 3 / SJ-S 3

Stand `lernen-app` 11e1544 übernommen. Nur Tests geändert, **Migrationen unverändert**; nichts eingespielt, kein DROP/DELETE, kein App-Code.
- geändert: `supabase/tests/nb_s_rauchtest.sql`, `supabase/tests/sj_s_rauchtest.sql`, `supabase/tests/zp_s_rauchtest.sql` (Tests 12 und 13 neu).
- Lesend auf dem echten Stand nachvollzogen: Funktionen (`karte_buchen` und `karte_wdh_ereignis` lokal md5-gleich mit echt), Auswahl der Test-Daten je Test, Sterne des Testkinds. Die Tests selbst schreiben (mit Rollback) und sind deshalb nur lokal gelaufen.

**1. nb_s – „unerwartete Sterne“: Fehler im Test, nicht in NB-S**
- Das Testkind hat auf dem echten Stand schon Sterne aus früheren Probeläufen (lesend gezählt: landung 80 ×5, landung 40 ×1, uebung 10 ×12).
- Test 5 prüfte alle Sterne des Testkinds statt nur der neuen. Neu dazu kam im Test nur ein Landungs-Bonus (das 6. „landung 80“).
- **Neu:**
  - Test 1 prüft wie bisher, dass das Einspielen nichts ändert.
  - `nb_lesen` prüft in Test 2–4, dass alle Lese-Stellen von NB-S (Liste, Konto, Übersicht, Reisekarte) nichts verändern.
  - Die Buchungen der nachgestellten Antworten (bisherige Regeln) meldet Test 5 nur noch, ab dem Aufbau gezählt. Fahrplan, Stempel und andere Kinder bleiben geprüft.
- **Berichtigung meiner Meldung NB-S („Tipp löscht den Fehler-Zähler“): falsch.**
  - Auf dem echten Weg über `versuch` setzt `versuch_hilfe_merken` die Hilfe. `karte_wdh_ereignis` (WD-S 3/4) hält dann bei „richtig mit Tipp“ in der fälligen Wiederholung den Fehler-Zähler.
  - „Fehler – (nächster Lerntag) richtig mit Tipp – Fehler“ öffnet also wieder.
  - Den Zähler löscht nur eine richtige Antwort, solange die Etappe nicht fällig ist (am selben Tag nach dem Fehler).
  - Der Test bildet das jetzt nach (Hilfe gesetzt wie über `versuch`, „nächster Lerntag“ = wieder fällig) und prüft genau diese Folge.
- Auswahl auf dem echten Stand (lesend): Testkind, Einheit 3, Etappe mit 20 Übungsaufgaben, Ort mit 3 Themen. Bisher keine wieder offene Etappe beim Testkind.

**2. sj_s – „kann er“ machte zwei Flüge fertig: Fehler im Test, `schuljahr_stand` zählt richtig**
- **Ursache (lesend):** Der Test nahm das Pflicht-Thema mit den meisten Etappen. Auf dem echten Stand ist das Thema 98 am Ort 80, und dort liegen zwei Themen (98, 44).
- Gesetzt hat der Test `route.kann_schon = true`. Das heißt „kann er“ für den **ganzen Ort** (`thema_kann_schon`: `kann_schon` oder Thema in `kann_schon_themen`). Also werden beide Flüge fertig, das ist richtig.
- **Neu:**
  - Erst „kann er“ nur für das Thema (`kann_schon_themen`): genau +1 fertig, das Thema mit allen Etappen.
  - Dann der ganze Ort: alle Pflicht-Themen des Orts fertig mit allen Etappen.
- Auf dem echten Stand läuft das mit dem Testkind Kl. 7 (Thema 98, 9 Etappen; Ort 80 mit 2 Themen). Lokal mit nur einem Thema am Ort geprüft.

**3. ZP-S – neue Testfälle aus ChatGPT 966 (`zp_s` Test 12 und 13)**
- **Test 12: zwei eingeplante Zusatz-Flüge am selben Ort.** Diesen Fall gibt es heute nicht (lesend: jeder Zusatz-Teil hat einen eigenen Ort: 233, 234, 235, 109, 237). Im Test nachgestellt: zwei Themen eines Orts für die Gruppe als Zusatz markiert. Verhalten:
  - **Stempel je Teil** (`flug_erstabschluss` je Einheit): 2.
  - **100 Sterne nur einmal je Ort**, nicht je Teil: Die Buchung hat den Schlüssel `ort` / `block:<Ort>` (eindeutig je Kind).
  - Der Ort wird erst nach dem zweiten Teil fertig.
  - **Ungenau:** `zusatz_geschafft.sterne` und damit `zusatz_plan[].sterne` zeigen bei **beiden** Teilen 100, gebucht ist nur einmal.
  - **Gleiche Wirkung bei Ort mit Pflicht-Thema und eingeplantem Zusatz-Thema:** Die 100 des Orts gehen dann schon beim Zusatz weg, beim Abschluss der Pflicht kommt nichts mehr.
  - Bitte entscheiden: 100 je Teil (Schlüssel je Thema) oder je Ort (so wie jetzt; dann das Feld auf die tatsächlich gebuchte Menge setzen). Beides bräuchte eine kleine Nach-Migration ZP-S 2; heute ohne Wirkung, weil es keinen solchen Ort gibt.
- **Test 13: abgeschlossenen Zusatz-Flug aus dem Plan nehmen.**
  - Die Route steht danach auf `entfernt`. Stempel, 100 Sterne und `zusatz_geschafft` bleiben, nichts wird zurückgebucht.
  - Im `zusatz_plan` steht der Flug nicht mehr. Die Stufe fällt auf „nicht im Plan“, weil der Zusatz ohne Eintrag wieder freiwillig ist und keine Pflicht-Etappe hat.
  - Wieder einplanen: Route wieder `fertig`, nichts doppelt.
  - Hinweis für die App: Ein herausgenommener, geschaffter Zusatz zeigt im Lehrplan „nicht im Plan“ statt „geschafft“. Der Stempel bleibt im Reisepass.

**Rauchtests** (lokal, Kopien wie echt): 50 Läufe grün.
- Tests: `nb_s, sj_s, zp_s, tl_s, rd_s, ex_s, lz_s, nt_s, lk_s, fp_s`.
- Stände: vor ZP-S, nach ZP-S, NB → SJ, SJ → NB, Testkind in Kl. 8.

## 2026-11-23 – FERTIG: NB-S 2 / SJ-S 2

Stand `lernen-app` 31d5374 übernommen. Nur Dateien, nichts eingespielt, kein DROP/DELETE, kein App-Code.
- geändert: `supabase/tests/nb_s_rauchtest.sql`, `supabase/tests/sj_s_rauchtest.sql`, `supabase/migrations/20261127_sj_s_schuljahr.sql`
- unverändert: `supabase/migrations/20261127_nb_s_nachbessern.sql`

**1. Rauchtests ohne feste ids**
- **Ursache:** Auf dem echten Stand sind alle `schule.*.id` `generated always` (lesend geprüft: 28 Tabellen). Meine lokalen Kopien hatten `by default` oder gar keine Identität, deshalb lief das lokal grün.
- **Betroffen:**
  - `schule.route`: nb_s 1×, sj_s 2×. Jetzt ohne id; die id wird nirgends gebraucht.
  - `schule.aufgabe`: Kopie in nb_s. Jetzt ohne id und ohne Identitäts-Spalten. Auf dem echten Stand greift das kaum, weil fast immer schon 3 Übungsaufgaben da sind.
  - `schule.karte_stand` hat keine id (Schlüssel Kind/Einheit/Etappe), war nicht betroffen.
- **Weitere Inserts in meinen Tests:** keine. Sterne, Stempel und `landung` schreiben die Funktionen selbst, ohne id.
- **Lokale Kopien:** jetzt wie echt, alle ids `generated always`. Damit fällt derselbe Fehler lokal auf.

**2. SJ-S 2 – beide Zählungen vorbereitet (nicht umgestellt)**
- Je Klasse kommen zu den bisherigen Feldern hinzu:
  - `etappen_pflicht {gesamt, gelandet, offen}` und `prozent_pflicht`: nur Pflicht-Etappen der Gruppe des Kindes (`stufe_etappen`, wie `thema_stufe.etappen`).
  - `kuer {gesamt, gelandet, offen}`: übrige Etappen der Pflicht-Flüge.
- Unverändert: `etappen` (alle Etappen, wie der Ring), `prozent`, `fluege`, `ring`, `zusatz`.
- Fertige Flüge (Wiederholung oder „kann er“) zählen in beiden Teilen mit allen Etappen, also gilt Pflicht + Kür = `etappen.gesamt`.
- **Eigenheit des Rings (nur Hinweis):** Bei offenen Flügen zählt `etappen.gelandet` nur gelandete Pflicht-Etappen. Gelandete Kür-Etappen offener Flüge stehen nur in `kuer.gelandet`.
- **Zeilenfunktion umbenannt:** jetzt `schule.schuljahr_fluege` (vorher `schuljahr_themen`). Eine neue Ergebnis-Spalte geht sonst nur mit DROP; die alte Funktion war nie auf dem echten Stand.
- **Echter Stand (lesend gerechnet, ohne ZP-S):**

| Kind | Klasse | Etappen alle (Ring) | Pflicht-Etappen | Kür |
|---|---|---|---|---|
| 1 | 5 | 29 / 112 (26 %) | 28 / 107 (26 %) | 1 / 5 |
| 1 | 6 | 0 / 82 | 0 / 78 | 0 / 4 |
| 2 | 7 | 26 / 69 (38 %) | 23 / 61 (38 %) | 3 / 8 |
| 2 | 8 | 9 / 102 (9 %) | 9 / 97 (9 %) | 0 / 5 |
| 2 | 9 | 0 / 107 | 0 / 87 | 0 / 20 |

Die Pflicht-Etappen entsprechen genau der Abfrage des Haupt-Chats von 03:10. Flüge sind unverändert (z. B. Kind 2 Kl. 7: 12 / 5 / 7).

**App:** Kein Feld fällt weg. Für „nur Pflicht“ nimmt die App `etappen_pflicht` und `prozent_pflicht` statt `etappen` und `prozent` und zeigt `kuer` getrennt, ohne neue Migration. Der Ring müsste dann mitgehen; nach Sebastians Entscheidung.

**Rauchtests** (lokal, Kopien wie echt mit ids `generated always`): 50 Läufe grün.
- Tests: `nb_s, sj_s, zp_s, tl_s, rd_s, ex_s, lz_s, nt_s, lk_s, fp_s`.
- Stände: vor ZP-S, nach ZP-S, NB → SJ, SJ → NB → SJ.
- `sj_s` hat neu Test 4: `etappen_pflicht` = Summe aus `thema_stufe` (Etappen, gelandet; fertig: alle), Pflicht + Kür = alle, offen und Prozent stimmen.

## 2026-11-23 – FERTIG: SJ-S

Stand `lernen-app` 745e0be übernommen. Nur Dateien, nichts eingespielt, kein DROP/DELETE, kein App-Code.
- neu: `supabase/migrations/20261127_sj_s_schuljahr.sql`, `supabase/tests/sj_s_rauchtest.sql`
- **Reihenfolge Einspielen:** LZ-S → ZP-S → SJ-S. SJ-S bricht ab, wenn ZP-S fehlt. Unabhängig von NB-S, beide Reihenfolgen getestet. Mehrfach einspielbar.

**Rechnung (eine Stelle: `schule.schuljahr_themen` → `schule.schuljahr_stand`), gleich dem Ring `lernLwRing`**
- **Pflicht-Flüge der Klasse:** Thema mit freigegebener Einheit. Jahrgang in der Schulart des Kindes = Klasse. Dazu eine aktive Basis-Quelle dieser Schulart (IB: alle mit MYP-Jahr; Klasse = MYP-Jahr + 5).
- **Etappen je Flug:** alle Etappen der Einheit (`etappen_anzahl` der Matrix). Nicht nur die Etappen der Regel.
- **Fertig:** Stufe „komplett“ (auch gesetzt „kann er“) oder „wiederholung“. Fertige Flüge zählen mit allen Etappen, sonst zählen die gelandeten Etappen.
- **Prozent:** gelandet ÷ gesamt, gerundet.
- **Zusatz:** Zusatz-Teile der Gruppe des Kindes zählen nicht. Übrige Themen der Klasse stehen getrennt unter `zusatz`, mit eingeplant (ZP-S).
- **Klassen:** −1, Haupt, +1 im Bereich 5–10, soweit Flüge da sind. Kind in Kl. 5 → 5, 6; Kind in Kl. 8 → 7, 8, 9.

**Felder für die App:** `schuljahr_stand` in `schule_konto` (oben) und `schule_uebersicht.lernende[]` (je Kind)
```
{ schulart, klasse, rechnung: "<Text für ⓘ>",
  klassen: [ { klasse, myp_jahr (nur IB), haupt,
               fluege:  { gesamt, fertig, offen },
               etappen: { gesamt, gelandet, offen },
               prozent,                          // null, wenn 0 Etappen
               ring:    { kann, wdh, an },       // Etappen je Ring-Farbe, Summe = gelandet
               zusatz:  { fluege: { gesamt, fertig, offen, eingeplant }, etappen: { gesamt, gelandet, offen } } } ] }
```
Kinder-Karte z. B.: „Noch {fluege.offen} Flüge und {etappen.offen} Etappen bis Klasse {klasse} geschafft“.

**Zahlen (echter Stand, lesend gerechnet, ohne ZP-S; Gymnasium)**
| Kind | Klasse | Flüge gesamt/fertig/offen | Etappen gesamt/gelandet/offen | Prozent |
|---|---|---|---|---|
| 1 | 5 (Haupt) | 15 / 2 / 13 | 112 / 29 / 83 | 26 % |
| 1 | 6 | 11 / 0 / 11 | 82 / 0 / 82 | 0 % |
| 2 | 7 | 12 / 5 / 7 | 69 / 26 / 43 | 38 % |
| 2 | 8 (Haupt) | 16 / 1 / 15 | 102 / 9 / 93 | 9 % |
| 2 | 9 | 14 / 0 / 14 | 107 / 0 / 107 | 0 % |

Zusatz Kind 2, Kl. 7: 2 Flüge (Teile 278, 279), 5 Etappen, 0 gelandet.

**Abgleich mit dem Ring und der Abfrage des Haupt-Chats**
- **Gesichert:** Die Ring-Funktion der App (`lernLwRing` aus `lernen.js`, unverändert per node ausgeführt) liefert auf den echten Matrix-Daten genau dieselben Zahlen, z. B. Kind 2 Kl. 7 mit 5/12 Themen und 26/69 Etappen (38 %).
- **Etappen:** Der Haupt-Chat hat die Etappen der Regel gezählt (`thema_stufe.etappen`: 107 bzw. 61, 28 bzw. 23 gelandet). Der Ring zählt alle Etappen der Einheit (112 bzw. 69). Gerundet ergeben beide Rechnungen zufällig dieselben Prozente (26 % bzw. 38 %), die Zahlen dahinter unterscheiden sich. `schuljahr_stand` folgt dem Ring.
- **5 oder 6 fertig (Kind 2, Kl. 7):** Auf dem heutigen Stand sind es 5: Teile 2, 28 („kann er“), 29, 102, 277. Die „6“ kann ich auf dem heutigen Stand nicht nachrechnen. Annahme: Der Ring in der Lehrplan-Ansicht rechnet mit der Arbeitskopie des Plans. Eine gerade gesetzte, noch nicht gespeicherte oder später zurückgenommene „Kann er“-Setzung zählt dort sofort mit. Der Ring im Überblick zeigt heute 5.

**Abweichung (bewusst, betrifft heute kein Kind)**
- Der Ring schließt Zusatz nur über die Quellen der Schulart aus. SJ-S zieht zusätzlich die Zusatz-Teile der Gruppe ab.
- Für Gymnasium-Kinder ist das gleich: 278 und 279 haben keine Gymnasium-Quelle.
- Für Realschule Zweig II/III (Teil 280) und IB „myp_standard“ (Teile 91, 282) würde SJ-S diese Teile als Zusatz führen, der Ring als Pflicht. Vorschlag an bau-motivation: Im Ring ebenso Zusatz der Gruppe abziehen, oder die Zahlen aus `schuljahr_stand` nehmen.

**Rauchtest `sj_s` (lokal, Kopie des echten Stands; vor und nach ZP-S grün, mit NB-S in beiden Reihenfolgen)**
1. Einspielen ändert nichts. Zahlen je Kind = Gegenrechnung nach der Ring-Regel aus `schule.lehrplan_matrix` (also `thema_stufe`). `offen` stimmt, Klassen −1/Haupt/+1. Konto und Übersicht sind gleich. Dauer je Kind höchstens 45 ms lokal; echt rund 90 ms für alle drei Kinder.
2. Kein Zusatz der Gruppe unter Pflicht; Zusatz-Zahlen = übrige Themen der Klasse.
3. Testkind: „kann er komplett“ → +1 fertig, alle Etappen gelandet. Eingeplanter Zusatz erscheint nur unter `zusatz.eingeplant`, die Pflicht-Zahlen bleiben gleich. Lokal mit dem Testkind in Kl. 8 geprüft, weil die lokalen Auszüge für seine Klasse keine Pflicht-Flüge haben; auf dem echten Stand läuft Teil 3 mit Testkind Kl. 7.
- Weiter grün: `nb_s, zp_s, tl_s, rd_s, ex_s, lz_s, nt_s, lk_s, fp_s`. `wd_s` und `lw_s` laufen lokal schon vor ZP-S nicht (fehlende Auszüge), Ergebnis vor und nach gleich.

## 2026-11-23 – FERTIG: NB-S

Stand `lernen-app` 745e0be übernommen. Nur Dateien, nichts eingespielt, kein DROP/DELETE, kein App-Code.
- neu: `supabase/migrations/20261127_nb_s_nachbessern.sql`, `supabase/tests/nb_s_rauchtest.sql`
- **Reihenfolge Einspielen:** LZ-S → ZP-S → NB-S. NB-S bricht ab, wenn ZP-S fehlt. Mehrfach einspielbar.
- Nur lesend: keine Tabelle, kein Trigger, keine Schreib-Funktion. `karte_buchen` ist unverändert, Fahrplan, Stempel und Sterne ebenso.

**Regel (wie bisher in `karte_buchen`, nur gelesen)**
- **Wieder offen:** Zwei Fehler in Folge in der Wiederholung → `sitzt = false`, `geoeffnet_am`, `folge = 0`.
- **Zurück:** drei eigene Lösungen in Folge (`least(3, karte_ziel)`). Tipp oder 2. Versuch zählt nicht, die Folge bleibt; ein Fehler setzt sie auf 0. Danach gelandet, Wiederholung ab Stufe 0, fällig in 1 Tag.
- **Liste:** wie `thema_stufe.wieder_offen` und Stadt-Stand `wieder_offen`, aber über **alle** Etappen der aktuellen Einheit. Sie gilt auch bei fertigem Ort, bei Kür-Etappen und bei „Kann er“-Setzung. Älteste zuerst.

**Felder für die App**
- `schule_konto.nachbessern[]` und `schule_uebersicht.lernende[].nachbessern[]`, je Eintrag:
  `thema_id, titel, einheit_id, block_id, stadt, lernziel, etappe_nr, etappe` (Titel der Etappe), `pflicht, wieder_offen_seit, folge, folge_noetig` (3), `noch, ort_fertig, gesetzt` (`komplett` | `wiederholen` | `etappe` | null).
- `schule_reise_karte`:
  - `naechster_start` mit `grund: 'nachbessern'` vor `dran`/`kommt` (erster Eintrag der Liste, dessen Flug auf der Karte liegt). Felder wie bisher: `thema_id, kontinent_id, land, iso, titel, grund, stadt {nr, name, lernziel, pflicht}, staedte`. Dazu `einheit_id, etappe, folge, folge_noetig`.
  - Neu `nachbessern[]` (dieselbe Liste).
  - Die Stadt steht wie bisher mit `stand: 'wieder_offen'`.
- Karten-Text z. B.: „Nachbessern: {etappe}, noch {noch} richtige in Folge“.

**Was App 0.90.1 zeigt:** unverändert. Die neuen Felder werden nicht gelesen, und `naechster_start` nutzt die App 0.90.1 nicht (nur Stadt-Stände im Reisepass). Die Lücke „Ort fertig → Etappe nicht mehr vorgelegt“ schließt erst NB-App.

**Gefunden, nicht geändert (bitte entscheiden)**
- In der Wiederholung setzt jede richtige Antwort, auch mit Tipp, den Fehler-Zähler zurück (`wdh_fehler := 0`).
- „Fehler – richtig mit Tipp – Fehler“ öffnet die Etappe also **nicht** wieder. „Richtig mit Tipp zählt nicht“ gilt heute nur für die Folge nach dem Wieder-Öffnen.
- **Stand heute (echt, lesend):** 0 wieder offene Etappen bei allen Kindern.

**Rauchtest `nb_s` (lokal, Kopie des echten Stands; vor und nach ZP-S grün)** – am Testkind, Rollback:
0. Lesend: wieder offene Etappen je Kind.
1. Einspielen ändert nichts. Liste = wieder offene Etappen. Konto, Übersicht und Reisekarte liefern dieselbe Liste.
2. Ort fertig, Etappe fällig: 1 Fehler → kein Eintrag. 2. Fehler → Eintrag mit Folge 0 von 3, `ort_fertig`, Titel und Datum. Die Stadt ist „wieder offen“, `naechster_start.grund = 'nachbessern'`.
3. Richtig mit Tipp → Folge bleibt 0. Eigene Lösung → 1, Fehler → 0. Dann 3 eigene in Folge → Eintrag weg, Wiederholung neu (Stufe 0, fällig in 1 Tag).
4. „Kann er komplett“ mit Rückfall → Eintrag `gesetzt: 'komplett'`, Stufe bleibt ◉ mit Hinweis `rueckfall`, nächster Start nachbessern. Nach 3 in Folge ist der Eintrag weg.
5. Fahrplan und Stempel unverändert, andere Kinder unverändert.
   - Sterne: nur der Landungs-Bonus der Etappe, wie bisher je Etappe einmal (`on conflict do nothing`).
   - Er fällt im Test an, weil das Testkind vorher keine Landung hatte. Bei einem echten Kind ist er schon gebucht, die Rückkehr bringt also keine Sterne.
- Weiter grün: `sj_s, zp_s, tl_s, rd_s, ex_s, lz_s, nt_s, lk_s, fp_s`.

## 2026-11-23 – FERTIG: ZP-S (Nachtrag Rückläufer ChatGPT 964)

Stand `lernen-app` 80e54f2 übernommen. Nur Dateien, nichts eingespielt, kein DROP/DELETE, kein App-Code. Ersetzt die erste ZP-S-Fassung (6601e7b) vollständig:
- `supabase/migrations/20261126_zp_s_zusatz_plan.sql` (neu geschrieben), `supabase/tests/zp_s_rauchtest.sql` (neu geschrieben)
- `supabase/tests/tl_s_rauchtest.sql`: Teil 12 lässt „im Plan“ ohne Erstabschluss zu, wenn die Eltern den Teil selbst eingeplant haben (heute echt: Kind 1 Teil 276, Kind 2 Teile 276/279/280 – wäre sonst auf dem echten Stand rot).

**Reihenfolge Einspielen:** LZ-S → ZP-S (bricht ab, wenn LZ-S fehlt). Mehrfach einspielbar.

**Zwei getrennte Eigenschaften**
1. **Pflicht/Kür je Gruppe** – unverändert (`thema.zusatz`).
2. **„Von den Eltern eingeplant“** – der Plan-Eintrag bleibt `route.art = 'normal'` mit eigenem Platz (`position`) und `geaendert_von = 'eltern:…'`. Abgeleitet: `schule.zusatz_eingeplant(kind, thema)` = Zusatz-Teil der Gruppe + Plan-Eintrag `normal`, nicht entfernt, (von Eltern geplant oder schon fertig), nicht ausgelassen.
- Warum nicht `art 'zusatz'`: App 0.90.1 nimmt Route-Einträge ohne `art`-Filter als „jetzt/nächster Flug“, und die Eltern-Planung verwirft `art <> 'normal'` – genau die Befunde aus 964.
- **route 485:** bleibt unverändert (art normal, Platz 21, eltern, offen). Karten und Sterne unverändert (Rauchtest md5). Schutzschritt: Eltern-Einträge mit `art 'zusatz'` gehen auf `normal` zurück (heute 0 Zeilen). Entdecker-Orte des Systems bleiben `zusatz`.

**Kinderseite (Server)**
- `schule_uebersicht.route`: offener eingeplanter Zusatz-Ort fehlt dort → App 0.90.1 zeigt ihn **nicht** als nächsten Pflicht-Flug. Ist er geschafft (route fertig), steht er wieder in der Liste wie jeder fertige Ort.
- `reiseoptionen` und `naechster_flug` überspringen ihn → der nächste Pflicht-Flug bleibt erreichbar, kein Kontinent wird verdeckt.
- Die Einheit bleibt anklickbar (Lernstand/Einheitenliste unverändert).
- Kein Flug-Test: `flug_ohne_test` gilt auch für eingeplanten Zusatz; `nachtest_stand` liefert `faellig false`, `grund 'zusatz'`.
- Zählt nicht für Visum, nicht für „hart“/Pflicht-Weiterflug, nicht in die Lehrplan-Quote (Matrix zählt ihn als Zusatz wie bisher).

**„Zusatz geschafft“, Stempel, 100 Sterne – bewusste Buchung**
- Neue Tabelle `schule.zusatz_geschafft` (Kind, Teil, Einheit, Block, Sterne, am; ein Eintrag je Kind und Teil).
- `schule.zusatz_geschafft_buchen(kind, thema)` – nur wenn eingeplant und **alle** Etappen gelandet: schreibt `zusatz_geschafft`, `flug_erstabschluss` (Stempel) und genau einmal 100 Sterne (`ort`, `block:<id>`, Regel `sterne_ort_geschafft`); erst danach `route.status = 'fertig'` (Kennung `geaendert_von` bleibt). Zweiter Aufruf bucht nichts.
- Aufgerufen von Triggern bei Landung (`karte_stand`) und Plan-Änderung (`route`); `ort_stand` meldet „erledigt“ nur mit Eintrag in `zusatz_geschafft`. Der Sterne-Trigger an `route.status='fertig'` bucht hier nicht doppelt (gleicher Schlüssel, Rauchtest prüft genau 100).
- Gruppen-Wechsel (Teil wird Pflicht): offene Orte werden neu bewertet, wie Pflicht weitergeführt.

**Felder für die neue App („Zusatz · eingeplant“, Fortschritt, „Zusatz geschafft“)**
- `schule_uebersicht.zusatz_plan[]`: `route_id, block_id, position, status, thema_id, einheit_id, etappen` (y, alle Etappen), `gelandet` (x), `geschafft`, `geschafft_am`, `sterne`.
- `schule_plan_lesen.plan[]`: zusätzlich `zusatz_eingeplant: true` am Eintrag.
- `thema_stufe` (über `lehrplan_matrix`, Einheitenseite): `zusatz`, `zusatz_eingeplant`, `zusatz_geschafft`; Etappen/gelandet bei eingeplantem Zusatz über **alle** Etappen.
- `schule_reise_karte`: Flug `zusatz_eingeplant`, `zusatz_geschafft`; Stadt `zaehlt: true` (Etappe zählt für den Fortschritt). `naechster_start` bleibt ein Pflicht-Flug.

**Was App 0.90.1 bis zur Umstellung zeigt**
- Kinderseite: Einheit sichtbar unter „früher/zum Auffrischen“ (Teil 279 liegt in Jahrgang 7, Kind in Kl. 8), **nicht** als nächster Flug, kein Test. Nach „Zusatz geschafft“ unter „kann“. Stempel und Sterne erscheinen wie gewohnt in Konto/Pass.
- Eltern-Planung: normaler Eintrag an seinem Platz – wählbar, abwählbar, verschiebbar. Ohne Kennzeichen „Zusatz · eingeplant“ (kommt mit ZP-App).
- Lehrplan: Zusatz gestrichelt mit Stufe wie bisher.

**Rauchtests (lokal, Kopie des echten Stands; vor und nach Einspielen grün)**
- `zp_s` 0–11: lesend vorher; Kinderdaten md5; Platz/Absicht 485-Fall; Eltern einplanen, **umsortieren, herausnehmen, wieder einplanen**; Kinderseite: nicht in Route, nicht in Reiseoptionen, **nächster Pflicht-Flug kommt**, Einheit sichtbar, Fortschritt 0/y; Landen ohne Test, Nachtest `zusatz`; nach letzter Landung genau ein Stempel, genau 100 Sterne, route fertig, kein zweites Mal; kein Visum/hart; Matrix/Reisekarte; nicht eingeplanter Zusatz bucht nichts; Gruppen-Wechsel; andere Kinder unverändert.
- Dazu grün: `tl_s, rd_s, ex_s, lz_s, nt_s, lk_s`.
- Stände: vor ZP (Kopie echt), nach ZP (zweimal eingespielt), und simulierter 485-Fall + ZP.

**Offen / Annahmen**
- Lokal mit PG 16 und Auszügen der echten Funktionen (Fixtures); echte Funktionen wurden lesend übernommen. Echt nichts eingespielt.
- Nächster Auftrag laut AUFTRAEGE: NB-S (Nachbessern).

## 2026-11-23 – FERTIG: ZP-S

Stand `lernen-app` 0ef5bdc übernommen. Nur Dateien, nichts eingespielt, kein DROP/DELETE, kein App-Code:
- neu: `supabase/migrations/20261126_zp_s_zusatz_plan.sql`, `supabase/tests/zp_s_rauchtest.sql`
- angepasst: `supabase/tests/tl_s_rauchtest.sql` (Teil 5), `supabase/tests/rd_s_rauchtest.sql`

**Reihenfolge Einspielen:** LZ-S → ZP-S. ZP-S bricht ab, wenn LZ-S fehlt.

**Vorab geprüft (lesend, echter Stand): Könnte route 485 heute fertig werden? – Nein, er bliebe für immer offen.**
- **Ort:** `ort_stand` verlangt mindestens eine Pflicht-Etappe („ohne Pflicht kein Abschluss“). Damit markieren weder `plan_setzen` noch `test_abschliessen` den Ort je als fertig.
- **Stempel:** `test_abschliessen` bucht den Erstabschluss nur mit einer Pflicht-Etappe. Kein Stempel, keine 100 Sterne.
- **Stufe:** `thema_stufe` zählt 0 Etappen, also nie „wiederholung“ oder „komplett“. Nach der ersten Landung bliebe der Teil für immer „dran“.
- **Abflugtafel:** Die Reiseoptionen nehmen je Kontinent den ersten nicht fertigen Ort. Sobald die Orte davor fertig sind, stünde der Teil dort dauerhaft als Afrika-Ziel und verdeckte die folgenden Afrika-Orte.

**Umsetzung**
- **Plan-Eintrag bleibt `art 'normal'`.**
  - Die App 0.90 führt den Plan nur über `art 'normal'` (Plan-Liste, Reihenfolge, Abflugtafel).
  - `art 'zusatz'` ist bisher den Entdecker-Orten des Systems vorbehalten und erscheint weder im Plan noch in den Reiseoptionen. Ein umgestellter Eintrag wäre aus dem Plan verschwunden.
  - „Als Zusatz geführt“ heißt daher: das Kennzeichen `zusatz_eingeplant` nach der neuen Regel.
- **route 485** braucht keine Datenänderung; der Eintrag fällt automatisch unter die Regel. `schule_plan_setzen` bleibt unverändert.
- **„Alle einplanen“** gibt es nur in der App (ohne „auch Zusatz“ nimmt sie Zusatz nicht mit). Auf dem Server gibt es keine Sammelaktion.
- **Regel `schule.zusatz_eingeplant(Kind, Thema)`:** Die Gruppe des Kindes steht in `thema.zusatz`, und es gibt einen Plan-Eintrag `art 'normal'`, der nicht entfernt ist, von den Eltern stammt oder schon fertig ist, und in dem das Thema nicht abgewählt ist.
- **Fortschritt:** `thema_stufe` zählt beim eingeplanten Zusatz über alle Etappen statt über die leere Pflichtliste. Alle Etappen gelandet → „wiederholung“, ohne Zwangstest.
- **Abschluss:**
  - `ort_stand`: erledigt, sobald alle Etappen selbst gelandet sind (sitzt, nicht gesetzt).
  - Auslöser bei der Landung: Der Ort wird „fertig“; `route_sterne` bucht die 100 Sterne (`sterne_ort_geschafft`) genau einmal.
  - Auslöser beim „fertig“: Erstabschluss, also der Stempel, genau einmal.
  - Wird der Teil erst nach dem Landen eingeplant, schließt `plan_setzen` den Ort über `ort_stand` ab.
- **Kein Flug-Test, keine Nachtests – Vorschlag „wie ohne Test“:**
  - `flug_ohne_test` gilt jetzt auch für eingeplanten Zusatz. Der Flug-Test meldet „nichts_zu_testen“, `nachtest_stand` gibt `grund` = `'zusatz'` zurück.
  - Begründung: Ohne Pflicht-Etappe gibt es keinen Nachtest-Vorrat. Ohne diese Regel könnten die Karten nie „sicher“ werden, denn `karte_sicher` verlangt sonst einen bestandenen Nachtest – kein „golden“ möglich.
  - Mit der Regel „ohne Test“ werden sie über Wiederholung (Stufe 4) und Mischkarte sicher, wie bei „Kann er – aber wiederholen“.
- **Gruppenwechsel:**
  - Wird der Teil Pflicht: Der Ort geht wieder auf „offen“, die normale Regel gilt (Flug-Test über die Pflicht-Etappen). Stempel und Sterne bleiben, nichts wird doppelt gebucht.
  - Zurück zu Zusatz: wieder fertig, wenn alle Etappen gelandet sind.
- **Nicht eingeplanter Zusatz:** unverändert freiwillig, ohne Stempel und ohne Ort-Sterne.
- **Reiseoptionen, Visum und harte Voraussetzungen:** unverändert. Die Gruppe nennt Zusatz-Teile schon heute nirgends; der Rauchtest prüft das.

**Felder für die App**
- `thema_stufe` (damit auch die Matrix `lernstand[kind][thema]` und Plan `orte[].themen[].stufe`):
  - `zusatz: true` und `zusatz_eingeplant: true`, nur in diesem Fall;
  - `etappen` = Anzahl aller Etappen; `gelandet`/`sicher` über alle Etappen; Stufe wie sonst (kommt, dran, wiederholung, komplett).
- `reise_karte`:
  - je Flug `zusatz_eingeplant`;
  - je Stadt `zaehlt: true` (nur in diesem Fall; Regel für die App: `zaehlt ?? pflicht`);
  - der Flug darf `naechster_start` sein.
- `nachtest_stand.grund` = `'zusatz'`; `einheit_lesen.ohne_test` und `schule_uebersicht` `stand[].ohne_test` sind `true`.

**Tests**
- `zp_s_rauchtest`:
  - 0: Prüfung vorab.
  - 1: Einspielen ändert keine Kinderdaten und keine Reiseoptionen; bestehende Einträge wie 485 werden als „Zusatz · eingeplant“ mit allen Etappen geführt.
  - 2: einplanen über `plan_setzen_intern`, falls vorhanden.
  - 3: landen, Fortschritt über alle Etappen, kein Flug-Test, kein Nachtest.
  - 4: Ort fertig, ein Stempel, 100 Sterne genau einmal, auch nach erneuter Landung.
  - 5: nichts dahinter gesperrt.
  - 6: Matrix und Reisekarte.
  - 7: nicht eingeplanter Zusatz ohne Stempel und Sterne.
  - 8: Gruppenwechsel hin und zurück.
  - 9: übrige Sterne unverändert.
- `tl_s` Teil 5: Ein offener `normal`-Eintrag mit Zusatz-Teil ist erlaubt, wenn er als `zusatz_eingeplant` geführt wird. Auf dem echten Stand ist er nach dem Einspielen grün; vorher bleibt er rot wie gemeldet.
- `rd_s`:
  - Migration nur, wenn sie noch fehlt (sonst würde sie im Lauf `reise_karte` ohne ZP-S überschreiben).
  - Die Zähler vergleicht der Test über `zaehlt ?? pflicht`.

**Lokal geprüft** (Nachbau nach LZ-S; Teile mit anderen IDs; ohne `plan_setzen_intern`, Einplanen dort als direkter Eintrag wie `plan_setzen` ihn anlegt)
- ZP-S läuft zweimal.
- Auf dem Stand vor und nach dem Einspielen grün: `zp_s`, `rd_s`, `ex_s`, `lz_s`, `tl_s`, `nt_s`, `lk_s`.
- Nicht lokal geprüft: der Weg über `plan_setzen_intern`. Der Rauchtest nutzt ihn auf dem echten Stand.

## 2026-11-23 – FERTIG: LZ-S

Stand `lernen-app` e07976a übernommen. Nur Dateien, nichts eingespielt, kein DROP/DELETE, kein App-Code:
- `supabase/migrations/20261126_lz_s_ladezeit.sql`
- `supabase/tests/lz_s_rauchtest.sql`

**Die drei größten Posten** (lesend auf dem echten Stand gemessen, `explain analyze`)
1. **`stufe_etappen` und `thema_stufe`:**
   - Die Pflichtliste wird je Etappe neu berechnet. Der Planer bettet den CTE ein, dadurch wird `pflicht_lernziele` je Element von `unnest` erneut aufgerufen.
   - `thema_stufe` ruft `stufe_etappen` zusätzlich je Karte im WHERE auf.
   - Die Matrix ruft `thema_stufe` je Kind und Thema doppelt auf: Die Lateral-Unterabfrage wird hochgezogen, `s.st` wird zweimal verwendet.
   - Messwerte: `stufe_etappen` 95× 409 ms (bei einmaliger Pflichtliste 53 ms); `thema_stufe` 105× 0,92 s, so wie es die Matrix aufruft 1,79 s je Kind.
2. **`thema_klassen` je Thema:** Die Sicht `thema_lage_klasse` rechnet bei jedem Aufruf alle Themen. 105× mit `thema_teil_json` 741 ms; die Sicht einmal: 10 ms.
3. **`thema_jahrgang` und „pflicht“ der Matrix:** Der Planer startet bei quelle → eintrag → zuordnung, mit 84 630 Schleifen auf 105 Themen. 105× 118–123 ms; mit den Zuordnungen des Themas zuerst 8,5 ms. Die Übersicht ruft `thema_jahrgang` 210× auf (rund 250 ms).

Weitere Messwerte vorher, echter Stand:
- `lehrplan_matrix` (zwei Kinder, Leitung): 3,76 s.
- `pflicht_lernziele` 105×: 49 ms.
- Expeditionsteil der Übersicht (drei Kinder): 164 ms.
- Lernstand Kind 2 (Hauptabfrage): 376 ms.

**Änderungen** (Ergebnisse unverändert)
- `pflicht_lernziele` und `stufe_etappen` sind jetzt plpgsql: Die Bewertung wird einmal gelesen, die Pflichtliste einmal berechnet. Reihenfolge und Rückgabe (`null` bzw. `'{}'`) bleiben wie bisher.
- `thema_stufe` per Anker: Die Etappen der Regel werden einmal je Aufruf berechnet statt je Karte. `thema_stufe` bleibt als Funktion erhalten.
- `lehrplan_matrix` per Anker:
  - „pflicht“ liest die Zuordnungen des Themas zuerst.
  - `thema_stufe` läuft je Kind und Thema genau einmal (`offset 0`).
- `thema_jahrgang`: Zuordnungen des Themas zuerst; neuer Index `zuordnung_thema_id_idx (thema_id, eintrag_id)`.
- Neu `schule.thema_klassen_alle(schulart, zweig, kurz)`: gleicher Aufbau wie `thema_klassen`, für alle Themen in einem Durchgang. `lehrplan_matrix_lk` nutzt sie statt `thema_klassen` je Thema.
- `schule_uebersicht`, `schule_lernstand`, `schule_plan_lesen` und `reise_karte` sind selbst unverändert; sie werden über die schnelleren Hilfsfunktionen schneller.

**Rauchtest `lz_s_rauchtest`**
- Ablauf: md5 der Antworten vor der Migration, Migration zweimal, md5 danach, Vergleich.
- Umfang:
  - je echtem Kind und für das Testkind in allen fünf Gruppen (Gruppenwechsel jeweils in einer Untertransaktion): Matrix (Kindsicht), Lernstand, Plan, Reisekarte, `thema_stufe` aller Themen;
  - dazu Matrix ohne Kind (ohne und mit Testkind) und Übersicht (Leitung).
- Die api-Funktionen laufen als pg_temp-Kopien ohne Schlüssel: Nur die Zugriffsprüfung ist ersetzt, und jeder Ersetzungs-Anker wird geprüft.
- Der Test gibt die Laufzeiten vorher und nachher je Funktion aus. Im Probelauf auf der echten Datenbank liefert er damit die Messwerte nachher.
- Gegenprobe: Mit absichtlich falscher Pflichtregel meldet der Test „Antwort verändert“.

**Lokal geprüft** (Nachbau mit den echten Etappen und den live gelesenen Funktionen; kleinere Kinderdaten, die Zahlen sind daher nur relativ)
- 48 Antworten vorher = nachher, vor und nach dem Einspielen.
- `rd_s`, `ex_s`, `tl_s`, `nt_s`, `lk_s` bleiben grün.
- Laufzeiten vorher → nachher:
  - Matrix ohne Kind: 803 → 168 ms
  - Matrix mit Testkind: 903 → 230 ms
  - Matrix je Kind: 167–330 → 62–87 ms
  - `thema_stufe` aller Themen: 55–91 → 19–29 ms
  - Reisekarte: 104–159 → 59–81 ms (ein Ausreißer 125 → 161 ms)
  - Plan: 120–159 → 80–101 ms
  - Übersicht: 1 576 → 112 ms beim ersten Lauf, 192 → 145 ms warm

**Nicht gemessen:** Die Werte nachher auf der echten Datenbank – dafür müsste die Migration eingespielt werden. Erwartung aus den Einzelmessungen (Annahme):
- Matrix je Kind 1,9 s → ca. 0,3 s
- Matrix ohne Kind 5,8 s → ca. 0,5 s
- `thema_stufe` aller Themen 0,9 s → ca. 0,2 s
- Reisekarte 1,7 s → ca. 0,4 s
- Übersicht und Plan je unter 0,5 s

Den Beleg liefert `lz_s_rauchtest` im Probelauf.

## 2026-11-23 – FERTIG: RD-S 2

Stand `lernen-app` fb2fcfb übernommen. Nur Dateien, nichts eingespielt, kein DROP/DELETE, kein App-Code:
- neu: `supabase/migrations/20261125_ex_f_expedition_familie.sql`
- geändert: `supabase/migrations/20261125_ex_s_expedition.sql`, `supabase/tests/rd_s_rauchtest.sql`, `supabase/tests/ex_s_rauchtest.sql`
- Inhaltsquelle angeglichen: `inhalte/expeditionen/8-schulfest.json`, `inhalte/generatoren/expedition_schulfest.py`

**Reihenfolge Einspielen:** RD-S-Migration → `rd_einspiel_2311.sql` → `20261125_ex_f_expedition_familie.sql` → `20261125_ex_s_expedition.sql`. EX-S bricht ab, wenn `ex_f` fehlt.

**1) „sicher“ (rd_s Test 3)**
- Live gilt `schule.karte_sicher`: Die Karte sitzt, `wdh_stufe` ≥ 4, und es gibt einen Nachweis.
  - Nachweis entweder: Mischkarte seit dem Landen und bestandener Nachtest mit richtiger Antwort zu dieser Etappe.
  - Oder: bei „Kann er“ bzw. Flug ohne Test keine Mischkarte seit dem Setzen, bzw. eine bestandene.
- Der Zähler `sicher` in `thema_stufe` nutzt genau diese Funktion.
- Die Karten-Funktion (`reise_etappe_stand`) nutzt sie schon. Sie ist unverändert; falsch war der Test.
  - Der alte Test setzte nur `wdh_stufe` 3 ohne Nachweis; das ist live „gelandet“.
  - Der lokale Nachbau hatte eine vereinfachte `karte_sicher`.
- Test 3 neu:
  - Erste Karte sicher über „Kann er“: `wdh_stufe` 4, `gesetzt_am`, keine Mischkarte seitdem. Vorab prüft der Test, dass `karte_sicher` greift.
  - Zweite Karte nur gelandet, danach wieder offen, begonnen, offen.
  - Golden: alle Karten so sicher.
- Test 4 neu je Kind und Flug:
  - `sicher` = Anzahl Pflicht-Städte mit Stand „sicher“ = `thema_stufe.sicher`.
  - `gelandet` = Anzahl Pflicht-Städte „gelandet“ oder „sicher“.
  - `golden` = alle Etappen der Regel sicher.
  - Damit nutzen Stand je Stadt und die Zähler je Flug dieselbe Regel.
- Gegenprobe lokal mit der Live-Fassung von `karte_sicher`: Der alte Test schlägt mit genau der Meldung aus dem Probelauf fehl, der neue ist grün.

**2) Expedition „8-schulfest“ und Familie des Themas (`ex_f`)**
- Neu: `schule.thema_familie(thema)` (Stamm über `teil_stamm`) und `schule.lernziel_thema(thema, lernziel)` (das Thema der Familie, dessen aktuelle Einheit die Etappe hat; das genannte Thema zuerst).
- `expedition_voraussetzungen_ok` und `expedition_etappe` suchen die Karte in der Familie des genannten Themas. Eine künftige Teilung bricht Expeditionen damit nicht mehr.
- Der Auslöser aus EX-S (`expedition_angebot_pruefen`: Auswahl der Expedition und „seit“ = späteste Landung) nutzt dieselbe Familien-Regel.
- Datenkorrektur ohne feste IDs:
  - Voraussetzungen, deren Lernziel nicht im genannten Thema liegt, zeigen auf den Teil, der es enthält; `thema_schluessel` wird mitgeführt.
  - Ebenso Thema und Einheit der Expeditions-Teile (Aufgaben).
  - Live betrifft das „8-schulfest“: laplace und grosse_zahlen, je Voraussetzung und Teil, gehen nach „Zufall und Laplace – Teil 2 von 2“.
  - Live gibt es keine Karten und keine Antworten dazu; kein Kind ist betroffen.
- Inhaltsquelle: Die JSON und der Generator nennen jetzt `stochastik.grundbegriffe_teil2`. Sonst würde ein neuer Import die alte Zuordnung zurückholen.
- `ex_s_rauchtest` Test 8:
  - Jede Voraussetzung und jeder Teil jeder Expedition findet seine Etappe im genannten Thema; der Themen-Schlüssel passt zur ID.
  - Eine Voraussetzung, die den Stamm nennt, deren Etappe aber in einem späteren Teil liegt, gilt als erfüllt. Der Auslöser legt das Angebot an, und `expedition_etappe` findet die Karte im Teil.

**Lokal geprüft**
- `ex_f` und EX-S liefen je zweimal (zweiter Lauf: 0 Änderungen).
- Auf dem Stand vor und nach dem Einspielen grün:
  - `ex_s_rauchtest` (Tests 0–8)
  - `rd_s_rauchtest`, zusätzlich mit der Live-Fassung von `karte_sicher`
  - `tl_s`, `nt_s`, `lk_s`

## 2026-11-23 – FERTIG: EX-S

Gehört zu RD-S. Stand `lernen-app` 759fa30 übernommen. Nur Dateien, nichts eingespielt, kein DROP/DELETE, kein App-Code:
- `supabase/migrations/20261125_ex_s_expedition.sql`
- `supabase/tests/ex_s_rauchtest.sql` (spielt die Migration selbst ein, Rollback)
- `supabase/functions/lernen-api/index.ts` 0.9.3: zusätzlich `schule_expedition_spaeter`

**1) Sterne**
- `sterne_expedition_geschafft` steigt von 50 auf **150**.
- Neu: `sterne_expedition_fehlerfrei` = **200**. Fehlerfrei heißt: Bei jedem Teil war der erste Versuch außerhalb von Tests richtig, ohne Tipp und im ersten Anlauf.
- `expedition_buchen` bucht 200 oder 150, genau einmal je Kind und Expedition (eindeutiger Schlüssel Kind + Grund + Bezug).
- Beide Werte stehen auch in `sterne_regeln`.
- Live gibt es noch keine Expeditions-Sterne und keine Antworten auf Expeditionen, also ist keine Nachbuchung nötig. Rauchtest 0 prüft das und bricht sonst ab.
- Beim Einspielen setzt die Migration beide Werte auf 150 und 200, auch wenn sie vorher anders standen.

**2) Angebot und „Später“**
- Neue Tabelle `schule.expedition_angebot` (Kind, Expedition, `angeboten_am`, `spaeter_am`, `spaeter_bis`).
- Das Angebot entsteht, sobald die letzte Voraussetzung sitzt: Auslöser auf `karte_stand.sitzt`.
  - `angeboten_am` = Zeit der spätesten Landung unter den Voraussetzungen.
  - Bestehende Stände trägt die Migration nach; auf dem echten Stand ist eine solche Nachtragung noch nicht gelaufen.
- „Später“ setzt `spaeter_bis` auf das heutige Ortsdatum des Kindes (Zeitzone wie bei `lerntag`).
  - Ausgeblendet ist die Expedition, solange `spaeter_bis` ≥ heute ist; ab dem nächsten Lerntag ist sie wieder vorn.
- Es wird nichts gesperrt und nichts am Lernstand geändert.

**Schnittstelle**
- `expeditionen_kind` je Expedition: wie bisher, dazu:
  - `angeboten_am`, `spaeter_am`, `spaeter_bis`, `ausgeblendet`
  - `sterne` (gebuchte Menge), `fehlerfrei`
  - `sterne_geschafft` (150), `sterne_fehlerfrei` (200)
- Reihenfolge der Liste: begonnen → angeboten (vorn) → angeboten (später) → geschafft.
- `expeditionen_stand` (neu in `schule_konto` und je Kind in `schule_uebersicht`):
  - `stationen_gesamt`, `stationen_geschafft` (für „3 von 21 Stationen“)
  - `angeboten` (Anzahl angeboten + begonnen), `vorn` (davon nicht ausgeblendet)
  - `oben_id` = die Expedition für die oberste Karte der Abflugtafel: begonnen vor angeboten, dann nach `angeboten_am`
  - `heute`, `angebote[]`
- Neue Aktion `api.schule_expedition_spaeter {lernender_id, expedition_id}` mit Zugriffsprüfung wie `schule_konto`.
  - Antwort: `{ok, lernender_id, expedition_id, spaeter_bis, expeditionen_stand}`.
  - Fehler „Expedition ist nicht angeboten“, wenn es kein Angebot gibt.
- „Jetzt starten“ braucht keine eigene Aktion: Die Antworten laufen wie bisher über `schule_uebung_pruefen`.
- `schule_konto`, `schule_uebersicht` und `sterne_regeln` sind über eindeutige Anker erweitert. Die Anker habe ich auf dem echten Stand gelesen: je genau einmal vorhanden.

**Lokal geprüft**
- Nachbau: Stand nach RD-S, dazu die Expeditions-Funktionen so, wie sie live gelesen wurden.
- Migration zweimal, Rauchtest grün, sowohl ohne als auch mit vorher eingespieltem EX-S:
  - 0: keine Nachbuchung nötig.
  - 1: Regelwerte 150 / 200.
  - 2: Einspielen ändert Lernstand, Sterne, Route und Reiseoptionen nicht.
  - 3: Kein Angebot, solange eine Voraussetzung fehlt; nach der letzten Landung ein Angebot mit „seit“ = diese Landung.
  - 4: Das Angebot sperrt nichts (Reiseoptionen, Stufen, Lernziel-Stände).
  - 5: „Später“ blendet bis zum nächsten Lerntag aus; Zugriff wird geprüft.
  - 6: Mit Tipp 150, fehlerfrei 200, erst falsch und dann richtig 150 – je genau einmal, auch bei erneuter Antwort. Übrige Sterne, Lernstand anderer Kinder und Reiseoptionen unverändert.
  - 7: Ausgabe in `schule_konto` und `schule_uebersicht`.
- `rd_s`, `tl_s` und `nt_s` bleiben grün.
- Die Erweiterung von `schule_uebersicht` ließ sich lokal nicht ausführen (die Funktion fehlt im Nachbau); live ist nur der Anker geprüft.

## 2026-11-23 – FERTIG: RD-S

Stand `lernen-app` 6da3aec übernommen. Grundlage `inhalte/reise/aufbau-vorschlag.json` (Reise-Aufbau 4), Datenbank nur gelesen. Nur Dateien, nichts eingespielt, kein DROP/DELETE, kein App-Code:
- `supabase/migrations/20261125_rd_s_reise.sql` – Tabellen, Regeln, Lesefunktion, Aktion.
- `inhalte/reise/rd_bauen.py` → `inhalte/reise/rd_einspiel_2311.sql` (Daten; Aufruf `python3 -I inhalte/reise/rd_bauen.py`, prüft die JSON vorab, Exit 1 bei Fehler).
- `supabase/tests/rd_s_rauchtest.sql` – spielt Migration und Daten selbst ein (beide wiederholbar), alles mit Rollback.
- `supabase/functions/lernen-api/index.ts` 0.9.3: Aktion `schule_reise_karte` (nur Datei, nicht ausgerollt).

**Reihenfolge Einspielen:** Migration → `rd_einspiel_2311.sql` (ein DO-Block: ganz oder gar nicht) → Rauchtest. Edge Function 0.9.3 erst mit RK-App.

**Tabellen (alle neu, RLS an, nur über security-definer-Funktionen)**
- `reise_kontinent`: Kontinent ↔ Reise-Name. `kontinent.erdteil` bleibt unverändert (Kontinent 4 zeigt bis RK-App weiter „Antarktis“, die Reise heißt „Orient …“).
- `reise_land`: Flug-Länder und Reserve-Länder in einer Tabelle.
  - Felder: `thema_id` (eindeutig), `flug_schluessel` („29-2“), Name, ISO, Region, Mittelpunkt, Hauptstadt (deutscher Name + Lage + GeoNames-ID), `hauptort` (nur Landesteile), `kurzflug`, `insel_ausnahme`, `nachbarteil`, `nachbarschaft`, Reihenfolge.
- `reise_stadt`: Etappen- und Reserve-Städte.
  - Felder: Thema + Lernziel, Einheit beim Einspielen, Name, Breite, Länge, GeoNames-ID, Reihenfolge, `kuer_vorschlag`.
  - `kuer_vorschlag` ist nur zum Abgleich da; maßgeblich ist die Pflichtliste der Einheit.
- `reise_station` + `reise_station_expedition`: je Expedition eine Station.
- `reise_quelle`: Quellenangaben.

**Regeln**
- Jedes Land genau einmal: eindeutig nach ISO + Region und nach Name, über Flug- und Reserve-Länder zusammen.
- Jede Stadt genau einmal: eindeutige GeoNames-ID.
- Je Etappe höchstens eine Stadt: eindeutig nach Thema + Lernziel.
- Jede Stadt liegt im Land ihres Flugs (Fremdschlüssel Land + Thema).
- „Mindestens eine Stadt je Etappe“ prüfen die Sicht `reise_abweichung` und das Einspielen. Es bricht ab bei: Etappe ohne Stadt, Stadt ohne Etappe, freigegebenes Thema ohne Land, Land ohne Freigabe.
- Die Themen der Teile löst das Einspielen über `teil_stamm` + `teil_nr` auf. Lokal hatten die Teile andere IDs (1000–1007), live sind es 276–283; beide liefen durch.

**Schnittstelle** `api.schule_reise_karte(schluessel, {lernender_id})`
- Zugriffsprüfung wie `schule_konto` (`schule.zugriff`, Kind aktiv).
- Antwort: `{ok, lernender_id, gruppe, kontinente[], naechster_start, antarktis, quellen[]}`.
- `kontinente[]`:
  - Felder je Kontinent: `id`, `schluessel`, `themengebiet`, `reise`, `zusatz`, `laender`, `geschafft`, `zusatz_laender`, `fluege[]`.
  - `laender` und `geschafft` zählen ohne Zusatz.
- `fluege[]`, je Flug:
  - Thema und Teil: `thema_id`, `flug`, `titel`, `untertitel`, `teil`, `teil_von`, `teil_stamm`.
  - Land: `land`, `iso`, `region`, `mitte{breite, laenge}`, `hauptstadt{name, breite, laenge}`, `hauptort`, `kurzflug`, `insel_ausnahme`, `nachbarteil`.
  - Stand des Kindes: `stufe`, `zeichen`, `gesetzt` (aus `thema_stufe`), `stempel` und `stempel_am` (= `flug_erstabschluss`), `golden` (alle Etappen der Regel sicher), `im_plan`, `plan_platz`, `zusatz`, `etappen`, `gelandet`, `sicher`.
  - `staedte[]`: `nr`, `name`, `breite`, `laenge`, `lernziel`, `titel`, `pflicht`, `stand`.
- `stand` einer Stadt: `offen` · `begonnen` · `gelandet` · `sicher` · `wieder_offen` (gleiche Zählung wie `thema_stufe`).
- `pflicht` richtet sich nach der Gruppe des Kindes (`pflicht_lernziele`, gleiche Etappen wie `stufe_etappen`).
- `naechster_start`:
  - Auswahl: zuerst ein Flug „dran“, sonst der nächste „kommt“ im Plan, ohne Zusatz.
  - Inhalt: `thema_id`, `kontinent_id`, `land`, `iso`, `titel`, `grund`, `staedte` (Anzahl) und `stadt{nr, name, lernziel, pflicht}`; die Stadt ist die erste offene, Pflicht vor Kür.
  - Der Startknopf führt wie heute; das Feld dient nur zum Anzeigen und Hinzoomen.
- `antarktis.stationen[]`: `name`, `betreiber`, `breite`, `laenge`, `expeditionen[]`.
- `quellen[]`: GeoNames (CC BY 4.0), Natural Earth (gemeinfrei), COMNAP.

**Abweichungen JSON ↔ Datenbank** (JSON gegen den echten Stand gelesen; die Datenbank hat 95 freigegebene Einheiten)
- Etappen ohne Stadt: **0**. Städte ohne Etappe: **0**. Reihenfolge anders: **0**. Themen ohne Flug: **0**.
- `noch_nicht_in_db`: alle 12 so markierten Etappen sind inzwischen in der Datenbank (Teilung und LK-D 4 eingespielt). Das Kennzeichen in der JSON ist veraltet und wird nicht übernommen.
- Kür:
  - Die 22 Etappen, die die JSON als Kür markiert (`kuer_in` bzw. `kuer`), stimmen in jeder Gruppe mit der Pflichtliste der Datenbank überein.
  - Weitere 39 Etappen alter Themen sind laut Pflichtliste der Datenbank in allen Gruppen Kür, in der JSON aber nicht markiert, z. B. 15 `dualsystem`, 63 `venn`. Die Karte nimmt die Datenbank.
  - Diese Fälle zeigt die Sicht `reise_kuer_abweichung`; der Zähler in der Einspiel-Meldung zählt dabei je Gruppe.
- Die Zeile `stand` in der JSON lautet noch „Reise-Aufbau 2“, der Inhalt ist aber Reise-Aufbau 4 (95 Flüge, 618 Städte).
- Umfang: 8 Kontinente, 95 Flug-Länder, 618 Etappen-Städte, 28 Reserve-Länder, 209 Reserve-Städte, 21 Stationen.

**Größe der Karten-Antwort je Kind:** etwa 150 KB als JSON ohne Leerzeichen, etwa 26 KB gepackt (gzip). Lokal gemessen mit kurzen Etappen-Titeln; live kommen die echten Titel dazu, also etwas mehr.

**Lokal geprüft** – im Nachbau mit den echten Etappen aller 95 Einheiten (Live, nur gelesen), dem Stand nach TL-S 7 / NT-S 2 und Teilen mit anderen IDs:
- Migration lief zweimal, Einspielen ebenfalls zweimal; die Daten sind danach gleich.
- `rd_s_rauchtest` grün, sowohl auf dem Stand ohne RD als auch mit schon eingespieltem RD:
  - Test 0: wiederholbar.
  - Test 1: je Etappe genau eine Stadt.
  - Test 2: nichts doppelt, Regeln greifen.
  - Test 3: Karte in allen fünf Gruppen; alle fünf Stände je Etappe; golden.
  - Test 4: Stufe, Stempel, Pflicht und Zusatz je Kind wie `thema_stufe`, Erstabschluss und `stufe_etappen`.
  - Test 5: Zugriff wird geprüft.
  - Test 6: Lernstand, Sterne, Stempel, Route, Ortsnamen und Reiseoptionen unverändert.
- `tl_s`, `nt_s` und `lk_s` bleiben grün.

**Offen für Sebastian / Haupt-Chat**
- COMNAP-Daten (Stationen) laut JSON „frei für Bildung, nicht kommerziell“ – vor RK-App klären, wie in Bau-Auftrag RK vorgesehen.
- Die bisherigen Ortsnamen (`block.stadt/land`) bleiben, bis die RK-App live ist; danach eigener Auftrag.

## 2026-11-22 – FERTIG: TL-S 7 / NT-S 2

Stand `lernen-app` 00cd00e übernommen (Rückläufer Prüfung 951). Nur Dateien: `supabase/migrations/20261123_tl_s_teilung.sql`, `supabase/migrations/20261124_nt_s_nachtest_menge.sql`, `supabase/tests/tl_s_rauchtest.sql`, `supabase/tests/nt_s_rauchtest.sql`, `supabase/tests/lk_s_rauchtest.sql`. Nicht eingespielt, kein DROP/DELETE, kein App-Code.

**Muss**
- **A1 (TL-S):** Vor der Buchung eines Erstabschlusses prüft `tl_teilen` jetzt je Pflicht-Etappe des neuen Teils die Testabdeckung: `schule.tl_testabdeckung(Kind, alte Einheit, Etappe)` = im alten **abgeschlossenen** Flug-Test oder Korrektur-Test der alten Einheit eine Aufgabe dieser Etappe **richtig** beantwortet. Ohne Abdeckung: kein Erstabschluss, kein Stempel, keine 100 Sterne, Teil bleibt „nicht im Plan“ und steht in der Liste je Kind. Echter Stand (lesend): Kind 2 hat im alten Flug-Test von 29 je Etappe eine richtige Antwort → 29 Teil 2 bleibt geschafft.
  Negativtests (Rauchtest 18, Testkind, vor der Teilung angelegt): a) 26 – alle Karten selbst gelandet, Lernziele „nachgewiesen“, kein alter Flug-Test; b) 61 – Flug-Test abgeschlossen, aber nur mit Aufgabe zu `laplace` → je null neue Abschlüsse, null Ort-Sterne, nicht im Plan. Mit der Fassung von TL-S 6 schlägt der Rauchtest fehl (Gegenprobe).
- **D1 (NT-S 2):** `nachtest_auswahl` liefert genau die Menge oder nichts; `test_starten_intern` verlangt je Pflicht-Etappe genau `nachtest_je_etappe` Aufgaben, sonst kein Teststart (`grund` = `vorrat_erschoepft`, Liste der Etappen, `nachtest.aufgaben_je_etappe`). Rauchtest 6: 1 Pflicht-Etappe mit 1, 2, 3, 4 verfügbaren Aufgaben (bei 3 und 4 eine schon gestellt) → kein Start, keine Sitzung; echter Start mit 4 Pflicht-Etappen → 8 Aufgaben, je 2.

**Sollte**
- **A2:** `stufe_etappen` – ausdrücklich leere Pflichtliste → keine Etappen (Kür zählt nicht); ohne Liste wie bisher alle.
- **D2:** Nachtest-Menge zählt die Pflicht-Etappen des Kindes (`lernziel_stand.pflicht`, gesetzt nach `pflicht_lernziele` der Gruppe); `schule.nachtest_vorrat` jetzt je Gruppe (gym_by, rs_I, rs_II_III, myp_standard, myp_extended) – RS II/III ausgewiesen.
- **lk_s Teil 4:** statt md5 über das Stufen-JSON: Karten, Versuche, Sterne unverändert, bestehende Lernziel-Stände unverändert (neue offene Zeilen erlaubt), Etappenzahl der Stufe = Pflichtliste der Gruppe (`stufe_etappen`; vor TL-S alle Etappen). Lokal vor und nach der Teilung durchgelaufen.
- **Liste je Kind:** `schule.tl_teile_je_kind` mit neuer Spalte `visum_aus_altem_thema` (fertig | gesetzt) – bewusste, dauerhafte Ausnahme, Sebastian bestätigt einmal.

**Gesehen/getestet (lokal, Nachbau mit echten Indizes, echtem Graph, echtem `lk_einspiel` vor TL-S, Live-Funktionen):** TL-S zweimal ohne Fehler; `tl_s_rauchtest` vor und nach der Teilung grün; NT-S zweimal ohne Fehler, `nt_s_rauchtest` vor und nach der Teilung grün; `lk_s_rauchtest` vor und nach der Teilung durchgelaufen. Auf der echten Datenbank nicht ausgeführt.

## 2026-11-20 – FERTIG: LB, Teil 5 – App 0.82.2 (Cache v148)

Stand `lernen-app` 5e3a975 übernommen. Grundlage `inhalte/pruefung/lehrer/nachpruefung-3.md`. Datenbank nicht berührt, keine Migration. Kein Merge.
Bilder: `docs/previews/la/lb5-klasse-gym8-400.png`, `lb5-klasse-gym8-820.png`, `lb5-klasse-gym8-1280.png`, `lb5-auswahl-820.png`, `lb5-lehrplan-1280.png`.

**Gemessen mit echten Daten:** Die neuen Tests laden den Lehrstoff aus `inhalte/themenliste.json` (95 Flüge: Titel, Lernbereiche, Lehrplan-Bezüge, Reihenfolgen, Etappen-Titel aus den Themendateien); der Lernstand eines Gym-8-Kindes ist erfunden (alle fünf Stufen, auch „gesetzt: wiederholen“).

**Muss**
- **M1:** „Nach Klasse“ – für **jede** Klasse aller drei Schularten (Gym 5–10, RS 5–10, MYP 1–5) bei 400, 820 und 1280 px gemessen: kein Wort über zwei Zeilen (Titel, Unterzeile, Stufenwort, Lernbereich), keine Überlappung Titel ↔ Stufenwort, kein Titel läuft über, kein Querrollen. Umsetzung: unter 1100 px steht das Stufenwort mit Zusatz **unter** dem Titel; Tablet 700–1099 px Spalten 55 % / 45 %; ab 1100 px Stufenwort höchstens 42 % breit und umbrechend; Unterzeilen ohne Silbentrennung; Wörter mit Bindestrich („n-te“) werden nicht am Bindestrich umbrochen. Die längsten Titel je Klasse schreibt der Test nach `test-results/lb5-laengste-titel.json`.

**Sollte**
- **S1 Auswahl kompakt:** Orte bleiben zugeklappt; je Ort ein Häkchen (alle geplanten Flüge) statt Griff, daneben „▸ einzeln“; je Abschnitt (▶, ○, ↻, ◉) ein Häkchen „alle auswählen“; Flug-Knöpfe, „alle Flüge: kann er komplett“ und „Ort aus dem Plan nehmen“ sind beim Auswählen ausgeblendet. Gemessen (820, echte Daten): Seite wächst nicht mehr um das 8-Fache (Test: < 1,6-fach).
- **S2:** Abschnitte „▶ GERADE DRAN · 1 Ort, 2 Flüge“, „◉ Kann er komplett · 11 Orte, 11 Flüge“ usw.; Kopf weiter in Flügen.
- **S3:** Lehrplan-Übersicht je Klasse in Lehrplan-Reihenfolge der gewählten Schulart, Gruppen nach Lernbereich (ohne Lernbereich-Daten wie bisher nach Gebiet). Getestet Gym 8 und RS 7 gegen die Reihenfolge der Themenliste.
- **S4:** Aufgeklappt stehen die Etappen als Liste „1 Ungleichungen umformen · offen“ (Stand: offen · begonnen · gelandet · sicher · wieder offen), kein Tooltip nötig.

**Kann**
- K1 Legende: eine Zeile mit den fünf Zeichen und „Legende“, aufklappbar (Wörter und Klassenfarben darin).
- K2 Lehrplan-Spalte ohne eigene Bildlaufleiste (nicht mehr klebend) – die Seite rollt, beide Ansichten.
- K3 IB-Lernbereiche deutsch zuerst („MYP 3 Zahl und Algebra (Numerical and abstract reasoning)“), nur Anzeige.
- K4 Fehlt der Lehrplan-Bezug der Schulart, zeigt „Lehrplan:“ den Lernbereich. Lehrplan-Bezüge als Liste werden mit „ · “ verbunden.

**Gesehen/getestet**
- lernen: 112 von 112 (neu 4 Tests LB Teil 5: M1 alle Klassen × 400/820/1280; S4/K3/K4; S1/S2/K1/K2; S3). Angepasst: Abschnitts-Texte („· 1 Ort, 2 Flüge“), Legende vor dem Messen der Farben aufklappen, Touch-Ziehen erst nach oben rollen (Spalte klebt nicht mehr).
- Suche: 139 bestanden, 9 Fehler – die bekannten alten (13, 15, 101, 103, 105, 111, 113, 126, 127).

**Nicht geprüft / Hinweise**
- Mit echten Kinderdaten und echten Geräten nicht angesehen; nur Chromium.
- Ob der Live-Server `lernbereich`/`lehrplan`/`lehrplan_reihenfolge` in `schule_lehrplan_uebersicht` liefert, habe ich nicht geprüft; ohne diese Felder gliedert die Übersicht wie bisher nach Gebiet.
- Der Lehrplan rechts klebt nicht mehr beim Rollen (Folge von K2). Ziehen aus dem Lehrplan in den Plan funktioniert weiter (E-2-Test), bei langen Listen muss man aber rollen.

## 2026-11-20 – FERTIG: Teil 4, Punkt 5 d–h – App 0.82.1

Stand `lernen-app` e728367 übernommen (Punkt 5 a–h unverändert gegenüber 10a3155). a)–c) waren in 0.82.0; d)–h) jetzt als **0.82.1** (Version in app.js, sw.js, index.html, lernen/index.html, lernen/schule.js, tests/search.test.cjs). Datenbank nicht berührt (keine Migration nötig: `schule_test_starten` mit `art: korrektur` und `schule_einheit_lesen` gibt es schon). Kein Merge.
Bilder: `docs/previews/la/teil4-test-folgt-390.png`, `teil4-ergebnis-entdecker-390.png`, `teil4-ergebnis-nacht-390.png`.

**Umgesetzt**
- **d) Knobel hinten dran:** Nach der Landung kommt sofort die Knobel-Bordkarte der Etappe (eine noch nicht versuchte; sonst entfällt der Schritt), darüber „Gelandet: … ✓ Zum Schluss eine harte Nuss – falsch kostet nichts.“. Kein Angebot zur Auswahl mehr. Vor dem Prüfen klein „Heute keine Knobel-Bordkarte“, nach dem Prüfen groß „Weiter ›“ → Landebildschirm. Regeln der Knobel-Bordkarte unverändert.
- **e) Test folgt:** Ist mit der Landung jede Pflicht-Etappe gelandet, hat der Landebildschirm nur einen großen Knopf „Jetzt zum Test ›“ („n Bordkarten, ohne Tipps. Bestehst du ihn, ist der Flug geschafft.“; Nachtrag: „Test zu den neuen Etappen ›“), dazu was für den Stempel des Ortes noch fehlt (aus `schule_konto.orte`), klein „Pause – zur Abflugtafel“. Öffnen des Flugs (ohne Ziel oder „üben“ ohne Etappe) zeigt dann die Testseite mit „Alle Etappen sind gelandet ✓“ statt der Übungen; „‹ Zu den Etappen“ führt auf `…-erklaeren` (sonst Kreis). Die Abflugtafel führte schon direkt zum Test (`testDran`). Gesetzte Flüge ohne Test (`ohne_test`) ausgenommen. Die gelandete Etappe aus b) zeigt in diesem Fall „Jetzt zum Test ›“.
- **f) Test-Ergebnis:** Summe groß („**1 von 2** richtig“), jede Antwort mit kräftiger Fläche, 10-px-Balken, großem ✓/✗ im Kreis und dem Wort RICHTIG/FALSCH, hell und nacht. Kontrast im Test gemessen (Text ≥ 4,5 : 1, Zeichen ≥ 3 : 1).
- **g) Verbessern:** „Verbessern ›“ zeigte auf die eigene Adresse. Jetzt nach einem Ergebnis mit Fehlern genau zwei Wege: groß „Erst üben: <Etappe> ›“ und „Gleich verbessern ›“ (Knopf, startet `schule_test_starten` mit `art: korrektur` direkt), darunter klein „Zum Flug“ · „Zur Abflugtafel“. Geprüft: Kein Link der Ergebnisseite zeigt auf die eigene Adresse.
- **h) Alter Stand:** Nach jedem abgeschlossenen Test (alle Arten) lädt die App `schule_einheit_lesen` neu, bevor sie Knöpfe zeichnet; Fehler-Etappen und „Flug geschafft“ kommen aus dem frischen Stand (Fallback: Antwort des Tests). Geschafft → „Flug geschafft! 🎉“ und „Weiter zum nächsten Flug ›“, kein „Verbessern“.

**Gesehen/getestet** (mit 0.82.1: lernen 108 von 108; Suche 138 + 1 bestanden – Nr. 108 war wie bekannt wackelig und besteht einzeln –, 9 bekannte alte Fehler 13, 15, 101, 103, 105, 111, 113, 126, 127)
- d: Knobel kommt von selbst, falsch → „Weiter ›“ → Landebildschirm, kein zweiter Versuch; „Heute keine Knobel-Bordkarte“ → Landebildschirm.
- e: nach der letzten Pflicht-Etappe nur „Jetzt zum Test ›“, führt auf die Testseite; Flug öffnen mit fehlendem Test → Aufforderung, keine Bordkarte.
- f: hell und nacht, Wörter, Zeichen, Balkenbreite, Kontrast.
- g: hell und nacht, „Gleich verbessern ›“ → Korrektur läuft (`art: korrektur`).
- h: Korrektur vollständig richtig, Testantwort mit altem Stand → „Flug geschafft“, kein „Verbessern“, Stand neu geladen.

**Nicht geprüft / Hinweise**
- d und e nur in der Abflug-Gestaltung (alle Kinder außer „alt“); in der alten Gestaltung bleibt das Knobel-Angebot nach „Etappe sitzt“.
- „Was für den Stempel noch fehlt“ rechnet mit `schule_konto.orte` (themen, erledigt) – mit echten Daten nicht angesehen.

## 2026-11-20 – FERTIG: LB-1/LB-2/LB-5 – App 0.82.0

Zweig `bau-lehrer`, Stand `lernen-app` (c750ad2) übernommen. Kein Merge. Vorgabe: `inhalte/pruefung/lehrer/umsetzung-lb.md`, Entwurf `lehrplan-klasse-4-stufen.html`; Server-Felder LB-3 laut `bau-motivation.md`.
Bilder: `docs/previews/la/lb-plan-400.png`, `lb-plan-820.png`, `lb-plan-1280.png`, `lb5-auswahl-1280.png`, `la7-lehrplan-820.png`, `la4-plan-820.png`.

**Umgesetzt**
- **LB-2 – 4 Stufen überall gleich** (◉ Kann er komplett · ↻ In Wiederholung „Wdh x von 5 · nächste in n Lerntagen“ · ▶ Gerade dran · ○ Kommt noch · + Nicht im Plan; gleiche Zeichen, Farben, Wörter): Plan links (je Ort und je Flug aufgeklappt), „Nach Themengebiet“ (Stufe statt „✓ im Plan“), „Nach Klasse“, Lehrplan-Übersicht (Stufe je Kind, Ort-Spalte entfernt, „Gebiet · andere Schularten“ unter dem Titel), Überblick „Zuletzt geschafft“ mit ◉/↻. Quelle: `stufe` vom Server; ohne Server-Stufe aus dem Stand geschätzt.
- **LB-1 „Nach Klasse“:** eine Zeile je Flug, Filter streng (genau diese Klasse der gewählten Schulart), Reihenfolge Lehrplan (`lehrplan_reihenfolge`, sonst Themenliste), RS/IB „Reihenfolge vorläufig wie Gymnasium.“, „Nur Realschule“/„Nur IB MYP“ am Ende, Lernbereich-Zwischenüberschriften (sobald `lernbereich` da ist), Eingeplante bleiben an ihrem Platz. Aufklappen: Lehrplan-Bezug, Kurzbeschreibung, Etappen mit Stand, „Inhalte ansehen“, 4 Knöpfe. „+ In den Plan“ nimmt den Ort nur mit diesem Flug auf (andere ausgelassen). Oben nur „Gym 8: X von Y Themen im Plan oder schon gekonnt“ mit Balken.
- **LB-5 Plan = Cockpit:** Kopf „Gymnasium Kl. 8 · n ▶ · n ○ · n ↻ · n ◉ · Gespeichert · Auswählen · ↶ Rückgängig“ (gezählt je Flug). Links „Unser Lehrplan“ nach Stufe: ▶ und ○ ziehbar/↑↓, ↻ mit Wdh-Angabe, ◉ zugeklappt mit Datum (ersetzt „Geschafft“). Knöpfe an jedem Flug, bei ◉ zusätzlich „Wieder in die Wiederholung“. Auswahlmodus (Häkchen je Flug/Ort, links und rechts) mit Sammelleiste: Lernen · Kann er – aber wiederholen · Kann er komplett · Aus dem Plan nehmen · Wieder in die Wiederholung. Speichert sofort; Rückgängig schickt `rueckgaengig: <schritt_id>`. Nach jedem Speichern werden die Stufen neu gelesen.
- „Kann er – aber wiederholen“ und „Wieder in die Wiederholung“ nur, wenn `kann_wdh` kommt. Ohne LB-4-Felder läuft alles (getestet mit Testdaten ohne `lernbereich`/`lehrplan`).
- **Migration als Datei (nicht ausgeführt):** `supabase/migrations/20261120_lb_lehrplan_felder.sql` – Spalten `schule.thema.lernbereich`/`lehrplan` (jsonb) und Ausgabe von `beschreibung`, `lernbereich`, `lehrplan`, `etappen` (Lernziel/Titel) in `schule_plan_lesen` sowie `lernbereich`, `lehrplan`, `lehrplan_reihenfolge` in `schule_lehrplan_uebersicht`. Anker in den Live-Funktionen nur lesend geprüft. Rauchtest `supabase/tests/lb_lehrplan_felder_rauchtest.sql` (Rollback, nur Testdaten). Die Inhalte der Felder (LB-4) füllt der Haupt-Chat.
- Info-Seite: Plan-Absatz neu (Stufen, Knöpfe, Auswählen), Lehrplan-Übersicht „Stufe je Kind“.

**Gesehen/getestet**
- lernen: 102 von 102. Neu: 6 Gym-7-Flüge per Auswahl mit **einem** `schule_plan_setzen` auf `kann_wdh_themen`; ◉-Flug „Wieder in die Wiederholung“ (`wieder_wdh_themen`) und Rückgängig mit `rueckgaengig: 901`; alle Knöpfe links und rechts erreichbar; 400/820/1280 ohne Querrollen und ohne gebrochene Wörter (Wortbereich über zwei Zeilen gemessen).
- Angepasst: Plan-, LA-4/5/7/8-, I-7/I-8-, E-2-Tests auf Stufen und neue Klasse-Ansicht; Reisewörter-Test lässt den Vorgabe-Satz „Themen im Plan oder schon gekonnt“ zu.
- Suche: 139 bestanden, 9 Fehler – die bekannten alten (13, 15, 101, 103, 105, 111, 113, 126, 127).

**Nicht geprüft / Abweichungen**
- Nur mit Testdaten, nicht mit echten Lernständen im Browser angesehen.
- Im Auswahlmodus klappen links alle Orte auf (damit jeder Flug ein Häkchen hat) – auf dem Handy lang.
- Zähler im Kopf zählt Flüge (nicht Orte).
- Lehrplan-Übersicht: „andere Schularten“ steht jetzt klein hinter dem Titel statt in eigener Spalte (Zeile wie LB-1, passt weiter aufs Tablet).

## 2026-11-20 – FERTIG: Auftrag I, Teil 4 – App 0.82.0

Bilder: `docs/previews/la/teil4-fertig-390.png`, `lb-plan-820.png`.

**Umgesetzt**
1. Umschalter: unter 1100 px kurz „Themengebiet | Klasse“, ab 1100 px lang; kein Wort gebrochen.
2. Plan links auf dem Handy: lange Überschriften einzeilig mit „…“ (wie Tablet).
3. Kann-Punkte: Legende oben in der Spalte (kein inneres Rollen nötig); IB-Linie auch ohne MYP-Jahr (oben); kein doppeltes „–“ in der IB-Zelle bei Kl. 5 (Kinder-Tabelle, Karten, Überblick); Satz zum Pausentag (Kalendertag am Ort des Kindes) auf der Info-Seite und unter „Reisetage und Pausen“. Vorlese-Namen der Plan-Knöpfe nennen jetzt den Flug-Titel.
4. Inhalte ansehen: In geprüften/freigegebenen Flügen sind gesperrte Bordkarten „aussortiert“ (nicht „in Prüfung“), zugeklappt am Ende der Etappe „n aussortierte Bordkarten (ersetzt oder überzählig) anzeigen“; Etappen-Zeile und Kopf zählen nur aktive; Lehrplan-Übersicht „Fertig · n Etappen · m Bordkarten“ ohne aussortierte. „In Prüfung“ nur für Flüge im Entwurf. Info-Seite ergänzt.
5. Kinderansicht: a) nach dem Knobeln vom Landebildschirm (richtig, falsch, abgebrochen) zurück auf den Landebildschirm; b) gelandete, nicht fällige Etappe zeigt „Hier bist du fertig ✓“ mit großem Weiter-Knopf (nächste offene Etappe · „Zum Test“ · „Weiter zum nächsten Flug“ → Abflugtafel) und kleinem „Trotzdem weiterüben“; der Weiter-Knopf bleibt über jeder weiteren Bordkarte; c) Abflugtafel/„Weiter geht’s“ öffnen ohne Etappen-Nummer die empfohlene Etappe (fällig, sonst offen) – eine gelandete nur, wenn nichts offen ist, und dann mit dem Weiter-Knopf aus b).

**Gesehen/getestet** (in den 102 oben)
- Kein Wort gebrochen: Umschalter 820, Plan-Überschriften 400; Zählung ohne aussortierte (Inhalte ansehen + Lehrplan-Übersicht); Knobel → zurück auf Landung (abgebrochen und falsch); gelandete Etappe zeigt Weiter-Knopf, auch nach einer weiteren Bordkarte.

**Nicht geprüft**
- 5c nur über den Code und Test b), kein eigener Test für die Abflugtafel. In der alten (nicht „neu“) Kinderansicht führt Knobel-Zurück auf „Hier bist du fertig ✓“ statt auf einen eigenen Landebildschirm (dort gibt es keinen).

## 2026-11-20 – FERTIG: Auftrag I, Teil 1b (LA-8) – App 0.81.0 (zusammen mit Teil 1)

Zweig `bau-lehrer`, Stand `lernen-app` (mit Entwurf `lehrplan-spalte.html`) übernommen. Kein Merge. **Keine Migration nötig:** `schule_plan_lesen` liefert je Ort schon `kontinent` (= `schule.kontinent.titel`), `reihenfolge`, je Flug `jahrgang` (aus `schule.thema_jahrgang`, IB als MYP-Jahr) und `lehrplan_reihenfolge` (lesend geprüft). Die 10 aufgelösten Themen hängen an keinem Ort und erscheinen daher nicht (66 Orte, 95 Flüge).
Bilder: `docs/previews/la/la8-plan-1280.png`, `la8-plan-400.png`.

**Umgesetzt (nur Flugplan der Eltern/Lehrer; die Kinderansicht behält die Orte)**
1. **Überschrift „Themengebiet – Thema“** links und rechts (z. B. „Zahlen – Natürliche Zahlen und Ganze Zahlen“; ab 3 Flügen „A, B …“). Darunter „Gym 5 · RS 5 · MYP 1 · 0/2 Flüge“, links am Ende kursiv „Ort in der Reise: Rom“. Rückreise-Hinweis ebenso. Vorlese-Namen der Knöpfe (↑ ↓, +, ziehen, entfernen) nennen weiter den Ort – sichtbar ist er nicht in der Überschrift.
2. **Umschalter** oben in der Spalte: „Nach Themengebiet“ (Standard) | „Nach Klasse (Lehrplan)“.
3. **Nach Themengebiet:** Gebiet-Knöpfe in der Reihenfolge des Gestalters (nur Gebiete mit Orten), vorbelegt mit dem Gebiet des ersten offenen Ortes im Plan; „Sortiert nach Klasse in: Gymnasium | Realschule | IB MYP“, vorbelegt mit der Schulart des Kindes; alle Orte des Gebiets aus allen Klassen, sortiert nach Klasse (gewählte Schulart, fett), dann Lehrplan-Reihenfolge, dann Reihenfolge der Orte; Orte ohne Klasse in der gewählten Schulart ans Ende. Gestrichelte Linie „ab hier über Klasse X des Kindes“ (IB: „MYP-Jahr X“). Kopf „Zahlen: 4 von 8 Orten im Plan · von leicht nach schwer“ mit Balken. „+“ oder Ziehen plant jeden Ort ein, eingeplante grau mit „✓ im Plan“.
4. **Nach Klasse (Lehrplan):** wie LA-4 (Schulart, Klasse, „X von Y Flügen im Plan“, Suche), mit den neuen Überschriften und Farben.
5. **Farbe je Gymnasium-Klasse:** Kästchen mit der Zahl und linker Rand mit hellem Verlauf, links und rechts gleich (5 #2E7D32 · 6 #0277BD · 7 #6A1B9A · 8 #C62828 · 9 #EF6C00 · 10 #455A64); ohne Gymnasium-Klasse graues „–“; Legende unten in der Spalte.
- Info-Seite (Erste Schritte → Flugplan prüfen) um die zwei Ansichten und die Farben ergänzt.

**Abweichungen / Entscheidungen**
- **Kontrast:** Kästchen-Schrift weiß, bei Orange (9) dunkel – alle Kästchen ≥ 4,5 : 1 (im Test gemessen). Der orange Rand liegt auf der hellen Fläche bei 2,98 : 1 (Vorgabefarbe, knapp unter 3 : 1); die Klasse steht zusätzlich im Kästchen.
- **Dunkle Gestaltung:** Den Eltern/Lehrer-Bereich gibt es nur hell (`body[data-area=lernen]` setzt `color-scheme: light`); auch bei dunkler Systemeinstellung bleibt er hell. Getestet: Farben und Kontraste bleiben dann gleich. Eine eigene dunkle Variante habe ich deshalb nicht gebaut.
- **Tablet (700–1099 px):** links eine Zeile je Ort mit „…“ (voller Text als Tooltip und aufgeklappt), damit E-2 (12 Orte, Zeilen ≤ 72 px) weiter gilt. Handy und ab 1100 px brechen die Überschriften um wie im Entwurf.
- Die Lehrplan-Übersicht (LA-7, eigene Seite) ist unverändert: dort ist jede Zeile ein Flug, der Ort steht in einer eigenen Spalte.

**Gesehen/getestet**
- lernen: 94 von 94 (neu LA-8 ×3 für alle vier „Fertig, wenn“-Punkte: Gebiet des aktuellen Ortes vorbelegt; kein Ortsname in Überschriften links/rechts; Gym-9-Ort mit einem Tipp in den Plan eines Klasse-5-Kindes, gespeichert; Kästchen- und Randfarbe je Gymnasium-Klasse gemessen, auch bei dunkler Systemeinstellung; Handy ohne Querrollen). Angepasst: Plan-Tests auf neue Überschriften bzw. vorher „Nach Klasse (Lehrplan)“ wählen; Info-Seiten-Test lässt „Themengebiet“ zu.
- Suche: 139 bestanden, 9 Fehler – die bekannten alten (13, 15, 101, 103, 105, 111, 113, 126, 127).

**Nicht geprüft**
- Mit echten Daten (66 Orte) nur über die Datenlage gelesen, nicht im Browser angesehen; Testdaten sind nachgebildet.
- Ziehen aus der Ansicht „Nach Themengebiet“ nutzt denselben Ablauf wie in „Nach Klasse“ (E-2-Test dort); im Gebiet selbst nur „+“ getestet.
- Echte Geräte nicht.

## 2026-11-20 – FERTIG: Auftrag I, Teil 1 (Punkte 1–10) – App 0.81.0

Zweig `bau-lehrer` (Stand `lernen-app` mit Zusatz Punkt 10 übernommen). Kein Merge. Datenbank nur gelesen. Bilder: `docs/previews/la/i1-wackelt-400.png`, `i2-eltern-1280.png`, `i3-lehrplan-400.png`, `i8-start-820.png`, `i10-start-1280.png`, `i10-einstellen-400.png`.

**Umgesetzt**
1. **Was wackelt auf dem Handy (< 560 px):** je Etappe eine Karte (Kopf antippbar, Marken, „richtig / falsch“, „häufigster Fehler“, „seit“, aufklappbare Fehler mit „Besprochen ✓“); Tabelle nur ab 560 px. Reiterband passt auf 400 px.
2. **Wunsch in „Zu tun“:** Einlöse-Wunsch eines Kindes als blauer Eintrag mit „Bestätigen“/„Ablehnen“ direkt im Eintrag; Kasten „Wartet auf dich“ entfällt auf der Eltern-Startseite. Kopf „Was ist los?“ einzeilig, damit die Kinder-Tabelle auf 1280 × 800 ohne Rollen sichtbar ist.
3. **Lehrplan auf dem Handy:** Liste je Ort (Gruppe, Flug, Ort/andere Schularten, je Kind „geschafft/offen …“) statt Tabelle.
4. **Reisewörter erklärt:** Rückreise (Wiederholung nach nicht bestandenem Nachtest), Etappe (Lernschritt), Flug (Thema), Bordkarte (Aufgabe) – in Zu tun, Überblick, Was wackelt.
5. **Nachtragstest:** Link „Test zu den neuen Etappen“, wenn der Blocktest fertig ist und neue Etappen dazugekommen sind.
6.–9. Überblick-Satz mit Rückreise-Erklärung; „noch kein Inhalt“ bei Flügen ohne Einheit; Kinder-Tabelle (IB unter Kl. 6 „– (ab Kl. 6)“, Knöpfe nebeneinander, gleiche Zeilenhöhe); alle Texte mit „Datenbank“ durch „geht hier noch nicht“ ersetzt.
10. **Reisetage und Pausen:**
   - Migration `supabase/migrations/20261120_i_pause.sql` (nicht ausgeführt): Tabelle `schule.pause` (Kind, von, bis, grund ≤ 40 Zeichen, wer, am, geaendert_am, geloescht_am; höchstens 1 Jahr; RLS an). Löschen = als gelöscht markieren (kein DELETE).
     Eintragen/ändern/löschen über die **bestehende** Aktion `schule_notiz_setzen` mit `pause` (`{lernender_id, pause}`, `{alle: true, pause}` für alle sichtbaren Kinder ohne Testkinder, `{pause: {id, …}}`, `{pause: {id, loeschen: true}}`) – nur Eltern/Lehrer, Zugriff aufs Kind geprüft. Zweige „besprochen“ (LA-3) und Notiz unverändert. `schule_lernstand` liefert `pausen[]`. lernen-api braucht keine Änderung.
   - Rauchtest `supabase/tests/i_pause_rauchtest.sql` (Rollback, nur Testkind, legt eigene Einträge an).
   - App: „⚙ Einstellen“ des Kindes hat die Karte „Reisetage und Pausen“ (Eintragen mit von/bis, Wahl Reisetag/krank/Ferien oder eigenes Wort; Liste mit Ändern/Löschen; vergangene grau mit „vorbei“). Startseite: „+ Reisetag eintragen“ oben in „Zu tun“ (Blatt, vorbelegt heute und „alle Kinder“).
     Wirkung: heute in einer Pause → „Lernt“ blau „Pause bis 23.11. (Reisetag)“ statt rot/gelb, kein „kein Lerntag“ in Zu tun. Vergangene Pausentage werden beim Zählen „seit … kein Lerntag“ ausgelassen (Text in Zu tun dann z. B. „seit 6 Tagen kein Lerntag (ohne Pausentage: 3)“). Lernregeln unverändert.
   - Solange die Migration nicht eingespielt ist, steht im Blatt „Reisetage lassen sich hier noch nicht eintragen.“ und der Startseiten-Knopf fehlt.
   - Info-Seite: Absatz „Reisetage und Pausen“.
- Entschieden, nicht gebaut: Stand-Zellen bleiben ohne Ampelfarbe.

**Gesehen/getestet**
- lernen: 91 von 91 vor LA-8, 94 von 94 mit LA-8 (neu I-1 bis I-10; angepasst u. a. Eltern-Wunsch, Lehrplan/Wackelt bei 820 px, Reisewörter, E-2, IB, LA-2, LA-6, W177).
- Suche: 138 bestanden, 10 Fehler – die bekannten alten aus Reisen/PWA (13, 15, 101, 103, 105, 111, 113, 126, 127) plus 108, der gelegentlich wackelt; keiner betrifft die Lern-Seiten.
- Migration und Rauchtest: mit pglast geparst; keine Variablen-/Alias-Doppelungen; Ankerstelle in `schule_lernstand` und der heutige Text von `schule_notiz_setzen` (mit LA-3-Zweig) vorher lesend geprüft.

**Nicht geprüft**
- Migration und Rauchtest nicht ausgeführt (Haupt-Chat). Der Weg über `schule_notiz_setzen` mit echtem Zugangsschlüssel (`alle`, Zugriffsprüfung) ist nur im Rauchtest-Umfang (Funktionstext enthält den Zweig) geprüft, nicht als Aufruf.
- „Pause“ zählt nach dem Kalender des Geräts (Ortszeit); Lerntage kommen aus der Datenbank – an einem Tag mit Zeitzonenwechsel kann ein Tag verrutschen.
- Echte Geräte (iPhone, iPad) nicht; nur Chromium bei 400/820/1280 px.

## 2026-11-20 – Test „LA-1: Seite des Kindes mit 4 Reitern“ stabil

- Stand von `lernen-app` übernommen. Im Test wird jetzt nach `waitForURL` erst auf den gezeichneten Reiter gewartet (`.lern-reiter a[aria-current]` „Überblick“), dann werden die Reiter gelesen. Sonst nichts geändert.
- **Ergebnis:** lernen 81 von 81 – zweimal hintereinander im Gesamtlauf.
  Suche: 138 bestanden, 10 Fehler – die bekannten alten aus Reisen/PWA (13, 15, 101, 103, 105, 111, 113, 126, 127) plus 108 („W80: Jede neue Suche hat eine Reise …“), der schon früher gelegentlich wackelte; keiner betrifft die Lern-Seiten.

## 2026-11-18 – FERTIG: Auftrag LA (LA-1 bis LA-7) – App 0.80.0

Zweig `bau-lehrer` (von `lernen-app` b8f910e), kein Merge. Reihenfolge wie verlangt: LA-1 → LA-2 → LA-6 → LA-3 → LA-5 → LA-4 → LA-7; je Paket eine Meldung unten.
- **Migrationen** (nur als Datei, nicht ausgeführt, unabhängig von Auftrag H einspielbar – andere Ersetz-Stellen): `20261119_la_3_besprochen.sql`, `20261119_la_4_kann_schon_fluege.sql`;
  Rauchtests `supabase/tests/la_3_rauchtest.sql`, `la_4_rauchtest.sql`. Keine neue Aktion in `lernen-api`, kein DROP, kein DELETE.
- **App 0.80.0**; ohne die Migrationen läuft alles, nur „Besprochen ✓“ meldet „geht, sobald die Datenbank dafür bereit ist“ und „kann schon“ je Flug zeigt einen Hinweis statt Häkchen.
- **Tests:** lernen 80 von 80; Suche: dieselben 9 alten Fehler wie auf lernen-app (Reisen/PWA, nicht Lernen).
- **„Fertig, wenn“:** Tablet-Startseite mit „Zu tun“ und Tabelle ohne Rollen ✓ · Kind B mit 0 Lerntagen rot ✓ · Startseite → falsche Antworten einer wackelnden Etappe: 1 Tipp ✓ ·
  Plan 820 px zweispaltig, Abdeckung sichtbar, „kann schon“ je Flug zählt ✓ · Geschafftes nicht mehr zwischen offenen ✓ · Klasse/Stufen/Notizen nur im ⚙-Blatt ✓ · Lehrplan Gym 5 (14 Flüge) auf einem Tablet-Bildschirm ✓ (je eigener Test).
- **Bilder** (Mock-Daten): `docs/previews/la/` – la2-start-*, la1-ueberblick-*, la6-blatt-*, la3-wackelt-*, la4-plan-*, la5-geschafft-820, la7-lehrplan-* (820 / 400 / 1280).
- **Offen / nicht gebaut:** „Pausen/Reisetage“ als Ausnahme für rot (gibt es noch nicht, Abweichung 4); Ampel für die Stand-Zellen (bewusst weggelassen, s. LA-2);
  „Kurz gesagt“ in allen Themen-Dateien vorhanden? – nicht geprüft (Inhalts-Chats).

## 2026-11-18 – FERTIG: LA-7 Nachschlagen (7A)

- Lehrplan-Übersicht `#/lehrplan` als **kompakte Tabelle**: oben Reiter Gymnasium · Realschule · IB MYP, Klassen-Knöpfe mit Marken der Kinder (Klasse des Kindes: Buchstabe, z. B. „A“, „B“), „alle Klassen“, Suche, „⛰ Expeditionen ansehen“.
- Eine Zeile je Flug: Flug · Ort · andere Schularten · Inhalt (● fertig, ◐ in Prüfung, ○ fehlt; Punkte als Formen, nicht Schriftzeichen) · Stand je Kind (Spalte je Kind, „· im Plan“).
  Zeilen nach Klasse und Kontinent gruppiert. Zeile antippen → „Inhalte ansehen“; fehlt der Inhalt, steht klein „✎ Ändern lassen“ (Auftrag „Neuer Flug“ wie bisher).
- Vorbelegt mit Schulart und Klasse des ersten Kindes; Zähler (Flüge · fertig · in Prüfung · fehlt) sind zugleich Filter.
- Ziel „eine Klasse passt auf einen Tablet-Bildschirm“: Test mit 14 Flügen Gym 5 bei 820 × 1180 ✓. Info-Seite: Abschnitt zur Lehrplan-Übersicht angepasst.
- Bilder: `la7-lehrplan-820.png`, `la7-lehrplan-400.png`, `la7-lehrplan-1280.png`.

## 2026-11-18 – Zwischenmeldung nach LA-4 (Bilder)

`docs/previews/la/`: Plan Tablet 820 px `la4-plan-820.png` (zwei Spalten, Rom aufgeklappt, „kann schon“ je Flug), Handy 400 px `la4-plan-400.png`, Rechner `la4-plan-1280.png`,
Block „Geschafft“ `la5-geschafft-820.png`. Mock-Daten, keine Kinderdaten.
„Fertig, wenn“: Plan auf dem Tablet in zwei Spalten ✓ (Test misst es); Abdeckung der Klasse sichtbar ✓; „kann schon“ je Flug zählt im Stand ✓ (Server: thema_stand/ort_stand; App: Stand-Modell, Abflugtafel);
geschaffte Orte nicht mehr zwischen offenen ✓; Klasse, Stufen, Notizen nur im ⚙-Blatt ✓.

## 2026-11-18 – FERTIG: LA-4 Flugplan (4A)

**Migration** `supabase/migrations/20261119_la_4_kann_schon_fluege.sql` (nicht ausgeführt; pglast ok; alle Ersetz-Stellen im Live-Text je genau einmal; kein DROP, kein DELETE; Kollisions-Prüfung ohne Treffer):
- `route.kann_schon_themen bigint[]` (Abweichung 3), entsprechend `ausgelassen`. `schule_plan_setzen` nimmt `eintraege[].kann_schon_themen` (fehlt es, bleibt die Liste; Flug muss zum Ort gehören);
  wird „kann schon“ in einem fertigen Ort zurückgenommen, prüft der Server den Ort wie bei „ausgelassen“ und macht ihn ggf. wieder offen – **Rückgängig ohne Verlust**.
- Zählt wie gelandet in `thema_stand` (Lehrplan-Übersicht, Konto) und `ort_stand` (Ort-Abschluss → Status „fertig“, Stempel wie bisher), **nicht** als `karte_stand.sitzt` → keine Mischkarten, Wiederholungen, Expeditionen daraus.
  Neue Hilfsfunktion `schule.thema_kann_schon` (Flug einzeln oder ganzer Ort). `schule_plan_lesen`: `plan[].kann_schon_themen`, `themen[].kann_schon`; `schule_uebersicht`: `route[].kann_schon_themen`.
- Das bisherige „kann schon“ des ganzen Orts bleibt („alle Flüge: kann schon“).
- Rauchtest `supabase/tests/la_4_rauchtest.sql` (Rollback, Testkind): ein Flug → thema_stand erledigt; alle Flüge → Ort abgeschlossen, keine Karte angelegt; zurückgenommen → wie vorher; wdh_in.

**App (Reiter „Plan“):**
- Zwei Spalten ab 700 px (Tablet hochkant eingeschlossen), Handy untereinander. Kopf „Gymnasium Kl. 5 · n offen · n geschafft · Gespeichert · ↶ Rückgängig“.
- Links nur offene Orte (Griff ⠿, ↑ ↓; Ziehen/Pfeile bewegen zwischen den offenen, die Lernreise-Reihenfolge der geschafften bleibt).
- Ort aufgeklappt: je Flug „im Plan“ (links), Klassen, Stand, rechts „kann schon“ je Flug (erst wenn die Datenbank das Feld liefert; vorher Hinweis), „ansehen“; Flug einer höheren Klasse: „Gym 6 – höhere Klasse“ (L9).
- Rechts der Lehrplan: Reiter Gymnasium · Realschule · IB MYP, Klassen-Knöpfe (vorbelegt mit Klasse/Stufe des Kindes, „alle“), Zeile „Klasse 5: n von m Flügen im Plan“ mit Balken,
  alle Orte der Klasse: eingeplante mit ✓ (grau, „im Plan“), fehlende mit ⠿ und „+“; Suche bleibt.
- „Kann schon“ je Flug in der App: Stand (Lernstand-Modell, eigener Zustand „kann schon“), Abflugtafel des Kindes (Gruppe „konnte ich schon“), Überblick „Zuletzt geschafft“.
- Tests: LA-4 ×2 (zwei Spalten, Abdeckung, ✓, „kann schon“ speichert `kann_schon_themen`, Hinweis höhere Klasse, Stand-Modell).

## 2026-11-18 – FERTIG: LA-5 Geschafftes (5A)

- Geschaffte Orte (Status „fertig“, ganzer Ort „kann schon“ oder alle geplanten Flüge gelandet/„kann schon“) stehen nicht mehr im Plan, sondern darunter im **zugeklappten** Block „Geschafft (n)“.
- Je Flug: Ort · Flug · gelandet am (letzte Landung, aus `schule_lernstand`; bei „kann schon“ ohne Landung: „kann schon“) · Nachtest (aus `schule_merkheft`: bestanden / fällig / fällig in n Lerntagen)
  · nächste Wiederholung (neu `wdh_in` je Etappe, Migration LA-4; „jetzt fällig“ / „in n Lerntagen“; ohne Migration „–“).
- Überblick: die letzten 3 geschafften Flüge als Zeile (seit LA-1; jetzt mit „kann schon“-Flügen hinten, ohne Datum).
- Reihenfolge der Lernreise unverändert; nur die Anzeige trennt Offen und Geschafft. Als Liste statt Tabelle (in der linken Spalte des Tablets ist eine 5-spaltige Tabelle zu schmal).
- Test LA-5 (Ort fertig → nicht in der Liste, „Geschafft (1)“ zugeklappt, Werte je Flug). Tests gesamt: lernen 79 von 79.

## 2026-11-18 – FERTIG: LA-3 Was wackelt (3B)

**Migration** `supabase/migrations/20261119_la_3_besprochen.sql` (nicht ausgeführt; pglast ok; Ersetz-Stellen im Live-Text je genau einmal geprüft; kein DROP, kein DELETE; Skript-Prüfung auf Variable/Alias-Kollisionen ohne Treffer):
- Neue Tabelle `schule.besprochen` (Kind, Einheit, Lernkarte, von, am; eine Zeile je Kind + Etappe, RLS an wie die übrigen schule-Tabellen).
  `schule.besprochen_aktiv(…)`: gilt, solange danach keine **endgültig** falsche Antwort in der Etappe kam (1. Versuch mit zweiter Chance zählt nicht).
- Setzen über die **bestehende** Aktion `schule_notiz_setzen` mit `{lernender_id, besprochen: {einheit_id, lernziel}}` – keine neue Aktion in `lernen-api`. Lehrer und Eltern (ist_leiter), Zugriff auf das Kind geprüft.
- `schule_lernstand` je Etappe neu: `regel` („Kurz gesagt“), `besprochen_am`/`besprochen_von` (nur gültig), `fehler_gruende` {grund: Anzahl}; in `fehler[]` je Antwort `grund`.
  `grund` wird – wie beim Prüfen – aus der gespeicherten Antwort berechnet (`antwort_bewerten`); in `versuch` gibt es keine Spalte dafür.
- Rauchtest `supabase/tests/la_3_rauchtest.sql` (Rollback, Testkind): besprochen aktiv → 1. Versuch falsch bleibt → endgültig falsch holt zurück; Fehlerarten als Objekt.

**App:** Reiter „Was wackelt“ = Kopfzeile „Diese Woche: n Bordkarten, n richtig · n Lerntage“, dann **eine Tabelle** aller Etappen mit Fehlern (wackelt zuerst, dann nach Datum): Etappe (Ort darunter) · richtig / falsch · häufigster Fehler · seit.
- Häufigster Fehler nur, wenn ein `grund` bei mindestens zwei falschen Antworten vorkommt, sonst „–“ (Abweichung 5). Keine Aussage, wie das Kind gerechnet hat.
- „seit“ = Datum der ältesten der (bis zu 3) gespeicherten letzten falschen Antworten – schlichteste Lösung; die Datenbank liefert keinen „wackelt seit“.
- Zeile antippen: letzte 3 falsche Antworten (Bordkarte · Antwort · richtig), „Kurz gesagt“, „Erklärung ansehen ›“, „Besprochen ✓“. Danach Marke „besprochen 18.11.“, Etappe fällt aus „Zu tun“.
  Ohne Migration meldet der Knopf „‚Besprochen‘ geht, sobald die Datenbank dafür bereit ist.“
- Gelber „Zu tun“-Eintrag öffnet die Etappe schon aufgeklappt → **1 Tipp** von der Startseite zu den falschen Antworten (Ziel: höchstens 2).
- Regelblock „Was kommt wann wieder?“ entfällt hier (steht auf „So funktioniert’s“ unter „Wie wird gelernt?“). Der bisherige Stand je Etappe steht zugeklappt unter „Alle Etappen mit Stand“.
- „Kurz gesagt“ fehlt in keiner Etappe der Themen-Dateien? – nicht geprüft (Inhalts-Chats); fehlt `regel`, entfällt die Zeile.
- Bilder: `docs/previews/la/la3-wackelt-820.png`, `la3-wackelt-400.png`. Info-Seite: Eintrag „Was wackelt“. Tests: lernen 76 von 76.

## 2026-11-18 – FERTIG: LA-6 Einstellungen (6B)

- „⚙ Einstellen“ (mit Text) in der Tabellenzeile/Karte der Startseite und im Kopf der Kind-Seite öffnet ein Blatt „Kind A einstellen“ – Tablet/Rechner von rechts, Handy von unten; Esc, × oder Tippen daneben schließt.
- Karten, alles speichert sofort (`schule_kind_setzen`, `schule_notiz_setzen`, `schule_plan_setzen` – keine neue Aktion, keine Migration):
  1. Schule: Hauptschulart (Knöpfe) und Klasse (Knöpfe 5–10) – „Bestimmt seine Klasse in Lernreise und Plan.“
  2. Stand messen gegen …: Stufe je Schulart (Gym, RS, IB MYP; „aus Klasse (…)“, IB unter Klasse 6 „noch kein MYP-Jahr“) – „Nur für die Anzeige ‚Wo steht es?‘ – ändert nichts an der Lernreise.“
  3. Notizen und Verlauf (zugeklappt).
  4. Neuer Plan aus Lehrplan-Vorlage – **mit Rückfrage** („Ja, Plan ersetzen“ / „Abbrechen“), danach „↶ Rückgängig“ im Blatt.
- Der Plan zeigt Vorlage, Klasse, Stufen, Notizen, Verlauf nicht mehr. Schließen nach einer Änderung zeichnet die Seite neu.
- Schlichteste Lösung, wo der Text offen ist: Klasse als Knöpfe 5–10 (die Datenbank nimmt 1–13; andere Werte bleiben erhalten, solange niemand einen Knopf drückt).
- Bilder: `docs/previews/la/la6-blatt-820.png`, `la6-blatt-400.png`. Info-Seite: Abschnitt „⚙ Einstellen“. Tests: lernen 74 von 74.

## 2026-11-18 – Zwischenmeldung nach LA-2 (Bilder)

Bilder (Mock-Daten, keine Kinderdaten) in `docs/previews/la/`:
- Startseite Tablet 820 px: `la2-start-820.png` · Handy 400 px: `la2-start-400.png` · Rechner 1280 px: `la2-start-1280.png`
- Überblick der Kind-Seite Tablet: `la1-ueberblick-820.png` · Handy: `la1-ueberblick-400.png`

Prüfpunkte aus „Fertig, wenn“: Tablet – „Zu tun“ und Kinder-Tabelle ohne Rollen sichtbar (Test misst es); Kind B mit 0 Lerntagen ist rot (Zeile und „Zu tun“).

## 2026-11-18 – FERTIG: LA-2 Startseite (2B)

- **Zu tun** oben, rot → gelb → blau, je Eintrag ein Link:
  rot = letzter Lerntag ≥ 3 Kalendertage zurück oder keiner in 4 Wochen (→ Überblick), offene automatische Rückreise (= Nachtest unter 60 %, → Plan);
  gelb = Etappe wackelt (≥ 3 falsch und mehr falsch als richtig, oder wieder offen) und nicht besprochen (→ Was wackelt; „besprochen“ kommt mit LA-3);
  blau = Antwort auf einen Auftrag in den letzten 7 Tagen (→ Meine Aufträge). Leer: „Alles ruhig.“
- **Tabelle** je Kind: Kind (Name, Schulart Kl.) · Lernt · Wackelt · GYM · RS · IB (Stufe und Prozent, Rechenregel K3) · Jetzt · Knöpfe. Zeile antippen → Überblick des Kindes.
  Farbe nur bei Lernt (rot ≥ 3 Tage, gelb 2 Tage, sonst grün) und Wackelt (rot Rückreise, gelb offene wackelnde Etappe, sonst grün).
  **Stand-Zellen ohne Ampel** (schlichteste Lösung, Entwurf liegt nicht vor): Mitte des Schuljahrs wären fast alle Prozentwerte „rot“, das wäre irreführend.
- **Handy < 560 px:** je Kind eine Karte mit denselben Feldern.
- **„Lernen starten“** (Abweichung 1): Rolle Eltern – in jeder Zeile/Karte und im Kopf der Kind-Seite; Rolle Lehrer – entfällt, im Kopf klein „Lernreise ansehen ›“.
  Rolle: Lern-Seite aus `schule_ich`; die ganze App ist der Eltern-Zugang.
- **IB unter Klasse 6:** überall „noch kein MYP-Jahr“ (statt „vor MYP-Jahr 1 · 0/0“), auch in Abflugtafel, Stand und Info-Seite.
- „Eingetragene Pausen/Reisetage“ gibt es noch nicht – rot gilt ohne diese Ausnahme (Abweichung 4).
- Daten: je Kind `schule_lernstand` (Lerntage 4 Wochen, Woche, Etappen) – keine neue Aktion, keine Migration.

## 2026-11-18 – FERTIG: LA-1 Gliederung (1A)

- Startseite `#/lernen` (Eltern/Lehrer) = „Was ist los?“: Zu tun · Kinder-Tabelle · Zeile „Nachschlagen“ (Lehrplan · Expeditionen · Meine Aufträge · So funktioniert’s); darunter „Verwalten“
  (Testkind, Zugänge nur Eltern, eigene Lernen-Seite) und für Eltern die Belohnungen. „So funktioniert’s“ zusätzlich oben rechts.
- Neue Kind-Seite `#/kind/<id>-<reiter>` mit Reitern **Überblick · Was wackelt · Stand · Plan**. Kopf: Name, Schulart/Klasse, „⚙ Einstellen“ (bis LA-6: öffnet den Plan),
  „Lernreise ansehen“ (Lehrer) bzw. „Lernen starten“ (Eltern), „So funktioniert’s“.
- Alte Adressen `#/lernstand/<id>[-…]`, `#/wackelt/<id>`, `#/plan/<id>` leiten auf den Reiter um (auch mit Schulart/Ebene: `#/lernstand/1-gym_by-7` → `#/kind/1-stand-gym_by-7`).
- **Überblick:** Lernt es? (Lerntage diese Woche, zuletzt, Bordkarten 7 Tage) · Wo hakt es? (bis 3 wackelnde Etappen, Rückreise) · Wo steht es? (drei Schularten, Prozent) · Was kommt? (Jetzt) · Zuletzt geschafft (3 Flüge mit Datum der letzten Landung).
- „Alle Kinder im Vergleich“ (`#/schulstand`) bleibt erreichbar, ist aber nicht mehr verlinkt.
- Plan-Kopf jetzt eine Zeile („Gymnasium Kl. 5 · 10 offen · 2 geschafft · Gespeichert · ↶ Rückgängig“) – sonst passten 12 Orte unter Kopf und Reitern nicht mehr auf das Tablet.
- Info-Seite: Startseite, Seite des Kindes, „Lernen starten“ je Rolle; Erste Schritte verlinken die Reiter.
- Tests: lernen 73 von 73 (neu LA-1, LA-2 ×4; angepasst: Wege über die Kind-Seite, IB-Beschriftung, Ziehen mit Kopf).
