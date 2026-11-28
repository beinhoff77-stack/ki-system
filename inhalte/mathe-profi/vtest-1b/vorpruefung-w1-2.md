# Vorprüfung W1, zweite Runde – Einheit 20 `gleichungen.bruch` (VT1B-022 bis 041), Stand 06db098c

Umfang: die 20 Aufgaben der Neufassung (18 neu, 023 und 041 unverändert). `vorrat-folgerunde/` nicht geprüft. Maßstab: Urteil 1222, `vtest-1/auftrag.md` und die Vorgabe dieser Runde (je Lernziel höchstens eine Schema-Aufgabe, Test nie Schema und anspruchsvollste, ≥ 4 Denkfiguren, verschiedene Denkfiguren über die vier Tests, kein Bestandskern, Bauart, Grundmenge, Klasse 8). Nichts an Aufgaben geändert.

Werkzeug: `vorpruefung_w1_rechnen.py` (für diese Fassung neu geschrieben; exakte Rechnung mit `Fraction`, Polynom-Interpolation, Kandidaten gegen D; Parameter über ein Raster von rund 300 rationalen Werten einschließlich aller Sonderwerte; 030 über alle a, b, c, d ∈ {−3 … 3} mit b ≠ d). Ergebnis: **alle 20 Sollwerte bestätigt**, jede Lücke mit eigenem Fehlbild, kein Fehlbild gleich der Lösung. `tools/vtest_pruefen.py --runde 1b`: für Einheit 20 nur die erwarteten Pool-Meldungen „2 statt 3“.

Bestand erneut gelesen: `themen/gleichungen.bruch.json` (325), `rollend-7`/`-11`/`-13` (40), `rollend-15` (keine Datei der Einheit), dazu gezielt `terme.bruchterme` (330), `groessen.verhaeltnisse` (230), `groessen.indirekt` (309), `groessen.proportional`, `gleichungen.linear` per Mustersuche über alle Aufgabentexte. „T n“ = Position n (ab 0) in `themen/gleichungen.bruch.json`, „BT n“ in `themen/terme.bruchterme.json`.

## Urteil

**Bereit für die Gegenprüfung: nein.** Rechnung und Fehlbilder sind sauber, und die Neufassung schließt die meisten Befunde der ersten Runde. Es bleiben: eine mehrdeutige Lücke im Test 022, dieselbe Denkfigur in den Tests 022 und 032, ein Test 032, der leichter ist als seine Korrektur 033, zwei bzw. drei Schema-Aufgaben in `ueber_kreuz` und `scheinloesung`, eine Bestandsdoppelung (036) und ein über drei Aufgaben gleiches Bauart-Muster (025/030/035). **7 A, 7 B, 7 C.**

## Entscheidungen zu den vom Schreiber genannten Angriffspunkten

| Punkt | Entscheidung |
|---|---|
| Schema-Grenzfall 022 | kein Schema (keine Standardroutine fragt, was eine Umformung mit D macht) – aber A1, A2 |
| Schema-Grenzfall 026 | kein Schema, aber dieselbe Denkfigur wie 023 (Parameter rückwärts aus D) → B2 |
| Schema-Grenzfall 028 | **Schema**: x₀ = −9,5 ausrechnen, in die zweite Gleichung einsetzen, a bestimmen (Verfahren T 131/T 134) löst die Aufgabe ohne die Einsicht „nur das Zählerverhältnis zählt“ → A4 |
| Schema-Grenzfall 036 | **Schema**: f − g ausrechnen ist reine Bruchterm-Subtraktion; ein Bild gibt es nicht. Dazu Bestand R8-V053 → A5, A6 |
| Test 027, Fall a = 0 | trifft den Kern von `ueber_kreuz` ausreichend: der Fall a = 7 (0 · x = 49) entsteht genau beim Über-Kreuz-Multiplizieren; a = 0 ist Vertiefung. Zulässig, aber schwer und mit Überschneidung zu 033 → B1 |
| Test 032 als Auswahl | nicht die anspruchsvollste: 033 (Hauptnenner durch Ausklammern, zwei Werte rückwärts) verlangt mehr; 032 ist Wiedererkennen mit Hinweis im Text → A3 |
| Bestandsnähe 036 / 037 / 040 / 031 | 036 Bestandskern (A6); 037 kein Bestandskern (Bestand vergleicht nur zwei Mischungen, mischt sie nicht); 040 kein Bestandskern (`groessen.indirekt` fragt fehlende Werte, nicht das Verhältnis); 031 Einsicht wie T 130, als Schema offen ausgewiesen – in Ordnung, belegt aber den einen Schema-Platz |
| Etiketten einkleidung/mehrschritt + bruecke | 029 und 031 passen (echte zwei Wege bzw. Verfahren wählen). 024, 034, 038 nicht: Modell aufstellen ist `transfer`, nicht `bruecke` → B6 |
| „immer – manchmal – nie“ (025, 030, 035) | erkennbares Muster → A7 |
| Grundmenge ℤ in 026 | Klasse 8 zulässig (Grundmenge ist M7-Begriff) → C1 |
| Graphen von Bruchtermen in 036 | Lernbereich M8 4 deckt Bruchgleichungen grafisch (Lernziel `graphisch` der Einheit); hier aber ohne Bild nur Etikett → C4 |

## Befunde A (Muss)

| Nr. | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| A1 | 022 (Test) | Die Form von Gleichung (T) steht nicht im Text. Schreibt ein Kind Toms Umformung ungekürzt hin, (x − 2) · 6/(x − 2) = (x − 2) · 3/(x − 1), schließt ihre Definitionsmenge 1 **und** 2 aus – Antwort 2, die gerade als Fehlbild („Malnehmen ändere D nicht“) gewertet wird. Erst das stille Kürzen auf 6 = 3(x − 2)/(x − 1) gibt 1. | Zusammen mit A2 lösen: Tom-Teil streichen, zweite Lücke „(L) schließt □ Zahlen aus“ → [0; 3] (geprüft: 0, 1, 2). Will man Tom behalten, (T) wörtlich in den Text schreiben. |
| A2 | 022 und 032 (Tests) | Gleiche Denkfigur in zwei Tests: Toms Malnehmen vergrößert D (die 2 wird erlaubt), Tims Kürzen vergrößert D (die 0 wird erlaubt) – „Umformung verändert D, darum D an der Ausgangsgleichung“. Der Lösungsweg von 022 formuliert genau die Lehre von 032. | Mit A1: 022 nur noch „Addieren eines Bruchs verkleinert D, die Lösung geht verloren“; 032 behält „Kürzen vergrößert D“. |
| A3 | 032 (Test) | Leichter als Korrektur 033: Auswahl unter Tims drei Schritten, Inas Satz („bestimmt zuerst die Definitionsmenge der Ausgangsgleichung“) zeigt die Richtung, Möglichkeit 1 („{0} und { } dasselbe“) wählt kaum jemand, nur die richtige hat einen „obwohl“-Nebensatz. Ein gutes Kind braucht 1–2 Minuten. | 032: Inas Hinweis streichen; Möglichkeit 1 durch einen plausiblen Ablenker mit falscher Folgerung ersetzen (z. B. „Beim Lösen von x + 6 = −3x + 6, denn daraus folgt x = 3“); alle Möglichkeiten im selben Satzbau. 033 auf einen Wert kürzen (c für Kandidat 2 → 6, geprüft), damit die Korrektur nicht schwerer als der Test ist. |
| A4 | Schema ueber_kreuz: 028, 031 | 031 offen als Schema; 028 per Rechnung lösbar (Skript: x₀ = −19/2, einziges a = 6), Verfahren wie T 131/T 134. → 2 Schema. | 028 so stellen, dass Ausrechnen nicht geht: „10/(x − p) = a/(x + q) und 15/(x − p) = 9/(x + q) mit beliebigen Zahlen p, q (p ≠ −q): Für welches a haben beide Gleichungen immer dieselbe Lösung?“ → 6 (geprüft für 11 Paare p, q). |
| A5 | Schema scheinloesung: 034, 035, 036 | 034 offen als Schema (Zahlenrätsel, Standardverfahren). 035: die richtige Regel „Scheinlösungen können vorkommen“ weiß jedes Kind, das den Begriff kennt – Wissensabruf, kein Verstehen; die vier Beispiele muss man nicht einmal prüfen. 036: f − g = −1 ist reine Bruchterm-Subtraktion. → 3 Schema. | 035 ersetzen (z. B. „Welche Gleichung hat eine Scheinlösung, obwohl kein Bruch die Form (x + a)/(x − a) hat?“ mit vier Gleichungen, Hauptnenner nötig); 036 siehe A6. |
| A6 | 036 | Bestand `rollend-13` R8-V053: Graphen von x/(x − 2) und 2/(x − 2), „der Abstand der Graphen ist die Differenz ihrer Funktionswerte“, Aussage: keine Lösung, Scheinlösung 2. Gleiche Darstellung, gleiche Rechnung (Differenz konstant), gleiche Frage (gemeinsame Punkte / Lösungen). | Ersetzen, nicht mit Graphen-Differenz. |
| A7 | 025, 030, 035 | Dreimal dieselbe Schablone „immer – kann – nie – nur“, und jedes Mal ist die richtige Möglichkeit die einzige, deren Aussage kein Absolutwort trägt („können verschieden sein“, „können auch keine Lösung haben“, „können vorkommen“); alle Ablenker sagen „immer“, „nie“ oder „nur“. Das „können“ im Ablenker steht stets mit „nur“. Ein testkluges Kind löst alle drei ohne Mathematik. | Mindestens zwei der drei umbauen; in einer die richtige Aussage mit Absolutwort, z. B. 030 mit Zusatz a ≠ b, c ≠ d: richtig „Sie haben nie mehr als eine Lösung, denn x² fällt weg“ (geprüft: dann nur 0 oder 1 Lösung), Ablenker „immer genau eine“ (widerlegt durch 4 = 6) und „können zwei haben“. |

## Befunde B (Soll)

| Nr. | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| B1 | 027 (Test) | Rechnung vollständig: keine Lösung genau für a ∈ {0; 7} (a = 7: 0 · x = 49; a = 0: einziger Kandidat −5 verboten; sonst x = (2a + 35)/(a − 7), nie 2, nie −5). Grundmenge genannt, eindeutig. Aber: den Fall a = 0 findet man nur über (2a + 35)/(a − 7) = −5 oder den Blick auf 0/(x + 5) – das schaffen nur sehr starke Kinder in 3–4 Minuten; der Fall „Parameter macht den Kandidaten verboten“ ist zugleich der Kern von 033 (scheinloesung). | Als Test behalten; „genau zwei Zahlen“ bleibt als Hilfe. Überschneidung mit 033 durch A3 (033 nur ein Wert) mildern. |
| B2 | 023 und 026 | Dieselbe Denkfigur „Parameter im Nenner rückwärts aus D bestimmen“; 026 fügt nur die Grundmenge ℤ hinzu. definitionsmenge hat damit 4 verschiedene Denkfiguren (022, 023/026, 024, 025) – genug, aber knapp. | 026 ohne Rückwärts-Teil: „Wie viele ganze Zahlen schließt D von 5/(2x + 3) + 1/(x² − 6x) = 2 in ℤ aus, wie viele in ℚ?“ → [2; 3]. |
| B3 | 033 | `rollend-7` K8-V081: „Für welche Zahl a ist x = 3 bei (x + a)/(x − 3) = 7/(x − 3) eine Scheinlösung?“ – gleiche Frage; neu sind Hauptnenner durch Ausklammern und der zweite Wert. Gleiche Einsicht, etwas andere Rechnung. | Akzeptabel mit A3 (ein Wert); in `abgrenzung` K8-V081 nennen. |
| B4 | 034 | Bestand T 229 (x/(x − 2) = 2/(x − 2) + 3, L = { }) und T 222: gleiche Rechnung (Bruch + Zahl = Bruch mit gleichem Nenner, Kandidat = verbotene Zahl); neu ist nur die Einkleidung als Zahlenrätsel. Als Schema-Aufgabe ausgewiesen. | Als Schema-Platz zulässig, falls 035 und 036 ersetzt werden; sonst eigenen Kern. |
| B5 | 032 | Bestand T 224 ((x² − 1)/(x − 1) = 2, L = { } nach Kürzen) und BT 36 („Haben 1/(x − 2) und x/(x² − 2x) dieselbe Definitionsmenge?“ – derselbe Nenner x² − 2x). Gleiche Einsicht, andere Denkleistung (Schritt diagnostizieren) – darf bleiben, ist aber nahe. | In `abgrenzung` nennen; andere Nennerzahlen als x² − 2x. |
| B6 | Etiketten 024, 034, 038 | `einkleidung` + `form: bruecke` – eine Brücke ist laut Auftrag ein Darstellungswechsel (Anteil ↔ Prozent); Modell aufstellen ist `transfer`. Bei 034 hebt das Etikett eine offen gezählte Schema-Aufgabe über die Verstehens-Prüfung des Werkzeugs. | 024, 038: `typ: transfer`, `form: anwenden`; 034 ehrlich ohne Verstehens-Form (oder ersetzen). |
| B7 | 039, 040, 041 | 039 und 041 tragen dieselbe Denkfigur (Teil : Teil ↔ Teil : Ganzes); 040 ist Grenzfall (bekannte Regel der indirekten Proportionalität, hier nicht als Schema gezählt). verhaeltnis hat damit 4 Denkfiguren (037, 038, 039/041, 040). | 041 (Schema-Platz) durch eine andere Denkfigur ersetzen, z. B. Verhältnis dreier Größen aus zwei Verhältnissen mit Fehlvorstellung (vorher gegen den Bestand „gemeinsames Glied“ prüfen) oder Maßstab rückwärts. |

## Befunde C (Kann)

| Nr. | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| C1 | 026 | Grundmenge ℤ in M8 ungewöhnlich, aber zulässig; eindeutig (Skript: nur b = 6). | – |
| C2 | 030 | Ausmultiplizieren (x + a)(x + d) als M8-Stoff vorausgesetzt (Annahme, nicht am Lehrplantext belegt). Der Fall „unendlich viele Lösungen“ (a = b, c = d) kommt vor (Skript), wird im Lösungsweg nicht erwähnt. | In `w` ergänzen oder mit A7 a ≠ b, c ≠ d vorgeben. |
| C3 | 037 (Test) | obere Grenze für 3–4 Minuten; Fehlbild 125 beschreibt eine wenig wahrscheinliche Rechnung. | Fehlbild „Verhältniszahlen addiert: 1 : 1 + 1 : 4 = 2 : 5“ mit passender Menge ergänzen. |
| C4 | 036 | „zeichnet man die Graphen“ ohne Grafik. | Mit A6 erledigt. |
| C5 | 029 | Kehrwert-Weg wie `rollend-7` K8-V071 (dort Rechnen, hier Beurteilen) – andere Denkleistung, darf bleiben. Richtige Möglichkeit hat als einzige „hier“. | „hier“ auch in einen Ablenker. |
| C6 | 038 | Rechnerisch M6-Niveau (+ 4, · 10/6); als Korrektur vertretbar. | – |
| C7 | 024 | „welche Zahl muss x für die Sachaufgabe übertreffen“ ungelenk. | „x muss größer sein als □“. |

## Tabelle je Lernziel

| Lernziel | Test | Schema (streng, entschieden) | verschiedene Denkfiguren | Test ok? |
|---|---|---|---|---|
| definitionsmenge | 022 | keine (022, 026 Grenzfälle → nein) | 4: Umformung ändert D (022), Parameter rückwärts (023, 026), D gegen sinnvolle Werte im Modell (024), L legt D nicht fest (025) | nein: mehrdeutige Lücke (A1), Denkfigur wie Test 032 (A2) |
| ueber_kreuz | 027 | 028, 031 → **2** | 5: Fallunterscheidung (027), Zählerverhältnis (028), zwei Wege Kehrwert (029), x² fällt weg (030), wann direkt (031) | ja, aber nur für sehr starke Kinder (B1) |
| scheinloesung | 032 | 034, 035, 036 → **3** | 5 nominal: Kürzen (032), Scheinlösung bauen (033), Rätsel (034), Regel aus Beispielen (035), Graphen-Differenz (036) | nein: leichter als 033 (A3), Denkfigur wie 022 (A2) |
| verhaeltnis | 037 | 041 → 1 (040 Grenzfall → nein) | 4: Mischung (037), additiv/multiplikativ (038), Teil–Ganzes (039, 041), umgekehrtes Verhältnis (040) | ja |

Denkfiguren über die vier Tests: 022 und 032 gleich (A2); 027 berührt mit a = 0 den Kern von 033 (B1); 037 eigenständig.

## Schwierigkeit der Tests (Einschätzung)

| Test | Schafft ein gutes Kind der 8. Klasse das in 3–4 Minuten? | Was muss es verstanden haben? |
|---|---|---|
| 022 | Ja (etwa 3 Minuten), wenn (T) eindeutig ist. | Die Ausgangsgleichung lösen (x = 0) und sehen, dass ein neuer Nenner x genau diese Lösung verbietet; D gehört zur jeweiligen Gleichung. |
| 027 | Nur sehr starke Kinder; a = 7 finden die meisten, a = 0 wenige. | Über Kreuz mit Parameter, (a − 7)x = 2a + 35, Fall Koeffizient 0, dann den Kandidaten gegen D prüfen – zwei verschiedene Gründe für „keine Lösung“. |
| 032 | Ja, in 1–2 Minuten – zu leicht für den Test. | Kürzen mit x entfernt die Einschränkung x ≠ 0; Probe gehört in die Ausgangsgleichung. |
| 037 | Knapp, eher 4–5 Minuten. | Mit Mengen statt Verhältniszahlen rechnen: Saft- und Wasseranteil von B (1/5, 4/5) ansetzen, Verhältnisgleichung aufstellen. |

## Protokoll je Aufgabe

| Kennung | Pool | Rechnung (Skript) | Ablenker verboten / wörtlich wahr? | Schema? | Bestand | Weitere |
|---|---|---|---|---|---|---|
| 022 | Test | [0; 1] ok, aber (T) ungekürzt → 2 | – | nein (Grenzfall) | `gleichungen.linear` „Quadrieren: dieselbe Lösungsmenge?“ andere Einsicht | A1, A2 |
| 023 | K | 14, eindeutig | – | nein | T 33 anderer Kern | B2 |
| 024 | K | [2; 3; 9]; Breiten 9 und 6 cm positiv | – | nein | T 45/T 9 gleiche Einsicht, Modell neu | B6, C7 |
| 025 | S | Beispiele stimmen; nur Index 1 | nein / nein | nein | – | A7 |
| 026 | S | [6; 0], nur b = 6 | – | nein (Grenzfall) | T 47 anderer Kern | B2, C1 |
| 027 | Test | [0; 7], alle a geprüft | – | nein | T 225/K8-V081 gleiche Frageart, andere Rechnung | B1 |
| 028 | K | 6 (x₀ = −9,5), eindeutig | – | **ja** | T 131/T 134 Verfahren | A4 |
| 029 | K | x = 11 beide Wege; Index 3 | nein / nein | nein | K8-V071 (C5) | C5 |
| 030 | S | Index 0; Fälle 0, 1, unendlich kommen vor | nein / nein | nein | T 144 nur Lösen | A7, C2 |
| 031 | S | Index 2 | nein | **ja** (offen) | T 130 Einsicht | – |
| 032 | Test | L = { }, gekürzt {0}; Index 3 | nein / nein | nein | T 224, BT 36 (B5) | A2, A3 |
| 033 | K | [6; −2]; keine Lösung genau für c ∈ {−2; 6} | – | nein | K8-V081 (B3) | A3 |
| 034 | K | 0, Scheinlösung 4 | – | **ja** (offen) | T 229, T 222 (B4) | B6 |
| 035 | S | Beispiele 3 / 4 / 5 / −3 stimmen; Index 1 | nein / nein | **ja** (Wissen) | T 192/T 199 | A5, A7 |
| 036 | S | [−1; 0], Kandidat 3 | – | **ja** | R8-V053 (A6) | C4 |
| 037 | Test | 250 ml, einzig; Saft 150, Wasser 300 | – | nein | Mischungsvergleich `groessen.verhaeltnisse`, kein Kern | C3 |
| 038 | K | [13; 15] | – | nein | – | B6, C6 |
| 039 | K | 7 (1 : 7, Anteil 1/8) | – | nein | – | B7 |
| 040 | S | 4 : 3 für jede Strecke; Index 0 | nein / nein | Grenzfall → nein | `groessen.indirekt` Einsicht, kein Kern | B7 |
| 041 | S | 19 | – | **ja** (offen) | – | B7 |
