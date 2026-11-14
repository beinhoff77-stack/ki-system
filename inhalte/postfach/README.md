# Postfach: Meldungen der Chats an den Haupt-Chat

Damit niemand Berichte von Hand weiterreichen muss, schreibt jeder Chat seine Meldungen hierher – auf **seinem eigenen Zweig**, mit Commit und Push. Der Haupt-Chat sieht alle Zweige und liest das Postfach regelmäßig.

Datei: `inhalte/postfach/<name-des-zweigs>.md` (z. B. `einarbeiten-kl8.md`). Neueste Meldung oben, jede mit Zeitpunkt.

```markdown
## 2026-11-14 15:10 – STATUS | FRAGE | BLOCKIERT | FERTIG
Kurz und konkret: was ist erledigt, was fehlt, was brauchst du?
- Bei FRAGE: die Frage, deine eigene Annahme, und womit du inzwischen weitermachst.
- Bei BLOCKIERT: was genau nicht geht (Fehlermeldung wörtlich) und was du schon versucht hast.
- Bei FERTIG: der Abschlussbericht, den du sonst in den Chat schreiben würdest (Tabelle der Themen, umgesetzte/abgelehnte Punkte, offene Punkte).
```

Regeln:
- **Nicht auf Antwort warten.** Bei einer Frage die fachlich naheliegende Annahme treffen, notieren, weiterarbeiten.
- Nach jedem fertigen Thema eine STATUS-Zeile, am Ende FERTIG.
- Antworten des Haupt-Chats stehen auf dem Zweig `lernen-app` in `inhalte/postfach/antworten.md`. Vor jedem neuen Thema den Stand von `lernen-app` holen und dort nachsehen.
- Wünsche an die App (fehlende Zeichnung, fehlender Antworttyp, Fehler in der App) ebenfalls hier als FRAGE mit dem Wort „App-Wunsch“.
