# LK-D 4 – Kür je Etappe und Schulart (22.11.2026, „Entscheidungen Sebastian 17:05“)

**Regel (Entscheidung 17:05, Punkt 1):** Eine Etappe ohne Lehrplanpunkt in der Schulart des Kindes ist dort **Kür**. Sie zählt nicht für Flug-Abschluss, Flug-Test und Stempel.
- Ein Teil ganz ohne Pflicht-Etappe ist der bisherige „Zusatz“-Teil.
- Pflicht-Etappe heißt: In dieser Schulart verlangt ein Lehrplanpunkt die Etappe als Hauptthema. Grundlage ist dieselbe Klasse je Etappe wie bei der Teilung.

**JSON (`lk_teilung_2211.json`):**
- In `teilungsliste`:
  - jede Etappe hat `kuer_in` (Schularten, in denen sie Kür ist) und `klasse_je_schulart`;
  - jeder Teil hat `pflicht_etappen_je_schulart`;
  - `stand_je_kind` ist neu gerechnet (nur Pflicht-Etappen der Schulart des Kindes, beide Kinder Gymnasium); der alte Stand steht in `stand_je_kind_vorher`.
- `etappen_kuer`: dieselbe Angabe für **alle** 87 Themen (617 Etappen). Kür je Schulart: Gym 204, RS I 275, RS II/III 322, IB Std 416, IB Ext 408.
- `stand_je_kind_ungeteilt`: Stand der Kinder in ungeteilten Themen nach der Kür-Regel.

### Pflicht-Etappen je Teil und Schulart, Stand je Kind

Spalten Gym bis IB Ext: Pflicht-Etappen / alle Etappen des Teils.

| Teil | Gym | RS I | RS II/III | IB Std | IB Ext | Kür-Etappen (Schulart) | Stand jetzt (nur Pflicht, Gym) | Stand vorher (alle Etappen) |
|---|---|---|---|---|---|---|---|---|
| 26 Teil 1/2 | 3/5 | 2/5 | 2/5 | 4/5 | 4/5 | `geschickt`: Gym, RS I, RS II/III, IB Std, IB Ext; `sach`: RS I, RS II/III; `aenderung`: Gym, RS I, RS II/III | K1: 0/3 · K2: 0/3 | K1: 0/5 · K2: 0/5 |
| 26 Teil 2/2 | 1/3 | 3/3 | 3/3 | 3/3 | 3/3 | `vervielfachen`: Gym; `pruefen`: Gym | K1: 0/1 · K2: 0/1 | K1: 0/3 · K2: 0/3 |
| 29 Teil 1/2 | 5/5 | 5/5 | 5/5 | 3/5 | 3/5 | `minusklammer`: IB Std, IB Ext; `aequivalenz`: IB Std, IB Ext | K1: 0/5 · K2: 5/5 **vollständig** | K1: 0/5 · K2: 5/5 |
| 29 Teil 2/2 | 3/4 | 4/4 | 4/4 | 3/4 | 3/4 | `gleichungen_binomisch`: Gym, IB Std, IB Ext | K1: 0/3 · K2: 3/3 **vollständig** | K1: 0/4 · K2: 3/4 |
| 44 Teil 1/2 | 5/5 | 4/5 | 3/5 | 3/5 | 3/5 | `gleichschenklig`: RS I, RS II/III, IB Std, IB Ext; `planfigur`: IB Std, IB Ext; `satz_kehrsatz`: RS II/III | K1: 0/5 · K2: 0/5 | K1: 0/5 · K2: 0/5 |
| 44 Teil 2/2 | 0/2 (Zusatz) | 2/2 | 2/2 | 0/2 (Zusatz) | 0/2 (Zusatz) | `vierecke`: Gym, IB Std, IB Ext; `vierecke_konstruieren`: Gym, IB Std, IB Ext | K1: 0/0 · K2: 0/0 | K1: 0/2 · K2: 0/2 |
| 46 Teil 1/3 | 5/6 | 6/6 | 6/6 | 2/6 | 2/6 | `mittelsenkrechte`: IB Std, IB Ext; `winkelhalbierende`: IB Std, IB Ext; `symmetrie`: IB Std, IB Ext; `vierecke_ordnen`: IB Std, IB Ext; `eigenschaften`: Gym | K1: 0/5 · K2: 0/5 | K1: 0/6 · K2: 0/6 |
| 46 Teil 2/3 | 0/3 (Zusatz) | 3/3 | 3/3 | 1/3 | 1/3 | `verschiebung`: Gym; `gegenvektor`: Gym, IB Std, IB Ext; `vektor_koordinaten`: Gym, IB Std, IB Ext | K1: 0/0 · K2: 0/0 | K1: 0/3 · K2: 0/3 |
| 46 Teil 3/3 | 1/3 | 3/3 | 0/3 (Zusatz) | 2/3 | 2/3 | `punktspiegelung`: RS II/III; `drehung`: Gym, RS II/III; `vektor_drehen`: Gym, RS II/III, IB Std, IB Ext | K1: 0/1 · K2: 0/1 | K1: 0/3 · K2: 0/3 |
| 61 Teil 1/2 | 3/3 | 3/3 | 3/3 | 2/3 | 2/3 | `darstellen`: IB Std, IB Ext | K1: 0/3 · K2: 0/3 | K1: 0/3 · K2: 0/3 |
| 61 Teil 2/2 | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 | – | K1: 0/4 · K2: 0/4 | K1: 0/4 · K2: 0/4 |
| 91 Teil 1/2 | 1/4 | 4/4 | 2/4 | 0/4 (Zusatz) | 0/4 (Zusatz) | `pyramide`: IB Std, IB Ext; `lage`: Gym, RS II/III, IB Std, IB Ext; `wahre_groesse`: Gym, IB Std, IB Ext; `raumwinkel`: Gym, RS II/III, IB Std, IB Ext | K1: 0/1 · K2: 0/1 | K1: 0/4 · K2: 0/4 |
| 91 Teil 2/2 | 1/4 | 4/4 | 2/4 | 0/4 (Zusatz) | 0/4 (Zusatz) | `koordinaten`: Gym, RS II/III, IB Std, IB Ext; `rotation`: IB Std, IB Ext; `axialschnitt`: Gym, IB Std, IB Ext; `koerper_symmetrie`: Gym, RS II/III, IB Std, IB Ext | K1: 0/1 · K2: 0/1 | K1: 0/4 · K2: 0/4 |
| 101 Teil 1/2 | 7/7 | 0/7 (Zusatz) | 0/7 (Zusatz) | 0/7 (Zusatz) | 0/7 (Zusatz) | `prisma_volumen`: RS I, RS II/III, IB Std, IB Ext; `prisma_oberflaeche`: RS I, RS II/III, IB Std, IB Ext; `prisma_umstellen`: RS I, RS II/III, IB Std, IB Ext; `zylinder_volumen`: RS I, RS II/III, IB Std, IB Ext; `zylinder_oberflaeche`: RS I, RS II/III, IB Std, IB Ext; `sach`: RS I, RS II/III, IB Std, IB Ext; `verstehen`: RS I, RS II/III, IB Std, IB Ext | K1: 0/7 · K2: 0/7 | K1: 0/7 · K2: 0/7 |
| 101 Teil 2/2 | 1/1 | 1/1 | 1/1 | 0/1 (Zusatz) | 0/1 (Zusatz) | `cavalieri`: IB Std, IB Ext | K1: 0/1 · K2: 0/1 | K1: 0/1 · K2: 0/1 |

- **Kind 2, 29 Teil 2:** Im Gymnasium sind es 3/3, also **vollständig**. `gleichungen_binomisch` ist dort Kür (nur RS 8). Stempel und 100 Sterne also nachträglich, wie entschieden.
- **Folge für das Gymnasium – viele kurze Pflicht-Flüge:**
  - Mit einer einzigen Pflicht-Etappe: 26 Teil 2 (`erkennen`), 46 Teil 3 (`punktspiegelung`), 91 Teil 1 (`pyramide`), 91 Teil 2 (`rotation`), 101 Teil 2 (`cavalieri`).
  - 44 Teil 2 und 46 Teil 2 sind im Gymnasium ganz Kür (Zusatz).
  - Annahme: Der Flug-Test zieht dann nur aus diesen Etappen. TL-S muss klären, ob ein Test aus einer Etappe reicht.
- **Etappen ohne Lehrplanpunkt in irgendeiner Schulart** sind jetzt überall Kür, z. B. 26 `geschickt` und `aenderung` (außer IB). Das ist die Regel, aber Sebastian soll es sehen.

### Ungeteilte Themen: wo sich der Stand durch die Kür-Regel verschiebt

Die Tabelle enthält nur Fälle, in denen die Kür-Regel etwas ändert oder Stand und Flug nicht zusammenpassen.

| Kind | Thema | Pflicht erledigt | vorher alle Etappen? | Flug geschafft? |
|---|---|---|---|---|
| 1 | 15 Natürliche Zahlen | 12/12 | nein | ja |
| 2 | 24 Prozent- und Zinsrechnung | 6/6 | ja | nein |
| 2 | 30 Potenzen und negative Exponenten | 2/2 | ja | nein |
| 2 | 57 Daten erfassen und darstellen | 6/6 | ja | nein |
| 2 | 99 Flächen von Parallelogramm, Dreieck und Trapez | 7/7 | nein | nein |
| 2 | 100 Volumen | 7/7 | ja | nein |

- **Durch die Kür-Regel neu vollständig:** Kind 2 in 99 (die fehlende Etappe `drachen_raute` ist nur RS). Kind 1 in 15 war schon geflogen und ist jetzt auch rechnerisch vollständig (`dualsystem` ist im Gymnasium Kür).
- **Kind 2 in 24, 30, 57 und 100:** Alle Etappen sind erledigt, aber der Flug ist nicht abgeschlossen. Annahme: Es fehlt der Flug-Test. Das ändert die Kür-Regel nicht; ich nenne es nur.

### Widerspruch zum Inhalt: „Vertiefung“ in der Themendatei, aber mit Lehrplanpunkt

- Heute gibt es Kür nur für alle Schularten gemeinsam (`bewertung.lernziele_vertiefung` in der Themendatei). **47 Etappen** stehen dort als Vertiefung, haben aber in mindestens einer Schulart einen Lehrplanpunkt.
- Nach der neuen Regel wären sie dort Pflicht. Im Gymnasium betrifft das: 7 `pruefen`, 7 `stufenform`, 7 `eliminieren`, 26 `erkennen`, 33 `wirkung`, 35 `spiegeln`, 61 `darstellen`, 62 `unabhaengig`, 63 `elemente`, 63 `schnitt`, 63 `venn`, 63 `mengen_verstehen`, 98 `aussenwinkel`, 101 `cavalieri`, 102 `geteilt_gleiche_basis`, 102 `anwenden`.
- Dazu gehören meine neuen LK-Etappen (z. B. 61 `darstellen`, 101 `cavalieri`). Ich hatte sie als Vertiefung angelegt, damit bestehende Flüge unverändert bleiben.
- **Offen, Sebastian/TL-S:** Welche Angabe gilt?
  - Mein Vorschlag: Die Schulart-Regel gilt (Lehrplan), und `lernziele_vertiefung` gilt nur noch für Etappen ohne Lehrplanpunkt.
  - Die Liste steht in `vertiefung_aber_lehrplanpunkt`.
  - Der Stand je Kind oben ist schon nach der Schulart-Regel gerechnet.

### (a) F1 und (c) F3 – schon geliefert (Commit c7a86ada, vor der Entscheidung von 17:05)

- **(a) F1:**
  - Alle Themen habe ich systematisch gegen `lk_daten_2211.json` durchgezählt: 62 Fälle in `mehrere_klassen`, jeder mit Entscheidung und Begründung (Abschnitt „Ergänzung 939/940“ unten).
  - **57:** Wiederholung ohne neue Etappe, Anzeige „wird in Kl. 7 wieder aufgegriffen“.
  - **2:** In RS hat 2 nur noch Hauptpunkte in Kl. 7. Der Kl.-8-Punkt 734/749 hängt seit LK-D 2 an 29 Teil 2; nicht teilen, Anzeige „wird in Kl. 8 in 29 Teil 2 wieder aufgegriffen“.
- **(c) F3:** Neue Etappe 61 `darstellen` „Baumdiagramm und Vierfeldertafel“ in 61 Teil 1 (Punkte 950, 968, Gym 185).
- **Für `reise-aufbau`:** Neben den drei genannten neuen Etappen gibt es zwei weitere: **61 `darstellen`** (Teil 1) und **91 `raumwinkel`** (Teil 1).

---


# LK-D 3 – Teilungsliste nach der neuen Regel (22.11.2026; mit Ergänzung „Rückläufer ChatGPT 939/940“, 16:40)

## LK-D 3, Ergänzung 939/940 – Ergebnis vorab

**(1) Zählung berichtigt.**
- Die 6 Themen der Entscheidung von 16:20 ergeben **13 Teile und 7 neue Flüge** (26: 2 · 29: 2 · 44: 2 · 46: 3 · 61: 2 · 91: 2). Die Angabe „15 Teile, 9 Flüge“ war mein Zählfehler.
- Mit 101 aus dem Gym-Audit: **7 Themen, 15 Teile, 8 neue Flüge.** Daran ändert diese Ergänzung nichts.

**(2) Muss F1 – alle Themen mit Hauptpunkten in mehreren Klassen.**
- Gezählt habe ich maschinell gegen `lk_daten_2211.json`: je Thema und Spur jede Klasse mit Hauptpunkt; als „neu“ zählt eine Etappe, die in keiner früheren Klasse dieser Spur verlangt war.
- Ergebnis: **62 Fälle** (Thema × Spur × spätere Klasse). In der JSON steht jeder Fall unter `mehrere_klassen`, mit Entscheidung, Anzeige und Begründung.
- Die Anzeigen für „Wiederholung ohne neue Etappe“ stehen zusätzlich in `wiederholung_anzeige`.
- **Gymnasium:** nur 101 (8 → 10), bereits geteilt.
- **RS I:** 26, 29, 44, 46 (zweimal), 61 und 91 sind geteilt, 57 ist Wiederholung.
- **Thema 2 hat in RS I nur noch Hauptpunkte in Kl. 7.** ChatGPT hat vermutlich den Stand vor LK-D 2 gelesen (Feld `vorher` von 734/749). Begründung siehe unten.
- **101:** geteilt, siehe Gym-Audit.

| Thema | Spur | Klassen | Punkte (spätere Klasse) | neue Etappen dort | Entscheidung | Anzeige | Begründung |
|---|---|---|---|---|---|---|---|
| 8 Quadratische Gleichungen (allgemein) | RS II/III | 9 → 10 | 859, 860 | `ausklammern`, `diskriminante`, `ergaenzung`, `faktorisieren`, `loesungsformel` | **grenzfall** | wird in Kl. 10 weitergeführt | rs_II_III löst keine Teilung aus (Regel 15:30/15:35); neue Etappen dort nur als Anzeige „weitergeführt“. |
| 26 Direkte Proportionalität und Dreisatz | RS I | 5 → 6 | 385, 386, 387, 388 | `erkennen`, `pruefen`, `vervielfachen` | **geteilt** | eigener Teil 2 von 2 in Kl. 6 | Die spätere Klasse verlangt eigene Etappen; Gym/RS I sind Maßstab der Teilung. |
| 26 Direkte Proportionalität und Dreisatz | RS II/III | 5 → 6 | 385, 386, 387, 388 | `erkennen`, `pruefen`, `vervielfachen` | **grenzfall** | wird in Kl. 6 weitergeführt | rs_II_III löst keine Teilung aus (Regel 15:30/15:35); neue Etappen dort nur als Anzeige „weitergeführt“. |
| 29 Terme umformen | RS I | 7 → 8 | 732, 734 | `ausklammern`, `binomisch`, `gleichungen_binomisch`, `summe_mal_summe` | **geteilt** | eigener Teil 2 von 2 in Kl. 8 | Die spätere Klasse verlangt eigene Etappen; Gym/RS I sind Maßstab der Teilung. |
| 29 Terme umformen | RS II/III | 7 → 8 | 747, 749 | `ausklammern`, `binomisch`, `gleichungen_binomisch`, `summe_mal_summe` | **grenzfall** | wird in Kl. 8 weitergeführt | rs_II_III löst keine Teilung aus (Regel 15:30/15:35); neue Etappen dort nur als Anzeige „weitergeführt“. |
| 33 Lineare Funktionen | RS II/III | 8 → 9 | 988, 989, 990, 991 | `ablesen`, `aufstellen`, `bueschel`, `deuten`, `wirkung`, `zwei_punkte` | **grenzfall** | wird in Kl. 9 weitergeführt | rs_II_III löst keine Teilung aus (Regel 15:30/15:35); neue Etappen dort nur als Anzeige „weitergeführt“. |
| 44 Konstruktionen, Kongruenz und Beweise | RS I | 7 → 8 | 931 | `vierecke`, `vierecke_konstruieren` | **geteilt** | eigener Teil 2 von 2 in Kl. 8 | Die spätere Klasse verlangt eigene Etappen; Gym/RS I sind Maßstab der Teilung. |
| 46 Kongruenzabbildungen | RS I | 6 → 7 | 868, 869, 870, 871 | `gegenvektor`, `vektor_koordinaten`, `verschiebung` | **geteilt** | eigener Teil 2 von 3 in Kl. 7 | Die spätere Klasse verlangt eigene Etappen; Gym/RS I sind Maßstab der Teilung. |
| 46 Kongruenzabbildungen | RS I | 6 → 8 | 930, 933, 934, 935, 936, 937 | `drehung`, `punktspiegelung`, `vektor_drehen` | **geteilt** | eigener Teil 3 von 3 in Kl. 8 | Die spätere Klasse verlangt eigene Etappen; Gym/RS I sind Maßstab der Teilung. |
| 46 Kongruenzabbildungen | RS II/III | 6 → 7 | 906, 907, 908, 909 | `gegenvektor`, `vektor_koordinaten`, `verschiebung` | **grenzfall** | wird in Kl. 7 weitergeführt | Kl. 8 (Vierecke nach Eigenschaften unterscheiden) steckt in vierecke_ordnen aus Kl. 6; RS II/III löst ohnehin keine Teilung aus. |
| 46 Kongruenzabbildungen | RS II/III | 6 → 8 | 956 | – | **wiederholung** | wird in Kl. 8 wieder aufgegriffen | Kl. 8 (Vierecke nach Eigenschaften unterscheiden) steckt in vierecke_ordnen aus Kl. 6; RS II/III löst ohnehin keine Teilung aus. |
| 57 Daten erfassen und darstellen | RS I | 5 → 7 | 900 | – | **wiederholung** | wird in Kl. 7 wieder aufgegriffen | Kl. 7 (8 I 8/K4) verlangt dieselbe Fähigkeit wie Kl. 5 (6/k3, verzerrte Diagramme erkennen/berichtigen) auf höherem Niveau; die Etappe irrefuehrend deckt beides. Keine neue Etappe → kein eigener Flug. |
| 57 Daten erfassen und darstellen | RS II/III | 5 → 7 | 928 | – | **wiederholung** | wird in Kl. 7 wieder aufgegriffen | wie RS I: Kl. 7 (6/K4) = Kl. 5 (6/k3) auf höherem Niveau; Etappe irrefuehrend. |
| 61 Zufall und Laplace | RS I | 8 → 9 | 798, 799, 800, 801, 802 | `gegenereignis`, `grosse_zahlen`, `laplace`, `laplace_pruefen` | **geteilt** | eigener Teil 2 von 2 in Kl. 9 | Die spätere Klasse verlangt eigene Etappen; Gym/RS I sind Maßstab der Teilung. |
| 61 Zufall und Laplace | RS II/III | 8 → 9 | 993, 994, 995, 996, 997 | `gegenereignis`, `grosse_zahlen`, `laplace`, `laplace_pruefen` | **grenzfall** | wird in Kl. 9 weitergeführt | rs_II_III löst keine Teilung aus (Regel 15:30/15:35); neue Etappen dort nur als Anzeige „weitergeführt“. |
| 91 Schrägbilder und Raumdarstellung | RS I | 7 → 8 | 939, 940, 941 | `axialschnitt`, `koerper_symmetrie`, `koordinaten`, `rotation` | **geteilt** | eigener Teil 2 von 2 in Kl. 8 | Die spätere Klasse verlangt eigene Etappen; Gym/RS I sind Maßstab der Teilung. |
| 91 Schrägbilder und Raumdarstellung | RS II/III | 8 → 10 | 1006 | `axialschnitt`, `rotation` | **grenzfall** | wird in Kl. 10 weitergeführt | rs_II_III löst keine Teilung aus (Regel 15:30/15:35); neue Etappen dort nur als Anzeige „weitergeführt“. |
| 101 Prismen und Zylinder | Gym | 8 → 10 | 285 | `cavalieri` | **geteilt** | eigener Teil 2 von 2 in Kl. 10 | Die spätere Klasse verlangt eigene Etappen; Gym/RS I sind Maßstab der Teilung. |
| 2 Lineare Gleichungen | RS I, RS II/III | vorher 7 → 8, jetzt nur 7 | 734, 749 | – | **nicht teilen** | wird in Kl. 8 in „29 Terme umformen – Teil 2 von 2“ wieder aufgegriffen | Der Kl.-8-Punkt verlangt Gleichungen mit Summenprodukten und binomischen Ausdrücken. Das braucht binomische Formeln aus 29 Teil 2; die eigene Etappe gleichungen_binomisch steht deshalb seit LK-D 2 in 29 Teil 2 (Hauptthema 29, 2 bleibt Nebenthema). 2 hat damit nur noch Hauptpunkte in Kl. 7 – kein zweiter Teil, kein zusätzlicher Flug. |

- **IB (nur Orientierung, löst keine Teilung aus):** 32 Grenzfälle mit neuen Etappen in der späteren Klasse (Anzeige „wird in Kl. x weitergeführt“) und 12 Wiederholungen ohne neue Etappe (Anzeige „wird in Kl. x wieder aufgegriffen“).
  - Die Wiederholungen betreffen: 6 Gleichungssysteme mit 2 Unbekannten (Kl. 4); 33 Lineare Funktionen (Kl. 4); 44 Konstruktionen, Kongruenz und Beweise (Kl. 4); 46 Kongruenzabbildungen (Kl. 4); 53 Volumen und Oberfläche (Kl. 2); 57 Daten erfassen und darstellen (Kl. 2); 59 Zweidimensionale Daten (Kl. 4); 92 Pyramide, Kegel, Kugel (Kl. 4).
- **Offen bei 57:** Die Etappe `irrefuehrend` übt das Erkennen verzerrter Diagramme. „Berichtigen/verbessern“ (RS 5 und RS 7) kommt in ihren Aufgaben kaum vor.
  - Das ist keine neue Etappe, sondern eine Lücke in den Aufgaben. Vorschlag: einige Aufgaben „richtige Darstellung wählen“ ergänzen. Nicht geliefert.

**(3) Muss F2 – Zusatz-Regel je Schulart in den JSON-Kanten.**
- Jede der 137 Kanten in `kanten` hat jetzt `art_je_schulart` mit „hart“, „empfohlen“ oder „Zusatz“ (null = Kante gilt in dieser Schulart nicht).
- Regeln:
  - Ist der Teil, der etwas braucht, in der Schulart Zusatz, steht dort „Zusatz“: keine Pflicht, sperrt nichts. Das betrifft 9 Kanten.
  - Ist die Voraussetzung Zusatz, steht dort „empfohlen“.
  - Sonst gilt die bisherige Art.
- Jeder Teil hat `status_je_schulart` (Pflicht/Zusatz).
- Gymnasium wie verlangt:
  - **46 Teil 3 ← Teil 1 hart**, ← Teil 2 nur empfohlen;
  - **44 Teil 2 Zusatz** (← Teil 1: „Zusatz“);
  - ebenso 46 Teil 2.
- `kanten_je_schulart` führt die Zusatz-Teile jetzt ausdrücklich mit art „Zusatz“:

| Schulart | Teil | braucht | Art | Grund |
|---|---|---|---|---|
| gym | 46 Kongruenzabbildungen – Teil 3 von 3 | 46 Kongruenzabbildungen – Teil 2 von 3 | **empfohlen** | Vorgänger ist in dieser Schulart Zusatz |
| gym | 46 Kongruenzabbildungen – Teil 3 von 3 | 46 Kongruenzabbildungen – Teil 1 von 3 | **hart** | letzter Pflicht-Teil davor |
| rs_I | 101 Prismen und Zylinder – Teil 2 von 2 | 101 Prismen und Zylinder – Teil 1 von 2 | **empfohlen** | Vorgänger ist in dieser Schulart Zusatz |
| rs_II_III | 101 Prismen und Zylinder – Teil 2 von 2 | 101 Prismen und Zylinder – Teil 1 von 2 | **empfohlen** | Vorgänger ist in dieser Schulart Zusatz |
| gym | 44 Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 | 44 Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 | **Zusatz** | Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts |
| ib_standard | 44 Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 | 44 Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 | **Zusatz** | Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts |
| ib_extended | 44 Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 | 44 Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 | **Zusatz** | Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts |
| gym | 46 Kongruenzabbildungen – Teil 2 von 3 | 46 Kongruenzabbildungen – Teil 1 von 3 | **Zusatz** | Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts |
| rs_II_III | 46 Kongruenzabbildungen – Teil 3 von 3 | 46 Kongruenzabbildungen – Teil 2 von 3 | **Zusatz** | Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts |
| ib_standard | 91 Schrägbilder und Raumdarstellung – Teil 2 von 2 | 91 Schrägbilder und Raumdarstellung – Teil 1 von 2 | **Zusatz** | Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts |
| ib_extended | 91 Schrägbilder und Raumdarstellung – Teil 2 von 2 | 91 Schrägbilder und Raumdarstellung – Teil 1 von 2 | **Zusatz** | Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts |
| ib_standard | 101 Prismen und Zylinder – Teil 2 von 2 | 101 Prismen und Zylinder – Teil 1 von 2 | **Zusatz** | Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts |
| ib_extended | 101 Prismen und Zylinder – Teil 2 von 2 | 101 Prismen und Zylinder – Teil 1 von 2 | **Zusatz** | Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts |

**(4) Sollte F3 – 61 Teil 1 und 91.**
- **61 Teil 1 – Baumdiagramm und Vierfeldertafel (RS 8 I 7/K1, Punkt 950; II/III 6/K1, Punkt 968): fehlten.**
  - Die Etappen `begriffe` und `rel_haeufigkeit` enthalten in keiner Aufgabe ein Baumdiagramm oder eine Vierfeldertafel. Die Nebenbezüge 60 und 63 liegen in RS I erst in Kl. 9 bzw. 10.
  - Geliefert: **neue Etappe 61 `darstellen` „Baumdiagramm und Vierfeldertafel“** (22 Aufgaben, Vertiefung), zugeordnet zu 950 und 968. Außerdem zu Gym 8 5/k5 (Punkt 185, Baumdiagramm).
  - **61 Teil 1 hat damit 3 Etappen** und ist kein Kurzflug mehr. Klassen bleiben gleich (Gym 8, RS I 8).
- **91 gegen die Anforderungen von Kl. 7 und 8 (RS I) geprüft:**
  - Kl. 7, Punkt 881 – Lage von Geraden/Ebenen und Raumwinkel:
    - Die Lage war gedeckt (`lage`), **Raumwinkel fehlte**.
    - Geliefert: **neue Etappe 91 `raumwinkel` „Winkel im Raum“** (22 Aufgaben). Sie kommt in 91 Teil 1 (RS I 7); dort stehen jetzt 4 Etappen.
  - Kl. 7, Punkt 882 – Schrägbilder mit Verzerrung und Achsenlage zeichnen:
    - `pyramide` übt nur Ecken, Kanten und Flächen; den Verzerrungsfaktor enthält `wahre_groesse`.
    - 882 bekommt deshalb zusätzlich `wahre_groesse`; ebenso II/III 959.
    - Das Zeichnen selbst geht in der App nicht und bleibt Papierarbeit.
  - Kl. 7, Punkt 883 – wahre Größe: gedeckt (`wahre_groesse`).
  - Kl. 8, Punkte 939, 940, 941 – Körpersymmetrie, Axialschnitt und Rotation, Koordinaten: gedeckt (`koerper_symmetrie`, `axialschnitt`, `rotation`, `koordinaten`).
- **Kinder:** Kein Kind hat in 61 oder 91 etwas erledigt, die neuen Etappen ändern also keinen Stand.
- **SQL:**
  - Nur die Begründungstexte von 185 haben sich geändert (Etappe `darstellen`).
  - Die Änderungszahlen bleiben 33/18/13/187.
  - Die RS-Punkte 950, 968, 881, 882 und 959 sind im SQL nicht enthalten, weil sich an ihrer Themenzuordnung nichts ändert. Ihre Etappen stehen in der JSON.
  - Probelauf auf dem vollständigen echten Stand: LP-RS zweimal, dann LK-D zweimal, bestanden; `thema_jahrgang` unverändert.

---


## Frühere Fassung (LK-D 2/3, Stand nach „Entscheidung Teilung“ 16:20)

## LK-D 3 – was sich gegenüber der Entscheidung von 16:20 ändert

- **Die Entscheidung von 16:20 nennt die alte, falsch gezählte Fassung:** „6 Themen → 15 Teile, 9 neue Flüge“.
  - Richtig waren für diese 6 Themen 13 Teile und 7 neue Flüge (26: 2 · 29: 2 · 44: 2 · 46: 3 · 61: 2 · 91: 2 = 13).
  - Die Aufteilung je Thema in der Entscheidung stimmt, nur die Summe nicht.
- **Gym-Audit (ChatGPT 937, Muss A1) liegt vor** (Abschnitt 1; geliefert mit Commit 83d61a2e). Es bringt **ein weiteres geteiltes Thema: 101 Prismen und Zylinder** (Teil 2 von 2 · schiefe Körper und Cavalieri, Gym 10 / RS I 9).
  - **Damit steht die Liste: 7 Themen, 15 Teile, 8 neue Flüge.**
  - Dazu je eine neue Etappe in den schon geteilten Themen 29 (Teil 2) und 91 (Teil 2); die Zahl der Teile ändert das nicht.
- **Kind 2, Thema 29 (betrifft Punkt 4 der Entscheidung):** Teil 2 hat durch die neue Etappe „Gleichungen mit Klammerprodukten“ jetzt 4 Etappen, Kind 2 hat 3. **Teil 2 ist nach dem Umhängen also nicht vollständig.**
  - Stempel und die 100 Flug-Sterne für Teil 2 kommen erst, wenn die neue Etappe gelandet ist.
  - Alternative: die neue Etappe in Teil 2 als Zusatz führen, dann ist Teil 2 für Kind 2 sofort vollständig. Sebastian entscheidet.
- **Zusatz-Regel umgesetzt:** je Teil und Schulart `zusatz` in der JSON; Kanten je Schulart in `kanten_je_schulart` (Abschnitt 3a).
- **IB-Zählung:** 2 harte Verstöße je Kurs (63 ← 61, 29 ← 102), nicht 3. LK-D-Bericht und Postfach sind berichtigt.
- **Kurzflüge:** 44 Teil 2 und 61 Teil 1 (je 2 Etappen), neu 101 Teil 2 (1 Etappe).

---

Grundlage: AUFTRAEGE `lernen-app`:
- „Teilungsregel NEU“ (15:30), „Berichtigung“ (15:35), „Ergänzung – Benennung und Aufbau“ (15:40);
- „Stand 15:50 – Rückläufer ChatGPT 936/937“ (Muss A1, IB Muss B1).

Daten aus LK-D (`lk_daten_2211.json`, Stand nach dem Live).
- Nichts eingespielt. Kinder nur als Nummern.
- JSON: `lk_teilung_2211.json` (Teile, Grenzfälle, alle Voraussetzungs-Kanten, Verstöße, Aufbau-Kette je Teil).

**Berichtigungen gegenüber der ersten Fassung von LK-D 2:**
- Die erste Fassung meldete „15 Teile, 9 neue Flüge“. Richtig waren **13 Teile, 7 neue Flüge** (6 Themen); ich hatte falsch gezählt.
- Mit dem Audit (Abschnitt 1) kommt 101 Prismen und Zylinder dazu. Stand jetzt: **7 Themen, 15 Teile, 8 neue Flüge.**
- **IB-Voraussetzungen (Muss B1):**
  - Der LK-D-Bericht nannte „3 harte Verstöße je Kurs“. **Das war falsch, es sind 2:** 63 ← 61 und 29 ← 102. Einen dritten gab es in keiner Fassung der Daten.
  - Bericht und Postfach sind berichtigt; die JSON war schon richtig.
  - Stand jetzt je IB-Kurs: 2 hart, 7 empfohlen.

## 1 Audit an den Übergängen 7→8, 8→9, 9→10 (Muss A1)

**Vorgehen:**
- Für Gymnasium und RS Gruppe I habe ich jeden Punkt ab Klasse 8 gesucht, der nur Etappen verlangt, die schon in einer früheren Klasse neu waren. Das sind Kandidaten für „der Lehrplan verlangt mehr, als unsere Etappen enthalten“.
- Danach habe ich die Punkte geprüft, deren Kurzfassung einen neuen Aspekt nennt (Beweis, Verallgemeinerung, schiefe Körper, Symmetrie).
- Kriterium: Deckt eine vorhandene Etappe den verlangten Inhalt ab?

| Übergang | Punkt | verlangt (eigene Worte) | bisher | Befund | geliefert |
|---|---|---|---|---|---|
| Gym 8→10 | Gym 10 5/k4 (285) | Volumen schiefer Prismen, Volumengleichheit (Cavalieri) | 101 `prisma_volumen` (gerade Körper, Gym 8) | **fehlte** | neue Etappe **101 `cavalieri`** „Schiefe Körper und Cavalieri“ → eigener Teil (101 Teil 2 von 2, Gym 10) |
| RS 8→9 | RS 9 I 5/K1 (781), II/III 10 2/K2 (1007) | Cavalieri bzw. Grenzwertidee für Volumen | 92 `verstehen` | **teilweise** | jetzt 101 `cavalieri` (92 bleibt Neben); RS-I-Klasse von 101 Teil 2 = 9 |
| RS 7→8 | RS 8 I 3/K1 (939) | Symmetrische Körper: Symmetrieebenen, -achsen, -zentren | 91 `pyramide` (Ecken, Kanten) | **fehlte** | neue Etappe **91 `koerper_symmetrie`** „Symmetrie von Körpern“ (91 Teil 2, RS 8) |
| RS 7→8 | RS 8 I 4/K3 (734), II/III 3/K3 (749) | lineare Gleichungen mit binomischen Ausdrücken auf beiden Seiten | 2 `klammern`, `beide_seiten` (RS 7) | **fehlte** | neue Etappe **29 `gleichungen_binomisch`** „Gleichungen mit Klammerprodukten“ (29 Teil 2, RS 8); 2 bleibt Neben |
| RS 7→8 | RS 8 I 1/K1 (930) | Vierecke nach Eigenschaften unterscheiden | 46 `vierecke_ordnen` (RS 6) | gedeckt | – (Wiederholung, Anzeige „weitergeführt“) |
| RS 8→9 | RS 9 I 8/K3 (800) | Ergebnisraum bilden | 61 `begriffe` (RS 8) | gedeckt | – |
| Gym 8→9 | Gym 9 1/k3 (202) | Irrationalität von √2 durch indirekten Beweis | 20 `zahlarten` | **teilweise** (Beweisgedanke fehlt) | nicht geliefert: Ein Beweis lässt sich in der App nur als Lückentext abbilden. Vorschlag: Begründen-Aufgabe in 20 ergänzen (offen) |
| Gym 9→10 | Gym 10 3/k3 (271) | große und negative Winkel auf 0 bis 2π zurückführen | 38 `periode` | gedeckt (Periodizität) | – |

**Neue Inhalte:**
- Je Etappe 12 Übungen (Stufe 1–3, alle Aufgabentypen), 1 Test, 3 Korrektur, 6 Sicherung, dazu ein Kann-Satz.
- Alle Lösungen sind berechnet, die Texte selbst formuliert.
- Sie stehen in `_lk_etappen_2211.py`, eingehängt in `messen.prisma_zylinder.py`, `terme_umformen.py` und `raum.schraegbilder.py`; diese Generatoren erzeugen die Dateien danach unverändert.
- Prüfskript: alle Inhalte OK. Die Karten sind wie in LK-D Vertiefung; Flug und Stempel bestehender Themen bleiben unverändert.

**Folgen:**
- Die Zuordnung in `lk_daten_2211.json` und `lk_korrektur_2211.sql` ist angepasst:
  - 285 bekommt die Etappe `cavalieri` (Thema unverändert);
  - 781: 92 → 101;
  - 734: 2 → 29;
  - 939 bekommt die Etappe `koerper_symmetrie`.
- **Das SQL hat sich damit geändert:** 33/18/13/187 statt 31/18/13/185 Änderungen.
- Probelauf auf dem vollständigen echten Stand erneut bestanden: LP-RS, dann LK-D zweimal. Klassen unverändert.
- **Der Probelauf des Haupt-Chats von 15:50 galt der alten Fassung.**

## 2 Verfahren der Teilung

- **Klasse einer Etappe je Schulart:** die erste Klasse, in der ein Lehrplanpunkt sie als Hauptthema verlangt.
- **Teilung:** Etappen mit gleichem Klassenpaar (Gym, RS I) bilden einen Teil, also die feinste gemeinsame Teilung, sortiert nach Klasse.
  - Hat eine Etappe nur in einer Schulart eine Klasse, kommt sie zum passenden Teil.
  - Hat sie in keiner eine Klasse, kommt sie zum Teil der Etappe davor (nur 26: 2 Etappen).
- **IB und RS II/III** lösen keine Teilung aus; wo ein Teil dort mehrere Klassen hat, steht er bei den Grenzfällen.

## 3 Teilungsliste: 7 Themen, 15 Teile

- Im Gymnasium liegen die Teile eines Themas in derselben Klasse und kommen dort als Teil 1, 2, 3 nacheinander. Ausnahme: 101, Teil 2 liegt im Gymnasium in Klasse 10.
- Keine Gym-Klasse ändert sich.


### 26 Direkte Proportionalität und Dreisatz

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/2 | Direkte Proportionalität und Dreisatz – Teil 1 von 2 · Dreisatz | Auf die Einheit schließen, Der Dreisatz, Geschickte Zwischenschritte °, Sachaufgaben mit Dreisatz, Änderungsraten berechnen ° | 5 | 5 | 5 | 2 / 2 | 0/5 (Pflicht Gym 0/3) | 0/5 (Pflicht Gym 0/3) |
| 2/2 | Direkte Proportionalität und Dreisatz – Teil 2 von 2 · proportionale Zuordnungen erkennen | Was heißt proportional?, Verdoppeln, verdreifachen, halbieren, Ist die Tabelle proportional? | 5 | 6 | 6 | 2 / 2 | 0/3 (Pflicht Gym 0/1) | 0/3 (Pflicht Gym 0/1) |

### 29 Terme umformen · Flug geschafft: Kind 2

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/2 | Terme umformen – Teil 1 von 2 · zusammenfassen und ausmultiplizieren | Gleichartige Glieder zusammenfassen, Produkte vereinfachen, Minus vor der Klammer, Ausmultiplizieren, Äquivalente Terme | 7 | 7 | 7 | 1/2 / 1/2 | 0/5 (Pflicht Gym 0/5) | 5/5 (Pflicht Gym 5/5) |
| 2/2 | Terme umformen – Teil 2 von 2 · Summe mal Summe, binomische Formeln, Gleichungen mit Klammern | Summe mal Summe, Gemeinsamen Faktor ausklammern, Binomische Formeln, Gleichungen mit Klammerprodukten | 7 | 8 | 8 | 4 / 4 | 0/4 (Pflicht Gym 0/3) | 3/4 (Pflicht Gym 3/3) |

### 44 Konstruktionen, Kongruenz und Beweise

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/2 | Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 · Dreiecke konstruieren, Kongruenz | Gleichschenklige Dreiecke, Welcher Kongruenzsatz passt?, Ist das Dreieck konstruierbar?, Planfigur und Konstruktionsbeschreibung, Satz und Kehrsatz | 7 | 7 | 8 | 2/3 / 2/3 | 0/5 (Pflicht Gym 0/5) | 0/5 (Pflicht Gym 0/5) |
| 2/2 | Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 · Vierecke **(dünn)** | Winkel in symmetrischen Vierecken, Vierecke konstruieren | 7 * | 8 | 8 | – / – | 0/2 (Pflicht Gym 0/0) | 0/2 (Pflicht Gym 0/0) |

### 46 Kongruenzabbildungen

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/3 | Kongruenzabbildungen – Teil 1 von 3 · Spiegeln und Symmetrie | An einer Achse spiegeln, Mittelsenkrechte und Lot, Die Winkelhalbierende, Symmetrische Figuren, Symmetrische Vierecke ordnen, Was bleibt bei Abbildungen gleich? | 7 | 6 | 6 | 3 / 3 | 0/6 (Pflicht Gym 0/5) | 0/6 (Pflicht Gym 0/5) |
| 2/3 | Kongruenzabbildungen – Teil 2 von 3 · Verschieben und Vektoren | Figuren verschieben, Gegenvektor und Rückweg, Vektoren in Koordinaten | 7 * | 7 | 7 | 3 / 3 | 0/3 (Pflicht Gym 0/0) | 0/3 (Pflicht Gym 0/0) |
| 3/3 | Kongruenzabbildungen – Teil 3 von 3 · Drehen und Punktspiegelung | An einem Punkt spiegeln, Um einen Punkt drehen, Vektoren um 90° und 180° drehen | 7 | 8 | – | 3 / 3 | 0/3 (Pflicht Gym 0/1) | 0/3 (Pflicht Gym 0/1) |

### 61 Zufall und Laplace

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/2 | Zufall und Laplace – Teil 1 von 2 · Ergebnis, Ereignis, relative Häufigkeit | Ergebnis, Ergebnisraum, Ereignis, Relative Häufigkeit, Baumdiagramm und Vierfeldertafel | 8 | 8 | 8 | 2 / 2 | 0/3 (Pflicht Gym 0/3) | 0/3 (Pflicht Gym 0/3) |
| 2/2 | Zufall und Laplace – Teil 2 von 2 · Laplace-Wahrscheinlichkeit | Laplace-Wahrscheinlichkeit, Ist es ein Laplace-Experiment?, Das Gegenereignis, Gesetz der großen Zahlen | 8 | 9 | 9 | 2 / 2 | 0/4 (Pflicht Gym 0/4) | 0/4 (Pflicht Gym 0/4) |

### 91 Schrägbilder und Raumdarstellung

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/2 | Schrägbilder und Raumdarstellung – Teil 1 von 2 · Schrägbilder und Lage im Raum | Pyramiden: Ecken, Kanten, Flächen, Parallel, schneidend oder windschief?, Wahre Größe im Schrägbild, Winkel im Raum | 10 | 7 | 8 | – / – | 0/4 (Pflicht Gym 0/1) | 0/4 (Pflicht Gym 0/1) |
| 2/2 | Schrägbilder und Raumdarstellung – Teil 2 von 2 · Raumkoordinaten, Körpersymmetrie, Rotationskörper | Punkte im Raum mit Koordinaten, Rotationskörper, Axialschnitte berechnen, Symmetrie von Körpern | 10 | 8 | 10 | – / – | 0/4 (Pflicht Gym 0/1) | 0/4 (Pflicht Gym 0/1) |

### 101 Prismen und Zylinder

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/2 | Prismen und Zylinder – Teil 1 von 2 · gerade Prismen und Zylinder | Volumen eines Prismas, Oberfläche eines Prismas, Fehlende Größen am Prisma, Zylinder: Volumen begründen, Zylinder: Oberfläche über das Netz, Prismen und Zylinder im Alltag, Begründen und beurteilen | 8 | 9 * | – | – / – | 0/7 (Pflicht Gym 0/7) | 0/7 (Pflicht Gym 0/7) |
| 2/2 | Prismen und Zylinder – Teil 2 von 2 · schiefe Körper und Cavalieri **(dünn)** | Schiefe Körper und Cavalieri | 10 | 9 | 10 | – / – | 0/1 (Pflicht Gym 0/1) | 0/1 (Pflicht Gym 0/1) |

Legende:
- `*`: Diese Schulart hat für den Teil keinen eigenen Lehrplanpunkt; die Klasse folgt aus der Reihenfolge.
- `°`: Etappe ohne Lehrplanpunkt in Gym und RS I.
- „–“: kein Lehrplanstoff in dieser Spur.
- Stand: erledigt/Etappen des Teils (gelandet, gesetzt oder nachgewiesen).

**Zu dünn (nur gemeldet, nichts ergänzt):**
- 44 Teil 2 (2 Etappen), 61 Teil 1 (2) und 101 Teil 2 (1, neu).
- Vorschlag: Kurzflug mit 1–2 Städten.

**Lernstand (Regel Punkt 6):**
- Nur Kind 2 hat Lernstand in einem geteilten Thema: 29 Terme umformen, Flug geschafft.
- Teil 1 ist vollständig (5/5).
- **Teil 2 hat durch die neue Etappe „Gleichungen mit Klammerprodukten“ jetzt 4 Etappen, Kind 2 hat 3/4.** Ohne die Audit-Ergänzung wäre Teil 2 vollständig (3/3).
- Nichts geht verloren: Der Flug-Abschluss von 29 bleibt. Teil 2 gilt erst nach der neuen Etappe als geschafft, Stempel dann nach der Regel.
- Vorschlag: die neue Etappe für Kind 2 als „nachholen“ einplanen. Sebastian entscheidet.

**Benennung:** „‹Titel› – Teil x von y“ mit Untertitel wie oben.

## 3a Zusatz je Teil und Schulart (Regel 16:20)

Ein Teil ohne Lehrplanpunkt in der Schulart ist dort Zusatz: keine Pflicht, sperrt nichts, und Voraussetzungen auf ihn sind nur „empfohlen“.

| Teil | Gym | RS I | RS II/III | IB Std | IB Ext |
|---|---|---|---|---|---|
| Direkte Proportionalität und Dreisatz – Teil 1 von 2 | Pflicht | Pflicht | Pflicht | Pflicht | Pflicht |
| Direkte Proportionalität und Dreisatz – Teil 2 von 2 | Pflicht | Pflicht | Pflicht | Pflicht | Pflicht |
| Terme umformen – Teil 1 von 2 | Pflicht | Pflicht | Pflicht | Pflicht | Pflicht |
| Terme umformen – Teil 2 von 2 | Pflicht | Pflicht | Pflicht | Pflicht | Pflicht |
| Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 | Pflicht | Pflicht | Pflicht | Pflicht | Pflicht |
| Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 | Zusatz | Pflicht | Pflicht | Zusatz | Zusatz |
| Kongruenzabbildungen – Teil 1 von 3 | Pflicht | Pflicht | Pflicht | Pflicht | Pflicht |
| Kongruenzabbildungen – Teil 2 von 3 | Zusatz | Pflicht | Pflicht | Pflicht | Pflicht |
| Kongruenzabbildungen – Teil 3 von 3 | Pflicht | Pflicht | Zusatz | Pflicht | Pflicht |
| Zufall und Laplace – Teil 1 von 2 | Pflicht | Pflicht | Pflicht | Pflicht | Pflicht |
| Zufall und Laplace – Teil 2 von 2 | Pflicht | Pflicht | Pflicht | Pflicht | Pflicht |
| Schrägbilder und Raumdarstellung – Teil 1 von 2 | Pflicht | Pflicht | Pflicht | Zusatz | Zusatz |
| Schrägbilder und Raumdarstellung – Teil 2 von 2 | Pflicht | Pflicht | Pflicht | Zusatz | Zusatz |
| Prismen und Zylinder – Teil 1 von 2 | Pflicht | Zusatz | Zusatz | Zusatz | Zusatz |
| Prismen und Zylinder – Teil 2 von 2 | Pflicht | Pflicht | Pflicht | Zusatz | Zusatz |

**Kanten, die sich durch die Zusatz-Regel ändern** (vollständig in `kanten_je_schulart`):
- Gym: 46 Kongruenzabbildungen – Teil 3 von 3 ← 46 Kongruenzabbildungen – Teil 2 von 3: **empfohlen** (Vorgänger ist in dieser Schulart Zusatz)
- Gym: 46 Kongruenzabbildungen – Teil 3 von 3 ← 46 Kongruenzabbildungen – Teil 1 von 3: **hart** (letzter Pflicht-Teil davor)
- RS I: 101 Prismen und Zylinder – Teil 2 von 2 ← 101 Prismen und Zylinder – Teil 1 von 2: **empfohlen** (Vorgänger ist in dieser Schulart Zusatz)
- RS II/III: 101 Prismen und Zylinder – Teil 2 von 2 ← 101 Prismen und Zylinder – Teil 1 von 2: **empfohlen** (Vorgänger ist in dieser Schulart Zusatz)
- Gym: 44 Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 ← 44 Konstruktionen, Kongruenz und Beweise – Teil 1 von 2: **Zusatz** (Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts)
- IB Std: 44 Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 ← 44 Konstruktionen, Kongruenz und Beweise – Teil 1 von 2: **Zusatz** (Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts)
- IB Ext: 44 Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 ← 44 Konstruktionen, Kongruenz und Beweise – Teil 1 von 2: **Zusatz** (Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts)
- Gym: 46 Kongruenzabbildungen – Teil 2 von 3 ← 46 Kongruenzabbildungen – Teil 1 von 3: **Zusatz** (Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts)
- RS II/III: 46 Kongruenzabbildungen – Teil 3 von 3 ← 46 Kongruenzabbildungen – Teil 2 von 3: **Zusatz** (Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts)
- IB Std: 91 Schrägbilder und Raumdarstellung – Teil 2 von 2 ← 91 Schrägbilder und Raumdarstellung – Teil 1 von 2: **Zusatz** (Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts)
- IB Ext: 91 Schrägbilder und Raumdarstellung – Teil 2 von 2 ← 91 Schrägbilder und Raumdarstellung – Teil 1 von 2: **Zusatz** (Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts)
- IB Std: 101 Prismen und Zylinder – Teil 2 von 2 ← 101 Prismen und Zylinder – Teil 1 von 2: **Zusatz** (Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts)
- IB Ext: 101 Prismen und Zylinder – Teil 2 von 2 ← 101 Prismen und Zylinder – Teil 1 von 2: **Zusatz** (Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts)

- Im Gymnasium braucht 46 Teil 3 hart nur Teil 1, wie entschieden.
- 101 Teil 2 braucht Teil 1 in RS I und II/III nur empfohlen: Prismen und Zylinder stehen in der Realschule bei 92. Damit ist der II/III-Verstoß „101 Teil 2 ← Teil 1“ aufgelöst.

## 4 Aufbau nach der Teilung

- **Teilung:** Teil n braucht Teil n−1, hart (8 Kanten).
- **Bisherige Voraussetzungen** (128, ohne stillgelegte Themen) sind dem passenden Teil zugeordnet:
  - „braucht“ geht an den ersten Teil, dessen Klasse in Gym und RS I nicht vor der Voraussetzung liegt.
  - „wird gebraucht von“ geht an den letzten Teil, der nicht nach dem abhängigen Thema liegt.
  - Drei Fälle sind inhaltlich gesetzt (Annahme): 47, 44 und 4 brauchen nur Teil 1 von 46 bzw. 29.
- Zusammen 137 Kanten, alle in der JSON.

**Wichtige Zuordnungen:**
- 29 Terme umformen:
  - Teil 1 braucht 28 und 102 (hart).
  - Teil 2 wird gebraucht von 8, 31, 97 (hart) und 35 (empfohlen).
  - 4 braucht Teil 1.
- 61 Zufall und Laplace: Teil 1 wird gebraucht von 63; Teil 2 von 62 und 64 (alle hart).
- 46 Kongruenzabbildungen: Teil 2 wird gebraucht von 74, Teil 3 von 49, Teil 1 von 47 und 44.
- 26 Proportionalität: Teil 1 braucht 25; Teil 2 wird gebraucht von 93 (hart).
- 91 Schrägbilder: Teil 1 braucht 52 (hart).
- 101 Prismen und Zylinder: Teil 2 (Cavalieri) wird gebraucht von 92 Pyramide, Kegel, Kugel (empfohlen). Das passt: Gym 10 und RS 9 begründen damit das Pyramidenvolumen.

**Prüfung der ganzen Kette gegen die Klassenlage:**
- **Gymnasium: 0 Verstöße. RS Gruppe I: 0 Verstöße.**
- RS II/III: 2 vor der Zusatz-Regel, danach 1.
  - 37 ← 103 (empfohlen; 103 ist in II/III kein Lehrplanstoff).
  - 101 Teil 2 ← Teil 1: Nach der Zusatz-Regel ist das nur empfohlen, der Verstoß entfällt (Abschnitt 3a).
- IB je Kurs: 2 hart, 7 empfohlen.
  - Hart: 63 ← 61 Teil 1 (MYP 1 gegen 2) und 29 Teil 1 ← 102. Das zweite ist **Sebastians Entscheidung, bleibt**, nur gemeldet.
  - Empfohlen, u. a.: 92 ← 101 Teil 2 (101 hat keine IB-Klasse), 44 ← 46, 34 ← 93, 37 ← 103, 45 ← 73, 23 ← 16, 100 ← 25.

**46 im Gymnasium:** entschieden (16:20) und umgesetzt: Teil 2 ist Zusatz, Teil 3 braucht hart nur Teil 1.

**Sollte A2 (Voraussetzungen je Etappe):** offen. Die 87 Reihenfolge-Hinweise aus LK-D sind die Grundlage. Mit der Teilung lösen sich die meisten davon auf, weil die betroffenen Etappen jetzt in getrennten Teilen liegen (26, 29, 46). Eine Liste je Etappe liefere ich auf Ansage.

## 5 Grenzfälle (keine Teilung, Anzeige „weitergeführt“)

| Thema | Teil | Spur | Klassen | Empfehlung |
|---|---|---|---|---|
| 2 Lineare Gleichungen | – | IB Std | 2, 3 | nicht teilen |
| 2 Lineare Gleichungen | – | IB Ext | 2, 3 | nicht teilen |
| 6 Gleichungssysteme mit 2 Unbekannten | – | IB Ext | 3, 4 | nicht teilen |
| 8 Quadratische Gleichungen (allgemein) | – | RS II/III | 9, 10 | nicht teilen |
| 18 Grundrechenarten und Rechengesetze | – | IB Std | 1, 2 | nicht teilen |
| 18 Grundrechenarten und Rechengesetze | – | IB Ext | 1, 2 | nicht teilen |
| 20 Wurzeln und reelle Zahlen | – | IB Std | 3, 4 | nicht teilen |
| 20 Wurzeln und reelle Zahlen | – | IB Ext | 3, 4 | nicht teilen |
| 21 Brüche und Anteile | – | IB Std | 1, 2 | nicht teilen |
| 21 Brüche und Anteile | – | IB Ext | 1, 2 | nicht teilen |
| 28 Terme aufstellen und deuten | – | IB Std | 1, 2 | nicht teilen |
| 28 Terme aufstellen und deuten | – | IB Ext | 1, 2 | nicht teilen |
| 29 Terme umformen | 1 | IB Std | 1, 2 | nicht teilen |
| 29 Terme umformen | 1 | IB Ext | 1, 2 | nicht teilen |
| 32 Zuordnung und Funktion | – | IB Std | 1, 4 | nicht teilen |
| 32 Zuordnung und Funktion | – | IB Ext | 1, 4 | nicht teilen |
| 33 Lineare Funktionen | – | RS II/III | 8, 9 | nicht teilen |
| 33 Lineare Funktionen | – | IB Std | 3, 4 | nicht teilen |
| 42 Grundbegriffe und Figuren | – | IB Std | 1, 2 | nicht teilen |
| 42 Grundbegriffe und Figuren | – | IB Ext | 1, 2 | nicht teilen |
| 44 Konstruktionen, Kongruenz und Beweise | 1 | IB Std | 2, 3 | nicht teilen |
| 44 Konstruktionen, Kongruenz und Beweise | 1 | IB Ext | 2, 3 | nicht teilen |
| 47 Ähnlichkeit und Strahlensätze | – | IB Std | 3, 4 | nicht teilen |
| 47 Ähnlichkeit und Strahlensätze | – | IB Ext | 3, 4 | nicht teilen |
| 50 Umfang und Flächeninhalt | – | IB Std | 1, 2 | nicht teilen |
| 50 Umfang und Flächeninhalt | – | IB Ext | 1, 2 | nicht teilen |
| 55 Trigonometrie im rechtwinkligen Dreieck | – | IB Std | 3, 4 | nicht teilen |
| 55 Trigonometrie im rechtwinkligen Dreieck | – | IB Ext | 3, 4 | nicht teilen |
| 63 Verknüpfte Ereignisse | – | IB Std | 1, 4 | nicht teilen |
| 63 Verknüpfte Ereignisse | – | IB Ext | 1, 4 | nicht teilen |
| 98 Winkelsätze | – | IB Std | 1, 3 | nicht teilen |
| 98 Winkelsätze | – | IB Ext | 1, 3 | nicht teilen |

- RS II/III: 8 (9 + 10) und 33 (8 + 9). Würde II/III teilen, kämen genau diese zwei Themen dazu.
- IB: Schulbuch-Orientierung, kein Teilungsgrund.

## 6 Aufbau-Kette je Teil (Anzeige)

| Teil | Baut auf | Geht weiter in |
|---|---|---|
| 26 Direkte Proportionalität und Dreisatz – Teil 1 von 2 | 25 Größen und Einheiten (Gym 5 · RS I 5) (hart) | 26 Direkte Proportionalität und Dreisatz – Teil 2 von 2 (Gym 5 · RS I 6) |
| 26 Direkte Proportionalität und Dreisatz – Teil 2 von 2 | 26 Direkte Proportionalität und Dreisatz – Teil 1 von 2 (Gym 5 · RS I 5) (hart) | 93 Indirekte Proportionalität (Gym 8 · RS I 7) |
| 29 Terme umformen – Teil 1 von 2 | 28 Terme aufstellen und deuten (Gym 7 · RS I 6) (hart); 102 Potenzgesetze (Gym 7 · RS I 7) (hart) | 4 Formeln umstellen (Gym 8 · RS I –); 29 Terme umformen – Teil 2 von 2 (Gym 7 · RS I 8) |
| 29 Terme umformen – Teil 2 von 2 | 29 Terme umformen – Teil 1 von 2 (Gym 7 · RS I 7) (hart) | 8 Quadratische Gleichungen (allgemein) (Gym 9 · RS I 9); 97 Quadratische Terme und Extremwerte (Gym – · RS I 8); 35 Quadratische Funktionen (Gym 9 · RS I 9); 31 Bruchterme (Gym 8 · RS I 8) |
| 44 Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 | 43 Mit Winkeln rechnen (Gym 5 · RS I 5); 98 Winkelsätze (Gym 7 · RS I 7); 46 Kongruenzabbildungen – Teil 1 von 3 (Gym 7 · RS I 6) | 44 Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 (Gym 7 · RS I 8) |
| 44 Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 | 44 Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 (Gym 7 · RS I 7) (hart) | – |
| 46 Kongruenzabbildungen – Teil 1 von 3 | 42 Grundbegriffe und Figuren (Gym 5 · RS I 5) | 47 Ähnlichkeit und Strahlensätze (Gym 9 · RS I 9); 44 Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 (Gym 7 · RS I 7); 46 Kongruenzabbildungen – Teil 2 von 3 (Gym 7 · RS I 7) |
| 46 Kongruenzabbildungen – Teil 2 von 3 | 46 Kongruenzabbildungen – Teil 1 von 3 (Gym 7 · RS I 6) (hart) | 74 Zweireihige Determinanten (Gym – · RS I 7); 46 Kongruenzabbildungen – Teil 3 von 3 (Gym 7 · RS I 8) |
| 46 Kongruenzabbildungen – Teil 3 von 3 | 46 Kongruenzabbildungen – Teil 2 von 3 (Gym 7 · RS I 7) (hart) | 49 Matrizen und Abbildungen mit Matrizen (Gym – · RS I 10) |
| 61 Zufall und Laplace – Teil 1 von 2 | 21 Brüche und Anteile (Gym 6 · RS I 6) (hart) | 63 Verknüpfte Ereignisse (Gym 9 · RS I 8); 61 Zufall und Laplace – Teil 2 von 2 (Gym 8 · RS I 9) |
| 61 Zufall und Laplace – Teil 2 von 2 | 61 Zufall und Laplace – Teil 1 von 2 (Gym 8 · RS I 8) (hart) | 62 Mehrstufige Zufallsexperimente (Gym 10 · RS I 10); 64 Simulation (Gym 10 · RS I 9) |
| 91 Schrägbilder und Raumdarstellung – Teil 1 von 2 | 52 Körper darstellen (Gym 8 · RS I 5) (hart) | 91 Schrägbilder und Raumdarstellung – Teil 2 von 2 (Gym 10 · RS I 8) |
| 91 Schrägbilder und Raumdarstellung – Teil 2 von 2 | 91 Schrägbilder und Raumdarstellung – Teil 1 von 2 (Gym 10 · RS I 7) (hart) | – |
| 101 Prismen und Zylinder – Teil 1 von 2 | 99 Flächen von Parallelogramm, Dreieck und Trapez (Gym 6 · RS I 6); 100 Volumen (Gym 6 · RS I 6); 51 Kreisberechnungen (Gym 8 · RS I 9) | 101 Prismen und Zylinder – Teil 2 von 2 (Gym 10 · RS I 9) |
| 101 Prismen und Zylinder – Teil 2 von 2 | 101 Prismen und Zylinder – Teil 1 von 2 (Gym 8 · RS I 9) (hart) | 92 Pyramide, Kegel, Kugel (Gym 10 · RS I 9) |

Für alle übrigen Themen steht die Kette in `aufbau_kette` (JSON).

## Gesichert / Annahme / offen

**Gesichert:**
- Teilung nach der Regel.
- 0 Verstöße in Gymnasium und RS I.
- Keine Klassenänderung; SQL-Probelauf mit der neuen Fassung bestanden.
- Prüfskript OK.
- Die IB-Zahl der harten Verstöße ist 2 (berichtigt).

**Annahme:**
- Etappen-Klassen aus meiner Etappenzuordnung.
- Drei inhaltlich gesetzte Voraussetzungen.
- Audit-Urteil „gedeckt / teilweise / fehlte“.
- Untertitel als Vorschlag.

**Offen (Sebastian):**
- Liste mit 101 bestätigen (7 Themen, 15 Teile, 8 neue Flüge).
- Kurzflug 101 Teil 2.
- Kind 2 in 29 Teil 2: neue Etappe nachholen oder als Zusatz führen.
- 43/69/71 als Vertiefung (A3).
- Beweis-Aufgabe zu √2 (Gym 9).
- Etappen-Voraussetzungen (A2).
- Neuer Probelauf des Haupt-Chats mit der geänderten `lk_korrektur_2211.sql`.
