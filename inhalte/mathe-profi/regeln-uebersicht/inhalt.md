# Gesetzbuch der Mathematik, Klasse 5 bis 10 – Landkarte und vollständiges Inhaltsverzeichnis

Mathe-Profi, 26.11.2026 (Auftrag 10, nach der Klarstellung „Gesetzbuch“). Erzeugt von `gesetzbuch.py`.
Für ChatGPT zum Angreifen und für den Designer als Stoff. Noch keine Darstellung.
**[G]** gesichert · **[A]** Annahme · **[M]** Meinung.

| Datei | Inhalt | Stand |
|---|---|---|
| `inhalt.md` (diese Datei) | Landkarte, ehrliche Gesamtzahl, alle Gesetze je Gebiet mit Klasse und Schulart | vollständig |
| `sonne.md` | die 14 Rechenregeln, ausgearbeitet | Muster 1 |
| `planet-flaeche-und-raum.md` | ein Planet, ausgearbeitet | Muster 2 |
| `gesetzbuch.py`, `bauen.py` | Daten, Prüfungen, Erzeugung | Lauf „OK“ |

## Die Antwort in einer Minute

- **Das Gesetzbuch hat 174 Einträge:** 14 Rechenregeln (die Sonne), 152 Gesetze in sieben Gebieten und auf den Entdecker-Inseln (die Planeten), 8 Arbeitsweisen (eigener Ort).
- **Die Sonne** sind die Rechenregeln, weil sie in jedem Gebiet wiederkehren: 80 der 152 Gesetze brauchen mindestens eine von ihnen ([G], gezählt).
- **Die Planeten sind die Gebiete der App.** Der Schnitt trägt – mit einer Einschränkung, siehe unten.
- Jedes der 97 Themen der App ist von mindestens einem Gesetz oder einer Rechenregel erfasst ([G], `gesetzbuch.py` prüft es).
- **Ehrlich zur Zahl:** 152 ist die Zahl der Gesetze, wie ich sie geschnitten habe. Manche Einträge bündeln mehrere Formeln (die drei binomischen Formeln, die drei Potenzgesetze, vier Kongruenzsätze). Zählt man jede Formel einzeln, sind es deutlich mehr. Wer feiner oder gröber schneidet, kommt auf eine andere Zahl; an der Größenordnung ändert das nichts.

## Die Landkarte

| Ort | Gesetze | Lage | Abschnitte |
|---|---|---|---|
| **Sonne: Rechenregeln** | 14 | Mitte | Zahlen · Klammern und Potenzen · Brüche und Verhältnis · Gleichungen |
| Zahlen | 24 | innerster Planet | Zahlen schreiben und ordnen, Teilbarkeit, Brüche und Dezimalzahlen, Potenzen, Wurzeln, Logarithmen |
| Algebra | 23 | zweiter Planet | Terme, Gleichungen ersten Grades, Gleichungen höheren Grades |
| Geld und Verhältnisse | 11 | dritter Planet | Größen, Proportionalität, Prozent und Zins |
| Geometrie | 30 | vierter Planet | Lage und Winkel, Figuren und Konstruktion, Abbilden, Ähnlichkeit und rechtwinkliges Dreieck |
| Fläche und Raum | 19 | fünfter Planet | Flächen, Körper |
| Funktionen | 20 | sechster Planet | Grundbegriffe, Funktionsarten |
| Daten und Zufall | 20 | siebter Planet | Daten, Zählen und Zufall |
| Entdecker-Inseln | 5 | Kleinplaneten am Rand | Nur IB – Kür |
| **Arbeitsweisen** | 8 | eigener Ort – Vorschlag: die Raumstation, die jeden Planeten anfliegt | – |

**Trägt der Schnitt „Planet = Gebiet der App“?** Ja, mit drei Anmerkungen:
1. **Zahlen und Algebra liegen der Sonne am nächsten.** Viele ihrer Gesetze sind Rechenregeln in einem bestimmten Gewand oder folgen aus ihnen (Spalte „braucht aus der Sonne“). Das ist kein Fehler des Schnitts, sondern der Grund für die Reihenfolge der Planeten: von innen (nah am Rechnen) nach außen (eigene Sätze).
2. **Die Grenzen sind an wenigen Stellen unscharf.** 1 Gesetz steht bei mir auf einem anderen Planeten als alle seine Themen in der App ([G], Liste unten); weitere 13 Gesetze greifen auf Themen aus zwei Gebieten zu (zum Beispiel die Hyperbel: Funktionen und Verhältnisse). Ich habe nach dem Inhalt geordnet, nicht nach dem Flug.
3. **Die Entdecker-Inseln** sind kein Gebiet, sondern fünf einzelne IB-Themen. Im Gesetzbuch sind sie Kleinplaneten am Rand, ausdrücklich Kür.

Wann die Gesetze dazukommen (Gymnasium, erste Klasse, in der das Gesetz vorkommt) [G]: Klasse 5: 30 · Klasse 6: 19 · Klasse 7: 21 · Klasse 8: 28 · Klasse 9: 26 · Klasse 10: 12 · ohne Gymnasium-Zuordnung (nur Realschule oder IB): 16.

## Die Sonne: 14 Rechenregeln

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

Ausgearbeitet in `sonne.md`: je Regel Merksatz, Warum, Wo es nicht gilt, ein Beispiel je Klasse, Aufbau, Bild.

## Das vollständige Inhaltsverzeichnis

Spalten **G / R / I**: Klasse, in der das Gesetz laut App vorkommt – Gymnasium Bayern / Realschule Bayern (Wahlpflichtfächergruppe I) / IB-MYP-Jahr. „5–8“ heißt: Es kommt in mehreren Themen von Klasse 5 bis 8 vor. „–“ heißt: in dieser Schulart nicht zugeordnet.
Die Zahlen in der letzten Spalte sind die Nummern der Rechenregeln.

### Zahlen – 24 Gesetze (innerster Planet)

| Nr. | Gesetz | In einem Satz | G | R | I | braucht aus der Sonne |
|---|---|---|---|---|---|---|
| | *Zahlen schreiben und ordnen* | | | | | |
| Z1 | **Stellenwertsystem** | Jede Stelle ist zehnmal so viel wert wie die Stelle rechts daneben – auch hinter dem Komma. | 5–6 | 5–6 | 1 | 1 |
| Z2 | **Runden** | Die Ziffer rechts von der Rundungsstelle entscheidet: 0 bis 4 abrunden, 5 bis 9 aufrunden. | 5–6 | 5–6 | 1 | 1 |
| Z3 | **Andere Zahlschriften** | Römische Zahlen reihen Zeichen aneinander; das Zweiersystem bündelt in Zweiern statt in Zehnern. | 5 | 5 | 1 | – |
| Z4 | **Ordnung auf der Zahlengeraden** | Was weiter links liegt, ist kleiner – auch bei negativen Zahlen und Brüchen. | 5–6 | 5–6 | 1–2 | 2 |
| Z5 | **Betrag und Gegenzahl** | Der Betrag ist der Abstand zur Null. Die Gegenzahl liegt gleich weit auf der anderen Seite. | 5 | 5 | 2–5 | 2 |
| | *Teilbarkeit* | | | | | |
| Z6 | **Teiler und Vielfache** | a ist Teiler von b, wenn b geteilt durch a ohne Rest aufgeht. | 5 | 5 | 1 | – |
| Z7 | **Teilbarkeitsregeln** | Durch 2, 5 und 10: letzte Ziffer ansehen. Durch 3 und 9: Quersumme ansehen. | 5 | 5 | 1 | 1 |
| Z8 | **Primzahlen und Primfaktoren** | Jede Zahl größer als 1 lässt sich auf genau eine Weise in Primzahlen zerlegen. | 5 | 5 | 1 | – |
| Z9 | **ggT und kgV** | Der größte gemeinsame Teiler kürzt vollständig, das kleinste gemeinsame Vielfache ist der Hauptnenner. | 6 | 6 | 1 | 9 |
| | *Brüche und Dezimalzahlen* | | | | | |
| Z10 | **Bruch als Anteil** | Der Nenner teilt, der Zähler zählt. Anteil = Teil durch Ganzes. | 6 | 6 | 1 | – |
| Z11 | **Brüche vergleichen** | Bei gleichem Nenner ist der Bruch mit dem größeren Zähler größer; sonst erst gleichnamig machen. | 6 | 6 | 1 | 9 |
| Z12 | **Drei Schreibweisen einer Zahl** | Bruch, Dezimalzahl und Prozent sagen dasselbe: ½ = 0,5 = 50 %. | 6 | 6 | 1 | 1 |
| Z13 | **Periodische Dezimalzahlen** | Jeder Bruch wird als Dezimalzahl endlich oder periodisch – nie etwas anderes. | 6 | 6 | 1 | – |
| Z14 | **Rechnen mit Komma** | Mal: Nachkommastellen zusammenzählen. Geteilt: das Komma in beiden Zahlen gleich weit verschieben. | 6 | 6 | 2 | 1 |
| | *Potenzen, Wurzeln, Logarithmen* | | | | | |
| Z15 | **Quadratzahlen** | Hoch 2 heißt Zahl mal sich selbst; die Quadratzahlen bis 20² weiß man auswendig. | 5 | 5 | 1 | 8 |
| Z16 | **Potenz mit negativer Basis** | Gerade Hochzahl: Ergebnis positiv. Ungerade Hochzahl: Ergebnis negativ. | 5 | 5 | 1 | 3, 8 |
| Z17 | **Hoch null und negative Hochzahl** | a⁰ = 1. Eine negative Hochzahl heißt Kehrwert: a⁻ⁿ = 1 : aⁿ. | 6–8 | 7 | 3–4 | 8 |
| Z18 | **Zehnerpotenzen** | 10ⁿ ist eine 1 mit n Nullen, 10⁻ⁿ hat n Stellen hinter dem Komma. Kilo, Mega, Milli, Mikro sind Zehnerpotenzen. | 5–6 | 5–7 | 1–4 | 1, 8 |
| Z19 | **Potenzgesetze** | Gleiche Basis: Hochzahlen addieren. Gleiche Hochzahl: Basen malnehmen. Potenz der Potenz: Hochzahlen malnehmen. | 7–9 | 7–10 | 3–5 | 8 |
| Z20 | **Quadratwurzel** | Die Wurzel aus a ist die Zahl ab null, deren Quadrat a ist. Aus negativen Zahlen gibt es keine. | 9 | 9 | 1 | 12 |
| Z21 | **Wurzelgesetze** | Wurzel mal Wurzel ist Wurzel aus dem Produkt, Wurzel durch Wurzel ist Wurzel aus dem Quotienten – nicht bei Plus und Minus. | 9 | 9 | 4 | 8 |
| Z22 | **Irrationale und reelle Zahlen** | Manche Zahlen sind kein Bruch, zum Beispiel √2. Brüche und diese Zahlen zusammen heißen reelle Zahlen. | 9 | 9 | 4 | – |
| Z23 | **n-te Wurzel und Bruch als Hochzahl** | a hoch 1/n ist die n-te Wurzel aus a. | 9 | 10 | 5 | 8, 12 |
| Z24 | **Logarithmus** | Der Logarithmus ist die gesuchte Hochzahl. Aus Mal wird Plus, aus Hoch wird Mal. | 10 | 10 | 5 | 8, 12 |

### Algebra – 23 Gesetze (zweiter Planet)

| Nr. | Gesetz | In einem Satz | G | R | I | braucht aus der Sonne |
|---|---|---|---|---|---|---|
| | *Terme* | | | | | |
| A1 | **Term und Variable** | Ein Buchstabe steht für eine Zahl. Die zuletzt ausgeführte Rechnung gibt dem Term seinen Namen. | 7 | 6 | 1 | 4 |
| A2 | **Gleichwertige Terme** | Zwei Terme sind gleichwertig, wenn sie für jede eingesetzte Zahl denselben Wert haben. | 7 | 7 | 3 | – |
| A3 | **Summe mal Summe** | Jedes Glied der ersten Klammer mal jedes Glied der zweiten. | 7 | 7 | 3 | 6 |
| A4 | **Binomische Formeln** | (a + b)² = a² + 2ab + b² · (a − b)² = a² − 2ab + b² · (a + b)(a − b) = a² − b² | 7 | 7–8 | 3 | 6 |
| A5 | **Definitionsmenge** | Ein Nenner darf nie null sein. Diese Zahlen werden vorher ausgeschlossen. | 8 | 8 | 4 | 14 |
| A6 | **Bruchterme** | Mit Bruchtermen rechnet man wie mit Brüchen: erst faktorisieren, dann kürzen. | 8 | 8 | 4 | 9, 10 |
| A7 | **Kleinster und größter Wert** | (x − d)² + e ist nie kleiner als e und wird es genau bei x = d. | – | 8 | – | 6 |
| | *Gleichungen ersten Grades* | | | | | |
| A8 | **Äquivalenzumformung** | Dieselbe Rechnung auf beiden Seiten ändert die Lösung nicht – außer mal null und geteilt durch null. | 5–7 | 6–7 | 1–2 | 13 |
| A9 | **Wie viele Lösungen?** | Eine lineare Gleichung hat genau eine Lösung, keine oder jede Zahl als Lösung. | 5–7 | 6–7 | 1–2 | – |
| A10 | **Ungleichungen** | Mal oder geteilt durch eine negative Zahl dreht das Ungleichheitszeichen um. | 8 | 7 | 4 | 3, 13 |
| A11 | **Intervalle** | Eckige Klammer: Die Grenze gehört dazu. Nach außen gedrehte oder runde Klammer: Sie gehört nicht dazu. | 8 | 7 | 4 | – |
| A12 | **Bruchgleichungen** | Mit dem Hauptnenner malnehmen; die Lösung muss in der Definitionsmenge liegen. Bruch gleich Bruch: über Kreuz. | 8 | 8 | 4 | 10, 13 |
| A13 | **Formeln umstellen** | Eine Formel ist eine Gleichung mit mehreren Buchstaben: nach dem gesuchten auflösen. | 8 | – | 4 | 12, 13 |
| A14 | **Gleichungssystem mit zwei Unbekannten** | Gesucht ist das Zahlenpaar, das beide Gleichungen erfüllt: einsetzen, gleichsetzen oder addieren. Zwei Geraden schneiden sich, sind parallel oder gleich. | 8 | 9 | 4 | 13 |
| A15 | **Gleichungssystem mit drei Unbekannten** | Erst eine Unbekannte entfernen, dann von unten nach oben einsetzen. | 9 | – | – | 13 |
| | *Gleichungen höheren Grades* | | | | | |
| A16 | **x² = a** | Zwei Lösungen, wenn a positiv ist (Wurzel und Gegenzahl), eine bei a = 0, keine bei negativem a. | 9 | 9 | 4 | 12 |
| A17 | **Faktorisieren** | Alles auf eine Seite, ausklammern, dann jeden Faktor gleich null setzen. | 9–10 | 9 | 4 | 6, 14 |
| A18 | **Quadratische Ergänzung** | Zum Binom ergänzen, was fehlt – und es gleich wieder abziehen. | 9 | 8–9 | 4 | 6 |
| A19 | **Lösungsformel** | Die Lösungsformel löst jede quadratische Gleichung. Der Ausdruck unter der Wurzel entscheidet: positiv zwei Lösungen, null eine, negativ keine. | 9 | 9 | 4 | 12 |
| A20 | **Wurzelgleichungen** | Quadrieren kann falsche Lösungen erzeugen. Die Probe ist Pflicht. | – | 9 | – | 12 |
| A21 | **Potenzgleichungen** | xⁿ = c: bei gerader Hochzahl zwei Lösungen oder keine, bei ungerader genau eine. | 9 | 10 | 4 | 3, 12 |
| A22 | **Exponentialgleichungen** | Gleiche Basis: Hochzahlen gleichsetzen. Sonst hilft der Logarithmus. | 10 | 10 | 5 | 12 |
| A23 | **Polynomgleichungen** | Ausklammern oder x² ersetzen. Eine doppelte Lösung berührt die Achse nur. | 10 | – | – | 6, 14 |

### Geld und Verhältnisse – 11 Gesetze (dritter Planet)

| Nr. | Gesetz | In einem Satz | G | R | I | braucht aus der Sonne |
|---|---|---|---|---|---|---|
| | *Größen* | | | | | |
| V1 | **Größe und Einheit** | Eine Größe ist Zahl mal Einheit. Umrechnungszahlen: Längen 10 (und 1 000 bis km), Massen 1 000, Zeit 60. | 5 | 5 | 2 | 1 |
| V2 | **Maßstab** | 1 : n heißt: 1 cm im Plan sind n cm in Wirklichkeit. | 5 | 5 | 2 | 11 |
| | *Proportionalität* | | | | | |
| V3 | **Direkte Proportionalität** | Doppelt so viel von dem einen, doppelt so viel von dem anderen. Der Quotient bleibt gleich. | 5–8 | 6–8 | 2–3 | 11 |
| V4 | **Dreisatz** | Erst auf eins, dann auf viele. | 5 | 6 | 2 | 11 |
| V5 | **Verhältnisse** | a : b lässt sich kürzen wie ein Bruch. Aufteilen im Verhältnis: erst die Teile zusammenzählen. | 6 | 6 | 1 | 9 |
| V6 | **Indirekte Proportionalität** | Doppelt so viel von dem einen, halb so viel von dem anderen. Das Produkt bleibt gleich. | 8 | 7 | 4 | 11 |
| V7 | **Änderungsrate** | Änderung je Einheit: Unterschied der Werte durch Unterschied der Schritte. | 5 | 6 | 2 | 11 |
| | *Prozent und Zins* | | | | | |
| V8 | **Grundgleichung der Prozentrechnung** | Prozentwert = Prozentsatz mal Grundwert. Zwei der drei Größen bestimmen die dritte. | 6 | 6 | 1 | 1, 12 |
| V9 | **Wachstumsfaktor** | Plus p % heißt mal (1 + p/100), minus p % heißt mal (1 − p/100). Erst plus 10 %, dann minus 10 % ist nicht wieder der Anfang. | 7 | 7 | 3 | 1 |
| V10 | **Zinsen** | Jahreszinsen = Kapital mal Zinssatz. Für Monate nimmt man den Anteil am Jahr. | 6 | 7 | 4 | 1 |
| V11 | **Zinseszins** | Kapital nach n Jahren = Anfangskapital mal Wachstumsfaktor hoch n. | 7 | 7 | 3 | 8 |

### Geometrie – 30 Gesetze (vierter Planet)

| Nr. | Gesetz | In einem Satz | G | R | I | braucht aus der Sonne |
|---|---|---|---|---|---|---|
| | *Lage und Winkel* | | | | | |
| G1 | **Koordinatensystem** | Punkt (x | y): erst nach rechts oder links, dann nach oben oder unten. | 5 | 5 | 1 | – |
| G2 | **Parallel, senkrecht, Abstand** | Der Abstand ist die kürzeste Verbindung – sie steht senkrecht. | 5 | 5 | 1 | – |
| G3 | **Winkelarten** | Voller Winkel 360°, gestreckter 180°, rechter 90°. | 5 | 5 | 1 | – |
| G4 | **Scheitel- und Nebenwinkel** | Scheitelwinkel sind gleich groß. Nebenwinkel ergeben zusammen 180°. | 5–7 | 5–7 | 1–2 | – |
| G5 | **Stufen- und Wechselwinkel** | An parallelen Geraden sind Stufenwinkel und Wechselwinkel gleich groß – und umgekehrt. | 7 | 7 | 2 | – |
| G6 | **Winkelsumme** | Im Dreieck 180°, im Viereck 360°, im n-Eck (n − 2) mal 180°. Ein Außenwinkel ist so groß wie die beiden anderen Innenwinkel zusammen. | 7 | 7 | 2 | – |
| | *Figuren und Konstruktion* | | | | | |
| G7 | **Besondere Vierecke** | Quadrat, Rechteck, Raute, Parallelogramm, Trapez, Drachenviereck: Jedes hat seine festen Eigenschaften. | 5–7 | 5–7 | 1–3 | – |
| G8 | **Ortslinien** | Kreis: gleich weit von einem Punkt. Mittelsenkrechte: gleich weit von zwei Punkten. Winkelhalbierende: gleich weit von zwei Schenkeln. | 5–7 | 6–7 | 3 | – |
| G9 | **Gleichschenkliges Dreieck** | Gleiche Schenkel, gleiche Basiswinkel – und umgekehrt. Gleichseitig: dreimal 60°. | 7 | 7 | 3 | – |
| G10 | **Kongruenzsätze** | Drei passende Angaben legen ein Dreieck fest: SSS, SWS, WSW, SsW. Zwei Seiten sind zusammen immer länger als die dritte. | 7 | 7 | 3 | – |
| G11 | **Satz und Kehrsatz** | Die Umkehrung eines Satzes ist ein neuer Satz und muss eigens begründet werden. | 7 | 7 | 3–4 | – |
| G12 | **Satz des Thales** | Liegt die Ecke auf dem Halbkreis über einer Seite, hat das Dreieck dort einen rechten Winkel – und umgekehrt. | 7 | 7 | 4 | – |
| G13 | **Tangente** | Die Tangente steht senkrecht auf dem Radius zum Berührpunkt. | 7 | 7 | 4 | – |
| G14 | **Umkreis und Inkreis** | Umkreis-Mittelpunkt: Schnitt der Mittelsenkrechten. Inkreis-Mittelpunkt: Schnitt der Winkelhalbierenden. | 7 | 7 | 4 | – |
| | *Abbilden* | | | | | |
| G15 | **Spiegeln, Verschieben, Drehen** | Diese Abbildungen ändern weder Längen noch Winkel: Bild und Original sind deckungsgleich. | 7 | 6 | 3 | – |
| G16 | **Symmetrie** | Achsensymmetrisch: Spiegeln an der Achse ändert nichts. Punktsymmetrisch: halbe Drehung ändert nichts. | 7 | 6 | 3 | – |
| G17 | **Vektoren** | Ein Vektor ist eine Verschiebung: Spitze minus Fuß. Der Gegenvektor führt zurück. | 7 | 6 | 3 | 2 |
| G18 | **Fläche mit Determinante** | Zwei Vektoren spannen ein Parallelogramm auf; seine Fläche ist der Betrag von a·d − b·c. | – | 7 | – | – |
| G19 | **Matrizen und Skalarprodukt** | Eine Matrix beschreibt eine Abbildung. Skalarprodukt null heißt senkrecht. | – | 10 | 5 | – |
| | *Ähnlichkeit und rechtwinkliges Dreieck* | | | | | |
| G20 | **Ähnlichkeit** | Ähnliche Figuren haben gleiche Winkel und alle Seiten im selben Verhältnis. | 9 | 9 | 3 | 11 |
| G21 | **Strahlensätze** | Schneiden Parallelen zwei Strahlen, stehen die Abschnitte im selben Verhältnis. | 9 | 9 | 3 | 11 |
| G22 | **Vergrößern mit Faktor k** | Längen mal k, Flächen mal k², Volumen mal k³. | 8–9 | 9 | 3 | 8 |
| G23 | **Schwerpunkt** | Die Seitenhalbierenden schneiden sich im Schwerpunkt; er teilt sie im Verhältnis 2 : 1. | 9 | 9 | 3 | 11 |
| G24 | **Satz des Pythagoras** | Im rechtwinkligen Dreieck gilt a² + b² = c² – und nur dort. | 9 | 9 | 3 | 12 |
| G25 | **Sinus, Kosinus, Tangens** | Sinus = Gegenkathete durch Hypotenuse, Kosinus = Ankathete durch Hypotenuse, Tangens = Gegenkathete durch Ankathete. | 9 | 9 | 4 | 11 |
| G26 | **Zusammenhänge der Winkelfunktionen** | sin² + cos² = 1 und tan = sin : cos. | 9 | 9 | 4 | – |
| G27 | **Einheitskreis** | Am Kreis mit Radius 1 sind Kosinus und Sinus die Koordinaten des Punktes – für jeden Winkel. | 9 | 10 | 4 | – |
| G28 | **Sinussatz und Kosinussatz** | In jedem Dreieck: Seite durch Sinus des Gegenwinkels ist für alle drei gleich. Der Kosinussatz ist Pythagoras mit Korrektur. | 9 | 10 | 4 | – |
| G29 | **Additionstheoreme** | Der Sinus einer Summe ist nicht die Summe der Sinus: sin(α + β) = sin α · cos β + cos α · sin β. | 9 | 10 | 4 | – |
| G30 | **Winkel aus Sinus oder Kosinus** | Zu einem Wert gehören in einer vollen Drehung meist zwei Winkel. | 9 | 10 | 5 | 12 |

### Fläche und Raum – 19 Gesetze (fünfter Planet)

| Nr. | Gesetz | In einem Satz | G | R | I | braucht aus der Sonne |
|---|---|---|---|---|---|---|
| | *Flächen* | | | | | |
| F1 | **Fläche messen** | Flächeninhalt heißt: Wie viele Einheitsquadrate passen hinein? Umrechnungszahl 100. | 5 | 5 | 1 | 1 |
| F2 | **Rechteck** | Fläche = Länge mal Breite. Umfang = einmal außen herum. | 5 | 5 | 1 | – |
| F3 | **Fläche ist nicht Umfang** | Gleicher Umfang heißt nicht gleiche Fläche. | 5 | 5–8 | 1 | – |
| F4 | **Zerlegen und Ergänzen** | Zerschneiden und neu zusammenlegen ändert die Fläche nicht. | 5–6 | 5–6 | 1 | – |
| F5 | **Parallelogramm** | Fläche = Grundseite mal Höhe. Die Höhe steht senkrecht. | 6 | 6 | – | – |
| F6 | **Dreieck** | Fläche = Grundseite mal Höhe, geteilt durch 2. | 6–8 | 6 | 4 | – |
| F7 | **Trapez** | Fläche = Mittelwert der beiden parallelen Seiten mal Höhe. | 6–8 | 6 | 4 | – |
| F8 | **Drachenviereck und Raute** | Fläche = Diagonale mal Diagonale, geteilt durch 2. | 6 | 6 | – | – |
| F9 | **Kreis** | Umfang = 2 · π · r. Fläche = π · r². π ist etwas mehr als 3. | 8 | 9 | 3 | – |
| F10 | **Kreisausschnitt** | Der Anteil am vollen Winkel ist der Anteil an Umfang und Fläche. | 8 | 9 | 3 | 11 |
| | *Körper* | | | | | |
| F11 | **Volumen messen** | Volumen heißt: Wie viele Einheitswürfel passen hinein? Umrechnungszahl 1 000. 1 Liter = 1 dm³. | 6 | 6 | – | 1 |
| F12 | **Quader** | Volumen = Länge mal Breite mal Höhe. | 6 | 6 | – | – |
| F13 | **Oberfläche** | Die Oberfläche ist die Summe aller Flächen des Netzes. Quader: sechs Rechtecke, je zwei gleich. | 5–6 | 6 | 1 | – |
| F14 | **Netz und Schrägbild** | Das Netz ist der aufgeklappte Körper. Im Schrägbild werden Kanten nach hinten schräg und verkürzt gezeichnet. | 8–10 | 5–7 | 3–4 | – |
| F15 | **Prisma und Zylinder** | Volumen = Grundfläche mal Höhe. Oberfläche = zwei Grundflächen plus Mantel. | 8 | 9 | – | – |
| F16 | **Satz von Cavalieri** | Gleiche Höhe und auf jeder Höhe gleich große Schnittfläche: gleiches Volumen. | 8 | 9 | – | – |
| F17 | **Pyramide und Kegel** | Volumen = ein Drittel von Grundfläche mal Höhe. | 10 | 9 | 3 | – |
| F18 | **Kugel** | Volumen = 4/3 · π · r³. Oberfläche = 4 · π · r². | 10 | 9 | 3 | – |
| F19 | **Lage im Raum** | Zwei Geraden im Raum sind parallel, schneiden sich oder laufen windschief aneinander vorbei. | 10 | 7 | 4 | – |

### Funktionen – 20 Gesetze (sechster Planet)

| Nr. | Gesetz | In einem Satz | G | R | I | braucht aus der Sonne |
|---|---|---|---|---|---|---|
| | *Grundbegriffe* | | | | | |
| U1 | **Funktion** | Zu jedem x gehört genau ein y. | 8 | 8 | 3 | – |
| U2 | **Punktprobe** | Ein Punkt liegt auf dem Graphen, wenn seine Koordinaten die Gleichung erfüllen. | 8–9 | 8–9 | 3–4 | – |
| U3 | **Nullstelle und Achsenabschnitt** | Nullstelle: y = 0. Schnitt mit der y-Achse: x = 0. | 8 | 8 | 3–4 | 13 |
| U4 | **Schnittpunkt** | Im Schnittpunkt haben beide Funktionen denselben Wert: gleichsetzen. | 8–9 | 8–9 | 3–4 | 13 |
| U5 | **Graphen verschieben und strecken** | Plus e schiebt nach oben, (x − d) schiebt nach rechts, mal a streckt, ein Minus davor spiegelt. | 8–10 | 9–10 | 4–5 | – |
| U6 | **Umkehrfunktion** | x und y tauschen; der Graph wird an der Geraden y = x gespiegelt. Geht nur, wenn zu jedem y genau ein x gehört. | 9 | 10 | 4 | 12 |
| | *Funktionsarten* | | | | | |
| U7 | **Lineare Funktion** | y = m · x + t: m ist die Steigung (Höhenunterschied durch Längenunterschied), t der Abschnitt auf der y-Achse. | 8 | 8 | 3 | 11 |
| U8 | **Ursprungsgerade** | Proportional heißt: Gerade durch den Ursprung. | 8 | 8 | 3 | 11 |
| U9 | **Parallel und senkrecht** | Parallele Geraden haben dieselbe Steigung. Senkrechte: Die Steigungen ergeben malgenommen −1. | 8 | 8 | 3 | – |
| U10 | **Geradenscharen** | Ein Parameter in m dreht die Gerade, ein Parameter in t verschiebt sie. | 8 | 8 | 3 | – |
| U11 | **Hyperbel** | y = a : x: doppeltes x, halbes y. Der Graph kommt den Asymptoten beliebig nahe, erreicht sie aber nie. | 8 | 7 | 4 | 11 |
| U12 | **Parabel** | y = a · (x − d)² + e hat den Scheitel (d | e). a entscheidet über Öffnung und Breite. | 9 | 9 | 4 | 6 |
| U13 | **Potenzfunktionen** | Gerade Hochzahl: symmetrisch zur y-Achse. Ungerade Hochzahl: symmetrisch zum Ursprung. | 9 | 10 | 4 | 8 |
| U14 | **Exponentialfunktion** | Exponentiell: In gleichen Schritten wird mit derselben Zahl malgenommen. Linear: Es kommt dieselbe Zahl dazu. | 10 | 10 | 5 | 8 |
| U15 | **Logarithmusfunktion** | Sie ist die Umkehrung der Exponentialfunktion. | 10 | 10 | 5 | 12 |
| U16 | **Sinus- und Kosinusfunktion** | Sie wiederholen sich nach 360° (im Bogenmaß 2π). Die Amplitude ist die größte Auslenkung. 180° entsprechen π. | 10 | 10 | 5 | – |
| U17 | **Ganzrationale Funktionen** | Die höchste Hochzahl bestimmt, wohin der Graph außen läuft. Die Produktform zeigt die Nullstellen. | 10 | – | 5 | 14 |
| U18 | **Betragsfunktion** | Der Graph hat einen Knick. |x| = a hat die Lösungen a und −a. | – | – | 5 | 2 |
| U19 | **Folgen** | Arithmetisch: immer dieselbe Zahl dazu. Geometrisch: immer mit derselben Zahl mal. | – | – | 5 | – |
| U20 | **Reihen** | Arithmetische Reihe: Anzahl mal Mittelwert aus erstem und letztem Glied. Für die geometrische gibt es eine eigene Summenformel. | – | – | 5 | – |

### Daten und Zufall – 20 Gesetze (siebter Planet)

| Nr. | Gesetz | In einem Satz | G | R | I | braucht aus der Sonne |
|---|---|---|---|---|---|---|
| | *Daten* | | | | | |
| D1 | **Häufigkeit** | Absolute Häufigkeit: wie oft. Relative Häufigkeit: Anzahl durch Gesamtzahl. | 6–8 | 5–9 | 1–2 | 11 |
| D2 | **Diagramme lesen** | Im Kreisdiagramm gehört zu jedem Anteil derselbe Anteil von 360°. Eine Achse, die nicht bei 0 beginnt, übertreibt Unterschiede. | 6 | 5 | 1 | 11 |
| D3 | **Mittelwert** | Alle Werte addieren, durch die Anzahl teilen. | 6 | 7 | 2 | – |
| D4 | **Median, Modalwert, Spannweite** | Median: der Wert in der Mitte der geordneten Liste. Modalwert: der häufigste. Spannweite: größter minus kleinster. | 7 | 7 | 4 | – |
| D5 | **Mittelwert oder Median** | Ein Ausreißer zieht den Mittelwert mit, den Median nicht. | 7 | 7 | 4 | – |
| D6 | **Quartile und Boxplot** | Die Box enthält die mittlere Hälfte der Werte. | 7 | 7 | 4 | – |
| D7 | **Stichprobe** | Eine Stichprobe taugt nur, wenn sie zufällig gezogen und groß genug ist. | – | 7 | 2 | 11 |
| D8 | **Zusammenhang ist nicht Ursache** | Zwei Größen können zusammen steigen, ohne dass die eine die andere bewirkt. | – | – | 5 | – |
| D9 | **Streuung** | Die Standardabweichung misst, wie weit die Werte im Mittel vom Mittelwert entfernt liegen. | – | – | 5 | 12 |
| D10 | **Normalverteilung** | Etwa 68 % der Werte liegen höchstens eine Standardabweichung vom Mittelwert entfernt, 95 % höchstens zwei. | – | – | 5 | – |
| | *Zählen und Zufall* | | | | | |
| D11 | **Zählprinzip** | Die Möglichkeiten der einzelnen Stufen werden malgenommen. | 5 | 5 | 2 | – |
| D12 | **Ergebnis und Ereignis** | Ein Ereignis ist eine Menge von Ergebnissen. | 8 | 9 | 2 | – |
| D13 | **Laplace-Wahrscheinlichkeit** | Günstige durch mögliche Ergebnisse – nur wenn alle gleich wahrscheinlich sind. | 8 | 9 | 2 | 11 |
| D14 | **Gegenereignis** | Jede Wahrscheinlichkeit liegt zwischen 0 und 1. Gegenereignis: 1 minus die Wahrscheinlichkeit. | 8–10 | 9–10 | 2–4 | – |
| D15 | **Gesetz der großen Zahlen** | Bei sehr vielen Versuchen nähert sich die relative Häufigkeit der Wahrscheinlichkeit. | 8–10 | 9 | 2 | – |
| D16 | **Additionssatz** | Entweder-oder: Wahrscheinlichkeiten addieren und das doppelt Gezählte abziehen. | 9 | 9 | 4 | – |
| D17 | **Vierfeldertafel** | Zeilen und Spalten ergeben die Randsummen; ein Feld folgt aus den anderen. | 9 | 9 | 4 | – |
| D18 | **Bedingte Wahrscheinlichkeit** | Unter der Bedingung B zählt nur noch, was in B liegt. Unabhängig heißt: Die Bedingung ändert nichts. | 9 | 9 | 4 | 11 |
| D19 | **Pfadregeln** | Entlang eines Pfades malnehmen, mehrere Pfade addieren. | 10 | 10 | 4 | 10 |
| D20 | **Simulation** | Ein Zufallsversuch lässt sich mit Zufallszahlen nachspielen; viele Durchgänge ergeben einen Schätzwert. | 10 | 9 | 2 | – |

### Entdecker-Inseln – 5 Gesetze (Kleinplaneten am Rand)

| Nr. | Gesetz | In einem Satz | G | R | I | braucht aus der Sonne |
|---|---|---|---|---|---|---|
| | *Nur IB – Kür* | | | | | |
| E1 | **Mengen** | Schnittmenge: in beiden. Vereinigungsmenge: in mindestens einer. | – | – | – | – |
| E2 | **Aussagenlogik** | „Und“ ist nur wahr, wenn beide wahr sind. „Wenn A, dann B“ ist nur falsch, wenn A wahr und B falsch ist. | – | – | 4 | – |
| E3 | **Graphen** | Jede Kante zählt an zwei Knoten. Ein Rundweg über alle Kanten geht nur, wenn jeder Knoten gerade viele Kanten hat. | – | – | 4 | – |
| E4 | **Lineare Optimierung** | Der beste Wert liegt in einer Ecke des erlaubten Bereichs. | – | – | 5 | – |
| E5 | **Schranken** | Ein gerundeter Messwert kann eine halbe Einheit größer oder kleiner sein. | – | – | 5 | 1 |

## Die Arbeitsweisen – eigener Ort

| Arbeitsweise | Merksatz |
|---|---|
| Probe | **Setz ein und rechne nach.** |
| Überschlag | **Erst grob, dann genau.** |
| Einheiten | **Rechne mit Einheiten – die Einheit des Ergebnisses prüft die Rechnung.** |
| Skizze | **Zeichne, was du weißt.** |
| Ansatz | **Gegeben, gesucht, Rechnung, Antwort.** |
| Begründen | **Nenne den Satz, dann wende ihn an. Für „stimmt nicht“ genügt ein Gegenbeispiel.** |
| Ablesen und Darstellen | **Erst Achsen und Einheiten lesen, dann die Werte.** |
| Formel anwenden | **Formel hinschreiben, einsetzen, auflösen.** |

Sie sind keine Gesetze, sondern Vorgehen, und gelten auf jedem Planeten. „Einheiten“ ist neu dabei, wie im Auftrag genannt.

## Was bewusst nicht im Gesetzbuch steht

- **Rechenverfahren** (schriftliches Malnehmen und Teilen, Heron-Verfahren, Konstruktionsschritte): Das sind Abläufe, keine Gesetze. Sie gehören in die Lernreise.
- **Reine Begriffe** (Was ist ein Trapez, was ist ein Ereignis): nur dort aufgenommen, wo aus dem Begriff eine Regel folgt.
- **Einzelne Formeln ohne eigene Idee** (Kreisring, Kreisabschnitt, Mantel der Pyramide): Sie entstehen aus den aufgeführten Gesetzen durch Zerlegen.

## Gesetze, die auf einem anderen Planeten stehen als ihr Thema in der App

| Planet im Gesetzbuch | Gesetz | Gebiet des Themas in der App |
|---|---|---|
| Zahlen | Logarithmus | Algebra, Funktionen |

## Vorschlag für die weitere Ausarbeitung

1. Diese Datei, `sonne.md` und `planet-flaeche-und-raum.md` an ChatGPT (Schritt 2).
2. Nach dem Einarbeiten die übrigen Planeten in dieser Reihenfolge [M]: Geometrie (dort sind beide Kinder als Nächstes), Geld und Verhältnisse, Daten und Zufall, Zahlen, Algebra, Funktionen, Entdecker-Inseln.
3. Je Planet dasselbe Muster wie beim Muster-Planeten: Merksatz, Warum, Wo es nicht gilt, Beispiele je Klasse, baut auf, Bild.

## Nicht geprüft

- **Lehrplan:** Klasse und Schulart stammen aus `inhalte/themenliste.json` (Zuordnung der App), **nicht aus den Lehrplänen an der Quelle**. Die bekannten Zweifel (vier Widersprüche zur App, mehrere Realschul-Zuordnungen) gelten hier weiter.
- **Vollständigkeit gegen den Lehrplan:** Geprüft ist, dass jedes Thema der App erfasst ist. Ob in den Lehrplänen ein Gesetz steht, zu dem die App kein Thema hat, ist nicht geprüft.
- Vollständigkeit innerhalb eines Themas: Ich habe die Titel aller Etappen gelesen, nicht jede Erklärung.
- Merksätze und Bilder nicht mit einem Kind erprobt; Bilder nur beschrieben.

## Annahmen

- Sonne = Rechenregeln, Planeten = Gebiete der App (Lesart des Projektleiters, hier übernommen und geprüft).
- Ein Gesetz ist, was fest gilt und was man wissen muss: Regel, Satz, Formel oder feste Vereinbarung.
- Reihenfolge der Planeten von innen nach außen nach Nähe zum Rechnen – ein Vorschlag für den Designer.
