# Themen-Bausatz (Werkstatt #150, Lernen Schule)

Mehrere Chats bauen parallel Mathe-Themen als **Dateien**. Kein Chat außer dem Haupt-Chat fasst Datenbank, Server oder App-Code an.

## Ablauf

1. Auftrag aus `inhalte/AUFTRAEGE.md` nehmen (ein Paket = eine Klassenstufe).
2. Eigenen Zweig von `lernen-app` anlegen: `inhalte-kl5`, `inhalte-kl6`, `inhalte-kl8`, `inhalte-kl9`.
3. Je Thema aus `inhalte/themenliste.json`:
   - Generator schreiben: `inhalte/generatoren/<thema_schluessel>.py` (Vorlage: `inhalte/vorlage_generator.py`).
   - Ausführen → `inhalte/themen/<thema_schluessel>.json`.
   - Prüfen: `python3 -I tools/inhalt_pruefen.py inhalte/themen/<thema_schluessel>.json` → muss **OK** sein, ohne „nicht nachgerechnet“-Hinweise bei Zahl-Aufgaben.
   - Commit + Push auf den eigenen Zweig. Ein Thema = ein Commit.
4. Fertig melden: Liste der Dateien + offene Punkte (z. B. „Thema X braucht Zeichnungen“).
5. Der Haupt-Chat spielt ein (`tools/inhalt_sql.py`), als **Entwurf**: sichtbar nur für das Testkind und für Eltern/Lehrer als „in Prüfung“. ChatGPT prüft je Thema Erklärungen und Schwierigkeit. Danach Freigabe.

## Verboten

- Datenbank, Edge Functions, `lernen.js`, `app.js`, `style.css`, Tests ändern. Merge nach `main`.
- Schulbuch- oder Internetaufgaben abschreiben. Alles selbst erzeugen.
- Lösungen von Hand eintippen. Jede Lösung berechnet das Generator-Programm.
- Namen der Kinder, Schlüssel, Tokens in Dateien oder Commits.

## Was ein Thema enthält

- **4–10 Lernkarten** (`inhalt.etappen`), jede = eine klar abgegrenzte Fähigkeit, in sinnvoller Lernreihenfolge, gruppiert in 2–4 **Bereiche** (`inhalt.abschnitte`).
- Je Lernkarte mindestens: **12 Übungen** (≥ 3 je Stufe leicht/mittel/schwer, mit Tipp), **1 Test**, **3 Korrektur**, **6 Sicherung** (Test/Korrektur/Sicherung ohne Tipp, Stufe 2). Mehr Übungen sind erwünscht (Ziel 18–24).
- Alle Aufgaben einer Lernkarte verschieden; keine Aufgabe gleich dem vorgerechneten Beispiel.

### Lernkarte (Erklärung wie im Mathe-Lernblatt)

```json
{"lernziel": "addieren", "titel": "Ganze Zahlen addieren",
 "regel": "Ein bis zwei Sätze. Wichtiges in ⟦Klammern⟧ wird hervorgehoben.",
 "schritte": ["Vorgerechnetes Beispiel, Schritt 1.", "Schritt 2 mit ⟦Ergebnis⟧."],
 "probe": "optional: kurze Probe",
 "fehler": "Der typische Fehler – konkret mit Zahlen, und warum er falsch ist.",
 "bild": {"typ": "zahlenstrahl", "start": 0, "ende": 100, "abschnitte": 10, "beschriftet": "anfang_ende"}}
```

- `lernziel`: nur a–z, 0–9, `_`. `titel` höchstens 40 Zeichen, als Fähigkeit oder Frage formuliert.
- Sprache: für das Kind der jeweiligen Klasse. Kurze Sätze, „du“, Fachbegriffe wie im LehrplanPLUS Bayern, beim ersten Auftreten erklärt.
- `fehler` ist Pflicht und wird im Reiter „Fehler“ gezeigt.
- `bild` ist optional; es gibt nur `zahlenstrahl` und `stellentafel` (`{"typ":"stellentafel","stellen":["T","H","Z","E"],"ziffern":[4,0,5,2],"markiert":0}`).

### Aufgabe

| Feld | Bedeutung |
|---|---|
| `l` | Lernziel (Lernkarte) |
| `t` | Teilfähigkeit (`inhalt.teilfaehigkeiten[].k`) |
| `p` | `uebung` · `test` · `korrektur` · `sicherung` · `bonus` (freiwillige Knobel-Bordkarte, siehe „Stufen und Aufgabentypen“) |
| `s` | Stufe 1 leicht · 2 mittel · 3 schwer – folgt aus dem Aufgabentyp `g` |
| `g` | Aufgabentyp („Gedanke“), siehe „Stufen und Aufgabentypen“. Freiwillig für alte Aufgaben, Pflicht für neue. |
| `y` | Antworttyp, siehe unten |
| `f` | Frage: `{"text": "…"}` plus typabhängige Felder |
| `a` | nur bei `auswahl`: 3–4 Antworten |
| `o` | Lösung, typabhängig |
| `h` | Tipp (nur Übungen, Pflicht). Hilft beim Ansatz, verrät das Ergebnis nicht. |
| `w` | Lösungsweg mit den Zahlen dieser Aufgabe |
| `c` | Rechenausdruck zum Nachrechnen, z. B. `"(-7) + (4)"`. Pflicht bei `zahl`. Erlaubt: `+ - * / // % **`, Klammern, `abs min max round`. |

Antworttypen:

- `zahl`: `o = {"wert": 12}` oder `{"wert": 2.5, "einheit": "cm"}`. Bei gerundeten Ergebnissen (π, Wurzeln, sin/cos) zusätzlich `"toleranz": 0.1` (bzw. eine Einheit der letzten verlangten Stelle). Kind tippt die Zahl (Komma als Dezimalzeichen). Nur Ergebnisse, die als endliche Dezimalzahl exakt sind. Brüche als Ergebnis → `luecken` oder `auswahl`.
- `auswahl`: `a = ["…","…","…"]`, `o = {"index": 1}`. Falsche Antworten aus **typischen Fehlern** ableiten, nicht zufällig. Position der richtigen Antwort mischen.
- `luecken`: `f = {"text": "…", "schablone": "…", "hinweis": "Wie eintragen"}`, `o = {"werte": [3, 4]}`. Nur ganze Zahlen. `c` als Liste von Ausdrücken. Zwei Arten:
  - **Term-Vorlage** (nur □, einzelne Kleinbuchstaben, `+ − · ( ) ² ³`), z. B. `□x² + □x + □`: Das Kind tippt den Term frei ein.
  - **Alles andere**, z. B. Bruch `□/□` (wird als Zähler über Nenner gezeigt), Zahlenpaar `x = □; y = □`, Punkt `S(□ | □)`: je Lücke ein Zahlenfeld.
- `text`: `o = {"text": "MMXXIV"}`. Nur für sehr kurze, eindeutige Antworten (Groß-/Kleinschreibung und Leerzeichen egal).
- `markierung`: `f.grafik = {"typ":"zahlenstrahl","start":0,"ende":160,"abschnitte":8,"beschriftet":"anfang_ende"}`, `o = {"index": 7}`, zusätzlich `"zahl": 140` zum Nachrechnen.

Schreibweise in Texten: Minus `−`, Mal `·`, Geteilt `:`, große Zahlen mit Leerzeichen (`20 000`), Dezimalkomma, negative Zahlen in Rechnungen geklammert `(−7)`.

### Stufen und Aufgabentypen (Bau-Auftrag F, 17.11.)

**Regel: Die Stufe folgt aus dem Typ, nicht aus der Größe der Zahlen.** Stufe 2 ist nicht „Stufe 1 mit größeren Zahlen“, Stufe 3 nicht „Stufe 2 mit mehr Schritten derselben Art“.
Jede Bordkarte bekommt im Feld `g` ihren Typ – den Gedanken, den sie verlangt:

| Stufe | `g` | Was die Aufgabe verlangt | Beispiel (Prozent, Klasse 7) |
|---|---|---|---|
| 1 | `direkt` | wie das Beispiel der Lernkarte, andere Zahlen | „Wie viel sind 20 % von 150 €?“ |
| 1 | `erkennen` | zuordnen, ablesen, benennen | „Welcher Anteil ist 25 %: ein Viertel, ein Drittel oder die Hälfte?“ |
| 2 | `mehrschritt` | zwei bis drei Rechenschritte | „Eine Jacke kostet 80 €, erst 10 % Rabatt, dann noch 5 € Gutschein. Was zahlst du?“ |
| 2 | `einkleidung` | Sachsituation, die direkt auf die Rechnung führt | „Von 24 Kindern fahren 6 mit dem Bus. Wie viel Prozent sind das?“ |
| 2 | `umkehr` | eine andere Größe ist gesucht als im Beispiel | „15 € sind 30 % des Preises. Wie teuer ist das Spiel?“ |
| 2 | `darstellung` | Wechsel zwischen Tabelle, Bild und Term | „Im Kreisdiagramm ist der Bus-Anteil ein Viertel. Wie viel Prozent?“ |
| 3 | `rueckwaerts` | vom Ergebnis über mehrere Schritte zur Ausgangsgröße | „Nach 20 % Rabatt und 19 % Mehrwertsteuer kostet ein Rad 476 €. Wie hoch war der Nettopreis?“ |
| 3 | `verknuepfen` | braucht früheren Stoff dazu | „Ein Rechteck wird 10 % länger und 10 % schmaler. Um wie viel Prozent ändert sich die Fläche?“ |
| 3 | `begruenden` | Aussage prüfen, Gegenbeispiel finden | „Stimmt: Erst +50 %, dann −50 % ergibt wieder den Anfangswert?“ |
| 3 | `fehler` | Fehler in einer Rechnung finden und deuten | „Lea rechnet: 30 % von 60 = 60 : 30 = 2. Was hat sie falsch gemacht?“ |
| 3 | `transfer` | ungewohnte Einkleidung, Modell selbst aufstellen | „Ein Glas ist zu 40 % voll. Nach 120 ml mehr ist es zu 70 % voll. Wie viel passt hinein?“ |
| 3 | `parameter` | Variable statt Zahl („für welche a …“) | „Für welches a sind a % von 200 genauso viel wie 40 % von 50?“ |
| 3 | `pruefung` | Aufbau wie eine echte Prüfungs- oder Schulaufgabe (Typ nachbauen, nie Wortlaut) | mehrteilige Sachaufgabe wie in einer Jahrgangsstufentest-Aufgabe |
| Bonus | `knobel` | Wettbewerbsniveau, mehrere Ideen nötig (Vorbild: Art der Känguru- oder Olympiade-Aufgaben) | „Eine Zahl wird um 20 % erhöht und das Ergebnis um 20 % gesenkt. Danach ist sie 4 kleiner. Welche Zahl war es?“ |

Regeln (prüft `tools/inhalt_pruefen.py` für Aufgaben mit `g`):

- Unbekannter Typ oder Typ, der nicht zur Stufe `s` passt, ist ein **Fehler**.
- Haben **alle** Übungen einer Lernkarte ein `g`: mindestens 2 verschiedene Typen auf Stufe 1, 3 auf Stufe 2, 4 auf Stufe 3; höchstens 2 Aufgaben desselben Typs je Stufe mit gleichem Satzbau
  (Fragetext nach Ersetzen aller Zahlen identisch) – sonst **Fehler**.
- **Hinweis** für alle Lernkarten: Zahl der Übungen je Stufe mit/ohne `g` und „gleich gebaut hintereinander“ (3 oder mehr Übungen in Folge mit demselben Fragetext nach Ersetzen der Zahlen).
  Am Ende jeder Datei steht die Zahl dieser Gruppen; Ziel ist 0. Innerhalb einer Lernkarte nie zwei Aufgaben desselben Typs direkt hintereinander.

**Pool `bonus` (Knobel-Bordkarte):** freiwillig, zählt weder für „sitzt“ noch für den Test, kein Punktabzug. Je Lernkarte höchstens 3, nur Typ `knobel`, Stufe 3, mit Tipp `h`
(verrät die Idee nicht) und ausführlichem Lösungsweg `w`. Richtig im ersten Versuch: 30 Sterne und ein Knobel-Stern. Die Mengenregeln der anderen Pools bleiben.

### Lernregel „gelandet“ und „sicher“ (Werkstatt-Wunsch 176, ab App 0.76)

Für Inhalte wichtig, weil die Regel Aufgabentypen und schwere Bordkarten voraussetzt:

- **Gelandet** (intern `sitzt`): 6 eigene Lösungen (richtig im 1. Versuch ohne Tipp; bei weniger freien Übungen so viele wie da sind, mindestens 2), darunter mindestens **2 verschiedene Typen** `g`
  (wenn die Lernkarte mindestens 2 hat) und **1 Stufe-3-Aufgabe mit Stufe-3-Typ** (wenn vorhanden), und die **letzten 3 in Folge** richtig.
- **Keine Minuspunkte.** Ein endgültiger Fehler setzt nur „in Folge“ auf 0; eigene Lösungen bleiben. Tipp oder 2. Versuch richtig zählt nicht und unterbricht die Folge nicht.
- **Stufe:** steigt mit den eigenen Lösungen, fällt erst nach 2 Fehlern in Folge um 1. Deshalb braucht jede Lernkarte auf jeder Stufe mehrere Typen (siehe oben).
- **Sicher** (Anzeige): gelandet + Wiederholung nach 14 Lerntagen bestanden + Nachtest des Flugs bestanden (später zusätzlich: eine Mischkarte richtig).
- Knobel-Bordkarten (`bonus`) zählen nie.

### Wenn ein Thema Zeichnungen braucht

Die App kann bisher nur Zahlenstrahl und Stellenwerttafel zeichnen. Für Geometrie, Funktionsgraphen, Diagramme:

- Bauen, was **ohne Bild** fachlich sauber geht (Rechnen, Begriffe, in Worten beschriebene Figuren mit allen Maßen).
- Nichts erfinden, was ein Bild voraussetzt. Stattdessen in der Datei `"offen": ["Lernkarte X braucht Zeichnung: …"]` eintragen. Der Haupt-Chat baut die Zeichenfunktion nach.

### Qualitätsmaßstab (wird von ChatGPT geprüft)

- Deckt das Thema den `umfang` und `lehrplan_gym` aus `themenliste.json` ab – nicht mehr (Stoff höherer Klassen weglassen)?
- Stufe 1 = Grundform direkt nach der Erklärung; Stufe 2 = Standard; Stufe 3 = ein anderer Gedanke (Typen siehe „Stufen und Aufgabentypen“), nicht nur größere Zahlen.
- Mindestens eine Lernkarte je Thema prüft **Verstehen** (begründen, Fehler finden, Aussage beurteilen) statt nur Rechnen.
- Sachaufgaben mit realistischen Zahlen; keine Namen realer Personen.

## Vertiefung

`inhalt.bewertung` teilt die Lernkarten eines Themas auf: `lernziele_pflicht` (Grundstoff) und `lernziele_vertiefung` (Zusatzstoff, z. B. Vorgriff auf eine höhere Klasse).
Zusammen enthalten beide Listen jede Lernkarte genau einmal.

- Vertiefung heißt: nicht testrelevant und zählt nicht für den Stempel. Das Kind kann die Etappe trotzdem lernen und üben.
- In den Generatoren meist über den Parameter `vertiefung=(…)` gesetzt (Beispiel: geometrie.winkel, Lernkarte kreuzung).
- Wer eine Lernkarte zur Vertiefung macht, begründet das unter `offen` oder im Postfach; Aufgaben und Lernkarten-Texte bleiben dabei unverändert.

## Erfahrungen aus der ersten Runde (bitte beachten)

- **Brüche, Zahlenpaare, Punkte als Antwort**: als `luecken` mit Schablone `□/□`, `x = □; y = □`, `S(□ | □)` – die App zeigt je Lücke ein Zahlenfeld (negative ganze Zahlen sind erlaubt). Nicht mehr auf Auswahl ausweichen.
- **Gerundete Ergebnisse** (π, Wurzeln, sin/cos, Logarithmus): immer `"toleranz"` in `o` setzen (eine Einheit der letzten verlangten Stelle) und im Text sagen, auf wie viele Stellen gerundet wird.
- **Dubletten** werden über das ganze Thema geprüft, nicht nur je Lernkarte.
- `__pycache__` nicht einchecken (steht in `.gitignore`). Eigene Hilfsdatei mit eindeutigem Namen (`_kl7.py`), nie `_basis.py`.
- Stoff höherer Klassen weglassen, auch wenn er im Feld `umfang` steht; maßgeblich ist `lehrplan_gym`. Die Entscheidung unter `offen` notieren.
- Sachaufgaben auf Plausibilität lesen (realistische Mengen und Preise). Mindestens 10 Aufgaben je Lernkarte selbst durchlesen.

## Zeichnungen (neu, 14.11.)

Die App zeichnet jetzt selbst. Dasselbe Objekt geht als `bild` in einer Lernkarte **und** als `f.grafik` in einer Aufgabe (jeder Antworttyp außer `markierung`, der beim Zahlenstrahl bleibt). Koordinaten sind mathematisch (y nach oben).

- **Koordinatensystem** `{"typ": "koordinaten", "x": [-4, 4], "y": [-3, 5], "graphen": [...], "punkte": [{"x": 1, "y": 3, "name": "P"}], "strecken": [[0, 1, 1, 1, "gestrichelt"]], "senkrecht": [-1], "waagrecht": [1]}`
  - Graphen: `{"art": "linear", "m": 2, "t": 1}` · `{"art": "poly", "k": [c0, c1, c2, …]}` · `{"art": "hyperbel", "a": 2, "b": 1, "c": 1}` (a/(x+b)+c) · `{"art": "potenz", "a": 1, "n": 3}` · `{"art": "wurzel"}` · `{"art": "sin"|"cos", "a", "b", "c", "d"}` (x in Grad; mit `"bogen": true` im Bogenmaß) · `{"art": "exp", "a": 1, "b": 2}` · `{"art": "log", "b": 10}`. Optional je Graph `"name": "g"`, `"bereich": [x0, x1]`.
  - Optional: `"schritt_x"`, `"schritt_y"`, `"grad": true` (x-Achse in °), `"name_x"`, `"name_y"`, `"streckung"`, Punkte mit `"offen": true` (hohler Punkt).
- **Neu seit 16.11. (für die Bildergeschichte, auch als `f.grafik` in Aufgaben):**
  - Zahlenstrahl mit Zusätzen: `{"typ": "zahlenstrahl", "start": -10, "ende": 10, "abschnitte": 20, "punkte": [{"wert": -7, "name": "Taucher"}], "boegen": [{"von": -7, "bis": 0, "name": "7"}], "bereich": {"von": -3, "bis": 3}, "beschriftet": "alle"}`
    – Punkte mit Namen, Sprünge als Bogen mit Pfeil (von → bis), schattierter Bereich. Anfang, Ende, die 0 und die Werte der Punkte werden beschriftet, soweit Platz ist.
  - Thermometer: `{"typ": "thermometer", "start": -10, "ende": 30, "schritt": 10, "stand": -4, "bereich_unter_null": true, "einheit": "°C"}`
  - Bruchstreifen: `{"typ": "bruchstreifen", "teile": 4, "gefaerbt": 3, "ganzes": "20 €", "teil_text": "15 €", "zeilen": [{"teile": 8, "gefaerbt": 6}]}` (zeilen = weitere Streifen darunter, z. B. zum Erweitern)
  - Schrift in allen Zeichnungen ist jetzt mindestens 16 px groß. Beschriftungen kurz halten (Achsen- und Säulennamen möglichst ≤ 8 Zeichen); was nicht passt, lässt die App weg oder setzt es versetzt.
- **Koordinatensystem, Ergänzungen seit 15.11.:** Graph-Arten zusätzlich `tan` (wie sin/cos: a, b, c, d, bogen), `betrag` (a·|x − b| + c), `glocke` (a, mu, sigma);
  `"pi": true` beschriftet die x-Achse in Vielfachen von π (Bogenmaß, Standard-Schritt π/2); `"kreise": [{"m": [1, 2], "r": 3, "name": "k"}]` (ohne Graphen gleicher Maßstab → echter Kreis);
  `"pfeile": [[0, 0, 3, 2, "a"]]` Vektorpfeile mit Spitze; `"flaechen": [{"punkte": [[0, 0], [4, 0], [0, 3]]}]` gefüllter Bereich (z. B. zulässiger Bereich, Halbebene als Vieleck bis zum Rand).
- **Figur** `{"typ": "figur", "punkte": {"A": [0, 0], "B": [4, 0], "C": [4, 3]}, "flaeche": ["A", "B", "C"], "linien": [["A", "B", "c = 4 cm"], ["A", "C", "b = ?", "gestrichelt"]], "rechter_winkel": [["B", "A", "C"]], "winkel": [["A", "B", "C", "α"]], "kreise": [{"m": "M", "r": 3}]}`
  - Dreiecke, Vierecke, Strahlensatzfiguren, Thaleskreis, Kreis mit Radius/Sehne. Punkte, deren Name mit `_` beginnt, werden nicht beschriftet (Hilfspunkte). `rechter_winkel`/`winkel`: [Scheitel, Schenkelpunkt 1, Schenkelpunkt 2, Text].
  - Maßstab frei wählbar; die Figur wird eingepasst. Beschriftungen kurz halten.
- **Säulendiagramm** `{"typ": "saeulen", "einheit": "Kinder", "werte": [{"name": "Hund", "wert": 9}], "y_start": 0, "zahlen": true}` – `"zahlen": false` blendet die Werte aus (zum Ablesen), `"y_start"` > 0 zeigt eine abgeschnittene Achse (irreführende Diagramme).
- **Kreisdiagramm** `{"typ": "kreisdiagramm", "einheit": " %", "werte": [{"name": "Bus", "wert": 40}], "zahlen": true}`
- **Tabelle** `{"typ": "tabelle", "kopf": ["", "Brille", "keine Brille", "Summe"], "zeilen": [["Mädchen", "5", "9", "14"]]}` – für Vierfeldertafeln, Wertetabellen, Häufigkeitstabellen. Unbekanntes als „?“.

- **Boxplot** `{"typ": "boxplot", "achse": [0, 20], "einheit": "Punkte", "reihen": [{"name": "Klasse a", "min": 3, "q1": 8, "median": 11, "q3": 14, "max": 19}]}` – eine oder mehrere Reihen über derselben Achse.
- **Baumdiagramm** `{"typ": "baum", "aeste": [{"text": "rot", "p": "3/5", "aeste": [{"text": "rot", "p": "2/4"}, {"text": "blau", "p": "2/4"}]}, …]}` – bis zu drei Stufen, höchstens etwa 8 Blätter; `p` (Wahrscheinlichkeit am Ast) ist optional, „?“ für Gesuchtes.

Noch nicht möglich: Schrägbilder und Netze von Körpern, Flächen zum Färben, Zeichnen durch das Kind. Weiter unter `offen` notieren.

## Meldungen an den Haupt-Chat

Status, Fragen, Blocker und der Abschlussbericht gehören zusätzlich in `inhalte/postfach/<name-des-zweigs>.md` (Format und Regeln: `inhalte/postfach/README.md`). So muss niemand Berichte von Hand weiterreichen.


## Verständliche Erklärungen (Pflicht seit 15.11.)

Rückmeldung aus dem ersten echten Einsatz: Vater und Kind (Klasse 8) haben die erste Lernkarte nicht verstanden. Die Erklärung begann mit dem Fachsatz
(„Eine Funktion ordnet jedem x-Wert genau einen y-Wert zu“), benutzte Wörter und Schreibweisen ohne Erklärung („Zuordnung“, „(1 | 5)“) und sprang dann in eine Prüf-Frage.
Maßstab ab jetzt: **Ein Kind, das das Thema noch nie gesehen hat, und ein Elternteil ohne Mathe-Erinnerung verstehen die Karte beim ersten Lesen.**

Jede Lernkarte bekommt zusätzlich zwei Felder (Muster: inhalte/generatoren/funktionen.grundbegriffe.py, Abschnitt KLAR):

- `einstieg` (Text, 2–5 Sätze): eine Alltagssituation, in der die Idee ohne Fachwort vorkommt (Getränkeautomat, Taxi-Tarif, Wetter-App, Taschengeld, Rezept …).
  Erst die Situation, am Ende das neue Fachwort in ⟦…⟧. Kein „x“, keine Formel im ersten Satz. Eine Situation möglichst über mehrere Karten eines Themas weiterführen.
- `woerter` (Liste aus `[Wort, Erklärung]`): jedes Fachwort, jedes Zeichen und jede Schreibweise, die in dieser Karte zum ersten Mal vorkommt
  (auch scheinbar Selbstverständliches wie „x-Wert“, „f(x)“, „(1 | 5)“, „{0; 1; 3}“, „D“). Erklärung in Alltagssprache, höchstens eine Zeile, gern mit Bezug zur Situation.

Dazu gelten für die bestehenden Felder:
- `schritte`: ein Beispiel in kleinen Schritten, je Schritt ein Gedanke und ein ganzer Satz, der sagt, was man tut und warum („Auf beiden Seiten 4 dazuzählen: 3x = 15.“).
  Keine Schritte, die nur einen Term hinschreiben. 3–5 Schritte. Das Ergebnis in ⟦…⟧.
- `regel`: der Merksatz steht in der App jetzt am Ende („MERKE“). Kurz, mit den Wörtern aus `woerter`, als Handlungsanweisung („So prüfst du: …“).
- `bild`: Tabellen mit sprechender Beschriftung („x (Eingabe)“), nicht nur „x“ und „y“.
- `fehler`: den Fehler in der Alltagssituation deuten („wie eine Taste, die mal Cola und mal Wasser gibt“).
- Verboten in `einstieg` und `schritte`: Fachwörter, die nicht in `woerter` dieser oder einer früheren Karte desselben Themas stehen; Schachtelsätze; „offensichtlich“, „einfach“, „trivial“.

**Vorgabe seit 16.11.** (Sebastians Auswahl; Herleitung in inhalte/pruefung/erklaerungen/darstellung/umsetzung.md und bericht.md). Wo sie den Regeln weiter oben in diesem Abschnitt widerspricht (Längen, Zahl der Wörter und Schritte), gilt diese Vorgabe.

Die Anzeige (alle Klassen gleich): Übersicht (Titel + Merksatz als „Kurz gesagt“) → eine Karte:
WORUM GEHT’S? → Bild → Beispiel als Bildergeschichte (jeder Schritt mit Bild) → „Pass auf!“ (fehler + fehler_bild) → MERKE.
Neue Wörter werden im Text antippbar; die App macht das selbst aus `woerter`.

Längen und Form:
- einstieg ≤ 35 Wörter, 2–3 Sätze. Dieselbe Situation wie Bild und Beispiel.
- höchstens 3 neue Wörter je Karte; jedes muss im einstieg oder in den schritten vorkommen.
- schritte: 2–4 Schritte (höchstens 5), je ≤ 15 Wörter, je Schritt ein Gedanke. Jeder Schritt, in dem sich im Bild etwas ändert, hat ein eigenes `bild`.
- fehler ≤ 30 Wörter, in der Situation gedeutet; `fehler_bild`, wenn der Fehler sichtbar gemacht werden kann.
- regel ≤ 25 Wörter, der erste Satz taugt allein als „Kurz gesagt“ (≤ 12 Wörter).
- Sätze ≤ 15 Wörter (Kl. 5/6), ≤ 20 Wörter (Kl. 7–10).
- ⟦…⟧ nur für das Ergebnis eines Schritts und das Kernwort im Merksatz, höchstens 2 je Absatz.
- Brüche als a/b schreiben (die App stapelt sie), nicht als Unicode-Bruchzeichen.
- Jede Karte hat ein Kartenbild. Gibt es keine passende Zeichnungsart: in "offen" notieren, nicht erfinden.
Aufgaben werden beim Umbau nicht geändert (Texte wörtlich gleich, damit Fortschritt erhalten bleibt).

Schritte mit Bild (neues Format; reine Text-Schritte bleiben erlaubt):

```json
"bild": {"typ": "zahlenstrahl", "start": -10, "ende": 10, "abschnitte": 20, "beschriftet": "anfang_ende"},
"schritte": [
  {"text": "Der Taucher ist bei −7 m, der Vogel bei 7 m.", "bild": {"punkte": [{"wert": -7, "name": "Taucher"}, {"wert": 7, "name": "Vogel"}]}},
  {"text": "Von −7 bis 0 sind es 7 Schritte. Also ist ⟦|−7| = 7⟧.", "bild": {"boegen": [{"von": -7, "bis": 0, "name": "7"}]}},
  {"text": "Der Vogel ist genauso weit weg: |7| = 7."}
],
"fehler": "Den Betrag negativ schreiben: |−7| ist nicht −7. Ein Abstand ist nie kleiner als null.",
"fehler_bild": {"boegen": [{"von": -7, "bis": 0, "name": "7, nicht −7"}]}
```

- Das `bild` im Schritt ergänzt oder überschreibt Felder des Kartenbildes; ein anderes `typ` ersetzt das Bild ganz.
- Ein Schritt ohne `bild` zeigt den Bildzustand des vorigen Schritts (nur wenn die Karte überhaupt Schrittbilder hat). `fehler_bild` funktioniert genauso.
- Felder je Karte (Pflicht für neue und umgebaute Karten): `titel`, `einstieg`, `woerter`, `bild`, `schritte` (Objekte), `fehler`, `fehler_bild` (wenn sich der Fehler zeigen lässt), `regel`.
