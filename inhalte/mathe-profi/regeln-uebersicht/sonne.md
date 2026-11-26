# Gesetzbuch · Die Sonne: die 14 Rechenregeln – ausgearbeitet

Mathe-Profi, 26.11.2026. Erzeugt von `bauen.py`; jedes Beispiel ist nachgerechnet (71 Beispiele, Lauf „OK“).
Die Sonne ist die Mitte des Gesetzbuchs: Diese Regeln gelten von Klasse 5 bis 10 unverändert, nur das Gewand wechselt (Zahl, Bruch, Buchstabe, Bruchterm, Wurzel). Das ganze Gesetzbuch mit allen Gebieten steht in `inhalt.md`.
**[G]** gesichert · **[A]** Annahme · **[M]** Meinung.

**Aus 15 werden 14:** „Einsetzen und Probe“ ist keine Rechenregel, sondern eine Arbeitsweise, und steht jetzt dort. [M]

## Die 14 Merksätze

1. **Stellenwert und Prozent:** Mal 10 schiebt jede Ziffer eine Stelle nach links, geteilt durch 10 eine nach rechts. Prozent heißt Hundertstel.
2. **Plus und Minus mit negativen Zahlen:** Plus geht nach rechts, Minus nach links. Ein Minus in der Klammer dreht die Richtung um.
3. **Vorzeichen bei Mal und Geteilt:** Minus mal Minus gibt Plus. Plus mal Minus gibt Minus.
4. **Reihenfolge beim Rechnen:** Klammer zuerst, dann Hoch, dann Punkt, dann Strich.
5. **Tauschen und Zusammenfassen:** Bei Plus und Mal darfst du tauschen, bei Minus und Geteilt nicht. Zusammenfassen darfst du nur Gleiches.
6. **Ausmultiplizieren und Ausklammern:** Der Faktor vor der Klammer trifft jeden in der Klammer.
7. **Minus vor der Klammer:** Minus vor der Klammer dreht jedes Zeichen in der Klammer um.
8. **Potenzen:** Hoch heißt: so oft mit sich selbst malnehmen. Gleiche Basis mal gleiche Basis: Hochzahlen addieren.
9. **Erweitern und Kürzen:** Zähler und Nenner mit derselben Zahl malnehmen oder durch dieselbe Zahl teilen: Der Bruch behält seinen Wert.
10. **Rechnen mit Brüchen:** Plus und Minus: erst gleicher Nenner. Mal: Zähler mal Zähler, Nenner mal Nenner. Geteilt: mal den Kehrbruch.
11. **Verhältnis (Dreisatz):** Erst auf eins, dann auf viele.
12. **Gegenrechnung:** Jede Rechnung hat eine Gegenrechnung: Plus und Minus, Mal und Geteilt, Quadrat und Wurzel.
13. **Gleichung als Waage:** Eine Gleichung ist eine Waage: Was du links tust, musst du auch rechts tun.
14. **Nullprodukt:** Ein Produkt ist null, wenn ein Faktor null ist – und nur dann.

Namen sind die üblichen Schulwörter. „Zeichen-Paar“, „Wert bleibt“, „Richtung“ und „Verteilen“ aus den früheren Papieren kommen nicht mehr vor.

## Dieselbe Regel in vielen Klassen

Jeder Punkt ist ein nachgerechnetes Beispiel aus einem Thema dieser Klasse (Abschnitt „Die Regeln einzeln“).

| Regel | Kl. 5 | Kl. 6 | Kl. 7 | Kl. 8 | Kl. 9 | Kl. 10 |
|---|---|---|---|---|---|---|
| 1 Stellenwert und Prozent | ● | ● | ● | ● |  | ● |
| 2 Plus und Minus mit negativen Zahlen | ● | ● | ● | ● | ● |  |
| 3 Vorzeichen bei Mal und Geteilt | ● | ● | ● | ● | ● | ● |
| 4 Reihenfolge beim Rechnen | ● | ● | ● | ● | ● | ● |
| 5 Tauschen und Zusammenfassen | ● | ● | ● | ● | ● |  |
| 6 Ausmultiplizieren und Ausklammern | ● | ● | ● | ● | ● | ● |
| 7 Minus vor der Klammer | ● |  | ● | ● | ● |  |
| 8 Potenzen | ● | ● | ● | ● | ● | ● |
| 9 Erweitern und Kürzen |  | ● | ● | ● | ● |  |
| 10 Rechnen mit Brüchen |  | ● | ● | ● |  | ● |
| 11 Verhältnis (Dreisatz) | ● | ● | ● | ● | ● |  |
| 12 Gegenrechnung | ● | ● | ● | ● | ● | ● |
| 13 Gleichung als Waage | ● |  | ● | ● | ● | ● |
| 14 Nullprodukt | ● |  |  | ● | ● | ● |

12 der 14 Regeln beginnen in Klasse 5, die übrigen 2 in Klasse 6 mit den Brüchen. Jede reicht mindestens bis Klasse 9. [G, gezählt aus den Beispielen]

## Der Aufbau: Was setzt was voraus

Vier Etagen, von unten nach oben zu lesen. Eine Regel steht nie unter einer Regel, die sie braucht ([G], `bauen.py` prüft es).

| Etage | Regeln |
|---|---|
| **4 · Gleichungen** | 12 Gegenrechnung · 13 Gleichung als Waage · 14 Nullprodukt |
| **3 · Brüche und Verhältnis** | 9 Erweitern und Kürzen · 10 Rechnen mit Brüchen · 11 Verhältnis (Dreisatz) |
| **2 · Klammern und Potenzen** | 5 Tauschen und Zusammenfassen · 6 Ausmultiplizieren und Ausklammern · 7 Minus vor der Klammer · 8 Potenzen |
| **1 · Zahlen** | 1 Stellenwert und Prozent · 2 Plus und Minus mit negativen Zahlen · 3 Vorzeichen bei Mal und Geteilt · 4 Reihenfolge beim Rechnen |

Die einzelnen Abhängigkeiten:

- **3 Vorzeichen bei Mal und Geteilt** braucht: 2 Plus und Minus mit negativen Zahlen
- **5 Tauschen und Zusammenfassen** braucht: 2 Plus und Minus mit negativen Zahlen
- **6 Ausmultiplizieren und Ausklammern** braucht: 4 Reihenfolge beim Rechnen
- **7 Minus vor der Klammer** braucht: 6 Ausmultiplizieren und Ausklammern, 3 Vorzeichen bei Mal und Geteilt
- **8 Potenzen** braucht: 4 Reihenfolge beim Rechnen, 3 Vorzeichen bei Mal und Geteilt
- **9 Erweitern und Kürzen** braucht: 1 Stellenwert und Prozent
- **10 Rechnen mit Brüchen** braucht: 9 Erweitern und Kürzen
- **11 Verhältnis (Dreisatz)** braucht: 9 Erweitern und Kürzen, 1 Stellenwert und Prozent
- **12 Gegenrechnung** braucht: 4 Reihenfolge beim Rechnen
- **13 Gleichung als Waage** braucht: 12 Gegenrechnung, 6 Ausmultiplizieren und Ausklammern
- **14 Nullprodukt** braucht: 6 Ausmultiplizieren und Ausklammern, 13 Gleichung als Waage

Vorschlag für die Darstellung [M]: **ein Haus mit vier Etagen** für den Aufbau und daneben **ein Band je Regel von Klasse 5 bis 10**, auf dem in jedem Jahr das Beispiel steht. Das Haus zeigt „aufeinander aufbauend“, die Bänder zeigen „für viele Klassen dasselbe“. Nach der Klarstellung des Nutzers ist das Sonnensystem gesetzt: Dann sind die vier Etagen **vier Schichten der Sonne von innen nach außen** (Kern: Zahlen; darüber Klammern und Potenzen; darüber Brüche und Verhältnis; außen Gleichungen), und die Bänder bleiben als Strahlen von Klasse 5 bis 10.

## Die Regeln einzeln

### 1. Stellenwert und Prozent

> **Mal 10 schiebt jede Ziffer eine Stelle nach links, geteilt durch 10 eine nach rechts. Prozent heißt Hundertstel.**

**Warum das gilt:** Unser Zahlensystem zählt in Zehnerbündeln: Jede Stelle ist zehnmal so viel wert wie die Stelle rechts von ihr. Deshalb verschiebt Malnehmen mit 10 alle Ziffern, ohne sie zu ändern. Das Komma trennt nur Ganze von Zehnteln; „Prozent“ ist ein anderes Wort für Hundertstel.

**Wo es nicht gilt:** Es wird nicht „eine Null angehängt“: 2,5 · 10 ist 25, nicht 2,50. Beim Runden entscheidet die Ziffer rechts von der Rundungsstelle (ab 5 aufrunden).

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 5 | 3 400 m = 3,4 km | `groessen.einheiten` |
| 6 | 15 % von 240 = 0,15 · 240 = 36 | `bruch.prozent` |
| 7 | 20 % mehr heißt mal 1,2: aus 50 € werden 60 € | `bruch.prozent_grundwert` |
| 8 | 3 · 10⁻⁴ = 0,0003 | `terme.potenzgesetze_ganzzahlig` |
| 10 | Jedes Jahr 5 % mehr heißt jedes Jahr mal 1,05 | `funktionen.exponential_log` |

**Baut auf:** nichts – Fundament
**Bild (gewählt):** Stellenwerttafel, in der die Ziffern 2 und 5 beim Malnehmen mit 10 gemeinsam ein Fach nach links rutschen – das Komma bleibt stehen.
**Verworfen:** „Null anhängen“ (falsch bei Kommazahlen); wanderndes Komma (zeigt die Wirkung, nicht den Grund).

### 2. Plus und Minus mit negativen Zahlen

> **Plus geht nach rechts, Minus nach links. Ein Minus in der Klammer dreht die Richtung um.**

**Warum das gilt:** Auf der Zahlengeraden ist Addieren ein Schritt nach rechts und Subtrahieren ein Schritt nach links. Eine negative Zahl ist ein Schritt in die Gegenrichtung. Wer eine negative Zahl abzieht, dreht also zweimal um und geht nach rechts: 9 − (−5) = 9 + 5.

**Wo es nicht gilt:** Die Regel sagt nichts über die Größe: −30 ist kleiner als −10, obwohl 30 größer ist als 10. Der Betrag ist der Abstand zur Null und nie negativ.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 5 | (−7) + 4 = −3 · 9 − (−5) = 14 | `zahlen.ganz` |
| 6 | −½ − ¾ = −1¼ | `bruch.rechnen` |
| 7 | 3x − 5x = −2x | `terme.umformen` |
| 8 | x + 5 < 2, also x < −3 | `gleichungen.ungleichungen` |
| 9 | Die Wurzel aus x² ist der Betrag von x: aus (−3)² wird 3 | `zahlen.reell` |

**Baut auf:** nichts – Fundament
**Bild (gewählt):** Zahlengerade mit einer Figur: Sie steht auf der 9, schaut nach links (Minus), dreht sich wegen der (−5) um und geht fünf Schritte nach rechts.
**Verworfen:** Schulden und Guthaben (trägt beim Abziehen von Schulden schlecht); Thermometer (gut für das Vergleichen, schwach für „minus minus“).

### 3. Vorzeichen bei Mal und Geteilt

> **Minus mal Minus gibt Plus. Plus mal Minus gibt Minus.**

**Warum das gilt:** Setzt man die Reihe 3 · (−2) = −6, 2 · (−2) = −4, 1 · (−2) = −2, 0 · (−2) = 0 fort, wächst das Ergebnis jedes Mal um 2. Also muss (−1) · (−2) = 2 sein. Nur so bleiben alle anderen Rechengesetze gültig. Für Geteilt gilt dasselbe, weil Teilen die Gegenrechnung zum Malnehmen ist.

**Wo es nicht gilt:** Gilt nur bei Mal und Geteilt, nicht bei Plus: (−3) + (−4) ist −7, nicht +7. Bei Ungleichungen dreht Malnehmen mit einer negativen Zahl das Ungleichheitszeichen um.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 5 | (−3) · (−4) = 12 | `zahlen.rechengesetze` |
| 6 | (−⅔) · ¾ = −½ | `bruch.rechnen` |
| 7 | (−2x) · (−3) = 6x | `terme.umformen` |
| 8 | −2x < 6, also x > −3 | `gleichungen.ungleichungen` |
| 9 | x² = 25 hat zwei Lösungen: 5 und −5 | `gleichungen.quadratisch` |
| 10 | (−2)³ = −8: Eine ungerade Hochzahl behält das Minus | `funktionen.ganzrational` |

**Baut auf:** Plus und Minus mit negativen Zahlen
**Bild (gewählt):** Die Musterreihe als Treppe: vier Stufen abwärts von −6 bis 0 – und die nächste Stufe landet zwingend bei +2.
**Verworfen:** Vierfeldertafel der Zeichen (richtig, aber erklärt nichts); „Feind meines Feindes“ (merkbar, aber kein Grund).

### 4. Reihenfolge beim Rechnen

> **Klammer zuerst, dann Hoch, dann Punkt, dann Strich.**

**Warum das gilt:** Die Reihenfolge ist eine Vereinbarung, damit jeder dieselbe Rechnung gleich liest. Sie folgt dem Aufbau: Hoch ist wiederholtes Malnehmen, Mal ist wiederholtes Addieren – die „stärkere“ Rechnung bindet enger. Klammern sind das Mittel, die Reihenfolge zu ändern.

**Wo es nicht gilt:** Die zuletzt ausgeführte Rechnung gibt dem Term seinen Namen: 2 + 3x ist eine Summe. Deshalb darf man 2 + 3x nicht zu 5x zusammenziehen.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 5 | 2 + 3 · 4 = 14, nicht 20 | `zahlen.rechengesetze` |
| 6 | ½ + ½ · ½ = ¾ | `bruch.rechnen` |
| 7 | 2 + 3x ist eine Summe, nicht 5x | `terme.umformen` |
| 8 | 3 · 2⁻² = ¾, nicht 6⁻² | `terme.potenzgesetze_ganzzahlig` |
| 9 | −3² = −9, aber (−3)² = 9 | `gleichungen.quadratisch` |
| 10 | 2 · 3² = 18, nicht 6² = 36: Hoch kommt vor Mal | `gleichungen.exponential` |

**Baut auf:** nichts – Fundament
**Bild (gewählt):** Vier Treppenstufen von oben nach unten: Klammer, Hoch, Punkt, Strich. Daneben 2 + 3 · 4 mit einem Rahmen um 3 · 4.
**Verworfen:** Kunstwort aus Anfangsbuchstaben (merkt sich, erklärt nichts); Ampel (keine Rangfolge erkennbar).

### 5. Tauschen und Zusammenfassen

> **Bei Plus und Mal darfst du tauschen, bei Minus und Geteilt nicht. Zusammenfassen darfst du nur Gleiches.**

**Warum das gilt:** Bei einer Summe und bei einem Produkt kommt es nicht auf die Reihenfolge an: 3 + 5 und 5 + 3 sind dieselbe Menge. Beim Abziehen und Teilen schon: 5 − 3 ist nicht 3 − 5. Wer jede Zahl mit ihrem Rechenzeichen zusammen verschiebt, darf trotzdem umstellen. Zusammenfassen heißt zählen: 3 Äpfel und 4 Äpfel sind 7 Äpfel – 3 Äpfel und 4 Birnen bleiben getrennt.

**Wo es nicht gilt:** 3a + 4b lässt sich nicht zusammenfassen, 3a · 4b schon (12ab). a und a² sind nicht „Gleiches“.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 5 | 25 · 37 · 4 = 25 · 4 · 37 = 3 700 | `zahlen.rechengesetze` |
| 6 | 0,5 · 7 · 2 = 0,5 · 2 · 7 = 7 | `bruch.dezimal` |
| 7 | 3a + 2b + 4a = 7a + 2b | `terme.umformen` |
| 8 | a³ · b · a⁻¹ = a² · b | `terme.potenzgesetze_ganzzahlig` |
| 9 | 3 · √2 + 2 · √2 = 5 · √2 (nur gleiche Wurzeln) | `zahlen.reell` |

**Baut auf:** Plus und Minus mit negativen Zahlen
**Bild (gewählt):** Zwei Körbe: In einen wandern alle x, in den anderen alle Zahlen. Jedes Teil trägt sein Rechenzeichen wie ein Etikett mit.
**Verworfen:** Äpfel und Birnen allein (zeigt das Zusammenfassen, nicht das Tauschen).

### 6. Ausmultiplizieren und Ausklammern

> **Der Faktor vor der Klammer trifft jeden in der Klammer.**

**Warum das gilt:** Ein Rechteck mit den Seiten a und (b + c) hat dieselbe Fläche wie die zwei Teilrechtecke a · b und a · c zusammen. Rückwärts gelesen ist es das Ausklammern: Steckt in jedem Summanden derselbe Faktor, darf man ihn vor eine Klammer ziehen.

**Wo es nicht gilt:** Gilt für Mal vor einer Summe, nicht für Hoch: (a + b)² ist nicht a² + b². Das Rechteckbild zeigt warum – es fehlen zwei Rechtecke a · b.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 5 | 6 · 98 = 6 · 100 − 6 · 2 = 588 | `zahlen.rechengesetze` |
| 6 | 4 · 2,5 = 4 · 2 + 4 · 0,5 = 10 | `bruch.dezimal` |
| 7 | 3 · (x + 2) = 3x + 6 · (a + b)² = a² + 2ab + b² | `terme.umformen` |
| 8 | (3x + 6) : (x + 2) = 3 · (x + 2) : (x + 2) = 3 | `terme.bruchterme` |
| 9 | x² + 5x = x · (x + 5) | `gleichungen.quadratisch` |
| 10 | x³ − 4x = x · (x² − 4) | `gleichungen.polynom` |

**Baut auf:** Reihenfolge beim Rechnen
**Bild (gewählt):** Ein Rechteck, durch einen Strich in zwei Teile geteilt: Breite a, Längen b und c. Darunter dasselbe Bild für (a + b)² mit vier Feldern.
**Verworfen:** Pfeile vom Faktor zu jedem Summanden (gut als Rechenhilfe, aber ohne Grund); Verteilen von Bonbons (trägt nicht bis zu Buchstaben).

### 7. Minus vor der Klammer

> **Minus vor der Klammer dreht jedes Zeichen in der Klammer um.**

**Warum das gilt:** Ein Minus vor der Klammer heißt „mal (−1)“. Nach der Regel „der Faktor trifft jeden“ wird jeder Summand mit −1 malgenommen, also wechselt jedes Vorzeichen. Im Alltag: Wer 20 € hat und einen Einkauf von 8 € mit 3 € Rabatt bezahlt, hat 20 − 8 + 3 € übrig.

**Wo es nicht gilt:** Ein Plus vor der Klammer ändert nichts. Die Regel ist keine neue Regel, sondern folgt aus den beiden Regeln davor – sie steht eigens da, weil hier die meisten Fehler entstehen.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 5 | 20 − (8 − 3) = 20 − 8 + 3 = 15 (in Klasse 5 nur zum Nachrechnen) | `zahlen.rechengesetze` |
| 7 | 5x − (3x − 2) = 2x + 2 | `terme.umformen` |
| 8 | 7 − 2 · (x − 3) = 7 − 2x + 6 | `gleichungen.bruch` |
| 9 | (x + 1)² − (x² − 3) = 2x + 4 | `gleichungen.quadratisch` |

**Baut auf:** Ausmultiplizieren und Ausklammern, Vorzeichen bei Mal und Geteilt
**Bild (gewählt):** Kassenzettel: 20 € − (8 € − 3 € Rabatt). Der Rabatt in der Klammer wird beim Auflösen zu + 3 €.
**Verworfen:** Vorzeichen-Wechsel als Schalter (zeigt nur das Was); Spiegel (führt in die Irre).

### 8. Potenzen

> **Hoch heißt: so oft mit sich selbst malnehmen. Gleiche Basis mal gleiche Basis: Hochzahlen addieren.**

**Warum das gilt:** 2³ · 2² ist (2 · 2 · 2) · (2 · 2) – zusammen fünf Zweien, also 2⁵. Teilt man, fallen Faktoren weg; deshalb werden die Hochzahlen abgezogen. Setzt man das fort, ergibt sich 2⁰ = 1 und 2⁻¹ = ½: Eine negative Hochzahl heißt Kehrwert.

**Wo es nicht gilt:** Gilt nur bei gleicher Basis und nur bei Mal: 2³ + 2² ist nicht 2⁵. Und a · a ist a², nicht 2a. Eine negative Hochzahl macht die Zahl nicht negativ.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 5 | 2⁵ = 2 · 2 · 2 · 2 · 2 = 32 | `zahlen.potenzen_basis` |
| 6 | 10³ · 10² = 10⁵ | `terme.potenzgesetze` |
| 7 | x² · x³ = x⁵ | `terme.potenzgesetze_natuerlich` |
| 8 | a⁻² = 1 : a² | `terme.potenzgesetze_ganzzahlig` |
| 9 | 9 hoch ½ ist die Wurzel aus 9, also 3 | `zahlen.rationale_exponenten` |
| 10 | 2ˣ · 2³ = 2 hoch (x + 3) | `funktionen.exponential_log` |

**Baut auf:** Reihenfolge beim Rechnen, Vorzeichen bei Mal und Geteilt
**Bild (gewählt):** Faltblatt: einmal falten 2 Lagen, zweimal 4, dreimal 8. Darunter die Reihe 8, 4, 2, 1, ½, ¼ mit den Hochzahlen 3, 2, 1, 0, −1, −2.
**Verworfen:** Turm aus Würfeln (zeigt Wachstum, nicht das Gesetz); Schachbrett mit Reiskörnern (schön, aber nur die Größe).

### 9. Erweitern und Kürzen

> **Zähler und Nenner mit derselben Zahl malnehmen oder durch dieselbe Zahl teilen: Der Bruch behält seinen Wert.**

**Warum das gilt:** Der Nenner sagt, in wie viele gleiche Teile das Ganze geschnitten ist, der Zähler, wie viele davon gemeint sind. Schneidet man jedes Teil noch einmal durch, gibt es doppelt so viele Teile und man nimmt doppelt so viele – die Menge bleibt gleich: ½ = 2/4.

**Wo es nicht gilt:** Kürzen darf man nur Faktoren, nie aus Summen: (x + 6) : (x + 2) ist nicht 3. Und Plus oder Minus in Zähler und Nenner ändert den Wert: 2/3 ist nicht 3/4.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 6 | 12/18 = 2/3 | `bruch.brueche` |
| 7 | 6x : 9 = 2x : 3 | `terme.umformen` |
| 8 | (3x + 6) : (x + 2) = 3, aber (x + 6) : (x + 2) lässt sich nicht kürzen | `terme.bruchterme` |
| 9 | Seitenverhältnis 6 : 9 ist dasselbe wie 2 : 3 | `abbildungen.aehnlichkeit` |

**Baut auf:** Stellenwert und Prozent
**Bild (gewählt):** Dieselbe Pizza dreimal: in 2, in 4 und in 8 Stücke geschnitten – jedes Mal ist dieselbe Hälfte gefärbt.
**Verworfen:** Bruchstreifen (genauso gut, aber weniger einprägsam); Formel a/b = ac/bc (richtig, aber kein Bild).

### 10. Rechnen mit Brüchen

> **Plus und Minus: erst gleicher Nenner. Mal: Zähler mal Zähler, Nenner mal Nenner. Geteilt: mal den Kehrbruch.**

**Warum das gilt:** Addieren kann man nur gleich große Teile – Drittel und Halbe müssen erst in Sechstel umgerechnet werden. „Mal ½“ heißt „die Hälfte von“; deshalb werden beim Malnehmen die Teile feiner (Nenner mal Nenner). Teilen fragt „wie oft passt es hinein“: In 6 passt ½ zwölfmal – das ist dasselbe wie 6 mal 2.

**Wo es nicht gilt:** Nie Zähler plus Zähler und Nenner plus Nenner: ½ + ⅓ ist nicht 2/5. Beim Malnehmen braucht man keinen gemeinsamen Nenner.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 6 | ½ + ⅓ = 3/6 + 2/6 = 5/6 · 6 : ½ = 12 | `bruch.rechnen` |
| 7 | x/2 + x/3 = 5x/6 | `gleichungen.linear` |
| 8 | 2/x + 3/(x + 1) = (5x + 2) : (x · (x + 1)) | `terme.bruchterme` |
| 10 | Zweimal Kopf: ½ · ½ = ¼ | `stochastik.mehrstufig` |

**Baut auf:** Erweitern und Kürzen
**Bild (gewählt):** Zwei gleich lange Streifen: einer halbiert, einer gedrittelt. Darunter beide in Sechstel geteilt – drei Sechstel und zwei Sechstel liegen nebeneinander.
**Verworfen:** Zwei Pizzen (unterschiedliche Stückgrößen sind schlecht zu sehen); Rechenregel als Kasten (kein Grund sichtbar).

### 11. Verhältnis (Dreisatz)

> **Erst auf eins, dann auf viele.**

**Warum das gilt:** Wenn zwei Größen im selben Verhältnis wachsen, kostet jede Einheit gleich viel. Wer den Wert für eine Einheit kennt, kennt jeden anderen: 3 kg kosten 7,50 €, also 1 kg 2,50 €, also 5 kg 12,50 €. Dieselbe Idee steckt in Prozent (Wert je Hundertstel), in der Steigung einer Geraden (Höhe je Schritt nach rechts) und im Maßstab.

**Wo es nicht gilt:** Gilt nur, wenn nichts Festes dazukommt: Mit Grundgebühr stimmt es nicht mehr. Und es gibt das Gegenstück: Bei „je mehr, desto weniger“ (doppelt so viele Helfer, halbe Zeit) bleibt das Produkt gleich, nicht das Verhältnis.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 5 | 3 kg kosten 7,50 €, 1 kg kostet 2,50 €, 5 kg kosten 12,50 € | `groessen.proportional` |
| 6 | 15 von 60 sind 25 % | `bruch.prozent` |
| 7 | 80 % sind 48 €, 1 % sind 0,60 €, 100 % sind 60 € | `bruch.prozent_grundwert` |
| 8 | Steigung 1,5: je 2 nach rechts geht es 3 nach oben | `funktionen.linear` |
| 9 | Strahlensatz: 2 : 3 = 4 : x, also x = 6 | `abbildungen.aehnlichkeit` |

**Baut auf:** Erweitern und Kürzen, Stellenwert und Prozent
**Bild (gewählt):** Drei Zeilen untereinander: 3 kg – 7,50 €, 1 kg – 2,50 €, 5 kg – 12,50 €, mit Pfeilen „geteilt durch 3“ und „mal 5“ auf beiden Seiten. Daneben ein Steigungsdreieck: 1 nach rechts, 2,5 nach oben.
**Verworfen:** Kreuz-Schema „über Kreuz malnehmen“ (schnell, aber blind); Waage (schon vergeben).

### 12. Gegenrechnung

> **Jede Rechnung hat eine Gegenrechnung: Plus und Minus, Mal und Geteilt, Quadrat und Wurzel.**

**Warum das gilt:** Die Gegenrechnung macht eine Rechnung rückgängig. Wer weiß, was mit einer Zahl gemacht wurde, findet sie, indem er rückwärts geht und jede Rechnung umkehrt – die letzte zuerst. In Klasse 10 kommt ein viertes Paar dazu: Hoch und Logarithmus.

**Wo es nicht gilt:** Rückwärts in umgekehrter Reihenfolge: Was zuletzt gerechnet wurde, kommt zuerst weg. Beim Quadrat gibt es zwei Wege zurück: x² = 49 hat die Lösungen 7 und −7. Durch null teilen hat keine Gegenrechnung.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 5 | 4 · (□ − 12) = −20: erst : 4, dann + 12, also □ = 7 | `gleichungen.einfach` |
| 6 | ¾ von einer Zahl sind 12: Die Zahl ist 12 : ¾ = 16 | `bruch.rechnen` |
| 7 | Nach 20 % Aufschlag kostet es 60 €: vorher 60 : 1,2 = 50 € | `bruch.prozent_grundwert` |
| 8 | A = g · h : 2 nach h: erst mal 2, dann durch g | `gleichungen.formeln` |
| 9 | x² = 49, also x = 7 oder x = −7 | `gleichungen.quadratisch` |
| 10 | 2ˣ = 8, also x = 3 (Logarithmus) | `gleichungen.exponential` |

**Baut auf:** Reihenfolge beim Rechnen
**Bild (gewählt):** Eine Zahl geht durch zwei Maschinen („− 12“, dann „· 4“) und kommt als −20 heraus. Darunter derselbe Weg rückwärts: „: 4“, dann „+ 12“.
**Verworfen:** Hin- und Rückweg auf einer Straße (gleichwertig, weniger genau bei der Reihenfolge); Reißverschluss.

### 13. Gleichung als Waage

> **Eine Gleichung ist eine Waage: Was du links tust, musst du auch rechts tun.**

**Warum das gilt:** Das Gleichheitszeichen sagt: Links und rechts steht gleich viel. Nimmt man auf beiden Seiten dasselbe weg oder verdoppelt beide Seiten, bleibt die Waage im Gleichgewicht – die Gleichung hat danach dieselbe Lösung. Welche Rechnung man wählt, sagt die Gegenrechnung.

**Wo es nicht gilt:** „Auf beiden Seiten“ heißt: die ganze Seite. Beim Malnehmen und Teilen trifft es jeden Summanden. Mit null malnehmen oder durch einen Term teilen, der null sein kann, zerstört die Gleichung. Bei Ungleichungen dreht mal oder geteilt durch eine negative Zahl das Zeichen um.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 5 | □ + 7 = 3: auf beiden Seiten 7 abziehen, □ = −4 | `gleichungen.einfach` |
| 7 | 2x + 2 = 12, also 2x = 10, also x = 5 | `gleichungen.linear` |
| 8 | 3/x + ½ = 5/x: beide Seiten mal 2x, dann 6 + x = 10, x = 4 | `gleichungen.bruch` |
| 9 | 2x² = 18, also x² = 9 | `gleichungen.quadratisch` |
| 10 | 3 · 2ˣ = 24, also 2ˣ = 8 | `gleichungen.exponential` |

**Baut auf:** Gegenrechnung, Ausmultiplizieren und Ausklammern
**Bild (gewählt):** Balkenwaage: links zwei Säckchen x und zwei Kugeln, rechts zwölf Kugeln. Auf beiden Seiten werden zwei Kugeln weggenommen, dann beide Seiten halbiert.
**Verworfen:** „Rüberbringen und Zeichen wechseln“ (führt zu Fehlern bei Mal und Geteilt); Wippe.

### 14. Nullprodukt

> **Ein Produkt ist null, wenn ein Faktor null ist – und nur dann.**

**Warum das gilt:** Null mal irgendetwas ist null. Umgekehrt kann aus zwei Zahlen, die beide nicht null sind, beim Malnehmen nie null werden. Deshalb darf man eine Gleichung „Produkt = 0“ in mehrere einfache Gleichungen zerlegen: Jeder Faktor für sich kann null sein.

**Wo es nicht gilt:** Gilt nur für null: Aus (x − 2) · (x + 3) = 6 folgt nicht x − 2 = 6. Erst alles auf eine Seite bringen, dann ausklammern.

| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |
|---|---|---|
| 5 | 0 · 7 = 0 · und: durch 0 kann man nicht teilen | `zahlen.rechengesetze` |
| 8 | Der Nenner x · (x − 4) ist null für x = 0 oder x = 4 | `terme.bruchterme` |
| 9 | (x − 2) · (x + 3) = 0, also x = 2 oder x = −3 | `gleichungen.quadratisch` |
| 10 | x³ − 4x = x · (x − 2) · (x + 2) = 0, also x = 0, 2 oder −2 | `gleichungen.polynom` |

**Baut auf:** Ausmultiplizieren und Ausklammern, Gleichung als Waage
**Bild (gewählt):** Eine Kette aus zwei Gliedern, die an der Null hängt: Reißt ein Glied (ist es null), fällt alles auf null.
**Verworfen:** Lichtschalter in Reihe (passt, aber fremd für Klasse 5); Dominosteine.

## Fehlt beim Rechnen etwas?

Keine eigene Regel, aber fünf Dinge, die bisher nicht ausdrücklich dastanden. Sie sind jetzt eingeordnet:

| Was | Wo es jetzt steht | Warum keine eigene Regel |
|---|---|---|
| Runden | Regel 1 Stellenwert (unter „Wo es nicht gilt“) | eine Vereinbarung über die Ziffer rechts daneben |
| Überschlag | Arbeitsweise | ein Vorgehen, kein Gesetz |
| Betrag | Regel 2 Plus und Minus | Abstand zur Null auf der Zahlengeraden |
| Ungleichung umdrehen | Regel 3 Vorzeichen und Regel 13 Waage | Folge aus „mal Minus“ |
| Wurzel und Logarithmus | Regel 12 Gegenrechnung (als Paare), ihre Gesetze unter „Sätze und Formeln“ | Gegenrechnungen zu Quadrat und Hoch; die Gesetze folgen aus den Potenzen |

Alles Weitere – die Gesetze der Gebiete und die Arbeitsweisen – steht in `inhalt.md`.

## Für die Technik

Nummern der Übersicht und Nummern in den Aufgaben-Etiketten (`schritt1/etiketten.json`): 1 = Etikett 13 · 2 = Etikett 1 · 3 = Etikett 2 · 4 = Etikett 3 · 5 = Etikett 6 · 6 = Etikett 4 · 7 = Etikett 5 · 8 = Etikett 12 · 9 = Etikett 10 · 10 = Etikett 11 · 11 = Etikett 14 · 12 = Etikett 8 · 13 = Etikett 7 · 14 = Etikett 15. Etikett 9 „Einsetzen und Probe“ ist jetzt die Arbeitsweise „Probe“; die Etiketten bleiben gültig.

## Nicht geprüft

- **Lehrplan:** Die Klasse jedes Beispiels ist gegen `inhalte/themenliste.json` geprüft (Gymnasium Bayern, Zuordnung der App), **nicht gegen den Lehrplan an der Quelle**. Die vier Widersprüche zwischen Themenliste und App aus dem Lehrplan-Auftrag betreffen keines der Beispiele.
- „Minus vor der Klammer“ in Klasse 5: Das Thema gehört zur Klasse, erklärt die Regel aber nicht; das Beispiel ist dort nur zum Nachrechnen gedacht.
- Realschule und IB: Die Beispiele folgen den Gymnasium-Klassen. Bei der Realschule liegen einige Themen ein Jahr früher oder später.
- Ob ein Kind der Klasse 5 die Merksätze versteht und behält – nicht erprobt.
- Die Bilder sind beschrieben, nicht gezeichnet.

## Annahmen

- Die Übersicht soll alle Klassen 5 bis 10 zeigen, auch wenn die Kinder erst in 5 und 8 sind.
- „Professionell“ heißt: fachlich richtig, mit Grund und Grenze, in üblichen Schulwörtern.
- 14 statt 15 ist ein Vorschlag; die alte Zählung lässt sich ohne Verlust wiederherstellen.
