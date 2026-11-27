# Vorgabe „Expedition freigeschaltet“ (EX-G) – Expeditionen dem Kind vor die Nase legen

Stand 23.11.2026. Auftrag: `inhalte/AUFTRAEGE.md`, „Auftrag EX – Expeditionen dem Kind vor die Nase legen (23.11.)“, Teil EX-G (Stand `lernen-app` 759fa30).
Entwurf zum Anklicken: `entwurf/expedition.html` (oben umschalten: Handy 400 / Tablet 820, hell / nacht, Bewegung an / aus).
Bilder: `bilder/{handy|tablet}-hell-{fall}.png` und `bilder/handy-nacht-{fall}.png`, Fälle `1-freigeschaltet`, `2-abflugtafel`, `2b-spaeter`, `3a-geschafft`, `3b-fehlerfrei`, `4-sammlung`.
Beispiel erfunden (Kind A, Klasse 5): „Die Wetterstation“ (4 Teile) an der Neumayer-Station III; Stationsnamen und Voraussetzungen aus `inhalte/reise/aufbau-vorschlag.json` und `inhalte/expeditionen/`. Keine Kinderdaten. Nur Vorgabe – kein App-Code, keine Datenbank.

Passt zu: Abschluss-Ansichten (`../abschluss/umsetzung.md`: Szene oben, Blatt unten, **ein** großer Knopf + Textlink, Bewegung ≤ 1,8 s, „weniger Bewegung“ = Endzustand), „abgelegt“ (`../abgelegt/umsetzung.md`: **Gold nur für „abgelegt“**) und Reisekarte (`../karte/umsetzung.md`: Antarktis als eigener Bereich, Startknopf in der Karte).

## 0 Heute (gelesen in `lernen.js`, 759fa30)
Kasten `lernExpeditionAngebot` irgendwo auf der Abflugtafel („⛰ EXPEDITION“, Zweitknopf „Expedition starten ›“), Kopf der Expedition „⛰ EXPEDITION · FREIWILLIG“, Abschluss als kleiner Kasten „⛰ EXPEDITION ABGESCHLOSSEN“, Reisepass-Zeile „⛰ Expeditions-Stempel: n“. Kein Ereignis beim Freischalten, keine sichtbare Belohnung vorher.

## 1 Regeln für alle Ansichten
- Das Wort **„freiwillig“** (und „Kür“, „Zusatz“) steht bei Expeditionen nirgends auf der Kinderseite. Wort ist **„Expedition freigeschaltet“**. Eltern/Lehrer-Seiten bleiben, wie sie sind.
- Die Expedition **sperrt nichts**: Auf jeder Expeditions-Ansicht ist der nächste Flug mit einem Tipp erreichbar.
- **Farbe Polar** (Nachtblau `#0A2540`, Eisblau `#7FE3F0`, Polarlicht-Grün `#4BE3A6`, Stempel `#1D6E8C`). Nicht Gold (= abgelegt), nicht Siegelrot (= Ort-Stempel). Sterne-Zahlen wie überall in Sternfarbe.
- Zeichen: ⛯ (Leuchtturm/Station) statt ⛰ – passt zur Antarktis-Station. Keine Emojis in Überschriften.
- Szene ist hell und nacht gleich, das Blatt folgt der Gestaltung (wie Abschluss).
- Texte für Klasse 5; „Station {nr} von {gesamt}“ zählt alle Expeditionen über alle Klassen (heute 21), Nummer = feste Reihenfolge aus dem Reise-Aufbau.

## 2 Ansicht 1 – „Expedition freigeschaltet“ (Ereignis)
**Wann:** nach der Landung (Etappe gelandet, Ansicht 1a/1b/1c), die die **letzte** Voraussetzung einer Expedition erfüllt. Die Landungs-Ansicht bleibt unverändert; ihr großer Knopf führt **zuerst hierher**, „Später“ führt dorthin, wohin der Knopf sonst geführt hätte. Einmal je Kind und Expedition (Server: `angeboten_seit`).
Wird eine Expedition ohne Landung frei (Teilung, „Kann er“ der Eltern, neue Expedition eingespielt): Ansicht 1 beim nächsten Öffnen der Startseite, einmal.

Szene (Polarnacht, Polarlicht, Schnee, Eisfläche, Station mit Fahne):
- oben `ANTARKTIS · STATION {nr} VON {gesamt}`
- Titel **`EXPEDITION FREIGESCHALTET`**
- Satz `{Titel} an der {Station}. {n} Teile, a bis {letzter Buchstabe} – alles, was du dafür brauchst, hast du gelandet.` ({Titel} fett)
- Chips je Voraussetzung: `✓ {Etappen-Titel}`

Blatt:
- links `★ 150` / `für die Expedition` / `★ 200, wenn alle Teile im ersten Versuch ohne Tipp klappen`
- rechts Stempel-Vorschau (klein) / `Neuer Stempel für deine Sammlung`
- mehrere zugleich frei: darunter `+{k} weitere Expedition(en) freigeschaltet` (angezeigt wird die mit der kleinsten Stationsnummer)
- Knopf **`Jetzt starten`** / klein `Teil a von {n} · etwa {min} Minuten` ({min}: Annahme 4 Minuten je Teil, aufgerundet auf 5; besser vom Server aus der Antwortzeit des Kindes)
- Textlink `Später`

Bewegung (≤ 1,8 s): Polarlicht weht ein, Blatt fährt hoch. Handy 400 × 780 ohne Scrollen.

## 3 Ansicht 2 – Karte auf der Abflugtafel / Startseite „Meine Reise“
Solange eine Expedition **angeboten oder begonnen** und nicht „später“ ist: **oberste und größte Karte**, vor „Gerade dran“.
- Reisekarte (Handy/Tablet): in der schwebenden Kartenzone unten **über** „Gerade dran“; „Gerade dran“ wird dabei einzeilig-schmal (Text + gelber Knopf `Weiter in {Stadt} ›`), bleibt aber immer sichtbar. Rechner ab 1100 px: oben in der rechten Spalte.
- Solange die Reisekarte noch nicht gebaut ist (heutige Abflugtafel): gleiche Karte als erstes Element über „Jetzt dran“.

Texte:
- `⛯ EXPEDITION FREIGESCHALTET` + Marke `NEU` (nur am Lerntag des Freischaltens)
- Titel groß, darunter `{Station} · Antarktis · Station {nr} von {gesamt}`
- Teile-Kästchen `a b c d …` (gelöst grün, aktuelles mit Ring), rechts `★ 150` / klein `★ 200 ohne Fehler` (ist ein Teil schon nicht mehr fehlerfrei: nur `★ 150`)
- Knopf **`Expedition starten`** bzw. begonnen **`Weiter mit Teil {k}`**, klein `Teil {k} von {n} · etwa {min} Minuten`
- mehrere offen: die begonnene, sonst kleinste Stationsnummer; Zeile `+{k} weitere warten im Reisepass`
- kleines `✕` oben rechts = „Später“

Check-in (WD) bleibt vor allem anderen: Steht „Vorher kurz einchecken“ an, sitzt diese Zeile in „Gerade dran“; die Expeditions-Karte bleibt oben, ihr Knopf startet trotzdem direkt die Expedition (sperrt nichts, wird nicht gesperrt).

## 4 Nach „Später“ (Ansicht 2b)
Bis zum Ende des Lerntags: statt der großen Karte ein Chip über „Gerade dran“ – **`⛯ Expedition wartet: {Titel} ›`** (öffnet Ansicht 1 ohne Bewegung). „Gerade dran“ wieder normal groß. Am **nächsten Lerntag** ist die große Karte wieder oben (Server: `spaeter_bis` = Ende des Lerntags; zählt Lerntage, nicht Kalendertage). Kein Zähler, keine Mahnung, kein „verpasst“.

## 5 Ansicht 3 – nach geschaffter Expedition
Ersetzt den heutigen Kasten „EXPEDITION ABGESCHLOSSEN“. Aufbau wie „Flug geschafft“: Szene + Blatt, Textlink `Überspringen ›` oben rechts.

**3a – geschafft (150 ★):** mindestens ein Teil mit Fehler, zweitem Versuch oder Tipp.
- oben `ANTARKTIS · STATION {nr} VON {gesamt}`, Titel **`EXPEDITION GESCHAFFT`**, Satz `{Titel} – alle {n} Teile gelöst.`
- Stempel knallt auf (0,5 s): `ANTARKTIS` / **`{STATION}`** / `STATION {nr}/{gesamt} · {Datum}`
- Blatt: `★ +150` / `für die Expedition` · `{k} / {gesamt}` / `Stationen in deiner Sammlung`
- Satz `Bei der nächsten Expedition gibt es ★ 200, wenn alle Teile im ersten Versuch ohne Tipp klappen.` (nur, wenn noch eine Expedition offen oder gesperrt ist). Keine Fehlerzahl, kein Vergleich.

**3b – fehlerfrei (200 ★):** alle Teile im ersten Versuch richtig, kein Tipp (Regel EX-S).
- eigene Szene: Polarlicht über den ganzen Himmel, Grün statt Blau
- Titel **`FEHLERFREI DURCHGEKOMMEN`**, Satz `{Titel} – alle {n} Teile im ersten Versuch, ohne Tipp.`
- Stempel mit Band **`★ FEHLERFREI`** (bleibt so in der Sammlung)
- Blatt: `★ +200` / `150 für die Expedition` / `+ 50 fürs fehlerfreie Lösen` · Sammlung wie 3a

Beide: ein großer Knopf zum nächsten Flug in dessen Farbe (gelb): `Weiter in {Stadt}` / klein `{Flug} · Etappe {i} von {m}`; ist der Flug-Test dran `Weiter: Flug-Test`; nichts im Plan `Zur Reise`. Textlink `Stempel-Sammlung ansehen`. Einmal je Kind und Expedition; die Teile-Antworten bleiben über „Expedition ansehen“ in der Sammlung erreichbar.

## 6 Ansicht 4 – Stempel-Sammlung (Reisepass)
Neuer Abschnitt im Reisepass, erreichbar auch über „Stempel-Sammlung ansehen“ und über die Antarktis in der Welt-Ebene der Reisekarte (dort: `Expeditionen · {k} von {gesamt} Stationen`, wie Reisekarte §2; Station antippen → dieselbe Info wie hier).
- Kopf: `REISEPASS · EXPEDITIONEN` / **`Antarktis`** / **`{k} von {gesamt} Stationen`** + `· {f} freigeschaltet` (wenn > 0), Fortschritts-Balken Eis → Polarlicht.
- Gruppen je Klasse der Expedition: `KLASSE {x} · {n} STATIONEN`.
- **Ein Platz je Station**, Kurzname darunter (ganzes Wort, nie abgeschnitten):
  - geschafft: kleiner Stempel (`ANTARKTIS` / Nummer / ✓), mit Band `★ FEHLERFREI`, wenn so geschafft
  - freigeschaltet: grün gestrichelt, `{nr}` / `frei`, einmal Puls
  - begonnen: grün gestrichelt, `Teil {k}/{n}`
  - gesperrt: graue gestrichelte Lücke mit Nummer und 🔒
- **Gesperrt antippen** (Blatt, Handy von unten): `STATION {nr} VON {gesamt} · GESPERRT` / **`{Station}: {Titel}`** / `Noch {k} Etappe(n), dann ist sie frei:` / Liste aller Voraussetzungen `✓ {Etappe}` bzw. **`○ {Etappe}`** `· {Flug}` (fehlende fett) / `Die Etappen kommen in deinem Plan.` bzw. `Diese Etappen sind noch nicht in deinem Plan.` / `★ 150 · ★ 200 ohne Fehler`. Gesperrt durch Klasse statt Etappen: `Ab Klasse {x}`.
- Frei/begonnen antippen: Ansicht 1 ohne Bewegung (Knopf `Jetzt starten` bzw. `Weiter mit Teil {k}`). Geschafft antippen: Stempel groß, `Geschafft am {Datum}` (+ ` · fehlerfrei`), Textlink `Expedition ansehen`.
- Die heutige Zeile „⛰ Expeditions-Stempel: n“ im Reisepass wird zu `⛯ Expeditionen: {k} von {gesamt} Stationen ›` (führt in diese Sammlung).

## 7 Reisekarte (Antarktis)
Ergänzt `../karte/umsetzung.md` §2/§4:
- Welt-Ebene: Antarktis-Bereich zeigt `Expeditionen · {k} von {gesamt} Stationen`; ist eine Expedition freigeschaltet, pulsiert ihr Stations-Pin (Polarlicht-Grün) und die Zeile lautet `⛯ 1 Expedition freigeschaltet`.
- Stationen als Pins nach Breite/Länge (`aufbau-vorschlag.json`, `expeditionen[]`): geschafft Stempel-Blau mit ✓, frei grün mit Puls, gesperrt grau mit 🔒; Antippen = Blatt wie §6.
- Hinweis zur Reisekarte §11 („Zusatz – freiwillig, für Entdecker“): Satz des Nutzers „wenn da irgendwo freiwillig steht, machen sie es nie“ trifft dort genauso. Vorschlag, nicht Teil von EX: dort `Zusatz für Entdecker` ohne „freiwillig … Muss nicht sein“.

## 8 Daten (Schnittstelle; Umsetzung EX-S)
| Angabe | heute | neu |
|---|---|---|
| je Expedition `id`, `titel`, Teile, Voraussetzungen | ja | – |
| `station`, `nr` (Reihenfolge), `gesamt` | Station im Reise-Aufbau | in `schule_konto.expeditionen[]` mitliefern |
| Zustand je Kind `gesperrt` / `angeboten` / `begonnen` / `geschafft` | angeboten/begonnen/geschafft | `gesperrt` mit `fehlt: [{etappe, flug, im_plan}]` bzw. `ab_klasse` |
| `angeboten_seit`, `spaeter_bis` | – | EX-S (Ansicht 1 einmal, Karte nach „Später“) |
| `fehlerfrei` (alle Teile erster Versuch ohne Tipp), `sterne` 150/200, `geschafft_am` | 50 ★ | EX-S (Regelwerte) |
| Auslöser „gerade freigeschaltet“ in der Antwort, die die Etappe landet | – | `expedition_frei: [id]` in der Landungs-Antwort |
| `teil_k`, `noch_fehlerfrei` (für Ansicht 2) | teilweise | EX-S |
Fehlt ein neues Feld (alter Server): App zeigt die Karte ohne Belohnungs-Zeile und ohne Ansicht 1 – nie „freiwillig“.

## 9 Fertig, wenn (Prüfen nach dem Bau)
- Nirgends auf der Kinderseite „freiwillig“ bei Expeditionen.
- Landung der letzten Voraussetzung → Landungs-Ansicht → Ansicht 1 (einmal); „Später“ führt dorthin, wo der Landungs-Knopf hinführte.
- Startseite: offene Expedition ist oberste, größte Karte; „Gerade dran“ bleibt sichtbar und tippbar. Nach „Später“ Chip bis Lerntag-Ende, am nächsten Lerntag wieder groß.
- 3a/3b nach Regel; Sterne aus dem Server (150/200), nicht in der App gerechnet.
- Sammlung mit allen Stationen, gesperrte zeigen genau die fehlenden Etappen.
- 400 × 780 ohne Scrollen bei 1, 3a, 3b; 360 × 640 mit Blatt scrollbar; 820; hell und nacht; „weniger Bewegung“; keine Wörter mitten im Wort umbrochen oder abgeschnitten; Testkind und erfundene Daten.
