# Postfach nacharbeit (Fünfzehnte Runde)

Neueste Meldung oben.

## 2026-11-17 02:02 – FERTIG
Fünfzehnte Runde abgeschlossen (Zweig nacharbeit, nicht gemergt). Alle Themen: inhalt_pruefen OK ohne Hinweise; Nachweis je Thema mit inhalte/generatoren/_nacharbeit_nachweis.py <thema> (gegen origin/lernen-app): nur die unten genannten Stellen geändert, keine alte Aufgabe entfernt oder umsortiert. Zweig lässt sich konfliktfrei mit dem aktuellen lernen-app (9d092d0) zusammenführen.

### geänderte Lernkarten
- funktionen.trig / bogenmass: 2 Schritte (90° = π/2, 270° = 3π/2, 360° = 2π; „ab jetzt Bogenmaß“, sin-Graph mit π-Achse); 8 Bogenmaß-Übungen.
- funktionen.trig / werte: Karte unverändert (war schon im Bogenmaß); 8 Bogenmaß-Übungen.
- funktionen.trig / periode: Schritt 3 nur Gradmaß, neuer Schritt 4 „p = 2π : 3 = 2π/3“ mit π-Achse; Regel „Periode von sin(b · x): 2π : b = 360° : b“; 8 Übungen.
- funktionen.trig / parameter: Schritt 5 (Extremstellen π/2 und 3π/2, π-Achse); fehler_bild auf π-Achse umgestellt (sonst lägen die Punkte falsch); 8 Übungen.
- funktionen.trig / zuordnen: Schritt 5 (b = 2π : π = 2, π-Achse); Regel + „b = 2π : p“; 8 Übungen.
- funktionen.trig / eigenschaften: Schritt 5 (Nullstellen π/2, 3π/2 bzw. 0, π; π-Achse); Regel im Bogenmaß mit Grad in Klammern; 8 Übungen.
- funktionen.trig / anwendung: Schritt 5 (30° = π/6, h(t) = 20 − 18 · cos(π/6 · t)); Regel „b = 2π : Periodendauer oder 360° : Periodendauer“; 8 Übungen.
- funktionen.trig / offen: überholte Begründung „π-Beschriftung nicht möglich“ und der App-Vorschlag „x-Achse in π beschriften“ entfernt.
- daten.kennwerte / modal_spannweite: Vertiefung (median war es schon).
- geometrie.grundbegriffe / kreis_lage: 2 Schritte mit Zeichnung (zwei Kreise berühren sich außen bei r₁ + r₂; getrennt).
- geometrie.ortslinien / zwei_kreise: 1 Schritt mit Zeichnung (Kreis im Kreis, d < r₁ − r₂).
- trigo.allgemein / kosinussatz_seite: 1 Schritt mit Zeichnung (Dreieckswinkel = 180° − Drehwinkel), Wort „Drehwinkel“; fehler_bild vollständig angegeben (Anzeige unverändert).
- gleichungen.lgs3 / loesen: 1 Schritt mit Tabelle („0 = −5: keine Lösung; 0 = 0: unendlich viele“); alte Schritte 4 und 5 zu einem zusammengefasst (höchstens 5 Schritte).
- geometrie.konstruktion / kongruenzsatz: 6 SsW-Aufgaben Stufe 3 mit Zeichnung (nur Feld f.grafik ergänzt, Text/Antworten/Lösung gleich).
- geometrie.winkel, funktionen.grundbegriffe: nur offen berichtigt.
- inhalte/README.md: Abschnitt „Vertiefung“.

### ersetzt
- keine (alle SsW-Aufgaben ließen sich sauber zeichnen).

### offen geblieben
- geometrie.konstruktion: Die 6 SsW-Aufgaben gelten im Vergleich als „geändert“ (Feld f). Falls das Einspielen geänderte Aufgaben wie neue behandelt, bitte prüfen.
- geometrie.ortslinien: Der Generator schreibt inzwischen block_id 83 (aus themenliste.json, Einheit Kairo); im JSON bleibt 79 wie freigegeben. Welche gilt?
- funktionen.trig: Die älteren Aufgaben-Graphen sind weiter in Grad beschriftet (nicht beauftragt, Aufgaben unverändert).
- funktionen.grundbegriffe: Aufgaben mit Kreis als Gegenbeispiel („kein Funktionsgraph“) wären jetzt zeichenbar, sind aber nicht gebaut.
- Nicht geändert wie beauftragt: Zinseszins (Kl. 9), zahlen.intervalle und gleichungen.ungleichungen (Kl. 8), Schrägbilder/Simulation/Ortslinien.

## 2026-11-17 02:01 – STATUS
funktionen.trig fertig: Bogenmaß in den Lernkarten durchgehend – bogenmass +2 Schritte (90° = π/2 … 2π; Graph mit π-Achse), periode/parameter/zuordnen/eigenschaften/anwendung je ein Schlussschritt im Bogenmaß (π-Achse, außer anwendung: Zeitachse), Regeln von periode, zuordnen, eigenschaften, anwendung mit Bogenmaß; Schritt 3 von periode ohne den Bogenmaß-Teil (steht jetzt in Schritt 4); fehler_bild von parameter auf π-Achse umgestellt. werte war schon im Bogenmaß (unverändert). Je Lernkarte 8 neue Übungen im Bogenmaß (S1: 2, S2: 3, S3: 3) = 56, alte 238 Aufgaben unverändert. offen: überholte Begründung „π-Beschriftung nicht möglich“ und der Vorschlag „x-Achse in π beschriften“ entfernt. inhalt_pruefen OK ohne Hinweise, Nachweis OK.

## 2026-11-17 01:56 – STATUS
geometrie.konstruktion fertig: Lernkarte kongruenzsatz – alle 6 Stufe-3-Aufgaben zum Fall SsW haben jetzt eine Zeichnung (figur): bei „Wie viele Dreiecke gibt es?“ Seite c, Winkel α mit freiem Schenkel und das Lot von B auf den Schenkel mit seiner Länge; bei „Dreiecke ABC und DEF“ das Dreieck mit AB, AC und dem Winkel bei B. Fragetexte, Antworten, Lösungen unverändert, nur f.grafik ergänzt – keine Aufgabe ersetzt. inhalt_pruefen OK, Nachweis OK (6 Aufgaben, nur Feld f).

## 2026-11-17 01:54 – STATUS
geometrie.ortslinien fertig: Lernkarte zwei_kreise – neuer letzter Schritt „Bei 0,5 km Abstand ist 0,5 < 5 − 4: Kreis im Kreis, kein Ort.“ mit Zeichnung. Aufgaben unverändert; inhalt_pruefen OK ohne Hinweise, Nachweis OK (nur schritte). Hinweis: Der Generator schreibt jetzt block_id 83 (Kairo, aus themenliste.json); die Datei hatte 79. Ich habe 79 in der Datei belassen (nicht beauftragt) – bitte beim Einspielen entscheiden.

## 2026-11-17 01:54 – STATUS
geometrie.grundbegriffe fertig: Lernkarte kreis_lage – zwei neue Schritte mit Zeichnung: zwei Kreise berühren sich von außen (Mittelpunkte 5 m = 3 m + 2 m) und liegen getrennt (7 m > 3 + 2). Aufgaben unverändert; inhalt_pruefen OK ohne Hinweise, Nachweis OK (nur schritte).

## 2026-11-17 01:53 – STATUS
trigo.allgemein fertig: Lernkarte kosinussatz_seite – neuer letzter Schritt „Schiff: Drehwinkel 50°. Der Dreieckswinkel am Wendepunkt ist 180° − 50° = 130°.“ mit Zeichnung (Kurs mit gestrichelter Verlängerung, 50° und 130°), neues Wort „Drehwinkel“. fehler_bild vollständig angegeben (die App übernimmt sonst das Bild des letzten Schritts); Anzeige des Fehlers wie bisher. Aufgaben unverändert; inhalt_pruefen OK ohne Hinweise, Nachweis OK.

## 2026-11-17 01:52 – STATUS
gleichungen.lgs3 fertig: Lernkarte loesen – neuer letzter Schritt „Kommt 0 = −5 heraus: keine Lösung. Bei 0 = 0: unendlich viele.“ mit Tabelle; damit höchstens 5 Schritte bleiben, die alten Schritte 4 und 5 zu einem zusammengefasst („In (I): 1 − 2 + z = 2. Lösung: (1 | −2 | 3).“). Aufgaben unverändert; inhalt_pruefen OK ohne Hinweise, Nachweis OK (nur inhalt.etappen[loesen].schritte).

## 2026-11-17 01:51 – STATUS
inhalte/README.md: Abschnitt „Vertiefung“ ergänzt (lernziele_pflicht/lernziele_vertiefung; nicht testrelevant, zählt nicht für den Stempel).

## 2026-11-17 01:50 – STATUS
funktionen.grundbegriffe fertig: offen-Eintrag „Kreis kann die App nicht zeichnen“ berichtigt (Kreis zeichenbar; Kreis-Gegenbeispiel als mögliche Ergänzung offen). Sonst nichts geändert; inhalt_pruefen OK, Nachweis OK (nur „offen“).

## 2026-11-17 01:50 – STATUS
geometrie.winkel fertig: veralteten offen-Eintrag („Winkelsätze Kl. 5“) berichtigt – Titel „Mit Winkeln rechnen“, Winkelsätze als eigener Flug Kl. 7, kreuzung Vertiefung. Sonst nichts geändert; inhalt_pruefen OK, Nachweis OK (nur „offen“).

## 2026-11-17 01:50 – STATUS
daten.kennwerte fertig: Lernkarte modal_spannweite aus lernziele_pflicht nach lernziele_vertiefung (median war schon Vertiefung). Sonst nichts geändert. inhalt_pruefen OK; Nachweis (_vertiefung_nachweis.py und _nacharbeit_nachweis.py): Aufgaben und Lernkarten unverändert, nur inhalt.bewertung geändert.
