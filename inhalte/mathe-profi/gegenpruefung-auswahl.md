# Gegenprüfung der Auswahl: 20 Aufgabentypen und Pakete A–F (Auftrag 6)

Mathe-Profi, 26.11.2026. Grundlage: `inhalte/plan/aufgabentypen-auswahl.md` (Stand `lernen-app` b2e51cd0). Kein Bau.
Rechnungen: `gegenpruefung_probe.py` (Lauf „OK“). **[G]** gesichert (gerechnet oder im Repo nachgelesen) · **[A]** Annahme · **[M]** Meinung.

**Kurz:** Die Auswahl ist gut. Der Paket-Plan hat drei Schwächen: (1) Er stellt `punkte` ans Ende, obwohl der Nutzer es am 25.11. als Bau 1 freigegeben hat. (2) Fünf Pakete brauchen dieselben drei Bausteine (Term-Rechner, zwei Antworten in einer Karte, Mehrfach-Auswahl); die stehen in keinem Paket. (3) Paket A ist nicht „klein“.

---

## 1. Die sechs Fragen

**1. Reihenfolge – D vor C?** Weder noch; D gehört geteilt. [M]
- Typ 4 (Lückenweg) braucht nur die vorhandene Form `luecken` [G] → nach B, sofort.
- Typ 2 (Heft mit Stichprobe) ist der größte Hebel für den Rechenweg → direkt nach A. Er braucht Wegmarken je Aufgabe, aber keinen neuen Antworttyp.
- Typ 3 und Typ 1 zuletzt aus D: Der Schalter nützt erst, wenn 3 und 4 für die laufenden Themen Inhalt haben. Sonst zeigt „nur Handy“ ins Leere.

**2. Typ 3 – reichen falsche Karten?** Nein. [G für das Beispiel, M für die Regel]
- Im Beispiel der Datei (fertige Karten „I + II“, „3x = 12“, „x = 4“, „y = 3“) folgt die Reihenfolge aus der Form: Die Zeilen werden kürzer. Die falsche Karte „3x = 10“ fällt durch Vergleich mit „x = 4“ heraus, ohne dass das Kind die Aufgabe löst.
- Nötig sind drei Dinge zusammen: **jede Karte hat eine Lücke** (Zahl eintragen); **falsche Karten sehen aus wie richtige** und werden erst durch die naheliegende falsche Zahl falsch; **mindestens zwei richtige Wege**, damit es keine eine Musterreihenfolge zum Merken gibt. Ausgearbeitet in Abschnitt 4.

**3. Typ 1 – was ist im Handy-Modus gleichwertig?**
- Gleichwertig, weil ohnehin kein Rechenweg geschrieben wird [M]: 6–9, 12–17, 20, 21, auch 18 und 19.
- **Nicht gleichwertig:** 3 und 4 als Ersatz für das Heft. Sie geben die Gliederung des Wegs vor; genau die muss das Kind in der Prüfung selbst leisten. Typ 11 in der freien Stufe und jede mehrschrittige Rechnung ebenso.
- Minimum: **Der Nutzer hat am 26.11. drei Tisch-Sitzungen je Woche festgelegt** [G, `aufgabentypen-auswahl.md` Stand 817e917f]; mein Vorschlag „zwei“ ist damit überholt. Unabhängig davon [M]: Eine Etappe mit Rechenweg wird nur „gelandet“, wenn mindestens eine Aufgabe davon am Tisch mit bestandenem Heft-Beleg gelöst wurde. Die zweite Regel ist wichtiger als die Zahl, weil sie nicht vom Kalender abhängt.

**4. Was passt nicht zu welcher Klasse?**
| Typ | Klasse 5 | Klasse 8 |
|---|---|---|
| 13 Verfahren wählen | nicht mit Gleichungssystemen; dafür „welcher Rechenvorteil passt?“ | passt; Gleichungssysteme erst, wenn das Thema dran ist (heute nicht [G, Versuchsdaten]) |
| 11 Ansatz aufstellen | nur ein Term oder eine Gleichung mit einer Unbekannten | passt |
| 15 Immer gleich oder Zufall? | nur in Worten oder mit □, nicht mit Buchstaben-Termen [A: Variable kommt laut Lehrplan erst später; Stelle nicht nachgeschlagen] | passt |
| 7 Datensatz bauen | ohne Mittelwert und Median, bis die Lehrplan-Stelle geprüft ist [A]; mit Summe, kleinster, größter Zahl | passt |
| 16 Begründungs-Bausteine | nicht mit Sätzen am Dreieck; mit Rechengesetzen | passt |
| 20 Diagramm-Lügendetektor | ohne Prozent („wirkt doppelt so hoch“) | passt |
| 9 Steckbrief | passt | nicht mit Zahlen (zu leicht); mit Gleichungen oder Termen als Gegenständen |
| 14 Zwei Wege vergleichen | passt | nicht am Zahlenrechnen; an Gleichungs- und Termwegen |
Alle übrigen passen zu beiden. [M]

**5. Wo ist die Aufwand-Schätzung falsch?** [M, zum Teil G]
- **Paket A „kleinster Bau“: eher mittel.** Meine Prüfregel arbeitet mit Programm-Funktionen. Am Server müssen Bedingungen als **Daten** in der Aufgabe stehen („Summe = 0“, „Median = 3“). Dafür braucht es eine kleine Rechensprache mit Vergleich, Betrag, Teilbarkeit, Summe, Median. Dazu kommt die Rückmeldung mit Zahl („deine Summe ist −6“).
- **Typ 9 „klein“: falsch.** Er braucht Mehrfach-Auswahl (siehe Abschnitt 3).
- **Typ 12 und 15 „klein“: nur, wenn eine Karte zwei Antworten haben kann** (Zeile markieren und weiterrechnen; Urteil und Gegenbeispiel). Den Aufwand dafür habe ich in Auftrag 2 erfragt; die Antwort steht aus [G].
- **Typ 2 „mittel“: beim Bau ja, beim Inhalt groß** – jede Aufgabe braucht Wegmarke und Kürzel.
- **Typ 21 „klein“:** stimmt nur, wenn die Auswahl-Logik der vorhandenen Wiederholung zu Sitzungsbeginn mitbenutzt wird. Vorher klären, ob 21 diese ersetzt oder ergänzt – sonst gibt es zwei Wiederholungen hintereinander.
- **Typ 20 „mittel“:** hängt daran, ob Diagramme erzeugt oder je Aufgabe gezeichnet werden [A, nicht nachgesehen].
- Zu niedrig geschätzt habe ich nichts gefunden bei 4, 6, 8, 13, 14, 17.

**6. Was fehlt, damit ein Typ nicht zur Auswahl mit Umweg wird?** [M]
1. **Zahl immer frei eintippen**, nie aus Vorschlägen wählen (6, 7, 8, 17, 19, Stichprobe in 2).
2. **Urteil nie allein:** Zu jedem „stimmt / stimmt nicht“ gehört ein Beleg (15: Gegenbeispiel; 13: erster Schritt des gewählten Verfahrens; 12: weiterrechnen).
3. **Offene Aufgaben mit vielen gültigen Antworten** und beim Wiedersehen eine Zusatzbedingung („diesmal beide Zahlen negativ“), sonst merkt sich das Kind eine Antwort.
4. **Bausteine mit Obergrenze** und mindestens einem Baustein, der gar nicht stimmt (9, 16). In den vier Steckbriefen unten sind nur 1 bis 4 von 15 bis 63 Ankreuz-Möglichkeiten richtig [G].
5. **Falsche Angebote sind berechnete Fehlbilder**, nie Unsinn.
6. **Typ 14** nicht als „welcher Weg stimmt?“, sondern: „Welche Zahl in Weg B entspricht der 12 in Weg A?“ – Antwort eine Zahl.
7. **Typ 3 und 4 zählen nie allein für „gelandet“.** Typ 4 mit voller Hilfe zählt gar nicht.

---

## 2. Angriff auf den Paket-Vorschlag

**Widerspruch zu einer Entscheidung des Nutzers [G]:** Am 25.11. hat der Nutzer die Reihenfolge „Bau 1 `punkte` · Bau 2 Mehrfach-Auswahl · Bau 3 falsche Antwort als Bild“ bestätigt (Postfach, Auftrag 3). Der Vorschlag stellt `punkte` in Paket F ans Ende und nennt die Mehrfach-Auswahl gar nicht. Entweder gilt die alte Reihenfolge oder der Nutzer hebt sie auf – das sollte er wissen.

**Vergessene Abhängigkeiten**
| Baustein | gebraucht von | steht im Vorschlag |
|---|---|---|
| Term-Rechner am Server (Terme und Gleichungen einsetzen, vergleichen) | 6, 7, 8, 15 (A) · 10, 12 (C) · 3, Stichprobe in 2 (D) · 11 (E) | nur als „Bedingungs-Prüfung“ in A |
| Zwei Antworten in einer Karte | 12, 13, 15, 19 | nirgends |
| Mehrfach-Auswahl | 9, 16 | nirgends (war Bau 2) |
| Fehlbild-Rechnung je Aufgabe | 10, 12, 3, Rückmeldung allgemein | in C als „Fehler-Katalog“ |
| Wegmarke und Kürzel je Aufgabe | 2, 3 | in D genannt |
| `punkte` | 18, 19 | F |
| Zählregel: Welcher Typ zählt für „gelandet“, welcher nicht? | alle | nirgends |
| Papier-Test als Ausgangswert (Auftrag 5) | Wirkung aller Pakete | nicht verknüpft |

**Zuschnitt, der nicht stimmt**
- **A:** Typ 9 gehört nicht hinein (andere Eingabe) – er passt zu 16. Typ 15 braucht die Doppel-Karte.
- **B:** Typ 21 ist kein Inhalt, sondern Ablauf-Logik; Typ 13 braucht die Doppel-Karte, sonst ist er Auswahl aus drei.
- **C:** vier Typen mit vier verschiedenen Bauteilen – kein Paket, sondern eine Sammlung. Typ 4 ist heute machbar.
- **E:** Typ 11 mit Kacheln ist die Eingabe mit dem höchsten Risiko am Handy; die erste Stufe (Ansatz aus vier berechneten Angeboten, dann lösen) geht ohne neue Form.

**Mein Gegenvorschlag** [M]
| Schritt | Inhalt | Bau |
|---|---|---|
| 0 | Papier-Test Blatt A (Auftrag 5), sobald der Nutzer startet | keiner |
| 1 | Typen 4, 14, 17 und 13/12 in einfacher Form – nur Inhalt mit heutigen Formen | keiner |
| 2 | **Fundament:** Term-Rechner am Server und Doppel-Karte | mittel, einmal |
| 3 | Typen 6, 7, 8, 15, dazu 12 und 13 in voller Form | klein, weil Fundament steht |
| 4 | Typ 2 (Heft-Beleg und Fehlersuche), Wegmarken zuerst für zwei Themen je Kind | mittel |
| 5 | `punkte` (Vorgabe liegt in `auftrag2.md`), dann 18, 19 | mittel |
| 6 | Mehrfach-Auswahl, dann 9, 16 | klein bis mittel |
| 7 | Typ 10, Typ 3, danach Schalter Typ 1 | mittel |
| 8 | Typ 11 mit Kacheln, Typ 20, Typ 21 | mittel |
Begründung der Reihenfolge: zuerst alles ohne Bau, dann der Baustein, den die meisten Typen teilen, dann der größte Hebel für den Rechenweg. Typ 21 steht spät, weil die App Wiederholung schon hat; sein Zusatz ist nur „ohne Etikett“.

---

## 3. Paket A: Trägt die Prüfregel?

**Ergebnis [G]:** `pruefe` aus `massstab_probe.py` trägt die Typen **6, 7 und 8 unverändert** (feste Zahl von Zahlenfeldern, Bedingungen der Reihe nach, erste verletzte Bedingung als Hinweis). Für **15 und 9 fehlt je eine Feldart**. Die erweiterte Fassung `pruefe2` steht in `gegenpruefung_probe.py`; alle 20 Musteraufgaben laufen mit guten und schlechten Antworten durch.

| Typ | trägt? | was fehlt |
|---|---|---|
| 6 Bedingung erfüllen | ja | – |
| 7 Datensatz bauen | ja | Median und Mittelwert als Bausteine der Bedingungs-Sprache |
| 8 Aufgabe ergänzen | ja | je Aufgabe eine Bedingung gegen die Ausweich-Lösung (z. B. „nur eine Lösung“) |
| 15 Immer gleich oder Zufall? | mit Zusatz | Feldart **Wahl** (immer / nicht immer) vor den Zahlenfeldern; bei wahren Behauptungen ist die Antwort nur ein Urteil – deshalb wahre und falsche mischen und bei „immer“ eine Begründung (Typ 16) anhängen |
| 9 Steckbrief schreiben | mit Zusatz | Feldart **Menge** (Bausteine ankreuzen), eine endliche Grundmenge, Obergrenze der Bausteine, Rückmeldung „passt auch auf …“ |
| alle | | Bedingungen als Daten statt als Programm; Hinweis mit eingesetzter Zahl; Zusatzbedingung beim Wiedersehen |

**Grenze von Typ 9:** Ein frei geschriebener Steckbrief ist nicht prüfbar. Prüfbar ist nur die Bausteine-Fassung. Das ist näher an Auswahl als die anderen vier Typen; der Schutz ist die Obergrenze und die Rückmeldung mit Gegenkandidat.

### Musteraufgaben (alle nachgerechnet)

**Typ 6 Bedingung erfüllen**
- K5: Nenne drei verschiedene ganze Zahlen mit der Summe 0. Genau eine davon soll positiv sein. – z. B. 5, −2, −3. Falsch: 2, 3, −5 (zwei positive).
- K5: Nenne zwei ganze Zahlen: Ihr Produkt ist −24, ihre Summe ist positiv. – z. B. −3 und 8. Falsch: 3 und −8 (Summe −5).
- K8: Setze a und b so ein, dass a · x + b = 3x − 6 keine Lösung hat. – a = 3, b beliebig außer −6. Falsch: 3 und −6 (jede Zahl ist Lösung).
- K8: Nenne eine Zahl x, für die (x + 1)/(x − 2) negativ ist. – jede Zahl zwischen −1 und 2, z. B. 0. Falsch: −1 (Wert 0), 2 (nicht definiert), 3.

**Typ 7 Datensatz bauen**
- K5: Fünf verschiedene ganze Zahlen; die kleinste ist −6, die größte 3, die Summe −5. – z. B. −6, −3, −1, 2, 3.
- K5: Vier ganze Zahlen; Summe 0, Produkt positiv. – z. B. −3, −1, 1, 3. Falsch: −3, 1, 1, 1 (Produkt −3); viermal 0 (Produkt 0).
- K8: Fünf ganze Zahlen; kleinste −2, Median 3, Mittelwert 5. – z. B. −2, 0, 3, 10, 14.
- K8: Vier Zahlen; Mittelwert 0, Median 1, Abstand zwischen kleinster und größter 10. – z. B. −6, 1, 1, 4. Falsch: −5, 0, 0, 5 (Median 0).

**Typ 8 Aufgabe ergänzen**
- K5: (□ − 9) · □ = −20, die erste Zahl positiv. – z. B. 5 und 5, oder 7 und 10.
- K5: □ · 6 − □ = −15, die erste Zahl negativ. – z. B. −1 und 9, oder −2 und 3.
- K8: □ · (x − 4) = 2x + □ so, dass x = 3 die einzige Lösung ist. – z. B. 1 und −7. Falsch: 2 und −8 (jede Zahl ist Lösung).
- K8: (x + □)/(x − □) ist für x = 5 nicht definiert und hat für x = 1 den Wert −2. – 7 und 5 (einzige Lösung).

**Typ 9 Steckbrief schreiben** (Bausteine ankreuzen)
- K5: Steckbrief für −6 unter den ganzen Zahlen von −10 bis 10, höchstens drei aus sieben Bausteinen (negativ · gerade · durch 3 teilbar · Betrag größer als 4 · links von −3 · Gegenzahl größer als 5 · kleiner als −7). – z. B. negativ, gerade, durch 3 teilbar. „Negativ, durch 3 teilbar, Betrag größer als 4“ → „passt auch auf −9“.
- K5: Steckbrief für 36 unter 1 bis 50, höchstens drei aus sieben (Quadratzahl · gerade · durch 3 teilbar · zweistellig · Quersumme 9 · kleiner als 40 · durch 8 teilbar). – z. B. Quadratzahl, gerade, durch 3 teilbar. „Quadratzahl, gerade“ → „passt auch auf 4“.
- K8: Sechs Gleichungen liegen aus (3x − 6 = x + 2 · 2x + 5 = 2x − 1 · 4x + 8 = 0 · 5x = 2x · x − 3 = 3 − x · 2(x + 1) = 2x + 2). Steckbrief für x − 3 = 3 − x aus höchstens zwei Bausteinen. – „Lösung positiv“ und „Lösung kleiner als 4“. Nur „Lösung positiv“ → „passt auch auf 3x − 6 = x + 2“.
- K8: Sechs Bruchterme liegen aus. Steckbrief für (x − 1)/(x + 2) aus höchstens zwei Bausteinen. – z. B. „für x = −2 nicht definiert“ und „für x = 0 negativ“. „Für x = −2 nicht definiert, für x = 1 den Wert 0“ → „passt auch auf (1 − x)/(x + 2)“.

**Typ 15 Immer gleich oder Zufall?**
- K5 (falsch): „Tauscht man bei einer Minus-Aufgabe die beiden Zahlen, kommt dasselbe heraus.“ – nicht immer; Gegenbeispiel 5 und 3. Mit 4 und 4: „Bei deinen Zahlen sind beide Seiten gleich. Das ist Zufall.“
- K5 (wahr): „Statt eine Klammer (b − c) abzuziehen, kann man erst b abziehen und dann c dazuzählen.“ – immer.
- K8 (falsch): „(x + 3)/(x + 6) lässt sich zu 1/2 kürzen.“ – nicht immer; Gegenbeispiel x = 1. Die Falle ist x = 0: Dort stimmt es zufällig.
- K8 (wahr): a⁻² · a⁵ = a³ für jede Zahl außer 0. – immer.

---

## 4. Typ 3 „Rechenweg zusammenbauen“

**Prüfregel** (`pruefe_weg`, im Skript):
1. Die Aufgabe hat Stufen (1, 2, 3 …). Das Kind legt **je Stufe genau eine Karte**, in aufsteigender Folge, und trägt in jede Karte **eine Zahl** ein.
2. Jede gelegte Karte muss – mit der eingetragenen Zahl – **gleichwertig zur Aufgabe** sein. Das wird gerechnet, nicht hinterlegt: bei Zahlentermen gleicher Wert, bei Gleichungen gleiche Lösung.
3. Gemeldet wird die **erste nicht gleichwertige Karte**; passt die eingetragene Zahl zu einem bekannten Fehlbild, mit dessen Namen.
4. Jede Karte kann richtig oder falsch werden – es gibt keine von vornherein falschen Karten. Je Stufe liegen zwei Karten aus; mindestens zwei Wege führen zum Ziel.

Warum das Wiedererkennen verhindert [M]: Die Form der Karte verrät nichts. Die „verführerische“ Karte wird nur mit der naheliegenden Zahl falsch; wer sie richtig füllt, hat gerechnet. Was bleibt: Die Karten geben die Gliederung vor. Deshalb zählt Typ 3 nicht allein für „gelandet“.

**Musteraufgabe 1 (Klasse 5):** 25 − 4 · (3 − 8) [= 45]
| Stufe | Karte | richtig mit | naheliegend falsch → Fehlbild |
|---|---|---|---|
| 1 | 25 − 4 · (□) | −5 | 5 → Richtung |
| 1 | □ · (3 − 8) | −9 | 21 → Rangfolge |
| 2 | 25 + □ | 20 | −20 → Zeichen-Paar |
| 2 | 25 − □ | −20 | 20 → Zeichen-Paar |
| 3 | = □ | 45 | 5 oder −105 |

**Musteraufgabe 2 (Klasse 8):** 4 − 3(x − 2) = 2x − 5 [x = 3]
| Stufe | Karte | richtig mit | naheliegend falsch → Fehlbild |
|---|---|---|---|
| 1 | 4 − 3x + □ = 2x − 5 | 6 | 2 → Verteilen |
| 1 | 4 − 3x − □ = 2x − 5 | −6 | 6 → Minusklammer |
| 2 | □ − 3x = 2x − 5 | 10 | −2 → Minusklammer |
| 3 | □ = 5x | 15 | 5 → Waage |
| 3 | −5x = □ | −15 | 15 → Waage |
| 4 | x = □ | 3 | −3 |

**Musteraufgabe 3 (Klasse 8):** 5/(x + 3) = 2/(x − 3) [x = 7]
| Stufe | Karte | richtig mit | naheliegend falsch → Fehlbild |
|---|---|---|---|
| 1 | 5 · (x − □) = 2 · (x + 3) | 3 | −3 → Verhältnis |
| 1 | 5 · (x + □) = 2 · (x − 3) | – (nur mit einer krummen Zahl) | 3 → Verhältnis: mit dem eigenen Nenner malgenommen |
| 2 | 5x − □ = 2x + 6 | 15 | 3 → Verteilen |
| 2 | 5x − 15 = 2x + □ | 6 | 3 → Verteilen |
| 3 | 3x = □ | 21 | −9 → Waage |
| 4 | x = □ | 7 | – |
Nach Stufe 4 folgt bei Bruchgleichungen eine Zusatzfrage: „Liegt 7 in der Definitionsmenge?“

Geprüft je Aufgabe: zwei bis drei richtige Lösungen über verschiedene Wege, drei bis fünf falsche mit erwarteter Meldung, falsche Reihenfolge und ausgelassene Stufe [G].

---

## Nicht geprüft
- Lehrplan-Stellen für Variable, Mittelwert und Median in Klasse 5 (nur Annahme).
- Bedienung am Handy: Karten legen und Zahl eintragen in einem Schritt; Liste mit fünf Zahlenfeldern.
- Ob die App Diagramme erzeugen kann (Typ 20) und wie die vorhandene Wiederholung ihre Aufgaben wählt (Typ 21).
- Die Aufwand-Urteile zum Bau: Ich kenne `lernen.js` und den Server nur aus den Teilen, die ich für `punkte` gelesen habe.
- Die 23 Musteraufgaben mit `tools/inhalt_pruefen.py` (kennt die neuen Feldarten nicht).

## Annahmen
- Alle „naheliegend falschen“ Zahlen sind aus den Fehlbildern abgeleitet, nicht aus Versuchsdaten.
- Offen zur Drei-Sitzungen-Regel: Was geschieht in einer Woche mit weniger als drei Lerntagen oder ohne Tisch (Reisetag)? Vorschlag [M]: Die Regel sperrt nichts, sondern hält „gelandet“ für Rechenweg-Etappen zurück, bis der Heft-Beleg da ist.
- Je Klasse lernt ein Kind; „laufende Themen“ nach den Versuchsdaten vom 25.11. (nichts davon im Repo).
