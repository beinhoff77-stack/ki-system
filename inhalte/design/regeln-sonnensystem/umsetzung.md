> **ABGELEHNT am 26.11.2026.** Der Nutzer hat diese Vorgabe abgelehnt. Sie gilt nicht mehr und wird nicht gebaut. Nachfolger: `inhalte/design/gesetzbuch/umsetzung.md` (Vorgabe GB). Die Dateien bleiben nur zum Nachlesen.

# Vorgabe RS-H: Regeln am Himmel – Übersicht „Sonnensystem“ und Regel-Karte

Designer, 26.11.2026. Stand `lernen-app` 9c2d316 (App 0.93.4). Kein App-Code, keine Datenbank. Fachlicher Inhalt: `inhalte/mathe-profi/denkpapier-grundregeln.md` auf `origin/mathe-profi`, Abschnitte 1, 2 und 5.
**[G]** gesichert (im Entwurf gebaut und gemessen) · **[A]** Annahme · **[M]** Meinung.

Kürzel **RS-H**, weil „RS“ im Repo schon vergeben ist (Vorschau-Bilder `rs-*`).

## 0 Kurzfassung

- **Empfehlung: Fassung A „Sonnensystem“ als Seite.** Die ruhige Liste aus Fassung B steckt in A hinter der Sonne („Alle 15 in einer Liste“). So gibt es eine Seite, nicht zwei.
- **Ein Planet je Gruppe, ein Mond je Regel.** Voller Mond = sitzt, offener Ring = in Arbeit, gepunkteter Ring = kommt später. Keine Zahlen, keine Balken.
- **Die Erde ist ein Planet im Bild.** Antippen fliegt zurück zur Reisekarte. Die Sonne hat die Farbe des Hauptknopfs (#FFD23F).
- **Regel-Karte:** Satz, Bild, drei Zeilen „Zahlen / mit x / mit Brüchen“ mit gleichem Aufbau, Grenze, Probe zum Antippen, Orte, ein Hauptknopf.
- **Entwürfe zum Anklicken:** `entwurf/uebersicht-a.html`, `uebersicht-b.html`, `regel-karte.html`, `wege.html` (je eine Datei, Schriften eingebettet). Unten links „Entwurf ⚙“: hell / dunkel, zwei erfundene Stände, weniger Bewegung, Laden und Fehler. Bilder: `bilder/`. Quellen der Entwürfe: `entwurf/teile/`, zusammengesetzt mit `entwurf/bauen.py`.

## 1 Welche Fassung und warum

| | A „Sonnensystem“ | B „Planetenreihe“ |
|---|---|---|
| Bild | Sonne am Rand, sechs Bahnen als Bögen, Planeten mit Monden, Gürtel außen | Sonne und Planeten an einer Linie, darunter die Regel-Namen |
| Stärke | Man sieht auf einen Blick: wenige Körper, eine Sonne. Das ist die Seite, die der Nutzer „toll“ nennt | Alle 15 Namen ohne Antippen lesbar |
| Schwäche | Regel-Namen erst nach einem Antippen | Wirkt wie eine Liste mit Symbolen |
| Handy 360 × 640 | scrollt 140 px (Gürtel und Legende liegen darunter) | Sonne und fünf Planeten ohne Scrollen, Gürtel darunter |
| Handy 400 × 860 | alles ohne Scrollen | alles ohne Scrollen |
| Bewegung | sparsam (siehe 9) | keine |

**Empfehlung A [M].** Gründe:
1. Zur Regel-Karte führen zwei der drei Wege direkt (nach einem Fehler, beim neuen Thema). Die Übersicht hat deshalb vor allem eine Aufgabe: das Gefühl „es sind 15, nicht 300“. Das leistet das Bild, nicht die Liste.
2. Was B besser kann, bekommt A dazu: Die Sonne öffnet die Liste aller 15 Regeln mit Namen und Satz.
3. A passt an die Reisekarte: Karte auf der Erde, Sternkarte am Himmel. Hell sieht A aus wie eine gedruckte Sternkarte, dunkel wie der Nachthimmel.

Wählt der Nutzer B, gelten die Abschnitte 4 bis 12 unverändert; nur Abschnitt 3 wird durch 3.6 ersetzt.

## 2 Vorschläge zu den drei offenen Entscheidungen

| Frage | Vorschlag | Begründung |
|---|---|---|
| Schnitt der Planeten | **Fünf Regel-Planeten wie vorgeschlagen, dazu die Erde. Die Werkzeuge werden kein Planet, sondern der „Werkzeug-Gürtel“** (Ring aus kleinen Brocken ganz außen). | Arbeitsweisen haben kein Richtig oder Falsch und keinen Stand. Als Planet mit Monden sähen sie aus wie Regeln. „Werkzeuggürtel“ ist dazu ein Wort, das die Kinder kennen. |
| Etwas zu tun in der Sonne | **Ja, aber klein:** Die Sonne öffnet die Liste aller 15. Darunter steht ein Knopf „Gemischte Fünf“. | Die Sonne ist der Ort, an dem alle Regeln zusammenkommen. Der Hauptknopf der App bleibt auf der Reisekarte; die Gemischte Fünf ist freiwillig. Ob es sie zusätzlich automatisch am Anfang einer Sitzung gibt, entscheidet der Mathe-Profi. |
| Stand je Regel für die Kinder | **Ja, in zwei Zuständen: „sitzt“ und „in Arbeit“.** Dazu neutral „kommt später“ für Regeln, die das Kind noch nicht hatte. Der Erwachsene sieht mehr (nicht Teil dieser Vorgabe). | Ohne Stand ist die Seite ein Plakat und kein Grund wiederzukommen. Zwei Zustände erlaubt der Mathe-Profi. Fällt eine Regel zurück, wird der Mond still wieder zum Ring: kein „wackelt“, keine Meldung, keine Farbe Rot. |

**Frage an den Mathe-Profi [M]:** „Potenz“ steht im Planeten „Bruch“. Im Bild passt sie schlecht dorthin. Möglich wäre „Potenz“ zu „Verhältnis“ (dann: Stellenwert, Potenz, Verhältnis – alles „wie etwas wächst“). Die Entwürfe zeigen den Schnitt des Projektleiters; der Wechsel wäre eine Zeile in den Daten.

**Dritter Zustand:** „kommt später“ ist kein Leistungs-Zustand, aber ein drittes Zeichen. Wenn der Mathe-Profi das nicht will, werden diese Monde wie „in Arbeit“ gezeichnet und die Legende hat zwei Einträge.

## 3 Übersicht A – Aufbau und Maße

Bilder: `a-360-hell`, `a-400-dunkel`, `a-400-hell`, `a-820-dunkel`, `a-1280-dunkel`, `a-1280-hell`, `a-400-ohne-stand`.

### 3.1 Aufbau

Von hinten nach vorn: Himmel (Verlauf) · Sterne · sechs Bahnen · Gürtel · Schein der Sonne · Sonne · Titel · Planeten mit Monden und Schild · Legende · Zurück-Knopf.

- **Sonne:** Kreis, zum größten Teil außerhalb des Bildschirms. Darin „15“ (Space Grotesk 700) und darunter „REGELN“ (JetBrains Mono 700, Versalien, Laufweite 1,6 px).
- **Titel:** hoch „Mehr sind es nicht.“ unter der Sonne, darunter „Tippe auf einen Planeten.“ Quer „15 Regeln. Mehr sind es nicht.“ oben links.
- **Planeten in dieser Reihenfolge von der Sonne:** Vorzeichen · Klammer · Erde · Waage · Bruch · Verhältnis. Jeder hat ein Zeichen auf der Scheibe und eine eigene Farbe (5.2). Die helle Seite zeigt immer zur Sonne.
- **Monde:** einer je Regel, gleichmäßig auf einem Kreis um den Planeten (Abstand Planetenrand bis Mondmitte 12 px).
- **Schild:** Name (700) und darunter „2 Regeln“ / „3 Regeln“ / „4 Regeln“. Bei der Erde „Deine Reise ›“.
- **Gürtel:** drei gepunktete Kreise ganz außen, darauf eine Kapsel „Werkzeug-Gürtel“ / „5 Arbeitsweisen“.
- **Zurück:** 44 × 44 px oben links, Vorleser-Text „Zur Reise“.

### 3.2 Geometrie

Alle Bahnen sind Kreise um den Mittelpunkt der Sonne. **Hoch** (Breite unter 900 px): Sonne oben in der Mitte. **Quer** (ab 900 px): Sonne links in der Mitte, dasselbe Bild um 90° gedreht.

| Größe | Hoch | Quer |
|---|---|---|
| Einheit u | Breite / 360, höchstens 1,57 | Breite / 1280, zwischen 0,72 und 1,25 |
| Radius Sonne | 118 u | 150 u |
| Mitte Sonne | x = Breite / 2, y = −0,42 · Radius | x = −0,38 · Radius, y = Höhe / 2 |
| Erste Bahn | Radius Sonne + 128 u | Radius Sonne + 150 u |
| Abstand der Bahnen | 84 u | 150 u |
| Gürtel | letzte Bahn + 0,92 · Abstand | letzte Bahn + 0,93 · Abstand |
| Höhe der Szene | Mitte y + Gürtel + 86 px | Fensterhöhe, mindestens 560 px |
| Versatz der Planeten | seitlich: −0,72 · +0,74 · −0,50 · +0,78 · −0,70 · +0,62 mal hw; hw = kleinerer Wert aus (Breite / 2 − 62 u) und (0,55 · Bahnradius) | senkrecht: −0,55 · +0,60 · −0,30 · +0,70 · −0,62 · +0,50 mal hh; hh = kleinerer Wert aus (Höhe / 2 − 120) und (0,5 · Bahnradius) |
| Radius der Planeten | 24 · 31 · 22 · 31 · 28 · 24 px mal u (höchstens 1,35) | dieselben mal 1,2 (bei u unter 0,9: mal 1,08) |
| Schild | neben dem Planeten zur Bildmitte hin, 26 px Abstand zum Planetenrand | mittig unter dem Planeten, 38 px unter dem Rand |

Der Radius folgt der Zahl der Regeln: 2 Regeln 24 px, 3 Regeln 28 px, 4 Regeln 31 px, Erde 22 px.

**Ergebnis je Breite [G]** (x / y / Radius der sechs Planeten, in px):

| Fenster | Sonne R, Mitte | Bahnen | Planeten | Höhe |
|---|---|---|---|---|
| 360 × 640 | 118, 180 / −50 | 246 · 330 · 414 · 498 · 582 · 666, Gürtel 743 | 95/181/24 · 267/269/31 · 121/360/22 · 272/440/31 · 97/527/28 · 253/612/24 | 780 (scrollt 140) |
| 400 × 860 | 131, 200 / −55 | 273 · 367 · 460 · 553 · 647 · 740, Gürtel 826 | 106/201/27 · 297/299/34 · 134/400/24 · 302/489/34 · 108/585/31 · 281/680/27 | 857 |
| 820 × 1180 | 185, 410 / −78 | 386 · 518 · 650 · 782 · 914 · 1046, Gürtel 1167 | 257/277/32 · 621/395/42 · 254/553/30 · 654/665/42 · 191/809/38 · 604/950/32 | 1175 |
| 1280 × 800 | 150, −57 / 400 | 300 · 450 · 600 · 750 · 900 · 1050, Gürtel 1190 | 231/318/29 · 372/535/37 · 537/316/26 · 667/596/37 · 826/226/34 · 984/540/29 | 800 |

### 3.3 Schrift und Linien

| Teil | Wert |
|---|---|
| Name am Planeten | 18 px / 700; ab 600 px Breite 21 px |
| Zeile darunter, Hinweis unter dem Titel | 16 px / 500, Farbe „leise“; ab 600 px 17 px |
| Titel | 22 px / 700; ab 600 px 26 px |
| „15“ in der Sonne | 32 px mal u (höchstens 1,3) |
| „REGELN“ in der Sonne | 12,5 px mal u (höchstens 1,2), Mono |
| Rand um Schrift am Himmel | 6 px in Himmelsfarbe hinter der Schrift, damit Bahnen sie nicht durchkreuzen |
| Bahnen | 1,25 px |
| Gürtel | drei gepunktete Kreise (Radius −5 / +1 / +6 px): Punkte 3,5 / 5 / 2,5 px, Abstand 17 / 53 / 29 px, Deckkraft 55 % |
| Kapsel am Gürtel | 200 × 58 px, Radius 29 px; Name 18 px / 700, darunter 16 px |
| Sterne | 1 je 5200 px² (dunkel) bzw. 9000 px² (hell), Radius 0,5–1,6 px, Deckkraft 25–85 % |
| Mond „sitzt“ | Kreis Radius 5,5 px, gefüllt in Textfarbe |
| Mond „in Arbeit“ | Ring Radius 4,6 px, Strich 2,3 px in Textfarbe, innen Himmelsfarbe |
| Mond „kommt später“ | Ring Radius 4,6 px, Strich 1,7 px gepunktet (2 / 2,6) in „leise“ |
| Mond ohne Stand | Punkt Radius 3,6 px in „leise“ |
| Legende | unten, 16 px: „sitzt“ · „in Arbeit“ · „kommt später“, je mit seinem Zeichen. Hoch mittig, quer unten links. Ohne Stand entfällt sie |

### 3.4 Die Planeten

| Planet | Zeichen | Besonderes | Satz im Blatt | Regeln |
|---|---|---|---|---|
| Vorzeichen | ± | – | Plus und Minus: wohin es geht und was beim Malnehmen passiert. | 1, 2 |
| Klammer | ( ) | – | Was zuerst gerechnet wird und was mit Klammern passiert. | 3, 4, 5, 6 |
| Erde | – | grüne Flecken, ein kleines Flugzeug kreist | – | – |
| Waage | = | waagrechter Ring (Breite 1,5 R, Höhe 0,3 R) | Gleichungen: Auf beiden Seiten steht gleich viel. | 7, 8, 9, 15 |
| Bruch | Bruchstrich mit Punkt darüber und darunter | – | Brüche und Hochzahlen. | 10, 11, 12 |
| Verhältnis | : | – | Stellen, Prozent und der Wert je Einheit. | 13, 14 |

Zeichen: JetBrains Mono 800, Größe 0,95 R (Klammer 0,68 R), Farbe #11161D mit 82 % Deckkraft. Schattenseite: zweiter Kreis gleicher Größe, um 0,36 R zur Sonne verschoben, in der hellen Farbe, auf die Scheibe beschnitten.

### 3.5 Antippen

| Ziel | Fläche | Was passiert |
|---|---|---|
| Planet | Kreis mit Radius R + 20 px, mindestens 34 px; dazu das Schild | Blatt „Planet“ (4.1) |
| Erde | wie Planet | zurück zur Reisekarte (8.1) |
| Sonne | die ganze sichtbare Scheibe | Blatt „Sonne“ (4.2) |
| Gürtel | Kapsel und Brocken | Blatt „Werkzeug-Gürtel“ (4.3) |
| Zurück | 44 × 44 px | zurück zur Reisekarte |

Alle Ziele sind mit der Tastatur erreichbar (Reihenfolge: Zurück, Sonne, Planeten von innen nach außen, Gürtel) und haben einen Vorleser-Text, z. B. „Planet Klammer, 4 Regeln: 2 sitzen, 2 in Arbeit, 0 kommen später.“ Fokus: gestrichelter Ring 3 px in Textfarbe um die Tippfläche.

### 3.6 Übersicht B (nur falls der Nutzer B wählt)

Bilder: `b-360-dunkel`, `b-400-hell`, `b-820-hell`, `b-1280-dunkel`.

- **Bis 899 px:** eine Spalte, höchstens 640 px breit (ab 600 px: 700 px). Kopfzeile 56 px mit Titel „Regeln“. Senkrechte Linie 2 px bei x = 43 px (ab 600 px: 59 px). Zeilen: Sonne (Scheibe Radius 26 px, „15 Regeln. Mehr sind es nicht.“ 19 px / 700), Planeten (Scheibe Radius 20 px, Name 18 px / 700, darunter die Regel-Namen 16 px mit Mond-Zeichen 14 px davor), Erde (Radius 15 px, „Deine Reise“), Gürtel (Namen der fünf Arbeitsweisen), Legende. Zeile mindestens 64 px hoch, ganze Zeile ist ein Knopf: Planet → Blatt „Planet“.
- **Ab 600 px:** Scheiben Radius 26 px, Name 23 px, Regel-Namen 19 px, Zeile mindestens 92 px.
- **Ab 900 px:** sieben Spalten nebeneinander (Sonne 190 px, sechs gleich breite), waagrechte Linie durch die Scheiben. Unter jedem Planeten seine Regeln als Knöpfe (mindestens 48 px hoch, 16 px / 600): direkt zur Regel-Karte.

## 4 Die Blätter

Ein Blatt ist die Fläche, die sich über die Seite legt.

| Breite | Lage | Maß |
|---|---|---|
| unter 820 px | von unten | volle Breite, höchstens 92 % der Fensterhöhe, Ecken oben 24 px. Die Regel-Karte füllt das ganze Fenster |
| ab 820 px | rechts | 460 px breit (ab 1200 px: 520 px), 16 px Abstand zu den Rändern, Ecken 24 px |

- Kopf: Über-Zeile (Mono 13 px, Versalien), Titel 22 px / 700, rechts „Schließen“ 44 × 44 px. Liegt ein Blatt auf einem anderen (Regel aus Planet), steht links zusätzlich „Zurück“ 44 × 44 px.
- Dahinter ein Schleier (dunkel 62 %, hell 38 %). Antippen des Schleiers und die Taste Esc schließen.
- Beim Schließen geht der Fokus zurück auf das Ziel, das geöffnet hat.

### 4.1 Blatt „Planet“ (Bild `blatt-planet-400`)

Über-Zeile „PLANET · 4 REGELN“, Titel = Name, darunter der Satz aus 3.4. Dann je Regel eine Zeile (mindestens 64 px, Rand 1,5 px, Radius 14 px): Mond-Zeichen 14 px · Name 18 px / 700 · Satz 16 px in „leise“, höchstens zwei Zeilen · „›“. Antippen: Regel-Karte. Unten die Legende.

### 4.2 Blatt „Sonne“ (Bild `blatt-sonne-400`)

Über-Zeile „SONNE“, Titel „15 Regeln. Mehr sind es nicht.“, darunter: „Sie kommen in jedem Thema wieder, nur in neuem Gewand: erst mit Zahlen, später mit x.“ Dann alle 15 Regeln wie in 4.1, mit laufender Nummer davor und dem Planeten-Namen als Zwischenüberschrift. Fuß: Hauptknopf „Gemischte Fünf ›“, darunter 16 px: „Fünf Aufgaben quer durch deine Regeln. Welche Regel dran ist, steht nicht dabei.“ Ohne die Entscheidung für die Gemischte Fünf entfällt der Fuß.

### 4.3 Blatt „Werkzeug-Gürtel“ (Bild `blatt-guertel-400`)

Über-Zeile „GÜRTEL · 5 ARBEITSWEISEN“, Titel „Werkzeug-Gürtel“, darunter: „Keine Regeln, sondern Arbeitsweisen. Hier gibt es kein Richtig oder Falsch – sie helfen dir bei jeder Aufgabe.“ Fünf Zeilen ohne Mond und ohne Pfeil, nicht antippbar:

| Name | Satz (Entwurf des Designers, Mathe-Profi prüft) |
|---|---|
| Skizze | Erst zeichnen, dann rechnen. |
| Überschlag | Vorher grob schätzen, was herauskommen muss. |
| Einheiten prüfen | Passt die Einheit zum Ergebnis? |
| Zerlegen und Ergänzen | Schwieriges in einfache Teile schneiden oder zu etwas Einfachem auffüllen. |
| Darstellung wechseln | Tabelle, Bild, Term: dieselbe Sache anders zeigen. |

## 5 Farben

### 5.1 Grundfarben (aus der App, `style.css` Zeile 3641 und 3644) und neue Himmelsfarben

| Zweck | Abflug dunkel | Abflug hell |
|---|---|---|
| Grund | #0B0F14 | #F3F1EA |
| Fläche (Blatt, Karte) | #151B24 | #FFFFFF |
| Fläche 2 (Bild-Kasten, Probe) | #1D2530 | #F3F1EA |
| Text | #F2F4F7 | #11161D |
| leise | #A9B3C1 | #4A5563 |
| Akzent / Hauptknopf | #FFD23F, Kante #C79E1C, Schrift #11161D | gleich |
| Linie | #2E3947 | #C9C4B6 |
| gut | #45E0A0 | #0B7A4B |
| Kurs | #FFAD7A auf #33201A | #A8410F auf #FFE9DC |
| **neu:** Himmel oben → unten | #060911 → #0B0F14 | #ECE8DC → #F3F1EA |
| **neu:** Bahn | #334154 | #BDB7A6 |
| **neu:** Stern | #F2F4F7 | #A39C88 |
| **neu:** Sonne, Rand | #FFD23F, #FFE58A 2 px | #FFD23F, #C79E1C 2 px |
| **neu:** Schein der Sonne | Verlauf #FFD23F 50 % → 0 %, Radius 1,75 · Sonnenradius | gleich |
| **neu:** Rand der Planeten | Weiß 16 %, 1,25 px | #11161D 50 %, 1,25 px |
| **neu:** Grenze (Kasten) | Grund #2A1A1C, Rand #FF8A8A gestrichelt 1,5 px, Über-Zeile #FFC9C9 | Grund #FFF0EE, Rand #B3261E, Über-Zeile #7A1712 |
| Marke in Rechnungen | #FFD23F, Schrift #11161D, Radius 6 px | gleich |

### 5.2 Planeten (in beiden Gestaltungen gleich)

| Planet | helle Seite | Schattenseite |
|---|---|---|
| Vorzeichen | #FF8A66 | #B4472B |
| Klammer | #A99BFF | #5B4CC4 |
| Erde | #5AAEFF, Flecken #45E0A0 | #1F5FA8 |
| Waage | #3AD6C5 | #14877C |
| Bruch | #FF9BD0 | #B8487F |
| Verhältnis | #B4E86A | #5F9A22 |

Die Farbe trägt nie allein: Jeder Planet hat sein Zeichen und seinen Namen, jeder Zustand seine Form.

## 6 Regel-Karte

Entwurf: `entwurf/regel-karte.html`. Bilder: `karte-verteilen-400-ganz`, `karte-minusklammer-400-ganz`, `karte-verteilen-360`, `karte-verteilen-1280`, `karte-minusklammer-820`.

### 6.1 Aufbau von oben nach unten

| Nr. | Teil | Maß und Verhalten |
|---|---|---|
| 1 | Kopf | Über-Zeile „KLAMMER · REGEL 4 VON 15“, Titel = Name der Regel, „Schließen“ |
| 2 | Ruf-Zeile, nur auf Weg b und c | Kasten in Kurs-Farbe, Radius 18 px, Zeichen 26 px, Text 17 px / 600 (Texte in 8) |
| 3 | Zustand | Mond-Zeichen und Wort, 16 px. Ohne Stand entfällt die Zeile |
| 4 | Der Satz | 22 px / 700, Zeilen ausgeglichen umbrochen. Zweiter Satz 17 px in „leise“ |
| 5 | Das Bild | Kasten Fläche 2, Rand 1,5 px, Radius 18 px. Zeichnung 320 Einheiten breit, füllt die Breite. Darunter ein Satz, 16 px, mittig |
| 6 | „Dieselbe Regel, drei Gewänder“ | drei Zeilen untereinander: Zahlen · mit x · mit Brüchen. Je Zeile Über-Zeile und Rechnung (Mono 17 px / 600; unter 380 px Breite 15,5 px), mindestens 64 px hoch. **Gleicher Aufbau in allen drei Zeilen, nichts ausgerechnet.** Was die Regel tut, ist markiert |
| 7 | „Die Grenze“ | Kasten wie in 5.1. Fett der Satz der Grenze, dahinter ein Satz Erklärung, darunter ein Zahlen-Gegenbeispiel mit ≠ |
| 8 | „Die Probe“ | Satz, dann „x =“ mit drei Knöpfen 2 · 3 · 4 (je 48 × 48 px, 3 ist vorgewählt). Darunter beide Seiten untereinander, je mit eingesetzter Rechnung und Ergebnis (Mono 22 px). Darunter Haken und „Beide Seiten geben 15.“ |
| 9 | „Diese Regel brauchst du in …“ | Liste im Aussehen der Abflugtafel (Grund #05080C dunkel, #11161D hell; Mono 16 px): Ort gelb in Versalien · Name des Flugs · Klasse. Höchstens vier Zeilen. Nicht antippbar |
| 10 | Fuß, bleibt stehen | ein Hauptknopf (56 px hoch), darunter eine Zeile 16 px (Texte in 8) |

Abstand zwischen den Teilen 20 px, Rand links und rechts 16 px.

### 6.2 Karte „Verteilen“ (Regel 4) – Texte wörtlich

- **Satz:** Der Faktor trifft jeden in der Klammer. · **Zweiter Satz:** Rückwärts: Gemeinsames herausziehen.
- **Bild: Rechteck.** Links die Höhe als gelbe Marke, oben die Breiten, in den Teilen die Flächen. Antippen einer Gewand-Zeile zeigt diese Zeile im Bild; die gewählte Zeile hat links einen gelben Streifen 4 px und trägt „im Bild“, die anderen „im Bild zeigen“.

| Zeile | Rechnung (gelb markiert: der Faktor) | Bild | Satz unter dem Bild |
|---|---|---|---|
| Zahlen | **6** · (20 − 2) = **6** · 20 − **6** · 2 | Breite 20 mit Maßlinie darüber; rechter Streifen „6 · 2“ schraffiert und gestrichelt; linker Teil „6 · 18“; darunter „18“ und „2 weg“ | Das ganze Rechteck ist 6 · 20. Der Streifen 6 · 2 kommt weg, übrig bleibt 6 · 18. |
| mit x | **3** · (x + 2) = **3** · x + **3** · 2 | zwei Teile mit den Breiten „x“ und „2“, darin „3 · x“ und „3 · 2“; darunter „zusammen: 3 · x + 3 · 2“ | Eine Höhe, zwei Breiten: Die Höhe trifft beide Teile. |
| mit Brüchen | **½** · (4 + ⅔) = **½** · 4 + **½** · ⅔ | wie „mit x“ mit „4“ und „⅔“ | wie „mit x“ |

- **Grenze:** **Nicht beim Quadrat.** Das Quadrat trifft nicht jeden einzeln. Mit Zahlen siehst du es sofort: · (3 + 4)² ≠ 3² + 4² · 49 ≠ 25
- **Probe:** Stimmt die Umformung? Setz für x eine Zahl ein – 2 oder 3, nie 0 oder 1. · Seiten: „3 · (x + 2)“ und „3x + 6“. Ergebnisse: x = 2 → 12 / 12 · x = 3 → 15 / 15 · x = 4 → 18 / 18.

### 6.3 Karte „Minusklammer“ (Regel 5) – Texte wörtlich

- **Satz:** Minus vor der Klammer dreht jedes Zeichen darin. · **Zweiter Satz:** Plus davor dreht nichts.
- **Bild: Zahlenstrahl** von 9 bis 21, beschriftet 12, 15, 20. Oben ein Pfeil von 20 nach 12 „− 8“ (Kurs-Farbe), darunter ein Pfeil von 12 nach 15 „+ 3“ (Farbe „gut“). Unter dem Strahl ein Pfeil von 20 nach 15 „− (8 − 3)“ in „leise“. Bei 15 ein gelber Punkt mit Rand. Das Bild bleibt für alle drei Zeilen gleich.
- **Satz unter dem Bild:** Erst 8 zurück – das war zu viel. Also 3 wieder vor.
- **Unter den drei Zeilen:** Das Bild zeigt es mit Zahlen. Mit x und mit Brüchen läuft es genauso.

| Zeile | Rechnung (gelb markiert: das Minus vor der Klammer; unterstrichen 3 px in Kurs-Farbe: die gedrehten Zeichen) |
|---|---|
| Zahlen | 20 **−** (8 − 3) = 20 <u>− 8 + 3</u> |
| mit x | 5x **−** (3x − 2) = 5x <u>− 3x + 2</u> |
| mit Brüchen | 1 **−** (½ − ¼) = 1 <u>− ½ + ¼</u> |

- **Grenze:** **Plus davor dreht nichts.** Nur das Minus dreht. Und es dreht jedes Zeichen, nicht nur das erste: · 20 − (8 − 3) ≠ 20 − 8 − 3 · 15 ≠ 9
- **Probe:** gleicher Satz wie bei Regel 4. Seiten: „5x − (3x − 2)“ und „2x + 2“. Ergebnisse: x = 2 → 6 / 6 · x = 3 → 8 / 8 · x = 4 → 10 / 10.

Brüche stehen in den Rechnungen als echter Bruch (Zähler über Nenner mit Strich 2 px), nicht als Schrägstrich.

**Abweichung vom Denkpapier [G]:** Die Zahlen sind dieselben, aber die Zeilen sind so umgestellt, dass alle drei denselben Aufbau haben (z. B. „6 · (20 − 2)“ statt „6 · 18“ links). Das folgt der Idee „Zwillingszeilen“ aus Abschnitt 3 des Denkpapiers. Alle Ergebnisse sind nachgerechnet. Der Mathe-Profi prüft die Fassung.

### 6.4 Bildmotiv je Regel

| Nr. | Regel | Bild |
|---|---|---|
| 1 | Richtung | Zahlenstrahl mit zwei Pfeilen: Plus nach rechts, Minus nach links; bei einer negativen Zahl klappt der Pfeil um |
| 2 | Zeichen-Paar | Vier-Felder-Tafel der Zeichen: gleiche Zeichen helles Feld mit Plus, verschiedene dunkles Feld mit Minus |
| 3 | Rangfolge | Treppe mit vier Stufen: Klammer, Potenz, Punkt, Strich; die unterste Stufe trägt das Namensschild des Terms |
| 4 | Verteilen | Rechteck mit einer Höhe und zwei Breiten |
| 5 | Minusklammer | Zahlenstrahl: zu weit zurück, ein Stück wieder vor |
| 6 | Tauschen und Bündeln | Zwei Kisten: gleiche Sorte in dieselbe Kiste (x zu x, Zahl zu Zahl) |
| 7 | Waage | Balkenwaage im Gleichgewicht; von beiden Schalen wird dasselbe genommen |
| 8 | Umkehren | Hin- und Rückpfeil zwischen zwei Zahlen: hin „· 4“, zurück „: 4“ |
| 9 | Einsetzen und Probe | Eine Zahl rutscht in das Fach „x“; zwei Wege enden auf derselben Anzeige |
| 10 | Wert bleibt | Ein Bruchstreifen, zweimal gezeichnet: grob und fein geschnitten, gleich lang gefärbt |
| 11 | Bruchrechnen | Zwei Streifen mit verschiedener Teilung, darunter beide mit gemeinsamer Teilung |
| 12 | Potenz | Verdoppelungs-Baum: aus 1 werden 2, 4, 8; die Hochzahl zählt die Stufen |
| 13 | Stellenwert | Stellentafel, in der jede Ziffer beim Malnehmen mit 10 eine Spalte wandert |
| 14 | Verhältnis | Doppelter Zahlenstrahl (oben kg, unten €), die Marken stehen übereinander |
| 15 | Nullprodukt | Zwei Kästen mit Mal-Punkt dazwischen; einer zeigt 0, das Ergebnis-Feld zeigt 0 |

Alle Bilder: Strichzeichnung 2 px in Textfarbe auf Fläche 2, eine gelbe Marke für das, was die Regel tut, Beschriftung in Mono. Kein Foto, keine Figur.

## 7 Zustände der Seite

| Zustand | Übersicht | Regel-Karte |
|---|---|---|
| Lädt (Bild `a-400-laedt`) | Himmel, Sonne, Bahnen und Gürtel stehen sofort. Statt der Planeten gestrichelte Kreise am selben Ort. Unter dem Titel: „Die Regeln werden geholt …“ | Kopf mit Namen sofort; Teile erscheinen, sobald sie da sind |
| Stand fehlt, Regeln da (Bild `a-400-ohne-stand`) | Seite ohne Stand: alle Monde als kleine Punkte, keine Legende. **Keine Fehlermeldung** | Zeile „Zustand“ entfällt |
| Regeln fehlen (Bild `a-400-fehler`) | Himmel und Sonne bleiben. Mittig ein Kasten (höchstens 340 px): „**Die Regeln sind gerade nicht zu erreichen.**“ / „Prüfe das Internet und versuch es nochmal.“ / Hauptknopf „Nochmal versuchen“ / Zweitknopf „Zur Reise“. Kein Technik-Text | derselbe Kasten im Blatt, Zweitknopf „Schließen“ |
| Regel „kommt später“ | Mond gepunktet | Karte öffnet normal. Der Hauptknopf entfällt; im Fuß steht: „Diese Regel kommt später auf deiner Reise.“ |

**Vorschlag an den Bau [M]:** Die 15 Regeln mit Satz, Grenze und Beispielen als feste Datei mit der App ausliefern (wie `daten/jugendwoerter.json`). Dann kann nur der Stand fehlen, und die Seite geht auch ohne Netz.

## 8 Die drei Wege

Entwurf: `entwurf/wege.html`. Reisekarte, Rückmeldung und Einstieg sind dort Platzhalter; neu ist nur, was hier steht.

### 8.1 Weg a – von der Reisekarte nach oben (Bild `weg-a-reisekarte`)

- **Knopf „Regeln“** oben rechts in der Karte, 12 px vom Rand: Kapsel 48 px hoch, Fläche mit Rand 1,5 px, links eine Sonne (Kreis 32 px, #FFD23F, Schein 5 px, darin „15“ 14 px / 700), rechts „Regeln“ 16 px / 700. Vorleser-Text: „Regeln am Himmel ansehen“.
- **Aufstieg (760 ms):** Die Karte schrumpft in 650 ms auf 9 % und wird rund; ab 150 ms blendet der Himmel in 500 ms ein. Auf der Übersicht fliegen die Planeten auf ihren Bahnen an ihren Platz (9), und um die Erde laufen zweimal zwei Ringe nach außen (je 1,1 s, Radius 1 → 2,6, Deckkraft 90 % → 0).
- **Zurück:** Erde antippen oder „Zurück“. Dieselbe Bewegung rückwärts: Die Erde wächst zur Karte.
- **Weniger Bewegung:** Überblenden in 150 ms, keine Ringe.
- Der Hauptknopf der Reisekarte bleibt unverändert der einzige gelbe Knopf dort. Die Sonne im Knopf „Regeln“ ist ein Zeichen, kein zweiter Hauptknopf: Die Kapsel selbst ist neutral.

### 8.2 Weg b – nach einem Fehler (Bilder `weg-b-nach-fehler`, `weg-b-karte`)

- Nur wenn der Server zum Fehler die Regel mitliefert (erkanntes Fehlbild). Sonst erscheint nichts.
- **Zeile unter „DU / ZIEL“**, 10 px Abstand: Knopf über die ganze Breite, mindestens 64 px, Rand 1,5 px in Kurs-Farbe, Grund Kurs-Grund, Radius 14 px. Links der Planet der Regel (34 px), dann „**Hier hat die Minusklammer geklemmt.**“ (17 px / 700) und darunter „Regel ansehen“ (16 px, unterstrichen), rechts „›“.
- Der Satz steht je Regel fertig in den Daten, weil die Namen verschiedene Artikel haben:

| Nr. | Satz | Nr. | Satz |
|---|---|---|---|
| 1 | Hier hat die Richtung geklemmt. | 9 | Hier hat die Probe gefehlt. |
| 2 | Hier hat das Zeichen-Paar geklemmt. | 10 | Hier hat „Wert bleibt“ geklemmt. |
| 3 | Hier hat die Rangfolge geklemmt. | 11 | Hier hat das Bruchrechnen geklemmt. |
| 4 | Hier hat das Verteilen geklemmt. | 12 | Hier hat die Potenz geklemmt. |
| 5 | Hier hat die Minusklammer geklemmt. | 13 | Hier hat der Stellenwert geklemmt. |
| 6 | Hier hat das Bündeln geklemmt. | 14 | Hier hat das Verhältnis geklemmt. |
| 7 | Hier hat die Waage geklemmt. | 15 | Hier hat das Nullprodukt geklemmt. |
| 8 | Hier hat das Umkehren geklemmt. | | |

- Antippen öffnet die Regel-Karte **über** der Aufgabe. Oben in der Karte die Ruf-Zeile mit demselben Satz. Fuß: Hauptknopf „Zurück zur Aufgabe“, keine zweite Zeile, **kein** Einstieg zu drei Aufgaben.
- „Zurück zur Aufgabe“, „Schließen“ und Esc schließen die Karte. Die Aufgabe steht unverändert da: gleiche Rückmeldung, gleiche Scroll-Lage, kein Versuch verbraucht.
- Die Zeile erscheint höchstens einmal je Rückmeldung und nie bei einer richtigen Antwort.

### 8.3 Weg c – neues Thema (Bild `weg-c-neues-thema`)

- Nur wenn in der Etappe eine Regel in neuem Gewand kommt (Etikett vom Mathe-Profi).
- **Kasten „Das kennst du schon“** über dem Hauptknopf der Etappe: Fläche, Rand 1,5 px, Radius 18 px, innen 14 px. Über-Zeile „DAS KENNST DU SCHON“, Überschrift 20 px / 700 (Beispiel: „Bisher mit Zahlen. Jetzt mit x.“), dann zwei Zwillingszeilen untereinander (Fläche 2, Radius 12 px): „Das kannst du“ mit der bekannten Zeile, „Das kommt jetzt“ mit der neuen. Rechnung Mono 15 px, ab 420 px Breite 17 px. Darunter Kapsel 48 px: Planet 34 px, „Regel: Verteilen ›“.
- Antippen der Kapsel öffnet die Regel-Karte. Ruf-Zeile: „Das kennst du schon. Hier kommt die Regel in neuem Gewand.“ Fuß: Hauptknopf „Weiter zur Erklärung ›“, schließt die Karte.
- Der Hauptknopf der Etappe („Erklärung starten ›“) bleibt der einzige gelbe Knopf auf der Seite.

### 8.4 Fuß der Regel-Karte je Weg

| Geöffnet von | Hauptknopf | Zeile darunter |
|---|---|---|
| Übersicht, Sonne, Planet | Drei Aufgaben zu dieser Regel › | Etwa 3 Minuten. |
| Weg b | Zurück zur Aufgabe | – |
| Weg c | Weiter zur Erklärung › | – |

## 9 Bewegung

| Was | Mit Bewegung | Weniger Bewegung |
|---|---|---|
| Ankunft der Planeten | je Planet 0,9 s: Drehung um die Sonne von −16° auf 0°, dabei einblenden; je Planet 70 ms später. Schilder blenden ab 0,5 s in 0,4 s ein | alles steht sofort |
| Monde | kreisen um ihren Planeten, eine Runde in 62 s (2 Regeln), 71 s (3), 80 s (4); Flugzeug der Erde 38 s | stehen |
| Sterne | etwa jeder achte blinkt: Deckkraft auf 12 % und zurück in 5 s. Nur dunkel | stehen |
| Schein der Sonne | Deckkraft 100 % ↔ 60 % in 7 s | steht |
| Blätter | fahren in 280 ms herein, Schleier 200 ms | erscheinen sofort |
| Wartekreise beim Laden | blinken in 1,4 s | stehen |
| Fenstergröße ändert sich | neu zeichnen ohne Ankunft | gleich |

Die Planeten selbst bleiben stehen: Tippflächen wandern nicht. „Weniger Bewegung“ gilt, wenn das Gerät es meldet (`prefers-reduced-motion`).

## 10 Was der Bau an Daten braucht

- **Fest, mit der App:** je Regel Nummer, Name, Satz für Weg b (8.2), Satz, zweiter Satz, Grenze, drei Gewand-Zeilen, Gegenbeispiel, zwei Seiten der Probe, Bild-Art. Je Planet Name, Zeichen, Satz, Regeln. Fünf Arbeitsweisen. Quelle: Mathe-Profi; für Regel 4 und 5 steht alles in 6.2 und 6.3.
- **Vom Server:** je Regel der Zustand `sitzt` / `in_arbeit` / `spaeter` – nur diese drei Werte, keine Zahl. Zu einer falschen Antwort wahlweise die Nummer der Regel (Weg b). Zu einer Etappe wahlweise die Nummer der Regel und die zwei Zwillingszeilen (Weg c). Je Regel bis zu vier Orte (Ort, Flug, Klasse).
- **Nicht in dieser Vorgabe:** wie „sitzt“ gerechnet wird, die drei Aufgaben, die Gemischte Fünf. Das legt der Mathe-Profi fest.

## 11 Prüfliste

**Muss**
- M1 Übersicht zeigt Sonne mit „15 REGELN“, sechs Planeten in der Reihenfolge aus 3.1 und den Gürtel; Radien, Lagen und Höhe wie in der Tabelle 3.2 (±2 px) bei 360 × 640, 400 × 860, 820 × 1180, 1280 × 800.
- M2 Bei 400 × 860, 820 × 1180 und 1280 × 800 passt alles ohne Scrollen; bei 360 × 640 scrollt die Seite höchstens 140 px, nichts ragt seitlich hinaus.
- M3 Je Regel genau ein Mond; die drei Zustände unterscheiden sich in der Form (voll, Ring, gepunktet), auch in Graustufen. Keine Zahl, kein Balken, kein Rot, kein Wort „wackelt“.
- M4 Jede Tippfläche mindestens 44 × 44 px; Sonne, Planeten, Gürtel und Zurück mit der Tastatur erreichbar, mit Vorleser-Text und sichtbarem Fokus.
- M5 Erde und „Zurück“ führen zur Reisekarte.
- M6 Regel-Karte „Verteilen“ und „Minusklammer“ haben alle zehn Teile aus 6.1 in dieser Reihenfolge, Texte wörtlich wie in 6.2 und 6.3.
- M7 In den drei Gewand-Zeilen läuft bei 360 px Breite keine Rechnung über den Rand; Brüche sind echte Brüche.
- M8 Probe: Die Knöpfe 2, 3, 4 ändern beide Seiten; die Ergebnisse stimmen mit 6.2 und 6.3.
- M9 Je Karte genau ein gelber Knopf; sein Text richtet sich nach dem Weg (8.4).
- M10 Weg b: Die Zeile erscheint nur mit erkannter Regel; nach „Zurück zur Aufgabe“ steht die Aufgabe unverändert da.
- M11 Hell und dunkel: alle Farben aus 5; Text gegen seinen Grund mindestens 4,5 : 1 (gerechnet: schwächstes Paar „leise“ auf hellem Himmel 6,2 : 1).
- M12 Fließtext mindestens 16 px. Ausnahmen: Über-Zeilen in Mono-Versalien 13 px, „REGELN“ in der Sonne, Klassen-Angabe in der Orte-Liste 14 px, laufende Nummer im Blatt „Sonne“ 14 px.
- M13 „Weniger Bewegung“: nichts bewegt sich (9).
- M14 Fehler-Kasten wie in 7, ohne Technik-Text; fehlt nur der Stand, erscheint keine Fehlermeldung.
- M15 Keine Namen der Kinder, keine echten Lerndaten in Bildern oder Tests.

**Soll**
- S1 Ankunft der Planeten und kreisende Monde wie in 9.
- S2 Aufstieg von der Reisekarte und Ringe an der Erde (8.1).
- S3 Die helle Seite jedes Planeten zeigt zur Sonne.
- S4 Schrift am Himmel hat den Rand in Himmelsfarbe; keine Bahn läuft durch einen Buchstaben.
- S5 Beim Schließen eines Blatts geht der Fokus zurück auf das öffnende Ziel; Esc schließt.
- S6 Blatt „Sonne“ mit allen 15 Regeln und Nummern.
- S7 Karte einer Regel „kommt später“ ohne Hauptknopf, mit dem Satz aus 7.

**Kann**
- K1 Sterne blinken, Schein der Sonne atmet.
- K2 Ab 900 px Regel-Namen neben den Planeten, wenn Platz ist.
- K3 Bilder für die Regeln 1–3 und 6–15 nach 6.4.
- K4 Übersicht B als zweite Ansicht.

## 12 Nicht geprüft, Annahmen

**Geprüft [G]:** Alle vier Entwürfe in Chrome ohne Fenster bei 360 × 640, 400 × 860, 820 × 1180 und 1280 × 800, hell und dunkel: keine Skriptfehler; Klickfolge Planet → Regel → Gewand → Probe → Zurück → Schließen, Sonne, Gürtel, Wege a, b, c; kein Ziel kleiner als 44 px; keine Rechnung läuft über; Maße der Tabelle 3.2 aus dem Entwurf gelesen.

**Nicht geprüft**
- Echte Geräte, Finger-Bedienung, Safari und Firefox.
- Kontrast: für Text aus den Farbwerten gerechnet (alle Paare ab 6,2 : 1), nicht am Bildschirm gemessen. Die Zeichen auf den Planeten liegen am Rand über der Schattenseite bei 2,8 bis 4,1 : 1; sie sind Schmuck, der Name steht daneben.
- Bewegung: nur im Code festgelegt, nicht als Film angesehen. Rechenlast der kreisenden Monde auf alten Geräten nicht gemessen.
- Vorleser (Screenreader): Texte gesetzt, nicht angehört.
- Platz des Knopfs „Regeln“ auf der echten Reisekarte (Überdeckung mit Pins oder Sticker): Der Entwurf zeigt einen Platzhalter.
- Fachlich: Sätze der Arbeitsweisen, Planeten-Sätze, umgestellte Beispiel-Zeilen, die 13 weiteren Karten.

**Annahmen**
- Der Server kann je Regel einen von drei Zuständen liefern und zu einer falschen Antwort die Regel nennen. Beides gibt es heute nicht.
- „Drei Aufgaben zu dieser Regel“ und „Gemischte Fünf“ lassen sich mit vorhandenen Aufgabenformen bauen (so steht es im Denkpapier, Abschnitt 7).
- Die Orte in „Diese Regel brauchst du in …“ kommen aus den Regel-Etiketten des Mathe-Profis. Im Entwurf sind sie erfunden.
- Alle Zustände in Entwürfen und Bildern sind erfunden („Beispiel A“, „Beispiel B“).
