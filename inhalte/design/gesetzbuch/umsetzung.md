# Vorgabe GB: Regel-Universum – Zeichenstil, Übersicht, eine Regel aufgeschlagen

Designer, 26.11.2026, **Fassung 5 (vierte Runde)**. Stand `lernen-app` f1e499d. Der Ordner heißt weiter `gesetzbuch/`, damit nichts bricht; sichtbar heißt alles „Regel-Universum“. Kein App-Code, keine Datenbank, kein Lernstand.
Mathe-Inhalt wörtlich vom Mathe-Profi (`origin/mathe-profi` 4bd08be – die Lieferung zu Auftrag 15 liegt dort noch nicht: `ebene1.md`, `sonne.md`, `planet-flaeche-und-raum.md`, `planet-geometrie.md`, `inhalt.md`), eingelesen mit `entwurf/inhalt_lesen.py`.
**[G]** gesichert (im Entwurf gebaut und gemessen) · **[A]** Annahme · **[M]** Meinung.

Die frühere Vorgabe RS-H (`inhalte/design/regeln-sonnensystem/`) ist abgelehnt und gilt nicht mehr.

## F5 Vierte Runde – „es ist dasselbe“ sichtbar machen (gilt vor F4 bis F2 und den Abschnitten 0 bis 12)

Anlass: Auftrag des Projektleiters 26.11., 23:30. **Die Lieferung des Mathe-Profis zu Auftrag 15 lag beim Bauen nicht auf seinem Zweig** (letzter Stand dort: Auftrag 14). Deshalb sind die Punkte 1, 3 und 4 nach meiner Lesart gebaut und als Annahme gekennzeichnet.

### F5.1 Die Klassenleiter „gleich gebaut“ [G]
Eine Regel, ihre Beispiele untereinander, eine Zeile je Beispiel, in Festbreitenschrift 17 px (Handy 16 px).

| Spalte | Breite | Inhalt |
|---|---|---|
| 1 | 36 px | Klasse im schwarzen Kreis |
| 2 | so breit wie der längste Text **vor** der wirkenden Stelle | rechtsbündig |
| 3 | so breit wie die längste wirkende Stelle | **gelb mit Rahmen**; ist die Stelle höchstens 6 Zeichen lang, füllt sie die Spalte mittig, sonst linksbündig |
| 4 | Rest | linksbündig, darf umbrechen |

- Durch Spalte 3 läuft von oben nach unten ein blasses gelbes Band (26 % Gelb). So steht die wirkende Stelle in jeder Klasse an derselben Stelle.
- Darunter je Zeile klein: Einführung, Anwendung oder Vorwissen und das Thema der App.
- **Vorsatz:** Ist der Text vor der Stelle lang, steht er grau in einer eigenen Zeile über der Rechnung („4 · (□ − 12) = −20:“), und nur der Rest wird ausgerichtet.
- **Handy, „wo es geht“:** Sind längster Vortext und längste Stelle zusammen über 20 Zeichen, wird unter 560 px nicht ausgerichtet; die Stelle bleibt gelb umrahmt. Gemessen bei 400 px: 12 von 14 Rechenregeln ausgerichtet, nicht ausgerichtet die Regeln 10 und 13.
- Dieselbe Leiter steht im Kasten „Dieselbe Regel in 6 Klassen“ oben in der Übersicht.

### F5.2 Wirkende Stelle bei allen 14 Rechenregeln [A – meine Lesart]
Markiert sind **63 von 74 Beispielen**, nach dem Satz „Wirkstelle“ des Mathe-Profis je Regel. Die Auszeichnung steht in `entwurf/teile/wirkstelle.json`; `bauen.py` prüft, dass jeder Text wörtlich sein Beispiel ist.
**Nicht markiert sind 11 Beispiele, weil die wirkende Stelle nicht in der Zeile steht** (im Entwurf steht das klein dabei): Regel 1 „3 400 m = 3,4 km“ und „15 % = 15 Hundertstel = 0,15“ · Regel 9 „½ = 2/4“, „12/18 = 2/3“, „6x : 9 = 2x : 3“, „Seitenverhältnis 6 : 9 …“ · Regel 11 „15 von 60 sind 25 %“ und „Strahlensatz …“ · Regel 13 „2x + 2 = 12, also …“, „2x² = 18 …“, „3 · 2ˣ = 24 …“. Bitte an den Mathe-Profi: diese Beispiele so schreiben, dass der gemeinsame Faktor, der Wert für eins und die Handlung auf beiden Seiten in der Zeile stehen.

### F5.3 Lücken ehrlich [G, Wortlaut A]
Jede Klasse 5 bis 10 hat in der Leiter eine Zeile. Gibt es kein Beispiel: gestrichelter Kreis und der Satz „Noch kein Beispiel hinterlegt. Ob die Regel in Klasse 9 vorkommt, klärt der Mathe-Profi.“ Sobald er „kommt nicht vor“ liefert, steht dort: „Kommt in Klasse 9 nicht vor.“ (Einlesen noch nicht gebaut, weil sein Format noch nicht vorliegt.)

### F5.4 Klassenleiter für die Ideen der Planeten [vorläufig]
Auf jeder Ideen-Seite: Überschrift „Diese Idee läuft von Klasse 5 bis 8“ und die Regeln der Idee nach der Klasse geordnet, in der sie am Gymnasium zuerst vorkommen (Quelle: Spalte „Gym“ in `inhalt.md`); Regeln nur für Realschule oder IB stehen unter „RS IB“. **Rechenbeispiele je Klasse fehlen**, bis Auftrag 15 Teil B geliefert ist.

### F5.5 „Genau gesagt“ auf der Übersicht – zwei Fassungen zum Wählen [G]
Bild `bilder/vergleich-genau-gesagt-400.jpg`: links mit, rechts ohne. Adresse der zweiten Fassung: `uebersicht-a.html?genau=0`. In der aufgeschlagenen Regel und Idee steht „Genau gesagt“ in beiden Fassungen.
Gemessen bei 400 px: ganze Seite mit 20 697 px, ohne 17 344 px hoch – 16 % kürzer. [M] Der Gewinn ist kleiner als erwartet, weil die Zeichnungen die Höhe bestimmen. Ruhiger wird die Karte trotzdem: Bild, Name, ein Satz, Klassenband.

## F4 Dritte Runde – was jetzt gilt (gilt vor F3, F2 und den Abschnitten 0 bis 12)

Anlass: Auftrag des Projektleiters 26.11., 09:50 Teil 2, Nachtrag 09:57; Antworten und Prüfung des Mathe-Profis (Auftrag 13).

### F4.1 Name [G]
Titelzeile, Brotkrumen, Suchfeld, Seitentitel: **„Regel-Universum“**. Einträge: „Rechenregel“ (Sonne), „Idee“ (Planeten), dahinter „Regel F17“ oder „Formel“. „Gesetzbuch“ und „Gesetz“ kommen in der Anzeige nicht mehr vor – außer in zwei Fachnamen des Mathe-Profis („Potenzgesetze“, „Gesetz der großen Zahlen“). [A] Diese bleiben.

### F4.2 Der Hauptwunsch: dieselbe Regel in vielen Klassen, und worauf sie aufbaut [G]
- **Klassenband** an jeder der 14 Rechenregeln (Übersicht A und aufgeschlagene Regel): sechs Kästchen 5 bis 10, 24 × 22 px, Schrift 13 px. **voll** = eingeführt · **Balken unten** = angewendet · **gestrichelt** = Vorwissen · **leer** = kein Beispiel hinterlegt. Legende einmal im Kopf der Sonne und einmal über der Klassenleiter. Quelle: Tabelle „Dieselbe Regel in vielen Klassen“ in `sonne.md` (Einschätzung des Mathe-Profis, nicht am Lehrplan geprüft).
- **Kasten oben rechts** „Dieselbe Regel in 6 Klassen“ bleibt (Regel 6 von Klasse 5 bis 10).
- **Aufbauen, von der Sonne nach außen:** Jede Ideen-Karte nennt „braucht die Rechenregeln 9, 11“. Jede Regel eines Planeten hat den Abschnitt „Baut auf diesen Rechenregeln auf“ mit Sprung. Jede Rechenregel hat den Abschnitt „Darauf bauen auf: 7 Regeln auf 2 Planeten“ mit den Ideen als Sprung. Quelle: Spalte „Sonne“ in `inhalt.md`.
- **Innerhalb der Sonne:** „erklärbar über Regel 4“ auf der Karte, „Lässt sich erklären über“ in der Regel – mit dem Satz „keine Lernvoraussetzung und keine Sperre“.
- Schicht 1 heißt „Grundrechnen“ (Antwort 6).

### F4.3 Hin und zurück zur Erklärung (Nachtrag) [G]
- In der aufgeschlagenen Rechenregel: Abschnitt „Kommt vor in diesen Themen“, je Thema ein Feld „Rom · Grundrechenarten … · zur Erklärung ›“. Quelle: Spalte „Thema in der App“ der Beispiele.
- Kommt man aus einer Erklärung (`?von=uebung`), steht über dem Kopf eine gelbe Leiste „‹ Zurück zur Erklärung“ (17 px fett, 44 px hoch). Bild `rueckweg-aus-erklaerung-400-hell`.
- Feld „Regel dahinter“, Blatt und Rückweg in der Erklärung und in der Übung: Vorgabe ÜB, `inhalte/design/uebung/umsetzung.md` Abschnitt 5.

### F4.4 Inhalt und Suche [G]
- Zweizeilige Sätze aus `ebene1.md`; Rechenregel 10 mit drei kurzen Sprüchen untereinander.
- „Die wirkende Stelle“ steht je Rechenregel als Satz über der Klassenleiter (Antwort 7). In den Beispielen markiert ist sie nur bei den Regeln 2, 6 und 13.
- Suche findet zusätzlich die 28 einzelnen Formeln („Kegel – Mantel (Kegelmantel)“ ist erster Treffer und führt zu F17).

### F4.5 Zeichnungen: 42 von 42 [G]
Jede der 14 Rechenregeln und jede der 28 Ideen hat ihre Hauptzeichnung; nirgends steht mehr „Zeichnung folgt“ (geprüft: 14 Rechenregeln, 147 Regeln, 28 Ideen).

**Berichtigt nach der Prüfung des Mathe-Profis:** Rechteck-Zeichnung in der Reihenfolge Zahlen mit Plus, mit x, mit Brüchen (neu 3/2 · (4 + ½) = 6 + ¾, Höhe 1,5, Breite 4,5), zuletzt „auch bei Minus“ mit den Werten 108 und 12 · Kreis: Klammer „etwa π · r“ jetzt über 6 Stückbreiten · Drachenviereck: Schild verdeckt keine Kante mehr · Kugel: „h = 2 · r“ · Satz „Pyramide und Kegel füllen je ein Drittel des Körpers darum“ · Zahlengerade: Lot endet über der Rechnung, nur die Minuszeichen sind umrahmt.

**Neu:** zwei Nebenfelder zu Rechenregel 10 (Quadrat mit 12 Feldern für ⅔ · ¾; sechs halbierte Streifen für 6 : ½) und 19 Zeichnungen:

| Planet | Idee | Felder | Was zu sehen ist |
|---|---|---|---|
| Zahlen | Zahlengerade | 1 | −3 bis 3, Punkte −2,5 und −1 gelb umringt, Pfeil „nach rechts wird es größer“ |
| | Bündeln in Zehnern | 2 | zehn Würfel → Zehnerstange; ein Einer → zehn Zehntel; Tauschpfeil mit gelber „10“ |
| | Bausteine | 1 | zwei Bäume für 60, Primzahlen in gelben Kreisen |
| | Schreibweisen | 2 | Streifen über Zahlengerade mit gemeinsamer gelber Linie bei 0,5; Hunderterfeld mit 50 Feldern |
| | Hoch und zurück | 1 | Quadrat 3 × 3, Pfeile „hoch 2“ und „Wurzel“ als Paar |
| Algebra | Term | 2 | zwei Rechenketten; Tabelle mit den zwei gleichen Ausgabe-Spalten gelb umrahmt |
| | Erlaubte Zahlen | 1 | kräftige Gerade mit offenem Ring bei 2, Tabelle „geht nicht“ |
| | Gleichung lösen | 1 | Gerade 2 bis 7, darunter 8, 10, 12, 14 mit Kreuz oder Haken |
| | Höherer Grad | 2 | drei Rechenzeilen mit gelber Null und zwei Kästen; Parabel mit den Schnittpunkten −3 und 2 |
| Geld und Verhältnisse | Größe | 1 | Balken mit Maßband in m (3) und dm (30) |
| | Wert für eins | 1 | doppelte Zahlengerade kg / €, Paar 1 kg – 2,50 € gelb, zwei Bögen „· 2“ |
| | Prozent als Faktor | 2 | Hunderterfeld mit 25 Feldern; Streifen mit Prozent- und Euro-Skala, 80 % – 48 € |
| Funktionen | Zuordnung | 3 | Tabelle, Graph, Gleichung; Wertepaar (2 \| 5) in allen drei gelb |
| | Wachstum | 1 | Gerade (blau, „+2“) und Kurve (Tinte, „·2“ gelb) mit Stufen |
| | Gleichung und Form | 4 | Gerade, Parabel, Hyperbel, Knick; in der Gleichung die formgebende Stelle gelb |
| Daten und Zufall | Kennzahl | 1 | zwei Punktreihen, Dreieck bei Mittelwert 5 genau untereinander |
| | Vom Teil aufs Ganze | 1 | 100 Punkte, 30 gefüllt; zehn zufällige gelb umringt (3 gefüllt), zehn in der Ecke blau gerahmt (8 gefüllt) – beim Bauen nachgezählt |
| | Anteil | 1 | sechs Würfelflächen, 2, 4, 6 gelb mit dickem Rahmen und Haken |
| | Stufen | 1 | Baum für zwei Münzwürfe; ein Pfad gelb hinterlegt, zwei Enden blau gerahmt |

### F4.6 Offen
- Nebenzeichnungen aus der Zeile „Gleiche Zeichnung, andere Beschriftung“ fehlen bis auf Regel 6 und Regel 10 (laut Mathe-Profi kein Muss für die Übersicht).
- „Genau gesagt“ steht auf jeder Karte der Übersicht; dadurch ist die Seite am Handy sehr lang. Vorschlag unverändert: auf der Übersicht weglassen.
- „Darauf bauen auf“ zählt nur, was die Spalte „Sonne“ nennt. Bei manchen Rechenregeln ist die Zahl klein (Regel 6: 7 Regeln); das liegt an den Daten, nicht an der Anzeige.
- Die Abschnitte 0 bis 12 unten beschreiben in Einzelheiten noch Fassung 1.

## F3 Zweite Runde – was jetzt gilt (gilt vor F2 und vor den Abschnitten 0 bis 12)

Anlass: Auftrag des Projektleiters vom 26.11., 09:05; Auftrag 12 des Mathe-Profis (Merksatz + „Genau gesagt“, vier geänderte Zeichen-Vorgaben).

### F3.1 Zwei Zeilen je Satz [G]
- Alle 42 Sätze stehen zweizeilig: **Merksatz** groß und fett (Übersicht 18 px, Gesetz-Seite groß wie bisher), darunter **„Genau gesagt:“** in 16 px, leise. So auf jeder Regel-Karte, jeder Ideen-Karte, im aufgeschlagenen Gesetz, auf der Ideen-Seite und im Zeichnungs-Blatt.
- Einzelne Gesetze (F1 bis F19, G1 bis G30 …) haben nur einen Satz; dort steht keine zweite Zeile.
- Folge: Die Karten der Übersicht sind höher geworden. [M] Am Rechner tragbar, am Handy wird die Seite lang (Bild `a-400-dunkel`). Wenn das stört: „Genau gesagt“ auf der Übersicht weglassen und nur im aufgeschlagenen Gesetz zeigen – der Mathe-Profi nennt das ausdrücklich als zweite Möglichkeit.

### F3.2 Zeichnungen: 23 von 23 [G]
In der Sonne und in den Planeten „Fläche und Raum“ und „Geometrie“ gibt es keine Karte und keine Seite mehr mit „Zeichnung folgt“ (geprüft: 14 Regeln, 49 Gesetze, 9 Ideen). Ein einzelnes Gesetz zeigt die Zeichnung seiner tragenden Idee.

Neu gegenüber F2 (alles 320 Einheiten breit, kleinste Schrift bei 360 px Breite: 13 px):

| Zeichnung | Felder | Wie gebaut |
|---|---|---|
| Regel 1 Stellenwert | 1 | Tafel H, Z, E, z, h mit festem, dickem Komma-Strich; 2,5 oben, 25 unten; zwei gleiche gelbe Pfeile mit Rahmen schräg nach links. |
| Regel 2 Minus heißt umdrehen | 1 | **Neu nach Auftrag 12:** Figur am Start bei 3 mit Blick nach rechts. Je Minuszeichen ein Kehrtwende-Zeichen (gelbes Feld mit Rahmen und U-Pfeil): oben eines, „einmal umdrehen“, unten zwei, „zweimal umdrehen“. Jedes Minus in der Rechnung ist ebenso gelb umrahmt. Starts genau übereinander, Pfeile genau zwei Einheiten. |
| Regel 3 Treppe | 1 | Fünf gleich hohe Stufen (eine Stufe = 2), Null-Linie durchgezogen und beschriftet, an jedem Tritt „+2“ mit Pfeil nach oben, letzte Stufe gelb mit Rahmen über der Null-Linie; darunter 3, 2, 1, 0, (−1) und jeweils „· (−2)“. |
| Regel 4 Reihenfolge | 1 | Vier Stufen von oben nach unten (1 Klammer, 2 Hoch, 3 Punkt · :, 4 Strich + −); Stufe 3 gelb mit Rahmen; rechts 2 + 3 · 4 mit gelbem Rahmen genau um „3 · 4“, dann 2 + 12, dann 14. |
| Regel 5 Kärtchen | 2 | Kärtchen mit dem Zeichen vorn im gelben Feld; Tauschen 25 · 37 · 4 → 25 · 4 · 37 mit Klammer „100“; zwei Körbe „für a“ (+3a, +4a → 7a) und „für b“ (+2b). |
| Regel 7 Kassenzettel | 2 | Zettel mit Klammer um „Einkauf 8 €“ (gelb) und „Rabatt −3 €“ (blau); daneben zwei Rechenzeilen in festen Spalten: „− 8“ steht unter „8“, „+ 3“ unter „− 3“, Paare gleich markiert, Ergebnis 15. |
| Regel 8 Potenzen | 2 | Fünf Zweien in gleichen Abständen; die erste Klammer mit drei Zweien und „2³“ gelb mit Rahmen (Hauptsache), „2²“ und „2⁵“ zweitrangig; Reihe 8, 4, 2, 1, ½, ¼ mit Hochzahlen darüber und „: 2“ dazwischen, Feld 2⁰ = 1 blau umrahmt. |
| Regel 9 zwei Streifen | 1 | Gleich lang, genau untereinander, ½ und 2/4; die gemeinsame Endlinie gelb mit gestrichelter Linie; Pfeile „Zähler und Nenner · 2“ abwärts und „: 2“ aufwärts. |
| Regel 10 drei Streifen | 1 | ½ blau, ⅓ schraffiert, im dritten 3 blaue und 2 schraffierte Sechstel lückenlos, die fünf dick umrahmt mit gelber Maßlinie „5 Sechstel“; Hilfslinien dünn nach unten. |
| Regel 11 Dreisatz | 1 | Tabelle kg / €; mittlere Zeile gelb mit Rahmen, darunter „mittlere Zeile: für eins“; links und rechts dieselben Pfeile mit „: 3“ und „· 5“ in gelben Schildern. Kein Kreuz. |
| Regel 12 Gegenrechnung | 1 | Zwei Reihen, Kästchen genau untereinander; oben nach rechts, unten nach links; „· 4“ und „: 4“ gelb, „− 12“ und „+ 12“ blau; Zwischenwert −5. |
| Regel 14 Nullprodukt | 1 | Zwei gleich große gelbe Kästen, rechts „= 0“ mit gelber Null; darunter je eine eigene Gleichung und Lösung, dazwischen „oder“. |
| Geometrie 1 Winkel an Geraden | 1 | Dreieck mit 50°, 60°, 70° maßstäblich; Parallele durch C mit Parallel-Zeichen; α gelb, β blau, γ schraffiert – bei C lückenlos nebeneinander. |
| Geometrie 2 Gleicher Abstand | 1 + 2 | Hauptzeichnung Kreis (r = 3 cm, vier Radien); eigene Reihe mit Mittelsenkrechte (AB = 4 cm, P 3 cm über der Mitte) und Winkelhalbierende (60°, zwei Lote mit rechtem Winkel). Gleich lange Strecken: gelber Leuchtstift, ein Querstrich. |
| Geometrie 3 Deckungsgleich | 3 | Dreieck 3 cm, 4 cm, 5 cm je einmal gespiegelt, verschoben, um 90° gedreht; Seiten mit einem, zwei, drei Querstrichen auf gelbem Punkt; gleiche Winkel gleiche Bögen; Ecken A, B, C und A′, B′, C′. |
| Geometrie 4 Ähnlich | 1 | Strahlen von S, 2 cm / 4 cm und 3 cm / 6 cm, Parallelen 2,5 cm / 5 cm, maßstäblich; gleiche Winkel gelb; Schild „alles mal 2“. |
| Geometrie 5 Rechtwinkliges Dreieck | 1 | 3 cm, 4 cm, 5 cm mit Quadraten aus 9, 16, 25 Feldern; rechter Winkel und Hypotenuse gelb mit Rahmen. |
| Fläche und Raum 4 Aufklappen | 3 | **Neu nach Auftrag 12:** Quader, halb aufgeklappt, Netz. Gelb = 20 cm², blau = 15 cm², schraffiert = 12 cm² in allen drei Bildern. |

Darstellungsregel ergänzt: Wo zwei oder drei Dinge paarweise zusammengehören, gibt es neben Gelb mit Rahmen eine zweite Markierung (Blau mit blauem Rahmen) und eine dritte (Schraffur). Jede ist auch ohne Farbe unterscheidbar.

### F3.3 Übrige fünf Planeten [G]
Zahlen, Algebra, Geld und Verhältnisse, Funktionen, Daten und Zufall zeigen ihre tragenden Ideen als Karten ohne Zeichnungs-Rahmen: Kurzname, Merksatz, „Genau gesagt“, „n Gesetze dahinter“.

### F3.4 Meine acht Fragen – Antworten des Mathe-Profis fehlen noch (Auftrag 13), deshalb Annahmen [A]
1. Minus oder Plus im Zahlen-Feld: beides, wie in seiner Zeichen-Vorgabe (Feld 1 Plus, Feld 2 Minus).
2. Wirkstelle je Regel: nur bei den Regeln 2, 6 und 13 markiert (von mir gesetzt, `teile/wirkstelle.json`); bei den übrigen elf Regeln stehen die Beispiele ohne Markierung.
3. Zwei Beispiele derselben Klasse: zwei eigene Zeilen (so liefert er sie inzwischen).
4. Mantel und Oberfläche: über seine Stichwörter auffindbar („Kegelmantel“ → F17 als erster Treffer).
5. Doppelter Name „Zahlen“ (Schicht 1 der Sonne und Planet 1): bleibt; die Schicht heißt in der Anzeige immer „Schicht 1 · Zahlen“.
6. bis 8. (Geometrie-Sätze, Zuordnung Gesetz → Idee, Stichwörter): durch `ebene1.md` und `inhalt.md` erledigt.

### F3.5 Offen
- Varianten aus den Vorgaben („Gleiche Zeichnung, andere Beschriftung“) sind nur bei Regel 6 gebaut. Für alle anderen fehlen sie noch (zum Beispiel Stellenwerttafel für 3 400 m = 3,4 km, Treppe und Dreisatz für Prozent, Dreieck im Einheitskreis, Netz von Prisma und Zylinder).
- Regel 10 soll laut Projektleiter drei kurze Sprüche statt eines langen bekommen; die Karte nimmt, was `ebene1.md` liefert.
- Die Zeichnungen sind vom Mathe-Profi noch nicht fachlich geprüft (Teil von Auftrag 13).

## F2 Fassung 2 – was sich gegenüber Fassung 1 geändert hat (gilt vor den Abschnitten 0 bis 12)

Anlass: Zeichen-Vorgaben und 42 Sätze des Mathe-Profis (Auftrag 11). Wo dieser Abschnitt den Abschnitten 0 bis 12 widerspricht, gilt dieser Abschnitt.

### F2.1 Inhalt [G]
- **42 Sätze der Ebene 1** aus `ebene1.md`: 14 Rechenregeln, 28 tragende Ideen auf sieben Planeten (Zahlen 5, Algebra 4, Geld und Verhältnisse 3, Geometrie 5, Fläche und Raum 4, Funktionen 3, Daten und Zufall 4). Alle sieben Planeten zeigen jetzt ihre Ideen. Jede Idee trägt Kurzname (klein, Versalien), Satz (fett, 18 px), „n Gesetze dahinter“.
- **Zuordnung Gesetz → Idee** kommt vom Mathe-Profi. Meine eigene Zuordnung aus Fassung 1 und die fünf Geometrie-Sätze des Projektleiters sind entfernt.
- **Keine Sperren mehr:** „braucht 4“, „baut auf Schicht 1 auf“, „Darauf bauen auf“ sind gestrichen. Der Mathe-Profi nennt nur noch einen „möglichen Erklärweg“ und schreibt ausdrücklich: keine Lernvoraussetzung, keine Sperre. So steht es im Gesetz. An der Sonne steht: „Die Schichten ordnen, sie sperren nichts.“
- **Ein Gesetz aufgeschlagen**, Reihenfolge: Merksatz · Zeichnung · Warum das gilt · Dieselbe Regel in n Klassen (mit Art: Vorwissen, Einführung, Anwendung) · Voraussetzung: wann es gilt · Häufiger Fehler · Verwandt · Möglicher Erklärweg.
- **Suche** nutzt die Stichwörter aus `inhalt.md`. Treffer über ein Stichwort zeigen ein gelb umrahmtes Schild „Stichwort „Kegelmantel“ steht hier“. Auch die 28 Ideen sind Treffer.
- **Zwei Zeilen je Satz (Auftrag 12, noch nicht geliefert):** Der Entwurf ist vorbereitet. Sobald ein Satz ein Feld `genau` hat, steht darunter klein (16 px, leise) „Genau gesagt: …“. Die Merksätze werden sich also noch einmal ändern; an Maßen und Aufbau ändert das nichts. [A] Zwölf Wörter passen in jede Karte.

### F2.2 Regeln für alle Zeichnungen [G]
1. **Maßstäblich.** Nur die Zahlen des Mathe-Profis. Ein Karo ist eine Einheit.
2. **Hervorhebung = Gelb + Rahmen.** Gelb allein trägt nie. In der Zeichnung: gelbe Fläche mit Rahmen in Tinte (4 Einheiten Strich) oder Leuchtstift-Strich mit gestrichelter Linie darauf. In der Rechenzeile: gelb hinterlegt mit Rahmen 1,5 px. Zweite und dritte Farbe, wo Paare nötig sind (Netz): Blau mit blauem Rahmen, Schraffur mit grauem Rahmen.
3. **„·“ ist nur Malzeichen.** In Rechenzeilen und Beschriftungen kein „·“ als Trenner. (Die Kopfzeilen der Seite nutzen „·“ weiter als Trenner – außerhalb jeder Rechnung. [A] Wenn das stört: durch „|“ ersetzen.)
4. **Höhen:** gelber Leuchtstift (8 Einheiten), darauf gestrichelt in Tinte, am Fuß das Zeichen für den rechten Winkel (Quadrat 9 Einheiten mit Punkt). Bei Körpern: h blau gestrichelt mit rechtem Winkel, G gelb mit Rahmen und Buchstabe „G“.
5. **Eine Aussage je Zeile** unter dem Bild. Lange Rechenzeilen brechen nur vor „=“ um.
6. Vier Felder in einer Reihe stehen ab 900 px zu zweit nebeneinander (2 × 2), darunter untereinander.

### F2.3 Die Zeichnungen, wie gebaut [G]

| Zeichnung | Felder | Maße und Beschriftung |
|---|---|---|
| Regel 6 Ausmultiplizieren | 4 | (1) 6 · (20 + 2): 6 × 22 Karos zu 10 Einheiten, Trennstrich bei 20, Felder „120“ und „12“. (2) 6 · (20 − 2): dasselbe Rechteck 20 breit, rechts Stück der Breite 2 gestrichelt und schraffiert, Klammer „20“ darunter. (3) 3 · (x + 2): ohne Karos, x viermal so lang wie 2, Felder „3x“ und „6“; im Satz das Ausklammern rückwärts. (4) ½ · (4 + ⅔): maßstäblich, Felder „2“ und „⅓“. Links immer der Faktor im gelben Schild mit Rahmen und gelbem Balken; in der Zeile ist „6 ·“ beide Male gelb umrahmt. |
| Regel 13 Waage | 3 | Balken immer waagerecht. 2x + 2 = 12 · 2x = 10 · x = 5. Kugeln in zwei Reihen. In Bild 1 sind auf jeder Seite zwei Kugeln gelb und gestrichelt umrahmt; in Bild 2 und 3 steht das Weggenommene als gestrichelter Umriss. Schilder zwischen den Bildern: „− 2 auf beiden Seiten“, „: 2 auf beiden Seiten“. |
| Regel 2 Zahlengerade | 1 | Zwei Geraden von −1 bis 6 in einem Bild, 34 Einheiten je Schritt, beide Starts bei 3 genau übereinander (gepunktetes Lot). Voller Punkt = Start, Ring = Ziel, Bogenpfeil genau zwei Einheiten. Über jeder Geraden die Rechnung; Rechenzeichen und Vorzeichen gelb umrahmt. |
| Idee „Auslegen und zählen“ | 2 | Rechteck 6 cm mal 4 cm aus 24 Quadraten, unterste Reihe gelb umrahmt, „1 cm²“ an einem Quadrat, Zeile „4 Reihen zu je 6 = 24 cm²“. Quader 5 · 4 · 3 aus Würfeln im Schrägbild (45°, Tiefe halb), unterste Schicht gelb umrahmt, an drei Seiten abzählbar, „3 Schichten zu je 5 · 4 = 60 cm³“. |
| Idee „Aus dem Rechteck“ | 4 + 2 | Karo 18 Einheiten = 1 cm. Rechteck, Parallelogramm, Dreieck mit Grundseite 6 cm, Höhe 4 cm: 24, 24, 12 cm². Trapez mit den Zahlen aus F7 (9 cm, 5 cm, Höhe 4 cm, 28 cm²). Schilder: „abschneiden und ansetzen“, „halbieren“, „verdoppeln“. Abgeschnittenes und angesetztes Dreieck gleich schraffiert. Zweite Reihe „Zwei eigene Äste, wieder vom Rechteck aus“: Drachenviereck (Zahlen aus F8: 8 cm, 5 cm, 20 cm²) im Rechteck; Kreis r = 3 cm in 12 Tortenstücken, darunter umgelegt, „etwa π · r“ breit, r hoch. |
| Idee „Aus dem Quader“ | 4 | Alle Körper 102 Einheiten hoch. Quader · Prisma und Zylinder (Schichten gepunktet) · Pyramide im Quader und Kegel im Zylinder · Kugel im passenden Zylinder. Zeilen: „V = G · h“, „V = ⅓ · G · h“, „Kugel = ⅔ des Zylinders“. |
| Idee „Haut des Körpers“ (zusätzlich) | 2 | Quader 5 cm mal 4 cm mal 3 cm im Schrägbild und sein Netz in Kreuzform; Paare gelb (20 cm²), blau (15 cm²), schraffiert (12 cm²); „O = 2 · (20 + 15 + 12) cm² = 94 cm²“ mit denselben drei Markierungen. |

Kleinste Schrift in einer Zeichnung bei 360 px Breite: 13 px. Sätze unter den Bildern (grau, 16 px) sind von mir; sie erklären nur, was man sieht.

### F2.4 Antworten auf die vier Fragen des Mathe-Profis
1. **Feste Grundform, austauschbare Beschriftung: ja**, so ist es gebaut (eine Zeichenfunktion, die Beschriftung ist ein Parameter). Grenze: „dieselbe Form“ und „maßstäblich“ schließen sich bei anderen Zahlen aus. Ich habe maßstäblich gewählt; dadurch ist das Bruch-Rechteck ein flacher Streifen. [M] Wenn Wiedererkennen wichtiger ist als Maßstab, bitte Bescheid – dann bekommen alle vier dieselbe Form und der Hinweis „nicht maßstäblich“.
2. **Originalgröße geht nicht.** Ein Bildschirm-Zentimeter ist nicht verlässlich. Ich nutze Kästchen: ein Karo = 1 cm in der Beschriftung, ohne echte Länge.
3. **Am Handy lesbar ist alles, weil die Felder untereinander stehen** (gemessen bei 360 px). Als ein einziges Bild lesbar wäre keiner der Stammbäume. Deshalb: Hauptzeichnung Rechteck → Parallelogramm → Dreieck → Trapez, Nebenzeichnungen Drachenviereck und Kreis als eigene Reihe. Bitte „Gleicher Abstand“ ebenso als drei getrennte Felder liefern; mehr als vier Felder je Reihe bitte nicht.
4. **Vorgaben für die anderen fünf Planeten: einverstanden, später.** Erst muss der Nutzer den Stil sehen. Früher brauche ich nur eines: ob jede der 28 Ideen genau eine Zeichnung bekommt (für die Übersicht).

### F2.5 Offen nach Fassung 2
- **Gezeichnet: 7 von 23 Vorgaben** (3 Rechenregeln, 4 Ideen Fläche und Raum). **Nicht gezeichnet:** 11 Rechenregeln, 5 Ideen Geometrie – dort steht „Zeichnung folgt“ mit dem Satz „Zu sehen sein wird: …“ aus der Vorgabe.
- Aus den Vorgaben noch nicht gebaut: Zusatzbild (a + b)² zu Regel 6; Zahlengerade in Vierteln und mit Einheit x; Dreieck mit Höhe außerhalb; Buchstaben-Fassungen g, h; Cavalieri-Münzstapel; Netz von Prisma und Zylinder; 9 cm mal 1 cm zu „Fläche ist nicht Umfang“.
- In Übersicht A sind Karten mit und ohne Bild verschieden hoch. Das verschwindet erst, wenn alle 14 Regeln ein Bild haben.
- Prüfliste Abschnitt 10: Muss-Punkte zu „braucht“ und „Darauf bauen auf“ entfallen; neu als **Muss**: Hervorhebung trägt ohne Farbe · jede Höhe mit rechtem Winkel · Zahlen nur aus den Vorgaben · „Kegelmantel“ und „Minus vor der Klammer“ sind erster Treffer.
- Die Abschnitte 1, 2, 5, 9 und 11 unten beschreiben in Einzelheiten noch Fassung 1.

## 0 Kurzfassung

- **Vier Entwürfe zum Anklicken** in `entwurf/`: `uebersicht-a.html`, `uebersicht-b.html`, `gesetz.html`, `zeichnungen.html`. Je eine Datei, Schriften und Inhalt eingebettet. Unten links „Entwurf ⚙“ wechselt die Seiten und hell / dunkel. Bilder: `bilder/` (20 Stück).
- **Zeichenstil „Heft und Tafel“**, gezeigt an den sechs verlangten Zeichnungen (Abschnitt 2).
- **Übersicht in zwei Fassungen:** A „Schnitt von innen nach außen“ und B „Durch die Klassen“. **Empfehlung: A als Seite**, die Tabelle aus B als zweite Ansicht am Rechner (Abschnitt 3).
- **Ein Gesetz aufgeschlagen:** Merksatz groß, Zeichnung, dieselbe Regel in jeder Klasse mit gelber Wirkstelle, wo es nicht gilt, Voraussetzung (Abschnitt 5).
- **Suche** auf jeder Seite über alle 14 Regeln, 152 Gesetze und 8 Arbeitsweisen. „Kegelmantel“ findet „Pyramide und Kegel“ zuerst (Abschnitt 7).
- **Fertig im Sinn der ersten Lieferung:** Sonne ganz, Fläche und Raum ganz. **Nicht fertig:** Geometrie hat fünf Sätze, aber noch keine Zeichnungen; 11 der 14 Rechenregeln haben noch keine Zeichnung; fünf Planeten haben noch keine tragenden Ideen. Diese Stellen sagen im Entwurf selbst „folgt“.

## 1 Was die Seite sagt

Maßstab: Ein Erwachsener ohne Vorwissen sagt nach einer Minute, was die Seite ihm sagt. Dafür stehen oben drei Sätze, bevor irgendein Bild kommt:

> Mathe von Klasse 5 bis 10 steht auf **14 Rechenregeln**. Sie gelten in jeder Klasse und in jedem Gebiet. Darum liegen **sieben Gebiete**, jedes mit wenigen tragenden Ideen. Alle Formeln dahinter findest du über die Suche.

Darunter drei Wegweiser mit Farbpunkt:
- **Die Sonne:** 14 Rechenregeln in vier Schichten, von innen nach außen aufeinander aufgebaut.
- **Sieben Planeten:** die Gebiete, von der Sonne aus immer weiter weg vom reinen Rechnen.
- **Acht Arbeitsweisen:** wie man vorgeht. Sie gelten überall.

Daneben (am Handy darunter) der Beweis für „dieselbe Regel in vielen Klassen“: Kasten „Ein Beispiel · Dieselbe Regel in sechs Klassen“ mit Regel 6 von Klasse 5 bis 10, der Faktor in jeder Zeile gelb.

**Was die Wünsche des Nutzers trägt:**

| Wunsch | Wo man es sieht |
|---|---|
| der gesamte Aufbau, übersichtlich | Schnitt: vier Schichten der Sonne, dann sieben Planeten, dann Arbeitsweisen – eine Richtung, von innen nach außen |
| dieselbe Regel in vielen Klassen | Kasten oben; „Klasse 5–10“ an jeder Regel; die Klassenleiter in jedem Gesetz; Fassung B als ganze Tabelle |
| aufeinander aufbauend | Schichten mit „baut auf Schicht 1 auf“ (aus den Abhängigkeiten gerechnet); „braucht 4“ an jeder Regel; „Voraussetzung“ und „Darauf bauen auf“ im Gesetz; die Zeichnungen der Ideen 2 und 3 sind selbst Folgen |
| sehr anschaulich, einprägsame Bilder | jede Regel und jede Idee hat ihren Platz für eine Zeichnung; sechs sind gezeichnet |
| die Sätze selbst lesbar | der Merksatz ist auf jeder Karte die größte Schrift; kein Inhalt liegt hinter einem Antippen |

## 2 Zeichenstil „Heft und Tafel“

Hell sieht die Zeichnung aus wie im Rechenheft, dunkel wie an der Tafel. Entwurf: `zeichnungen.html`, Bilder `zeichnungen-*`.

### 2.1 Regeln des Stils

| Regel | Wert |
|---|---|
| Strich | 2,5 px in Tinte, runde Enden und Ecken |
| Hilfslinie (Höhe, verdeckte Kante, Zwilling) | 1,75–2 px, gestrichelt 4 / 4 oder 5 / 4 |
| Gelb | **die Stelle, an der das Gesetz wirkt** – und nur die: der Faktor, das abgeschnittene Stück, die Grundfläche, der Zielpunkt. Höchstens eine gelbe Sache je Feld |
| Blau | die Fläche oder Größe, um die es geht (Füllung), und die Höhe (gestrichelt) |
| Schraffur | „kommt weg“ |
| Karos | **nur, wo gezählt wird** (Kästchen = Einheit). Sonst leeres Blatt |
| Beschriftung | Maße und Rechnungen in JetBrains Mono 600, 15–16 Einheiten; Anmerkungen in Space Grotesk 14,5 Einheiten. Auf Farbe bekommt Schrift ein Schild in Papierfarbe |
| Felder | Jede Zeichnung besteht aus 1 bis 4 Feldern, je 280–360 Einheiten breit. Am Rechner nebeneinander mit Pfeil, unter 900 px untereinander mit Pfeil nach unten |
| Schritt | Was zwischen zwei Feldern getan wird, steht als schwarze Kapsel oben im folgenden Feld (16 px / 700) |
| Unter jedem Feld | die Rechnung (Mono 17 px, Wirkstelle gelb hinterlegt) und ein Satz (16 px, leise) |
| Verboten | Figuren, Gesichter, Gegenstände als Schmuck, Farbverläufe, Schatten, Perspektive außer dem Schrägbild |

Schrägbild für Körper: nach hinten 30 Einheiten nach rechts und 18 nach oben; alle Körper als Drahtmodell, verdeckte Kanten gestrichelt, die Grundfläche gelb.

### 2.2 Farben der Zeichnungen

| Zweck | hell (Heft) | dunkel (Tafel) |
|---|---|---|
| Papier | #FFFEFA | #10161E |
| Karo | #C7D8E8 | #243140 |
| Tinte | #11161D | #F2F4F7 |
| leise | #5B6675 | #9AA6B5 |
| Gelb | #FFD23F | #FFD23F |
| Blau, Strich | #1F5FBF | #7CB7FF |
| Blau, Füllung | #D9E8FB | #1B3A5F |
| Rahmen des Felds | 1,5 px #C9C4B6, Radius 16 px | 1,5 px #2E3947 |

### 2.3 Die sechs Zeichnungen

| Nr. | Gesetz | Felder und was zu sehen ist | Rechnung unter dem Feld |
|---|---|---|---|
| 1 | Regel 6 Ausmultiplizieren | Drei Felder, **dieselbe Zeichnung**: Rechteck aus großem Teil (158 breit) und Streifen (60 breit), Höhe 96. Links ein gelber Balken über die Höhe und der Faktor als gelbe Marke. Oben die Breiten, in den Teilen die Flächen, unten eine Klammer mit dem Ganzen. Feld „Zahlen“: der Streifen ist schraffiert und gestrichelt (kommt weg). | 6 · (20 − 2) = 6 · 20 − 6 · 2 · 3 · (x + 2) = 3 · x + 3 · 2 · ½ · (4 + ⅔) = ½ · 4 + ½ · ⅔ |
| 2 | Regel 13 Gleichung als Waage | Drei Felder, die Waage immer waagrecht, im Ständer eine gelbe Marke „=“. Feld 1: links zwei Säckchen x und zwei Kugeln, rechts zwölf Kugeln. Feld 2 (Schritt „beide Seiten − 2“): auf jeder Seite zwei Kugeln nur noch gelb gestrichelt. Feld 3 (Schritt „beide Seiten : 2“): links ein Säckchen und ein gestricheltes, rechts fünf Kugeln und fünf gestrichelte. | 2x + 2 = 12 · 2x = 10 · x = 5 |
| 3 | Regel 2 Plus und Minus mit negativen Zahlen | Zwei Felder, Zahlenstrahl von −1 bis 6, Start bei 3 (schwarzer Punkt). Oben gestrichelt die Blickrichtung des Rechenzeichens, daneben gepunktet „umdrehen“, darunter ein gelber Pfeil „2 Schritte“ zum gelben Zielpunkt. Feld 1: Blick nach rechts, Pfeil nach links auf 1. Feld 2: Blick nach links, Pfeil nach rechts auf 5. | 3 + (−2) = 1 · 3 − (−2) = 5 (gelb: das Minus in der Klammer) |
| 4 | Idee „Messen heißt auslegen und zählen“ | Ein Feld: Rechteck aus 6 mal 4 Quadraten (je 34 Einheiten). Oberste Reihe blau, „6 Quadrate in einer Reihe“; links Klammer „4 Reihen“; ein Quadrat unten links gelb mit „1 cm²“; Maße „6 cm“, „4 cm“. | 4 · 6 = 24 Quadrate, also 24 cm² |
| 5 | Idee „Aus dem Rechteck entsteht jede Fläche“ | Vier Felder auf Karos (20 Einheiten), alle mit Grundseite 6 und Höhe 4, damit man nachzählen kann. Rechteck → (Schritt „abschneiden und ansetzen“) Parallelogramm, das linke Dreieck gelb, Pfeil nach rechts, dort gestrichelt → (Schritt „halbieren“) Dreieck mit gestricheltem Zwilling → (Schritt „auch halbieren“) Trapez 6 und 3 mit gestricheltem Zwilling. | 6 · 4 = 24 · 6 · 4 = 24 · 6 · 4 : 2 = 12 · (6 + 3) · 4 : 2 = 18 |
| 6 | Idee „Aus dem Quader entsteht jeder Körper“ | Drei Felder im Schrägbild, Grundfläche G gelb, Höhe h blau gestrichelt. Quader mit zwei gepunkteten Schichten, „Schicht auf Schicht“ → (Schritt „andere Grundfläche“) Dreiecksprisma und Zylinder mit denselben Schichten → (Schritt „ein Drittel“) Pyramide in ihrem gepunkteten Quader, Kegel in seinem gepunkteten Zylinder. | Volumen = G · h · Volumen = G · h · Volumen = ⅓ · G · h |

Alle Zahlen sind nachgerechnet [G]: 6 · 18 = 120 − 12 = 108; ½ · 4⅔ = 2⅓; 2 · 5 + 2 = 12; Parallelogramm 24, Dreieck 12, Trapez 18 Kästchen.

## 3 Übersicht – zwei Fassungen

### 3.1 Fassung A „Schnitt von innen nach außen“ (Bilder `a-*`)

Die Seite ist ein Schnitt vom Kern der Sonne nach außen. Man liest sie von oben nach unten und damit von innen nach außen.

| Teil | Inhalt | Maße |
|---|---|---|
| Kopf (bleibt stehen) | Marke „Gesetzbuch der Mathematik“ (unter 700 px: „Gesetzbuch“), Suchfeld „Suchen, z. B. Kegelmantel“ | 60 px hoch; Suchfeld 44 px, höchstens 420 px breit |
| Einstieg | Titel, drei Sätze, drei Wegweiser; daneben der Kasten „Dieselbe Regel in sechs Klassen“ | Titel 30 px, ab 980 px 40 px; Sätze 19 px; ab 980 px zwei Spalten |
| Sonne | vier Bänder untereinander, jedes mit gebogenem unteren Rand; das nächste Band schiebt sich 40 px darunter. Im ersten Band der Kopf „Die Sonne: 14 Rechenregeln“ mit einem kleinen Bild der vier Ringe (92 px) | Bogen: Ellipse 50 % × 44 px. Schein unter dem letzten Band: 70 px, Gelb 30 % |
| Band-Titel | Kapsel „SCHICHT 1“ (schwarz, gelbe Mono-Schrift 13 px), Name 21 px / 700, dahinter „der Kern: Darauf baut alles auf“ bzw. „baut auf Schicht 1 auf“ / „baut auf Schicht 1 und 2 auf“ | – |
| Regel-Karte | Zeichnung (erstes sprechendes Feld, ohne Anmerkungen) oder Platz „Zeichnung folgt“ · „REGEL 6“ und Name (16 px, leise) · **Merksatz 18 px / 700** · unten „Klasse 5–10“ und „braucht 4“ | 1 Spalte; ab 640 px 2; ab 1100 px 4 (bei drei Regeln 3). Radius 16 px, innen 12–14 px |
| Planeten | sieben Zeilen, jede endet mit einer gebogenen Linie (ihre Bahn). Links Scheibe 52 px mit Zeichen, Name 22 px / 700, „5. Planet · 19 Gesetze · Klasse 5–10“. Rechts die tragenden Ideen als Karten: Zeichnung, **Satz 18 px / 700**, „8 Gesetze dahinter“ | ab 900 px: 250 px + Rest; Ideen 1 Spalte, ab 640 px 2, ab 1100 px 3 (bei vier Ideen 4) |
| Arbeitsweisen | acht gestrichelte Kästen: Name (16 px, leise), Merksatz 17 px / 700 | 1 Spalte; ab 640 px 2; ab 1100 px 4 |

Farben der Bänder, in hell und dunkel gleich, Schrift darauf immer #11161D: Schicht 1 #F59E00 · Schicht 2 #FFB81F · Schicht 3 #FFD23F · Schicht 4 #FFE68C. Die Karten auf den Bändern haben die Flächenfarbe der Gestaltung.

Seitenlänge [G]: 1280 px etwa 4700 px, 820 px etwa 7100 px, 400 px etwa 8800 px, 360 px etwa 9100 px. Kein Querscrollen.

### 3.2 Fassung B „Durch die Klassen“ (Bilder `b-*`)

- **Ab 900 px:** eine Tabelle. Zeilen = die 14 Regeln, gruppiert unter vier farbigen Schicht-Zeilen. Erste Spalte 300 px: „REGEL 6“, Name, Merksatz 16 px / 700. Sechs Spalten Klasse 5 bis 10, in jeder Zelle das Beispiel dieser Klasse (Mono 14,5 px). Über den Zellen von der ersten bis zur letzten Klasse läuft ein gelber Strich 5 px: der Strahl der Regel. Mindestbreite 1100 px, darunter scrollt die Tabelle quer in ihrem Rahmen.
- **Unter 900 px:** je Regel eine Karte: Name, Merksatz 18 px / 700, ein Streifen aus sechs Kästchen 5 bis 10 (gelb = kommt vor), darunter alle Beispiele als Liste „Kl. 5 …“.
- Planeten und Arbeitsweisen wie in A.

### 3.3 Empfehlung

**A als Seite [M].** A zeigt den Aufbau als ein Bild, die Merksätze sind groß, und die Zeichnungen haben Platz. B zeigt „dieselbe Regel in vielen Klassen“ am vollständigsten, ist aber eine Tabelle mit 71 Rechnungen: am Rechner gut zum Nachsehen, als erste Seite zu dicht, am Handy sehr lang. Vorschlag: A ist die Übersicht; am Rechner führt ein Umschalter „Aufbau | Durch die Klassen“ zur Tabelle aus B. Im Entwurf sind es zwei Dateien.

## 4 Verhalten

| Thema | Vorgabe |
|---|---|
| Ohne Antippen | Jeder Merksatz, jede tragende Idee und jede Arbeitsweise steht ausgeschrieben auf der Übersicht. Antippen führt nur zu mehr (Zeichnung groß, Klassen, Fehler, Formeln). |
| Antippen | Regel-Karte → Gesetz. Idee-Karte → Idee mit ihren Gesetzen. Marke im Kopf → Übersicht. Jede Fläche mindestens 44 px hoch. |
| Tastatur, Vorleser | Karten sind Verweise in Lesereihenfolge; jede Zeichnung hat einen beschreibenden Text; Fokus 3 px in Textfarbe. |
| Laden | Der Inhalt wird als feste Datei mit der App ausgeliefert (Vorschlag an den Bau, wie `daten/jugendwoerter.json`). Dann gibt es keinen Ladezustand und die Seite geht ohne Netz. |
| Fehler | Fehlt die Datei: im Seitenbereich „**Das Gesetzbuch ist gerade nicht zu erreichen.**“ / „Prüfe das Internet und versuch es nochmal.“ / Knopf „Nochmal versuchen“. Kein Technik-Text. Nicht im Entwurf gebaut. |
| Leere Suche | „Nichts gefunden für „…“ – Versuch ein einzelnes Wort, zum Beispiel „Kegel“, „Prozent“ oder „Klammer“.“ |
| Bewegung | Keine. Damit ist „weniger Bewegung“ erfüllt. |
| Lernstand | Keiner: keine Monde, keine Balken, keine Häkchen. |
| Weg von der Lernreise | Nicht Teil dieser Vorgabe. Die drei Wege aus RS-H (Reisekarte, nach einem Fehler, neues Thema) passen weiter, sobald der Nutzer sie wieder will. |

## 5 Ein Gesetz aufgeschlagen (Bilder `gesetz-*`)

Entwurf: `gesetz.html` zeigt Regel 6. Dieselbe Seite öffnet jede Regel und jedes Gesetz.

| Nr. | Teil | Inhalt und Maß |
|---|---|---|
| 1 | Pfad | „Übersicht › Sonne › Schicht 2: Klammern und Potenzen“ bzw. „Übersicht › Fläche und Raum › Aus dem Quader entsteht jeder Körper.“ 16 px, Verweise 44 px hoch |
| 2 | Kopf | Über-Zeile „RECHENREGEL 6 VON 14 · KLASSE 5–10“; Name 22 px in leise; **Merksatz 30 px / 700, ab 900 px 40 px** |
| 3 | Die Zeichnung | alle Felder mit Rechnung und Satz. Fehlt sie: gestrichelter Kasten „Zeichnung folgt“ mit der Bildbeschreibung des Mathe-Profis |
| 4 | Warum das gilt | zwei bis drei Sätze, 18 px |
| 5 | Dieselbe Regel in jeder Klasse | Leiter: links ein gelber Strich 4 px, darauf je Klasse ein schwarzer Kreis 36 px mit der Zahl; rechts das Beispiel (Mono 16 px) und darunter Ort und Thema der App (15 px). **Die Wirkstelle ist in jeder Zeile gleich gelb hinterlegt**; darüber ein Satz, was gelb ist |
| 6 | Wo es nicht gilt · häufiger Fehler | gestrichelter Kasten in Rot-Tönen, 18 px |
| 7 | Voraussetzung | „Das musst du vorher können:“ mit Verweis-Knöpfen (44 px); „Darauf bauen auf:“ ebenso. Ohne Voraussetzung: „Keine. Dieses Gesetz ist ein Anfang.“ |

Ab 1040 px zwei Spalten wie ein aufgeschlagenes Buch: links 3 und 4, rechts 5 bis 7. Darunter eine Spalte in der Reihenfolge 3, 4, 5, 6, 7.

Wirkstelle für Regel 6 (Text wörtlich vom Mathe-Profi, **fett** = gelb):
- Klasse 5: **6** · 98 = **6** · 100 − **6** · 2 = 588
- Klasse 6: **4** · 2,5 = **4** · 2 + **4** · 0,5 = 10
- Klasse 7: **3** · (x + 2) = **3**x + 6 · zweite Zeile: (a + b)² = a² + 2ab + b²
- Klasse 8: (3x + 6) : (x + 2) = **3** · (x + 2) : (x + 2) = 3
- Klasse 9: x² + 5x = **x** · (x + 5)
- Klasse 10: x³ − 4x = **x** · (x² − 4)

Farben des Fehler-Kastens: hell Grund #FFF0EE, Rand #B3261E, Über-Zeile #7A1712 · dunkel Grund #2A1A1C, Rand #FF8A8A, Über-Zeile #FFC9C9.

## 6 Von der tragenden Idee zu den Formeln (Bilder `idee-*`)

Seite einer Idee: Über-Zeile „FLÄCHE UND RAUM · TRAGENDE IDEE 2 VON 3“; der Satz als Überschrift (32 px, ab 900 px 42 px); ein Satz dazu; die Zeichnung; dann „8 Gesetze und Formeln, die daraus folgen“ als Karten (ab 900 px zwei Spalten): Nummer, Name 18 px / 700, Merksatz 16,5 px, Klasse. Antippen öffnet das Gesetz (Abschnitt 5). Dort führt der Pfad zurück zur Idee.

## 7 Suche (Bilder `suche-*`)

- Sucht in Name, Merksatz, Beispielen und „Wo es nicht gilt“ aller 14 Regeln, 152 Gesetze und 8 Arbeitsweisen. Ab drei Buchstaben erscheinen Treffer beim Tippen.
- Zusammengesetzte Wörter werden zerlegt: „Kegelmantel“ trifft „Kegel“ und „Mantel“. Umlaute und Groß- und Kleinschreibung spielen keine Rolle.
- Gewicht: Treffer im Namen 6, im Merksatz 3, im übrigen Text 1; höchstens 12 Treffer.
- Jeder Treffer zeigt zuerst den Ort („Fläche und Raum › Aus dem Quader entsteht jeder Körper.“), dann Nummer und Name, den Merksatz und die Klasse. Man muss den Planeten nicht kennen.
- Geprüft [G]: Kegelmantel → Pyramide und Kegel · Pythagoras → Satz des Pythagoras · Minusklammer → Minus vor der Klammer · Prozent · Dreisatz · Trapez.

## 8 Grundfarben der Seite

Aus der App (`style.css` Zeile 3641 und 3644), unverändert: Grund #0B0F14 / #F3F1EA · Fläche #151B24 / #FFFFFF · Text #F2F4F7 / #11161D · leise #A9B3C1 / #4A5563 · Linie #2E3947 / #C9C4B6 · Akzent #FFD23F.
Planeten-Scheiben (nur als Zeichen, Schrift darauf #11161D): Zahlen #FF8A66 · Algebra #A99BFF · Geld und Verhältnisse #B4E86A · Geometrie #3AD6C5 · Fläche und Raum #5AAEFF · Funktionen #FF9BD0 · Daten und Zufall #FFC46B.
Schrift: Space Grotesk; Rechnungen, Nummern und Über-Zeilen in JetBrains Mono.

## 9 Was vom Mathe-Profi stammt und was von mir

| Vom Mathe-Profi, wörtlich | Von mir |
|---|---|
| alle Merksätze, „Warum“, „Wo es nicht gilt“, Beispiele je Klasse, Abhängigkeiten, vier Schichten, sieben Planeten mit Zahlen und Abschnitten, acht Arbeitsweisen | Reihenfolge und Gestalt der Seite, die drei Sätze im Einstieg, die Wegweiser |
| die drei Ideen von „Fläche und Raum“ und der Satz darunter | **welche Gesetze hinter welcher Idee stehen [A]:** Idee 1: F1, F3, F11 · Idee 2: F2, F4–F10 · Idee 3: F12–F19 |
| die Sätze der fünf Geometrie-Ideen (aus G6, G10, G15, G20, G24; Auswahl ist der Vorschlag des Projektleiters) | Zuordnung der Geometrie-Gesetze nach den vier Abschnitten [A]; je Geometrie-Idee ein Bild-Vorschlag (steht im Entwurf als „Vorschlag des Designers“) |
| Bildbeschreibungen der 14 Regeln und 19 Gesetze | die sechs Zeichnungen selbst und der Stil |
| – | die gelben Wirkstellen in den Beispielen der Regeln 6, 13 und 2. `bauen.py` prüft, dass der Text ohne Markierung wörtlich dem Beispiel entspricht |

## 10 Prüfliste

**Muss**
- M1 Die Übersicht zeigt ohne Antippen: 14 Merksätze in vier Schichten, sieben Planeten in der Reihenfolge von `inhalt.md`, je Planet seine tragenden Ideen als Satz, acht Arbeitsweisen.
- M2 Der Merksatz ist auf jeder Regel- und Idee-Karte die größte Schrift (18 px / 700); der Name steht kleiner darüber.
- M3 Jede Schicht nennt, worauf sie aufbaut; der Text ist aus den Abhängigkeiten gerechnet, nicht fest eingetragen.
- M4 Bei 360, 400, 820 und 1280 px ragt nichts seitlich hinaus (Ausnahme: die Tabelle in B scrollt in ihrem Rahmen).
- M5 Zeichnungen nach Abschnitt 2: Gelb nur an der Wirkstelle, Karos nur beim Zählen, keine Schmuck-Elemente; Farben hell und dunkel aus 2.2.
- M6 Die sechs Zeichnungen zeigen genau, was in 2.3 steht; Rechnungen wörtlich.
- M7 Schrift in Zeichnungen ist bei 360 px Breite mindestens 13 px groß; Felder rutschen unter 900 px untereinander.
- M8 Gesetz-Seite mit allen sieben Teilen aus Abschnitt 5 in dieser Reihenfolge; die Wirkstelle ist in jeder Klassen-Zeile gleich hervorgehoben.
- M9 Die Suche steht auf jeder Seite, findet „Kegelmantel“ → „Pyramide und Kegel“ an erster Stelle und zeigt bei jedem Treffer den Ort.
- M10 Von jeder Idee führt ein Antippen zu ihren Gesetzen, von jedem Gesetz der Pfad zurück.
- M11 Kein Lernstand in irgendeiner Form.
- M12 Fließtext mindestens 16 px. Ausnahmen: Über-Zeilen und Nummern in Mono 13 px, Klassen-Angaben 13–15 px, Rechnungen der Tabelle in B 14,5 px.
- M13 Jede Tippfläche mindestens 44 px hoch; Fokus sichtbar; jede Zeichnung hat einen beschreibenden Text.
- M14 Kein Technik-Text bei Fehlern.

**Soll**
- S1 Die Bänder der Sonne haben den gebogenen unteren Rand, die Planeten-Zeilen ihre gebogene Bahn.
- S2 Auf der Übersicht erscheint an jeder Regel und Idee die Zeichnung klein, ohne Anmerkungs-Texte.
- S3 Unter jedem Klassen-Beispiel stehen Ort und Thema der App.
- S4 „Darauf bauen auf“ im Gesetz.
- S5 Treffer erscheinen beim Tippen ab drei Buchstaben.

**Kann**
- K1 Umschalter „Aufbau | Durch die Klassen“ am Rechner.
- K2 Gesetz-Seite ab 1040 px zweispaltig.
- K3 Entdecker-Inseln (5 Gesetze, nur IB) als kleiner Eintrag hinter den Planeten; im Entwurf nur über die Suche erreichbar.

## 11 Fragen an den Mathe-Profi

1. **Zeichnung 1, Zahlen-Feld:** Der Auftrag nennt 6 · (20 − 2). Mit Minus ist es nicht wörtlich „dieselbe Zeichnung“ wie 3 · (x + 2): Der Streifen kommt einmal weg und einmal dazu. Ich habe dieselbe Geometrie genommen und den Streifen schraffiert. Lieber ein Plus-Beispiel (dein Klasse-6-Beispiel 4 · (2 + 0,5))? Dann wären alle drei Felder bis auf die Beschriftung gleich.
2. **Zeichnung 3:** Lesart „Rechenzeichen = Blickrichtung, Minus in der Klammer = umdrehen“. Trägt das für dich, auch für 3 + (+2)?
3. **Zuordnung Gesetz → Idee** (Abschnitt 9): bitte bestätigen oder ändern. F2 Rechteck steht bei mir unter Idee 2, könnte auch unter Idee 1 stehen.
4. **Trennzeichen:** In den Beispielen trennt „ · “ sowohl zwei Beispiele als auch zwei Faktoren („(−7) + 4 = −3 · 9 − (−5) = 14“). Bitte zwei Beispiele als zwei Einträge liefern.
5. **Kegelmantel:** Die Suche findet das Gesetz F17, aber die Formel für den Mantel steht nur im Beispiel („Mantel 15 · π“). Wenn Ebene 2 jede Formel einzeln finden soll, braucht sie eigene Einträge für Mantel und Oberfläche.
6. **Zwei Mal „Zahlen“:** Schicht 1 der Sonne und der erste Planet heißen beide „Zahlen“. Ein anderer Name für die Schicht (z. B. „Grundrechnen“) würde die Übersicht klarer machen.
7. **Wirkstelle:** Für Regel 6 ist sie eindeutig (der Faktor). Bitte je Regel festlegen, was markiert wird; für Regel 13 und 2 habe ich je einen Vorschlag gemacht.
8. **Geometrie:** fünf Bild-Vorschläge stehen im Entwurf auf den Idee-Seiten. Bitte festlegen, was genau zu sehen sein muss.

## 12 Nicht geprüft, Annahmen

**Geprüft [G]:** alle vier Entwürfe in Chrome ohne Fenster bei 360 × 640, 400 × 860, 820 × 1180 und 1280 × 800, hell und dunkel. Keine Skriptfehler; 14 Regeln und 7 Planeten auf beiden Übersichten; Klickfolge Regel → Gesetz → Voraussetzung → Übersicht → Idee → Gesetz → Suche; sieben Suchwörter; nichts ragt seitlich hinaus; keine Tippfläche unter 44 px; kleinste Schrift in einer Zeichnung 13,4 px bei 360 px Breite.

**Nicht geprüft**
- Der Maßstab „ein Erwachsener versteht es in einer Minute“: mit niemandem erprobt.
- Echte Geräte, Finger, Safari und Firefox; Vorleser nur als Text gesetzt.
- Kontrast nicht gemessen; die Grundfarben sind die der App.
- Fachliche Richtigkeit der Zeichnungen durch den Mathe-Profi (seine genauen Vorgaben je Zeichnung lagen noch nicht vor).
- Ob die Bild-Beschreibungen des Mathe-Profis für die 11 offenen Regeln im selben Stil zeichenbar sind (einige nennen Gegenstände: Pizza, Kassenzettel, Körbe).

**Annahmen**
- Die ersten sechs Zeichnungen dürfen von den Bild-Beschreibungen des Mathe-Profis abweichen, wo der Auftrag des Projektleiters etwas anderes nennt (Zahlenstrahl ohne Figur, Waage wie beschrieben).
- Der Inhalt bleibt in der Form von `sonne.md` und `planet-*.md`; `inhalt_lesen.py` liest genau diese Form.
- Die fünf Geometrie-Sätze sind ein Vorschlag und können sich ändern; der Entwurf zieht sie aus `teile/ideen.js`.
