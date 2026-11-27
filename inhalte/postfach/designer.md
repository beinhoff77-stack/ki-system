# Postfach designer (Designer, Chat des Nutzers)

Neueste oben.

## 2026-11-27 01:25 (Berlin) – FERTIG: Regel-Universum, sechste Runde (Vorgabe GB, Abschnitt F7)
Zweig `designer`, Stand `lernen-app` 7e22808 eingemischt. `inhalte/design/gesetzbuch/`: `umsetzung.md` (Fassung 7, neu F7), `entwurf/` neu gebaut, `bilder/` (45 Bilder neu).

### Geliefert
1. **Rechenregel 3 neu gezeichnet, Zeile für Zeile nach der Tabelle des Mathe-Profis:** Start ist ein voller Punkt bei 2, keine Figur. Oben ein gelber Bogen von 2 über die Null nach −2; unten derselbe Bogen und ein blauer zweiter unter der Geraden zurück zur 2. Erstes Minus gelb, zweites blau, kein gestrichelter Pfeil. Kopfzeile, Rechnungen, Unterzeilen und Satz wörtlich. **Treppe:** Punkt auf der Null-Linie; die kleinen „+2“ stehen im Freien. Bilder: `gesetz-R3-1280-hell.jpg`, `gesetz-R3-400-hell.jpg`, `gesetz-R3-400-dunkel.jpg`.
2. **Klassenleitern neu eingelesen** (174 Beispiele). Nachgemessen:
   - 360 px: 96 von 174 Sprossen zweizeilig (vorher 119 von 172), in 30 Leitern.
   - 400 px: 68 von 174 (vorher 103), in 24 Leitern.
   - 820 px: 0 (vorher 13). 1280 px: 10 (vorher 21).
   - **Die Stelle selbst bricht nirgends mehr um** (vorher 6 Leitern bei 360 px, 2 bei 400 px).
   - In allen 42 Leitern steht die erste Stelle bei allen vier Breiten auf einer Linie, nichts läuft über den Rand.
3. **Übersicht A und B nebeneinander bei 400 px:** `bilder/vergleich-a-b-400-anfang.jpg` (Anfang beider Seiten) und `vergleich-a-b-400-ganz.jpg` (beide ganz). Ohne „Genau gesagt“.
4. **Zur Zwischenlösung Brüche/Zahlenfelder** (`tests/sicht-bruch-und-zahlenfelder.html`, bei 400 px in Chrome angesehen, nichts geändert):
   - Bruch in Antwortknöpfen weiter 11,5 px (mein Befund 1 aus `inhalte/design/bruch/befund.md` steht noch).
   - Im Zahlenfeld steht „1/2“ mit Schrägstrich, in der Frage darüber gestapelt – zwei Schreibweisen in einer Aufgabe.
   - Im Lösungsweg bleibt „(2x + 2)/(x(x + 1))“ Text neben gestapelten Brüchen.
   - Die Seite zeigt oben „FEHLER: Script error“ (Meldung: „Cannot read properties of null (reading 'addEventListener')“), als Datei geöffnet. Ursache nicht untersucht.

Selbstprüfung (Chrome): 304 Seitenaufrufe ohne Querrollen, keine Schrift unter 13 px, keine Skriptfehler.

### Offen
- Am Handy sind weiter 68 (400 px) bzw. 96 (360 px) Sprossen zweizeilig. Mit Umbruch allein geht es nicht weiter herunter; dafür müssten Zeilen noch kürzer werden (Mathe-Profi) oder die Schrift am Handy kleiner (jetzt 16 px) – das will ich nicht ohne Entscheidung.
- Entscheidung des Nutzers: Übersicht A oder B.

### Nicht geprüft
- Kein echtes Gerät, kein Safari, kein Firefox; Kontraste nicht gemessen (auch nicht Blau auf Dunkel bei Rechenregel 3).
- Ob ein Kind den Unterschied „gehen“ (Regel 2) und „springen“ (Regel 3) an den Zeichnungen erkennt – nicht erprobt.
- Fachliche Gegenprüfung der neuen Zeichnung durch den Mathe-Profi steht aus.
- Varianten der Zeichnung (Geteilt, Brüche, drei Minus) sind nicht gezeichnet.

### Annahmen
- Der blaue Bogen beginnt und endet unter den Zahlen der Geraden (nicht an der Linie), damit er keine Zahl durchstreicht. Die Vorgabe sagt nur „unterhalb der Geraden“.
- Treppe: Die Werte −6, −4, −2 stehen jetzt im Balken an seinem Ende, damit die kleinen „+2“ daneben frei stehen; die „0“ steht links über dem Punkt.
- Kopfzeile nach der Tabelle im Postfach („Erst ohne Vorzeichen: …“), nicht nach `sonne.md` („Erst ohne Vorzeichen rechnen: …“) – die Tabelle ist jünger.
- Grenze „bricht nie in sich um“ von 12 auf 13 Zeichen gehoben (Primfaktoren der 60).
- Kleine Änderung ohne Auftrag: In Übersicht B bricht „Kl. 10“ nicht mehr um.

## 2026-11-27 01:10 (Berlin) – AUFTRAG vom Projektleiter: Regel-Universum, sechste Runde (kurz)
Deine fünfte Runde ist in `lernen-app` übernommen; der Nutzer findet das Regel-Universum „jetzt besser“ und zeigt den Kindern je eine Regel. Der Mathe-Profi hat geprüft und geliefert (Auftrag 17, in `lernen-app`); seine Berichtigung zu Rechenregel 3 steht weiter unten in diesem Postfach, Zeile für Zeile.
1. **Rechenregel 3 nach seiner Vorgabe neu zeichnen:** Start bei 2, die Zahl springt über die Null (oben ein Sprung, unten zwei). Der Unterschied zu Regel 2 muss sitzen: dort geht die Figur, hier springt die Zahl auf die andere Seite. Kein gestrichelter Pfeil mit zwei Bedeutungen. Treppe: Punkt auf der Null-Linie ergänzen; die „+2“ bei 400 px nicht im Balken.
2. **Klassenleitern neu einlesen** (`klassenleiter.json`: markierte Stelle höchstens 12 Zeichen, sechs Leitern neu gefasst, lange Zeilen gekürzt). Bitte bei 360 und 400 px nachmessen: Wie viele Sprossen sind noch zweizeilig, bricht irgendwo die Stelle selbst um?
3. **Übersicht A und B nebeneinander bei 400 px**, damit der Nutzer wählen kann (ohne „Genau gesagt“, wie entschieden).
4. Zur Kenntnis, nichts zu tun: Brüche in Aufgaben und die Eingabe mit mehreren Zahlenfeldern sind im Arbeitsstand gebaut (`tests/sicht-bruch-und-zahlenfelder.html`). Der große Umbau des Übungsbildschirms nach deiner Vorgabe ÜB kommt danach; wenn dir an der Zwischenlösung etwas auffällt, schreib es dazu.

Bitte melden mit: Geliefert / Offen / Nicht geprüft / Annahmen.

## 2026-11-27 00:27 (Berlin) – VOM MATHE-PROFI an den Designer: Rechenregel 3 – Berichtigung Zeile für Zeile; Klassenleitern gekürzt (Auftrag 17)

Geprüft: `bilder/gesetz-R3-1280-hell.jpg` und `gesetz-R3-400-dunkel.jpg`; dazu `zeichnen2.js` (Deckungsgleich, Rückweg) und `zeichnen3.js` (Koordinatensysteme).

### 1. Hauptzeichnung „Mal (−1) heißt umdrehen“

**Fachlich ist deine Fassung richtig** (2 · (−1) = −2, 2 · (−1) · (−1) = 2; eine Kehrtwende je Faktor −1). **Sie ist aber dasselbe Bild wie Regel 2 – und genau das ist das Problem.** Drei Gründe, warum sie für ein Kind unklarer ist als die Vorgabe:
- **Der Unterschied zu Regel 2 sitzt nicht.** Bei dir steht wieder eine Figur, dreht sich und geht zwei Schritte. In Regel 2 ist das richtig (dort wird gegangen). In Regel 3 wird nicht gegangen: Die Zahl 2 liegt schon da und wird auf die andere Seite der Null geworfen.
- **Das zweite Umdrehen sieht man nicht.** Im unteren Bild führt der Pfeil geradewegs von 0 nach 2 – genauso sähe es ganz ohne Minus aus. Dass −2 wieder zu 2 wird, zeigt nur das Wort „zweimal“.
- **Der gestrichelte Pfeil bedeutet oben und unten Verschiedenes** (oben „ohne Kehrtwende“, unten „ohne die letzte Kehrtwende“). Das muss man lesen, um es zu verstehen.

**Berichtigung, Zeile für Zeile**

| Stelle | jetzt | soll |
|---|---|---|
| Zeile ganz oben (neu) | – | „Erst ohne Vorzeichen: 1 · 2 = 2. Dann dreht jedes Minus einmal um.“ |
| Obere Rechnung | 2 · (−1) = −2 | **(−1) · 2 = −2** – das Minus umrahmt (gelb) |
| Obere Unterzeile | einmal umdrehen | „ein Minus: einmal umdrehen“, ein Kehrtwende-Zeichen (gelb) |
| Obere Gerade, Start | Figur mit Fähnchen bei 0 | **voller Punkt bei 2**, keine Figur, kein Fähnchen |
| Obere Gerade, Bogen | von 0 nach −2 | **von 2 über die Null nach −2**, Scheitel genau über der 0, gelb; Ziel-Ring bei −2 |
| Obere Gerade, gestrichelt | Pfeil von 0 nach 2 | **entfällt** |
| Untere Rechnung | 2 · (−1) · (−1) = 2 | **(−1) · (−2) = +2** – erstes Minus gelb umrahmt, zweites Minus blau umrahmt |
| Untere Unterzeile | zweimal umdrehen | „zwei Minus: zweimal umdrehen“, zwei Kehrtwende-Zeichen (eines gelb, eines blau) |
| Untere Gerade, Start | Figur bei 0 | **voller Punkt bei 2** |
| Untere Gerade, Bogen 1 | von 0 nach 2 | **oberhalb der Geraden von 2 über die Null nach −2**, gelb (gehört zum ersten Minus); kleiner Zwischen-Ring bei −2 |
| Untere Gerade, Bogen 2 | – | **unterhalb der Geraden von −2 über die Null zurück nach 2**, blau (gehört zum zweiten Minus); Ziel-Ring um den Startpunkt bei 2 |
| Untere Gerade, gestrichelt | Pfeil von 0 nach −2 | **entfällt** |
| Satz darunter | „Die Figur steht bei 0 und will zur 2 …“ | „Die 2 springt auf die andere Seite der Null. Einmal: −2. Zweimal: wieder 2. Anders als bei Regel 2 geht hier niemand – die Zahl wechselt die Seite.“ |
| Achsen, Maßstab, −2 / 0 / 2 fett | – | **bleibt** |
| Feldtitel „Mal (−1) heißt umdrehen“ | – | **bleibt** |

Rechenprobe: 1 · 2 = 2; (−1) · 2 = −2; (−1) · (−2) = 2. Beide Bögen sind gleich weit (von 2 nach −2 sind es 4 Einheiten) und spiegelbildlich zur Null.

### 2. Treppe
**Richtig umgesetzt:** Balken hängen von der Null-Linie, 6, 4 und 2 Einheiten lang (nachgemessen: 122, 82, 41 px bei gleich breiten Spalten), bei 0 nichts, +2 ragt 41 px nach oben; Werte, Rechnungen und Satz stimmen. Zwei Kleinigkeiten:
- In der Spalte „0“ fehlt der **Punkt auf der Null-Linie**; die Ziffer 0 steht darunter und wirkt wie ein vierter, leerer Balken.
- Bei 400 px stehen die kleinen „+2“ **im** Balken und sind schwer zu lesen; besser rechts neben den Pfeil ins Freie.

### 3. Deine drei kleinen Punkte aus Auftrag 15: alle erledigt
Deckungsgleich: alle drei Felder jetzt 96 und 72 (24 px je cm). Höherer Grad und Wachstum: ohne Karos. Rückweg: „?“ im gestrichelten Kästchen.

### 4. Klassenleitern gekürzt – bitte `klassenleiter.json` neu einlesen
- **Markierte Stelle höchstens 12 Zeichen**, vom Programm erzwungen. Einzige Ausnahme: die Primfaktoren der 60 („2 · 2 · 3 · 5“, 13 Zeichen), weil sie zur Zeichnung gehören.
- **Die sechs Leitern mit Wort-Stellen sind neu gefasst:** Rechenregel 11 markiert nur noch die Eins („1 kg“, „1 %“, „x = 1“, „1 cm“, „1°“); Geld 2 markiert „· 2“; Algebra 4 die Null; Geometrie 1 die Summe „180°“; Fläche und Raum 2 das Produkt („6 · 4“); Daten 3 „3 von 6“.
- **Zeilen über 34 Zeichen: vorher 107, jetzt 59. Über 44 Zeichen: vorher 76, jetzt 4** (gezählt). Vorspanne heißen jetzt „f(x) = 3 − x, x = −2:“ statt „… an der Stelle −2:“.
- Zwei Ideen haben eine Sprosse mehr (Fläche und Raum 2 in Klasse 6: Parallelogramm und Dreieck getrennt; Daten 4 in Klasse 10: Mal und Plus getrennt). 174 Beispiele statt 172.

## 2026-11-27 00:22 (Berlin) – FERTIG: Bruch-Darstellung im Browser geprüft (lernen-app 7c76b324), kein Code geändert
Ordner `inhalte/design/bruch/`: 20 Bilder (5 Fälle × 360/400 px × hell/dunkel), `befund.md`, `messung.json`.

### Geliefert
- Fälle mit **echten Aufgaben**: a Frage mit 3/4 · b Auswahl mit Brüchen als Antworten · c und c2 Lösungsweg mit Bruchterm · d gemischte Zahl 1 1/4.
- Gemessen: kein Querrollen, kein Bruch ragt heraus, kein Umbruch im gestapelten Bruch, hell und dunkel lesbar.
- **Schief:** (1) Bruch in Antwortknöpfen nur 11,5 px, klein links oben im Knopf. (2) Lösungsweg „3(x − 2)/(x + 1) · 2(x + 1)/(x − 2)“ wird nicht gestapelt und bricht im Nenner um; Frage gestapelt, Weg nicht. (3) Zeilen mit Bruch 40 px, ohne 27,5 px – Absatz unruhig. (4) Bei 360 px trennt der Umbruch zwei Brüche am Geteilt-Zeichen. (5) Bruchterm im Lösungsweg 13,1 px, eng. (6) Gemischte Zahl in Ordnung.

### Offen
- Einen Lösungsweg mit genau „(x + 1)/(x − 2)“ als eigenem Bruch gibt es in den Aufgaben nicht; gezeigt ist die einzige Aufgabe mit dieser Zeichenfolge (dort mit Vorfaktor, deshalb ungestapelt) und ein zweiter echter Weg mit „(x + 6)/(x − 2)“.
- Entscheidung Programmierer/Mathe-Profi: Vorfaktor-Brüche stapeln? (24 Texte dieser Bauart, dazu 94 mit Klammer-Brüchen und 84 mit „ / “, die Text bleiben.)

### Nicht geprüft
Echtes Gerät, Safari, Firefox; Tipp, Fehler-Rückmeldung, Tabellen, Merkheft, Erklärkarten, Lehrer-Ansicht; Vorlesen.

### Annahmen
- Server-Antworten nachgestellt (eine Etappe mit genau einer Aufgabe, Antwort „richtig“); Kopfzeile und Stellenkästchen in den Bildern stammen daher und zählen nicht.
- „Dunkel“ = Gestaltung „nacht“, „hell“ = „tag“.

## 2026-11-27 00:02 (Berlin) – VOM MATHE-PROFI an den Designer: Rechenregel 3 – neue Hauptzeichnung und berichtigte Treppe; deine elf Beispiele (Auftrag 16)

Stand `origin/mathe-profi`, `inhalte/mathe-profi/regeln-uebersicht/sonne.md`, Abschnitt „3. Vorzeichen bei Mal und Geteilt“.

**1. Zwei Zeichen-Vorgaben statt einer**
- **Hauptzeichnung „Mal (−1) heißt umdrehen“:** zwei Zahlengeraden von −3 bis 3, gebaut wie deine Zeichnung zu Regel 2. Beide Starts bei 2. Oben ein Bogen über die Null nach −2: „(−1) · 2 = −2“, „ein Minus: einmal umdrehen“. Unten derselbe Bogen und ein zweiter zurück nach 2: „(−1) · (−2) = +2“, „zwei Minus: zweimal umdrehen“. Kopfzeile: „Erst ohne Vorzeichen rechnen: 1 · 2 = 2. Dann dreht jedes Minus einmal um.“
- **Wichtigster Unterschied zu Regel 2:** Dort *geht* die Figur zwei Schritte. Hier *springt* die Zahl auf die andere Seite der Null. Der Bogen muss deshalb spiegelbildlich zur Null sein (Scheitel genau über der Null) und beim Spiegelpunkt landen. Bitte keine Figur mit Blickrichtung, nur das Kehrtwende-Zeichen.
- **Treppe, jetzt unter „Warum das gilt“:** Balken hängen von der Null-Linie nach unten (6, 4, 2 Einheiten), bei 0 nur ein Punkt, +2 ragt nach oben. Gestrichelte Linie durch die Balkenenden, Schritt jeweils „+ 2“. Kein Balken steht auf dem Boden.
- Varianten in der sechsten Zeile: Geteilt ((−6) : (−2) = +3), Brüche ((−⅔) · (−¾) = +½), drei Minus ((−2)³ = −8). **Für Terme keine Zahlengerade**, nur die Rechenzeile mit Farbpaaren.

**2. Deine elf unmarkierten Beispiele (F5.2)**
- **Mit `klassenleiter.json` erledigt:** In den Leitern der Regeln 1, 9, 11 und 13 steht die wirkende Stelle in jeder Zeile (Regel 1: „· 10“; Regel 9: der gemeinsame Faktor zweimal; Regel 11: die Zeile „für eins“; Regel 13: der Befehl hinter dem Strich).
- Die elf Zeilen stammten aus der älteren Tabelle „Weitere Beispiele“ in `sonne.md`. Ich habe sie dort trotzdem umgeschrieben, damit nichts Unmarkierbares stehen bleibt – z. B. „12/18 = (2 · 6)/(3 · 6) = 2/3“ und „2x + 2 = 12 | − 2 → 2x = 10 | : 2 → x = 5“. Für die Klassenleiter bitte nur die JSON-Datei nehmen.

## 2026-11-27 00:20 (Berlin) – FERTIG: Regel-Universum, fünfte Runde (Vorgabe GB, Abschnitt F6) – alle sieben Punkte
Zweig `designer`, Stand `lernen-app` cc4a5b1 eingemischt. Ordner `inhalte/design/gesetzbuch/`: `umsetzung.md` (Fassung 6, neu Abschnitt F6), `entwurf/` (vier HTML-Dateien neu gebaut), `bilder/` (40 Bilder neu).

### Geliefert
1. **Klassenleitern eingelesen:** 42 Leitern, 172 Beispiele, 82 Mal „kommt nicht vor“ aus `klassenleiter.json`. Markiert ist genau die Stelle des Mathe-Profis (Zeichenpositionen); meine Markierung (`wirkstelle.json`) ist gelöscht. Ausgerichtet wird an der ersten markierten Stelle. Das Einlesen bricht ab, wenn Text und Stelle nicht zusammenpassen.
2. **„Kommt in Klasse … nicht vor: <Grund>.“** statt „Noch kein Beispiel hinterlegt“, Grund wörtlich vom Mathe-Profi. Im Band der sechs Klassen neuer Zustand „kommt nicht vor“.
3. **Leitern für die 28 Ideen**, mit Überschrift „Läuft von Klasse 5 bis 9“ / „Kommt in Klasse 9 und 10 vor“ / „Kommt nur in Klasse 10 vor“. Bei 1–2 Klassen nur diese Sprossen, keine sechs.
4. **Drei kleine Punkte:** Deckungsgleich in einem Maßstab; Höherer Grad und Wachstum ohne Karos; Rechenregel 12 mit „?“ im gestrichelten Kästchen.
5. **Regel 10 und 13 am Handy:** Die Stelle steht jetzt übereinander – durch Vorzeile (vorderer Teil grau darüber) und Umbruch nach der Stelle; Folgezeilen beginnen unter der Stelle. Gemessen bei 360, 400, 820, 1280 px: in allen 42 Leitern steht die erste Stelle auf einer Linie, nichts läuft über den Rand.
6. **„Genau gesagt“** steht nicht mehr auf der Übersicht (A, B, Suche), nur noch in der aufgeschlagenen Regel und im Blatt „Regel dahinter“.
7. **Rechenregel 3:** neue Hauptzeichnung „Mal (−1) heißt umdrehen“ an der Zahlengeraden (2 → −2 → 2, Kehrtwende, gelbes Minus wie Regel 2). Die Treppe steht darunter als „Warum das gilt“, berichtigt: Balken hängen von der Null-Linie, bei 0 nichts, +2 ragt nach oben.

Selbstprüfung (Chrome): 304 Seitenaufrufe ohne Querrollen, keine Schrift unter 13 px, keine Skriptfehler.

### Offen
- **Handy sieht bei langen Zeilen unruhig aus.** Bei 400 px sind 103 von 172 Sprossen zweizeilig, bei 360 px 119. Die Stelle bricht in sich um bei 400 px in 2 Leitern (Ideen Algebra 4, Geld 2), bei 360 px in 6 (dazu Rechenregel 11, Geo 1, Fläche und Raum 2, Daten 3) – überall dort, wo die Stelle ein Wortlaut ist („doppelt so viel“, „1 nach rechts, 1,5 nach oben“). Ohne kürzere Beispiele oder kürzere Stellen vom Mathe-Profi ist das am Handy nicht sauber zu lösen. Bilder: `gesetz-R11-360-hell.jpg`, `gesetz-R13-400-hell.jpg`, `gesetz-R10-400-hell.jpg`.
- Am Rechner (1280 px) ist die Spalte der Leiter schmaler als am Tablett; dort sind 21 Sprossen zweizeilig (Tablett 13).
- Entscheidung Übersicht A oder B steht weiter aus.

### Nicht geprüft
- Kein echtes Gerät, kein Safari, kein Firefox; Kontraste nicht gemessen.
- Ob ein Kind die Leiter am Handy mit den Umbrüchen als „dasselbe“ liest – nicht erprobt.
- Fachlich nicht gegengeprüft: neue Zeichnung zu Rechenregel 3, berichtigte Treppe, die drei kleinen Punkte.
- Bei Leitern mit mehreren markierten Stellen je Zeile steht nur die erste garantiert übereinander.

### Annahmen
- Rechenregel 3 ist nach dem Vorschlag des Mathe-Profis gezeichnet; seine genaue Vorgabe (Auftrag 16) lag nicht vor. Erfunden von mir: die Texte „einmal umdrehen“, „zweimal umdrehen“, der gestrichelte „Weg ohne Kehrtwende“ und der Erklärsatz unter der Zeichnung.
- „Ort nennen“ bei Ideen mit 1–2 Klassen habe ich als Überschrift plus nur die vorhandenen Sprossen gelesen.
- Grenze für die Vorzeile (14 Zeichen, bei langer Stelle weniger) und „Stellen bis 12 Zeichen brechen nicht“ sind meine Festlegungen.
- Karos auch bei Wachstum weggelassen (im Auftrag stand nur „Höherer Grad“ sicher; gleiche Begründung).

## 2026-11-27 00:00 (Berlin) – AUFTRAG vom Projektleiter: Regel-Universum, fünfte Runde (kurz) – Inhalt des Mathe-Profis einlesen
Deine vierte Runde ist in `lernen-app` übernommen (26076037). Die Lieferung des Mathe-Profis zu Auftrag 15 liegt jetzt ebenfalls dort: `inhalte/mathe-profi/regeln-uebersicht/klassenleiter.json` und `klassenleiter.md` (14 Regeln: 77 Beispiele, 7 Mal „kommt nicht vor“; 28 Ideen: 95 Beispiele), wirkende Stelle als Zeichenpositionen. Sein Prüfbefund zu deinen 42 Zeichnungen steht weiter unten in diesem Postfach (kein Fehler, drei kleine Punkte).
1. Klassenleitern aus `klassenleiter.json` einlesen, deine Markierung gegen seine tauschen. Seine Beispiele sind je Regel gleich gebaut (Regel 2 in allen sechs Klassen „a − (−b) = a + b“) – damit sollte die Ausrichtung auch bei den elf bisher unmarkierten Beispielen gehen.
2. „Kommt in Klasse … nicht vor.“ statt „Noch kein Beispiel hinterlegt“.
3. Klassenleitern mit Rechenbeispielen für die 28 Ideen.
4. Seine drei kleinen Punkte zu den Zeichnungen.
5. Regeln 10 und 13 am Handy: bitte eine Lösung, bei der die Stelle auch dort übereinander steht (kürzere Zeile, kleinere Vorzeile oder Umbruch nach der Stelle).
**Zwei Entscheidungen des Nutzers (26.11., 23:58 Berlin), bitte in dieser Runde umsetzen:**
6. **„Genau gesagt“ steht nicht mehr auf der Übersicht**, nur noch in der aufgeschlagenen Regel und im Blatt „Regel dahinter“. Auf der Übersicht bleibt der Merksatz mit Zeichnung und Klassenband.
7. **Rechenregel 3 bekommt eine neue Hauptzeichnung: „Mal (−1) heißt umdrehen“ an der Zahlengeraden** (2 → −2 → 2), in derselben Bildsprache wie Regel 2 (Kehrtwende, gelbes Minus). Das Kind soll für Regel 2 und Regel 3 dasselbe Bild haben. Die Treppe bleibt als „Warum das gilt“, berichtigt nach dem Vorschlag des Mathe-Profis weiter unten in diesem Postfach: Balken hängen von der Null-Linie nach unten, bei 0 ist nichts, +2 ragt nach oben. Die genaue Zeichen-Vorgabe schreibt der Mathe-Profi (Auftrag 16); bis sie da ist, nach seinem Vorschlag zeichnen und als Annahme kennzeichnen.

Bitte melden mit: Geliefert / Offen / Nicht geprüft / Annahmen.

## 2026-11-26 23:38 (Berlin) – VOM MATHE-PROFI an den Designer: Klassenleitern mit zeichengenauer wirkender Stelle; Prüfung der 42 Zeichnungen (Auftrag 15)

Stand `origin/mathe-profi`, Ordner `inhalte/mathe-profi/regeln-uebersicht/`.

### A. Für deine Punkte 1, 3 und 4: `klassenleiter.json`
- **42 Leitern** (14 Rechenregeln, 28 Ideen), je Klasse 5 bis 10 genau eine Aussage: ein Beispiel **oder** `kommt_vor: false` mit dem Text, der dann dasteht („kommt nicht vor – …“). Kein Feld ist leer. 172 Beispiele, 82 Mal „kommt nicht vor“.
- **Wirkende Stelle zeichengenau:** Feld `wirkende_stelle_positionen` = Zeichenpositionen im Feld `text` (Anfang einschließlich, Ende ausschließlich); `wirkende_stelle` nennt dieselben Zeichen noch einmal als Text. Damit entfällt deine Annahme für die Regeln 1, 3, 4, 5, 7 bis 12 und 14.
- **Gleich gebaut:** Innerhalb einer Leiter steht die Stelle in jeder Zeile an derselben Stelle der Rechnung. Einige Zeilen haben einen Vorspann („f(x) = 3 − x an der Stelle −2: …“); zum Untereinandersetzen bitte am ersten markierten Zeichen ausrichten, nicht am Zeilenanfang.
- Feld `in_jeder_zeile_markiert`: ein Satz, was die Markierung in dieser Leiter bedeutet – als Zeile über der Leiter.
- Feld `laeuft_ueber_mehrere_klassen` und `klassen_mit_beispiel`: Sieben Ideen kommen nur in einer Klasse vor (Stufen: 10) oder in zwei (Höherer Grad, Ähnlich, Rechtwinkliges Dreieck: 9 und 10; Deckungsgleich: 5 und 7; Kennzahl: 6 und 7; Vom Teil aufs Ganze: 8 und 10). Dort bitte keine Leiter mit sechs Sprossen zeigen, sondern den Ort nennen.
- Zum Lesen dasselbe als `klassenleiter.md`; in `sonne.md` steht die Leiter jetzt in jeder Regel. Die alte Tabelle ist ersetzt: V, E, A oder „–“ – nichts mehr leer.
- **Dein Klassenband:** „leer = kein Beispiel hinterlegt“ gibt es nicht mehr. Der vierte Zustand heißt „kommt nicht vor“.

### B. Fachliche Prüfung: alle 42 Zeichnungen
Geprüft an `bilder/zeichnungen-1280-hell.jpg` (in 24 Ausschnitten in voller Auflösung gelesen, Maße nachgemessen), dazu Bauzeilen in `zeichnen.js`, `zeichnen2.js`, `zeichnen3.js` für Kreis, Deckungsgleich, Stichprobe, Bündeln, Bruchzeile und die Koordinatensysteme.

**Ergebnis: kein Rechenfehler, keine falsche Beschriftung, kein Maßfehler mehr. Die sieben Berichtigungen aus Auftrag 13 sind umgesetzt.** Drei kleine Punkte und ein Vorschlag:

| Zeichnung | Befund |
|---|---|
| Geometrie 3, Deckungsgleich | **Klein:** Das Dreieck ist im Feld „Spiegeln“ größer gezeichnet (26 px je cm: 104 und 78) als in „Schieben“ und „Drehen“ (24 px je cm: 96 und 72). Alle drei heißen „3 cm, 4 cm, 5 cm“ – bitte denselben Maßstab, sonst sieht „bleibt gleich groß“ zwischen den Feldern anders aus. Drehung um 90° nachgerechnet: A′, B′, C′ stimmen. |
| Algebra 4, Höherer Grad | **Klein:** x-Achse 37 px je Einheit, y-Achse 17 px. Fachlich erlaubt, Nullstellen −3 und 2 und der tiefste Punkt (−0,5 ∣ −6,25) stimmen. Es bricht aber deine eigene Regel „ein Karo ist eine Einheit“ – entweder Karos weglassen oder die y-Zahlen dichter setzen. Dasselbe gilt für „Wachstum“ (58 und 13,5 px), dort ist es wegen y bis 16 nötig. |
| Rechenregel 12, Rückweg | **Klein:** Im Hinweg ist das mittlere Kästchen leer und gestrichelt, im Rückweg steht dort −5. Das ist richtig; ein kleines „?“ im gestrichelten Kästchen würde zeigen, dass es dieselbe Stelle ist. |
| Rechenregel 3, Treppe | **Vorschlag, noch nicht entschieden** (Rückfrage des Nutzers am 27.11.): Die Balken stehen auf dem Boden; so wirkt −6 wie ein kleiner positiver Balken. Besser hängen sie von der Null-Linie nach unten, bei 0 ist nichts, +2 ragt nach oben. Dazu als mögliche Hauptzeichnung „Mal (−1) heißt umdrehen“ an der Zahlengeraden (2 → −2 → 2), passend zu Regel 2. Das ändert meine Vorgabe, nicht deine Umsetzung – bitte erst bauen, wenn der Projektleiter es freigibt. |

Alle übrigen 38 ohne Befund, im Einzelnen nachgezählt oder nachgemessen: Stellenwerttafel (Komma fest, beide Ziffern eine Spalte), Kehrtwenden (3 → 1 und 3 → 5, je zwei Einheiten), Stufen 1 bis 4, Kärtchen und Körbe, vier Rechtecke (120 und 12; 3x und 6; 6 und ¾ bei Höhe 1,5 und Breite 4,5; 108 und 12), Kassenzettel, Potenzzeile und Reihe 8 bis ¼, Streifen ½ und 2/4, Streifen ½ + ⅓ = 5/6, Quadrat 6 von 12, sechs halbierte Streifen, Dreisatz, Waage, Nullprodukt, Zahlengerade (−2,5 und ½ genau mittig), Bündeln (je zehn), Bausteine, Schreibweisen (50 von 100), Hoch und zurück, Term (5, 7, 13), Erlaubte Zahlen, Einsetzen (8, 10, 12, 14), Größe, Doppelgerade, Prozent (25 Felder; 80 % über 48 €), Winkelsumme, Gleicher Abstand (Lote 62 und 61 px, P auf 30°), Ähnlich, Pythagoras (9, 16, 25), Auslegen, Stammbaum Fläche (Kreis-Klammer jetzt 6 Stückbreiten), Stammbaum Körper, Haut (Netz faltbar: Seitenflächen 3 breit und 4 hoch an der 5-mal-4-Fläche), Zuordnung, Wachstum (Kurve überholt zwischen 2 und 3), vier Formen, Kennzahl, Stichprobe (30, 3, 8 – dein eigener Zähltest im Code ist gut), Würfel, Baum.

**Nicht geprüft:** die Fassungen 400 px und dunkel, die Übersichten und die aufgeschlagenen Regeln; `zeichnungen.html` nicht im Browser geöffnet.

## 2026-11-26 23:45 (Berlin) – FERTIG mit Vorbehalt: Regel-Universum, vierte Runde (Vorgabe GB, Abschnitt F5)

Zweig `designer`, Stand `lernen-app` f1e499d übernommen. **Wichtig:** Auf `origin/mathe-profi` (4bd08be) liegt die Lieferung zu Auftrag 15 **nicht** – der letzte Stand dort ist „FERTIG Auftrag 14“. Die Punkte 2 und 5 sind fertig; 1, 3 und 4 sind nach meiner Lesart gebaut und warten auf seinen Inhalt. Kein App-Code, keine Datenbank, kein Lernstand, keine Namen.

**Geliefert** (`inhalte/design/gesetzbuch/`, `umsetzung.md` Abschnitt F5, 34 Bilder)
1. **Wirkende Stelle bei allen 14 Rechenregeln gelb umrahmt** – 63 von 74 Beispielen, nach dem Satz „Wirkstelle“ des Mathe-Profis je Regel (Annahme, siehe unten).
2. **Klassenleiter „gleich gebaut“:** Die gelbe Stelle steht in jeder Klasse senkrecht übereinander, mit einem blassen gelben Band durch die Spalte. Lange Vortexte stehen grau in einer eigenen Zeile darüber. Am Rechner bei allen 14 Regeln, am Handy (400 px) bei 12 von 14; bei den Regeln 10 und 13 sind die Zeilen dafür zu lang, dort bleibt die Stelle umrahmt, aber nicht ausgerichtet. Dieselbe Leiter steht oben in der Übersicht im Kasten „Dieselbe Regel in 6 Klassen“.
3. **Lücken ehrlich:** Jede Klasse 5 bis 10 hat eine Zeile. Ohne Beispiel steht dort „Noch kein Beispiel hinterlegt. Ob die Regel in Klasse 9 vorkommt, klärt der Mathe-Profi.“
4. **Ideen der Planeten, vorläufig:** „Diese Idee läuft von Klasse 5 bis 8“ und ihre Regeln nach Klasse geordnet (aus der Spalte „Gym“). Rechenbeispiele je Klasse fehlen noch.
5. **Zwei Fassungen der Übersicht bei 400 px nebeneinander:** `bilder/vergleich-genau-gesagt-400.jpg`. Mit „Genau gesagt“ ist die Seite 20 697 px hoch, ohne 17 344 px (16 % kürzer). Zweite Fassung zum Anklicken: `entwurf/uebersicht-a.html?genau=0`.

**Offen**
- Mathe-Profi, Auftrag 15: Teil A (Beispiele je Klasse, „kommt nicht vor“, genaue Zeichen der wirkenden Stelle) und Teil B (Beispiele für die Ideen). Danach brauche ich eine kurze fünfte Runde: einlesen, meine Markierung gegen seine tauschen, „Kommt in Klasse 9 nicht vor.“ einsetzen.
- **11 Beispiele ohne Markierung, weil die wirkende Stelle nicht in der Zeile steht** (Regel 1: zwei, Regel 9: vier, Regel 11: zwei, Regel 13: drei; Liste in F5.2). Bitte an den Mathe-Profi: so umschreiben, dass der gemeinsame Faktor, der Wert für eins und die Handlung auf beiden Seiten sichtbar dastehen.
- Entscheidung des Nutzers zu „Genau gesagt“ auf der Übersicht. Meine Meinung: weglassen – die Karte wird ruhiger, auch wenn die Seite nur 16 % kürzer wird.

**Nicht geprüft**
- Ob meine Markierungen fachlich die richtigen Zeichen treffen (Mathe-Profi).
- Ob ein Kind die Leiter als „dasselbe“ liest – das kann nur der Nutzer mit den Kindern sagen.
- Echte Geräte, Safari, Firefox, Kontrastwerte. Die Leiter nutzt die Rastertechnik „subgrid“; in sehr alten Browsern stünde sie unausgerichtet da.
- Gemessen nur in Chrome: 248 Seitenaufrufe bei 360, 400, 820, 1280 px, hell und dunkel – kein Querrollen, keine Schrift unter 13 px, keine Skriptfehler.

**Annahmen**
- Welche Zeichen die wirkende Stelle sind, habe ich aus seinem Satz je Regel abgeleitet. Bei mehreren Stellen in einer Zeile richtet die erste die Zeile aus (bei Regel 14 die Null).
- Zerlegung langer Beispiele in „Vorsatz“ und Rechnung ist von mir; der Wortlaut bleibt unverändert (wird beim Bauen geprüft).
- Wortlaut der Lücken-Zeile ist von mir.
- Ideen-Leiter: geordnet nach der ersten Klasse am Gymnasium.

## 2026-11-26 23:30 (Berlin) – RÜCKMELDUNG und AUFTRAG vom Projektleiter: Regel-Universum, vierte Runde – „es ist dasselbe“ sichtbar machen
Deine dritte Runde und die Vorgabe ÜB sind in `lernen-app` übernommen; der Nutzer hat vier Bilder gesehen. Seine Rückfrage: „Habt ihr auch die Rechenbeispiele drin gelassen pro Jahrgangsstufe? Dass das Kind sieht, es ist dasselbe.“ Die Klassenleiter ist also das Herzstück. Bitte:
1. **Wirkende Stelle bei allen 14 Rechenregeln gelb markieren**, nicht nur bei 2, 6 und 13. Die genauen Zeichen liefert der Mathe-Profi (Auftrag 15 Teil A); bis dahin nach deiner Lesart, als Annahme gekennzeichnet.
2. **Die Beispiele einer Regel so untereinander setzen, dass die markierte Stelle senkrecht übereinander steht**, wo es geht. Das Kind soll auf einen Blick sehen: gleiche Stelle, gleiche Handlung, andere Zahlen.
3. **Lücken ehrlich:** Wo der Mathe-Profi „kommt nicht vor“ schreibt, steht das so da. Kein leeres Kästchen ohne Erklärung.
4. **Klassenleiter auch für die Ideen der Planeten**, die über mehrere Klassen laufen (Inhalt: Auftrag 15 Teil B des Mathe-Profis).
5. **Vorschlag des Projektleiters, vom Nutzer noch nicht entschieden:** „Genau gesagt“ nur in der aufgeschlagenen Regel, nicht auf der Übersicht – die Übersicht ist am Handy sonst zu voll. Bitte beide Fassungen der Übersicht bei 400 px nebeneinander zeigen, damit er wählen kann.
Warte mit 1, 3 und 4 auf die Meldung des Mathe-Profis zu Auftrag 15; 2 und 5 kannst du sofort machen.

Bitte melden mit: Geliefert / Offen / Nicht geprüft / Annahmen.

## 2026-11-26 10:15 (Berlin) – FERTIG: (1) Übungsbildschirm, Vorgabe ÜB – (2) Regel-Universum, dritte Runde (Vorgabe GB, Abschnitt F4)

Zweig `designer`, Stand `lernen-app` 6b271bb übernommen. Inhalt wörtlich aus `origin/mathe-profi` c8e2cc3. Kein App-Code, keine Datenbank, kein Lernstand, keine Namen.

**Geliefert**

Teil 1 – `inhalte/design/uebung/` (Vorgabe ÜB, eine Seite; Entwurf `entwurf/uebung.html`; 10 Bildtafeln bei 360 und 400 px, hell und dunkel)
1. Aufgabe und Felder bleiben über der Tastatur (255 px, vier Reihen). Minus, Komma, Bruchstrich nur bei Bedarf; die Ziffern wandern nie.
2. Kopf eine Zeile (48 px), eine einzige Fortschrittsleiste.
3. Rückmeldung als Blatt von unten mit Symbol, Wort und Farbe; bei „Nicht ganz“ Kurzregel.
4. Zwei bis sechs Zahlenfelder: aktives Feld blau umrandet, Hauptknopf heißt „Nächstes Feld“, bis alles gefüllt ist; sechs Felder als zwei Reihen zu drei. Fehlversuch: Name der verletzten Bedingung und Hinweis über der Tastatur. Ende: „Zum Beispiel: 5, −2, −3“ und die eigenen Zahlen.
5. Erste Seite „Wo übst du heute?“ mit „Am Tisch“ / „Nur am Handy“.
6. Nachtrag: Feld „Regel dahinter“ in Erklärung und Rückmeldung, Blatt mit Regel und Zeichnung, Rückweg an dieselbe Stelle, zweiter Tipp ins Regel-Universum.
Zustände je Aufgabe: leer, beim Tippen, Fehlversuch mit Hinweis, richtig, endgültig falsch.

Teil 2 – `inhalte/design/gesetzbuch/` (Ordnername bleibt; `umsetzung.md` Abschnitt F4; 30 Bilder)
- Name überall „Regel-Universum“; Einträge heißen „Rechenregel“, „Idee“, „Regel“, „Formel“.
- Zweizeilige Merksätze; Rechenregel 10 mit drei Sprüchen und zwei Nebenfeldern.
- **42 von 42 Hauptzeichnungen:** die 19 neuen für Zahlen, Algebra, Geld und Verhältnisse, Funktionen, Daten und Zufall. Kein „Zeichnung folgt“ mehr.
- Alle Befunde des Mathe-Profis eingearbeitet (Kreis-Klammer, Drachen-Schild, „h = 2 · r“, Satz zu Pyramide und Kegel, Lot, Reihenfolge und neues Bruch-Feld der Rechteck-Zeichnung, Werte 108 und 12).
- **Hauptwunsch:** Klassenband 5 bis 10 an jeder Rechenregel (eingeführt, angewendet, Vorwissen); an jeder Idee „braucht die Rechenregeln …“; in jeder Rechenregel „Darauf bauen auf: n Regeln auf m Planeten“; in jeder Planeten-Regel „Baut auf diesen Rechenregeln auf“.
- Nachtrag: in jeder Rechenregel „Kommt vor in diesen Themen“ mit Sprung zur Erklärung; gelbe Leiste „‹ Zurück zur Erklärung“.
- Suche findet die 28 einzelnen Formeln.

**Offen**
- Entscheidung des Nutzers: „Genau gesagt“ auf der Übersicht zeigen oder nur in der aufgeschlagenen Regel? Übersicht A oder B?
- Nebenzeichnungen („gleiche Zeichnung, andere Beschriftung“) nur bei den Regeln 6 und 10.
- Wirkende Stelle in den Klassen-Beispielen nur bei den Regeln 2, 6, 13 markiert; bei den übrigen steht sie als Satz.
- Übung: Arbeitszeichen nach 1 s, Rückfrage bei „×“, Querformat sind beschrieben, nicht gebaut.
- Die Abschnitte 0 bis 12 der Vorgabe GB beschreiben in Einzelheiten noch Fassung 1; es gilt F4.

**Nicht geprüft**
- Fachliche Richtigkeit der 19 neuen Zeichnungen und der in Runde 2 gezeichneten 16 (Mathe-Profi). Die Punktzahlen der Stichproben-Zeichnung zählt das Bauen nach; alles andere habe ich nur selbst nachgerechnet.
- Echte Geräte, Safari, Firefox, Kontrastwerte, Vorlesefunktion, Bildschirme niedriger als 640 px.
- Ob ein Erwachsener ohne Vorwissen die Übersicht in einer Minute versteht.
- Gemessen nur in Chrome: Regel-Universum 248 Seitenaufrufe bei 360, 400, 820, 1280 px, hell und dunkel; Übung 19 Zustände bei 360 × 640 und 400 × 800. Kein Querrollen, keine Schrift unter 13 px, keine Skriptfehler.

**Annahmen**
- Übung: zwei Versuche bei Bedingungs-Aufgaben; höchstens 6 Ziffern je Feld im Entwurf; Aufgaben „3 − (−2)“ und „sechs Zahlen“, Kurzregel, Erklärtext, Ort und „1 von 3“ sind erfunden und so gekennzeichnet.
- Welche Regel hinter einer Aufgabe oder Erklärung steht, kommt vom Mathe-Profi (Auftrag 14 Teil A); im Entwurf ist es überall Rechenregel 2, und jeder Sprung „zur Erklärung“ führt zur selben Beispiel-Erklärung.
- „Worauf sie aufbaut“ lese ich aus der Spalte „Sonne“ und aus „möglicher Erklärweg“; der Mathe-Profi nennt beides ausdrücklich keine Sperre.
- Die Fachnamen „Potenzgesetze“ und „Gesetz der großen Zahlen“ bleiben.
- Wachstum: Die Gerade ist blau, die Kurve in Tinte, damit „+2“ und „·2“ unterscheidbar sind.

## 2026-11-26 09:57 (Berlin) – NACHTRAG vom Projektleiter (vom Nutzer bestätigt): Hin und zurück zwischen Erklärung und Regel-Universum
Gehört zu Teil 2 des Auftrags darunter, betrifft auch den Übungsbildschirm aus Teil 1.
- In der Anfangs-Erklärung eines Themas, im Lösungsweg und in der Rückmeldung nach einem Fehler steht an passender Stelle ein kleines Feld „Regel dahinter“ mit dem Merksatz.
- Ein Tipp öffnet die Regel mit Zeichnung als Blatt über der Erklärung. Schließen oder Zurück führt an genau dieselbe Stelle; der Übungsstand bleibt erhalten.
- Vom Blatt führt ein zweiter Tipp ins ganze Regel-Universum; Zurück führt von dort wieder in die Erklärung.
- Umgekehrt: Im Regel-Universum steht bei jeder Regel, in welchen Themen sie vorkommt, mit Sprung in die jeweilige Erklärung.
- Das Feld erscheint nur bei echtem Zusammenhang (Zuordnung durch den Mathe-Profi, Auftrag 14 Teil A). Vorschlag des Projektleiters, nicht entschieden: höchstens zwei bis drei Regeln je Erklärung.
Bitte zeigen: das Feld in einer Erklärung, das offene Blatt, den Rückweg – bei 360 und 400 px.

## 2026-11-26 09:50 (Berlin) – AUFTRAG vom Projektleiter: (1) Übungsbildschirm, kurze Vorgabe – (2) Regel-Universum, dritte Runde
Der Nutzer hat gesagt: „Ja lege überall los“, und ausdrücklich an die Verbesserung der Darstellung erinnert. Zwei Teile. **Teil 1 zuerst, er ist kurz und der Bau wartet darauf.**

**Teil 1 – Übungsbildschirm am Handy (360 und 400 px), eine Seite Vorgabe und Bilder.** Grundlage: `inhalte/recherche/tief-11-bedienung-eltern.md`, Lieferung 2 und Lieferung 5 Punkte 1, 2, 7; Plan: `inhalte/plan/aufgabentypen-auswahl.md`, Abschnitt „Darstellung verbessern“. Gebraucht wird:
1. Aufgabe und Antwortfeld bleiben über der Tastatur sichtbar; Minus, Komma, Bruchstrich nur, wenn die Aufgabe sie braucht.
2. Kopf auf eine Zeile, eine einzige Fortschrittsleiste.
3. Rückmeldung als Blatt von unten: Symbol, Wort und Farbe zugleich; bei „nicht ganz“ eine Kurzregel.
4. **Neu, weil der neue Aufgabentyp kommt:** Eingabe mit zwei bis sechs Zahlenfeldern in einer Aufgabe (Beispiel: „Nenne drei verschiedene ganze Zahlen mit der Summe 0, genau eine positiv“). Welches Feld ist aktiv, wie springt man weiter, wie sieht es mit sechs Feldern auf 360 px aus? Nach einem Fehlversuch steht der Name der verletzten Bedingung und ein Hinweis da („Deine Summe ist 1.“); am Ende „Zum Beispiel: 5, −2, −3“. Format: `inhalte/plan/bedingung-format.md`.
5. Platz für den Schalter „am Tisch / nur am Handy“ beim Start einer Sitzung (einfache Form).
Zustände je Bild: leer, beim Tippen, Fehlversuch mit Hinweis, richtig, endgültig falsch mit „Zum Beispiel“. Hell und dunkel. Für den Älteren sachlich, ohne Sticker.

**Teil 2 – Regel-Universum, dritte Runde.** Oben in diesem Postfach stehen die Antworten des Mathe-Profis auf deine acht Fragen und seine Prüfung deiner sieben Zeichnungen (ein Maßfehler am umgelegten Kreis, vier kleine Punkte). Bitte:
- Name überall „Regel-Universum“; kein „Gesetzbuch“, kein „Gesetz“.
- Die neuen zweizeiligen Merksätze aus `inhalte/mathe-profi/regeln-uebersicht/ebene1.md` (Merksatz oben, „Genau gesagt“ darunter); Rechenregel 10 mit drei kurzen Sprüchen.
- Die fehlenden Zeichnungen: 16 der ersten 23 Vorgaben und die 19 neuen aus `zeichen-vorgaben-fuenf-planeten.md`. Keine Stelle mehr mit „Zeichnung folgt“ in dem, was der Nutzer sieht. Reihenfolge: Sonne, Fläche und Raum, Geometrie vollständig; danach die übrigen fünf Planeten.
- Die Übersicht muss zeigen, dass dieselbe Regel über viele Klassen gilt und worauf sie aufbaut. Das ist der Hauptwunsch des Nutzers.

Bitte melden mit: Geliefert / Offen / Nicht geprüft / Annahmen. Der Nutzer sieht das Ergebnis erst, wenn der Mathe-Profi die Zeichnungen fachlich und ChatGPT das Ganze gegengelesen hat.

## 2026-11-26 09:45 (Berlin) – FERTIG: Gesetzbuch, zweite Runde (Vorgabe GB, Abschnitt F3)

Zweig `designer`, Stand `lernen-app` 9b3f7d1 übernommen. Inhalt wörtlich aus `origin/mathe-profi` 9e0bedf (Aufträge 11 und 12). Kein App-Code, keine Datenbank, kein Lernstand, keine Namen.

**Geliefert** (alles unter `inhalte/design/gesetzbuch/`)
1. **Inhalt neu eingelesen.** Auf jeder Karte der Merksatz groß, „Genau gesagt:“ klein darunter – alle 42 Sätze, in beiden Übersichten, im aufgeschlagenen Gesetz, auf der Ideen-Seite.
2. **Alle 23 Zeichnungen** nach den Zeichen-Vorgaben: 14 Rechenregeln, 5 Ideen Geometrie, 4 Ideen Fläche und Raum. Neu gezeichnet: Regeln 1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14 und Geometrie 1 bis 5. Nach Auftrag 12 neu gefasst: Regel 2 (Figur am Start, je Minus eine Kehrtwende) und „Haut des Körpers“ (drei Bilder: Quader, halb aufgeklappt, Netz). Regel 8 hebt die Klammer mit den drei Zweien hervor; Geometrie 2 hat den Kreis als Hauptzeichnung. In Sonne und diesen zwei Planeten gibt es kein „Zeichnung folgt“ mehr (geprüft für 14 Regeln, 49 Gesetze, 9 Ideen).
3. **Die fünf übrigen Planeten** zeigen ihre tragenden Ideen als Karten ohne Zeichnungs-Rahmen.
4. `umsetzung.md`, neuer Abschnitt **F3** oben: Aufbau jeder neuen Zeichnung, zweite und dritte Markierung (Blau mit Rahmen, Schraffur), Annahmen zu den acht Fragen. 26 Bilder in `bilder/`. Entwürfe: `entwurf/zeichnungen.html` (alle 23), `uebersicht-a.html`, `uebersicht-b.html`, `gesetz.html`.

**Annahmen, weil die Antworten des Mathe-Profis (Auftrag 13) noch nicht auf seinem Zweig liegen**
- Wirkstelle in den Klassen-Beispielen nur bei den Regeln 2, 6 und 13 markiert; bei den anderen elf stehen die Beispiele ohne Markierung.
- Doppelter Name „Zahlen“ bleibt; die Schicht heißt in der Anzeige „Schicht 1 · Zahlen“.
- Mantel und Oberfläche gelten als auffindbar über seine Stichwörter.
- Regel 2: Ein und dieselbe Markierung (Gelb mit Rahmen) für jedes Minus und jede Kehrtwende, nicht je Minus eine eigene Farbe.
- Regel 7: Das zweite Paar ist blau umrahmt statt in einer zweiten Leuchtfarbe.
- Halb aufgeklappter Quader: Die Vorderwand liegt schon flach, Seitenwände und Rückwand stehen schräg, der Deckel hängt an der Rückwand. Die Vorgabe sagt nur „Deckel und Seitenwände stehen schräg ab“.

**Offen**
- Die Varianten „gleiche Zeichnung, andere Beschriftung“ sind nur bei Regel 6 gebaut.
- „Genau gesagt“ macht die Übersicht am Handy lang. Meine Meinung: auf der Übersicht weglassen, nur im aufgeschlagenen Gesetz zeigen. Entscheidung beim Nutzer.
- Regel 10: drei kurze Sprüche statt eines langen kommen erst mit der nächsten Lieferung des Mathe-Profis.
- Die Abschnitte 1, 2, 5, 9, 11 der `umsetzung.md` beschreiben in Einzelheiten noch Fassung 1; es gelten F3 und F2.

**Nicht geprüft**
- Fachliche Richtigkeit der 23 Zeichnungen durch den Mathe-Profi (Auftrag 13, Punkt 2). Selbst konstruiert und nur von mir nachgerechnet: Winkel 50°/60°/70°, Strahlensatz-Figur, Quadrat über der Hypotenuse, Drehung um 90°, Kreis-Umlegung, Schrägbilder.
- Ob ein Erwachsener ohne Vorwissen die Seite in einer Minute versteht.
- Echte Geräte, Safari, Firefox, Kontrastwerte. Gemessen nur in Chrome bei 360, 400, 820, 1280 px, hell und dunkel: 152 Seitenaufrufe, kein Querrollen, keine Schrift unter 13 px, keine Skriptfehler.

## 2026-11-26 09:40 (Berlin) – ENTSCHEIDUNG des Nutzers: Der Name ist „Regel-Universum“
Ersetzt den Arbeitsnamen „Mathe-Regeln“ aus dem Hinweis darunter. Titelzeile, Brotkrumen und Suchfeld: „Regel-Universum“. Die einzelnen Einträge heißen weiter „Regel“ (Sonne: „Rechenregel“; Planeten: „Idee“, dahinter „Regel“ oder „Formel“). „Gesetzbuch“ und „Gesetz“ kommen nirgends mehr vor.

## 2026-11-26 09:35 (Berlin) – HINWEIS vom Projektleiter an beide: Der Name „Gesetzbuch“ entfällt
Der Nutzer: Das Wort „Gesetzbuch“ war nur ein Bild zur Verdeutlichung und soll **nicht** der Name werden. Bitte in allem, was ein Kind oder der Nutzer sieht, nicht mehr verwenden – auch nicht „Gesetz“ als Bezeichnung der einzelnen Einträge. Arbeitsname bis zu seiner Entscheidung: **„Mathe-Regeln“**; ein Eintrag heißt **„Regel“** (in der Sonne „Rechenregel“, auf den Planeten „Idee“ und dahinter „Regel“ oder „Formel“). Titelzeile, Brotkrumen, Suchfeld, Zählungen („19 Gesetze“) entsprechend. Datei- und Ordnernamen dürfen bleiben, damit nichts bricht. Ein Namensvorschlag je Chat ist willkommen (ein Wort oder zwei, passend zu Sonne und Planeten).

## 2026-11-26 09:37 (Berlin) – VOM MATHE-PROFI an den Designer: Antworten auf deine acht Fragen, Prüfung der sieben Zeichnungen, 19 neue Zeichen-Vorgaben (Auftrag 13)

Stand `origin/mathe-profi`. Geprüft habe ich `bilder/zeichnungen-1280-hell.jpg` (in sieben Ausschnitten in voller Auflösung gelesen und nachgemessen) und die Bauzeilen in `entwurf/teile/zeichnen.js` für Waage und Kreis. Die übrigen Bilder und Breiten habe ich nicht geprüft.

### A. Deine acht Fragen (Abschnitt 11)

1. **Zahlen-Feld der Rechteck-Zeichnung: Plus.** Hauptfeld ist 6 · (20 + 2); dann sind Zahlen, x und Brüche bis auf die Beschriftung dieselbe Zeichnung. Das Minus-Feld bleibt als **viertes** Feld („auch bei Minus“), weil Klasse 5 genau so im Kopf rechnet (6 · 98). Reihenfolge: Zahlen mit Plus, mit x, mit Brüchen, Zahlen mit Minus. Im Minus-Feld bitte die Werte „108“ und „12“ in die Flächen schreiben statt der Terme.
   **Zu „maßstäblich oder dieselbe Form“:** maßstäblich bleibt. Ich ändere stattdessen die Zahlen des Bruch-Feldes, damit die Gestalt passt: **3/2 · (4 + ½) = 6 + ¾** (Höhe 1,5, Breite 4,5; Felder „6“ und „¾“). Der flache Streifen ½ · (4 + ⅔) entfällt.
2. **Zahlengerade, Lesart:** Es gibt nur **eine** Regel, nicht zwei Rollen: Die Figur blickt am Start nach rechts, und **jedes Minuszeichen ist eine Kehrtwende** – gleich, ob Rechenzeichen oder Vorzeichen. Das trägt alle vier Fälle: 3 + (+2) keine Kehrtwende, nach rechts auf 5; 3 − (+2) eine, nach links auf 1; 3 + (−2) eine, nach links auf 1; 3 − (−2) zwei, nach rechts auf 5. Folge für die Markierung: **nur die Minuszeichen** umrahmen, das Plus nicht.
3. **Zuordnung Gesetz → Idee:** Es gilt `ebene1.md`. F2 Rechteck gehört zu Idee 1 „Auslegen und zählen“.
4. **Trennzeichen:** erledigt. Jedes Beispiel ist eine eigene Tabellenzeile; auch der „mögliche Erklärweg“ und die Schichten der Sonne trennen jetzt mit Komma.
5. **Mantel und Oberfläche:** eigene auffindbare Einträge, ja. `inhalt.md` hat einen neuen Abschnitt „Formeln einzeln – Fläche und Raum“: 28 Formeln (Formel, Bedingung, Gesetz), darunter „Kegel – Mantel (Kegelmantel)“ und „Pyramide – Mantel (Pyramidenmantel)“. Sie sind Treffer der Suche und führen zu ihrem Gesetz; als Gesetze zählen sie nicht. Für die anderen Planeten folgt die Liste mit der Ausarbeitung.
6. **Zweimal „Zahlen“:** Schicht 1 der Sonne heißt jetzt **„Grundrechnen“**.
7. **Wirkstelle je Regel:** festgelegt, steht in `sonne.md` je Regel unter „Wirkstelle“. Kurz: 1 die rückenden Ziffern · 2 jedes Minuszeichen · 3 die Vorzeichen der beiden Zahlen und des Ergebnisses · 4 der Teil, der zuerst gerechnet wird · 5 Rechenzeichen samt Zahl, beim Zusammenfassen der gleiche Buchstabenteil · 6 der Faktor vor der Klammer · 7 das Minus vor der Klammer und jedes wechselnde Vorzeichen · 8 Hochzahl und gleich viele Faktoren · 9 der gemeinsame Faktor · 10 gemeinsamer Nenner, Zähler mit Zähler, Kehrwert · 11 der Wert für eins · 12 Rechnung und Gegenrechnung als Paar · 13 was auf beiden Seiten getan wird · 14 die Null und der Faktor, der null wird. (Hier ist „·“ Trenner einer Aufzählung, nicht in einer Rechnung.) Dein Vorschlag für 13 gilt; bei 2 bitte nach Antwort 2 ändern.
8. **Geometrie:** Was genau zu sehen ist, steht je Idee in `planet-geometrie.md` unter „Zeichen-Vorgabe“. „Gleicher Abstand“ ist, wie du wünschst, in Hauptfeld (Kreis) und zwei Nebenfelder geteilt.

**Zu F2.4, Punkt 4:** Ja – jede der 28 Ideen und jede der 14 Regeln bekommt genau **eine Hauptzeichnung**. Nebenzeichnungen stehen in der Zeile „Gleiche Zeichnung, andere Beschriftung“ und sind für die Übersicht kein Muss. Höchstens vier Felder je Reihe ist eingehalten.

**Neu durch Entscheidung des Projektleiters:** Rechenregel 10 hat **drei kurze Merksätze** statt eines langen (Plus und Minus · Mal · Geteilt) und dazu zwei Nebenfelder (Vorgabe in `sonne.md`).

### B. Fachliche Prüfung deiner sieben Zeichnungen

**Ergebnis: kein Rechenfehler, keine falsche Beschriftung. Ein Maßfehler, vier kleine Punkte.**

| Zeichnung | Befund |
|---|---|
| Regel 6, vier Felder | richtig: 6 · 22 mit 120 und 12; 6 · 20 − 6 · 2; 3x und 6 (Höhe 3 passt zur Breite 2); ½ · 4 = 2 und ½ · ⅔ = ⅓. Maßstab in allen vier nachgemessen. Änderungen nur nach Antwort 1. |
| Regel 13, Waage | richtig: 2 Säckchen + 2 Kugeln gegen 12; 2 Säckchen gegen 10; 1 Säckchen gegen 5. Balken waagerecht. |
| Regel 2, Zahlengerade | richtig: 3 → 1 und 3 → 5, beide Bögen zwei Einheiten. **Klein:** Das gepunktete Lot läuft durch die Rechnung „3 − (−2) = 5“ und streicht die „2)“ durch – Lot oberhalb der Rechnung enden lassen. Markierung nach Antwort 2. |
| Auslegen und zählen | richtig: 6 mal 4 Quadrate; Quader vorn 5 mal 3, Tiefe 4; 60 cm³. |
| Aus dem Rechteck, Hauptreihe | richtig: Rechteck, Parallelogramm, Dreieck je 6 cm und 4 cm (24, 24, 12 cm²); abgeschnittenes und angesetztes Dreieck gleich; Dreieck ist die Hälfte desselben Parallelogramms; Trapez 9 cm, 5 cm, 4 cm, zusammen mit dem gedrehten 14 cm breit, 28 cm². |
| Drachenviereck | richtig (8 cm, 5 cm, 20 cm²). **Klein:** Das Schild „20 cm²“ verdeckt ein Stück der unteren rechten Kante; die Figur wirkt dort offen. |
| Kreis | **Maßfehler:** Die Klammer „etwa π · r“ überspannt 13 halbe Stückbreiten (6½ Stücke, bei r = 3 cm rund 10,1 cm). Der halbe Umfang sind 6 Stücke (rund 9,4 cm). Berichtigung in `zeichnen.js`, Zeile mit `zKlammer(xa - sn, xa + 12 * sn, …)`: von `xa - sn / 2` bis `xa + 11.5 * sn` – also von der Mitte der linken Schräge bis zur Mitte der rechten. Höhe r und Formel stimmen. |
| Aus dem Quader | richtig: gleiche Höhen; Spitze von Pyramide und Kegel über der Mitte, Höhe senkrecht; Kugel berührt Deckel und Boden. **Klein:** am Kugel-Feld „h = 2 · r“ ergänzen, sonst sieht man nicht, warum der Zylinder „genau passt“. **Klein:** Der graue Satz „Die Spitze füllt ein Drittel des Körpers darum“ – besser „Pyramide und Kegel füllen je ein Drittel des Körpers darum.“ |
| Haut des Körpers | richtig: Schrägbild 5 cm, 4 cm, 3 cm (Tiefe halb, 45°); Netz faltbar, Flächen 20, 15, 12 je zweimal, 94 cm². Nach Auftrag 12 bitte ein drittes Bild in die Mitte: halb aufgeklappt. |

### C. Neu für dich
- `zeichen-vorgaben-fuenf-planeten.md`: 19 Zeichen-Vorgaben für die Ideen von Zahlen, Algebra, Geld und Verhältnisse, Funktionen, Daten und Zufall – gleiche sechs Zeilen, alle Zahlen nachgerechnet.
- `ebene1.md`: die 42 Sätze in der Form Merksatz + „Genau gesagt“ (Auftrag 12). Die Überschriften-Sätze in deinen Zeichnungen sind noch die alten.

## 2026-11-26 09:05 (Berlin) – RÜCKMELDUNG und AUFTRAG vom Projektleiter: Gesetzbuch, zweite Runde
Vorgabe GB gelesen und die Bilder angesehen (Zeichenstil, Übersicht A, Gesetz aufgeschlagen). Urteil des Projektleiters: Der Zeichenstil „Heft und Tafel“ trifft, was der Nutzer wollte – die Zeichnung zeigt die Regel, dieselbe Zeichnung trägt Zahlen, x und Brüche. Dein eigenes Urteil teile ich: als fertig zeigen wir es erst, wenn die Platzhalter weg sind. Die sechs Zeichnungen und die Gesetz-Seite zeige ich dem Nutzer als Zwischenstand.

Inzwischen neu auf `origin/mathe-profi`: Auftrag 11 (42 Sätze auf Ebene 1: 14 Rechenregeln, 28 tragende Ideen für alle sieben Planeten; 23 Zeichen-Vorgaben für die Sonne und die Planeten Fläche und Raum und Geometrie) und Auftrag 12 (jeder Satz zweizeilig: **Merksatz** oben, **„Genau gesagt“** klein darunter; vier Zeichen-Vorgaben geändert – steht oben in deinem Postfach auf seinem Zweig).

Bitte:
1. Inhalt neu einlesen (`ebene1.md`, `sonne.md`, beide Planeten). Auf jeder Karte der Merksatz groß, „Genau gesagt“ klein darunter.
2. Die fehlenden Zeichnungen nach seinen Vorgaben: 11 Rechenregeln, 5 Ideen Geometrie, Idee 4 Fläche und Raum. Keine Karte mit „Zeichnung folgt“ in Sonne und diesen zwei Planeten.
3. Die tragenden Ideen der übrigen fünf Planeten in die Übersicht aufnehmen (Sätze stehen in `ebene1.md`); dort sind Zeichnungen noch nicht verlangt – die Karten ohne leeren Zeichnungs-Rahmen setzen, bis die Vorgaben kommen.
4. Deine acht Fragen beantwortet der Mathe-Profi (Auftrag 13 in seinem Postfach); wo seine Antwort noch fehlt, triff eine Annahme und nenne sie.
Meldung hier. Danach liest ChatGPT gegen, dann geht es an den Nutzer.

## 2026-11-26 09:05 (Berlin) – FERTIG: Gesetzbuch, Fassung 2 nach den Zeichen-Vorgaben des Mathe-Profis (Vorgabe GB)

Zweig `designer`, Stand `lernen-app` d6752b7 übernommen. Inhalt wörtlich aus `origin/mathe-profi` dc6817d. Kein App-Code, keine Datenbank, kein Lernstand, keine Namen.

**Geliefert** (alles unter `inhalte/design/gesetzbuch/`)
- `umsetzung.md`, neuer Abschnitt **F2** oben: was sich geändert hat, Regeln für alle Zeichnungen, Maße jeder Zeichnung, Antworten an den Mathe-Profi.
- Die sechs Zeichnungen neu nach den Zeichen-Vorgaben: Ausmultiplizieren maßstäblich mit vier Beschriftungen (6 · (20 + 2), 6 · (20 − 2), 3 · (x + 2), ½ · (4 + ⅔)); Waage dreimal mit waagerechtem Balken; zwei Zahlengeraden untereinander, Starts bei 3 übereinander; Auslegen mit Rechteck und Würfel-Quader 5 · 4 · 3; Stammbaum Fläche mit Ästen Drachenviereck und Kreis; Stammbaum Körper mit Kugel im Zylinder. Zusätzlich eine siebte: Quader und Netz („Haut des Körpers“).
- Hervorhebung überall Gelb **mit Rahmen**, dieselbe Markierung in der Rechenzeile; jede Höhe mit Zeichen für den rechten Winkel.
- Beide Übersichten mit den 42 Sätzen aus `ebene1.md`: alle sieben Planeten zeigen ihre tragenden Ideen (28). Zuordnung Gesetz → Idee vom Mathe-Profi.
- Gesetz aufgeschlagen: Voraussetzung, häufiger Fehler, Verwandt, möglicher Erklärweg („keine Sperre“) aus den neuen Dateien. Suche mit den Stichwörtern des Mathe-Profis.
- `entwurf/inhalt_lesen.py` liest das neue Format; `bauen.py` prüft, dass markierte Beispiele wörtlich die des Mathe-Profis sind. 22 Bilder in `bilder/`.

**Antworten an den Mathe-Profi** (ausführlich in `umsetzung.md` F2.4; in seinen Zweig darf ich nicht schreiben)
1. Feste Grundform mit austauschbarer Beschriftung: ja, so gebaut. Aber „dieselbe Form“ und „maßstäblich“ schließen sich bei anderen Zahlen aus – ich habe maßstäblich gewählt. Bitte entscheiden.
2. Originalgröße geht am Bildschirm nicht. Ein Karo steht für 1 cm.
3. Am Handy ist alles lesbar, weil die Felder untereinander stehen. Bitte höchstens vier Felder je Reihe, Nebenzeichnungen als eigene Reihe; „Gleicher Abstand“ als drei getrennte Felder.
4. Vorgaben für die anderen fünf Planeten: später ist recht.

**Offen**
- Entscheidung des Nutzers: Trägt der Zeichenstil? Übersicht A oder B?
- 7 von 23 Zeichen-Vorgaben sind gezeichnet. Es fehlen 11 Rechenregeln und 5 Ideen der Geometrie; dort steht „Zeichnung folgt“ mit dem Text der Vorgabe.
- Auftrag 12 (Merksatz + „Genau gesagt“) ist noch nicht geliefert. Der Entwurf zeigt die zweite Zeile, sobald sie da ist; die Sätze ändern sich also noch.
- Einige Varianten aus den Vorgaben fehlen (Liste in F2.5). Die Abschnitte 1, 2, 5, 9, 11 der `umsetzung.md` beschreiben in Einzelheiten noch Fassung 1.

**Nicht geprüft**
- Ob ein Erwachsener ohne Vorwissen die Seite in einer Minute versteht – das kann nur der Nutzer sagen.
- Echte Geräte, Safari, Firefox. Gemessen nur in Chrome bei 360, 400, 820, 1280 px, hell und dunkel: 112 Seitenaufrufe, kein Querrollen, keine Schrift unter 13 px, keine Skriptfehler.
- Kontrastwerte nicht nachgerechnet. Mathematische Richtigkeit der Zeichnungen nicht vom Mathe-Profi gegengelesen (Kreis-Umlegung, Schrägbilder, Kugel im Zylinder sind von mir konstruiert).

**Annahmen**
- Trapez und Drachenviereck tragen die Zahlen aus den Beispielen F7 und F8, weil die Zeichen-Vorgabe keine nennt.
- Die grauen Sätze unter den Bildern sind von mir.
- Bei 3 · (x + 2) ist x viermal so lang wie 2 gezeichnet.

## 2026-11-26 08:54 (Berlin) – VOM MATHE-PROFI an den Designer: Merksätze neu (Auftrag 12) – vier Zeichen-Vorgaben geändert

Entscheidung des Nutzers: Jeder der 42 Sätze hat jetzt **zwei Zeilen** – oben groß der **Merksatz** zum Aufsagen (4 bis 14 Wörter), klein darunter **„Genau gesagt“**. Wortlaut: `ebene1.md` auf `origin/mathe-profi`. Auf der Übersicht steht der Merksatz; „Genau gesagt“ ist die kleine zweite Zeile oder erscheint beim aufgeschlagenen Gesetz.

**Geänderte Zeichen-Vorgaben** (in `sonne.md` und den Planeten-Dateien schon eingetragen)
1. **Rechenregel 2** (Merksatz „Minus heißt umdrehen – zweimal umdrehen ist wieder geradeaus“): Am Start bei 3 steht eine kleine Figur mit Blick nach rechts. Je Minuszeichen ein kleiner Kehrtwende-Bogen: oben einer (3 + (−2) = 1, sie geht nach links), unten zwei (3 − (−2) = 5, sie geht nach rechts). Hervorgehoben: jedes Minuszeichen und seine Kehrtwende in derselben Farbe.
2. **Rechenregel 8** (Merksatz „Hoch drei heißt: die Zahl dreimal hinschreiben und malnehmen“): Hervorgehoben ist jetzt zuerst die Klammer mit den drei Zweien samt Hochzahl 3; der Rest ist zweitrangig.
3. **Fläche und Raum, Idee 4** (Merksatz „Aufklappen zeigt die ganze Haut des Körpers“): drei Bilder statt zwei – Quader, halb aufgeklappt, Netz. Das mittlere Bild ist die Hauptsache.
4. **Geometrie, Idee 2** (Merksatz „Der Kreis: alle Punkte gleich weit von der Mitte“): Der Kreis ist die Hauptzeichnung; Mittelsenkrechte und Winkelhalbierende sind kleinere Nebenzeichnungen. Damit ist meine Frage 3 für diese Vorgabe erledigt.

**Unverändert passend:** Waage (13), Rechteck (6), Treppe (3), Streifen (9, 10), Rückweg in zwei Reihen (12), Stammbäume, Dreieck mit Quadraten.

## 2026-11-26 08:50 (Berlin) – FERTIG: Gesetzbuch der Mathematik – Zeichenstil, Übersicht, ein Gesetz aufgeschlagen (Vorgabe GB)

Zweig `designer`, ausgehend von `lernen-app` 01b103d. Kein App-Code, keine Datenbank, kein Lernstand, keine Namen. Mathe-Inhalt wörtlich aus `origin/mathe-profi` df14ade; der Designer hat keinen Mathe-Inhalt erfunden.

**Geliefert** (alles unter `inhalte/design/gesetzbuch/`)
- `umsetzung.md`: Vorgabe mit Zeichenstil, Maßen je Breite, Farben hell und dunkel, Texten, Verhalten, Prüfliste (14 Muss, 5 Soll, 3 Kann).
- `entwurf/zeichnungen.html`: Zeichenstil „Heft und Tafel“ an den sechs verlangten Zeichnungen (Ausmultiplizieren mit drei Beschriftungen, Waage, Zahlenstrahl, Auslegen und Zählen, Rechteck → Parallelogramm → Dreieck → Trapez, Quader → Prisma und Zylinder → Pyramide und Kegel).
- `entwurf/uebersicht-a.html`: Übersicht A „Schnitt von innen nach außen“ – die Sonne als vier Schichten mit allen 14 Merksätzen, darunter die sieben Planeten mit ihren tragenden Ideen, dann die acht Arbeitsweisen.
- `entwurf/uebersicht-b.html`: Übersicht B „Durch die Klassen“ – jede Regel als Zeile von Klasse 5 bis 10 mit ihrem Beispiel in jeder Klasse.
- `entwurf/gesetz.html`: ein Gesetz aufgeschlagen (Regel 6): Merksatz, Zeichnung, dieselbe Regel in sechs Klassen mit gelber Wirkstelle, wo es nicht gilt, Voraussetzung. Dazu der Weg Idee → Gesetze dahinter und die Suche über alle 174 Einträge („Kegelmantel“ → „Pyramide und Kegel“).
- `bilder/`: 20 Bilder bei 360, 400, 820, 1280 px, hell und dunkel. Quellen in `entwurf/teile/`; `inhalt_lesen.py` liest den Inhalt des Mathe-Profis, `bauen.py` setzt die Seiten zusammen.

**Empfehlung:** Übersicht A als Seite; die Tabelle aus B als zweite Ansicht am Rechner. Begründung in Abschnitt 3.3.

**Mein Urteil in einem Satz:** Ich halte Zeichenstil, Übersicht A und die Gesetz-Seite für gut, weil die Merksätze selbst groß dastehen, der Aufbau eine einzige Leserichtung hat und „dieselbe Regel in vielen Klassen“ an echten Rechnungen zu sehen ist – ich bin aber nicht einverstanden, es dem Nutzer als fertig zu zeigen, solange 11 von 14 Regeln und die fünf Geometrie-Ideen „Zeichnung folgt“ zeigen.

**Offen**
- Für die erste Lieferung fehlen noch: Zeichnungen zu den fünf Geometrie-Ideen und zu 11 Rechenregeln; tragende Ideen für fünf Planeten (Zahlen, Algebra, Geld und Verhältnisse, Funktionen, Daten und Zufall). Im Entwurf steht an diesen Stellen „folgt“.
- Entscheidung des Nutzers: A oder B.
- **An den Mathe-Profi – acht Fragen in Abschnitt 11 der Vorgabe**, die wichtigsten: (1) Zahlen-Feld der Zeichnung 1 mit Minus wie im Auftrag oder mit Plus, damit alle drei Felder gleich sind? (3) Zuordnung der Gesetze zu den Ideen bestätigen. (4) Zwei Beispiele je Klasse bitte als zwei Einträge, nicht mit „ · “ getrennt. (5) Mantel und Oberfläche als eigene Einträge, wenn die Suche Formeln finden soll. (6) Schicht 1 und Planet 1 heißen beide „Zahlen“. (7) Wirkstelle je Regel festlegen. (8) Was genau die fünf Geometrie-Zeichnungen zeigen müssen.

**Nicht geprüft**
- Der Maßstab „ein Erwachsener versteht es in einer Minute“: mit niemandem erprobt.
- Fachliche Richtigkeit der Zeichnungen durch den Mathe-Profi; seine genauen Vorgaben je Zeichnung lagen noch nicht vor.
- Echte Geräte, Finger, Safari und Firefox; Vorleser nur als Text gesetzt; Kontrast nicht gemessen.
- Gegenlesen durch ChatGPT.

**Geprüft:** alle vier Entwürfe in Chrome bei 360 × 640, 400 × 860, 820 × 1180, 1280 × 800, hell und dunkel: keine Skriptfehler, 14 Regeln und 7 Planeten auf beiden Übersichten, Klickfolgen durch Gesetz, Idee und Suche, sieben Suchwörter, nichts ragt seitlich hinaus, keine Tippfläche unter 44 px. Alle Zahlen in den Zeichnungen nachgerechnet.

**Annahmen**
- Welche Gesetze hinter welcher Idee stehen, habe ich zugeordnet (Fläche und Raum: 3 / 8 / 8; Geometrie nach den vier Abschnitten).
- Die fünf Geometrie-Sätze sind der Vorschlag des Projektleiters, formuliert mit den Sätzen der Gesetze G6, G10, G15, G20, G24.
- Der Inhalt wird als feste Datei mit der App ausgeliefert; dann braucht die Seite keinen Ladezustand.
- Die Vorgabe RS-H ist als abgelehnt gekennzeichnet; ihre Dateien bleiben nur zum Nachlesen im Zweig `designer`.

## 2026-11-26 08:40 (Berlin) – VOM MATHE-PROFI an den Designer: Zeichen-Vorgaben liegen bereit (Auftrag 11) – mit vier Fragen

Alles auf `origin/mathe-profi` unter `inhalte/mathe-profi/regeln-uebersicht/`. Die Abschnitte „Bild“ der ersten Fassung gelten nicht mehr.

**Wo was steht**
- `ebene1.md`: alle 42 Sätze der Ebene 1 im Wortlaut – 14 Rechenregeln und 28 tragende Ideen (Zahlen 5, Algebra 4, Geld und Verhältnisse 3, Geometrie 5, Fläche und Raum 4, Funktionen 3, Daten und Zufall 4). Das ist der Text für deine Übersicht.
- `sonne.md`: je Rechenregel ein Abschnitt „Zeichen-Vorgabe“ (14 Stück).
- `planet-flaeche-und-raum.md` (4 Ideen) und `planet-geometrie.md` (5 Ideen): je Idee eine „Zeichen-Vorgabe“, darunter die Gesetze der Idee mit Voraussetzung, häufigem Fehler und Beispielen – der Stoff für „ein Gesetz aufgeschlagen“.
- `inhalt.md`: Ebene 2 mit Stichwörtern für die Suche („Kegelmantel“ führt zu F17, „Minus vor der Klammer“ zu Rechenregel 7).

**Jede Zeichen-Vorgabe hat sechs Zeilen:** Zu sehen · Maße · Beschriftung · Hervorgehoben · Darf nicht falsch aussehen · Gleiche Zeichnung, andere Beschriftung.

**Zu deinen sechs Stil-Zeichnungen – Abweichungen vom Auftragstext des Projektleiters**
- Ausmultiplizieren: Grundfassung ist 6 · (20 + 2), maßstäblich, Trennstrich bei 20. Die Minus-Fassung 6 · (20 − 2) ist dasselbe Rechteck mit gestrichelt abgetrenntem Stück. Dazu 3 · (x + 2) und ½ · (4 + ⅔). Vier Beschriftungen, eine Zeichnung.
- Zahlenstrahl: zwei Geraden untereinander, beide Starts genau übereinander bei 3; beide Pfeile genau zwei Einheiten lang.
- Waage: drei Bilder nebeneinander (2x + 2 = 12, 2x = 10, x = 5), Balken immer waagerecht.
- „Auslegen und zählen“: neben dem Rechteck 6 cm mal 4 cm gehört der Quader 5 · 4 · 3 aus Würfeln dazu.
- Stammbaum Fläche: zusätzlich ein Ast Drachenviereck und ein Ast Kreis (Tortenstücke). Rechteck, Parallelogramm und Dreieck haben dieselbe Grundseite 6 cm und Höhe 4 cm.
- Stammbaum Körper: zusätzlich die Kugel im passenden Zylinder.

**Was für alle Zeichnungen gilt**
1. Maßstäblich. Alle Zahlen in den Vorgaben sind nachgerechnet; bitte keine anderen Zahlen einsetzen, ohne mich zu fragen.
2. Die hervorgehobene Stelle hat in Zeichnung und Rechenzeile dieselbe Farbe – und zusätzlich ein Zeichen, das ohne Farbe trägt (Strich-Zeichen, Rahmen, Strichart).
3. Eine Aussage je Zeile. Der Punkt „·“ ist in diesem Buch immer ein Malzeichen, nie ein Trenner.
4. Höhen immer mit dem Zeichen für den rechten Winkel.

**Fragen an dich**
1. Kannst du eine Zeichnung als feste Grundform mit austauschbarer Beschriftung führen (Rechteck mit vier Beschriftungen, Dreieck 3–4–5 mit zwei)? Das ist der Kern von „dieselbe Regel in vielen Klassen“.
2. „Originalgröße 6 cm mal 4 cm“ geht am Handy vermutlich nicht. Dann bitte Kästchen ohne den Anspruch auf echte Zentimeter – sag mir, was du nimmst, ich passe den Text an.
3. Welche Vorgabe ist am Handy nicht lesbar zu zeichnen? Ich vermute: Stammbaum Fläche (sechs Figuren) und „Gleicher Abstand“ (drei Felder). Ich teile sie dann in eine Hauptzeichnung und Nebenzeichnungen.
4. Die Zeichen-Vorgaben für die Ideen der übrigen fünf Planeten schreibe ich, sobald dein Stil steht – einverstanden, oder brauchst du sie vorher?

Antworten bitte hier oben; ich lese mit.

## 2026-11-26 08:40 (Berlin) – AUFTRAG vom Projektleiter: Gesetzbuch der Mathematik – Zeichnungen und Übersicht (jetzt, gleichzeitig mit dem Mathe-Profi)
Der Nutzer will dich ausdrücklich dabeihaben und erwartet echte Zeichnungen. Bitte lies `inhalte/plan/regeln-uebersicht-auftrag.md` ganz; **der letzte Abschnitt ist maßgeblich** (zwei Ebenen). Die frühere Vorgabe RS-H ist abgelehnt.

**Die Idee:** Ein „Gesetzbuch“ neben der Lernreise – in der Mitte die Sonne mit 14 Rechenregeln, darum sieben Planeten (die Gebiete der App), je Planet 3 bis 5 tragende Ideen; dahinter zum Nachschlagen die einzelnen Formeln.

**Abgelehnt wurde:** Etiketten statt Inhalt, erfundene Namen, Lernstand im Mittelpunkt, Seiten, die man erst durch Antippen versteht. **Gewünscht ist:** übersichtlich der gesamte Aufbau; sichtbar, dass dieselbe Regel in vielen Klassen gilt; sehr anschaulich; aufeinander aufbauend; einprägsame Bilder.

**Deine Aufgabe**
1. **Zeichenstil festlegen** und an sechs Zeichnungen zeigen – jede zeigt die Idee, keine schmückt:
   - Ausmultiplizieren: ein zerlegtes Rechteck – dieselbe Zeichnung beschriftet mit 6 · (20 − 2), mit 3 · (x + 2) und mit Brüchen.
   - Gleichung als Waage.
   - Plus und Minus mit negativen Zahlen am Zahlenstrahl (zweimal von 3 aus: 3 + (−2) = 1 und 3 − (−2) = 5).
   - „Messen heißt auslegen und zählen“: Rechteck 6 cm mal 4 cm mit Einheitsquadraten.
   - „Aus dem Rechteck entsteht jede Fläche“: Stammbaum Rechteck → Parallelogramm → Dreieck → Trapez.
   - „Aus dem Quader entsteht jeder Körper“: Quader → Prisma und Zylinder → Pyramide und Kegel.
   Genaue Vorgaben je Zeichnung liefert der Mathe-Profi; bis dahin gelten die Abschnitte „Bild“ in `sonne.md` und `planet-flaeche-und-raum.md` auf `origin/mathe-profi`.
2. **Die Übersicht (Ebene 1)** in zwei Fassungen: Sonne und sieben Planeten, auf denen die Merksätze selbst lesbar stehen. Ein Erwachsener ohne Vorwissen muss nach einer Minute sagen können, was die Seite ihm sagt. Rechner und Handy; ohne Antippen verständlich.
3. **Ein Gesetz aufgeschlagen:** Merksatz, Zeichnung, dieselbe Regel in mehreren Klassen mit gleich hervorgehobener Wirkstelle, Voraussetzung, häufiger Fehler. Dazu der Weg von einer tragenden Idee zu den Formeln dahinter und eine Suche (z. B. „Kegelmantel“).
4. Kein Lernstand, keine Monde, keine Prozentbalken in dieser Fassung.

**Abstimmung:** Der Mathe-Profi arbeitet gleichzeitig (Auftrag 11) und schreibt Fragen und Antworten an dich hier oben hinein. Erste gemeinsame Lieferung: Sonne und zwei Planeten (Fläche und Raum, Geometrie). Ablage `inhalte/design/gesetzbuch/`, Meldung hier mit „Nicht geprüft“ und „Annahmen“.

## 2026-11-26 05:40 (Berlin) – RÜCKMELDUNG und neuer AUFTRAG vom Projektleiter: Regel-Übersicht
Der Nutzer hat die Vorgabe RS-H abgelehnt („Katastrophal. Verstehe nicht einmal ich, was ihr mir sagen wollt“) und ebenso meinen eigenen Gegenentwurf. Die Ursache liegt vor allem im Inhalt, den ich dir gegeben habe (erfundene Namen, Lernstand im Mittelpunkt), nicht in deinem Handwerk. Der gemeinsame Auftrag steht in `inhalte/plan/regeln-uebersicht-auftrag.md` – bitte ganz lesen. **Du bist erst in Schritt 4 dran**, wenn Mathe-Profi und ChatGPT den Inhalt abgestimmt haben; ich melde mich dann hier. Bis dahin nichts bauen. Wenn du vorab Bedenken oder Ideen zur Darstellung „dieselbe Regel in vielen Klassen, aufeinander aufbauend“ hast: kurz hier notieren.

## 2026-11-26 04:30 (Berlin) – FERTIG: Regel-Übersicht „Sonnensystem“ und Regel-Karte (Vorgabe RS-H)

Zweig `designer`, ausgehend von `lernen-app` 9c2d316. Kein App-Code, keine Datenbank, keine Namen, alle Zustände und Orte in den Entwürfen erfunden und so gekennzeichnet.

**Geliefert** (alles unter `inhalte/design/regeln-sonnensystem/`)
- `umsetzung.md`: Vorgabe mit Maßen je Breite, Farben hell und dunkel, Texten wörtlich, Antippen, Laden, Fehler, Bewegung mit „weniger Bewegung“, Daten-Bedarf, Prüfliste (15 Muss, 7 Soll, 4 Kann).
- `entwurf/uebersicht-a.html` – Fassung A „Sonnensystem“: Sonne am Rand, Bahnen, Planeten mit einem Mond je Regel, Werkzeug-Gürtel außen.
- `entwurf/uebersicht-b.html` – Fassung B „Planetenreihe“: Sonne und Planeten an einer Linie, alle Regel-Namen sofort lesbar.
- `entwurf/regel-karte.html` – Karten „Verteilen“ und „Minusklammer“ ganz: Satz, Bild, drei Gewänder, Grenze, Probe zum Antippen, Orte, Hauptknopf.
- `entwurf/wege.html` – die drei Wege (Reisekarte nach oben, nach einem Fehler, neues Thema).
- `bilder/`: 25 Bilder bei 360, 400, 820, 1280 px, hell und dunkel. Quellen der Entwürfe in `entwurf/teile/`, zusammengesetzt mit `entwurf/bauen.py`.
- Bildmotiv für alle 15 Regeln (Abschnitt 6.4).

**Empfehlung:** Fassung A als Seite; die Liste aus B steckt in A hinter der Sonne. Begründung in Abschnitt 1.

**Vorschläge zu den offenen Entscheidungen des Nutzers** (Abschnitt 2)
- Schnitt: fünf Regel-Planeten wie vorgeschlagen, dazu die Erde; die Werkzeuge als „Werkzeug-Gürtel“ statt als sechster Planet.
- Sonne: öffnet die Liste aller 15; darunter freiwillig „Gemischte Fünf“.
- Stand: Kinder sehen ihn, in zwei Zuständen („sitzt“, „in Arbeit“) plus neutral „kommt später“; als Mond-Form, ohne Zahl und Balken.

**Offen**
- Entscheidung des Nutzers: A oder B, und die drei Punkte oben.
- An den Mathe-Profi: (1) „Potenz“ im Planeten „Bruch“ lassen oder zu „Verhältnis“? (2) Ist „kommt später“ als drittes Zeichen in Ordnung? (3) Bitte prüfen: umgestellte Beispiel-Zeilen der Regeln 4 und 5 (gleiche Zahlen, gleicher Aufbau in allen drei Zeilen), Sätze der fünf Arbeitsweisen, Planeten-Sätze, die 15 Sätze „Hier hat … geklemmt“.
- Karten für die übrigen 13 Regeln: Aufbau steht, Inhalte und Bilder fehlen.
- Abschnitt 10 nennt, was der Server neu liefern müsste (Zustand je Regel, Regel zum Fehler, Zwillingszeilen zur Etappe). Das gibt es heute nicht.

**Nicht geprüft**
- Echte Geräte, Finger, Safari und Firefox; Vorleser nur als Text gesetzt.
- Bewegung nur im Code festgelegt, nicht als Film angesehen; Rechenlast auf alten Geräten nicht gemessen.
- Platz des Knopfs „Regeln“ auf der echten Reisekarte (im Entwurf ein Platzhalter).
- Kontrast für Text gerechnet (ab 6,2 : 1), nicht am Bildschirm gemessen.

**Geprüft:** alle vier Entwürfe in Chrome bei 360 × 640, 400 × 860, 820 × 1180, 1280 × 800, hell und dunkel: keine Skriptfehler, Klickfolgen durch alle Blätter und Wege, kein Ziel unter 44 px, keine Rechnung läuft über den Rand.

**Annahmen**
- Drei Aufgaben je Regel und die Gemischte Fünf lassen sich mit vorhandenen Aufgabenformen bauen.
- Die Orte in „Diese Regel brauchst du in …“ kommen aus den Regel-Etiketten des Mathe-Profis.
- Kürzel RS-H gewählt, weil „RS“ im Repo schon belegt ist.

## 2026-11-26 02:40 (Berlin) – AUFTRAG vom Projektleiter: Regel-Übersicht „Sonnensystem“ und Regel-Karte

**Wunsch des Nutzers, wörtlich im Kern:** „Wichtig ist mir eine tolle Übersichtsseite für die Regeln. Schön und übersichtlich, nicht einfach hingeklatscht.“ Die Idee des Sonnensystems stammt von ihm. Kein Bau, keine Einspielung – du lieferst Entwurf und Vorgabe.

**Worum es geht**
Über allen Themen stehen wenige Grundregeln, die immer wiederkehren („immer dasselbe, nur anders dargestellt“; Klasse 5 rechnet mit Zahlen, Klasse 8 mit x – dieselbe Regel). Die Kinder sollen diese Regeln jederzeit ansehen können und spüren: Es sind 15 Dinge, nicht 300 Themen.

**Bildsprache**
Die Reisewelt (Flug, Bordkarte, Stadt, Reisekarte) bleibt. Das Sonnensystem ist keine zweite Welt daneben, sondern der Blick nach oben: Die Reisewelt ist die Erde, die Regeln stehen am Himmel. Diese Erweiterung hat der Nutzer selbst gewollt; sie hebt den Satz „keine zweite Bildsprache erfinden“ für diesen Fall auf. Der Übergang Erde ↔ Himmel ist Teil deiner Aufgabe.

**Inhalt, fachlich vorgegeben** (Quelle: `inhalte/mathe-profi/denkpapier-grundregeln.md` auf `origin/mathe-profi`, Abschnitte 1, 2 und 5 – bitte lesen)
- 15 Regeln mit Namen für Kinder, je ein Satz, die Grenze („gilt nicht bei …“), Beispiel mit Zahlen, mit x, mit Brüchen.
- Vorschlag des Projektleiters für die Gruppen (der Nutzer hat ihn gesehen, aber noch nicht bestätigt):
  - Sonne: Übersicht, „15 Regeln“
  - Erde: die Reisewelt
  - Vorzeichen: Richtung, Zeichen-Paar
  - Klammer: Rangfolge, Verteilen, Minusklammer, Tauschen und Bündeln
  - Waage: Waage, Umkehren, Einsetzen und Probe, Nullprodukt
  - Bruch: Wert bleibt, Bruchrechnen, Potenz
  - Verhältnis: Stellenwert, Verhältnis
  - Werkzeuge (Arbeitsweisen, ohne richtig/falsch): Skizze, Überschlag, Einheiten prüfen, Zerlegen und Ergänzen, Darstellung wechseln
- Regeln des Mathe-Profis für die Anzeige: höchstens zwei Zustände je Regel („sitzt“ / „in Arbeit“), **keine Prozentbalken**, kein dauernd sichtbares „wackelt“ (Beschämung), Zustand nie nur über Farbe.

**Was du lieferst**
1. **Übersichtsseite** in zwei deutlich verschiedenen Fassungen zum Anklicken (je eine HTML-Datei): eine mit echtem Sonnensystem-Gefühl (Bahnen, Tiefe, Bewegung sparsam), eine ruhigere, die am Handy auf einen Blick lesbar ist. Sag, welche du empfiehlst und warum.
2. **Regel-Karte** am Beispiel „Verteilen“ (Regel 4) und „Minusklammer“ (Regel 5): Satz, Bild, dieselbe Regel mit Zahlen / mit x / mit Brüchen, die Grenze, die Probe, „Diese Regel brauchst du in …“, Einstieg zu drei Aufgaben. Das Bild je Regel ist wichtig (bei Verteilen das Rechteck) – schlage für alle 15 Regeln ein Bildmotiv in je einer Zeile vor.
3. **Die drei Wege zur Regel:** (a) von der Reisekarte nach oben, (b) nach einem Fehler in einer Aufgabe der Satz „Hier hat die Minusklammer geklemmt“ mit Sprung zur Karte und zurück zur Aufgabe, (c) beim Einstieg in ein neues Thema „Das kennst du schon“.
4. Vorgabe so genau, dass ein Bau-Helfer sie ohne Rückfrage umsetzt: Maße, Farben hell und dunkel, Texte wörtlich, Verhalten bei 360 / 400 / 820 / 1280 px, Antippen, Laden, Fehler, Bewegung mit „weniger Bewegung“-Fassung. Dazu die Prüfliste (Muss / Soll / Kann).

**Als Inhalts-Skizze, nicht als Aussehen:** Der Projektleiter hat dem Nutzer einen schnellen Rohentwurf gezeigt (dunkler Grund, Sonne oben, sechs Planeten als Karten, Regel-Karte „Verteilen“). Der Nutzer will es schöner. Nimm daraus nur, was inhaltlich auf die Seiten gehört.

**Offene Entscheidungen des Nutzers – bitte je einen Vorschlag mitliefern**
- Schnitt der Planeten: sechs wie oben oder anders.
- Ob in der Sonne etwas zu tun ist (z. B. „gemischte Fünf“ quer über alle Regeln).
- Ob die Kinder den Stand je Regel sehen oder nur der Erwachsene.

**Regeln wie immer:** Zweig `designer`, vorher auf `origin/lernen-app` bringen. Öffentliches Repo: keine Namen, keine Lerndaten. Beispiel-Zustände in den Entwürfen sind erfunden und als erfunden gekennzeichnet. Ablage `inhalte/design/regeln-sonnensystem/`, Meldung hier mit „Nicht geprüft“ und „Annahmen“.

## 2026-11-25 02:00 – FERTIG: Bestandsaufnahme

Zweig `designer`, ausgehend von `lernen-app` 4351182 (App 0.93.4). Vorgaben gelesen auf `pruefung-kinderansicht` ab6a9fb. Kein App-Code, keine Datenbank, keine Namen, nichts Neues entworfen.

**Geliefert**
- `inhalte/design/bestandsaufnahme.md`: Stand der Vorgaben, eigene Befunde mit Messwerten, drei Vorschläge.
- `inhalte/design/bestandsaufnahme/bilder/`: 15 Bilder aus einem eigenen Rundgang (als Kind angemeldet, Testdaten der Suite; 400, 820, 1280 px, hell und dunkel; Übung zusätzlich 390 × 664).
- Kern:
  - Alle Vorgaben des Vorgängers sind gebaut, außer FX (nichts im Code) und den Kann-Punkten K1, K3, K5, K8 der Prüfung KJ.
  - Übung: Bei 390 × 664 und 360 × 640 px ist beim Öffnen keine Aufgabe zu sehen (Bordkarte ab 386 px, Tastenfeld ab 385 bzw. 361 px). Bei 400 × 860 sind die Antwortfelder im unteren Drittel und „Tipp“ ganz verdeckt. Bei 1280 × 800 liegt „Prüfen“ unter dem Fensterrand.
  - Nachts wird die Etappen-Kachel unter dem Zeiger hell mit weißer Schrift; der Chip „Expedition wartet“ bleibt hell. Tablet: Schrift im Landungs-Blatt 11–14 px.
- Vorschlag nach Wirkung je Aufwand: 1. Übungs-Bildschirm „Aufgabe zuerst“ · 2. Aufräum-Paket Lesbarkeit · 3. FX erste Stufe (Motor, Legendary Drop, Respawn, Dezember-Saison).

**Offen**
- Entscheidung des Nutzers, was ich zuerst entwerfe.
- FX: Freigabe („warten“ vom 24.11.); Server-Felder für „Etappe sicher“ und „wieder offen“; Prüfliste ohne Muss / Soll / Kann.
- Im Auftrag steht FX „Fassung 2“, im Repo liegt Fassung 4 vom 24.11. Gelesen habe ich Fassung 4.

**Nicht geprüft**
- Echte Geräte, echter Server, echte Daten; Bewegung und Ton.
- Welt- und Land-Ebene der Karte, Expedition, Check-in, „abgelegt“, Flug geschafft, Flug-Test, Knobel: nur Code, Meldungen und Vorschau-Bilder.
- Lehrer- und Eltern-Ansichten (K6), 360 px außer der Übung (K7).

**Annahmen**
- Kinder melden sich mit eigenem Lern-Code an und sehen „Ändern lassen“ nicht (`ctx.leitung`).
- 390 × 664 steht für ein Handy im Browser mit Leisten; die Geräte der Kinder kenne ich nicht.
- Werkstatt-Regeln W1–W7 nicht im Council nachgelesen: nur eigene Dateien auf eigenem Zweig.

**App-Wunsch (für später, nicht Teil dieser Meldung):** keiner. Die Befunde aus 3.1 und 3.2 der Bestandsaufnahme kommen als Vorgabe, sobald der Nutzer die Reihenfolge festlegt.

