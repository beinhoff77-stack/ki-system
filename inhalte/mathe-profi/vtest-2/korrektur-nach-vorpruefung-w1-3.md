# Korrektur nach der dritten Vorprüfung Welle 1 (Runde 2)

Stand 29.11.2026, Zweig `schreiber-w1-r2` (mit `vorpruefer-w1-r2-3`, `366d7d84`, zusammengeführt). Grundlage: `vorpruefung-w1-3.md` (2 A, 3 B, 3 C). Nur diese Punkte umgesetzt, sonst nichts geändert.

| Befund | geschlossen wie |
|---|---|
| A1 strahl_eintragen: Test nicht die anspruchsvollste | Pools getauscht: VT2-098 (zwei Teilungen bis 12 000, gemeinsame Striche alle 600) ist Test, Stufe 3, typ transfer; VT2-095 (Maßstab umgekehrt) ist Sicherung, Stufe 2, typ umkehr. Kennungen unverändert. |
| A2 minusklammer: 038 durch Auflisten lösbar | Zahlen a ≠ b von 1 bis 20 statt 1 bis 5: 38 verschiedene Werte (1 bis 39 ohne 20), größter 39 (alle 380 Paare nachgerechnet). Fehlbilder 380, 39, 19 bzw. 1, −1. |
| B1 112, 117: Gegenbeispiel nur in der richtigen Möglichkeit | Beide jetzt ohne Beispiel in jeder Möglichkeit: 112 „… wenn ein neues Zeichen gebraucht wird, kann eine Schreibweise auch kürzer werden“, 117 „… für den Wert zählt, an welchen Stellen die Einsen stehen, und nicht, wie viele es sind“. Das Gegenbeispiel muss das Kind selbst finden; es steht nur im Lösungsweg und in den Fehlbildern. |
| B2 110 verrät 112 | Beispiel in 112 (Lösungsweg, Fehlbilder) ist jetzt XIV → XV, III → IV, IV → V; die Neun aus dem Lösungsweg von 110 kommt nicht mehr vor. |
| B3 097 Voraussetzung | „eine Zahl, die auf einem Strich liegt (nicht die 0)“ im Text. |
| C1, C2 | kein Handlungsbedarf (vom Prüfer als vertretbar bzw. zulässig eingestuft). |
| C3 040 | Frage lautet jetzt „Welche Zählweise passt zum Aufbau ihres Terms?“. |

Sonst nichts berührt; geändert wurden nur `th_natuerlich.py`, `th_umformen.py`, die beiden JSON-Dateien, `gegenrechnung.py` (Prüfzeilen für 038 und 112) und `sonderfaelle.md`.
