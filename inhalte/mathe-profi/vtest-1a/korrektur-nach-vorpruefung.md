# Korrektur nach der Vorprüfung (Runde VT1A)

Grundlage: `vorpruefung.md` (Zweig `vorpruefer-vt1a`, Commit 8257cf21). Alle A- und B-Befunde sind eingearbeitet, die C-Befunde einzeln umgesetzt oder begründet gelassen. Die Kennungen (VT1A-nnn) bleiben gleich: an derselben Stelle steht jetzt die neue Aufgabe. „Idee“ bezeichnet das Feld `idee` im JSON (Denkfigur der Aufgabe).

Ergebnis: **40 Aufgaben ersetzt**, 8 geändert (Text, Lösungsweg oder Fehlbild), 29 unverändert. Je Lernziel mindestens 5 verschiedene Ideen, keine Idee öfter als zweimal (`bauen.py` prüft das; Ideen-Zahl je Lernziel: schreibweise 7, quadrat 7, zehner 7, sach (Potenzen) 5, klammern 5, termaufbau 6, vorteil 7, verteilen 7, umkehraufgabe_mal 6, ueberschlag 6, sach (Rechengesetze) 6).

## A

| Kennung | Befund | alt → neu |
|---|---|---|
| 040 | Parkhaus mehrdeutig (angefangene Stunde) | Text: „Es wird nur für volle Stunden bezahlt … Für wie viele Stunden wurde bezahlt?“ Antwort 6 bleibt, nun eindeutig. |

## B

| Kennung | Befund | alt → neu |
|---|---|---|
| 001 | Standard-Fehlvorstellung, als Test zu leicht | ersetzt: „3² + 2³ = 5⁵“ mit drei Fehlvorstellungen als Ablenker (Idee begruenden_fehlvorstellung) |
| 002 | Bestand-Niveau, Sollantwort 3 wie 004 | ersetzt: Was-wäre-wenn „aus 2⁶ wird 2⁷“ |
| 003 | Fehlbild 64 falsch erklärt, Tabelle trägt nichts | Tabelle entfällt (Werte im Text), Fehlbild 64 neu erklärt (Generationsnummer als Basis), Fehlbild 8 und 32 neu |
| 004 | Bestand-Niveau, Sollantwort 3 | bleibt als einzige Aufgabe „Exponent suchen“ in `schreibweise` (Sollantwort 3 kommt nur noch einmal vor) |
| 006 | Rechnen; Doppelung `vertauschen` | ersetzt: Begründung, warum 2⁴ = 4² trotz Vertauschungsverbot gilt (Zufall der Zahlen) |
| 007 | Dieselbe Aufgabe wie 001 | ersetzt: Fehler in 2 · 3² = 6² mit Berichtigung |
| 016 | Doppelung rollend-5 (3 400 000) | ersetzt: andere Zahl (56 000 000), andere Schreibweisen |
| 017 | Fehlbild 3 führt nicht zur Zahl | Fehlbild 3 ersetzt durch 2 („Umrechnung kg in g vergessen“) mit Rechnung |
| 018 | Kein Verstehen (Nullen streichen) | ersetzt: 45 · 10⁵ gegen 450 · 10⁴, wer hat recht |
| 020 | Doppelung rollend-12, Schema | ersetzt: Fehler in 10³ + 10³ = 10⁶ |
| 026 | Doppelung rollend-5, Tabelle als Bild | ersetzt: Werte im Text, andere Zahlen (4er-Folge), andere Ausdrücke |
| 030 | Rechnen nach Schema | ersetzt: Zahl im Kästchen in (□ + 4) · 3 − 5 = 25 (Klammer rückwärts) |
| 031 | passt nicht zu `klammern`, Schablone | ersetzt: Term 40 − (12 + 8) : 4 → Beschreibung in Worten |
| 034 | Rechnen nach Schema | ersetzt: Rechenzeichen so einsetzen, dass 23 herauskommt |
| 037 | mehrdeutig, Schablone | ersetzt: bei welchem Term ist der letzte Schritt ein Malnehmen |
| 039 | Lösungsweg behauptet, die Klammer sei nötig | Lösungsweg berichtigt (Klammer fasst zusammen; ohne Klammer 20 − 4 · 3 − 2 · 2) |
| 041 | zu leicht | ersetzt: für welche Zahl □ sind 8 + 5 · □ und (8 + 5) · □ gleich |
| 042 | Rechnen ohne Aufstellen | ersetzt: wie ändert sich der Term, wenn der Rabatt steigt (Was-wäre-wenn) |
| 044 | Mustererkennung | ersetzt: 83 − 29 + 17 umstellen, alle Ablenker mit Plus und Minus bzw. Klammer |
| 045 | geschickt nur im Lösungsweg | ersetzt: 25 · 17 · 4, welcher erste Schritt ist am geschicktesten und warum |
| 046 | gleiche Zahlen wie 048 | bleibt unverändert; 048 geändert |
| 047 | Doppelung Bestand, ein Schritt | ersetzt: 4 · □ · 25 = 700 geschickt |
| 048 | gleiche Zahlen wie 046 | ersetzt: Bens Fehler bei 4 · 18 · 25 (andere Zahlen) |
| 053 | Doppelung Bestand | ersetzt: 4 · 27 auf zwei Wegen (20 + 7 und 30 − 3), wer hat recht |
| 055 | Verfahren vorgegeben | ersetzt: wie rechnet man am geschicktesten, mit Begründung (Verfahren nicht genannt) |
| 066 | Standard-Runden | ersetzt: 3 · 198 € mit 3 · 200 € überschlagen, in welche Richtung liegt der Fehler |
| 067 | Rechnen | ersetzt: zwei Überschläge (Tausender, Hunderter) vergleichen |
| 068 | Rechnen | ersetzt: Lager mit 1 000 Plätzen, der Überschlag 20 · 50 reicht nicht |
| 069 | übliche Rundung als „Fehler“, „17 %“ | Neu: der Fehler ist der Schluss „passt nicht, also falsch“; Lösungsweg ohne Prozent; Option 0 ersetzt |
| 009 | zu leicht (Quadratzahl erkennen) | ersetzt: zwischen welchen benachbarten Quadratzahlen liegt 150 |
| 031/037 | Mehrdeutigkeit „gleich viele Gäste“ | 037 ersetzt (siehe oben) |
| 051, 072, 074 | schwach | 051 und 072 bleiben (zählen als Idee „Platzhalter im Distributivgesetz“ bzw. „Gesamt − Teil, geteilt durch Anzahl“, höchstens zweimal je Lernziel); 074 ersetzt: Mias und Toms Rechenweg in vertauschter Reihenfolge |
| 002/004 | Sollantwort 3 im selben Pool | nur 004 hat noch 3; 002 ist eine Auswahl-Aufgabe |

## C

| Kennung | Befund | Umgang |
|---|---|---|
| 005 / 011 | nah beieinander | 011 ersetzt (Quadrat mit Seite 3 cm + 4 cm); 005 bleibt |
| 008 | Doppelung Klasse 9 | ersetzt: zweites Feld mit doppeltem Umfang, Fläche gesucht |
| 012 / 013 | gleiche Idee | 013 ersetzt (Fehler in (3 + 4)² = 3² + 4²); 012 bleibt |
| 024 | Ähnlichkeit Kombinatorik | Einkleidung Passwort statt Zahlenschloss |
| 029 | 5 Optionen, README „immer 4“ | bleibt (5 Optionen); README berichtigt |
| 032 / 059 / 065 | Fehlbild-Texte ungenau | 032 und 065 umformuliert; 059 ersetzt (zwei Zahlen mit Produkt 48 und Summe 14) |
| 036 / 043 / 050 | als Stufe 3 zu leicht | ersetzt durch anspruchsvollere Tests (036 mehrere Terme zur Geschichte, 043 erlaubte Umformung bei Minus, 050 Begründung für 7 · 98) |
| 049 | Frage ungenau | „richtig begründet“ |
| 050 / 054 | gleiche Idee | 054 ersetzt (Höhe verdoppelt) |
| 054 | verneint | durch den Austausch entfällt die Verneinung; 016 behält „NICHT“ (eindeutig, begründet) |
| 060–063 | x und □ gemischt | bleibt: x steht dort, wo eine Gleichung gedeutet wird (a · x = b nach Lehrplan M5 3.1); □ steht für eine Lücke in einer Rechnung |
| 062 | Option „nicht durch 7 teilen darf“ | ersetzt durch „Weil 7 eine Primzahl ist“ (widerlegt durch 7 · 7 = 49) |
| 070 | erratbar | ersetzt: Summe der kleinsten und größten Zahl (9 199), Stufe 2 |
| 071 / 075 | gleiche Idee | 075 ersetzt (Tarifvergleich) |
| 073 | Dezimalzahl im Fehlbild | „keine natürliche Lösung“ |
| 008, 012, 024, 074 | Doppelung / Einkleidung | siehe oben; 074 ersetzt |
| 011 (alt) 8² | Standardwissen | ersetzt |

## Stufen, Regeln, Auswahl

- Tests: alle 11 sind Stufe 3 und deutlich anspruchsvoller als zuvor (001, 036, 043, 050 ersetzt).
- Regel bei `ueberschlag`: `id.zahlen.buendeln` trägt den Weg nicht. Alle 7 Aufgaben stehen jetzt **ohne Regel**, mit Begründung in `regeln-zuordnung.md` (im Katalog gibt es keinen Eintrag zum Überschlagen und Runden). `vtest_pruefen.py` meldet dazu 7 Hinweise „Regel fehlt (Lernkarte hat id.zahlen.buendeln)“, bewusst.
- `auswahl.md`: Begründung berichtigt (negative Zahlen gehören laut Vorprüfung zum Jahrgang 5); `negativ`, `mal_ganz`, `geteilt_ganz`, `vertauschen`, `schriftlich` sind für eine Folgerunde vorgemerkt.
