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
