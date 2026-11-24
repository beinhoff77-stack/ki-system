# Vorgabe FX – Spezialeffekte: 10 große, 10 kleine (mit Horror)

Stand 24.11.2026 (Fassung 2: spektakulärer, länger, mit Horror – Wünsche Sebastian) · Daten: `effekte.json` · Entwurf zum Anklicken: `entwurf/effekte.html` (Artefakt 0ceb2a4f-cdef-4a72-a3f0-4dcb90cfe1c4) · Bilder: `bilder/<effekt>-400-tag|nacht.png` (Bildfolge über die Zeit), `bilder/<clown|tresor|hacker>-820-tag.png`, `bilder/uebersicht-1280.png`, `bilder/clown-400-ruhig.png`

Kein App-Code, keine Datenbank, keine Namen. Alles läuft auf dem Gerät. Kein Effekt vergibt Sterne.

## 0. Kurzfassung

- **10 große Effekte:** kleine Filme von 4–7,5 s mit Ton, Beben, Teilchen und einer Pointe; Knopf „Überspringen ›“.
- **10 kleine Effekte:** 2–3,6 s; Antippen überspringt.
- **Zwei Effekte kommen immer:**
  - **Für immer:** Raketenstart ins eigene Sternbild, wenn eine Etappe endgültig sicher ist.
  - **Koffer-Chaos:** wenn die Wiederholung eine Etappe wieder öffnet.
- **Alle anderen kommen per Zufall:**
  - etwa jeder 5. passende Anlass, höchstens 2 am Lerntag, davon höchstens 1 großer;
  - je Anlass wechseln die Varianten, nie dieselbe zweimal hintereinander;
  - Sicherheitsnetz nach 3 Lerntagen ohne Effekt.
- **Horror:** Der Clown, Stromausfall mit Geist und die Riesenkrake (groß), Knochenhand und Spinne (klein).
  - Schock höchstens 1 s, dann sofort die Pointe (Lachen, Schild, Konfetti).
  - Kein Blut.
  - Höchstens 2 je Woche, nur nach Erfolg.
- **4 Reserve-Effekte** sind gebaut, aber aus: Kampfjet, Applaus, Rückspulen, Gewitter. Sie sind zum Austauschen da.

## 1. Die 10 großen Effekte

| # | Effekt | Anlass | Ablauf (Kurz) | Texte wörtlich | Sticker | Dauer |
|---|---|---|---|---|---|---|
| G1 | **Für immer – Raketenstart** · IMMER | Etappe endgültig sicher | Nachthimmel mit dem eigenen Sternbild (alle sicheren Etappen) → Rakete „{ETAPPE}“ auf der Rampe → Countdown 3-2-1 → START: Flamme, Rauch, Beben, Aufstieg → Explosion zu einem neuen Stern, goldene Linie ins Sternbild → Text | `3` `2` `1` `START!` · `FÜR IMMER` · `{Etappe} sitzt – und leuchtet jetzt in deinem Sternbild.` · `Muss nie wieder geübt werden.` · `★ {n} Etappen für immer` | +1000 Aura | 7,5 s |
| G2 | **Koffer-Chaos** · IMMER | Wiederholung mit 2 Fehlern → Etappe wieder offen | Rundumleuchte, Warnband, Sirene → 3 Koffer auf dem Band, der mit „{ETAPPE}“ wackelt und bläht sich auf → KABUMM (Blitz 110 ms, Beben): Deckel fliegt, Socken, T-Shirt, Gummiente und Ziffern fliegen → Riesensocke klatscht an die Scheibe und rutscht ab → Teile fliegen in 3 leere Kreise → Nachbessern-Karte | `⚠ STÖRUNG · GEPÄCKBAND 3 ⚠` · `Dein Koffer ist aufgegangen!` · `Sammeln wir’s wieder ein.` · `3 richtige in Folge – dann ist alles wieder drin.` | – | 6,5 s |
| G3 | **Gehackt! (Matrix)** | 10 in Folge richtig | App-Bild verzerrt → schwarz, grüner Zeichenregen → Terminal tippt, Balken 0–100 % → Warnbalken bernstein → wird grün → Auflösung | `> VERBINDE MIT MATHE-ZENTRALE …` · `> UMGEHE FIREWALL … OK` · `> ENTSCHLÜSSELE BRÜCHE … OK` · `⚠ FIREWALL DURCHBROCHEN` · `ZUGRIFF GEWÄHRT` · `> HACKER IDENTIFIZIERT: DU` · `> GRUND: 10 VON 10 RICHTIG` | Gommemode aktiviert | 6 s |
| G4 | **Der Clown** 👁 Horror | Direktflug | Licht aus, verstimmte Spieluhr → roter Luftballon steigt → Schrift → Stille, einmal schwarz → **SCHOCK:** Clown-Gesicht bildschirmfüllend, „BUH!“, Beben → Clown schrumpft, lacht, hupt mit der Nase → Schild, Konfetti | `Psst … ganz ohne Fehler?` · `BUH!` · `HAHAHA` · `Direktflug? Respekt. 🎩` | PEAK | 6,5 s |
| G5 | **Stromausfall** 👁 Horror | Flug geschafft | Licht flackert und geht aus → Taschenlampen-Kegel (folgt auch dem Finger) → zwei gelbe Augen blinken → **SCHOCK:** Geist springt ins Bild, „BUUUH!“ → Licht an, Geist kichert, Konfetti | `BUUUH!` · `👻 Hihi – erschrocken? Glückwunsch zum Flug!` | Flug-Sticker | 5,8 s |
| G6 | **Feuerwerk** | Flug geschafft | Himmel dunkelt → 5 Raketen pfeifen hoch und explodieren in 5 Farben | – | Flug-Sticker | 4,5 s |
| G7 | **Big Brain** | Knobel richtig | violetter Schein → Gehirn wächst in 6 Pulsen, Blitze zucken → Blitz, Gehirn platzt in Konfetti | `BIG BRAIN` | Çüş! | 3,6 s |
| G8 | **Phönix** | Comeback (nach Fehler 3 in Folge richtig) | Glut, Flammen steigen → Feuervogel steigt groß auf (Fanfare) | `AUFERSTANDEN` | Comeback. | 3,5 s |
| G9 | **Tornado** | Sturmflug gemeistert | Himmel dunkelt → Wirbelsturm mit Kuh, Koffer, Geodreieck, Kaktus, Stuhl, Huhn → alles fliegt raus, klart auf | `DURCHGEZOGEN` | Macher-Modus | 3,6 s |
| G10 | **Riesenkrake** 👁 Horror | Expedition geschafft | Eiswasser steigt → 4 Fangarme schießen hoch → **SCHOCK:** Arm klatscht an die Scheibe, „KLATSCH!“ → Kopf taucht auf mit Schild → alles taucht ab | `KLATSCH!` · `🐙 Respekt, Polarprofi. Ich tauche wieder ab.` | Tuff, Polarprofi. | 5,6 s |

## 2. Die 10 kleinen Effekte

| # | Effekt | Anlass | Ablauf | Texte wörtlich | Sticker | Dauer |
|---|---|---|---|---|---|---|
| K1 | Fehler 404 | Direktflug | 2 Flacker-Wechsel → Tafel „404“ mit Farbversatz → bricht weg | `404` · `FEHLER NICHT GEFUNDEN` | Çüş – null Fehler. | 2,2 s |
| K2 | Sterne-Glitch | Flug geschafft | Sterne rattern bis 4.000.000 ★ → fallen zurück | `Moment … {sterne} ★. Sorry, war aufgeregt.` | Flug-Sticker | 2,4 s |
| K3 | Glückstaube | saubere Landung | Klecks aufs Glas, wegwischen | `Bringt Glück! Wegwischen.` | W | bis 4 s |
| K4 | Knochenhand 👁 | saubere Landung | Boden reißt, Skeletthand schießt hoch, winkt, sinkt | `💀 Saubere Landung? Knochenstark.` | Süper! | 2,8 s |
| K5 | Möwe | Knobel richtig | Möwe klatscht an die Scheibe, Federn, rutscht ab | – | Sheesh! | 2,2 s |
| K6 | Turbulenzen | 5 in Folge | Beben, Sauerstoffmasken, Kapitän | `Hier spricht euer Kapitän: Ihr rechnet zu schnell – wir müssen bremsen.` | Locked in. | 2,4 s |
| K7 | Nitro-Combo | 5 in Folge | Speed-Linien, „5× COMBO“ rast herein, Flammenschweif | `5×` · `COMBO` | Locked in. | 2,9 s |
| K8 | Spinne 👁 | Wiederholung bestanden | Spinne saust am Faden herunter, Schild, klettert hoch | `🕸️ Sitzt noch!` | Hält stabil. | 2,8 s |
| K9 | Kaffee verschüttet | erster Fehler des Tages | Fleck an der Ecke der Bordkarte, Kapitän | `Ups – mein Kaffee. Daran lag’s. Nächste!` | – | 1,8 s |
| K10 | Kapitän niest | erster Fehler des Tages | „Haaa… TSCHI!“, Tröpfchen, Scheibenwischer | `Haaa… haaaa…` · `TSCHI!` · `Gesundheit! Daran lag’s. Nächste!` | – | 2,9 s |

**Reserve (gebaut, aus):** Kampfjet-Überflug (Direktflug), Applaus an Bord (saubere Landung), Rückspulen (Comeback), Gewitter (Sturmflug). Halbjährlich kann ein abgenutzter Effekt gegen einen aus der Reserve getauscht werden.

**Abwechslung je Anlass:**

| Anlass | Varianten |
|---|---|
| Direktflug | Clown · 404 |
| saubere Landung | Taube · Knochenhand |
| Sturmflug | Tornado |
| Flug geschafft | Stromausfall · Feuerwerk · Glitch |
| Knobel richtig | Big Brain · Möwe |
| 5 in Folge | Turbulenzen · Nitro |
| 10 in Folge | Gehackt! |
| Comeback | Phönix |
| Wiederholung bestanden | Spinne |
| Expedition geschafft | Krake |
| erster Fehler | Kaffee · Niesen |

## 3. Regeln (fest)

1. **Zufall:** Bei einem passenden Anlass kommt mit 20 % ein Effekt; welche Variante, entscheidet der Zufall. Nie dieselbe Variante wie beim letzten Mal für diesen Anlass, nie derselbe Effekt wie zuletzt.
2. **Höchstens 2 Zufalls-Effekte je Lerntag, davon höchstens 1 großer.**
3. **Sicherheitsnetz:** Gab es an 3 Lerntagen passende Anlässe, aber keinen Effekt, kommt beim nächsten passenden Anlass sicher einer.
4. **Immer:** „Für immer“ und „Koffer“ – je Etappe einmal, nicht im Tageslimit. Mehrere Etappen auf einmal: ein Durchlauf mit Zahl (`3 Etappen sitzen.` / `2 Koffer sind aufgegangen – sammeln wir’s wieder ein.`). Wird der Flug dadurch golden: zusätzlich `Flug golden! {Land} ist komplett.`
5. **Horror:**
   - Nur nach Erfolg, nie bei Fehlern; höchstens 2 je Woche, höchstens 1 je Lerntag.
   - Schock höchstens 1 s, danach sofort die Pointe.
   - Kein Blut, keine Verletzung, keine Schreie. Der Clown ist schick und gruselig, nicht verstümmelt.
   - Vorschlag (Meinung): nicht nach 20 Uhr, damit niemand damit ins Bett geht.
6. **Nie:** im Flug-Test, ab dem 2. Fehler in Folge, zwei Effekte direkt hintereinander, Lehrer- und Elternansicht.
7. **Überspringen:**
   - Große Effekte: Knopf „Überspringen ›“ oben rechts. Antippen anderswo bricht nicht ab, damit ein Kind nicht aus Versehen den Clown wegtippt.
   - Kleine Effekte: Antippen irgendwo.
8. **Flackern und Blitze:**
   - Höchstens 3 Hell-Dunkel-Wechsel pro Sekunde, keine roten Vollbild-Blitze (Anfallsrisiko).
   - Beben höchstens 10 px.
9. **Ruhige Fassung** (Gerät auf „Bewegung reduzieren“): Text-Tafel 1,5 s und Sticker, kein Schock, kein Flackern (Bild `clown-400-ruhig.png`).
10. **Ton:** nur wenn der Ton der App an ist.
    - Im Entwurf erzeugt mit Web Audio (Piep, Grollen, Sirene, Spieluhr, Hupe); keine Tondateien nötig.
    - Ohne Ton funktionieren alle Effekte.
11. **Sticker:** Der Effekt-Sticker ersetzt in dieser Ansicht den gezogenen Jugendwort-Sticker (höchstens einer je Ansicht).
12. **Keine Systemfenster nachbauen:** Hacker und 404 sehen nach Spiel aus, nicht nach Windows oder iPhone. Kein „Virus“, kein „Daten gelöscht“.

## 4. Speicher (ohne Datenbank)

`localStorage` je Kind, Schlüssel `lern.fx.<kind-id>`:
```
{ "tag": "2026-11-24", "heute": ["clown"], "letzter": "clown", "letzte_variante": {"landung_direkt": "clown"},
  "ohne_effekt_lerntage": 0, "horror_woche": {"kw": "2026-48", "n": 1},
  "fuer_immer": [etappen-ids], "koffer": [etappen-ids], "sternbild_n": 12 }
```

**Zu prüfen:**
- Kennt die App im Wiederholungs-Ergebnis die Angaben „Etappe jetzt sicher“ und „Etappe wieder offen“? Wenn nicht, muss der Server sie mitliefern.
- Für die Zahl im Sternbild (`{n}`) braucht die App die Anzahl der sicheren Etappen. Die ist vermutlich aus dem Reise-Stand ablesbar (Annahme).

## 5. Bauschritte (Vorschlag)

1. **FX-1 Motor und die zwei festen Effekte:** Auswahl (Zufall, Varianten, Tageslimit, groß/klein, Horror-Wochenlimit, Sicherheitsnetz), Speicher, Überspringen, ruhige Fassung, Ton-Schalter, Einhängen vor dem Sticker. Dazu Für immer und Koffer-Chaos.
2. **FX-2 Die 10 kleinen Effekte.**
3. **FX-3 Die übrigen 8 großen Effekte:** Gehackt!, Clown, Stromausfall, Feuerwerk, Big Brain, Phönix, Tornado, Krake.

Der Entwurf enthält für jeden Effekt lauffähiges JS/CSS/SVG als Vorlage. Übernehmen darf der Bau gerne, im Stil der App und ohne die Steuerleiste. Clown, Geist, Krake, Rakete und Koffer sind eigene SVG-Zeichnungen, keine fremden Figuren.

**Aufwand (Annahme):** FX-1 etwa die Größe des Jugendwort-Auftrags; FX-2 klein; FX-3 der größte Brocken, weil acht Filme mit Ablauf, Ton und Teilchen.

## 6. Prüfpunkte für meine Nachprüfung

- „Für immer“ und „Koffer“ kommen bei jeder betroffenen Etappe genau einmal.
- Simulierte 14 Lerntage: höchstens 2 Effekte je Tag, höchstens 1 großer, Horror höchstens 2 je Woche, nie dieselbe Variante zweimal hintereinander.
- Nichts im Flug-Test, nichts ab dem 2. Fehler in Folge, kein Horror bei Fehlern.
- „Überspringen ›“ beendet jeden großen Effekt sofort; Antippen jeden kleinen.
- Flackern höchstens 3 Wechsel pro Sekunde; ruhige Fassung ohne Schock.
- Kaffee und Niesen verdecken nie die Lösung.
- 360, 400 und 820 px, Tag und Nacht: Texte lesbar, nichts abgeschnitten.
