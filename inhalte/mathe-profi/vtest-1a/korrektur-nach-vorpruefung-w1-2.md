# Korrektur nach Vorprüfung W1, 2. Durchgang, Runde VT1A

Stand 29.11.2026. Ausgang: `vorpruefung-w1-2.md` (A 4, B 7, C 9). Geändert habe ich nur, was ein Befund verlangt. Die Kennungen bleiben gleich (VT1A-001 bis 055); in `ueberschlag` haben Test und eine Sicherung die Plätze getauscht.

Prüfläufe: `bauen.py` OK; `gegenrechnung.py` 55 Sollantworten, 0 Abweichungen; `tools/vorrat_pruefen.py` 0 Meldungen; `tools/vtest_pruefen.py --runde 1a` nur die 11 erwarteten Pool-Meldungen „2 statt 3“.

Für jede neue Aufgabe habe ich den Bestand der Etappe vorher gelesen; Bestandskern und Unterschied stehen in `bestandsvergleich.md`. Die Schema-Zählung der Vorprüfung ist übernommen: In jedem Lernziel gibt es genau eine Schema-Aufgabe, nie im Test.

## Befund → geschlossen wie

| Nr | geschlossen wie |
|---|---|
| A1 klammern | 025 ersetzt: Im Term (□ + 7) · 3 wird □ um 5 größer – um wie viel wächst der Wert? (15; □ unbekannt). Einziges Schema bleibt 023. |
| A2 termaufbau | 030 ersetzt: 20 − 8, die 8 durch 5 + 3 ersetzt, mit und ohne Klammer – welche Termart? Nichts ist auszurechnen, und die Denkfigur ist eine andere als bei 027. Einziges Schema bleibt 027. |
| A3 umkehraufgabe_mal | 045 ersetzt: Welche Art Gleichung (Mal oder Geteilt) kann ohne Lösung sein? (f). Einziges Schema bleibt 043. Denkfiguren: Teiler 041, Aufgabenfamilie 042, Geschichte 043, Abhängigkeit von a 044, Lösbarkeit Mal gegen Geteilt 045. Auch wenn man 041 und 045 zusammenzählt, sind es 4. 044 trägt jetzt den Typ `umkehr` (Stufe 2), weil die Sicherung je eine Stufe 2 und eine Stufe 3 braucht. |
| A4 ueberschlag | Die Stellenzahl-Aufgabe ist umgebaut und jetzt der Test (046): Bei 3 412 · 3 438 ergibt der grobe Überschlag 3 000 · 3 000 nur 7 Stellen; erst die Schranken 3 400² und 3 500² zeigen 8 Stellen. Einziges Schema bleibt 048. |
| Zählung 033, 038 | Beide als Schema eingetragen, jeweils die einzige ihres Lernziels. |
| B1 Kinderregel-Routine | Nur noch 4 Aufgaben in dieser Form, jede anders gebaut. 022: Regel erschließen, gefragt ist der Unterschied zum richtigen Ergebnis (3). 029: Regel wählen (unverändert). 039: der Fall, in dem die Regel zufällig stimmt (□ = 1). 047: Regel genannt, gefragt ist die größte mögliche Abweichung vom richtigen Runden (2 000). Umgestellt: 002 (Summe gleicher Potenzen → Hochzahl 32), 012 (Zehnerpotenzen zwischen 5 · 10³ und 5 · 10⁷ → 4), 042 (gleichwertige Gleichung zu 8 · x = □), 053 (20 € in Hefte zu 3 € und Stifte zu 2 € zerlegen → 3). Keine Zahlaufgabe hat mehr einen falschen Wert als Lösung. |
| B2 Zwillings-Ablenker | 005: alle vier Optionen gleich gebaut. 018: alle vier beginnen gleich. 023: zwei Paare (50 − 3 · 9 ∓ 2 und 50 − 3 · (9 ∓ 2)). 034: Der Zwilling sind jetzt zwei falsche Optionen. 038: zwei Paare. 055: zwei Paare (+12 … und −12 …). Neue feste Prüfung in `bauen.py`: Ein Paar mit gleichem Anfang (5 Wörter) oder nur einem anderen Wort darf die richtige Option nur enthalten, wenn es eine zweite solche Gruppe gibt. Dabei wurden auch 010, 040, 044, 045 entdoppelt. |
| B3 Test-Vorlage | 001 behält „Drei der vier …“. 036 ist jetzt eine Urteilsaufgabe: Welche Teilprodukte fehlen dem Kind bei 300 · 40 + 68 · 7? 046 ist jetzt eine Zahlaufgabe (Stellenzahl). Der frühere Test-Inhalt von 046 (wann entscheidet ein Überschlag sicher?) steht als Sicherung in 049. |
| B4/B7 Test 016 | Gefragt ist jetzt nach den überzähligen Faktoren 2 in 6⁶ (5), so wie vorgeschlagen. 018 hat den Ablenker 6⁵ nicht mehr; an seiner Stelle steht „Startzahl und Hochzahl vertauscht“ (5 · 2³). |
| B5 Test 031 | □ · 23 · △ = 4 600, beide größer als 5, keine endet auf 0, △ größer als □ → △ = 25. Es bleibt genau eine Zerlegung, Abzählen entfällt. Hinweis: Mit dem Vorschlag „beide größer als 5“ allein blieben zwei Paare (8 · 25 und 10 · 20); deshalb die Zusatzbedingung „endet nicht auf 0“. |
| B6 Test 021 | Die Anfangszahl ist unbekannt („eine Zahl, die größer als 10 000 ist“), − 4 800 + 650 gegen − (4 800 + 650) → 1 300. Schriftliches Ausrechnen geht nicht. |
| C1 | 004: Im Lösungsweg steht der Grund (jeder weitere Faktor verdoppelt mindestens). |
| C2 | 011: „größer als 7 · 10¹¹ (also nicht nur gleich groß)“. |
| C3, C4 | siehe Zählung 033, 038. |
| C5 | unverändert (jetzt 049). |
| C6 | 017: Anfangszahl natürlich, Verdopplung genau zur vollen Stunde, beides im Text. |
| C7 | unverändert (026 bleibt Test). |
| C8, C9 | unverändert. |

## Neue oder geänderte Kennungen

- **neu gebaut:** 002, 012, 016, 021, 025, 030, 031, 036, 042, 045, 046 (Test, umgebaut aus der früheren 049), 047, 053
- **geändert:**
  - Optionen oder Text: 004 (Lösungsweg), 005, 010, 011, 017, 018, 022 (Frage), 023, 034, 038, 039 (Frage), 040, 044, 055
  - nur Schema-Feld: 033
  - verschoben: 049 (Inhalt des früheren Tests 046)
