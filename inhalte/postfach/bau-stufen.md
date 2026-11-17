# Postfach bau-stufen (Bau-Chat, Bau-Auftrag F)

Neueste oben.

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
