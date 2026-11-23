# Vorgabe JW – Jugendwörter in Geschafft- und Belohnungs-Ansichten

Stand 23.11.2026 · Grundlage `lernen-app` c98fffd (`lernAbschlussEtappe`, `lernAbschlussFlug`, `lernExGeschafftAnsicht`, Knobel- und Bordkarten-Rückmeldung) · Daten: `woerter.json` · Entwurf: `entwurf/jugendwoerter.html` · Bilder: `bilder/*_400|820_tag|nacht.png` · Entwurf online: Artefakt f41b44f0-f8fc-460f-85ef-2e3df5760deb

Kein App-Code, keine Datenbank, keine Namen. Alles hier ist Vorschlag für den Bau.

## 0. Kurzfassung

- **Ein Sticker, nie ein Satz in Slang.** Das Jugendwort klebt groß als schräger Sticker in der Szene. Titel („Direktflug“), Zahlen und der erklärende Satz bleiben unverändert normales Deutsch.
- **Selten und verdient.** Höchstens ein Sticker je Ansicht, Zufall nach Dosis, Tagesgrenze, kein Spruch zweimal hintereinander, kein Wort aus den letzten 4 Stickern.
- **Stärke folgt dem Ergebnis.** „PEAK“, „GOAT“, „+1000 Aura“ nur für Direktflug, Flug geschafft, fehlerfrei. Mit Tipp gibt es höchstens „Akkurat.“.
- **Das Kind entscheidet.** Erst nach einem Ja des Kindes an (Standard aus). Eltern können sperren. Jeder Sticker lässt sich antippen: Bedeutung + „Wort gefällt mir nicht“.
- **Wortliste:** 74 Wörter geprüft, 32 im Einsatz, 42 ausgeschlossen mit Grund; 53 fertige Sprüche. Halbjährliche Prüfung, Wörter mit abgelaufenem Verfallsdatum werden automatisch nicht mehr gezogen.

## 1. Recherche

**Gesicherte Fakten (mit Quelle in `woerter.json`):**
- 2026: Jugendwort „Ragebait“; Top 10: 67, Crashout, Digga, Du bist gut genug, Gute Käse, Macker, Peak, Ragebait, Schere, Süper (ZDFheute). Top 3: Crashout, Ragebait, Peak (GIGA).
- 2025: „Das crazy“ vor „goonen“ und „checkst du“; Top 10 außerdem Digga(h), lowkey, Rede, Schere, sybau, tot, tuff (SRF).
- 2024: „Aura“ vor „Talahon“ und „Schere“; Top 10 außerdem Hölle nein, Pyrotechnik, Yolo, Nein Pascal ich denke nicht, Yurr, Akh, Digga(h) (web.de, QuillBot).
- 2021–2023: cringe/sheesh/sus · smash/bodenlos/Macher (+ Gommemode, SIU, wild, Slay, Bro …) · goofy/side eye/NPC (+ Auf Lock, Darf er so, Kerl*in, Rizz, Slay, Yolo).
- Çüş: Ausruf des Staunens (boah, krass, oha), gesprochen „Tschüsch“; Nebenbedeutungen „igitt“ bzw. ursprünglich Halte-Ruf für Esel → „mach mal halblang“.

**Annahmen (in `woerter.json` mit `beleg: "Annahme …"` markiert):** W, GOAT, Locked in, Nice, krass, stabil, safe, Ohne Witz, Sigma, Skibidi, Brainrot, cooked, L, Vallah, Mashallah – gängiger Netz-Slang, aber nicht aus einer Langenscheidt-Liste und von mir nicht mit Quelle geprüft. Bei der ersten Halbjahresprüfung belegen oder streichen.

**Nicht geprüft:** Bedeutung von „Mehrzweckeier“ (2026 von der Jury ausgeschlossen) → ungeeignet.

**Pflichtwörter laut Auftrag – alle drin:** Çüş (staunen), Digga (Anrede, nur 14 und nur wenn gewählt), Peak (lob_gross), Gute Käse (lob_klein), Süper (lob), Das crazy (staunen), Schere (nur fehler_mild).

**Ausgeschlossen laut Auftrag und Prüfung** (Auszug, alle mit Grund in der Datei): Ragebait, Crashout, goonen, sybau, Talahon, smash, Hawk Tuah, AMK (Wut/Provokation, sexuell, beleidigend, abwertend) · cringe, sus, goofy, lost, NPC, side eye, L, cooked, bodenlos, tot (beschämen bei Fehlern) · checkst du (belehrend) · 67, Skibidi, Mittwoch (kein Sinn) · Akh, Vallah, Mashallah (religiöse/gruppenbezogene Formeln) · Yolo, Pyrotechnik (falsches Signal) · I bims, fly, Kerl*in (veraltet).

**Nebenbedeutungen, die den Einsatz begrenzen:** Çüş, Sheesh, wild, krass, Das crazy (können negativ/gelangweilt sein → nur nach klar gutem Ergebnis, nie bei Fehlern) · Slay („töten“ → nur 14) · Aura (nur „+1000“, nie Minus) · Peak (nie mit negativem Wort) · Macher (nur neutral „Macher-Modus“) · Bro/Digga (nur wenn das Kind es als Anrede wählt) · SIU/Gommemode (Bezug auf reale Personen → gut ausblendbar).

## 2. Einbau – wo, wie, wie oft

### 2.1 Wo genau

| Anlass (Schlüssel) | Ansicht im Code | Platz des Stickers | Stärke |
|---|---|---|---|
| `landung_direkt` | `lernAbschlussEtappe`, art `direkt` | Szene unten rechts | 3 |
| `landung_sauber` | art `sauber`, ohne Tipp, nicht „wieder“ | Szene unten rechts | 2 |
| `landung_leicht` | art `sauber` mit Tipp oder `wieder_gelandet` | Szene unten rechts | 1 |
| `landung_sturm` | art `sturm` | Szene unten rechts, unter „⚡ Ausdauer“ | 2 (Ausdauer-Ton, nie „Peak“) |
| `knobel_richtig` | Knobel-Bordkarte richtig im 1. Versuch | Szene / grüne Box | 3 (Staunen) |
| `serie_5`, `serie_10` | Bordkarten-Rückmeldung „✓ An Bord“ bei 5 bzw. 10 in Folge | in der grünen Box, unter dem Text | 2 / 3 |
| `wiederholung` | Rückmeldung „Wiederholung bestanden“ | in der grünen Box | 1 |
| `flug_geschafft` | `lernAbschlussFlug` | Szene unten rechts, nach dem Konfetti | 3 |
| `expedition_geschafft` / `_fehlerfrei` | `lernExGeschafftAnsicht` | Szene unten rechts (Polarfarben) | 2 / 3 |
| `nachbessern` | Stadt nach „wieder offen“ wieder abgelegt (3 in Folge) | Szene unten rechts | 2 |
| `fehler` | Rückmeldung „Noch nicht. Richtig ist: …“ | in der gelben Box **unter** der Lösung, klein und grau | 1 |
| `anrede` | Abflugtafel, Kopf der Ansage | Szene unten rechts | 1 |

Fester Punkt: **Der Sticker verdeckt nie Titel, Zahl, Lösung oder Knopf.** In Boxen steht er nach dem Text im Fluss (nicht darüber), in Szenen unten rechts mit eigenem Freiraum (Szene bekommt unten ~60 px Polster, wenn ein Sticker kommt). Ort-Stempel, Reisepass, Expeditions-Stempel und Test-Ergebnis bekommen **keinen** Sticker – dort steht schon ein Stempel; zwei Stempel nebeneinander wirken überladen.

### 2.2 Wie es aussieht

- Schräg (−7°), weißer Rand, kräftige Schrift, kleiner Schatten, ein „?“-Punkt unten rechts als Hinweis „antippbar“.
- Farbe nach Stärke: 3 Gold (wie das Direkt-Abzeichen), 2 Mint, 1 Hellblau-Lila; Fehler: Grau, kleiner, nur −3°, kein Plopp-Effekt.
- Erscheint 0,35 s nach der Szene mit einem kurzen Plopp (0,4 s); bei „Bewegung reduzieren“ ohne Animation.
- Lange Sprüche (> 11 Zeichen) eine Stufe kleiner; höchstens zwei Zeilen.
- Vorlesen: `aria-label="Sticker: PEAK. Tippen für die Bedeutung."`; Zeichen wie Ç bleiben (Schriftart prüfen, siehe 6).
- Tag/Nacht: Sticker-Farben gleich (sie sitzen auf der farbigen Szene); die Boxen folgen der Ansicht.

### 2.3 Wie oft (Dosis)

| Einstellung | Wahrscheinlichkeit je Anlass | höchstens je Lerntag |
|---|---|---|
| Aus | 0 | 0 |
| Selten | 25 % | 3 |
| Normal | 50 % | 6 |
| Oft | 80 % | 10 |

- Große Anlässe (Direktflug, Flug geschafft, Expedition fehlerfrei, Knobel richtig) × 1,5 – sie sind seltener und sollen öfter einen Sticker bekommen.
- Fehler × 0,5, höchstens 2 Fehler-Sticker je Lerntag, nie zwei Fehler hintereinander, **kein Fehler-Sticker ab dem 2. Fehler in Folge** (dann nur der normale Text – Frust nicht mit Witz übertünchen).
- Anrede höchstens 1× je Lerntag.
- Lerntag = derselbe Tag wie bei den übrigen Lerntag-Zählern.

### 2.4 Abwechslung

- Je Anlass ein „Sack“: Sprüche werden ohne Zurücklegen gezogen, bis der Sack leer ist.
- Nie derselbe Spruch wie der letzte Sticker (auch über Anlässe hinweg).
- Kein Wort aus den letzten 4 Stickern, solange ein anderer passender Spruch da ist.
- Wenn wegen Alter/Ausblenden kein Spruch passt: kein Sticker (nie ein Ersatzwort aus einem anderen Anlass).

### 2.5 Stärke passend zum Ergebnis

- Stärke des Spruchs = Stärke des Anlasses (Tabelle 2.1). Nie nach oben ausweichen.
- Mit Tipp, „wieder gelandet“ oder Wiederholung: nur Stärke 1 (Akkurat, Lowkey stark, W, Hält stabil).
- Sturmflug: Ausdauer-Wörter (Macher-Modus, Locked in, Tuff durchgezogen, Stabil durchgehalten) – kein „Peak“, das wäre bei 14 Bordkarten ironisch.
- Fehler: nur „Schere“ (als Stimme des Kindes: „Schere – passiert.“) und „Auf Lock. Nächste.“ Nie Spott, nie Staunen.

### 2.6 Was es nicht peinlich macht (Meinung, begründet)

1. Opt-in durch das Kind: Ein Erwachsenen-Programm, das ungefragt Slang spricht, ist der Klassiker für „cringe“. Erste Frage kommt nach der ersten Landung mit Stärke ≥ 2 (Bild `erstes_mal_*`).
2. Nur Ausrufe, keine Sätze im Slang; nie zwei Jugendwörter in einem Spruch.
3. Nie erklären, warum die App „cool“ ist; nie Emojis um den Sticker.
4. Kein Wort, das älter als ~3 Jahre aussieht, für 14 (Läuft bei dir, SIU nur 11).
5. Jedes Wort kann das Kind mit einem Tipp loswerden.

### 2.7 Passung zu den bestehenden Vorgaben

- **Reisekarte:** Auf der Karte selbst keine Sticker (Karte bleibt ruhig, Zustände sind Farben/Flaggen-Pins). Einzige Ausnahme wäre die Landungs-Einblendung, die über der Karte liegt – die ist Teil von `lernAbschlussEtappe`.
- **Expedition:** Polarfarben bleiben; Sticker gold/mint auf hellblau – Kontrast geprüft im Bild `expedition_*`. Wort „freiwillig“ kommt in keinem Spruch vor.
- **Drei Karten (Nachbessern · Mein Schuljahr · Zusatz):** Auf den Startseiten-Karten keine Sticker. Der Sticker kommt erst in der Geschafft-Ansicht („Nachbessern“ geschafft).
- **Faire Punkte / Landungs-Bonus:** Sticker ersetzt keine Sterne-Angabe; ★ bleibt im Blatt.

## 3. Sprüche (wörtlich)

„Alter“: beide = 11 und 14. Probe = standardmäßig aus. Wörter-IDs siehe `woerter.json`.


**Landung einer Etappe – Direktflug (kein Fehler, kein Tipp)** (`landung_direkt`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J01 | **PEAK** | 3 | beide | Peak |
| J02 | **Das war Peak.** | 3 | 14 | Peak |
| J03 | **GOAT** | 3 | beide | GOAT |
| J04 | **+1000 Aura** | 3 | beide | Aura |
| J05 | **SIUUU!** | 3 | 11 | SIU |
| J06 | **Çüş – auf Anhieb!** | 3 | beide | Çüş |

**Landung – Saubere Landung ohne Tipp** (`landung_sauber`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J07 | **Tuff.** | 2 | 14 | tuff |
| J08 | **Süper!** | 2 | beide | Süper |
| J09 | **Slay.** | 2 | 14 | Slay |
| J10 | **Gute Käse** | 2 | beide | Gute Käse |
| J11 | **Sauber, Digga.** | 2 | 14 · nur mit Anrede digga | Digga |
| J12 | **Nice gelandet!** | 2 | 11 | Nice |

**Landung – Saubere Landung mit Tipp oder „Wieder gelandet“** (`landung_leicht`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J13 | **Läuft bei dir.** | 1 | 11 | Läuft bei dir |
| J14 | **Lowkey stark.** | 1 | 14 | lowkey |
| J15 | **Akkurat.** | 1 | beide | Akkurat |
| J16 | **W** | 1 | 14 | W |

**Landung – Sturmflug gemeistert (Ausdauer)** (`landung_sturm`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J17 | **Tuff durchgezogen.** | 2 | 14 | tuff |
| J18 | **Macher-Modus** | 2 | beide | Macher |
| J19 | **Locked in.** | 2 | 14 | Locked in |
| J20 | **Stabil durchgehalten.** | 2 | beide | stabil |

**Knobel-Bordkarte im ersten Versuch richtig** (`knobel_richtig`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J21 | **Çüş!** | 3 | beide | Çüş |
| J22 | **Sheesh!** | 3 | beide | Sheesh |
| J23 | **Das crazy!** | 3 | beide | Das crazy |
| J24 | **Wild.** | 3 | 14 | wild |
| J25 | **Ohne Witz – geknackt.** | 3 | beide | Ohne Witz |

**Serie: 5 Bordkarten in Folge richtig** (`serie_5`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J26 | **5 in Folge – locked in** | 2 | 14 | Locked in |
| J27 | **Läuft. 5 in Folge.** | 2 | 11 | Läuft bei dir |

**Serie: 10 Bordkarten in Folge richtig** (`serie_10`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J28 | **Gommemode** | 3 | beide | Gommemode |
| J29 | **Krass – 10 am Stück** | 3 | beide | krass |

**Wiederholung bestanden** (`wiederholung`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J30 | **Hält stabil.** | 1 | beide | stabil |
| J31 | **Safe gekonnt.** | 1 | 14 | safe |
| J32 | **Noch drin. Nice.** | 1 | 11 | Nice |
| J33 | **Süper – noch gewusst.** | 1 | beide | Süper |

**Flug geschafft** (`flug_geschafft`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J34 | **Peak-Flug** | 3 | beide | Peak |
| J35 | **GOAT-Flug** | 3 | 14 | GOAT |
| J36 | **SIUUU!** | 3 | 11 | SIU |
| J37 | **Aura +1000** | 3 | beide | Aura |

**Expedition geschafft** (`expedition_geschafft`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J38 | **Çüş, Expedition!** | 2 | beide | Çüş |
| J39 | **Tuff, Polarprofi.** | 2 | 14 | tuff |

**Expedition fehlerfrei** (`expedition_fehlerfrei`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J40 | **GOAT der Antarktis** | 3 | beide | GOAT |
| J41 | **Peak. Null Fehler.** | 3 | beide | Peak |

**„Nachbessern“ geschafft (wieder offene Stadt wieder abgelegt)** (`nachbessern`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J42 | **Macher-Modus: repariert** | 2 | beide | Macher |
| J43 | **Süper repariert!** | 2 | beide | Süper |
| J44 | **Stabil zurück.** | 2 | 14 | stabil |
| J45 | **Wieder drin – nice.** | 2 | 11 | Nice |
| J46 | **Du bist gut genug.** | 2 | 14 · Probe | Du bist gut genug |

**Fehler-Rückmeldung (falsche Antwort)** (`fehler`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J47 | **Schere.** | 1 | beide | Schere |
| J48 | **Kleine Schere – passiert.** | 1 | beide | Schere |
| J49 | **Auf Lock. Nächste.** | 1 | beide | Auf Lock |
| J50 | **Schere. Nächste Runde.** | 1 | 14 | Schere |

**Begrüßung auf der Abflugtafel (nur mit gewählter Anrede)** (`anrede`)

| Nr | Sticker | Stärke | Alter | Wort |
|---|---|---|---|---|
| J51 | **Yurr!** | 1 | 14 · nur mit Anrede yurr | Yurr |
| J52 | **Digga!** | 1 | 14 · nur mit Anrede digga | Digga |
| J53 | **Bro!** | 1 | 14 · nur mit Anrede bro | Bro |

Hinweis Anrede: J51–J53 setzen den Sticker über die unveränderte Ansage der Abflugtafel. Nur, wenn das Kind genau diese Anrede gewählt hat.

## 4. Einstellungen

**Kind** (im Menü „Ansicht“, dort wo „Helle/Dunkle Ansicht“ sitzt – Bild `landung_direkt_820_*`):
- Jugendwörter: Aus · Selten · Normal · Oft (mit Satz, was das heißt).
- „Wie soll die App dich nennen?“ Gar nicht · Digga · Bro · Yurr (Standard: gar nicht).
- Ausgeblendete Wörter mit „wieder zeigen“.

**Am Sticker** (Bild `bedeutung_*`): Antippen → Blatt mit Wort, „gesprochen …“ (bei Çüş), Bedeutung in einem Satz, Jahr · Knöpfe „„Peak“ gefällt mir nicht“, „Jugendwörter einstellen ›“, „Schließen“. Nach dem Ausblenden kurzer Hinweis „„Peak“ kommt nicht mehr. Rückgängig“. Ausblenden gilt für alle Sprüche mit diesem Wort, nur für dieses Kind.

**Eltern** (im Elternbereich je Kind – Bild `eltern_*`):
- Gleiche Stufen Aus … Oft.
- „Darf das Kind selbst ändern?“ Ja · Nein, festlegen. Bei Nein sieht das Kind die Stufe mit 🔒 „Von deinen Eltern festgelegt.“; Ausblenden einzelner Wörter darf das Kind trotzdem.
- Liste der vom Kind ausgeblendeten Wörter (nur lesen – Eltern holen ein Wort nicht gegen den Willen des Kindes zurück; Meinung).
- Zeile „Wortliste Stand … · nächste Prüfung …“.

**Startwert:** Aus, bis das Kind Ja sagt (Karte „Neu: Jugendwort-Sticker“). Haben die Eltern vorher „Aus, festlegen“ gewählt, kommt die Frage nicht.

**Halbjährliche Prüfung:** `woerter.json` hat `stand`, `naechste_pruefung` (15.05.2027) und je Wort `verfall`. Die App zieht kein Wort mit `verfall` < aktueller Monat. Prüfung jeweils Mai und November (nach der Langenscheidt-Wahl im Oktober) als Auftrag an mich: neue Liste, Verfall verschieben oder streichen, Annahmen belegen. Wenn die Prüfung ausfällt, verschwinden alte Wörter von allein – lieber zu wenig als peinlich.

## 5. Was geht ohne Datenbank, was braucht den Server

| Teil | Ohne Datenbank (auf dem Gerät) | Server nötig? |
|---|---|---|
| Wortliste und Sprüche | `woerter.json` als feste Datei in der App | nein |
| Auswahl, Zufall, Säcke, letzte Sticker, Tageszähler | `localStorage` je Kind, Schlüssel z. B. `lern.jw.<kind-id>` (wie `lern.gestaltung.<kind-id>`) | nein |
| Stufe und Anrede, vom Kind gewählt | `localStorage` je Kind | nein (Stufe 1) |
| Ausgeblendete Wörter des Kindes | `localStorage` je Kind | nein (Stufe 1) |
| Erstes-Mal-Frage schon gestellt | `localStorage` | nein |
| Anlass-Daten (Direkt/Sauber/Sturm, Tipp, wieder, Serie, Knobel, fehlerfrei) | kommen schon vom Server bzw. stehen in der App | **prüfen:** „Tipp genutzt“ bei sauberer Landung – im Code sehe ich `landung.landung_art`, `wieder_gelandet`, `bordkarten`, `eigene_loesungen`, kein Tipp-Feld (Annahme: fehlt). Ohne Feld: „sauber“ immer als Stärke 2 behandeln, oder die App merkt sich Tipps der Etappe selbst. |
| Eltern-Stufe und „festlegen“, auf allen Geräten gültig | geht nicht sicher: auf dem Gerät kann das Kind den Speicher löschen; Eltern-Einstellung am eigenen Handy erreicht das Kind-Gerät nicht | **ja** – ein Feld in den Kind-Einstellungen, z. B. `jugendwoerter: {stufe, kind_darf, anrede, aus: [ids]}` |
| Ausblenden auf allen Geräten des Kindes | nur pro Gerät | ja (gleiches Feld) |
| Auswertung „welche Wörter werden ausgeblendet“ für die Halbjahresprüfung | nein | optional, nur Zählung, keine Namen |

**Vorschlag zur Reihenfolge:** JW-1 nur Gerät (Kind-Einstellung, Ausblenden, Dosis) – kann sofort, ohne Datenbank. JW-2 Server-Feld für Eltern-Sperre und geräteübergreifendes Ausblenden (Werkstatt-Wunsch mit Sperre nach W1–W7).

## 6. Offene Punkte / Risiken

- Schrift: „Çüş“ braucht Ç und ş in der Sticker-Schrift (im Entwurf Systemschrift, korrekt dargestellt). Bei eigener Schrift prüfen.
- „Das crazy“ wirkt ohne Ausrufezeichen gelangweilt – Zeichen nicht weglassen.
- „Du bist gut genug“ (J46) ist Probe und standardmäßig aus: Meme-Ironie möglich.
- Annahme-Wörter (siehe 1) bis zur ersten Prüfung belegen.
- Kein Test in echten Kinderdaten; Entwurf nur mit Testkind-Texten.

## 7. Bauschritte (Vorschlag)

1. JW-1a Daten: `woerter.json` übernehmen (ohne Änderung der Inhalte), Lader mit Verfalls-Filter.
2. JW-1b Auswahl: Dosis, Säcke, Sperren, Tageszähler, Frust-Bremse (2.3–2.5) im Gerät.
3. JW-1c Sticker in den 12 Anlässen (2.1), Platzregeln, Animation, Vorlesen.
4. JW-1d Bedeutungs-Blatt, Ausblenden + Rückgängig, Einstellungen Kind, Erstes-Mal-Karte.
5. JW-2 Server-Feld + Elternbereich + Sperre.

Prüfpunkte für meine Nachprüfung: Sticker verdeckt nichts (400 und 820, Tag und Nacht) · keine Wiederholung in 20 Zügen · Fehler-Sticker nie ab 2. Fehler in Folge · Stärke passt · Ausblenden wirkt sofort · Aus = wirklich nichts.
