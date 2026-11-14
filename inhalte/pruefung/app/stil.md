# Stil-Vorschläge Lernreise (Prüfrunde App, Zweig `pruefung-app`)

Zum Prüfen durch die Projektleitung. Nichts davon ist in der App umgesetzt. Die dazugehörigen Befunde 30–34 stehen in `bericht.json`.

- **Entwurf zum Anklicken:** `entwurf/index.html?ansicht=heute|ueben|richtig|falsch&look=ozean|nacht`. Die Datei ist eigenständig, Schrift liegt bei. Im Üben-Entwurf führt die Eingabe „2000“ zu „richtig“, alles andere zu „falsch“.
- **Bilder erzeugen:** `PW_TEST_EXECUTABLE=… node inhalte/pruefung/app/entwurf/bilder.cjs` schreibt `bilder/stil-entwurf-*.png`.
- **Vorher/Nachher:**
  - `bilder/stil-vorher-nachher-heute-390.png`
  - `bilder/stil-vorher-nachher-ueben-390.png`
  - `bilder/stil-vorher-nachher-nacht-390.png`

## 1. Befund in einem Satz

Der Stil ist sauber und ruhig (Stand 2023/24). Für 10-Jährige fehlen aber eine klare Rangfolge, eine durchgehende Reise-Optik und Freude im Moment des Erfolgs.

**Gut und beibehalten:**
- echte Weltkarte
- Linien-Icons
- große Knöpfe mit „Druckkante“
- die vier Looks (Ozean, Nacht, Dschungel, Wüste)
- keine Gamification-Hektik

## 2. Fakten (nachgestellt, mit Bild)

| Nr. | Beobachtung | Beleg |
|---|---|---|
| F1 | Look „Nacht“: Kopfzeile und der Streifen darüber bleiben beige über der dunkelblauen Seite. | Befund 30, `bilder/30-nacht-kopfzeile-beige.png` |
| F2 | Die Kinderschrift `ui-rounded` gibt es nur auf Apple-Geräten. „Nunito“ steht in der Liste, wird aber nicht geladen (kein `@font-face`). Auf dem Testgerät (Linux-Chrome) erscheint die normale Systemschrift. | Befund 31, `style.css` Zeile 3184 |
| F3 | Auf „Heute“ (390 px) stehen sieben gerahmte Kästen übereinander; der Hauptknopf ist der achte Block. | Befund 32 |
| F4 | Richtig/Falsch/Lernkarte sitzt: nur Text- und Farbwechsel, keine Bewegung, keine Figur. | Befund 33 |
| F5 | Am Rechner: 600-px-Spalte, Leiste über die volle Breite, „Prüfen“ unter dem Rand. | Befund 34, Befund 1 |
| F6 | Zwei Stilwelten im Kinderablauf: Der Test nutzt die Eltern-Optik. | Befund 13 |

## 3. Vorschläge S1–S8 (nach Gewinn geordnet)

### S1 – Ein Look von oben bis unten (klein)
- Im Kindmodus `body` ohne `padding-top`, Kopfzeile ohne Glocke.
- Kopfzeile mit `background: var(--lr-bg)` und Text in `var(--lr-text)`.
- Inhalt der Kopfzeile: links „‹“ + Ort (z. B. „Rom“), rechts ein Sterne-/Stempel-Chip. Der Chip führt zum Reisepass.
- Test, Test-Ergebnis und Fehlerseite in `lr-karte-box` und `lr-knopf` statt `card` und `primary`.

### S2 – Eine Hauptkarte pro Seite (mittel)
- **Heute:**
  - Begrüßung (eine Zeile), darunter **eine** Karte: Erdteil-Band, Ort, Thema, Route und der Knopf „Los geht’s“.
  - Der Unterzeile des Knopfs sagt, was kommt: „erst 2 Wiederholungen, dann Lernkarte 1“.
  - Alles andere ohne Rahmen als einfache Liste („Danach“).
  - Zahlenkästen entfallen; sie stecken im Chip oben.
- **Üben:**
  - Oben eine Textzeile „Lernkarte 1 · Titel“ mit drei Punkten für die Karten.
  - Darunter die Aufgabenkarte mit Frage, Eingabe und Prüfen.
  - Tipp und Erklärung als Textknöpfe darunter.
  - Chips, Stufen, Pfad und doppelter Titel entfallen bzw. kommen in ein Menü.
- **Regel:** höchstens ein Schatten-Element pro Bildschirm. Nebeninhalte mit Trennlinie statt Rahmen.

### S3 – Schrift und Größen (klein)
- **Schrift:** Nunito (variabel, SIL OFL 1.1) selbst ausliefern, `nunito-latin-wght-normal.woff2`, 39 KB (liegt in `entwurf/`).
  ```css
  @font-face { font-family: "Nunito"; src: url("nunito.woff2") format("woff2"); font-weight: 200 1000; font-display: swap; }
  .lr { font-family: "Nunito", ui-rounded, system-ui, sans-serif; font-variant-numeric: tabular-nums; }
  ```
- **Größen:**

  | Rolle | Größe / Stärke |
  |---|---|
  | Seitentitel | 30 px / 900 |
  | Ort in der Hauptkarte | 28 px / 900 |
  | Aufgabentext | 26 px / 900 |
  | Eingabe | 30 px / 900, zentriert |
  | Fließtext | 18 px / 600–700 |
  | Kleinschrift | mindestens 13 px / 800, Großbuchstaben mit Abstand .08em |

- `tabular-nums` sorgt dafür, dass Stellenwerte untereinander stehen (wichtig für 182 887 / 20 000).

### S4 – Weltreise als Farbsystem (mittel)
- **Erdteilfarbe als Variable.** Die Farben gibt es schon je Look in `style.css` (Zeilen 3187–3193: `--lr-EU`, `--lr-AS`, `--lr-AF`, `--lr-NA`, `--lr-SA`, `--lr-OC`, `--lr-AN`). Neu ist nur eine Zuordnung auf dem Thema-Container über `LERN_ERDTEIL`:
  ```css
  .lr-erdteil-EU { --erdteil: var(--lr-EU); }  /* … AS, AF, NA, SA, OC, AN entsprechend */
  .lr-ozean, .lr-dschungel, .lr-wueste { --erdteil-text: #2B2410; }  /* dunkle Schrift auf hellen Erdteilfarben */
  .lr-nacht { --erdteil-text: #F2F4FF; }                            /* helle Schrift auf den dunklen Nacht-Erdteilfarben */
  ```
  Kontrast vor dem Einbau je Look prüfen (Ziel ≥ 4,5:1 für Band-Text). Im Entwurf ist Europa/Ozean (#F6C85F) gezeigt; im Nacht-Entwurf bewusst dieselbe helle Farbe, die echte Nacht-Farbe wäre #3B4A86.
- **Verwendung:**
  - Band oben auf der Hauptkarte („EUROPA · ZAHLEN · ORT 1 VON 5“)
  - Stationen der Route
  - markierte Zelle in Stellentafel/Zeichnung
  - Hintergrund der Erklärbox bei Fehlern (Erdteilfarbe 22 % gemischt)
- **Fortschritt als Route:** Jede Lernkarte ist eine Station (Kreis 34 px mit Nummer), Strecke dazwischen gepunktet bzw. durchgezogen, wenn geschafft. Am Ende das Stempel-Symbol. Darunter: „3 Lernkarten bis zum Stempel von Rom“. Das ersetzt den Balken „2 von 3 Etappen“.
- **Kartenausschnitt auf Heute** wird zur Route. Die echte Weltkarte bleibt im Reiter „Karte“.
  - Alternative zum Prüfen: kleiner Kartenausschnitt (80 px) im Band statt Farbfläche.

### S5 – Rückmeldung mit kurzer Bewegung (klein)
- **Richtig:** Haken-Kreis springt auf (`scale .3→1`, 450 ms, Federkurve). Kasten gleitet von unten ein (350 ms). „★ +10“ fliegt vom Eingabefeld zum Kasten (900 ms). In der Kopfzeile zählt der Sterne-Chip hoch.
- **Falsch:** Eingabefeld wackelt 2× um 6 px (350 ms), Rand in `--falsch`. Text „Fast! Richtig ist 2 000.“ Darunter klappt „So geht’s“ in Erdteilfarbe auf. Kein rotes Kreuz, kein Ton.
- **Lernkarte sitzt:** Station der Route wird gefüllt, Stempel-Symbol pulsiert einmal.
- **Hover:** `filter: brightness(1.05)` statt Hintergrundwechsel (behebt Befund 4).
- **Regeln:**
  - Alles aus bei `prefers-reduced-motion: reduce`.
  - Keine Bewegung länger als 1 s.
  - Kein Konfetti bei jeder Aufgabe, nur beim Stempel.

### S6 – Reisefigur „Koffi“ (mittel)
- Ein kleiner Reisekoffer mit Gesicht. Eigener Entwurf, im Entwurf als SVG mit Theme-Farben, 64 px.
- **Einsatz:**
  - Begrüßung auf Heute
  - leere Zustände („Deine Reise ist noch nicht geplant“ statt „null“)
  - Serverfehler („Da hat was gehakt – nochmal?“)
  - Stempel-Moment (Koffi bekommt einen Aufkleber der Stadt)
- **Nicht** bei jeder Aufgabe und nicht als Druckmittel („Koffi ist traurig“).
- Zwei Gesichter genügen: froh und neutral.
- **Zu prüfen:** Gefällt den Kindern eine Figur? Vorschlag: die drei Varianten Koffer, Papierflieger, Kompass zeigen und sie wählen lassen.

### S7 – Tablet und Rechner (mittel)
- Ab 820 px: Leiste als Seitenleiste links (96 px, Einträge oben gestapelt).
- Im Üben: zwei Spalten, links die Erklärung der Karte (bleibt beim Scrollen stehen), rechts die Aufgabe.
- Heute: Hauptkarte höchstens 560 px breit, mittig.
- Ergebnis: Prüfen und Erklärung sind ohne Scrollen sichtbar (`bilder/stil-entwurf-ueben-1280.png`).

### S8 – Leiste mit Reisepass, Eltern-Kleinschrift (klein)
- **Kinder-Leiste mit fünf Einträgen:** Heute, Mein Weg, Merkheft, Karte, Reisepass. Aktiver Eintrag mit hinterlegter Fläche (10 % Akzent) statt nur Farbe.
- **Eltern-Bereich bleibt erwachsen** (Georgia-Titel, Beige). Nur:
  - Kopfzeilen in Großbuchstaben 12 px statt 10 px, Farbe #7a5640
  - `--muted` im Lernen-Bereich #5c6a61
  - dunkle Signalfarben im Lernen-Bereich auf helle Werte setzen (Befund 16)

## 4. Vorschlag zur Reihenfolge

1. **S1, S3, S8:** 1–2 Tage, rein CSS/kleine JS-Änderungen, sofort sichtbar.
2. **S2 + S5:** zusammen mit den Bedienungs-Befunden 1, 2, 26, 27 bauen, denn es sind dieselben Bildschirme.
3. **S4:** vorhandene Erdteilfarben (`--lr-EU` …) als `--erdteil` auf Thema und Heute durchreichen.
4. **S7:** Breitbild-Raster.
5. **S6:** erst nach Kindertest der Figur.

## 5. Offen / Annahmen

- **Schrift auf den Geräten der Kinder:** Ob die runde Schrift heute fehlt, hängt vom Gerät ab. Nicht geprüft; Annahme nach CSS: iPad/iPhone vorhanden, Windows/Android nicht.
- **Kartenausschnitt:** Ob die Kinder den Kartenausschnitt auf Heute vermissen, wenn er zur Route wird, ist offen. Gegebenenfalls Alternative aus S4.
- **Erdteilfarben:** vorhanden in `style.css`; Kontrast des Band-Texts je Look noch zu prüfen.
- **Geschmack:** Farben, Figur und Bewegung sind Vorschläge und am Kind zu testen.
