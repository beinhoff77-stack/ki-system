# Postfach durchsicht-rsib-1 (Neunzehnte Runde, Teil B, Chat 1)

## 2026-11-17 13:46 – FERTIG
Abschlussbericht Neunzehnte Runde, Teil B, Chat 1 (Zweig `durchsicht-rsib-1`, 12 Themen, 69 Lernkarten). Ein Thema = ein Commit, alle gepusht. Kein Merge, keine Datenbank, kein App-Code, keine Tests.

### Kurzfassung
- **Tatsache:** Alle 12 Dateien: `inhalt_pruefen` **OK, 0 Hinweise**. Jede Lernkarte hat jetzt mindestens **6 / 6 / 8 Übungen** (Stufe 1 / 2 / 3), dazu unverändert 1 Test, 3 Korrektur, 6 Sicherung. Jede Karte hat mindestens 2 Stufe-3-Aufgaben nach Prüfungsvorbild und mindestens 1 Knobelaufgabe (Rückwärtsdenken, Parameter, Begründen, Gegenbeispiel).
- **Tatsache:** 2 echte Fehler gefunden und behoben (Lösung widersprach der Frage): gleichungen.wurzel und funktionen.umkehr (Liste „ersetzt“, markiert mit FEHLER).
- **Tatsache:** „Kurz gesagt“: Nach dem Umbau gestern ist in diesen 12 Themen **kein** erster Merksatz-Satz länger als 12 Wörter oder 90 Zeichen (längster: 75 Zeichen). Die im Auftrag genannten „rund 100 zu lang“ stammen offenbar aus der Zeit vor dem Umbau. Nichts zu kürzen.
- **Hauptbefund (Meinung, begründet):** Die Stufen unterschieden sich vorher oft nur äußerlich. Typische Muster: Stufe 3 = dieselbe Rechnung als Auswahl mit Ablenkern; Stufe 3 = dieselbe Sachaufgabe wie Stufe 2; sechsmal dieselbe Frage mit getauschten Zahlen. Das ist jetzt behoben (umgestuft, ersetzt, ergänzt).
- **Technik:** Neue Hilfsdatei `inhalte/generatoren/_rsib1.py` (`nachtrag`: umstufen / ersetzen / neu / karten; rechnet jede Lösung mit „c“ nach, prüft Dopplungen und Mindestzahlen). In jedem Generator ein Abschnitt `# ---------- DURCHSICHT …`, der nach dem Umbau läuft. Alle übrigen Aufgaben bleiben Zeichen für Zeichen gleich (Nachweis per Skript gegen `origin/lernen-app`: geändert sind nur Stufe `s` der umgestuften Aufgaben, die ersetzten und die neuen Aufgaben, dazu eine Lernkarte).

### (1) Urteil je Thema (Noten 1–5; Stufen vorher → nachher)
| Thema | Schulart/Klasse | Thema passt | Erklärungen | Stufen vorher → nachher | freigabereif |
|---|---|---|---|---|---|
| abbildungen.determinanten2 | RS 7 | 2 – Flächen mit Determinanten in RS 7 I; JT 8 I prüft es | 2 – Beet-Situation, Bild je Schritt | 3 → 2 | ja |
| abbildungen.vektoren | RS 7 | 2 – passt; Titel „…und Determinanten“ irreführend | 2 – Mittelpunkt fehlte, ergänzt | 4 → 2 | ja |
| daten.stichproben | RS 7 | 2–3 – Lernbereich „Auswertung von Daten“ belegt, genaue Inhalte Annahme | 2 | 3 → 2 | ja |
| funktionen.scharen | RS 8 | 2 | 2 – Fall „0 · x = 0“ fehlt auf der Karte | 3–4 → 2 | ja |
| terme.quadratische_extreme | RS 8 | 1–2 – „8I.4“ quadratische Ergänzung/Extremwert | 2 | 3 → 2 | ja |
| funktionen.transformation | RS 9 | 3 – Karten spiegeln/punkte eher RS 10 | 2 | 3 → 2 | ja, mit Vorbehalt (Klasse der zwei Karten klären) |
| gleichungen.reinquadratisch | RS 9 | 1–2 | 2 | 3 → 2 | ja |
| gleichungen.wurzel | RS 9 | 2 – zwei_seiten braucht die Lösungsformel | 2 | 3–4 → 2 | ja (Fehler behoben) |
| abbildungen.matrizen | RS 10, MYP 4 | 3 – Inverse/Skalarprodukt im RS-Lehrplan nicht belegt; MYP-Zuordnung unsicher | 2 | 3 → 2 | ja, mit Vorbehalt (Umfang klären) |
| funktionen.umkehr | RS 10, MYP 4 | 2 – RS-AP 2021 verlangt Umkehrfunktion; MYP eher Extended | 2 | 3 → 2 | ja (Fehler behoben) |
| mengen.grundbegriffe | MYP 1 | 2 – üblich, nicht vorgeschrieben | 2 | 4 → 2 | ja |
| groessen.verhaeltnisse | MYP 2 | 2 – „Ratios“ MYP 1–3 | 2 | 3 → 2 | ja |

Begründung Stufen-Note „2“ statt „1“ nachher (Meinung): Stufe 1 und 2 sind teils weiter Zahlvarianten derselben Aufgabe; das ist für Stufe 1 so gewollt, bei Stufe 2 ist der Unterschied oft nur „negative Zahlen“ oder „Dezimalzahlen“ (kleine Abwandlung, aber kein neuer Gedanke).

### (2) Worin sich die Stufen unterscheiden – je Lernkarte (vorher → nachher)
**abbildungen.determinanten2 (RS 7)**

| Lernkarte | Stufen vorher | Stufen nachher (neu bzw. umgestuft) |
|---|---|---|
| det_berechnen | S1 positive Zahlen, S2 negative Zahlen (nur Vorzeichen), S3 x rückwärts + 1 Rechen-Auswahl | S3 zusätzlich Lücke wie JT, Determinante als Term in x, Vertauschen/Verdoppeln begründen. |
| parallelogramm | S1 Vektoren, S2 Punkte, S3 Maßstab + Rechen-Auswahl | Rechen-Auswahl S2; S3 Fläche als Term in x (AP), Rückwärts x, Sonderfall Fläche 0, Verdoppeln aller Koordinaten. |
| dreieck | S1 Vektoren, S2 Punkte, S3 Maßstab, x rückwärts, Rechen-Auswahl | Auswahl S2; S3 + Term in x (AP), x für 12 FE, C parallel zu AB verschieben. |
| umlaufsinn | S1 sechsmal „Det negativ – wie laufen?“, S2 Punkte→Umlauf/Fläche, S3 Reihenfolge, Fehler finden, kollinear | S1 mit 0 und positiv gemischt; S3 + x für kollinear, Bereich y > 0. |
| viereck | S1 Vektoren, S2 Punkte, S3 Rechen-Auswahl ×2, Fehler finden, Maßstab | Auswahl S2; S3 + Term in x (AP), x für 25 FE, andere Diagonale, rückwärts aus Fläche. |
| vieleck | S1 Vektoren, S2 Punkte, S3 Anzahl Dreiecke, Sechseck, Maßstab | + Term in x (AP), x für 31 FE, fehlende Determinante rückwärts. |

**abbildungen.vektoren (RS 7)**

| Lernkarte | Stufen vorher | Stufen nachher (neu bzw. umgestuft) |
|---|---|---|
| vektor_bestimmen | S1 Punkte positiv, S2 negativ, S3 4× Auswahl derselben Rechnung + Fußpunkt | S3: Fehler finden, Punkt R mit QR = PQ, Vektor in Abhängigkeit von x (AP), x für waagrecht, AB = BC deuten, B mit Bedingung. |
| bildpunkt | S3 2× Auswahl-Rechnung + Bild aus A→A′ | + P′ in Abhängigkeit von x (AP), x für P′ auf x-Achse, Urpunkt aus anderem Paar, zweimal verschieben rückwärts. |
| gegenvektor | S3 3× „Wo lag P“ (= S2), „rückgängig“ (= S1), Roboter | Urpunkte in x (AP), Viereck rekonstruieren, Bild des Bildes, Nullvektor, Fehler finden, w aus Gesamtweg. |
| addition | S3 Ergänze ×2, drei Verschiebungen ×3, Auswahl-Summe (= S1) | Rundweg DA, Boot mit Strömung, AB + BC unabhängig von B, AB + BA, passendes Paar finden. |
| punkt_berechnen | S3 Auswahl D ×2 (= S2), B gesucht, Mittelpunkt ×2 | C in Abhängigkeit von x (AP), x für C auf y-Achse, drei mögliche vierte Ecken, Fehler finden. |
| eigenschaften | S1 sechsmal „Länge bleibt“, S2 Aussagen, S3 A′B′ ×2, X→Y, Umfang ×3 | Fläche des Bilds, Fixpunkt ⇒ Nullvektor, |BB′| = |AA′|, AA′B′B Parallelogramm, A auf B schieben. |

**daten.stichproben (RS 7)**

| Lernkarte | Stufen vorher | Stufen nachher (neu bzw. umgestuft) |
|---|---|---|
| begriffe | S1 n ablesen/Grundgesamtheit, S2 n aus Prozent, S3 Division je Klasse | S3: Prozent rückwärts, Interviewer-Zahl (mehrschrittig), Grundgesamtheit bei Mehrstufen-Auswahl, Zufallsstichprobe erkennen, Vollerhebung unmöglich (Raketen). |
| hochrechnen | S1 Anteil, S2 hochrechnen, S3 rückwärts + Prozentpunkte + Auswahl-Rechnung | + Fang-Wiederfang, welche Hochrechnung vertrauenswürdiger, fehlende Anzahl rückwärts, Gegenanteil. |
| repraesentativ | S1 geeignet?, S2 beste Auswahl, S3 groß-verzerrt vs. klein-zufällig, Hauptproblem | + Mensa-Schlagzeile, Telefonumfrage (wer fehlt). |
| fehlerquellen | S1 suggestiv, S2 Fehlerquelle benennen, S3 Verbesserung + 2× Benennen | + neutrale Frage wählen, zwei Fehlerquellen zugleich, „mehr aus derselben Gruppe“ hilft nicht, Rücklaufquote. |
| aussagen | S1 sechsmal „welche schwankt weniger“, S2 Schätzwert/Spannweite, S3 Zeitung ×3, knapp 49/51, Prozentpunkte | S1 gemischt; S3 + Trend-Aussage prüfen, 5-%-Hürde, 0,5-Prozentpunkte-Rechnung, Mindestanzahl für Mehrheit, Werbeaussage. |

**funktionen.scharen (RS 8)**

| Lernkarte | Stufen vorher | Stufen nachher (neu bzw. umgestuft) |
|---|---|---|
| einsetzen | S1 Gleichung, S2 y-Wert, S3 Gleichung wählen/Punktprobe | S3: k aus Punkt (auch mit (k − 1)x + 2k), Bereich k > 3, gemeinsamer y-Wert, Taxi zweischrittig, Unterschied ohne Rechnen, P(0 | 5) unmöglich, doppelt so steil. |
| parallelenschar | S1 t aus P, S2 t ablesen/Dezimal, S3 Parallele durch P + 4× Fehler finden | + t für Nullstelle 6, Gerade 3 tiefer, Unterschied der Achsenabschnitte. |
| bueschel | S1 Z ablesen, S2 m aus Q, S3 m aus Z/Q, Senkrechte, Auswahl Z (= S1) | + Z nach Ausklammern (AP), Gerade durch Ursprung, m für Nullstelle. |
| wirkung | S1 waagrecht, S2 Steigung/parallel/fallend, S3 k aus Graph, Ursprung ×3 | + „steiler als“, k im Achsenabschnitt. |
| loesung_parameter | S1 einsetzen, S2 kein k / Schnitt-x, S3 Fallunterscheidung, keine Schnittpunkte ×3 | + k für Schnitt bei x = 4, unendlich viele Lösungen, positive Lösung. |
| sachaufgabe | S1 Preis, S2 m, S3 4× Auswahl m (= S2) + gleich teuer | Ersparnis-Vergleich, Grundgebühr aus zwei Angaben (AP), Tarifgleichung aus zwei Angaben, Gleichstand nach Preisänderung, kWh rückwärts. |

**terme.quadratische_extreme (RS 8)**

| Lernkarte | Stufen vorher | Stufen nachher (neu bzw. umgestuft) |
|---|---|---|
| ergaenzen | S1 +b, S2 −b, S3 ungerade b, Fehler finden, Auswahl (= S1) | + Lücken rückwärts (49), 4x² + 12x (Faktor), Abstand zum Quadrat. |
| scheitelform | S1/S2 ergänzen, S3 Ausmultiplizieren + kleinster Wert | S3: e als Dezimalzahl, Lücken rückwärts, Fehler finden, c aus Scheitelform, „immer positiv“ begründen, passenden Term wählen, Termgleichheit, x² − 5x. |
| extremwert | S1 ablesen, S2 mit Faktor, S3 aus Normalform, Aussagen | + c für kleinsten Wert 4, unerreichbarer Wert. |
| mit_faktor | S1/S2 ganzzahlige Faktoren, S3 0,5-Faktoren, Fehler finden, 2× Min/Max (= S1) | + a aus Extremstelle, A(x) = −0,5x² + … (AP), welcher Term hat Maximum, c für negatives Minimum. |
| optimierung | S1 Umfang/Summe, S2 Mauer/Kiosk, S3 Differenz, Mauer, Kiosk ×2, Summe ×2 | S3: Rechteck (10 − x)(2x + 2) Stelle und Wert (AP), Kinopreis, Quadratsumme, Hausecke. |

**funktionen.transformation (RS 9)**

| Lernkarte | Stufen vorher | Stufen nachher (neu bzw. umgestuft) |
|---|---|---|
| nach_oben | S1 Gleichung, S2 Scheitel verschieben, S3 Ablesen/rückwärts | S3: Verschiebung durch P, e aus Nullstellen, Abstand zweier Parabeln, keine Nullstelle, Symmetriepunkt. |
| nach_rechts | S1 Scheitel, S2 Deutung, S3 Ablesen + y-Werte | S3: zwei mögliche d, d mit Lagebedingung, y-Achsenschnitt, gleicher y-Wert in der Mitte, d aus y-Wert 16, Fehler finden. |
| strecken | S1 y-Werte, S2 a aus Punkt, S3 a ablesen (Bruch), enger | + Brückenbogen (AP-Sachaufgabe), Wert aus anderem Punkt. |
| spiegeln | S1 Punkte, S2 Scheitel, S3 4× Gleichung nach x-Achsen-Spiegelung | S3: Doppelspiegelung, Punktprobe am Bild, Schnittpunkt Bild/Urbild, welche Spiegelung. |
| kombiniert | S1 ablesen, S2 Gleichung aus Beschreibung, S3 Fehler ×3, Ablesen, y-Wert | S3: Gleichung aus Scheitel und Punkt (AP), Nullstellen, a und e aus zwei Punkten, Verschiebungsvektor. |
| punkte | S1 eine Abbildung, S2 kombiniert, S3 4× Fehler + rückwärts | S3: rückwärts, Scheitel von −f(x + 3) + 1, Scheitelform von g, f(0) aus g, kein Fixpunkt. |

**gleichungen.reinquadratisch (RS 9)**

| Lernkarte | Stufen vorher | Stufen nachher (neu bzw. umgestuft) |
|---|---|---|
| schaetzen | S1 zwischen, S2 näher an/TR, S3 Fehler ×4 + ganze Zahl | S3: ordnen, Anzahl ganzer Zahlen, „länger als 17 m?“, Anzahl möglicher a. |
| grundform | S1 Quadratzahlen, S2 Dezimal/keine, S3 Bruch, Fehler | + a aus Lösungen (Lehrplan: Gleichung zu Lösungsmenge), genau eine Lösung, keine Lösung für a < 4. |
| umformen | S1 +c, S2 beidseitig, S3 Fehler, Dezimal, 3× L = { } | + Bruchform, Klammer, c aus Lösungen. |
| gerundet | S1 eine Dezimale, S2 zwei Dezimalen, S3 Klammer gerundet + exakte Lösung (= S1) | + flächengleiches Quadrat, flächengleicher Kreis (AP), Probe mit gerundetem Wert, Einschachteln auf eine Dezimale. |
| klammer | S1/S2 (x ± p)² = q, S3 Fehler, a(x − p)² + c, L = { } | + binomische Formel erkennen, genau eine Lösung. |
| sachaufgabe | S1 Quadrat/Fall, S2 gerundet, S3 Terrasse ×4, Stein, Kreis-Fehler | S3: verbreitertes Grundstück, Würfeloberfläche, Bremsweg, Fallzeiten-Vergleich, Fläche ×4 → Seite ×2, dreifache Kreisfläche, Rechteck 2x · x. |

**gleichungen.wurzel (RS 9)**

| Lernkarte | Stufen vorher | Stufen nachher (neu bzw. umgestuft) |
|---|---|---|
| definitionsmenge | S1 x + c, S2 ax + c, S3 einsetzen ×3, ≤-Fall, Gleichung | S3: zwei Wurzeln (Intervall), Gleichung, kleinste ganze Zahl, √(x²), a rückwärts. |
| quadrieren | S1/S2 lösen, S3 Fehler, Dezimal, √(x : 2) | + c rückwärts, √(8x + 4) ohne Lösen, √(x² + 9) = 5. |
| isolieren | S1 +c, S2 a · √ + c, S3 Fehler ×4, Minus vor √ | S3: Wurzel auf beiden Seiten, Division, 10 − 2√, c rückwärts. |
| probe | S1 √ = negativ, S2 Probe/D, S3 warum, a√ + b = negativ ×3, Fehler | + wann √x = c lösbar, keine Scheinlösung bei positiver rechter Seite, Ausgangsgleichung zur Scheinlösung. |
| zwei_seiten | S1 √ = √, S2 mit Hinweis auf Scheinlösung, S3 ohne Hinweis | + √(2x + 3) = x, √(x²) = x. |
| sachaufgabe | S1/S2/S3 alle Beet/Fallzeit/Aufprall | S3: Pendel, doppelte Fallzeit, dreifache Geschwindigkeit, Fläche ×4, Sichtweite (Prüfungsklassiker), Fallzeit + 3 s, v = h, Höhe verdoppelt. |

**abbildungen.matrizen (RS 10, IB MYP 4)**

| Lernkarte | Stufen vorher | Stufen nachher (neu bzw. umgestuft) |
|---|---|---|
| bildpunkt | S1/S2 Zeile mal Spalte, S3 Urpunkt, Matrix aus Gleichungen, 2× Auswahl | + Bildpunkte in x (AP), k der Affinität, Fixpunkt, Bild über Einheitspunkte. |
| abbildungsmatrix | S1 anwenden, S2 erkennen, S3 nennen/erkennen + Fehler | S3: Matrix aus Bildern der Einheitspunkte, orthogonale Affinität (AP), k der Streckung, zweimal Punktspiegelung, Einheitsmatrix, Spiegelung an y = −x, 180°-Drehung. |
| drehung | S1–S3 x′/y′ runden, S3 + Abstand | S3: Winkel aus Bildpunkt, cos φ = 0,5, zwei Drehungen, exaktes Bild bei 90°, Quadrat-Symmetrie, Bild auf x-Achse. |
| rechnen | S1 Vielfache/Summe, S2 Produkt, S3 vertauschbar?, Verkettung, Auswahl | + D · D, vertauschbar für jedes x, A · A = E. |
| inverse | S1 det, S2 Inverse, S3 Parameter, Urpunkt | + det = 1, Inverse der Drehung. |
| skalarprodukt | S1 rechnen, S2 senkrecht, S3 Fehler ×4, Winkel | S3: t für 45°, rechter Winkel im Dreieck, Winkel 0°, Senkrechte mit Vorgabe. |

**funktionen.umkehr (RS 10, IB MYP 4)**

| Lernkarte | Stufen vorher | Stufen nachher (neu bzw. umgestuft) |
|---|---|---|
| umkehrbar | S1 Formel, S2 Graph/Tabelle, S3 Menge ×4, Begründung | + a aus Scheitel (Verknüpfung quadratische Ergänzung), welche Funktion auf ℝ, Monotonie begründen, Wert streichen. |
| werte | S1 Tabelle, S2 f⁻¹(b)/D, S3 W von f⁻¹, f⁻¹(f(x)) | + f(x) = f⁻¹(x), doppeltes f⁻¹, verschobenes f⁻¹, unlösbare Bedingung. |
| linear | S1/S2 Umkehrgerade, S3 Prüfen mit Zahl ×4, Auswahl | + m rückwärts, eigene Umkehrfunktion, Schnittpunkt f/f⁻¹, aus zwei Punkten, Steigung 1 : m, t aus Punkt auf f⁻¹. |
| quadratisch | S1 √, S2 verschobener Ast, S3 Punkt, D, „warum einschränken“ ×3 | + x aus f⁻¹(x) = 3, W von f⁻¹, linker Ast (−√x). |
| exp_log | S1 Logarithmen, S2 mit Summand, S3 Fehler, Umkehr von 5ˣ ± c, Punkte | + 2ˣ⁻¹, 3 · 2ˣ, f⁻¹(−4) unmöglich, lg 0,001. |
| spiegeln | S1 Punkte tauschen, S2 Gerade/Spiegelung, S3 „sicher auf f⁻¹“, Fehler | + Fixpunkt auf y = x, Achsenschnittpunkte von f⁻¹ aus f (3 Varianten). |

**mengen.grundbegriffe (IB MYP 1)**

| Lernkarte | Stufen vorher | Stufen nachher (neu bzw. umgestuft) |
|---|---|---|
| elemente | S1 ∈/Anzahl, S2/S3 Aufzählung | S3: Menge in Worten, Reihenfolge egal, Quersumme 5, Doppelte zählen einmal, gerade Primzahlen, Vielfache zählen, Zahl mit 5 Teilern, Quadrat < 50. |
| schnitt | S1 ablesen, S2 Teiler/Vielfache, S3 Namen ×4, leere Menge | + B passend wählen, ggT, kgV, Vielfache von 15, A ∩ B = A, Lisa-Logik. |
| vereinigung | S1/S2 bilden/zählen, S3 rückwärts + Formel ×5 | + disjunkt, „beides“ aus „keines“, n(B) rückwärts, Höchstzahl, B rekonstruieren. |
| venn | S1/S2 ablesen, S3 Bereiche berechnen (= Beispiel) | S3: Überlappung aus „keines“, x im Venn-Diagramm (MYP-Klassiker), nur Gemüse, Widerspruch erkennen, Prozent, Mindest-Überlappung. |
| verstehen (Vertiefung) | S1 höchstens, S2 Teilmengen/Tom, S3 Wiederholungen + mindestens + Lea | + disjunkt-Formel, Gegenbeispiel, Mindestgröße 0, immer wahre Aussage, n(A ∪ B) = n(A). |

**groessen.verhaeltnisse (IB MYP 2)**

| Lernkarte | Stufen vorher | Stufen nachher (neu bzw. umgestuft) |
|---|---|---|
| kuerzen | S1 Sachverhältnis, S2 Zahlen/Einheiten, S3 dreiteilig, Dezimal | + Brüche, Anteil aus Verhältnis, Verhältnis nach Zuwachs (Knobel). |
| gleichwertig | S1/S2 ergänzen, S3 Ina ×3, Mischung | + mittlere Proportionale, dreiteiliges Rezept, gleichwertige Paare finden, Gesamtzahl aus Teil. |
| aufteilen | S1/S2 aufteilen, S3 Differenz/Teil gegeben, dreiteilig | + Erbe aus kleinstem Teil, Rechteck aus Umfang. |
| proportion | S1/S2 Dreisatz, S3 Hemden ×3, Maßstab rückwärts | + Maler (antiproportional), Wechselkurs, Maßstab bestimmen, Poster. |
| einheitsrate | S1/S2 Rate/Vergleich, S3 Äpfel ×4 + Vergleich | S3: Stückpreisdifferenz, „4 nehmen, 3 zahlen“, Literpreis-Ersparnis, Reichweite, Seiten/Minute, Läuferinnen. |
| aenderung | S1/S2 Rate, S3 Tank vorwärts ×4, Kerze, Mäher | S3: Anfangswert rückwärts, Zeit bis Füllstand, Temperatur rückwärts, zwei Kerzen gleich hoch, Pool leer, Bedeutung negativer Rate, Rate aus Tabelle, Sinkrate. |

### (3) Zahlen
| Thema | umgestuft | berichtigt | ersetzt | neu | Lernkarten verbessert |
|---|---|---|---|---|---|
| abbildungen.determinanten2 | 6 | 0 | 2 | 20 | 0 |
| abbildungen.vektoren | 14 | 0 | 4 | 26 | 1 (punkt_berechnen: Schritt „Mittelpunkt“ + Wort) |
| daten.stichproben | 8 | 0 | 5 | 18 | 0 |
| funktionen.scharen | 8 | 0 | 5 | 20 | 0 |
| terme.quadratische_extreme | 9 | 0 | 3 | 19 | 0 |
| funktionen.transformation | 7 | 0 | 7 | 19 | 0 |
| gleichungen.reinquadratisch | 6 | 0 | 5 | 18 | 0 |
| gleichungen.wurzel | 5 | 0 | 8 | 17 | 0 |
| abbildungen.matrizen | 8 | 0 | 6 | 20 | 0 |
| funktionen.umkehr | 6 | 0 | 6 | 19 | 0 |
| mengen.grundbegriffe | 16 | 0 | 4 | 26 | 0 |
| groessen.verhaeltnisse | 9 | 0 | 6 | 21 | 0 |
| **Summe** | **102** | **0** | **61** | **243** | **1** |

Geänderte Lernkarte: abbildungen.vektoren / punkt_berechnen – vorher: nur „vierte Ecke des Parallelogramms“, obwohl Stufe-3-Aufgaben den Mittelpunkt verlangten; nachher: Schritt 4 „Mittelpunkt M von [AC]: A plus halber Vektor AC ergibt M(3 | 2)“ mit Bild, Wort „Mittelpunkt“ in `woerter`.

### (4) Liste „ersetzt“ (alte Fragetexte; da Entwurf: Abgleich mit 'loeschen')
FEHLER = die alte Aufgabe war falsch gelöst.
**abbildungen.determinanten2** (2)
- Für A, B, C ist die Determinante aus AB und AC gleich −15. Wie laufen die Ecken A → B → C?
- Für A, B, C ist die Determinante aus AB und AC gleich −6. Wie laufen die Ecken A → B → C?

**abbildungen.vektoren** (4)
- Welcher Vektor führt von A(2 | −1) nach B(−5 | 7)?
- Welcher Vektor führt von A(−4 | 5) nach B(4 | 3)?
- Ein Dreieck mit dem Umfang 13 cm wird zuerst mit v = (−1 | −6) und danach mit dem Gegenvektor verschoben. Welchen Umfang hat das Ergebnis?
- Ein Dreieck mit dem Umfang 19 cm wird zuerst mit v = (6 | −4) und danach mit dem Gegenvektor verschoben. Welchen Umfang hat das Ergebnis?

**daten.stichproben** (5)
- In einer Schule gibt es 4 Klassen. Aus jeder Klasse werden per Los gleich viele Kinder gezogen, insgesamt 16. Wie viele sind es pro Klasse?
- In einer Schule gibt es 12 Klassen. Aus jeder Klasse werden per Los gleich viele Kinder gezogen, insgesamt 84. Wie viele sind es pro Klasse?
- Stichprobe A hat 12 Befragte, Stichprobe B hat 400. Beide wurden zufällig ausgewählt. Welche schwankt vermutlich weniger?
- Stichprobe A hat 10 Befragte, Stichprobe B hat 500. Beide wurden zufällig ausgewählt. Welche schwankt vermutlich weniger?
- Eine Zeitung schreibt: „20 % der Einwohner von Würzburg wollen ein Stadion!“ Grundlage: 2 von 10 Personen in einer Fußballkneipe sagten ja. Wie ist die Aussage zu beurteilen?

**funktionen.scharen** (5)
- Liegt der Punkt P(−2 | −4) auf der Geraden der Schar y = (k + 2) · x + 2k mit k = −6?
- Liegt der Punkt P(1 | −18) auf der Geraden der Schar y = (k − 3) · x + 2k mit k = −5?
- Jemand rechnet für die Schar y = 2,5x + t und P(4 | −1): t = 9. Was stimmt?
- Ein Handwerker berechnet 40 € Anfahrt plus m € pro Stunde. Für 4 Stunden bezahlt man 240 €. Wie hoch ist m?
- Ein Stromtarif kostet 12 € Grundgebühr im Monat plus m € pro kWh. Für 250 kWh bezahlt man 74,50 €. Wie hoch ist m?

**terme.quadratische_extreme** (3)
- T(x) = x² + 3x − 4. Welchen kleinsten Wert kann T(x) annehmen?
- T(x) = x² − x + 4,5. Welchen kleinsten Wert kann T(x) annehmen?
- T(x) = x² + 7x + 15. Welchen kleinsten Wert kann T(x) annehmen?

**funktionen.transformation** (7)
- Berechne den y-Wert der Parabel y = (x + 3)² an der Stelle x = 1.
- Berechne den y-Wert der Parabel y = (x + 4)² an der Stelle x = −5.
- Die Parabel y = (x − 3)² − 5 wird an der x-Achse gespiegelt. Welche Gleichung hat das Bild?
- Die Parabel y = (x − 2)² − 2 wird an der x-Achse gespiegelt. Welche Gleichung hat das Bild?
- Jemand liest bei y = 2(x + 5)² + 2 den Scheitel S(5 | 2) ab. Was stimmt?
- P(−2 | −4) liegt auf f. Jemand rechnet für g(x) = f(x − 2) den Bildpunkt P'(−4 | −4). Was stimmt?
- P(2 | −3) liegt auf f. Jemand rechnet für g(x) = f(x − 1) den Bildpunkt P'(1 | −3). Was stimmt?

**gleichungen.reinquadratisch** (5)
- Jemand schätzt √238 ≈ 119. Was stimmt?
- Jemand schätzt √237 ≈ 118,5. Was stimmt?
- Welche Lösungsmenge hat 5x² + 6 = 0?
- Eine quadratische Terrasse soll 58 m² groß werden. Wie lang wird eine Seite? Runde auf eine Dezimale.
- Eine quadratische Terrasse soll 133 m² groß werden. Wie lang wird eine Seite? Runde auf eine Dezimale.

**gleichungen.wurzel** (8)
- FEHLER: Jemand löst √(2x − 19) = 1 so: 2x − 19 = 1, also x = 10. Was stimmt?
- Jemand quadriert √(x − 15) + 4 = 12 sofort und erhält x − 15 + 16 = 144. Was stimmt?
- Jemand quadriert √(x − 15) + 4 = 18 sofort und erhält x − 15 + 16 = 324. Was stimmt?
- Löse 5 · √(x + 1) + 17 = −23.
- Ein quadratisches Beet wird an jeder Seite um 4 m verlängert. Die neue Seitenlänge ist √A + 4 = 24 m. Wie groß war die alte Fläche A?
- Für die Fallzeit gilt t = √(h : 5) (h in m, t in s). Ein Ball fällt 1,5 s lang. Aus welcher Höhe fiel er?
- Ein quadratisches Beet wird an jeder Seite um 3 m verlängert. Die neue Seitenlänge ist √A + 3 = 6 m. Wie groß war die alte Fläche A?
- Für die Aufprallgeschwindigkeit nach einem Fall gilt näherungsweise v = √(20 · h) (v in m/s, h in m). Aus welcher Höhe muss etwas fallen, um mit 35 m/s aufzuprallen?

**abbildungen.matrizen** (6)
- Welche Abbildung beschreibt die Matrix (0  1; −1  0)?
- Welche Abbildung beschreibt die Matrix (−1  0; 0  1)?
- P(1 | −5) wird um O um 150° gedreht. Berechne x' auf zwei Dezimalen.
- P(5 | 5) wird um O um 200° gedreht. Berechne y' auf zwei Dezimalen.
- Jemand berechnet für a = (2 | 2) und b = (6 | −3): a · b = (12 | −6). Was stimmt?
- Jemand berechnet für a = (−1 | −2) und b = (−4 | −4): a · b = (4 | 8). Was stimmt?

**funktionen.umkehr** (6)
- Auf welcher Menge ist f(x) = (x − 5)² umkehrbar?
- Auf welcher Menge ist f(x) = (x + 5)² umkehrbar?
- Jemand gibt für f(x) = −0,25x + 1,25 die Umkehrfunktion g(x) = −4x + 1,25 an. Prüfe mit x = 1.
- Jemand gibt für f(x) = 0,5x + 3,5 die Umkehrfunktion g(x) = 2x + 3,5 an. Prüfe mit x = 2.
- Warum muss man bei f(x) = (x − 4)² + 2 die Definitionsmenge auf x ≥ 4 einschränken, um f⁻¹ zu bilden?
- FEHLER: Jemand spiegelt P(3 | −3) für die Umkehrfunktion zu P'(−3 | 3). Was stimmt?

**mengen.grundbegriffe** (4)
- A = die Teiler von 12. Welche Aufzählung ist richtig?
- A = die Teiler von 20. Welche Aufzählung ist richtig?
- Klasse 6a: A = Kinder in der Englisch-AG = {Ali; Eva; Finn; Gül; Lio}, B = Kinder, die im Chor singen = {Dana; Hanna; Kim; Lio; Noah}. Wer ist in A ∩ B?
- Sportverein: A = Mitglieder im Tennis = {Gül; Hanna; Ida; Jonas; Lio; Noah}, B = Mitglieder im Schwimmen = {Ali; Ben; Dana; Ida; Jonas; Noah}. Wer ist in A ∩ B?

**groessen.verhaeltnisse** (6)
- Ina sagt: „7 : 9 = 14 : 16, weil ich zu beiden Zahlen 7 addiert habe.“ Stimmt das?
- 4 Hemden hängen nebeneinander auf der Leine und sind nach 50 Minuten trocken. Wie lange brauchen 12 Hemden, die ebenfalls gleichzeitig hängen?
- Äpfel kosten 2,40 € pro kg. Wie viel kosten 20 kg?
- Äpfel kosten 2,40 € pro kg. Wie viel kosten 10 kg?
- Ein Tank wird mit 4 Litern pro Minute gefüllt. Am Anfang sind 59 Liter darin. Wie viele Liter sind es nach 6 Minuten?
- Ein Tank wird mit 6 Litern pro Minute gefüllt. Am Anfang sind 49 Liter darin. Wie viele Liter sind es nach 4 Minuten?

### (5) Für den Nutzer (Entscheidung nötig)
1. **funktionen.transformation (RS 9):** Die Karten „spiegeln“ (an den Achsen) und „punkte“ (g(x) = a · f(x − d) + e für beliebige f) gehen über die Parabeln der RS 9 hinaus; das Abbilden von Graphen steht nach meiner Recherche in RS 10 I (Lernbereiche 2–4). Vorschlag: beide Karten als Vertiefung führen oder in Klasse 10 verschieben. (Annahme, Lehrplantext nicht selbst gelesen.)
2. **abbildungen.matrizen:** Ob inverse Matrix, Matrizenprodukt und Skalarprodukt zum RS-10-Stoff gehören, konnte ich nicht belegen (belegt ist nur „Abbildung mit Matrix“, „10I.2“). Für IB sind Matrizen kein Standard-Inhalt des MYP-Frameworks; MYP 4 ist eine Annahme. Teil C sollte das klären.
3. **abbildungen.vektoren:** Titel „Vektoren und Determinanten“ passt nicht (Determinanten stehen in abbildungen.determinanten2); `umfang` in der Themenliste nennt Skalarprodukt (steht in matrizen). Titel/umfang anpassen?
4. **Reihenfolge:** Für vektoren, determinanten2, matrizen ist `reihenfolge.rs_by` leer. Sinnvoll: vektoren vor determinanten2 (determinanten2 setzt „Spitze minus Fuß“ voraus); gleichungen.reinquadratisch vor gleichungen.wurzel; funktionen.umkehr nach den Exponentialfunktionen.
5. **Generatoren mit Fehlervarianten:** In gleichungen.wurzel (Fehlerfrage bei rechter Seite 1) und funktionen.umkehr (Spiegel-Fehlerfrage bei x = −y) erzeugt der alte Generator-Code Aufgaben, deren „Fehler“ gar keiner ist. Ich habe die betroffenen Aufgaben ersetzt; der Generator-Code selbst ist unverändert (sonst ändern sich alle Aufgaben). Bei einem späteren Neubau dort eine Ausschlussbedingung einbauen.
6. **App-Wünsche (unverändert offen):** echte Matrix-Klammer; Zeichnungsart „venn“; hohle Punkte auf dem Zahlenstrahl; Graph-Art √(x − a) + b.
7. **funktionen.scharen / loesung_parameter:** Die Karte erklärt nur „keine Lösung“ (k = 2); der Fall „0 · x = 0 → unendlich viele Lösungen“ kommt nur in einer neuen Knobelaufgabe (mit Tipp) vor. Soll die Karte einen 5. Schritt bekommen?

### (6) Was ich nicht prüfen konnte / nicht gemacht habe
- **Lehrplantexte und Prüfungsaufgaben nur aus Suchergebnissen:** Der Abruf ganzer Seiten (lehrplanplus.bayern.de, ISB-PDFs) brauchte eine Freigabe, die nicht beantwortet wurde. Ich kenne die Lehrplan- und Prüfungsinhalte deshalb nur aus Suchauszügen und Lehrwerk-Gliederungen (Mathe.Logo-Stoffverteilungspläne, GeoGebra-Kennungen wie „8I.4“, „10I.2“). Die Klassenzuordnungen oben sind entsprechend als belegt / Annahme gekennzeichnet.
- **Erklärungen nachziehen (Auftrag Punkt 3):** Nicht gemacht außer der einen Karte. Die Karten sind seit gestern (Paket umbau-rest) nach dem neuen Muster gebaut (Bild je Schritt bei Bildwechsel); `fehler_bild` fehlt weiter bei den Karten, die umbau-rest begründet ausgelassen hat (Denk- statt Zeichenfehler). Ich halte die Begründungen für stichhaltig.
- **Zeichnungen nicht gerendert:** Der neue Schritt in vektoren/punkt_berechnen ist nur per Prüfskript, nicht im Browser angesehen. Neue Aufgaben haben keine Grafiken.
- **Gelesen:** alle Lernkarten ganz; alle Übungen der Stufen 2 und 3 und die ersten drei der Stufe 1 je Karte; aus Test/Korrektur/Sicherung je eine Aufgabe je Karte (vom selben Generator wie Stufe 2). Zahl- und Lückenaufgaben mit „c“ sind vom Prüfskript nachgerechnet; Auswahlaufgaben habe ich stichprobenartig von Hand nachgerechnet (dabei die zwei Fehler gefunden). Alle 243 neuen Aufgaben habe ich selbst geschrieben, gelesen und von Hand nachgerechnet.
- Nicht mit Kindern getestet.

### Prüfungsquellen (Vorbilder für Typ und Niveau, nie wörtlich übernommen)
- Realschul-Abschlussprüfung Mathematik I, ISB-Beispielaufgabe B 4 („Parallelogramme AnBnCnDn … Flächeninhalt in Abhängigkeit von x“): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Mathematik/Weiterentwicklung_Abschlusspruefung/Beispielaufgaben_Abschlusspruefung_I/aufgabenbeispiel_apmi_b4.pdf → determinanten2, vektoren, matrizen
- Abschlussprüfung 2021 Mathematik I (A 1.2 Umkehrfunktion): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Mathematik/Weiterentwicklung_Abschlusspruefung/Zeichenkatalog/2021_MI_HT.pdf → umkehr
- Abschlussprüfung 2004 Mathematik II (A(x), kleinstmöglicher Flächeninhalt): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2002-2010/2004_MII_HT-A-B-C_NT.pdf → quadratische_extreme
- Abschlussprüfung 2011 Mathematik I (A(x), Flächeninhalt vorgegeben → x): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2011/mathe_i_haupttermin_angaben.pdf → determinanten2, quadratische_extreme
- Jahrgangsstufentest 8 I 2021 (Determinante, Lücken ergänzen): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2021/2021_jt_mathe_8_i_angabe.pdf → determinanten2
- Jahrgangsstufentest 8 I 2025 (Mittelpunkt): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/2025_JT_Mathematik_8_I_Loesung.pdf → vektoren
- ISB Leistungsaufgaben 7 I / 8 I / 9 I: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Mathematik/Weiterentwicklung_Abschlusspruefung/Exemplarische_Leistungsaufgaben/rs_m_09_leistungsaufgaben_9i.pdf (analog 7i, 8i) → reinquadratisch, wurzel
- IB MYP: Mathematics skills framework (Zusammenfassung): https://www.ibo.org/globalassets/new-structure/research/pdfs/myp-math-skills-framework-summary-en.pdf; Themenübersicht Standard/Extended: https://www.revisiondojo.com/blog/what-topics-are-in-myp-standard-mathematics → mengen, verhaeltnisse, matrizen, umkehr
- Lehrplan-Zuordnung (Annahmen, s. o.): Mathe.Logo-Stoffverteilungspläne 7 I/10 I (ccbuchner.de), GeoGebra-Sammlungen mit Lehrplan-Kennung.

## 2026-11-17 13:43 – STATUS
groessen.verhaeltnisse fertig: 9 umgestuft, 6 ersetzt, 21 neu (Stufe 3: antiproportionale Falle, Maßstab bestimmen, „4 nehmen, 3 zahlen“, zwei Kerzen, Rate aus Tabelle). inhalt_pruefen: OK, 0 Hinweise. Alle 12 Themen durch; Abschlussbericht folgt.

## 2026-11-17 13:42 – STATUS
mengen.grundbegriffe fertig: 16 umgestuft (Stufe 3 bestand fast nur aus Stufe-2-Aufgaben), 4 ersetzt, 26 neu (Stufe 3: x im Venn-Diagramm, Mindest-Überlappung, ggT/kgV als Schnittmenge, Aussagen mit Gegenbeispiel). inhalt_pruefen: OK, 0 Hinweise.

## 2026-11-17 13:40 – STATUS
funktionen.umkehr fertig: 6 umgestuft, 6 ersetzt – darunter ein FEHLER: „Jemand spiegelt P(3 | −3) … zu P′(−3 | 3)“ war als falsch markiert, ist aber richtig (Generator-Variante bei x = −y). 19 neu (Stufe 3: Schnittpunkt f/f⁻¹, Umkehrgerade aus zwei Punkten, Achsenschnittpunkte von f⁻¹, linker Parabelast). inhalt_pruefen: OK, 0 Hinweise.

## 2026-11-17 13:38 – STATUS
abbildungen.matrizen fertig: 8 umgestuft, 6 ersetzt, 20 neu (Stufe 3: Bildpunkte in Abhängigkeit von x, orthogonale Affinität, Fixpunkt, Drehwinkel rückwärts, rechter Winkel mit Skalarprodukt). inhalt_pruefen: OK, 0 Hinweise.

## 2026-11-17 13:37 – STATUS
gleichungen.wurzel fertig: 5 umgestuft, 8 ersetzt – darunter ein FEHLER: „Jemand löst √(2x − 19) = 1 so: 2x − 19 = 1, also x = 10“ war als falsch markiert, ist aber richtig (Generator-Variante bei rechter Seite 1). 17 neu (Stufe 3: Definitionsmenge mit zwei Wurzeln, Pendel, Sichtweite, Fallzeit-Vergleiche). inhalt_pruefen: OK, 0 Hinweise.

## 2026-11-17 13:35 – STATUS
gleichungen.reinquadratisch fertig: 6 umgestuft, 5 ersetzt, 18 neu (Stufe 3: Gleichung zu gegebener Lösungsmenge, flächengleiche Figuren, Bremsweg, Fallzeiten-Vergleich, binomische Formel erkennen). inhalt_pruefen: OK, 0 Hinweise.

## 2026-11-17 13:34 – STATUS
funktionen.transformation fertig: 7 umgestuft (Ablesen und Einsetzen von Stufe 3 auf 2), 7 ersetzt (u. a. viermal gleiche Spiegel-Frage), 19 neu (Stufe 3: Parabel aus Scheitel und Punkt, Brückenbogen, a und e aus zwei Punkten, zwei mögliche Verschiebungen). inhalt_pruefen: OK, 0 Hinweise.

## 2026-11-17 13:32 – STATUS
terme.quadratische_extreme fertig: 9 umgestuft, 3 ersetzt (scheitelform: „kleinster Wert“ gehört zur nächsten Karte), 19 neu (Stufe 3: Lücken rückwärts, Parameter c, A(x) nach AP-Muster, Einnahmen-Optimierung). inhalt_pruefen: OK, 0 Hinweise.

## 2026-11-17 13:31 – STATUS
funktionen.scharen fertig: 8 umgestuft, 5 ersetzt, 20 neu (Stufe 3: Parameter aus Punktprobe, Büschelpunkt nach Ausklammern, Tarif aus zwei Angaben, unendlich viele Lösungen). inhalt_pruefen: OK, 0 Hinweise.

## 2026-11-17 13:29 – STATUS
daten.stichproben fertig: 8 umgestuft, 5 ersetzt (u. a. aussagen Stufe 1: sechsmal dieselbe Frage), 18 neu (Stufe 3: Fang-Wiederfang, Schlagzeilen und Werbeaussagen prüfen, Rücklaufquote, Mindestanzahl). inhalt_pruefen: OK, 0 Hinweise.

## 2026-11-17 13:27 – STATUS
abbildungen.vektoren fertig: 14 umgestuft (Auswahl-Rechnungen von Stufe 3 auf 2 bzw. 1), 4 ersetzt, 26 neu (Stufe 3), Lernkarte punkt_berechnen um den Schritt „Mittelpunkt“ ergänzt (kam in Aufgaben vor, war nicht erklärt). inhalt_pruefen: OK, 0 Hinweise.

## 2026-11-17 13:24 – STATUS
abbildungen.determinanten2 fertig: 6 umgestuft (reine Rechen-Auswahl von Stufe 3 auf 2), 2 ersetzt (umlaufsinn Stufe 1: sechsmal dieselbe Frage), 21 neue Stufe-3-Übungen
(je Karte 2 nach Prüfungsvorbild „Fläche in Abhängigkeit von x“ / „Lücke in der Determinante“ und 1–2 Knobelaufgaben). Jede Karte jetzt 6/7–8/8–9. inhalt_pruefen: OK, 0 Hinweise.
