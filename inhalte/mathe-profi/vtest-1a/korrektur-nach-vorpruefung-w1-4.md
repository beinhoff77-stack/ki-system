# Korrektur nach Vorprüfung W1, 4. Durchgang, Runde VT1A

Stand 29.11.2026. Ausgang: `vorpruefung-w1-4.md` (A1, B1–B4, C1–C4). Geändert sind nur VT1A-012, 039, 045, 046 und 053; alle anderen Aufgaben sind unverändert, auch die Lage ihrer richtigen Antwort.

Prüfläufe:
- `bauen.py`: OK
- `gegenrechnung.py`: 55 Sollantworten, 0 Abweichungen
- `tools/vorrat_pruefen.py`: 0 Meldungen
- `tools/vtest_pruefen.py --runde 1a`: Auf diesem Zweig steht die Mindestmenge noch auf 3, darum kommen noch die 11 Pool-Meldungen „2 statt 3“; sonst keine Fehler.

| Befund | geschlossen wie |
|---|---|
| A1 053 | Neu nach dem Vorschlag der Vorprüfung, nachgerechnet: Mia kauft 8 Hefte zu je □ € und 8 Stifte zu je 3 €, Tom 8 Hefte zu je (□ + 1) € und 8 Stifte zu je 1 €. Welche Aussage stimmt? Richtig: „Mia zahlt 8 € mehr.“ Ablenker: Tom zahlt 8 € mehr (Richtung vertauscht), Mia zahlt 16 € mehr (nur die Stifte verglichen), hängt von □ ab. **Warum kein Schema:** □ ist beliebig, nichts ist durchzuprobieren; keine Ersparnis steht im Text; der Vergleich gelingt nur über 8 · (□ + 1) = 8 · □ + 8 (Verteilen), und 8 · □ kommt auf beiden Seiten vor. Bestand gelesen (sach, verteilen), kein gleicher Kern. |
| B1/B2 045 | Kein „Fast immer“ mehr, andere Optionen-Bauart als 004: Die Optionen beschreiben, wie sich x zu b verhält. Richtig: „Bei a = 1 ist x so groß wie b, bei jedem größeren a ist x kleiner.“ Der Lösungsweg nennt die Behauptung des Kindes falsch. |
| B3 012 | Der teilwahre Ablenker ist ersetzt durch „Sie ist kleiner als 9 · 10⁷ und mindestens 10⁷.“ Das ist eindeutig falsch, zum Beispiel für 95 000 000. Das Fehlbild nennt die zu kleine obere Grenze. |
| B4 046 | Die richtige Option nennt beide Schranken: „Schon 3 400 · 3 400 hat 8 Stellen, und 3 500 · 3 500 hat auch 8.“ |
| C1 039 | „(mindestens 1)“ ergänzt. |
| C2–C4 | ohne Änderung (laut Bericht vertretbar). |

Technisch:
- `kern.py`: `W(…, lage=…)` erlaubt eine feste Lage. 053 nutzt sie (Lage 0), damit die Lagen von 054 und 055 gleich bleiben.
- `gegenrechnung.py`: für die fünf Aufgaben angepasst.
