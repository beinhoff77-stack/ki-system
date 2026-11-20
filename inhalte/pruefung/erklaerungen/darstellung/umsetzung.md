# Erklärungen umbauen – Umsetzung (Stand 2026-11-16)

Grundlage: Sebastians Auswahl (`bericht.md`, Abschnitt 6). Dieses Papier sagt, **was die App ändern muss**, **wie Inhalte künftig aussehen** und **wie der Bestand umgebaut wird**.
Geschrieben im Prüf-Zweig; hier ist nichts an App, Tests oder `inhalte/themen/` geändert. Umsetzen sollen der Haupt-Chat (App) und die Inhalts-Chats.

Bestand (gezählt am 2026-11-16): 87 Themen, 549 Lernkarten, 1 500 Schritte. Karten mit `einstieg`: Kl. 5 80 von 87, Kl. 8 90 von 97, alle anderen Klassen 0. Karten mit Bild: 242.

---

## 1. Das Muster (verbindlich für alt und neu)

**Erklären-Reiter**
1. **Übersicht:** Kacheln aller Lernkarten, nach Bereichen (`abschnitte`). Jede Kachel: Titel, Status, darunter der Merksatz als „Kurz gesagt“ (`regel`, gekürzt auf 1 Zeile). Die empfohlene Karte ist hervorgehoben.
2. **Karte öffnen:** Es ist immer nur eine Karte zu sehen. Oben steht „‹ Übersicht“, unten „Nächste Karte ›“.
3. **Aufbau der Karte, gleich für alle Klassen:**
   1. **Worum geht’s?** (`einstieg`, kurz)
   2. **Bild** (Kartenbild)
   3. **Beispiel als Bildergeschichte:** alle Schritte untereinander, jeder Schritt mit eigenem kleinen Bild
   4. **Letzter Schritt: „Pass auf!“** (`fehler`, mit eigenem Bild, wenn vorhanden)
   5. **MERKE** (`regel`)
   6. **„Jetzt du ›“** (öffnet Üben)
4. **Neue Wörter:** Das Wort ist beim ersten Vorkommen im Text gepunktet unterstrichen. Antippen zeigt die Erklärung direkt darunter. Eine Liste der Wörter steht eingeklappt am Kartenende.
5. **Markierung:** `⟦…⟧` überall als gelber Textmarker. Rot und Rosa nur für Fehler.
6. **Brüche:** `a/b` aus ganzen Zahlen wird gestapelt gesetzt (Zähler über Nenner).
7. **Schrift in Zeichnungen:** mindestens 16 px, auch auf dem Handy.

**Üben-Reiter, erster Besuch einer Karte:** Nur die Aufgabe. Darüber steht ein gut sichtbarer Link „Erklärung ansehen“. Kein Merksatz, keine Erklärung über der Aufgabe.

**Klasse 7–10:** Die Karte ist aufgebaut wie Klasse 5. „Kurz gesagt“ steht dort nur auf der Übersichtskachel.
*Noch offen:* Sebastian ist bei Punkt 10 unentschieden. Fällt die Wahl auf „Regel zuerst“, kommt in Klasse 7–10 zusätzlich „Kurz gesagt“ als erste Zeile in die Karte. Das ist in der App ein Schalter, die Inhalte bleiben gleich.

---

## 2. Auftrag an den Haupt-Chat (App)

| Nr. | Änderung | Ort (heute) | Fertig, wenn … |
|---|---|---|---|
| A1 | Übersicht → eine Karte | `lernEtappen` | Erklären öffnet die Übersicht. Antippen zeigt genau eine Karte. Zurück und Weiter funktionieren, auch mit der Zurück-Taste des Browsers. |
| A2 | Feste Reihenfolge nach 1.3, für alte und neue Karten | `lernErklaerung` | Karten ohne `einstieg` beginnen beim Bild. Es gibt keine zweite, „alte“ Anzeige mehr. |
| A3 | Bildergeschichte | `lernErklaerung`, `lernBild` | Jeder Schritt bekommt sein Bild (Format 3.1). Ein Schritt ohne eigenes Bild zeigt den Bildzustand des vorigen Schritts, aber nur, wenn die Karte Schrittbilder hat. Sonst gibt es keine Bilder in den Schritten, nur das Kartenbild oben. Handy: Bild über dem Text. Tablet und Rechner: Bild links, Text rechts. |
| A4 | „Pass auf!“ als letzter Schritt | `lernErklaerung` | Zeigt `fehler` und, falls vorhanden, `fehler_bild`. Der Reiter „Fehler“ bleibt unverändert. |
| A5 | Wörter im Text antippen | `lernMarkiert` | Trifft auch Beugungen (Wortanfang plus bis zu 3 Buchstaben). Nur das erste Vorkommen je Karte. |
| A6 | Eine Markierung | `style.css` | `⟦…⟧` überall `#FFE58A`, Kontrast ≥ 4,5:1, auch im Dunkelmodus. |
| A7 | Brüche stapeln | `lernMarkiert` | `3/4` im Text erscheint gestapelt. Daten und Uhrzeiten bleiben unberührt, ebenso URLs und `km/h`. |
| A8 | Bildschrift ≥ 16 px | `style.css`, `lernBild` | Gemessen bei 390, 820 und 1280 px. |
| A9 | Üben: nur die Aufgabe | `uebenOeffnen` (`erklBox`) | Die Aufgabe steht bei 390 px im ersten Bildschirm. |
| A10 | Neue Zeichnungsarten | `lernBild` | `zahlenstrahl` + `punkte`, `boegen`, `bereich`; `thermometer`; `bruchstreifen` (Felder in `bericht.md` 3.2). Alle sind auch als `f.grafik` in Aufgaben nutzbar. |
| A11 | Prüfregeln | `tools/inhalt_pruefen.py` | Prüft die Regeln aus Abschnitt 4: zu lange Texte gibt eine Warnung, ein falsches Format einen Fehler. |
| A12 | Inhalts-README | `inhalte/README.md` | Der Abschnitt „Die Anzeige mit `einstieg` …“ ist durch Abschnitt 4 dieses Papiers ersetzt. |

**Reihenfolge:**
- A2, A5–A9, A12 sofort. Sie wirken auf alle 549 Karten ohne Inhaltsarbeit.
- Danach A1, A3, A4.
- Danach A10, A11, denn sie sind Voraussetzung für den Umbau der Inhalte.

**Rückwärtskompatibel:** Alte Karten mit `schritte` als reine Texte laufen ohne Änderung. Aufgaben und Fortschritt bleiben unberührt.

---

## 3. Neues Inhaltsformat

### 3.1 Schritte mit Bild

```json
"bild": {"typ": "zahlenstrahl", "start": -10, "ende": 10, "abschnitte": 20, "beschriftet": "anfang_ende"},
"schritte": [
  {"text": "Der Taucher ist bei −7 m, der Vogel bei 7 m.", "bild": {"punkte": [{"wert": -7, "name": "Taucher"}, {"wert": 7, "name": "Vogel"}]}},
  {"text": "Von −7 bis 0 sind es 7 Schritte. Also ist ⟦|−7| = 7⟧.", "bild": {"boegen": [{"von": -7, "bis": 0, "name": "7"}]}},
  {"text": "Der Vogel ist genauso weit weg: |7| = 7."}
],
"fehler": "Den Betrag negativ schreiben: |−7| ist nicht −7. Ein Abstand ist nie kleiner als null.",
"fehler_bild": {"boegen": [{"von": -7, "bis": 0, "name": "7, nicht −7"}]}
```

- Das `bild` im Schritt **ergänzt oder überschreibt** Felder des Kartenbildes. Ein anderes `typ` ersetzt das Bild ganz.
- Ein Schritt ohne `bild` zeigt den Bildzustand des vorigen Schritts. `fehler_bild` funktioniert genauso.
- Reine Text-Schritte bleiben erlaubt.

### 3.2 Felder je Karte (Pflicht für neue und umgebaute Karten)

`titel`, `einstieg`, `woerter`, `bild`, `schritte` (Objekte), `fehler`, `fehler_bild` (wenn sich der Fehler zeigen lässt), `regel`.

---

## 4. Regeln für Inhalte (Text zum Einfügen in `inhalte/README.md`, ersetzt „Die Anzeige mit `einstieg` …“)

```text
Die Anzeige (alle Klassen gleich): Übersicht (Titel + Merksatz als „Kurz gesagt“) → eine Karte:
WORUM GEHT’S? → Bild → Beispiel als Bildergeschichte (jeder Schritt mit Bild) → „Pass auf!“ (fehler + fehler_bild) → MERKE.
Neue Wörter werden im Text antippbar; die App macht das selbst aus `woerter`.

Längen und Form:
- einstieg ≤ 35 Wörter, 2–3 Sätze. Dieselbe Situation wie Bild und Beispiel.
- höchstens 3 neue Wörter je Karte; jedes muss im einstieg oder in den schritten vorkommen.
- schritte: 2–4 Schritte (höchstens 5), je ≤ 15 Wörter, je Schritt ein Gedanke. Jeder Schritt, in dem sich im Bild etwas ändert, hat ein eigenes `bild`.
- fehler ≤ 30 Wörter, in der Situation gedeutet; `fehler_bild`, wenn der Fehler sichtbar gemacht werden kann.
- regel ≤ 25 Wörter, der erste Satz taugt allein als „Kurz gesagt“ (≤ 12 Wörter).
- Sätze ≤ 15 Wörter (Kl. 5/6), ≤ 20 Wörter (Kl. 7–10).
- ⟦…⟧ nur für das Ergebnis eines Schritts und das Kernwort im Merksatz, höchstens 2 je Absatz.
- Brüche als a/b schreiben (die App stapelt sie), nicht als Unicode-Bruchzeichen.
- Jede Karte hat ein Kartenbild. Gibt es keine passende Zeichnungsart: in "offen" notieren, nicht erfinden.
Aufgaben werden beim Umbau nicht geändert (Texte wörtlich gleich, damit Fortschritt erhalten bleibt).
```

---

## 5. Umbau des Bestands

**Voraussetzung:** A3, A4, A10 und A11 sind im Zweig `lernen-app`.

**Je Karte:**
- auf die Längen aus Abschnitt 4 kürzen
- `einstieg` und `woerter` ergänzen, wo sie fehlen (Kl. 6, 7, 9, 10, ohne Klasse)
- `schritte` in Objekte mit Bild umwandeln
- `fehler_bild` ergänzen
- Karten ohne Bild bekommen ein Kartenbild

`titel`, `lernziel` und `aufgaben` bleiben unverändert.

**Arbeit im Generator:** Der Umbau geschieht in `inhalte/generatoren/<thema>.py`, nicht von Hand in der JSON-Datei. Danach `python3 -I tools/inhalt_pruefen.py …` ohne Fehler.

**Pakete und Reihenfolge** (ein Zweig je Paket, ein Thema = ein Commit, Postfach nach `inhalte/postfach/README.md`):

| Paket | Zweig | Themen | Karten | Hinweis |
|---|---|---|---|---|
| U5 | `umbau-kl5` | 12 | 87 | zuerst (Kind A), braucht Thermometer, Zahlenstrahl mit Bögen, Bruchstreifen |
| U8 | `umbau-kl8` | 15 | 97 | Kind B, meist Koordinatensystem mit Schritt-Zuständen |
| U6 | `umbau-kl6` | 8 | 58 | auch `einstieg`/`woerter` neu |
| U7 | `umbau-kl7` | 7 | 45 | auch `einstieg`/`woerter` neu |
| U9 | `umbau-kl9` | 14 | 87 | auch `einstieg`/`woerter` neu |
| U10 | `umbau-kl10` | 7 | 45 | auch `einstieg`/`woerter` neu |
| UR | `umbau-rest` | 24 | 130 | Themen ohne `gym_by` (Realschule, IB) |

**Auftragstext je Paket** (in `inhalte/AUFTRAEGE.md` übernehmen, `<…>` ersetzen):

```text
Du baust die Lernkarten (Erklärungen) eines Pakets der Lern-App auf das neue Muster um.
Repository: beinhoff77-stack/ki-system, Ausgangszweig lernen-app. Lege den Zweig <zweig> an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (besonders „Verständliche Erklärungen“ und die Längenregeln),
inhalte/pruefung/erklaerungen/darstellung/umsetzung.md (Abschnitte 1, 3, 4, 5) und als Muster die Karte
zahlen.ganz/betrag in inhalte/pruefung/erklaerungen/darstellung/entwurf.html.

Aufgabe: Für jedes Thema mit "gym_by": <klasse> in inhalte/themenliste.json den Generator
inhalte/generatoren/<thema>.py so ändern, dass jede Lernkarte dem Muster entspricht:
einstieg, woerter (≤ 3), Kartenbild, schritte als Objekte mit Bild je Bildänderung, fehler + fehler_bild, regel (erster Satz = Kurz gesagt).

Regeln:
- Aufgaben nicht ändern (Texte wörtlich gleich). titel und lernziel nicht ändern.
- Nur Zeichnungsarten aus inhalte/README.md benutzen. Fehlt eine: im Feld "offen" notieren, nicht erfinden.
- Ein Thema ist fertig, wenn python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json ohne Fehler durchläuft
  und du jede Karte einmal laut gelesen hast: Versteht ein Kind der Klasse sie beim ersten Lesen?
- Ein Thema = ein Commit + Push auf <zweig>. Status nach jedem Thema in inhalte/postfach/<zweig>.md.
- Keine Datenbank, keine Serverfunktionen, kein App-Code, kein Merge nach main.
Arbeite ohne Rückfragen durch; Unklares unter "offen" notieren.
```

**Abnahme je Paket:** Der Projektleiter liest stichprobenartig 3 Karten auf dem Handy. Danach liest das Kind eine Karte und löst die erste Aufgabe, ohne Hilfe.

---

## 6. Offen

- **Punkt 10** (Klasse 7–10: „Kurz gesagt“ zusätzlich in der Karte?) entscheidet Sebastian. Das ist ein App-Schalter, die Inhalte sind davon nicht betroffen.
- **Nicht mit den Kindern getestet.** Vorschlag: nach A1–A9 je eine umgebaute Karte mit beiden Kindern ausprobieren, bevor die Pakete U6–UR starten.
- **Aufwand ist geschätzt, nicht gemessen:** U5 und U8 sind die größten Brocken, weil fast jeder Schritt ein eigenes Bild bekommt.
