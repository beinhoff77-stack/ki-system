# Reise-Aufbau – Vorschlag (Stand 22.11.2026, fortgeschrieben „Reise-Aufbau 4“)

**Nur Vorschlag.** Kein App-Code, nichts in der Datenbank geändert, die Datenbank nur gelesen. Grundlagen in `inhalte/AUFTRAEGE.md`:
- Festlegungen 1–14 („Vorarbeit ‚Reise-Aufbau‘“), Nachtrag „Vorschlag fortschreiben“ (15:25), „Entscheidung Teilung“ (16:20).
- „Entscheidungen Sebastian (17:05)“: Salomonen statt Neukaledonien; Marokko → Algerien → Mauretanien bleibt; 101 geteilt; drei neue Etappen aus LK-D 3.
- „Rückläufer ChatGPT 947–950 (19:30)“, Abschnitt „Reise-Aufbau 4“: drei fehlende Städte, Insel-Ausnahme, Reserve Ozeanien.
- Teilung aus `inhalte/pruefung/lehrplan/lk_teilung_2211.json` (Stand `lernen-app` 456c6ec2: 7 Themen, 15 Teile); Kartenbedarf aus `inhalte/pruefung/kind/karte/umsetzung.md`.

Dateien:
- `aufbau-vorschlag.json` – maschinenlesbar:
  - je Flug: `flug_id` (`"29"` oder `"29-2"`), `thema_id`, `teil`/`von`, Titel/Untertitel, Land, `iso`, `region`, `mitte` (Breite/Länge), `hauptstadt` (deutscher Name + Lage), bei Landesteilen `hauptort_landesteil`
  - je Etappe: `lernziel`, Stadt, Breite/Länge, `geonames_id`; Kennzeichen `neu_lkd`, `kuer`, `noch_nicht_in_db`, `kuer_in` (sobald LK-D 4 es liefert)
  - dazu `reserve`, `reserve_staedte_je_land`, `expeditionen` (mit Koordinaten) und `selbstpruefung`
- `aufbau_daten.py` – die Zuordnung selbst (eine Stelle zum Ändern), dazu Reserve, Landesteile, deutsche Hauptstädte, vorgemerkte Nachbarländer.
- `aufbau_pruefen.py` – baut die JSON und die Tabellen unten und prüft alles. Aufruf `python3 -I inhalte/reise/aufbau_pruefen.py`, braucht `pip install geonamescache`. Ein Fehler oder ein nicht gefundener Ort ergibt Exit 1.
- `laender_geo_bauen.py` → `laender_geo.json` – Mittelpunkte und deutsche Namen aus Natural Earth. Nur neu bauen, wenn Länder dazukommen; der Aufruf steht im Kopf des Skripts.
- `db_stand.json` – gelesener DB-Stand: Thema → Einheit, Anzahl Etappen, Lernziele je Etappe in DB-Reihenfolge.

## Was „Reise-Aufbau 4“ ändert (gegenüber Reise-Aufbau 3)

- **Drei neue Etappen aus LK-D 4 bekommen je eine Stadt:**
  - 20 `irrational_beweis` → **Wieliczka** (Polen, nach Zakopane)
  - 61 Teil 1 `darstellen` → Neuseeland – Nordinsel, Strecke jetzt Auckland → **Rotorua** → Wellington; Teil 1 ist damit kein Kurzflug mehr
  - 91 Teil 1 `raumwinkel` → Paraguay, Strecke jetzt Asunción → San Bernardino → **Encarnación** → Ciudad del Este
- **Ziel erreicht:** 95 Flüge, 618 Städte. Das Prüfskript kennt die neuen Schlüssel und lief neu gegen die aktuellen Themendateien und die aktuelle Teilungsliste. Die gespeicherte Selbstprüfung in der JSON ist damit erneuert.
- **Salomonen = Insel-Ausnahme, kein Nachbarland.** In der JSON steht dafür `insel_ausnahme: true` bei 61-2.
- **Reserve Ozeanien auf drei Gebiete und mehr aufgefüllt.** Mikronesien (6 Orte) und Palau (3 Orte) gehören geografisch zu Ozeanien und wechseln aus der Pazifik-Reserve. Neu ist **Guam** (8 Orte, US-Außengebiet wie Hawaii). Zusammen mit dem Australian Capital Territory (4 Orte) sind es 4 Gebiete.
- **Pazifik-Reserve** (Polynesien, wie Festlegung 5) neu: Amerikanisch-Samoa (6), **Wallis und Futuna** (7, französisches Gebiet, nicht strittig), **Tuvalu** (6, alle Orte auf dem Atoll Funafuti).
- **Reserve-Städte:** Encarnación und Rotorua sind jetzt belegt. Paraguay hat neu Pilar und Villarrica als Reserve.

## Was „Reise-Aufbau 3“ ändert (gegenüber Reise-Aufbau 2)

- **61 Teil 2 → Salomonen** (statt Neukaledonien; Entscheidung Sebastian 17:05). 4 Städte: Honiara → Tulagi → Auki → Kirakira. Die Salomonen sind kein Nachbarland, sondern eine Insel-Ausnahme (ca. 3 200 km über das Meer). Das ist bewusst so entschieden: Neuseelands Nachbarn sind sonst belegt.
- **101 geteilt:**
  - Teil 1 „gerade Prismen und Zylinder“ bleibt Brasilien – Südosten (7 Städte).
  - **Teil 2 „schiefe Körper und Cavalieri“ → Brasilien – Mittelwesten**, Kurzflug mit **Brasília** (Etappe `cavalieri`).
  - Die Großregionen grenzen aneinander (Minas Gerais ↔ Goiás/Distrito Federal).
- **Neue Etappen aus LK-D 3:**
  - 101 `cavalieri` → Brasília
  - 91 `koerper_symmetrie` → **Porto Alegre** (Brasilien – Süden, nach Florianópolis)
  - 29 `gleichungen_binomisch` → Turkmenistan; dafür wurde die Strecke neu geordnet: Daschoguz → Türkmenabat → Mary → **Aschgabat**. Turkmenbaschi entfällt.
- **Kür je Etappe** (Entscheidung 17:05, Punkt 1):
  - `gleichungen_binomisch` ist im Gymnasium Kür, in der Realschule 8 Pflicht.
  - Die Kür je Schulart liefert `lehrplan-lb` in LK-D 4 als `etappen[].kuer_in`. Das Prüfskript übernimmt das Feld dann automatisch in die Stadt. Für die Reise ändert es nichts: Auch eine Kür-Etappe hat ihre Stadt.
- **Reserve:**
  - Die Salomonen und Brasilien – Mittelwesten sind jetzt belegt.
  - Pirenópolis, Goiânia, Cuiabá, Campo Grande, Corumbá und Gizo, Noro, Buala bleiben ihren Ländern als Reserve-Städte.
  - **Ozeanien hat nur noch 1 Reserve-Gebiet** (Australian Capital Territory, 4 Orte), Südamerika noch 3.

## Teilungen gesamt (8 neue Flüge, 15 Teile; Stand Reise-Aufbau 4)

| Thema | Teil 1 (bisheriges Land) | neue Teile → Land | Nachbarschaft |
|---|---|---|---|
| 26 Proportionalität | Kuba (5) | Teil 2 → **Jamaika** (3) | über die Jamaikastraße, ca. 150 km Meer |
| 29 Terme umformen | Kasachstan (5) | Teil 2 → **Turkmenistan** (4) | Landgrenze |
| 44 Konstruktionen | Ruanda (5) | Teil 2 → **Burundi** (2, Kurzflug) | Landgrenze |
| 46 Kongruenzabbildungen | Marokko (6) | Teil 2 → **Algerien** (3), Teil 3 → **Mauretanien** (3) | Algerien: Landgrenze; Mauretanien: Landgrenze zu Algerien, zu Marokko nur über Westsahara (von Sebastian bestätigt) |
| 61 Zufall und Laplace | Neuseeland – Nordinsel (3) | Teil 2 → **Salomonen** (4) | **Insel-Ausnahme**, kein Nachbarland (Entscheidung Sebastian) |
| 91 Schrägbilder | Paraguay (4) | Teil 2 → **Brasilien – Süden** (4) | Landgrenze (Ciudad del Este ↔ Foz do Iguaçu) |
| 101 Prismen und Zylinder | Brasilien – Südosten (7) | Teil 2 → **Brasilien – Mittelwesten** (1, Kurzflug) | gemeinsame Grenze der Großregionen |

**Erweiterbar:** Das Prüfskript liest die Teilung aus `lk_teilung_2211.json`. Ist dort ein Thema geteilt, das hier noch ein Flug ist (oder umgekehrt), meldet es einen Fehler und nennt das vorgemerkte Nachbarland:
- 2 Kirgisistan → **Tadschikistan** (Reserve Asien, Landgrenze). Asien hätte dann nur noch 2 Reserve-Länder.
- 57 South Australia → **kein freier Nachbar** (WA, NT, QLD, NSW, VIC sind belegt). Optionen: Australian Capital Territory (Reserve, kein Nachbar, 4 Orte) oder Kangaroo Island als eigener Landesteil. Adelaide (begonnen) bleibt in Teil 1. **Entscheidung nötig, falls 57 geteilt wird.**

## Abgleich

**Gesichert:**
- **Datenbank** (erneut gelesen 22.11., nach 19:30): 87 freigegebene Einheiten, 606 Etappen. Prüfsumme über Thema, Einheit und Lernziele identisch mit `db_stand.json`, also keine Änderung. Das LK-D-Einspiel ist noch nicht in der DB.
- **Noch nicht in der DB:** 12 neue Etappen (6 aus LK-D, 3 aus LK-D 3, 3 aus LK-D 4) und die Teilung (TL-S); in der JSON mit `noch_nicht_in_db` gekennzeichnet.
- **`lk_teilung_2211.json`:** Stand `lernen-app` 456c6ec2, 7 Themen, 15 Teile. Alle Teile sind im Vorschlag, die Etappen je Thema sind disjunkt und zusammen gleich den Etappen der Themendatei.
- **Kür je Schulart:** `kuer_in` steht jetzt je Etappe in der Teilungsliste (LK-D 4) und wird in die Stadt übernommen. Ungeteilte Themen haben das Feld dort nicht; 20 `irrational_beweis` ist in der JSON nur als neue Etappe gekennzeichnet.
- **Lernstand** (nur gezählt): 29 – ein Kind, alle 8 bisherigen Etappen gelandet; 99 – ein Kind, alle 7 gelandet. In 26, 44, 46, 47, 61, 91 und 101 gibt es keinen Lernstand.

**Änderungen seit dem Vorschlag vom Morgen:**
- **Umfang:** 87 → 95 Flüge, 606 → 618 Städte.
- **Länder neu:** Jamaika, Turkmenistan, Burundi, Algerien, Mauretanien, Salomonen, Brasilien – Süden, Brasilien – Mittelwesten.
- **Länder mit anderen Städten:** Brasilien → Brasilien – Südosten. Kuba, Kasachstan, Marokko, Ruanda, Paraguay und Neuseeland – Nordinsel geben Städte an die Reserve ab.
- **Neue Städte in bestehenden Flügen:** Marokko mit Oujda, Kenia + Nyeri, Ecuador + Portoviejo, Polen + Wieliczka.

## Ergebnis der Selbstprüfung (Skript)

| Prüfung | Ergebnis |
|---|---|
| Flüge | 95 = 87 Einheiten + 8 neue Teile ✔ (Soll aus `lk_teilung_2211.json` berechnet) |
| Teile | je geteiltes Thema alle Teile da, Etappen disjunkt und zusammen = Themendatei ✔ |
| Jedes Land/Landesteil einmal | 95 verschiedene ✔ (auch ISO + Landesteil eindeutig) |
| Jede Stadt einmal | 618 verschiedene Namen und GeoNames-Orte ✔ |
| Städte = Etappen je Flug | bei allen 95 ✔ (Summe 618) |
| Stadt liegt im Land / Landesteil | 618/618 in GeoNames gefunden ✔, dazu alle Reserve-Städte und Hauptorte |
| Koordinaten | 618/618 Städte, 95 Mittelpunkte, alle Hauptstädte, 21/21 Stationen (gegen die COMNAP-Liste abgeglichen) ✔ |
| Begonnene Orte bleiben | 9/9 ✔ |
| Reserve nicht belegt | ✔ |

**Hinweise des Skripts:**
- Kurzflüge 44-2 Burundi (2 Städte) und 101-2 Brasilien – Mittelwesten (1); beide erlaubt.
- Reserve: Australian Capital Territory hat 4 Orte, Palau 3 (Ziel 6–8); dafür hat Ozeanien 4 Gebiete.
- 10 Teilstrecken über 700 km Luftlinie (große Länder).

**Grenzen der Prüfung:** GeoNames prüft „Ort dieses Namens im Land/Landesteil“, nicht „der gemeinte Ort“.

## Karte: Daten und Quellen

| Feld | Quelle | Lizenz |
|---|---|---|
| Stadt: Breite/Länge, `geonames_id` | GeoNames über `geonamescache` (Orte ab 500 Einwohnern; größter Ort gleichen Namens im Land/Landesteil) | CC BY 4.0 – Quellenangabe |
| Land: `mitte` | Natural Earth 1:50 m, Beschriftungspunkt (`LABEL_Y/X`). Landesteile: admin_1-Punkt bzw. Mittel der Bundesstaaten; Neuseeland-Inseln: Mittel der Städte (kein Natural-Earth-Punkt) | gemeinfrei |
| Land: `iso` | ISO 3166-1 alpha-2 (Landesteile: ISO des Staats + `region`) | – |
| Hauptstadt: deutscher Name | von Hand, gegen die GeoNames-Namen der Hauptstadt abgeglichen; Lage aus GeoNames | CC BY 4.0 |
| Station: Breite/Länge | COMNAP Antarctic Facilities (2024) | „frei für Bildung und nicht kommerziell“, Quelle „COMNAP 2024“ – **Lizenz vor dem Bau klären** |

**Hauptstadt-Abgleich:**
- Zwei Namen stimmen, stehen aber nicht in GeoNames: „Washington, D.C.“ (GeoNames: Washington) und „Neu-Delhi“. Bei Neu-Delhi ordnet geonamescache „New Delhi“ dem Ort Delhi zu; die Lage liegt ca. 6 km neben dem Regierungsviertel.
- Sonderfälle mit Hinweis in der JSON: Bern (Bundesstadt), Amsterdam/Den Haag, Sucre/La Paz, Pretoria, Colombo/Kotte, Astana (geonamescache führt noch „Nur-Sultan“), Ngerulmud (Palau), Überseegebiete (Papeete, Pago Pago).
- Landesteile haben zusätzlich `hauptort_landesteil` für die Spitze des Flaggen-Pins: die Bundesstaats-Hauptstadt; bei Neuseeland-Süd und den brasilianischen Großregionen die größte Stadt (Mittelwesten: Brasília), jeweils gekennzeichnet.

## Offene Punkte

- **Reserve Ozeanien:** jetzt 4 Gebiete (Mikronesien, Guam, Palau, Australian Capital Territory). Weitere Möglichkeit, nicht eingetragen: „Papua-Neuguinea – Inselregion“ ohne Bougainville (Kokopo, Rabaul, Kimbe, Kavieng, Namatanai, Lorengau). Dann hieße Flug 80 „Papua-Neuguinea – Festland“.
- **57 South Australia:** falls geteilt, gibt es keinen freien Nachbarn (siehe oben).
- **Reserve Pazifik:** 3 Gebiete (Amerikanisch-Samoa, Wallis und Futuna, Tuvalu). Die Orte sind kleine Dörfer, meist unter 1 500 Einwohnern.
- **Lizenz COMNAP** (Stationen): an den Haupt-Chat (Lizenzklärung RK).

## Begonnene Orte – was bleibt (Festlegung 6)

Gezählt aus `route` (fertig), `flug_erstabschluss`, `karte_stand`, `testsitzung`; keine Kinderdaten übernommen.

| heutiger Ort | Flug, der das Land behält | Land | Grund |
|---|---|---|---|
| Rom | Natürliche Zahlen | Italien | zuerst abgeschlossen |
| Samarkand | Potenzgesetze | Usbekistan | zuerst abgeschlossen |
| Paris | Potenzen und negative Exponenten | Frankreich | **Annahme:** kein Erstabschluss gespeichert, nur dieses Thema hat Übungsstand |
| Mumbai | Bruchterme | Indien | **Annahme:** kein Erstabschluss; Bruchterme und Bruchgleichungen haben Übungsstand, Bruchterme kommt im Lehrplan zuerst |
| Quito | Flächen von Parallelogramm, Dreieck, Trapez | Ecuador | **Annahme:** kein Erstabschluss; beide Themen mit Übungsstand, dieses kommt zuerst |
| New York, Mexiko-Stadt, Alexandria, Adelaide | jeweils einziger Flug | USA, Mexiko, Ägypten, South Australia | – |

Nachbarländer für die übrigen Flüge begonnener Orte: Rom → Österreich, Schweiz, Slowenien; Samarkand → Kasachstan, Kirgisistan; Mumbai → Nepal, Sri Lanka, Bhutan; Paris → Spanien; Quito → Kolumbien.

## Sonderfälle – je zwei Lösungen

**1. Funktionen (heute Antarktis, keine Länder)**
- **A (gewählt, Festlegung 2):** Funktionen zieht in den neuen Reise-Kontinent **Orient** (Naher Osten und Kaukasus), 10 Länder. Antarktis wird Heimat der Expeditionen (21 Forschungsstationen). In der Antarktis hat noch kein Kind gelernt – nichts geht verloren.
- B: Funktionen bleibt in der Antarktis, Flüge = Forschungsstationen, Etappen = Regionen/Stützpunkte. Nachteil: Station ist kein Land, 5–11 „Städte“ je Station gibt es nicht; widerspricht dem neuen Prinzip.

**2. Daten und Zufall (12 Flüge) und Entdecker-Inseln (4 Flüge) überschneiden sich im Pazifik**
- **A (gewählt, Festlegungen 4/5):** Daten und Zufall = Australien nach Bundesstaaten + Neuseeland (Nord/Süd) + Melanesien; Entdecker-Inseln = Polynesien (Hawaii, Französisch-Polynesien, Samoa, Tonga). Keine Überschneidung.
- B: Daten und Zufall nur Australien + Neuseeland (9 Gebiete) und drei Flüge nach Südostasien; Nachteil: Asien ist durch Algebra belegt.

**3. Befund zu Festlegung 4: Die Zählung „zusammen 12“ stimmt nicht.** 7 Bundesstaaten/Territorien + 2 Inseln Neuseelands + Papua-Neuguinea + Fidschi = **11**. Für den 12. Flug:
- **A (gewählt):** **Vanuatu** (Melanesien, Nachbar von Fidschi; 5 Etappen: Port Vila, Luganville, Norsup, Lakatoro, Isangel – kleine Orte, Inselhüpfen per Fähre/Flug).
- B: Salomonen (Honiara u. a.) – noch weniger bekannte Orte; seit Reise-Aufbau 3 Land von 61 Teil 2. (Neukaledonien gemieden: französisches Gebiet mit umstrittener Unabhängigkeitsfrage.)

**4. Hawaii ist kein eigenes Land, sondern US-Bundesstaat; die USA sind schon Land eines Flugs (Zinsen).** Vorschlag: Hawaii wie die australischen Bundesstaaten als Gebiet zählen (Festlegung 5 nennt es so). Alternative: statt Hawaii die Cookinseln oder Tuvalu – kaum Orte.

**5. Flüge mit mehr als 12 Etappen** (Auftrag sagt 3–12): Natürliche Zahlen (13), Grundrechenarten (14), Brüche (14). Gelöst mit großen Ländern: Italien, Schweiz, Deutschland. Alternative: diese Flüge in der App teilen (Inhaltsänderung – nicht Teil dieses Vorschlags).

## Weitere Annahmen und Unsicherheiten

- **Nordamerika** schließt Mittelamerika und Karibik ein (Kuba, Guatemala, Costa Rica), weil 6 Länder gebraucht werden und nur USA/Kanada/Mexiko groß sind. Geografisch üblich, aber Kinder denken bei „Nordamerika“ oft nur an USA/Kanada.
- **Singapur** entfällt (Stadtstaat, keine 6 Städte); der Flug „Gleichungssysteme mit 3 Unbekannten“ geht nach Malaysia.
- **Vereinigtes Königreich** als ein Land (heute steht „Schottland“ bei Edinburgh). Edinburgh und Glasgow bleiben als Städte erhalten.
- **Kindgerecht, aber wenig bekannt:** Kasachstan, Kirgisistan, Mongolei, Bhutan, Bangladesch, Laos, Aserbaidschan, Papua-Neuguinea, Vanuatu, Samoa, Tonga, Französisch-Polynesien. In Polynesien sind die „Städte“ kleine Hauptorte (500–30 000 Einwohner).
- **Irak, Iran, Saudi-Arabien** gehören laut Festlegung 2 dazu. Inhaltlich gibt es dort gute Highlights (Babylon, Persepolis/Isfahan, AlUla), real gelten aber Reisewarnungen. Mekka ist bewusst nicht dabei (für Nicht-Muslime gesperrt).
- **Strittige Gebiete gemieden:** kein Kaschmir, Tibet, Xinjiang, Taiwan, Krim, Westsahara, Abchasien/Südossetien, Bergkarabach, Kirkuk; kein Sabah (Anspruch der Philippinen), Mindanao, Belize, Bougainville. Neukaledonien bleibt gemieden (Entscheidung Sebastian 22.11., 17:05). Mauretanien grenzt an Marokko nur über Westsahara – Route Marokko → Algerien → Mauretanien von Sebastian bestätigt. Bewusst nicht gewählt wegen Krieg/Krise: Ukraine, Russland, Israel/Palästina, Syrien, Jemen, Libyen, Sudan, Mali (heute Timbuktu), Myanmar, Venezuela, Afghanistan.
- **Fahrbar** heißt Straße oder Fähre (z. B. Sansibar, Kangaroo Island, Bali, Philippinen, Fidschi/Samoa/Tonga). Hawaii, Französisch-Polynesien, Vanuatu, Papua-Neuguinea (Port Moresby hat keine Straße nach Lae) brauchen Inselflüge – **Annahme:** für Inselgebiete zulässig.
- **Reihenfolge innerhalb eines Landes** ist eine Strecke, nicht immer ein geschlossener Ring.
- Städtenamen auf Deutsch, wo gebräuchlich (Mailand, Breslau, Täbris); sonst Landesschreibweise.
- Die heutigen Orte, an denen niemand gelernt hat (z. B. Bagdad, Teheran, Timbuktu, Singapur, Göttingen, Brügge), sind frei verwendet; Bagdad, Brügge, Pisa, Florenz u. a. tauchen als Städte wieder auf.


## Zuordnung im Einzelnen

Vom Prüfskript erzeugt – nicht von Hand ändern. ↪ = weiterer Teil eines geteilten Themas (Nachbarland), ★Kür = neue Vertiefungs-Etappe, (neu) = neue LK-D-Etappe in einem Teil.

<!-- AUTO:START (aufbau_pruefen.py) -->

### Zahlen → Europa  (13 Flüge, 116 Etappen)

| # | Flug | Kl. | heute | Land (ISO) · Hauptstadt | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Natürliche Zahlen | Gym 5 · RS 5 | Rom | **Italien** (IT) · Rom | 13: Rom → Neapel → Pompei → Bari → Bologna → Venedig → Verona → Mailand → Turin → Genua → Pisa → Florenz → Siena |
| 2 | Ganze Zahlen | Gym 5 · RS 5 | Rom | **Österreich** (AT) · Wien | 11: Wien → St. Pölten → Linz → Salzburg → Kitzbühel → Innsbruck → Bregenz → Villach → Klagenfurt → Graz → Eisenstadt |
| 3 | Grundrechenarten und Rechengesetze | Gym 5 · RS 5 | Rom | **Schweiz** (CH) · Bern | 14: Basel → Zürich → Winterthur → St. Gallen → Chur → Lugano → Locarno → Sion → Montreux → Lausanne → Genf → Freiburg im Üechtland → Bern → Luzern |
| 4 | Potenzen als Schreibweise | Gym 5 · RS 5 | Rom | **Slowenien** (SI) · Ljubljana | 7: Ljubljana → Kranj → Bled → Postojna → Koper → Piran → Maribor |
| 5 | Teilbarkeit | Gym 5 · RS 5 | Athen | **Griechenland** (GR) · Athen | 7: Athen → Korinth → Nafplio → Olympia → Patras → Delphi → Thessaloniki |
| 6 | Brüche und Anteile | Gym 6 · RS 6 | Pisa | **Deutschland** (DE) · Berlin | 14: München → Augsburg → Stuttgart → Heidelberg → Frankfurt am Main → Köln → Münster → Bremen → Hamburg → Lübeck → Berlin → Dresden → Leipzig → Nürnberg |
| 7 | Dezimalzahlen | Gym 6 · RS 6 | Brügge | **Belgien** (BE) · Brüssel | 8: Brüssel → Antwerpen → Gent → Brügge → Ostende → Namur → Lüttich → Löwen |
| 8 | Rechnen mit rationalen Zahlen | Gym 6 · RS 6 | Florenz | **Vereinigtes Königreich** (GB) · London | 12: London → Oxford → Bath → Bristol → Cardiff → Liverpool → Manchester → York → Newcastle upon Tyne → Edinburgh → Glasgow → Belfast |
| 9 | Zehnerpotenzen und wissenschaftliche Schreibweise | Gym 6 · RS 7 | Paris | **Spanien** (ES) · Madrid | 7: Barcelona → Valencia → Granada → Sevilla → Córdoba → Toledo → Madrid |
| 10 | Potenzen und negative Exponenten | Gym 6 · RS 7 | Paris | **Frankreich** (FR) · Paris | 3: Paris → Lyon → Marseille |
| 11 | Elementare Wurzeln | Gym 9 · RS 9 | Göttingen | **Niederlande** (NL) · Amsterdam | 6: Amsterdam → Haarlem → Leiden → Den Haag → Rotterdam → Utrecht |
| 12 | Wurzeln und reelle Zahlen | Gym 9 · RS 9 | Göttingen | **Polen** (PL) · Warschau | 8: Warschau → Danzig → Thorn → Posen → Breslau → Krakau → Zakopane → Wieliczka ★Kür |
| 13 | Rationale Exponenten und n-te Wurzel | Gym 9 · RS 10 | Edinburgh | **Norwegen** (NO) · Oslo | 6: Oslo → Lillehammer → Trondheim → Ålesund → Bergen → Stavanger |

### Geld und Verhältnisse → Nordamerika (mit Mittelamerika und Karibik)  (7 Flüge, 45 Etappen)

| # | Flug | Kl. | heute | Land (ISO) · Hauptstadt | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Größen und Einheiten | Gym 5 · RS 5 | Toronto | **Kanada** (CA) · Ottawa | 8: Victoria → Vancouver → Banff → Calgary → Winnipeg → Toronto → Ottawa → Montreal |
| 2 | Direkte Proportionalität und Dreisatz – Teil 1 von 2 · Dreisatz | Gym 5 · RS 5 | Chicago | **Kuba** (CU) · Havanna | 5: Viñales → Havanna → Varadero → Santa Clara → Cienfuegos |
| 3 | ↪ Direkte Proportionalität und Dreisatz – Teil 2 von 2 · proportionale Zuordnungen erkennen | Gym 5 · RS 6 | Chicago | **Jamaika** (JM) · Kingston | 3: Montego Bay → Ocho Rios → Kingston |
| 4 | Prozent- und Zinsrechnung | Gym 6 · RS 6 | Mexiko-Stadt | **Mexiko** (MX) · Mexiko-Stadt | 6: Guadalajara → Guanajuato → Mexiko-Stadt → Puebla → Oaxaca → Veracruz |
| 5 | Zinsen | Gym 6 · RS 7 | New York | **USA** (US) · Washington, D.C. | 8: Boston → New York → Washington, D.C. → Chicago → Denver → Phoenix → Los Angeles → San Francisco |
| 6 | Vermehrter und verminderter Grundwert | Gym 7 · RS 7 | Los Angeles | **Guatemala** (GT) · Guatemala-Stadt | 8: Guatemala-Stadt → Antigua Guatemala → Panajachel → Chichicastenango → Quetzaltenango → Cobán → Flores → Puerto Barrios |
| 7 | Indirekte Proportionalität | Gym 8 · RS 7 | Vancouver | **Costa Rica** (CR) · San José | 7: San José → Alajuela → La Fortuna → Liberia → Puntarenas → Quepos → Cartago |

### Algebra → Asien (ohne Orient)  (20 Flüge, 117 Etappen)

| # | Flug | Kl. | heute | Land (ISO) · Hauptstadt | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Einfache Gleichungen | Gym 5 · RS 6 | Bagdad | **Kambodscha** (KH) · Phnom Penh | 5: Siem Reap → Battambang → Phnom Penh → Kampot → Sihanoukville |
| 2 | Terme aufstellen und deuten | Gym 7 · RS 6 | Teheran | **Vietnam** (VN) · Hanoi | 6: Hanoi → Ha Long → Hue → Da Nang → Hoi An → Ho-Chi-Minh-Stadt |
| 3 | Potenzgesetze | Gym 7 · RS 7 | Samarkand | **Usbekistan** (UZ) · Taschkent | 5: Fergana → Taschkent → Samarkand → Buchara → Chiwa |
| 4 | Terme umformen – Teil 1 von 2 · zusammenfassen und ausmultiplizieren | Gym 7 · RS 7 | Samarkand | **Kasachstan** (KZ) · Astana | 5: Almaty → Taras → Schymkent → Türkistan → Kysylorda |
| 5 | ↪ Terme umformen – Teil 2 von 2 · Summe mal Summe, binomische Formeln, Gleichungen mit Klammern | Gym 7 · RS 8 | Samarkand | **Turkmenistan** (TM) · Aschgabat | 4: Daschoguz → Türkmenabat → Mary → Aschgabat (neu) |
| 6 | Lineare Gleichungen | Gym 7 · RS 7 | Samarkand | **Kirgisistan** (KG) · Bischkek | 6: Bischkek → Tscholpon-Ata → Karakol → Naryn → Dschalal-Abad → Osch |
| 7 | Intervalle | Gym 8 · RS 7 | Delhi | **Mongolei** (MN) · Ulaanbaatar | 4: Ulaanbaatar → Darchan → Erdenet → Charchorin (Karakorum) |
| 8 | Lineare Ungleichungen | Gym 8 · RS 7 | Delhi | **Indonesien** (ID) · Jakarta | 7: Jakarta → Bandung → Yogyakarta → Solo → Surabaya → Malang → Denpasar |
| 9 | Bruchterme | Gym 8 · RS 8 | Mumbai | **Indien** (IN) · Neu-Delhi | 7: Delhi → Agra → Jaipur → Udaipur → Ahmedabad → Mumbai → Panaji (Goa) |
| 10 | Potenzgesetze mit ganzzahligen Exponenten | Gym 8 · RS 7 | Mumbai | **Nepal** (NP) · Kathmandu | 5: Bhaktapur → Lalitpur (Patan) → Kathmandu → Pokhara → Bharatpur |
| 11 | Bruch- und Verhältnisgleichungen | Gym 8 · RS 8 | Mumbai | **Sri Lanka** (LK) · Colombo | 7: Colombo → Galle → Nuwara Eliya → Kandy → Dambulla → Anuradhapura → Trincomalee |
| 12 | Formeln umstellen | Gym 8 | Mumbai | **Bhutan** (BT) · Thimphu | 5: Paro → Thimphu → Punakha → Wangdue Phodrang → Jakar |
| 13 | Gleichungssysteme mit 2 Unbekannten | Gym 8 · RS 9 | Peking | **China** (CN) · Peking | 9: Peking → Xi'an → Chengdu → Chongqing → Guilin → Guangzhou → Hangzhou → Shanghai → Nanjing |
| 14 | Quadratische Gleichungen (allgemein) | Gym 9 · RS 9 | Seoul | **Südkorea** (KR) · Seoul | 8: Incheon → Seoul → Suwon → Daejeon → Jeonju → Gwangju → Busan → Gyeongju |
| 15 | Gleichungssysteme mit 3 Unbekannten | Gym 9 | Singapur | **Malaysia** (MY) · Kuala Lumpur | 6: Johor Bahru → Malakka → Kuala Lumpur → Ipoh → George Town → Alor Setar |
| 16 | Potenzgleichungen | Gym 9 · RS 10 | Tokio | **Japan** (JP) · Tokio | 6: Tokio → Kamakura → Kyoto → Nara → Osaka → Hiroshima |
| 17 | Exponentialgleichungen | Gym 10 · RS 10 | Bangkok | **Thailand** (TH) · Bangkok | 6: Phuket → Hua Hin → Bangkok → Ayutthaya → Sukhothai → Chiang Mai |
| 18 | Polynomgleichungen | Gym 10 | Bangkok | **Laos** (LA) · Vientiane | 5: Luang Prabang → Vang Vieng → Vientiane → Thakhek → Pakse |
| 19 | Quadratische Terme und Extremwerte | RS 8 | Shanghai | **Philippinen** (PH) · Manila | 5: Baguio → Manila → Legazpi → Cebu → Tagbilaran |
| 20 | Wurzelgleichungen | RS 9 | Tokio | **Bangladesch** (BD) · Dhaka | 6: Rajshahi → Khulna → Dhaka → Sylhet → Chittagong → Cox's Bazar |

### Funktionen → Orient (Naher Osten und Kaukasus) – neu, ersetzt Antarktis  (10 Flüge, 79 Etappen)

| # | Flug | Kl. | heute | Land (ISO) · Hauptstadt | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Zuordnung und Funktion | Gym 8 · RS 8 | McMurdo-Station | **Georgien** (GE) · Tiflis | 9: Tiflis → Stepanzminda → Mzcheta → Gori → Borjomi → Batumi → Kutaissi → Telawi → Sighnaghi |
| 2 | Lineare Funktionen | Gym 8 · RS 8 | Neumayer-Station III | **Türkei** (TR) · Ankara | 11: Istanbul → Bursa → Çanakkale → Izmir → Selçuk → Bodrum → Antalya → Konya → Göreme → Ankara → Safranbolu |
| 3 | Gebrochen-rationale Funktionen | Gym 8 | Amundsen-Scott-Südpolstation | **Armenien** (AM) · Jerewan | 5: Jerewan → Etschmiadsin → Gjumri → Dilidschan → Sewan |
| 4 | Quadratische Funktionen | Gym 9 · RS 9 | Wostok-Station | **Irak** (IQ) · Bagdad | 9: Bagdad → Samarra → Mossul → Erbil → Sulaimaniyya → Basra → Nadschaf → Kerbela → Hilla (Babylon) |
| 5 | Potenzfunktionen | Gym 9 · RS 10 | Rothera-Station | **Iran** (IR) · Teheran | 10: Teheran → Rascht → Täbris → Hamadan → Isfahan → Schiras → Bandar Abbas → Kerman → Yazd → Kaschan |
| 6 | Exponential- und Logarithmusfunktionen | Gym 10 · RS 10 | Halley-Station | **Vereinigte Arabische Emirate** (AE) · Abu Dhabi | 7: Abu Dhabi → Dubai → Schardscha → Adschman → Umm al-Qaiwain → Ras al-Chaima → Fudschaira |
| 7 | Sinus- und Kosinusfunktion | Gym 10 · RS 10 | Concordia-Station | **Saudi-Arabien** (SA) · Riad | 8: Riad → Hail → AlUla → Tabuk → Medina → Dschidda → Taif → Abha |
| 8 | Ganzrationale Funktionen | Gym 10 | Casey-Station | **Oman** (OM) · Maskat | 7: Maskat → Barka → Sohar → Ibri → Bahla → Nizwa → Sur |
| 9 | Reihen | IB 5 | Palmer-Station | **Aserbaidschan** (AZ) · Baku | 8: Baku → Quba → Schamachy → Gabala → Scheki → Gandscha → Mingətschevir → Lənkəran |
| 10 | Betragsfunktion | IB 5 | Palmer-Station | **Jordanien** (JO) · Amman | 5: Amman → Dscherasch → Madaba → Wadi Musa (Petra) → Aqaba |

### Geometrie → Afrika  (17 Flüge, 104 Etappen)

| # | Flug | Kl. | heute | Land (ISO) · Hauptstadt | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Grundbegriffe und Figuren | Gym 5 · RS 5 | Kairo | **Tunesien** (TN) · Tunis | 7: Sidi Bou Saïd → Tunis → Sousse → Monastir → El Djem → Tozeur → Kairouan |
| 2 | Ortslinien und Ortsbereiche | Gym 5 · RS 7 | Kairo | **Senegal** (SN) · Dakar | 6: Saint-Louis → Thiès → Dakar → Mbour → Joal-Fadiouth → Kaolack |
| 3 | Mit Winkeln rechnen | Gym 5 · RS 5 | Timbuktu | **Ghana** (GH) · Accra | 7: Accra → Ho → Tamale → Kumasi → Takoradi → Elmina → Cape Coast |
| 4 | Kongruenzabbildungen – Teil 1 von 3 · Spiegeln und Symmetrie | Gym 7 · RS 6 | Marrakesch | **Marokko** (MA) · Rabat | 6: Casablanca → Rabat → Tanger → Chefchaouen → Fès → Oujda |
| 5 | ↪ Kongruenzabbildungen – Teil 2 von 3 · Verschieben und Vektoren | Gym 7 · RS 7 | Marrakesch | **Algerien** (DZ) · Algier | 3: Tlemcen → Oran → Algier (neu) |
| 6 | ↪ Kongruenzabbildungen – Teil 3 von 3 · Drehen und Punktspiegelung | Gym 7 · RS 8 | Marrakesch | **Mauretanien** (MR) · Nouakchott | 3: Nouadhibou → Nouakchott → Atar (neu) |
| 7 | Winkelsätze | Gym 7 · RS 7 | Addis Abeba | **Tansania** (TZ) · Dodoma | 9: Sansibar-Stadt → Daressalam → Bagamoyo → Tanga → Moshi → Arusha → Mwanza → Dodoma → Morogoro |
| 8 | Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 · Dreiecke konstruieren, Kongruenz | Gym 7 · RS 7 | Addis Abeba | **Ruanda** (RW) · Kigali | 5: Kigali → Musanze → Rubavu (Gisenyi) → Karongi (Kibuye) → Huye |
| 9 | ↪ Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 · Vierecke | Gym 7 · RS 8 | Addis Abeba | **Burundi** (BI) · Gitega | 2: Bujumbura → Gitega (neu) |
| 10 | Kreis und Tangenten | Gym 7 · RS 7 | Alexandria | **Ägypten** (EG) · Kairo | 6: Alexandria → Gizeh → Kairo → Hurghada → Luxor → Assuan |
| 11 | Ähnlichkeit und Strahlensätze | Gym 9 · RS 9 | Nairobi | **Kenia** (KE) · Nairobi | 9: Malindi → Mombasa → Nairobi → Naivasha → Nakuru → Kisumu → Eldoret → Nanyuki → Nyeri ★Kür |
| 12 | Satz des Pythagoras | Gym 9 · RS 9 | Kapstadt | **Simbabwe** (ZW) · Harare | 6: Harare → Mutare → Masvingo → Bulawayo → Hwange → Victoria Falls |
| 13 | Trigonometrie im rechtwinkligen Dreieck | Gym 9 · RS 9 | Sansibar | **Namibia** (NA) · Windhoek | 7: Windhoek → Otjiwarongo → Tsumeb → Swakopmund → Walvis Bay → Lüderitz → Keetmanshoop |
| 14 | Allgemeine Trigonometrie | Gym 9 · RS 10 | Sansibar | **Südafrika** (ZA) · Pretoria | 9: Kapstadt → Stellenbosch → Mossel Bay → Knysna → Gqeberha (Port Elizabeth) → Durban → Pretoria → Johannesburg → Bloemfontein |
| 15 | Trigonometrische Gleichungen | Gym 9 · RS 10 | Sansibar | **Mauritius** (MU) · Port Louis | 6: Port Louis → Grand Baie → Flic en Flac → Quatre Bornes → Curepipe → Mahébourg |
| 16 | Zweireihige Determinanten | RS 7 | Lagos | **Uganda** (UG) · Kampala | 6: Entebbe → Kampala → Jinja → Mbale → Fort Portal → Mbarara |
| 17 | Matrizen und Abbildungen mit Matrizen | RS 10 | Dakar | **Madagaskar** (MG) · Antananarivo | 7: Toamasina → Moramanga → Antananarivo → Antsirabe → Ambositra → Fianarantsoa → Toliara |

### Fläche und Raum → Südamerika  (11 Flüge, 62 Etappen)

| # | Flug | Kl. | heute | Land (ISO) · Hauptstadt | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Umfang und Flächeninhalt | Gym 5 · RS 5 | Lima | **Peru** (PE) · Lima | 7: Lima → Paracas → Nazca → Arequipa → Puno → Cusco → Aguas Calientes (Machupicchu) |
| 2 | Volumen und Oberfläche | Gym 5 · RS 6 | Rio de Janeiro | **Uruguay** (UY) · Montevideo | 5: Colonia del Sacramento → Montevideo → Punta del Este → Salto → Paysandú |
| 3 | Flächen von Parallelogramm, Dreieck und Trapez | Gym 6 · RS 6 | Quito | **Ecuador** (EC) · Quito | 8: Otavalo → Quito → Baños → Riobamba → Cuenca → Guayaquil → Manta → Portoviejo ★Kür |
| 4 | Volumen | Gym 6 · RS 6 | Quito | **Kolumbien** (CO) · Bogotá | 7: Cartagena → Barranquilla → Santa Marta → Medellín → Salento → Cali → Bogotá |
| 5 | Kreisberechnungen | Gym 8 · RS 9 | Buenos Aires | **Argentinien** (AR) · Buenos Aires | 6: Buenos Aires → Rosario → Mendoza → San Miguel de Tucumán → Salta → Puerto Iguazú |
| 6 | Körper darstellen | Gym 8 · RS 5 | Cusco | **Bolivien** (BO) · Sucre | 6: Copacabana → La Paz → Uyuni → Potosí → Sucre → Cochabamba |
| 7 | Prismen und Zylinder – Teil 1 von 2 · gerade Prismen und Zylinder | Gym 8 · RS 9 | Cusco | **Brasilien – Südosten** (BR) · São Paulo (Landesteil) | 7: Santos → São Paulo → Campinas → Belo Horizonte → Ouro Preto → Petrópolis → Rio de Janeiro |
| 8 | ↪ Prismen und Zylinder – Teil 2 von 2 · schiefe Körper und Cavalieri | Gym 10 · RS 9 | Cusco | **Brasilien – Mittelwesten** (BR) · Brasília (Landesteil) | 1: Brasília (neu) |
| 9 | Schrägbilder und Raumdarstellung – Teil 1 von 2 · Schrägbilder und Lage im Raum | Gym 10 · RS 7 | Brasília | **Paraguay** (PY) · Asunción | 4: Asunción → San Bernardino → Encarnación (neu) → Ciudad del Este (neu) |
| 10 | ↪ Schrägbilder und Raumdarstellung – Teil 2 von 2 · Raumkoordinaten, Körpersymmetrie, Rotationskörper | Gym 10 · RS 8 | Brasília | **Brasilien – Süden** (BR) · Curitiba (Landesteil) | 4: Foz do Iguaçu → Curitiba → Florianópolis → Porto Alegre (neu) |
| 11 | Pyramide, Kegel, Kugel | Gym 10 · RS 9 | Santiago de Chile | **Chile** (CL) · Santiago de Chile | 7: San Pedro de Atacama → Antofagasta → Copiapó → La Serena → Viña del Mar → Valparaíso → Santiago de Chile |

### Daten und Zufall → Australien (nach Bundesstaaten) und Ozeanien  (13 Flüge, 75 Etappen)

| # | Flug | Kl. | heute | Land (ISO) · Hauptstadt | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Zählen und Kombinatorik | Gym 5 · RS 5 | Melbourne | **Victoria** (AU) · Melbourne (Landesteil) | 7: Melbourne → Cowes (Phillip Island) → Geelong → Lorne → Warrnambool → Ballarat → Bendigo |
| 2 | Daten erfassen und darstellen | Gym 6 · RS 5 | Adelaide | **South Australia** (AU) · Adelaide (Landesteil) | 6: Adelaide → Hahndorf → Victor Harbor → Kingscote → Port Augusta → Coober Pedy |
| 3 | Mittelwert und Häufigkeiten | Gym 6 · RS 7 | Sydney | **Tasmanien** (AU) · Hobart (Landesteil) | 3: Hobart → Launceston → Devonport |
| 4 | Median, Quartile, Boxplot | Gym 7 · RS 7 | Brisbane | **Western Australia** (AU) · Perth (Landesteil) | 6: Perth → Fremantle → Margaret River → Albany → Esperance → Kalgoorlie |
| 5 | Zufall und Laplace – Teil 1 von 2 · Ergebnis, Ereignis, relative Häufigkeit | Gym 8 · RS 8 | Auckland | **Neuseeland – Nordinsel** (NZ) · Wellington (Landesteil) | 3: Auckland → Rotorua → Wellington (neu) |
| 6 | ↪ Zufall und Laplace – Teil 2 von 2 · Laplace-Wahrscheinlichkeit | Gym 8 · RS 9 | Auckland | **Salomonen** (SB) · Honiara | 4: Honiara → Tulagi → Auki → Kirakira |
| 7 | Verknüpfte Ereignisse | Gym 9 · RS 9 | Wellington | **Queensland** (AU) · Brisbane (Landesteil) | 11: Gold Coast → Brisbane → Noosa Heads → Hervey Bay → Bundaberg → Rockhampton → Mackay → Airlie Beach → Townsville → Cairns → Port Douglas |
| 8 | Mehrstufige Zufallsexperimente | Gym 10 · RS 10 | Darwin | **New South Wales** (AU) · Sydney (Landesteil) | 9: Sydney → Wollongong → Katoomba → Bathurst → Dubbo → Tamworth → Coffs Harbour → Port Macquarie → Newcastle |
| 9 | Simulation | Gym 10 · RS 9 | Darwin | **Northern Territory** (AU) · Darwin (Landesteil) | 6: Darwin → Jabiru → Katherine → Tennant Creek → Alice Springs → Yulara |
| 10 | Stichproben und Aussagekraft | RS 7 | Perth | **Neuseeland – Südinsel** (NZ) · Christchurch (Landesteil) | 5: Picton → Kaikōura → Christchurch → Dunedin → Queenstown |
| 11 | Standardabweichung | IB 5 | Suva | **Vanuatu** (VU) · Port Vila | 5: Port Vila → Luganville → Norsup → Lakatoro → Isangel |
| 12 | Zweidimensionale Daten | IB 5 | Hobart | **Fidschi** (FJ) · Suva | 5: Nadi → Lautoka → Sigatoka → Navua (Pacific Harbour) → Suva |
| 13 | Normalverteilung | IB 5 | Suva | **Papua-Neuguinea** (PG) · Port Moresby | 5: Port Moresby → Lae → Madang → Goroka → Mount Hagen |

### Entdecker-Inseln → Pazifik  (4 Flüge, 20 Etappen)

| # | Flug | Kl. | heute | Land (ISO) · Hauptstadt | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Aussagenlogik | IB 4 | Honolulu | **Hawaii** (US) · Honolulu (Landesteil) | 5: Honolulu → Kailua → Kahului → Hilo → Līhuʻe |
| 2 | Graphentheorie | IB 4 | Tahiti | **Französisch-Polynesien** (PF) · Papeete | 5: Papeete → Afareaitu → Fare → Uturoa → Vaitape |
| 3 | Schranken und Genauigkeit | IB 5 | Honolulu | **Tonga** (TO) · Nukuʻalofa | 5: Nukuʻalofa → Kolonga → Pangai → Neiafu → ʻOhonua |
| 4 | Lineare Optimierung | IB 5 | Tahiti | **Samoa** (WS) · Apia | 5: Apia → Leulumoega → Mulifanua → Palauli → Asau |

### Reserve-Länder je Kontinent (frei für neue Themen und weitere Teilungen)

| Kontinent | Land (ISO) · Hauptstadt | Städte |
|---|---|---|
| Europa | Portugal (PT) · Lissabon | 8: Porto → Braga → Coimbra → Lissabon → Sintra → Évora → Lagos → Faro |
| Europa | Schweden (SE) · Stockholm | 8: Kiruna → Uppsala → Stockholm → Visby → Kalmar → Lund → Malmö → Göteborg |
| Europa | Tschechien (CZ) · Prag | 7: Prag → Kuttenberg → Krumau → Pilsen → Karlsbad → Brünn → Olmütz |
| Europa | Kroatien (HR) · Zagreb | 6: Zagreb → Rijeka → Pula → Zadar → Split → Dubrovnik |
| Europa | Irland (IE) · Dublin | 7: Dublin → Kilkenny → Cork → Killarney → Limerick → Galway → Sligo |
| Nordamerika | Panama (PA) · Panama-Stadt | 6: Panama-Stadt → Colón → Penonomé → Santiago de Veraguas → David → Boquete |
| Nordamerika | Dominikanische Republik (DO) · Santo Domingo | 7: Santo Domingo → San Pedro de Macorís → La Romana → Higüey → Punta Cana → Santiago de los Caballeros → Puerto Plata |
| Nordamerika | El Salvador (SV) · San Salvador | 7: San Salvador → Suchitoto → San Miguel → La Libertad → Sonsonate → Juayúa → Santa Ana |
| Asien | Tadschikistan (TJ) · Duschanbe | 7: Chudschand → Istarawschan → Pandschakent → Duschanbe → Bochtar → Kulob → Chorugh |
| Asien | Pakistan (PK) · Islamabad | 7: Gilgit → Peshawar → Islamabad → Lahore → Multan → Hyderabad → Karachi |
| Asien | Osttimor (TL) · Dili | 7: Dili → Baucau → Lospalos → Viqueque → Same → Suai → Maliana |
| Orient | Katar (QA) · Doha | 7: Doha → Ar-Rayyan → Dukhan → Umm Salal Muhammad → Al-Chaur → Al-Wakra → Mesaieed |
| Orient | Kuwait (KW) · Kuwait-Stadt | 6: Kuwait-Stadt → Hawalli → Al-Farwaniya → Al-Dschahra → Al-Ahmadi → Fahaheel |
| Orient | Bahrain (BH) · Manama | 6: Manama → Muharraq → Sitra → Isa Town → Riffa → Hamad Town |
| Orient | Zypern (CY) · Nikosia | 6: Nikosia → Larnaka → Ayia Napa → Paralimni → Limassol → Paphos |
| Afrika | Botswana (BW) · Gaborone | 7: Gaborone → Lobatse → Serowe → Palapye → Francistown → Maun → Kasane |
| Afrika | Sambia (ZM) · Lusaka | 7: Livingstone → Mongu → Lusaka → Kabwe → Ndola → Kitwe → Chipata |
| Afrika | Malawi (MW) · Lilongwe | 7: Blantyre → Zomba → Mangochi → Salima → Lilongwe → Nkhata Bay → Mzuzu |
| Südamerika | Brasilien – Nordosten (BR) · Salvador (Landesteil) | 8: Salvador → Aracaju → Maceió → Recife → Olinda → João Pessoa → Natal → Fortaleza |
| Südamerika | Brasilien – Norden (BR) · Manaus (Landesteil) | 6: Macapá → Belém → Santarém → Manaus → Boa Vista → Porto Velho |
| Südamerika | Suriname (SR) · Paramaribo | 6: Nieuw Nickerie → Paramaribo → Lelydorp → Brownsweg → Moengo → Albina |
| Australien | Australian Capital Territory (AU) · Canberra (Landesteil) | 4: Canberra → Gungahlin → Belconnen → Tuggeranong |
| Australien | Mikronesien (FM) · Palikir | 6: Colonia (Yap) → Weno → Kolonia → Palikir → Tofol → Lelu |
| Australien | Guam (GU) · Hagåtña | 8: Hagåtña → Tamuning → Dededo → Yigo → Mangilao → Inarajan → Umatac → Agat |
| Australien | Palau (PW) · Ngerulmud | 3: Koror → Kloulklubed → Ngerkeai |
| Pazifik | Amerikanisch-Samoa (AS) · Pago Pago | 6: Pago Pago → Aūa → Tāfuna → Faleniu → Vaitogi → Leone |
| Pazifik | Wallis und Futuna (WF) · Mata-Utu | 7: Mata-Utu → Liku → Alele → Halalo → Utufua → Leava (Futuna) → Alo (Futuna) |
| Pazifik | Tuvalu (TV) · Funafuti | 6: Funafuti → Vaiaku → Fakaifou → Alapi → Senala → Teone |

Reserve-Städte, die durch die Teilung frei wurden: Kuba: Trinidad, Camagüey, Santiago de Cuba; Kasachstan: Karaganda, Astana, Pawlodar; Marokko: Meknès, Essaouira, Agadir, Ouarzazate, Marrakesch; Ruanda: Nyanza; Paraguay: Concepción, Pilar, Villarrica; Neuseeland – Nordinsel: Hamilton, Taupō, Napier; Salomonen: Gizo, Noro, Buala; Brasilien – Mittelwesten: Pirenópolis, Goiânia, Cuiabá, Campo Grande, Corumbá.

### Antarktis → Expeditionen (je Expedition eine Forschungsstation, Koordinaten COMNAP 2024)

| Expedition | Station | Betreiber | Breite | Länge |
|---|---|---|---|---|
| 5-aquarium | Palmer-Station | USA | -64.7742 | -64.0531 |
| 5-flug_toronto | McMurdo-Station | USA | -77.8500 | 166.6667 |
| 5-kettennachricht | Amundsen-Scott-Südpolstation | USA | -89.9833 | 142.2667 |
| 5-oase | Maitri-Station (Schirmacher-Oase) | Indien | -70.7668 | 11.7308 |
| 5-pyramide | Princess-Elisabeth-Station | Belgien | -71.9499 | 23.3469 |
| 5-roemerstrasse | Mario-Zucchelli-Station | Italien | -74.6948 | 164.1133 |
| 5-schatzsuche | Esperanza-Station | Argentinien | -63.3970 | -56.9981 |
| 5-uhrturm | Halley-VI-Station | Vereinigtes Königreich | -75.5711 | -25.4739 |
| 5-wetterstation | Neumayer-Station III | Deutschland | -70.6605 | -8.2841 |
| 5-zeltplatz | Kohnen-Station | Deutschland | -75.0019 | 0.0663 |
| 8-garten | Troll-Station | Norwegen | -72.0119 | 2.5331 |
| 8-handytarif | Rothera-Station | Vereinigtes Königreich | -67.5695 | -68.1249 |
| 8-kerzen | Wostok-Station | Russland | -78.4642 | 106.8369 |
| 8-klassenfahrt | Dumont-d’Urville-Station | Frankreich | -66.6628 | 140.0013 |
| 8-pool | Davis-Station | Australien | -68.5759 | 77.9695 |
| 8-radtour | Casey-Station | Australien | -66.2823 | 110.5268 |
| 8-roller | Mawson-Station | Australien | -67.6026 | 62.8730 |
| 8-saftbar | Syowa-Station | Japan | -69.0041 | 39.5818 |
| 8-schuelerzeitung | Zhongshan-Station | China | -69.3732 | 76.3719 |
| 8-schulfest | Arctowski-Station | Polen | -62.1598 | -58.4733 |
| 8-zelt | Scott Base | Neuseeland | -77.8494 | 166.7673 |
<!-- AUTO:ENDE -->
