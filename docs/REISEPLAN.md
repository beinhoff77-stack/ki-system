# Reiseplan – Handbuch für Änderungen (Claude & ChatGPT)

Stand: 07.11.2026, App 0.47.2. Verbindliche Anleitung, **was wo angelegt wird**, wenn Sebastian am Reiseplan etwas ändern lässt.
Vor jeder Änderung: Werkstatt-Ablauf W1–W7 (Wunsch → `werkstatt_sperre` → Änderung → `werkstatt_aenderung` → erledigt). Keine Schlüssel/Stammdaten in Nachrichten (W7). Nichts live ohne Sebastians „Live“.

## 1. Grundsätze

- Im Reiseplan steht **nur tatsächlich Gebuchtes** (Quelle: Buchungsmails im Gmail-Konto hofftour@). Pläne/Ideen nur mit `status = 'geplant'`.
- Preise immer in **Euro**; Fremdwährung wird automatisch zum Kurs umgerechnet (siehe 4). Unterkünfte: Gesamt + Ø pro Nacht.
- Schätzpreise (z. B. Mietwagen ohne Beleg, RTW) mit `preis_ca = true` → App zeigt „ca.“.
- In jede Notiz: Buchungscode, was bezahlt ist, Storno, **Link zur Bestätigungsmail**. Offene Punkte ausdrücklich als „offen“ markieren.
- Keine Doppelten: vor dem Anlegen prüfen (Buchungscode / Datum / Name).

## 2. Datenmodell (Supabase, Schema `unterkunft`)

| Was | Tabelle | Wie anlegen |
|---|---|---|
| Reise (z. B. „Weltreise“, id 1) | `reise` | `api.unterkunft_reise_speichern` |
| **Unterkunft** (Hotel, Airbnb …) | `etappe` mit `status='gebucht'` + `buchung` (jsonb) | `api.unterkunft_etappe_speichern` (App: „Buchung nachtragen“) |
| **Flug, Mietwagen, Zug, Fähre, Ticket** | `reise_posten` | derzeit **nur per SQL** (keine API-Funktion, kein Council-Befehl) |
| Fotos zum Aufenthalt (max. 3) | Storage-Bucket `aufenthalt-fotos` | nur über die App (Upload verkleinert auf 1200 px, JPEG 0,72) |

Lesen für die App: `api.unterkunft_etappen_lesen` → liefert `reisen`, `etappen`, `luecken`, `posten`.

### 2a. Unterkunft (`etappe`)

Pflicht: `reise_id`, `ziel` (Ort, z. B. „Kyoto“), `anreise`, `abreise` (date, Abreise > Anreise), `status='gebucht'`.
`buchung` (jsonb), Felder:

```
name, anbieter (Airbnb/Booking/Agoda…), link (Inserat), zimmer,
preis_original, waehrung, preis_gesamt_eur (wird berechnet),
storno_kostenlos_bis | storno_text, gebucht_am, notiz,
land  ← z. B. "Japan" (steuert Länder-Abschnitt + Flagge)
```

Achtung `land`: `unterkunft.buchung_bauen` übernimmt `land` **noch nicht** (Migration offen, braucht Sebastians Okay). Wird über die API gespeichert, danach `land` per SQL nachsetzen:
`update unterkunft.etappe set buchung = buchung || '{"land":"Japan"}' where id = …;`
Ohne `land` nutzt die App `ziel` als Land → eigener Abschnitt pro Stadt (unschön).
Ländernamen deutsch ausschreiben (z. B. „Japan“, „Australien“, „Vereinigte Arabische Emirate“); die Flagge kommt aus der Liste `TRIP_LAND_ISO` in `stay-trips.js` (Europa, Naher Osten, Afrika, Asien, Ozeanien, Amerika). Fehlt ein Land dort, erscheint keine Flagge → in der Liste ergänzen.

### 2b. Flüge / Transport (`reise_posten`)

Spalten: `reise_id`, `art` (`flug|mietwagen|zug|faehre|tauchen|sonstiges`), `status` (`gebucht|geplant`), `titel`, `anbieter`, `buchungscode`, `preis_original`, `waehrung`, `preis_ca`, `kurs_datum` (optional), `segmente` (jsonb-Array), `link`, `notiz`.
**Ein Posten = eine Buchung** (ein Preis), Segmente = einzelne Flüge/Abschnitte. Preis steht nur einmal am Posten.

Flug-Segment (Zeiten = **Ortszeit**, Format `YYYY-MM-DDTHH:MM`):
```json
{"nr":"JL 773","airline":"Japan Airlines","von":"NRT","von_name":"Tokio","von_land":"Japan",
 "ab":"2026-11-10T17:40","nach":"MEL","nach_name":"Melbourne","nach_land":"Australien",
 "an":"2026-11-11T05:40","klasse":"Business","sitze":"07H, 07C"}
```
Mietwagen-/Transport-Segment (ohne Uhrzeit nur Datum `YYYY-MM-DD` → App zeigt „bis TT.MM. · N Tage“):
```json
{"ab":"2026-10-27","an":"2026-11-10","ort":"Tokio","land":"Japan","fahrzeug":"…","vermieter":"…"}
```
`land` bzw. `von_land`/`nach_land` immer setzen (Abschnitte/Flaggen).

Beispiel:
```sql
insert into unterkunft.reise_posten (reise_id, art, status, titel, anbieter, buchungscode,
  preis_original, waehrung, preis_ca, segmente, notiz)
values (1,'flug','gebucht','Qantas Sydney – Auckland','Qantas','ABC123',1234.50,'AUD',false,
  '[{"nr":"QF 143","airline":"Qantas","von":"SYD","von_name":"Sydney","von_land":"Australien",
     "ab":"2027-01-05T09:00","nach":"AKL","nach_name":"Auckland","nach_land":"Neuseeland",
     "an":"2027-01-05T14:00","klasse":"Economy"}]'::jsonb,
  '4 Personen. Bestätigung: <Gmail-Link>');
```
Ändern: `update … set …` (Trigger rechnet neu). Löschen: `set geloescht_am = now()` (nicht hart löschen).

### 2c. Tauchen (`reise_posten`, `art = 'tauchen'`, seit W140)

**Ein Posten = ein Tauchtag bei einem Anbieter** (ein Preis), genau ein Segment. Preis in Originalwährung (`JPY` usw.), `preis_ca = true` bei Hochrechnung aus Angebot; Euro rechnet der Trigger.
Pflicht: `taucher` (Vornamen, wer getaucht ist), `tauchgaenge`, `gebiet` (genaues Tauchgebiet; unbekannt → nur `ort`). Log-Werte aus dem Tauchcomputer (UDDF) je Tauchgang in `tg`.
```json
{"ab":"2026-10-05T09:19","an":"2026-10-05T11:21","ort":"Ishigaki","land":"Japan",
 "gebiet":"Westküste vor der Sakieda-Halbinsel","taucher":["Sebastian","Kerstin","Leo","Rosa"],
 "tauchgaenge":2,"modus":"Gerät (Luft)",
 "tg":[{"nr":1,"start":"09:19","dauer_min":44,"max_tiefe_m":16.7,"temp_c":28.2,"lat":24.4196,"lon":124.0791,"gebiet":"vor Sakieda"}]}
```
UDDF-Hinweise: Temperatur steht in Kelvin (− 273,15), Tiefe in m, Dauer in s. Zeitstempel sind Ortszeit (Oceanic-Export schreibt fälschlich `+00:09`). `divemode apnoe` = Computer falsch eingestellt → nur Maximaltiefe, Dauer ungenau, im `modus` vermerken. Gebiet aus GPS ableiten und in der Notiz als „nicht vom Anbieter bestätigt“ kennzeichnen.
App: eigene Farbe (petrol), Filter „Tauchen“ (nur wenn vorhanden), Summe „Tauchen“ in der Gesamtzeile, Details mit Kartenlink je Tauchgang.

### 2d. Nebenkosten vor Ort (`reise_ausgabe`, seit W142)

Kreditkartenbuchungen (Wio, alle Karten) ab Reisebeginn, **eine Zeile je Buchung** – Quelle sind die Monatsabrechnungen (PDF). Felder: `datum`, `anbieter` (bereinigter Name), `text_original`, `karte_endung`, `waehrung_karte`, `betrag_aed`, `betrag_eur` (Tageskurs AED→EUR aus `wechselkurs`), `gebuehr_eur` (2 % Auslandseinsatzgebühr), `land`, `quelle_ref` (`wio:<n>`, eindeutig).
- `status`: `reise` = Nebenkosten (zählt), `privat` = nicht zählen, `plan` = steckt schon in `etappe`/`reise_posten` (nie doppelt zählen).
- `kategorie`: `essen` (Restaurants, Supermarkt, Konbini, Lieferdienst), `erleben` (Aktivitäten, Eintritte, Onsen, Massage), `unterwegs` (Taxi/Uber/Careem, Tanken, Parken, Flug-Nebenkosten), `sonst` (Shopping, Telefon/eSIM, Apps, Apotheke, Unklares).
- Regeln je Anbieter hat Sebastian in der Seite „Reisekasse Weltreise“ gesetzt (privat u. a.: KI-Abos, Apple, Behörden Dubai, Etisalat/du, Noon, Spas Dubai, Hoka). Neue Abrechnung: gleiche Regeln anwenden, nur neue Anbieter fragen.
- Gebühr zählt bei `status <> 'privat'` unter Sonstiges (auch für Plan-Buchungen).
- Plan-Buchungen auf der Karte: Plan-Wert = Kartenbetrag ohne Gebühr (Etappen: `waehrung` AED, `preis_buchung` = Originalpreis).
- `unterkunft.nebenkosten_json(reise)` fasst je Monat zusammen; `api.unterkunft_etappen_lesen` liefert sie als `nebenkosten`. App: Zeile „Nebenkosten <Monat>“ am Monatsende (rosé, Filter „Nebenkosten“), Summe in der Gesamtzeile.

## 3. Bestand Weltreise (reise_id 1), Stand 07.11.2026

Posten: 1 Emirates IDN6RJ · 2 Tigerair W75GXP · 3 Klook-Mietwagen Ishigaki · 4 oneworld-RTW YNGQBK (11 Flüge, ca. 24.490 €) · 5 ANA NH 90 · 6 Mietwagen Japan-Rundreise 27.10.–10.11. (ca. 1.200 €) · 7–10 Tauchtage Ishigaki 02./03./05./13.10. (Euro Divers, 3× Aqua-no-jikan; je 2 TG, alle 4; ca. 1.992 €).
Unterkünfte gebucht bis 09.11.2026 (Kyoto). Danach Lücken – die App zeigt sie automatisch mit „Suchen“.
Offen (Sebastian liefert): Emirates-Sitzplatzpreis, ob Mondial-Servicegebühr in 24.490 € enthalten, Kinderaufschlag Taipei.

## 4. Automatik – nichts davon von Hand machen

- **Euro-Umrechnung:** Trigger `buchung_umrechnen` (etappe) und `posten_umrechnen` (reise_posten). Kurs = Tag der Leistung bzw. heute; fehlt der Kurs, holt der Cron-Job `unterkunft-kurse` (jede Minute, `unterkunft.kurse_takt()`) ihn und rechnet nach.
- **Lücken** (Nächte ohne Unterkunft) berechnet die App aus Unterkünften + Flügen; nicht als Datensatz anlegen.
- **Gesamtausgaben, Tag x von y, Zähler** berechnet die App.

## 5. App-Code (Repo beinhoff77-stack/ki-system)

- Reiseplan-Ansicht: `stay-trips.js` (`viewReisen`, `segRow`, `gapRow`, `row`); Fotos: `stay-photos.js`; Stil: `style.css` (Klassen `.rp-*`).
- Abschnitte je Land (aktueller + nächste 4 Wochen offen), Filter Hotel/Flug/Transport/Tauchen, Farben: Flug blau, Transport orange, Tauchen petrol (`diveRow`).
- Jede Version: `APP_VERSION` in `app.js`, `?v=` in `index.html`/`sw.js`, Cache `vNN` in `sw.js`, Tests in `tests/search.test.cjs` mitziehen. `npm test`; danach `git checkout -- docs/previews`.
- PR auf `main`, Merge erst nach Sebastians „Live“.
