# Postfach klar-kl5 (Siebte Runde: Erklärungen verständlich machen, Klasse 5)

Technik: je Generator ein Abschnitt KLAR; eingesetzt über `inhalte/generatoren/_klar_kl5.py` erst NACH dem Erzeugen der Aufgaben
(die Generatoren nutzen die alten `schritte` gegen Dopplungen – so bleiben alle Aufgaben wörtlich gleich, wie `_verbot` im Muster).
Vergleich je Thema: `aufgaben` und alle Felder außer `inhalt.etappen` gegen `git show HEAD:inhalte/themen/<thema>.json`.

## 2026-11-15 17:30 – FERTIG
Alle 11 Themen der Klasse 5 (gym_by = 5) mit vorhandener Datei überarbeitet, 80 Lernkarten. Je Karte: `einstieg` und `woerter` neu,
`schritte` (3–5 ganze Sätze, Ergebnis in ⟦…⟧), `regel` (Merksatz „So …“), wo nötig `fehler` in der Alltagssituation gedeutet.

| Thema | Karten | Aufgaben | Aufgaben wörtlich gleich (gegen 61e1dde) | inhalt_pruefen |
|---|---|---|---|---|
| zahlen.ganz | 8 | 224 | ja | OK |
| zahlen.rechengesetze | 10 | 250 | ja | OK |
| zahlen.potenzen_basis | 7 | 175 | ja | OK |
| groessen.einheiten | 8 | 224 | ja | OK |
| groessen.proportional | 7 | 175 | ja | OK |
| geometrie.grundbegriffe | 7 | 196 | ja | OK |
| geometrie.winkel | 7 | 196 | ja | OK |
| geometrie.ortslinien | 6 | 168 | ja | OK |
| messen.flaechen | 7 | 196 | ja | OK |
| messen.koerper_berechnung | 6 | 168 | ja | OK |
| stochastik.kombinatorik | 7 | 196 | ja | OK |

Vergleich: kleines Skript, `aufgaben` und alle Felder außer `inhalt.etappen` gegen `git show HEAD:…` – überall identisch.
Technik: `_klar_kl5.py` setzt KLAR erst nach dem Erzeugen der Aufgaben ein (alte Beispieltexte bleiben so für die Dubletten-Prüfung
der Generatoren wirksam) und prüft dabei: alle Karten abgedeckt, 3–5 Schritte, Fachwort in ⟦…⟧ im Einstieg, keine Wörter „einfach/offensichtlich/trivial“.

Inhaltliche Entscheidungen:
- geometrie.ortslinien/zwei_kreise: Merksatz fachlich ergänzt um den Fall „ein Kreis liegt ganz im anderen“ (Unterschied der Radien > [AB] → kein Punkt);
  der alte Satz („sonst meist zwei“) passte nicht zu Aufgaben wie r = 2, r = 9, [AB] = 6.
- geometrie.winkel/kreuzung: bewusst „benachbarte“ und „gegenüberliegende Winkel“ statt „Nebenwinkel/Scheitelwinkel“ (Begriffe erst Klasse 7).
- zahlen.rechengesetze/vorteil, verteilen: Fachwörter Kommutativ-, Assoziativ-, Distributivgesetz in `woerter` genannt (LehrplanPLUS 5), Alltagsnamen zuerst.
- Beispielrechnungen meist beibehalten; neu/geändert nur dort, wo die Situation es verlangte (ueberschlag: Kino 487 Plätze · 21 Abende = 10 227, nachgerechnet).
- Bild geändert nur bei Tabellen (sprechende Kopfzeilen, gleiche Werte): groessen.proportional pruefen/dreisatz, stochastik.kombinatorik systematisch.

Nicht bearbeitet: gleichungen.einfach (Klasse 5 laut themenliste.json) – Datei existiert weder hier noch auf lernen-app (Runde 5, Haupt-Chat).
Sobald sie da ist, braucht sie ebenfalls einen KLAR-Abschnitt.

## 2026-11-15 16:40 – STATUS
zahlen.rechengesetze (10 Karten), zahlen.potenzen_basis (7), groessen.einheiten (8), groessen.proportional (7) fertig.
inhalt_pruefen je OK. Vergleich: 250 / 175 / 224 / 175 Aufgaben wörtlich gleich, übrige Datei gleich.
Bildbeschriftung geändert nur bei Tabellen (groessen.proportional: pruefen, dreisatz – gleiche Werte, sprechende Kopfzeilen).

## 2026-11-15 16:10 – STATUS
zahlen.ganz (8 Karten) fertig: einstieg + woerter neu, schritte/regel/fehler überarbeitet (Situationen Thermometer, Taschengeld/Schulden).
inhalt_pruefen: OK. Vergleich: 224 Aufgaben wörtlich gleich, übrige Datei gleich.
