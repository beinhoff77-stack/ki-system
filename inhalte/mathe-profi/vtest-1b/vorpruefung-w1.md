# Vorprüfung W1 – Einheit 20 `gleichungen.bruch` (VT1B-022 bis 041), Stand d79f5d3e

Umfang: die 20 Aufgaben der neuen Menge (4 Lernziele × 1 Test + 2 Korrektur + 2 Sicherung). `vorrat-folgerunde/` nicht geprüft. Maßstab: Urteil 1222 und `vtest-1/auftrag.md`. Nichts an Aufgaben geändert.

Werkzeug: `vorpruefung_w1_rechnen.py` (eigenes Verfahren: Gleichung · Produkt der Nenner wird exakt mit `Fraction` interpoliert, rationale Nullstellen gegen D geprüft, jeder Parameterwert einzeln gelöst, Sachgrößen auf Sinn geprüft; dazu Abdeckung der Lücken und Fehlbilder ≠ Lösung). Ergebnis: **alle 20 Sollwerte bestätigt, jede Lücke hat ein eigenes Fehlbild, kein Fehlbild gleich der Lösung.** Die Vorschläge unten sind im selben Skript nachgerechnet. `tools/vtest_pruefen.py --runde 1b`: für Einheit 20 nur die erwartete Pool-Meldung („2 statt 3“) und ein Hinweis zu 025 (siehe C1).

Bestand gelesen: `inhalte/themen/gleichungen.bruch.json` (325 Aufgaben, alle Texte), `rollend-7` (21), `rollend-11` (5), `rollend-13` (14); `rollend-15` enthält keine Datei und keine Bruchgleichung dieser Einheit. Zahlen „T n“ unten = Position n (ab 0) in `themen/gleichungen.bruch.json`.

## Urteil

**Bereit für die Gegenprüfung: nein.** Rechnung, Eindeutigkeit und Fehlbild-Abdeckung sind sauber, aber nach strengem Schema-Maßstab liegen alle vier Lernziele über einer Schema-Aufgabe, fünf Aufgaben haben denselben Kern wie eine Bestandsaufgabe der Einheit (darunter der Test 022), und der Test zu `scheinloesung` (032) enthält keine Scheinlösung. **9 A, 10 B, 10 C.**

## Fakt und Einschätzung

- Fakt (gerechnet): alle Sollwerte; 027 ohne Lösung genau k ∈ {0; 4} (k = 0 Scheinlösung x = −2, k = 4 Widerspruch); 032 nur b = −1 Identität, **für kein b eine Scheinlösung**; 026 Gleichung hat x ∈ {−9; 6}, sinnvoll nur 6; 030 richtig umgeformt (x + 3)² = 7(x − 1) ohne reelle Lösung, Maras 20/3 ist keine Lösung; 037 einziges Paar (20; 30); 038 Äpfel 50 ≥ 20.
- Fakt (Quelle: Bestandstext, unten wörtlich angeführt): Doppelungen.
- Einschätzung (von Hand): Schema, Denkfiguren, Bauart. Schema hier streng: lösbar durch das Standardverfahren (D bestimmen → Hauptnenner → lösen → gegen D prüfen), durch eine bekannte Regel oder bloßes Ausrechnen, auch wenn die Aufgabe als Fehler-Detektiv oder Auswahl verpackt ist und das Ausrechnen allein die richtige Möglichkeit liefert. Im Zweifel Schema.

## Befunde A (Muss)

| Nr. | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| A1 | 032 (Test scheinloesung) | Für kein b ∈ [−9; 9] entsteht eine Scheinlösung (Skript); für b ≠ −1 fällt x weg (falsche Aussage), für b = −1 Identität. Die Antwort 18 hängt nicht von D ab – wer x = 4 nie bedenkt, erhält auch 18. Der Test prüft das Lernziel nicht; dazu dieselbe Denkfigur (Identität nach dem Malnehmen) wie Test 022. | Test mit echter Scheinlösung im Parameter, z. B. (x + b)/(x − 4) = 3/(x − 4) + 2 → x = b + 5; Lücken „keine Lösung für b = □, für b = 2 ist x = □“ → [−1; 7] (geprüft: nur b = −1 ohne Lösung, Kandidat 4 verboten). |
| A2 | 022 (Test definitionsmenge) | Bestand T 233: „Jemand löst (x − 4)/(x − 4) = 1 und sagt: ‚Jede Zahl ist eine Lösung.‘ … Falsch: Alle Zahlen außer 4.“ und T 237 („Wie viele Lösungen hat x/(x − 1) + 1/(1 − x) = 1? … alle x ≠ 1“). Gleiche Rechnung (Malnehmen → wahre Aussage), gleicher Fehler (Einschränkung nach dem Malnehmen vergessen), gleiche Frage (welche/wie viele Lösungen); neu ist nur das Abzählen im Intervall. Zudem Schema-Grenzfall (Standardverfahren liefert L = D). | Identität mit zwei Nennern, die erst über den Hauptnenner sichtbar wird: 1/x − 1/(x + 1) = 1/(x(x + 1)), „wie viele ganze Zahlen von −12 bis 12 sind Lösung?“ → 23 (geprüft; Fehlbilder 24 = nur eine Ausnahme, 25 = keine). |
| A3 | 031 | Bestand T 143: „Zum Zähler und zum Nenner von 5/8 wird dieselbe Zahl x addiert. Der neue Bruch hat den Wert 3/4. Bestimme x.“ 031 ist dieselbe Aufgabe mit 5/11 und 2/3 (Ersatz der Sirup-Aufgabe ist wieder Bestand). | Ersetzen, nicht durch ein weiteres Zähler-Nenner-Rätsel. Denkfigur „Verfahren wählen“: „Welche der vier Gleichungen darf man sofort über Kreuz multiplizieren?“ mit einer Summe, die schon ein Bruch ist ((x + 1)/(x − 2) = 3/x), gegen echte Summen (1/(x − 2) + 1 = 3/x) und Differenzen; vorher gegen T 130 und T 104 prüfen. |
| A4 | 028 | Bestand T 102: „Welche Gleichung entsteht aus 3/x = 5/(x + 2) durch Multiplizieren über Kreuz?“ (auch K8-V073). Gleiche Rechnung und Frage; 028 ergänzt nur das Ausmultiplizieren. Zugleich die erklärte Schema-Aufgabe. | Ersetzen (nicht durch eine weitere Identität – die gibt es schon in 022/032). Wenn A3 wie vorgeschlagen „Verfahren wählen“ wird, hier z. B. Fehler-Detektiv „x² fällt nach Über-Kreuz weg“ (x/(x + 2) = (x − 1)/(x + 3) → x = −1), Kim bricht in Zeile 2 ab, weil sie x² für unlösbar hält; gegen T 99/T 144 abgrenzen (dort nur Lösen). |
| A5 | 034 | Bestand T 198: „Gib die Lösungsmenge von 1/(x − 1) + 1/(x + 1) = 2/(x² − 1) an“ (L = { }, Kandidat 1) und `rollend-7` K8-V079 (Lücken „einziger Kandidat x = ②, … ④ Lösungen“). Gleicher Nenner x² − 1, gleiche Scheinlösung 1, gleiche Frage – die Korrektur-Notiz („anderer Kern“) trifft nicht zu. Dazu Schema (Standardverfahren) und `typ: umkehr`, obwohl nichts umgekehrt wird. | Ersetzen, z. B. Umkehrung: „Wähle c so, dass 3/(x − 1) = c/(x² − 1) keine Lösung hat“ → c = 6 (einziger Kandidat dann 1); Fehlbilder c = 3, c = −6. |
| A6 | 038 + 037 | Bestand T 251: „Jungen : Mädchen = 4 : 5. Kommen 2 Jungen dazu, ist es 1 : 1. Wie viele Mädchen?“ 038 (5 : 3, 20 Äpfel weg, gleich viele) = gleiche Rechnung (Unterschied der Teile = Änderung), gleiche Frage. Außerdem prüfen Test 037 und Korrektur 038 dieselbe Einzelfrage (Teile-Ansatz k mit einer Änderung, neue Verhältnisgleichung) – Verstoß gegen „Test und Korrektur nicht dieselbe Einzelfrage“. | 038 ersetzen durch eine neue Denkfigur, z. B. umgekehrtes Verhältnis: „Für dieselbe Strecke brauchen A und B Zeiten im Verhältnis 3 : 4. In welchem Verhältnis stehen ihre Geschwindigkeiten?“ Lücken [4; 3], Fehlbild [3; 4] (im Bestand der Einheit nicht gefunden). |
| A7 | Schema definitionsmenge | 023 (erklärt: Nenner nie 0, dann x² = 1) und 025 (Fehler-Detektiv: Zeile 3 erklärt die Lösung selbst zur verbotenen Zahl – sofort sichtbar; Lücke 2 ist „D eines Nenners bestimmen“, genau die Übung laut `abgrenzung`). Grenzfall 022 (siehe A2). → 2 sicher, 3 mit Grenzfall. | 025: Fehler nicht offen benennen lassen, z. B. Nenner (x − 5) und (2x − 10), Mara schließt 5 und 10 aus (Nennerzahl statt Nullstelle); Lücken „Fehler in Zeile □, ausgeschlossen sind □ Zahlen“ → [1; 1]. |
| A8 | Schema ueber_kreuz | 028 (A4), 029 (nur Möglichkeit 3 nennt x = 10 – Ausrechnen mit Über-Kreuz wählt sie, ohne Jos Weg zu beurteilen), 031 (Standard-Rätsel, A3). → 3. Dazu 029 Bauart: die richtige Möglichkeit ist die einzige Sammel-Option („Beide …“). | 029: zwei Möglichkeiten mit x = 10 (z. B. „Nur Kim erhält sicher x = 10; Jos Weg trifft hier zufällig, ist aber keine Regel“ – Folgerung falsch, also erlaubt) und eine zweite „Beide …“-Möglichkeit mit falscher Folgerung (z. B. „Beide erhalten x = 8, denn …“, 24 : 3 = 8 als x gelesen). |
| A9 | Schema scheinloesung und verhaeltnis | scheinloesung: 033 (erklärt), 034 (A5), 036 (Regel „Bruch = 0 ⇔ Zähler 0, Nenner ≠ 0“ löst beide Lücken); Grenzfall 035 (Standardverfahren liefert L = { }, nur eine Möglichkeit sagt das). verhaeltnis: 038 (erklärt), 039 (18 · 2,5 ausrechnen wählt die Möglichkeit; Idas Weg steht im Text), 041 (Seite 6 → 9 → 81 ohne die Einsicht „Fläche mit Faktor²“; Einsicht wie Bestand T 250, Hausmodell 1 : 20 Fläche); Grenzfall 040 (eine Addition 7 + 12). → je 3 sicher, 4 mit Grenzfall. | Nach A1/A5/A6: 036 als Auswahl „Welche Gleichung hat keine Lösung, obwohl der Zähler eine Nullstelle hat?“ mit vier Gleichungen; 041 umkehren (Flächen 4 : 9 bekannt, Seitenverhältnis gesucht, Fehlbild 4 : 9) oder Auswahl gegen „Fläche wächst wie die Seite“; 039 siehe B6. |

## Befunde B (Soll)

| Nr. | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| B1 | Tests 022, 027, 032 | Drei der vier Tests haben dasselbe Format „Wie viele ganze Zahlen von … bis … (einschließlich)“; ein Abzählfehler im Intervall (25/20/19 Zahlen) wertet Verstehen als falsch, und zwei Tests (027, 032) tragen dieselbe Denkfigur „Ausnahmewerte eines Parameters“. | Höchstens ein Zähl-Test; 032 wie A1 als gekoppelte Lücken, 022 ggf. als Auswahl „L = …“. |
| B2 | 027 (Test ueber_kreuz) | Zumutbar und eindeutig (geprüft), aber der Kern ist Fallunterscheidung und Scheinlösung (k = 0), also Stoff von `scheinloesung`; zum Über-Kreuz-Kern (wann erlaubt, richtig aufstellen) prüft er nur den ersten Schritt. Grundmenge (x ∈ ℚ) nicht genannt. Als Vertiefung M8 4 vertretbar. | Grundmenge ergänzen; wenn A1 umgesetzt ist, droht Doppelung der Denkfigur mit dem neuen 032 – dann 027 auf den Fall k = 4 (0 · x = −12) oder auf „wann ist Über-Kreuz erlaubt“ ausrichten. |
| B3 | 030 | Lücke 2 ist ja/nein (50 %) und folgt aus Lücke 1; ihr Inhalt ist die Antwort von Bestand T 130 („Tom rechnet 2/x = 3/(x + 1) + 1 über Kreuz … Über Kreuz geht nur, wenn auf jeder Seite genau ein Bruch steht“). Die richtige Fortsetzung führt auf eine quadratische Gleichung ohne Lösung (M9). | Lücke 2 ersetzen durch „richtig zusammengefasst: (x + □)/(x − 1)“ → 3 (geprüft); in `w` vermerken, dass die Gleichung danach keine Lösung hat und das erst in M9 gezeigt wird – oder rechte Seite so wählen, dass linear bleibt. |
| B4 | 036 Fehlbilder Lücke 2 | Antwort 4 „x = 4 als Lösung genommen“ passt nicht zu einer Anzahl-Lücke (wer x = 4 nimmt, schreibt 1); Antwort 1 „als 1 gekürzt und gedacht, es gebe genau eine Lösung“ ist in sich widersprüchlich (1 = 0 hat keine Lösung). | Fehlbild 1: „x = 4 gezählt, weil der Zähler dort 0 ist“; Fehlbild 4 durch eine Anzahl ersetzen, die eine echte Rechnung ergibt. |
| B5 | 035 Bauart | Möglichkeiten 0 und 3 haben dieselbe Folgerung L = {5} – ein Testkluger streicht beide ohne Verständnis (Rest 50 %); die richtige ist zudem die längste (82 gegen 69–75 Zeichen). | Möglichkeit 3 mit eigener falscher Folgerung, z. B. „L = ℚ, denn 7/0 = 7/0 zeigt, dass beide Seiten immer gleich sind“ (geprüft falsch). |
| B6 | 039 | Der Text nennt Idas (richtigen) Weg und Bens (falschen) Weg – die Aufgabe ist faktisch Ben oder Ida (50 %); 7,2 cm und „bleibt 18 cm“ sind kaum gewählte Ablenker. Richtige Möglichkeit ist die längste und die einzige mit „beide/demselben“. `form: zwei_wege`, obwohl nur ein Weg gültig ist. | Namen und Wege aus dem Text; Ablenker mit echten Fehlern: 36 cm (additiv), 20 cm (12 · 30 : 18, Verhältnis vertauscht), 27 cm (Faktor 18 : 12 auf die Höhe); alle vier Möglichkeiten gleich gebaut (geprüft: nur 45 richtig). |
| B7 | 026 Bauart | Die richtige Möglichkeit ist die Schnittmenge: Gleichung wie Möglichkeit 0, Satzteil wie Möglichkeit 2; nur 1 und 2 übernehmen das Fragewort „als Kinderzahl“. | Alle vier im selben Satzrahmen „…, und als Kinderzahl kommen … in Frage, denn …“; vierte Möglichkeit mit falscher Gleichung **und** falscher Menge so bauen, dass jede Hälfte zweimal richtig und zweimal falsch vorkommt, ohne dass die richtige die einzige Kreuzung ist (z. B. zwei falsche Gleichungen mit je richtiger und falscher Menge). |
| B8 | Etiketten 023, 034 (`umkehr`), 031, 033, 036 (`darstellung`) | Keine Umkehr bzw. kein Darstellungswechsel; genau diese Aufgaben sind Schema-Kandidaten, und das Werkzeug erkennt „Verstehen“ nur über `typ`/`form`. Das Etikett verdeckt die Schema-Zählung. | Ehrlich etikettieren; was dann nicht als Verstehen gilt, ist zu ersetzen (siehe A7–A9). |
| B9 | 023 | Lücke 2 verlangt „genau zwei Lösungen“ von x² = 1; dass es nur ±1 gibt, ist in M8 nicht begründbar (Quadratwurzel/reinquadratische Gleichungen M9). Einsicht „Nenner nie 0“ wie Bestand T 38 (1/(x² + 1)), Gleichungsrahmen wie K8-V069 (5/(x² − 4) = 1). | Lineare Variante: (x − 3)/(x² + 4) = 0, Lücken „nicht definiert für □ Zahlen, Lösung x = □“ → [0; 3] (geprüft). |
| B10 | Denkfiguren scheinloesung, verhaeltnis; 037 | scheinloesung: 033 (A), 034, 036 (zweite Gleichung) teilen den Schritt „einziger Kandidat = verbotene Zahl ⇒ L = { }“; 032 hat keine Scheinlösung. Verschieden bleiben 4 nur, wenn Identität (032) mitzählt. verhaeltnis: 4 laut Schreiber; 037/038 teilen eine, 039 und 041 berühren beide „Vergrößern mit Faktor“ – bei strenger Zählung 3. 037: der eigene `bestandsvergleich.md` nennt als Bestand „3 : 5, je 4 dazu ergibt 2 : 3“ (`groessen.verhaeltnisse`/Datenbank; in den Repo-Dateien nicht gefunden) – gleicher Kern wie 037. | Nach A1/A5/A6 neu zählen; 037 gegen die Datenbank prüfen und bei Treffer Kern ändern (z. B. verschiedene Summanden oder Rückwärts „welche Zahl addieren“). |

## Befunde C (Kann)

| Nr. | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| C1 | 025 | Werkzeug-Hinweis „Zeile 2 … rechnet falsch: 8 = 2“ ist ein Fehlalarm (liest „8 = 2x − 10“ an). Stufe 3 für diese Aufgabe zu hoch. | Zeile 2 als „Ausmultiplizieren: 8 = 2x − 10, also x = 9“; Stufe 2. |
| C2 | 022 | Fehlbild Antwort 1 („nur die verbotene Zahl 2 als Lösung“) kaum plausibel; `typ: begruenden` bei Zahl-Antwort ohne Begründung. | Fehlbild 23 (zusätzlich eine zweite Zahl ausgeschlossen) oder 12 (nur positive gezählt). |
| C3 | 023 | Fehlbild Lücke 2 Antwort 4 („±1 und ±2“) unplausibel. | Mit B9 erledigt. |
| C4 | 027, 032 | Fehlbild 17 von 027 („einen weiteren Wert ausgeschlossen“) nennt keine Rechnung; Grundmenge fehlt in beiden. | Konkreten Wert nennen (z. B. k = −8, weil dort x = 0 herauskommt); „x ∈ ℚ“ ergänzen. |
| C5 | 029 | Begründung der richtigen Möglichkeit („doppelter Zähler verlangt doppelten Nenner“) trägt nur Jos Weg. | „…, denn beide Wege nutzen a : c = b : d“. |
| C6 | 031 | Fehlbild 23 („über Kreuz mit vertauschten Brüchen … Unbekannte nicht abgezogen“) passt nicht zu 3 · 11 − 2 · 5; Fehlbild 12 ist der neue Zähler. | Mit A3 erledigt. |
| C7 | 041 | Stufe 3 für reine Rechnung zu hoch; Bezug zu Bruch-/Verhältnisgleichung schwach. | Mit A9. |
| C8 | 026 | „Welche Werte kommen für x als Kinderzahl in Frage?“ – nach dem Lösen nur 6; gemeint ist „vor dem Lösen“. `form: bruecke` passt nicht. | „… kommen für x überhaupt in Frage, bevor man die Gleichung löst?“ |
| C9 | 027, 028, 030 | Dreimal der Bruch 4/(x − 1), 028 und 030 zusätzlich 7/(x + 3). Verrät nichts, wirkt aber wie eine Aufgabe in drei Fassungen. | Zahlen streuen. |
| C10 | Einheit | Auswahl `verhaeltnis` statt `graphisch` ist in `auswahl.md` begründet (Muster VRVRVVR). | – |

## Tabelle je Lernziel

| Lernziel | Test | Schema (streng) | verschiedene Denkfiguren | Test ok? |
|---|---|---|---|---|
| definitionsmenge | 022 | 023, 025 (+ Grenzfall 022) → 2–3 | 5: Identität (022), nie null (023), rückwärts a (024), Lösung ≠ verbotene Zahl (025), D gegen sinnvolle Werte (026) | nein: Kern = Bestand T 233/T 237 (A2) |
| ueber_kreuz | 027 | 028, 029, 031 → 3 | 5 nominal; 028 und 031 Bestand, nach Ersatz neu zählen | ja (zumutbar, eindeutig), Vorbehalt B2 |
| scheinloesung | 032 | 033, 034, 036 (+ Grenzfall 035) → 3–4 | 4 knapp: Identität (032), Kandidat verboten (033/034/036b), Probe 7/0 (035), Bruch = 0 (036a) | nein: keine Scheinlösung, Antwort ohne D (A1) |
| verhaeltnis | 037 | 038, 039, 041 (+ Grenzfall 040) → 3–4 | 4 laut Schreiber, streng 3 (037/038 gleich, 039/041 verwandt) | nein: dieselbe Einzelfrage wie Korrektur 038 (A6); sonst anspruchsvollste |

## Protokoll je Aufgabe

| Kennung | Pool | Rechnung (Skript) | Ablenker verboten? | Schema? | Bestand | Weitere |
|---|---|---|---|---|---|---|
| 022 | Test | 24 ok | – | Grenzfall | T 233, T 237 (A2) | B1, C2 |
| 023 | K | [0; 2] ok | – | ja | T 38, K8-V069 (B9) | x² = 1 M9 (B9), Etikett (B8), C3 |
| 024 | K | 14 ok, eindeutig | – | nein (rückwärts) | T 33 anderer Kern | – |
| 025 | S | [3; 5] ok | – | ja | – | offenkundiger Fehler (A7), C1 |
| 026 | S | Gleichung {−9; 6}, Index 1 ok | nein | nein | T 45 gleiche Einsicht, andere Denkleistung | B7, C8 |
| 027 | Test | 18 ok (k = 0, 4) | – | nein | neu | B1, B2, C4 |
| 028 | K | Index 3 ok | nein | ja | T 102 (A4) | – |
| 029 | K | x = 10, Index 3 ok | nein | ja (A8) | T 274 andere Denkleistung | Sammel-Option (A8), C5 |
| 030 | S | [1; 0] ok; richtige Gleichung ohne reelle Lösung | – | nein | T 130 (B3) | ja/nein-Lücke (B3) |
| 031 | S | 7 ok | – | ja | T 143 (A3) | C6 |
| 032 | Test | 18 ok (nur b = −1) | – | nein | neu, aber Denkfigur = 022 | keine Scheinlösung (A1), B1, C4 |
| 033 | K | 1 ok | – | ja | T 222/T 217 (Teil B) | Etikett (B8) |
| 034 | K | [1; 0] ok | – | ja | T 198, K8-V079 (A5) | Etikett (B8) |
| 035 | S | L = { }, Index 1 ok | nein | Grenzfall | T 200/T 192 gleiche Rechnung, neue Probe-Fehlvorstellung | B5 |
| 036 | S | [6; 0] ok | – | ja | T 233 verwandt | Fehlbilder Lücke 2 (B4) |
| 037 | Test | [20; 30] ok, eindeutig | – | Grenzfall (Teile-Ansatz) | laut eigenem Bestandsvergleich „3 : 5, je 4 dazu“ (B10) | A6 |
| 038 | K | 30 ok, Größen positiv | – | ja | T 251 (A6) | A6 |
| 039 | K | 45, Index 0 ok | nein | ja (A9) | – | B6 |
| 040 | S | 19 ok | – | Grenzfall | – | – |
| 041 | S | 81 ok | – | ja (A9) | T 250 gleiche Einsicht | C7 |

Verbotene Ablenker (richtige Folgerung, nur falsche Begründung): in 026, 028, 029, 035, 039 keiner gefunden.
