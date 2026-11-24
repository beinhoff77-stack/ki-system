# Vorgabe FX – Spezialeffekte nach Ereignissen

Stand 24.11.2026 · Daten: `effekte.json` · Entwurf zum Anklicken: `entwurf/effekte.html` (alle 11 Effekte abspielbar, Regel-Simulator) · Bilder: `bilder/<effekt>-400-tag|nacht|ende.png`, `bilder/f404|tresor-820-*.png`, `bilder/f404-400-ruhig.png` · Entwurf online: Artefakt 0ceb2a4f-cdef-4a72-a3f0-4dcb90cfe1c4

Kein App-Code, keine Datenbank, keine Namen. Alles läuft auf dem Gerät. Kein Effekt vergibt Sterne, keiner braucht den Server.

## 0. Kurzfassung

- **11 Effekte:** 8 positiv, 3 „negativ“ (Missgeschick mit Witz, nie Strafe).
- **Zwei Ereignisse bekommen ihren Effekt immer** (Wunsch Sebastian, 24.11.):
  - **„Für immer“:** Eine Etappe ist endgültig sicher und muss nie wieder geübt werden.
  - **„Koffer aufgeplatzt“:** Zwei Fehler in der Wiederholung öffnen die Etappe wieder; sie muss nachgebessert werden.
- **Die übrigen 9 kommen per Zufall:** Der Anlass bestimmt, welcher Effekt passt; der Zufall bestimmt, ob er kommt.
  - Etwa jeder 6. passende Anlass.
  - Höchstens 1 am Lerntag.
  - Nie zweimal derselbe hintereinander.
  - Sicherheitsnetz: Kam an 3 Lerntagen kein Effekt, kommt er beim nächsten passenden Anlass sicher.
- **Kurz und überspringbar:** 1,5–2,8 s; Antippen beendet sofort.
- **Ruhige Fassung:** Bei „Bewegung reduzieren“ kein Flackern und kein Wackeln, nur Text und Sticker.
- **Nie** beim Flug-Test, nie ab dem 2. Fehler in Folge, nie zwei Effekte direkt hintereinander.

## 1. Die Effekte

Spalte „Wo“ nennt die Ansicht im Code, Stand lernen-app 0.93.x. Die Texte sind wörtlich zu übernehmen; `{…}` wird eingesetzt.

| # | Effekt | Anlass (immer/Zufall) | Wo | Ablauf | Text | Sticker | Dauer | Aufwand |
|---|---|---|---|---|---|---|---|---|
| 1 | **Für immer** ✨ | Etappe endgültig sicher – **immer** | Ergebnis der Wiederholung, die die Etappe sicher macht | dunkelt ab → goldener Stempel „FÜR IMMER“ knallt von groß auf normal, kurzer Ruck, Druckwelle, Goldfunken → Text → Stempel fliegt klein nach oben rechts (Reisepass) | `FÜR IMMER` · `{Etappe} sitzt.` · `Muss nie wieder geübt werden.` | +1000 Aura | 2,8 s | mittel |
| 2 | **Gehackt!** ✨ | 10 in Folge richtig – Zufall | Rückmeldung der Bordkarte (Übung) | schwarz → grüne Zeilen tippen sich (je ~350 ms) → Sticker in der Mitte → zurück | `> EINDRINGLING ERKANNT …` · `> ZUGRIFF AUF MATHE-ZENTRALE …` · `> 10 VON 10 RICHTIG …` · `> QUELLE: DU` | Gommemode aktiviert | 2,6 s | klein |
| 3 | **Fehler 404** ✨ | Direktflug – Zufall | `lernAbschlussEtappe`, vor der Szene | 2 Flacker-Wechsel → dunkle Tafel „404“ mit leichtem Farbversatz → Tafel bricht weg → Landung | `404` · `FEHLER NICHT GEFUNDEN` | Çüş – null Fehler. | 2,2 s | klein |
| 4 | **Sterne-Glitch** ✨ | Flug geschafft – Zufall | `lernAbschlussFlug`, beim Hochzählen der Sterne | Zahl rattert über das Ziel bis 4.000.000 ★ (Farbversatz) → Zeile → fällt auf den echten Wert zurück | `Moment … {sterne} ★. Sorry, war aufgeregt.` | normaler Flug-Sticker | 2,4 s | klein |
| 5 | **Glückstaube** ✨ | saubere Landung – Zufall | `lernAbschlussEtappe` | Klecks platscht aufs Glas → Sprechblase → Wischen macht ihn blasser (weg ab 60 %), sonst nach 4 s weg | `Bringt Glück! Wegwischen.` | W | bis 4 s | klein–mittel |
| 6 | **Möwe** ✨ | Knobel-Bordkarte im 1. Versuch richtig – Zufall | Knobel-Rückmeldung | Möwe fliegt groß ins Bild → Aufprall (platt), Federn fliegen → rutscht nach unten raus | – | Sheesh! | 2,2 s | klein–mittel |
| 7 | **Turbulenzen** ✨ | 5 in Folge richtig – Zufall | Rückmeldung der Bordkarte | Bildschirm wackelt 0,8 s (≤ 6 px) → 3 Sauerstoffmasken fallen und pendeln → Sprechblase → Masken hoch | `Hier spricht euer Kapitän: Ihr rechnet zu schnell – wir müssen bremsen.` | Locked in. | 2,4 s | mittel |
| 8 | **Comeback** ✨ | nach einem Fehler 3 richtige in Folge in derselben Etappe (neuer Anlass) – Zufall | Rückmeldung der Bordkarte | Videokassetten-Rückspulen: Streifen, Verziehen, „◀◀ REWIND“ | `◀◀ REWIND` | Comeback. | 1,6 s | klein |
| 9 | **Kaffee verschüttet** 😬 | erster Fehler eines Lerntags – Zufall | Fehler-Rückmeldung | Becher kippt am oberen Rand → Fleck läuft über die **Ecke** der Bordkarte (nie über Antwort/Lösung) → Sprechblase → trocknet weg | `Ups – mein Kaffee. Daran lag’s. Nächste!` | – (ersetzt dort den Schere-Sticker) | 1,8 s | klein |
| 10 | **Koffer aufgeplatzt** 😬 | zwei Fehler in der Wiederholung → Etappe wieder offen – **immer** | Ergebnis der Wiederholung; gibt es dort keine Ansicht: erstes Erscheinen der Nachbessern-Karte | Koffer fährt auf dem Band ins Bild → fällt, Deckel springt auf → Ziffern fliegen heraus → Text → Nachbessern-Karte schiebt sich ins Bild | `Dein Koffer ist aufgegangen – sammeln wir’s wieder ein.` | – | 2,2 s | mittel |
| 11 | **Gewitter** 😬 | Sturmflug gemeistert – Zufall | `lernAbschlussEtappe` (sturm) | dunkelt ab → 2 Blitze (je 120 ms) → Regen läuft über das Glas → klart auf | – | Tuff durchgezogen. | 2,6 s | mittel |

**Zum Ton bei „Für immer“ und „Koffer“:**
- „Für immer“ ist der größte Moment der App: Gold, Ruck, Funken. Das Kind soll merken, dass das jetzt geschafft ist.
- „Koffer“ macht aus einem Rückschlag ein Missgeschick: „sammeln wir’s wieder ein“, nicht „falsch“. Die Nachbessern-Karte zeigt sofort den Ausweg (3 in Folge).

**Mehrere Etappen auf einmal:** Der Effekt läuft einmal, mit Zahl: `3 Etappen sitzen.` bzw. `2 Koffer sind aufgegangen – sammeln wir’s wieder ein.`

**Flug wird golden:** Macht „Für immer“ den ganzen Flug golden (alle Städte sicher), steht unter dem Text zusätzlich `Flug golden! {Land} ist komplett.`

## 2. Regeln (fest, keine Einstellungen)

1. **Zufall:** Bei einem passenden Anlass kommt der Effekt mit 17 % (etwa jeder 6.).
2. **Höchstens 1 Zufalls-Effekt je Lerntag.** Lerntag wie bei den übrigen Lerntag-Zählern.
3. **Nie derselbe Zufalls-Effekt zweimal hintereinander** (über Tage hinweg).
4. **Sicherheitsnetz:** Gab es an 3 Lerntagen passende Anlässe, aber keinen Effekt, kommt er beim nächsten passenden Anlass sicher.
5. **„Für immer“ und „Koffer“ kommen immer.**
   - Sie zählen nicht zum Tageslimit.
   - Nach ihnen kommt am selben Tag frühestens nach 2 weiteren Anlässen ein Zufalls-Effekt.
   - Je Etappe kommt jeder der beiden höchstens einmal.
6. **Nie:** im Flug-Test, ab dem 2. Fehler in Folge, zwei Effekte direkt hintereinander, Lehrer- und Elternansicht.
7. **Antippen** irgendwo beendet den Effekt sofort und zeigt den Endzustand mit Sticker.
8. **Sticker:** Der Effekt-Sticker ersetzt in dieser Ansicht den gezogenen Jugendwort-Sticker; es bleibt bei höchstens einem Sticker je Ansicht. Er zählt für die Wort-Sperre wie ein normaler Sticker.
9. **Flackern:** höchstens 3 Hell-Dunkel-Wechsel pro Sekunde, keine roten Vollbild-Blitze (Anfallsrisiko).
10. **Ruhige Fassung** (`prefers-reduced-motion`): statt der Bewegung eine dunkle Text-Tafel für 1,5 s, dann der Sticker. Texte stehen im Entwurf (`ruhig()`).
11. **Ton:** nur wenn der Ton der App an ist. Vorschläge: Tastaturklackern (Hacker), Platsch (Taube), Bong (Kapitän), Donner (Gewitter), Stempel-Knall (Für immer).
12. **Keine Systemfenster nachbauen:** kein Windows-/iPhone-Look, kein „Virus“, „Daten gelöscht“ oder Passwort. Hacker und 404 sehen erkennbar nach Spiel aus.

## 3. Speicher (ohne Datenbank)

`localStorage` je Kind, Schlüssel `lern.fx.<kind-id>`:
```
{ "tag": "2026-11-24", "heute": "hacker" | null, "letzter": "hacker",
  "ohne_effekt_lerntage": 0, "seit_immer": 0,
  "fuer_immer": [etappen-ids], "koffer": [etappen-ids] }
```
Geht der Speicher verloren, startet die Zählung neu; schlimmstenfalls kommt „Für immer“ für eine Etappe ein zweites Mal. Das ist hinnehmbar.

**Annahme zu prüfen:** Ob die App „Etappe ist jetzt sicher“ und „Etappe ist durch die Wiederholung wieder offen“ im Moment des Ergebnisses kennt (Felder in der Antwort der Wiederholung). Wenn nicht, muss der Server diese zwei Angaben in der Antwort mitliefern. Das ist der einzige mögliche Server-Teil.

## 4. Bauschritte (Vorschlag)

1. **FX-1 Motor:** Auswahl (Zufall, Tageslimit, Sicherheitsnetz, immer-Regel), Speicher, Überspringen, ruhige Fassung, Einhängen vor dem Sticker. Dazu „Für immer“ und „Koffer“ (die beiden festen).
2. **FX-2 Kleine Effekte:** Gehackt!, Fehler 404, Sterne-Glitch, Comeback, Kaffee.
3. **FX-3 Mittlere Effekte:** Glückstaube (Wischen), Möwe, Turbulenzen, Gewitter.

Der Entwurf enthält für jeden Effekt lauffähiges CSS/JS als Vorlage. Übernehmen darf der Bau gerne, aber im Stil der App (Farben, Schriften) und ohne die Steuerleiste.

## 5. Prüfpunkte für meine Nachprüfung

- „Für immer“ kommt bei jeder sicher gewordenen Etappe genau einmal; „Koffer“ bei jeder wieder geöffneten genau einmal.
- In 14 simulierten Lerntagen höchstens 1 Zufalls-Effekt je Tag, nie derselbe zweimal hintereinander, Sicherheitsnetz greift.
- Kein Effekt im Flug-Test und keiner ab dem 2. Fehler in Folge.
- Antippen beendet jeden Effekt sofort.
- Kaffee-Fleck verdeckt nie Antwort oder Lösung (360/400/820).
- Ruhige Fassung: kein Flackern, kein Wackeln.
- 360, 400 und 820 px, Tag und Nacht: Texte lesbar, nichts abgeschnitten.
