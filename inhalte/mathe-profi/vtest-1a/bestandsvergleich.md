# Runde VT1A: Bestandsvergleich und Tabelle je Lernziel

Erzeugt von `bauen.py` aus den Feldern `bauplan`, `schema`, `idee`, `alt`, `bestand`, `unterschied` in `th_*.py`. Bestand gelesen je Lernziel: `inhalte/themen/<einheit>.json` (alle Pools) und alle `inhalte/mathe-profi/rollend-*` (Aufgaben dieser Einheiten stehen nur in rollend-5, -11, -12; rollend-15 enthält keine). Zusätzlich gelesen, weil Inhalte überlappen: die R-Lernziele `vertauschen` und `berechnen` (Potenzen). Schema = durch Anwenden eines bekannten Verfahrens oder bloßes Ausrechnen lösbar, im Zweifel ja.

Baupläne: a Begründung wählen/geben; b Fehlvorstellung aufdecken; c Rückwärts mit Wahl; d Darstellungswechsel; e Was-wäre-wenn/Invarianz; f Gegenbeispiel/immer–manchmal–nie; g Vergleichen ohne Ausrechnen; h Modellwahl.

## zahlen.potenzen_basis / schreibweise

| Kennung | Pool | Bauplan | Denkfigur | Schema | früher | nächstliegender Bestandskern | Unterschied |
|---|---|---|---|---|---|---|---|
| VT1A-001 | test | d | faktoren_umgruppieren | nein | neu | themen schreibweise „Schreibe 6 · 6 · 6 · 2 · 2 · 2 als eine einzige Potenz“; rollend-5 berechnen „4³ als 2⁶ (Weg B)“ | Dort wird eine Darstellung gebildet oder ausgerechnet; hier werden vier Darstellungen über die Zahl der Faktoren verglichen, Ausrechnen (über eine Million) ist keine Hilfe. |
| VT1A-002 | korrektur | f | potenz_gerade_ungerade | nein | neu | themen quadrat (Bonus) „Wie viele der Quadratzahlen 1², 2², …, 20² sind gerade?“ (andere Etappe); themen schreibweise „Was bedeutet 3²?“ | Dort wird gezählt oder eine Bedeutung gelesen; hier wird eine allgemeine Aussage über alle Potenzen mit ungerader Basis begründet (Produkt ungerader Faktoren). Warum kein Schema: Basis und Hochzahl sind beliebig, Beispiele widerlegen nur die Ablenker; die richtige Aussage braucht die Begründung über die Faktoren. Ersetzt 002 (B2). |
| VT1A-003 | korrektur | e | wirkung_hochzahl | nein | neu | themen schreibweise „Die Zahlenfolge 3, 9, 27, 81, … Welche Zahl steht an der 6. Stelle?“ | Dort wird eine Folge fortgesetzt (ausrechnen); hier wird die Wirkung von Änderungen an Basis und Hochzahl verglichen, ohne die Potenz (über 500 000) auszurechnen. |
| VT1A-004 | sicherung | f | potenz_gegen_produkt | nein | neu | themen berechnen „Jemand rechnet 7² = 14. Was ist falsch?“ (und 9² = 18, 5³ = 15) | Dort wird ein einzelner Fehler (Basis mal Hochzahl) benannt; hier wird eine allgemeine Aussage über Potenz und Produkt geprüft und die einzige Ausnahme gefunden. |
| VT1A-005 | sicherung | d | situation_potenz | ja | neu | themen sach „Ein Karton enthält 10 Packungen. In jeder Packung sind 10 Beutel mit je 10 Bonbons. Wie viele Bonbons?“ | Dort wird eine Geschichte ausgerechnet; hier wird zu einer Potenz die passende Geschichte unter Geschichten mit vertauschten Rollen von Basis und Hochzahl gewählt. Im Kern das Format „Term ↔ Text“, darum als Schema gezählt. |

Schema: 1 von 5 · Denkfiguren: 5 verschieden · Test: VT1A-001

## zahlen.potenzen_basis / quadrat

| Kennung | Pool | Bauplan | Denkfigur | Schema | früher | nächstliegender Bestandskern | Unterschied |
|---|---|---|---|---|---|---|---|
| VT1A-006 | test | c | zuwachs_rueckwaerts | nein | neu | themen quadrat „Ein Quadrat ist aus Fliesen gelegt, 15 Fliesen je Seite. Wie viele Fliesen liegen am Rand?“; rollend-12 „Plättchen im Inneren (9 · 9)“ | Dort wird der Rand eines bekannten Quadrats gezählt (vorwärts); hier ist nur der Zuwachs bekannt, und das alte Quadrat muss über ein selbst gebildetes Modell (4 · n + 4) erschlossen werden. |
| VT1A-007 | korrektur | e | flaeche_skalieren | nein | neu | themen quadrat „Ein quadratisches Muster hat 15 Felder je Seite. Wie viele Felder hat es insgesamt?“; rollend-5 „Ein Quadrat hat die Fläche 196 cm². Wie lang ist eine Seite?“ | Dort wird aus der Seite die Fläche (oder umgekehrt) ausgerechnet; hier ist die Seite keine natürliche Zahl, die Wirkung der Verdreifachung muss am Bild der neun Teilquadrate erkannt werden. |
| VT1A-008 | korrektur | d | quadrat_einer_summe_zerlegen | nein | neu | themen quadrat „Berechne 20² − 2²“; themen berechnen „Berechne (2 + 3)² − (2² + 3²)“ | Dort wird der Unterschied ausgerechnet; hier wird am Flächenbild gedeutet, welche Teile beim Quadrat einer Summe fehlen, ohne zu rechnen. |
| VT1A-009 | sicherung | g | endziffer_quadratzahl | ja | VT1A-009 | themen quadrat „Stimmt die Aussage? Jede Quadratzahl endet auf 0, 1, 4, 5, 6 oder 9.“ | Dieselbe Einsicht, aber eine andere Leistung: Dort wird die Regel bestätigt, hier wird sie auf vierstellige Zahlen angewendet, deren Wurzeln man nicht kennt. Weil eine bekannte Regel angewendet wird, zähle ich die Aufgabe als Schema. |
| VT1A-010 | sicherung | f | muster_nachbarquadrate | nein | neu | themen quadrat „Berechne 15² − 14²“; „Zwei Quadratzahlen, die direkt aufeinander folgen, unterscheiden sich um 31“ | Dort wird ein Unterschied ausgerechnet oder rückwärts gesucht; hier wird eine allgemeine Aussage über alle Nachbarquadrate geprüft (immer – manchmal – nie). |

Schema: 1 von 5 · Denkfiguren: 5 verschieden · Test: VT1A-006

## zahlen.potenzen_basis / zehner

| Kennung | Pool | Bauplan | Denkfigur | Schema | früher | nächstliegender Bestandskern | Unterschied |
|---|---|---|---|---|---|---|---|
| VT1A-011 | test | g | faktor_hochzahl_verrechnen | nein | neu | themen zehner „Für welchen Exponenten n gilt 25 · 10ⁿ = 2 500 000?“; „4 300 000 = 43 · 10 hoch … Welcher Exponent passt?“ | Dort ist eine ausgeschriebene Zahl gegeben und der Exponent gesucht; hier werden zwei Zehnerpotenz-Schreibweisen ohne Ausschreiben (12 Stellen) verglichen und eine Grenze (größer, nicht gleich) bestimmt. |
| VT1A-012 | korrektur | c | stellenzahl_zu_zehnerpotenz | nein | neu | themen zehner „Wie viele Nullen hat die Zahl 10⁸?“; „Ein Lichtjahr ist etwa 9 · 10¹² km. Wie viele Nullen …?“ | Dort wird eine Schreibweise gelesen; hier wird von der Stellenzahl auf die Lage zwischen Zehnerpotenzen geschlossen, einschließlich der Grenzen. Warum kein Schema: Die Zahl ist beliebig; ein Beispiel entscheidet nicht, ob 10⁷ und 10⁸ selbst dazugehören, dafür braucht man „10ⁿ hat n + 1 Stellen“. Ersetzt 012 (A1). |
| VT1A-013 | korrektur | e | hochzahl_in_summe | nein | neu | themen zehner „Schreibe 3 · 10⁵ + 4 · 10³ als Zahl“; „Schreibe als Zahl: 2 · 10⁶ + 7 · 10⁴ + 5 · 10“ | Dort wird eine solche Summe ausgeschrieben; hier wird die Wirkung einer Änderung aller Hochzahlen auf die ganze Zahl beurteilt. |
| VT1A-014 | sicherung | g | stellenwert_buendeln | ja | neu | themen zehner „Schreibe 6 · 10⁵ + 3 · 10² + 8 als Zahl und runde sie auf Tausender“ | Ähnliche Rechnung (Summe von Stufenzahlen ausschreiben), aber andere Frage: Vergleich mit der nächsten Zehnerpotenz und Fehlvorstellung „lauter Neuner = nächste Stufe“. Weil Ausrechnen genügt, zähle ich die Aufgabe als Schema. |
| VT1A-015 | sicherung | f | aussage_nullen_pruefen | nein | neu | themen zehner „Wie viele Nullen hat die Zahl 50 · 10⁴, wenn man sie ausschreibt?“ | Dieselbe Einsicht (die Nullen der Zahl vorn zählen mit), aber eine andere Leistung: Dort wird gezählt, hier wird eine allgemeine Aussage geprüft und mit einem Gegenbeispiel entschieden (immer – manchmal – nie). |

Schema: 1 von 5 · Denkfiguren: 5 verschieden · Test: VT1A-011

## zahlen.potenzen_basis / sach

| Kennung | Pool | Bauplan | Denkfigur | Schema | früher | nächstliegender Bestandskern | Unterschied |
|---|---|---|---|---|---|---|---|
| VT1A-016 | test | b | falsche_basis_folgen | nein | neu | themen berechnen „Jemand rechnet 2 · 5² = 10² = 100. Was ist falsch?“; rollend-5 sach „Bakterien verdoppeln sich, 5 am Anfang, nach 4 Stunden?“ | Dort wird der Fehler benannt oder vorwärts gerechnet; hier wird die Folge der falschen Basis (Startzahl unter der Hochzahl) über die Zahl der Faktoren bestimmt. Nach B4 wird nach den überzähligen Faktoren gefragt, nicht mehr nach dem Verhältnis (46 656 : 1 458). |
| VT1A-017 | korrektur | c | rueckwaerts_mit_wahl | nein | neu | rollend-12 sach „Eine Bakterienkultur verdoppelt ihre Zahl jede Stunde. Nach 8 Stunden sind es 1 280. Wie viele waren es am Anfang?“; themen sach „dreimal verdoppelt, Ergebnis 200, Anfang?“ | Dort ist die Zahl der Verdopplungen bekannt und es gibt genau eine Anfangszahl; hier ist sie unbekannt, und alle möglichen Anfangszahlen müssen über die Teilbarkeit durch 2 bestimmt werden. |
| VT1A-018 | korrektur | d | term_zu_geschichte | ja | VT1A-025 | themen sach „Eine Zahl wird, beginnend bei 1, fünfmal verdoppelt. Welche Potenz beschreibt das Ergebnis?“ | Umgekehrte Richtung (Vorschlag B5): Zur Rechnung wird die Geschichte gewählt; die Ablenker vertauschen Startzahl und Faktor, deuten Verdoppeln als Dazulegen oder vertauschen Startzahl und Hochzahl (nicht mehr „6⁵“, das ist die Fehlvorstellung des Tests, B7). Im Kern das Format „Term ↔ Text“, darum als Schema gezählt. |
| VT1A-019 | sicherung | e | verhaeltnis_bleibt | nein | VT1A-026 | themen sach „In einer Schale sind 5 Bakterien. Alle 20 Minuten verdoppelt sich die Anzahl. Wie viele sind es nach 3 Stunden?“ | Dort wird ein Endwert ausgerechnet; hier ist Ausrechnen (3²⁰) nicht machbar, entscheidend ist, dass gleiches Wachstum das Verhältnis nicht ändert. Gegenüber der früheren Fassung (4 Tage, ausrechenbar) auf 20 Tage gesetzt. |
| VT1A-020 | sicherung | f | linear_gegen_verdoppeln | nein | VT1A-022 | themen sach „Eine Seerose bedeckt 1 m². Jede Woche verdoppelt sich die Fläche. Wie viele m² nach 6 Wochen?“ | Dort wird ein einzelnes Wachstum vorwärts gerechnet; hier werden zwei Wachstumsarten (gleichmäßiges Dazukommen, Verdoppeln) langfristig verglichen und begründet, warum B nach dem Überholen vorn bleibt. Frühere Fassung (VT1A-022, Zahlantwort 11) war durch eine Tabelle lösbar, darum umgebaut; „Kultur“ nach C3 durch „Schale“ ersetzt. |

Schema: 1 von 5 · Denkfiguren: 5 verschieden · Test: VT1A-016

## zahlen.rechengesetze / klammern

| Kennung | Pool | Bauplan | Denkfigur | Schema | früher | nächstliegender Bestandskern | Unterschied |
|---|---|---|---|---|---|---|---|
| VT1A-021 | test | e | klammer_wirkung | nein | neu | themen klammern „Jemand rechnet 30 − (10 − 4) = 30 − 10 − 4 = 16. Was ist falsch?“; rollend-12 „(48 − 12) : 6 auf zwei Wegen“ | Dort wird ein Term ausgerechnet oder ein Fehler benannt; hier wird die Wirkung einer Klammer über die Struktur bestimmt (eine Zahl wechselt von Plus zu Minus). Nach B6 ist die Anfangszahl unbekannt, schriftliches Ausrechnen führt nicht zum Ziel. |
| VT1A-022 | korrektur | b | fehlregel_erschliessen | nein | neu | themen klammern „Jemand rechnet 30 − (10 − 4) = 30 − 10 − 4 = 16. Was ist falsch?“; rollend-12 „Jan berechnet (30 − 6) · 3 − 4 · 2 … erster Fehler in Zeile …“ | Dort wird ein Fehler benannt; hier wird die falsche Regel aus drei Ergebnissen erschlossen, gefragt ist der Unterschied zum richtigen Ergebnis (kein falscher Wert als Lösung, B1). |
| VT1A-023 | korrektur | h | modellwahl_klammer | ja | neu | themen sach „Ein Fest: 39 Gäste zahlen je 4 € Eintritt. Davon gehen 43 € für Getränke ab. Welcher Term …?“; themen termaufbau „24 Kinder zahlen je 7 € … Welcher Term …?“ | Gleiches Format (Text → Term), aber die Klammer ist hier nötig, weil der Rabatt je Stück gilt; die Ablenker sind Modellfehler mit eigenem Wert. Format des Bestands, darum als Schema gezählt. |
| VT1A-024 | sicherung | f | verbinden_in_ketten | nein | neu | themen vorteil „Welche Gleichung ist falsch? (69 + 8) + 5 = 69 + (8 + 5) / 69 · 8 = 8 · 69 / 69 − 8 = 8 − 69 …“; themen klammern „30 − (10 − 4) = 30 − 10 − 4. Was ist falsch?“ | Dort wird eine einzelne Gleichung beurteilt; hier werden allgemeine Aussagen über alle Ketten einer Rechenart geprüft (immer – nie) und mit Gegenbeispielen widerlegt. |
| VT1A-025 | sicherung | e | aenderung_in_klammer | nein | neu | themen klammern „Für welche Zahl a ergeben (12 + a) · 2 und 12 + a · 2 zusammen 60?“ | Dort wird eine Zahl gesucht; hier wird die Wirkung einer Änderung in der Klammer bestimmt, die für jede Zahl □ gleich ist (□ unbekannt, Ausrechnen nicht möglich). Ersetzt den Termvergleich 97 · (348 + 6) (A1). |

Schema: 1 von 5 · Denkfiguren: 5 verschieden · Test: VT1A-021

## zahlen.rechengesetze / termaufbau

| Kennung | Pool | Bauplan | Denkfigur | Schema | früher | nächstliegender Bestandskern | Unterschied |
|---|---|---|---|---|---|---|---|
| VT1A-026 | test | e | aenderungswirkung_im_term | nein | VT1A-042 | themen termaufbau „24 Kinder zahlen je 7 € … Der Rest wird gleich auf 4 Gruppen verteilt. Welcher Term …?“; rollend-12 „Term A 6 + 4 · 5, Term B (6 + 4) · 5 … Um wie viel ist B größer?“ | Dort wird ein Term aufgestellt oder ausgerechnet; hier wird die Wirkung einer Änderung über den Aufbau (Differenz im Dividenden) bestimmt. Gegenüber der früheren Fassung große Zahlen, damit Ausrechnen nicht lohnt. |
| VT1A-027 | korrektur | d | mehrere_terme_zur_geschichte | ja | VT1A-036 | themen termaufbau „Welcher Term passt? Subtrahiere das Produkt aus 4 und 6 von 30.“; themen klammern „30 − (10 − 4) = 30 − 10 − 4. Was ist falsch?“ | Dort passt genau ein Term; hier passen zwei gleichwertige Terme, und die Ablenker sind Klammer- und Zeichenfehler. Weil man die vier Werte ausrechnen und mit der Geschichte vergleichen kann, zähle ich die Aufgabe im Zweifel als Schema. |
| VT1A-028 | korrektur | c | termart_herstellen | nein | neu | themen termaufbau „Welche Art von Term ist (2 + 6) · 5?“; „Welcher Term ist ein Produkt, dessen erster Faktor eine Summe ist?“ | Dort wird die Art eines gegebenen Terms erkannt; hier wird rückwärts vom Ziel (Produkt) zur nötigen Änderung gedacht, die Ablenker sind Verwechslungen von Malzeichen, Punktrechnung und letztem Schritt. |
| VT1A-029 | sicherung | b | fehlregel_benennen | nein | neu | themen termaufbau „Jemand sagt: 7 + 3 · 5 ist ein Produkt, weil ein Malzeichen vorkommt. Was ist falsch?“; rollend-5 „Kim benennt den Term 3 · (5 + 2) … erster Fehler in Zeile …“ | Dort wird eine einzelne falsche Benennung beurteilt; hier muss aus drei Benennungen die verborgene Regel bestimmt werden, indem vier mögliche Regeln an allen Beispielen geprüft werden. |
| VT1A-030 | sicherung | f | termart_aussagen_pruefen | nein | neu | themen termaufbau „Stimmt die Aussage? Jeder Term mit einer Klammer ist ein Produkt.“; „Jemand sagt: 7 + 3 · 5 ist ein Produkt, weil ein Malzeichen vorkommt.“ | Dort wird eine einzelne Aussage an einem genannten Term bestätigt oder widerlegt; hier gelten die Aussagen für alle Terme, und man muss selbst Gegenbeispiele finden. Warum kein Schema: Es ist kein konkreter Term zu benennen; die richtige Aussage braucht die Begründung über den letzten Rechenschritt, die falschen werden nur durch selbst gesuchte Gegenbeispiele widerlegt. Ersetzt 030 (A2). |

Schema: 1 von 5 · Denkfiguren: 5 verschieden · Test: VT1A-026

## zahlen.rechengesetze / vorteil

| Kennung | Pool | Bauplan | Denkfigur | Schema | früher | nächstliegender Bestandskern | Unterschied |
|---|---|---|---|---|---|---|---|
| VT1A-031 | test | c | zerlegungen_nach_vertauschen | nein | neu | themen vorteil „Ergänze: 25 · □ · 4 = 3 700“; rollend-12 „4 · □ · 25 = 1 700“ | Dort ist eine Lücke bei zwei bekannten Faktoren zu füllen; hier gibt es zwei Lücken, erst das Vertauschen zeigt □ · △ = 200, und die Bedingungen lassen genau eine Zerlegung übrig. Nach B5 andere Zahlen (nicht 37 · 100) und kein Abzählen mehr. |
| VT1A-032 | korrektur | g | umordnen_und_vergleichen | nein | VT1A-043 | themen vorteil „Rechne geschickt: 125 · 15 · 8“; rollend-5 „Du rechnest 25 · 17 · 4 geschickt …“ | Dort wird ein Produkt geschickt ausgerechnet; hier werden zwei Produkte durch Umordnen verglichen. Gegenüber der früheren Fassung große Zahlen, damit Ausrechnen (über 700 000) nicht lohnt. |
| VT1A-033 | korrektur | b | ausgleich_richtung | ja | neu | themen vorteil „Rechne geschickt: 198 + 467 + 2“ | Dort wird ein Rechenvorteil angewendet; hier wird ein Ausgleich in die falsche Richtung erkannt und seine Wirkung bestimmt. Nach der Zählung der Vorprüfung (zwei Subtraktionen genügen) als Schema gezählt; einzige im Lernziel. |
| VT1A-034 | sicherung | f | umstellen_mit_zeichen | nein | neu | themen vorteil „Welche Gleichung ist falsch? … 69 − 8 = 8 − 69 …“; „Jemand rechnet 80 : 8 : 2 = 80 : 4 = 20. Was ist falsch?“ | Dort wird eine einzelne falsche Gleichung gefunden; hier werden Regeln für das Umstellen in Ketten (mit oder ohne Rechenzeichen) geprüft, die Ablenker sind verallgemeinerte Fehlvorstellungen. |
| VT1A-035 | sicherung | e | beide_faktoren_aendern | nein | neu | themen vorteil „Rechne geschickt: 5 · 17 · 200“ (Faktoren umordnen und zusammenfassen) | Dort wird mit einer erlaubten Umformung gerechnet; hier wird die Wirkung einer unerlaubten (gleichsinnigen) Änderung beider Faktoren auf das Produkt bestimmt, ohne die Produkte auszurechnen. |

Schema: 1 von 5 · Denkfiguren: 5 verschieden · Test: VT1A-031

## zahlen.rechengesetze / verteilen

| Kennung | Pool | Bauplan | Denkfigur | Schema | früher | nächstliegender Bestandskern | Unterschied |
|---|---|---|---|---|---|---|---|
| VT1A-036 | test | b | zerlegung_pruefen | nein | neu | themen verteilen „Welcher Term ist gleich 3 · (10 + 3)?“; rollend-12 „8 · 27: Zerlege 27 in 20 + 7 und rechne 8 · 20 + 8 · 7“ | Dort wird ein Faktor zerlegt und angewendet; hier werden beide Faktoren zerlegt, und die fehlenden Teilprodukte müssen am Aufbau erkannt werden (Rechteck aus vier Teilen). Nach B3 nicht mehr „Drei der vier … welche anders?“. |
| VT1A-037 | korrektur | e | faktor_aendern_wirkung | nein | neu | themen verteilen „Rechne geschickt: 17 · 99 + 17“; „Rechne geschickt: 7 · 299“ | Dort wird ein Produkt mit dem Verteilungsgesetz ausgerechnet; hier wird nur die Wirkung einer Änderung eines Faktors bestimmt, ohne das Produkt auszurechnen. |
| VT1A-038 | korrektur | d | terme_deuten | ja | neu | themen verteilen „Ein Kino verkauft am Samstag 37 und am Sonntag 63 Karten zu je 9 €. Wie viel Geld …?“; rollend-5 „Zwei Teile eines Rechtecks: Welcher Term gibt die ganze Fläche?“ | Dort wird zur Situation ein Term gesucht oder ausgerechnet; hier werden zwei gleichwertige Terme nach ihrer Bedeutung (Bezahlweg) unterschieden. Format Term ↔ Text, nach C4 als Schema gezählt; einzige im Lernziel. |
| VT1A-039 | sicherung | b | fehlregel_verteilen_produkt | nein | neu | themen verteilen „Jemand rechnet 6 · (20 + 4) = 6 · 20 + 4 = 124. Was ist falsch?“; rollend-12 „Nina berechnet 6 · 43 … erster Fehler in Zeile …“ | Andere Fehlvorstellung als im Bestand (Verteilen über ein Produkt); gefragt ist nach der Wirkung der falschen Regel für jede Zahl □. Warum kein Schema: □ ist beliebig, die Antwort ist ein Zusammenhang (□-mal), kein Wert, der sich durch Einsetzen eines ersten Probierwerts ergibt. Ersetzt 039 (A4). |
| VT1A-040 | sicherung | e | gemeinsamer_faktor_skalieren | nein | VT1A-054 | rollend-5 verteilen „Die Tabelle beschreibt zwei Teile eines Rechtecks, die nebeneinander liegen. Welcher Term gibt die ganze Fläche?“ | Dort wird ein Term zur Fläche gewählt; hier wird ohne Zahlen die Wirkung einer Änderung des gemeinsamen Faktors auf die ganze Summe beurteilt. Gegenüber der früheren Fassung ohne Zahlen, damit Ausrechnen nicht genügt. |

Schema: 1 von 5 · Denkfiguren: 5 verschieden · Test: VT1A-036

## zahlen.rechengesetze / umkehraufgabe_mal

| Kennung | Pool | Bauplan | Denkfigur | Schema | früher | nächstliegender Bestandskern | Unterschied |
|---|---|---|---|---|---|---|---|
| VT1A-041 | test | c | loesbarkeit_teiler | nein | VT1A-057 | themen umkehraufgabe_mal (Bonus) „Für wie viele ganze Zahlen x ist (−60) : x eine ganze Zahl, die größer als 5 ist?“ | Dort wird eine Divisionsaufgabe mit ganzen Zahlen durchsucht; hier wird die Lösbarkeit einer Gleichung mit Parameter als Teilbarkeit gedeutet (nur natürliche Zahlen, Grenzen eingeschlossen). |
| VT1A-042 | korrektur | d | aufgabenfamilie | nein | neu | themen umkehraufgabe_mal „Welche Umkehraufgabe löst die Gleichung 5 · x = −10?“ | Dort wird die Rechnung für x gewählt; hier ist das Produkt □ unbekannt (nichts auszurechnen), gesucht ist eine gleichwertige Gleichung aus derselben Aufgabenfamilie. Ersetzt die Kinderregel-Aufgabe (B1). |
| VT1A-043 | korrektur | d | gleichung_zu_geschichte | ja | VT1A-061 | themen umkehraufgabe_mal „Welche Gleichung passt zu: Das (−4)-Fache einer Zahl ist 28?“ | Umgekehrte Richtung (Gleichung → Geschichte), Ablenker vertauschen die Rollen von Gesamtzahl, Anteil und Anzahl. Weil es im Kern das Bestandsformat „Text ↔ Gleichung“ ist, zähle ich die Aufgabe als Schema. |
| VT1A-044 | sicherung | e | parameter_wirkung | nein | neu | themen umkehraufgabe_mal „Für welche Zahl a hat die Gleichung a · x = −48 die Lösung x = −6?“ | Dort wird ein Parameter aus einer gegebenen Lösung bestimmt; hier wird ohne konkrete Zahlen beurteilt, wie sich die Lösung ändert, wenn sich der Parameter ändert. |
| VT1A-045 | sicherung | f | loesung_gegen_b | nein | neu | themen umkehraufgabe_mal „Stimmt die Aussage? Bei x : 8 = 5 rechnet man x = 5 : 8.“; „Löse 72 : x = 9“ | Dort wird eine Gleichung gelöst oder eine Rechenregel geprüft; hier wird eine allgemeine Aussage über die Größe der Lösung geprüft und das einzige Gegenbeispiel gesucht. Warum kein Schema: a und b sind beliebig, die Lösbarkeit (Test 041) spielt keine Rolle; entscheidend ist die Suche nach dem Gegenbeispiel a = 1 in einem offenen Suchraum. Ersetzt 045 (B1). |

Schema: 1 von 5 · Denkfiguren: 5 verschieden · Test: VT1A-041

## zahlen.rechengesetze / ueberschlag

| Kennung | Pool | Bauplan | Denkfigur | Schema | früher | nächstliegender Bestandskern | Unterschied |
|---|---|---|---|---|---|---|---|
| VT1A-046 | test | a | groessenordnung_eingrenzen | nein | VT1A-049 | themen ueberschlag „Ein Stadion hat 18 900 Plätze. Wie oft passt eine Schule mit 612 Kindern ungefähr hinein?“ | Dort wird ein ungefährer Wert geschätzt; hier wird eine vorgerechnete grobe Schätzung beurteilt: Das Kind muss selbst erkennen, dass sie die Stellenzahl nicht entscheidet, und eine sichere Schranke finden. Warum kein Schema: Der Text nennt kein Verfahren; die Ablenker haben verschiedene Urteile (7, 6, nicht entscheidbar), und genaues Ausrechnen (vierstellig mal vierstellig) ist nicht verlangt und unattraktiv. Ersetzt den Text von 046 (A3). |
| VT1A-047 | korrektur | b | fehlregel_abschneiden | nein | neu | rollend-5 ueberschlag „Kim überschlägt 4 987 · 21 … Zeile 1: Ich runde 4 987 auf Tausender: 4 000 … erster Fehler in Zeile …“ | Gleiche Fehlvorstellung (Abschneiden statt Runden), aber andere Leistung: Die Regel ist genannt, gefragt ist die größte mögliche Abweichung zum richtigen Runden (kein falscher Wert als Lösung, B1). |
| VT1A-048 | korrektur | a | genauigkeit_der_rundung | ja | VT1A-067 | rollend-5 ueberschlag „Überschlage 612 + 349 + 98. Weg A rundet auf Hunderter, Weg B auf Zehner. Um wie viel ist B größer?“ | Dort wird der Unterschied zweier Überschläge berechnet; hier wird die Genauigkeit beurteilt. Weil das genaue Ergebnis genannt ist, genügt Ausrechnen und Vergleichen; ich zähle die Aufgabe als Schema. |
| VT1A-049 | sicherung | h | sicher_entscheiden | nein | neu | themen ueberschlag „Ein Kino hat 12 Reihen mit je 28 Plätzen. Reichen die Plätze für 3 Klassen mit je 105 Kindern? Entscheide mit einem Überschlag.“ | Dort wird eine einzelne Frage mit einem Überschlag entschieden; hier muss beurteilt werden, wann ein Überschlag überhaupt sicher entscheidet (Rundungsrichtung und Abstand zur Grenze). Nach B3 aus dem Test in die Sicherung verschoben (früher VT1A-046). |
| VT1A-050 | sicherung | g | richtung_beim_teilen | nein | neu | themen ueberschlag „Stimmt die Aussage? Rundet man beim Überschlag einer Summe beide Zahlen auf, ist der Überschlag größer als das genaue Ergebnis.“; „Überschlage 4 812 : 6“ | Dort geht es um die Richtung bei einer Summe oder um das Bilden eines Überschlags; hier wird die Richtung beim Teilen beurteilt, wo Aufrunden des Teilers das Ergebnis kleiner macht. |

Schema: 1 von 5 · Denkfiguren: 5 verschieden · Test: VT1A-046

## zahlen.rechengesetze / sach

| Kennung | Pool | Bauplan | Denkfigur | Schema | früher | nächstliegender Bestandskern | Unterschied |
|---|---|---|---|---|---|---|---|
| VT1A-051 | test | h | zwei_modelle_vergleichen | nein | VT1A-071 | themen sach (Bonus) „Kinderkarten kosten 6 €, Erwachsenenkarten 10 €. 30 Personen zahlen zusammen 220 €. Wie viele Kinder?“ | Dort wird eine Aufteilung gesucht; hier werden zwei Kostenmodelle (Grundgebühr und Preis je Einheit) aufgestellt und der Punkt bestimmt, ab dem sich die Reihenfolge umkehrt. Gegenüber der früheren Fassung wird nach „ab wann teurer“ statt „gleich teuer“ gefragt. |
| VT1A-052 | korrektur | d | rest_deuten | nein | neu | themen sach „Eine Klasse fährt mit dem Bus ins Museum. Der Bus kostet 420 €, jedes Kind zahlt 15 €. Welche Angabe fehlt …?“ | Dort wird nach einer fehlenden Angabe gefragt; hier ist die Rechnung gegeben, und der Rest einer Division muss je nach Frage verschieden gedeutet werden (aufrunden, abrunden, Rest, Ergänzung). |
| VT1A-053 | korrektur | e | ausklammern_im_sachkontext | nein | neu | themen verteilen „Ein Kino verkauft am Samstag 37 und am Sonntag 63 Karten zu je 9 €“ (andere Etappe); themen sach „Ein Schulkino verkauft 249 Karten zu je 8 €. Die Filmmiete kostet 200 €.“ | Dort wird ein Betrag ausgerechnet; hier ist der Heftpreis unbekannt, und der Unterschied zweier Einkaufswege folgt nur über das Ausklammern. Warum kein Schema: □ ist beliebig, es gibt keine Fälle zum Durchprobieren; das Rechengesetz (8 · □ + 8 · 3 = 8 · (□ + 3)) trägt die Lösung. Ersetzt 053 (A5). |
| VT1A-054 | sicherung | f | reihenfolge_wirkung | nein | neu | rollend-5 sach „Ich denke mir eine Zahl. Ich addiere 12 und multipliziere die Summe mit 4 …“ | Dort wird ein einzelnes Rätsel rückwärts gelöst; hier wird die Wirkung der Reihenfolge zweier Schritte für alle Startzahlen beurteilt (immer – manchmal), begründet mit dem Verteilungsgesetz. |
| VT1A-055 | sicherung | h | modellwahl_gleichung | ja | VT1A-076 | themen sach „Ein Fest: 39 Gäste zahlen je 4 € Eintritt. Davon gehen 43 € für Getränke ab. Welcher Term …?“ | Modellwahl mit echten Modellfehlern, jede Option mit eigenem, im Modell richtig gerechnetem Ergebnis. Weil man die Geschichte auch direkt rückwärts lösen und die Option mit x = 25 suchen kann, zähle ich die Aufgabe als Schema. |

Schema: 1 von 5 · Denkfiguren: 5 verschieden · Test: VT1A-051
