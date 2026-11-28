# Vorprüfung W1, 3. Durchgang (gezielte Nachprüfung, Stand 48c90f32)

Geprüft wurden vollständig die neuen Aufgaben 002, 012, 016, 021, 025, 030, 031, 036, 042, 045, 046, 047, 053 und die geänderten 004, 005, 010, 011, 017, 018, 022, 023, 034, 038, 039, 040, 044, 049, 055.
Dazu die Gesamtsicht je Lernziel. Bestand wie bisher: themen (alle Pools), rollend-5, -11, -12, die R-Lernziele vertauschen und berechnen.
Rechenskript `vorpruefung_w1_rechnen.py` um den 3. Durchgang ergänzt (Aufzählen für Abzähl- und „für jede Zahl“-Aufgaben, Regelprüfung bei 022). Ergebnis: **0 Abweichungen**.

Nachgerechnet:
- 002: 4 · 2³⁰ = 2³², also 32.
- 012: 10⁴ bis 10⁷, also 4.
- 016: 6⁶ = 2⁶ · 3⁶ gegen 2 · 3⁶, also 5 Faktoren 2 mehr.
- 021: 1 300, für jede Startzahl über 10 000 gleich.
- 022: Die Regel ist eindeutig (Klammern weglassen, Punkt vor Strich); 23 − 20 = 3.
- 025: 15 für jedes □.
- 031: □ · △ = 200; unter allen Faktorpaaren bleibt nur 8 · 25, also △ = 25, eindeutig.
- 039: □ = 1 ist die einzige Lösung.
- 046: 3 400² = 11 560 000 und 3 500² = 12 250 000 haben beide 8 Stellen; genau 11 730 456.
- 047: 2 000 als größter Unterschied (z. B. 6 812 + 2 587).
- 053: genau 3 Paare (2 | 7), (4 | 4), (6 | 1).

Bauart: Es gibt keine Zwillings-Ablenker mehr (nur 034 hat noch ein einzelnes Paar mit gleichem Anfang, und die richtige Option gehört nicht dazu). Die Kinderregel kommt nur noch 4-mal vor (022, 029, 039, 047), jedes Mal anders formuliert und anders gefragt; das ist keine Routine mehr. „Drei der vier …“ steht nur noch in 001 (Test) und 049 (Sicherung).

## Urteil

| Einheit | bereit für die Gegenprüfung | Grund |
|---|---|---|
| zahlen.potenzen_basis | **nein** | A1: zehner hat 2 Schema (012 neu, 014). |
| zahlen.rechengesetze | **nein** | A2–A5: 2 Schema in termaufbau, verteilen, ueberschlag (dort ist der Test Schema) und sach. |

Befunde: **A 5, B 3, C 5.**

## Entscheidungen zu den gezielten Fragen

| Frage | Entscheidung |
|---|---|
| 025 (Zahl einsetzen und probieren) | **kein Schema.** Es ist keine Zahl gegeben, gefragt ist eine allgemeine Wirkung. Wer ein Beispiel wählt, muss die Klammer richtig auswerten und annehmen, dass es für jedes □ gilt. Das ist die Heuristik „Spezialfall untersuchen“, kein Routineverfahren. Dieselbe Regel gilt für Test 021. |
| 039 (□ = 1 probieren) | **Schema.** 1 ist der erste Wert, den jedes Kind probiert, und die Antwort ist ohne jede Einsicht erraten. Mit 038 hat verteilen damit 2 Schema (A4). |
| 053 (systematisches Probieren) | eindeutig (genau 3), aber **Schema**: 6 Heftzahlen durchprobieren, ein Rechengesetz braucht man nicht. Mit 055 hat sach damit 2 (A5). |
| 046 (3 412 · 3 438, Schranken) | **Schema, als Test ungeeignet.** Der Text schreibt das Verfahren vor („ein Überschlag sicher kleiner, einer sicher größer“); übrig bleibt 3 400 · 3 400 und 3 500 · 3 500 auszurechnen. Schriftliches Ausrechnen geht ebenfalls. Die Einsicht (grob runden täuscht) stellt nur der Lösungsweg her, nicht das Kind. |
| Denkfigur 041/045 | **eine Denkfigur** (Lösbarkeit: b muss in der Reihe von a stehen), siehe B1. |
| Denkfigur 002/003 | **eine Denkfigur** (mit der Basis malnehmen erhöht die Hochzahl), und 002 benutzt dieselbe Einsicht wie Test 001 (4 = 2 · 2), siehe B2. |
| Test 036 (beide Faktoren zerlegt) | für ein gutes Kind der 5. Klasse lösbar: 368 · 47 = 368 · 40 + 368 · 7, dann jeden Teil weiter zerlegen. Das Ausmultiplizieren zweier Summen ist eigentlich Stoff von M7; die Aufgabe ist als Transfer mit dem Rechteckbild noch vertretbar (C2). |
| Test 031 | eindeutig (siehe oben), verständlich, mit drei Bedingungen aber dicht gepackt (C3). In 2–3 Minuten lösbar: vertauschen, 4 600 : 23 = 200, die Zerlegungen von 200 durchgehen. |
| Test 016 | 5 stimmt. „einer richtigen Rechnung“ ist nicht eindeutig, siehe B3. In 1–2 Minuten lösbar; das Kind muss verstanden haben, dass 6⁶ sechsmal (2 · 3) heißt. |
| Test 021 | 1 300 stimmt und gilt für jede Zahl; kein Schema (wie 025). In 1–2 Minuten lösbar; die 650 wird abgezogen statt addiert. |
| Kinderregel jetzt 4-mal | keine Routine mehr (B1 aus dem 2. Durchgang erledigt). |

## Befunde

### A

| Nr | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| A1 | zehner: 012 (neu) und 014 | 012 ist ein bloßer Zahlenvergleich: 5 000 und 50 000 000 einordnen und die Zehnerpotenzen dazwischen zählen. Mit 014 sind es 2 Schema. | 012 mit einer Einsicht bauen, z. B. „Eine Zahl hat 8 Stellen. Zwischen welchen Zehnerpotenzen liegt sie sicher?“ (10⁷ ≤ z < 10⁸), oder 014 ersetzen. |
| A2 | termaufbau: 030 (neu) und 027 | 030 bestimmt die Termart zweier konkreter Terme: das Bestand-Format „Welche Art von Term ist …?“. Ablenker 1 ist die Fehlvorstellung aus rollend-5 („letzte Rechnung ist das Plus aus der Klammer“). | 030 ohne konkrete Termart-Bestimmung bauen, z. B. „Wo muss die Klammer in 20 − 5 + 3 · 2 stehen, damit der Term ein Produkt wird?“ (eindeutig machen) oder eine allgemeine Aussage prüfen lassen. |
| A3 | ueberschlag: Test 046 und 048 | Der Test ist Schema, weil das Verfahren im Text steht (siehe oben). Mit 048 sind es 2 Schema, und der Test darf nie Schema sein. | Den Hinweis auf die zwei Überschläge streichen und als Urteil fragen: „Lena überschlägt 3 000 · 3 000 = 9 000 000 und sagt: 7 Stellen. Welche Aussage stimmt?“ (4 Urteile). Oder 049 (sicher entscheiden) wieder zum Test machen und 046 als Sicherung. |
| A4 | verteilen: 039 und 038 | 039 wird durch den ersten Probierwert □ = 1 gelöst (siehe oben). Mit 038 (Term ↔ Text) sind es 2 Schema. | 039 fragen: „Wievielmal so groß ist das Ergebnis des Kindes bei 5 · (2 · 7) wie das richtige?“ (5). |
| A5 | sach (Rechengesetze): 053 (neu) und 055 | 053 ist systematisches Probieren über 6 Fälle, ohne Rechengesetz. Mit 055 sind es 2 Schema. | 053 ersetzen, mit einem Rechengesetz im Kern (z. B. Gesamtpreis zweier Einkäufe über Ausklammern vergleichen). |

### B

| Nr | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| B1 | 041 (Test) / 045 | Gleiche Einsicht: Eine Mal-Gleichung ist genau dann lösbar, wenn b in der Reihe von a steht. Der Lösungsweg von 045 spricht die Test-Einsicht aus. umkehraufgabe_mal hat damit nur genau 4 Denkfiguren. | 045 mit einer anderen Denkfigur bauen (z. B. Lösung bei verdoppeltem b und halbiertem a). |
| B2 | 001 (Test) / 002 / 003 | 002 und 003 haben dieselbe Denkfigur (mit der Basis malnehmen erhöht die Hochzahl). 002 benutzt außerdem 4 = 2 · 2 wie Test 001, Test und Korrektur liegen also bei derselben Einzelfrage. schreibweise hat nur genau 4 Denkfiguren. | 002 durch eine andere Denkfigur ersetzen (z. B. Potenz mit Hochzahl 1, oder 2¹⁰ und 10³ ohne Ausrechnen vergleichen). |
| B3 | 016 (Test) | „in einer richtigen Rechnung“ ist mehrdeutig: 2 · 729 oder 1 458 zeigen keine sechs Dreier und keine einzelne 2. | „… mehr als in der richtigen Rechnung 2 · 3 · 3 · 3 · 3 · 3 · 3“ schreiben. |

### C

| Nr | Kennung | Beleg / Vorschlag |
|---|---|---|
| C1 | 021, 025 | Auch durch ein selbst gewähltes Beispiel lösbar. Zulässig (siehe oben), aber im Lösungsweg die allgemeine Begründung zuerst nennen; das ist dort schon der Fall. |
| C2 | 036 | Zwei Summen miteinander malnehmen ist Stoff aus M7; als Transfer vertretbar. Ein Satz zum Rechteckbild im Fragetext würde schwächeren Kindern helfen, ohne die Lösung zu verraten. |
| C3 | 031 | Drei Bedingungen auf einmal (> 5, nicht auf 0, △ > □). Eindeutig und verständlich, aber dicht; „keine von beiden endet auf 0“ eventuell als „keine ist durch 10 teilbar“ lesen lassen. |
| C4 | 042 | Nahe an der Bestand-Umkehraufgabe („Welche Umkehraufgabe löst …“), jetzt allgemein mit □ und mit der anderen Geteilt-Form. Andere Leistung, darf bleiben. |
| C5 | 002 | Einsicht wie im vertauschen-Bonus „Wie oft passt 4¹⁹ in 2⁴⁰?“ (andere Etappe). |

## Schema und Gesamtsicht je Lernziel

| Lernziel | Schema | Denkfiguren | Test kein Schema und die anspruchsvollste | Test in 2–3 Minuten (gutes Kind) |
|---|---|---|---|---|
| schreibweise | 005 | 4 (002 = 003) | ja | ja |
| quadrat | 009 | 5 | ja | ja |
| zehner | **012, 014** | 5 | ja | ja |
| sach Potenzen | 018 | 5 | ja | ja (nach B3) |
| klammern | 023 | 5 | ja | ja |
| termaufbau | **027, 030** | 4 | ja | ja |
| vorteil | 033 | 4 | ja | ja |
| verteilen | **038, 039** | 5 | ja | ja, mit Lehrplan-Grenze (C2) |
| umkehraufgabe_mal | 043 | 4 (041 = 045) | ja | ja |
| ueberschlag | **046 (Test), 048** | 4 | **nein** | rechnerisch ja, aber Schema |
| sach Rechengesetze | **053, 055** | 4 | ja | ja |
