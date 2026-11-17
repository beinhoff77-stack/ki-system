# Postfach winkelsaetze-2 (Sechzehnte Runde: Flug „Winkelsätze“ nachbessern)

## 2026-11-17 02:50 – STATUS
**Achtung, doppelte Bearbeitung:** Auf `winkelsaetze-2` hatte eine andere Sitzung schon um 02:15 dieselbe Nachbesserung gepusht (103b7d6, Prüfskript OK).
Ich habe sie nicht überschrieben. Meine Fassung liegt deshalb auf dem Zweig **`winkelsaetze-2-alt`**. Sebastian entscheidet, welche Fassung eingespielt wird.

## 2026-11-17 02:45 – FERTIG
Zweig `winkelsaetze-2-alt` (gebaut als `winkelsaetze-2` von `lernen-app` 2e95607). Geändert: nur `inhalte/generatoren/geometrie.winkelsaetze.py`, die erzeugte `inhalte/themen/geometrie.winkelsaetze.json` und diese Meldung.
`python3 -I tools/inhalt_pruefen.py inhalte/themen/geometrie.winkelsaetze.json` → **OK** (8 Lernkarten, 224 Aufgaben, 154 nachgerechnet, keine Hinweise).
Der Generator erzeugt die Datei bei jedem Lauf gleich (gleiche Prüfsumme).

Mengen je Etappe wie bisher: 18 Übungen (4/6/8, davon 2 nach Prüfungsvorbild und 1 Knobelaufgabe), 1 Test, 3 Korrektur, 6 Sicherung.

**Prüfung der Zeichnungen, eingebaut in den Generator.** Sie läuft bei jedem Lauf und bricht bei einem Fehler ab. Geprüft werden 179 Bilder: Kartenbilder, Schrittbilder (mit dem Kartenbild zusammengeführt), fehler_bild und alle Aufgaben-Grafiken. Die Regeln:
- Jeder angeschriebene Gradwert weicht höchstens 3° vom gezeichneten Winkel ab.
- Beide Schenkel jedes Winkelbogens liegen auf einer gezeichneten Linie.

Alle Winkel werden jetzt exakt konstruiert. Die Abweichung ist deshalb überall < 0,5° (Rundung der Koordinaten). Ein Gegentest mit absichtlich falschen Bildern wird erkannt.

Zusätzlich habe ich etwa 30 Bilder gerendert und angesehen: Doppelkreuzungen gerade und gekippt, drei Geraden, Dreieck zwischen Parallelen, Weg A–P–B, Vielecke, Parallelogramm mit Diagonale, Trapez, Raute, Spiegel, Kreis, alle Lernkarten-Schrittbilder.

Alle 224 Bordkarten habe ich gelesen. Lösungen: Das Programm rechnet jede Zahl-Lösung über `c` nach, der Generator prüft sie schon beim Erzeugen. Stufe 3 und alle Auswahl-/Lückenaufgaben habe ich zusätzlich von Hand nachgerechnet.

### Teil A (Bericht pruefung-winkelsaetze)
| Befund | Stand |
|---|---|
| #51 „weder noch“ (S rechts oberhalb / T links unterhalb) | **behoben.** Paarliste neu: Stufenwinkel (4 Lagen), innere Wechselwinkel (lu/ro, ru/lo). „weder noch“ gibt es nur noch für ro/lo und lu/ru – an Parallelen nie gleich groß (außer 90°; gezeichnet 60°). Äußere Paare werden nicht mehr abgefragt. Die Lernkarte stufen_wechsel erklärt im Wort „Wechselwinkel“: „Manche Bücher nennen auch die äußeren Paare über Kreuz so.“ |
| #39 mehrdeutig ([CB] rechts bei C) | **behoben:** Zeichnung (Dreieck zwischen g und h, Bogen bei C rechts zwischen [CB] und g) und Text „rechts von C … (siehe Bild)“. |
| #67, #69, #71, #73 Außenwinkelsatz in parallel_pruefen | **anders gelöst:** Die Aufgaben bleiben in der Etappe. Lösungsweg und Tipp begründen jetzt nur mit Stufenwinkeln: „Zeichne durch T die Parallele zu g; sie bildet mit k den Stufenwinkel a, h bildet b – Neigung a − b.“ Jede dieser Aufgaben hat jetzt eine Zeichnung mit sichtbar gekipptem h. Das Wort Außenwinkelsatz kommt außerhalb der Etappe aussenwinkel nicht mehr vor. |
| Bildergeschichte innenwinkelsumme ohne Bilder | **behoben:** Jeder der 4 Schritte hat ein eigenes Bild. Schritt 2 zeigt den Winkel links an C (= α), Schritt 3 zusätzlich den rechts (= β), Schritt 4 nur die drei Winkel auf p. Text jetzt „ein Winkel so groß wie α“. |
| Aufgaben mit linearer Gleichung (#42, #44, #45, #97, #98, #126, #127, #129, #150, #157) | **behoben:** Die Typen „Terme gleichsetzen“ (stufen_wechsel, innenwinkelsumme, aussenwinkel) und „Ecken aus Innenwinkel“ (vieleck) sind entfernt. Feste Aufgabe 144° → n ersetzt durch „Fußball: Fünfeck + zwei Sechsecke an einer Ecke“ (348°). Lösungswege mit x (#4, #6, #12, #88, #100, #155 usw.) rechnen jetzt mit „Teilen“ bzw. „Unterschied wegnehmen“. Im Datensatz steht keine Variable x mehr. |
| #97, #98 „Wie groß ist x?“ mit Einheit ° | **behoben** (Aufgabentyp entfällt). |

### Teil B (Bericht pruefung-winkelsaetze)
| Befund | Stand |
|---|---|
| aussenwinkel nicht im Lehrplan | **behoben:** `bewertung.lernziele_vertiefung = ["aussenwinkel"]`, Begründung unter `offen`. Die anderen Etappen brauchen den Außenwinkelsatz nicht. |
| Basiswinkel in aussenwinkel (#117, #119, #122, #130, #131, #135–#139) | **behoben:** Der Zufallstyp „gleichschenklig“ ist entfernt. In der Etappe bleibt **eine** Aufgabe (Kreis/Durchmesser, Prüfungsvorbild). Ihr Text enthält jetzt „Im gleichschenkligen Dreieck sind die beiden Basiswinkel gleich groß.“, dazu eine Zeichnung. Neue Stufe-2-Typen: „Außenwinkel bei C und α → β“ und „Welche Innenwinkel ergeben den Außenwinkel bei …?“. Neuer Stufe-3-Typ: Außenwinkel und Verhältnis (Teile). |
| Basiswinkel in figuren (#181, #185) | **behoben:** Typ entfernt. Ersetzt durch „∢BAC und Winkel [CB]/g → ∢ACB“ (zwei Schritte: Wechselwinkel, dann gestreckter Winkel). |
| figuren ohne Zeichnung | **behoben:** alle 28 Bordkarten mit Zeichnung (Typ figur), im Generator per assert gesichert. Neue Zeichenbausteine: Parallelogramm (mit Diagonale), Trapez, Raute, Dreieck zwischen Parallelen, Weg A–P–B, Spiegel, zwei sich schneidende Geraden mit Querschnitt. |
| vieleck ohne Zeichnung | **behoben:** Stufe 1 und 2 haben Zeichnungen, ebenso Test, Korrektur und Sicherung (sie sind Stufe 2). Viereck und Fünfeck sind mit den genannten Winkeln exakt gezeichnet, n-Ecke regelmäßig, bei „Winkelsumme im n-Eck“ mit Diagonalen von einer Ecke. Die Lernkarte hat einen 4. Schritt mit Bild: „Im regelmäßigen Fünfeck ist jeder Winkel 540° : 5 = 108°.“ |
| beweisen: Test/Korrektur/Sicherung prüfen Etappen 1–2 | **behoben:** Stufe 2 (daraus kommen Test, Korrektur und Sicherung) ist ein neuer Pool aus 17 Aufgaben zum Lernziel: Fundamentalsatz oder abgeleiteter Satz, woraus ein Satz folgt, Zirkelschluss (3 Fälle), Reihenfolge und fehlender Schritt einer Beweiskette, „darf man diesen Satz benutzen?“. Die Lernkarte hat jetzt das Wort „Zirkelschluss“; Schritt 3 lautet „Winkelsumme im Viereck“ statt „Außenwinkelsatz“. |
| „Nachbarwinkel“ (#168, #171, #209) | **behoben:** jetzt „Winkel an derselben Seite“ bzw. ∢BAD/∢CBA. Das Wort kommt nur noch in der offen-Notiz vor. |
| #13, #17 zu leicht (Text verrät den Weg) | **behoben:** Typ ersetzt durch „Drei Geraden durch einen Punkt“ mit Zeichnung. Zwei nicht benachbarte Winkel sind gegeben, gesucht ist ein dritter. Lösung: Scheitelwinkel verschieben, dann gestreckter Winkel. Die drei Winkel sind verschieden groß. |
| innenwinkelsumme: 8× „zwei gleich große Winkel“ | **behoben:** Typ entfernt. Neu: „rechter Winkel + Winkel“ mit Zeichnung (Stufe 2) und „Seite über B verlängert“ mit Zeichnung (Stufe 3). Der Beweis-Typ kommt jetzt doppelt so oft. |
| figuren #182–#184 dreimal ∢ACD | **behoben:** Die Parallelogramm-Diagonale fragt zufällig nach ∢ACD, ∢ACB oder ∢ABC, immer mit Zeichnung. Im Lauf vorhanden: ∢ABC, ∢ACD, ∢ACB. |
| #40 Weg A→P→B (51° als ≈ 34° gezeichnet), #30, #33, #54, #202 | **behoben:** Alle Zeichnungen sind exakt konstruiert. Die Klemmung 35°–145° in `doppel` ist entfernt, sie war die Ursache für #30/#33/#54. Weg A–P–B wird aus beiden Winkeln berechnet. |
| Bögen bei gekipptem h | **behoben:** `doppel(a, …, b=…)` dreht h um T. Die Hilfsstrahlen bei T liegen auf h, der angeschriebene Winkel bei T ist der gezeichnete. Das gilt für fehler_bild Etappe 2, Schritt 4 Etappe 3 (jetzt 70°/80°) und #66 (jetzt 68°/62°). |

### Teil C (Bericht pruefung-winkelsaetze)
| Befund | Stand |
|---|---|
| #42 „+ 0“ | **behoben** (Typ entfällt; der Generator prüft, dass „+ 0 “ nicht vorkommt). |
| „Verschieden wie bei S“ | **behoben:** „Er ist anders als der Stufenwinkel bei S“ bzw. „gleich groß wie“. |
| ∠-Schreibweise | **behoben:** überall ∢ (z. B. ∢BAC). Erklärt einmal im Wort „∢BAC“ der Lernkarte figuren; Schritt 1 benutzt es. In der Vertiefungs-Etappe steht die Kreis-Aufgabe ohne ∢. |
| 1440° / 1 440° / 2340° uneinheitlich | **anders gelöst:** einheitlich wie in allen Themen über `_bausatz.zt`: vierstellige Zahlen ohne Leerzeichen (1440°, 2340°), ab 10 000 mit Leerzeichen (README-Beispiel „20 000“). Die feste Aufgabe schrieb als einzige „1 440°“, jetzt „1440°“. |
| „Winkelsumme“, „regelmäßig“, „Außenwinkelsatz“ fehlen in woerter | **behoben:** „Winkelsumme“ und „regelmäßig“ stehen in vieleck. „n-Eck“ bleibt, „Diagonale“ ist entfallen, weil höchstens 3 Wörter erlaubt sind; Diagonale ist aus Klasse 5/6 bekannt. „Außenwinkelsatz“ steht in aussenwinkel; Schritt 3 nennt ihn. |
| figuren Schritt 4 = Anweisung; Einstieg „Dachstuhl“ | **behoben:** Schritt 4 ist jetzt ein Rechenschritt (Wechselwinkel rechts bei C, mit Bild), dazu eine Probe „50° + 70° + 60° = 180°“. Neuer Einstieg: Dreieck zwischen zwei parallelen Schienen, passend zum Bild. |

### Bericht pruefung-eltern (Abschnitt „Flug Winkelsätze“)
| Befund | Stand |
|---|---|
| 1. Tasks 74/75/76 parallel gezeichnet, Lösung „Nein“ | **behoben:** Bei „Nein“ ist h um 8–12° gekippt (Winkelunterschied im Text ebenfalls 8–12°, damit Bild und Zahl übereinstimmen). Bei „Ja“ ist h parallel. |
| 2. #51 „weder noch“ | **behoben** (siehe Teil A; ('ro','lo') wie vorgeschlagen, dazu ('lu','ru')). |
| 3. #206 Reihenfolge nicht eindeutig | **behoben:** Kärtchen 1: „Also liegen α, γ und β nebeneinander auf p: α + γ + β = 180°.“ Kärtchen 4: „Die Winkel links und rechts von C auf p sind so groß wie α und β (Wechselwinkel).“ Kärtchen 3: „Damit ist der Satz für jedes Dreieck bewiesen.“ Nur 2, 4, 1, 3 ist schlüssig: 4 braucht p, 1 braucht 4, 3 schließt ab. |
| #42 „+ 0“ | **behoben** (s. o.). |
| Nebenwinkel-Begründungen ohne „an derselben Kreuzung“ (#203, 216, 217, 219, 220, 222) | **anders gelöst:** Diese Begründungsaufgaben in beweisen sind durch den Lernziel-Pool ersetzt (siehe Teil B). Wo die Lage noch beschrieben wird (beweisen Stufe 1), steht jetzt „an derselben Kreuzung“ bei Neben- und Scheitelwinkel. |
| #67/69/71/73 Außenwinkelsatz | **behoben** („Stufenwinkel-Unterschied“ über eine Parallele durch T, siehe Teil A). |
| 9 Zeichnungen 4–17° daneben | **behoben** (exakte Konstruktion, Prüfung ≤ 3° im Generator). |
| Überschneidung mit geometrie.konstruktion | **nicht umgesetzt (Vorgabe):** geometrie.konstruktion nicht geändert, Liste unten. |

### Weitere Änderungen
- Neue Stufe-3-Typen für mehr Abwechslung:
  - stufen_wechsel: „Nebenwinkel bei T, dann Wechselwinkel“ und „Scheitelwinkel bei S, dann Stufenwinkel“ statt der Terme.
  - parallel_pruefen: „Welche zwei von drei Geraden sind sicher parallel?“; der Typ „a ∥ b ∥ c“ kommt seltener.
  - vieleck: „Sechseck mit vier gleichen Winkeln“.
- scheitel_neben Stufe 2: Der Typ „um d größer“ kommt seltener, Lösungswege sprachlich glatter („Scheitelwinkel sind gleich groß: …“).
- Neu mit Zeichnung sind auch Aufgabe „drei Geraden 40°/65°“ (scheitel_neben), #39 und #40 (stufen_wechsel), #66 und #67 (parallel_pruefen), alle drei festen figuren-Aufgaben (Schnittpunkt X, Parallelogramm, Spiegel) und die Kreis-Aufgabe (aussenwinkel).
- `merke`, `ziel`, `offen` und `autor` sind angepasst; in `offen` neu: Vertiefung, Wechselwinkel-Definition, Zeichnungsprüfung.

### Überschneidung mit geometrie.konstruktion (gleicher Ort, nichts geändert)
| geometrie.konstruktion | geometrie.winkelsaetze | Überschneidung |
|---|---|---|
| parallelen „Winkel an Parallelen“ (30 Aufgaben) | stufen_wechsel, parallel_pruefen | Fast deckungsgleich: Stufen-/Wechselwinkel bei S → T mit gleichen Lagenbezeichnungen, „Welche Winkel-Beziehung?“, „Eine Gerade schneidet g und h … parallel?“. |
| winkelsumme „Winkel im Dreieck berechnen“ (30) | innenwinkelsumme, aussenwinkel (Vertiefung) | Gemeinsam: dritter Winkel aus zwei gegebenen; „β k-mal so groß wie α“; rechtwinklige Dreiecke; Parallele durch C (Beweisidee); 6 Aufgaben „Außenwinkel bei C“. |
| vierecke „Winkel in symmetrischen Vierecken“ (30) | figuren, vieleck | Gemeinsam: Parallelogramm (Winkel an derselben Seite), Raute mit Diagonale (Winkel halbieren), „Viereck α, β, γ → δ“. Nur dort: Drachenviereck, gleichschenkliges Trapez. |

Vorschlag wie bisher unter `offen`: In geometrie.konstruktion die Karten „parallelen“ und „winkelsumme“ als Wiederholung kennzeichnen oder auf Konstruktion/Kongruenz kürzen; „vierecke“ kann bleiben (Symmetrie-Schwerpunkt). Entscheidung Sebastian.

### Offen / Hinweise
- Einspielen wie im Auftrag: Entwurf → `einheit_abgleichen(…, 'loeschen')`, danach Nachprüfung und Freigabe durch Sebastian.
- Die Testaufgabe der Vertiefungs-Etappe aussenwinkel bleibt im Datensatz; sie zählt laut README nicht für den Stempel.
