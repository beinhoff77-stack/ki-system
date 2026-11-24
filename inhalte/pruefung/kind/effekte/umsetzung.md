# Vorgabe FX – Spezialeffekte im Teen-Stil: großer Vorrat + Saison

Stand 24.11.2026 · **Fassung 4** (Sebastian: mehr Vorrat, durchwechseln; Effekte nach Jahreszeit) · Daten: `effekte.json` · Entwurf: `entwurf/effekte.html` (Artefakt 0ceb2a4f-cdef-4a72-a3f0-4dcb90cfe1c4; Datum oben wählbar, Simulator über 21 Lerntage) · Bilder: `bilder/<id>-400-tag|nacht.png` (Bildfolge), `bilder/<legendary|absturz|rec>-820-tag.png`, `bilder/uebersicht-1280.png`, `bilder/rec-400-ruhig.png`

Kein App-Code, keine Datenbank, keine Namen. Alles läuft auf dem Gerät. Kein Effekt vergibt Sterne.

## 0. Kurzfassung

- **Vorrat:** 15 große und 15 kleine Effekte das ganze Jahr, dazu 8 Saison-Effekte und 4 in Reserve.
- **Durchwechseln:** Die App wählt bevorzugt, was das Kind am seltensten bzw. am längsten nicht gesehen hat. So taucht nach und nach alles auf und nichts nutzt sich ab.
- **Saison:**
  - Adventskalender jeden Tag (1.–24.12.), Nikolaus, Weihnachten (Geschenk-Drop), Silvester (Countdown).
  - Fasching, Eiersuche und Ostern (aus dem Osterdatum berechnet), Halloween.
  - In ihrem Zeitraum werden sie stark bevorzugt; Weihnachten, Ostern und Halloween kommen sicher einmal.
- **Stil, Streiche, Horror und Grenzen** wie in Fassung 3:
  - Gaming und Stream, dunkel, Neon, Glitch, Bass.
  - Streiche ≤ 1 pro Woche, Horror ≤ 2 pro Woche, nur nach Erfolg.
  - Kein Blut, keine nachgebauten Systembildschirme.

## 1. Große Effekte (15)

| Effekt | Anlass | Ablauf | Texte wörtlich | Sticker | Dauer |
|---|---|---|---|---|---|
| **Legendary Drop** · IMMER | Etappe für immer sicher · IMMER | Schwarz, Kinobalken, Scanlines → Karte mit „?“ schwebt herein, Lichtstrahlen drehen sich → Seltenheit steigt mit Bass-Schlägen: GEWÖHNLICH grau → SELTEN blau → EPISCH lila → LEGENDÄR gold → Karte dreht sich um: goldene Etappen-Karte „{ETAPPE} · FÜR IMMER“ mit Holo-Glanz, heller Blitz 110 ms, Beben, goldene Funken → Überschrift „FÜR IMMER“, Zeile, Sammlungs-Meldung | `GEWÖHNLICH` · `SELTEN` · `EPISCH` · `LEGENDÄR` · `FÜR IMMER` … | +1000 Aura | 7,5 s |
| **Checkpoint verloren · Respawn** · IMMER | Etappe wieder offen · IMMER | Bild wird grau, Herzschlag → Sechseck-Abzeichen „{ETAPPE} · CHECKPOINT“ → Risse laufen über das Abzeichen → es zerspringt in Zeitlupe in Scherben (Bass, Beben) → „CHECKPOINT VERLOREN“ in Bernstein → Farbe kehrt zurück: „RESPAWN“ in Cyan, drei Balken leuchten nacheinander → Nachbessern-Karte schiebt sich ins Bild | `CHECKPOINT VERLOREN` · `RESPAWN` · `3 RICHTIG IN FOLGE → CHECKPOINT ZURÜCK` | – | 6,5 s |
| **Account übernommen** · STREICH | 10 in Folge | Chat-Nachricht „UNBEKANNT“: „nice serie.“ → „wär schade um deine sterne.“ (Herzschlag) → App verzerrt sich, schwarz, Zeichenregen → „ACCOUNT ÜBERNOMMEN“, Sternzahl läuft auf 0, Balken „ÜBERTRAGE STERNE AN: x_sh4dow_x“ → Sterne rot auf 0, Herzschlag → Terminal: Rückverfolgung … Hacker identifiziert: DU → Sterne zählen zurück hoch → „ZUGRIFF GEWÄHRT“, Sticker | `nice serie.` · `wär schade um deine sterne.` · `ACCOUNT ÜBERNOMMEN` · `ÜBERTRAGE STERNE AN: x_sh4dow_x` · `> RÜCKVERFOLGUNG …` … | Gommemode aktiviert | 11,0 s |
| **Absturz** · STREICH | Direktflug | Buchstaben verrutschen, Knöpfe zittern (1,5 s) → App friert ein: Ladekreis, „Reagiert nicht …“, Tippen zeigt nur Kreise → schwarzes Absturz-Protokoll mit Fehlerzeilen und Hex-Kolonnen → Tafel „Die App musste beendet werden.“ mit Countdown 3–2–1 → schwarz, Neustart mit Logo und Ladebalken → Auflösung: „Reingelegt.“ und „Nichts kaputt. Nur ein Direktflug.“ | `Reagiert nicht …` · `FATAL lernen.js:404 Bordkarte 7: unerwarteter Zustand` · `fehler === 0 (erwartet: ≥ 1)` · `Die App musste beendet werden.` · `Ursache: Bordkarte 7 – unerwarteter Zustand (0 Fehler).` … | PEAK | 10,0 s |
| **REC 03:13** · HORROR | Direktflug | Videoband: Bildrauschen, „● REC 03:13 AM“, Rauschen → Untertitel: „ES HAT KEINEN FEHLER GEMACHT.“ – „NICHT EINEN.“ → zweimal blitzt für 90 ms eine weiße Maske im Rauschen auf → Schwarz, Stille → SCHOCK: Maske bildschirmfüllend, „WIR SEHEN DICH.“, Bass, Beben → „⏏ BAND AUSGEWORFEN“ → „lol. Direktflug.“ + Meldung RESPEKT | `● REC` · `03:13 AM` · `ES HAT KEINEN FEHLER GEMACHT.` · `NICHT EINEN.` · `WIR SEHEN DICH.` … | PEAK | 8,5 s |
| **Schatten im Flur** · HORROR | Flug geschafft | Licht flackert (≤ 3/s) und geht aus → dunkler Flur, Taschenlampe (folgt auch dem Finger), Herzschlag → am Ende des Flurs steht plötzlich eine Gestalt → „war da was?“ → SCHOCK: Schatten mit zwei hellen Augen rast auf den Bildschirm zu, Bass → Licht an: „MISSION COMPLETE“, Meldung | `war da was?` · `MISSION COMPLETE` · `FLUG · {Thema} · {sterne} ★` | – | 7,0 s |
| **Mission Complete** | Flug geschafft | Kinobalken, Bild zoomt langsam, Riser → „MISSION“ weiß und „COMPLETE“ gold rasen herein (Bass) → Glanz läuft über die Schrift → Werte zählen ein: Genauigkeit, Sterne, Respekt | `MISSION` · `COMPLETE` · `GENAUIGKEIT {x} %` · `STERNE +{sterne}` · `RESPEKT +1` | – | 5,5 s |
| **Big Brain Move** | Knobel richtig | dunkel violett, Scanlines → IQ-Anzeige, Nadel steigt, Zahl rattert von 100 auf 1000 → Anzeige platzt: Blitz, Bass, Funken, „IQ ∞“ → „BIG BRAIN MOVE“ | `IQ 100` · `IQ ∞` · `BIG BRAIN MOVE` | Çüş! | 4,5 s |
| **Clutch** | Comeback nach Fehler | Bild grau, Zeitlupe, Herzschlag, Kinobalken → „1 vs 3“ → drei Treffer: ✕ ✕ ✕, rechts oben „DU ⟶ FEHLER / ZWEIFEL / DRUCK“ → Farbe zurück: „CLUTCH“ in Neongrün, Bass, Funken | `1 vs 3` · `DU ⟶ FEHLER` · `DU ⟶ ZWEIFEL` · `DU ⟶ DRUCK` · `CLUTCH` | Comeback. | 4,5 s |
| **Survived** | Sturmflug gemeistert | Kinobalken, dunkler Sturm, Regen → Anzeige „STURM · STUFE 4“ mit Lebensbalken → drei Blitze, Balken fällt auf 62 %, 31 %, 9 % (grün → bernstein → rot) → Herzschlag, Regen hört auf → „SURVIVED“ in Neongrün | `STURM · STUFE 4` · `SURVIVED` · `{n} BORDKARTEN · NICHT ABGEDREHT` | Macher-Modus | 5,0 s |
| **Unter dem Eis** · HORROR | Expedition geschafft | dunkles Wasser, Sonar „TIEFE 412 M“, drei Pings → beim dritten: „KONTAKT · GROSS“ (Bernstein) → Eis reißt → SCHOCK: riesiges Auge öffnet sich bildschirmbreit, Bass, Beben → Auge schließt sich → „Es hat dich gesehen.“ – „Und lässt dich gehen.“ → Meldung EXPEDITION | `SONAR · TIEFE 412 M` · `SONAR · KONTAKT · GROSS` · `Es hat dich gesehen.` · `Und lässt dich gehen.` · `EXPEDITION · {Station} · geschafft` | Tuff, Polarprofi. | 6,5 s |
| **Boss besiegt** | Flug geschafft / Expedition geschafft | Kinobalken, dunkel → Boss-Leiste „BOSS · {Thema}“ mit Lebensbalken → 5 Treffer mit Schadenszahlen, Balken leert sich → „BOSS BESIEGT“, Funken, Beute-Meldung | `BOSS · {Thema}` · `-666 … -925` · `BOSS BESIEGT` · `BEUTE · +{sterne} ★ · Stempel {Stadt}` | – | 5,0 s |
| **Rang auf** | Flug geschafft | Rang-Abzeichen erscheint als Silber → wird Gold, dann Platin (jeweils Bass) → Funken, „RANG AUF“ | `SILBER` · `GOLD` · `PLATIN` · `RANG AUF` | – | 4,5 s |
| **Replay** | Direktflug | Kinobalken, „▶▶ REPLAY · 0,25×“ → die Bordkarten der Etappe fliegen in Zeitlupe als Liste ein, alle ✓ mit Zeit → „PERFEKTER LAUF“ | `▶▶ REPLAY · 0,25×` · `Bordkarte {n} ✓ {zeit}` · `PERFEKTER LAUF` | GOAT | 5,0 s |
| **Etwas klopft** · HORROR | Knobel richtig | dunkel → dreimal Klopfen (Bass), bei jedem Klopfen Risse im Glas von innen → eine blasse Hand drückt von innen gegen die Scheibe → „…darf ich mitrechnen?“ → „nö. knobel geknackt.“ | `…darf ich mitrechnen?` · `nö. knobel geknackt.` | Çüş! | 5,5 s |

## 2. Kleine Effekte (15)

| Effekt | Anlass | Ablauf | Texte wörtlich | Sticker | Dauer |
|---|---|---|---|---|---|
| **Sterne-Glitch** | Flug geschafft | Sternzahl rattert über das Ziel hinaus bis 4.000.000 ★ (Farbversatz rot/blau) → Zeile darunter erscheint → Zahl fällt auf den echten Wert zurück | `4.000.000 ★` · `Moment … {sterne} ★. Sorry, war aufgeregt.` | – | 2,4 s |
| **Erfolg freigeschaltet** | Saubere Landung | Meldung gleitet oben rechts herein (zwei Töne) | `ERFOLG FREIGESCHALTET` · `Saubere Landung · +20` | W | 2,5 s |
| **Hitmarker** | Saubere Landung | Fadenkreuz schwenkt ins Bild → gelber Treffer-Marker ✕ mit Klick → Feed oben rechts: „DU ⟶ LANDUNG · SAUBER“ | `DU ⟶ LANDUNG · SAUBER` | Süper! | 2,4 s |
| **Kritischer Treffer** | Knobel richtig | „KRIT 999“ springt groß heraus und steigt auf, Funken, kurzes Beben | `KRIT 999` | Sheesh! | 1,8 s |
| **Speedrun-Split** | 5 in Folge | Split-Anzeige gleitet links oben herein: SPLIT 5/5 · −0:12 · PERSÖNLICHE BESTZEIT | `SPLIT` · `5 / 5` · `−0:12` · `PERSÖNLICHE BESTZEIT` | Locked in. | 2,5 s |
| **Combo** | 5 in Folge | Speed-Linien, „5× COMBO“ rast herein | `5× COMBO` | Locked in. | 2,7 s |
| **Opa** | 5 in Folge | Opa mit Hut und Stock schlurft von links herein → bleibt stehen, dreht sich um, Popo (Hose an) Richtung Bildschirm → wackelt kurz – PUPS (Ton), Bildschirm wackelt, grüne Wolke breitet sich aus, Bild kurz grünstichig → „Pffrrrt“ → Sprechblase → Opa schlurft rechts raus | `Pffrrrt` · `„’tschuldigung. 5 in Folge – da musste was raus.“` | Locked in. | 5,0 s |
| **Unbekannt tippt …** · HORROR | Wiederholung bestanden | Chat-Nachricht von „UNBEKANNT“ gleitet herein → „…“ → „ich seh dir beim rechnen zu.“ (Herzschlag) → „sitzt immer noch. respekt.“ | `UNBEKANNT · jetzt` · `ich seh dir beim rechnen zu.` · `sitzt immer noch. respekt.` | Hält stabil. | 3,3 s |
| **Lag** | Erster Fehler des Tages | Bordkarte ruckelt und verfärbt sich kurz → „● 999 ms“ oben rechts → Zeile unten | `● 999 ms` · `Lag. Lag. Nicht du. Nächste.` | – | 2,2 s |
| **Controller-Drift** | Erster Fehler des Tages | Bordkarte driftet langsam nach rechts und zurück → Meldung | `CONTROLLER-DRIFT ERKANNT` · `Nicht deine Schuld. Nächste.` | – | 2,4 s |
| **Stream-Chat** | Knobel richtig / 5 in Folge | Chatfenster rechts, Nachrichten rauschen durch | `W` · `GOAT` · `clip that` · `Çüş` · `wie??` … | Sheesh! | 3,0 s |
| **Level up** | Saubere Landung | XP-Balken füllt sich → „LEVEL UP“ | `LVL 23` · `840 / 1000 XP` · `LEVEL UP` · `LVL 24` | Süper! | 2,8 s |
| **Clip gespeichert** | Comeback nach Fehler | kurzer weißer Auslöser-Blitz (80 ms) → Meldung „● CLIP GESPEICHERT“ | `● CLIP GESPEICHERT` · `Comeback · letzte 30 s` | Comeback. | 2,2 s |
| **Slice** | Saubere Landung | Klingen-Strich quer durchs Bild (Zisch) → Bild ruckt kurz → „Sauber zerlegt.“ | `Sauber zerlegt.` | Slay. | 2,0 s |
| **Spiegel** · HORROR | Wiederholung bestanden | ganze Ansicht springt gespiegelt, am Rand steht eine dunkle Gestalt (0,6 s) → zurück, Gestalt weg → „hast du das gesehen?“ | `hast du das gesehen?` | Hält stabil. | 2,6 s |

## 3. Saison-Effekte (8)

| Effekt | Zeitraum | Art | Ablauf | Texte | Sticker |
|---|---|---|---|---|---|
| **Adventskalender** | 1.–24. Dezember | Tagesereignis – jeden Tag sicher · klein | grüne Tür mit der Tageszahl → öffnet sich, goldenes Licht, Funken → „TÜR {Tag}“ | `TÜR {Tag}` · `+1000 Aura` | +1000 Aura |
| **Nikolaus** | 6. Dezember | Tagesereignis – jeden Tag sicher · klein | Stiefel springt ins Bild → Goldstücke fallen hinein → „NIKOLAUS WAR DA“ | `NIKOLAUS WAR DA` · `6. DEZEMBER · Stiefel voll · +Respekt` | Süper! |
| **Geschenk-Drop** | 24.–26. Dezember | sicher einmal im Zeitraum · gross | dunkel, Schnee fällt → Geschenk steigt in Seltenheit (blau, lila, gold) → Deckel fliegt, Blitz, Funken → „FROHE WEIHNACHTEN“ | `FROHE` · `WEIHNACHTEN` · `GESCHENK · Legendär · +1000 Aura` | +1000 Aura |
| **Countdown** | 31. Dezember – 1. Januar | Tagesereignis – jeden Tag sicher · gross | Kinobalken, dunkel → Countdown 10 → 1 (letzte drei gold, langsamer) → Blitz, Beben, Jahreszahl riesig, vier Feuerwerks-Funken → „NEUES JAHR · GLEICHER GOAT“ | `10 … 1` · `{Jahr}` · `NEUES JAHR · GLEICHER GOAT` | GOAT |
| **Legendäres Ei** | Karfreitag – Ostermontag (Datum berechnet) | sicher einmal im Zeitraum · gross | dunkles Ei → wackelt, Seltenheit steigt, Risse → Blitz, wird golden, Funken → „LEGENDÄRES EI“, „FROHE OSTERN“ | `LEGENDÄRES EI` · `FROHE OSTERN · +1000 Aura` | +1000 Aura |
| **Eiersuche** | 9 Tage vor Ostern – Ostermontag | Zufall, Gewicht × 4 · klein | drei Neon-Eier tauchen verteilt auf → antippen zum Einsammeln (Zähler) → alle 3 → „GOAT“, sonst „Süper!“ | `EIERSUCHE` · `{n} / 3 gefunden` | GOAT / Süper! |
| **Süßes oder Saures** · HORROR | 24.–31. Oktober | sicher einmal im Zeitraum · gross | schwarz, Kürbis mit flackerndem Gesicht → „süßes oder saures?“ → SCHOCK: Kürbis rast heran, „SAURES.“, Bass, Beben → „…war Spaß.“, Meldung | `süßes oder saures?` · `SAURES.` · `…war Spaß.` · `HALLOWEEN · Süßes · +Respekt` | Çüş! |
| **Fasching** | Weiberfastnacht – Aschermittwoch (berechnet) | Zufall, Gewicht × 4 · klein | Neon-Splitter von drei Seiten → Farben kippen stufenweise durch → „HELAU. ALAAF. EGAL.“ | `HELAU. ALAAF. EGAL.` | Peak |

**Reserve (gebaut, aus):** Kampfjet-Überflug, Gewitter, Comeback, Fehler 404.

**Varianten je Anlass (ganzjährig):**

| Anlass | Vorrat |
|---|---|
| Etappe für immer sicher · IMMER | Legendary Drop |
| Etappe wieder offen · IMMER | Checkpoint verloren · Respawn |
| 10 in Folge | Account übernommen |
| Direktflug | Absturz · REC 03:13 · Replay |
| Flug geschafft | Schatten im Flur · Mission Complete · Boss besiegt · Rang auf · Sterne-Glitch |
| Knobel richtig | Big Brain Move · Etwas klopft · Kritischer Treffer · Stream-Chat |
| Comeback nach Fehler | Clutch · Clip gespeichert |
| Sturmflug gemeistert | Survived |
| Expedition geschafft | Unter dem Eis · Boss besiegt |
| Saubere Landung | Erfolg freigeschaltet · Hitmarker · Level up · Slice |
| 5 in Folge | Speedrun-Split · Combo · Opa · Stream-Chat |
| Wiederholung bestanden | Unbekannt tippt … · Spiegel |
| Erster Fehler des Tages | Lag · Controller-Drift |

## 4. Regeln (fest)

1. **Ob ein Effekt kommt:** bei einem passenden Anlass mit 20 %. Höchstens 2 Zufalls-Effekte je Lerntag, davon höchstens 1 großer. Sicherheitsnetz: 3 Lerntage mit Anlässen ohne Effekt → beim nächsten passenden Anlass sicher einer.
2. **Welcher:** Gewichtete Auswahl aus dem ganzen Vorrat des Anlasses: Gewicht = 1 / (1 + wie oft schon gesehen); kam der Effekt in den letzten 14 Tagen, Gewicht × 0,3. So tauchen alle Effekte nach und nach auf, Neues zuerst, nichts nutzt sich ab. Nie derselbe wie zuletzt, nie dieselbe Variante wie beim letzten Mal für diesen Anlass.
3. **Saison:** Saison-Effekte sind nur in ihrem Zeitraum im Vorrat, dann mit Gewicht × 4. Tagesereignisse (Adventskalender, Nikolaus, Silvester) kommen in ihrem Zeitraum immer, je eines beim ersten, zweiten … Erfolg des Tages (am 6.12. also Adventstür und Nikolaus) und zählen nicht zum Tageslimit. Ostern und Fasching werden aus dem Osterdatum berechnet. Datum = Gerätedatum (Ortszeit). Weihnachten bleibt Weihnachten, auch im australischen Sommer. Weihnachten, Ostern und Halloween kommen sicher einmal im Zeitraum, beim ersten passenden großen Erfolg (zählen als großer Effekt des Tages).
4. **Immer:** Legendary Drop (Etappe endgültig sicher) und Respawn (Etappe wieder offen) – je Etappe einmal, nicht im Tageslimit.
5. **Horror:** nur nach Erfolg, nie bei Fehlern; ≤ 2 je Woche, ≤ 1 je Lerntag; Schock ≤ 1 s, dann Auflösung; kein Blut. Vorschlag (Meinung): nicht nach 20 Uhr.
6. **Streiche:** Streiche (Absturz, Account übernommen): sollen 6–8 s echt wirken. Kein sichtbarer Überspringen-Knopf; 1 s gedrückt halten beendet. Grenzen: nur das eigene Erscheinungsbild der App (kein iPhone-/Android-/Windows-Bildschirm nachgebaut), keine Behauptung „Daten gelöscht“, Auflösung spätestens nach 10 s, danach sind Sterne und Stand sichtbar unverändert. Höchstens 1 Streich je Woche.
7. **Nie:** im Flug-Test, ab dem 2. Fehler in Folge, zwei Effekte direkt hintereinander, Lehrer- und Elternansicht.
8. **Überspringen:**
   - Große Effekte: Knopf „Überspringen ›“ unten rechts (außer bei Streichen).
   - Kleine Effekte: Antippen.
   - Eiersuche: Antippen sammelt Eier, endet nach 4,5 s von selbst.
9. **Flackern:** ≤ 3 Wechsel pro Sekunde, Blitze ≤ 120 ms, keine roten Vollbild-Blitze; Beben ≤ 10 px.
10. **Ruhige Fassung** (Bewegung reduzieren): Text-Tafel 1,5 s und Sticker; kein Schock, kein Streich.
11. **Ton:** nur wenn der Ton der App an ist (im Entwurf Web Audio, keine Dateien).
12. **Sticker:** Der Effekt-Sticker ersetzt den gezogenen Jugendwort-Sticker dieser Ansicht.

## 5. Speicher (ohne Datenbank)

`localStorage` je Kind, Schlüssel `lern.fx.<kind-id>`:
```
{ "tag": "2026-12-06", "heute": ["advent", "nikolaus"], "letzter": "nikolaus", "letzte_variante": {"landung_direkt": "rec"},
  "gesehen": {"rec": 2, "absturz": 1}, "zuletzt": {"rec": "2026-11-30"},
  "ohne_effekt_lerntage": 0, "horror_woche": {"kw": "2026-49", "n": 1}, "streich_woche": {"kw": "2026-49", "id": "absturz"},
  "einmal": ["weihnachten-2026"], "legendaer": [etappen-ids], "respawn": [etappen-ids] }
```
Für die Saison zählt das Datum des Geräts in Ortszeit.

**Zu prüfen:**
- Liefert das Wiederholungs-Ergebnis „Etappe jetzt sicher“ und „Etappe wieder offen“? Wenn nicht, muss der Server sie mitliefern.
- `{n}` (legendäre Etappen) kommt aus dem Reise-Stand (Annahme).

## 6. Bauschritte (Vorschlag)

1. **FX-1 Motor:**
   - Auswahl: Zufall, gewichteter Vorrat, Limits, Saison mit Osterformel, Tagesereignisse, einmal im Zeitraum.
   - Speicher, Überspringen und Halten, ruhige Fassung, Ton.
   - Dazu Legendary Drop und Respawn.
2. **FX-2 kleine Effekte**, dann die Saison-Tagesereignisse (Advent, Nikolaus) vor dem 1.12.
3. **FX-3 große Effekte**, dann Weihnachten und Silvester vor dem 24.12.; Streiche zuletzt.

Der Entwurf enthält für jeden Effekt lauffähiges JS/CSS/SVG. Alle Figuren und Zeichen sind eigene Zeichnungen, keine fremden Marken. Neue Effekte lassen sich später ohne Motor-Änderung ergänzen: Eintrag in `effekte.json` plus eine Ablauf-Funktion.

**Aufwand (Annahme):** Der Motor ist einmalig. Jeder kleine Effekt ist klein, jeder große mittel. Wenn die Zeit knapp ist: zuerst Motor, Legendary, Respawn und Advent, Weihnachten, Silvester, weil die feste Termine haben.

## 7. Prüfpunkte

- Simulator 21 Lerntage ab 1.12.: jeden Tag Adventstür, am 6.12. zusätzlich Nikolaus, Weihnachten genau einmal, am 31.12. Countdown. Nie zwei große an einem Tag.
- Ostern 2027 (28.3.): Eiersuche ab 19.3., Legendäres Ei genau einmal zwischen 26. und 29.3.
- Nach 30 Lerntagen ist der Großteil des Vorrats mindestens einmal vorgekommen; kein Effekt öfter als dreimal so oft wie der seltenste.
- Streiche: kein Systembildschirm, kein „gelöscht“, Sterne am Ende unverändert, Auflösung ≤ 11 s.
- 360, 400 und 820 px, Tag und Nacht: Texte lesbar, nichts abgeschnitten.
