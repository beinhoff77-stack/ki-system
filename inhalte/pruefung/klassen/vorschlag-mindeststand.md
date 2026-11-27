# Mindeststand je Jahrgang – Vorschlag für den Plan (Einundzwanzigste Runde, Teil B)

Stand: 2026-11-18. Zweig `plan-mindeststand`. **Nur ein Vorschlag.** Nichts an `themenliste.json`, Themendateien, Generatoren, Datenbank oder App geändert. Kein Merge.

**Ziel (Auftrag 17.11.):** Am Ende jeder Klasse hat ein Kind mindestens den Stand von Gymnasium **und** Realschule Bayern. Gymnasium ist die Basis; hat die Realschule ein Thema früher, gilt die frühere Klasse. IB MYP läuft nebenbei und zieht keinen Gymnasium-Stoff nach vorn.

**Wörter in dieser Datei**
- **Plan-Klasse** = Klasse, in der das Thema im neuen Plan liegt. **Gym** = `klasse.gym_by`, **RS** = `klasse.rs_by`, **IB** = `klasse.ib_myp` (MYP-Jahr; MYP 1 ≈ Klasse 6).
- **RS korr.** = Realschul-Klasse nach den 7 beschlossenen Korrekturen und 5 beschlossenen Nachträgen aus `vorschlag-rsib.md`.
- **Ort** = Block (Stadt) mit `ziel_klasse`; **Kontinent** = Gebiet. **Flug** = Thema, **Etappe** = Lernkarte.

**Grundlagen (Tatsachen, gelesen am 18.11.2026)**
- `inhalte/themenliste.json` (Zweig `lernen-app`, Commit d71b0c3): 95 Themen; 71 mit Gym-Klasse, 10 nur mit RS, 10 nur mit IB, 4 ohne Klasse.
- `inhalte/pruefung/klassen/vorschlag-rsib.md` (Zweig `lernen-app`) und `inhalte/pruefung/klassen/vorschlag.md` (Zweig `daten-klassen`, D1/D2).
- Datenbank, nur gelesen: `schule.block` (66 Orte mit `ziel_klasse`, Kontinent, Koordinaten), `schule.block_thema` (stimmt mit `block_id` der Themenliste überein), `schule.einheit` (Status). **Freigegeben sind genau die 71 Gymnasium-Themen; die 24 übrigen sind `entwurf`.**
- Etappen-Titel, Merksätze und Aufgabentexte aus `inhalte/themen/*.json`.

**Wie sicher ist das?**
- Gesichert: alle Zahlen und Zuordnungen, die aus Themenliste, Datenbank und den beiden Vorschlägen folgen (Punkt 1, 4, 7 rechnerisch nachgeprüft, Rechenweg im Postfach).
- Annahme: Vorwissen (Punkt 3, 5) habe ich an Etappen-Titeln, Merksätzen und Stichproben der Aufgabentexte festgemacht, nicht an jeder Aufgabe.
- Annahme: Verteilung der IB-Themen (Punkt 2) und Inhalt der neuen Themen (Punkt 6) – fachliche Einschätzung, keine Vorgabe aus einem Lehrplan.
- Meinung: alles, was mit „Empfehlung“ oder „Meinung“ markiert ist.
- **Abhängigkeit von Teil A** (läuft parallel, Zweig `bereinigen`): Teil A legt Paare zusammen und verschiebt Etappen. Ergebnisse von Teil A sind hier noch nicht eingerechnet; wo sie sich berühren, steht es dabei.

---

## Kurzfassung

| Klasse | Flüge heute (Gym) | Flüge im Plan | dazu | weg (nach vorn gezogen) | davon IB-Zusatz | + neue Themen (Punkt 6) |
|---|---|---|---|---|---|---|
| 5 | 14 | **16** | 2 | 0 | 0 | – |
| 6 | 11 | **15** | 5 | 1 | 3 | – |
| 7 | 9 | **16** | 9 | 2 | 3 | – |
| 8 | 14 | **16** | 6 | 4 | 3 | 1 |
| 9 | 14 | **21** | 7 | 0 | 2 | 1 |
| 10 | 9 | **11** | 5 | 3 | 3 | 2 |
| **Summe** | **71** | **95** | 34 | 10 | 14 | 4 |

- 10 Gymnasium-Themen rutschen wegen der Realschule nach vorn (Punkt 3). Bei 5 davon greifen einzelne Etappen oder Aufgaben vor; eine Etappe verschieben bzw. Aufgaben sperren reicht (bei `abbildungen.kongruenz` erledigt das Teil A).
- 15 Orte bekommen eine (andere) Klasse, 6 Flüge ziehen an einen anderen Ort, 1 neuer Ort (Accra) für ein neues Thema. Danach hat jeder Ort genau eine Klasse; kein Ort hat mehr als 4 Flüge (nur Rom hat 4, wie heute).
- Klasse 9 wird mit 21 Flügen die schwerste (heute 14). Meinung: vertretbar, weil 5 davon kurze RS-Themen sind; sonst `funktionen.betrag` nach 10 (Punkt 2).

---

## Punkt 1 – Plan-Klasse je Thema (alle 95)

Regel: Plan-Klasse = Gym-Klasse; ist RS korr. kleiner, gilt RS korr.; ohne Gym-Klasse gilt RS korr.; ohne Gym und ohne RS → Punkt 2.
Spalte **Nr.** = vorgeschlagene Reihenfolge in der Plan-Klasse (Punkt 5). Spalte IB: Wert heute, in Klammern der Vorschlag aus `vorschlag-rsib.md` Teil 3 (nicht beschlossen, nur zur Information).

| Nr. | Thema | Gym | RS (alt → korr.) | IB heute (→ Vorschl. rsib) | Plan | Grund |
|---|---|---|---|---|---|---|
| | **Klasse 5** | | | | | |
| 1 | `zahlen.natuerlich` | 5 | – → **5** | – (→ 1) | **5** | Gymnasium; RS nachgetragen |
| 2 | `zahlen.ganz` | 5 | 5 | 2 | **5** | Gymnasium |
| 3 | `geometrie.grundbegriffe` | 5 | 5 | 1 | **5** | Gymnasium |
| 4 | `geometrie.ortslinien` | 5 | 7 | – | **5** | Gymnasium |
| 5 | `geometrie.winkel` | 5 | 5 | 1 | **5** | Gymnasium |
| 6 | `zahlen.rechengesetze` | 5 | 5 | 1 | **5** | Gymnasium |
| 7 | `zahlen.potenzen_basis` | 5 | 5 | 1 | **5** | Gymnasium |
| 8 | `zahlen.teilbarkeit` | 5 | – → **5** | – (→ 1) | **5** | Gymnasium; RS nachgetragen |
| 9 | `stochastik.kombinatorik` | 5 | 5 | 2 | **5** | Gymnasium |
| 10 | `daten.darstellen` | 6 | 5 | 1 | **5** | RS früher (Gym 6) → Punkt 3 |
| 11 | `gleichungen.einfach` | 5 | 6 | 1 | **5** | Gymnasium |
| 12 | `groessen.einheiten` | 5 | 5 | 2 | **5** | Gymnasium |
| 13 | `groessen.proportional` | 5 | 5 → **6** | 2 | **5** | Gymnasium; RS-Korrektur |
| 14 | `messen.flaechen` | 5 | 5 | 1 | **5** | Gymnasium |
| 15 | `messen.koerper_berechnung` | 5 | 6 | 1 | **5** | Gymnasium |
| 16 | `messen.koerper_darstellung` | 8 | 5 | 3 | **5** | RS früher (Gym 8) → Punkt 3 |
| | **Klasse 6** | | | | | |
| 1 | `bruch.brueche` | 6 | 6 | 1 | **6** | Gymnasium |
| 2 | `bruch.dezimal` | 6 | 6 | 1 | **6** | Gymnasium |
| 3 | `bruch.rechnen` | 6 | 6 | 1 (→ 2) | **6** | Gymnasium |
| 4 | `terme.aufstellen` | 7 | 6 | 1 | **6** | RS früher (Gym 7) → Punkt 3 |
| 5 | `abbildungen.kongruenz` | 7 | 6 | 3 | **6** | RS früher (Gym 7) → Punkt 3 |
| 6 | `messen.flaechen_vielecke` | 6 | – | – | **6** | Gymnasium |
| 7 | `messen.volumen` | 6 | – | – | **6** | Gymnasium |
| 8 | `zahlen.potenzen_zehner` | 6 | 5 → **7** | 3 (→ 4) | **6** | Gymnasium; RS-Korrektur |
| 9 | `terme.potenzgesetze` | 6 | 7 | 3 | **6** | Gymnasium |
| 10 | `groessen.verhaeltnisse` | – | – | 2 | **6** | nur IB/ohne Klasse → Punkt 2 |
| 11 | `bruch.prozent` | 6 | 6 | 1 | **6** | Gymnasium |
| 12 | `finanzen.zinsen` | 6 | – → **7** | – (→ 4) | **6** | Gymnasium; RS nachgetragen |
| 13 | `daten.kennwerte` | 6 | 7 | 2 | **6** | Gymnasium |
| 14 | `mengen.grundbegriffe` | – | – | 1 (→ 3) | **6** | nur IB/ohne Klasse → Punkt 2 |
| 15 | `sonder.graphentheorie` | – | – | 4 | **6** | nur IB/ohne Klasse → Punkt 2 |
| | **Klasse 7** | | | | | |
| 1 | `terme.umformen` | 7 | – → **7** | – (→ 3) | **7** | Gymnasium; RS nachgetragen |
| 2 | `abbildungen.vektoren` | – | 7 | – | **7** | nur Realschule |
| 3 | `abbildungen.determinanten2` | – | 7 | – | **7** | nur Realschule |
| 4 | `geometrie.winkelsaetze` | 7 | – → **7** | – (→ 2) | **7** | Gymnasium; RS nachgetragen |
| 5 | `gleichungen.linear` | 7 | 7 | 2 | **7** | Gymnasium |
| 6 | `zahlen.intervalle` | 8 | 7 | – (→ 4) | **7** | RS früher (Gym 8) → Punkt 3 |
| 7 | `gleichungen.ungleichungen` | 8 | 7 | 2 (→ 4) | **7** | RS früher (Gym 8) → Punkt 3 |
| 8 | `sonder.logik` | – | – | – (→ 4) | **7** | nur IB/ohne Klasse → Punkt 2 |
| 9 | `bruch.prozent_grundwert` | 7 | 7 | – (→ 3) | **7** | Gymnasium |
| 10 | `finanzen.zinseszins` | – | – | – (→ 4) | **7** | nur IB/ohne Klasse → Punkt 2 |
| 11 | `groessen.indirekt` | 8 | 7 | – (→ 4) | **7** | RS früher (Gym 8) → Punkt 3 |
| 12 | `zahlen.schranken` | – | – | – (→ 5) | **7** | nur IB/ohne Klasse → Punkt 2 |
| 13 | `daten.boxplot` | 7 | 7 | 2 (→ 4) | **7** | Gymnasium |
| 14 | `daten.stichproben` | – | 7 | – (→ 2) | **7** | nur Realschule |
| 15 | `geometrie.konstruktion` | 7 | 6 → **7** | 3 | **7** | Gymnasium; RS-Korrektur |
| 16 | `geometrie.kreis` | 7 | 7 | 4 | **7** | Gymnasium |
| | **Klasse 8** | | | | | |
| 1 | `funktionen.grundbegriffe` | 8 | 8 | 1 (→ 4) | **8** | Gymnasium |
| 2 | `funktionen.linear` | 8 | 8 | 3 | **8** | Gymnasium |
| 3 | `funktionen.scharen` | – | 8 | – | **8** | nur Realschule |
| 4 | `daten.zweidimensional` | – | – | 3 (→ 5) | **8** | nur IB/ohne Klasse → Punkt 2 |
| 5 | `funktionen.folgen` | – | – | 4 (→ 5) | **8** | nur IB/ohne Klasse → Punkt 2 |
| 6 | `terme.quadratische_extreme` | – | 8 | – | **8** | nur Realschule |
| 7 | `funktionen.gebrochen` | 8 | – | 4 | **8** | Gymnasium |
| 8 | `terme.bruchterme` | 8 | 8 | – (→ 4) | **8** | Gymnasium |
| 9 | `gleichungen.bruch` | 8 | 8 | – (→ 4) | **8** | Gymnasium |
| 10 | `gleichungen.formeln` | 8 | – | – (→ 4) | **8** | Gymnasium |
| 11 | `stochastik.grundbegriffe` | 8 | 8 → **9** | 2 | **8** | Gymnasium; RS-Korrektur |
| 12 | `gleichungen.lgs2` | 8 | 9 | 3 (→ 4) | **8** | Gymnasium |
| 13 | `sonder.optimierung` | – | – | 4 (→ 5) | **8** | nur IB/ohne Klasse → Punkt 2 |
| 14 | `messen.kreisberechnung` | 8 | 9 | 2 (→ 3) | **8** | Gymnasium |
| 15 | `messen.prisma_zylinder` | 8 | – | – | **8** | Gymnasium |
| 16 | `raum.schraegbilder` | 10 | 5 → **8** | 4 | **8** | RS früher (Gym 10) → Punkt 3; RS-Korrektur |
| | **Klasse 9** | | | | | |
| 1 | `zahlen.wurzeln_basis` | 9 | 9 | 1 | **9** | Gymnasium |
| 2 | `zahlen.reell` | 9 | 9 | 3 (→ 4) | **9** | Gymnasium |
| 3 | `gleichungen.reinquadratisch` | – | 9 | – (→ 4) | **9** | nur Realschule |
| 4 | `funktionen.transformation` | – | 9 | – (→ 5) | **9** | nur Realschule |
| 5 | `funktionen.quadratisch` | 9 | 8 → **9** | 4 | **9** | Gymnasium; RS-Korrektur |
| 6 | `gleichungen.quadratisch` | 9 | 9 | 4 | **9** | Gymnasium |
| 7 | `funktionen.betrag` | – | – | 4 (→ 5) | **9** | nur IB/ohne Klasse → Punkt 2 |
| 8 | `gleichungen.wurzel` | – | 9 | – | **9** | nur Realschule |
| 9 | `gleichungen.lgs3` | 9 | – | – | **9** | Gymnasium |
| 10 | `stochastik.verknuepft` | 9 | 8 → **9** | 4 | **9** | Gymnasium; RS-Korrektur |
| 11 | `stochastik.simulation` | 10 | 9 | 2 | **9** | RS früher (Gym 10) → Punkt 3 |
| 12 | `daten.standardabweichung` | – | – | 4 (→ 5) | **9** | nur IB/ohne Klasse → Punkt 2 |
| 13 | `abbildungen.aehnlichkeit` | 9 | 9 | 3 | **9** | Gymnasium |
| 14 | `zahlen.rationale_exponenten` | 9 | 10 | – (→ 5) | **9** | Gymnasium |
| 15 | `funktionen.potenz` | 9 | 10 | 4 | **9** | Gymnasium |
| 16 | `gleichungen.potenz` | 9 | 10 | – (→ 4) | **9** | Gymnasium |
| 17 | `trigo.pythagoras` | 9 | 9 | 3 | **9** | Gymnasium |
| 18 | `raum.pyramide_kegel_kugel` | 10 | 9 | 3 | **9** | RS früher (Gym 10) → Punkt 3 |
| 19 | `trigo.rechtwinklig` | 9 | 9 | 3 (→ 4) | **9** | Gymnasium |
| 20 | `trigo.allgemein` | 9 | 10 | 4 | **9** | Gymnasium |
| 21 | `gleichungen.trig` | 9 | 10 | – (→ 5) | **9** | Gymnasium |
| | **Klasse 10** | | | | | |
| 1 | `funktionen.exponential_log` | 10 | 10 | 4 (→ 5) | **10** | Gymnasium |
| 2 | `gleichungen.exponential` | 10 | 10 | – (→ 5) | **10** | Gymnasium |
| 3 | `funktionen.umkehr` | – | 10 | 4 (→ 5) | **10** | nur Realschule |
| 4 | `funktionen.reihen` | – | – | 4 (→ 5) | **10** | nur IB/ohne Klasse → Punkt 2 |
| 5 | `stochastik.mehrstufig` | 10 | 10 | – (→ 4) | **10** | Gymnasium |
| 6 | `stochastik.bedingt` | – | – | 4 (→ 5) | **10** | nur IB/ohne Klasse → Punkt 2 |
| 7 | `daten.normalverteilung` | – | – | – (→ 5) | **10** | nur IB/ohne Klasse → Punkt 2 |
| 8 | `funktionen.trig` | 10 | 10 | 4 (→ 5) | **10** | Gymnasium |
| 9 | `abbildungen.matrizen` | – | 10 | 4 (→ 5) | **10** | nur Realschule |
| 10 | `funktionen.ganzrational` | 10 | – | 4 (→ 5) | **10** | Gymnasium |
| 11 | `gleichungen.polynom` | 10 | – | – | **10** | Gymnasium |

**Ergebnis Punkt 1 (Tatsache, gerechnet):** 61 Themen behalten ihre Gym-Klasse, 10 rutschen wegen der Realschule nach vorn, 10 nur-RS-Themen übernehmen ihre RS-Klasse, 14 Themen ohne Gym/RS kommen aus Punkt 2.
Die RS-Korrekturen ändern die Plan-Klasse nur bei `raum.schraegbilder` (ohne Korrektur wäre es 5 statt 8). Bei den übrigen 6 Korrekturen ist die Gym-Klasse ohnehin kleiner oder gleich.

**Drei neue Themen seit `vorschlag-rsib.md`** (Ort Quito und Cusco, seit 17.11. in der Themenliste): `messen.flaechen_vielecke` (Gym 6), `messen.volumen` (Gym 6), `messen.prisma_zylinder` (Gym 8). Sie haben kein `rs_by`. Annahme nach `vorschlag-rsib.md` Teil 2 Nr. 4, 5, 14: RS 6, 6 und 9. An der Plan-Klasse ändert das nichts; `rs_by` nachtragen wäre ein eigener Beschluss.

---

## Punkt 2 – IB läuft nebenbei: die 14 Themen ohne Gym- und RS-Klasse

Regel: kein Gymnasium-Stoff wird nach vorn gezogen; je Klasse höchstens 3 IB-Flüge; Vorwissen muss in derselben oder einer früheren Klasse liegen. Die IB-Jahresangabe ist nur Anhaltspunkt (MYP 1 ≈ Kl. 6).

| Thema | IB heute (→ rsib) | Plan-Klasse | Vorwissen (Thema, Plan-Klasse) | Grund |
|---|---|---|---|---|
| `mengen.grundbegriffe` | 1 (→ 3) | **6** | nur natürliche Zahlen; Venn-Diagramm neu | früh möglich; Grundlage für `stochastik.verknuepft` (9) und `stochastik.bedingt` (10). Kl. 5 ginge auch, Kl. 5 ist aber schon mit 16 Flügen voll. |
| `groessen.verhaeltnisse` | 2 | **6** | `groessen.proportional` (5), `bruch.brueche` (6) | Kürzen von Verhältnissen braucht Bruchdenken; Änderungsraten mit negativem Wert brauchen `zahlen.ganz` (5). Nach den Brüchen. |
| `sonder.graphentheorie` | 4 | **6** | nur natürliche Zahlen (Grade, Wege addieren) | kein Rechenvorwissen; Knobelstoff. Steht am selben Ort wie die Mengen (Galápagos, Punkt 4) und macht dort keinen neuen Ort nötig. |
| `finanzen.zinseszins` | – (→ 4) | **7** | `finanzen.zinsen` (6), `bruch.prozent_grundwert` (7), `zahlen.potenzen_basis` (5) | Der Wachstumsfaktor q = 1 + p/100 ist genau der „vermehrte Grundwert“ aus Kl. 7. Verdopplungszeit wird durch Probieren gelöst, kein Logarithmus nötig. |
| `zahlen.schranken` | – (→ 5) | **7** | Runden (5), Dezimalzahlen (6) | Rechnen nur mit Dezimalzahlen und Vergleichen; IB stuft es als „Extended“ ein, mathematisch reicht Kl. 7. |
| `sonder.logik` | – (→ 4) | **7** | `gleichungen.linear`, `zahlen.intervalle` (7) | Etappe „Aussagen“ nutzt offene Sätze mit x; deshalb nach den Gleichungen. |
| `daten.zweidimensional` | 3 (→ 5) | **8** | `funktionen.linear` (8), `daten.kennwerte` (6) | Ausgleichsgerade braucht Geraden mit Steigung. |
| `funktionen.folgen` | 4 (→ 5) | **8** | `funktionen.linear` (8), `terme.aufstellen` (6), `zahlen.potenzen_basis` (5) | arithmetische Folge = lineare Funktion auf ℕ; geometrische Folge braucht nur Potenzen. |
| `sonder.optimierung` | 4 (→ 5) | **8** | `gleichungen.ungleichungen` (7), `funktionen.linear`, `gleichungen.lgs2` (8) | Eckpunkte = Gleichungssystem mit 2 Unbekannten; am Ende von Kl. 8. Kl. 9 wäre fachlich auch richtig, ist aber schon voll. |
| `daten.standardabweichung` | 4 (→ 5) | **9** | `daten.kennwerte` (6), `zahlen.wurzeln_basis` (9) | σ ist eine Wurzel. |
| `funktionen.betrag` | 4 (→ 5) | **9** | `funktionen.transformation` (9), `gleichungen.linear` (7) | a · \|x − d\| + e ist dieselbe Verschiebungslogik wie bei der Scheitelform. Ausweichklasse 10, falls Kl. 9 entlastet werden soll. |
| `stochastik.bedingt` | 4 (→ 5) | **10** | `stochastik.verknuepft` (9), `stochastik.mehrstufig` (10), `mengen.grundbegriffe` (6) | „Ziehen ohne Zurücklegen“ braucht Baumdiagramme aus Kl. 10. Hinweis: Teil A (A2) schiebt die Etappe `stochastik.verknuepft`/bedingt als Oberstufen-Stoff hinaus – hierher würde sie passen. |
| `funktionen.reihen` | 4 (→ 5) | **10** | `funktionen.folgen` (8), `funktionen.exponential_log` (10) | geometrische Reihe neben exponentiellem Wachstum. |
| `daten.normalverteilung` | – (→ 5) | **10** | `daten.standardabweichung` (9) | braucht μ und σ. |

**IB-Flüge je Klasse:** 5: 0 · 6: 3 · 7: 3 · 8: 3 · 9: 2 · 10: 3 (Regel höchstens 2–3 eingehalten).

**Zur Kenntnis, ohne Folge für den Plan – Gymnasium-Themen, die IB früher hat** (IB-Jahr nach `vorschlag-rsib.md`, umgerechnet MYP-Jahr + 5):

| Thema | Gym | IB-Jahr | ≈ Klasse | Plan-Klasse |
|---|---|---|---|---|
| `zahlen.wurzeln_basis` | 9 | 1 | 6 | 9 |
| `terme.aufstellen` | 7 | 1 | 6 | 6 (wegen RS) |
| `stochastik.grundbegriffe` | 8 | 2 | 7 | 8 |
| `stochastik.simulation` | 10 | 2 | 7 | 9 (wegen RS) |
| `abbildungen.aehnlichkeit` | 9 | 3 | 8 | 9 |
| `trigo.pythagoras` | 9 | 3 | 8 | 9 |
| `raum.pyramide_kegel_kugel` | 10 | 3 | 8 | 9 (wegen RS) |
| `raum.schraegbilder` | 10 | 4 | 9 | 8 (wegen RS) |
| `stochastik.mehrstufig` | 10 | 4 (Nachtrag) | 9 | 10 |

Annahme: Die IB-Jahre sind schwach belegt (Lehrwerk Haese, nicht Vorgabe des IB; siehe `vorschlag-rsib.md` „Wie sicher ist das?“). `zahlen.wurzeln_basis` in MYP 1 ist dort selbst als Annahme markiert.

---

## Punkt 3 – Vorwissen der 10 Themen, die nach vorn rutschen

Geprüft: Welche Themen setzt das Thema voraus, und liegen sie im neuen Plan davor (frühere Klasse oder früher in derselben Klasse, Reihenfolge aus Punkt 5)?

| Thema | Gym → Plan | braucht | liegt davor? | Vorschlag |
|---|---|---|---|---|
| `daten.darstellen` | 6 → 5 | Strichliste, Säulen (Kl. 5); **Bruch** für „Relative Häufigkeit“ (Antwort als Bruch □/□); **Prozent** für „Kreisdiagramme berechnen“ (Winkel für 65 %); Winkel (5) | **nein** für 2 Etappen: `bruch.brueche` und `bruch.prozent` sind Kl. 6 | **Thema lassen (Kl. 5), 2 Etappen nach hinten**: `relative_haeufigkeit` → `bruch.brueche` (Kl. 6), `kreisdiagramm` → `bruch.prozent` (Kl. 6), Schlüssel `l` behalten. Bei `tabelle_auswerten` greifen 10 von 42 Aufgaben mit Anteil/Prozent vor → für Kl. 5 sperren oder nach Stufe 3. „Voraussetzung mitziehen“ scheidet aus: Brüche nach Kl. 5 zu holen widerspräche Gym **und** RS. |
| `gleichungen.ungleichungen` | 8 → 7 | `gleichungen.linear` (7, davor), `zahlen.intervalle` (7, davor); Etappe „Ungleichung am Graphen lösen“ braucht **Geraden** `funktionen.linear` (8) | **nein** für Etappe `grafisch` | **Thema lassen (Kl. 7)**; Etappe `grafisch` nach `funktionen.linear` (8) verschieben oder als Vertiefung führen. `klammern` passt: Gym M7 3 hat x auf beiden Seiten. (RS hat diese Etappe erst in Kl. 8 – für den Mindeststand unschädlich.) |
| `zahlen.intervalle` | 8 → 7 | Zahlenstrahl, ganze Zahlen (5), Ungleichheitszeichen | ja | keine Änderung |
| `messen.koerper_darstellung` | 8 → 5 | Quader/Würfel (5), Umfang (5); **Kreisumfang mit π** in Etappe `zylinder` (8 von 34 Aufgaben mit π); **Dreiecksfläche** in 7 von 34 Netz-Aufgaben (Prisma mit Dreiecksgrundfläche) | **nein**: `messen.kreisberechnung` (8), `messen.flaechen_vielecke` (6) | **Thema lassen (Kl. 5), Etappe `zylinder` nach hinten** zu `messen.prisma_zylinder` (Kl. 8, hat schon „Zylinder: Oberfläche über das Netz“ – das ist zugleich das Teil-A-Paar `messen.kreisberechnung`/zylinder ↔ `messen.prisma_zylinder`). Die 7 Netz-Aufgaben mit Dreieck für Kl. 5 sperren oder nach Stufe 3. Hinweis Teil A: Das Paar `koerper_darstellung` ↔ `raum.schraegbilder` (Schrägbild q = 1/2, Ecken/Kanten/Flächen) bleibt dann bei `koerper_darstellung`, weil es dort zuerst gebraucht wird. |
| `raum.schraegbilder` | 10 → 8 | Schrägbild-Regeln aus `messen.koerper_darstellung` (5), Kreis (`messen.kreisberechnung`, 8, davor), Dreiecksfläche (6) | ja, bis auf 2 Aufgaben mit Wurzel/Pythagoras (Würfeldiagonale, Mantellinie im Axialschnitt) | Thema in Kl. 8 als letztes; die 2 Aufgaben sperren oder nach `raum.pyramide_kegel_kugel` (9). Vertiefungs-Etappen `lage`, `koordinaten` bleiben Vertiefung. |
| `stochastik.simulation` | 10 → 9 | `stochastik.grundbegriffe` (8), Kreisfläche für Monte-Carlo (`messen.kreisberechnung`, 8), Prozent (6) | ja | keine Änderung. Teil A legt die π-Schätzung aus `stochastik.mehrstufig` hierher zusammen – passt, weil Simulation jetzt früher liegt. |
| `terme.aufstellen` | 7 → 6 | ganze Zahlen (5), Termwert mit negativen Zahlen (5), Dezimalzahlen in Sachterm (`bruch.dezimal`, 6) | ja, wenn nach `bruch.dezimal` | keine Änderung; in Kl. 6 nach den Brüchen (Punkt 5). |
| `abbildungen.kongruenz` | 7 → 6 | Koordinatensystem, Winkel, besondere Vierecke (alle Kl. 5) | ja; **aber** Etappe `achsenspiegelung` nutzt Geradengleichungen (x = 3, y = x) und `parkett` (Vertiefung) Innenwinkel aus `geometrie.winkelsaetze` (7) | Thema lassen (Kl. 6). Beides beseitigt Teil A (A2, Kl. 7). Punktspiegelung kommt damit für Gymnasiasten ein Jahr früher – kein Vorwissensproblem. |
| `raum.pyramide_kegel_kugel` | 10 → 9 | `trigo.pythagoras` (9), `abbildungen.aehnlichkeit` (9, Faktor k² und k³), `messen.prisma_zylinder` (8), Kreisausschnitt (`messen.kreisberechnung`, 8) | ja, wenn in Kl. 9 nach Pythagoras und Ähnlichkeit | keine Änderung; Platz in Punkt 5 entsprechend. |
| `groessen.indirekt` | 8 → 7 | Dreisatz (`groessen.proportional`, 5), Brüche (6), Punkte im Koordinatensystem (5) | ja | keine Änderung. Annahme: Die Schreibweise y = k : x in der Etappe `graph` ist ohne Funktionsbegriff (8) verständlich, weil nur Punkte abgelesen und geprüft werden (RS M7 hat den Hyperbelast). Teil A legt `funktionen.gebrochen` (indirekt, indirekt_sach) hierher zusammen – passt. |

**Auch geprüft – die 10 nur-RS-Themen** (Vorwissen liegt jeweils davor): `abbildungen.vektoren` (7) braucht Koordinatensystem, Verschiebung (`abbildungen.kongruenz`, 6) · `abbildungen.determinanten2` (7) nach `abbildungen.vektoren` · `daten.stichproben` (7) braucht Anteile/Prozent (6) · `funktionen.scharen` (8) nach `funktionen.linear` · `terme.quadratische_extreme` (8) braucht binomische Formeln (`terme.umformen`, 7) · `gleichungen.reinquadratisch` (9) nach `zahlen.wurzeln_basis` · `funktionen.transformation` (9) vor `funktionen.quadratisch` (wie in `vorschlag-rsib.md`, bewusst) · `gleichungen.wurzel` (9) nach `gleichungen.quadratisch` · `funktionen.umkehr` (10) nach `funktionen.exponential_log` · `abbildungen.matrizen` (10) nach `funktionen.trig` (Drehmatrix mit sin/cos).

---

## Punkt 4 – Orte

Regel wie in `vorschlag.md` (D1): Ort mit **einem** Flug bekommt die Klasse des Flugs. Ort mit **mehreren** Flügen verschiedener Klassen: der abweichende Flug zieht an einen bestehenden Ort derselben Klasse auf demselben Kontinent. Kein Ort mit mehr als 4 Flügen. Klassen der Orte: `schule.block.ziel_klasse` (Datenbank, 18.11.).

### 4a – Orte mit Gymnasium-Themen, deren Klasse nicht mehr passt

| Ort (Kontinent) | Klasse heute | Flüge (Plan-Klasse) | Vorschlag |
|---|---|---|---|
| Delhi (Algebra) | 8 | `zahlen.intervalle` (7) · `gleichungen.ungleichungen` (7) | **Delhi wird 7.** Kein Umzug. (Macht D2 für Delhi rückgängig.) |
| Teheran (Algebra) | 7 | `terme.aufstellen` (6) | **Teheran wird 6.** Kein Umzug. |
| Vancouver (Geld und Verhältnisse) | 8 | `groessen.indirekt` (7) | **Vancouver wird 7.** Kein Umzug. |
| Marrakesch (Geometrie) | 7 | `abbildungen.kongruenz` (6) | **Marrakesch wird 6.** Kein Umzug. |
| Adelaide (Daten und Zufall) | 6 | `daten.darstellen` (5) | **Adelaide wird 5.** Kein Umzug. Im Lernweg vor Melbourne (Zählen, 5) oder danach – beides geht. |
| Cusco (Fläche und Raum) | 8 | `messen.koerper_darstellung` (5) · `messen.prisma_zylinder` (8) | **Cusco bleibt 8.** `messen.koerper_darstellung` zieht nach **Rio de Janeiro** (5, „Volumen und Oberfläche“; dann 2 Flüge, Reihenfolge: `messen.koerper_berechnung` → `messen.koerper_darstellung`, weil die Netzfläche die Quader-Oberfläche braucht). Ortstitel Cusco: „Prismen und Zylinder“. |
| Brasília (Fläche und Raum) | 10 | `raum.schraegbilder` (8) | **Brasília wird 8.** Kein Umzug. Im Lernweg nach Buenos Aires und Cusco. |
| Santiago de Chile (Fläche und Raum) | 10 | `raum.pyramide_kegel_kugel` (9) | **Santiago wird 9.** Kein Umzug. |
| Darwin (Daten und Zufall) | 10 | `stochastik.simulation` (9) · `stochastik.mehrstufig` (10) | **Darwin bleibt 10.** `stochastik.simulation` zieht nach **Wellington** (9, „Verknüpfte Ereignisse“). Ortstitel Darwin: „Mehrstufiger Zufall“. |

### 4b – Die 24 Themen ohne Gymnasium-Klasse

| Thema | Plan | Ort heute (Klasse) | Vorschlag |
|---|---|---|---|
| `abbildungen.vektoren` | 7 | Lagos (7) | passt |
| `abbildungen.determinanten2` | 7 | Lagos (7) | passt |
| `daten.stichproben` | 7 | Perth (7) | passt |
| `funktionen.scharen` | 8 | Neumayer-Station III (8) | passt |
| `terme.quadratische_extreme` | 8 | Shanghai (8) | passt |
| `funktionen.transformation` | 9 | Wostok-Station (9) | passt |
| `gleichungen.reinquadratisch` | 9 | Seoul (9) | passt |
| `gleichungen.wurzel` | 9 | Tokio (9) | passt |
| `abbildungen.matrizen` | 10 | Dakar (10) | passt |
| `funktionen.umkehr` | 10 | Halley-Station (10) | passt |
| `mengen.grundbegriffe` | 6 | Galápagos-Inseln (–) | **Galápagos wird 6.** Ortstitel: „Mengen und Graphen“. |
| `sonder.graphentheorie` | 6 | Tahiti (–) | zieht nach **Galápagos-Inseln** (6, Entdecker-Inseln; dann 2 Flüge). Kein anderer Ort der Klasse 6 auf diesem Kontinent. |
| `sonder.optimierung` | 8 | Tahiti (–) | **Tahiti wird 8.** Ortstitel: „Lineare Optimierung“. |
| `groessen.verhaeltnisse` | 6 | San Francisco (–) | **San Francisco wird 6.** |
| `finanzen.zinseszins` | 7 | Boston (–) | **Boston wird 7.** |
| `sonder.logik` | 7 | Honolulu (–) | **Honolulu wird 7** (beide Flüge 7). |
| `zahlen.schranken` | 7 | Honolulu (–) | wie oben |
| `daten.zweidimensional` | 8 | Hobart (–) | **Hobart wird 8.** |
| `funktionen.folgen` | 8 | Palmer-Station (–) | **Palmer-Station wird 8.** Ortstitel: „Folgen“. |
| `funktionen.betrag` | 9 | Palmer-Station (–) | zieht nach **Wostok-Station** (9, „Parabeln“; dann 3 Flüge: transformation → quadratisch → betrag). Ortstitel Wostok: „Parabeln und Graphen verschieben“. |
| `funktionen.reihen` | 10 | Palmer-Station (–) | zieht nach **Halley-Station** (10; dann 3 Flüge). Grund: geometrische Reihe neben Exponentialfunktion. Alternative: Casey-Station (10, 1 Flug). |
| `daten.standardabweichung` | 9 | Suva (–) | zieht nach **Wellington** (9; dann 3 Flüge: verknüpft → Simulation → Standardabweichung). |
| `stochastik.bedingt` | 10 | Suva (–) | **Suva wird 10** (2 Flüge). Ortstitel bleibt „Statistik vertieft“ oder „Bedingte Wahrscheinlichkeit und Normalverteilung“. Alternative: nach Darwin zu `stochastik.mehrstufig`. |
| `daten.normalverteilung` | 10 | Suva (–) | wie oben |

**Ergebnis Punkt 4 (Tatsache, gerechnet):** 15 Orte bekommen eine (neue) Klasse, 6 Flüge ziehen um, kein neuer Ort für bestehende Themen nötig. Danach hat jeder der 66 Orte genau eine Klasse; größter Ort Rom mit 4 Flügen, sonst höchstens 3.

Nebenbefund (Tatsache): Durch „ein Ort = ein Flug = eine Klasse“ liegen auf einem Kontinent manchmal mehrere Orte derselben Klasse (z. B. Fläche und Raum: Cusco, Buenos Aires, Brasília alle 8). Das war schon in D1 so beschlossen (Entscheidung 5). Die Reihenfolge der Orte im Kontinent (`block.reihenfolge`) habe ich nicht neu vorgeschlagen; der Lernweg folgt Punkt 5.

---

## Punkt 5 – Reihenfolge je Klasse (Vorwissen zuerst)

Grundlage ist `reihenfolge.gym_by`; Realschul- und IB-Themen sind nach ihrem Vorwissen eingefügt. Die Nummern stehen auch in der Tabelle in Punkt 1. [neu] = neues Thema aus Punkt 6 (Vorschlag für den Platz).

- **5:** 1 `zahlen.natuerlich` · 2 `zahlen.ganz` · 3 `geometrie.grundbegriffe` · 4 `geometrie.ortslinien` · 5 `geometrie.winkel` · 6 `zahlen.rechengesetze` · 7 `zahlen.potenzen_basis` · 8 `zahlen.teilbarkeit` · 9 `stochastik.kombinatorik` · 10 `daten.darstellen` · 11 `gleichungen.einfach` · 12 `groessen.einheiten` · 13 `groessen.proportional` · 14 `messen.flaechen` · 15 `messen.koerper_berechnung` · 16 `messen.koerper_darstellung`
- **6:** 1 `bruch.brueche` · 2 `bruch.dezimal` · 3 `bruch.rechnen` · 4 `terme.aufstellen` · 5 `abbildungen.kongruenz` · 6 `messen.flaechen_vielecke` · 7 `messen.volumen` · 8 `zahlen.potenzen_zehner` · 9 `terme.potenzgesetze` · 10 `groessen.verhaeltnisse` · 11 `bruch.prozent` · 12 `finanzen.zinsen` · 13 `daten.kennwerte` · 14 `mengen.grundbegriffe` · 15 `sonder.graphentheorie`
- **7:** 1 `terme.umformen` · 2 `abbildungen.vektoren` · 3 `abbildungen.determinanten2` · 4 `geometrie.winkelsaetze` · 5 `gleichungen.linear` · 6 `zahlen.intervalle` · 7 `gleichungen.ungleichungen` · 8 `sonder.logik` · 9 `bruch.prozent_grundwert` · 10 `finanzen.zinseszins` · 11 `groessen.indirekt` · 12 `zahlen.schranken` · 13 `daten.boxplot` · 14 `daten.stichproben` · 15 `geometrie.konstruktion` · 16 `geometrie.kreis`
- **8:** 1 `funktionen.grundbegriffe` · 2 `funktionen.linear` · 3 `funktionen.scharen` · 4 `daten.zweidimensional` · 5 `funktionen.folgen` · 6 `terme.quadratische_extreme` · 7 `funktionen.gebrochen` · 8 `terme.bruchterme` · 9 `gleichungen.bruch` · 10 `gleichungen.formeln` · 11 `stochastik.grundbegriffe` · 12 `gleichungen.lgs2` · 13 `sonder.optimierung` · 14 `messen.kreisberechnung` · 15 `messen.prisma_zylinder` · 16 `raum.schraegbilder` · [neu] „Vierecke und Drehung“ nach 16
- **9:** 1 `zahlen.wurzeln_basis` · 2 `zahlen.reell` · 3 `gleichungen.reinquadratisch` · 4 `funktionen.transformation` · 5 `funktionen.quadratisch` · 6 `gleichungen.quadratisch` · 7 `funktionen.betrag` · 8 `gleichungen.wurzel` · 9 `gleichungen.lgs3` · 10 `stochastik.verknuepft` · 11 `stochastik.simulation` · 12 `daten.standardabweichung` · 13 `abbildungen.aehnlichkeit` · 14 `zahlen.rationale_exponenten` · 15 `funktionen.potenz` · 16 `gleichungen.potenz` · 17 `trigo.pythagoras` · 18 `raum.pyramide_kegel_kugel` · 19 `trigo.rechtwinklig` · 20 `trigo.allgemein` · 21 `gleichungen.trig` · [neu] „Zentrische Streckung im Koordinatensystem“ nach 13
- **10:** 1 `funktionen.exponential_log` · 2 `gleichungen.exponential` · 3 `funktionen.umkehr` · 4 `funktionen.reihen` · 5 `stochastik.mehrstufig` · 6 `stochastik.bedingt` · 7 `daten.normalverteilung` · 8 `funktionen.trig` · 9 `abbildungen.matrizen` · 10 `funktionen.ganzrational` · 11 `gleichungen.polynom` · [neu] „Graphen abbilden“ nach 3 · [neu] „Trigonometrie – Ergänzungen“ nach 8

Bewusste Abweichungen von der Gymnasium-Reihenfolge: Kl. 9 `funktionen.transformation` vor `funktionen.quadratisch` (wie `vorschlag-rsib.md`); `raum.pyramide_kegel_kugel` nach `trigo.pythagoras` (braucht die Mantelhöhe). Die Klasse-9-Korrekturen des Haupt-Chats (rationale Exponenten vor Potenzfunktionen, `trigo.allgemein` vor `gleichungen.trig`) sind übernommen.

---

## Punkt 6 – Fehlender Realschul-Stoff: neue Themen

Stand gegenüber `vorschlag-rsib.md` Teil 2 (Tatsache): Nr. 4 Flächeninhalt der Vielecke ist inzwischen da (`messen.flaechen_vielecke`, Quito), ebenso Nr. 5 Volumeneinheiten/Liter (`messen.volumen`) und der Prisma-Teil von Nr. 14 (`messen.prisma_zylinder`). Offen sind vier neue Themen:

| Thema (Vorschlag) | Plan-Klasse | Lehrplan | Ort | Lernkarten (Stichworte) |
|---|---|---|---|---|
| **Vierecke und Drehung** | 8 (RS 8; Gym ohne eigenes Thema) | RS M8 LB1 (I und II/III), M8 LB2 (I) | **neuer Ort Accra** (Ghana), Kontinent Geometrie, Titel „Vierecke und Drehung“, 5,60° N / 0,19° W – es gibt keinen Geometrie-Ort der Klasse 8 | 1 Haus der Vierecke: Eigenschaften von Seiten, Winkeln, Diagonalen · 2 Viereck aus Eigenschaften bestimmen · 3 Winkel im Viereck (Summe 360°, Drachen, Raute) · 4 Ist das Viereck konstruierbar? (Planfigur, Angaben zählen) · 5 Um einen Punkt drehen: Bildpunkt bei 90° und 180° · 6 Drehsymmetrie und Ordnung erkennen · 7 Vektor um ±90° und 180° drehen (Koordinaten) · 8 Was bleibt bei der Drehung gleich? |
| **Zentrische Streckung im Koordinatensystem** | 9 (RS 9 Gruppe I) | RS M9 LB2 (I) | **Nairobi** (9, „Ähnlichkeit“; dann 2 Flüge, nach `abbildungen.aehnlichkeit`) | 1 Zahl mal Vektor · 2 Bildpunkt berechnen: Z + k · ZP · 3 Streckungsfaktor aus Punkt und Bildpunkt · 4 negativer Faktor: durch Z hindurch · 5 Bildgerade und Bildparabel (Parameterverfahren) · 6 Strecke im Verhältnis teilen, Goldener Schnitt · 7 Schwerpunkt des Dreiecks rechnerisch · 8 Flächen mal k² prüfen |
| **Trigonometrie – Ergänzungen** | 10 (RS 10 Gruppe I) | RS M10 LB1 (I) | **Dakar** (10, „Matrizen und Skalarprodukt“; dann 2 Flüge) | 1 Steigungswinkel: m = tan α · 2 Schnittwinkel zweier Geraden · 3 Graph der Tangensfunktion · 4 sin(90° − α) = cos α, sin(180° − α) = sin α · 5 sin² α + cos² α = 1 anwenden · 6 Additionstheoreme sin(α ± β), cos(α ± β) · 7 Winkel zwischen zwei Vektoren (Skalarprodukt) · 8 Abstand Punkt–Gerade |
| **Graphen abbilden: Potenz-, Exponential- und Logarithmusfunktionen** (weiteres) | 10 (RS 10 Gruppe I) | RS M10 LB2 (I) | **Casey-Station** (10, „Ganzrationale Funktionen“; dann 2 Flüge) | 1 Verschieben: y = f(x − d) + e · 2 Strecken und Stauchen: y = a · f(x) · 3 Spiegeln an den Achsen · 4 Asymptoten mitverschieben · 5 Gleichung aus dem Graphen: y = k · a^(x − b) + c · 6 Logarithmusfunktion mit Parametern · 7 Definitions- und Wertemenge nach der Abbildung |

Vorwissen der neuen Themen: Vierecke und Drehung ← `geometrie.grundbegriffe` (5), `abbildungen.kongruenz` (6), `geometrie.konstruktion` (7), `abbildungen.vektoren` (7). Zentrische Streckung im KS ← `abbildungen.vektoren` (7), `abbildungen.aehnlichkeit` (9), `funktionen.quadratisch` (9). Trigonometrie-Ergänzung ← `trigo.allgemein` (9), `funktionen.trig` (10), `abbildungen.vektoren` (7). Graphen abbilden ← `funktionen.transformation` (9), `funktionen.potenz` (9), `funktionen.exponential_log` (10).

Überschneidungen (Tatsache, zur Beachtung beim Bau): Drehung ist heute Vertiefungs-Etappe in `abbildungen.kongruenz`; „Haus der Vierecke“ steht als Etappe in `abbildungen.kongruenz` (`vierecke_ordnen`) und `geometrie.grundbegriffe` (`vierecke`). Additionstheoreme stehen im `umfang` von `trigo.allgemein`, aber in keiner Etappe.

**Nur erweitern, kein neues Thema** (aus `vorschlag-rsib.md` Teil 2, Dringlichkeit dort): Dualsystem → `zahlen.natuerlich` (Nr. 2) · Kegel/Kugel/Zylinder beschreiben → `messen.koerper_darstellung` (Nr. 3) · Raumgeometrie Winkel/wahre Größe → `raum.schraegbilder` (Nr. 6) · Ortslinien vollständig → `geometrie.ortslinien`, `geometrie.kreis` (Nr. 7) · Symmetrieebenen → `raum.schraegbilder` (Nr. 10) · Betrag eines Vektors → `trigo.pythagoras` (Nr. 13) · Cavalieri, Extremwerte bei Körpern → `raum.pyramide_kegel_kugel` (Nr. 14) · Parabelscharen → `funktionen.scharen`/`funktionen.quadratisch` (Nr. 15) · Logarithmensätze → `gleichungen.exponential` (Nr. 18) · Potenzfunktionen mit Asymptoten → `funktionen.gebrochen` (Nr. 19).

Meinung: Bei „Vierecke und Drehung“ wären zwei kleine Flüge (je 4–5 Etappen) sauberer als einer mit 8. Der Auftrag nennt sie zusammen; ich habe es als einen Flug vorgeschlagen.

---

## Punkt 7 – Folgen für zwei Kinder

Annahme: Beide Kinder folgen heute dem Gymnasium-Plan (71 Flüge nach `gym_by`). „Kommt dazu“ = Saldo neuer Plan minus heutiger Plan je Klasse. Die neuen Themen aus Punkt 6 stehen getrennt, weil es sie noch nicht gibt.

**Kind A (Klasse 5)** – alle Klassen liegen noch vor ihm:

| Klasse | heute | neu | Saldo | davon heute freigegeben | + neue Themen |
|---|---|---|---|---|---|
| 5 | 14 | 16 | +2 | 2 (`daten.darstellen`, `messen.koerper_darstellung`) | – |
| 6 | 11 | 15 | +4 | 2 von 5 neuen (`terme.aufstellen`, `abbildungen.kongruenz`); 3 IB-Entwürfe | – |
| 7 | 9 | 16 | +7 | 3 von 9 neuen (`zahlen.intervalle`, `gleichungen.ungleichungen`, `groessen.indirekt`); 6 Entwürfe | – |
| 8 | 14 | 16 | +2 | 1 von 6 neuen (`raum.schraegbilder`); 5 Entwürfe | +1 |
| 9 | 14 | 21 | +7 | 2 von 7 neuen (`stochastik.simulation`, `raum.pyramide_kegel_kugel`); 5 Entwürfe | +1 |
| 10 | 9 | 11 | +2 | 0 von 5 neuen; 5 Entwürfe | +2 |
| **Summe** | 71 | 95 | **+24** | | +4 |

Für Kind A ändert sich vor allem die Verteilung: 10 Flüge, die es ohnehin hätte, kommen 1–3 Jahre früher; 24 Flüge kommen dazu (10 RS, 14 IB), dazu später 4 neue Themen.

**Kind B (Klasse 8)** – Klassen 5–7 gelten als abgeschlossen:
- **In schon abgeschlossenen Klassen liegen 13 Flüge**, die es nach dem bisherigen Plan dort nicht hatte:
  - 4 sind Gymnasium-Flüge, die es sonst in Kl. 8 gemacht hätte und die jetzt früher eingeordnet sind (alle freigegeben): `zahlen.intervalle` (7), `gleichungen.ungleichungen` (7), `groessen.indirekt` (7), `messen.koerper_darstellung` (5). Für Kind B verschiebt sich hier nur die Einordnung; der Stoff fehlt ihm noch.
  - 9 sind neue RS-/IB-Flüge (alle `entwurf`): Kl. 6: `mengen.grundbegriffe`, `groessen.verhaeltnisse`, `sonder.graphentheorie` · Kl. 7: `abbildungen.vektoren`, `abbildungen.determinanten2`, `daten.stichproben`, `finanzen.zinseszins`, `sonder.logik`, `zahlen.schranken`.
- Klasse 8 (laufend): heute 14, neu 16 (6 dazu, 4 nach vorn gerutscht – das sind die 4 oben) **+2**, dazu später 1 neues Thema.
- Klasse 9: **+7**, Klasse 10: **+2**, dazu später 1 bzw. 2 neue Themen.
- Rechnerisch hat Kind B damit 13 Flüge „Rückstand“ aus Kl. 5–7. Davon sind 7 RS-Stoff (Mindeststand Realschule) und 6 IB-Zusatz (`mengen.grundbegriffe`, `groessen.verhaeltnisse`, `sonder.graphentheorie`, `finanzen.zinseszins`, `sonder.logik`, `zahlen.schranken`).

Meinung: Für Kind B die 6 IB-Flüge aus Kl. 6/7 nicht als Rückstand werten (IB läuft nebenbei), sondern als freiwillige Flüge anbieten; die 7 RS-Flüge vor dem Kl.-8-Stoff einplanen, der sie braucht (`zahlen.intervalle` und `gleichungen.ungleichungen` vor `sonder.optimierung`; `abbildungen.vektoren` vor dem neuen Thema „Vierecke und Drehung“). Wie die App „abgeschlossene Klasse mit neuem Flug“ anzeigt, ist eine App-Frage, nicht Teil dieses Vorschlags.

---

## Was der Nutzer entscheiden muss

1. **Plan-Klassen** wie Punkt 1 (10 Gym-Themen rutschen wegen RS nach vorn).
2. **Etappen, die dann vorgreifen** (Punkt 3): `daten.darstellen` 2 Etappen nach Kl. 6 verschieben; `gleichungen.ungleichungen`/grafisch nach `funktionen.linear` oder Vertiefung; `messen.koerper_darstellung`/zylinder zu `messen.prisma_zylinder`; einzelne Aufgaben sperren (7 in `messen.koerper_darstellung`/netz, 10 in `daten.darstellen`/tabelle_auswerten, 2 in `raum.schraegbilder`). Das ist Arbeit wie Teil A (eigener Inhalte-Chat).
3. **IB-Verteilung** (Punkt 2). Ausweichen bei Bedarf: `funktionen.betrag` 9 → 10 (entlastet Kl. 9 auf 20), `mengen.grundbegriffe` 6 → 5.
4. **Orte** (Punkt 4): 15 Klassen-Änderungen, 6 Umzüge, Ortstitel Cusco, Darwin, Galápagos, Tahiti, Palmer, Wostok.
5. **Neue Themen** (Punkt 6): vier Flüge, ein neuer Ort Accra. Einer oder zwei Flüge für Vierecke/Drehung?
6. **Kind B**: 9 neue Flüge in abgeschlossenen Klassen – nachholen (RS) und freiwillig anbieten (IB)?
7. **`rs_by` für die drei Quito/Cusco-Themen** nachtragen (6, 6, 9)?

## Quellen

- `inhalte/themenliste.json`, `inhalte/themen/*.json` (Zweig `lernen-app`, Commit d71b0c3)
- `inhalte/pruefung/klassen/vorschlag-rsib.md` (Zweig `lernen-app`) – Lehrplan-Belege Realschule (lehrplanplus.bayern.de/fachlehrplan/realschule/5–10/mathematik) und IB MYP (Mathematics guide 2020, Haese MYP 1–5)
- `inhalte/pruefung/klassen/vorschlag.md` (Zweig `daten-klassen`) – Lehrplan-Belege Gymnasium (lehrplanplus.bayern.de/fachlehrplan/gymnasium/5–10/mathematik), Regel „ein Ort = eine Klasse“
- `inhalte/AUFTRAEGE.md`, Einundzwanzigste Runde (Teil A für Überschneidungen)
- Datenbank (nur gelesen, 18.11.2026): `schule.block`, `schule.kontinent`, `schule.block_thema`, `schule.thema`, `schule.einheit`
- Koordinaten Accra: allgemein bekannte Lage (5,60° N, 0,19° W), nicht nachgeschlagen
