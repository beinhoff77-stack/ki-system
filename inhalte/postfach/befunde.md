# Postfach befunde (Dreizehnte Runde: Befundlisten aus Runde 10)

Neueste Meldung oben.

## 2026-11-16 05:57 – FERTIG (Abschlussbericht Dreizehnte Runde)
Alle Befundlisten der Klassen 8, 5, 7, 6, 9, 10 abgearbeitet: 63 Themen, je Thema ein Commit auf Zweig befunde. Summe: umgestuft 296, berichtigt (Lösung/Tipp/Weg) 21, ersetzt 95, neu ergänzt 4, nicht umgesetzt 42.

Vorgehen und Nachweis:
- Korrekturen stehen je Generator im Abschnitt „BEFUNDE“ (Werkzeug inhalte/generatoren/_befunde.py). Sie werden nach dem vollständigen Bau (inkl. Umbau und Zehnter Runde) auf die fertige Datei angewendet; jede Korrektur findet ihre Aufgabe über Lernkarte + genauen Fragetext und verlangt die erwartete Trefferzahl.
- Nachweis je Thema: `python3 -I inhalte/generatoren/_befunde_nachweis.py <thema>` vergleicht mit origin/lernen-app. Ergebnis für alle 63 Themen: NACHWEIS OK (nicht betroffene Aufgaben Zeichen für Zeichen gleich, keine Löschung, keine Umsortierung; bei Umstufung nur Feld s, bei Berichtigung nur o/h/w/c geändert; Lernkarten und Kopfdaten unverändert).
- `python3 -I tools/inhalt_pruefen.py` für alle Dateien in inhalte/themen: OK. Alle Generatoren neu ausgeführt: Ergebnis identisch mit dem Zweig.
- Nach dem Umstufen hat jede Lernkarte mindestens 3 Übungen je Stufe (vom Werkzeug geprüft); nur bei raum.schraegbilder/lage (1 neue Stufe-1-Übung) und messen.koerper_berechnung/sachaufgaben (3 neue Stufe-1-Übungen) mussten Übungen ergänzt werden.
- Einziger echter Rechenfehler der Listen (stochastik.verknuepft/verstehen: unmögliche Angaben, Lösung P(A ∪ B) = 1,03 > 1): Aufgabe ersetzt; alle übrigen Aufgaben dieses Typs nachgeprüft (P(A) + P(B) − 1 ≤ P(A ∩ B) ≤ min(P(A), P(B)) erfüllt). Den Zufallsteil des Generators habe ich nicht umgebaut, weil sich sonst alle übrigen Aufgaben des Themas mitändern würden.
- Ersetzte Aufgaben stehen an derselben Stelle im selben Pool, mit neuem Fragetext. Die alten Fragetexte unten bitte in der Datenbank sperren (sonst bleiben die fehlerhaften Fassungen aktiv). Keine Datenbank, kein App-Code, keine Tests, kein Merge.

### Liste „ersetzt“ (je Thema: Lernkarte, Pool, Stufe, alter Fragetext → neue Frage an derselben Stelle)
Die alten Fassungen bitte in der Datenbank sperren. Wo derselbe Fragetext mehrfach vorkommt, ist die gemeinte Fassung über Antworten bzw. Lösung angegeben.

Klasse 8:
- funktionen.grundbegriffe:
  - (stelle, uebung, Stufe 1) „Für welches x gilt f(x) = −3, wenn f(x) = −1(x + 1)?“ → „Für welches x gilt f(x) = −3, wenn f(x) = −(x + 1)?“
  - (stelle, uebung, Stufe 2) „Für welches x gilt f(x) = −2, wenn f(x) = −1(x + 4)?“ → „Für welches x gilt f(x) = −2, wenn f(x) = −(x + 4)?“
  - (stelle, uebung, Stufe 2) „Für welches x gilt f(x) = −4, wenn f(x) = −1(x + 4)?“ → „Für welches x gilt f(x) = −4, wenn f(x) = −(x + 4)?“
- funktionen.linear:
  - (zwei_punkte, uebung, Stufe 2) „Liegen A(−1 | −1), B(1 | 1) und C(3 | 3) auf einer Geraden?“ → „Liegen die Punkte A(−1 | −1), B(1 | 1) und C(3 | 3) auf einer gemeinsamen Geraden?“
  - (zwei_punkte, uebung, Stufe 3) „Liegen A(0 | 2), B(2 | 8) und C(4 | 14) auf einer Geraden?“ → „Liegen die Punkte A(0 | 2), B(2 | 8) und C(4 | 14) auf einer gemeinsamen Geraden?“
  - (proportional, uebung, Stufe 1) „6 m Stoff kosten 48 €. Wie viel kosten 1 m?“ → „6 m Stoff kosten 48 €. Wie viel kostet 1 m?“
  - (proportional, uebung, Stufe 1) „2 l Saft kosten 3 €. Wie viel kosten 1 l?“ → „2 l Saft kosten 3 €. Wie viel kostet 1 l?“
- gleichungen.lgs2:
  - (sachaufgabe, uebung, Stufe 3) „Ein Händler mischt Erdnüsse zu 10 € pro kg mit Cashewkerne zu 16 € pro kg. Er erhält 13 kg Mischung im Wert von 178 €. Wie viel kg der billigeren Sorte verwendet er?“ → „Ein Händler mischt Erdnüsse zu 10 € pro kg mit Cashewkernen zu 16 € pro kg. Er erhält 13 kg Mischung im Wert von 178 €. Wie viel kg der billigeren Sorte verwendet er?“
- gleichungen.ungleichungen:
  - (umformen, uebung, Stufe 3) „Löse 4x + 10 ≤ 4x + 3.“ → „Löse die Ungleichung 4x + 10 ≤ 4x + 3.“
  - (grafisch, uebung, Stufe 1) „Für welche x liegt der Graph von y = x + 4 oberhalb der x-Achse?“ → „Für welche x liegt der Graph von y = x + 4 echt oberhalb der x-Achse (also nicht auf ihr)?“
  - (grafisch, uebung, Stufe 1) „Für welche x liegt der Graph von y = 2x − 4 unterhalb der x-Achse?“ → „Für welche x liegt der Graph von y = 2x − 4 echt unterhalb der x-Achse (also nicht auf ihr)?“
- zahlen.intervalle:
  - (lesen, uebung, Stufe 3) „Ein Aquarium braucht Wasser von mindestens 24 °C bis höchstens 28 °C. Welches Intervall beschreibt die erlaubten Temperaturen (in °C)?“ → „Ein Impfstoff muss im Kühlschrank bei mehr als 2 °C, aber höchstens 8 °C gelagert werden. Welches Intervall beschreibt die erlaubten Temperaturen (in °C)?“
- gleichungen.formeln:
  - (ein_schritt, uebung, Stufe 3) „An einem Widerstand R = 10 Ω liegt U = 230 V. Jemand rechnet I = R : U = 0,04 A. Welche Probe zeigt den Fehler?“ → „An einem Widerstand R = 10 Ω liegt die Spannung U = 200 V. Jemand rechnet I = R : U = 0,05 A. Welche Probe zeigt den Fehler?“
- messen.koerper_darstellung:
  - (beurteilen, uebung, Stufe 2) „Welche Aussage ist richtig?“ [Text 13× vorhanden; gemeint: Auswahl mit den Antworten Eine Pyramide ist ein Prisma. | Ein sechsseitiges Prisma hat 6 Flächen. | Ein Zylinder hat genau zwei Kanten. | Im Schrägbild werden Kanten nach hinten in wahrer Länge gezeichnet.; richtig „Ein Zylinder hat genau zwei Kanten.“] → „Welche Aussage über Körper ist richtig?“
  - (beurteilen, uebung, Stufe 3) „Welche Aussage ist FALSCH?“ [Text 12× vorhanden; gemeint: Auswahl mit den Antworten Der Mantel eines geraden siebenseitigen Prismas besteht aus 7 Rechtecken. | Eine Pyramide ist ein Prisma. | Ein Zylinder hat keine Ecken. | Ein Zylinder hat genau zwei Kanten.; richtig „Eine Pyramide ist ein Prisma.“] → „Welche Aussage über Prismen und Pyramiden ist FALSCH?“
  - (beurteilen, uebung, Stufe 3) „Welche Aussage ist FALSCH?“ [Text 12× vorhanden; gemeint: Auswahl mit den Antworten Das Mantelrechteck eines Zylinders ist so lang wie der Durchmesser des Grundkreises. | Der Mantel eines geraden zwölfseitigen Prismas besteht aus 12 Rechtecken. | Ein Zylinder hat keine Ecken. | Ein Zylinder hat genau zwei Kanten.; richtig „Das Mantelrechteck eines Zylinders ist so lang wie der Durchmesser des Grundkreises.“] → „Welche Aussage über Zylinder und Prismen ist FALSCH?“
- stochastik.grundbegriffe:
  - (laplace, uebung, Stufe 1) „In einer Urne liegen 9 rote, 3 blaue und 1 grüne Kugeln. Eine wird zufällig gezogen. Wie groß ist P(grün)?“ → „In einer Urne liegen 9 rote Kugeln, 3 blaue Kugeln und 1 grüne Kugel. Eine wird zufällig gezogen. Wie groß ist P(grün)?“
  - (gegenereignis, uebung, Stufe 3) „Ein fairer Würfel hat die Zahlen 1 bis 10. Wie groß ist die Wahrscheinlichkeit, KEINE Zahl kleiner oder gleich 1 zu werfen? Gib sie als Dezimalzahl an.“ → „Ein Glücksrad hat 10 gleich große Felder mit den Zahlen 1 bis 10. Wie groß ist die Wahrscheinlichkeit, dass die Zahl NICHT durch 3 teilbar ist? Gib sie als Dezimalzahl an.“
  - (gegenereignis, uebung, Stufe 3) „Ein fairer Würfel hat die Zahlen 1 bis 6. Wie groß ist die Wahrscheinlichkeit, KEINE Zahl kleiner oder gleich 3 zu werfen? Gib sie als Dezimalzahl an.“ → „Ein Spielwürfel wird einmal geworfen. Wie groß ist die Wahrscheinlichkeit, dass KEINE Primzahl fällt? Gib sie als Dezimalzahl an.“
  - (grosse_zahlen, uebung, Stufe 3) „Ein Kronkorken landete bei 500 Würfen 225-mal mit der Öffnung nach oben. Schätze die Wahrscheinlichkeit dafür auf zwei Nachkommastellen.“ → „Anna wirft einen Kronkorken 20-mal, er landet 12-mal mit der Öffnung nach oben. Ben wirft denselben Kronkorken 500-mal, er landet 225-mal so. Welche Schätzung für P(Öffnung oben) ist besser?“
- stochastik.simulation:
  - (beurteilen, uebung, Stufe 3) „Ein Bauteil ist fehlerhaft mit p = 5/6. Simuliert wird mit einer Urne mit 7 roten von 10 Kugeln (mit Zurücklegen). Ist das geeignet?“ → „Ein Bauteil ist mit p = 0,15 fehlerhaft. Simuliert wird mit Zufallszahlen von 00 bis 99; Treffer sind die Zahlen 00 bis 15. Ist das geeignet?“
- groessen.indirekt:
  - (sach, uebung, Stufe 3) „Ein Freizeitpark: Eintritt 3 €, jede Fahrt 4 €. 3 Fahrten kosten mit Eintritt 15 €. Jemand rechnet für 6 Fahrten: 15 · 2 = 30 €. Stimmt das?“ → „Eine Handwerkerin berechnet 40 € Anfahrt und 50 € je Arbeitsstunde. 2 Stunden kosten zusammen 140 €. Jemand rechnet für 4 Stunden: 140 · 2 = 280 €. Stimmt das?“

Klasse 5:
- zahlen.potenzen_basis:
  - (quadrat, uebung, Stufe 3) „Welche Zahl ist eine Quadratzahl?“ [Text 3× vorhanden; gemeint: Auswahl mit den Antworten 124 | 121 | 22; richtig „121“] → „Welche Zahl liegt zwischen den Quadratzahlen 13² und 14²?“
- groessen.proportional:
  - (sach, uebung, Stufe 2) „Ein Hahn füllt in 4 Minuten einen Eimer mit 48 Litern. Ungefähr wie viele Liter laufen in 20 Minuten?“ → „Aus einem Hahn laufen in 4 Minuten 48 Liter Wasser, jede Minute gleich viel. Wie viele Liter laufen in 20 Minuten?“
  - (sach, test, Stufe 2) „Ein Hahn füllt in 2 Minuten einen Eimer mit 24 Litern. Ungefähr wie viele Liter laufen in 20 Minuten?“ → „Aus einem Hahn laufen in 2 Minuten 24 Liter Wasser, jede Minute gleich viel. Wie viele Liter laufen in 20 Minuten?“
- geometrie.grundbegriffe:
  - (lagebeziehungen, uebung, Stufe 3) „g geht durch A(−6 | −3) und B(−6 | 0), h geht durch C(4 | −3) und D(8 | −3). Wie liegen g und h zueinander?“ → „g geht durch A(−6 | −3) und B(−6 | 0), h geht durch C(4 | −3) und D(4 | 5). Wie liegen g und h zueinander?“
  - (kreis_lage, uebung, Stufe 3) „Zwei Kreise haben die Radien 7 cm und 4 cm. Ihre Mittelpunkte sind 3 cm voneinander entfernt. Wie viele gemeinsame Punkte haben sie?“ → „Ein Kreis um M(2 | 1) hat den Radius 4. Die waagrechte Gerade g geht durch alle Punkte mit y = −3. Wie viele gemeinsame Punkte haben Kreis und g?“
- geometrie.winkel:
  - (drehungen, uebung, Stufe 3) „Ein Karussell hat 3 Gondeln in gleichen Abständen. Um wie viel Grad muss es sich drehen, damit die nächste Gondel an die Stelle der vorigen kommt?“ → „Ein Karussell hat 8 Gondeln in gleichen Abständen. Es dreht sich um 135°. Um wie viele Gondelplätze ist es weitergerückt?“
  - (drehungen, uebung, Stufe 3) „Ein Karussell hat 5 Gondeln in gleichen Abständen. Um wie viel Grad muss es sich drehen, damit die nächste Gondel an die Stelle der vorigen kommt?“ → „Bei einem Karussell mit Gondeln in gleichen Abständen kommt nach einer Drehung um 24° die nächste Gondel an die Stelle der vorigen. Wie viele Gondeln hat es?“
  - (verstehen, uebung, Stufe 3) „Stimmt die Aussage? „Zwei stumpfe Winkel nebeneinander ergeben immer mehr als 180°.““ → „Stimmt die Aussage? „Drei spitze Winkel nebeneinander ergeben immer weniger als 270°.““
- geometrie.ortslinien:
  - (parallelen, uebung, Stufe 3) „g ist die waagrechte Gerade y = −1. Wie viele Punkte mit ganzzahligen Koordinaten auf der senkrechten Linie x = 2 haben von g höchstens den Abstand 3?“ → „g ist die waagrechte Gerade y = −1. Wie viele Punkte mit ganzzahligen Koordinaten auf der senkrechten Linie x = 2 haben von g mehr als 1, aber höchstens 3 Abstand?“
  - (zwei_kreise, uebung, Stufe 3) „Kreis um A mit r = 2 cm, Kreis um B mit r = 9 cm, [AB] = 6 cm. Wie viele Schnittpunkte haben die Kreise?“ → „Kreis um A mit r = 2 cm, Kreis um B mit r = 3 cm, [AB] = 7 cm. Wie viele Schnittpunkte haben die Kreise?“
  - (zwei_kreise, uebung, Stufe 3) „Ein großer Kreis um A hat r = 9 cm, ein kleiner Kreis um B hat r = 4 cm. B liegt im großen Kreis, [AB] = 5 cm. Wie viele gemeinsame Punkte haben die Kreise?“ → „Ein Kreis um A hat r = 6 cm, ein Kreis um B hat r = 4 cm, [AB] = 10 cm. Wie viele gemeinsame Punkte haben die Kreise?“
  - (zwei_kreise, uebung, Stufe 3) „Kreis um A mit r = 4 cm, Kreis um B mit r = 8 cm, [AB] = 4 cm. Wie viele Schnittpunkte haben die Kreise?“ → „Kreis um A mit r = 5 cm, Kreis um B mit r = 4 cm, [AB] = 7 cm. Wie viele Schnittpunkte haben die Kreise?“
  - (zwei_kreise, uebung, Stufe 3) „Ein großer Kreis um A hat r = 8 cm, ein kleiner Kreis um B hat r = 3 cm. B liegt im großen Kreis, [AB] = 5 cm. Wie viele gemeinsame Punkte haben die Kreise?“ → „Ein Kreis um A hat r = 3 cm, ein Kreis um B hat ebenfalls r = 3 cm, [AB] = 7 cm. Wie viele gemeinsame Punkte haben die Kreise?“
  - (sachsituationen, uebung, Stufe 3) „Zwei Sender A und B stehen 7 km auseinander. Ein Handy hat genau 8 km Abstand zu A und genau 4 km Abstand zu B. An wie vielen Stellen kann es sein?“ → „Zwei Sender A und B stehen 7 km auseinander. Ein Handy hat genau 2 km Abstand zu A und genau 4 km Abstand zu B. An wie vielen Stellen kann es sein?“
  - (sachsituationen, uebung, Stufe 3) „Zwei Sender A und B stehen 10 km auseinander. Ein Handy hat genau 5 km Abstand zu A und genau 6 km Abstand zu B. An wie vielen Stellen kann es sein?“ → „Zwei Sender A und B stehen 10 km auseinander. Ein Handy hat genau 4 km Abstand zu A und genau 6 km Abstand zu B. An wie vielen Stellen kann es sein?“
  - (zwei_kreise, uebung, Stufe 3) „Jemand sagt: „Kreise mit r = 3 cm und r = 5 cm, deren Mittelpunkte 1 cm auseinander liegen, schneiden sich, weil 1 cm < 3 cm + 5 cm.“ Stimmt das?“ → „Jemand sagt: „Kreise mit r = 3 cm und r = 5 cm, deren Mittelpunkte 9 cm auseinander liegen, schneiden sich, weil 9 cm > 5 cm.“ Stimmt das?“
- messen.flaechen:
  - (einheitsquadrate, uebung, Stufe 3) „Ein Rechteck aus 6 · 5 Einheitsquadraten wird in beiden Richtungen doppelt so lang. Wie viele Einheitsquadrate passen jetzt hinein?“ → „Ein Rechteck aus 4 · 3 Einheitsquadraten wird doppelt so lang und dreimal so breit. Wie viele Einheitsquadrate passen jetzt hinein?“
- messen.koerper_berechnung:
  - (oberflaeche, uebung, Stufe 3) „Ein Würfel hat die Oberfläche 486 cm². Wie lang ist eine Kante?“ → „Ein Würfel hat die Oberfläche 216 cm². Wie groß ist sein Volumen?“
  - (oberflaeche, uebung, Stufe 3) „Ein Würfel hat die Oberfläche 1014 cm². Wie lang ist eine Kante?“ → „Jede Kante eines Würfels wird doppelt so lang. Wie viel mal so groß wird seine Oberfläche?“
  - (zusammengesetzt, uebung, Stufe 3) „Zwei gleiche Quader (7 cm lang, 3 cm breit und 5 cm hoch) werden mit den 3 cm × 5 cm großen Flächen aneinandergeklebt. Wie groß ist die Oberfläche des neuen Quaders?“ → „Drei gleiche Würfel mit 2 cm Kantenlänge werden in einer Reihe aneinandergeklebt. Wie groß ist die Oberfläche des neuen Körpers?“
  - (zusammengesetzt, uebung, Stufe 3) „Zwei gleiche Quader (4 cm lang, 7 cm breit und 4 cm hoch) werden mit den 7 cm × 4 cm großen Flächen aneinandergeklebt. Wie groß ist die Oberfläche des neuen Quaders?“ → „Zwei gleiche Quader (6 cm × 4 cm × 2 cm) werden einmal mit den 6 cm × 4 cm großen Flächen und einmal mit den 4 cm × 2 cm großen Flächen aneinandergeklebt. Um wie viele cm² ist die Oberfläche im zweiten Fall größer?“
- gleichungen.einfach:
  - (probe, uebung, Stufe 3) „Bei 3 · x + 5 = 38 wird x = 12 getestet. Links kommt 41 heraus. Ist die Lösung größer oder kleiner als 12?“ → „Bei 3 · x + 5 = 38 ergibt die Probe mit x = 12 links 41 und mit x = 10 links 35. Die Lösung ist eine ganze Zahl. Welche?“
  - (probe, uebung, Stufe 3) „Bei 5 · x + 9 = 29 wird x = 3 getestet. Links kommt 24 heraus. Ist die Lösung größer oder kleiner als 3?“ → „Welche der Zahlen 2, 4, 6 und 8 löst die Gleichung 5 · x + 9 = 29? Entscheide mit der Probe.“
  - (aufstellen, uebung, Stufe 3) „Eine Mutter ist 3-mal so alt wie ihre Tochter. Zusammen sind sie 36 Jahre alt. Wie alt ist die Tochter?“ → „Ein Vater ist 28 Jahre älter als sein Sohn. Zusammen sind sie 46 Jahre alt. Wie alt ist der Sohn?“
  - (ohne_loesung, uebung, Stufe 3) „0 · x = 14. Wie viele Lösungen hat diese Gleichung?“ → „Für welche Zahl a hat die Gleichung a · x = 7 keine Lösung?“

Klasse 7:
- gleichungen.linear:
  - (probe, uebung, Stufe 3) „Jemand multipliziert 6x + 6 = 21 auf beiden Seiten mit 0 und erhält 0 = 0. Er folgert: „Jede Zahl ist eine Lösung.“ Stimmt das?“ → „Jemand multipliziert die Gleichung 6x + 6 = 21 auf beiden Seiten mit 0 und erhält 0 = 0. Er folgert: „Jede Zahl ist eine Lösung.“ Hat er recht?“
- abbildungen.kongruenz:
  - (symmetrie, uebung, Stufe 3) „Welcher Großbuchstabe (Blockschrift) ist punktsymmetrisch, hat aber keine Symmetrieachse?“ [Text 2× vorhanden; gemeint: Auswahl mit den Antworten A | X | V | N; richtig „N“] → „Welcher Großbuchstabe (Blockschrift) ist punktsymmetrisch und hat genau zwei Symmetrieachsen?“
  - (parkett, uebung, Stufe 3) „Passen 4 gleichseitige Dreiecke und ein Quadrat lückenlos um eine Ecke?“ → „Lässt sich eine Ecke lückenlos mit 4 gleichseitigen Dreiecken und einem Quadrat auslegen?“
  - (parkett, uebung, Stufe 3) „Passen 3 gleichseitige Dreiecke und 2 Quadrate lückenlos um eine Ecke?“ → „Lässt sich eine Ecke lückenlos mit 3 gleichseitigen Dreiecken und 2 Quadraten auslegen?“

Klasse 6:
- bruch.brueche:
  - (vergleichen, uebung, Stufe 3) „Um wie viel ist 5/6 größer als 4/7?“ → „Welcher Bruch liegt näher an 1: 5/6 oder 6/7?“
- bruch.dezimal:
  - (bruch_zu_dezimal, uebung, Stufe 3) „Berechne 1 + 0,5 und gib das Ergebnis als Dezimalzahl an.“ → „Berechne 3/4 + 0,5 und gib das Ergebnis als Dezimalzahl an.“
  - (bruch_zu_dezimal, uebung, Stufe 3) „Berechne 1 + 0,4 und gib das Ergebnis als Dezimalzahl an.“ → „Berechne 2/5 + 1,4 und gib das Ergebnis als Dezimalzahl an.“
  - (verstehen, uebung, Stufe 3) „Stimmt die Aussage? „Eine Zahl mit drei Nachkommastellen ist immer größer als eine mit einer, z. B. 0,37 > 0,8.““ → „Stimmt die Aussage? „Eine Zahl mit drei Nachkommastellen ist immer größer als eine mit einer, z. B. 0,375 > 0,8.““
- bruch.rechnen:
  - (vorzeichen, uebung, Stufe 3) „Berechne (−1/8) + 1/5.“ → „Berechne (−1/8) + 1/5 und gib das Ergebnis vollständig gekürzt an.“
  - (dezimal_mal, uebung, Stufe 3) „Ein Kilogramm Äpfel kostet 0,28 €. Was kosten 5,2 kg? Runde auf Cent.“ → „Ein Kilogramm Äpfel kostet 2,79 €. Was kosten 1,6 kg? Runde auf Cent.“
- terme.potenzgesetze:
  - (fehler_finden, uebung, Stufe 2) „Ein Kind rechnet: 3⁹ : 3³ = 3³. Was ist falsch?“ → „Ein Kind rechnet: 3⁹ : 3³ = 3³. Welcher Satz beschreibt den Fehler richtig?“
  - (fehler_finden, uebung, Stufe 3) „Ein Kind rechnet: 4³ · 4² = 16⁵. Was ist falsch?“ → „Ein Kind rechnet: 4³ · 4² = 16⁵. Welcher Satz beschreibt den Fehler richtig?“
  - (fehler_finden, uebung, Stufe 3) „Ein Kind rechnet: 3³ · 3³ = 9⁶. Was ist falsch?“ → „Ein Kind rechnet: 3³ · 3³ = 9⁶. Welcher Satz beschreibt den Fehler richtig?“
  - (fehler_finden, uebung, Stufe 3) „Ein Kind rechnet: 4⁴ · 4² = 16⁶. Was ist falsch?“ → „Ein Kind rechnet: 4⁴ · 4² = 16⁶. Welcher Satz beschreibt den Fehler richtig?“
  - (fehler_finden, uebung, Stufe 3) „Ein Kind rechnet: 4³ · 4³ = 4⁹. Was ist falsch?“ → „Ein Kind rechnet: 4³ · 4³ = 4⁹. Welcher Satz beschreibt den Fehler richtig?“
- bruch.prozent:
  - (verstehen, uebung, Stufe 1) „Stimmt die Aussage? „10 % von 500 € ist mehr als 10 % von 1000 €.““ → „Stimmt die Aussage? „10 % von 500 € ist mehr als 10 % von 1 000 €.““
  - (verstehen, uebung, Stufe 3) „Stimmt die Aussage? „Sinkt ein Preis von 1000 € auf 500 €, ist er um 100 % gesunken.““ → „Stimmt die Aussage? „Sinkt ein Preis von 1 000 € auf 500 €, ist er um 100 % gesunken.““
- daten.darstellen:
  - (absolute_haeufigkeit, uebung, Stufe 2) „Die Strichliste zeigt eine Umfrage zum Thema Lieblingsfach. Wie oft wurde „Kunst“ häufiger genannt als „Deutsch“?“ → „Die Strichliste zeigt eine Umfrage zum Thema Lieblingsfach. Wie viele Nennungen hat „Kunst“ mehr als „Deutsch“?“
  - (absolute_haeufigkeit, uebung, Stufe 2) „Die Strichliste zeigt eine Umfrage zum Thema Lieblingssport. Wie oft wurde „Fußball“ häufiger genannt als „Tanzen“?“ → „Die Strichliste zeigt eine Umfrage zum Thema Lieblingssport. Wie viele Nennungen hat „Fußball“ mehr als „Tanzen“?“
  - (absolute_haeufigkeit, test, Stufe 2) „Die Strichliste zeigt eine Umfrage zum Thema Haustier. Wie oft wurde „Katze“ häufiger genannt als „Fisch“?“ → „Die Strichliste zeigt eine Umfrage zum Thema Haustier. Wie viele Nennungen hat „Katze“ mehr als „Fisch“?“
  - (absolute_haeufigkeit, sicherung, Stufe 2) „Die Strichliste zeigt eine Umfrage zum Thema Haustier. Wie oft wurde „Katze“ häufiger genannt als „Hund“?“ → „Die Strichliste zeigt eine Umfrage zum Thema Haustier. Wie viele Nennungen hat „Katze“ mehr als „Hund“?“
  - (absolute_haeufigkeit, sicherung, Stufe 2) „Die Strichliste zeigt eine Umfrage zum Thema Lieblingssport. Wie oft wurde „Tanzen“ häufiger genannt als „Basketball“?“ → „Die Strichliste zeigt eine Umfrage zum Thema Lieblingssport. Wie viele Nennungen hat „Tanzen“ mehr als „Basketball“?“
- daten.kennwerte:
  - (mittel_tabelle, uebung, Stufe 3) „Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“. Wie viele Geschwister hat ein Kind im Mittel?“ [Text 12× vorhanden; gemeint: zahl-Aufgabe mit Lösung {"wert": 1.5}] → „Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“. Wie viele Kinder mit 3 Geschwistern müssten noch dazukommen, damit der Mittelwert genau 2 ist?“
  - (mittel_tabelle, uebung, Stufe 3) „Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“. Wie viele Geschwister hat ein Kind im Mittel?“ [Text 12× vorhanden; gemeint: zahl-Aufgabe mit Lösung {"wert": 1.2}] → „Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“. Jemand rechnet (0 + 1 + 2 + 3) : 4 = 1,5. Wie groß ist der Mittelwert richtig?“
  - (verstehen, uebung, Stufe 3) „Stimmt die Aussage? „Taschengeld (€): 9, 8, 8, 9, 77. Der Median beschreibt ein typisches Kind besser als der Mittelwert.““ → „Taschengeld (€): 9, 8, 8, 9, 77. Um wie viel € ist der Mittelwert größer als der Median?“
  - (verstehen, uebung, Stufe 3) „Stimmt die Aussage? „Taschengeld (€): 7, 4, 11, 12, 82. Der Median beschreibt ein typisches Kind besser als der Mittelwert.““ → „Stimmt die Aussage? „Lässt man bei 7, 4, 11, 12, 82 den Wert 82 weg, ändert sich der Median nicht.““

Klasse 9:
- zahlen.wurzeln_basis:
  - (wurzel_dezimal, uebung, Stufe 3) „Berechne 4 · √(25/4). Gib das Ergebnis als gekürzten Bruch an.“ → „Berechne 4 · √(25/4).“
- zahlen.rationale_exponenten:
  - (potenz_wert, uebung, Stufe 3) „Berechne 64^(−3/2). Gib das Ergebnis als Dezimalzahl an.“ → „Berechne 64^(−3/2). Gib das Ergebnis als Bruch an.“
  - (gleichung_exp, uebung, Stufe 3) „Löse x⁵ = −243.“ → „Löse x^(5/3) = 243 für x > 0.“
- gleichungen.lgs3:
  - (eliminieren, uebung, Stufe 3) „Gegeben: (I) −x − 2y − z = −10; (III) −2x − 4y − z = −20. Berechne (III) − 2 · (I).“ → „Gegeben: (I) −x − 2y − z = −10; (III) −2x − 4y − z = −20. Berechne (III) − 2 · (I). Welchen Wert hat z?“
- funktionen.quadratisch:
  - (extremwert, uebung, Stufe 3) „Ein Ball fliegt auf der Bahn h(x) = −0,05x² + 1x + 2 (x und h in m). Wie hoch fliegt er höchstens?“ → „Ein Ball fliegt auf der Bahn h(x) = −0,05x² + x + 2 (x und h in m). Wie hoch fliegt er höchstens?“
- funktionen.potenz:
  - (werte, uebung, Stufe 3) „Berechne f(−2) für f(x) = −2x³.“ [Text 2× vorhanden; gemeint: Auswahl mit den Antworten −16 | 64 | 12 | 16; richtig „16“] → „Welches Vorzeichen hat f(−5) für f(x) = −2x³? Entscheide, ohne den Wert auszurechnen.“
- trigo.pythagoras:
  - (anwendung, uebung, Stufe 3) „Eine Rampe steigt auf 600 cm waagrechter Länge um 17 cm an. Wie lang ist die Rampe? Runde auf ganze Zentimeter.“ → „Eine Rampe steigt auf 240 cm waagrechter Länge um 70 cm an. Wie lang ist die Rampe?“
- gleichungen.trig:
  - (sinus, uebung, Stufe 3) „Löse sin x = −0,69 im Bereich 0° ≤ x < 360°. Runde auf ganze Grad.“ → „Löse sin x = −0,9 im Bereich 0° ≤ x < 360°. Runde auf ganze Grad.“
- stochastik.verknuepft:
  - (verstehen, uebung, Stufe 3) „P(A) = 0,6, P(B) = 0,5, P(A ∩ B) = 0,07. Jemand rechnet P(A ∪ B) = 1,1. Was stimmt?“ → „P(A) = 0,6, P(B) = 0,5, P(A ∩ B) = 0,2. Jemand rechnet P(A ∪ B) = 1,1. Was stimmt?“

Klasse 10:
- gleichungen.exponential:
  - (wachstum, uebung, Stufe 1) „Ein Kapital von 5 000 € wird mit 6 % pro Jahr verzinst (Zinseszins). Wie groß ist es nach 5 Jahren? Runde auf Cent.“ → „Ein Kapital von 5 000 € wird mit 6 % pro Jahr verzinst (Zinseszins). Löse 5 000 · 1,06^t = 7 000, um zu sehen, wann es auf 7 000 € angewachsen ist. Runde auf eine Nachkommastelle.“
  - (wachstum, uebung, Stufe 1) „Ein Kapital von 2 000 € wird mit 2 % pro Jahr verzinst (Zinseszins). Wie groß ist es nach 2 Jahren? Runde auf Cent.“ → „Ein Kapital von 2 000 € wird mit 2 % pro Jahr verzinst (Zinseszins). Löse 2 000 · 1,02^t = 2 500, um zu sehen, wann es auf 2 500 € angewachsen ist. Runde auf eine Nachkommastelle.“
  - (wachstum, uebung, Stufe 1) „Ein Kapital von 1 000 € wird mit 6 % pro Jahr verzinst (Zinseszins). Wie groß ist es nach 2 Jahren? Runde auf Cent.“ → „Ein Kapital von 1 000 € wird mit 6 % pro Jahr verzinst (Zinseszins). Löse 1 000 · 1,06^t = 2 000, um zu sehen, wann es auf 2 000 € angewachsen ist. Runde auf eine Nachkommastelle.“
  - (wachstum, sicherung, Stufe 2) „Ein Kapital von 2 000 € wird mit 2 % pro Jahr verzinst (Zinseszins). Wie groß ist es nach 3 Jahren? Runde auf Cent.“ → „Ein Kapital von 2 000 € wird mit 2 % pro Jahr verzinst (Zinseszins). Löse 2 000 · 1,02^t = 3 000, um zu sehen, wann es auf 3 000 € angewachsen ist. Runde auf eine Nachkommastelle.“
- funktionen.exponential_log:
  - (werte, uebung, Stufe 3) „Berechne f(4) für f(x) = 1000 · 1,5^x.“ → „Berechne f(4) für f(x) = 1 000 · 1,5^x.“
- raum.pyramide_kegel_kugel:
  - (verstehen, uebung, Stufe 1) „Eine Pyramide hat als Grundfläche ein regelmäßiges 100-Eck. Was passiert, wenn man die Eckenzahl immer weiter erhöht?“ → „Wie viele Ecken hat eine Pyramide, deren Grundfläche ein regelmäßiges 12-Eck ist?“
  - (verstehen, uebung, Stufe 1) „Eine Pyramide hat als Grundfläche ein regelmäßiges 12-Eck. Was passiert, wenn man die Eckenzahl immer weiter erhöht?“ → „Welcher Körper hat genau eine Spitze und eine kreisförmige Grundfläche?“
- stochastik.mehrstufig:
  - (gegenereignis, uebung, Stufe 1) „Ein Würfel wird 2-mal geworfen. Wie groß ist P(mindestens eine Eins)?“ → „Eine Münze wird 3-mal geworfen. Wie groß ist P(mindestens einmal Zahl)?“
  - (baum_ergaenzen, uebung, Stufe 2) „In einem zweistufigen Baumdiagramm ist P(A) = 0,5 und die Wahrscheinlichkeit des Pfades „A, dann B“ = 0,45. Welche Wahrscheinlichkeit steht am Ast von A nach B?“ → „In einem zweistufigen Baumdiagramm ist P(A) = 0,5 und die Wahrscheinlichkeit des Pfades „A, dann B“ = 0,3. Welche Wahrscheinlichkeit steht am Ast von A nach B?“
  - (baum_ergaenzen, uebung, Stufe 2) „In einem zweistufigen Baumdiagramm ist P(A) = 0,2 und die Wahrscheinlichkeit des Pfades „A, dann B“ = 0,18. Welche Wahrscheinlichkeit steht am Ast von A nach B?“ → „In einem zweistufigen Baumdiagramm ist P(A) = 0,2 und die Wahrscheinlichkeit des Pfades „A, dann B“ = 0,1. Welche Wahrscheinlichkeit steht am Ast von A nach B?“
  - (verstehen, uebung, Stufe 2) „Jemand sagt: „Bei 5 Würfen ist P(mindestens eine Sechs) = 5 · 1/6 = 5/6.“ Was stimmt?“ → „Jemand behauptet: „Bei 5 Würfen ist P(mindestens eine Sechs) = 5 · 1/6 = 5/6.“ Was stimmt?“
  - (verstehen, uebung, Stufe 2) „Jemand sagt: „Bei 2 Würfen ist P(mindestens eine Sechs) = 2 · 1/6 = 1/3.“ Was stimmt?“ → „Jemand behauptet: „Bei 2 Würfen ist P(mindestens eine Sechs) = 2 · 1/6 = 1/3.“ Was stimmt?“
  - (verstehen, uebung, Stufe 3) „Jemand sagt: „Bei 4 Würfen ist P(mindestens eine Sechs) = 4 · 1/6 = 2/3.“ Was stimmt?“ → „Jemand behauptet: „Bei 4 Würfen ist P(mindestens eine Sechs) = 4 · 1/6 = 2/3.“ Was stimmt?“

(95 Aufgaben ersetzt.)

### Liste „nicht umgesetzt“ (mit Begründung)

Klasse 8:
- funktionen.grundbegriffe: punkt_graph S2 „Lies am Graphen ab: f(4) = ?“ (gehört eher zu graph_lesen) – Bei erneuter Prüfung passend: Den Punkt (4 | f(4)) am Graphen ablesen gehört zu „Liegt der Punkt auf dem Graphen?“. Lösung richtig, kein Mangel.
- funktionen.gebrochen: indirekt: Überschneidung mit groessen.indirekt – Kein Mangel an einer Aufgabe; betrifft die Reihenfolge im Plan (Haupt-Chat).
- terme.bruchterme: kuerzen S3 (x² − 49)/(x − 7) setzt die 3. binomische Formel voraus – Aufgaben sind richtig und echte Stufe 3. Offen ist nur, ob die binomischen Formeln im Plan vor diesem Thema stehen (Reihenfolge, Haupt-Chat).
- gleichungen.ungleichungen: sachaufgabe: Stufen 1 und 2 (Aufzug/Handytarif) inhaltlich gleich – Die Aufgaben sind richtig; Stufe 1 und 2 unterscheiden sich in den Zahlen (Kommazahlen, „angefangene“ km auf Stufe 2). Kein einzelner Fehler; neue Stufe-3-Typen kamen in Runde 10 dazu.
- zahlen.intervalle: enthalten S1 „Welche Zahl liegt im Intervall [1; 7]?“ hat nur 3 Antworten – Zulässig und richtig; kein Fehler.
- gleichungen.formeln: geometrie S3 Pyramide (V = G · h : 3) – Formel steht in der Aufgabe; als reine Formelanwendung (Umstellen) passend zum Thema, Lösung richtig.
- gleichungen.formeln: einsetzen S3 Dichte mit dm³ (Aluminium, Glas, Eis) – Drei verschiedene Stoffe und Zahlen, alle richtig; Übungsreihe zum gleichen Schritt (dm³ → cm³) ist gewollt.
- messen.kreisberechnung: flaeche S3 Pizzavergleich (3×) – Kein Fehler; Übungsreihe zum selben Typ mit verschiedenen Zahlen, Ablenker gut.
- messen.kreisberechnung: verstehen S2 „Jemand rechnet A = 2 · π · r …“ (3×) – Kein Fehler; Übungsreihe mit verschiedenen Zahlen.
- messen.koerper_darstellung: zylinder S2 Mantelfläche aus Umfang · Höhe (6×) – Kein Fehler; Übungsreihe mit verschiedenen Zahlen.
- messen.koerper_darstellung: netz S3 „Netz 442 cm², Grundfläche 7 × 8 cm, Höhe?“ (3×) – Kein Fehler; Übungsreihe (Rückwärtsrechnen) mit verschiedenen Zahlen.
- messen.koerper_darstellung: Überschneidung der Karten „schraegbild“ mit raum.schraegbilder – Betrifft den Plan (Haupt-Chat), keine einzelne Aufgabe.
- raum.schraegbilder: koordinaten S2 „Gib die z-Koordinate von C an“ (3× gleicher Typ) – Laut Befund in Ordnung; Lösungen richtig.
- raum.schraegbilder: Karte „laengen“ ≈ messen.koerper_darstellung/„schraegbild“ – Doppelung im Plan (Haupt-Chat), keine einzelne fehlerhafte Aufgabe.
- stochastik.grundbegriffe: gegenereignis S3 „3 Würfe, P(mindestens eine Sechs) = 91/216“ – Lösung richtig; Weg über das Gegenereignis (5/6)³ ist echte Stufe 3. Ob die Produktregel in Kl. 8 eingeführt ist, betrifft den Plan.
- stochastik.simulation: auswerten S3 „Gruppe A 100 / B 50 Durchgänge – wessen Schätzwert …“ (3×) – Kein Fehler; Übungsreihe zum selben Gedanken mit verschiedenen Zahlen.
- groessen.indirekt: erkennen S3 „… Je mehr, desto weniger, also indirekt proportional.“ (4×) – Kein Fehler; Übungsreihe zum selben Fehlschluss mit verschiedenen Beispielen.
- groessen.indirekt: unterscheiden S1/S2 „Welche Art von Zuordnung zeigt die Tabelle?“ (11×) – Kein Fehler; Stufe 2 hat den zusätzlichen Ablenker „nicht zu entscheiden“ und andere Tabellen.
- groessen.indirekt: sach S2 „Taxi … Was kosten 6 km?“ (weder noch) – Laut Befund gut als Abgrenzung; Lösung richtig.
- groessen.indirekt: Überschneidung mit funktionen.gebrochen/„indirekt“ – Reihenfolge im Plan (Haupt-Chat), keine einzelne Aufgabe.

Klasse 5:
- messen.koerper_berechnung: sachaufgaben S2 Aquarium ohne Deckel „anspruchsvoller als manche Stufe-3-Aufgabe“ – Passt auf Stufe 2 (fünf Flächen, ein Gedanke); Stufe 3 enthält Zusatzschritte (Abzüge, Fliesen, Umrechnung).
- gleichungen.einfach: probe S3 „Für welche der Zahlen 3, 4, 5, 6 gilt 2 · x + 7 = 4 · x − 3?“ – Hinweis aus der Liste, kein Mangel: Die Aufgabe passt zur Lernkarte „Probe machen“.

Klasse 7:
- bruch.prozent_grundwert: argumente: Ablenker „Sinkt ein Wert um 100 %, halbiert er sich, denn 100 % ist die Hälfte von 200 %“ – Laut Befund kein Fehler (eindeutig falsch als Ablenker).
- terme.aufstellen: sachsituation S3 „Kletterhalle … Bei wie vielen Besuchen kosten beide gleich viel?“ – Lösung 8 richtig und durch Probieren mit dem Term lösbar; passt als Stufe 3.
- terme.aufstellen: deuten S3 „Jemand übersetzt … in den Term … Stimmt das?“ prüft Übersetzen statt Deuten – Aufgaben richtig; Deuten von Teiltermen wurde in Runde 10 ergänzt. Die Karte bleibt unverändert.
- geometrie.konstruktion: kongruenzsatz S3 SsW-Fälle „Wie viele Dreiecke gibt es?“: Hinweis „Zeichne es auf Papier“ ergänzen – Der Tipp sagt schon „Zeichne c und α. Schlage um B einen Kreis mit Radius a …“; Lösungen richtig. Ein Hinweis im Fragetext wäre eine Änderung der Frage.
- daten.boxplot: vergleichen: Stufe 1 und 2 gleich gebaut („Welche Aussage ist richtig?“ zu zwei Boxplots) – Lösungen richtig; Stufe 2 fragt zusätzlich nach Streuung und Gesamtvergleich. Ein einzelner falsch eingestufter Fall ist nicht benannt.

Klasse 6:
- bruch.brueche: zahlenstrahl: Markierungen mit Dritteln/Sechsteln ohne Feld „zahl“ – Von Hand geprüft und richtig (laut Befund); kein Mangel.
- bruch.dezimal: runden „Runde 2,596 auf Hundertstel“ (Test 30,096): Lösung als 2,6 bzw. 30,1 gespeichert – Die App wertet 2,60 = 2,6; der Lösungsweg nennt die Endnull bereits („2,596 ≈ 2,60. Die Null am Ende bleibt stehen …“).
- bruch.rechnen: brueche_plus_minus S2 „Ergänze: 1/2 − □/□ = 1/4“ nicht eindeutig (2/8, 3/12 …) – Der Hinweis „Vollständig gekürzt“ steht bereits in der Aufgabe; damit ist nur 1/4 richtig.
- bruch.rechnen: gemischt S3 „3/2 · 2/5 − 1/4 · 5/2 …“ mit negativem Ergebnis – Laut Befund in Ordnung (Vorzeichen-Karte kommt vorher).

Klasse 9:
- gleichungen.potenz: sachaufgabe S2 Zinseszins („Guthaben wächst in 2 Jahren …“) – Aufgaben richtig; mathematisch nur (1 + p)² = q, also eine Potenzgleichung. Ob der Sachkontext in Kl. 9 passt, ist eine Plan-Frage (siehe „für Sebastian“).
- gleichungen.lgs3: loesen S3 „Wie viele Lösungen hat das System …?“ (unendlich viele) – Lösungen richtig; als Vertiefung vertretbar. Die Lernkarte bleibt unverändert (siehe „für Sebastian“).
- funktionen.quadratisch: bestimmen S3 „Parabel durch drei Punkte“ überschneidet sich mit gleichungen.lgs3/parabel – Laut Befund kein Fehler; Überschneidung betrifft den Plan.
- trigo.allgemein: kosinussatz_seite S3 viermal „Schiff fährt … dreht um … nach links“; Lernkarte erklärt „180° − Drehwinkel“ nicht – Aufgaben richtig; der Tipp nennt den Schritt („Der Innenwinkel am Wendepunkt ist 180° minus Drehwinkel“), der Lösungsweg rechnet ihn vor. Seit Runde 10 gibt es auf Stufe 3 weitere Typen. Lernkarte siehe „für Sebastian“.
- trigo.allgemein: sinussatz_seite S3 viermal „Zwei Beobachter … Baum auf der anderen Seite eines Sees“ – Kein Fehler; seit Runde 10 gibt es auf Stufe 3 vier andere Typen.
- gleichungen.trig: tangens S3 Rampe/„22 % Steigung“ gehören inhaltlich zu trigo.rechtwinklig – Lösungen richtig; tan x = Wert mit spitzem Winkel ist ein Sonderfall der Gleichung. Die Zuordnung zum Thema betrifft den Plan.

Klasse 10:
- gleichungen.polynom: vielfachheit: Ablenker „Nein, die Nullstelle ist 3-fach (ungerade)“ in sich widersprüchlich – Laut Befund kein Fehler; als Ablenker zulässig (prüft, ob man „ungerade ⇒ Wechsel“ kennt).
- gleichungen.polynom: Lückenaufgaben „x₁ = □; x₂ = □ …“ verraten die Zahl der Lösungen – Steht bereits unter „offen“; Runde 10 fragt die Anzahl teils als Zahl ab. Ein Umbau aller Lückenaufgaben wäre keine Einzelkorrektur.
- funktionen.trig: periode, parameter, zuordnen, eigenschaften, anwendung: fast nur Gradmaß statt Bogenmaß (LehrplanPLUS M10 3, Abitur) – Kein Fehler in einzelnen Aufgaben; ein Umstellen aller alten Aufgaben auf Bogenmaß wäre ein Umbau der Karten. Runde 10 hat Bogenmaß-Aufgaben ergänzt (siehe „für Sebastian“).
- funktionen.ganzrational: randverhalten S1 mit Polynom 7. Grades und 8 Gliedern – Laut Befund inhaltlich richtig; nur das höchste Glied zählt, das ist der Lerninhalt der Karte.
- stochastik.mehrstufig: simulation S2 „Simulation 500-mal … relative Häufigkeit“ (reines Ablesen) – Lösungen richtig; die eigentliche Simulation (Zufallszahlen zuordnen) wurde in Runde 10 ergänzt.

### Liste „für Sebastian“

Klasse 8:
- funktionen.grundbegriffe: Der Eintrag in „offen“ („Kreis kann die App nicht zeichnen“) ist veraltet – die App zeichnet Kreise (koordinaten.kreise). Nur der Haupt-Chat ändert „offen“.
- zahlen.intervalle: lehrplan_gym der Karten ist leer – das Thema hat keine eigene LehrplanPLUS-Zeile (Inhalt gehört zu Ungleichungen, Kl. 8). Karten-Text nicht geändert.
- raum.schraegbilder: lehrplan_gym leer; Raumkoordinaten und windschiefe Geraden stehen im LehrplanPLUS Gymnasium nicht in Jgst. 8 – Thema im Plan als Vertiefung markieren? Karten-Texte nicht geändert.
- stochastik.simulation: lehrplan_gym leer; Simulation steht im LehrplanPLUS Gym Kl. 8 nicht als eigener Inhalt – als Vertiefung zu Laplace/relative Häufigkeit führen? Karten-Texte nicht geändert.
- groessen.indirekt: lehrplan_gym leer und Überschneidung mit funktionen.gebrochen/„indirekt“ – Reihenfolge im Plan klären. Karten-Texte nicht geändert.

Klasse 5:
- geometrie.grundbegriffe/kreis_lage: Die Lernkarte erklärt nur Kreis und Gerade; die übrigen Stufe-3-Aufgaben zu zwei Kreisen (von außen berühren, getrennt) setzen r₁ + r₂ voraus. Erklärung ergänzen oder Aufgaben belassen? Karten-Text nicht geändert.
- geometrie.ortslinien/zwei_kreise: Die Lernkarte erklärt nur sich schneidende/berührende Kreise; „Kreis im Kreis“ (r₁ − r₂) ist aus den älteren Übungen genommen; die Aufgabe „Welcher Abstand [AB] ist möglich?“ (Runde 10) nutzt die Grenze r₁ − r₂ noch (im Lösungsweg erklärt). Soll die Lernkarte das ergänzen? Außerdem: lehrplan_gym leer, Ortslinien stehen im LehrplanPLUS Gym erst in Jgst. 7 (laut D2 inzwischen Kairo/Kl. 7). Karten-Text nicht geändert.

Klasse 7:
- geometrie.konstruktion/kongruenzsatz: SsW-Fälle (Stufe 3) sind ohne Zeichnung kaum zu entscheiden (Rechnung bräuchte den Sinus) – als Vertiefung kennzeichnen? Karten-Text nicht geändert.

Klasse 6:
- daten.kennwerte: laut themenliste lehrplan_gym ist für Kl. 6 nur „Arithmetisches Mittel bestimmen“ vorgesehen; die Karten modal_spannweite und median gehen darüber hinaus (BMT8-Stoff bis Kl. 7). Als Vertiefung führen? Karten nicht geändert.

Klasse 9:
- gleichungen.potenz/sachaufgabe: Zinseszins-Aufgaben (Stufe 2, alle Pools) – Zinseszins ist laut Themenliste Zusatzstoff Kl. 10 (finanzen.zinseszins). In Kl. 9 belassen?
- gleichungen.lgs3/loesen: Stufe-3-Aufgaben „Wie viele Lösungen hat das System …?“ (keine/unendlich viele) gehen über den LehrplanPLUS-Text hinaus und werden auf der Lernkarte nicht erklärt – Erklärung ergänzen oder als Vertiefung kennzeichnen?
- trigo.allgemein/kosinussatz_seite: Lernkarte erklärt nicht, dass der Dreieckswinkel 180° minus Drehwinkel ist (Schiff-Aufgaben). Ergänzen? Karten-Text nicht geändert.

Klasse 10:
- funktionen.trig: Die alten Aufgaben arbeiten fast nur im Gradmaß; LehrplanPLUS M10 3 und Abitur nutzen das Bogenmaß. Die Begründung unter „offen“ (keine π-Beschriftung) ist seit 15.11. überholt. Karten/alte Aufgaben auf Bogenmaß umstellen?

Allgemein:
- Laut D2 (antworten.md, 16.11.) gelten Schrägbilder und Simulation am Gymnasium inzwischen als Klasse 10 und Ortslinien liegen in Kairo (Kl. 7) – die Lehrplan-Hinweise oben zu raum.schraegbilder, stochastik.simulation und geometrie.ortslinien sind damit teils schon beantwortet.

## 2026-11-16 05:56 – STATUS
stochastik.mehrstufig fertig: umgestuft 3 / berichtigt 0 / ersetzt 6 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „In einem zweistufigen Baumdiagramm ist P(A) = 0,5 und die Wahrscheinlichkeit des Pfades „A, dann B“ = 0,45. Welche Wahrscheinlichkeit steht am Ast von A nach B?“
  - „In einem zweistufigen Baumdiagramm ist P(A) = 0,2 und die Wahrscheinlichkeit des Pfades „A, dann B“ = 0,18. Welche Wahrscheinlichkeit steht am Ast von A nach B?“
  - „Ein Würfel wird 2-mal geworfen. Wie groß ist P(mindestens eine Eins)?“
  - „Jemand sagt: „Bei 5 Würfen ist P(mindestens eine Sechs) = 5 · 1/6 = 5/6.“ Was stimmt?“
  - „Jemand sagt: „Bei 2 Würfen ist P(mindestens eine Sechs) = 2 · 1/6 = 1/3.“ Was stimmt?“
  - „Jemand sagt: „Bei 4 Würfen ist P(mindestens eine Sechs) = 4 · 1/6 = 2/3.“ Was stimmt?“
- nicht umgesetzt:
  - simulation S2 „Simulation 500-mal … relative Häufigkeit“ (reines Ablesen) – Lösungen richtig; die eigentliche Simulation (Zufallszahlen zuordnen) wurde in Runde 10 ergänzt.

## 2026-11-16 05:55 – STATUS
raum.pyramide_kegel_kugel fertig: umgestuft 3 / berichtigt 3 / ersetzt 2 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Eine Pyramide hat als Grundfläche ein regelmäßiges 100-Eck. Was passiert, wenn man die Eckenzahl immer weiter erhöht?“
  - „Eine Pyramide hat als Grundfläche ein regelmäßiges 12-Eck. Was passiert, wenn man die Eckenzahl immer weiter erhöht?“

## 2026-11-16 05:54 – STATUS
funktionen.ganzrational fertig: umgestuft 2 / berichtigt 6 / ersetzt 0 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - randverhalten S1 mit Polynom 7. Grades und 8 Gliedern – Laut Befund inhaltlich richtig; nur das höchste Glied zählt, das ist der Lerninhalt der Karte.

## 2026-11-16 05:53 – STATUS
funktionen.trig fertig: umgestuft 4 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - periode, parameter, zuordnen, eigenschaften, anwendung: fast nur Gradmaß statt Bogenmaß (LehrplanPLUS M10 3, Abitur) – Kein Fehler in einzelnen Aufgaben; ein Umstellen aller alten Aufgaben auf Bogenmaß wäre ein Umbau der Karten. Runde 10 hat Bogenmaß-Aufgaben ergänzt (siehe „für Sebastian“).
- für Sebastian:
  - funktionen.trig: Die alten Aufgaben arbeiten fast nur im Gradmaß; LehrplanPLUS M10 3 und Abitur nutzen das Bogenmaß. Die Begründung unter „offen“ (keine π-Beschriftung) ist seit 15.11. überholt. Karten/alte Aufgaben auf Bogenmaß umstellen?

## 2026-11-16 05:53 – STATUS
funktionen.exponential_log fertig: umgestuft 6 / berichtigt 2 / ersetzt 1 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Berechne f(4) für f(x) = 1000 · 1,5^x.“

## 2026-11-16 05:53 – STATUS
gleichungen.polynom fertig: umgestuft 2 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 2. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - vielfachheit: Ablenker „Nein, die Nullstelle ist 3-fach (ungerade)“ in sich widersprüchlich – Laut Befund kein Fehler; als Ablenker zulässig (prüft, ob man „ungerade ⇒ Wechsel“ kennt).
  - Lückenaufgaben „x₁ = □; x₂ = □ …“ verraten die Zahl der Lösungen – Steht bereits unter „offen“; Runde 10 fragt die Anzahl teils als Zahl ab. Ein Umbau aller Lückenaufgaben wäre keine Einzelkorrektur.

## 2026-11-16 05:52 – STATUS
gleichungen.exponential fertig: umgestuft 8 / berichtigt 0 / ersetzt 4 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Ein Kapital von 5 000 € wird mit 6 % pro Jahr verzinst (Zinseszins). Wie groß ist es nach 5 Jahren? Runde auf Cent.“
  - „Ein Kapital von 2 000 € wird mit 2 % pro Jahr verzinst (Zinseszins). Wie groß ist es nach 2 Jahren? Runde auf Cent.“
  - „Ein Kapital von 1 000 € wird mit 6 % pro Jahr verzinst (Zinseszins). Wie groß ist es nach 2 Jahren? Runde auf Cent.“
  - „Ein Kapital von 2 000 € wird mit 2 % pro Jahr verzinst (Zinseszins). Wie groß ist es nach 3 Jahren? Runde auf Cent.“

## 2026-11-16 05:52 – STATUS
stochastik.verknuepft fertig: umgestuft 6 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „P(A) = 0,6, P(B) = 0,5, P(A ∩ B) = 0,07. Jemand rechnet P(A ∪ B) = 1,1. Was stimmt?“

## 2026-11-16 05:51 – STATUS
gleichungen.trig fertig: umgestuft 9 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Löse sin x = −0,69 im Bereich 0° ≤ x < 360°. Runde auf ganze Grad.“
- nicht umgesetzt:
  - tangens S3 Rampe/„22 % Steigung“ gehören inhaltlich zu trigo.rechtwinklig – Lösungen richtig; tan x = Wert mit spitzem Winkel ist ein Sonderfall der Gleichung. Die Zuordnung zum Thema betrifft den Plan.

## 2026-11-16 05:51 – STATUS
trigo.allgemein fertig: umgestuft 5 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 2. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - kosinussatz_seite S3 viermal „Schiff fährt … dreht um … nach links“; Lernkarte erklärt „180° − Drehwinkel“ nicht – Aufgaben richtig; der Tipp nennt den Schritt („Der Innenwinkel am Wendepunkt ist 180° minus Drehwinkel“), der Lösungsweg rechnet ihn vor. Seit Runde 10 gibt es auf Stufe 3 weitere Typen. Lernkarte siehe „für Sebastian“.
  - sinussatz_seite S3 viermal „Zwei Beobachter … Baum auf der anderen Seite eines Sees“ – Kein Fehler; seit Runde 10 gibt es auf Stufe 3 vier andere Typen.
- für Sebastian:
  - trigo.allgemein/kosinussatz_seite: Lernkarte erklärt nicht, dass der Dreieckswinkel 180° minus Drehwinkel ist (Schiff-Aufgaben). Ergänzen? Karten-Text nicht geändert.

## 2026-11-16 05:50 – STATUS
trigo.rechtwinklig fertig: umgestuft 18 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.

## 2026-11-16 05:50 – STATUS
trigo.pythagoras fertig: umgestuft 3 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Eine Rampe steigt auf 600 cm waagrechter Länge um 17 cm an. Wie lang ist die Rampe? Runde auf ganze Zentimeter.“

## 2026-11-16 05:50 – STATUS
abbildungen.aehnlichkeit fertig: umgestuft 8 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.

## 2026-11-16 05:50 – STATUS
funktionen.potenz fertig: umgestuft 4 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Berechne f(−2) für f(x) = −2x³.“

## 2026-11-16 05:49 – STATUS
funktionen.quadratisch fertig: umgestuft 5 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Ein Ball fliegt auf der Bahn h(x) = −0,05x² + 1x + 2 (x und h in m). Wie hoch fliegt er höchstens?“
- nicht umgesetzt:
  - bestimmen S3 „Parabel durch drei Punkte“ überschneidet sich mit gleichungen.lgs3/parabel – Laut Befund kein Fehler; Überschneidung betrifft den Plan.

## 2026-11-16 05:49 – STATUS
gleichungen.lgs3 fertig: umgestuft 6 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Gegeben: (I) −x − 2y − z = −10; (III) −2x − 4y − z = −20. Berechne (III) − 2 · (I).“
- nicht umgesetzt:
  - loesen S3 „Wie viele Lösungen hat das System …?“ (unendlich viele) – Lösungen richtig; als Vertiefung vertretbar. Die Lernkarte bleibt unverändert (siehe „für Sebastian“).
- für Sebastian:
  - gleichungen.lgs3/loesen: Stufe-3-Aufgaben „Wie viele Lösungen hat das System …?“ (keine/unendlich viele) gehen über den LehrplanPLUS-Text hinaus und werden auf der Lernkarte nicht erklärt – Erklärung ergänzen oder als Vertiefung kennzeichnen?

## 2026-11-16 05:49 – STATUS
gleichungen.potenz fertig: umgestuft 3 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - sachaufgabe S2 Zinseszins („Guthaben wächst in 2 Jahren …“) – Aufgaben richtig; mathematisch nur (1 + p)² = q, also eine Potenzgleichung. Ob der Sachkontext in Kl. 9 passt, ist eine Plan-Frage (siehe „für Sebastian“).
- für Sebastian:
  - gleichungen.potenz/sachaufgabe: Zinseszins-Aufgaben (Stufe 2, alle Pools) – Zinseszins ist laut Themenliste Zusatzstoff Kl. 10 (finanzen.zinseszins). In Kl. 9 belassen?

## 2026-11-16 05:48 – STATUS
gleichungen.quadratisch fertig: umgestuft 4 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.

## 2026-11-16 05:48 – STATUS
zahlen.rationale_exponenten fertig: umgestuft 3 / berichtigt 0 / ersetzt 2 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Berechne 64^(−3/2). Gib das Ergebnis als Dezimalzahl an.“
  - „Löse x⁵ = −243.“

## 2026-11-16 05:48 – STATUS
zahlen.reell fertig: umgestuft 2 / berichtigt 2 / ersetzt 0 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.

## 2026-11-16 05:48 – STATUS
zahlen.wurzeln_basis fertig: umgestuft 6 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Berechne 4 · √(25/4). Gib das Ergebnis als gekürzten Bruch an.“

## 2026-11-16 05:47 – STATUS
daten.kennwerte fertig: umgestuft 4 / berichtigt 0 / ersetzt 4 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“. Wie viele Geschwister hat ein Kind im Mittel?“
  - „Stimmt die Aussage? „Taschengeld (€): 9, 8, 8, 9, 77. Der Median beschreibt ein typisches Kind besser als der Mittelwert.““
  - „Stimmt die Aussage? „Taschengeld (€): 7, 4, 11, 12, 82. Der Median beschreibt ein typisches Kind besser als der Mittelwert.““
- für Sebastian:
  - daten.kennwerte: laut themenliste lehrplan_gym ist für Kl. 6 nur „Arithmetisches Mittel bestimmen“ vorgesehen; die Karten modal_spannweite und median gehen darüber hinaus (BMT8-Stoff bis Kl. 7). Als Vertiefung führen? Karten nicht geändert.

## 2026-11-16 05:46 – STATUS
daten.darstellen fertig: umgestuft 5 / berichtigt 0 / ersetzt 5 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Die Strichliste zeigt eine Umfrage zum Thema Lieblingsfach. Wie oft wurde „Kunst“ häufiger genannt als „Deutsch“?“
  - „Die Strichliste zeigt eine Umfrage zum Thema Lieblingssport. Wie oft wurde „Fußball“ häufiger genannt als „Tanzen“?“
  - „Die Strichliste zeigt eine Umfrage zum Thema Haustier. Wie oft wurde „Katze“ häufiger genannt als „Fisch“?“
  - „Die Strichliste zeigt eine Umfrage zum Thema Haustier. Wie oft wurde „Katze“ häufiger genannt als „Hund“?“
  - „Die Strichliste zeigt eine Umfrage zum Thema Lieblingssport. Wie oft wurde „Tanzen“ häufiger genannt als „Basketball“?“

## 2026-11-16 05:46 – STATUS
bruch.prozent fertig: umgestuft 5 / berichtigt 0 / ersetzt 2 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Stimmt die Aussage? „Sinkt ein Preis von 1000 € auf 500 €, ist er um 100 % gesunken.““
  - „Stimmt die Aussage? „10 % von 500 € ist mehr als 10 % von 1000 €.““

## 2026-11-16 05:46 – STATUS
terme.potenzgesetze fertig: umgestuft 8 / berichtigt 0 / ersetzt 5 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Ein Kind rechnet: 4³ · 4² = 16⁵. Was ist falsch?“
  - „Ein Kind rechnet: 3³ · 3³ = 9⁶. Was ist falsch?“
  - „Ein Kind rechnet: 4⁴ · 4² = 16⁶. Was ist falsch?“
  - „Ein Kind rechnet: 4³ · 4³ = 4⁹. Was ist falsch?“
  - „Ein Kind rechnet: 3⁹ : 3³ = 3³. Was ist falsch?“

## 2026-11-16 05:45 – STATUS
bruch.rechnen fertig: umgestuft 1 / berichtigt 0 / ersetzt 2 / neu 0 / nicht umgesetzt 2. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Berechne (−1/8) + 1/5.“
  - „Ein Kilogramm Äpfel kostet 0,28 €. Was kosten 5,2 kg? Runde auf Cent.“
- nicht umgesetzt:
  - brueche_plus_minus S2 „Ergänze: 1/2 − □/□ = 1/4“ nicht eindeutig (2/8, 3/12 …) – Der Hinweis „Vollständig gekürzt“ steht bereits in der Aufgabe; damit ist nur 1/4 richtig.
  - gemischt S3 „3/2 · 2/5 − 1/4 · 5/2 …“ mit negativem Ergebnis – Laut Befund in Ordnung (Vorzeichen-Karte kommt vorher).

## 2026-11-16 05:44 – STATUS
bruch.dezimal fertig: umgestuft 5 / berichtigt 0 / ersetzt 3 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Stimmt die Aussage? „Eine Zahl mit drei Nachkommastellen ist immer größer als eine mit einer, z. B. 0,37 > 0,8.““
  - „Berechne 1 + 0,5 und gib das Ergebnis als Dezimalzahl an.“
  - „Berechne 1 + 0,4 und gib das Ergebnis als Dezimalzahl an.“
- nicht umgesetzt:
  - runden „Runde 2,596 auf Hundertstel“ (Test 30,096): Lösung als 2,6 bzw. 30,1 gespeichert – Die App wertet 2,60 = 2,6; der Lösungsweg nennt die Endnull bereits („2,596 ≈ 2,60. Die Null am Ende bleibt stehen …“).

## 2026-11-16 05:44 – STATUS
bruch.brueche fertig: umgestuft 6 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Um wie viel ist 5/6 größer als 4/7?“
- nicht umgesetzt:
  - zahlenstrahl: Markierungen mit Dritteln/Sechsteln ohne Feld „zahl“ – Von Hand geprüft und richtig (laut Befund); kein Mangel.

## 2026-11-16 05:44 – STATUS
zahlen.potenzen_zehner fertig: umgestuft 7 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.

## 2026-11-16 05:43 – STATUS
daten.boxplot fertig: umgestuft 4 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - vergleichen: Stufe 1 und 2 gleich gebaut („Welche Aussage ist richtig?“ zu zwei Boxplots) – Lösungen richtig; Stufe 2 fragt zusätzlich nach Streuung und Gesamtvergleich. Ein einzelner falsch eingestufter Fall ist nicht benannt.

## 2026-11-16 05:43 – STATUS
geometrie.kreis fertig: umgestuft 3 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.

## 2026-11-16 05:43 – STATUS
geometrie.konstruktion fertig: umgestuft 6 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - kongruenzsatz S3 SsW-Fälle „Wie viele Dreiecke gibt es?“: Hinweis „Zeichne es auf Papier“ ergänzen – Der Tipp sagt schon „Zeichne c und α. Schlage um B einen Kreis mit Radius a …“; Lösungen richtig. Ein Hinweis im Fragetext wäre eine Änderung der Frage.
- für Sebastian:
  - geometrie.konstruktion/kongruenzsatz: SsW-Fälle (Stufe 3) sind ohne Zeichnung kaum zu entscheiden (Rechnung bräuchte den Sinus) – als Vertiefung kennzeichnen? Karten-Text nicht geändert.

## 2026-11-16 05:42 – STATUS
abbildungen.kongruenz fertig: umgestuft 1 / berichtigt 0 / ersetzt 3 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Welcher Großbuchstabe (Blockschrift) ist punktsymmetrisch, hat aber keine Symmetrieachse?“
  - „Passen 4 gleichseitige Dreiecke und ein Quadrat lückenlos um eine Ecke?“
  - „Passen 3 gleichseitige Dreiecke und 2 Quadrate lückenlos um eine Ecke?“

## 2026-11-16 05:42 – STATUS
gleichungen.linear fertig: umgestuft 4 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Jemand multipliziert 6x + 6 = 21 auf beiden Seiten mit 0 und erhält 0 = 0. Er folgert: „Jede Zahl ist eine Lösung.“ Stimmt das?“

## 2026-11-16 05:42 – STATUS
terme.aufstellen fertig: umgestuft 5 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 2. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - sachsituation S3 „Kletterhalle … Bei wie vielen Besuchen kosten beide gleich viel?“ – Lösung 8 richtig und durch Probieren mit dem Term lösbar; passt als Stufe 3.
  - deuten S3 „Jemand übersetzt … in den Term … Stimmt das?“ prüft Übersetzen statt Deuten – Aufgaben richtig; Deuten von Teiltermen wurde in Runde 10 ergänzt. Die Karte bleibt unverändert.

## 2026-11-16 05:41 – STATUS
bruch.prozent_grundwert fertig: umgestuft 11 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - argumente: Ablenker „Sinkt ein Wert um 100 %, halbiert er sich, denn 100 % ist die Hälfte von 200 %“ – Laut Befund kein Fehler (eindeutig falsch als Ablenker).

## 2026-11-16 05:40 – STATUS
gleichungen.einfach fertig: umgestuft 2 / berichtigt 0 / ersetzt 4 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Bei 3 · x + 5 = 38 wird x = 12 getestet. Links kommt 41 heraus. Ist die Lösung größer oder kleiner als 12?“
  - „Bei 5 · x + 9 = 29 wird x = 3 getestet. Links kommt 24 heraus. Ist die Lösung größer oder kleiner als 3?“
  - „Eine Mutter ist 3-mal so alt wie ihre Tochter. Zusammen sind sie 36 Jahre alt. Wie alt ist die Tochter?“
  - „0 · x = 14. Wie viele Lösungen hat diese Gleichung?“
- nicht umgesetzt:
  - probe S3 „Für welche der Zahlen 3, 4, 5, 6 gilt 2 · x + 7 = 4 · x − 3?“ – Hinweis aus der Liste, kein Mangel: Die Aufgabe passt zur Lernkarte „Probe machen“.

## 2026-11-16 05:40 – STATUS
stochastik.kombinatorik fertig: umgestuft 9 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.

## 2026-11-16 05:39 – STATUS
messen.koerper_berechnung fertig: umgestuft 6 / berichtigt 0 / ersetzt 4 / neu 3 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Ein Würfel hat die Oberfläche 486 cm². Wie lang ist eine Kante?“
  - „Ein Würfel hat die Oberfläche 1014 cm². Wie lang ist eine Kante?“
  - „Zwei gleiche Quader (7 cm lang, 3 cm breit und 5 cm hoch) werden mit den 3 cm × 5 cm großen Flächen aneinandergeklebt. Wie groß ist die Oberfläche des neuen Quaders?“
  - „Zwei gleiche Quader (4 cm lang, 7 cm breit und 4 cm hoch) werden mit den 7 cm × 4 cm großen Flächen aneinandergeklebt. Wie groß ist die Oberfläche des neuen Quaders?“
- nicht umgesetzt:
  - sachaufgaben S2 Aquarium ohne Deckel „anspruchsvoller als manche Stufe-3-Aufgabe“ – Passt auf Stufe 2 (fünf Flächen, ein Gedanke); Stufe 3 enthält Zusatzschritte (Abzüge, Fliesen, Umrechnung).

## 2026-11-16 05:39 – STATUS
messen.flaechen fertig: umgestuft 2 / berichtigt 6 / ersetzt 1 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Ein Rechteck aus 6 · 5 Einheitsquadraten wird in beiden Richtungen doppelt so lang. Wie viele Einheitsquadrate passen jetzt hinein?“

## 2026-11-16 05:38 – STATUS
geometrie.ortslinien fertig: umgestuft 0 / berichtigt 0 / ersetzt 8 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Zwei Sender A und B stehen 7 km auseinander. Ein Handy hat genau 8 km Abstand zu A und genau 4 km Abstand zu B. An wie vielen Stellen kann es sein?“
  - „Zwei Sender A und B stehen 10 km auseinander. Ein Handy hat genau 5 km Abstand zu A und genau 6 km Abstand zu B. An wie vielen Stellen kann es sein?“
  - „g ist die waagrechte Gerade y = −1. Wie viele Punkte mit ganzzahligen Koordinaten auf der senkrechten Linie x = 2 haben von g höchstens den Abstand 3?“
  - „Kreis um A mit r = 2 cm, Kreis um B mit r = 9 cm, [AB] = 6 cm. Wie viele Schnittpunkte haben die Kreise?“
  - „Ein großer Kreis um A hat r = 9 cm, ein kleiner Kreis um B hat r = 4 cm. B liegt im großen Kreis, [AB] = 5 cm. Wie viele gemeinsame Punkte haben die Kreise?“
  - „Kreis um A mit r = 4 cm, Kreis um B mit r = 8 cm, [AB] = 4 cm. Wie viele Schnittpunkte haben die Kreise?“
  - „Ein großer Kreis um A hat r = 8 cm, ein kleiner Kreis um B hat r = 3 cm. B liegt im großen Kreis, [AB] = 5 cm. Wie viele gemeinsame Punkte haben die Kreise?“
  - „Jemand sagt: „Kreise mit r = 3 cm und r = 5 cm, deren Mittelpunkte 1 cm auseinander liegen, schneiden sich, weil 1 cm < 3 cm + 5 cm.“ Stimmt das?“
- für Sebastian:
  - geometrie.ortslinien/zwei_kreise: Die Lernkarte erklärt nur sich schneidende/berührende Kreise; „Kreis im Kreis“ (r₁ − r₂) ist aus den älteren Übungen genommen; die Aufgabe „Welcher Abstand [AB] ist möglich?“ (Runde 10) nutzt die Grenze r₁ − r₂ noch (im Lösungsweg erklärt). Soll die Lernkarte das ergänzen? Außerdem: lehrplan_gym leer, Ortslinien stehen im LehrplanPLUS Gym erst in Jgst. 7 (laut D2 inzwischen Kairo/Kl. 7). Karten-Text nicht geändert.

## 2026-11-16 05:37 – STATUS
geometrie.winkel fertig: umgestuft 1 / berichtigt 0 / ersetzt 3 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Stimmt die Aussage? „Zwei stumpfe Winkel nebeneinander ergeben immer mehr als 180°.““
  - „Ein Karussell hat 3 Gondeln in gleichen Abständen. Um wie viel Grad muss es sich drehen, damit die nächste Gondel an die Stelle der vorigen kommt?“
  - „Ein Karussell hat 5 Gondeln in gleichen Abständen. Um wie viel Grad muss es sich drehen, damit die nächste Gondel an die Stelle der vorigen kommt?“

## 2026-11-16 05:37 – STATUS
geometrie.grundbegriffe fertig: umgestuft 2 / berichtigt 0 / ersetzt 2 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „g geht durch A(−6 | −3) und B(−6 | 0), h geht durch C(4 | −3) und D(8 | −3). Wie liegen g und h zueinander?“
  - „Zwei Kreise haben die Radien 7 cm und 4 cm. Ihre Mittelpunkte sind 3 cm voneinander entfernt. Wie viele gemeinsame Punkte haben sie?“
- für Sebastian:
  - geometrie.grundbegriffe/kreis_lage: Die Lernkarte erklärt nur Kreis und Gerade; die übrigen Stufe-3-Aufgaben zu zwei Kreisen (von außen berühren, getrennt) setzen r₁ + r₂ voraus. Erklärung ergänzen oder Aufgaben belassen? Karten-Text nicht geändert.

## 2026-11-16 05:36 – STATUS
groessen.proportional fertig: umgestuft 4 / berichtigt 0 / ersetzt 2 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Ein Hahn füllt in 4 Minuten einen Eimer mit 48 Litern. Ungefähr wie viele Liter laufen in 20 Minuten?“
  - „Ein Hahn füllt in 2 Minuten einen Eimer mit 24 Litern. Ungefähr wie viele Liter laufen in 20 Minuten?“

## 2026-11-16 05:36 – STATUS
groessen.einheiten fertig: umgestuft 7 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.

## 2026-11-16 05:36 – STATUS
zahlen.potenzen_basis fertig: umgestuft 5 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Welche Zahl ist eine Quadratzahl?“

## 2026-11-16 05:35 – STATUS
zahlen.rechengesetze fertig: umgestuft 5 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.

## 2026-11-16 05:35 – STATUS
zahlen.ganz fertig: umgestuft 10 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.

## 2026-11-16 05:34 – STATUS
groessen.indirekt fertig: umgestuft 0 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 4. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Ein Freizeitpark: Eintritt 3 €, jede Fahrt 4 €. 3 Fahrten kosten mit Eintritt 15 €. Jemand rechnet für 6 Fahrten: 15 · 2 = 30 €. Stimmt das?“
- nicht umgesetzt:
  - erkennen S3 „… Je mehr, desto weniger, also indirekt proportional.“ (4×) – Kein Fehler; Übungsreihe zum selben Fehlschluss mit verschiedenen Beispielen.
  - unterscheiden S1/S2 „Welche Art von Zuordnung zeigt die Tabelle?“ (11×) – Kein Fehler; Stufe 2 hat den zusätzlichen Ablenker „nicht zu entscheiden“ und andere Tabellen.
  - sach S2 „Taxi … Was kosten 6 km?“ (weder noch) – Laut Befund gut als Abgrenzung; Lösung richtig.
  - Überschneidung mit funktionen.gebrochen/„indirekt“ – Reihenfolge im Plan (Haupt-Chat), keine einzelne Aufgabe.
- für Sebastian:
  - groessen.indirekt: lehrplan_gym leer und Überschneidung mit funktionen.gebrochen/„indirekt“ – Reihenfolge im Plan klären. Karten-Texte nicht geändert.

## 2026-11-16 05:34 – STATUS
stochastik.simulation fertig: umgestuft 4 / berichtigt 1 / ersetzt 1 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Ein Bauteil ist fehlerhaft mit p = 5/6. Simuliert wird mit einer Urne mit 7 roten von 10 Kugeln (mit Zurücklegen). Ist das geeignet?“
- nicht umgesetzt:
  - auswerten S3 „Gruppe A 100 / B 50 Durchgänge – wessen Schätzwert …“ (3×) – Kein Fehler; Übungsreihe zum selben Gedanken mit verschiedenen Zahlen.
- für Sebastian:
  - stochastik.simulation: lehrplan_gym leer; Simulation steht im LehrplanPLUS Gym Kl. 8 nicht als eigener Inhalt – als Vertiefung zu Laplace/relative Häufigkeit führen? Karten-Texte nicht geändert.

## 2026-11-16 05:33 – STATUS
stochastik.grundbegriffe fertig: umgestuft 4 / berichtigt 0 / ersetzt 4 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „In einer Urne liegen 9 rote, 3 blaue und 1 grüne Kugeln. Eine wird zufällig gezogen. Wie groß ist P(grün)?“
  - „Ein Kronkorken landete bei 500 Würfen 225-mal mit der Öffnung nach oben. Schätze die Wahrscheinlichkeit dafür auf zwei Nachkommastellen.“
  - „Ein fairer Würfel hat die Zahlen 1 bis 10. Wie groß ist die Wahrscheinlichkeit, KEINE Zahl kleiner oder gleich 1 zu werfen? Gib sie als Dezimalzahl an.“
  - „Ein fairer Würfel hat die Zahlen 1 bis 6. Wie groß ist die Wahrscheinlichkeit, KEINE Zahl kleiner oder gleich 3 zu werfen? Gib sie als Dezimalzahl an.“
- nicht umgesetzt:
  - gegenereignis S3 „3 Würfe, P(mindestens eine Sechs) = 91/216“ – Lösung richtig; Weg über das Gegenereignis (5/6)³ ist echte Stufe 3. Ob die Produktregel in Kl. 8 eingeführt ist, betrifft den Plan.

## 2026-11-16 05:33 – STATUS
raum.schraegbilder fertig: umgestuft 6 / berichtigt 0 / ersetzt 0 / neu 1 / nicht umgesetzt 2. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - koordinaten S2 „Gib die z-Koordinate von C an“ (3× gleicher Typ) – Laut Befund in Ordnung; Lösungen richtig.
  - Karte „laengen“ ≈ messen.koerper_darstellung/„schraegbild“ – Doppelung im Plan (Haupt-Chat), keine einzelne fehlerhafte Aufgabe.
- für Sebastian:
  - raum.schraegbilder: lehrplan_gym leer; Raumkoordinaten und windschiefe Geraden stehen im LehrplanPLUS Gymnasium nicht in Jgst. 8 – Thema im Plan als Vertiefung markieren? Karten-Texte nicht geändert.

## 2026-11-16 05:32 – STATUS
messen.koerper_darstellung fertig: umgestuft 0 / berichtigt 0 / ersetzt 3 / neu 0 / nicht umgesetzt 3. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Welche Aussage ist richtig?“
  - „Welche Aussage ist FALSCH?“
- nicht umgesetzt:
  - zylinder S2 Mantelfläche aus Umfang · Höhe (6×) – Kein Fehler; Übungsreihe mit verschiedenen Zahlen.
  - netz S3 „Netz 442 cm², Grundfläche 7 × 8 cm, Höhe?“ (3×) – Kein Fehler; Übungsreihe (Rückwärtsrechnen) mit verschiedenen Zahlen.
  - Überschneidung der Karten „schraegbild“ mit raum.schraegbilder – Betrifft den Plan (Haupt-Chat), keine einzelne Aufgabe.

## 2026-11-16 05:31 – STATUS
messen.kreisberechnung fertig: umgestuft 4 / berichtigt 1 / ersetzt 0 / neu 0 / nicht umgesetzt 2. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - flaeche S3 Pizzavergleich (3×) – Kein Fehler; Übungsreihe zum selben Typ mit verschiedenen Zahlen, Ablenker gut.
  - verstehen S2 „Jemand rechnet A = 2 · π · r …“ (3×) – Kein Fehler; Übungsreihe mit verschiedenen Zahlen.

## 2026-11-16 05:31 – STATUS
gleichungen.formeln fertig: umgestuft 2 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 2. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „An einem Widerstand R = 10 Ω liegt U = 230 V. Jemand rechnet I = R : U = 0,04 A. Welche Probe zeigt den Fehler?“
- nicht umgesetzt:
  - geometrie S3 Pyramide (V = G · h : 3) – Formel steht in der Aufgabe; als reine Formelanwendung (Umstellen) passend zum Thema, Lösung richtig.
  - einsetzen S3 Dichte mit dm³ (Aluminium, Glas, Eis) – Drei verschiedene Stoffe und Zahlen, alle richtig; Übungsreihe zum gleichen Schritt (dm³ → cm³) ist gewollt.

## 2026-11-16 05:31 – STATUS
zahlen.intervalle fertig: umgestuft 3 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Ein Aquarium braucht Wasser von mindestens 24 °C bis höchstens 28 °C. Welches Intervall beschreibt die erlaubten Temperaturen (in °C)?“
- nicht umgesetzt:
  - enthalten S1 „Welche Zahl liegt im Intervall [1; 7]?“ hat nur 3 Antworten – Zulässig und richtig; kein Fehler.
- für Sebastian:
  - zahlen.intervalle: lehrplan_gym der Karten ist leer – das Thema hat keine eigene LehrplanPLUS-Zeile (Inhalt gehört zu Ungleichungen, Kl. 8). Karten-Text nicht geändert.

## 2026-11-16 05:30 – STATUS
gleichungen.ungleichungen fertig: umgestuft 2 / berichtigt 0 / ersetzt 3 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Für welche x liegt der Graph von y = x + 4 oberhalb der x-Achse?“
  - „Für welche x liegt der Graph von y = 2x − 4 unterhalb der x-Achse?“
  - „Löse 4x + 10 ≤ 4x + 3.“
- nicht umgesetzt:
  - sachaufgabe: Stufen 1 und 2 (Aufzug/Handytarif) inhaltlich gleich – Die Aufgaben sind richtig; Stufe 1 und 2 unterscheiden sich in den Zahlen (Kommazahlen, „angefangene“ km auf Stufe 2). Kein einzelner Fehler; neue Stufe-3-Typen kamen in Runde 10 dazu.

## 2026-11-16 05:30 – STATUS
gleichungen.lgs2 fertig: umgestuft 4 / berichtigt 0 / ersetzt 1 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Ein Händler mischt Erdnüsse zu 10 € pro kg mit Cashewkerne zu 16 € pro kg. Er erhält 13 kg Mischung im Wert von 178 €. Wie viel kg der billigeren Sorte verwendet er?“

## 2026-11-16 05:30 – STATUS
gleichungen.bruch fertig: umgestuft 3 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK.

## 2026-11-16 05:29 – STATUS
terme.bruchterme fertig: umgestuft 4 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - kuerzen S3 (x² − 49)/(x − 7) setzt die 3. binomische Formel voraus – Aufgaben sind richtig und echte Stufe 3. Offen ist nur, ob die binomischen Formeln im Plan vor diesem Thema stehen (Reihenfolge, Haupt-Chat).

## 2026-11-16 05:29 – STATUS
funktionen.gebrochen fertig: umgestuft 5 / berichtigt 0 / ersetzt 0 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- nicht umgesetzt:
  - indirekt: Überschneidung mit groessen.indirekt – Kein Mangel an einer Aufgabe; betrifft die Reihenfolge im Plan (Haupt-Chat).

## 2026-11-16 05:29 – STATUS
funktionen.linear fertig: umgestuft 14 / berichtigt 0 / ersetzt 4 / neu 0 / nicht umgesetzt 0. Prüfskript OK, Nachweis OK. Ersatz zwei_punkte (A(0|2)…) steht jetzt auf Stufe 2 (gleicher Typ wie die andere Stufe-2-Aufgabe).
- ersetzt (alte Fragetexte, bitte sperren):
  - „Liegen A(−1 | −1), B(1 | 1) und C(3 | 3) auf einer Geraden?“
  - „Liegen A(0 | 2), B(2 | 8) und C(4 | 14) auf einer Geraden?“
  - „6 m Stoff kosten 48 €. Wie viel kosten 1 m?“
  - „2 l Saft kosten 3 €. Wie viel kosten 1 l?“

## 2026-11-16 05:28 – STATUS
funktionen.grundbegriffe fertig: umgestuft 3 / berichtigt 0 / ersetzt 3 / neu 0 / nicht umgesetzt 1. Prüfskript OK, Nachweis OK.
- ersetzt (alte Fragetexte, bitte sperren):
  - „Für welches x gilt f(x) = −3, wenn f(x) = −1(x + 1)?“
  - „Für welches x gilt f(x) = −2, wenn f(x) = −1(x + 4)?“
  - „Für welches x gilt f(x) = −4, wenn f(x) = −1(x + 4)?“
- nicht umgesetzt:
  - punkt_graph S2 „Lies am Graphen ab: f(4) = ?“ (gehört eher zu graph_lesen) – Bei erneuter Prüfung passend: Den Punkt (4 | f(4)) am Graphen ablesen gehört zu „Liegt der Punkt auf dem Graphen?“. Lösung richtig, kein Mangel.
- für Sebastian:
  - funktionen.grundbegriffe: Der Eintrag in „offen“ („Kreis kann die App nicht zeichnen“) ist veraltet – die App zeichnet Kreise (koordinaten.kreise). Nur der Haupt-Chat ändert „offen“.
