# Vorgabe JW – Jugendwörter in Geschafft- und Belohnungs-Ansichten

Stand 23.11.2026 · Grundlage `lernen-app` c98fffd (`lernAbschlussEtappe`, `lernAbschlussFlug`, `lernExGeschafftAnsicht`, Knobel- und Bordkarten-Rückmeldung) · Daten: `woerter.json` · Entwurf: `entwurf/jugendwoerter.html` · Bilder: `bilder/*_400|820_tag|nacht.png` · Entwurf online: Artefakt f41b44f0-f8fc-460f-85ef-2e3df5760deb

Kein App-Code, keine Datenbank, keine Namen. **Fassung 2 (23.11.2026, der Nutzer):** keine Einstellungen, keine Auswahl, keine Unterscheidung 11/14, Anrede „Digga“, Wörter werden wirklich verwendet. Alles ist festgelegt.

## 0. Kurzfassung

- **Ein Sticker, nie ein Satz in Slang.** Das Jugendwort klebt groß als schräger Sticker in der Szene. Titel („Direktflug“), Zahlen und der erklärende Satz bleiben unverändert normales Deutsch.
- **Immer, aber stylisch.** Jede Geschafft-Ansicht bekommt genau einen Sticker. Kein Spruch zweimal hintereinander, kein Wort aus den letzten 4 Stickern.
- **Stärke folgt dem Ergebnis.** „PEAK“, „GOAT“, „+1000 Aura“ nur für Direktflug, Flug geschafft, Knobel, fehlerfrei. Mit Tipp gibt es „Akkurat.“, „W“, „Lowkey stark.“.
- **Festgelegt für beide Kinder.** Keine Einstellungen, keine Altersstufen, Anrede „Digga“. Antippen des Stickers zeigt nur die Bedeutung (hilft beim Mitreden, z. B. „Çüş“ → gesprochen Tschüsch).
- **Wortliste:** 74 Wörter geprüft, 30 im Einsatz, 44 ausgeschlossen mit Grund; 52 fertige Sprüche. Halbjährliche Prüfung, Wörter mit abgelaufenem Verfallsdatum werden automatisch nicht mehr gezogen.

## 1. Recherche

**Gesicherte Fakten (mit Quelle in `woerter.json`):**
- 2026: Jugendwort „Ragebait“; Top 10: 67, Crashout, Digga, Du bist gut genug, Gute Käse, Macker, Peak, Ragebait, Schere, Süper (ZDFheute). Top 3: Crashout, Ragebait, Peak (GIGA).
- 2025: „Das crazy“ vor „goonen“ und „checkst du“; Top 10 außerdem Digga(h), lowkey, Rede, Schere, sybau, tot, tuff (SRF).
- 2024: „Aura“ vor „Talahon“ und „Schere“; Top 10 außerdem Hölle nein, Pyrotechnik, Yolo, Nein Pascal ich denke nicht, Yurr, Akh, Digga(h) (web.de, QuillBot).
- 2021–2023: cringe/sheesh/sus · smash/bodenlos/Macher (+ Gommemode, SIU, wild, Slay, Bro …) · goofy/side eye/NPC (+ Auf Lock, Darf er so, Kerl*in, Rizz, Slay, Yolo).
- Çüş: Ausruf des Staunens (boah, krass, oha), gesprochen „Tschüsch“; Nebenbedeutungen „igitt“ bzw. ursprünglich Halte-Ruf für Esel → „mach mal halblang“.

**Annahmen (in `woerter.json` mit `beleg: "Annahme …"` markiert):** W, GOAT, Locked in, Nice, krass, stabil, safe, Ohne Witz, Sigma, Skibidi, Brainrot, cooked, L, Vallah, Mashallah – gängiger Netz-Slang, aber nicht aus einer Langenscheidt-Liste und von mir nicht mit Quelle geprüft. Bei der ersten Halbjahresprüfung belegen oder streichen.

**Nicht geprüft:** Bedeutung von „Mehrzweckeier“ (2026 von der Jury ausgeschlossen) → ungeeignet.

**Pflichtwörter laut Auftrag – alle drin:** Çüş (staunen), Digga (feste Anrede), Peak (lob_gross), Gute Käse (lob_klein), Süper (lob), Das crazy (staunen), Schere (nur fehler_mild).

**Ausgeschlossen laut Auftrag und Prüfung** (Auszug, alle mit Grund in der Datei): Ragebait, Crashout, goonen, sybau, Talahon, smash, Hawk Tuah, AMK (Wut/Provokation, sexuell, beleidigend, abwertend) · cringe, sus, goofy, lost, NPC, side eye, L, cooked, bodenlos, tot (beschämen bei Fehlern) · checkst du (belehrend) · 67, Skibidi, Mittwoch (kein Sinn) · Akh, Vallah, Mashallah (religiöse/gruppenbezogene Formeln) · Yolo, Pyrotechnik (falsches Signal) · I bims, fly, Kerl*in (veraltet).

**Nebenbedeutungen, die den Einsatz begrenzen:** Çüş, Sheesh, wild, krass, Das crazy (können negativ/gelangweilt sein → nur nach klar gutem Ergebnis, nie bei Fehlern) · Slay (wörtlich „töten“ – im Slang längst nur Lob, darum drin) · Aura (nur „+1000“, nie Minus) · Peak (nie mit negativem Wort) · Macher (nur neutral „Macher-Modus“) · Digga (nie als Vorwurf, nur freundlich) · SIU/Gommemode (Bezug auf reale Personen; bei der Halbjahresprüfung als Erste prüfen).

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

### 2.3 Wie oft (festgelegt)

- **Erfolg:** jede Geschafft-Ansicht aus 2.1 bekommt genau einen Sticker.
- **Fehler:** Sticker beim 1., 3., 5. … Fehler eines Lerntags; **nie ab dem 2. Fehler in Folge** (dann nur der normale Text – Frust nicht mit Witz übertünchen).
- **Anrede:** einmal je Lerntag auf der Abflugtafel („Yo Digga!“, „Yurr, Digga!“, „Digga, los geht’s.“); dazu „Digga“ in einzelnen Sprüchen.
- Lerntag = derselbe Tag wie bei den übrigen Lerntag-Zählern.

### 2.4 Abwechslung

- Je Anlass ein „Sack“: Sprüche werden ohne Zurücklegen gezogen, bis der Sack leer ist.
- Nie derselbe Spruch wie der letzte Sticker (auch über Anlässe hinweg).
- Kein Wort aus den letzten 4 Stickern, solange ein anderer passender Spruch da ist.
- Ist der Sack leer, wird er neu gefüllt; „Digga“ zählt nicht zur Wort-Sperre (Anrede).

### 2.5 Stärke passend zum Ergebnis

- Stärke des Spruchs = Stärke des Anlasses (Tabelle 2.1). Nie nach oben ausweichen.
- Mit Tipp, „wieder gelandet“ oder Wiederholung: nur Stärke 1 (Akkurat, Lowkey stark, W, Hält stabil).
- Sturmflug: Ausdauer-Wörter (Macher-Modus, Locked in, Tuff durchgezogen, Stabil durchgehalten) – kein „Peak“, das wäre bei 14 Bordkarten ironisch.
- Fehler: nur „Schere“ (als Stimme des Kindes: „Schere – passiert.“) und „Auf Lock. Nächste.“ Nie Spott, nie Staunen.

### 2.6 Was es nicht peinlich macht (Meinung, begründet)

1. Nur Ausrufe als Sticker, keine Sätze im Slang; der erklärende Satz bleibt Deutsch.
2. Nie erklären, warum die App „cool“ ist; keine Emojis um den Sticker.
3. Stärke ehrlich: kein „Peak“ für einen Wackel-Erfolg.
4. Veraltete und spöttische Wörter sind raus (Abschnitt 1); die Liste wird halbjährlich erneuert.

### 2.7 Passung zu den bestehenden Vorgaben

- **Reisekarte:** Auf der Karte selbst keine Sticker (Karte bleibt ruhig, Zustände sind Farben/Flaggen-Pins). Einzige Ausnahme wäre die Landungs-Einblendung, die über der Karte liegt – die ist Teil von `lernAbschlussEtappe`.
- **Expedition:** Polarfarben bleiben; Sticker gold/mint auf hellblau – Kontrast geprüft im Bild `expedition_*`. Wort „freiwillig“ kommt in keinem Spruch vor.
- **Drei Karten (Nachbessern · Mein Schuljahr · Zusatz):** Auf den Startseiten-Karten keine Sticker. Der Sticker kommt erst in der Geschafft-Ansicht („Nachbessern“ geschafft).
- **Faire Punkte / Landungs-Bonus:** Sticker ersetzt keine Sterne-Angabe; ★ bleibt im Blatt.

## 3. Sprüche (wörtlich)

Gleich für beide Kinder. Wörter-IDs siehe `woerter.json`.


**Landung einer Etappe – Direktflug (kein Fehler, kein Tipp)** (`landung_direkt`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J01 | **PEAK** | 3 | Peak |
| J02 | **Das war Peak.** | 3 | Peak |
| J03 | **GOAT** | 3 | GOAT |
| J04 | **+1000 Aura** | 3 | Aura |
| J05 | **SIUUU!** | 3 | SIU |
| J06 | **Çüş – auf Anhieb!** | 3 | Çüş |

**Landung – Saubere Landung ohne Tipp** (`landung_sauber`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J07 | **Tuff.** | 2 | tuff |
| J08 | **Süper!** | 2 | Süper |
| J09 | **Slay.** | 2 | Slay |
| J10 | **Gute Käse** | 2 | Gute Käse |
| J11 | **Sauber, Digga.** | 2 | Digga |
| J12 | **Nice gelandet!** | 2 | Nice |

**Landung – Saubere Landung mit Tipp oder „Wieder gelandet“** (`landung_leicht`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J13 | **Lowkey stark.** | 1 | lowkey |
| J14 | **Akkurat.** | 1 | Akkurat |
| J15 | **W** | 1 | W |
| J16 | **Läuft, Digga.** | 1 | Läuft bei dir, Digga |

**Landung – Sturmflug gemeistert (Ausdauer)** (`landung_sturm`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J17 | **Tuff durchgezogen.** | 2 | tuff |
| J18 | **Macher-Modus** | 2 | Macher |
| J19 | **Locked in.** | 2 | Locked in |
| J20 | **Stabil durchgehalten.** | 2 | stabil |

**Knobel-Bordkarte im ersten Versuch richtig** (`knobel_richtig`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J21 | **Çüş!** | 3 | Çüş |
| J22 | **Sheesh!** | 3 | Sheesh |
| J23 | **Das crazy!** | 3 | Das crazy |
| J24 | **Wild.** | 3 | wild |
| J25 | **Ohne Witz – geknackt.** | 3 | Ohne Witz |

**Serie: 5 Bordkarten in Folge richtig** (`serie_5`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J26 | **5 in Folge – locked in** | 2 | Locked in |
| J27 | **5 am Stück, Digga.** | 2 | Digga |

**Serie: 10 Bordkarten in Folge richtig** (`serie_10`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J28 | **Gommemode** | 3 | Gommemode |
| J29 | **Krass – 10 am Stück** | 3 | krass |

**Wiederholung bestanden** (`wiederholung`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J30 | **Hält stabil.** | 1 | stabil |
| J31 | **Safe gekonnt.** | 1 | safe |
| J32 | **Noch drin. Nice.** | 1 | Nice |
| J33 | **Süper – noch gewusst.** | 1 | Süper |

**Flug geschafft** (`flug_geschafft`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J34 | **Peak-Flug** | 3 | Peak |
| J35 | **GOAT-Flug** | 3 | GOAT |
| J36 | **SIUUU!** | 3 | SIU |
| J37 | **Aura +1000** | 3 | Aura |

**Expedition geschafft** (`expedition_geschafft`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J38 | **Çüş, Expedition!** | 2 | Çüş |
| J39 | **Tuff, Polarprofi.** | 2 | tuff |

**Expedition fehlerfrei** (`expedition_fehlerfrei`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J40 | **GOAT der Antarktis** | 3 | GOAT |
| J41 | **Peak. Null Fehler.** | 3 | Peak |

**„Nachbessern“ geschafft (wieder offene Stadt wieder abgelegt)** (`nachbessern`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J42 | **Macher-Modus: repariert** | 2 | Macher |
| J43 | **Süper repariert!** | 2 | Süper |
| J44 | **Stabil zurück.** | 2 | stabil |
| J45 | **Wieder drin – nice.** | 2 | Nice |

**Fehler-Rückmeldung (falsche Antwort)** (`fehler`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J46 | **Schere.** | 1 | Schere |
| J47 | **Kleine Schere – passiert.** | 1 | Schere |
| J48 | **Auf Lock. Nächste.** | 1 | Auf Lock |
| J49 | **Schere, Digga. Nächste.** | 1 | Schere, Digga |

**Begrüßung auf der Abflugtafel (Anrede Digga)** (`anrede`)

| Nr | Sticker | Stärke | Wort |
|---|---|---|---|
| J50 | **Yo Digga!** | 1 | Digga |
| J51 | **Yurr, Digga!** | 1 | Yurr, Digga |
| J52 | **Digga, los geht’s.** | 1 | Digga |

Hinweis Anrede: J50–J52 setzen den Sticker auf die unveränderte Ansage der Abflugtafel, einmal je Lerntag.

## 4. Einstellungen

**Keine.** Festgelegt vom Nutzer am 23.11.2026: kein Ein/Aus, keine Dosis, keine Auswahl der Anrede, kein Ausblenden, keine Altersstufen.

Was bleibt:
- **Antippen des Stickers** → kleines Blatt mit Wort, „gesprochen …“ (bei Çüş), Bedeutung in einem Satz, „Schließen“ (Bild `bedeutung_*`). Kein Ausblenden.
- **Halbjährliche Prüfung:** `woerter.json` hat `stand`, `naechste_pruefung` (15.05.2027) und je Wort `verfall`. Die App zieht kein Wort mit abgelaufenem `verfall`. Prüfung jeweils Mai und November (nach der Langenscheidt-Wahl im Oktober) als Auftrag an mich. Fällt sie aus, verschwinden alte Wörter von allein.

## 5. Was geht ohne Datenbank, was braucht den Server

**Alles geht ohne Datenbank.**

| Teil | Wo |
|---|---|
| Wortliste und Sprüche | `woerter.json` als feste Datei in der App |
| Säcke, letzte 4 Sticker, Fehler-Zähler des Lerntags, „Anrede heute schon gezeigt“ | `localStorage` je Kind, z. B. `lern.jw.<kind-id>` (wie `lern.gestaltung.<kind-id>`); geht der Speicher verloren, startet die Abwechslung einfach neu |
| Anlass-Daten (Direkt/Sauber/Sturm, wieder, Serie, Knobel, fehlerfrei) | kommen schon vom Server bzw. stehen in der App |

Server nur nötig, falls gewünscht: Feld „Tipp genutzt“ bei sauberer Landung. Im Code sehe ich `landung_art`, `wieder_gelandet`, `bordkarten`, `eigene_loesungen`, kein Tipp-Feld (Annahme: fehlt). Ohne Feld wird jede saubere Landung als Stärke 2 behandelt – das reicht.

## 6. Offene Punkte / Risiken

- Schrift: „Çüş“ braucht Ç und ş in der Sticker-Schrift (im Entwurf Systemschrift, korrekt). Bei eigener Schrift prüfen.
- „Das crazy“ wirkt ohne Ausrufezeichen gelangweilt – Zeichen nicht weglassen.
- Annahme-Wörter (siehe 1) bis zur ersten Prüfung belegen.
- Entwurf nur mit Testkind-Texten, keine echten Kinderdaten.

## 7. Bauschritte (Vorschlag)

1. JW-1a Daten: `woerter.json` übernehmen, Lader mit Verfalls-Filter.
2. JW-1b Auswahl: Säcke, Sperren, Fehler-Regel, Anrede einmal je Lerntag (2.3–2.5), alles im Gerät.
3. JW-1c Sticker in den 14 Anlässen (2.1), Platzregeln, Animation, Vorlesen, Bedeutungs-Blatt.

Prüfpunkte für meine Nachprüfung: jede Geschafft-Ansicht hat einen Sticker · Sticker verdeckt nichts (400 und 820, Tag und Nacht) · keine Wiederholung in 20 Zügen · Fehler-Sticker nie ab 2. Fehler in Folge · Stärke passt · Anrede höchstens einmal je Lerntag.
