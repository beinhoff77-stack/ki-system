# Grafik-Bericht Entwurf 2 (Advent)

Stand 28.11.2026 · grafische Überarbeitung von `../entwurf1`. Konzept, Abläufe, Texte und Regeln sind unverändert, siehe `../entwurf1/konzept.md` und `../entwurf1/umsetzung1.md`. **Kein App-Code**, nichts eingespielt.

## Aufbau
- `index.html` ist der Entwurf: eine Datei, ohne Netz. Die Zustände werden per Adresse gewählt, wie in Entwurf 1.
  - Karte: `#s=karte&v=4`, `#s=karte&v=5`, `&g=nacht`, `&tag=6|24|31`, `&rm=1` (Bewegung reduzieren)
  - Neue Zustände: `#s=tuer&tag=6`, `#s=tuer&tag=24`, `#s=tuer&auf=1` (Standbild halb offen), `#s=inhalt-sterne`
- Die Datei wird gebaut: `python3 bauen.py` nimmt `../entwurf1/index.html` und hängt `teile/*.css` und `teile/*.js` an. Spätere Funktionen ersetzen gleichnamige frühere. Den Unterschied zu Entwurf 1 sieht man also vollständig in `teile/`.
- Bilder: `node bilder.cjs [filter]`, `python3 vergleich.py`, `node motive-blatt.cjs $PWD/index.html bilder/motive-uebersicht.png 1`.
- Bilder der unveränderten Zustände (v1–v3, Hinweiszeile, Menü, Eltern-Blätter) liegen nur in `../entwurf1/bilder/`.

## Vorher → nachher

### A. Weihnachts-Ebene (v4 / v5)

| Element | vorher | nachher |
|---|---|---|
| Mützen | gleiche Form auf allen 26–36 Pins, alle im gleichen Winkel, schwebend; in Benelux/Balkan ein roter Klumpen | Eine gezeichnete Mütze mit Kegelschatten, Glanzkante, Fellrand mit Flausch-Kante, Bommel und Kontaktschatten. Sitzt auf dem Kopfrand, Flagge frei, Winkel −6…−32° je Pin. Regel: nur große Pins (390: 10 Mützen, 1280: 11); kleine oder bedrängte Pins bekommen ein weißes Schneehäubchen (16 bzw. 24). Abzeichen und Beschriftungen bleiben frei. |
| Lichterkette | gerade Linie, bunt gewürfelte Ellipsen, Glow per Filter, 2 Reihen | Kettenlinie mit durchhängenden Bögen, Haken stecken in der Schneehaube. Fassungen, Glasbirnen mit Lichtpunkt, weicher Radial-Glow (nachts deutlich stärker). Feste Folge Gold-Rot-Warmweiß-Grün. |
| Schnee | 70 gleiche weiße Kreise, im Hellen mit grauem Rand | 3 Tiefen: hinten 34 kleine, Mitte 15, vorn 5 große unscharfe (1280: 70/30/9). Vorgezeichnete Sprites, im Hellen ein zarter Schattenrand, doppelte Auflösung. |
| Schneehaube / Eiszapfen | weiße Wellenkante, Dreiecke mit Rand | Unregelmäßige Haube mit blauer Schattenkante, Unterschatten und Glanzlinie. Eiszapfen verjüngt, mit Verlauf und Glanzstrich, nur unter den tiefen Stellen und nicht über Sonne oder Knöpfen. Wehe unten rechts mit zwei Hügeln, Glanz und Funkeln. Haube auf „Gerade dran“ mit Hügeln oben, im Nachtmodus auf 1280 vor dem Jugendwort-Schild beendet. |
| Schlitten | Ellipsen-Rentiere ×1,75, klobig | Scherenschnitt-Illustration: zwei Rentiere im Flug (Beine gestreckt, Geweih, Glöckchen), Schlitten mit Kufen-Schnörkel, Sack mit Paketen, Goldzügel, Funkenspur. Im Hellen dunkelbraun, nachts mondhell. ~90 px breit (390). Flugbahn entlang der Route, Neigung ±16°. |
| Tannen / Geschenke | Grundformen mit weißem Rand | Tanne in 3 Etagen mit Schattenhälfte, Schneekanten, Kugeln und Stern. Pakete in 2,5D (Deckel, Seitenschatten, Band, Schleife) mit Bodenschatten. Bei 390 ~18 px hoch, lesbar. |
| v5 Nordlicht | 3 Flächen, Mischmodus über allem | 4 weiche Bänder (Grün, Türkis, Violett, Rosa) plus feine Vorhang-Strahlen, zur Sonne hin ausgeblendet. |
| v5 Tönung | färbte Pins, Flaggen und Namen bläulich | Liegt jetzt wie in der App **unter** Pins und Namen. Im Standbild werden Pins, Abzeichen, Sonne, Knöpfe und die Schrift der Namen aus dem Bild wieder darübergelegt (Schrift per Helligkeitsmaske, also ohne Kästen). |
| v5 Stern | Vierstern mit Strahl neben dem Pin | Stern mit 4 langen und 4 kurzen Strahlen, Goldschatten, Halo und weichem Lichtkegel zum Pin. Ersetzt auf dem aktuellen Pin die Mütze. |
| 6.12. | kleiner Stiefel aus Rechtecken | Stiefel mit Fellstulpe, Schattenseite, Goldtalern und Zuckerstange, auf freier Fläche neben dem Ziel. |
| 24.12. | Schlitten mittelgroß, Punktlinie | Schlitten ×1,9 auf einem Bogen quer über die Karte, Glitzerspur aus zwei Punktreihen; im Standbild über der Nordsee. |
| 31.12. | 3 gleiche Strahlenkreise | 3 Bouquets mit verjüngten Strahlen, hellem Kern, fallenden Funken und Steigspur, auf freiem Meer. |

### B. Türen und Inhalte

| Element | vorher | nachher |
|---|---|---|
| Tür | Rechteck mit Neon-Rand, Zahl kursiv | Gezeichnete Klappe: Lack mit Fase, zwei vertiefte Füllungen, Stanzlinie, Messing-Scharniere links, Messingknauf, Satin-Schleife, Zahl als Goldprägung. Rahmen als Vertiefung. |
| Krampus-Tür | rote Neon-Tür mit dünnen Hörnern | Dunkles Holz mit Maserung, Eisenbänder mit Nieten, geriffelte Hörner, eingeritzte Kratzer, Eisenring, Schwanzspitze schaut seitlich heraus. Zahl beinfarben. |
| Tür 6 / Tür 24 | wie normal | Tür 6 mit Stiefel am Knauf. Tür 24 als Festtür in Nachtblau mit Goldschleife, Sternmuster und blauer Szene. |
| Öffnen | `rotateY` 0,7 s | Klappe schwingt mit leichtem Nachschwingen (0,62 s). Die Klappe wird beim Aufgehen dunkler, das Licht dahinter fächert in Strahlen auf. **Standbild** für „Bewegung reduzieren“: `#s=tuer&auf=1`. |
| Gutschein | Karte mit gestrichelter Linie und farbigen Halbkreisen | Echtes Ticket: ausgestanzte Kerben (Maske, passt auf jeden Hintergrund), Lochreihe, Guilloche-Untergrund, Blindprägung „ADVENTSKALENDER · 2026“, Nummer „07/24“, Abriss mit Sternen. |
| Nur Sterne | – (nicht gezeichnet) | Goldmünze mit Rändelrand und Prägestern, „+500 ★ GUTGESCHRIEBEN“. |
| Jackpot | 3 weiße Kästchen mit roten Sternen | Samt und Goldrahmen, gewölbte Walzen mit Goldsternen und angeschnittenen Nachbarn, Gewinnlinie, „JACKPOT“ als Goldfolie (einmaliger Glanz). |
| Niete | grauer Kasten mit Stempel | Grauer Abriss-Schein mit Zackenkante, Gummistempel mit Fehldruck, Trost-Stern mit Pflaster und Schmollmund neben „+1 ★“. |
| Krampus-Karte | rote Karte | Dunkler, leicht schiefer Zettel. Kopf mit Krallen-Kratzern, gezeichneter Krampus (frech, zwinkert, Besen, To-do), Lochreihe, Hufabdruck. Wirkt wie eine kleine Pflicht, nicht gruselig. |
| Karte 6 / 24 | Goldrand | Goldrahmen mit Verlauf und Innenlinie, neue Motive mit Goldband „6. / 24. DEZEMBER“. |
| Kalender | graue Kacheln in einer Tabelle | Dunkelgrüne **Tafel** mit 24 Papier-Klappen (Fase, Stanzlinie, Schatten). Zustände: **offen** = Fach mit Inhalt und aufgeklapptem Flügel links · **bereit** = Goldfolie mit Schleife und Puls · **heute** = grüne Klappe mit Goldzahl und Schleife · **nachholen** = orange gestrichelt mit Uhr · **morgen** = dunkleres Papier mit Mond · **zu** = Papier. Legende angepasst, nachts gedämpftes Papier. |
| Meine Gutscheine | Karten mit Goldrand | Tickets mit Kerben und Lochreihe. **angefragt** = blauer Kopf und Stempel „ANGEFRAGT“ · **heute nicht** = warmer Abriss mit Text · **eingelöst** = grau, durchgestrichen, Stempel „EINGELÖST“, unten. „Vom Krampus“ als dunkler Zettel mit Hufabdruck. |
| Motive | 6 ausgearbeitet, 10 Skizzen, 3 Sonder | **Alle 19 neu in einem Stil** (16 + Krampus, Nikolaus, Heiligabend), siehe `bilder/motive-uebersicht.png`. Die Eltern-Seite „Motiv-Vorrat“ zeigt sie; dort ist nur der Zähl-Satz angepasst. |

## Bewusst gelassen
- Szenen-Hintergründe der Tür-Ansicht, Blatt, Knöpfe, Sticker, Kopfzeilen, Kalender-Kopfkarte – das sind App-Bausteine (`lr-ab-*`).
- Varianten v1–v3, Hinweiszeile in „Gerade dran“, Menü, Eltern-Seiten außer dem Motiv-Vorrat.
- Alle Texte. Neu sind nur zwei Zustände, die das Konzept schon beschreibt („Nur Sterne“, Tür halb offen), und Stempelwörter auf Gutscheinen, die den bestehenden Status wiederholen.

## Einbau – was sich gegenüber `umsetzung1.md` ändert
Die Fundstellen bleiben gültig (`ebenen.fest`, `ebenen.fest_unter`, `festRand`, `lernAdventTuerZeigen`, `LERN_ADVENT_MOTIVE` usw.).

**Karte:**
- Neue Zeichenfunktionen aus `teile/karte2.js` übernehmen: `festMuetze`, `festHaeubchen`, `festLichterkette`, `festHaube`, `festWehe`, `festTanne`, `festPaket`, `festSchlitten`, `festStern`, `festNordlicht`, `festStiefel`, `festFeuerwerk`, `festLauf`.
- `KARTEN.namen`, `knoepfe` und die Bildmaske für v5 sind **nur für das Standbild** nötig. In der App liegt die Tönung in `ebenen.fest_unter` zwischen Land und Routen, das löst das Problem ohne Maske.
- **Mützen-Regel:**
  - braucht Pin-Radius, Abzeichen-Flag und die Belegungsliste `belegt` (Namen-Kästen) aus `zeichneOben`;
  - Mützen-Kästen kommen in `belegt`, damit die Namen ausweichen.

**Tür:** `tuerSvg(nr, sorte)` als SVG-Text in der App ablegen (≈ 6 kB). Der Knopf bleibt `button` mit `aria-label`. CSS `.rahmen2/.klappe/.licht2` statt `.rahmen/.flug`.

**Inhalte:** `gutscheinKarte`, `jackpotKarte`, `nieteKarte`, `sterneKarte`, `krampusKarte` plus CSS aus `teile/tuer2.css`. Die Kerben brauchen `mask-composite` (Chromium und Safari ab 15.4 ok; sonst ohne Kerben).

**Kalender:** Markup `.tafel > .tueren2 > .td2` und Klassen aus `teile/u_kalender2.css`.

**Motive:**
- `M2` aus `teile/v_motive2.js` mit den Helfern (`ML`, `MR`, `FU`, `MU`, `PAKET`, `BAND`, `LICHTER`) als `daten/advent-motive.js`;
- zusammen etwa 45 kB unkomprimiert.

**Aufwand (Bau-Chat), zusätzlich zu den Schätzungen in Entwurf 1:**

| Bereich | Aufwand |
|---|---|
| Karte v4/v5 | +2–3 h (Mützen-Regel mit `belegt`, Schnee-Sprites, gemeinsame Schleife) |
| Tür und Inhalte | +2 h |
| Kalender und Gutscheine | +1–1,5 h |
| Motive | +1 h (nur Übernahme; die Stufe-2-Position „10 Skizzen ausarbeiten“ entfällt, −3–4 h) |
| **Summe** | ungefähr **+3–4 h** gegenüber Entwurf 1 |

## Leistung (Karte, älteres Handy)

| Variante | CSS-animierte Knoten | rAF-Schleifen | SVG-Knoten der Ebene (390 / 1280) |
|---|---|---|---|
| v4 | 3 (Lampen-Gruppen) | 1 (Canvas-Schnee + Schlitten-Transform) | ≈ 460 / 640 |
| v5 | 5 (+ Nordlicht, Stern-Halo) | 1 | ≈ 650 / 900 |
| 31.12. | +3 (Feuerwerk, 3 Durchläufe, dann still) | – | – |

- **v4:** 5 bewegte Knoten.
- **v5:** 7 bewegte Knoten.
- **Bewegung reduzieren:** 0 bewegte Knoten.
- **Bei `document.hidden`:** keine Zeichenarbeit.

## Schwächen, die bleiben
- **Unschärfe-Filter:** Das Nordlicht wird per `transform` verschoben und hat einen Unschärfe-Filter. Chromium zeichnet den Filter dabei neu. Auf sehr alten Handys deshalb besser das Nordlicht still lassen (nur Deckkraft animieren) oder als HTML-Ebene mit CSS-`filter` bauen.
- **Freistellung v5:** Im Standbild ist v5 nur nachgestellt. Um Namen bleibt ein sehr feiner, ungetönter Saum. In der App entfällt das.
- **Mützen bei Beschriftungen:** Auf 390 haben DE, CH und BE wegen ihrer Beschriftungen nur ein Häubchen. Das ist gewollt (Beschriftung hat Vorrang), sieht aber unregelmäßig aus.
- **Schlitten:** Bei 390 ist er im Flug ~90 px breit und überfliegt kurz Pins. Das ist so gedacht, im Standbild aber sichtbar.
- **Motive:** Das Känguru ist anatomisch vereinfacht. Krampus- und Karten-Motive sind auf 108 px (Krampus-Karte) eher klein.
- **320 × 640:** Tür und Karten werden per `zoom` verkleinert. Sticker („Das crazy“, „Süper!“) können dort Text berühren, wie schon in Entwurf 1.
- **„Bewegung reduzieren“ an der Tür:** Es gibt keine Bewegung. Das Standbild wird im Entwurf nur über die Adresse gezeigt; im Ablauf geht es direkt zum Inhalt.
