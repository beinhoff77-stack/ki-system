# Zweite Vorprüfung VT1A (Runde 1a, Stand Commit 87a8bfee)

Prüfer: unabhängig, hat die Aufgaben nicht geschrieben. Grundlage: Zweig `helfer-vtest-k5` (Commit 87a8bfee) in meinen Zweig `vorpruefer-vt1a` eingemischt; erste Vorprüfung: `vorpruefung.md` (Commit 8257cf21). Eigene Nachrechnung: `vorpruefung_rechnen_2.py` (eigene Formeln, Zählschleifen, Aufzählung aller Rechenzeichen-Paare; Ergebnis „0 Abweichungen“). Kennzeichnung: **[F]** = Fakt (nachgerechnet oder aus Dateien gelesen), **[A]** = Annahme oder Einschätzung.

## Gesamturteil

**Brauchbar mit Nachbesserung, kein A-Befund mehr.** Alle 77 Sollantworten stimmen (eigene Rechnung, auch für die 47 ersetzten/geänderten). Der A-Befund 040 ist geschlossen. Von den 29 B-Befunden der ersten Runde sind 26 geschlossen, 3 nur teilweise (004, 016, 044/047-Nähe zum Bestand, siehe Tabelle 2). Neu gefunden: **0 A, 7 B, 9 C**. Die B-Befunde sind Bau- und Prüfmängel (Bestand-Nähe, Muster in den Auswahl-Optionen, dünne Ideen-Vielfalt in zwei Lernzielen, eine Test-Aufgabe, die sich durch Ausrechnen lösen lässt), keine falschen Aufgaben. Nach Behebung der B-Befunde 1 bis 7 würde ich die Runde freigeben.

Wichtigstes Urteil für die Test-Tauglichkeit: Das neue Verhältnis 50 Auswahl : 27 Zahl ist vertretbar, **aber** nur, wenn die Auswahl-Optionen nicht an Muster verraten werden. Das ist derzeit nicht der Fall (B7): „Kein Fehler“ ist in 9 von 9 Fällen falsch, „Nur …“ in 6 von 6, „Keiner“ in 2 von 2, „Beide“ in 5 von 9 richtig; die richtige Option ist in 26 von 50 Aufgaben die eindeutig längste. Die tatsächliche Ratechance liegt damit eher bei 35 bis 40 % als bei 25 %.

## Zahlen

| Größe | Wert | Quelle |
|---|---|---|
| Aufgaben | 77 (7 Lernziele ×… je 7; 4 Lernziele Potenzen, 7 Rechengesetze) | [F] `vtest_pruefen.py`, `bauen.py` |
| Sollantworten neu gerechnet | 77 von 77, 0 Abweichungen | [F] `gegenrechnung.py` (Projekt) und `vorpruefung_rechnen_2.py` (eigen) |
| Pools | test 11, korrektur 33, sicherung 33; Stufe 2: 44, Stufe 3: 33 | [F] `bauen.py` |
| Antwortform | 50 Auswahl, 27 Zahl; Test-Pool 7 Auswahl, 4 Zahl; Korrektur 21/12; Sicherung 22/11 | [F] eigenes Skript |
| Optionen je Auswahl | 49 mal 4, 1 mal 5 (029) | [F] |
| Lage der richtigen Option (Index 0/1/2/3) | 12 / 12 / 13 / 13 | [F] ausgewogen |
| Richtige Option eindeutig die längste | 26 von 50; länger als der Durchschnitt der anderen: 36 von 50; mittleres Längenverhältnis 1,28 | [F] |
| Ideen je Lernziel (verschiedene von 7) | schreibweise 7, quadrat 7, zehner 7, sach (Potenzen) 5, klammern 5, termaufbau 6, vorteil 7, verteilen 7, umkehraufgabe_mal 6, ueberschlag 6, sach (Rechengesetze) 6 | [F] Feld `idee` |
| `vtest_pruefen.py --runde 1a` | „OK – keine Fehler“, 10 Hinweise (3 Auswahl/Vorschlag-Abweichung, 7 mal „Regel fehlt“ für 064 bis 070, Lernkarte `id.zahlen.buendeln`) | [F] |
| Nähe zum Bestand (eigene Heuristik, Wort- und Zahlenähnlichkeit gegen 967 Bestandsaufgaben) | auffällig: 044, 047; schwach: 032 | [F] Heuristik, [A] Bewertung |

## 1. Alle ersetzten und geänderten Aufgaben

[F] Alle 47 neu gelesen und die Sollantwort selbst bestimmt. Sonderfälle der Auswahl-Optionen einzeln geprüft:

| Kennung | Prüfung | Ergebnis |
|---|---|---|
| 001 | 3² + 2³ = 17; 5⁵ = 3 125; 3²·2³ = 72. Optionen 1 und 3 (12) und Option 0 („Richtig“) sind falsch, nur Option 2 stimmt | in Ordnung |
| 009 | 150 liegt zwischen 144 = 12² und 169 = 13²; keine Quadratzahl dazwischen; Option 1 (196 = 14²) überspringt 169 | eindeutig |
| 034 | Alle 16 Rechenzeichen-Paare aufgezählt (Punkt vor Strich): genau (+, ·) ergibt 23; die anderen drei Optionen geben 17, 12, 60 | eindeutig |
| 036 | ① und ② = 20, ③ und ④ = 28; nur die Option „Genau ① und ②“ passt | eindeutig |
| 043 | 85 − 38 + 53 = 100 = 85 + 53 − 38; 85 − 53 + 38 = 70; 100 − 47 − 38 = 15, 100 − (47 − 38) = 91; 64 : 8 : 2 = 4, 64 : (8 : 2) = 16 | Sollantwort richtig, siehe B1 |
| 044 | 83 + 17 − 29 ist die einzige gleichwertige Option (83 − 29 − 17, 83 + 29 − 17, 83 − (29 + 17) sind es nicht) | richtig, siehe B2 |
| 045 | 25 · 4 = 100, dann 100 · 17 = 1 700; die anderen ersten Schritte sind mit „von links“, „kleinste Zahlen“, „addieren“ begründet und falsch | eindeutig |
| 053 | 4 · 27 = 4 · 20 + 4 · 7 = 4 · 30 − 4 · 3 = 108; beide Wege gelten | eindeutig |
| 055 | Ausklammern 19 · (36 + 64 − 50) = 19 · 50 = 950; die anderen drei Wege sind falsch oder unklug | eindeutig |
| 068 | 23 · 48 = 1 104 > 1 000; der Überschlag 20 · 50 rundet 23 zu weit ab | richtig |
| 069 | 596 · 12 = 7 152; Überschlag 600 · 12 = 7 200; Option 0 jetzt richtig, Fehler ist der Schluss „passt nicht, also falsch“ | richtig, A/B-Befund aus Runde 1 behoben |
| 008, 030, 040, 041, 042, 044, 048, 059, 066, 067, 070, 074, 075 | Zahl-Sollwerte (576 m², □ = 6 (eindeutig), 6 Stunden, □ = 1, 40 Stufen-Aufgabe, 71, 1 800, 8, 594 < 600, 8 000/8 300/8 299, 9 199, 24, 4 GB) selbst gerechnet | alle richtig |

Fehlbild-Texte, Lösungswege, Sprache: [F] bei 003 (Fehlbild 64: „Nummer der Generation als Basis“, 4³ = 64), 017 (Fehlbild 2: kg-in-g vergessen führt zur gespeicherten Zahl 2), 065, 073 führen die Erklärtexte nun zu den gespeicherten Zahlen. Kleinigkeit: C2. Klasse-5-Sprache und Stoff (M5 3, Potenzen mit ganzzahliger Basis, Terme, Distributivgesetz) passen; 5⁵ = 3 125 in 001 ist als Information in der Option gegeben und nicht gefordert. Tabellen/Bilder gibt es nicht mehr, alle Werte stehen im Text.

## 2. Sind meine A- und B-Befunde wirklich geschlossen?

| Befund (Runde 1) | Kennung | geschlossen? | Begründung |
|---|---|---|---|
| A: Parkhaus mehrdeutig | 040 | **ja** | Text „Es wird nur für volle Stunden bezahlt … Für wie viele Stunden wurde bezahlt?“; 4 + 2 · (h − 1) = 14 hat genau die Lösung 6 |
| B: Standard-Fehlvorstellung, zu leicht für Test | 001 | ja | zwei Fehlvorstellungen in einer Rechnung, Stufe 3 gerechtfertigt |
| B: Bestand-Niveau, gleiche Sollantwort | 002 | ja | Was-wäre-wenn (2⁶ → 2⁷) |
| B: Bestand-Niveau | 004 | **teilweise** | bleibt „Exponent suchen“ (6 hoch ? = 216), nur Sollantwort 3 nicht mehr doppelt; Bestand-Niveau bleibt. Herabgestuft auf C3, weil Korrektur Stufe 2 und nur eine solche Aufgabe in `schreibweise` |
| B: Fehlbild 64 falsch erklärt, Tabelle | 003 | ja | Tabelle entfällt, Fehlbild neu und stimmig |
| B: Rechnen, Doppelung `vertauschen` | 006 | ja | Begründung, warum 2⁴ = 4² trotzdem gilt |
| B: gleiche Aufgabe wie 001 | 007 | ja | 2 · 3² = 6², andere Fehlvorstellung |
| B: Bestand-Nähe, verneint | 016 | **teilweise** | andere Zahl und Schreibweisen (ja), aber weiterhin „NICHT“ gestellt (C1); Nähe zum Bestand behoben |
| B: Fehlbild führt nicht zur Zahl | 017 | ja | Fehlbild 2 mit Erklärung; Rest siehe C2 |
| B: kein Verstehen | 018 | ja | 45 · 10⁵ gegen 450 · 10⁴ |
| B: Doppelung rollend-12 | 020 | ja | Fehler in 10³ + 10³ = 10⁶ |
| B: Doppelung rollend-5, Tabelle | 026 | ja | andere Zahlen und Ausdrücke, keine Tabelle |
| B: Rechnen nach Schema | 030 | ja | Klammer rückwärts, Lösung 6 eindeutig |
| B: Rechnen nach Schema | 034 | ja | Zeichen einsetzen, genau eine Lösung (aufgezählt) |
| B: passt nicht zu `klammern` | 031 | ja | Term in Worten beschreiben |
| B: mehrdeutiger Satz | 037 | ja | Aufgabe ersetzt |
| B: falscher Lösungsweg | 039 | ja | Lösungsweg berichtigt |
| B: zu leicht | 041 | ja | □ = 1, Stufe angemessen |
| B: Rechnen ohne Aufstellen | 042 | ja | Was-wäre-wenn |
| B: Mustererkennung, Bestand | 044 | **teilweise** | Ablenker jetzt stark, aber Aufgabe fast gleich einer Bestandsübung (73 − 29 + 17); neuer B2 |
| B: „geschickt“ nur im Lösungsweg | 045 | ja | Auswahl mit Begründung |
| B: gleiche Zahlen wie 048 | 046, 048 | ja | 048 mit 4 · 18 · 25 |
| B: Bestand-Nähe, ein Schritt | 047 | **nein** | 4 · □ · 25 = 700 ist die Bestandsübung 4 · □ · 25 = 1 700 mit anderer Zahl; neuer B2 |
| B: Bestand-Nähe | 053 | ja | zwei Wege 20 + 7 und 30 − 3 |
| B: Verfahren vorgegeben | 055 | ja | Weg wird gewählt und begründet |
| B: Standard-Runden | 066 | ja | Richtung des Fehlers |
| B: Rechnen | 067, 068 | ja | zwei Überschläge, Lager-Aufgabe; Sonderfälle geprüft |
| B: Fehler des Prüfers markiert | 069 | ja | richtiges Runden wird nicht mehr als Fehler bezeichnet, Lösungsweg ohne Prozent |
| B: Antwort ablesbar 046/048 | 046/048 | ja | andere Zahlen |
| B: Ideen je Lernziel (Bauarten 5 → 4, `bauen.py`) | alle | ja | Werkzeug erzwingt ≥ 5 Ideen, höchstens 2 je Idee; erfüllt |

Ergebnis: **A: 1 von 1 geschlossen. B: 26 von 29 geschlossen; offen bleiben 047 (nein), 044 und 016/004 teilweise.** 004 und 016 stufe ich auf C herunter (C3, C1); 044 und 047 führe ich als neuen B2.

## 3. Wird echtes Verstehen geprüft? (7 Aufgaben je Lernziel nebeneinander)

[A] Maßstab: eine Denkfigur ist verschieden, wenn ein Kind sie nicht durch dieselbe Rechnung oder dasselbe Muster lösen kann.

| Lernziel | Ideen (Kennung) | Urteil |
|---|---|---|
| schreibweise | Fehlvorstellung begründen (001), Was-wäre-wenn (002), Generationen (003), Exponent suchen (004), 2⁴ = 4² (006), 2 · 3² (007), …  | 7 verschiedene, gut |
| quadrat | 009 Nachbar-Quadratzahlen, 008 Umfang/Fläche, 011/012/013 Quadrat und Terme | verschieden, aber 011 und 013 teilen die Zahlen (B4) |
| zehner | 015 Größenvergleich, 016, 017, 018, 020 Fehler, … | 7 verschiedene, gut |
| sach (Potenzen) | Wachstum rückwärts (022), Exponent suchen (023, 024), Term zur Situation (025, 026), Wachstum vergleichen (027), Fehler (028) | **dünn**: genau 5, davon 023/024 und 025/026 jeweils dieselbe Denkfigur und im selben Pool nebeneinander (B5) |
| klammern | Ziel herstellen (029, 034), Klammer-Lücke (030), Term ↔ Text (031, 032), Klammern weglassen (033), Fehler (035) | **dünn**: genau 5, drei davon doppelt; 031/032 beide „Term in Worten“ im Pool korrektur (B6) |
| termaufbau | 6 verschiedene | gut |
| vorteil | Umformung (043), gleichwertiger Term (044), Weg wählen (045), zwei Wege (046), Lücke (047), Fehler (048), gleicher Wert (049) | 7 Etiketten, aber 43/44 sind dieselbe Einsicht („Zahl nimmt ihr Rechenzeichen mit“), und 45, 47, 48, 49 laufen alle über 25 · 4 = 100 (B3, B2); inhaltlich eher 4 bis 5 echte Figuren |
| verteilen | 7 verschiedene | gut |
| umkehraufgabe_mal | 6 verschiedene | gut |
| ueberschlag | 6 verschiedene | gut |
| sach (Rechengesetze) | Gleichung aufstellen (073), Reihenfolge vertauschen (074), Gleichsetzen (075), Gesamt − Teil : Anzahl (072, 076), Fehler (077), Kette rückwärts (071) | 6, in Ordnung; 072 und 076 gleiche Schablone (C6) |

**051** (`17 · □ + 17 · 14 = 17 · 50`, □ = 36): Urteil **lassen**. Die Einsicht („50 − 14, weil 17 gemeinsamer Faktor ist“) ist die Rückrichtung des Distributivgesetzes und eine Denkfigur, die sonst nirgends vorkommt. Man kann es auch durch Ausrechnen lösen (17 · 50 = 850, minus 238, durch 17), das ist aber umständlicher; kein Befund.
**072** (Zoe: 24 €, 7 Wochen, 66 €): Urteil **schwach, aber noch vertretbar** als Korrektur Stufe 2: Rückwärtsarbeiten nach Schema (66 − 24 = 42, 42 : 7 = 6), gleiche Schablone wie 076 (C6). Ersatz wäre besser, kein Muss.

## 4. Auswahl gegen Zahl (50 : 27)

- **Ratechance:** formal 25 % (29: 20 %). Tatsächlich höher durch Muster [F]: „Kein Fehler“ (9 Vorkommen) nie richtig, „Nur …“ (6) nie richtig, „Keiner“ (2) nie richtig, „Beide“ (9) fünfmal richtig (018, 046, 049, 053, 067), „Genau …“ einmal richtig. Bei den 27 „Fehler:“-Optionen ist die richtige Antwort 9 von 27; erkennbar an „Die Hochzahl 2 gehört nur zur 3 …“ (längste, erklärt den Fehler). Ein Kind, das Muster nutzt, hat bei etwa jeder dritten Aufgabe eine Chance von 1 zu 2 bis 1 zu 3. Für einen Test mit 11 Aufgaben (7 davon Auswahl) ist das zu großzügig (B7).
- **Länge/Stil:** richtige Option eindeutig die längste in 26 von 50 Aufgaben, länger als der Durchschnitt der anderen in 36 von 50; in 31 von 50 enthält sie „weil/denn/:“ als Begründung. Beispiele: 001, 036 („Genau ① und ②: Beide ziehen insgesamt 10 Kinder ab …“), 045, 050, 053, 055, 068. [A] Leicht zu beheben: Ablenker gleich lang und gleich begründet formulieren.
- **Ablenker-Stärke:** gut in 001 (Fehlvorstellung 12 mit zwei Begründungen), 009, 034, 044, 050 (Klammer weglassen), 064 (letzte Ziffer 8 passt scheinbar). Schwach in 043 (zwei Ablenker betreffen andere Terme), 068/069 („genau 1 000“, „Überschläge sind nutzlos“), 036 („Eine Klammer darf bei einer Geschichte nicht vorkommen“), 064 („Ein Überschlag kann nie zeigen …“).
- **Test-Aufgaben (Pool test) als Auswahl, die als Zahl-/Lücken-Aufgabe dieselbe Einsicht prüfen könnten:**
  - **043** (vorteil): „85 − 38 + 53 = 85 + □ − 38“ oder besser „8 427 − 3 859 + 1 573 = 8 427 + □ − 3 859“. Prüft dieselbe Einsicht, Ratechance null, und das Ausrechnen lohnt nicht mehr.
  - **064** (ueberschlag): „Tim hat 612 · 49 = 2 998. Um welchen Faktor ist das Ergebnis ungefähr zu klein?“ (Antwort 10, Zahl).
  - **050** (verteilen): „7 · 98 = 7 · 100 − 7 · □“ (Antwort 2) oder „Mia rechnet 7 · 98 = 7 · (100 − □)“.
  - **015** (zehner): „9 · 10⁵ + □ · 10⁴ = 10⁶“ (Antwort 10) würde den Vergleich als Zahl prüfen.
  - **036** (termaufbau) und **029** (klammern) sind als Auswahl sinnvoll, weil mehrere Terme gleichzeitig beurteilt werden; 001 braucht die Begründung.
  Mit diesen vier Änderungen wären im Test 3 von 11 Auswahl und 8 von 11 offen, ohne Verlust an Einsicht.

## 5. Stufe-3-Tests 001, 036, 043, 050

| Kennung | Urteil | Begründung |
|---|---|---|
| 001 | anspruchsvoll, lösbar in Klasse 5 | beide Potenzen ausrechnen (9 + 8) reicht für die Richtung; die Begründung unterscheidet die Fehlvorstellungen. Schwäche: richtige Option die längste und die einzige mit Zusatzinformation (5⁵ = 3 125) (C4) |
| 036 | anspruchsvoll, lösbar | Aufstellen und Beurteilen von vier Termen für eine Geschichte; echte Schulaufgabe. Wer jeden Term ausrechnet (20, 20, 28, 28) und den Wert der Geschichte kennt, löst sie auch ohne Einsicht; akzeptabel. Ablenker 0 und 1 schwach (C5) |
| 043 | **am schwächsten** | zwei der vier Optionen beziehen sich auf andere Terme (100 − 47 − 38, 64 : 8 : 2), obwohl die Frage 85 − 38 + 53 nennt; die Aufgabe ist durch Ausrechnen von zwei Termen lösbar (100 gegen 70), die Begründungen werden nicht gebraucht; dieselbe Einsicht wie 044 (B1) |
| 050 | gut, lösbar | Begründungs-Aufgabe zum Distributivgesetz; Ablenker 3 („7 · (100 − 2) = 7 · 100 − 2“) ist ein typischer echter Fehler. Richtige Option die längste (B7) |

## Befundtabelle neu

### A
Keine.

### B

| Nr | Kennung | Befund | Korrekturvorschlag |
|---|---|---|---|
| B1 | 043 | Test (Stufe 3): zwei Ablenker (100 − 47 − 38, 64 : 8 : 2) gehören nicht zur Frage „Umformung von 85 − 38 + 53“; durch Ausrechnen lösbar; gleiche Einsicht wie 044 | Ablenker auf denselben Term beziehen (85 − (38 + 53), 85 + 38 − 53, 53 − 38 + 85 als richtige Variante prüfen) oder als Lücke mit schweren Zahlen: „8 427 − 3 859 + 1 573 = 8 427 + □ − 3 859“ |
| B2 | 044, 047 (und 045, 048, 049) | 044 ist die Bestandsübung „73 − 29 + 17“ mit 83 statt 73, gleiche Optionsform; 047 ist die Bestandsübung „4 · □ · 25 = 1 700“ mit 700. Zusätzlich laufen 045, 047, 048, 049 alle über 25 · 4 = 100 | 044: andere Struktur (zwei Minus: 94 − 37 − 23 mit Umstellen und Klammer) oder zu 043 verschieben; 047: andere Zahlen und Zusammenhang (z. B. 8 · □ · 125 = 4 000); in 045/048/049 mindestens zwei andere Paare (50 · 2, 125 · 8) |
| B3 | 043 / 044 | Beide prüfen dasselbe („Zahl nimmt ihr Rechenzeichen mit“) | Eine der beiden auf Klammern setzen (a − (b + c)) oder auf Verbinden (a + b) + c |
| B4 | 011 / 013 | Dieselben Zahlen (3 + 4)² = 49: die richtige Option von 011 verrät die Berichtigung in 013 | andere Zahlen in 013 (z. B. (5 + 2)²), Fehler beibehalten |
| B5 | 023, 024, 025, 026 (sach Potenzen) | Genau 5 Ideen; 023/024 beide „Exponent suchen“ nebeneinander im Pool korrektur, 025/026 beide „Term zur Situation“ mit fast gleicher Form; zusätzlich 004 „Exponent suchen“ | 024 ersetzen durch eine weitere Denkfigur (z. B. zwei Wachstumsvorgänge vergleichen, Vervielfachung rückwärts oder Schätzen); dann 6 Ideen |
| B6 | 029/034, 031/032 (klammern) | Genau 5 Ideen; „Ziel herstellen“ (029, 034) und „Term in Worten“ (031, 032) doppelt, 031/032 im selben Pool direkt nebeneinander | 032 ersetzen (z. B. „Klammer erforderlich ja/nein“, Klammern zählen, Term gegen Term vergleichen), 034 behalten |
| B7 | alle Auswahl (50) | Muster: „Kein Fehler“ nie richtig (9/9), „Nur …“ nie (6/6), „Keiner“ nie (2/2), „Beide“ in 5 von 9 richtig; richtige Option in 26 von 50 die eindeutig längste | Mindestens in 007, 013, 020 und 069 je einmal „Kein Fehler“ als richtig einbauen (Rechnung stimmt wirklich); „Beide“ in 4 von 9 falsch machen; Ablenker und richtige Option gleich lang und gleich begründet; Auswahl im Test bei 043, 050, 064, 015 durch Zahl/Lücke ersetzen (Abschnitt 4) |

### C

| Nr | Kennung | Befund | Korrekturvorschlag |
|---|---|---|---|
| C1 | 016 | weiterhin verneint gestellt („NICHT zur Zahl“); Lesefehler kostet | „Welche Schreibweise gehört zu 56 000 000?“ mit drei falschen und einer richtigen Option oder „Bei einer Schreibweise ist der Wert anders“ mit Hervorhebung |
| C2 | 017 | Fehlbild 6 „Ziffern gezählt (5 + 1)“ ist ungenau: 100 000 hat 6 Ziffern, die Rechnung (5 + 1) erscheint aus dem Nichts | Text „Ziffern von 100 000 (6) statt Nullen (5) gezählt“ |
| C3 | 004 | bleibt „Exponent suchen“, Bestand-Niveau (6 hoch ? = 216) | durch Aufgabe mit Fehlerdiagnose ersetzen oder bewusst lassen (Stufe 2) |
| C4 | 001 | richtige Option die längste und die einzige mit Zusatzinformation (5⁵ = 3 125) | Zusatz in alle Optionen oder streichen |
| C5 | 036 | Ablenker 0 („Eine Klammer darf bei einer Geschichte nicht vorkommen“) und 1 („4 addieren“) sind zu offensichtlich | Ablenker mit echter Fehlvorstellung („Nur ② hat die Klammer, also stimmt nur ②“) |
| C6 | 072, 076 | gleiche Schablone (Gesamt − Fester Teil, geteilt durch Anzahl), auch 040 | 072 durch Gleichungs-Idee (Was wäre wenn) ersetzen |
| C7 | 068, 069, 064 | einzelne Ablenker absurd („Überschläge sind nutzlos“, „genau 1 000“, „Ein Überschlag kann nie zeigen …“) | je einen Ablenker mit echter Schüler-Fehlvorstellung ersetzen |
| C8 | 064 bis 070 | `vtest_pruefen.py` meldet „Regel fehlt (Lernkarte hat id.zahlen.buendeln)“; Autor hat das bewusst offen gelassen (keine Regel zu `ueberschlag`) | prüfen, ob eine Regel `rr.ueberschlag` angelegt werden soll; sonst bewusst so lassen |
| C9 | 032 | Nähe zum Bestand („Multipliziere die Summe aus 10 und 3 mit 6“), aber mit zwei Schritten schwerer; kein Doppel | lassen |

## Nicht geprüft

- Ob die Lernkarten (Lernkarte `id.zahlen.buendeln` usw.) inhaltlich zur Idee passen: nur an Etiketten gesehen.
- Wirkliche Lösezeiten und Erfahrungswerte von Kindern: nicht messbar; Stufe/Zeit [A] aus Aufgabentext geschätzt (Stufe 3 etwa 2 bis 3 Minuten).
- Lehrplan: nur die Zusammenfassung des Lehrplans (Fetch-Tool) gelesen, nicht den vollen Text; die Abgrenzung M5 3 (Gymnasium) gegen M5 1.3 (Realschule) wie in Runde 1.
- Die Nähe zum Bestand ist eine Wort- und Zahlenähnlichkeit (Heuristik) gegen `inhalte/themen` und `rollend-*`; sie sieht keine Optionen-Muster und keine Ideen.
