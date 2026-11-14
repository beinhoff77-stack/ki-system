# Postfach inhalte-rs (Paket Realschule)

Neueste Meldung oben.

## 2026-11-14 18:20 – FERTIG
Paket Realschule abgeschlossen: 10 Themen, 1 624 Aufgaben, alle mit `python3 -I tools/inhalt_pruefen.py` OK. Jede Zahl- und Lückenaufgabe wird beim Bauen gegen ihren Rechenausdruck `c` geprüft (Abbruch bei Abweichung). Je Lernkarte mindestens 10 Aufgaben selbst gelesen; dabei gefundene Fehler (Grammatik, fehlende Angaben, „+ 0“, „1x“) behoben.

| Thema | Klasse | Lernkarten | Aufgaben | mit Bild |
|---|---|---|---|---|
| abbildungen.determinanten2 | RS 7 | 6 | 168 | 34 |
| abbildungen.vektoren | RS 7 | 6 | 168 | 6 |
| daten.stichproben | RS 7 | 5 | 140 | 0 |
| funktionen.scharen | RS 8 | 6 | 168 | 13 |
| terme.quadratische_extreme | RS 8 | 5 | 140 | 0 |
| funktionen.transformation | RS 9 | 6 | 168 | 12 |
| gleichungen.reinquadratisch | RS 9 | 6 | 168 | 0 |
| gleichungen.wurzel | RS 9 | 6 | 168 | 0 |
| abbildungen.matrizen | RS 10, IB MYP 4 | 6 | 168 | 0 |
| funktionen.umkehr | RS 10, IB MYP 4 | 6 | 168 | 28 |

Getroffene Annahmen (stehen jeweils unter `offen` in der Datei):
- funktionen.scharen und funktionen.umkehr: Lehrplan-Feld leer → üblicher RS-Stoff (lineare Scharen RS 8; Umkehrbarkeit, Gerade, Parabelast, Exponential/Logarithmus RS 10).
- abbildungen.vektoren: Determinanten im eigenen Thema, Skalarprodukt (RS 10) ins Thema abbildungen.matrizen verschoben.
- funktionen.transformation: auf RS-9-Niveau (Normalparabel, Bildpunkte allgemeiner Graphen); RS-10-Teil (Exp/Log, Spiegelung an y = x) weggelassen, y = x steht in funktionen.umkehr.
- terme.quadratische_extreme: ohne Parabelgraphen (laut Umfang).
- abbildungen.matrizen: Parkettierungen und Spiegelung an beliebigen Ursprungsgeraden weggelassen.

App-Wünsche:
- Pfeilspitzen für Strecken im Koordinatensystem (Vektoren).
- 2×2-Matrixdarstellung im Text oder als Zeichnung; bis dahin zeilenweise (a  b; c  d), Lücken (□ □; □ □).

Technik: eigene Hilfsdatei `inhalte/generatoren/_rs.py` (Kopie der Klasse-9-Bausteine plus Nachrechnen beim Bauen, Ausgleich der Antwortposition, Vektor-/Vieleck-Helfer). Gerundete Wurzel-/Winkelwerte stehen als 12-stelliges Literal in `c`, weil der Prüfrechner keine Wurzel kennt; `toleranz` ist gesetzt. Kein App-Code, keine Datenbank, kein Merge.

## 2026-11-14 18:00 – STATUS
Thema 9/10 fertig: `abbildungen.matrizen` – 6 Lernkarten, 168 Aufgaben, Prüfskript OK. Matrizen zeilenweise als (a  b; c  d), Lücken (□ □; □ □).
- FRAGE / App-Wunsch: echte 2×2-Matrixdarstellung (Klammer mit zwei Zeilen) im Aufgabentext oder als Zeichnung. Annahme bis dahin: zeilenweise Schreibweise mit Strichpunkt, in jeder Lernkarte erklärt.

## 2026-11-14 17:40 – STATUS
Thema 8/10 fertig: `gleichungen.wurzel` – 6 Lernkarten, 168 Aufgaben, Prüfskript OK. Inklusive √(x + b) = x + c mit Scheinlösung (nutzt quadratische Gleichungen aus RS 9).

## 2026-11-14 17:25 – STATUS
Thema 7/10 fertig: `gleichungen.reinquadratisch` – 6 Lernkarten, 168 Aufgaben, Prüfskript OK. Gerundete Wurzeln mit `toleranz`; Rechenausdruck enthält den Wurzelwert als 12-stelliges Literal (der Prüfrechner kennt keine Wurzel).

## 2026-11-14 17:10 – STATUS
Thema 6/10 fertig: `funktionen.transformation` – 6 Lernkarten, 168 Aufgaben, Prüfskript OK. Gebaut auf RS-9-Niveau (Normalparabel + Bildpunkte allgemeiner Graphen); RS-10-Teil (Exp/Log, Spiegelung an y = x) weggelassen, siehe `offen`.

## 2026-11-14 16:50 – STATUS
Thema 5/10 fertig: `terme.quadratische_extreme` – 5 Lernkarten, 140 Aufgaben, Prüfskript OK. Ohne Parabelgraphen (laut Umfang), Extremwerte über quadratische Ergänzung, Optimierung (Rechteck, Mauer, Zahlen, Preis).

## 2026-11-14 16:30 – STATUS
Thema 4/10 fertig: `funktionen.scharen` – 6 Lernkarten, 168 Aufgaben, Prüfskript OK. Lehrplan-Feld war leer: Annahme „Scharen linearer Funktionen (RS 8)“, unter `offen` notiert.

## 2026-11-14 16:10 – STATUS
Thema 3/10 fertig: `daten.stichproben` – 5 Lernkarten, 140 Aufgaben, Prüfskript OK. Überwiegend Verstehensaufgaben (Auswahl aus typischen Fehlurteilen); Hochrechnung als üblicher Schulstoff ergänzt (unter `offen` notiert).

## 2026-11-14 15:55 – STATUS
Thema 2/10 fertig: `abbildungen.vektoren` – 6 Lernkarten, 168 Aufgaben, Prüfskript OK. Skalarprodukt (RS 10) weggelassen, Determinanten im eigenen Thema; siehe `offen`.

## 2026-11-14 15:40 – STATUS
Thema 1/10 fertig: `abbildungen.determinanten2` – 6 Lernkarten, 168 Aufgaben, Prüfskript OK, alle Zahl-Aufgaben nachgerechnet.
- App-Wunsch: Pfeilspitzen für Strecken im Koordinatensystem (Vektoren). Bis dahin erscheinen Vektoren als Strecken.
