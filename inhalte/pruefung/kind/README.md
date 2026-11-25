# Gestaltung Kinderansicht – Übersicht für den Designer

Stand 25.11.2026. Alle Vorgaben und Entwürfe des bisherigen Gestalters (Opus 5.5).
Jeder Ordner: `umsetzung.md` = Vorgabe für den Bau, `entwurf/` = klickbarer Entwurf
(im Browser öffnen), `bilder/` = Bildfolgen, ggf. Prüfberichte `nachpruefung*.md`.

| Ordner | Inhalt | Stand |
|---|---|---|
| `effekte/` | Vorgabe FX Fassung 4: Effekt-Motor, 15 große, 15 kleine, 8 Saison-, 4 Reserve-Effekte; `effekte.json` (Texte, Anlässe, Regeln), `entwurf/effekte.html` (alle Effekte abspielbar, Datum, 21-Tage-Simulator, Ton, „Bewegung reduzieren“) | Vorgabe fertig, Bau offen |
| `effekte/quelle/` | Quellen des Entwurfs: `vorlage.html` (Gerüst, Platzhalter `/*DATEN*/null`), `lang*.js` / `teen*.js` (Effekt-Funktionen), `*.cjs` (Playwright: Bilder, Bildfolgen, Simulator), `kleben.py` (Bildfolgen zusammensetzen) | Arbeitsdateien |
| `effekt-test/` | Blindtest 24.11.: 7 KIs, „Opa“ + „Horror-Clown“; `ergebnis.md`, `einreichungen/`, `vergleich/` | ausgewertet: Fable 5.2 und Kimi vorn |
| `jugendwoerter/` | 74 Wörter, 52 Sprüche, Regeln; `woerter.json`, `entwurf/jugendwoerter.html`, `quelle/gen.py` (erzeugt woerter.json) | Vorgabe fertig, Sticker live (0.93.1) |
| `karte/` | Reisekarte je Kind (Kontinente, Flüge, Städte, Länder-Schilder, Sperr-Anzeige); `entwurf/reisekarte.html` + Bau-Skripte; Prüfungen RK 1/2 | live (0.92.3 ff.) |
| `karten/` | Kartenansichten (Nachbessern, Mein Schuljahr, Zusatz eingeplant, Stand); Prüfung KJ | live (0.93.x) |
| `abschluss/` | Abschluss-Ansichten (Etappe/Flug geschafft, Landungsarten direkt/sauber/sturm) | live |
| `expedition/` | Expeditionen (verknüpfte Aufgaben, Stempel, 150/200 Sterne) | live (0.91.2) |
| `abgelegt/` | Ansicht abgelegter Etappen/Flüge | Vorgabe |
| `reise-aufbau/` | Aufbau Kontinent/Land/Stadt | Vorgabe |
| `faire-punkte/` | Punkteregel ohne Minuspunkte | Vorgabe |
| `n087/`, `nachpruefung_2211.md` | ältere Prüfungen | erledigt |

Entscheidungen des Nutzers zum Stil: siehe Start-Auftrag des Designers (Teenager-Stil, „Digga“,
Horror ohne Blut, Effekte spektakulär, Pflicht-Effekte bei „Etappe 100 %“ und „wieder offen“,
Saison-Effekte, Schutzregeln Flackern/Bewegung/Ton).

Postfach des bisherigen Gestalters: `inhalte/postfach/pruefung-kinderansicht.md`.
