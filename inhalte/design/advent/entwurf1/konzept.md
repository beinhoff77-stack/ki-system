# Adventskalender mit echten Türchen – technisches Konzept (Entwurf 1)

Stand 28.11.2026 · Designer-Helfer · **kein App-Code, keine Migration, nichts eingespielt.**
Entwurf: `index.html` (eine Datei, ohne Netz, Schalter unten rechts bzw. per Adresse). Bilder: `bilder/`. Wo es in der App eingehängt wird: `umsetzung1.md`.
Die Weihnachts-Ebene auf der Reisekarte ist ein **eigener Teil** (Abschnitt 11) und lässt sich unabhängig vom Kalender bauen und live schalten.

Berücksichtigte Vorgaben des Nutzers (28.11.):
- Eine Etappe geschafft → ein Türchen. Nachholen ist erlaubt, höchstens 2 am Tag; für das zweite braucht es eine zweite Etappe. Das älteste geschlossene Türchen kommt zuerst. Künftige Türchen bleiben zu.
- Ein gemeinsamer Vorrat, je Kind eine eigene Reihenfolge, je Kind änderbar.
- **Keine eigenen Fotos**: Bild-Türchen sind gezeichnete Motive plus ein Satz der Eltern.
- Gutscheine liegen in der App des Kindes und werden ausgeschaltet, wenn sie eingelöst sind.
- Sterne je Türchen: 0–5000, in Zehnerschritten.

---

## 1. Kurzfassung

- **Kind:** Nach der bestehenden Landungs-Ansicht erscheint vor dem nächsten Schritt eine **Tür mit Tageszahl**. Das Kind tippt sie auf und sieht den Inhalt:
  - ein Motiv mit Satz,
  - eine Gutschein-Karte,
  - nur Sterne,
  - oder „nur Licht“, wenn der Platz leer ist.

  Danach führt derselbe große Knopf weiter, der vorher da war.
- **Kalender:** Ein Kalender mit 24 Türen ist erreichbar über das Menü und über eine Zeile in der Karte „Gerade dran“. Die Weltkarte selbst bleibt unverändert.
- **Gutscheine:** „Meine Gutscheine“ ist eine eigene Seite. Ein Gutschein ist offen, angefragt, „heute nicht“ oder eingelöst. Eingelöste werden grau und rutschen nach unten.
- **Eltern:** Die Seite „Adventskalender“ ist von der Lehrer-Startseite aus erreichbar. Füllen geht so:
  1. Ideen antippen.
  2. Die App mischt für jedes Kind.
  3. Einzelne Türen per Antippen ändern (Text, Sterne, für wen).

  Angefragte Gutscheine stehen zusätzlich als Zeile in „Zu tun“ mit den Knöpfen „Eingelöst“ und „Heute nicht“.
- **Server entscheidet alles:**
  - ob heute eine Etappe geschafft ist,
  - wie viele Türchen heute schon offen sind,
  - welches das älteste geschlossene ist.

  Der Inhalt eines geschlossenen Türchens erreicht das Gerät des Kindes nie.
- **Empfehlung für den 1.12.:** Stufe 1a, das heißt Türchen, Kalender, Eltern-Füllen, Sterne und eine Gutschein-Liste. Die Eltern schalten Gutscheine auf ihrer Seite aus. Die **Einlösen-Anfrage des Kindes kommt als Stufe 1b**, wenige Tage später. Geht es erst am 3.12. live, holen die Kinder die verpassten Türchen innerhalb von 1–2 Tagen nach (Abschnitt 9).

---

## 2. Was die App heute schon hat (gelesen, nicht geändert)

| Baustein | Fundstelle | Nutzen für den Kalender |
|---|---|---|
| Landung einer Etappe: `r.karte.neu_sitzt` und `r.landung` (`landung_art` direkt/sauber/sturm) aus `schule_uebung_pruefen` | `lernen.js` ab Z. 4570 (`jetztSitzt`), Z. 4622–4653; Server `schule.landung_zaehlen` / `landung_speichern` in `20261120_ab_s_abschluss.sql` | **Auslöser.** Eine eigene Landung schreibt `schule.karte_stand.landung_art` und `sitzt_am`. Gesetzte Landungen (LB-3) haben `landung_art = null` und zählen nicht. |
| Ablauf nach der Landung: Knobel-Bordkarte (außer Sturm) → `zeigeLandung()` → Abschluss-Ansicht `lernAbschlussEtappe` mit **einem** großen Knopf (nächste Etappe / Flug-Test / Abflug) | `lernen.js` Z. 4628–4653, 4076–4121 | Die Tür hängt sich an diesen Knopf, nach dem Muster der Expedition (`lernExVorKnopf`, Z. 618 ff.). Ablauf, Knobel und Test bleiben unverändert. |
| Vollbild-Hülle `lernAbschlussZeigen` / `lernAbschlussZu`, „weniger Bewegung“ `lernWenigBewegung` | Z. 4040–4060 | Hülle und Stil für die Tür-Ansicht (Szene oben, Blatt unten). |
| Tag des Kindes `schule.heute_tag(p_l)` = heutiges Datum in `lernender.zeitzone` (Rückfall Europe/Berlin) | `20261120_i2_lernregeln.sql` Z. 176 | **Kalendertag**, Nachhol- und Tageslimit. |
| Sterne-Buchung `insert into schule.sterne(lernender_id, menge, grund, bezug)`, eindeutig je `(lernender_id, grund, bezug)`, `on conflict do nothing` | z. B. `20261125_ex_s_expedition.sql` Z. 135–138; Prüfregel `sterne_grund_check` zuletzt in `20261122_fp_s_faire_punkte.sql` Z. 36–46 | Weg für „+n Sterne“ (Abschnitt 5). |
| Rechte `schule.ist_eltern(schluessel)`, `schule.zugriff(schluessel, lernender)` | `20261114_w150_lern_zugaenge_plan.sql` Z. 68–95 | Eltern-Aktionen und Kind-Aktionen. |
| Belohnungen/Einlösungen `schule_eltern.einloesungen`, `schule_einloesung_entscheiden` (bestätigt/abgelehnt, „abgelehnt gibt die Sterne zurück“) | Tabellen aus der Grundanlage (nicht im Zweig); App Z. 1095–1130, 1734, 2901 | **Nicht wiederverwenden**, sondern nur die Optik der „Zu tun“-Zeile (Abschnitt 6). |
| „Zu tun“-Zeilen mit Knöpfen `lernZuTun(…, wuensche, …)` | Z. 1261–1276 | Zeile „Kind 1 möchte … einlösen“ |
| Foto-Ablage | `stay-photos.js` (Unterkunft, Haupt-App); Entwurf `20261130_ma_s_materialablage.sql` liegt nur beim Projektleiter | **Wird nicht gebraucht**, weil es keine Fotos gibt. |

---

## 3. Datenmodell (neu, nur Zusätze)

Alle Tabellen liegen in `schule`, mit RLS an und ohne direkten Zugriff. Gelesen und geschrieben wird nur über `api.schule_advent_*` (security definer), wie bei den anderen `schule_…`-Funktionen.

```
schule.advent_inhalt          -- Vorrat (gemeinsam), auch Zusatz-Inhalte für nur ein Kind
  id bigserial pk
  jahr smallint not null default 2026
  art text not null check (art in ('gutschein','motiv','sterne'))
  titel text not null check (char_length(titel) <= 80)
  text text check (char_length(text) <= 140)          -- Satz fürs Kind
  motiv text                                           -- id aus dem Motiv-Vorrat der App (Pflicht bei art='motiv')
  sterne int not null default 0 check (sterne between 0 and 5000 and sterne % 10 = 0)
  nur_fuer bigint references schule.lernender(id)      -- null = beide
  idee text                                            -- Schlüssel der Idee, aus der er entstand (Startvorrat)
  von_hand boolean not null default false              -- Idee mit Lern-Wirkung (Joker …): reiner Gutschein, Eltern lösen von Hand ein
  aktiv boolean not null default true
  angelegt_am / geaendert_am timestamptz

schule.advent_platz           -- Reihenfolge je Kind
  lernender_id bigint, jahr smallint, nr smallint check (nr between 1 and 24)
  inhalt_id bigint null references schule.advent_inhalt(id)   -- null = leer („nur Licht“)
  geaendert_am timestamptz
  primary key (lernender_id, jahr, nr)

schule.advent_tuer            -- geöffnete Türchen (Ereignis + Schnappschuss)
  id bigserial pk
  lernender_id, jahr, nr
  geoeffnet_am timestamptz not null default now()
  tag date not null                                   -- schule.heute_tag(lernender) beim Öffnen
  inhalt_id bigint null
  inhalt jsonb not null                               -- Schnappschuss {art,titel,text,motiv,sterne}; spätere Änderungen am Vorrat ändern Geöffnetes nicht
  client_id text                                      -- Wiederholung desselben Tipps = dieselbe Antwort
  zurueckgenommen_am timestamptz, zurueckgenommen_von text
  unique (lernender_id, jahr, nr) where zurueckgenommen_am is null
  unique (lernender_id, client_id)

schule.advent_gutschein       -- nur für art='gutschein'
  id bigserial pk
  tuer_id bigint unique not null references schule.advent_tuer(id)
  lernender_id bigint not null
  titel text, text text                               -- Kopie aus dem Schnappschuss
  zustand text not null default 'offen' check (zustand in ('offen','angefragt','spaeter','eingeloest'))
  angefragt_am, entschieden_am timestamptz, entschieden_von text
  eingeloest_am timestamptz
  gueltig_bis date                                    -- Stufe 2; null = gilt, bis eingelöst (kein Verfall)
  geaendert_am timestamptz
```

Notizen zum Modell:
- Die **Ideenliste (95 Vorschläge, elf Gruppen)** ist App-Datenmaterial, z. B. `daten/advent-ideen.json` mit Schlüssel, Gruppe, Titel, Text, Vorschlags-Sterne und Kennzeichen `von_hand`. „Übernehmen“ schreibt die gewählten Ideen als normale Einträge in `advent_inhalt`. Im Zweig liegt die Liste noch nicht; der Entwurf zeigt einen Auszug.
- **Motive:** Es gibt 16 Motive, die gezeichnet sind und in der App liegen (`MOTIVE` im Entwurf, später etwa `daten/advent-motive.js`). 6 sind ausgearbeitet, 10 sind Skizzen. Der Server speichert nur die Motiv-id. Damit gibt es keine Bildablage und kein Datenschutzproblem.
- „**Gleiche Inhalte, andere Tage**“: Kind 1 bekommt einen Zufall, Kind 2 dieselbe Folge, um 3–8 Tage versetzt. Tür 24 ist bei beiden fest („Hinweis auf den 24.“). Das Mischen passiert auf dem Gerät der Eltern; gespeichert wird die fertige Liste mit `schule_advent_belegen`.

---

## 4. Rechte

| Wer | darf | darf nicht |
|---|---|---|
| **Kind** (Lern-Sitzung, Rolle kind, nur eigenes `lernender_id`) | Stand lesen (ohne Inhalt geschlossener Türen) · ein Türchen öffnen (Server wählt welches) · geöffnete Türchen und eigene Gutscheine lesen · Gutschein anfragen (Stufe 1b) | Vorrat oder Belegung lesen · eine bestimmte Tür wählen · Gutschein-Zustände außer „angefragt“ setzen |
| **Eltern** (`schule.ist_eltern`) | alles lesen (Vorschau) · Vorrat und Belegung schreiben · Gutschein „eingelöst / heute nicht / zurückholen“ · Türchen zurücknehmen | ein Türchen für ein **echtes** Kind öffnen (nur fürs Testkind), damit beim Nachsehen nichts aus Versehen aufgeht |
| Gerät | nichts entscheiden | Datum, Zählen, Limit (nur Anzeige) |

**Der Inhalt geschlossener Türchen verlässt den Server nicht zum Kind:**
- `schule_advent_stand` liefert für geschlossene Türen nur `nr` und `zustand`.
- Inhalt kommt nur aus `schule_advent_oeffnen` (genau das eine, eben geöffnete Türchen) und aus `schule_advent_tuer_lesen` (nur geöffnete).
- `schule_advent_lesen` (mit Vorrat) prüft `ist_eltern`.
- Die Vorschau der Eltern („so sieht es Kind 1“) baut die App aus den Eltern-Daten. Sie ruft dafür nicht `oeffnen` auf.

---

## 5. API-Aktionen (Muster `schule_…`, lernen-api `AKTIONEN` + `api.schule_advent_*`)

| Aktion | Parameter | Wer | Ergebnis |
|---|---|---|---|
| `schule_advent_stand` | `lernender_id` | Kind/Eltern | `{ aktiv, jahr, heute, tag_nr, etappen_heute, offen_heute, frei_heute, naechste_nr, nachholen_bis, tueren:[{nr, zustand, art?, titel?, motiv?}], gutscheine:{offen, angefragt} }` – `zustand` ∈ offen · bereit · nachholen · heute · morgen · zu; art/titel/motiv **nur bei offen** |
| `schule_advent_oeffnen` | `lernender_id, client_id` | Kind (Eltern nur Testkind) | `{ nr, nachgeholt, art, titel, text, motiv, sterne, sterne_gutgeschrieben, gutschein_id?, leer, frei_heute, naechste_nr }` oder Fehler „Heute schon 2 Türchen“ / „Erst nach deiner nächsten Etappe“ / „Alles offen“ |
| `schule_advent_tuer_lesen` | `lernender_id, nr` | Kind/Eltern | Schnappschuss eines **geöffneten** Türchens |
| `schule_advent_gutscheine` | `lernender_id` | Kind/Eltern | Liste: offen/spaeter zuerst, dann angefragt, eingelöst am Ende |
| `schule_advent_gutschein_anfragen` *(1b)* | `lernender_id, gutschein_id` | Kind | Zustand `angefragt` (wiederholbar ohne Wirkung) |
| `schule_advent_lesen` | – | Eltern | Vorrat, Belegung je Kind, Türen je Kind (mit Inhalt), Gutscheine, Anfragen |
| `schule_advent_inhalt_setzen` | `{id?, art, titel, text, motiv?, sterne?, nur_fuer?, aktiv?}` oder `eintraege:[…]` | Eltern | id(s) |
| `schule_advent_belegen` | `lernender_id, plaetze:[{nr, inhalt_id\|null}], revision?` | Eltern | neue `revision`; **geöffnete Plätze bleiben**, Änderung daran wird abgewiesen |
| `schule_advent_gutschein_entscheiden` | `gutschein_id, zustand: 'eingeloest'\|'spaeter'\|'offen'` | Eltern | „offen“ = Zurückholen eines versehentlich eingelösten Gutscheins |
| `schule_advent_tuer_zuruecknehmen` | `lernender_id, nr` | Eltern | Tür wieder zu (Abschnitt 8) |

**Prüfungen des Servers in `schule_advent_oeffnen`** (in einer Transaktion):

1. `pg_advisory_xact_lock(hashtext('advent:' || l))` – zwei Geräte gleichzeitig werden nacheinander bearbeitet.
2. Gab es diesen `client_id` schon, wird dieselbe Antwort zurückgegeben (Netz-Wiederholung).
3. `v_heute := schule.heute_tag(l)`. Aktiv ist der Kalender vom **1.12. bis `nachholen_bis`** (Vorschlag 31.12., siehe Frage 2). `tag_nr := least(extract(day), 24)` im Dezember.
4. Geschaffte Etappen heute:
   ```sql
   v_etappen := count(*) from schule.karte_stand k
     where k.lernender_id = l and k.landung_art is not null
       and (k.sitzt_am at time zone tz)::date = v_heute;
   ```
   Das zählt nur eigene Landungen (LB-3-Setzungen haben keine `landung_art`). Jede Etappe zählt höchstens einmal am Tag. „Wieder gelandet“ nach Nachbessern zählt mit, siehe Frage 3.
5. `v_offen_heute := count(*) from advent_tuer where lernender_id = l and tag = v_heute and zurueckgenommen_am is null`.
6. `if v_offen_heute >= least(2, v_etappen) then` Fehler („Erst nach deiner nächsten Etappe“ bzw. „Heute schon 2 Türchen“).
7. `v_nr := min(nr)` aus `1..tag_nr`, die noch nicht offen sind. Das ist das **älteste zuerst**; künftige bleiben zu.
8. Einfügen des Schnappschusses. Bei `art = 'gutschein'` dazu eine Zeile in `advent_gutschein`. Bei `sterne > 0`:
   ```sql
   insert into schule.sterne(lernender_id, menge, grund, bezug)
   values (l, v_sterne, 'advent', 'advent:' || jahr || ':' || v_nr)
   on conflict do nothing;
   ```

**Sterne:** Dafür kommt ein neuer Grund `'advent'` in `sterne_grund_check`. Das Ersetzen der Prüfregel ist dasselbe Muster wie bei FP-S und WD-S: die bisherige Definition genau prüfen, sonst abbrechen. Sterne werden **sofort beim Öffnen** gutgeschrieben, die Sterne-Regeln bleiben unberührt. Wird das Ersetzen der Prüfregel nicht gewünscht, ist der Rückfall `grund = 'korrektur_hand'` mit `bezug = 'advent:…'`.

---

## 6. Gutscheine einlösen

**Standard A (Vorschlag Projektleiter, empfohlen):**
1. Das Kind tippt „Einlösen“. Der Gutschein steht dann auf **angefragt**.
2. Bei den Eltern erscheint in „Zu tun“ eine blaue Zeile „Kind 1 möchte ‚Frühstück ans Bett‘ einlösen“ mit den Knöpfen **Eingelöst | Heute nicht**.
3. „Heute nicht“ setzt den Gutschein auf `spaeter`. Er bleibt einlösbar, und das Kind sieht „Heute nicht – ein andermal“.
4. Zusätzlich gibt es auf der Eltern-Seite „Als eingelöst markieren“ (wenn es mündlich lief) und „Zurückholen“ (versehentlich Eingelöstes wird wieder offen).

Warum nicht `schule_einloesung_entscheiden` wiederverwenden?
- Eine Einlösung hängt an einer **Belohnung** aus dem Katalog und an **Sterne-Kosten**. „Abgelehnt“ bucht Sterne zurück.
- Ein Gutschein hat keinen Preis und keinen Katalog-Eintrag. Eine Wiederverwendung würde den ausgeblendeten Belohnungs-Katalog über die Hintertür wieder sichtbar machen (Reisepass-Verlauf, `schule_eltern`).
- Wiederverwendet wird nur die **Optik**: `lernZuTun(…, wuensche)` nimmt beliebige `{text, knoepfe}`. Die Daten kommen aus `schule_advent_lesen().anfragen`.
- `schule_eltern` bleibt unverändert. Die Lehrer-Startseite ruft `schule_advent_lesen` zusätzlich ab, nur vom 1.12. bis 31.1. Eine Erweiterung von `schule_eltern` um ein Feld spart einen Abruf, ändert aber eine bestehende Funktion. Für Stufe 1b wird die getrennte Abfrage empfohlen.

**Alternative B – nur die Eltern schalten aus (ohne Anfrage des Kindes):**

| | Vorteil | Nachteil |
|---|---|---|
| A Anfrage | Das Kind entscheidet, wann. Die Eltern sehen es sofort in „Zu tun“, und nichts wird vergessen. Fühlt sich an wie ein echtes Ticket. | Eine Aktion mehr (Server + App). Die Eltern müssen tippen, auch wenn es mündlich schon lief. |
| B nur Eltern | Kleiner (keine Anfrage, keine Zu-tun-Zeile). Passt, wenn ohnehin alles mündlich läuft. | Das Kind kann nur zeigen, nicht anfragen. Nicht ausgeschaltete Gutscheine bleiben offen stehen, was leicht zu Diskussionen führt. |

**Zwei Geräte bei Gutscheinen:**
- Jeder Zustandswechsel geht nur über den Server und gilt nur, wenn der erwartete Ausgangszustand stimmt (`update … where zustand in (…)`).
- „Einlösen“ zweimal hintereinander bleibt „angefragt“.
- Haben die Eltern schon „Eingelöst“ getippt, bekommt das zweite Gerät „schon eingelöst“ zurück und zeichnet den Gutschein neu.

**Kein Verfall:** Gutscheine gelten über den Advent hinaus, bis sie eingelöst sind. „Gültig bis“ ist ein optionales Feld (Stufe 2).

**Ideen mit Lern-Wirkung** („Lerntag mit halber Wiederholungsrunde“, „Joker: ein Lerntag frei“, „Doppelte Sterne für die nächste Etappe“):
- In Stufe 1 sind sie **reine Gutscheine** mit dem Kennzeichen `von_hand`. Die Eltern lösen sie von Hand ein; die Lernlogik bleibt unverändert.
- Eine echte Kopplung wäre nur ein Vorschlag für Stufe 2. Das Einlösen würde dann einen Eintrag schreiben, den die Lernlogik liest:
  - Joker → ein `schule.pause`-Tag (gibt es schon, `20261120_i_pause.sql`),
  - halbe Runde → `anzahl` in `schule_wiederholung`,
  - doppelte Sterne → ein Faktor in der Landungs-Buchung.

  Jede dieser Kopplungen greift in geprüfte Regeln ein und bräuchte eigene Rauchtests. Davon wird für den Advent abgeraten.

---

## 7. Zeitzone und Datum

- Maßgeblich ist der **Tag des Kindes** `schule.heute_tag(l)`, also das Datum in `lernender.zeitzone`. Damit beginnt der 1.12. in Australien, wenn er dort beginnt, und nicht nach der Gerätezeit.
- Das Gerät zeigt Datum und „morgen“ nur an. Die Kalenderseite lädt bei `visibilitychange` neu, damit nach Mitternacht nicht „heute“ von gestern stehen bleibt.
- **Prüfen vor dem 1.12.:** Steht `lernender.zeitzone` für beide Kinder auf der aktuellen Ortszeit (z. B. `Australia/Melbourne`)? Sonst rechnet der Server mit dem Rückfall `Europe/Berlin`.
- Ostern, Fasching und andere Saison-Effekte rechnen weiter wie in Vorgabe FX (Gerätedatum). Das betrifft den Kalender nicht.

---

## 8. Zwei Geräte, Rücknahme

**Zwei Geräte:**
- Durch die Sperre pro Kind und den eindeutigen Index pro `(lernender, jahr, nr)` kann nie ein Türchen doppelt aufgehen, und das Tageslimit kann nicht überschritten werden.
- Tippen beide Geräte fast gleichzeitig, bekommt das zweite „schon offen“ zurück und zeigt den Inhalt des geöffneten Türchens (`tuer_lesen`). Es entsteht also kein zweites Türchen.

**Rücknahme durch Eltern** (`schule_advent_tuer_zuruecknehmen`):
- setzt `zurueckgenommen_am` (kein Löschen),
- bucht die Sterne mit `bezug = 'advent:…:zurueck'` und negativer Menge zurück,
- setzt einen dazugehörigen Gutschein auf eingelöst-zurückgenommen (er verschwindet beim Kind).

Danach ist die Tür wieder „nachholen“. Zählt sie fürs Tageslimit? Nein, gezählt werden nur nicht zurückgenommene Öffnungen.

---

## 9. Stufen und Aufwand (ehrliche Schätzung, Arbeitsstunden eines Bau-Chats)

| Stufe | Inhalt | Server | App | Prüfung | Summe |
|---|---|---|---|---|---|
| **1a – zum 1.12.** | Tür nach der Etappe (Hülle wie Abschluss, tippen zum Öffnen, überspringbar, ruhige Fassung) · Kalender 24 Türen · Hinweiszeile in „Gerade dran“ + Menü · Eltern-Seite: Ideen übernehmen, mischen, Raster, Tür ändern (Text, Sterne, für wen) · Sterne beim Öffnen · **Gutschein-Liste des Kindes zum Ansehen** · Eltern: „als eingelöst markieren / zurückholen“ · 6 Motive · Ideenliste als Daten | 4 Tabellen, 8 Funktionen, `sterne_grund_check` + `'advent'`, lernen-api 0.10.0, Rauchtest: **5–7 h** | **8–10 h** | Nachbau im Testserver, Bilder 390/1280, Durchklick: **3 h** | **16–20 h** |
| **1b – 3.–5.12.** | Kind fragt an · Zeile in „Zu tun“ mit Eingelöst / Heute nicht · Zustand „heute nicht“ beim Kind | 2 Funktionen: **1–2 h** | **2–3 h** | **1 h** | **4–6 h** |
| **2 – Komfort** | 10 Skizzen-Motive ausarbeiten · „gültig bis“ · Ideenliste durchsuchen · Wiederansehen mit Wisch-Geste · optionale Kopplung der Lern-Ideen (Abschnitt 6) · Spezialeffekt „Adventskalender“ der Vorgabe FX als Öffnungs-Effekt | 2–3 h | 4–6 h | 2 h | 8–11 h |

**Realistisch bis 1.12.?**
- Heute ist Samstag, der 28.11. Stufe 1a passt nur, wenn der Bau am 29.11. beginnt und der Nutzer am 30.11. oder 1.12. ausdrücklich einspielen lässt.
- Dabei gilt: Server zuerst, App danach, Prüfung am Testkind.
- Knapp, aber machbar, weil keine Bildablage und kein Eingriff in die Lernlogik nötig sind.

**Wenn es erst am 3.12. live geht:**
- Am 3.12. sind die Türchen 1–3 fällig. Das Kind öffnet mit zwei Etappen 1 und 2.
- Am 4.12. sind 3 und 4 fällig; mit zwei Etappen öffnet es beide und ist **aufgeholt**.
- Das Nachholen deckt also bis zu etwa einer Woche Verspätung ab; je verspätetem Tag braucht es einen Tag mit zwei Etappen.
- Die Eltern füllen den Kalender ohnehin vorher. Die Eltern-Seite kann einen Tag vor den Kinder-Teilen live gehen.

**Notfall, falls der Server nicht rechtzeitig fertig ist:** Erst Kalender und Tür „ohne Inhalt“ zeigen, also nur die Tür mit Zahl und dem Satz „Hol dir dein Türchen bei Mama oder Papa ab“. Das geht ohne Server und ohne Inhalte auf dem Gerät. Es ist nur eine Brücke, das Tageslimit gilt dann nur je Gerät.

---

## 10. Was bewusst NICHT geändert wird

- Lernlogik, Sterne-Regeln, Landungs-Bonus, Knobel-Bordkarte, Flug-Test, Wiederholungen, Nachbessern-Ablauf.
- Die Abschluss-Ansicht der Etappe bleibt gleich (Text, Knöpfe, Sticker). Die Tür kommt **nach** ihr, beim Tipp auf den großen Knopf.
- Die Weltkarte bekommt keine Knöpfe und keine Leiste. Die Hinweiszeile sitzt **in der bestehenden Karte „Gerade dran“**, so wie heute `lr-dock-ansage` / `lernExtraLink`.
- Belohnungs-Katalog, `schule_eltern`, `schule_einloesung_entscheiden` bleiben unverändert und ausgeblendet.
- Keine Fotos, keine Bildablage, kein Speicher-Bucket. Der Entwurf `20261130_ma_s_materialablage.sql` (beim Projektleiter) wird dafür nicht gebraucht.
- Kein Effekt im Flug-Test, keine Tür in Eltern- und Lehreransicht (außer der Vorschau).

---

## 11. Weihnachts-Ebene auf der Reisekarte (1.–31.12., eigener Teil)

Die Vorgabe des Nutzers war: „Du kannst nur Grafiken drüber legen.“ Umsetzung:
- Eine Ebene (SVG + ein Canvas) liegt über `.rk-rahmen` mit `pointer-events: none`.
- Keine Knöpfe, keine Leiste. Pins, Routen, Ziehen, Zoomen und Doppeltipp bleiben unverändert.
- Die Ebene schaltet sich nach dem **Gerätedatum** (Ortszeit) ein und am 1.1. wieder aus.
- Server und Daten werden nicht angefasst.

| | Variante 1 „dezent“ | Variante 2 „verspielt“ | Variante 3 „Neon-Nordlicht“ |
|---|---|---|---|
| Was | Lichterkette am oberen Kartenrand (zwischen Regel-Universum-Sonne und Zoom-Knöpfen), Mütze auf dem Pin des aktuellen Landes, leichter Schnee (26 Flocken, Canvas) | Mützen auf besuchten Pins und dem aktuellen, kleine Geschenke an gelandeten Ländern, Eiskristalle in der freien Ecke unten rechts, Schlitten mit zwei Rentieren fliegt alle ~25 s einmal 5 s entlang der Flugroute | Polarlicht am Nordrand (links zur Sonne hin ausgeblendet), Neon-Stern mit Lichtstrahl über dem aktuellen Ziel, sechs Funkelsterne im Polarlicht |
| Bewegung | Lampen funkeln langsam (opacity, 3,2 s), Schnee fällt | Schlitten (ein Element), sonst still | Polarlicht wandert langsam, Stern-Halo pulsiert |
| Bewegung reduzieren | kein Schnee, Lampen ruhig | kein Schlitten | still |
| Elemente | ~1 Pfad + 15 Lampen + 26 Punkte | ~6 Gruppen + 1 bewegter | 3 Flächen + 8 Formen |
| Alte Handys | sehr leicht | leicht | leicht (ein Unschärfe-Filter, einmal gezeichnet) |

**Tages-Sonderfälle** (zusätzlich zur gewählten Variante):
- **6.12.:** Nikolaus-Stiefel mit drei Goldstücken neben dem aktuellen Pin.
- **24.12.:** Der Schlitten zieht **einmal** quer über die Karte, mit goldener Glitzerspur; danach bleibt nur die Spur.
- **31.12.:** Drei Feuerwerks-Bursts **neben** dem aktuellen Ort, an einer Stelle ohne Pins, je 2,4 s, dreimal, dann Ruhe.

**Freizonen** (Entwurf `#s=karte&v=2&frei=1`): Regel-Universum-Sonne, Zoom-Knöpfe, Quellenzeile, Jugendwort-Schild und „Gerade dran“ bleiben frei. Mützen sitzen **über** dem Pin-Kopf und verdecken die Flagge nicht.

---

## 12. Offene Fragen an den Nutzer (Auswahl)

1. **Gutscheine einlösen:** **A** Das Kind fragt an, die Eltern tippen „Eingelöst / Heute nicht“ (Empfehlung) · **B** nur die Eltern schalten aus.
2. **Nachholen nach dem 24.:** **A** bis 31.12. (Empfehlung; Weihnachtstage sind oft lernfrei) · **B** nur bis 24.12. · **C** bis 6.1.
3. **Zählt „Sitzt wieder!“ (Nachbessern) als geschaffte Etappe?** **A** ja, eigene Landung ist eigene Landung (Empfehlung) · **B** nein, nur neue Etappen.
4. **Weihnachts-Ebene auf der Karte:** **1** dezent · **2** verspielt · **3** Neon-Nordlicht · **2+3** gemischt (Mützen, Geschenke und Schlitten aus 2, Stern aus 3).
