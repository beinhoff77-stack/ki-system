# Ideen-Sammler 12: Ideensammlung Aufgaben (Mathe Kl. 5 und Kl. 8, Maßstab Gymnasium Bayern)

Stand: 25.11.2026. Alle Links an diesem Tag abgerufen.

**Kennzeichnung**
- [G] = gesichert, mit Link.
- [A] = Annahme oder allgemein bekannt, hier nicht eigens geprüft.
- [M] = Meinung.
- „Beispielwert“ = erfundene Zahl, nicht über die Welt belegt.

**Nachrechnen:** Alle Beispiele sind selbst gebaut. Sie wurden mit einem Skript in `/tmp/ideen12/check.py` nachgerechnet; Eindeutigkeit wurde wo nötig per Durchprobieren geprüft. Aufgabentexte aus Quellen wurden nicht übernommen, nur Aufgabenarten.

**Lücken-Marken (aus tief-5, BMT 8):**
- **[B]** Begründen
- **[G]** Geometrie sehen/konstruieren
- **[D]** Daten lesen
- **[Ü]** Übertragen / Sachaufgaben-Ansatz / Regel + Transfer

**Prüfarten:** Zahl · Auswahl · Lücken · mehrere Zahlen · Menge (Felder antippen) · Reihenfolge · Zuordnung · Punkt(e) · „nenne ein Beispiel“ per Einsetzen (Server prüft eine Bedingung) · Term (Server setzt Zufallswerte ein) · nur Papier.

**Reiz:** 1 = nüchtern, 2 = angenehm, 3 = „noch eins!“ [M].

---

## 0. Einordnung: was es schon gibt (nicht doppeln)

| Schon vorhanden (Ablage) | Wo | Diese Sammlung liefert dazu |
|---|---|---|
| Felder antippen, Schieber, Gitterpunkte, Zuordnen, Bausteine ordnen, Bereich markieren, Wertetabelle mit Graph (F1–F7) | mathe-profi/ideen.md | Inhalte für diese Formen: Z9, GE2, GE4, GE7, FU6, D3 … |
| Mach 100, Aufgabe umdrehen, Gegenbeispiel, Muster fortsetzen, Korrigiere das Heft, Faulster Weg, Zahlen-Steckbrief, Erst schätzen (A1–A8) | ideen.md | Varianten, die nicht doppeln: Ziffernkarten-Ziel (Z1), Steckbrief **für das Geschwister bauen** (B9) |
| Gegenbeispiel, Gitterpunkte, Diagramm lesen und ergänzen, Tabellenkalkulations-Formel, Begründungs-Puzzle, immer/manchmal/nie, Fehler markieren, Zahlenstrahl, Wertetabelle, Karten zuordnen, Winkel einstellen (12 Formen) | tief-10 | Formen bleiben; hier kommen die Aufgaben-**Ideen**, mit denen man sie füllt |
| Balkenmodell, Lösungswege vergleichen, Variations-Reihen, „ohne ausrechnen“, offene Umkehraufgaben, Kontrollzahlen, Fehlerheft | tief-6, tief-7, tief-8 | Hier nicht mehr ausgeführt; Z4 und AL5 nutzen das Variationsprinzip |

**Grundidee dieser Sammlung [M]:** Die App hat genug „Rechne aus“. Es fehlen vier Dinge:
- Aufgaben, bei denen das Kind **wählt, baut oder entscheidet** (Ziffernkarten, Datensatz bauen, Regel erfinden);
- Aufgaben, die **Struktur sichtbar machen** (Päckchen, Rechendreieck, Kalender);
- **Geometrie ohne Formel** (japanische Flächen- und Winkelrätsel);
- **echte Reisezahlen**.

Fast alles davon ist trotzdem automatisch prüfbar, weil der Server **eine Bedingung prüft statt eine Musterlösung zu vergleichen**.

---

## 1. Ideensammlung: 61 Aufgaben-Muster nach Themengebiet

Übersicht: Zahlen 10 · Algebra 10 · Geld und Verhältnisse 9 · Geometrie 8 · Fläche und Raum 9 · Daten und Zufall 8 · Funktionen 7.

### 1.1 Zahlen (Z1–Z10)

**Z1 Ziffernkarten-Ziel** – Quelle: Open Middle (Kaplinsky), https://www.openmiddle.com/ [G: Seite zeigt Aufgaben „closed beginning/end, open middle“]
- Trainiert: Verfahren + Problemlösen (Stellenwert, Rechengesetze, Bruchgröße). Gebiete: Zahlen, Algebra, Brüche.
- Kl. 5: „Lege die Karten 1 bis 6, jede genau einmal, in □□□ − □□□. Mach die Differenz so klein wie möglich, aber größer als 0.“ → 412 − 365 = **47**. Per Programm geprüft: die einzige Belegung mit 47.
- Kl. 8: „Ziffern 1–9, jede höchstens einmal: □/□ + □/□ so nah wie möglich an 1, aber nicht genau 1.“ → 1/9 + 7/8 = **71/72**, Abstand 1/72. Geprüft: bis auf Vertauschen der Summanden die beste Belegung.
- Prüfung: Kind legt Karten (Lücken). Der Server rechnet und bewertet in Stufen: gültig / nah / optimal. Die Bestwerte werden vorab per Durchprobieren berechnet.
- Zufall: ja (Kartensatz und Zielzahl würfeln, Bestwert per Programm). Reiz: 3.

**Z2 Zahlenmauer rückwärts** – Quelle: produktive Übungsformate (Wittmann, „mathe 2000“) [A: Format allgemein bekannt]; Mauern auch bei NRICH („Number Pyramids“, laut mrbartonmaths-Liste) [G: https://mrbartonmaths.com/topics/algebra-skills/writing-algebraic-expressions/richtasks.html]
- Trainiert: Umkehrung, Termstruktur, Übergang zur Variablen. Gebiete: Zahlen, Algebra.
- Kl. 5: Unten 7 · □ · 12, oben 45. Gesucht ist der mittlere Stein: 7 + 2·□ + 12 = 45 → **13**.
- Kl. 8: Vier Steine unten: 2 · x · 5 · 3x, oben 53. Der oberste Stein ist a + 3b + 3c + d = 2 + 3x + 15 + 3x = 6x + 17 = 53 → **x = 6**. Zusatzfrage: „Warum zählt der zweite Stein dreifach?“ (Auswahl) [B]
- Prüfung: Zahl, Lücken. Zufall: ja. Reiz: 2.

**Z3 Rechendreieck (Arithmagon)** – Quelle: Don Steward, Median-Blog („arithmagon“) [G: Titel in der Liste https://mrbartonmaths.com/topics/number-skills/written-arithmetic/richtasks.html]
- Trainiert: Problemlösen, Gleichungssystem ohne Formalismus. Gebiete: Zahlen, Algebra.
- Kl. 5: Auf den Seiten steht die Summe der beiden Ecken: 11, 16, 15. Gesucht: die Ecken → 5, 6, 10. Trick: Alle Seiten zusammen sind 42, also die doppelte Eckensumme; die Eckensumme ist 21; eine Ecke ist 21 minus die gegenüberliegende Seite.
- Kl. 8: **Mal**-Rechendreieck mit negativen Zahlen. Die Seiten sind die Produkte der Ecken: 6, −15, −10. „Finde **beide** Lösungen.“ → (−2, −3, 5) und (2, 3, −5); per Programm im Bereich −20…20 geprüft, es gibt genau diese zwei. [B: „Warum gibt es zwei?“]
- Prüfung: mehrere Zahlen. Der Server prüft die drei Produkte; jede richtige Lösung zählt, und beide geben einen Bonus. Zufall: ja (Ecken würfeln, Seiten berechnen). Reiz: 2–3.

**Z4 Strukturiertes Päckchen** – Quelle: Wittmann/Müller „strukturierte Päckchen“ [A]; Inquiry Maths nutzt Gleichungen als Anlass, z. B. 24 × 21 = 42 × 12 [G: https://www.stem.org.uk/cx5yw]
- Trainiert: Begriff (Muster sehen), Begründen, Rechenvorteil. Gebiete: Zahlen, Algebra.
- Kl. 5: 12·12 = 144, 11·13 = 143, 10·14 = 140, 9·15 = 135. Nächste Zeile? → 8·16 = 128. Dann: „Ohne zu rechnen: 6·18 = ?“ Die Abstände sind 1, 4, 9 … also 144 − 36 = **108**.
- Kl. 8: Dasselbe als Term: (n − k)(n + k) = n² − k² → 47·53 = 2500 − 9 = **2491**. Danach eine Begründung aus Bausteinen [B]. Das ist zugleich die binomische Formel aus Jgst. 7.
- Prüfung: Zahl; Begründung als Auswahl/Reihenfolge. Zufall: ja (Mitte n und Abstand k würfeln). Reiz: 2.

**Z5 Rückwärtszahl** – Quelle: Don Steward („number reverse“) [G: Titel in der mrbartonmaths-Liste oben]
- Trainiert: Begründen, Stellenwert, Teilbarkeit. Gebiete: Zahlen, Algebra.
- Kl. 5: Zweistellige Zahl minus Rückwärtszahl (72 − 27 = 45). „Probiere drei Zahlen. Was fällt auf? Kann 36 herauskommen? Und 40?“ → 36 ja (51 − 15), 40 nie. Bei Ziffern 1–9 und größerer Zehnerziffer sind nur 9, 18, …, 72 möglich (geprüft).
- Kl. 8: Beweis: (10a + b) − (10b + a) = 9(a − b). Dreistellig: abc − cba = 99(a − c), z. B. 852 − 258 = 594 = 99·6. [B]
- Prüfung: Auswahl (möglich/unmöglich) + Zahl; Beweis als Begründungs-Puzzle. Zufall: ja. Reiz: 2.

**Z6 Ziffern-Detektiv (Lückenrechnung)** – Quelle: Kryptarithmen, Mathematik-Olympiade Kl. 5/6 (Kapitel „Zahlen werden gesucht“ im Trainingsmaterial) [G: https://www.sachsen.schule/~bezirkskomitee/01-MO-Vo-Einl-6-1.pdf]
- Trainiert: Verfahren rückwärts (Übertrag), systematisch probieren. Gebiete: Zahlen.
- Kl. 5: 3□7 + □8□ = 912 → 327 + 585 (per Programm geprüft: eindeutig).
- Kl. 8: □7 · □ = □41 → 47 · 3 = 141 (eindeutig). Gegenbeispiel für die Freigabe-Prüfung: 4□ · □ = 3□6 hat vier Lösungen, ist also **nicht** freigabefähig.
- Prüfung: Lücken. Vor der Freigabe muss das Programm die Eindeutigkeit prüfen. Zufall: ja (Rechnung würfeln, Ziffern verstecken, prüfen, ob eindeutig). Reiz: 2–3.

**Z7 Schätzen mit Bereich (zu niedrig / zu hoch / beste Schätzung)** – Quelle: Estimation 180 (Andrew Stadel) [A: Website nicht abgerufen, Format laut Lehrerseiten: täglich ein Schätzbild]
- Trainiert: Schätzen, Größenvorstellung, Zehnerpotenzen. Gebiete: Zahlen, Fläche und Raum.
- Kl. 5: „Wie viele Reiskörner sind in 200 g?“ Das Kind gibt drei Zahlen ein. Danach wiegt die Familie 100 Körner selbst (Beispielwert 2,5 g) → 200 : 2,5 · 100 = **8 000**.
- Kl. 8: „Wie oft schlägt dein Herz in einem Jahr?“ Mit 70 Schlägen/min: 70·60·24·365 = 36 792 000 ≈ **3,7·10⁷**.
- Prüfung: drei Zahlen. Bewertet wird, ob niedrig ≤ Wahrheit ≤ hoch gilt und wie eng der Bereich ist (z. B. hoch : niedrig ≤ 2 gibt einen Stern). Zufall: teilweise (Rechenteil ja, Schätzobjekt nein). Reiz: 3, wenn echte Gegenstände der Reise geschätzt werden.

**Z8 Vergleichen ohne Ausrechnen (<, =, >)** – Quelle: Number-Sense-Routinen, Inquiry-Maths-Ungleichungen wie 43 + 21 > 12 + 34 [G: https://www-legacy.stem.org.uk/resources/collection/4060/number]
- Trainiert: Begriff, Struktur, Begründen. Gebiete: Zahlen, Algebra.
- Kl. 5: 199·201 □ 200·200 → „<“, der Unterschied ist genau 1. 37 + 48 □ 38 + 47 → „=“.
- Kl. 8: 2¹⁰ □ 10³ → „>“ (1024). 3/7 □ 5/12 → „>“ (36/84 gegen 35/84).
- Prüfung: Auswahl + Grund-Auswahl. Mit Zeitanzeige, aber ohne Druck (laut ideen.md ist Zeitdruck nicht gewollt). Zufall: ja. Reiz: 2.

**Z9 Teiler-Schloss** – Quelle: Hundertertafel-Aufgaben (NRICH-Tradition) [A]
- Trainiert: Begriff (Teiler, Primzahl, Quadratzahl), Begründen. Gebiete: Zahlen.
- Kl. 5: „Tippe alle Zahlen bis 50 an, die **genau 3 Teiler** haben.“ → 4, 9, 25, 49. Folgefrage: „Was haben sie gemeinsam?“ → Quadrate von Primzahlen. [B]
- Kl. 8: „Wie viele Teiler hat 2⁴·3²?“ → (4 + 1)(2 + 1) = **15**. Und: „Kleinste Zahl mit genau 6 Teilern?“ → 12.
- Prüfung: Menge (Felder antippen, F1) bzw. Zahl. Zufall: ja. Reiz: 2.

**Z10 Welche passt nicht? (WODB)** – Quelle: wodb.ca (Mary Bourassa, nach Christopher Danielsons Buch). Jede der vier Karten hat mindestens einen Grund, nicht dazuzugehören. [G: https://nlpslearns.sd68.bc.ca/wp-content/uploads/wodb_handout.pdf]
- Trainiert: Begriff, Begründen, Fachsprache. Gebiete: alle (Zahlen, Graphen, Figuren).
- Kl. 5: 9 · 16 · 25 · 43. Gründe: 43 ist keine Quadratzahl; 16 ist gerade; 9 ist einstellig; 25 ist durch 5 teilbar.
- Kl. 8: A y = 3x + 1 · B y = 2x − 3 · C y = −0,5x + 1 · D y = x² + 1. Gründe: D ist keine Gerade; C fällt; B hat einen negativen y-Abschnitt; nur A geht durch (1|4) (geprüft). [B]
- Prüfung: Das Kind wählt Karte + Grund aus einer Liste von etwa 8 Eigenschaften. Der Server prüft, ob die Eigenschaft **nur** auf die gewählte Karte zutrifft. Bonus, wenn das Kind für alle vier Karten einen Grund findet. Zufall: ja (aus einer Eigenschaften-Bibliothek Vierersätze suchen, bei denen jede Karte einen eigenen Grund hat). Reiz: 3.

### 1.2 Algebra (AL1–AL10)

**AL1 Zahlentrick entlarven** – Quelle: Don Steward („maths tricks“) [G: Titel in https://mrbartonmaths.com/topics/algebra-skills/writing-algebraic-expressions/richtasks.html]
- Trainiert: Term aufstellen, vereinfachen, Begründen. Gebiete: Algebra, Zahlen.
- Kl. 5: „Denk dir eine Zahl, addiere 5, verdopple, ziehe 4 ab, halbiere, ziehe deine Zahl ab.“ → Es kommt immer **3** heraus (mit 7: 12, 24, 20, 10, 3). Das Kind probiert drei Zahlen und erklärt den Trick mit einem Bild aus Säckchen und Steinen.
- Kl. 8: „Quadriere zwei aufeinanderfolgende Zahlen und ziehe ab.“ (7, 8: 64 − 49 = 15 = 7 + 8.) Lücke: Ergebnis = □·n + □ → 2, 1. [B]
- Prüfung: Zahl; Term per Einsetzen. Zufall: ja (Trickbausteine kombinieren, das Programm prüft, dass das Ergebnis konstant ist). Reiz: 3 – Kinder führen den Trick gern anderen vor.

**AL2 Ein Bild – viele Terme** – Quelle: Flächenterme, Card Sorts (MAP Classroom Challenges) [G: https://map.mathshell.org/]
- Trainiert: Term aus einer Figur, Gleichwertigkeit, Übertragen. Gebiete: Algebra, Fläche. [Ü][B]
- Kl. 5: L-Form: ein Rechteck 8 × 5 mit einer ausgeschnittenen Ecke 3 × 2. Das Kind wählt **alle** passenden Rechnungen: 8·5 − 3·2 ✓, 5·5 + 3·3 ✓, 8·3 + 5·2 ✓, aber nicht 8·5 − 3·3 (= 31). Alle richtigen ergeben 34.
- Kl. 8: Dasselbe mit x: Rechteck x × (x + 5). Richtig sind x² + 5x und x(x + 5). Ablenker: x² + 3x + 2, der bei x = 1 **zufällig gleich** ist (geprüft). Das ist eine gute Folgefrage: „Reicht ein Testwert?“
- Prüfung: Menge (alle richtigen antippen). Der Server prüft gleichwertige Terme an 5 Zufallswerten. Zufall: ja. Reiz: 2.

**AL3 Bild-Gleichungen (Emoji-Rätsel)** – Quelle: verbreitetes Rätselformat; Singapur-„Model“-Denken (tief-6) [A]
- Trainiert: Gleichungssystem intuitiv, Einsetzen. Gebiete: Algebra.
- Kl. 5: 🍎 + 🍎 + 🍌 = 14 · 🍎 + 🍌 = 9 · 🍌 + 🥥 = 11 → 🍎 = 5, 🍌 = 4, 🥥 = 7. Schlussfrage: 🍎·🥥 − 🍌 = **31**.
- Kl. 8: 3·🐨 + 2·🦘 = 31 · 🐨 − 🦘 = −3 → 🐨 = 5, 🦘 = 8 (LGS, Jgst. 8).
- Prüfung: Zahl(en). Zufall: ja (Werte würfeln, Zeilen erzeugen, das Programm prüft eindeutige Lösbarkeit). Reiz: 3.

**AL4 Was ist meine Regel? (Zahlenautomat)** – Quelle: Don Steward „What’s my rule?“ [G: Titel in der mrbartonmaths-Algebra-Liste oben]; Desmos-ähnliche „Function Carnival“-Logik [A]
- Trainiert: Muster → Term, Funktionsbegriff. Gebiete: Algebra, Funktionen.
- Kl. 5: Das Kind gibt selbst Zahlen in den Automaten: 1 → 5, 2 → 8, 4 → 14. „Was kommt bei 10 heraus?“ → 32. „Welche Eingabe gibt 50?“ → 16. Regel: 3n + 2.
- Kl. 8: 1 → 0, 2 → 3, 3 → 8, −2 → 3. Term eingeben: n² − 1.
- Prüfung: Zahl; Term (der Server setzt 5 Zufallswerte ein). Wenige Abfragen geben einen Bonus. Zufall: ja. Reiz: 3.

**AL5 Gleichwertig – oder nur zufällig gleich?** – Quelle: Termgleichwertigkeit im BMT (tief-5) und Gegenbeispiel-Denken
- Trainiert: Begriff, Begründen. Gebiete: Algebra. [B]
- Kl. 5: „a·a und 2·a ergeben bei a = 2 beide 4. Sind sie immer gleich?“ → nein: a = 3 gibt 9 und 6.
- Kl. 8: 2x + 4 und x² + 4 sind bei x = 0 **und** x = 2 gleich, bei x = 1 nicht (6 gegen 5). „Ein Wert, an dem es nicht stimmt, genügt.“
- Prüfung: Auswahl + Gegenbeispiel-Zahl (Einsetzen: die Werte sind verschieden). Zufall: ja. Reiz: 2.

**AL6 Magisches Quadrat mit Variable** – Quelle: Lo-Shu-Quadrat; Rätseltradition [A]
- Trainiert: Gleichungen, Struktur, Begründen. Gebiete: Algebra, Zahlen.
- Kl. 5: Gegeben sind 8 _ 6 / _ 5 _ / _ _ 2, die Summe ist überall gleich. → 8 1 6 / 3 5 7 / 4 9 2 (eindeutig).
- Kl. 8: Die Mitte heißt c; die Einträge sind c + 3, c − 4, c + 1 / c − 2, c, c + 2 / c − 1, c + 4, c − 3. „Die magische Summe ist 36 – fülle aus.“ → c = 12; erste Zeile 15, 8, 13 (geprüft). [B: „Warum ist die Mitte immer ein Drittel der Summe?“]
- Prüfung: Lücken. Zufall: ja. Reiz: 2.

**AL7 Kalender-Fenster** – Quelle: klassische Kalender-Algebra; Inquiry-Maths-Art [A]
- Trainiert: Term aufstellen, Begründen (Teilbarkeit). Gebiete: Algebra, Zahlen. [B][Ü]
- Kl. 5: Ein 2×2-Fenster im Monatskalender enthält n, n + 1, n + 7, n + 8. „Die Summe ist 64 – welche Tage?“ → 4n + 16 = 64 → 12, 13, 19, 20.
- Kl. 8: 3×3-Fenster: Die Summe ist 9·Mitte. „Kann die Summe 100 sein?“ → nein, 100 ist nicht durch 9 teilbar. „Summe 144?“ → Mitte 16 (wenn der 16. kein Montag oder Sonntag ist).
- Prüfung: Zahl / Auswahl + Begründungs-Baustein. Zufall: ja. Reiz: 2; mit dem echten Reisekalender (Abflugtage, Zeitzonen-Wechsel) 3.

**AL8 Aufgabe ohne Zahlen** – Quelle: Numberless Word Problems (Brian Bushart) [A: nicht abgerufen; Format: erst Situation ohne Zahlen, dann Frage, dann Zahlen]
- Trainiert: Übertragen, Struktur einer Sachaufgabe erkennen. Gebiete: alle Sachaufgaben. [Ü]
- Kl. 5: „Kai kauft einige Postkarten, alle gleich teuer, bezahlt mit einem Schein und bekommt Geld zurück.“ Schritt 1: „Welche Frage passt?“ Schritt 2: „Welche Rechnung?“ → Schein − Anzahl·Preis. Schritt 3: Zahlen kommen: 6 Karten à 1,50 AUD, 20-AUD-Schein → **11 AUD**.
- Kl. 8: Mietwagen mit Tagespreis und km-Zuschlag über einer Freigrenze. Struktur: Tage·Tagespreis + Zuschlag·(km − Freigrenze). Mit Beispielwerten (4 Tage à 65 AUD, 0,25 AUD/km über 400 km, 620 km gefahren) → **315 AUD**.
- Prüfung: Auswahl (Frage, Struktur), dann Zahl. Zufall: ja (Struktur fest, Zahlen würfeln). Reiz: 2.

**AL9 Binomische Formel am Quadrat** – Quelle: Flächenmodell; BMT-Lücke „binomische Formel an einer Figur“ (tief-5)
- Trainiert: Begründen mit Figur, Verfahren. Gebiete: Algebra, Fläche. [B][G]
- Kl. 5: 23² mit einem Quadrat, das in 20 + 3 zerlegt ist: 400 + 60 + 60 + 9 = **529**. Das Kind füllt vier Felder des Bildes.
- Kl. 8: (x + 5)²: Das Bild zeigt den Fehler x² + 25 mit zwei leeren Rechtecken. Das Kind füllt sie mit 5x und 5x → x² + 10x + 25.
- Prüfung: Lücken; Term per Einsetzen. Zufall: ja. Reiz: 2.

**AL10 Fibonacci-artige Folgen** – Quelle: NRICH-Tradition, Folgen mit Rückwärtssuche [A]
- Trainiert: Gleichung aufstellen, Begründen. Gebiete: Algebra, Zahlen. [B]
- Kl. 5: „Jede Zahl ist die Summe der zwei davor. Die erste ist 2, die fünfte 19. Wie heißt die zweite?“ → 2, b, 2 + b, 2 + 2b, 4 + 3b = 19 → **b = 5** (2, 5, 7, 12, 19).
- Kl. 8: „Behauptung: Die Summe der ersten 10 Glieder ist immer 11-mal das 7. Glied.“ Mit 1, 3: Summe 319 = 11·29. Beweis: 55a + 88b = 11(5a + 8b). Per Programm an 200 Zufallsstarts geprüft.
- Prüfung: Zahl + Begründungs-Puzzle. Zufall: ja. Reiz: 3 (überraschende Regel).

### 1.3 Geld und Verhältnisse (G1–G9)

**G1 Bester Kauf** – Quelle: Grundpreis-Vergleich; Lehrplan Größen Jgst. 5, Prozent Jgst. 6 [G: tief-5 §4]
- Trainiert: Übertragen, Dreisatz, Prozent. Gebiete: Geld, Zahlen. [Ü]
- Kl. 5: 4 Becher à 150 g für 2,40 € oder 1 Becher 500 g für 1,90 € (Beispielwerte)? → 0,40 € gegen 0,38 € je 100 g → der große Becher ist günstiger.
- Kl. 8: Einzelpreis 3,60 AUD. „3 für 2“ oder „30 % Rabatt“? → 2,40 AUD gegen 2,52 AUD je Stück → „3 für 2“ ist besser (≈ 33 %).
- Prüfung: Auswahl + Zahl. Zufall: ja. Reiz: 2; mit echten Supermarktfotos der Reise 3.

**G2 Was wäre dir lieber? (Rabatt-Duell)** – Quelle: „Would You Rather Math“ (John Stevens) [A: Website nicht abgerufen; Format: zwei Optionen, mit Mathe begründet wählen]
- Trainiert: Begründen, Prozent, Vergleich. Gebiete: Geld. [B]
- Kl. 5: Rucksack 60 €: „halber Preis“ oder „25 € billiger“? → 30 € gegen 35 €. Folgefrage: „Unter welchem Preis wäre 25 € billiger besser?“ → unter 50 €.
- Kl. 8: Erst 20 %, dann 10 % Rabatt – oder gleich 30 %? → 0,8·0,9 = 0,72, also 28 %. Bei 85 €: 61,20 € gegen 59,50 €. „Ist die Reihenfolge der Rabatte wichtig?“ → nein (Kommutativgesetz).
- Prüfung: Auswahl + Zahl + Grund-Baustein. Zufall: ja. Reiz: 3.

**G3 Hin und zurück (Prozent-Falle)** – Quelle: Fehlvorstellung „+x % und −x % heben sich auf“ (tief-2) [A]
- Trainiert: Begriff, Begründen. Gebiete: Geld, Algebra. [B]
- Kl. 5 (ohne Prozent): „Erst halbieren, dann 10 dazu – oder erst 10 dazu, dann halbieren?“ → Bei jeder Startzahl ist der erste Weg um genau **5** größer (geprüft). Immer / manchmal / nie gleich? → nie.
- Kl. 8: +25 % dann −20 % → genau zurück (1,25·0,8 = 1). +20 % dann −20 % → 96 %. „Um wie viel Prozent musst du nach +60 % senken, um zurückzukommen?“ → **37,5 %**.
- Prüfung: Zahl, Auswahl. Zufall: ja. Reiz: 2.

**G4 Mischung und Rezept** – Quelle: Illustrative Mathematics Gr. 6 „Color Mixtures“ (Verhältnisse) [G: Lektion im Inhalt von https://k12.kendallhunt.com/sites/default/files/k12upload/KH_IM_6-8Math_Sampler.pdf]
- Trainiert: Verhältnis, Übertragen. Gebiete: Geld und Verhältnisse. [Ü]
- Kl. 5: Pfannkuchen für 4: 200 g Mehl, 400 ml Milch → für 6: 300 g, 600 ml. Zusatz: 3 Eier für 4 → 4,5 Eier für 6. „Was machst du?“ → Auswahl „4 oder 5 Eier, beides vernünftig“ (Sachverstand).
- Kl. 8: Sirup A 2 : 5 Wasser, Sirup B 3 : 8. Welcher ist stärker? → 2/7 ≈ 0,286 gegen 3/11 ≈ 0,273 → A. [B: „Warum ist ‚B hat mehr Sirup‘ kein Argument?“]
- Prüfung: Zahl, Auswahl. Zufall: ja. Reiz: 2.

**G5 Prozent oder Prozentpunkte? (Schlagzeilen-Check)** – Quelle: LehrplanPLUS Jgst. 6 „Prozent und Prozentpunkte“ [G: tief-5 §4]
- Trainiert: Begriff, Daten lesen, Begründen. Gebiete: Geld, Daten. [D][B]
- Kl. 5: Klasse A: 10 von 20 Kindern mögen Spinat, Klasse B: 12 von 30. „Wo mögen mehr Kinder Spinat?“ → absolut B, als Anteil A (1/2 gegen 2/5).
- Kl. 8: „Der Anteil steigt von 20 % auf 25 %.“ → +5 Prozentpunkte = +25 %. Das Kind ordnet zwei Schlagzeilen zu (beide richtig formuliert, eine irreführend).
- Prüfung: Zahl, Auswahl. Zufall: ja. Reiz: 2.

**G6 Verdopplung und Zinseszins** – Quelle: Schachbrett-Reiskorn-Legende; 72er-Regel [A]
- Trainiert: Potenzen, Schätzen, Zins. Gebiete: Geld, Funktionen.
- Kl. 5: 1 Cent am 1. Tag, dann täglich doppelt so viel. „An welchem Tag bekommst du zum ersten Mal mehr als 10 €?“ → Tag **11** (1 024 Cent).
- Kl. 8: 7 % Zins im Jahr. „Wann ist das Geld verdoppelt?“ → 1,07¹⁰ ≈ 1,967, 1,07¹¹ ≈ 2,105 → im 11. Jahr. Die 72er-Regel schätzt 72 : 7 ≈ 10,3.
- Prüfung: Zahl. Zufall: ja. Reiz: 2.

**G7 Wer ist schneller, wer sparsamer? (Raten vergleichen)** – Quelle: Rate-Aufgaben (IM Gr. 6 „Rates“) [A]
- Trainiert: Verhältnis, indirekte Darstellung. Gebiete: Geld und Verhältnisse, Funktionen. [Ü]
- Kl. 5: Mia wandert 20 km in 4 h, Kai 12 km in 3 h. → 5 km/h gegen 4 km/h.
- Kl. 8: Auto A braucht 6,5 l/100 km, Auto B fährt 16 km mit 1 l. → B braucht 6,25 l/100 km, ist also sparsamer.
- Prüfung: Zahl + Auswahl. Zufall: ja. Reiz: 2.

**G8 Proportional – oder nicht? (Karten sortieren)** – Quelle: Card Sorts (MAP) [G: https://map.mathshell.org/]; Fehlvorstellung „alles ist proportional“ (tief-2)
- Trainiert: Begriff, Begründen. Gebiete: Verhältnisse, Funktionen. [B]
- Kl. 5: Karten: 3 Hefte 4,50 € → 6 Hefte 9 € (proportional) · Kai 4 Jahre, Schwester 8 → mit 8 ist sie 16? (nein) · Taxi 4 € Grundgebühr + 2 €/km: 3 km 10 €, 6 km 16 € (nicht proportional) · 1 Pizza = 8 Stücke (proportional).
- Kl. 8: Dazu „indirekt proportional“: 4 Pumpen 6 h → 8 Pumpen 3 h. Und „linear, nicht proportional“: y = 2x + 3.
- Prüfung: Zuordnung zu Kategorien. Zufall: teilweise (Kartenbibliothek). Reiz: 2.

**G9 Gerecht teilen** – Quelle: Fair-Share-Aufgaben (RME/Niederlande, tief-7) [A]
- Trainiert: Verhältnis, Begründen, Modellieren. Gebiete: Geld. [B][Ü]
- Kl. 5: Kai zahlt 6 €, Mia 4 € für 20 Postkarten. Gerecht? → 12 und 8.
- Kl. 8: Ein Taxi kostet 60 € für 20 km. A steigt nach 10 km aus, B nach 20 km. Zwei vertretbare Regeln:
  - Abschnittsweise: A 15 €, B 45 €.
  - Nach gefahrenen km: A 20 €, B 40 €.
  Das Kind wählt eine Regel und gibt die Beträge an.
- Prüfung: Die Summe muss 60 sein, A < B, und die Beträge müssen zur gewählten Regel passen (mehrere Zahlen + Auswahl). Zufall: ja. Reiz: 2–3 (echter Streitfall).

### 1.4 Geometrie (GE1–GE8)

**GE1 Winkeljagd ohne Messen** – Quelle: japanische Mittelschul-Aufnahmeaufgaben (Winkel an Parallelen, Dreieckssumme; Wikibooks „中学受験算数/平面図形“) [G: https://ja.wikibooks.org/wiki/%E4%B8%AD%E5%AD%A6%E5%8F%97%E9%A8%93%E7%AE%97%E6%95%B0/%E5%B9%B3%E9%9D%A2%E5%9B%B3%E5%BD%A2]
- Trainiert: Begriff (Neben-, Scheitel-, Wechselwinkel), Begründen. Gebiete: Geometrie. [G][B]
- Kl. 5: An einer Geraden liegen 35°, x und ein rechter Winkel → x = **55°**. Am Vollwinkel liegen 120°, 95° und x → x = **145°**.
- Kl. 8 (Stoff Jgst. 7): Zickzack zwischen zwei Parallelen mit 40° oben und 30° unten → Knickwinkel **70°**. Gleichschenkliges Dreieck mit Basiswinkel 52° → Spitze **76°**.
- Prüfung: Zahl + Begründung aus Bausteinen („Wechselwinkel an Parallelen“, „Winkelsumme 180°“, Ablenker „sieht so aus“). Zufall: ja (Figurenvorlage + Zufallswinkel). Reiz: 2–3.

**GE2 Gleiche Fläche ohne Formel (等積変形, Scherung)** – Quelle: japanischer Unterricht/Aufnahmeprüfung. Ein Lehrmittel der Präfektur Osaka zeigt das Verschieben der Spitze auf einer Parallelen und △ABO = △DCO im Trapez. [G: https://www.osaka-c.ed.jp/sansu/chu2/c2_8.pdf]
- Trainiert: Begriff (Grundseite/Höhe), Begründen. Gebiete: Geometrie, Fläche. [G][B] – trifft die BMT-Lücke „gleiche Flächen begründen“ (unter 20 % gelöst, tief-5).
- Kl. 5: Auf dem Gitter stehen 5 Dreiecke, drei davon mit Grundseite 4 und der Spitze auf derselben Parallelen (Höhe 3). „Tippe alle mit 6 Kästchen Fläche an.“
- Kl. 8: Trapez mit AB = 8, CD = 4, Höhe 3; die Diagonalen schneiden sich in O. → △AOB = 8, △BOC = 4, △AOD = 4, △COD = 2, zusammen 18 = Trapezfläche. Begründung: △ABC und △ABD haben dieselbe Grundseite und Höhe.
- Prüfung: Menge bzw. Zahl + Begründungs-Puzzle. Zufall: ja. Reiz: 2.

**GE3 Gitterflächen (Zerlegen, Ergänzen, Pick)** – Quelle: Geobrett-Tradition; Satz von Pick [A]
- Trainiert: Verfahren, Problemlösen, Entdecken. Gebiete: Geometrie, Fläche.
- Kl. 5: Dreieck (0|0), (4|0), (1|3) → als Hälfte von Rechtecken: **6**. Fünfeck (0|0), (4|0), (4|2), (2|4), (0|2) → Rechteck 4 × 4 minus zwei Ecken zu je 2 → **12**.
- Kl. 8: Pick entdecken: Beim Fünfeck liegen 12 Gitterpunkte auf dem Rand und 7 innen. 7 + 12/2 − 1 = 12 ✓. „Teste die Formel an deiner eigenen Figur.“
- Prüfung: Zahl; eigene Figur per Punkte (F3), der Server rechnet die Fläche. Zufall: ja. Reiz: 2.

**GE4 Koordinaten-Schatzsuche** – Quelle: Koordinatengeometrie im BMT (tief-5), „Battleship“-Spiele [A]
- Trainiert: Koordinaten, Eigenschaften von Vierecken, Spiegeln. Gebiete: Geometrie, Funktionen. [G]
- Kl. 5: A(1|1), B(5|1), C(6|4). „Setze D so, dass ein Parallelogramm entsteht – es gibt drei Möglichkeiten.“ → (2|4), (0|−2), (10|4).
- Kl. 8 (Achsenspiegelung, Jgst. 7): Spiegle P(5|1) an y = x → (1|5). An x + y = 2 → (1|−3); Kontrolle: Der Mittelpunkt (3|−1) liegt auf der Geraden.
- Prüfung: Punkt(e). Bei mehreren Lösungen zählt jede, alle geben einen Bonus. Zufall: ja. Reiz: 3 als Schatzkarte der Reise-Stadt.

**GE5 Würfelnetze und Augensumme** – Quelle: Raumvorstellung (Lehrplan Jgst. 5 Quader/Netz; Jgst. 8 Zylinder/Netz) [G: tief-5 §4]
- Trainiert: Raumvorstellung (Papier-Stoff), Übertragen. Gebiete: Geometrie, Raum. [G]
- Kl. 5: Von sechs Netzen falten nur einige zum Würfel – antippen. Dann: Gegenüberliegende Augen ergeben 7; das Kind trägt im Netz die fehlenden Augenzahlen ein.
- Kl. 8: Zylindernetz r = 3 cm: Die Rechteckseite ist der Umfang 2π·3 ≈ **18,85 cm**. „Welches Netz gehört zu welchem Körper?“
- Prüfung: Menge, Lücken, Zahl. Pflicht ist ein Papiernetz zum Ausschneiden (P-Stoff laut tief-5). Zufall: teilweise. Reiz: 2.

**GE6 Ornamente lesen (Symmetrie und Vielecke)** – Quelle: japanische Familienwappen (Kamon), islamische Sternmuster [A]
- Trainiert: Begriff (Achsen-, Drehsymmetrie), Innenwinkel. Gebiete: Geometrie. [G]
- Kl. 5: Regelmäßiges Sechseck im Wappen: **6** Symmetrieachsen, kleinster Drehwinkel **60°**.
- Kl. 8 (Jgst. 7 Winkelsumme): Innenwinkel im regelmäßigen 8-Eck (6·180) : 8 = **135°**, im 12-Eck 150°. „Mit welchen regelmäßigen Vielecken allein kann man pflastern?“ → 3, 4, 6 (geprüft: nur dort geht 360° glatt auf). [B]
- Prüfung: Zahl, Menge. Zufall: ja (n würfeln). Reiz: 3 mit Fotos aus Tempeln und Museen.

**GE7 Wo darf der Punkt liegen? (Bedingung statt Konstruktion)** – Quelle: BMT-Lücke „Punkt mit Abstandsbedingung“, Mittelsenkrechte (tief-5)
- Trainiert: Begriff (gleich weit entfernt, Abstand), Übertragen. Gebiete: Geometrie. [G][Ü]
- Kl. 5: „Setze einen Punkt, der von A(1|1) und B(7|1) gleich weit entfernt ist und auf der Linie y = 4 liegt.“ → (4|4).
- Kl. 8: „P liegt auf y = x + 1 und ist von A(0|0) und B(4|0) gleich weit entfernt.“ → P(2|3). Danach als Papierauftrag: Mittelsenkrechte mit dem Zirkel.
- Prüfung: Punkt; der Server prüft die Bedingung (gleiche Abstände, auf der Linie). Zufall: ja. Reiz: 2.

**GE8 Sangaku light (Kreise im Quadrat)** – Quelle: Sangaku, Edo-zeitliche Geometrietafeln an Tempeln. Sammlung: Fukagawa/Rothman „Sacred Mathematics“, Princeton 2008. [G: https://en.wikipedia.org/wiki/Sacred_Mathematics] Linkliste Durham [G: https://maths.dur.ac.uk/users/anna.felikson/Projects/sangaku/sangaku-res.html]
- Trainiert: Kreis (Jgst. 8), Staunen, Begründen. Gebiete: Geometrie, Fläche. [G][B]
- Kl. 5: Ein Quadrat mit 8 cm Seite enthält 4 gleiche Kreise, die sich berühren (2 × 2). → Durchmesser 4 cm, Radius 2 cm.
- Kl. 8: Ein Kreis in einem Quadrat mit Seite 10 → Restfläche 100 − 25π ≈ **21,46 cm²**. Vier Kreise in 2 × 2-Anordnung → Rest **ebenso** 100 − 25π (geprüft). „Warum? Und bei 9 Kreisen?“ [B]
- Prüfung: Zahl mit Toleranz, Auswahl. Zufall: ja. Reiz: 3 (Überraschung, Tempelgeschichte aus Japan).

### 1.5 Fläche und Raum (FR1–FR9)

**FR1 Gleiche Fläche, anderer Umfang** – Quelle: NRICH-Klassiker [A]; Fehlvorstellung „mehr Fläche heißt mehr Umfang“ (tief-2) [A]
- Trainiert: Begriff, Problemlösen, Extremwert ohne Analysis. Gebiete: Fläche, Funktionen. [B]
- Kl. 5: Rechtecke aus 24 Kästchen: 1 × 24 (Umfang 50), 2 × 12 (28), 3 × 8 (22), 4 × 6 (20). → Größter Umfang 50, kleinster 20.
- Kl. 8: 20 m Zaun, Rechteck an einer Hauswand (drei Seiten): A = x(20 − 2x). Tabelle x = 1 … 9 → größte Fläche bei x = 5: **50 m²**.
- Prüfung: Zahl, Wertetabelle. Zufall: ja. Reiz: 2.

**FR2 Der bemalte Würfel** – Quelle: Klassiker („painted cube“, NRICH-Tradition) [A]
- Trainiert: Raumvorstellung, Muster → Term. Gebiete: Raum, Algebra.
- Kl. 5: Ein 3 × 3 × 3-Würfel wird außen angemalt und zerlegt. Wie viele kleine Würfel haben 3, 2, 1 oder 0 bemalte Flächen? → 8, 12, 6, 1 (zusammen 27).
- Kl. 8: Für n = 5 → 8, 36, 54, 27. Allgemein: 8, 12(n − 2), 6(n − 2)², (n − 2)³ (Summe n³ geprüft).
- Prüfung: mehrere Zahlen; Terme per Einsetzen. Zufall: ja (n). Reiz: 3.

**FR3 Packen und Verpacken** – Quelle: Optimierungsaufgaben, Mathematik-Olympiade-Stil [A]
- Trainiert: Volumen, Problemlösen, Modellieren. Gebiete: Raum, Geld. [Ü]
- Kl. 5: Wie viele Würfel mit 5 cm Kante passen in einen Karton 30 × 20 × 10 cm? → 6·4·2 = **48**. Schwerer: Kartons 30 × 20 × 10 in eine Kiste 100 × 60 × 40. → Je nach Drehung 30, 36 oder **40** (geprüft): Die Drehung entscheidet!
- Kl. 8: Dose A r = 4, h = 20 / Dose B r = 6, h = 9. Volumen ≈ 1 005 bzw. 1 018 cm³; Oberfläche ≈ 603 bzw. 565 cm². → B fasst mehr und braucht weniger Blech.
- Prüfung: Zahl, Auswahl. Zufall: ja. Reiz: 2.

**FR4 Maßstab bei Fläche und Volumen** – Quelle: BMT-Lücke „Maßstab beim Volumen“ (unter 20 %, tief-5)
- Trainiert: Übertragen, Begriff. Gebiete: Raum, Verhältnisse. [Ü][G]
- Kl. 5: Ein Quadrat mit 3 cm Seite bekommt doppelt so lange Seiten → Fläche 9 → 36 cm², also ×4. „Wie viele 1-cm-Würfel braucht ein Würfel mit 2 cm Kante?“ → 8.
- Kl. 8: Hausmodell 1 : 50. Eine Wand ist im Modell 0,2 m² → in echt 0,2·2 500 = **500 m²**. Volumen ×125 000.
- Prüfung: Zahl + Auswahl („×50 / ×2 500 / ×125 000“). Zufall: ja. Reiz: 2.

**FR5 Füllgraphen** – Quelle: Shell Centre „The Language of Functions and Graphs“ (Malcolm Swan), heute als Download [G: Hinweis auf https://mathshell.org/materials.htm]
- Trainiert: Funktionsbegriff, Raum, Darstellungswechsel. Gebiete: Raum, Funktionen. [D][Ü]
- Kl. 5: Quaderbecken mit Grundfläche 50 × 40 cm, Zulauf 4 l/min → die Höhe steigt um 2 cm/min. Nach 15 min: **30 cm**.
- Kl. 8: Vier Gefäße (Zylinder, Kegel mit Spitze unten, bauchige Flasche, Trichter) ↔ vier Höhe-Zeit-Graphen.
- Prüfung: Zahl; Zuordnung. Zufall: Kl. 5 ja, Kl. 8 Bibliothek. Reiz: 2.

**FR6 Fermi-Volumen** – Quelle: Fermi-Aufgaben [A]
- Trainiert: Schätzen, Einheiten, Modellieren. Gebiete: Raum, Zahlen. [Ü]
- Kl. 5: Garten-Pool 8 m × 4 m × 1,5 m = 48 m³ = 48 000 l. Badewanne 150 l (Beispielwert) → **320** Wannen.
- Kl. 8: 12 mm Regen auf 120 m² Dach → 1,44 m³ = **1 440 l**. „Reicht das für …?“
- Prüfung: Zahl im Bereich (Annahmen gibt das Kind selbst an, der Server rechnet mit ihnen nach). Zufall: ja. Reiz: 2–3.

**FR7 Würfelbauten und Oberfläche** – Quelle: Raumvorstellung, Würfelgebäude (Schweizer Mathbuch-Tradition) [A]
- Trainiert: Raumvorstellung, Begründen. Gebiete: Raum. [G]
- Kl. 5: 4 Würfel: Reihe = 18 Flächen, 2 × 2-Quadrat = **16**, L-Form = 18 (geprüft). „Welche Form hat die kleinste Oberfläche?“
- Kl. 8: 8 Würfel: 2 × 2 × 2 = 24, Stange 1 × 8 = 34. „Ordne die Bauten nach Oberfläche“ und „Warum ist der Würfel am sparsamsten?“ [B]
- Prüfung: Zahl, Reihenfolge. Zufall: ja (Bauten per Programm, Oberfläche zählt das Programm). Reiz: 2.

**FR8 Flächenlabyrinth (Area Maze, 面積迷路)** – Quelle: Rätselautor Naoki Inaba (Japan) [A: als „area maze“ bekannt, keine Quelle abgerufen]
- Trainiert: Fläche = Länge × Breite rückwärts, Verhältnisse, ohne Formelrechnen. Gebiete: Fläche, Verhältnisse. [G]
- Kl. 5: Zwei Rechtecke nebeneinander, gleich hoch: links 24 cm² und 6 cm breit, rechts 20 cm². „Wie breit ist alles?“ → Höhe 4, rechts 5 breit, zusammen **11**. 2 × 2-Feld mit 12 | 18 / 10 | ? → **15**.
- Kl. 8: 6 | 9 / 8 | ? → **12**. Mit Variable: Rechteck x × (x + 3) = 40 → x = 5.
- Prüfung: Zahl. Zufall: ja (Gitter mit ganzzahligen Seiten würfeln, Flächen zeigen, die Lösung auf Eindeutigkeit prüfen). Reiz: 3.

**FR9 Bauplan und Ansichten** – Quelle: Würfelbaupläne (Schweizer/deutsche Schulbuchtradition) [A]
- Trainiert: Raumvorstellung. Gebiete: Raum. [G]
- Kl. 5: Bauplan 2 × 3 mit Höhen 3 1 2 / 2 2 1 → **11** Würfel. „Wie sieht die Ansicht von vorn aus?“ → Säulenhöhen = Maximum je Spalte.
- Kl. 8: „Vorder- und Seitenansicht sind gegeben. Wie viele Würfel braucht man mindestens und höchstens?“ Beispiel auf einem 2 × 2-Feld: Vorderansicht 2 | 3, Seitenansicht 3 | 1 → mindestens **6**, höchstens **7** (per Durchprobieren geprüft).
- Prüfung: Zahl(en). Zufall: ja (Bauplan würfeln, Ansichten und Grenzen berechnen). Reiz: 2.

### 1.6 Daten und Zufall (D1–D8)

**D1 Datensatz bauen („Gib ein Beispiel …“)** – Quelle: Watson & Mason, „learner-generated examples“ [A: nicht abgerufen]. Inquiry-Maths-Anstoß: „Es gibt keinen Datensatz mit Median > Modus > Mittelwert > Spannweite“ [G: in der Liste https://mrbartonmaths.com/topics/averages-and-range/averages-and-range-from-a-list-of-data/richtasks.html]
- Trainiert: Begriff (Kennwerte), offene Umkehraufgabe. Gebiete: Daten. [D][B][Ü] – die schwerste BMT-Gruppe („gib Werte an, sodass …“).
- Kl. 5 (Vorgriff auf den Durchschnitt aus Jgst. 6): „Gib 4 verschiedene Zahlen an, deren Durchschnitt 10 ist.“ Prüfregel: Summe 40, alle verschieden.
- Kl. 8: „5 Zahlen mit Mittelwert 6, Median 5 und Spannweite 8.“ → z. B. 2, 4, 5, 9, 10 (geprüft).
- Prüfung: „nenne ein Beispiel“; der Server berechnet die Kennwerte. Billige Antworten (alle gleich) werden per Zusatzregel abgewiesen. Zufall: ja (Zielwerte würfeln, Lösbarkeit vorab prüfen). Reiz: 2–3.

**D2 Diagramm-Lügendetektor** – Quelle: LehrplanPLUS Jgst. 6 „Manipulation erkennen“ [G: tief-5 §4]
- Trainiert: Daten lesen, Begründen. Gebiete: Daten. [D][B]
- Kl. 5: Zwei Säulen 92 und 96, die Achse beginnt bei 90. Im Bild ist B dreimal so hoch. „Wie viel mehr ist es wirklich?“ → 4, etwa 4 %.
- Kl. 8: Im Piktogramm ist der Durchmesser verdoppelt, also die Fläche ×4, obwohl sich der Wert nur verdoppelt. „Um welchen Faktor täuscht das Bild?“ → 2.
- Prüfung: Zahl + Grund-Auswahl. Zufall: ja (Achsenstart würfeln). Reiz: 2–3.

**D3 Welche Daten gehören zu welchem Bild?** – Quelle: Card Sort (MAP), Desmos Card Sort (tief-10) [G: https://map.mathshell.org/]
- Trainiert: Darstellungswechsel. Gebiete: Daten. [D]
- Kl. 5: Vier Strichlisten ↔ vier Säulendiagramme. Zwei unterscheiden sich nur in einer Säule, damit genau gelesen werden muss.
- Kl. 8 (Jgst. 7 Boxplot): Drei Datensätze ↔ drei Boxplots ↔ drei Aussagen („Die Hälfte liegt zwischen …“).
- Prüfung: Zuordnung. Zufall: ja (Daten würfeln, Diagramm zeichnen, Ablenker durch Ändern eines Werts). Reiz: 2.

**D4 Ist das Spiel fair?** – Quelle: Spielanalysen (Laplace, Jgst. 8) [G: tief-5 §4]
- Trainiert: Zählprinzip, Wahrscheinlichkeit, Begründen. Gebiete: Zufall. [B]
- Kl. 5 (Zählprinzip Jgst. 5): Zwei Würfel, gewertet wird die Summe. Mia gewinnt bei 6, 7 oder 8, Kai sonst. „Zähle die Fälle.“ → 16 gegen 20 von 36 → Kai ist im Vorteil.
- Kl. 8: P(Mia) = 16/36 = 4/9. „Ändere Mias Summen so, dass das Spiel fair ist.“ → z. B. {2, 6, 7, 8, 12} = 18 Fälle (geprüft).
- Prüfung: Zahl/Bruch. Offene Änderung: Der Server zählt, ob es 18 von 36 Fällen sind. Zufall: ja. Reiz: 3 (die Kinder spielen es danach echt).

**D5 Selbst würfeln, dann vergleichen** – Quelle: Gesetz der großen Zahlen (Lehrplan Jgst. 8) [G: tief-5 §4]
- Trainiert: Daten erheben, Schwankung verstehen. Gebiete: Zufall, Daten. [D]
- Kl. 5: 20 Münzwürfe mit Strichliste eintragen. „Wie viele Kopf hättest du erwartet?“ → 10. „Ist 13 verdächtig?“ → nein.
- Kl. 8: 60 echte Würfelwürfe. Erwartet sind je 10. „Die 6 kam nur 6-mal – ist der Würfel gezinkt?“ → nein, das reicht nicht als Beleg. Danach legt die App die eigenen Würfe beider Kinder zusammen (120 Würfe): Die relative Häufigkeit nähert sich 1/6.
- Prüfung: Eingabe (die Summe muss stimmen) + Auswahl. Zufall: nein (echte Daten), dafür jedes Mal neue. Reiz: 3.

**D6 Was macht der neue Wert?** – Quelle: Don Steward Kennwert-Aufgaben („spread“, „central tendency“) [G: Titel in der mrbartonmaths-Liste oben]
- Trainiert: Begriff (Mittelwert vs. Median, Ausreißer). Gebiete: Daten. [D][B]
- Kl. 5: Bei 4 Würfen ist der Durchschnitt 5. Der fünfte Wurf ist 10 → neuer Durchschnitt **6**.
- Kl. 8: 3, 5, 5, 6, 8 (Mittelwert 5,4, Median 5). Dazu kommt 40 → Mittelwert ≈ 11,17, Median 5,5. „Welcher Kennwert beschreibt die Gruppe besser?“
- Prüfung: Zahl + Auswahl („steigt / fällt / bleibt“). Zufall: ja. Reiz: 2.

**D7 Zählen mit System** – Quelle: Zählprinzip/Baumdiagramm (Jgst. 5 LB 3) [G: tief-5 §4]; Kombinatorik in der MO Kl. 5/6 [G: Bezirkskomitee-PDF oben]
- Trainiert: Problemlösen, Systematik. Gebiete: Zufall, Zahlen.
- Kl. 5: Eis mit 2 verschiedenen Kugeln aus 5 Sorten, Reihenfolge egal → **10**. Wege im Gitter (3 nach rechts, 2 nach oben) → **10**. „Warum ist es zweimal 10?“ [B]
- Kl. 8: 4-stelliger Zahlencode: P(alle Ziffern verschieden) = 5 040/10 000 = **0,504**.
- Prüfung: Zahl. Zufall: ja. Reiz: 2.

**D8 Wer schätzt am besten?** – Quelle: Don Steward „Best Guesser“ [G: Titel in der mrbartonmaths-Liste oben]
- Trainiert: Abweichung, Median gegen Mittelwert. Gebiete: Daten, Zahlen. [D]
- Kl. 5: Im Glas sind 137 Bonbons (Beispielwert). Schätzungen: 120, 150, 140, 100 → 140 liegt am nächsten (Abstand 3).
- Kl. 8: Schätzungen 80, 95, 100, 105, 400; wahr sind 110. Mittelwert 156, Median 100 → der Median ist der bessere „Gruppenschätzer“.
- Prüfung: Zahl, Auswahl. Zufall: ja. Reiz: 2; als Familienspiel mit echten Schätzungen 3.

### 1.7 Funktionen (FU1–FU7)

**FU1 Geschichte ↔ Graph** – Quelle: Shell Centre „Language of Functions and Graphs“ [G: https://mathshell.org/materials.htm]; Don Steward „graphical interpretation“ [G: https://donsteward.blogspot.com/2015]
- Trainiert: Darstellungswechsel, Steigung als Geschwindigkeit. Gebiete: Funktionen, Daten. [D][Ü]
- Kl. 5: Wanderung als Tabelle: 0 h 0 km · 1 h 4 km · 2 h 4 km · 3 h 9 km. „Wann war Pause? Welche Stunde war am schnellsten?“ → die 2.; die 3. mit 5 km.
- Kl. 8: Vier Weg-Zeit-Graphen ↔ vier Geschichten (Pause, Umkehren, Bus, Rennen). Steigung im letzten Abschnitt = **5 km/h**.
- Prüfung: Zuordnung, Zahl. Zufall: ja. Reiz: 2; mit den echten Wanderungen der Familie 3.

**FU2 Ab wann lohnt sich das? (Tarife)** – Quelle: lineare Funktionen, Schnittpunkt (Jgst. 8) [G: tief-5 §4]
- Trainiert: Modellieren, Schnittpunkt, Ungleichung. Gebiete: Funktionen, Geld. [Ü]
- Kl. 5: Fahrradmiete A: 5 € + 2 € je Stunde; B: 3 € je Stunde. Tabelle 1–7 h → bei 5 h gleich (15 €), ab 6 h ist A günstiger.
- Kl. 8: y = 0,25x + 49 und y = 0,40x + 25 (Mietwagen, Beispielwerte) → gleich bei **x = 160 km**.
- Prüfung: Zahl; Bereich (F6). Zufall: ja. Reiz: 2.

**FU3 Parameter-Detektiv** – Quelle: Desmos-Aktivitäten (Parameter verändern, Vorhersage vor dem Zeigen) [A]
- Trainiert: Begriff (m, t), Vorhersagen. Gebiete: Funktionen.
- Kl. 5: Kosten = 2·Anzahl + 3. „Was passiert, wenn aus der 3 eine 5 wird?“ → Alle Kosten steigen um 2.
- Kl. 8: y = 3x + t soll durch (2|7) gehen → t = **1**. „Die Gerade wird um 2 nach oben verschoben – welche Zahl ändert sich?“
- Prüfung: Auswahl, Zahl; erst vorhersagen, dann zeigt der Schieber (F2) das Bild. Zufall: ja. Reiz: 2.

**FU4 Je mehr, desto weniger** – Quelle: indirekte Proportionalität/Hyperbel (Jgst. 8) [G: tief-5 §4]
- Trainiert: Begriff, Asymptote im Sachzusammenhang. Gebiete: Funktionen, Verhältnisse.
- Kl. 5: 24 Bonbons auf 1, 2, 3, 4, 6, 8 Kinder → 24, 12, 8, 6, 4, 3. „Geht es mit 5 Kindern ohne Rest?“ → nein. [B]
- Kl. 8: Fahrzeit für 300 km: t = 300/v → 60 km/h: 5 h, 75: 4 h, 100: 3 h. „Was passiert, wenn v sich verdoppelt? Kann t jemals 0 werden?“
- Prüfung: Lücken, Auswahl. Zufall: ja. Reiz: 2.

**FU5 Linear gegen Verdoppeln** – Quelle: „Would You Rather“-Format [A]
- Trainiert: Wachstumsarten vergleichen, Tabelle. Gebiete: Funktionen, Geld.
- Kl. 5: A: jeden Tag 10 €. B: am ersten Tag 1 €, dann jeden Tag doppelt so viel. Nach 5 Tagen: 50 gegen 31 (A vorn). Nach 6 Tagen: 60 gegen 63 (B vorn). Nach 7: 70 gegen 127.
- Kl. 8: y = 50 + 20x gegen y = 10·2ˣ → bei x = 3: 110 gegen 80, bei x = 4: 130 gegen 160 → der Wechsel liegt zwischen 3 und 4.
- Prüfung: Zahl. Zufall: ja. Reiz: 3.

**FU6 Triff die Sterne** – Quelle: Desmos „Marbleslides“-Idee (Graph durch Ziele legen) [A]
- Trainiert: Koordinaten, Gleichung aus zwei Punkten. Gebiete: Funktionen, Geometrie. [G]
- Kl. 5: „Setze 4 Punkte, für die x + y = 6 gilt.“ Dann: „Was fällt dir auf?“ → Sie liegen auf einer Linie.
- Kl. 8: „Gib eine Gerade an, die durch (1|2) und (4|8) geht.“ → y = 2x. Für (−1|4) und (3|−4) → y = −2x + 2.
- Prüfung: Punkte per Bedingung; der Term wird an den Sternen geprüft. Zufall: ja. Reiz: 3 (Spiel mit Levels).

**FU7 Die Zeile, die nicht passt** – Quelle: Fehler-Finden (tief-10, Form 8), angewendet auf Tabellen
- Trainiert: Regel erkennen, Kontrolle. Gebiete: Funktionen, Verhältnisse.
- Kl. 5: Anzahl/Preis: 1 → 2,50 · 2 → 5,00 · 3 → 7,50 · 4 → 11,00 · 5 → 12,50 → Zeile 4 ist falsch, richtig 10,00.
- Kl. 8: y = −2x + 5: x = −1 → 7, 0 → 5, 1 → 3, 2 → −1 (falsch, richtig 1), 3 → −1.
- Prüfung: Zeile antippen + Zahl. Zufall: ja (einen Wert verfälschen). Reiz: 1–2.

### 1.8 Übersicht: Abdeckung und BMT-Lücken

| Gebiet | Ideen | davon [B] | [G] | [D] | [Ü] |
|---|---|---|---|---|---|
| Zahlen | 10 | 6 | – | – | – |
| Algebra | 10 | 7 | 1 | – | 3 |
| Geld/Verhältnisse | 9 | 6 | – | 1 | 4 |
| Geometrie | 8 | 4 | 7 | – | 1 |
| Fläche/Raum | 9 | 2 | 4 | 1 | 4 |
| Daten/Zufall | 8 | 5 | – | 6 | 1 |
| Funktionen | 7 | 1 | 1 | 1 | 2 |
| **Summe** | **61** | **31** | **13** | **9** | **15** |

**Nur Papier oder teilweise Papier:**
- GE5 (Netz ausschneiden), GE7 (Mittelsenkrechte mit Zirkel), FR9 (echte Würfel).
- Begründungen jeweils als Papier-Folge (siehe tief-5 §7c).

---

## 2. Reise-Aufgaben: 30 Ideen mit Bezug zu Ländern und Städten

**Regeln:**
- Weltzahlen nur mit [G]-Beleg, sonst als „Beispielwert“ gekennzeichnet.
- Kurse, Preise und Fahrzeiten setzt die Familie vor Ort ein. Die App zeigt den Wert **in der Aufgabe** an, wie in ideen.md M1.
- „Exp.“ = Vorschlag, wie daraus eine Expedition aus 3–5 Teilen wird.

**Belegte Fakten:**

| Fakt | Beleg |
|---|---|
| Konsumsteuer Japan 10 %, ermäßigt 8 % für Lebensmittel zum Mitnehmen; im Lokal 10 % | [G] https://www.mof.go.jp/english/tax_policy/consumption_tax/index.html |
| GST Australien 10 %; Rückerstattung (TRS) ab 300 AUD bei einem Händler (eine ABN), Kauf höchstens 60 Tage vor Abreise | [G] https://www.abf.gov.au/entering-and-leaving-australia/tourist-refund-scheme/selling |
| Australien: Barzahlungen werden seit 1992 auf 5 Cent gerundet | [G] https://ramint.gov.au/australian-coin-history |
| Rundungsregel: Endziffer 1, 2, 6, 7 ab, 3, 4, 8, 9 auf | [G] https://www.pcgseurope.com/article/the-end-of-the-cent-part-2-oceania |
| Zeitzonen Australien: Sommerzeit vom 1. Sonntag im Oktober bis 1. Sonntag im April in NSW, ACT, Vic, Tas (UTC+11) und SA (UTC+10:30); Qld (UTC+10), NT (UTC+9:30), WA (UTC+8) ohne Sommerzeit | [G] https://www.timeanddate.com/time/change/australia, https://www.australia.com/en-sg/facts-and-planning/about-australia/time-zones.html |
| Tokaido-Shinkansen: 515,4 km | [G] https://en.wikipedia.com/wiki/Shinkansen |
| Tokaido-Shinkansen: Höchstgeschwindigkeit 285 km/h, schnellster Zug Tokio–Shin-Osaka 2 h 21 min | [G] https://global.jr-central.co.jp/en/company/about_shinkansen |
| Uluru: 348 m über der Ebene, Umfang 9,4 km | [G] https://parksaustralia.gov.au/uluru/discover/highlights/amazing-facts |
| Kata Tjuta: höchste Kuppel 546 m | [G] https://parksaustralia.gov.au/uluru/discover/highlights/amazing-facts |
| Uluru-Rundweg: 10,6 km, etwa 3 h 30 min; bei Hitze vor 11 Uhr fertig sein | [G] https://uluru.gov.au/things-do/activities/walks/uluru-walks/uluru-base-walk/ |
| Sydney Harbour Bridge: Bogen 503 m, Höhe 134 m, Gesamtlänge 1 149 m | [G] https://www.sydney.com/destinations/sydney/sydney-city/sydney-harbour/sydney-harbour-bridge, https://www.bridgeclimb.com/explore/the-bridge |
| Tokyo Skytree 634 m (6-3-4 als „Mu-sa-shi“ gelesen), Tokyo Tower 333 m | [G] https://wikipedia.com/wiki/Sky_Tree, https://structurae.net/de/bauwerke/20049226 |
| Reiwa-Ära seit 1.5.2019, 2026 = Reiwa 8; Heisei 1989–2019 | [G] https://cotoacademy.com/guide-japanese-yearly-calendar-converting-western-japanese-year/ |
| Japan UTC+9 ohne Sommerzeit | [A] nicht eigens geprüft |
| Yen-Münzen 1, 5, 10, 50, 100, 500 | [A] nicht eigens geprüft |
| 1 Meile = 1,609344 km; 1 Knoten = 1,852 km/h; 1 US-Gallone = 3,785 l | [A] Definitionen, nicht eigens geprüft |
| Erdumfang ≈ 40 000 km | [A] |

### Japan

**R1 Yen passend zahlen** – Kl. 5, Stellenwert/Zerlegen; Kl. 8, Prozent.
- Kl. 5: 768 Yen mit möglichst wenigen Münzen → 500 + 100 + 100 + 50 + 10 + 5 + 1 + 1 + 1 = **9 Münzen**.
- Kl. 8: Ein Bento kostet netto 500 Yen. Zum Mitnehmen (8 %): 540 Yen, im Laden gegessen (10 %): 550 Yen. Rückwärts: 540 Yen inklusive 8 % → netto 500.
- Exp.: Konbini-Einkauf, Steuer, Wechselgeld, Umrechnung in Euro mit dem Tageskurs.

**R2 Soroban (japanischer Abakus)** – Kl. 5, Stellenwert.
- Pro Stab gibt es eine Fünferperle und vier Einerperlen. Für 768 werden 3 + 2 + 4 = **9** Perlen bewegt (7 = 5 + 2, 6 = 5 + 1, 8 = 5 + 3).
- „Welche dreistellige Zahl braucht die meisten Perlen?“ → 999 (je 5, zusammen 15).
- Kl. 8: Addition auf dem Soroban als Algorithmus mit Ergänzung zu 5 und zu 10. Reiz 3, wenn ein echter Soroban gekauft wird.

**R3 Shinkansen** – Kl. 5, Zeit/Größen; Kl. 8, Geschwindigkeit, Graph.
- Kl. 5: 2 h 21 min = **141 min**.
- Kl. 8: 515,4 km in 141 min → Durchschnitt ≈ **219 km/h**, obwohl die Spitze 285 km/h ist. „Warum ist der Schnitt kleiner?“ [B] Halte, Anfahren.
- Exp.: Fahrplan lesen, Zeit, Durchschnitt, Weg-Zeit-Graph mit Halt in Nagoya (Halte-Zeiten als Beispielwerte).

**R4 Skytree und Tokyo Tower** – Kl. 5, Differenz/Maßstab; Kl. 8, Prozent.
- Kl. 5: 634 − 333 = **301 m**. „Wie viele Tokyo Tower übereinander sind ungefähr ein Skytree?“ → knapp 2.
- Kl. 8: Der Skytree ist um (634 − 333)/333 ≈ **90,4 %** höher.
- Knobel: Zahlen als Wörter (Goroawase, 634 = Mu-sa-shi). „Erfinde eine Zahl, die sich als Wort lesen lässt.“

**R5 Reiwa-Jahre** – Kl. 5, Rechnen mit Jahreszahlen; Kl. 8, lineare Zuordnung und Umkehrung.
- Kl. 5: 2026 = Reiwa 8. „Welches Reiwa-Jahr ist 2030?“ → 12.
- Kl. 8: Jahr = Reiwa + 2018 und Jahr = Heisei + 1988. „In welchem Heisei-Jahr ist jemand geboren, der 2012 geboren ist?“ → **Heisei 24**.
- Exp.: Tempelinschriften, Münzjahre (stehen in Ära-Jahren), Geburtsjahre der Familie umrechnen.

**R6 Sangaku am Tempel** – Kl. 8, Kreis; Kl. 5, Radius/Durchmesser.
- Siehe GE8. Exp.: Ein Tafelbild (Foto, falls die Familie einen Tempel mit Sangaku findet) wird vereinfacht nachgebaut, dann gelöst und mit dem Ergebnis der Edo-Zeit verglichen.

**R7 Kaiten-Sushi-Rechnung** – Kl. 5, Mehrschritt; Kl. 8, LGS.
- Beispielwerte: Teller zu 150 und zu 300 Yen.
- Kl. 5: 4 Teller zu 150 und 5 zu 300 → 600 + 1 500 = **2 100 Yen**.
- Kl. 8: „9 Teller, 2 100 Yen – wie viele von jeder Farbe?“ → x + y = 9, 150x + 300y = 2 100 → 4 und 5.
- Exp.: Rechnung schätzen, genau rechnen, Steuer, Teilen unter 4 Personen. Reiz 3.

**R8 Kamon-Wappen und Symmetrie** – Kl. 5/8, Symmetrie, Drehwinkel, Innenwinkel.
- Siehe GE6, mit echten Fotos (Tempel, Laternen, Stoffe).

### Australien

**R9 GST herausrechnen** – Kl. 8, Prozent rückwärts.
- 33 AUD inklusive 10 % GST → die GST ist **3 AUD** (1/11), nicht 3,30. [B: Fehlvorstellung]
- TRS: 2 Käufe bei verschiedenen Händlern zu 180 und 150 AUD → keine Rückerstattung (je Händler unter 300). Ein Kauf zu 330 AUD → 30 AUD zurück.
- Exp.: Kassenzettel sammeln, GST ausrechnen, „Lohnt sich der TRS-Schalter?“, Frist 60 Tage am Reisekalender.

**R10 Bargeld-Rundung auf 5 Cent** – Kl. 5, Runden.
- 7,42 → 7,40; 7,43 → 7,45; 7,48 → 7,50.
- „Wie viel Cent gewinnt oder verliert man höchstens pro Einkauf?“ → **2**.
- Kl. 8: „Lohnt es sich, zwei Einkäufe getrennt zu bezahlen?“ Beispiel 3,02 und 3,02 → getrennt 3,00 + 3,00 = 6,00, zusammen 6,04 → 6,05.

**R11 Zeitzonen-Puzzle Australien** – Kl. 5, Zeitspannen, negative Zahlen; Kl. 8, Funktion/Tabelle.
- Kl. 5: Flug Tokio 20:00 (UTC+9) nach Melbourne (UTC+11 im November), Flugdauer 10 h (Beispielwert) → Ankunft **08:00** Ortszeit am nächsten Tag.
- Kl. 8: Am selben Augenblick ist es in Melbourne 12:00. → Adelaide 11:30, Brisbane 11:00, Perth 09:00, Bayern (UTC+1) 02:00.
- Silvester-Knobel: „Wann muss man in Bayern zum Telefon greifen, um ‚Frohes Neues‘ nach Melbourne zu sagen?“ → 31.12. um **14:00**.
- Exp.: Videoanruf planen, Flug, Fahrt nach Adelaide (Uhr eine halbe Stunde zurück), Zeitzonen-Karte.

**R12 Uluru** – Kl. 5, Maßstab/Zeit; Kl. 8, Geschwindigkeit, Prozent.
- Kl. 5: Modell 1 : 1 000 → 348 m werden **34,8 cm**. Kata Tjuta ist 546 − 348 = **198 m** höher. Der Rundweg dauert 3 h 30 min und soll vor 11 Uhr enden → spätestens **07:30** losgehen.
- Kl. 8: 10,6 km in 3,5 h ≈ 3 km/h. „Warum ist der Weg (10,6 km) länger als der Umfang (9,4 km)?“ → Er hält Abstand zum Felsen. Um wie viel Prozent länger? ≈ **12,8 %**.

**R13 Sydney Harbour Bridge** – Kl. 5, Maßstab, Schätzen; Kl. 8, Verhältnis.
- Kl. 5: 1 149 m mit 60-cm-Schritten → etwa **1 915 Schritte** (dann selbst zählen!).
- Kl. 8: Zeichnung 1 : 5 000 → Bogen **10,06 cm**. Höhe : Spannweite ≈ 0,27. Ausblick Jgst. 9: Der Bogen als Parabel.

**R14 Roadtrip-Expedition Melbourne–Adelaide** – Kl. 5/8, Mehrschritt, Tarife.
- Beispielwerte: Strecke, Verbrauch, Spritpreis.
- Teile: Fahrzeit bei Durchschnitt und Pausen · Tankstopps (Reichweite = Tank : Verbrauch·100) · Kosten · Mietwagen-Tarif (FU2) · Zeitzone (Adelaide 30 min zurück).

**R15 Fähre nach Tasmanien** – Kl. 8, Einheiten, Geschwindigkeit.
- Beispielwert: 430 km in 10 h → 43 km/h ≈ **23,2 Knoten**.
- „Wie lange braucht ein Flugzeug mit 750 km/h (Beispielwert)?“ → ≈ 34 min reine Flugzeit.

**R16 Weihnachten im Sommer – Tageslänge** – Kl. 5, Zeitspannen; Kl. 8, Daten/Graph.
- Die Familie liest Sonnenauf- und -untergang in der Wetter-App ab. Beispielwerte: Hobart ≈ 15 h 20 min, München ≈ 8 h 20 min am 21.12. → **7 h** Unterschied.
- Kl. 8: Monatswerte als Graph. „Wann sind beide Orte gleich lang hell?“ → um die Tagundnachtgleichen (Begriff).

**R17 Buckelwale an der Ostküste** – Kl. 5, Division; Kl. 8, Daten.
- Beispielwerte: 5 000 km in 60 Tagen → ≈ **83 km/Tag**.
- Kl. 8: Sichtungszahlen je Woche als Diagramm (vom Whale-Watching-Anbieter); Median der Woche.

**R18 Punktmuster zählen** – Kl. 5, Muster; Kl. 8, Term.
- Eigene Punktmuster aus Ringen, gezeichnet nach dem Besuch eines Museums. Werke werden nicht kopiert, und das Kind achtet auf die Hinweise zu Aborigine-Kunst vor Ort.
- Ringe mit 6, 12, 18 … Punkten → der n-te Ring hat 6n Punkte. Summe aus 4 Ringen = 60. Kl. 8: Summe = 3n(n + 1).

**R19 Gezeiten am Strand** – Kl. 8, Bruchteile, Zeitspannen.
- Beispielwerte: Hochwasser 06:12, Niedrigwasser 12:25, Tidenhub 2,4 m.
- Faustregel Zwölftelregel [A]: In der 3. Stunde fällt das Wasser um 3/12·2,4 = **0,6 m**.
- „Wann ist der Felsweg (trocken unter 0,8 m Pegel, Beispielwert) begehbar?“
- Exp.: Gezeitentabelle vor Ort lesen. Sicherheit: Die App ersetzt keine Tafel vor Ort.

**R20 Sportstatistik Cricket** – Kl. 5, Durchschnitt; Kl. 8, Kennwerte.
- Beispielwerte: Ein Spieler hat in 6 Innings 34, 0, 112, 8, 45, 21 Runs und war 5-mal aus. Cricket-Schnitt = Runs : Outs = 220 : 5 = **44**.
- „Warum teilt man durch die Outs, nicht durch die Innings?“ [B]

### Südostasien, Europa, Amerika, Welt

**R21 Wechselstube: Ankauf und Verkauf** – Kl. 8, Prozent, Verhältnis.
- Beispielwerte: Die Wechselstube kauft 1 € für 1,62 AUD und verkauft 1 € für 1,78 AUD.
- 100 € → 162 AUD → zurückgetauscht **91,01 €** → fast 9 % weg. „Welcher Kurs ist für mich der ‚gute‘?“ [B]
- Kl. 5: Mit glattem Kurs 1 € = 2 Einheiten (Beispielwert): Preise halbieren zum Überschlagen.

**R22 Großkreis: Wie weit ist Tokio–Sydney?** – Kl. 8, Kreisumfang, Grad.
- 1° auf einem Meridian ≈ 40 000 : 360 ≈ 111 km.
- Tokio 35,7° N, Sydney 33,9° S → 69,6° Breitenunterschied → ≈ **7 730 km** (untere Schranke).
- Genau, mit Kugelformel: ≈ 7 830 km (per Programm; Kinder vergleichen nur).
- Kl. 5: Mit Faden auf dem Globus messen und am Maßstab umrechnen.

**R23 Fahrenheit (USA)** – Kl. 5, Faustregel; Kl. 8, lineare Funktion.
- Kl. 5: Faustregel „verdoppeln + 30“ gegen genau: 20 °C → 70 gegen 68 °F; 30 °C → 90 gegen 86.
- Kl. 8: F = 1,8C + 32. „Bei welcher Temperatur zeigen beide Skalen dieselbe Zahl?“ → **−40**. „Wo ist die Faustregel genau?“ → bei 10 °C.

**R24 Meilen und km (USA, UK)** – Kl. 5, Schätzen; Kl. 8, Proportionalität.
- 65 mph ≈ **104,6 km/h**.
- Trick: Fibonacci-Zahlen: 5 mi ≈ 8 km (8,05), 8 mi ≈ 13 km (12,87). „Warum klappt das ungefähr?“ → das Verhältnis aufeinanderfolgender Fibonacci-Zahlen ≈ 1,618 ≈ 1,609.

**R25 Verbrauch l/100 km gegen mpg** – Kl. 8, indirekte Proportionalität.
- 30 mpg (US-Gallone) → ≈ **7,84 l/100 km**. „Doppelt so viele mpg – halber Verbrauch?“ → ja, l/100 km halbiert sich.

**R26 Trinkgeld und Sales Tax (USA)** – Kl. 8, Prozentkette.
- Beispielwerte: 42 $ Essen, 8,875 % Steuer, 18 % Trinkgeld auf den Betrag vor Steuer → 42 + 3,73 + 7,56 = **53,29 $**.
- „Ist ‚20 % auf den Endbetrag‘ mehr oder weniger?“ → mehr (9,15 $).

**R27 Islamische Sternmuster** – Kl. 5, Symmetrie; Kl. 8, Innenwinkel, Drehung.
- Für Reiseziele mit solchen Ornamenten (z. B. Andalusien, Türkei, Marokko, Malaysia – je nach Route).
- Achtzackiger Stern aus zwei Quadraten, 45° gedreht. „Wie viele Symmetrieachsen?“ → 8. Siehe GE6.

**R28 Peilung und Kompass** – Kl. 5, Winkel bis 360°.
- Kurs 135° = Südost; Rückkurs 135 + 180 = **315°**.
- Kl. 8: Schatzkarte mit Kurs und Strecke auf dem Gitter (GE4), Endpunkt bestimmen.

**R29 Höhenmeter und Temperatur** – Kl. 8, lineare Funktion.
- Faustwert [A]: ≈ −0,65 °C je 100 m. Talstation 1 200 m mit 18 °C (Beispielwert) → auf 3 200 m ≈ 18 − 13 = **5 °C**.
- „Was muss in den Rucksack?“ Exp.: Wanderung mit Höhenprofil (FU1), Temperatur, Zeit, Wasserbedarf.

**R30 Länder-Steckbrief-Vergleich** – Kl. 5, große Zahlen, Runden; Kl. 8, Dichte, Verhältnis, Diagramm.
- Fläche und Einwohner von Deutschland, Japan, Australien aus einer amtlichen Quelle (z. B. Statistikämter).
- **In dieser Recherche nicht belegt**, die Werte muss die Familie einsetzen.
- Kl. 8: Einwohner je km², Säulendiagramm, Lügendetektor (D2) mit abgeschnittener Achse.

**Bauregel für Reise-Expeditionen [M]:**
- Teil 1 schätzen (Z7);
- Teil 2 rechnen;
- Teil 3 ein Darstellungswechsel (Tabelle/Graph/Karte);
- Teil 4 eine Entscheidung mit Begründung („lohnt sich?“, „welcher Kurs?“);
- Teil 5 optional ein echtes Messen vor Ort (Schritte, Zeit, Kassenzettel).

So steckt in jeder Expedition [B] und [Ü].

---

## 3. Zehn Knobel-Rubriken (wiederkehrend, z. B. „Knobel der Woche“ aus ideen.md M2)

Jede Rubrik hat eine Kl.-5- und eine Kl.-8-Stufe mit gleicher Idee (wie M2). Alle Beispiele sind per Programm auf eindeutige Lösung geprüft.

| Nr | Rubrik | Quelle/Vorbild | Beispiel Kl. 5 | Stufe Kl. 8 | Prüfung | Zufall |
|---|---|---|---|---|---|---|
| K1 | **Flächenlabyrinth** | Area Maze (Inaba) [A] | 12 \| 18 / 10 \| ? → 15 | Seiten als Brüche oder mit x | Zahl | ja |
| K2 | **Rechenkäfig (KenKen-Art) 4 × 4** | KenKen [A] | Jede Zeile/Spalte enthält 1–4. Summen-Käfige: (Z1 S1+S2) 3 · (Z1 S3+S4) 7 · (Z2 S1+Z3 S1) 7 · (Z2 S2+S3) 5 · (Z2 S4+Z3 S4) 3 · (Z3 S2+Z4 S2) 4 · (Z3 S3+Z4 S3) 6 · Z4 S1 = 2 · Z4 S4 = 3 → eindeutig (geprüft). Lösung: 1 2 3 4 / 3 4 1 2 / 4 3 2 1 / 2 1 4 3. Erster Versuch mit ·-Käfigen hatte 2 Lösungen, deshalb ist die Eindeutigkeits-Prüfung Pflicht. | Käfige mit −, ·, : und negativen Zahlen | Lücken (16) | ja (Lösung würfeln, Käfige wählen, auf Eindeutigkeit prüfen) |
| K3 | **Kakuro mini** | Kakuro [A] | 2 × 2: Zeilen 4 und 11, Spalten 9 und 6, keine Ziffer doppelt → 3 1 / 6 5 (eindeutig) | 3 × 3 mit größeren Summen | Lücken | ja |
| K4 | **Nim gegen die App** | Nim-Spiele [A] | 21 Hölzer, abwechselnd 1–3 nehmen, wer das letzte nimmt, gewinnt. Gewinnstrategie: dem Gegner immer ein Vielfaches von 4 lassen → als Erster 1 nehmen. | „Mit 1–5 nehmen? Mit 50 Hölzern?“ → Vielfache von 6; 50 = 48 + 2 → 2 nehmen. Begründung [B] | Spielzüge; Schlussfrage Zahl | ja |
| K5 | **Geheimschrift** | Caesar, Zahlencodes [A] | Caesar +3: SYDNEY → VBGQHB; Kind entschlüsselt die nächste Reisestadt | Verschlüsselung als Funktion x ↦ (x + k) mod 26 oder (3x + 1) mod 26; „Welches k entschlüsselt?“ | Text/Zahl | ja |
| K6 | **Logikrätsel** | Einstein-Rätsel light [A] | Kai, Mia und Ben waren in Japan, Australien und Thailand. Kai nicht in Japan, Mia weder in Australien noch in Thailand, Ben nicht in Thailand → Kai Thailand, Mia Japan, Ben Australien (eindeutig) | 4 × 4 mit „wenn – dann“ und einer Lügner-Aussage | Zuordnung | teilweise |
| K7 | **Streichholz-Gleichung** | Streichholzrätsel [A] | Ein Holz umlegen, damit die Gleichung stimmt (Ziffern aus 7-Segment-Hölzern, der Server prüft das Ergebnis) | Mit „×“ und zweistelligen Zahlen | Server prüft: ein Holz bewegt + Gleichung wahr | ja (7-Segment-Regeln) |
| K8 | **Tangram-Bruchteile** | Tangram [A] | „Welcher Teil des Quadrats ist ein kleines Dreieck?“ → 1/16; großes Dreieck 1/4, Quadrat 1/8 (Summe aller 7 Teile = 1, geprüft) | Flächen in cm² bei 12 cm Seite; Figur legen, Fläche bleibt gleich [B] | Bruch/Zahl | nein (feste Teile) |
| K9 | **Vier Vieren** | klassisch; Variante zu A1 „Mach 100“ | 1 bis 5 mit vier Vieren: 44 : 44 = 1; 4 : 4 + 4 : 4 = 2; (4 + 4 + 4) : 4 = 3; 4·(4 − 4) + 4 = 4; (4·4 + 4) : 4 = 5 | Mit Potenzen, Wurzel, Fakultät bis 20 | Term-Rechner (wie A1) | ja |
| K10 | **Känguru-Freitag** | Känguru-Archiv 1998–2026, frei als PDF [G: https://www.mathe-kaenguru.de/chronik/aufgaben/index.html] | 3 Originalaufgaben Kl. 5/6 auf **Papier**, Antwort-Buchstaben in die App | dasselbe mit Kl. 7/8 | Auswahl (A–E) | nein |

Zu K10: Nur Antwortbuchstaben gehören in die App, nicht die Aufgabentexte. Nutzungsbedingungen siehe Abschnitt 5.

---

## 4. Zehn Formate: Kinder bauen oder verändern Aufgaben (mit Prüfregel)

| Nr | Auftrag | Prüfregel (Server) | Beispiel Kl. 5 | Beispiel Kl. 8 |
|---|---|---|---|---|
| B1 | **Erfinde eine Rechnung mit Ergebnis 12, in der mindestens zwei verschiedene Rechenzeichen und eine Klammer vorkommen** | Term-Rechner: Wert = 12, Zeichen-Bedingung erfüllt, Klammer verändert den Wert (sonst „Klammer überflüssig“) | (2 + 4)·2 = 12 ✓; 3·4 ✗ (nur ein Zeichen) | Mit negativer Zahl und Potenz: (−2)² · 3 = 12 ✓ |
| B2 | **Ändere eine Zahl, sodass …** | Zielbedingung, Rest unverändert | 4·17·□ soll sich leicht rechnen lassen → □ = 25 (4·25 = 100; Ergebnis 1 700) | 3x + □ = 20 soll x = 4 haben → □ = 8 |
| B3 | **Baue ein Zahlenmauer-Rätsel mit genau einer Lösung** | Der Server löst die Mauer, zählt die Lösungen und zeigt bei mehreren zwei davon | 3 Steine unten, einer fehlt, Spitze gegeben | Mit Variable unten, Lösung ganzzahlig |
| B4 | **Erfinde Daten, sodass Mittelwert > Median** | Kennwerte berechnen | (Vorgriff) 1, 2, 3, 10 → Durchschnitt 4, Mitte 2,5 ✓ | 5 Werte, zusätzlich Spannweite 10 |
| B5 | **Steckbrief für das Geschwister** (A7 umgekehrt) | Der Server prüft im Bereich (z. B. 1–1 000) die Eindeutigkeit, sonst die Rückmeldung „passt auch auf 84“ | „zweistellig, durch 3 und 4 teilbar, Quersumme 12“ → zweideutig (48, 84), ergänzen! | Steckbrief eines Terms oder einer Geraden („steigt, durch (0\|−1) …“) |
| B6 | **Fehler-Erfinder** – baue eine falsche Rechnung mit einem typischen Fehler für die App-Figur | Seiten an Zufallswerten ungleich + Fehlermuster aus der Bibliothek (tief-2) erkannt | 7 − 3·2 = 8 (Punkt vor Strich missachtet) | −(x − 4) = −x − 4 (Minusklammer) |
| B7 | **Gib Werte an, sodass das Ergebnis möglichst groß ist (eigenes Open Middle)** | Brute force zeigt das Optimum und den Abstand des Kindes | Ziffern 1–6 in □□ × □□ möglichst groß → 63·54 = 3 402 (geprüft) | □x + □ = □ mit Lösung möglichst nah an 0, aber ≠ 0 |
| B8 | **Erfinde eine Figur mit Fläche 12, die kein Rechteck ist** | Punkte (F3), Flächenformel des Programms (Gauß), einfaches Vieleck, kein Rechteck | Parallelogramm 4 × 3 auf dem Gitter | Trapez oder Dreieck mit Fläche 12, Ecken nicht auf den Achsen |
| B9 | **Erfinde ein faires Würfelspiel** | Fälle zählen: genau die Hälfte der 36 | „Gerade Summe gewinnt“ → 18 ✓ | Mit Produkt: „Produkt gerade“ → 27 von 36, unfair; Kind korrigiert |
| B10 | **Mach die Aufgabe für deine Schwester bzw. deinen Bruder passend** (Kl. 8 baut für Kl. 5 und umgekehrt) | Das Programm prüft Lösbarkeit und Ganzzahligkeit; Eltern oder Lehrer geben frei | Kl. 5 baut eine Bild-Gleichung (AL3) für Kl. 8 | Kl. 8 vereinfacht ein LGS zu einem Emoji-Rätsel für Kl. 5 |

Nachgerechnet:
- B7: Größtes Produkt □□ × □□ aus 1–6 ist 63 · 54 = 3 402 (alle Belegungen durchprobiert).
- B9: „Produkt gerade“: 36 − 9 = 27 Fälle; „Summe gerade“: 18 Fälle.
- B1: (−2)²·3 = 12.
- K4: Bei 50 Hölzern und 1–5 nehmen 2 nehmen, Rest 48 = 8·6.
- Die Prüfskripte liegen in `/tmp/ideen12/` (check.py, knobel.py), nicht im Projektordner.

---

## 5. Die 15 besten frei zugänglichen Quellen

Nutzungsbedingungen nur wiedergegeben, keine Rechtsberatung. „Nicht geprüft“ heißt: auf der Seite nicht gefunden oder nicht abgerufen.

| # | Quelle | Link | Sprache | Nutzungsbedingung (wiedergegeben) | Besonders |
|---|---|---|---|---|---|
| 1 | NRICH (Univ. Cambridge) | https://nrich.maths.org | EN | Kein Spiegeln im Netz; Kopien für Schüler der eigenen Schule erlaubt; sonst schriftliche Erlaubnis [G: https://nrich.maths.org/terms] | Tausende „low threshold, high ceiling“-Aufgaben für 3–18 Jahre, Lehrerhinweise zum Stützen |
| 2 | Don Steward, Median-Blog | https://donsteward.blogspot.com | EN | CC BY-NC-SA 4.0 (nicht-kommerziell, bearbeiten erlaubt) [G: https://donsteward.blogspot.com/p/don-stewards-rough-notes.html] | „Tasks with depth“ für 10–16 Jahre, nach Themen; Rechendreiecke, Rückwärtszahlen, Kennwert-Aufgaben |
| 3 | Illustrative Mathematics 6–8 | https://im.kendallhunt.com/MS/students/1/index.html | EN (ES) | CC BY 4.0 für IM 6–8/K–12; IM v.360 CC BY-NC 4.0 [G: https://www.illustrativemathematics.org/terms-of-use] | Vollständiges, problembasiertes Curriculum; Warm-ups „Notice and Wonder“, „Which one doesn’t belong“; **einzige große Quelle, deren Aufgaben man bearbeitet übernehmen dürfte** |
| 4 | Mathematics Assessment Project (Shell Centre) | https://map.mathshell.org | EN | CC BY-NC-ND 3.0 (unverändert, nicht-kommerziell) [G: https://map.mathshell.org/docs/map_cc_teacher_guide.pdf] | 100 Classroom Challenges: Card Sorts, Fehlvorstellungen, Problemlösen |
| 5 | Känguru der Mathematik (Archiv) | https://www.mathe-kaenguru.de/chronik/aufgaben/index.html | DE, EN, FR | Freie PDFs 1998–2026 für alle Stufen; eigene Nutzungsbedingung auf der Seite nicht gefunden | Kurze, witzige Auswahlaufgaben; Kl. 5/6 und 7/8 |
| 6 | Mathematik-Olympiade (Trainingsmaterial) | z. B. https://www.sachsen.schule/~bezirkskomitee/01-MO-Vo-Einl-6-1.pdf | DE | Aufgabenblätter tragen „© Aufgabenausschuss … Alle Rechte vorbehalten“ [G: z. B. https://stadtteilschule-kirchwerder.hamburg.de/wp-content/uploads/sites/170/2024/09/MO641_Aufgaben_3-6.pdf] | Freie Aufgaben mit Lösungsweg; Kombinatorik, „Zahlen werden gesucht“; Begründen wird bewertet |
| 7 | Tag der Mathematik Uni Bayreuth (Archiv) | https://www.tdm.uni-bayreuth.de/de/archiv/aeltere-aufgaben/2019/loesungen_2019_05-06.pdf | DE | nicht geprüft | **Bayerischer Wettbewerb**, Kl. 5–6 mit Lösungen, Ansätze werden bepunktet |
| 8 | Landeswettbewerb Mathematik (RLP-Archiv; Bayern mit BW) | https://bildung.rlp.de/fileadmin/user_upload/lawema.bildung.rlp.de/Aufgaben1_Runde_2026.pdf | DE | nicht geprüft | Aufgaben mit Bewertungsvorschlägen (Teilpunkte!), auch „Gib jeweils ein Beispiel an“ |
| 9 | MathALÉA (Coopmaths) | https://coopmaths.fr/alea/ | FR | Hefte unter CC BY-SA, Quellcode offen [G: https://lyc-hautil-jouy.ac-versailles.fr/IMG/pdf/cdv_premiere_2025.pdf, https://bibnum.publimath.fr/AAB/AAB24027.pdf] | **Über 2 000 Aufgaben-Generatoren mit Zufallsdaten** – das engste Vorbild für die eigene App-Technik und -Inhalte |
| 10 | Open Middle | https://www.openmiddle.com | EN, ES, FR | Seite: „© … All rights reserved“; ältere Kopien nennen CC BY-NC-SA 4.0 → widersprüchlich, nur Ideen nutzen [G: Startseite] | Ziffernkarten-Aufgaben nach Klasse und Thema |
| 11 | Inquiry Maths | https://sites.google.com/site/inquirymaths | EN | nicht geprüft | „Prompts“ wie 40 % von 70 = 70 % von 40 – Startpunkte für Begründen |
| 12 | SSDD Problems (Craig Barton) | https://ssddproblems.com | EN | nicht geprüft (Mr-Barton-Seite: teilen/ändern mit Nennung [G: https://mrbartonmaths.com/about/terms.html]) | Vier Aufgaben mit gleicher Oberfläche, verschiedener Mathematik – trainiert „Welches Verfahren?“ |
| 13 | Which One Doesn’t Belong | https://wodb.ca | EN | nicht geprüft | Viererkarten zu Zahlen, Formen, Graphen |
| 14 | AoPS-Wiki: AMC 8 | https://artofproblemsolving.com/wiki/index.php/AMC_8_Problems_and_Solutions | EN | Aufgaben © MAA. MAA ermutigt Lehrkräfte, sie Schülern zu Lernzwecken zu geben, mit Quellenangabe [G: https://isinj.com/mt-amc8/2020-AMC8-Solutions.pdf] | 25 Aufgaben/40 min, ab 1985 mit vielen Lösungswegen |
| 15 | Japanisch: Wikibooks „中学受験算数“ und Präfektur-Lehrmaterial (Osaka, Kanagawa) | https://ja.wikibooks.org/wiki/中学受験算数/平面図形 · https://www.osaka-c.ed.jp/sansu/chu2/c2_8.pdf | JA | Wikibooks: CC BY-SA [A: Standard bei Wikibooks]; Präfektur: nicht geprüft | Japanische Geometrie-Kultur: Scherung, Hilfslinien, Winkeljagd |

**Weitere, nicht in die 15:**
- UKMT: neue Past Papers frei, ältere kostenpflichtig [G: https://ukmt.org.uk/product-category/past-paper].
- Dan Meyer 3-Act: Lizenzangabe CC BY-NC 3.0 laut einer PBS-Übernahme [G: https://lsintspl3.wgbh.org/en-us/lesson/mgbh_il_superbear/credits/]; für die App ohne Video wenig nutzbar.
- Polypad/Mathigon: frei, nicht-kommerziell [G: https://polypad.amplify.com/faqs].
- MathUs.ru: Olympiade-Aufgaben Kl. 5, russisch [G: https://mathus.ru:443/math/5math2023.pdf].
- Sangaku-Linkliste Durham (siehe GE8).

---

## 6. Meine Top 20 für diese zwei Kinder [M]

Kriterien:
- schließt eine BMT-Lücke;
- macht beiden Kindern Lust;
- läuft mit Zufallswerten;
- braucht keine neue Großtechnik oder nur den ohnehin geplanten Term-Rechner bzw. die geplanten Punkte-, Felder- und Zuordnungsformen.

| Rang | Idee | Warum zuerst |
|---|---|---|
| 1 | **D1 Datensatz bauen** + **B4** | Trifft die schwerste BMT-Gruppe (offene Umkehr, ≈ 31 %) und Daten zugleich; Prüfung per Kennwert-Rechnung ist trivial |
| 2 | **Z1 Ziffernkarten-Ziel** | Eine Form, endlos viele Aufgaben in allen Gebieten; Optimum per Programm; hoher Reiz |
| 3 | **GE2 Gleiche Fläche ohne Formel** | BMT-Geometrie-Begründen (unter 20 % gelöst); japanische Stärke, direkt passend zum Japan-Teil der Reise |
| 4 | **GE1 Winkeljagd** mit Begründungs-Bausteinen | Geometrie + [B] in einem; Jgst. 7 („Papier-Jahr“) steht dem 8.-Klässler gerade bevor |
| 5 | **Z10 WODB** (für alle Gebiete) | Begründen in Fachsprache, jede Antwort kann richtig sein → Selbstvertrauen |
| 6 | **AL4 Was ist meine Regel?** | Spielerisch zum Term; zieht von Kl. 5 bis Funktionen Kl. 8 |
| 7 | **AL2 Ein Bild – viele Terme** | BMT „Term aus Figur“; zeigt Gleichwertigkeit statt Regel |
| 8 | **R11 Zeitzonen-Puzzle** + **R9 GST** | Echte Reisezahlen, belegt; negative Zahlen und Prozent rückwärts im Alltag |
| 9 | **D4 Ist das Spiel fair?** + **B9** | Zählen/Laplace mit echtem Spielen am Abend |
| 10 | **FR8 Flächenlabyrinth** als Rubrik | Hoher Reiz, Fläche rückwärts, endlos generierbar |
| 11 | **D2 Diagramm-Lügendetektor** | Daten + Begründen, Lehrplan „Manipulation erkennen“ |
| 12 | **FR4 Maßstab bei Fläche/Volumen** | BMT-Lücke unter 20 %; kurz und klar |
| 13 | **AL5 Gleichwertig oder zufällig gleich?** | Begründen-Kern: ein Gegenbeispiel genügt, ein Beispiel beweist nichts |
| 14 | **G2 Rabatt-Duell / G3 Hin und zurück** | Prozent mit Entscheidung und Begründung, Alltagsnutzen |
| 15 | **GE7 Wo darf der Punkt liegen?** | BMT „Punkt mit Bedingung“, per Gitterpunkt automatisch prüfbar, Vorstufe zur Konstruktion |
| 16 | **Z3 Rechendreieck** (Plus für Kl. 5, Mal mit Negativen für Kl. 8) | Gleiche Rubrik für beide Kinder, Systematik statt Raten |
| 17 | **FU1 Geschichte ↔ Graph** mit eigenen Wanderungen | Daten + Funktionen + Reise; Darstellungswechsel ist BMT-Kern |
| 18 | **R7 Kaiten-Sushi / AL3 Bild-Gleichungen** | LGS (Jgst. 8) und Gleichungs-Gefühl (Kl. 5) mit höchstem Reiz |
| 19 | **B10 Aufgaben fürs Geschwister** | Wer baut, muss verstehen; verbindet die beiden Kinder; die Prüfung macht das Programm |
| 20 | **Z4 Strukturiertes Päckchen** | Variation + Begründen + binomische Formel; Brücke Kl. 5 ↔ Kl. 8 |

**Reihenfolge-Tipp [M]:** Ränge 1, 2, 5, 13 und 19 laufen über den Term-Rechner bzw. eine Bedingungsprüfung. Diese Prüfart einmal sauber bauen („Server prüft Bedingung statt Musterlösung“) trägt etwa die Hälfte dieser Liste.

---

## 7. Was die App schon gut abdeckt – und was auffällig fehlt

Grundlage: ideen.md, auftrag1 §0 (Antworttypen: `zahl` 54 %, `auswahl` 31 %, `luecken` 15 %, Zeichnung in 10,7 % der Aufgaben), Auftragstext.

**Gut abgedeckt [A, aus der Beschreibung]:**
- Verfahren üben (direkt, mehrschrittig) in allen sieben Gebieten.
- Umkehraufgaben und eingekleidete Aufgaben.
- Knobel am Ende eines Lernziels und Expeditionen als Rahmen; das passt ideal zur Reise-Geschichte.
- „Finde den Fehler“ und „Begründe“ – aber nur als Auswahl.

**Auffällig fehlt [M]:**
1. **Offene Antworten mit Bedingungsprüfung** („gib ein Beispiel“, „erfinde“, „baue“): D1, Z1, B1–B10. Das ist die schwerste BMT-Gruppe, und die App hat dafür heute praktisch nichts.
2. **Begründen mit eigener Struktur.** Die heutige Auswahl prüft Wiedererkennen. Es fehlen Gegenbeispiel, „zufällig gleich?“, Bausteine ordnen, WODB mit eigenem Grund.
3. **Geometrie ohne Formel und ohne Messen:** Scherung, Winkeljagd, Ortslinie per Gitterpunkt, Ornamente. Bisher ist Geometrie vor allem Berechnen.
4. **Daten aus eigener Erhebung** (würfeln, schätzen, messen auf der Reise) und **Diagramm-Kritik**.
5. **Struktur-Aufgaben:** Päckchen, Mauern, Rechendreiecke, Kalender. Sie zeigen, *warum* ein Verfahren funktioniert; bei 30 000 Einzelaufgaben fehlt der Zusammenhang zwischen Aufgaben.
6. **Entscheidungsaufgaben** („Was wäre dir lieber?“, „Lohnt sich das?“, „Welcher Kurs ist gut?“). Sie verbinden Rechnen mit Urteilen und sind der natürliche Abschluss jeder Reise-Expedition.
7. **Gemeinsame Rubrik für beide Kinder** mit gleicher Idee in zwei Stufen. In ideen.md als M2 angelegt; die 10 Rubriken aus Abschnitt 3 füllen sie.
8. **Spiele mit Gegner** (Nim, faire Würfelspiele). Nur sie trainieren Strategie und Begründen „warum gewinne ich immer?“.
9. **Papier-Teil mit klarer Rolle:** Netze, Zirkel, Känguru-Freitag, Begründungen frei schreiben. Die App kann nur Antwortbuchstaben bzw. Zwischenergebnisse prüfen (tief-10 §6).

**Kurz: Was die inhaltlich stärksten Apps anders machen** – [A]: in diesem Lauf **nicht** eigens recherchiert, aus allgemeinem Wissen.
- Beast Academy und Alcumus (AoPS): Aufgaben mit steigender Tiefe und vielen Knobel-Aufgaben.
- Brilliant: zuerst ein interaktives Rätsel, dann der Begriff.
- DragonBox: Gleichungen als Spiel mit Karten.
- Mathigon: Geschichten mit eingebetteten Fragen.
- Desmos: Vorhersagen vor dem Zeigen; Card Sorts; Graph-Ziele.
- MathALÉA: Zufalls-Generatoren für jedes Thema ([G] siehe Quelle 9).

Für Details siehe tief-1 und tief-10; hier nicht geprüft.

---

## Was ich nicht prüfen konnte

- **Nicht abgerufen**, nur aus Sekundärquellen oder Allgemeinwissen beschrieben: Estimation 180, Would You Rather Math, Numberless Word Problems, Watson & Mason, Area Maze (Inaba), KenKen, Beast Academy, Brilliant, DragonBox, Desmos, Alcumus, Dr Frost, bettermarks.
- **Wettbewerbe ohne Prüfung von Archiv und Bedingungen:** Bolyai, Pangea, Mathcounts, Australian Mathematics Competition, Singapur (SMO, SASMO), japanische Sansu-Olympiade, Turnier der Städte, Kvant, KöMaL, Purple Comet.
- **Mathematik-Olympiade:** Das zentrale Aufgabenarchiv mathematik-olympiaden.de ließ sich nicht abrufen (robots-Sperre). Belegt sind nur Schul-PDFs mit dem ©-Vermerk.
- **Landeswettbewerb Bayern:** eigenes Archiv nicht gefunden, nur das RLP-Archiv und ein bayerisches Aufgabenblatt 2023/24.
- **Nutzungsbedingungen:** Bei mehreren Quellen „nicht geprüft“ (siehe Tabelle 5). Open Middle ist widersprüchlich.
- **Weltzahlen:** Nicht belegt sind Yen-Münzen, Japan UTC+9, Meile, Knoten und Gallone, Erdumfang, Temperatur-Faustwert, Zwölftelregel (alle als [A] markiert) sowie alle „Beispielwerte“. Ländervergleich R30 ohne Zahlen.
- **Kinder:** Wie die zwei Kinder auf die Formate reagieren, kann nur ein Versuch zeigen. Die Reiz-Noten sind Meinung.
