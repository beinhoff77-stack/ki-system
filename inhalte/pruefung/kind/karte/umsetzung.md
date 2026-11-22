# Vorgabe „Reisekarte“ – Kinder-Startseite mit echter Landkarte

Stand 22.11.2026. Entwurf zum Anklicken: `entwurf/reisekarte.html` (oben umschaltbar: Welt / Europa / Italien, Tag/Nacht, Handy/Rechner; Stand des Kindes erfunden). Bilder: `bilder/`. Grundlage: `inhalte/reise/briefing-gestalter.md` (Zweig `lernen-app`). Nur Vorgabe, kein App-Code.

**Entscheidungen Sebastian (22.11.):** echte Karte statt Anzeigetafel, kein Google Maps · Land-Zeichen **Flaggen-Pin** · Startknopf **in der Karte** · Strecke im Land als **dezente gezeichnete Linie** (kein Straßenverlauf) · **keine eigene Karte für Eltern/Lehrer** (dort bleibt „Unser Lehrplan“).

Leitregel: Die Karte zeichnet alles **aus den Daten** – keine feste Zahl an Kontinenten, Ländern oder Städten, nichts von Hand platziert. Neue Länder/Städte/Fächer kommen ohne Umbau dazu.

## 1 Aufbau der Startseite
- Oben: Titel „Meine Reise“, Sterne-Zähler.
- Darunter die **Pfad-Zeile** mit kleiner Ebenen-Beschriftung über jedem Teil: `WELT › KONTINENT › LAND` → „🌍 Welt › Europa › 🇮🇹 Italien“ (runde Flaggen-Plakette). 📍 markiert die eigene Position. Rechts „📍 Zu mir“ (springt zum aktuellen Land/zur aktuellen Stadt).
- Darunter die Karte, volle Breite und Höhe.
- **Startknopf in der Karte:** schwebende Karte unten (Rand 12 px, abgerundet, leicht durchscheinend): Zeile „GERADE DRAN · **Bologna** in Italien · Natürliche Zahlen · Stadt 5 von 13“, rechts „3/6“ mit 6 Strichen; darunter der gelbe Knopf „**Weiter in Bologna ›**“ (Unterzeile: Etappen-Titel). Der Knopf führt wie heute (Check-in zuerst, wenn fällig – die Check-in-Ansage aus WD sitzt als eine Zeile über dem Knopf in dieser Karte, siehe Nachprüfung 0.87.0 S1).
- **Start-Ansicht:** der Kontinent des aktuellen Flugs, eingezoomt auf die eigene Länder-Route (Platz für die schwebende Karte unten einrechnen).
- **Rechner ab 1100 px:** Karte links, rechts Spalte 360 px mit „Gerade dran“ + Startknopf, darunter angetipptes Land und „Meine Route · Länder“ bzw. „Städte in …“.

## 2 Drei Ebenen
| Ebene | zeigt | Wechsel |
|---|---|---|
| **Welt** | Kontinente in ihrer Farbe, Name groß in Großbuchstaben, darunter Mathe-Gebiet und „3/13 Länder“; Antarktis mit „Expeditionen · 0 von 21 Stationen“; Punkt „hier bist du“. Beim Hineinzoomen alle Länder als Flaggen-Pins mit Namen und Hauptstadt. | Kontinent antippen → Kontinent |
| **Kontinent** | Alle Länder mit Grenzen und Flaggen-Pin (auch Länder ohne Flug). Länder mit Flug farbig nach Zustand (§4), Reise als Bögen zwischen den Pins. | Land mit Flug antippen → Blatt → „Städte in … ansehen ›“ |
| **Land** | Das Land hell mit blauem Rand, Nachbarländer gedämpft mit Namen; Städte der Reise als nummerierte Haltestellen, dezente Linie dazwischen; Hauptstadt-Pin. | Pfad-Zeile zurück |
- Verschieben mit Finger/Maus, Zoomen mit zwei Fingern, Mausrad, „+ / − / ⤢“. Zoom geht stufenlos; die Ebene wechselt nur über Antippen bzw. Pfad-Zeile.

## 3 Zeichensprache – Kontinent, Land, Hauptstadt, Stadt unterscheidbar
| Was | Zeichen | Schrift |
|---|---|---|
| **Kontinent** | Farbfläche | Name sehr groß, Großbuchstaben, weit gesperrt |
| **Land** | **Flaggen-Pin**: runder Kopf = Flagge (rund ausgeschnitten, weißer Rand, Schatten), Nadel-Spitze = **genaue Lage der Hauptstadt** | Schild rechts neben dem Kopf: **LANDNAME** (Großbuchstaben, fett, gesperrt), darunter *Hauptstadt* (klein, kursiv, grau) |
| **Stadt der Reise** (nur Land-Ebene) | abgerundetes Quadrat mit Nummer / ✓ / ★ | Name normal, fett |
| Kür-Stadt | gestricheltes Quadrat | „Siena · Kür“ grau |
- **Farbe der Nadel = Zustand des Landes** (§4). Länder ohne Flug: kleine graue Nadel, kleinere Schrift.
- Ländergrenzen deutlich: Tag warmgrau `#8F8775`, Nacht `#5D738A`, 1,15 px, unabhängig vom Zoom gleich dick.
- Beschriftungen bleiben beim Zoomen gleich groß (gegen den Zoom skaliert).

## 4 Zustände
**Land** (Fläche + Nadel + Abzeichen oben rechts am Pin-Kopf):
| Zustand | Fläche | Nadel / Abzeichen |
|---|---|---|
| gerade dran | hellblau, Rand blau | blau, Puls an der Spitze, kleines Flugzeug |
| im Plan | hellgelb | gelb, Abzeichen mit Platznummer |
| offen | hell | dunkel |
| gesperrt | schraffiert | grau, Flagge blass, Abzeichen 🔒; Blatt nennt den Grund („ab Klasse 9“, „Visum fehlt: erst …“) |
| geschafft | hellgrün | grün, Abzeichen ✓ – Legende „**✓ geschafft – noch in Wiederholung**“ |
| golden | gold | gold, Abzeichen ★ – Legende „**★ golden – alles sitzt**“; Blatt: „Alle Städte sind abgelegt. Hier musst du nichts mehr wiederholen.“ |
| „Kann er“ (Eltern gesetzt) | wie geschafft, ohne Stempel-Abzeichen | grün, Abzeichen ◉ |
**Stadt** (Land-Ebene): ★ gold = abgelegt · ✓ grün = gelandet · ✓ grün + gelbes ↻ = heute wiederholen · blau groß mit Puls, Flugzeug, „Bologna · 3/6“ = hier bist du · weiß mit Nummer = kommt noch · gestrichelt = Kür.
**Kontinent** (Welt): „3/13 Länder“; Kontinent des aktuellen Flugs mit Punkt.
**Antarktis:** eigener Bereich unten in der Welt-Ebene, Stationen erst beim Antippen (eigene Ansicht später).

## 5 Linien
- **Länder-Route** (Kontinent): Bögen zwischen den Pin-Köpfen in der Reihenfolge des Plans, 2 px, dezent: geflogen grün durchgezogen, kommt noch gelb gepunktet.
- **Städte-Route** (Land): leicht gebogene Linie zwischen den Haltestellen, gleiche Farben; zur Kür-Stadt grau gepunktet. **Kein Straßenverlauf** (Sebastian).
- Plan wechselt den Kontinent: am Kartenrand ein Hinweis „Danach: ✈ Usbekistan (Asien) ›“; in der Welt-Ebene die ganze Route über die Kontinente.
- Geteilte Themen: siehe §11.

## 6 Beschriften nach Zoom (wichtig fürs Handy)
- Reihenfolge: Länder mit Flug immer; übrige nach Fläche – große zuerst. Pin-Kopf erscheint ab ca. 60 px² Landfläche auf dem Bildschirm (Welt: 250), Schild (Name + Hauptstadt) ab ca. 2 200 px² (Welt: 2 500).
- **Überdeckung:** Ein Schild, das einen anderen Pin-Kopf oder ein wichtigeres Schild berührt, wird weggelassen (Vorrang: Länder mit Flug, dann Fläche). Im Entwurf noch nicht vollständig – im Bau sauber lösen.
- Welt auf dem Handy: startet als Ausschnitt um den aktuellen Kontinent.

## 7 Antippen – Blatt (Handy von unten, Rechner in der Spalte)
Kopfzeile „LAND“, Plakette + Name, „◉ Hauptstadt: Athen · Kontinent Europa“; bei Flug: „✈ Teilbarkeit · 7 Städte“, Zustand mit Platz/Grund; Knopf „Städte in … ansehen ›“. Ohne Flug: „Hier gibt es (noch) keinen Mathe-Flug.“ Der Startknopf bleibt unverändert beim aktuellen Flug.

## 8 Daten und Quellen
| Was | Quelle | Lizenz (vor Bau prüfen) |
|---|---|---|
| Ländergrenzen | Natural Earth 1:50 m (npm `world-atlas`) | gemeinfrei / Paket ISC |
| Landesteile (Australien, Neuseeland, Hawaii …) | Natural Earth Admin-1 1:10 m, vereinfacht | gemeinfrei |
| Flaggen | npm `flag-icons` (SVG) | MIT |
| Ländernamen deutsch | npm `i18n-iso-countries` | MIT |
| Hauptstädte | npm `countries-list`; Lage und deutsche Namen aus GeoNames | MIT / CC BY 4.0 – Quellenangabe auf der Info-Seite |
| Städte der Reise | `aufbau-vorschlag.json` + Koordinaten aus GeoNames | CC BY 4.0 |
- **Fehlt noch (Daten-Schritt, `reise-aufbau`/`lehrplan-lb`):** Breite/Länge je Stadt der Reise und je Antarktis-Station; deutsche Hauptstadt-Namen vollständig aus GeoNames (Entwurf: rund 60 von Hand); je Flug `iso` + `region` (vorhanden).
- **Technik (Vorschlag):** Karten vorab im Build zu SVG-Pfaden rechnen (d3-geo, nur Werkzeug, nicht in der App), je Kontinent eine Datei (≈ 0,3–0,5 MB), Welt grob (1:110 m) + fein beim Hineinzoomen; Flaggen als kleine Bilder erst beim Anzeigen laden. Kein Kartenserver, keine Schlüssel, funktioniert mit schwachem Netz (zwischengespeichert).
- **Kartendaten und Belegung getrennt** (spätere Fächer: gleiche Karte, eigene Belegung).
- Nicht verwendete Gebiete (Krisen-/strittige Gebiete, Liste im Vorschlag) werden gezeichnet, aber ohne Flug.

## 9 Gestaltung
- Tag: Meer `#CFE4EF`, Land hell `#FBF9F4`, fremde Kontinente `#E3DED1`; Nacht wie die App-Nacht (Meer `#0F2233`, Land `#243444`). Zustandsfarben wie §4 (gleiche Bedeutung wie in „Unser Lehrplan“: blau = dran, gelb = Plan, grün, gold).
- Bewegung: Puls am aktuellen Ort (1,8 s, „weniger Bewegung“ → aus); beim Wechsel der Ebene weich zoomen (≤ 0,5 s).
- Bedienbar ohne Karte: Pfad-Zeile, Blatt und „Meine Route“-Liste (Rechner) enthalten alles; Pins sind Knöpfe mit Text („Italien, Hauptstadt Rom, gerade dran“).

## 11 Teile und Zusatz (Entscheidung Teilung, 22.11., 16:20)
Ein geteiltes Thema = mehrere Flüge = mehrere **Nachbarländer** (Land je Teil liefert `reise-aufbau`). Heute 6 Themen → 15 Teile; Kurzflüge mit 2 Städten sind erlaubt. Keine feste Zahl annehmen.

- **Karte (Kontinent):** jedes Teil-Land ist ein normaler Flaggen-Pin mit eigenem Zustand. Die Länder eines Themas verbindet eine **feine Kette**: dünne graue Linie Pin-Kopf zu Pin-Kopf, kleine Kettenglied-Punkte, unter der Reise-Route (nicht farbig, damit sie nicht wie eine geflogene Strecke aussieht). Am Pin-Kopf links unten ein kleines Zahl-Abzeichen **„1/2“, „2/2“** (neben dem Zustands-Abzeichen oben rechts).
- **Pin-Schild:** bleibt LAND + Hauptstadt (keine Mathe-Wörter auf der Karte).
- **Blatt (Antippen):** „✈ **Terme umformen – Teil 2 von 2**“, darunter der Untertitel; Zeile „Teil 1: 🇰🇿 Kasachstan ✓ · Teil 2: 🇰🇬 Kirgisistan (hier)“ – Länder antippbar (springt hin). Gesperrt durch Teil 1: „Erst Teil 1 in Kasachstan“.
- **Zusatz** (in der Schulart des Kindes kein Pflichtstoff): Pin mit **„+“-Abzeichen** in Sandfarbe, Landfläche hell mit gestricheltem Rand; Blatt: „**Zusatz** – freiwillig, für Entdecker. Muss nicht sein.“ Sperrt nichts; zählt nicht in „3/13 Länder“ des Kontinents (Anzeige dort: „3/13 Länder · +1 Zusatz“).
- **Gerade dran / Startknopf:** „Bologna in Italien · Natürliche Zahlen“ wird bei Teilen zu „… in Kirgisistan · Terme umformen – Teil 2 von 2“ (Untertitel nur im Blatt).
- **Route (Land-Ebene):** unverändert je Teil; am Ende der letzten Stadt ein dezenter Hinweis-Pfeil „Teil 2 geht weiter in Kirgisistan ›“, wenn der nächste Teil existiert.
- **Stempel (Reisepass):** ein Stempel je Teil, rund wie bisher, unten im Stempelrand klein **„TEIL 2/2“**; nachgetragene Stempel tragen das Datum der Teilung und das Wort „nachgetragen“ (einmalige Nachbuchungs-Karte wie FP-3: „Neuer Stempel: Terme umformen – Teil 2 von 2“). Golden je Teil.
- **Meine Route 5–10 / Listen:** „Terme umformen · Teil 2 von 2“ mit Untertitel klein; Zusatz mit Marke „Zusatz“.

## 10 Prüfen nach dem Bau
(zusätzlich: Thema mit 3 Teilen, ein Zusatz-Teil, ein nachgetragener Stempel)
400 / 820 / 1280, 360 × 640; Tag und Nacht; Startknopf immer sichtbar, Karte hinter der schwebenden Karte verschiebbar; Kontinent mit 1 und mit 19 Ländern; Land mit 3 und 14 Städten; ein Land je Zustand; Thema in zwei Ländern; Beschriftungen ohne Überdeckung; Ladezeit Kontinent < 1 s bei gutem Netz; Testkind und erfundene Daten.
