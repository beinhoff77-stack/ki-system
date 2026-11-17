# Postfach pruefung-winkelsaetze (Prüfung Flug „Winkelsätze“, Klasse 7)

## 2026-11-17 02:40 – FERTIG
Geprüft: `inhalte/themen/geometrie.winkelsaetze.json` und Generator auf `lernen-app` (Stand 5742532). Nichts geändert.
Umfang: alle 8 Etappen (Erklärung, Bildergeschichte, README-Regeln mit Wort- und Satzzählung per Skript) und **alle 224 Bordkarten** gelesen (je Etappe 28), Lösungen nachgerechnet,
Zeichnungen per Skript geprüft (beschriftete Winkel gegen gezeichnete Winkel, Lage „rechts oberhalb“ usw. gegen das Bild).
Prüfskript `tools/inhalt_pruefen.py`: OK (8 Lernkarten, 224 Aufgaben, 168 nachgerechnet). Mengen je Etappe wie im Auftrag (Stufe 1/2/3 = 4/6/8, 1 Test, 3 Korrektur, 6 Sicherung).
Lehrplan nachgelesen: LehrplanPLUS M7 2.2 (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik). Dort: Scheitel-, Neben-, Stufen-, Wechselwinkel; Beweis der Innenwinkelsumme
ausgehend von „Wechselwinkel an Parallelen sind gleich groß“ (oder umgekehrt); Fundamentalsatz vs. abgeleiteter Satz; Hilfslinien; Vieleck; Parallelität prüfen. **Außenwinkel kommt nicht vor.**
Lineare Gleichungen stehen erst in M7 3, gleichschenklige Dreiecke (Basiswinkel) erst in M7 5.

Keine falsche Zahl-Lösung gefunden. Probleme liegen bei Eindeutigkeit, Lehrplan-Reihenfolge, Zeichnungen und Einstufung.

### A. Muss vor der Freigabe geändert werden
| Etappe | Bordkarte | Befund |
|---|---|---|
| stufen_wechsel | Sicherung #51 „Wie heißen der Winkel bei S rechts oberhalb und der Winkel bei T links unterhalb?“ → „weder noch“ | Fachlich angreifbar. Nach verbreiteter Schulbuch-Definition (verschiedene Seiten der schneidenden Geraden **und** der geschnittenen Geraden, „beide innen oder beide außen“) ist das ein Wechselwinkelpaar (äußere Wechselwinkel); die Winkel sind auch gleich groß. Ein Kind mit Schulbuch-Wissen wird als falsch bewertet. Vorschlag: Aufgabentyp nur mit eindeutigen Paaren (z. B. S rechts oberhalb / T rechts unterhalb) oder „weder noch“ streichen. |
| stufen_wechsel | Übung S3 #39 „… Welchen Winkel bildet [CB] rechts bei C mit g?“ (ohne Zeichnung) | Mehrdeutig: Ob B rechts von C liegt und ob der Winkel unter- oder oberhalb von g gemeint ist, steht nicht da – 70° oder 110°. Zeichnung ergänzen oder Lage genau beschreiben. |
| parallel_pruefen | Übung S3 #67, #69, #71, #73 „Unter welchem Winkel schneiden sich g und h?“ | Lösungsweg und Tipp nutzen den **Außenwinkelsatz** – der kommt erst in Etappe 5. Entweder in Etappe aussenwinkel/figuren verschieben oder über Winkelsumme im Dreieck begründen (dann auch erst nach Etappe 4). |
| innenwinkelsumme | Bildergeschichte Schritt 2–4 | Kernschritt des Beweises ohne Bild: Die Wechselwinkel an C auf der Hilfslinie p werden nicht eingezeichnet (Schritte 2–4 erben das Bild von Schritt 1). README: Jeder Schritt, in dem sich im Bild etwas ändert, braucht ein eigenes `bild`. Außerdem „Links von C entsteht α“ – genauer „ein Winkel so groß wie α“. |
| stufen_wechsel, innenwinkelsumme, aussenwinkel, vieleck | #42, #44, #45, #97, #98, #126, #127, #129, #150, #157 | Lösung nur mit linearer Gleichung (Term mit x gleichsetzen). Lineare Gleichungen kommen laut LehrplanPLUS erst in M7 3, also nach diesem Flug. Als Stufe-3-Vertiefung kennzeichnen oder ohne Variable stellen. (Weitere Aufgaben wie #4, #6, #12, #88, #100, #155 sind auch durch Überlegen lösbar – nur den x-Ansatz im Lösungsweg durch „Teile“ ersetzen.) |
| innenwinkelsumme | Übung S3 #97, #98 „Wie groß ist x?“ | Einheit „°“ bei x falsch: x ist eine Zahl (die Winkel sind (x + 27)°). Antwort zeigt „28°“. Einheit weglassen oder nach dem Winkel fragen. Beide Aufgaben haben zudem dieselbe Lösung 28. |

### B. Sollte geändert werden (Lehrplan-Reihenfolge, Einstufung, Zeichnungen)
| Etappe | Bordkarte | Befund |
|---|---|---|
| aussenwinkel | ganze Etappe | Außenwinkel steht nicht im LehrplanPLUS M7 2.2, ist hier aber Pflicht (testrelevant). Vorschlag: als Vertiefung führen (bewertung.lernziele_vertiefung) – Entscheidung Sebastian, der Auftrag hatte die Etappe ausdrücklich verlangt. |
| aussenwinkel | Übung S2 #117, #119; Test #130; Korrektur #131; Sicherung #135–#139; Übung S3 #122 | Nutzen „gleichschenklig“ und gleiche Basiswinkel (Basiswinkelsatz) – Stoff von M7 5, kommt später. 8 von 10 Test/Korrektur/Sicherung-Karten dieser Etappe sind genau dieser Typ. |
| figuren | Übung S3 #181, #185 | Ebenfalls Basiswinkel im gleichschenkligen Dreieck (M7 5). |
| figuren | alle 28 Bordkarten | Keine einzige Zeichnung, obwohl die Etappe „Winkel in Figuren bestimmen“ heißt (Lehrplan: „Figuren mit mehrfachen Geradenkreuzungen“). Parallelogramm-, Trapez-, Rauten- und Dreieck-zwischen-Parallelen-Aufgaben sind in Worten schwer vorstellbar. Zeichnungsart `figur` ist vorhanden. |
| vieleck | alle 28 Bordkarten | Keine Zeichnung; für Stufe 1/2 (Fünfeck zerlegen) wäre ein Bild hilfreich. Weniger dringend als figuren. |
| beweisen | Test #214, Korrektur #215–#217, Sicherung #218–#223 | Prüfen nur Scheitel-/Neben-/Stufenwinkel zuordnen (Stoff der Etappen 1–2), nicht das Lernziel der Etappe (Fundamentalsatz vs. abgeleiteter Satz, Zirkelschluss, Reihenfolge einer Beweiskette). Test sollte das Lernziel prüfen. |
| figuren, beweisen | #168, #171 („Nachbarwinkel an derselben Seite“), Lösungsweg #209 („zwei Nachbarwinkel“) | Widerspricht der eigenen offen-Notiz („Nachbarwinkel wird nicht eingeführt“). Wort ersetzen („die beiden Winkel an derselben Seite“) oder in `woerter` aufnehmen. |
| scheitel_neben | Übung S3 #13, #17 | Der Text verrät den Lösungsweg („ergänzt sie zu einer Geraden“) – Rechnung 180° − a − b, eher Stufe 1/2. |
| innenwinkelsumme | Übung S2 #90–#92, Korrektur #103–#105, Sicherung #107, #110 | Achtmal derselbe Typ „zwei gleich große Winkel von je …“ (180° − 2 · a) – Stufe-1-Niveau, wenig Abwechslung in Korrektur/Sicherung. |
| figuren | Übung S3 #182–#184 | Dreimal dieselbe Aufgabe (∢ACD im Parallelogramm) mit anderen Zahlen. |
| stufen_wechsel | Übung S3 #40 (Weg A → P → B) | Zeichnung deutlich nicht maßstäblich: bei B steht 51°, gezeichnet ≈ 34° (A und B sind gleich gezeichnet). Weitere Abweichungen 6–8°: #30 (150°/145°), #33 (153°/145°), #54 und #202 (27°/35°). Werte stehen im Text, daher kein Fehler, aber irritierend. |
| stufen_wechsel, parallel_pruefen | fehler_bild Etappe 2, Schritt 4 und fehler_bild Etappe 3, Übung S3 #66 (geneigtes h) | Bei geneigtem h bleibt der Winkelbogen bei T am waagrechten Hilfsstrahl, T liegt nicht genau auf h. In Etappe 3 Schritt 4 steht am Bogen „72°“, gezeichnet sind 70° gegen die Waagrechte (gegen h ≈ 64°). Bogen-Schenkel auf h legen. |

### C. Kleinigkeiten (Form)
| Etappe | Bordkarte | Befund |
|---|---|---|
| stufen_wechsel | Übung S3 #42, Lösungsweg | „6 · 16 + 0 = 96°“ – „+ 0“ ist ein Rest aus dem Generator. |
| parallel_pruefen | Test #74, Korrektur #75, #76, Lösungsweg | „Verschieden wie bei S (50°)“ – sprachlich falsch, besser „anders als bei S“. |
| aussenwinkel, figuren | #122, #179, #182–#184 | Schreibweise „∠BAC“ wird nicht erklärt; in Bayern üblich ist „∢BAC“. Einheitlich machen und einmal in `woerter`. |
| vieleck | #140 „1440°“, #152 „1 440°“, #153 „2340°“ | Uneinheitliche Zahlschreibweise (README: Leerzeichen bei großen Zahlen). |
| vieleck / beweisen | Lernkarten | „Winkelsumme“, „regelmäßig“ (vieleck) und „Außenwinkelsatz“ (beweisen, im Merksatz-Schritt hervorgehoben) stehen in keiner `woerter`-Liste. |
| figuren | Lernkarte, Schritt 4 | „Schreibe zu jedem Schritt den passenden Winkelsatz dazu.“ ist eine Anweisung, kein Schritt des Beispiels. Einstieg „Dachstuhl“ passt nur lose zum abstrakten Bild (zwei Parallelen mit Dreieck). |

### Etappen: Erklärung und Bildergeschichte
| Etappe | Befund |
|---|---|
| 1 scheitel_neben | Verständlich, Bild und Schritte stimmen (Winkel geprüft), alle Längenregeln eingehalten. |
| 2 stufen_wechsel | Verständlich; Lage der Winkel in allen Schrittbildern richtig (Stufen-, Scheitel-, Wechselwinkel). Definition „Wechselwinkel = über Kreuz zwischen den Parallelen“ ist enger als in vielen Schulbüchern (siehe A, #51). |
| 3 parallel_pruefen | Verständlich (Schreinerin, Umkehrung). Bild Schritt 4 siehe B. |
| 4 innenwinkelsumme | Einstieg (Ecken abreißen) gut. Bildergeschichte unvollständig (siehe A). Fundamentalsatz passt zum Lehrplan (Wechselwinkel). |
| 5 aussenwinkel | Einstieg (Läufer biegt ab) passt fachlich und zum Bild. Lehrplan siehe B. |
| 6 vieleck | Verständlich, Bild (Fünfeck mit Diagonalen) passt. |
| 7 figuren | Erklärung knapp, Bild und Schritt 3 (Wechselwinkel bei C) stimmen; Schritt 4 siehe C. |
| 8 beweisen | Inhalt passt zum Lehrplan (Fundamentalsatz/abgeleiteter Satz, Zirkelschluss). Bild ändert sich in keinem Schritt – vertretbar, die Karte ist textlich. |
README-Regeln (per Skript): einstieg ≤ 35 Wörter, ≤ 3 neue Wörter, jedes Wort im Einstieg/in den Schritten, 2–4 Schritte ≤ 15 Wörter, Sätze ≤ 20 Wörter, fehler ≤ 30, regel ≤ 25 (erster Satz ≤ 12), höchstens zwei ⟦…⟧ – **alle eingehalten**. `fehler_bild` fehlt bei innenwinkelsumme, vieleck, figuren, beweisen (zulässig, „wenn sich der Fehler zeigen lässt“; bei vieleck wäre „5 statt 3 Dreiecke“ zeigbar).

Weitere Quelle zur Wechselwinkel-Definition (innen und außen): Studyflix „Stufenwinkel und Wechselwinkel“ (https://studyflix.de/mathematik-schueler/stufenwinkel-und-wechselwinkel-4319), Uni Bielefeld (https://www.math.uni-bielefeld.de/fast/geo2/studar/winkel.pdf).

**freigabereif: nein** – wegen Teil A (eine fachlich angreifbare Sicherungsaufgabe, eine mehrdeutige Aufgabe, Stoff späterer Etappen bzw. späterer Lernbereiche, unvollständige Bildergeschichte beim Beweis). Nach Behebung von A ist das Thema aus meiner Sicht freigabefähig; B kann in einer Folgerunde kommen.
