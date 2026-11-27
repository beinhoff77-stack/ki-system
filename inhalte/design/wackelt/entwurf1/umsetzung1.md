# Vorgabe WK, erste Runde: „Was wackelt“ als Gesprächsvorbereitung

Designer, 27.11.2026. Ersetzt für den Reiter „Was wackelt“ die Arbeitsliste LW-3 (1a) und die Tabelle „Je Etappe“ (LA-3). Kein App-Code geändert.
Entwurf: `entwurf1/index.html` (eine Datei, keine Netz-Abhängigkeit, hell/dunkel, 400 und 1280 px). Unten links der Entwurfs-Schalter (A/B, hell/dunkel, leer, ↺); er gehört nicht zur App.
Adresse für feste Zustände: `#k=2&z=g|w|a&v=A|B&g=hell|nacht&p=<n>&weg=1&besp=<n>&leer=1&zettel=1&ohne=1`.
Daten im Entwurf sind erfunden: „Kind 1“ (Klasse 5), „Kind 2“ (Klasse 8), heute = Fr 27.11.2026. Fehlbild-Kennungen, Beschreibungen und Merksätze stammen aus `daten/regeln-universum.json`; zwei Aufgaben aus `inhalte/mathe-profi/rollend-12/` (R5-V121, R5-V159, R5-V163).
**[G]** gesichert (im Repo gelesen oder im Entwurf gebaut und gemessen, Chrome 400 × 860) · **[A]** Annahme · **[M]** Meinung.

## 1 Kurzfassung

- Die Seite beantwortet zuerst eine Frage: **„Worüber rede ich heute mit dem Kind – und wie fange ich an?“** Oben eine Voranalyse in einem Satz („Drei Punkte lohnen ein Gespräch. Zwei Fehler waren nur Flüchtigkeit.“), darunter **höchstens drei** nummerierte Punkte „Das zuerst besprechen“, jeder mit Art (Fehlvorstellung / Lücke), einem Satz Begründung und Kennzahlen.
- Ein Punkt aufgeklappt (Handy: darunter; Rechner: rechts daneben): **So fangen Sie an** (eine Frage an das Kind) → **Wenn es stockt: die Regel** (Merksatz + Blatt im Regel-Universum) → **die falschen Aufgaben** (Aufgabe mit Tabelle/Zeichnung, Eingegeben/Richtig, erkannter Fehler, Versuch, Tipp, später richtig?, Lösungsweg zum Aufklappen; beim Fehler-Detektiv die Auswahl mit „gewählt“ und „richtig“) → **Danach üben lassen** (2–3 Aufgaben mit Lösung) → **Besprochen … / Später**.
- Zustände je Punkt: offen → besprochen (Datum, Notiz) → sitzt wieder (3 eigene Lösungen in Folge, automatisch) → Verlauf. „Später“ legt zur Seite. Ein neuer Fehler holt jeden Punkt zurück („wieder offen“, alte Notiz bleibt sichtbar).
- **Empfehlung: Variante A „Gesprächsplan“.** Variante B „Aufgaben zuerst“ (alle falschen Aufgaben nach Lernkarte, Voranalyse nur als Kopf) ist im File umschaltbar; sie ist ein Inventar, kein Plan. [M] Begründung in Abschnitt 2.4.

## 2 Was die Seite zeigt

### 2.1 Reihenfolge von oben nach unten (Variante A) [G]
1. Kopf wie heute (‹ · Kinder-Umschalter · ⋯; Reiter Überblick | **Was wackelt (Zahl)** | Lehrplan). Die rote Zahl = Zahl der offenen Punkte (Regel R9), grau bei 0.
2. **Zeitraum**: „Seit Gespräch (Datum)“ | „7 Tage“ | „Alles“; Standard „Seit Gespräch“. Am Rechner nur so breit wie die linke Spalte (470 px).
3. **Voranalyse-Karte**: Etikett „Voranalyse · seit dem Gespräch am 18.11.“, Satz 22 px fett, darunter Aufgaben · richtig · falsch · „dauert etwa n Min.“ (5 Min. je Punkt), Knopf „Gesprächszettel drucken“.
4. **Das zuerst besprechen** (1–3 Karten, linker Rand 8 px in Artfarbe, Nummer im schwarzen Kreis 32 px, Marken, Titel 19 px fett, Ort 14 px leise, Begründung 16 px, Kennzahlen 14 px Festbreite).
5. **Besprochen – wird nachgeübt** (Nummer ✓, blaues Feld mit Notiz und drei Punkten „n von 3“).
6. **Auch noch offen** (Punkte ab Rang 4, ohne Begründungssatz).
7. **Nicht besprechen** – eine Zeile je Flüchtigkeit und je „einmal falsch“; antippen zeigt die Aufgabe.
8. **Später** (zur Seite gelegte Punkte).
9. **Verlauf · erledigt (n)** zugeklappt: ✓, Titel, Art, „besprochen am“, „sitzt wieder seit“, Notiz, Knopf „Wieder öffnen“.
10. **ⓘ So entsteht die Voranalyse** zugeklappt: die Regeln in vier Sätzen.

Leerer Zustand (keine offenen und keine wartenden Punkte): grüner Haken, „Nichts wackelt seit dem Gespräch am 20.11.“, Zahlen, ein gelbes Feld **„Statt Fehler: einmal konkret loben“** mit einem Satz zur Lernkarte mit den meisten richtigen Antworten, „Wieder sicher: …“ aus dem Verlauf, Verweis „Was als Nächstes kommt: im Lehrplan ansehen ›“; darunter weiter „Nicht besprechen“ und Verlauf. [G] Seite 866 px bei 400 px.

### 2.2 Ein Punkt, aufgeklappt [G]
Reihenfolge: (bei besprochen/später zuerst der Zustand) · So fangen Sie an · Wenn es stockt: die Regel · Die Aufgaben (n) · neueste zuerst · Danach üben lassen · Zustand.
- **So fangen Sie an**: gelbe Fläche (wie Merksatz im Regel-Universum), die Frage 20 px fett in Anführungszeichen, darunter fest: „Dann zuhören, nicht vorrechnen. Das Kind soll selbst sagen, was es gemacht hat. Erst wenn es stockt: die Regel unten zeigen und die erste Aufgabe gemeinsam noch einmal lösen.“
- **Regel**: Etikett „Rechenregel 7 · Minus vor der Klammer“, Merksatz 17 px fett, Verweis „Blatt für Eltern und Lehrer ›“ (`#/regeln/lehrer-r7`). Bei Ideen und Arbeitsweisen „Im Regel-Universum ansehen ›“ (`#/regeln/kind-idee-geo-5`, `#/regeln/kind-weise-7`), weil es dafür kein Lehrer-Blatt gibt.
- **Aufgabe**: Kopf „[Fehler-Detektiv ·] Thema“ links, Tag rechts (13 px Versalien). Text 17 px; Zeilen des Fehler-Detektivs nummeriert in Festbreite; Tabelle oder Zeichnung (höchstens 300 px breit). Zahl/Term: zwei Felder **EINGEGEBEN** (rot getönt) | **RICHTIG** (grün getönt), Wert 19 px Festbreite. Auswahl / Fehler-Detektiv: alle Optionen, „✗ gewählt“ rot, „✓ richtig“ grün. Darunter „**Erkannter Fehler:** …“ oder leise „Fehlerart nicht erkannt.“ Meta-Zeile 14 px: „Erstes Mal an dieser Aufgabe | n. Mal“ · „im 2. Anlauf (1. Anlauf: …)“ · „mit/ohne Tipp“ · „✓ später richtig gelöst (Tag)“ | „✓ danach eine andere Aufgabe dieser Lernkarte richtig“ | „seitdem nicht richtig gelöst“. Klappzeile „Lösungsweg“ (40 px).
- Handy: höchstens **2 Aufgaben**, dann Knopf „Noch n Aufgaben zeigen“. Rechner: alle, zweispaltig.
- **Danach üben lassen**: 2–3 Zeilen „Aufgabe … | Lösung“, darunter „Auf Papier oder mündlich. Die App prüft danach von selbst: 3 eigene Lösungen in Folge in diesen Lernkarten = ‚sitzt wieder‘.“
- **Zustand** siehe Abschnitt 4.

### 2.3 Rechner ab 1000 px [G]
Variante A zweispaltig: links 470 px (Voranalyse und Listen), rechts der gewählte Punkt in einem Kasten mit Tinte-Rand, klebend unter dem Kopf, eigener Bildlauf. Ohne Auswahl ist Punkt 1 gewählt. Gewählte Karte links mit 2 px Ring, Pfeil zeigt nach rechts.

### 2.4 Rangfolge der Inhalte und warum [M]
Ein Elternteil ohne Mathelehrer-Ausbildung braucht in dieser Reihenfolge:
1. **Worüber reden** (höchstens drei Punkte) – mehr schafft ein Gespräch von 10–15 Minuten nicht; der Rest wartet sichtbar unter „Auch noch offen“.
2. **Wie anfangen** – eine Frage, die das Kind erklären lässt. Das ist der schwerste Teil für Laien; deshalb steht er vor den Aufgaben.
3. **Was richtig ist** – der Merksatz in Kinderworten, wörtlich wie im Regel-Universum. Er ist die Rückfallebene, kein Vortrag.
4. **Die Belege** – die falschen Aufgaben mit Antwort, Lösung und erkanntem Fehler. Zum Nachsehen vor dem Gespräch und zum gemeinsamen Anschauen.
5. **Was danach** – zwei, drei Aufgaben und das Wissen, dass die App von selbst merkt, wann es wieder sitzt.

**Bewusst weggelassen** (wäre zu viel): Prozentwerte, Trefferquoten je Etappe, Serien und Stufen, Kennungen wie `fb.minusklammer…` (stehen nur auf dem Lehrer-Blatt), alle Versuche einer Aufgabe, richtige Antworten, Zeitkurven, „Knobel“-Zahlen, der ganze Lernstand je Etappe (steht im Lehrplan). Flüchtigkeiten bekommen keine Gesprächsfrage – das Signal ist: nicht ansprechen.
**Warum A statt B:** B zeigt alles gleichwertig; der Elternteil muss die Rangfolge selbst bilden und findet den Gesprächseinstieg erst nach dem Inventar. B ist sinnvoll für jemanden, der jede Aufgabe sehen will – das deckt A über „Alles“ und den Aufklapper je Punkt ab. Gemessen [G]: B ist bei 400 px 5 101 px hoch, A mit einem offenen Punkt 3 467–4 191 px, geschlossen 1 764 px.

## 3 Voranalyse – prüfbare Regeln

Grundmenge: **endgültig falsche Antworten** des Kindes (`schule.fehler_endgueltig_am(v) is not null`, wie LW-S 2: Übung nach Wertung „falsch“, Test sofort; ein falscher 1. Anlauf mit zweiter Chance zählt nicht), mit `am` im Zeitraum.
Zeitraum: „Seit Gespräch“ = nach dem spätesten Zeitpunkt „besprochen“ dieses Kindes **vor dem heutigen Tag** (wer heute bespricht, verschiebt den Zeitraum erst morgen, sonst verschwänden die übrigen Punkte sofort); „7 Tage“ = jetzt − 7 × 24 h; „Alles“ = ohne Grenze. Ohne je ein Gespräch: wie „Alles“.

| Nr | Regel |
|---|---|
| R0 | Eine falsche Antwort, die zu einem gespeicherten Punkt gehört (gleiche Fehlbild-Kennung bzw. gleiche Lernkarte) und **vor** dessen Zeitpunkt (besprochen / später) liegt, zählt nicht noch einmal. |
| R1 Fehlvorstellung | Dieselbe **erkannte Fehlbild-Kennung** in ≥ 3 Antworten aus ≥ 2 verschiedenen Aufgaben **oder** in ≥ 2 Antworten aus ≥ 2 verschiedenen Lernkarten. Ein Punkt je Kennung; die Antworten sind damit verbraucht. Stufe 1 (nur grobes `grund`): ≥ 3 Antworten mit demselben `grund` in ≥ 2 Lernkarten. |
| R2 Lücke | Übrige Antworten je Lernkarte (`einheit_id` + `lernziel`): ≥ 2 Antworten aus ≥ 2 verschiedenen Aufgaben. Außerdem jede Etappe mit `wieder_offen` (H1). Ein Punkt je Lernkarte. |
| R3 Flüchtigkeit | Übrige Lernkarte mit genau 1 Antwort, und danach ≥ 1 richtige Antwort in derselben Lernkarte ohne Tipp (`hilfe = 0`). |
| R3b Einmal falsch | Übrige Lernkarte mit genau 1 Antwort ohne richtige danach. Steht wie R3 unter „Nicht besprechen“ („kommt in der Wiederholung“). |
| R4 Wieder offen | Gespeicherter Punkt (besprochen, später, sitzt wieder) und danach ≥ 1 neue Antwort derselben Kennung bzw. Lernkarte → Punkt wieder „offen“, Marke „wieder offen“, **Art bleibt** die gespeicherte (auch bei nur einer Antwort). |
| R5 Gewicht | Art (Fehlvorstellung 30, Lücke 20) + 5 je Antwort (höchstens 5 Antworten) + Frische des letzten Fehlers (heute/gestern +10, ≤ 7 Tage +5) + „wieder offen“ +15 − 10, wenn seit dem letzten Fehler schon ≥ 2 richtige in Folge ohne Tipp. |
| R6 Sortierung | Gewicht absteigend, bei Gleichstand letzter Fehler neuer zuerst, dann `thema_id`. |
| R7 Oben | Die ersten **3** offenen Punkte stehen unter „Das zuerst besprechen“ (mit Begründungssatz), alle weiteren offenen unter „Auch noch offen“. R3/R3b nie oben. |
| R8 Sätze | Fehlvorstellung: „{N-mal} derselbe Fehler in {a} Aufgaben[ aus {t} Themen | aus {l} Lernkarten]: {Beschreibung des Fehlbilds}.“ · Lücke: „{n} von {a} Aufgaben zu „{Lernkarte}“ falsch[, jedes Mal mit einem anderen Fehler] – das Verfahren sitzt noch nicht.“ · Wieder offen: „Am {Datum} besprochen – danach {N-mal} wieder derselbe Fehler.“ · Flüchtigkeit: „Einmal falsch ({Tag}), danach {k}× richtig.“ · Kennzahlen: „{n} falsch · zuletzt {heute|gestern|vor n Tagen|am T.M.} · danach {k}× richtig | seitdem nicht richtig“. Kopfsatz: „{Ein Punkt lohnt|Zwei/Drei Punkte lohnen} ein Gespräch. {Ein Fehler war|n Fehler waren} nur Flüchtigkeit.“ oder „Nichts zu besprechen.“ |
| R9 Zahl am Reiter | Anzahl offener Punkte (R1, R2, R4) **ohne** Zeitraum-Grenze (R0 nimmt Erledigtes heraus) – die Zahl springt nicht mit dem Filter. |

Prüffälle aus dem Entwurf [G]: Kind 2 „Seit Gespräch 18.11.“ → 1. Minusklammer (R1, 4 Antworten, 4 Aufgaben, 2 Themen, Gewicht 60) · 2. Ungleichung (R4, Gewicht 55) · 3. Pythagoras (R2, Gewicht 45) · Flüchtigkeit Prozentwert, Steigung; Zahl 3. Kind 1 „Seit Gespräch 20.11.“ → 1. Umrechnen eine Stelle daneben (R1, 55) · 2. Tabelle auswerten (R2, 40) · Flüchtigkeit Winkel · Einmal falsch Absolute Häufigkeit; Zahl 2.

## 4 Zustandsmodell

| Zustand | Wie hinein | Sichtbar als | Wie heraus |
|---|---|---|---|
| **offen** | neu nach R1/R2; „Doch jetzt besprechen“; „Wieder öffnen“; R4 | Karte oben bzw. „Auch noch offen“; Knöpfe „✓ Besprochen …“, „Später“ | Besprochen, Später |
| **besprochen** | „✓ Besprochen …“ → Feld „Notiz (freiwillig)“ mit Platzhalter „Was hat das Kind gesagt?“ → „✓ Besprochen speichern“ | Abschnitt „Besprochen – wird nachgeübt“, Marke „besprochen T.M.“, Notiz, „Nachüben: ●○○ 1 von 3 eigenen Lösungen in Folge“; Knopf „Doch noch offen“ | automatisch → sitzt wieder; neuer Fehler → offen (R4) |
| **später** | „Später“ | Abschnitt „Später“, Marke gestrichelt | „Doch jetzt besprechen“; neuer Fehler → offen (R4) |
| **sitzt wieder** | automatisch: nach „besprochen“ 3 richtige Antworten in Folge ohne Tipp in den Lernkarten des Punkts (wie „3 eigene Lösungen in Folge“, H1) | Verlauf: ✓, besprochen am, sitzt wieder seit, Notiz | „Wieder öffnen“; neuer Fehler → offen (R4) |

Jede Änderung: sofort speichern, unten 5 Sekunden „↶ Rückgängig“ (wie heute). Nichts wird gelöscht; der Verlauf zeigt alles Erledigte. Gespeichert wird je Kind und **Schlüssel**: `fb:<Kennung>` (Fehlvorstellung) oder Lernkarte (Lücke). Flüchtigkeiten haben keinen Zustand.

**Gesprächszettel**: Knopf in der Voranalyse öffnet eine Papierfassung (Drucken | Schließen): je der drei Punkte Titel, Begründung, „Fragen: …“, die Aufgaben mit Antwort des Kindes und Lösung, „Wenn es stockt: …“, „Danach üben: …“, drei Linien „Notiz“. Druck blendet Kopf und Knöpfe aus. [G] 2 542 px bei 400 px für drei Punkte.

## 5 Datenbedarf je Element

### 5.1 Liefert der Server heute schon [G]
| Quelle | Felder | Gebraucht für |
|---|---|---|
| `schule_wackelt_lesen` | `zu_besprechen`, `eintraege[]`: `thema_id`, `titel`, `einheit_id`, `lernziel`, `status` (zu_besprechen \| beobachten \| besprochen), `status_gespeichert`, `status_am`, `status_von`, `wieder_offen`, `fehler`, `fehler_neu`, `letzter_fehler_am`, `etappen[]` (`titel`, `fehler`, `wackelt`, `sitzt`, `besprochen_am`) | Zustand je Thema/Etappe, „wieder offen“, Zahl am Reiter (heutige Regel) |
| `schule_wackelt_setzen` | `{lernender_id, thema_id, status, einheit_id?, lernziel?}` | offen = `zu_besprechen`, später = `beobachten`, besprochen |
| `schule_lernstand` je Etappe | `richtig`, `falsch`, `mit_tipp`, `zuletzt`, `sitzt`, `wieder_offen`, `eigene_loesungen`, `folge`, `regel` („Kurz gesagt“), `besprochen_am/_von`, `fehler_gruende {grund: n}`, `fehler[]` (**nur die letzten 3**): `frage`, `antwort`, `antworttyp`, `antworten`, `loesung`, `schablone`, `grafik`, `am`, `grund` | Aufgabe, Eingegeben/Richtig, Tabelle/Zeichnung, Auswahl des Fehler-Detektivs (`antwort.index` + `antworten`) |
| `schule_notiz_setzen` | freie Notiz `{lernender_id, text}`; `besprochen: {einheit_id, lernziel}` (LA-3) | Notiz beim Besprechen (Stufe 1) |
| Tabelle `schule.versuch` | `aufgabe_id`, `am`, `richtig`, `antwort`, `hilfe` (0–2), `versuch_nr`, `anlauf` (1/2/null), `misch`, `testsitzung_id`, `wertung_fest`; Funktionen `fehler_endgueltig_am`, `versuch_wertung` | alles für R0–R9 – liegt vor, wird aber nicht ausgeliefert |
| Tabelle `schule.aufgabe` | `frage` (text, grafik, schablone), `antworttyp`, `antworten`, `loesung`, `loesungsweg`, `variante_gruppe` (= Lernkarte), `einheit_id`, `stufe`, `typ`, `form` (u. a. `fehler_detektiv`), `zaehlt` | Aufgabe, Lösungsweg, Kennzeichen „Fehler-Detektiv“ |
| `antwort_bewerten` | `grund`: vorzeichen, komma, vertauscht, gerundet, falsche_einheit (nur Zahl/Lücken; bei Auswahl keins) | grobe Fehlerart (Stufe 1) |
| `daten/regeln-universum.json` | `regeln[].satz` (Merksatz), `lehrer[R].themen[].thema_id`, `lehrer[R].fehlbilder[]` (`kennung`, `beschreibung`); Adressen `#/regeln/lehrer-r<n>`, `#/regeln/kind-idee-…`, `#/regeln/kind-weise-<n>` | Regel-Verweis, Fehlbild-Beschreibung |

### 5.2 Muss neu erfasst oder berechnet werden
| Element | Was fehlt | Vorschlag |
|---|---|---|
| Liste der falschen Aufgaben im Zeitraum | `fehler[]` ist auf 3 je Etappe begrenzt, ohne Zeitraum, ohne `aufgabe_id`, `loesungsweg`, `anlauf`, Antwort des 1. Anlaufs, `hilfe`, `versuch_nr` | **neue Lese-Aktion** `schule_wackelt_analyse {lernender_id, seit?}` → je endgültig falscher Antwort: `versuch_id`, `aufgabe_id`, `einheit_id`, `lernziel`, `thema_id`, `am`, `antwort`, `erst_antwort` (1. Anlauf derselben Aufgabe, falls `anlauf = 2`), `anlauf`, `hilfe`, `versuch_nr`, `grund`, Aufgabe (`frage`, `antworttyp`, `antworten`, `loesung`, `loesungsweg`, `form`); dazu je Lernkarte die Folge richtig/falsch ab dem ersten Fehler (`am`, `richtig`, `hilfe`) |
| „später richtig gelöst“, Flüchtigkeit, „sitzt wieder“ | Reihenfolge der Versuche nach dem Fehler | aus der Folge oben (App rechnet) |
| **Erkanntes Fehlbild** (Kennung + Beschreibung) | `fehlbilder`, `regel`, `kennung` der Aufgaben-Dateien werden **nicht eingespielt** (`tools/rollend_sql.py`: nur `l t p s g y f a o h w` + `form`, `zaehlt`); in `supabase/` kommt „fehlbild“ nicht vor | Spalten `schule.aufgabe.fehlbilder jsonb` (`[{antwort | index, fehlbild, beschreibung}]`), `regel text`, `kennung text`; Einspielen in `rollend_sql.py`; beim Lesen Antwort normalisiert (wie `antwort_bewerten`) gegen `fehlbilder[].antwort` bzw. `index` vergleichen → `fehlbild`, `fehlbild_text` |
| Zustand je Fehlvorstellung | `wackelt_status` ist je Thema/Etappe; eine Fehlvorstellung geht über Themen | `schule.wackelt_status` + Spalte `fehlbild text` (Teil von `bezug`), Status `'spaeter'` als Name für `beobachten` (oder Anzeige-Übersetzung) |
| Notiz am Punkt | `wackelt_status` hat kein Textfeld | Spalte `notiz text` (≤ 500 Zeichen) in `wackelt_status`; Verlauf = alte Zeilen behalten (Tabelle `wackelt_verlauf` oder `am`-Historie) – heute überschreibt `on conflict` |
| Gesprächseinstieg | gibt es nirgends | Inhalt vom Mathe-Profi: je Fehlbild-Kennung `einstieg` (in `kennungen.json`, gebaut nach `regeln-universum.json`), je Lernkarte ein Ersatz-Einstieg; ohne Text der feste Satz „Erklär mir, wie du bei dieser Aufgabe vorgegangen bist – Schritt für Schritt.“ |
| Danach üben lassen | keine Auswahl | Stufe 1: 2–3 Aufgaben derselben Lernkarte, die das Kind noch nicht gesehen hat (`aufgabe` ohne `versuch`), mit `loesung`; Stufe 2: je Fehlbild 2–3 Aufgaben mit genau diesem Fehlbild in `fehlbilder` |
| Zeit je Antwort | nicht gespeichert (kein Feld in `schule.versuch`) | nicht nötig für die Regeln; nicht erfassen (siehe Frage 5) |

## 6 Offene Fragen an den Nutzer (mit Vorschlag)
1. **Höchstens drei Punkte oben – passt das?** Vorschlag: ja, drei; der Rest steht darunter unter „Auch noch offen“.
2. **Gesprächseinstiege schreiben lassen?** Ohne sie bleibt nur ein allgemeiner Satz. Vorschlag: Auftrag an den Mathe-Profi, je Fehlbild-Kennung eine Frage (65 verschiedene Kennungen in den Aufgaben-Dateien unter `inhalte/mathe-profi/`, davon 30 im Regel-Universum beschrieben, gezählt [G]) plus je Thema eine Ersatz-Frage.
3. **„Danach üben“ nur zeigen oder dem Kind schicken?** Vorschlag Stufe 1: nur zeigen (Papier/mündlich); Stufe 2: Knopf „In ‚Nachbessern‘ legen“, damit die Aufgaben beim Kind auf der Abflugtafel erscheinen.
4. **Zeitraum-Standard „Seit Gespräch“ oder „7 Tage“?** Vorschlag: „Seit Gespräch“ – es passt zum Rhythmus „einmal sprechen, dann wieder lernen“; ohne je ein Gespräch gilt „Alles“.
5. **Zeit je Antwort erfassen?** Vorschlag: nein. Für Flüchtigkeit reicht „danach richtig“; eine Zeitmessung lädt zum Hetzen ein.

## 7 Schnittfolge für den Bau

**Stufe 1 – ohne neue Datenbankfelder** (eine neue Lese-Funktion, sonst nur App):
1. Server: `api.schule_wackelt_analyse {lernender_id, seit?}` (nur lesen; nutzt `fehler_endgueltig_am`, `antwort_bewerten`; liefert die Felder aus 5.2 Zeile 1 und die Folge je Lernkarte). Zugriff wie `schule_wackelt_lesen`.
2. App: Regeln R0–R9 in einer reinen Funktion (testbar ohne Browser); R1 mit `grund` statt Fehlbild-Kennung (strengere Schwelle). Prüffälle aus Abschnitt 3 als Test.
3. App: Seite nach Abschnitt 2 (Variante A), Gesprächszettel, leerer Zustand. Zustand über `schule_wackelt_setzen`: offen = `zu_besprechen`, später = `beobachten`, besprochen; Schlüssel nur Thema oder Etappe (Fehlvorstellung über Themen: Status auf jedes betroffene Thema setzen). Notiz über `schule_notiz_setzen` als freie Notiz „Besprochen: {Titel} – {Text}“. „Sitzt wieder“ aus der Folge nach `status_am`.
4. Regel-Verweis: über `regeln-universum.json` → `lehrer[R].themen[].thema_id`; hat ein Thema mehrere Regeln, „Regeln zu diesem Thema: …“ als Liste statt eines Merksatzes.
5. Gesprächseinstieg: fester allgemeiner Satz; Nachüben: 2–3 ungesehene Aufgaben der Lernkarte (in Aktion 1 mitliefern).
6. Alte Tabelle „Je Etappe“ und „Alle Etappen mit Stand“ entfallen (stehen im Lehrplan); Zähler am Reiter nach R9.

**Stufe 2 – mit neuen Feldern**:
1. `schule.aufgabe`: `fehlbilder jsonb`, `regel text`, `kennung text`; `tools/rollend_sql.py` und `aufgaben_einfuegen` spielen sie ein; Nachtrag für den Bestand aus den Dateien.
2. `schule_wackelt_analyse` liefert je Antwort `fehlbild`, `fehlbild_text`, `regel`; R1 mit Kennung (Schwellen wie Abschnitt 3).
3. `schule.wackelt_status`: `fehlbild text` (im `bezug`), `notiz text`, Verlauf behalten (keine Überschreibung); Status `spaeter`.
4. Inhalt: `einstieg` je Fehlbild (Mathe-Profi) → `regeln-universum.json`; Nachüben je Fehlbild.
5. Optional: „In ‚Nachbessern‘ legen“ (Frage 3).

## 8 Bilder (`bilder/`, Chrome, deviceScaleFactor 1, Entwurfs-Schalter ausgeblendet außer 13)
01/02 Voranalyse 400 hell/dunkel · 03 Punkt 1 offen mit Fehler-Detektiv, allen Aufgaben und offenem Lösungsweg · 04 dasselbe dunkel · 05 Kind 1, Lücke mit Tabellen · 06 Pythagoras mit Zeichnung · 07 besprochen mit Notiz, 1 von 3 · 08 nach dreimal Nachüben: Verlauf offen, Meldung „sitzt wieder“ · 09/10 leerer Zustand hell/dunkel · 11 Gesprächszettel · 12 Variante B · 13 1280 hell mit Schalter · 14 1280 hell ganze Seite · 15 1280 dunkel Kind 1 · 16 1280 Variante B.
Gemessen [G]: bei 400 und 1280 px kein Element breiter als das Fenster (scrollWidth = Fensterbreite in allen 16 Fassungen).

## 9 Annahmen
- [A] „Letztes Gespräch“ = letzter gespeicherter Zeitpunkt „besprochen“ eines Punkts vor heute; ein eigenes Gesprächs-Datum gibt es nicht.
- [A] Der falsche 1. Anlauf zählt nicht als Fehler, wird aber an der Aufgabe gezeigt („im 2. Anlauf (1. Anlauf: …)“) – er verrät oft die Fehlvorstellung.
- [A] Gesprächseinstiege, Nachübe-Aufgaben und die Notizen im Entwurf sind Beispiele des Designers, vom Mathe-Profi nicht geprüft.
- [A] Schriften wie im Regel-Universum (Space Grotesk, JetBrains Mono); der Entwurf lädt nichts nach und zeigt die Ersatzschrift des Systems.
