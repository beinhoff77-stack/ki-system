# Postfach potenz-teilen (Sechsundzwanzigste Runde: Potenzgesetze in zwei eigene Flüge teilen)

Neueste Meldung oben. Zeiten: Ortszeit Adelaide (UTC+10:30).

## 2026-11-20 22:50 – FERTIG: Potenzgesetze geteilt

Zweig `potenz-teilen` (von `lernen-app`, e71a72d). Commits: Flug A 56cbd40 · Flug B 1e14734 · Themenliste und Texte c13e59d · dieser Bericht. Nichts in die Datenbank geschrieben, kein App-Code, kein Merge, keine Kinderdaten, keine Schulbuchaufgaben.

### Kurz
- **Flug A `terme.potenzgesetze_natuerlich`** (thema_id 102, block_id 62 Samarkand, Gym 7 · RS 7 · MYP 4): die vier Lernkarten aus `terme.umformen` mit **unveränderten Lernziel-Schlüsseln** (`mal_gleiche_basis`, `gleicher_exponent` Pflicht; `geteilt_gleiche_basis`, `anwenden` Vertiefung). Karten (Erklärungen) Zeichen für Zeichen wie bisher. 191 Aufgaben.
- **Flug B `terme.potenzgesetze_ganzzahlig`** (thema_id 103, block_id 60 Mumbai, Gym 8 · RS 7 · MYP 4): neu, 5 Lernkarten (`warum_gilt`, `gleiche_basis_ganz`, `exponent_und_potenz`, `terme_vereinfachen` Pflicht; `fehler_ganz` Vertiefung), Erklärungen nach der Vorgabe vom 16.11. (eine Algenfläche, die sich täglich verdoppelt, als durchgehende Situation). 175 Aufgaben.
- **`terme.umformen`:** die vier Karten (168 Aufgaben) entfallen; die übrigen 8 Karten und ihre 273 Aufgaben sind Zeichen für Zeichen gleich (im Generator geprüft). Ziel und Merke angepasst.
- **`terme.potenzgesetze` (Gym 6):** „Fehler finden“ nur noch zu Potenzbegriff, Hoch 0 und negativem Exponenten; 23 Aufgaben nach Flug A, 14 neu gebaut, Karte neu erklärt. Titel in der Themenliste „Potenzen und negative Exponenten“.
- **Themenliste:** zwei neue Einträge, Reihenfolgen nachgezogen; Selbstprüfung lückenlos und eindeutig (unten). **kann-Texte:** zwei neue Dateien, `terme.umformen` ohne die vier Lernziele, `terme.potenzgesetze` ein Text angeglichen.
- `python3 -I tools/inhalt_pruefen.py --alle`: **118 × OK**, Rückgabewert 0 (vorher 116). Ohne Hinweise zu den Karten der neuen und geänderten Flüge; „gleich gebaut hintereinander“ überall 0.

### Abweichungen vom Auftrag (bitte ansehen)
1. **29 statt 22 Aufgaben nach Flug B.** 22 haben einen negativen Exponenten im Text (wie gezählt). 7 weitere haben ihn im Ergebnis: Das Gesetz liefert aᵐ⁻ⁿ mit m < n (z. B. „3⁴ : 3⁸ = 3ᵏ“, k = −4). Das ist M8-4-Stoff, deshalb auch nach Flug B und in Flug A ersetzt. Zwei weitere Aufgaben gehen auch ohne negativen Exponenten; dort habe ich nur Lösungsweg und Tipp neu geschrieben (Frage und Lösung gleich).
2. **23 statt 19 Aufgaben aus Gym 6 nach Flug A.** Maßgeblich war die Regel der Entscheidung („In Gym 6 bleiben nur Aufgaben zu Potenzbegriff, Hoch 0 und negativem Exponenten“). Vermutlich nicht mitgezählt waren: „Welche Rechnung ist richtig?“ (3² · 3⁴ …), die Parameter-Aufgabe zu „a² · a³ = a⁶“, die Rückwärts-Aufgabe zu aᵏ · a² und die Knobel-Aufgabe 2⁵ + 2⁵. Keine der 23 hat einen negativen Exponenten im Text; nach Flug B ging deshalb keine.
3. **Alle 23 sind jetzt Übungen Stufe 3 vom Typ „fehler“**, wie verlangt – auch die früheren Test-, Korrektur-, Sicherungs- und Knobel-Aufgaben (8 davon bekamen einen Tipp, Übungen brauchen einen). Folge: In `mal_gleiche_basis` hat Stufe 3 jetzt 22 Übungen, davon 15 „fehler“, darunter leichte wie „Stimmt die Rechnung? 4⁴ · 4² = 4⁶“. Das Prüfskript ist zufrieden (je Typ und Satzbau höchstens 2), die Regel „Stufe 3 je Typ höchstens 3“ aus `_bereinigen` gilt hier nur je Satzbau. **Für Sebastian:** Sollen die vier „Stimmt die Rechnung? …“-Aufgaben lieber Stufe 1 „erkennen“ werden?
4. **Antworten geändert, ohne Frage und richtige Antwort zu ändern:** In 4 umgezogenen Aufgaben (Flug A) stand eine falsche Antwort mit negativem Exponenten („Ein negativer Exponent bedeutet Kehrbruch …“). Sie ist durch einen typischen Fehler mit natürlichen Exponenten ersetzt. In Gym 6 nannten 5 bleibende Aufgaben Potenzgesetze als falsche Antworten („Exponenten subtrahieren, nicht teilen: 4⁸“). Die sind durch typische Fehler beim negativen Exponenten ersetzt („Richtig wäre −12, denn man rechnet 4 · (−3)“, „Richtig wäre 1/12“). Dazu zwei Lösungswege bzw. Tipps in Gym 6 ohne Potenzgesetz.
5. **Themenliste `terme.potenzgesetze`:** Neben Titel, `umfang` und dem dritten Eintrag habe ich auch den **zweiten** Eintrag von `lehrplan_gym` geändert („Potenzen mit gleicher Basis oder gleichem natürlichen Exponenten zusammenfassen“ war ebenfalls ein Gesetzes-Versprechen) sowie `lehrplan_rs` und `lehrplan_ib` (beide nannten Potenzgesetze). Neu: „Potenzen mit rationaler Basis und natürlichen Exponenten berechnen“ (M6 1.4, laut `inhalte/pruefung/aufbau/klasse6.json`), „Typische Fehler bei Potenzen mit einer Zahlenprobe erkennen (Vertiefung)“.
6. **Flug B: Stufe und Typ der 29 übernommenen Aufgaben angepasst** (Text, Antworten, Lösung gleich). Zweierprodukte und -quotienten wie „z³ · z⁻⁵ = zᵏ“ sind in diesem Flug die Grundform → Stufe 1 „direkt“; Dreierprodukte und die Dezimal-Aufgaben → Stufe 2 „mehrschritt“. Test-, Korrektur- und Sicherungsaufgaben blieben in ihrem Pool. Darum hat `gleiche_basis_ganz` 4 Korrektur- und 10 Sicherungsaufgaben.

### Zählung je Flug, Karte, Pool und Stufe

**terme.potenzgesetze_natuerlich** (thema_id 102, block_id 62, klasse {'gym_by': 7, 'rs_by': 7, 'ib_myp': 4}) – 191 Aufgaben

| Lernkarte | P/V | Übung S1 | Übung S2 | Übung S3 | davon ohne Typ | Knobel | Test | Korrektur | Sicherung | zusammen |
|---|---|---|---|---|---|---|---|---|---|---|
| mal_gleiche_basis | P | 9 | 13 | 22 | 0 | 2 | 1 | 3 | 6 | 56 |
| gleicher_exponent | P | 10 | 12 | 11 | 2 | 2 | 1 | 3 | 6 | 45 |
| geteilt_gleiche_basis | V | 7 | 16 | 13 | 0 | 2 | 1 | 3 | 6 | 48 |
| anwenden | V | 7 | 14 | 9 | 0 | 2 | 1 | 3 | 6 | 42 |

**terme.potenzgesetze_ganzzahlig** (thema_id 103, block_id 60, klasse {'gym_by': 8, 'rs_by': 7, 'ib_myp': 4}) – 175 Aufgaben

| Lernkarte | P/V | Übung S1 | Übung S2 | Übung S3 | davon ohne Typ | Knobel | Test | Korrektur | Sicherung | zusammen |
|---|---|---|---|---|---|---|---|---|---|---|
| warum_gilt | P | 5 | 8 | 9 | 0 | 2 | 1 | 3 | 6 | 34 |
| gleiche_basis_ganz | P | 9 | 9 | 8 | 0 | 2 | 1 | 4 | 10 | 43 |
| exponent_und_potenz | P | 6 | 8 | 8 | 0 | 2 | 1 | 3 | 6 | 34 |
| terme_vereinfachen | P | 5 | 7 | 8 | 0 | 2 | 1 | 3 | 6 | 32 |
| fehler_ganz | V | 5 | 6 | 9 | 0 | 2 | 1 | 3 | 6 | 32 |

**terme.potenzgesetze** (thema_id 30, block_id 44, klasse {'gym_by': 6, 'rs_by': 7, 'ib_myp': 3}) – 109 Aufgaben

| Lernkarte | P/V | Übung S1 | Übung S2 | Übung S3 | davon ohne Typ | Knobel | Test | Korrektur | Sicherung | zusammen |
|---|---|---|---|---|---|---|---|---|---|---|
| potenz_begriff | P | 8 | 11 | 8 | 0 | 2 | 1 | 3 | 6 | 39 |
| negativer_exponent | P | 5 | 13 | 8 | 0 | 2 | 1 | 3 | 6 | 38 |
| fehler_finden | V | 4 | 8 | 8 | 0 | 2 | 1 | 3 | 6 | 32 |

**terme.umformen** (thema_id 29, block_id 62, klasse {'gym_by': 7}) – 273 Aufgaben

| Lernkarte | P/V | Übung S1 | Übung S2 | Übung S3 | davon ohne Typ | Knobel | Test | Korrektur | Sicherung | zusammen |
|---|---|---|---|---|---|---|---|---|---|---|
| zusammenfassen | P | 5 | 7 | 8 | 0 | 2 | 1 | 3 | 6 | 32 |
| produkte | P | 5 | 7 | 8 | 1 | 2 | 1 | 3 | 6 | 32 |
| minusklammer | P | 6 | 9 | 8 | 0 | 2 | 1 | 3 | 6 | 35 |
| ausmultiplizieren | P | 6 | 10 | 8 | 2 | 2 | 1 | 3 | 6 | 36 |
| summe_mal_summe | P | 6 | 9 | 8 | 3 | 2 | 1 | 3 | 6 | 35 |
| ausklammern | P | 6 | 8 | 8 | 4 | 2 | 1 | 3 | 6 | 34 |
| aequivalenz | P | 10 | 6 | 8 | 4 | 2 | 1 | 3 | 6 | 36 |
| binomisch | P | 6 | 7 | 8 | 2 | 2 | 1 | 3 | 6 | 33 |

`terme.umformen`: unverändert gegenüber vorher, nur die vier Karten fehlen (vorher 12 Karten, 441 Aufgaben).

### Was wohin umgezogen ist (alt → neu)
**1. terme.umformen → Flug B (29 Aufgaben; Text, Antworten, Lösung gleich)**

| Fragetext | vorher (Karte, Pool, Stufe/Typ) | nachher in Flug B |
|---|---|---|
| z³ · z⁻⁵ = zᵏ. Wie groß ist k? | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| y⁻³ · y⁻¹ = yᵏ. Wie groß ist k? | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| 10⁻¹ · 10⁵ · 10² = 10ᵏ. Wie groß ist k? | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 2/mehrschritt |
| 3⁻² · 3⁻³ · 3⁻¹ = 3ᵏ. Wie groß ist k? | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 2/mehrschritt |
| Berechne 10⁶ · 10⁻⁸ und gib das Ergebnis als Dezimalzahl an. | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 2/mehrschritt |
| Berechne 10² · 10⁻⁸ und gib das Ergebnis als Dezimalzahl an. | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 2/mehrschritt |
| 3⁴ · 3⁻⁶ = 3ᵏ. Wie groß ist k? | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| b³ · b⁻⁵ = bᵏ. Wie groß ist k? | mal_gleiche_basis, Korrektur, 2/– | gleiche_basis_ganz, Korrektur, 2/– |
| a³ · a⁻⁵ = aᵏ. Wie groß ist k? | mal_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| 10³ · 10⁻² · 10⁵ = 10ᵏ. Wie groß ist k? | mal_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| b⁻³ · b⁻¹ = bᵏ. Wie groß ist k? | mal_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| b⁻³ · b⁻⁵ = bᵏ. Wie groß ist k? | mal_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| a⁻² · a⁻² = aᵏ. Wie groß ist k? | mal_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| Berechne geschickt: 2⁻¹ · 5⁻¹ und gib das Ergebnis als Dezimalzahl an. | gleicher_exponent, Übung, 2/mehrschritt | exponent_und_potenz, Übung, 2/mehrschritt |
| Berechne geschickt: 5⁻¹ · 20⁻¹ und gib das Ergebnis als Dezimalzahl an. | gleicher_exponent, Übung, 2/mehrschritt | exponent_und_potenz, Übung, 2/mehrschritt |
| a⁻³ : a³ = aᵏ. Wie groß ist k? | geteilt_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| 3⁴ : 3⁸ = 3ᵏ. Wie groß ist k? | geteilt_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| z⁻² : z⁵ = zᵏ. Wie groß ist k? | geteilt_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| 2¹ : 2⁷ = 2ᵏ. Wie groß ist k? | geteilt_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| Berechne 10¹ : 10⁶ und gib das Ergebnis als Dezimalzahl an. | geteilt_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 2/mehrschritt |
| b⁻² : b⁶ = bᵏ. Wie groß ist k? | geteilt_gleiche_basis, Test, 2/– | gleiche_basis_ganz, Test, 2/– |
| 5⁴ : 5⁶ = 5ᵏ. Wie groß ist k? | geteilt_gleiche_basis, Korrektur, 2/– | gleiche_basis_ganz, Korrektur, 2/– |
| 2¹ : 2⁸ = 2ᵏ. Wie groß ist k? | geteilt_gleiche_basis, Korrektur, 2/– | gleiche_basis_ganz, Korrektur, 2/– |
| y¹ : y⁻² = yᵏ. Wie groß ist k? | geteilt_gleiche_basis, Korrektur, 2/– | gleiche_basis_ganz, Korrektur, 2/– |
| y⁴ : y⁶ = yᵏ. Wie groß ist k? | geteilt_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| a⁻³ : a⁴ = aᵏ. Wie groß ist k? | geteilt_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| y⁷ : y⁻⁴ = yᵏ. Wie groß ist k? | geteilt_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| 10¹ : 10⁹ = 10ᵏ. Wie groß ist k? | geteilt_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| x⁻⁴ : x⁷ = xᵏ. Wie groß ist k? | geteilt_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |

**2. Ersatz in Flug A (an derselben Stelle, gleicher Pool, gleiche Stufe, gleicher Typ)**

| Karte | alt (→ Flug B) | neu |
|---|---|---|
| mal_gleiche_basis | z³ · z⁻⁵ = zᵏ. Wie groß ist k? | x⁴ · x² · x³ = xᵏ. Wie groß ist k? |
| mal_gleiche_basis | y⁻³ · y⁻¹ = yᵏ. Wie groß ist k? | b² · b⁵ · b = bᵏ. Wie groß ist k? |
| mal_gleiche_basis | 10⁻¹ · 10⁵ · 10² = 10ᵏ. Wie groß ist k? | 10³ · 10 · 10⁴ = 10ᵏ. Wie groß ist k? |
| mal_gleiche_basis | 3⁻² · 3⁻³ · 3⁻¹ = 3ᵏ. Wie groß ist k? | 2² · 2³ · 2⁴ = 2ᵏ. Wie groß ist k? |
| mal_gleiche_basis | Berechne 10⁶ · 10⁻⁸ und gib das Ergebnis als Dezimalzahl an. | Berechne 10² · 10⁴ mit dem Potenzgesetz. Gib das Ergebnis als Zahl an. |
| mal_gleiche_basis | Berechne 10² · 10⁻⁸ und gib das Ergebnis als Dezimalzahl an. | Berechne 3² · 3² · 3 mit dem Potenzgesetz. Gib das Ergebnis als Zahl an. |
| mal_gleiche_basis | 3⁴ · 3⁻⁶ = 3ᵏ. Wie groß ist k? | 4³ · 4 · 4² = 4ᵏ. Wie groß ist k? |
| mal_gleiche_basis | b³ · b⁻⁵ = bᵏ. Wie groß ist k? | b⁴ · b³ = bᵏ. Wie groß ist k? |
| mal_gleiche_basis | a³ · a⁻⁵ = aᵏ. Wie groß ist k? | a² · a⁷ = aᵏ. Wie groß ist k? |
| mal_gleiche_basis | 10³ · 10⁻² · 10⁵ = 10ᵏ. Wie groß ist k? | 10² · 10³ · 10⁴ = 10ᵏ. Wie groß ist k? |
| mal_gleiche_basis | b⁻³ · b⁻¹ = bᵏ. Wie groß ist k? | b⁴ · b · b² = bᵏ. Wie groß ist k? |
| mal_gleiche_basis | b⁻³ · b⁻⁵ = bᵏ. Wie groß ist k? | x³ · x⁵ = xᵏ. Wie groß ist k? |
| mal_gleiche_basis | a⁻² · a⁻² = aᵏ. Wie groß ist k? | y⁶ · y⁶ = yᵏ. Wie groß ist k? |
| gleicher_exponent | Berechne geschickt: 2⁻¹ · 5⁻¹ und gib das Ergebnis als Dezimalzahl an. | Berechne geschickt: 0,2⁵ · 50⁵ |
| gleicher_exponent | Berechne geschickt: 5⁻¹ · 20⁻¹ und gib das Ergebnis als Dezimalzahl an. | Berechne geschickt: 2,5² · 4² · 10² |
| geteilt_gleiche_basis | a⁻³ : a³ = aᵏ. Wie groß ist k? | z⁹ : z² : z³ = zᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | 3⁴ : 3⁸ = 3ᵏ. Wie groß ist k? | a⁶ · a⁴ : a⁷ = aᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | z⁻² : z⁵ = zᵏ. Wie groß ist k? | 2⁴ · 2⁵ : 2⁶ = 2ᵉ. Wie groß ist e? |
| geteilt_gleiche_basis | 2¹ : 2⁷ = 2ᵏ. Wie groß ist k? | Berechne 10⁷ : 10³. Gib das Ergebnis als Zahl an. |
| geteilt_gleiche_basis | Berechne 10¹ : 10⁶ und gib das Ergebnis als Dezimalzahl an. | x¹² : x⁵ : x⁴ = xᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | b⁻² : b⁶ = bᵏ. Wie groß ist k? | b⁹ : b³ = bᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | 5⁴ : 5⁶ = 5ᵏ. Wie groß ist k? | 5⁸ : 5³ = 5ᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | 2¹ : 2⁸ = 2ᵏ. Wie groß ist k? | 2⁹ : 2² = 2ᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | y¹ : y⁻² = yᵏ. Wie groß ist k? | y⁷ : y = yᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | y⁴ : y⁶ = yᵏ. Wie groß ist k? | y⁸ : y⁵ = yᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | a⁻³ : a⁴ = aᵏ. Wie groß ist k? | a¹⁰ : a⁴ = aᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | y⁷ : y⁻⁴ = yᵏ. Wie groß ist k? | x⁹ : x² = xᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | 10¹ : 10⁹ = 10ᵏ. Wie groß ist k? | 10⁹ : 10⁵ = 10ᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | x⁻⁴ : x⁷ = xᵏ. Wie groß ist k? | b¹¹ : b³ = bᵏ. Wie groß ist k? |

Nur Lösungsweg und Tipp neu (ohne negativen Exponenten): „2¹⁰ : 2ⁿ = 1/4. Wie groß ist n?“ (geteilt_gleiche_basis); „Berechne 10⁴ : 10⁴ : 10⁴ · 10⁸.“ (geteilt_gleiche_basis).

**3. terme.potenzgesetze/fehler_finden → Flug A (23 Aufgaben, alle als Übung Stufe 3 „fehler“)**

| Fragetext | vorher (Pool, Stufe/Typ) | nachher (Karte) |
|---|---|---|
| Stimmt die Rechnung? 5² · 5² = 5⁴ | Übung, 1/erkennen | mal_gleiche_basis |
| Ein Kind rechnet: 3⁹ : 3³ = 3³. Welcher Satz beschreibt den Fehler richtig? | Übung, 2/mehrschritt | geteilt_gleiche_basis |
| Stimmt die Rechnung? 4⁵ : 4² = 4³ | Übung, 2/mehrschritt | geteilt_gleiche_basis |
| Stimmt die Rechnung? 4⁴ · 4² = 4⁶ | Übung, 1/erkennen | mal_gleiche_basis |
| Stimmt die Rechnung? 2⁴ · 2³ = 2⁷ | Übung, 1/erkennen | mal_gleiche_basis |
| Ein Kind rechnet: 2² · 5² = 10⁴. Was ist falsch? | Übung, 2/mehrschritt | gleicher_exponent |
| Ein Kind rechnet: 2³ · 5³ = 10⁶. Was ist falsch? | Übung, 2/mehrschritt | gleicher_exponent |
| Ein Kind rechnet: 3³ · 3³ = 9⁶. Welcher Satz beschreibt den Fehler richtig? | Übung, 3/fehler | mal_gleiche_basis |
| Ein Kind rechnet: 4³ · 4² = 16⁵. Welcher Satz beschreibt den Fehler richtig? | Übung, 2/mehrschritt | mal_gleiche_basis |
| Stimmt die Rechnung? 5² · 5³ = 5⁶ | Test, 2/– | mal_gleiche_basis |
| Ein Kind rechnet: 3⁴ · 3⁴ = 9⁸. Was ist falsch? | Korrektur, 2/– | mal_gleiche_basis |
| Ein Kind rechnet: 2⁴ · 5⁴ = 10⁸. Was ist falsch? | Korrektur, 2/– | gleicher_exponent |
| Stimmt die Rechnung? 4⁷ : 4⁴ = 4³ | Sicherung, 2/– | geteilt_gleiche_basis |
| Stimmt die Rechnung? 5⁵ : 5² = 5³ | Sicherung, 2/– | geteilt_gleiche_basis |
| Ein Kind rechnet: 4⁴ · 4² = 4⁸. Was ist falsch? | Sicherung, 2/– | mal_gleiche_basis |
| Ein Kind rechnet: 5⁴ · 5⁴ = 5¹⁶. Was ist falsch? | Sicherung, 2/– | mal_gleiche_basis |
| Ein Kind rechnet: 5⁶ : 5² = 5³. Was ist falsch? | Sicherung, 2/– | geteilt_gleiche_basis |
| Ein Kind rechnet: 4³ · 4³ = 4⁹. Welcher Satz beschreibt den Fehler richtig? | Übung, 3/fehler | mal_gleiche_basis |
| Ein Kind rechnet: 4⁴ · 4² = 16⁶. Welcher Satz beschreibt den Fehler richtig? | Übung, 2/mehrschritt | mal_gleiche_basis |
| Welche Rechnung ist richtig? | Übung, 3/begruenden | anwenden |
| Die Regel „a² · a³ = a⁶“ ist falsch. Für welche Zahlen a stimmt sie trotzdem? | Übung, 3/parameter | mal_gleiche_basis |
| Ein Kind hat bei aᵏ · a² die Exponenten malgenommen und a¹² erhalten. Was wäre der richtige Exponent gewesen? | Übung, 3/rueckwaerts | mal_gleiche_basis |
| Ein Kind schreibt 2⁵ + 2⁵ = 2¹⁰. Richtig ist 2ᵏ. Wie groß ist k? | Knobel, 3/knobel | mal_gleiche_basis |

Antwortlisten geändert (eine falsche Antwort mit negativem Exponenten durch einen typischen Fehler mit natürlichen Exponenten ersetzt; Frage und richtige Antwort gleich): „Ein Kind rechnet: 2² · 5² = 10⁴. Was ist falsch?“; „Ein Kind rechnet: 4⁴ · 4² = 4⁸. Was ist falsch?“; „Ein Kind rechnet: 5⁴ · 5⁴ = 5¹⁶. Was ist falsch?“; „Ein Kind rechnet: 5⁶ : 5² = 5³. Was ist falsch?“.

**4. terme.potenzgesetze (Gym 6), fehler_finden: neu (14)**

- Übung, Stufe 3, fehler: Ein Kind rechnet 3⁻² = −9. Wie heißt das richtige Ergebnis?
- Übung, Stufe 3, fehler: Ein Kind rechnet (2/3)² = 4/3. Wie heißt das richtige Ergebnis?
- Übung, Stufe 3, rueckwaerts: Ein Kind sollte 2ⁿ ausrechnen. Es hat aus Versehen 2 · n gerechnet und 10 erhalten. Welches Ergebnis wäre richtig gewesen?
- Übung, Stufe 3, parameter: Für wie viele natürliche Zahlen n von 1 bis 10 ist (−2)ⁿ negativ?
- Übung, Stufe 3, transfer: In einem Datenblatt steht: Dicke 10⁻³ m. Ein Kind meint, das sei eine negative Dicke. Wie viele Millimeter sind 10⁻³ m wirklich?
- Knobel, Stufe 3, knobel: Ein Kind behauptet: (−1)¹⁰⁰ + (−1)¹⁰¹ + 1⁻¹⁰⁰ = 3. Was kommt wirklich heraus?
- Test, Stufe 2: Ein Kind rechnet: 10⁻² = −100. Was ist falsch?
- Korrektur, Stufe 2: Ein Kind rechnet 0,3² = 0,9. Wie heißt das richtige Ergebnis?
- Korrektur, Stufe 2: Stimmt die Rechnung? 7⁰ = 7
- Sicherung, Stufe 2: Ein Kind rechnet 2⁻⁴ = −16. Wie heißt das richtige Ergebnis als Dezimalzahl?
- Sicherung, Stufe 2: Ein Kind rechnet (−3)² = −9. Wie heißt das richtige Ergebnis?
- Sicherung, Stufe 2: Ein Kind rechnet 4³ = 12. Wie heißt das richtige Ergebnis?
- Sicherung, Stufe 2: Stimmt die Rechnung? (−2)³ = −8
- Sicherung, Stufe 2: Ein Kind rechnet −2⁴ = 16. Wie heißt das richtige Ergebnis?

Antwortlisten ohne Potenzgesetze (je 2 falsche Antworten ersetzt, Frage und richtige Antwort gleich): „Ein Kind rechnet: 4⁻³ = −64. Was ist falsch?“; „Ein Kind rechnet: 4⁻⁴ = −256. Was ist falsch?“; „Ein Kind rechnet: 5⁻⁴ = −625. Was ist falsch?“; „Ein Kind rechnet: 5⁻² = −25. Was ist falsch?“; „Ein Kind rechnet: 2⁻³ = −8. Was ist falsch?“.
Nur Lösungsweg bzw. Tipp neu: „Wie viel Mal so groß ist 2² wie 2⁻²?“ (negativer_exponent, w); „Ein Kind rechnet 2³ + 2³ = 2⁶. Welche Zahl ist richtig?“ (fehler_finden, h).

### Einordnung (Themenliste)
| | Flug A | Flug B |
|---|---|---|
| `reihenfolge.gym_by` | 2 (Kl. 7: ab `terme.umformen` alles +1) | 8 (Kl. 8: ab `gleichungen.bruch` alles +1) |
| `reihenfolge.rs_by` | 2 (Kl. 7, hinter `terme.potenzgesetze`) | 3 (direkt hinter A, vor `zahlen.potenzen_zehner`; ab dort alles +2) |
| `reihenfolge.ib_myp` | 1 (MYP 4, alles +2) | 2 |
| `lernbereich` | Gym „M7 1 Terme mit Variablen“ · RS „M7 1 Potenzen“ · IB „MYP 4 Numerical and abstract reasoning (Zahl und Algebra)“ | Gym „M8 4 Bruchterme und Bruchgleichungen“ · RS „M7 1 Potenzen“ · IB wie A |

- **Belegt:** Gym M7 1.2 („Produkte von Potenzen mit natürlichen Exponenten (bei gleicher Basis oder gleichem Exponenten) … zusammenfassen“, auch „Potenzen von Potenzen“); Gym M8 4 („machen die Rechengesetze für Potenzen mit ganzzahligen Exponenten plausibel und wenden diese in einfachen Fällen an“); RS M7 1 Potenzen enthält negative Exponenten und Potenzgesetze; IB: Potenzgesetze mit ganzzahligen/negativen Exponenten = MYP 4–5 Standard.
- **Annahme (so gekennzeichnet):** die Aufteilung der RS-Potenzgesetze auf zwei Flüge und ihre Nummern 2/3 (der Lehrplan gibt die Reihenfolge innerhalb eines Lernbereichs nicht vor); IB-Nummern 1/2 (das MYP gibt keine Reihenfolge vor); IB-Stufe für Flug A und den neuen IB-Text von `terme.potenzgesetze`.
- Selbstprüfung (Skript `inhalte/generatoren/_potenz_teilen_liste.py`, Ausgabe unverändert):
```
Themenliste: schon nachgezogen, nur Prüfung
gym_by  Kl.  5: 14 Themen · Nummern 1–14 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
gym_by  Kl.  6: 11 Themen · Nummern 1–11 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: NEIN (3 Überschriften)
gym_by  Kl.  7: 10 Themen · Nummern 1–10 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (5 Überschriften)
gym_by  Kl.  8: 15 Themen · Nummern 1–15 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (7 Überschriften)
gym_by  Kl.  9: 14 Themen · Nummern 1–14 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (7 Überschriften)
gym_by  Kl. 10:  9 Themen · Nummern 1–9 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (5 Überschriften)
rs_by   Kl.  5: 12 Themen · Nummern 1–12 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (6 Überschriften)
rs_by   Kl.  6: 11 Themen · Nummern 1–11 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (6 Überschriften)
rs_by   Kl.  7: 20 Themen · Nummern 1–20 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (7 Überschriften)
rs_by   Kl.  8:  7 Themen · Nummern 1–7 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
rs_by   Kl.  9: 17 Themen · Nummern 1–17 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (8 Überschriften)
rs_by   Kl. 10: 11 Themen · Nummern 1–11 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (5 Überschriften)
ib_myp  Kl.  1: 15 Themen · Nummern 1–15 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (3 Überschriften)
ib_myp  Kl.  2: 12 Themen · Nummern 1–12 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (3 Überschriften)
ib_myp  Kl.  3: 12 Themen · Nummern 1–12 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
ib_myp  Kl.  4: 29 Themen · Nummern 1–29 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
ib_myp  Kl.  5: 18 Themen · Nummern 1–18 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
terme.potenzgesetze_natuerlich: kurz 91 Zeichen, 4 Etappen, längster kann-Text 75 Zeichen
terme.potenzgesetze_ganzzahlig: kurz 98 Zeichen, 5 Etappen, längster kann-Text 86 Zeichen
terme.umformen: kurz 92 Zeichen, 8 Etappen, längster kann-Text 90 Zeichen
terme.potenzgesetze: kurz 85 Zeichen, 3 Etappen, längster kann-Text 84 Zeichen
Selbstprüfung: OK
```
  Gym 6 „Lernbereiche zusammenhängend: NEIN“ ist der bekannte Befund aus LB-4 (nicht Teil dieses Auftrags, unverändert).
- **Lehrplan-Quellen:** LehrplanPLUS Gymnasium 7 und 8 (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik · …/gymnasium/8/mathematik, Abschnitte M7 1.2 und M8 4), Realschule 7 Gruppe I (…/realschule/7/mathematik/wpfg1, M7 1), IB MYP Mathematics guide 2020 (Framework S. 23–29) – **alle abgerufen am 20.11.2026 durch den Chat `lehrplan-lb`** (Postfach `lehrplan-lb.md`, Abschnitt „Quellen“; Zitat M8 4 dort im Auftragsentwurf; Zitat M7 1.2 in `inhalte/pruefung/aufbau/klasse6.json`). **Ich habe die Seiten nicht selbst geöffnet:** Die Abruf-Freigabe wurde in diesem Chat nicht beantwortet.

### Texte für die Abschluss-Ansichten (`inhalte/kann/`)
- `terme.potenzgesetze_natuerlich.json`: kurz „Du lernst, Potenzen mit gleicher Basis oder gleichem Exponenten geschickt zusammenzufassen.“ (91 Zeichen); die vier kann-Texte unverändert aus `terme.umformen`.
- `terme.potenzgesetze_ganzzahlig.json`: kurz 98 Zeichen, 5 kann-Texte (höchstens 86 Zeichen).
- `terme.umformen.json`: die vier Lernziele gestrichen. `terme.potenzgesetze.json`: `fehler_finden` an den neuen Inhalt angeglichen („Fehler bei Potenzen und negativen Exponenten finden und mit einer Zahlenprobe prüfen“).
- Selbstprüfung: jede Etappe genau ein Eintrag, keine überzähligen, Längen eingehalten, gültiges JSON (siehe Ausgabe oben).

### Nachgerechnet
- Jede Aufgabe mit Zahl- oder Lücken-Lösung wird beim Bauen gegen ihr `c` gerechnet (Generator) und vom Prüfskript noch einmal.
- **Unabhängig von `c`:** Ein eigenes Skript übersetzt die Terme aus dem Fragetext und setzt die Lösung ein (Variablen mit zwei verschiedenen Zahlen belegt): 202 Aufgaben der vier Flüge automatisch, 0 Fehler.
- **Von Hand:** alle 122 übrigen neuen Aufgaben (Sachaufgaben, Auswahl, Muster) einzeln gelesen und nachgerechnet, dazu die geänderten Antwortlisten (richtige Antwort weiter richtig, ersetzte falsche Antworten wirklich falsch). Einen unglücklichen Satz habe ich dabei umformuliert.

### Für den Haupt-Chat
- **Lernstand umhängen:** Die vier Lernziele haben in Flug A dieselben Schlüssel. Achtung: 29 Aufgaben, die bisher zu diesen Karten in Thema 29 gehörten, stehen jetzt in Thema 103 (Liste 1). 29 Aufgaben in Flug A sind neu (Liste 2). Die 23 Aufgaben aus Thema 30 haben jetzt eine andere Karte, einen anderen Pool, Stufe 3 und Typ „fehler“ (Liste 3).
- Expeditionen verweisen auf keine der betroffenen Lernkarten (per Skript geprüft).
- `terme.umformen` behält in der Themendatei `klasse` nur `gym_by` (unverändert). Der `lehrplan_rs`-Text von `terme.umformen` („… auch mit Potenzgesetzen …“) ist unverändert. Er könnte Wortlaut des RS-Lernbereichs M7 6 sein; nicht geprüft.

### Offen / nicht geprüft
- **M7 1.2 „Potenzen von Potenzen“** hat in Flug A keine Karte (in Flug B: `exponent_und_potenz`). Vorschlag: eigene Karte in Flug A – Sebastian entscheidet. Steht auch unter `offen` in der Themendatei.
- Nicht in der App angesehen: Tabellen als Kartenbild und in einer Aufgabe, Lücken „c = □; n = □“ (Flug B, `terme_vereinfachen`).
- Alte, unveränderte Aufgaben nur über `c` und das Prüfskript nachgerechnet, nicht von Hand.
- Lehrplantexte nicht selbst gelesen (siehe Quellen).

## 2026-11-20 22:41 – STATUS
Flug B `terme.potenzgesetze_ganzzahlig` gebaut, Prüfskript OK (Commit 1e14734). Weiter mit Themenliste und Texten.

## 2026-11-20 22:40 – STATUS
Flug A `terme.potenzgesetze_natuerlich`, `terme.umformen` und `terme.potenzgesetze` umgebaut, Prüfskript OK (Commit 56cbd40). Weiter mit Flug B.
