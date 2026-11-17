# Postfach winkelsaetze-2 (Sechzehnte Runde: Flug „Winkelsätze“ nachbessern)

## 2026-11-17 – FERTIG
Zweig `winkelsaetze-2` (von `lernen-app`). Geändert: nur `inhalte/generatoren/geometrie.winkelsaetze.py` und die daraus erzeugte `inhalte/themen/geometrie.winkelsaetze.json`.
Keine Datenbank, kein App-Code, keine Tests, keine anderen Themen, kein Merge.

**Prüfung:**
- `python3 -I tools/inhalt_pruefen.py inhalte/themen/geometrie.winkelsaetze.json` meldet **OK**: 8 Lernkarten, 224 Aufgaben, 158 nachgerechnet, ohne Hinweise.
- Mengen je Etappe unverändert: 18 Übungen (4/6/8), 1 Test, 3 Korrektur, 6 Sicherung. Je Etappe 2 Prüfungsvorbilder und 1 Knobelaufgabe.
- Zeichnungen per Skript geprüft: 259 angeschriebene Winkel (Karten, Schritte, fehler_bild, Bordkarten). Jeder gezeichnete Winkel weicht höchstens 3° ab, tatsächlich 0°, weil alle Zeichnungen jetzt maßstäblich gerechnet werden.
- Weitere Skriptprüfungen:
  - Jede figuren-Bordkarte hat ein Bild.
  - Jede vieleck-Bordkarte der Stufen 1 und 2 hat ein Bild.
  - Kein „∠“, kein x-Ansatz, keine Zahl ≥ 1 000 ohne Leerzeichen.
  - Basiswinkel nur in einer Aufgabe der Etappe aussenwinkel.
- Alle 224 Bordkarten habe ich von Hand gelesen; Lösungen und Lösungswege nachgerechnet.

### Bericht pruefung-winkelsaetze – A (vor der Freigabe)
| Befund | Stand |
|---|---|
| #51 „weder noch“ bei S ro / T lu | **behoben.** Nur noch eindeutige Paare: Stufenwinkel in gleicher Lage, Wechselwinkel lu/ro und ru/lo. „weder noch“ nur für Paare, die an Parallelen nie gleich groß sind (ro/lo, lo/ro, lu/ru, ru/lu). Der Lösungsweg erklärt, warum. Karte stufen_wechsel, Wort „Wechselwinkel“: Satz ergänzt, dass manche Bücher auch die äußeren Paare über Kreuz so nennen. |
| #39 [CB] rechts bei C mehrdeutig | **behoben.** Zeichnung (Dreieck zwischen Parallelen); Text sagt „rechts von C (siehe Bild)“. |
| #67/#69/#71/#73 Außenwinkelsatz in parallel_pruefen | **anders gelöst.** Der Generator-Typ „schnitt“ ist gestrichen. Die feste Aufgabe (75°/68°) wird mit einer Parallelen g′ durch T begründet: Stufenwinkel 75° gegen 68°, Unterschied 7°. Kein Außenwinkelsatz, mit gekippter Zeichnung. Neu auf Stufe 3: „Welche zwei von a, b, c sind parallel?“ und „a ∥ b, b ∥ c: Winkel bei c“. |
| Bildergeschichte innenwinkelsumme | **behoben.** Jeder Schritt hat ein eigenes Bild mit der gestrichelten Parallelen p. Die Wechselwinkel bei C (links α, rechts β) sind eingezeichnet. Text: „Links von C entsteht ein Winkel so groß wie α: Wechselwinkel.“ |
| Lineare Gleichungen (#42, #44, #45, #97, #98, #126, #127, #129, #150, #157 und Lösungswege #4, #6, #12, #88, #100, #155) | **behoben.** Kein x mehr. Die Aufgaben stehen als „Teile“-Aufgaben: „k-mal so groß“, Verhältnis, „um d größer“ („Unterschied wegnehmen, dann halbieren“). Regelmäßiges Vieleck rückwärts geht über Probieren mit (n − 2) · 180° : n. |
| #97/#98 „Wie groß ist x?“ mit Einheit Grad | **behoben.** Die Aufgabenart ist ersetzt; es gibt keine Frage nach x mehr. |

### Bericht pruefung-winkelsaetze – B
| Befund | Stand |
|---|---|
| aussenwinkel als Pflicht | **behoben.** `bewertung.lernziele_vertiefung = ['aussenwinkel']`, Pflicht sind die anderen 7. Auch ziel, merke und quellen nennen den Außenwinkel als Vertiefung. Andere Etappen brauchen den Außenwinkelsatz nicht mehr (beweisen: BEGR-Eintrag und Aufgabe „aussen“ gestrichen). |
| Basiswinkel in aussenwinkel (#117, #119, #130, #131, #135–#139, #122) | **behoben.** Der Typ „gleichschenklig“ ist gestrichen. Neue Stufe 2: Außenwinkel bei A, B oder C rückwärts. Es bleibt eine Aufgabe, die Kreisaufgabe #122: Sie hat eine Zeichnung, den Satz „Im gleichschenkligen Dreieck sind die beiden Basiswinkel gleich groß“ im Text und ∢ statt ∠. |
| Basiswinkel in figuren (#181, #185) | **behoben.** Der Typ ist gestrichen. |
| figuren ohne Zeichnung | **behoben.** Alle 28 Bordkarten haben eine maßstäbliche Zeichnung: Dreieck zwischen Parallelen, Parallelogramm (auch mit Diagonale), Trapez, Raute, Weg A → P → B, drei Geraden, zwei Spiegel. |
| vieleck ohne Zeichnung | **behoben.** Stufen 1 und 2 haben immer eine Zeichnung: Vierecke, Fünfecke und Sechsecke mit den echten Winkeln; regelmäßige n-Ecke mit Diagonalen. Stufe 3 hat teils Zeichnungen. |
| beweisen: Test/Korrektur/Sicherung prüfen nicht das Lernziel | **behoben.** Neue Stufe 2 mit vier Arten: „Fundamentalsatz oder abgeleiteter Satz?“, „Auf welchen Satz stützt sich der Beweis direkt?“, Zirkelschluss (Viereck, Fünfeck, Sechseck) und Reihenfolge der Beweiskette. Test, Korrektur und Sicherung kommen nur noch daraus. Die Zuordnung zu Scheitel-, Neben- und Stufenwinkeln bleibt auf Stufe 1. |
| „Nachbarwinkel“ (#168, #171, #209) | **behoben.** Das Wort kommt nicht mehr vor. Parallelogramm und Trapez werden mit Verlängerung, Stufen- bzw. Wechselwinkel und Nebenwinkel begründet. Die Aufgabe zu #209 (Gegenbeispiel) sagt „die Winkel bei A und B im Parallelogramm“. |
| scheitel_neben #13, #17 verraten den Weg | **behoben.** Der Typ „drei Geraden, Winkel an einer Geraden“ ist auf Stufe 2 verschoben. Neu auf Stufe 3: „zwei Scheitelwinkel zusammen“, „drei der vier Winkel zusammen“ und das Verhältnis zum Nebenwinkel des Scheitelwinkels. |
| innenwinkelsumme: achtmal „zwei gleich große Winkel“ | **behoben.** Die Variante „je x°“ ist gestrichen. „γ gegeben, α = β“ ist eine von fünf Arten, die abwechselnd gewählt werden. Die anderen: k-mal so groß (Teile), Beweisfragen zur Parallelen p, rechtwinklig, „Gibt es das Dreieck?“. |
| figuren #182–#184 dreimal ∢ACD | **behoben.** Auf Stufe 3 gibt es vier Arten, die abwechselnd gewählt werden: Diagonale im Parallelogramm, Weg A → P → B vorwärts und rückwärts, Dreieck zwischen Parallelen. Dazu drei feste Aufgaben. |
| Zeichnung #40 und Abweichungen 6–8° | **behoben.** Alle Zeichnungen sind maßstäblich (Skript: 0 Abweichungen). „offen“ ist angepasst. |
| Bögen bei geneigtem h | **behoben.** `doppel(ro_s, …, ro_t)` dreht h um ro_s − ro_t; T liegt auf h, die Bögen bei T liegen auf h. Betrifft Karten stufen_wechsel (fehler_bild 60°/75°) und parallel_pruefen (Schritt 4: 70°/80°) sowie #66 (jetzt 72°/64°). |

### Bericht pruefung-winkelsaetze – C
| Befund | Stand |
|---|---|
| „6 · 16 + 0“ | **behoben** (Aufgabenart ersetzt). |
| „Verschieden wie bei S“ | **behoben:** „Anders als bei S (…)“. |
| ∠BAC unerklärt | **behoben:** überall ∢. Erklärt in figuren-`woerter`: „∢CAB – der Winkel bei A zwischen [AC] und [AB]; der mittlere Buchstabe ist der Scheitel“. |
| 1440° / 2340° | **behoben:** Zahlen ab 1 000 mit Leerzeichen (`zahl()`), auch in Lösungswegen. |
| fehlende `woerter` | **behoben.** Neu: Winkelsumme (innenwinkelsumme), n-Eck, Diagonale, regelmäßig (vieleck), ∢CAB (figuren). „Außenwinkelsatz“ steht nicht mehr in beweisen. |
| figuren Schritt 4 / Einstieg Dachstuhl | **behoben.** Neuer Einstieg: Regal mit dreieckiger Stütze zwischen zwei Brettern, passend zum Bild. Schritt 4 ist jetzt ein Rechenschritt (Wechselwinkel rechts von C zu ∢ABC) mit eigenem Bild; dazu kommt eine Probe. |

### Bericht pruefung-eltern – Flug „Winkelsätze“
| Befund | Stand |
|---|---|
| 1. Bild „parallel“ bei Lösung „Nein“ (#74–#76) | **behoben.** Bei „nicht parallel“ ist h immer sichtbar gekippt: um 8–10° bei Stufe 2, um 7–8° bei den festen Aufgaben. Die angeschriebenen Winkel stimmen mit der Zeichnung überein. „Ja“ und „Nein“ wechseln ab. |
| 2. „weder noch“ ro/lu | **behoben** (wie A oben, `('ro', 'lo', 'weder noch')` u. a.). |
| 3. Lückenaufgabe nicht eindeutig (#206) | **behoben, etwas anders formuliert.** Kärtchen 1 lautet: „Die drei Winkel an C auf p ergeben 180°. Setzt man α und β ein: α + γ + β = 180°.“ Das Einsetzen braucht Kärtchen 4 (Wechselwinkel). Kärtchen 3 lautet: „Das gilt für jedes Dreieck: Die Winkelsumme ist 180°.“ Damit ist nur 2, 4, 1, 3 schlüssig. |
| Kleinigkeit „+ 0“ | **behoben.** |
| Kleinigkeit „an derselben Kreuzung“ bei Nebenwinkel-Begründungen | **behoben.** Die Begründungsaufgaben in beweisen Stufe 1 nennen „an derselben Kreuzung“ bei Scheitel- und Nebenwinkeln. |
| Kleinigkeit Außenwinkelsatz in parallel_pruefen | **behoben** (siehe A). |
| Kleinigkeit Zeichnungen 4–17° daneben | **behoben** (maßstäblich, 0 Abweichungen). |
| Überschneidung mit geometrie.konstruktion | **nicht umgesetzt (Grund: Auftrag sagt, dort nichts ändern).** Liste unten. |

### Überschneidung mit geometrie.konstruktion (dort nichts geändert)
| geometrie.konstruktion | geometrie.winkelsaetze | Überschneidung |
|---|---|---|
| `parallelen` „Winkel an Parallelen“ | `stufen_wechsel` (auch `parallel_pruefen`) | gleiche Regel „An Parallelen sind Stufen- und Wechselwinkel gleich groß“ |
| `winkelsumme` „Winkel im Dreieck berechnen“ | `innenwinkelsumme` | fehlenden Winkel mit 180° berechnen; winkelsaetze zusätzlich mit Beweis |
| `vierecke` „Winkel in symmetrischen Vierecken“ | `figuren` (Parallelogramm, Trapez, Raute), teils `vieleck` (Viereck 360°) | Parallelogramm: gegenüberliegende Winkel gleich, benachbarte 180° |
| `gleichschenklig` | `aussenwinkel` (nur Aufgabe Kreis/∢BMC, Basiswinkel im Text erklärt) | Basiswinkel |
| `satz_kehrsatz` | `beweisen` (Umkehrung, Gegenbeispiel) | Kehrsatz/Umkehrung, Gegenbeispiel |

### Annahmen und offene Punkte
- **Annahme:** Im Aufbau dieses Flugs ist der Fundamentalsatz „Wechselwinkel an Parallelen sind gleich groß“. So stand es schon in der Karte. LehrplanPLUS lässt laut Prüfbericht auch „oder umgekehrt“ zu. Manche Schulbücher nehmen den Stufenwinkelsatz als Fundamentalsatz. Deshalb heißen die Fragen „In unserem Aufbau der Winkelsätze: …“.
- Raute: ∢CAB = ∢DAB : 2 wird mit der Symmetrieachse begründet (Achsensymmetrie aus früheren Klassen), nicht mit Basiswinkeln.
- Der Weg A → P → B kommt viermal vor: 1 feste Knobelaufgabe in stufen_wechsel und 3 Aufgaben in figuren Stufe 3 (vorwärts und rückwärts). Ich halte das für vertretbar; bei Bedarf in figuren auf 2 kürzen.
