# Postfach reise-aufbau

## 2026-11-22 17:30 – FERTIG: Reise-Aufbau 3

Grundlage: AUFTRAEGE `lernen-app` 723770dd, „Entscheidungen Sebastian (17:05)“, Abschnitt „An reise-aufbau – Reise-Aufbau 3“. Nur Vorschlag – kein App-Code, keine DB-Änderung (DB nur gelesen). Dateien in `inhalte/reise/`.

**Ergebnis (Prüfskript grün, Exit 0):**
- 95 Flüge (87 + 8 neue Teile); 95 Länder/Landesteile, jedes einmal.
- 615 Städte (606 + 9 neue Etappen), jede einmal; Städte = Etappen bei allen Flügen.
- 615/615 Städte in GeoNames im richtigen Land/Landesteil, alle mit Koordinaten; 9/9 begonnene Orte erhalten.

**Umgesetzt:**
- **61 Teil 2 → Salomonen:** Honiara → Tulagi → Auki → Kirakira. Kein Nachbar Neuseelands, wie entschieden.
- **101 geteilt:** Teil 1 bleibt Brasilien – Südosten (7 Städte); **Teil 2 → Brasilien – Mittelwesten**, Kurzflug mit Brasília (`cavalieri`). Die beiden Großregionen grenzen aneinander.
- **Neue Etappen LK-D 3:**
  - 91 `koerper_symmetrie` → Porto Alegre
  - 29 `gleichungen_binomisch` → Turkmenistan, neu geordnet: Daschoguz → Türkmenabat → Mary → Aschgabat
  - 101 `cavalieri` → Brasília
- **Marokko → Algerien → Mauretanien** unverändert.
- **Kür je Etappe:** Das Prüfskript übernimmt `etappen[].kuer_in` aus `lk_teilung_2211.json`, sobald LK-D 4 es liefert (heute noch nicht in der JSON). An der Reise ändert das nichts, auch Kür-Etappen haben eine Stadt.
- **Abgleich `lk_teilung_2211.json`** (723770dd, 7 Themen, 15 Teile): alle Teile da, Etappen disjunkt und vollständig.
- **Abgleich DB:** unverändert seit Reise-Aufbau 2 (Prüfsumme über Einheiten und Lernziele identisch).

**Offen:**
1. **Reserve Ozeanien:** nur noch 1 Gebiet (Australian Capital Territory, 4 Orte). Mehr geht nur, wenn ein belegtes Gebiet geteilt wird, z. B. „Papua-Neuguinea – Inseln“.
2. **Falls 57 geteilt wird:** South Australia hat keinen freien Nachbarn – Australian Capital Territory oder Kangaroo Island als Landesteil.
3. **Falls 2 geteilt wird:** Tadschikistan ist vorgemerkt (Landgrenze). Asiens Reserve sinkt dann auf 2.
4. **Lizenz COMNAP** (Stationen): nur Bildung/nicht kommerziell – in die Lizenzklärung RK.

## 2026-11-22 16:55 – FERTIG: Reise-Aufbau 2

Grundlage: AUFTRAEGE `lernen-app` ea507c4 („Vorschlag fortschreiben“ 15:25, „Entscheidung Teilung“ 16:20), Berichtigung Sebastian: **7 neue Flüge (13 Teile), nicht 9**. Nur Vorschlag – kein App-Code, keine DB-Änderung (DB nur lesend). Dateien in `inhalte/reise/`; Bericht `aufbau-vorschlag.md`, Daten `aufbau-vorschlag.json`.

**Ergebnis (Prüfskript grün, Exit 0):** 94 Flüge (87 + 7 Teile), 94 Länder/Landesteile je einmal, 612 Städte je einmal (606 + 6 neue LK-D-Etappen), Städte = Etappen bei allen Flügen, 612/612 Städte in GeoNames im richtigen Land/Landesteil, 9/9 begonnene Orte erhalten, 21 Stationen.

| Thema | Teil 1 | neue Teile |
|---|---|---|
| 26 | Kuba (5) | Jamaika (3, über das Meer) |
| 29 | Kasachstan (5) | Turkmenistan (3) |
| 44 | Ruanda (5) | Burundi (2, Kurzflug) |
| 46 | Marokko (6) | Algerien (3), Mauretanien (3) |
| 61 | Neuseeland – Nordinsel (2, Kurzflug) | Neukaledonien (4, über das Meer) |
| 91 | Paraguay (3) | Brasilien – Süden (3) |

- **Neue Etappen-Städte:** 46 → Algier, Atar; 44 → Gitega; 91 → Ciudad del Este; Kür: 47 → Nyeri, 99 → Portoviejo.
- **Brasilien nach Großregionen:** 101 = Brasilien – Südosten (andere Städte; 101 ohne Lernstand), damit 91 Teil 2 ein Nachbargebiet hat (alle Nachbarländer Paraguays waren belegt).
- **DB-Abgleich:** Einheiten und Etappenzahlen unverändert seit dem Morgen; die 6 LK-D-Etappen und die Teilung sind noch nicht in der DB (in der JSON gekennzeichnet).
- **Karte:** je Stadt Breite/Länge + `geonames_id`; je Land/Landesteil `mitte` (Natural Earth), `iso`, deutsche Hauptstadt mit Lage, bei Landesteilen `hauptort_landesteil`; Stationen mit Koordinaten (COMNAP 2024, gegen die Liste abgeglichen).
- **Reserve:** Europa 5, Nordamerika 3, Asien 3, Orient 4, Afrika 3, Südamerika 4 (3 brasilianische Großregionen + Suriname), Ozeanien **nur 2**, Pazifik 3 (Palau nur 3 Orte); dazu 18 frei gewordene Städte.
- **Erweiterbar:** Teilung wird aus `lk_teilung_2211.json` gelesen; ein dort neu geteiltes Thema ohne Eintrag ist ein Skript-Fehler mit vorgemerktem Nachbarn (2 → Tadschikistan, 101 → Brasilien – Mittelwesten/Nordosten). Gegen `lk_teilung_2211.json` von ea507c4 abgeglichen: 13 Teile, passt.

**Offen / Entscheidung Sebastian bzw. Haupt-Chat:**
1. 46 Teil 3 Mauretanien grenzt an Marokko nur über Westsahara (an Algerien direkt). Alternative Mali (Reisewarnung).
2. 61 Teil 2 Neukaledonien (am Morgen gemieden). Alternative Salomonen (kein Nachbar).
3. Falls 57 geteilt wird: South Australia hat keinen freien Nachbarn – ACT oder Kangaroo Island als Landesteil.
4. Reserve Ozeanien: drittes Gebiet nur mit „Papua-Neuguinea – Inseln“ (80 hieße dann „– Festland“).
5. LK-D-2-Bericht nennt im Kopf „15 Teile“ – Liste/JSON haben 13 (an `lehrplan-lb`).
6. Lizenz COMNAP (Stationen): nur Bildung/nicht kommerziell – in die Lizenzklärung RK.
