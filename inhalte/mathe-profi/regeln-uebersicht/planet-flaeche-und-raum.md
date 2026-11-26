# Gesetzbuch · Planet „Fläche und Raum“ – ausgearbeitet als Muster

Mathe-Profi, 26.11.2026. Erzeugt von `gesetzbuch.py`; 44 Beispiele, alle mit Zahlen nachgerechnet (Lauf „OK“).
So soll jeder Planet aussehen: je Gesetz Merksatz, Warum, Wo es nicht gilt, dasselbe Gesetz in mehreren Klassen, worauf es aufbaut, ein Bild.

## Der Planet in einer Minute

- **19 Gesetze:** zehn für Flächen, neun für Körper.
- **Eine Idee trägt alle:** *Messen heißt auslegen und zählen* – Flächen mit Einheitsquadraten, Körper mit Einheitswürfeln. Jede Formel ist eine Abkürzung für dieses Zählen.
- **Ein Gesetz erzeugt die anderen:** Aus dem Rechteck entstehen durch Zerlegen Parallelogramm, Dreieck, Trapez, Drachen und Kreis. Aus dem Quader entstehen durch Stapeln Prisma und Zylinder, daraus durch „ein Drittel“ Pyramide und Kegel.
- Der Planet begleitet die Kinder von Klasse 5 (Rechteck) bis Klasse 10 (Kugel).

## Aufbau

- **F2 Rechteck** braucht: F1 Fläche messen
- **F3 Fläche ist nicht Umfang** braucht: F2 Rechteck
- **F4 Zerlegen und Ergänzen** braucht: F2 Rechteck
- **F5 Parallelogramm** braucht: F4 Zerlegen und Ergänzen
- **F6 Dreieck** braucht: F5 Parallelogramm
- **F7 Trapez** braucht: F5 Parallelogramm
- **F8 Drachenviereck und Raute** braucht: F6 Dreieck
- **F9 Kreis** braucht: F2 Rechteck, F4 Zerlegen und Ergänzen
- **F10 Kreisausschnitt** braucht: F9 Kreis
- **F11 Volumen messen** braucht: F1 Fläche messen
- **F12 Quader** braucht: F11 Volumen messen, F2 Rechteck
- **F13 Oberfläche** braucht: F2 Rechteck
- **F15 Prisma und Zylinder** braucht: F12 Quader, F6 Dreieck, F9 Kreis
- **F16 Satz von Cavalieri** braucht: F15 Prisma und Zylinder
- **F17 Pyramide und Kegel** braucht: F15 Prisma und Zylinder, F16 Satz von Cavalieri
- **F18 Kugel** braucht: F9 Kreis, F17 Pyramide und Kegel
- **F19 Lage im Raum** braucht: F14 Netz und Schrägbild

Vorschlag für das Bild des Planeten [M]: **zwei Stammbäume nebeneinander** – links wächst aus dem Rechteck jede Flächenformel, rechts aus dem Quader jede Volumenformel; an jedem Ast steht, was getan wurde („abschneiden und ansetzen“, „halbieren“, „stapeln“, „ein Drittel“).

## Die Gesetze

### F1 · Fläche messen

> **Flächeninhalt heißt: Wie viele Einheitsquadrate passen hinein? Umrechnungszahl 100.**

Gymnasium Klasse 5 · Realschule Klasse 5 · IB-Jahr 1

**Warum das gilt:** Eine Fläche misst man, indem man sie mit gleich großen Quadraten auslegt und zählt. Ein Quadratdezimeter ist 10 cm lang und 10 cm breit, also passen 10 mal 10 = 100 Quadratzentimeter hinein. Deshalb ist die Umrechnungszahl bei Flächen 100 und nicht 10.

**Wo es nicht gilt:** Bei Längen ist die Umrechnungszahl 10, bei Flächen 100, bei Volumen 1 000 – wer sie verwechselt, liegt um das Zehn- oder Hundertfache daneben. Von m² zu a und ha ist sie ebenfalls 100.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 5 | 3 m² = 300 dm² |
| 5 | 2,5 dm² = 250 cm² |
| 8 | 5 000 cm² = 0,5 m² |

**Baut auf:** Rechenregel 1 Stellenwert und Prozent
**Bild:** Ein Quadratdezimeter in Originalgröße, in 10 mal 10 Kästchen geteilt; eines davon ist gefärbt: 1 cm².

### F2 · Rechteck

> **Fläche = Länge mal Breite. Umfang = einmal außen herum.**

Gymnasium Klasse 5 · Realschule Klasse 5 · IB-Jahr 1

**Warum das gilt:** In ein Rechteck mit 6 cm Länge und 4 cm Breite passen 4 Reihen mit je 6 Einheitsquadraten. Das sind 6 mal 4. Der Umfang ist der Weg einmal außen herum: zweimal die Länge und zweimal die Breite.

**Wo es nicht gilt:** Beide Seiten müssen in derselben Einheit stehen. Fläche und Umfang sind verschiedene Größen: Die Fläche hat cm², der Umfang cm.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 5 | 6 cm lang, 4 cm breit: Fläche 24 cm², Umfang 20 cm |
| 7 | Seiten x und x + 4: Fläche x · (x + 4) = x² + 4x |
| 8 | Grundfläche eines Quaders oder Prismas |
| 9 | Fläche 60, eine Seite 4 länger als die andere: x² + 4x = 60, also x = 6 |

**Baut auf:** F1 Fläche messen
**Bild:** Rechteck 6 mal 4 mit Kästchengitter; daneben dasselbe Rechteck nur als Rand, mit einem Pfeil, der außen herumläuft.

### F3 · Fläche ist nicht Umfang

> **Gleicher Umfang heißt nicht gleiche Fläche.**

Gymnasium Klasse 5 · Realschule Klasse 5–8 · IB-Jahr 1

**Warum das gilt:** Der Umfang zählt den Rand, die Fläche das Innere. Ein langes, schmales Rechteck hat viel Rand und wenig Inneres. Unter allen Rechtecken mit gleichem Umfang hat das Quadrat die größte Fläche.

**Wo es nicht gilt:** Umgekehrt gilt es genauso: Gleiche Fläche heißt nicht gleicher Umfang.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 5 | 5 · 5 und 8 · 2: beide Umfang 20, Flächen 25 und 16 |
| 8 | Umfang 20: Fläche x · (10 − x) ist am größten bei x = 5 (Realschule) |

**Baut auf:** F2 Rechteck
**Bild:** Zwei Rechtecke aus derselben Schnur gelegt: 5 mal 5 und 8 mal 2. Beide haben den Umfang 20, die Flächen 25 und 16.

### F4 · Zerlegen und Ergänzen

> **Zerschneiden und neu zusammenlegen ändert die Fläche nicht.**

Gymnasium Klasse 5–6 · Realschule Klasse 5–6 · IB-Jahr 1

**Warum das gilt:** Beim Zerschneiden geht nichts verloren und kommt nichts dazu. Deshalb darf man eine unbekannte Figur in bekannte Stücke zerlegen oder zu einer bekannten ergänzen und das Zuviel abziehen. Alle Flächenformeln dieses Planeten entstehen so aus dem Rechteck.

**Wo es nicht gilt:** Der Umfang ändert sich beim Zerlegen sehr wohl.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 5 | L-Form: 6 · 4 minus die Ecke 2 · 2 ergibt 20 |
| 6 | Parallelogramm: Dreieck links abschneiden, rechts ansetzen – es entsteht ein Rechteck |
| 9 | Pythagoras lässt sich durch Zerlegen zweier gleich großer Quadrate begründen |

**Baut auf:** F2 Rechteck
**Bild:** Eine L-Form: einmal in zwei Rechtecke zerschnitten, einmal zum großen Rechteck ergänzt, mit dem fehlenden Eck gestrichelt.

### F5 · Parallelogramm

> **Fläche = Grundseite mal Höhe. Die Höhe steht senkrecht.**

Gymnasium Klasse 6 · Realschule Klasse 6 · IB-Jahr –

**Warum das gilt:** Schneidet man an einer Seite ein Dreieck ab und setzt es an der anderen wieder an, entsteht ein Rechteck mit derselben Grundseite und derselben Höhe.

**Wo es nicht gilt:** Gemeint ist die Höhe senkrecht zur Grundseite, nicht die schräge Seite. Die schräge Seite braucht man nur für den Umfang.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 6 | Grundseite 8 cm, Höhe 5 cm: 40 cm² – egal, wie lang die schräge Seite ist |
| 8 | Fläche 40 und Grundseite 8: Höhe 40 : 8 = 5 |

**Baut auf:** F4 Zerlegen und Ergänzen
**Bild:** Parallelogramm mit gestrichelter Höhe; das abgeschnittene Dreieck wandert mit einem Pfeil auf die andere Seite.

### F6 · Dreieck

> **Fläche = Grundseite mal Höhe, geteilt durch 2.**

Gymnasium Klasse 6–8 · Realschule Klasse 6 · IB-Jahr 4

**Warum das gilt:** Zwei gleiche Dreiecke lassen sich immer zu einem Parallelogramm zusammenlegen. Ein Dreieck ist also ein halbes Parallelogramm mit derselben Grundseite und Höhe.

**Wo es nicht gilt:** Das „geteilt durch 2“ wird am häufigsten vergessen. Bei stumpfen Dreiecken liegt die Höhe außerhalb – die Formel gilt trotzdem.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 6 | Grundseite 14 cm, Höhe 15 cm: 14 · 15 : 2 = 105 cm² |
| 8 | Fläche 36 und Grundseite 9: erst mal 2, dann durch 9, Höhe 8 |
| 9 | Rechtwinklig mit den Katheten 6 und 8: 24 – die Katheten sind Grundseite und Höhe |

**Baut auf:** F5 Parallelogramm
**Bild:** Ein Dreieck und sein gedrehter Zwilling ergeben ein Parallelogramm; eines der beiden ist gefärbt.

### F7 · Trapez

> **Fläche = Mittelwert der beiden parallelen Seiten mal Höhe.**

Gymnasium Klasse 6–8 · Realschule Klasse 6 · IB-Jahr 4

**Warum das gilt:** Zwei gleiche Trapeze ergeben zusammen ein Parallelogramm mit der Grundseite a + c. Ein Trapez ist die Hälfte davon. Anders gesagt: Man rechnet mit einem Rechteck, das so breit ist wie der Mittelwert der beiden parallelen Seiten.

**Wo es nicht gilt:** a und c sind die parallelen Seiten, nicht irgendwelche. Die Klammer um a + c ist nötig.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 6 | a = 7, c = 11, h = 6: (7 + 11) · 6 : 2 = 54 |
| 8 | Fläche 60, a = 9, c = 11: Höhe 2 · 60 : 20 = 6 |

**Baut auf:** F5 Parallelogramm · Rechenregel 4 Reihenfolge beim Rechnen
**Bild:** Trapez und gedrehter Zwilling als Parallelogramm; darunter das gleich große Rechteck mit der mittleren Breite.

### F8 · Drachenviereck und Raute

> **Fläche = Diagonale mal Diagonale, geteilt durch 2.**

Gymnasium Klasse 6 · Realschule Klasse 6 · IB-Jahr –

**Warum das gilt:** Die Diagonalen stehen senkrecht aufeinander. Das umschließende Rechteck hat die Seiten e und f und ist genau doppelt so groß wie das Viereck.

**Wo es nicht gilt:** Gilt nur, wenn die Diagonalen senkrecht aufeinander stehen – also nicht für jedes Viereck.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 6 | Diagonalen 8 cm und 5 cm: 8 · 5 : 2 = 20 cm² |

**Baut auf:** F6 Dreieck
**Bild:** Drachen im Rechteck: Die vier Ecken-Dreiecke außen sind genauso groß wie die vier innen.

### F9 · Kreis

> **Umfang = 2 · π · r. Fläche = π · r². π ist etwas mehr als 3.**

Gymnasium Klasse 8 · Realschule Klasse 9 · IB-Jahr 3

**Warum das gilt:** Bei jedem Kreis ist der Umfang gleich oft so lang wie der Durchmesser: etwa 3,14-mal. Diese Zahl heißt π. Schneidet man den Kreis in viele Tortenstücke und legt sie abwechselnd nebeneinander, entsteht fast ein Rechteck: so hoch wie der Radius, so breit wie der halbe Umfang – also π · r mal r.

**Wo es nicht gilt:** r ist der Radius, nicht der Durchmesser. Doppelter Radius: doppelter Umfang, aber vierfache Fläche. π ist kein Bruch; 3,14 ist gerundet.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 8 | r = 5 cm: Umfang 10 · π ≈ 31,4 cm, Fläche 25 · π ≈ 78,5 cm² |
| 8 | Radius von 3 auf 6: Fläche von 9 · π auf 36 · π – das Vierfache |
| 10 | Grundfläche von Zylinder und Kegel |

**Baut auf:** F2 Rechteck · F4 Zerlegen und Ergänzen · Rechenregel 8 Potenzen
**Bild:** Kreis in zwölf Tortenstücke geschnitten und zum „Rechteck“ umgelegt; an den Seiten stehen r und π · r.

### F10 · Kreisausschnitt

> **Der Anteil am vollen Winkel ist der Anteil an Umfang und Fläche.**

Gymnasium Klasse 8 · Realschule Klasse 9 · IB-Jahr 3

**Warum das gilt:** Ein Viertelkreis hat ein Viertel des Umfangs und ein Viertel der Fläche. Für jeden anderen Winkel gilt dasselbe mit dem Anteil am vollen Winkel von 360°.

**Wo es nicht gilt:** Der Bogen ist nur der gekrümmte Teil; zum Umfang des Ausschnitts kommen zwei Radien dazu.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 8 | 90° bei r = 4: Bogen 2 · π, Fläche 4 · π |

**Baut auf:** F9 Kreis · Rechenregel 11 Verhältnis (Dreisatz)
**Bild:** Pizza mit einem herausgezogenen Stück; am Stück stehen der Winkel 90° und „ein Viertel“.

### F11 · Volumen messen

> **Volumen heißt: Wie viele Einheitswürfel passen hinein? Umrechnungszahl 1 000. 1 Liter = 1 dm³.**

Gymnasium Klasse 6 · Realschule Klasse 6 · IB-Jahr –

**Warum das gilt:** Ein Volumen misst man mit gleich großen Würfeln. In einen Würfel mit 1 dm Kantenlänge passen 10 mal 10 mal 10 = 1 000 Zentimeterwürfel. Ein Liter ist genau so ein Dezimeterwürfel.

**Wo es nicht gilt:** Umrechnungszahl 1 000, nicht 10 und nicht 100. Milliliter und cm³ sind dasselbe.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 6 | 2 dm³ = 2 000 cm³ = 2 Liter |
| 6 | 750 ml = 0,75 l = 750 cm³ |
| 8 | 1 m³ = 1 000 Liter |

**Baut auf:** F1 Fläche messen · Rechenregel 1 Stellenwert und Prozent
**Bild:** Dezimeterwürfel aus 1 000 kleinen Würfeln, eine Schicht (100 Stück) herausgezogen; daneben eine Literflasche.

### F12 · Quader

> **Volumen = Länge mal Breite mal Höhe.**

Gymnasium Klasse 6 · Realschule Klasse 6 · IB-Jahr –

**Warum das gilt:** Auf dem Boden liegen Länge mal Breite Würfel. Davon stapelt man so viele Schichten, wie der Quader hoch ist.

**Wo es nicht gilt:** Alle drei Kanten in derselben Einheit. Für den Würfel wird daraus a · a · a.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 5 | Oberfläche und Kanten eines Quaders 5 · 4 · 3 (das Volumen kommt in Klasse 6) |
| 6 | 5 cm · 4 cm · 3 cm = 60 cm³ |
| 6 | 60 Liter in ein Becken mit 50 cm mal 40 cm Boden: 30 cm hoch |

**Baut auf:** F11 Volumen messen · F2 Rechteck
**Bild:** Quader aus Schichten: unten eine Lage 5 mal 4 Würfel, darüber zwei weitere Lagen leicht angehoben.

### F13 · Oberfläche

> **Die Oberfläche ist die Summe aller Flächen des Netzes. Quader: sechs Rechtecke, je zwei gleich.**

Gymnasium Klasse 5–6 · Realschule Klasse 6 · IB-Jahr 1

**Warum das gilt:** Klappt man einen Körper auf, liegen alle seine Flächen nebeneinander: das Netz. Die Oberfläche ist deren Summe. Beim Quader sind es drei Paare gleicher Rechtecke.

**Wo es nicht gilt:** Oberfläche ist eine Fläche (cm²), Volumen ein Rauminhalt (cm³). Bei offenen Gefäßen fehlt der Deckel.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 5 | Quader 5 · 4 · 3: 2 · (20 + 15 + 12) = 94 cm² |
| 8 | Zylinder: zwei Kreise und ein Rechteck als Mantel |

**Baut auf:** F2 Rechteck · Rechenregel 4 Reihenfolge beim Rechnen
**Bild:** Quader und daneben sein aufgeklapptes Netz, die drei Paare in drei Farben.

### F14 · Netz und Schrägbild

> **Das Netz ist der aufgeklappte Körper. Im Schrägbild werden Kanten nach hinten schräg und verkürzt gezeichnet.**

Gymnasium Klasse 8–10 · Realschule Klasse 5–7 · IB-Jahr 3–4

**Warum das gilt:** Ein Körper hat drei Ausdehnungen, das Papier nur zwei. Das Netz zeigt alle Flächen in wahrer Größe, aber nicht den Zusammenhang. Das Schrägbild zeigt den Zusammenhang, aber verkürzt die Kanten nach hinten. Für das Schrägbild gibt es eine feste Vereinbarung (meist 45° und halbe Länge).

**Wo es nicht gilt:** Im Schrägbild darf man nach hinten laufende Längen und Winkel nicht abmessen.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 5 | Ein Würfelnetz besteht aus 6 Quadraten (Realschule Klasse 5) |
| 8 | Quader: 8 Ecken, 12 Kanten, 6 Flächen – 8 − 12 + 6 = 2 |
| 10 | Im Schrägbild einer Pyramide erscheint die Höhe unverkürzt, die Grundkante nach hinten halb |

**Baut auf:** nichts – Anfang
**Bild:** Würfel dreimal: als Körper, als Netz (Kreuzform) und als Schrägbild mit gestrichelten verdeckten Kanten.

### F15 · Prisma und Zylinder

> **Volumen = Grundfläche mal Höhe. Oberfläche = zwei Grundflächen plus Mantel.**

Gymnasium Klasse 8 · Realschule Klasse 9 · IB-Jahr –

**Warum das gilt:** Wie beim Quader: Auf der Grundfläche liegt eine Schicht, und davon stapelt man so viele, wie der Körper hoch ist. Welche Form die Grundfläche hat, ist dafür gleichgültig. Der Mantel ist abgerollt ein Rechteck: Umfang der Grundfläche mal Höhe.

**Wo es nicht gilt:** Die Höhe steht senkrecht auf der Grundfläche. Die Grundfläche ist die Fläche, die oben und unten gleich ist – sie muss nicht unten liegen.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 6 | Quader ist der einfachste Fall: Grundfläche 20 cm², Höhe 3 cm, 60 cm³ |
| 8 | Dreiecksprisma: Grundfläche 24 cm², Höhe 10 cm, Volumen 240 cm³ |
| 8 | Zylinder r = 3, h = 10: Volumen 90 · π, Mantel 60 · π |

**Baut auf:** F12 Quader · F6 Dreieck · F9 Kreis
**Bild:** Münzstapel als Zylinder und ein Stapel dreieckiger Bierdeckel als Prisma; daneben das abgerollte Etikett einer Dose.

### F16 · Satz von Cavalieri

> **Gleiche Höhe und auf jeder Höhe gleich große Schnittfläche: gleiches Volumen.**

Gymnasium Klasse 8 · Realschule Klasse 9 · IB-Jahr –

**Warum das gilt:** Verschiebt man in einem Münzstapel die Münzen gegeneinander, wird der Stapel schief – aber es bleiben dieselben Münzen. Zwei Körper, die auf jeder Höhe gleich große Schnittflächen haben, haben deshalb dasselbe Volumen.

**Wo es nicht gilt:** Die Schnittflächen müssen auf jeder Höhe gleich groß sein, nicht nur unten und oben. Die Oberfläche ändert sich beim Schiefstellen.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 8 | Ein schiefes Prisma mit Grundfläche 24 cm² und Höhe 10 cm hat ebenfalls 240 cm³ |

**Baut auf:** F15 Prisma und Zylinder
**Bild:** Ein gerader und ein schiefer Münzstapel aus denselben Münzen.

### F17 · Pyramide und Kegel

> **Volumen = ein Drittel von Grundfläche mal Höhe.**

Gymnasium Klasse 10 · Realschule Klasse 9 · IB-Jahr 3

**Warum das gilt:** Ein Würfel lässt sich in drei gleiche Pyramiden zerlegen, deren Spitzen in einer Ecke zusammenlaufen. Jede füllt also ein Drittel. Mit Cavalieri gilt das für jede Pyramide und jeden Kegel: ein Drittel des Prismas oder Zylinders mit gleicher Grundfläche und Höhe.

**Wo es nicht gilt:** Die Höhe geht senkrecht von der Spitze zur Grundfläche – nicht entlang der schrägen Seitenkante oder Mantellinie.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 10 | Pyramide: Grundfläche 36 cm², Höhe 10 cm, Volumen 120 cm³ (Realschule Klasse 9) |
| 10 | Kegel r = 3, h = 4: Volumen 12 · π; Mantellinie 5 (Pythagoras), Mantel 15 · π |

**Baut auf:** F15 Prisma und Zylinder · F16 Satz von Cavalieri · Rechenregel 10 Rechnen mit Brüchen
**Bild:** Ein Kegel wird dreimal mit Wasser gefüllt und in einen Zylinder mit gleicher Grundfläche und Höhe gegossen: genau voll.

### F18 · Kugel

> **Volumen = 4/3 · π · r³. Oberfläche = 4 · π · r².**

Gymnasium Klasse 10 · Realschule Klasse 9 · IB-Jahr 3

**Warum das gilt:** Eine Halbkugel hat dasselbe Volumen wie ein Zylinder gleicher Höhe, aus dem ein Kegel herausgebohrt ist – das zeigt Cavalieri. Daraus folgen zwei Drittel des umschließenden Zylinders für die ganze Kugel. Die Oberfläche ist genau viermal so groß wie der größte Kreis durch die Kugel.

**Wo es nicht gilt:** Hoch 3 beim Volumen, hoch 2 bei der Oberfläche. Doppelter Radius: achtfaches Volumen.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 10 | r = 3: Volumen 36 · π, Oberfläche 36 · π (Realschule Klasse 9) |
| 10 | Radius verdoppelt: Volumen mal 8 |

**Baut auf:** F9 Kreis · F17 Pyramide und Kegel · Rechenregel 8 Potenzen
**Bild:** Kugel in einem genau passenden Zylinder: Sie füllt zwei Drittel davon.

### F19 · Lage im Raum

> **Zwei Geraden im Raum sind parallel, schneiden sich oder laufen windschief aneinander vorbei.**

Gymnasium Klasse 10 · Realschule Klasse 7 · IB-Jahr 4

**Warum das gilt:** In der Ebene schneiden sich zwei Geraden oder sie sind parallel. Im Raum gibt es eine dritte Möglichkeit: Sie laufen aneinander vorbei, ohne parallel zu sein. Am Quader sieht man alle drei Fälle an den Kanten.

**Wo es nicht gilt:** Windschief gibt es nur im Raum. Im Schrägbild können sich windschiefe Geraden scheinbar schneiden.

| Klasse | Dasselbe Gesetz in diesem Jahr |
|---|---|
| 10 | Am Quader: Eine Bodenkante und die Deckenkante quer darüber sind windschief (Realschule Klasse 7) |

**Baut auf:** F14 Netz und Schrägbild
**Bild:** Quader mit drei Kantenpaaren in drei Farben: parallel, schneidend, windschief.

## Nicht geprüft

- Klassen aus `inhalte/themenliste.json`, nicht aus dem Lehrplan an der Quelle. Die Zuordnung von Netzen und Schrägbildern (Realschule 5 und 7, Gymnasium 8 und 10) gehört zu den Zuordnungen, an denen ich zweifle.
- Die Begründungen sind Schul-Begründungen, keine Beweise (Kreisfläche über Tortenstücke, Pyramide über den Würfel, Kugel über Cavalieri).
- Bilder nur beschrieben. Merksätze nicht mit einem Kind erprobt.
