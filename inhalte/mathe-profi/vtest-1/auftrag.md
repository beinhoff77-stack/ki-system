# Auftragsblatt „Verstehen in Tests“ (Stufe 1) – für die Aufgabenschreiber

Stand 28.11.2026. Gilt für alle Schreib-Runden der Stufe 1 (`vtest-1a`, `vtest-1b`, `vtest-2`, `vtest-3`). Es passt zum Auftrag des Projektleiters vom 28.11. (Format wie `rollend-15` plus `pool`, `typ`, `form`, `stufe`, `zaehlt`, `lehrplan`, `ersetzt_test`). **Abschnitt 9 listet, was ihr gegenüber diesem Auftrag nachziehen müsst**, damit das Prüfwerkzeug durchläuft.
Plan, Mengen und technische Wirkung: `plan.md` (gleicher Ordner). Vorschlag der Lernziele: `auswahl.json` (gleicher Ordner).

Prüfen: `python3 -I tools/vtest_pruefen.py --runde 1a` (bzw. `1b`, `2`, `3`) muss mit `OK – keine Fehler` enden. HINWEISE von Hand ansehen. Euer `bauen.py` kann zusätzlich prüfen, ersetzt das Werkzeug aber nicht.

---

## 1. Worum es geht

In jeder Einheit bekommt die **Hälfte der Lernziele** (bei ungerader Zahl aufgerundet) im Test eine **Verstehens-Aufgabe statt der bisherigen Rechen-Aufgabe**. Der Test bleibt gleich lang: eine Aufgabe je Lernziel. Für diese Lernziele schreibt ihr außerdem die Korrektur- und Nachtest-Aufgaben, damit auch „Verbessern“ und „Nachtest“ beim Verstehen bleiben. Die anderen Lernziele (Rechnen) bleiben unverändert – für sie schreibt ihr **nichts**.

Maßstab: **wie eine echte Schulaufgabe am bayerischen Gymnasium (G9, LehrplanPLUS)** – nicht wie eine Übungsaufgabe. Stufe 2 oder 3, keine Stufe 1, keine reine Reproduktion. Eine Bauart muss vorher **nicht** geübt worden sein (in der Schulaufgabe wird darauf auch nicht geschaut).

## 2. Welche Lernziele (Reihenfolge der Runden)

Die Reihenfolge der Lernziele ist die der Etappen (`lz` in `inhalte/plan/rollend-einheiten.json`). V = Verstehens-Test (neu schreiben), R = Rechen-Test (bleibt). Regel: genau ⌈n/2⌉ V; möglichst nie zwei R oder drei V nebeneinander (das Werkzeug meldet das als Hinweis). Die Spalte „Vorschlag“ ist meine begründete Auswahl; wählt ihr anders, ist das erlaubt, wenn die Hälfte stimmt – schreibt dann eure Begründung in `auswahl.md` eurer Runde (das Werkzeug meldet die Abweichung als Hinweis).

| Runde | Einheit (id) | Lernbereich (gym_by) | Muster | Vorschlag V-Lernziele | Kurzbegründung |
|---|---|---|---|---|---|
| 1a | `zahlen.potenzen_basis` (41) | M5 3 | R V R V R V V | berechnen, vertauschen, negativ, sach | vertauschen/negativ sind der Verstehenskern (Basis/Exponent, Vorzeichen begründen); berechnen als Fehler-Detektiv (2³ ≠ 6); sach als Umkehren |
| 1a | `zahlen.rechengesetze` (44) | M5 3 | R V R V … R V | klammern, vorteil, verteilen, mal_ganz, umkehraufgabe_mal, schriftlich, sach | Klammern setzen, welches Gesetz/zwei Wege, Vorzeichen begründen, Umkehren, Fehler in schriftlicher Rechnung, rückwärts |
| 1b | `bruch.prozent` (11) | M6 3 | R V R V R V | prozentwert, grundwert, verstehen | Brücke Bruch ↔ Prozent; Grundwert als Umkehren/Fehlerbild „80 % von 272“; Aussagen prüfen |
| 1b | `gleichungen.bruch` (20) | M8 4 | V R V R V R V | definitionsmenge, ueber_kreuz, scheinloesung, graphisch | D begründen/Parameter, Fehler beim Über-Kreuz-Rechnen, Scheinlösung, Graph ↔ Gleichung |
| 1b | `terme.potenzgesetze` (35) | M6 1 | R V V | negativer_exponent, fehler_finden | Muster fortsetzen 2⁻³ = 1/8; Fehler-Detektiv |
| 1b | `zahlen.potenzen_zehner` (42) | M6 1 | R V R V R V V | gross_wissenschaftlich, negativer_exponent, vorsilben_klein, vergleichen_pruefen | „23,1 · 10⁴ ist nicht wissenschaftlich“; 10⁻³ = 1/1000 = 0,001; Umkehren; Vergleichen |
| 1b | `messen.flaechen_vielecke` (93) | M6 2 | R V R V V R V R | dreieck, rueckwaerts, zusammengesetzt, verstehen | Höhe außerhalb/zwei Wege; Umkehren; Zerlegen gegen Ergänzen; Verdoppeln |
| 2 | `finanzen.zinsen` (2) | M6 3 | R V R V R V R V | rollen, jahreszinsen_komma, kapital, zeitanteil | wer zahlt (begründen), Kommafehler, Umkehren, Monate ↔ Jahresbruch |
| 2 | `terme.umformen` (3) | M7 1 | V R V R V | zusammenfassen, minusklammer, aequivalenz | typische Vorzeichenfehler, Äquivalenz durch Einsetzen |
| 2 | `terme.umformen_teil2` (305) | M7 1 | R V V R | ausklammern, binomisch | Ausklammern = Umkehrung; (a − b)² ≠ a² − b² |
| 2 | `geometrie.kreis` (58) | M7 5 | R V R V R V | umkehrung, lage, umkreis_inkreis | Umkehrung Thales; Abstand ↔ Schnittpunkte; Lage des Mittelpunkts |
| 2 | `zahlen.natuerlich` (1) | M5 1 | V R V R … V | stellenwert, ziffern_zu_zahlwort, strahl_eintragen, runden_regel, runden_sinnvoll, roemisch_schreiben, dualsystem | Stellenwertidee, Runden rückwärts, sinnvoll runden, Zweiersystem |
| 3 | `messen.volumen` (95) | M6 2 | R V R V V R V | quader, liter, rueckwaerts, verstehen | Kante ·2 → Volumen ·8; dm³ ↔ l; Umkehren |
| 3 | `daten.darstellen` (13) | M6 3 | R V R V R V | relative_haeufigkeit, saeulendiagramm, irrefuehrend | Brücke Anteil ↔ Prozent; Achse/Maßstab; Irreführung |
| 3 | `daten.kennwerte` (14) | M6 3 | V R V | mittelwert, mittel_rueckwaerts | Wirkung eines geänderten Werts; Umkehren |
| 3 | `funktionen.grundbegriffe` (16) | M8 1 | R V R V R V R V V | mengen, stelle, graph_lesen, punkt_graph, sachzusammenhang | W begründen, Umkehren, Graph ↔ Term, Prüfen durch Einsetzen, Modell aufstellen |
| 3 | `geometrie.winkel` (49) | M5 2 | R V R V R V V | kreuzung, uhr, figuren, verstehen | Scheitel-/Nebenwinkel begründen, Uhrzeit rückwärts, Fehler-Detektiv |

Zusammen 65 von 120 Lernzielen. Runde 1a/1b = die sieben Einheiten, an denen gerade gearbeitet wird (zuerst schreiben).

## 3. Wie viele Aufgaben je Verstehens-Lernziel

| Pool | Anzahl | Stufe | warum (Auswahl-Logik, siehe `plan.md`) |
|---|---|---|---|
| `test` | **genau 1** (`ersetzt_test: true`) | 2–3 | ersetzt die bisherige Test-Aufgabe; der Flugtest zieht ALLE freigegebenen Test-Aufgaben → genau eine je Lernziel |
| `korrektur` | **2, empfohlen 3** | 2 | „Verbessern“ zieht je Versuch die erste ungesehene Korrektur-Aufgabe; mit 2 sind die ersten zwei Verbesserungs-Versuche Verstehen, mit 3 auch noch einer nach einem späteren Nachtest-Fehler |
| `sicherung` | **3** | 2 und 3 gemischt | Nachtest Runden 1–3 mit je einer Aufgabe je Etappe; danach (oder bei kleinen Einheiten mit 2 je Etappe) kommt wieder Rechen-Bestand |

Das Werkzeug nimmt Korrektur 2–4 und Sicherung 3–5 an. Bitte die 6 bzw. 7 Aufgaben eines Lernziels **verschieden bauen** (andere Bauart, andere Einkleidung, andere Zahlen), nicht dieselbe Aufgabe mit neuen Zahlen.

## 4. Bauarten: erlaubt und verboten

Antworttypen in Stufe 1: **nur `zahl`, `luecken` (ganze Zahlen), `auswahl` (mindestens 4 Möglichkeiten)**. `typ` (Pflicht, Datenbank-Typ): umkehr, rueckwaerts, begruenden, fehler, darstellung, parameter, transfer, verknuepfen, mehrschritt, einkleidung, pruefung – **nicht** `direkt`, `erkennen`, `knobel`. Verstehen muss erkennbar sein: `typ` ist einer von umkehr/rueckwaerts/begruenden/fehler/darstellung/parameter/transfer **oder** `form` ist fehler_detektiv/verfahren_waehlen/zwei_wege/bruecke/umkehren (anwenden nur zusammen mit `typ: transfer`).

| Bauart | im Test | gutes Beispiel | schlechtes Beispiel (verboten/zu schwach) |
|---|---|---|---|
| Umkehren (`umkehren`, typ umkehr/rueckwaerts) | ja | „Ein Trapez mit a = 11 cm und c = 5 cm hat 40 cm² Flächeninhalt. Wie hoch ist es?“ (zahl 5) | „Berechne den Flächeninhalt …“ (das ist Rechnen in Vorwärtsrichtung) |
| Fehler-Detektiv (`fehler_detektiv`, typ fehler) | ja, NUR als **luecken** „Fehler in Zeile □, richtig ist □“ (mindestens 3 Zeilen) oder **auswahl** mit mindestens 4 Zeilen im Text und mindestens 4 Möglichkeiten, die JEDE eine Zeile **und** eine Begründung nennen („In Zeile 2, weil …“) | „Zeile 1: 2⁵ = 2 · 5 · Zeile 2: 2 · 5 = 10 · Zeile 3: Also 2⁵ = 10. Fehler in Zeile □, richtig: 2⁵ = □“ → [1, 32] | „In welcher Zeile steckt der Fehler? (Zeile 1 / 2 / 3)“ – 33 % Ratechance; ebenso nur „Was ist das richtige Ergebnis?“ als Zahl (prüft nicht, ob der Fehler gefunden wurde) |
| Begründung wählen (typ begruenden) | ja, mindestens 4 Möglichkeiten, Ablenker = echte Fehlvorstellungen | „Welche Aussage über 2³ und 3² stimmt? … 3² ist größer, denn 3² = 9 und 2³ = 8 / 2³ ist größer, denn der Exponent ist größer / beide gleich, denn dieselben Zahlen / 2³ ist größer, denn 8 > 9“ | „Stimmt die Aussage? ja / nein“ (50 %) |
| Verfahren wählen (`verfahren_waehlen`) | ja, als Auswahl ≥ 4 oder mit Ausführung gekoppelt (luecken „Weg □, Ergebnis □“) | „Welcher Ansatz löst 9/(x − 8) = 3/(x − 5) ohne Scheinlösung? (4 Ansätze)“ | „Welche Rechenart brauchst du? + / − / ·“ |
| Zwei Wege (`zwei_wege`) | ja, nur echte zwei Zugänge | „Anna zerlegt die Figur, Ben ergänzt sie zum Rechteck. Welchen Wert muss Ben abziehen?“ | zweimal dieselbe Rechnung in anderer Reihenfolge |
| Brücke (`bruecke`) | ja (zahl/luecken oder Auswahl ≥ 4) | „Ein Anteil ist 3/8. Wie viel Prozent sind das? (auf Zehntel gerundet)“ mit `runden: 1` | Tabelle abschreiben |
| Parameter/Was-wäre-wenn (typ parameter) | ja | „Grundseite und Höhe eines Dreiecks werden verdoppelt. Das Wievielfache ist der neue Flächeninhalt?“ | „Setze g = 4 ein.“ |
| Transfer (`anwenden` + typ transfer) | ja | Sachaufgabe, für die das Modell selbst aufgestellt werden muss | Sachaufgabe, die nur eine Formel einsetzt (= Rechnen) |
| Lückenweg | **nein** | – | jedes Gerüst mit vorgegebenen Schritten |
| viele_antworten (`bedingung`), `markierung`, `text` | **nicht in Stufe 1** | – | (Bewertung/Korrektur im Test noch nicht abgesichert) |

## 5. Qualität

- **Eigene Aufgaben.** Nichts wörtlich aus Schulbüchern, Prüfungen oder dem Netz. Neutrale Vornamen, keine Namen echter Personen aus dem Projekt.
- **Eindeutig:** genau eine richtige Antwort; Definitionsmenge, Einheit, Vorzeichen, Grenzen („einschließlich“), Zahl der Lösungen ausdrücklich im Text. Bei Auswahl: genau eine Möglichkeit richtig, alle verschieden.
- **Rundung ohne Toleranz:** keine `toleranz`. Verlangt die Aufgabe Runden, steht die Vorschrift im Text („auf Zehntel gerundet“) und das Feld `runden` (Nachkommastellen) im Eintrag; die Lösung hat genau so viele Stellen.
- **Nachrechenbar:** Die Lösung steht als Ausdruck in `loesung_rechnung` (oder im Rechenanker `aufgabe.c`): zahl ein Ausdruck, luecken je Lücke einer. Erlaubt: Ziffern, `+ − · : * /`, Klammern, `²`, `³`, `**`, `abs()`, Komma als Dezimalzeichen. Das Werkzeug rechnet jeden Ausdruck exakt (Brüche) nach.
- **Fehlbilder = ausführbare Fehlrechnungen** (Runde 15: Erklärtexte mussten dreimal nachgebessert werden): zahl/luecken mindestens 2 Fehlbilder, jedes mit `antwort`, `rechnung` (ergibt genau die `antwort`) und `beschreibung`, die genau diese Rechnung in Worten nennt. Bei auswahl zu **jeder** falschen Möglichkeit ein Fehlbild (`index`, `antwort` = Text der Möglichkeit, `beschreibung`; ist die Möglichkeit eine Zahl, auch `rechnung`). Kein Fehlbild gleich der Lösung, keine zwei gleichen Fehlantworten.
- **Lehrplan:** `lehrplan` beginnt mit dem Lernbereich der Einheit (Spalte oben, z. B. „M5 3“ oder genauer „M5 3.2“). Nichts aus späteren Klassen; Unsicherheit in `abgrenzung` oder in eurer `auswahl.md` ehrlich vermerken.
- **Abgrenzung zur Übung:** keine Aufgabe, die einer Aufgabe derselben Etappe im Bestand gleicht (Übungen in `inhalte/themen/<einheit>.json` und `inhalte/mathe-profi/rollend-*/`, auch die alten Test-/Korrektur-/Sicherungs-Aufgaben) oder einer der anderen neuen Aufgaben des Lernziels. Das Werkzeug prüft einfach und streng: gleicher Text; dieselben Zahlen (ab 3 Zahlen); Wörter zu ≥ 75 % gleich; Wörter ≥ 50 % gleich **und** ≥ 80 % der Zahlen gemeinsam. Empfohlen: ein Satz im Feld `abgrenzung`, was die Aufgabe anders macht als die Übungen.
- **Lösungsweg** (`aufgabe.w`) vollständig, in der Sprache der Klassenstufe (wird nach dem Test gezeigt). Tipps (`h`) sind erlaubt, werden im Test aber nicht gezeigt.

## 6. Dateiformat

Je Einheit eine Datei `<einheit>.json` im Ordner der Runde (z. B. `inhalte/mathe-profi/vtest-1a/zahlen.potenzen_basis.json`), Kopf wie `rollend-15`, Einträge unter `aufgaben`. Kennungen `<KÜRZEL>-nnn`, Kürzel je Runde: 1a = `VT1A`, 1b = `VT1B`, 2 = `VT2`, 3 = `VT3`. Vollständiges Beispiel (eine Test-Aufgabe, Fehler-Detektiv mit Kopplung):

```json
{
 "stand": "2026-11-28", "runde": "vtest-1a", "kuerzel": "VT1A", "titel": "zahlen.potenzen_basis", "klasse": 5,
 "themen": ["zahlen.potenzen_basis"], "hinweis": "Verstehen in Tests, Stufe 1. Nicht eingespielt.",
 "aufgaben": [
  {
   "kennung": "VT1A-001",
   "thema": "zahlen.potenzen_basis",
   "lernkarte": "berechnen",
   "pool": "test",
   "ersetzt_test": true,
   "typ": "fehler",
   "form": "fehler_detektiv",
   "stufe": 3,
   "zaehlt": "ja",
   "lehrplan": "M5 3",
   "regel": "rr.potenz",
   "abgrenzung": "Die Übungen rechnen Potenzen aus; hier muss der Denkfehler „Basis mal Exponent“ gefunden und berichtigt werden.",
   "antwortform": "luecken",
   "loesung_rechnung": ["1", "2 · 2 · 2 · 2 · 2"],
   "fehlbilder": [
    {"luecke": 2, "antwort": 10, "rechnung": "2 · 5", "beschreibung": "wie Mia Basis mal Exponent gerechnet: 2 · 5 = 10", "fehlbild": null, "regel_des_fehlbilds": null},
    {"luecke": 2, "antwort": 25, "rechnung": "5 · 5", "beschreibung": "Basis und Exponent vertauscht: 5² = 5 · 5 = 25", "fehlbild": null, "regel_des_fehlbilds": null}
   ],
   "aufgabe": {
    "l": "berechnen", "t": "berechnen", "p": "test", "s": 3, "g": "fehler", "y": "luecken",
    "f": {"text": "Mia rechnet 2⁵ so. Zeile 1: 2⁵ = 2 · 5 Zeile 2: 2 · 5 = 10 Zeile 3: Also ist 2⁵ = 10. In welcher Zeile steckt der erste Fehler, und welchen Wert hat 2⁵ wirklich?",
          "schablone": "Fehler in Zeile □, richtig: 2⁵ = □", "hinweis": "Je Feld eine ganze Zahl."},
    "o": {"werte": [1, 32]},
    "w": "Schon Zeile 1 ist falsch: 2⁵ heißt 2 · 2 · 2 · 2 · 2 (fünfmal die 2), nicht 2 · 5. Richtig ist 2⁵ = 32."
   }
  }
 ]
}
```

Pflichtfelder je Eintrag: `kennung`, `thema`, `lernkarte`, `pool`, `typ`, `stufe`, `zaehlt` („ja“), `lehrplan`, `fehlbilder` (mit `rechnung`), `aufgabe` mit `l` (= lernkarte), `t` (Teilfähigkeit aus `tf` der Einheit oder die der alten Test-Aufgabe), `p` (= pool), `s` (= stufe), `y`, `f`, `o`, `w`; `a` nur bei auswahl; `aufgabe.g` darf fehlen (sonst = `typ`); `ersetzt_test: true` genau bei der Test-Aufgabe. Optional: `form`, `regel` (Kennung `rr.…`/`id.…`, möglichst aus `inhalte/mathe-profi/regeln-uebersicht/kennungen.json`), `runden`, `abgrenzung`. Sechs geprüfte Muster in allen drei Pools und Antworttypen: `tools/tests/vtest_muster/runde/muster.potenzen.json`.

## 7. Ablauf einer Runde

1. `auswahl.md` (welche Lernziele, je ein Satz Begründung) – zuerst committen.
2. Aufgaben schreiben (Bauskript wie `rollend-15/bauen.py`, das die JSON-Dateien erzeugt).
3. `python3 -I tools/vtest_pruefen.py --runde <R>` → `OK`. Jeder HINWEIS: entweder beheben oder in der README begründen.
4. README der Runde: Zahlen je Einheit und Pool, Stufen, Bauarten, offene Zweifel.
5. Gegenprüfung durch einen zweiten Schreiber (Nachrechnen, Eindeutigkeit, Schulaufgaben-Niveau).
6. Einspielen macht der Projektleiter mit `tools/vtest_sql.py` nach `plan.md` (nicht ihr).

## 8. Was ihr NICHT tut

Keine Aufgaben für Rechen-Lernziele; keine Änderung an bestehenden Aufgaben, Themen-Dateien, App-Code oder Datenbank; nichts einspielen; keine Lerndaten oder Namen ins Repo.

## 9. Abweichungen gegenüber dem Auftrag vom 28.11. (bitte nachziehen)

| Punkt | Auftrag 28.11. | Werkzeug verlangt | Grund |
|---|---|---|---|
| Fehlbild-Rechnung | „ausführbare Rechnung im Bauskript“ | zusätzlich **in der JSON**: Feld `rechnung` je Fehlbild, Lösung in `loesung_rechnung` oder `aufgabe.c` | unabhängige Nachprüfung ohne euer Skript |
| Fehler-Detektiv | Zeile nennen und Ergebnis angeben „(Lücken/Zahl)“; Auswahl aus ≥ 4 Aussagen „Fehler ist … und richtig wäre …“ | **nur** luecken „Zeile □ … richtig □“ (≥ 3 Zeilen „Zeile n: …“) oder Auswahl mit ≥ 4 Zeilen im Text, jede Möglichkeit mit „Zeile n“ und „weil/denn/da“; **keine reine Zahl** | eine Zahl allein zeigt nicht, dass der Fehler gefunden wurde |
| viele_antworten (`bedingung`) | als Form erlaubt | in Stufe 1 **nicht** (ebenso `markierung`, `text`) | Bewertung/Korrektur dieser Typen im Test nicht abgesichert |
| Korrektur-Menge | 2 je Lernziel | 2 angenommen, **3 empfohlen** | siehe Abschnitt 3 und `plan.md` |
| `aufgabe.p`, `aufgabe.s`, `aufgabe.l` | – | müssen `pool`, `stufe`, `lernkarte` gleichen | eine Quelle für das Einspielen |
| Lehrplan | „z. B. M5 1.2“ | Anfang = Lernbereich der Einheit laut `inhalte/themenliste.json` (Tabelle oben) | maschinell prüfbar |
| Auswahl | in `auswahl.md` | dazu wertet das Werkzeug die Lernziele mit Aufgaben aus (Hälfte = Fehler, nicht abwechselnd = Hinweis) | – |
