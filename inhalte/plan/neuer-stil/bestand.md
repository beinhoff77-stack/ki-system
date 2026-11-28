# Neuer Stil – Teil 1: Bestandsaufnahme mit Fundstellen

Stand 28.11.2026, Helfer „neuer Stil“ (Zweig `helfer-neuerstil`, Basis `lernen-app` 75cfbedb). **Nur gelesen, nichts gebaut, keine Datenbank gesehen.**
Kennzeichen: **[B]** belegt (mit Fundstelle) · **[L]** Lage-Zahl des Projektleiters (live gezählt, von mir nicht nachprüfbar) · **[R]** aus dem Repo gezählt (Repo-Sicht, kann von live abweichen) · **[A]** Annahme · **[S]** Schätzung · **[M]** Meinung · **[?]** nicht prüfbar, Lücke.

Pfadkürzel: `M/` = `supabase/migrations/`, `L` = `lernen.js`.

---

## 0. Zwei Einteilungen: `typ` und `form` (Ergänzung nach Hinweis des Projektleiters)

**Was es gibt**
- **`typ`** (älter, 14 Werte, in den Inhaltsdateien das Feld `g`). [L] Jede freigegebene Übungsaufgabe hat einen: mehrschritt 3 043, direkt 2 789, erkennen 1 530, einkleidung 1 410, knobel 1 339 (nur Pool bonus), verknuepfen 1 219, transfer 1 216, umkehr 1 165, fehler 1 136, begruenden 958, darstellung 937, rueckwaerts 833, pruefung 603, parameter 561. Er sagt, **was das Kind tut** (Tätigkeit).
- **`form`** (neu seit FT-S, 8 Werte, 2 241 Aufgaben) [B] `M/20261203_ft_s_form_takt.sql` Abschnitt 1 (Spalte + Prüfbedingung). Sie sagt, **wie gefragt und geantwortet wird** (Fragebauart). Sie kommt **zusätzlich** zum `typ`; jede Form-Aufgabe hat auch einen `typ`.
- [B] Begründung für zwei Felder: `inhalte/mathe-profi/rollend-2/verhaeltnis.md` Z. 7–11 („Der Unterschied zwischen neu und alt ist nicht die Tätigkeit, sondern die Form“).
- Der Auftraggeber spricht von „rund 20 Aufgabentypen“ – gemeint sind beide zusammen (13 Übungs-`typ` + 8 `form`, teils überlappend).

**Wie sie zusammenhängen** [R] – gezählt an allen 2 448 Form-Aufgaben der Runden 1–15 (`inhalte/mathe-profi/rollend-*/*.json`, Feld `aufgabe.g` gegen `form`):

| form | häufigste `typ` | Art nach Mathe-Profi (`verhaeltnis.md` Z. 62–90) |
|---|---|---|
| lueckenweg (413) | direkt 406, mehrschritt 7 | rechnen (Gerüst, zählt nicht) |
| fehler_detektiv (355) | fehler 322, erkennen 16, begruenden 9 | verstehen |
| verfahren_waehlen (173) | mehrschritt 74, erkennen 67, begruenden 12 | verstehen (laut Profi), real halb rechnen |
| zwei_wege (252) | mehrschritt 190, verknuepfen 59 | rechnen |
| umkehren (334) | umkehr 174, rueckwaerts 140, parameter 13 | rechnen (laut Profi) |
| bruecke (242) | darstellung 200, verknuepfen 22 | gemischt / verstehen |
| anwenden (599) | einkleidung 279, mehrschritt 131, transfer 108, verknuepfen 36 | anwenden (nur ~400 davon mit `typ` der Art anwenden) |
| viele_antworten (80) | umkehr 29, direkt 16, parameter 16 | rechnen/verstehen gemischt |

**Zuordnung `typ` → Art** [B] `verhaeltnis.md` Z. 62–76 (Mathe-Profi): rechnen = direkt, mehrschritt, umkehr, rueckwaerts, verknuepfen · verstehen = erkennen, darstellung, begruenden, fehler, parameter · anwenden = einkleidung, transfer, pruefung.
Daraus mit den Live-Zahlen [L] (17 400 freigegebene Übungen ohne knobel): **rechnen 9 049 (52 %), verstehen 5 122 (29 %), anwenden 3 229 (19 %)** – deckt sich mit `verhaeltnis.md` Z. 7.
Nimmt man die Liste des Projektleiters als „verstehensnah“ (begruenden, fehler, umkehr, rueckwaerts, transfer, verknuepfen, darstellung, parameter), sind es **8 025 (46 %)** – der Unterschied liegt bei umkehr/rueckwaerts/verknuepfen (Profi: Rechnen mit anderer Fragerichtung) und transfer (Profi: anwenden). **[M]** Für die Tests schlage ich in `didaktik.md` eine eigene, prüfbare Klasse „V“ vor, die beide Sichten verbindet.

**Wofür die App welches Feld nutzt** [B]
| Stelle | Feld | Wirkung |
|---|---|---|
| `schule.karte_typen_noetig` (`M/20261118_w176_t1_punkteregel.sql` Z. 43) und `karte_buchen` (`M/20261119_w176_h_muss.sql` Z. 97 ff., `k.typen`) | `typ` | „typen nötig“: zum Landen mindestens min(2, Zahl der verschiedenen `typ`) verschiedene Typen gezählt |
| `karte_buchen` (dieselbe Datei, Bedingung `a.stufe = 3 and a.typ in ('rueckwaerts','verknuepfen','begruenden','fehler','transfer','parameter','pruefung')`) | `typ` + `stufe` | „schwer ok“ |
| `schule.aufgabe_anwenden` (`M/20261203_ft_s_form_takt.sql` Z. 90 ff.) | `typ` ∈ einkleidung, transfer, pruefung | Sachaufgaben-Pflicht (Schalter `anwenden_pflicht`, live 0 = aus [B] `offene-punkte.md`, Abschnitt 28.11. „Sachaufgaben-Pflicht einschalten (eigener Satz)“) |
| `L` 430 `lernAnders`, 432 ff. `lernWaehleKern` (`neuTyp`, `gesehenTyp`) | `typ` | nie zweimal derselbe Typ hintereinander; noch nicht gesehene Typen bevorzugt |
| `L` 476 ff. `lernWaehleBordkarte`, 469 `lernFormPlatz` | `form` | Form-Takt (jede 3. Bearbeitung) |
| `L` 472 `lernTaktErlaubt` | `form` | nie zwei Lückenwege hintereinander, kein Fehler-Detektiv direkt nach eigenem Fehler |
| `schule.aufgabe_zaehlt` (FT-S) | `zaehlt` | Lückenwege zählen nicht |

**Test-Aufgaben** [L] Alle 7 023 freigegebenen Test-/Korrektur-/Sicherungsaufgaben haben **weder `typ` noch `form`**. [R] Bestätigt im Repo: in `inhalte/themen/*.json` haben alle 675 `test`, 2 097 `korrektur`, 4 252 `sicherung`-Aufgaben kein Feld `g`. Sie sind **unklassifiziert**, nicht nachweislich „nur Rechnen“ – Schätzung dazu in Abschnitt 7.

---

## a) Üben: Wie wird die nächste Aufgabe gewählt?

**Ablauf** [B]
1. Die App bekommt je Etappe alle freigegebenen Übungen (`einheit_lesen_intern` → `uebungen`; **Grundfassung nicht im Repo** [?], nur Patches, siehe `inhalte/plan/form-takt-bau.md` Tabelle (b) letzte Zeile).
2. `L` 4521: Vorrat `warte` sortiert: ungelöste zuerst, dann wenig Versuche, dann niedrige Stufe.
3. `L` 4548–4549: vor jeder Bordkarte `lernWaehleBordkarte(warte, e, letzte, gesehenTyp, takt())`, nur wenn keine Stufe von Hand gewählt ist und die Etappe nicht sitzt (`!stufe && !e.sitzt && !e.fertig`). Bei gelandeten Etappen also **kein Takt**.
4. `lernWaehleBordkarte` (`L` 476–505), Reihenfolge der Regeln:
   1. schwere Aufgabe, wenn Punkte voll und „schwer“ fehlt (`L` 440–447, ohne `zaehlt = nein`);
   2. nach zwei Fehlern in Folge einmal ein Lückenweg (`L` 484–488);
   3. Sachaufgabe, wenn nur sie fehlt (`lernAnwendenFehlt`, `L` 466 – wirkt nur bei Schalter an, live aus);
   4. **Form-Platz**: `(bearbeitungen + 1) % form_jede == 0` (`L` 469, 4548; `form_jede` = 3 aus `schule.regel`, FT-S Abschnitt 2) **und** es gibt eine ungelöste Form-Aufgabe **genau der Soll-Stufe** (`L` 497–500: `(x.stufe || 2) === soll`);
   5. sonst ausdrücklich eine Aufgabe **ohne** Form (`L` 502: „der Vorrat der neuen Formen bleibt für die Form-Plätze“);
   6. Notfall ohne Verbote.
5. Soll-Stufe `lernSollStufe` (`L` 427): bei Ziel 6 und `p` eigenen Lösungen 1 + ⌊p·3/6⌋, minus Senkung nach je 2 Fehlern. Fehlerfreies Kind: Bearbeitung 1–2 Stufe 1, 3–4 Stufe 2, 5–6 Stufe 3.
6. `bearbeitungen` = Übungsversuche an der Lernkarte ohne Test, ohne Mischkarte, 2. Anlauf nicht extra – zählt **auch Antworten in der Wiederholung** dieser Karte mit [B] `schule.karte_bearbeitungen`, FT-S Z. 118; Risiko benannt in `form-takt-bau.md` (f) letzter Punkt.
7. „Etappe = 6 Aufgaben“: [B] `schule.karte_ziel` = least(6, greatest(2, Zahl zählender Übungen)) (`M/20261116_w150_sitzt_regel_6_mit_schwer.sql` Z. 10 + FT-S-Patch).

**Gewicht des neuen Stils heute**
- [B] Obergrenze: jede 3. Bearbeitung (Form-Plätze 3, 6, 9 …) plus höchstens ein Lückenweg nach zwei Fehlern. Außerhalb dieser Plätze wählt die App **absichtlich keine** Form-Aufgabe (`L` 502).
- [B, gerechnet aus Regel 5 + `L` 497] Fehlerfreies Kind, neue Lernkarte: Platz 3 (Soll-Stufe 2) und Platz 6 (Soll-Stufe 3) → **2 von 6 Bearbeitungen = 33 %**, aber nur, wenn die Lernkarte eine ungelöste zählende Form auf genau Stufe 2 bzw. 3 hat. Sonst normale Aufgabe (nichts wird nachgeholt).
- [R] Stufen der Form-Aufgaben (alle Runden 1–15): Lückenweg 406 von 413 auf Stufe 1, Fehler-Detektiv 331 von 355 auf Stufe 3, Umkehren nur Stufe 2/3, Zwei Wege 190 auf Stufe 2. Folge: Platz 3 (Stufe 2) bekommt Zwei Wege/Brücke/Umkehren/Anwenden, Platz 6 (Stufe 3) Fehler-Detektiv/Umkehren/Anwenden. **Lückenweg kommt fast nur nach zwei Fehlern**, nicht im Takt.
- [B] Befund des Projektleiters: „ein starkes Kind sieht bis zur Landung oft nur EINE neue Form“ (`inhalte/plan/offene-punkte.md` Z. 49), behoben durch Nachlieferung Stufe 3 (`rollend-11`, Z. 51). [R] Heute haben in Klasse 5 109 von 112 Lernkarten eine zählende Form auf Stufe 3, in Klasse 8 91 von 93 (mit Form).
- [B] Das Kind sieht Form-Aufgaben nur in Einheiten, die welche haben, und erst seit dem Einspielen (Klasse 5 seit 27.11., `offene-punkte.md` „rollend-5 (Klasse 5) eingespielt“). **Davor gelandete Etappen wurden ohne neuen Stil geübt.**
- [A/S] Über den `typ` sieht das Kind schon heute deutlich mehr Verstehen, als die 13 % Form-Anteil vermuten lassen: `lernWaehleKern` bevorzugt ungesehene Typen, 29 % der Übungen haben einen Verstehens-`typ`. Wie viel davon in den 6 Bearbeitungen ankommt, hängt von der Stufenfolge ab (Stufe 1 ist meist direkt/erkennen) – ohne Lerndaten nicht bezifferbar.
- [B] Abhängig von: (1) gibt es in der Einheit Form-Aufgaben, (2) passt deren Stufe zur Soll-Stufe, (3) Fehlerfolge (Lückenweg, Stufensenkung), (4) Wiederholungsantworten verschieben den Takt, (5) Stufe von Hand gewählt → kein Takt, (6) gelandete Etappe → kein Takt.

## b) Wann gilt eine Etappe als „sitzt“, und wie zählen Formen?

[B] `schule.karte_landet` (`M/20261120_lb3_nachbesserung.sql` Z. 24, FT-S-Patch) = alle vier (fünf) Bedingungen:
1. `eigene_loesungen ≥ karte_ziel` (6 bzw. weniger bei kleinem Vorrat); eigene Lösung = richtig ohne Tipp, jede Aufgabe einmal (`karte_buchen`, `M/20261119_w176_h_muss.sql`, `v_eigen`, `gezaehlt`); 2. Anlauf richtig zählt nicht (`M/20261116_w150_r2_…` Kopf, V2);
2. `typen` ≥ `karte_typen_noetig` (min(2, verschiedene `typ`));
3. `schwer_ok` oder keine Stufe-3-Aufgabe vorhanden;
4. `folge ≥ min(3, ziel)` (drei in Folge richtig);
5. Sachaufgabe (Typ einkleidung/transfer/pruefung), **nur bei Schalter `anwenden_pflicht = 1`** – live aus.

Form-Aufgaben: [B] zählen **genau wie Bestand**, wenn `zaehlt` leer/ja. Lückenwege (`zaehlt = nein`) ändern an der Karte nichts (FT-S `karte_buchen`-Patch, `uebung_pruefen_intern` liefert nur `bearbeitungen`). **Es gibt keine Regel, die eine Form-Aufgabe für „sitzt“ verlangt.** „Anwenden nötig“ hängt am `typ`, nicht an `form = anwenden`. Der Vorschlag „alle drei Arten für sitzt“ ist vom Nutzer zurückgestellt (`offene-punkte.md` Z. 20).

## c) Tests: Zusammenstellung, Bewertung, Abschluss

Vollständige aktuelle Fassungen: `test_starten_intern`, `nachtest_auswahl`, `nachtest_stand` in `M/20261208_nf_s_nachtest_freigegeben.sql` (Z. 57, 76, 120). **`test_abschliessen_intern` und `test_antwort_intern`: Grundfassung nicht im Repo** [?]; bekannt nur Patches (`M/20261120_ab_s_abschluss.sql` Z. 256 ff., `M/20261120_ab_s_flug_abschluss_einmal.sql`, `M/20261121_ab_s_flug_geschafft_robust.sql`, `M/20261123_tl_s_teilung.sql` Z. 274, `M/20261202_bd_s2_bedingung_ausgabe.sql` Z. 69) und eine live gelesene Beschreibung (`inhalte/postfach/bau-motivation.md` Z. 1029–1032).

| Testart | Auswahl [B] | Bewertung |
|---|---|---|
| **Flugtest** (`blocktest`) | **alle** freigegebenen Aufgaben des Pools `test` der Einheit, nach `reihenfolge` (nf_s Z. 157 `array_agg … where pool = 'test' and freigegeben`) – auch Kür-Etappen (`bau-motivation.md` „Blocktest-Auswahl … nur Pflicht“ offen) | je Etappe „alle richtig“ (bool_and), keine Quote; falsch → Status `fehler` → Korrektur (`bau-motivation.md` Z. 1030, live gelesen 22.11.) |
| **Nachtragstest** (blocktest nach abgeschlossenem Flugtest, W177) | je **offene** Pflicht-Etappe **eine** ungesehene Aufgabe, zuerst Pool `test`, sonst `korrektur`, nach `reihenfolge` (nf_s Z. 140–155) | wie Flugtest: richtig → nachgewiesen, falsch → fehler (`M/20261118_w177_nachtragstest.sql` Kopf) |
| **Korrektur** („Verbessern“) | je Etappe mit Status `fehler` **eine** ungesehene Aufgabe aus `korrektur`, nach `reihenfolge` (nf_s Z. 178–186) | richtig → korrigiert [A: falsch → bleibt fehler; Grundfassung fehlt] |
| **Nachtest** (10/25/60 Lerntage) | je Pflicht-Etappe `nachtest_je_etappe` = ⌈5 / Pflicht-Etappen⌉ Aufgaben aus `sicherung` (`M/20261124_nt_s_nachtest_menge.sql` Z. 14); ungestellte zuerst, aufgefüllt mit am längsten zurückliegenden; ohne ungestellte → „Vorrat erschöpft“, kein verkürzter Test (nf_s Z. 57–70) | Quote über alle: ≥ 0,8 bestanden (Runde +1, nach 3 „gesichert“), ≥ 0,6 wiederholen, sonst Rückreise (NT-S Kopf; `L` 5157, 5240–5243). Wertung je Etappe „wie bisher“ [?, Grundfassung fehlt] |

[R] Vorrat je Lernziel im Repo (`inhalte/themen/*.json`, entspricht in der Summe fast genau den freigegebenen Live-Zahlen 675/2 096/4 252): `test` **genau 1** je Lernziel (675 Lernziele), `korrektur` 3 (603) oder 4 (72), `sicherung` meist 6 (585), sonst 7–12. Live am 22.11.: 546 Etappen mit 1, 84 mit 2, 1 mit 3 Test-Aufgaben (vor der Sperre) [B] `bau-motivation.md` Z. 1029.
[B] Flugtest live mit 25 Bordkarten beobachtet (`offene-punkte.md`, Designer Nachtrag 3).

**Anzeige und Bewertung im Test** [B]
- Server bewertet **typunabhängig vom Pool** mit `schule.antwort_bewerten` (`M/20261116_w150_r2_…` Z. 17; Zweig `bedingung` aus BD-S1). Antworttypen: zahl, auswahl, markierung, luecken (nur ganze Zahlen), text, bedingung.
- App: der Test nutzt **dieselbe** Aufgabendarstellung wie das Üben (`lernTestLauf`, `L` 5170: `lernAufgabe(a, antworten.get(a.id))`; `lernAufgabe` `L` 3150 ff. kann alle sechs Antworttypen inkl. `bedingung` `L` 3201).
- **Die acht Formen sind keine eigenen Antworttypen**, sondern Inhalte in den alten Typen [R]: Fehler-Detektiv 344× auswahl (256 mit **3**, 88 mit 4 Möglichkeiten), 10× zahl, 1× luecken; Lückenweg 413× luecken; viele_antworten 80× bedingung; Umkehren 307× zahl; Zwei Wege 237× zahl; Anwenden 566× zahl; Brücke 141× auswahl, 87× zahl; Verfahren wählen 173× auswahl (153 mit 4). Eine echte „Zeilenauswahl“ gibt es nicht – die Zeile wird als Auswahl („in Zeile 2 / 3 / in keiner“) gefragt.
- ⇒ **Alle 2 241 Form-Aufgaben lassen sich im Test-Bildschirm heute darstellen und prüfen.** `bedingung` im Test ist serverseitig nachgewiesen: Prüfpaket BD-S2 legt eine Probe-Aufgabe in den Pool `test`, ruft `test_antwort_intern` und `test_abschliessen_intern` und verlangt `antworttyp: bedingung` und die geschützte Lösung im Ergebnis (`tools/tests/bedingung_einspielen2.py` Z. 118–125, 164–166).
- Im Test **nicht** vorhanden [B]: Tipp (`aufgabe_anzeige(a, false)`, nf_s Z. 199; `M/20261118_w150_f_…` Z. 52), zweiter Versuch, Rückmeldung vor dem Abgeben, Fehlbild-Rückmeldung („Flug-Test liefert kein Fehlbild“, `offene-punkte.md` Eintrag „Entwurf Regelkarte“), Tastenfeld (Designer Nachtrag 3). Nach dem Abgeben: richtig/falsch je Karte, bei falsch Lösung und Lösungsweg (`L` 5225 ff.).
- Hinweis Form im Test [B]: `aufgabe_anzeige` liefert seit FT-S `form` und `zaehlt` auch im Test mit; die App nutzt `form` nur im Üben („Zum Aufwärmen – zählt nicht“, `L` 4735). Der Test kennt `zaehlt` nicht: ein Lückenweg im Test-Pool würde voll zählen.
- Texte, die ein Umbau berührt: „Eine Bordkarte je Etappe, ohne Tipps“ (`L` 5152), Nachtragstest-Text (`L` 5154), Nachtest-Text (`L` 5157).

## d) Wiederholung, Mischkarten, „Was wackelt“

- [B] Wiederholung und Mischkarte wählen serverseitig mit `schule.wdh_aufgabe_waehlen` (`M/20261122_wd_s3_frische_aufgaben.sql` Z. 55; FT-S-Patch: nur zählende): Pool uebung, freigegeben, Mischkarte nur Stufe 2/3; Reihenfolge **nie bearbeitete zuerst**, dann Stufe 1 hinten, dann Zufall. `form` spielt keine Rolle.
- [A] Folge: Weil das Üben Form-Aufgaben nur auf Form-Plätzen zieht, bleiben viele ungesehen und kommen in der Wiederholung bevorzugt dran – die Wiederholung zeigt den neuen Stil vermutlich **öfter** als das Üben, aber zufällig und ungesteuert. Nicht messbar ohne Lerndaten.
- [B] „Was wackelt“ (`M/20261205_ww_s_wackelt.sql` Z. 80 ff., `wackelt_analyse`): liest alle Versuche (auch Test), gibt `form` und `typ` nur zur Anzeige mit; Fehlerarten über Fehlbilder (RB-S) und `grund`. Keine Auswertung nach Form oder Art.
- [B] Tests liefern keine Fehlbilder; die Test-Aufgaben haben im Repo keine Fehlbild-Angaben (Fehlbilder kamen mit den Runden, RB-S).

## e) Wie Aufgaben und Pakete entstehen – was ein Generator für Test-Pools können müsste

[B] Weg heute: Rundenordner `inhalte/mathe-profi/rollend-N/` (je Thema eine JSON, `bauen.py`, bei neueren Runden `th_*.py`, `kern.py`, `regeln.py`, Vorprüfung) → `tools/vorrat_pruefen.py` (Hinweise: verratene Lückenwerte, Abhängigkeit, Fehlbilder, Detektiv-Zeilen; nur Runden 1–4 + fachwoerter fest verdrahtet, Z. 24–25) → `tools/rollend_sql.py --runden N --sql` → Paket mit `schule.aufgaben_einfuegen` + Regelbezug-Block (`tools/regelbezug_sql.py`).
Sperren im Werkzeug [B] `tools/rollend_sql.py`:
- Z. 120: `if a['p'] != 'uebung': fehler … Vorrat … statt uebung` – **nur Übungen**.
- Z. 140–145: Reihenfolge-Nummern ab `max_r` der Einheit (Pool uebung, aus `inhalte/plan/rollend-einheiten.json`) + 1000·Runde.
- SQL prüft `max(reihenfolge) … pool = 'uebung'` (Z. 228).
Server [B] `schule.aufgaben_einfuegen` (`M/20261118_w150_f_…` Z. 39, FT-S-Patch) nimmt **jeden** Pool an (Feld `p`; `art` = blocktest für test, nachtest für korrektur/sicherung), übernimmt `form`, `zaehlt`, `typ` (`g`), und fügt nur ein, was es in der Einheit (gleiche Frage, gleiche Antworten) – **poolübergreifend** – noch nicht gibt.
[B] Freigegebene Einheiten/Aufgaben sind durch Trigger `einheit_schutz`/`aufgabe_schutz` unveränderlich (`bau-motivation.md`, LK-S Punkt 2). Bestehende Test-Aufgaben kann man **nicht nachträglich** mit `typ`/`form` versehen, ohne diese Schranke anzufassen.

Ein Generator für Test-Pools müsste [M]:
1. Feld `p` = test/korrektur/sicherung erlauben; je Pool eigene `max_r` lesen (Erweiterung `rollend-einheiten.json`) und eigene Nummernbereiche; die Reihenfolge steuert, **was zuerst gezogen wird** (Flugtest-Reihenfolge, Korrektur `limit 1`, Nachtest nach `reihenfolge` unter Ungestellten).
2. Sperren: kein `lueckenweg`, `zaehlt` nur `ja`, Lernkarte ist Pflicht-Etappe, keine Frage, die einer Übung derselben Einheit gleicht oder nur andere Zahlen hat (sonst „schon gesehen“; `aufgaben_einfuegen` würde gleiche Fragen still überspringen, das Paket bricht dann an der Zählung ab).
3. Ratesperre: `auswahl` mit mindestens 4 Möglichkeiten, Fehler-Detektiv als `luecken` (Zeile + berichtigter Wert) statt 3er-Auswahl (Regeln in `didaktik.md`).
4. Stufe: Test-Aufgaben haben heute alle Stufe 2 [L]; neue ebenso (Stufe 3 nur Kür/Bonus).
5. `typ` mitsetzen (für Auswertung „Rechnen/Verstehen“) und die Tippspalte füllen (wird im Test nicht gezeigt, aber vom Werkzeug verlangt, Z. 124).
6. Vorprüfung (`vorrat_pruefen.py`) auf beliebige Runden ausweiten.

## f) Verteilung der Form-Aufgaben (Repo-Sicht)

[R] Gezählt aus `inhalte/mathe-profi/rollend-1` … `rollend-15` (2 448 Aufgaben = 2 241 eingespielt + 207 Runde 15) gegen `inhalte/themen/*.json` (Etappen) und `inhalte/themenliste.json` (Klasse = Gymnasium Bayern). **Repo-Sicht**: Teil-Einheiten (`_teil2`) haben im Repo keine eigene Themendatei; Live-Zuordnung kann abweichen.

| Klasse (gym) | Einheiten | davon mit Form | Lernziele | Form-Aufgaben | Bemerkung |
|---|---|---|---|---|---|
| 5 | 15 | 15 | 112 | 676 | jede Lernkarte hat Form; 109/112 zählende Stufe-3-Form; meist 5 zählende je Lernkarte |
| 6 | 11 | 11 | 82 | 355 | viel `anwenden`, wenig Fehler-Detektiv; `daten.kennwerte`, `terme.potenzgesetze` dünn (9) |
| 7 | 14 | 14 | 74 | 476 | inkl. Runde 15 |
| 8 | 17 | 15 | 103 | 492 | **ohne Form: `funktionen.gebrochen`, `gleichungen.formeln`**; 91/93 Stufe-3-Form; 15 Lernkarten nur 2 zählende |
| 9 | 14 | 8 | 107 | 289 | ohne: funktionen.potenz, gleichungen.lgs3/.potenz/.trig, trigo.allgemein, zahlen.rationale_exponenten |
| 10 | 10 | 4 | 63 | 83 | ohne: 6 Einheiten |
| ohne Klasse (IB/Sonder) | 24 | 4 | 134 | 77 | fast leer |

Stark: Klasse 5 Zahlen (`zahlen.rechengesetze` 76, `zahlen.natuerlich` 72, `zahlen.ganz` 61). Dünn: `messen.prisma_zylinder_teil2` (3), `daten.kennwerte`/`terme.potenzgesetze` (9), `raum.schraegbilder` (12). Formenmix in Klasse 6 einseitig (`anwenden` 135 von 355).

## 7. Schätzung: Wie viel der 7 023 Test-Aufgaben ist reines Rechnen?

Methode [R]: (1) Stichwortsuche über alle 7 024 Test-/Korrektur-/Sicherungsaufgaben in `inhalte/themen/*.json`, (2) 40 zufällig gezogene Aufgaben von Hand nach der Profi-Tabelle eingeordnet (Zufallsstart 7; Skript außerhalb des Repos).
- Stichworte (Fehler/„stimmt“/„hat recht“ bzw. begründe/warum/„welche Aussage“): nur **≈ 3 %** (fehler 120, begründen 99). Sachkontext (€, km, Liter …): ≈ 9 %.
- Handstichprobe 40: reines Ausführen eines Verfahrens (direkt/mehrschritt, z. B. „Berechne die Nullstelle“, „Löse … durch Faktorisieren“, „Berechne A·B“) **16 (40 %)**; Sachaufgabe, im Kern Rechnen **9 (≈ 22 %)**; Ablesen/Erkennen (Diagramm, Winkelnamen, Periode) **5 (≈ 13 %)**; verstehensnah (Umkehr/Rückwärts, Bedingung prüfen „wie viele Schnittpunkte“, „welche Aussage ist falsch“, Weg A/B vergleichen, f⁻¹) **10 (25 %)**; ausdrücklich Fehler finden oder begründen: 2 (5 %).
- **[S] Ehrliche Schätzung: 55–70 % „Rechnen“ im Sinn des Profis** (direkt, mehrschritt, umkehr, rueckwaerts, verknuepfen), **10–20 % Verstehen** (erkennen, darstellung, begründen, fehler), **15–25 % Sachaufgaben**; Form-Bauarten des neuen Stils (Fehler-Detektiv, Zwei Wege, Verfahren wählen) fast nicht (< 5 %). Unsicherheit bei n = 40 etwa ± 15 Prozentpunkte. Repo ≈ live, weil die Repo-Zahlen den freigegebenen Live-Zahlen entsprechen.
- Vorschlag Einordnung als eigener Schritt: siehe `konzept.md`, Schritt E.
