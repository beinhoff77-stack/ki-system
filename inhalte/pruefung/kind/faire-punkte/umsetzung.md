# Vorgabe „faire Punkte“ (FP-App): Landungs-Bonus und Hinweis bei 5 Sternen

Stand 22.11.2026. Grundlage: `inhalte/AUFTRAEGE.md` (Zweig `lernen-app`), „Bau-Auftrag FP – faire Punkte“, Abschnitt FP-App. Nur Vorgabe, kein App-Code. Stil und Bewegungsregeln wie die Abschluss-Ansichten (AB-A, `inhalte/pruefung/kind/abschluss/umsetzung.md`). Texte für Klasse 5. Alle Zahlen kommen vom Server (`landung.bonus`, `landung.fehler`, `landung.stufe`, `sterne`); die App rechnet nichts selbst.

## 0 Wichtig: Bonus-Stufe ≠ Abschluss-Fassung
Die Fassung der Einblendung (Direktflug / Saubere Landung / Sturmflug, AB-A) hat **andere Regeln** als der Bonus (zählt jede falsche Übungsantwort, Tipps zählen nicht). Beispiele: 0 Fehler, aber mit Tipp → Fassung „Saubere Landung“, Bonus +80; 2 Fehler über mehrere Lerntage → „Sturmflug“, Bonus +40.
**Darum:** Der Bonus bekommt **eigene Wörter** und benutzt **nicht** „Direktflug“ (sonst stünde „Saubere Landung“ und „Direktflug +80“ im selben Bild). Der Vorschlag „Direktflug – ohne Fehler +80“ aus dem Auftrag wird ersetzt.

## 1 Landungs-Einblendung mit Bonus
Ort: im Blatt der Etappen-Einblendung (alle drei Fassungen von AB-A), **direkt unter dem Abzeichen bzw. der großen Zahl, über dem Knopf**. Eine eigene Zeile, als Kachel:

```
┌───────────────────────────────────────────┐
│ ★  Landungs-Bonus          +80 ★          │
│    ohne Fehler gelandet                   │
└───────────────────────────────────────────┘
```

| `landung.stufe` | Zeile 1 (fett) | Zeile 2 (klein) | Kachel |
|---|---|---|---|
| `ohne` (0 Fehler) | **Landungs-Bonus +80 ★** | „ohne Fehler gelandet“ | Gold-Rand, heller Gold-Grund, drei kleine Funken |
| `wenig` (1–2 Fehler) | **Landungs-Bonus +40 ★** | „mit 1 Fehler gelandet“ / „mit 2 Fehlern gelandet“ (Zahl aus `landung.fehler`) | Rand in der Fassungsfarbe, weißer Grund |
| `sonst` (3+) | **Landungs-Bonus +10 ★** | „gelandet – geschafft!“ | Rand in der Fassungsfarbe, weißer Grund |

- **Beim Sturmflug (Fassung 1c) nie eine Fehlerzahl** (Regel aus AB-A): Zeile 2 dort immer „gelandet – geschafft!“, auch bei Stufe `wenig`; bei `ohne` „ohne Fehler gelandet“ darf stehen (kein Tadel).
- **Kein Vergleich, kein „hätte“:** kein „Mit weniger Fehlern wären es 80 gewesen“. Wie man mehr bekommt, steht nur auf der Info-Seite (Punkt 4).
- **Bewegung** (≤ 0,8 s, nach der Bewegung der Fassung; abschaltbar wie AB-A): Kachel schiebt von unten ein, Zahl zählt hoch (0 → 80/40/10), dann fliegt „+80“ zum Sterne-Zähler oben, der kurz springt. Antippen beendet sofort (Endzustand).
- **Handy 360 × 640:** Die Kachel darf nicht zum Scrollen zwingen. Wird es zu eng, fällt Zeile 2 weg (Zeile 1 bleibt).
- **Fehlt `landung`** (alter Server, gesetzte Etappe „Kann er“): keine Kachel, alles wie bisher.
- Kommt danach „Flug geschafft“ / „Flug abgelegt“, zählt deren Sternezeile den Bonus **nicht** noch einmal.

## 2 Hinweis bei 5 statt 10 Sternen (Übung)
Nach einer richtigen Antwort zeigt die Rückmeldung den Serverwert `sterne`:

| Fall | Rückmeldung | Hinweis darunter (klein, grau, ohne Symbol) |
|---|---|---|
| 1. Versuch, ohne Tipp (`sterne` 10) | „Richtig!  +10 ★“ | – |
| mit Tipp (`sterne` 5) | „Richtig!  +5 ★“ | „Ganz ohne Tipp gibt es 10 ★.“ |
| 2. Versuch (`sterne` 5) | „Richtig!  +5 ★“ | „Gleich beim ersten Mal gibt es 10 ★.“ |
| schon gezählt (`sterne` 0) | „Richtig!“ | – |

- **Nicht nerven:** Der Hinweis erscheint höchstens **einmal je Etappe und Lerntag**; danach nur „Richtig! +5 ★“.
- Farbe der „+5 ★“-Marke **gleich** wie bei +10 (kein Grau, kein Rot) – 5 Sterne sind ein Gewinn.
- Keine Wörter wie „nur“, „leider“, „Abzug“, „weniger“.

## 3 Einmaliger Hinweis nach der Nachbuchung
Wenn der Server ihn liefert (einmal je Kind, beim nächsten Öffnen der Startseite), als schmale Karte über „Jetzt dran“:

> **★ Geschenk für deine Landungen**  
> Für deine bisherigen Landungen gibt es nachträglich **+{n} ★** Landungs-Bonus.  
> [Super ›]

Gold-Rand, ein Funken-Moment beim Erscheinen; „Super ›“ schließt sie für immer. Keine Aufschlüsselung nach Etappen.

## 4 Info-Seite (Eltern/Lehrer und Kinder-Hilfe)
Abschnitt „Sterne“ ersetzen durch:
- „Jede Übungsaufgabe bringt einmal Sterne: **10 ★**, wenn sie im ersten Versuch ohne Tipp gelöst ist, sonst **5 ★**.“
- „Bei jeder Landung einer Etappe gibt es einmal einen **Landungs-Bonus**: **+80 ★** ohne Fehler, **+40 ★** mit 1–2 Fehlern, sonst **+10 ★**. Tipps zählen nicht als Fehler. Tests, Wiederholungen und Mischkarten zählen hier nicht mit.“
- „Wiederholungen bringen 10 ★, wenn sie selbst gelöst sind.“ (wie WD)
- „Für Etappen, die vor dem 22.11. gelandet sind, wurde der Bonus einmal nachgetragen. Gebuchte Sterne werden nie abgezogen.“

## Prüfen nach dem Bau (0.87.0)
Alle drei Bonus-Stufen in allen drei Fassungen (u. a. Sauber + 80, Sturmflug + 40 ohne Fehlerzahl); 400/820/1280 und 360 × 640 ohne Scrollen; „weniger Bewegung“; Hinweis 5 ★ nur einmal je Etappe und Tag; ohne `landung` unverändert; Nachbuchungs-Karte einmalig; Testkind und erfundene Daten.
