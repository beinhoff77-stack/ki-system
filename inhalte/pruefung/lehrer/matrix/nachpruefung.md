# Nachprüfung Lehrplan-Matrix (LM-1 bis LM-5) – App 0.84.0, und Übersichtsblatt nach der Dreißigsten Runde

Stand: `main` 44c1e7a (App 0.84.0, Cache v154), Datenbank 22.11. (lesend: `schule.voraussetzung`, `schule.thema.eigenstaendig`, Funktionen `api.schule_lehrplan_matrix`/`_thema` vorhanden). Vorgabe: `umsetzung.md`, Vorlage `entwurf/lehrplan-matrix.html`, Abweichungen laut `inhalte/postfach/bau-motivation.md` („FERTIG: 0.84.0“, „0.84.0 b“).
Geprüft: die 8 LM-Tests des Bau-Chats selbst laufen lassen (8/8 grün, Bilder dabei neu erzeugt: `nachpruefung-bilder/`), Bilder 400/820/1280 angesehen. Testkind und erfundener Lernstand; **nicht** gegen den echten Server mit Lernstand der Kinder (keine Kinderdaten).

## A Übersichtsblatt neu erzeugt (Artifact „Mathe 5–10 – was gelernt wird“, Kopie `entwurf/lehrplan-matrix.html`)
- Grundlage: `inhalte/themenliste.json` (97 Themen) und `schule.voraussetzung` (128 Verbindungen, 66 hart; Kopie `nachpruefung-bilder/verbindungen-22-11.json`), „eigenständig“ aus `schule.thema.eigenstaendig` (7 Themen, Begründung im Detail grün).
- Die zehn aufgelösten Themen stehen blass („aufgelöst“) und zählen nicht in den Klassen-Zahlen. Die Liste „vermutete Datenlücke“ ist entfernt.

### Die drei Prüfregeln
| Regel | Gymnasium | Realschule |
|---|---|---|
| 1 Kein Thema mit Klasse ohne Verbindung, außer eigenständig | **erfüllt** (73 Themen) | **5 Verstöße** – alle aufgelöste Themen, siehe D1 |
| 2 Keine Voraussetzung in einer späteren Klasse | **erfüllt** | **erfüllt** |
| 3 Themen 100–103 verknüpft | **erfüllt** (Volumen, Prismen und Zylinder, Potenzgesetze, Potenzgesetze mit ganzzahligen Exponenten) | |

## B Matrix 0.84.0 gegen die Vorgabe
| Punkt | Stand |
|---|---|
| LM-1 Matrix unter Nachschlagen → Lehrplan, alle Themen, Zeilen/Spalten, „Einordnen nach“ (+ IB MYP), Kennzeichen „Gym 8 · RS 7 · IB 4“, Kopf je Klasse, Suche, Kurzbeschreibung | erledigt |
| LM-1 Handy als Liste, Detail unter dem Thema | erledigt (`lm-matrix-400.png`) |
| LM-2 Detail (gefordert, braucht vorher mit Begründung, weiter zurück, baut darauf auf, merke, Beispiel, Etappen, Lehrplan, ‹ ›), „Eigenständig: … ‹Begründung›“ | erledigt |
| LM-3 Verbindungen, Linien hinter den Karten, „→ n“, Handy ohne Linien | erledigt (im Test per `elementFromPoint` geprüft) |
| LM-4 Lernstand Aus / Kind / Beide, „hier ist …“, Balken je Klasse, Detail mit „Im Plan öffnen“/„Fehler besprechen“ | erledigt |
| LM-5 Stufen-Knöpfe im Detail (Variante A) mit Rückgängig; „Als Matrix ansehen ›“ im Plan; „Im Plan öffnen“ klappt auf | erledigt |
| Abnahme 400/820/1280: kein Wort ohne Trennstrich umbrochen, kein Querrollen | erledigt (Test) – Lesbarkeit siehe N1 |

### Abweichungen des Baus – Bewertung
- Stufenfarben wie im Plan statt Vorlagenfarben: **einverstanden** (Vorgabe sagt „wie im Plan“). Der Rahmen unterscheidet ▶ von den gelben Voraussetzungen ausreichend.
- „IB MYP“ als dritte Schulart: **einverstanden**.
- Liste `LUECKE` nicht übernommen: **richtig** (in Runde 30 geklärt; auch im Blatt entfernt).
- Filter „Inhalt“ (fertig / in Prüfung / fehlt) als Ersatz für den weggefallenen Sammelblick: **einverstanden**.
- Info-Seite: neue Texte gelesen, passen zur Matrix.

## Neu aufgefallen
**N1 (Sollte) – Rechner 1280: Spalten zu schmal, Titel stark zerstückelt.** Acht Spalten plus Detail rechts (ca. 320 px) lassen je Spalte rund 95 px. Titel werden mehrfach getrennt („Li-neare Gleichun-gen“, „Ver-hältnisse und Raten“); mit Kennzeichen und Stufenzeile sind die Karten 5–7 Zeilen hoch. Bild: `lm-matrix-1280.png`. Vorschlag: Detail bei ≥ 1100 px **erst beim Antippen** als Spalte einblenden (sonst volle Breite für die Matrix), oder Kennzeichen „Gym 7 · RS 7 · IB 2“ bei gewähltem Kind ausblenden (die Stufe ist dann wichtiger).

**N2 (Sollte, Daten → `lehrplan-lb`) – Fünf aufgelöste Themen haben noch eine Realschul-Klasse:** 48 Vektoren und Determinanten (RS 7), 78 Parameter und Funktionenscharen (RS 8), 40 Graphentransformation (RS 9), 12 Reinquadratische Gleichungen (RS 9), 77 Umkehrfunktionen (RS 10). Sie haben keinen Flug und keine Verbindungen, stehen aber im Lehrplan der Realschule als Pflicht. Wie bei Thema 12 fürs Gymnasium: `rs_by` entfernen oder in der Matrix über `ohne_flug` sicher blass und ohne Zählung (im Test mit nachgebildeten Daten nicht prüfbar, weil die Testdaten `ohne_flug` dort nicht setzen).

**N3 (Kann, Daten) – Thema 83 „Mengen und Venn-Diagramme“** ist aufgelöst, trägt aber `eigenstaendig`. Einer der beiden Einträge ist überholt.

**Hinweis** – Realschule Kl. 8 bleibt dünn (6 Pflichtthemen ohne aufgelöste, Kl. 7: 19). Laut Bericht `lehrplan-lb` fehlen Inhalte (Vierecke, Drehung, Baumdiagramm/Vierfeldertafel); die Zuordnung ist richtig. Kein Fehler der Matrix.

## Nicht geprüft
Echter Server mit echtem Lernstand (Kinderdaten), Safari/iPad-Silbentrennung, Ladezeit auf langsamer Verbindung.
