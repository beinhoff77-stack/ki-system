# Postfach bau-app

Neueste oben.

## 2026-11-27 – FERTIG RU-1b (App 0.95.0) Auflagen Werkstatt 1079 (Zweig `helfer-uni`, Cache v187)

**Geliefert**
- `sw.js`: `daten/regeln-universum.json` steht nicht mehr in der Vorab-Liste (fällt die Datei aus, scheitert die Hülle nicht mehr); der `daten/`-Handler speichert sie beim ersten Öffnen. Neu im Handler (für alle Hüllen- und Datendateien): Bei HTTP-Fehler (z. B. 503) kommt die gespeicherte Fassung, ohne gespeicherte Fassung die Antwort des Servers; bei Netzabbruch wie bisher der Cache. Cache v187, Version bleibt 0.95.0.
- Kinderseiten ohne doppelten Kopf: eigene Marke „Regel-Universum“ entfällt (Titel steht im App-Kopf; zurück zu Ebene 0 über die Brotkrume „‹ Universum“), der Menüknopf der oberen Menüzeile steht jetzt rechts in der (klebenden) Zeile der Suche, die Überschrift „Regel-Universum“ auf Ebene 0 ist nur noch für Bildschirmleser da. Ebene 0 bei 400 × 860: 6 von 7 Gebieten im ersten Bildschirm (vorher 5). Menü unten, Suche, Umschalter unverändert. Eltern-Bereich unverändert.
- Daten laden nicht: Meldung „Das Regel-Universum lädt gerade nicht. Prüfe das Internet und versuch es noch einmal.“ mit Knopf „Noch einmal versuchen“, beim Kind im Rahmen der Kinderseite (Menü bleibt).
- Nicht angefasst: `daten/regeln-universum.json`, `tools/regeln_bauen.cjs`, `tests/lernen-regeln.test.cjs`, `inhalte/` außer Bildern und Postfach.

**Tests**
- 3 neue Tests in `tests/lernen.test.cjs` (Kopf 400 × 860 hell/dunkel: ≥ 6 Gebiete, Menü und Suche in einer Zeile; Ladefehler 503 → Meldung → „Noch einmal versuchen“ → Universum; Service Worker im Node-`vm` nachgestellt: nicht in der Vorab-Liste, beim ersten Abruf gespeichert, 503 und Netzabbruch → gespeicherte Fassung, ohne Speicher → Antwort des Servers).
- Gesamttest 217/217 (1. Lauf 215/217: zwei Wettläufe in meinen eigenen Tests – sie warteten auf ein Element, das auch die vorige Seite hat, bzw. maßen während des Übergangs; berichtigt, mit `LERN_CPU=4` grün). `lernen-regeln` 6/6, `lernen-bruch` 24/24, `lernen-takt` 10/10, `node --check` alle geänderten Dateien.
- Bilder erneuert (`inhalte/pruefung/regeln/bilder/`, neu `fehler-laden-400-dunkel.jpg`), angesehen: Ebene 0 400 dunkel/hell, 1280 hell, Fehlerseite.

**Nicht geprüft**: Service Worker im echten Browser (Tests blockieren ihn), echte Geräte.

## 2026-11-27 – FERTIG RU-1 (App 0.95.0) Regel-Universum Stufe 1, ohne Datenbank (Zweig `helfer-uni`, Cache v186)

**Geliefert**
- Kinder: Regel-Universum nach `umsetzung7.md` (Abschnitt 10) und `entwurf7/` – Ebene 0 (Sonne, 7 Gebiete, Arbeitsweisen; ab 900 px Sonnensystem-Bild), Ebene 1 Sonne (Schnitt durch die Sonne, 14 Regeln in 4 Schichten mit Merksatz und Klassenband, Legende), Gebiet (Ideen mit Band), Arbeitsweisen; Ebene 2 gestufte Regel-/Ideenseite (Kurzbeschreibung, Merksatz, Beispiel offen; „Dieselbe Regel in Klasse …“, „Genau erklärt“, „Typische Fehler“, „Aufbau“ zu), Arbeitsweise mit Kurzbeschreibung/Beispiel/Erklärung; Ebene 3 Einzelregel; Umschalter „Aufbau | Durch die Klassen“ (Handy Klassenwahl, Rechner Tabelle); Suche im Kopf; Brotkrumen; Übergang 220 ms; Sternenfeld dunkel auf Ebene 0/1. Kein Lernstand.
- Einstieg Kind: Menüblatt der Kinderseiten (≡ Menü) – fünfter Eintrag „Regel-Universum“ → `#/regeln/<kind>`. Kein Verweis vor einer Aufgabe.
- Eltern/Lehrer: „Regeln“ in „Nachschlagen“ der Startseite → `#/regeln` (Liste: 14 Rechenregeln nach Schichten, 28 Ideen nach Gebieten, 8 Arbeitsweisen) → Blatt `#/regeln/lehrer-r<n>` mit 5 Abschnitten offen (Merksatz, Was das Kind sieht, Fachliche Erklärung, Verweise und Zuordnung mit Lehrplan-Tabelle aus `texte8/lehrplan.json` und „Nicht geprüft“, Themen mit „Lehrer-Seite ›“ (öffnet den Lehrplan mit dem Thema), bis zu 3 Beispielaufgaben, Fehlbilder, Aufbau; Stand je Kind „Stand folgt“). „So sieht es das Kind ›“ → `#/regeln/kind-r<n>` (mit Leiste zurück zum Blatt).
- Rückmeldung: gebaut, an Merksatz/Karte/Erklärung/Zuordnung. Weg `schule_rueckmeldung_geben` ohne Einheit, `bezug: 'allgemein'` (Migration 20261117 lässt `allgemein` zu, Einheit/Block sind optional; lernen-api reicht `daten` unverändert durch). Arten Fehler → `fehler`, Vorschlag/Frage → `sonstiges` (Prüfbedingung der Tabelle); Text beginnt mit „Regel 6 · Ausmultiplizieren und Ausklammern (rr.ausmultiplizieren) · Merksatz · Frage: “. `lernAuftragForm` hat dafür zwei optionale Parameter (`arten`, `vorsatz`), sonst unverändert.
- Daten: `daten/regeln-universum.json` (606 kB, gzip 101 kB), erzeugt mit `node tools/regeln_bauen.cjs` (endet mit „OK“; `--pruefen` vergleicht). Übernommen aus `texte8`: 42 Kurzbeschreibungen (18 berichtigt), Regel 10 kürzere Fassung, 25 Lücken (genau/voraus/fehler), 8 Arbeitsweisen, 30 Einzelregeln (Beispiel + Grenze), Lehrplan je Regel, Beispielaufgaben R10/R14. Die Zeichnungen des Entwurfs werden beim Bau einmal ausgeführt und als SVG-Text abgelegt (42 Zeichnungen). Laden erst beim Öffnen; `sw.js` nimmt Datei, `lernen-regeln.js`, `lernen-regeln.css` in die Hülle.
- Code: `lernen-regeln.js` (eigene Datei), `lernen-regeln.css` (alles unter `.ru`, Präfix `ru-`). `lernen.js` +4 Zeilen (Menüeintrag, Link „Regeln“, Formular-Optionen), `app.js`/`schule.js` je Route `regeln`. Hell/dunkel folgt der Gestaltung des Kindes bzw. dem System (kein eigener Umschalter). Version 0.95.0 an allen 5 Stellen, Cache v186.

**Tests**
- `tests/lernen-regeln.test.cjs` (neu, ohne Browser): 6/6 – Datei = Bau, Vollständigkeit (14/4/7/28/8, Merksatz, Kurzbeschreibung, Beispiel), texte8 übernommen (R10 kurz, R6 unverändert, 18 + 25), Suche, alle 235 Adressen ohne leere Texte/„undefined“, Adressen/Ebenen/Rückmelde-Text und Arten gegen die Migrationen.
- `tests/lernen.test.cjs`: 2 neue Browser-Tests (Kind 400 hell/dunkel + 1280; Eltern 400 + 1280; Querscrollen, Tippflächen ≥ 44 px nach dem Übergang, keine Skriptfehler). Gesamttest 214/214.
- `lernen-bruch` 24/24, `lernen-takt` 10/10. Bilder: `inhalte/pruefung/regeln/bilder/` (29, mit `RU_BILDER=1` aus den Browser-Tests).

**Abweichungen vom Entwurf**
- Über dem Universum stehen App-Kopf (Zurück, Titel) und die Menüzeile der Kinderseiten: Ebene 0 beginnt ~160 px tiefer; am Handy sind im ersten Bildschirm 5 statt 7 Gebiete zu sehen, am Rechner ist die Kapsel „Arbeitsweisen“ erst nach Wischen sichtbar.
- Schnitt durch die Sonne: Tippfläche ist das ganze Band (im Entwurf nur die Schriftzeile, 26 px hoch).
- Eltern-Bereich: Kopf und Klassenwahl kleben nicht (die App-Leiste klebt schon); Farben der App statt Abflug-Farben.
- Für Ideen und Arbeitsweisen gibt es noch kein Lehrer-Blatt; die Liste verweist auf die Kinderseite.
- Regel 9: Beispielaufgabe BG-05 nicht gezeigt (Stichprobe Mathe-Profi „passt nicht“), stattdessen Hinweis; R4/R11 mit Hinweis „nur teilweise geprüft“.

**Nicht geprüft**
- Echter Server (Rückmeldung nur gegen die simulierte lernen-api), echte Geräte/Safari, Offline-Betrieb (Tests blockieren den Service Worker; die eigene Lernen-Seite `lernen/` registriert keinen Service Worker), Bildschirmleser, dunkel im Eltern-Bereich, „Lehrer-Seite ›“ mit echten Themen-Nummern.

**Annahmen**
- Einstieg für Kinder im Menüblatt (nicht auf der Karte), weil es auf jeder Kinderseite da ist und nicht vor einer Aufgabe steht. Im alten Design (Leiste unten) gibt es keinen Einstieg.
- Die Daten-HTML (Bruch-Schreibweise, SVG) wird als HTML eingesetzt – nur aus der im Repo erzeugten Datei; übrige Texte maskiert.

**Stufe 2 braucht von der Datenbank**: Bezugsfeld „Regel“ (Kennung + Abschnitt) für `schule_rueckmeldung_geben` und `schule_rueckmeldungen`, Stand je Kind und Regel (sitzt / in Arbeit / kommt später), Fehlbilder je Regel aus dem Server.

## 2026-11-27 – FERTIG 0.94.0 Form-Takt, Nachbesserung nach Werkstatt 1039/1040 (Zweig `helfer-app2`, Cache v185)

**Geliefert**
- Eine zentrale Stelle `lernTaktErlaubt(letzte, takt)` in `lernen.js`: „nie zwei Lückenwege hintereinander“ und „kein Fehler-Detektiv direkt nach einem eigenen Fehler“. In `lernWaehleBordkarte` läuft jede Kandidatenliste durch diesen Filter (Schwer-Vorrang, Lückenweg nach 2 Fehlern, Sachaufgabe, Form-Platz, Bordkarten ohne form, alle). Das Muster „gefiltert, sonst ungefiltert“ je Schritt ist weg.
- Notfall (neuer Grund `notfall`): Nur wenn mit den Verboten gar keine Bordkarte wählbar ist (außer höchstens der eben gelösten letzten), läuft die alte Auswahl ohne die Verbote. Begründung: Sonst stünde keine neue Bordkarte da bzw. dieselbe noch einmal; ein Gerüst oder Detektiv ist dann das kleinere Übel. Sobald eine andere wählbare da ist, kommt sie; die schwere wird später nachgeholt.
- Pflicht „schwere Aufgabe“: Aufgaben mit `zaehlt = nein` werden vom Schwer-Vorrang nicht mehr gewählt (in `lernWaehleKern`, also auch auf dem alten Weg ohne form; ohne `zaehlt` wie bisher). Die normale Auswahl darf sie weiter ziehen.
- Version bleibt 0.94.0, Cache v185.

**Tests**
- `tests/lernen-takt.test.cjs`: 10/10 (6 alte + 4 neue: beide nachgewiesenen Fälle samt Varianten Brücke/allgemeine Auswahl/Schwer nachholen, Punkt 3, Gegenproben „Vorrat leer“ → Notfall, Zufallstest 20 000 Lagen mit form als Invarianten). Die 4 neuen schlagen mit dem Stand vor der Nachbesserung fehl. Der 4000-Fälle-Vergleich mit 0.93.8 besteht weiter.
- `tests/lernen-bruch.test.cjs`: 24/24. `tests/notifications.test.cjs`: 3/3.
- Gesamttest `tests/lernen.test.cjs`: 212 Tests, 212 bestanden, 0 fehlgeschlagen.

**Offen / nicht geprüft**
- Nicht gegen den echten Server; keine Sichtprüfung auf Geräten. Kein Test zählt die Cache-Nummer (nur die Versionsgleichheit 0.94.0).

## 2026-11-27 – FERTIG 0.94.0 Form-Takt (Zweig `helfer-app`, Cache v184)

**Geliefert**
- Auswahl (`lernen.js`): `lernWaehleBordkarte(warte, e, letzte, gesehenTyp, takt)` ist jetzt ein Aufsatz auf `lernWaehleKern` (= Auswahl von 0.93.8, nur mit optionalem Vorrat-Filter). Hilfen: `lernSollStufe`, `lernAnders`, `lernFormPlatz`, `lernAnwendenFehlt`, `lernIstAnwenden`.
  Reihenfolge: schwere Bordkarte nötig → Lückenweg nach 2 Fehlern in Folge → Sachaufgabe fehlt → Form-Platz (ungelöste Bordkarte mit `form`, Stufe die dran ist, anderer Typ als die letzte) → Bordkarten ohne `form`, solange es ungelöste gibt → alle.
  Hat keine Bordkarte `form` und fehlt keine Sachaufgabe, läuft unverändert der alte Weg (Kern ohne Filter).
- Platz = `bearbeitungen` (etappen_stand) + in der Sitzung abgeschlossene Bearbeitungen dieser Lernkarte + 1. Liefert die Antwort `bearbeitungen` (in `karte` oder daneben), gilt dieser Stand und der Sitzungszähler fängt bei 0 an; fehlt er (auch: `karte` fehlt ganz), zählt die App selbst +1. Zweiter Anlauf = dieselbe Bearbeitung; Mischkarten zählen nicht.
- Takt nur beim normalen Üben einer offenen Lernkarte (Auswahl läuft heute schon nicht bei gewählter Stufe, gelandeter/fälliger Karte = Wiederholung); Mischkarten, Knobel, Expedition, Test unberührt. Nach dem Wiederöffnen läuft der Platz am Gesamtstand weiter.
- Regel 4: `fehlFolge === 2` setzt einmal „nachFehler“; nie zwei Lückenwege hintereinander; nach einem Fehler kein `fehler_detektiv` (auch nicht auf dem Form-Platz – dann eine andere Form oder normal).
- Regel 6: Checkliste zeigt „○ Eine Sachaufgabe fehlt noch“ (gleiche Stelle/Stil wie „schwere“), nur wenn `anwenden_noetig && !anwenden_ok` und sonst alles erfüllt (eigene ≥ ziel, Typen, schwer, Folge). Dann wird eine ungelöste zählende Sachaufgabe (`typ` einkleidung/transfer/pruefung, `zaehlt` ≠ nein) vorgelegt.
- `zaehlt: "nein"`: im Kopf der Bordkarte (neues und altes Design) klein „Zum Aufwärmen – zählt nicht für die Landung“, Farbe der Kopfzeile (`.lr-zaehlt-nicht` in `style.css`).
- Nachtrag Werkstatt 1030–1032, Bruch-Erkennung: `lernZeichenAb`/`lernZeichenVor` prüfen an allen vier Grenzen (Klammer-Zähler, Zähler, Klammer-Nenner, Nenner) ganze Codepoints; „4/x𐞥“, „4/(x)𐞥“ bleiben Text.
- Version 0.94.0 in den fünf Dateien, Cache v184.

**Tests**
- `tests/lernen-takt.test.cjs` (neu, ohne Browser): 6/6 – darunter 4000 Zufallsfälle: ohne neue Felder wählt die App genau wie 0.93.8 (Vergleich gegen die wörtliche alte Funktion).
- `tests/lernen-bruch.test.cjs`: 24/24 (22 alte + 2 neue: Fälle U+107A5 und systematische Probe über alle Codepoints der Klasse `LERN_HOCH_ALLG`, vorwärts und rückwärts; die neuen Tests schlagen mit dem alten Code fehl).
- `tools/bruch_durchsicht.cjs`: 0 Texte mit geändertem Ergebnis (13 323 / 13 323 gestapelte Brüche), verdächtige Reste 0/0.
- Gesamttest `tests/lernen.test.cjs`: 212 Tests, 212 bestanden, 0 fehlgeschlagen (203 alte + 9 neue „Form-Takt …“). Ein erster Gesamtlauf vor dem Nachtrag: 209/209.

**Annahmen (nicht prüfbar, Server noch nicht eingespielt)**
- `bearbeitungen` in der Antwort von `schule_uebung_pruefen` zählt die gerade beantwortete Bearbeitung schon mit.
- Der Server zählt Antworten in der Wiederholung mit (Bau-Bericht (e)/(f)); die App zählt sie in der Sitzung ebenso, damit der Platz nach dem Wiederöffnen gleich bleibt. Knobel-Antworten zählt die App nicht; falls der Server sie zählt, gleicht die nächste Antwort mit `bearbeitungen` das aus.
- `form_jede` steht oben in `schule_einheit_lesen`; `form`/`zaehlt` je Übung; `anwenden_noetig`/`anwenden_ok` in `etappen_stand[lz]` und `karte` (nur wenn `eigene_loesungen` geliefert wird – neue Regel).
- „Solange es welche ohne form gibt“ = solange es UNGELÖSTE ohne form gibt (sonst bekämen Kinder auf zwei von drei Plätzen nur noch gezählte Wiederholungen).

**Offen / nicht geprüft**
- Nicht gegen den echten Server geprüft (nur Simulation). Keine Sichtprüfung auf Handy/Tablet/Rechner, hell/dunkel; keine Vorschau-Bilder erneuert.
- Schwer-Vorrang bleibt wie heute ohne Takt-Vorrat (eine schwere Bordkarte mit `form` kann dort auch außerhalb des Form-Platzes kommen).

## 2026-11-27 – FERTIG 0.93.8 (Bruch-Erkennung nachgebessert, Zweig `helfer-bruch2`, Commit f3e24697, Cache v183)

- Zweideutige Gruppe im Zähler („2 125/128“, „1 200/x“) bleibt ganz Text; gestapelt nur, wenn auch der Nenner eine Tausendergruppe hat („11 880/20 736“). Gemischte Zahlen „2 1/2“, „3 25/48“ unverändert.
- Alle hochgestellten Zeichen (Ziffern, ⁺⁻⁼⁽⁾, ⁿⁱ, ᵃ…ᶻ) gehören zur Basis; die Durchsicht nimmt dieselbe Liste aus `lernen.js`.
- Datum: nur nach „am“, „vom“, „zum“, „seit“ (Tag 1–31, Monat 1–12). „bis“ und „ab“ verworfen: trafen 5 echte Brüche des Bestands („von 3/8 bis 1/2“, „AB 2/4“); „den“ weggelassen (zu riskant).
- Auswahl-Kürzel w/m, m/w, m/w/d, j/n, ja/nein, u/o bleiben Text.
- Durchsicht: 6 Texte geändert (alle 1 200/x bzw. 1 500/x → Text, gewollt); zweideutige Gruppe im Zähler: 7 Texte, davon 6 bewusst Text, 1 gestapelt (11 880/20 736); verdächtige Reste 0/0.
- Tests: lernen-bruch 19/19; Gesamttest 203 Tests, 203 bestanden, 0 fehlgeschlagen.
- Nicht geprüft: Darstellung im Browser von Hand (nur über den Gesamttest); Texte außerhalb `inhalte/themen`.

## 2026-11-25 – FERTIG: WT (App 0.93.5)

Ausgangsstand `origin/lernen-app` 8ae84ee, Zweig `bau-app`. Nur App und Tests: keine Datenbank, nichts eingespielt, kein Merge. Cache v180.

**Ursache des wackligen Tests „KJ §0: Kinderseite …“**
- Rot war die Prüfung `ohneQuerrollen` bei 400 px (Tag), nicht der Hauptknopf.
- Auslöser ist die Anrede-Sticker („Digga“) auf der Ecke der ersten Karte (unter 600 px, `.lr-jw-ecke`). Ihr Auftauchen („Plopp“, `lrJwPlopp`, 0,35 s Verzögerung + 0,4 s) schwingt über 100 % hinaus. Dabei ragt das „?“ (`.lr-jw-frage`) etwa 0,45–0,6 s nach dem Zeichnen 2–3 px über den rechten Rand: Die Seite ist kurz quer rollbar (scrollWidth 402–403 bei 400 px).
- Der Test prüft nach `waitFor` + 400 ms + den übrigen Prüfungen. Je nach Rechnerlast fällt die Prüfung in dieses Fenster oder nicht. Das ist ein echter, kleiner Fehler der App (kurzes Querrollen auf dem Handy), kein Fehler des Tests.
- Der Verdacht „Hauptknopf wird nachträglich gefüllt“ trifft diesen Test nicht: Die Abflugtafel zeichnet erst, wenn alle Antworten da sind, und `lernSchrittKnopf` kommt dort nicht vor. Mit verzögerter Karte, Übersicht, Konto oder Merkheft (je 800 ms) und mit Zufallsverzögerung blieb Reihenfolge, Text und Ziel immer richtig.

**Fehlermeldung im Wortlaut** (KJ §0 einzeln, 3 von 10 Läufen rot, Zeile 5042 = `ohneQuerrollen` in der Schleife 400/820):
```
not ok 1 - KJ §0: Kinderseite – Nachbessern zuerst (Expedition als Chip), Gerade dran, Zusatz · eingeplant, Mein Schuljahr; Zahlen aus schuljahr_stand; gelber Knopf nie Zusatz (400/820, Tag und Nacht)
  error: |-
    The expression evaluated to a falsy value:

      assert.ok(await ohneQuerrollen(page))

  code: 'ERR_ASSERTION'
```
Messung (alle 40 ms nach dem Zeichnen): 4 von 8 Durchläufen bei 400 px mit `I.lr-jw-frage r=402` zwischen 484 und 565 ms; bei 820 px nie.

**Geändert**
- `style.css`: `.lr-jw-ecke { transform-origin: 100% 100%; }` – der Sticker wächst von seiner rechten unteren Ecke aus nach links. Danach 0 von 8 Messdurchläufen mit Querrollen, KJ §0 einzeln 10 von 10 grün (vorher 7 von 10).
- Wettlauf beim Hauptknopf (Punkt 2/3 des Auftrags), unabhängig vom wackligen Test, aber echt:
  - `lernSchrittKnopf` war sofort mit dem Ziel des Servers (`vorher`, z. B. `#/reise/1` oder `…-erklaeren-1`) antippbar und hatte den Stadtnamen schon im Text. Bis zur Antwort konnte ein Tippen woanders hinführen als der fertige Schritt. Mit verzögerter Karte nachgewiesen: auf 0.93.4 zeigte der Knopf „Weiter“ nach dem Test 43 ms nach dem Start antippbar `#/reise/1` statt `#/lerneinheit/1-2-ueben-2-start`.
  - Neu: Der Knopf steht sofort sichtbar da, aber gesperrt (`lr-schritt-wartet`, `aria-disabled`, ohne `href`, Antippen wird abgefangen), Text nur „Weiter“. Er wird erst mit dem fertigen Ziel frei. Bei Fehler, ohne Stände der Karte oder bei `ohne` gilt wie bisher das Ziel vom Server.
  - `lernReiseKarte`: Antworten älterer Abrufe werden verworfen. Eine Antwort ersetzt die gemerkte Karte nur, wenn seit ihrem Abruf nichts vergessen wurde und keine neuere Antwort da ist. Vorher konnte eine langsame alte Antwort Namen und Stände auf den alten Stand zurücksetzen.
  - Reisekarte und Abflugtafel, die mit der gemerkten (alten) Karte gezeichnet sind: Hauptknopf, „Gerade dran“ und Einsteigen bleiben sichtbar, aber gesperrt und ohne Stadtname (`lr-ziel-offen`), bis die frische Karte da ist. Dann wird neu gezeichnet; kommt keine, wird der Knopf frei. Die Abflugtafel zeichnete vorher mit alter Karte gar nicht neu.
  - Wechsel des Kindes war schon geschützt (`viewGuard`: Hash und Zeichen-Nummer). Geprüft, nichts geändert.
- Version 0.93.5 (`app.js`, `lernen/schule.js`, `index.html`, `lernen/index.html`, `sw.js`, Erwartungen in `tests/search.test.cjs`), Cache v179 → v180.

**Tests**
- Hilfe in `setup`: `verzoegerungJe(aktion, daten)` verzögert einzelne Antworten des nachgestellten Servers.
- Neu: „WT: Hauptknopf erst antippbar, wenn sein Ziel feststeht …“. Ein Beobachter im Browser prüft alle 15 ms jeden Hauptknopf: entweder gesperrt ohne Ziel und ohne Stadtname oder das fertige Ziel. Den ersten wartenden Knopf tippt er an, das darf nicht navigieren.
  - Karte 800 ms und Übersicht 800 ms: Knopf nach bestandenem Test und anschließend die Reisekarte.
  - Wechsel Kind 1 → Kind 2 während Kind 1 lädt (Karte und Konto 900 ms), Reisekarte und Abflugtafel: nie ein Ziel von Kind 1, Kopf von Kind 2.
  - Auf 0.93.4 rot (s. o.), auf 0.93.5 grün.
- KJ §0 unverändert. Der Test hat zu Recht angeschlagen.

**Gesamtläufe** (`node --test tests/lernen.test.cjs`)
- Vor der Änderung (0.93.4): Lauf 1 202/202, Lauf 2 202/202 (parallel zu Messläufen). Lauf 3 202/202, aber während dieses Laufs habe ich `style.css` schon geändert; er zählt nicht sauber als Lauf auf 0.93.4. Im Gesamtlauf kam der Fehler also nicht wieder. Nachgewiesen ist er einzeln (3 von 10, Wortlaut oben).
- Nach der Änderung (0.93.5): zweimal hintereinander 203/203 grün.

**Offen / nicht geprüft**
- `tests/search.test.cjs` „PWA installiert vollständige Offline-Hülle …“ ist rot, auch auf dem unveränderten Stand 8ae84ee: Der Test öffnet fest den Cache `:v143`. Das war schon vorher kaputt, ich habe es nicht behoben. Nur die Versionsnummern darin sind auf 0.93.5 gesetzt.
- Nicht auf echten Geräten geprüft, nur Chromium im Test. Weitere Stellen mit Plopp-Animation am Rand (z. B. Sticker auf der Startkarte der Reisekarte `.rk-schwebe-karte`) bekommen dieselbe Regel, sind aber nicht einzeln vermessen.
- Gesperrter Knopf bei langsamem Netz: Das Kind sieht bis zur Antwort nur „Weiter“ (gedimmt). Bei sehr langsamer Verbindung wirkt das wie ein toter Knopf. Eine Zeitgrenze gibt es nicht; bei Fehler wird er mit dem Server-Ziel frei.
- Keine neuen Vorschau-Bilder.

**Annahmen**
- „Ohne Stadtname“ heißt: Der wartende Knopf zeigt nur „Weiter“; Reisekarte und Tafel blenden die Texte von Startknopf, „Gerade dran“ und Einsteigen aus, die Flächen bleiben sichtbar.
- Der Wackler des Gesamtlaufs vom 24.11. hatte dieselbe Ursache. Die Meldung von damals ist nicht erfasst; belegt ist es nur durch dieselbe Stelle im Test und die Messung.
