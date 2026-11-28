# Plan „Verstehen in Tests“ – Stufe 1 technisch

Stand 28.11.2026, Helfer Werkzeuge (Zweig `helfer-vtest`). Grundlage: `inhalte/plan/neuer-stil/` (bestand, didaktik, konzept, entscheidung) und die **Entscheidungen des Auftraggebers vom 28.11.** (unten E1–E8). Kennzeichen: **[B]** belegt (Fundstelle) · **[T]** im lokalen Nachbau getestet (`tools/tests/vtest_sql_test.py`, mit und ohne ICU) · **[A]** Annahme.

Entscheidungen: E1 Hälfte der Test-Aufgaben Verstehen · E2 Test bleibt gleich lang, eine Aufgabe je Etappe, abwechselnd R/V → V **statt** R · E3 R richtig / V falsch → Korrektur mit neuer V · E4 Üben: „gelandet“ erst mit ≥ 1 richtiger V (später) · E5 Start mit den 17 Einheiten in Arbeit · E6 keine Fairness-Regel (jede Bauart darf kommen) · E7 Tests schwerer: Stufe 2–3, keine Reproduktion · E8 kein Ersatz durch V anderer Schwierigkeit beim Üben (nicht wieder vorschlagen).

Gestrichen gegenüber `konzept.md` wegen E6: Form-Bekanntheit (`didaktik.md` 1.5, 6.1, 6.2, Schritt S3, „Fairness Alt-Etappen“ in der Risikotabelle). Gestrichen wegen E2: „1 R + 1 V je Etappe“ (Konzept B, Flugtest doppelt so lang). Wegen E7: „Keine Stufe 3 im Test“ (`didaktik.md` 6.4) gilt nicht mehr.

---

## 1. Wie Stufe 1 ohne Server-Änderung wirkt

Serverfassungen: `supabase/migrations/20261208_nf_s_nachtest_freigegeben.sql` (NF-S; das Paket verlangt genau diese drei Funktionstexte per md5).

| Stelle | Auswahl im Server [B] | Folge für Stufe 1 |
|---|---|---|
| erster Flugtest | **alle** freigegebenen `test`-Aufgaben der Einheit, `order by reihenfolge` (nf_s Z. 157) | Für jedes V-Lernziel wird die alte Rechen-Test-Aufgabe **gesperrt** (`freigegeben = false`) und die neue V-Aufgabe eingefügt → weiter genau 1 Aufgabe je Lernziel [T]. Reihenfolge: Rechen-Aufgaben zuerst (alter Platz), V-Aufgaben danach (Platz `max_r + 80000 + 1000·Block + Nr.`) [T]. |
| Nachtragstest | je offene Etappe 1 ungesehene, zuerst `test`, dann `korrektur`, nach `reihenfolge` (nf_s Z. 140–150) | V-Lernziel bekommt die neue V-Test-Aufgabe. |
| Korrektur | je Etappe mit Status `fehler` die erste **ungesehene** `korrektur`-Aufgabe `order by reihenfolge` (nf_s Z. 178–184) | Neue V-Korrektur-Aufgaben bekommen **negative** Plätze (`−100000 + 1000·Block + Nr.`) → stehen vor jedem Bestand und werden zuerst gezogen [T]. |
| Nachtest | je Etappe `nachtest_je_etappe` Aufgaben aus `sicherung`: `order by gestellt, zuletzt nulls first, reihenfolge, id` (nf_s Z. 61–70) | Neue V-Sicherungen ebenfalls negativ → unter den ungestellten zuerst [T]. Nach ihrem Verbrauch kommt der Rechen-Bestand (die Etappe wird also später auch wieder im Rechnen geprüft). |
| Rechen-Lernziele | – | völlig unverändert (keine neue Aufgabe, nichts gesperrt). |

Warum „je Lernziel eine feste Art“ statt Abwechseln innerhalb des Lernziels: Abwechseln über `reihenfolge` zwischen neuen V- und alten R-Sicherungen bräuchte freie Plätze **zwischen** den Bestandsplätzen (live unbekannt, ganzzahlig) und würde durch schon gestellte Aufgaben je Kind sofort verschoben. Das Abwechseln geschieht daher **über die Etappen** (E2): in jedem Test einer Einheit ist etwa jede zweite Etappe V. Das ist ohne Server-Änderung exakt steuerbar.

### Was Stufe 1 garantiert (ohne Server-Änderung)

1. Flugtest: genau **eine** Aufgabe je Lernziel; bei ⌈n/2⌉ Lernzielen ist es die neue V-Aufgabe (Stufe 2–3), sonst die bisherige R-Aufgabe [T]. Nie eine Etappe ohne freigegebene Test-Aufgabe (Nachprüfung im Paket: genau eine, die neue) [T].
2. **E3 im Hauptfall:** Ist im Flugtest (oder Nachtragstest) eine V-Aufgabe falsch, zieht die Korrektur dieses Lernziels eine **neue V-Aufgabe** – beim 1. und 2. Verbesserungs-Versuch (Menge 2), bei Menge 3 auch beim 3. [T für den 1.; Rückfall nach Verbrauch ebenfalls T].
3. Korrektur eines R-Lernziels bleibt R (Bestand).
4. Kein Kind bekommt für eine **schon falsche alte R-Aufgabe** eine V-Korrektur: Lernziele, die beim Einspielen bei irgendeinem Kind im Status `fehler` stehen, werden **zurückgestellt** (unberührt) und erst nach der Korrektur nachgeholt [T]. Ebenso Lernziele mit laufender Testsitzung, die die alte Aufgabe enthält [T].
5. Nachtest: V-Lernziele bekommen in den ersten Runden V-Sicherungen (bei 1 Aufgabe je Etappe: Runde 1–3 V), danach Rechen-Bestand; „Vorrat erschöpft“ wird durch die neuen Aufgaben nie häufiger (nur mehr Vorrat) [B nf_s Z. 68].
6. Lernstände werden nie verändert (Paket schreibt nur `aufgabe`, `aufgabe_regel`, `aufgabe_fehlbild`, `einheit` – xmin-Prüfung über das ganze Schema) [T].

### Was NICHT garantiert ist (Entscheidung 3 genau lesen)

1. **Korrektur nach einem Nachtest-Fehler:** Der Server schaut nicht, welche Art falsch war. Bei einem V-Lernziel kommt die nächste ungesehene Korrektur – V, solange vorhanden, sonst R; war die falsche Nachtest-Aufgabe eine R-Sicherung (nach Verbrauch der V), kommt trotzdem V.
2. **Nach Verbrauch der V-Korrekturen** (2 bzw. 3 Versuche) kommt beim selben Kind wieder Rechen-Korrektur [T].
3. Die Testanzeige trennt nicht „Rechnen ✓ · Verstehen ✗“ (kein Feld dafür; A1).
4. Reihenfolge im Flugtest: alle R zuerst, dann alle V – nicht „abwechselnd“ in der Anzeige (die Abwechslung betrifft die Etappen).
5. Bei Einheiten, deren Flugtest ein Kind schon gemacht hat (laut Liste nur bei `terme.umformen`, `terme.umformen_teil2`, `zahlen.natuerlich` für eines der Kinder), wirken die neuen Aufgaben in dessen **Nachtests und Korrekturen** (V vorn). Das ist mit E6/E7 gewollt, sei aber genannt.
6. Ob eine **gesperrte** Aufgabe in einer schon laufenden Sitzung noch bewertet wird, hängt an `test_antwort_intern` (Grundfassung nicht im Repo, `bestand.md` c). Deshalb: laufende Sitzungen → zurückstellen + Lernpause.

### Kleinstmögliche Server-Änderung für E3 genau (später, nur beschrieben)

**S1 „Korrektur gleicher Art“** – nur der Korrektur-Zweig von `schule.test_starten_intern` (nf_s Z. 178–184), eine Zeile `order by`:
```sql
order by (schule.aufgabe_ist_v(a) = coalesce((select schule.aufgabe_ist_v(f) from schule.versuch v join schule.aufgabe f on f.id = v.aufgabe_id
            where v.lernender_id = p_lernender and v.testsitzung_id is not null and f.einheit_id = v_einheit and f.variante_gruppe = r.lernziel and not v.richtig
            order by v.am desc, v.id desc limit 1), schule.aufgabe_ist_v(a))) desc, a.reihenfolge
```
mit einer neuen kleinen Funktion `schule.aufgabe_ist_v(a) = a.typ in ('begruenden','fehler','darstellung','parameter','umkehr','rueckwaerts','transfer') or a.form in ('fehler_detektiv','verfahren_waehlen','zwei_wege','bruecke','umkehren','viele_antworten')` (alte Aufgaben ohne typ/form = R). Wirkung: Die Korrektur nimmt zuerst eine ungesehene Aufgabe **derselben Art wie die zuletzt falsche Test-Aufgabe** dieses Lernziels, sonst wie heute (nie „Vorrat erschöpft“ wegen der Art). Damit sind Punkte 1 und 2 oben gelöst, soweit Vorrat da ist. Bau als selbstprüfendes Paket nach dem Muster NF-S (zwei zulässige md5-Zustände), danach neuer Soll-Hash in `tools/vtest_sql.py`. Aufwand [A] 3–4 h.

## 2. Stufenplan

| Stufe | Inhalt | Voraussetzung |
|---|---|---|
| **1 (jetzt)** | W1 `tools/vtest_sql.py`, W2 `tools/vtest_pruefen.py`, Test `tools/tests/vtest_sql_test.py`; Aufgaben für 65 V-Lernziele in 4 Runden (1a, 1b, 2, 3); Einspielen je Runde | NF-S live; Gegenprüfung je Runde; Satz des Nutzers |
| **2** | S1 (oben); A1 Ergebnis je Etappe mit Art „Rechnen/Verstehen“ (braucht `test_abschliessen_intern`, Grundfassung erst live lesen); T App-Text „Eine Bordkarte je Etappe“ bleibt richtig (E2) – nur Zusatz „Etwa jede zweite prüft Verstehen“ | Stufe 1 zwei Wochen live, Messung (konzept.md Abschnitt 7) |
| **3** | **E4**: Üben „gelandet“ erst mit ≥ 1 richtiger V-Aufgabe, nur für noch nicht gelandete Etappen: Schalter `verstehen_pflicht`, Patch `karte_landet` (wie Sachaufgaben-Pflicht FT-S Regel 6), App „Noch eine Verstehens-Aufgabe“ (`lernen.js` 466, 476–505) – **nach TEMPO-S1**; übrige Einheiten/Klassen beliefern | Stufe 2 bewährt |

Nicht mehr vorgesehen: S3 Form-Bekanntheit (E6), Form-Platz mit Nachbarstufe (E8).

## 3. Mengen

Je V-Lernziel (Begründung je Pool in `auftrag.md` Abschnitt 3):

| Pool | Konzept | Auftrag 28.11. | **Werkzeug: Mindestmenge / Empfehlung** | Begründung |
|---|---|---|---|---|
| test | 1 | 1 | **1 / 1** (genau) | E2; Flugtest zieht alle |
| korrektur | 2 | 2 | **2 / 3** | 1. Korrektur nach Flugtest-Fehler, 2. nach erneutem Fehler, 3. nach einem späteren Nachtest-Fehler – sonst fällt die 3. Korrektur auf R zurück (nicht garantiert 1/2) |
| sicherung | 3 | 3 | **3 / 3** | Nachtest-Runden 1–3 bei 1 je Etappe; bei Einheiten mit ≤ 4 Pflicht-Etappen (2 je Etappe: `terme.potenzgesetze`, `terme.umformen_teil2`, `daten.kennwerte` laut Repo) reichen 3 für 1½ Runden, danach R – gewollt halb/halb |

Je Runde (Lernziele = V-Lernziele; Aufgaben bei 1/2/3 bzw. Empfehlung 1/3/3):

| Runde | Einheiten | V-Lernziele | Aufgaben 1/2/3 | Aufgaben 1/3/3 |
|---|---|---|---|---|
| 1a | potenzen_basis, rechengesetze | 11 | 66 | 77 |
| 1b | prozent, gleichungen.bruch, potenzgesetze, potenzen_zehner, flaechen_vielecke | 17 | 102 | 119 |
| 2 | zinsen, umformen, umformen_teil2, kreis, natuerlich | 19 | 114 | 133 |
| 3 | volumen, darstellen, kennwerte, grundbegriffe, winkel | 18 | 108 | 126 |
| **Summe** | 17 | **65** | **390** | **455** |

Nachschreiben für die Empfehlung: je V-Lernziel 1 Korrektur-Aufgabe (Runde 1a/1b: 28). Das Werkzeug nimmt beide Mengen an; die nachgeschriebene Korrektur bekommt dann einen Platz hinter den beiden ersten – **nur wenn sie in derselben Runde und vor dem Einspielen dazukommt**. Nach dem Einspielen ändert ein Nachtrag den Gruppenzustand („Zwischenstand“, Abbruch) – dafür bräuchte W1 eine eigene Nachtrags-Runde (kleiner Ausbau, nicht gebaut).

## 4. Ausführung (Einspielen je Runde)

Reihenfolge: 1a und 1b getrennt (je ein Paket), Reihenfolge egal (verschiedene Einheiten, eigene Platz-Blöcke).

1. **Prüfen:** `python3 -I tools/vtest_pruefen.py --runde 1a` → `OK`; Gegenprüfung abgeschlossen; Satz des Nutzers liegt vor.
2. **Pakete:** `python3 -I tools/vtest_sql.py --runde 1a --pakete` → `tools/tests/aus/vtest1a_probe.sql`, `vtest1a_einspielen.sql` (md5 notieren, committen). Ein Paket = eine Datei, ein Aufruf, eine Transaktion, kein BEGIN/COMMIT; Ausführung wie bisher (Inhalt in **einem** `execute`).
3. **Voraussetzung:** NF-S eingespielt (sonst bricht das Paket mit „erst NF-S einspielen“ ab). Keine Prüfbedingung auf `aufgabe.reihenfolge` (sonst eigener Abbruch; dann melden – die negativen Plätze gingen nicht).
4. **Lernpause: ja**, von kurz vor dem Probelauf bis nach dem Einspielen (Minuten). Begründung: (a) eine im Augenblick des Einspielens **gestartete** Testsitzung bekäme noch die alte Aufgabe, die das Paket dann sperrt – das Paket nimmt zwar vor dem Sperren die Test-Start-Sperre aller Kinder (`pg_advisory_xact_lock(hashtext('schule_test'), Kind)`, wie `test_starten_intern`) und prüft danach erneut, aber eine schon geöffnete App-Seite mit altem Stand und `test_antwort_intern` (Grundfassung nicht im Repo) sind nicht prüfbar; (b) Mischkarten/erste Anläufe wie in der Bestands-Berichtigung.
5. **Probelauf:** `vtest1a_probe.sql`. Erwartet: Fehlermeldung, die **mit dem Bericht beginnt**, z. B.
   `VT1A BERICHT: Lernziele 11 (neu 11, schon fertig 0, zurückgestellt 0) | Aufgaben neu 66 (test 11, korrektur 22, sicherung 33) | alte Test-Aufgaben gesperrt 11 | Regeln …, Fehlbilder … | Einheiten geändert 2 | PROBELAUF bestanden, ALLES zurückgerollt …`
   Für 1b: `Lernziele 17 … Aufgaben neu 102 (test 17, korrektur 34, sicherung 51) … gesperrt 17 … Einheiten geändert 5`. (Bei Korrektur-Menge 3: 77/33 bzw. 119/51.) Fehlbilder = Summe der Fehlbilder der Runde (W1-Übersicht nennt die Zahl). Jede andere Meldung (`ABBRUCH …`) = nicht einspielen, Befund melden.
   „zurückgestellt k > 0“: diese Lernziele (Liste in den Einzelheiten) haben eine laufende Sitzung oder eine offene Korrektur; sie bleiben unberührt. Einspielen trotzdem möglich; später nochmals ausführen.
6. **Einspielen:** `vtest1a_einspielen.sql`. Erwartet: Hinweis mit denselben Zahlen und „eingespielt“; danach die Zählabfrage (je Einheit/Pool freigegeben/gesperrt): `test` gesperrt +11 (1a), `korrektur`/`sicherung` freigegeben + Soll.
7. **Zweitlauf** (sofort): dasselbe Paket → `neu 0, schon fertig 11` (bzw. die Zahl der eingespielten), nichts geschrieben. Zurückgestellte später nachholen: dasselbe Paket erneut, wenn Sitzung/Korrektur erledigt.
8. **Zeitgrenzen:** `lock_timeout` 3 s, `statement_timeout` 120 s (im Paket gesetzt). Bei Zeitüberschreitung: Abbruch ohne Wirkung, in der Lernpause wiederholen. Erwartete Laufzeit [A] wenige Sekunden (lokal mit 6 Aufgaben < 1 s).
9. **Nachher prüfen (lesend):** je V-Lernziel genau eine freigegebene Test-Aufgabe; für ein Testkind `test_starten_intern` *nicht* aufrufen (schreibt) – die Wirkung ist im Nachbau getestet.

## 5. Werkzeuge (Kurzfassung)

- **W2 `tools/vtest_pruefen.py`**: Auswahl (⌈n/2⌉ Fehler, Abwechseln Hinweis), Vollständigkeit/Mengen, Verbote V1–V17 (Lückenweg, zaehlt, Stufe, typ, Verstehens-Klasse, Antworttypen, Auswahl ≥ 4, Fehler-Detektiv-Bauweise, Toleranz, Lösung und Fehlbilder nachgerechnet, Regel, Lehrplan, Lösungsweg, Ähnlichkeit, Teilfähigkeit, ersetzt_test). `--nur-auswahl` zeigt die Tabelle des Vorschlags.
- **W1 `tools/vtest_sql.py`**: baut nur, wenn W2 fehlerfrei ist; Paket mit Schutz wie `tools/bestand_berichtigung1_sql.py` (NF-S-Hashes, feste Trigger-Liste als Mengenvergleich, nullsichere Vergleiche, Sortierungen `collate "C"`, Verweisprüfung zweimal, Zurückstellen statt Abbruch, Fingerabdruck unberührter Zeilen, xmin-Prüfung, Antwortprobe aller Soll- und Fehlantworten über `antwort_bewerten`/`fehlbild_finden`, Lernkarten-Regeln gleich), dazu: je Gruppe genau eine Test-Aufgabe, Zählung je Lernziel/Pool genau um das Soll, neue Korrektur/Sicherung vorn in der Zugreihenfolge.
- **Test** `tools/tests/vtest_sql_test.py` (mit und ohne `RB_PG_ICU=de-DE`).
