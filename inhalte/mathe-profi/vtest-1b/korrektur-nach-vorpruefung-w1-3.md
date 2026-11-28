# Korrektur nach Vorprüfung W1-3 – Einheit 20 `gleichungen.bruch`

Grundlage: `vorpruefung-w1-3.md` (Stand 1f365ffc). Geändert habe ich nur die unten genannten Punkte. Die anderen Einheiten sind byte-gleich, und `bauen.py`, `kern.py`, `tools/` und `readme_vorlage.md` sind unverändert. In der Vorrat-Datei hat sich nur das Feld `abgrenzung` von scheinloesung geändert, weil B4 das so verlangt.

| Nr. | geschlossen wie |
|---|---|
| A1 | In ueber_kreuz habe ich die Pools getauscht. Die Aufgabe mit beliebigen p und q ist jetzt der Test: VT1B-027, `typ: parameter`, Stufe 3. Die Aufgabe mit a = 7 und a = 14 ist jetzt Korrektur: VT1B-028, `typ: umkehr`, Stufe 2. Die Kennungen ergeben sich aus der Reihenfolge der Pools. |
| A2 | 035: Zeile 3 ist jetzt eine Behauptung, „…, also ist −3 eine Lösung der Gleichung“. Damit ist sie die erste falsche Aussage; die Rechnungen in Zeile 1 bis 3 stimmen. Der Lösungsweg und die Fehlbilder (Zeile 4, Zeile 1; Anzahl 1) sind angepasst. |
| B1 | 022: Der Satz mit der Lösung x = 0 ist gestrichen. Der Text beginnt jetzt mit „Gegeben ist die Gleichung … mit der Grundmenge ℚ“. |
| B2 | 035 hat jetzt den Nenner x² + 3x: 5/(x + 3) + 2/x = (x − 12)/(x² + 3x), Scheinlösung −3, Lösung [3; 0]. |
| B3 | 036: Den Ablenker mit dem Vorzeichenfehler in D habe ich ersetzt durch eine Fehlvorstellung über die Rolle der Bedingungen: „5x + 2 = c, wobei auch x = −2 und x = 0 als Lösungen gelten“. Die Folgerung ist falsch und kommt in keiner anderen Möglichkeit vor. |
| B4 | Die `abgrenzung` von scheinloesung nennt jetzt T 180, T 198, T 224 und K8-V081, dazu ein Nachtrag in `bestandsvergleich.md`. |
| B5 | 030: Die richtige Möglichkeit lautet jetzt „…, denn über Kreuz fällt x² weg, und die Bedingungen schließen aus, dass 0 = 0 übrig bleibt.“ Sie ist ähnlich lang wie die anderen Möglichkeiten (alle mit „denn“). |
| B6 | Die Etiketten bleiben vorerst unverändert. Sobald das Werkzeug `transfer` auch auf Stufe 2 zulässt und ein Kennzeichen für die eine Schema-Aufgabe je Lernziel kennt, sollen gesetzt werden: 024 `typ: transfer` (Form `anwenden`), 038 `typ: transfer` (Form `anwenden`), 034 das Schema-Kennzeichen. Bei 034 entfällt dann die Form `bruecke`, und als `typ` steht ehrlich `einkleidung`. Die anderen Schema-Aufgaben der Einheit sind 031 und 041; sie sollten dasselbe Kennzeichen bekommen. |

Prüfläufe:
- `bauen.py` endet mit OK; `vorrat_pruefen` meldet 0, es gibt keine Doppelungen.
- `tools/vtest_pruefen.py --runde 1b` meldet nur die vier Pool-Meldungen.
- `gegenrechnung.py` meldet 0 Abweichungen.
