# Stil-Leitblatt Advent (Entwurf 2)

Gilt für Weihnachts-Ebene, Türen, Inhaltskarten, Kalender und Motive. Quelle: `teile/` (Werte stehen dort als Konstanten).

## Grundsatz
- **Flach mit einer Schattenform.** Jede Fläche hat eine Grundfarbe, eine dunklere Schattenform unten rechts und eine schmale Glanzkante oben links. Das ist dieselbe Logik wie bei den Planeten im Regel-Universum.
- **Licht kommt immer von oben links.**
- **Keine Umrisslinien.** Ausnahmen: Perforationen, Stempel und Kabel.
- **Nichts Bedienbares in der Grafik.** Grafik-Ebenen haben `pointer-events: none` und `aria-hidden="true"`.

## Palette

| Rolle | hell | Nacht | Schatten / Glanz |
|---|---|---|---|
| Rot (Mütze, Schleife, Stiefel) | `#E5243B` | gleich | `#B3122B` / `#FF8A95` |
| Gold (Zahl, Stern, Messing) | `#FFD23F` | gleich | `#E0A40E`, `#9A6A08` / `#FFF1A8` |
| Tannengrün (Tür, Tafel, Tanne) | `#1F8A55` | `#14532D` | `#0D5232` / `#5FD39A` |
| Fell / Schnee | `#FFFFFF` | `#FFFFFF` | `#C7D3E3` (hell), `#B8C7DD` (Nacht) |
| Eis | `#DDF0FB` → `#A9D7F2` | gleich | Kante `#B5CFE2` / `#7F9BB8` |
| Tinte (Augen, Schrift auf Papier) | `#1B0C3A` | gleich | – |
| Papier (Ticket, Klappe) | `#FFFBEF`, `#F7F0DE` | Klappe `#D9CFB7` | `#E9DFC6` |
| Krampus | `#2C1214`, Kopf `#D9363E` | gleich | `#6B1E26` |
| Sommer | Meer `#2FA4E7`/`#0A6FB8`, Sand `#F3D48A`/`#D9AE5C`, Abend `#7B1E6E`→`#F0522B`→`#FF9A3C` | – | – |

**Lichterkette:** feste Folge Gold `#FFC94A` · Rot `#FF5A5F` · Warmweiß `#FFF3D1` · Grün `#3DDC84`. Nicht zufällig mischen.

**Nordlicht:**
- hell: `#10B981`, `#0EA5C6`, `#8B5CF6`, `#EC4899`
- Nacht: `#3DFFB0`, `#2DD4E6`, `#A78BFA`, `#F472B6`

## Linien, Radien, Schatten

| Was | Wert |
|---|---|
| Kabel | 1,7 px plus 0,5 px Glanzlinie |
| Stanzlinie / Perforation | Punkte 1,6 px, Abstand 9 px |
| Fellrand der Mütze | 0,4 × Kopfradius |
| Radien: Tür | 14 |
| Radien: Rahmen | 22 |
| Radien: Ticket | 16 |
| Radien: Kalender-Klappe | 11 |
| Radien: Tafel | 22 |
| Radien: Motiv | 18 (12 innen) |
| Radien: Füllungen | 9 |
| Schlagschatten Karten | `0 18px 24px #0009` (als `drop-shadow` am Wrapper, weil die Kerben per Maske entstehen) |
| Schlagschatten Klappen | `0 2px 0 #031009, 0 4px 8px #0005` |
| Glow (Lampen, Stern) | Radialverlauf statt Unschärfe-Filter |

**Glow-Werte:** hell Deckkraft 0,7 → 0, Radius 9 px · Nacht 0,95 → 0, Radius 13 px.

## Schrift
- **Space Grotesk 700:** Zahlen und Titel. Türzahl 96–112, Zeichenabstand −4.
- **ui-monospace 800:** Kopfzeilen, Laufweite 0,1–0,16 em, Großbuchstaben.
- **Goldprägung der Zahl:**
  - Verlauf `#FFF6C8` → `#FFD23F` → `#C98A0A`,
  - harter Schatten 5 px nach unten in der dunkelsten Flächenfarbe,
  - 1 px helle Kante oben links.

## Bewegung

| Was | Wert |
|---|---|
| Tür öffnen | 0,62 s `cubic-bezier(.25,.9,.3,1.12)` (leichtes Nachschwingen), Lichtstrahlen 0,5 s / 0,9 s mit 0,12 s Verzug |
| Inhalt erscheinen | 0,5 s |
| Wackeln der geschlossenen Tür | alle 3,2 s |
| Lampen | 3 Gruppen, 2,8 s, versetzt um ⅓ |
| Stern-Halo | 3,6 s |
| Nordlicht | 14 s |
| Schlitten | 6 s Flug, 8 s Pause; am 24.12. einmal 7 s |
| Schnee | eine rAF-Schleife, 3 Tiefen |

**Bewegung reduzieren:**
- Kein Schnee, kein Schlitten, keine CSS-Animation.
- Die Tür springt ohne Drehung ins Standbild „halb offen“ (`rotateY(-68deg)`, Licht an). Siehe `#s=tuer&auf=1`.

## Regeln für Motive
- **Format:** 200 × 200. Ein Held, 1–2 Requisiten, Hintergrund in 2–3 Ebenen. Das Wichtige muss auf einer 76-px-Kalenderkachel erkennbar bleiben.
- **Augen:** Tinte mit weißem Lichtpunkt oben links. Funkeln als 4-Zacken-Form `#FFF3C4`.
- **Mütze:** Immer `MU()` – dieselbe Form wie auf der Karte, damit Karte und Motive zusammenpassen.
- **Themen:** Sommer-Weihnacht, Reise, Tiere mit Charakter, leiser Humor für Teenager. Keine echten Personen, Marken, Logos oder bekannten Figuren. Keine roten Rentiernasen.
- **Krampus:** frech, nicht gruselig – runde Formen, Zwinkern, Besen und To-do-Zettel. „Negativ“ entsteht durch dunkle Rottöne, Kratzer und Hufabdruck, nicht durch Grusel.
- **Schrift im Motiv:** nur auf Bändern (Tür 6/24) oder Gegenständen (Bordkarte), höchstens 2 Wörter.
- **SVG-IDs:** mit Präfix `u`, damit mehrere Motive auf einer Seite nicht kollidieren. Keine externen Bilder, keine Schriften aus dem Netz.

## Karte (Weihnachts-Ebene)
- **Mützen:**
  - Nur auf großen Pins (Radius ≥ 12 bei 390 bzw. ≥ 15 bei 1280).
  - Kleine Pins und Pins, über denen dicht ein anderer Pin steht, bekommen ein weißes **Schneehäubchen**.
  - Der Fellrand sitzt auf dem Kopfrand, die Flagge bleibt frei. Der Zipfel fällt nach links.
  - Pins mit Abzeichen (Zahl, Haken, Stern) kippen weiter nach links (−24…−32°), sonst −6…−24°.
  - Berührt eine Mütze eine Beschriftung, wird sie bis 80 % kleiner, sonst gibt es nur das Häubchen.
- **v5:** Der aktuelle Pin trägt den Stern statt einer Mütze.
- **Freizonen:**
  - Lichterkette nur zwischen Sonne und Zoom-Knöpfen.
  - Keine Eiszapfen und kein Schnee über Sonne, Knöpfen oder Quellenzeile.
  - Feuerwerk und Stiefel nur auf freien Flächen (in der App aus `belegt`).
