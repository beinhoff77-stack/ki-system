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

## Nachtrag 27.11.: zwei echte Darstellungsfehler gefunden und im Arbeitsstand behoben (nicht live)
- **Tabellen in Aufgaben:** Die Zeilenhöhe war 0 (`.lr-bild` setzt sie für Zeichnungen auf 0, die Tabelle erbte das). Zeilen lagen ineinander. **Der Fehler steckt auch in der Live-Fassung** (gleiche Stil-Regeln in `main`) und betrifft dort jede Aufgabe mit Tabelle. Behoben in `style.css` (`.lr-bild-tabelle` mit eigener Zeilenhöhe).
- **Kreisdiagramm:** Die Breite war fest, lange Beschriftungen wurden abgeschnitten. Jetzt richtet sich die Breite nach der längsten Beschriftung (`lernKreisdiagramm`).
- Nachher angesehen (Sichtseite, 420 px): Tabellen und Legende sind lesbar. Nicht geprüft: echtes Gerät, dunkle Ansicht.

## Inhaltsprüfung der Gegenprüfung (Werkstatt 1020, 27.11.)
- 142 Aufgaben einzeln geprüft, 156 Rechnungen nachgerechnet, keine Abweichung. Urteil je Datei: `ge1`, `ge2`, `a4` Ja; `f1` Ja mit Auflage (Tabelle); `z2`, `a1`, `d1`, `g1`, `g8`, `g2-teil2` erst nach Berichtigung.
- Inhaltliche Muss-Befunde: Z2-07, A1-04, G1-07, G8-01, G8-04, G1-12, G2T2-03 → Auftrag 20 an den Mathe-Profi (Postfach). Darstellung (Tabellen, Legende) im Arbeitsstand behoben.
- Verhältnis: Vorschlag 1 neue Form auf 2 Bestandsaufgaben je Lernkarte und Stufe, gemischt; „neu“ muss über ein eigenes Kennzeichen erkennbar sein. Technische Fragen (Werkstatt 1019, A–C) noch offen.

## Offen vor dem Einspielen
1. Gegenprüfung der Inhalte durch ChatGPT (fachlich, Sprache, Schwierigkeit).
2. Die beiden Darstellungs-Korrekturen müssen live sein, bevor die Aufgaben mit Tabelle oder Kreisdiagramm hineingehen (siehe Nachtrag).
3. Satz des Nutzers. Das SQL ist rund 70 KB groß; es wird je Einheit einzeln ausgeführt.
4. **Pflicht (Auftrag des Nutzers vom 27.11.):** neue Formen bevorzugt ziehen – siehe `aufgabentypen-auswahl.md`, Abschnitt „Neue Aufgabenformen bevorzugt ziehen“. Bisher offen und nicht nachgesehen: wie die App aus dem Vorrat einer Lernkarte auswählt (ob neue Formen bevorzugt werden oder nur zufällig dazukommen).
