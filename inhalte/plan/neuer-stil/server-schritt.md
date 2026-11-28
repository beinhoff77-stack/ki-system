# Neuer Stil – Server-Schritt VTEST-S („Verstehen in Tests“, Server)

Stand 29.11.2026, Zweig `helfer-vtest-s`. **Nichts eingespielt.** Gebaut nach den Entscheidungen des Nutzers vom 28.11. (Hälfte Verstehen, Test gleich lang = eine Aufgabe je Etappe, Verstehen falsch → neue Verstehens-Aufgabe, Landung erst mit ≥ 1 richtiger Verstehens-Aufgabe nur für nie gelandete Etappen, keine Fairness-Regel).
Dateien: Migration `supabase/migrations/20261212_vtest_s.sql` (= Einspiel-Paket, byteidentisch), Pakete `tools/tests/aus/vtest_s_probe.sql` / `vtest_s_einspielen.sql`, Erzeuger `tools/tests/vtest_s_einspielen.py`, Nachbau `tools/tests/vtest_s_nachbau.py`, Test `tools/tests/vtest_s_test.py`.
Kürzel: NF-S = `supabase/migrations/20261208_nf_s_nachtest_freigegeben.sql`, FT-S = `…/20261203_ft_s_form_takt.sql`, LB-3 = `…/20261120_lb3_nachbesserung.sql`, TEMPO = `…/20261207_tempo_s1.sql`. V = Verstehens-, R = Rechen-Aufgabe.

---

## 1. Ist-Zustand: Was die heutigen Funktionen garantieren, sobald die vtest-Aufgaben eingespielt sind

**Wie erkennt der Server „Verstehen“?** Gar nicht – keine Funktion fragt heute nach einer Art. Kennzeichnung der vtest-Pakete: `aufgabe.typ` (aus Feld `typ`/`g`, über `aufgaben_einfuegen`, `x->>'g'`) und `aufgabe.form` (FT-S Abschnitt 1, 6). Das Prüfwerkzeug erzwingt für jede vtest-Aufgabe `typ` ∈ begruenden, fehler, darstellung, parameter, umkehr, rueckwaerts, transfer **oder** `form` ∈ fehler_detektiv, verfahren_waehlen, zwei_wege, bruecke, umkehren, viele_antworten (`tools/vtest_pruefen.py` Z. 59–60, Regel V5 Z. 243). Alle alten Test-/Korrektur-/Sicherungs-Aufgaben haben weder `typ` noch `form` (`bestand.md` Abschnitt 0) → gelten als R. `variante_gruppe` = Lernziel (Etappe); `teilfaehigkeit` trägt keine Art.

| Stelle | Heutige Auswahl (Fundstelle) | Folge mit den vtest-Aufgaben |
|---|---|---|
| **Flugtest** (erster Blocktest) | **alle** freigegebenen `test`-Aufgaben der Einheit, `order by reihenfolge` (NF-S Z. 157) – kein Zufall, keine Art, keine Etappe | Eine Aufgabe je Etappe **nur**, weil `tools/vtest_sql.py` die alte R-Testaufgabe jedes V-Lernziels sperrt (Z. 15, Z. 327) und das prüft (Z. 150). Ohne Sperre (oder bei einem zurückgestellten Lernziel, dem die V dann aber fehlt) zöge der Server beide. „Hälfte Verstehen“ entsteht nur durch die Auswahl der Lernziele in den Paketen (⌈n/2⌉, `vtest_pruefen.py`), nicht im Server. Anzeige: erst alle R, dann alle V (V-Plätze `max_r + 80000 + …`), nicht abwechselnd. |
| **Nachtragstest** | je offene Etappe 1 ungesehene, erst `test`, dann `korrektur`, je nach `reihenfolge` (NF-S Z. 145–149) | V-Lernziel: die V-Testaufgabe (alte gesperrt); schon gesehen → V-Korrektur (negative Plätze). Ist die alte R nicht gesperrt, kommt R zuerst. |
| **Korrektur** | je Etappe mit Status `fehler` die erste **ungesehene** `korrektur`-Aufgabe nach `reihenfolge` (NF-S Z. 178–184); ohne ungesehene → „Vorrat erschöpft“ | „Gleiche Art“ nur zufällig über die Platznummern: V-Lernziel bekommt immer zuerst V (auch wenn eine R-Nachtestaufgabe falsch war); nach 2–3 V-Korrekturen kommt R, auch wenn Verstehen falsch war (`vtest-1/plan.md` „Was NICHT garantiert ist“ 1–2). Welche Aufgabe falsch war, wird nicht angesehen. |
| **Nachtest** | je Etappe `nachtest_je_etappe` Aufgaben aus `sicherung`: ungestellte zuerst, dann am längsten her, dann `reihenfolge` (NF-S Z. 60–70) | „Verstehen zuerst“: ja, aber nur durch die negativen Plätze – die ersten 3 Runden eines V-Lernziels V, danach R. Kein „halb/halb“ (bleibt so; nicht Teil dieses Schritts). |
| **Landung beim Üben** | `karte_landet` (LB-3 Z. 24 + FT-S Z. 152–154): eigene Lösungen ≥ Ziel, Typen, schwere, 3 in Folge, Sachaufgabe nur mit Schalter; aufgerufen von `karte_buchen` (`if not v_war_gelandet and schule.karte_landet(k)`, LB-3 Z. 175) | Keine Verstehens-Regel. |
| **Aufgabenwahl beim Üben** | trifft **die App** (`lernen.js` `lernWaehleBordkarte`/`lernWaehleKern`, aus `einheit_lesen_intern`), nicht der Server (`inhalte/plan/fehlerkarten.md` Abschnitt 2, „Aufrufer der Auswahl“). Der Server wählt nur Wiederholung/Mischkarte gelandeter Etappen (`wdh_aufgabe_waehlen`, FB-S). | Eine Landungs-Pflicht im Server kann die App nicht „sehen“, solange sie die Felder nicht liest → Abschnitt 4. |

**Bewertung im Test** (`test_abschliessen_intern`, `test_antwort_intern`): Grundfassung nicht im Repo (`bestand.md` c). Dieser Schritt ändert sie nicht; die Art der falschen Aufgabe wird aus `versuch` (mit `testsitzung_id`) und `testsitzung.aufgaben` gelesen.

## 2. Was gebaut ist (nur bei eingeschaltetem Schalter; Schalter 0 = genau das bisherige Verhalten)

**Klasse V** (`schule.aufgabe_verstehen(a)`): `typ` ∈ V-Typen oder `form` ∈ V-Formen (genau die Listen des Prüfwerkzeugs, im Test verglichen), nie `lueckenweg`. Ohne `typ`/`form` = R.

**Schalter** (`schule.regel`, beim Einspielen 0, ein vorhandener Wert bleibt): `verstehen_test_an` (Tests, a + b) und `verstehen_landung_an` (Üben, c) – je **0 aus · 2 nur Testkind (`lernender.ist_test`) · 1 alle**. Getrennt, weil (a)/(b) ohne App-Änderung gehen, (c) erst mit App (Abschnitt 4).

**(a) Test zieht in Verstehens-Etappen die Verstehens-Testaufgabe** (`test_starten_intern`). Verstehens-Etappe = Etappe mit einer freigegebenen V-Aufgabe im Pool `test`.
- Erster Flugtest: je Verstehens-Etappe **genau eine** V-Testaufgabe (die erste nach `reihenfolge`), ihre R-Testaufgaben entfallen – auch wenn die alte nicht gesperrt ist. Andere Etappen wie bisher (alle ihre Test-Aufgaben). Reihenfolge nach Etappen (`einheit.inhalt.etappen`), in der Etappe nach `reihenfolge` → R und V wechseln so, wie die Etappen gewählt sind. Etappen, die nicht in `inhalt.etappen` stehen, ans Ende.
- Nachtragstest: in einer Verstehens-Etappe zuerst eine ungesehene V-Aufgabe (erst `test`, dann `korrektur`), sonst wie bisher (nie „Vorrat erschöpft“ wegen der Art).
- Nachtest: **unverändert** (siehe Abschnitt 1).

**(b) Korrektur gleicher Art** (`test_starten_intern`, Korrektur-Zweig; neue Hilfe `schule.verstehen_korrektur_art`). Gesuchte Art = Art der falschen **oder unbeantworteten** Aufgabe(n) dieser Etappe in der **letzten abgeschlossenen Testsitzung** des Kindes in dieser Einheit, die die Etappe enthielt (Flugtest, Nachtrag, Korrektur oder Nachtest). Ist dort V falsch (auch wenn zugleich R falsch) → V, sonst R; nichts gefunden → wie bisher.
Auswahl aus dem Pool `korrektur` (freigegeben), definierter Rückfall:
1. ungesehen und gleiche Art (nach `reihenfolge`);
2. **nur wenn Verstehen gesucht:** eine schon gestellte V-Korrektur dieser Etappe, die am längsten her ist (statt einer Rechenaufgabe; **offene Frage 1**);
3. ungesehen, andere Art (= heutiges Verhalten, z. B. R falsch und nur noch V da → V);
4. sonst „Vorrat erschöpft“ wie heute.
Stufe: Korrektur-Aufgaben sind laut Auftragsblatt Stufe 2; es wird **keine** Aufgabe aus einem anderen Pool oder einer anderen Stufe als Ersatz geholt.

**(c) Landung erst mit Verstehen** (`karte_landet` + eine Bedingung; Hilfen `karte_verstehen_noetig/_pflicht/_ok`). Eine Etappe landet nur, wenn unter den **gezählten** Aufgaben (`karte_stand.gezaehlt`: selbst gelöst, ohne Tipp, 1. Anlauf) eine V-Aufgabe ist – aber nur, wenn
- der Schalter für dieses Kind an ist,
- die Etappe **nie gelandet** ist (`sitzt_am` leer, nicht `sitzt`): gelandete, wieder geöffnete und gesetzte („Kann er“) bleiben wie bisher; Rücknahme/Rückgängig unverändert,
- die Lernkarte eine **freigegebene, zählende V-Übung** hat (sonst entfällt die Pflicht; gesperrte V-Übungen und Lückenwege zählen nicht).
Kein Festhängen (Server): Jede V-Übung kann jederzeit wieder gestellt und dann gezählt werden (`karte_buchen` zählt jede Aufgabe einmal, sobald sie selbst gelöst ist – auch nach einem früheren Fehler oder Tipp). Getestet: ein Kind, das alle Übungen einmal selbst löst, landet jede Etappe. Ein früher gelöstes V zählt mit. Schalter wieder 0 → die nächste Antwort landet wie bisher.
Nicht geändert: `karte_buchen`, `landung_zaehlen`, `wdh_aufgabe_waehlen`/`mischkarten` (FB-S), `nachtest_*`, `uebung_pruefen_intern`, Tests-Bewertung.

## 3. Pakete, Schutz, Einspielen

- Je geänderter Funktion genau zwei Zustände (prosrc-md5): `test_starten_intern` 7abcd291… (NF-S neu) → 059fb2fe…; `etappen_stand` 3f49198f… (TEMPO neu) → 9e594f54…; `karte_landet` 2c03a8f5… (LB-3 + FT-S, aus dem Repo nachgerechnet) → e7b94fe5…; 7 neue Hilfen fehlt → neu. Jeder Mischstand = Abbruch, kein Wiederanlauf. Der neue Text ist der alte plus Einfügungen (Test: Entfernen der Einfügungen ergibt den alten Text; jeder alte Auswahl-Befehl steht unverändert im `else`-Zweig von `if v_vt`).
- Voraussetzungen mit eigener Meldung: NF-S fehlt („erst NF-S“), TEMPO-S1 fehlt („erst TEMPO-S1“), FB-S fehlt (`wdh_aufgabe_waehlen` 79812f…, `mischkarten` b5674c… – „erst FB-S“). Bezug (unverändert, md5): `aufgabe_zaehlt`, `karte_anwenden_ok`, `karte_anwenden_pflicht`; `karte_buchen` muss die Landeregel genau einmal an der Stelle `if not v_war_gelandet and schule.karte_landet(k) then` rufen. Eigenschaften aller Funktionen gegen festes Soll; Besitzer/Rechte der ersetzten unverändert; neue Hilfen nicht für public/anon/authenticated.
- Vergleich mit Schalter AUS in je **einer** Anweisung: `etappen_stand` alt (Kopie in pg_temp) gegen neu für alle Kinder × Einheiten; `karte_landet` alt gegen neu für alle Karten und dieselben Karten als „nie gelandet“ – jede Abweichung = Abbruch. Danach Schalter AN nur in der Transaktion (nur Zahlen), Schalter zurück.
- Meldung Probe: `VTEST-S KURZ {…} PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt). VOLL {…}`; jeder Befund: `VTEST-S PROBELAUF NICHT bestanden …`. Einspielen: Hinweis `VTEST-S eingespielt KURZ {…}`, sonst `VTEST-S ABBRUCH …`. Zweitlauf: `"zustand": "neu -> neu …"`, nichts geändert.
- **Reihenfolge:** NF-S → TEMPO-S1 → FB-S → (vtest-Aufgabenpakete 1a/1b, beliebig davor oder danach – `tools/vtest_sql.py` nimmt jetzt beide Stände von `test_starten_intern` an) → VTEST-S Probe → VTEST-S Einspielen. Schalter danach von Hand (unten).
- **Lernpause: nicht nötig** (keine Tabellen-DDL, Schalter 0, Vergleiche je in einer Anweisung). Eine Pause von ein paar Minuten schadet nicht.
- KURZ-Bericht (Schalter AN, nur Zahlen): Flugtest-Aufgaben bisher/neu, Verstehens-Etappen, offene Korrekturen nach Art (V/R/unbekannt), Karten „landebereit bis auf Verstehen“ (diese würden mit Schalter 1 auf eine V-Aufgabe warten), Lernkarten ohne Verstehens-Übung (dort entfällt die Pflicht). VOLL: dazu Rückfälle der Korrektur je Fall, Etappen mit fehlendem Verstehen je Kind.

Einschalten (nach dem Einspielen):
- Tests: `update schule.regel set wert = '2'::jsonb where schluessel = 'verstehen_test_an';` (Testkind), später `'1'` (alle). Geht ohne App-Änderung.
- Üben: `verstehen_landung_an` erst auf 2/1, wenn die App Abschnitt 4 kann. Ausschalten jederzeit `'0'` – sofort wie vorher.

## 4. Was die App später tun soll (NICHT gebaut)

Der Server liefert, **nur wenn `verstehen_landung_an` für das Kind an ist**, in `etappen_stand[lernziel]` (kommt über `einheit_lesen_intern`/`merkheft` als `etappen_stand` an; `lernEtappen`, `lernRegelFelder` in `lernen.js`) zwei neue Felder:

| Feld | Bedeutung |
|---|---|
| `verstehen_noetig` (bool) | Diese Etappe braucht zum Landen noch eine gezählte Verstehens-Aufgabe (Schalter an, nie gelandet, Lernkarte hat freigegebene zählende V-Übung). `false` bei gelandeten/wieder geöffneten/gesetzten. |
| `verstehen_ok` (bool) | Unter den gezählten Aufgaben ist schon eine V-Aufgabe. |

Fehlen die Felder, ist der Schalter aus → alles wie bisher (genau wie `anwenden_noetig`). `uebung_pruefen_intern.karte` liefert die Felder **nicht** (Grundfassung nicht im Repo); sie liefert aber `gezaehlt` und `sitzt`.

Die App soll:
1. `lernRegelFelder`: `verstehenNoetig`, `verstehenOk` übernehmen, wenn vorhanden (wie `anwendenNoetig`).
2. Klasse V lokal: `typ` ∈ {begruenden, fehler, darstellung, parameter, umkehr, rueckwaerts, transfer} oder `form` ∈ {fehler_detektiv, verfahren_waehlen, zwei_wege, bruecke, umkehren, viele_antworten}, nie `lueckenweg`, `zaehlt ≠ nein`. Nach jeder Antwort `verstehenOk` = `gezaehlt` (aus `karte`) enthält eine V-Aufgabe der Etappe; `verstehenNoetig` bis zum Neuladen behalten (wird mit `sitzt` hinfällig).
3. Auswahl (`lernWaehleBordkarte`): neue Regel wie `lernAnwendenFehlt` – „alles für die Landung beisammen, nur Verstehen fehlt“ (`verstehenNoetig && !verstehenOk && !sitzt && eigene ≥ ziel && Typen && schwer && folge ≥ folgeZiel`) → eine ungelöste zählende V-Aufgabe, sonst eine noch nicht gezählte V-Aufgabe (≠ letzte; Verbot „kein Fehler-Detektiv direkt nach eigenem Fehler“ gilt weiter, notfalls ohne Verbot). Besser schon früher: solange `verstehenNoetig && !verstehenOk`, auf einem Nicht-Form-Platz V nicht ausschließen. Rangfolge neben „Sachaufgabe fehlt“: Sachaufgabe zuerst, wenn beides fehlt und eine Aufgabe beides ist (typ transfer), diese.
4. Anzeige: Checkliste „Verstehens-Aufgabe ✓/–“ und, wenn nur sie fehlt, „Noch eine Verstehens-Aufgabe bis zur Landung“.
5. Test-Ergebnis: `aufgabe_anzeige` liefert `typ`/`form` auch im Test → „Rechnen“/„Verstehen“ je Bordkarte anzeigbar (Klasse wie 2.); Text „Eine Bordkarte je Etappe“ bleibt richtig.
6. Tests: `tests/lernen-takt.test.cjs` um die Regel erweitern (Pflicht an/aus, Felder fehlen, nur V fehlt, kein Festhängen bei nur gelösten V).

## 5. Tests

`python3 -I tools/tests/vtest_s_test.py` – Teil 1 (Stand, Einfügungen, else-Zweige, Klasse V = Prüfwerkzeug, `vtest_sql.py` kennt den neuen Hash) und Teil 2 im lokalen Nachbau dreimal (Kollation C, ICU en-US, ICU de-DE): Schalter 0 und Schalter 2 für ein Nicht-Testkind = alle Fälle identisch zum alten Stand; Flugtest je Etappe eine, V statt R (auch ungesperrte R), Reihenfolge der Etappen; Nachtragstest; Korrektur gleicher Art, Wiederholung einer gestellten V bei leerem V-Vorrat, Rückfall R ohne V-Korrektur, „Vorrat erschöpft“ wie bisher; gesperrte Aufgaben nie; Landung mit/ohne V, Tipp und Lückenweg zählen nicht, gesperrte V-Übung → keine Pflicht, gelandete/wieder geöffnete bleiben, Testkind-Schalter, Schalter aus danach, kein Festhängen; Pakete: Probe (leer und mit Lernständen) rollt zurück, Einspielen, Zweitlauf, 8 Negativfälle je Probe/Einspielen, Mischstand, Gegenprobe (2 verdorbene Fassungen).
Grenze: Nachbau, nicht die echte Datenbank. `karte_landet` und die Bezugsfunktionen sind aus dem Repo nachgerechnet – weicht live ab, bricht das Paket mit dem Live-md5 ab (dann Live-Text lesen, nicht raten).

## 6. Offene Fragen an den Nutzer

1. **Verbessern, wenn keine neue Verstehens-Aufgabe mehr da ist.** Ein Kind hat die Verstehens-Aufgabe falsch, und alle Verbesserungs-Aufgaben zum Verstehen hat es schon einmal gehabt. Was soll kommen? (A) eine dieser Aufgaben noch einmal, die am längsten her ist – **so ist es jetzt eingestellt**; (B) eine Rechenaufgabe; (C) nichts – erst wenn neue Aufgaben geschrieben sind.
2. **Was zählt beim Üben als Verstehens-Aufgabe?** Eingestellt ist: auch Rückwärts-Aufgaben („Welche Zahl wurde gesucht?“) zählen als Verstehen (so wie bei den neuen Test-Aufgaben). Dann haben fast alle Etappen solche Aufgaben, und die neue Lande-Regel ist leicht zu erfüllen. Soll das so bleiben, oder sollen nur „Fehler finden / begründen / zwei Wege“ zählen (strenger, mehr Etappen ohne passende Aufgabe → dort gilt die Regel dann nicht)?
