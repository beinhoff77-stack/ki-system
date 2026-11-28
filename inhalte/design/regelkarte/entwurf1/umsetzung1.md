# Regelkarte unter dem Fehler – Entwurf 1: Umsetzung

Stand 28.11.2026, Zweig `helfer-regelkarte`. **Nur Entwurf, kein App-Code.** Grundlage: Entscheidungen des Nutzers vom 27.11., Vertrag `regelbezug` (`inhalte/plan/regelbezug.md`, Abschnitt „Was der Client später braucht“; Kopfkommentar `supabase/migrations/20261204_rb_s_regelbezug.sql`).

## Dateien

| Datei | Was |
|---|---|
| `index.html` | der Entwurf, eine Datei ohne Netz (Schriften und Regeldaten eingebettet). Schalter in der Adresse, oben ein Entwurfs-Streifen zum Umschalten |
| `vorlage.html`, `bauen.py` | Quelle; `python3 -I inhalte/design/regelkarte/entwurf1/bauen.py` holt Schriften aus `vendor/schriften` und die Beispielregeln aus `daten/regeln-universum.json` |
| `bilder.cjs` | Bildschirmfotos (Playwright aus dem Haupt-Checkout, lokales Chromium) → `bilder/` |
| `bilder/*.png` | jede Variante 390 hell/dunkel; 1280 hell/dunkel für Lerneinheit endgültig und Test-Ergebnis; 820 hell für endgültig, Test und Regel-Seite |

Schalter: `#z=erst|end|ohne|checkin|misch|knobel|test|regel` · `#r=minus|stellenwert|waage|prozent` · `#g=nacht` · `#k=beispiel` (Gewand-Zeile mit Rechenbeispiel statt Orten) · `#bild=auf` (Bild im 1. Fehlversuch offen) · `&foto` (ohne Streifen und Notizen). Beispiel: `index.html#z=end&r=waage&g=nacht`.

Beispielregeln (Aufgaben erfunden, Regeln echt): `minus` = Rechenregel 7, Kl. 7, Lücken, mit Bild · `stellenwert` = Rechenregel 1, Kl. 5, Zahl mit Kurskorrektur · `waage` = Regel der Bordkarte `rr.waage`, `fehlbild_regel` = `rr.minusklammer` (abweichend), Kl. 8 · `prozent` = Idee „Prozent als Faktor“, Kl. 7, **ohne Bild vorgeführt**.

## Was der Entwurf zeigt (Bilder)

| Bild | Zustand |
|---|---|
| `01-erst-minus-390-*` | (a) erster Fehlversuch: nur Regel, Bild zugeklappt |
| `13-erst-bild-offen-390-*` | (a) mit aufgeklapptem Bild |
| `04-erst-stellenwert-390-*` | (a) Klasse 5, „Kommt wieder in“ (keine frühere Klasse) |
| `02-end-minus-{390,820,1280}-*` | (b) endgültig: Richtig ist → Du hast vermutlich … → Regel + Bild → So geht’s; ab 1100 px rechts „Heute“ zum Vergleich |
| `05-end-stellenwert-{390,1280}-*` | (b) mit Kurskorrektur (Zahl) |
| `06-end-waage-abweichend-{390,1280}-*` | (b) `fehlbild_regel` ≠ `regel`: Karte zeigt die verletzte Regel („Hier hat es gehakt“), darunter eine Textzeile „Die Bordkarte selbst übt: Gleichung als Waage ›“ |
| `07-end-prozent-ohne-bild-390-*` | (b) Regel ohne Bild |
| `03-ohne-minus-390-*` | (c) kein `regelbezug`: unverändert wie heute |
| `08-checkin`, `09-misch`, `10-knobel` | kompakte Karte |
| `11-test-ergebnis-{390,820,1280}-*` | Zusatzvorschlag: Test-Ergebnis nach Regel gruppiert |
| `12-regel-seite-{390,820}-*` | Kopf der Regel-Seite mit „Zurück zur Bordkarte“ |

## Entwurfsentscheidungen

1. **Eine Karte, nicht zwei.** Fehlbild-Satz und Regel stehen in *einer* Karte: oben „Du hast vermutlich …“, gestrichelte Linie, darunter „Die Regel dazu“. Weicht `fehlbild_regel` ab, zeigt die Karte die verletzte Regel mit der Überschrift „Hier hat es gehakt“; die Regel der Bordkarte steht nur als leiser Textlink darunter. So gibt es nie zwei gleich laute Regelkarten.
2. **Reihenfolge (b), in 10 Sekunden lesbar:** ✕ + „Richtig ist: …“ (1 Zeile) → Kurskorrektur (nur Zahl, wie heute) → „Du hast vermutlich …“ → Name + Merksatz (gelber Merksatz-Kasten wie im Regel-Universum, `.ru-merk`) → Bild → „So geht’s“ → „Die nächste zählt wieder voll.“
3. **(a) ruhig halten.** Beim ersten Fehlversuch bleibt das Tastenfeld mit „Prüfen“ der Hauptknopf. Die Karte zeigt Name, Merksatz, Gewand-Zeile, Nebenknopf „Regel ansehen ›“ und das Bild **zugeklappt** („▸ Bild zur Regel zeigen“), damit das Tastenfeld nah bleibt (ca. 350 px Karte statt ca. 560 px mit Bild). Nach der endgültigen Antwort ist das Bild offen.
4. **Bild:** Die Zeichnungen der Regeln sind 320 Einheiten breit mit Schrift 14–18; verkleinert wären sie unter 13 px. Deshalb in voller Kartenbreite (max. 360 px), ab 760 px Breite rechts neben dem Merksatz (300 px). Es wird nur das **erste** Bild der Regel (`zeichnungen[id][0]`) mit Satz und Rechenzeile gezeigt.
5. **„Dieselbe Regel, anderes Gewand“:** eine Zeile mit Ring-Zeichen aus der Klassenleiter (`leitern[id].stufen`): „Kennst du aus: **Florenz**, Kl. 6 · **Rom**, Kl. 5“ – die Orte der Reise, nicht Lehrplan-Namen, weil die Kinder die Orte kennen. Früher gesehene Klassen (≤ eigene Klasse, anderes Thema als die Bordkarte), die nächste zuerst; gibt es keine, „Kommt wieder in: …“. Passen zwei Orte nicht in eine Zeile, bleibt nur der nächste stehen (nie abgeschnitten). Auf der Regel-Seite steht die ganze Leiter: „Dieselbe Regel in jeder Klasse“ mit dem Rechenbeispiel jeder Klasse, die markierten Stellen gelb (`pos`), „✓ schon gesehen“ / „● hier bist du“ / „kommt noch“. Variante `#k=beispiel`: Zeile mit Rechenbeispiel statt Orten (siehe offene Frage 2).
6. **Kompakt (Check-in, Misch, Knobel):** gelbe Randlinie statt Kasten, Fehlbild-Satz, Name, Merksatz in normaler Schrift, Gewand-Zeile, Textlink „Regel ansehen ›“. Kein Bild.
7. **Test-Ergebnis (Zusatzvorschlag):** oben „4 von 9 richtig“, Balken (gefüllt = richtig, leer = falsch, also nicht nur Farbe), Satz „Deine 5 Fehler hängen an 2 Regeln.“ Je Regel eine Gruppe mit Regelkarte (ohne Bild) und „Bordkarten zeigen (3)“ zum Aufklappen; größte Gruppe zuerst; Fehler ohne Regel in eigener Gruppe; Richtige zusammengeklappt. Knöpfe unten unverändert.
8. **Rückweg:** Band oben auf der Regel-Seite (bleibt beim Rollen stehen): „Bordkarte 3 · Samarkand – dein zweiter Versuch wartet.“ und Nebenknopf „‹ Zurück zur Bordkarte“; derselbe Knopf noch einmal am Ende der Seite.
9. **Nicht nur Farbe:** ✕ / ↻ / ✓ als Zeichen vor jeder Rückmeldung; Test-Balken gefüllt/leer; Gruppen mit Wort („3 FEHLER“, „4 RICHTIG“).

### Benutzte Knopfarten (keine neue)
- **Hauptknopf gelb** (`.lr-knopf`): unverändert „Prüfen“ (Tastenfeld), „Neue Bordkarte ›“, „Nächste Bordkarte ›“, „Erst üben: … ›“.
- **Nebenknopf** (`.lr-knopf-zweit`, 48 px): „Regel ansehen ›“ in (a), (b) und Test; „‹ Zurück zur Bordkarte“ auf der Regel-Seite.
- **Textlink** (`.lr-textlink`): „Regel ansehen ›“ kompakt; „▸ Bild zur Regel zeigen“; „Die Bordkarte selbst übt: … ›“. **Höhe 44 px** statt heute 32 px (`style.css` Zeile 3610) – sonst ist die Tippfläche zu klein.

### Feste Wortlaute
| Stelle | Text |
|---|---|
| 1. Fehlversuch, Kopf | Noch nicht – du hast einen zweiten Versuch. (wie heute) |
| Kartenkopf | DIE REGEL DAZU · rechts „Rechenregel 7“ bzw. „Idee · Geld und Verhältnisse“ |
| Kartenkopf, abweichende Regel | HIER HAT ES GEHAKT |
| Bild | ▸ Bild zur Regel zeigen / ▾ Bild ausblenden |
| Knopf | Regel ansehen › |
| Gewand | Kennst du aus: … / Kommt wieder in: … |
| Fehlbild | Du hast vermutlich ‹text›. (Regel siehe unten) |
| Abweichend | Die Bordkarte selbst übt: ‹Name› › |
| Endgültig, Kopf | NOCH NICHT bzw. FAST – KURSKORREKTUR · Richtig ist: … (wie heute) |
| Weg | So geht’s: … (wie heute) |
| Test, Satz | Deine 5 Fehler hängen an 2 Regeln. Schau dir zuerst die Regel an, dann deine Bordkarten. |
| Test, Gruppen | 3 FEHLER · DIESELBE REGEL / 1 FEHLER / 1 FEHLER OHNE REGELKARTE / ✓ 4 RICHTIG |
| Test, Aufklappen | Bordkarten zeigen (3) / Bordkarten verbergen (3) |
| Test, Balken | gefüllt = richtig · leer = falsch |
| Regel-Seite, Band | Bordkarte 3 · Samarkand – dein zweiter Versuch wartet. / … – deine Antwort und der Lösungsweg bleiben stehen. / … – zurück zum Test-Ergebnis. |
| Regel-Seite, Knopf | ‹ Zurück zur Bordkarte |
| Regel-Seite, Leiter | Dieselbe Regel in jeder Klasse · Sie sieht jedes Jahr etwas anders aus – die Regel bleibt gleich. · ✓ SCHON GESEHEN / ● HIER BIST DU / KOMMT NOCH |

## Welche Daten woher

| Anzeige | Quelle |
|---|---|
| Regel-Kennung | `r.regelbezug.regel`; fehlt sie: `inhalte/plan/regelbezug-lernkarten.json` → `themen[<thema ohne _teilN>].lernkarten[<lernziel>].regel` (bei `quelle: offen` keine Karte) |
| angezeigte Regel | `fehlbild_regel` falls vorhanden, sonst `regel` |
| Kennung → Eintrag | `daten/regeln-universum.json`: `leitern[<id>].kennung` ist die Kennung; daraus `id` (`R7`, `I-geld-3`). Für den Client eine kleine Umkehrtabelle beim Laden bauen (`ruIndex` hat alles Nötige) |
| Name, Merksatz | Rechenregel: `regeln[].name`, `.satz`; Idee: `planeten[].ideen[].kurz`, `.satz` |
| Art rechts im Kopf | Rechenregel `nr` bzw. `Idee · <Planet>` |
| Bild | `zeichnungen[<id>][0]`: `svg`, `satz`, `gl` (Farben über `--z-…` wie in `lernen-regeln.css`). **Heute haben alle 42 Einträge ein Bild**; der Fall „ohne Bild“ gilt für künftige Regeln und wenn die Datei noch nicht geladen ist |
| Gewand-Zeile, Leiter | `leitern[<id>].stufen` (`klasse`, `thema`, `text`, `pos`), Ort über `themen[<schluessel>].ort`; eigene Klasse aus `kind.klasse`, aktuelles Thema aus der Einheit |
| Adresse Regel-Seite | `#/regeln/<kind>-<adr>`: Rechenregel `r7` (`adr.regel`), Idee `idee-geld-3` (`adr.idee`) |
| Fehlbild-Satz | `regelbezug.text`; nur bei endgültiger Antwort |
| Test-Gruppen | Test-Antwort hat **kein** `regelbezug` (Plan, „WAS NICHT“): je Ergebnis `x.lernziel` + Thema der Einheit → `regelbezug-lernkarten.json`. Kein Fehlbild-Satz im Test |

`daten/regeln-universum.json` lädt heute erst das Regel-Universum (`ruDatenHolen`). Für die Karte muss die Lerneinheit sie (oder einen kleinen Auszug) vorab holen; der Service Worker hält sie schon offline. Vorschlag: `ruDatenHolen()` im Hintergrund starten, wenn die Lerneinheit öffnet; ist sie bei der Rückmeldung noch nicht da, nur Name aus `kennungen` – oder keine Karte (Rückmeldung wie heute). `regelbezug-lernkarten.json` gehört dann in die Cache-Liste von `sw.js` (oder `tools/regeln_bauen.cjs` übernimmt die Zuordnung in die Universum-Datei, siehe Plan).

## Was in `lernen.js` wo zu ändern wäre

(Zeilen Stand `origin/lernen-app` d8ecae38.)

1. **Neue Bausteine** (bei `lernDetektiv`, ca. Zeile 3263): `lernRegelkarte(rb, { modus: 'erst'|'end'|'kompakt'|'test', kind, thema, rueckweg })`, `lernGewand(id, klasse, thema)`, `lernFehlbildSatz(text)`, `lernRegelAdresse(kind, kennung)`.
2. **Lerneinheit, 1. Fehlversuch** (Zeile 4529–4536): in den Kasten `lr-rueck-nochmal` nach dem Kopf `lernRegelkarte(r.regelbezug, { modus: 'erst' })`. Der bestehende Hinweis (`LERN_GRUND`/Tipp) bleibt zwischen Kopf und Karte; „Tipp:“-Text bleibt wie heute.
3. **Lerneinheit, endgültig** (Zeile 4589–4601): nach `lernKurs`/„Richtig ist“ die Karte (`modus: 'end'`); `lernDetektiv(…)` nur, wenn kein `r.regelbezug?.text` (sonst doppelt). „So geht’s“ nach die Karte. Gilt für beide Gestaltungen (`neu` und alt).
4. **Reihenfolge der Kästen** (Zeile 4680/4687: `hilfeBox, meldung`): `meldung` direkt unter die Bordkarte, `hilfeBox` darunter – behebt die gemessenen 177 px Abstand.
5. **Mischkarte**: derselbe Weg wie 3, aber `modus: 'kompakt'` wenn `a.misch`.
6. **Knobel** (Zeile 369): im falschen Zweig `lernRegelkarte(r.regelbezug, { modus: 'kompakt' })` nach „Richtig ist“.
7. **Check-in/Wiederholen** (Zeile 7507): ebenso, `modus: 'kompakt'`, vor „Kein Problem – …“.
8. **Flug-Test-Ergebnis** (`lernTestErgebnis`, Zeile 5155 ff.) – nur falls der Nutzer den Zusatz will: die Liste `r.ergebnisse` nach Regel (aus Lernkarte) gruppieren, Summe oben, `<details>` je Gruppe; `lernTestKnoepfe` bleibt.
9. **Rückweg**: Beim Tippen auf „Regel ansehen“ schreibt die Lerneinheit `sessionStorage['lr-rueckweg'] = { hash, aufgabe_id, anlauf, cid, antwort (auf.antwort()), modus, zeit }` und geht auf `#/regeln/<kind>-<adr>`. `lernen-regeln.js` (`ruAufbauen`, Zeile 847 ff.) zeigt das Band, wenn ein Rückweg da ist und jünger als 30 Minuten; „Zurück zur Bordkarte“ = `history.back()`, sonst `location.hash = rueckweg.hash`. Die Lerneinheit prüft beim Aufbau den Rückweg: gleiche Aufgabe → diese Bordkarte statt der nächsten aus `warte` zeigen, `anlauf`/`cid` übernehmen, Eingabe wieder einsetzen (1. Fehlversuch) bzw. Rückmeldung mit Lösung wieder anzeigen (endgültig; die Antwort des Servers dafür im Rückweg mitspeichern, denn die Seite wird neu gebaut). Danach Rückweg löschen. Kein Serveraufruf, keine Bewertung ändert sich; dieselbe `client_id` sorgt dafür, dass nichts doppelt zählt.
10. **CSS** (`style.css`, Kinderseiten `lr-…`): Klassen `rk-…` aus `vorlage.html` übernehmen (Karte, Merksatz, Bild, Gewand, kompakt, Test-Gruppen, Band); `.lr-textlink` auf `min-height: 44px`.
11. **Erklärkarte** (Wunsch 27.11.): unter `lernErklaerung` dieselbe kompakte Karte ohne Fehlbild-Satz, Regel aus `regelbezug-lernkarten.json`. Nicht im Bild, gleicher Baustein.

## Fehlbild-Satz: Satzteil oder ganzer Satz

Die Texte der Dateien sind meist Satzteile („das Minus vergessen“, „4 + 7 gerechnet“) → „Du hast vermutlich das Minus vergessen.“ Etwa 500 von 5 700 sind ganze Sätze (Fehler-Detektiv-Aufgaben: „Diese Zeile ist richtig, weil … Der erste Fehler steht früher.“, auch klein: „diese Zeile ist richtig; der Fehler steckt woanders“). Entwurf: beginnt der Text groß oder enthält „;“ bzw. „. “, steht er für sich (erster Buchstabe groß), sonst mit „Du hast vermutlich … .“ davor. Besser auf Dauer: der Mathe-Profi kennzeichnet ganze Sätze in der Datei (Hinweis an ihn, keine Frage an den Nutzer).

## Bewusst NICHT geändert

- Bewertung, zweiter Versuch, Sterne, Folge, Warteschlange, Form-Takt, Sticker, „Ändern lassen“, Knöpfe nach dem Test.
- Ohne `regelbezug` (und ohne Lernkarten-Regel) bleibt jede Rückmeldung Zeichen für Zeichen wie heute (Bild `03-ohne-…`).
- Kein Fehlbild-Satz beim ersten Fehlversuch (Entscheidung 27.11.).
- Expeditionen: keine Karte (Server schickt dort kein `regelbezug`).
- Server, Datenbank, `regelbezug`-Vertrag, `daten/`, `sw.js`, `tests/`: nichts angefasst.

## Offene Fragen an den Nutzer

1. **Bild beim ersten Fehlversuch:** (A) zugeklappt, ein Tipp zeigt es (Entwurf) · (B) immer offen (Tastenfeld rückt ca. 210 px nach unten).
2. **Zeile „Dieselbe Regel, anderes Gewand“:** (A) Orte der Reise: „Kennst du aus: Florenz, Kl. 6 · Rom, Kl. 5“ (Entwurf) · (B) ein Rechenbeispiel aus der früheren Klasse: „Schon in Rom, Kl. 5: 20 − (8 − 3) = 20 − 8 + 3“ (`#k=beispiel`).
3. **Test-Ergebnis nach Regel gruppiert:** (A) gleich mit der Regelkarte bauen · (B) später getrennt · (C) gar nicht.
