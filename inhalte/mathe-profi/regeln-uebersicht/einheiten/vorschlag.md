# Vorschlag: Wo die Tafel „Einheiten umrechnen“ im Regel-Universum hingehört

Nur Vorschlag und Inhalte. Geändert wurden weder `daten/regeln-universum.json`, noch `tools/regeln_bauen.cjs`, noch bestehende Textdateien. **[G]** gesichert (im Repo belegt), **[A]** Annahme.

## 1 Befund [G]
- Die Tafel passt in keine der drei Ebenen: Sie ist keine Rechenregel (14), keine Idee (28) und keine Einzelregel (152), sondern ein Nachschlagewerk. Sie sollte deshalb **keine neue Regel-Nummer** bekommen und die Zählung 14 / 28 / 152 nicht verändern.
- Die Suche des Universums kennt `stichwoerter` als Liste `{wort, ziel}` (19 Einträge, `ziel` ist eine Kennung wie `R11`, `V8` oder „Arbeitsweise Probe“). Zum Umrechnen gibt es dort heute kein Stichwort.

## 2 Ort [A, Empfehlung]
1. **Eigene Tafel mit Kennung `T-einheiten`**, im Gebiet „Geld und Verhältnisse“ an die Idee „Größe“ (`I-geld-1`, `id.verhaeltnisse.groesse`) gehängt: auf der Seite der Idee ein deutlicher Knopf „Einheiten umrechnen (Tafel)“, auf der Tafel oben die Richtungsregel der Idee („Kleinere Einheit, größere Zahl – größere Einheit, kleinere Zahl.“).
2. **Von dort verlinkt**: V1 (Größe und Einheit), F1 (Fläche messen), F11 (Volumen messen), beim Lernkarten-Thema `groessen.einheiten` und bei `messen.flaechen` / `messen.volumen` (je ein Satz „Alle Umrechnungen: Tafel“).
3. **Über die Suche** direkt erreichbar (Liste in Abschnitt 3). Ein Kind, das „cm in m“ eintippt, soll ohne Umweg auf der Tafel landen.
4. Verworfen: V1 selbst erweitern (zu lang für den Ein-Satz-Stil der Einzelregeln, vgl. Grenzen in `texte8/README.md`); Tafel als Rechenregel 15 (würde die Zählung 14 und die Schichten-Logik sprengen).

## 3 Stichwörter für die Suche (alle → `T-einheiten`)
umrechnen · Einheiten umrechnen · Einheit · Einheiten · Umrechnungszahl · Umrechnungstabelle · Einheitentafel · Maßeinheiten · Größen · Länge · km · m · dm · cm · mm · Kilometer · Meter · Zentimeter · Millimeter · Fläche (Einheiten) · m² · cm² · Hektar · ha · Ar · Quadratmeter · Volumen (Einheiten) · m³ · cm³ · Kubikmeter · Liter · Milliliter · ml · Hektoliter · hl · Masse · Gewicht · Tonne · kg · g · mg · Kilogramm · Gramm · Zeit umrechnen · Stunde · Minute · Sekunde · h · min · s · Euro · Cent · Geld umrechnen · km/h · m/s · Geschwindigkeit · Tempo · 3,6 · Dichte · g/cm³ · kg/m³

Hinweis [A]: Bei den Kurzzeichen (m, g, s, h, l) sollte die Suche nur auf ganzes Wort passen, sonst trifft „m“ fast jeden Eintrag.

## 4 Was an V1, F1, F11 gekürzt oder verlinkt würde (nur Vorschlag)
| Eintrag | Heute (Bestand) | Vorschlag |
|---|---|---|
| V1 | Satz mit sieben Umrechnungen (km, m, cm, mm, kg, g, mg, h, min, d) | Satz kürzen auf „Eine Größe ist Zahl mal Einheit. Kleinere Einheit, größere Zahl.“ und anfügen „Alle Umrechnungen: Tafel“. Beispiel und Grenze zur Zeit bleiben. |
| V1, Grenze | „Bei Flächen (Klasse 6) ist der Faktor … 100“ | **Klasse prüfen**: F1 und das Thema `messen.flaechen` führen Flächeneinheiten für Gymnasium und Realschule in Klasse 5 (Zweifelsfall 1). |
| F1 | Satz: „… zehnmal kleiner, braucht man 100-mal so viele.“ | Satz bleibt (er erklärt den Grund); anfügen „Treppe km² bis mm²: Tafel“. |
| F11 | Satz mit 1 000-mal und „1 Liter = 1 dm³“ | Satz bleibt; „1 Liter = 1 dm³“ bleibt wegen der Wichtigkeit; anfügen „Auch ml, hl und m³: Tafel“. |
| Idee „Größe“ (`I-geld-1`) | Merksatz zur Richtung | unverändert; Tafel als „Nachschlagen“-Knopf. |

## 5 Was der Bau später braucht
1. **Datenquelle:** `einheiten.json` (hier) als Eingabe für `tools/regeln_bauen.cjs`; neuer Schlüssel in `daten/regeln-universum.json`, z. B. `tafeln: [{id: "T-einheiten", ...}]`. Die Felder sind bewusst flach gehalten (je Größenart `treppe` als Liste, `beispiele`, `stolperstellen`).
2. **Anzeige:** eine Treppe als Folge von Kästchen mit Pfeil und Zahl (`km –1 000→ m`) und drei Zustände je Größenart (Treppe, Beispiele, Fehler); Kinder-Tonfall bleibt „du“. Tabelle muss auf dem Handy ohne Querwischen lesbar sein (Flächen-Treppe hat sieben Stufen).
3. **Suche:** Einträge in `stichwoerter` mit `ziel: "T-einheiten"`; Test, dass jedes Stichwort aus Abschnitt 3 dort landet.
4. **Zählung:** `assert.deepEqual([…], [14, 4, 7, 28, 8, 25, 30, 42])` im Bau bleibt unverändert, solange die Tafel nicht als Regel gezählt wird; neue Zahl `tafeln: 1` getrennt führen.
5. **Prüfung:** `python3 -I inhalte/mathe-profi/regeln-uebersicht/einheiten/pruefen.py` endet mit OK; sie rechnet jede Gleichung und jedes Beispiel exakt nach, gleicht Klassen, Lernziele, Einheiten und Kennungen mit dem Bestand ab und prüft `tafel.md` gegen `einheiten.json`.
6. **Schreibweise beim Anzeigen:** Der Bestand nutzt ein gewöhnliches Leerzeichen als Tausendertrenner und vor der Einheit. Damit „3 500 m“ am Zeilenende nicht getrennt wird, sollte die Anzeige ein geschütztes Leerzeichen setzen (nur beim Darstellen, nicht in den Daten) [A].
7. **Offene Bausteine:** Die Verweise `regeln` (Kennungen) setzen in der Anzeige Links; `ab_klasse` kann den Klassenfilter der Seite füttern (Gymnasium/Realschule/IB getrennt).

## 6 Zweifelsfälle
1. V1 sagt bei Flächen „Klasse 6“, F1 und `messen.flaechen` sagen Klasse 5 [G]. Die Tafel folgt dem Lernkarten-Thema (Klasse 5).
2. `ab_klasse` ist für Geschwindigkeit und Dichte **leer**: Der Bestand hat dafür keine Lernkarte zur Umrechnung. m/s nach km/h kommt nur als Aufgabe im Thema `gleichungen.formeln` (Gymnasium Klasse 8) vor, Dichte als Formel (ρ = m : V, Klasse 8) und in Körperaufgaben (Gymnasium Klasse 10, Realschule Klasse 9). Die Tafel nennt diese Vorkommen unter `vorkommen_im_bestand`.
3. hl, dl, cl sind nicht im Bestand und als „zusatz“ markiert; ebenso kg/m³. Die Lernkarten kennen nur l und ml. Entscheidung: drin lassen oder streichen.
4. Winkel und Temperatur sind bewusst nicht aufgenommen (Begründung in `einheiten.json`, Feld `nicht_aufgenommen`).
5. Woche, Monat und Jahr stehen nur als Hinweis bei Zeit; „1 Jahr = 365 Tage“ nur mit dem Zusatz „ohne Schalttag“.
