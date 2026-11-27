# Nachprüfung Lehrer-Aufbau (LA-1 bis LA-7), App 0.80.0

Stand 2026-11-20. Geprüft wurde `main` 15d2c2d gegen zwei Vorgaben: `umsetzung.md` (dieser Ordner) und Auswahl des Nutzers 1A · 2B · 3B · 4A · 5A · 6B · 7A. Abweichungen laut `inhalte/postfach/bau-lehrer.md` (Zweig lernen-app) sind berücksichtigt.

Ich habe nur gelesen: kein App-Code, keine Datenbank, kein Merge geändert.

## So geprüft

- **Ablauf:** Die App aus `main` lief lokal. Die lernen-api war mit den erfundenen Daten der App-Tests nachgestellt (`laLage`, `laUebersicht`, `laPlan` aus `tests/lernen.test.cjs`):
  - Kind A: Klasse 5, lernt. „Runden“ wackelt.
  - Kind B: Klasse 7, kein Lerntag. Rückreise Pisa.
  - Dazu ein Testkind. Keine echten Kinderdaten, keine echten Namen.
- **Rollen:** Eltern über den App-Zugang, Lehrer über die eigene Lernen-Seite mit Lehrer-Code.
- **Breiten:** 400 × 860 (Handy), 820 × 1180 (Tablet), 1280 × 800 (Rechner).
- **Ablage:**
  - Skript: `nachpruefung.test.cjs`. Es läuft aus einem Ordner `pruef/` neben `tests/`.
  - Messwerte: `nachpruefung-messung.json`.
  - Bilder: `bilder-0800/<rolle>-<schritt>-<breite>.png`, mit Rolle `eltern` oder `lehrer`.
- **Live-Datenbank (nur gelesen):**
  - Die Migrationen LA-3 und LA-4 sind eingespielt (`20261118093905 w176_h_muss_h_sollte_la_3_la_4`).
  - `schule.besprochen`, `route.kann_schon_themen`, `besprochen_aktiv` und `thema_kann_schon` sind vorhanden.
  - `schule_lernstand` liefert `besprochen_am`, `fehler_gruende`, `regel` und `wdh_in`.

## Ergebnis je Paket

| Paket | Urteil | Bilder |
|---|---|---|
| LA-1 Gliederung (1A) | **erfüllt** | `*-2a-ueberblick-*`, `*-2b-wackelt-*`, `*-2c-stand-*`, `*-2d-plan-*` |
| LA-2 Startseite (2B) | **teilweise** | `*-1-start-*`, `*-1-start-ganz-*` |
| LA-3 Was wackelt (3B) | **teilweise** (auf dem Handy) | `*-3a-wackelt-offen-*`, `*-3b-besprochen-*` |
| LA-4 Flugplan (4A) | **erfüllt** | `*-2d-plan-*`, `*-3c-kann-schon-*` |
| LA-5 Geschafftes (5A) | **erfüllt** | `*-3f-geschafft-*` |
| LA-6 Einstellungen (6B) | **erfüllt** (Karte 2 nur im Mock leer) | `*-3d-einstellen-*` |
| LA-7 Nachschlagen (7A) | **teilweise** (auf dem Handy) | `*-3e-lehrplan-*` |
| Rollen: „Lernen starten“ / „Lernreise ansehen“ | **erfüllt** | `eltern-2a-…`, `lehrer-2a-…` |
| Texte für einen Lehrer ohne App-Kenntnis | **teilweise** | – |

### LA-1 Gliederung – erfüllt

**Gesehen**
- Startseite „Was ist los?“ mit Zu tun, Tabelle „Die Kinder“ und der Zeile Nachschlagen (Lehrplan · Expeditionen · Meine Aufträge · So funktioniert’s). „So funktioniert’s“ steht zusätzlich oben rechts.
- Kind-Seite `#/kind/<id>-<reiter>` mit den Reitern Überblick · Was wackelt · Stand · Plan.
- Kopf der Kind-Seite: Name, „Gymnasium · Klasse 5“, „⚙ Einstellen“, „Lernreise ansehen ›“ (Lehrer) bzw. „Lernen starten ›“ (Eltern), „So funktioniert’s“.
- Alte Adressen leiten in allen drei Breiten und beiden Rollen richtig um:
  - `lernstand/1` → `kind/1-stand`
  - `wackelt/1` → `kind/1-wackelt`
  - `plan/1` → `kind/1-plan`
  - `lernstand/1-rs_by` → `kind/1-stand-rs_by`
  - `lernstand/1-gym_by-7` → `kind/1-stand-gym_by-7`
- `#/schulstand` ist noch erreichbar, aber nirgends verlinkt (erlaubt).
- **Überblick:** Die vier Fragen beantwortet je eine Karte (Tablet und Rechner 2 × 2, Handy untereinander). Die Farbe stimmt: „Lernt es?“ ist grün bei Kind A und rot bei Kind B. Darunter steht „Zuletzt geschafft“.
- Jeder Reiter beantwortet seine Frage oben auf der Seite: Überblick = Lage, Was wackelt = Tabelle der Etappen, Stand = Kontinente × Klassen, Plan = Reihenfolge und Abdeckung.

**Auffällig**
- Bei Kind B steht unter „Wo hakt es?“ zuerst „Nichts wackelt.“ und direkt darunter „Rückreise Pisa – Nachtest nicht bestanden“. Das liest sich widersprüchlich (Kann).

### LA-2 Startseite – teilweise

**Gesehen, stimmt**
- Zu tun in der Reihenfolge rot, rot, gelb, blau:
  1. Kind B: kein Lerntag in den letzten 4 Wochen → `kind/2-ueberblick` (Reiter Überblick)
  2. Kind B: Rückreise Pisa – Nachtest nicht bestanden → `kind/2-plan` (Reiter Plan)
  3. Kind A: „Runden“ wackelt (5 falsch) → `kind/1-wackelt-1.runden` (Reiter Was wackelt, Etappe schon aufgeklappt = 1 Tipp)
  4. Neue Antwort auf euren Auftrag → `lernauftraege`
- Tabelle mit den Spalten Kind · Lernt · Wackelt · GYM · RS · IB · Jetzt · ⚙. „Lernt“ und „Wackelt“ sind gefärbt: Kind B rot/rot, Kind A grün/gelb. Zeile antippen → `kind/2-ueberblick`.
- IB bei Klasse 5: „noch kein MYP-Jahr“. Kind B Klasse 7: „MYP-Jahr 2“, passend zur neuen Regel Klasse − 5.
- Handy: Karten statt Tabelle, kein Querrollen auf der Startseite.
- Unterkante der Tabelle ohne Rollen:

| Breite | Lehrer | Eltern | Fenster | sichtbar? |
|---|---|---|---|---|
| Tablet 820 | 865 px | 1057 px | 1180 px | beide ja |
| Rechner 1280 | 790 px | 1057 px | 800 px | Lehrer ja, Eltern nein |

**Abweichend**
1. Stand-Zellen (GYM, RS, IB) sind ohne Ampelfarbe. Die Vorgabe verlangte rot/gelb/grün wie im Entwurf. Das ist eine bewusste Abweichung des Baus mit plausibler Begründung: Mitte des Jahres wäre fast alles rot. Der Nutzer sollte sie bestätigen.
2. „Pausen/Reisetage“ als Ausnahme für rot fehlt (Abweichung 4 laut Bau). Auf der Weltreise wird „kein Lerntag seit 3 Tagen“ an Reisetagen rot, obwohl alles in Ordnung ist.
3. Eltern: Über „Zu tun“ steht der Kasten „Wartet auf dich – Kind A möchte ‚Eis‘ einlösen“. „Zu tun“ ist damit nicht mehr oben, und auf dem Rechner (800 px hoch) passt die Tabelle nicht ohne Rollen. Besser als eigener Eintrag in „Zu tun“ (Sollte).
4. Tablet: Die Rahmenlinie der Zelle „⚙ Einstellen“ sitzt nicht auf der Zeilenlinie (`lehrer-1-start-820`). „noch kein MYP-Jahr“ bricht in vier Zeilen um (Kann).
5. Die Spaltenüberschrift heißt „AKTIONEN“; die Vorgabe sah nur ⚙ vor (Kann).

### LA-3 Was wackelt – teilweise

**Gesehen, stimmt**
- Kopfzeile „Diese Woche: 30 Bordkarten, 22 richtig, 4-mal mit Tipp · 2 Lerntage“.
- Tabelle mit den Spalten Etappe (Ort darunter) · richtig / falsch · häufigster Fehler · seit. „Wackelt“ steht zuerst.
- „falsch gerundet (2×)“ erscheint erst ab 2 gleichen Gründen, sonst „–“ (Abweichung 5 des Baus).
- Aufgeklappt: die letzten falschen Antworten (Aufgabe · Antwort · richtig), „Kurz gesagt: …“, „Erklärung ansehen ›“ und „Besprochen ✓“.
- „Besprochen ✓“ sendet `schule_notiz_setzen {lernender_id, besprochen: {einheit_id, lernziel}}`. Danach steht in der Zeile „besprochen 20.11.“. Die Erklärung unter der Tabelle nennt die Regel in einem Satz.

**Mangel**
- **Handy 400 px:** Die Tabelle ist zu schmal. Wörter brechen mitten im Wort („Rund-en“, „wac-kelt“, „Welc-hen Wert hat eine Ziffer ?“). Die Spalte „seit“ ist abgeschnitten, im Reiterband auch „Plan“. Auf einen Blick ist das nicht lesbar (`lehrer-3a-wackelt-offen-400`). Muss.

**Vermutet, nicht selbst gesehen**
- Dass die besprochene Etappe nach dem Neuladen aus „Zu tun“ verschwindet und nach einer neuen endgültig falschen Antwort zurückkommt: Der Mock speichert nichts. Belegt ist das nur durch den App-Test „LA-3: besprochene Etappe …“ und den Rauchtest des Baus. Den Rauchtest habe ich nicht ausgeführt.

### LA-4 Flugplan – erfüllt

**Gesehen**
- Zwei Spalten auf Tablet und Rechner, auf dem Handy untereinander.
- Kopf „Gymnasium Kl. 5 · 2 offen · 0 geschafft · Alles gespeichert · ↶ Rückgängig“.
- Ort aufgeklappt:
  - Je Flug Häkchen „im Plan“ links, Klassen, Stand, rechts „kann schon“ und „ansehen“.
  - „alle Flüge: kann schon“ und „Entfernen“.
- „Kann schon“ bei „Ganze Zahlen“ speichert `kann_schon_themen: [16]`. Der Ort zeigt danach „1/2 Flüge“, der Flug zählt also im Stand mit.
- Lehrplan rechts:
  - Reiter Gymnasium · Realschule · IB MYP.
  - Klassen 5–10 und „alle“, vorbelegt mit 5.
  - Zeile „Klasse 5: 2 von 3 Flügen im Plan“ mit Balken.
  - Eingeplante Orte grau mit ✓, fehlende mit ⠿ und „+“.
- Höhere Klasse: Am Ort steht „Klasse 6 – über der Klasse des Kindes · Kind sieht ihn unter ‚Später‘“. Auf dem Tablet wird der Satz mit „…“ abgeschnitten (Kann). Die Flugzeile „Gym 8 – höhere Klasse“ belegt nur der App-Test; im Mock kam sie nicht vor.

### LA-5 Geschafftes – erfüllt

**Gesehen**
- Ein fertiger Ort fehlt in der Liste. Kopf „1 offen · 1 geschafft“. Der Block „Geschafft (1)“ ist zugeklappt.
- Je Flug: „gelandet: 12.11. · Nachtest: fällig in 6 Lerntagen · nächste Wiederholung: in 1 Lerntag“.
- Satz darunter: „Die Reihenfolge der Lernreise bleibt …“.

**Auffällig**
- Ein Flug ohne Inhalt im fertigen Ort steht mit „gelandet: – · Nachtest: – · nächste Wiederholung: –“ unter Geschafft. Besser wäre „noch kein Inhalt“ (Kann).

### LA-6 Einstellungen – erfüllt

**Gesehen**
- „⚙ Einstellen“ mit Text an der Tabellenzeile/Karte und im Kopf der Kind-Seite.
- Das Blatt „Kind A einstellen“ kommt auf dem Handy von unten.
- Karten: Schule (Schulart, Klasse 5–10, „Bestimmt seine Klasse in Lernreise und Plan.“) · Stand messen gegen … · Notizen und Verlauf (zugeklappt) · Neuer Plan aus Lehrplan-Vorlage.
- Plan-Seite ohne Klasse, Stufen und Notizen.

**Nicht gesehen**
- Karte 2 zeigte im Mock „Kommt, sobald die Datenbank Stufen je Schulart liefert.“, weil die Testdaten kein `stufen` enthalten.
- Live gibt es die Spalte `lernender.stufen`; dort sollte die Auswahl erscheinen. Den Satz für den IB-Fall belegt nur der App-Test LA-6.

### LA-7 Nachschlagen – teilweise

**Gesehen**
- Tabelle mit Reitern Schulart. Klassen-Knöpfe mit Marken der Kinder („Kl. 5 A“, „Kl. 8 B“), „alle Klassen“, Suche.
- Zähler „Flüge · fertig · in Prüfung · fehlt“, die zugleich filtern.
- Spalten Flug · Ort · andere Schularten · Inhalt (●/◐/○) · Spalte je Kind. Gruppiert nach „Klasse 5 · Zahlen“.
- Tablet und Rechner ohne Querrollen.

**Mangel**
- **Handy:** Die Tabelle ist 660 px breit bei 368 px Platz. Inhalt und Spalten der Kinder liegen außerhalb, „Ath-en“ und „Ro-m“ brechen um (`lehrer-3e-lehrplan-400`). Laut Vorgabe nur fürs Tablet verlangt, daher Sollte.

**Nicht gesehen**
- „Gym 5 passt auf einen Tablet-Bildschirm“: Der Mock hatte nur 2 Flüge. Belegt ist es durch den App-Test LA-7 (14 Flüge).

### Rollen – erfüllt

**Gesehen**
- **Eltern:** „Lernen starten“ in jeder Zeile/Karte und im Kopf der Kind-Seite (4× auf der Startseite: 2 Kinder × Zeile/Karte). Kein „Lernreise ansehen“.
- **Lehrer:** kein „Lernen starten“, nirgends. Im Kopf der Kind-Seite steht „Lernreise ansehen ›“.
- **Verwalten:** Lehrer sehen nur „Testkind (zum Ausprobieren)“. Eltern sehen zusätzlich Zugänge, Eigene Lernen-Seite und die Belohnungen.

### Texte – teilweise

**Gesehen**
- Die Reisewörter sind auf „So funktioniert’s“ erklärt (Kontinent, Ort, Flug = Mathe-Thema, Etappe, Bordkarte). Die Zu-tun-Farben und „wackelt“ sind erklärt. Die Sätze sind kurz und ohne Programmiererwörter.

**Mängel**
- Ein Lehrer, der die App nicht kennt, sieht auf Startseite und Kind-Seite „Etappe“, „Rückreise“, „Nachtest“, „Bordkarten“ und „kann schon“, ohne Erklärung an Ort und Stelle. Die Erklärung steht nur auf „So funktioniert’s“. Meinung: Ein kleines „?“ oder ein Satz beim ersten Vorkommen von „Rückreise“ und „Etappe“ würde reichen (Sollte).
- Drei Texte nennen „die Datenbank“:
  - Blatt: „Kommt, sobald die Datenbank Stufen je Schulart liefert.“
  - Stand: „Gezählt werden vorerst nur Flüge mit Inhalt; alle Flüge kommen, sobald die Datenbank sie liefert.“
  - Expeditionen: „… sobald die Datenbank sie liefert.“

  Laut Code erscheinen sie nur, wenn ein Feld fehlt. Live fehlt es vermutlich nicht (vermutet). Wenn doch, ist „Datenbank“ ein Entwicklerwort (Kann).
- „AKTIONEN“ als Spaltenkopf (Kann).

## Mängel

### Muss
1. **Was wackelt auf dem Handy:** Wörter brechen mitten im Wort, die Spalte „seit“ ist abgeschnitten. Auf dem Handy als Liste je Etappe zeigen, wie die Kinder-Karten der Startseite.

### Sollte
1. **Pausen/Reisetage für rot** nachziehen, oder bis dahin „rot ab 3 Tagen“ als bewusste Entscheidung bestätigen. Auf Reisen wird sonst ständig rot gemeldet.
2. **Eltern-Startseite:** „Wartet auf dich“ (Belohnung) als blauen Eintrag in „Zu tun“ statt darüber. Dann passt die Tabelle auch auf dem Rechner ohne Rollen.
3. **Lehrplan-Übersicht auf dem Handy:** als Liste oder mit fester erster Spalte.
4. **Reisewörter beim ersten Vorkommen** kurz erklären („Rückreise = Wiederholung nach nicht bestandenem Nachtest“, „Etappe = Lernschritt“).
5. **Stand-Zellen ohne Ampel:** der Nutzer bestätigt die Abweichung, oder die Ampel kommt so, dass sie zur Jahreszeit passt.

### Kann
1. Überblick Kind B: „Nichts wackelt.“ und die Rückreise nicht direkt untereinander. Zum Beispiel „Keine Etappe wackelt · Rückreise Pisa offen“.
2. Geschafft: Flug ohne Inhalt als „noch kein Inhalt“ statt dreimal „–“.
3. Tablet-Tabelle: Rahmen der ⚙-Zelle ausrichten. „noch kein MYP-Jahr“ kürzer, zum Beispiel „– (ab Kl. 6)“.
4. Spaltenkopf „AKTIONEN“ weglassen.
5. Hinweis „über der Klasse des Kindes“ im Plan auf dem Tablet nicht abschneiden.
6. Hinweise mit „Datenbank“ durch neutrale Sätze ersetzen.

## Nicht geprüft
- **Die echte Live-Seite mit Anmeldung:** Mir fehlt ein Code. Alles lief lokal aus `main`; die Daten waren erfunden.
- **Ob 0.80.0 live ausgeliefert wird:** nicht gesehen. `sw.js` auf main nennt 0.80.0.
- **Reiter „Plan“ für Kind B:** Der Mock liefert immer den Plan von Kind A; die Seitenüberschrift lautete deshalb „Flugplan Kind A“. Ob der rote Eintrag „Rückreise Pisa“ live den Plan von Kind B zeigt und die Rückreise dort sichtbar ist, ist offen.
- **RS-Prozent in der Tabelle:** Im Mock steht überall „–“, weil die Testdaten keine RS-Zuordnung haben. Live nicht geprüft.
- **Echte Fehlerarten (`grund`) und „Kurz gesagt“ in allen Etappen:** nur im Mock gesehen.
- **Besprochen und „kann schon“ dauerhaft gespeichert:** Rauchtests nicht ausgeführt; die Datenbank habe ich nur auf vorhandene Spalten und Funktionen geprüft.
- **Ziehen mit Finger oder Maus im Plan:** nicht erneut geprüft; der App-Test deckt es ab.
- **Tablet quer** (1180 × 820) und dunkle Gestaltung.
