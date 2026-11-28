# Adventskalender – Server (ADVENT-S): Schnittstelle für den App-Helfer

Stand 28.11.2026 · Zweig `helfer-advent-server` · **nichts eingespielt, nichts live.**

Dateien:
- Migration: `supabase/migrations/20261209_advent_s.sql`
- Pakete: `tools/tests/aus/advent_s_probe.sql` / `advent_s_einspielen.sql` (erzeugt von `tools/tests/advent_pakete.py`)
- Tests: `tools/tests/advent_s_test.py`
- Belegung: `tools/advent_belegung_sql.py`, Beispiel `belegung-beispiel.json`
- Edge Function (vorbereitet): `supabase/functions/lernen-api/index.ts` 0.10.0

Der App-Teil (`lernen*.js`, CSS, `sw.js`, …) ist **nicht** angefasst.

---

## 1. Was gilt (verbindlich, ersetzt Abweichendes in `entwurf1/konzept.md` und `umsetzung1.md`)

1. **24 Türchen, 1.–24.12.**
   - Ein Türchen geht auf nach einer **geschafften Etappe an diesem Tag**. Das ist eine eigene Landung oder „Sitzt wieder!“ nach dem Nachbessern.
   - Je Türchen braucht es eine **eigene Etappe**. Dieselbe Etappe zählt am selben Tag nur einmal.
   - Höchstens **2 Türchen pro Tag**.
   - Es geht immer das **älteste** geschlossene, fällige Türchen auf.
   - Tür *n* ist fällig ab Start + *n* − 1. Türchen der Zukunft gehen nie auf.
2. **Datumsgrenzen** stehen als Einträge in `schule.regel`, sie sind kein festes Datum im Code.
   - `advent_start` = `"2026-12-01"`
   - `advent_nachholen_bis` = `"2027-01-06"` (einschließlich)
   - `advent_sichtbar_bis` = `"2027-01-06"` (einschließlich)
   - Ab 7.1. Ortszeit ist der Kalender weg; geschlossene Türchen verfallen.
   - Offene Gutscheine und Krampus-Aufgaben bleiben abrufbar und einlösbar.
3. **„Tag“** ist der Kalendertag in der gespeicherten Lernort-Zeitzone des Kindes (`schule.lernender.zeitzone`).
   - Es gibt **keinen** Rückfall auf Berlin.
   - Fehlt die Zeitzone oder ist sie ungültig, kommt `grund: "zeitzone_fehlt"`.
4. **Inhalte je Kind und Tür** legen die Eltern fest:
   - `art`: `bild` · `gutschein` · `sterne` · `karte` · `krampus` · `leer`
   - `variante`:
     - bei `sterne`: `normal` | `jackpot` | `niete`
     - bei `gutschein`: `normal` | `tausch` (Tauschkarte)
     - sonst leer
   - `titel` (höchstens 80 Zeichen), `text` (höchstens 300), `motiv` (Schlüssel)
   - `sterne`: ganze Zahl 0–5000. **Jede** Art kann Sterne tragen, z. B. Tür 24 als Karte mit Jackpot.
5. **Gutscheine** liegen in „Meine Gutscheine“.
   - Das **Kind** löst selbst ein. Es gibt kein Anfragen und kein Bestätigen.
   - Die Eltern sehen, wer was wann eingelöst hat. Sie können ebenfalls einlösen („ausschalten“) und **zurückholen**; der Gutschein ist dann wieder offen.
   - Gutscheine verfallen nicht.
   - **Krampus-Aufgaben** setzen nur die Eltern auf erledigt bzw. „noch nicht“.
6. **Tauschkarte**: Das Kind tauscht einen eigenen offenen Gutschein gegen einen offenen Gutschein des Geschwisters, ohne dessen Zustimmung. Die Karte ist danach verbraucht.
   - **Schalter `advent_tausch`, Standard AUS** (siehe Abschnitt 9).
7. **„Beide am selben Tag“** ist nur eine Frage der Belegung: `belegung_setzen` mit `lernender_ids: [1, 2]`.
8. Der Inhalt **geschlossener** Türchen erreicht das Gerät des Kindes nie. Die Eltern-Aktionen sehen alles.
9. **Sterne** werden beim Öffnen genau einmal gebucht:
   - Buchung in `schule.sterne`, Grund `advent`, Bezug `advent:<jahr>:<nr>`, eindeutig.
   - Wiederholte, doppelte oder gleichzeitige Aufrufe buchen nie doppelt und öffnen nie zwei Türchen für eine Etappe.
10. Die Weihnachts-Ebene der Karte braucht keinen Server, siehe Abschnitt 6.

**Schalter `advent_aktiv`** (in `schule.regel`):

| Wert | Wirkung |
|---|---|
| `0` (Standard) | Alle Kind-Aktionen liefern `{"ok":true,"aktiv":false,"grund":"nicht_aktiv"}` und buchen nichts. |
| `1` | an |
| `2` | nur das Testkind (`lernender.ist_test`) |

Die Eltern-Aktionen gehen immer, damit die Eltern vor dem Start füllen können.

## 2. Wie der Server eine „geschaffte Etappe“ erkennt (nur lesen)

Grundlage ist `schule.karte_stand` des Kindes. Gezählt wird eine Zeile mit:
- `sitzt` = true,
- `landung_art` nicht leer,
- `landung.am = sitzt_am`, und das Datum von `sitzt_am` in der Lernort-Zeitzone ist **heute**.

So schreiben es live `karte_buchen` → `landung_speichern` bei einer eigenen Landung **und** bei „Sitzt wieder!“; die Landezeit ist neu und `landung_art` ist `sauber`.

Nicht gezählt werden:
- eine Setzung („Kann er“: neue `sitzt_am` ohne neue `landung`),
- gesetzte Etappen ohne `landung_art`,
- eine Etappe, die heute schon ein Türchen geöffnet hat.

Die Landung von 23:50 Uhr gilt nur für ihren Tag. Wer sie bis Mitternacht nicht einlöst, verliert dieses Türchen nicht: Es bleibt fällig und kann nachgeholt werden. Es braucht dann aber eine neue Etappe.

## 3. Aktionen

Alle Aktionen gehen über `POST /lernen-api/aktion {aktion, daten}`. Erwartbare Zustände kommen als `ok: true` mit `grund`. Echte Fehler kommen als `ok: false, fehler: "<Text>"`; das sind Rechte, falsche Eingaben und Verbote.

### Gemeinsame Fehler

| Fehlertext | wann |
|---|---|
| `Nicht angemeldet` | keine gültige Sitzung |
| `Kein Zugriff auf diesen Lernenden` | ein Kind fragt ein anderes Kind ab |
| `lernender_id fehlt` | |
| `Kind nicht gefunden` | Kind fehlt oder ist inaktiv |
| `Nur Eltern` | Eltern-Aktion mit Kind- oder Lehrer-Zugang |
| `Adventskalender: Einstellung in schule.regel ungültig (…)` | falsche Regel-Werte |

### 3.1 `schule_advent_stand` – Kind (Kalender, Hinweiszeile, Menü)

**Eingabe:** `{lernender_id}`

**Antwort, wenn der Kalender läuft:**

```json
{"ok": true, "aktiv": true, "jahr": 2026, "heute": "2026-12-04", "ortszeit": "2026-12-04T18:00", "zeitzone": "Australia/Melbourne",
 "start": "2026-12-01", "nachholen_bis": "2027-01-06", "sichtbar_bis": "2027-01-06", "phase": "laeuft", "tag_nr": 4,
 "max_pro_tag": 2, "offen_heute": 0, "etappen_heute": 1, "moeglich_heute": 2, "frei_heute": 1, "naechste_nr": 1,
 "bereit": true, "braucht_etappe": false, "tausch": true,
 "tueren": [{"nr": 1, "zustand": "bereit"}, {"nr": 2, "zustand": "nachholen"}, {"nr": 3, "zustand": "nachholen"},
            {"nr": 4, "zustand": "heute"}, {"nr": 5, "zustand": "morgen"}, {"nr": 6, "zustand": "zu"}, "…"],
 "gutscheine": {"offen": 0, "tauschkarten": 0, "eingeloest": 0, "krampus_offen": 0, "krampus_erledigt": 0},
 "menue": {"kalender": true, "gutscheine": true}}
```

Eine **offene** Tür trägt zusätzlich die Kachel-Angaben:

```json
{"nr": 1, "zustand": "offen", "art": "bild", "variante": null, "titel": null, "motiv": "koala", "sterne": 50, "nachgeholt": true, "tag": "2026-12-04"}
```

Den vollen Text liefert `tuer_lesen`.

**Antwort, wenn der Kalender nicht da ist** (vor dem Start, nach `sichtbar_bis`, ohne Zeitzone):

```json
{"ok": true, "aktiv": false, "grund": "vorbei", "heute": "2027-01-07", "start": "2026-12-01", "sichtbar_bis": "2027-01-06",
 "gutscheine": {"offen": 1, "tauschkarten": 0, "eingeloest": 1, "krampus_offen": 1, "krampus_erledigt": 0},
 "menue": {"kalender": false, "gutscheine": true}}
```

`grund` ist `vor_start`, `vorbei` oder `zeitzone_fehlt`. Bei Schalter aus kommt nur `{"ok":true,"aktiv":false,"grund":"nicht_aktiv"}`.

**Felder:**

| Feld | Bedeutung |
|---|---|
| `phase` | `laeuft` (Tag 1–24) · `nachholen` (ab 25.12. bis `nachholen_bis`, keine „heute“-Tür mehr) · `nur_ansehen` (nach `nachholen_bis`, aber vor oder an `sichtbar_bis`) |
| `tag_nr` | Tag seit Start (1 = 1.12.); kann über 24 liegen |
| `etappen_heute` | geschaffte Etappen heute |
| `moeglich_heute` | wie viele Türchen heute noch höchstens gehen (Limit und fällige geschlossene) |
| `frei_heute` | wie viele **jetzt** gehen (dafür ist schon eine Etappe da) |
| `naechste_nr` | welches als Nächstes aufgeht |
| `bereit` | `frei_heute > 0` |
| `braucht_etappe` | heute geht noch eins, aber erst nach der nächsten Etappe |

**Tür-Zustände:**

| Zustand | Bedeutung |
|---|---|
| `offen` | geöffnet |
| `bereit` | = `naechste_nr`, wenn `frei_heute > 0`; in der Hinweiszeile gold |
| `heute` | `nr = tag_nr` |
| `nachholen` | fällig, älter als heute |
| `morgen` | `nr = tag_nr + 1`, wenn morgen noch geöffnet werden darf |
| `zu` | Zukunft |
| `verfallen` | nur in `nur_ansehen`; vor dem Start ist der Kalender gar nicht da |

**Menü** (ersetzt „1.12.–31.1.“ aus `umsetzung1.md`):
- „Adventskalender“, solange `menue.kalender` gilt, also vom Start bis `sichtbar_bis`.
- „Meine Gutscheine“, solange `menue.gutscheine` gilt: im Kalenderzeitraum **oder** solange ein Gutschein bzw. eine Krampus-Aufgabe offen ist. Das gilt auch nach dem Ende.

**Hinweiszeile in „Gerade dran“:**

| Lage | Text |
|---|---|
| `bereit` | „Türchen {naechste_nr} ist bereit – jetzt öffnen ›“ |
| `braucht_etappe` | „Türchen … warten – je Etappe eins ›“ (Zahl aus den Türen `heute`/`nachholen`) |
| `moeglich_heute = 0` und noch geschlossene fällige | „2 Türchen heute offen – morgen geht's weiter ›“ |
| alle offen | keine Zeile |

### 3.2 `schule_advent_oeffnen` – Kind (Tür nach der Etappe, „bereit“ im Kalender)

**Eingabe:** `{lernender_id, client_id}`
- `client_id`: 1–200 Zeichen, je Tipp neu, z. B. `lernCid()`.
- Bei einer Netz-Wiederholung dieselbe `client_id` noch einmal schicken.
- Das Gerät wählt **keine** Tür; der Server nimmt die älteste.

**Antwort beim Öffnen:**

```json
{"ok": true, "aktiv": true, "geoeffnet": true, "wiederholt": false,
 "tuer": {"nr": 2, "tag": "2026-12-04", "geoeffnet_am": "2026-12-04T06:30:00+00:00", "nachgeholt": true,
          "art": "gutschein", "variante": "normal", "titel": "Kinoabend", "text": "Du suchst den Film aus.", "motiv": null,
          "sterne": 0, "sterne_gutgeschrieben": false, "gutschein": {"id": 1, "art": "gutschein", "zustand": "offen"}},
 "frei_heute": 0, "moeglich_heute": 0, "naechste_nr": 3,
 "gutscheine": {"offen": 1, "tauschkarten": 0, "eingeloest": 0, "krampus_offen": 0, "krampus_erledigt": 0}}
```

- Dieselbe `client_id` noch einmal: dieselbe `tuer` mit `"wiederholt": true`. Es wird nichts gebucht.
- `sterne_gutgeschrieben`: true, wenn die Sterne gebucht sind. Danach `lernVergessen(kind)`, damit Konto und Sterne-Chip neu laden.
- `gutschein` steht nur bei Gutschein, Tauschkarte und Krampus.

**Nicht geöffnet** (`ok: true, geoeffnet: false, grund`):

| `grund` | Bedeutung | App |
|---|---|---|
| `keine_etappe` | Heute ist keine unverbrauchte Etappe da. Auch das zweite Gerät nach dem ersten bekommt das. | still weiter; `letzte_nr` = heute zuletzt geöffnete Tür, die die App mit `tuer_lesen` zeigen kann |
| `limit` | heute schon `max_pro_tag` | still weiter; `letzte_nr` wie oben |
| `alles_offen` | alle fälligen sind offen | still weiter |
| `nachholen_vorbei` | Phase `nur_ansehen` | still weiter |

Die Gründe `nicht_aktiv`, `vor_start`, `vorbei` und `zeitzone_fehlt` kommen als `aktiv: false`.

**Fehler:**
- `client_id fehlt (1 bis 200 Zeichen)`
- `Das geht nur in der App des Kindes (Eltern: nur fürs Testkind)`

### 3.3 `schule_advent_tuer_lesen` – Kind (offene Tür ansehen)

**Eingabe:** `{lernender_id, nr}`

**Antwort:** `{"ok":true,"aktiv":true,"tuer":{…wie bei oeffnen…}}`

**Fehler:**
- `Türchen 7 ist noch zu`: geschlossene Tür, kein Inhalt.
- `nr: 1 bis 24`

### 3.4 `schule_advent_gutscheine` – Kind („Meine Gutscheine“)

**Eingabe:** `{lernender_id}`

Diese Aktion geht auch vor und nach dem Kalenderzeitraum, solange der Schalter an ist.

```json
{"ok": true, "aktiv": true,
 "zaehler": {"offen": 2, "tauschkarten": 1, "eingeloest": 0, "krampus_offen": 1, "krampus_erledigt": 0},
 "gutscheine": [{"id": 1, "nr": 2, "art": "gutschein", "titel": "Kinoabend", "text": "Du suchst den Film aus.", "zustand": "offen", "getauscht": false},
                {"id": 2, "nr": 3, "art": "tausch", "titel": "Tauschkarte", "zustand": "offen", "getauscht": false}],
 "krampus": [{"id": 3, "nr": 4, "art": "krampus", "titel": "Zimmer aufräumen", "text": "Heute noch.", "zustand": "offen", "getauscht": false}],
 "tausch": {"aktiv": true, "tauschkarten": 1,
            "geschwister": [{"lernender_id": 2, "name": "Kind 2", "gutscheine": [{"id": 4, "nr": 2, "titel": "Kinoabend", "text": "…", "motiv": null}]}]},
 "menue": {"gutscheine": true}}
```

**Reihenfolge:** offene zuerst, dann nach Tür.

**Zustände:**

| Art | Zustände |
|---|---|
| `gutschein` | `offen` · `eingeloest` |
| `tausch` | `offen` · `verbraucht` · `eingeloest` (nur wenn die Eltern sie ausschalten) |
| `krampus` | `offen` · `erledigt` |

**Weitere Felder:**
- `eingeloest_am`, `eingeloest_von` (beim Kind nur `kind` oder `eltern`)
- `zurueckgeholt_am`, `erledigt_am`, `verbraucht_am`
- `getauscht` / `getauscht_am`: durch Tausch erhalten oder abgegeben

`tausch.geschwister` ist nur gefüllt, wenn der Tausch an ist **und** das Kind eine offene Tauschkarte hat. Es enthält die offenen normalen Gutscheine der anderen Kinder derselben Familie; das Testkind ist eine eigene Familie.

### 3.5 `schule_advent_einloesen` – Kind (selbst „Eingelöst“)

**Eingabe:** `{lernender_id, gutschein_id}`

**Antwort:**

```json
{"ok": true, "aktiv": true, "wiederholt": false,
 "gutschein": {"id": 1, "zustand": "eingeloest", "eingeloest_am": "…", "eingeloest_von": "kind", "…": "…"},
 "zaehler": {"…": "…"}}
```

War der Gutschein schon eingelöst (zwei Geräte), kommt `wiederholt: true` ohne Änderung.

**Fehler:**
- `Gutschein nicht gefunden`: fremd, unbekannt oder gerade weggetauscht.
- `Krampus-Aufgaben haken nur Mama oder Papa ab`
- `Die Tauschkarte wird beim Tauschen verbraucht`

### 3.6 `schule_advent_tauschen` – Kind (Tauschkarte)

**Eingabe:** `{lernender_id, tauschkarte_id, mein_gutschein_id, fremder_gutschein_id, client_id}`

**Antwort:**

```json
{"ok": true, "aktiv": true, "getauscht": true, "wiederholt": false,
 "tausch": {"id": 1, "am": "…", "jahr": 2026, "von_lernender_id": 1, "mit_lernender_id": 2, "tauschkarte_id": 2, "gegeben_id": 1, "bekommen_id": 4},
 "zaehler": {"…": "…"}}
```

- Dieselbe `client_id` noch einmal: `wiederholt: true`.
- Schalter aus: `{"ok":true,"aktiv":true,"getauscht":false,"grund":"tausch_aus"}`.

**Fehler (Verbote):**
- `… drei verschiedene Gutscheine`
- `… keine Tauschkarte von dir`
- `… die Tauschkarte ist schon verbraucht`
- `… dein Gutschein wurde nicht gefunden`
- `… Gutschein des Geschwisters nicht gefunden`
- `… nur normale Gutscheine (keine Krampus-Aufgabe, keine Tauschkarte)`
- `… nur offene Gutscheine (nicht eingelöst)`
- `… nur mit dem Geschwister`
- `… hat gerade den Besitzer gewechselt – bitte neu laden`
- Eltern nur fürs Testkind

Danach beide Listen neu laden.

### 3.7 `schule_advent_eltern` – Eltern (Übersicht beider Kinder)

**Eingabe:** `{protokoll?}`, die Zahl der letzten Protokoll-Einträge (Standard 10, höchstens 100).

**Antwort:**

```json
{"ok": true, "einstellung": {"aktiv": 1, "start": "2026-12-01", "nachholen_bis": "2027-01-06", "sichtbar_bis": "2027-01-06", "max_pro_tag": 2, "tausch": 0, "jahr": 2026},
 "kinder": [{"lernender_id": 1, "name": "Kind 1", "ist_test": false, "familie": "familie", "offen": 4, "belegt": 24,
             "lage": {"phase": "laeuft", "heute": "2026-12-05", "ortszeit": "…", "zeitzone": "…", "offen_heute": 2, "etappen_heute": 2,
                      "frei_heute": 0, "moeglich_heute": 0, "naechste_nr": 5, "grund": null, "…": "…"},
             "zaehler": {"…": "…"},
             "gutscheine": [{"id": 4, "nr": 2, "art": "gutschein", "titel": "…", "zustand": "offen", "getauscht": true, "getauscht_am": "…",
                             "herkunft_lernender_id": 2, "lernender_id": 1, "eingeloest_am": "…", "eingeloest_von": "kind:Kind 1",
                             "zurueckgeholt_am": "…", "zurueckgeholt_von": "eltern:Mama", "…": "…"}]}],
 "ohne_teilnahme": [{"lernender_id": 3, "name": "Testkind", "ist_test": true}],
 "protokoll": [{"id": 12, "am": "…", "lernender_id": 2, "aktion": "getauscht_von_geschwister", "nr": 2, "gutschein_id": 4, "von": "kind:Kind 1", "daten": {"…": "…"}}]}
```

- Ein Kind „nimmt teil“, sobald es eine Belegung hat.
- `lage.grund = "zeitzone_fehlt"` zeigt eine fehlende Zeitzone an.
- **„Zu tun“-Zeilen:** offene Krampus-Aufgaben (`art = krampus`, `zustand = offen`) mit „Erledigt ✓ | Noch nicht“. Eingelöste Gutscheine erscheinen als Info („Kind 1 hat … eingelöst“, `eingeloest_am`) mit „Zurückholen“.

### 3.8 `schule_advent_belegung_lesen` – Eltern (Raster je Kind, auch geschlossene Türen)

**Eingabe:** `{lernender_id?}`. Ohne `lernender_id` kommen alle teilnehmenden Kinder.

**Antwort:** `{"ok":true,"jahr":2026,"kinder":[{"lernender_id","name","ist_test","tueren":[…24…]}]}`

Je Tür:
- `belegung`: `{art, variante, titel, text, sterne, motiv, geaendert_am, geaendert_von}` oder `null`. Kein Inhalt bedeutet „nur Licht“ beim Öffnen.
- `offen`, `geoeffnet_am`, `tag`, `nachgeholt`, `sterne_gutgeschrieben`
- `inhalt_beim_oeffnen`: Schnappschuss; spätere Änderungen ändern Geöffnetes nicht.
- `etappe`: `{einheit_id, lernziel, sitzt_am, landung_art}`
- `gutschein`

### 3.9 `schule_advent_belegung_setzen` – Eltern (je Kind oder beide zugleich)

**Eingabe:**

```json
{"lernender_id": 1, "tueren": [{"nr": 7, "art": "gutschein", "variante": "tausch", "titel": "Tauschkarte"}]}
{"lernender_ids": [1, 2], "tueren": [{"nr": 24, "art": "karte", "motiv": "heiligabend", "text": "…", "sterne": 2000}], "nur_geschlossene": true}
```

- Erlaubte Felder je Tür: `nr`, `art`, `variante`, `titel`, `text`, `sterne`, `motiv`. Ein unbekanntes Feld ist ein Fehler.
- Eine Tür mit `art: "leer"` setzt den Inhalt auf leer.

**Antwort:**

```json
{"ok": true, "jahr": 2026, "kinder": [{"lernender_id": 1, "gesetzt": 1, "unveraendert": 0, "uebersprungen_offen": []}]}
```

**Nur geschlossene Türchen:**
- Ist eine genannte Tür schon offen, bricht der Aufruf **ohne Änderung** ab: `Belegung: schon offene Türchen bleiben, wie sie sind (Kind 1: 3, 5) – nichts geändert; nur_geschlossene: true überspringt sie`.
- Mit `nur_geschlossene: true` werden offene Türen übersprungen und in `uebersprungen_offen` gemeldet.

**Prüfungen** (Fehlertext jeweils `Tür n: …`):
- `nr` 1–24, keine Tür doppelt
- `art` aus der Liste; `variante` passend zur Art
- `bild` braucht `motiv`; `gutschein` und `krampus` brauchen `titel`
- `sterne` ganze Zahl 0–5000
- Längen: `titel` höchstens 80, `text` höchstens 300
- `motiv` als Schlüssel `[a-z0-9_]`

**Nicht** auf dem Server geprüft: die Mischregeln aus Konzept 13 (Tür 6/24 Karte, Krampus nicht auf 1/24 …). Die hält die Eltern-Seite ein.

**Motiv-Schlüssel** (Entwurf 2, `teile/v_motive2.js`):
- allgemein: `koala`, `surf`, `neonbaum`, `pinguin`, `polarlicht`, `flieger`, `kaenguru`, `sandmann`, `erdkugel`, `rentier`, `bordkarte`, `controller`, `strandfeuer`, `kompass`, `schneeflocke`, `stern`
- Sonder-Motive: `krampus`, `nikolaus`, `heiligabend`

### 3.10 `schule_advent_gutschein_eltern` – Eltern

**Eingabe:** `{gutschein_id, aktion}`

| `aktion` | gilt für | Wirkung |
|---|---|---|
| `einloesen` | Gutschein, Tauschkarte | ausschalten |
| `zurueckholen` | Gutschein, Tauschkarte | eingelöst → offen; `zurueckgeholt_am/von` |
| `erledigt` | Krampus | erledigt |
| `noch_nicht` | Krampus | zurück auf offen |

**Antwort:** `{"ok":true,"unveraendert":false,"gutschein":{…mit wer/wann…}}`. Ist nichts zu tun, kommt `unveraendert: true`.

**Fehler:**
- `Krampus-Aufgabe: erledigt oder noch_nicht`
- `erledigt / noch_nicht nur bei Krampus-Aufgaben`
- `Die Tauschkarte ist schon beim Tauschen verbraucht`
- `Gutschein wurde gerade getauscht – bitte neu laden`

### 3.11 `schule_advent_protokoll` – Eltern

**Eingabe:** `{lernender_id?, anzahl?}`; Standard 50, höchstens 500.

**Antwort:** `{"ok":true,"eintraege":[{id, am, lernender_id, name, aktion, nr, gutschein_id, von, daten}]}`

`aktion` ist eine von: `oeffnen`, `einloesen`, `eltern_einloesen`, `eltern_zurueckholen`, `eltern_erledigt`, `eltern_noch_nicht`, `tausch`, `getauscht_von_geschwister`, `belegung`.

## 4. Was sich gegenüber `umsetzung1.md` / Konzept ändert

**Datenmodell:**
- Es gibt keinen gemeinsamen Vorrat `advent_inhalt` und keine `inhalt_id`. Die Belegung steht direkt je Kind und Tür (`advent_belegung`).
- „Beide“ heißt: gleiche Belegung für mehrere `lernender_ids`.
- Ideenliste und „Mischen“ bleiben auf dem Gerät der Eltern; gespeichert wird mit `belegung_setzen`.
- Die Art heißt `bild` statt `motiv`. Neu ist `leer` als ausdrückliche Art.
- `sterne` kann bei **jeder** Art stehen, auch bei `karte` (Tür 24 = Karte + Jackpot).

**Einlösen:**
- Das **Kind** löst selbst ein.
- Entfallen sind `angefragt` und `heute nicht`/`spaeter`, die Zu-tun-Zeile „möchte einlösen“ und die Aktion `schule_advent_gutschein_anfragen`.
- Die Eltern können ausschalten und zurückholen (`schule_advent_gutschein_eltern` statt `…_entscheiden`).

**Zeitraum:**
- Nachholen bis 6.1. statt 31.12. Sichtbarkeit bis 6.1. statt bis 31.1.
- Alle Grenzen stehen in `schule.regel`.
- „Meine Gutscheine“ bleibt über den 6.1. hinaus, solange etwas offen ist (`menue.gutscheine`).

**Neu:**
- `schule_advent_tauschen` mit Tauschkarte (Gutschein-Variante `tausch`)
- Felder `tausch` in Stand und Gutscheinen
- Rubrik „Vom Krampus“ = `krampus`-Liste (ohne Knopf beim Kind)

**Entfallen:**
- `schule_advent_tuer_zuruecknehmen`: nicht beauftragt; falls nötig, Stufe 2.
- `schule_advent_inhalt_setzen` / `schule_advent_lesen` heißen jetzt `belegung_setzen` / `belegung_lesen` / `eltern`.

**Weitere Änderungen:**
- Fehlende Zeitzone ergibt `zeitzone_fehlt` statt Berliner Zeit.
- Antworten tragen `ok: true` mit `grund` statt Fehlertexten für „Heute schon 2“ / „Erst nach deiner nächsten Etappe“ (`limit` / `keine_etappe`).
- Öffnen und Tauschen durch Eltern geht nur fürs Testkind.

## 5. Felder, die die App je Zustand braucht

| Stelle | Felder |
|---|---|
| Tür nach der Etappe (A1) | vorher `stand.bereit`/`naechste_nr` (parallel zu `lernExNachLandung`), dann `oeffnen` → `tuer.*`, `sterne_gutgeschrieben`, `gutschein`. Bei `grund` still weiter. |
| Nachbessern „Sitzt wieder!“ | dieselbe Hülle; der Server zählt es als Etappe |
| Kalender (A2) | `stand.tueren[]` (`zustand` + Kachel-Felder bei offen), `phase`, `heute`, `tag_nr`; offene per `tuer_lesen`, `bereit` per `oeffnen` |
| Hinweiszeile (A3) | `bereit`, `naechste_nr`, `braucht_etappe`, `moeglich_heute`, `offen_heute`, `tueren` |
| Menü | `stand.menue.kalender`, `stand.menue.gutscheine`, Zähler aus `stand.gutscheine` |
| Meine Gutscheine | `gutscheine`, `krampus`, `zaehler`, `tausch`; Knopf „Eingelöst“ nur bei `art = gutschein` und `zustand = offen`; Tauschkarte mit „Tauschen“, wenn `tausch.aktiv` |
| Eltern-Seite | `eltern` (Heute je Kind, Gutscheine mit wer/wann, Zu tun), `belegung_lesen` (Raster), `belegung_setzen`, `gutschein_eltern`, `protokoll` |

**Neu laden:**
- nach `visibilitychange` (Mitternacht in der Lernort-Zeitzone)
- nach jeder schreibenden Aktion

## 6. Hinweis Weihnachts-Ebene der Karte (kein Server)

Die Ebene soll **dieselben Datumsgrenzen** nutzen: sichtbar ab 1.12. bis einschließlich **6.1.** (nicht nur bis 31.12.).

- Ohne Server: Gerätedatum mit fester Grenze 1.12.–6.1.
- Besser, wenn ohnehin geladen: `stand.start` und `stand.sichtbar_bis` aus `schule_advent_stand`. Sie kommen auch bei `aktiv: false` (`vor_start`/`vorbei`), nur nicht bei Schalter aus.

## 7. Belegungs-Werkzeug (`tools/advent_belegung_sql.py`)

Die echte Belegung mit persönlichen Texten liegt **außerhalb des Repos**. Das Werkzeug weigert sich, eine Eingabe im Repo zu lesen (außer dieser Beispiel-Datei) oder in das Repo zu schreiben.

**Format:**

```json
{"jahr": 2026,
 "kinder": {"Kind 1": 1, "Kind 2": 2},
 "tueren": [{"nr": 1, "fuer": "beide", "art": "bild", "motiv": "koala", "text": "…", "sterne": 50},
            {"nr": 3, "fuer": "Kind 1", "art": "sterne", "variante": "jackpot", "sterne": 1111},
            {"nr": 3, "fuer": "Kind 2", "art": "gutschein", "titel": "…"},
            {"nr": 24, "fuer": ["Kind 1", "Kind 2"], "art": "karte", "motiv": "heiligabend", "text": "…", "sterne": 1000}]}
```

- `kinder`: Bezeichnung → `lernender_id`. Die ID vorher in der Datenbank nachsehen.
- `fuer`: `"beide"` (Standard = alle in `kinder`), eine Bezeichnung oder eine Liste davon.
- Jede Kombination aus Kind und Tür höchstens einmal.
- Felder wie bei `belegung_setzen`; `motiv` muss einer der Schlüssel aus Abschnitt 3.9 sein.
- Fehlende Türen bleiben, wie sie sind. Sind sie nie belegt, erscheinen sie im Bericht unter `ohne Inhalt` und öffnen sich als „nur Licht“.

**Aufruf:**

```
python3 -I tools/advent_belegung_sql.py ~/privat/belegung.json --aus ~/privat/
```

Das schreibt `advent_belegung_probe.sql` und `advent_belegung_einspielen.sql`.

**Das Paket:**
- ein Aufruf, Zeitgrenzen als erste Anweisung
- prüft, dass ADVENT-S eingespielt ist, mit genau dieser Fassung von `schule.advent_belegen` (md5)
- prüft Jahr = Einstellung und dass die Kinder vorhanden und aktiv sind
- setzt je Kind über `schule.advent_belegen(…, nur geschlossene)`
- **Bericht:** je Kind gesetzt, unverändert, übersprungen (schon offen), ohne Inhalt, ZEITZONE FEHLT
- wiederholbar: ein zweiter Lauf setzt 0

## 8. Einspielen (Projektleiter, nach Freigabe des Nutzers)

### Vorher lesend bestätigen (echte Datenbank)

1. **Zeitzonen der Kinder:**
   ```sql
   select id, ist_test, zeitzone, now() at time zone zeitzone from schule.lernender where aktiv order by id;
   ```
   Beide Kinder und das Testkind brauchen ihre aktuelle australische Zeitzone, z. B. `Australia/Melbourne` oder `Australia/Adelaide`. Der Probe-Bericht nennt fehlende Zeitzonen vorn unter BEFUNDE.
2. **Prüfregel:**
   ```sql
   select pg_get_constraintdef(oid) from pg_constraint where conname = 'sterne_grund_check';
   ```
   Erwartet ist genau `… 'flug_abgelegt'::text, 'landung'::text])))` (Stand nach FP-S), sonst bricht das Paket ab.
3. **Bestandsfunktionen:** Der Probe-Bericht vergleicht `md5(prosrc)` mit dem Repo-Stand und meldet Abweichungen unter BEFUNDE (nur als Hinweis).
   - `schule.zugriff` `f99e88b5fd488d8d51d2d3e3bc562d24`
   - `schule.sieht` `1482384a60fdc66c83589429ae34a84c`
   - `schule.ist_eltern` `f98748d5c603e5b80a46417d2278f91e`
   - `schule.ist_lern` `6ae7797d89a581d2707b6e7c5311de86`
   - `schule.lern_ich` `87caa4fa1f41b887f077fd2a61ff011b`
   - `schule.wer_tn` `b2aeaeba4d4b9fd46a3d11482605aff7`

   Die genauen Werte stehen in `tools/tests/advent_pakete.py → bestand_md5()` und im Probe-Paket.
4. **Landungen:** Der Probe-Bericht zeigt „Landungen erkannt X von Y“. Y sind gelandete Etappen mit `landung_art`, X die mit `landung.am = sitzt_am`.
   - X darf kleiner sein: Setzungen nach einer eigenen Landung zählen nicht.
   - **X = 0 bei Y > 0 heißt STOPP**, denn dann gilt die Annahme aus Abschnitt 2 live nicht.

### Ablauf

1. `tools/tests/aus/advent_s_probe.sql` in **einem** Aufruf ausführen.
   - Erwartet ist der Fehler „ADVENT-S PROBELAUF bestanden, ALLES zurückgerollt …“.
   - Vorn steht KURZ, danach BEFUNDE, dann DETAILS.
2. `tools/tests/aus/advent_s_einspielen.sql` in **einem** Aufruf ausführen. Erwartet: kein Fehler. Ein zweiter Lauf ändert nichts.
   - Bricht es mit „lock timeout“ ab (laufende Lern-Transaktion auf `schule.sterne`), ist nichts geändert; einfach wiederholen.
3. Belegung: Werkzeug außerhalb des Repos, dann Probe, dann Einspielen.
4. Edge Function `lernen-api` 0.10.0 ausliefern (Deployment durch den Projektleiter).
5. `update schule.regel set wert = '2' where schluessel = 'advent_aktiv';` (nur Testkind), dann die Nachkontrolle.
6. Wenn die App live ist: `… wert = '1' …`. Tausch bei Bedarf mit `update schule.regel set wert = '1' where schluessel = 'advent_tausch';`.

**Lernpause: nicht nötig.**
- Es entstehen nur neue Tabellen und Funktionen, ohne Fremdschlüssel auf Bestandstabellen und ohne Trigger.
- Bestehende Funktionen und Daten werden nicht geändert.
- Einzige Sperre: Die Prüfregel von `schule.sterne` wird als letzter Schritt ersetzt. Die kurze ACCESS-EXCLUSIVE-Sperre hält bis zum Ende der Transaktion (Millisekunden).
- `lock_timeout` 3 s verhindert langes Warten. Im ungünstigsten Fall bricht das Paket ab und wird wiederholt.
- Beim Schalter `0` ändert das Einspielen für die Kinder nichts.

## 9. Tausch: Standard AUS – warum

- Er greift als einzige Aktion in die Gutscheine **eines anderen Kindes** ein.
- Er ist im Nachbau mit Sperren, Verboten und Gleichzeitigkeit geprüft. Am Testkind ist er live aber **nicht** nachprüfbar, denn das Testkind hat kein Geschwister.
- Deshalb kommt er nach der Nachkontrolle der übrigen Teile, mit einem bewussten `advent_tausch = 1`.

## 10. Nachkontrolle am Testkind (lernender 3, echte App, `advent_aktiv = 2`)

1. Eltern-Seite: Belegung für das Testkind setzen, Türen 1–4 z. B. Bild + 50 ★, Gutschein, Krampus, Sterne-Jackpot. `belegung_lesen` zeigt sie.
2. Als Testkind vor einer Etappe:
   - `stand.braucht_etappe = true`
   - die Kalendertür hat **keinen** Inhalt; im Netzwerk-Mitschnitt kein Titel und kein Text geschlossener Türen
3. Eine Etappe landen:
   - Die Tür erscheint nach der Landung; Tippen öffnet Tür 1 (älteste).
   - Sterne-Chip +50, im Konto genau einmal.
   - Ein zweiter Tipp oder ein zweites Gerät öffnet nichts Neues.
4. Sofort noch einmal öffnen (ohne Etappe): still weiter.
   - Zweite Etappe → Tür 2.
   - Dritte Etappe → `limit` (Hinweiszeile „2 Türchen heute offen …“).
5. Eine wieder offene Etappe nachbessern („Sitzt wieder!“) → am nächsten Tag öffnet sie ein Türchen.
6. „Meine Gutscheine“:
   - Gutschein selbst einlösen → grau.
   - Eltern sehen „kind:…“ mit Uhrzeit und holen zurück → wieder offen.
   - Krampus beim Kind ohne Knopf; Eltern setzen Erledigt / Noch nicht.
7. Prüfen in der Datenbank:
   ```sql
   select grund, bezug, menge from schule.sterne where lernender_id = 3 and grund = 'advent';
   ```
   Je geöffneter Tür mit Sternen genau eine Zeile.
8. Ein echtes Kind (Schalter 2) sieht „nicht aktiv“: Menü und Hinweiszeile fehlen.

## 11. Edge Function

`supabase/functions/lernen-api/index.ts` ist **vorbereitet, nicht ausgeliefert**.
- `VERSION` 0.10.0
- 11 Einträge in `AKTIONEN`, Hinweise für `belegung_setzen` und `gutschein_eltern` in `HINWEISE`

Sonst ändert sich nichts, denn die Aktionen laufen wie alle als `council_mcp` über `api.schule_advent_*`. Ohne diese Einträge antwortet die Funktion „Unbekannte Aktion“. Ausliefern erst nach dem Einspielen von ADVENT-S; 0.9.6 kommt dabei mit.

## 12. Nur als Attrappe geprüft (lokaler Nachbau)

- Landung und „Sitzt wieder!“: Zeilen in `schule.karte_stand` werden so nachgestellt, wie `karte_buchen`/`landung_speichern` sie live schreiben. Die echte Landelogik lief im Test nicht.
- `schule.sterne` ist vereinfacht (gleiche Prüfregel, gleicher eindeutiger Schlüssel). Konto und Sterne-Chip sind nicht geprüft.
- Die Uhr `schule.advent_jetzt()` ist im Nachbau ersetzt; live ist sie `now()`.
- Council-Zugänge (App-Schlüssel) gibt es im Nachbau nicht; geprüft sind die Lern-Sitzungen von Eltern, Kind und Lehrer.
- Lokales PostgreSQL 16 (live 17), geprüft ohne ICU sowie mit ICU en-US und de-DE.
