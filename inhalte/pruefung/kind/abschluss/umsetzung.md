# Entwurf: Abschluss nach Etappe, Flug und Ort (Kinderansicht)

Auftrag: `inhalte/AUFTRAEGE.md`, „Kinderansicht: Abschluss nach Etappe und Flug (20.11., Wunsch von Sebastian)“. Stand gelesen: `lernen-app` (Merge in `pruefung-kinderansicht`, 20.11.).
Nur Entwurf und Beschreibung – kein App-Code, keine Datenbank. Freigabe durch Sebastian, danach Bau-Chat.

- Klickbarer Entwurf (Entwurf 2): `entwurf/abschluss.html` (oben umschalten: Handy 400 / Tablet 820, hell / nacht, Bewegung an / aus; „↺“ spielt die Bewegung nochmal).
- Bilder: `bilder/<gerät>-<gestaltung>-<fall>.png` (28 Einzelbilder), Übersichten `bilder/uebersicht-etappe.png`, `bilder/uebersicht-flug-ort.png`, `bilder/uebersicht-tablet.png`.
- Beispiele erfunden (Kind A, Flug „Natürliche Zahlen“ in Rom, danach „Ganze Zahlen“ bzw. Athen „Teilbarkeit“). Keine Kinderdaten.

## 0. Was es heute gibt (gelesen in `lernen.js`)

| Stelle | Heute |
|---|---|
| Etappe gelandet (`lr-gelandet`, Übungsablauf) | „ETAPPE n VON m“, Stempel „GELANDET“ + Ortskürzel, Titel ✓, „x Bordkarten selbst gelöst, die letzten 3 in Folge“, „+n Sterne“, „Sicher wird die Etappe, wenn du sie in ein paar Tagen wieder kannst.“, Knobel-Angebot, Knopf „Anschlussflug: …“ bzw. Test-Teil, „Zur Abflugtafel“, Link „Wiederholungen ansehen, falls noch welche offen sind“. Eine Fassung für alle Verläufe. Vier gleichrangige Wege nach unten. |
| Flug-Test abgeschlossen (`lernTestErgebnis`) | Karte „x von y richtig“, Zeile „Flug geschafft! 🎉“, danach die Liste aller Test-Bordkarten mit Antworten, Knöpfe „Zum Flug / Zur Abflugtafel“. Kein Hinweis auf das nächste Thema. |
| Ort geschafft | Im selben Test-Ergebnis: kleiner Stempel „GESCHAFFT · Neuer Stempel“ + Satz „Ort geschafft! Der Stempel ist jetzt in deinem Reisepass.“ – geht zwischen Testergebnis und Antwortliste unter. |

Folge (Anlass des Auftrags): Nach der Landung gibt es mehrere gleich starke Wege, keiner sagt „du bist fertig, jetzt kommt X“. Nach dem Flug fehlt der Schritt zum neuen Thema ganz.

## 1. Abschluss einer Etappe (drei Fassungen, Entwurf 2)

Sebastians Rückmeldung zu Entwurf 1: „zu unspektakulär und zu gleich“. Entwurf 2: jede Fassung hat **eigene Szene, eigene Farbe, eigenes Abzeichen, eigene Bewegung** – auf den ersten Blick unterscheidbar.

### Aufbau (gleich gegliedert, verschieden gestaltet)

Oben die **Szene** (ca. 60 % der Höhe, Vollbild-Hintergrund), darunter ein **Blatt** (weiß bzw. nacht-dunkel), das von unten hereinfährt:
- Szene: Kopfzeile `ETAPPE {n} VON {m} · {Etappen-Titel}`, großer Titel (Großbuchstaben), Fassungs-Element, Abzeichen, Bild.
- Blatt: Karte **„Du kannst jetzt“** + ein Satz · `★ +{Sterne}` · Knobel-Angebot (nicht bei 1c) · ein leiser Satz · **ein** großer Knopf (Farbe der Fassung) · Textlink `Pause – zur Abflugtafel`.

Entfällt gegenüber heute: „Wiederholungen ansehen …“ und jeder Weg zurück ins Üben derselben Etappe.

### Die drei Fassungen

| | 1a Direktflug | 1b Saubere Landung | 1c Sturmflug gemeistert |
|---|---|---|---|
| Szene | Sonnenuntergang (Nachtblau → Lila → Orange), Kondensstreifen über die ganze Breite, Jet am Ende, Gold-Funken | Blauer Taghimmel, Landebahn in Perspektive, Flugzeug setzt auf | Gewitterwolken, Blitz, Licht bricht unten rechts durch, Flugzeug fliegt aus dem Sturm ins Licht |
| Titel | `DIREKTFLUG` | `SAUBERE LANDUNG` (nach „wieder offen“: `WIEDER GELANDET`) | `STURMFLUG GEMEISTERT` |
| Fassungs-Element | riesig `{ziel}/{ziel}` in Gold, darunter `AUF ANHIEB`; Satz `Kein Fehler, kein Tipp, kein Umweg.` | Chips `{n} Bordkarten` · `{eigene} selbst gelöst` · `{folge_ziel} in Folge` | Satz `{n} Bordkarten{, zweimal neu angesetzt} – und nicht abgedreht. Am Ende {folge_ziel} in Folge richtig.` |
| Abzeichen | Sechseck Gold „⚡ DIREKT“ | Kreis Grün „✓ SAUBER“ | Schild Gold-Lila „⚡ AUSDAUER“ (als Band `⚡ AUSDAUER-ABZEICHEN`) |
| Knopf-Farbe | Gold | Grün | Sonnengelb auf Violett |
| Satz im Blatt | `Neues Abzeichen im Reisepass: Direktflug. In 1 Lerntag kommt die Etappe kurz zur Wiederholung.` | `In 1 Lerntag kommt die Etappe kurz zur Wiederholung.` | `Das war die schwerste Strecke – und du bist angekommen. In 1 Lerntag kommt die Etappe kurz wieder.` |
| Knobel | ja | ja | nein (bleibt über die Etappe erreichbar) |

1c nennt keine Fehlerzahl und vergleicht mit niemandem; „neu angesetzt“ = Stufe gesenkt (Wort: einmal / zweimal / mehrmals; bei 0 entfällt der Einschub). Das Ausdauer-Abzeichen ist ausdrücklich gleichwertig – im Reisepass steht es neben „Direkt“ und „Sauber“.

Knopf: nächste Etappe `Weiter: {Titel}` / klein `Etappe {n+1} von {m}`; letzte Pflicht-Etappe `Weiter: Flug-Test` / klein `{k} Bordkarten, eine je Etappe, ohne Tipps`; Test schon bestanden: `Zur Abflugtafel`.

### Regel für die Fassung (Schwellen)

Gezählt über alle Bordkarten dieser Etappe bis zur Landung, ohne Mischkarten, Knobel, Expeditionen:

| Fassung | Bedingung |
|---|---|
| 1a Direktflug | `bordkarten == ziel` und `fehler_endgueltig == 0` und `mit_tipp == 0` und `zweite_versuche == 0` |
| 1b Saubere Landung | nicht 1a und `fehler_endgueltig <= 2` und `stufe_gesenkt == 0` und `bordkarten <= ziel + 4` |
| 1c Sturmflug | alles andere (mehr Fehler, Stufe gesenkt, mehr als `ziel + 4` Bordkarten oder über mehrere Lerntage) |
| Wieder gelandet | Etappe war `wieder_offen` → Szene 1b, Titel „WIEDER GELANDET“ |

### Daten

| Angabe | Heute vorhanden? |
|---|---|
| `eigene_loesungen`, `folge`, `folge_ziel`, `ziel`, `wieder_offen`, Sterne | ja |
| `bordkarten`, `fehler_endgueltig`, `mit_tipp`, `zweite_versuche`, `stufe_gesenkt` (Anzahl), `lerntage` bis zur Landung | **neu**: Feld `landung` in der Antwort von `schule_antwort`, wenn die Etappe landet (aus gespeicherten Antworten zählbar) |
| Fassung/Abzeichen speichern (`landung_art`: direkt / sauber / sturm) und im Reisepass zählen | **neu** (Datenbank, W1–W7); Reisepass: Zeile „Abzeichen: ⚡ Direkt 4 · ✓ Sauber 9 · ⚡ Ausdauer 3“ |
| Satz „Du kannst jetzt …“ | **neu** Feld `kann` je Etappe (Inhalts-Chats); Ersatz „Kurz gesagt“, sonst Etappen-Titel |

### Fertig, wenn (Etappe)

- Jede Landung zeigt genau eine Fassung nach den Schwellen; die drei sind ohne Lesen an Farbe und Bild unterscheidbar.
- Handy 400 × 780 ohne Scrollen, hell und nacht (die Szene ist in beiden gleich, das Blatt folgt der Gestaltung).
- Genau ein großer Knopf; kein Weg zurück in die Übungen derselben Etappe.
- 1c ohne Fehlerzahl, ohne Knobel; das Abzeichen wird gespeichert und im Reisepass gezählt.

## 2. Abschluss eines Flugs → Bordkarte zum neuen Thema (zwei Bildschirme)

### Bildschirm 1 „Flug geschafft“

- Szene Nachtblau mit Konfetti (fällt einmal, 1,8 s), oben `{ORT} · FLUG {i} VON {k} · {FLUGTITEL}`, Textlink `Überspringen ›`
- Riesig in Gold: **`FLUG GESCHAFFT`**
- Eine Reihe Lichter: je Etappe ein goldener Punkt, gehen nacheinander an
- Zähler: `{Summe} ★` zählt hoch, darunter `Sterne in diesem Flug · Test {r} von {g}{, {v} verbessert}`
- Blatt: **`Das kannst du jetzt – {m} Etappen`** mit Haken-Liste (Handy scrollbar, Tablet zweispaltig) · `Damit es bleibt: Jede Etappe kommt in den nächsten Wochen ein paar Mal kurz wieder – je eine Bordkarte.` + Kette `nach 1 Lerntag · 3 · 7 · 14 · 30`
- Knopf Gold: `Weiter zum nächsten Thema` / klein `Deine neue Bordkarte`; Textlink `Test ansehen` (die heutige Antwortliste)

### Bildschirm 2 „Neues Thema“ – die Bordkarte

Ganzer Bildschirm dunkel, darauf eine **Bordkarte** (fährt herein):
- Oben gelb: `NEUES THEMA`
- Kopf rot: `BORDKARTE` · `{Kind}`
- Gleicher Ort: `ORT {ORT}` ✈ `FLUG {i+1} / {k}`; Ortswechsel siehe 3
- `FLUG` **`{Titel des nächsten Flugs}`** (groß), darunter ein Satz worum es geht
- Felder `ETAPPEN {n}` · `GEBIET {Gebiet}` · `FLUG {i+1} von {k}`
- Abriss-Linie, Strichcode, `GATE: ERKLÄRUNG`
- Großer Knopf Gold: `Boarding: {Titel}` / klein `Zuerst kommt die Erklärung` → öffnet die Erklärung der ersten Etappe
- Textlink `Später – zur Abflugtafel`
- Kein nächster Flug im Plan: Bordkarte ohne Ziel, `Alles geschafft, was im Plan steht. Deine Eltern legen fest, wie es weitergeht.`, Knopf `Zur Abflugtafel`.

Erster Entwurf hatte daneben „alles auf einer Seite“; mit der Bordkarte als eigenem Bildschirm entfällt diese Variante (auf dem Handy war das neue Thema dort unter dem Bildrand).

Daten: `richtig`, `gesamt`, `einheit_abgeschlossen` ja; verbesserte Bordkarten ja (zusammenführen); Sterne-Summe **neu** `sterne_flug`; nächster Flug (Titel, Ort, i von k, Etappen) ja im Client nach Neuladen; Satz **neu** `kurz` je Thema (Ersatz `umfang`); `kann` je Etappe wie oben.

Fertig, wenn: Nach bestandenem Flug erst „Flug geschafft“, dann nach einem Tipp oder „Überspringen“ die Bordkarte; „Boarding“ öffnet die Erklärung der ersten Etappe; die Antwortliste nur über „Test ansehen“.

## 3. Abschluss eines Orts → Reisepass-Stempel → Bordkarte zum neuen Ort

Ablauf: Flug-Bildschirm 1 → **Ort-Bildschirm** → Bordkarte mit Ortswechsel.

Ort-Bildschirm: Hintergrund wie Reisepass-Papier (Sand/Beige), oben `REISEPASS · STEMPEL {n}`, großer roter Doppelrand-Stempel knallt auf: `GESCHAFFT` / **`{ORT}`** / `{Gebiet} · {Datum}`, darunter **`{ORT} IST GESCHAFFT`**, `Alle {k} Flüge · ★ +100 Ort-Sterne`. Blatt: `Deine Flüge in {Ort}` mit Haken; Knopf (Siegelrot) `Weiter: neuer Ort` / klein `Deine Bordkarte nach {neuer Ort}`; Textlink `Reisepass ansehen`.

Bordkarte bei Ortswechsel: oben `NEUES THEMA · NEUER ORT`, `VON {ALTER ORT}` ✈ `NACH {NEUER ORT}`, Knopf `Abflug nach {neuer Ort}`.

Abhebung vom Flug: eigene Papier-Szene statt Nachthimmel, Stempel statt Lichterreihe, Orts-Sterne, und die Bordkarte zeigt den Ortswechsel.

Daten: `ort.abgeschlossen`, Stempelzahl, Datum, Flüge des Orts – alles vorhanden.

## 4. Bewegung und Ton

Nur CSS (und ein kleiner Zähler in JS), keine Bibliothek; bei `prefers-reduced-motion: reduce` oder Einstellung „Bewegung aus“ sofort Endzustand. Jede Szene höchstens 1,8 s, Antippen beendet sie, „Überspringen ›“ springt weiter.

| Ansicht | Bewegung |
|---|---|
| 1a Direktflug | Kondensstreifen zeichnet sich (1 s), Jet erscheint, Gold-Funken sprühen, „6/6“ knallt auf, Abzeichen dreht sich ein |
| 1b Saubere Landung | Flugzeug sinkt auf die Landebahn (1,1 s), Abzeichen dreht sich ein |
| 1c Sturmflug | zwei Blitze (Aufhellen 1,1 s), Flugzeug fliegt aus der Ecke ins Licht, Licht wächst, Ausdauer-Band knallt auf |
| Flug | „FLUG GESCHAFFT“ wächst, Lichter gehen nacheinander an, Konfetti fällt, Sterne zählen hoch |
| Ort | Stempel knallt auf (0,5 s) |
| Bordkarte | fährt mit leichter Drehung herein (0,6 s) |
| Blatt | fährt nach der Szene von unten herein (0,45 s) |

Ton: standardmäßig keiner; optional später „Töne“ (aus) unter Gestaltung, nur nach Einwilligung der Eltern. Texte sachlich-anerkennend, Großbuchstaben-Titel statt Ausrufezeichen, keine Emojis in Überschriften (Kinder 11 und 14).

## 5. Was nach dem Abschluss nicht mehr passieren darf

- Keine Knöpfe „weiter üben“, „nochmal“ oder die Übungsansicht derselben Etappe auf dem Abschluss.
- Zurück-Taste/Wischen nach der Landung führt zur Etappen-Übersicht des Flugs, nicht zurück in die Bordkarten (setzt die Korrektur aus Bau-Auftrag I, Teil 4, Punkt 5 voraus).
- Bewusster Weg zurück bleibt: Etappe in der Übersicht antippen → „Freiwillig üben“ (zählt nur für „in Folge“, wie heute bei bekannten Bordkarten).

## 6. Wer macht was (Vorschlag für die Verteilung)

| Teil | Wer |
|---|---|
| Ansichten 1–3, Animationen, Wege nach dem Abschluss, Abzeichen im Reisepass | Bau-Chat (App) |
| Feld `landung` in `schule_antwort`, `landung_art` speichern, `sterne_flug` im Test-Ergebnis | Bau-Chat mit Datenbank (W1–W7) |
| `kann` je Etappe, `kurz` je Thema | Inhalts-Chats |

## 7. Freigabe (Sebastian, 20.11.)

- Entwurf 2 freigegeben, so wie im klickbaren Entwurf.
- Schwellen bleiben: Saubere Landung = höchstens 2 endgültige Fehler, Stufe nie gesenkt, höchstens `ziel + 4` Bordkarten; alles darüber Sturmflug.
- Abzeichen werden gespeichert und im Reisepass gezählt.
