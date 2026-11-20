# Postfach schwer-kl10 (Zehnte Runde, Klasse 10)

## 2026-11-16 08:10 – FERTIG
Zehnte Runde Klasse 10 abgeschlossen: 7 Themen, 45 Lernkarten, **270 neue Übungen** (je Lernkarte 4 × Stufe 3, 2 × Stufe 2; danach jede Lernkarte 10 Stufe-3-Übungen).
Je Thema ein Commit auf `schwer-kl10` (auf den aktuellen Stand von `lernen-app` aea5ee3 umgesetzt). Alle Themen ohne Ausnahme bearbeitet (alle haben einen Generator).

**Prüfung (alle 7 Themen, Endstand):** `python3 -I tools/inhalt_pruefen.py` → OK, keine „nicht nachgerechnet“-Hinweise.
**Unverändert-Nachweis:** `python3 -I inhalte/generatoren/_schwer_kl10.py <thema>` → „NACHWEIS OK“ für alle 7: jede Aufgabe des Stands `origin/lernen-app` steht unverändert an derselben Stelle,
Lernkarten/Abschnitte/übrige Felder identisch, neue Aufgaben nur angehängt und nur im Pool `uebung`.
**Technik:** In jedem Generator ein Abschnitt „Zehnte Runde“ mit eigener Funktion `schwer()` und eigenem festen Zufallsstart (10010–10016, nur zum Mischen der Antworten);
er läuft erst nach `bauen(...)`. Hilfsdatei `inhalte/generatoren/_schwer_kl10.py` (`ergaenzen` prüft Tipp, Weg, Dubletten im ganzen Thema und die Mindestzahl je Lernkarte; `nachweis`).
Alle Lösungen berechnet das Programm; jede neue Aufgabe habe ich gelesen und von Hand nachgerechnet (dabei einen falschen Wert im Lösungsweg einer eigenen Aufgabe gefunden und korrigiert).
Keine wörtlich oder mit gleichen Zahlen übernommene Prüfungsaufgabe: Vorbild sind Typ, Aufbau und Niveau.

**Hinweise für das Einspielen:**
- Die neuen Aufgaben stehen am Ende von `aufgaben` (nach Test/Korrektur/Sicherung). Falls die App die Reihenfolge der Datei nutzt, ändert das nichts an den alten Aufgaben.
- funktionen.trig: Neue Aufgaben sind teils im **Bogenmaß** und eine Zuordnungsaufgabe nutzt eine π-beschriftete Achse (`"pi": true`, `"bogen": true`).
- Lückenaufgaben mit Term-Vorlage nur bis x³ (Vorgabe README); höhere Grade als Zahlenfelder („a = □; b = □“).
- App-Wunsch (nicht dringend): Antworttyp „Lösungsmenge“ wäre für Polynomgleichungen besser – die Zahl der Lücken verrät die Zahl der Lösungen (steht schon unter „offen“).

### (1) Befundliste aus Teil 1 (vorhandene Aufgaben nicht geändert)
### gleichungen.exponential (6 Lernkarten, je ≥ 10 Aufgaben gelesen)
Keine falsche Lösung gefunden; Rundungen und Toleranzen stimmen.
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| verstehen | Übung Stufe 3 „Jemand formt a · b^x = c um zu (ab)^x = c …“ und „Welche Aussage ist falsch? lg(a + b) = …“ | Gleicher Aufgabentyp wie Stufe 2 – Stufe 3 ist hier nicht schwerer (Einstufung zu hoch). |
| verstehen | Übung Stufe 1 und 2 „Welche Lösung hat b^x = −…?“ | Derselbe Typ auf zwei Stufen; als Stufe 2 zu leicht. |
| wachstum | Übung Stufe 1 „Ein Kapital von 5 000 € … Wie groß ist es nach 5 Jahren?“ | Fragt nicht nach dem Zeitpunkt („Wann?“, Kartentitel); passt eher zu funktionen.exponential_log. |
| gleiche_basis | – | Lücke: Ausklammern gleicher Potenzen (3^(x + 1) + 3^x = …), in Schulaufgaben/Grundwissen G9 üblich – jetzt ergänzt. |
| mit_log_loesen | – | Lücke: Ungleichung mit Basis < 1 (Zeichen dreht sich), „kleinste ganze Zahl“ – jetzt ergänzt. |
| verstehen | – | Lücke: Definitionsmenge von lg(x − a) (Abitur Teil A) – jetzt ergänzt. |

### gleichungen.polynom (5 Lernkarten, je ≥ 10 Aufgaben gelesen)
Keine falsche Lösung gefunden.
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| verstehen | Übung Stufe 3 „Jemand löst x³ = 4x, indem er durch x teilt …“ | Gleicher Typ wie Stufe 2 („x³ = 49x“, „x³ = 16x“) – als Stufe 3 zu leicht. |
| vielfachheit | Übung Stufe 3 „f(x) = (x + 2)² · (x − 2)³. Wechselt f bei x = 2 das Vorzeichen?“ | Gleicher Typ wie Stufe 2, nur ohne Zeichnung – grenzwertig Stufe 2. |
| vielfachheit | Auswahl „Wechselt f … das Vorzeichen?“ | Antwort „Nein, die Nullstelle ist 3-fach (ungerade)“ ist in sich widersprüchlich; als Ablenker wenig trennscharf (kein Fehler). |
| alle | Lückenaufgaben „x₁ = □; x₂ = □ …“ | Die Zahl der Lücken verrät die Zahl der Lösungen (steht schon unter „offen“). In Prüfungen ist gerade „wie viele Lösungen?“ der Knackpunkt – neue Aufgaben fragen das teils als Zahl ab. |
| ausklammern / nullprodukt | – | Lücke: Gleichungen, bei denen man nicht durch einen Term teilen darf (x²(x − 1) = 4(x − 1)), und Gleichungen mit Parameter (x³ − kx = 0 mit gegebener Lösung) – jetzt ergänzt. |
| verstehen | – | Lücke: Term aus Nullstellen und „schneiden/berühren“ aufstellen (BMT 10, Abitur Teil A) – jetzt ergänzt. |

### funktionen.exponential_log (6 Lernkarten, je ≥ 10 Aufgaben gelesen)
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| faktor | Übung Stufe 3 „Die Menge eines Medikaments im Blut sinkt jede Stunde um 15 % (bzw. 25 %). Um welchen Faktor ändert sie sich in 2 Stunden?“ | **Fehler im Lösungsweg**: „Faktor pro Jahr 0,85; in 2 Jahren …“ – richtig wäre „pro Stunde … in 2 Stunden“. Lösung (0,7225 bzw. 0,5625) stimmt. Ursache: g_faktor schreibt im Weg immer „Jahr“ (Zeile ~145). Nur den Weg korrigieren (Aufgabentext bleibt), wenn der Haupt-Chat das darf. |
| faktor | Übung Stufe 3 „Um welchen Faktor ändert sich … in 2/3 Jahren?“ und „Wachstum oder Zerfall um wie viel %?“ | Einschritt-Aufgaben; eher Stufe 2. |
| werte | Übung Stufe 3 „f(x) = 1000 · 1,5^x“ | Schreibweise: 1000 ohne Leerzeichen, sonst im Thema „1 000“ (nur Form). Stufe 3 = nur größere Rechnung (1,5⁴), kein anderer Gedanke. |
| graph | Übung Stufe 3 „g(x) = 3^x − 1 … y-Achse?“ | Eher Stufe 2. |
| logfunktion | Übung Stufe 3 „Berechne f(0,25) für f(x) = log₄(x)“ | Eher Stufe 2. |
| werte / graph | – | Lücke: Funktionswert im Sachzusammenhang deuten (BMT 10 2025), Wertemenge, Spiegeln an der x-Achse + Verschieben, senkrechte Asymptote und Nullstelle der Logarithmusfunktion (Realschul-Abschlussprüfung) – jetzt ergänzt. |

### funktionen.trig (7 Lernkarten, je ≥ 10 Aufgaben gelesen)
Keine falsche Lösung gefunden.
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| periode, parameter, zuordnen, eigenschaften, anwendung | alle bisherigen Aufgaben | Funktionen werden fast nur im **Gradmaß** behandelt (Periode 360° : b, Graphen mit Grad-Achse). LehrplanPLUS M10 3 und die Abiturprüfung (Teil A) arbeiten mit dem Bogenmaß (Periode 2π : b, Lösungen in [0; 2π[). Die Begründung unter „offen“ (keine π-Beschriftung) ist seit 15.11. überholt (`"pi": true`). Neue Aufgaben nutzen jetzt auch das Bogenmaß. |
| periode | Übung Stufe 3 „f(x) = sin(b · x) soll die Periode 90° haben. Bestimme b.“ | Einschritt-Aufgabe, eher Stufe 1–2. |
| periode | Übung Stufe 3 „Jemand sagt: f(x) = sin(0,5x) hat die Periode 180° …“ | Gleicher Typ wie Stufe 1 (Periode berechnen) in Auswahlform; Stufe 2. |
| werte | Übung Stufe 1/2 „Berechne cos(2,5) … auf drei Nachkommastellen“ | Reine Taschenrechner-Aufgaben auf Stufe 1 und 2 gleich; kein Unterschied in der Schwierigkeit. |
| eigenschaften | – | Lücke: Lösungen von sin x = c in [0; 2π[ (Grundwissen/Schulaufgabe), Symmetrie zusammengesetzter Terme – jetzt ergänzt. |
| parameter | – | Lücke: Parameter aus zwei Punkten bestimmen (Abitur 2025 Teil A) – jetzt ergänzt. |

### funktionen.ganzrational (7 Lernkarten, je ≥ 10 Aufgaben gelesen)
Keine falsche Lösung gefunden.
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| symmetrie | Übung Stufe 3 „Für f(x) = … gilt f(3) = −374. Bestimme f(−3) mithilfe der Symmetrie.“ | Lösungsweg schreibt „Achsensymmetrisch zur y-achse“ / „Punktsymmetrisch zum ursprung“ (Kleinschreibung) – nur Form. |
| graph_term | Übung Stufe 3 „Welcher Funktionsterm gehört zum Graphen?“ mit 2 · (x − 1)(x − 3) bzw. (x + 1) · x | Grad 2 mit zwei einfachen Nullstellen – leichter als die Stufe-2-Aufgaben (Grad 3/4 mit Berührung). Einstufung zu hoch. |
| randverhalten | Übung Stufe 1 mit Polynom 7. Grades und 8 Gliedern | Viel Text für Stufe 1; inhaltlich richtig. |
| symmetrie | – | Lücke: Symmetrie mit Parameter (x³ + (a − 3)x², x⁴ − kx²) und Folgerungen aus Symmetrie (Hochpunkt → Tiefpunkt) wie in Abitur Teil A / IlluPA A2, A5 – jetzt ergänzt. |
| graph_term | – | Lücke: Verschobener Graph g(x) = f(x + c) (Abitur 2025 Teil A), Entscheidung zwischen Termen mit gleichen Nullstellen über f(0) – jetzt ergänzt. |

### raum.pyramide_kegel_kugel (7 Lernkarten, je ≥ 10 Aufgaben gelesen)
Keine falsche Lösung gefunden.
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| sachkontext | Übung Stufe 3 „Eine quadratische Pyramide (als Modell eines Bauwerks) hat die Grundkante 230 m und die Höhe 146 m …“ | Stufe 3 nur wegen großer Zahlen – derselbe Gedanke wie Stufe 1 (V = 1/3 · G · h). Einstufung zu hoch. |
| verstehen | Übung Stufe 1 „Pyramide mit regelmäßigem 12-/24-/100-Eck …“ | Dreimal dieselbe Aufgabe mit anderer Eckenzahl; die Antwort ist immer gleich (wird nach dem ersten Mal auswendig gewusst). |
| verstehen | Übung Stufe 2/3 „Radius verdoppelt/vervierfacht – Volumen?“ | Stufe 3 („Radius verdreifacht, Volumen“) ist derselbe Typ wie Stufe 2. |
| kegel_volumen | Übung Stufe 1 „… = 64/3π ≈ 67 cm³“ (Lösungsweg) | Schreibweise „64/3π“ ist mehrdeutig (64/(3π)?); besser „64π/3“. |
| kugel | Übung Stufe 3 „Radius auf zwei Nachkommastellen“ | Lösung 10,1 wird ohne zweite Nachkommastelle angezeigt (10,10) – nur Form. |
| alle | – | Lücke laut Lehrplan („Strategien vergleichen, einfache Kopfüberlegungen“, „Schrägbilder und Netze“): Überschlag mit π ≈ 3, Körper im Würfel, Lage eines Punkts für ein vorgegebenes Volumen, Volumenverhältnis bei gleicher Höhe (Realschul-Abschlussprüfung, Abitur 2025 Teil A Geometrie) – jetzt ergänzt. Schrägbilder/Netze weiter offen (Zeichnung fehlt in der App). |

### stochastik.mehrstufig (7 Lernkarten, je ≥ 10 Aufgaben gelesen)
Keine falsche Lösung gefunden.
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| baum_ergaenzen | Übung Stufe 2 „P(A) = 0,4 / 0,5 / 0,2 und Pfad … = 0,36 / 0,45 / 0,18“ | Alle drei Stufe-2-Übungen haben dieselbe Lösung 0,9 – Kind kann raten. |
| gegenereignis | Übung Stufe 1 „Würfel 2-mal: mindestens eine Sechs“ und „… mindestens eine Eins“ | Inhaltlich dieselbe Aufgabe mit derselben Lösung 11/36. |
| pfad_add | Übung Stufe 3 „Glücksrad mit 0,7/0,6/0,2 … genau zweimal Gewinn“ | Dreimal dasselbe Schema – eher Stufe 2 nach dem ersten Mal. |
| verstehen | Übung Stufe 3 „Bei 4 Würfen … 4 · 1/6“ | Gleicher Typ wie Stufe 2 (5 bzw. 2 Würfe). Antwort „Falsch: richtig ist 1 − 1/6 · 2“ ist als Ablenker unklar formuliert. |
| simulation | Übung Stufe 2 „Simulation 500-mal … relative Häufigkeit“ | Reines Ablesen und Teilen; die eigentliche Simulation (Zufallszahlen zuordnen) fehlte – jetzt ergänzt. |
| alle | – | Lücke laut LehrplanPLUS M10 2 und Prüfungen: Ziehen bis zum ersten Erfolg (Abbruch), „bei welchem Zug sicher?“ (Realschul-Abschlussprüfung 2024), Term ↔ Ereignis (Abitur 2023/2025 Teil A), Produkt/Summe mehrerer Würfel, Urneninhalt aus dem Baum (ZP10 NRW), π mit Zufallspunkten (Lehrplan) – jetzt ergänzt. |


### (2) Genutzte Prüfungsquellen und abgeleitete Aufgabentypen
Prüfungen (frei zugänglich):
- [BMT10 2025 A] Bayerischer Mathematik-Test Jgst. 10 Gymnasium 2025, Gruppe A – https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/BMT10_2025_Aufgaben_Gruppe_A.pdf
- [BMT10 2024 A] dto. 2024 – https://isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/BMT10_2024_Aufgaben_Gruppe_A.pdf
- [BMT10 2010 B] dto. 2010, Gruppe B – https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2010/bmt10-2010-aufgaben-gruppe-b.pdf
- [Abi 2025 A] Abiturprüfung Bayern 2025, Prüfungsteil A (ohne Hilfsmittel) – https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Abiturpruefung/Mathematik/2025/abiturpruefung_mathematik_2025_pruefungsteil_a.pdf
- [Abi 2023 A] Abiturprüfung Bayern 2023, Prüfungsteil A – https://mathegym.de/docs-v1/docs/d_abi2023_A.pdf
- [IlluPA A] Illustrierende Prüfungsaufgaben Abitur ab 2026, Teil A – https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/IlluPA/M/IlluPA_Mathematik_Beispielaufgaben_A.pdf
- [RS 2022] Abschlussprüfung Realschule Bayern Mathematik I 2022 HT – https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2022/2022_mi_ht.pdf
- [RS 2021] dto. 2021 NT – https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2021/2021_mi_nt.pdf
- [RS 2024] dto. 2024 HT – https://isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2024/2024_mi_ht.pdf
- [RS 2008] dto. 2008 (A 1 Logarithmusfunktion) – https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2002-2010/2008_MI_HT-P-W_NT.pdf
- [RS Bsp A4] Beispielaufgabe weiterentwickelte Abschlussprüfung, Raumgeometrie ohne Taschenrechner – https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Mathematik/Weiterentwicklung_Abschlusspruefung/Beispielaufgaben_Abschlusspruefung_I/aufgabenbeispiel_apmi_a4.pdf
- [ZP10 NRW] Aufgabenbeispiele ZP10 Mathematik ohne Hilfsmittel ab 2023 – https://standardsicherung.schulministerium.nrw.de/cms/zentrale-pruefungen-10/faecher/getfile.php?file=2715
- [SA Kl10] Schulaufgabe Mathematik 10. Klasse Gymnasium Bayern (Bogenmaß, Kugeln) – https://www.klassenarbeiten.de/data/dynamic/pdf/4299.pdf

Ergänzend (keine Prüfungen, nur Abgleich mit dem Schulstoff): Grundwissen M10 G9 Hildegardis-Gymnasium Kempten – https://hildegardis-gymnasium.de/wp-content/uploads/2026/07/10.-Klasse-Grundwissen-Mathe.pdf ;
Grundwissen 10 Leibniz-Gymnasium Altdorf (nur Suchauszug gelesen) – https://leibniz-gymnasium-altdorf.de/wp-content/uploads/2023/07/10_Grundwissen_G9.pdf ;
Lernkarten M10 Werdenfels-Gymnasium – https://www.werdenfels-gymnasium.de/images/Unterricht/Mathematik/M10%20-%20Ruckseiten%20-%20G9.pdf ; LehrplanPLUS M10 – https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/10/mathematik

| Thema | Quellen | daraus abgeleitete Aufgabentypen, Niveau, Fallen |
|---|---|---|
| gleichungen.exponential | RS 2021, RS 2022, Abi 2023 A, Grundwissen | Rate aus zwei Werten; „erstmals über …“ mit Aufrunden auf ganze Jahre; zwei Vorgänge gleichsetzen; Definitionsmenge lg(x − a); Ausklammern 3^(x+1) + 3^x; Falle: Zeichenwechsel bei Basis < 1, Klammer bei (x − 1) · lg 3. |
| gleichungen.polynom | BMT10 2025 A (1a/1b), Abi 2023 A (Grad), IlluPA A2 (x⁴ − kx²), Grundwissen | Ausklammern ohne Teilen, Gleichung mit Parameter und gegebener Lösung, „Term angeben, sodass …“, Term aus „schneiden/berühren“; Falle: Lösung beim Teilen verloren, negative z bei Substitution. |
| funktionen.exponential_log | BMT10 2025 A (5b deuten), RS 2021 A 1, RS 2022 A 1 + B 1, RS 2024 A 3.3, RS 2008 A 1 | Funktionswert im Sachzusammenhang deuten (auch negatives t), Prozent pro Zeiteinheit aus Halbwertszeit, Spiegeln an der x-Achse + Verschieben, Wertemenge, senkrechte Asymptote/Nullstelle/Definitionsmenge der Log-Funktion, Umkehrfunktion. |
| funktionen.trig | Abi 2025 A (Analysis 1.5: a, b aus zwei Punkten), BMT10 2025 A (4b sin(α + 90°)), SA Kl10, Grundwissen | Parameter aus Punkten, Einheitskreis-Symmetrien, Lösungen von sin x = c in [0; 2π[, Bogenlänge/Sektor, Beschreibung der Transformation; Falle: Taschenrechner im falschen Modus. |
| funktionen.ganzrational | Abi 2023 A (Grad begründen), Abi 2025 A (g(2x − 1)), IlluPA A2, A5, Grundwissen | Mindestgrad aus Eigenschaften, Symmetrie mit Parameter, Folgerung Hochpunkt → Tiefpunkt, verschobener Graph, Vorzeichenbereiche, Term über f(0) unterscheiden. |
| raum.pyramide_kegel_kugel | RS 2021 A 3.3 + B 2.6, RS 2024 B 4.5, RS Bsp A4, Abi 2025 A Geometrie, ZP10 NRW, BMT10 2010 B (Kopfüberlegung π ≈ 3), SA Kl10 | Punkt auf Kante für vorgegebenes Volumen, Volumenverhältnis bei gleicher Höhe, Pyramide mit Spitze über einer Ecke, Würfelecke abschneiden, Anteil in Prozent, Überschlag; Falle: Höhe statt Seitenhöhe. |
| stochastik.mehrstufig | Abi 2023 A, Abi 2025 A, IlluPA A7, RS 2024 A 2, BMT10 2010 B (6a/6b), BMT10 2025 A (2b/2c), ZP10 NRW, LehrplanPLUS (π-Simulation) | Term ↔ Ereignis, Produkt/Summe mehrerer Würfel, Ziehen bis zum ersten Erfolg, „spätestens sicher“, Urneninhalt aus Baum, Gegenereignis als Term, relative Häufigkeit; Falle: Gegenereignis „nur Sechsen“ statt „keine Sechs“. |

Knobelaufgaben (je Lernkarte mindestens eine): eigene Aufgaben nach den Merkmalen des Auftrags (Rückwärtsdenken, Parameter statt Zahl, Fehler finden, Verknüpfung mit früherem Stoff,
ungewohnte Einkleidung), z. B. log₂(log₃ x) = 2, Ziffernzahl von 2¹⁰⁰, Algenteppich, sin x = 0,1x (7 Schnittpunkte), Summe der Koeffizienten = f(1), Pyramiden im Würfel, de-Méré-Vergleich.

### (3) Neue Aufgaben je Lernkarte und Stufe
| Thema | Lernkarte | neu Stufe 2 | neu Stufe 3 | Stufe-3-Übungen vorher → jetzt |
|---|---|---|---|---|
| gleichungen.exponential | logarithmus | 2 | 4 | 6 → 10 |
| gleichungen.exponential | gleiche_basis | 2 | 4 | 6 → 10 |
| gleichungen.exponential | mit_log_loesen | 2 | 4 | 6 → 10 |
| gleichungen.exponential | potenzregel | 2 | 4 | 6 → 10 |
| gleichungen.exponential | wachstum | 2 | 4 | 6 → 10 |
| gleichungen.exponential | verstehen | 2 | 4 | 6 → 10 |
| gleichungen.polynom | ausklammern | 2 | 4 | 6 → 10 |
| gleichungen.polynom | nullprodukt | 2 | 4 | 6 → 10 |
| gleichungen.polynom | substitution | 2 | 4 | 6 → 10 |
| gleichungen.polynom | vielfachheit | 2 | 4 | 6 → 10 |
| gleichungen.polynom | verstehen | 2 | 4 | 6 → 10 |
| funktionen.exponential_log | werte | 2 | 4 | 6 → 10 |
| funktionen.exponential_log | faktor | 2 | 4 | 6 → 10 |
| funktionen.exponential_log | modell | 2 | 4 | 6 → 10 |
| funktionen.exponential_log | graph | 2 | 4 | 6 → 10 |
| funktionen.exponential_log | logfunktion | 2 | 4 | 6 → 10 |
| funktionen.exponential_log | zeitpunkt | 2 | 4 | 6 → 10 |
| funktionen.trig | bogenmass | 2 | 4 | 6 → 10 |
| funktionen.trig | werte | 2 | 4 | 6 → 10 |
| funktionen.trig | periode | 2 | 4 | 6 → 10 |
| funktionen.trig | parameter | 2 | 4 | 6 → 10 |
| funktionen.trig | zuordnen | 2 | 4 | 6 → 10 |
| funktionen.trig | eigenschaften | 2 | 4 | 6 → 10 |
| funktionen.trig | anwendung | 2 | 4 | 6 → 10 |
| funktionen.ganzrational | grad | 2 | 4 | 6 → 10 |
| funktionen.ganzrational | ausmultiplizieren | 2 | 4 | 6 → 10 |
| funktionen.ganzrational | randverhalten | 2 | 4 | 6 → 10 |
| funktionen.ganzrational | symmetrie | 2 | 4 | 6 → 10 |
| funktionen.ganzrational | nullstellen | 2 | 4 | 6 → 10 |
| funktionen.ganzrational | graph_term | 2 | 4 | 6 → 10 |
| funktionen.ganzrational | term_bestimmen | 2 | 4 | 6 → 10 |
| raum.pyramide_kegel_kugel | pyr_volumen | 2 | 4 | 6 → 10 |
| raum.pyramide_kegel_kugel | pyr_oberflaeche | 2 | 4 | 6 → 10 |
| raum.pyramide_kegel_kugel | kegel_volumen | 2 | 4 | 6 → 10 |
| raum.pyramide_kegel_kugel | kegel_mantel | 2 | 4 | 6 → 10 |
| raum.pyramide_kegel_kugel | kugel | 2 | 4 | 6 → 10 |
| raum.pyramide_kegel_kugel | sachkontext | 2 | 4 | 6 → 10 |
| raum.pyramide_kegel_kugel | verstehen | 2 | 4 | 6 → 10 |
| stochastik.mehrstufig | pfad_mult | 2 | 4 | 6 → 10 |
| stochastik.mehrstufig | pfad_add | 2 | 4 | 6 → 10 |
| stochastik.mehrstufig | ohne_zuruecklegen | 2 | 4 | 6 → 10 |
| stochastik.mehrstufig | gegenereignis | 2 | 4 | 6 → 10 |
| stochastik.mehrstufig | baum_ergaenzen | 2 | 4 | 6 → 10 |
| stochastik.mehrstufig | simulation | 2 | 4 | 6 → 10 |
| stochastik.mehrstufig | verstehen | 2 | 4 | 6 → 10 |

Zusammen 270 neue Übungen (45 Lernkarten × 6).

### (4) Themen ohne belastbare Prüfungsaufgaben
- Keine echte Lücke bei einem ganzen Thema, aber ehrlich eingeschränkt:
  - **gleichungen.polynom:** Biquadratische Gleichungen/Substitution habe ich in keiner frei zugänglichen bayerischen Prüfung gefunden (nur im Schul-Grundwissen und im Lehrplan). Diese Aufgabentypen orientieren sich am Lehrplan, nicht an einer Prüfung.
  - **funktionen.trig:** Sinus/Kosinus mit Parametern kommt nur im Abitur (Teil A 2025, mit Integral/Analysis-Anteilen) und im BMT10 2025 (Einheitskreis) vor; reine Klasse-10-Prüfungsaufgaben zu Periode/Amplitude habe ich nicht gefunden.
  - **raum.pyramide_kegel_kugel:** Kegel und vor allem **Kugel** kommen in den gefundenen bayerischen Prüfungen kaum vor (Realschule: fast nur Pyramiden/Prismen). Kegel-Vorbild aus ZP10 NRW; Kugel nur aus einer Schulaufgabe.
  - **Wettbewerbe:** Känguru 2021 (Klasse 9/10, https://www.rudolf-hildebrand-schule.de/assets/downloads/kaenguru2021_910.pdf) durchgesehen – zu diesen sieben Themen nichts Passendes (nur Algebra-Identität, ebene Geometrie). Die Knobelaufgaben sind daher eigene Aufgaben, nicht nach Wettbewerbsvorbild. Mathematik-Olympiade und Pangea habe ich nicht ausgewertet.
- Abitur-Prüfungsteil A ist Oberstufen-Niveau (Ableitung, Integral); übernommen wurden nur Teile, die mit Stoff der Klasse 10 lösbar sind.

## 2026-11-16 07:55 – STATUS
stochastik.mehrstufig fertig: 42 neue Übungen (7 Lernkarten), Prüfskript OK, Nachweis OK. Alle 7 Themen erledigt, Abschlussbericht folgt.

## 2026-11-16 07:30 – STATUS
raum.pyramide_kegel_kugel fertig: 42 neue Übungen (7 Lernkarten), Prüfskript OK, Nachweis OK.

## 2026-11-16 07:05 – STATUS
funktionen.ganzrational fertig: 42 neue Übungen (7 Lernkarten), Prüfskript OK, Nachweis OK.

## 2026-11-16 06:40 – STATUS
funktionen.trig fertig: 42 neue Übungen (7 Lernkarten), Prüfskript OK, Nachweis OK. Neue Aufgaben auch im Bogenmaß, eine mit π-beschrifteter Achse.

## 2026-11-16 06:10 – STATUS
funktionen.exponential_log fertig: 36 neue Übungen, Prüfskript OK, Nachweis OK. Befund mit Fehler im Lösungsweg (faktor, „pro Jahr“ statt „pro Stunde“) steht im Abschlussbericht.

## 2026-11-16 05:45 – STATUS
gleichungen.polynom fertig: 30 neue Übungen (je Lernkarte 4 × Stufe 3, 2 × Stufe 2), Prüfskript OK, Nachweis OK.

## 2026-11-16 05:20 – STATUS
gleichungen.exponential fertig: 36 neue Übungen (je Lernkarte 4 × Stufe 3, 2 × Stufe 2), Prüfskript OK, Nachweis „alte Aufgaben unverändert“ OK
(`python3 -I inhalte/generatoren/_schwer_kl10.py gleichungen.exponential`). Neue Hilfsdatei: inhalte/generatoren/_schwer_kl10.py (ergaenzen + nachweis).
