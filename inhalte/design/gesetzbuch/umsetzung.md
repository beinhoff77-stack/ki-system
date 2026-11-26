# Vorgabe GB: Gesetzbuch der Mathematik – Zeichenstil, Übersicht, ein Gesetz aufgeschlagen

Designer, 26.11.2026. Stand `lernen-app` 01b103d. Kein App-Code, keine Datenbank, kein Lernstand.
Mathe-Inhalt wörtlich vom Mathe-Profi (`origin/mathe-profi` df14ade: `sonne.md`, `planet-flaeche-und-raum.md`, `inhalt.md`), eingelesen mit `entwurf/inhalt_lesen.py`. Was ich selbst ergänzt habe, steht in Abschnitt 9.
**[G]** gesichert (im Entwurf gebaut und gemessen) · **[A]** Annahme · **[M]** Meinung.

Die frühere Vorgabe RS-H (`inhalte/design/regeln-sonnensystem/`) ist abgelehnt und gilt nicht mehr.

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
