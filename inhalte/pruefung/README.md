# Prüfrunde: Ablage der Ergebnisse (Werkstatt #150)

Drei Prüfer-Chats bewerten die Lerninhalte. Sie ändern **nichts** an `inhalte/themen/`, `inhalte/generatoren/`, App, Server oder Datenbank. Sie schreiben nur Ergebnisdateien in diesen Ordner, jeder auf seinem eigenen Zweig (von `lernen-app`). Der Haupt-Chat setzt die Ergebnisse um.

Gelesen wird: `inhalte/themen/<thema_schluessel>.json` (Erklärungen unter `inhalt.etappen`, Aufgaben unter `aufgaben`), `inhalte/themenliste.json` (Umfang, Lehrplan), `inhalte/README.md` (Format; Abschnitt „Zeichnungen“ zeigt, welche Bilder möglich sind).

Reihenfolge der Themen: zuerst Klasse 5, dann 8, dann 6, dann 9 (Feld `klasse.gym_by`). Ein Thema = eine Ergebnisdatei = ein Commit. Dateiname immer `<thema_schluessel>.json`.

## 1. Erklärungen → `inhalte/pruefung/erklaerungen/<thema_schluessel>.json` (Zweig `pruefung-erklaerungen`)

```json
{
  "thema_schluessel": "zahlen.ganz",
  "gesamturteil": "gut | brauchbar | schwach",
  "thema_hinweise": ["Was am Aufbau des Themas fehlt oder stört (Reihenfolge, fehlende Lernkarte, roter Faden)."],
  "karten": [
    {
      "lernziel": "addieren",
      "urteil": "ok | verbessern | neu_schreiben",
      "probleme": ["Konkret: was ist unklar, falsch, zu abstrakt, ohne Alltagsbezug?"],
      "neu": {
        "titel": "nur angeben, wenn geändert (höchstens 40 Zeichen)",
        "regel": "Neue Fassung. Wichtiges in ⟦…⟧.",
        "schritte": ["Vorgerechnetes Beispiel, Schritt 1", "Schritt 2 mit ⟦Ergebnis⟧"],
        "probe": "optional",
        "fehler": "Typischer Fehler mit konkreten Zahlen und Begründung",
        "bild": { "typ": "…" }
      },
      "strategie": "Optional: die elegantere Lösungsidee oder das Anschauungsmodell (z. B. Waage), falls in 'neu' eingearbeitet."
    }
  ],
  "neue_karten": [
    { "nach": "lernziel, hinter dem die Karte eingefügt wird", "lernziel": "neuer_name", "titel": "…", "regel": "…", "schritte": ["…", "…"], "fehler": "…", "begruendung": "Warum fehlt sie?" }
  ]
}
```

- Bei `urteil: "ok"` entfällt `neu`. In `neu` nur die Felder, die sich ändern; jedes angegebene Feld ersetzt das alte **vollständig** und muss fertig formuliert sein (kein „man könnte …“).
- `neue_karten` haben noch keine Aufgaben; die baut der Haupt-Chat nach.

## 2. Aufgaben → `inhalte/pruefung/aufgaben/<thema_schluessel>.json` (Zweig `pruefung-aufgaben`)

```json
{
  "thema_schluessel": "zahlen.ganz",
  "gesamturteil": "gut | brauchbar | schwach",
  "karten": [
    {
      "lernziel": "sach",
      "urteil": "ok | verbessern",
      "stufen": "Passen leicht/mittel/schwer? Was ist zu leicht, zu schwer, zu ähnlich?",
      "fehlende_aufgabentypen": ["Aufgabentyp, der fehlt – so genau, dass man ihn programmieren kann, mit 2 Beispielaufgaben samt Lösung."],
      "generator_regeln": ["Regel für das Erzeugungsprogramm, z. B. 'Einzahlung und Abhebung nie gleich groß', 'Rezeptmengen höchstens 500 g Zucker'."]
    }
  ],
  "fehler": [
    { "aufgabe": "Fragetext wörtlich", "art": "falsch | mehrdeutig | unrealistisch | sprache | tipp_verraet_loesung | loesungsweg", "problem": "…", "korrektur": "Richtige Fassung von Frage, Lösung oder Lösungsweg" }
  ]
}
```

## 3. Aufbau und Lehrplan → `inhalte/pruefung/aufbau/<klasse>.json` (Zweig `pruefung-aufbau`), z. B. `klasse5.json`

```json
{
  "klasse": 5,
  "reihenfolge": [ { "thema_schluessel": "zahlen.natuerlich", "position": 1, "braucht_vorher": ["…"], "begruendung": "…" } ],
  "luecken": [ { "was_fehlt": "…", "lehrplan_bezug": "…", "wohin": "neues Thema | Thema X, neue Lernkarte", "dringlichkeit": "hoch | mittel | niedrig" } ],
  "zu_viel": [ { "thema_schluessel": "…", "lernziel": "…", "warum": "gehört in Klasse …" } ],
  "themen": [ { "thema_schluessel": "…", "abdeckung": "vollständig | teilweise | dünn", "hinweise": ["…"] } ]
}
```

## Für alle

- Auf Deutsch, in der Sprache des Kindes der jeweiligen Klasse (kurze Sätze, „du“).
- Fakten von Meinungen trennen: Rechen- und Fachfehler als solche benennen; Geschmacksfragen als Vorschlag.
- Keine Schulbuchtexte abschreiben. Keine Namen realer Personen.
- Am Ende eine kurze Zusammenfassung im Chat: wie viele Themen geprüft, die 10 wichtigsten Befunde.
