# Runde VT1A: Verstehens-Aufgaben für Tests, Klasse 5

Stand 29.11.2026 (nach Vorprüfung W1, 2. Durchgang; siehe `korrektur-nach-vorpruefung-w1-2.md`). Nichts davon ist eingespielt; es sind nur Inhalte in `inhalte/mathe-profi/vtest-1a/`.

**55 Aufgaben** in zwei Einheiten (11 von 21 Lernzielen: `zahlen.potenzen_basis` 4 von 7, `zahlen.rechengesetze` 7 von 14). Je Lernziel **1 Test-Aufgabe** (`ersetzt_test`), **2 Korrektur-** und **2 Sicherungs-Aufgaben** (Entscheidung des Nutzers; vorher 1/3/3). Kennungen `VT1A-001` bis `VT1A-055`.

## Dateien

| Datei | Inhalt |
|---|---|
| `zahlen.potenzen_basis.json`, `zahlen.rechengesetze.json` | die Aufgaben (Format wie `rollend-15`, dazu `pool`, `bauplan`, `schema`, `idee`, `alt_kennung`, `abgrenzung`, `loesung_rechnung`, `rechnung` je Fehlbild) |
| `kern.py`, `th_*.py` | Quelltexte (Hilfsfunktionen, Aufgaben je Einheit mit Bauplan, Schema-Urteil, Denkfigur, Bestandskern) |
| `bauen.py` | prüft alle Regeln (siehe unten), schreibt die JSON-Dateien, `regeln-zuordnung.md` und `bestandsvergleich.md`, ruft `tools/vorrat_pruefen.py` und `tools/vtest_pruefen.py --runde 1a` auf; endet mit „OK“ |
| `gegenrechnung.py` | rechnet alle 55 Sollantworten unabhängig neu (Auswahl mit Termen: jede Option ausgewertet); endet mit „0 Abweichungen“ |
| `bestandsvergleich.md` | je Aufgabe: Bauplan, Denkfigur, Schema ja/nein, frühere Kennung, nächstliegender Bestandskern, Unterschied; Tabelle je Lernziel |
| `korrektur-nach-vorpruefung-w1.md` | Befund → geschlossen wie (A1–A17, B1–B17, C1–C7), Zuordnung alt → neu |
| `vorrat-folgerunde/` | 47 gestrichene, aber brauchbare Aufgaben der Fassung mit 77 Aufgaben (`VT1A-ALT-nnn`, Grund je Eintrag); nicht Teil der Runde |
| `auswahl.md`, `regeln-zuordnung.md` | Auswahl der Lernziele; Regel-Kennung je Aufgabe |
| `vorpruefung*.md`, `korrektur-nach-vorpruefung.md`, `korrektur-nach-vorpruefung-2.md`, `korrektur-nach-gegenpruefung.md`, `sonderfaelle.md`, `vorpruefung_rechnen*.py` | frühere Stände (77 Aufgaben, alte Kennungen) |

Aufrufe vom Wurzelordner: `python3 -I inhalte/mathe-profi/vtest-1a/bauen.py`, `python3 -I inhalte/mathe-profi/vtest-1a/gegenrechnung.py`, `python3 -I tools/vtest_pruefen.py --runde 1a`.

## Maßstab und feste Prüfungen in `bauen.py`

- je Lernziel genau 1/2/2; Korrektur Stufe 2, Sicherung Stufe 2 und 3, Test Stufe 3
- höchstens eine Schema-Aufgabe je Lernziel, der Test ist keine; Schema = durch ein bekanntes Verfahren oder bloßes Ausrechnen lösbar, auch als Zahlenvergleich, Fehler-Detektiv oder Auswahl durch Ausrechnen der Optionen, im Zweifel ja (Urteil von Hand, Feld `schema`)
- mindestens 4 Denkfiguren (`idee`) je Lernziel, keine doppelt im selben Pool (erreicht: überall 5)
- Auswahl: genau eine richtige Option; jedes Urteil höchstens einmal je Aufgabe; kein Zwillings-Paar (gleicher Anfang aus 5 Wörtern oder nur ein Wort anders), das als einziges Paar die richtige Option enthält; kein Merkmal nur in der richtigen Option (=, ·, darf/muss/man, denn/weil, Nebensatz, Sammelwort, Absolutwort, Verneinung, kleiner/größer); Merkmale global gleich verteilt; Länge, Lage und Anfangswörter geprüft
- Fehlbilder: jede Zahl-Fehlantwort mit Rechnung, die genau sie ergibt; Zahlen der Beschreibung stammen aus Text oder Rechnung; zu jeder falschen Option eine Beschreibung der Fehlvorstellung
- Bestand: kein gleicher oder nur zahlenverschiedener Fragetext (maschinell); der Kernvergleich von Hand in `bestandsvergleich.md`

## Zahlen

| Einheit | Lernziel | zahl | auswahl | Baupläne (T K K S S) | Schema | Denkfiguren |
|---|---|---|---|---|---|---|
| zahlen.potenzen_basis | schreibweise | 1 | 4 | d d e f d | 1 (005) | 5 |
| zahlen.potenzen_basis | quadrat | 2 | 3 | c e d g f | 1 (009) | 5 |
| zahlen.potenzen_basis | zehner | 2 | 3 | g g e g f | 1 (014) | 5 |
| zahlen.potenzen_basis | sach | 3 | 2 | b c d e f | 1 (018) | 5 |
| zahlen.rechengesetze | klammern | 3 | 2 | e b h f e | 1 (023) | 5 |
| zahlen.rechengesetze | termaufbau | 0 | 5 | e d c b d | 1 (027) | 5 |
| zahlen.rechengesetze | vorteil | 3 | 2 | c g b f e | 1 (033) | 5 |
| zahlen.rechengesetze | verteilen | 2 | 3 | b e d b e | 1 (038) | 5 |
| zahlen.rechengesetze | umkehraufgabe_mal | 1 | 4 | c d d e f | 1 (043) | 5 |
| zahlen.rechengesetze | ueberschlag | 2 | 3 | g b a h g | 1 (048) | 5 |
| zahlen.rechengesetze | sach | 2 | 3 | h d c f h | 1 (055) | 5 |

Baupläne: a Begründung wählen, b Fehlvorstellung aufdecken, c Rückwärts mit Wahl, d Darstellungswechsel, e Was-wäre-wenn/Invarianz, f immer–manchmal–nie, g Vergleichen ohne Ausrechnen, h Modellwahl.
Gesamt: 34 Auswahl, 21 Zahl; Stufe 2: 33, Stufe 3: 22; 11 Schema-Aufgaben (je Lernziel genau eine, nie im Test; Zählung der Vorprüfung W1-2 übernommen).

## Ehrlich: Zweifel und Grenzen

1. **Pool-Meldung.** `tools/vtest_pruefen.py` verlangt 3 Sicherungs-Aufgaben und meldet je Lernziel „2 sicherung-Aufgaben, Soll 3“ (11 Fehlerzeilen). Das ist mit der Entscheidung 1/2/2 erwartet; `bauen.py` lässt genau diese Meldungen zu und bricht bei jeder anderen ab. Vor dem Einspielen muss `mengen.sicherung` in `vtest-1/auswahl.json` (oder das Werkzeug) angepasst werden – das habe ich nicht getan (nicht mein Ordner).
2. **Schema-Urteile sind von Hand;** maßgeblich ist die Zählung der Vorprüfung W1-2 (033 und 038 jetzt Schema). Grenzfälle, die ich weiter als „nein“ zähle: 025 (□ unbekannt, aber eine Zahl ausprobieren geht), 039 (□ = 1 lässt sich schnell probieren), 053 (systematisches Probieren), 046 (zwei Schranken ausrechnen).
3. **Typ-Etiketten.** Korrektur muss Stufe 2 sein; Fehlvorstellungs-Aufgaben (Bauplan b) in der Korrektur tragen deshalb `umkehr` (von den Ergebnissen zurück auf die Regel), Vergleiche `mehrschritt` mit `zwei_wege`. Der Bauplan steht im Feld `bauplan`.
4. **Kinderregel-Form** (B1) nur noch in 022, 029, 039, 047, jeweils anders gefragt (Unterschied zum richtigen Ergebnis, Regel wählen, Fall in dem die Regel zufällig stimmt, größte Abweichung); keine Zahlaufgabe hat mehr einen falschen Wert als Lösung. Fehlvorstellungs-Aufgaben ohne Kinderregel-Form: 016, 036.
5. **Regeln.** Bei `ueberschlag` keine Regel (kein Katalogeintrag); 5 Hinweise des Werkzeugs.
6. **Lehrplan.** „M5 3“ wie bisher; nur natürliche Zahlen; Variablen nur als x oder a in Gleichungen (M5 3.1) und als □/△ für Lücken.
