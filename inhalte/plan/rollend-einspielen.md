# Vorrats-Aufgaben einspielen (rollend-1, rollend-2) – Vorbereitung, nichts eingespielt

Stand 27.11.2026. Werkzeug: `tools/rollend_sql.py` (ohne Schalter: Übersicht und Prüfung; `--sql`: ein selbstprüfendes SQL).

## Befund
- **142 Aufgaben in den alten Antwortformen** verteilen sich auf **14 bestehende, freigegebene Einheiten** (zehn Flüge; drei Flüge bestehen aus zwei oder drei Einheiten). Zuordnung über das Lernziel: `inhalte/plan/rollend-einheiten.json` (aus der Datenbank gelesen, nur Aufbau).
- Jedes Lernziel und jede Teilfähigkeit gibt es in der Ziel-Einheit. Keine Frage doppelt. Jede Aufgabe hat Tipp und Lösungsweg.
- In keiner der 14 Einheiten haben Kind 1 oder Kind 2 bisher einen Versuch. Das Einfügen ändert also keinen laufenden Lernstand.
- Neue Aufgaben kommen als **freigegeben** hinein (Vorgabe der Tabelle; eine freigegebene Einheit lässt nachträgliches Ändern nicht zu). Deshalb: erst Gegenprüfung der Inhalte, dann einspielen.
- 50 Aufgaben des Typs `bedingung` bleiben liegen, bis die App-Seite live ist.

## Die 12 Aufgaben mit Zeichnung (Sichtseite `tests/sicht-rollend-zeichnungen.html`, 420 px breit angesehen)
Alle zwölf werden gezeichnet; die Rechnungen habe ich an den Bildern nachvollzogen. Auffällig:
- **D1-14 (Kreisdiagramm):** Die Legende ist rechts abgeschnitten („Fangen (35“). Am echten Gerät prüfen; notfalls kürzere Beschriftung.
- **Tabellen (D1-05, D1-13, F1-05, G2T2-06, G2T2-07, G8-07):** In der Sichtseite stehen die Zeilen sehr eng. Unklar, ob das an der Sichtseite liegt oder echt ist – am Gerät prüfen.
- **F1-07, F1-15:** Achsenzahlen liegen teils auf dem Graphen bzw. dem Kreis. Lesbar, nicht schön.

## Offen vor dem Einspielen
1. Gegenprüfung der Inhalte durch ChatGPT (fachlich, Sprache, Schwierigkeit).
2. Entscheidung zu D1-14 und den Tabellen nach Blick am Gerät (Testkind).
3. Satz des Nutzers. Das SQL ist rund 70 KB groß; es wird je Einheit einzeln ausgeführt.
4. **Pflicht (Auftrag des Nutzers vom 27.11.):** neue Formen bevorzugt ziehen – siehe `aufgabentypen-auswahl.md`, Abschnitt „Neue Aufgabenformen bevorzugt ziehen“. Bisher offen und nicht nachgesehen: wie die App aus dem Vorrat einer Lernkarte auswählt (ob neue Formen bevorzugt werden oder nur zufällig dazukommen).
