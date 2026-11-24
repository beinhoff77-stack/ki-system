# Effekt-Test W180 – Ergebnis (24.11.2026)

Auftrag: zwei Highlight-Effekte „Opa“ (5 in Folge) und „Horror-Clown“ (Direktflug) als je eine HTML-Datei,
gleicher Auftragstext (Fassung 2/3) für alle, Bewertung blind durch Sebastian.

## Zuordnung (nach der Bewertung aufgedeckt)

| Effekt | Plan | Modell |
|---|---|---|
| Opa | A | Kimi K3.1 Pro (Council) |
| Opa | B | Claude Fable 5.2 |
| Opa | C | Muse Spark 1.3 (Council) |
| Opa | D | GPT-6 (Codex) |
| Clown | A | GPT-6 (Codex) |
| Clown | B | GLM 5.3 (Council) |
| Clown | C | Claude Fable 5.2 |
| Clown | D | Kimi K3.1 Pro (Council) |
| Clown | E | Muse Spark 1.3 (Council) |

Nicht dabei: Gemini 4 Neon und Grok 4.7 (beide Effekte), GLM 5.3 (Opa) – Council-Motor brach die
langen Aufrufe nach ca. 150 s ab (siehe Werkstatt-Wunsch 181), danach OpenRouter-Tagesbudget erschöpft.

## Reihenfolge Sebastian

- Opa: B > A > D > C → Fable, Kimi, GPT, Muse
- Clown: D > C > A > B > E → Kimi, Fable, GPT, GLM, Muse

Punkte (Platz 1 = Anzahl Teilnehmer, Opa 4…1, Clown 5…1):

| Modell | Opa | Clown | Summe |
|---|---|---|---|
| Claude Fable 5.2 | 4 | 4 | 8 |
| Kimi K3.1 Pro | 3 | 5 | 8 |
| GPT-6 (Codex) | 2 | 3 | 5 |
| GLM 5.3 | – | 2 | 2 (nur Clown) |
| Muse Spark 1.3 | 1 | 1 | 2 |

## Kosten

| Modell | erfasst (Council) | Hinweis |
|---|---|---|
| Kimi K3.1 Pro | 0,30 $ + 0,32 $ = 0,62 $ | zu niedrig: abgebrochene Versuche vor dem Erfolg nicht erfasst |
| Muse Spark 1.3 | 0,04 $ + 0,04 $ = 0,08 $ | im ersten Versuch fertig |
| GLM 5.3 | 0,08 $ (Clown) | zu niedrig, wie oben |
| Gemini 4 Neon, Grok 4.7 | 0 $ erfasst | nur abgebrochene Aufrufe, Kosten unbekannt |
| Fable 5.2, GPT-6 | Abo | kein Einzelpreis |

OpenRouter-Tagesbudget 24.11.: 10,54 $ verbraucht, davon 0,78 $ im Council erfasst. Annahme: Rest überwiegend
abgebrochene Aufrufe dieses Tests (im OpenRouter-Aktivitätsprotokoll prüfbar).

## Einbau-Aufwand (Ersteinschätzung aus dem Codeaufbau, keine Vollprüfung)

Alle 9 Dateien: laufen ohne Konsolenfehler bei 390 × 700, haben Abspielen/Überspringen/Nochmal,
Ton per Web Audio, Fassung für „Bewegung reduzieren“.

| Modell | Größe je Effekt | Aufbau | Einbau |
|---|---|---|---|
| GPT-6 | ca. 10 KB | eine Zeitschleife, kompakt | leicht |
| Muse Spark 1.3 | ca. 11 KB | Zeitgeber-Kette | leicht |
| GLM 5.3 | ca. 14 KB | Zeitgeber + Animation | leicht–mittel |
| Fable 5.2 | ca. 25 KB | SVG-Figur + Canvas-Wolke, Zeitgeber | mittel |
| Kimi K3.1 Pro | ca. 37–40 KB | große CSS/SVG-Szenen | mittel |

## Dateien

- einreichungen/<modell>/opa.html, clown.html (Fable/GPT mit notiz.md)
- vergleich/index.html – Blindvergleich (Artefakt), vergleich/zuordnung.json – Zuordnung
