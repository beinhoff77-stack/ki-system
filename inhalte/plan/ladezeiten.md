# Ladezeiten Lernen Schule – Analyse und Entwurf (TEMPO, Stand 28.11.2026, App 0.96.0)

Zweig `helfer-tempo`, ENTWURF: nichts live, nichts eingespielt, Versionsnummer unverändert.
Live-Messwerte: vom Projektleiter (Chrome Desktop, warmer Cache). Alle anderen Zahlen stammen aus dem nachgestellten Server der Tests
bzw. aus dem lokalen Nachbau der Datenbank mit erfundenen Daten. Annahmen sind als solche markiert.

## 1. Woher die Doppelaufrufe kommen (lernen.js)

**Grundproblem: nur ein Teil der Leseabrufe wurde gemerkt.**
- `lernCall` merkte bisher nur sechs Aktionen der Lehrer-Seiten (`LERN_MERKEN`: uebersicht, lehrplan_matrix, lehrplan_uebersicht, lernstand, plan_lesen, wackelt_lesen).
- `merkheft`, `konto`, `wiederholung` und `einheit_lesen` gingen bei jedem Aufruf ans Netz. Auch zwei gleichzeitige gleiche Aufrufe liefen doppelt.
- Jedes zweite Zeichnen derselben Seite lud diese vier deshalb noch einmal.

**Wege, auf denen die Reiseseite zweimal zeichnet:**
1. **WT-Weg (0.93.5):** Die Seite wird mit der alten Karte gezeichnet (`lernReiseKarteAlt`). Wenn die frische Karte kommt, ruft `lernZielBisFrisch` `render()` auf.
   - Das trifft zu, wenn eine Änderung die Karte als alt markiert hat und für dieses Kind noch keine „letzte Ansicht“ gespeichert ist.
   - Beim zweiten Zeichnen liefen `konto`, `merkheft`, `wiederholung` und `einheit_lesen` erneut. `uebersicht` (gemerkt) und `reise_karte` liefen nur einmal.
   - Das ist genau das Muster der Live-Messung.
   - Im Test nachgestellt (Expeditionen öffnen → Änderung → Reisekarte): Mit 0.96.0 läuft `merkheft` dort zweimal. Test: „TEMPO: Reisekarte mit alter Karte …“.
2. **Hinweise, die mit `render()` neu zeichnen:** Expedition freigeschaltet (`weiter: () => render()`), Look/Ansicht wechseln, Einlösen.
3. **Hauptknopf auf Abschluss- und Landungsseiten:** `lernSchrittKnopf` → `lernSchrittLaden` lädt uebersicht, konto, reise_karte, merkheft und wiederholung. Ein Tippen auf „Weiter“ zur Reisekarte lud dann alles noch einmal.

**`schule_rueckmeldungen` galt als schreibend:**
- Die Aktion fehlte in `LERN_NUR_LESEN`. Jedes Öffnen der Eltern-Startseite rief deshalb `lernVergessen()` auf, und zwar vor und nach dem Abruf.
- Dabei wurde alles vergessen: Übersicht, Matrix, Lernstand und alle Reisekarten.
- Danach wurde die Übersicht auf der nächsten Seite neu geladen, und die Reisekarte galt als alt. Das führte in den WT-Weg aus Punkt 1.
- Laut Datenbank ist `api.schule_rueckmeldungen` eine reine Lesefunktion (`stable`, nur `select`).

**Eltern `#/kind/<id>` (11 Aufrufe, zwei Wellen):**
- Welle 1 ist das Vorladen des Reiters (alles gleichzeitig).
- Welle 2 kommt 300 ms nach dem Zeichnen: `lernstand`, `plan_lesen` und `wackelt_lesen` für das andere Kind bzw. die anderen Kinder, ohne Testkind. Das ist gewollt (schneller Wechsel) und blockiert nichts.
- „plan_lesen ×3 / wackelt_lesen ×3“ erklärt sich so: eigenes Kind plus zwei weitere echte Kinder (**Annahme**, im Nachbau gibt es zwei Kinder → je 2×).
- `lehrplan_matrix` ×2 (184 kB / 194 kB): Die zweite Antwort ist die Matrix mit Testkind (`mit_testkind: true`). Sie wird geladen, wenn das Kind in der Matrix ohne Testkind fehlt.
  - Diese Matrix lief erst **nach** der ersten.
  - Neu: Sie wird mit vorgeladen, wenn das schon bekannt ist (Testkind laut Übersicht, oder Kind fehlt in einer gemerkten Matrix).
  - Beim ersten Öffnen ist das noch nicht bekannt. Dort bleibt es bei zwei Abrufen nacheinander.

**Seiten, die erst auf konto warten (Nachtrag Projektleiter):**
- `lernLadeKind` holt uebersicht und konto gleichzeitig. Die eigentlichen Abrufe der Seite starteten erst danach.
- Betroffen: `#/weg` (merkheft), `#/route` (lehrplan_matrix), `#/wiederholen` (wiederholung), `#/merkheft` (merkheft), `#/stationen` (reise_karte).
- Die Parameter hängen in allen fünf Fällen nur an der Kind-Nummer aus der Adresse, nicht am konto-Ergebnis. Diese Abrufe starten jetzt gleich mit.

## 2. Was die Reiseseite aus `merkheft` braucht

Mit Reisekarte (neue Gestaltung) bestimmt `lernSchritt` den Hauptknopf aus den Ständen der **Karte** (`staedte[].stand`). Das Merkheft liefert nur:
- `lernEtappenZahl` der Einheit des Schritts: Zahl der Etappen und der fertigen Etappen (`etappen[].lernziel`, `stand[lz].fertig`). Ohne Merkheft gibt es einen Rückfall auf `uebersicht` (`n`, `fertig`).
- `lernNamenSetzen`: die nächste offene Pflicht-Etappe je Einheit, also der Name der Stadt im Knopf (`etappen[].lernziel/pflicht`, `stand[lz].fertig/pflicht`). Ohne Merkheft gibt es einen Rückfall auf die Städte-Stände der Karte.
- `ortVon`: die Etappen aller Flüge des Ortes (Band).

Gebraucht werden also je Einheit nur `einheit_id`, die Lernziele und Pflicht-Kennzeichen der Etappen sowie `stand[lz].fertig/pflicht`.
**Nicht** gebraucht werden die Texte der Etappen (`regel`, `schritte`, `bild`, `fehler` …) und `abschnitte`. Genau diese machen die 1187 kB aus (**Annahme** nach Aufbau; Größe je Feld nicht gemessen).

**Gebaut:**
- Die Reisekarte wartet nicht mehr auf das Merkheft.
- Ist die Karte vorher da, wird sie sofort gezeichnet. Hauptknopf, „Gerade dran“ und Einsteigen sind gesperrt und ohne Stadtname (`.lr-ziel-offen`, dieselbe Sperre wie bei der alten Karte, WT 0.93.5).
- Mit dem Merkheft wird die Seite einmal neu gezeichnet. Wiederholung und Bordkarten der Stadt werden dabei aus demselben Abruf weiterverwendet (kein zweiter Abruf, keine neue Zufallsauswahl).
- Hinweise „Expedition frei“ und „Zusatz geschafft“ erscheinen erst nach dem Neuzeichnen, also mit vollem Stand.
- Ohne Karte (Abflugtafel, alte Gestaltung) bleibt alles wie bisher: Es wird erst mit dem Merkheft gezeichnet.

**Mein Weg (`#/weg`):**
- Nur der Reiter „Stand“ (Überblick) nutzt das Merkheft: „Gerade dran: Etappe x von n“ sowie Nachtest und Link bei geschafften Orten.
- „Kontinente“ und die tieferen Ebenen von „Stand“ (Klasse, Kontinent) nutzen es nicht.
- Neu:
  - Das Merkheft startet gleichzeitig mit uebersicht und konto.
  - Die Seite wird ohne Merkheft schon gezeichnet. Die zwei Angaben aus dem Merkheft zeigen dann „…“.
  - Mit dem Merkheft wird einmal neu gezeichnet.
  - Tiefere Ebenen warten nicht mehr darauf.
- Nur mit uebersicht und reise_karte geht es nicht ganz: Den Nachtest-Stand liefert nur das Merkheft (bzw. `einheit_lesen`).

## 3. Warum `schule.etappen_stand` langsam ist

Maßgeblich ist die jüngste Fassung: nachgerechnet aus `20261114_w150_lernkarten_meisterschaft.sql` und den Text-Ersetzungen in r3, sitzt_regel_6, t1, t3, h_muss und ft_s.
- Der md5 des Funktionstexts ist `bf3152e9…` (`tools/tests/tempo_einspielen.py`).
- Die Migration spielt nur ein, wenn die Datenbank genau diesen Text hat.

**Je Etappe (Lernziel) einer Einheit rechnet die Funktion:**

| Teil | liest | je Etappe |
|---|---|---|
| gesamt | aufgabe (einheit, pool, lernziel, freigegeben) | 1 Abfrage |
| geloest | versuch ⋈ aufgabe (Kind, Einheit, Lernziel) | 1 |
| `karte_ziel` (für `ziel` **und** `folge_ziel`) | aufgabe | 2 |
| `karte_typen_noetig`, `karte_schwer_noetig`, `karte_anwenden_noetig` | aufgabe | 3 |
| `karte_bearbeitungen` | versuch ⋈ aufgabe | 1 |
| `karte_sicher`, `karte_faellig`, `karte_anwenden_ok` | testsitzung/versuch/misch_ausgabe, lerntag, aufgabe | je nach Karte |
| `flug_nachtest(Kind, Einheit)` → `flug_ohne_test` → `thema_kann_wdh`, `zusatz_eingeplant` | route, block_thema, thema, testsitzung | 1 – **je Einheit gleich, aber je Etappe gerechnet** |

**Fehlende Indizes:**
- Im Repo gibt es keinen Index auf `schule.aufgabe(einheit_id …)` und keinen auf `schule.versuch(lernender_id, aufgabe_id)`.
- Bekannt sind live nur die eindeutigen Indizes (`supabase/tests/nachbau_live_constraints.sql`): `versuch` (testsitzung_id, aufgabe_id) und (lernender_id, client_id) aus dem Nachbau.
- Ohne diese Indizes ist jede der rund zehn Unterabfragen je Etappe ein Lauf über die ganze Tabelle `aufgabe` (rund 15 000 Zeilen im Nachbau) bzw. über alle Versuche des Kindes.
- Bei 95 Einheiten mit je 5–10 Etappen sind das einige Tausend Tabellenläufe je `schule_merkheft`.
- Ob live ein nicht eindeutiger Index existiert, ist **nicht bekannt**. Die Probe listet alle Indizes beider Tabellen vor und nach dem Einspielen.

**Lokaler Nachbau** (erfunden: 95 Einheiten, 15 488 Aufgaben, 23 498 Versuche, `tools/tests/tempo_nachbau.sql`), etappen_stand für alle Einheiten eines Kindes:

| Fassung | Laufzeit |
|---|---|
| alt, ohne Indizes | 15,6 s |
| neu, ohne Indizes | 5,3 s |
| alt + Index aufgabe | 4,1 s |
| alt + beide Indizes | 0,69 s |
| neu + beide Indizes | 0,65 s |

- Merkheft-Kopie je Kind im Nachbau: 6,3–8,4 s → 0,30–0,68 s.
- Die Indizes bringen das meiste. Die neue Funktion spart vor allem dann, wenn ein Index fehlt oder nicht greift.
- **Annahme:** Live ist es ähnlich, also für `schule_merkheft` von rund 4,7–5,9 s auf deutlich unter 1 s, plus die Übertragung von 1,2 MB. Nicht live gemessen.

**`schule_uebersicht` (196 kB, 1,0–2,3 s):**
- Die Funktion steht nicht vollständig im Repo (nur Text-Ersetzungen).
- Sie rechnet je Kind die Stände aller Einheiten (`lernziel_stand` ⋈ `karte_stand`, `etappe_fertig`) und liefert alle Orte, Einheiten und Themen.
- Im Client ist sie gemerkt (`LERN_MERKEN`, nach 10 s im Hintergrund aufgefrischt). Neu geladen wurde sie vor allem aus drei Gründen:
  - nach jeder Änderung, z. B. einer beantworteten Aufgabe – richtig so;
  - durch den Rückmeldungen-Fehler oben – behoben;
  - durch das Auffrischen im Hintergrund nach 10 s – blockiert nicht.
- Serverseitig nicht angefasst. Vorschlag in Abschnitt 6.

## 4. Gebaut (Client)

- **`lernCall`:** drei neue Stufen für reine Lese-Aktionen. `LERN_MERKEN` bleibt unverändert.
  1. `LERN_KURZ` (merkheft, konto, eltern, rueckmeldungen, lehrplan_thema): Die Antwort gilt 15 s ab Eingang. Danach wird wieder **blockierend** vom Server geladen (kein „alt zeigen“).
  2. Vorab (`lernVorladen`): Die Antwort bleibt für den **ersten** gleichen Abruf liegen, einmal und höchstens 15 s lang.
     - Das gilt für `wiederholung` und `einheit_lesen`: Zufall, und der Server stellt Mischkarten aus.
     - So bleibt es bei einem Server-Abruf je Ansicht wie bisher, nur früher gestartet.
  3. Alle übrigen Lese-Aktionen: Gleichzeitige gleiche Anfragen teilen sich die laufende Antwort. Danach wird nichts gemerkt.
- **Vergessen:**
  - Jede schreibende Aktion vergisst alles zum Kind und alles Kindunabhängige; ohne Kind vergisst sie alles. Das geschieht wie bisher **vor und nach** dem Schreiben.
  - Eine Leseantwort, die während des Schreibens lief, wird nicht gemerkt.
  - Kindwechsel (bei `LERN_KURZ`) vergisst das kurz Gemerkte anderer Kinder.
  - Ein anderer Zugang (Abmelden, neu angemeldet, 401) vergisst alles, auch die Reisekarten und die letzte Reise-Ansicht.
  - Eine Vorab-Antwort gilt nach jedem Vergessen nicht mehr.
- **`schule_rueckmeldungen`** gilt als lesend.
- **Reiseseite:** wie in Abschnitt 2. Beim WT-Neuzeichnen und beim Neuzeichnen nach dem Merkheft werden Wiederholung und Bordkarten der Stadt aus dem ersten Abruf weiterverwendet, wenn seitdem nichts geändert wurde.
- **Gleichzeitig starten:** `#/weg`, `#/merkheft`, `#/route`, `#/wiederholen`, `#/stationen`. Bei `#/kind` die Matrix mit Testkind, wenn bekannt.
- **Lehrer-Startseite** (`viewLernen`, lernZuTun, lernKinderTabelle): nicht angefasst. Wirkung dort nur über den Rückmeldungen-Fehler (kein Vergessen mehr).
- **`sw.js`:**
  - Hüllen-Dateien mit `?v=<version>` aus der Liste `HUELLE` kommen zuerst aus dem Cache **dieser** Version, nur bei Fehlen aus dem Netz.
  - `index.html`, `./`, Bilder ohne Version, `karte/` und `daten/` bleiben „Netz zuerst“.
  - Ein neues Release kommt so sofort an:
    - `index.html` kommt aus dem Netz und nennt neue `?v=`-Adressen. Die stehen nicht in der Hülle der laufenden Version, also lädt der Browser sie selbst aus dem Netz.
    - Der neue Service Worker (neuer Cache-Name) lädt bei `install` alles frisch (`no-cache`) und löscht beim Aktivieren den alten Cache.
    - Im Browser-Test geprüft: Das neue `lernen.js` läuft schon beim ersten Neuladen; danach bleibt nur noch der neue Cache.
  - **Bedingung:** Jede inhaltliche Änderung an einer Hüllen-Datei braucht eine neue `?v=` **oder** einen neuen Cache-Namen in `sw.js`. Beides geschieht bei jedem Release ohnehin zusammen. Wer eine Datei ändert, ohne eines davon zu erhöhen, liefert sie bis zum nächsten Release nicht mehr aus (vorher kam sie trotzdem an).

## 5. Gebaut (Server-Entwurf) – `supabase/migrations/20261207_tempo_s1.sql`

- `create index if not exists`:
  - `aufgabe_einheit_pool_lz_idx` auf `schule.aufgabe (einheit_id, pool, variante_gruppe)`
  - `versuch_kind_aufgabe_idx` auf `schule.versuch (lernender_id, aufgabe_id)`
- `schule.etappen_stand` neu (create or replace, nur bei passendem md5), gleiches Ergebnis:
  - `flug_nachtest` einmal je Aufruf (Unterabfrage mit `offset 0`);
  - `karte_ziel` einmal je Etappe;
  - gesamt und geloest gruppiert je Einheit;
  - alle anderen Hilfsfunktionen unverändert.
- Kein DROP, kein DELETE, keine Tabelle, keine andere Funktion. `api.schule_merkheft` bleibt, wie sie ist.

**Pakete** (`python3 -I tools/tests/tempo_einspielen.py`, Prüfung mit `--pruefen`):

| Datei | Zweck | erwartet |
|---|---|---|
| `tools/tests/aus/tempo_s1_probe.sql` | Probelauf, rollt alles zurück | Meldung „PROBELAUF bestanden, ALLES zurückgerollt …“ mit `abweichungen_etappen_stand: 0`, `merkheft: verglichen`, `abweichungen_merkheft: []` |
| `tools/tests/aus/tempo_s1_einspielen.sql` | Einspielen (prüft sich selbst, Abweichung = Abbruch) | Hinweis „TEMPO-S1 eingespielt: …“ |
| `tools/tests/aus/tempo_s1_messen.sql` | danach, neue Transaktion, ändert nichts | „MESSUNG (nichts geändert): …“ mit den Laufzeiten |

**Vergleich in Probe und Einspielen:**
- md5 von `etappen_stand` für **alle Lernenden × alle Einheiten**, vorher und nachher. Dazu je Kind die ganze Merkheft-Antwort über eine Kopie von `api.schule_merkheft` in `pg_temp`, deren Zugriffsprüfung (`schule.zugriff`) ersetzt ist.
- Jeder Lauf läuft in einem Unterblock, der zurückgerollt wird. Was Funktionen dabei schreiben, bleibt also nicht.
- `setseed` steht vor jedem Lauf. `now()` ist in beiden Läufen gleich (eine Transaktion).
- Berichtet werden: Laufzeiten vorher/nachher, Indizes vorher/nachher (mit `indcheckxmin`) und der md5 des Funktionstexts.

**Hinweis:** Ist `indcheckxmin` beim neuen Index gesetzt, nutzt die anlegende Transaktion den Index noch nicht. Die Zeit „nachher“ in Probe und Einspielen ist dann zu hoch. Maßgeblich ist dann `tempo_s1_messen.sql`.

**Laufzeit des Pakets:** zweimal alle Paare plus je Kind das Merkheft, live vorher ≈ 4 s je Kind. Mit 30–90 s rechnen (**Annahme**). `statement_timeout` ist auf 300 s gesetzt.

## 6. Vorschläge (nicht gebaut)

1. **Schlankes Merkheft für Reiseseite und Mein Weg:** `schule_merkheft` mit `{ knapp: true }`.
   - Inhalt je Einheit: `einheit_id`, `block_id`, `etappen: [{lernziel, pflicht}]`, `stand: {lz: {fertig, pflicht}}`, `nachtest`, `blocktest_fertig`.
   - Die vollen Texte (`etappen` mit Erklärung, `abschnitte`) braucht nur `#/merkheft`, und dort nur für Geschafftes.
   - **Annahme:** 1187 kB → unter 100 kB. Das ist eine Vertragsänderung (neuer Parameter, App fragt ihn an), daher nur als Vorschlag.
2. **Übersicht teilen:** einen festen Teil (Orte, Einheiten, Themen; ändert sich nur mit neuen Inhalten, lange merkbar) und einen Teil je Kind (`lernende[].stand`, `route`; nach jeder Antwort neu). Das wäre ebenfalls eine Vertragsänderung.
3. **`etappen_stand` weiter:** Die übrigen Hilfen (`karte_sicher`, `karte_faellig`, `karte_bearbeitungen`) je Einheit in einer Abfrage. Lohnt erst, wenn die Messung nach dem Einspielen noch über ≈ 1 s liegt. Die Regeln stünden dann an zwei Stellen.
4. **Index-Bestand live auslesen** (`pg_indexes` für schule.*; im Probe-Bericht für aufgabe/versuch enthalten). Auch die anderen großen Leser (uebersicht, lernstand, reise_karte) filtern über `aufgabe.einheit_id` und `versuch.lernender_id`. Sie profitieren von denselben Indizes (**Annahme**, nicht gemessen).
5. **Eltern-Startseite:** `schule_lernstand` je Kind wartet auf `uebersicht`. Er könnte gleich mitstarten, sobald die Kinder bekannt sind (gemerkte Übersicht). Bewusst nicht angefasst, weil der nächste Helfer diese Seite umbaut.

## 7. Erwartete Wirkung je Seite (Annahmen, außer wo „Test“ steht)

| Seite | vorher (live) | erwartet | Grund |
|---|---|---|---|
| `#/reise/<id>` | Netz ruhig nach 6–12 s, Karte erst nach dem Merkheft (≈ 5 s) | Karte nach ≈ max(uebersicht, konto, reise_karte, wiederholung) ≈ 1–2 s; Hauptknopf frei, wenn das Merkheft da ist (mit TEMPO-S1 ≈ 1–1,5 s statt 5 s); keine Doppelaufrufe | Test: Karte steht vor dem Merkheft, jede Aktion genau einmal, auch im WT-Weg |
| Rückweg Aufgabe → Reise | wie oben, alles neu | gleich viele Abrufe (nach einer Antwort muss alles frisch sein), aber Merkheft schneller und nicht mehr blockierend | Vergessen nach jedem Schreiben bleibt |
| `#/weg/<id>` | 5,7 s (konto/uebersicht, dann merkheft) | Seite nach ≈ 1,7 s (uebersicht), Merkheft-Angaben danach; mit TEMPO-S1 ≈ 1,5–2 s fertig | Test: Merkheft startet vor dem Ende von konto, Seite steht vorher |
| `#/merkheft/<id>` | konto/uebersicht, dann merkheft | gleichzeitig; mit TEMPO-S1 deutlich kürzer | Test |
| `#/route/<id>` | konto 0,5 s, dann matrix 1,2 s | ≈ 1,2–1,7 s (gleichzeitig) | Test |
| `#/wiederholen/<id>` | konto, dann wiederholung | gleichzeitig | Test |
| `#/stationen/<id>` | konto, dann reise_karte | gleichzeitig | Test |
| `#/kind/<id>` | 11 Aufrufe, fertig 3,6–5 s | Welle 1 unverändert; Matrix mit Testkind gleichzeitig, wenn bekannt; Übersicht nicht mehr wegen Rückmeldungen neu | |
| Seitenwechsel allgemein | uebersicht und konto oft neu | innerhalb von 15 s ohne Änderung aus dem Speicher | |
| Hülle | ≈ 0,6 s (304 je Datei) | JS/CSS ohne Netz-Anfrage; nur index.html revalidiert | Test (Browser): kein Abruf von `lernen.js` beim Neuladen |

## 8. Offene Risiken

- **Neue Lese-Aktionen:** Eine neue Aktion, die in Wahrheit schreibt, aber auf `_lesen` endet oder in `LERN_NUR_LESEN` steht, würde nicht vergessen. Das galt schon vorher. Neu ist nur, dass `LERN_KURZ`-Antworten bis zu 15 s gelten.
- **Andere Geräte:** Eine Antwort von einem anderen Gerät (Kind am Tablet, Eltern am Laptop) sieht diese Seite bis zu 15 s später (merkheft, konto). `LERN_MERKEN`-Antworten sah sie schon vorher erst nach dem Auffrischen.
- **Sperre der Reiseseite:** Kommt das Merkheft gar nicht (Fehler), wird mit dem Rückfall `[]` neu gezeichnet und der Knopf freigegeben. Das war vorher derselbe Rückfall.
- **Cache-first im `sw.js`:** Siehe die Bedingung in Abschnitt 4.
- **Probe nur so gut wie die Datenlage:** Sie vergleicht alle vorhandenen Kinder × Einheiten zum Zeitpunkt der Probe. Fälle, die es live noch nicht gibt, sind nur im Nachbau geprüft, etwa:
  - eine doppelte Etappe;
  - eine Einheit ohne Etappen;
  - gesetzte Flüge;
  - Zusatz;
  - Regel `anwenden_pflicht` an und aus.
- **Etappe ohne `lernziel`:** Alte und neue Fassung brechen dort gleich ab (`jsonb_object_agg` mit leerem Schlüssel).
- **Merkheft-Kopie ohne Zugriffsprüfung:** Gibt sie für einen Schlüssel `null` anders aus als echt (z. B. Entwürfe nur für Leiter), vergleicht die Probe trotzdem alt gegen neu mit derselben Kopie. Das ist gültig für die Gleichheit, aber nicht unbedingt die echte Antwortgröße.
