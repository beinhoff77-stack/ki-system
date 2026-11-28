# Gestaltungs-Durchsicht der ganzen Lern-App

Designer, 28.11.2026. Stand `lernen-app` 615962e (App-Version 0.96.0). Kein App-Code geändert.

**Kennzeichnung in diesem Bericht:**
**[B]** am Bild gesehen · **[C]** nur aus dem Code geschlossen · **[L]** an der laufenden App gemessen · **[M]** meine Meinung

**Wie ich vorgegangen bin.** Der Zweig `helfer-bilder` lag beim Beginn der Arbeit nicht vor (`refs/heads/helfer-bilder` gibt es nicht), darum habe ich alle Bilder selbst gemacht: Server nachgebaut über das Setup aus `tests/lernen.test.cjs`, Chrome, 390 px und 1280 px, hell und dunkel, erfundene Beispieldaten, Kinder heißen „Kind A/B". 129 Bilder in `bilder-designer/` (die Bilder des Helfers liegen in `bilder/`). Zusätzlich habe ich am gerenderten DOM gemessen: 290 sichtbare Knöpfe und Links, 51 Kartenflächen, 66 Überschriften, 778 Textknoten auf 18 Seiten. Die Zahlen in Teil 2 sind Messwerte, keine Schätzungen.

**Was ich nicht im Bild habe** (Mock fehlt oder Zustand nicht erreichbar): `wiederholen`, `zugaenge`, einzelne Expedition, Flug-Test, Landung mit Stempel, Knobel-Bordkarte, Wiederholungs- und Mischkarten, „Ändern lassen" aufgeklappt, „Einstellen je Kind". Diese Seiten sind unten mit **[C]** beurteilt. Fragen dazu stehen am Ende.

---

## 1. Gesamturteil

Die App ist **nicht aus einem Guss, aber sie ist auch nicht schlecht gebaut** – sie besteht aus drei Welten, die jede für sich stimmig sind und untereinander fast nichts teilen: der Kinderbereich (creme, schwarze Karten, Gelb als Akzent, Großbuchstaben-Reiter), der Lehrerbereich (weiß-grau, Dunkelgrün als Akzent, Pillen-Filter) und das Regel-Universum (weiß, bunte Gebietskreise, schwarzer Umschalter, Brotkrume). Die drei größten Baustellen sind: **erstens die Kopfzeile**, die auf fast jeder Seite anders aufgebaut ist und den Menü-Knopf an drei verschiedene Stellen setzt; **zweitens die Knöpfe**, von denen ich auf 18 Seiten 89 verschiedene Erscheinungsformen gemessen habe, mit vier verschiedenen Farben für „dieser Reiter ist aktiv"; **drittens die Schrift**, 31 verschiedene Größen im sichtbaren Text, davon 261 Textknoten unter 13 px. Das Regel-Universum ist der am saubersten gestaltete Teil und taugt als Vorbild für den Rest. Die Prüfung an der laufenden App (Nachtrag unten) hat zwei Dinge ergeben, die kein Standbild zeigt: Knöpfe geben beim Antippen fast nie eine Rückmeldung, und auf zwei Seiten wartet man sechs Sekunden auf nichts als das Wort „Lade …“. Der Lehrerbereich ist in sich am konsequentesten, wirkt aber wie ein Verwaltungswerkzeug neben einer Kinder-App – und er hat als einziger Bereich **keine dunkle Ansicht**.

---

## 2. Bestandsaufnahme der Bausteine

Gemessen am gerenderten DOM bei 390 px auf 18 Seiten. **[B]**

### 2.1 Knöpfe, Reiter und Links

| Maß | Befund |
|---|---|
| sichtbare Knöpfe/Links | 290 |
| **verschiedene Erscheinungen** (Radius + Polster + Größe + Fettung + Hintergrund + Rand) | **89** |
| Eckenradien | **11**: 0 · 8 · 9 · 10 · 11 · 12 · 14 · 50 % · 99 · 999 · „0 0 18 18" |
| Schriftgrößen | **17**: 12 · 12,5 · 13 · 14 · 14,4 · 15 · 15,2 · 16 · 16,5 · 16,8 · 17 · 18 · 20 · 22 · 24 · 32 |
| Hintergrundfarben | **17** |
| Tippflächen unter 44 px hoch | **83 von 290 (28 %)** |

**Was mir auffällt**
- `99px` und `999px` stehen nebeneinander, beide heißen „ganz rund". Dazu `50%`. Drei Schreibweisen für dasselbe. **[B]**
- 8 · 9 · 10 · 11 · 12 · 14 px sind sechs Radien, die man nebeneinander nicht unterscheiden kann. Sie sind nicht gewählt, sie sind entstanden. **[M]**
- 14,4 · 15,2 · 16,8 px sind rem-Rechnungen (0,9 · 0,95 · 1,05 rem), keine gestalterischen Entscheidungen. **[B]**
- **Vier Farben für „aktiv":** Gelb (Kind-Reiter „Üben", „Mein Merkheft", „Stand/Kontinente/Reisepass"), Dunkelgrün (Lehrer-Reiter „Überblick", Filter „Alle", „Gymnasium"), Schwarz (Regel-Universum „Aufbau", Klassenfilter), Gelb-umrandet-weiß (Menüeintrag „Abflugtafel"). **[B]**

**Mein Vorschlag:** Auf **fünf** Knopfarten eindampfen – Hauptknopf (gefüllt, Akzentfarbe des Bereichs), Nebenknopf (weiß mit Rand), Textlink (unterstrichen, keine Fläche), Reiter (eine Aktivfarbe für die ganze App), Marke/Pille (nicht antippbar, nur Zustand). Zwei Radien: 12 px für Flächen, 999 px für Pillen und Reiter. Drei Schriftgrößen: 14 / 16 / 18 px. **[M]**

### 2.2 Karten

| Maß | Befund |
|---|---|
| sichtbare Kartenflächen | 51 |
| **verschiedene Erscheinungen** | **20** |
| Eckenradien | **8**: 8 · 9 · 10 · 11 · 12 · 14 · 18 · 19 |
| Schatten | manche mit, die meisten ohne – ohne erkennbare Regel **[M]** |

18 px und 19 px stehen direkt nebeneinander, ebenso 9 px und 10 px. **[B]** Mein Vorschlag: zwei Kartenarten – große Fläche (19 px, Schatten) und eingebetteter Kasten (12 px, kein Schatten, nur Rand). **[M]**

### 2.3 Überschriften

| Stufe | gemessene Größen | Befund |
|---|---|---|
| H1 | 18,4 · 20 · 20,8 · 24 · 26 · 28 px | sechs Größen für dieselbe Stufe |
| H2 | 13 · 17,6 · 22 · 24 · 34 px | fünf, Spanne 13–34 px |
| H3 | 10,5 · 16 · 18 · 18,72 px | vier |

**Die Stufe sagt nichts über die Größe.** Ein H3 mit 18,7 px ist größer als ein H2 mit 13 px; ein H3 mit 10,5 px ist die kleinste Überschrift der App. Ein H2 steht einmal mit Schriftstärke 400 (gar nicht fett) bei 34 px, ein anderes mit 900 bei 13 px. **[B]** Für Vorleseprogramme ist das zusätzlich ein Problem, weil die Stufen die Gliederung nicht mehr abbilden. **[M]**

### 2.4 Schrift insgesamt

**31 verschiedene Größen** im sichtbaren Text: 9 · 9,5 · 10 · 10,5 · 11 · 11,5 · 11,67 · 12 · 12,48 · 12,5 · 13 · 13,12 · 13,33 · 14 · 15 · 15,2 · 16 · 16,8 · 17 · 17,6 · 18 · 18,72 · 19 · 19,2 · 20 · 22 · 24 · 26 · 28 · 34 px. **[B]**

**261 Textknoten stehen unter 13 px**, 114 davon unter 11 px. Zum Vergleich: Im Regel-Universum-Entwurf habe ich 13 px als Untergrenze gesetzt und halte sie ein. Auf dem Handy eines Zehnjährigen sind 9,5 px sehr wenig. **[M]**

### 2.5 Farben und Symbole

- In `style.css` stehen **881 verschiedene rohe Farbwerte** (direkt geschriebene `#…`, nicht über Variablen). Die Datei deckt die ganze Hauptapp ab, nicht nur die Lern-App – aber auch der Lern-Teil schreibt Farben überwiegend direkt hin. **[B]**
- `style.css` hat **6212 Zeilen** und enthält **46 verschiedene Eckenradien** und **108 Schreibweisen für Schriftgrößen** (49 davon in px, der Rest in rem/em). **[B]**
- Symbole sind gemischt: SVG-Pfade (Stern, Stempel), Unicode-Zeichen (≡ ✕ ‹ › ★ ⓘ ◉ ↻ ▶ ⛯ ❄ ✎), und Emoji (📒 Mein Merkheft). Drei Stile nebeneinander. **[B]** Emoji sehen auf jedem Gerät anders aus; in einer App mit eigener Bildsprache fallen sie auf. **[M]**
- `!important` kommt bei Schriftgrößen und Radien mehrfach vor – ein Zeichen, dass Regeln sich gegenseitig überschreiben. **[B]**

### 2.6 Die drei Bereiche nebeneinander

Bild: `vergleich-drei-bereiche.jpg` (Reise · Lerneinheit · Regel-Universum · Lehrer-Start · Kind-Überblick).

| | Kinderbereich | Regel-Universum | Lehrerbereich |
|---|---|---|---|
| Hintergrund | Creme | Weiß | Creme/Weiß |
| Akzent | Gelb | Schwarz + bunte Gebietsfarben | Dunkelgrün |
| Reiter aktiv | gelb gefüllt | schwarz gefüllt | grün gefüllt |
| Kopfzeile | Titel links, kein Zurück auf der Startseite | Zurück + Werkzeugleiste (Suche, Merkheft, ≡) | Zurück + „Abmelden" |
| Schrift | groß, Großbuchstaben-Reiter | gemischt, Festbreite für Formeln | klein, viele Filterzeilen |
| dunkle Ansicht | ja (3 Gestaltungen) | ja | **nein** |

**Das sind erkennbar drei Apps.** Ein Kind, das aus der Lerneinheit ins Regel-Universum springt, wechselt die Farbwelt und die Bedienlogik mit. **[M]**

---

## 3. Seite für Seite

### Einstieg

**Anmeldung** (`#/`, abgemeldet) · Bild `anmeldung-390-hell.jpg`
*Passt:* Eine Karte, ein Feld, ein Knopf, klarer Text („Gib deinen Lern-Code ein."). Die einzige Seite ohne Ablenkung. **[B]**
*Fällt auf:* Das Eingabefeld zeigt `XXXX-XXXX-XXXX` als Platzhalter, formatiert aber erst beim Absenden – beim Tippen sieht man nicht, ob man richtig liegt. **[C]** · Die Fehlermeldung erscheint als kleiner grauer Text unter dem Knopf, in derselben Zeile wie „Prüfe …". **[C]**
*Vorschlag:* Strich automatisch beim Tippen setzen; Fehler in Rot mit Symbol statt grau. **[M]**

**Startseite des Lehrers „Was ist los?"** (`#/lernen`) · Bild `start-lehrer-390-hell.jpg`, `-1280-`
*Passt:* „Zu tun" oben mit farbigen Punkten (rot/gelb/blau) und einer Zeile je Fall – das ist der beste Einstieg der App, man weiß sofort, was ansteht. **[B]**
*Fällt auf:* Die Seite heißt im Kopf „Lernen Schule", die Überschrift darunter „Was ist los?" – zwei Namen für dieselbe Seite. **[B]** · „Abmelden" steht als auffälliger Knopf oben rechts, auf jeder Lehrer-Seite; das ist die Aktion, die man am seltensten braucht. **[B]** · Die Kinderkarten wiederholen „Lernt: 0 Lerntage diese Woche · zuletzt 14.11." in Rot und darunter „Wackelt: 1 Etappe" in Gelb – zwei Warnfarben übereinander in einer Karte. **[B]**
*Vorschlag:* Ein Name für die Seite. „Abmelden" ins Menü. In der Kinderkarte nur die dringendste Zeile farbig. **[M]** (Zu dieser Seite läuft der eigene Entwurf `inhalte/design/lehrer-start/entwurf1/` – deshalb hier nur am Rand.)

### Kind

**Reisekarte** (`#/reise/<id>`) · Bilder `reise-390-hell.jpg`, `reise-menue-390-hell.jpg`
*Passt:* Die schwarze Abflugtafel mit „R O M" gesperrt gesetzt ist ein starkes Bild und sofort als „hier geht's los" lesbar. Der Fortschrittsstreifen mit Flugzeug darunter ist klar. **[B]**
*Fällt auf:* **Der Menü-Knopf ≡ steht zweimal auf der Seite** – oben rechts als eigener Kasten und unten als „≡ Menü". **[B]** · Darunter stehen fünf verschiedene Bedienelemente untereinander: zwei Pillen („◎ 0 Stempel", „Abflug, wann es dir passt"), zwei unterstrichene Textlinks, zwei Aufklapper („▸ Später – für höhere Klassen (1)", „▸ Was kommt wann wieder?"). Sechs Formen für sechs Ziele. **[B]** · Der Sticker „Yurr, Digga!" fällt aus der Tonlage der ganzen App. **[B]** Ob das gewollt ist, kann ich nicht beurteilen – es ist der einzige Jugendsprache-Einsprengsel, den ich gesehen habe. **[M]** · Im Menü steht „Dunkle Ansicht" – dieselbe Einstellung gibt es im Reisepass unter „Gestaltung" mit drei Knöpfen. Zwei Orte, eine Einstellung. **[B]**
*Vorschlag:* ≡ nur einmal, oben rechts. Die sechs Elemente auf zwei reduzieren (eine Knopfzeile, ein Aufklapper). Gestaltungswahl nur im Reisepass. **[M]**

**Mein Weg · Stand** (`#/weg/<id>-stand`) · Bild `weg-stand-390-hell.jpg`
*Passt:* Die drei Haltestellenlinien (Gymnasium / Realschule / IB MYP) sind eine gute Idee, weil sie drei Schularten nebeneinander zeigen, ohne zu werten. **[B]**
*Fällt auf:* Sehr viel Zahlenwerk für ein Kind: drei Kästen mit Prozentbalken, drei Linien mit je 6 Haltestellen, drei Zahlen-Kacheln („0 kann ich / 1 gerade dran / 1 kommen noch"), dazu „GYM 5 / RS 5 / noch kein MYP-Jahr". Das ist Lehrer-Information auf einer Kinderseite. **[M]** · Die Haltestellen zeigen „–" statt einer Zahl, wenn nichts da ist; „0 %" und „–" nebeneinander bedeuten verschiedene Dinge, erklärt wird es nicht. **[B]**
*Vorschlag:* Für das Kind eine Linie (die eigene Schulart), die anderen hinter „Andere Schularten ansehen". **[M]**

**Mein Weg · Kontinente** (`#/weg/<id>-kontinente`) · Bild `weg-kontinente-390-hell.jpg`
*Passt:* Gliederung nach Kontinenten ist eingängig und passt zum Reisebild. **[B]**
*Fällt auf:* Reiterzeile ist hier gelb-aktiv, im Lehrerbereich grün-aktiv, im Regel-Universum schwarz-aktiv. **[B]**

**Mein Weg · Karte** (`#/weg/<id>-karte`)
*Befund:* **Diese Adresse gibt es nicht mehr** – sie leitet auf `#/reise/<id>` um. Im Auftrag ist sie als Reiter genannt. **[B]** (Im Testcode steht dazu „altes Design: dort gibt es den Reiter Karte noch".)
*Vorschlag:* Aus der Liste streichen oder die Umleitung dokumentieren. **[M]**

**Reisepass** (`#/reisepass/<id>`) · Bild `reisepass-390-hell.jpg`
*Passt:* Drei Zahlenkacheln (Stempel, Sterne, Lerntage) sind klar. „Belohnungen" mit „Einlösen"-Knopf ist verständlich. **[B]**
*Fällt auf:* Die Kopfzeile sagt „Reisepass", die Überschrift darunter „Mein Weg" – der Reisepass ist ein Reiter von „Mein Weg", aber die Seite nennt sich anders als ihr Kopf. **[B]** · Unten steht „Gestaltung" mit drei Knöpfen „Abflug dunkel / Abflug hell / Bisheriges Design". **Drei parallele Gestaltungen** schleppt die App mit; „Bisheriges Design" ist ein altes Design, das weiter gepflegt werden muss. **[B]** · „Noch kein Stempel. Den ersten gibt es, wenn du alle Flüge eines Ortes geschafft hast." – guter leerer Zustand, einer der wenigen. **[B]**
*Vorschlag:* „Bisheriges Design" abkündigen. Kopfzeile und Überschrift angleichen. **[M]**

**Meine Route** (`#/route/<id>`) · Bild `route-390-hell.jpg`
*Fällt auf:* Die Seite zeigt im Testaufbau nur „Die Route ist bald da." mit einem sehr großen gelben Knopf „Zur Abflugtafel" – der Knopf ist größer als die Aussage. **[B]** Ob das der normale Zustand ist oder meinem Nachbau geschuldet, kann ich nicht sagen. **[C]** · Auch hier wieder „≡ Menü" unten zusätzlich zum ≡ oben. **[B]**

**Wiederholen** (`#/wiederholen/<id>`) · **kein Bild**
*Befund:* In meinem Nachbau fehlt die Antwort für `schule_wiederholung`, die Seite fällt auf die Fehlerseite. **[C]** Beurteilung steht aus – Frage am Ende.

**Expeditionen (Kind)** (`#/stationen/<id>`) · Bild `stationen-390-hell.jpg`
*Passt:* 21 Stationen als Kreisraster mit Namen (Palmer, McMurdo, Amundsen-Scott …) – schön und übersichtlich. **[B]**
*Fällt auf:* Alle 21 Kreise zeigen dasselbe Schloss-Symbol, gestrichelt, grau. Eine Seite, auf der nichts erreicht ist, sieht aus wie eine Seite, auf der nichts passieren kann. **[M]** · Die Stationsnamen brechen um („Amundsen-Scott", „Princess Elisabeth") und sind 9,5–10 px klein. **[B]**
*Vorschlag:* Die nächste erreichbare Station hervorheben („als Nächstes"), damit das Raster eine Richtung bekommt. **[M]**

**Einzelne Expedition** (`#/expedition/…`) · **kein Bild** **[C]**
Im Code: eigene Karte mit Stempel-Symbol, Tipp-Knopf (`lr-knopf-zweit`) und Rückmeldung in `lr-rueck`. Benutzt dieselben Knopfklassen wie die Lerneinheit – das spricht für einheitliches Verhalten. **[C]**

**Merkheft** (`#/merkheft/<id>`) · Bild `merkheft-390-hell.jpg`
*Passt:* Klare Gliederung nach Kontinent und Ort, Zeilen mit „sitzt"-Marke und Pfeil. **[B]**
*Fällt auf:* Oben eine Reiterzeile „Regel-Universum | Mein Merkheft" – das Merkheft gehört damit zum Regel-Universum, steht aber auch im Reise-Menü. Zwei Wege zur selben Seite, ohne dass der Zusammenhang erklärt wird. **[B]** · Eigenes Suchfeld „Suchen, z. B. runden"; das Regel-Universum hat ein zweites Suchfeld „Suchen". **Zwei Suchen mit verschiedenem Umfang.** **[B]** · Der Eintrag „Welchen Wert hat eine Ziffer?" erscheint zweimal (Rom und New York) – ohne Unterscheidung sieht es wie ein Doppel aus. **[B]**

### Lernen selbst

Bilder: `le-erklaeren` · `le-ueben` · `le-tipp` · `le-rueckmeldung` · `le-fehler` (je 390/1280, hell/dunkel)

**Lerneinheit · Erklärung**
*Passt:* „BORDKARTE 1 · ROM" als Kopfzeile der Aufgabe ist ein schönes Bild und hält das Reisethema durch. **[B]**
*Fällt auf:* **Drei Navigationselemente in der oberen Ecke**: „‹" (Zurück) in der Kopfzeile, „≡" darunter rechts, „✕" darunter links. Alle drei führen weg. **[B]**

**Lerneinheit · Üben**
*Passt:* Die Aufgabe steht groß, die Stellenwertkästchen (T H Z E) sind klar, die Zifferntastatur unten ist gut erreichbar und hat „,"- und „−"-Taste. **[B]**
*Fällt auf:* Zwischen Aufgabe und Tastatur steht der gestrichelte Kasten **„✎ Ändern lassen"** – mitten im Übungsfluss, an derselben Stelle, an der sonst die Rückmeldung erscheint. Für ein übendes Kind ist das eine Einladung zur Ablenkung. **[M]** · Die Reiterzeile „ERKLÄREN | ÜBEN 5 | FEHLER 1" steht in Großbuchstaben; alle anderen Reiter der App in Normalschrift. **[B]**

**Lerneinheit · Tipp**
*Fällt auf:* Der Tipp erscheint in einem grünen Kasten mit dem Zusatz „(zählt nicht als eigene Lösung; unterbricht deine Folge nicht)" – ein Klammersatz mit zwei Fachbegriffen („eigene Lösung", „Folge") an der Stelle, an der ein Kind gerade nicht weiterweiß. **[B] [M]**

**Lerneinheit · falsch beantwortet**
*Fällt auf:* Die Rückmeldung („Noch nicht – du hast einen zweiten Versuch. Tipp: Denk an die Stellenwerttafel.") steht **unterhalb** des Tipp-Kastens, nicht bei der Aufgabe – und **wiederholt den Tipp wörtlich**, der zwei Zeilen darüber schon steht. **[B]** · Die eingegebene Zahl bleibt in den Kästchen gelb stehen; es gibt keine Markierung, welche Ziffer falsch war. **[B]**
*Vorschlag:* Rückmeldung direkt an die Aufgabe, Tipp nicht doppeln. **[M]**

**Lerneinheit · richtig beantwortet** · **[C]**
Im Code `lr-rueck lr-rueck-ok`, grüner Kasten, gleiche Stelle wie die Fehlermeldung. **[C]**

**Lerneinheit · Fehler-Reiter** · Bild `le-fehler-390-hell.jpg`
*Fällt auf:* Ein Kasten „Achtung: Die 0 hält einen Platz frei." und ein Knopf „Erklärung ansehen" – darunter die halbe Seite leer, ganz unten „≡ Menü". Mager für einen eigenen Reiter. **[B]**

**Bordkarten (Wiederholungs- und Mischkarten), Knobel-Bordkarte, Flug-Test, Landung** · **kein Bild** **[C]**
Im Code: eigene Klassen `lr-bordkarte`, `lr-knobel`, `lr-abschluss-bordkarte`, Stempel-SVG und Sterne-Anzeige. Die Knobel-Rückmeldung heißt „★ Geknackt!" bzw. „Diesmal nicht – das war eine harte Nuss." – der Ton passt zum Kinderbereich. **[C]** Beurteilung der Gestaltung steht aus – Frage am Ende.

### Regel-Universum

Bilder: `ru-aufbau` · `ru-klassen` · `ru-gebiet` · `ru-tafel` · `ru-suche`, Übersicht `vergleich-regel-universum.jpg`

**Sonnensystem · Aufbau** (`#/regeln/<id>`)
*Passt:* Die gelbe Sonne mit „14 Rechenregeln" und die sieben Gebiete mit farbigen Kreisen sind der klarste Einstieg der ganzen App. Jedes Gebiet nennt die Zahl seiner tragenden Ideen. **[B]**
*Fällt auf:* Der Umschalter „Aufbau | Durch die Klassen" ist **schwarz** aktiv – vierte Aktivfarbe der App. **[B]** · Auch hier „≡ Menü" unten zusätzlich zum ≡ in der Werkzeugleiste. **[B]**

**Sonnensystem · Durch die Klassen**
*Passt:* „Dieselben 14 Rechenregeln in Klasse 5 bis 10" mit Klassenfilter und gelb umrahmter wirkender Stelle – genau das, woran wir in den letzten Runden gearbeitet haben, und es trägt. **[B]**

**Gebiet / einzelne Regel**
*Passt:* Brotkrume „‹ Universum › Sonne › Schicht 1", Merksatz im gelben Kasten, Zeichnung, „Dieselbe Regel in Klasse 5 bis 10" als Aufklapper. Durchgehend einheitlich. **[B]**

**Tafeln** („Formeln auf einen Blick") · Bild `ru-tafel-390-hell.jpg`
*Passt:* Tabelle mit Figur, Umfang, Flächeninhalt; aufklappbare Zeile mit Zeichnung und Bezeichnungsliste. Sauber. **[B]**
*Fällt auf:* Der Klassenfilter heißt hier **„bis Klasse 5 6 7 8 9 10 alle"**, bei „Durch die Klassen" **„Klasse 5 6 7 8 9 10"** – andere Beschriftung, anderer Umfang (einmal mit „alle"), gleiche Optik. **[B]** · „Drucken" steht als kleiner unterstrichener Textlink ohne Symbol – die einzige Druckfunktion, die ich gesehen habe, und sie sieht aus wie eine Fußnote. **[B]**

**Suche** · Bild `ru-suche-390-hell.jpg`
*Passt:* „16 Treffer für „Dreieck"" mit Quelle je Treffer (Tafeln · Formeln …, Geometrie › Deckungsgleich) – gut lesbar, Festbreitenschrift für die Formeln. **[B]**
*Fällt auf:* Ein Treffer ist schwarz umrandet (vermutlich der genaueste), ohne dass erklärt wird, warum. **[B]**

**„Ändern lassen"** · **kein Bild** (aufgeklappt nicht erreicht) **[C]**
Im Code: `details`-Aufklapper mit `summary` „✎ Ändern lassen", derselbe an Erklärung, Etappe, Bordkarte, Flug und Plan. Dass es überall derselbe ist, ist gut. **[C]** Dass er im Kinderbereich mitten in der Übung steht, ist das Problem (siehe Lerneinheit). **[M]**

### Lehrer und Eltern

Bilder in `vergleich-lehrer.jpg` und einzeln.

**Kind-Ansicht · Überblick** (`#/kind/<id>-ueberblick`) · Bild `kind-ueberblick-390-hell.jpg`
*Passt:* Kind-Umschalter als Pillen (A, B, T) oben – schneller Wechsel ohne Umweg. „GERADE DRAN" im blauen Kasten mit Fortschrittsbalken ist sofort lesbar. **[B]**
*Fällt auf:* Fünf Kästen untereinander mit je eigener Rahmenfarbe (blau, weiß, rot-links, weiß, weiß) und verschiedenen Radien. **[B]** · „…" als dritter Knopf neben den Kind-Pillen, ohne Beschriftung. **[B]**

**Kind-Ansicht · Was wackelt** (`#/kind/<id>-wackelt`) · Bild `kind-wackelt-390-hell.jpg`
Dazu liegt bereits die eigene Vorgabe `inhalte/design/wackelt/umsetzung.md` vom 27.11. vor (Voranalyse statt Rohdaten). Hier nur: Die Seite beginnt mit einem Fließtext-Absatz („Diese Woche: 30 Bordkarten (Aufgabe), 22 richtig, 4-mal mit Tipp …") statt mit Zahlen oder Befund. **[B]**

**Kind-Ansicht · Lehrplan** (`#/kind/<id>-lehrplan`) · Bild `kind-lehrplan-390-hell.jpg`
*Fällt auf:* Kopfzeile mit „Fahrplan · 2", „Alle Themen", „Filter ▾", „ⓘ", „↶ Rückgängig", „Gym Kl. 5" – sechs Bedienelemente in einer Zeile bei 390 px. **[B]**

**Lehrplan** (`#/lehrplan`) · Bild `lehrplan-390-hell.jpg`
*Fällt auf:* **Vier Filterzeilen und eine fünfzeilige Legende**, bevor der erste Inhalt kommt: Schulart-Pillen, Suchfeld, Haken „Kurzbeschreibung", Status-Pillen („Alle / fertig 1 / in Prüfung 1 / fehlt 3"), Lernstand-Pillen („Aus / Kind A / Kind B / Beide vergleichen"), dann fünf Legendenzeilen mit farbigen Rahmen. **[B]** Auf dem Handy ist der halbe Bildschirm Steuerung. **[M]**
*Vorschlag:* Filter hinter einen Knopf „Filter (2)", Legende hinter „ⓘ". **[M]**

**Alle Kinder im Vergleich** (`#/schulstand/<id>`) · Bild `schulstand-390-hell.jpg`
*Fällt auf:* „Einstieg prüfen: aus / Kl. 6 / Kl. 7 / Kl. 8 / Kl. 9 / Kl. 10" – sechs Pillen in zwei Zeilen, darunter eine Tabelle mit zwei Spalten und fünf Legendenfarben. Dicht, aber für ein Werkzeug vertretbar. **[B] [M]**

**Expeditionen (Lehrer)** (`#/expeditionen`) · Bild `expeditionen-390-hell.jpg`
*Fällt auf:* Kurze Seite, im Wesentlichen ein Erklärtext. Könnte ein Abschnitt in „So funktioniert's" sein. **[M]**

**Meine Aufträge** (`#/lernauftraege`) · Bild `lernauftraege-390-hell.jpg`
*Passt:* Filter „Offen (0) / Beantwortet (1) / Alle (1)" mit Zahlen – vorbildlich, weil man sieht, was sich lohnt. Die Antwort steht im grünen Kasten unter dem Auftrag. **[B]**
*Fällt auf:* Der Knopf „▸ ✎ Neuer Auftrag (allgemein)" ist ein gestrichelter Aufklapper – dieselbe Form wie „Ändern lassen" im Kinderbereich, gut. **[B]**

**So funktioniert's** (`#/info`) · Bild `info-390-hell.jpg`
*Fällt auf:* Eine **Textwüste**: lange Absätze mit Fettungen am Anfang, keine Bilder, keine Beispiele, keine Sprungmarken. Die Seite erklärt eine farbcodierte Oberfläche ausschließlich in Worten („rot: seit 3 Tagen kein Lerntag …; gelb: eine Etappe wackelt …; blau: ein Wunsch eines Kindes"). **[B]**
*Vorschlag:* Jeden Absatz mit dem Bildausschnitt bebildern, den er beschreibt; Inhaltsverzeichnis oben. **[M]**

**Zugänge** (`#/zugaenge`) · **kein Bild** – siehe Fehlerzustand unten. **[C]**

**Einstellen je Kind** · **kein Bild** **[C]**
Erreichbar über „⚙ Einstellen" auf der Lehrer-Startseite. Im Code: Formular mit Schulart, Klasse, Pausen. **[C]**

### Seiten, die im Auftrag fehlen – im Code gefunden **[B]**

| Adresse | Befund |
|---|---|
| `#/weltkarte` | eigene Ansicht `viewWeltkarte`, im Auftrag nicht genannt |
| `#/inhalte` | **leitet auf `#/lehrplan` um** – zwei Adressen, eine Seite |
| `#/lernstand/<id>` | **leitet auf `#/kind/<id>-lehrplan` um** – ebenso |
| `#/plan` | Umleitung |
| `#/rueckmeldungen` | identisch mit `#/lernauftraege` (dieselbe Funktion `viewRueckmeldungen`) |

Vier Adressen, die auf andere Seiten zeigen. **[B]** Das ist für Lesezeichen gut und für die Pflege schlecht, weil jede Umleitung mitgedacht werden muss. **[M]**

### Überall

**Kopfzeile** – **der größte Einzelbefund.** Fünf Bauarten auf fünf Seiten: **[B]**
1. Reise: Titel links, keine Knöpfe, ≡ darunter rechts
2. Lerneinheit: „‹ Rom", darunter ≡, darunter „✕ ROM / Natürliche Zahlen"
3. Regel-Universum: „‹ Regel-Universum", darunter Werkzeugleiste (Suchen, Mein Merkheft, ≡)
4. Lehrer-Start: „Lernen Schule" + „Abmelden"
5. Kind-Ansicht: „‹" + Kind-Pillen + „…"

Der Menü-Knopf ≡ sitzt an **drei** Stellen (oben rechts als Kasten, in der Werkzeugleiste, unten als „≡ Menü"), und auf mehreren Seiten **gleichzeitig oben und unten**. **[B]**

**Versionsnummer `v0.96.0`** steht auf **jeder** Seite oben rechts, auch im Kinderbereich. Für ein Kind ohne Bedeutung, nimmt den Platz, an dem sonst der wichtigste Knopf stünde. **[B] [M]**

**Ladezustand:** `loading()` zeigt „Lade …" als Text in einem `.spinner`-Kasten, auf allen Seiten gleich. **[C]** Einheitlich, aber ohne Platzhalter – die Seite springt beim Fertigladen. **[M]**

**Fehlerzustand:** Bild `zugaenge-390-hell.jpg`. „Das hat gerade nicht geklappt. / Prüfe das Internet und versuch es nochmal." mit Knopf „Nochmal versuchen" – guter, kindgerechter Text. **[B]** **Darunter steht aber die technische Meldung im Original:** „Cannot read properties of undefined (reading 'zugaenge')". Englischer Programmiertext auf einer Seite für Eltern und Kinder. **[B]**
*Vorschlag:* Technische Meldung hinter „Einzelheiten ▸" legen. **[M]**

**Leere Zustände:** uneinheitlich. Gut: Reisepass („Noch kein Stempel. Den ersten gibt es, wenn …"). Mager: „Noch kein Flug geschafft." ohne Hinweis, was zu tun ist; „Die Route ist bald da."; Expeditionen mit 21 gleichen Schlössern. **[B]**

**Dunkle Ansicht:** Gemessen – **14 von 23 Seiten ändern sich nicht**, wenn man die dunkle Gestaltung wählt: anmeldung, expeditionen, info, inhalte, kind-lehrplan, kind-ueberblick, kind-wackelt, lehrplan, lernauftraege, lernstand, schulstand, start-lehrer, wiederholen, zugaenge. **[B]** Zusätzlich geprüft: Bei echtem Dunkelmodus des Geräts (`prefers-color-scheme: dark`) bleibt der Lehrerbereich hell (gemessener Hintergrund `rgb(246,244,236)`). **[B]** **Der Eltern- und Lehrerbereich hat keine dunkle Ansicht.**

**Tippflächen:** 83 von 290 unter 44 px Höhe (28 %). Die kleinsten: ein Link mit 17 px Höhe, zwei mit 26 px. **[B]**

**Rückmeldung beim Tippen:** Im Code gibt es `:active`-Zustände für `lr-knopf` und `btn`, aber nicht für alle Knopfklassen. **[C]** Am Bild nicht prüfbar. Frage am Ende.

---

## 4. Rein / Weg

### Rein

1. **Eine einzige Kopfzeile für die ganze App** – links Zurück, Mitte Titel, rechts genau ein Menü-Knopf. Alles andere (Suche, Merkheft, Abmelden, Kind-Wechsel) ins Menü oder in eine zweite Zeile, die überall gleich aussieht. **[M]**
2. **Eine Datei mit den Bausteinen** (Farben, Abstände, Radien, Schriftgrößen als Variablen), auf die alle drei Bereiche zugreifen – heute stehen Farben überwiegend direkt im CSS. **[M]**
3. **Dunkle Ansicht für Eltern und Lehrer**, mindestens für `prefers-color-scheme: dark`. **[M]**
4. **Gedrückt-Zustand und Ladezustand an jedem Knopf**, der etwas zum Server schickt (heute springt die Seite). **[M]**
5. **Sprungmarken und Bilder in „So funktioniert's"** – die Seite erklärt Farben in Worten, statt sie zu zeigen. **[M]**
6. **„Als Nächstes" auf der Expeditions-Seite**, damit 21 gleiche Schlösser eine Richtung bekommen. **[M]**

### Weg

1. **Die Versionsnummer aus dem Kinderbereich** – sie gehört in „So funktioniert's" oder ins Menü. **[M]**
2. **Der doppelte Menü-Knopf** („≡" oben *und* „≡ Menü" unten auf Reise, Merkheft, Expeditionen, Route, Regel-Universum). **[B] [M]**
3. **„Bisheriges Design"** als dritte Gestaltung im Reisepass – drei parallele Gestaltungen zu pflegen, kostet bei jeder Änderung dreifach. **[B] [M]**
4. **Die zweite Suche** – Merkheft und Regel-Universum haben getrennte Suchfelder mit verschiedenem Umfang; eine Suche mit Filter reicht. **[B] [M]**
5. **Die doppelte Gestaltungswahl** – „Dunkle Ansicht" im Reise-Menü *und* „Gestaltung" im Reisepass. **[B] [M]**
6. **Der doppelte Tipp** in der Fehler-Rückmeldung der Lerneinheit. **[B] [M]**
7. **Die technische Fehlermeldung** auf der Fehlerseite (hinter „Einzelheiten ▸"). **[B] [M]**
8. **„Ändern lassen" aus dem Übungsfluss** – ans Ende der Etappe oder ins Menü, nicht zwischen Aufgabe und Tastatur. **[M]**
9. **Zusammenlegen:** „Expeditionen (Lehrer)" ist fast nur Erklärtext → Abschnitt in „So funktioniert's". Die Adressen `#/inhalte`, `#/lernstand`, `#/rueckmeldungen` sind Umleitungen auf andere Seiten → eine Adresse je Seite. **[B] [M]**
10. **Der „…"-Knopf** neben den Kind-Pillen ohne Beschriftung. **[M]**

---

## 5. Ideen (nach erwarteter Wirkung)

| # | Idee | Aufwand | Wirkung |
|---|---|---|---|
| 1 | **Eine Kopfzeile, drei Farben.** Dieselbe Kopfzeile überall, nur die Akzentfarbe wechselt je Bereich (Gelb Kind, Grün Lehrer, Schwarz Regel-Universum). Die App wirkt sofort wie eine App, ohne dass die Bereiche ihre Eigenart verlieren. | mittel | sehr groß |
| 2 | **Knopf-Diät.** Fünf Knopfarten, zwei Radien, drei Schriftgrößen – aus 89 Erscheinungen werden fünf. Lässt sich schrittweise machen, Seite für Seite. | groß | sehr groß |
| 3 | **Eine Aktivfarbe für Reiter.** Heute vier (Gelb, Grün, Schwarz, Gelb-Rahmen). Kleinster Eingriff mit der größten Wirkung auf „ein Stil". | klein | groß |
| 4 | **Schriftstaffel 13/15/17/20/26.** Alles unter 13 px anheben, krumme rem-Werte ersetzen. Betrifft 261 Textknoten und hilft besonders den Jüngeren. | mittel | groß |
| 5 | **Der Weiter-Platz.** An jeder Kinderseite unten rechts immer derselbe Platz für „was jetzt dran ist" – heute steht dort mal „≡ Menü", mal nichts, mal ein Textlink. Das Kind lernt einen Ort statt zehn. | mittel | groß |
| 6 | **Rückmeldung an der Aufgabe.** Richtig/falsch erscheint direkt am Eingabefeld, nicht unter dem Tipp; die falsche Ziffer wird markiert. | klein | groß |
| 7 | **Platzhalter statt Springen.** Während geladen wird, stehen graue Kästen in der Form des kommenden Inhalts – die Seite springt nicht mehr. | mittel | mittel |
| 8 | **Stempel-Fortschritt statt Schlösser.** Auf der Expeditions-Seite die nächste Station hervorheben und den Weg dorthin zeichnen. | klein | mittel |
| 9 | **„So funktioniert's" bebildern.** Jeder Absatz mit dem Ausschnitt, den er erklärt – aus der Textwüste wird eine Anleitung. | mittel | mittel |
| 10 | **Ein Ort für Einstellungen.** Gestaltung, Pausen, Zugang in einer Seite statt verteilt auf Menü, Reisepass und Lehrerbereich. | mittel | mittel |

---

## 6. Reihenfolge – acht Schritte zur Einheitlichkeit

1. **Bausteine festschreiben:** Farben, Abstände, Radien (12/999), Schriftgrößen (13/15/17/20/26) als Variablen an einer Stelle. Noch nichts ändern, nur festlegen. *(Vorarbeit, ohne sichtbare Wirkung – aber ohne sie wird jeder weitere Schritt wieder uneinheitlich.)*
2. **Eine Aktivfarbe für alle Reiter.** Ein Tag Arbeit, sofort sichtbar.
3. **Kopfzeile vereinheitlichen** und den doppelten Menü-Knopf entfernen. Danach fühlt sich jede Seite wie dieselbe App an.
4. **Versionsnummer aus dem Kinderbereich** und technische Fehlermeldung hinter „Einzelheiten".
5. **Knöpfe auf fünf Arten bringen**, Bereich für Bereich: erst Kinderbereich, dann Lehrer, dann Regel-Universum.
6. **Schrift anheben**, alles unter 13 px; krumme rem-Werte ersetzen.
7. **Tippflächen auf 44 px** bringen (28 % sind heute kleiner).
8. **Dunkle Ansicht für den Lehrerbereich** und „Bisheriges Design" abkündigen.

---

## Nachtrag vom 28.11., nachmittags: an der laufenden App geprüft **[L]**

Auf Zuruf des Projektleiters habe ich die **echte App** geöffnet (Claude in Chrome, angemeldeter Lehrer-Zugang, `beinhoff77-stack.github.io/ki-system/lernen/`) und dort gearbeitet, wo Standbilder nicht hinkommen. Gearbeitet habe ich mit dem **Testkind (`#/reise/3`)**, nicht mit den Zugängen der Kinder. **Nichts geschrieben, nichts gespeichert, keine Aufgabe beantwortet.** Aus den Lehrer-Seiten stehen hier keine Namen und keine Zugangscodes, und davon ist kein Bild im Repo.

**[L]** = an der laufenden App gemessen.

### N1. Gedrückt-Zustand – die offene Frage 2 ist beantwortet **[L]**
Von den **7 Knopfklassen**, die auf den Kinderseiten sichtbar sind, hat **genau eine** (`lr-knopf`) eine `:active`-Regel. Ohne jede Rückmeldung beim Antippen – kein `:active`, kein `:hover`, kein Übergang – sind: `rk-legende-knopf`, `lr-knopf-klein`, `lr-textlink`, `rk-ru-link`, `iconbtn`, `lr-chip-stern`.
Auf dem Handy heißt das: Das Kind tippt, und bis die neue Seite kommt, passiert sichtbar nichts. Bei den unten gemessenen Ladezeiten sind das mehrere Sekunden ohne Bestätigung, dass der Tipp angekommen ist. **[M]**
*Vorschlag:* Eine gemeinsame Regel für alle Knopfklassen – beim Drücken kurz dunkler und 1 px nach unten. Ein Eintrag im CSS, wirkt überall. **[M]**

### N2. Wie lange man wartet – gemessen **[L]**
Zeit vom Antippen bis der Inhalt steht (eigene Messung in der laufenden App, je einmal, kalt):

| Seite | Ladezeit |
|---|---|
| Mein Weg · Stand | **6,3 s** |
| Merkheft | **6,7 s** |
| Regel-Universum | 3,8 s |
| Expeditionen | 2,9 s |
| Reisepass | 2,8 s |
| Meine Route | 2,5 s |
| Wiederholen (Check-in) | 2,1 s |
| Reisekarte (schon geladen) | 0,1 s |

In dieser ganzen Zeit steht nur das Wort **„Lade …"** auf der Seite – kein Fortschritt, kein Gerüst, keine Angabe, worauf gewartet wird. Dass an den Ladezeiten selbst gearbeitet wird, steht im Auftrag; die **Gestaltung des Wartens** gehört hierher: Sechs Sekunden „Lade …" fühlen sich länger an als sechs Sekunden mit einem Platzhalter-Gerüst, das schon die Form der Seite zeigt. **[M]** Das stützt Idee 7 im Bericht.

### N3. „Wiederholen" ist der Check-in – jetzt gesehen **[L]**
Die Seite, die mir im Nachbau fehlte, heißt im Betrieb **„CHECK-IN · 1 VON 4"**: vier kleine Kästchen als Fortschritt, darunter eine Aufgabenkarte mit der Herkunft („Jahreszinsen berechnen · aus Washington, D.C."), ein Eingabefeld mit Einheit („€"), ein großer gelber Knopf „Prüfen", darunter der Textlink „Pause – später weiter einchecken".
*Passt:* Der Fortschritt aus vier Kästchen ist auf einen Blick lesbar; die Herkunftszeile ordnet die Aufgabe ein. **[L]**
*Fällt auf – und das ist ein neuer Befund:* **Dieselbe Tätigkeit hat zwei verschiedene Bedienungen.**

| | Lerneinheit | Check-in, Knobel-Bordkarte, Expedition |
|---|---|---|
| Eingabe | Stellenwert-Kästchen (T H Z E) | ein einfaches Feld |
| Tastatur | **eigenes Tastenfeld** im Daumenbereich, mit „−", „,", „⌫" und einer Taste „⌨" für die Gerätetastatur | die Tastatur des Geräts |
| Prüfen | gelbe Taste **im** Tastenfeld | eigener Knopf über die ganze Breite (gemessen 1008 px bei 1920 px Fenster) |

Im Code steht das ausdrücklich: `lernAufgabe(…, { tasten: false })` an drei Stellen (Knobel-Bordkarte, Expedition und der Check-in), `{ tasten: neu }` in der Lerneinheit. **[C]** Ein Kind, das von der Etappe in den Check-in wechselt, bedient dieselbe Art Aufgabe anders. **[M]**
*Vorschlag:* Das Tastenfeld überall einsetzen, wo eine Zahl einzugeben ist. **[M]**

**Was ich dabei fast falsch gemeldet hätte:** Die Antwortfelder stehen im Quelltext mit `inputmode: 'text'`, was die Buchstabentastatur holen würde. Die Lerneinheit setzt aber zur Laufzeit `inputmode: 'none'`, sobald das Gerät einen groben Zeiger hat (`pointer: fine` ist falsch) – dort ist es also **richtig gelöst**. Nur die drei Stellen ohne eigenes Tastenfeld haben weder das eine noch `inputmode="numeric"`; dort kommt am Handy für eine Zahlenantwort die Buchstabentastatur. **[C]** Am Handy nachgesehen habe ich das nicht.

### N4. „Zugänge": eine Sperre, die wie ein Netzwerkfehler aussieht **[L]**
In meinem Nachbau hielt ich die Fehlerseite auf `#/zugaenge` für ein Artefakt meines fehlenden Server-Nachbaus. **Sie kommt auch in der laufenden App** – mit dem Zusatz „Nur Eltern". Der angemeldete Lehrer-Zugang darf die Seite nicht sehen, und das wird ihm so gezeigt:

> Das hat gerade nicht geklappt. / Prüfe das Internet und versuch es nochmal. / **[Nochmal versuchen]**

Eine Rechte-Beschränkung erscheint als Netzwerkstörung, mit einem Knopf, der nie zum Ziel führt. **[L]** Das ist der härteste einzelne Bedienfehler, den ich in der Durchsicht gefunden habe. **[M]**
*Vorschlag:* Eigene Meldung: „Diese Seite ist nur für Eltern. Mit einem Lehrer-Zugang gibt es keine Zugangscodes." Kein „Nochmal versuchen", stattdessen ein Weg zurück. **[M]**
*Allgemein:* Unterscheiden zwischen „geht gerade nicht" (Netz) und „darfst du nicht" (Rechte) – heute landet beides auf derselben Seite. **[M]**

### N5. Was gut ist **[L]**
- **`prefers-reduced-motion` wird beachtet** – wer am Gerät weniger Bewegung eingestellt hat, bekommt sie auch hier nicht. Das ist sorgfältig und in der Durchsicht sonst selten.
- Die **Brüche stehen gestapelt** auch im Check-in (2/3 in der Zinsaufgabe) – die Arbeit vom 27.11. trägt bis in diese Seite.
- Die **Reisekarte lädt aus dem Zwischenspeicher in 0,1 s** – wenn die Daten schon da sind, ist die App sofort da.

### N6. Was auch live offen bleibt
Nicht geprüft habe ich weiterhin: **Flug-Test, Landung mit Stempel und Sternen, Knobel-Bordkarte, Wiederholungs- und Mischkarten** – sie erscheinen erst, wenn man Aufgaben beantwortet, und das hätte in die Datenbank geschrieben. Der Auftrag sagt „nichts live, nichts in die Datenbank", darum habe ich es gelassen. Mit einem Wort des Projektleiters spiele ich sie am Testkind durch.
Ebenso offen: **echtes Handy** (die Fensterbreite ließ sich in Chrome nicht auf 390 px zwingen; die Live-Prüfung lief in Rechner-Breite), Safari, Firefox, Kontrastwerte.

## Fragen an den Projektleiter

1. **Bilder, die mir fehlen:** `wiederholen` und `zugaenge` sind durch die Live-Prüfung erledigt (N3, N4). Weiter offen: einzelne Expedition, Flug-Test, Landung mit Stempel und Sternen, Knobel-Bordkarte, Wiederholungs- und Mischkarten, „Ändern lassen“ aufgeklappt, „Einstellen je Kind“ – sie entstehen erst beim Beantworten von Aufgaben. **Darf ich sie am Testkind durchspielen?** Das schreibt Lernstand in die Datenbank, was der Auftrag ausschließt.
2. ~~Gedrückt-Zustand~~ – **erledigt**, siehe Nachtrag N1: von sieben Knopfklassen hat genau eine einen Gedrückt-Zustand.
3. **„Yurr, Digga!"** auf der Reisekarte – gewollte Tonlage oder Rest aus einem Versuch?
4. **„Bisheriges Design"**: Darf ich davon ausgehen, dass es abgekündigt werden kann, oder benutzt es jemand?
5. Die Weltkarte ist laut Auftrag gesetzt – gilt das auch für die **Abflugtafel** (die schwarze Karte auf der Reiseseite), oder darf ich dort Vorschläge machen?

---

# Nachtrag 2 vom 28.11.: die Bilder des Helfers ausgewertet

Antwort des Projektleiters vom 28.11., 06:10 abgearbeitet. Grundlage: Zweig `helfer-bilder` 338e0713, **376 Bilder** zu 94 Seiten und Zuständen, Liste in dessen `seiten.md`. Der Bericht oben bleibt unverändert; hier steht nur, was dazugekommen ist oder sich geändert hat.

**Hinweis zum Ordner:** Der Helfer legt seine Bilder in denselben Pfad `inhalte/design/durchsicht-2811/bilder/`, in dem meine 129 eigenen Bilder liegen. Die Dateinamen überschneiden sich nicht (seine beginnen mit einer Nummer, meine mit dem Seitennamen), aber beim Zusammenführen der Zweige liegen dann 505 Bilder in einem Ordner. **Vorschlag:** meine nach `bilder-designer/` verschieben, seine behalten den Platz. Mache ich auf ein Wort.

## A. Gedrückt-Zustand – die Tabelle (Punkt 2 der Antwort) **[B]**

Gemessen über alle Klassen, die `lernen.js` und `lernen/schule.js` an anklickbare Elemente (`button`, `a`, `summary`) hängen – **51 knopfartige Klassen**. Geprüft gegen `style.css`, einschließlich globaler Regeln.

| | Zahl | Anteil |
|---|---|---|
| mit `:active` (Gedrückt-Zustand) | **2** | 4 % |
| mit `:focus-visible` (Tastaturbedienung) | 6 | 12 % |
| mit `:hover` | 12 | 24 % |
| **ohne jede Rückmeldung** | **36** | **71 %** |

**Die ganze `style.css` (6212 Zeilen) enthält genau vier `:active`-Regeln:**

| Regel | Wirkung | Wo |
|---|---|---|
| `.lr-knopf:active` | 2 px nach unten, Schatten weg | Hauptknöpfe im Kinderbereich |
| `.lr-taste:active` | 1 px nach unten, Fläche dunkler | Tasten des Zifferntastenfelds |
| `.lr-ab-gross:active` | 4 px nach unten, Schatten bleibt | großer Knopf der Abflugtafel |
| `.rk-rahmen:active` | `cursor: grabbing` | Weltkarte – kein Knopf, nur der Mauszeiger |

Also haben **drei Knopfarten der ganzen App** einen Gedrückt-Zustand. Ein globales `button:active` gibt es nicht; globale Regeln existieren nur für `:hover` (drei Stück, Zeilen 160–162).

Ohne Rückmeldung sind unter anderem: `.lr-einsteigen-knopf` (der wichtigste Knopf des Kinderbereichs), `.lr-knopf-start`, `.lr-knopf-zweit`, `.lr-knopf-klein`, `.lr-schritt-knopf`, `.lr-pfeilknopf`, `.lr-textlink`, `.lr-ortlink`, `.lr-route-link`, `.lr-ru-link`, `.rk-weiter-knopf`, `.rk-staedte-knopf`, `.rk-legende-knopf`, `.rk-grund-knopf`, `.lw-filter-knopf`, `.lw-leg-knopf`, `.ww-link`, `.ww-link-zeile`, `.mx-link`, `.rt-link`.

**Besonders:** Nur 6 von 51 Klassen haben `:focus-visible`. Wer die App mit der Tastatur bedient, sieht auf den meisten Knöpfen nicht, wo er steht. **[M]**
*Vorschlag:* Eine Regel für alle: `.lr-knopf, .lr-taste, [class*="-knopf"], [class*="-link"], [class*="-chip"] { transition: transform .06s; }` mit `:active { transform: translateY(1px); }` und ein gemeinsamer `:focus-visible`-Ring. Ein Eintrag, wirkt auf 51 Klassen. **[M]**

## B. Die mit [C] gekennzeichneten Seiten – jetzt am Bild **[B]**

### B1. Flug-Test (06o, 06p, 06q)
*Passt:* Der Ablauf ist klar geführt. Der Start erklärt die Regeln in drei Zeilen („Eine Bordkarte je Etappe, ohne Tipps. Die Lösungen siehst du nach dem Abgeben."). Bei der Frage zeigen zwei Kreise oben, wo man steht; „Abgeben kannst du bei der letzten Bordkarte. Bis dahin kannst du Antworten ändern." nimmt die Angst. Das Ergebnis trennt sauber in einen grünen RICHTIG- und einen roten FALSCH-Kasten, beide mit Überschrift **und** Zeichen (✓/✗), nicht nur mit Farbe – das ist vorbildlich und sollte überall so sein.
*Fällt auf:*
- **Die Startseite ist fast leer**: eine Karte, drei Zeilen, ein Knopf, darunter zwei Drittel Leerraum und „≡ Menü". Für den Einstieg in eine Prüfung wirkt das unfertig. **[M]**
- Im Ergebnis stehen zwei fast gleich wichtige Knöpfe untereinander: „Erst üben: Zahlenstrahl >" (gelb) und „Gleich verbessern >" (weiß). Welcher der empfohlene Weg ist, sagt die Gestaltung – aber der erklärende Satz dazu steht weit oben in der Karte. **[M]**
- **Neuer Fehler gefunden:** Im Test-Ergebnis wird der Lösungsweg **ohne `lernMathe()`** ausgegeben (`lernen.js` Zeile 4998: `x.loesungsweg && !x.richtig ? el('p', …, x.loesungsweg)`). An allen anderen sieben Stellen der Datei steht `lernMathe(…loesungsweg)`. **Folge: Brüche im Lösungsweg erscheinen hier als „3/4" mit Schrägstrich statt gestapelt** – im Widerspruch zum Rest der App und zur Umstellung vom 27.11. **[C]**

### B2. Landungen (06h, 06i, 06j, 06r, 06s, 06t, 06u)
*Passt:* Das sind die stärksten Bilder der App. Vollbild, keine Kopfzeile, nur „Überspringen ›" oben rechts. „FLUG GESCHAFFT" in großen gelben Versalien auf Dunkelblau mit der Sternzahl; „ROM IST GESCHAFFT" als roter Stempel auf Goldbeige. Darunter jeweils eine weiße Karte mit dem, was das Kind jetzt kann, und wann es wiederkommt (3 · 7 · 14 · 30 Tage). Der Moment ist als Moment gestaltet, nicht als Seite – das ist richtig. **[B]**
*Fällt auf:*
- **Der Hauptknopf hat je nach Landung eine andere Farbe:** gelb („Weiter zum nächsten Thema") auf der Flug-Landung, dunkelrot („Weiter: neuer Ort") auf der Ort-Landung. Gleiche Rolle, zwei Farben. **[B]**
- Diese Ansichten bringen eine **vierte Farbwelt** (Dunkelblau/Gold) in die App. Für einen Belohnungsmoment halte ich das für richtig – es ist kein Ort, an dem man sich zurechtfinden muss. **[M]**

### B3. Knobel-Bordkarte (06k, 06k2) und Mischkarte (06l)
*Passt:* Die Knobel-Karte sagt vorweg, dass sie nicht zählt („zählt nicht für ‚sitzt' und nicht für den Test. Richtig beim ersten Versuch: 30 Sterne."). Das ist fair und nimmt den Druck. Die Mischkarte kennzeichnet sich kursiv mit „Aus deiner Reise – erkennst du, was gefragt ist?".
*Fällt auf:* **Beide bestätigen meinen Befund N3 am Bild.** Hier gibt es **kein Zifferntastenfeld**, sondern ein freies Eingabefeld und einen gelben „Prüfen"-Knopf über die volle Breite; der „Tipp"-Knopf steht klein darunter. In der Lerneinheit ist es genau umgekehrt: Tastenfeld im Daumenbereich, Prüfen als gelbe Taste darin. Dieselbe Tätigkeit, zwei Bedienungen – jetzt an vier Stellen belegt (Check-in, Knobel, Mischkarte, Expedition). **[B]**

### B4. Einzelne Expedition (05e)
*Passt:* Klare Gliederung: Marke „✻ EXPEDITION FREIGESCHALTET", Titel, Herkunftszeile („Neumayer-Station III · Antarktis · Station 9 von 21"), Einführungstext, dann „TEIL A VON 3" mit der Aufgabe. Dass man jederzeit aufhören kann und Erledigtes bleibt, steht ausdrücklich da. **[B]**
*Fällt auf:* Die Marke „EXPEDITION FREIGESCHALTET" ist **türkis** – eine Akzentfarbe, die sonst nirgends vorkommt. Damit sind es im Kinderbereich Gelb, Türkis, Dunkelblau und Gold. **[B]**

### B5. Einstellen je Kind (08k)
*Passt:* Als Blatt über der Seite mit ✕ oben rechts, Schulart und Klasse als Pillen – schnell zu bedienen. **[B]**
*Fällt auf – und das ist ein eigener Befund:* **Zwei der vier Abschnitte sagen nur, dass etwas nicht geht.**
> „Stand messen gegen …" → „Die Stufe je Schulart lässt sich hier noch nicht einstellen; gemessen wird an der Klasse."
> „Reisetage und Pausen" → „Reisetage lassen sich hier noch nicht eintragen."

Eine Überschrift verspricht eine Einstellung, der Text nimmt sie zurück. Das kostet die Hälfte des Blattes und enttäuscht jeden, der danach sucht. **[M]**
*Vorschlag:* Beide Abschnitte entfernen und stattdessen eine Zeile unten: „Reisetage und Stufen stellst du auf der Startseite unter ‚+ Reisetag eintragen' ein." **[M]**

### B6. Check-in und „Etappe abgelegt" (05c, 06m, 06m2, 06n)
*Passt:* „Etappe abgelegt!" ist gut gemacht – goldenes Siegel, „+30 ★ Sonder-Sterne fürs Ablegen", ein Fortschrittsbalken aus Segmenten und der Satz „4 von 7 Etappen abgelegt – noch 3, dann wird der Flug golden." Man weiß sofort, was man erreicht hat und was noch fehlt. **[B]**

### B7. Zugänge (08j) und leere Zugänge (09d3)
Die Bilder zeigen die Seite aus **Eltern**-Sicht, also die eigentliche Ansicht. Mein Live-Befund N4 bleibt davon unberührt: Mit einem **Lehrer**-Zugang erscheint statt einer Erklärung die allgemeine Fehlerseite. Der Helfer vermerkt das in seiner Liste ebenso („Lehrer hat keinen Zugang zu dieser Seite"). **[B]**

### B8. Seiten, die in meinem Bericht ganz fehlten **[B]**
Der Helfer hat Zustände aufgenommen, die ich nicht kannte: Abflugtafel in drei Fassungen (03c–03e), „Expedition freigeschaltet" auf der Reisekarte (03f), Arbeitsweisen (07d), **elf Tafeln** statt der einen, die ich sah (07f1–07f11), die Lehrer-Ansicht des Regel-Universums (07i, 07j), „Was wackelt" im Zustand „alles besprochen" (08c), Schulstand aller Kinder (08f2), Eltern-Startseite (08l) und fünf leere Zustände (09d–09d5). Sie bestätigen das Bild aus Teil 3, ohne es zu ändern; Einzelheiten nur, wo unten etwas dazu steht.

## C. Die Meldungen des Bilder-Helfers – nachgeprüft (Punkt 6 der Antwort)

| # | Meldung | Mein Befund |
|---|---|---|
| 1 | Ladeanzeige und Fehlerseite bleiben im Nachtmodus hell | **Bestätigt, gemessen.** Mittlere Helligkeit des oberen Seitenteils: Ladeanzeige hell 243 / dunkel 243, Fehlerseite hell 237 / dunkel 237 – identisch. Zum Vergleich funktioniert der Nachtmodus sonst: Reisekarte 225/51, Merkheft 237/29, Fehler **innerhalb** einer Aufgabe 231/31. Betroffen sind nur die beiden **ganzseitigen** Zustände aus `lernen/schule.js` (`loading()`, `showError()`), die gezeichnet werden, bevor die Kinderseite ihre Nacht-Klasse setzt. **[B]** Für ein Kind, das abends im Nachtmodus lernt, heißt das: bei jedem Seitenwechsel und jedem Fehler ein heller Blitz. **[M]** |
| 2 | Knopf „Heute keine Knobel-Bordkarte" im Nachtmodus weiß mit fast unsichtbarem Text | **Bestätigt** (06k-390-dunkel): heller Rahmen, Text praktisch nicht lesbar. **[B]** |
| 3 | Aufgeklappte Zeile „Kreis" in der Formel-Tafel im Dunkelmodus mit hellem Kasten | **Teilweise.** Die Tafel selbst ist korrekt dunkel; hell bleibt die **klebende Werkzeugleiste** („Suchen", „Mein Merkheft", ≡), die im Dunkelmodus als heller Balken mitten über der Tabelle steht (07f10-390-dunkel). Das ist auffälliger als die Zeile selbst. **[B]** |
| 4 | Lehrer-Seiten auf 1280 px mit rund 100 px Leerraum über dem Kopf | **Bestätigt, gemessen.** Leerraum bis zum ersten Inhalt: Lehrplan 96 px, Meine Aufträge 96, So funktioniert's 96, Schulstand 96, Lehrer-Start 97, Kind-Ansicht 55. Kinderseiten zum Vergleich: Reisekarte 8 px, Merkheft 24, Regel-Universum 24. **[B]** |
| 5 | „Meine Aufträge" auf 390 px mit zweizeiligem Kopf | **Bestätigt** (08h-390-hell): Der Titel bricht in „Meine / Aufträge", die Kopfzeile wird dadurch höher als auf allen anderen Seiten. **[B]** |
| 6 | Spitzklammern statt Anführungszeichen in „Noch 1 Etappe bis ›…‹ gelandet" | **Bestätigt** (`lernen.js` Zeile 1807: `›${n.titel}‹`). Im Bild (03c-390-hell) liest es sich als „bis >Natürliche Zahlen< gelandet" – in Space Grotesk sehen die einfachen Guillemets wie Größer-/Kleiner-Zeichen aus. In einer Kinder-App wirkt das wie Programmcode. **[B] [M]** *Vorschlag:* „…" wie überall sonst. |

## D. Jugendwort-Schild (Punkt 3 der Antwort) **[B]**

Zur Kenntnis genommen, dass es gewollt ist (`daten/jugendwoerter.json`). Das Überdecken kann ich bestätigen und genauer fassen: Auf 390 px liegt das Schild **über dem Wort „EINSTEIGEN"** und verdeckt dessen obere Hälfte vollständig (03c-390-hell: „Digga, los geht's." über dem gelben Knopf). Verdeckt wird damit ausgerechnet der einzige Knopf, der die Lernreise startet. Das kleine „?" am rechten Rand des Schildes sitzt zur Hälfte auf der Kante des Knopfes. **[B]**
*Vorschlag, falls erwünscht:* Das Schild über die **linke** Hälfte der Tafel legen (über „ROM"), wo kein Bedienelement liegt – dann bleibt der Einfall erhalten, ohne den Startknopf zu verdecken. **[M]**

## E. Was sich am Bericht oben ändert

Nichts muss gestrichen werden. Zwei Stellen werden durch die neuen Bilder **schärfer**:
1. **Teil 2.1** (89 Knopf-Erscheinungen): Die Landungen fügen zwei weitere Hauptknopf-Farben hinzu (gelb und dunkelrot in gleicher Rolle). Die Zahl steigt, die Aussage bleibt.
2. **Idee 6 „Rückmeldung an der Aufgabe"**: Der Flug-Test macht es bereits richtig (RICHTIG/FALSCH mit Überschrift, Zeichen und Begründung in einem Kasten). Das ist die Vorlage, nach der die Lerneinheit umgebaut werden sollte – nicht eine neue Erfindung. **[M]**

Und eine **neue Zeile für die Liste „Weg"**: die zwei leeren Abschnitte im Blatt „Kind einstellen" (B5).

## F. Weiter offen

- **Punkt 4 und 5 der Antwort** („Bisheriges Design" abkündbar? Vorschläge zur schwarzen Abflug-Karte?) liegen beim Nutzer. Ich habe dazu nichts ausgearbeitet, wie angewiesen.
- Weiter nicht geprüft: echtes Gerät, Safari, Firefox, Kontrastwerte, Bediengefühl in Bewegung über die gemessenen `:active`-Regeln hinaus.
- Nicht aufgenommen, auch vom Helfer nicht: Flug-Test „Gleich verbessern" (Korrektur) und Nachtragstest; „Auch offen" auf der Abflugtafel.

---

# Nachtrag 3 vom 28.11.: am Testkind durchgespielt

Freigabe des Projektleiters vom 28.11., 06:25. Gearbeitet **nur am Testkind** (`#/reise/3`, alle Adressen auf `/3` geprüft) in der laufenden App über Claude in Chrome. Nichts eingestellt, keine Aufträge geschickt, keine Wünsche bestätigt, Kind 1 und Kind 2 nicht geöffnet. Keine Namen, Codes oder Bilder echter Daten in diesem Bericht.

**[L]** = an der laufenden App gemessen.

**Durchgespielt:** eine Aufgabe falsch und richtig beantwortet (Lerneinheit „Natürliche Zahlen", Etappe 2) · Flug-Test vom Start bis zur Auswertung · „Gleich verbessern" · Check-in mit allen vier Bordkarten bis „Eingecheckt!".
**Nicht erreicht:** Landung mit Stempel, Knobel-Bordkarte und Mischkarte – sie setzen den Abschluss einer Etappe bzw. eines Ortes voraus, und die offene Etappe des Testkinds verlangt „3 richtige in Folge" aus 337 Aufgaben. Diese drei sind in Nachtrag 2 an den Bildern des Helfers beurteilt (B2, B3); ich habe sie live nicht erzwungen, weil das viele Schreibvorgänge am Testkind bedeutet hätte. **[L]**

## N3.1 Wartezeit beim Prüfen – gemessen **[L]**

| Vorgang | Zeit bis zur Rückmeldung |
|---|---|
| Aufgabe prüfen (Lerneinheit, falsch) | 833 ms |
| Aufgabe prüfen (Lerneinheit, richtig) | ~490 ms |
| Check-in, Zahl prüfen | 1 286 ms |
| Check-in, vier Felder prüfen | 643 ms |
| Flug-Test abgeben (25 Karten) | 1 377 ms |

**Berichtigung an mir selbst:** In Nachtrag 1 (N1) habe ich geschrieben, beim Antippen passiere sichtbar nichts. Für den Prüfen-Knopf stimmt das nicht: Er wird während der Wartezeit auf `disabled` gesetzt, und es gibt die Regel `.lr-knopf:disabled { opacity: 0.5 }` – der Knopf wird also blasser. **[L]**
Was fehlt, ist etwas anderes: **kein Hinweis, dass gerechnet wird.** Kein Spinner, keine Textänderung („Prüfe …"), der Knopf behält Wort und Farbe. Bei 1,3 Sekunden ist das die Stelle, an der ein Kind ein zweites Mal tippt. **[M]**
Die Aussage aus N1 gilt unverändert für die **anderen** Knöpfe: 36 von 51 Klassen haben weder `:active` noch `:hover` noch `:focus-visible`.

## N3.2 Die Rückmeldung steht zu weit unten – jetzt gemessen **[L]**

Nach dem Prüfen: Eingabefeld bei y = 516 px, Rückmeldung bei y = 693 px – **177 px darunter**, hinter dem Tipp-Kasten. Das belegt den Befund aus Teil 3 („Lerneinheit · falsch beantwortet") mit einer Zahl. **[L]**

*Inhaltlich sind die Rückmeldungen gut:*
- falsch: „Noch nicht – du hast einen zweiten Versuch. Fast – das ist nur ungefähr. Rechne genau oder runde so, wie es die Bordkarte verlangt." – erkennt, dass die Antwort *ungefähr* stimmte.
- richtig: „✓ AN BORD · +5 STERNE / Gleich beim ersten Mal gibt es 10 ★. In Dreiergruppen: 94 620." – nennt den Gewinn und was beim ersten Versuch drin gewesen wäre.
Das ist besser als die Platzierung. **[M]**

## N3.3 Flug-Test: live 25 Bordkarten statt 2 **[L]**

Im Nachbau des Helfers hat der Test zwei Bordkarten (Bild 06p), **live sind es 25** – eine je Etappe.

*Passt:*
- Die Nummernleiste (`lern-punkte`) bricht sauber um (zwei Zeilen bei 1 522 px, bei 390 px entsprechend mehr), **nichts läuft über den Rand**.
- **Die Sicherung vor dem Abgeben ist vorbildlich:** „24 Bordkarten sind noch leer. Leere Bordkarten zählen als falsch." mit den Knöpfen „Zu Bordkarte 2" und „Trotzdem abgeben". Genau so soll ein Schutz vor Versehen aussehen. **[L]**

*Fällt auf:*
- Die Nummern sind **36 × 48 px** – unter den 44 px Breite, die für sichere Tippflächen gelten, und sie liegen dicht nebeneinander. Bei 25 Stück ist Vertippen wahrscheinlich. **[L] [M]**
- **Kein Tastenfeld im Test** (`.lr-taste`-Elemente: 0), Feld `type="text"` ohne `inputmode`. Damit ist der Test die **fünfte** Stelle mit Zahleneingabe ohne das eigene Tastenfeld – nach Check-in, Knobel-Bordkarte, Mischkarte und Expedition. **[L]**
- **„Verbessern" sieht aus wie „Test".** Nach „Gleich verbessern ›" steht „VERBESSERN · BORDKARTE 1 VON 13" – gleiche Kopfzeile, gleiche Nummernleiste, gleiche Knöpfe, gleiche Hinweiszeile. Nur das eine Wort unterscheidet die beiden Durchgänge. Wer mitten drin ist, weiß nicht, worin er sich befindet. **[L] [M]** *Vorschlag:* Den Verbessern-Durchgang farblich absetzen (etwa die Nummernleiste in Gelb statt Grau) und die Zeile „Du verbesserst 13 Bordkarten aus dem Test" darüber. **[M]**

## N3.4 Das Test-Ergebnis bei einem schlechten Lauf **[L]**

Ich habe den Test mit 24 leeren Karten abgegeben – das Ergebnis war „0 von 25 richtig". Gemessen:

| | |
|---|---|
| Seitenhöhe | **7 451 px** |
| entspricht | **8,8 Handy-Bildschirmen** (bei 844 px) |
| Fehlerkästen untereinander | **25** |
| Höhe eines Kastens | 224 px |
| Zusammenfassung „fang hier an" | **keine** |

Oben stehen die 25 Etappen als rosa Marken in einem Block, darunter 25 rote Kästen mit je Frage, eigener Antwort, richtiger Antwort und Erklärung. Fachlich ist jeder einzelne Kasten gut gemacht (Überschrift, Zeichen ✗, Begründung). Zusammen ergeben sie eine neun Bildschirme lange rote Wand – für ein Kind, dem gerade alles misslungen ist, der denkbar ungünstigste Anblick. **[M]**
*Vorschlag:* Über die Liste eine Zusammenfassung setzen: „Drei Dinge zuerst: …" mit den drei Etappen, an denen die meisten Fehler hängen, und den Rest hinter „Alle 25 Rückmeldungen ansehen ▾". Die Daten dafür liegen vor. **[M]**

## N3.5 Check-in vollständig durchgespielt **[L]**

Vier Bordkarten („1 VON 4" bis „4 VON 4"), Themen aus verschiedenen Orten (Washington, Chicago, Denver, Rom), am Ende: „🧳 **Eingecheckt!** 3 von 4 richtig · +30 ★ / Eine Bordkarte kommt beim nächsten Mal wieder."

*Passt:* Der Abschluss ist knapp, nennt das Ergebnis und was mit der falschen Karte geschieht. Die Rückmeldung nach einem Fehler ist freundlich und lehrreich: „Noch nicht. Richtig ist: 1 T + 0 H + 9 Z + 7 E / 1 097 = 1 Tausender + 0 Hunderter + 9 Zehner + 7 Einer. / **Kein Problem – diese Bordkarte kommt beim nächsten Mal wieder.**" **[L]**

*Fällt auf:*
- **Bei vier Eingabefeldern (T/H/Z/E) fehlt das Tastenfeld besonders.** Vier Felder nacheinander mit der Gerätetastatur zu füllen, ist am Handy mühsam; genau dafür hat die Lerneinheit ihr Tastenfeld mit „weiter"-Logik. **[L] [M]**
- Der Erklärknopf heißt je nach Karte „Hält stabil. ?", „Safe gekonnt. ?", „Schere. ?" – die Jugendwörter aus `daten/jugendwoerter.json` stehen **im Knopf selbst**, zusammen mit dem Fragezeichen, das die Erklärung öffnet. Der Knopf trägt damit zwei Dinge auf einmal: eine Bewertung und eine Hilfe. **[L] [M]**
- Das Emoji 🧳 im Abschluss – wie in Teil 2.5 angemerkt, mischt sich damit ein dritter Symbolstil unter SVG und Unicode. **[L]**

## N3.6 Brüche sind barrierefrei richtig gelöst **[L]**

In der Check-in-Aufgabe „Von 2 400 € Erspartem liegen ¾ zu 2 %" steht der Bruch gestapelt. Im reinen Text liest er sich als „3 4", was ein Vorleseprogramm als „vierunddreißig" ausgeben könnte. **Das ist abgefangen:**

```html
<span class="lern-bruch-text" role="img" aria-label="3 durch 4"><span>3</span><span>4</span></span>
```

Ein Vorleseprogramm sagt „3 durch 4". Auch die Antwortoptionen bekommen nach dem Prüfen ein Zeichen mit `aria-label="richtig"`, also nicht nur Farbe. Das ist sorgfältiger, als die Durchsicht sonst nahelegt, und gehört ausdrücklich erwähnt. **[L]**

## N3.7 Eine mehrdeutige Aufgabenstellung – mir selbst passiert **[L]**

Check-in, Bordkarte 4: „**Zerlege 1 097 in Stellenwerte.** Trage in jedes Feld eine Zahl ein." Darunter vier Felder, beschriftet `T + H + Z + E`.
Ich habe **1000, 0, 90, 7** eingetragen – die Stellen*werte*. Richtig war **1, 0, 9, 7** – die Ziffern je Stelle. Die Rückmeldung löst es auf („1 097 = 1 Tausender + 0 Hunderter + 9 Zehner + 7 Einer"), aber die Frage selbst lässt beides zu: „Stellenwerte" meint im Wortsinn 1000 und 90, die Feldbeschriftung T/H/Z/E meint die Ziffern. **[L]**
Das ist **kein Gestaltungsfehler im engeren Sinn**, sondern eine Formulierung – gehört damit zum Mathe-Profi. Ich melde es, weil es mir beim Durchspielen selbst passiert ist und einem Kind der Klasse 5 erst recht passieren wird. **[M]** *Vorschlag an den Inhalt:* „Trage in jedes Feld die **Ziffer** ein, die an dieser Stelle steht." Oder die Felder mit „___ T" statt „T" beschriften. **[M]**

## N3.8 Was sich an den Teilen oben ändert

- **Teil 3, „Lerneinheit · falsch beantwortet":** Abstand jetzt mit 177 px belegt.
- **Nachtrag 1, N1:** berichtigt – der Prüfen-Knopf wird während des Wartens blasser; es fehlt nur der „es rechnet"-Hinweis. Für die übrigen 36 Klassen bleibt der Befund.
- **Nachtrag 1, N3 / Nachtrag 2, B3:** Die Liste der Stellen ohne Tastenfeld wächst auf **fünf** (Check-in, Knobel, Mischkarte, Expedition, **Flug-Test**).
- **Neu für die Liste „Rein":** eine Zusammenfassung über dem Test-Ergebnis (N3.4) und ein Hinweis „es rechnet" am Prüfen-Knopf (N3.1).
- **Neu für die Liste „Weg":** nichts.
