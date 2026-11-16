# klar-kl9 – Erklärungen verständlich machen (Klasse 9)

Neueste Meldung oben.

## 2026-11-16 – FERTIG: Runde 7 Klasse 9 (Zweig klar-kl9, nicht gemergt)

| Thema | Lernkarten | Aufgaben | Unterschiede zu lernen-app | inhalt_pruefen |
|---|---|---|---|---|
| zahlen.wurzeln_basis | 6 | 168 | 0 | OK |
| zahlen.reell | 6 | 168 | 0 | OK |
| zahlen.rationale_exponenten | 6 | 168 | 0 | OK |
| gleichungen.quadratisch | 7 | 196 | 0 | OK |
| gleichungen.potenz | 6 | 168 | 0 | OK |
| gleichungen.lgs3 | 6 | 168 | 0 | OK |
| funktionen.quadratisch | 7 | 196 | 0 | OK |
| funktionen.potenz | 6 | 168 | 0 | OK |
| abbildungen.aehnlichkeit | 6 | 168 | 0 | OK |
| trigo.pythagoras | 6 | 168 | 0 | OK |
| trigo.rechtwinklig | 6 | 168 | 0 | OK |
| trigo.allgemein | 7 | 196 | 0 | OK |
| gleichungen.trig | 6 | 168 | 0 | OK |
| stochastik.verknuepft | 6 | 168 | 0 | OK |
| **Summe** | **87** | **2 436** | **0** | |

- Jede Karte hat jetzt `einstieg` (Alltagssituation, Fachbegriff am Ende in ⟦…⟧), `woerter`, 3–5 `schritte` (ganze Sätze, Ergebnis in ⟦…⟧), handlungsorientierte `regel` und einen `fehler` mit Bezug zur Situation. Bild-Beschriftungen sind sprechend (z. B. „Messpunkt (0 | 1)“, „Zaun a = 6 m“, „B (Los gespielt)“).
- Durchgehende Situationen je Thema, u. a.: Teppich/Würfel (Wurzeln), Bakterien (rationale Exponenten), Fliesen/Gemüsebeet (quadratische Gleichungen), Zahlenautomat (Potenzgleichungen, Potenzfunktionen), Kiosk (LGS), Skaterbahn/Springbrunnen (Parabeln), Schattenspiel (Ähnlichkeit), Garten/Leiter (Pythagoras), Rampe (Trigonometrie), Vermessung/Wanderung (Sinus-/Kosinussatz), Riesenrad (trigonometrische Gleichungen), Schulfest (Stochastik).
- Aufgaben unverändert: Vergleich jeder Aufgabe als JSON-Objekt gegen `origin/lernen-app`. Die alten Beispielschritte bleiben über `ALT_SCHRITTE` in `_kl9.py` für den Dopplungsabgleich maßgeblich.
- Prüfung auf verbotene Wörter („offensichtlich“, „einfach“, „trivial“) in einstieg und schritte: als Teilwort, also auch „vereinfachen“. Zweimal getroffen und umformuliert.
- Geänderte Dateien nur unter `inhalte/generatoren/`, `inhalte/themen/` und `inhalte/postfach/`. Nichts unter `inhalte/pruefung/`, kein App-Code, keine Datenbank.
- Annahmen: Wo die alte `probe` nicht mehr zur neuen Schrittfolge passte, steht in KLAR eine neue probe. Inhaltlich wurden keine Regeln geändert, nur erklärt und umformuliert. Alle Zahlen in den Situationen wurden nachgerechnet.
- Offene Frage: keine. Merge nach `main` erst nach „Live“.

## 2026-11-16 – STATUS
- Technik: `_kl9.py` hat jetzt `klar(ETAPPEN, KLAR)`. Die Funktion legt einstieg, woerter, schritte, regel, fehler (und wo nötig bild/probe) über die Lernkarten.
  Für den Dopplungsabgleich in `bauen()` bleiben die alten Beispielschritte maßgeblich (wie `_verbot` im Muster), damit sich keine Aufgabe ändert.
- Vergleich der Aufgaben gegen `lernen-app` (Skript: jede Aufgabe als JSON-Objekt verglichen):
  - zahlen.wurzeln_basis: 168 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - zahlen.reell: 168 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - zahlen.rationale_exponenten: 168 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - gleichungen.quadratisch: 196 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - gleichungen.potenz: 168 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - gleichungen.lgs3: 168 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - funktionen.quadratisch: 196 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - funktionen.potenz: 168 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - abbildungen.aehnlichkeit: 168 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - trigo.pythagoras: 168 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - trigo.rechtwinklig: 168 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - trigo.allgemein: 196 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - gleichungen.trig: 168 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
  - stochastik.verknuepft: 168 Aufgaben, 0 Unterschiede, inhalt_pruefen OK
