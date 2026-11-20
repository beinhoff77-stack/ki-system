# Nachprüfung 3: Bau-Auftrag LB (App 0.82.0)

Geprüft: `origin/main` a6639df (App 0.82.0, Merge von `lernen-app`). Vorgabe: `umsetzung-lb.md`, Entwurf `entwurf/lehrplan-klasse-4-stufen.html`. Bericht des Bau-Chats: `inhalte/postfach/bau-lehrer.md` (lernen-app).

**Wie geprüft:** Playwright (Chromium) bei 400 × 860, 820 × 1180, 1280 × 900, angemeldet als Lehrer. Das Testkind (Gym 8) ist erfunden. Lehrstoff aus der echten Themenliste (`inhalte/themenliste.json`, 95 Flüge, mit LB-4-Feldern; stimmt mit der Datenbank überein, dort nur Lehrstoff gelesen). Lernstand des Testkinds erfunden: alle fünf Stufen kommen vor, auch „gesetzt: wiederholen“. Skript `n3/n3.test.cjs`, Messwerte `n3/mess.json`, Bilder `n3/bilder/`.

## 1. „Fertig, wenn“ aus umsetzung-lb.md

| # | Punkt | Ergebnis | Gesehen | Bild |
|---|---|---|---|---|
| 1 | „Realschule Kl. 7“ zeigt genau die 18 Themen mit RS 7 | **erfüllt** | 18 Zeilen (15 im Plan/gekonnt, 3 „+“): gemeinsame und Zusatzthemen gemischt in RS-Lehrplan-Reihenfolge, Überschriften M7 1 … M7 8. Kein Hinweis „vorläufig wie Gymnasium“ mehr, weil die RS-Reihenfolge jetzt da ist. Keine andere Klasse in der Liste. | `1280-klasse-rs7.jpg`, `820-klasse-rs7.jpg` |
| 2 | Gym 8 in Lehrplan-Reihenfolge mit Lernbereich-Überschriften | **erfüllt** | M8 1 Funktion und Term → M8 2 Lineare Funktionen (Lineare Funktionen, Intervalle, Lineare Ungleichungen) → M8 3 → M8 4 → M8 5 → M8 6 → M8 7, Reihenfolge 1–14. Kopf „Gym 8: 12 von 14 Themen im Plan oder schon gekonnt“ mit Balken. Eingeplantes bleibt an seinem Platz. | `1280-klasse-gym8.jpg`, `820-klasse-gym8.jpg` |
| 3 | Jede Themenzeile zeigt ◉ ↻ ▶ ○ + (Lehrplan beide Ansichten, Plan, Lehrplan-Übersicht) | **erfüllt** | Plan links je Ort und aufgeklappt je Flug; „Nach Klasse“; „Nach Themengebiet“; Lehrplan-Übersicht (Spalte je Kind). | `1280-plan-blick.jpg`, `1280-lehrplan.jpg` |
| 4 | Alle Knöpfe im Plan erreichbar | **erfüllt** | Aufgeklappt: Lernen · Kann er – aber wiederholen · Kann er komplett · Aus dem Plan nehmen; bei ◉ zusätzlich „Wieder in die Wiederholung“; bei „+“ „+ In den Plan“. Links (je Flug) und rechts gleich. | `820-klasse-gym8-auf.jpg`, `820-klasse-gym8-komplett-auf.jpg`, `820-links-ort-auf.jpg` |
| 5 | 6 Themen aus Gym 7 in einem Schritt auf „wiederholen“ | **teilweise geprüft** | Auswahlmodus: 2 Häkchen → „Kann er – aber wiederholen“ → **ein** `schule_plan_setzen` mit `kann_wdh_themen` (z. B. Delhi [3, 69]). Die Sammelleiste bleibt beim Rollen oben sichtbar („2 Flüge ausgewählt“). Mit 6 Themen hat es der Bau-Chat getestet; ich habe 2 genommen. | `820-auswahl-gescrollt.jpg` |
| 6 | „Wiederholung am nächsten Lerntag“, zwei Fehler → wieder offen | **nicht geprüft** | Server-Regel (LB-3). Ohne echte Antworten und Datenbank-Lauf nicht nachstellbar. In der App erscheint die Stufe richtig: ↻ „gesetzt: kann er, wird wiederholt · Wdh 1 von 5 · nächste in 1 Lerntag“. | `820-klasse-rs7.jpg` |
| 7 | ◉-Thema mit „Wieder in die Wiederholung“ zurückholen | **teilweise** | Der Knopf ist da (◉-Zeile). Ausgelöst habe ich ihn nicht; der Bau-Chat meldet einen Test dafür (`wieder_wdh_themen`). | `820-klasse-gym8-komplett-auf.jpg` |
| 8 | Themenliste hat Reihenfolge und Lernbereich für alle drei Schularten | **erfüllt (Daten)** | Reihenfolge: gym 71, rs 76, ib 84 Themen, also jedes Thema, das es in der Schulart gibt. Lernbereich bei allen 95. | – |

## 2. Die vier Stufen (Zeichen, Farben, Wörter)

| Stufe | Zeichen | Wort + Zusatz | Farbe (gemessen) | Ergebnis |
|---|---|---|---|---|
| Kann er komplett | ◉ | „Kann er komplett“ · „alle Etappen sicher“ / „gesetzt“ | weiß auf Dunkelgrün `#0F6B45` | erfüllt |
| In Wiederholung | ↻ | „In Wiederholung“ · „Wdh 2 von 5 · nächste in 4 Lerntagen“, gesetzt: „gesetzt: kann er, wird wiederholt · …“ | Grün `#2F8A57` auf Hellgrün | erfüllt |
| Gerade dran | ▶ | „Gerade dran“ · „3 von 7 Etappen“ | Gelb | erfüllt |
| Kommt noch | ○ | „Kommt noch“ · „im Plan“ | Grau | erfüllt |
| Nicht im Plan | + | „Nicht im Plan“ · „fehlt“ | gestrichelt | erfüllt |

Gleich in Plan, „Nach Klasse“, „Nach Themengebiet“ und Lehrplan-Übersicht. Die Legende steht oben in der Lehrplan-Spalte.

## 3. Abweichungen des Bau-Chats – Bewertung

| Abweichung | Gesehen | Bewertung |
|---|---|---|
| Im Auswahlmodus klappen links alle Orte auf | Ja. Die Seite wächst von 2 060 px auf **16 189 px** (Tablet), 20 383 px (Handy), 12 224 px (Rechner); 95 Häkchen. Jeder Flug zeigt dabei weiter seine vier Knöpfe, jeder Ort zusätzlich das alte Häkchen „alle Flüge: kann er komplett“. Zwei Arten Häkchen untereinander. | **Sollte** ändern (S1). Funktioniert, ist aber unübersichtlich. |
| Kopf zählt Flüge statt Orte | Ja. Kopf „1 ▶ · 8 ○ · 20 ↻ · 17 ◉“ (Flüge), die Abschnitte darunter „GERADE DRAN (1) · KOMMT NOCH (5) · IN WIEDERHOLUNG (16)“ (Orte). | Flüge im Kopf sind richtig, weil der Lehrer in Themen denkt. Die Abschnitte müssen aber dieselbe Einheit zeigen (S2). |
| Lehrplan-Übersicht: andere Schularten klein hinter dem Titel | Ja. | in Ordnung |

## 4. Mängel

### Muss

- **M1 Tablet 820: Lehrplan-Spalte zu schmal – Wörter brechen, Text überlappt.** In „Nach Klasse“ steht die Unterzeile senkrecht in Silben („Fun / ktio / nen · RS / 8 · MYP / 3“, „Alge / bra“). „Zehnerpotenzen und wissenschaftliche Schreibweise“ läuft in „Kann er komplett“ hinein. Der Grund: Die Spalte ist rund 330 px breit, und Titel, Unterzeile und Stufenwort teilen sich eine Zeile. Gesehen mit echten Thementiteln; der Bau-Chat hat „kein Wort gebrochen“ mit Testdaten gemessen. Handy 400 (eine Spalte) und Rechner 1280 sind in Ordnung.
  Vorschlag: Unter 1100 px steht das Stufenwort unter dem Titel statt rechts daneben (wie auf dem Handy). Oder: auf dem Tablet links 55 %, rechts 45 %.
  Bilder: `820-klasse-gym8-auf.jpg`, `820-klasse-rs7.jpg`.

### Sollte

- **S1 Auswahlmodus kompakt.** Im Auswahlmodus bleiben die Orte zugeklappt. Je Ort ein Häkchen (wählt alle seine Flüge), daneben „▸ einzeln“ zum Aufklappen. Je Abschnitt ein Häkchen „alle ↻ auswählen“. Die vier Knöpfe je Flug und „alle Flüge: kann er komplett“ werden ausgeblendet, solange ausgewählt wird. Die Sammelleiste bleibt oben stehen; das ist schon so.
- **S2 Gleiche Einheit in Kopf und Abschnitten.** Zum Beispiel „○ KOMMT NOCH · 5 Orte, 8 Flüge“, oder alles in Flügen.
- **S3 Lehrplan-Übersicht wie „Nach Klasse“ gliedern.** Heute: Gruppen „Klasse 8 · Algebra / Daten und Zufall / …“ nach Gebiet; darin nicht Lehrplan-Reihenfolge („Lineare Ungleichungen“ vor „Intervalle“, „Zuordnung und Funktion“ (M8 1) hinter „Gebrochen-rationale Funktionen“). Vorgabe LB-2: gleiche Zeile wie LB-1. Dazu gehören auch dieselbe Gliederung nach Lernbereich und dieselbe Reihenfolge. Bild `1280-lehrplan.jpg`.
- **S4 Etappen beim Aufklappen mit Titel.** Heute „Etappe 1 … Etappe 7“, der Titel steht nur im Tooltip; auf Tablet und Handy gibt es kein Überfahren mit der Maus. Ob die Chips den Stand zeigen (gelandet/sicher), konnte ich nicht sehen (siehe 5).

### Kann

- **K1** Die Legende oben in der Lehrplan-Spalte braucht 4–5 Zeilen, bevor der Umschalter kommt. Zuklappbar oder als eine Zeile wäre besser.
- **K2** „Nach Themengebiet“: Die Liste rollt innerhalb der Spalte (innere Bildlaufleiste) – auf dem Tablet leicht zu übersehen.
- **K3** IB-Lernbereiche englisch zuerst („MYP 3 Numerical and abstract reasoning (Zahl und Algebra)“) – deutsch voran wäre einheitlicher.
- **K4 Daten (LB-4, Inhalts-Chat):** In der Datenbank fehlt `lehrplan.gym_by` bei „Teilbarkeit und Primzahlen“ und „Intervalle“. Die Aufklapp-Zeile „Lehrplan:“ bleibt dort für das Gymnasium leer (in der Themenliste steht ein Bezug).

## 5. Nicht geprüft / Grenzen

- Echte Kinderdaten und echte Geräte: nein. Nur Chromium, nur das erfundene Testkind.
- Server-Regeln von LB-3 (Wiederholung startet, zwei Fehler → wieder offen, Rückgängig): nicht ausgeführt. Nur die Darstellung und die gesendeten Daten habe ich geprüft.
- Überblick „Zuletzt geschafft“ und „Wo steht es?“ zeigen in meinem Lauf „Noch kein Flug geschafft“ bzw. „–“. Das liegt an meinen Testdaten: Die kommen aus `schule_lernstand`, und das habe ich nicht nachgebildet. Kein Befund.
- Stand-Farbe der Etappen-Chips: aus demselben Grund nicht gesehen.
- Ziehen per Finger: nicht geprüft (Bau-Chat: Test vorhanden).
