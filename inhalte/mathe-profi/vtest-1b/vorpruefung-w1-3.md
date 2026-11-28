# Vorprüfung W1, dritte Runde (Nachprüfung) – Einheit 20 `gleichungen.bruch`, Stand 1f365ffc

Umfang: neuer Inhalt 026, 028, 032, 033, 034, 035, 036, 041; geändert 022, 027, 030, 037; Wortlaut 024, 029; dazu die Gesamtsicht je Lernziel. Maßstab wie in `vorpruefung-w1-2.md`. Nichts an Aufgaben geändert.

Werkzeug: `vorpruefung_w1_rechnen.py` (für diesen Stand angepasst). **Alle Sollwerte bestätigt**, jede Lücke mit eigenem Fehlbild, kein Fehlbild gleich der Lösung, bei jeder Auswahl genau eine richtige Möglichkeit. Gerechnete Sonderfälle: 027 über rund 300 rationale a ≠ 0 (keine Lösung nur für a = 7; a = 14 → x = 9); 028 über alle 110 Paare p, q ∈ {−5 … 5} mit p ≠ −q (die zweite Gleichung hat stets genau eine Lösung, nie eine Scheinlösung; nur a = 6 passt für alle Paare; a = 10 gäbe 0 · x = Zahl); 030 über alle a, b, c, d ∈ {−4 … 4} mit a ≠ b, c ≠ d, b ≠ d (4272 Gleichungen mit einer, 336 ohne Lösung, keine mit zwei oder unendlich vielen); 033 über alle c (nur c = 28 macht 4 zur Scheinlösung); 036 für jedes c des Rasters nur Möglichkeit 1 gleichwertig; 037 400 ml (Saft 200, Wasser 400); 041 25 %. Bestand: Mustersuche über alle Themen und `rollend-*`, gezielt `terme.bruchterme`, `groessen.*`, `bruch.prozent`.

## Urteil

**Bereit für die Gegenprüfung: nein – aber nah.** Alle Befunde der zweiten Runde sind in der Sache geschlossen. Es bleiben **2 A** (Test 027 nicht die anspruchsvollste Aufgabe des Lernziels, 035 nicht eindeutig) und **6 B, 3 C**; beide A sind mit kleinen Änderungen zu schließen.

## Gezielte Entscheidungen

| Punkt | Entscheidung |
|---|---|
| 022 [0; 3] und 032 [1; 0; 2] | Verschiedene Denkfiguren: 022 Lösungsverlust, weil ein neuer Nenner D verkleinert; 032 Scheinlösung, weil Kürzen D vergrößert. Beide eindeutig (Leas Gleichung steht jetzt wörtlich da). Die Frageform ist ähnlich (C2). |
| 032 als Lücken-Test | Enthält eine echte Scheinlösung (0, entstanden durch Kürzen). Etwa gleich schwer wie 033, schwerer als 034–036: als Test zulässig. Schema-Grenzfall, weil jede Lücke ein Routineschritt ist (B2) – entschieden: kein Schema, denn gefragt ist der Vergleich zweier Lösungsmengen. |
| 033 (c = 28) | Richtig und eindeutig; Fehlbilder 30 und 44 passen. |
| 028 (a = 6) | Für alle p ≠ −q richtig. Sonderlagen gibt es nicht: Bei p ≠ −q hat 15/(x − p) = 9/(x + q) stets genau eine Lösung x = (−3p − 5q)/2, und die ist nie p und nie −q. Kein Schema (ausrechnen geht nicht). |
| 027 (a ≠ 0, [7; 9]) | Richtig und eindeutig, aber nicht mehr die anspruchsvollste Aufgabe des Lernziels: 028 und 030 verlangen mehr. Die zweite Lücke ist eine Routinerechnung → A1. |
| 030 („nie mehr als eine“) | Immer wahr: Aus a + d = b + c und bc = ad folgt mit b ≠ d, dass a = b ist – darum keine unendlich vielen Lösungen; x² fällt weg, also nie zwei. „Immer genau eine“, „nie eine“ und „können zwei“ sind falsch (Beispiele im Skript). Die Begründung in der richtigen Möglichkeit ist unvollständig (B5). |
| 035 ([3; 0]) | Kein Schema (Denkfehler, nicht Rechenfehler), aber nicht eindeutig → A2. |
| 036 | Kein Bauart-Merkmal: auch Möglichkeit 3 hat zwei Bedingungen, alle beginnen gleich. Kein Schema, denn zwischen 0 und 1 entscheidet die Einsicht „die Bedingungen gehören dazu“; aber 2 und 3 prüfen nur die D-Rechnung (B3). |
| 026 ([2; 3]) | Richtig; ℤ und ℚ in Klasse 8 zulässig. **Schema** (D bestimmen, ganzzahlige Nullstellen zählen) – das ist dann die eine Schema-Aufgabe von definitionsmenge. Kein Bestandskern (BT 28 und BT 31 haben ähnliche Nenner, aber weder ℤ noch Text). |
| 041 (25 %) | Richtig, offen als Schema; im Bestand keine Aufgabe „a : b gegeben, um wie viel Prozent größer“. |
| 037 (400 ml) | Richtig; Fehlbild 200 (Verhältniszahlen addiert) passt. |
| 034 gegen T 229/T 222 | Neuer Rechenkern gegenüber T 229/T 222, aber jetzt nahe an T 180 und T 198 (zwei lineare Nenner, ihr Produkt rechts, Kandidat verboten, L = { }) → B4. |

## Befunde A (Muss)

| Nr. | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| A1 | 027 (Test ueber_kreuz) | Lücke 1 (a = 7) ist mit dem Blick auf gleiche Zähler in einer Minute erledigt, Lücke 2 (a = 14 einsetzen, x = 9) ist reine Routine. 028 (allgemein mit p und q, nur das Zählerverhältnis entscheidet) und 030 (allgemeine Aussage) verlangen mehr. Der Test ist damit weder die anspruchsvollste Aufgabe noch frei von Routine. | Pools tauschen: 028 als Test (Stufe 3), 027 als Korrektur (Stufe 2). Tests der Einheit bleiben dann vier verschiedene Denkfiguren. |
| A2 | 035 | Zeile 3 enthält keine falsche Aussage: Die Probe in Zeile 1 ist richtig gerechnet, „das stimmt“ ist wahr. Die erste falsche Aussage ist Zeile 4 (L = {4}). Wer 4 eingibt, ist vertretbar und wird als Fehlbild gewertet. | Zeile 3 als Behauptung fassen: „Probe in Zeile 1: 5 · 4 + 2 · 0 = 20 und 4 + 16 = 20, also ist 4 eine Lösung der Gleichung.“ Dann ist Zeile 3 eindeutig die erste falsche Aussage. |

## Befunde B (Soll)

| Nr. | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| B1 | 022 (Test) | Der Text nennt die Lösung x = 0 der Ausgangsgleichung. Damit ist der Test in 1–2 Minuten gelöst; 024 (Modell, D, sinnvolle Werte, Lösung) macht mehr Arbeit. | „hat in der Grundmenge ℚ die Lösung x = 0“ streichen; dann muss das Kind 6(x − 1) = 3(x − 2) selbst lösen und erkennen, dass die Lösung verboten wird. |
| B2 | 032, 033, 035 | Dreimal der Nenner x² − 4x, in 033 und 035 dieselbe Scheinlösung 4; wer 033 als Korrektur gesehen hat, erkennt 035 sofort wieder. 032: jede Lücke ist ein Routineschritt (Grenzfall, siehe oben). | 035 auf einen anderen Nenner umstellen (z. B. x² + 3x mit Scheinlösung −3). |
| B3 | 036 | Möglichkeiten 2 und 3 unterscheiden sich von der richtigen nur in der D-Rechnung; wer D kann, wählt zwischen zwei Möglichkeiten. | Eine D-Fehler-Möglichkeit durch eine zweite Fehlvorstellung über die Rolle der Bedingungen ersetzen (mit falscher Folgerung, z. B. „…, die Bedingungen braucht man nur bei der Probe, sie ändern die Lösungsmenge nie“). |
| B4 | 034 | Bestand T 180 (2/(x − 3) − 1/x = 6/(x(x − 3)), L = { }) und T 198 (1/(x − 1) + 1/(x + 1) = 2/(x² − 1), L = { }): gleiche Rechnung, gleiche Frage; neu ist die Einkleidung. Offen als Schema gezählt. | Als Schema-Platz vertretbar; in `abgrenzung` T 180/T 198 nennen. |
| B5 | 030 | Die Begründung der richtigen Möglichkeit („x² fällt weg, es bleibt eine Gleichung ohne x²“) trägt allein nicht: Auch eine Gleichung ohne x² kann 0 = 0 ergeben. Dass das hier nicht geht, folgt erst aus a ≠ b, c ≠ d, b ≠ d. | „…, und weil a ≠ b, c ≠ d, b ≠ d ist, bleibt nicht 0 = 0 übrig“ – oder die Begründung kürzer und richtig: „denn x² fällt weg und die Bedingungen schließen 0 = 0 aus“. |
| B6 | Etiketten 024, 034, 038 | siehe Abschnitt B6 unten. | – |

## Befunde C (Kann)

| Nr. | Kennung | Beleg |
|---|---|---|
| C1 | 022 | Fehlbild Lücke 2, Antwort 1 („die beiden Brüche 1/x höben sich auf und es bleibe nur der Nenner x“) – wer 1/x wegstreicht, behält die Nenner x − 2 und x − 1 (Antwort 2, schon belegt). Beschreibung passt nicht. |
| C2 | 022, 032 | Gleiche Frageform („wie viele Lösungen, wie viele ausgeschlossen“) in zwei Tests; Denkfiguren verschieden. |
| C3 | 025 | Einzige verbleibende Aufgabe mit „immer – kann – nie“, die richtige ohne Absolutwort; allein kein Muster mehr. |

## B6: Etiketten – fachliche Einschätzung

Fachlich richtig ist, dass `typ` die Denkleistung beschreibt und `stufe` den Anspruch – beides unabhängig. Ein Modell aus einem kurzen Sachtext aufstellen (024, 038) ist `transfer` und kann Stufe 2 sein. Die Kopplung „transfer ⇒ Stufe 3“ im Bauskript ist eine Faustregel, keine Regel des Auftrags. Für die eine erlaubte Schema-Aufgabe je Lernziel (034) ist ein falsches Verstehens-Etikett die schlechteste Lösung: Es verdeckt genau das, was die Gegenprüfung zählt.

Empfehlung: **Werkzeug- und Bauskript-Regel ändern, nicht die Pools.** (1) `transfer` auch mit Stufe 2 zulassen. (2) Ein ausdrückliches Kennzeichen für die eine Schema-Aufgabe je Lernziel einführen (z. B. `schema: true`), das V5 für diese Aufgabe aufhebt, aber prüft: höchstens eine je Lernziel und nie im Pool `test`. Ein Pool-Tausch bricht die Stufenmischung und löst die Ursache nicht.

## Gesamtsicht je Lernziel

| Lernziel | Schema (entschieden) | Denkfiguren | Test die anspruchsvollste, Kern, kein Schema? |
|---|---|---|---|
| definitionsmenge | 026 → 1 | 5: Lösungsverlust durch neuen Nenner (022), rückwärts a (023), Modell und sinnvolle Werte (024), L legt D nicht fest (025), D in ℤ und ℚ (026) | Kern ja, kein Schema; knapp, weil die Lösung im Text steht (B1) |
| ueber_kreuz | 031 → 1 (Lücke 2 von 027 Routine) | 5: Fallunterscheidung (027), Zählerverhältnis allgemein (028), zwei Wege Kehrwert (029), x² fällt weg (030), wann direkt (031) | nein (A1) |
| scheinloesung | 034 → 1 (032 Grenzfall → nein) | 5: Kürzen (032), Scheinlösung bauen (033), Rätsel (034), Probe in falscher Gleichung (035), Bedingungen gehören zur Umformung (036) | ja |
| verhaeltnis | 041 → 1 (040 Grenzfall → nein) | 5: Mischung (037), additiv/multiplikativ (038), Anteil halbieren (039), umgekehrtes Verhältnis (040), Bezugswert in Prozent (041) | ja |

Vier Tests mit verschiedenen Denkfiguren: ja (022 Lösungsverlust, 027 bzw. nach A1 028 Zählerverhältnis, 032 Kürzen, 037 Mischung).

## Schwierigkeit der Tests

| Test | Gutes Kind der 8. Klasse in 3–4 Minuten? | Was muss es verstanden haben? |
|---|---|---|
| 022 | Ja, in 1–2 Minuten (zu schnell, B1); ohne die genannte Lösung etwa 3 Minuten. | Ein neuer Nenner x verbietet die 0, und genau das war die einzige Lösung. |
| 027 | Ja, in 2–3 Minuten. | Gleiche Zähler bei verschiedenen Nennern: nie gleich; dann Routine. |
| 028 (als Test nach A1) | Ja, knapp in 3–4 Minuten. | Über Kreuz kommt es nur auf das Verhältnis der Zähler an, nicht auf die Nenner. |
| 032 | Ja, etwa 3 Minuten. | Kürzen mit x entfernt die Einschränkung x ≠ 0; die Lösung der gekürzten Gleichung ist in der Ausgangsgleichung verboten. |
| 037 | Ja, 3–4 Minuten. | Mit Mengen von Saft und Wasser rechnen, nicht mit Verhältniszahlen. |

## Protokoll (geprüfte Aufgaben)

| Kennung | Rechnung (Skript) | Optionen/Lücken | Schema? | Bestand | Befund |
|---|---|---|---|---|---|
| 022 | [0; 3] | eindeutig | nein | – | B1, C1, C2 |
| 024 | [2; 3; 9] | eindeutig | nein | T 45 Einsicht | B6 |
| 026 | [2; 3] | eindeutig | **ja** | BT 28/31 nur ähnlich | – |
| 027 | [7; 9], alle a ≠ 0 | eindeutig | Lücke 2 Routine | T 225 Frageart | A1 |
| 028 | 6, alle p ≠ −q | eindeutig | nein | – | A1 (als Test) |
| 029 | x = 11, Index 3 | eine richtig | nein | K8-V071 Einsicht | – |
| 030 | Index 0, alle Fälle | eine richtig | nein | – | B5 |
| 032 | [1; 0; 2], Scheinlösung 0 | eindeutig | Grenzfall → nein | T 224 Einsicht | B2, C2 |
| 033 | 28 | eindeutig | nein | K8-V081 genannt | B2 |
| 034 | 0, Scheinlösung 2 | eindeutig | **ja** | T 180, T 198 | B4, B6 |
| 035 | [3; 0] | **nicht eindeutig** (3 oder 4) | nein | – | A2, B2 |
| 036 | Index 1 für jedes c | eine richtig | nein | – | B3 |
| 037 | 400 | eindeutig | nein | – | – |
| 041 | 25 | eindeutig | **ja** | – | – |
