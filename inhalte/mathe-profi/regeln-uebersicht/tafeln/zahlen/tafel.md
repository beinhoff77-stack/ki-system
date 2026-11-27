# Zahlen zum Nachschlagen – Tafel

Quadrat-, Kubik-, Zweier- und Zehnerpotenzen, Primzahlen und Teilbarkeitsregeln.

Stand 2026-11-27. Entwurf: nichts ist in die App eingespielt; geprüft mit `../pruefen.py`. Spalte „ab“ = frühester Beleg im Bestand (Gym = Gymnasium Bayern, RS = Realschule Bayern, IB = IB MYP); „Regel“ = passende Kennung im Regel-Universum.

## Quadratzahlen

n² heißt n · n: die Zahl mal sich selbst.

0² = 0; 1² = 1; 2² = 4; 3² = 9; 4² = 16; 5² = 25; 6² = 36; 7² = 49; 8² = 64; 9² = 81; 10² = 100; 11² = 121; 12² = 144; 13² = 169; 14² = 196; 15² = 225; 16² = 256; 17² = 289; 18² = 324; 19² = 361; 20² = 400; 25² = 625

Trick: Endet die Zahl auf 5, rechne: Zehnerziffer z mal (z + 1), dahinter 25. Beispiel 35²: 3 · 4 = 12, dahinter 25 ergibt 1 225.

## Kubikzahlen

n³ heißt n · n · n: die Zahl dreimal malnehmen.

0³ = 0; 1³ = 1; 2³ = 8; 3³ = 27; 4³ = 64; 5³ = 125; 6³ = 216; 7³ = 343; 8³ = 512; 9³ = 729; 10³ = 1 000

## Zweierpotenzen

Von einer Zweierpotenz zur nächsten verdoppelt sich der Wert; 2⁰ ist 1.

2⁰ = 1; 2¹ = 2; 2² = 4; 2³ = 8; 2⁴ = 16; 2⁵ = 32; 2⁶ = 64; 2⁷ = 128; 2⁸ = 256; 2⁹ = 512; 2¹⁰ = 1 024

## Zehnerpotenzen

| Potenz | Zahl | Name |
|---|---|---|
| 10⁰ | 1 | Eins |
| 10¹ | 10 | Zehn |
| 10² | 100 | Hundert |
| 10³ | 1 000 | Tausend |
| 10⁴ | 10 000 | Zehntausend |
| 10⁵ | 100 000 | Hunderttausend |
| 10⁶ | 1 000 000 | Million |
| 10⁷ | 10 000 000 | Zehn Millionen |
| 10⁸ | 100 000 000 | Hundert Millionen |
| 10⁹ | 1 000 000 000 | Milliarde |
| 10¹⁰ | 10 000 000 000 | Zehn Milliarden |
| 10¹¹ | 100 000 000 000 | Hundert Milliarden |
| 10¹² | 1 000 000 000 000 | Billion |

Kleine Zehnerpotenzen:

| Potenz | Zahl | Name |
|---|---|---|
| 10⁻¹ | 0,1 | Zehntel |
| 10⁻² | 0,01 | Hundertstel |
| 10⁻³ | 0,001 | Tausendstel |
| 10⁻⁴ | 0,0001 | Zehntausendstel |
| 10⁻⁵ | 0,00001 | Hunderttausendstel |
| 10⁻⁶ | 0,000001 | Millionstel |

## Primzahlen bis 100

Eine Primzahl hat genau zwei Teiler: 1 und sich selbst. Die 1 ist keine Primzahl; die 2 ist die einzige gerade.

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 (25 Zahlen)

Test: Für eine Zahl von 2 bis 100: Ist es 2, 3, 5 oder 7, ist sie prim. Sonst teile sie einzeln durch 2, 3, 5 und 7. Geht keine Division ohne Rest auf, ist sie eine Primzahl. Eine zusammengesetzte Zahl bis 100 hat einen Teiler von höchstens 7, denn 11 · 11 = 121 ist schon größer als 100. Für 97 reicht es sogar bis √97, das ist knapp unter 10: 9 · 9 = 81 und 10 · 10 = 100. Die Primteiler bis dahin sind 2, 3, 5 und 7.

- 91 ist nicht durch 2, 3, 5 teilbar, aber 7 · 13 = 91. Also keine Primzahl.
- 97 : 2 ist 48 Rest 1; 97 : 3 ist 32 Rest 1; 97 : 5 ist 19 Rest 2; 97 : 7 ist 13 Rest 6. Kein Rest ist 0, weitere Primteiler bis √97 gibt es nicht: Primzahl.

## Teilbarkeitsregeln

| Kennung | Teilbar durch | Regel | Ja-Beispiel | Nein-Beispiel | ab |
|---|---|---|---|---|---|
| zz-07 | 2 | Sieh nur die letzte Ziffer an. Ist sie 0, 2, 4, 6 oder 8, ist die Zahl durch 2 teilbar. | 7 314: Letzte Ziffer 4: gerade, also durch 2 teilbar. | 7 315: Letzte Ziffer 5: ungerade, also nicht durch 2 teilbar. | Gym 5 · RS 5 · IB 1 |
| zz-08 | 3 | Zähle alle Ziffern zusammen (Quersumme). Ist die Quersumme durch 3 teilbar, dann auch die Zahl. | 5 214: Quersumme: 5 + 2 + 1 + 4 = 12; 12 : 3 = 4, also durch 3 teilbar. | 5 215: Quersumme: 5 + 2 + 1 + 5 = 13; 13 ist nicht durch 3 teilbar, also die Zahl auch nicht. | Gym 5 · RS 5 · IB 1 |
| zz-09 | 4 | Sieh die letzten zwei Ziffern als Zahl an. Ist sie durch 4 teilbar (auch 00), dann auch die ganze Zahl. | 3 124: Letzte zwei Ziffern: 24; 24 : 4 = 6, also durch 4 teilbar. | 3 126: Letzte zwei Ziffern: 26; 4 · 6 = 24 und 4 · 7 = 28, also nicht durch 4 teilbar. | ohne Beleg |
| zz-10 | 5 | Sieh nur die letzte Ziffer an. Ist sie 0 oder 5, ist die Zahl durch 5 teilbar. | 1 235: Letzte Ziffer 5: durch 5 teilbar. | 1 236: Letzte Ziffer 6: nicht durch 5 teilbar. | Gym 5 · RS 5 · IB 1 |
| zz-11 | 6 | Prüfe beides: Die Zahl muss durch 2 und durch 3 teilbar sein (gerade und Quersumme durch 3). | 4 218: Letzte Ziffer 8: gerade. Quersumme: 4 + 2 + 1 + 8 = 15; 15 : 3 = 5. Beides stimmt: durch 6 teilbar. | 4 216: Letzte Ziffer 6: gerade. Quersumme: 4 + 2 + 1 + 6 = 13; 13 ist nicht durch 3 teilbar. Es stimmt nur eins von beiden: nicht durch 6 teilbar. | ohne Beleg |
| zz-12 | 8 | Sieh die letzten drei Ziffern als Zahl an. Ist sie durch 8 teilbar (auch 000), dann auch die ganze Zahl. | 5 128: Letzte drei Ziffern: 128; 128 : 8 = 16, also durch 8 teilbar. | 5 124: Letzte drei Ziffern: 124; 8 · 15 = 120 und 8 · 16 = 128, also nicht durch 8 teilbar. | ohne Beleg |
| zz-13 | 9 | Zähle alle Ziffern zusammen (Quersumme). Ist die Quersumme durch 9 teilbar, dann auch die Zahl. | 6 345: Quersumme: 6 + 3 + 4 + 5 = 18; 18 : 9 = 2, also durch 9 teilbar. | 6 346: Quersumme: 6 + 3 + 4 + 6 = 19; 19 ist nicht durch 9 teilbar, also die Zahl auch nicht. | Gym 5 · RS 5 · IB 1 |
| zz-14 | 10 | Sieh nur die letzte Ziffer an. Ist sie 0, ist die Zahl durch 10 teilbar. | 8 560: Letzte Ziffer 0: durch 10 teilbar. | 8 565: Letzte Ziffer 5: nicht durch 10 teilbar (aber durch 5). | Gym 5 · RS 5 · IB 1 |
| zz-15 | 25 | Sieh die letzten zwei Ziffern an. Sind es 00, 25, 50 oder 75, ist die Zahl durch 25 teilbar. | 3 675: Letzte zwei Ziffern: 75; 25 · 3 = 75, also durch 25 teilbar. | 3 665: Letzte zwei Ziffern: 65; 25 · 2 = 50 und 25 · 3 = 75, also nicht durch 25 teilbar. | ohne Beleg |

## Belege und Regeln

| Kennung | Eintrag | ab | Regel |
|---|---|---|---|
| zz-01 | Quadratzahlen bis 20² (und 25²) | Gym 5 · RS 5 · IB 1 | Z15 |
| zz-02 | Kubikzahlen bis 10³ | Gym 5 · RS 5 · IB 1 | R8 |
| zz-03 | Zweierpotenzen 2⁰ bis 2¹⁰ | Gym 5 · RS 5 · IB 1 | R8, Z3 |
| zz-04 | Zehnerpotenzen 10⁰ bis 10¹² mit Namen | Gym 5 · RS 5 · IB 1 | Z18 |
| zz-05 | Zehnerpotenzen 10⁻¹ bis 10⁻⁶ mit Namen | Gym 6 · RS 7 · IB 4 | Z18 |
| zz-06 | Primzahlen bis 100 | Gym 5 · RS 5 · IB 1 | Z8 |
| zz-07 | Teilbar durch 2 | Gym 5 · RS 5 · IB 1 | Z7 |
| zz-08 | Teilbar durch 3 | Gym 5 · RS 5 · IB 1 | Z7 |
| zz-09 | Teilbar durch 4 | ohne Beleg | – |
| zz-10 | Teilbar durch 5 | Gym 5 · RS 5 · IB 1 | Z7 |
| zz-11 | Teilbar durch 6 | ohne Beleg | – |
| zz-12 | Teilbar durch 8 | ohne Beleg | – |
| zz-13 | Teilbar durch 9 | Gym 5 · RS 5 · IB 1 | Z7 |
| zz-14 | Teilbar durch 10 | Gym 5 · RS 5 · IB 1 | Z7 |
| zz-15 | Teilbar durch 25 | ohne Beleg | – |

## Vorschlag zur Gliederung der Karte

- **Nebeneinander (Hauptansicht):** drei schmale Spalten Quadratzahlen, Kubikzahlen, Zweierpotenzen; darunter die Zehnerpotenzen als Tabelle (Potenz, Zahl, Name). Das ist die Auswendig-Ecke und passt auf eine Bildschirmseite.
- **Primzahlen:** als Zahlengitter 1 bis 100 mit eingefärbten Primzahlen; der Test „nur mit 2, 3, 5, 7 prüfen“ steht als Merksatz darunter.
- **Teilbarkeit:** eine Zeile je Teiler (2, 3, 4, 5, 6, 8, 9, 10, 25) mit Regel; Ja- und Nein-Beispiel erst nach Antippen sichtbar (zum Aufklappen), damit das Kind erst selbst probiert.
- **Zum Aufklappen:** Begründung „warum nur bis 7“, Trick fürs Quadrieren von Zahlen mit Endziffer 5, kleine Zehnerpotenzen.
- **Suche:** `stichwoerter` (z. B. „Quadratzahl“, „Primzahl“, „teilbar durch 9“).
