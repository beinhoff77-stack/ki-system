# Umsetzung 1 – wo der Adventskalender und die Weihnachts-Ebene eingehängt werden

Stand 28.11.2026 · Fundstellen auf dem Zweig `lernen-app` (Commit 11849d0e). Zeilennummern sind ungefähr, gesucht wird nach dem Namen.
Das Konzept steht in `konzept.md`, der Entwurf in `index.html`, die Bilder in `bilder/`.

## A. Adventskalender

### A1. Tür nach der Etappe (Kind)

**Wo:** `lernen.js`, Übungs-Ansicht, Zweig `if (jetztSitzt && neu)` (um Z. 4622–4653):
```
const exFrei = lernExNachLandung(ctx);
const zeigeLandung = () => { … lernAbschlussZeigen(ctx.kindObj, lernAbschlussEtappe({ …, knopf: lernExVorKnopf(knopf(), exFrei), … }), { label: 'Etappe gelandet' }); };
```

**Neu:**
1. `const advent = lernAdventNachLandung(ctx)` ruft `schule_advent_stand` auf, und zwar gleichzeitig mit `exFrei`. Ausnahmen: kein Dezember, oder `lernNeu(kind)` ist falsch → `null`.
2. Der Knopf wird zweimal umhüllt: `knopf: lernAdventVorKnopf(lernExVorKnopf(knopf(), exFrei), advent)`. Das folgt genau dem Muster von `lernExVorKnopf` (Z. 618 ff.):
   - Klick abfangen (Capture).
   - Ist `frei_heute > 0` und `naechste_nr` gesetzt, zuerst `lernAdventTuerZeigen(...)` zeigen, danach mit dem ursprünglichen Ziel weiter.
   - Andernfalls sofort weiter.
3. **Reihenfolge:** Erst kommt „Expedition freigeschaltet“, dann die Tür, dann das ursprüngliche Ziel (nächste Etappe, Flug-Test oder Abflug). Knobel-Bordkarte, Sturmflug-Textlink und der Flug-Test bleiben unverändert.
4. Der Link **„Pause – zur Abflugtafel/Reisekarte“** (`lr-ab-pause`) zeigt die Tür **nicht**. Das verdiente Türchen bleibt dann „bereit“: Die Hinweiszeile auf der Karte wird gold („Türchen 6 ist bereit – jetzt öffnen ›“), und es lässt sich im Kalender öffnen.
5. Nachbessern („Sitzt wieder!“, `nbFertig`, um Z. 4460): Wenn Frage 3 mit A beantwortet wird, bekommt dieser Knopf dieselbe Hülle (`lernAdventVorKnopf(knopf, advent)`).

**Tür-Ansicht `lernAdventTuerZeigen(kind, stand, weiter)`:**
- Hülle `lernAbschlussZeigen(kindObj, inhalt, { label: 'Türchen 7' })`. Die Szene hat die Klasse `lr-ab-app lr-advent`; Blatt und großer Knopf werden wie bei der Landung genutzt (`lr-ab-blatt`, `lernGrossKnopf`).
- **Zu:** Tür (Button, `aria-label` „Türchen 7 öffnen“) und großer gelber Knopf „Türchen 7 öffnen“. Darunter der Textlink „Später öffnen – weiter zu: …“, der den Ablauf überspringt.
- **Tippen:** `lernCall('schule_advent_oeffnen', { lernender_id, client_id: lernCid() })`.
  - Während der Antwort dreht sich die Tür auf (CSS `rotateY`, 0,7 s).
  - Bei `lernWenigBewegung()` gibt es keine Drehung und kein Wackeln; der Inhalt steht sofort da.
- **Inhalt je Art:**
  - Motiv: SVG aus `LERN_ADVENT_MOTIVE[motiv]` plus Satz.
  - Gutschein: Karte im Bordkarten-Stil (Kopf „GUTSCHEIN · TÜR 7“, Perforation, „Hol dir bei Mama oder Papa ab“, „Liegt jetzt in ‚Meine Gutscheine‘“).
  - Nur Sterne: große Zahl „+500 ★“ mit „gutgeschrieben“.
  - Leer: „nur Licht.“ plus Spruch.

  Sterne werden zusätzlich als „+50 ★“ in der Karte gezeigt. Danach wird `lernVergessen(kind)` aufgerufen, damit Konto und Sterne-Chip frisch geladen werden.
- **Sticker:** `lernJwPlatz(kind, 'advent')`. Dafür kommt ein neuer Anlass in `daten/jugendwoerter.json` (Stärke 2–3: W, Sheesh!, +1000 Aura …).
- **Danach:** Der große Knopf zeigt den ursprünglichen Text („Weiter: Zahlenstrahl“), dazu der Link „Adventskalender ansehen“.
- **Fehler** „Heute schon 2“ oder „Erst nach deiner nächsten Etappe“: Die Ansicht schließt sich ohne Meldung und geht weiter, das Gerät hatte nur alte Zahlen. Alle anderen Fehler: kleine Zeile im Blatt und „Weiter“.

### A2. Kalender, Gutscheine (Kind)

- **Neue Routen:**
  - `#/advent/<kind>` → `viewAdvent`
  - `#/gutscheine/<kind>` → `viewGutscheine`

  Beide kommen in `app.js` (`views`, Z. 228), in `lernen/schule.js` (`views` Z. 113 und `KIND_ANSICHTEN` Z. 50) sowie in den Bereich `lernen` in `app.js` Z. 179/181.
- **Rahmen:** `lernRahmen(kind, 'advent', …)` (Z. 256).
- **Menü:** Im Menüblatt (Z. 265) kommen zwei Einträge dazu, nur vom 1.12. bis 31.1.:
  - `['advent', 'Adventskalender']` mit Zähler „2 warten“,
  - `['gutscheine', 'Meine Gutscheine']` mit Zähler offen + angefragt (Gutscheine bleiben sichtbar, solange einer offen ist).
- **Kalender:**
  - Raster 24 Türen in fester, gemischter Anordnung: 4 Spalten bis 600 px, 6 bis 1100 px, 8 darüber.
  - Zustände aus `schule_advent_stand`: offen · bereit · heute · nachholen · morgen · zu.
  - Offene Türen öffnen ein Blatt mit dem Inhalt (`schule_advent_tuer_lesen`); „bereit“ öffnet die Tür-Ansicht A1.
  - Rechts (bzw. darunter) stehen die Karte „Meine Gutscheine“ und „So geht’s“.
- **Gutscheine:**
  - Liste aus `schule_advent_gutscheine`, Reihenfolge offen/„heute nicht“ → angefragt → eingelöst (grau, durchgestrichen, nicht antippbar).
  - Knopf „Einlösen“ erst in Stufe 1b; in 1a steht dort „Zeig ihn Mama oder Papa“.

### A3. Hinweis auf der Reisekarte (ohne die Karte zu verändern)

**Wo:** `geradeDran()` in der Reisekarte, um Z. 2371–2389, Karte `rk-schwebe-karte`. Heute steht dort `start.ansage ? el('p', { class: 'lr-dock-ansage rk-ansage' }, …)`.

**Neu:** Eine Zeile `lernAdventZeile(kind, stand)` zwischen Ansage und Startknopf: ein Link mit 44 px Höhe und einer kleinen grünen Tür mit Zahl.

| Zustand | Text |
|---|---|
| wartet | „Türchen 6 + 7 warten – je Etappe eins ›“ |
| bereit (gold) | „Türchen 6 ist bereit – jetzt öffnen ›“ |
| Limit | „2 Türchen heute offen – morgen geht’s weiter ›“ |
| vor dem 1.12. | „Noch 3 Tage bis Türchen 1“ (nur ab 28.11.) |
| alles offen | keine Zeile |

- Die Schwebekarte wird dadurch etwa 50 px höher. Die Karte rechnet das schon über `unten()` ein (Z. 2405).
- Auf dem Rechner steht die Zeile in derselben Karte rechts.
- Den Stand liefert `schule_advent_stand`. Der Abruf läuft nur im Dezember, parallel zu `schule_einheit_lesen` (Z. 2350), und kann fehlschlagen, ohne dass die Karte darunter leidet.

### A4. Eltern

- **Lehrer-Startseite** (`viewLernen`, LS-Zweig um Z. 1144–1170):
  - In `verwalten` kommt `['#/advent', 'Adventskalender', '2 Gutscheine angefragt · Tür 8 morgen']` dazu, nur vom 15.11. bis 31.1. (Bild `eltern-zutun-*`).
  - Die Belohnungen bleiben ausgeblendet.
- **„Zu tun“** (Stufe 1b): Die Anfragen aus `schule_advent_lesen().anfragen` werden wie `wuensche` an `lernZuTun(…, wuensche)` übergeben (Z. 1269). Der Text lautet „Kind 1 möchte „…“ einlösen · Gutschein aus Tür 3“. Die Knöpfe „Eingelöst“ und „Heute nicht“ rufen `schule_advent_gutschein_entscheiden` auf.
- **Seite `#/advent`** → `viewAdventEltern` (nur `ist_eltern`, sonst Umleitung). Der Stil folgt `lst-` / „Was wackelt“: Karten mit 19 px Radius, Zeilen mit 44 px.
  - **Abschnitte:**
    1. Heute je Kind
    2. Gutscheine (angefragt / offen / eingelöst + Zurückholen)
    3. Vorrat
    4. Türchen je Kind: auf dem Handy mit Umschalter Kind 1 | Kind 2, ab 1000 px beide nebeneinander.
  - **Erststart:** „Mit 24 Vorschlägen füllen“ macht in einem Schritt drei Dinge: Ideen übernehmen, mischen und speichern.
  - **Blätter:**
    - Ideen: Chips in Gruppen, „von Hand“-Kennzeichen.
    - Tür ändern: So lassen · aus Vorrat · tauschen · nur für dieses Kind · leer.
    - Inhalt bearbeiten: Art, Titel, Text, Sterne mit −/+ und 0/50/100/500, für wen.
  - Vorschau „so sieht es Kind 1“ zeigt die Tür-Ansicht A1 mit Eltern-Daten und Band „Vorschau“. Sie ruft `oeffnen` nicht auf.
- **Daten in der App:**
  - `daten/advent-ideen.json` mit 95 Ideen in elf Gruppen. Die Liste des Projektleiters liegt nicht im Zweig, im Entwurf steht ein Auszug.
  - `LERN_ADVENT_MOTIVE` mit den 16 Motiven als SVG-Text. 6 sind fertig (koala, surf, neonbaum, pinguin, polarlicht, flieger) und können aus `index.html` (`MOTIVE`) übernommen werden.

### A5. Server

- **Migration:** `supabase/migrations/2026113x_ad_s_advent.sql`
  - 4 Tabellen und 10 `api.schule_advent_*`-Funktionen (Konzept 3–5),
  - Erweiterung von `sterne_grund_check` um `'advent'`, mit genauer Prüfung der bisherigen Definition (Muster `20261122_fp_s_faire_punkte.sql` Z. 36–46),
  - Rauchtest `supabase/tests/ad_s_rauchtest.sql`.
- **lernen-api `index.ts`:**
  - 10 Einträge in `AKTIONEN`,
  - `VERSION` 0.10.0.
- Einspielen nur mit dem ausdrücklichen Satz des Nutzers.

### A6. Prüfung

- Nachbau in `tests/lernen.test.cjs` (Server-Nachbau wie `rkServer`/`wdhServer`):
  - Stand mit 0, 1 und 2 Etappen heute,
  - Nachholen,
  - Limit,
  - 24. und danach,
  - leerer Platz,
  - zwei Geräte (zweiter Aufruf → „schon offen“).
- Bildschirmfotos wie in der Durchsicht vom 28.11.

**Aufwand:** Stufe 1a etwa 16–20 h, Stufe 1b etwa 4–6 h (Konzept Abschnitt 9).

---

## B. Weihnachts-Ebene auf der Reisekarte (unabhängig vom Kalender)

**Eine Stelle:** die Reisekarte in `lernen.js` (um Z. 2296–2303):
```
const ebenen = { meer, land, kette, route, oben };   // svg.append(… ebenen.oben)
const rahmen = el('div', { class: 'rk-rahmen' }, svg);
```

**Neu:**
1. **Schalter nach Datum:** `const fest = lernFestAn()`. Ergibt das Gerätedatum (Ortszeit) Monat 12, ist `fest` 1–31, sonst `null`. Am 1.1. ist die Ebene weg. Zum Prüfen gibt es eine Übersteuerung mit `localStorage['lern.fest']` (`an` | `aus`).
2. **Zwei Ebenen, beide nur Grafik:**
   - `ebenen.fest = s('g', { class: 'rk-fest', 'pointer-events': 'none', 'aria-hidden': 'true' })` wird **nach** `ebenen.oben` angehängt. Diese Gruppe bewegt sich mit der Karte (Ziehen/Zoomen); sie trägt Mützen, Geschenke, Stiefel, Stern und Feuerwerk.
   - `const festRand = el('div', { class: 'rk-fest-rand', 'aria-hidden': 'true' })` mit `position: absolute; inset: 0; pointer-events: none` kommt in `rahmen`. Diese Ebene steht fest; sie trägt Lichterkette, Polarlicht, Eiskristalle und das Schnee-Canvas.
3. **Zeichnen:** Am Ende von `zeichneOben()` (Z. 2493) steht `if (fest) lernFestZeichnen(ebenen.fest, { pins, dran, besucht, route, k, W, H, variante, tag: fest })`. Die Positionen sind dieselben wie für die Pins (`bild(p)`), deshalb sitzen Mützen immer auf dem Pin-Kopf, auch nach dem Zoomen.
   - „Besucht“ = Pins mit Zustand `gesch` / `gold`.
   - „Aktuell“ = `dranFlug`.
   - Route = `zeichneRouten()` (Z. 2476 ff.).
4. **Bewegung:**
   - Nur CSS (`opacity`/`transform`) und **ein** `requestAnimationFrame` für Schnee (26 Punkte) bzw. den Schlitten (5 s Flug, 20 s Pause).
   - Bei `lernWenigBewegung()` ist alles still: kein Schnee, kein Schlitten.
   - Bei `document.hidden` wird angehalten.
   - Am 24.12. fliegt der Schlitten einmal am Tag (`localStorage['lern.fest.24']`).
5. **Nachtmodus:** Die Farben kommen aus `lernGestaltung(kind)`. Im Hellen haben die Flocken einen feinen Rand, im Dunklen leuchtet das Polarlicht stärker.
6. **Freizonen:**
   - Die Lichterkette läuft nur zwischen Sonne (`.rk-uni`) und Zoom-Knöpfen.
   - Eiskristalle gibt es nur unten rechts, über der Schwebekarte (`unten()`).
   - Das Feuerwerk steht neben dem Ziel, an der Seite mit den wenigsten Pins (aus der Liste `belegt` in `zeichneOben`, die schon für die Beschriftungen genutzt wird).
   - Das Jugendwort-Schild liegt außerhalb des Kartenrahmens und bleibt unberührt.
7. **Stil:** Neue Klassen `rk-fest-*` in `style.css` neben `rk-…` (Z. ~5617), etwa 40 Zeilen.

**Aufwand je Variante (ohne Server):**

| Variante | Aufwand |
|---|---|
| V1 dezent | 2–3 h |
| V2 verspielt | 4–5 h (Schlitten entlang der Route, Geschenke) |
| V3 Neon-Nordlicht | 3 h |
| Sonderfälle 6./24./31.12. | je 0,5–1 h |
| Prüfung (Bilder Europa/Welt, hell/dunkel, Bewegung reduzieren, altes Handy) | 1 h |

**Unabhängig:**
- Die Ebene braucht keinen Server, keine Daten und keine Migration und berührt den Kalender nicht.
- Sie kann vor oder nach dem Adventskalender live gehen und lässt sich jederzeit mit `lernFestAn = () => null` abschalten.

---

## C. Nachtrag 28.11.

- **Tür-Sorten** in `lernAdventTuerZeigen`: Klasse `lr-advent-<sorte>` (krampus · jackpot · niete · karte). Die Krampus-Tür bekommt Hörnchen und Kratzer statt der Schleife (Frage 3). Inhalte und Stile stehen im Entwurf (`.krampus-karte`, `.jackpot`, `.niete`, `.karte-gross`) und können als CSS übernommen werden.
- **Sonder-Motive** `krampus`, `nikolaus` (Tür 6), `heiligabend` (Tür 24) aus `MOTIVE` des Entwurfs in `LERN_ADVENT_MOTIVE`. Sie stehen nicht in der allgemeinen Motiv-Auswahl.
- **„Meine Gutscheine“:** Rubrik „Vom Krampus“ unter der Liste (Typ `krampus`), ohne Knopf.
- **Eltern:**
  - Bearbeiten-Blatt mit Art „Gutschein · Motiv + Satz · Sterne · Krampus“, bei Sterne die Sorte (normal/Jackpot/Niete) und den Schalter **„Beide am selben Tag“** (`role="switch"`).
  - Im Raster: Tür 6/24 „fest“, gemeinsame Türen „= beide“, Krampus dunkel.
  - „Zu tun“ bekommt die Krampus-Zeile über denselben Weg wie die Gutschein-Anfragen (`lernZuTun(…, wuensche)`).
- **Mischen:** `lernAdventMischen(basis, versatz)` nach den Regeln in Konzept 13 (Entwurf: `mische()`). Der Server prüft dieselben Regeln in `schule_advent_belegen`.
- **Weihnachts-Ebene v4/v5:** wie Teil B, dazu
  1. die Gruppe `ebenen.fest_unter` zwischen `ebenen.land` und `ebenen.route` (Tönung, Nordlicht), gezeichnet in `zeichneOben()` am aktuellen `z.vb`;
  2. CSS-Schneehaube an `.rk-schwebe-karte::before` und Mütze an `.lr-jw-ecke::after` (beide `pointer-events: none`), nur wenn `lernFestAn()`;
  3. die Lampen in 3 Gruppen animieren statt einzeln.
