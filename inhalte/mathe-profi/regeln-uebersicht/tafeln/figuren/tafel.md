# Figuren: Winkel, Dreiecke, Vierecke, Kongruenz – Tafel

Winkelarten, Dreiecke, Vierecke mit Haus der Vierecke und Kongruenzsätze.

Stand 2026-11-27. Entwurf: nichts ist in die App eingespielt; geprüft mit `../pruefen.py`. Spalte „ab“ = frühester Beleg im Bestand (Gym = Gymnasium Bayern, RS = Realschule Bayern, IB = IB MYP); „Regel“ = passende Kennung im Regel-Universum.

## Winkelarten

| Kennung | Art | Bereich | Erkennen | Beispiel | ab |
|---|---|---|---|---|---|
| fg-01 | spitzer Winkel | 0° < α < 90° | kleiner als eine Heftecke | 45° | Gym 5 · RS 5 · IB 1 |
| fg-02 | rechter Winkel | α = 90° | genau eine Heftecke; im Bild mit einem kleinen Viereck am Scheitel markiert | 90° | Gym 5 · RS 5 · IB 1 |
| fg-03 | stumpfer Winkel | 90° < α < 180° | größer als eine Heftecke, aber nicht ganz gerade | 135° | Gym 5 · RS 5 · IB 1 |
| fg-04 | gestreckter Winkel | α = 180° | die Schenkel bilden eine gerade Linie | 180° | Gym 5 · RS 5 · IB 1 |
| fg-05 | überstumpfer Winkel | 180° < α < 360° | mehr als eine gerade Linie, aber noch keine ganze Drehung | 235° | Gym 5 · RS 5 · IB 1 |
| fg-06 | Vollwinkel | α = 360° | eine ganze Drehung; die Schenkel liegen wieder aufeinander | 360° | Gym 5 · RS 5 · IB 1 |

## Winkelsumme im Dreieck

- Formel: α + β + γ = 180°
- Bedingung: ebenes Dreieck mit den Innenwinkeln α, β, γ
- So geht es: Addiere die zwei bekannten Winkel. Ziehe die Summe von 180° ab.
- Beispiel: γ = 180° − 50° − 60° = 70°; Probe: 50° + 60° + 70° = 180°

## Dreiecksarten

| Kennung | Art | nach | Definition | Eigenschaften | Beispiel | ab |
|---|---|---|---|---|---|---|
| fg-08 | Allgemeines (ungleichseitiges) Dreieck | seiten | Keine zwei Seiten sind gleich lang. | Alle drei Winkel sind verschieden groß. | Seiten 4 cm, 5 cm, 6 cm | ohne Beleg |
| fg-09 | Gleichschenkliges Dreieck | seiten | Mindestens zwei Seiten sind gleich lang. Die gleich langen Seiten heißen Schenkel, die dritte heißt Basis. | Die beiden Basiswinkel (an der Basis) sind gleich groß. Es gibt mindestens eine Symmetrieachse: von der Spitze zur Mitte der Basis. | Seiten 5 cm, 5 cm, 8 cm \| Winkel 70°, 70°, 40° | Gym 7 · RS 7 · IB 3 |
| fg-10 | Gleichseitiges Dreieck | seiten | Alle drei Seiten sind gleich lang. Es ist ein Sonderfall des gleichschenkligen Dreiecks. | Alle drei Winkel sind 60° groß. Es gibt drei Symmetrieachsen. | Seiten 6 cm, 6 cm, 6 cm \| Winkel 60°, 60°, 60° | Gym 7 · RS 7 · IB 2 |
| fg-11 | Spitzwinkliges Dreieck | winkel | Alle drei Winkel sind kleiner als 90°. | Alle drei Höhen liegen innerhalb des Dreiecks. | Winkel 70°, 60°, 50° | ohne Beleg |
| fg-12 | Rechtwinkliges Dreieck | winkel | Ein Winkel ist genau 90°. Die Seite gegenüber heißt Hypotenuse, die zwei anderen Seiten heißen Katheten. | Die beiden anderen Winkel sind spitz und ergeben zusammen 90°. Die Hypotenuse ist die längste Seite. | Winkel 90°, 35°, 55° \| Seiten 3 cm, 4 cm, 5 cm | Gym 9 · RS 9 · IB 3 |
| fg-13 | Stumpfwinkliges Dreieck | winkel | Ein Winkel ist größer als 90° (und kleiner als 180°). | Die beiden anderen Winkel sind spitz. Eine Höhe liegt außerhalb des Dreiecks. | Winkel 120°, 35°, 25° | Gym 6 · RS 6 |

In jedem ebenen Dreieck gilt α + β + γ = 180°.

## Vierecke

| Kennung | Viereck | Seiten | Winkel | Diagonalen | Symmetrieachsen | punktsymmetrisch | Einordnung | ab |
|---|---|---|---|---|---|---|---|---|
| fg-14 | Quadrat | Alle vier Seiten sind gleich lang; Gegenseiten sind parallel. | Alle vier Winkel sind 90°. | Die Diagonalen sind gleich lang, halbieren sich und stehen senkrecht aufeinander. | 4 | ja | Sonderfall von Rechteck und Raute; damit auch von Parallelogramm, Drachenviereck, gleichschenkligem Trapez und Trapez. Nicht jedes Rechteck und nicht jede Raute ist ein Quadrat. | Gym 5 · RS 5 · IB 1 |
| fg-15 | Rechteck | Gegenseiten sind gleich lang und parallel. | Alle vier Winkel sind 90°. | Die Diagonalen sind gleich lang und halbieren sich. | 2 (beim Quadrat 4) | ja | Sonderfall von Parallelogramm und gleichschenkligem Trapez; damit auch von Trapez. Nicht jedes Rechteck ist ein Quadrat. | Gym 5 · RS 5 · IB 1 |
| fg-16 | Raute | Alle vier Seiten sind gleich lang; Gegenseiten sind parallel. | Gegenüberliegende Winkel sind gleich groß. | Die Diagonalen halbieren sich und stehen senkrecht aufeinander. | 2 (beim Quadrat 4): die beiden Diagonalen | ja | Sonderfall von Parallelogramm und Drachenviereck; damit auch von Trapez. Nicht jede Raute ist ein Quadrat. | Gym 5 · RS 5 · IB 1 |
| fg-17 | Parallelogramm | Gegenseiten sind gleich lang und parallel. | Gegenüberliegende Winkel sind gleich groß; benachbarte Winkel ergeben zusammen 180°. | Die Diagonalen halbieren sich. | keine (bei Rechteck und Raute 2, beim Quadrat 4) | ja | Sonderfall von Trapez. Nicht jedes Parallelogramm ist ein Rechteck oder eine Raute. | Gym 5 · RS 5 · IB 1 |
| fg-18 | Trapez | Mindestens ein Paar gegenüberliegender Seiten ist parallel (Vereinbarung, siehe unten). | Die beiden Winkel an jedem Schenkel ergeben zusammen 180°. | Keine besondere Eigenschaft, die für jedes Trapez gilt. | keine (beim gleichschenkligen Trapez 1) | nein | Kein Sonderfall von einem anderen besonderen Viereck, nur vom allgemeinen Viereck. Nicht jedes Trapez ist ein Parallelogramm. | Gym 5 · RS 5 · IB 1 |
| fg-19 | Gleichschenkliges Trapez | Ein Paar paralleler Seiten; die beiden anderen Seiten (Schenkel) sind gleich lang. | Die beiden Winkel an jeder parallelen Seite sind gleich groß. | Die Diagonalen sind gleich lang. | 1 (beim Rechteck 2, beim Quadrat 4): durch die Mitten der parallelen Seiten | nein | Sonderfall von Trapez. Nicht jedes Trapez ist gleichschenklig. | Gym 7 · RS 6 · IB 3 |
| fg-20 | Drachenviereck | Zwei Paare gleich langer Nachbarseiten. | Die beiden Winkel abseits der Symmetrieachse sind gleich groß. | Die Diagonalen stehen senkrecht aufeinander; die Symmetrieachse ist eine der Diagonalen. | 1 (bei der Raute 2, beim Quadrat 4): eine Diagonale | nein | Kein Sonderfall von einem anderen besonderen Viereck, nur vom allgemeinen Viereck. Nicht jedes Drachenviereck ist eine Raute. | Gym 5 · RS 5 · IB 1 |
| fg-21 | Allgemeines Viereck | Keine besonderen Seiteneigenschaften. | Die Winkelsumme ist 360°. | Keine besondere Eigenschaft. | keine | nein | Oberbegriff: Jedes Viereck ist ein allgemeines Viereck. Es ist kein Sonderfall von etwas anderem. | Gym 7 · RS 7 · IB 3 |

## Haus der Vierecke (fg-22)

Ein Sonderfall hat alle Eigenschaften des allgemeineren Vierecks und noch mehr. Beispiel: Jedes Quadrat ist ein Rechteck und eine Raute, aber nicht jedes Rechteck ist ein Quadrat.

Trapez heißt hier: mindestens ein Paar paralleler Gegenseiten. Darum ist jedes Parallelogramm auch ein Trapez.

**Vereinbarung (Konvention):** Diese Definition ist eine Vereinbarung. Manche Bücher verlangen genau ein Paar paralleler Seiten; dann ist das Parallelogramm kein Trapez. Frage im Zweifel, welche Definition in deinem Buch steht.

- Quadrat ist Sonderfall von Rechteck.
- Quadrat ist Sonderfall von Raute.
- Rechteck ist Sonderfall von Parallelogramm.
- Rechteck ist Sonderfall von Gleichschenkliges Trapez.
- Raute ist Sonderfall von Parallelogramm.
- Raute ist Sonderfall von Drachenviereck.
- Parallelogramm ist Sonderfall von Trapez.
- Gleichschenkliges Trapez ist Sonderfall von Trapez.
- Drachenviereck ist Sonderfall von Allgemeines Viereck.
- Trapez ist Sonderfall von Allgemeines Viereck.

Schichten von oben nach unten: Quadrat / Rechteck, Raute / Parallelogramm, gleichschenkliges Trapez, Drachenviereck / Trapez / Allgemeines Viereck

## Kongruenzsätze

| Kennung | Satz | Gegeben | Bedingung | Beispiel |
|---|---|---|---|---|
| fg-23 | SSS (Seite – Seite – Seite) | Alle drei Seiten sind gegeben. | Jede Seite ist kürzer als die beiden anderen zusammen (Dreiecksungleichung). | a = 3 cm, b = 4 cm, c = 5 cm; 3 + 4 > 5, 3 + 5 > 4 und 4 + 5 > 3 |
| fg-24 | SWS (Seite – Winkel – Seite) | Zwei Seiten und der Winkel dazwischen sind gegeben. | Der Winkel liegt zwischen den beiden Seiten (nicht an einer anderen Stelle). | b = 5 cm, c = 7 cm und α = 40° zwischen b und c |
| fg-25 | WSW (Winkel – Seite – Winkel) | Eine Seite und die beiden Winkel an ihren Enden sind gegeben. | Die beiden Winkel sind zusammen kleiner als 180°. | c = 6 cm, α = 50° und β = 60°; 50° + 60° < 180° |
| fg-26 | SsW (Seite – Seite – Winkel) | Zwei Seiten und der Winkel sind gegeben, der der längeren der beiden Seiten gegenüberliegt. | Der Winkel liegt der längeren Seite gegenüber. Liegt er der kürzeren gegenüber, können zwei verschiedene Dreiecke entstehen. | b = 5 cm, c = 7 cm und γ = 40° gegenüber von c; 7 cm > 5 cm |

Reicht nicht: WWW: Drei Winkel allein legen das Dreieck nicht fest: Es gibt beliebig große Dreiecke mit denselben Winkeln. Zwei gleichseitige Dreiecke mit den Seiten 3 cm und 6 cm haben dieselben drei Winkel (60°), sind aber nicht kongruent.

## Belege und Regeln

| Kennung | Eintrag | ab | Regel |
|---|---|---|---|
| fg-01 | spitzer Winkel | Gym 5 · RS 5 · IB 1 | G3 |
| fg-02 | rechter Winkel | Gym 5 · RS 5 · IB 1 | G3 |
| fg-03 | stumpfer Winkel | Gym 5 · RS 5 · IB 1 | G3 |
| fg-04 | gestreckter Winkel | Gym 5 · RS 5 · IB 1 | G3 |
| fg-05 | überstumpfer Winkel | Gym 5 · RS 5 · IB 1 | G3 |
| fg-06 | Vollwinkel | Gym 5 · RS 5 · IB 1 | G3 |
| fg-07 | Winkelsumme im Dreieck | Gym 7 · RS 7 · IB 2 | G6 |
| fg-08 | Allgemeines (ungleichseitiges) Dreieck | ohne Beleg | G9 |
| fg-09 | Gleichschenkliges Dreieck | Gym 7 · RS 7 · IB 3 | G9 |
| fg-10 | Gleichseitiges Dreieck | Gym 7 · RS 7 · IB 2 | G9 |
| fg-11 | Spitzwinkliges Dreieck | ohne Beleg | G3 |
| fg-12 | Rechtwinkliges Dreieck | Gym 9 · RS 9 · IB 3 | G24 |
| fg-13 | Stumpfwinkliges Dreieck | Gym 6 · RS 6 | G3 |
| fg-14 | Quadrat | Gym 5 · RS 5 · IB 1 | G7 |
| fg-15 | Rechteck | Gym 5 · RS 5 · IB 1 | G7 |
| fg-16 | Raute | Gym 5 · RS 5 · IB 1 | G7 |
| fg-17 | Parallelogramm | Gym 5 · RS 5 · IB 1 | G7 |
| fg-18 | Trapez | Gym 5 · RS 5 · IB 1 | G7 |
| fg-19 | Gleichschenkliges Trapez | Gym 7 · RS 6 · IB 3 | – |
| fg-20 | Drachenviereck | Gym 5 · RS 5 · IB 1 | G7 |
| fg-21 | Allgemeines Viereck | Gym 7 · RS 7 · IB 3 | – |
| fg-22 | Haus der Vierecke: Wer ist Sonderfall von wem? | Gym 7 · RS 6 · IB 3 | G7, G16 |
| fg-23 | Kongruenzsatz SSS | Gym 7 · RS 7 · IB 3 | G10 |
| fg-24 | Kongruenzsatz SWS | Gym 7 · RS 7 · IB 3 | G10 |
| fg-25 | Kongruenzsatz WSW | Gym 7 · RS 7 · IB 3 | G10 |
| fg-26 | Kongruenzsatz SsW | Gym 7 · RS 7 · IB 3 | G10 |
| fg-27 | Reicht nicht: WWW | Gym 7 · RS 7 · IB 3 | G10 |

## Vorschlag zur Gliederung der Karte

- **Nebeneinander (Hauptansicht):** links das Haus der Vierecke als Bild (Schichten von unten nach oben: allgemeines Viereck; Trapez; Parallelogramm, gleichschenkliges Trapez, Drachenviereck; Rechteck, Raute; Quadrat) mit Pfeilen „ist Sonderfall von“; rechts die Eigenschaftentabelle des angetippten Vierecks (Seiten, Winkel, Diagonalen, Achsen).
- **Dreiecke:** zwei Reihen nebeneinander: „nach Seiten“ (allgemein, gleichschenklig, gleichseitig) und „nach Winkeln“ (spitzwinklig, rechtwinklig, stumpfwinklig); die Winkelsumme 180° steht als Kopfzeile über beiden.
- **Winkelarten:** Skala von 0° bis 360° mit den sechs Bereichen; die Grenzen (90°, 180°, 360°) als eigene Namen, nicht als Bereich.
- **Zum Aufklappen:** Kongruenzsätze mit Skizze (SSS, SWS, WSW, SsW) samt Bedingung und dem Hinweis, dass WWW nicht reicht; Beispieldaten der Dreiecke; Definition „Trapez = mindestens ein Paar paralleler Seiten“.
- **Suche:** `stichwoerter` (z. B. „Raute“, „gleichschenklig“, „Haus der Vierecke“, „deckungsgleich“).
