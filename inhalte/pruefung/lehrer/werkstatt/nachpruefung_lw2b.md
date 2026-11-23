# Nachprüfung „Unser Lehrplan“ – App 0.89.1 (live seit 23.11., `main` b8ffdd7 = `lernen-app` c941c33), 23.11.2026

Geprüft gegen `lehrer/werkstatt/umsetzung.md`, `nachpruefung_lw2.md` und Sebastians Rückmeldung zu 0.89.1 („Nachtrag LW-3“ in `inhalte/AUFTRAEGE.md`). Rechner **1280 × 800**, Tablet **820 × 1180**, Handy **400 × 860**; Testkind und erfundene Daten (Testsuite mit nachgebildetem Server). **Nicht** gegen die echte Seite mit echten Daten (Anmeldung mit Code nicht möglich). Bilder: `lw2b/`.

## Erledigt aus der Prüfung LW-2
- **M1** Warnung liegt auf dem Handy über dem Detail-Blatt, Knöpfe bedienbar – erledigt (Test „LW-2b M1/S1/K1/K3“ grün, nachgestellt).
- **S1** Warnungstext kurz (≤ 160 px) – erledigt. **K1** Platz-Buchstaben in Reihenfolge (3a, 3b, 3c, 3d) – erledigt (`400-start.png`). **K2** Meldung beim Zurückziehen weg – erledigt. **K3** „Teile dieses Themas“ vor den Etappen – erledigt.
- Kür-Etappe in „Wiederholung“ auf der Kinderseite startbar (LW-2b) – erledigt.
- Kein Querrollen der Seite in allen drei Breiten; Detail-Schublade 1280 rechts, Handy als Blatt von unten (`1280-detail.png`, `400-detail.png`).

## Abweichungen

### Muss (bereits als LW-3-Nachtrag beauftragt – hier nur gemessen)
- **N1 – Matrix auf dem Rechner zu klein.** 1280 × 800: Matrix beginnt bei **441 px**, sichtbar **359 px** (Ziel LW-3: ≥ 600). Darüber stapeln sich App-Kopf (72), Titelzeile „Lehrplan Kind A“ (97), Kind-Zeile mit drei Knöpfen, Reiter-Kasten und zwei Werkzeug-Zeilen. `1280-start.png`.
- **N2 – Kein Wechsel zwischen den Kindern** auf der Seite (LW-3: Kinder-Umschalter im Kopf).
- **N3 – „Einordnen“ ohne Erklärung** (LW-3: „Lehrplan von:“ + ⓘ).

### Soll
- **N4 – Name doppelt:** Titel „Lehrplan Kind A“ und darunter nochmals „Kind A · Gymnasium · Klasse 8“. Mit dem Kinder-Umschalter (N2) entfällt die Titelzeile ganz.
- **N5 – Erste Kartenzeile vom Spaltenkopf verdeckt (820, 1280).** Die Matrix springt zur Klasse des Kindes, aber die oberste Karte (hier „Intervalle“) liegt halb unter dem festen Spaltenkopf – zu sehen ist nur „↻ Wdh 2/5“, das Klassen-Schild „Kl. 8“ ist oben angeschnitten. **Änderung:** beim Springen um die Höhe des Spaltenkopfs (+ 8 px) weniger rollen. `820-start.png`, `1280-start.png`.
- **N6 – Titel in der Matrix (820, 1280) mitten im Wort gekürzt:** „Lineare Ungleichun…“, „Quadratische Gleichunge…“, „Gebrochen-rationale…“, „Potenzge-setze mit…“. Auf dem Handy (eine Spalte) stehen sie vollständig. **Änderung:** Titel auf bis zu 3 Zeilen umbrechen lassen (nur an Silbengrenzen), Kürzen nur an Wortgrenzen; voller Titel als Tooltip. Mit der größeren Matrix aus LW-3 wird es seltener.

### Kann
- **N7 – Tablet 820: sieben Spalten passen nicht** („Daten und Zufall“ rechts abgeschnitten, inneres Querrollen). Vorschlag: auf 820 Spalten 104 px statt 112 px oder die Klassen-Spalte links schmaler (Ring kleiner).

## Urteil
Alle Punkte aus der Prüfung LW-2 sind erledigt. Die Hauptschwäche ist die Seitenaufteilung auf dem Rechner (N1–N4) – genau Sebastians Rückmeldung; sie ist mit dem LW-3-Nachtrag beauftragt. N5 und N6 bitte mit LW-3 erledigen.

FERTIG: Nachprüfung 0.89.1 – 3 Muss (= LW-3-Nachtrag, gemessen), 3 Soll (Name doppelt, erste Zeile verdeckt, Titel mitten im Wort gekürzt), 1 Kann.
