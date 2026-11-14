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
| `p` | `uebung` · `test` · `korrektur` · `sicherung` |
| `s` | Stufe 1 leicht · 2 mittel · 3 schwer |
| `y` | Antworttyp, siehe unten |
| `f` | Frage: `{"text": "…"}` plus typabhängige Felder |
| `a` | nur bei `auswahl`: 3–4 Antworten |
| `o` | Lösung, typabhängig |
| `h` | Tipp (nur Übungen, Pflicht). Hilft beim Ansatz, verrät das Ergebnis nicht. |
| `w` | Lösungsweg mit den Zahlen dieser Aufgabe |
| `c` | Rechenausdruck zum Nachrechnen, z. B. `"(-7) + (4)"`. Pflicht bei `zahl`. Erlaubt: `+ - * / // % **`, Klammern, `abs min max round`. |

Antworttypen:

- `zahl`: `o = {"wert": 12}` oder `{"wert": 2.5, "einheit": "cm"}`. Kind tippt die Zahl (Komma als Dezimalzeichen). Nur Ergebnisse, die als endliche Dezimalzahl exakt sind. Brüche als Ergebnis → `luecken` oder `auswahl`.
- `auswahl`: `a = ["…","…","…"]`, `o = {"index": 1}`. Falsche Antworten aus **typischen Fehlern** ableiten, nicht zufällig. Position der richtigen Antwort mischen.
- `luecken`: `f = {"text": "…", "schablone": "□/□", "hinweis": "Wie eintragen"}`, `o = {"werte": [3, 4]}`. Nur ganze Zahlen. `c` als Liste von Ausdrücken.
- `text`: `o = {"text": "MMXXIV"}`. Nur für sehr kurze, eindeutige Antworten (Groß-/Kleinschreibung und Leerzeichen egal).
- `markierung`: `f.grafik = {"typ":"zahlenstrahl","start":0,"ende":160,"abschnitte":8,"beschriftet":"anfang_ende"}`, `o = {"index": 7}`, zusätzlich `"zahl": 140` zum Nachrechnen.

Schreibweise in Texten: Minus `−`, Mal `·`, Geteilt `:`, große Zahlen mit Leerzeichen (`20 000`), Dezimalkomma, negative Zahlen in Rechnungen geklammert `(−7)`.

### Wenn ein Thema Zeichnungen braucht

Die App kann bisher nur Zahlenstrahl und Stellenwerttafel zeichnen. Für Geometrie, Funktionsgraphen, Diagramme:

- Bauen, was **ohne Bild** fachlich sauber geht (Rechnen, Begriffe, in Worten beschriebene Figuren mit allen Maßen).
- Nichts erfinden, was ein Bild voraussetzt. Stattdessen in der Datei `"offen": ["Lernkarte X braucht Zeichnung: …"]` eintragen. Der Haupt-Chat baut die Zeichenfunktion nach.

### Qualitätsmaßstab (wird von ChatGPT geprüft)

- Deckt das Thema den `umfang` und `lehrplan_gym` aus `themenliste.json` ab – nicht mehr (Stoff höherer Klassen weglassen)?
- Stufe 1 = Grundform direkt nach der Erklärung; Stufe 2 = Standard; Stufe 3 = mehrschrittig, Sonderfälle, Sachaufgabe oder „Fehler finden“.
- Mindestens eine Lernkarte je Thema prüft **Verstehen** (begründen, Fehler finden, Aussage beurteilen) statt nur Rechnen.
- Sachaufgaben mit realistischen Zahlen; keine Namen realer Personen.
