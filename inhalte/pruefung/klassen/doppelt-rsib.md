# Was an den 24 Realschul-/IB-Themen ist wirklich neu? (Dreiundzwanzigste Runde)

Stand: 2026-11-18. Zweig `doppelt-pruefen`, abgezweigt von `lernen-app` (Commit 04f0fec). **Nur Prüfung und Vorschlag.** Nichts an Themendateien, `themenliste.json`, Datenbank oder App geändert. Kein Merge.

**Frage (Sebastian):** „Die lernen doch grundsätzlich dasselbe Mathe – warum so viele neue Themen?“ `vorschlag-mindeststand.md` plant alle 24 Themen ohne Gymnasium-Klasse als zusätzliche Flüge ein.

**Wörter:** Flug = Thema, Lernkarte = Etappe (`inhalt.etappen`, Schlüssel `l`). **A** = schon in einem Gym-Flug, **B** = kleiner Zusatz zu einem Gym-Flug, **C** = in keinem Gym-Flug. Plan-Klasse wie in `vorschlag-mindeststand.md`. RS = Realschule Bayern, „Gruppe I“ = Wahlpflichtfächergruppe I (mathematischer Zweig). IB-Stufen (MYP 1–3, Standard, Extended, Enrichment) und Haese-Kapitel (H1 … H5E) wie in `vorschlag-rsib.md`.

**Wie geprüft (Tatsache):** Je Lernkarte der 24 Themen Titel, Merksatz (`regel`) und Stichproben der Aufgaben gegen die Lernkarten aller 71 Gym-Themen (Titel, Merksatz, Aufgaben). Dazu gezielte Textsuche in allen Gym-Aufgaben (z. B. „Determinante“, „Streudiagramm“, „Varianz“, „∈“, „Zinseszins“, „Umkehrfunktion“, „gespiegelt“). Belege unten: zwei Aufgaben je Seite im Wortlaut der App (gekürzt mit „…“). Vertiefungs-Status aus `inhalt.bewertung.lernziele_vertiefung`. Lehrplan-Stellen aus `vorschlag-rsib.md` (Abruf 17.11.), **nicht neu abgerufen**.

**Sicherheit**
- **Tatsache:** Gruppe-Einordnung, wo ein Beleg in der Tabelle steht; alle Zählungen (per Skript aus den Themendateien).
- **Annahme:** „A“ heißt „derselbe Stoff, dieselbe Aufgabenart“ – geprüft an Merksatz und Stichproben, nicht an jeder der ~40 Aufgaben je Karte. Lehrplan-Zuordnung wie in `vorschlag-rsib.md` (dort teils selbst Annahme, v. a. IB-Jahre).
- **Meinung:** alles mit „Vorschlag“, „Meinung“ oder „besser“.

---

## Kurzfassung

- **130 Lernkarten** in den 24 Themen: **38 A** (schon da), **25 B** (kleiner Zusatz), **67 C** (wirklich neu).
- **Urteil:** **11 auflösen** (davon 1 Sonderfall: `terme.quadratische_extreme`, Entscheidung 2) · **0 verkleinern** · **13 bleiben**.
- Die Vermutung stimmt für die **Realschule** weitgehend: Von den 10 Themen mit RS-Klasse sind 6 doppelt (`vektoren`, `scharen`, `quadratische_extreme`, `transformation`, `reinquadratisch`, `umkehr`). Echt neu bleiben nur 4: `determinanten2`, `stichproben` (beide RS alle Zweige, Kl. 7), `wurzel`, `matrizen` (beide nur Gruppe I).
- Bei **IB** ist es umgekehrt: Von 14 IB-/klassenlosen Themen sind 5 doppelt (`mengen`, `verhaeltnisse`, `zinseszins`, `bedingt`, `folgen`), **9 bleiben** – davon 1 Standard (`zweidimensional`), 5 Extended (`graphentheorie`, `schranken`, `optimierung`, `standardabweichung`, `betrag`) und 3 ohne Pflicht (`logik`, `reihen`, `normalverteilung`).
- **Die 4 neuen Themen aus `vorschlag-mindeststand.md` Punkt 6 sind nicht nötig** (Teil 3a): 19 der 31 geplanten Lernkarten stehen schon in Gym-Flügen, 7 sind kleine Zusätze, 5 werden neue Lernkarten in bestehenden Flügen.
- Für die auflösten Themen kommen in Gym-Flüge: **6 neue Lernkarten** (alle Vertiefung bzw. Pflicht nur für RS-Gruppe I) und etwa **30–45 Aufgaben** in bestehende Lernkarten. Dazu 3 Folgen-Karten in `funktionen.reihen`.

**Zusätzliche Flüge für die beiden Kinder** (gegenüber dem heutigen Gym-Plan; „vorher“ = `vorschlag-mindeststand.md`):

| | vorher | nachher | nachher je Plan-Klasse 5 / 6 / 7 / 8 / 9 / 10 |
|---|---|---|---|
| **Kind A (Klasse 5)** – alle Klassen vor sich | 24 Flüge + 4 neue Themen = **28** | **13** (14 bei Variante 2b) | 0 / 1 / 4 / 2 (+1) / 3 / 3 |
| **Kind B (Klasse 8)** – in abgeschlossenen Kl. 5–7 | 9 | **5** (`graphentheorie`; `determinanten2`, `stichproben`, `logik`, `schranken`) | – |
| **Kind B** – ab Kl. 8 | 15 + 4 neue Themen = **19** | **8** (9 bei Variante 2b) | – / – / – / 2 (+1) / 3 / 3 |

Von Kind Bs 5 Flügen in abgeschlossenen Klassen sind nur 2 Realschul-Pflicht für alle Zweige (`determinanten2`, `stichproben`); 3 sind IB Extended bzw. ohne Pflicht. Die Aufgaben, die in Gym-Flüge der Kl. 5–7 wandern (`kongruenz`, `brueche`, `proportional`, `prozent_grundwert`), sind für Kind B nur Ergänzungen schon geflogener Flüge.

---

## Teil 1 – Alle 24 Themen auf einen Blick

„Plan heute“ = Plan-Klasse aus `vorschlag-mindeststand.md`. „Plan-Klasse neu“ und „Ort“ = Vorschlag; bei „auflösen“ steht das Zielthema (in Klammern dessen Plan-Klasse).

| Plan heute | Thema | Klasse heute | Karten A/B/C | Urteil | Pflicht für wen | Plan-Klasse neu | Ort bzw. Ziel |
|---|---|---|---|---|---|---|---|
| 6 | `groessen.verhaeltnisse` | IB 2 | 3 / 3 / 0 | **auflösen** | nur IB (MYP 1–3) | – | `groessen.proportional` (5), `bruch.brueche` (6) |
| 6 | `mengen.grundbegriffe` | IB 3 | 1 / 3 / 1 | **auflösen** | nur IB (Framework: Extended; Haese: Jahr 3) | – | `stochastik.verknuepft` (9) |
| 6 | `sonder.graphentheorie` | IB 4 | 0 / 0 / 5 | **bleibt** | nur IB (Extended) | 6 | Galápagos-Inseln (dann allein) |
| 7 | `abbildungen.vektoren` | RS 7 | 5 / 1 / 0 | **auflösen** | RS alle Zweige | – | `abbildungen.kongruenz` (Plan 6) |
| 7 | `abbildungen.determinanten2` | RS 7 | 0 / 0 / 6 | **bleibt** | RS alle Zweige (Karte `vieleck` nur Gruppe I) | 7 | Lagos (dann allein) |
| 7 | `sonder.logik` | IB 4 | 0 / 1 / 4 | **bleibt** | keines (Zusatz) | 7 | Honolulu |
| 7 | `finanzen.zinseszins` | IB 4 | 4 / 1 / 0 | **auflösen** | nur IB (H4 Kap. 11D–E, Annahme) | – | `bruch.prozent_grundwert` (7), `gleichungen.potenz` (9), `gleichungen.exponential` (10) |
| 7 | `zahlen.schranken` | IB 5 | 0 / 1 / 4 | **bleibt** | nur IB (Extended) | 7 | Honolulu |
| 7 | `daten.stichproben` | RS 7, IB 2 | 0 / 1 / 4 | **bleibt** | RS alle Zweige; IB (MYP 1–3) | 7 | Perth |
| 8 | `funktionen.scharen` | RS 8 | 2 / 3 / 1 | **auflösen** | RS Gruppe I Kl. 8 (II/III Kl. 9) für Parallelenscharen; Büschel und parameterabhängige Lösungen: kein Lehrplan-Beleg | – | `funktionen.linear` (8) |
| 8 | `daten.zweidimensional` | IB 5 | 0 / 1 / 4 | **bleibt** | nur IB (Standard) | 8 | Hobart |
| 8 | `funktionen.folgen` | IB 5 | 2 / 2 / 1 | **auflösen** | nur IB (Annahme Extended; einfache Folgen H1) | – | `funktionen.reihen` (10) |
| 8 | `terme.quadratische_extreme` | RS 8 | 5 / 0 / 0 | **auflösen (Sonderfall)** | RS alle Zweige Kl. 8 | 8 (Sonderfall) | Shanghai |
| 8 | `sonder.optimierung` | IB 5 | 0 / 1 / 4 | **bleibt** | nur IB (Extended) | 8 | Tahiti |
| 9 | `gleichungen.reinquadratisch` | RS 9, IB 4 | 6 / 0 / 0 | **auflösen** | RS alle Zweige Kl. 9; IB Standard | – | `gleichungen.quadratisch` (9), `zahlen.wurzeln_basis` (9), `gleichungen.potenz` (9) |
| 9 | `funktionen.transformation` | RS 9, IB 5 | 4 / 1 / 1 | **auflösen** | RS Gruppe I Kl. 9 (II/III Kl. 10); Karte `punkte`: RS Gruppe I Kl. 10; IB Extended (Annahme) | – | `funktionen.quadratisch` (9), Karte `punkte` → `funktionen.exponential_log` (10) |
| 9 | `funktionen.betrag` | IB 5 | 0 / 1 / 4 | **bleibt** | nur IB (Extended, Annahme) | 9 | Wostok-Station (wie `vorschlag-mindeststand.md`) |
| 9 | `gleichungen.wurzel` | RS 9 | 0 / 1 / 5 | **bleibt** | nur RS Gruppe I | 9 | Tokio |
| 9 | `daten.standardabweichung` | IB 5 | 0 / 1 / 4 | **bleibt** | nur IB (Extended) | 9 | Wellington (wie `vorschlag-mindeststand.md`) |
| 10 | `funktionen.umkehr` | RS 10, IB 5 | 2 / 2 / 2 | **auflösen** | RS Gruppe I Kl. 10; IB Enrichment | – | `funktionen.potenz` (9) und `funktionen.exponential_log` (10) |
| 10 | `funktionen.reihen` | IB 5 | 0 / 0 / 5 | **bleibt** | keines (Zusatz) | 10 | Palmer-Station (dann allein, Klasse 10) |
| 10 | `stochastik.bedingt` | IB 5 | 4 / 1 / 1 | **auflösen** | nur IB (Extended) | – | `stochastik.verknuepft` (9), `stochastik.mehrstufig` (10) |
| 10 | `daten.normalverteilung` | IB 5 | 0 / 0 / 5 | **bleibt** | keines (Zusatz) | 10 | Suva |
| 10 | `abbildungen.matrizen` | RS 10, IB 5 | 0 / 0 / 6 | **bleibt** | nur RS Gruppe I (Karten `rechnen`, `inverse`: keines → Vertiefung) | 10 | Dakar |
**Ergebnis Teil 1 (Tatsache, gezählt):** auflösen 11 · verkleinern 0 · bleibt 13. „Verkleinern“ kam nicht vor: Wo A-Karten waren, war der C-Rest immer kleiner als 3 Karten; wo 3 oder mehr C-Karten waren, gab es keine A-Karten (höchstens eine B-Karte, die als Einstieg im Flug bleibt).

**Pflicht der 13 bleibenden Flüge (Tatsache nach `vorschlag-rsib.md`):** RS alle Zweige 2 · nur RS Gruppe I 2 · nur IB 6 (1 Standard, 5 Extended; `betrag` als Annahme) · keines 3.

---

## Teil 2 – Je Thema: Lernkarte für Lernkarte

Reihenfolge nach Plan-Klasse heute. Spalte „Gym-Gegenstück“: Thema/Lernkarte, Titel, „(Vertiefung)“ falls dort Vertiefung, Plan-Klasse. Bei C ohne Beleg: Die Textsuche fand nichts Gleichwertiges.

### `groessen.verhaeltnisse` – Verhältnisse und Raten (Plan heute 6, IB 2) → **auflösen**

Lehrplan: IB H2 Kap. 16. Pflicht: nur IB (MYP 1–3). Dreisatz, Stückpreis, Aufteilen, sogar die Hemden-auf-der-Leine-Falle stehen in Gym-Flügen. Neu: „Verhältnis kürzen/ergänzen“ als 3–4 Aufgaben in `bruch.brueche`/kuerzen bzw. erweitern; Änderungsrate als 2–3 Aufgaben in `groessen.proportional`/sach (Steigung kommt erst Kl. 8).

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `kuerzen` Verhältnisse kürzen | **B** | `bruch.brueche`/kuerzen „Brüche vollständig kürzen“ (6) | „Kürze das Verhältnis 12 : 18 so weit wie möglich.“ · „Kürze das Verhältnis 3 kg : 400 g.“ | „Kann man 22/46 kürzen?“ · „Durch welche dieser Zahlen kann man 12/18 kürzen?“ | „Verhältnis kürzen“ = Bruch kürzen; 3–4 Aufgaben in `bruch.brueche`/kuerzen. |
| `gleichwertig` Gleichwertige Verhältnisse | **B** | `gleichungen.bruch`/verhaeltnis „Verhältnisgleichungen“ (8) | „Ergänze: 6 : 7 = 18 : □“ · „Ergänze: 6 : 11 = □ : 22“ | „Löse die Verhältnisgleichung 5 : x = 10 : 6.“ · „Löse die Verhältnisgleichung 5 : x = 6 : 12.“ | Im Gym als Verhältnisgleichung erst Kl. 8; für IB (MYP 2) als Aufgaben in `bruch.brueche`/erweitern. |
| `aufteilen` Im Verhältnis aufteilen | **A** | `gleichungen.bruch`/verhaeltnis „Verhältnisgleichungen“ (8) | „Ein 112,5 m langes Seil wird im Verhältnis 4 : 5 zerschnitten. Wie lang ist das kürzere Stück?“ · „Für einen Teig werden Mehl und Zucker im Verhältnis 7 : 6 gemischt, zusammen 2 470 g. Wie viel Gramm Zucker sind es?“ | „500 ml Saft sind im Verhältnis Sirup : Wasser = 1 : 4 gemischt. Wie viel ml Sirup muss man dazugeben, damit das Verhältnis 1 : 2 wird?“ · „Für Beton mischt man Zement und Kies im Verhältnis 1 : 5. Wie viel kg Zement braucht man für 15 kg Kies?“ |  |
| `proportion` Proportionen lösen | **A** | `groessen.proportional`/sach „Sachaufgaben mit Dreisatz“ (5) | „Für 8 Portionen braucht man 400 g Butter. Wie viel Butter braucht man für 6 Portionen?“ · „Für 5 Portionen braucht man 250 g Zucker. Wie viel Zucker braucht man für 10 Portionen?“ | „Ein Rezept für 4 Personen braucht 500 g Reis. Wie viel Gramm braucht man für 12 Personen?“ · „3 Hemden trocknen auf der Leine in 75 Minuten. Wie viele Minuten brauchen 7 Hemden auf derselben Leine?“ |  |
| `einheitsrate` Einheitsraten und Stückpreise | **A** | `groessen.proportional`/einheit „Auf die Einheit schließen“ (5) | „Eine Packung Kaffee mit 250 g kostet 8,25 €. Wie viel kostet das pro 100 g?“ · „Ein Auto verbraucht 6 Liter auf 100 km. Wie weit kommt es mit 45 Litern?“ | „12 Eintrittskarten kosten 144 €. 1 Karte kostet wie viel €?“ · „3 Äpfel und 2 Birnen kosten 1,90 €. 3 Äpfel und 4 Birnen kosten 2,90 €. Wie viel Cent kostet 1 Birne?“ |  |
| `aenderung` Änderungsraten berechnen | **B** | `funktionen.linear`/ablesen „Steigung m und Achsenabschnitt t“ (8) | „Ein Becken enthält 100 Liter Wasser. Nach 8 Minuten sind es 260 Liter. Wie viele Liter fließen pro Minute zu?“ · „Ein Becken enthält 100 Liter Wasser. Nach 2 Minuten sind es 140 Liter. Wie viele Liter fließen pro Minute zu?“ | „Ein Handyvertrag kostet y = 0,09x + 7,99 Euro im Monat (x Minuten). Im Vertrag sind 3 GB Daten enthalten. Wie viel kostet jede …“ · „Ein Becken wird gefüllt: y = 0,8x + 15 (x in Minuten, y in cm). Das Becken ist 95 cm tief. Wie viele Minuten dauert es, bis es voll ist?“ | Im Gym erst Kl. 8 als Steigung (dazu Einzelaufgabe in `zahlen.rechengesetze`/geteilt_ganz); für IB 2–3 Aufgaben in `groessen.proportional`/sach. |

### `mengen.grundbegriffe` – Mengen und Venn-Diagramme (Plan heute 6, IB 3) → **auflösen**

Lehrplan: IB H3 Kap. 2, H4 Kap. 5/7. Pflicht: nur IB (Framework: Extended; Haese: Jahr 3). Schnitt, Vereinigung, „weder noch“ und die Zählformel stehen in `stochastik.verknuepft` (verknuepfen, vierfeld, additionssatz) – mit Vierfeldertafel statt Venn-Diagramm. Neu ist nur die Mengenschreibweise { }, ∈: als Einstiegskarte „Mengen und Venn-Diagramm“ vor `verknuepfen` (Vertiefung). Folge: Mengen kommen dann erst in Kl. 9 statt 6 (für IB unschädlich, IB läuft nebenbei).

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `elemente` Was gehört zu einer Menge? | **C** | – |  |  | Mengenschreibweise { }, ∈ kommt in keinem Gym-Flug als Aufgabe vor. |
| `schnitt` Die Schnittmenge A ∩ B | **B** | `stochastik.verknuepft`/verknuepfen „Schnitt, Vereinigung, Gegenereignis“ (9) | „A = Kinder mit Brille, B = Kinder mit Geschwistern. Lisa gehört zu A, aber nicht zu A ∩ B. Was weißt du über Lisa?“ · „A = die Quadratzahlen bis 24, B = die Vielfachen von 5 bis 24. Welche Menge ist A ∩ B?“ | „S: „Ein Kind spielt Schach.“ M: „Ein Kind macht Musik.“ Welche Beschreibung passt zu (S ∩ M̄) ∪ (S̄ ∩ M)?“ · „In zwei verschiedenen Spielen gilt: A: „Team Rot gewinnt.“ B: „Team Blau gewinnt.“ Was bedeutet Ā ∩ B̄?“ | Gleicher Begriff, im Gym nur als Ereignis mit Wahrscheinlichkeit (Kl. 9). |
| `vereinigung` Die Vereinigungsmenge A ∪ B | **A** | `stochastik.verknuepft`/vierfeld „Vierfeldertafel ergänzen“ (9) | „In einer Klasse mit 28 Kindern haben 15 einen Hund, 12 eine Katze und 4 keines von beiden. Wie viele haben beides?“ · „In einer Klasse: 11 Kinder haben einen Hund, 22 Kinder haben eine Katze, 7 haben beides. Wie viele Kinder haben mindestens ein Haustier …“ | „Untersucht werden 100 Besucher eines Freibads. A: „ist Erwachsener“, B: „hat eine Jahreskarte“. 70 haben A, 46 haben B, 42 haben beides. …“ · „Untersucht werden 500 Besucher eines Freibads. A: „ist Erwachsener“, B: „hat eine Jahreskarte“. 352 haben A, 393 haben B, 324 haben …“ | n(A ∪ B) = n(A) + n(B) − n(A ∩ B) ist die Zählform des Additionssatzes (`additionssatz`). |
| `venn` Mit Venn-Diagrammen zählen | **B** | `stochastik.verknuepft`/vierfeld „Vierfeldertafel ergänzen“ (9) | „33 Familien wurden befragt: 25 haben einen Hund, 18 haben eine Katze, 10 haben beides. Wie viele gehören nur zu „Hund“?“ · „25 Familien wurden befragt: 11 haben einen Hund, 16 haben eine Katze, 2 haben beides. Wie viele haben weder Hund noch Katze?“ | „Untersucht werden 100 Besucher eines Freibads. A: „ist Erwachsener“, B: „hat eine Jahreskarte“. 70 haben A, 46 haben B, 42 haben beides. …“ · „Untersucht werden 500 Besucher eines Freibads. A: „ist Erwachsener“, B: „hat eine Jahreskarte“. 352 haben A, 393 haben B, 324 haben …“ | Dieselben Zahlen, aber Vierfeldertafel statt Venn-Diagramm. |
| `verstehen` Aussagen über Mengen prüfen | **B** | `stochastik.verknuepft`/verstehen „Aussagen über Ereignisse prüfen“ (9) | „A = die Vielfachen von 6 bis 24, B = die geraden Zahlen bis 24. Was ist A ∪ B?“ · „A = {1; 2; 3; 4} und B = {3; 4; 5}. Wie viele Elemente hat A ∩ B?“ | „Bei 5 Torschüssen ist A: „mindestens einmal ein Treffer“. Was ist das Gegenereignis Ā?“ · „Bei 5 Losen ist A: „mindestens einmal ein Gewinn“. Was ist das Gegenereignis Ā?“ | Vertiefung im RS/IB-Flug. |

### `sonder.graphentheorie` – Graphentheorie (Plan heute 6, IB 4) → **bleibt**

Lehrplan: IB Extended (Netzwerke); H4 Kap. 28 (online). Pflicht: nur IB (Extended). Kein Graph im Sinn von Knoten/Kanten in einem Gym-Flug.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `grundbegriffe` Knoten, Kanten und Grad | **C** | – |  |  |  |
| `euler` Alle Kanten genau einmal | **C** | – |  |  |  |
| `kuerzester` Kürzeste Wege finden | **C** | – |  |  |  |
| `spannbaum` Minimaler Spannbaum | **C** | – |  |  |  |
| `verstehen` Aussagen über Graphen prüfen | **C** | – |  |  |  |

### `abbildungen.vektoren` – Vektoren und Determinanten (Plan heute 7, RS 7) → **auflösen**

Lehrplan: M7 LB2 Parallelverschiebung (I und II/III). Pflicht: RS alle Zweige. A-Stoff steht in `abbildungen.kongruenz`/verschiebung – bis in den Wortlaut („Verschiebe P(…) mit v = (…)“). Die Parallelogramm-Ecke steht sogar schon in `geometrie.grundbegriffe`/vierecke (Kl. 5). Die B-Karte `gegenvektor` wird 3–4 Aufgaben in `verschiebung`. **Haken:** `verschiebung` ist dort Vertiefung (Gym M7 hat keine Verschiebung) → Entscheidung 3. Skalarprodukt aus dem `umfang` steht in keiner Karte (gehört zu `abbildungen.matrizen`).

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `vektor_bestimmen` Einen Vektor aus zwei Punkten | **A** | `abbildungen.kongruenz`/verschiebung „Figuren verschieben“ (Vertiefung) (6) | „Berechne den Vektor CD für C(0 \| −1) und D(−1 \| 1).“ · „Berechne den Vektor AB für A(0 \| 0) und B(3 \| 3).“ | „P(−3 \| 3) wird auf P'(1 \| 7) verschoben. Gib den Verschiebungspfeil an.“ · „P(7 \| −6) wird auf P'(9 \| −1) verschoben. Gib den Verschiebungspfeil an.“ |  |
| `bildpunkt` Punkte verschieben | **A** | `abbildungen.kongruenz`/verschiebung „Figuren verschieben“ (Vertiefung) (6) | „Verschiebe P(2 \| 6) mit dem Vektor v = (5 \| 2).“ · „Verschiebe P(2 \| 7) mit dem Vektor v = (4 \| 1).“ | „Verschiebe P(−7 \| 3) mit v = (1 \| −4).“ · „Verschiebe P(3 \| −3) mit v = (−1 \| −5).“ |  |
| `gegenvektor` Gegenvektor und Rückweg | **B** | `abbildungen.kongruenz`/verschiebung „Figuren verschieben“ (Vertiefung) (6) | „Bei der Verschiebung mit v = (−7 \| 4) entsteht der Bildpunkt P'(−6 \| 2). Berechne den Urpunkt P.“ · „Bei der Verschiebung mit v = (7 \| 3) entsteht der Bildpunkt P'(12 \| 5). Berechne den Urpunkt P.“ | „P(−3 \| 3) wird auf P'(1 \| 7) verschoben. Gib den Verschiebungspfeil an.“ · „P(7 \| −6) wird auf P'(9 \| −1) verschoben. Gib den Verschiebungspfeil an.“ | Rückwärts-Aufgaben („Wo lag P?“) gibt es dort nur bei Spiegelung/Drehung – 3–4 Aufgaben ergänzen. |
| `addition` Vektoren addieren | **A** | `abbildungen.kongruenz`/verschiebung „Figuren verschieben“ (Vertiefung) (6) | „Eine Figur wird nacheinander mit (3 \| −1), (−3 \| 5) und (−5 \| 5) verschoben. Durch welche einzige Verschiebung erreicht man dasselbe?“ · „Eine Figur wird nacheinander mit (−6 \| −6), (−1 \| −2) und (−3 \| 5) verschoben. Durch welche einzige Verschiebung erreicht man dasselbe?“ | „P(−4 \| −7) wird erst mit (1 \| −2), dann mit (−2 \| −6) verschoben. Wohin kommt P?“ · „P(−4 \| 4) wird erst mit (5 \| 2), dann mit (6 \| 1) verschoben. Wohin kommt P?“ |  |
| `punkt_berechnen` Punkte mit Vektoren berechnen | **A** | `geometrie.grundbegriffe`/vierecke „Besondere Vierecke“ (5) | „Im Parallelogramm ABCD ist A(0 \| 0), Vektor AB = (2 \| 1) und Vektor AD = (0 \| 4). Berechne C.“ · „Gegeben sind A(−3 \| −1), B(3 \| 1) und D(−1 \| 5) eines Parallelogramms ABCD. a) Berechne C. b) Berechne den Mittelpunkt M von [AC].“ | „ABCD ist ein Parallelogramm mit A(2 \| −6), B(8 \| −6) und C(10 \| −4). Welche Koordinaten hat D?“ · „ABCD ist ein Parallelogramm mit A(1 \| 1), B(5 \| 1) und C(6 \| 4). Welche Koordinaten hat D?“ | Dieselbe Aufgabe („Parallelogramm ABCD mit A, B, C – wo liegt D?“) schon in Kl. 5, dort ohne das Wort Vektor. |
| `eigenschaften` Was bleibt bei der Verschiebung? | **A** | `abbildungen.kongruenz`/eigenschaften „Was bleibt bei Abbildungen gleich?“ (6) | „Welche Aussage über die Parallelverschiebung ist FALSCH?“ · „Ein Dreieck ABC wird mit v = (4 \| 5) verschoben. Die Seite [BC] ist 11 cm lang. Wie lang ist B'C'?“ | „Eine Strecke [AB] ist 6,5 cm lang. Sie wird an einer Achse gespiegelt. Wie lang ist [A'B']?“ · „Ein Winkel von 37° wird um einen Punkt um 90° gedreht. Wie groß ist der Bildwinkel?“ |  |

### `abbildungen.determinanten2` – Zweireihige Determinanten (Plan heute 7, RS 7) → **bleibt**

Lehrplan: M7 LB2 (I); II/III laut `vorschlag-rsib.md` ebenfalls 7, wieder M9 LB5 (II). Pflicht: RS alle Zweige (Karte `vieleck` nur Gruppe I). Keine Determinante in einem Gym-Flug (Textsuche „Determinante“: 0 Treffer außerhalb).

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `det_berechnen` Eine Determinante berechnen | **C** | – |  |  |  |
| `parallelogramm` Fläche eines Parallelogramms | **C** | – |  |  |  |
| `dreieck` Fläche eines Dreiecks | **C** | – |  |  |  |
| `umlaufsinn` Was sagt das Vorzeichen? | **C** | – |  |  |  |
| `viereck` Fläche eines Vierecks | **C** | – |  |  |  |
| `vieleck` Fläche eines Vielecks | **C** | – |  |  |  |

### `sonder.logik` – Aussagenlogik (Plan heute 7, IB 4) → **bleibt**

Lehrplan: IB: kein Beleg im Framework; H4 Kap. 30 (online). Pflicht: keines (Zusatz). Gym hat nur Satz/Kehrsatz mit Gegenbeispiel (`geometrie.konstruktion`).

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `aussagen` Was ist eine Aussage? | **C** | – |  |  |  |
| `negation` Aussagen verneinen | **C** | – |  |  |  |
| `verknuepfen` Und und Oder | **C** | – |  |  |  |
| `tafel` Wahrheitstafeln ausfüllen | **C** | – |  |  |  |
| `folgerung` Wenn …, dann … | **B** | `geometrie.konstruktion`/satz_kehrsatz „Satz und Kehrsatz“ (7) | „Die Aussage „Wenn ein Tier ein Hund ist, dann ist es ein Säugetier.“ ist wahr (p: Wenn-Teil, q: Dann-Teil). Folgt daraus die Umkehrung …“ · „Es gilt: „Wenn ein Tier ein Hund ist, dann ist es ein Säugetier.“ Man beobachtet: q ist eingetreten. Darf man schließen, dass auch p gilt?“ | „Widerlege den Kehrsatz: „Wenn ein Dreieck gleichschenklig ist, dann ist es gleichseitig.“ Welches Gegenbeispiel passt?“ · „Satz: „Wenn eine Zahl durch 10 teilbar ist, dann endet sie auf 0.“ Ist der Kehrsatz wahr?“ | Kehrsatz/Gegenbeispiel = Gym Kl. 7; Wahrheitswert von p ⇒ q und Kontraposition sind neu. Bleibt im Flug. |

### `finanzen.zinseszins` – Zinseszins (Plan heute 7, IB 4) → **auflösen**

Lehrplan: –. Pflicht: nur IB (H4 Kap. 11D–E, Annahme). Alles da: vermehrter Grundwert, Faktoren nacheinander (Kl. 7), Zinssatz aus zwei Jahren (`gleichungen.potenz`/sachaufgabe, 11 Zinseszins-Aufgaben), Verdopplungszeit (`gleichungen.exponential`/wachstum, 16 Aufgaben). Neu nur das Wort „Zinseszins“ und Kₙ = K₀ · qⁿ als Formel: 3–4 Aufgaben in `bruch.prozent_grundwert`/mehrfach.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `jahr` Zinsen Jahr für Jahr | **A** | `bruch.prozent_grundwert`/vermehrt „Den vermehrten Grundwert berechnen“ (7) | „1 500 € werden mit 4 % Zinseszins angelegt. Nach einem Jahr zahlt man 200 € dazu. Wie hoch ist das Kapital nach 2 Jahren?“ · „2 400 € liegen 2 Jahre bei 1 %. Wie viel mehr bringt Zinseszins als einfache Zinsen (jedes Jahr nur Zinsen vom Anfangskapital)?“ | „Ein Sparguthaben beträgt 800 €. In einem Jahr kommen 2 % Zinsen dazu. Wie hoch ist das Guthaben danach?“ · „Ein Guthaben von 2 000 € wächst in einem Jahr durch Zinsen auf 2 070 €. Wie hoch ist der Zinssatz?“ |  |
| `faktor` Der Wachstumsfaktor q | **A** | `bruch.prozent_grundwert`/mehrfach „Mehrere Änderungen nacheinander“ (7) | „Ein Guthaben wird im ersten Jahr mit 2 %, im zweiten mit 5 % verzinst. Mit welchem Faktor wurde es insgesamt multipliziert?“ · „Ein Kapital wird jedes Jahr mit dem Faktor q = 1,04 multipliziert. Wie hoch ist der Zinssatz in %?“ | „Ein Preis von 100 € ändert sich um +25 %, dann +50 %. Wie hoch ist der Endpreis?“ · „Ein Preis ändert sich nacheinander um +5 %, dann +10 %. Um wie viel Prozent hat er sich insgesamt geändert? (Zunahme positiv, Abnahme …“ |  |
| `formel` Kapital nach n Jahren | **B** | `bruch.prozent_grundwert`/mehrfach „Mehrere Änderungen nacheinander“ (7) | „2 000 € werden 5 Jahre mit 2,5 % Zinseszins angelegt. Wie hoch ist das Endkapital? (auf Cent)“ · „1 500 € werden 8 Jahre mit 3 % Zinseszins angelegt. Wie viel Zinsen bringt das insgesamt? (auf Cent)“ | „2 000 € werden 3 Jahre lang mit 2 % pro Jahr verzinst; die Zinsen bleiben auf dem Konto. Wie hoch ist das Guthaben danach? Runde auf Cent.“ · „Ein Preis steigt zweimal hintereinander um denselben Prozentsatz und ist danach 44 % höher als am Anfang. Um wie viel Prozent stieg er …“ | Kₙ = K₀ · qⁿ steht im Gym als Einzelaufgabe („3 Jahre … Zinsen bleiben auf dem Konto“) und in `funktionen.exponential_log`/werte; Wort „Zinseszins“ + 3–4 Aufgaben ergänzen. |
| `rueck` Rückwärts rechnen | **A** | `gleichungen.potenz`/sachaufgabe „Sachaufgaben mit Potenzgleichungen“ (9) | „Aus 2 000 € werden in einem Jahr 2 050 €. Wie hoch ist der Zinssatz in %?“ · „Nach 2 Jahren mit 2 % Zinseszins sind 1 040,40 € auf dem Konto. Wie hoch war das Anfangskapital?“ | „Ein Guthaben wächst in 2 Jahren bei gleichem Zinssatz (mit Zinseszins) von 4 000 € auf 4 326,40 €. Wie hoch ist der Zinssatz in Prozent?“ · „Ein Guthaben wächst in 2 Jahren bei gleichem Zinssatz (mit Zinseszins) von 20 000 € auf 22 050 €. Wie hoch ist der Zinssatz in Prozent?“ |  |
| `vergleich` Angebote vergleichen | **A** | `gleichungen.exponential`/wachstum „Wachstum und Zerfall: Wann?“ (10) | „Nach wie vielen ganzen Jahren hat sich ein Kapital bei 12 % Zinseszins erstmals mindestens verdoppelt?“ · „Ein Kapital hat sich mit Zinseszins in 10 Jahren etwa verdoppelt. Welcher Zinssatz passt am besten?“ | „Ein Guthaben wird mit 5 % pro Jahr verzinst. Nach wie vielen vollen Jahren hat es sich erstmals verdoppelt?“ · „Für welchen Wachstumsfaktor b verdoppelt sich ein Bestand f(t) = a · b^t in genau 10 Jahren? Runde auf vier Nachkommastellen.“ |  |

### `zahlen.schranken` – Schranken und Genauigkeit (Plan heute 7, IB 5) → **bleibt**

Lehrplan: IB Extended (obere/untere Schranken); kein Haese-Beleg. Pflicht: nur IB (Extended). Für ganze Zahlen steht „rund 18 000 … mindestens?“ schon in `zahlen.natuerlich`; Schranken bei Rechnungen fehlen.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `grenzen` Untere und obere Schranke | **B** | `zahlen.natuerlich`/runden_sinnvoll „Wann darf man runden?“ (5) | „Eine Zahl wird zuerst auf Zehntel gerundet, dann wird das Ergebnis auf Ganze gerundet. Am Ende steht 3. Wie groß kann die ursprüngliche …“ · „Die Zahl der Teilnehmer wurde auf Zehner gerundet: 890. Wie viele Teilnehmer waren es mindestens?“ | „Drei ganze Zahlen ergeben auf Hunderter gerundet 400, 500 und 600. Zusammen ergeben sie genau 1 500. Wie groß kann die Zahl, die auf 600 …“ · „25 Kinder geben ihre Körpergröße auf 10 cm gerundet an. Die Summe der gerundeten Werte ist 3 600 cm. Alle wirklichen Größen sind ganze …“ | Für ganze Zahlen identisch („rund 9 000 … höchstens?“); halbe Rundungseinheit bei Dezimalzahlen und das Wort „Schranke“ neu. Bleibt als Einstieg. |
| `messen` Genauigkeit von Messungen | **C** | – |  |  |  |
| `summe` Schranken bei Summen und Differenzen | **C** | – |  |  |  |
| `produkt` Schranken bei Produkten und Quotienten | **C** | – |  |  |  |
| `entscheiden` Mit Schranken entscheiden | **C** | – |  |  |  |

### `daten.stichproben` – Stichproben und Aussagekraft (Plan heute 7, RS 7, IB 2) → **bleibt**

Lehrplan: M7 LB8 (I) / LB6 (II/III); IB H2 Kap. 18A. Pflicht: RS alle Zweige; IB (MYP 1–3). Gym hat Umfragen nur als Datenlieferant (Strichliste, Diagramm), nie die Frage „Ist die Stichprobe brauchbar?“.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `begriffe` Grundgesamtheit und Stichprobe | **C** | – |  |  |  |
| `hochrechnen` Von der Stichprobe hochrechnen | **B** | `stochastik.grundbegriffe`/grosse_zahlen „Gesetz der großen Zahlen“ (8) | „Von 50 befragten Kindern einer Schule mit 750 Kindern fahren 18 mit dem Rad. Schätze, wie viele Kinder der Schule NICHT mit dem Rad fahren.“ · „Von 50 befragten Besuchern eines Festivals mit 1 550 Besuchern reisen 23 mit dem Zug an. Schätze, wie viele Besucher insgesamt mit dem …“ | „Ein Würfel wird 300-mal geworfen. Wie oft erwartest du ungefähr eine Zahl größer als 4?“ · „Wie oft erwartest du bei 100 Versuchen ungefähr „rot“ beim Glücksrad mit 10 gleichen Feldern, davon 6 rot?“ | Rechnung (Anteil · Gesamtzahl) ist bekannt; bleibt als Einstieg im Flug. |
| `repraesentativ` Ist die Stichprobe geeignet? | **C** | – |  |  |  |
| `fehlerquellen` Wie entstehen verzerrte Ergebnisse? | **C** | – |  |  | `daten.darstellen`/irrefuehrend behandelt Diagramme, nicht Stichproben. |
| `aussagen` Aussagen kritisch prüfen | **C** | – |  |  |  |

### `funktionen.scharen` – Parameter und Funktionenscharen (Plan heute 8, RS 8) → **auflösen**

Lehrplan: M8 LB6 (I) Parallelenscharen; Parabelscharen M9 LB7 (I). Pflicht: RS Gruppe I Kl. 8 (II/III Kl. 9) für Parallelenscharen; Büschel und parameterabhängige Lösungen: kein Lehrplan-Beleg. Rechnung „Gerade mit Steigung m durch P“ = `funktionen.linear`/aufstellen; Tarife = `deuten`. Neu ist nur das Wort „Schar“ und das Geradenbüschel. Vorschlag: 3–4 Aufgaben „Für welches k …?“ in `lage`, Karte `bueschel` als **Vertiefungskarte** in `funktionen.linear` nach `lage`, `loesung_parameter` als Aufgaben in `gleichungen.lgs2`/loesbarkeit (Vertiefung).

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `einsetzen` Einen Parameterwert einsetzen | **B** | `funktionen.linear`/deuten „Lineare Funktionen im Sachzusammenhang“ (8) | „Gegeben ist die Schar y = (k + 3) · x + 2k. Berechne für k = 5 den y-Wert an der Stelle x = 5.“ · „Gegeben ist die Schar y = (k − 1) · x + 2k. Für welches k geht die Gerade durch P(2 \| 10)?“ | „Eine Taxifahrt: P(x) = 2,4x + 3,5 (x in km, P in €). Wie weit ist man gefahren, wenn 15,50 € zu zahlen sind?“ · „Ein Tarif: K(x) = 0,15x + 6 (x Minuten, K in €). Wie viel Prozent der Rechnung macht bei 40 Minuten die Grundgebühr aus?“ | Wort „Schar“ fehlt im Gym-Flug; 2–3 Aufgaben in `funktionen.linear`/lage. |
| `parallelenschar` Parallele Geraden: y = m · x + t | **A** | `funktionen.linear`/aufstellen „Geradengleichung aufstellen“ (8) | „Welche Gerade der Schar y = −x + t geht durch P(−6 \| −5)? Berechne t.“ · „Welche Gerade der Schar y = −2x + t geht durch P(−1 \| 8)? Berechne t.“ | „Eine Gerade hat die Steigung 3 und geht durch P(−3 \| −11). Gib den Funktionsterm an.“ · „Eine Gerade hat die Steigung −3 und geht durch P(−4 \| 5). Gib den Funktionsterm an.“ |  |
| `bueschel` Geraden durch einen Punkt | **C** | – |  |  | RS: kein Lehrplan-Beleg → als Vertiefungskarte in `funktionen.linear` nach `lage`. |
| `wirkung` Was bewirkt der Parameter? | **B** | `funktionen.linear`/lage „Parallel oder senkrecht?“ (8) | „Für welches k hat die Gerade der Schar y = (3k − 6) · x + 1 die Steigung 9?“ · „Die gezeichnete Gerade gehört zur Schar y = (k − 3) · x − 2. Bestimme k.“ | „Wie liegen die Geraden g: y = 1,5x + 4 und h: 2y = 3x + 8 zueinander?“ · „Wie liegen die Geraden g: y = 1,5x − 1 und h: y = 1,5x + 3 zueinander?“ | „Für welches k parallel …?“ als 3–4 Aufgaben in `lage`. |
| `loesung_parameter` Lösungen, die vom Parameter abhängen | **B** | `gleichungen.lgs2`/loesbarkeit „Wie viele Lösungen hat das System?“ (8) | „Für welchen Wert von k haben die Geraden y = −2x + 3 und y = k · x − 1 keinen Schnittpunkt?“ · „Für welchen Wert von k haben die Geraden y = −4x − 2 und y = k · x − 3 keinen Schnittpunkt?“ | „Tarif A: y = 0,2x + 6, Tarif B: y = m · x + 4. Für welches m gibt es KEINEN Schnittpunkt? Die Grundgebühren stehen schon fest, der …“ | RS: kein Lehrplan-Beleg; Aufgaben in `loesbarkeit` (Vertiefung). |
| `sachaufgabe` Parameter in Sachaufgaben | **A** | `funktionen.linear`/deuten „Lineare Funktionen im Sachzusammenhang“ (8) | „Handytarif A: 5 € im Monat plus 0,10 € pro Minute. Tarif B: keine Grundgebühr, 0,15 € pro Minute. Wie viel spart man mit A bei 300 Minuten?“ · „Ein Fahrradverleih nimmt 5 € Grundgebühr plus m € pro Stunde. Für 3 Stunden bezahlt man 23 €. Berechne m.“ | „Eine Taxifahrt: P(x) = 2,4x + 3,5 (x in km, P in €). Wie weit ist man gefahren, wenn 15,50 € zu zahlen sind?“ · „Ein Tarif: K(x) = 0,15x + 6 (x Minuten, K in €). Wie viel Prozent der Rechnung macht bei 40 Minuten die Grundgebühr aus?“ |  |

### `daten.zweidimensional` – Zweidimensionale Daten (Plan heute 8, IB 5) → **bleibt**

Lehrplan: IB Standard: Streudiagramm, Ausgleichsgerade, qualitative Korrelation; H5E Kap. 19. Pflicht: nur IB (Standard). Kein Streudiagramm in einem Gym-Flug (Textsuche: 0 Treffer).

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `ablesen` Streudiagramme lesen | **C** | – |  |  |  |
| `zusammenhang` Art des Zusammenhangs erkennen | **C** | – |  |  |  |
| `gerade` Mit der Ausgleichsgeraden schätzen | **C** | – |  |  | Braucht `funktionen.linear` (8), die Ausgleichsgerade selbst gibt es dort nicht. |
| `ausreisser` Ausreißer finden | **B** | `daten.boxplot`/median „Den Median bestimmen“ (7) | „Temperaturen um 12 Uhr an sechs Sommertagen: 18 °C, 19 °C, 21 °C, 20 °C, −19 °C, 22 °C. Was ist am wahrscheinlichsten passiert?“ | „Daten: 32, 8, 28, 39, 10, 20, 17, 27, 23, 318. Welchen Kennwert verändert der Ausreißer 318 stärker?“ | Ausreißer nur bei eindimensionalen Daten; bleibt im Flug. |
| `kausal` Korrelation oder Ursache? | **C** | – |  |  |  |

### `funktionen.folgen` – Folgen (Plan heute 8, IB 5) → **auflösen**

Lehrplan: IB H1 Kap. 14, H5E Kap. 22A–C. Pflicht: nur IB (Annahme Extended; einfache Folgen H1). Explizite Terme = Figurenfolgen (`terme.aufstellen`/muster, Kl. 6), „gleiche Differenzen / gleiche Quotienten“ = `funktionen.exponential_log`/linear_oder_exponentiell. Die Karten `rekursiv`, `arithmetisch`, `geometrisch` werden die ersten drei Karten von `funktionen.reihen` (dann 8 Karten, Titel „Folgen und Reihen“). Ausnahme von der Regel „B in einen Gym-Flug“: Die Schreibweise aₙ braucht nur der Reihen-Flug.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `explizit` Folgenglieder berechnen | **A** | `terme.aufstellen`/muster „Figurenfolgen mit Termen beschreiben“ (6) | „Gib die ersten drei Glieder von aₙ = 2n − 1 an.“ · „Ist 109 ein Glied der Folge aₙ = 6n + 7?“ | „Plättchen in einer Figurenfolge: Figur 1: 5, Figur 2: 7, Figur 3: 9. Gib einen Term für die Anzahl bei Figur n an.“ · „Plättchen in einer Figurenfolge: Figur 1: 4, Figur 2: 9, Figur 3: 14. Gib einen Term für die Anzahl bei Figur n an.“ |  |
| `rekursiv` Rekursiv weiterrechnen | **C** | – |  |  |  |
| `arithmetisch` Arithmetische Folgen | **B** | `terme.aufstellen`/muster „Figurenfolgen mit Termen beschreiben“ (6) | „Arithmetische Folge mit a₁ = −3 und a₆ = −23. Berechne d.“ · „Arithmetische Folge mit a₁ = 15 und a₅ = 7. Berechne d.“ | „Plättchen in einer Figurenfolge: Figur 1: 5, Figur 2: 7, Figur 3: 9. Gib einen Term für die Anzahl bei Figur n an.“ · „Plättchen in einer Figurenfolge: Figur 1: 4, Figur 2: 9, Figur 3: 14. Gib einen Term für die Anzahl bei Figur n an.“ | Gleicher Gedanke („Zunahme pro Figur vor dem n“), neue Schreibweise aₙ = a₁ + (n − 1)·d. |
| `geometrisch` Geometrische Folgen | **B** | `funktionen.exponential_log`/linear_oder_exponentiell „Linear oder exponentiell?“ (10) | „Bestimme den Faktor q der geometrischen Folge 1; 2; 4; 8; …“ · „Geometrische Folge 1; −2; 4; −8; … Berechne a₁₀.“ | „Bei den Werten 3; 6; 12; 24 ist der Quotient aufeinanderfolgender Werte immer gleich. Wie groß ist er?“ | Gleicher Gedanke (Faktor), neue Schreibweise aₙ = a₁·qⁿ⁻¹. |
| `erkennen` Folgen erkennen und prüfen | **A** | `funktionen.exponential_log`/linear_oder_exponentiell „Linear oder exponentiell?“ (10) | „Arithmetische Folge mit a₁ = 6, d = 8. Nina rechnet a₁₈ = 6 + 18 · 8 = 150. Stimmt das?“ · „Geometrische Folge mit a₁ = 4, q = 3. Lars rechnet a₈ = (4 · 3)⁷ = 35 831 808. Stimmt das?“ | „Wächst oder fällt die Größe in der Tabelle linear oder exponentiell?“ · „Wächst oder fällt die Größe in der Tabelle linear oder exponentiell?“ |  |

### `terme.quadratische_extreme` – Quadratische Terme und Extremwerte (Plan heute 8, RS 8) → **auflösen (Sonderfall)**

Lehrplan: M8 LB4 (I) / LB3 (II/III) Extremwerte von ax² + bx + c. Pflicht: RS alle Zweige Kl. 8. Inhaltlich vollständig in `funktionen.quadratisch` (umformen, scheitel, extremwert) und `terme.umformen`/binomisch. **Aber:** `funktionen.quadratisch` hat Plan-Klasse 9, die Realschule verlangt den Stoff in Kl. 8 (alle Zweige). Auflösen bricht den Mindeststand um ein Jahr → Entscheidung 2.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `ergaenzen` Zum Binom ergänzen | **A** | `terme.umformen`/binomisch „Binomische Formeln“ (7) | „a) Welche Zahl musst du zu x² + 14x addieren, damit ein Binom entsteht? b) Schreibe das Binom als Quadrat. c) Welchen Wert hat es für x …“ · „Ergänze so, dass ein Binom entsteht.“ | „Für welche positive Zahl k lässt sich x² + kx + 16 als Quadrat (x + □)² schreiben?“ · „Ergänze so, dass eine binomische Formel entsteht: (□x − 3)² = 4x² − □x + 9“ |  |
| `scheitelform` Quadratische Ergänzung | **A** | `funktionen.quadratisch`/umformen „Von der allgemeinen zur Scheitelform“ (9) | „Bringe T(x) = x² + 8x + 6 mit quadratischer Ergänzung in die Form (x + □)² + □.“ · „Bringe T(x) = x² − 10x + 18 mit quadratischer Ergänzung in die Form (x + □)² + □.“ | „Bestimme den Scheitel von y = x² − 14x + 42.“ · „Bestimme den Scheitel von y = 2x² − 8x.“ |  |
| `extremwert` Minimum oder Maximum ablesen | **A** | `funktionen.quadratisch`/scheitel „Scheitelpunkt ablesen“ (9) | „Bestimme Stelle und Wert des Extremums von T(x) = −(x − 4)² + 14.“ · „Bestimme Stelle und Wert des Extremums von T(x) = −(x − 5)².“ | „Gib den Scheitel der Parabel y = 0,5(x − 4)² − 1 an.“ · „Eine Parabel y = (x − x₁)(x − x₂) hat die Nullstellen −1 und 5. Gib ihren Scheitel an.“ |  |
| `mit_faktor` Terme mit Faktor vor x² | **A** | `funktionen.quadratisch`/umformen „Von der allgemeinen zur Scheitelform“ (9) | „Bestimme Stelle und Wert des Extremums von T(x) = 0,5x² − 4x + 10.“ · „Bestimme Stelle und Wert des Extremums von T(x) = 2x² − 16x + 37.“ | „Bestimme den Scheitel von y = −x² − 12x − 41.“ · „Bestimme den Scheitel von y = −2x² + 12x − 17.“ |  |
| `optimierung` Optimierungsaufgaben | **A** | `funktionen.quadratisch`/extremwert „Extremwertprobleme lösen“ (9) | „An einer Mauer wird mit 40 m Zaun ein Rechteck abgegrenzt (Mauer als eine Seite). Wie groß kann die Fläche höchstens werden?“ · „An einer Mauer wird mit 60 m Zaun ein Rechteck abgegrenzt (Mauer als eine Seite). Wie groß kann die Fläche höchstens werden?“ | „Mit 16 m Zaun wird an einer Mauer ein rechteckiges Gehege gebaut (die Mauer ist eine Seite). Jedes Huhn braucht mindestens 3 m². Wie …“ · „Ein rechteckiges Gehege soll mit 108 m Zaun umgeben werden. Welchen größten Flächeninhalt kann es haben?“ |  |

### `sonder.optimierung` – Lineare Optimierung (Plan heute 8, IB 5) → **bleibt**

Lehrplan: IB Extended; H5E Kap. 12E–F. Pflicht: nur IB (Extended). Gym löst Ungleichungen nur mit einer Variablen; Eckpunkte rechnen = LGS (Gym Kl. 8), deshalb `ecken` als B im Flug.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `bereich` Liegt ein Punkt im Bereich? | **C** | – |  |  | Gym löst Ungleichungen nur mit einer Variablen, auch am Graphen (`gleichungen.ungleichungen`/grafisch). |
| `aufstellen` Bedingungen aufstellen | **C** | – |  |  |  |
| `ecken` Eckpunkte berechnen | **B** | `gleichungen.lgs2`/sachaufgabe „Sachaufgaben mit zwei Unbekannten“ (8) | „Wo schneidet die Randgerade x + 8y = 40 die y-Achse?“ · „Wo schneidet die Randgerade 2x + y = 10 die x-Achse?“ | „Ein Bleistift und ein Heft kosten zusammen 2,30 €. Das Heft kostet 1,10 € mehr als der Bleistift. Was kostet der Bleistift?“ · „Eine Eintrittskarte kostet für Erwachsene 15 €, für Kinder 8 €. Eine Gruppe aus 45 Personen zahlt 563 €. Wie viele Kinder sind dabei?“ | Eckpunkt = Gleichungssystem (Gym Kl. 8); bleibt im Flug, weil Teil des Verfahrens. |
| `optimum` Das Optimum finden | **C** | – |  |  |  |
| `sach` Optimierung im Sachzusammenhang | **C** | – |  |  |  |

### `gleichungen.reinquadratisch` – Reinquadratische Gleichungen (Plan heute 9, RS 9, IB 4) → **auflösen**

Lehrplan: M9 LB1 x² = a. Pflicht: RS alle Zweige Kl. 9; IB Standard. Alle 6 Karten haben einen Gym-Gegenpart in derselben Plan-Klasse 9, bis zur gleichen Sachaufgabe („Würfel mit Oberfläche … – Kante?“). Nichts zu ergänzen.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `schaetzen` Wurzeln einschätzen | **A** | `zahlen.wurzeln_basis`/abschaetzen „Zwischen welchen Zahlen liegt √a?“ (9) | „Liegt √188 näher an 13 oder an 14?“ · „Liegt √244 näher an 15 oder an 16?“ | „Für welche natürlichen Zahlen n gilt 6 < √n < 7? Gib die kleinste und die größte an.“ · „Welche Zahl ist am größten: 3,2; √10 oder ∛30?“ |  |
| `grundform` x² = a lösen | **A** | `gleichungen.quadratisch`/reinquadratisch „Gleichungen ohne x-Glied lösen“ (9) | „Löse x² = 5,76.“ · „Löse x² = 2,25.“ | „Löse 4x² − 196 = 0.“ · „Löse (x + 4)² = 16.“ |  |
| `umformen` Erst nach x² auflösen | **A** | `gleichungen.quadratisch`/reinquadratisch „Gleichungen ohne x-Glied lösen“ (9) | „Löse 3x² − 132 = x² − 34.“ · „Löse 3x² − 32 = x² + 0.“ | „Löse 6x² − 6 = 0.“ · „Löse 3x² − 300 = 0.“ |  |
| `gerundet` Lösungen runden | **A** | `gleichungen.potenz`/gerade „xⁿ = c mit geradem Exponenten“ (9) | „Ein Rechteck ist 6 cm breit und 15 cm lang. Ein Quadrat soll denselben Flächeninhalt haben. Wie lang ist seine Seite? Runde auf zwei …“ · „Löse 2x² − 24 = 546. Gib die positive Lösung auf zwei Dezimalen gerundet an.“ | „Löse x² = 1.“ · „Löse x² = 150. Gib die Lösungen exakt an.“ |  |
| `klammer` Quadrat einer Klammer: (x − p)² = q | **A** | `gleichungen.quadratisch`/reinquadratisch „Gleichungen ohne x-Glied lösen“ (9) | „Löse (x + 4)² = 1.“ · „Löse (x + 3)² = 4.“ | „Löse (x + 2)² = 25.“ · „Löse (x − 1)² = (2x + 1)². (kleinere Lösung zuerst)“ |  |
| `sachaufgabe` Sachaufgaben mit x² = a | **A** | `zahlen.wurzeln_basis`/wurzel_sache „Seitenlänge aus Fläche und Volumen“ (9) | „Ein Würfel hat eine Oberfläche von 150 cm². Wie lang ist eine Kante?“ | „Ein Würfel hat eine Oberfläche von 486 cm². Wie lang ist eine Kante?“ · „Ein Würfel hat ein Volumen von 1 331 cm³. Wie lang ist eine Kante?“ |  |

### `funktionen.transformation` – Graphentransformation (Plan heute 9, RS 9, IB 5) → **auflösen**

Lehrplan: M9 LB7 (I) Parameter der Scheitelform; M10 LB2 (I) Abbildungen von Graphen. Pflicht: RS Gruppe I Kl. 9 (II/III Kl. 10); Karte `punkte`: RS Gruppe I Kl. 10; IB Extended (Annahme). 4 von 6 Karten = `funktionen.quadratisch`/parameter und scheitel. Spiegeln: 3–4 Aufgaben in `parameter`. Die C-Karte `punkte` (P → P′ bei a·f(x − d) + e) wird **Pflichtkarte für RS-I / Vertiefung für Gym** in `funktionen.exponential_log` nach `graph` – dort, wo Verschieben schon für bˣ und log vorkommt. Damit ist auch das vorgeschlagene neue Thema „Graphen abbilden“ erledigt (Teil 3a).

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `nach_oben` Nach oben oder unten verschieben | **A** | `funktionen.quadratisch`/parameter „Was bewirken a, d und e?“ (9) | „Die Normalparabel wird um 1 nach unten verschoben. Welche Gleichung gehört dazu?“ · „Die Normalparabel wird um 6 nach unten verschoben. Welchen y-Wert hat die neue Parabel bei x = 2?“ | „Die Normalparabel wird um 1 nach rechts und um 6 nach oben verschoben. Welche Gleichung hat die neue Parabel?“ · „Die Normalparabel wird um d nach rechts verschoben (d > 0). Die neue Parabel geht durch (5 \| 9). Welche Werte kann d haben? (kleineres …“ |  |
| `nach_rechts` Nach links oder rechts verschieben | **A** | `funktionen.quadratisch`/parameter „Was bewirken a, d und e?“ (9) | „Die Parabel y = (x + 3)² wird um 5 nach links verschoben. Wie lautet die neue Gleichung?“ · „Die Normalparabel wird um 3 nach rechts verschoben. Welche Gleichung gehört dazu?“ | „Die Normalparabel wird um 1 nach rechts und um 6 nach oben verschoben. Welche Gleichung hat die neue Parabel?“ · „Die Normalparabel wird um d nach rechts verschoben (d > 0). Die neue Parabel geht durch (5 \| 9). Welche Werte kann d haben? (kleineres …“ |  |
| `strecken` Strecken, stauchen, nach unten öffnen | **A** | `funktionen.quadratisch`/parameter „Was bewirken a, d und e?“ (9) | „Welche Parabel ist enger: y = 1,5x² oder y = 2x²?“ · „Berechne den y-Wert von y = 0,25x² an der Stelle x = 1.“ | „Eine Rutsche hat im Querschnitt die Form y = 0,25(x − 4)² (in m). Wie ist sie im Vergleich zur Normalparabel?“ · „Wie sieht die Parabel y = −0,25(x − 1)² + 2 im Vergleich zur Normalparabel aus?“ |  |
| `spiegeln` An den Achsen spiegeln | **B** | `funktionen.quadratisch`/scheitel „Scheitelpunkt ablesen“ (9) | „Die Parabel y = (x + 3)² − 3 wird an der y-Achse gespiegelt. Gib den Scheitel der Bildparabel an.“ · „Die Parabel y = (x + 4)² − 4 wird an der y-Achse gespiegelt. Gib den Scheitel der Bildparabel an.“ | „Die Parabel y = (x − 3)² − 4 wird erst an der x-Achse gespiegelt und dann um 6 nach oben verschoben. Wo liegt der neue Scheitel?“ | Im Gym-Flug nur Einzelaufgaben (Spiegeln an der x-Achse, auch `funktionen.exponential_log`/graph); 3–4 Aufgaben in `funktionen.quadratisch`/parameter. |
| `kombiniert` Mehrere Schritte: y = a(x − d)² + e | **A** | `funktionen.quadratisch`/scheitel „Scheitelpunkt ablesen“ (9) | „Die gezeichnete Parabel hat die Form y = a(x − d)² + e mit a = 1 oder a = −1. Gib a und den Scheitel an.“ · „Berechne den y-Wert von y = 3(x − 4)² − 6 an der Stelle x = 3.“ | „Gib den Scheitel der Parabel y = 2(x + 6)² − 1 an.“ · „Gib den Scheitel der Parabel y = (x − 6)² − 4 an.“ |  |
| `punkte` Punkte mit abbilden | **C** | – |  |  | P(x\|y) → P′ bei g(x) = a·f(x − d) + e für beliebiges f: im Gym nur eine Einzelaufgabe (`funktionen.ganzrational`/graph_term). Als Lernkarte nach `funktionen.exponential_log`/graph (RS M10 LB2 I). |

### `funktionen.betrag` – Betragsfunktion (Plan heute 9, IB 5) → **bleibt**

Lehrplan: IB H5E Kap. 20F; Betrag als Zahl MYP 1–3. Pflicht: nur IB (Extended, Annahme). Gym kennt den Betrag nur als Zahl (Kl. 5); Graph, stückweise Darstellung, Betragsgleichungen fehlen.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `betrag` Betrag berechnen | **B** | `zahlen.ganz`/betrag „Betrag und Gegenzahl“ (5) | „Ein Aufzug fährt vom 2. Untergeschoss (−2) in den 5. Stock und dann ins 1. Untergeschoss (−1). Wie viele Stockwerke legt er insgesamt …“ · „Eine Zahl x liegt rechts von 1 auf dem Zahlenstrahl. Es gilt \|x − 1\| = 4. Welche Zahl ist x?“ | „Welche Zahlen haben den Betrag 23?“ · „Wie viele ganze Zahlen haben einen Betrag kleiner als 4?“ | Betrag einer Zahl = Gym Kl. 5; \|a − b\| als Abstand ist neu. Bleibt als Einstieg. |
| `graph` Graph und Knickpunkt | **C** | – |  |  |  |
| `stueckweise` Stückweise ohne Betrag schreiben | **C** | – |  |  |  |
| `gleichung` Betragsgleichungen lösen | **C** | – |  |  |  |
| `verstehen` Aussagen über Beträge prüfen | **C** | – |  |  |  |

### `gleichungen.wurzel` – Wurzelgleichungen (Plan heute 9, RS 9) → **bleibt**

Lehrplan: M9 LB7 (I) Wurzelgleichungen mit Definitionsmenge; II/III und IB kein Beleg. Pflicht: nur RS Gruppe I. Gym hat nur √x = c und „Wann ist √(x − 4) erklärt?“; das Lösen mit Quadrieren und Scheinlösungen fehlt.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `definitionsmenge` Wann ist die Wurzel definiert? | **B** | `zahlen.wurzeln_basis`/wurzel_deuten „Wurzeln richtig deuten“ (9) | „Gib die Definitionsmenge der Gleichung √(x − 5) = √(x − 8) + 1 an.“ · „Für welche Zahlen a liegt die 0 in der Definitionsmenge von √(x + a)?“ | „Für welche Zahlen x ist √(x − 4) erklärt?“ | Im Gym-Flug eine Einzelaufgabe; bleibt als Einstieg im Flug. |
| `quadrieren` Durch Quadrieren lösen | **C** | – |  |  | Gym hat nur √x = c (`zahlen.wurzeln_basis`/quadratwurzel), keinen Term unter der Wurzel. |
| `isolieren` Erst die Wurzel allein stellen | **C** | – |  |  |  |
| `probe` Probe und Scheinlösungen | **C** | – |  |  | Scheinlösungen kennt der Gym-Flug nur bei Bruchgleichungen (Definitionsmenge), nicht durch Quadrieren. |
| `zwei_seiten` Wurzel und x auf beiden Seiten | **C** | – |  |  |  |
| `sachaufgabe` Formeln mit Wurzeln | **C** | – |  |  |  |

### `daten.standardabweichung` – Standardabweichung (Plan heute 9, IB 5) → **bleibt**

Lehrplan: IB Extended; H5E Kap. 18G. Pflicht: nur IB (Extended). Gym misst Streuung nur mit Spannweite und Quartilsabstand.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `abweichung` Abweichungen vom Mittelwert | **B** | `daten.kennwerte`/mittel_rueckwaerts „Rückwärts rechnen mit dem Mittelwert“ (6) | „Der Mittelwert eines Datensatzes ist 60. Ein Wert hat die Abweichung −11. Wie groß ist dieser Wert?“ · „Der Mittelwert eines Datensatzes ist 21. Ein Wert hat die Abweichung −10. Wie groß ist dieser Wert?“ | „5 Kinder haben im Mittel 13 Bücher gelesen. Wie viele Bücher sind das zusammen?“ · „Der Mittelwert von 3, 8, 10 und x ist genauso groß wie x. Wie groß ist x?“ | Mittelwert-Teil = Gym Kl. 6; „Abweichungen summieren sich zu 0“ ist neu. Bleibt als Einstieg. |
| `varianz` Die Varianz berechnen | **C** | – |  |  |  |
| `sigma` Die Standardabweichung σ | **C** | – |  |  |  |
| `eigenschaften` Wie verändert sich σ? | **C** | – |  |  |  |
| `deuten` Streuung vergleichen und deuten | **C** | – |  |  | Streuung vergleichen kennt `daten.boxplot`/vergleichen nur mit Box und Antennen. |

### `funktionen.umkehr` – Umkehrfunktionen (Plan heute 10, RS 10, IB 5) → **auflösen**

Lehrplan: M10 LB3 und LB4 (I) Umkehrfunktion. Pflicht: RS Gruppe I Kl. 10; IB Enrichment. Nur 2 C-Karten (`umkehrbar`, `linear`) – zu wenig für einen Rest-Flug (Regel: mindestens 3). Vorschlag: beide als neue Karten in `funktionen.potenz` **vor** `wurzelfunktion` (Pflicht RS-I, für Gym Vertiefung, Annahme: Gym-Lehrplan nicht geprüft); `quadratisch` und `spiegeln` als je 3–4 Aufgaben in `wurzelfunktion`. Alternative (Meinung: schlechter): Rest-Flug aus `umkehrbar`, `linear`, `spiegeln` (3 Karten) in Kl. 10.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `umkehrbar` Ist eine Funktion umkehrbar? | **C** | – |  |  |  |
| `werte` Werte der Umkehrfunktion | **A** | `funktionen.grundbegriffe`/stelle „Zu einem y-Wert das x finden“ (8) | „Für eine Funktion f gilt f(2) = 7 und f(7) = 2. Berechne f⁻¹(f⁻¹(2)).“ · „Eine Taxifahrt kostet f(x) = 2x + 3 Euro für x km. Eine Fahrt kostet 19 €. Wie lang war sie? Berechne f⁻¹(19).“ | „Eine Kerze ist nach t Stunden h(t) = 24 − 1,5t cm hoch. Wann ist sie nur noch 15 cm hoch?“ · „Die Funktion f(x) = −2x + 7 hat an der Stelle a den Wert 1. Berechne a und dann f(a + 1). Gib f(a + 1) an.“ |  |
| `linear` Umkehrfunktion einer Geraden | **C** | – |  |  |  |
| `quadratisch` Umkehrfunktion einer Parabel | **B** | `funktionen.potenz`/wurzelfunktion „Wurzelfunktionen und Umkehrung“ (9) | „Jemand gibt für f(x) = (x − 1)² + 2 mit x ≥ 1 die Umkehrfunktion f⁻¹(x) = √(x − 1) + 2 an. Was stimmt?“ · „Gib die Definitionsmenge der Umkehrfunktion von f(x) = (x − 4)² + 3 mit x ≥ 4 an.“ | „Jemand sagt: „Die Umkehrfunktion von f(x) = x² (x ≥ 0) ist g(x) = 1/x².“ Was stimmt?“ · „f(x) = 2x³ für x ≥ 0. Für welches x ist f(x) = 250?“ | Gym: nur x² und x³ für x ≥ 0; verschobene Parabelast-Aufgaben ergänzen. |
| `exp_log` Exponential- und Logarithmusfunktion | **A** | `funktionen.exponential_log`/logfunktion „Die Logarithmusfunktion“ (10) | „Jemand rechnet log₅ 25 = 5. Was stimmt?“ · „P(2 \| 100) liegt auf dem Graphen von y = 10ˣ. Welcher Punkt liegt auf dem Graphen von y = lg x?“ | „Berechne f(10) für f(x) = lg(x).“ · „Berechne ohne Taschenrechner: lg(0,01).“ |  |
| `spiegeln` Graph der Umkehrfunktion | **B** | `funktionen.potenz`/wurzelfunktion „Wurzelfunktionen und Umkehrung“ (9) | „Der Graph von f geht durch P(4 \| 1) und Q(1 \| 5). Durch welchen Punkt geht der Graph von f⁻¹ sicher?“ · „Der Punkt P(1 \| −5) liegt auf der gezeichneten Geraden f. Welcher Punkt liegt auf f⁻¹?“ | „Der Punkt (2 \| 4) liegt auf dem Graphen von y = x². Welcher Punkt liegt dann auf dem Graphen von y = √x?“ · „Im Bild siehst du y = x² (für x ≥ 0), y = √x und die Gerade y = x. Wie liegen die beiden Kurven zueinander?“ | Gym: eine Bildaufgabe mit y = x; 3–4 Aufgaben ergänzen. |

### `funktionen.reihen` – Reihen (Plan heute 10, IB 5) → **bleibt**

Lehrplan: IB Enrichment; H5E Kap. 22E–G („nicht im Framework“). Pflicht: keines (Zusatz). Nur eine Knobelaufgabe 1 + 2 + … + 20 im Gym. Nimmt die 3 Folgen-Karten auf.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `summenzeichen` Das Summenzeichen ∑ | **C** | – |  |  |  |
| `arith` Arithmetische Reihen | **C** | – |  |  | Im Gym nur eine Knobelaufgabe 1 + 2 + … + 20 (`zahlen.rechengesetze`/vorteil). |
| `geom` Geometrische Reihen | **C** | – |  |  |  |
| `sach` Reihen in Sachaufgaben | **C** | – |  |  |  |
| `verstehen` Fehler bei Reihen finden | **C** | – |  |  |  |

### `stochastik.bedingt` – Bedingte Wahrscheinlichkeit (Plan heute 10, IB 5) → **auflösen**

Lehrplan: IB H5E Kap. 17H; abhängige Ereignisse H4 Kap. 26E. Pflicht: nur IB (Extended). P(A | B) aus Tafel und Formel, Ziehen ohne Zurücklegen, P(A | B) ≠ P(B | A) stehen im Gym. Neu nur „unabhängig prüfen“: als Karte in `stochastik.mehrstufig` nach `ohne_zuruecklegen` (Vertiefung). Die 1000-Fälle-Methode als Aufgaben in `stochastik.verknuepft`/bedingt. **Haken:** `stochastik.verknuepft`/bedingt ist seit Teil A Vertiefung – für IB-Extended passt das.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `tafel` P(A \| B) aus der Vierfeldertafel | **A** | `stochastik.verknuepft`/bedingt „Bedingte Wahrscheinlichkeit“ (Vertiefung) (9) | „Die Vierfeldertafel zeigt 200 Befragte einer Umfrage. Berechne P(liest keine E-Books \| unter 30). Gib das Ergebnis als gekürzten Bruch an.“ · „Die Vierfeldertafel zeigt 100 Besucher eines Kinos. Ein Feld fehlt. Berechne P(Erwachsene \| Popcorn gekauft). Gib das Ergebnis als …“ | „Die Tafel zeigt 100 Besucher eines Freibads. A: „ist Erwachsener“, B: „hat eine Jahreskarte“. Ein Besucher mit Merkmal A wird zufällig …“ · „Die Tafel zeigt 200 Mitglieder eines Fußballvereins. A: „spielt in einer Mannschaft“, B: „ist jünger als 18 Jahre“. Ein Vereinsmitglied …“ |  |
| `formel` Die Formel P(A \| B) | **A** | `stochastik.verknuepft`/bedingt „Bedingte Wahrscheinlichkeit“ (Vertiefung) (9) | „P(B) = 0,02, P(A \| B) = 0,9. Berechne P(A ∩ B).“ · „P(B) = 0,4, P(A ∩ B) = 0,08. Berechne P(A \| B).“ | „Berechne P_B(A), also die Wahrscheinlichkeit für A unter der Bedingung B, als Dezimalzahl.“ · „Es gilt P(A ∩ B) = 0,12 und P_B(A) = 0,4. Wie groß ist P(B)?“ |  |
| `baum` Ziehen ohne Zurücklegen | **A** | `stochastik.mehrstufig`/ohne_zuruecklegen „Ziehen ohne Zurücklegen“ (10) | „In einer Urne liegen 3 rote und 3 blaue Kugeln. Es werden zwei Kugeln ohne Zurücklegen gezogen. Berechne P(erst rot, dann blau).“ · „In einer Urne liegen 4 rote und 4 blaue Kugeln. Es werden zwei Kugeln ohne Zurücklegen gezogen. Berechne P(zweimal rot).“ | „In einer Urne liegen 4 blaue und 11 weiße Kugeln. Man zieht ohne Zurücklegen. Bei welchem Zug hat man spätestens sicher eine blaue Kugel …“ · „In einer Urne liegen 4 rote und 6 grüne Kugeln. Zwei werden ohne Zurücklegen gezogen. Wie groß ist P(zuerst rot, dann grün)?“ |  |
| `unabhaengig` Abhängig oder unabhängig? | **C** | – |  |  | „unabhängig“ steht im Gym nur als Voraussetzung (`stochastik.mehrstufig`), nie als Prüfung P(A ∩ B) = P(A) · P(B). |
| `rueckschluss` Rückschlüsse mit 1000 Fällen | **B** | `stochastik.verknuepft`/bedingt „Bedingte Wahrscheinlichkeit“ (Vertiefung) (9) | „2 % der Geräte sind defekt. Ein Prüfgerät meldet 80 % dieser Geräte, aber irrtümlich auch 10 % der übrigen. Stelle dir 1 000 Geräte vor. …“ · „10 % der Geräte sind defekt. Ein Prüfgerät meldet 100 % dieser Geräte, aber irrtümlich auch 5 % der übrigen. Stelle dir 1 000 Geräte …“ | „Berechne mit dem Baumdiagramm P(B).“ · „Berechne mit dem Baumdiagramm P_B(A) als gekürzten Bruch.“ | Rückwärts-Bedingung gibt es dort mit Baumdiagramm; die 1000-Fälle-Methode ist neu (Vertiefung). |
| `verstehen` Bedingungen richtig lesen | **A** | `stochastik.verknuepft`/bedingt „Bedingte Wahrscheinlichkeit“ (Vertiefung) (9) | „Von 258 Kindern einer Schule spielen 44 im Schulorchester. 42 der Orchesterkinder spielen Geige, außerhalb des Orchesters niemand. Wie …“ · „„Unter den Kunden mit Kundenkarte zahlen 40 % mit dem Handy.“ Wie schreibt man das als Wahrscheinlichkeit?“ | „Die Tafel zeigt 100 Besucher eines Freibads. A: „ist Erwachsener“, B: „hat eine Jahreskarte“. Ein Besucher mit Merkmal A wird zufällig …“ · „Die Tafel zeigt 200 Mitglieder eines Fußballvereins. A: „spielt in einer Mannschaft“, B: „ist jünger als 18 Jahre“. Ein Vereinsmitglied …“ |  |

### `daten.normalverteilung` – Normalverteilung (Plan heute 10, IB 5) → **bleibt**

Lehrplan: IB: kein Beleg im Framework; H5E Kap. 18H. Pflicht: keines (Zusatz). Braucht σ aus `daten.standardabweichung`.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `eigenschaften` Die Glockenkurve | **C** | – |  |  |  |
| `regel` Die 68-95-99,7-Regel | **C** | – |  |  |  |
| `anteile` Anteile in Teilbereichen | **C** | – |  |  |  |
| `zwert` Der z-Wert | **C** | – |  |  |  |
| `vergleichen` Vergleichen und beurteilen | **C** | – |  |  |  |

### `abbildungen.matrizen` – Matrizen und Abbildungen mit Matrizen (Plan heute 10, RS 10, IB 5) → **bleibt**

Lehrplan: M10 LB2 (I) Abbildungen mit Matrizen; Skalarprodukt M10 LB1 (I); Matrizenprodukt/Umkehrmatrix kein Beleg. IB: Guide 2020 kein Beleg. Pflicht: nur RS Gruppe I (Karten `rechnen`, `inverse`: keines → Vertiefung). Gym 5–10 hat weder Vektoren noch Matrizen.

| Lernkarte | Gr. | Gym-Gegenstück (Plan-Klasse) | Beleg RS/IB-Flug | Beleg Gym-Flug | Hinweis |
|---|---|---|---|---|---|
| `bildpunkt` Bildpunkte mit einer Matrix | **C** | – |  |  |  |
| `abbildungsmatrix` Matrizen bekannter Abbildungen | **C** | – |  |  | Sonderfall 90°-Drehung ohne Matrix steht in `abbildungen.kongruenz`/drehung (Vertiefung). |
| `drehung` Drehung um einen beliebigen Winkel | **C** | – |  |  |  |
| `rechnen` Mit Matrizen rechnen | **C** | – |  |  | RS: kein Lehrplan-Beleg (Zusatz). |
| `inverse` Determinante und Umkehrmatrix | **C** | – |  |  | RS: kein Lehrplan-Beleg (Zusatz). |
| `skalarprodukt` Skalarprodukt und Winkel | **C** | – |  |  |  |
---

## Teil 3 – Gegenprobe in die andere Richtung

### 3a – Die vier neuen Themen aus `vorschlag-mindeststand.md` Punkt 6

Dieselbe Einordnung, Lernkarte für Lernkarte (Stichworte dort). Belege kurz; Gym-Lernkarten mit Plan-Klasse.

**„Vierecke und Drehung“ (RS M8 LB1 I/II, M8 LB2 I) → kein neues Thema.** A 7 · B 1 · C 0

| geplante Lernkarte | Gr. | steht schon in |
|---|---|---|
| Haus der Vierecke | A | `geometrie.grundbegriffe`/vierecke (5), `abbildungen.kongruenz`/vierecke_ordnen (6) – Merksatz dort: „Je mehr Symmetrie, desto weiter unten im Haus der Vierecke.“ |
| Viereck aus Eigenschaften bestimmen | A | `abbildungen.kongruenz`/vierecke_ordnen: „Eine Tischplatte hat vier gleich lange Seiten, aber keinen rechten Winkel. Welches Viereck ist sie?“ |
| Winkel im Viereck | A | `geometrie.winkelsaetze`/vieleck und figuren (7), `geometrie.konstruktion`/vierecke (7): „In einem Parallelogramm ABCD ist α = 95°. Wie groß ist β?“ |
| Ist das Viereck konstruierbar? | B | `geometrie.konstruktion`/konstruierbar (7) nur für Dreiecke → 3–4 Viereck-Aufgaben dort |
| Um einen Punkt drehen (90°, 180°) | A | `abbildungen.kongruenz`/drehung (6, **Vertiefung**): „Drehe P(2 \| 1) um O(0 \| 0) um 90° gegen den Uhrzeigersinn.“ |
| Drehsymmetrie | A | `abbildungen.kongruenz`/symmetrie: „Ein Windrad hat drei gleiche Flügel. Um welchen kleinsten Winkel muss es sich drehen …?“ |
| Vektor um ±90°, 180° drehen | A | `abbildungen.kongruenz`/drehung, Merksatz: „90° links herum: aus (x \| y) wird (−y \| x).“ |
| Was bleibt bei der Drehung gleich? | A | `abbildungen.kongruenz`/eigenschaften: „Ein Winkel von 37° wird um einen Punkt um 90° gedreht. Wie groß ist der Bildwinkel?“ |

**„Zentrische Streckung im Koordinatensystem“ (RS M9 LB2 I) → kein neues Thema.** A 4 · B 2 · C 2

| geplante Lernkarte | Gr. | steht schon in / Vorschlag |
|---|---|---|
| Zahl mal Vektor | B | `abbildungen.aehnlichkeit`/streckung rechnet mit Koordinaten, ohne Vektorschreibweise → Wort ergänzen |
| Bildpunkt berechnen | A | `abbildungen.aehnlichkeit`/streckung (9): „Strecke den Punkt P(2 \| 0) zentrisch mit dem Zentrum Z(1 \| 1) und k = 2.“ |
| Streckungsfaktor aus Punkt und Bildpunkt | A | ebd.: „ZP = 6 cm und ZP' = 9 cm … Bestimme k.“; „P(−3 \| −7) wird mit k = 3 auf P'(−11 \| −15) abgebildet. Wo liegt das Zentrum Z?“ |
| negativer Faktor | A | ebd.: „Strecke P(1 \| 2) zentrisch mit dem Zentrum Z(3 \| 0) und k = −2.“ |
| Bildgerade und Bildparabel | C | → neue Lernkarte in `abbildungen.aehnlichkeit` nach `streckung` (Pflicht RS-I, Gym Vertiefung) |
| Strecke im Verhältnis teilen, Goldener Schnitt | B | `abbildungen.aehnlichkeit`/strahlensatz2: „In welchem Verhältnis teilt M die Diagonale AC?“ → 3–4 Aufgaben |
| Schwerpunkt des Dreiecks rechnerisch | C | Textsuche „Schwerpunkt“, „Seitenhalbierende“: 0 Treffer → neue Lernkarte in `abbildungen.aehnlichkeit` (Pflicht RS-I, Gym Vertiefung) |
| Flächen mal k² | A | `abbildungen.aehnlichkeit`/flaeche_volumen |

**„Trigonometrie – Ergänzungen“ (RS M10 LB1 I) → kein neues Thema.** A 4 · B 1 · C 3

| geplante Lernkarte | Gr. | steht schon in / Vorschlag |
|---|---|---|
| Steigungswinkel m = tan α | A | `trigo.rechtwinklig`/anwendung (9): „Eine Straße hat 12 % Steigung. Wie groß ist der Steigungswinkel?“; `gleichungen.trig`/tangens |
| Schnittwinkel zweier Geraden | C | → neue Lernkarte in `trigo.rechtwinklig` nach `anwendung` (Pflicht RS-I, Gym Vertiefung) |
| Graph der Tangensfunktion | B | `gleichungen.trig`/tangens hat tan-Lösungen und Periode, `funktionen.trig` nur sin/cos → 3–4 Graph-Aufgaben in `funktionen.trig`/zuordnen |
| sin(90° − α) = cos α, sin(180° − α) = sin α | A | `trigo.rechtwinklig`/beziehungen (Merksatz: „sin α = cos(90° − α)“), `trigo.allgemein`/einheitskreis (Merksatz: „sin(180° − α) = sin α“) |
| sin² α + cos² α = 1 | A | `trigo.rechtwinklig`/beziehungen: „Für einen spitzen Winkel β gilt cos β = 0,96. Berechne sin β.“ |
| Additionstheoreme | C | Textsuche: 0 Treffer (nur im `umfang` von `trigo.allgemein`) → neue Lernkarte in `trigo.allgemein` (Pflicht RS-I, Gym Vertiefung) |
| Winkel zwischen zwei Vektoren | A | `abbildungen.matrizen`/skalarprodukt (RS-Flug, bleibt): „Berechne den Winkel zwischen a = (−8 \| 6) und b = (3 \| 0) …“ |
| Abstand Punkt–Gerade | C | → neue Lernkarte in `abbildungen.matrizen` nach `skalarprodukt` (Pflicht RS-I) |

**„Graphen abbilden“ (RS M10 LB2 I) → kein neues Thema.** A 4 · B 3 · C 0 (der neue Kern steckt in der Karte `funktionen.transformation`/punkte, Teil 2)

| geplante Lernkarte | Gr. | steht schon in |
|---|---|---|
| Verschieben y = f(x − d) + e | A | `funktionen.gebrochen`/parameter (10 Aufgaben, z. B. „g(x) = 3/x … um 5 nach rechts und um 2 nach oben verschoben“), `funktionen.trig`/verschiebung_x, `funktionen.exponential_log`/graph |
| Strecken y = a · f(x) | A | `funktionen.trig`/zuordnen: „Der Graph von sin x wird in y-Richtung mit dem Faktor 3 gestreckt …“ |
| Spiegeln an den Achsen | B | nur Einzelaufgaben (`funktionen.exponential_log`/graph: „… an der x-Achse gespiegelt und danach um 4 nach oben verschoben“) → mit der Karte `punkte` abgedeckt |
| Asymptoten mitverschieben | A | `funktionen.gebrochen`/asymptoten (38 Aufgaben), `funktionen.exponential_log`/graph |
| y = k · a^(x − b) + c aus dem Graphen | B | `funktionen.exponential_log`/modell (ohne b und c) → 3–4 Aufgaben |
| Logarithmusfunktion mit Parametern | A | `funktionen.exponential_log`/logfunktion: „Welche Gerade ist Asymptote des Graphen von f(x) = 2 · log₃(x + 5) − 1?“ |
| Definitions- und Wertemenge nach der Abbildung | B | `funktionen.quadratisch`/scheitel (Wertemenge), `funktionen.gebrochen`/definitionsmenge → in Karte `punkte` |

**Ergebnis 3a:** 31 geplante Lernkarten: 19 A, 7 B, 5 C. Statt 4 neuer Flüge (und des neuen Orts Accra): 5 neue Lernkarten in `abbildungen.aehnlichkeit` (2), `trigo.rechtwinklig` (1), `trigo.allgemein` (1), `abbildungen.matrizen` (1) und etwa 15–20 Aufgaben. Die RS-Gruppe-I-Karten sind für Gymnasiasten Vertiefung.

### 3b – Stoff, den RS (alle Zweige) oder IB bis Jahr 4 verlangt und der in keinem Flug steht

Abgleich mit `vorschlag-rsib.md` Teil 2 und „Was aus dem Framework fehlt“, je Punkt neu per Textsuche geprüft (Stand `lernen-app` 04f0fec). Gruppe-I-Stoff und IB Extended stehen am Ende, weil sie die Frage nicht betreffen.

| Stoff | verlangt von | heute da? (Tatsache) | Vorschlag |
|---|---|---|---|
| **Dualsystem / andere Zahlensysteme** | RS alle Zweige M5 1.2; IB (MYP 4–5) | fehlt (Suche „Dual“, „Zweiersystem“, „binär“: 0) | neue Lernkarte in `zahlen.natuerlich` (5) nach `roemisch_system`; Pflicht |
| **Zeit: Zeitzonen, 24-Stunden-Uhr, Fahrpläne** | IB MYP 1–3 | `groessen.einheiten`/zeit („Mit Zeit rechnen“) da; Zeitzonen fehlen (Suche „Zeitzone“, „Ortszeit“: 0) | 3–4 Aufgaben in `groessen.einheiten`/zeit (IB, Vertiefung) |
| **Stängel-Blatt-Diagramm, gruppierte Daten, Summenkurve, Perzentile** | IB MYP 1–3 bzw. Standard | Quartilsabstand da (`daten.boxplot`/quartile); der Rest fehlt (Suche: 0) | 2 Lernkarten: „Stängel-Blatt“ in `daten.darstellen` (5), „Gruppierte Daten und Summenkurve“ in `daten.boxplot` (7); IB, Vertiefung |
| **Peilungen / Kurswinkel** | IB Standard (H4 Kap. 23G) | nur eine Aufgabe mit „Nordrichtung“ in `trigo.allgemein`/kosinussatz_seite | 3–4 Aufgaben in `trigo.allgemein`/anwendung |
| **Algorithmen, Flussdiagramme** | IB (laut `vorschlag-rsib.md`, Stufe unklar) | fehlt (Suche: 0) | **für Sebastian:** keine sinnvolle Gym-Heimat; weglassen oder später eigenes kleines Thema |
| Kegel, Kugel, Zylinder nach Ecken/Kanten/Flächen beschreiben | RS alle Zweige M5 LB3 | nicht geprüft (Textsuche nach „Kugel“ liefert nur Eiskugeln/Urnen) | offen |
| Ortsbereiche, Tangente von einem Außenpunkt | RS M7 LB5 (I) / LB3 (II) | **da**: `geometrie.ortslinien`/parallelen („Streifen aller Punkte, die … höchstens 2,5 cm entfernt sind“), `geometrie.kreis`/tangente und beweis | – |
| Vierecke, Drehung | RS M8 LB1, LB2 | **da** (Teil 3a) | – |
| Daten und Zufall Kl. 8 | RS M8 LB7 (I) / LB6 (II) | **da**: `stochastik.grundbegriffe`/begriffe, rel_haeufigkeit (Plan 8) | – |
| Faktorisieren x² + bx + c | IB Standard | **da**: `gleichungen.quadratisch`/faktorisieren | – |
| Prinzip von Cavalieri | RS M9 LB5 (I) | teilweise: im Merksatz von `raum.pyramide_kegel_kugel`/verstehen | – |
| *nur Gruppe I:* Symmetrieebenen von Körpern (M8 LB3), Winkel Gerade–Ebene / wahre Größe (M7 LB4), Trägergraph (M9 LB7, M10), Logarithmensätze für Produkt und Quotient (M10 LB4) | RS Gruppe I | fehlen (Suche: 0; bei Logarithmen nur die Potenzregel in `gleichungen.exponential`/potenzregel) | je 1 Lernkarte oder Aufgaben in `raum.schraegbilder`, `funktionen.quadratisch`, `gleichungen.exponential` – nur falls Gruppe I abgedeckt wird (Entscheidung 4) |
| *nur IB Extended:* Kreissätze, drei Mengen, Logarithmen anderer Basen, Korrelationskoeffizient | IB Extended | fehlen | nicht Teil der Frage (Extended); bei Entscheidung 5 mitentscheiden |

**Ergebnis 3b:** Für RS alle Zweige fehlt nur das **Dualsystem** sicher (dazu ungeprüft: Körper beschreiben, Kl. 5). Für IB bis Jahr 4 fehlen kleine Stücke Statistik, Zeitzonen, Peilungen und Algorithmen. Nichts davon braucht einen eigenen Flug (Meinung; Ausnahme vielleicht Algorithmen).

---

## Teil 4 – Für Sebastian zu entscheiden

1. **Grundsatz:** 11 Themen auflösen, 13 behalten, keine neuen Themen (statt 4) – Stoff als Lernkarten/Aufgaben in bestehende Flüge (Liste unten). Zusätzliche Flüge: Kind A 13 statt 28, Kind B 13 statt 28 (5 davon in abgeschlossenen Klassen statt 9).
2. **`terme.quadratische_extreme` (Sonderfall).** Inhaltlich vollständig in `funktionen.quadratisch` – aber dort erst Plan-Klasse 9; die Realschule verlangt es in Kl. 8 (alle Zweige).
   - (a) auflösen: einfacher, aber RS-Mindeststand Kl. 8 gebrochen (der Stoff kommt ein Jahr später).
   - (b) Flug bleibt in Kl. 8 (Shanghai); in `funktionen.quadratisch` werden `umformen`/`extremwert` zur Wiederholung bzw. kürzer. Kein zusätzlicher Stoff, nur früher.
   - **Meinung: (b)**, weil sonst die Regel „Mindeststand von Gym **und** RS“ an dieser Stelle nicht gilt. Dann +1 Flug in Kl. 8 für beide Kinder.
3. **Pflicht je Schulart.** Die App kennt Pflicht/Vertiefung nur je Thema, nicht je Schulart (`inhalt.bewertung`). Beim Auflösen landet RS-Pflichtstoff auf Gym-Vertiefungskarten: `abbildungen.kongruenz`/verschiebung und drehung (RS M7 LB2, M8 LB2), dazu alle neuen Gruppe-I-Karten. Entweder Pflicht für alle (Gym-Kind lernt mehr) oder eine Pflicht-Kennung je Schulart (App-Frage, kein Inhalt).
4. **Mathematischer RS-Zweig (Gruppe I) abdecken?** Betrifft die Flüge `gleichungen.wurzel`, `abbildungen.matrizen` und 8 Lernkarten (Teil 2: `transformation`/punkte, `umkehr`/umkehrbar und linear; Teil 3a: 5 Karten), dazu die Gruppe-I-Zeile aus 3b. Wenn nein: beide Flüge werden Zusatz.
5. **IB Extended und Stoff ohne Pflicht** – 8 der 13 bleibenden Flüge (`graphentheorie`, `schranken`, `optimierung`, `standardabweichung`, `betrag`; `logik`, `reihen`, `normalverteilung`): Pflicht, freiwillig oder weglassen? Meinung: freiwillig; für Kind B auf keinen Fall als Rückstand zählen.
6. **Dualsystem** (RS alle Zweige, Kl. 5) als Lernkarte in `zahlen.natuerlich` ergänzen? Und die kleinen IB-Lücken aus 3b?
7. **Orte** (Folge, falls 1 angenommen): leer werden Shanghai (bei 2a), San Francisco, Boston. Palmer-Station behält nur `funktionen.reihen` (dann Klasse 10, Titel „Folgen und Reihen“) – einfacher als der Umzug nach Halley aus `vorschlag-mindeststand.md`. Galápagos behält nur `sonder.graphentheorie` (Kl. 6). Lagos behält nur `abbildungen.determinanten2` (Kl. 7). Accra wird nicht gebraucht.

**Einbau-Liste bei „ja“ zu 1** (Arbeit für einen Inhalte-Chat):
- Neue Lernkarten in Gym-Flügen: `funktionen.linear` + `bueschel` (Vertiefung) · `funktionen.exponential_log` + `punkte` (aus `transformation`) · `funktionen.potenz` + `umkehrbar`, `linear` (aus `umkehr`) · `stochastik.verknuepft` + „Mengen und Venn-Diagramm“ (aus `mengen`/elemente, Vertiefung) · `stochastik.mehrstufig` + `unabhaengig` (aus `bedingt`, Vertiefung) · aus Teil 3a: `abbildungen.aehnlichkeit` + 2, `trigo.rechtwinklig` + 1, `trigo.allgemein` + 1; RS-Flug `abbildungen.matrizen` + 1.
- `funktionen.reihen` + `rekursiv`, `arithmetisch`, `geometrisch` (aus `folgen`) an den Anfang.
- Aufgaben in bestehende Karten (je 3–4): `abbildungen.kongruenz`/verschiebung · `funktionen.linear`/lage · `gleichungen.lgs2`/loesbarkeit · `funktionen.quadratisch`/parameter · `funktionen.potenz`/wurzelfunktion (2×) · `bruch.brueche`/kuerzen und erweitern · `groessen.proportional`/sach · `stochastik.verknuepft`/bedingt · `bruch.prozent_grundwert`/mehrfach · aus Teil 3a: `geometrie.konstruktion`/konstruierbar, `abbildungen.aehnlichkeit`/strahlensatz2, `funktionen.trig`/zuordnen, `funktionen.exponential_log`/modell.
- Lernstände: Die 11 aufgelösten Themen sind laut `vorschlag-mindeststand.md` `entwurf` – vermutlich gibt es keine Lernstände (Datenbank hier **nicht** gelesen).

---

## Was nicht geprüft wurde

- Nicht jede Aufgabe: je Lernkarte Titel, Merksatz, zwei Stichproben je Seite und gezielte Textsuche. Ein „A“ kann im Einzelfall eine Aufgabenart übersehen, die nur der RS-/IB-Flug hat.
- Lehrplan-Stellen nicht neu abgerufen (übernommen aus `vorschlag-rsib.md`, Stand 17.11.). Ob der Gym-Lehrplan Umkehrfunktionen oder Abbildungen beliebiger Graphen verlangt (für Pflicht/Vertiefung der neuen Karten), habe ich nicht geprüft.
- Datenbank nicht gelesen (Status `entwurf`, Lernstände).
- Ob die umgezogenen Aufgaben die Stufen-Regeln (4/6/8 Übungen, Typen, Knobel) in der Zielkarte erfüllen, ist nicht geprüft – das wäre Teil des Einbaus.
- RS-Gruppe II/III nur so weit, wie `vorschlag-rsib.md` sie nennt.

## Quellen

- `inhalte/themenliste.json`, `inhalte/themen/*.json` (Zweig `lernen-app`, Commit 04f0fec; enthält die Ergebnisse von Teil A „Bereinigen“)
- `inhalte/pruefung/klassen/vorschlag-mindeststand.md` (Plan-Klassen, Orte, Kinder, Punkt 6 neue Themen)
- `inhalte/pruefung/klassen/vorschlag-rsib.md` (Lehrplan-Stellen RS: lehrplanplus.bayern.de/fachlehrplan/realschule/5–10/mathematik; IB: Mathematics guide 2020, Haese MYP 1–5)
- `inhalte/AUFTRAEGE.md`, Dreiundzwanzigste Runde
- Prüfskripte (Textsuche, Belegauswahl): nur lokal, nicht eingecheckt
