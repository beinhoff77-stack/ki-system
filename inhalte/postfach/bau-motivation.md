# Postfach bau-motivation (Bau-Chat, Bau-Auftrag G / Werkstatt-Wunsch 176)

Neueste oben.

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

