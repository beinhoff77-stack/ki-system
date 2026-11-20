# Antworten des Haupt-Chats

Neueste oben.

## 2026-11-14 14:50 – an alle
- `lernen-app` ist ein Zweig im Repository `beinhoff77-stack/ki-system`, kein eigenes Repository.
- Die App kann zeichnen (Koordinatensystem, Figur, Säulen-/Kreisdiagramm, Tabelle, Boxplot, Baumdiagramm) und allgemeine Lücken (Bruch, Zahlenpaar, Punkt). Details: `inhalte/README.md`.
- Gerundete Ergebnisse brauchen `toleranz` in `o`.

## 2026-11-14 15:30 – an inhalte-ib: klasse bei Themen ohne Lehrplan-Zuordnung
Einverstanden: `"klasse": {"zusatz": 10}` für daten.normalverteilung, finanzen.zinseszins, sonder.logik, zahlen.schranken. Weiterarbeiten wie angenommen. Ob der Import den Schlüssel verträgt, prüfe ich beim Einspielen; falls nicht, passe ich das Prüfskript bzw. den Import an, nicht deine Dateien.

## 2026-11-15 11:40 – an alle Bau-Chats: App-Wünsche für Zeichnungen umgesetzt (ab App 0.72.4)
Koordinatensystem kann jetzt zusätzlich: Graph-Arten `tan`, `betrag`, `glocke`; x-Achse in Vielfachen von π (`"pi": true`); Kreise (`kreise`), Vektorpfeile (`pfeile`),
gefüllte Bereiche (`flaechen`, z. B. zulässiger Bereich der linearen Optimierung). Reine Geometrie hat jetzt wirklich gleichen Maßstab (Kreise sind rund).
Polstellen (tan, Hyperbel) werden nicht mehr durch eine senkrechte Linie verbunden. Beschreibung: inhalte/README.md, Abschnitt „Zeichnungen“.
Noch nicht umgesetzt: Matrix-Darstellung, Intervall auf dem Zahlenstrahl, Körper-Zeichnung (Quader/Zylinder/Kegel), Urnen, Simulationsknopf, Antworttyp Lösungsmenge.

## 2026-11-16 03:20 – an pruefung-rueckmeldung-lernweg: Paket R1 ist im Zweig lernen-app (App 0.73.1), Nachprüfung kann laufen
- V1 Flächen: `.lern-zeichnung .flaeche` und gefüllte Bruchstreifen jetzt deckend mit Kontur – hell #B58500 auf Weiß (3,3:1), dunkel #8A6A00 auf #151B24 (3,4:1). Hunderterfeld hell und dunkel angesehen.
- V5: Nach einem Fehler wandert die Aufgabe ans Ende der Warteschlange; als Nächstes kommt eine andere, ungelöste Aufgabe derselben Stufe (falls vorhanden).
- V6 (Datenbank, Migration supabase/migrations/20261116_w150_r1_wiederholung_stufe_zurueck.sql, eingespielt): neue Spalte schule.karte_stand.wdh_fehler.
  1. Fehler bei „sitzt“: wdh_stufe − 1 (mindestens 0), faellig_am = Zeitpunkt + 1 Tag, sitzt bleibt. 2. Fehler hintereinander: zurück auf üben. Richtig dazwischen setzt den Zähler zurück.
  Mit dem Testkind in einer zurückgerollten Transaktion nachgestellt: sitzt → 2× richtig (Stufe 2) → Fehler (Stufe 1, morgen fällig, sitzt bleibt) → richtig (Stufe 2) → 2 Fehler (zurück auf üben).
- V7: Ende der Wiederholung mit Haken nur bei „alles richtig“, sonst „N Karte(n) brauchen noch Übung – morgen kommen sie wieder.“; „FAST – KURSKORREKTUR“ nur bei Zahl-Aufgaben, sonst „NOCH NICHT“; Tipp „zählt nicht für die Serie“.
- V10: Auswahl nach dem Prüfen: richtige Option grün mit ✓, gewählte falsche rot mit ✗ (Üben und Wiederholen).
- V11: lernZahl mit „−“; Lücken-Lösung „□x + □“ mit −1 → „−3x − 1“ (auch „− −1“ → „+ 1“); Kurs-Grafik ohne Komma in der Zeile ohne Nachkommastellen.
- Nicht in R1: Tests/Nachtests (V10 dort nicht eingebaut), R2 und R3 folgen.

## 2026-11-16 03:55 – an pruefung-rueckmeldung-lernweg: Paket R2 ist im Zweig lernen-app (App 0.73.2), Nachprüfung kann laufen
- V3 (Datenbank, Migration 20261116_w150_r2_fehlermuster_zweiter_versuch.sql, eingespielt): antwort_bewerten liefert bei falsch `grund`:
  vorzeichen (Betrag stimmt; bei Lücken: alle Beträge stimmen), komma (Faktor 10/100/1000 bzw. 0,1/0,01/0,001), vertauscht (Lücken: richtige Zahlen, falsche Felder),
  gerundet (±1 % oder auf weniger Nachkommastellen gerundet), falsche_einheit (wie bisher). uebung_pruefen_intern gibt grund weiter.
  Die App zeigt dazu einen Satz als erste Zeile der Rückmeldung (LERN_GRUND in lernen.js). „FAST – KURSKORREKTUR“ nur noch bei Zahl-Aufgaben mit erkanntem Muster, sonst „NOCH NICHT“.
- V2: Üben schickt `anlauf` 1 bzw. 2 (neue Spalte schule.versuch.anlauf). 1. Fehler: keine Lösung, kein Lösungsweg, keine Buchung auf die Lernkarte (Serie bleibt),
  Meldung „Noch nicht – du hast einen zweiten Versuch.“ plus Satz aus V3, sonst der Tipp, sonst ein allgemeiner Satz; Eingabe bleibt änderbar.
  2. Versuch richtig: zählt wie „mit Hilfe“ (Serie steigt nicht). 2. Versuch falsch: Lösung, Lösungsweg, Detektiv, Serie 0.
  Ausnahme: Auswahl-Aufgaben mit nur zwei Antworten haben keinen zweiten Versuch. Wiederholen und Tests unverändert (ohne anlauf verhält sich die Datenbank wie bisher).
  Mit dem Testkind in einer zurückgerollten Transaktion nachgestellt (grund-Fälle, Serie bleibt nach 1. Fehler, steigt nicht nach richtig im 2. Versuch, 0 nach 2. Fehler).
- V8: Nach 2 falschen Aufgaben derselben Karte hintereinander: „Leichtere Aufgabe“ (falls eine ungelöste mit kleinerer Stufe da ist) und „Beispiel ansehen“ (öffnet die Erklärung);
  nach 3 zusätzlich „Frag Mama oder Papa – sie sehen im Lernstand, wo es hakt.“ Elternansicht: Die Karte erscheint wie bisher oben unter den wackelnden Karten,
  sobald sie mindestens 3 Fehler und mehr Fehler als Richtige hat – eine eigene neue Markierung dafür gibt es nicht.
- Hinweis: Im 1. Fehlversuch speichert die Datenbank die falsche Antwort (für die spätere Auswertung echter Fehler, R4).

## 2026-11-16 04:25 – an pruefung-rueckmeldung-lernweg: Paket R3 ist im Zweig lernen-app (App 0.73.3), Nachprüfung kann laufen
- V9 (Datenbank, Migration 20261116_w150_r3_wiederholung_lerntage.sql, eingespielt): Abstände 1/3/7/14/30 jetzt in Lerntagen.
  Neue Spalten schule.karte_stand.wdh_ab und wdh_lerntage; neue Funktion schule.karte_faellig(k). Fällig = so viele Mathe-Lerntage nach wdh_ab;
  der heutige Tag zählt mit, sobald er ein späterer Kalendertag ist (sonst würde eine Karte erst nach der ersten Aufgabe des Tages fällig).
  schule_wiederholung, schule_lernstand und etappen_stand fragen karte_faellig. Karten, die vor der Umstellung „sitzen“, laufen bis zur nächsten Buchung nach altem Kalenderdatum weiter.
  Mit dem Testkind in einer zurückgerollten Transaktion nachgestellt (braucht 3 Lerntage: nur heute → nicht fällig; 2 Lerntage + heute → fällig).
- V9 (App): höchstens eine Runde mit bis zu 6 Wiederholungen vor dem Thema. Ist die Runde heute gemacht (gemerkt je Kind auf dem Gerät), führt der Startknopf ins Thema;
  der Rest steht als Link „Noch N Wiederholungen offen – wenn du magst“ auf der Startseite und als Link auf dem Bildschirm nach „Lernkarte sitzt“.
  Die 6 ist die Konstante LERN_WDH_RUNDE in lernen.js (Vorschlag aus dem Papier; Sebastian kann eine andere Zahl nennen). Die Datenbank liefert ohnehin höchstens 6 je Abruf.
- V12: „Was kommt wann wieder?“ – Kindansicht: aufklappbar auf der Startseite und am Ende der Wiederholung; Elternansicht (Lernstand): aufklappbar, mit „N Lernkarten sitzen, M davon sind dran“.
  Zum Nachtest steht dort nur die Regel in Worten; Zahlen je Kind zum Nachtest zeigt die Ansicht (noch) nicht.
- Abweichung: „Restliche fällige Wiederholungen werden nach dem Üben angeboten“ ist als Link umgesetzt, nicht als eigener Schritt.

## 2026-11-16 03:16 – an pruefung-rueckmeldung-lernweg: Entscheidungen von Sebastian
- V9: Es bleibt bei höchstens 6 Wiederholungen vor dem Thema.
- Freigabe Datenauswertung (für R4): Ja. Der Prüf-Chat darf in etwa 3–4 Wochen die echten falschen Antworten der Kinder nur lesend auswerten
  (Kinder nur als Kind A / Kind B nennen, nichts ändern). R4 startet erst danach.
- R1–R3 sind seit 16.11. live (App 0.73.3).

## 16.11. – Neue Regel „Lernkarte sitzt“ (Entscheidung Sebastian) – App 0.73.6
- 6 Punkte statt 2–4 (bei weniger Übungen entsprechend weniger, mindestens 2). Richtig im ersten Versuch ohne Hilfe: +1; Fehler: −2 (nicht mehr zurück auf 0).
- Zusätzlich muss mindestens eine Stufe-3-Übung im ersten Versuch ohne Hilfe richtig sein (falls die Karte Stufe-3-Übungen hat).
- Die App wählt die Stufe nach Punktestand: erstes Drittel leicht, zweites mittel, drittes schwer. Wiederholungen bevorzugen Stufe 2/3.
- Neue Lernkarte: erst Erklärung, dann Aufgaben (0.73.5). Karten, die schon sitzen, bleiben unverändert.
- Migration: supabase/migrations/20261116_w150_sitzt_regel_6_mit_schwer.sql (eingespielt).
- Zehnte Runde (Durchsicht je Jahrgang + schwerere Aufgaben nach Prüfungsvorbild) steht in inhalte/AUFTRAEGE.md; Zweige schwer-kl5 … schwer-kl10.

## 16.11. – Gesamtauftrag Umbau, Phase 1 fertig (App 0.74.0, Zweig lernen-app, nicht live)
Grundlage: inhalte/pruefung/UMBAU-AUFTRAG.md (Zweig pruefung-kinderansicht).
- Erklärungen A2, A5–A9, A12 und Rückmeldung R1: waren schon umgesetzt (0.73.0–0.73.3, siehe Meldungen oben). Unverändert.
- Kinderansicht K1:
  - U1 Band bis zum Stempel zählt alle Etappen aller Flüge des Ortes („Noch 29 Etappen bis zum Stempel von Rom (5 Flüge)“); ab 15 Etappen als Balken.
  - U2 Mein Weg und Merkheft zeigen den Flugnamen statt des Ortsnamens; „Etappe 4 von 8“.
  - U3 „Kommt noch“ wie die Abflugtafel: eigene Klasse / „Aus früheren Klassen – zum Auffrischen“ / „Später – für höhere Klassen“; Orte ohne Klasse nur unter „Später“.
  - U4 Menü markiert im Reisepass „Reisepass“.
  - U5 Flug-Kopf zeigt nur die eigene Schulart („ROM · Gymnasium · Klasse 5“); Eltern/Lehrer sehen weiter alle drei.
  - U8 Rückreise-Karte auf der Abflugtafel („KURZ ZURÜCK NACH …“, Grund, „Danach geht es weiter mit …“); bei Stoff aus früheren Klassen im Plan ein kurzer Hinweis.
  - Reisewörter in allen Kindertexten (beide Gestaltungen): Flug, Etappe, Bordkarte, Kontinent/Ort. Eltern-/Lehrer-Ansichten und Code behalten die bisherigen Namen.
- Zusätzlich seit der letzten Prüfung (Entscheidungen Sebastian 16.11.): neue Etappe zeigt zuerst die Erklärung (0.73.5); „sitzt“ erst nach 6 Punkten und einer schweren Bordkarte (0.73.6).
- Nachgestellt: rundgang.test.cjs läuft durch (5 von 5); in den Kindertexten kein „Lernkarte“, „Aufgabe“, „Thema“, „Gebiet“ mehr (ein Treffer ist Inhalt: „Maßstab auf Karten und Plänen“).
- D1 (Klassen-Zuordnung): Auftrag steht als „Elfte Runde“ in inhalte/AUFTRAEGE.md, Zweig daten-klassen. Noch nicht gestartet.
- Phase 2 (K2 Mein Weg, A1/A3/A4 und R2 sind bereits umgesetzt) folgt nach der Nachprüfung.

## 16.11. – Runde 9 und 10 eingespielt
- Zweige aufgaben-auffuellen und schwer-kl5 … schwer-kl10 nach lernen-app zusammengeführt (Stand 973ac27). Alle 90 Themendateien: inhalt_pruefen OK.
  Eigene Gegenprüfung: In allen 63 geänderten Dateien ist jede alte Aufgabe unverändert enthalten, Lernkarten unverändert; dazu kommen nur Übungen der Stufen 2 und 3.
- Eingespielt mit einheit_abgleichen(…, 'lassen'): 3 068 neue Aufgaben (Runde 10: 2 516 Übungen, davon 1 677 Stufe 3 und 839 Stufe 2; Runde 9: je 184 Aufgaben für drei Themen).
  Keine vorhandene Aufgabe geändert oder gelöscht, Lernstände unberührt.
- Stand danach (67 freigegebene Gymnasium-Themen, 455 Lernkarten): 9 940 Übungen, im Schnitt 21,8 je Karte (vorher 15,6); 4 035 Stufe-3-Übungen (vorher 2 262).
  Unter 12 Übungen oder unter 4 Stufe-3-Übungen liegen nur noch die Karten von zahlen.natuerlich (Einheit 1, kein Generator) → Auftrag „Zwölfte Runde“ in AUFTRAEGE.md.
- Die Befundlisten der Klassen-Chats (falsch eingestufte oder fehlerhafte alte Aufgaben) sind noch nicht abgearbeitet.

## 16.11. – D2 (Klassen-Zuordnung) umgesetzt, bis auf einen Umzug
Freigabe Sebastian: alles wie im Vorschlag (inhalte/pruefung/klassen/vorschlag.md, Zweig daten-klassen). Migration supabase/migrations/20261116_w150_d2_klassen_zuordnung.sql, eingespielt.
- Ortsklassen: Vancouver 8, Cusco 8, Teheran 7, Marrakesch 7, Timbuktu 5, Rio 5, Brasília 10, Santiago 10, Adelaide 6, New York 6; Alexandria heißt „Kreis“.
- Umzüge: Zehnerpotenzen Rom → Paris, Ortslinien Alexandria → Kairo. Schrägbilder und Simulation gelten am Gymnasium als Klasse 10 (neues Feld thema.klasse_fest).
- geometrie.winkel heißt „Mit Winkeln rechnen“. inhalte/themenliste.json angeglichen.
- Folge im Plan des Kindes der Klasse 5: Alexandria (jetzt nur Klasse-7-Stoff) aus dem Plan genommen; Ortslinien liegen in Kairo, das im Plan steht.
- OFFEN: Umzug „Lineare Gleichungen“ Delhi → Samarkand und damit Delhi → Klasse 8. Grund: Ein Kind hat Samarkand schon abgeschlossen; der Flug würde dort als erledigt gelten. Wartet auf Sebastian.
- Folgeaufträge: „Vierzehnte Runde“ (neuer Flug Winkelsätze Klasse 7 in Addis Abeba, Vertiefungen, Lehrplan-Reihenfolge) und „Bau-Auftrag Phase 2 und 3“ in inhalte/AUFTRAEGE.md.
- Nachprüfung Phase 1 (NACHPRUEFUNG-2026-11-16.md) gelesen: K1 bestätigt; neue Befunde N1–N5 stehen im Bau-Auftrag Phase 2 (Schritt A).

## 16.11. – D2 Teil 2 umgesetzt (Entscheidung Sebastian: A und ja)
Migration supabase/migrations/20261116_w150_d2_teil2_lineare_gleichungen.sql, eingespielt.
- „Lineare Gleichungen“ liegt jetzt in Samarkand (nach „Terme umformen“); Delhi ist Klasse 8 und heißt „Lineare Ungleichungen“. Kein Ort hat mehr Flüge mit abweichender Gymnasium-Klasse.
- Samarkand ist bei dem Kind, das es schon abgeschlossen hatte, wieder offen (Sterne bleiben).
- Plan Klasse 8: Cusco nicht mehr „kann schon“; Darwin und Brasília (Klasse 10) hinter die Orte der Klasse 9 gerückt.

## 16.11. – Zwölfte Runde eingespielt (zahlen.natuerlich, Rom)
Zweig schwer-natuerlich zusammengeführt (Stand a1558f6), inhalt_pruefen OK. Lernkarten in Datei und Datenbank identisch. Eingespielt mit einheit_abgleichen(…, 'lassen'):
334 neue Aufgaben, 2 vorhandene mit gleicher Frage angeglichen. Je Lernkarte jetzt 20 freigegebene Übungen, davon 8–10 Stufe 3 (vorher 2 freigegebene Übungen je Karte, der Rest war gesperrt).

## 16.11. (nachmittags) – E-1, Dreizehnte und Vierzehnte Runde zusammengeführt und eingespielt
Zweige bau-eltern, befunde, daten-klassen-2 nach lernen-app zusammengeführt (Stand 8eaab9c). App 0.74.1, nicht live. tests/lernen.test.cjs: 18 von 18. inhalt_pruefen: 92 von 92 OK.
- **Phase 1 (E-1) fertig:** Flugplan speichert sofort mit „Rückgängig“ und „Neu laden“ bei Versionskonflikt; Info-Seite „So funktioniert’s“ (#/info) mit der aktuellen Regel
  „sitzt nach 6 Punkten und einer schweren Bordkarte“; Reisewörter in allen Eltern-/Lehrertexten. Bericht: inhalte/postfach/bau-eltern.md. Keine Datenbank-Änderung.
- **Dreizehnte Runde (Befundlisten):** 63 Themen mit einheit_abgleichen(…, 'sperren') eingespielt: 317 Aufgaben angeglichen (296 umgestuft, 21 berichtigt), 99 neu (95 Ersatz + 4),
  die 95 ersetzten alten Fassungen gesperrt. Jede Etappe hat weiter mindestens 3 freie Übungen je Stufe. 42 Befunde nicht umgesetzt (begründet), Liste „für Sebastian“ in inhalte/postfach/befunde.md.
- **Vierzehnte Runde:** Vertiefungen gekennzeichnet (geometrie.winkel: kreuzung; abbildungen.kongruenz: verschiebung, drehung, parkett; raum.schraegbilder: lage, koordinaten).
  Neuer Flug „Winkelsätze“ (Thema 98, Einheit 92, Addis Abeba, 8 Etappen, 224 Aufgaben) als ENTWURF importiert – Freigabe durch Sebastian offen.
  inhalte/themenliste.json: 4 Themen ergänzt, lehrplan_gym gefüllt, neues Feld reihenfolge (nur Gymnasium).
- **Korrektur zu D2:** Die Zuordnung Thema ↔ Ort steht zusätzlich in schule.block_thema; das hatten Teil 1 und 2 nicht mitgezogen (drei Themen wichen etwa 7 Stunden ab).
  Nachgezogen mit supabase/migrations/20261116_w150_d2_teil3_block_thema.sql; Prüfung danach: 0 Abweichungen. Dazu 20261116_w150_d2_thema_winkelsaetze.sql (Themen-Eintrag 98).
- Bau-Auftrag Phase 2 und 3 kann starten (Schritt A = N1–N8).

## 17.11. – App 0.74.1 live; Entscheidungen zu Winkelsätzen und zur Liste „für Sebastian“
- 0.74.1 (Phase 1 vollständig: K1, E-1, Reisewörter überall) ist auf main.
- Neuer Flug „Winkelsätze“ (Einheit 92): bleibt Entwurf, bis ein Prüf-Chat ihn angesehen hat; danach Freigabe.
- Liste „für Sebastian“ (befunde.md): Bogenmaß in funktionen.trig ergänzen; Median und Spannweite (Klasse 6) als Vertiefung; vier Erklärungen ergänzen; SsW-Aufgaben mit Zeichnung;
  Zinseszins bleibt in Klasse 9. Auftrag „Fünfzehnte Runde“ in inhalte/AUFTRAEGE.md, Zweig nacharbeit.

## 17.11. – Schritt A (N1–N8) zusammengeführt; Prüfberichte E-1 und Winkelsätze gelesen
- Zweig bau-phase2 (Schritt A, App 0.74.2) nach lernen-app zusammengeführt (Stand fc30671), tests/lernen.test.cjs 24 von 24. Nicht live. Nachprüfung N1–N8 kann laufen.
- Nachprüfung E-1: alle vier Prüfpunkte erfüllt. Die sechs Befunde gehen als Zusatz an den Bau-Chat (inhalte/AUFTRAEGE.md, „Zusatz zum Bau-Auftrag Phase 2“);
  die beiden Datenbank-Punkte (geschafft geht bei Entfernen/Rückgängig verloren; Positionen wachsen) kommen mit der E-2-Migration.
- Flug „Winkelsätze“: beide Prüfungen „nicht freigabereif“. Bleibt Entwurf. Nachbesserung als „Sechzehnte Runde“ (Zweig winkelsaetze-2); Außenwinkel wird Vertiefung.

## 17.11. – Fünfzehnte Runde eingespielt; Schritt B (K2) zusammengeführt; Nachprüfung N1–N8 gelesen
- Zweige nacharbeit und bau-phase2 (Schritt B) nach lernen-app zusammengeführt (Stand 50b17bd). App 0.74.3, nicht live. tests/lernen.test.cjs 26 von 26; inhalt_pruefen für alle Themendateien OK.
- Fünfzehnte Runde eingespielt (7 Themen, einheit_abgleichen 'sperren'): funktionen.trig 56 neue Bogenmaß-Übungen und ergänzte Erklärungen; daten.kennwerte: modal_spannweite und median Vertiefung;
  ergänzte Erklärschritte in geometrie.grundbegriffe, geometrie.ortslinien, trigo.allgemein, gleichungen.lgs3; geometrie.konstruktion: 6 SsW-Aufgaben mit Zeichnung (alte Fassungen gesperrt).
  Themendatei geometrie.ortslinien trägt jetzt block_id 83 (Kairo) wie die Datenbank.
- Nachprüfung N1–N8: N3–N8 erfüllt, N2 nicht erfüllt (87 „Kurz gesagt“ mit zwei Sätzen), N1 teilweise (Abblenden, Steigungsdreieck). → „Zusatz 2 zum Bau-Auftrag Phase 2“ (Schritt A2)
  und „Siebzehnte Runde“ (Inhalte) in inhalte/AUFTRAEGE.md.
- Schritt B: Die App ordnet Flüge im Ort nach dem Feld reihenfolge, sobald schule_uebersicht es liefert; die Migration dazu schreibt der Bau-Chat mit Schritt C.

## 17.11. – Selbst-Check: UR, Siebzehnte und Sechzehnte Runde eingespielt; Bau Schritt A2 + C zusammengeführt; Migrationen E-2/E-3 eingespielt
Stand lernen-app 2d0d164, App 0.74.5, nicht live. tests/lernen.test.cjs 34 von 34 (ein Test an den neuen Inhalt angepasst: Steigungsdreieck der Kerze jetzt 2 Einheiten breit). inhalt_pruefen 92 von 92 OK.
- **Paket UR (Realschule/IB):** 24 Themen, 130 Lernkarten im neuen Muster; Aufgaben unverändert. Eingespielt, Themen bleiben ENTWURF (für Kinder unsichtbar).
- **Siebzehnte Runde:** kein Merksatz der Gymnasium-Themen war zu lang (die gemeldeten liegen in den RS/IB-Themen); Steigungsdreiecke in funktionen.linear 2 Einheiten breit mit passendem Text;
  überdeckte Beschriftungen versetzt (8 Themen). Eingespielt.
- **Sechzehnte Runde (Winkelsätze):** zwei Chats haben parallel nachgebessert. Eingespielt ist die Fassung vom Zweig winkelsaetze-2 (zuerst fertig, alle Zeichnungen maßstäblich);
  die zweite liegt ungenutzt auf winkelsaetze-2-alt. Einheit 92 bleibt ENTWURF bis zur Nachprüfung.
- **Bau-Chat:** Schritt A2 (N1/N2/N7) und Schritt C (E-2, E-3) zusammengeführt.
- **Migrationen eingespielt** (Werkstatt-Sperre, Dateien per Prüfsumme gegen das Repository abgeglichen): 20261117_w150_e2_plan_fluege_abwaehlbar.sql und 20261117_w150_e3_auftraege_bezug.sql.
  Danach geprüft: neue Spalten da, schule_uebersicht liefert thema_id/reihenfolge/ausgelassen, Pläne der Kinder unverändert (64 Einträge), entfernte Einträge stehen bei 1 000 001–1 000 037.
- Offen: Nachprüfung A2/B/C und Winkelsätze; Schritt D (K3, K4, E-4) des Bau-Chats; RS/IB: Merksätze (103 zu lang), schwere Bordkarten, Lehrplan-Abgleich, Freigabe.

## 17.11. – Schritt D (Phase 3) zusammengeführt, Migration D eingespielt; Nachprüfung 0.74.5 gelesen
- Zweig bau-phase2 (Schritt D: K3, K4, E-4) nach lernen-app zusammengeführt (Stand b7c4078), App 0.74.6, nicht live. tests/lernen.test.cjs 38 von 38 (K4-Test stabilisiert: wartete nicht auf die fertige Seite).
- Migration supabase/migrations/20261117_w150_d_stufen_stand.sql eingespielt (Werkstatt-Sperre, per Prüfsumme gegen das Repository abgeglichen). Danach geprüft: 68 Themen mit Lehrplan-Reihenfolge,
  lernender.stufen vorhanden, die vier Funktionen tragen die neuen Felder; bis_sitzt liefert plausible Zahlen (neueste Etappen: 8 und 9 Bordkarten bis „sitzt“).
- Nachprüfung 0.74.5 (NACHPRUEFUNG-2026-11-17.md): A1–A12, R1–R3, N5–N7, K1/K2, D2, E-1 bis E-3 nachgestellt und umgesetzt. Neue Befunde M1–M9 → „Zusatz 3 zum Bau-Auftrag“ (Schritt E).
  M4 mit echten Daten geprüft: Im Plan des Kindes der Klasse 5 steht kein Klasse-8-Ort (Cusco stammt aus den Testdaten); Adelaide (Klasse 6) steht bewusst im Klasse-6-Teil des Plans.
- Damit sind alle Pakete des Gesamtauftrags gebaut: Phase 1 (A, R1, K1, E-1), Phase 2 (K2, E-2, E-3, R2), Phase 3 (K3, K4, E-4, R3). Offen: Schritt E, Nachprüfung von D, R4, Inhalte.

## 17.11. – Nachprüfung Phase 2 (A2, K2, E-2, E-3) und Winkelsätze – Meldung des Prüf-Chats, von Sebastian weitergegeben
Der Prüf-Chat (Zweig pruefung-phase2) konnte nicht pushen; seine Meldung hier im Wortlaut der Ergebnisse:
- A2 (N1/N2/N7): erfüllt. „Kurz gesagt“ ist noch an einer Stelle zu lang: bei funktionen.reihen hält die App „: 2.“ für eine Aufzählung.
- K2: erfüllt, ein Befund: Die Karte wählt die Orte nach block.ziel_klasse und beachtet die Schulart nicht. Der Reiter „Stand“ rechnet dagegen mit jahrgang[schulart].
  Bei RS- und IB-Kindern zeigen Karte und Stand deshalb unterschiedliche Orte.
- E-2: erfüllt, ein Befund: Wählt man den letzten offenen Flug eines Ortes ab, zählt der Stempel sofort. Der Ort wird aber nie „fertig“, weil das nur beim Abschluss eines Tests gesetzt wird.
  Er bleibt also „dran“, und die Ort-Sterne fehlen.
- E-3: erfüllt. Noch keine Rückmeldung in der Datenbank, deshalb nicht im Echtbetrieb geprüft.
- Winkelsätze: alle Punkte beider Befundlisten behoben, Prüfskript OK, 209 beschriftete Winkel höchstens 3° Abweichung. Neu: Sicherungsaufgabe zum Sechseck („Auf welchen Satz stützt sich der Beweis …“) –
  die Auswahl „Winkelsumme im Viereck ist 360°“ ist ebenfalls richtig. Nach dieser Korrektur freigabereif.
- Geprüft mit tests/lernen.test.cjs (34 von 34), eigenen Skripten über 593 Merksätze, alle Schrittbilder und die Winkelsätze-Datei; Datenbank nur gelesen; API mit Kind-Code nicht prüfbar.
Folgen (Haupt-Chat):
- Winkelsätze: Generator korrigiert (Stand eb6a852): Bei „stützt sich auf“ erscheinen Sätze über Vielecke mit weniger Ecken nicht mehr als falsche Auswahl; beim Stufenwinkel-Satz nicht mehr
  „Scheitelwinkel“ (derselbe Fehlertyp). Datei neu erzeugt, inhalt_pruefen OK, Entwurf in der Datenbank ersetzt (11 Aufgaben der Etappe beweisen neu gezogen). Wartet auf Sebastians Freigabe.
- Die drei App-Befunde stehen als „Zusatz 4 zum Bau-Auftrag“ (P1–P3) in inhalte/AUFTRAEGE.md.

## 17.11. – Winkelsätze freigegeben; Themen-Einträge für drei neue Flüge; Achtzehnte Runde
- Entscheidung Sebastian („alles so, wie du sagst“): Winkelsätze freigeben, „Live“ erst nach Schritt E, Inhalte: zuerst Lücken, dann RS/IB.
- Flug „Winkelsätze“ (Einheit 92, Addis Abeba, vor „Konstruktionen“) ist freigegeben: 8 Etappen, 224 Aufgaben.
- Migration supabase/migrations/20261117_w150_luecken_themen_quito.sql eingespielt: neuer Ort Quito (Klasse 6, Kontinent „Fläche und Raum“, block_id 114) und drei Themen-Einträge –
  messen.flaechen_vielecke (99, Quito), messen.volumen (100, Quito), messen.prisma_zylinder (101, Cusco). Noch ohne Inhalt.
  Hinweis: Cusco hat damit einen zweiten Flug ohne Inhalt; der Ort gilt erst als abgeschlossen, wenn auch dieser Flug da und geschafft (oder abgewählt) ist.
- Auftrag „Achtzehnte Runde“ (Teil A: drei neue Flüge, Zweig luecken-neu; Teil B: fehlende Etappen je Klasse, Zweige luecken-kl5 … luecken-kl10) in inhalte/AUFTRAEGE.md.
- Die Meldung „Nachprüfung 0.74.5“ (M1–M9) des Prüf-Chats ist schon als „Zusatz 3 zum Bau-Auftrag“ beim Bau-Chat; M4 wurde mit echten Daten geprüft (kein Klasse-8-Ort im Plan der Klasse 5).

## 17.11. – Schritt E zusammengeführt (App 0.74.7), Migration P3 eingespielt; K3/K4: Vergleichszahlen aus echten Daten
- Zweig bau-phase2 (Schritt E: M1–M9, P1–P3) nach lernen-app zusammengeführt (Stand f8f069d), tests/lernen.test.cjs 46 von 46. Nicht live.
- Migration supabase/migrations/20261117_w150_e_ort_fertig_bei_abwahl.sql eingespielt (Werkstatt-Sperre, Prüfsumme gegen das Repository). Pläne der Kinder unverändert.
- Zum Wunsch „K3 und K4 vorziehen“ (Prüf-Chat, 17.11.): K3 und K4 sind seit Schritt D gebaut (0.74.6) – Mini-Linien GYM · RS · IB auf der Abflugtafel, „Mein Weg · Stand“ in drei Ebenen,
  Eltern-Seite „Stand über Schularten“ (#/schulstand) mit Prozent je Klasse, Feld stufen je Kind (speichert sofort seit Schritt E). Bitte gegen die Vorgabe des Prüf-Chats nachprüfen.
- Vergleichszahlen nach der Rechenregel „Stand“, direkt aus der Datenbank gerechnet (gelandet = Ort geschafft, „kann schon“ oder alle Pflicht-Etappen des Flugs erledigt; alle Flüge der Klasse zählen,
  auch ohne Inhalt), Stand 17.11. mittags:
  - Kind A · Gymnasium: Kl. 5 1/14 = 7 % · Kl. 6 0/11 · Kl. 7 0/9 · Kl. 8 0/14 · Kl. 9 0/14 · Kl. 10 0/9
  - Kind A · Realschule: Kl. 5 1/15 = 7 % · Kl. 6 0/10 · Kl. 7 0/14 · Kl. 8 0/9 · Kl. 9 0/13 · Kl. 10 0/11
  - Kind A · IB MYP: 1 1/19 = 5 % · 2 0/12 · 3 0/13 · 4 0/20
  - Kind B · Gymnasium: Kl. 5 13/14 = 93 % · Kl. 6 8/11 = 73 % · Kl. 7 3/9 = 33 % · Kl. 8 0/14 · Kl. 9 0/14 · Kl. 10 0/9
  - Kind B · Realschule: Kl. 5 12/15 = 80 % · Kl. 6 9/10 = 90 % · Kl. 7 3/14 = 21 % · Kl. 8 0/9 · Kl. 9 0/13 · Kl. 10 0/11
  - Kind B · IB MYP: 1 15/19 = 79 % · 2 5/12 = 42 % · 3 3/13 = 23 % · 4 0/20
  Die App sollte dieselben Zahlen zeigen; Abweichungen bitte melden (die App rechnet im Browser aus schule_uebersicht, diese Zahlen sind unabhängig per SQL gerechnet).

## 17.11. – Achtzehnte Runde Teil B (Lücken je Klasse) zusammengeführt und eingespielt
Zweige luecken-kl5 … luecken-kl10 nach lernen-app zusammengeführt (Stand ffdad93). inhalt_pruefen 92 von 92 OK; tests/lernen.test.cjs 46 von 46.
Eigene Gegenprüfung über alle 23 geänderten Themen: keine alte Aufgabe fehlt, keine Lernkarte entfernt, nichts aus der Pflicht genommen.
- Eingespielt mit einheit_abgleichen(…, 'sperren') (Weg A): 26 neue Lernkarten, 8 erweiterte Lernkarten, 799 neue Aufgaben (Übung 109/176/254 nach Stufe, 26 Test, 78 Korrektur, 156 Sicherung).
  Danach: 489 freigegebene Lernkarten; jede hat mindestens 3 freie Übungen je Stufe; keine neue Aufgabe gesperrt.
- Neue Lernkarten: Kl. 5 zahlen.ganz (schriftlich_plus_minus, umkehraufgabe, verstehen), zahlen.rechengesetze (kopfrechnen, umkehraufgabe_mal, schriftlich_geteilt, sach) ·
  Kl. 6 bruch.brueche (gemischte_zahlen, zahlbereiche), bruch.dezimal (merkwerte), bruch.rechnen (potenzen, sach) · Kl. 7 abbildungen.kongruenz (mittelsenkrechte, winkelhalbierende, vierecke_ordnen),
  geometrie.konstruktion (planfigur) · Kl. 8 funktionen.linear (graph_ablesen), funktionen.grundbegriffe (sachzusammenhang), funktionen.gebrochen (indirekt_sach) ·
  Kl. 9 funktionen.quadratisch (schnittpunkte), gleichungen.quadratisch (bruchgleichung), zahlen.reell (heron), trigo.allgemein (anwendung) ·
  Kl. 10 funktionen.trig (verschiebung_x), funktionen.exponential_log (linear_oder_exponentiell), stochastik.mehrstufig (pi_schaetzen).
- Betroffene Lernstände: kein abgeschlossener Flug der beiden Kinder liegt in diesen Themen; ein Kind hat in zahlen.ganz 2 Lernkarten begonnen (dort kommen 3 neue dazu).
- Offen aus den Berichten: App-Wünsche (gemischte Zahl als gestapelter Bruch, Einheitskreis neben Graph, Kegel/Körper-Zeichnungen, Simulationsknopf, Konstruieren durch Zeichnen);
  in den Themendateien stochastik.simulation und raum.schraegbilder steht noch gym_by 8 (Datenbank und Themenliste: 10); veraltete „offen“-Einträge in bruch.rechnen, bruch.dezimal, geometrie.konstruktion;
  Frage, ob die neuen Pflichtkarten der Klasse 9 auch für Realschule/IB Pflicht sind; gleichungen.trig nach Klasse 10?
- Teil A (drei neue Flüge, Zweig luecken-neu) ist noch nicht gestartet bzw. hat noch nichts hochgeladen.

## 17.11. – Prüfung der Achtzehnten Runde Teil B (Prüf-Chat, von Sebastian weitergegeben) – Ergebnis und Folgen
Geprüft: 26 neue und 8 erweiterte Etappen (Stand e32f315), je neue Etappe Erklärung und etwa 13 Bordkarten von Hand, alle Koordinaten-Grafiken der 799 neuen Aufgaben per Skript. **Keine falsche Lösung gefunden.**
Befunde des Prüf-Chats (Nummern = Position in der Aufgabenliste, ab 0 gezählt):
- MUSS – abbildungen.kongruenz / winkelhalbierende: Gerade h (x = −3 bzw. −2) und ein Auswahlpunkt liegen außerhalb des Bildausschnitts.
  → behoben (Haupt-Chat): Generator erweitert den Ausschnitt auf g, h und alle Auswahlpunkte; 5 Aufgaben (3 Übung, 2 Sicherung) haben nur ein neues Bild, alles andere gleich; eingespielt, alte Fassungen gesperrt.
- SOLLTE – Klasse 7 (abbildungen.kongruenz mittelsenkrechte/winkelhalbierende, geometrie.konstruktion planfigur): Aufgabentexte, Lückenformen und Lösungswege nutzen Geradengleichungen
  (y = −2, x = 4, y = x, „x + y = 10“); die kommen am Gymnasium erst in Klasse 8. Vorschlag: „die waagrechte Linie durch (0 | −2)“ bzw. Punkte statt Gleichungen.
- Annahme, zu prüfen: dieselben Karten gelten für Realschule Klasse 6, nutzen aber negative Koordinaten.
- abbildungen.kongruenz / vierecke_ordnen: Lösungsweg „ein Quadrat (oder ein Spezialfall davon)“ – Klammer streichen; Fehler-Satz „Wie bei Fliesen zählt die Richtung des Satzes“ unklar.
- zahlen.rechengesetze / umkehraufgabe_mal: Bild zu Schritt 2 zeigt schon die 6 Sprünge bis −8 und verrät die Lösung – Bögen erst in Schritt 3.
- zahlen.rechengesetze / sach: drei Aufgaben nach derselben Vorlage („Fest, Eintritt, Getränke“) direkt hintereinander auf Stufe 2.
- gleichungen.quadratisch / bruchgleichung: Die Scheinlösung (Lösung nicht in D) kommt nur in einer Übung vor – in Bildergeschichte und in mindestens einer Sicherungsaufgabe ergänzen.
- Prüfskript: einige Rechenausdrücke „c“ liefern die richtige Zahl, rechnen die Aufgabe aber nicht nach (zahlen.reell, zahlen.rationale_exponenten) – Lösungen von Hand geprüft: richtig.
Die Punkte außer dem MUSS gehen an die Klassen-Chats der Neunzehnten Runde (Klasse 5, 7 und 9; in inhalte/AUFTRAEGE.md ergänzt).

## 2026-11-17 19:30 – an durchsicht-kl5 … kl10 und lehrplan-rsib: Neunzehnte Runde Teil A und C übernommen
- Alle sechs Zweige `durchsicht-kl5` … `durchsicht-kl10` und `lehrplan-rsib` sind in `lernen-app` (Stand 4eda8cb). Prüfskript: 92 Themendateien OK. App-Tests: 46 von 46.
- Eingespielt in die Datenbank (68 freigegebene Gymnasium-Themen, Abgleich mit „sperren“, nichts gelöscht, Lernstände unverändert): 233 Aufgaben neu, 1 320 geändert (davon 1 294 umgestuft), 782 gesperrt.
- Freie Übungen jetzt: Stufe 1: 2 874 · Stufe 2: 4 698 · Stufe 3: 3 243 (vorher 2 541 / 4 027 / 4 153). 489 Etappen, keine unter 3 Übungen je Stufe; 162 Etappen haben weniger als 6 Stufe-3-Übungen → wird in der Zwanzigsten Runde aufgefüllt.
- Konflikt: `raum.schraegbilder` und `stochastik.simulation` wurden von Klasse 8 und Klasse 10 bearbeitet. Es gilt die Fassung von Klasse 10 (Themenliste: Klasse 10); die Änderungen aus Klasse 8 an diesen zwei Themen sind nicht übernommen. Das Hilfsskript von Klasse 8 heißt jetzt `_durchsicht_nachweis_kl8.py`.
- Nur umgestuft wurde der Pool `uebung`. Test, Korrektur und Sicherung sind nicht vollständig durchgesehen (Klasse 8 und 9 melden das ausdrücklich).
- Die Listen „Für Sebastian“ (Überschneidungen, Reihenfolge, Vertiefung, App-Wünsche) und die neun Entscheidungen aus `inhalte/pruefung/klassen/vorschlag-rsib.md` liegen bei Sebastian. Bis zu seiner Entscheidung nichts davon umsetzen.
- Nächster Schritt: Bau-Auftrag F (Aufgabentyp `g`, Stufenanzeige, Knobel-Bordkarte), danach Zwanzigste Runde (echte Stufen je Lernkarte).

## 17.11. 14:20 – an bau-stufen: Teil 1 übernommen, Migration F eingespielt; Zusatz 1
- Teil 1 ist in `lernen-app` (Stand siehe Zweig). Prüfskript: 95 von 95 Themendateien OK.
- Migration `20261118_w150_f_stufen_typ_bonus.sql` ist eingespielt (md5 geprüft). Rauchtest mit dem Testkind (zurückgerollt): `konto`, `einheit_lesen_intern`, `uebung_pruefen_intern` mit `karte_buchen` laufen; die neuen Felder (`bonus`, `knobel_sterne`) kommen.
- **Neu: Zusatz 1 zu Bau-Auftrag F** in `inhalte/AUFTRAEGE.md` („Lernstand“ öffnet die Klassen-Übersicht des Kindes; die alte Seite heißt „Was wackelt?“). Bitte in Teil 2 mit erledigen.

## 17.11. 14:20 – an durchsicht-rsib-1, durchsicht-rsib-2, luecken-neu: übernommen
- Alle drei Zweige sind in `lernen-app`. 24 Realschul-/IB-Themen als Entwurf abgeglichen (alte, nicht mehr enthaltene Aufgaben gesperrt, nichts gelöscht). Drei neue Flüge als Entwurf importiert: Einheit 93 (Flächen von Parallelogramm, Dreieck, Trapez – Quito), 95 (Volumen – Quito), 94 (Prismen und Zylinder – Cusco), je 7 Lernkarten und 196 Aufgaben.
- Nichts davon ist freigegeben. Freigabe entscheidet Sebastian (drei neue Flüge: nach unabhängiger Prüfung).
- **Zwanzigste Runde kann starten** („Schritt 2 erledigt“): Feld `g`, Pool `bonus` und die neuen Prüfregeln sind im Arbeitszweig und in der Datenbank.

## 17.11. 14:30 – an bau-stufen: Teil 2 (App 0.75.0) übernommen
- Teil 2 ist in `lernen-app`. App-Tests: 51 von 51. Migration F war schon eingespielt – bitte jetzt die echte Antwortform prüfen (aufgabe_anzeige typ/bonus, einheit_lesen bonus, uebung_pruefen bei Bonus, konto knobel_sterne/knobel_tag, lernstand knobel_*), wie angekündigt.
- Noch offen: **Zusatz 1 zu Bau-Auftrag F** in `inhalte/AUFTRAEGE.md` („Lernstand“ öffnet die Klassen-Übersicht des Kindes). Bitte vom aktuellen `lernen-app` aus auf `bau-stufen` bauen und melden.
- `main` bleibt bis zu Sebastians „Live“ auf 0.74.7.

## 17.11. 15:15 – an stufen-kl6, stufen-kl7, stufen-kl10, bau-stufen: übernommen und eingespielt
- `stufen-kl6`, `stufen-kl7`, `stufen-kl10` und `bau-stufen` (App 0.75.1, Zusatz 1) sind in `lernen-app`. Prüfskript: 95 von 95 OK. App-Tests: 52 von 52.
- Eingespielt: 29 Themen (27 freigegeben, 2 Entwurf). In der Datenbank jetzt 5 060 Aufgaben mit Typ und 420 Knobel-Bordkarten. Etappen mit weniger als 6 Stufe-3-Übungen: 77 (vorher 162) – der Rest gehört zu Klasse 5, 8, 9.
- **Überzählige Übungen (ohne `g`):** bleiben vorerst freigegeben. Die App wechselt Typ und Satzbau ohnehin ab. Ob sie gesperrt werden, entscheidet Sebastian.
- `main` ist 0.75.0; 0.75.1 wartet auf Sebastians „Live“.

## 17.11. 15:35 – an stufen-kl5, stufen-kl8, stufen-kl9 (und alle der Zwanzigsten Runde): übernommen und eingespielt
- Alle sechs Zweige der Zwanzigsten Runde sind in `lernen-app`. Prüfskript: 95 von 95 OK. Namenskonflikt: `_stufen_nachweis.py` ist die Fassung von Klasse 7; die von Klasse 8 heißt `_stufen_nachweis_kl8.py`.
- Datenbank: alle 489 Etappen der 68 freigegebenen Flüge haben Aufgabentypen, mindestens 4 / 6 / 8 freie Übungen auf Stufe 1 / 2 / 3 und mindestens eine Knobel-Bordkarte. Freie Übungen: Stufe 1: 2 742 · Stufe 2: 4 130 · Stufe 3: 4 010.
- **Überzählige Übungen (ohne `g`) sind auf Sebastians Entscheidung gesperrt, nicht gelöscht** (928 in Klasse 6/7/10, 1 443 in Klasse 5/8/9). Annahme der Chats damit bestätigt.
- Offen: unabhängige Stichprobe der neuen Stufe-3- und Knobel-Aufgaben; Test-, Korrektur- und Sicherungsaufgaben haben keine Typen; 24 Realschul-/IB-Themen haben noch keine Typen.

## 17.11. 15:50 – Entscheidungen von Sebastian und was daraus folgt
- **Drei neue Flüge freigegeben** (Einheiten 93, 94, 95) – auf Sebastians Entscheidung, ohne unabhängige Prüfung (so vermerkt). Quito steht im Plan von Kind A hinter Florenz. Überzählige Übungen dort gesperrt.
- **Lehrplan-Reihenfolge Klasse 9 geändert:** `zahlen.rationale_exponenten` 8, `funktionen.potenz` 9, `gleichungen.potenz` 10, `trigo.allgemein` 13, `gleichungen.trig` 14 (Datenbank und Themenliste). Klasse 6 und 8 mit den neuen Flügen in der Datenbank nachgezogen.
- **Realschule und IB werden nicht zurückgestellt:** neue Abschnitte in `inhalte/AUFTRAEGE.md` – „Zwanzigste Runde – Zusatz Realschule und IB“ (zwei Chats) und „Einundzwanzigste Runde“ (Teil A Bereinigen, Teil B Mindeststand je Jahrgang).

## 17.11. 16:15 – an stufen-rsib-2: übernommen und als Entwurf eingespielt
- `stufen-rsib-2` ist in `lernen-app`. Die 12 Dateien: Prüfskript OK. Datenbank: 373 Aufgaben neu, 1 049 geändert, 171 überzählige gesperrt; alle 61 Etappen mit Typen, mindestens 4 / 6 / 8 je Stufe und Knobel-Bordkarten. Weiter Entwurf – Freigabe und Einordnung in den Plan folgen nach dem Vorschlag „Mindeststand je Jahrgang“.

## 17.11. 16:30 – an bau-motivation: Teil 1 übernommen, Probelauf bestanden, Migration noch nicht eingespielt
- Teil 1 (App 0.76.0) ist in `lernen-app`. App-Tests: 55 von 55.
- Probelauf gegen die echte Datenbank in einer zurückgerollten Transaktion (Migration + Rauchtest): Rauchtest ohne Fehler; sitzende Etappen und Punktesumme vorher = nachher, keine sitzende Etappe ohne eigene Lösungen.
- Die Migration spiele ich erst unmittelbar vor Sebastians „Live“ ein, damit die alte App nicht tagelang „volle Punkte, aber nicht gelandet“ zeigt. Prüfbitte an ChatGPT ist gestellt (Werkstatt, Wunsch 176, Nachricht 841).
- **Bitte jetzt mit Teil 2 weitermachen** (Format für Expeditionen: README und Prüfskript) – dafür braucht es die Migration nicht.

## 17.11. 16:35 – an bau-motivation: Teil 2 übernommen; an stufen-rsib-1: übernommen und als Entwurf eingespielt
- `bau-motivation` Teil 2 (Format für Expeditionen) ist in `lernen-app`; `--alle` meldet OK einschließlich `8-handytarif`. Bitte mit **Teil 3 (Mischkarten)** weitermachen. Teil 1 ist live (App 0.76.0, Migration eingespielt, Bestand unverändert: 28 gelandete Etappen, Punktesumme 73).
- `stufen-rsib-1`: 12 Themen als Entwurf abgeglichen – 480 Aufgaben neu, 1 155 geändert, 330 überzählige gesperrt; alle 69 Etappen mit Typen, mindestens 4 / 6 / 8 je Stufe und Knobel-Bordkarten.
- Neu in `inhalte/AUFTRAEGE.md`: „Zweiundzwanzigste Runde: mehr Textaufgaben in Klasse 8“ (Auftrag des Lehrers) und „Expeditionen – Inhalte für Klasse 5 und Klasse 8“.

## 18.11. 03:15 – an text-kl8, bereinigen, plan-mindeststand: übernommen; an bau-motivation: Teil 3 – eine Korrektur nötig
- `text-kl8`, `bereinigen`, `plan-mindeststand` und `bau-motivation` (Teil 3, App 0.77.0) sind in `lernen-app`. Prüfskript: 96 von 96 OK. App-Tests: 57 von 57.
- Sechs Klasse-8-Themen hatten `text-kl8` und `bereinigen` beide geändert (Konflikt nur in den JSON-Dateien). Die Generatoren ließen sich zusammenführen; die Dateien sind daraus neu erzeugt. 10 neue Textaufgaben entfallen, weil ihre Lernkarte umgezogen ist (`funktionen.gebrochen` indirekt/indirekt_sach, `messen.kreisberechnung` zylinder).
- Eingespielt: 46 Themen, 1 182 Aufgaben neu, 158 überzählige gesperrt. Lernstände: Von den umgezogenen oder entfallenen Lernkarten hatte kein Kind einen Stand; Bestand unverändert.
- **bau-motivation, Teil 3 – Probelauf der Migration (zurückgerollt): Rauchtest bricht bei „FEHLER 2“ ab.** Ursache: `schule.mischkarten` nimmt für das Testkind auch Aufgaben mit `freigegeben = false` (`a.freigegeben or (select test from ich)`). Seit dem 17.11. sind 2 500 überzählige Übungen in freigegebenen Flügen gesperrt (`freigegeben = false`, `typ is null`); das Testkind bekommt sie als Mischkarte. Für echte Kinder stimmt die Auswahl. Mit `and a.freigegeben` an dieser Stelle läuft der ganze Rauchtest fehlerfrei durch (Probelauf). Bitte in der Migrationsdatei korrigieren (gesperrte Aufgaben nie als Mischkarte, auch nicht für das Testkind; Entwurfs-Flüge des Testkinds bleiben über den Status der Einheit erlaubt) und prüfen, ob dieselbe Stelle anderswo vorkommt (z. B. Wiederholung, Übungsauswahl). Danach „FERTIG: Teil 3 (korrigiert)“ melden. Die Migration ist nicht eingespielt; App 0.77.0 ist nicht live.

## 18.11. 03:45 – an alle: Realschul-Klasse und IB-Jahr je Thema sind jetzt fest eingetragen
- Befund (Sebastian): Die App zeigte z. B. „Terme umformen“ mit Realschule 6 und IB 1. Ursache: `schule.thema_jahrgang` nahm je Schulart die früheste Zuordnung, auch Neben-Zuordnungen; 860 von 862 Zuordnungen sind ungeprüft.
- Jetzt gilt für `rs_by` und `ib_myp` der Wert aus `inhalte/pruefung/klassen/vorschlag-mindeststand.md`, Punkt 1 (RS korrigiert nach `vorschlag-rsib.md`; IB = Vorschlag rsib, sonst bisheriger Wert). Migration `supabase/migrations/20261118_w150_klassen_rs_ib_fest.sql` ist eingespielt; `inhalte/themenliste.json` hat dieselben Werte (54 Einträge geändert). `gym_by` ist unverändert.
- `ib_myp` ist das Jahr 1–5 im IB Middle Years Programme (entspricht etwa Klasse 6–10), keine Klasse. IB-Werte bleiben „üblich“ oder „Annahme“ – das IB legt keinen Stoff je Jahr fest.
- **an bau-motivation (Zusatz, mit der Korrektur zu Teil 3 liefern):** Überall, wo die App IB anzeigt (Lernstand-Tabelle, Mini-Linien, Flugplan, Lehrplan-Übersicht, Info-Seite): Beschriftung „MYP-Jahr 1–5“ mit dem Hinweis „entspricht etwa Klasse 6–10“; keine Spalte „Kl. 5“ für IB. Prüfen, wo die App MYP-Jahr in eine Klasse umrechnet (bisher teils + 4) – richtig ist + 5. Dazu der Knopf „Lernen starten“ als erster Knopf an der Kinderkarte (siehe Kopiertext von Sebastian).

## 18.11. 04:10 – an stufen-kl5: Korrekturen übernommen und eingespielt; an bau-motivation: Teil 3 (korrigiert) und Teil 4 übernommen, Probelauf
- `stufen-kl5` (Stand ce83787, 31 korrigierte Aufgaben in 8 Themen) ist in `lernen-app` und eingespielt: 16 Aufgaben neu angelegt (Frage oder Antworten geändert; die alte Fassung ist gesperrt), die übrigen an Ort und Stelle berichtigt. Die Formulierung „k. Strich nach dem Anfang“ steht in keiner freigegebenen Aufgabe von `zahlen.ganz` mehr. Lernstände unverändert.
- `bau-motivation` (Teil 3 korrigiert, Teil 4, IB-Beschriftung, App 0.78.0) ist in `lernen-app`. App-Tests 62 von 62, Prüfskript 96 von 96.
- Probelauf beider Migrationen gegen die echte Datenbank (zurückgerollt): **Teil 3** – Rauchtest ohne Fehler. **Teil 4** – Migration läuft; der Rauchtest bricht mit „column reference k.einheit_id is ambiguous“ ab. Das ist ein Fehler **im Test**, nicht in der Migration: Die Variable `k` (Zeile `schule.karte_stand`) kollidiert mit dem Tabellen-Alias `k` in den Zeilen 20–52. Mit `#variable_conflict use_column` läuft der ganze Test fehlerfrei durch. Bitte in `supabase/tests/w176_t4_rauchtest.sql` beheben (Alias oder Variable umbenennen) – die Migration bleibt, wie sie ist.
- Eingespielt wird beides bei Sebastians „Live“.

## 18.11. 04:50 – an stufen-kl6 … stufen-kl10: inhaltliche Prüfung übernommen und eingespielt; an bau-motivation: Sperr-Korrektur eingespielt
- Alle fünf Zweige sind in `lernen-app` (ohne Konflikt; alle 56 geänderten Themen aus den Generatoren neu erzeugt – deckungsgleich). Prüfskript 96 von 96 OK.
- Zusammen 3 814 neue Aufgaben geprüft, 264 geändert (Kl. 6: 778/75 · Kl. 7: 454/47 · Kl. 8: 1 449/71 · Kl. 9: 697/40 · Kl. 10: 436/31). Eingespielt: 89 neu angelegt (alte Fassung gesperrt), 175 an Ort und Stelle berichtigt. Lernstände unverändert.
- `bau-motivation`: Migration `20261118_w176_a_gesperrt_pruefen.sql` ist eingespielt (Probelauf und Rauchtest ohne Fehler). App 0.78.1 ist in `lernen-app`, noch nicht live.

## 18.11. 06:20 – an bau-motivation: H8 eingespielt; `h_muss` bricht im Probelauf ab – bitte korrigieren. Danach neuer Auftrag LA
- Auftrag H ist in `lernen-app` (App 0.79.0, Tests 70 von 70, Prüfskript 96 von 96). **H8 ist eingespielt** (Probelauf und H8-Rauchtest ohne Fehler, Lernstände unverändert).
- **`20261119_w176_h_muss.sql` bricht im Probelauf gegen die echte Datenbank ab:** `record "v" is not assigned yet` in der Schleife des H2-Blocks (`select k.* from schule.karte_stand k where not k.sitzt and k.folge > 0 and not exists (select 1 from schule.versuch v join …)`). Ursache: Im selben `do`-Block ist eine Variable `v` (record) deklariert; sie kollidiert mit dem Tabellen-Alias `v`. Bitte Alias oder Variable umbenennen und die ganze Datei auf weitere solche Kollisionen prüfen (auch `h_sollte`, das ich deshalb noch nicht laufen lassen konnte).
- **Rauchtests:** `w176_t4_rauchtest.sql` bricht ab mit `"a_ids" is not a known variable` (nach der Änderung von Schritt 9). `w176_t3_rauchtest.sql` Schritt 4 erwartet nach einer falschen Mischkarte noch `wdh_fehler = 1` – seit H8 ist das überholt („FEHLER 4“); bitte an die neue Regel anpassen. `w176_h8_rauchtest.sql` läuft durch.
- Hinweis zum Probelauf: Ich führe die Migrationen in einer Transaktion aus, die am Ende zurückgerollt wird, und danach die `do`-Blöcke der Rauchtests. Du kannst die Datenbank lesen, aber nichts ausführen – deshalb bitte besonders auf Namenskonflikte zwischen plpgsql-Variablen und Tabellen-Aliasen achten (dritter Fall dieser Art).
- Nach „FERTIG: Auftrag H (korrigiert)“ spiele ich `h_muss` und `h_sollte` ein; App 0.79.0 geht mit Sebastians „Live“ zusammen mit `h_muss` live.
- **Danach neuer Auftrag:** „Bau-Auftrag LA (18.11.): Lehrer-Aufbau“ in `inhalte/AUFTRAEGE.md` (Zweig `bau-lehrer`).

## 18.11. 06:35 – an expedition-kl5, expedition-kl8, doppelt-pruefen: übernommen
- Alle drei Zweige sind in `lernen-app`. Prüfskript: 116 von 116 OK (95 Themen, 21 Expeditionen).
- Die 21 Expeditionen (10 Klasse 5, 11 Klasse 8 mit dem Beispiel) sind als **Entwurf** in der Datenbank; für echte Kinder nicht sichtbar. Fachliche Prüfbitte an ChatGPT ist gestellt (Werkstatt, Wunsch 176). Freigabe erst nach dieser Prüfung, nach Bau-Auftrag H (H9–H11) und Sebastians Entscheidung.
- `doppelt-pruefen`: Ergebnis liegt bei Sebastian (11 Themen auflösen, 13 bleiben, keine neuen Themen nötig). Bis zu seiner Entscheidung nichts umsetzen.

## 18.11. 08:40 – an bau-motivation: Auftrag H läuft jetzt im Probelauf durch (eine Zeile von mir berichtigt); Rauchtest H12b anpassen
- `h_muss` brach wieder ab: `"n_gleich" is not a known variable`. Ursache: Im H2-Block stand der Kommentar `-- w, nicht v …` mitten in der `declare`-Zeile und verschluckte `n_neu`, `n_null`, `n_gleich`. Ich habe den Kommentar ans Zeilenende gesetzt (Commit 9d2f9be in `lernen-app`) – bitte in deinen Zweig übernehmen, nicht überschreiben.
- Probelauf danach (zurückgerollt): `h_muss`, `h_sollte` und die Rauchtests `h_muss`, `h8` ohne Fehler. Die Folge-Summe eines Kindes steigt durch H2 um 2, gelandete Etappen und eigene Lösungen unverändert.
- `w176_h_sollte_rauchtest.sql` meldet „FEHLER H12b: ungültiger Import hat geschrieben“ – nur weil `8-handytarif` schon als Entwurf in der Datenbank liegt. Mit einem anderen Schlüssel läuft der Test durch. Bitte im Test einen Schlüssel nehmen, den es nicht gibt.
- Eingespielt ist noch nichts; `h_muss`, `h_sollte` und App 0.79.0/0.80.0 warten auf Sebastians „Live“.

## 18.11. 08:40 – an bau-lehrer: LA übernommen; ein Test wackelt
- Zweig ist in `lernen-app` (App 0.80.0). `la_3` und `la_4` mit Rauchtests im Probelauf (zurückgerollt) ohne Fehler; eingespielt wird mit Sebastians „Live“.
- Tests lernen: 80 von 81. „LA-1: Seite des Kindes mit 4 Reitern …“ scheitert im Gesamtlauf (auch auf deinem Zweig allein), einzeln läuft er: `allInnerTexts()` liest die Reiter direkt nach `waitForURL`, bevor sie gezeichnet sind (Ergebnis `[]`). Bitte vorher auf `.lern-reiter a` warten.

## 18.11. 08:40 – an aufloesen: übernommen, noch nicht eingespielt
- Zweig ist in `lernen-app`; Prüfskript 116 von 116 OK; Generatoren und Dateien stimmen überein.
- Eingespielt wird erst nach Sebastians Entscheidung zu deinen Punkten 3 (gegenvektor Pflicht, verschiebung Vertiefung) und 4 (Dualsystem Pflicht für alle), weil sonst abgeschlossene Flüge beider Kinder wieder offen werden.

## 18.11. 08:40 – an expedition-kl5, expedition-kl8: fachliche Prüfung da – 4 Auflagen
- ChatGPT (Werkstatt 853): 17 freigabereif, 4 mit Auflagen (Text, keine Rechnung). Auftrag: „Expeditionen – Korrekturen nach der fachlichen Prüfung“ am Ende von `inhalte/AUFTRAEGE.md`.

## 18.11. 11:20 – an alle: App 0.80.0 ist live; Auflösen eingespielt; 14 Flüge und 17 Expeditionen freigegeben
- **Live (Sebastians „Live“):** `main` = App 0.80.0 (Lehrer-Aufbau LA-1 bis LA-7, Auftrag H). Eingespielt: `h_muss` (berichtigt), `h_sollte`, `la_3`, `la_4`; Rauchtests danach ohne Fehler.
- **aufloesen:** Die 17 Zielthemen sind eingespielt (15 freigegeben, 2 damals Entwurf). Sebastians Entscheidung: **Dualsystem und Gegenvektor sind Vertiefung** (in `_af_neu.py` und `_af_plan.py` geändert, Commit 216d50b) – kein abgeschlossener Flug wird wieder offen. Die 10 aufgelösten Themen bleiben als Entwurf liegen.
- **Freigegeben (Sebastian):** 14 Flüge – `abbildungen.determinanten2`, `daten.stichproben`, `terme.quadratische_extreme`, `abbildungen.matrizen`, `gleichungen.wurzel`, `funktionen.reihen`, `funktionen.betrag`, `daten.zweidimensional`, `daten.standardabweichung`, `daten.normalverteilung`, `sonder.graphentheorie`, `sonder.logik`, `sonder.optimierung`, `zahlen.schranken`. Im Plan von Kind B neu: Shanghai (Kl. 8), Perth und Lagos (Kl. 7). `gleichungen.wurzel` ist in Tokio abgewählt (freiwillig). Die übrigen liegen in Zusatz-Orten außerhalb des Plans.
- **Expeditionen:** 17 freigegeben; `5-flug_toronto`, `5-schatzsuche`, `8-radtour`, `8-pool` bleiben Entwurf bis zu den Korrekturen (Auftrag am Ende von `AUFTRAEGE.md`).
- **an bau-motivation – Fehler gefunden:** `schule.einheit_abgleichen(…, 'sperren')` sperrt auch Expeditions-Teile (`pool = 'expedition'`) des Flugs, weil sie nicht in der Themendatei stehen (heute 21 Teile in 14 Expeditionen; durch erneuten Import behoben). Bitte als Migration liefern: Abgleich lässt `pool = 'expedition'` unberührt; Rauchtest dazu.

## 18.11. 11:25 – an bau-motivation: „Abgleich ohne Expeditionen“ eingespielt; Rauchtest bricht ab
- Migration `20261119_abgleich_ohne_expeditionen.sql` ist eingespielt (md5 verglichen). Eigener Probelauf: 17 Themen erneut abgeglichen, freie Expeditions-Teile 90 → 90.
- `abgleich_ohne_expeditionen_rauchtest.sql` bricht ab: „Aufgaben einer freigegebenen Einheit sind unveränderlich“. Der Test muss den Flug vorher auf `geprueft` setzen (so läuft auch das Einspielen) oder einen Entwurfs-Flug nehmen. Bitte bei Gelegenheit anpassen – nicht dringend.

## 20.11. 02:55 – an alle: übernommen; neuer Bau-Auftrag I
- **bau-lehrer, bau-motivation:** eure Test-Korrekturen sind in `lernen-app` (Tests lernen 81 von 81).
- **expedition-kl5, expedition-kl8:** Korrekturen 853 sind in `lernen-app` (Prüfskript 116 von 116, Generatoren = Dateien). Die vier Expeditionen mit Auflagen gehen noch einmal an ChatGPT und bleiben bis dahin Entwurf.
- **pruefung-kinderansicht:** Nachprüfung übernommen (`inhalte/pruefung/lehrer/nachpruefung.md`). 1 Muss, 5 Sollte, 6 Kann.
- **ChatGPT (Werkstatt 872, 873):** Auftrag H – 2 Muss offen (H10 Mischkarte nicht serverseitig gebunden, H2 Nachrechnung der Folge), Rest geschlossen oder Sollte. Nachtragstest – kein Muss.
- **Neuer Auftrag:** „Bau-Auftrag I (20.11.)“ am Ende von `inhalte/AUFTRAEGE.md`. **Zuerst Teil 1 (`bau-lehrer`), danach Teil 2 (`bau-motivation`)** – nicht gleichzeitig.

## 20.11. 03:10 – an bau-lehrer: Auftrag I, Teil 1 hat einen Zusatz (Punkt 10)
- Sebastian hat entschieden: **Reisetage und Pausen** werden eintragbar (Punkt 10 in Teil 1). Die Stand-Zellen bleiben ohne Ampel. Falls du schon begonnen hast: Punkt 10 bitte mit aufnehmen.
- An bau-motivation (Teil 2, Punkt 6): Die Frist nach einem Nachtragstest bleibt, wie sie ist – nur beschreiben.

## 20.11. 03:35 – an bau-lehrer: zusätzlich Teil 1b (LA-8 „Lehrplan nach Themengebiet“)
- Sebastian hat LA-8 freigegeben. Auftrag: „Teil 1b“ im Abschnitt „Bau-Auftrag I (20.11.)“ in `inhalte/AUFTRAEGE.md`; Vorgabe `inhalte/pruefung/lehrer/umsetzung.md` Abschnitt LA-8, Entwurf `inhalte/pruefung/lehrer/entwurf/lehrplan-spalte.html` (jetzt in `lernen-app`). Nach Teil 1, im selben Zweig, eine Version 0.81.0.

## 20.11. 03:35 – an expedition-kl5: zwei Sätze nach ChatGPTs Nachprüfung (875) vom Haupt-Chat geändert
- `5-flug_toronto` Teil d: „Von der Landung bis zur Ankunft im Hotel vergehen insgesamt 1 h 30 min – einschließlich Aussteigen, Gepäckabholen und Fahrt.“ `5-pyramide` Teil c: „Die echten großen Pyramiden bestehen aus Steinblöcken und sind viel größer als die beiden Holzmodelle.“ Beides im Generator geändert, Prüfskript OK. Bitte vor weiteren Änderungen `lernen-app` holen.

## 20.11. 03:55 – an bau-lehrer, bau-motivation, pruefung-kinderansicht, pruefung-neu-1/2: übernommen
- **bau-lehrer:** Auftrag I Teil 1 und Teil 1b (LA-8) sind in `lernen-app` (App 0.81.0, Tests lernen 94 von 94). `20261120_i_pause.sql` mit Rauchtest im Probelauf (zurückgerollt) ohne Fehler. Eingespielt und live erst mit Sebastians „Live“.
- **bau-motivation:** Teil 1 ist zusammengeführt – **Teil 2 kann beginnen** (Stand `lernen-app` 67dae64 oder neuer holen; Version 0.81.1).
- **pruefung-kinderansicht:** Der Bau ist fertig zum Nachprüfen (Mängel aus der Nachprüfung, Reisetage, LA-8) – Stand `lernen-app`, noch nicht live.
- **pruefung-neu-1, pruefung-neu-2:** Korrekturen übernommen (Prüfskript 116 von 116, Generatoren = Dateien); werden eingespielt, sobald kein Kind übt.

## 20.11. 04:00 – an alle: App 0.81.0 ist live; Prüf-Korrekturen und Expeditionen eingespielt
- **Live (Sebastians „Live“):** `main` = App 0.81.0 (Auftrag I Teil 1 und 1b). `20261120_i_pause.sql` ist eingespielt, Rauchtest danach ohne Fehler.
- **pruefung-neu-1/2:** Korrekturen an 13 Flügen sind in der Datenbank (Mindestmengen erfüllt, nichts gelöscht).
- **Expeditionen:** alle 21 freigegeben (Sebastians Entscheidung), 0 gesperrte Teile.
- **bau-motivation:** Teil 2 baut auf `lernen-app` 68a663d oder neuer auf (Version 0.81.1).

## 20.11. 04:30 – an bau-motivation: Auftrag I Teil 2 übernommen; ein Testfehler
- Zweig ist in `lernen-app` (App 0.81.1, Tests lernen 95 von 95). Probelauf (zurückgerollt): `20261120_i2_lernregeln.sql` ohne Fehler; Rauchtests `i2`, `w177` Block 1, `h_muss`, `h_sollte`, `h8`, `t1`, `t3`, `abgleich` ohne Fehler; Lernstände unverändert.
- **`w177_nachtragstest_rauchtest.sql`, zweiter Block, bricht ab:** `operator does not exist: bigint = bigint[]` im `if` in Zeile 54 des Blocks (nach dem Sterne-Vergleich). Bitte den Vergleich berichtigen (vermutlich `= any(…)`).
- Eingespielt und live erst mit Sebastians „Live“.

## 20.11. 04:30 – an pruefung-kinderansicht: Nachprüfung 2 übernommen
- Dein Muss (Pausen-Migration vor dem Merge) ist erfüllt: `i_pause` ist eingespielt, Rauchtest danach ohne Fehler; 0.81.0 ist live. Die Stand-Zellen bleiben ohne Ampel (Sebastians Entscheidung vom 20.11.). Sollte 1 und 2 (Trennung im Umschalter, lange Überschriften auf dem Handy) und die Kann-Punkte gehen in den nächsten Bau-Auftrag.

## 20.11. 04:25 – an alle: App 0.81.1 ist live
- `main` = App 0.81.1 (Auftrag I Teil 2). `20261120_i2_lernregeln.sql` ist eingespielt; Rauchtests `i2`, `h_muss`, `h_sollte`, `h8`, `t1`, `t3` danach ohne Fehler, Lernstände unverändert. Prüfbitte an ChatGPT ist gestellt.
- Offen bei bau-motivation: zweiter Block von `w177_nachtragstest_rauchtest.sql` (Eintrag 04:30).

## 20.11. 04:45 – an bau-motivation, bau-lehrer: Teil 3 und Teil 4 des Bau-Auftrags I
- bau-motivation: Test-Korrektur W177 übernommen. ChatGPT (Werkstatt 878) hat zu Teil 2 zwei Muss bei H2 gefunden (endgültige Wertung festhalten; Nachbuchen genau einmal) und vier Sollte. Auftrag: „Teil 3“ im Abschnitt „Bau-Auftrag I“ in `inhalte/AUFTRAEGE.md`.
- bau-lehrer: „Teil 4“ (Restpunkte des Gestalters) – erst nach Teil 3.

## 20.11. 05:05 – an alle: neuer Bau-Auftrag LB (vom Gestalter, von Sebastian freigegeben)
- Abschnitt „Bau-Auftrag LB (20.11.)“ am Ende von `inhalte/AUFTRAEGE.md`; Vorgabe `inhalte/pruefung/lehrer/umsetzung-lb.md` und Entwurf liegen jetzt in `lernen-app`.
- Reihenfolge: `bau-motivation` Teil 3 → (LB-3 Serverteil, sobald Sebastian LB-3 bestätigt hat) → `bau-lehrer` Teil 4 + LB-1 + LB-2. Neuer Inhalts-Chat `lehrplan-lb` für LB-4 läuft sofort.
