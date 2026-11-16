# Erklärungen für die Kinder: Darstellung und Verständlichkeit

- **Zweig:** `pruefung-erklaerung-darstellung` (von `lernen-app`, Stand `284d809`). Nichts an App, Inhalten oder Tests geändert.
- **Nachgestellt:** acht echte Themen (Klasse 5, 6 und 8) mit `aufnahme.test.cjs`, auf Handy (390 × 844) und Tablet (820 × 1180).
- **Gezählt:** Inhalte aller 549 Lernkarten in `inhalte/themen`.
- **Klickbarer Entwurf:** `entwurf.html` (Doppelklick genügt).
- **Kennzeichnung:** **Fakt** = gemessen oder im Code/Bild nachprüfbar. **Urteil** = Gestaltungsmeinung. **Annahme** = nicht geprüft.

## Kurzfassung

Die Erklärungen sind inhaltlich gut gemeint und seit der Runde „verständlich“ freundlicher geschrieben. Sie scheitern aber an drei Stellen der Darstellung:

1. **Menge:** Alle Lernkarten eines Themas stehen untereinander. Auf dem Handy sind das 14–19 Bildschirme, schon eine einzelne Karte über 2.
2. **Reihenfolge:** Erst Text, dann ein Wörterbuch mit bis zu sechs Begriffen, erst dann Bild und Beispiel. Das Kind liest Definitionen, bevor es weiß, worum es geht.
3. **Bild und Schritt sind getrennt:** Das Bild zeigt den Endzustand, weit weg vom Schritt, der es erklärt.

Der Entwurf zeigt dieselben Texte anders:
- eine Karte nach der anderen;
- das Beispiel Schritt für Schritt zum Durchtippen, das Bild ändert sich mit jedem Schritt;
- neue Wörter antippbar im Text;
- der Merksatz am Ende, danach sofort „Jetzt du“.

Auf dem Handy ist die erste Aufgabe damit ohne Scrollen erreichbar: mit einem Tipp (Reiter Üben) oder nach der ganzen Erklärung mit 6 Tipps. Heute sind es rund 1 600–2 000 px Scrollen.

## 1. Befunde

### 1.1 Länge und Menge (Fakt, gemessen)

| Thema | Klasse | Format | Lernkarten | Erklären-Seite Handy | ≈ Bildschirme | Höhe einer Karte (größte) | „Dazu üben“ der 1. Karte bei | Üben (1. Besuch): Aufgabe beginnt bei |
|---|---|---|---|---|---|---|---|---|
| zahlen.ganz | 5 | verständlich (einstieg) | 8 | 13 529 px | 16 | 1 877 px | 1 706 px | 1 665 px |
| messen.flaechen | 5 | verständlich (einstieg) | 7 | 11 766 px | 14 | 1 780 px | 1 834 px | 1 793 px |
| zahlen.rechengesetze | 5 | verständlich (einstieg) | 10 | 16 428 px | 19 | 1 886 px | 1 677 px | 1 664 px |
| geometrie.winkel | 5 | verständlich (einstieg) | 7 | 13 019 px | 15 | 1 826 px | 1 922 px | 1 909 px |
| gleichungen.einfach | 5 | alt | 7 | 7 092 px | 8 | 1 096 px | 1 206 px | 1 165 px |
| funktionen.linear | 8 | verständlich (einstieg) | 7 | 12 303 px | 15 | 1 938 px | 2 048 px | 2 007 px |
| gleichungen.lgs2 | 8 | verständlich (einstieg) | 8 | 13 243 px | 16 | 1 921 px | 1 608 px | 1 568 px |
| bruch.brueche | 6 | alt | 8 | 8 059 px | 10 | 1 191 px | 1 035 px | 1 015 px |

**Was die Tabelle zeigt:**
- **Wortzahl:** Eine Lernkarte im verständlichen Format hat im Median **192 Wörter** (höchstens 279), im alten Format 84. Ein Thema der 5. Klasse kommt so auf 1 100–2 070 Wörter auf einer Seite (`zahlen.rechengesetze`: 2 069).
- **Üben beim ersten Besuch:** Die ganze Erklärung der Karte steht über der Aufgabe. Die Aufgabe beginnt 1 570–2 000 px tiefer, also nach etwa zwei Bildschirmen (`zahlen.ganz-handy-ueben-ganz.png`).

### 1.2 Reihenfolge und Aufbau (Fakt)

- **Reihenfolge im verständlichen Format** (`lernErklaerung`, lernen.js Z. 1009): Worum geht’s? → Neue Wörter → Bild → Beispiel Schritt für Schritt → Probe → Merke → Achtung, typischer Fehler.
- **Neue Wörter vor dem Bild:** Bei `geometrie.winkel` steht das Bild erst bei 1 140 px, nach sechs Wortdefinitionen (`geometrie.winkel-handy-erklaeren-ganz.png`). 49 der 170 verständlichen Karten haben 5 oder mehr „neue Wörter“.
- **Zwei Formate nebeneinander:**
  - Klasse 5 und 8 („verständlich“): Merksatz unten, Überschrift „Beispiel – Schritt für Schritt“.
  - Klasse 6, 7, 9, 10 („alt“): Merksatz oben fett, Überschrift „So geht’s“, kein Einstieg.
- **Karte nicht für sich lesbar:** Jede Karte trägt noch ein Statuszeilchen, „Dazu üben ▸“ und – für Erwachsene – einen gestrichelten Anmerkungskasten. Die Karten folgen ohne Pause aufeinander.

### 1.3 Bild und Text (Fakt)

- **Ohne Bild:** 103 von 170 verständlichen Karten (61 %), obwohl der Einstieg oft ein Bild beschreibt. Beispiele:
  - `zahlen.ganz/deuten`: Thermometer im Text, kein Bild.
  - `messen.kreisberechnung/flaeche` (Pizza, Kreisfläche) und `terme.bruchterme/erweitern` (Pizza in 2 bzw. 8 Stücken): Die Situation wird nur in Worten beschrieben.
- **Bild zeigt das Ende, Text erzählt den Weg:** `funktionen.linear/ablesen`, Schritt 4: „Genau das zeigt das gestrichelte Steigungsdreieck im Bild.“ Das Bild steht 350 px weiter oben und zeigt Punkt, Gerade und Dreieck von Anfang an.
- **Bild passt nicht zur Geschichte:** `zahlen.ganz/betrag` erzählt von Taucher (−7) und Vogel (7). Das Bild ist ein Zahlenstrahl mit einem Pfeil bei −7 ohne Vogel und ohne Abstand.
- **Drei Situationen in einer Karte:** `funktionen.linear/ablesen`: Einstieg Taxi (3 € + 2 € je km), Beispiel y = 5 − 2x, Bild y = −2x + 5. Nach grober Zählung (keine gemeinsame Zahl in Einstieg und Beispiel) betrifft das mindestens 7 weitere Karten, z. B. `funktionen.grundbegriffe/stelle`, `gleichungen.bruch/ein_bruch`, `terme.bruchterme/termwert`.
- **Bildschrift zu klein:** Auf dem Handy 11,5–12,5 px (Tablet 14,8 px), der Fließtext daneben 18 px (`.lern-zeichnung .zahl { font-size: 12px }`).

### 1.4 Schrift und Hervorhebung (Fakt)

- **Zwei Farben für dieselbe Markierung:** `⟦…⟧` ist im Reiter Erklären rosa hinterlegt, im Reiter Fehler knallgelb (`zahlen.ganz-handy-fehler-ganz.png`). Das Rosa ist fast der Ton des Fehlerkastens; ein neues Fachwort sieht dadurch aus wie ein Fehler.
- **Alles fett:** Schritte, Merksatz und Markierungen sind fett. Dadurch hebt sich nichts mehr ab.
- **Brüche als Text:** „3/4“ steht als Zeichenfolge im Text (21 verständliche Karten und das ganze Bruch-Thema der 6. Klasse). In Aufgaben stellt die App Brüche dagegen als Zähler über Nenner dar.
- **Lange Sätze:** 90 der 170 verständlichen Karten haben mindestens einen Satz mit mehr als 20 Wörtern (längster: 36).
- **Status-Symbol:** Die Kreise vor „noch nicht geübt“ stehen ohne Abstand und lesen sich wie „OOOOnoch nicht geübt“.

### 1.5 Urteil

- **Inhalte:** Die Runde „verständlich“ hat sie freundlicher gemacht (Alltagssituation, du-Form, Wörter erklärt), aber auch etwa doppelt so lang.
- **Darstellung:** Sie ist nicht mitgewachsen. Die App zeigt den längeren Text wie ein Arbeitsblatt am Stück.
- **Das eigentliche Problem:** nicht schlechter Text, sondern zu viel gleichzeitig und das Bild am falschen Ort.
- **Für die 13-Jährigen** ist das Format zu ausführlich; sie brauchen zuerst die Regel und ein Beispiel.
- **Für die 10-Jährigen** ist es zu textlastig; sie brauchen zuerst ein Bild.

## 2. Vorschläge (nach Wirkung geordnet)

| Nr. | Vorschlag | Was genau | Wo | Aufwand |
|---|---|---|---|---|
| V1 | **Eine Lernkarte auf einmal** | Im Reiter Erklären nur die gewählte Karte. Darüber „‹ Karte 1 von 8 · alle ▾ ›“; die Liste ist nach Bereichen gegliedert. Empfohlene Karte vorausgewählt. | `lernEtappen` (Erklären-Panel) | klein |
| V2 | **Beispiel zum Durchtippen, Bild wechselt mit** | Ein Schritt pro Ansicht („Schritt 2 von 4“, Weiter/Zurück, auf dem Handy unten im Daumenbereich). Erledigte Schritte bleiben am Tablet als kurze Zeilen sichtbar. Das Bild zeigt den Zustand des Schritts (Format siehe 3.). Tastatur: → / Leertaste weiter, ← zurück. | `lernErklaerung`, `lernBild` | mittel |
| V3 | **Neue Wörter im Text antippen** | Erstes Vorkommen gepunktet unterstrichen; Antippen zeigt die Erklärung direkt darunter. Die Liste „Wörter (5) ▸“ steht eingeklappt am Ende der Karte statt vorweg. | `lernMarkiert`/`lernErklaerung` | klein |
| V4 | **Reihenfolge nach Alter** | Klasse 5/6: Worum geht’s (kurz) → Beispiel mit Bild → Merke → „Jetzt du: erste Aufgabe ›“. Klasse 7–10: „Kurz gesagt“ (Merke) → Beispiel → „Wozu brauche ich das?“ (Einstieg, eingeklappt). Typischer Fehler in beiden Fällen als „Vorsicht, Falle ▸“ eingeklappt (der Reiter Fehler bleibt). | `lernErklaerung` (Klasse aus dem Kind) | klein |
| V5 | **Üben: Spickzettel statt ganzer Erklärung** | Beim ersten Besuch über der Aufgabe nur der Merksatz (2–4 Zeilen) und der Link „Erklärung“. Die Aufgabe steht im ersten Bildschirm. | `uebenOeffnen` (`erklBox`) | klein |
| V6 | **Eine Markierung, eine Fehlerfarbe** | ⟦…⟧ überall als gelber Textmarker (#FFE58A); Rot und Rosa nur für Fehler. Schritte normal gesetzt, nur das Ergebnis markiert; der Merksatz ist das einzige Fettgedruckte. | `style.css` (`.lr-erklaert mark`, Fehler-Reiter) | klein |
| V7 | **Brüche stapeln** | `a/b` in Erklärtexten automatisch als Zähler über Nenner zeigen (wie in den Aufgaben). | `lernMarkiert` | klein |
| V8 | **Bildschrift ≥ 16 px** | `.lern-zeichnung .zahl` auf 16–17 px, `.klein` auf 16 px; Zeichnungen auf dem Handy nicht kleiner als die Textbreite skalieren. | `style.css`, `lernBild` | klein |
| V9 | **Mehr Bilder für Klasse 5** | Neue Zeichnungsarten, siehe App-Wünsche in 3.2. Danach Bilder für die 61 % Karten ohne Bild nachziehen, zuerst wo der Einstieg schon ein Bild beschreibt. | `lernBild` + Inhalte | mittel |
| V10 | **Längenregeln für Inhalte** | Einstieg ≤ 35 Wörter; höchstens 3 neue Wörter (der Rest im Text erklärt); 2–4 Schritte mit je ≤ 15 Wörtern; Merke ≤ 25 Wörter; Sätze ≤ 15 Wörter (Kl. 5/6) bzw. ≤ 20 (Kl. 7–10). **Einstieg, Beispiel und Bild erzählen dieselbe Situation.** | `inhalte/README.md` und Prüfung `inhalt_pruefen` | klein (Regel), mittel (Inhalte) |
| V11 | **Ein Darstellungsschema für alle Klassen** | Das alte Format (Kl. 6, 7, 9, 10) läuft durch dieselbe Darstellung (V1–V8). Fehlt der Einstieg, beginnt die Karte mit „Kurz gesagt“. | `lernErklaerung` | klein |
| V12 | **Kleinigkeiten** | Abstand zwischen Status-Kreisen und Text; Tablet: Bild links mitlaufend (sticky), Text rechts; Anmerkungskasten für Erwachsene am Kartenende eingeklappt. | `style.css` | klein |

**Reihenfolge der Umsetzung (Empfehlung):**
1. V1, V5, V6, V7, V8, V12 – reine Darstellung, die Inhalte bleiben unverändert und der Gewinn ist sofort da.
2. V2, V3, V4.
3. V10 als Regel für neue Inhalte, danach V9 und das Kürzen.

## 3. Formatvorschläge (für Haupt-Chat und Inhalts-Chats)

### 3.1 Bild je Schritt (optional, rückwärtskompatibel)

`schritte` darf Objekte enthalten. `bild` überschreibt einzelne Felder des Kartenbildes für diesen Schritt; reine Texte bleiben erlaubt.

```json
"bild": {"typ": "zahlenstrahl", "start": -10, "ende": 10, "abschnitte": 20, "beschriftet": "anfang_ende"},
"schritte": [
  {"text": "Der Taucher ist bei −7 m, der Vogel bei 7 m.", "bild": {"punkte": [{"wert": -7, "name": "Taucher"}, {"wert": 7, "name": "Vogel"}]}},
  {"text": "Von −7 bis 0 sind es 7 Schritte. Also ist ⟦|−7| = 7⟧.", "bild": {"boegen": [{"von": -7, "bis": 0, "name": "7"}]}},
  "Auch |7| = 7: Der Vogel ist genauso weit weg."
]
```

Regel: Ein Schritt ohne `bild` übernimmt den Bildzustand des vorigen Schritts.

### 3.2 App-Wünsche für Zeichnungen (Klasse 5 zuerst)

| Zeichnungsart | Felder | Wofür (Beispiele) |
|---|---|---|
| `zahlenstrahl` + `punkte`, `boegen`, `bereich` | Punkte mit Namen; Bögen von–bis mit Beschriftung; schattierter Bereich | Betrag, Addieren/Subtrahieren als Sprünge, Ordnen |
| `thermometer` (senkrechter Zahlenstrahl) | `start`, `ende`, `stand`, `bereich_unter_null` | negative Zahlen deuten |
| `bruchstreifen` | `teile`, `gefaerbt`, `ganzes` (Text), `teil_text` | Bruchteile, das Ganze aus einem Teil |
| `koordinaten` + Schritt-Zustände | `punkte`, `strecken` je Schritt einblendbar | Steigung, Achsenabschnitt |

### 3.3 Anzeige-Regeln, die die App selbst anwenden kann

- `a/b` mit ganzen Zahlen → gestapelter Bruch.
- Wörter aus `woerter` beim ersten Vorkommen im Text antippbar machen (auch Plural- und Beugungsformen: Wortanfang genügt).
- `⟦…⟧` überall dieselbe Markierung.

## 4. Der Entwurf

Öffnen: `entwurf.html`. Oben die Leiste „Entwurf – Ansicht“ wählt das Thema: Klasse 5 Ganze Zahlen, Klasse 6 Brüche, Klasse 8 Lineare Funktionen.

**Echt oder Vorschlag:**
- Alle Texte sind die echten Lernkarten (eingesetzt mit `werkzeug/bauen.py`).
- Nur der Einstieg der Karte „Was bedeutet eine negative Zahl?“ ist gekürzt; er ist im Entwurf mit „gekürzt (Vorschlag)“ markiert.
- Schritt-Bilder gibt es für vier Karten:
  - Thermometer (`zahlen.ganz/deuten`)
  - Taucher/Vogel mit Abstandsbögen (`zahlen.ganz/betrag`)
  - Bruchstreifen (`bruch.brueche/bruchteil_von`)
  - Gerade mit Achsenabschnitt und Steigungsdreieck (`funktionen.linear/ablesen`)
- Andere Karten zeigen den vorhandenen Zahlenstrahl oder einen Platzhalter.

**Geprüft** mit `werkzeug/bilder.cjs`:
- in allen 24 Bildern der Hauptknopf im ersten Bildschirm sichtbar;
- Text überall ≥ 16 px, auch in den Zeichnungen;
- keine Skriptfehler.

**Wichtigste Bilder** (alle in `bilder/`):

| Bild | Was es zeigt |
|---|---|
| `vergleich-erklaeren-handy.png` | Heute vs. Entwurf: erster Blick, Start der Karte, Schritt 3 |
| `vergleich-ueben-handy.png` | Heute vs. Entwurf: Üben beim ersten Besuch |
| `entwurf-kl5-karte4-schritt4-handy.png` | Taucher und Vogel: Abstand und Gegenzahl im Bild |
| `entwurf-kl5-karte1-wort-handy.png` | Neues Wort antippen |
| `entwurf-kl5-karte1-merke-handy.png` | Merke, „Jetzt du“, Falle aufgeklappt |
| `entwurf-kl8-kurz-handy.png` | Klasse 8: „Kurz gesagt“ zuerst |
| `entwurf-kl8-schritt3-tablet.png` | Tablet: Bild links, Schritte rechts, Steigungsdreieck im Schritt |
| `entwurf-kl6-bruch-schritt2-handy.png` | Bruchstreifen im Schritt |

Heutiger Zustand: `<thema>-handy-erklaeren-ganz.png` (ganze Seite, halbe Auflösung), `<thema>-handy-erklaeren-blick.png`, `<thema>-tablet-erklaeren-blick.png`, `zahlen.ganz-handy-ueben-ganz.png`, `zahlen.ganz-handy-fehler-ganz.png`.

## 5. Offen / Annahmen

- **Nicht mit den Kindern getestet.** Ob die 10-Jährige das Durchtippen dem Lesen vorzieht, ist eine Annahme aus der Gestaltung. Vorschlag: beide Kinder je eine Karte im Entwurf und in der App lesen lassen und danach eine Aufgabe dazu lösen lassen.
- **Schritt-Bilder als Inhaltsarbeit:** Sie verlangen je Karte Arbeit an den Inhalten (V9/3.1). Ohne sie bringen V1, V3–V8 schon den größten Teil des Gewinns.
- **Grobe Zählungen:** Die Zahlen zu Satzlänge und „Einstieg ≠ Beispiel“ sind grobe automatische Zählungen; die Einzelfälle sind genannt, die Gesamtzahlen sind Richtwerte.
- **Messwerte:** Gemessen mit lokalem Chrome unter Linux; die Schrift der App kann auf Apple-Geräten etwas schmaler laufen. Die Seitenhöhen ändern sich dadurch nur wenig (Annahme).

## 6. Auswahl Sebastian (2026-11-16)

Gewählt auf der Vergleichsseite (Heute / Vorschlag A / B). **Wo die Auswahl von Abschnitt 2 abweicht, gilt die Auswahl.**

| Punkt | Gewählt | Folge für die Vorschläge |
|---|---|---|
| 1 Lernkarten | **B – erst Übersicht, dann eine Karte** | ersetzt den Blätterkopf aus V1: Erklären öffnet mit einer Übersicht aller Karten (nach Bereichen, Status, empfohlene Karte hervorgehoben); Antippen öffnet genau eine Karte, „‹ Übersicht“ führt zurück. |
| 2 Kartenanfang (Kl. 5) | **A – kurzer Text, dann Bild** | wie V4 (Worum geht’s kurz → Bild/Beispiel). |
| 3 Beispiel | **B – Bildergeschichte** | ersetzt das Durchtippen aus V2: alle Schritte untereinander, jeder mit eigenem kleinen Bild. Das Format „Bild je Schritt“ (3.1) wird dadurch Pflicht für Karten mit Beispiel, nicht nur Option. Keine Weiter/Zurück-Knöpfe nötig. |
| 4 Neue Wörter | **A – im Text antippen** | wie V3. |
| 5 Hervorhebung | **A – überall gelber Textmarker** | wie V6. |
| 6 Brüche | **A – übereinander** | wie V7. |
| 7 Bildschrift | **A – größer** | wie V8. |
| 8 Typischer Fehler | **B – letzter Schritt „Pass auf!“** | ersetzt das eingeklappte „Vorsicht, Falle ▸“ aus V4: die Falle ist das letzte Bild der Bildergeschichte (mit eigenem Bild). Der Reiter „Fehler“ bleibt. |
| 9 Üben beim ersten Mal | **B – nur die Aufgabe** | ersetzt V5: über der Aufgabe nur ein gut sichtbarer Link „Erklärung ansehen“, kein Merksatz. |
| 10 Klasse 8 | **offen** | Empfehlung siehe unten. |

**Punkt 10 – Empfehlung (Meinung):** B (Alltag zuerst, wie Klasse 5), und der „Kurz gesagt“-Satz steht zusätzlich auf der Übersichtskachel der Karte (Punkt 1B). Begründung: Zum Nachschlagen reicht die Übersicht; die Karte selbst bleibt in allen Klassen gleich aufgebaut, also eine Darstellung statt zwei (passt zu V11). Gegenargument: Wer die Regel schon kennt, muss bei B erst über den Alltag scrollen. Entscheiden lässt sich das am besten, wenn das Kind in Klasse 8 eine Karte in beiden Fassungen liest.

**Entwurf:** `entwurf.html` zeigt noch die frühere Fassung (Blättern, Durchtippen, Falle eingeklappt, Merksatz über der Aufgabe). Bei 1, 3, 8 und 9 weicht er damit von der Auswahl ab; maßgeblich ist diese Tabelle.
