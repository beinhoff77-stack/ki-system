# Entwurf: Abschluss nach Etappe, Flug und Ort (Kinderansicht)

Auftrag: `inhalte/AUFTRAEGE.md`, „Kinderansicht: Abschluss nach Etappe und Flug (20.11., Wunsch von Sebastian)“. Stand gelesen: `lernen-app` (Merge in `pruefung-kinderansicht`, 20.11.).
Nur Entwurf und Beschreibung – kein App-Code, keine Datenbank. Freigabe durch Sebastian, danach Bau-Chat.

- Klickbarer Entwurf: `entwurf/abschluss.html` (oben umschalten: Handy 400 / Tablet 820, hell / nacht, Bewegung an / aus).
- Bilder: `bilder/<gerät>-<gestaltung>-<fall>.png` (32 Einzelbilder), Übersichten `bilder/uebersicht-etappe.png`, `bilder/uebersicht-flug-ort.png`, `bilder/uebersicht-tablet.png`.
- Beispiele erfunden (Kind A, Flug „Natürliche Zahlen“ in Rom, danach „Ganze Zahlen“ bzw. Athen „Teilbarkeit“). Keine Kinderdaten.

## 0. Was es heute gibt (gelesen in `lernen.js`)

| Stelle | Heute |
|---|---|
| Etappe gelandet (`lr-gelandet`, Übungsablauf) | „ETAPPE n VON m“, Stempel „GELANDET“ + Ortskürzel, Titel ✓, „x Bordkarten selbst gelöst, die letzten 3 in Folge“, „+n Sterne“, „Sicher wird die Etappe, wenn du sie in ein paar Tagen wieder kannst.“, Knobel-Angebot, Knopf „Anschlussflug: …“ bzw. Test-Teil, „Zur Abflugtafel“, Link „Wiederholungen ansehen, falls noch welche offen sind“. Eine Fassung für alle Verläufe. Vier gleichrangige Wege nach unten. |
| Flug-Test abgeschlossen (`lernTestErgebnis`) | Karte „x von y richtig“, Zeile „Flug geschafft! 🎉“, danach die Liste aller Test-Bordkarten mit Antworten, Knöpfe „Zum Flug / Zur Abflugtafel“. Kein Hinweis auf das nächste Thema. |
| Ort geschafft | Im selben Test-Ergebnis: kleiner Stempel „GESCHAFFT · Neuer Stempel“ + Satz „Ort geschafft! Der Stempel ist jetzt in deinem Reisepass.“ – geht zwischen Testergebnis und Antwortliste unter. |

Folge (Anlass des Auftrags): Nach der Landung gibt es mehrere gleich starke Wege, keiner sagt „du bist fertig, jetzt kommt X“. Nach dem Flug fehlt der Schritt zum neuen Thema ganz.

## 1. Abschluss einer Etappe (drei Fassungen)

### Aufbau (gleich für alle Fassungen, höchstens ein Handy-Bildschirm)

1. Kopfzeile klein: `ETAPPE {n} VON {m} · {Flugtitel}`
2. Stempel (links) + Band (nur 1a/1c) + Überschrift + Etappen-Titel (leise)
3. Ein Satz zum Verlauf
4. Karte **„Du kannst jetzt“** + ein Satz (siehe Daten)
5. `★ +{Sterne} Sterne`
6. Ein leiser Satz zur Wiederholung
7. Knobel-Angebot als kleine Karte (nicht bei 1c)
8. **Ein** großer Knopf zum nächsten Schritt
9. Textlink „Pause – zur Abflugtafel“

Entfällt gegenüber heute: der Link „Wiederholungen ansehen, falls noch welche offen sind“ (gehört auf die Abflugtafel) und jeder Weg zurück ins Üben derselben Etappe.

### Texte wörtlich

| | 1a Direktflug | 1b Sauber gelandet | 1c Drangeblieben |
|---|---|---|---|
| Stempel | `DIREKT` / `{ORT}` – Gold | `GELANDET` / `{ORT}` – Grün (Ozean: Petrol, nacht: Limette) | `GELANDET` / `{ORT}` – Lila |
| Band | `DIREKTFLUG` | – | `DRANGEBLIEBEN` |
| Überschrift | `Direktflug.` | `Sauber gelandet.` (nach „wieder offen“: `Wieder gelandet.`) | `Drangeblieben – gelandet.` |
| Satz | `{ziel} Bordkarten – alle beim ersten Versuch richtig.` | `{n} Bordkarten, {eigene} davon selbst gelöst, die letzten {folge_ziel} in Folge.` (wieder gelandet: `Nach der Wiederholung wieder {folge_ziel} in Folge richtig.`) | `{n} Bordkarten{, zweimal neu angesetzt} – und am Ende {folge_ziel} in Folge richtig. Genau so lernt man etwas Schweres.` |
| Wiederholung | `In 1 Lerntag kommt die Etappe kurz zur Wiederholung.` | wie 1a | `In 1 Lerntag kommt die Etappe kurz wieder. Dann merkst du, wie gut sie schon sitzt.` |
| Knobel | `Knobel-Bordkarte – freiwillig, ein Versuch, richtig: ★ +30` [Knobeln] | wie 1a | – (nach einem harten Weg nicht anbieten; über die Etappe weiter erreichbar) |

„Neu angesetzt“ = Stufe gesenkt; Zahl in Worten („einmal“, „zweimal“, „mehrmals“ ab 3). Bei 0 entfällt der Einschub. 1c nennt **keine** Fehlerzahl und vergleicht mit niemandem.

Knopf:
- nächste Etappe vorhanden: `Weiter: {Titel der nächsten Etappe}` / klein `Etappe {n+1} von {m}` (ist sie neu, öffnet der Knopf zuerst die Erklärung – wie heute)
- letzte Pflicht-Etappe (Fall 1d): `Weiter: Flug-Test` / klein `{k} Bordkarten, eine je Etappe, ohne Tipps`
- Test schon bestanden (Etappe nach „wieder offen“ neu gelandet): `Weiter: Zur Abflugtafel`

### Regel für die Fassung (Schwellen)

Gezählt über alle Bordkarten **dieser Etappe seit der letzten Landung bzw. seit Beginn**, ohne Mischkarten, Knobel, Expeditionen:

| Fassung | Bedingung |
|---|---|
| 1a Direktflug | `bordkarten == ziel` **und** `fehler_endgueltig == 0` **und** `mit_tipp == 0` **und** `zweite_versuche == 0` (also nur erste Versuche, alle richtig) |
| 1b Sauber | nicht 1a **und** `fehler_endgueltig <= 2` **und** `stufe_gesenkt == 0` **und** `bordkarten <= ziel + 4` |
| 1c Drangeblieben | alles andere (mehr als 2 endgültige Fehler, oder Stufe mindestens einmal gesenkt, oder mehr als `ziel + 4` Bordkarten, oder Etappe über mehr als einen Lerntag) |
| „Wieder gelandet“ | Etappe war `wieder_offen` → Layout 1b mit Überschrift „Wieder gelandet.“ (unabhängig von den Schwellen) |

### Daten – was der Server schon liefert

| Angabe | Heute vorhanden? |
|---|---|
| `eigene_loesungen`, `folge`, `folge_ziel`, `ziel`, `schwer_noetig`, `wieder_offen` | ja (`karte_stand`, `lernRegelFelder`) |
| `stufe_senkung` | nur der **aktuelle** Wert, nicht „wie oft gesenkt“ |
| Sterne dieser Antwort | ja |
| Ortskürzel, Etappe n von m, nächste Etappe | ja (Client) |
| `bordkarten` (alle Antworten der Etappe bis zur Landung), `fehler_endgueltig`, `mit_tipp`, `zweite_versuche`, `stufe_gesenkt` (Anzahl), `lerntage` | **neu**: als Feld `landung` in der Antwort von `schule_antwort`, wenn `jetzt_sitzt` wahr wird (aus den gespeicherten Antworten zählbar) |
| Satz „Du kannst jetzt …“ | **neu je Etappe**: Feld `kann` im Inhalt (Inhalts-Chats, ein Satz ohne „Du kannst“, z. B. „auf eine Stelle runden – ab 5 wird aufgerundet“). Bis dahin Ersatz: „Kurz gesagt“ (erster Satz des Merksatzes); fehlt auch der: Etappen-Titel. |

### Fertig, wenn (Etappe)

- Jede Landung zeigt genau eine der Fassungen 1a / 1b / 1c (bzw. „Wieder gelandet“) nach den Schwellen oben.
- Die Ansicht passt auf einen Handy-Bildschirm (400 × 760) ohne Scrollen, bei beiden Gestaltungen.
- Es gibt genau einen großen Knopf; kein Knopf oder Link führt zurück in die Übungen derselben Etappe.
- 1c enthält keine Fehlerzahl und kein Knobel-Angebot.

## 2. Abschluss eines Flugs (nach bestandenem Flug-Test bzw. Verbessern)

Zwei Wege im Entwurf – **Empfehlung: Weg A (zwei Schritte)**.

### Weg A, Schritt 1 „Flug geschafft“ (vor der Liste der Test-Antworten; die Liste wandert hinter „Test ansehen“)

- Klein: `{Ort} · Flug {i} von {k}`; Textlink oben rechts `Überspringen ›` (springt zu Schritt 2)
- Stempel `FLUG` / `GESCHAFFT` (Gold), groß: **`Flug geschafft`**, darunter Flugtitel
- Drei Kacheln: `{m}/{m}` `Etappen gelandet` · `{r}/{g}` `im Flug-Test{, {v} verbessert}` · `★ {Summe}` `in diesem Flug`
- Karte **„Das kannst du jetzt“**: je Etappe ein Haken + Satz `kann` (Ersatz wie oben). Handy: erste 5, dann `und {m-5} weitere anzeigen`; Tablet: alle, zweispaltig.
- Karte: **`Damit es bleibt:`** `Jede Etappe kommt in den nächsten Wochen ein paar Mal kurz wieder – je eine Bordkarte. Was man nach Tagen noch kann, sitzt wirklich.` + Kette `nach 1 Lerntag · 3 · 7 · 14 · 30`
- Knopf: `Weiter` / klein `Was als Nächstes kommt`
- Textlink: `Test ansehen` (die heutige Antwortliste)

### Weg A, Schritt 2 „Neues Thema“ (ganze Fläche in der Akzentfarbe – unübersehbar)

- Klein: `NEUES THEMA` (bei Ortswechsel: `NEUES THEMA · NEUER ORT`, siehe 3)
- Sehr groß: **`{Titel des nächsten Flugs}`**
- Ein Satz, worum es geht: neues Feld `kurz` je Thema (Inhalts-Chat), bis dahin `umfang` aus der Themenliste, auf den ersten Satzteil gekürzt (max. ~100 Zeichen)
- Chip: `📍 weiter in {Ort} · Flug {i+1} von {k}`
- `{n} Etappen · zuerst kommt die Erklärung`
- Großer Knopf (helle Fläche): `Los geht’s: {Titel}` → öffnet die Erklärung der ersten Etappe
- Textlink: `Später – zur Abflugtafel`
- Kein nächster Flug im Plan: Überschrift `Alles geschafft, was im Plan steht.`, Satz `Deine Eltern legen fest, wie es weitergeht.`, Knopf `Zur Abflugtafel`.

### Weg B: eine Seite

Wie Schritt 1, aber statt `Weiter` eine große Karte in der Akzentfarbe „Neues Thema · {Titel} · Satz · Ort“ mit Knopf `Los geht’s: {Titel}`. Ein Tipp weniger; auf dem Handy liegt die Karte aber unter dem Bildrand (siehe `bilder/handy-*-2b-flug-eine-seite.png`) – deshalb nicht empfohlen.

### Daten

| Angabe | Heute vorhanden? |
|---|---|
| `richtig`, `gesamt`, `einheit_abgeschlossen` | ja (`schule_test_abschliessen`) |
| verbesserte Bordkarten | ja (Korrektur-Sitzung), im Ergebnis zusammenführen |
| Sterne-Summe des Flugs | **neu** (`sterne_flug` im Ergebnis) – oder Kachel weglassen |
| nächster Flug: Titel, Ort, i von k, Zahl der Etappen | ja im Client (`lernReiseDaten(...).naechste`) – nach dem Test neu laden |
| Satz zum nächsten Thema | **neu** `kurz` je Thema; Ersatz `umfang` |
| „Du kannst jetzt“ je Etappe | **neu** `kann` je Etappe (wie 1) |

### Fertig, wenn (Flug)

- Nach bestandenem Flug erscheint zuerst „Flug geschafft“, dann – nach einem Tipp oder „Überspringen“ – die ganzflächige Seite „Neues Thema: {Titel}“.
- „Los geht’s“ öffnet direkt die Erklärung der ersten Etappe des nächsten Flugs.
- Die Antwortliste des Tests ist nur noch über „Test ansehen“ erreichbar.
- Beide Gestaltungen, Handy und Tablet, wie in den Bildern.

## 3. Abschluss eines Orts (letzter Flug des Orts geschafft)

Ablauf: **Flug geschafft (Schritt 1) → Ort geschafft (eigene Seite) → Neues Thema · Neuer Ort**.

Ort-Seite:
- Klein: `Alle Flüge in {Ort} geschafft`; `Überspringen ›`
- Großer Reisepass-Stempel (Gold, doppelter Rand): `GESCHAFFT` / **`{ORT}`** / `{Kontinent-Gebiet} · {Datum}`
- Überschrift: **`{Ort} ist geschafft`**
- `Der Stempel ist jetzt in deinem Reisepass – dein {n}. Stempel.`
- `★ +100 Ort-Sterne`
- Karte `Deine Flüge in {Ort}` mit Haken je Flug
- Knopf `Weiter: neuer Ort` / klein `Wohin die Reise geht`; Textlink `Reisepass ansehen`

Neues Thema bei Ortswechsel: wie Schritt 2, zusätzlich oben eine Flugroute `{alter Ort} → {neuer Ort}` (Linie zeichnet sich), Chip `✈ {neuer Ort} · {Gebiet} · Flug 1 von {k}`, Knopf `Abflug nach {neuer Ort}`.

Abhebung vom Flug: eigener Bildschirm statt Zeile; Reisepass-Stempel statt Flug-Stempel; Orts-Sterne; Route als „Abschied und neuer Ort“ in einem Bild.

Daten: `ort.abgeschlossen` ja (Test-Ergebnis); Zahl der Stempel ja (`schule_konto`); Datum ja; Flüge des Orts ja (Reise-Daten). Nichts Neues nötig außer `kurz` (wie 2).

Fertig, wenn: Mit dem letzten Flug eines Orts erscheinen nacheinander Flug-Abschluss, Ort-Seite, „Neues Thema · Neuer Ort“; der Stempel steht danach im Reisepass.

## 4. Bewegung und Ton

- Nur CSS-Animationen, keine Bibliothek, alles abgeschaltet bei `prefers-reduced-motion: reduce` (dann sofort Endzustand). Längste Animation 1,4 s.
- Etappe: Stempel „fällt“ (Skalierung 1,8 → 1, Drehung, 0,45 s), Sterne erscheinen danach (0,4 s). Direktflug zusätzlich eine Flugbahn über dem Kopf (0,9 s).
- Flug: Überschrift wächst (0,5 s), Haken der Etappen erscheinen nacheinander (je 70 ms, gedeckelt bei 0,7 s).
- Ort: Reisepass-Stempel wie Etappe, größer.
- Neues Thema: Fläche gleitet von unten herein (0,45 s); bei Ortswechsel zeichnet sich die Route (1,1 s).
- Überspringbar: Antippen irgendwo beendet die Animation; „Überspringen ›“ springt zum nächsten Schritt.
- Ton: **kein Ton** standardmäßig. Optional später eine Einstellung „Töne“ (aus) unter Gestaltung; nur nach ausdrücklicher Einwilligung der Eltern.
- Ton der Texte: sachlich-anerkennend, ohne Ausrufezeichen-Ketten und Emojis in Überschriften (Kinder 11 und 14).

## 5. Was nach dem Abschluss nicht mehr passieren darf

- Keine Knöpfe „weiter üben“, „nochmal“ oder die Übungsansicht derselben Etappe auf dem Abschluss.
- Zurück-Taste/Wischen nach der Landung führt zur Etappen-Übersicht des Flugs, nicht zurück in die Bordkarten (setzt die Korrektur aus Bau-Auftrag I, Teil 4, Punkt 5 voraus).
- Bewusster Weg zurück bleibt: Etappe in der Übersicht antippen → „Freiwillig üben“ (zählt nur für „in Folge“, wie heute bei bekannten Bordkarten).

## 6. Wer macht was (Vorschlag für die Verteilung)

| Teil | Wer |
|---|---|
| Ansichten 1–3, Animationen, Wege nach dem Abschluss | Bau-Chat (App) |
| Feld `landung` in `schule_antwort`, `sterne_flug` im Test-Ergebnis | Bau-Chat mit Datenbank (W1–W7) |
| `kann` je Etappe, `kurz` je Thema | Inhalts-Chats |

## 7. Offene Wahl für Sebastian

- Flug-Abschluss: **Weg A (zwei Schritte, empfohlen)** oder Weg B (eine Seite).
- Schwellen für 1b/1c (`fehler_endgueltig <= 2`, `bordkarten <= ziel + 4`): so lassen oder anpassen.
