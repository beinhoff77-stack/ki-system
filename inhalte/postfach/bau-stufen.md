# Postfach bau-stufen (Bau-Chat, Bau-Auftrag F)

Neueste oben.

## 2026-11-17 16:20 – FERTIG: Teil 2 fertig (App) – App 0.75.0 – wartet auf Migration F

Die App läuft ohne Migration F wie bisher (ohne typ: Abwechslung nach Fragetext ohne Zahlen; ohne bonus/knobel_tag/knobel_sterne: nichts davon sichtbar).

**Kinderansicht**
- **Stufenzeichen** im Kopf jeder Bordkarte: ● leicht · ●● mittel · ●●● schwer, mit Text für Vorleser („Stufe: mittel“), ohne Rot und ohne „zu schwer“; Knobel: „★ KNOBEL“.
- **Abwechslung** (`lernWaehleBordkarte`, vorher `waehleStufe`): innerhalb der Ziel-Stufe nie zweimal hintereinander derselbe Typ (ohne typ: nie zweimal derselbe Fragetext nach Ersetzen der Zahlen),
  Typen, die in dieser Etappe noch nicht dran waren, zuerst. Die schwere Bordkarte für „sitzt“ bleibt Pflicht; mit Typen zählt nur ein Stufe-3-Typ (nie knobel).
- **Knobel-Bordkarte:** Sitzt eine Etappe und hat sie Bonus-Bordkarten, bietet die Landung „★ Knobel-Bordkarte (freiwillig)“ an. Ein Versuch, Tipp möglich; falsch kostet nichts und zeigt
  Lösung und Weg; richtig im ersten Versuch: „+30 Sterne · ein Knobel-Stern“. Kein zweiter Anlauf, kein Einfluss auf Punkte, „sitzt“, Wiederholung oder Test (die App schickt kein `anlauf`/`hilfe`).
- **Knobeln des Tages** auf der Abflugtafel aus `schule_konto.knobel_tag`, höchstens einmal je Lerntag (Server: null, wenn heute schon geknobelt; App merkt sich den Tag zusätzlich).
- **Reisepass:** „★ Knobel-Sterne: n“ (aus `konto.knobel_sterne`), mit Erklärung.

**Eltern/Lehrer**
- „Inhalte ansehen“: je Bordkarte Stufe und Art (z. B. „schwer · rückwärts“), Knobel-Bordkarten als „★ Knobel · freiwillig“.
- Lernstand: je Etappe „Knobel: x von y“.
- Info-Seite: „Drei Stufen = drei Arten zu denken“ und „Knobel-Bordkarten“ (freiwillig, 30 Sterne), Belohnungen ergänzt.

**Tests:** lernen 51 von 51 (neu: Stufenzeichen, Auswahl ohne gleichen Typ hintereinander / neue Typen zuerst / Schwer nur mit Stufe-3-Typ, Knobel nach der Landung mit 30 Sternen und ohne Einfluss auf „sitzt“,
Knobel falsch, Knobeln des Tages einmal je Tag, Knobel-Sterne, Eltern-Ansichten). Suche: die 9 bekannten alten Fehler (W132 schwankt, einzeln grün).

**Nach dem Einspielen der Migration** prüfe ich die echte Antwortform (aufgabe_anzeige typ/bonus, einheit_lesen bonus, uebung_pruefen bei Bonus, konto knobel_sterne/knobel_tag, lernstand knobel_*).
Kein Merge nach main oder lernen-app von mir.

## 2026-11-17 14:40 – FERTIG: Teil 1 fertig (README, Prüfskript, Migration als Datei)

Darauf können die Inhalts-Chats der „Zwanzigsten Runde“ aufsetzen, sobald Teil 1 nach lernen-app zusammengeführt ist.

**inhalte/README.md** – neuer Abschnitt „Stufen und Aufgabentypen“: Feld `g` (Typ je Stufe, je Typ ein Satz und ein Beispiel), Regel „Die Stufe folgt aus dem Typ, nicht aus der Größe der Zahlen“,
Prüfregeln, Pool `bonus` (Knobel-Bordkarte). Tabelle der Aufgabenfelder um `g` und `bonus` ergänzt; Qualitätsmaßstab Stufe 3 angepasst.

**tools/inhalt_pruefen.py**
- `g` freiwillig. Mit `g`: unbekannter Typ = Fehler; Typ passt nicht zur Stufe = Fehler; `knobel` nur im Pool `bonus`.
- Haben alle Übungen einer Lernkarte `g`: weniger als 2/3/4 verschiedene Typen auf Stufe 1/2/3 = Fehler; mehr als 2 Aufgaben desselben Typs je Stufe mit gleichem Satzbau
  (Fragetext nach Ersetzen aller Zahlen gleich) = Fehler.
- Hinweis für alle Lernkarten: Übungen je Stufe mit `g` / ohne `g`; „gleich gebaut hintereinander“ (3 oder mehr Übungen derselben Lernkarte in Folge mit gleichem Fragetext ohne Zahlen).
  Am Ende je Datei: „Gruppen ‚gleich gebaut hintereinander‘: n“ (auch im Info-JSON als `gleich_gebaut_hintereinander`, dazu `mit_typ`, `bonus`).
- Pool `bonus`: höchstens 3 je Lernkarte, nur Typ `knobel`, Stufe 3, Tipp `h` Pflicht; Mindestmengen der anderen Pools unverändert.
- Gegenprobe: `--alle` meldet weiter 92 von 92 OK (keine neuen Fehler für alte Dateien); heute 549 Gruppen „gleich gebaut hintereinander“ über alle Themen.
  Neue Regeln an einer Probedatei geprüft (falscher Typ, Typ zur falschen Stufe, Bonus ohne knobel, 4 Bonus-Bordkarten).

**Migration `supabase/migrations/20261118_w150_f_stufen_typ_bonus.sql`** (nicht ausgeführt; pglast ok; alle Ersetzungsstellen im Live-Text vorhanden, nur gelesen)
- `schule.aufgabe.typ text` mit Prüfbedingung (Liste der Typen); Bonus nur mit typ knobel und Stufe 3.
- **Ausnahme von „kein DROP“, bitte bewusst einspielen:** `aufgabe_pool_check` (um `bonus`) und `sterne_grund_check` (um `bonus`) werden ersetzt – in Postgres nur als
  `drop constraint … , add constraint …` in einem Befehl; keine Daten betroffen. Kein DROP von Tabellen, Spalten, Funktionen, kein DELETE.
- `schule.regel` `sterne_bonus_richtig` = 30.
- `aufgaben_einfuegen` und `einheit_abgleichen`: `a->>'g'` → `typ`, beim Abgleich auch für vorhandene Aufgaben mit gleicher Frage; Pool `bonus` mit art `uebung`.
  Weiter gilt: Aufgaben freigegebener Einheiten schützt `aufgabe_schutz` – dort scheitert ein Abgleich wie bisher.
- `karte_buchen` bucht nur `pool = 'uebung'` (geprüft) → Bonus zählt nicht für „sitzt“/Wiederholung. Die schwere Bordkarte für „sitzt“ verlangt bei vorhandenem `typ` einen Stufe-3-Typ.
- `sterne_aus_versuch`: Bonus richtig im ersten Versuch = 30 Sterne (Grund `bonus`, je Aufgabe einmal); falsch oder später richtig = nichts. Übungen wie bisher.
- **Felder für die App:**
  - jede Bordkarte (`aufgabe_anzeige`): `typ`, bei Bonus `bonus: true`
  - `schule_einheit_lesen`: `bonus: [ … , versuche, geloest, geloest_erst ]`
  - `schule_uebung_pruefen` nimmt Bonus-Bordkarten an: `{ richtig, bonus: true, erster_versuch, sterne, knobel_sterne, loesung, loesungsweg }`, kein „nochmal“, kein `karte`
  - `schule_konto`: `konto.knobel_sterne`, `knobel_tag` (eine Knobel-Bordkarte aus einer sitzenden Etappe, je Tag fest; null, wenn heute schon geknobelt)
  - `schule_lernstand`: je Etappe `knobel_gesamt`, `knobel_geloest`
  - `schule_inhalt_lesen`: je Aufgabe `typ`
  Keine neue Aktion in lernen-api nötig (alles über bestehende Aktionen).

Weiter mit Teil 2 (App).
