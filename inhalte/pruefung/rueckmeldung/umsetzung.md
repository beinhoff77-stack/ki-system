# Rückmeldung & Lernweg – wer macht was (Stand 2026-11-16)

Grundlage: `bericht.md` (Befunde F1–F9, L1–L7, Vorschläge V1–V12).
Hier: Aufteilung auf **Haupt-Chat (App)**, **Haupt-Chat (Datenbank)**, **Inhalts-Chats**, **Sebastian** und **Prüf-Chat**, jeweils mit Prüfpunkten „fertig, wenn …“.
Alles im Zweig `lernen-app`. Datenbankänderungen nach den Werkstatt-Regeln W1–W7 (Wunsch → Sperre → Änderung → erledigt), als neue Datei unter `supabase/migrations/`. Kein Merge nach `main` ohne Sebastians „Live“.

---

## Überblick

| Paket | Wer | Inhalt | Wann |
|---|---|---|---|
| **R1** | Haupt-Chat (App + 1 kleine DB-Änderung) | V1, V5, V6, V7, V10, V11 | sofort, klein |
| **R2** | Haupt-Chat (App + DB) | V2, V3, V8 | nach R1 |
| **R3** | Haupt-Chat (App + DB) | V9, V12 | nach R2 |
| **R4** | Inhalts-Chats | V4 Fehlbilder in den Aufgaben | nach R2 und nach Auswertung echter Fehler (siehe Sebastian) |
| – | Sebastian | Freigaben und Ausprobieren | siehe unten |
| – | Prüf-Chat | Nachprüfung nach jedem Paket | nach R1, R2, R3 |

**Zusammenspiel mit dem Umbau der Erklärungen** (`inhalte/pruefung/erklaerungen/darstellung/umsetzung.md`):
- R1 läuft parallel zu A2/A5–A9.
- A9 („Üben: nur die Aufgabe“) und R2 (V2, V8) ändern dieselbe Stelle, `zeichneUeben` in `lernen.js`. Sie gehen deshalb nacheinander und in einer Hand: zuerst A9, dann R2.
- V1 (Flächen) gehört zu A8 (Bildschrift), beides in `style.css`.

---

## R1 – Haupt-Chat, sofort

| Nr. | Änderung | Ort | Fertig, wenn … |
|---|---|---|---|
| V1 | Gefärbte Flächen sichtbar machen | `style.css` `.lern-zeichnung .flaeche` | Kontrast der Fläche zum Hintergrund ≥ 3 : 1 in heller und dunkler Ansicht. Eine Kontur ist zusätzlich erlaubt. Das Hunderterfeld („Wie viel Prozent sind gefärbt?“) ist auf dem Handy eindeutig zählbar. |
| V5 | Gemerkte Lösung zählt nicht | `lernen.js` `zeichneUeben` (`warte.splice`) | Nach einem Fehler kommt dieselbe Aufgabe in dieser Sitzung nicht wieder, sondern eine andere Aufgabe derselben Lernkarte und Stufe. Erst wenn keine andere mehr da ist, kommt sie ans Ende. Nachstellung R2 zeigt keine Wiederholung der falschen Aufgabe mehr. |
| V6 | Fehler in der Wiederholung: eine Stufe zurück | DB `schule.karte_buchen` (neue Migration) | Falsch bei `sitzt`: `wdh_stufe` um 1 kleiner (mindestens 0), `faellig_am` = nächster Tag, `sitzt` bleibt. Erst ein 2. Fehler hintereinander setzt auf „üben“ (heutiges Verhalten). Die Karte bleibt damit in `schule_wiederholung`. |
| V7 | Ehrliche Meldungen | `lernen.js` | Ende der Wiederholung: der Haken nur, wenn alles richtig war; sonst „N Karte(n) brauchen noch Übung – morgen kommen sie wieder.“ „FAST – KURSKORREKTUR“ nur bei Zahl-Aufgaben mit erkannter Nähe (bis R2: bei Zahl-Aufgaben), sonst „NOCH NICHT“. Der Tipp-Hinweis heißt „zählt nicht für die Serie“. |
| V10 | Auswahl: Antworten markieren | `lernen.js`, `style.css` | Nach dem Prüfen ist die gewählte falsche Option rot umrandet, die richtige grün, mit Zeichen ✗/✓ (nicht nur Farbe). |
| V11 | Schreibweise | `lernen.js` (`lernZahl`, `lernLoesungText`, `lernKurs`) | Minuszeichen „−“ statt Bindestrich. „□x + □“ mit −1 ergibt „−3x − 1“. Die Kurs-Grafik zeigt kein Komma ohne Nachkommastellen. |

## R2 – Haupt-Chat, danach

| Nr. | Änderung | Ort | Fertig, wenn … |
|---|---|---|---|
| V3 | Fehlermuster erkennen und weitergeben | DB `schule.antwort_bewerten`, `schule.uebung_pruefen_intern`; `lernen.js` | `antwort_bewerten` liefert bei falschen Antworten `grund`: `vorzeichen` (Betrag stimmt), `komma` (×/÷ 10, 100, 1000), `falsche_einheit` (gibt es schon), `vertauscht` (Lücken richtig, Reihenfolge falsch), `gerundet` (innerhalb ±1 % bzw. ±0,5 der letzten Stelle). `uebung_pruefen_intern` gibt `grund` zurück. Die App zeigt dazu einen Satz als erste Zeile der Rückmeldung, z. B. „Schau aufs Vorzeichen.“ |
| V2 | Zweiter Versuch vor der Lösung | `lernen.js` Üben; DB `uebung_pruefen_intern` | 1. Fehler: Die Lösung wird **nicht** gezeigt, nur der Satz aus V3 bzw. der Tipp, und die Eingabe bleibt änderbar. 2. Fehler: Lösung, Lösungsweg, Detektiv. Die Datenbank liefert die Lösung erst ab dem 2. Fehlversuch oder bei richtig. Richtig im 2. Versuch: Die Serie bleibt, wie sie war, und steigt nicht. Gilt für Üben, nicht für Tests. |
| V8 | Nach 2 Fehlern in Folge: anderer Weg | `lernen.js` | Nach 2 falschen Aufgaben derselben Karte hintereinander erscheinen „Leichtere Aufgabe“ (Stufe − 1, falls vorhanden) und „Beispiel ansehen“. Nach 3: zusätzlich „Frag Mama/Papa – sie sehen, wo es hakt“. Die Karte steht in der Elternansicht oben. |

## R3 – Haupt-Chat, danach

| Nr. | Änderung | Ort | Fertig, wenn … |
|---|---|---|---|
| V9 | Wiederholung reisetauglich | DB `karte_buchen`, `schule_wiederholung`; „Heute“ in `lernen.js` | Abstände 1/3/7/14/30 in **Lerntagen** (wie die Nachtests, `schule.lerntage_seit`). Vor dem Thema höchstens 6 Wiederholungen (Vorschlag, Sebastian kann ändern); danach führt der Startknopf ins Thema. Restliche fällige Wiederholungen werden nach dem Üben angeboten. |
| V12 | Wiederholen erklären | Eltern- und Kindansicht | Eine kurze Erklärung „Was kommt wann wieder?“: Karten-Wiederholung und Nachtest in einfachen Worten, in der Elternansicht mit den Zahlen je Kind. |

## R4 – Inhalts-Chats (später)

| Nr. | Änderung | Fertig, wenn … |
|---|---|---|
| V4 | Fehlbilder je Aufgabe | Neues optionales Feld `fb` in Übungsaufgaben: `[{"antwort": <Wert, Index oder Werte>, "text": "…"}]`, höchstens 3 je Aufgabe. Bei Auswahl ein Text je falscher Option. Text ≤ 20 Wörter, sagt, was das Kind vermutlich gedacht hat, und nicht die Lösung. Die App (Haupt-Chat) zeigt `fb` statt des allgemeinen Detektivs; ohne Treffer kein Detektiv. Zuerst die Karten, auf denen die Kinder laut echten Daten am häufigsten Fehler machen. Format und Regel in `inhalte/README.md`, Prüfung in `tools/inhalt_pruefen.py`. |

## Sebastian

1. **Freigabe Datenauswertung:** Der Prüf-Chat darf in etwa 3–4 Wochen die echten falschen Antworten der Kinder **nur lesend** auswerten. Daraus wird die Liste für R4. Ohne Freigabe startet R4 mit den Fehlern aus den `fehler`-Texten der Lernkarten.
2. **Ausprobieren nach R1:** Kind A löst 2 Hunderterfeld-Aufgaben, Kind B übt eine Karte bis „sitzt“. Danach kurz sagen, ob sich das richtig anfühlt.
3. **Entscheiden bei V9:** Wie viele Wiederholungen vor dem Thema höchstens? Vorschlag 6.

## Prüf-Chat (Nachprüfung)

Nach jedem Paket `inhalte/pruefung/rueckmeldung/nachstellen.test.cjs` gegen `lernen-app` laufen lassen und die Erwartungen anpassen. Danach im Postfach melden, welche Befunde erledigt sind:
- R1: R2 ohne Wiederholung der falschen Aufgabe, r7 ohne Haken, r9 mit Kontrast ≥ 3 : 1.
- R2: R1/R3/R5 mit passendem Satz und zweitem Versuch.
