# Vorprüfung W1, 4. Durchgang (letzte Nachprüfung, Stand f21e6bd7)

Geprüft wurden nur die geänderten Aufgaben 002, 012, 016, 030, 039, 045, 046 und 053, jede vollständig, dazu die Gesamtsicht der betroffenen Lernziele. Bestand wie bisher (themen alle Pools, rollend-5, -11, -12).
Das Rechenskript `vorpruefung_w1_rechnen.py` ist um diese acht Aufgaben ergänzt; die allgemeinen Aussagen werden über Aufzählen geprüft (002, 012, 039, 045, 053), 030 von Hand mit Gegenbeispielen. Ergebnis: **0 Abweichungen**.

## Urteil

| Einheit | bereit für die Gegenprüfung | Grund |
|---|---|---|
| zahlen.potenzen_basis | **ja** | Kein A-Befund. Vor dem Einspielen B3 (012) beheben. |
| zahlen.rechengesetze | **nein** | A1: sach (Rechengesetze) hat 2 Schema (053, 055). |

Befunde: **A 1, B 4, C 4.**

## Je Aufgabe

| Kennung | Nachrechnung / Wahrheit der Optionen | Schema | Bestand | Urteil |
|---|---|---|---|---|
| 002 | Ungerade Basis ergibt bei jeder Hochzahl (auch 0: 3⁰ = 1) eine ungerade Zahl, für alle Basen bis 39 und Hochzahlen bis 11 aufgezählt. Option 0 ist wahr, die Optionen 1–3 sind falsch, keine ist teilwahr. | nein | Parität bei Quadratzahlen im themen-Bonus (andere Etappe) | ok; Klasse 5 in 1 Minute (ungerade · ungerade = ungerade). Neue Denkfigur, schreibweise hat jetzt 5. |
| 012 | Richtig ist: mindestens 10⁷ und kleiner als 10⁸. Option 0 („größer als 10⁷ und höchstens 10⁸“) ist für jede achtstellige Zahl außer 10⁷ wahr, und ihre zweite Hälfte („höchstens 10⁸“) ist sogar immer wahr. | nein | „Wie viele Ziffern hat 10¹⁰⁰ − 1“ (themen-Bonus): gleiche Einsicht, andere Leistung | **B3** |
| 016 | 5 (6⁶ = 2⁶ · 3⁶ gegen 2 · 3⁶). Mit der genannten richtigen Rechnung jetzt eindeutig. | nein | – | ok; Test in 1–2 Minuten |
| 030 | Option 3 ((Term) · 2 ist immer ein Produkt) ist wahr. Gegenbeispiele zu den anderen: 2 · 3 + 4; 20 − 5 + 3 gegen 20 − (5 + 3); 7 + 3 · 5. | nein | themen „Stimmt die Aussage? Jeder Term mit einer Klammer ist ein Produkt“: gleiche Einsicht, andere Leistung | ok; C3 |
| 039 | Das Kind hat □ · 2 · □ · 7, also □-mal so viel, für jedes □ ≥ 1. „doppelt“ und „14-mal“ gelten nur für □ = 2 bzw. 14, als allgemeine Aussage also falsch. | nein | – | ok; C1 |
| 045 | x = b : a ist kleiner als b genau dann, wenn a ≥ 2; bei a = 1 ist x = b (aufgezählt). Option 0 ist inhaltlich wahr, die anderen sind falsch. Die Grundmenge ist genannt (a, b mindestens 1), damit sind a = 0 und b = 0 ausgeschlossen. | nein | – | **B1, B2** |
| 046 | 7, 6 und „nicht entscheidbar“ sind falsch, 8 ist richtig (genau 11 730 456). Die vier Urteile sind trennscharf. Die richtige Begründung nennt aber nur eine Untergrenze (3 400 · 3 400 hat 8 Stellen, also mindestens 8). | nein, Grenzfall: schriftlich ausrechnen geht, dauert in Klasse 5 aber über 3 Minuten | – | **B4**; Test in 2–3 Minuten (34 · 34 = 1 156, dann die Nullen) |
| 053 | 16 €, für jeden Heftpreis gleich (aufgezählt). Eindeutig. | **ja**: Jedes Päckchen spart 2 €, 8 · 2 = 16. Ein Schritt; □ und Ausklammern braucht man nicht. | – | **A1** |

## Befunde

### A

| Nr | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| A1 | 053; sach (Rechengesetze) | Gelöst wird in einem Schritt (Ersparnis je Päckchen mal 8); das Rechengesetz wird nicht gebraucht. Mit 055 sind es 2 Schema. | Ein Verteilen mit □ erzwingen, z. B. „Mia kauft 8 Hefte zu □ € und 8 Stifte zu 3 €. Tom kauft 8 Hefte, die je 1 € mehr kosten, und 8 Stifte zu je 1 €. Wer zahlt mehr, und um wie viel?“ Dort ist 8 · (□ + 1) + 8 · 1 = 8 · □ + 16 gegen 8 · □ + 24, also zahlt Mia 8 € mehr. |

### B

| Nr | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| B1 | 004, 045 | Neues Bauart- und Routine-Muster: „Fast immer“ kommt nur in diesen beiden Aufgaben vor und ist beide Male die richtige Option (2 von 2, in keinem Ablenker). Beide haben dieselbe Vorlage (Behauptung „… immer …“; Optionen „Immer: / Fast immer: … / Nie: / Bei … nicht/ja“). | 045 anders bauen (z. B. als Zahl: „Für welches a ist x = b?“ oder mit vier Gleichungen). Oder „Fast immer“ in einer weiteren Aufgabe als Ablenker verwenden. |
| B2 | 045 | „Fast immer“ ist hier nicht sauber: Die Ausnahme a = 1 umfasst unendlich viele Gleichungen (1 · x = b für jedes b), also kein Einzelfall wie 2² in 004. Die Behauptung des Kindes ist schlicht falsch. | „Nicht immer: Bei a = 1 ist x so groß wie b, sonst ist x kleiner.“ |
| B3 | 012 | Ablenker 0 ist teilwahr: „höchstens 10⁸“ stimmt für jede achtstellige Zahl, „größer als 10⁷“ scheitert nur an der einen Zahl 10⁷. Die Fehlbild-Beschreibung (10⁸ habe schon 9 Stellen) trifft den falschen Teil. | Ablenker 0 ersetzen, z. B. „Sie ist mindestens 10⁷ und kleiner als 9 · 10⁷“ (falsch für alle Zahlen ab 90 000 000), mit passendem Fehlbild. |
| B4 | 046 (Test) | Die richtige Begründung trägt nur „mindestens 8 Stellen“. Dass es nicht 9 sind, steht nicht da (Obergrenze 3 500 · 3 500 oder: zwei vierstellige Zahlen ergeben höchstens 8 Stellen). | „…, und schon 3 400 · 3 400 hat 8 Stellen, 3 500 · 3 500 auch.“ |

### C

| Nr | Kennung | Beleg / Vorschlag |
|---|---|---|
| C1 | 039 | „beliebige natürliche Zahl □“: mit „(mindestens 1)“ ergänzen, weil bei □ = 0 beide Ergebnisse 0 sind und „□-mal so groß“ keinen Sinn hat. |
| C2 | 046 | Schriftlich ausrechnen ist möglich (4 · 4 Stellen), dauert aber deutlich länger als die Einsicht; als Test vertretbar. |
| C3 | 028 / 030 | Nahe Denkfiguren (welche Änderung macht einen Term zum Produkt). termaufbau hat trotzdem 4 verschiedene (026, 027, 028/030, 029). |
| C4 | Aussage-Aufgaben | Mit 002, 004, 012, 030, 045 (und 010, 015, 020, 024, 054) gibt es jetzt viele Aussagen der Art „Welche Aussage stimmt (für jede …)?“. Außer B1 kein Bauart-Merkmal: „immer“ steht in 7 von 38 richtigen und 10 von 114 falschen Optionen, „nie“ in 1 richtigen und 6 falschen, Einschränkungen (nur/sonst/außer) in 3 richtigen und 7 falschen, „mindestens/höchstens“ in 1 richtigen und 3 falschen. |

## Gesamtsicht der betroffenen Lernziele

| Lernziel | Schema | Denkfiguren | Test kein Schema und die anspruchsvollste | ok? |
|---|---|---|---|---|
| schreibweise | 005 | 5 | 001 ja | ja |
| zehner | 014 | 5 | 011 ja | ja (B3) |
| sach Potenzen | 018 | 5 | 016 ja | ja |
| termaufbau | 027 | 4 | 026 ja | ja |
| verteilen | 038 | 5 | 036 ja | ja |
| umkehraufgabe_mal | 043 | 5 | 041 ja | ja (B1, B2) |
| ueberschlag | 048 | 4 | 046 ja | ja (B4) |
| sach Rechengesetze | **053, 055** | 4 | 051 ja | **nein** (A1) |

Schema in den übrigen Lernzielen, unverändert seit dem 3. Durchgang: quadrat 009, klammern 023, vorteil 033.
