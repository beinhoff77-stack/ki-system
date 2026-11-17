# Postfach bau-phase2 (Bau-Chat App-Code, Phasen 2 und 3)

Neueste oben.

## 2026-11-17 – Schritt D (K3, K4, E-4) gebaut – App 0.74.6 – **wartet auf Migration**

**Schritt C gegen die echte Antwortform geprüft** (nur lesend): `route.ausgelassen`/`status_vor_entfernen`, `rueckmeldung.bezug`, `plan_lesen.kann_abwaehlen`,
`uebersicht` mit `thema_id`/`reihenfolge`/`ausgelassen`, `plan_setzen` mit `status_vor_entfernen`, `ort_stand` ohne abgewählte Flüge, `rueckmeldungen.bezug` – alles so, wie die App es liest.
Entfernte Einträge stehen bei höchstens 1 000 037 (46 Zeilen), `block_thema.reihenfolge` ohne Lücken. Keine Abweichung gefunden.

**Migration `supabase/migrations/20261117_w150_d_stufen_stand.sql`** (nicht ausgeführt; Syntax mit pglast geprüft; Ersetzungsstellen im Live-Text vorhanden; kein DROP, kein DELETE)
- `schule.lernender.stufen jsonb` (Standard `{}`): Stufe je Schulart, z. B. `{"rs_by": 6}`. Fehlt eine, gilt: eigene Schulart = Klasse, andere = Klasse, IB MYP = Klasse − 4.
- `schule.thema.lehrplan_reihenfolge jsonb`: Reihenfolge innerhalb der Klasse je Schulart, befüllt für 68 Flüge aus `inhalte/themenliste.json` (Feld `reihenfolge`, nur `gym_by`).
- `api.schule_kind_setzen` nimmt zusätzlich `stufen: {gym_by|rs_by|ib_myp: 1–13 | null}` an (null löscht).
- `api.schule_uebersicht`: je Kind `stufen`; neu oben `themen: [{thema_id, titel, jahrgang, reihenfolge, block_id, stadt, kontinent, erdteil, einheit_id}]` = **alle** Mathe-Flüge, auch ohne Inhalt.
  Damit zählen Stand und Einstiegs-Check nach der Rechenregel alle Flüge der Klasse. Ohne das Feld zählt die App nur Flüge mit Inhalt und sagt das dazu.
- `api.schule_plan_lesen`: `kind.stufen`; je Flug `lehrplan_reihenfolge` (für E-4).
- `api.schule_lernstand`: je Etappe `sitzt_am` und `bis_sitzt` = Zahl der Bordkarten (erste Versuche, ohne Tests) bis zum ersten „sitzt“ (K4-Wunsch; das Feld fehlte).

**App (läuft ohne Migration weiter, getestet)**
- **K3 Kind:** Abflugtafel mit drei Mini-Linien GYM · RS · IB (ersetzt die Jahrgangs-Box). „Mein Weg · Stand“ in drei Ebenen: Linienplan (Klassen 5–10, IB MYP n unter Klasse n+5, „DU“ an der eigenen Stufe) →
  Passkarte einer Klasse mit ‹ › und Kontinenten → Flüge eines Kontinents mit „zählt auch für …“. Pfad oben (Überblick › Stufe › Kontinent).
- **K4 Eltern/Lehrer:** neue Seite „Stand über Schularten“ (`#/schulstand`, Karte unter „Für alle Kinder“, Mini-Linien je Kind auf der Startseite verlinkt).
  Ebene 1 Kinder × drei Schularten; Ebene 2 Landkarte Kontinente × Klassen mit Reitern je Schulart und „Einstieg prüfen: Kl. X“ (Ampel ≥ 90 % grün, ≥ 70 % gelb, sonst rot,
  Klassen ab X ausgegraut, Liste „Für den Einstieg fehlen“), Hinweis „Orientierung, keine Einstufung durch eine Schule.“; Ebene 3 Flüge eines Feldes mit dem Stand jeder Etappe,
  „sitzt – nach N Bordkarten“ (auch im Lernstand), Link „Was wackelt?“.
- **E-4:** im Flugplan „Neuer Plan aus Lehrplan-Vorlage“ (Schulart, Klasse; vorbelegt aus Stufe): ersetzt den Plan durch die Orte mit Inhalt dieser Klasse, geordnet nach `lehrplan_reihenfolge`
  (ohne Migration: Reihenfolge im Lehrplan-Verzeichnis, wird angesagt); Flüge anderer Klassen werden abgewählt, wenn die Datenbank das kann. „Rückgängig“ holt den alten Plan zurück, „geschafft“ bleibt.
  Stufen je Schulart lassen sich unter „Klasse“ setzen, sobald `kind.stufen` geliefert wird.
- Info-Seite: Hinweise auf „Stand über Schularten“ und die Vorlage.
- Tests: 38 von 38 (neu: K3 mit/ohne Migration, K4 mit Ampel, Hinweis, ausgegrauten Klassen, `bis_sitzt`, E-4 mit Reihenfolge, Abwählen, Rückgängig). Suche: die 9 bekannten alten Fehler.

**Offen / zu prüfen nach dem Einspielen:** Antwortform der vier geänderten Funktionen gegen die App; danach Ende Schritt D. Merge auf `main` erst nach „Live“.

## 2026-11-17 – Schritt C (E-2, E-3) gebaut – App 0.74.5 – **wartet auf Migration**

Zwei Migrationen liegen bereit (nicht ausgeführt). Ich habe dafür die aktuellen Funktionsdefinitionen nur **gelesen** (pg_get_functiondef), damit Ersetzungen und
`create or replace` auf dem Live-Stand aufsetzen; alle Ersetzungsstellen sind im Live-Text vorhanden (geprüft). Syntax beider Dateien mit dem Postgres-Parser (pglast) geprüft.
Kein DROP, kein DELETE. Die App läuft ohne die Migrationen weiter (Feld fehlt → bisheriges Verhalten; getestet).

**1. `supabase/migrations/20261117_w150_e2_plan_fluege_abwaehlbar.sql`** (E-2 + Befunde 2 und 3 der Nachprüfung E-1)
- Neue Spalten `schule.route.ausgelassen bigint[]` (abgewählte Flüge = `thema.id`) und `schule.route.status_vor_entfernen text`.
- `schule.ort_stand`: zählt nur geplante Flüge → Stempel, Ort-Status und `konto.stempel` ohne abgewählte Flüge. `konto.jahrgang` (Stand je Schulart) zählt weiter alle.
- `api.schule_plan_setzen` nimmt je Eintrag `ausgelassen: [thema_id, …]` an (fehlt das Feld: Liste bleibt). Prüft, dass die Flüge zum Ort gehören.
  **Befund 2:** „Entfernen“ merkt den alten Status; beim Zurückholen (Rückgängig) wird er wiederhergestellt – „geschafft“ bleibt. Die Sterne für den Ort werden dabei nicht doppelt gebucht (Eindeutigkeit lernender/grund/bezug).
  **Befund 3:** Entfernte Einträge stehen fortlaufend ab 1 000 001 und wachsen nicht mehr bei jedem Speichern (einmalige Neu-Nummerierung in der Migration; `route_pos` ist DEFERRABLE).
- `api.schule_plan_lesen` liefert `kann_abwaehlen: true`, je Eintrag `ausgelassen`, und **zusätzlich Orte, die das System auf „fertig“ gesetzt hat** (bisher fehlten sie im Plan der App, weil `ist_plan` `geaendert_von = 'system'` ausschließt – beim nächsten Speichern wurden sie als „nicht genannt“ entfernt und verloren „geschafft“; das ist eine zweite Ursache für Befund 2).
- `api.schule_uebersicht` (gezieltes Ersetzen): je Einheit `thema_id` und `reihenfolge` (aus `schule.block_thema.reihenfolge` = Lehrplan-Reihenfolge im Ort, für K2 „Flüge im Ort ordnen“), je Route-Eintrag `ausgelassen`.

**2. `supabase/migrations/20261117_w150_e3_auftraege_bezug.sql`** (E-3)
- Die Arten bleiben (Prüfbedingung unverändert). Neue Spalte `schule.rueckmeldung.bezug` (erklaerung · etappe · bordkarte · flug · plan · allgemein).
- `api.schule_rueckmeldung_geben` speichert `daten.bezug`. `api.schule_rueckmeldungen` liefert zusätzlich `bezug, block_id, lernender_id, kind, flug, etappe`.
- Werkstatt-Nachricht nennt den Bezug und verweist auf „Meine Aufträge“.

**App (schon gebaut, Tests 34 von 34):**
- **E-2 Startseite:** je Kind ein Bereich (Name, Schulart · Klasse, drei Mini-Balken GYM/RS/IB mit gelandet/gesamt, Jetzt, Sterne/Stempel/Lerntage, Knöpfe Lernstand · Flugplan · Lernreise ansehen); darunter „Für alle Kinder“: Lehrplan-Übersicht · Meine Aufträge · So funktioniert’s · Testkind · Zugänge. Mini-Balken nach Rechenregel „Stand“; Stufe RS = Klasse, IB = Klasse − 4, bis K3 `stufen` liefert. Gezählt werden Flüge mit Inhalt (die Übersicht kennt keine Flüge ohne Einheit).
- **E-2 Flugplan:** Kopfzeile bleibt oben mit Speicherstand und **„↶ Rückgängig“ dauerhaft** (Befund 4). Zwei Spalten ab 1 000 px (Plan links, Lehrplan nach Schulart/Klasse rechts, Suche), darunter auf Tablet und Handy. Eine Zeile je Ort (zugeklappt 58 px), **Ziehen am Griff ⠿** mit Maus und Finger (Pointer-Ereignisse, `touch-action: none`, Rollen am Rand), dazu ↑ ↓; aus dem Lehrplan in den Plan ziehen oder „+“. Ort antippen → Flüge mit Häkchen „im Plan“ (erst nach Migration, vorher Hinweis), „kann es schon“, Entfernen.
  Prüfpunkte: Platz 10 → 2 mit einer Ziehbewegung = ein Speichern ✓; zugeklappt ≤ 72 px ✓ (58); 12 Orte auf einem Tablet-Bildschirm 820 × 1180 ✓; abgewählter Flug fehlt in der Kinderansicht ✓ (App filtert nach `route.ausgelassen`/`thema_id`, sobald geliefert).
- **E-3:** ein Knopf „✎ Ändern lassen“ an Erklärung, Etappe, Bordkarte, Flug (Erklären-Reiter, Inhalte ansehen, Lehrplan-Übersicht statt „Bauen lassen“) und Flugplan. Das Formular zeigt den Bezug („An: Bordkarte „…““), Arten Erklärung · Bordkarten · Fehler · Neuer Flug · Sonstiges, Vorlagen-Chips, fragt „Was soll anders sein?“. **„Meine Aufträge“** (`#/lernauftraege`, `#/rueckmeldungen` bleibt) mit Filter Offen/Beantwortet/Alle, Status, Bezug und Antwort; Startseite „Neue Antworten auf eure Aufträge“. Route nicht `#/auftraege`, weil die Hauptapp diese Adresse schon für Council-Aufträge nutzt.
- **Info-Seite** (Befund 1 und neue Regeln): „über 90 Flüge“ statt fester Zahl; Satz zu den 16 Flügen gestrichen; „100 Sterne und ein Stempel für jeden geschafften Ort“; Kapitel „Was kann ich selbst ändern?“ und „Wie beauftrage ich eine Änderung?“ auf E-2/E-3 umgestellt (abwählen gilt nach der Migration).
- **Befund 5:** Reisewörter-Test mit `\bThema\b|\bThemen\b`, die Erklärung „= ein Mathe-Thema“ ausgenommen.

**Nach dem Einspielen prüfe ich gegen die echte Antwortform:** `schule_plan_lesen.kann_abwaehlen`/`plan[].ausgelassen`, `schule_uebersicht.einheiten[].thema_id/reihenfolge`, `lernende[].route[].ausgelassen`, `schule_rueckmeldungen[].bezug/flug/etappe/kind`. Danach Schritt D (K3, K4, E-4; braucht das Feld `stufen`, Migration folgt mit D).

## 2026-11-17 – Schritt A2 fertig (Nacharbeit N1/N2/N7) – App 0.74.4 – Nachprüfung kann laufen

| Punkt | Umsetzung | Nachweis |
|---|---|---|
| N2 | „Kurz gesagt“ endet am ersten . ! ? vor Leerzeichen oder Textende (`lernSatzEnde`). Ausnahmen: Abkürzungen (z. B., d. h., u. a., z. T., s. o., bzw., ca., usw., vgl., etc., ggf., evtl., bspw., inkl., Nr.), Aufzählungen („1. … , 2. …“) und Ordnungszahlen nach Artikel („die 3. Wurzel“) sowie vor kleinem Wort. Einzelbuchstaben am Satzende („… durch P.“) beenden den Satz. | Test: alle 593 Merksätze aus `inhalte/themen` – „Kurz gesagt“ ist höchstens ein Satz (dazu eine unabhängige Gegenprobe „Satzzeichen + Großbuchstabe“). |
| N1 Abblenden | Keine Deckkraft mehr für Graphen, Linien und Punkte: der Rest wird grau gezeichnet (hell #6B7280 auf Weiß 4,8:1, dunkel #9AA3B2 auf #151B24 6,9:1); nur Gitter und alte Hilfslinien werden heller. Abgeblendet wird nur, wenn im Bild wirklich ein Element `.neu` trägt. | Test (Kerze): Graph Deckkraft 1, Farbe grau. |
| N1 Steigungsdreieck | Die App vergrößert nichts mehr; das Dreieck steht so im Bild wie im Inhalt, neu = kräftig in der Akzentfarbe. | Test: 1 Einheit breit; `lernDreieckGross` entfernt. |
| N1 Tabellen/Stellentafel | Ändert ein Schritt einzelne Zellen (neuer Wert) oder die Markierung der Stellentafel, ist genau diese Zelle hervorgehoben (gelb hinterlegt, Rahmen in Akzentfarbe). Ändert sich die ganze Tabelle, wird nichts hervorgehoben. | Test. |
| N7 | Richtige Markierung am Zahlenstrahl in festem Grün #2E9E44 in allen Gestaltungen. | Test. |

Tests: `tests/lernen.test.cjs` 28 von 28. `tests/search.test.cjs`: die bekannten 9 alten Fehler.
Schritt C (E-2/E-3 mit Migrationen) ist gebaut und folgt als nächste Meldung.

## 2026-11-17 – STATUS Schritt B (K2) fertig – App 0.74.3

- **Menü:** Abflugtafel · Mein Weg · Merkheft · Reisepass (alte Gestaltung: Heute · Mein Weg · Merkheft · Reisepass). `#/weltkarte/<kind>` führt in „Mein Weg · Karte“.
- **Mein Weg** mit Reitern **Stand · Kontinente · Karte** (`#/weg/<kind>-stand|-kontinente|-karte`):
  - Stand: Balken der eigenen Klasse nach der Rechenregel (Flüge mit `jahrgang[schulart] = Klasse`; gelandet = alle Pflicht-Etappen sitzen, „kann schon“ oder Ort geschafft), dazu wie bisher Gerade dran · Kommt noch · Kann ich. K3 ergänzt Mini-Linien und die drei Ebenen.
  - Kontinente: je Kontinent eine aufklappbare Karte mit „gelandet/gesamt“ (ohne Flüge für spätere Klassen), darin die Flüge mit Ort, Klasse und Stand.
  - Karte: nur Orte der eigenen Klasse (`orte[].ziel_klasse`), Route in Plan-Reihenfolge. Antarktis als Polarkarte von oben (Umriss aus der Weltkarte zurückgerechnet, Südpol in der Mitte, 0° oben).
- **Merkheft:** nur Geschafftes (Etappe fertig oder sitzt), gegliedert Kontinent → Flug → Etappe, Suche oben.
- **Reihenfolge der Flüge im Ort:** nach `reihenfolge` aus `schule_uebersicht.einheiten[]` (Zahl oder `{gym_by: n, …}` je Schulart des Kindes), sobald geliefert; sonst wie bisher.
  **Für den Haupt-Chat:** `schule_uebersicht` liefert das Feld noch nicht – es steht nur in `inhalte/themenliste.json`. Vorschlag: Spalte `thema.reihenfolge jsonb` und Ausgabe in `einheiten[]`; die Migration kommt mit Schritt C.
- Tests: 26 von 26 (3 neu: Reiter, Antarktis, Reihenfolge; Merkheft-Test auf „nur Geschafftes“ umgestellt).

## 2026-11-17 – Schritt A fertig (Befunde N1–N8) – App 0.74.2, Zweig bau-phase2 – Nachprüfung kann laufen

| Nr. | Umsetzung | Prüfpunkt |
|---|---|---|
| N1 | `lernErklaerung` zeigt ein Schrittbild nur, wenn sich die Zeichnung gegenüber dem zuletzt gezeigten Bild (auch dem Einstiegsbild) ändert; sonst steht nur der Text. Verglichen wird das gezeichnete Bild, nicht die Daten. Neu im Bild (Punkte, Strecken, Hilfslinien, Graphen, Kreise, Winkel, Bögen, Flächen, Thermometer-Stand) wird in der Akzentfarbe kräftig gezeichnet (Punkte größer, Linien 4 px), der Rest tritt zurück (40 % Deckkraft). Ein Steigungsdreieck (waagrechte + angehängte senkrechte Hilfslinie) wird in Erklärungen mindestens 2 Einheiten breit gezeichnet, gleiche Steigung; in Bordkarten nie. | „Was bedeutet eine negative Zahl?“: 3 Schritte, nur Schritt 1 mit Bild (vorher 3 gleiche Thermometer); Handy deutlich unter 2 400 px (Test). Kerze (Kl. 8): keine zwei gleichen Bilder hintereinander (Test). |
| N8 | Bildergeschichte mit Bild: Handy Nummer · Bild, darunter Text; ab 760 px Nummer · Bild links · Text rechts in einer Zeile. | Test: Text steht rechts neben dem Bild, gleiche Zeile (820 px). |
| N2 | „Kurz gesagt“ wird ganz gezeigt, kein „…“ und keine Zeilenkürzung. Satzende erkennt jetzt Abkürzungen („z. B.“). | Test. **Hinweis Inhalte:** 116 von 593 Etappen haben einen ersten Merksatz über 90 Zeichen (auf dem Handy mehr als zwei Zeilen). Das ist eine Inhaltsregel (≤ 12 Wörter), kein App-Fehler. |
| N3 | Kurs-Grafik: Der Komma-Platz in der Zeile ohne Nachkommastellen bleibt leer, ohne gestrichelten Rahmen. | Test (0,24 gegen 24). |
| N4 | Startknopf: „Erst 1 Wiederholung ›“ (Anzahl statt Ziel); ist die Runde heute gemacht: „Weiter nach Rom ›“. | Test. |
| N5 | Fehler-Detektiv nur, wenn kein Fehlermuster (`grund`) erkannt wurde – in Abflug- und alter Gestaltung. Die Einschränkung „nur Kl. 5/6“ habe ich nicht zusätzlich eingebaut (Auftrag: nur ohne Fehlermuster). | Code-Test. |
| N6 | Test-Seiten: Kopf „Rom · Natürliche Zahlen“ (Ort · Flug). | Test. |
| N7 | Testergebnis: Knöpfe im Abflug-Stil. Bei „noch üben“: Hauptknopf „Erst üben: <Etappe> ›“ (öffnet Üben dieser Etappe), dann „Verbessern ›“ (Test-Seite mit „Verbessern starten“), darunter „Zum Flug“ und „Zur Abflugtafel“. Zahlenstrahl: richtige Markierung grün mit ✓, gewählte falsche rot gestrichelt. „Einheit geschafft!“ heißt jetzt „Flug geschafft!“. | Test, Bild `test-results/n7-testergebnis-390.png`. |

**Tests:** `tests/lernen.test.cjs` 24 von 24 (6 neu). `tests/search.test.cjs`: die bekannten 9 alten Fehler, keine neuen.

**Hinweise für Inhalte (kein App-Fehler):** In der Kerze-Etappe überdeckt der Punktname „leer“ den Graphennamen „Kerze“ (beide bei x ≈ 13). Neue Elemente sind jetzt hervorgehoben; ob ein Schritt überhaupt ein neues Element bringt, entscheidet der Inhalt.
