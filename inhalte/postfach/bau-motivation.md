# Postfach bau-motivation (Bau-Chat, Bau-Auftrag G / Werkstatt-Wunsch 176)

Neueste oben.

## 2026-11-22 – FERTIG: 0.86.3 – Nachtrag WD-S 4 (ChatGPT 921), Teil bau-motivation (Cache v159)

Auf `lernen-app` d0e911e. Nur App, Version in sechs Dateien, Tests. Nichts in der Datenbank, kein Merge nach `main`.
- **Keine frische Aufgabe (Sollte 2):** „Noch 3 Extra-Bordkarten?“ erscheint nur noch, wenn mehr fällig ist **und** der Server dafür wählbare Bordkarten liefert (`aufgaben[]` ohne `pflicht` bzw. nach der Runde überhaupt welche). Sonst steht ruhig „Heute keine passende frische Aufgabe – bleibt für später offen.“ – auf der Abflugtafel (beide Designs), nach „Eingecheckt!“ und auf `#/wiederholen/<kind>-extra`.
- **Kein „für immer“ (Sollte 4):** Etappe abgelegt oben „ABGELEGT“, Siegel „★ ABGELEGT“ (statt „FÜR IMMER“), Flug abgelegt „ALLE ETAPPEN ABGELEGT“ und „Alle n Etappen von … sind abgelegt.“, Reisepass „alle Etappen abgelegt“, Satz „Gold heißt: Alle Etappen sind abgelegt.“ Die Vorgabe des Gestalters (`inhalte/pruefung/kind/abgelegt/`) nennt noch „FÜR IMMER“ – **bitte dort nachziehen** oder anderen Wortlaut liefern.
- **0 Sterne bei Hilfe:** Wiederholung (Runde, Extra) und Mischkarte zeigen nur den Serverwert; bei `sterne: 0` (bzw. `wiederholung.sterne` 0) keine Sterne, der Zähler bleibt stehen (Test).
**Getestet:** lernen 159 von 159 (neu 2), Gesamtlauf sonst nur die bekannten Reise-Fehler.
## 2026-11-22 – bau-lehrer – FERTIG: FP-S

Bau-Auftrag FP, Teil FP-S. Nur Dateien, nichts eingespielt, Nachbuchung nicht ausgeführt (nur lesend nachgerechnet). Kein DROP einer Tabelle/Spalte, kein DELETE.

**Dateien:** `supabase/migrations/20261122_fp_s_faire_punkte.sql` (nach WD-S 2 und WD-S 3, eine Transaktion), `supabase/tests/fp_s_rauchtest.sql`.

**Was gebaut ist**
- Regel 1: `sterne_aus_versuch` bucht 10 (`sterne_uebung_richtig`) nur bei richtig im ersten Versuch ohne Tipp, sonst 5 (`sterne_uebung_mit_hilfe`). Je Aufgabe weiter eine Buchung – die erste richtige Antwort entscheidet (wer zuerst mit Tipp löst, bekommt für diese Aufgabe später keine 10 mehr; Annahme, bitte bestätigen). Gilt auch für Mischkarten, die als Übung gebucht werden; Wiederholungen bleiben wie in WD; Knobeln unverändert.
- Regel 2/3: Bonus im Moment der Landung (Haken in `landung_speichern`, das nur bei einer echten Landung aus `karte_buchen` läuft): 80 / 40 / 10 nach `fehler_endgueltig` aus `landung_zaehlen` (dieselbe Zählung wie die Landungs-Art seit AB-S: nur Übung dieser Etappe, ohne Tests, Mischkarten, Wiederholungen; Tipp ist kein Fehler). Neuer Sterne-Grund `landung` (Prüfregel ersetzt, vorher gegen den WD-S-2-Stand geprüft), `bezug 'landung:<einheit>:<etappe>'` eindeutig → doppelter Aufruf und gleichzeitige Antworten: genau eine Buchung (die Landung selbst ist zusätzlich über die Zeilensperre in `karte_buchen` serialisiert). Gesetzte Etappen („Kann er“, `gesetzt_am`) bekommen keinen Bonus.
- Regel 4: `schule.landung_bonus_nachbuchen()` (auch je Kind: `(p_l)`) – liefert je Kind `etappen`, `sterne`; zweiter Lauf bucht nichts. Schreibt `schule.landung_nachbuchung` für den einmaligen Hinweis der App.
- Antworten: `schule_uebung_pruefen` liefert jetzt **immer `sterne`** (in diesem Aufruf tatsächlich gebucht: Übung + Wiederholung + Bonus + Ablegen) und bei der Landung **`landung {…, bonus, fehler, stufe: 'ohne'|'wenig'|'sonst'}`** (zur bisherigen Landungs-Einblendung dazu). `schule_konto` liefert **`regeln`** (alle Sterne-Regeln) und **`landung_nachbuchung {etappen, sterne, am}`** (null, solange nicht nachgebucht).

**Rauchtest** (lokal grün, Postgres 16 mit byte-gleichen Live-Funktionen inkl. `landung_speichern`/`landung_zaehlen`; zusammen mit WD-S- und WD-S-3-Test grün): 10/5/5/0, Bonus 80/40/10 (0/2/3 Fehler) über den echten Antwortweg, genau einmal, gesetzte Etappe ohne Bonus, Nachbuchung zweimal = einmal, Regeln, Lernstände/Stufen/Karten/Sterne der anderen Kinder unverändert. Der Test nimmt nur Etappen, die das Testkind nie beantwortet hat, und setzt die Karte selbst kurz vor die Landeschwelle – unabhängig von der Zusammensetzung echter Etappen.

**Nachbuchung – lesender Lauf auf der echten Datenbank (22.11., nur Nummern)**

| Kind | Sterne vorher | Etappen echt gelandet | ohne / 1–2 / mehr Fehler | Bonus | Sterne nachher | gesetzt (kein Bonus) |
|---|---|---|---|---|---|---|
| 1 | 2740 | 25 | 17 / 6 / 2 | +1620 | 4360 | 0 |
| 2 | 3970 | 28 | 27 / 1 / 0 | +2200 | 6170 | 36 |
| 3 (Testkind) | 120 | 6 | 5 / 1 / 0 | +440 | 560 | 0 |

Hinweise: Bei 16 bzw. 21 Etappen gibt es keine gespeicherte Landung (vor AB-S gelandet) – dort zählt die Nachbuchung die Fehler aus den Versuchen bis zur Landung neu. Die Nachbuchung erhöht den Kontostand um rund 55–60 % – vor dem Ausführen bitte mit Sebastian abstimmen (Belohnungen/Einlösungen hängen an Sternen).

## 2026-11-22 – bau-lehrer – FERTIG: WD-S 3 Test

Auf „Nachtrag WD-S 3 – Rauchtest stabil machen“. Nur `supabase/tests/wd_s3_rauchtest.sql` geändert, keine Migration.
- Vor Schritt 1 werden alle übrigen Übungsaufgaben beider Test-Etappen (alles außer Auswahl Stufe 2–3) als **gestern** beantwortet markiert (Testsitzung, also ohne Buchung; Lerntag gestern wird angelegt) – damit innerhalb der Sperre, aber nicht „heute“ (sonst wäre die Mischkarte in Schritt 3 zu Recht gesperrt).
- Lokal nachgestellt: Etappe mit zusätzlichen Aufgaben anderer Art → alter Test bricht wie im Probelauf in Schritt 2 ab („nicht die am längsten zurückliegende“), neuer Test läuft ganz durch.

## 2026-11-22 – FERTIG: 0.86.2 – Fehler Mischkarten (App-Teil) und ChatGPT 919 (Cache v158)

Auf `lernen-app` f278a3c. Nur App (`lernen.js`, `style.css`), Version in sechs Dateien, Tests. Nichts in der Datenbank, kein Merge nach `main`.

**Fehler Mischkarten (22.11.), Teil bau-motivation**
- **(a) Eine gezeigte Mischkarte ist für die ganze Sitzung des Flugs verbraucht** (`ctx.mischGezeigt`), nicht mehr je Etappe neu. Verbraucht ist sie, sobald sie gezeigt wurde, auch unbeantwortet. Ist die Liste leer, holt die App sie **einmal** je Sitzung im Hintergrund neu (`schule_einheit_lesen`, nur `mischkarten` werden übernommen); schon gezeigte bleiben verbraucht, sonst geht es ohne Mischkarte weiter. Neue Sitzung (Flug neu geöffnet) = neue Liste vom Server – die Frische über Sitzungen hinweg regelt WD-S 3.
- **(b) Sterne nur aus der Antwort des Servers:** `sterne` (tatsächlich gebucht), sonst `wiederholung.sterne`. Eine Mischkarte ohne beides zeigt keine Sterne. **Einschränkung:** Bei einer normalen Bordkarte und einem Server ohne `sterne` (heute live: `sterne` nur bei Knobel-Bordkarten) bleibt die bisherige Anzeige „+10 beim ersten Richtig“, sonst stünden bei jeder Landung 0 Sterne. **Bitte an bau-lehrer (WD-S 3):** `sterne` in **jeder** Antwort von `schule_uebung_pruefen` mitschicken (auch 0) – dann rechnet die App nirgends mehr selbst. Im Check-in: `wiederholung.sterne`, sonst `sterne`.
- **(c) `misch.gueltig === false`:** kein „Das war …“, kein „↻ Zählt als Wiederholung“, Sterne nur laut Server.

**ChatGPT 919, Teil bau-motivation**
- `wiederholung.bestanden === false` bei richtiger Antwort (mit Tipp oder im zweiten Versuch): „Richtig – morgen noch einmal ohne Hilfe.“ – bei der Mischkarte unter „✓ An Bord“, im Check-in statt „Richtig!“; Koffer hellgelb ohne Stern (neuer Zustand), keine Sterne, kein Fehlerton.
- Nach dem Ablegen nicht mehr „kommt nicht mehr wieder“: Ticket „5-mal wiederholt, über 30 Lerntage. Raus aus der regelmäßigen Wiederholung – nur noch bei Bedarf zum Auffrischen.“; Kindertext „… ist sie abgelegt: Sie ist raus aus der regelmäßigen Wiederholung und kommt nur noch, wenn sie aufgefrischt werden muss“; Info-Seite „Sie fällt aus der regelmäßigen Wiederholung und wird nur noch bei Bedarf aufgefrischt“. Die Gestalter-Wörter „FÜR IMMER GELERNT“/Siegel „FÜR IMMER“ und „sitzen für immer“ (Flug abgelegt) habe ich gelassen – bitte prüfen, ob sie zum neuen Satz passen.

**Getestet:** lernen 157 von 157. Neu: „drei Etappen nacheinander – keine Mischkarte doppelt; leere Liste einmal neu vom Server, danach ohne Mischkarte“ (schlägt mit 0.86.1 fehl, mit 0.86.2 grün); „Sterne nur vom Server; gueltig false; bestanden false“; „Check-in – richtig mit Hilfe“. Angepasst: WD-3 zeigt jetzt +5 (nur `wiederholung.sterne`) statt 10 + 5. Gesamtlauf sonst nur die bekannten Reise-Fehler.
**Nicht geprüft:** echter Server (WD-S 3 noch nicht da), echte Geräte.

## 2026-11-22 – bau-lehrer – FERTIG: WD-S 3

Auf AUFTRAEGE.md „Fehler Mischkarten (22.11.)“, Nachtrag „WD-S 3 – frische Aufgaben“ und „ChatGPT 919“, Teil bau-lehrer. Nur Dateien, nichts in der echten Datenbank ausgeführt (nur lesende Abfragen), kein App-Code. `sterne_wdh_richtig` bleibt 10.

**Dateien**
- `supabase/migrations/20261122_wd_s3_frische_aufgaben.sql` – neu, nach WD-S 2 einspielen (eine Transaktion).
- `supabase/migrations/20261122_wd_4b_stau_strecken.sql` – überarbeitet (nicht eingespielt): jetzt als Funktionen `schule.wdh_staffel_strecken` / `schule.wdh_staffel_zurueck`, nach WD-S 3 einspielen.
- `supabase/tests/wd_s3_rauchtest.sql` (neu, 7 Teile), `supabase/tests/wd_s3_gleichzeitig.sh` (neu, zwei gleichzeitige Transaktionen – **nur Wegwerf-Datenbank**, schreibt Daten), `supabase/tests/wd_s3_lesend.sql` (neu, nur lesend). `wd_s_rauchtest.sql` Teil 10 nimmt jetzt eine heute noch nicht beantwortete Etappe (sonst sperrt die neue Regel die Mischkarte zu Recht).

**(1) Frische Aufgaben** – eine Auswahl für Wiederholung und Mischkarte (`schule.wdh_aufgabe_waehlen`): nie aus den letzten 3 Lerntagen (heute + 2 vorige **Lerntage**, Reisetage zählen nicht; jede Rolle inkl. Test und Knobeln; Regel `wdh_sperre_lerntage`), zuerst nie beantwortete (darunter zufällig), sonst die am längsten zurückliegende, sonst heute keine (Wiederholung bleibt fällig, in der Runde = bearbeitet). Stufe 3–4: beliebig, bevorzugt die am längsten zurückliegende – „noch nie“ zählt dabei als am längsten zurück; damit fallen beide Regeln in eine Reihenfolge zusammen (Annahme, bitte bestätigen). Mischkarten: nie aus einer Etappe, in der das Kind heute schon geantwortet hat; offene Ausgabe verfällt sofort bei anderer Antwort (Trigger) und beim nächsten Ausgeben, wenn schon beantwortet oder Etappe heute dran. Mischkarte ohne gültige Ausgabe: `misch {gueltig: false, sterne}`, keine Buchung als Wiederholung (Takt bleibt), als normales Üben wie bisher; gültig: `misch.gueltig: true` + `misch.sterne`. `sterne` = in diesem Aufruf tatsächlich gebucht.
**(2) Nur selbst** (Regel `wdh_nur_selbst` = true): Fortschritt, Wiederholungs-Sterne, Ablegen nur richtig im ersten Versuch ohne Tipp – Runde, freiwillig, Mischkarte. Mit Tipp/zweitem Versuch: `wiederholung {bestanden: false, mit_hilfe: true, naechste_in: 1}`, kein Fehler, am nächsten Lerntag wieder. Dafür zählt eine Mischkarte mit Tipp jetzt als Antwort (richtig + 1, kein Beleg) – sonst bliebe sie in der Runde offen.
**(3) WD-4b:** Etappen einer offenen Tagesrunde ausgenommen (zählen auf den heutigen Platz); von WD-4 schon belegte Folgetage zählen mit; Rückweg nur ohne Zwischenübung (sonst Ablehnung, nichts geändert); kein zweiter Lauf.
**(4) Sollte:** Misch-Fehler für die Reihenfolge erst nach endgültiger Wertung; zwei gleichzeitige Transaktionen über die Antwort-Funktion (lokal: Gerät A „bestanden, Stufe 2“, Gerät B wartet auf die Sperre und bekommt „keine Wiederholung“; genau ein Fortschritt, einmal Sterne); Lerntage statt Kalendertage (Test 1: Sperre ab 18.11. bei heute 22.11. = 3 Lerntage über 4 Kalendertage).

**(5) Lesend, Stand 22.11. (echte Datenbank):** gelandete Etappen mit < 3 frischen Aufgaben (Stufe 2–3): **Kind 1: Einheit 39 „ordnen“ und „zahlengerade“ (0 von 18 frisch); Kind 2: Einheit 5 „waage“ (0 von 18)**. Nach WD-S 3 bekommen diese Etappen die am längsten zurückliegende Aufgabe (nie aus den letzten 3 Lerntagen) – Nachliefern empfohlen. Nach dem Einspielen: `select * from schule.etappen_wenig_frisch();`.
**Gegenprüfung `flug_erstabschluss`:** 5 Einträge, alle stimmig (Sitzung passt, Flug heute fertig, höchstens eine Sitzung mit flug_geschafft).

**Lokal ausgeführt** (Postgres 16, Live-Funktionen byte-gleich inkl. `misch_gueltig`; `uebung_pruefen_intern` als Platzhalter mit echter Auswahl-Wertung, Hilfe/Anlauf/Mischkarte wie live): alle drei Migrationen je zweimal, `wd_s_rauchtest` grün, `wd_s3_rauchtest` grün, Gleichzeitig-Skript grün. Dabei gefunden und behoben: zufällige Aufgabenwahl muss `volatile` sein (sonst wertet Postgres sie doppelt aus).
**Für bau-motivation (0.86.2):** `misch.gueltig`, `misch.sterne`, `wiederholung.mit_hilfe` sind die neuen Felder.

## 2026-11-22 – FERTIG: 0.86.1 – Rückläufer 22.11. abends, Teil C (Cache v157)

Auf `lernen-app` 6ec1c3e. Nur App (`lernen.js`, `style.css`), Version in sechs Dateien, Tests. Nichts in der Datenbank, kein Merge nach `main`.
Bilder: `docs/previews/la/wd-etappe-abgelegt-400.png`, `-1280.png`, `wd-flug-abgelegt-360.png` (360 × 640), `-1280.png`, `wd-reisepass-400.png`.

**1 Test „LM-S 2: Raster … Detail …“ – Ursache: Testdaten, nicht die App.** Der Test nimmt die Verbindungen aus der Vorlage `entwurf/lehrplan-matrix.html`; der Gestalter hat sie am 22.11. neu erzeugt (128 statt 70). Seitdem braucht Thema 22 eine Voraussetzung – und „Eigenständig: braucht keine Voraussetzung …“ steht (richtig) nur bei Themen ohne Voraussetzung; sonst zeigt das Detail die Liste „Braucht vorher“. Behoben: Der Test wählt das eigenständige Thema jetzt aus den Daten (bevorzugt 42, sonst das erste ohne Voraussetzung). Die live laufende Lehrer-Matrix ist davon nicht betroffen. Hinweis zu den Daten (wie N3): Ein Thema mit `eigenstaendig` **und** Voraussetzungen zeigt die Voraussetzungen, die Begründung nicht.

**2 Angleichung an die Vorgabe „abgelegt“** (`inhalte/pruefung/kind/abgelegt/umsetzung.md`, `entwurf/abgelegt.html`)
- **Ansage (1):** im Kasten über dem Startknopf „Vorher kurz einchecken“ · „{n} Bordkarten von früher · etwa {min} Minuten“ (n × 0,5, unter 2 „ganz kurz“) · Koffer-Leiste in Päckchen (bis 6 eins; 7–9 zu 3; 10–12 zu 4). Startknopf „Weiter geht’s ›“. Unterbrochen: „Check-in fortsetzen · Noch 2 von 3 Bordkarten …“, erledigte Koffer grau. „je richtig ★ n“ nur, wenn der Server `sterne_je_richtig` liefert (**Vorschlag an bau-lehrer**: die Zahl aus `sterne_wdh_richtig` mitschicken – ohne Feld lässt die App den Teil weg, weil 5 oder 10 noch offen ist).
- **Check-in (2):** „CHECK-IN · i VON n“, Koffer-Leiste, Sterne-Zähler rechts, „+n“ fliegt (abschaltbar), unter der Bordkarte „{Etappe} · aus {Stadt}“; richtig „Richtig!“ mit „+n ★“ (nur mit `wiederholung.sterne`), Koffer gold mit Stern; falsch „Noch nicht. Richtig ist …“ + „Kein Problem – diese Bordkarte kommt beim nächsten Mal wieder.“, Koffer rötlich, „Zur Etappe“ klein; volles Päckchen hellgelb; „Nächste Bordkarte ›“/„Fertig ›“; dazu „Pause – später weiter einchecken“.
- **Fertig (3):** „Eingecheckt!“, Koffer, „{r} von {n} richtig · +{sterne} ★“ (inkl. 30/100), Fehlersatz bzw. „Alles richtig – super eingecheckt!“, „Weiter nach {Stadt} ›“ ins Thema, „Noch 3 Extra-Bordkarten?“ nur wenn mehr fällig als die Runde (`#/wiederholen/<kind>-extra`, höchstens 3, Kopf „EXTRA · i VON 3“).
- **Etappe abgelegt (4):** Handy Blatt von unten (≤ 72 % Höhe), ab 760 px Karte in der Mitte (≤ 520 px), Bordkarte bleibt abgedunkelt sichtbar; „FÜR IMMER GELERNT“, „Etappe abgelegt!“, Ticket gestrichelt mit Titel und „5-mal wiederholt, über 30 Lerntage. Kommt nicht mehr zum Wiederholen.“, Siegel „FÜR IMMER“ (fällt gedreht), „+30 ★ Sonder-Sterne fürs Ablegen“, Funken; Knopf „Weiter einchecken ›“ im Check-in, sonst „Weiter ›“. Fortschritt des Flugs mit Gold-Leiste **nur, wenn der Server ihn mitschickt** – **Vorschlag an bau-lehrer:** in `abgelegt.etappe` zusätzlich `flug` (Titel), `etappen_abgelegt`, `etappen`. Wird mit derselben Antwort der Flug abgelegt, entfällt das Blatt.
- **Flug abgelegt (5):** ganzer Bildschirm Gold auf Dunkel, Strahlen, „ALLE ETAPPEN FÜR IMMER GELERNT“, „FLUG ABGELEGT!“ in Gold-Schrift, „Alle {n} Etappen von {Flug} sitzen für immer. Im Reisepass ist der Flug jetzt golden.“ (`flug.etappen`, sonst ohne Zahl), aufgeschlagener Pass mit drei Flug-Zeilen (Nachbarn aus den Flügen des Kindes), die Zeile wird golden; Blatt „+100 ★ für den ganzen Flug / +30 ★ für die letzte Etappe“, bei `ort_gold` kleiner Gold-Stempel „Und: Alle Flüge in {Ort} sind abgelegt …“ (`abgelegt.ort` – **bitte mitschicken**, sonst „an diesem Ort“). 360 × 640 ohne Scrollen (Test).
- **Reisepass (6):** Abschnitt „Flüge“ aus `konto.fluege[]` (Ort über `einheit_id`): ganz abgelegt Gold-Verlauf, „★ ABGELEGT“, „{Ort} · alle Etappen für immer gelernt“; teilweise „{a} von {n} abgelegt“ mit Kästchen-Leiste; 0 „noch nichts abgelegt“. Stempel golden „★ GOLD ★“. Satz „Gold heißt: Das sitzt für immer.“ Ohne die Felder bleibt der Reisepass wie bisher.
- Kindertext „Was kommt wann wieder?“ ohne „fällig“, „endgültig“, „Stufe“, „Takt“ und ohne feste Sternzahl (Test). Wartende gesetzte Etappen sieht das Kind nicht mehr (7); im Plan der Eltern bleibt der Zusatz aus 0.85.0 (`wartet`/`kommt_ab_in`, wenn geliefert).

**3 WD-S 2**
- `schule_wiederholung` **ohne `anzahl`**. Pflicht-Bordkarten = `aufgaben[]` mit `pflicht: true` (ohne Feld: die ersten `runde`). Stand „3 von 9“ = `runde` − offene Pflicht-Bordkarten (oder `runde_erledigt`, falls geliefert) – so geht es nach einer Pause und auf einem anderen Gerät an der richtigen Stelle weiter.
- „Runde gemacht“ setzt der Server; die App setzt nichts mehr und schreibt kein `localStorage`. `schule_wiederholung_runde_fertig` ruft sie am Ende nur zum Bestätigen (Fehler werden still ignoriert).
- Keine Rückstandszahl: `faellig` steht nirgends auf der Kinderseite; „Noch k Wiederholungen offen“ ist ersetzt durch „Noch 3 Extra-Bordkarten?“.
- Alter Server (ohne `runde`): liefert ohne `anzahl` nur 3 – die App fragt dann einmal mit `anzahl: 6` nach; sonst alles wie 0.84.0 (Test).

**4 Matrix N1:** Am Rechner (≥ 1100 px) gibt es die Detail-Spalte erst beim Antippen; ohne gewähltes Thema hat die Matrix die volle Breite (Spalten bei 1280 ≈ 130 statt 95 px, Test ≥ 125). Mit geöffnetem Detail bleibt es eng – falls das stört, zusätzlich die Kennzeichen bei gewähltem Kind ausblenden (zweiter Vorschlag der Nachprüfung, nicht gebaut).

**Getestet:** lernen 154 von 154 (neu/ersetzt: Ansage mit Päckchen 6/9/12; Check-in mit Unterbrechen/Fortsetzen, Koffer, Sternen, Extra, 400/820/1280; alter Server; Etappe/Flug abgelegt bei 360×640, 400, 820, 1280; Reisepass; Info und Kindertext; N1; weniger Bewegung). Gesamtlauf: nur die bekannten Reise-Fehler (dazu das datumsabhängige „W80: Jede neue Suche“).
**Nicht geprüft:** echter Server (WD-S 2 noch nicht gebaut), echte Geräte, Safari.

## 2026-11-22 – bau-lehrer – FERTIG: WD-S 2

Auf AUFTRAEGE.md „Rückläufer 22.11. abends“, Teil A (acht Punkte). Nur Dateien, nichts ausgeführt, kein App-Code. Da WD-S nicht eingespielt ist, sind `20261122_wd_s_wiederholungen.sql` und `wd_s_rauchtest.sql` überarbeitet (keine Zusatzdatei). Nacharbeit 907 und `wd_4b_stau_strecken.sql` bleiben unverändert. `sterne_wdh_richtig` bleibt 10.

1. **Prüfregel Sterne:** `sterne_grund_check` wird ersetzt (alle 7 bisherigen Gründe + `wdh`, `etappe_abgelegt`, `flug_abgelegt`). Die Migration vergleicht vorher den Live-Text der Regel (gelesen) und bricht ab, wenn er abweicht. Lokal mit derselben Regel geprüft (vorher: Abbruch wie im Probelauf nachstellbar, nachher grün).
2. **Runde serverseitig:** `schule.wdh_runde` (Tagesziel, fällige beim Festhalten, `fertig_am`) + `schule.wdh_runde_etappe` (zugeordnete Etappen, `bearbeitet_am`). Festgehalten beim ersten Abruf des Lerntags (`schule_wiederholung`); jede Antwort auf eine Etappe der Runde (richtig oder falsch) hakt ab; sind alle abgehakt, setzt der Server `fertig_am` selbst. Etappe ohne verfügbare Aufgabe = bearbeitet; 0 fällige = sofort gemacht. Zweites Gerät bekommt dieselbe Runde; neue Fälligkeiten am selben Tag nur freiwillig. `schule_wiederholung_runde_fertig` bestätigt nur – fehlen Aufgaben: Fehler „Die Wiederholungs-Runde ist noch nicht fertig: x von y bearbeitet“.
   **Antwort `schule_wiederholung` neu:** `runde` (Ziel), `runde_bearbeitet`, `runde_offen`, `runde_gemacht`; `aufgaben[]` = zuerst die noch offenen Etappen der Runde (`pflicht: true`), dann weitere fällige freiwillig. Für die App: „3 von 9“ = `runde_bearbeitet` von `runde`.
3. **Genau ein Fortschritt je Fälligkeit:** nach dem ersten Bestehen ist die Etappe nicht mehr fällig (Zeile gesperrt), der Sterne-Schlüssel je Fälligkeit verhindert eine zweite Buchung; doppelt gesendete Antwort (gleiche `client_id`) wird von der Tabelle abgewiesen. Nicht fällige Mischkarte: nur `misch_ok_am`, kein Fortschritt. Falsche Mischkarte seit Beginn der Fälligkeit zählt in der Reihenfolge als Wiederholungs-Fehler (`schule.wdh_fehler`, ohne den Karten-Stand zu ändern – so öffnet sie weiterhin nie).
4. **Reihenfolge:** mindestens ⌈Runde/3⌉ Pflicht-Plätze für die am längsten fälligen, die übrigen nach Fehler → am längsten fällig → Stufe.
5. **Rückfall nach dem Ablegen:** falsch beim Üben, falsche Mischkarte oder „fehler“ im Nachtest/Test (Trigger auf `lernziel_stand`) → am nächsten Lerntag zurück in den Takt mit Stufe 2; Gold, Sterne, Einblendung bleiben; zweites Ablegen gibt nichts. Kopf: Ablegen an der bestandenen fünften Wiederholung, frühestens 55 Lerntage nach der Landung, nicht an „sicher“ gebunden; `abgelegt` ist ein eigenes Ereignis, nie aus `wdh_stufe` abgeleitet.
6. **Sterne:** letzte Wiederholung = Wiederholungs-Sterne + 30 (+ 100 beim letzten Flug-Teil), je einmal – im Test summiert.
7. **Kopf:** Ziel „Stau schrittweise abbauen, etwa fünf Lerntage bei ausreichender Kapazität – keine Garantie“; Grenze „ohne Bündeln trägt die Kapazität dauerhaft etwa 3 Landungen je Lerntag“.
8. **Tests (`wd_s_rauchtest.sql`, 15 Prüfungen):** Rundengröße; 20/41/60/100 fällige (je eigener Tag: Größe, Pflicht zuerst, ältestes Drittel enthalten, auch mit 50 % Fehlern); Runde ohne Mischkarten, zwei Geräte, Abbruch mitten in der Runde → fortsetzen, Ablehnung vor dem Ende, neue Fälligkeit freiwillig, Server setzt „gemacht“; Tageswechsel, Etappe ohne Aufgabe, 0 fällige; ein Fortschritt/eine Vergütung bei doppelter Antwort und zweitem Gerät; Mischkarten (nicht fällig / falsch / richtig); letzte Stufe mit Sternensumme; Rückfall (Üben, Nachtest), Gold bleibt, zweites Ablegen leer; Konto; Staffelung; Mischkarten-Auswahl; andere Kinder unverändert. `wiederholung_intern`/`wdh_runde_fertig` haben dafür einen Tag-Parameter, den nur der Test nutzt (die api-Funktionen nehmen immer heute_tag).

**Lokal ausgeführt** (Postgres 16, die 20 berührten Live-Funktionen byte-gleich, `sterne_grund_check` und Eindeutigkeit `versuch (lernender_id, client_id)` wie live; Platzhalter u. a. für `uebung_pruefen_intern`, `thema_stufe`, `reiseoptionen`): Migration zweimal, Rauchtest vollständig grün, dazu die api-Kette (Wiederholung → Antwort → Bestätigen).
**Nicht geprüft:** echt gleichzeitige Antworten zweier Geräte (im Test nacheinander; gleichzeitig entscheidet die Zeilensperre in `karte_buchen`/`misch_buchen`).
**Für bau-motivation:** Runde nicht mehr selbst als gemacht setzen; `schule_wiederholung_runde_fertig` nur zum Bestätigen (kann ablehnen); `anzahl` weglassen; `runde_bearbeitet`/`runde` für „x von y“.

## 2026-11-22 – FERTIG: 0.86.0 – LM-6 Kinderseite „Meine Route 5–10“, Cache v156

Auf 0.85.0 (gleicher Zweig). Nur App, Version in sechs Dateien, Tests. Nichts in der Datenbank, kein Merge nach `main`.
Bilder: `docs/previews/la/lm6-route-nacht-400.png`, `lm6-route-tag-400.png`, `lm6-route-nacht-820.png`, `lm6-route-nacht-1280.png` (jeweils mit geöffnetem ▶-Flug).

**Gebaut** (Vorgabe `inhalte/pruefung/lehrer/matrix/umsetzung.md`, LM-6)
- **Zugang:** Textlink „Meine Route 5–10 ›“ auf der Abflugtafel (unter „Erst die Erklärungen ansehen“) und im bisherigen Design unter „Reisepass und Belohnungen ansehen“; neue Seite `#/route/<kind>` (in App und Lern-Seite angemeldet). Der große Knopf bleibt.
- **Nur das eigene Kind:** Lernstand immer an, Schulart fest, keine Leiste, kein Vergleich, keine Kennzeichen „Gym 8 · RS 7“, keine Pflicht-Zählung, kein Lehrplan-Wortlaut, keine Lernbereiche, nichts zum Ändern.
- **Reisewörter:** Überschrift „Deine Route durch die Mathe-Welt“, Spalten = Kontinente (Titel aus `gebiete[]`), Zeilen = Klasse 5–10, je Flug die Stadt klein darunter. Stufen: „◉ kannst du“, „↻ kommt zur Wiederholung“, „▶ hier bist du – Etappe x von y“, „○ kommt noch“; nicht im Plan blass, ohne Text. Beim Öffnen zum ▶-Flug gescrollt. Kopf je Klasse: Balken (◉ ↻ ▶) und „Du kannst schon n von m Flügen“ (m = Flüge der Klasse mit Inhalt, ohne eingeordnete).
- **Detail** (beim Antippen `schule_lehrplan_thema {thema_id, lernender_id}`): „Was du hier lernst“, „Das muss sitzen“, „Das brauchst du vorher“ und „Danach geht’s weiter mit“ – je mit eigener Stufe (Zeichen + Wort), antippbar; „Die Etappen (n)“ mit ✓ für gelandete Etappen (aus dem Merkheft). Beim ▶-Flug großer Knopf „Weiter lernen ›“ (`#/lerneinheit/<kind>-<einheit>-ueben`), sonst kein Lern-Knopf.
- **Verbindungen** wie LM-3 (gelb vorher, blau danach, „→ n“), Linien hinter den Karten.
- **Handy und Tablet zuerst:** unter 1000 px Liste je Klasse nach Kontinent, Detail direkt unter dem Flug, keine Linien (die Kinderseiten sind höchstens 640–760 px breit – acht Spalten passten dort nicht); ab 1000 px Matrix mit Linien, die Seite dafür bis 1240 px breit. Farben der Kinderseiten (Ozean, Nacht, Dschungel, Wüste) über die `--lr-`-Variablen.
- **Daten:** Mit Lern-Zugang liefert LM-S die Kindsicht (`zeile`, `reihenfolge_kind`). Öffnen Eltern die Seite des Kindes, liefert der Server die Lehrer-Sicht – dann rechnet die App die Zeile aus `jahrgang` und der Schulart des Kindes (wie `schule.thema_klasse_fuer`) und zeigt nur dieses Kind. Aufruf mit `mit_testkind: true`, damit auch das Testkind seine Route sieht. Ohne LM-S (alter Server): „Die Route ist bald da.“
- **Info-Seite:** nicht geändert (die Kinderseite erklärt sich mit Einleitung und Legende). Wenn gewünscht, Satz für die Eltern liefern.

**Getestet** (lernen 151, neu 4): Link auf der Abflugtafel, alle Flüge, keine Kennzeichen/Leiste/Knöpfe, Stufen-Texte, Scrollen zum ▶, Kopf je Klasse, Kontinente als Spalten, Reisewörter (keine „Thema/Lehrplan/Gymnasium/Pflicht/Aufgabe“); Detail mit Voraussetzungen (eigene Stufe), Nachfolgern, Linien, Etappen-✓, „Weiter lernen ›“ nur beim ▶-Flug, kein Wortlaut, keine Begründung; Abnahme 400/820/1280 in Nacht und Tag (nichts läuft über, kein Wort ohne Trennstrich gebrochen, kein Querrollen, Liste mit Detail unter dem Flug bzw. Matrix mit Linien); Lehrer-Sicht (Zeile aus jahrgang, kein Geschwister) und alter Server. Suche: nur die bekannten Reise-Fehler.

**Nicht geprüft:** gegen den echten LM-S-Server (Kindsicht über den Lern-Zugang), echte Geräte.

## 2026-11-22 – FERTIG: 0.85.0 – Wiederholungen dynamisch (WD, App-Teil), Cache v155

Auf `lernen-app` 986d43e. Gebaut gegen die Schnittstelle im „Nachtrag zum Bau-Auftrag WD“. Nur App (`lernen.js`, `style.css`), Version in sechs Dateien, Tests. Nichts in der Datenbank, keine Kinderdaten, kein Merge nach `main`. Den Server habe ich nicht gesehen (`bau-lehrer` hat noch keinen WD-Stand) – getestet gegen nachgebildete Antworten.
Bilder: `docs/previews/la/wd-etappe-abgelegt-400.png`, `wd-flug-abgelegt-400.png`, `wd-flug-abgelegt-1280.png`, `wd-reisepass-400.png`.

**Gebaut**
- **WD-1 Runde:** `schule_wiederholung` wird mit `anzahl: 12` aufgerufen (der alte Server begrenzt selbst auf 6 – `least(anzahl, 6)` –, also kein Unterschied). Liefert der Server `runde`, sind die ersten `runde` Bordkarten aus `aufgaben[]` die Pflicht-Runde (Reihenfolge vom Server): Startknopf „Erst n Wiederholungen ›“, Kopf „WIEDERHOLEN i VON n“. Danach „Noch k Wiederholungen offen – wenn du magst“ (k = `faellig` − Runde); freiwillige heißen „FREIWILLIG WIEDERHOLEN“.
- **WD-2 Merker:** Mit `runde` gilt nur noch `runde_gemacht` vom Server, `localStorage` wird dann weder gelesen noch geschrieben. Am Ende der Pflicht-Runde ruft die App `schule_wiederholung_runde_fertig {lernender_id}` (scheitert der Aufruf, merkt sich das Gerät die Runde wie bisher).
- **WD-4 Staffelung:** `gestaffelt` > 0 → auf der Abflugtafel (beide Designs) und am Ende der Runde: „n Etappen warten noch auf die erste Wiederholung – sie kommen ab dem nächsten Lerntag nach und nach dazu.“ Ein Datum „kommt ab …“ je Etappe liefert die Schnittstelle nicht – **Vorschlag (optional, nicht verbindlich):** im Plan je Flug in `thema_stufe` `wartet` (Zahl) und `kommt_ab_in` (Lerntage); die App zeigt dann im Plan „3 Etappen warten · kommt ab in 2 Lerntagen“ (ist schon eingebaut, ohne die Felder unsichtbar). Ebenso `etappen_abgelegt` → „2 von 7 abgelegt“.
- **WD-5 Sterne:** `wiederholung.sterne` erscheint als „Richtig! · +5 Sterne“, darunter „Nächste Wiederholung in n Lerntagen“ (`naechste_in`), am Ende „★ +n Sterne“. Die App rechnet nichts selbst – sie zeigt, was der Server meldet.
- **WD-3 Mischkarte:** Bei `wiederholung.bestanden` steht unter „✓ An Bord“ „↻ Zählt als Wiederholung dieser Etappe“; die Sterne-Zeile zeigt 10 (Mischkarte, wie heute) **plus** `wiederholung.sterne`. Entscheidet Sebastian anders (nur 5 oder nur 10), bitte entsprechend buchen und `wiederholung.sterne` 0 bzw. die Differenz melden – die App zeigt genau das.
- **WD-6 Einblendungen** (aus `abgelegt` in `schule_uebung_pruefen`, nach einer Wiederholung oder Mischkarte): „Etappe abgelegt“ klein – goldene Karte über der Seite (★-Siegel, Titel der Etappe, Satz, „★ +30“, „Weiter“); danach, falls `flug`, „Flug abgelegt“ groß – Vollbild im Stil von „Flug geschafft“, in Gold (Konfetti, Zähler 100 ★, Siegel, „Im Reisepass: Dein Flug ist jetzt golden.“, bei `ort_gold` „Alle Flüge dieses Orts sind abgelegt – dein Stempel ist jetzt golden.“, „Weiter“, „Reisepass ansehen“). Gestalter-Vorgabe gab es noch nicht – bitte nachprüfen, ich gleiche an.
- **Gold im Reisepass:** `konto.orte[].gold` → Stempel golden mit „★ GOLD“. Flüge: neuer Abschnitt „Abgelegt“ (nur wenn etwas abgelegt ist) mit dem Eintrag je Flug, golden bei `abgelegt`, sonst „1 von 2 Etappen abgelegt“. Bisher gab es im Reisepass keinen Eintrag je Flug – das ist der „Eintrag des Flugs“. **Erwartetes Format:** `konto.fluege[] { block_id, titel, abgelegt, etappen_abgelegt, etappen }` oder dieselben Felder in `konto.orte[].fluege[]` (beides gelesen) – bitte so liefern oder melden.
- **Info-Seite:** Wiederholung (Rundengröße, ein Mal je Lerntag auch beim Gerätewechsel), neuer Eintrag „Endgültig abgelegt“, Mischkarten (zählen als Wiederholung), Belohnungen (5 / 30 / 100), Plan („Kann er – aber wiederholen“: höchstens 6 je Lerntag neu in den Takt). „Was kommt wann wieder?“ (Kind) mit Runde und Sternen nur, wenn der Server `runde` liefert. Die Info-Texte beschreiben WD – **erst mit dem Server live schalten.**
- **Alter Server:** ohne `runde` alles wie 0.84.0 (höchstens 6, Merker auf dem Gerät, kein `runde_fertig`, keine neuen Zeilen) – eigener Test.

**Getestet** (lernen 147, neu 6): Runde in Server-Größe und Server-Merker (Gerät sagt „gemacht“, Server nicht → Server gilt; umgekehrt auch), runde_fertig, freiwillig, wartende Etappen, 400/820/1280 ohne Querrollen; alter Server; 5 Sterne, „Etappe abgelegt“ (klein, 400/820/1280, keine gebrochenen Wörter) und „Flug abgelegt“ (Vollbild, Zähler 100, Stempel golden); Mischkarte als Wiederholung; Reisepass golden (400/820/1280) und ohne Felder unverändert; Info-Texte. Die bekannten Fehler der Reise-Tests unverändert.

**Nicht geprüft:** echter Server, echte Geräte; Animation nur in Chromium.

## 2026-11-22 – bau-lehrer – FERTIG: Nacharbeit 907

Auf AUFTRAEGE.md „Nacharbeit aus ChatGPTs Prüfergebnis 907“, Teil bau-lehrer. Neue Dateien; die eingespielten Migrationen bleiben unverändert. Nichts in der echten Datenbank ausgeführt.
- `supabase/migrations/20261122_nacharbeit_907.sql`:
  - **Kopf dokumentiert** den Altzustand „früher fertiger Flug (Sitzung NULL oder durch Lesen false) → neue Pflicht-Etappe → erst dann Nachtrag → Nachtragstest“: festgelegtes Ergebnis **flug_geschafft = true** (zweites „Flug geschafft“); beim Einspielen im Bestand ausgeschlossen (Haupt-Chat: 4 von 4 Flügen mit Test fertig, Pflichtlisten vollständig); neue Fälle entstehen nicht. Ebenso festgehalten: erneutes Lesen derselben erfolgreichen Sitzung zeigt wieder true (gewollt).
  - `schule.flug_erstabschluss_nachtragen`: `sitzung_id` und `am` aus **derselben, zeitlich ersten** Sitzung (`order by abgeschlossen_am, id`).
  - LM-S: `etappe_jetzt` = Nummer der ersten noch nicht gelandeten Etappe in Etappen-Reihenfolge (neue Funktion `schule.etappe_jetzt`); fehlt, wenn alle gelandet sind. Umbau von `schule.lehrplan_matrix` an genau einer Stelle (live genau einmal vorhanden, gelesen).
- `supabase/tests/ab_s_nacharbeit_907_rauchtest.sql`: der Altzustand in beiden Formen (NULL / vorher gelesen) → Nachtrag danach → Nachtragstest = true, erneutes Lesen wieder true; Nachtrag mit gegenläufigen ids/Zeiten → beide Werte aus der zeitlich ersten Sitzung.
- `supabase/tests/lm_s_nacharbeit_907_rauchtest.sql`: Lern-Zugang des Testkinds und ein Eltern-Zugang, beide im Test angelegt (Name „Rauchtest“, Zufalls-Hash, Rollback – kein echter Schlüssel): fremde `lernender_id`, `mit_testkind: true`, Detail als Kind, Eltern = Lehrer-Sicht, gesperrter Zugang und abgelaufene Sitzung abgewiesen („Nicht angemeldet“), Größe mit `octet_length` (Raster < 90 000 Bytes, Detail < 30 000), `etappe_jetzt` (2 / keine / 1) und im Raster stimmig.
- `supabase/tests/lm_s_lehrplan_matrix_rauchtest.sql` Prüfung 4 angepasst (etappe_jetzt nur bei „dran“, kann jetzt fehlen) – sonst würde der alte Test nach der Nacharbeit fälschlich abbrechen.
- **Lokal ausgeführt** (Postgres 16): `test_abschliessen_intern`, `lehrplan_matrix`, `flug_erstabschluss_nachtragen` byte-gleich zum Live-Stand (md5 gleich), Zugangsfunktionen (`lern_ich`, `ist_leiter`, `wer_tn`, `sieht`, `zugriff`) wie live; Migration zweimal, beide neuen Tests grün, alter LM-S-Test grün. Gegenprobe: mit dem alten Nachtrag schlägt Prüfung 2 fehl.

## 2026-11-22 – bau-lehrer – FERTIG: WD-S

Bau-Auftrag WD (Server) nach der Schnittstelle im Nachtrag. Nur Dateien, in der echten Datenbank nichts ausgeführt, kein App-Code, kein Merge nach main, keine Kinderdaten.

**Sterne heute (Live-Text gelesen 22.11.) – Meldung vor dem Bau:**
- Jede richtige Antwort außerhalb eines Tests – auch mit Tipp oder im 2. Anlauf, auch eine Wiederholung oder Mischkarte – gibt `sterne_uebung_richtig` = **10 Sterne**, aber **je Aufgabe nur einmal** (Schlüssel `uebung` + `aufgabe:<id>`). Die Wiederholungs-Runde wählt bevorzugt ungesehene Aufgaben → eine richtige Wiederholung gibt heute meist 10, sonst 0. Mischkarte genauso.
- Also: **Ja, eine richtige Wiederholung gibt heute schon 10.** Nicht gekürzt: `sterne_wdh_richtig` steht in der Migration auf **10** (Schnittstelle: 5). **Sebastian entscheidet 5 oder 10** – Umstellen ohne Bau: `update schule.regel set wert = '5' where schluessel = 'sterne_wdh_richtig'`.
- Neu gilt: je bestandener Wiederholung (Runde, freiwillig, Mischkarte nach WD-3) einmal je Etappe und Fälligkeit `sterne_wdh_richtig`; für denselben Versuch dann keine `uebung`-Sterne (nichts doppelt). Die `uebung`-Sterne dieser Aufgabe bleiben für später übrig.

**Dateien**
- `supabase/migrations/20261122_wd_s_wiederholungen.sql` – WD-1 bis WD-6 (Regeln, Tabellen `schule.wdh_runde`, `schule.abgelegt`, Trigger `karte_wdh_ereignis`, Umbauten an genau bezeichneten Stellen). Prüft am Ende: Karten, Lernstände, Plan, Sterne vorher = nachher, sonst Abbruch. In einer Transaktion einspielen.
- `supabase/migrations/20261122_wd_4b_stau_strecken.sql` – **eigene Datei, erst nach Probelauf und Sebastians Okay**: streckt einmalig gesetzte, heute fällige Etappen auf Stufe 0 (je Kind 6 je Lerntag); nur `faellig_am`, `wdh_ab`, `wdh_lerntage`; alte Werte in `schule.wdh_staffel_sicherung` (Rückweg im Kopf der Datei); prüft, dass sich sonst nichts ändert. Nur gelesen nachgerechnet: Kind 2 hat 34 solche Etappen → heute 6, dann 6/6/6/6/4 an den nächsten 5 Lerntagen; heute fällig 42 → 14 (die 8 übrigen sind natürlich gelandet oder mit Fehler und bleiben).
- `supabase/tests/wd_s_rauchtest.sql` – Rollback, nur Testkind; Prüfungen 1–9 (s. u.), 10: Karten, Lernstände, Plan, Sterne, Stufen (`thema_stufe`) und Reiseoptionen aller anderen Kinder vorher = nachher.
- `supabase/functions/lernen-api/index.ts`: Aktion `schule_wiederholung_runde_fertig: ['lernender_id']`, VERSION 0.9.0.

**Schnittstelle (wie im Nachtrag; Abweichungen fett)**
- `schule_wiederholung`: bisher `aufgaben`, `faellig`; neu `runde`, `runde_gemacht`, `gestaffelt`; `aufgaben[]` in WD-1-Reihenfolge (Wiederholungs-Fehler → am längsten fällig (`faellig_am`) → niedrigste Stufe), je Aufgabe zusätzlich **`pflicht`** (die ersten `runde`), `lernziel`, `wdh_stufe`. **`anzahl`** = höchstens so viele Aufgaben, Obergrenze jetzt 60 statt 6; ohne `anzahl` alle fälligen (≤ 60). Die App 0.84 schickt `anzahl: 6` → bekommt wie bisher 6 (jetzt in WD-1-Reihenfolge). Die neue App sollte `anzahl` weglassen.
- `schule_wiederholung_runde_fertig {lernender_id}` → `{ok, runde_gemacht: true, tag}`; Merker je Kind und `heute_tag`, zweimal setzen geht.
- `schule_uebung_pruefen`: bei Antwort auf eine **fällige** Etappe (auch Mischkarte) `wiederholung {bestanden, sterne, stufe_neu, naechste_in}`; bei Ablegen `abgelegt {etappe {titel, sterne}, flug? {titel, sterne}, ort_gold?}` – je Kind und Etappe/Flug/Ort einmal. `naechste_in` in Lerntagen; fehlt nach dem Ablegen.
- `schule_konto`: `konto.fluege[] {thema_id, einheit_id, titel, abgelegt, etappen_abgelegt, etappen}` (Flüge mit Karten), `konto.orte[].gold`.
- `gestaffelt` = gesetzte Etappen auf Stufe 0, die noch warten (erste Wiederholung später als in 1 Lerntag). „Kommt ab …“: `naechste_in` der Karte wie bisher.
- Mischkarten-Liste (`schule.mischkarten`): fällige zuerst; jede Karte aus der Auswahl trägt **`faellig`**.

**Regeln im Detail**
- WD-1: bis 6 fällige alle; sonst ⌈fällige/5⌉, mindestens 6, höchstens 12 (bis Kl. 6: 10). Regeln `wdh_runde_min/max/max_bis_kl6/teiler`.
- WD-3: Mischkarte aus fälliger Etappe, richtig ohne Tipp im 1. Versuch → wie eine richtige Wiederholung (Stufe +1, Takt 1/3/7/14/30), Beleg `misch_ok_am` wie bisher. Falsch → wie heute fällig, öffnet nie. Häufigkeit unverändert. Eine normale Wiederholung zählt wie heute auch mit Tipp/2. Anlauf als bestanden (Regel von `karte_buchen`, nicht geändert).
- WD-4: `flug_wdh_setzen` gibt jeder Etappe den ersten Lerntag mit freiem Platz (je Kind höchstens `wdh_gesetzt_je_lerntag` = 6 erste Wiederholungen je Lerntag), in Aufruf-Reihenfolge (Plan-Reihenfolge aus `plan_setzen_intern`, im Flug die Etappen-Reihenfolge).
- WD-6: „letzte Wiederholung“ = die Wiederholung auf Stufe 4 (30 Lerntage) bestanden → abgelegt: keine Fälligkeit mehr, 30 Sterne. **Flug abgelegt = alle Pflicht-Etappen abgelegt** (ohne Pflichtliste: alle Etappen) → 100 Sterne. Ort golden = alle Flüge mit Inhalt im Ort abgelegt (keine Sterne – die Schnittstelle nennt keine). Fällt eine abgelegte Etappe später auf (falsch beim Üben oder falsche Mischkarte), kommt sie wie heute für alle gelandeten Etappen am nächsten Lerntag zurück; Gold und Sterne bleiben, ein zweites Ablegen gibt nichts.

**Wirklich ausgeführt – lokal** (Postgres 16, Wegwerf-Datenbank): die 20 berührten Live-Funktionen **byte-gleich** (md5 je Funktion gleich), Platzhalter nur für `uebung_pruefen_intern` (speichert den Versuch wie live), `konto`, `thema_stufe`, `reiseoptionen` und Inhalts-Hilfen. Migration zweimal; Rauchtest 1–10 grün: Rundengröße (0/5/6/7/20/41/60/100 → 0/5/6/6/6/9/12/12, Kl. 6: 60 → 10), Reihenfolge und `pflicht`, Merker, bestandene Wiederholung (Stufe 2 → 3, Sterne einmal, keine `uebung`-Sterne), Mischkarte falsch/richtig, Ablegen Etappe/Flug (je einmal), Konto, Staffelung (Regel testweise 2: 14 Etappen → 2 je Lerntag), Mischkarten-Auswahl fällige zuerst, andere Kinder unverändert. Dazu `api.schule_uebung_pruefen` / `schule_wiederholung` / `_runde_fertig` / `schule_konto` mit Platzhalter-Zugang. WD-4b lokal: 14 → 6/6/2, zweiter Lauf ändert nichts.

**Vorschläge**
1. **„sicher“ (◉) gegenüber „abgelegt“:** Heute heißt ◉ „Stufe 4 erreicht und belegt (Mischkarte oder Nachtest)“ – also *vor* der letzten 30-Tage-Wiederholung. Vorschlag: auf der Kinderseite ◉ nicht mehr als eigenen Zustand zeigen, sondern die Stufe als „Wiederholung x von 5“ und am Ende nur Gold (abgelegt). Für Eltern/Lehrer bleibt „sicher“ als Beleg-Hinweis. Auf dem Server bleibt `karte_sicher` unverändert (Nachtest-Logik hängt daran). Alternative (nicht empfohlen, verzögert das Gold): Ablegen erst, wenn zusätzlich „sicher“.
2. **Nachtest nach dem Ablegen:** Heute ändert ein Nachtest den Karten-Takt nicht (er setzt nur die Etappe im Flug auf „fehler“ → Verbessern). Vorschlag wie im Auftrag: fällt eine abgelegte Etappe im Nachtest durch, kommt sie **einmalig mit 7 Lerntagen** (Stufe 2) zurück in den Takt; Gold, Sterne und Einblendung bleiben, ein erneutes Ablegen gibt nichts. **Nicht gebaut** – braucht eine Stelle in `test_abschliessen_intern`; auf Sebastians Okay als eigene kleine Datei.

## 2026-11-21 – FERTIG: 0.84.0 b – Matrix an LM-S 2 angepasst, Filter „Inhalt“, Info-Texte (Version bleibt 0.84.0, Cache v154)

Auf AUFTRAEGE.md „Rückläufer 21.11. morgens“, Teil D. Stand `lernen-app` d463182 übernommen. Nur App (`lernen.js`, `style.css`) und Tests. Nichts in der Datenbank, keine Kinderdaten, kein Merge nach `main`.
Bilder neu: `docs/previews/la/lm-oben-400/820/1280.png` (mit Filterzeile), `lm-matrix-*.png`.

**Datenformat LM-S 2** (Feldliste „FERTIG: LM-S 2“)
- Raster aus `schule_lehrplan_matrix`: Gebiet-Titel über `gebiet_id` aus `gebiete[]` (Spaltenreihenfolge = `reihenfolge`); `verbindungen[]` als Tripel `[thema_id, braucht_id, "h"|"e"]` (Objekte gehen weiter); `etappen_anzahl` → „Etappe x von y“ (y = `etappen_anzahl`, x = `etappe_jetzt`) und „Inhalte ansehen (n Etappen)“; `ohne_flug` blass; `eigenstaendig: true`. Fehlendes `fehler_offen` = nein (kein „Fehler besprechen ›“).
- Detail über die eigene Aktion **`schule_lehrplan_thema { thema_id }`** beim Antippen, einmal je Thema: `kurz, ort, was_gefordert, merke, etappen (pflicht → „· freiwillig“), beispiel, braucht/baut_darauf (Begründungen an den Verbindungen), lehrplan, eigenstaendig` (Text: „Eigenständig: braucht keine Voraussetzung – ‹Begründung›“). Bis die Antwort da ist: „Einzelheiten werden geladen …“; bei Fehler bleibt das Raster-Detail.
- Weiter parallel `schule_lehrplan_uebersicht` für Ort, Kurzbeschreibung im Raster, Inhaltsstand (◐ in Prüfung) und Aufträge. Ohne LM-S trägt die Übersicht allein (wie bisher).

**Filter „Inhalt“ (was fehlt noch?)** – eigene Zeile über dem Lernstand: „Alle · ● fertig n · ◐ in Prüfung n · ○ fehlt n“ (Zähler über alle Themen). Nicht passende Themen werden blass (wie bei der Suche, beides kombinierbar); Themen ohne Flug zählen nirgends mit. Im Detail weiter Inhaltsstand, „Inhalte ansehen“, Aufträge und „✎ Ändern lassen“.

**Info-Seite – Vorschlag zum Prüfen (umgesetzt):**
- „Wie entstehen die Inhalte …“, letzter Satz statt „Die Lehrplan-Übersicht … Eine Zeile antippen öffnet ‚Inhalte ansehen‘.“: „Der Lehrplan (Nachschlagen auf der Startseite) zeigt alle Flüge als Übersicht: Zeilen Klasse 5–10, Spalten die Themengebiete, eingeordnet nach Gymnasium, Realschule oder IB, in der Reihenfolge des Lehrplans. Der Filter „Inhalt“ zeigt, was fertig ist (●), was in Prüfung ist (◐) und was noch fehlt (○). Ein Thema antippen: was gefordert ist, was es vorher braucht, worauf es aufbaut, Lernbereich und „Inhalte ansehen“. Mit „Lernstand“ steht bei jedem Thema die Stufe eines Kindes (◉ ↻ ▶ ○ +) – ist ein Kind gewählt, lässt sich der Plan dort direkt ändern.“
- Lehrplan-Grundlage: „… Die Lehrplan-Übersicht zeigt alle Flüge.“ → „… Der Lehrplan (Nachschlagen auf der Startseite) zeigt alle Flüge auf einer Seite: Klasse 5 bis 10 und alle Themengebiete.“
- „Ändern lassen“: „Für Flüge ohne Inhalt steht er im Lehrplan, wenn man das Thema antippt, mit „Neuer Flug“ vorbelegt.“
- Expeditionen: „Alle Expeditionen mit Lösungen: Lehrplan → „Expeditionen ansehen“.“
- Erste Schritte, Schritt 3: „Im Lehrplan ein Thema antippen, dann „Inhalte ansehen“: …“, Link „Lehrplan ›“.
- Die Gliederung nach Lernbereich fällt im Text weg (Lernbereich steht im Detail). Test „LB Teil 7“ prüft den neuen Satz und dass „Lehrplan-Übersicht“ nicht mehr vorkommt.

**Gesehen/getestet**
- lernen: 141 Tests; im Gesamtlauf 140 bestanden, „LB Teil 8: aufgeklappte Karte“ wackelt unter Last (einzeln zweimal bestanden, wie schon in 0.84.0). Neu/ersetzt: „LM-S 2“ (Raster mit Tripeln, gebiet_id, etappen_anzahl, Detail über schule_lehrplan_thema mit Begründungen, eigenständig, freiwillig, fehler_offen, ohne Flug, Testkind) und „LM: Filter Inhalt“ (Zähler, blass, mit Suche, 400/820 ohne gebrochene Wörter und Querrollen). Testdaten: echte Themenliste, Verbindungen aus der Vorlage, Lernstand erfunden.
- Suche: die bekannten alten Fehler (PWA-Hülle, Startkarte, W80 ×4, Review301, Woanders gebucht, W88).

**Nicht geprüft / Hinweise**
- Gegen den echten LM-S-Server nicht getestet (LM-S 3 behebt erst den Abbruch der Migration). Die App fällt ohne LM-S auf die Übersicht zurück.
- `schule_lehrplan_thema` rufe ich ohne `lernender_id` auf (Eltern/Lehrer-Sicht).

## 2026-11-21 – bau-lehrer – FERTIG: flug_erstabschluss

Auf AUFTRAEGE.md „Rückläufer 21.11. morgens“, Teil C. Nur Dateien, in der echten Datenbank nichts ausgeführt, kein App-Code.
- `supabase/migrations/20261121_ab_s_flug_geschafft_robust.sql` **ersetzt** (der Entwurf mit `flug_fertig_nach` war nie eingespielt; die Funktion kommt nicht mehr vor):
  - Tabelle `schule.flug_erstabschluss (lernender_id, einheit_id, sitzung_id, am, primary key (lernender_id, einheit_id))`, RLS an, keine Rechte für public/anon/authenticated.
  - `schule.flug_erstabschluss_nachtragen(p_l default null)`: trägt alle Flüge ein, die jetzt fertig sind (alle Pflicht-Etappen nachgewiesen/korrigiert/gesichert), und alle mit abgeschlossener Flug-Test-/Verbessern-Sitzung mit `flug_geschafft = true` (`sitzung_id` = früheste solche, sonst null). Die Migration ruft sie einmal auf (NOTICE mit Anzahl); wiederholt: 0.
  - `test_abschliessen_intern`: die Stelle aus 20261120 wird ersetzt. Neu: `flug_geschafft` = dieser Aufruf schließt ab (blocktest/korrektur), Flug danach fertig, vorher nicht, **und** `insert … on conflict do nothing` hat eine Zeile angelegt (`found`). War der Flug vorher schon fertig, wird er nur festgehalten (`sitzung_id` null), `flug_geschafft` false. Die Stelle steht live genau einmal (gelesen).
- `supabase/tests/ab_s_abschluss_rauchtest.sql`: Prüfung 9 als eigener Block, die alten Sitzungen legt der Test selbst an:
  9a alter bestandener Flug + neue Pflicht-Etappe + Nachtragstest → false · 9b alte Sitzung vorher erneut gelesen → false (sperrt nichts) · 9c alter nicht bestandener Test + Verbessern → true mit Abschluss-Feldern, Eintrag mit dieser Sitzung · 9d zweimal abschließen (dieselbe Sitzung erneut + zweites Verbessern) → genau eine Sitzung mit true, ein Eintrag · 9e Nachtest → false.
- **Wirklich ausgeführt – lokal** (Postgres 16, eigene Wegwerf-Datenbank, erfundene Inhalte): `test_abschliessen_intern` lokal **byte-gleich zum Live-Stand** (md5 432e041a… gleich), Migration zweimal, Prüfung 9 grün; Gegenprobe mit der alten Funktion: 9c schlägt fehl (der Test unterscheidet). Nachtrag geprüft (fertig → null, true-Sitzung → deren id, nur Vertiefung → kein Eintrag, zweiter Lauf 0). Platzhalter lokal: `ort_stand`, `flug_abschluss`, `nachtest_*`, `thema_stand`.
- Gleichzeitige Sitzungen: entscheidet der Primärschlüssel (die zweite wartet auf die erste und legt nichts an) – lokal nicht nebenläufig getestet.

## 2026-11-21 – bau-lehrer – FERTIG: LM-S 3

Auf „Rückläufer 21.11. morgens“, Teil B. Ursache: in `schule.lehrplan_thema` (Feld `etappen`) eine Klammer zu viel vor `order by`. pglast prüft den Funktionsrumpf nicht – darum nicht aufgefallen.
- `supabase/migrations/20261121_lm_s_lehrplan_matrix.sql` behoben (md5 vorher 544f48ff…, jetzt 976e974e…).
- **Wirklich ausgeführt – lokal** (Postgres 16, Wegwerf-Datenbank): Tabellen mit den Live-Spalten (gelesen), `thema_einheit`/`thema_jahrgang` wie live, Platzhalter für `thema_stufe` und die Zugangsfunktionen, erfundene Inhalte und Kinder. Den Fehler „mismatched parentheses“ lokal nachgestellt, nach der Korrektur: Migration läuft (auch zweimal), Rauchtest ohne Spalte `eigenstaendig` grün (9 übersprungen), mit Spalte (Text) grün inkl. 9. Zusätzlich beide api-Aktionen mit Lehrer-, Kind- und fremdem Schlüssel: Kind bekommt nur sich selbst (fremde `lernender_id` wird ignoriert), fremder Zugang → „Kein Zugriff“, ohne `thema_id` → „thema_id fehlt“, Physik-Thema → „Thema nicht gefunden“.
- Rauchtest 8 nimmt jetzt ein Thema mit Pflicht-Etappen (vorher konnte es eines ohne merke/Etappen treffen).
- Feldliste unverändert (Eintrag „LM-S 2“).

## 2026-11-21 – FERTIG: 0.84.0 – Lehrplan-Matrix LM-1 bis LM-5 (Eltern/Lehrer), Cache v154

Stand `lernen-app` 168a744 übernommen (mit LM-S und Runde 30). Nur App (`lernen.js`, `style.css`), Version in sechs Dateien, Tests. Nichts in der Datenbank, keine Kinderdaten, keine Schlüssel, kein Merge nach `main`.
Bilder: `docs/previews/la/lm-oben-400.png`, `lm-oben-820.png`, `lm-oben-1280.png` (Kopf, Kind A gewählt), `lm-matrix-400/820/1280.png` (Thema mit Verbindungen und Detail), `lm-plan-link-400.png`.

**Gebaut**
- **LM-1:** Nachschlagen → „Lehrplan“ (`#/lehrplan`) ist jetzt die Matrix „Mathe Klasse 5–10: was gelernt wird“. Zeilen Kl. 5–10 in den Klassenfarben (LA-8), Spalten die Themengebiete inkl. Entdecker-Inseln (Reihenfolge aus `gebiete[]`, sonst wie die Vorlage); Schalter „Klassen als Zeilen / als Spalten“ (gemerkt). Alle Themen. „Einordnen nach“ Gymnasium · Realschule · IB MYP bestimmt die Zeile; fehlt die Schulart: andere bayerische Schulart, sonst MYP-Jahr + 5 → gestrichelt, mit Marke (RS/Gym/IB/Insel) und Erklärung im Detail. Kennzeichen „Gym 8 · RS 7 · IB 4“ (gewählte dunkel, fehlende durchgestrichen, orange wenn es die gewählte ist). Zelle in Lehrplan-Reihenfolge der Schulart. Kopf je Zeile „n Themen“ / „m Gym‑Pflicht“ (mit LM-S: `pflicht[]`). Suche, „Kurzbeschreibung“ (gemerkt). Unter 760 px Liste je Klasse nach Gebiet, Detail direkt unter dem Thema.
- **LM-2 Detail:** Titel, Gebiet, Klassen je Schulart, Lernbereich; Inhalt (● fertig, ◐ in Prüfung, ○ fehlt) mit „Inhalte ansehen (n Etappen) ›“, Aufträge-Link, Ort, „✎ Ändern lassen“ bei fehlendem Inhalt (aus LB-1); Was gefordert ist; Braucht vorher (Begründung, Klasse, „empfohlen“); Weiter zurück auf dem Weg; Darauf baut auf; Das muss sitzen; Beispielaufgabe; Schritte in der App (nicht-Pflicht-Etappen „· freiwillig“); Im Lehrplan (Wortlaut); ‹ › blättern. Ohne Voraussetzung: „Keine Voraussetzung hinterlegt …“; mit `eigenstaendig` „Eigenständig: braucht keine Voraussetzung – ‹Begründung›“. Liefert der Server keine Verbindungen (heute live), steht dort ehrlich „Die Verbindungen … liefert der Server noch nicht“.
- **LM-3:** gewählt → direkte Voraussetzungen gelb mit Linie, weiter zurück hellgelb, darauf aufbauend blau mit Linie, Rest blass, „empfohlen“ gestrichelt, „→ n“ ab 2 Nachfolgern. Linien als SVG **hinter** den Karten (z-index 1 < 2, im Test per `elementFromPoint` geprüft); Handy ohne Linien.
- **LM-4:** Leiste „Lernstand: Aus · Kind A · Kind B · Beide vergleichen“ (bei mehr Kindern „Alle vergleichen“); ein Kind: Hintergrund je Stufe **in den Farben des Plans** (LB), „▶ Etappe x von y · hier ist ‹Name›“ (`etappe_jetzt`), „↻ Wdh n von 5“, „+ nicht im Plan“ gestrichelt/blass; beim Einschalten zum ▶-Thema gescrollt; Schulart springt auf die des Kindes. Vergleich: „A/B“ mit zwei Punkten in Stufenfarbe. Kopf je Klasse: Balken je Kind (◉ ↻ ▶) über die Pflichtthemen. Detail: Lernstand je Kind (Stufe, Zusatz wie im Plan, nächste Wiederholung) mit „Im Plan öffnen ›“ und „Fehler besprechen ›“ (nur bei `fehler_offen`; ohne LM-S bei `wieder_offen`) → Reiter „Was wackelt“ des Kindes.
- **LM-5:** Im Detail bei genau einem Kind die Stufen-Knöpfe aus LB Teil 8 (Lernen · Kann er – wiederholen · Kann er komplett, rechts „Aus dem Plan nehmen“/„In den Plan nehmen“, bei ◉ „Wieder in die Wiederholung“). Dafür ist der Plan-Kern aus `viewPlan` herausgelöst (`lernPlanSetzeIn`, `lernPlanEintraege`, …) – **dieselben Aufrufe** (`schule_plan_lesen`, `schule_plan_setzen` mit revision, Rückgängig mit `schritt_id`, Konflikt sperrt mit „Neu laden“). Nach dem Speichern werden die Stufen neu geholt. „Im Plan öffnen ›“ springt in den Reiter „Plan“: Flug im Plan → Ort links aufgeklappt und markiert; sonst rechts „Nach Klasse“ mit dem Flug aufgeklappt. Reiter „Plan“: Link „Als Matrix ansehen ›“ rechts in der Reiterzeile (Handy: darunter), öffnet `#/lehrplan/<kind>` mit Kind und Schulart; kein fünfter Reiter.

**Daten (LM-S)**
- Die App ruft `schule_lehrplan_matrix` **und** `schule_lehrplan_uebersicht` parallel: die Matrix-Daten tragen, die Übersicht liefert Inhaltsstand (◐ in Prüfung) und Aufträge je Flug, die LM-S nicht hat. Kennt der Server `schule_lehrplan_matrix` noch nicht (heute live), trägt die Übersicht allein – alles läuft, nur ohne Verbindungen, Das muss sitzen, Beispiel, Pflicht-Etappen.
- Aus dem Plan eines Kindes, das nicht in `kinder[]` ist (Testkind), lädt die App erneut mit `mit_testkind: true`.
- Vorbereitet für **LM-S 2** (Nachbesserung 21.11., noch nicht gebaut): `eigenstaendig` als Text (auch `true`), `ohne_flug: true` → Karte blass gepunktet + Hinweis im Detail. Fehlen in der Liste `lehrplan` **und** `merke`, lädt das Detail einmal nach mit **`schule_lehrplan_matrix { thema_id }`** und erwartet `themen[0]` (oder `thema`) mit `lehrplan, merke, beispiel` (Annahme zu Name/Form – bitte so bauen oder mir den Namen melden; Anpassung ist eine Zeile).

**Was von der bisherigen Lehrplan-Übersicht (LB-1) wegfällt** (Auftrag: nennen)
- Die Kacheln „Flüge · fertig · in Prüfung · fehlt“ mit Zählern und der **Filter nach Inhaltsstand** – der Inhaltsstand steht nur noch je Thema im Detail. Wer „was fehlt noch?“ sucht, hat keinen Sammelblick mehr.
- **Gruppen nach Lernbereich** (Überschriften „M8 2 Lineare Funktionen“) – die Matrix gliedert nach Themengebiet; der Lernbereich steht im Detail.
- Klassen-Knöpfe mit Kind-Marken (A/B) – ersetzt durch die Lernstand-Leiste.
- „Zeile antippen → Inhalte ansehen“ ist jetzt zwei Schritte (Thema antippen, dann „Inhalte ansehen ›“).
- Die Tabelle „Stufe je Kind in einer Zeile mit Wort“ – ersetzt durch „Beide vergleichen“ (Punkte, Wort im Detail).
- **Info-Seite:** Die wörtlichen Texte aus Teil 7 beschreiben noch die alte Übersicht („Eine Zeile antippen öffnet ‚Inhalte ansehen‘“, „Lehrplan-Übersicht ›“). Nicht geändert – bitte neuen Wortlaut liefern.

**Abweichungen von der Vorlage**
- Stufenfarben wie im Plan (◉ grün, ↻ hellgrün, ▶ gelb mit Rahmen) statt der Vorlagenfarben (Wdh gelb, dran blau) – die Vorgabe sagt „wie im Plan (LB)“. Dadurch ähnelt ▶ dem Gelb der Voraussetzungen; die Rolle zeigt zusätzlich der Rahmen.
- „IB MYP“ als dritte Schulart in „Einordnen nach“ (für ein IB-Kind nötig); Zeilen bleiben Kl. 5–10 mit „MYP-Jahr n“ darunter.
- Die Liste vermuteter Zuordnungslücken der Vorlage (`LUECKE`) ist nicht übernommen – das klärt Runde 30 in den Daten.
- Silbentrennung (`hyphens: auto`) in Karten und Gebietsköpfen: Wörter werden nur mit Trennstrich umbrochen, nie ohne; „Gym‑Pflicht“ mit festem Bindestrich.

**Gesehen/getestet**
- lernen: 141 von 141 (neu 9 Tests: LM-1; LM-2/LM-3; LM-4; LM-5 Knöpfe/Rückgängig/Im Plan öffnen/Als Matrix; Abnahme 400/820/1280 je Lernstand-Modus und Aufbau – nichts läuft über, kein Umbruch ohne Trennstrich, kein Querrollen, Handy Liste ohne Linien, Detail unter dem Thema; Link in der Reiterzeile; LM-S-Format; LM-S-2-Nachladen). Ersetzt: vier Tests der alten Übersicht (LA-7 Tabelle, LA-7 Tablet, I-3 Liste, LB Teil 5 S3 → jetzt Reihenfolge je Zelle und Lernbereich im Detail). Testdaten: echte Themenliste, Verbindungen aus der Vorlage, Lernstand erfunden (Kind A/Kind B, Testkind).
- Suche: die bekannten alten Fehler (PWA-Hülle, Startkarte, W80 ×4, Review301, Woanders gebucht, W88) und das datumsabhängige „W80: Jede neue Suche“; „LB Teil 8: aufgeklappte Karte“ wackelte einmal im Gesamtlauf und besteht einzeln.

**Nicht geprüft / Hinweise**
- Mit echten Daten und echten Geräten nicht angesehen; nur Chromium. Mit dem LM-S-Server nur gegen nachgebildete Antworten getestet (Feldliste oben).
- Größe: LM-S im Probelauf 249 KB plus Übersicht – auf langsamer Verbindung spürbar, bis LM-S 2 den Wortlaut auslagert.
- Auf dem Tablet (820 px) sind acht Spalten eng: viele Titel werden getrennt (mit Trennstrich). „Klassen als Spalten“ ist dort etwas luftiger.
- Nächster Schritt: LM-6 Kinderseite als 0.85.0.

## 2026-11-21 – bau-lehrer – FERTIG: LM-S 2

Auf AUFTRAEGE.md „Nachbesserung Dreißigste Runde und LM-S (21.11.)“, Teil B. Nur Dateien, nichts ausgeführt, kein App-Code. Die LM-S-Dateien von heute früh sind ersetzt (nicht eingespielt, daher in derselben Datei).

**Dateien:** `supabase/migrations/20261121_lm_s_lehrplan_matrix.sql`, `supabase/tests/lm_s_lehrplan_matrix_rauchtest.sql`, `supabase/functions/lernen-api/index.ts` (neue Aktion `schule_lehrplan_thema: ['thema_id', 'lernender_id?']`, VERSION 0.8.0).

**Was sich ändert**
- `eigenstaendig` ist Text (Begründung, null = nicht gekennzeichnet), gelesen über `to_jsonb(t)->>'eigenstaendig'` – läuft vor und nach `20261121_lehrplan_zuordnung_voraussetzungen.sql` (der boolean-Abbruch ist weg). Raster: `eigenstaendig: true`, wenn gesetzt; Detail: der Begründungstext; Kind: nie.
- `ohne_flug: true` bei Themen ohne freigegebene Einheit (dann auch kein `einheit_id`, kein `etappen_anzahl`) – im Raster und im Detail.
- Aufgeteilt in **Raster** (`schule_lehrplan_matrix`) und **Detail** (`schule_lehrplan_thema`, beim Antippen). Zugang für beide gleich (`schule.lehrplan_sicht`): Eltern/Lehrer → Lehrer-Sicht; Lern-Zugang → nur das Kind selbst; sonst `lernender_id` + `schule.zugriff`.

**Größe** (Teile nur lesend nachgerechnet, 21.11.): Raster Lehrer ≈ 43 KB Themen + ≈ 1 KB Verbindungen + ≈ 11 KB Lernstand je Kind → mit zwei Kindern ≈ 65 KB (vorher 249 KB). Kindsicht deutlich kleiner (ohne jahrgang/lernbereich/pflicht). Detail ≈ 2–5 KB je Thema. Rauchtest Prüfung 7 bricht ab, wenn das Lehrer-Raster mit allen aktiven Kindern ≥ 90 000 Zeichen hat; Prüfung 8 beim Detail ≥ 30 000.

**Feldliste Raster** `{ok, kindsicht, themen[], verbindungen[], gebiete[], kinder[], lernstand{}}` (fehlende Werte weggelassen; fehlt = nein)
- `themen[]` je Mathe-Thema einmal, sortiert Gebiet → Thema: `thema_id, schluessel, titel, gebiet_id, block_id, einheit_id | ohne_flug, etappen_anzahl`; nur Lehrer: `jahrgang {gym_by, rs_by, ib_myp}`, `lehrplan_reihenfolge`, `lernbereich`, `pflicht [schularten]`, `eigenstaendig: true`; nur Kind: `zeile {klasse, eingeordnet?}`, `reihenfolge_kind`.
- `verbindungen[]` = `[thema_id, braucht_id, "h"|"e"]` („thema_id braucht braucht_id“, h = hart, e = empfohlen). „Weiter zurück“ = Kette darüber.
- `gebiete[] {gebiet_id, titel, reihenfolge, zusatz}` (Gebiet-Titel nur hier).
- `kinder[] {id, name, klasse, schulart}` (Kind: nur es selbst, ohne schulart).
- `lernstand[kind_id][thema_id]`: `stufe` (immer), sonst nur wenn gesetzt: `zeichen, im_plan, begonnen, gelandet, sicher, wieder_offen, wdh_nr, naechste_in, rueckreise, test_offen, hinweis, etappe_jetzt` (nur bei „dran“; „Etappe x von y“ mit y = `themen[].etappen_anzahl`), nur Lehrer `fehler_offen`. Weggelassen gegenüber thema_stufe: `etappen, gesetzt, ohne_test, wdh_stufe_min`.

**Feldliste Detail** (`daten: {thema_id}`; Kind über Lern-Zugang ohne weitere Angabe)
- `thema_id, titel, kurz, ort, was_gefordert, einheit_id | ohne_flug, merke [], etappen [{lernziel, titel, pflicht}], beispiel` (< 160 Zeichen), `braucht [{thema_id, titel, art, begruendung}]`, `baut_darauf [{thema_id, titel, art, begruendung}]`; nur Lehrer: `lehrplan {schulart: Wortlaut}`, `eigenstaendig` (Text). Kind: ohne `lehrplan`, `eigenstaendig`, `pflicht`, `begruendung`.

**Rauchtest:** 1–8 wie gehabt angepasst (Raster knapp, ohne_flug, Detail, Größe); 9 eigenständig als Text (setzt in der Transaktion eine Begründung an einem Thema und nimmt sie zurück; übersprungen, solange die Spalte fehlt); 10 Selbstprüfung als NOTICE: 10a–c wie bisher (10a: eigenständig = Begründung gesetzt), neu 10d „keine Verbindung von oder zu einem Thema ohne Flug“ (Teil A).

**Annahmen:** Kindsicht-Zeile MYP-Jahr + 5 = Klasse. Größe je Kind steigt mit Fortschritt (mehr gesetzte Felder); Obergrenze grob ≈ 15 KB je Kind.

## 2026-11-21 – bau-lehrer – FERTIG: LM-S

Bau-Auftrag LM (21.11.), Schritt 1. Nur Dateien, nichts ausgeführt, kein App-Code, kein Merge nach main, keine Kinderdaten.

**Dateien**
- `supabase/migrations/20261121_lm_s_lehrplan_matrix.sql`: `schule.thema_klasse_fuer(jahrgang, schulart)`, `schule.lehrplan_matrix(kinder[], kindsicht)` (innere Funktion), `api.schule_lehrplan_matrix(schlüssel, daten)` (security definer, Rechte wie üblich: nur council_mcp). Kein DROP/DELETE, Bestand unverändert, wiederholbar. `api.schule_lehrplan_uebersicht` bleibt unverändert (App 0.83 nutzt sie weiter).
- `supabase/tests/lm_s_lehrplan_matrix_rauchtest.sql`: Rollback, nur Testkind, Prüfungen 1–7 vergleichen gegen die Tabellen (keine festen Bestandszahlen), Prüfung 6 legt sich „Fehler offen“ im Testkind selbst an; Prüfung 8 = Selbstprüfung (s. u.).
- `supabase/functions/lernen-api/index.ts`: Aktion `schule_lehrplan_matrix: ['lernender_id?', 'mit_testkind?']`, VERSION 0.8.0 (Server-Datei, muss mit deployt werden).

**Befund: was die Übersicht nicht liefert** (Live-Text gelesen): merke, Etappen mit Pflicht, Verbindungen (Art, Begründung), kurz, Pflicht je Schulart, Beispielaufgabe, Gebiet-Reihenfolge, „Etappe x von y“, „Fehler offen“, Kinderzugang. Außerdem eine Zeile je Thema × Ort (Matrix braucht je Thema einmal).

**Zugriff**
- Eltern/Lehrer (`schule.ist_leiter`): alle aktiven Kinder in einem Aufruf; Testkind nur mit `mit_testkind: true`.
- Kind (Lern-Zugang): nur es selbst (aus `lern_ich`; `lernender_id` wird ignoriert). Sonstige Zugänge: `lernender_id` + `schule.zugriff`. Immer Kindsicht.

**Feldliste für den App-Bau** (`ergebnis` = `{ok, kindsicht, themen[], verbindungen[], gebiete[], kinder[], lernstand{}}`; fehlende Werte sind weggelassen, nicht null)
- `themen[]` (je Mathe-Thema genau einmal; sortiert Gebiet → Thema-Reihenfolge):
  - beide Sichten: `thema_id, schluessel, titel, kurz, gebiet, gebiet_id, ort, block_id` (erster Ort nach Block-Reihenfolge), `was_gefordert` (= thema.beschreibung, „Was gefordert ist“), `einheit_id` (nur mit freigegebener Einheit), `merke` (Array, „Das muss sitzen“), `etappen[] {lernziel, titel, pflicht}`, `beispiel` (erste freigegebene Übungsaufgabe, Text < 160 Zeichen)
  - nur Eltern/Lehrer: `jahrgang {gym_by, rs_by, ib_myp}` (Klasse je Schulart; IB = MYP-Jahr), `lehrplan_reihenfolge {schulart: n}`, `lernbereich {schulart: …}`, `lehrplan {schulart: Wortlaut}`, `pflicht [schularten]` (Thema einem Eintrag einer aktiven Basis-Quelle zugeordnet), `eigenstaendig` (s. u., heute nie gesetzt)
  - nur Kindsicht: `zeile {klasse, eingeordnet}` (Klasse in der Schulart des Kindes; fehlt sie, die der anderen bayerischen Schulart bzw. MYP+5 → `eingeordnet: true`), `reihenfolge_kind`
- `verbindungen[] {thema_id, braucht_id, art: hart|empfohlen, begruendung}` – „thema_id braucht braucht_id“. Kindsicht ohne `begruendung`. „Braucht vorher“, „weiter zurück“ (Kette) und „Darauf baut auf“ rechnet die App daraus; Klasse der Voraussetzung über `themen[].jahrgang`. Leere Liste → Hinweis „Keine Voraussetzung hinterlegt“.
- `gebiete[] {gebiet_id, titel, reihenfolge, zusatz}`
- `kinder[] {id, name, klasse, schulart}` – Kindsicht: nur das Kind, ohne `schulart`.
- `lernstand[kind_id][thema_id]` = `schule.thema_stufe` (u. a. `stufe, zeichen, im_plan, etappen, begonnen, gelandet, sicher, wieder_offen, wdh_nr, naechste_in, rueckreise, test_offen`) + `etappe_jetzt` (nur bei stufe „dran“: gelandet+1, höchstens etappen → „Etappe x von y“ mit y = `etappen`) + nur Eltern/Lehrer `fehler_offen` (Pflicht-Etappe mit Status „fehler“ → Link „Fehler besprechen ›“).

**„eigenständig“** – Fakt: wird heute nirgends gespeichert. Vorschlag (nicht gebaut): Spalte `schule.thema.eigenstaendig boolean default false` (+ ggf. `eigenstaendig_grund text`), gesetzt vom Lehrplan-Chat. Die Matrix-Funktion und Regel 8a lesen sie schon über `to_jsonb(t)->'eigenstaendig'` – sobald die Spalte da ist, wirkt sie ohne weitere Änderung. Entscheidung, wer sie anlegt: Haupt-Chat.

**Selbstprüfung Dreißigste Runde** (Rauchtest Prüfung 8, NOTICE mit Anzahl und Nummern, kein Abbruch). Stand heute, nur gelesen:
- 8a Thema mit Klasse ohne Verbindung, nicht eigenständig: 28 (17, 19, 22, 27, 34, 40, 42–45, 59, 60, 64–66, 69, 70, 73, 75, 81, 83, 84, 98–103).
- 8b Voraussetzung in späterer Klasse als das Thema: 1 (33 braucht 32, nur IB-MYP).
- 8c Themen 100–103 verknüpft: nein, alle 4 ohne Verbindung.
→ Die Regeln sind heute nicht erfüllt; deshalb NOTICE statt Abbruch. Sollen sie nach dem Nachpflegen hart werden: in Prüfung 8 NOTICE → EXCEPTION.

**Annahmen / offen**
- Kindsicht-Zeile: MYP-Jahr + 5 = Klasse (wie in lernen.js).
- Größe: Lehrer-Antwort ca. 140 KB (Themen ~113 KB ohne Lehrplan-Wortlaut + ~24 KB Wortlaut) plus Lernstand je Kind. Wenn das zu groß ist: Wortlaut erst im Detail nachladen.
- Rauchtest-Prüfung 6 braucht eine Einheit mit Pflicht-Etappe (sonst „übersprungen“).

## 2026-11-21 – bau-lehrer – FERTIG: flug_geschafft robust 2

Auf antworten.md „21.11. 04:25“. Nur Dateien, nichts ausgeführt, kein App-Code, kein Merge nach main.
- Neu: `supabase/migrations/20261121_ab_s_flug_geschafft_robust.sql` – legt `schule.flug_fertig_nach(lernender, einheit, sitzung)` an und baut die eingespielte `schule.test_abschliessen_intern` um: alte Bedingung `x.flug_geschafft is distinct from false` → `x.flug_geschafft or (x.flug_geschafft is null and schule.flug_fertig_nach(...))`. Umbau über `pg_get_functiondef` + `replace`; die Stelle steht live genau einmal (gelesen 21.11.). Wiederholbar: ist `flug_fertig_nach` schon im Funktionstext, passiert nichts. Fehlt die Stelle (alte Datei nicht eingespielt), bricht die Migration mit Hinweis ab.
- Zurückgesetzt: `20261120_ab_s_flug_abschluss_einmal.sql` = eingespielter Stand (Commit 80e67e8, md5 f79c1701…).
- `supabase/tests/ab_s_abschluss_rauchtest.sql`: nur Kopfzeile – Prüfung 9 setzt jetzt beide Dateien voraus. Prüfung 9 (9a–9e) unverändert.
- Reihenfolge Haupt-Chat: neue Datei einspielen → Rauchtest ab_s (Prüfung 9c muss jetzt grün sein).

## 2026-11-21 – FERTIG: 0.83.3 – App 0.83.3, Cache v153

Stand `lernen-app` 05037ef (0.83.2 live, Nachträge aus Prüfergebnis 888). Nur App (`lernen.js`, `style.css`), Versionsnummer in sechs Dateien, Tests. Nichts in der Datenbank, keine Kinderdaten, keine Schlüssel, kein Merge nach `main`.

1. **„Etappen ▸“ (Entscheidungen Sebastian 21.11., Punkt 3):** In der Inhalte-Zeile der kompakten Themen-Karte („Inhalte ansehen (n Etappen)“ · „Ort: …“) steht ein zugeklappter Textlink „Etappen ▸“ (`aria-expanded`, `aria-controls`). Aufgeklappt („Etappen ▾“) die Liste wie in 0.83.0: Nummer, Titel, Stand rechtsbündig in der ersten Titelzeile (offen / begonnen / gelandet / sicher / wieder offen, Farben wie vorher). Zuklappen mit demselben Link, der Fokus bleibt darauf. Gilt in „Nach Klasse“ und im aufgeklappten Ort unter „Nach Themengebiet“. Bei Flügen ohne Etappen gibt es den Link nicht.
2. **Reisewörter (Punkt 4):** Der Test „Reisewörter auf allen Eltern-/Lehrerseiten“ verbietet „Thema“, „Themen“ (und damit „Themengebiet“) nicht mehr; „Lernkarte“, „Aufgabe“, „Themenplan“, „Lernziel“ und das alleinstehende „Gebiet“ bleiben auch dort verboten (enge Auslegung – sag Bescheid, wenn auf Eltern-/Lehrerseiten gar nichts mehr geprüft werden soll). Ebenso im Test der Info-Seite. Neu: **Test „Reisewörter auf den Kinderseiten“** (Abflugtafel, Reisepass, Erklärung, Bordkarten, Flug-Test; klassisch und neue Gestaltung) gegen Lernkarte, Aufgabe, Themen, Themenplan, Lernziel, Gebiet. Hinweis: „Thema“ (Einzahl) prüfe ich dort nicht, weil die Abschluss-Ansichten es laut Vorgabe selbst verwenden („Weiter zum nächsten Thema“, „NEUES THEMA“). Keine Texte geändert.
3. **Nachtrag 888 (Teil bau-motivation):** Meldet der Server `ort_geschafft: true` mit `flug_geschafft: false`, startet die Abschluss-Ansicht direkt mit dem Ort-Stempel, danach die Bordkarte – kein zweites „Flug geschafft“. Bei `flug_geschafft: true` und `ort_geschafft: true` bleibt die Reihenfolge Flug → Ort → Bordkarte; ohne das Feld (alter Server) wie 0.83.0.

**Getestet** (Playwright mit Chrome): **lernen 135 von 135** – neu 3 („Etappen ▸“ auf 400 px mit Lage des Stands und Fokus; Reisewörter Kinderseiten; nur `ort_geschafft`), angepasst 3 (Reisewörter Eltern/Lehrer, Info-Seite, Nachtrag B: Fall „flug und ort geschafft“). Alle Tests: 277 bestanden, 1 übersprungen, 9 Fehler – die 9 bekannten im Reise-Bereich. W175 ist heute wieder grün (datumsabhängig); „W80: Jede neue Suche hat eine Reise“ fiel in einem Gesamtlauf einmal aus und lief danach dreimal grün (Reise-Bereich, wackelt).

**Nicht geprüft:** echte Geräte und Safari, Bildschirmleser, gegen den echten Server.

FERTIG: 0.83.3

## 2026-11-21 – FERTIG: flug_geschafft robust (Nachträge aus ChatGPT 888)

Stand `lernen-app` 05037ef übernommen. Nur Dateien – nichts ausgeführt, kein App-Code, kein Merge. pglast ok.
**Migration** `supabase/migrations/20261120_ab_s_flug_abschluss_einmal.sql` (weiter nicht eingespielt):
- neu `schule.flug_fertig_nach(kind, einheit, sitzung)`: War der Flug nach dieser Sitzung fertig? Je Pflicht-Etappe zählt das letzte Ergebnis in einem abgeschlossenen Flug-Test, Verbessern oder Nachtest bis einschließlich dieser Sitzung (alle Antworten der Etappe richtig); eine Pflicht-Etappe ohne Ergebnis bis dahin → nicht fertig.
- Bedingung „früherer Abschluss“: frühere abgeschlossene Flug-Test-/Verbessern-Sitzung mit `flug_geschafft` true **oder** mit NULL **und** `flug_fertig_nach(...)` true. Eine alte nicht bestandene Sitzung (NULL, Flug danach offen) sperrt also keinen späteren ersten Abschluss mehr. Alles andere unverändert (vorher nicht fertig; nur `blocktest`/`korrektur`; einmal festgehalten).
**Rauchtest** `ab_s_abschluss_rauchtest.sql`, Prüfung 9 neu aufgebaut – **ohne Überspringen**: Die Sitzungen legt der Test selbst an (Hilfsfunktion `pg_temp.ab9_sitzung`: eine Bordkarte je Pflicht-Etappe, Antworten richtig/falsch), abgeschlossen wird über `test_abschliessen_intern`; Flug mit mindestens 2 Pflicht-Etappen in einem Ort mit weiteren offenen Flügen.
- 9a/9b nicht bestanden + erneuter Aufruf → false, keine Felder.
- **9r/9c Regression:** die nicht bestandene Sitzung auf NULL gesetzt (wie alt), Flug offen → Verbessern macht ihn erstmals fertig → **true** mit Feldern; erneuter Aufruf gleich.
- 9c-2: die erste Verbessern-Sitzung auf NULL gesetzt (alte Sitzung, die den Flug fertig gemacht hatte) → zweites Verbessern → false.
- 9d Nachtragstest → false. **9e Nachtest (neu, eigener Negativfall)** → false, keine Felder.
**Hinweis:** Vor dem Probelauf die Bestandsprüfung aus 888 gilt weiter (7 alte Sitzungen, alle zu fertigen Flügen) – mit der neuen Bedingung zählen sie als frühere Abschlüsse, wenn `flug_fertig_nach` sie als fertig erkennt.

## 2026-11-21 – FERTIG: 0.83.2 (LB Teil 9, Punkte 1, 2, 4, 5, 6) – App 0.83.2, Cache v152

Stand `lernen-app` b2a71ba übernommen. Nur App (`lernen.js`, `style.css`), Versionsnummer in sechs Dateien, Tests. Nichts in der Datenbank, keine Kinderdaten, keine Schlüssel, kein Merge nach `main`. **Punkt 3 (N8, Wort „Themen“) bleibt offen** – nichts geändert.

**Lehrer-Ansicht**
1. **N6:** Der gewählte Themengebiet-Knopf (`.lern-chip[aria-pressed="true"]`) behält beim Hover den dunklen Hintergrund und die weiße Schrift (gilt für alle Chips dieser Art; die eigenen Farben der Kinderseite bleiben). Gemessen: Kontrast unter dem Zeiger ≥ 4,5 : 1; nicht gewählte Knöpfe werden beim Hover weiter hell.
2. **N7 (Handy < 560 px):** Titel der Plan-Zeile ist nur noch das Thema; das Themengebiet steht klein und grau am Anfang der Zeile darunter („Algebra · ▶ Gerade dran · …“). Der volle Titel bleibt im `title` und im Bildschirmleser-Namen. ↑ ↓ sind 32 px breit. Die automatische Silbentrennung aus Teil 6 ist wieder aus – damit gibt es **nie Trennstrich und „…“ hintereinander**. Messung mit der echten Themenliste (36 Plan-Zeilen): **400 px: 2 Titel mit „…“** (Nachprüfung 5: fast alle; nach Teil 6: 12); 820 px: 6 (die Trennung fehlt jetzt auch dort; vorher 3, ursprünglich 28). Ab 560 px steht das Gebiet wie bisher vor dem Titel.
4. **Info-Seite, Schritt 1:** „Rechts (auf dem Handy darunter) der Lehrplan: …“.

**Abschluss-Ansichten (Kind)**
5. **N1:** Datum im Ort-Stempel wird selbst gebaut („21.11.“) statt `toLocaleDateString` + Punkt – nie „..“, unabhängig vom Browser.
6. **N2:** 18 px Abstand unter „2/2“ (der Schrägstrich berührt „AUF ANHIEB“ nicht mehr; 400 × 780 weiter ohne Scrollen). **N3:** Der Blitz beim Sturmflug beginnt weiter rechts unten (neben dem Flugzeug) – maschinell geprüft: bei 360 × 640, hell und nacht, liegt kein Punkt des Blitzes in Titel, Unterzeile, Abzeichen oder Kopfzeile (mit dem alten Blitz schlägt die Prüfung fehl). **N4:** Test „AB-A 2“ wartet jetzt auf das Schließen der Ansicht (`.lr-abschluss` detached, höchstens 3 s) – 5 von 5 Läufen grün. **N5:** „Überspringen ›“ auf dem Ort-Bildschirm: dunkelbraun (#3B2A14) mit hellem Rand, fett; Kontrast Schrift/Knopf ≥ 4,5 : 1, Knopf/Sand ≥ 3 : 1 (gemessen).

**Getestet** (Playwright mit Chrome): **lernen 132 von 132** – neu 5 (N6, N7 mit Messung, Info-Schritt 1, N1/N5, N2/N3), angepasst 3 (AB-A 2 wartet auf das Schließen; „Teil 6 N2“ prüft zusätzlich „nie Trennstrich und …“ und ≤ 4 gekürzte auf dem Handy; „Flugplan: Änderung bleibt …“ liest die Reihenfolge aus dem Titel-Attribut, weil auf dem Handy das Gebiet nicht mehr im Titel steht). Alle Tests: 273 bestanden, 1 übersprungen, 10 Fehler – alle im Reise-Bereich, dieselben wie bei 0.83.1 (die 9 bekannten und W175, datumsabhängig).

**Nicht geprüft:** echte Geräte und Safari, Bildschirmleser; „Hover bleibt auf dem Tablet hängen“ (N6) nur am Rechner nachgestellt.

FERTIG: 0.83.2

## 2026-11-21 – FERTIG: 0.83.1 (LB Teil 8 und Nachtrag B) – App 0.83.1, Cache v151

Stand `lernen-app` 31b73f6 übernommen, dazu `bau-lehrer` 80e67e8 („FERTIG: flug_geschafft“ lag vor); vor dem Push `lernen-app` 44a30d2 eingemischt (nur Postfach/Inhalte). Nur App (`lernen.js`, `style.css`), Versionsnummer in sechs Dateien (`app.js`, `index.html`, `lernen/index.html`, `lernen/schule.js`, `sw.js`, `tests/search.test.cjs`), Tests. Nichts in der Datenbank, keine Kinderdaten, keine Schlüssel, kein Merge nach `main`.

**LB Teil 8 – aufgeklappte Themen-Karte, Variante A** („Nach Klasse“ und aufgeklappter Ort in „Nach Themengebiet“)
- Kopf, „Lehrplan: …“ und Beschreibung unverändert.
- Eine Zeile: Knopf „Inhalte ansehen (n Etappen)“ mit Rahmen in Akzentfarbe (öffnet `#/inhalte/<Flug>` wie bisher), daneben klein und grau „Ort: <Ort>“; ohne Inhalt steht dort „noch kein Inhalt“. Die Etappen-Kästchen entfallen.
- Trennlinie, dann „Stufe ⓘ“ (ⓘ öffnet „So funktioniert’s“ mit aufgeklappter Frage „Was kann ich selbst ändern?“, in der die vier Stufen erklärt sind – neue Adresse `#/info/stufen`) und drei schmale Knöpfe „Lernen“ · „Kann er – wiederholen“ · „Kann er komplett“; der aktive grün hinterlegt mit „✓“. Keine Erklärungszeilen mehr.
- Rechts als roter Textlink „Aus dem Plan nehmen“, außerhalb des Plans „In den Plan nehmen“ (Akzentfarbe). Wirkung und Speichern unverändert (dieselbe `setze`-Funktion wie bisher).
- Rückfall-Hinweis aus Teil 6 bleibt im Kopf der Zeile sichtbar. Nebenbei berichtigt: Er erscheint nur noch bei der Stufe ◉ (vorher auch, wenn die App einen „komplett“ gesetzten Flug lokal auf „Kommt noch“ umrechnete).
- **Abweichungen / offen (bitte entscheiden):**
  1. **Etappen-Liste mit Stand (Teil 5 S4) ist im Plan nicht mehr zu sehen.** „Inhalte ansehen“ zeigt die Inhalte, nicht den Stand des Kindes je Etappe. Den Stand je Etappe sehen Eltern/Lehrer weiter unter „Was wackelt“ (nur Etappen mit Fehlern) und auf der Abflugtafel des Kindes. Wenn er im Plan bleiben soll: Vorschlag ein zugeklappter Textlink „Etappen ▸“ in der Inhalte-Zeile.
  2. **„Wieder in die Wiederholung“** steht bei ◉-Flügen weiter in der Stufen-Zeile, als grauer Textlink (sonst ginge die Funktion in der Karte verloren; Variante A nennt ihn nicht).
  3. **„Aus dem Plan nehmen“ in derselben Zeile** passt nur, wenn die Spalte breit genug ist. Die Lehrplan-Spalte ist auch bei 1280 px nur etwa 450 px breit – dort und bei 820 px steht der Link rechtsbündig in einer eigenen Zeile unter den Knöpfen (wie auf dem Handy). Siehe `test-results/lb8-karte-{400,820,1280}.png` beim Testlauf.
  4. Die alte Etappen-Liste mit Stand rechts (Teil 6 N5) ist damit ebenfalls weg; ihr Test entfällt.
- Abnahme: 400, 820, 1280 – kein Wort mitten im Wort umbrochen in der Karte (gemessen vor und nach dem Umschalten), kein Querrollen, zugeklappte Zeilen unverändert.

**Nachtrag B – Flug-Abschluss an `flug_geschafft`:** Die Abschluss-Ansicht des Flugs kommt, wenn die Antwort `flug_geschafft: true` oder `ort_geschafft: true` enthält. Steht `flug_geschafft` gar nicht in der Antwort (Server ohne `20261120_ab_s_flug_abschluss_einmal.sql`, also heute live), gilt die Regel von 0.83.0 (`einheit_abgeschlossen` bzw. Flug-Test bestanden, nicht nach Nachtest). Das Test-Ergebnis selbst (Liste, „Flug geschafft!“-Zeile, Knöpfe) ist unverändert. Die App ist damit vor und nach dem Einspielen der Migration richtig – sie kann also vor der Migration live gehen.

**Getestet** (Playwright mit Chrome): **lernen 127 von 127** – neu 3 (Teil 8 Karte bei 400/820/1280 mit Wirkung, Farbe, Lage und zugeklappten Zeilen; Themengebiet + Rückfall + ⓘ; Nachtrag B mit `flug_geschafft` true/false, `ort_geschafft`, alter Server), angepasst 4 (LA-4, LB-1/LB-5, Teil 5 S4: neue Knopf-Texte und Karte; Teil 6 N5 entfällt). Alle Tests: 268 bestanden, 1 übersprungen, 10 Fehler – alle im Reise-Bereich: die 9 bekannten (PWA-Hülle, „Lernen Schule: Startkarte“, W80 ×4, Review301, „Woanders gebucht“, W88) und neu **W175 „Reiseplan-Kopf“** – hängt am Datum („Tag 11 von 110“, seit heute 21.11. Tag 12) und schlägt ohne meine Änderungen genauso fehl.

**Nicht geprüft:** echte Geräte und Safari, Bildschirmleser, gegen den echten Server (`flug_geschafft` nur nach der Feldbeschreibung von bau-lehrer nachgebildet).

FERTIG: LB Teil 8
FERTIG: 0.83.1

## 2026-11-20 – FERTIG: flug_geschafft (Nachträge 20.11. nachmittags, Teil A)

Stand `lernen-app` e8450e0 übernommen. Nur Dateien – nichts ausgeführt, kein App-Code, kein Merge. pglast ok.
**Migration** `supabase/migrations/20261120_ab_s_flug_abschluss_einmal.sql` (weiter nicht eingespielt): `flug_geschafft` = dieser Aufruf schließt die Sitzung ab **und der Flug wird dadurch zum ersten Mal fertig** – über den Flug-Test (`blocktest`) **oder** über Verbessern (`korrektur`). Geprüft wird
- vorher nicht fertig (Stand der Pflicht-Etappen beim Betreten des Aufrufs, bevor die Ergebnisse gebucht werden) und
- keine frühere abgeschlossene Flug-Test- oder Verbessern-Sitzung dieses Flugs mit `flug_geschafft` true oder unbekannt (`null`, vor dem Einspielen).
Weiter false: nicht bestandener Test, zweites Verbessern, Nachtragstest, Nachtest, Sitzungen vor dem Einspielen. Erneuter Aufruf derselben Sitzung: dasselbe wie beim ersten Mal (Wert ist gespeichert). Die Abschluss-Felder kommen weiter nur bei `flug_geschafft` oder `ort_geschafft`.
**Rauchtest** `ab_s_abschluss_rauchtest.sql`: **9c** neu – Verbessern macht den Flug erstmals fertig → `flug_geschafft` true mit `flug`, `etappen`, `sterne_flug`, `naechster_flug`; erneuter Aufruf gleich. **9c-2** neu – zweites Verbessern (eine Etappe wieder „fehler“) → false, keine Felder. 9a/9b (nicht bestanden, erneuter Aufruf) und 9d (Nachtragstest) unverändert false.
**Grenzfall (Annahme):** Eine Sitzung von vor dem Einspielen zählt als „Ausgang unbekannt“ und verhindert die Ansicht für diesen Flug – außer sie wurde inzwischen erneut gelesen (dann steht dort false). Lieber einmal keine Ansicht als eine doppelte.

## 2026-11-20 – FERTIG: AB-A und LB Teil 6 (dazu LB Teil 7) – App 0.83.0, Cache v150

Stand `lernen-app` 1cc6edc übernommen (Zweig `bau-motivation`). Nur App (`lernen.js`, `style.css`, `sw.js`) und Tests. Nichts in der Datenbank, keine Kinderdaten, keine Schlüssel, kein Merge nach `main`.

**AB-A:** war beim Holen schon in `lernen-app` (Commit 9cea758, App 0.83.0, Cache v149, Meldung „FERTIG: AB-A“ weiter unten; gebaut über `bau-lehrer`). Nicht noch einmal gebaut. Die Version bleibt **0.83.0** (noch nicht live), Teil 6 und Teil 7 kommen dazu, Cache **v149 → v150**.

**LB Teil 6 (Nachprüfung 4)**
- **N1 (Muss) „Nach Themengebiet“:** Unter 1100 px steht die Stufe (bzw. „+“) unter dem Titel, die Zeilen haben feste Plätze (Griff/Häkchen · Klassen-Kasten · Titel), damit auch das Auswählen die Zeile nicht auseinanderzieht. **Messung mit dem Skript des Gestalters (`n4/n4.test.cjs`, echte Themenliste):** gebrochene Wörter in allen 8 Gebieten – vorher 400: 2, 820: 16, 1280: 0 → **jetzt 0 / 0 / 0**; „Nach Klasse“ weiter 0 in allen 17 Klassen. Hinweis zum Skript: Es rechnet die Wurzel als `../../..` von `n4/` aus und findet so `tests/lernen.test.cjs` nicht (läuft nur, wenn es zwei Ebenen tiefer liegt) – ich habe es dafür in einen Hilfsordner kopiert, nicht geändert.
- **N2 (Sollte) Plan links:** Titel unter 1100 px bis zu zwei Zeilen (14 px, Silbentrennung `hyphens: auto`, Sprache `de`), erst danach „…“. Gekürzte Titel: 400 px **31 → 12** von 36, 820 px **28 → 3** von 36 (die übrigen brauchen mehr als zwei Zeilen). Die Schrift ist dafür 1 px kleiner, damit E-2 („12 Orte auf einem Tablet, Zeile ≤ 72 px“) weiter erfüllt ist. Lange Wörter werden jetzt mit Trennstrich umbrochen („Gleichungs-systeme“) statt abgeschnitten – bitte ansehen.
- **N3 (Sollte) Zähler:** Jeder Abschnitt zählt nur die Flüge seiner Stufe, im ganzen Plan – dieselbe Zahl wie im Kopf, nach dem Muster der Vorgabe („16 Orte · 20 Flüge in Wiederholung“); mit den Testdaten des Gestalters z. B. „1 Ort · 1 Flug gerade dran“, „5 Orte · 9 Flüge kommen noch“ bei Kopf „1 ▶ · 9 ○“. Für ◉: „… Flüge komplett gekonnt“. Liegt ein Flug dieser Stufe in einem Ort weiter oben (z. B. ein ↻-Flug in einem ▶-Ort), steht „(davon n in Orten weiter oben)“ dabei.
- **N4 (Kann):** eingeplante Zeilen in „Nach Themengebiet“ nicht mehr blass (Deckkraft 1, gleiche Titelfarbe wie die übrigen).
- **N5 (Kann):** Etappen-Liste: Stand („offen“, „gelandet“ …) rechtsbündig in der ersten Titelzeile, ohne „·“.
- **Punkt 6:** „↶ Rückgängig“ gilt nur für den jüngsten Schritt (war schon mit 9cea758 so; jetzt mit Test: nach einem Rückgängig kein zweiter Schritt zurück; lehnt der Server ab, steht „Rückgängig geht nur für die letzte Änderung. Inzwischen wurde etwas anderes geändert.“ mit „Neu laden“). **Rückfall:** `hinweis: 'rueckfall'` zeigt bei ◉ „gesetzt · Rückfall: n Etappen wieder offen“ (bzw. „alle Etappen sicher · Rückfall: …“), rot hervorgehoben – überall, wo die Stufe steht (Plan links, „Nach Klasse“, Themengebiet aufgeklappt). **heute_bis:** neu `lernHeuteTag(kind)` = Tag des Kindes vom Server, solange `heute_bis` nicht vorbei ist, sonst Kalendertag des Geräts; genutzt für „Knobeln des Tages“ (vorher UTC-Datum!) und die „Wiederholungsrunde heute“ (vorher Gerätedatum); der Tageszähler nutzte es schon (9cea758). Nicht umgestellt: Eltern-Seiten (Pausen, „seit … Tagen“) – dort gilt der Tag der Eltern bzw. die Pausenregel „Ortszeit des Kindes“ rechnet schon der Server; ein `heute_bis` je Kind liefert dort keine Aktion.

**LB Teil 7 (Info-Seite, `info-seite-update.md` Punkte 1–7)** – wörtlich übernommen, mit diesen Abweichungen (bitte prüfen):
- Punkt 1: „alle Flüge eines **Themen**gebiets“ statt „eines Gebiets“; Punkt 7: „in welchem Jahr ein **Flug** dran ist“ statt „ein Thema“ – sonst bricht der Test „Reisewörter auf allen Eltern-/Lehrerseiten“ (verboten: „Gebiet“, „Thema“).
- Punkt 3 steht direkt hinter dem Satz mit den Knöpfen („… bei ◉ zusätzlich ‚Wieder in die Wiederholung‘.“), nicht mitten in der Klammer – sonst zerreißt der Satz.
- Punkt 4: Knopftext „Weiter: Flug-Test“ statt „Jetzt zum Test ›“ – mit AB-A heißt der Knopf auf dem Landebildschirm so („Jetzt zum Test ›“ steht nur noch in der Flug-Übersicht).
- „Lernstand:“ und „Was wackelt?:“ gelöscht.
- **Neuer Eintrag (Punkt 8 / AB-A) in „Wie wird gelernt?“, hinter „Etappe gelandet“:**
  > **Abschluss einer Etappe:** Nach der Landung (und der Knobel-Bordkarte) zeigt die App eine von drei Fassungen – jede mit eigenem Bild und eigener Farbe: Direktflug (alle Bordkarten im ersten Versuch richtig, ohne Tipp, genau so viele wie nötig), Saubere Landung (höchstens 2 endgültige Fehler, Stufe nie leichter geworden, höchstens 4 Bordkarten mehr als nötig; nach „wieder offen“ heißt sie „Wieder gelandet“) oder Sturmflug gemeistert (alles darüber; ohne Fehlerzahl, die Knobel-Bordkarte kommt dann nicht von selbst, nur als Textlink). Dazu ein Abzeichen – ⚡ Direkt, ✓ Sauber oder ⚡ Ausdauer –, das im Reisepass gezählt wird, der Satz „Du kannst jetzt …“ und genau ein Knopf zum nächsten Schritt (nächste Etappe, Flug-Test oder Abflugtafel); zurück in die Übungen derselben Etappe führt von dort kein Weg. Nach dem bestandenen Flug-Test: „Flug geschafft“ mit den Sternen des Flugs und der Liste „Das kannst du jetzt“, danach eine Bordkarte zum nächsten Flug im Plan („Boarding“ öffnet seine erste Erklärung). Mit dem letzten Flug eines Orts kommt dazwischen der Reisepass-Stempel. Landungen vor dieser Version haben kein Abzeichen.
- Punkt 3 beschreibt den Stand nach der LB-3-Nachbesserung am Server (noch nicht eingespielt).

**Getestet** (Playwright mit Chrome, lokal): **lernen 125 von 125** (neu 7: N1 als Messung 400/820/1280 × 8 Gebiete + N4, N2, N3, N5, Rückgängig nur jüngster Schritt mit Ablehnung, Rückfall + heute_bis, Info-Seite Teil 7; angepasst 4: Abschnittstexte in LB-5/LA-5/LB Teil 5 S2, Etappen-Format S4, „Teil 4 Punkt 1+2“ misst links jetzt „höchstens zwei Zeilen, nichts seitlich abgeschnitten“ statt „kein getrenntes Wort“). Alle Tests: 267 bestanden, 1 übersprungen, 9 Fehler – dieselben 9 wie vor meinen Änderungen auf demselben Stand (PWA-Hülle, „Lernen Schule: Startkarte“, W80 ×4, Review301, „Woanders gebucht“, W88; Reise-Bereich, nicht Lernen).

**Nicht geprüft:** echte Geräte und Safari (Silbentrennung auf dem iPad), Bildschirmleser, gegen den echten Server (Rückfall-Hinweis und `heute_bis` kommen erst mit der LB-3-Nachbesserung).

FERTIG: AB-A und LB Teil 6
FERTIG: LB Teil 7

## 2026-11-20 – FERTIG: LB-3 Tests ergänzt (Nachträge aus ChatGPT 885, an bau-lehrer)

Stand `lernen-app` 6e04b10 übernommen. Nur Server-Tests und eine Migration als Datei – kein App-Code, **nichts in der Datenbank ausgeführt** (Live-Text nur gelesen, Einfügestellen je genau einmal vorhanden), kein Merge. pglast für alle Dateien ok; die Rauchtests selbst sind **nicht ausgeführt** – bitte im Probelauf.

1. **`lb3_nachbesserung_rauchtest.sql`, neuer Fall „M2-echt“:** gesetzter Flug; das Testkind erarbeitet eine Etappe wirklich über `uebung_pruefen_intern` (verschiedene Auswahl-Bordkarten, richtig im ersten Anlauf: zuerst eine schwere, dann je Typ eine, dann weitere – bis `karte_landet` erfüllt ist: Ziel-Anzahl, Typen, schwere, Folge). Keine Nachweisfelder von Hand. Danach Rücknahme → diese Etappe bleibt gelandet (Herkunft selbst, eigene Lösungen ≥ Ziel), alle anderen Etappen des Flugs offen. Flug/Etappe werden dynamisch gewählt (nur Auswahl-Bordkarten, vom Testkind ungeübt; live 304 passende Etappen).
2. **`i4_misch_ausgabe_rauchtest.sql`:** 1b – zweimal derselbe Flug → dieselben Karten, beide `misch_gueltig`; neu **4b** – Flugwechsel → Ausgaben des anderen Flugs verfallen; zurückgewechselt → neu ausgegeben (Ausgabezeit jetzt) und gültig; ein weiteres Mal zurück; älter als 24 h → verfallen.
3. **`ab_s_abschluss_rauchtest.sql`, Befund und Migration:**
   - **Befund (Live-Text gelesen):** `test_abschliessen_intern` hängt `schule.flug_abschluss(...)` an **jede** Antwort an. Bei nicht bestandenem Flug-Test, bei Verbessern, beim Nachtragstest, beim Nachtest und beim erneuten Aufruf kommen also `flug`, `etappen`, `kurz`, `sterne_flug` (Test-Sterne dieser Sitzung und Summe des Flugs), `naechster_flug`, `ort_wechsel`, `ort_fluege` mit; `ort_geschafft` ist dort false (festgehalten). `einheit_abgeschlossen` ist der **Stand** des Flugs (auch beim erneuten Aufruf und nach Nachtests true), kein Ereignis.
   - **Migration** `supabase/migrations/20261120_ab_s_flug_abschluss_einmal.sql` (nicht ausgeführt): neue Spalte `testsitzung.flug_geschafft`, einmal festgehalten, wenn **dieser Aufruf** die Sitzung abschließt, es der **erste** abgeschlossene Flug-Test (`blocktest`) des Flugs ist und der Flug damit fertig ist. Verbessern, Nachtragstest (späterer `blocktest`), Nachtest, vor dem Einspielen abgeschlossene Sitzungen: false. Antwort: immer `flug_geschafft`; die Abschluss-Felder nur bei `flug_geschafft` oder `ort_geschafft` – auch beim erneuten Aufruf derselben Sitzung (gleiches Ergebnis für „Test ansehen“).
   - **Rauchtest:** 6 und 7 prüfen zusätzlich `flug_geschafft` und dass die Felder beim ersten Abschluss da sind; neu **9a** nicht bestandener Flug-Test, **9b** erneuter Aufruf, **9c** Verbessern (Flug danach fertig), **9d** Nachtragstest – jeweils `flug_geschafft` false und keine Felder `flug`, `naechster_flug`, `sterne_flug` (9a auch `etappen`, `ort_wechsel`). Startet Verbessern oder Nachtragstest mit dem gewählten Flug nicht, meldet der Test „Info“ statt abzubrechen.
   - **Für die App (bau-motivation, kein App-Code von mir):** die Abschluss-Ansicht des Flugs an `flug_geschafft` (oder `ort_geschafft`) hängen statt an `einheit_abgeschlossen`; die App 0.83.0 zeigt sie heute bei „Flug fertig und kein Nachtest“ (also auch nach Verbessern).
   - **Annahme:** „Verbessern“, das einen Flug erstmals fertig macht, zeigt keine Abschluss-Ansicht (so steht es in den Nachträgen: „nicht Verbessern/Nachtragstest“). Soll das Kind dann doch „Flug geschafft“ sehen, genügt in der Migration `t.art in ('blocktest', 'korrektur')` und „kein früherer Abschluss“ – bitte entscheiden.

## 2026-11-20 – FERTIG: lb3-Rauchtest

Anlass: `antworten.md`, „20.11. 13:25“ – `supabase/tests/lb3_rauchtest.sql` brach nach der LB-3 Nachbesserung mit „Inzwischen wurde etwas anderes geändert.“ ab (Prüfung 6 machte den Sammelschritt rückgängig, nachdem Prüfung 5 schon einen neueren Plan-Schritt angelegt hatte; neue Regel Sollte 4).
**Nur die Testdatei geändert** (Stand `lernen-app` f1a0ad7 übernommen; kein App-Code, nichts in der Datenbank, kein Merge):
- Prüfung **6** (Rückgängig des Sammelschritts) läuft jetzt direkt nach Prüfung 4 – der Sammelschritt ist dann noch der jüngste Plan-Schritt (Prüfungen 2–4 legen keinen Plan-Schritt an). Prüfungen und Erwartungen von 6 unverändert (6c prüft weiter, dass die selbst gelandete Etappe mit Wiederholungsstufe 2 zurückkommt).
- Prüfung **5** (Rücknahme eines Flugs) danach: zuerst werden die 6 Flüge wieder gesetzt, dann wird einer zurückgenommen – gleiche Erwartung (keine gesetzte Landung, Stufe ○).
- Prüfungen 1–4 und 7–10 unverändert; die Meldungen „ok n“ erscheinen in der Reihenfolge 1, 2, 3, 4, 6, 5, 7, 8, 9, 10.
**Geprüft:** pglast ok. **Nicht ausgeführt** (Datenbank nur lesen) – bitte im nächsten Probelauf mit der Migration `lb3_nachbesserung`.

## 2026-11-20 – FERTIG: AB-A (App 0.83.0, Cache v149)

Gebaut im Zweig `bau-lehrer` auf `lernen-app` e71a72d (App 0.82.2) – ich war der einzige Chat am App-Code. Datenbank nur gelesen (für AB-A nichts). Kein Merge nach `main`, keine Kinderdaten.
Vorgabe: `inhalte/pruefung/kind/abschluss/umsetzung.md`, `entwurf/abschluss.html`, Zusätze von Sebastian in `AUFTRAEGE.md`. Server-Felder: AB-S (Meldung unten).
Bilder: `docs/previews/ab/` – Etappe `direkt`/`sauber`/`sturm` × `tag`/`nacht` (400 × 780) und Tablet 820, Flug geschafft (tag/nacht 400, tag 820), Ort geschafft, Bordkarte (gleicher Ort, Ortswechsel).

**Umgesetzt (nur Abflug-Gestaltung „tag“/„nacht“; die alte Gestaltung bleibt wie bisher)**
- **1 Etappe gelandet:** Vollbild über der Seite, drei Fassungen nach `landung.landung_art` (Ersatz `einheit_lesen.landungen`, sonst „sauber“ bei altem Server): Direktflug (Sonnenuntergang, Jet, Funken, „{ziel}/{ziel} AUF ANHIEB“, Abzeichen Direkt), Saubere Landung (Taghimmel, Landebahn, Chips Bordkarten · selbst gelöst · in Folge; bei `wieder_gelandet` „WIEDER GELANDET“), Sturmflug gemeistert (Gewitter, Durchbruch, Satz ohne Fehlerzahl mit „einmal/zweimal/mehrmals neu angesetzt“, Band „⚡ AUSDAUER-ABZEICHEN“). Blatt: „Du kannst jetzt“ (`kann` → „Kurz gesagt“ → Titel), ★ +Sterne, ein Satz zur Wiederholung, **ein** großer Knopf (Weiter: nächste Etappe · Weiter: Flug-Test „{k} Bordkarten, eine je Etappe, ohne Tipps“ · Zur Abflugtafel), Textlink „Pause – zur Abflugtafel“. Kein Weg zurück in die Übungen; die Adresse wird beim Landen durch `…-erklaeren` ersetzt (Zurück-Taste führt nicht in die Bordkarten).
- **Ablauf (Zusatz Sebastian):** Übungen → Knobel-Bordkarte von selbst → Abschluss-Ansicht. **Sturmflug:** Knobel kommt nicht von selbst, nur als kleiner Textlink im Blatt; danach wieder die Abschluss-Ansicht. Nach der letzten Pflicht-Etappe führt der Knopf zum Flug-Test.
- **2 Flug geschafft** (nach bestandenem Flug-Test bzw. vollständiger Korrektur, nicht nach Nachtests): Gold-Szene, Konfetti, je Etappe ein Licht, Sterne-Zähler (`sterne_flug.summe`) mit „Test r von g{, v verbessert}“, Liste „Das kannst du jetzt – n Etappen“, Wiederholungs-Kette, Knopf „Weiter zum nächsten Thema“, Textlink „Test ansehen“ (schließt die Ansicht; darunter die Antwortliste mit Teil 4/5f). „Überspringen ›“.
- **Bordkarte:** NEUES THEMA, ORT ✈ FLUG nr/von, Flugname, `kurz`, ETAPPEN · GEBIET · FLUG, Gate „ERKLÄRUNG“; „Boarding: {Titel}“ → `#/lerneinheit/{kind}-{einheit}-erklaeren-1` (Erklärung der ersten Etappe); „Später – zur Abflugtafel“. `naechster_flug: null` → „Alles geschafft, was im Plan steht …“ + „Zur Abflugtafel“. Alter Server ohne das Feld → Abflugtafel.
- **3 Ort geschafft** (`ort_geschafft`): Papier-Szene, Stempel „GESCHAFFT / ORT / Gebiet · Datum“, „REISEPASS · STEMPEL n“ (Konto neu geladen), „Alle k Flüge · ★ +100 Ort-Sterne“, „Deine Flüge in …“, Knopf „Weiter: neuer Ort“ → Bordkarte „NEUES THEMA · NEUER ORT“, „VON … ✈ NACH …“, „Abflug nach {Ort}“.
- **4 Bewegung:** nur CSS (+ Zähler), längste Bewegung 1,8 s (Funken und Konfetti gegenüber dem Entwurf verkürzt, damit 1,8 s eingehalten sind), Antippen der Szene beendet sie, bei „weniger Bewegung“ sofort Endzustand. Kein Ton.
- **Reisepass:** Zeile „⚡ Direkt n · ✓ Sauber n · ⚡ Ausdauer n“ aus `konto.abzeichen` (nur wenn der Server sie liefert).
- **H6 (LB-3 Nachbesserung, Sollte 6):** Der Tageszähler „heute selbst gelöst“ gilt bis `heute_bis` des Servers (unabhängig von Uhr und Zeitzone des Geräts); ohne `heute_bis` wie bisher.
- **Rückgängig (LB-3 Nachbesserung, Sollte 4):** Die App bietet nach einem Rückgängig keinen weiteren Schritt zurück an; lehnt der Server ab, steht dort „Rückgängig geht nur für die letzte Änderung …“ mit „Neu laden“.

**Getestet** (Playwright, Chromium; lernen 118 von 118; Suche 138 bestanden + Nr. 108 einzeln bestanden (bekannt wackelig), 9 bekannte alte Fehler 13, 15, 101, 103, 105, 111, 113, 126, 127; neu 6 Tests AB-A, angepasst 5 Tests aus Teil 4/5): drei Fassungen mit verschiedenen Szenen, je hell und nacht auf 400 × 780 ohne Scrollen, genau ein großer Knopf, kein Link in die Übungen, Adresse nach der Landung `…-erklaeren`; Sturmflug ohne Fehlerzahl und ohne Knobel von selbst, Knobel über den Textlink und zurück; Wieder gelandet; alter Server ohne `landung`; Reisepass-Zeile; Tablet 820; Bewegung ≤ 1,8 s, Antippen beendet, „weniger Bewegung“ ohne Animation; Flug → Bordkarte → Boarding öffnet `-erklaeren-1`; „Test ansehen“; Ort → Stempel → Bordkarte VON/NACH; ohne nächsten Flug.

**Nicht geprüft / offen**
- Gegen den echten Server nicht ausgeführt (AB-S-Felder nur nach der Feldbeschreibung nachgebildet).
- „Zurück-Taste führt zur Etappen-Übersicht“: umgesetzt als Ersetzen der Adresse durch `…-erklaeren`; die Taste selbst führt dann zur vorigen Seite (z. B. Abflugtafel), nie in die Bordkarten.
- Das Konfetti/Funken-Timing weicht leicht vom Entwurf ab (1,4 s bzw. 0,9 s statt 1,8 s/1,2 s), damit die Grenze von 1,8 s auch mit Verzögerung gilt.
- Echte Geräte, Safari und Bildschirmleser nicht geprüft.

## 2026-11-20 – FERTIG: LB-3 Nachbesserung (Server, Muss 1–3, Sollte 4–7)

Gebaut im Zweig `bau-lehrer` (Stand `lernen-app` e71a72d übernommen). Nur Migration und Rauchtests – kein `lernen.js`. **Nichts in der Datenbank ausgeführt**, nur gelesen: alle Einfügestellen im Live-Text geprüft (je genau einmal vorhanden). Kein Merge nach `main`.
**Bestand (lesend, 20.11.):** keine Route mit `kann_wdh_themen`, keine Karte mit `gesetzt_am`, 3 Plan-Schritte mit Karten-Lage → keine Bestandsänderung nötig.
**Migration** `supabase/migrations/20261120_lb3_nachbesserung.sql` (nach `lb3`, `i5`, `ab_s`; pglast ok; kein DROP/DELETE; wiederholt ausführbar).
**Rauchtest neu** `supabase/tests/lb3_nachbesserung_rauchtest.sql` (Rollback, nur Testkind, Flüge dynamisch aus dem Inhalt gewählt). **Angepasst:** `lb3_rauchtest.sql` (1c: selbst gelandete Etappe behält Landung/Herkunft, Wiederholung neu ab Stufe 1; 6c: Rückgängig stellt Stufe 2 wieder her), `i3_lernregeln_rauchtest.sql` (Sollte 7).
**Nicht ausgeführt** – weder Migration noch Rauchtests (Datenbank nur lesen). Bitte im Probelauf: Migration, dann `lb3_nachbesserung`, `lb3`, `i3`, `i2`, `i4`, `i5`, `ab_s`.

### Muss
1. **Setzen = alle Etappen ab Wiederholungsstufe 1.** `flug_wdh_setzen`: auch schon gelandete Etappen gehen auf Stufe 1, fällig am nächsten Lerntag; `sitzt_am`, eigene Lösungen, Belege bleiben, kein `gesetzt_am` (Herkunft selbst). Lage davor steht im Schritt (Rückgängig stellt sie her). Neu `karte_stand.wdh_gesetzt_am` (Beginn der Wiederholung durch Setzen, für Muss 3). Test M1: vorher ◉ → ↻ Wdh 1 von 5, am nächsten Lerntag fällig; Rückgängig → wieder ◉.
2. **Rücknahme/Rückgängig: nur belegte Landungen bleiben.** Gemeinsame Landeregel `schule.karte_landet(k)` (eigene Lösungen ≥ Ziel, Typen, schwere, Folge) – `karte_buchen` ruft sie jetzt auch auf. Damit sie für gesetzte Etappen etwas prüfen kann, zählt `karte_buchen` dort eigene Lösungen, Typen, schwere und Folge weiter (die Wiederholung läuft daneben unverändert). Rücknahme (`flug_wdh_zuruecknehmen`, auch beim Entfernen eines Ortes) und Rückgängig (`karten_wiederherstellen`): gesetzte Etappe bleibt nur bei `karte_landet`, sonst offen (`sitzt_am` null). Versuche, eigene Lösungen, Sterne bleiben. Tests: Fehler → offen; offener erster Anlauf → offen; eine richtige Wiederholung → offen mit 1 eigener Lösung; eigene Landung → bleibt (Herkunft selbst); dasselbe über Rückgängig (Setzen → Fehler → Rückgängig → offen).
3. **sicher nach dem Flug.** `karte_sicher`: steht der Flug auf „Kann er – aber wiederholen“ (oder ist die Etappe gesetzt), gilt für alle Etappen: gelandet + Wiederholung nach 14 Lerntagen + Mischkarte richtig, falls seit dem Setzen (`wdh_gesetzt_am`) eine **eingelöst oder beantwortet** wurde; nur vorgeladen zählt nicht. Test M3: selbst gelandete Etappe ohne Nachtest + gesetzte, Wiederholungen bestanden → alle sicher, Flug ◉; vorgeladen → bleibt sicher; eingelöst ohne richtige → ↻, mit richtiger → ◉.

### Sollte
4. `plan_setzen_intern`: `rueckgaengig` nur für den jüngsten Plan-Schritt (`route_aenderung`, anlass `plan`) des Kindes, sonst „Inzwischen wurde etwas anderes geändert.“ Test: A → B → A rückgängig abgelehnt, B rückgängig angenommen. **Folge für die App:** ein zweites „↶ Rückgängig“ hintereinander wird abgelehnt – die App bietet nur noch einen Schritt an (in AB-A, 0.83.0).
5. `thema_stufe`: „komplett“ gesetzt + wieder offene Etappe → Stufe ◉ bleibt, `hinweis: 'rueckfall'`, `wieder_offen` > 0.
6. `schule.heute_bis(kind)` = nächster Tagesbeginn in der Zeitzone des Kindes; `einheit_lesen_intern` und `uebung_pruefen_intern` liefern `heute_bis` neben `heute_tag`.
7. `i3_lernregeln_rauchtest.sql`: Ursache – der eindeutige Index `misch_ausgabe_offen_eindeutig` gilt für alle nicht eingelösten Ausgaben, **auch verfallene**; hat `mischkarten` im Test eine Ausgabe derselben Bordkarte angelegt und verfallen lassen, stieß das Einfügen von Hand darauf. Jetzt fügen beide Stellen mit `on conflict … do update` ein (wie `mischkarten` selbst); die Prüfung „zweite offene Ausgabe wird abgelehnt“ bleibt.

### Annahmen / nicht geprüft
- „Seit dem Setzen“ für Muss 3 = `wdh_gesetzt_am` (neu); für ältere gesetzte Karten ohne diesen Wert gilt `gesetzt_am`, sonst `sitzt_am`.
- „gezeigt“ einer Mischkarte = beantwortet (Versuch mit `misch`); eine Anzeige ohne Antwort speichert der Server nicht.
- Muss 2 „echte eigene Landung“ im Test über gesetzte Zähler (eigene Lösungen = Ziel, Typen, schwer, Folge 3) statt vieler Antworten.
- Nichts davon ausgeführt.

## 2026-11-20 – FERTIG: AB-S (Server: Abschluss nach Etappe, Flug und Ort)

Stand `lernen-app` 10a3155 in `bau-motivation` zusammengeführt. Nur Migration und Rauchtest – kein `lernen.js`, keine neue App-Version. Datenbank nur gelesen (alle Einfügestellen im Live-Text je einmal vorhanden;
`karte_buchen` lokal bytegleich nachgebaut, md5 = live). Kein Merge nach `main`.
**Migration** `supabase/migrations/20261120_ab_s_abschluss.sql` (nach `i4` und `i5`, von beiden unabhängig; nicht ausgeführt; pglast ok; kein DROP, kein DELETE, keine Bestandsänderung; wiederholt ausführbar).
**Rauchtest** `supabase/tests/ab_s_abschluss_rauchtest.sql` (Rollback, nur Testkind; über `uebung_pruefen_intern`, `test_starten_intern`, `test_abschliessen_intern`, `einheit_lesen_intern`, `konto`).

### Neu in der Datenbank
- `karte_stand.landung_art` (`direkt` | `sauber` | `sturm`, Check) und `karte_stand.landung` (jsonb, Zählung) – gesetzt in `karte_buchen` genau beim Landen (neue Funktion `schule.landung_speichern`), bei „wieder gelandet“ überschrieben.
  Gesetzte Landungen (LB-3) laufen nicht über `karte_buchen` → bekommen keine Art.
- `schule.landung_zaehlen(kind, flug, lernziel)` – nur lesen. Gezählt seit Beginn bzw. seit dem letzten „wieder offen“ (`geoeffnet_am`) bis `sitzt_am`; nur `pool = 'uebung'` dieser Etappe, ohne Mischkarten, Knobel, Expedition, Test.
- Schwellen in `schule.regel`: `landung_sauber_fehler_max` 2 · `landung_sauber_mehr_max` 4 · `landung_sauber_stufe_gesenkt_max` 0 · `landung_sauber_lerntage_max` **null (aus)** – siehe Offene Punkte.
- `testsitzung.ort_geschafft` (beim Abschluss festgehalten, damit „Test ansehen“ später dasselbe zeigt).
- Ablage für AB-I: `thema.kurz` und Tabelle `schule.etappe_text(thema_id, lernziel, kann, geaendert_am)`, PK (thema_id, lernziel), RLS an (wie alle `schule`-Tabellen, ohne Policy).
- Hilfsfunktionen: `schule.flug_im_ort`, `schule.flug_karte`, `schule.naechster_flug`, `schule.flug_abschluss`.

### Regel für `landung_art` (wie umgesetzt)
| Art | Bedingung |
|---|---|
| `direkt` | `bordkarten <= ziel`, `fehler_endgueltig = 0`, `mit_tipp = 0`, `zweite_versuche = 0` |
| `sauber` | sonst `fehler_endgueltig <= 2`, `stufe_gesenkt <= 0`, `bordkarten <= ziel + 4` (und Lerntage, falls die Regel gesetzt wird) – **oder** `wieder_gelandet` (Szene 1b) |
| `sturm` | alles andere |
Zählweise: `bordkarten` = Antworten ohne 2. Anlauf (je Bordkarte eine) · `fehler_endgueltig` = Wertung `falsch` (ein 1. Anlauf, nach dem der 2. Anlauf kommt, zählt nicht) · `mit_tipp` = Antworten ohne 2. Anlauf mit `hilfe > 0` ·
`zweite_versuche` = Antworten mit `anlauf = 2` · `stufe_gesenkt` = aus den Versuchen nachgerechnet wie in `karte_buchen` (jeder 2. Fehler in Folge, höchstens bis Stufe 2; im Zählfenster ab 0) · `lerntage` = verschiedene Tage (Zeitzone des Kindes) mit Versuchen im Zählfenster.

### Für AB-A (App): Felder
**1. Antwort auf eine Übung** (`schule_uebung_pruefen`) – neues Feld **`landung`** auf oberster Ebene, **nur** in der Antwort, mit der die Etappe gerade landet (nicht bei Wiederholung, Mischkarte, Knobel, nicht bei erneutem Senden derselben `client_id`):
```
landung: { landung_art: 'direkt'|'sauber'|'sturm', bordkarten: n, ziel: n, fehler_endgueltig: n, mit_tipp: n, zweite_versuche: n,
           stufe_gesenkt: n, lerntage: n, wieder_gelandet: bool, eigene_loesungen: n, folge_ziel: n, am: zeit, kann?: text }
```
- Direktflug: „{ziel}/{ziel} AUF ANHIEB“ · Saubere Landung: Chips `bordkarten` · `eigene_loesungen` selbst gelöst · `folge_ziel` in Folge; `wieder_gelandet` → Titel „WIEDER GELANDET“ ·
  Sturmflug: `bordkarten`, `stufe_gesenkt` (1 einmal · 2 zweimal · ≥3 mehrmals · 0 Einschub weglassen), `folge_ziel` – keine Fehlerzahl zeigen.
- `kann` fehlt, solange kein Text da ist (jsonb_strip_nulls der Antwort) → „Kurz gesagt“ bzw. Etappen-Titel.
- Die bisherigen Felder (`karte.neu_sitzt` usw.) bleiben; `landung` ist da, genau wenn `karte.neu_sitzt` aus einer eigenen Landung kommt.
**2. Reisepass** (`schule_konto`): `konto.abzeichen = { direkt: n, sauber: n, sturm: n }` (je Kind und Etappe die letzte Art).
**3. Flug lesen** (`schule_einheit_lesen`): `kurz: text|null` · `kann: { <lernziel>: text|null }` (alle Etappen aus `inhalt.etappen`) · `landungen: { <lernziel>: 'direkt'|'sauber'|'sturm' }` (nur Etappen mit gespeicherter Art; Ersatz, falls die Lande-Antwort fehlt).
**4. Test-Ergebnis** (`schule_test_abschliessen`, auch erneutes Lesen) – zusätzlich auf oberster Ebene; alle bisherigen Felder unverändert:
```
sterne_flug:   { test: n, summe: n }     test = Sterne dieses Tests; summe = Übungs-, Knobel- und Test-Sterne aller Versionen dieses Flugs (ohne Expedition, ohne Ort-Sterne)
kurz:          text|null                 Satz zum Flug
flug:          Bordkarte (s. u.) des gerade geschafften Flugs
etappen:       [{ lernziel, titel, kann: text|null }]   Reihenfolge wie inhalt.etappen – Liste „Das kannst du jetzt“, je Etappe ein Licht
ort_geschafft: bool                      Ort durch DIESEN Abschluss geschafft (war vorher nicht fertig) → Ort-Bildschirm
ort_sterne:    n                         gebuchte Ort-Sterne (100), sonst 0
ort_fluege:    [{ thema_id, titel, zustand }]           Flüge des Orts ohne abgewählte – „Deine Flüge in {Ort}“
naechster_flug: Bordkarte | null         nächster Flug laut Plan; null → „Alles geschafft, was im Plan steht …“
ort_wechsel:   bool | null               nächster Flug in anderem Ort → „VON … NACH …“, Knopf „Abflug nach {Ort}“
Bordkarte = { thema_id, einheit_id, titel, gebiet, kurz, block_id, ort, land, flug: { nr, von }, etappen: n, erste_etappe: { lernziel, titel } }
```
- „Boarding“ → `naechster_flug.einheit_id` + `erste_etappe.lernziel` (Erklärung der ersten Etappe).
- Plan-Reihenfolge für `naechster_flug`: Orte nach `position`, Flüge nach `block_thema.reihenfolge`; übersprungen: abgewählt, „kann schon“ (Flug oder Ort), „kann er – aber wiederholen“, ohne geprüften Flug, erledigt, der gerade geschaffte Flug; Orte `fertig`/`entfernt` zählen nicht.
- Stempel-Nummer „REISEPASS · STEMPEL {n}“ = `konto.stempel` nach dem Abschluss (Konto neu laden). „{v} verbessert“ bleibt App-Sache (wie im Entwurf).
**Alte App:** bekommt nur zusätzliche Felder; nichts entfernt oder umbenannt.

### Rauchtest `ab_s_abschluss_rauchtest.sql`
1 Direktflug (genau `ziel` Bordkarten; `landung` nur in der Lande-Antwort; gespeichert) · 2 Saubere Landung (1 Fehler, 1 Tipp, 1 zweiter Versuch) · 3 Sturmflug (3 Fehler, Stufe 1× gesenkt), Reisepass je +1 ·
4 wieder gelandet → `sauber`, nur Bordkarten seit dem Öffnen gezählt, Art überschrieben · 5 `einheit_lesen`: `kurz`, `kann` (fehlend = null), `landungen` ·
6 Flug-Test im eigenen Plan: `sterne_flug`, Ort geschafft (+100), `ort_fluege`, nächster Flug in anderem Ort, Flug 1 von 1 · 7 erneut gelesen: `ort_geschafft` bleibt, alte Felder da · 8 ohne weiteren Flug im Plan → `naechster_flug` null.
Hinweise für den Probelauf: Schritt 4 schiebt im Test `versuch.am` der Etappe zurück (in einer Transaktion ist `now()` fest). Etappen-Auswahl: nur Auswahl-Bordkarten (heute 6 Etappen passend, alle vom Testkind ungeübt).

### Bestand
43 gelandete Etappen (heute) bekommen **keine** nachträgliche Art (nichts erfunden); der Reisepass zählt ab dem Einspielen. Sitzungen, die vor dem Einspielen abgeschlossen wurden: `ort_geschafft` wird beim ersten Lesen festgehalten (dann meist `false`, weil der Ort schon fertig ist).

### Offene Punkte (bitte entscheiden)
1. **Widerspruch in `umsetzung.md`:** Tabelle 1c nennt „über mehrere Lerntage“ als Grund für Sturmflug, die Bedingungstabelle und die Freigabe (Abschnitt 7) nennen es nicht. Umgesetzt nach Freigabe: Lerntage zählen **nicht**
   (`landung_sauber_lerntage_max = null`). Soll „mehr als 1 Lerntag → Sturmflug“ gelten, genügt `update schule.regel set wert = '1' where schluessel = 'landung_sauber_lerntage_max'`.
2. „Wieder gelandet“ zählt im Reisepass als **Sauber**-Abzeichen (Szene 1b, `landung_art = 'sauber'`) und ersetzt die Art der ersten Landung derselben Etappe.
3. Direktflug mit `bordkarten <= ziel` statt `== ziel` (weniger als `ziel` ist praktisch unmöglich; so fällt kein Sonderfall in „Sturm“).
4. `ort_geschafft` setzt einen Plan-Eintrag des Orts voraus (ohne Route keine Ort-Sterne, also `false`).

### Gesehen/getestet
Lokale Nachbildung (PostgreSQL 16): Tabellen und Funktionen des Lande-, Test- und Misch-Pfads aus dem Live-Text abgeschrieben, Inhalte erfunden, `test_starten_intern` als vereinfachter Stub.
Migrationen `i4`, `i5`, `ab_s` je **zweimal** eingespielt ohne Fehler; Rauchtests **`i4` (5/5), `i5` (4/4), `ab_s` (8/8)** ohne Fehler. Dabei einen Fehler gefunden und behoben (Alias `r` kollidierte in `test_abschliessen_intern` mit einer Variablen).
**Nicht geprüft:** gegen die echte Datenbank nicht ausgeführt (Probelauf beim Haupt-Chat); echtes `test_starten_intern` nur gelesen; Laufzeit von `naechster_flug` (ruft `thema_stand` je Flug im Plan) nicht gemessen.

## 2026-11-20 – FERTIG: `thema_stufe` sieht den offenen Nachtragstest (Befund 20.11. 06:00)

**Migration** `supabase/migrations/20261120_i5_stufe_nachtragstest.sql` (nach `lb3`; Ersetzung im Live-Text, Stelle einmal vorhanden; wiederholt ausführbar; pglast ok). **Rauchtest** `supabase/tests/i5_stufe_nachtragstest_rauchtest.sql`.
- „Alle Etappen gelandet, aber Flug-Test noch nicht geschrieben“ gilt jetzt auch, wenn der Flug-Test geschrieben ist und eine Pflicht-Etappe in `lernziel_stand` noch `offen` steht – genau die Bedingung, unter der `test_starten_intern` seit W177 den Nachtragstest startet.
  Ergebnis im Fall aus dem Betrieb: `▶ dran`, `test_offen: true` (vorher `↻`, `false`). Gesetzte Flüge (LB-3) wie bisher ausgenommen. Ist die offene Etappe noch nicht gelandet: `▶` über „begonnen“, `test_offen: false`.
- Rauchtest: alles nachgewiesen → ↻ · offene gelandete Pflicht-Etappe → ▶, test_offen · Nachtragstest startbar · offene Etappe nicht gelandet → ▶ ohne test_offen. Lokal 4/4 (s. AB-S).

## 2026-11-20 – Nachtrag zu „Misch-Ausgaben wiederverwenden“
Unverändert gegenüber der Meldung darunter (Commit 78ca3c7, jetzt mit `lernen-app` 10a3155 zusammengeführt). Neu: Migration und `i4_misch_ausgabe_rauchtest.sql` in der lokalen Nachbildung ausgeführt – 5/5 ohne Fehler.
Reihenfolge zum Einspielen: `i4` → `i5` → `ab_s`.

## 2026-11-20 – FERTIG: Misch-Ausgaben wiederverwenden (Befund 20.11. 05:55)

Stand `lernen-app` c750ad2 übernommen. Nur Migration und Rauchtest – kein `lernen.js`, keine neue App-Version. Datenbank nur gelesen (I-3 eingespielt, `misch_ausgabe` hat 8 Zeilen; Ersetzungsstelle in `misch_buchen` einmal vorhanden). Kein Merge.
**Migration** `supabase/migrations/20261120_i4_misch_ausgabe_wieder.sql` (nach I-3; nicht ausgeführt; pglast ok; kein DROP, kein DELETE, keine Bestandsänderung; wiederholt ausführbar):
- neue Spalte `misch_ausgabe.verfallen_am`.
- `schule.mischkarten(kind, flug, anzahl)`: 1. offene Ausgaben dieses Kindes für einen **anderen Flug**, **älter als 24 Stunden** oder **nicht mehr gültig** (Etappe nicht mehr gelandet, Bordkarte gesperrt, Flug nicht mehr geprüft/freigegeben) → `verfallen_am = now()` (nicht löschen);
  2. die noch offenen Ausgaben **für diesen Flug** werden wieder ausgegeben (dieselben Karten, je Etappe höchstens eine, älteste zuerst); 3. **aufgefüllt** wird nur, wenn weniger als gewünscht offen sind, und nur aus Etappen ohne offene Karte
  (Auswahl wie bisher über `mischkarten_waehlen`; eine verfallene Ausgabe derselben Bordkarte wird dabei wiederbelebt statt eine zweite Zeile anzulegen – der eindeutige Index bleibt). Antwort im bisherigen Format (`einheit_id`, `quelle`, `stadt`, `etappe`), sortiert Flug → Kontinent → älter.
- `misch_gueltig` und `misch_buchen` zählen verfallene Ausgaben nicht.
**Rauchtests**
- neu `supabase/tests/i4_misch_ausgabe_rauchtest.sql` (Rollback, nur Testkind, eigene zwei gelandete Etappen, alle anderen im Test „nicht gelandet“): zweimal gelesen → dieselben Karten, keine neuen Ausgaben · eine eingelöst → die andere bleibt, nur die fehlende Etappe wird aufgefüllt ·
  anderer Flug → alte Ausgaben verfallen, offene = ausgelieferte · älter als 24 h → verfällt, neu ausgestellt · Etappe nicht mehr gelandet → Ausgabe verfällt, keine Karte mehr daraus.
- angepasst `i3_lernregeln_rauchtest.sql`: **S3d** prüft jetzt „zweimal ausgeliefert → dieselben Karten, offene Ausgaben = ausgelieferte Karten“ (hängt nicht mehr davon ab, wie viele Etappen gelandet sind);
  **S4a** wählt die Ausgabe gezielt (offen, nicht verfallen, dieser Flug). Damit braucht `i3` die I-4-Migration (Spalte `verfallen_am`).
- Durchgesehen, unverändert passend: `i2` (H10b: 25 h alte Ausgabe verfällt beim nächsten Ausliefern), `lb3`, `w176_t3`, `w176_h8`, `w176_h_muss`, `w176_h_sollte` – gelesen, nicht ausgeführt.
**Nicht geprüft:** Migration und Rauchtests nicht ausgeführt.

## 2026-11-20 – FERTIG: LB-3 Serverteil („Kann er – aber wiederholen“, „Wieder in die Wiederholung“, Sammelaktionen, 4 Stufen) – App 0.81.3

Auftrag I, Teil 3 war schon fertig (83da72d, Meldung darunter; Teil-3-Text in `lernen-app` 752acf0 unverändert) – nichts neu gebaut; LB-3 setzt darauf auf.
Zweig `bau-motivation`, Stand `lernen-app` 752acf0 übernommen. Kein Merge. Datenbank nur gelesen; alle Einfügestellen im Live-Text je einmal vorhanden.
**Migration** `supabase/migrations/20261120_lb3_kann_wiederholen.sql` (nach I-2 und I-3; nicht ausgeführt; pglast ok; kein DROP, kein DELETE, keine Bestandsänderung; wiederholt ausführbar).
**Rauchtest** `supabase/tests/lb3_rauchtest.sql` (Rollback, nur Testkind, nicht ausgeführt). Bisherige Rauchtests: keiner angepasst (Durchsicht: `karte_sicher`, `thema_stand`, `ort_stand`,
`flug_nachtest` verhalten sich ohne gesetzte Flüge wie bisher; `la_4`, `i2`, `i3`, `w176_*`, `w177` laufen damit unverändert – gelesen, nicht gesehen).

### Regeln (wie umgesetzt)
- **„Kann er – aber wiederholen“ setzen:** für jede Etappe des Flugs (aktuelle geprüfte/freigegebene Version, `inhalt.etappen`), die noch nicht gelandet ist: `sitzt = true`, Wiederholung Stufe 1
  (`wdh_stufe 0`, `wdh_lerntage 1`, fällig am nächsten Lerntag – genau wie nach einer eigenen Landung), Herkunft `karte_stand.gesetzt_am`/`gesetzt_von`. Schon gelandete Etappen und eigene Lösungen bleiben unberührt.
  Danach die bestehenden Regeln: Fehler → nächster Lerntag; zwei Fehler hintereinander → wieder offen (▶).
- **Kein Flug-Test, kein Nachtest** für diese Flüge: `test_starten_intern` (blocktest/nachtest) → `{ok:false, grund:'nichts_zu_testen', gesetzt:true}` (ein schon laufender Test bleibt fortsetzbar);
  `nachtest_stand` → `{faellig:false, grund:'gesetzt'}`; `flug_nachtest` → `null` („entfällt“).
- **„sicher“ für gesetzte Etappen:** gelandet + `wdh_stufe ≥ 4` (Wiederholung nach 14 Lerntagen bestanden) + Mischkarte richtig seit der Landung, **falls seit der Landung eine ausgegeben wurde** (`misch_ausgabe`); kein Nachtest.
- **Stand:** `thema_stand`/`ort_stand` zählen kann_wdh-Flüge als erledigt (gelandet), außer eine Etappe ist wieder offen → „läuft“/Ort offen.
- **Sterne:** keine Sterne für gesetzte Landungen (Landungen geben ohnehin keine Sterne). Ort-Sterne wie bei „kann schon“: Ist ein Ort dadurch komplett, wird er „fertig“ und `route_sterne` bucht die Ort-Sterne einmal.
- **Rücknahme** (Flug aus `kann_wdh_themen` genommen, Ort aus dem Plan genommen oder Flug auf komplett/abgewählt gestellt): gesetzte Landungen, bei denen das Kind **seit dem Setzen keinen Versuch** gemacht hat, werden aufgehoben
  (nicht gelandet, Wiederholung leer); mit eigenen Versuchen bleibt der Stand, nur die Herkunft „gesetzt“ fällt weg. Versuche, eigene Lösungen, Sterne bleiben; kein DELETE.
- **„Wieder in die Wiederholung“:** alle gelandeten Etappen des Flugs → Stufe 1, fällig am nächsten Lerntag; „gelandet“ (`sitzt`, `sitzt_am`) und alle Belege bleiben. Bei „Kann er komplett“ gesetzt
  (je Flug oder ganzer Ort) wird daraus „Kann er – aber wiederholen“ (Flug wandert von `kann_schon_themen` nach `kann_wdh_themen`; beim ganzen Ort werden die übrigen Flüge einzeln „komplett“).
  **Flug-Nachtests selbst geschaffter Flüge laufen unverändert weiter** (Begründung: sie prüfen den Flug als Ganzes und sind Teil von „sicher“; der Flug war nicht gesetzt). Ein bestandener Flug-Test bleibt.
- **Die 4 Stufen** (`schule.thema_stufe`, Reihenfolge der Prüfung): gesetzt komplett → ◉ · wieder offen oder Rückreise → ▶ · alle Etappen sicher → ◉ · Test läuft/Verbessern offen/alle gelandet, aber Flug-Test noch nicht geschrieben (nur ungesetzte Flüge) → ▶ ·
  gesetzt wiederholen oder alle gelandet → ↻ · etwas begonnen → ▶ · im Plan → ○ · sonst +.

### Für `bau-lehrer`: neue Felder und Aktionen
**Lesen – `schule_plan_lesen`**
- `kann_wdh: true` – Merkmal: der Server kennt LB-3 (Knöpfe „Kann er – aber wiederholen“ und „Wieder in die Wiederholung“ nur dann zeigen).
- `plan[].kann_wdh_themen: [thema_id]` – wie `kann_schon_themen`.
- `orte[].themen[].kann_wdh: bool` und **`orte[].themen[].stufe`** (für jeden Flug, auch nicht eingeplante):
  `{ stufe: 'komplett'|'wiederholung'|'dran'|'kommt'|'nicht_im_plan', zeichen: '◉'|'↻'|'▶'|'○'|'+', gesetzt: 'komplett'|'wiederholen'|null, im_plan: bool,
     etappen: n, begonnen: n, gelandet: n, sicher: n, wieder_offen: n, wdh_stufe_min: n|null, wdh_nr: 1–5|null („Wdh x von 5“), naechste_in: Lerntage|null (0 = fällig),
     rueckreise: bool, test_offen: bool, ohne_test: bool }`
- `verlauf[].schritt_id` (und `ereignis` ohne die Karten-Liste).
**Lesen – weitere:** `schule_lehrplan_uebersicht.themen[].stufe = {kind_id: <wie oben>}`; `schule_lernstand.einheiten[].thema_id`, `.stufe` und `.karten[].gesetzt`, `.karten[].gesetzt_am`
(Eltern: „gesetzt: kann er, wird wiederholt“); `schule_uebersicht.lernende[].route[].kann_wdh_themen`, `.stand[].ohne_test`; `schule_einheit_lesen.ohne_test`.
**Schreiben – `schule_plan_setzen`** (dieselbe Aktion, ein Aufruf = ein Schritt; mehrere Flüge aus verschiedenen Orten, auch Orte, die noch nicht im Plan stehen – einfach als Eintrag mitschicken):
- je Eintrag zusätzlich `kann_wdh_themen: [thema_id]` (Zustand; fehlt das Feld, bleibt die Liste) und `wieder_wdh_themen: [thema_id]` (Aktion, nur in diesem Aufruf).
- Die vier Einstellungen je Flug: **Lernen** = in keiner Liste · **Kann er – aber wiederholen** = `kann_wdh_themen` · **Kann er komplett** = `kann_schon_themen` · **Aus dem Plan nehmen** = `ausgelassen`.
  Schickt ein Eintrag denselben Flug in `kann_wdh_themen` und in `kann_schon_themen`/`ausgelassen` (oder `kann_schon: true` mit `kann_wdh_themen`), lehnt der Server ab
  („Ein Flug kann nur eine Einstellung haben …“). Schickt ein Eintrag `kann_wdh_themen` nicht mit (alte App), gehen komplett/abgewählt vor und der Flug fällt aus `kann_wdh_themen`.
- Antwort zusätzlich: **`schritt_id`** (und `karten_geaendert`, `karten_zurueck`).
- **Rückgängig:** `schule_plan_setzen` mit `rueckgaengig: <schritt_id>` **und** den Einträgen von davor (wie heute) und der aktuellen `revision`. Der Server stellt die Karten-Stände dieses Schritts wieder her
  (nur Etappen ohne eigene Versuche seither; einmal je Schritt) und wendet dann die Einträge an. So gilt eine Rücknahme für alle Flüge des Sammelschritts, auch für „Wieder in die Wiederholung“.
- Beispiel Sammelschritt: 6 Flüge aus Gym 7 → alle betroffenen Orte als Einträge mit ihren `kann_wdh_themen`, ein Aufruf; `schritt_id` merken für „↶ Rückgängig“.

### Rauchtest `lb3_rauchtest.sql`
6 Flüge Gym 7 in einem Aufruf → alle Etappen gelandet (selbst gelandete Etappe unberührt), Stufe ↻, heute nicht, am nächsten Lerntag fällig · kein Flug-Test/Nachtest, `flug_nachtest` null, `ohne_test` ·
Mischkarten aus gesetzten Etappen · zwei Fehler in der Wiederholung → wieder offen, ▶ · Rücknahme eines Flugs → ○ · Rückgängig des ganzen Sammelschritts (selbst gelandete Etappe und eigene Versuche bleiben) ·
doppelte Einstellung abgelehnt · „Kann er komplett“ → Wieder in die Wiederholung → ↻ · selbst geschafft ◉ → Wieder in die Wiederholung → ↻ (Wdh 1 von 5, Nachtests laufen weiter) → Rückgängig → ◉ · keine Geschenk-Sterne.
Der Weg geht über die neue innere Funktion `schule.plan_setzen_intern` (api ruft sie nach der Zugriffsprüfung); der äußere Zugang ist nicht getestet (Schlüssel).

### App 0.81.3 (nur Kinderseite, damit nichts ins Leere läuft)
Abflugtafel: gesetzte Flüge ohne „TEST BEREIT“ und unter „gelandet“, solange keine Etappe wieder offen ist; Testseite eines gesetzten Flugs: „Für diesen Flug gibt es keinen Test. Du wiederholst ihn nur …“.
Die alte App 0.81.2 bricht nicht (neue Felder werden ignoriert; ein Test-Start bei gesetztem Flug endet mit „Gerade gibt es nichts zu testen.“).
**Gesehen/getestet:** lernen 96 von 96 (neu: LB-3 Testseite ohne Test); Suche 139 bestanden, 9 Fehler – die bekannten alten (13, 15, 101, 103, 105, 111, 113, 126, 127).
**Nicht geprüft:** Migration und Rauchtest nicht ausgeführt; Laufzeit von `thema_stufe` für alle 95 Flüge × Kinder in `schule_plan_lesen`/`schule_lehrplan_uebersicht` nicht gemessen
(je Flug wenige kleine Abfragen; falls zu langsam, später als eine Abfrage je Kind); Lehrer-/Eltern-App für LB-1/2/5 baut `bau-lehrer`.

## 2026-11-20 – FERTIG: Auftrag I, Teil 3 (Nachprüfung ChatGPT 878) – App 0.81.2

Zweig `bau-motivation`, Stand `lernen-app` 23a8b6a übernommen. Kein Merge. Datenbank nur gelesen: I-2 ist eingespielt; `misch_ausgabe` hat heute **0 Zeilen, keine Dopplungen**;
keine Versuche mit `wertung_offen`. Ersetzungsstellen (`einheit_lesen_intern`, `test_starten_intern`) im Live-Text je einmal vorhanden.
**Migration** `supabase/migrations/20261120_i3_lernregeln_nachpruefung.sql` (nicht ausgeführt; pglast ok; kein DROP, kein DELETE, keine Bestandsänderung; wiederholt ausführbar; nach I-2).
**Rauchtest** neu `supabase/tests/i3_lernregeln_rauchtest.sql` (Rollback, nur Testkind, nicht ausgeführt).

**Muss**
1. **Endgültige Wertung festgehalten:** neue Spalte `versuch.wertung_fest` (`eigen | neutral | falsch | ersetzt`), geschrieben, sobald der Trigger entscheidet. `versuch_wertung` liest sie zuerst
   (also auch `folge_nachrechnen`). Ein 2. Anlauf, dessen 1. Anlauf schon endgültig falsch gebucht ist, gilt als `neutral` und bucht nichts – auch wenn er falsch ist.
   Rauchtest genau des Falls aus 878 (2 richtig, X falsch, Y richtig, X im 2. Anlauf richtig): Buchung 1 = Nachrechnung 1 (vorher 1 ≠ 3); Gegenstück mit falschem spätem 2. Anlauf: kein zweiter Fehler.
2. **Nachbuchen genau einmal:** neue Funktion `schule.offene_entscheiden(kind, ausser)` beansprucht offene erste Anläufe in einem Schritt
   (`update … set wertung_offen = false where id in (select … for update skip locked) returning`) und bucht nur die beanspruchten; der Trigger ruft sie auf.
   Rauchtest: zweimal entschieden → 1, dann 0; der Fehler steht einmal in `falsch`. Echte Gleichzeitigkeit (zwei Tabs) lässt sich im Rauchtest nicht erzeugen.

**Sollte**
3. **Einlösen atomar:** `misch_buchen` löst mit `update … returning` (Zeile mit `for update skip locked`) ein; nur wenn das eine Ausgabe trifft, gibt es die Mischkarten-Buchung, sonst normale Buchung.
   Eindeutiger Index `misch_ausgabe_offen_eindeutig` (offene Ausgabe je Kind und Bordkarte); die Migration bricht mit Meldung ab, falls beim Einspielen doch Dopplungen liegen (heute keine).
   `schule.mischkarten` legt Ausgaben mit `insert … on conflict … do update` an.
4. **Ausgabe an die Lage gebunden:** `misch_ausgabe.einheit_id` (gelesener Flug) und `lernziel` (erste noch nicht gelandete Etappe dieses Flugs beim Ausliefern). `misch_gueltig` vergleicht mit dieser Lage,
   nicht mit `aktuell_*` des Geräts. Ausgaben ohne Lage (aus 0.81.1, falls bis zum Einspielen welche entstehen) prüfen wie bisher die Geräte-Angaben.
   Hinweis: Weil Mischkarten nur aus gelandeten Etappen kommen und die gespeicherte Etappe die erste nicht gelandete ist, schließt der Vergleich vor allem gefälschte/veraltete Geräte-Angaben aus.
5. **30-Minuten-Grenze:** `einheit_lesen_intern` und `test_starten_intern` rufen `offene_entscheiden` auf. Rauchtest: über 30 Minuten alte erste Anläufe werden beim Lesen und beim Teststart entschieden, frische nicht.
6. **Tageswechsel (App):** Der Zwischenspeicher merkt sich zusätzlich den Gerätetag beim letzten Server-Stand. Ist auf dem Gerät seither ein neuer Tag (Seite über Nacht offen), gilt der alte Stand nicht mehr (0);
   eine Antwort ohne Karte (z. B. Mischkarte) zählt dann neu ab 1; der nächste Server-Stand (Laden oder Antwort) ersetzt alles, ein neuer Server-Tag verwirft den alten Stand. Test in Playwright.

**Bisherige Rauchtests – angepasst**
- `w176_t3_rauchtest.sql` und `w176_h8_rauchtest.sql`: rufen `misch_buchen` direkt bzw. legen Mischkarten-Versuche direkt an. Seit Teil 3 zählt das nur mit Ausgabe → vor jedem Aufruf wird eine Ausgabe angelegt
  (nur wenn die Tabelle existiert). In h8 sind die zwei Mischkarten-Versuche dafür zwei Anweisungen statt einer.
- Unverändert und nach Durchsicht weiter passend: `i2_lernregeln`, `w177_nachtragstest` (beide Blöcke), `w176_h_muss`, `w176_h_sollte`, `w176_t1`, `w176_t4`, `abgleich_ohne_expeditionen`, `i_pause`, `la_3`, `la_4`.
  Nicht ausgeführt – „läuft weiter“ ist hier gelesen, nicht gesehen.

**Alte App 0.81.1:** keine neue oder geänderte Aktion; Mischkarten kommen weiter über `schule_einheit_lesen`, `heute_selbst`/`heute_tag` unverändert.
**Gesehen/getestet:** lernen 95 von 95 (H6-Test um den Tageswechsel erweitert); Suche 138 bestanden, 10 Fehler – die bekannten alten (13, 15, 101, 103, 105, 111, 113, 126, 127) plus 108, der gelegentlich wackelt. pglast ok für Migration und alle geänderten Rauchtests; keine Variablen-/Alias-Doppelungen.
**Nicht geprüft:** Migration und Rauchtests nicht ausgeführt; Gleichzeitigkeit nur über die Sperr-Klausel abgesichert, nicht unter Last getestet; äußerer Zugang (api.*) nicht getestet (Schlüssel).

## 2026-11-20 – Rauchtest W177, zweiter Block berichtigt (Antwort 20.11. 04:30)

- `supabase/tests/w177_nachtragstest_rauchtest.sql`, Prüfung „FEHLER 7b“: `a.id = any((select aufgaben …))` las die Unterabfrage als Menge von Arrays → `bigint = bigint[]`.
  Jetzt werden die Aufgaben der Korrektur-Sitzung zuerst in `v_ids` gelesen, dann `a.id = any(v_ids)` – wie in Prüfung 5b. Sonst unverändert.
- Stand `lernen-app` übernommen. pglast ok, keine Variablen-/Alias-Doppelungen; in den übrigen Rauchtests kommt das Muster nicht vor. **Nicht ausgeführt** (keine Datenbank), kein Merge.

## 2026-11-20 – FERTIG: Auftrag I, Teil 2 (Lernregeln) – App 0.81.1

Zweig `bau-motivation`, Stand `lernen-app` 68a663d (Teil 1 und 1b enthalten) übernommen. Kein Merge. Datenbank nur gelesen (Funktionstexte, Stellen je einmal vorhanden geprüft).
**Migration** `supabase/migrations/20261120_i2_lernregeln.sql` (nicht ausgeführt; pglast ok; kein DROP, kein DELETE, keine Bestandsänderung; wiederholt ausführbar).
**Rauchtests** (nicht ausgeführt, Rollback, nur Testkind): neu `supabase/tests/i2_lernregeln_rauchtest.sql`; ergänzt `w177_nachtragstest_rauchtest.sql` (zweiter Block);
angepasst `w176_h_muss_rauchtest.sql` (H10a legt jetzt eine Ausgabe an – ohne sie wäre der alte Fall nach I-2 zu Recht keine Mischkarte mehr).

**Muss**
1. **H10 – Mischkarte serverseitig gebunden.** Neue Tabelle `schule.misch_ausgabe` (Kind, Bordkarte, ausgegeben am, eingelöst am). `schule.mischkarten` merkt jede ausgelieferte Karte
   (die bisherige Auswahl heißt jetzt `schule.mischkarten_waehlen`, unverändert); schon offene Ausgaben werden nur aufgefrischt. `misch_gueltig` verlangt zusätzlich eine
   ausgegebene, nicht eingelöste Ausgabe der letzten 24 Stunden; `misch_buchen` löst sie ein. `uebung_pruefen_intern` prüft einmal vor dem Speichern (sonst wäre die Ausgabe
   für die Antwort schon verbraucht). Ohne Ausgabe: normale Buchung als Übung, kein Misch-Beleg, kein `misch` in der Antwort.
   **App 0.80.0** holt ihre Mischkarten über `schule_einheit_lesen` → sie sind ausgegeben, der Ablauf bleibt gleich; sie bricht nicht.
   Rauchtest: gefälschter Kontext ohne Ausgabe und mit Ausgabe älter als 24 h → kein Beleg (Negativ); Flug lesen → Ausgabe → Antwort → Beleg, `misch.ok`, eingelöst (Positiv); dieselbe Karte zweimal → beim zweiten Mal kein Beleg.
2. **H2 – eine Regel für „endgültig falsch“.** `schule.versuch_wertung(versuch)` = `eigen | neutral | falsch | ersetzt | offen | test`: ohne zweite Chance oder im 2. Anlauf falsch → sofort `falsch`;
   falscher 1. Anlauf → `offen`, bis ein 2. Anlauf derselben Bordkarte kommt (`ersetzt`, der 2. Anlauf entscheidet) oder das Kind weitergeht bzw. 30 Minuten vergehen (`falsch`).
   Der Trigger `versuch_karte` bucht damit (`schule.versuch_buchen`) und merkt sich offene erste Anläufe (`versuch.wertung_offen`); beim nächsten Versuch des Kindes werden sie entschieden und,
   wenn endgültig falsch, nachgebucht. `schule.folge_nachrechnen(kind, einheit, lernziel, ab)` rechnet „folge“ mit derselben Regel nach (nur lesen).
   **Keine Bestandsänderung:** alte Zeilen haben `wertung_offen = null` und werden nie nachgebucht.
   **Verhaltensänderung in der laufenden Buchung:** Ein falscher 1. Anlauf, den das Kind liegen lässt, bricht jetzt die Folge (bisher wurde er nie gebucht).
   Rauchtest (Negativ): 2 richtig → 1. Anlauf falsch, liegengelassen → nächste richtig → Folge 1 (vorher 3); Nachrechnung = Buchung. Dazu: 1. Anlauf falsch + 2. richtig → Folge bleibt; ohne zweite Chance falsch → 0.

**Sollte**
3. **H4/H11/H14 – Tests** (im neuen Rauchtest): H4 Nachtest 4/5 bestanden, diese Etappe falsch → nicht „sicher“, Gegenprobe richtig → sicher. H11 über die ganze Buchung: Expedition-Teil zeigt auf eine
   neue Version des Flugs (im Test angelegt), Antwort über `uebung_pruefen_intern` bucht „angewandt“ auf die gelandete alte Version. H14: Teil a → „begonnen“, Unterbrechung mit Rückfall einer Voraussetzung,
   Teile b und c → „geschafft“, Sterne einmal, auch wenn Teil a wiederholt wird.
4. **H12 – Import:** `expedition_importieren` prüft jede angegebene Voraussetzung auch auf eine vorhandene Lernkarte (Lernziel mit Übungen, Flug nicht „ersetzt“), vor jedem Schreiben.
   Alle 21 vorhandenen Expeditionen erfüllen das (gelesen). Rauchtest: unbekannte Lernkarte → Fehler „Voraussetzung: Lernkarte …“, nichts geschrieben; gültige Datei läuft.
5. **H6 – Tageszähler:** Server liefert `heute_tag` (Kalendertag in der Zeitzone des Kindes, `schule.heute_tag`) in `schule_einheit_lesen` und in `schule_uebung_pruefen.karte`.
   App speichert `{tag, n, server}` und zeigt den Server-Zähler unabhängig vom Gerätetag; nur ohne Server-Tag (alter Server) zählt das Gerät nach seinem Tag.
6. **W177 – Nachtragstest** (Rauchtest ergänzt): offen + fehlerhaft zugleich → Nachtragstest nur für die offene Etappe, danach Korrektur nur für die fehlerhafte; Abbruch und Wiederaufnahme → dieselbe Sitzung,
   Antwort einmal gespeichert; Sterne vorher/nachher = richtige × Regel, zweiter Abschluss bucht nichts. Läuft der Nachtragstest, bekommt eine Korrektur-Anfrage den laufenden Test zurück (heutiges Verhalten, nur notiert).
   **Frist des nächsten Nachtests (nichts geändert – Sebastian entscheidet):** Der Nachtragstest ist technisch ein Flugtest (`blocktest`). Solange es **noch keinen Nachtest** gab, ist der Anker
   der letzte Abschluss eines Flugtests oder einer Korrektur → **die 10-Lerntage-Frist beginnt nach dem Nachtragstest (und nach jeder folgenden Korrektur) neu.** Gab es **schon einen Nachtest**,
   zählt die Frist ab diesem Nachtest weiter; der Nachtragstest verschiebt sie nicht. Solange eine Pflicht-Etappe offen oder fehlerhaft ist, ist ohnehin kein Nachtest fällig.
7. **H5/H13 – was wie getestet ist:**
   - Über die **innere Funktion** (Rauchtest, Rollback): alle Fälle oben – `schule.uebung_pruefen_intern`, `schule.einheit_lesen_intern`, `schule.mischkarten`, `schule.test_starten_intern`,
     `schule.test_abschliessen_intern`, `schule.expedition_importieren`; dahinter echte Trigger (`versuch_karte`, Sterne). Die Testsitzung für H4 und Testantworten im W177-Block werden direkt eingetragen.
   - Über den **äußeren Zugang** (`api.schule_*` mit Zugangsschlüssel, Edge-Funktion `lernen-api`): **nicht getestet** – braucht einen Schlüssel, der in keine Datei gehört. Die `api.*`-Funktionen sind unverändert
     und rufen genau diese inneren Funktionen nach der Zugriffsprüfung auf.
   - App: Playwright mit nachgebildeten Server-Antworten (H6).

**Gesehen/getestet:** lernen 95 von 95 (neu I-2/H6); Suche 138 bestanden, 10 Fehler – die bekannten alten (13, 15, 101, 103, 105, 111, 113, 126, 127) plus 108, der gelegentlich wackelt; keiner betrifft die Lern-Seiten. Migration und Rauchtests mit pglast geparst, keine Variablen-/Alias-Doppelungen; Ersetzungsstellen im Live-Text je einmal vorhanden.
**Nicht geprüft:** Migration und Rauchtests nicht ausgeführt. Die 30-Minuten-Grenze für „weitergegangen“ ist eine Annahme (im Rauchtest nur der Fall „andere Bordkarte“). Einzelne Ausgaben,
die nie beantwortet werden, bleiben als offene Zeilen in `misch_ausgabe` liegen (zählen nach 24 h nicht mehr; kein Aufräumen, weil kein DELETE).

## 2026-11-20 – Rauchtest „Abgleich ohne Expeditionen“ angepasst

- `supabase/tests/abgleich_ohne_expeditionen_rauchtest.sql`: setzt den gewählten Flug vor dem Abgleich auf `geprueft` (nur wenn er `freigegeben` ist; im Rollback, nichts bleibt) –
  wie beim Einspielen, weil Aufgaben freigegebener Einheiten unveränderlich sind. Sonst unverändert. pglast ok, nicht ausgeführt.

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

