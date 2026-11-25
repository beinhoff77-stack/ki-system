# Bestandsaufnahme Designer – App 0.93.4

Stand 25.11.2026 · `lernen-app` 4351182 · Vorgaben gelesen auf `pruefung-kinderansicht` ab6a9fb. Nichts Neues entworfen, kein App-Code geändert.

## 0 Kurzfassung

- **Stark:** Reisekarte und Landungs-Ansichten. Hell und dunkel sind auf 400, 820 und 1280 px durchgehend stimmig. Die Fehler-Rückmeldung (DU / ZIEL) ist die beste Ansicht der App.
- **Größtes Problem:** der Übungs-Bildschirm, also der Ort, an dem die Kinder die meiste Zeit sind. Über der Aufgabe stehen sechs Zeilen Bedienung (386 px). Bei 390 × 664 px sieht das Kind beim Öffnen **keine Aufgabe**, nur Kopf und Tastenfeld.
- **Vorgaben des Vorgängers:** alles gebaut außer FX (Spezialeffekte, 0 Zeilen im Code) und einem Teil der Kann-Punkte der Prüfung KJ (K1, K3, K5, K8 offen; K6, K7 nicht nachgeprüft).
- **Vorschlag, Reihenfolge nach Wirkung je Aufwand:** 1. Übungs-Bildschirm entschlacken · 2. Aufräum-Paket Lesbarkeit (Nacht, Tablet, Sticker) · 3. FX in einer ersten kleinen Stufe (Motor, zwei Pflicht-Effekte, Dezember-Saison).

## 1 Wie ich geschaut habe

- **Selbst nachgestellt:** App lokal mit dem nachgebildeten Server der Testsuite (`tests/lernen.test.cjs`, Testkind „Kind A“, erfundene Zahlen), Chrome ohne Fenster. Als Kind angemeldet (Lern-Code), Gestaltung „Abflug hell“ und „Abflug dunkel“, je 400 × 860, 820 × 1180 und 1280 × 800. Zusätzlich die Übung bei 390 × 664 und 360 × 640.
- **Ansichten:** Reisekarte (Kontinent), Abflugtafel mit allen Karten (Nachbessern, Expedition, Zusatz, Mein Schuljahr), Übung, erste und zweite falsche Antwort, richtige Antwort, Landung direkt / sauber / Sturm, Erklären-Übersicht, Reisepass, Merkheft, Mein Weg.
- **Bilder:** `bestandsaufnahme/bilder/`. In den Vierer-Bildern steht links 400 hell, 400 dunkel, dann 820 hell, 820 dunkel.
- **Einschränkung der Bilder:** Die Vierer-Bilder der Übung zeigen den Kasten „✎ Ändern lassen“. Den sehen nur Eltern und Lehrer (`ctx.leitung`); die Testdaten setzen dieses Feld auch beim Kind. Die Messungen unten sind ohne den Kasten gemacht.
- **Nur aus Code, Meldungen und Vorschau-Bildern (`docs/previews/la/`):** Welt- und Land-Ebene der Karte, Expeditions-Ansichten, Check-in, „abgelegt“, Flug geschafft, Test, Lehrer-Ansichten.

## 2 Vorgaben des Vorgängers – Stand

| Vorgabe (`inhalte/pruefung/kind/…`) | Stand | Woher ich das weiß |
|---|---|---|
| `abschluss/` Landung direkt / sauber / Sturm | umgesetzt | selbst gesehen, 6 Fassungen |
| `karte/` Reisekarte, Flaggen-Pins, Startknopf in der Karte | umgesetzt | Kontinent-Ebene selbst gesehen; Welt und Land nur Vorschau-Bilder `rk2-*`, `rk3-*` |
| `karten/` Nachbessern · Mein Schuljahr · Zusatz eingeplant | umgesetzt | selbst gesehen: Reihenfolge §0, Farben, Texte |
| Prüfung KJ, Muss M1, M2 und Soll S1–S6 | umgesetzt | Meldung „KJ 2 (0.93.1)“; selbst gesehen: S1 Sticker auf der Ecke, S2 Linie unter der Tafel, S4 Nachtfarben, M2 keine Mini-Linien |
| `jugendwoerter/` Sticker, 52 Sprüche, Bedeutungs-Blatt | umgesetzt | alle 14 Anlässe im Code verdrahtet; selbst gesehen: Landung, Fehler, Anrede |
| `expedition/` | umgesetzt | Meldung 0.91.x; selbst gesehen nur der Chip „Expedition wartet“ |
| `abgelegt/`, `faire-punkte/` | umgesetzt | Nachprüfung 0.87.0 des Vorgängers; nicht selbst nachgestellt |
| `reise-aufbau/` Kontinent / Land / Stadt | umgesetzt | steckt in der Reisekarte |
| **`effekte/` FX Spezialeffekte** | **offen** | siehe 2.1 |

### 2.1 FX – offen

- **Gesichert:** In `lernen.js` und `style.css` gibt es keinen Effekt-Motor, keinen Speicher `lern.fx.*`, keinen der 42 Effekte. Unter `daten/` liegt nur `jugendwoerter.json`. In `AUFTRAEGE.md` steht am 24.11.: Vorgabe liegt vor, Nutzer: „warten“.
- **Abweichung zum Auftrag:** Im Auftrag steht „Fassung 2“. Im Repo liegt **Fassung 4** vom 24.11. (15 große, 15 kleine, 8 Saison-, 4 Reserve-Effekte). Ich habe Fassung 4 gelesen.
- **In der Vorgabe selbst noch offen:**
  - Liefert der Server „Etappe jetzt sicher“ und „Etappe wieder offen“ in der Antwort mit? In der App gibt es beide Ereignisse schon („ABGELEGT“-Einblendung, Liste `nachbessern`). Ob die Felder für die zwei Pflicht-Effekte reichen, ist nicht geprüft.
  - Woher `{n}` (Zahl der legendären Etappen) kommt, ist eine Annahme.
  - Die Prüfliste nennt Punkte, aber ohne Muss / Soll / Kann. Die Rolle Designer verlangt das.
- **Termine aus der Vorgabe:** Adventskalender ab 1.12., Nikolaus 6.12., Geschenk-Drop 24.–26.12., Countdown 31.12. Bis zum 1.12. sind es sechs Tage.
- **Meinung:** Die Streiche „Absturz“ (10 s) und „Account übernommen“ (11 s) haben keinen sichtbaren Überspringen-Knopf. Das ist so entschieden. Ich würde sie als Letztes bauen und zuerst an einem Kind ausprobieren.

### 2.2 Kann-Punkte der Prüfung KJ

| Punkt | Stand | Beleg |
|---|---|---|
| K1 Sticker größer (24 / 20 px) | **offen** | `style.css`: 20 px, lange Sprüche 16 px |
| K2a Bedeutungs-Blatt nachts dunkel | erledigt | Meldung KJ 2 |
| K2b Çüş „gesprochen“ doppelt | erledigt | Meldung KJ 2 |
| K3 Abflugtafel bei 820 zweispaltig | **offen** | gesehen: einspaltig. Weniger wichtig geworden, seit die Reisekarte die Startseite ist |
| K4 „Weiter nachbessern“ als großer Knopf | erledigt | `lernen.js` Z. 3949 (`lernGrossKnopf`); nur im Code gesehen |
| K5 Zusatz-Karte: Flagge und „Teil x von y“ | **offen oder unklar** | gesehen: keine Flagge. Die Testdaten haben keinen Teil |
| K6 Lehrer 400: Ringe und Tabelle doppelt | nicht nachgeprüft | – |
| K7 360 px: Abzeichen überdeckt „DIREKTFLUG“ | nicht nachgeprüft | bei 400 px berührt es den Titel nicht |
| K8 unteres Ende der Abflugtafel aufräumen | **offen** | gesehen: Stempel, „Abflug, wann es dir passt“, zwei Links, zwei Aufklapper, „Zur Reisekarte“, „Menü“ |

## 3 Was mir selbst auffällt

Geordnet nach Gewicht für die Kinder.

### 3.1 Übung: die Aufgabe steht zu tief (gemessen)

Über der Bordkarte stehen sechs Zeilen: App-Kopf „‹ Rom · v0.93.4“, eine eigene Zeile nur für „≡“, „✕ ROM Natürliche Zahlen“, die Reiter ERKLÄREN / ÜBEN / FEHLER, die Etappen-Leiste, „? Erklärung ansehen“. Die Bordkarte beginnt bei 386 px. Das Tastenfeld klebt unten und ist 269 px hoch.

| Fenster | Bordkarte | Tastenfeld | Was das Kind beim Öffnen sieht |
|---|---|---|---|
| 400 × 860 | 386–698 | 581–850 | Frage sichtbar. Antwortfelder (544–598) im unteren Drittel verdeckt, „Tipp“ (645–685) ganz verdeckt |
| 390 × 664 | 386–693 | 385–654 | **keine Aufgabe.** Nur Kopf und Tastenfeld (Bild `uebung-390x664.png`) |
| 360 × 640 | 386–693 | 361–630 | **keine Aufgabe**, Tastenfeld liegt schon über „Erklärung ansehen“ |
| 820 × 1180 | 386–671 | 901–1170 | alles sichtbar, aber 230 px Leere zwischen Aufgabe und Tastenfeld |
| 1280 × 800 | 402–687 | 721–989 | „Prüfen“ liegt unter dem Fensterrand |

- 390 × 664 entspricht etwa einem Handy im Browser mit Adress- und Werkzeugleiste. **Annahme:** Ich weiß nicht, welche Geräte die Kinder benutzen und ob die App als installierte App ohne Leisten läuft.
- Die Versionsnummer im Kopf ist für Kinder ohne Nutzen.

### 3.2 Lesbarkeit: vier Stellen

- **Nacht, Erklären-Übersicht:** Die Etappen-Kachel unter dem Mauszeiger wird hell (238, 234, 224), die Schrift bleibt fast weiß (242, 244, 247). Unlesbar. Für `.lr-kachel` gibt es keine eigene Regel für „Zeiger darüber“, vermutlich greift die helle Regel der alten App (Ursache nicht bis zur Zeile verfolgt). Auf Tablets bleibt dieser Zustand nach dem Antippen oft stehen (Annahme, nicht am Gerät geprüft). Bild `erklaeren-400-820.jpg`.
- **Nacht, Abflugtafel:** Der Chip „Expedition wartet“ bleibt hellblau-weiß. Daneben sind Nachbessern und Zusatz seit KJ 2 dunkel. Bild `abflugtafel-400-820.jpg`.
- **Tablet 820, Landung:** Im Blatt unter der Szene sind die Schriften 11 bis 14 px („DU KANNST JETZT“ 11, Erklärsatz 13,5, „Etappe 2 von 3“ 13, „Pause“ 14). Der Rahmen der App verlangt mindestens 16 px. Die Szene darüber hat dabei viel leere Fläche.
- **Sticker:** 20 px, lange Sprüche 16 px. Bei 820 px wirken sie wie ein Etikett am Rand (= K1).

### 3.3 Der häufigste Moment ist der blasseste (Meinung)

Richtige Antwort: eine grüne Zeile „✓ AN BORD · +10 STERNE“ und der Lösungsweg. Das passiert viele Male am Tag. Landungen, die selten sind, bekommen dagegen eine ganze Szene. Die kleinen FX-Effekte (Combo, Hitmarker, Level up) setzen genau hier an, sind aber nicht gebaut.

### 3.4 Kleinere Beobachtungen

- **Zwei Kopfzeilen auf jeder Unterseite:** App-Kopf und darunter eine Zeile nur für „≡“. Das kostet überall rund 60 px.
- **Reisepass** sieht aus wie eine Einstellungs-Seite: drei Zahlen-Kacheln, „Noch kein Stempel“, Belohnungen, Gestaltung, Abmelden. Kein Pass, keine Stempel-Seite. Die Wahl „Bisheriges Design“ steht noch für Kinder da.
- **Mein Weg** benutzt eine zweite Bildsprache (Linienplan mit „Haltestellen“). Dort heißt „Kontinent“ ein Mathe-Gebiet, auf der Reisekarte ist ein Kontinent ein echter Erdteil. Im Merkheft steht beides nebeneinander: „EUROPA · ZAHLEN“.
- **Fehler-Ansicht** („Das hat gerade nicht geklappt“): nachts hell, im alten Aussehen, mit englischer Technik-Meldung im Klartext. Ausgelöst habe ich sie mit meinen Testdaten unter `#/wiederholen`; das ist kein Befund zur Wiederholung selbst.
- **Farbe des Hauptknopfs wechselt:** gelb (Start, Direktflug), grün (saubere Landung), bernstein (Sturm), orange (Nachbessern). Das folgt den Vorgaben. Zur Leitregel „ein Hauptknopf“ würde eine feste Farbe besser passen (Meinung).
- **Abflugtafel bei 1280:** Karten 1008 px breit, die Tafel selbst 720 px, alles einspaltig untereinander.

## 4 Die drei wirkungsvollsten Verbesserungen für die Kinder

Geordnet nach Wirkung je Aufwand. Aufwand ist meine Schätzung, kein Bau-Angebot.

### 1. Übungs-Bildschirm: Aufgabe zuerst

- **Was:** Die sechs Zeilen über der Bordkarte auf eine oder zwei zusammenlegen. Frage, Antwortfeld, „Tipp“ und Tastenfeld passen bei 390 × 664 ohne Scrollen auf einen Bildschirm. Auf dem Tablet rückt das Tastenfeld an die Aufgabe, am Rechner bleibt „Prüfen“ im Fenster.
- **Wirkung: hoch.** Betrifft jede einzelne Aufgabe bei beiden Kindern. Passt zur Vorgabe „fast alles läuft automatisch“: Reiter und Blättern sind Wege zum freiwilligen Ansehen und dürfen zurücktreten.
- **Aufwand: klein bis mittel.** Umordnen vorhandener Teile, keine neue Mechanik, keine Daten.
- **Von mir:** eine Vorgabe mit Maßen für 360, 400, 820, 1280 und ein Entwurf zum Anklicken.

### 2. Aufräum-Paket Lesbarkeit

- **Was:** Nacht-Farbe für Kacheln unter Zeiger und Finger, Expeditions-Chip nachts dunkel, Blatt der Landung auf dem Tablet mindestens 16 px, Sticker größer (K1), Fehler-Ansicht im Aussehen der Kinder und ohne Technik-Text, Versionsnummer für Kinder weg. Dazu die offenen K5 und K8.
- **Wirkung: mittel.** Jede Stelle ist klein, aber unlesbare Stellen wirken kaputt. Annahme: Mindestens ein Kind nutzt die dunkle Gestaltung.
- **Aufwand: klein.** Fast nur Farben und Schriftgrößen.
- **Von mir:** eine Liste mit Farbwerten hell und dunkel und einer Prüfliste Muss / Soll / Kann.

### 3. FX, erste Stufe

- **Was:** FX-1 aus der Vorgabe: Motor mit Regeln und Speicher, „Legendary Drop“, „Respawn“, dazu Adventskalender, Nikolaus, Geschenk-Drop und Countdown. Danach die kleinen Effekte für die richtige Antwort (3.3). Streiche und Horror zuletzt.
- **Wirkung: hoch.** Das ist der vom Nutzer gewünschte Stil, und die Saison-Effekte gibt es nur im Dezember.
- **Aufwand: groß.** Deshalb Platz 3. Der Motor ist einmalig, jeder große Effekt ist ein eigenes Stück.
- **Abhängig von:** der Freigabe des Nutzers („warten“ vom 24.11.) und der Server-Frage aus 2.1.
- **Von mir:** die Vorgabe für die erste Stufe schneiden, Prüfliste Muss / Soll / Kann ergänzen, die zwei offenen Punkte klären.

## 5 Nicht geprüft

- Echte Geräte, echter Server, echte Kinderdaten.
- Bewegung und Ton; ich habe nur Standbilder.
- Welt- und Land-Ebene der Karte, Expedition, Check-in, „abgelegt“, Flug geschafft, Flug-Test, Knobel: nicht selbst geöffnet.
- Lehrer- und Eltern-Ansichten, damit K6.
- 360 px außer der Übung, damit K7.
- Die Systemeinstellung „dunkel“ des Geräts. Geprüft sind die zwei Gestaltungen der App.

## 6 Annahmen

- Kinder melden sich mit eigenem Lern-Code an und sehen „Ändern lassen“ nicht.
- Die Testdaten der Suite bilden die echten Ansichten ab.
- Die Werkstatt-Regeln W1–W7 aus `AGENTS.md` betreffen Änderungen an der App. Ich habe sie nicht im Council nachgelesen, weil ich nur Dateien in meinem Ordner auf meinem Zweig anlege.
