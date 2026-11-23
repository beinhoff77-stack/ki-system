# Zweite Prüfung RK-App – Reisekarte, App 0.92.2 (Zweig lernen-app, 7c7e4bc), 23.11.2026

Geprüft gegen `kind/karte/umsetzung.md` und meine erste Prüfung `kind/karte/nachpruefung_rk.md` (M1, S1–S7, K1–K5). Grundlage: Meldung `bau-motivation.md` „FERTIG: RK-App 2 (App 0.92.2)“, Bilder `docs/previews/la/rk2-*.png`, Code `lernen.js` (`lernReisekarte`, `lernRkPin`, `lernRkZustand`). Felder „gesperrt/abgelegt“: `bau-lehrer.md` „FERTIG: RK-D / RK-D 2“.

**Wie geprüft:** 400 × 860, 820 × 1180, 1280 × 800, Tag und Nacht; Testkind, erfundener Stand auf den echten Reise-Aufbau-Daten (nachgestellter Server der Testsuite). Gemessen wurde mit Kästen (Überdeckung von Kopf-Knöpfen, Länder-Schildern, Haltestellen, Kontinent-Namen) und echten Klicks. Eigene Bilder liegen in `nachpruefung2/`. Für Frage 3 habe ich zwei Kinder mit den genannten Zahlen nachgestellt (95 Flüge; Kl. 5: 68 gesperrt, 26 im Plan, davon 9 gesperrt auf Platz 3, 7, 8, 11, 14, 17, 20, 23, 25; Kl. 8: 31 gesperrt, 44 im Plan, 2 gesperrt). Die beiden Darstellungen A und B habe ich nur im Prüf-Browser auf die Pins gelegt. **Die App selbst liest die Felder `gesperrt`/`abgelegt` noch nicht** – in `lernen.js` kommen sie in der Reisekarte nicht vor; das ist Fakt.

## Ergebnis

**0.92.2 kann aus meiner Sicht live gehen, sobald Muss M1 (Kopfzeile auf dem Handy) behoben ist.** Alles andere ist Soll/Kann. Die Sperr-Anzeige (Frage 3) muss spätestens **mit** dem Einspielen von RK-D fertig sein, nicht vorher live.

## 1) Erste Prüfung: M1 und S1–S7

| Punkt | Stand | Stelle / Nachweis |
|---|---|---|
| **M1** „wieder offen“ eigener Zustand | **erfüllt** | Land-Ebene alle Größen: Pompei orange mit ↻, gestrichelter Ring, Unterzeile „wieder offen“, kein ✓ (`land-*.png`); Liste rechts „wieder offen – nachbessern“ (1280); Land-Pin Italien mit orangem ↻ (`kontinent-*.png`); Vorlesetext stimmt. Offen nur die Legende (es gibt keine Kartenlegende) → K4. |
| **S1** Rechner fensterfüllend | **erfüllt** | 1280: Kopf eine Zeile (‹ · Meine Reise · Pfad · Zu mir · Abflugtafel · ★ · ≡), Karte bis unten, Seite rollt nicht (gemessen). |
| **S2** Handy kompakt | **teilweise** | Schwebekarte kompakt (Bologna · in Italien · 3/6 · Knopf) und Expeditionszeile einzeilig: erfüllt. **Kopfzeile 400 überdeckt sich** → neues Muss M1. |
| **S3** x/6 statt 4/13 | **erfüllt** | Schwebekarte/rechte Spalte „3/6“ mit 6 Strichen, Haltestelle „Bologna · 3/6“, Text „Stadt 5 von 13“. |
| **S4** Land-Ebene Ausschnitt und Namen | **teilweise** | Rahmen um die Route und alle 13 Namen ohne Überdeckung: erfüllt. **Haltestellen-Kästchen überdecken sich** (400: 6 Paare – 11/12/13 bei Pisa/Florenz/Siena, 6/7; 820 und 1280: Neapel ✓ halb unter Pompei ↻) → Soll S1. |
| **S5** Welt auf dem Handy | **erfüllt** | 400/820 Ausschnitt um Europa, keine Überdeckung der Namen, „x/y Länder“ erst nach Hineinzoomen; 1280 alle 9 Namen frei. Anmerkung → K2. |
| **S6** Blatt schließt beim Ebenenwechsel | **erfüllt** | Test und nachgestellt (400). |
| **S7** Zusatz-Text | **erfüllt** | „Zusatz für Entdecker – muss nicht sein.“, kein „freiwillig“ auf der Reisekarte. |
| K1 Puls/Trefferfläche | erfüllt | echter Klick auf den pulsierenden Pin klappt. |
| K2 Kette grau | erfüllt | Kette grau #8C918E, Deckkraft 0,5, dünn (gemessen). |
| K3 Hauptstadt in der Land-Ebene | erfüllt | nur ◉, kein Pin über Rom. |

## Muss

- **M1 – Kopfzeile auf dem Handy (400 px) überdeckt sich; in der Land-Ebene ist „Zu mir“ nicht antippbar und der Name des Landes verdeckt.** Gemessen bei 400 × 860, Tag und Nacht:
  - Kontinent: Pfad 72–218 px, 📍 Zu mir 186–230 px, ▤ Abflugtafel 224–268 px → Pfad liegt unter 📍, 📍 und ▤ überdecken sich um 6 px (Bild `kontinent-400-*.png`).
  - Land: Pfad „🌍 › Europa 📍 › 🇮🇹 Italien 📍“ läuft unter ▤ und ★; „Italien“ ist nicht zu sehen (nur „🇮🇹 I“). 📍 Zu mir liegt bei 289–333 px **ganz unter** ★ 340 (275–334) – ein echter Klick auf „Zu mir“ trifft nicht (nachgestellt, Zeitüberschreitung). Bild `land-400-tag.png`.
  - Warum Muss: Das ist die Hauptansicht auf dem Hauptgerät; ein Knopf ist tot, und die Zeile, die sagen soll „wo bin ich“, ist abgeschnitten.
  - **Änderung:** Auf dem Handy rechts feste Knöpfe in dieser Reihenfolge ohne Überlappung: ▤ · ★ · ≡ (je ≥ 44 px, 4 px Abstand). „📍 Zu mir“ wandert aus dem Kopf in die Kartenknöpfe rechts oben (unter ⤢, gleiche Form wie + − ⤢). Der Pfad bekommt den Rest der Breite und kürzt **von links**: Auf Land-Ebene `‹ … › 🇮🇹 Italien 📍` (Welt und Kontinent als „…“, antippbar → Kontinent), auf Kontinent-Ebene `🌍 › Europa 📍`. Die aktuelle Stufe steht immer ganz, nie unter einem Knopf. Test: Kästen der Kopf-Elemente bei 360 und 400 px ohne Überdeckung, „Zu mir“ per echtem Klick.

## Soll

- **S1 – Haltestellen-Kästchen überdecken sich (Land-Ebene).** 400: 11/12/13 (Pisa, Florenz, Siena) und 6/7 liegen übereinander (Bild `land-400-tag.png`); 820/1280: das ✓ von Neapel steckt zur Hälfte unter Pompei (`land-1280-nacht.png`). Die Namen sind schon frei (S4 erfüllt), die Kästchen nicht. **Änderung:** Gleiches Verfahren wie bei den Namen auch für die Kästchen: Kästchen nach Vorrang (hier bist du, wieder offen, nächste 3, gelandet, Rest) setzen; überdeckt eines ein schon gesetztes, rückt es bis 16 px weg und bekommt eine feine Linie zum echten Ort (Punkt bleibt am Ort). Test wie bei den Namen: Kästchen-Kästen ohne Überdeckung, 400 und 1280.
- **S2 – Länder-Schilder in dichten Gegenden (Frage 2).** Lösung siehe Abschnitt 2.
- **S3 – Sperr-Anzeige nach Abschnitt 3 bauen.** Wird zu Muss, sobald RK-D (`gesperrt`, `gesperrt_grund`, `ab_klasse`, `visum_fehlt`, `abgelegt`) auf dem echten Server eingespielt wird: Ohne Anzeige zeigt die Karte Platz 3 als normalen nächsten Schritt, während die Abflugtafel „Visum fehlt“ sagt – zwei Aussagen zum selben Land.

## Kann

- **K1 – Quellen-Zeile und Pin oben links.** 1280 Land: Schweiz/Bern liegt halb unter „Karte: Natural Earth · Orte: GeoNames“ (`land-1280-nacht.png`). Quellen-Zeile unten links an den Rand oder Pins darunter nicht beschriften.
- **K2 – Welt auf Handy/Tablet zeigt nur Europa.** 400 und 820: In der Welt-Ebene steht nur „EUROPA“ im Bild, sie sieht fast aus wie die Kontinent-Ebene. Ausschnitt so weit, dass die Nachbarn angeschnitten mit Namen sichtbar sind (Afrika, Asien/Orient).
- **K3 – Ostafrika und Benelux auch bei den Pins dicht** (Uganda/Ruanda/Burundi/Kenia, `sperre-kl5-afrika-400-A.png`) – mit Abschnitt 2 (Fächer) erledigt.
- **K4 – Kleine Legende** (ⓘ in den Kartenknöpfen): ✈ gerade dran · Zahl = Platz im Plan · ✓ geschafft · ★ golden · ↻ wieder offen – nachbessern · 🔒 wartet · + Zusatz.

## 2) Länder-Schilder in Mitteleuropa auf dem Handy (bekannt offen)

Nachgestellt bei 400 px: Schilder überdecken sich (Belgien × Vereinigtes Königreich, Polen × Deutschland), dazu liegen Schilder auf fremden Pin-Köpfen (Niederlande und Vereinigtes Königreich auf Belgien, Bild `kontinent-400-tag.png`). Bei 820 und 1280: keine Überdeckung der Schilder. Gleiches Bild in Ostafrika und Südostasien.

**Vorgabe (für alle Kontinente, nur wenn es eng ist – im Wesentlichen das Handy):**
1. **Vorrang beim Beschriften:** gerade dran → nächste 3 freie Plätze → wieder offen → geschafft/golden → übrige im Plan → Zusatz → offen → gesperrt → ohne Flug.
2. **Vier Lagen je Schild:** rechts (wie jetzt), links, oben, unten. Das erste freie Feld gewinnt; „frei“ heißt: kein Schild und **kein Pin-Kopf** darunter.
3. **Kein Platz → Schild weglassen, Pin bleibt.** Der Name kommt beim Hineinzoomen (ab 1,4-fach) oder beim Antippen. Nie zwei Schilder übereinander.
4. **Hauptstadt-Zeile auf dem Handy** nur für gerade dran, die nächsten 3 und das angetippte Land; sonst nur der Landesname. Das halbiert die Schildhöhe.
5. **Köpfe, die sich zu mehr als einem Drittel überdecken** (Benelux, Ostafrika): Fächer – der Kopf mit kleinerem Vorrang rückt bis 14 px schräg weg, die Nadelspitze bleibt an der Hauptstadt.
6. Test: bei 360 und 400 px in Europa, Afrika, Asien keine Überdeckung von Schild/Schild und Schild/Kopf; gerade dran und die nächsten 3 immer beschriftet.

Das Verfahren entspricht dem, was in der Land-Ebene für die Städtenamen schon läuft (S4) – nur mit dem Weglassen als letztem Schritt.

## 3) „gesperrt“ – Wald aus Schlössern?

**Nachgestellt (Bilder `vergleich-kl5-afrika-400.png`, `vergleich-kl5-europa-asien-400.png`, `vergleich-kl8-400.png`, `sperre-kl5-afrika-1280-*.png`):**

| Kind | Ansicht | Pins im Bild | Variante A: Schloss an jedem gesperrten Pin | Variante B: meine Vorgabe |
|---|---|---|---|---|
| Kl. 5 | Afrika (nichts im Plan) | 17 | **17 Schlösser** – jeder Pin hat eins | 0 Schlösser, alles gedämpft |
| Kl. 5 | Asien | 20 | 15 Schlösser | 3 Schlösser (nur eingeplante) |
| Kl. 5 | Europa | 13 | 4 Schlösser (alle eingeplant: Platz 3, 7, 8, 11) | 4 Schlösser |
| Kl. 8 | Afrika | 17 | 9 Schlösser | 0 |
| Kl. 8 | Europa | 13 | 0 | 0 |

**Urteil:** Ja – mit einem Schloss an jedem gesperrten Pin (A) wird die Karte für das Kind in Klasse 5 außerhalb Europas zum Wald aus Schlössern (Afrika 17 von 17, Asien 15 von 20), und das Schloss sagt dort nichts, was hilft: Das Kind kann in Afrika ohnehin nichts tun. Bei Klasse 8 ist es halb so schlimm, aber Afrika hat noch 9. In Europa (Plan) sind die 4 Schlösser dagegen nützlich: Sie sagen „Platz 3 wartet, erst Platz 2“.

**Vorgabe „gesperrt“ auf der Reisekarte:**

1. **Nicht im Plan und gesperrt (Visum oder Klasse): nur gedämpft, kein Schloss.**
   - Pin 40 % Deckkraft, Flagge grau; Schild in Grau, ohne Hauptstadt-Zeile; Land-Fläche 55 %.
   - Wie ein Land ohne Flug – der Unterschied steht erst beim Antippen. Ergebnis: Kl. 5 Afrika ist ruhig grau, „hier ist noch nichts dran“ (Bild B).
2. **Im Plan und gesperrt (nur Visum, Klasse sperrt im Plan nicht – Festlegung RK-D): Schloss.**
   - Platznummer bleibt, aber grau statt gelb; kleines 🔒 unten links am Kopf (Abzeichen-Platz gegenüber der Nummer).
   - Route zu diesem Land grau gepunktet statt gelb.
   - So sieht das Kind in Europa: 2 gelb = geht als Nächstes, 3 grau mit 🔒 = wartet.
3. **Freie Plätze im Plan bleiben gelb**; „gerade dran“ ✈ mit Puls wie jetzt. Schwebekarte/rechte Spalte unverändert („Weiter in Bologna“). Damit ist die Antwort auf „was geht als Nächstes“ immer der Knopf, und auf der Karte das nächste **gelbe** Zahl-Abzeichen.
4. **Grund beim Antippen** (Blatt bzw. rechte Spalte), unter der Flug-Zeile, mit 🔒 vorne:
   - Visum, 1 Land fehlt: `🔒 Erst Kroatien schaffen` + Knopf `Zu Kroatien ›` (wählt das Land auf der Karte, wechselt bei Bedarf den Kontinent).
   - Visum, 2 Länder: `🔒 Erst Kroatien und Ungarn schaffen`; ab 3: `🔒 Erst Kroatien, Ungarn und 1 weiteres Land schaffen` (Reihenfolge wie `visum_fehlt`).
   - Klasse: `🔒 Ab Klasse 7 – kommt später.` (aus `ab_klasse`).
   - Kein Knopf „Städte ansehen“ bei gesperrten Flügen ohne Plan; im Plan bleibt er (Kind darf schauen).
   - Vorlesetext des Pins: „…, wartet – erst Kroatien schaffen“ bzw. „…, ab Klasse 7“.
5. **Land-Ebene eines gesperrten Flugs:** Haltestellen grau ohne Nummernfarbe, Route grau gepunktet, oben im Blatt derselbe Grund. Keine Schlösser an jeder Stadt.
6. **Kontinent-Zahl in der Welt:** „x/y Länder“ zählt wie bisher; keine Schloss-Zahl.
7. **abgelegt** (gleicher Datenauftrag): Stadt-Kästchen mit kleinem goldenem ★ statt ✓; Flug mit allen Städten abgelegt = golden wie jetzt.
8. **Test:** Kl.-5-Lage (Afrika ohne Plan) → 0 Schlösser; Europa mit Platz 3 gesperrt → genau ein 🔒 an Platz 3, Nummer grau, Antippen zeigt „Erst … schaffen“ und der Knopf springt zum Land.

## 4) Frage 8 noch einmal – weiß ein Kind nach drei Sekunden, wo es ist und was als Nächstes kommt?

**Was als Nächstes kommt: ja, auf allen Größen.** Unten (Handy/Tablet) bzw. rechts (Rechner) steht `Bologna in Italien · 3/6` mit dem gelben Knopf `Weiter in Bologna ›`; das ist eindeutig und deckt sich mit der Tafel. Die Verwirrung „4/13“ ist weg.

**Wo es ist: auf Rechner und Tablet ja, auf dem Handy mit Einschränkungen.**
- Gut: Italien-Pin mit ✈ und Puls, blau gefärbte Fläche, in der Land-Ebene „hier bist du“ groß bei Bologna, wieder offene Stadt sofort erkennbar (orange ↻).
- Bremst: Handy-Kopf (M1) – in der Land-Ebene fehlt der Name „Italien“ oben; dichte Schilder in Mitteleuropa (Abschnitt 2); 11/12/13 übereinander (S1).
- Sobald gesperrte Länder kommen: nur mit Variante B lesbar. Mit einem Schloss an jedem Pin (A) würde das Kind in Klasse 5 auf Afrika und Asien „alles zu“ lesen und die eingeplanten Wartenden nicht mehr von den unwichtigen unterscheiden.

## Nicht geprüft

Echter Server (RK-D ist nicht eingespielt), echte Ladezeit, echte Geräte und echter Finger. Die Sperr-Bilder zeigen die **Vorgabe als Überlagerung im Prüf-Browser**, nicht gebaute App.

FERTIG: Prüfung RK-App 2 (0.92.2) – 1 Muss (Handy-Kopf überdeckt sich, „Zu mir“ in der Land-Ebene nicht antippbar), 3 Soll, 4 Kann; live nach M1.
