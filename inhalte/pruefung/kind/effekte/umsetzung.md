# Vorgabe FX – Spezialeffekte im Teen-Stil (11 große, 10 kleine)

Stand 24.11.2026 · **Fassung 3** (Sebastian: „zu kindlich – es sind Teenager“, dazu Opa-Gag und glaubhafte Absturz-/Hacker-Streiche) · Daten: `effekte.json` · Entwurf: `entwurf/effekte.html` (Artefakt 0ceb2a4f-cdef-4a72-a3f0-4dcb90cfe1c4) · Bilder: `bilder/<id>-400-tag|nacht.png` als Bildfolge über die Zeit, `bilder/<legendary|absturz|rec>-820-tag.png`, `bilder/uebersicht-1280.png`, `bilder/rec-400-ruhig.png`

Kein App-Code, keine Datenbank, keine Namen. Alles läuft auf dem Gerät. Kein Effekt vergibt Sterne.

## 0. Kurzfassung

- **Stil:** Gaming und Stream statt Kinderfernsehen. Dunkel, Neon (Cyan, Magenta, Neongrün, Gold), Glitch und Farbversatz, Scanlines, Kinobalken, kursive Blockschrift in Großbuchstaben. Ton: Bass, Riser, Herzschlag statt Piepsen. Keine Emojis, keine Comic-Tiere, kein buntes Konfetti. Einzige Ausnahme ist der Opa, der absichtlich albern ist.
- **Zwei Effekte kommen immer:**
  - **Legendary Drop:** Eine Etappe ist endgültig sicher; Karten-Ziehung, die bis LEGENDÄR steigt.
  - **Checkpoint verloren → Respawn:** Die Wiederholung öffnet eine Etappe wieder.
- **Zwei Streiche, die echt wirken sollen:**
  - **Absturz:** App ruckelt, friert ein, Absturz-Protokoll, „App musste beendet werden“, Neustart, dann „Reingelegt.“
  - **Account übernommen:** Fremder schreibt, Sterne laufen auf 0, dann stellt sich heraus: Der Hacker bist du.
  - Beide etwa 10–11 s, ohne sichtbaren Überspringen-Knopf (1 s gedrückt halten beendet).
- **Horror:** REC 03:13 (Analog-Horror-Maske), Schatten im Flur, Unter dem Eis (Auge unter dem Eis), Unbekannt tippt … (klein).
  - Schock ≤ 1 s, dann die Auflösung.
  - Kein Blut.
- **Zufall:** etwa jeder 5. passende Anlass, höchstens 2 am Lerntag (davon ≤ 1 groß), Varianten wechseln, Sicherheitsnetz nach 3 Lerntagen. Horror höchstens 2 pro Woche, Streiche höchstens 1 pro Woche.

## 1. Die 11 großen Effekte

| Effekt | Anlass | Ablauf | Texte wörtlich | Sticker | Dauer |
|---|---|---|---|---|---|
| **Legendary Drop** · IMMER | Etappe für immer sicher · IMMER | Schwarz, Kinobalken, Scanlines → Karte mit „?“ schwebt herein, Lichtstrahlen drehen sich → Seltenheit steigt mit Bass-Schlägen: GEWÖHNLICH grau → SELTEN blau → EPISCH lila → LEGENDÄR gold → Karte dreht sich um: goldene Etappen-Karte „{ETAPPE} · FÜR IMMER“ mit Holo-Glanz, heller Blitz 110 ms, Beben, goldene Funken → Überschrift „FÜR IMMER“, Zeile, Sammlungs-Meldung | `GEWÖHNLICH` · `SELTEN` · `EPISCH` · `LEGENDÄR` · `FÜR IMMER` · `{ETAPPE} SITZT · NIE WIEDER ÜBEN` … | +1000 Aura | 7.5 s |
| **Checkpoint verloren · Respawn** · IMMER | Etappe wieder offen · IMMER | Bild wird grau, Herzschlag → Sechseck-Abzeichen „{ETAPPE} · CHECKPOINT“ → Risse laufen über das Abzeichen → es zerspringt in Zeitlupe in Scherben (Bass, Beben) → „CHECKPOINT VERLOREN“ in Bernstein → Farbe kehrt zurück: „RESPAWN“ in Cyan, drei Balken leuchten nacheinander → Nachbessern-Karte schiebt sich ins Bild | `CHECKPOINT VERLOREN` · `RESPAWN` · `3 RICHTIG IN FOLGE → CHECKPOINT ZURÜCK` | – | 6.5 s |
| **Account übernommen** · STREICH | 10 in Folge | Chat-Nachricht „UNBEKANNT“: „nice serie.“ → „wär schade um deine sterne.“ (Herzschlag) → App verzerrt sich, schwarz, Zeichenregen → „ACCOUNT ÜBERNOMMEN“, Sternzahl läuft auf 0, Balken „ÜBERTRAGE STERNE AN: x_sh4dow_x“ → Sterne rot auf 0, Herzschlag → Terminal: Rückverfolgung … Hacker identifiziert: DU → Sterne zählen zurück hoch → „ZUGRIFF GEWÄHRT“, Sticker | `nice serie.` · `wär schade um deine sterne.` · `ACCOUNT ÜBERNOMMEN` · `ÜBERTRAGE STERNE AN: x_sh4dow_x` · `> RÜCKVERFOLGUNG …` · `> QUELLE GEFUNDEN` … | Gommemode aktiviert | 11.0 s |
| **Absturz** · STREICH | Direktflug | Buchstaben verrutschen, Knöpfe zittern (1,5 s) → App friert ein: Ladekreis, „Reagiert nicht …“, Tippen zeigt nur Kreise → schwarzes Absturz-Protokoll mit Fehlerzeilen und Hex-Kolonnen → Tafel „Die App musste beendet werden.“ mit Countdown 3–2–1 → schwarz, Neustart mit Logo und Ladebalken → Auflösung: „Reingelegt.“ und „Nichts kaputt. Nur ein Direktflug.“ | `Reagiert nicht …` · `FATAL lernen.js:404 Bordkarte 7: unerwarteter Zustand` · `fehler === 0 (erwartet: ≥ 1)` · `Die App musste beendet werden.` · `Ursache: Bordkarte 7 – unerwarteter Zustand (0 Fehler).` · `Neustart in 3 …` … | PEAK | 10.0 s |
| **REC 03:13** · HORROR | Direktflug | Videoband: Bildrauschen, „● REC 03:13 AM“, Rauschen → Untertitel: „ES HAT KEINEN FEHLER GEMACHT.“ – „NICHT EINEN.“ → zweimal blitzt für 90 ms eine weiße Maske im Rauschen auf → Schwarz, Stille → SCHOCK: Maske bildschirmfüllend, „WIR SEHEN DICH.“, Bass, Beben → „⏏ BAND AUSGEWORFEN“ → „lol. Direktflug.“ + Meldung RESPEKT | `● REC` · `03:13 AM` · `ES HAT KEINEN FEHLER GEMACHT.` · `NICHT EINEN.` · `WIR SEHEN DICH.` · `⏏ BAND AUSGEWORFEN` … | PEAK | 8.5 s |
| **Schatten im Flur** · HORROR | Flug geschafft | Licht flackert (≤ 3/s) und geht aus → dunkler Flur, Taschenlampe (folgt auch dem Finger), Herzschlag → am Ende des Flurs steht plötzlich eine Gestalt → „war da was?“ → SCHOCK: Schatten mit zwei hellen Augen rast auf den Bildschirm zu, Bass → Licht an: „MISSION COMPLETE“, Meldung | `war da was?` · `MISSION COMPLETE` · `FLUG · {Thema} · {sterne} ★` | – | 7.0 s |
| **Mission Complete** | Flug geschafft | Kinobalken, Bild zoomt langsam, Riser → „MISSION“ weiß und „COMPLETE“ gold rasen herein (Bass) → Glanz läuft über die Schrift → Werte zählen ein: Genauigkeit, Sterne, Respekt | `MISSION` · `COMPLETE` · `GENAUIGKEIT {x} %` · `STERNE +{sterne}` · `RESPEKT +1` | – | 5.5 s |
| **Big Brain Move** | Knobel richtig | dunkel violett, Scanlines → IQ-Anzeige, Nadel steigt, Zahl rattert von 100 auf 1000 → Anzeige platzt: Blitz, Bass, Funken, „IQ ∞“ → „BIG BRAIN MOVE“ | `IQ 100` · `IQ ∞` · `BIG BRAIN MOVE` | Çüş! | 4.5 s |
| **Clutch** | Comeback nach Fehler | Bild grau, Zeitlupe, Herzschlag, Kinobalken → „1 vs 3“ → drei Treffer: ✕ ✕ ✕, rechts oben „DU ⟶ FEHLER / ZWEIFEL / DRUCK“ → Farbe zurück: „CLUTCH“ in Neongrün, Bass, Funken | `1 vs 3` · `DU ⟶ FEHLER` · `DU ⟶ ZWEIFEL` · `DU ⟶ DRUCK` · `CLUTCH` | Comeback. | 4.5 s |
| **Survived** | Sturmflug gemeistert | Kinobalken, dunkler Sturm, Regen → Anzeige „STURM · STUFE 4“ mit Lebensbalken → drei Blitze, Balken fällt auf 62 %, 31 %, 9 % (grün → bernstein → rot) → Herzschlag, Regen hört auf → „SURVIVED“ in Neongrün | `STURM · STUFE 4` · `SURVIVED` · `{n} BORDKARTEN · NICHT ABGEDREHT` | Macher-Modus | 5.0 s |
| **Unter dem Eis** · HORROR | Expedition geschafft | dunkles Wasser, Sonar „TIEFE 412 M“, drei Pings → beim dritten: „KONTAKT · GROSS“ (Bernstein) → Eis reißt → SCHOCK: riesiges Auge öffnet sich bildschirmbreit, Bass, Beben → Auge schließt sich → „Es hat dich gesehen.“ – „Und lässt dich gehen.“ → Meldung EXPEDITION | `SONAR · TIEFE 412 M` · `SONAR · KONTAKT · GROSS` · `Es hat dich gesehen.` · `Und lässt dich gehen.` · `EXPEDITION · {Station} · geschafft` | Tuff, Polarprofi. | 6.5 s |

## 2. Die 10 kleinen Effekte

| Effekt | Anlass | Ablauf | Texte wörtlich | Sticker | Dauer |
|---|---|---|---|---|---|
| **Sterne-Glitch** | Flug geschafft | Sternzahl rattert über das Ziel hinaus bis 4.000.000 ★ (Farbversatz rot/blau) → Zeile darunter erscheint → Zahl fällt auf den echten Wert zurück | `4.000.000 ★` · `Moment … {sterne} ★. Sorry, war aufgeregt.` | – | 2.4 s |
| **Erfolg freigeschaltet** | Saubere Landung | Meldung gleitet oben rechts herein (zwei Töne) | `ERFOLG FREIGESCHALTET` · `Saubere Landung · +20` | W | 2.5 s |
| **Hitmarker** | Saubere Landung | Fadenkreuz schwenkt ins Bild → gelber Treffer-Marker ✕ mit Klick → Feed oben rechts: „DU ⟶ LANDUNG · SAUBER“ | `DU ⟶ LANDUNG · SAUBER` | Süper! | 2.4 s |
| **Kritischer Treffer** | Knobel richtig | „KRIT 999“ springt groß heraus und steigt auf, Funken, kurzes Beben | `KRIT 999` | Sheesh! | 1.8 s |
| **Speedrun-Split** | 5 in Folge | Split-Anzeige gleitet links oben herein: SPLIT 5/5 · −0:12 · PERSÖNLICHE BESTZEIT | `SPLIT` · `5 / 5` · `−0:12` · `PERSÖNLICHE BESTZEIT` | Locked in. | 2.5 s |
| **Combo** | 5 in Folge | Speed-Linien, „5× COMBO“ rast herein | `5× COMBO` | Locked in. | 2.7 s |
| **Opa** | 5 in Folge | Opa mit Hut und Stock schlurft von links herein → bleibt stehen, dreht sich um, Popo (Hose an) Richtung Bildschirm → wackelt kurz – PUPS (Ton), Bildschirm wackelt, grüne Wolke breitet sich aus, Bild kurz grünstichig → „Pffrrrt“ → Sprechblase → Opa schlurft rechts raus | `Pffrrrt` · `„’tschuldigung. 5 in Folge – da musste was raus.“` | Locked in. | 5.0 s |
| **Unbekannt tippt …** · HORROR | Wiederholung bestanden | Chat-Nachricht von „UNBEKANNT“ gleitet herein → „…“ → „ich seh dir beim rechnen zu.“ (Herzschlag) → „sitzt immer noch. respekt.“ | `UNBEKANNT · jetzt` · `ich seh dir beim rechnen zu.` · `sitzt immer noch. respekt.` | Hält stabil. | 3.3 s |
| **Lag** | Erster Fehler des Tages | Bordkarte ruckelt und verfärbt sich kurz → „● 999 ms“ oben rechts → Zeile unten | `● 999 ms` · `Lag. Lag. Nicht du. Nächste.` | – | 2.2 s |
| **Controller-Drift** | Erster Fehler des Tages | Bordkarte driftet langsam nach rechts und zurück → Meldung | `CONTROLLER-DRIFT ERKANNT` · `Nicht deine Schuld. Nächste.` | – | 2.4 s |

**Reserve (gebaut, aus):** Kampfjet-Überflug, Gewitter, Comeback, Fehler 404.

**Varianten je Anlass:**

| Anlass | Varianten |
|---|---|
| Etappe für immer sicher · IMMER | Legendary Drop |
| Etappe wieder offen · IMMER | Checkpoint verloren · Respawn |
| 10 in Folge | Account übernommen |
| Direktflug | Absturz · REC 03:13 |
| Flug geschafft | Schatten im Flur · Mission Complete · Sterne-Glitch |
| Knobel richtig | Big Brain Move · Kritischer Treffer |
| Comeback nach Fehler | Clutch |
| Sturmflug gemeistert | Survived |
| Expedition geschafft | Unter dem Eis |
| Saubere Landung | Erfolg freigeschaltet · Hitmarker |
| 5 in Folge | Speedrun-Split · Combo · Opa |
| Wiederholung bestanden | Unbekannt tippt … |
| Erster Fehler des Tages | Lag · Controller-Drift |

## 3. Regeln (fest)

1. **Zufall:** Bei einem passenden Anlass kommt mit 20 % ein Effekt; die Variante entscheidet der Zufall. Nie dieselbe Variante wie beim letzten Mal für diesen Anlass, nie derselbe Effekt wie zuletzt.
2. **Höchstens 2 Zufalls-Effekte je Lerntag, davon höchstens 1 großer.**
3. **Sicherheitsnetz:** 3 Lerntage mit passenden Anlässen ohne Effekt → beim nächsten passenden Anlass sicher einer.
4. **Immer:** Legendary Drop und Respawn – je Etappe einmal, nicht im Tageslimit. Mehrere Etappen auf einmal: ein Durchlauf mit Zahl („3 Etappen legendär“). Wird der Flug dadurch golden: zusätzlich `FLUG GOLDEN · {Land} komplett`.
5. **Horror:** nur nach Erfolg, nie bei Fehlern; höchstens 2 je Woche, 1 je Lerntag. Schock ≤ 1 s, dann Auflösung. Kein Blut, keine Verletzung, keine Schreie. Vorschlag (Meinung): nicht nach 20 Uhr.
6. **Streiche (Absturz, Account übernommen):**
   - Höchstens 1 je Woche, nie zwei Wochen hintereinander derselbe.
   - Sie sollen 6–8 s glaubhaft sein, deshalb kein Überspringen-Knopf; 1 s gedrückt halten beendet.
   - Grenzen, bewusst gesetzt:
     - Nur das eigene Aussehen der App; kein nachgebauter iPhone-, Android- oder Windows-Bildschirm. Sonst drückt das Kind womöglich Geräte-Knöpfe oder setzt das Handy zurück.
     - Nie „Daten gelöscht“ oder „Lernstand weg“.
     - Die Sterne dürfen im Hacker-Streich auf 0 laufen, kommen aber im selben Effekt sichtbar zurück.
     - Auflösung spätestens nach 11 s.
7. **Nie:** im Flug-Test, ab dem 2. Fehler in Folge, zwei Effekte direkt hintereinander, Lehrer- und Elternansicht.
8. **Überspringen:**
   - Große Effekte: Knopf „Überspringen ›“ unten rechts (außer bei Streichen).
   - Kleine Effekte: Antippen.
9. **Flackern und Blitze:** höchstens 3 Hell-Dunkel-Wechsel pro Sekunde, Blitze ≤ 120 ms, keine roten Vollbild-Blitze. Beben ≤ 10 px.
10. **Ruhige Fassung** (Gerät auf „Bewegung reduzieren“): Text-Tafel 1,5 s und Sticker; kein Schock, kein Streich (Bild `rec-400-ruhig.png`).
11. **Ton:** nur wenn der Ton der App an ist. Im Entwurf mit Web Audio erzeugt (Bass, Riser, Herzschlag, Rauschen, Pups) – keine Dateien nötig.
12. **Sticker:** Der Effekt-Sticker ersetzt in dieser Ansicht den gezogenen Jugendwort-Sticker (höchstens einer je Ansicht).

## 4. Speicher (ohne Datenbank)

`localStorage` je Kind, Schlüssel `lern.fx.<kind-id>`:
```
{ "tag": "2026-11-24", "heute": ["rec"], "letzter": "rec", "letzte_variante": {"landung_direkt": "rec"},
  "ohne_effekt_lerntage": 0, "horror_woche": {"kw": "2026-48", "n": 1}, "streich_woche": {"kw": "2026-48", "id": "absturz"},
  "legendaer": [etappen-ids], "respawn": [etappen-ids] }
```

**Zu prüfen:**
- Liefert das Wiederholungs-Ergebnis die Angaben „Etappe jetzt sicher“ und „Etappe wieder offen“? Wenn nicht, muss der Server sie mitliefern.
- Die Zahl `{n}` legendäre Etappen kommt aus dem Reise-Stand (Annahme).
- Der Hacker-Streich zeigt die echte Sternzahl des Kindes.

## 5. Bauschritte (Vorschlag)

1. **FX-1 Motor + Legendary Drop + Respawn:** Auswahl (Zufall, Varianten, Limits für Tag, groß, Horror und Streich, Sicherheitsnetz), Speicher, Überspringen und Halten, ruhige Fassung, Ton, Einhängen vor dem Sticker.
2. **FX-2 die 10 kleinen.**
3. **FX-3 die übrigen 9 großen**, Streiche zuletzt.

Der Entwurf enthält für jeden Effekt lauffähiges JS/CSS/SVG als Vorlage. Maske, Opa, Karte und Anzeigen sind eigene Zeichnungen, keine fremden Figuren oder Marken. Meldungen wie „Erfolg freigeschaltet“ sind allgemein gehalten, nicht im Look einer Konsole.

**Aufwand (Annahme):** FX-1 etwa die Größe des Jugendwort-Auftrags, FX-2 klein, FX-3 der größte Teil.

## 6. Prüfpunkte für meine Nachprüfung

- Legendary und Respawn bei jeder betroffenen Etappe genau einmal.
- 14 simulierte Lerntage: ≤ 2 Effekte je Tag, ≤ 1 groß, Horror ≤ 2 und Streich ≤ 1 je Woche, nie dieselbe Variante zweimal hintereinander.
- Streiche: kein Systembildschirm, kein „gelöscht“, Sterne am Ende unverändert, Auflösung ≤ 11 s, 1 s Halten beendet.
- Nichts im Flug-Test, nichts ab dem 2. Fehler in Folge, kein Horror bei Fehlern.
- Flackern ≤ 3/s; ruhige Fassung ohne Schock und ohne Streich.
- 360, 400 und 820 px, Tag und Nacht: Texte lesbar, nichts abgeschnitten.
