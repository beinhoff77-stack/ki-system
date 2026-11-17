# Postfach merksaetze (Siebzehnte Runde)

Neueste Meldung oben.

## 2026-11-17 02:32 – FERTIG
Siebzehnte Runde abgeschlossen (Zweig merksaetze, von lernen-app 2e95607, nicht gemergt, konfliktfrei mit dem aktuellen lernen-app). 8 Themen geändert, je Thema inhalt_pruefen OK ohne Hinweise und Nachweis mit inhalte/generatoren/_nacharbeit_nachweis.py OK: alle Aufgaben Zeichen für Zeichen unverändert, geändert nur schritte, bild bzw. fehler_bild der genannten Karten. Alle Änderungen im Generator, JSON neu erzeugt (die Generatoren erzeugen den freigegebenen Stand vorher exakt).

### 1. „Kurz gesagt“ – kein Merksatz zu ändern
Prüfskript inhalte/generatoren/_merksaetze_pruefen.py (Satzende wie beauftragt, Abkürzungen z. B., d. h., u. a., bzw., ca., usw., vgl. ausgenommen): In allen Themen mit gym_by-Klasse hat **kein** Merksatz einen ersten Satz mit mehr als 12 Wörtern oder 90 Zeichen (0 von 463 Karten in 68 Themen). Die etwa 75 aus dem Prüfbericht stammen aus allen 593 Karten: mit derselben Satzerkennung sind es 73 über 90 Zeichen bzw. 103 über 12 Wörter oder 90 Zeichen – **alle in Themen ohne gym_by** (Realschule, IB, Zusatz; noch im alten Kartenformat ohne einstieg). Die gym-Karten wurden beim Umbau nach der Vorgabe 16.11. schon gekürzt; der Ablauf der 87 Merksätze in den nächsten Satz ist ein App-Fehler (N2, Schritt A2 im Bau-Chat), kein Inhaltsfehler.
Annahme: Der Auftrag gilt wie geschrieben nur für gym_by („alle Kinder sind am Gymnasium“). Die 103 Merksätze in RS/IB/Zusatz-Themen habe ich nicht angefasst – soll das eine eigene Runde werden (dann zusammen mit dem Umbau dieser Karten auf das neue Muster)?
**Liste alt → neu:** keine Einträge (kein Merksatz geändert).

### 2. Steigungsdreieck (funktionen.linear)
- ablesen S3: „Die Zahl vor x ist ⟦m = 2⟧: 1 km weiter, 2 € mehr.“ → „Vor x: ⟦m = 2⟧. 2 km kosten 4 € mehr, 2 € je km.“ Dreieck (1 | 5) → (3 | 5) → (3 | 9).
- lage S1: „g: y = 2x + 1 hat die Steigung m₁ = 2.“ → „g: y = 2x + 1 hat m₁ = 2: 2 nach rechts, 4 hoch.“ Dreieck (0 | 1) → (2 | 1) → (2 | 5).
- lage S2: „h: y = −0,5x + 3 hat m₂ = −0,5.“ → „h: y = −0,5x + 3 hat m₂ = −0,5: 2 rechts, 1 runter.“ g-Dreieck wie S1; das h-Dreieck (war schon 2 breit) liegt jetzt bei (2 | 2) → (4 | 2) → (4 | 1), sonst läge es auf der senkrechten Seite des breiteren g-Dreiecks.
- deuten S3: „m = −1,5: Jede Stunde wird sie 1,5 cm kürzer.“ → „m = −1,5: In 2 Stunden wird sie 3 cm kürzer, 1,5 cm je Stunde.“ Dreieck (2 | 17) → (4 | 17) → (4 | 14).
Alle Schritte ≤ 15 Wörter. Danach gibt es in keinem gym-Thema mehr ein Steigungsdreieck in einer Erklärung, das die App bisher vergrößert hätte (einzig ablesen/fehler_bild ist 1 breit; dort vergrößert die App schon heute nicht, weil das große Dreieck aus dem Bild ragen würde, und der Text passt dazu).

### 3. Überdeckte Beschriftungen
Gesucht in allen Koordinaten-Bildern der gym-Themen (Kartenbild, jeder Schrittzustand, zusätzlich fehler_bild), (a) per Skript: Namen mit Ankerpunkten näher als 1 Einheit (_merksaetze_pruefen.py), (b) zur Kontrolle alle 513 Bilder mit lernKoordinaten aus lernen.js im Browser gezeichnet und echte Textkästen verglichen. Versetzt wurde über name_x am Graphen (die App kennt das Feld schon; Punkte bleiben, wo sie mathematisch liegen):
- funktionen.linear / deuten: „Kerze“ name_x 6 (überdeckte „leer“). proportional/fehler_bild: „2,5x“ name_x 2,8 (lag 0,76 neben „2x + 1“).
- funktionen.grundbegriffe / funktionswert: „Preis“ name_x 2 (überdeckte „(5 | 13)“ und im Fehlerbild „richtig“).
- funktionen.quadratisch / umformen/fehler_bild: „richtig“ name_x 6,3, „falsch“ name_x 4,5 (lagen übereinander).
- funktionen.trig / parameter: „f“ name_x 45° (S3) bzw. π/4 (S5) (überdeckte „kleinster: −2“). eigenschaften: „cos x“ name_x −300° (Karte) bzw. −5π/3 (S5) (überdeckte „270°“/„3π/2“).
- funktionen.potenz / negativ: „y = x⁻²“ name_x 1; wurzelfunktion S3: „y = ∛x“ name_x 4 (je 0,96 Einheiten; im Bild ohne Überdeckung, aber unter der Grenze).
- gleichungen.bruch / graphisch: „6/x“ name_x 1,5 (überdeckte „(3 | 2)“; nur im Bild gefunden, > 1 Einheit).
- gleichungen.exponential / wachstum S5: Ausschnitt x 8 … 13, y 1 300 … 1 700, damit „10 J.: 1 480 €“ und „11 J.: 1 539 €“ getrennt stehen; fehler_bild setzt x, y, schritt_y und punkte: [] selbst (sonst erbt es den Ausschnitt; die beiden Jahres-Punkte gehören nicht zum Fehler mit dem Faktor 0,04).
- gleichungen.ungleichungen / grafisch: „Geld“ name_x 1,5, „Ausgaben“ name_x 2,5 (überdeckten „S(4 | 17)“ bzw. „zu teuer“).
Danach: 0 Funde unter 1 Einheit; im Browser keine Überdeckung mehr über 6 px.

### offen geblieben (nicht beauftragt)
- Im Browser nur knapp berührend (≤ 6 px, nicht geändert): funktionen.exponential_log/werte S4, funktionen.gebrochen/achsenpunkte S4 + Fehler, funktionen.grundbegriffe/stelle Fehler und punkt_graph S4, gleichungen.lgs3/parabel (alle Zustände).
- Namen über Achsenzahlen (nicht Name gegen Name): funktionen.trig/parameter S2 „3 sin x“ und S4 „kleinster: −2“ liegen auf „270°“; „kleinster: −2“, „f(4)“ (potenz/negativ) und „8 → 2“ (potenz/wurzelfunktion) werden am rechten Rand abgeschnitten. Lösung wäre in der App (Namen am Rand nach links setzen) oder ein Inhaltsauftrag.
- Vierstellige y-Achsenzahlen (exponential/wachstum: „1 500“) werden links abgeschnitten – App.
- tools/__pycache__/inhalt_pruefen.cpython-313.pyc ist eingecheckt und wird bei jedem Lauf verändert; nicht mitcommittet.

## 2026-11-17 02:32 – STATUS
gleichungen.ungleichungen fertig: grafisch – „Geld“ (name_x 1,5) und „Ausgaben“ (name_x 2,5) versetzt (überdeckten „S(4 | 17)“ bzw. im Fehlerbild „zu teuer“, 0,51 Einheiten). Aufgaben 210 von 210 unverändert; inhalt_pruefen OK ohne Hinweise; Nachweis OK.

## 2026-11-17 02:32 – STATUS
gleichungen.exponential fertig: wachstum – Schritt 5 zeigt einen Ausschnitt (x 8 … 13, y 1 300 … 1 700), damit „10 J.: 1 480 €“ und „11 J.: 1 539 €“ nicht übereinander stehen (Punktnamen lassen sich nicht verschieben, ohne die Punkte zu ändern). fehler_bild setzt den vollen Ausschnitt (x 0 … 15, y 0 … 2 000) und leere Punkte wieder selbst, weil es sonst den Zustand von Schritt 5 erbt. Aufgaben 204 von 204 unverändert; inhalt_pruefen OK ohne Hinweise; Nachweis OK.

## 2026-11-17 02:32 – STATUS
gleichungen.bruch fertig: graphisch – „6/x“ mit name_x 1,5 versetzt (überdeckte „(3 | 2)“ in Schritt 2, 3 und im Fehlerbild; Abstand > 1 Einheit, aber im Bild überdeckt). Aufgaben 210 von 210 unverändert; inhalt_pruefen OK ohne Hinweise; Nachweis OK.

## 2026-11-17 02:31 – STATUS
funktionen.potenz fertig: negativ – „y = x⁻²“ (name_x 1) und wurzelfunktion Schritt 3 – „y = ∛x“ (name_x 4) versetzt (je 0,96 Einheiten neben „f(4)“ bzw. „8 → 2“; im Bild ohne Überdeckung, aber unter der Grenze von 1 Einheit). Aufgaben 204 von 204 unverändert; inhalt_pruefen OK ohne Hinweise; Nachweis OK.

## 2026-11-17 02:31 – STATUS
funktionen.trig fertig: parameter – Graphname „f“ in Schritt 3 (name_x 45°) und Schritt 5 (π/4) versetzt (überdeckte „kleinster: −2“); eigenschaften – „cos x“ im Kartenbild (name_x −300°) und Schritt 5 (−5π/3) versetzt (überdeckte „270°“ bzw. „3π/2“, 0,09 Einheiten). Aufgaben 294 von 294 unverändert; inhalt_pruefen OK ohne Hinweise; Nachweis OK.

## 2026-11-17 02:31 – STATUS
funktionen.quadratisch fertig: umformen/fehler_bild – „richtig“ (name_x 6,3) und „falsch“ (name_x 4,5) auseinander gesetzt (lagen 0,24 Einheiten übereinander). Aufgaben 238 von 238 unverändert; inhalt_pruefen OK ohne Hinweise; Nachweis OK.

## 2026-11-17 02:31 – STATUS
funktionen.grundbegriffe fertig: funktionswert – Graphname „Preis“ mit name_x 2 versetzt (lag 0,63 Einheiten neben „(5 | 13)“ bzw. „richtig“ und überdeckte sie). Nur Kartenbild dieser Karte; _TAXI für die anderen Karten unverändert. Aufgaben 240 von 240 unverändert; inhalt_pruefen OK ohne Hinweise; Nachweis OK.

## 2026-11-17 02:31 – STATUS
funktionen.linear Nachbesserung: proportional/fehler_bild – statt „2x + 1“ (lag mit name_x 1,5 im Schnittpunkt) jetzt „2,5x“ mit name_x 2,8 versetzt. Neues Prüfskript inhalte/generatoren/_merksaetze_pruefen.py („Kurz gesagt“ und Namen-Abstand < 1 Einheit). inhalt_pruefen OK ohne Hinweise; Nachweis OK (210 von 210 Aufgaben unverändert).

## 2026-11-17 02:40 – STATUS
funktionen.linear fertig: Steigungsdreiecke 2 Einheiten breit, Schritt-Texte angepasst (ablesen S3, lage S1+S2, deuten S3; in lage S2 liegt das h-Dreieck jetzt bei x = 2 … 4, weil es sonst auf dem breiteren g-Dreieck läge). Kerze: Graphname „Kerze“ mit name_x 6 versetzt (überdeckte „leer“). proportional/fehler_bild: Name „2x + 1“ versetzt (weniger als 1 Einheit neben „2,5x“). Aufgaben 210 von 210 unverändert; inhalt_pruefen OK ohne Hinweise; Nachweis OK.
