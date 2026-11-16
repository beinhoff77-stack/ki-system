# Rückmeldung nach Fehlern und Lernweg – Prüfbericht (2026-11-16)

Zweig `pruefung-rueckmeldung-lernweg` (von `lernen-app`, Stand 3f03b8a). Nichts an App, Tests, Datenbank, Server oder `inhalte/themen/` geändert.

**Grundlage:**
- **Gelesen:**
  - `lernen.js`: Üben, Wiederholen, Eltern-Lernstand.
  - `supabase/migrations/20261114_w150_lernkarten_meisterschaft.sql`.
  - Die Datenbankfunktionen `uebung_pruefen_intern`, `antwort_bewerten`, `nachtest_stand`, `test_starten_intern`, `test_abschliessen_intern` und `reiseoptionen`. Sie wurden **nur gelesen**: `pg_get_functiondef`.
- **Nachgestellt:** `nachstellen.test.cjs` nutzt echte Aufgaben aus `inhalte/themen` und `setup()` aus den App-Tests. Bewertung und Serie werden so berechnet wie in der Datenbank. Ergebnisse stehen in `protokoll.json`, die Bilder in `bilder/`.
  Start: `PW_TEST_EXECUTABLE=/usr/bin/google-chrome node --test inhalte/pruefung/rueckmeldung/nachstellen.test.cjs`
- **Echte Nutzung:** Bisher gibt es zu wenig Daten. Kind A hat 34 Übungsantworten gegeben (7 falsch, 2-mal Tipp), Kind B 3. Das reicht nicht für eine Auswertung. Die einzelnen falschen Antworten habe ich nicht gelesen. Das braucht Sebastians Freigabe.

Kennzeichnung: **[nachgestellt]** = mit Bild/Protokoll belegt · **[Code]** = aus dem gelesenen Code abgeleitet, nicht durchgespielt · **[Annahme]** / **[Meinung]**.

---

## Kurzfassung

- **Das Gute:**
  - Jede der 9 274 Übungsaufgaben hat einen Tipp und einen Lösungsweg. Die Tipps verraten fast nie die Lösung (7 von 4 910 Zahl-Aufgaben).
  - Bei Formfehlern hilft die App freundlich weiter, etwa bei Punkt statt Komma oder bei leeren Feldern.
  - Bei Zahl-Aufgaben zeigt eine „Kurskorrektur“ Stelle für Stelle, wo die eigene Zahl vom Ziel abweicht.
- **Das Hauptproblem bei der Rückmeldung:**
  - Nach einem Fehler steht sofort die Lösung da.
  - Was danach kommt, ist immer gleich, egal welcher Fehler gemacht wurde.
  - Der „Fehler-Detektiv“ passt oft nicht zum tatsächlichen Fehler.
  - Das Kind korrigiert sich nie selbst.
- **Das Hauptproblem beim Lernweg:**
  - Eine falsch gelöste Aufgabe kommt nach drei anderen Aufgaben wieder, mit gerade gesehener Lösung. Die gemerkte Antwort zählt dann für „sitzt“.
  - Ein einziger Fehler in der Wiederholung setzt die Karte ganz auf null. Danach verschwindet sie aus der Wiederholung, obwohl die App „kommt bald nochmal dran“ sagt.
- **Ein Darstellungsfehler mit hoher Wirkung:** Gefärbte Flächen in Zeichnungen sind kaum zu sehen (Kontrast 1,05 : 1 hell, 1,32 : 1 dunkel). Das betrifft 169 Übungsaufgaben wie „Wie viel Prozent sind gefärbt?“ und 41 Lernkarten.

---

## 1. Befunde: Rückmeldung nach einer falschen Antwort

| Nr. | Befund | Beleg | Schwere |
|---|---|---|---|
| F1 | **Die Lösung kommt sofort, es gibt keinen zweiten Versuch.** Nach dem ersten Fehler zeigt die App „Richtig ist: …“ und den Lösungsweg. Das Kind sucht den Fehler nie selbst. Die Forschung nennt das „Rückmeldung mit der richtigen Antwort“; günstiger gilt eine Rückmeldung mit Hinweis und neuem Versuch (Shute 2008). | [nachgestellt] `r1-vorzeichen-handy.png`; [Code] `lernen.js` Z. 1225 ff. | hoch |
| F2 | **Die Rückmeldung hängt nicht vom Fehler ab.** Ob „5“ statt „−5“ (Vorzeichen), „999“ oder „75 €“: der Text ist gleich. Die Datenbank erkennt „falsche Einheit“ schon (`antwort_bewerten` liefert `grund: falsche_einheit`), aber `uebung_pruefen_intern` gibt das nicht weiter. | [nachgestellt] `r3-einheit-handy.png`, `protokoll.json` r3; [Code] | hoch |
| F3 | **„Fehler-Detektiv“ passt oft nicht.** Es erscheint immer der eine Fehlertext der Lernkarte. Beispiele: Kind wählt „parallel“, der Detektiv erklärt „senkrecht“ (`r6`). Kind vertauscht m und t, der Detektiv erklärt das Einsetzen eines Punktes (`r5`). Für das Kind wirkt das wie: „Das habe ich doch gar nicht gemacht.“ | [nachgestellt] `r5-kl8-vertauscht-handy.png`, `r6-auswahl-falsch-handy.png` | mittel |
| F4 | **„FAST – KURSKORREKTUR“ steht über jeder falschen Antwort**, auch bei „999“ statt „−56“ und bei einer falschen Auswahl. „Fast“ stimmt dort nicht. Bei Auswahl- und Lücken-Aufgaben gibt es auch keine Kurs-Grafik. | [nachgestellt] r2, r5, r6 | mittel |
| F5 | **Nach zwei oder mehr Fehlern hintereinander ändert sich nichts.** Es kommt keine leichtere Aufgabe, kein Vorschlag, die Erklärung anzusehen, und kein „Frag nach“. Das Kind sieht die Bordkarte, die Lösung und die nächste Bordkarte. Im neuen Design klappt die Erklärung nach einem Fehler nicht auf (`!neu` in Z. 1224); im alten Design schon. | [nachgestellt] `r5-kl8-zweiter-fehler-handy.png`; [Code] | mittel |
| F6 | **Auswahl-Aufgaben:** Die gewählte falsche Antwort wird nicht rot, die richtige Antwort in der Liste nicht grün markiert. Die Lösung steht nur als Text darunter. | [nachgestellt] `r6` | niedrig |
| F7 | **Schreibweise der Lösung:** „Richtig ist: -5“ mit Bindestrich statt Minuszeichen. „Richtig ist: −3x + −1“ statt „−3x − 1“. In der Kurs-Grafik steht das Ziel als „2 4 ,“ mit Komma ohne Nachkommastellen. | [nachgestellt] r1, r5, r3 | niedrig |
| F8 | **Tipp und Sterne passen nicht zusammen.** Der Tipp sagt „zählt nicht für die Punkte“; danach gibt es trotzdem „+10 Sterne“. Für die Serie zählt die Antwort richtig nicht. Für ein Kind sind „Punkte“ und „Sterne“ kaum zu unterscheiden. | [nachgestellt] `r4-tipp-richtig-handy.png` | niedrig |
| F9 | **Gefärbte Flächen kaum sichtbar:** Die Füllung `.lern-zeichnung .flaeche` ist Gelb mit 12 % Deckkraft. Kontrast: 1,05 : 1 auf Weiß, 1,32 : 1 auf Dunkel; für Grafiken sind mindestens 3 : 1 üblich (WCAG 1.4.11). Betroffen sind 169 Übungsaufgaben, 51 Sicherungsaufgaben, 19 Korrekturaufgaben, 8 Testaufgaben und 41 Lernkarten mit Fläche. Bei „Wie viel Prozent sind gefärbt?“ (33 Aufgaben) ist die Aufgabe damit praktisch nicht lösbar. | [nachgestellt] `r9-flaeche-tag.png`, `r9-flaeche-nacht.png`, `r3-dezimal-statt-prozent-handy.png` | **hoch** |
| – | **Gut:** Formhinweise helfen ohne Strafe weiter, etwa „Bitte schreibe Dezimalzahlen mit Komma …“ oder „Fehlt ein Glied, trage 0 ein“; die Aufgabe zählt dabei nicht als falsch. Auf dem Tablet steht die Rückmeldung im ersten Bildschirm (438–806 px von 1 180). Der Reiter „Fehler“ listet „Hat bei dir noch nicht geklappt“. | [nachgestellt] r8; [Code] | – |

## 2. Befunde: Lernweg (führt die App das Kind allein weiter?)

| Nr. | Befund | Beleg | Schwere |
|---|---|---|---|
| L1 | **Eine gemerkte Lösung zählt für „sitzt“.** Eine falsch gelöste Aufgabe wird an Stelle 4 wieder eingereiht (`warte.splice(3, 0, a)`). Nachgestellt: 1. Aufgabe falsch → Lösung „−56“ gesehen → 3 andere richtig → dieselbe Aufgabe mit „−56“ richtig → Serie 4 von 4 → „GELANDET“. Damit besteht ein Viertel des „Sitzt“-Nachweises aus einer Antwort, die gerade zu sehen war. | [nachgestellt] `protokoll.json` r2, `r2-gelandet-mit-wiederholter-aufgabe-handy.png` | hoch |
| L2 | **Ein Fehler in der Wiederholung setzt alles zurück, und die Karte verschwindet danach aus dem Blick.** `karte_buchen`: falsch bei „sitzt“ setzt `sitzt=false`, die Serie auf 0, die Stufe auf 0 und `faellig_am=null`. `schule_wiederholung` holt nur Karten mit `sitzt`. Die Karte kommt also nicht wieder in die Wiederholung. Sie taucht erst wieder auf, wenn das Kind das Thema selbst öffnet oder ein Nachtest (frühestens nach 10 Lerntagen) das Lernziel prüft. Hat ein Test das Lernziel früher bestätigt, zeigt die Karte weiter „sitzt“ (`etappen_stand.fertig`). | [Code] | hoch |
| L3 | **Die Meldung am Ende der Wiederholung widerspricht dem.** Ein großer grüner Haken, darunter „0 von 1 richtig“, dazu „Was nicht geklappt hat, kommt bald nochmal dran“ (siehe L2). | [nachgestellt] `r7-wiederholung-falsch-handy.png` | mittel |
| L4 | **Wiederholungen versperren das Neue.** Der Startknopf auf „Heute“ führt zuerst in die Wiederholung, solange etwas fällig ist, in Paketen zu je 3. Jede Karte wird 5-mal wiederholt (nach 1, 3, 7, 14, 30 Tagen). Bei 2 neuen Karten je Lerntag sind das im Dauerbetrieb etwa 10 Wiederholungsaufgaben am Tag [Rechnung]. Die Abstände laufen in **Kalendertagen**, die Nachtests dagegen in **Lerntagen**. Nach einer Reisepause von 2 Wochen ist fast alles auf einmal fällig, und das Kind muss sich vor dem Thema durch alle Pakete arbeiten [Code + Annahme]. | [Code] `lernen.js` Z. 334, 370; SQL `v_abst` | mittel |
| L5 | **Zwei Wiederholungssysteme nebeneinander:** Karten-Wiederholung (Tage, eine Aufgabe je Karte) und Nachtest je Thema (10/25/60 Lerntage, Schwellen 80 %/60 %, „Rückreise“). Für das Kind heißt beides „wiederholen“. Wann was kommt, ist für Kind und Eltern nicht zu durchschauen [Meinung]. | [Code] | niedrig |
| L6 | **Raten** ist kaum ein Problem: Reines Raten durch 4 richtige in Folge gelingt bei Karten nur mit 3er-Auswahl (73 Karten) mit 1,2 % Wahrscheinlichkeit. Die richtigen Antworten sind gleichmäßig auf die Plätze verteilt (4er-Auswahl: 490/492/495/476). Das echte „Durchkommen ohne Können“ ist L1. | [Zählung] | – |
| L7 | **Festhängen erkennt nur die Elternansicht** („wackelt“ ab 3 Fehlern und mehr Fehlern als richtigen Antworten). Das Kind selbst bekommt keinen anderen Weg angeboten (siehe F5). | [Code] Z. 1916 | mittel |

---

## 3. Vorschläge (nach Wirkung geordnet)

| Nr. | Vorschlag | Was genau | Wo | Aufwand |
|---|---|---|---|---|
| V1 | **Flächen sichtbar machen** | `.flaeche` mit kräftiger Füllung (Kontrast ≥ 3 : 1 hell und dunkel), z. B. Akzentfarbe mit 45–55 % Deckkraft plus Kontur. Hunderterfeld-Aufgaben einmal mit beiden Kindern prüfen. | `style.css` | klein |
| V2 | **Erst ein zweiter Versuch, dann die Lösung** | Erster Fehler: „Noch nicht – schau noch mal“ plus passender Hinweis (V3) oder Tipp; die Eingabe bleibt stehen und ist änderbar. Zweiter Fehler: Lösung, Lösungsweg, Detektiv wie heute. Richtig im zweiten Versuch zählt nicht für die Serie, bricht sie aber auch nicht. | `lernen.js` Üben + `uebung_pruefen_intern` (Versuchsnummer) | mittel |
| V3 | **Rückmeldung nach Fehlermuster** | Allgemeine Regeln in `antwort_bewerten`, die einen `grund` zurückgeben:<br>• Zahl hat das falsche Vorzeichen → „Prüf das Vorzeichen.“<br>• Zahl ist um ×10/×100/÷10/÷100 verschoben → „Prüf das Komma / die Einheit.“<br>• falsche Einheit → „Achte auf die Einheit.“<br>• Lücken richtig, aber vertauscht → „Die Zahlen stimmen, die Reihenfolge nicht.“<br>• Ergebnis gerundet statt genau.<br>Diese Gründe weitergeben (heute gehen sie verloren) und als ersten Satz der Rückmeldung zeigen. | Datenbank (`antwort_bewerten`, `uebung_pruefen_intern`), `lernen.js` | mittel |
| V4 | **Fehler-Detektiv nur, wenn er passt** | Inhalte: optional je Aufgabe `fb` (Fehlbilder), z. B. `[{"antwort": 5, "text": "Minus vergessen? …"}]`; bei Auswahl ein Text je falscher Option. Die App zeigt den passenden Text. Ohne Treffer kommt **kein** Detektiv statt des allgemeinen Kartentextes; der Kartentext bleibt im Reiter „Fehler“. | Inhaltsformat + `lernen.js` | mittel (Inhalte: groß, schrittweise) |
| V5 | **Gemerkte Lösung zählt nicht** | Nach einem Fehler kommt statt derselben Aufgabe eine **andere** Aufgabe derselben Stufe (genug Vorrat: 14–18 je Karte). Die falsch gelöste Aufgabe erst nach einer späteren Sitzung wieder. Alternativ in `karte_buchen`: Eine Aufgabe, die in den letzten 24 h falsch war, zählt nicht für die Serie. | `lernen.js` (Reihenfolge) und/oder `karte_buchen` | klein |
| V6 | **Fehler in der Wiederholung: eine Stufe zurück, nicht auf null** | Falsch → `wdh_stufe` −1 (mindestens 0), `faellig_am` = morgen, Karte bleibt in der Wiederholung. Erst bei 2 Fehlern hintereinander zurück auf „üben“, dann aber sichtbar: Karte auf „Heute“ als „Wackelt – kurz üben“. | `karte_buchen`, „Heute“ | klein |
| V7 | **Ehrliche Meldungen** | Kein großer Haken bei 0 richtig, sondern z. B. „1 Karte braucht noch Übung – morgen kommt sie wieder“. „FAST“ nur, wenn ein Fehlermuster aus V3 erkannt wurde, sonst „Noch nicht“. Tipp-Hinweis: „zählt nicht für die Serie“ statt „Punkte“. | `lernen.js` | klein |
| V8 | **Nach 2 Fehlern in Folge: anderer Weg** | Angebot: „Leichtere Aufgabe“ (Stufe −1), „Beispiel ansehen“ (Erklärung bei der Bildergeschichte öffnen) und nach 3 Fehlern „Frag Mama/Papa – die sehen, wo es hakt“. Gleichzeitig kommt die Karte in die Elternansicht oben. | `lernen.js` | klein |
| V9 | **Wiederholung reisetauglich** | Abstände in **Lerntagen** statt Kalendertagen (wie die Nachtests). Höchstens 6 Wiederholungen vor dem Thema; der Rest kommt nach dem Üben oder am nächsten Tag. „Weiter mit dem Thema“ immer erreichbar. | `karte_buchen`/`schule_wiederholung`, „Heute“ | mittel |
| V10 | **Auswahl: gewählte und richtige Antwort markieren** | Falsch gewählte Option rot umrandet, richtige grün. | `lernen.js`/`style.css` | klein |
| V11 | **Schreibweise** | Minuszeichen in `lernZahl`; „+ −1“ → „− 1“ in `lernLoesungText`; Kurs-Grafik ohne Komma, wenn keine Nachkommastellen da sind. | `lernen.js` | klein |
| V12 | **Ein Wort für Wiederholung** | Karten-Wiederholung und Nachtest für Kind und Eltern in einer Ansicht erklären („Was kommt wann wieder?“) [Meinung]. | Eltern- und Kindansicht | klein |

**Umsetzungsreihenfolge (Empfehlung):**
1. V1, V5, V6, V7, V10, V11 zuerst. Sie sind klein und beheben Fehler, die das Lernen verfälschen oder verwirren.
2. Danach V2, V3, V8.
3. Danach V9, V4 und V12.

## 4. Was echte Nutzungsdaten klären würden

Sobald die Kinder einige Wochen geübt haben, und nur mit Sebastians Freigabe:
- **Häufigste falsche Antworten je Lernkarte.** Daraus werden die Fehlbilder für V3/V4. Die Elternansicht „Was wackelt?“ zeigt sie schon.
- **Was nach einem Fehler passiert:** Wie oft ist die wiederholte Aufgabe richtig, wie oft die nächste neue Aufgabe? Das misst L1 und V5.
- **Wie oft wird der Tipp genutzt** und hilft er? Gemessen als „richtig nach Tipp“.

## 5. Offen / Annahmen

- Die Wiederholungslast in L4 ist gerechnet (5 Wiederholungen je Karte), nicht gemessen.
- L2 ist aus dem Code abgeleitet und nicht in der echten Datenbank durchgespielt. Die Datenbank wurde nur gelesen.
- Im Nachstell-Skript ist die Bewertung der Datenbank nachgebaut (`bewerte` und Serienlogik). Für Zahl-, Auswahl- und Lücken-Aufgaben stimmt sie mit `antwort_bewerten` und `karte_buchen` überein. Nicht nachgebaut: Text-Aufgaben und `toleranz`-Sonderfälle.
- Quelle zu F1/V2: V. J. Shute, *Focus on Formative Feedback*, Review of Educational Research 78 (2008) 153–189.
