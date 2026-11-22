# Postfach bau-motivation (Bau-Chat, Bau-Auftrag G / Werkstatt-Wunsch 176)

Neueste oben.

## FERTIG: NT-S (22.11., bau-lehrer)

**Dateien:** `supabase/migrations/20261124_nt_s_nachtest_menge.sql` (nach TL-S; nicht eingespielt, kein DROP/DELETE), `supabase/tests/nt_s_rauchtest.sql` (Rollback, Testkind, eigene Test-Flüge).

**Umsetzung:**
- Regel `schule.nachtest_je_etappe(Pflicht-Etappen)` = aufrunden(5 / n): 1 → 5, 2 → je 3, 3–4 → je 2, ab 5 → je 1 (Mindestzahl als Regel `nachtest_min_aufgaben` = 5). Gezählt: Pflicht-Etappen des Kindes (`lernziel_stand.pflicht`, nach TL-S Pflicht/Kür je Schulart).
- `test_starten_intern`, nur der Nachtest-Zweig (Umbau per Anker): je Etappe `schule.nachtest_auswahl` – ungestellte Aufgaben zuerst; fehlen welche zur Menge, wird mit schon gestellten aufgefüllt (die am längsten zurückliegenden zuerst), nie doppelt im selben Nachtest. Ohne jede ungestellte Aufgabe bleibt es „Vorrat erschöpft“ wie bisher → für Flüge mit ≥ 5 Pflicht-Etappen ändert sich nichts.
- Quote, Einstufung (0,8 / 0,6) und Wertung je Etappe unverändert; Flug-Test und Korrektur-Test unverändert.
- `nachtest_stand`: `vorrat_runden` = Runden mit ungestellten Aufgaben bei dieser Menge, neu `aufgaben_je_etappe`.
- Sicht `schule.nachtest_vorrat` (Bericht): je Pflicht-Etappe vorhanden / Bedarf für drei Nachtests / fehlen.

**Rauchtest (lokal mit den Live-Funktionen nachgebaut, grün):** 1 Etappe: 5 Aufgaben, 1 Fehler → bestanden (bisher Rückreise); 2: 6 → bestanden (bisher Rückreise); 3: 6 → bestanden (bisher wiederholen); 5: 5 → bestanden (unverändert). Keine Aufgabe doppelt, Etappen gleich verteilt, zweite Runde ohne Wiederholung, Auffüllen 2 ungestellte + 3 älteste, ohne ungestellte → erschöpft.
Hinweis (Fakt, unverändert): ein Fehler setzt die Etappe weiter auf „fehler“ → vor dem nächsten Nachtest Korrektur-Test, auch wenn der Nachtest bestanden ist.

**Fehlliste Sicherungs-Aufgaben** (Bedarf drei Nachtests: 1 Etappe 15, 2 je 9, 3–4 je 6, ab 5 je 3; vorhanden = echter Stand, lesend):
*Nach der Teilung – Gymnasium (Kinder 1, 2):*
- 46 Teil 3 (1 Pflicht-Etappe): punktspiegelung 6 von 15 → **fehlen 9**
- 91 Teil 2 (2): rotation 6 von 9 → **3**, axialschnitt 6 von 9 → **3**
- 61 Teil 1 (3): darstellen 0 von 6 → **6** (Etappe kommt mit LK-D-Einspiel)
- 91 Teil 1 (3): wahre_groesse 0 → **6**, raumwinkel 0 → **6** (kommen mit LK-D)
- 101 Teil 2 (1): cavalieri 0 von 15 → **15** (kommt mit LK-D)
- ohne Fehlbedarf: 26 T1/T2, 29 T1/T2, 44 T1, 46 T1, 61 T2, 101 T1; ohne Pflicht (kein Nachtest): 44 T2, 46 T2.
*Zusätzlich Realschule I:* 29 T2 gleichungen_binomisch **6**; 44 T2 vierecke **3**, vierecke_konstruieren **9**; 46 T2 vektor_koordinaten **6**; 46 T3 vektor_drehen **6**; 91 T2 koerper_symmetrie **6** (dafür 91 T2 rotation/axialschnitt dort ausreichend, 4 Pflicht-Etappen).
*IB (myp_standard):* wie RS I bei 29 T2, 44 T2, 46 T2/T3, 61 T1, 101 T2; 91 ohne Pflicht.
*Bestehende Flüge mit ≤ 4 Pflicht-Etappen (vor der Teilung):* nur **30 Potenzen und negative Exponenten** (2): potenz_begriff 6 von 9 → **3**, negativer_exponent 7 von 9 → **2**. Ausreichend: 1, 7, 58, 65, 66, 69, 91, 102, 103.
Annahme: Pflicht je Schulart aus `lk_teilung_2211.json` (LK-D 4), Etappen, die es noch nicht gibt, mitgezählt.

## FERTIG: LK-S Test 2 (22.11., bau-lehrer)

**Datei:** `supabase/tests/lk_s_rauchtest.sql` (nur Test, keine Migration).
- Prüfung 3 (Thema 61 in RS I 8 und 9) läuft jetzt über die Teile-Familie (`coalesce(teil_stamm, id) = 61`): zusammen Klassen 8 und 9, „neu“ ab 8, Route-Start 9 beim Teil mit Klasse 9 (ungeteilt: 61 selbst; geteilt: Teil 2), `thema_jahrgang` und `route_start` an diesem Teil. Spalten der Teilung werden über `to_jsonb` gelesen – der Test läuft auch ohne TL-S.
- Lokal nachgestellt: alter Test nach der Teilung von 61 → „FEHLER 3 Thema 61“ (wie im Probelauf); neuer Test vor und nach der Teilung durchgelaufen (Teil 1: RS 8, Teil 2: RS 9).

## FERTIG: TL-S 4 (22.11., bau-lehrer)

**Dateien:** `supabase/migrations/20261123_tl_s_teilung.sql`, `supabase/tests/tl_s_rauchtest.sql`, `supabase/werkzeug/tl_s_daten.py`, neu `supabase/tests/nachbau_graph_live.sql` (Voraussetzungen, Orte, Ort-Themen wie live; keine Kinderdaten). Nicht eingespielt, kein DROP/DELETE.

**Ursache (Fehler, kein gewolltes Delta):** In `lk_teilung_2211.json` steht bei Kanten `art_je_schulart: "Zusatz"`, wenn der **abhängige** Teil in der Schulart Zusatz ist (z. B. 91 Teil 1 ← 52 im IB). Ich hatte „Zusatz“ als „empfohlen“ übersetzt → im IB fiel u. a. 91 ← 52 weg (Ort 109 → 86). Richtig: „Zusatz“ ändert die Kante nicht; nur ausdrückliches „hart“/„empfohlen“ weicht je Schulart ab, und „nur empfohlen“ gilt, wenn die **Voraussetzung** in der Schulart Zusatz ist (Entscheidung 16:20).
**Zweiter Fund (lokal, live ohne Wirkung):** Teil 1 als Zusatz im Plan (101 Teil 1 in der Realschule) hätte den ganzen Ort 86 auf „zusatz“ gesetzt – dort liegt auch 52. Jetzt nur, wenn am Ort kein anderes Thema liegt.

**Vorher/nachher je Schulart (Graph wie live, lesend übernommen; Migration lokal):**
- Visum vorher 46 Ort-Paare; nachher je Schulart nach Abbildung der neuen Orte auf den Ort von Teil 1: Gym, RS, IB **ohne fehlende und ohne zusätzliche Paare**. Der Abbruch-Vergleich B4 läuft durch.
- 102 ← 30 und 29 ← 102 sind in allen drei Schularten hart; Ort 62 braucht 44 in allen Schularten.
- Neuer Rauchtest 13: keine harte Kante wird je Schulart abgeschwächt, außer ihre Voraussetzung ist dort Zusatz; 102 ← 30 und 29 ← 102 in jeder Schulart hart.
- Migration lokal zweimal ohne Fehler, Rauchtest vorher/nachher grün.

**Hinweis Kür-Daten (LK-D 4 ist in der JSON angekommen):** Die Migration übernimmt jetzt `pflicht_je_schulart` je Teil. Gegenüber der bisherigen Pflichtliste ändert sich im Gymnasium: 26 Teil 2 `erkennen` wird Pflicht, 44 Teil 2 `vierecke` wird Kür (44 Teil 2 ist dort ohnehin Zusatz). Weitere Abweichungen nur RS/IB. Live gibt es Lernstand-Zeilen nur zu 29 (Kinder 1–3), und dort stimmt die Regel mit dem Bestand überein → kein Abgleich nötig. Bestehende Zeilen werden sonst beim nächsten Teststart des Kindes abgeglichen (`lernziele_anlegen`); einen Sammel-Abgleich schlage ich für KS vor.

## FERTIG: TL-S 3 (22.11., bau-lehrer)

**Dateien:** `supabase/migrations/20261123_tl_s_teilung.sql`, `supabase/tests/tl_s_rauchtest.sql` (nicht eingespielt, kein DROP/DELETE).

**Ursache (lokal nachgestellt):** „Kann er komplett“ steht live als `route.kann_schon` am Ort; `thema_kann_schon`/`thema_kann_wdh` zählen nur Plan-Einträge mit Art „normal“. 46 Teil 2 ist im Gymnasium Zusatz → Plan-Art „zusatz“ → Setzung weg → B4 brach zu Recht ab. Mein Nachbau hatte vereinfachte `thema_kann_schon`/`thema_kann_wdh` – jetzt wie live.

**Lösung:**
- `thema_kann_schon` und `thema_kann_wdh` zählen auch Plan-Einträge „zusatz“ (Umbau per Anker, wiederholbar). Gesetzt bleibt gesetzt, Plan-Art bleibt „zusatz“, `im_plan` bleibt dort wie bisher nur für „normal“ (erlaubtes Delta).
- Jeder neue Teil erbt vom Plan-Eintrag des Themas: Platz direkt dahinter, Status, `kann_schon`, `kann_schon_themen`/`kann_wdh_themen`/`ausgelassen` (auf den Teil umgeschrieben), auch Rückreise-Einträge. Wiederholungs-Setzung: je Teil mit dessen Etappen; Karten mit Fälligkeiten ziehen unverändert mit.
- Live geprüft (lesend): Folgen hat heute nur das Setzen am Ort (`kann_schon`); Einträge „zusatz“ mit Setzung gibt es keine → die Änderung ändert am heutigen Stand nichts.

**Fakten, echter Stand (lesend, nur Nummern):**
- Bei den 7 geteilten Themen: Kind 2 hat 26 und 46 „Kann er komplett“ (Orte 54, 82), Kind 1 hat 26 im Plan, nicht begonnen; keine Wiederholungs-Setzung, keine Rückreise.
- Sonst gesetzt (nicht geteilt): Kind 2 „komplett“ bei 23, 22, 21, 17, 15/16/18/67, 25, 28, 1, 42/73, 53, 50, 58, 60 und 19; „wiederholen“ bei 30, 71, 24, 57, 99/100. Zusatz-Einträge (ohne Setzung) bei beiden Kindern.

**Nachbau ergänzt:** gesetzt komplett (Kind 2: 26, 46 inkl. Zusatz-Teil), gesetzt mit Wiederholung (RS-Kind: 46, mit Karten), im Plan nicht begonnen (Kind 1: 26), Rückreise (RS-Kind: 26). Neuer Rauchtest 12: jeder Teil erbt Setzung, Rückreise und Plan-Platz (Zusatz-Teil: als „zusatz“; leerer Teil: nicht im Plan). Migration lokal zweimal ohne Fehler, Rauchtest vorher und nachher grün.

**KS** (Kür im Server: Tages-Wiederholung, Mischkarten, Blocktest-/Korrektur-Auswahl) wie vereinbart als eigener Auftrag nach dem Teilen.

## FERTIG: TL-S 2 (22.11., bau-lehrer)

**Dateien:** `supabase/migrations/20261123_tl_s_teilung.sql` (eine atomare Migration, nicht eingespielt, kein DROP/DELETE), `supabase/tests/tl_s_rauchtest.sql` (spielt die Migration ein, Rollback), neu `supabase/werkzeug/tl_s_daten.py` (Datenblock aus `lk_teilung_2211.json`), `supabase/tests/nachbau_live_constraints.sql` (echte Indizes/Constraints für lokale Nachbauten).
**Reihenfolge:** lk_korrektur (neu) → FP-S 4 → LW-S 2 → LK-S → TL-S.

**Fakten (lokal, Nachbau jetzt mit den echten eindeutigen Indizes/Constraints aus pg_indexes/pg_constraint, `thema_stufe` und `reiseoptionen` wie live):**
- Abbruch `zuordnung_eintrag_id_idx` lokal nachgestellt und behoben. Lösung: je Punkt bleibt **ein** Hauptbezug – beim Teil mit den meisten Etappen des Punkts (Gleichstand: früherer Teil); die anderen Teile bekommen einen **Nebenbezug** mit `rolle` und ihren Etappen. `thema_lage_klasse` (LK-S) zählt Nebenbezüge von Geschwister-Teilen wie Hauptbezüge (Umbau per Anker, wiederholbar) → jeder Teil behält seine Klassen; `lehrplan_abdeckung` bleibt bei „Punkte mit Hauptthema“. Punkte „ganzes Thema“ (`*`) gelten für alle Teile (Nebenbezug). Index nicht erweitert.
- Liste: 7 Themen / **15 Teile / 8 neue Flüge**, 34 Kanten inkl. `art_je_schulart` (z. B. 46 T3 ← T1 nur im Gym hart). Neue Etappen aus LK-D 3 (`cavalieri`, `koerper_symmetrie`, `gleichungen_binomisch`, `darstellen`, `raumwinkel`) sind eingeplant; live noch nicht vorhanden → übersprungen und gemeldet. **101 Teil 2** besteht nur aus `cavalieri` → wird als leere Hülle angelegt (Thema, Ort, Einheit im Entwurf, in keinem Plan, sperrt nichts; Zuordnungen folgen der vollen Etappenliste).
- **B2 – eine Regel:** `schule.pflicht_lernziele(kind, einheit)` = Liste `bewertung.pflicht_je_schulart` der Gruppe (rs_I, rs_II_III, myp_standard …, über `kind_zweig`), sonst der Schulart, sonst `lernziele_pflicht`. `lernziele_anlegen` schreibt `lernziel_stand.pflicht` danach. Damit folgen Flug-Test-Wertung, Korrektur, Flug-Abschluss/Stempel, 100 Ort-Sterne, Nachtests, Ort-/Thema-Stand der Regel (alle lesen `lernziel_stand.pflicht`); `wdh_ablegen` und `konto_wd` auf die Regel umgestellt. `thema_stufe`: Teil mit 0 Pflicht-Etappen → kein Zwangstest; Kür-Fehler machen den Flug nicht „dran“. Teile: „vollständig“ (Stempel/100 Sterne) nur über die Pflicht-Etappen des Kindes.
- **B3 – Schulartwechsel:** Trigger auf `lernender.schulart/zweig` gleicht `lernziel_stand.pflicht` der Einheiten mit Listen ab. Nichts wird gelöscht; neue Pflicht-Etappe = „offen“ → Flug wieder offen über den vorhandenen Nachtragstest (W177/I-5); Rückwechsel → wieder Kür. Erstabschluss/Stempel/Sterne bleiben, keine Doppelbuchung (Rauchtest 11).
- Regressionen im Rauchtest: 3/3 Pflicht + 0/1 Kür → geschafft; nach Wechsel 3/4 → offen; Rückwechsel → geschafft; Sterne/Lernstand-Zeilen unverändert; 0 Pflicht → kein Test. Gültiger Testpfad: jede Pflicht-Etappe eines freigegebenen Teils hat eine Test-Aufgabe (Fehler sonst).
- Ohne Daten aus LK-D 4 (`kuer_in`) ändert sich am Pflicht-Stand der Kinder nichts – Listen gibt es erst, wenn der Datenblock sie enthält (Werkzeug erzeugt sie aus `etappen[].kuer_in`).

**Annahmen / offen:**
- Live gibt es heute Kür nur als `lernziele_vertiefung` (26: erkennen, aenderung; 46: verschiebung, drehung, gegenvektor; 91: lage, koordinaten). Dadurch hat **46 Teil 2** nach der Teilung keine Pflicht-Etappe (für alle) → Zusatz ohne Zwangstest, kein Stempel. In der Realschule ist er laut Lehrplan Pflicht → LK-D 4 muss das mit `kuer_in` liefern.
- Datenbank kennt nur `gym_by/rs_by/ib_myp` + `zweig` (rs_I/rs_II_III); IB-Gruppe (standard/extended) hat keinen Platz am Kind → `myp_standard` per `kind_zweig`.
- Zusatz-**Teile** (Themen-Ebene) beim Schulartwechsel: Plan-Art (`zusatz`/`normal`) wird **nicht** automatisch umgestellt – gehört in Plan/Reise.

**Vorschlag Aufteilung (B2 ist für eine Datei zu groß; in TL-S 2 nur, was die Teilung braucht):**
1. TL-S 2 (diese Datei): Teilung, Zuordnungen, Kanten je Schulart, die Regel + Abgleich + Schulartwechsel, thema_stufe.
2. **KS (eigener Auftrag, nach LK-D 4):** Tages-Wiederholung und Mischkarten nur aus Pflicht-Etappen; Blocktest-Auswahl und Korrektur-Test nur Pflicht (heute kommen Kür-Testaufgaben in den Blocktest, zählen aber nicht); `flug_erstabschluss_nachtragen`/`ort_stand` für Teile mit 0 Pflicht klären (Stempel ja/nein); Anzeige „Pflicht im Gym / Kür in der RS“ (Gestalter). Grund: das ändert das Verhalten für alle Flüge mit Vertiefung, nicht nur für die geteilten.

## FERTIG: TL-S (22.11., bau-lehrer)

**Dateien:** `supabase/migrations/20261123_tl_s_teilung.sql` (eine atomare Migration, nicht eingespielt, kein DROP/DELETE), `supabase/tests/tl_s_rauchtest.sql` (spielt die Migration in einer Transaktion ein, prüft, Rollback).
**Reihenfolge:** nach LK-S und LW-S/LW-S 2 (Schritt 0 prüft beides); einspielen erst nach dem Gym-Audit (LK-D 3).

**Fakten (lokal, PG 16, Nachbau der 6 Themen mit Live-Struktur, echtem `thema_stufe`, `reiseoptionen`, `fehler_endgueltig_am`):**
- 13 Teile / 7 neue Flüge (Zahl 15 im Kopf berichtigt). Zweimal eingespielt: zweiter Lauf teilt nichts mehr. Rauchtest grün, vor und nach dem Einspielen.
- **B3a:** Lehrplan-Punkte nach `zuordnung.etappen` auf die Teile (über mehrere Teile → je Teil eine Zuordnung). Alle 28 Kanten der JSON gesetzt, u. a. 31/8/97/35 ← 29 Teil 2, 62/64 ← 61 Teil 2, 93 ← 26 Teil 2, 74 ← 46 Teil 2, 49 ← 46 Teil 3; alte Kanten auf Teil 1 umgehängt, nicht doppelt.
- **B3b:** Aufgaben ziehen mit gleicher Id in die Einheit ihres Teils → `versuch → aufgabe → einheit` zeigt ohne Lesepfad-Umbau auf den richtigen Teil (Was wackelt, Lernstand, Lehrer-Ansicht, Wertung). Rauchtest 3 erfasst alle alten Antworten vor dem Teilen und prüft danach Teil und Summe der „Was wackelt“-Fehler je Kind.
- **B3c:** `schule.voraussetzung_schulart` + `v_ort_visum.schulart`; `reiseoptionen` filtert nach der Schulart des Kindes. Gym: 44 T2 und 46 T2 Zusatz, 46 T3 ← T2 nur empfohlen, ← T1 hart. Zusatz-Teile stehen im Plan als Art „zusatz“ und sind nirgends Visum (Rauchtest 5).
- **B4:** Abbruch-Vergleich je Thema und Kind jetzt mit ganzen Karten-/Lernziel-Zeilen (alle `wdh_*`, `misch_ok_am`), offenen Mischkarten, `thema_stufe`, Reiseoptionen; global zusätzlich Visum je Schulart. Erlaubte Deltas ausdrücklich: im Plan/gesetzt/Rückreise je Teil wie vorher (Zusatz-Teil: als „zusatz“ im Plan); Etappen/begonnen/gelandet/sicher/wieder offen summieren sich zum alten Wert; Stufe je Teil ergibt sich neu; Reiseoptionen/Visum gleich nach Abbildung neuer Orte auf den Ort von Teil 1. Alles andere bricht ab (lokal mehrfach ausgelöst und behoben).
- **Kind 2, 29 Teil 2:** Stempel, Ort fertig, 100 Ort-Sterne (einmal), Stufe „wiederholung“ statt „Test offen“ – dafür wird der abgeschlossene Flug-Test der alten Einheit als Test-Sitzung des Teils mitgeführt (Einfügen bucht keine Sterne; Trigger nur bei UPDATE).
- **LW-Rest:** `besprochen_aktiv` nutzt `fehler_endgueltig_am` (LW-S 2). Regression im Rauchtest 8: alte Markierung + endgültiger erster Fehlversuch → wieder offen; offener erster Anlauf → bleibt besprochen; ohne Fehler → bleibt.
- Neue Teile: freigegebene Einheiten, jede Etappe mit ≥ 1 Test-Aufgabe (lokal 0 Etappen ohne). Live fehlen noch die LK-D-Etappen `vierecke_konstruieren`, `vektor_koordinaten`, `vektor_drehen`, `wahre_groesse` – werden übersprungen und gemeldet; nach Einspielen der Aufgaben gehören sie in den jeweiligen Teil.

**Annahmen (bitte bestätigen oder ändern):**
- Vorläufige Orte = Kopie des bisherigen Orts („Titel · Teil k“) direkt dahinter; folgende Orte rücken nach.
- Expeditions-Aufgaben und Aufgaben ohne Etappe im Katalog (29: Potenz-Gruppen, 44: parallelen/winkelsumme, 46: parkett, 91: laengen) bleiben bei Teil 1.
- Einheit-Texte (Ziel, Merke) gelten noch fürs ganze Thema → Nacharbeit je Teil nötig.
- Freigegebene Einheit wird in der Transaktion kurz auf 'geprueft' gesetzt (Schutz-Trigger), danach wieder freigegeben.
- `klasse_fest` von Teil 1 aus der Liste (26 RS 6→5, 61 RS 9→8, 91 RS 8→7). RS II/III nicht nach Zusatz unterschieden.
- Erweiterung durch LK-D 3 (2, 57, 101): nur der Datenblock `v_daten` wächst, das Verfahren ist allgemein. Nicht berücksichtigt: Live-Abweichungen, die nach meinem Lesestand entstehen – vor dem Einspielen Rauchtest gegen live in Transaktion laufen lassen.

**Rückfrage Flug-Test (Fakten, live gelesen):**
- Flug-Test (Blocktest, `test_starten_intern`): **alle** Aufgaben des Pools „test“ der Einheit. Verteilung live: 546 Etappen mit 1, 84 mit 2, 1 mit 3 Test-Aufgaben.
- Wertung (`test_abschliessen_intern`): je Etappe „alle richtig“ (bool_and). Keine Quote: eine falsche Antwort → Etappe „fehler“ → Korrektur-Test (eine Aufgabe je Fehler-Etappe aus Pool „korrektur“) → „korrigiert“. Flug geschafft, wenn alle Pflicht-Etappen nachgewiesen/korrigiert/gesichert sind. Ein Fehler entscheidet also nicht über Bestehen, sondern löst eine Korrektur aus – unabhängig von der Etappenzahl.
- Nachtests nach 10/25/60 Lerntagen: je Pflicht-Etappe **eine** Aufgabe aus Pool „sicherung“. Einstufung mit Quote: ≥ 0,8 bestanden (Sicherung +1, bei 3 „gesichert“), ≥ 0,6 wiederholen, sonst Rückreise.
- Folge für kleine Teile: 2 Etappen (z. B. 61 T1, 46 T2/T3 live) → 1 Fehler = 50 % = **Rückreise**; 3 Etappen → 67 % = wiederholen; erst ab 5 Etappen kostet ein Fehler nur eine Stufe nicht.
- Vorschlag (Meinung): Nachtest mindestens **5 Aufgaben je Flug**, verteilt: 1 Etappe → 5, 2 Etappen → je 3, 3–4 Etappen → je 2, ab 5 → je 1. Dann gilt bei kleinen Teilen: 1 Fehler von 5–6 = 80–83 % = bestanden bzw. wiederholen, nie Rückreise. Dafür je Etappe genug Sicherungs-Aufgaben für 3 Runden ohne Wiederholung: bei 3 je Runde ≥ 9 (live 6–17 vorhanden – bei Etappen mit < 9 nachschreiben). Flug-Test (Blocktest) optional ebenso auf ≥ 2 Test-Aufgaben je Etappe bei Teilen mit ≤ 3 Etappen, damit ein Glückstreffer nicht reicht.
- Umsetzung braucht Änderung an `test_starten_intern` (Anzahl je Etappe aus Etappenzahl) – eigener Bau-Auftrag, nicht in TL-S.

## 2026-11-22 – FERTIG: LK-S Test (und Teil-Verfahren nach der neuen Teilungsregel)

Zweig `bau-lehrer`, auf `lernen-app` (Stand 15:50). Nichts eingespielt, kein DROP, kein DELETE.

**1. Test-Fehler `eintrag_bearbeitung_check`** (nur Test geändert)
- Erlaubte Werte laut echter Constraint: `originaltitel`, `deutsche_uebertragung`, `zusammenfassung_eigene_worte`, `redaktionelle_zuordnung`, `annahme`.
- Der Test legt seine drei Test-Einträge jetzt mit `annahme` an (vorher `original`).
- Gleich mitgeprüft: die übrigen Constraints und Trigger, die der Test berührt (`eintrag_parent_pruefen`, `zuordnung_*`, `einheit_status_check`, `einheit_schutz`, `aufgabe_schutz`, `block_thema` eindeutige Reihenfolge). Lokal bilde ich sie jetzt nach.

**2. Teilungsregel (22.11., 15:35/15:40)** – Datei `20261123_lk_s_thema_je_klasse.sql`, nur Abschnitt 5 `thema_teilen` (Vorlage, wird nicht aufgerufen; die übrige Migration ist unverändert)
- **Beliebig viele Teile, keine Mindestzahl:** `teile: [{etappen, neu, untertitel?, block_id?, einheit_id?}]`. Das alte Thema bleibt Teil 1.
  - Geprüft wird: kein Teil leer (auch Teil 1 nicht), alle disjunkt, zusammen genau der alte Katalog, jede Teil-Einheit hat genau ihre Etappen.
  - Die Kurzform mit nur einem Teil geht weiter.
- **Benennung:** alle Teile „‹Titel› – Teil k von n“, mit Untertitel „… · ‹Untertitel›“; abschaltbar mit `benennen: false`.
- **Kette:** Teil k braucht Teil k−1 (hart). Die übrigen Voraussetzungen ordnet `lehrplan-lb` den Teilen zu.
- **Neu, weil freigegebene Einheiten unveränderlich sind:** Live verbieten die Trigger `einheit_schutz` und `aufgabe_schutz`, eine freigegebene Einheit oder ihre Aufgaben zu ändern. Die erste Fassung (Katalog an Ort und Stelle verkleinern, Aufgaben umhängen) wäre an jedem echten Flug gescheitert. Jetzt:
  - Mit `rest_einheit_id` (neue Version des alten Themas mit den verbleibenden Etappen; Pflicht, wenn die alte Einheit freigegeben ist): alte Einheit → `ersetzt`. Die Aufgaben bleiben dort, damit Antworten und Sterne-Bezüge `aufgabe:` gültig bleiben.
  - Lernstand je Etappe zieht in Teil-1- bzw. Teil-Einheit.
  - Flug-Abschlüsse und abgeschlossene Tests der alten Einheit gehen an Teil 1.
  - Offene Misch-Ausgaben ihrer Aufgaben verfallen.
  - Ohne `rest_einheit_id` (nur bei nicht freigegebener alter Einheit): wie bisher Katalog verkleinern und Aufgaben umhängen.
- **Vorher/Nachher je Kind:** Wie bisher, jetzt über alle beteiligten Einheiten. Die Flug-Abschlüsse werden nach Anzahl und Zeitpunkt verglichen. Offene Misch-Ausgaben stehen jetzt im Bericht, weil sie bei `ersetzt` verfallen. Neu je Kind und Teil: erledigt / Etappen.
- **Test** Teil 7: drei Teile (2 + 1 + 3 Etappen) an einer freigegebenen Test-Einheit. Abgelehnt werden: leerer Teil, doppelte Etappe, leerer Teil 1, falscher Katalog, fehlende Rest-Version. Geprüft werden: Titel und Kette, Probelauf ohne Änderung, echter Lauf (`ersetzt`, Lernstand je Teil, Flug-Abschluss bei Teil 1, Sterne gleich, kein zweiter Bonus).
- Lokal grün (alle sieben Teile), Migration zweimal eingespielt.

**3. Wo „mindestens 3 Etappen“ vorausgesetzt wird** (live gelesen) – Folgen für Flüge mit 1–2 Etappen
- `schule.einheit_importieren` und `schule.einheit_abgleichen`: „Datei unvollständig“ bei weniger als 3 Etappen; Import zusätzlich erst ab 30 Aufgaben. **Ein Teil mit 1–2 Etappen lässt sich heute nicht importieren.** Das braucht eine Lockerung (eigener Auftrag, Sebastians Okay).
- `einheit_importieren` lehnt außerdem ab, wenn das Thema schon eine Einheit hat, die nicht `ersetzt` ist. Für die Rest-Version von Teil 1 muss die alte Einheit vorher auf `ersetzt` oder die Version anders angelegt werden. Das Teil-Verfahren erwartet die Einheiten fertig angelegt.
- Mischkarten: Regel `misch_ab_gelandet` (Vorgabe 3) wird über `einheit_lesen_intern` an die App gegeben. Ob sie je Flug oder insgesamt zählt, entscheidet die App (bitte bei `bau-motivation` prüfen). Zählt sie je Flug, gäbe es in einem Flug mit 1–2 Etappen nie Mischkarten.
- Flug-Test (`test_starten_intern`): je Pflicht-Etappe eine Aufgabe. Ein Flug mit 1 Etappe hat also 1 Testaufgabe (Quote 0 oder 100 %), mit 2 Etappen 2. Technisch geht das, als Test ist es dünn.
- Nachtests, Abschluss, Landung: keine Mindestzahl an Etappen gefunden (die „3“ dort sind 3 Lösungen in Folge bzw. 3 Nachtest-Runden).
- Expeditionen: mindestens 3 **Themen** (nicht Etappen). Mehr Teile machen das eher leichter.

## 2026-11-22 – FERTIG: LW-1 – App 0.88.0 „Unser Lehrplan“ (Reiter „Lehrplan“), Cache v163

Auf `lernen-app` (mit Vorgabe `inhalte/pruefung/lehrer/werkstatt/umsetzung.md`) und 0.87.2. Nur App, Version in sechs Dateien, Tests, Info-Seite. Nichts in der Datenbank, kein Merge nach `main`.
Bilder: `docs/previews/la/lw1-1280.png` (Detail offen), `lw1-820.png` (Fahrplan-Schublade), `lw1-400-fahrplan.png`, `lw1-400-detail.png`.

**Gebaut**
- **Kind-Seite mit drei Reitern** Überblick · Was wackelt · Lehrplan. Alte Adressen `#/kind/<id>-stand[-<schulart>]`, `-plan`, `#/plan/<id>`, `#/lernstand/<id>[-<schulart>]` führen auf „Lehrplan“ (mit Schulart → „Einordnen“). Links auf Überblick, „Zu tun“ und Info-Seite umgestellt. Der alte Reiter „Plan“ (viewPlan) ist entfernt; „Stand“ (Landkarte) ist nicht mehr erreichbar, „Alle Kinder im Vergleich“ bleibt.
- **Leiste:** Einordnen Gym | RS | IB · Zeigen Alle Themen | Noch nicht im Plan · n | Im Plan · n (hebt hervor, nichts verschwindet) · **Klassen 5–10 Mehrfachauswahl** (Standard: Klasse des Kindes bis 10, je Kind auf dem Gerät gemerkt `lw.kl.<id>`, blauer Punkt = Themen aus dem Fahrplan, mindestens eine bleibt an) · Einstieg prüfen ▾ (Ampel, Fehlendes hervorgehoben, „Orientierung, keine Einstufung“) · Suchen · Auswählen · Stand/„↶ Rückgängig“ dauerhaft. Legende einzeilig.
- **Fahrplan links (268 px):** Gerade dran (blau, Balken „Etappe x/y“), Kommt noch nummeriert (gelb), Ziehen am Griff ⋮⋮ und ↑ ↓ (Rechner beim Darüberfahren, Tablet/Handy immer), Ort mit mehreren Flügen „Flüge ▸“ klappt auf; unten zugeklappt „↻ In Wiederholung n ›“ und „✓ Fertig (kann er) n ›“ mit „Wieder in die Wiederholung“; „✎ Ändern lassen“ zum Plan. Darüberfahren hebt die Karten in der Matrix hervor.
- **Matrix:** Spalten Themengebiete (Kopf klebt), Zeilen Klassen (Klassen-Kasten klebt links) mit **drei Ringen** (groß gewählte Schule mit „%“ und „n/m Themen“, klein die beiden anderen), Rechnung nach Abschnitt 2 (gelandete Etappen / alle Etappen der Pflichtthemen, IB = Klasse − 5, aufgelöste zählen nicht). **Ganz gekonnte Klassen eingeklappt** („✓ Alles gekonnt · n Themen · davon m in Wiederholung · aufklappen ▾“). Beim Öffnen scrollt die Matrix zum ▶-Thema.
- **Karten** nach Abschnitt 3 (schon jetzt, nicht erst LW-2): blau gerade dran, hellgelb im Plan mit Platznummer, hellgrün Wiederholung, durchsichtig fertig, weiß eigene Schule, grau nur andere Schule; Stand-Zeile (`▶ Etappe 3/7`, `Platz 4`, `↻ Wdh 2/5`, `◉ kann er/gesetzt`, `2/7 begonnen`, `+ einplanen`), Schul-Kennzeichen `Gym 8 RS 7 IB 4` (Tablet/Handy `G8 R7 I4`), „+“ beim Darüberfahren.
- **Detail als Schublade** von rechts (390 px; Handy: Blatt von unten, 82 %): Kopf mit ✕ (auch Esc), Stand von ‹Kind› mit jeder Etappe (gelandet / Wiederholung / gerade dran „n von m“ / begonnen mit Fehlern / offen / freiwillig), Planen („In den Plan: als Nächstes ▾“ mit „… ans Ende“, „… nach Lehrplan einsortieren“; im Plan „Als Nächstes“, „Ans Ende“, „Aus dem Plan“), Stufe als Segment (Lernen | Kann er – wiederholen | Kann er komplett, bei ◉ „Wieder in die Wiederholung“), Lehrstoff („Inhalte ansehen (n Etappen) ›“, „Fehler besprechen (n) ›“, ohne Inhalt „Bitte Inhalte bauen“), Zusammenhang (Braucht vorher / Darauf baut auf als kleine Karten mit ✓ / Platz n / fehlt, antippen öffnet). Detail lädt `schule_lehrplan_thema` mit `lernender_id`.
- **Meldung unten** „‹Thema› als Nächstes eingeplant · ↶ Rückgängig“ (5 s). Speichern, Revision, Rückgängig mit Schritt des Servers, Konflikt „Neu laden“ (Seite gesperrt) wie bisher im Plan. Nach jedem Speichern werden Plan, Raster und Lernstand neu geholt.
- **Tablet (760–1099):** Matrix volle Breite, Fahrplan als Schublade von links über „Fahrplan · n“. **Handy (< 760):** Umschalter „Fahrplan · n | Alle Themen“, je Klasse eine Karte mit Kasten und Ringen.
- **Nachschlagen → Lehrplan:** keine Stufen-Knöpfe mehr; im Detail „Für ‹Kind› planen ›“ öffnet diesen Reiter mit dem Thema (Klasse wird eingeblendet und aufgeklappt). Der Klassenkopf trägt die Ring-Zahl derselben Rechnung (`data-ring`) – Test: gleiche Zahlen.
- Expeditionen des Kindes (früher unter „Stand“) stehen unter der Matrix.

**Abweichungen / Annahmen**
- Fahrplan-Eintrag = Ort (wie heute im Plan), Abschnitt 10 letzter Punkt; „Als Nächstes“ setzt den Ort vor den ersten „kommt noch“-Ort.
- Kein Ziehen Matrix ↔ Fahrplan und keine Reihenfolge-Warnungen – das ist LW-2. „Alle n einplanen“ ebenfalls LW-2.
- Rückgängig auch dauerhaft oben rechts (nicht nur 5 s in der Meldung), damit „Rückgängig“ aus „Plan“ nicht verloren geht.
- Die „Ort-Einstellung“ „alle Flüge: kann er komplett“ und „Ort aus dem Plan nehmen“ gibt es nicht mehr als eigene Knöpfe – dafür „Auswählen“ (mehrere Themen, ein Schritt).

**Getestet:** neu 6 LW-1-Tests (Reiter/Umleitungen, Klassenwahl, Ringe = Nachschlagen, Zeigen/Einstieg/Suche, Detail, Planen + Rückgängig, Ziehen/↑↓, Auswählen/Sammelaktion, Wieder in die Wiederholung, Konflikt „Neu laden“, 400/820/1280). 34 Tests des alten Plan-/Stand-Bildschirms entfernt, ihr Inhalt steckt in den LW-Tests; 12 weitere angepasst. Lernen alle grün. Gesamtlauf sonst nur Reise-Tests (bekannte + W132/W175 mit Tagesdatum). **Nicht geprüft:** echter Server, echte Geräte.

## 2026-11-22 – FERTIG: 0.87.2 – Nachprüfung Kinderansicht (S1, S2, K2, K3), Cache v162

Auf `lernen-app` eadcfb4, getrennt von LW-1 (LW-1 liegt noch unfertig zur Seite). Nur App, Version in sechs Dateien, Tests. Nichts in der Datenbank, kein Merge nach `main`.
- **S1:** Die Ansage „Vorher kurz einchecken“ steht jetzt direkt unter der Abflugtafel (vor Fortschritt, Stempel, Knobel). Zusätzlich über dem festen Knopf eine Zeile „Erst 9 Bordkarten Check-in · ca. 5 Min.“ (Zahl aus `offen` der Runde; nach Unterbrechung „Noch n …“). 360×640 und 400×860: Zeile einzeilig im Bild über „Weiter geht’s“.
- **S2:** Hinweis bei 5 Sternen als eigene Zeile über die volle Breite der Rückmeldung (am Ende des grünen Kastens, unter „Weg zur Lösung“), nicht mehr als schmale Mittelspalte.
- **K2:** Pause-Link „Pause – später weiter einchecken“ im Tag-Modus dunkel und fett (Kontrast ≥ 4,5).
- **K3:** Auswahl-Antworten mit `hyphens: auto` (Seite ist `lang="de"`), Umbruch nur noch mit Trennstrich.
Bilder: `docs/previews/la/0872-ansage-360.png`, `0872-fuenf-400.png`.

**Getestet:** neu 5 (S1 und S2 je 360×640 und 400×860, K2/K3). Gesamtlauf 310 grün; Fehler nur die bekannten Reise-Tests und W175 (rechnet mit dem Tagesdatum: „Tag 12“ statt „Tag 11“ seit Mitternacht – nicht von mir, betrifft die Reise-Seite). **Nicht geprüft:** echte Geräte.
## 2026-11-22 – FERTIG: LK-S 2 – Nacharbeit ChatGPT 934 (B1–B6, Befüllung aus lk_daten_2211.json)

Zweig `bau-lehrer`, auf `lernen-app` e9a0d66. In der gelieferten, noch nicht eingespielten Datei korrigiert: `supabase/migrations/20261123_lk_s_thema_je_klasse.sql`; Test `supabase/tests/lk_s_rauchtest.sql` neu gefasst. Nichts eingespielt, kein DROP, kein DELETE.
**Einspielen jetzt nach `rs_korrektur_2211.sql` UND `lk_korrektur_2211.sql`.** Schritt 0 bricht ab, wenn die LK-D-Korrektur fehlt.

**Muss**
- **B1:** `thema_lage_klasse` zeigt alle belegten Klassen, auch die vor `klasse_fest`.
  - Neue Spalte `klasse_route`: `klasse_fest`, sonst früheste Klasse; null = nicht in der Route dieser Schulart.
  - Die früheste Klasse heißt `neu`, die späteren `weitergefuehrt`. Route/Stufen/`thema_jahrgang` bleiben unverändert.
  - Test: Thema 61 in RS I 8 (neu) und 9 (Start der Route), `thema_jahrgang(61).rs_by` = 9.
- **B2:** `zuordnung.etappen = null` heißt „unbekannt“, nicht „alle“. Ganzes Thema nur ausdrücklich: `{*}`, beim Befüllen `"ganzes_thema": true`.
  - Je Klasse gibt es jetzt `etappen` (genannte), `ganzes_thema`, `etappen_unbekannt`. Etappen-`klasse_ab` zählt nur ausdrücklich genannte Etappen.
  - `klassen_kind`: `etappen_verlangt` und `etappen_erledigt` nur für genannte Etappen; bei nur unbekannten Etappen keine Zahl.
  - Test: 2 von 3, 1 von 3, unbekannt ohne Zahl, ganzes Thema 3 von 6.
- **B3** (Teilen): Je Teil mindestens 3 verschiedene Etappen; disjunkt; zusammen genau der alte Katalog; die neue Einheit hat genau die Etappen des neuen Teils.
  - Atomar wird der alte Katalog verkleinert: `inhalt.etappen`, `bewertung.lernziele_pflicht`, `lernziele_vertiefung`, `testaufgaben_je_lernziel`.
  - `aufgaben_umhaengen = false` bei vorhandenem Lernstand oder vorhandenen Antworten: abgelehnt.
  - Offene Test-Sitzung der alten Einheit: abgelehnt (ein laufender Flug-Test lässt sich nicht teilen – erst abschließen).
  - Der Rauchtest teilt 3 + 3; 2 + 4 und 4 + 2 werden abgelehnt.
- **B4** (Teilen, Vorher/Nachher je Kind):
  - Muss gleich bleiben, sonst Abbruch mit Unterschied: Lernstand je Etappe (über beide Einheiten nach Schlüssel), Lernziel-Stand, Sterne-Buchungen mit Bezug (Einheit im Bezug neutralisiert), Flug-Abschlüsse, abgelegt (Stempel), Plan, offene Misch-Ausgaben.
  - Im Bericht vorher/nachher (darf sich ändern): `thema_stufe` beider Teile (Stufe, `im_plan`), Reiseoptionen, Visum-Regeln.
  - Umgehängt werden zusätzlich offene Misch-Ausgaben (Lage), Was-wackelt-Einträge je Etappe und Rückmeldungen.

**Sollte**
- **B5:** Unbekannter Etappen-Schlüssel, leere Liste oder `*` zusammen mit anderen: Die Zuordnung bleibt ganz unverändert und wird mit Grund gemeldet.
- **B6:** „Abdeckung“ heißt jetzt Zuordnungsgrad.
  - Spalte `lehrplan_abdeckung.stunden_zugeordnet` (Schätzung: Stunden × Anteil der Punkte mit Thema).
  - In der Matrix heißt das Feld `lehrplan_zuordnung` statt `abdeckung`, mit `stunden` und `stunden_zugeordnet`; für die App „Lehrplan zugeordnet: x von y Stunden“.

**Befüllung:** jetzt aus `lk_daten_2211.json`: 690 Hauptbezüge aller drei Schularten, alle mit Etappen. Rolle und Etappen aus `rs_pruefung_2211.json` (erste Fassung) sind damit ersetzt, meine Titel-Zuordnung bei Thema 33 entfällt.
- Gruppe II/III und die IB-Ergänzungsquelle 23 sind in den Sichten nicht dabei (nur aktive Basis-Quellen). Deren Punkte stehen beim Einspielen unter „ohne Zuordnung“ bzw. tragen nur das Feld.
- Schlüssel, die es in der Datenbank noch nicht gibt (neue Etappen aus LK-D, die noch nicht eingespielt sind), meldet die Migration als „unbekannt“ und lässt die Zuordnung unverändert.

**Schnittstelle für die App (Änderungen gegenüber LK-S)**
- Matrix: `abdeckung` → `lehrplan_zuordnung` (`stunden_abgedeckt` → `stunden_zugeordnet`).
- Je Klasse neu: `route_start`, `ganzes_thema`, `etappen_unbekannt`; `etappen` nur ausdrücklich genannte.
- `klassen_kind`: `etappen_verlangt`/`etappen_erledigt` fehlen bei unbekannten Etappen.
- `weiter_in` je Klasse mit `ganzes_thema`/`etappen_unbekannt`.

**Test** `lk_s_rauchtest.sql` (lokal grün, Migration zweimal eingespielt; Ausschnitt der echten Lehrplan-Daten, Ersatz für `lehrplan_matrix`/`lehrplan_thema`)
1. Thema in zwei Klassen.
2. RS 8 I LB 4: 40 von 40 Std. zugeordnet.
3. B1 Thema 61.
4. Zweig II/III: 33 in 8 und 9.
5. B2 Stand je Klasse.
6. B5.
7. B3/B4 Teilen 3 + 3 mit Probelauf und echtem Lauf.

**Hinweis:** Laut LK-D erfüllt derzeit kein Thema die Teilungsregel. `thema_teilen` bleibt eine geprüfte Vorlage und wird nicht aufgerufen.

## 2026-11-22 – FERTIG: LW-S 2 – Nacharbeit ChatGPT 934 (A1, A2)

Zweig `bau-lehrer`, auf `lernen-app` e9a0d66. In der gelieferten, noch nicht eingespielten Datei korrigiert: `supabase/migrations/20261123_lw_s_wackelt_status.sql`; Test `supabase/tests/lw_s_rauchtest.sql`. Nichts eingespielt, kein DROP, kein DELETE. **Die Schnittstelle bleibt gleich.**

- **A1:** „Neuer Fehler öffnet wieder“ richtet sich jetzt nach der endgültigen Wertung. Neue Hilfsfunktion `schule.fehler_endgueltig_am(versuch)` liefert, wann eine Antwort endgültig falsch wurde:
  - falsche Testantwort und 2. Anlauf bzw. Antwort ohne zweite Chance: sofort;
  - 1. Anlauf: nach 30 Minuten oder beim Weitergehen, je nachdem, was zuerst kommt (wie `versuch_wertung`);
  - neutral, ersetzt oder noch offen: zählt nicht.
  - `wackelt_fehler` und `wackelt_liste` benutzen beide diese Funktion. Verglichen wird mit dem Zeitpunkt, an dem die Antwort endgültig wurde. Darum öffnet auch ein Fehler, der vor dem Status gegeben, aber erst danach endgültig wurde.
- **A2:** Zugangstest mit Lern-Zugängen, die der Test selbst anlegt (zufällige Schlüssel, Rollback).
  - Abgelehnt: Kind-Zugang beim eigenen und beim fremden Kind (lesen und setzen), gesperrter Zugang, abgelaufene Sitzung.
  - Erlaubt: Lehrer liest beide Testkinder und setzt; `status_von` = „lehrer:Name“.
  - **Hinweis:** Laut `schule.sieht` sehen Eltern/Lehrer mit Lern-Zugang alle Kinder. Ein „fremdes Kind“ gibt es für sie nicht. Council-Schlüssel mit Kind-Freigabe (`schule.zugang`) habe ich nicht getestet, weil das echte Council-Zugänge bräuchte.
- **Test** (lokal grün, Migration zweimal eingespielt): neu Teil 3 (offener 1. Anlauf öffnet nicht → durch Weitergehen endgültig → wieder „zu besprechen“; neutraler 2. Anlauf öffnet nicht) und Teil 6 (Zugänge).

## 2026-11-22 – FERTIG: FP-S 4 – Sperrreihenfolge Mischkarte (ChatGPT 932, Sollte 1 und 2)

Zweig `bau-lehrer`, auf `lernen-app` 3f693c4. Nur Dateien, **nicht eingespielt**, kein DROP, kein DELETE, kein App-Code.
Neue Datei: `supabase/migrations/20261123_fp_s4_sperrfolge.sql`, einspielen nach FP-S 3.
Gelesen (nur lesend): FP-S 3 ist in der Live-Datenbank schon drin (`misch_buchen`, `uebung_pruefen_wd`). `versuch_misch_verfall` und `misch_buchen` sind live gleich wie in meiner Testdatenbank.

**Befund (Sollte 1)**
Regel überall: erst die Etappe (`karte_stand`), dann die Ausgabe (`misch_ausgabe`). Ein Zyklus ist nur möglich, wenn eine Transaktion die Ausgabe hält und danach auf die Karte wartet.
- **Mischpfad** (`uebung_pruefen_wd`, FP-S 3): Etappe → Ausgabe. ✓
- **Normale Antwort, Trigger `versuch_misch_verfall`:** Die Trigger laufen in Namensfolge, also bucht `versuch_karte` vorher und sperrt dabei die Etappe. Etappe → Ausgabe. Ohne Buchung (1. Anlauf falsch, Wertung offen) sperrt der Trigger nur die Ausgabe und wartet danach auf nichts mehr. Kein Zyklus, aber auch keine feste Regel.
- **`misch_buchen` – echte Lücke:** Es löst erst die Ausgabe ein und schreibt dann die Karte. Über den Mischpfad ist die Etappe schon gesperrt. Bucht aber `offene_entscheiden` einen früheren, offenen Mischkarten-Versuch (1. Anlauf falsch) aus einer Antwort ohne Misch-Wunsch, gilt Ausgabe → Etappe. Gleichzeitig mit einer Mischkarten-Antwort (Etappe → Ausgabe) ist ein Deadlock möglich.
- **`mischkarten`** (Ausgeben/Verfallen) sperrt keine Karte und wartet danach auf nichts. Kein Zyklus.

**Gebaut**
- `versuch_misch_verfall` sperrt zuerst die Etappe, nur wenn es eine offene Ausgabe gibt.
- `misch_buchen` sperrt zuerst die Etappe.
- Eine Sperre, die die Transaktion schon hält, kostet nichts. Bestand unverändert (wird in der Migration geprüft).

**Tests** `wd_s3_gleichzeitig.sh` (lokal mit allen acht Migrationen zweimal hintereinander grün, 9 × ok)
- **Neu G1/G2:** Mischkarte und normale Antwort zur selben Aufgabe gleichzeitig, beide Reihenfolgen. Geprüft: kein Deadlock (abgebrochener Prozess = FEHLER), höchstens einmal gültig, gültig ⇔ eingelöst, sonst verfallen, genau ein Fortschritt, einmal Wiederholungs-Sterne. Ergebnis: Mischkarte zuerst → gültig; normale Antwort zuerst → verfallen, nicht gültig.
- **Sollte 2:** E und F prüfen jetzt reihenfolgeunabhängig.
  - E: genau eine von zwei Antworten gültig, egal welche.
  - F: Mischkarte gültig und eingelöst, wenn sie die Sperre wirklich zuerst bekam, sonst nicht gültig und verfallen; in beiden Fällen ein Fortschritt.
- **Gegenprobe ohne FP-S 4:** G1/G2 sind auch dann grün, weil der normale Pfad über `versuch_karte` schon Etappe → Ausgabe sperrt. Die behobene Lücke (`offene_entscheiden` → `misch_buchen`) lässt sich im Test nicht zuverlässig zeitlich herbeiführen; sie ist oben begründet.

**Hinweis, nicht geändert:** Zwei gleichzeitige `mischkarten`-Aufrufe für dasselbe Kind setzen mehrere Ausgaben in einem UPDATE auf verfallen. Ein Deadlock zwischen ihnen ist nur denkbar, wenn sie die Zeilen in verschiedener Folge sperren. Das betrifft die Sperrfolge Etappe → Ausgabe nicht. Bisher nicht beobachtet.

## 2026-11-22 – FERTIG: LK-S – ein Thema in mehreren Klassen (Server)

Zweig `bau-lehrer`, auf `lernen-app` 22251c0. Nur Dateien, **nicht eingespielt**, kein DROP, kein DELETE, kein App-Code.
Neue Dateien:
- `supabase/migrations/20261123_lk_s_thema_je_klasse.sql` – einspielen **nach** `inhalte/pruefung/lehrplan/rs_korrektur_2211.sql`, in einer Transaktion;
- `supabase/tests/lk_s_rauchtest.sql`.

Geändert: `supabase/tests/fp_s_rauchtest.sql` Teil 5. Er läuft jetzt auch, wenn das Testkind schon eine Nachbuchungs-Zeile hat; diese bleibt unverändert.
Gelesen (nur lesend): `rs_korrektur_2211.sql` ist live noch nicht eingespielt. Jedes Thema hat `klasse_fest` für RS und IB.

**Schnittstelle für die App** (alle alten Felder bleiben; fehlen die neuen, bleibt die alte Anzeige)
- `schule_lehrplan_matrix`
  - Eltern/Lehrer, je Thema `klassen`: `{schulart: {zweig: [{klasse, rolle: neu|weitergefuehrt, etappen?, lernbereiche: [{eintrag_id, pfad, titel, stunden}], stunden, rolle_lehrplan?, nur_klasse_fest?}]}}`.
    - Zweige: `gym_by.allgemein`, `rs_by.rs_I` / `rs_by.rs_II_III`, `ib_myp.myp_standard` / `ib_myp.myp_extended`.
    - `etappen` fehlt = ganzes Thema; sonst die Lernziel-Schlüssel, die in dieser Klasse verlangt sind.
  - Oben neu `abdeckung`: `{schulart: {zweig: {"<klasse>": {stunden, stunden_abgedeckt, lernbereiche: [{eintrag_id, pfad, titel, stunden, punkte, punkte_mit_thema, stunden_abgedeckt}]}}}}`.
  - `kinder[].zweig`.
  - Kindsicht: je Thema nur `klassen_kind: [{klasse, rolle, etappen?}]` (Schulart und Zweig des Kindes) und oben `zweig`.
- `schule_lehrplan_thema {thema_id, lernender_id?}`
  - Zusätzlich `klassen` (wie oben) und `etappen_titel {lernziel: titel}`.
  - `baut_auf: [{thema_id, titel, art, klassen: {"rs_by/rs_I": 7, …}, verstoss: ["rs_by/rs_II_III", …]}]`. `verstoss` heißt: Die Voraussetzung liegt in dieser Schulart/diesem Zweig später als das Thema.
  - `weiter_in: {"rs_by/rs_II_III": [{klasse: 9, etappen?}]}`.
  - Mit Kind zusätzlich `zweig` und `klassen_kind: [{klasse, rolle, etappen?, etappen_verlangt, etappen_erledigt}]` („2 von 3 Etappen dieser Klasse“; erledigt = gelandet oder gesetzt). Eltern/Lehrer übergeben `lernender_id`; der Zugriff auf das Kind wird geprüft. Kindsicht: `klassen_kind`, `baut_auf` (mit Klasse).
- **Regeln** (wie in `rs_pruefung_2211.md` Abschnitt 6):
  - Klassen aus Hauptbezügen aktiver Basis-Quellen, ohne archivierte Einträge und ohne Zuordnungen mit `klaerungsbedarf`.
  - RS 5/6 „allgemein“ gilt für beide Gruppen.
  - `klasse_fest` gewinnt: Es ist die erste Klasse (null = kein Pflichtstoff dieser Schulart), frühere Klassen fallen weg.
  - Rolle je Klasse: die erste Klasse `neu`, spätere `weitergefuehrt`. Die Aussage der Prüfung steht zusätzlich in `rolle_lehrplan`.
  - Lernstand und Sterne bleiben je Thema/Etappe einmal.
- Stand je Klasse und „Flug bleibt Flug“: `thema_stufe`, Flug-Abschluss und Stempel sind unverändert und gelten fürs ganze Thema; `klassen_kind` zeigt nur zusätzlich den Stand der Etappen dieser Klasse.

**Server**
- **Felder:** `schule.zuordnung.rolle`, `.etappen`; `schule.lernender.zweig` (`rs_I` | `rs_II_III`; leer = `rs_I`). Für IB gilt vorerst `myp_standard` (**Annahme**, es gibt kein IB-Kind-Feld).
- **Sichten:** `schule.lehrplan_zweig`, `schule.thema_lage_klasse`, `schule.thema_lage` (je Etappe `klasse_ab`, `klassen[]`, `rollen`), `schule.lehrplan_abdeckung`.
- **Befüllen:** `schule.lehrplan_rolle_setzen(jsonb)` ist wiederholbar. Es ändert nur vorhandene Zuordnungen und meldet fehlende Zuordnungen und unbekannte Etappen. Die Migration befüllt damit die Realschule aus `rs_pruefung_2211.json`: 409 Vorschläge, davon 19 mit Etappen. Gym/IB später aus `lk_daten_2211.json` mit derselben Funktion.
  - Titel → Schlüssel (**Annahmen**, bitte von `lehrplan-lb` prüfen lassen): 33 „Steigung m und Achsenabschnitt t, Parameter“ → `ablesen`, `wirkung`; „Geradengleichung aus zwei Angaben, Parallelenscharen“ → `zwei_punkte`, `lage`.
  - 44/931 „Vierecke konstruieren (Etappe fehlt)“ ohne Etappe.
  - Gruppe II/III ist im Korrektur-SQL nicht eingespielt; deren Vorschläge treffen nur, wo die Zuordnung schon so besteht. Die Zahl meldet die Migration beim Einspielen.
- **Teilen eines Themas** (Nachtrag „Route“): `schule.thema_teilen(plan, probelauf default true)`, nur angelegt, nicht aufgerufen. Ablauf:
  1. Thema anlegen (über `schluessel` wiederholbar), Kann-Texte, Ort (`block_id`), Voraussetzung „Teil 2 braucht Teil 1“ (hart), Zuordnungen mit nur diesen Etappen umhängen.
  2. Mit `neue_einheit_id` (vorher per `einheit_importieren` angelegt): Aufgaben, Karten, Lernziel-Stand, besprochen, Was wackelt, Wiederholungs-Runden, Staffel-Sicherung, abgelegt und Rückmeldungen umhängen. Sterne-Bezüge `landung:`/`wdh:` werden mitgezogen; Menge gleich, kein zweiter Bonus.
  3. Vorher/Nachher je Kind (gelandet, gesetzt, Karten, Sterne, Flug-Abschlüsse, Plan) muss gleich sein, sonst Abbruch. Je Kind `neu_vollstaendig`.
  - Weniger als 3 Etappen: abgelehnt. **Nicht drin:** Nachtrag Stempel/Bonus für den neuen Teil (Festlegung 14) und Plan/Route für den neuen Ort (Reise-Aufbau).
- **Vorher/Nachher in der Migration** (sonst Abbruch): `thema_stufe` aller Kinder × Themen, Reiseoptionen, Klassen (`thema_jahrgang`), Kinder (ohne neues Feld), Plan, Karten, Lernziel-Stand, Sterne, Flug-Abschlüsse, Visum-Regeln, Themen, Voraussetzungen, Orte.

**Test** `lk_s_rauchtest.sql` (Rollback, Testkind, Test-Thema; lokal grün, Migration zweimal eingespielt)
1. Thema in zwei Klassen (neu + weitergeführt) erscheint in beiden, Matrix mit Abdeckung und alten Feldern.
2. RS 8 I Lernbereich 4 = 40 Std., abgedeckt 40.
3. Testkind II/III: Thema 33 in 8 und 9, Gruppe I nur in 8; Stufen durch den Zweig unverändert; Detail mit Stand je Klasse.
4. Befüllen wiederholbar, Meldungen.
5. Teilen: Schritt 1 ohne Einheit, Probelauf ändert nichts, echter Lauf hängt um (Sterne-Summe gleich, kein zweiter Bonus), < 3 Etappen abgelehnt.

**Offen / nicht geprüft**
- Nicht gegen die Live-Datenbank gelaufen. Lokal mit einem Ausschnitt der echten Lehrplan-Daten (Ids wie live) und Ersatz für `lehrplan_matrix`/`lehrplan_thema`. Die Erwartungen 40 Std. und 33 in 8/9 habe ich live nachgelesen (Zuordnungen bestehen schon so).
- Laufzeit der Matrix mit allen Themen live nicht gemessen; die Sichten rechnen bei jedem Aufruf.

## 2026-11-22 – FERTIG: LW-S – „Was wackelt“ mit gespeichertem Status (für LW-3)

Zweig `bau-lehrer`, auf `lernen-app` 22251c0. Nur Dateien, **nicht eingespielt**, kein DROP, kein DELETE, kein App-Code.
Neue Datei: `supabase/migrations/20261123_lw_s_wackelt_status.sql`. Unabhängig von LK-S und den WD/FP-Dateien; braucht nur LA-3 (`schule.besprochen`, ist live).

**Schnittstelle** (in `lernen-api` freigeschaltet, Version 0.9.2; nur Eltern/Lehrer, Zugriff auf das Kind geprüft)
- `schule_wackelt_lesen {lernender_id}` → `{ok, lernender_id, zu_besprechen, eintraege: [...]}`
  - `zu_besprechen` = Zahl für den roten Punkt am Reiter.
  - Je Eintrag: `thema_id`, `titel`, `einheit_id`/`lernziel` (null = ganzes Thema; gesetzt = Eintrag für eine Etappe), `status` (wirksam: `zu_besprechen` | `beobachten` | `besprochen`), `quelle` (`gespeichert` | `vorgabe`), `status_gespeichert`, `status_am`, `status_von`, `wieder_offen` (gespeichert war besprochen/beobachten, aber danach neue Fehler), `fehler` (endgültig falsche Antworten), `fehler_neu` (seit dem Status), `letzter_fehler_am`, `etappe` (die mit dem letzten Fehler – für die Zeile „Etappe: …“), `etappen` (alle mit Fehlern: `einheit_id`, `lernziel`, `titel`, `fehler`, `letzter_fehler_am`, `wackelt`, `sitzt`, `besprochen_am`).
  - Sortiert: zu besprechen → beobachten → besprochen, darin neueste Fehler zuerst.
- `schule_wackelt_setzen {lernender_id, thema_id, status, einheit_id?, lernziel?}` → `{ok, eintrag, zu_besprechen}` (`eintrag` im selben Format, gleich neu berechnet). Erneutes Setzen überschreibt Zeitpunkt und Person.
- Aufgabe und Antwort zum Aufklappen weiter aus `schule_lernstand` (je Etappe `fehler[]`), dort unverändert.

**Regeln**
- Neue endgültig falsche Antwort im Thema (bzw. in der Etappe) nach dem Status → wieder `zu_besprechen`. „Endgültig“ wie bei LA-3: der 1. Versuch mit zweiter Chance zählt nicht. Ausgewertet beim Lesen; beim Antworten wird nichts geschrieben.
- Hat eine Etappe einen eigenen Status, ist sie ein eigener Eintrag und steht nicht mehr im Eintrag ihres Themas.
- **Annahme (bitte bestätigen):** Ohne gespeicherten Status gilt eine Vorgabe:
  - `zu_besprechen`, wenn eine Etappe wackelt (Regel wie in der App: nicht gelandet und wieder offen, oder ≥ 3 falsch und mehr falsch als richtig) und nicht als besprochen markiert ist (LA-3);
  - `besprochen`, wenn alle Etappen mit Fehlern als besprochen markiert sind;
  - sonst `beobachten`.
  - Damit entspricht die Zahl am ersten Tag etwa dem heutigen „offen“ (wackelt und nicht besprochen), nur je Thema statt je Etappe.
- `schule.besprochen` (LA-3, „Besprochen ✓“ je Etappe) bleibt wie es ist; `schule_wackelt_setzen` schreibt dort nicht hinein.

**Test** `supabase/tests/lw_s_rauchtest.sql` (Rollback, nur Testkind, Thema ohne Antworten des Testkinds; lokal grün, Migration zweimal eingespielt)
1. drei Fehler → `zu_besprechen` (Vorgabe), Zahl +1;
2. besprochen gesetzt (wer, wann), Zahl zurück, Lernstand/Sterne/Plan/Kinder/Antworten unverändert;
3. 1. Versuch mit zweiter Chance zählt nicht, danach ein neuer Fehler → wieder `zu_besprechen`;
4. Etappe mit eigenem Status → eigener Eintrag, kein Doppel, erneutes Setzen überschreibt;
5. falscher Status, fremde Etappe, halbe Etappe, Aufruf ohne Eltern-/Lehrer-Recht abgelehnt.

Nicht gegen die Live-Datenbank gelaufen (lokal mit Nachbau; die benutzten Spalten habe ich live nachgelesen).

## 2026-11-22 – FERTIG: 0.87.1 – Nachbuchungs-Hinweis beim Server quittiert (Nachtrag FP-S 3), Cache v161

Auf `lernen-app` b359169 (mit FP-S 2: `gesehen_am`, Aktion `schule_landung_nachbuchung_gesehen`). Nur App, Version in sechs Dateien, Tests. Nichts in der Datenbank, kein Merge nach `main`.
- Karte „★ Geschenk für deine Landungen“ erscheint nur, wenn `schule_konto.landung_nachbuchung.gesehen_am` leer ist.
- „Super ›“ schließt die Karte sofort und ruft `schule_landung_nachbuchung_gesehen {lernender_id}` auf (einmal); `gesehen_am` aus der Antwort wird übernommen. Damit gilt „gesehen“ auf allen Geräten.
- localStorage (`lern.fpnach.<kind>.<am>`) nur noch als Rückfall: wird weiter gesetzt und geprüft, damit die Karte nicht wiederkommt, wenn der Server die Aktion noch nicht kennt oder der Aufruf scheitert. Kein Fehlerhinweis ans Kind.

**Getestet:** neu FP-5 (Quittung genau einmal mit `lernender_id`; nach Neuladen ohne localStorage weg, weil der Server `gesehen_am` liefert; Server-Fehler → Karte bleibt weg über den Rückfall); FP-1–4 weiter grün. Gesamtlauf 306 grün, nur die 9 bekannten Reise-Fehler. **Nicht geprüft:** echter Server (FP-S 2 nicht eingespielt).
## 2026-11-22 – FERTIG: FP-S 3 – Nacharbeit ChatGPT 929 (Mischkarte atomar einlösen)

Zweig `bau-lehrer`, auf `lernen-app` b359169. Nur Dateien, **nicht eingespielt**, kein DROP, kein DELETE, gelieferte Migrationen unverändert, kein App-Code, kein Merge nach `main`.
Neue Datei: `supabase/migrations/20261122_fp_s3_nacharbeit_929.sql`. Einspielen nach FP-S 2: WD-S 2 → WD-S 3 → WD-4b → WD-S 4 → FP-S → FP-S 2 → **FP-S 3**.
Gelesen (nur lesend): FP-S 2 ist in der Live-Datenbank schon eingespielt; die Stellen, die FP-S 3 umbaut (`misch_buchen`, `versuch_buchen`, `sterne_aus_versuch`, `uebung_pruefen_wd`), sind dort gleich wie in meiner Testdatenbank. Einziger Weg zur Prüfung ist `api.schule_uebung_pruefen` → `uebung_pruefen_wd`.

**Gebaut**
1. **Eine Sperre für Gültigkeit und Einlösen:** `uebung_pruefen_wd` sperrt bei einer Mischkarte zuerst die Etappe (`karte_stand`, dieselbe Sperre wie jede Antwort auf diese Etappe) und dann die offene Ausgabe, und prüft erst danach mit dem Stand nach der Sperre. Folge: Eine zweite Antwort auf dieselbe Karte (andere `client_id`) wartet und sieht die Ausgabe eingelöst. Eine Antwort auf eine andere Aufgabe derselben Etappe ist entweder vorher fertig (dann ist die Mischkarte ungültig) oder wartet bis nach dem Einlösen.
2. **Tatsächlicher Ausgang:** `misch_buchen` meldet, ob wirklich eingelöst und als Mischkarte gebucht wurde. Im Rückfall wird normal gebucht, aber **ohne Wiederholungswertung** (`kein_wdh`). Außerdem: `versuch.misch = false`, Sterne wie eine normale Übung, Antwort `misch.gueltig = false`.

**Für die App:** keine neue Schnittstelle. `misch.gueltig` meldet jetzt den tatsächlichen Ausgang (bisher die Vorprüfung).

**Tests** (lokal PG 16, alle sieben Migrationen je zweimal eingespielt)
- `wd_s3_gleichzeitig.sh` neu:
  - **E:** dieselbe Mischkarte mit zwei `client_id` → eine `gueltig: true`, eine `false`, ein Fortschritt (Stufe 1 → 2), einmal eingelöst, ein Mischkarten-Versuch.
  - **F:** Antwort auf eine andere Aufgabe der Etappe läuft, Mischkarte wird währenddessen eingelöst → `gueltig: false`, nicht eingelöst, nur der eine Fortschritt der normalen Antwort.
  - **D2:** zwei Nachbuchungen gleichzeitig auf denselben Landungs-Bonus → genau einmal gebucht, Meldungen zusammen = Summe.
  - A–D weiter ok, Ergebnis ok (zweimal hintereinander).
- **Gegenprobe ohne FP-S 3:** E meldet zweimal gültig (zwei Mischkarten-Versuche), F meldet gültig und löst ein → FEHLER. Der Test greift also. D2 ist auch ohne FP-S 3 ok (dort schützt der eindeutige Schlüssel der Sterne).
- `fp_s_rauchtest.sql` Teil 9: Rückfall erzwungen (Ausgabe vor dem Einlösen schon eingelöst) → Ausgang „Rückfall“, Versuch nicht als Mischkarte, keine Wiederholungswertung, 10 Sterne wie Übung. Danach dieselbe Karte über `uebung_pruefen_wd` → keine Bestätigung. Ohne FP-S 3 wird Teil 9 übersprungen. Die drei Rauchtests sind grün.

**Offen / nicht geprüft**
- Nicht gegen die Live-Datenbank gelaufen; lokal mit Nachbau von `uebung_pruefen_intern`.
- Bei einer Mischkarte wird die Etappe jetzt kurz gesperrt: Gleichzeitige Antworten auf dieselbe Etappe warten aufeinander. Andere Etappen warten nicht.

## 2026-11-22 – FERTIG: FP-S 2 – Nacharbeit ChatGPT 924

Zweig `bau-lehrer`, auf `lernen-app` 3e333b6. Nur Dateien, **nicht eingespielt**, kein DROP, kein DELETE, gelieferte Migrationen unverändert, kein App-Code, kein Merge nach `main`.
Neue Datei: `supabase/migrations/20261122_fp_s2_nacharbeit_924.sql`. Einspielen nach FP-S: WD-S 2 → WD-S 3 → WD-4b → WD-S 4 → FP-S → **FP-S 2**.

**Gebaut**
1. **`sterne` nur aus diesem Aufruf:** keine Differenz der Kind-Summe mehr. Ein Zähler je Aufruf (`schule.aufruf_sterne`, transaktionslokal) wird von einem Trigger auf `schule.sterne` (AFTER INSERT) hochgezählt; `uebung_pruefen_wd` setzt ihn vor der Prüfung auf 0 und liest ihn danach. Sterne, die eine andere Sitzung gleichzeitig für dasselbe Kind bucht (Nachbuchung, zweites Gerät), landen nicht mehr in der Antwort. `misch.sterne` ebenso.
2. **Misch-Gültigkeit einmal entschieden:** `uebung_pruefen_wd` entscheidet einmal (`schule.misch_entscheid` = Aufgabe:t/f) und reicht das an die Wertung (`misch_gueltig` übernimmt die Entscheidung für genau diese Aufgabe) und an die Antwort (`misch.gueltig`) durch. Kein zweites Nachrechnen mit anderem Ergebnis.
3. **Nachbuchungs-Hinweis „gesehen“ im Server:** Spalte `landung_nachbuchung.gesehen_am` (je Kind), Aktion setzt sie einmal (späteres Antippen ändert den Zeitpunkt nicht).

**Schnittstelle für die App**
- `api.schule_landung_nachbuchung_gesehen` – Daten `{lernender_id}` (Zugriffsprüfung wie alle Lern-Aktionen; in `lernen-api` freigeschaltet, Version 0.9.1) → `{ok: true, gesehen_am}`.
- `schule_konto.landung_nachbuchung` hat zusätzlich `gesehen_am` (null = Hinweis noch zeigen). `localStorage` ist damit nicht mehr nötig; bei altem Server (Feld fehlt) bisheriges Verhalten.
- `sterne` und `misch.sterne` der Antwort: Bedeutung gleich, jetzt nur noch die Buchungen dieser Antwort. Abzug von `landung.bonus` in der App bleibt richtig.

**Tests** (lokal PG 16, alle sechs Migrationen je zweimal eingespielt; Rollback bzw. Wegwerf-Datenbank, nur Testkind)
- `fp_s_rauchtest.sql` Teil 8: 1 Fehler → 40, Tipp → 80, zweiter Versuch (erst falsch, dann richtig) → 80 und kein Fehler, gültige Mischkarte mit Tipp → `misch.gueltig` true, 0 Sterne, Fehler nach der Landung ohne Wirkung, Wiederlandung ohne zweiten Bonus, Misch-Entscheidung übernommen, Hinweis gesehen. Durchgelaufen; WD-S- und WD-S-3-Rauchtest weiter grün.
- `wd_s3_gleichzeitig.sh`: wartet jetzt auf jeden Prozess einzeln (Abbruch = FEHLER, Exit 1). Neu C: Antwort, während eine andere Sitzung 7 Sterne bucht → Antwort meldet 10. Neu D: Landung gleichzeitig mit Nachbuchung → Landung 90 (10 + Bonus 80), Nachbuchung 320, Summe +410 = 90 + 320. Gegenprobe ohne FP-S 2: C meldet 17, D meldet 410 → FEHLER (Test greift).

**Offen / nicht geprüft**
- Nicht gegen die Live-Datenbank gelaufen (nur lokal mit Nachbau von `uebung_pruefen_intern`).
- `sterne_wdh_richtig` unverändert 10 (Sebastians Entscheidung offen).

## 2026-11-22 – FERTIG: 0.87.0 – faire Punkte (FP-App), Cache v160

Auf `lernen-app` 55d8921 (mit FP-S und Vorgabe „faire Punkte“ des Gestalters). Nur App, Version in sechs Dateien, Tests. Nichts in der Datenbank, Nachbuchung nicht ausgeführt, kein Merge nach `main`.
Bilder: `docs/previews/la/fp-landung-360.png` (Sturmflug + 40, 360 × 640), `fp-landung-1280.png`.

**Gebaut nach `inhalte/pruefung/kind/faire-punkte/umsetzung.md`** (gilt vor dem Wortlaut im Auftrag)
- **Sterne nach der Antwort (2):** aus `sterne` der Antwort, **abzüglich** `landung.bonus` und Ablegen-Sterne (die stehen in ihren Einblendungen) – also „+10“ bzw. „+5“. Hinweis darunter klein und grau: mit Tipp „Ganz ohne Tipp gibt es 10 ★.“, im 2. Versuch „Gleich beim ersten Mal gibt es 10 ★.“ (10 aus `regeln.sterne_uebung_richtig`), höchstens einmal je Etappe und Lerntag (Gerät, `localStorage`), keine Wörter wie „nur/leider/weniger“. Fehlt `sterne` (alter Server), bleibt die bisherige Anzeige. Die Rückmeldung heißt im Abflug-Design weiter „✓ An Bord · +5 Sterne“ (bisheriger Stil), nicht „Richtig! +5 ★“ – bei Wunsch angleichen.
- **Landungs-Bonus (1):** eigene Kachel im Blatt aller drei Fassungen, unter der Sternzeile, über dem Knopf: „★ Landungs-Bonus · ohne Fehler gelandet · +80 ★“ (Gold-Rand, heller Gold-Grund, Funken) / „mit 1 Fehler gelandet“, „mit 2 Fehlern gelandet“ +40 / „gelandet – geschafft!“ +10 (Rand in der Fassungsfarbe). Beim Sturmflug nie eine Fehlerzahl. Kein „Direktflug“, kein Vergleich. Zahl zählt hoch, Kachel schiebt ein (≤ 0,8 s, abschaltbar, Antippen beendet). Unter 680 px Höhe fällt Zeile 2 weg; 360 × 640 ohne Scrollen (Test). Fehlt `landung.bonus`: keine Kachel. **Nicht gebaut:** das Fliegen von „+80“ zu einem Sterne-Zähler oben – die Etappen-Einblendung hat oben keinen Zähler.
- **Geschenk nach der Nachbuchung (3):** aus `schule_konto.landung_nachbuchung` (oberste Ebene der Antwort, neben `konto`) eine schmale Gold-Karte über der Abflugtafel (und im bisherigen Design oben): „★ Geschenk für deine Landungen – Für deine bisherigen Landungen gibt es nachträglich +n ★ Landungs-Bonus.“ [Super ›]. „Super ›“ merkt sich das **auf dem Gerät** (je Kind und `am`) – der Server kennt kein „gesehen“; auf einem zweiten Gerät erscheint die Karte noch einmal. **Vorschlag an bau-lehrer:** Aktion zum Quittieren oder `gesehen_am` in `landung_nachbuchung`.
- **Info-Seite (4):** neuer Eintrag „Sterne:“ mit dem Wortlaut der Vorgabe (10/5, Landungs-Bonus 80/40/10, Tipps keine Fehler, Tests/Wiederholungen/Mischkarten zählen nicht, Wiederholungen 10 selbst gelöst, Nachtrag vor dem 22.11., nie abgezogen); „Belohnungen:“ nennt nur noch Test, Ablegen, Knobeln, Ort.
- **Offen beim Server:** Die Vorgabe sagt, „Flug geschafft“ solle den Bonus nicht noch einmal zählen – „Flug geschafft“ zeigt `sterne_flug.summe` vom Server; ob der Bonus darin steckt, entscheidet die Server-Summe.

**Getestet:** lernen 163 von 163 (neu 4: Bonus-Kachel in allen Fassungen und Stufen, Sturmflug ohne Fehlerzahl, ohne `landung` keine Kachel, 360×640/400/820/1280; Serverwert +5 und Hinweis einmal je Etappe/Tag; Geschenk-Karte einmal, 360/820/1280; Info-Seite). Gesamtlauf sonst nur die bekannten Reise-Fehler. **Nicht geprüft:** echter Server (FP-S nicht eingespielt), echte Geräte.

## 2026-11-22 – FERTIG: 0.86.3 – Nachtrag WD-S 4 (ChatGPT 921), Teil bau-motivation (Cache v159)

Auf `lernen-app` d0e911e. Nur App, Version in sechs Dateien, Tests. Nichts in der Datenbank, kein Merge nach `main`.
- **Keine frische Aufgabe (Sollte 2):** „Noch 3 Extra-Bordkarten?“ erscheint nur noch, wenn mehr fällig ist **und** der Server dafür wählbare Bordkarten liefert (`aufgaben[]` ohne `pflicht` bzw. nach der Runde überhaupt welche). Sonst steht ruhig „Heute keine passende frische Aufgabe – bleibt für später offen.“ – auf der Abflugtafel (beide Designs), nach „Eingecheckt!“ und auf `#/wiederholen/<kind>-extra`.
- **Kein „für immer“ (Sollte 4):** Etappe abgelegt oben „ABGELEGT“, Siegel „★ ABGELEGT“ (statt „FÜR IMMER“), Flug abgelegt „ALLE ETAPPEN ABGELEGT“ und „Alle n Etappen von … sind abgelegt.“, Reisepass „alle Etappen abgelegt“, Satz „Gold heißt: Alle Etappen sind abgelegt.“ Die Vorgabe des Gestalters (`inhalte/pruefung/kind/abgelegt/`) nennt noch „FÜR IMMER“ – **bitte dort nachziehen** oder anderen Wortlaut liefern.
- **0 Sterne bei Hilfe:** Wiederholung (Runde, Extra) und Mischkarte zeigen nur den Serverwert; bei `sterne: 0` (bzw. `wiederholung.sterne` 0) keine Sterne, der Zähler bleibt stehen (Test).
**Getestet:** lernen 159 von 159 (neu 2), Gesamtlauf sonst nur die bekannten Reise-Fehler.
## 2026-11-22 – bau-lehrer – FERTIG: WD-S 4

Auf „Nachtrag WD-S 4 – Rückläufer ChatGPT 921“, Teil „An bau-lehrer“ (ersetzt „FERTIG: WD-S 3 Test“). Nur Dateien, nichts eingespielt, kein DROP, kein DELETE.
**Reihenfolge beim Einspielen:** WD-S 2 → WD-S 3 → WD-4b → **WD-S 4** (`supabase/migrations/20261122_wd_s4_nacharbeit_921.sql`) → FP-S.

1. **Mischkarte beim Einlösen geprüft:** `misch_gueltig` verlangt zusätzlich, dass seit der Ausgabe keine *andere* Aufgabe derselben Etappe beantwortet wurde; der zweite Anlauf derselben Mischkarte bleibt gültig. Sonst `misch.gueltig: false`, keine Wiederholung (Umbau an genau einer Stelle; `misch_gueltig` lokal byte-gleich zu live geprüft).
2. **Mit Hilfe 0 Sterne:** fällige Wiederholung mit Tipp/2. Versuch → `karte_wdh_ereignis` markiert den Versuch, `sterne_aus_versuch` bucht keine Übungssterne; gültige Mischkarte mit Tipp/2. Versuch → `sterne_aus_versuch` bucht nichts. Ungültige Mischkarte = normales Üben (wie bisher). Antwort und Konto lesen beide `schule.sterne`.
3. **Runden-Abschluss unter Sperre:** `wdh_runde_pruefen` sperrt die Runden-Zeile vor dem Zählen.
4. **Staffel unter Sperre:** `wdh_staffel_strecken` und `wdh_staffel_zurueck` sperren die Karten in fester Reihenfolge (`for update`) und prüfen/schreiben darunter.
5. **Tests:** `wd_s3_rauchtest.sql` – Nachtrag „stabil machen“ enthalten; Teil 7 bricht ab, wenn die WD-4b-Funktionen fehlen (statt zu überspringen); neuer Teil 8: A ausgeben → B derselben Etappe beantworten → A einlösen = `gueltig false`, keine Wiederholung; Wiederholung mit Tipp und Mischkarte im 2. Versuch: Sternsumme unverändert, keine Übungs-/Wiederholungs-Gründe; 1 bzw. 0 freie Aufgabe; Lerntage mit Pausen (Sperre über 4 Kalendertage = 3 Lerntage). `wdh_aufgabe_da` ist jetzt ein deterministisches EXISTS. `wd_s3_gleichzeitig.sh`: zusätzlich zwei Sitzungen an den zwei letzten Pflicht-Etappen der Runde (Zustand danach per SELECT); Exit 1 bei jedem „FEHLER“.
6. **Rechte:** alle `schule.*`-Helfer aus WD-S 2/3/4 ohne Rechte für public, anon, authenticated.

**Lokal ausgeführt** (Postgres 16, berührte Live-Funktionen byte-gleich): alle fünf Migrationen in der Reihenfolge oben je zweimal, `wd_s_rauchtest`, `wd_s3_rauchtest` (Teile 1–8) und `fp_s_rauchtest` grün; `wd_s3_gleichzeitig.sh` Exit 0. **Gegenprobe ohne WD-S 4:** Teil 8 bricht ab, und der Gleichzeitig-Test meldet „FEHLER B: Runde nicht fertig (offen: 0)“ mit Exit 1 – genau der Fehler aus ChatGPT 921, mit WD-S 4 behoben.

**FP-S nach WD-S 4 geprüft:** passt – die Stelle in `sterne_aus_versuch`, die FP-S ersetzt, bleibt unberührt, und `uebung_pruefen_wd` ändert WD-S 4 nicht. Geändert nur der Kopf von `20261122_fp_s_faire_punkte.sql` (Reihenfolge; 5 Sterne mit Hilfe nur beim normalen Üben). Vorher/Nachher-Zahlen der Nachbuchung: Eintrag „FERTIG: FP-S“ unten (unverändert).

## 2026-11-22 – bau-lehrer – FERTIG: FP-S

Bau-Auftrag FP, Teil FP-S. Nur Dateien, nichts eingespielt, Nachbuchung nicht ausgeführt (nur lesend nachgerechnet). Kein DROP einer Tabelle/Spalte, kein DELETE.

**Dateien:** `supabase/migrations/20261122_fp_s_faire_punkte.sql` (nach WD-S 2 und WD-S 3, eine Transaktion), `supabase/tests/fp_s_rauchtest.sql`.

**Was gebaut ist**
- Regel 1: `sterne_aus_versuch` bucht 10 (`sterne_uebung_richtig`) nur bei richtig im ersten Versuch ohne Tipp, sonst 5 (`sterne_uebung_mit_hilfe`). Je Aufgabe weiter eine Buchung – die erste richtige Antwort entscheidet (wer zuerst mit Tipp löst, bekommt für diese Aufgabe später keine 10 mehr; Annahme, bitte bestätigen). Gilt auch für Mischkarten, die als Übung gebucht werden; Wiederholungen bleiben wie in WD; Knobeln unverändert.
- Regel 2/3: Bonus im Moment der Landung (Haken in `landung_speichern`, das nur bei einer echten Landung aus `karte_buchen` läuft): 80 / 40 / 10 nach `fehler_endgueltig` aus `landung_zaehlen` (dieselbe Zählung wie die Landungs-Art seit AB-S: nur Übung dieser Etappe, ohne Tests, Mischkarten, Wiederholungen; Tipp ist kein Fehler). Neuer Sterne-Grund `landung` (Prüfregel ersetzt, vorher gegen den WD-S-2-Stand geprüft), `bezug 'landung:<einheit>:<etappe>'` eindeutig → doppelter Aufruf und gleichzeitige Antworten: genau eine Buchung (die Landung selbst ist zusätzlich über die Zeilensperre in `karte_buchen` serialisiert). Gesetzte Etappen („Kann er“, `gesetzt_am`) bekommen keinen Bonus.
- Regel 4: `schule.landung_bonus_nachbuchen()` (auch je Kind: `(p_l)`) – liefert je Kind `etappen`, `sterne`; zweiter Lauf bucht nichts. Schreibt `schule.landung_nachbuchung` für den einmaligen Hinweis der App.
- Antworten: `schule_uebung_pruefen` liefert jetzt **immer `sterne`** (in diesem Aufruf tatsächlich gebucht: Übung + Wiederholung + Bonus + Ablegen) und bei der Landung **`landung {…, bonus, fehler, stufe: 'ohne'|'wenig'|'sonst'}`** (zur bisherigen Landungs-Einblendung dazu). `schule_konto` liefert **`regeln`** (alle Sterne-Regeln) und **`landung_nachbuchung {etappen, sterne, am}`** (null, solange nicht nachgebucht).

**Rauchtest** (lokal grün, Postgres 16 mit byte-gleichen Live-Funktionen inkl. `landung_speichern`/`landung_zaehlen`; zusammen mit WD-S- und WD-S-3-Test grün): 10/5/5/0, Bonus 80/40/10 (0/2/3 Fehler) über den echten Antwortweg, genau einmal, gesetzte Etappe ohne Bonus, Nachbuchung zweimal = einmal, Regeln, Lernstände/Stufen/Karten/Sterne der anderen Kinder unverändert. Der Test nimmt nur Etappen, die das Testkind nie beantwortet hat, und setzt die Karte selbst kurz vor die Landeschwelle – unabhängig von der Zusammensetzung echter Etappen.

**Nachbuchung – lesender Lauf auf der echten Datenbank (22.11., nur Nummern)**

| Kind | Sterne vorher | Etappen echt gelandet | ohne / 1–2 / mehr Fehler | Bonus | Sterne nachher | gesetzt (kein Bonus) |
|---|---|---|---|---|---|---|
| 1 | 2740 | 25 | 17 / 6 / 2 | +1620 | 4360 | 0 |
| 2 | 3970 | 28 | 27 / 1 / 0 | +2200 | 6170 | 36 |
| 3 (Testkind) | 120 | 6 | 5 / 1 / 0 | +440 | 560 | 0 |

Hinweise: Bei 16 bzw. 21 Etappen gibt es keine gespeicherte Landung (vor AB-S gelandet) – dort zählt die Nachbuchung die Fehler aus den Versuchen bis zur Landung neu. Die Nachbuchung erhöht den Kontostand um rund 55–60 % – vor dem Ausführen bitte mit Sebastian abstimmen (Belohnungen/Einlösungen hängen an Sternen).

## 2026-11-22 – bau-lehrer – FERTIG: WD-S 3 Test

Auf „Nachtrag WD-S 3 – Rauchtest stabil machen“. Nur `supabase/tests/wd_s3_rauchtest.sql` geändert, keine Migration.
- Vor Schritt 1 werden alle übrigen Übungsaufgaben beider Test-Etappen (alles außer Auswahl Stufe 2–3) als **gestern** beantwortet markiert (Testsitzung, also ohne Buchung; Lerntag gestern wird angelegt) – damit innerhalb der Sperre, aber nicht „heute“ (sonst wäre die Mischkarte in Schritt 3 zu Recht gesperrt).
- Lokal nachgestellt: Etappe mit zusätzlichen Aufgaben anderer Art → alter Test bricht wie im Probelauf in Schritt 2 ab („nicht die am längsten zurückliegende“), neuer Test läuft ganz durch.

## 2026-11-22 – FERTIG: 0.86.2 – Fehler Mischkarten (App-Teil) und ChatGPT 919 (Cache v158)

Auf `lernen-app` f278a3c. Nur App (`lernen.js`, `style.css`), Version in sechs Dateien, Tests. Nichts in der Datenbank, kein Merge nach `main`.

**Fehler Mischkarten (22.11.), Teil bau-motivation**
- **(a) Eine gezeigte Mischkarte ist für die ganze Sitzung des Flugs verbraucht** (`ctx.mischGezeigt`), nicht mehr je Etappe neu. Verbraucht ist sie, sobald sie gezeigt wurde, auch unbeantwortet. Ist die Liste leer, holt die App sie **einmal** je Sitzung im Hintergrund neu (`schule_einheit_lesen`, nur `mischkarten` werden übernommen); schon gezeigte bleiben verbraucht, sonst geht es ohne Mischkarte weiter. Neue Sitzung (Flug neu geöffnet) = neue Liste vom Server – die Frische über Sitzungen hinweg regelt WD-S 3.
- **(b) Sterne nur aus der Antwort des Servers:** `sterne` (tatsächlich gebucht), sonst `wiederholung.sterne`. Eine Mischkarte ohne beides zeigt keine Sterne. **Einschränkung:** Bei einer normalen Bordkarte und einem Server ohne `sterne` (heute live: `sterne` nur bei Knobel-Bordkarten) bleibt die bisherige Anzeige „+10 beim ersten Richtig“, sonst stünden bei jeder Landung 0 Sterne. **Bitte an bau-lehrer (WD-S 3):** `sterne` in **jeder** Antwort von `schule_uebung_pruefen` mitschicken (auch 0) – dann rechnet die App nirgends mehr selbst. Im Check-in: `wiederholung.sterne`, sonst `sterne`.
- **(c) `misch.gueltig === false`:** kein „Das war …“, kein „↻ Zählt als Wiederholung“, Sterne nur laut Server.

**ChatGPT 919, Teil bau-motivation**
- `wiederholung.bestanden === false` bei richtiger Antwort (mit Tipp oder im zweiten Versuch): „Richtig – morgen noch einmal ohne Hilfe.“ – bei der Mischkarte unter „✓ An Bord“, im Check-in statt „Richtig!“; Koffer hellgelb ohne Stern (neuer Zustand), keine Sterne, kein Fehlerton.
- Nach dem Ablegen nicht mehr „kommt nicht mehr wieder“: Ticket „5-mal wiederholt, über 30 Lerntage. Raus aus der regelmäßigen Wiederholung – nur noch bei Bedarf zum Auffrischen.“; Kindertext „… ist sie abgelegt: Sie ist raus aus der regelmäßigen Wiederholung und kommt nur noch, wenn sie aufgefrischt werden muss“; Info-Seite „Sie fällt aus der regelmäßigen Wiederholung und wird nur noch bei Bedarf aufgefrischt“. Die Gestalter-Wörter „FÜR IMMER GELERNT“/Siegel „FÜR IMMER“ und „sitzen für immer“ (Flug abgelegt) habe ich gelassen – bitte prüfen, ob sie zum neuen Satz passen.

**Getestet:** lernen 157 von 157. Neu: „drei Etappen nacheinander – keine Mischkarte doppelt; leere Liste einmal neu vom Server, danach ohne Mischkarte“ (schlägt mit 0.86.1 fehl, mit 0.86.2 grün); „Sterne nur vom Server; gueltig false; bestanden false“; „Check-in – richtig mit Hilfe“. Angepasst: WD-3 zeigt jetzt +5 (nur `wiederholung.sterne`) statt 10 + 5. Gesamtlauf sonst nur die bekannten Reise-Fehler.
**Nicht geprüft:** echter Server (WD-S 3 noch nicht da), echte Geräte.

## 2026-11-22 – bau-lehrer – FERTIG: WD-S 3

Auf AUFTRAEGE.md „Fehler Mischkarten (22.11.)“, Nachtrag „WD-S 3 – frische Aufgaben“ und „ChatGPT 919“, Teil bau-lehrer. Nur Dateien, nichts in der echten Datenbank ausgeführt (nur lesende Abfragen), kein App-Code. `sterne_wdh_richtig` bleibt 10.

**Dateien**
- `supabase/migrations/20261122_wd_s3_frische_aufgaben.sql` – neu, nach WD-S 2 einspielen (eine Transaktion).
- `supabase/migrations/20261122_wd_4b_stau_strecken.sql` – überarbeitet (nicht eingespielt): jetzt als Funktionen `schule.wdh_staffel_strecken` / `schule.wdh_staffel_zurueck`, nach WD-S 3 einspielen.
- `supabase/tests/wd_s3_rauchtest.sql` (neu, 7 Teile), `supabase/tests/wd_s3_gleichzeitig.sh` (neu, zwei gleichzeitige Transaktionen – **nur Wegwerf-Datenbank**, schreibt Daten), `supabase/tests/wd_s3_lesend.sql` (neu, nur lesend). `wd_s_rauchtest.sql` Teil 10 nimmt jetzt eine heute noch nicht beantwortete Etappe (sonst sperrt die neue Regel die Mischkarte zu Recht).

**(1) Frische Aufgaben** – eine Auswahl für Wiederholung und Mischkarte (`schule.wdh_aufgabe_waehlen`): nie aus den letzten 3 Lerntagen (heute + 2 vorige **Lerntage**, Reisetage zählen nicht; jede Rolle inkl. Test und Knobeln; Regel `wdh_sperre_lerntage`), zuerst nie beantwortete (darunter zufällig), sonst die am längsten zurückliegende, sonst heute keine (Wiederholung bleibt fällig, in der Runde = bearbeitet). Stufe 3–4: beliebig, bevorzugt die am längsten zurückliegende – „noch nie“ zählt dabei als am längsten zurück; damit fallen beide Regeln in eine Reihenfolge zusammen (Annahme, bitte bestätigen). Mischkarten: nie aus einer Etappe, in der das Kind heute schon geantwortet hat; offene Ausgabe verfällt sofort bei anderer Antwort (Trigger) und beim nächsten Ausgeben, wenn schon beantwortet oder Etappe heute dran. Mischkarte ohne gültige Ausgabe: `misch {gueltig: false, sterne}`, keine Buchung als Wiederholung (Takt bleibt), als normales Üben wie bisher; gültig: `misch.gueltig: true` + `misch.sterne`. `sterne` = in diesem Aufruf tatsächlich gebucht.
**(2) Nur selbst** (Regel `wdh_nur_selbst` = true): Fortschritt, Wiederholungs-Sterne, Ablegen nur richtig im ersten Versuch ohne Tipp – Runde, freiwillig, Mischkarte. Mit Tipp/zweitem Versuch: `wiederholung {bestanden: false, mit_hilfe: true, naechste_in: 1}`, kein Fehler, am nächsten Lerntag wieder. Dafür zählt eine Mischkarte mit Tipp jetzt als Antwort (richtig + 1, kein Beleg) – sonst bliebe sie in der Runde offen.
**(3) WD-4b:** Etappen einer offenen Tagesrunde ausgenommen (zählen auf den heutigen Platz); von WD-4 schon belegte Folgetage zählen mit; Rückweg nur ohne Zwischenübung (sonst Ablehnung, nichts geändert); kein zweiter Lauf.
**(4) Sollte:** Misch-Fehler für die Reihenfolge erst nach endgültiger Wertung; zwei gleichzeitige Transaktionen über die Antwort-Funktion (lokal: Gerät A „bestanden, Stufe 2“, Gerät B wartet auf die Sperre und bekommt „keine Wiederholung“; genau ein Fortschritt, einmal Sterne); Lerntage statt Kalendertage (Test 1: Sperre ab 18.11. bei heute 22.11. = 3 Lerntage über 4 Kalendertage).

**(5) Lesend, Stand 22.11. (echte Datenbank):** gelandete Etappen mit < 3 frischen Aufgaben (Stufe 2–3): **Kind 1: Einheit 39 „ordnen“ und „zahlengerade“ (0 von 18 frisch); Kind 2: Einheit 5 „waage“ (0 von 18)**. Nach WD-S 3 bekommen diese Etappen die am längsten zurückliegende Aufgabe (nie aus den letzten 3 Lerntagen) – Nachliefern empfohlen. Nach dem Einspielen: `select * from schule.etappen_wenig_frisch();`.
**Gegenprüfung `flug_erstabschluss`:** 5 Einträge, alle stimmig (Sitzung passt, Flug heute fertig, höchstens eine Sitzung mit flug_geschafft).

**Lokal ausgeführt** (Postgres 16, Live-Funktionen byte-gleich inkl. `misch_gueltig`; `uebung_pruefen_intern` als Platzhalter mit echter Auswahl-Wertung, Hilfe/Anlauf/Mischkarte wie live): alle drei Migrationen je zweimal, `wd_s_rauchtest` grün, `wd_s3_rauchtest` grün, Gleichzeitig-Skript grün. Dabei gefunden und behoben: zufällige Aufgabenwahl muss `volatile` sein (sonst wertet Postgres sie doppelt aus).
**Für bau-motivation (0.86.2):** `misch.gueltig`, `misch.sterne`, `wiederholung.mit_hilfe` sind die neuen Felder.

## 2026-11-22 – FERTIG: 0.86.1 – Rückläufer 22.11. abends, Teil C (Cache v157)

Auf `lernen-app` 6ec1c3e. Nur App (`lernen.js`, `style.css`), Version in sechs Dateien, Tests. Nichts in der Datenbank, kein Merge nach `main`.
Bilder: `docs/previews/la/wd-etappe-abgelegt-400.png`, `-1280.png`, `wd-flug-abgelegt-360.png` (360 × 640), `-1280.png`, `wd-reisepass-400.png`.

**1 Test „LM-S 2: Raster … Detail …“ – Ursache: Testdaten, nicht die App.** Der Test nimmt die Verbindungen aus der Vorlage `entwurf/lehrplan-matrix.html`; der Gestalter hat sie am 22.11. neu erzeugt (128 statt 70). Seitdem braucht Thema 22 eine Voraussetzung – und „Eigenständig: braucht keine Voraussetzung …“ steht (richtig) nur bei Themen ohne Voraussetzung; sonst zeigt das Detail die Liste „Braucht vorher“. Behoben: Der Test wählt das eigenständige Thema jetzt aus den Daten (bevorzugt 42, sonst das erste ohne Voraussetzung). Die live laufende Lehrer-Matrix ist davon nicht betroffen. Hinweis zu den Daten (wie N3): Ein Thema mit `eigenstaendig` **und** Voraussetzungen zeigt die Voraussetzungen, die Begründung nicht.

**2 Angleichung an die Vorgabe „abgelegt“** (`inhalte/pruefung/kind/abgelegt/umsetzung.md`, `entwurf/abgelegt.html`)
- **Ansage (1):** im Kasten über dem Startknopf „Vorher kurz einchecken“ · „{n} Bordkarten von früher · etwa {min} Minuten“ (n × 0,5, unter 2 „ganz kurz“) · Koffer-Leiste in Päckchen (bis 6 eins; 7–9 zu 3; 10–12 zu 4). Startknopf „Weiter geht’s ›“. Unterbrochen: „Check-in fortsetzen · Noch 2 von 3 Bordkarten …“, erledigte Koffer grau. „je richtig ★ n“ nur, wenn der Server `sterne_je_richtig` liefert (**Vorschlag an bau-lehrer**: die Zahl aus `sterne_wdh_richtig` mitschicken – ohne Feld lässt die App den Teil weg, weil 5 oder 10 noch offen ist).
- **Check-in (2):** „CHECK-IN · i VON n“, Koffer-Leiste, Sterne-Zähler rechts, „+n“ fliegt (abschaltbar), unter der Bordkarte „{Etappe} · aus {Stadt}“; richtig „Richtig!“ mit „+n ★“ (nur mit `wiederholung.sterne`), Koffer gold mit Stern; falsch „Noch nicht. Richtig ist …“ + „Kein Problem – diese Bordkarte kommt beim nächsten Mal wieder.“, Koffer rötlich, „Zur Etappe“ klein; volles Päckchen hellgelb; „Nächste Bordkarte ›“/„Fertig ›“; dazu „Pause – später weiter einchecken“.
- **Fertig (3):** „Eingecheckt!“, Koffer, „{r} von {n} richtig · +{sterne} ★“ (inkl. 30/100), Fehlersatz bzw. „Alles richtig – super eingecheckt!“, „Weiter nach {Stadt} ›“ ins Thema, „Noch 3 Extra-Bordkarten?“ nur wenn mehr fällig als die Runde (`#/wiederholen/<kind>-extra`, höchstens 3, Kopf „EXTRA · i VON 3“).
- **Etappe abgelegt (4):** Handy Blatt von unten (≤ 72 % Höhe), ab 760 px Karte in der Mitte (≤ 520 px), Bordkarte bleibt abgedunkelt sichtbar; „FÜR IMMER GELERNT“, „Etappe abgelegt!“, Ticket gestrichelt mit Titel und „5-mal wiederholt, über 30 Lerntage. Kommt nicht mehr zum Wiederholen.“, Siegel „FÜR IMMER“ (fällt gedreht), „+30 ★ Sonder-Sterne fürs Ablegen“, Funken; Knopf „Weiter einchecken ›“ im Check-in, sonst „Weiter ›“. Fortschritt des Flugs mit Gold-Leiste **nur, wenn der Server ihn mitschickt** – **Vorschlag an bau-lehrer:** in `abgelegt.etappe` zusätzlich `flug` (Titel), `etappen_abgelegt`, `etappen`. Wird mit derselben Antwort der Flug abgelegt, entfällt das Blatt.
- **Flug abgelegt (5):** ganzer Bildschirm Gold auf Dunkel, Strahlen, „ALLE ETAPPEN FÜR IMMER GELERNT“, „FLUG ABGELEGT!“ in Gold-Schrift, „Alle {n} Etappen von {Flug} sitzen für immer. Im Reisepass ist der Flug jetzt golden.“ (`flug.etappen`, sonst ohne Zahl), aufgeschlagener Pass mit drei Flug-Zeilen (Nachbarn aus den Flügen des Kindes), die Zeile wird golden; Blatt „+100 ★ für den ganzen Flug / +30 ★ für die letzte Etappe“, bei `ort_gold` kleiner Gold-Stempel „Und: Alle Flüge in {Ort} sind abgelegt …“ (`abgelegt.ort` – **bitte mitschicken**, sonst „an diesem Ort“). 360 × 640 ohne Scrollen (Test).
- **Reisepass (6):** Abschnitt „Flüge“ aus `konto.fluege[]` (Ort über `einheit_id`): ganz abgelegt Gold-Verlauf, „★ ABGELEGT“, „{Ort} · alle Etappen für immer gelernt“; teilweise „{a} von {n} abgelegt“ mit Kästchen-Leiste; 0 „noch nichts abgelegt“. Stempel golden „★ GOLD ★“. Satz „Gold heißt: Das sitzt für immer.“ Ohne die Felder bleibt der Reisepass wie bisher.
- Kindertext „Was kommt wann wieder?“ ohne „fällig“, „endgültig“, „Stufe“, „Takt“ und ohne feste Sternzahl (Test). Wartende gesetzte Etappen sieht das Kind nicht mehr (7); im Plan der Eltern bleibt der Zusatz aus 0.85.0 (`wartet`/`kommt_ab_in`, wenn geliefert).

**3 WD-S 2**
- `schule_wiederholung` **ohne `anzahl`**. Pflicht-Bordkarten = `aufgaben[]` mit `pflicht: true` (ohne Feld: die ersten `runde`). Stand „3 von 9“ = `runde` − offene Pflicht-Bordkarten (oder `runde_erledigt`, falls geliefert) – so geht es nach einer Pause und auf einem anderen Gerät an der richtigen Stelle weiter.
- „Runde gemacht“ setzt der Server; die App setzt nichts mehr und schreibt kein `localStorage`. `schule_wiederholung_runde_fertig` ruft sie am Ende nur zum Bestätigen (Fehler werden still ignoriert).
- Keine Rückstandszahl: `faellig` steht nirgends auf der Kinderseite; „Noch k Wiederholungen offen“ ist ersetzt durch „Noch 3 Extra-Bordkarten?“.
- Alter Server (ohne `runde`): liefert ohne `anzahl` nur 3 – die App fragt dann einmal mit `anzahl: 6` nach; sonst alles wie 0.84.0 (Test).

**4 Matrix N1:** Am Rechner (≥ 1100 px) gibt es die Detail-Spalte erst beim Antippen; ohne gewähltes Thema hat die Matrix die volle Breite (Spalten bei 1280 ≈ 130 statt 95 px, Test ≥ 125). Mit geöffnetem Detail bleibt es eng – falls das stört, zusätzlich die Kennzeichen bei gewähltem Kind ausblenden (zweiter Vorschlag der Nachprüfung, nicht gebaut).

**Getestet:** lernen 154 von 154 (neu/ersetzt: Ansage mit Päckchen 6/9/12; Check-in mit Unterbrechen/Fortsetzen, Koffer, Sternen, Extra, 400/820/1280; alter Server; Etappe/Flug abgelegt bei 360×640, 400, 820, 1280; Reisepass; Info und Kindertext; N1; weniger Bewegung). Gesamtlauf: nur die bekannten Reise-Fehler (dazu das datumsabhängige „W80: Jede neue Suche“).
**Nicht geprüft:** echter Server (WD-S 2 noch nicht gebaut), echte Geräte, Safari.

## 2026-11-22 – bau-lehrer – FERTIG: WD-S 2

Auf AUFTRAEGE.md „Rückläufer 22.11. abends“, Teil A (acht Punkte). Nur Dateien, nichts ausgeführt, kein App-Code. Da WD-S nicht eingespielt ist, sind `20261122_wd_s_wiederholungen.sql` und `wd_s_rauchtest.sql` überarbeitet (keine Zusatzdatei). Nacharbeit 907 und `wd_4b_stau_strecken.sql` bleiben unverändert. `sterne_wdh_richtig` bleibt 10.

1. **Prüfregel Sterne:** `sterne_grund_check` wird ersetzt (alle 7 bisherigen Gründe + `wdh`, `etappe_abgelegt`, `flug_abgelegt`). Die Migration vergleicht vorher den Live-Text der Regel (gelesen) und bricht ab, wenn er abweicht. Lokal mit derselben Regel geprüft (vorher: Abbruch wie im Probelauf nachstellbar, nachher grün).
2. **Runde serverseitig:** `schule.wdh_runde` (Tagesziel, fällige beim Festhalten, `fertig_am`) + `schule.wdh_runde_etappe` (zugeordnete Etappen, `bearbeitet_am`). Festgehalten beim ersten Abruf des Lerntags (`schule_wiederholung`); jede Antwort auf eine Etappe der Runde (richtig oder falsch) hakt ab; sind alle abgehakt, setzt der Server `fertig_am` selbst. Etappe ohne verfügbare Aufgabe = bearbeitet; 0 fällige = sofort gemacht. Zweites Gerät bekommt dieselbe Runde; neue Fälligkeiten am selben Tag nur freiwillig. `schule_wiederholung_runde_fertig` bestätigt nur – fehlen Aufgaben: Fehler „Die Wiederholungs-Runde ist noch nicht fertig: x von y bearbeitet“.
   **Antwort `schule_wiederholung` neu:** `runde` (Ziel), `runde_bearbeitet`, `runde_offen`, `runde_gemacht`; `aufgaben[]` = zuerst die noch offenen Etappen der Runde (`pflicht: true`), dann weitere fällige freiwillig. Für die App: „3 von 9“ = `runde_bearbeitet` von `runde`.
3. **Genau ein Fortschritt je Fälligkeit:** nach dem ersten Bestehen ist die Etappe nicht mehr fällig (Zeile gesperrt), der Sterne-Schlüssel je Fälligkeit verhindert eine zweite Buchung; doppelt gesendete Antwort (gleiche `client_id`) wird von der Tabelle abgewiesen. Nicht fällige Mischkarte: nur `misch_ok_am`, kein Fortschritt. Falsche Mischkarte seit Beginn der Fälligkeit zählt in der Reihenfolge als Wiederholungs-Fehler (`schule.wdh_fehler`, ohne den Karten-Stand zu ändern – so öffnet sie weiterhin nie).
4. **Reihenfolge:** mindestens ⌈Runde/3⌉ Pflicht-Plätze für die am längsten fälligen, die übrigen nach Fehler → am längsten fällig → Stufe.
5. **Rückfall nach dem Ablegen:** falsch beim Üben, falsche Mischkarte oder „fehler“ im Nachtest/Test (Trigger auf `lernziel_stand`) → am nächsten Lerntag zurück in den Takt mit Stufe 2; Gold, Sterne, Einblendung bleiben; zweites Ablegen gibt nichts. Kopf: Ablegen an der bestandenen fünften Wiederholung, frühestens 55 Lerntage nach der Landung, nicht an „sicher“ gebunden; `abgelegt` ist ein eigenes Ereignis, nie aus `wdh_stufe` abgeleitet.
6. **Sterne:** letzte Wiederholung = Wiederholungs-Sterne + 30 (+ 100 beim letzten Flug-Teil), je einmal – im Test summiert.
7. **Kopf:** Ziel „Stau schrittweise abbauen, etwa fünf Lerntage bei ausreichender Kapazität – keine Garantie“; Grenze „ohne Bündeln trägt die Kapazität dauerhaft etwa 3 Landungen je Lerntag“.
8. **Tests (`wd_s_rauchtest.sql`, 15 Prüfungen):** Rundengröße; 20/41/60/100 fällige (je eigener Tag: Größe, Pflicht zuerst, ältestes Drittel enthalten, auch mit 50 % Fehlern); Runde ohne Mischkarten, zwei Geräte, Abbruch mitten in der Runde → fortsetzen, Ablehnung vor dem Ende, neue Fälligkeit freiwillig, Server setzt „gemacht“; Tageswechsel, Etappe ohne Aufgabe, 0 fällige; ein Fortschritt/eine Vergütung bei doppelter Antwort und zweitem Gerät; Mischkarten (nicht fällig / falsch / richtig); letzte Stufe mit Sternensumme; Rückfall (Üben, Nachtest), Gold bleibt, zweites Ablegen leer; Konto; Staffelung; Mischkarten-Auswahl; andere Kinder unverändert. `wiederholung_intern`/`wdh_runde_fertig` haben dafür einen Tag-Parameter, den nur der Test nutzt (die api-Funktionen nehmen immer heute_tag).

**Lokal ausgeführt** (Postgres 16, die 20 berührten Live-Funktionen byte-gleich, `sterne_grund_check` und Eindeutigkeit `versuch (lernender_id, client_id)` wie live; Platzhalter u. a. für `uebung_pruefen_intern`, `thema_stufe`, `reiseoptionen`): Migration zweimal, Rauchtest vollständig grün, dazu die api-Kette (Wiederholung → Antwort → Bestätigen).
**Nicht geprüft:** echt gleichzeitige Antworten zweier Geräte (im Test nacheinander; gleichzeitig entscheidet die Zeilensperre in `karte_buchen`/`misch_buchen`).
**Für bau-motivation:** Runde nicht mehr selbst als gemacht setzen; `schule_wiederholung_runde_fertig` nur zum Bestätigen (kann ablehnen); `anzahl` weglassen; `runde_bearbeitet`/`runde` für „x von y“.

## 2026-11-22 – FERTIG: 0.86.0 – LM-6 Kinderseite „Meine Route 5–10“, Cache v156

Auf 0.85.0 (gleicher Zweig). Nur App, Version in sechs Dateien, Tests. Nichts in der Datenbank, kein Merge nach `main`.
Bilder: `docs/previews/la/lm6-route-nacht-400.png`, `lm6-route-tag-400.png`, `lm6-route-nacht-820.png`, `lm6-route-nacht-1280.png` (jeweils mit geöffnetem ▶-Flug).

**Gebaut** (Vorgabe `inhalte/pruefung/lehrer/matrix/umsetzung.md`, LM-6)
- **Zugang:** Textlink „Meine Route 5–10 ›“ auf der Abflugtafel (unter „Erst die Erklärungen ansehen“) und im bisherigen Design unter „Reisepass und Belohnungen ansehen“; neue Seite `#/route/<kind>` (in App und Lern-Seite angemeldet). Der große Knopf bleibt.
- **Nur das eigene Kind:** Lernstand immer an, Schulart fest, keine Leiste, kein Vergleich, keine Kennzeichen „Gym 8 · RS 7“, keine Pflicht-Zählung, kein Lehrplan-Wortlaut, keine Lernbereiche, nichts zum Ändern.
- **Reisewörter:** Überschrift „Deine Route durch die Mathe-Welt“, Spalten = Kontinente (Titel aus `gebiete[]`), Zeilen = Klasse 5–10, je Flug die Stadt klein darunter. Stufen: „◉ kannst du“, „↻ kommt zur Wiederholung“, „▶ hier bist du – Etappe x von y“, „○ kommt noch“; nicht im Plan blass, ohne Text. Beim Öffnen zum ▶-Flug gescrollt. Kopf je Klasse: Balken (◉ ↻ ▶) und „Du kannst schon n von m Flügen“ (m = Flüge der Klasse mit Inhalt, ohne eingeordnete).
- **Detail** (beim Antippen `schule_lehrplan_thema {thema_id, lernender_id}`): „Was du hier lernst“, „Das muss sitzen“, „Das brauchst du vorher“ und „Danach geht’s weiter mit“ – je mit eigener Stufe (Zeichen + Wort), antippbar; „Die Etappen (n)“ mit ✓ für gelandete Etappen (aus dem Merkheft). Beim ▶-Flug großer Knopf „Weiter lernen ›“ (`#/lerneinheit/<kind>-<einheit>-ueben`), sonst kein Lern-Knopf.
- **Verbindungen** wie LM-3 (gelb vorher, blau danach, „→ n“), Linien hinter den Karten.
- **Handy und Tablet zuerst:** unter 1000 px Liste je Klasse nach Kontinent, Detail direkt unter dem Flug, keine Linien (die Kinderseiten sind höchstens 640–760 px breit – acht Spalten passten dort nicht); ab 1000 px Matrix mit Linien, die Seite dafür bis 1240 px breit. Farben der Kinderseiten (Ozean, Nacht, Dschungel, Wüste) über die `--lr-`-Variablen.
- **Daten:** Mit Lern-Zugang liefert LM-S die Kindsicht (`zeile`, `reihenfolge_kind`). Öffnen Eltern die Seite des Kindes, liefert der Server die Lehrer-Sicht – dann rechnet die App die Zeile aus `jahrgang` und der Schulart des Kindes (wie `schule.thema_klasse_fuer`) und zeigt nur dieses Kind. Aufruf mit `mit_testkind: true`, damit auch das Testkind seine Route sieht. Ohne LM-S (alter Server): „Die Route ist bald da.“
- **Info-Seite:** nicht geändert (die Kinderseite erklärt sich mit Einleitung und Legende). Wenn gewünscht, Satz für die Eltern liefern.

**Getestet** (lernen 151, neu 4): Link auf der Abflugtafel, alle Flüge, keine Kennzeichen/Leiste/Knöpfe, Stufen-Texte, Scrollen zum ▶, Kopf je Klasse, Kontinente als Spalten, Reisewörter (keine „Thema/Lehrplan/Gymnasium/Pflicht/Aufgabe“); Detail mit Voraussetzungen (eigene Stufe), Nachfolgern, Linien, Etappen-✓, „Weiter lernen ›“ nur beim ▶-Flug, kein Wortlaut, keine Begründung; Abnahme 400/820/1280 in Nacht und Tag (nichts läuft über, kein Wort ohne Trennstrich gebrochen, kein Querrollen, Liste mit Detail unter dem Flug bzw. Matrix mit Linien); Lehrer-Sicht (Zeile aus jahrgang, kein Geschwister) und alter Server. Suche: nur die bekannten Reise-Fehler.

**Nicht geprüft:** gegen den echten LM-S-Server (Kindsicht über den Lern-Zugang), echte Geräte.

## 2026-11-22 – FERTIG: 0.85.0 – Wiederholungen dynamisch (WD, App-Teil), Cache v155

Auf `lernen-app` 986d43e. Gebaut gegen die Schnittstelle im „Nachtrag zum Bau-Auftrag WD“. Nur App (`lernen.js`, `style.css`), Version in sechs Dateien, Tests. Nichts in der Datenbank, keine Kinderdaten, kein Merge nach `main`. Den Server habe ich nicht gesehen (`bau-lehrer` hat noch keinen WD-Stand) – getestet gegen nachgebildete Antworten.
Bilder: `docs/previews/la/wd-etappe-abgelegt-400.png`, `wd-flug-abgelegt-400.png`, `wd-flug-abgelegt-1280.png`, `wd-reisepass-400.png`.

**Gebaut**
- **WD-1 Runde:** `schule_wiederholung` wird mit `anzahl: 12` aufgerufen (der alte Server begrenzt selbst auf 6 – `least(anzahl, 6)` –, also kein Unterschied). Liefert der Server `runde`, sind die ersten `runde` Bordkarten aus `aufgaben[]` die Pflicht-Runde (Reihenfolge vom Server): Startknopf „Erst n Wiederholungen ›“, Kopf „WIEDERHOLEN i VON n“. Danach „Noch k Wiederholungen offen – wenn du magst“ (k = `faellig` − Runde); freiwillige heißen „FREIWILLIG WIEDERHOLEN“.
- **WD-2 Merker:** Mit `runde` gilt nur noch `runde_gemacht` vom Server, `localStorage` wird dann weder gelesen noch geschrieben. Am Ende der Pflicht-Runde ruft die App `schule_wiederholung_runde_fertig {lernender_id}` (scheitert der Aufruf, merkt sich das Gerät die Runde wie bisher).
- **WD-4 Staffelung:** `gestaffelt` > 0 → auf der Abflugtafel (beide Designs) und am Ende der Runde: „n Etappen warten noch auf die erste Wiederholung – sie kommen ab dem nächsten Lerntag nach und nach dazu.“ Ein Datum „kommt ab …“ je Etappe liefert die Schnittstelle nicht – **Vorschlag (optional, nicht verbindlich):** im Plan je Flug in `thema_stufe` `wartet` (Zahl) und `kommt_ab_in` (Lerntage); die App zeigt dann im Plan „3 Etappen warten · kommt ab in 2 Lerntagen“ (ist schon eingebaut, ohne die Felder unsichtbar). Ebenso `etappen_abgelegt` → „2 von 7 abgelegt“.
- **WD-5 Sterne:** `wiederholung.sterne` erscheint als „Richtig! · +5 Sterne“, darunter „Nächste Wiederholung in n Lerntagen“ (`naechste_in`), am Ende „★ +n Sterne“. Die App rechnet nichts selbst – sie zeigt, was der Server meldet.
- **WD-3 Mischkarte:** Bei `wiederholung.bestanden` steht unter „✓ An Bord“ „↻ Zählt als Wiederholung dieser Etappe“; die Sterne-Zeile zeigt 10 (Mischkarte, wie heute) **plus** `wiederholung.sterne`. Entscheidet Sebastian anders (nur 5 oder nur 10), bitte entsprechend buchen und `wiederholung.sterne` 0 bzw. die Differenz melden – die App zeigt genau das.
- **WD-6 Einblendungen** (aus `abgelegt` in `schule_uebung_pruefen`, nach einer Wiederholung oder Mischkarte): „Etappe abgelegt“ klein – goldene Karte über der Seite (★-Siegel, Titel der Etappe, Satz, „★ +30“, „Weiter“); danach, falls `flug`, „Flug abgelegt“ groß – Vollbild im Stil von „Flug geschafft“, in Gold (Konfetti, Zähler 100 ★, Siegel, „Im Reisepass: Dein Flug ist jetzt golden.“, bei `ort_gold` „Alle Flüge dieses Orts sind abgelegt – dein Stempel ist jetzt golden.“, „Weiter“, „Reisepass ansehen“). Gestalter-Vorgabe gab es noch nicht – bitte nachprüfen, ich gleiche an.
- **Gold im Reisepass:** `konto.orte[].gold` → Stempel golden mit „★ GOLD“. Flüge: neuer Abschnitt „Abgelegt“ (nur wenn etwas abgelegt ist) mit dem Eintrag je Flug, golden bei `abgelegt`, sonst „1 von 2 Etappen abgelegt“. Bisher gab es im Reisepass keinen Eintrag je Flug – das ist der „Eintrag des Flugs“. **Erwartetes Format:** `konto.fluege[] { block_id, titel, abgelegt, etappen_abgelegt, etappen }` oder dieselben Felder in `konto.orte[].fluege[]` (beides gelesen) – bitte so liefern oder melden.
- **Info-Seite:** Wiederholung (Rundengröße, ein Mal je Lerntag auch beim Gerätewechsel), neuer Eintrag „Endgültig abgelegt“, Mischkarten (zählen als Wiederholung), Belohnungen (5 / 30 / 100), Plan („Kann er – aber wiederholen“: höchstens 6 je Lerntag neu in den Takt). „Was kommt wann wieder?“ (Kind) mit Runde und Sternen nur, wenn der Server `runde` liefert. Die Info-Texte beschreiben WD – **erst mit dem Server live schalten.**
- **Alter Server:** ohne `runde` alles wie 0.84.0 (höchstens 6, Merker auf dem Gerät, kein `runde_fertig`, keine neuen Zeilen) – eigener Test.

**Getestet** (lernen 147, neu 6): Runde in Server-Größe und Server-Merker (Gerät sagt „gemacht“, Server nicht → Server gilt; umgekehrt auch), runde_fertig, freiwillig, wartende Etappen, 400/820/1280 ohne Querrollen; alter Server; 5 Sterne, „Etappe abgelegt“ (klein, 400/820/1280, keine gebrochenen Wörter) und „Flug abgelegt“ (Vollbild, Zähler 100, Stempel golden); Mischkarte als Wiederholung; Reisepass golden (400/820/1280) und ohne Felder unverändert; Info-Texte. Die bekannten Fehler der Reise-Tests unverändert.

**Nicht geprüft:** echter Server, echte Geräte; Animation nur in Chromium.

## 2026-11-22 – bau-lehrer – FERTIG: Nacharbeit 907

Auf AUFTRAEGE.md „Nacharbeit aus ChatGPTs Prüfergebnis 907“, Teil bau-lehrer. Neue Dateien; die eingespielten Migrationen bleiben unverändert. Nichts in der echten Datenbank ausgeführt.
- `supabase/migrations/20261122_nacharbeit_907.sql`:
  - **Kopf dokumentiert** den Altzustand „früher fertiger Flug (Sitzung NULL oder durch Lesen false) → neue Pflicht-Etappe → erst dann Nachtrag → Nachtragstest“: festgelegtes Ergebnis **flug_geschafft = true** (zweites „Flug geschafft“); beim Einspielen im Bestand ausgeschlossen (Haupt-Chat: 4 von 4 Flügen mit Test fertig, Pflichtlisten vollständig); neue Fälle entstehen nicht. Ebenso festgehalten: erneutes Lesen derselben erfolgreichen Sitzung zeigt wieder true (gewollt).
  - `schule.flug_erstabschluss_nachtragen`: `sitzung_id` und `am` aus **derselben, zeitlich ersten** Sitzung (`order by abgeschlossen_am, id`).
  - LM-S: `etappe_jetzt` = Nummer der ersten noch nicht gelandeten Etappe in Etappen-Reihenfolge (neue Funktion `schule.etappe_jetzt`); fehlt, wenn alle gelandet sind. Umbau von `schule.lehrplan_matrix` an genau einer Stelle (live genau einmal vorhanden, gelesen).
- `supabase/tests/ab_s_nacharbeit_907_rauchtest.sql`: der Altzustand in beiden Formen (NULL / vorher gelesen) → Nachtrag danach → Nachtragstest = true, erneutes Lesen wieder true; Nachtrag mit gegenläufigen ids/Zeiten → beide Werte aus der zeitlich ersten Sitzung.
- `supabase/tests/lm_s_nacharbeit_907_rauchtest.sql`: Lern-Zugang des Testkinds und ein Eltern-Zugang, beide im Test angelegt (Name „Rauchtest“, Zufalls-Hash, Rollback – kein echter Schlüssel): fremde `lernender_id`, `mit_testkind: true`, Detail als Kind, Eltern = Lehrer-Sicht, gesperrter Zugang und abgelaufene Sitzung abgewiesen („Nicht angemeldet“), Größe mit `octet_length` (Raster < 90 000 Bytes, Detail < 30 000), `etappe_jetzt` (2 / keine / 1) und im Raster stimmig.
- `supabase/tests/lm_s_lehrplan_matrix_rauchtest.sql` Prüfung 4 angepasst (etappe_jetzt nur bei „dran“, kann jetzt fehlen) – sonst würde der alte Test nach der Nacharbeit fälschlich abbrechen.
- **Lokal ausgeführt** (Postgres 16): `test_abschliessen_intern`, `lehrplan_matrix`, `flug_erstabschluss_nachtragen` byte-gleich zum Live-Stand (md5 gleich), Zugangsfunktionen (`lern_ich`, `ist_leiter`, `wer_tn`, `sieht`, `zugriff`) wie live; Migration zweimal, beide neuen Tests grün, alter LM-S-Test grün. Gegenprobe: mit dem alten Nachtrag schlägt Prüfung 2 fehl.

## 2026-11-22 – bau-lehrer – FERTIG: WD-S

Bau-Auftrag WD (Server) nach der Schnittstelle im Nachtrag. Nur Dateien, in der echten Datenbank nichts ausgeführt, kein App-Code, kein Merge nach main, keine Kinderdaten.

**Sterne heute (Live-Text gelesen 22.11.) – Meldung vor dem Bau:**
- Jede richtige Antwort außerhalb eines Tests – auch mit Tipp oder im 2. Anlauf, auch eine Wiederholung oder Mischkarte – gibt `sterne_uebung_richtig` = **10 Sterne**, aber **je Aufgabe nur einmal** (Schlüssel `uebung` + `aufgabe:<id>`). Die Wiederholungs-Runde wählt bevorzugt ungesehene Aufgaben → eine richtige Wiederholung gibt heute meist 10, sonst 0. Mischkarte genauso.
- Also: **Ja, eine richtige Wiederholung gibt heute schon 10.** Nicht gekürzt: `sterne_wdh_richtig` steht in der Migration auf **10** (Schnittstelle: 5). **Sebastian entscheidet 5 oder 10** – Umstellen ohne Bau: `update schule.regel set wert = '5' where schluessel = 'sterne_wdh_richtig'`.
- Neu gilt: je bestandener Wiederholung (Runde, freiwillig, Mischkarte nach WD-3) einmal je Etappe und Fälligkeit `sterne_wdh_richtig`; für denselben Versuch dann keine `uebung`-Sterne (nichts doppelt). Die `uebung`-Sterne dieser Aufgabe bleiben für später übrig.

**Dateien**
- `supabase/migrations/20261122_wd_s_wiederholungen.sql` – WD-1 bis WD-6 (Regeln, Tabellen `schule.wdh_runde`, `schule.abgelegt`, Trigger `karte_wdh_ereignis`, Umbauten an genau bezeichneten Stellen). Prüft am Ende: Karten, Lernstände, Plan, Sterne vorher = nachher, sonst Abbruch. In einer Transaktion einspielen.
- `supabase/migrations/20261122_wd_4b_stau_strecken.sql` – **eigene Datei, erst nach Probelauf und Sebastians Okay**: streckt einmalig gesetzte, heute fällige Etappen auf Stufe 0 (je Kind 6 je Lerntag); nur `faellig_am`, `wdh_ab`, `wdh_lerntage`; alte Werte in `schule.wdh_staffel_sicherung` (Rückweg im Kopf der Datei); prüft, dass sich sonst nichts ändert. Nur gelesen nachgerechnet: Kind 2 hat 34 solche Etappen → heute 6, dann 6/6/6/6/4 an den nächsten 5 Lerntagen; heute fällig 42 → 14 (die 8 übrigen sind natürlich gelandet oder mit Fehler und bleiben).
- `supabase/tests/wd_s_rauchtest.sql` – Rollback, nur Testkind; Prüfungen 1–9 (s. u.), 10: Karten, Lernstände, Plan, Sterne, Stufen (`thema_stufe`) und Reiseoptionen aller anderen Kinder vorher = nachher.
- `supabase/functions/lernen-api/index.ts`: Aktion `schule_wiederholung_runde_fertig: ['lernender_id']`, VERSION 0.9.0.

**Schnittstelle (wie im Nachtrag; Abweichungen fett)**
- `schule_wiederholung`: bisher `aufgaben`, `faellig`; neu `runde`, `runde_gemacht`, `gestaffelt`; `aufgaben[]` in WD-1-Reihenfolge (Wiederholungs-Fehler → am längsten fällig (`faellig_am`) → niedrigste Stufe), je Aufgabe zusätzlich **`pflicht`** (die ersten `runde`), `lernziel`, `wdh_stufe`. **`anzahl`** = höchstens so viele Aufgaben, Obergrenze jetzt 60 statt 6; ohne `anzahl` alle fälligen (≤ 60). Die App 0.84 schickt `anzahl: 6` → bekommt wie bisher 6 (jetzt in WD-1-Reihenfolge). Die neue App sollte `anzahl` weglassen.
- `schule_wiederholung_runde_fertig {lernender_id}` → `{ok, runde_gemacht: true, tag}`; Merker je Kind und `heute_tag`, zweimal setzen geht.
- `schule_uebung_pruefen`: bei Antwort auf eine **fällige** Etappe (auch Mischkarte) `wiederholung {bestanden, sterne, stufe_neu, naechste_in}`; bei Ablegen `abgelegt {etappe {titel, sterne}, flug? {titel, sterne}, ort_gold?}` – je Kind und Etappe/Flug/Ort einmal. `naechste_in` in Lerntagen; fehlt nach dem Ablegen.
- `schule_konto`: `konto.fluege[] {thema_id, einheit_id, titel, abgelegt, etappen_abgelegt, etappen}` (Flüge mit Karten), `konto.orte[].gold`.
- `gestaffelt` = gesetzte Etappen auf Stufe 0, die noch warten (erste Wiederholung später als in 1 Lerntag). „Kommt ab …“: `naechste_in` der Karte wie bisher.
- Mischkarten-Liste (`schule.mischkarten`): fällige zuerst; jede Karte aus der Auswahl trägt **`faellig`**.

**Regeln im Detail**
- WD-1: bis 6 fällige alle; sonst ⌈fällige/5⌉, mindestens 6, höchstens 12 (bis Kl. 6: 10). Regeln `wdh_runde_min/max/max_bis_kl6/teiler`.
- WD-3: Mischkarte aus fälliger Etappe, richtig ohne Tipp im 1. Versuch → wie eine richtige Wiederholung (Stufe +1, Takt 1/3/7/14/30), Beleg `misch_ok_am` wie bisher. Falsch → wie heute fällig, öffnet nie. Häufigkeit unverändert. Eine normale Wiederholung zählt wie heute auch mit Tipp/2. Anlauf als bestanden (Regel von `karte_buchen`, nicht geändert).
- WD-4: `flug_wdh_setzen` gibt jeder Etappe den ersten Lerntag mit freiem Platz (je Kind höchstens `wdh_gesetzt_je_lerntag` = 6 erste Wiederholungen je Lerntag), in Aufruf-Reihenfolge (Plan-Reihenfolge aus `plan_setzen_intern`, im Flug die Etappen-Reihenfolge).
- WD-6: „letzte Wiederholung“ = die Wiederholung auf Stufe 4 (30 Lerntage) bestanden → abgelegt: keine Fälligkeit mehr, 30 Sterne. **Flug abgelegt = alle Pflicht-Etappen abgelegt** (ohne Pflichtliste: alle Etappen) → 100 Sterne. Ort golden = alle Flüge mit Inhalt im Ort abgelegt (keine Sterne – die Schnittstelle nennt keine). Fällt eine abgelegte Etappe später auf (falsch beim Üben oder falsche Mischkarte), kommt sie wie heute für alle gelandeten Etappen am nächsten Lerntag zurück; Gold und Sterne bleiben, ein zweites Ablegen gibt nichts.

**Wirklich ausgeführt – lokal** (Postgres 16, Wegwerf-Datenbank): die 20 berührten Live-Funktionen **byte-gleich** (md5 je Funktion gleich), Platzhalter nur für `uebung_pruefen_intern` (speichert den Versuch wie live), `konto`, `thema_stufe`, `reiseoptionen` und Inhalts-Hilfen. Migration zweimal; Rauchtest 1–10 grün: Rundengröße (0/5/6/7/20/41/60/100 → 0/5/6/6/6/9/12/12, Kl. 6: 60 → 10), Reihenfolge und `pflicht`, Merker, bestandene Wiederholung (Stufe 2 → 3, Sterne einmal, keine `uebung`-Sterne), Mischkarte falsch/richtig, Ablegen Etappe/Flug (je einmal), Konto, Staffelung (Regel testweise 2: 14 Etappen → 2 je Lerntag), Mischkarten-Auswahl fällige zuerst, andere Kinder unverändert. Dazu `api.schule_uebung_pruefen` / `schule_wiederholung` / `_runde_fertig` / `schule_konto` mit Platzhalter-Zugang. WD-4b lokal: 14 → 6/6/2, zweiter Lauf ändert nichts.

**Vorschläge**
1. **„sicher“ (◉) gegenüber „abgelegt“:** Heute heißt ◉ „Stufe 4 erreicht und belegt (Mischkarte oder Nachtest)“ – also *vor* der letzten 30-Tage-Wiederholung. Vorschlag: auf der Kinderseite ◉ nicht mehr als eigenen Zustand zeigen, sondern die Stufe als „Wiederholung x von 5“ und am Ende nur Gold (abgelegt). Für Eltern/Lehrer bleibt „sicher“ als Beleg-Hinweis. Auf dem Server bleibt `karte_sicher` unverändert (Nachtest-Logik hängt daran). Alternative (nicht empfohlen, verzögert das Gold): Ablegen erst, wenn zusätzlich „sicher“.
2. **Nachtest nach dem Ablegen:** Heute ändert ein Nachtest den Karten-Takt nicht (er setzt nur die Etappe im Flug auf „fehler“ → Verbessern). Vorschlag wie im Auftrag: fällt eine abgelegte Etappe im Nachtest durch, kommt sie **einmalig mit 7 Lerntagen** (Stufe 2) zurück in den Takt; Gold, Sterne und Einblendung bleiben, ein erneutes Ablegen gibt nichts. **Nicht gebaut** – braucht eine Stelle in `test_abschliessen_intern`; auf Sebastians Okay als eigene kleine Datei.

## 2026-11-21 – FERTIG: 0.84.0 b – Matrix an LM-S 2 angepasst, Filter „Inhalt“, Info-Texte (Version bleibt 0.84.0, Cache v154)

Auf AUFTRAEGE.md „Rückläufer 21.11. morgens“, Teil D. Stand `lernen-app` d463182 übernommen. Nur App (`lernen.js`, `style.css`) und Tests. Nichts in der Datenbank, keine Kinderdaten, kein Merge nach `main`.
Bilder neu: `docs/previews/la/lm-oben-400/820/1280.png` (mit Filterzeile), `lm-matrix-*.png`.

**Datenformat LM-S 2** (Feldliste „FERTIG: LM-S 2“)
- Raster aus `schule_lehrplan_matrix`: Gebiet-Titel über `gebiet_id` aus `gebiete[]` (Spaltenreihenfolge = `reihenfolge`); `verbindungen[]` als Tripel `[thema_id, braucht_id, "h"|"e"]` (Objekte gehen weiter); `etappen_anzahl` → „Etappe x von y“ (y = `etappen_anzahl`, x = `etappe_jetzt`) und „Inhalte ansehen (n Etappen)“; `ohne_flug` blass; `eigenstaendig: true`. Fehlendes `fehler_offen` = nein (kein „Fehler besprechen ›“).
- Detail über die eigene Aktion **`schule_lehrplan_thema { thema_id }`** beim Antippen, einmal je Thema: `kurz, ort, was_gefordert, merke, etappen (pflicht → „· freiwillig“), beispiel, braucht/baut_darauf (Begründungen an den Verbindungen), lehrplan, eigenstaendig` (Text: „Eigenständig: braucht keine Voraussetzung – ‹Begründung›“). Bis die Antwort da ist: „Einzelheiten werden geladen …“; bei Fehler bleibt das Raster-Detail.
- Weiter parallel `schule_lehrplan_uebersicht` für Ort, Kurzbeschreibung im Raster, Inhaltsstand (◐ in Prüfung) und Aufträge. Ohne LM-S trägt die Übersicht allein (wie bisher).

**Filter „Inhalt“ (was fehlt noch?)** – eigene Zeile über dem Lernstand: „Alle · ● fertig n · ◐ in Prüfung n · ○ fehlt n“ (Zähler über alle Themen). Nicht passende Themen werden blass (wie bei der Suche, beides kombinierbar); Themen ohne Flug zählen nirgends mit. Im Detail weiter Inhaltsstand, „Inhalte ansehen“, Aufträge und „✎ Ändern lassen“.

**Info-Seite – Vorschlag zum Prüfen (umgesetzt):**
- „Wie entstehen die Inhalte …“, letzter Satz statt „Die Lehrplan-Übersicht … Eine Zeile antippen öffnet ‚Inhalte ansehen‘.“: „Der Lehrplan (Nachschlagen auf der Startseite) zeigt alle Flüge als Übersicht: Zeilen Klasse 5–10, Spalten die Themengebiete, eingeordnet nach Gymnasium, Realschule oder IB, in der Reihenfolge des Lehrplans. Der Filter „Inhalt“ zeigt, was fertig ist (●), was in Prüfung ist (◐) und was noch fehlt (○). Ein Thema antippen: was gefordert ist, was es vorher braucht, worauf es aufbaut, Lernbereich und „Inhalte ansehen“. Mit „Lernstand“ steht bei jedem Thema die Stufe eines Kindes (◉ ↻ ▶ ○ +) – ist ein Kind gewählt, lässt sich der Plan dort direkt ändern.“
- Lehrplan-Grundlage: „… Die Lehrplan-Übersicht zeigt alle Flüge.“ → „… Der Lehrplan (Nachschlagen auf der Startseite) zeigt alle Flüge auf einer Seite: Klasse 5 bis 10 und alle Themengebiete.“
- „Ändern lassen“: „Für Flüge ohne Inhalt steht er im Lehrplan, wenn man das Thema antippt, mit „Neuer Flug“ vorbelegt.“
- Expeditionen: „Alle Expeditionen mit Lösungen: Lehrplan → „Expeditionen ansehen“.“
- Erste Schritte, Schritt 3: „Im Lehrplan ein Thema antippen, dann „Inhalte ansehen“: …“, Link „Lehrplan ›“.
- Die Gliederung nach Lernbereich fällt im Text weg (Lernbereich steht im Detail). Test „LB Teil 7“ prüft den neuen Satz und dass „Lehrplan-Übersicht“ nicht mehr vorkommt.

**Gesehen/getestet**
- lernen: 141 Tests; im Gesamtlauf 140 bestanden, „LB Teil 8: aufgeklappte Karte“ wackelt unter Last (einzeln zweimal bestanden, wie schon in 0.84.0). Neu/ersetzt: „LM-S 2“ (Raster mit Tripeln, gebiet_id, etappen_anzahl, Detail über schule_lehrplan_thema mit Begründungen, eigenständig, freiwillig, fehler_offen, ohne Flug, Testkind) und „LM: Filter Inhalt“ (Zähler, blass, mit Suche, 400/820 ohne gebrochene Wörter und Querrollen). Testdaten: echte Themenliste, Verbindungen aus der Vorlage, Lernstand erfunden.
- Suche: die bekannten alten Fehler (PWA-Hülle, Startkarte, W80 ×4, Review301, Woanders gebucht, W88).

**Nicht geprüft / Hinweise**
- Gegen den echten LM-S-Server nicht getestet (LM-S 3 behebt erst den Abbruch der Migration). Die App fällt ohne LM-S auf die Übersicht zurück.
- `schule_lehrplan_thema` rufe ich ohne `lernender_id` auf (Eltern/Lehrer-Sicht).

## 2026-11-21 – bau-lehrer – FERTIG: flug_erstabschluss

Auf AUFTRAEGE.md „Rückläufer 21.11. morgens“, Teil C. Nur Dateien, in der echten Datenbank nichts ausgeführt, kein App-Code.
- `supabase/migrations/20261121_ab_s_flug_geschafft_robust.sql` **ersetzt** (der Entwurf mit `flug_fertig_nach` war nie eingespielt; die Funktion kommt nicht mehr vor):
  - Tabelle `schule.flug_erstabschluss (lernender_id, einheit_id, sitzung_id, am, primary key (lernender_id, einheit_id))`, RLS an, keine Rechte für public/anon/authenticated.
  - `schule.flug_erstabschluss_nachtragen(p_l default null)`: trägt alle Flüge ein, die jetzt fertig sind (alle Pflicht-Etappen nachgewiesen/korrigiert/gesichert), und alle mit abgeschlossener Flug-Test-/Verbessern-Sitzung mit `flug_geschafft = true` (`sitzung_id` = früheste solche, sonst null). Die Migration ruft sie einmal auf (NOTICE mit Anzahl); wiederholt: 0.
  - `test_abschliessen_intern`: die Stelle aus 20261120 wird ersetzt. Neu: `flug_geschafft` = dieser Aufruf schließt ab (blocktest/korrektur), Flug danach fertig, vorher nicht, **und** `insert … on conflict do nothing` hat eine Zeile angelegt (`found`). War der Flug vorher schon fertig, wird er nur festgehalten (`sitzung_id` null), `flug_geschafft` false. Die Stelle steht live genau einmal (gelesen).
- `supabase/tests/ab_s_abschluss_rauchtest.sql`: Prüfung 9 als eigener Block, die alten Sitzungen legt der Test selbst an:
  9a alter bestandener Flug + neue Pflicht-Etappe + Nachtragstest → false · 9b alte Sitzung vorher erneut gelesen → false (sperrt nichts) · 9c alter nicht bestandener Test + Verbessern → true mit Abschluss-Feldern, Eintrag mit dieser Sitzung · 9d zweimal abschließen (dieselbe Sitzung erneut + zweites Verbessern) → genau eine Sitzung mit true, ein Eintrag · 9e Nachtest → false.
- **Wirklich ausgeführt – lokal** (Postgres 16, eigene Wegwerf-Datenbank, erfundene Inhalte): `test_abschliessen_intern` lokal **byte-gleich zum Live-Stand** (md5 432e041a… gleich), Migration zweimal, Prüfung 9 grün; Gegenprobe mit der alten Funktion: 9c schlägt fehl (der Test unterscheidet). Nachtrag geprüft (fertig → null, true-Sitzung → deren id, nur Vertiefung → kein Eintrag, zweiter Lauf 0). Platzhalter lokal: `ort_stand`, `flug_abschluss`, `nachtest_*`, `thema_stand`.
- Gleichzeitige Sitzungen: entscheidet der Primärschlüssel (die zweite wartet auf die erste und legt nichts an) – lokal nicht nebenläufig getestet.

## 2026-11-21 – bau-lehrer – FERTIG: LM-S 3

Auf „Rückläufer 21.11. morgens“, Teil B. Ursache: in `schule.lehrplan_thema` (Feld `etappen`) eine Klammer zu viel vor `order by`. pglast prüft den Funktionsrumpf nicht – darum nicht aufgefallen.
- `supabase/migrations/20261121_lm_s_lehrplan_matrix.sql` behoben (md5 vorher 544f48ff…, jetzt 976e974e…).
- **Wirklich ausgeführt – lokal** (Postgres 16, Wegwerf-Datenbank): Tabellen mit den Live-Spalten (gelesen), `thema_einheit`/`thema_jahrgang` wie live, Platzhalter für `thema_stufe` und die Zugangsfunktionen, erfundene Inhalte und Kinder. Den Fehler „mismatched parentheses“ lokal nachgestellt, nach der Korrektur: Migration läuft (auch zweimal), Rauchtest ohne Spalte `eigenstaendig` grün (9 übersprungen), mit Spalte (Text) grün inkl. 9. Zusätzlich beide api-Aktionen mit Lehrer-, Kind- und fremdem Schlüssel: Kind bekommt nur sich selbst (fremde `lernender_id` wird ignoriert), fremder Zugang → „Kein Zugriff“, ohne `thema_id` → „thema_id fehlt“, Physik-Thema → „Thema nicht gefunden“.
- Rauchtest 8 nimmt jetzt ein Thema mit Pflicht-Etappen (vorher konnte es eines ohne merke/Etappen treffen).
- Feldliste unverändert (Eintrag „LM-S 2“).

## 2026-11-21 – FERTIG: 0.84.0 – Lehrplan-Matrix LM-1 bis LM-5 (Eltern/Lehrer), Cache v154

Stand `lernen-app` 168a744 übernommen (mit LM-S und Runde 30). Nur App (`lernen.js`, `style.css`), Version in sechs Dateien, Tests. Nichts in der Datenbank, keine Kinderdaten, keine Schlüssel, kein Merge nach `main`.
Bilder: `docs/previews/la/lm-oben-400.png`, `lm-oben-820.png`, `lm-oben-1280.png` (Kopf, Kind A gewählt), `lm-matrix-400/820/1280.png` (Thema mit Verbindungen und Detail), `lm-plan-link-400.png`.

**Gebaut**
- **LM-1:** Nachschlagen → „Lehrplan“ (`#/lehrplan`) ist jetzt die Matrix „Mathe Klasse 5–10: was gelernt wird“. Zeilen Kl. 5–10 in den Klassenfarben (LA-8), Spalten die Themengebiete inkl. Entdecker-Inseln (Reihenfolge aus `gebiete[]`, sonst wie die Vorlage); Schalter „Klassen als Zeilen / als Spalten“ (gemerkt). Alle Themen. „Einordnen nach“ Gymnasium · Realschule · IB MYP bestimmt die Zeile; fehlt die Schulart: andere bayerische Schulart, sonst MYP-Jahr + 5 → gestrichelt, mit Marke (RS/Gym/IB/Insel) und Erklärung im Detail. Kennzeichen „Gym 8 · RS 7 · IB 4“ (gewählte dunkel, fehlende durchgestrichen, orange wenn es die gewählte ist). Zelle in Lehrplan-Reihenfolge der Schulart. Kopf je Zeile „n Themen“ / „m Gym‑Pflicht“ (mit LM-S: `pflicht[]`). Suche, „Kurzbeschreibung“ (gemerkt). Unter 760 px Liste je Klasse nach Gebiet, Detail direkt unter dem Thema.
- **LM-2 Detail:** Titel, Gebiet, Klassen je Schulart, Lernbereich; Inhalt (● fertig, ◐ in Prüfung, ○ fehlt) mit „Inhalte ansehen (n Etappen) ›“, Aufträge-Link, Ort, „✎ Ändern lassen“ bei fehlendem Inhalt (aus LB-1); Was gefordert ist; Braucht vorher (Begründung, Klasse, „empfohlen“); Weiter zurück auf dem Weg; Darauf baut auf; Das muss sitzen; Beispielaufgabe; Schritte in der App (nicht-Pflicht-Etappen „· freiwillig“); Im Lehrplan (Wortlaut); ‹ › blättern. Ohne Voraussetzung: „Keine Voraussetzung hinterlegt …“; mit `eigenstaendig` „Eigenständig: braucht keine Voraussetzung – ‹Begründung›“. Liefert der Server keine Verbindungen (heute live), steht dort ehrlich „Die Verbindungen … liefert der Server noch nicht“.
- **LM-3:** gewählt → direkte Voraussetzungen gelb mit Linie, weiter zurück hellgelb, darauf aufbauend blau mit Linie, Rest blass, „empfohlen“ gestrichelt, „→ n“ ab 2 Nachfolgern. Linien als SVG **hinter** den Karten (z-index 1 < 2, im Test per `elementFromPoint` geprüft); Handy ohne Linien.
- **LM-4:** Leiste „Lernstand: Aus · Kind A · Kind B · Beide vergleichen“ (bei mehr Kindern „Alle vergleichen“); ein Kind: Hintergrund je Stufe **in den Farben des Plans** (LB), „▶ Etappe x von y · hier ist ‹Name›“ (`etappe_jetzt`), „↻ Wdh n von 5“, „+ nicht im Plan“ gestrichelt/blass; beim Einschalten zum ▶-Thema gescrollt; Schulart springt auf die des Kindes. Vergleich: „A/B“ mit zwei Punkten in Stufenfarbe. Kopf je Klasse: Balken je Kind (◉ ↻ ▶) über die Pflichtthemen. Detail: Lernstand je Kind (Stufe, Zusatz wie im Plan, nächste Wiederholung) mit „Im Plan öffnen ›“ und „Fehler besprechen ›“ (nur bei `fehler_offen`; ohne LM-S bei `wieder_offen`) → Reiter „Was wackelt“ des Kindes.
- **LM-5:** Im Detail bei genau einem Kind die Stufen-Knöpfe aus LB Teil 8 (Lernen · Kann er – wiederholen · Kann er komplett, rechts „Aus dem Plan nehmen“/„In den Plan nehmen“, bei ◉ „Wieder in die Wiederholung“). Dafür ist der Plan-Kern aus `viewPlan` herausgelöst (`lernPlanSetzeIn`, `lernPlanEintraege`, …) – **dieselben Aufrufe** (`schule_plan_lesen`, `schule_plan_setzen` mit revision, Rückgängig mit `schritt_id`, Konflikt sperrt mit „Neu laden“). Nach dem Speichern werden die Stufen neu geholt. „Im Plan öffnen ›“ springt in den Reiter „Plan“: Flug im Plan → Ort links aufgeklappt und markiert; sonst rechts „Nach Klasse“ mit dem Flug aufgeklappt. Reiter „Plan“: Link „Als Matrix ansehen ›“ rechts in der Reiterzeile (Handy: darunter), öffnet `#/lehrplan/<kind>` mit Kind und Schulart; kein fünfter Reiter.

**Daten (LM-S)**
- Die App ruft `schule_lehrplan_matrix` **und** `schule_lehrplan_uebersicht` parallel: die Matrix-Daten tragen, die Übersicht liefert Inhaltsstand (◐ in Prüfung) und Aufträge je Flug, die LM-S nicht hat. Kennt der Server `schule_lehrplan_matrix` noch nicht (heute live), trägt die Übersicht allein – alles läuft, nur ohne Verbindungen, Das muss sitzen, Beispiel, Pflicht-Etappen.
- Aus dem Plan eines Kindes, das nicht in `kinder[]` ist (Testkind), lädt die App erneut mit `mit_testkind: true`.
- Vorbereitet für **LM-S 2** (Nachbesserung 21.11., noch nicht gebaut): `eigenstaendig` als Text (auch `true`), `ohne_flug: true` → Karte blass gepunktet + Hinweis im Detail. Fehlen in der Liste `lehrplan` **und** `merke`, lädt das Detail einmal nach mit **`schule_lehrplan_matrix { thema_id }`** und erwartet `themen[0]` (oder `thema`) mit `lehrplan, merke, beispiel` (Annahme zu Name/Form – bitte so bauen oder mir den Namen melden; Anpassung ist eine Zeile).

**Was von der bisherigen Lehrplan-Übersicht (LB-1) wegfällt** (Auftrag: nennen)
- Die Kacheln „Flüge · fertig · in Prüfung · fehlt“ mit Zählern und der **Filter nach Inhaltsstand** – der Inhaltsstand steht nur noch je Thema im Detail. Wer „was fehlt noch?“ sucht, hat keinen Sammelblick mehr.
- **Gruppen nach Lernbereich** (Überschriften „M8 2 Lineare Funktionen“) – die Matrix gliedert nach Themengebiet; der Lernbereich steht im Detail.
- Klassen-Knöpfe mit Kind-Marken (A/B) – ersetzt durch die Lernstand-Leiste.
- „Zeile antippen → Inhalte ansehen“ ist jetzt zwei Schritte (Thema antippen, dann „Inhalte ansehen ›“).
- Die Tabelle „Stufe je Kind in einer Zeile mit Wort“ – ersetzt durch „Beide vergleichen“ (Punkte, Wort im Detail).
- **Info-Seite:** Die wörtlichen Texte aus Teil 7 beschreiben noch die alte Übersicht („Eine Zeile antippen öffnet ‚Inhalte ansehen‘“, „Lehrplan-Übersicht ›“). Nicht geändert – bitte neuen Wortlaut liefern.

**Abweichungen von der Vorlage**
- Stufenfarben wie im Plan (◉ grün, ↻ hellgrün, ▶ gelb mit Rahmen) statt der Vorlagenfarben (Wdh gelb, dran blau) – die Vorgabe sagt „wie im Plan (LB)“. Dadurch ähnelt ▶ dem Gelb der Voraussetzungen; die Rolle zeigt zusätzlich der Rahmen.
- „IB MYP“ als dritte Schulart in „Einordnen nach“ (für ein IB-Kind nötig); Zeilen bleiben Kl. 5–10 mit „MYP-Jahr n“ darunter.
- Die Liste vermuteter Zuordnungslücken der Vorlage (`LUECKE`) ist nicht übernommen – das klärt Runde 30 in den Daten.
- Silbentrennung (`hyphens: auto`) in Karten und Gebietsköpfen: Wörter werden nur mit Trennstrich umbrochen, nie ohne; „Gym‑Pflicht“ mit festem Bindestrich.

**Gesehen/getestet**
- lernen: 141 von 141 (neu 9 Tests: LM-1; LM-2/LM-3; LM-4; LM-5 Knöpfe/Rückgängig/Im Plan öffnen/Als Matrix; Abnahme 400/820/1280 je Lernstand-Modus und Aufbau – nichts läuft über, kein Umbruch ohne Trennstrich, kein Querrollen, Handy Liste ohne Linien, Detail unter dem Thema; Link in der Reiterzeile; LM-S-Format; LM-S-2-Nachladen). Ersetzt: vier Tests der alten Übersicht (LA-7 Tabelle, LA-7 Tablet, I-3 Liste, LB Teil 5 S3 → jetzt Reihenfolge je Zelle und Lernbereich im Detail). Testdaten: echte Themenliste, Verbindungen aus der Vorlage, Lernstand erfunden (Kind A/Kind B, Testkind).
- Suche: die bekannten alten Fehler (PWA-Hülle, Startkarte, W80 ×4, Review301, Woanders gebucht, W88) und das datumsabhängige „W80: Jede neue Suche“; „LB Teil 8: aufgeklappte Karte“ wackelte einmal im Gesamtlauf und besteht einzeln.

**Nicht geprüft / Hinweise**
- Mit echten Daten und echten Geräten nicht angesehen; nur Chromium. Mit dem LM-S-Server nur gegen nachgebildete Antworten getestet (Feldliste oben).
- Größe: LM-S im Probelauf 249 KB plus Übersicht – auf langsamer Verbindung spürbar, bis LM-S 2 den Wortlaut auslagert.
- Auf dem Tablet (820 px) sind acht Spalten eng: viele Titel werden getrennt (mit Trennstrich). „Klassen als Spalten“ ist dort etwas luftiger.
- Nächster Schritt: LM-6 Kinderseite als 0.85.0.

## 2026-11-21 – bau-lehrer – FERTIG: LM-S 2

Auf AUFTRAEGE.md „Nachbesserung Dreißigste Runde und LM-S (21.11.)“, Teil B. Nur Dateien, nichts ausgeführt, kein App-Code. Die LM-S-Dateien von heute früh sind ersetzt (nicht eingespielt, daher in derselben Datei).

**Dateien:** `supabase/migrations/20261121_lm_s_lehrplan_matrix.sql`, `supabase/tests/lm_s_lehrplan_matrix_rauchtest.sql`, `supabase/functions/lernen-api/index.ts` (neue Aktion `schule_lehrplan_thema: ['thema_id', 'lernender_id?']`, VERSION 0.8.0).

**Was sich ändert**
- `eigenstaendig` ist Text (Begründung, null = nicht gekennzeichnet), gelesen über `to_jsonb(t)->>'eigenstaendig'` – läuft vor und nach `20261121_lehrplan_zuordnung_voraussetzungen.sql` (der boolean-Abbruch ist weg). Raster: `eigenstaendig: true`, wenn gesetzt; Detail: der Begründungstext; Kind: nie.
- `ohne_flug: true` bei Themen ohne freigegebene Einheit (dann auch kein `einheit_id`, kein `etappen_anzahl`) – im Raster und im Detail.
- Aufgeteilt in **Raster** (`schule_lehrplan_matrix`) und **Detail** (`schule_lehrplan_thema`, beim Antippen). Zugang für beide gleich (`schule.lehrplan_sicht`): Eltern/Lehrer → Lehrer-Sicht; Lern-Zugang → nur das Kind selbst; sonst `lernender_id` + `schule.zugriff`.

**Größe** (Teile nur lesend nachgerechnet, 21.11.): Raster Lehrer ≈ 43 KB Themen + ≈ 1 KB Verbindungen + ≈ 11 KB Lernstand je Kind → mit zwei Kindern ≈ 65 KB (vorher 249 KB). Kindsicht deutlich kleiner (ohne jahrgang/lernbereich/pflicht). Detail ≈ 2–5 KB je Thema. Rauchtest Prüfung 7 bricht ab, wenn das Lehrer-Raster mit allen aktiven Kindern ≥ 90 000 Zeichen hat; Prüfung 8 beim Detail ≥ 30 000.

**Feldliste Raster** `{ok, kindsicht, themen[], verbindungen[], gebiete[], kinder[], lernstand{}}` (fehlende Werte weggelassen; fehlt = nein)
- `themen[]` je Mathe-Thema einmal, sortiert Gebiet → Thema: `thema_id, schluessel, titel, gebiet_id, block_id, einheit_id | ohne_flug, etappen_anzahl`; nur Lehrer: `jahrgang {gym_by, rs_by, ib_myp}`, `lehrplan_reihenfolge`, `lernbereich`, `pflicht [schularten]`, `eigenstaendig: true`; nur Kind: `zeile {klasse, eingeordnet?}`, `reihenfolge_kind`.
- `verbindungen[]` = `[thema_id, braucht_id, "h"|"e"]` („thema_id braucht braucht_id“, h = hart, e = empfohlen). „Weiter zurück“ = Kette darüber.
- `gebiete[] {gebiet_id, titel, reihenfolge, zusatz}` (Gebiet-Titel nur hier).
- `kinder[] {id, name, klasse, schulart}` (Kind: nur es selbst, ohne schulart).
- `lernstand[kind_id][thema_id]`: `stufe` (immer), sonst nur wenn gesetzt: `zeichen, im_plan, begonnen, gelandet, sicher, wieder_offen, wdh_nr, naechste_in, rueckreise, test_offen, hinweis, etappe_jetzt` (nur bei „dran“; „Etappe x von y“ mit y = `themen[].etappen_anzahl`), nur Lehrer `fehler_offen`. Weggelassen gegenüber thema_stufe: `etappen, gesetzt, ohne_test, wdh_stufe_min`.

**Feldliste Detail** (`daten: {thema_id}`; Kind über Lern-Zugang ohne weitere Angabe)
- `thema_id, titel, kurz, ort, was_gefordert, einheit_id | ohne_flug, merke [], etappen [{lernziel, titel, pflicht}], beispiel` (< 160 Zeichen), `braucht [{thema_id, titel, art, begruendung}]`, `baut_darauf [{thema_id, titel, art, begruendung}]`; nur Lehrer: `lehrplan {schulart: Wortlaut}`, `eigenstaendig` (Text). Kind: ohne `lehrplan`, `eigenstaendig`, `pflicht`, `begruendung`.

**Rauchtest:** 1–8 wie gehabt angepasst (Raster knapp, ohne_flug, Detail, Größe); 9 eigenständig als Text (setzt in der Transaktion eine Begründung an einem Thema und nimmt sie zurück; übersprungen, solange die Spalte fehlt); 10 Selbstprüfung als NOTICE: 10a–c wie bisher (10a: eigenständig = Begründung gesetzt), neu 10d „keine Verbindung von oder zu einem Thema ohne Flug“ (Teil A).

**Annahmen:** Kindsicht-Zeile MYP-Jahr + 5 = Klasse. Größe je Kind steigt mit Fortschritt (mehr gesetzte Felder); Obergrenze grob ≈ 15 KB je Kind.

## 2026-11-21 – bau-lehrer – FERTIG: LM-S

Bau-Auftrag LM (21.11.), Schritt 1. Nur Dateien, nichts ausgeführt, kein App-Code, kein Merge nach main, keine Kinderdaten.

**Dateien**
- `supabase/migrations/20261121_lm_s_lehrplan_matrix.sql`: `schule.thema_klasse_fuer(jahrgang, schulart)`, `schule.lehrplan_matrix(kinder[], kindsicht)` (innere Funktion), `api.schule_lehrplan_matrix(schlüssel, daten)` (security definer, Rechte wie üblich: nur council_mcp). Kein DROP/DELETE, Bestand unverändert, wiederholbar. `api.schule_lehrplan_uebersicht` bleibt unverändert (App 0.83 nutzt sie weiter).
- `supabase/tests/lm_s_lehrplan_matrix_rauchtest.sql`: Rollback, nur Testkind, Prüfungen 1–7 vergleichen gegen die Tabellen (keine festen Bestandszahlen), Prüfung 6 legt sich „Fehler offen“ im Testkind selbst an; Prüfung 8 = Selbstprüfung (s. u.).
- `supabase/functions/lernen-api/index.ts`: Aktion `schule_lehrplan_matrix: ['lernender_id?', 'mit_testkind?']`, VERSION 0.8.0 (Server-Datei, muss mit deployt werden).

**Befund: was die Übersicht nicht liefert** (Live-Text gelesen): merke, Etappen mit Pflicht, Verbindungen (Art, Begründung), kurz, Pflicht je Schulart, Beispielaufgabe, Gebiet-Reihenfolge, „Etappe x von y“, „Fehler offen“, Kinderzugang. Außerdem eine Zeile je Thema × Ort (Matrix braucht je Thema einmal).

**Zugriff**
- Eltern/Lehrer (`schule.ist_leiter`): alle aktiven Kinder in einem Aufruf; Testkind nur mit `mit_testkind: true`.
- Kind (Lern-Zugang): nur es selbst (aus `lern_ich`; `lernender_id` wird ignoriert). Sonstige Zugänge: `lernender_id` + `schule.zugriff`. Immer Kindsicht.

**Feldliste für den App-Bau** (`ergebnis` = `{ok, kindsicht, themen[], verbindungen[], gebiete[], kinder[], lernstand{}}`; fehlende Werte sind weggelassen, nicht null)
- `themen[]` (je Mathe-Thema genau einmal; sortiert Gebiet → Thema-Reihenfolge):
  - beide Sichten: `thema_id, schluessel, titel, kurz, gebiet, gebiet_id, ort, block_id` (erster Ort nach Block-Reihenfolge), `was_gefordert` (= thema.beschreibung, „Was gefordert ist“), `einheit_id` (nur mit freigegebener Einheit), `merke` (Array, „Das muss sitzen“), `etappen[] {lernziel, titel, pflicht}`, `beispiel` (erste freigegebene Übungsaufgabe, Text < 160 Zeichen)
  - nur Eltern/Lehrer: `jahrgang {gym_by, rs_by, ib_myp}` (Klasse je Schulart; IB = MYP-Jahr), `lehrplan_reihenfolge {schulart: n}`, `lernbereich {schulart: …}`, `lehrplan {schulart: Wortlaut}`, `pflicht [schularten]` (Thema einem Eintrag einer aktiven Basis-Quelle zugeordnet), `eigenstaendig` (s. u., heute nie gesetzt)
  - nur Kindsicht: `zeile {klasse, eingeordnet}` (Klasse in der Schulart des Kindes; fehlt sie, die der anderen bayerischen Schulart bzw. MYP+5 → `eingeordnet: true`), `reihenfolge_kind`
- `verbindungen[] {thema_id, braucht_id, art: hart|empfohlen, begruendung}` – „thema_id braucht braucht_id“. Kindsicht ohne `begruendung`. „Braucht vorher“, „weiter zurück“ (Kette) und „Darauf baut auf“ rechnet die App daraus; Klasse der Voraussetzung über `themen[].jahrgang`. Leere Liste → Hinweis „Keine Voraussetzung hinterlegt“.
- `gebiete[] {gebiet_id, titel, reihenfolge, zusatz}`
- `kinder[] {id, name, klasse, schulart}` – Kindsicht: nur das Kind, ohne `schulart`.
- `lernstand[kind_id][thema_id]` = `schule.thema_stufe` (u. a. `stufe, zeichen, im_plan, etappen, begonnen, gelandet, sicher, wieder_offen, wdh_nr, naechste_in, rueckreise, test_offen`) + `etappe_jetzt` (nur bei stufe „dran“: gelandet+1, höchstens etappen → „Etappe x von y“ mit y = `etappen`) + nur Eltern/Lehrer `fehler_offen` (Pflicht-Etappe mit Status „fehler“ → Link „Fehler besprechen ›“).

**„eigenständig“** – Fakt: wird heute nirgends gespeichert. Vorschlag (nicht gebaut): Spalte `schule.thema.eigenstaendig boolean default false` (+ ggf. `eigenstaendig_grund text`), gesetzt vom Lehrplan-Chat. Die Matrix-Funktion und Regel 8a lesen sie schon über `to_jsonb(t)->'eigenstaendig'` – sobald die Spalte da ist, wirkt sie ohne weitere Änderung. Entscheidung, wer sie anlegt: Haupt-Chat.

**Selbstprüfung Dreißigste Runde** (Rauchtest Prüfung 8, NOTICE mit Anzahl und Nummern, kein Abbruch). Stand heute, nur gelesen:
- 8a Thema mit Klasse ohne Verbindung, nicht eigenständig: 28 (17, 19, 22, 27, 34, 40, 42–45, 59, 60, 64–66, 69, 70, 73, 75, 81, 83, 84, 98–103).
- 8b Voraussetzung in späterer Klasse als das Thema: 1 (33 braucht 32, nur IB-MYP).
- 8c Themen 100–103 verknüpft: nein, alle 4 ohne Verbindung.
→ Die Regeln sind heute nicht erfüllt; deshalb NOTICE statt Abbruch. Sollen sie nach dem Nachpflegen hart werden: in Prüfung 8 NOTICE → EXCEPTION.

**Annahmen / offen**
- Kindsicht-Zeile: MYP-Jahr + 5 = Klasse (wie in lernen.js).
- Größe: Lehrer-Antwort ca. 140 KB (Themen ~113 KB ohne Lehrplan-Wortlaut + ~24 KB Wortlaut) plus Lernstand je Kind. Wenn das zu groß ist: Wortlaut erst im Detail nachladen.
- Rauchtest-Prüfung 6 braucht eine Einheit mit Pflicht-Etappe (sonst „übersprungen“).

## 2026-11-21 – bau-lehrer – FERTIG: flug_geschafft robust 2

Auf antworten.md „21.11. 04:25“. Nur Dateien, nichts ausgeführt, kein App-Code, kein Merge nach main.
- Neu: `supabase/migrations/20261121_ab_s_flug_geschafft_robust.sql` – legt `schule.flug_fertig_nach(lernender, einheit, sitzung)` an und baut die eingespielte `schule.test_abschliessen_intern` um: alte Bedingung `x.flug_geschafft is distinct from false` → `x.flug_geschafft or (x.flug_geschafft is null and schule.flug_fertig_nach(...))`. Umbau über `pg_get_functiondef` + `replace`; die Stelle steht live genau einmal (gelesen 21.11.). Wiederholbar: ist `flug_fertig_nach` schon im Funktionstext, passiert nichts. Fehlt die Stelle (alte Datei nicht eingespielt), bricht die Migration mit Hinweis ab.
- Zurückgesetzt: `20261120_ab_s_flug_abschluss_einmal.sql` = eingespielter Stand (Commit 80e67e8, md5 f79c1701…).
- `supabase/tests/ab_s_abschluss_rauchtest.sql`: nur Kopfzeile – Prüfung 9 setzt jetzt beide Dateien voraus. Prüfung 9 (9a–9e) unverändert.
- Reihenfolge Haupt-Chat: neue Datei einspielen → Rauchtest ab_s (Prüfung 9c muss jetzt grün sein).

## 2026-11-21 – FERTIG: 0.83.3 – App 0.83.3, Cache v153

Stand `lernen-app` 05037ef (0.83.2 live, Nachträge aus Prüfergebnis 888). Nur App (`lernen.js`, `style.css`), Versionsnummer in sechs Dateien, Tests. Nichts in der Datenbank, keine Kinderdaten, keine Schlüssel, kein Merge nach `main`.

1. **„Etappen ▸“ (Entscheidungen Sebastian 21.11., Punkt 3):** In der Inhalte-Zeile der kompakten Themen-Karte („Inhalte ansehen (n Etappen)“ · „Ort: …“) steht ein zugeklappter Textlink „Etappen ▸“ (`aria-expanded`, `aria-controls`). Aufgeklappt („Etappen ▾“) die Liste wie in 0.83.0: Nummer, Titel, Stand rechtsbündig in der ersten Titelzeile (offen / begonnen / gelandet / sicher / wieder offen, Farben wie vorher). Zuklappen mit demselben Link, der Fokus bleibt darauf. Gilt in „Nach Klasse“ und im aufgeklappten Ort unter „Nach Themengebiet“. Bei Flügen ohne Etappen gibt es den Link nicht.
2. **Reisewörter (Punkt 4):** Der Test „Reisewörter auf allen Eltern-/Lehrerseiten“ verbietet „Thema“, „Themen“ (und damit „Themengebiet“) nicht mehr; „Lernkarte“, „Aufgabe“, „Themenplan“, „Lernziel“ und das alleinstehende „Gebiet“ bleiben auch dort verboten (enge Auslegung – sag Bescheid, wenn auf Eltern-/Lehrerseiten gar nichts mehr geprüft werden soll). Ebenso im Test der Info-Seite. Neu: **Test „Reisewörter auf den Kinderseiten“** (Abflugtafel, Reisepass, Erklärung, Bordkarten, Flug-Test; klassisch und neue Gestaltung) gegen Lernkarte, Aufgabe, Themen, Themenplan, Lernziel, Gebiet. Hinweis: „Thema“ (Einzahl) prüfe ich dort nicht, weil die Abschluss-Ansichten es laut Vorgabe selbst verwenden („Weiter zum nächsten Thema“, „NEUES THEMA“). Keine Texte geändert.
3. **Nachtrag 888 (Teil bau-motivation):** Meldet der Server `ort_geschafft: true` mit `flug_geschafft: false`, startet die Abschluss-Ansicht direkt mit dem Ort-Stempel, danach die Bordkarte – kein zweites „Flug geschafft“. Bei `flug_geschafft: true` und `ort_geschafft: true` bleibt die Reihenfolge Flug → Ort → Bordkarte; ohne das Feld (alter Server) wie 0.83.0.

**Getestet** (Playwright mit Chrome): **lernen 135 von 135** – neu 3 („Etappen ▸“ auf 400 px mit Lage des Stands und Fokus; Reisewörter Kinderseiten; nur `ort_geschafft`), angepasst 3 (Reisewörter Eltern/Lehrer, Info-Seite, Nachtrag B: Fall „flug und ort geschafft“). Alle Tests: 277 bestanden, 1 übersprungen, 9 Fehler – die 9 bekannten im Reise-Bereich. W175 ist heute wieder grün (datumsabhängig); „W80: Jede neue Suche hat eine Reise“ fiel in einem Gesamtlauf einmal aus und lief danach dreimal grün (Reise-Bereich, wackelt).

**Nicht geprüft:** echte Geräte und Safari, Bildschirmleser, gegen den echten Server.

FERTIG: 0.83.3

## 2026-11-21 – FERTIG: flug_geschafft robust (Nachträge aus ChatGPT 888)

Stand `lernen-app` 05037ef übernommen. Nur Dateien – nichts ausgeführt, kein App-Code, kein Merge. pglast ok.
**Migration** `supabase/migrations/20261120_ab_s_flug_abschluss_einmal.sql` (weiter nicht eingespielt):
- neu `schule.flug_fertig_nach(kind, einheit, sitzung)`: War der Flug nach dieser Sitzung fertig? Je Pflicht-Etappe zählt das letzte Ergebnis in einem abgeschlossenen Flug-Test, Verbessern oder Nachtest bis einschließlich dieser Sitzung (alle Antworten der Etappe richtig); eine Pflicht-Etappe ohne Ergebnis bis dahin → nicht fertig.
- Bedingung „früherer Abschluss“: frühere abgeschlossene Flug-Test-/Verbessern-Sitzung mit `flug_geschafft` true **oder** mit NULL **und** `flug_fertig_nach(...)` true. Eine alte nicht bestandene Sitzung (NULL, Flug danach offen) sperrt also keinen späteren ersten Abschluss mehr. Alles andere unverändert (vorher nicht fertig; nur `blocktest`/`korrektur`; einmal festgehalten).
**Rauchtest** `ab_s_abschluss_rauchtest.sql`, Prüfung 9 neu aufgebaut – **ohne Überspringen**: Die Sitzungen legt der Test selbst an (Hilfsfunktion `pg_temp.ab9_sitzung`: eine Bordkarte je Pflicht-Etappe, Antworten richtig/falsch), abgeschlossen wird über `test_abschliessen_intern`; Flug mit mindestens 2 Pflicht-Etappen in einem Ort mit weiteren offenen Flügen.
- 9a/9b nicht bestanden + erneuter Aufruf → false, keine Felder.
- **9r/9c Regression:** die nicht bestandene Sitzung auf NULL gesetzt (wie alt), Flug offen → Verbessern macht ihn erstmals fertig → **true** mit Feldern; erneuter Aufruf gleich.
- 9c-2: die erste Verbessern-Sitzung auf NULL gesetzt (alte Sitzung, die den Flug fertig gemacht hatte) → zweites Verbessern → false.
- 9d Nachtragstest → false. **9e Nachtest (neu, eigener Negativfall)** → false, keine Felder.
**Hinweis:** Vor dem Probelauf die Bestandsprüfung aus 888 gilt weiter (7 alte Sitzungen, alle zu fertigen Flügen) – mit der neuen Bedingung zählen sie als frühere Abschlüsse, wenn `flug_fertig_nach` sie als fertig erkennt.

## 2026-11-21 – FERTIG: 0.83.2 (LB Teil 9, Punkte 1, 2, 4, 5, 6) – App 0.83.2, Cache v152

Stand `lernen-app` b2a71ba übernommen. Nur App (`lernen.js`, `style.css`), Versionsnummer in sechs Dateien, Tests. Nichts in der Datenbank, keine Kinderdaten, keine Schlüssel, kein Merge nach `main`. **Punkt 3 (N8, Wort „Themen“) bleibt offen** – nichts geändert.

**Lehrer-Ansicht**
1. **N6:** Der gewählte Themengebiet-Knopf (`.lern-chip[aria-pressed="true"]`) behält beim Hover den dunklen Hintergrund und die weiße Schrift (gilt für alle Chips dieser Art; die eigenen Farben der Kinderseite bleiben). Gemessen: Kontrast unter dem Zeiger ≥ 4,5 : 1; nicht gewählte Knöpfe werden beim Hover weiter hell.
2. **N7 (Handy < 560 px):** Titel der Plan-Zeile ist nur noch das Thema; das Themengebiet steht klein und grau am Anfang der Zeile darunter („Algebra · ▶ Gerade dran · …“). Der volle Titel bleibt im `title` und im Bildschirmleser-Namen. ↑ ↓ sind 32 px breit. Die automatische Silbentrennung aus Teil 6 ist wieder aus – damit gibt es **nie Trennstrich und „…“ hintereinander**. Messung mit der echten Themenliste (36 Plan-Zeilen): **400 px: 2 Titel mit „…“** (Nachprüfung 5: fast alle; nach Teil 6: 12); 820 px: 6 (die Trennung fehlt jetzt auch dort; vorher 3, ursprünglich 28). Ab 560 px steht das Gebiet wie bisher vor dem Titel.
4. **Info-Seite, Schritt 1:** „Rechts (auf dem Handy darunter) der Lehrplan: …“.

**Abschluss-Ansichten (Kind)**
5. **N1:** Datum im Ort-Stempel wird selbst gebaut („21.11.“) statt `toLocaleDateString` + Punkt – nie „..“, unabhängig vom Browser.
6. **N2:** 18 px Abstand unter „2/2“ (der Schrägstrich berührt „AUF ANHIEB“ nicht mehr; 400 × 780 weiter ohne Scrollen). **N3:** Der Blitz beim Sturmflug beginnt weiter rechts unten (neben dem Flugzeug) – maschinell geprüft: bei 360 × 640, hell und nacht, liegt kein Punkt des Blitzes in Titel, Unterzeile, Abzeichen oder Kopfzeile (mit dem alten Blitz schlägt die Prüfung fehl). **N4:** Test „AB-A 2“ wartet jetzt auf das Schließen der Ansicht (`.lr-abschluss` detached, höchstens 3 s) – 5 von 5 Läufen grün. **N5:** „Überspringen ›“ auf dem Ort-Bildschirm: dunkelbraun (#3B2A14) mit hellem Rand, fett; Kontrast Schrift/Knopf ≥ 4,5 : 1, Knopf/Sand ≥ 3 : 1 (gemessen).

**Getestet** (Playwright mit Chrome): **lernen 132 von 132** – neu 5 (N6, N7 mit Messung, Info-Schritt 1, N1/N5, N2/N3), angepasst 3 (AB-A 2 wartet auf das Schließen; „Teil 6 N2“ prüft zusätzlich „nie Trennstrich und …“ und ≤ 4 gekürzte auf dem Handy; „Flugplan: Änderung bleibt …“ liest die Reihenfolge aus dem Titel-Attribut, weil auf dem Handy das Gebiet nicht mehr im Titel steht). Alle Tests: 273 bestanden, 1 übersprungen, 10 Fehler – alle im Reise-Bereich, dieselben wie bei 0.83.1 (die 9 bekannten und W175, datumsabhängig).

**Nicht geprüft:** echte Geräte und Safari, Bildschirmleser; „Hover bleibt auf dem Tablet hängen“ (N6) nur am Rechner nachgestellt.

FERTIG: 0.83.2

## 2026-11-21 – FERTIG: 0.83.1 (LB Teil 8 und Nachtrag B) – App 0.83.1, Cache v151

Stand `lernen-app` 31b73f6 übernommen, dazu `bau-lehrer` 80e67e8 („FERTIG: flug_geschafft“ lag vor); vor dem Push `lernen-app` 44a30d2 eingemischt (nur Postfach/Inhalte). Nur App (`lernen.js`, `style.css`), Versionsnummer in sechs Dateien (`app.js`, `index.html`, `lernen/index.html`, `lernen/schule.js`, `sw.js`, `tests/search.test.cjs`), Tests. Nichts in der Datenbank, keine Kinderdaten, keine Schlüssel, kein Merge nach `main`.

**LB Teil 8 – aufgeklappte Themen-Karte, Variante A** („Nach Klasse“ und aufgeklappter Ort in „Nach Themengebiet“)
- Kopf, „Lehrplan: …“ und Beschreibung unverändert.
- Eine Zeile: Knopf „Inhalte ansehen (n Etappen)“ mit Rahmen in Akzentfarbe (öffnet `#/inhalte/<Flug>` wie bisher), daneben klein und grau „Ort: <Ort>“; ohne Inhalt steht dort „noch kein Inhalt“. Die Etappen-Kästchen entfallen.
- Trennlinie, dann „Stufe ⓘ“ (ⓘ öffnet „So funktioniert’s“ mit aufgeklappter Frage „Was kann ich selbst ändern?“, in der die vier Stufen erklärt sind – neue Adresse `#/info/stufen`) und drei schmale Knöpfe „Lernen“ · „Kann er – wiederholen“ · „Kann er komplett“; der aktive grün hinterlegt mit „✓“. Keine Erklärungszeilen mehr.
- Rechts als roter Textlink „Aus dem Plan nehmen“, außerhalb des Plans „In den Plan nehmen“ (Akzentfarbe). Wirkung und Speichern unverändert (dieselbe `setze`-Funktion wie bisher).
- Rückfall-Hinweis aus Teil 6 bleibt im Kopf der Zeile sichtbar. Nebenbei berichtigt: Er erscheint nur noch bei der Stufe ◉ (vorher auch, wenn die App einen „komplett“ gesetzten Flug lokal auf „Kommt noch“ umrechnete).
- **Abweichungen / offen (bitte entscheiden):**
  1. **Etappen-Liste mit Stand (Teil 5 S4) ist im Plan nicht mehr zu sehen.** „Inhalte ansehen“ zeigt die Inhalte, nicht den Stand des Kindes je Etappe. Den Stand je Etappe sehen Eltern/Lehrer weiter unter „Was wackelt“ (nur Etappen mit Fehlern) und auf der Abflugtafel des Kindes. Wenn er im Plan bleiben soll: Vorschlag ein zugeklappter Textlink „Etappen ▸“ in der Inhalte-Zeile.
  2. **„Wieder in die Wiederholung“** steht bei ◉-Flügen weiter in der Stufen-Zeile, als grauer Textlink (sonst ginge die Funktion in der Karte verloren; Variante A nennt ihn nicht).
  3. **„Aus dem Plan nehmen“ in derselben Zeile** passt nur, wenn die Spalte breit genug ist. Die Lehrplan-Spalte ist auch bei 1280 px nur etwa 450 px breit – dort und bei 820 px steht der Link rechtsbündig in einer eigenen Zeile unter den Knöpfen (wie auf dem Handy). Siehe `test-results/lb8-karte-{400,820,1280}.png` beim Testlauf.
  4. Die alte Etappen-Liste mit Stand rechts (Teil 6 N5) ist damit ebenfalls weg; ihr Test entfällt.
- Abnahme: 400, 820, 1280 – kein Wort mitten im Wort umbrochen in der Karte (gemessen vor und nach dem Umschalten), kein Querrollen, zugeklappte Zeilen unverändert.

**Nachtrag B – Flug-Abschluss an `flug_geschafft`:** Die Abschluss-Ansicht des Flugs kommt, wenn die Antwort `flug_geschafft: true` oder `ort_geschafft: true` enthält. Steht `flug_geschafft` gar nicht in der Antwort (Server ohne `20261120_ab_s_flug_abschluss_einmal.sql`, also heute live), gilt die Regel von 0.83.0 (`einheit_abgeschlossen` bzw. Flug-Test bestanden, nicht nach Nachtest). Das Test-Ergebnis selbst (Liste, „Flug geschafft!“-Zeile, Knöpfe) ist unverändert. Die App ist damit vor und nach dem Einspielen der Migration richtig – sie kann also vor der Migration live gehen.

**Getestet** (Playwright mit Chrome): **lernen 127 von 127** – neu 3 (Teil 8 Karte bei 400/820/1280 mit Wirkung, Farbe, Lage und zugeklappten Zeilen; Themengebiet + Rückfall + ⓘ; Nachtrag B mit `flug_geschafft` true/false, `ort_geschafft`, alter Server), angepasst 4 (LA-4, LB-1/LB-5, Teil 5 S4: neue Knopf-Texte und Karte; Teil 6 N5 entfällt). Alle Tests: 268 bestanden, 1 übersprungen, 10 Fehler – alle im Reise-Bereich: die 9 bekannten (PWA-Hülle, „Lernen Schule: Startkarte“, W80 ×4, Review301, „Woanders gebucht“, W88) und neu **W175 „Reiseplan-Kopf“** – hängt am Datum („Tag 11 von 110“, seit heute 21.11. Tag 12) und schlägt ohne meine Änderungen genauso fehl.

**Nicht geprüft:** echte Geräte und Safari, Bildschirmleser, gegen den echten Server (`flug_geschafft` nur nach der Feldbeschreibung von bau-lehrer nachgebildet).

FERTIG: LB Teil 8
FERTIG: 0.83.1

## 2026-11-20 – FERTIG: flug_geschafft (Nachträge 20.11. nachmittags, Teil A)

Stand `lernen-app` e8450e0 übernommen. Nur Dateien – nichts ausgeführt, kein App-Code, kein Merge. pglast ok.
**Migration** `supabase/migrations/20261120_ab_s_flug_abschluss_einmal.sql` (weiter nicht eingespielt): `flug_geschafft` = dieser Aufruf schließt die Sitzung ab **und der Flug wird dadurch zum ersten Mal fertig** – über den Flug-Test (`blocktest`) **oder** über Verbessern (`korrektur`). Geprüft wird
- vorher nicht fertig (Stand der Pflicht-Etappen beim Betreten des Aufrufs, bevor die Ergebnisse gebucht werden) und
- keine frühere abgeschlossene Flug-Test- oder Verbessern-Sitzung dieses Flugs mit `flug_geschafft` true oder unbekannt (`null`, vor dem Einspielen).
Weiter false: nicht bestandener Test, zweites Verbessern, Nachtragstest, Nachtest, Sitzungen vor dem Einspielen. Erneuter Aufruf derselben Sitzung: dasselbe wie beim ersten Mal (Wert ist gespeichert). Die Abschluss-Felder kommen weiter nur bei `flug_geschafft` oder `ort_geschafft`.
**Rauchtest** `ab_s_abschluss_rauchtest.sql`: **9c** neu – Verbessern macht den Flug erstmals fertig → `flug_geschafft` true mit `flug`, `etappen`, `sterne_flug`, `naechster_flug`; erneuter Aufruf gleich. **9c-2** neu – zweites Verbessern (eine Etappe wieder „fehler“) → false, keine Felder. 9a/9b (nicht bestanden, erneuter Aufruf) und 9d (Nachtragstest) unverändert false.
**Grenzfall (Annahme):** Eine Sitzung von vor dem Einspielen zählt als „Ausgang unbekannt“ und verhindert die Ansicht für diesen Flug – außer sie wurde inzwischen erneut gelesen (dann steht dort false). Lieber einmal keine Ansicht als eine doppelte.

## 2026-11-20 – FERTIG: AB-A und LB Teil 6 (dazu LB Teil 7) – App 0.83.0, Cache v150

Stand `lernen-app` 1cc6edc übernommen (Zweig `bau-motivation`). Nur App (`lernen.js`, `style.css`, `sw.js`) und Tests. Nichts in der Datenbank, keine Kinderdaten, keine Schlüssel, kein Merge nach `main`.

**AB-A:** war beim Holen schon in `lernen-app` (Commit 9cea758, App 0.83.0, Cache v149, Meldung „FERTIG: AB-A“ weiter unten; gebaut über `bau-lehrer`). Nicht noch einmal gebaut. Die Version bleibt **0.83.0** (noch nicht live), Teil 6 und Teil 7 kommen dazu, Cache **v149 → v150**.

**LB Teil 6 (Nachprüfung 4)**
- **N1 (Muss) „Nach Themengebiet“:** Unter 1100 px steht die Stufe (bzw. „+“) unter dem Titel, die Zeilen haben feste Plätze (Griff/Häkchen · Klassen-Kasten · Titel), damit auch das Auswählen die Zeile nicht auseinanderzieht. **Messung mit dem Skript des Gestalters (`n4/n4.test.cjs`, echte Themenliste):** gebrochene Wörter in allen 8 Gebieten – vorher 400: 2, 820: 16, 1280: 0 → **jetzt 0 / 0 / 0**; „Nach Klasse“ weiter 0 in allen 17 Klassen. Hinweis zum Skript: Es rechnet die Wurzel als `../../..` von `n4/` aus und findet so `tests/lernen.test.cjs` nicht (läuft nur, wenn es zwei Ebenen tiefer liegt) – ich habe es dafür in einen Hilfsordner kopiert, nicht geändert.
- **N2 (Sollte) Plan links:** Titel unter 1100 px bis zu zwei Zeilen (14 px, Silbentrennung `hyphens: auto`, Sprache `de`), erst danach „…“. Gekürzte Titel: 400 px **31 → 12** von 36, 820 px **28 → 3** von 36 (die übrigen brauchen mehr als zwei Zeilen). Die Schrift ist dafür 1 px kleiner, damit E-2 („12 Orte auf einem Tablet, Zeile ≤ 72 px“) weiter erfüllt ist. Lange Wörter werden jetzt mit Trennstrich umbrochen („Gleichungs-systeme“) statt abgeschnitten – bitte ansehen.
- **N3 (Sollte) Zähler:** Jeder Abschnitt zählt nur die Flüge seiner Stufe, im ganzen Plan – dieselbe Zahl wie im Kopf, nach dem Muster der Vorgabe („16 Orte · 20 Flüge in Wiederholung“); mit den Testdaten des Gestalters z. B. „1 Ort · 1 Flug gerade dran“, „5 Orte · 9 Flüge kommen noch“ bei Kopf „1 ▶ · 9 ○“. Für ◉: „… Flüge komplett gekonnt“. Liegt ein Flug dieser Stufe in einem Ort weiter oben (z. B. ein ↻-Flug in einem ▶-Ort), steht „(davon n in Orten weiter oben)“ dabei.
- **N4 (Kann):** eingeplante Zeilen in „Nach Themengebiet“ nicht mehr blass (Deckkraft 1, gleiche Titelfarbe wie die übrigen).
- **N5 (Kann):** Etappen-Liste: Stand („offen“, „gelandet“ …) rechtsbündig in der ersten Titelzeile, ohne „·“.
- **Punkt 6:** „↶ Rückgängig“ gilt nur für den jüngsten Schritt (war schon mit 9cea758 so; jetzt mit Test: nach einem Rückgängig kein zweiter Schritt zurück; lehnt der Server ab, steht „Rückgängig geht nur für die letzte Änderung. Inzwischen wurde etwas anderes geändert.“ mit „Neu laden“). **Rückfall:** `hinweis: 'rueckfall'` zeigt bei ◉ „gesetzt · Rückfall: n Etappen wieder offen“ (bzw. „alle Etappen sicher · Rückfall: …“), rot hervorgehoben – überall, wo die Stufe steht (Plan links, „Nach Klasse“, Themengebiet aufgeklappt). **heute_bis:** neu `lernHeuteTag(kind)` = Tag des Kindes vom Server, solange `heute_bis` nicht vorbei ist, sonst Kalendertag des Geräts; genutzt für „Knobeln des Tages“ (vorher UTC-Datum!) und die „Wiederholungsrunde heute“ (vorher Gerätedatum); der Tageszähler nutzte es schon (9cea758). Nicht umgestellt: Eltern-Seiten (Pausen, „seit … Tagen“) – dort gilt der Tag der Eltern bzw. die Pausenregel „Ortszeit des Kindes“ rechnet schon der Server; ein `heute_bis` je Kind liefert dort keine Aktion.

**LB Teil 7 (Info-Seite, `info-seite-update.md` Punkte 1–7)** – wörtlich übernommen, mit diesen Abweichungen (bitte prüfen):
- Punkt 1: „alle Flüge eines **Themen**gebiets“ statt „eines Gebiets“; Punkt 7: „in welchem Jahr ein **Flug** dran ist“ statt „ein Thema“ – sonst bricht der Test „Reisewörter auf allen Eltern-/Lehrerseiten“ (verboten: „Gebiet“, „Thema“).
- Punkt 3 steht direkt hinter dem Satz mit den Knöpfen („… bei ◉ zusätzlich ‚Wieder in die Wiederholung‘.“), nicht mitten in der Klammer – sonst zerreißt der Satz.
- Punkt 4: Knopftext „Weiter: Flug-Test“ statt „Jetzt zum Test ›“ – mit AB-A heißt der Knopf auf dem Landebildschirm so („Jetzt zum Test ›“ steht nur noch in der Flug-Übersicht).
- „Lernstand:“ und „Was wackelt?:“ gelöscht.
- **Neuer Eintrag (Punkt 8 / AB-A) in „Wie wird gelernt?“, hinter „Etappe gelandet“:**
  > **Abschluss einer Etappe:** Nach der Landung (und der Knobel-Bordkarte) zeigt die App eine von drei Fassungen – jede mit eigenem Bild und eigener Farbe: Direktflug (alle Bordkarten im ersten Versuch richtig, ohne Tipp, genau so viele wie nötig), Saubere Landung (höchstens 2 endgültige Fehler, Stufe nie leichter geworden, höchstens 4 Bordkarten mehr als nötig; nach „wieder offen“ heißt sie „Wieder gelandet“) oder Sturmflug gemeistert (alles darüber; ohne Fehlerzahl, die Knobel-Bordkarte kommt dann nicht von selbst, nur als Textlink). Dazu ein Abzeichen – ⚡ Direkt, ✓ Sauber oder ⚡ Ausdauer –, das im Reisepass gezählt wird, der Satz „Du kannst jetzt …“ und genau ein Knopf zum nächsten Schritt (nächste Etappe, Flug-Test oder Abflugtafel); zurück in die Übungen derselben Etappe führt von dort kein Weg. Nach dem bestandenen Flug-Test: „Flug geschafft“ mit den Sternen des Flugs und der Liste „Das kannst du jetzt“, danach eine Bordkarte zum nächsten Flug im Plan („Boarding“ öffnet seine erste Erklärung). Mit dem letzten Flug eines Orts kommt dazwischen der Reisepass-Stempel. Landungen vor dieser Version haben kein Abzeichen.
- Punkt 3 beschreibt den Stand nach der LB-3-Nachbesserung am Server (noch nicht eingespielt).

**Getestet** (Playwright mit Chrome, lokal): **lernen 125 von 125** (neu 7: N1 als Messung 400/820/1280 × 8 Gebiete + N4, N2, N3, N5, Rückgängig nur jüngster Schritt mit Ablehnung, Rückfall + heute_bis, Info-Seite Teil 7; angepasst 4: Abschnittstexte in LB-5/LA-5/LB Teil 5 S2, Etappen-Format S4, „Teil 4 Punkt 1+2“ misst links jetzt „höchstens zwei Zeilen, nichts seitlich abgeschnitten“ statt „kein getrenntes Wort“). Alle Tests: 267 bestanden, 1 übersprungen, 9 Fehler – dieselben 9 wie vor meinen Änderungen auf demselben Stand (PWA-Hülle, „Lernen Schule: Startkarte“, W80 ×4, Review301, „Woanders gebucht“, W88; Reise-Bereich, nicht Lernen).

**Nicht geprüft:** echte Geräte und Safari (Silbentrennung auf dem iPad), Bildschirmleser, gegen den echten Server (Rückfall-Hinweis und `heute_bis` kommen erst mit der LB-3-Nachbesserung).

FERTIG: AB-A und LB Teil 6
FERTIG: LB Teil 7

## 2026-11-20 – FERTIG: LB-3 Tests ergänzt (Nachträge aus ChatGPT 885, an bau-lehrer)

Stand `lernen-app` 6e04b10 übernommen. Nur Server-Tests und eine Migration als Datei – kein App-Code, **nichts in der Datenbank ausgeführt** (Live-Text nur gelesen, Einfügestellen je genau einmal vorhanden), kein Merge. pglast für alle Dateien ok; die Rauchtests selbst sind **nicht ausgeführt** – bitte im Probelauf.

1. **`lb3_nachbesserung_rauchtest.sql`, neuer Fall „M2-echt“:** gesetzter Flug; das Testkind erarbeitet eine Etappe wirklich über `uebung_pruefen_intern` (verschiedene Auswahl-Bordkarten, richtig im ersten Anlauf: zuerst eine schwere, dann je Typ eine, dann weitere – bis `karte_landet` erfüllt ist: Ziel-Anzahl, Typen, schwere, Folge). Keine Nachweisfelder von Hand. Danach Rücknahme → diese Etappe bleibt gelandet (Herkunft selbst, eigene Lösungen ≥ Ziel), alle anderen Etappen des Flugs offen. Flug/Etappe werden dynamisch gewählt (nur Auswahl-Bordkarten, vom Testkind ungeübt; live 304 passende Etappen).
2. **`i4_misch_ausgabe_rauchtest.sql`:** 1b – zweimal derselbe Flug → dieselben Karten, beide `misch_gueltig`; neu **4b** – Flugwechsel → Ausgaben des anderen Flugs verfallen; zurückgewechselt → neu ausgegeben (Ausgabezeit jetzt) und gültig; ein weiteres Mal zurück; älter als 24 h → verfallen.
3. **`ab_s_abschluss_rauchtest.sql`, Befund und Migration:**
   - **Befund (Live-Text gelesen):** `test_abschliessen_intern` hängt `schule.flug_abschluss(...)` an **jede** Antwort an. Bei nicht bestandenem Flug-Test, bei Verbessern, beim Nachtragstest, beim Nachtest und beim erneuten Aufruf kommen also `flug`, `etappen`, `kurz`, `sterne_flug` (Test-Sterne dieser Sitzung und Summe des Flugs), `naechster_flug`, `ort_wechsel`, `ort_fluege` mit; `ort_geschafft` ist dort false (festgehalten). `einheit_abgeschlossen` ist der **Stand** des Flugs (auch beim erneuten Aufruf und nach Nachtests true), kein Ereignis.
   - **Migration** `supabase/migrations/20261120_ab_s_flug_abschluss_einmal.sql` (nicht ausgeführt): neue Spalte `testsitzung.flug_geschafft`, einmal festgehalten, wenn **dieser Aufruf** die Sitzung abschließt, es der **erste** abgeschlossene Flug-Test (`blocktest`) des Flugs ist und der Flug damit fertig ist. Verbessern, Nachtragstest (späterer `blocktest`), Nachtest, vor dem Einspielen abgeschlossene Sitzungen: false. Antwort: immer `flug_geschafft`; die Abschluss-Felder nur bei `flug_geschafft` oder `ort_geschafft` – auch beim erneuten Aufruf derselben Sitzung (gleiches Ergebnis für „Test ansehen“).
   - **Rauchtest:** 6 und 7 prüfen zusätzlich `flug_geschafft` und dass die Felder beim ersten Abschluss da sind; neu **9a** nicht bestandener Flug-Test, **9b** erneuter Aufruf, **9c** Verbessern (Flug danach fertig), **9d** Nachtragstest – jeweils `flug_geschafft` false und keine Felder `flug`, `naechster_flug`, `sterne_flug` (9a auch `etappen`, `ort_wechsel`). Startet Verbessern oder Nachtragstest mit dem gewählten Flug nicht, meldet der Test „Info“ statt abzubrechen.
   - **Für die App (bau-motivation, kein App-Code von mir):** die Abschluss-Ansicht des Flugs an `flug_geschafft` (oder `ort_geschafft`) hängen statt an `einheit_abgeschlossen`; die App 0.83.0 zeigt sie heute bei „Flug fertig und kein Nachtest“ (also auch nach Verbessern).
   - **Annahme:** „Verbessern“, das einen Flug erstmals fertig macht, zeigt keine Abschluss-Ansicht (so steht es in den Nachträgen: „nicht Verbessern/Nachtragstest“). Soll das Kind dann doch „Flug geschafft“ sehen, genügt in der Migration `t.art in ('blocktest', 'korrektur')` und „kein früherer Abschluss“ – bitte entscheiden.

## 2026-11-20 – FERTIG: lb3-Rauchtest

Anlass: `antworten.md`, „20.11. 13:25“ – `supabase/tests/lb3_rauchtest.sql` brach nach der LB-3 Nachbesserung mit „Inzwischen wurde etwas anderes geändert.“ ab (Prüfung 6 machte den Sammelschritt rückgängig, nachdem Prüfung 5 schon einen neueren Plan-Schritt angelegt hatte; neue Regel Sollte 4).
**Nur die Testdatei geändert** (Stand `lernen-app` f1a0ad7 übernommen; kein App-Code, nichts in der Datenbank, kein Merge):
- Prüfung **6** (Rückgängig des Sammelschritts) läuft jetzt direkt nach Prüfung 4 – der Sammelschritt ist dann noch der jüngste Plan-Schritt (Prüfungen 2–4 legen keinen Plan-Schritt an). Prüfungen und Erwartungen von 6 unverändert (6c prüft weiter, dass die selbst gelandete Etappe mit Wiederholungsstufe 2 zurückkommt).
- Prüfung **5** (Rücknahme eines Flugs) danach: zuerst werden die 6 Flüge wieder gesetzt, dann wird einer zurückgenommen – gleiche Erwartung (keine gesetzte Landung, Stufe ○).
- Prüfungen 1–4 und 7–10 unverändert; die Meldungen „ok n“ erscheinen in der Reihenfolge 1, 2, 3, 4, 6, 5, 7, 8, 9, 10.
**Geprüft:** pglast ok. **Nicht ausgeführt** (Datenbank nur lesen) – bitte im nächsten Probelauf mit der Migration `lb3_nachbesserung`.

## 2026-11-20 – FERTIG: AB-A (App 0.83.0, Cache v149)

Gebaut im Zweig `bau-lehrer` auf `lernen-app` e71a72d (App 0.82.2) – ich war der einzige Chat am App-Code. Datenbank nur gelesen (für AB-A nichts). Kein Merge nach `main`, keine Kinderdaten.
Vorgabe: `inhalte/pruefung/kind/abschluss/umsetzung.md`, `entwurf/abschluss.html`, Zusätze von Sebastian in `AUFTRAEGE.md`. Server-Felder: AB-S (Meldung unten).
Bilder: `docs/previews/ab/` – Etappe `direkt`/`sauber`/`sturm` × `tag`/`nacht` (400 × 780) und Tablet 820, Flug geschafft (tag/nacht 400, tag 820), Ort geschafft, Bordkarte (gleicher Ort, Ortswechsel).

**Umgesetzt (nur Abflug-Gestaltung „tag“/„nacht“; die alte Gestaltung bleibt wie bisher)**
- **1 Etappe gelandet:** Vollbild über der Seite, drei Fassungen nach `landung.landung_art` (Ersatz `einheit_lesen.landungen`, sonst „sauber“ bei altem Server): Direktflug (Sonnenuntergang, Jet, Funken, „{ziel}/{ziel} AUF ANHIEB“, Abzeichen Direkt), Saubere Landung (Taghimmel, Landebahn, Chips Bordkarten · selbst gelöst · in Folge; bei `wieder_gelandet` „WIEDER GELANDET“), Sturmflug gemeistert (Gewitter, Durchbruch, Satz ohne Fehlerzahl mit „einmal/zweimal/mehrmals neu angesetzt“, Band „⚡ AUSDAUER-ABZEICHEN“). Blatt: „Du kannst jetzt“ (`kann` → „Kurz gesagt“ → Titel), ★ +Sterne, ein Satz zur Wiederholung, **ein** großer Knopf (Weiter: nächste Etappe · Weiter: Flug-Test „{k} Bordkarten, eine je Etappe, ohne Tipps“ · Zur Abflugtafel), Textlink „Pause – zur Abflugtafel“. Kein Weg zurück in die Übungen; die Adresse wird beim Landen durch `…-erklaeren` ersetzt (Zurück-Taste führt nicht in die Bordkarten).
- **Ablauf (Zusatz Sebastian):** Übungen → Knobel-Bordkarte von selbst → Abschluss-Ansicht. **Sturmflug:** Knobel kommt nicht von selbst, nur als kleiner Textlink im Blatt; danach wieder die Abschluss-Ansicht. Nach der letzten Pflicht-Etappe führt der Knopf zum Flug-Test.
- **2 Flug geschafft** (nach bestandenem Flug-Test bzw. vollständiger Korrektur, nicht nach Nachtests): Gold-Szene, Konfetti, je Etappe ein Licht, Sterne-Zähler (`sterne_flug.summe`) mit „Test r von g{, v verbessert}“, Liste „Das kannst du jetzt – n Etappen“, Wiederholungs-Kette, Knopf „Weiter zum nächsten Thema“, Textlink „Test ansehen“ (schließt die Ansicht; darunter die Antwortliste mit Teil 4/5f). „Überspringen ›“.
- **Bordkarte:** NEUES THEMA, ORT ✈ FLUG nr/von, Flugname, `kurz`, ETAPPEN · GEBIET · FLUG, Gate „ERKLÄRUNG“; „Boarding: {Titel}“ → `#/lerneinheit/{kind}-{einheit}-erklaeren-1` (Erklärung der ersten Etappe); „Später – zur Abflugtafel“. `naechster_flug: null` → „Alles geschafft, was im Plan steht …“ + „Zur Abflugtafel“. Alter Server ohne das Feld → Abflugtafel.
- **3 Ort geschafft** (`ort_geschafft`): Papier-Szene, Stempel „GESCHAFFT / ORT / Gebiet · Datum“, „REISEPASS · STEMPEL n“ (Konto neu geladen), „Alle k Flüge · ★ +100 Ort-Sterne“, „Deine Flüge in …“, Knopf „Weiter: neuer Ort“ → Bordkarte „NEUES THEMA · NEUER ORT“, „VON … ✈ NACH …“, „Abflug nach {Ort}“.
- **4 Bewegung:** nur CSS (+ Zähler), längste Bewegung 1,8 s (Funken und Konfetti gegenüber dem Entwurf verkürzt, damit 1,8 s eingehalten sind), Antippen der Szene beendet sie, bei „weniger Bewegung“ sofort Endzustand. Kein Ton.
- **Reisepass:** Zeile „⚡ Direkt n · ✓ Sauber n · ⚡ Ausdauer n“ aus `konto.abzeichen` (nur wenn der Server sie liefert).
- **H6 (LB-3 Nachbesserung, Sollte 6):** Der Tageszähler „heute selbst gelöst“ gilt bis `heute_bis` des Servers (unabhängig von Uhr und Zeitzone des Geräts); ohne `heute_bis` wie bisher.
- **Rückgängig (LB-3 Nachbesserung, Sollte 4):** Die App bietet nach einem Rückgängig keinen weiteren Schritt zurück an; lehnt der Server ab, steht dort „Rückgängig geht nur für die letzte Änderung …“ mit „Neu laden“.

**Getestet** (Playwright, Chromium; lernen 118 von 118; Suche 138 bestanden + Nr. 108 einzeln bestanden (bekannt wackelig), 9 bekannte alte Fehler 13, 15, 101, 103, 105, 111, 113, 126, 127; neu 6 Tests AB-A, angepasst 5 Tests aus Teil 4/5): drei Fassungen mit verschiedenen Szenen, je hell und nacht auf 400 × 780 ohne Scrollen, genau ein großer Knopf, kein Link in die Übungen, Adresse nach der Landung `…-erklaeren`; Sturmflug ohne Fehlerzahl und ohne Knobel von selbst, Knobel über den Textlink und zurück; Wieder gelandet; alter Server ohne `landung`; Reisepass-Zeile; Tablet 820; Bewegung ≤ 1,8 s, Antippen beendet, „weniger Bewegung“ ohne Animation; Flug → Bordkarte → Boarding öffnet `-erklaeren-1`; „Test ansehen“; Ort → Stempel → Bordkarte VON/NACH; ohne nächsten Flug.

**Nicht geprüft / offen**
- Gegen den echten Server nicht ausgeführt (AB-S-Felder nur nach der Feldbeschreibung nachgebildet).
- „Zurück-Taste führt zur Etappen-Übersicht“: umgesetzt als Ersetzen der Adresse durch `…-erklaeren`; die Taste selbst führt dann zur vorigen Seite (z. B. Abflugtafel), nie in die Bordkarten.
- Das Konfetti/Funken-Timing weicht leicht vom Entwurf ab (1,4 s bzw. 0,9 s statt 1,8 s/1,2 s), damit die Grenze von 1,8 s auch mit Verzögerung gilt.
- Echte Geräte, Safari und Bildschirmleser nicht geprüft.

## 2026-11-20 – FERTIG: LB-3 Nachbesserung (Server, Muss 1–3, Sollte 4–7)

Gebaut im Zweig `bau-lehrer` (Stand `lernen-app` e71a72d übernommen). Nur Migration und Rauchtests – kein `lernen.js`. **Nichts in der Datenbank ausgeführt**, nur gelesen: alle Einfügestellen im Live-Text geprüft (je genau einmal vorhanden). Kein Merge nach `main`.
**Bestand (lesend, 20.11.):** keine Route mit `kann_wdh_themen`, keine Karte mit `gesetzt_am`, 3 Plan-Schritte mit Karten-Lage → keine Bestandsänderung nötig.
**Migration** `supabase/migrations/20261120_lb3_nachbesserung.sql` (nach `lb3`, `i5`, `ab_s`; pglast ok; kein DROP/DELETE; wiederholt ausführbar).
**Rauchtest neu** `supabase/tests/lb3_nachbesserung_rauchtest.sql` (Rollback, nur Testkind, Flüge dynamisch aus dem Inhalt gewählt). **Angepasst:** `lb3_rauchtest.sql` (1c: selbst gelandete Etappe behält Landung/Herkunft, Wiederholung neu ab Stufe 1; 6c: Rückgängig stellt Stufe 2 wieder her), `i3_lernregeln_rauchtest.sql` (Sollte 7).
**Nicht ausgeführt** – weder Migration noch Rauchtests (Datenbank nur lesen). Bitte im Probelauf: Migration, dann `lb3_nachbesserung`, `lb3`, `i3`, `i2`, `i4`, `i5`, `ab_s`.

### Muss
1. **Setzen = alle Etappen ab Wiederholungsstufe 1.** `flug_wdh_setzen`: auch schon gelandete Etappen gehen auf Stufe 1, fällig am nächsten Lerntag; `sitzt_am`, eigene Lösungen, Belege bleiben, kein `gesetzt_am` (Herkunft selbst). Lage davor steht im Schritt (Rückgängig stellt sie her). Neu `karte_stand.wdh_gesetzt_am` (Beginn der Wiederholung durch Setzen, für Muss 3). Test M1: vorher ◉ → ↻ Wdh 1 von 5, am nächsten Lerntag fällig; Rückgängig → wieder ◉.
2. **Rücknahme/Rückgängig: nur belegte Landungen bleiben.** Gemeinsame Landeregel `schule.karte_landet(k)` (eigene Lösungen ≥ Ziel, Typen, schwere, Folge) – `karte_buchen` ruft sie jetzt auch auf. Damit sie für gesetzte Etappen etwas prüfen kann, zählt `karte_buchen` dort eigene Lösungen, Typen, schwere und Folge weiter (die Wiederholung läuft daneben unverändert). Rücknahme (`flug_wdh_zuruecknehmen`, auch beim Entfernen eines Ortes) und Rückgängig (`karten_wiederherstellen`): gesetzte Etappe bleibt nur bei `karte_landet`, sonst offen (`sitzt_am` null). Versuche, eigene Lösungen, Sterne bleiben. Tests: Fehler → offen; offener erster Anlauf → offen; eine richtige Wiederholung → offen mit 1 eigener Lösung; eigene Landung → bleibt (Herkunft selbst); dasselbe über Rückgängig (Setzen → Fehler → Rückgängig → offen).
3. **sicher nach dem Flug.** `karte_sicher`: steht der Flug auf „Kann er – aber wiederholen“ (oder ist die Etappe gesetzt), gilt für alle Etappen: gelandet + Wiederholung nach 14 Lerntagen + Mischkarte richtig, falls seit dem Setzen (`wdh_gesetzt_am`) eine **eingelöst oder beantwortet** wurde; nur vorgeladen zählt nicht. Test M3: selbst gelandete Etappe ohne Nachtest + gesetzte, Wiederholungen bestanden → alle sicher, Flug ◉; vorgeladen → bleibt sicher; eingelöst ohne richtige → ↻, mit richtiger → ◉.

### Sollte
4. `plan_setzen_intern`: `rueckgaengig` nur für den jüngsten Plan-Schritt (`route_aenderung`, anlass `plan`) des Kindes, sonst „Inzwischen wurde etwas anderes geändert.“ Test: A → B → A rückgängig abgelehnt, B rückgängig angenommen. **Folge für die App:** ein zweites „↶ Rückgängig“ hintereinander wird abgelehnt – die App bietet nur noch einen Schritt an (in AB-A, 0.83.0).
5. `thema_stufe`: „komplett“ gesetzt + wieder offene Etappe → Stufe ◉ bleibt, `hinweis: 'rueckfall'`, `wieder_offen` > 0.
6. `schule.heute_bis(kind)` = nächster Tagesbeginn in der Zeitzone des Kindes; `einheit_lesen_intern` und `uebung_pruefen_intern` liefern `heute_bis` neben `heute_tag`.
7. `i3_lernregeln_rauchtest.sql`: Ursache – der eindeutige Index `misch_ausgabe_offen_eindeutig` gilt für alle nicht eingelösten Ausgaben, **auch verfallene**; hat `mischkarten` im Test eine Ausgabe derselben Bordkarte angelegt und verfallen lassen, stieß das Einfügen von Hand darauf. Jetzt fügen beide Stellen mit `on conflict … do update` ein (wie `mischkarten` selbst); die Prüfung „zweite offene Ausgabe wird abgelehnt“ bleibt.

### Annahmen / nicht geprüft
- „Seit dem Setzen“ für Muss 3 = `wdh_gesetzt_am` (neu); für ältere gesetzte Karten ohne diesen Wert gilt `gesetzt_am`, sonst `sitzt_am`.
- „gezeigt“ einer Mischkarte = beantwortet (Versuch mit `misch`); eine Anzeige ohne Antwort speichert der Server nicht.
- Muss 2 „echte eigene Landung“ im Test über gesetzte Zähler (eigene Lösungen = Ziel, Typen, schwer, Folge 3) statt vieler Antworten.
- Nichts davon ausgeführt.

## 2026-11-20 – FERTIG: AB-S (Server: Abschluss nach Etappe, Flug und Ort)

Stand `lernen-app` 10a3155 in `bau-motivation` zusammengeführt. Nur Migration und Rauchtest – kein `lernen.js`, keine neue App-Version. Datenbank nur gelesen (alle Einfügestellen im Live-Text je einmal vorhanden;
`karte_buchen` lokal bytegleich nachgebaut, md5 = live). Kein Merge nach `main`.
**Migration** `supabase/migrations/20261120_ab_s_abschluss.sql` (nach `i4` und `i5`, von beiden unabhängig; nicht ausgeführt; pglast ok; kein DROP, kein DELETE, keine Bestandsänderung; wiederholt ausführbar).
**Rauchtest** `supabase/tests/ab_s_abschluss_rauchtest.sql` (Rollback, nur Testkind; über `uebung_pruefen_intern`, `test_starten_intern`, `test_abschliessen_intern`, `einheit_lesen_intern`, `konto`).

### Neu in der Datenbank
- `karte_stand.landung_art` (`direkt` | `sauber` | `sturm`, Check) und `karte_stand.landung` (jsonb, Zählung) – gesetzt in `karte_buchen` genau beim Landen (neue Funktion `schule.landung_speichern`), bei „wieder gelandet“ überschrieben.
  Gesetzte Landungen (LB-3) laufen nicht über `karte_buchen` → bekommen keine Art.
- `schule.landung_zaehlen(kind, flug, lernziel)` – nur lesen. Gezählt seit Beginn bzw. seit dem letzten „wieder offen“ (`geoeffnet_am`) bis `sitzt_am`; nur `pool = 'uebung'` dieser Etappe, ohne Mischkarten, Knobel, Expedition, Test.
- Schwellen in `schule.regel`: `landung_sauber_fehler_max` 2 · `landung_sauber_mehr_max` 4 · `landung_sauber_stufe_gesenkt_max` 0 · `landung_sauber_lerntage_max` **null (aus)** – siehe Offene Punkte.
- `testsitzung.ort_geschafft` (beim Abschluss festgehalten, damit „Test ansehen“ später dasselbe zeigt).
- Ablage für AB-I: `thema.kurz` und Tabelle `schule.etappe_text(thema_id, lernziel, kann, geaendert_am)`, PK (thema_id, lernziel), RLS an (wie alle `schule`-Tabellen, ohne Policy).
- Hilfsfunktionen: `schule.flug_im_ort`, `schule.flug_karte`, `schule.naechster_flug`, `schule.flug_abschluss`.

### Regel für `landung_art` (wie umgesetzt)
| Art | Bedingung |
|---|---|
| `direkt` | `bordkarten <= ziel`, `fehler_endgueltig = 0`, `mit_tipp = 0`, `zweite_versuche = 0` |
| `sauber` | sonst `fehler_endgueltig <= 2`, `stufe_gesenkt <= 0`, `bordkarten <= ziel + 4` (und Lerntage, falls die Regel gesetzt wird) – **oder** `wieder_gelandet` (Szene 1b) |
| `sturm` | alles andere |
Zählweise: `bordkarten` = Antworten ohne 2. Anlauf (je Bordkarte eine) · `fehler_endgueltig` = Wertung `falsch` (ein 1. Anlauf, nach dem der 2. Anlauf kommt, zählt nicht) · `mit_tipp` = Antworten ohne 2. Anlauf mit `hilfe > 0` ·
`zweite_versuche` = Antworten mit `anlauf = 2` · `stufe_gesenkt` = aus den Versuchen nachgerechnet wie in `karte_buchen` (jeder 2. Fehler in Folge, höchstens bis Stufe 2; im Zählfenster ab 0) · `lerntage` = verschiedene Tage (Zeitzone des Kindes) mit Versuchen im Zählfenster.

### Für AB-A (App): Felder
**1. Antwort auf eine Übung** (`schule_uebung_pruefen`) – neues Feld **`landung`** auf oberster Ebene, **nur** in der Antwort, mit der die Etappe gerade landet (nicht bei Wiederholung, Mischkarte, Knobel, nicht bei erneutem Senden derselben `client_id`):
```
landung: { landung_art: 'direkt'|'sauber'|'sturm', bordkarten: n, ziel: n, fehler_endgueltig: n, mit_tipp: n, zweite_versuche: n,
           stufe_gesenkt: n, lerntage: n, wieder_gelandet: bool, eigene_loesungen: n, folge_ziel: n, am: zeit, kann?: text }
```
- Direktflug: „{ziel}/{ziel} AUF ANHIEB“ · Saubere Landung: Chips `bordkarten` · `eigene_loesungen` selbst gelöst · `folge_ziel` in Folge; `wieder_gelandet` → Titel „WIEDER GELANDET“ ·
  Sturmflug: `bordkarten`, `stufe_gesenkt` (1 einmal · 2 zweimal · ≥3 mehrmals · 0 Einschub weglassen), `folge_ziel` – keine Fehlerzahl zeigen.
- `kann` fehlt, solange kein Text da ist (jsonb_strip_nulls der Antwort) → „Kurz gesagt“ bzw. Etappen-Titel.
- Die bisherigen Felder (`karte.neu_sitzt` usw.) bleiben; `landung` ist da, genau wenn `karte.neu_sitzt` aus einer eigenen Landung kommt.
**2. Reisepass** (`schule_konto`): `konto.abzeichen = { direkt: n, sauber: n, sturm: n }` (je Kind und Etappe die letzte Art).
**3. Flug lesen** (`schule_einheit_lesen`): `kurz: text|null` · `kann: { <lernziel>: text|null }` (alle Etappen aus `inhalt.etappen`) · `landungen: { <lernziel>: 'direkt'|'sauber'|'sturm' }` (nur Etappen mit gespeicherter Art; Ersatz, falls die Lande-Antwort fehlt).
**4. Test-Ergebnis** (`schule_test_abschliessen`, auch erneutes Lesen) – zusätzlich auf oberster Ebene; alle bisherigen Felder unverändert:
```
sterne_flug:   { test: n, summe: n }     test = Sterne dieses Tests; summe = Übungs-, Knobel- und Test-Sterne aller Versionen dieses Flugs (ohne Expedition, ohne Ort-Sterne)
kurz:          text|null                 Satz zum Flug
flug:          Bordkarte (s. u.) des gerade geschafften Flugs
etappen:       [{ lernziel, titel, kann: text|null }]   Reihenfolge wie inhalt.etappen – Liste „Das kannst du jetzt“, je Etappe ein Licht
ort_geschafft: bool                      Ort durch DIESEN Abschluss geschafft (war vorher nicht fertig) → Ort-Bildschirm
ort_sterne:    n                         gebuchte Ort-Sterne (100), sonst 0
ort_fluege:    [{ thema_id, titel, zustand }]           Flüge des Orts ohne abgewählte – „Deine Flüge in {Ort}“
naechster_flug: Bordkarte | null         nächster Flug laut Plan; null → „Alles geschafft, was im Plan steht …“
ort_wechsel:   bool | null               nächster Flug in anderem Ort → „VON … NACH …“, Knopf „Abflug nach {Ort}“
Bordkarte = { thema_id, einheit_id, titel, gebiet, kurz, block_id, ort, land, flug: { nr, von }, etappen: n, erste_etappe: { lernziel, titel } }
```
- „Boarding“ → `naechster_flug.einheit_id` + `erste_etappe.lernziel` (Erklärung der ersten Etappe).
- Plan-Reihenfolge für `naechster_flug`: Orte nach `position`, Flüge nach `block_thema.reihenfolge`; übersprungen: abgewählt, „kann schon“ (Flug oder Ort), „kann er – aber wiederholen“, ohne geprüften Flug, erledigt, der gerade geschaffte Flug; Orte `fertig`/`entfernt` zählen nicht.
- Stempel-Nummer „REISEPASS · STEMPEL {n}“ = `konto.stempel` nach dem Abschluss (Konto neu laden). „{v} verbessert“ bleibt App-Sache (wie im Entwurf).
**Alte App:** bekommt nur zusätzliche Felder; nichts entfernt oder umbenannt.

### Rauchtest `ab_s_abschluss_rauchtest.sql`
1 Direktflug (genau `ziel` Bordkarten; `landung` nur in der Lande-Antwort; gespeichert) · 2 Saubere Landung (1 Fehler, 1 Tipp, 1 zweiter Versuch) · 3 Sturmflug (3 Fehler, Stufe 1× gesenkt), Reisepass je +1 ·
4 wieder gelandet → `sauber`, nur Bordkarten seit dem Öffnen gezählt, Art überschrieben · 5 `einheit_lesen`: `kurz`, `kann` (fehlend = null), `landungen` ·
6 Flug-Test im eigenen Plan: `sterne_flug`, Ort geschafft (+100), `ort_fluege`, nächster Flug in anderem Ort, Flug 1 von 1 · 7 erneut gelesen: `ort_geschafft` bleibt, alte Felder da · 8 ohne weiteren Flug im Plan → `naechster_flug` null.
Hinweise für den Probelauf: Schritt 4 schiebt im Test `versuch.am` der Etappe zurück (in einer Transaktion ist `now()` fest). Etappen-Auswahl: nur Auswahl-Bordkarten (heute 6 Etappen passend, alle vom Testkind ungeübt).

### Bestand
43 gelandete Etappen (heute) bekommen **keine** nachträgliche Art (nichts erfunden); der Reisepass zählt ab dem Einspielen. Sitzungen, die vor dem Einspielen abgeschlossen wurden: `ort_geschafft` wird beim ersten Lesen festgehalten (dann meist `false`, weil der Ort schon fertig ist).

### Offene Punkte (bitte entscheiden)
1. **Widerspruch in `umsetzung.md`:** Tabelle 1c nennt „über mehrere Lerntage“ als Grund für Sturmflug, die Bedingungstabelle und die Freigabe (Abschnitt 7) nennen es nicht. Umgesetzt nach Freigabe: Lerntage zählen **nicht**
   (`landung_sauber_lerntage_max = null`). Soll „mehr als 1 Lerntag → Sturmflug“ gelten, genügt `update schule.regel set wert = '1' where schluessel = 'landung_sauber_lerntage_max'`.
2. „Wieder gelandet“ zählt im Reisepass als **Sauber**-Abzeichen (Szene 1b, `landung_art = 'sauber'`) und ersetzt die Art der ersten Landung derselben Etappe.
3. Direktflug mit `bordkarten <= ziel` statt `== ziel` (weniger als `ziel` ist praktisch unmöglich; so fällt kein Sonderfall in „Sturm“).
4. `ort_geschafft` setzt einen Plan-Eintrag des Orts voraus (ohne Route keine Ort-Sterne, also `false`).

### Gesehen/getestet
Lokale Nachbildung (PostgreSQL 16): Tabellen und Funktionen des Lande-, Test- und Misch-Pfads aus dem Live-Text abgeschrieben, Inhalte erfunden, `test_starten_intern` als vereinfachter Stub.
Migrationen `i4`, `i5`, `ab_s` je **zweimal** eingespielt ohne Fehler; Rauchtests **`i4` (5/5), `i5` (4/4), `ab_s` (8/8)** ohne Fehler. Dabei einen Fehler gefunden und behoben (Alias `r` kollidierte in `test_abschliessen_intern` mit einer Variablen).
**Nicht geprüft:** gegen die echte Datenbank nicht ausgeführt (Probelauf beim Haupt-Chat); echtes `test_starten_intern` nur gelesen; Laufzeit von `naechster_flug` (ruft `thema_stand` je Flug im Plan) nicht gemessen.

## 2026-11-20 – FERTIG: `thema_stufe` sieht den offenen Nachtragstest (Befund 20.11. 06:00)

**Migration** `supabase/migrations/20261120_i5_stufe_nachtragstest.sql` (nach `lb3`; Ersetzung im Live-Text, Stelle einmal vorhanden; wiederholt ausführbar; pglast ok). **Rauchtest** `supabase/tests/i5_stufe_nachtragstest_rauchtest.sql`.
- „Alle Etappen gelandet, aber Flug-Test noch nicht geschrieben“ gilt jetzt auch, wenn der Flug-Test geschrieben ist und eine Pflicht-Etappe in `lernziel_stand` noch `offen` steht – genau die Bedingung, unter der `test_starten_intern` seit W177 den Nachtragstest startet.
  Ergebnis im Fall aus dem Betrieb: `▶ dran`, `test_offen: true` (vorher `↻`, `false`). Gesetzte Flüge (LB-3) wie bisher ausgenommen. Ist die offene Etappe noch nicht gelandet: `▶` über „begonnen“, `test_offen: false`.
- Rauchtest: alles nachgewiesen → ↻ · offene gelandete Pflicht-Etappe → ▶, test_offen · Nachtragstest startbar · offene Etappe nicht gelandet → ▶ ohne test_offen. Lokal 4/4 (s. AB-S).

## 2026-11-20 – Nachtrag zu „Misch-Ausgaben wiederverwenden“
Unverändert gegenüber der Meldung darunter (Commit 78ca3c7, jetzt mit `lernen-app` 10a3155 zusammengeführt). Neu: Migration und `i4_misch_ausgabe_rauchtest.sql` in der lokalen Nachbildung ausgeführt – 5/5 ohne Fehler.
Reihenfolge zum Einspielen: `i4` → `i5` → `ab_s`.

## 2026-11-20 – FERTIG: Misch-Ausgaben wiederverwenden (Befund 20.11. 05:55)

Stand `lernen-app` c750ad2 übernommen. Nur Migration und Rauchtest – kein `lernen.js`, keine neue App-Version. Datenbank nur gelesen (I-3 eingespielt, `misch_ausgabe` hat 8 Zeilen; Ersetzungsstelle in `misch_buchen` einmal vorhanden). Kein Merge.
**Migration** `supabase/migrations/20261120_i4_misch_ausgabe_wieder.sql` (nach I-3; nicht ausgeführt; pglast ok; kein DROP, kein DELETE, keine Bestandsänderung; wiederholt ausführbar):
- neue Spalte `misch_ausgabe.verfallen_am`.
- `schule.mischkarten(kind, flug, anzahl)`: 1. offene Ausgaben dieses Kindes für einen **anderen Flug**, **älter als 24 Stunden** oder **nicht mehr gültig** (Etappe nicht mehr gelandet, Bordkarte gesperrt, Flug nicht mehr geprüft/freigegeben) → `verfallen_am = now()` (nicht löschen);
  2. die noch offenen Ausgaben **für diesen Flug** werden wieder ausgegeben (dieselben Karten, je Etappe höchstens eine, älteste zuerst); 3. **aufgefüllt** wird nur, wenn weniger als gewünscht offen sind, und nur aus Etappen ohne offene Karte
  (Auswahl wie bisher über `mischkarten_waehlen`; eine verfallene Ausgabe derselben Bordkarte wird dabei wiederbelebt statt eine zweite Zeile anzulegen – der eindeutige Index bleibt). Antwort im bisherigen Format (`einheit_id`, `quelle`, `stadt`, `etappe`), sortiert Flug → Kontinent → älter.
- `misch_gueltig` und `misch_buchen` zählen verfallene Ausgaben nicht.
**Rauchtests**
- neu `supabase/tests/i4_misch_ausgabe_rauchtest.sql` (Rollback, nur Testkind, eigene zwei gelandete Etappen, alle anderen im Test „nicht gelandet“): zweimal gelesen → dieselben Karten, keine neuen Ausgaben · eine eingelöst → die andere bleibt, nur die fehlende Etappe wird aufgefüllt ·
  anderer Flug → alte Ausgaben verfallen, offene = ausgelieferte · älter als 24 h → verfällt, neu ausgestellt · Etappe nicht mehr gelandet → Ausgabe verfällt, keine Karte mehr daraus.
- angepasst `i3_lernregeln_rauchtest.sql`: **S3d** prüft jetzt „zweimal ausgeliefert → dieselben Karten, offene Ausgaben = ausgelieferte Karten“ (hängt nicht mehr davon ab, wie viele Etappen gelandet sind);
  **S4a** wählt die Ausgabe gezielt (offen, nicht verfallen, dieser Flug). Damit braucht `i3` die I-4-Migration (Spalte `verfallen_am`).
- Durchgesehen, unverändert passend: `i2` (H10b: 25 h alte Ausgabe verfällt beim nächsten Ausliefern), `lb3`, `w176_t3`, `w176_h8`, `w176_h_muss`, `w176_h_sollte` – gelesen, nicht ausgeführt.
**Nicht geprüft:** Migration und Rauchtests nicht ausgeführt.

## 2026-11-20 – FERTIG: LB-3 Serverteil („Kann er – aber wiederholen“, „Wieder in die Wiederholung“, Sammelaktionen, 4 Stufen) – App 0.81.3

Auftrag I, Teil 3 war schon fertig (83da72d, Meldung darunter; Teil-3-Text in `lernen-app` 752acf0 unverändert) – nichts neu gebaut; LB-3 setzt darauf auf.
Zweig `bau-motivation`, Stand `lernen-app` 752acf0 übernommen. Kein Merge. Datenbank nur gelesen; alle Einfügestellen im Live-Text je einmal vorhanden.
**Migration** `supabase/migrations/20261120_lb3_kann_wiederholen.sql` (nach I-2 und I-3; nicht ausgeführt; pglast ok; kein DROP, kein DELETE, keine Bestandsänderung; wiederholt ausführbar).
**Rauchtest** `supabase/tests/lb3_rauchtest.sql` (Rollback, nur Testkind, nicht ausgeführt). Bisherige Rauchtests: keiner angepasst (Durchsicht: `karte_sicher`, `thema_stand`, `ort_stand`,
`flug_nachtest` verhalten sich ohne gesetzte Flüge wie bisher; `la_4`, `i2`, `i3`, `w176_*`, `w177` laufen damit unverändert – gelesen, nicht gesehen).

### Regeln (wie umgesetzt)
- **„Kann er – aber wiederholen“ setzen:** für jede Etappe des Flugs (aktuelle geprüfte/freigegebene Version, `inhalt.etappen`), die noch nicht gelandet ist: `sitzt = true`, Wiederholung Stufe 1
  (`wdh_stufe 0`, `wdh_lerntage 1`, fällig am nächsten Lerntag – genau wie nach einer eigenen Landung), Herkunft `karte_stand.gesetzt_am`/`gesetzt_von`. Schon gelandete Etappen und eigene Lösungen bleiben unberührt.
  Danach die bestehenden Regeln: Fehler → nächster Lerntag; zwei Fehler hintereinander → wieder offen (▶).
- **Kein Flug-Test, kein Nachtest** für diese Flüge: `test_starten_intern` (blocktest/nachtest) → `{ok:false, grund:'nichts_zu_testen', gesetzt:true}` (ein schon laufender Test bleibt fortsetzbar);
  `nachtest_stand` → `{faellig:false, grund:'gesetzt'}`; `flug_nachtest` → `null` („entfällt“).
- **„sicher“ für gesetzte Etappen:** gelandet + `wdh_stufe ≥ 4` (Wiederholung nach 14 Lerntagen bestanden) + Mischkarte richtig seit der Landung, **falls seit der Landung eine ausgegeben wurde** (`misch_ausgabe`); kein Nachtest.
- **Stand:** `thema_stand`/`ort_stand` zählen kann_wdh-Flüge als erledigt (gelandet), außer eine Etappe ist wieder offen → „läuft“/Ort offen.
- **Sterne:** keine Sterne für gesetzte Landungen (Landungen geben ohnehin keine Sterne). Ort-Sterne wie bei „kann schon“: Ist ein Ort dadurch komplett, wird er „fertig“ und `route_sterne` bucht die Ort-Sterne einmal.
- **Rücknahme** (Flug aus `kann_wdh_themen` genommen, Ort aus dem Plan genommen oder Flug auf komplett/abgewählt gestellt): gesetzte Landungen, bei denen das Kind **seit dem Setzen keinen Versuch** gemacht hat, werden aufgehoben
  (nicht gelandet, Wiederholung leer); mit eigenen Versuchen bleibt der Stand, nur die Herkunft „gesetzt“ fällt weg. Versuche, eigene Lösungen, Sterne bleiben; kein DELETE.
- **„Wieder in die Wiederholung“:** alle gelandeten Etappen des Flugs → Stufe 1, fällig am nächsten Lerntag; „gelandet“ (`sitzt`, `sitzt_am`) und alle Belege bleiben. Bei „Kann er komplett“ gesetzt
  (je Flug oder ganzer Ort) wird daraus „Kann er – aber wiederholen“ (Flug wandert von `kann_schon_themen` nach `kann_wdh_themen`; beim ganzen Ort werden die übrigen Flüge einzeln „komplett“).
  **Flug-Nachtests selbst geschaffter Flüge laufen unverändert weiter** (Begründung: sie prüfen den Flug als Ganzes und sind Teil von „sicher“; der Flug war nicht gesetzt). Ein bestandener Flug-Test bleibt.
- **Die 4 Stufen** (`schule.thema_stufe`, Reihenfolge der Prüfung): gesetzt komplett → ◉ · wieder offen oder Rückreise → ▶ · alle Etappen sicher → ◉ · Test läuft/Verbessern offen/alle gelandet, aber Flug-Test noch nicht geschrieben (nur ungesetzte Flüge) → ▶ ·
  gesetzt wiederholen oder alle gelandet → ↻ · etwas begonnen → ▶ · im Plan → ○ · sonst +.

### Für `bau-lehrer`: neue Felder und Aktionen
**Lesen – `schule_plan_lesen`**
- `kann_wdh: true` – Merkmal: der Server kennt LB-3 (Knöpfe „Kann er – aber wiederholen“ und „Wieder in die Wiederholung“ nur dann zeigen).
- `plan[].kann_wdh_themen: [thema_id]` – wie `kann_schon_themen`.
- `orte[].themen[].kann_wdh: bool` und **`orte[].themen[].stufe`** (für jeden Flug, auch nicht eingeplante):
  `{ stufe: 'komplett'|'wiederholung'|'dran'|'kommt'|'nicht_im_plan', zeichen: '◉'|'↻'|'▶'|'○'|'+', gesetzt: 'komplett'|'wiederholen'|null, im_plan: bool,
     etappen: n, begonnen: n, gelandet: n, sicher: n, wieder_offen: n, wdh_stufe_min: n|null, wdh_nr: 1–5|null („Wdh x von 5“), naechste_in: Lerntage|null (0 = fällig),
     rueckreise: bool, test_offen: bool, ohne_test: bool }`
- `verlauf[].schritt_id` (und `ereignis` ohne die Karten-Liste).
**Lesen – weitere:** `schule_lehrplan_uebersicht.themen[].stufe = {kind_id: <wie oben>}`; `schule_lernstand.einheiten[].thema_id`, `.stufe` und `.karten[].gesetzt`, `.karten[].gesetzt_am`
(Eltern: „gesetzt: kann er, wird wiederholt“); `schule_uebersicht.lernende[].route[].kann_wdh_themen`, `.stand[].ohne_test`; `schule_einheit_lesen.ohne_test`.
**Schreiben – `schule_plan_setzen`** (dieselbe Aktion, ein Aufruf = ein Schritt; mehrere Flüge aus verschiedenen Orten, auch Orte, die noch nicht im Plan stehen – einfach als Eintrag mitschicken):
- je Eintrag zusätzlich `kann_wdh_themen: [thema_id]` (Zustand; fehlt das Feld, bleibt die Liste) und `wieder_wdh_themen: [thema_id]` (Aktion, nur in diesem Aufruf).
- Die vier Einstellungen je Flug: **Lernen** = in keiner Liste · **Kann er – aber wiederholen** = `kann_wdh_themen` · **Kann er komplett** = `kann_schon_themen` · **Aus dem Plan nehmen** = `ausgelassen`.
  Schickt ein Eintrag denselben Flug in `kann_wdh_themen` und in `kann_schon_themen`/`ausgelassen` (oder `kann_schon: true` mit `kann_wdh_themen`), lehnt der Server ab
  („Ein Flug kann nur eine Einstellung haben …“). Schickt ein Eintrag `kann_wdh_themen` nicht mit (alte App), gehen komplett/abgewählt vor und der Flug fällt aus `kann_wdh_themen`.
- Antwort zusätzlich: **`schritt_id`** (und `karten_geaendert`, `karten_zurueck`).
- **Rückgängig:** `schule_plan_setzen` mit `rueckgaengig: <schritt_id>` **und** den Einträgen von davor (wie heute) und der aktuellen `revision`. Der Server stellt die Karten-Stände dieses Schritts wieder her
  (nur Etappen ohne eigene Versuche seither; einmal je Schritt) und wendet dann die Einträge an. So gilt eine Rücknahme für alle Flüge des Sammelschritts, auch für „Wieder in die Wiederholung“.
- Beispiel Sammelschritt: 6 Flüge aus Gym 7 → alle betroffenen Orte als Einträge mit ihren `kann_wdh_themen`, ein Aufruf; `schritt_id` merken für „↶ Rückgängig“.

### Rauchtest `lb3_rauchtest.sql`
6 Flüge Gym 7 in einem Aufruf → alle Etappen gelandet (selbst gelandete Etappe unberührt), Stufe ↻, heute nicht, am nächsten Lerntag fällig · kein Flug-Test/Nachtest, `flug_nachtest` null, `ohne_test` ·
Mischkarten aus gesetzten Etappen · zwei Fehler in der Wiederholung → wieder offen, ▶ · Rücknahme eines Flugs → ○ · Rückgängig des ganzen Sammelschritts (selbst gelandete Etappe und eigene Versuche bleiben) ·
doppelte Einstellung abgelehnt · „Kann er komplett“ → Wieder in die Wiederholung → ↻ · selbst geschafft ◉ → Wieder in die Wiederholung → ↻ (Wdh 1 von 5, Nachtests laufen weiter) → Rückgängig → ◉ · keine Geschenk-Sterne.
Der Weg geht über die neue innere Funktion `schule.plan_setzen_intern` (api ruft sie nach der Zugriffsprüfung); der äußere Zugang ist nicht getestet (Schlüssel).

### App 0.81.3 (nur Kinderseite, damit nichts ins Leere läuft)
Abflugtafel: gesetzte Flüge ohne „TEST BEREIT“ und unter „gelandet“, solange keine Etappe wieder offen ist; Testseite eines gesetzten Flugs: „Für diesen Flug gibt es keinen Test. Du wiederholst ihn nur …“.
Die alte App 0.81.2 bricht nicht (neue Felder werden ignoriert; ein Test-Start bei gesetztem Flug endet mit „Gerade gibt es nichts zu testen.“).
**Gesehen/getestet:** lernen 96 von 96 (neu: LB-3 Testseite ohne Test); Suche 139 bestanden, 9 Fehler – die bekannten alten (13, 15, 101, 103, 105, 111, 113, 126, 127).
**Nicht geprüft:** Migration und Rauchtest nicht ausgeführt; Laufzeit von `thema_stufe` für alle 95 Flüge × Kinder in `schule_plan_lesen`/`schule_lehrplan_uebersicht` nicht gemessen
(je Flug wenige kleine Abfragen; falls zu langsam, später als eine Abfrage je Kind); Lehrer-/Eltern-App für LB-1/2/5 baut `bau-lehrer`.

## 2026-11-20 – FERTIG: Auftrag I, Teil 3 (Nachprüfung ChatGPT 878) – App 0.81.2

Zweig `bau-motivation`, Stand `lernen-app` 23a8b6a übernommen. Kein Merge. Datenbank nur gelesen: I-2 ist eingespielt; `misch_ausgabe` hat heute **0 Zeilen, keine Dopplungen**;
keine Versuche mit `wertung_offen`. Ersetzungsstellen (`einheit_lesen_intern`, `test_starten_intern`) im Live-Text je einmal vorhanden.
**Migration** `supabase/migrations/20261120_i3_lernregeln_nachpruefung.sql` (nicht ausgeführt; pglast ok; kein DROP, kein DELETE, keine Bestandsänderung; wiederholt ausführbar; nach I-2).
**Rauchtest** neu `supabase/tests/i3_lernregeln_rauchtest.sql` (Rollback, nur Testkind, nicht ausgeführt).

**Muss**
1. **Endgültige Wertung festgehalten:** neue Spalte `versuch.wertung_fest` (`eigen | neutral | falsch | ersetzt`), geschrieben, sobald der Trigger entscheidet. `versuch_wertung` liest sie zuerst
   (also auch `folge_nachrechnen`). Ein 2. Anlauf, dessen 1. Anlauf schon endgültig falsch gebucht ist, gilt als `neutral` und bucht nichts – auch wenn er falsch ist.
   Rauchtest genau des Falls aus 878 (2 richtig, X falsch, Y richtig, X im 2. Anlauf richtig): Buchung 1 = Nachrechnung 1 (vorher 1 ≠ 3); Gegenstück mit falschem spätem 2. Anlauf: kein zweiter Fehler.
2. **Nachbuchen genau einmal:** neue Funktion `schule.offene_entscheiden(kind, ausser)` beansprucht offene erste Anläufe in einem Schritt
   (`update … set wertung_offen = false where id in (select … for update skip locked) returning`) und bucht nur die beanspruchten; der Trigger ruft sie auf.
   Rauchtest: zweimal entschieden → 1, dann 0; der Fehler steht einmal in `falsch`. Echte Gleichzeitigkeit (zwei Tabs) lässt sich im Rauchtest nicht erzeugen.

**Sollte**
3. **Einlösen atomar:** `misch_buchen` löst mit `update … returning` (Zeile mit `for update skip locked`) ein; nur wenn das eine Ausgabe trifft, gibt es die Mischkarten-Buchung, sonst normale Buchung.
   Eindeutiger Index `misch_ausgabe_offen_eindeutig` (offene Ausgabe je Kind und Bordkarte); die Migration bricht mit Meldung ab, falls beim Einspielen doch Dopplungen liegen (heute keine).
   `schule.mischkarten` legt Ausgaben mit `insert … on conflict … do update` an.
4. **Ausgabe an die Lage gebunden:** `misch_ausgabe.einheit_id` (gelesener Flug) und `lernziel` (erste noch nicht gelandete Etappe dieses Flugs beim Ausliefern). `misch_gueltig` vergleicht mit dieser Lage,
   nicht mit `aktuell_*` des Geräts. Ausgaben ohne Lage (aus 0.81.1, falls bis zum Einspielen welche entstehen) prüfen wie bisher die Geräte-Angaben.
   Hinweis: Weil Mischkarten nur aus gelandeten Etappen kommen und die gespeicherte Etappe die erste nicht gelandete ist, schließt der Vergleich vor allem gefälschte/veraltete Geräte-Angaben aus.
5. **30-Minuten-Grenze:** `einheit_lesen_intern` und `test_starten_intern` rufen `offene_entscheiden` auf. Rauchtest: über 30 Minuten alte erste Anläufe werden beim Lesen und beim Teststart entschieden, frische nicht.
6. **Tageswechsel (App):** Der Zwischenspeicher merkt sich zusätzlich den Gerätetag beim letzten Server-Stand. Ist auf dem Gerät seither ein neuer Tag (Seite über Nacht offen), gilt der alte Stand nicht mehr (0);
   eine Antwort ohne Karte (z. B. Mischkarte) zählt dann neu ab 1; der nächste Server-Stand (Laden oder Antwort) ersetzt alles, ein neuer Server-Tag verwirft den alten Stand. Test in Playwright.

**Bisherige Rauchtests – angepasst**
- `w176_t3_rauchtest.sql` und `w176_h8_rauchtest.sql`: rufen `misch_buchen` direkt bzw. legen Mischkarten-Versuche direkt an. Seit Teil 3 zählt das nur mit Ausgabe → vor jedem Aufruf wird eine Ausgabe angelegt
  (nur wenn die Tabelle existiert). In h8 sind die zwei Mischkarten-Versuche dafür zwei Anweisungen statt einer.
- Unverändert und nach Durchsicht weiter passend: `i2_lernregeln`, `w177_nachtragstest` (beide Blöcke), `w176_h_muss`, `w176_h_sollte`, `w176_t1`, `w176_t4`, `abgleich_ohne_expeditionen`, `i_pause`, `la_3`, `la_4`.
  Nicht ausgeführt – „läuft weiter“ ist hier gelesen, nicht gesehen.

**Alte App 0.81.1:** keine neue oder geänderte Aktion; Mischkarten kommen weiter über `schule_einheit_lesen`, `heute_selbst`/`heute_tag` unverändert.
**Gesehen/getestet:** lernen 95 von 95 (H6-Test um den Tageswechsel erweitert); Suche 138 bestanden, 10 Fehler – die bekannten alten (13, 15, 101, 103, 105, 111, 113, 126, 127) plus 108, der gelegentlich wackelt. pglast ok für Migration und alle geänderten Rauchtests; keine Variablen-/Alias-Doppelungen.
**Nicht geprüft:** Migration und Rauchtests nicht ausgeführt; Gleichzeitigkeit nur über die Sperr-Klausel abgesichert, nicht unter Last getestet; äußerer Zugang (api.*) nicht getestet (Schlüssel).

## 2026-11-20 – Rauchtest W177, zweiter Block berichtigt (Antwort 20.11. 04:30)

- `supabase/tests/w177_nachtragstest_rauchtest.sql`, Prüfung „FEHLER 7b“: `a.id = any((select aufgaben …))` las die Unterabfrage als Menge von Arrays → `bigint = bigint[]`.
  Jetzt werden die Aufgaben der Korrektur-Sitzung zuerst in `v_ids` gelesen, dann `a.id = any(v_ids)` – wie in Prüfung 5b. Sonst unverändert.
- Stand `lernen-app` übernommen. pglast ok, keine Variablen-/Alias-Doppelungen; in den übrigen Rauchtests kommt das Muster nicht vor. **Nicht ausgeführt** (keine Datenbank), kein Merge.

## 2026-11-20 – FERTIG: Auftrag I, Teil 2 (Lernregeln) – App 0.81.1

Zweig `bau-motivation`, Stand `lernen-app` 68a663d (Teil 1 und 1b enthalten) übernommen. Kein Merge. Datenbank nur gelesen (Funktionstexte, Stellen je einmal vorhanden geprüft).
**Migration** `supabase/migrations/20261120_i2_lernregeln.sql` (nicht ausgeführt; pglast ok; kein DROP, kein DELETE, keine Bestandsänderung; wiederholt ausführbar).
**Rauchtests** (nicht ausgeführt, Rollback, nur Testkind): neu `supabase/tests/i2_lernregeln_rauchtest.sql`; ergänzt `w177_nachtragstest_rauchtest.sql` (zweiter Block);
angepasst `w176_h_muss_rauchtest.sql` (H10a legt jetzt eine Ausgabe an – ohne sie wäre der alte Fall nach I-2 zu Recht keine Mischkarte mehr).

**Muss**
1. **H10 – Mischkarte serverseitig gebunden.** Neue Tabelle `schule.misch_ausgabe` (Kind, Bordkarte, ausgegeben am, eingelöst am). `schule.mischkarten` merkt jede ausgelieferte Karte
   (die bisherige Auswahl heißt jetzt `schule.mischkarten_waehlen`, unverändert); schon offene Ausgaben werden nur aufgefrischt. `misch_gueltig` verlangt zusätzlich eine
   ausgegebene, nicht eingelöste Ausgabe der letzten 24 Stunden; `misch_buchen` löst sie ein. `uebung_pruefen_intern` prüft einmal vor dem Speichern (sonst wäre die Ausgabe
   für die Antwort schon verbraucht). Ohne Ausgabe: normale Buchung als Übung, kein Misch-Beleg, kein `misch` in der Antwort.
   **App 0.80.0** holt ihre Mischkarten über `schule_einheit_lesen` → sie sind ausgegeben, der Ablauf bleibt gleich; sie bricht nicht.
   Rauchtest: gefälschter Kontext ohne Ausgabe und mit Ausgabe älter als 24 h → kein Beleg (Negativ); Flug lesen → Ausgabe → Antwort → Beleg, `misch.ok`, eingelöst (Positiv); dieselbe Karte zweimal → beim zweiten Mal kein Beleg.
2. **H2 – eine Regel für „endgültig falsch“.** `schule.versuch_wertung(versuch)` = `eigen | neutral | falsch | ersetzt | offen | test`: ohne zweite Chance oder im 2. Anlauf falsch → sofort `falsch`;
   falscher 1. Anlauf → `offen`, bis ein 2. Anlauf derselben Bordkarte kommt (`ersetzt`, der 2. Anlauf entscheidet) oder das Kind weitergeht bzw. 30 Minuten vergehen (`falsch`).
   Der Trigger `versuch_karte` bucht damit (`schule.versuch_buchen`) und merkt sich offene erste Anläufe (`versuch.wertung_offen`); beim nächsten Versuch des Kindes werden sie entschieden und,
   wenn endgültig falsch, nachgebucht. `schule.folge_nachrechnen(kind, einheit, lernziel, ab)` rechnet „folge“ mit derselben Regel nach (nur lesen).
   **Keine Bestandsänderung:** alte Zeilen haben `wertung_offen = null` und werden nie nachgebucht.
   **Verhaltensänderung in der laufenden Buchung:** Ein falscher 1. Anlauf, den das Kind liegen lässt, bricht jetzt die Folge (bisher wurde er nie gebucht).
   Rauchtest (Negativ): 2 richtig → 1. Anlauf falsch, liegengelassen → nächste richtig → Folge 1 (vorher 3); Nachrechnung = Buchung. Dazu: 1. Anlauf falsch + 2. richtig → Folge bleibt; ohne zweite Chance falsch → 0.

**Sollte**
3. **H4/H11/H14 – Tests** (im neuen Rauchtest): H4 Nachtest 4/5 bestanden, diese Etappe falsch → nicht „sicher“, Gegenprobe richtig → sicher. H11 über die ganze Buchung: Expedition-Teil zeigt auf eine
   neue Version des Flugs (im Test angelegt), Antwort über `uebung_pruefen_intern` bucht „angewandt“ auf die gelandete alte Version. H14: Teil a → „begonnen“, Unterbrechung mit Rückfall einer Voraussetzung,
   Teile b und c → „geschafft“, Sterne einmal, auch wenn Teil a wiederholt wird.
4. **H12 – Import:** `expedition_importieren` prüft jede angegebene Voraussetzung auch auf eine vorhandene Lernkarte (Lernziel mit Übungen, Flug nicht „ersetzt“), vor jedem Schreiben.
   Alle 21 vorhandenen Expeditionen erfüllen das (gelesen). Rauchtest: unbekannte Lernkarte → Fehler „Voraussetzung: Lernkarte …“, nichts geschrieben; gültige Datei läuft.
5. **H6 – Tageszähler:** Server liefert `heute_tag` (Kalendertag in der Zeitzone des Kindes, `schule.heute_tag`) in `schule_einheit_lesen` und in `schule_uebung_pruefen.karte`.
   App speichert `{tag, n, server}` und zeigt den Server-Zähler unabhängig vom Gerätetag; nur ohne Server-Tag (alter Server) zählt das Gerät nach seinem Tag.
6. **W177 – Nachtragstest** (Rauchtest ergänzt): offen + fehlerhaft zugleich → Nachtragstest nur für die offene Etappe, danach Korrektur nur für die fehlerhafte; Abbruch und Wiederaufnahme → dieselbe Sitzung,
   Antwort einmal gespeichert; Sterne vorher/nachher = richtige × Regel, zweiter Abschluss bucht nichts. Läuft der Nachtragstest, bekommt eine Korrektur-Anfrage den laufenden Test zurück (heutiges Verhalten, nur notiert).
   **Frist des nächsten Nachtests (nichts geändert – Sebastian entscheidet):** Der Nachtragstest ist technisch ein Flugtest (`blocktest`). Solange es **noch keinen Nachtest** gab, ist der Anker
   der letzte Abschluss eines Flugtests oder einer Korrektur → **die 10-Lerntage-Frist beginnt nach dem Nachtragstest (und nach jeder folgenden Korrektur) neu.** Gab es **schon einen Nachtest**,
   zählt die Frist ab diesem Nachtest weiter; der Nachtragstest verschiebt sie nicht. Solange eine Pflicht-Etappe offen oder fehlerhaft ist, ist ohnehin kein Nachtest fällig.
7. **H5/H13 – was wie getestet ist:**
   - Über die **innere Funktion** (Rauchtest, Rollback): alle Fälle oben – `schule.uebung_pruefen_intern`, `schule.einheit_lesen_intern`, `schule.mischkarten`, `schule.test_starten_intern`,
     `schule.test_abschliessen_intern`, `schule.expedition_importieren`; dahinter echte Trigger (`versuch_karte`, Sterne). Die Testsitzung für H4 und Testantworten im W177-Block werden direkt eingetragen.
   - Über den **äußeren Zugang** (`api.schule_*` mit Zugangsschlüssel, Edge-Funktion `lernen-api`): **nicht getestet** – braucht einen Schlüssel, der in keine Datei gehört. Die `api.*`-Funktionen sind unverändert
     und rufen genau diese inneren Funktionen nach der Zugriffsprüfung auf.
   - App: Playwright mit nachgebildeten Server-Antworten (H6).

**Gesehen/getestet:** lernen 95 von 95 (neu I-2/H6); Suche 138 bestanden, 10 Fehler – die bekannten alten (13, 15, 101, 103, 105, 111, 113, 126, 127) plus 108, der gelegentlich wackelt; keiner betrifft die Lern-Seiten. Migration und Rauchtests mit pglast geparst, keine Variablen-/Alias-Doppelungen; Ersetzungsstellen im Live-Text je einmal vorhanden.
**Nicht geprüft:** Migration und Rauchtests nicht ausgeführt. Die 30-Minuten-Grenze für „weitergegangen“ ist eine Annahme (im Rauchtest nur der Fall „andere Bordkarte“). Einzelne Ausgaben,
die nie beantwortet werden, bleiben als offene Zeilen in `misch_ausgabe` liegen (zählen nach 24 h nicht mehr; kein Aufräumen, weil kein DELETE).

## 2026-11-20 – Rauchtest „Abgleich ohne Expeditionen“ angepasst

- `supabase/tests/abgleich_ohne_expeditionen_rauchtest.sql`: setzt den gewählten Flug vor dem Abgleich auf `geprueft` (nur wenn er `freigegeben` ist; im Rollback, nichts bleibt) –
  wie beim Einspielen, weil Aufgaben freigegebener Einheiten unveränderlich sind. Sonst unverändert. pglast ok, nicht ausgeführt.

## 2026-11-18 – FERTIG: Abgleich ohne Expeditionen

Stand von `lernen-app` übernommen (enthält 9d2f9be – dein berichtigter Kommentar in `h_muss` bleibt so).

- **Migration** `supabase/migrations/20261119_abgleich_ohne_expeditionen.sql` (nicht ausgeführt; pglast ok; kein DROP, kein DELETE):
  `schule.einheit_abgleichen` lässt Aufgaben mit `pool = 'expedition'` ganz unberührt – an allen 5 Stellen mit `b.einheit_id = v_e` (Änderungen übernehmen, „schon vorhanden?“, Zählen „nicht mehr in der Datei“, **Sperren**, Löschen bei Entwürfen).
  Die Migration bricht ab, wenn es nicht genau 5 Stellen sind oder die Funktion schon angepasst ist. Expeditions-Teile pflegt nur `expedition_importieren`.
- **Rauchtest** `supabase/tests/abgleich_ohne_expeditionen_rauchtest.sql` (Rollback): baut aus dem Datenbank-Stand die Themendatei eines Flugs mit freigegebenen Expeditions-Teilen (heute z. B. Einheit 1 mit 5 Teilen),
  gleicht mit `'sperren'` ab → Teile bleiben frei, „nicht mehr in der Datei“ = 0, keine neuen Aufgaben; Gegenprobe: eine Übung aus der Datei genommen → genau diese wird gesperrt, die Teile nicht.
  Vor der Migration schlägt der Test mit „FEHLER 2“ fehl (Nachweis des Fehlers).
- **Rauchtest H12b** (`w176_h_sollte_rauchtest.sql`): nimmt jetzt den Schlüssel `8-rauchtest-h12`, den es nicht gibt (prüft das vorab), statt `8-handytarif`. Damit stimmt auch H12d (4 neue Teile).
- Gelesen (nur lesend): heute 90 Expeditions-Teile, davon 0 gesperrt.

## 2026-11-18 – FERTIG: Auftrag H (korrigiert)

**Ursache** „record "v" is not assigned yet“: Im H2-Block von `20261119_w176_h_muss.sql` hieß die Schleifenvariable `v` wie der Tabellen-Alias `schule.versuch v`. Variable heißt jetzt `w`.

**Geprüft mit einem Skript** (Variablen jedes `declare` gegen Tabellen-/Funktions-Aliase im selben Block; erkennt die gemeldeten Fälle in den alten Fassungen):
- `h_sollte`: zweite Kollision gefunden und behoben – in `expedition_importieren` (H12-Prüfungen) liefen `jsonb_array_elements(…) t` / `… v` gegen die Variablen `t`, `v` → Aliase `tt`, `vv`.
- In die Live-Funktionen eingesetzte Stücke (`uebung_pruefen_intern`, `etappen_stand`, `schule_lernstand`, `schule_uebersicht`, `einheit_lesen_intern`, `expeditionen_kind`) gegen deren `declare` geprüft: keine Kollision.
- Danach: keine Treffer mehr in `h8`, `h_muss`, `h_sollte` und allen Rauchtests.
- Nebenbei: Bestandsfüllung H3 nimmt `misch` jetzt mit `coalesce(…, false)`.

**Rauchtests**
- `w176_t4_rauchtest.sql`: „a_ids is not a known variable“ – ein Kommentar stand mitten in der `declare`-Zeile und verschluckte `a_ids` und `v_n` (seit der Umbenennung k → ks). Behoben. Schritt 5 erwartet seit H8 `wdh_fehler = 0` (nur fällig).
- `w176_t3_rauchtest.sql` Schritt 4: erwartet jetzt `wdh_fehler = 0`, `wdh_lerntage = 1`, Etappe gelandet (H8).
- `w176_t1_rauchtest.sql`: an H3 angepasst (6-mal dieselbe Bordkarte → eigene 1, folge 6; Landen mit genug verschiedenen Bordkarten).
- `w176_h_muss_rauchtest.sql`: Variable `a` → `ag` (kollidierte mit `schule.aufgabe a`). `w176_h_sollte_rauchtest.sql`: Aliase `a`, `x` im H13-Teil → `au`, `xa`.
- Reihenfolge Probelauf: `h_muss` → `h_sollte` → Rauchtests `h8`, `t1`, `t3`, `t4`, `gesperrt`, `h_muss`, `h_sollte`.

Fachlich unverändert gegenüber „FERTIG: Auftrag H“; App unverändert (0.79.0).

## 2026-11-18 – FERTIG: Auftrag H (H1–H4, H9–H11 Muss; H5–H7, H12–H15 Sollte) – App 0.79.0

**Migrationen** (nicht ausgeführt; pglast ok; alle Ersetz-Stellen vorher im Live-Text geprüft, Abbruch mit Meldung, falls eine fehlt; kein DROP, kein DELETE; gelandete Etappen bleiben gelandet, Lernstände bleiben).
Reihenfolge: `20261119_w176_h8_misch_fehler_offen_lassen.sql` → `20261119_w176_h_muss.sql` → `20261119_w176_h_sollte.sql`. **App 0.79.0 mit `h_muss` zusammen live nehmen** (sonst zählen Mischkarten der alten App nicht mehr als Misch-Beleg, siehe H10).

**Rauchtests** (Rollback, nur Testkind, keine Namen, über den echten Weg `schule.uebung_pruefen_intern` → Trigger): `supabase/tests/w176_h_muss_rauchtest.sql` (H1, H3, H4, H9, H10, H11),
`supabase/tests/w176_h_sollte_rauchtest.sql` (H6, H12, H13-Server, H14, H15). `w176_t4_rauchtest.sql` Schritt 9 angepasst (ohne Teil b statt d, damit 3 Themen bleiben – H12).
**App-Tests:** lernen 70 von 70 (neu: H1, H3/H6, H4, H7, H13 ×2; erweitert: T3 Mischkarte H10, T4 Expedition H15); Suche: 9 bekannte alte Fehler.

**Zahlen vorher → nachher (gelesen, ohne Namen):**
- Karten-Stände 36, gelandet 34 → 34 (unverändert).
- H1: 1 offene Etappe mit früherer Landung und bestandenem Test – vorher überall „fertig“, nachher „wieder offen“ (Test getrennt sichtbar). Abflugtafel: 22 Flug-Stände, 7 ändern ihre Zahl der fertigen
  Etappen (6 höher, weil gelandete Etappen jetzt zählen, nicht nur bestandene Tests; 1 niedriger = die wieder offene); Summe fertiger Etappen 20 → 32; vollständig 1 → 1.
- H2: 1 offene Zeile aus der Übernahme mit erfundener Folge: `folge` 3 → 5 (nachgerechnet aus 5 eigenen Lösungen in Folge); die andere offene Zeile hat Folge 0 und bleibt. 0 Zeilen seit der Übernahme überschrieben.
- H3: 36 Karten-Stände bekommen die Liste gezählter Aufgaben (131 verschiedene Aufgaben); 0 Karten haben mehr eigene Lösungen als verschiedene Aufgaben → `eigene_loesungen` unverändert.
- H4: „sicher“ 0 → 0; Flug-Nachtest bestanden bei gelandeten Etappen 0; Misch-Belege 0. H9/H11/H15: 0 Expeditionen live.

**Antworten für ChatGPT:**
- **H1** Angenommen. Eine Funktion `schule.etappe_fertig`: fertig = gelandet; ein bestandener Test zählt nur, solange die Etappe nie gelandet war (alte Stände ohne Übungsweg). Gilt in `etappen_stand` (Etappe, Testsperre),
  in der `karte`-Antwort (App übernimmt `fertig` vom Server statt `fertig || sitzt`), in `schule_uebersicht` (Abflugtafel) und bei den Eltern (`wieder_offen`, „wieder offen“). Neu `geoeffnet_am`, `test_nachgewiesen` getrennt.
  Die Reiseroute (Ort/Stempel erreicht) bleibt bewusst testbasiert – ein Rückfall nimmt keinen Ort weg. Test: gelandet + Test → 2 Fehler in der Wiederholung → überall offen → 3 eigene in Folge → gelandet.
- **H2** Angenommen. `folge` offener Etappen nur in Zeilen ohne Übungsversuch seit der Übernahme (17.11. 15:17 UTC) aus den geordneten endgültigen Versuchen nachgerechnet; früher schon gelandete → 0.
- **H3** Angenommen. Für eigene Lösungen, Typen und „schwer“ zählt jede Aufgabe je Lernkarte einmal (`gezaehlt`); für „in Folge“ zählt jede eigene Lösung – sonst könnte eine Lernkarte mit genau 6 Aufgaben
  nach einem Fehler nie wieder landen. Nach dem Wiederöffnen sind eigene Lösungen/Typen/schwer schon erfüllt, es fehlen nur 3 in Folge; dafür zählen bekannte Aufgaben. Eine Regel „nach ≥ 1 Lerntag neu zählen“
  ist deshalb nicht nötig (nicht gebaut). Text „Die kennst du schon – gut wiederholt.“; die App nimmt ungezählte zuerst, gezählte nur, wenn keine ungezählte mehr da ist.
- **H4** Angenommen. „sicher“ verlangt jetzt: Misch-Beleg und im Flug-Nachtest die Aufgabe dieser Lernkarte richtig – beides nach der letzten Landung. Sonst bei den Eltern „Flug-Nachtest bestanden“.
- **H5** Angenommen: beide Rauchtests laufen über `uebung_pruefen_intern` und den Trigger. `api.schule_uebung_pruefen` ruft genau diese Funktion nach der Zugriffsprüfung; ein Zugangsschlüssel gehört nicht in eine Datei.
- **H6** Angenommen (bevorzugte Variante): `heute_selbst` zählt der Server aus bestätigten Versuchen im Tag des Kindes (`lernender.zeitzone`); die App zeigt den Wert und speichert ihn nur noch unter dem Ortstag, nicht UTC.
- **H7** Angenommen. Tipp: „zählt nicht als eigene Lösung; unterbricht deine Folge nicht“. „Punkte“/„Serie“ aus Kinder- und Elterntexten entfernt (auch in der Rückfall-Anzeige alter Server).
- **H8** Erledigt (eigene Meldung unten).
- **H9** Angenommen. Ein Expeditions-Teil wird nur gewertet, wenn alle Voraussetzungen gelandet sind oder die Expedition schon begonnen ist (Rückfall: zu Ende führen ohne Nachteil). `klasse` = nur Einordnung.
- **H10** Angenommen. `schule.misch_gueltig`: Pool Übung, Stufe 2–3, freigegeben, Etappe beim Kind gelandet, nicht die gerade geübte (App schickt `aktuell_einheit`, `aktuell_lernziel`). Sonst normale Buchung ohne Misch-Beleg.
  Negativtests: ohne aktuelle Etappe, aus der aktuellen Etappe, aus nicht gelandeter Etappe.
- **H11** Angenommen. `schule.expedition_etappe` sucht je Kind über `thema_id` + Lernkarte die gelandete Version; Test mit zwei Versionen.
- **H12** Angenommen. Import lehnt vor dem Schreiben ab: nicht 3–5 Teile, doppelte Kennung, fehlender Antworttyp/Frage/Lösung, < 3 Themen, Bezug außerhalb der Voraussetzungen, unbekannte Lernkarte,
  „geprueft/freigegeben“ ohne entsprechend geprüfte/freigegebene Bezugs-Flüge. `tools/inhalt_pruefen.py` prüft „≥ 3 Themen“ ebenfalls.
- **H13** Angenommen. Tests: Klasse 5 jede 6., Klasse 8 jede 4. (Server und App), nie mit nur 2 gelandeten, nie bei gewählter Stufe, alle 8 genau einmal, Lernkarte wechseln/Neustart beginnt neu, nach falscher Mischkarte normal weiter.
- **H14** Angenommen: Expedition (zweimal falsch, dann richtig, geschafft) und gesperrt laufen über `uebung_pruefen_intern`.
- **H15** Angenommen. Expedition meldet getrennt `teile_erledigt` (abgeschlossen) und `teile_selbst` (1. Versuch ohne Tipp); Kind: „x von n Teilen selbst gelöst“, Eltern ebenso. Misch-Beleg zählt für „sicher“ nur nach der letzten Landung.

**README** (`inhalte/README.md`) und Info-Seite (App) ergänzt: einmal zählen je Aufgabe, „Wieder offen“, „sicher“ nach der letzten Landung, Server-Prüfung der Mischkarten, Expeditions-Regeln H9/H11/H12/H15.

## 2026-11-18 – FERTIG: H8 (Fehler in Mischkarte/Expedition öffnet keine gelandete Etappe mehr) – sofort einspielbar

**Migration** `supabase/migrations/20261119_w176_h8_misch_fehler_offen_lassen.sql` (nicht ausgeführt; pglast ok; ersetzt die Live-Fassungen von `misch_buchen` und `expedition_buchen`, vorher gelesen; kein DROP, kein DELETE; keine App-Änderung nötig).
- Neu `schule.karte_faellig_machen(kind, einheit, lernkarte, zeit)`: Etappe am nächsten Lerntag fällig (`wdh_ab = jetzt`, `wdh_lerntage = 1`); `sitzt`, `wdh_stufe`, `wdh_fehler`, `misch_ok_am`, `angewandt_am` und alle übrigen Belege bleiben.
  Ist die Etappe schon fällig, bleibt der frühere Termin.
- `misch_buchen` und `expedition_buchen` rufen bei einem endgültigen Fehler nur noch diese Funktion (nicht mehr `karte_buchen(…, false)`); auch beim 2. und 3. Fehler und bei `wdh_fehler = 1` bleibt die Etappe gelandet.
  Wieder öffnen kann allein die fällige Wiederholung (`karte_buchen`, unverändert). `misch_buchen` zählt den Fehler zusätzlich in `falsch`.
- Hinweis: Wird die durch einen Mischfehler fällige Wiederholung bestanden, rückt die Wiederholungsstufe wie bei jeder bestandenen fälligen Wiederholung um 1 vor (unverändertes Verhalten von `karte_buchen`).

**Zahlen (gelesen vor dem Einspielen, ohne Namen):** 36 Karten-Stände, davon 34 gelandet; 1 Karten-Stand offen mit früherer Landung (nicht durch Mischkarte – es gibt noch 0 Mischkarten-Versuche);
0 Expeditionen, 0 Expeditions-Versuche → keine Etappe ist durch H8 betroffen, keine Reparatur nötig. Nachher erwartet: unverändert 34 von 36 gelandet.

**Rauchtest** `supabase/tests/w176_h8_rauchtest.sql` (Rollback, nur Testkind): Etappe gelandet mit `wdh_fehler = 1` → 2 endgültige Mischkarten-Fehler über den echten Trigger → bleibt gelandet, Belege gleich, fällig ·
Expedition 2 × falsch und gemischt mit Mischkarte → bleibt gelandet · Gegenprobe: 2. Fehler in der fälligen Wiederholung öffnet weiterhin.

**Antwort für ChatGPT (H8):** Angenommen. Mischkarten und Expeditionen haben jetzt einen eigenen Fehlerweg, der nur fällig macht; `sitzt` und Belege ändern sich nie, unabhängig von `wdh_fehler`. Das Öffnen bleibt der fälligen Wiederholung vorbehalten.

## 2026-11-18 – FERTIG: Fehler „Diese Aufgabe ist noch nicht freigegeben“ beim Prüfen; Rauchtest Teil 4 korrigiert – App 0.78.1

**Server – Migration** `supabase/migrations/20261118_w176_a_gesperrt_pruefen.sql` (nicht ausgeführt; pglast ok; Stelle im Live-Text genau einmal vorhanden; kein DROP, kein DELETE):
- `schule.uebung_pruefen_intern`: Eine gesperrte Bordkarte (`freigegeben = false`) wird beim **Prüfen** noch normal gewertet, wenn ihr Flug **geprüft oder freigegeben** ist. Die Sperre greift nur bei der
  **Auswahl** neuer Bordkarten (Übung, Wiederholung, Mischkarten, Knobel, Tests – unverändert). Entwurfs-Flüge bleiben für echte Kinder gesperrt (vorher schon über `einheit_pruefen_sichtbar`;
  gesperrte Bordkarte im Entwurf nur fürs Testkind, wie bisher).
- Die Datei läuft auf dem heutigen Stand **und** vor oder nach W176 Teil 1/3/4 (erkennt beide Fassungen der Stelle, zweimal einspielen schadet nicht). Sie kann sofort und unabhängig von „Live“ eingespielt werden.
- **Geändert in Teil 3** (`20261118_w176_t3_mischkarten.sql`, noch nicht eingespielt): fasst `uebung_pruefen_intern` an dieser Stelle nicht mehr an (sonst hätte Teil 3 die Prüf-Sperre fürs Testkind wieder verschärft
  bzw. die Stelle nicht mehr gefunden). Die beiden Auswahl-Stellen (Flug laden, Wiederholung) bleiben in Teil 3.
- Rauchtest `supabase/tests/w176_gesperrt_rauchtest.sql` (Rollback, ohne Namen): gesperrte Übung in freigegebenem Flug wird gewertet · gesperrte Übung im Entwurf bleibt für echte Kinder gesperrt.

**App 0.78.1** – kommt beim Prüfen trotzdem „… nicht freigegeben“ (z. B. bevor die Migration eingespielt ist): keine rote Meldung. Üben (auch Mischkarten), Wiederholung und Expedition laden still neu
und zeigen die nächste Bordkarte; eine Knobel-Bordkarte schließt sich still; im Test geht es zur nächsten Bordkarte (der Server prüft im Test nicht auf die Sperre – nur zur Sicherheit).
Gewertet wurde nichts, die Checkliste bleibt unverändert. Tests: Üben (neu geladen, keine Meldung, Checkliste gleich), Knobel und Wiederholung.

**Rauchtest Teil 4** `supabase/tests/w176_t4_rauchtest.sql`: Variable `k` → `ks` (kollidierte mit dem Tabellen-Alias `k`). Migration Teil 4 unverändert.

**Tests:** lernen 64 von 64; Suche: 9 bekannte alte Fehler.

## 2026-11-18 – FERTIG: Teil 4 (P3 Expeditionen, Technik) – App 0.78.0 – wartet auf Migration

**Migration** `supabase/migrations/20261118_w176_t4_expeditionen.sql` (nicht ausgeführt; pglast ok; Ersetzungsstellen im Live-Text vorhanden; setzt Teil 1 und Teil 3 voraus; kein DROP von Tabellen/Spalten/Funktionen, kein DELETE).
**Ausnahme wie bei Migration F:** `aufgabe_pool_check` (+ `expedition`) und `sterne_grund_check` (+ `expedition`) werden als „drop constraint + add constraint“ in einem Befehl erweitert.

- **Datenmodell (Entscheidung):** Kopf in neuer Tabelle `schule.expedition` (schluessel, klasse, titel, einleitung, grafik, voraussetzungen mit thema_id, autor, status entwurf/geprueft/freigegeben, version);
  **Teile als Zeilen in `schule.aufgabe`** (pool `expedition`, `expedition_id`, `teil`; einheit_id/variante_gruppe = Etappe des Bezugs). Begründung: Teile sind Bordkarten – Bewertung, zweiter Versuch,
  Lösung und `schule.versuch` (aufgabe_id Pflicht) laufen unverändert; der eigene Pool hält Teile aus Übung, Mischkarten, Wiederholung und Tests heraus. `aufgabe_schutz` nimmt Expeditions-Teile aus
  (sonst wären Teile mit Bezug auf einen freigegebenen Flug nicht abgleichbar).
- **Import/Abgleich:** `schule.expedition_importieren(datei jsonb, status text default null)` – neu anlegen oder nach `schluessel` bzw. Teil-Kennung `k` abgleichen; Teile, die nicht mehr in der Datei stehen,
  werden gesperrt, nichts gelöscht. Neu = `entwurf` (nur Testkind), Status per zweitem Argument.
- **Angebot:** nur wenn **alle** Voraussetzungs-Lernkarten beim Kind gelandet sind (jede Version der Einheit des Themas), Plan-Reihenfolge egal; Entwurf nur Testkind.
- **Ablauf/Belege:** Teil erledigt = richtig oder endgültig (2. Versuch bzw. Lösung gezeigt). Richtig im 1. Versuch ohne Tipp → `karte_stand.angewandt_am` der Bezugs-Etappe (Anzeige mit P5).
  Endgültig falsch → Bezugs-Etappe am nächsten Lerntag fällig (wie eine falsche Mischkarte; gebucht über `karte_buchen` mit einer Übung dieser Etappe). Keine Minuspunkte, zählt nicht für „gelandet“.
- **Sterne/Stempel:** Vorschlag `sterne_expedition_geschafft` = 50 (ein Ort 100) bei „alle Teile erledigt“, je Expedition einmal; jeder richtige Teil wie jede Bordkarte 10. Stempel = `konto.expeditions_stempel`.
- **Felder für die App (keine neue Aktion in lernen-api):** `schule_konto.expeditionen` (angeboten/begonnen/geschafft, mit Teilen; Lösung nur bei erledigten), `konto.expeditions_stempel`;
  `schule_uebung_pruefen` nimmt Teile an und antwortet mit `expedition: {id, teil, erledigt, geschafft, sterne}`; `schule_uebersicht`: je Kind `expeditionen [{id, zustand}]`,
  für Eltern/Lehrer oben `expeditionen` (alle, mit Lösungen).

**App 0.78.0** (ohne Migration: keine Expeditionen sichtbar)
- Kind: Karte „⛰ EXPEDITION“ auf der Abflugtafel (begonnene zuerst), Seite `#/expedition/<kind>-<id>`: Einleitung und Grafik, Teil für Teil mit 2 Versuchen; danach Lösung und Weg,
  „Keine Abzüge – im nächsten Teil geht es mit den richtigen Zahlen weiter.“, „Weiter mit Teil B ›“; erledigte Teile bleiben sichtbar; Abbruch jederzeit (Stand kommt vom Server);
  Abschluss „EXPEDITION GESCHAFFT“ mit Sternen; Reisepass „⛰ Expeditions-Stempel: n“.
- Eltern/Lehrer: Lehrplan-Übersicht → „Expeditionen ansehen“ (`#/expeditionen`, mit Status, Voraussetzungen, Teilen, Lösungen); Lernstand des Kindes: Abschnitt „Expeditionen“ (angeboten/begonnen/geschafft);
  in „Inhalte ansehen“ eines Flugs erscheinen Expeditions-Teile nicht. Info-Seite: „Expeditionen“.
- Grafik: die App zeichnet wie bisher; das Kind liest ab und wählt aus, gezeichnet wird nicht.

**Rauchtest** `supabase/tests/w176_t4_rauchtest.sql` (nach dem Einspielen; Rollback; Testkind; importiert „Handytarif“ als Entwurf): Entwurf nur Testkind · ohne alle Voraussetzungen kein Angebot ·
alle gelandet → angeboten · Teil falsch → erledigt, Bezugs-Etappe fällig · Abbruch verliert nichts · Teil richtig → Beleg · alle Teile → geschafft, Sterne genau einmal · Abgleich ohne Änderung ändert nichts,
entfernter Teil wird gesperrt, nicht gelöscht.
**Tests:** lernen 62 von 62 (neu T4: Angebot und Durchlauf mit Fehler/2. Versuch/Lösung/nächster Teil/Abschluss; Abbruch und kein Angebot; Eltern-Ansichten). Suche: bekannte alte Fehler (diesmal 10, schwankend).
**Nicht geprüft:** Migration gegen echte Daten; die Handytarif-Grafik in der echten App (nur im Test-Mock ohne Grafik).

## 2026-11-18 – FERTIG: IB richtig beschriften (Auftrag 18.11. 03:33, Punkt 2) – in App 0.78.0

- Einheitlich **MYP-Jahr = Klasse − 5** (vorher an einer Stelle Klasse − 4); ein Kind in Klasse 5 steht **vor MYP-Jahr 1** (Stufe 0, Anzeige „vor MYP-Jahr 1“, 0 Flüge). Linienplan unverändert (MYP-Jahr n unter Klasse n + 5).
- Beschriftung überall „MYP-Jahr n“ (Lernstand-Tabelle, Einstieg prüfen, Mini-Linien, Passkarte, Lehrplan-Übersicht „IB MYP-Jahr n“, Flugplan, Vorlage, Stufen-Auswahl), Hinweis „MYP-Jahr 1–5 entspricht etwa Klasse 6–10“
  (Linienplan-Name, IB-Reiter im Lernstand, Lehrplan-Übersicht, Stufen im Flugplan, Info-Seite „Worauf baut die App auf?“ – vorher stand dort „MYP 1–4“).
- Test: Umrechnung (Kl. 5 → 0, Kl. 8 → 3, Kl. 10 → 5, gesetzte Stufe bleibt), Spaltenköpfe „MYP-Jahr 1…5“, Hinweis, Info-Seite, kein „Klasse − 4“ mehr im Quelltext. Punkte 1 und 3 des Auftrags: siehe Eintrag „Teil 3 (korrigiert)“ unten.

## 2026-11-18 – FERTIG: Teil 3 (korrigiert) und Wunsch „Lernen starten“ – App 0.77.1

**Korrektur Migration** `supabase/migrations/20261118_w176_t3_mischkarten.sql` (weiter nicht eingespielt; pglast ok; Stellen im Live-Text vorhanden):
- `schule.mischkarten` nimmt nur noch `a.freigegeben` – gesperrte Aufgaben nie als Mischkarte, auch nicht für das Testkind. Entwurfs-Flüge des Testkinds bleiben über `e.status` erlaubt.
- **Dieselbe Stelle gab es dreimal anderswo** (Live-Text gelesen) – dort gilt jetzt dieselbe Regel (Abschnitt am Ende der Migration):
  `schule.einheit_lesen_intern` (Übungen und Knobel-Bordkarten der Einheit: `a.freigegeben or Testkind` → `a.freigegeben`),
  `api.schule_wiederholung` (`a.freigegeben or v_test` → `a.freigegeben`), `schule.uebung_pruefen_intern` (Testkind durfte gesperrte Aufgaben prüfen → jetzt nicht mehr).
  Folge: Das Testkind sieht beim Üben und in der Wiederholung keine gesperrten Aufgaben mehr; Entwurfs-Flüge sieht es weiter (Status der Einheit). Zahlen heute: in Entwurfs-Flügen
  2 797 freigegebene und 1 500 gesperrte Übungen, in freigegebenen Flügen 11 427 / 3 457 – das Testkind übt also weiter Entwürfe, nur ohne die gesperrten.
  Bitte bewusst mit einspielen; wer das für das Testkind anders will, nimmt den letzten Block heraus (die Mischkarten-Korrektur steht davon getrennt in `schule.mischkarten`).
- Rauchtest `supabase/tests/w176_t3_rauchtest.sql` unverändert; Fall 2 prüft genau diese Bedingung.

**Wunsch 18.11. – „Lernen starten“ an der Kinderkarte** (Eltern/Lehrer-Startseite): erster, hervorgehobener Knopf „Lernen starten ›“ (Akzentfarbe, öffnet `#/reise/<id>`), danach „Lernstand“,
„Was wackelt?“, „Flugplan“; „Lernreise ansehen“ entfällt (gleiches Ziel). Auf dem Handy (≤ 600 px) steht „Lernen starten“ allein über die ganze erste Zeile.
Info-Seite: Absatz „Lernen starten“ oben. Test: Reihenfolge, Hervorhebung, erste Zeile auf 390/820/1280 px (auf 390 px allein), Klick öffnet die Abflugtafel, Info-Satz.

**Tests:** lernen 58 von 58. Suche: die bekannten alten Fehler (diesmal 10 – W80 Nr. 108 schwankt; „PWA …“ und „Lernen Schule: Startkarte …“ scheitern auch ohne diese Änderung). Prüfskript 96 von 96 OK.

## 2026-11-18 – FERTIG: Teil 3 (P2 Mischkarten) – App 0.77.0 – wartet auf Migration

**Migration** `supabase/migrations/20261118_w176_t3_mischkarten.sql` (nicht ausgeführt; pglast ok; Ersetzungsstellen im Live-Text je genau einmal vorhanden; setzt Teil 1 voraus; kein DROP, kein DELETE).
- Neu: `karte_stand.misch_ok_am`, `versuch.misch`, Regeln `misch_jede` = 4, `misch_jede_bis_kl6` = 6, `misch_ab_gelandet` = 3 (Startwerte in `schule.regel`).
- `schule.mischkarten(kind, einheit)`: je gelandeter Etappe des Kindes eine Übung (Pool `uebung`, Stufe 2–3, freigegeben; Entwürfe nur Testkind), am seltensten gesehen;
  Rang: gleicher Flug → gleicher Kontinent → älterer Flug; höchstens 8. Dynamisch je Kind, unabhängig vom Flugplan.
- `schule.misch_buchen` (über den Trigger `versuch_karte`, wenn `versuch.misch`): richtig im 1. Versuch ohne Tipp → `misch_ok_am`; endgültig falsch → wie ein Fehler in der Wiederholung
  (am nächsten Lerntag fällig, zwei hintereinander wie bisher); Tipp/2. Versuch richtig → nichts. Ist die Herkunfts-Etappe nicht gelandet, wird normal gebucht.
- „sicher“ (`karte_sicher`) verlangt jetzt zusätzlich `misch_ok_am`.
- **Keine neue Aktion in lernen-api.** Neue Felder: `schule_einheit_lesen`: `mischkarten[]` (Bordkarte + `einheit_id, lernziel, quelle, etappe, stadt`), `misch_jede`, `misch_ab`;
  `schule_uebung_pruefen` nimmt `misch: true` an und antwortet dann mit `misch: {lernziel, einheit_id, etappe, stadt, ok}` und **ohne** `karte`; `etappen_stand` und `schule_lernstand`: `misch_ok`.

**App 0.77.0** (ohne Migration: keine Mischkarten, alles wie bisher)
- Start, wenn im aktuellen Flug mindestens `misch_ab` (3) Etappen gelandet sind; dann jede `misch_jede`-te Bordkarte (4, bis Klasse 6: 6) eine Mischkarte; nie bei gewählter Stufe.
- Auswahl (`lernMischWahl`): gleicher Flug zuerst, dann Kontinent; jede 3. Mischkarte aus einem älteren Flug; nie die gerade geübte Etappe, nie Knobel-Bordkarten; jede Karte höchstens einmal je Sitzung.
- Anzeige neutral: „BORDKARTE n · AUS DEINER REISE“, „Aus deiner Reise – erkennst du, was gefragt ist?“, kein Link zur Erklärung, kein Etappen-Muster im Detektiv;
  nach der Lösung „Das war: <Etappe> – <Stadt>“. Die Checkliste der aktuellen Etappe bleibt unverändert.
- Eltern: „Was wackelt?“ zeigt „in einer Mischkarte erkannt ✓“. Info-Seite (Mischkarten, „sicher“) und README (Mischkarten; Übungen müssen für sich allein verständlich sein) angepasst.

**Rauchtest** `supabase/tests/w176_t3_rauchtest.sql` (nach dem Einspielen; Rollback; nur Testkind): ohne gelandete Etappe keine Mischkarte · nur gelandete Etappen, Pool uebung, Stufe 2–3, freigegeben ·
richtig → Beleg, Wiederholung unverändert · falsch → am nächsten Lerntag fällig, bleibt gelandet · Versuch mit `misch` angenommen · keine Knobel- oder gesperrten Bordkarten.
**Tests:** lernen 57 von 57 (neu: Auswahlregeln inkl. weniger als 3 gelandet, Dosis jede 6.; Mischkarte beim Üben mit Kennzeichnung, ohne Erklärung, „Das war …“, `misch: true`, aktuelle Etappe unverändert,
kein Knobel). Suche: 9 bekannte alte Fehler.
**Nicht geprüft:** Migration gegen echte Daten (Rauchtest nach dem Einspielen). Die Grenze „höchstens 6 Wiederholungen vor einem Flug“ ist unverändert (Mischkarten sind keine Wiederholungen;
eine falsche Mischkarte macht die Etappe nur fällig).

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

