# Verhältnis rechnen : verstehen – Vorschlag des Mathe-Profis

Antwort auf die Frage des Projektleiters (Postfach 27.11., 01:45) zu Auftrag 19. Nur ein fachlicher Vorschlag, nichts gebaut.
Zeichen: **[G]** gesichert (aus den Dateien gelesen oder gezählt), **[A]** Annahme, **[M]** meine fachliche Einschätzung.
Kein Wert hier stammt aus einer Studie. Wo ich mich auf allgemein bekannte Lernforschung stütze, steht es als [M].

## Kurzfassung

- **Takt:** je Lernkarte etwa 2 rechnen : 1 verstehen, fest auf den Plätzen 1, 4, 7, 10 … (bei Klasse 5 Zahlen und Brüche: 3 : 1, Plätze 1, 5, 9). [M]
- **Mindestens 4 von 6 Punkten** für „sitzt“ müssen aus selbst Gerechnetem kommen; Verstehen-Aufgaben zählen höchstens 2 Punkte. [M]
- **Zwei Arten genügen** (rechnen, verstehen). Anwenden und Umkehren sind Rechnen. [M]
- **Der Vorrat reicht nicht.** Gebraucht werden mindestens 2, besser 3 neue Verstehen-Aufgaben je Lernkarte **und Stufe**. [M]

## Was der Bestand heute hergibt [G]

Gezählt in `rollend-1` bis `rollend-3` (rund 320 Aufgaben, 131 Lernkarten; Art nach Tabelle 6a):
Verstehen-Aufgaben je Lernkarte im Mittel 1,8 (je Stufe 0,7 / 0,7 / 0,4). **65 von 131 Lernkarten haben auf Stufe 1 keine, 65 auf Stufe 2 keine, 88 auf Stufe 3 keine.** Umkehren und Anwenden (87 Aufgaben, 27 %) sind Rechnen und füllen den Verstehen-Vorrat nicht. Lückenweg liegt fast nur auf Stufe 1 (26 von 33).

## 1. Verhältnis

- **Grundzahl 2 : 1 je Lernkarte** (bei 8 Aufgaben 5 rechnen, 3 verstehen; Takt „jede dritte“). [M] Das ist dasselbe Verhältnis wie der Vorschlag der zweiten KI (1 : 2), nur zähle ich es **je Lernkarte, nicht je Lernkarte und Stufe**: Der Vorrat je Stufe (0,4 bis 0,7) ist zu klein für einen festen Takt je Stufe. [G für den Vorrat, M für die Folgerung]
- **Klasse 5:** bei Zahlen, Brüchen, Größen 3 : 1. Hier muss Rechenfertigkeit erst automatisch werden; sie braucht Menge. **Klasse 8:** 2 : 1, weil Algebra und Funktionen ohne Verständnis nicht tragen. [M]
- **Geometrie und Daten:** gleiche Zahl 2 : 1. Dort ist „rechnen“ oft Zeichnen oder Messen, das die App nicht kann; mehr Verstehen wäre fachlich gut, der Vorrat gibt es aber nicht her. [M] Der Takt wird je Flug als Zahl in der Datenbank eingestellt, damit man nach den ersten Erfahrungen nachjustieren kann. [A]

**Widerspruch zum Entwurf:** „Verstehen“ im Entwurf enthält Umkehren. Wer ein Ergebnis rückwärts selbst ausrechnet, rechnet. Umkehren gehört zu „rechnen“; sonst zählt das Kind Rechnen als Verstehen und „sitzt“ wird weicher.

## 2. Ablauf einer Lernkarte (etwa 8 Aufgaben)

Die Form hängt an der **Stufe**, nicht am Platz; die Stufe steigt ohnehin mit den Punkten (0–1 Punkte Stufe 1, 2–3 Stufe 2, 4–5 Stufe 3) [G]. Das ergibt:

| Platz | Art | Form | Stufe | Punkt? |
|---|---|---|---|---|
| 1 | verstehen | **Lückenweg** (wie ein Lösungsbeispiel, [M]) | 1 | nein |
| 2, 3 | rechnen | direkt, erkennen | 1 | ja |
| 4 | verstehen | Verfahren wählen oder Brücke | 2 | ja |
| 5, 6 | rechnen | mehrschritt, Umkehren, Anwenden | 2 bis 3 | ja |
| 7 | verstehen | **Fehler-Detektiv** oder bedingung | 3 | ja |
| 8 | rechnen | schwere Rechenaufgabe, zum Schluss wieder selbst rechnen | 3 | ja |

Ja zu „Lückenweg zuerst“ und „Fehler-Detektiv spät“. Nein zu „Umkehren gegen Ende als Verstehen-Platz“ (siehe oben). Das Ende soll **rechnen** sein: Die „letzten 3 in Folge“ aus der heutigen Regel prüfen dann das Rechnen. [M]

## 3. Mindestzahl selbst gerechneter Aufgaben und `zaehlt`

- **Von 6 Punkten mindestens 4 aus Art rechnen, höchstens 2 aus verstehen.** Die Stufe-3-Aufgabe, die heute verlangt wird, muss Art rechnen sein. [M] Bei Takt 2 : 1 ergibt das genau die natürliche Mischung (4 + 2); wer Verstehen-Aufgaben verfehlt, rechnet einfach mehr.
- **`zaehlt` passt nicht ganz.** Es sagt nur, wie viel Hilfe da war (nein / folge / ja), nicht ob das Kind selbst gerechnet hat. Ein Fehler-Detektiv mit `ja` gäbe heute einen vollen Punkt. Lösung: `zaehlt` bleibt, die Art kommt als zweites Merkmal dazu (Tabelle 6a). Feste Bedeutung: **nein** = kein Punkt, auch kein Fehler in Folge; **folge** = kein Punkt, richtig zählt für „letzte 3 in Folge“, falsch unterbricht sie; **ja** = Punkt (bei Art verstehen unter der Obergrenze 2). [G: Feld und Werte aus `rollend-1/README.md`; Bedeutung von mir festgelegt]
- Die Art braucht **kein neues Handfeld**: Sie folgt für neue Aufgaben aus `typ` (6a), für den Bestand aus `g` (6b); ohne `g` gilt „rechnen“. [A]

## 4. Reicht der Vorrat?

**Nein.** [G] Bedarf je Lernkarte [M]: Lernweg 3 (eine je Stufe) plus Reserve für Fehlversuche 3, dazu Wiederholungen nach 1, 3, 7, 14, 30 Tagen (5 Termine, je eine Verstehen-Aufgabe, nicht schon gelöst). Das sind rund 10.
- **Mindestwert für den Start: 2 je Lernkarte und Stufe** (6 je Lernkarte). **Ziel: 3 je Lernkarte und Stufe** (9).
- Den Rest deckt, so weit nötig, der Bestand mit den Typen `erkennen`, `fehler`, `begruenden` (Tabelle 6b) als Fallback. Wie viele das je Lernkarte sind, **habe ich nicht gezählt** [A: es sind genug für die Lücke auf Stufe 3, nicht auf Stufe 1].
- **Für Auftrag 19 und danach:** je Lernkarte und Stufe 2 Verstehen-Aufgaben in diesen Formen: Stufe 1 Lückenweg und Verfahren wählen; Stufe 2 Brücke, Zwei Wege vergleichen, Verfahren wählen; Stufe 3 Fehler-Detektiv, bedingung. **Keine zusätzlichen Umkehren- und Anwenden-Aufgaben** (87 sind genug). Das ist bei sechs Lernkarten rund 36 statt heute rund 11 Verstehen-Aufgaben je Flug, also mehr als dreimal so viele. Für die schon gelieferten Flüge ergänzt man zuerst die Stufe-1- und Stufe-2-Lücken.

## 5. Wiederholungen (Tag 1, 3, 7, 14, 30)

**Gemischt, aber mit Verschiebung.** [M] Tag 1 und 3: wie normal, 2 : 1 (das Gelernte abrufen). Tag 7, 14, 30: 1 : 1, die Verstehen-Aufgabe zuerst (nach Wochen hält die Rechenfertigkeit meist länger als das „Warum“; das ist die Erfahrung der Lernforschung zum verteilten Üben, nicht ein Messwert von uns). In der Wiederholung ändern **nur Rechnen-Aufgaben den Stand der Karte**; eine falsche Verstehen-Aufgabe zeigt die Regel, bucht aber nichts. [A, damit eine einzige Auswahl-Aufgabe keine Karte kippt]

## 6. Zwei Arten genügen

Die Art steuert nur zwei Dinge: den Takt und die Zählung für „sitzt“. Beides fragt: „Hat das Kind selbst gerechnet?“ Eine dritte Art „anwenden“ ändert keine dieser Entscheidungen und würde einen dritten Vorrat schaffen, der leer läuft. Sachaufgaben bleiben über `g` (`einkleidung`, `transfer`) sichtbar. [M]

**6a – neue Form → Art**

| Form | Art | `zaehlt` (Vorschlag) |
|---|---|---|
| Lückenweg | verstehen | nein oder folge |
| Fehler-Detektiv | verstehen | ja |
| Verfahren wählen | verstehen | ja |
| Zwei Wege vergleichen | verstehen | ja |
| Brücke | verstehen | ja |
| Viele richtige Antworten (bedingung) | verstehen | ja |
| Umkehren | **rechnen** | ja |
| Anwenden | **rechnen** | ja |

**6b – Typ `g` des Bestands → Art**

| `g` | Art | `g` | Art |
|---|---|---|---|
| direkt | rechnen | rueckwaerts | rechnen |
| erkennen | verstehen | verknuepfen | rechnen |
| mehrschritt | rechnen | begruenden | verstehen |
| einkleidung | rechnen | fehler | verstehen |
| umkehr | rechnen | transfer | rechnen |
| darstellung | rechnen | parameter | rechnen |
| pruefung | rechnen | knobel | keine (Bonus, zählt weder für Takt noch für „sitzt“) |

Ein `typ` der neuen Formen schlägt das `g` (Lückenweg mit `g = direkt` ist verstehen). [M]

## 7. Die Regeln

1. **Art:** Jede Aufgabe hat die Art `rechnen` oder `verstehen`, abgeleitet nach 6a (neue Formen) oder 6b (Bestand); ohne `typ` und ohne `g`: `rechnen`.
2. **Takt:** Je Lernkarte und Sitzung zählt die App die gezogenen Aufgaben (ab Platz 1). Platz 1, 4, 7, 10 … (Zahl `n = 3`, einstellbar je Flug; Klasse 5 Zahlen, Brüche, Größen `n = 4`) ist ein Verstehen-Platz, alle anderen Rechnen-Plätze.
3. **Form nach Stufe:** Auf einem Verstehen-Platz wählt die App die Aufgabe der **aktuellen Stufe**; sonst die nächstleichtere. Ungelöst vor gelöst, nie dieselbe Form zweimal hintereinander (wie heute).
4. **Leerer Vorrat:** Reihenfolge auf dem Verstehen-Platz: neue Form, Stufe passend → Bestand-Verstehen (`erkennen`, `fehler`, `begruenden`) → neue Form der nächstleichteren Stufe → Rechnen. Ein ausgefallener Platz wird **nicht nachgeholt**. Auf einem Rechnen-Platz wird nie eine Verstehen-Aufgabe gezogen.
5. **Neue Rechenformen:** Auf Rechnen-Plätzen darf eine nicht gelöste Umkehren- oder Anwenden-Aufgabe der passenden Stufe **jede zweite** Rechnen-Aufgabe sein; so verschwinden sie nicht hinten, ohne das Verhältnis zu ändern.
6. **Zwei Fehler in Folge** (nur Aufgaben mit `zaehlt` = ja oder folge): wie heute eine Stufe leichter, und die nächste Aufgabe ist ein **Lückenweg** der neuen Stufe (ersetzt den nächsten Platz, höchstens einmal je Sitzung). Gibt es keinen, kommt eine rechnen-Aufgabe der leichteren Stufe.
7. **Punkte:** `ja` zählt einen Punkt (bei erstem Versuch richtig, ohne Tipp, wie heute). `nein` und `folge` zählen keinen.
8. **„Sitzt“:** 6 Punkte, davon mindestens 4 aus Art rechnen, höchstens 2 aus Art verstehen (die übrigen verstehen-Punkte verfallen nicht, sie zählen nur nicht darüber hinaus). Dazu die heutigen Bedingungen: mindestens 2 Typen `g`; eine Stufe-3-Aufgabe der Art rechnen mit Stufe-3-Typ; die letzten 3 gebuchten Antworten richtig. Gibt es weniger als 4 freie Rechnen-Aufgaben, gilt wie heute „so viele wie da sind, mindestens 2“.
9. **Wiederholung:** Tag 1 und 3 Takt `n = 3`, Tag 7, 14, 30 Takt `n = 2` mit Verstehen auf Platz 1. Nur Rechnen-Aufgaben ändern den Stand der Karte.
10. **Flug-Test:** Mindestens 3 von 4 Aufgaben Art rechnen. Verstehen nur mit Eingabe (`zahl`, `luecken`, `bedingung`), nie `Lückenweg` und nie reine Auswahl wie `Verfahren wählen` (Ratechance). Für „bestanden“ zählen nur die Rechnen-Aufgaben. [A]
11. **Nachtest:** wie Flug-Test; Verstehen-Aufgaben nur zur Rückmeldung, nie für „bestanden“. [A: Ich nehme an, der Nachtest ist die Wiederholung eines nicht bestandenen Flug-Tests.]
12. **Knobel-Bonus** (`knobel`) bleibt außerhalb von Takt, Punkten und Tests.
13. **Verweis ins Regel-Universum:** **Nicht zu Beginn** einer Verstehen-Aufgabe (er würde die Lösung vorwegnehmen und das Kind liest statt zu denken [M]), **außer beim Lückenweg** auf Stufe 1, der ohnehin geführt ist. Sonst erst **nach einer falschen Antwort**: ein Satz plus Verweis (Regel- und Fehlbild-Kennung stehen schon in jeder Aufgabe). [G: Kennungen liegen vor]

## Was ich nicht weiß

- **Kein Kind hat die neuen Formen bisher bearbeitet.** Takt `n = 3`, die Obergrenze 2, die 4 Punkte und die Wiederholungs-Verschiebung sind begründete Schätzungen, keine Messwerte. [M]
- **Wie viele Bestand-Aufgaben `erkennen`, `fehler`, `begruenden` je Lernkarte da sind**, habe ich nicht gezählt; davon hängt ab, wie groß der Fallback in Regel 4 wirklich ist.
- **Ob 8 Aufgaben je Lernkarte stimmen.** Der Auftrag nennt etwa 8; die tatsächliche Zahl hängt von Fehlern und Tipps ab.
- **Wie viele Aufgaben eine Wiederholung hat** und ob der Nachtest wirklich ein wiederholter Flug-Test ist. [A]
- **Ob ein Kind die Verstehen-Formen ohne Heft am Handy gut bedienen kann** (Zeile antippen, Felder füllen): nicht erprobt.
- **Ob sich Klasse 5 und 8 beim Verhältnis wirklich unterscheiden sollten.** Ich habe keine Daten; die Trennung ist fachliche Einschätzung und kann mit `n` später eingeebnet werden.
