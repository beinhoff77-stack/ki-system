> **FREIGEGEBEN vom Nutzer am 27.11.** („Was wackelt sieht jetzt gut aus“). Gültige Vorlage für den Bau. Entwürfe 1 und 2 sind abgelehnt, Entwurf 3 ist überholt.

# Vorgabe WK, vierte Runde: „Was wackelt“ – Fehler als schlanke Tabelle

Designer, 27.11.2026. Weiterentwicklung von `../entwurf3/` (dort gilt alles, was hier nicht steht: Stil, Auswertung, Regeln fürs Verschwinden, Datenbedarf). Entwurf: `index.html`, Bilder: `bilder/`.
Nutzer zu Entwurf 3: „Ihre falschen Antworten müssen nicht so riesig dargestellt werden, eher schlank, tabellarisch und übersichtlich. Die Auswertung oben ist ein guter Anfang.“

## Unterschiede zu Entwurf 3
- **Auswertung** unverändert, nur geschärft: je Thema neben „3 von 4“ die Fehlerquote fett („75 %“).
- **Letzte Fehler**: die 5 neuesten als Tabelle in einer Karte, eine Zeile je Antwort (44 px): Datum · Thema › Lernkarte · Aufgabe (einzeilig, voller Text als Tooltip) · Eingegeben (dezent rot) · Richtig (dezent grün) · Fehlerart kurz („nur 1. Zeichen gedreht“, „Wurzel vergessen“; ✓ = danach richtig gelöst; ganze Beschreibung als Tooltip) · zwei Symbolknöpfe 32 px „↻“ Nachüben schicken und „✓“ Abhaken (mit `aria-label` und `title`). Spalten 1440 px: 52 · 300 · Rest · 96 · 96 · 176 · 76.
- **Aufklappen**: Klick auf die Aufgabe → direkt unter der Zeile voller Text, Zeilen des Fehler-Detektivs, Zeichnung/Tabelle, ganze Fehlerbeschreibung (+ 2. Anlauf / mit Tipp / danach richtig) und Lösungsweg. Standard: zu.
- **Nachüben geschickt**: statt des ↻-Knopfs in der Zeile „↻ liegt bereit“ (blau, Tooltip mit Datum); Abhaken bleibt.
- **Nach Themen**: eine Karte, je Thema eine Gruppenzeile (52 px) mit ▸/▾, Name, Zähler, rechts „alle nachüben“ und „alle abhaken“. Offen ist zu Beginn nur das Thema mit den meisten offenen Fehlern; zugeklappte Themen zeigen in derselben Zeile die Fehlerarten. Im offenen Thema: Spaltenkopf, Lernkarte als Zwischenzeile mit Zähler, darunter die Aufgabenzeilen (ohne Spalte Thema › Lernkarte).
- **Handy (< 760 px)**: jede Zeile zweizeilig – oben ▸ Aufgabe, unten „Eingegeben → Richtig · Datum“ und die zwei Knöpfe; Spalten Thema und Fehlerart entfallen (stehen aufgeklappt); Themen-Knöpfe unter dem Namen. Kein seitliches Rollen.
- Sammelaktion je Lernkarte entfällt (je Thema reicht bei 1–3 Lernkarten).

## Gemessene Seitenhöhen (Chrome, Kind 2, 10 offene Fehler, Zeitraum 14 Tage)
| Fassung | Höhe | Bildschirme |
|---|---|---|
| Entwurf 3, 1440 × 900 | 4 869 px | 5,4 |
| **Entwurf 4, 1440 × 900** | **1 738 px** | **1,9** |
| Entwurf 4, eine Zeile aufgeklappt (Fehler-Detektiv) | 1 935 px | 2,2 |
| Entwurf 4, Kind 1 (7 offene) | 1 529 px | 1,7 |
| Entwurf 4, 400 × 860 (Handy) | 2 876 px | 3,3 (Entwurf 3: 7 994 px) |
In allen zehn Bildern ist nichts breiter als das Fenster (scrollWidth = Fensterbreite).

## Bilder
01 oben hell · 02 ganze Seite hell · 03 ganze Seite dunkel · 04 eine Zeile aufgeklappt · 05 nach Abhaken (Meldung mit Rückgängig, 9 offen) · 06 Thema „Lineare Ungleichungen“ aufgeklappt mit „liegt bereit“ · 07 leer · 08 Kind 1 ganze Seite · 09 Handy ganze Seite hell · 10 Handy ganze Seite dunkel (Kind 1).
