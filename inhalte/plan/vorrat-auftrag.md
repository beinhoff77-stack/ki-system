# Auftrag „Vorrat neue Formen“ (für Helfer „Aufgaben“)

Projekt Lern-App (Mathe). Du schreibst Übungsaufgaben in NEUEN FORMEN für Themen, die noch keine haben.

## Harte Regeln
- Arbeite NUR in deinem Git-Worktree (im Auftrag genannt). Keine Datenbank-, Council- oder Konten-Werkzeuge. Kein App-Code (`lernen.js`, `style.css`, `app.js`, `sw.js`, `lernen/`), keine Migrationen ändern. `tools/rollend_sql.py` und `inhalte/plan/rollend-einheiten.json` NICHT ändern (ein anderer Helfer arbeitet daran).
- Du schreibst nur in deinen neuen Ordner `inhalte/mathe-profi/<runde>/`.
- Repo ist öffentlich: keine Namen von Kindern/Familie; in Sachaufgaben NICHT die Vornamen „Leo“ oder „Rosa“. Keine Schulbuch- oder Prüfungsaufgaben wörtlich, nichts wörtlich aus dem Bestand.
- Einfaches Deutsch, kurze Sätze, altersgerecht für die genannte Klasse (bayerischer Lehrplan Realschule/Gymnasium).
- Nur deinen eigenen Zweig pushen. Commit-Meldungen enden mit:
Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01RWRKSArQNYwC5Aun9rPxAd

## Zuerst lesen
- `inhalte/plan/form-takt.md` (Regeln 1 bis 6: Formen, `zaehlt`, Takt, Sachaufgaben-Pflicht)
- `inhalte/mathe-profi/rollend-4/README.md`, `inhalte/mathe-profi/rollend-4/bauen.py` und zwei JSON-Dateien dort als Muster für Format, Felder und Prüfung
- `inhalte/mathe-profi/rollend-2/verhaeltnis.md` (warum die Form zählt)
- `inhalte/plan/rollend-einspielen.md`
- Zu jedem deiner Themen den Bestand: suche den Themen-Schlüssel unter `inhalte/` und `supabase/migrations/` (Themen-Dateien mit Etappen, Lernzielen und vorhandenen Aufgaben), damit Niveau, Schreibweise, Antwortformen und Lernkarten-Schlüssel passen.

## Was zu liefern ist
- Je Lernkarte (Schlüssel im Auftrag je Thema genannt) GENAU DREI Aufgaben in neuer Form. Antworttypen nur die im Bestand üblichen (zahl, auswahl, text/term wie in rollend-4), keine neuen Bauteile, keine Zeichnungen, die es als Bauteil noch nicht gibt.
- Mischung je Lernkarte – das ist die Lehre aus rollend-4 (dort zu einseitig):
  - höchstens EINE `lueckenweg` (Stufe 1, `zaehlt = nein`: Weg vorgegeben, Kind füllt Lücken),
  - mindestens EINE Aufgabe mit `zaehlt = ja` aus: `umkehren`, `zwei_wege`, `bruecke`, `verfahren_waehlen`, `anwenden`,
  - `fehler_detektiv` höchstens eine je Lernkarte (`zaehlt = ja`).
  - Über das ganze Thema: jede der Formen `umkehren`, `zwei_wege`, `bruecke`, `anwenden` kommt mindestens zweimal vor, wo sie fachlich passt.
  - Für Lernkarten ohne eigene Sachaufgaben im Bestand bevorzugt eine `anwenden`-Aufgabe (echte Sachsituation, plausibel, Einheiten stimmen).
- JEDE Aufgabe trägt zusätzlich das Feld `thema` (Themen-Schlüssel, z. B. `bruch.brueche`) neben der Lernkarte, damit die Zuordnung eindeutig ist. Themen mit `_teil2` sind eigene Einheiten: nimm für deren Lernkarten den Schlüssel mit `_teil2`.
- Eine JSON-Datei je Thema im Format von rollend-4, Kennungen fortlaufend und eindeutig mit dem im Auftrag genannten Kürzel (z. B. `K5A-V001`).
- Jede Aufgabe: Lösung nachgerechnet (bei Zahlen per Python im Bau-/Prüfskript, nicht im Kopf), bei `auswahl` genau eine richtige Antwort und Falschantworten aus typischen Fehlern, Hinweis (`h`) und Erklärung/Lösungsweg wie im Muster, bei `fehler_detektiv` ein echter typischer Fehler.
- `bauen.py` oder Prüfskript im Ordner (nach Muster rollend-4), das alle Dateien lädt, Pflichtfelder, Formen, `zaehlt`, Mischungsregeln je Lernkarte, eindeutige Kennungen und die nachgerechneten Lösungen prüft und mit „OK“ endet. Zusätzlich `python3 -I tools/inhalt_pruefen.py` so anwenden, wie die README von rollend-4 es beschreibt.
- `README.md` im Ordner (höchstens 60 Zeilen): Tabelle Thema / Lernkarten / Aufgaben / Formen-Verteilung / zaehlt-Verteilung, wie geprüft, Annahmen und offene Punkte getrennt von Gesichertem, Lernkarten, bei denen eine Form fachlich nicht passte.

## Gerüst-Aufgaben (Lückenweg) – Vorgabe des Nutzers vom 27.11.: nicht erratbar
Das Kind darf die richtige Antwort nicht sofort raten können. Für jede `lueckenweg`-Aufgabe gilt:
- Antwortform `luecken` (Zahlen eintragen). Keine Auswahl-Antwort für einen Lückenweg.
- Mindestens ZWEI, besser drei Lücken, an verschiedenen Schritten des Wegs.
- Mindestens eine Lücke sitzt an der ENTSCHEIDENDEN Stelle des Verfahrens (dort, wo der typische Fehler passiert: Vorzeichen, Umkehrrechnung, Reihenfolge, Einheit), nicht nur beim letzten Ausrechnen.
- Kein Lückenwert steht schon im Aufgabentext, in der Schablone oder im Hinweis, und keiner ergibt sich durch bloßes Abschreiben einer gegebenen Zahl.
- Spätere Lücken hängen von früheren ab (wer vorne rät, liegt hinten falsch); die Zahlen sind so gewählt, dass der typische Fehler zu einer anderen, ebenfalls glatten Zahl führt.
- Der Text erklärt den Schritt, nennt aber nicht das Zwischenergebnis.

## Arbeitsweise
Thema für Thema: schreiben, prüfen, committen und pushen (nach jedem Thema, damit nichts verloren geht). Qualität vor Menge: lieber eine Lernkarte als „zurückgestellt“ melden als eine schwache Aufgabe liefern.

## Abschlussbericht an den Projektleiter (höchstens 15 Zeilen)
Letzter Commit, Zahl Themen/Lernkarten/Aufgaben, Formen- und zaehlt-Verteilung, zurückgestellte Lernkarten, offene Punkte.
