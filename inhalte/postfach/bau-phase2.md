# Postfach bau-phase2 (Bau-Chat App-Code, Phasen 2 und 3)

Neueste oben.

## 2026-11-17 – STATUS Schritt B (K2) fertig – App 0.74.3

- **Menü:** Abflugtafel · Mein Weg · Merkheft · Reisepass (alte Gestaltung: Heute · Mein Weg · Merkheft · Reisepass). `#/weltkarte/<kind>` führt in „Mein Weg · Karte“.
- **Mein Weg** mit Reitern **Stand · Kontinente · Karte** (`#/weg/<kind>-stand|-kontinente|-karte`):
  - Stand: Balken der eigenen Klasse nach der Rechenregel (Flüge mit `jahrgang[schulart] = Klasse`; gelandet = alle Pflicht-Etappen sitzen, „kann schon“ oder Ort geschafft), dazu wie bisher Gerade dran · Kommt noch · Kann ich. K3 ergänzt Mini-Linien und die drei Ebenen.
  - Kontinente: je Kontinent eine aufklappbare Karte mit „gelandet/gesamt“ (ohne Flüge für spätere Klassen), darin die Flüge mit Ort, Klasse und Stand.
  - Karte: nur Orte der eigenen Klasse (`orte[].ziel_klasse`), Route in Plan-Reihenfolge. Antarktis als Polarkarte von oben (Umriss aus der Weltkarte zurückgerechnet, Südpol in der Mitte, 0° oben).
- **Merkheft:** nur Geschafftes (Etappe fertig oder sitzt), gegliedert Kontinent → Flug → Etappe, Suche oben.
- **Reihenfolge der Flüge im Ort:** nach `reihenfolge` aus `schule_uebersicht.einheiten[]` (Zahl oder `{gym_by: n, …}` je Schulart des Kindes), sobald geliefert; sonst wie bisher.
  **Für den Haupt-Chat:** `schule_uebersicht` liefert das Feld noch nicht – es steht nur in `inhalte/themenliste.json`. Vorschlag: Spalte `thema.reihenfolge jsonb` und Ausgabe in `einheiten[]`; die Migration kommt mit Schritt C.
- Tests: 26 von 26 (3 neu: Reiter, Antarktis, Reihenfolge; Merkheft-Test auf „nur Geschafftes“ umgestellt).

## 2026-11-17 – Schritt A fertig (Befunde N1–N8) – App 0.74.2, Zweig bau-phase2 – Nachprüfung kann laufen

| Nr. | Umsetzung | Prüfpunkt |
|---|---|---|
| N1 | `lernErklaerung` zeigt ein Schrittbild nur, wenn sich die Zeichnung gegenüber dem zuletzt gezeigten Bild (auch dem Einstiegsbild) ändert; sonst steht nur der Text. Verglichen wird das gezeichnete Bild, nicht die Daten. Neu im Bild (Punkte, Strecken, Hilfslinien, Graphen, Kreise, Winkel, Bögen, Flächen, Thermometer-Stand) wird in der Akzentfarbe kräftig gezeichnet (Punkte größer, Linien 4 px), der Rest tritt zurück (40 % Deckkraft). Ein Steigungsdreieck (waagrechte + angehängte senkrechte Hilfslinie) wird in Erklärungen mindestens 2 Einheiten breit gezeichnet, gleiche Steigung; in Bordkarten nie. | „Was bedeutet eine negative Zahl?“: 3 Schritte, nur Schritt 1 mit Bild (vorher 3 gleiche Thermometer); Handy deutlich unter 2 400 px (Test). Kerze (Kl. 8): keine zwei gleichen Bilder hintereinander (Test). |
| N8 | Bildergeschichte mit Bild: Handy Nummer · Bild, darunter Text; ab 760 px Nummer · Bild links · Text rechts in einer Zeile. | Test: Text steht rechts neben dem Bild, gleiche Zeile (820 px). |
| N2 | „Kurz gesagt“ wird ganz gezeigt, kein „…“ und keine Zeilenkürzung. Satzende erkennt jetzt Abkürzungen („z. B.“). | Test. **Hinweis Inhalte:** 116 von 593 Etappen haben einen ersten Merksatz über 90 Zeichen (auf dem Handy mehr als zwei Zeilen). Das ist eine Inhaltsregel (≤ 12 Wörter), kein App-Fehler. |
| N3 | Kurs-Grafik: Der Komma-Platz in der Zeile ohne Nachkommastellen bleibt leer, ohne gestrichelten Rahmen. | Test (0,24 gegen 24). |
| N4 | Startknopf: „Erst 1 Wiederholung ›“ (Anzahl statt Ziel); ist die Runde heute gemacht: „Weiter nach Rom ›“. | Test. |
| N5 | Fehler-Detektiv nur, wenn kein Fehlermuster (`grund`) erkannt wurde – in Abflug- und alter Gestaltung. Die Einschränkung „nur Kl. 5/6“ habe ich nicht zusätzlich eingebaut (Auftrag: nur ohne Fehlermuster). | Code-Test. |
| N6 | Test-Seiten: Kopf „Rom · Natürliche Zahlen“ (Ort · Flug). | Test. |
| N7 | Testergebnis: Knöpfe im Abflug-Stil. Bei „noch üben“: Hauptknopf „Erst üben: <Etappe> ›“ (öffnet Üben dieser Etappe), dann „Verbessern ›“ (Test-Seite mit „Verbessern starten“), darunter „Zum Flug“ und „Zur Abflugtafel“. Zahlenstrahl: richtige Markierung grün mit ✓, gewählte falsche rot gestrichelt. „Einheit geschafft!“ heißt jetzt „Flug geschafft!“. | Test, Bild `test-results/n7-testergebnis-390.png`. |

**Tests:** `tests/lernen.test.cjs` 24 von 24 (6 neu). `tests/search.test.cjs`: die bekannten 9 alten Fehler, keine neuen.

**Hinweise für Inhalte (kein App-Fehler):** In der Kerze-Etappe überdeckt der Punktname „leer“ den Graphennamen „Kerze“ (beide bei x ≈ 13). Neue Elemente sind jetzt hervorgehoben; ob ein Schritt überhaupt ein neues Element bringt, entscheidet der Inhalt.
