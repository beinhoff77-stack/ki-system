# Regel-Universum · Klassenleitern: dieselbe Regel, dieselbe Idee – von Klasse 5 bis 10

Mathe-Profi, 27.11.2026 (Auftrag 15, Teil A und B). Erzeugt von `klassenleiter.py` aus `leiter_daten.py`; 174 Beispiele, jedes nachgerechnet, jede Klasse gegen die Themenliste geprüft (Lauf „OK“).
Für den Designer liegt dasselbe als `klassenleiter.json` vor – mit den genauen Zeichenpositionen der wirkenden Stelle.

## Wie die Leitern gebaut sind

- **Je Regel und Klasse genau eine Aussage:** ein Rechenbeispiel mit dem Thema der App – oder ausdrücklich „kommt nicht vor“ mit Grund. Kein Feld ist leer, nichts ist erfunden.
- **Gleich gebaut:** In jeder Zeile einer Leiter steht dieselbe Stelle an derselben Position und es geschieht dieselbe Handlung. Nur die Zahlen werden zu Brüchen, Buchstaben, Wurzeln.
- **Wirkende Stelle:** die Zeichen in ⟦ ⟧. Genau diese markiert der Designer; untereinandergesetzt stehen sie senkrecht übereinander.
- **Art:** Vorwissen (kommt vor, wird noch nicht als Regel gelehrt), Einführung, Anwendung. Geprüft gegen die Lehrplan-Kopie der App: `lehrplan-pruefung.md`.
- **Klassen:** Gymnasium Bayern. Realschule und IB: siehe `lehrplan-pruefung.md`.
- „kommt nicht vor … wird als bekannt benutzt“ heißt: Die Regel wird in dieser Klasse gebraucht, aber kein Thema der App übt sie eigens. „Beginnt später“ heißt: Der Stoff ist noch nicht dran.

## Teil A – die 14 Rechenregeln

77 Beispiele, 7 Mal „kommt nicht vor“ (von 84 Feldern).

| | Kl. 5 | Kl. 6 | Kl. 7 | Kl. 8 | Kl. 9 | Kl. 10 |
|---|---|---|---|---|---|---|
| Stellenwert | E | E | A | A | – | – |
| Plus und Minus mit negativen Zahlen | E | A | A | A | A | A |
| Vorzeichen bei Mal und Geteilt | E | A | A | A | A | A |
| Reihenfolge beim Rechnen | E | A | A | A | A | A |
| Tauschen, Klammern, Zusammenfassen | E | A | E | A | A | A |
| Ausmultiplizieren und Ausklammern | E | A | E | A | A | A |
| Minus vor der Klammer | V | V | E | A | A | A |
| Potenzen | E | A | E | E | E | A |
| Erweitern und Kürzen | – | E | A | A | A | A |
| Rechnen mit Brüchen | – | E | A | A | A | A |
| Verhältnis (Dreisatz) | E | E | A | A | A | A |
| Gegenrechnung | E | A | A | A | E | E |
| Gleichung als Waage | V | – | E | A | A | A |
| Nullprodukt | V | – | – | V | E | A |

### Rechenregel 1: Stellenwert (`rr.stellenwert`)

> **Mal zehn: Jede Ziffer rückt eins nach links.**

**In jeder Zeile markiert:** Das „· 10“ (oder „· 100“, „· 10⁻⁴“) – die Ziffern bleiben, sie rücken nur.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | 34 ⟦· 10⟧ = 340 | Einführung | `zahlen.natuerlich` |
| 6 | 2,5 ⟦· 10⟧ = 25 | Einführung | `bruch.dezimal` |
| 7 | 0,15 ⟦· 100⟧ = 15, also 15 % | Anwendung | `bruch.prozent_grundwert` |
| 8 | 3 ⟦· 10⁻⁴⟧ = 0,0003 | Anwendung | `terme.potenzgesetze_ganzzahlig` |
| 9 | *kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt* | – | – |
| 10 | *kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt* | – | – |

### Rechenregel 2: Plus und Minus mit negativen Zahlen (`rr.plusminus`)

> **Minus heißt umdrehen – zweimal umdrehen ist wieder geradeaus.**

**In jeder Zeile markiert:** Die zwei Minuszeichen nebeneinander: Rechenzeichen und Vorzeichen.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | 3 ⟦−⟧ (⟦−⟧2) = 3 + 2 = 5 | Einführung | `zahlen.ganz` |
| 6 | ½ ⟦−⟧ (⟦−⟧¼) = ½ + ¼ = ¾ | Anwendung | `bruch.rechnen` |
| 7 | 3x ⟦−⟧ (⟦−⟧2x) = 3x + 2x = 5x | Anwendung | `terme.umformen` |
| 8 | f(x) = 3 − x, x = −2: 3 ⟦−⟧ (⟦−⟧2) = 3 + 2 = 5 | Anwendung | `funktionen.linear` |
| 9 | 3√2 ⟦−⟧ (⟦−⟧2√2) = 3√2 + 2√2 = 5√2 | Anwendung | `zahlen.reell` |
| 10 | f(x) = 3 − 2x³, x = −1: 3 ⟦−⟧ (⟦−⟧2) = 3 + 2 = 5 | Anwendung | `funktionen.ganzrational` |

### Rechenregel 3: Vorzeichen bei Mal und Geteilt (`rr.vorzeichen`)

> **Minus mal Minus gibt Plus, Minus mal Plus gibt Minus.**

**In jeder Zeile markiert:** Die Vorzeichen der Zahlen und das Vorzeichen des Ergebnisses. In Klasse 10 sind es drei Minus: Ein Umdrehen bleibt übrig.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | (⟦−⟧3) · (⟦−⟧4) = ⟦+⟧12 | Einführung | `zahlen.rechengesetze` |
| 6 | (⟦−⟧⅔) · (⟦−⟧¾) = ⟦+⟧½ | Anwendung | `bruch.rechnen` |
| 7 | (⟦−⟧3x) · (⟦−⟧4) = ⟦+⟧12x | Anwendung | `terme.umformen` |
| 8 | Steigung: (⟦−⟧6) : (⟦−⟧2) = ⟦+⟧3 | Anwendung | `funktionen.linear` |
| 9 | (⟦−⟧5)² = (⟦−⟧5) · (⟦−⟧5) = ⟦+⟧25 | Anwendung | `gleichungen.quadratisch` |
| 10 | (⟦−⟧2)³ = (⟦−⟧2) · (⟦−⟧2) · (⟦−⟧2) = ⟦−⟧8 | Anwendung | `funktionen.ganzrational` |

### Rechenregel 4: Reihenfolge beim Rechnen (`rr.reihenfolge`)

> **Klammer zuerst, dann Hoch, dann Punkt vor Strich.**

**In jeder Zeile markiert:** Der Teil, der zuerst gerechnet wird – in jeder Zeile der Punkt-Teil hinter dem Plus. Steht darin ein Hoch (Klasse 9 und 10), kommt es noch davor.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | 2 + ⟦3 · 4⟧ = 2 + 12 = 14 | Einführung | `zahlen.rechengesetze` |
| 6 | ½ + ⟦½ · ½⟧ = ½ + ¼ = ¾ | Anwendung | `bruch.rechnen` |
| 7 | 2 + ⟦3 · x⟧ bleibt 2 + 3x – nicht 5x | Anwendung | `terme.umformen` |
| 8 | f(x) = 2 + 3x, x = 4: 2 + ⟦3 · 4⟧ = 14 | Anwendung | `funktionen.linear` |
| 9 | f(x) = 2 + 3x², x = 2: 2 + ⟦3 · 2²⟧ = 14 | Anwendung | `funktionen.quadratisch` |
| 10 | f(x) = 2 + 3 · 2ˣ, x = 2: 2 + ⟦3 · 2²⟧ = 14 | Anwendung | `funktionen.exponential_log` |

### Rechenregel 5: Tauschen, Klammern, Zusammenfassen (`rr.tauschen`)

> **Tauschen bei Plus und Mal. Zusammenfassen: nur Gleiches zu Gleichem.**

**In jeder Zeile markiert:** Der Summand, der wandert – immer zusammen mit seinem Rechenzeichen.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | 12 − 30 ⟦+ 18⟧ = 12 ⟦+ 18⟧ − 30 = 0 | Einführung | `zahlen.ganz` |
| 6 | ¼ − ½ ⟦+ ¾⟧ = ¼ ⟦+ ¾⟧ − ½ = ½ | Anwendung | `bruch.rechnen` |
| 7 | 3a + 2b ⟦+ 4a⟧ = 3a ⟦+ 4a⟧ + 2b = 7a + 2b | Einführung | `terme.umformen` |
| 8 | 2x + 3y ⟦− 2x⟧ + y = 2x ⟦− 2x⟧ + 4y = 4y | Anwendung | `gleichungen.lgs2` |
| 9 | 3√2 + 5 ⟦+ 2√2⟧ = 3√2 ⟦+ 2√2⟧ + 5 = 5√2 + 5 | Anwendung | `zahlen.reell` |
| 10 | 3x³ + 2x ⟦+ 4x³⟧ = 3x³ ⟦+ 4x³⟧ + 2x = 7x³ + 2x | Anwendung | `funktionen.ganzrational` |

### Rechenregel 6: Ausmultiplizieren und Ausklammern (`rr.ausmultiplizieren`)

> **Was vor der Klammer steht, nimmt jeden in der Klammer mal.**

**In jeder Zeile markiert:** Der Faktor vor der Klammer – an allen drei Stellen, an denen er steht.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | ⟦6⟧ · (20 + 2) = ⟦6⟧ · 20 + ⟦6⟧ · 2 = 132 | Einführung | `zahlen.rechengesetze` |
| 6 | ⟦4⟧ · (2 + ½) = ⟦4⟧ · 2 + ⟦4⟧ · ½ = 10 | Anwendung | `bruch.rechnen` |
| 7 | ⟦3⟧ · (x + 2) = ⟦3⟧ · x + ⟦3⟧ · 2 = 3x + 6 | Einführung | `terme.umformen` |
| 8 | ⟦x⟧ · (3/x + ½) = ⟦x⟧ · (3/x) + ⟦x⟧ · ½, für x ≠ 0 | Anwendung | `gleichungen.bruch` |
| 9 | ⟦√2⟧ · (√2 + 3) = ⟦√2⟧ · √2 + ⟦√2⟧ · 3 = 2 + 3√2 | Anwendung | `zahlen.reell` |
| 10 | ⟦x⟧ · (x² − 4) = ⟦x⟧ · x² − ⟦x⟧ · 4 = x³ − 4x | Anwendung | `gleichungen.polynom` |

### Rechenregel 7: Minus vor der Klammer (`rr.minusklammer`)

> **Minus vor der Klammer dreht alle Zeichen um.**

**In jeder Zeile markiert:** Das Minus vor der Klammer und das Zeichen in der Klammer, das wechselt.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | 20 ⟦−⟧ (8 ⟦−⟧ 3) = 20 ⟦−⟧ 8 ⟦+⟧ 3 = 15 | Vorwissen | `zahlen.rechengesetze` |
| 6 | 2 ⟦−⟧ (¾ ⟦−⟧ ¼) = 2 ⟦−⟧ ¾ ⟦+⟧ ¼ = 1½ | Vorwissen | `bruch.rechnen` |
| 7 | 5x ⟦−⟧ (3x ⟦−⟧ 2) = 5x ⟦−⟧ 3x ⟦+⟧ 2 = 2x + 2 | Einführung | `terme.umformen` |
| 8 | 7 ⟦−⟧ (2x ⟦−⟧ 6) = 7 ⟦−⟧ 2x ⟦+⟧ 6 = 13 − 2x | Anwendung | `gleichungen.ungleichungen` |
| 9 | x² ⟦−⟧ (x² ⟦−⟧ 3x) = x² ⟦−⟧ x² ⟦+⟧ 3x = 3x | Anwendung | `gleichungen.quadratisch` |
| 10 | x³ ⟦−⟧ (x³ ⟦−⟧ 4x) = x³ ⟦−⟧ x³ ⟦+⟧ 4x = 4x | Anwendung | `gleichungen.polynom` |

### Rechenregel 8: Potenzen (`rr.potenz`)

> **Hoch drei heißt: die Zahl dreimal hinschreiben und malnehmen.**

**In jeder Zeile markiert:** Die Hochzahlen: Sie zählen die Faktoren und werden beim Malnehmen addiert.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | 2⟦³⟧ · 2⟦²⟧ = (2 · 2 · 2) · (2 · 2) = 2⟦⁵⟧ = 32 | Einführung | `zahlen.potenzen_basis` |
| 6 | 10⟦³⟧ · 10⟦²⟧ = 10⟦⁵⟧ = 100 000 | Anwendung | `zahlen.potenzen_zehner` |
| 7 | x⟦³⟧ · x⟦²⟧ = (x · x · x) · (x · x) = x⟦⁵⟧ | Einführung | `terme.potenzgesetze_natuerlich` |
| 8 | x⟦³⟧ · x⟦⁻²⟧ = x⟦¹⟧ = x, für x ≠ 0 | Einführung | `terme.potenzgesetze_ganzzahlig` |
| 9 | x^⟦½⟧ · x^⟦½⟧ = x⟦¹⟧ = x, für x ≥ 0 | Einführung | `zahlen.rationale_exponenten` |
| 10 | 2⟦ˣ⟧ · 2⟦³⟧ = 2⁽⟦ˣ⁺³⟧⁾ | Anwendung | `funktionen.exponential_log` |

### Rechenregel 9: Erweitern und Kürzen (`rr.kuerzen`)

> **Oben und unten dasselbe mal oder geteilt – der Bruch bleibt gleich.**

**In jeder Zeile markiert:** Der gemeinsame Faktor – einmal im Zähler, einmal im Nenner.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – der Stoff dafür beginnt später (Brüche ab Klasse 6)* | – | – |
| 6 | 12/18 = (2 · ⟦6⟧) / (3 · ⟦6⟧) = 2/3 | Einführung | `bruch.brueche` |
| 7 | 6x/9 = (2x · ⟦3⟧) / (3 · ⟦3⟧) = 2x/3 | Anwendung | `gleichungen.linear` |
| 8 | (3 · ⟦(x + 2)⟧) / (1 · ⟦(x + 2)⟧) = 3, für x ≠ −2 | Anwendung | `terme.bruchterme` |
| 9 | 6 cm : 9 cm = (2 · ⟦3⟧) : (3 · ⟦3⟧) = 2 : 3 | Anwendung | `abbildungen.aehnlichkeit` |
| 10 | 2/4 = (1 · ⟦2⟧) / (2 · ⟦2⟧) = ½ | Anwendung | `stochastik.mehrstufig` |

### Rechenregel 10: Rechnen mit Brüchen (`rr.bruchrechnen`)

> **Plus und Minus: erst gleiche Nenner. Mal: oben mal oben, unten mal unten. Geteilt: mit dem Kehrwert malnehmen.**

**In jeder Zeile markiert:** Der gemeinsame Nenner – in jedem der drei Brüche.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – der Stoff dafür beginnt später (Brüche ab Klasse 6)* | – | – |
| 6 | 1/2 + 1/3 = 3/⟦6⟧ + 2/⟦6⟧ = 5/⟦6⟧ | Einführung | `bruch.rechnen` |
| 7 | x/2 + x/3 = 3x/⟦6⟧ + 2x/⟦6⟧ = 5x/⟦6⟧ | Anwendung | `gleichungen.linear` |
| 8 | 1/x + 1/(2x) = 2/⟦(2x)⟧ + 1/⟦(2x)⟧ = 3/⟦(2x)⟧, für x ≠ 0 | Anwendung | `terme.bruchterme` |
| 9 | 1/2 + 1/3 − 1/6 = 3/⟦6⟧ + 2/⟦6⟧ − 1/⟦6⟧ = 4/⟦6⟧ | Anwendung | `stochastik.verknuepft` |
| 10 | 1/6 + 1/3 = 1/⟦6⟧ + 2/⟦6⟧ = 3/⟦6⟧ | Anwendung | `stochastik.mehrstufig` |

### Rechenregel 11: Verhältnis (Dreisatz) (`rr.verhaeltnis`)

> **Erst auf eins, dann auf viele.**

**In jeder Zeile markiert:** Die Eins in der Mitte: erst auf eins, dann auf viele.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | 3 kg: 7,50 € → ⟦1 kg⟧: 2,50 € → 5 kg: 12,50 € | Einführung | `groessen.proportional` |
| 6 | 100 %: 60 € → ⟦1 %⟧: 0,60 € → 25 %: 15 € | Einführung | `bruch.prozent` |
| 7 | 80 %: 48 € → ⟦1 %⟧: 0,60 € → 100 %: 60 € | Anwendung | `bruch.prozent_grundwert` |
| 8 | x = 2: y = 3 → ⟦x = 1⟧: y = 1,5 → x = 4: y = 6 | Anwendung | `funktionen.linear` |
| 9 | 2 cm: 3 cm → ⟦1 cm⟧: 1,5 cm → 4 cm: 6 cm | Anwendung | `abbildungen.aehnlichkeit` |
| 10 | 360°: 2π → ⟦1°⟧: π/180 → 90°: π/2 | Anwendung | `funktionen.trig` |

### Rechenregel 12: Gegenrechnung (`rr.gegenrechnung`)

> **Rückwärts rechnen: Was zuletzt kam, geht zuerst.**

**In jeder Zeile markiert:** Die Rechnung und ihre Gegenrechnung – als Paar.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | □ ⟦+ 7⟧ = 3, also □ = 3 ⟦− 7⟧ = −4 | Einführung | `gleichungen.einfach` |
| 6 | □ ⟦· ¾⟧ = 12, also □ = 12 ⟦: ¾⟧ = 16 | Anwendung | `bruch.rechnen` |
| 7 | G ⟦· 1,2⟧ = 60 €, also G = 60 € ⟦: 1,2⟧ = 50 € | Anwendung | `bruch.prozent_grundwert` |
| 8 | A = g ⟦· h⟧, also g = A ⟦: h⟧ (für h ≠ 0) | Anwendung | `gleichungen.formeln` |
| 9 | x ⟦hoch 2⟧ = 49, also x = ⟦±√⟧49 = ±7 | Einführung | `gleichungen.quadratisch` |
| 10 | 2 ⟦hoch x⟧ = 8, also x = ⟦log₂⟧ 8 = 3 | Einführung | `gleichungen.exponential` |

### Rechenregel 13: Gleichung als Waage (`rr.waage`)

> **Eine Gleichung ist eine Waage: Was du links tust, musst du auch rechts tun.**

**In jeder Zeile markiert:** Was auf beiden Seiten getan wird – der Befehl hinter dem Strich.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | □ + 7 = 3 &#124; ⟦− 7⟧ → □ = −4 | Vorwissen | `gleichungen.einfach` |
| 6 | *kommt nicht vor – kein Thema der App in dieser Klasse (keine Gleichungen in Klasse 6)* | – | – |
| 7 | 2x + 2 = 12 &#124; ⟦− 2⟧ → 2x = 10 &#124; ⟦: 2⟧ → x = 5 | Einführung | `gleichungen.linear` |
| 8 | 2x + 2 < 12 &#124; ⟦− 2⟧ → 2x < 10 &#124; ⟦: 2⟧ → x < 5 | Anwendung | `gleichungen.ungleichungen` |
| 9 | 2x² + 2 = 20 &#124; ⟦− 2⟧ → 2x² = 18 &#124; ⟦: 2⟧ → x² = 9 | Anwendung | `gleichungen.quadratisch` |
| 10 | 2 · 2ˣ + 2 = 18 &#124; ⟦− 2⟧ → 2 · 2ˣ = 16 &#124; ⟦: 2⟧ → 2ˣ = 8 | Anwendung | `gleichungen.exponential` |

### Rechenregel 14: Nullprodukt (`rr.nullprodukt`)

> **Mal ergibt nur null, wenn eine der Zahlen null ist.**

**In jeder Zeile markiert:** Die Null rechts und der Faktor, der null wird.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | ⟦□⟧ · 7 = ⟦0⟧: □ = 0 | Vorwissen | `gleichungen.einfach` |
| 6 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 7 | *kommt nicht vor – kein Thema der App in dieser Klasse (Gleichungen mit x² erst ab Klasse 9)* | – | – |
| 8 | Nenner ⟦x⟧ · ⟦(x − 4)⟧ ist ⟦null⟧ für x = 0 oder x = 4: beide Werte sind ausgeschlossen | Vorwissen | `terme.bruchterme` |
| 9 | ⟦(x − 2)⟧ · ⟦(x + 3)⟧ = ⟦0⟧: x = 2 oder −3 | Einführung | `gleichungen.quadratisch` |
| 10 | ⟦x⟧ · ⟦(x − 2)⟧ · ⟦(x + 2)⟧ = ⟦0⟧: x = 0, 2 oder −2 | Anwendung | `gleichungen.polynom` |

## Teil B – die 28 tragenden Ideen

| | Kl. 5 | Kl. 6 | Kl. 7 | Kl. 8 | Kl. 9 | Kl. 10 |
|---|---|---|---|---|---|---|
| Zahlengerade | E | A | – | A | A | – |
| Bündeln in Zehnern | E | E | – | A | – | – |
| Bausteine | E | A | – | – | A | – |
| Schreibweisen | – | E | A | A | A | – |
| Hoch und zurück | E | A | A | A | E | E |
| Term | V | – | E | A | A | A |
| Erlaubte Zahlen | – | – | – | E | A | A |
| Gleichung lösen | E | – | E | E | E | A |
| Höherer Grad | – | – | – | – | E | A |
| Größe | E | E | – | – | – | A |
| Wert für eins | E | A | A | A | A | – |
| Prozent als Faktor | – | E | E | A | – | A |
| Winkel an Geraden | E | – | E | – | A | – |
| Gleicher Abstand | E | – | E | – | A | – |
| Deckungsgleich | V | – | E | – | – | – |
| Ähnlich | – | – | – | – | E | A |
| Rechtwinkliges Dreieck | – | – | – | – | E | A |
| Auslegen und zählen | E | E | A | – | – | – |
| Aus dem Rechteck | E | E | – | E | A | A |
| Aus dem Quader | – | E | – | E | – | E |
| Haut des Körpers | E | – | – | E | – | E |
| Zuordnung | V | – | V | E | A | A |
| Wachstum | V | – | – | E | – | E |
| Gleichung und Form | – | – | – | E | E | E |
| Kennzahl | – | E | E | – | – | – |
| Vom Teil aufs Ganze | – | – | – | E | – | A |
| Anteil | V | – | – | E | A | A |
| Stufen | – | – | – | – | – | E |

**Ideen, die nur in einer oder zwei Klassen vorkommen** (keine Leiter, sondern ein Ort): Höherer Grad (Algebra): Klasse 9 und 10; Deckungsgleich (Geometrie): Klasse 5 und 7; Ähnlich (Geometrie): Klasse 9 und 10; Rechtwinkliges Dreieck (Geometrie): Klasse 9 und 10; Kennzahl (Daten und Zufall): Klasse 6 und 7; Vom Teil aufs Ganze (Daten und Zufall): Klasse 8 und 10; Stufen (Daten und Zufall): Klasse 10.

### Planet „Zahlen“

#### Zahlengerade (`id.zahlen.zahlengerade`) – läuft über die Klassen 5, 6, 8, 9

> **Links ist kleiner, rechts ist größer – auch unter null.**

**In jeder Zeile markiert:** Das Kleiner-Zeichen: Links steht, was auf der Zahlengeraden weiter links liegt.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | −3 ⟦<⟧ 2 | Einführung | `zahlen.ganz` |
| 6 | −½ ⟦<⟧ ¼ | Anwendung | `bruch.rechnen` |
| 7 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 8 | Intervall ]−3; 2]: −3 ⟦<⟧ x ⟦≤⟧ 2 | Anwendung | `zahlen.intervalle` |
| 9 | 1 ⟦<⟧ √2 ⟦<⟧ 2 | Anwendung | `zahlen.reell` |
| 10 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |

#### Bündeln in Zehnern (`id.zahlen.buendeln`) – läuft über die Klassen 5, 6, 8

> **Zehn Einer sind ein Zehner, zehn Zehntel sind ein Einer.**

**In jeder Zeile markiert:** Die Zehn, die getauscht wird.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | ⟦10⟧ Einer = 1 Zehner | Einführung | `zahlen.natuerlich` |
| 6 | ⟦10⟧ Zehntel = 1 Einer | Einführung | `bruch.dezimal` |
| 7 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 8 | ⟦10⟧ Tausendstel = 1 Hundertstel | Anwendung | `terme.potenzgesetze_ganzzahlig` |
| 9 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 10 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |

#### Bausteine (`id.zahlen.bausteine`) – läuft über die Klassen 5, 6, 9

> **Primzahlen sind die Bausteine: Jede Zahl ab zwei ist aus ihnen malgenommen.**

**In jeder Zeile markiert:** Die Primfaktoren.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | 60 = ⟦2 · 2 · 3 · 5⟧ | Einführung | `zahlen.teilbarkeit` |
| 6 | 12/18 = (⟦2 · 2 · 3⟧) / (⟦2 · 3 · 3⟧) = 2/3 | Anwendung | `bruch.brueche` |
| 7 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 8 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 9 | √12 = √(⟦2 · 2 · 3⟧) = 2 · √3 | Anwendung | `zahlen.wurzeln_basis` |
| 10 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |

#### Schreibweisen (`id.zahlen.schreibweisen`) – läuft über die Klassen 6, 7, 8, 9

> **Ein Halb, null Komma fünf, fünfzig Prozent: dreimal dieselbe Zahl.**

**In jeder Zeile markiert:** Die Gleichheitszeichen zwischen den drei Schreibweisen.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – der Stoff dafür beginnt später (Brüche ab Klasse 6)* | – | – |
| 6 | ½ ⟦=⟧ 0,5 ⟦=⟧ 50 % | Einführung | `bruch.prozent` |
| 7 | ⅕ ⟦=⟧ 0,2 ⟦=⟧ 20 % | Anwendung | `bruch.prozent_grundwert` |
| 8 | ¼ ⟦=⟧ 0,25 ⟦=⟧ 25 % | Anwendung | `stochastik.grundbegriffe` |
| 9 | ⅓ ⟦=⟧ 0,333… ⟦≈⟧ 33,3 % | Anwendung | `zahlen.reell` |
| 10 | *kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt* | – | – |

#### Hoch und zurück (`id.zahlen.hoch_zurueck`) – läuft über die Klassen 5, 6, 7, 8, 9, 10

> **Hoch rechnet hin, die Wurzel rechnet zurück.**

**In jeder Zeile markiert:** Das Hoch – und ab Klasse 9 die Rechnung, die zurückfragt.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | 3 ⟦hoch 2⟧ = 9 | Einführung | `zahlen.potenzen_basis` |
| 6 | 10 ⟦hoch 3⟧ = 1 000 | Anwendung | `zahlen.potenzen_zehner` |
| 7 | x ⟦hoch 2⟧ · x = x³ | Anwendung | `terme.potenzgesetze_natuerlich` |
| 8 | 2 ⟦hoch −3⟧ = ⅛ | Anwendung | `terme.potenzgesetze_ganzzahlig` |
| 9 | 3 ⟦hoch 2⟧ = 9 und zurück: ⟦√⟧9 = 3 | Einführung | `zahlen.wurzeln_basis` |
| 10 | 2 ⟦hoch 3⟧ = 8 und zurück: ⟦log₂⟧ 8 = 3 | Einführung | `funktionen.exponential_log` |

### Planet „Algebra“

#### Term (`id.algebra.term`) – läuft über die Klassen 5, 7, 8, 9, 10

> **Ein Term ist ein Rechenrezept: Zahl hinein, Ergebnis heraus.**

**In jeder Zeile markiert:** Die Zahl, die eingesetzt wird – die 5, in Klasse 10 die 2 (3⁵ wäre unhandlich).

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | 2 · ⟦5⟧ + 3 = 13 | Vorwissen | `zahlen.rechengesetze` |
| 6 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 7 | T(⟦5⟧) = 2 · ⟦5⟧ + 3 = 13 | Einführung | `terme.aufstellen` |
| 8 | f(⟦5⟧) = 2 · ⟦5⟧ + 3 = 13 | Anwendung | `funktionen.grundbegriffe` |
| 9 | f(⟦5⟧) = 2 · ⟦5⟧² + 3 = 53 | Anwendung | `funktionen.quadratisch` |
| 10 | f(x) = 2 · 3ˣ + 3; f(⟦2⟧) = 2 · 3⟦²⟧ + 3 = 21 | Anwendung | `funktionen.exponential_log` |

#### Erlaubte Zahlen (`id.algebra.erlaubte_zahlen`) – läuft über die Klassen 8, 9, 10

> **Durch null teilen geht nie – prüfe das zuerst.**

**In jeder Zeile markiert:** Die Bedingung für x: Kein Nenner wird 0, unter keiner Quadratwurzel steht etwas Negatives.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 6 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 7 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 8 | 1 : (x − 2): nicht erlaubt ⟦x = 2⟧ | Einführung | `terme.bruchterme` |
| 9 | √(x − 2): erlaubt nur ⟦x ≥ 2⟧ | Anwendung | `zahlen.wurzeln_basis` |
| 10 | log₂(x − 2): erlaubt nur ⟦x > 2⟧ | Anwendung | `funktionen.exponential_log` |

#### Gleichung lösen (`id.algebra.gleichung_loesen`) – läuft über die Klassen 5, 7, 8, 9, 10

> **Lösen heißt: alle Zahlen finden, für die die Gleichung stimmt.**

**In jeder Zeile markiert:** Die Lösung – jede Zahl, für die die Zeile stimmt.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | □ + 7 = 3 stimmt für ⟦□ = −4⟧ | Einführung | `gleichungen.einfach` |
| 6 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 7 | 2x + 2 = 12 stimmt für ⟦x = 5⟧ | Einführung | `gleichungen.linear` |
| 8 | x + 5 < 2 stimmt für ⟦alle x < −3⟧ | Einführung | `gleichungen.ungleichungen` |
| 9 | x² = 9 stimmt für ⟦x = 3⟧ und für ⟦x = −3⟧ | Einführung | `gleichungen.quadratisch` |
| 10 | 2ˣ = 8 stimmt für ⟦x = 3⟧ | Anwendung | `gleichungen.exponential` |

#### Höherer Grad (`id.algebra.hoeherer_grad`) – läuft über die Klassen 9, 10

> **Steht x im Quadrat: erst null auf eine Seite, dann zerlegen.**

**In jeder Zeile markiert:** Die Null auf der rechten Seite – erst dann wird zerlegt.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 6 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 7 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 8 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 9 | x² + x − 6 = ⟦0⟧ → (x − 2) · (x + 3) = ⟦0⟧ | Einführung | `gleichungen.quadratisch` |
| 10 | x³ − 4x = ⟦0⟧ → x · (x − 2) · (x + 2) = ⟦0⟧ | Anwendung | `gleichungen.polynom` |

### Planet „Geld und Verhältnisse“

#### Größe (`id.verhaeltnisse.groesse`) – läuft über die Klassen 5, 6, 10

> **Kleinere Einheit, größere Zahl – größere Einheit, kleinere Zahl.**

**In jeder Zeile markiert:** Die beiden Zahlen an derselben Größe.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | ⟦3⟧ m = ⟦30⟧ dm | Einführung | `groessen.einheiten` |
| 5 | ⟦3⟧ m² = ⟦300⟧ dm² | Einführung | `messen.flaechen` |
| 6 | ⟦3⟧ m³ = ⟦3 000⟧ dm³ | Einführung | `messen.volumen` |
| 7 | *kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt* | – | – |
| 8 | *kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt* | – | – |
| 9 | *kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt* | – | – |
| 10 | ⟦180⟧° = ⟦π⟧ im Bogenmaß | Anwendung | `funktionen.trig` |

#### Wert für eins (`id.verhaeltnisse.wert_fuer_eins`) – läuft über die Klassen 5, 6, 7, 8, 9

> **Doppelt so viel kostet doppelt so viel.**

**In jeder Zeile markiert:** Das „· 2“ – es gilt für beide Größen zugleich.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | 3 kg: 7,50 € ⟦· 2⟧ → 6 kg: 15 € | Einführung | `groessen.proportional` |
| 6 | 25 %: 15 € ⟦· 2⟧ → 50 %: 30 € | Anwendung | `bruch.prozent` |
| 7 | 40 %: 24 € ⟦· 2⟧ → 80 %: 48 € | Anwendung | `bruch.prozent_grundwert` |
| 8 | x = 3: y = 7,5 ⟦· 2⟧ → x = 6: y = 15 | Anwendung | `funktionen.linear` |
| 9 | 3 cm: 4,5 cm ⟦· 2⟧ → 6 cm: 9 cm | Anwendung | `abbildungen.aehnlichkeit` |
| 10 | *kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt* | – | – |

#### Prozent als Faktor (`id.verhaeltnisse.prozent`) – läuft über die Klassen 6, 7, 8, 10

> **Prozent heißt: von hundert.**

**In jeder Zeile markiert:** Der Faktor, der aus dem Prozentsatz wird.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – der Stoff dafür beginnt später (Prozent ab Klasse 6)* | – | – |
| 6 | 25 % von 60 € = ⟦0,25⟧ · 60 € = 15 € | Einführung | `bruch.prozent` |
| 7 | 50 € plus 20 % = ⟦1,2⟧ · 50 € = 60 € | Einführung | `bruch.prozent_grundwert` |
| 8 | 12 von 48: 12 : 48 = ⟦0,25⟧ = 25 % | Anwendung | `stochastik.grundbegriffe` |
| 9 | *kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt* | – | – |
| 10 | Zweimal plus 5 %: ⟦1,05⟧ · ⟦1,05⟧ · 1 000 € = 1 102,50 € | Anwendung | `funktionen.exponential_log` |

### Planet „Geometrie“

#### Winkel an Geraden (`id.geometrie.winkel`) – läuft über die Klassen 5, 7, 9

> **Gleiche Winkel an Parallelen – darum im Dreieck immer 180 Grad.**

**In jeder Zeile markiert:** Die Summe 180° – die gerade Linie.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | Gestreckter Winkel: 90° + 90° = ⟦180°⟧ | Einführung | `geometrie.grundbegriffe` |
| 6 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 7 | Dreieck: 50° + 60° + 70° = ⟦180°⟧ | Einführung | `geometrie.winkelsaetze` |
| 8 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 9 | Rechtwinklig: 90° + 30° + 60° = ⟦180°⟧ | Anwendung | `trigo.rechtwinklig` |
| 10 | *kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt* | – | – |

#### Gleicher Abstand (`id.geometrie.abstand`) – läuft über die Klassen 5, 7, 9

> **Der Kreis: alle Punkte gleich weit von der Mitte.**

**In jeder Zeile markiert:** Der gleiche Abstand.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | Kreis um M: alle Punkte ⟦3 cm⟧ von M | Einführung | `geometrie.ortslinien` |
| 6 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 7 | Mittelsenkrechte: von A und B ⟦gleich weit⟧ | Einführung | `geometrie.konstruktion` |
| 8 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 9 | (3 &#124; 4) ist vom Ursprung ⟦5⟧ entfernt | Anwendung | `trigo.pythagoras` |
| 10 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |

#### Deckungsgleich (`id.geometrie.deckungsgleich`) – läuft über die Klassen 5, 7

> **Spiegeln, schieben, drehen – Form und Größe bleiben gleich.**

**In jeder Zeile markiert:** Die Länge, die vorher und nachher gleich ist.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | Rechteck: Gegenseiten ⟦gleich lang⟧ | Vorwissen | `geometrie.grundbegriffe` |
| 6 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 7 | Spiegeln: [AB] = ⟦3⟧, danach [A′B′] = ⟦3⟧ | Einführung | `abbildungen.kongruenz` |
| 8 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 9 | *kommt nicht vor – kein Thema der App in dieser Klasse (dort beginnt „Ähnlich“)* | – | – |
| 10 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |

#### Ähnlich (`id.geometrie.aehnlich`) – läuft über die Klassen 9, 10

> **Gleiche Form, andere Größe: alle Längen mal dieselbe Zahl.**

**In jeder Zeile markiert:** Der Faktor, mit dem jede Länge malgenommen wird.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 6 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 7 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 8 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 9 | 3, 4, 5 cm ⟦· 2⟧ → 6, 8, 10 cm | Einführung | `abbildungen.aehnlichkeit` |
| 10 | Pyramide, Spitze bei halber Höhe abgeschnitten: Kanten ⟦· ½⟧, Volumen · ⅛ | Anwendung | `raum.pyramide_kegel_kugel` |

#### Rechtwinkliges Dreieck (`id.geometrie.rechtwinklig`) – läuft über die Klassen 9, 10

> **Rechter Winkel im Dreieck: a² plus b² ist c².**

**In jeder Zeile markiert:** Die Quadrate der drei Seiten.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 6 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 7 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 8 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 9 | Dreieck 3, 4, 5 cm: ⟦3² + 4² = 5²⟧ | Einführung | `trigo.pythagoras` |
| 10 | Kegel r = 3, h = 4, s = 5: ⟦3² + 4² = 5²⟧ | Anwendung | `raum.pyramide_kegel_kugel` |

### Planet „Fläche und Raum“

#### Auslegen und zählen (`id.flaeche_raum.auslegen`) – läuft über die Klassen 5, 6, 7

> **Messen heißt auslegen und zählen.**

**In jeder Zeile markiert:** Das, was gezählt wird: Reihen und Schichten.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | Rechteck: ⟦4 Reihen⟧ zu je 6 = 24 cm² | Einführung | `messen.flaechen` |
| 6 | Quader: ⟦3 Schichten⟧ zu je 20 = 60 cm³ | Einführung | `messen.volumen` |
| 7 | Rechteck: ⟦4 Reihen⟧ zu je x = 4x | Anwendung | `terme.aufstellen` |
| 8 | *kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt* | – | – |
| 9 | *kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt* | – | – |
| 10 | *kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt* | – | – |

#### Aus dem Rechteck (`id.flaeche_raum.aus_dem_rechteck`) – läuft über die Klassen 5, 6, 8, 9, 10

> **Aus dem Rechteck entsteht jede Fläche.**

**In jeder Zeile markiert:** Grundseite mal Höhe – das Rechteck, das in jeder Formel steckt. Längen in cm.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | Rechteck: ⟦6 · 4⟧ = 24 cm² | Einführung | `messen.flaechen` |
| 6 | Parallelogramm: ⟦6 · 4⟧ = 24 cm² | Einführung | `messen.flaechen_vielecke` |
| 6 | Dreieck: ⟦6 · 4⟧ : 2 = 12 cm² | Einführung | `messen.flaechen_vielecke` |
| 7 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 8 | Kreis, r = 3: ⟦π · 3 · 3⟧ ≈ 28,3 cm² | Einführung | `messen.kreisberechnung` |
| 9 | Gleichseitig, a = 6: ⟦6 · 5,2⟧ : 2 ≈ 15,6 cm² | Anwendung | `trigo.pythagoras` |
| 10 | Pyramidenmantel: 4 mal ⟦6 · 5⟧ : 2 = 60 cm² | Anwendung | `raum.pyramide_kegel_kugel` |

#### Aus dem Quader (`id.flaeche_raum.aus_dem_quader`) – läuft über die Klassen 6, 8, 10

> **Grundfläche mal Höhe – bei Spitzen nur ein Drittel.**

**In jeder Zeile markiert:** Grundfläche mal Höhe. Grundfläche in cm², Höhe in cm.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – der Stoff dafür beginnt später (Volumen ab Klasse 6)* | – | – |
| 6 | Quader: ⟦20 · 3⟧ = 60 cm³ | Einführung | `messen.volumen` |
| 7 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 8 | Prisma: ⟦6 · 10⟧ = 60 cm³ | Einführung | `messen.prisma_zylinder` |
| 9 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 10 | Pyramide: ⟦36 · 4⟧ : 3 = 48 cm³ | Einführung | `raum.pyramide_kegel_kugel` |

#### Haut des Körpers (`id.flaeche_raum.haut`) – läuft über die Klassen 5, 8, 10

> **Aufklappen zeigt die ganze Haut des Körpers.**

**In jeder Zeile markiert:** Das Plus: Die Flächen der Haut werden zusammengezählt.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | Quader 5 · 4 · 3 cm: 2 · 20 ⟦+⟧ 2 · 15 ⟦+⟧ 2 · 12 = 94 cm² | Einführung | `messen.koerper_berechnung` |
| 6 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 7 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 8 | Prisma (Dreieck 3 · 4 · 5 cm, Höhe 6 cm): 2 · 6 ⟦+⟧ 18 ⟦+⟧ 24 ⟦+⟧ 30 = 84 cm² | Einführung | `messen.prisma_zylinder` |
| 9 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 10 | Pyramide: 36 ⟦+⟧ 60 = 96 cm² | Einführung | `raum.pyramide_kegel_kugel` |

### Planet „Funktionen“

#### Zuordnung (`id.funktionen.zuordnung`) – läuft über die Klassen 5, 7, 8, 9, 10

> **Zu jedem x gehört genau ein y.**

**In jeder Zeile markiert:** Das Paar: zu diesem x genau dieses y.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | zu ⟦3 kg⟧ gehört ⟦7,50 €⟧ | Vorwissen | `groessen.proportional` |
| 6 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 7 | T(x) = 2x + 1: zu ⟦x = 3⟧ gehört ⟦7⟧ | Vorwissen | `terme.aufstellen` |
| 8 | y = 2x + 1: zu ⟦x = 3⟧ gehört ⟦y = 7⟧ | Einführung | `funktionen.grundbegriffe` |
| 9 | y = x²: zu ⟦x = 3⟧ gehört ⟦y = 9⟧ | Anwendung | `funktionen.quadratisch` |
| 10 | y = 2ˣ: zu ⟦x = 3⟧ gehört ⟦y = 8⟧ | Anwendung | `funktionen.exponential_log` |

#### Wachstum (`id.funktionen.wachstum`) – läuft über die Klassen 5, 8, 10

> **Plus gleich viel gibt eine Gerade, mal gleich viel eine steile Kurve.**

**In jeder Zeile markiert:** Der Schritt von einem Wert zum nächsten.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | Preis für 1, 2, 3 kg: 2,50 €; 5 €; 7,50 € – immer ⟦+ 2,50 €⟧ | Vorwissen | `groessen.proportional` |
| 6 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 7 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 8 | y = 1 + 2x: 1; 3; 5; 7 – immer ⟦+ 2⟧ | Einführung | `funktionen.linear` |
| 9 | *kommt nicht vor – kein Thema der App in dieser Klasse (quadratisch wächst weder in gleichen Schritten noch mit gleichem Faktor)* | – | – |
| 10 | y = 2ˣ: 1; 2; 4; 8 – immer ⟦· 2⟧ | Einführung | `funktionen.exponential_log` |

#### Gleichung und Form (`id.funktionen.gleichung_form`) – läuft über die Klassen 8, 9, 10

> **Die Gleichung verrät die Form: x gibt eine Gerade, x² eine Parabel.**

**In jeder Zeile markiert:** Die Stelle in der Gleichung, die die Form bestimmt.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 6 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 7 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 8 | y = 2 · ⟦x⟧ + 1: Gerade | Einführung | `funktionen.linear` |
| 8 | y = 1 : ⟦x⟧: Hyperbel | Einführung | `funktionen.gebrochen` |
| 9 | y = ⟦x²⟧: Parabel | Einführung | `funktionen.quadratisch` |
| 10 | y = ⟦x³⟧ − 4x: drei Nullstellen | Einführung | `funktionen.ganzrational` |

### Planet „Daten und Zufall“

#### Kennzahl (`id.daten.kennzahl`) – läuft über die Klassen 6, 7

> **Eine Zahl für viele – und immer geht etwas verloren.**

**In jeder Zeile markiert:** Die eine Zahl, die für alle steht.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 6 | 4, 5, 5, 6: Mittelwert ⟦5⟧ | Einführung | `daten.kennwerte` |
| 7 | 2, 3, 3, 4, 18: Median ⟦3⟧, Mittelwert 6 | Einführung | `daten.boxplot` |
| 8 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 9 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 10 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |

#### Vom Teil aufs Ganze (`id.daten.teil_ganzes`) – läuft über die Klassen 8, 10

> **Wenige sagen nur etwas über alle, wenn der Zufall sie auswählt.**

**In jeder Zeile markiert:** Der Anteil in der Stichprobe – er schätzt den Anteil im Ganzen.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 6 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 7 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 8 | 30 von 100 gezogenen Kugeln rot: ⟦30 %⟧ | Einführung | `stochastik.grundbegriffe` |
| 9 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 10 | 493 Treffer in 1 000 Versuchen: ⟦49,3 %⟧ | Anwendung | `stochastik.simulation` |

#### Anteil (`id.daten.anteil`) – läuft über die Klassen 5, 8, 9, 10

> **Wahrscheinlichkeit: günstige durch mögliche.**

**In jeder Zeile markiert:** Die Zahl der Möglichkeiten – ab Klasse 8 mit den günstigen davor.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | 3 Hosen, 2 Hemden: 3 · 2 = ⟦6⟧ Möglichkeiten | Vorwissen | `stochastik.kombinatorik` |
| 6 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 7 | *kommt nicht vor – kein Thema der App in dieser Klasse* | – | – |
| 8 | Würfel, gerade Zahl: ⟦3 von 6⟧ = ½ | Einführung | `stochastik.grundbegriffe` |
| 9 | Würfel, gerade oder über 4: ⟦4 von 6⟧ = ⅔ | Anwendung | `stochastik.verknuepft` |
| 10 | Zweimal Kopf: ⟦1 von 4⟧ = ¼ | Anwendung | `stochastik.mehrstufig` |

#### Stufen (`id.daten.stufen`) – kommt nur in Klasse 10 vor

> **Am Pfad entlang mal, Pfade zusammen plus.**

**In jeder Zeile markiert:** Das Mal entlang des Pfades.

| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |
|---|---|---|---|
| 5 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 6 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 7 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 8 | *kommt nicht vor – der Stoff dafür beginnt später* | – | – |
| 9 | *kommt nicht vor – der Stoff dafür beginnt später (Klasse 9 arbeitet mit der Vierfeldertafel, noch ohne Pfade)* | – | – |
| 10 | Kopf, dann Zahl: ½ ⟦·⟧ ½ = ¼ | Einführung | `stochastik.mehrstufig` |
| 10 | Genau einmal Kopf: ¼ ⟦+⟧ ¼ = ½ | Einführung | `stochastik.mehrstufig` |

## Nicht geprüft

- Die Beispiele sind fachlich nachgerechnet; ob ein Kind an ihnen „es ist dasselbe“ wirklich sieht, ist nicht erprobt.
- „Kommt nicht vor“ ist an den Themen der App entschieden, nicht am Unterricht einer Schule.
- Klassen der Realschule und des IB sind in den Leitern nicht eigens ausgeführt.
