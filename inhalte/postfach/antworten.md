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
