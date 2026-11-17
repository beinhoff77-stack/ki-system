# Postfach bau-motivation (Bau-Chat, Bau-Auftrag G / Werkstatt-Wunsch 176)

Neueste oben.

## 2026-11-18 – FERTIG: Teil 2 (Format für Expeditionen: README, Prüfskript, Beispiel „Handytarif“)

Kein App-Code, keine Migration. Darauf können die Inhalte-Chats für Expeditionen aufsetzen.

- **inhalte/README.md**, neuer Abschnitt „Expeditionen“ (am Ende): Dateien `inhalte/expeditionen/<klasse>-<name>.json` aus `inhalte/generatoren/expedition_<name>.py`;
  Felder `schluessel, klasse, titel, einleitung, grafik?, voraussetzungen[{thema_schluessel, lernziel}], teile[3–5], autor?`;
  je Teil die Felder einer Bordkarte (`k, y, f, a, o, c, w, h?`) und `bezug {thema_schluessel, lernziel}`; Regeln inkl. „kein Folgefehler-Domino“ (jeder Teil nennt seine Werte);
  vollständiges Beispiel im Wortlaut.
- **tools/inhalt_pruefen.py** prüft Expeditionen (erkennt sie am Ordner `expeditionen` oder am Feld `teile`; `--alle` nimmt sie mit): Pflichtfelder, Dateiname = schluessel = `<klasse>-<name>`,
  Voraussetzungen existieren (Thema und Lernkarte in `inhalte/themen/`), Plan-Klasse jedes Voraussetzungs-Themas ≤ Klasse der Expedition, Bezug jedes Teils in den Voraussetzungen
  (ungenutzte Voraussetzung = Hinweis), 3–5 Teile, keine doppelten Fragetexte/Kennungen, Antwortform je Typ wie bei Bordkarten, `c` Pflicht bei `zahl`/`luecken` und nachgerechnet.
  Gegenprobe mit absichtlich falschen Varianten (Klasse 9 als Voraussetzung, falsche Lösung, fremder Bezug, 1 Teil, doppelter Text, unbekanntes Thema) – alle erkannt. `--alle`: 96 von 96 OK.
- **Beispiel** `inhalte/expeditionen/8-handytarif.json` (Generator `inhalte/generatoren/expedition_handytarif.py`), Voraussetzungen funktionen.linear/aufstellen, funktionen.linear/graph_ablesen,
  gleichungen.ungleichungen/sachaufgabe, bruch.prozent_grundwert/vermehrt:
  a) Term für Tarif A in Cent (Lücken `□x + □` → 10x + 500) · b) Welcher Graph gehört zu A? (Koordinatensystem mit 3 Geraden: richtig, Minutenpreis halbiert, Grundgebühr vergessen) ·
  c) Ab wie vielen ganzen Minuten ist B (12 € Flat) günstiger? → 71 · d) B wird 15 % teurer (13,80 €) → 89. Jeder Teil nennt die nötigen Werte.
- **Nicht geprüft:** wie die App die Grafik von Teil b zeichnet (kommt mit Teil 4); dass Folgeteile ohne Vorteil lösbar sind, prüft das Skript nicht mechanisch (Regel in der README).

## 2026-11-17 16:50 – FERTIG: Teil 1 (P1 Punkteregel „gelandet“ ohne Minuspunkte) – App 0.76.0 – wartet auf Migration

**Migration** `supabase/migrations/20261118_w176_t1_punkteregel.sql` (nicht ausgeführt; pglast ok; Ersetzungsstellen im Live-Text je einmal vorhanden; kein DROP, kein DELETE).
- `schule.karte_stand` neu: `eigene_loesungen int`, `typen text[]`, `folge int`, `fehler_folge int`, `stufe_senkung smallint` (alle mit Standardwert, nicht null).
- `schule.karte_buchen` neu gefasst (Regel siehe unten); neue Funktionen `schule.karte_typen_noetig(einheit, lernziel)` und `schule.karte_sicher(karte_stand)`.
- **Entscheidung `serie`:** bleibt als Spalte und wird weiter geschrieben als `least(eigene_loesungen, ziel)`. Die alte App 0.75.1 läuft damit ohne Fehler weiter
  (zeigt Punkte, wird nie weniger). Einziger sichtbarer Unterschied bis zum Wechsel: volle Punkte, aber noch nicht „sitzt“, solange Typen oder Folge fehlen.
- **Bestandsübernahme** (einmalig, nur Zeilen, die noch nicht übernommen sind): `eigene_loesungen = serie`, `folge = least(serie, 3)`, `typen` aus `schule.versuch`
  (richtig, 1. Versuch, ohne Tipp, mit `aufgabe.typ`). `sitzt` wird nicht angefasst → sitzende Etappen bleiben sitzend.
  Zahlen heute (gelesen): 31 Karten-Stände, davon 28 sitzend, Summe `serie` 73. Nach der Migration erwartet: 28 sitzend, Summe `eigene_loesungen` 73 (Rauchtest gibt beide Zahlen aus).

**Regel „gelandet“** (`sitzt = true`): eigene_loesungen ≥ ziel · Typen ≥ `karte_typen_noetig` (2, wenn die Etappe ≥ 2 Typen hat) · `schwer_ok` (Stufe-3-Typ), wenn nötig · `folge ≥ min(3, ziel)`.
Eigene Lösung: +1, folge +1, fehler_folge 0, stufe_senkung −1. Endgültig falsch: folge 0, fehler_folge +1, nach je 2 Fehlern in Folge stufe_senkung +1 (höchstens 2). Tipp/2. Versuch richtig: nichts.
Wiederholung unverändert (1/3/7/14/30 Lerntage); zwei Fehler in der Wiederholung → wieder offen, Belege bleiben, es fehlen wieder 3 in Folge (vorher: Punkte auf 0).
**„sicher“** = gelandet + `wdh_stufe ≥ 4` (Wiederholung nach 14 Lerntagen bestanden) + Nachtest des Flugs bestanden; die Mischkarte kommt mit Teil 3 dazu.

**Neue Felder für die App:** `schule_uebung_pruefen.karte` und `schule_einheit_lesen.etappen_stand[lernziel]`: `eigene_loesungen, folge, folge_ziel, typen_anzahl, typen_noetig, fehler_folge, stufe_senkung, sicher`;
`schule_lernstand.karten[]`: `eigene_loesungen, folge, typen_anzahl, sicher`. Keine neue Aktion in lernen-api.

**App 0.76.0** (läuft ohne Migration wie bisher, mit Punkten):
- Satz „Ein Fehler kostet 2 Punkte“ gestrichen; nach einem Fehler steht „Die nächste zählt wieder voll.“ (beide Gestaltungen).
- Statt Punkten eine Checkliste: „Eigene Lösungen 4/6 · 2 Aufgabentypen ✓ · schwere ✓ · 3 in Folge: 1/3“; daneben „heute X Aufgaben selbst gelöst“ (Zähler je Kind und Tag auf dem Gerät, ohne Bezug zur Schwelle).
- Stufenwahl: nach eigenen Lösungen, minus `stufe_senkung`.
- Landung: „GELANDET“ bleibt, Zusatz „Sicher wird die Etappe, wenn du sie in ein paar Tagen wieder kannst.“; „Sicher!“ beim Üben einer sicheren Etappe.
- Eltern: „Was wackelt?“ zeigt „gelandet“/„sicher“ und je offener Etappe „x eigene Lösungen · y in Folge · z Arten von Bordkarten“; Lernstand-Zellen „gelandet – nach N Bordkarten“.
- Info-Seite („Etappe gelandet“, „Etappe sicher“, Wiederholung) und `inhalte/README.md` (Abschnitt „Lernregel ‚gelandet‘ und ‚sicher‘“). Nirgends mehr „−2“ oder „Punkte verlieren“ (Test prüft den Quelltext).

**Rauchtest** (nach dem Einspielen, Transaktion mit Rollback, nur Testkind): `supabase/tests/w176_t1_rauchtest.sql` – Fälle: 6 richtige mit nur einem Typ → nicht gelandet ·
letzte falsch → nicht gelandet, folge 0, keine Abzüge · Tipp-Treffer zählt nicht und bricht die Folge nicht · danach 3 in Folge → gelandet · 1 Fehler senkt nicht, 2 in Folge senken um 1 ·
Etappen mit wenigen Übungen (Hinweis) · Knobel zählt nicht · Bestandszahlen (sitzend, Summe serie/eigene).

**Tests:** lernen 55 von 55 (neu: Checkliste/„heute“/„Die nächste zählt wieder voll.“, Stufensenkung + kein Minuspunkt-Text, gelandet/sicher für Kind und Eltern). Suche: 9 bekannte alte Fehler.
**Nicht geprüft:** die Migration gegen echte Daten (Rauchtest erst nach dem Einspielen); der Zähler „heute“ zählt nur auf dem Gerät des Kindes.

