# Verhältnis rechnen : verstehen – Antwort auf die FRAGE vom 27.11., 01:45

Nur Inhalte, nichts eingespielt. **[G]** gesichert (im Code gelesen oder im Bestand gezählt), **[M]** meine Einschätzung.

## Zuerst der Widerspruch: Über die Art gezogen bleibt alles beim Alten

- **[G]** Der Bestand ist nicht einseitig. 18 095 Übungen, 84 % mit Typ `g`. Nach Tätigkeit: **rechnen 52 %, verstehen 30 %, anwenden 19 %** – und zwar in allen acht Gebieten fast gleich (rechnen 46–53 %, verstehen 25–33 %, anwenden 14–25 %). Der verlangte Takt „jede dritte verstehen“ ist im Bestand **schon erfüllt**.
- **[G]** Auch meine neuen Aufgaben sind nach `g` mehrheitlich „rechnen“ (Runde 3: 75 rechnen, 45 verstehen, 7 anwenden).
- **[M] Folge: Ein Takt über die Art fordert eine Verstehen-Aufgabe an – und bekommt eine aus dem Bestand.** Der steht vorn und hat je Lernkarte 9 bis 13 verschiedene `g` **[G]**, deckt also jede Art ab. Das Problem bliebe unverändert.

Der Unterschied zwischen neu und alt ist nicht die Tätigkeit, sondern die **Form**: wie gefragt und wie geantwortet wird. Deshalb zwei Kennzeichen mit zwei Zwecken:

1. **Takt über die Form** – löst die Vorrats-Frage. Dafür ist ein neues Feld `form` nötig (leer = Bestand).
2. **Mindestzahlen über die Art** – löst eine andere, echte Frage: dass `anwenden` nicht untergeht. **[G] Dafür ist kein neues Feld nötig:** Die Art folgt aus `g`, und `g` steht schon in der Datenbank (`schule.aufgabe.typ`).

## 1. Welches Verhältnis

**[M]** Keine Quote je Lernkarte, sondern zwei Regeln nebeneinander, beide im Fenster der ersten 9 Aufgaben:

- **Form:** jede dritte Aufgabe in neuer Form, solange Vorrat da ist.
- **Art:** mindestens 3 „verstehen“ und mindestens 1 „anwenden“, Rest frei.

**Gleich für Klasse 5 und 8** – die Klasse ist nicht der Unterschied, die Stufe ist es. **Gleich für alle Gebiete** – der Bestand liefert es dort von selbst **[G]**. Einzige Stelle, an der die Mindestzahl wirklich greift: Funktionen mit nur 14 % `anwenden`.

## 2. Platz im Ablauf

„Lückenweg zuerst, Fehler-Detektiv und Umkehren gegen Ende“ stimmt. Drei Einschränkungen **[M]**:

- Lückenweg **nur beim ersten Öffnen** der Lernkarte – nicht bei einer wieder geöffneten Etappe, nie in der Wiederholung. Ein Gerüst misst nichts.
- Der Lückenweg zählt nicht für „gelandet“ (`zaehlt: nein`) und kostet damit eine Aufgabe. Das ist der Preis und er ist vertretbar; genannt werden muss er trotzdem.
- **Fehler-Detektiv gegen Ende** stützt sich fachlich: Ein falscher Rechenweg, bevor der eigene sicher ist, prägt sich mit ein. Ergänzung: **nie direkt nach einem eigenen Fehler.**

**[G] Anfang, Mitte und Ende stecken größtenteils schon in der Stufe**, denn die App zieht nach Stufe und die Stufe folgt aus `g`. Ein zweiter Takt daneben kann ihr widersprechen. Deshalb: Der Form-Takt wählt **innerhalb** der Stufe, die die App ohnehin bestimmt, und verschiebt sie nie.

## 3. Wie viele selbst gerechnete Aufgaben, und `zaehlt`

**[G]** Heute: 6 eigene Lösungen, 2 verschiedene `g`, 1 Stufe-3-Typ, die letzten 3 in Folge. **[M]** Die 6 bleibt richtig, mit zwei Nachbesserungen:

- **Mindestens eine der 6 muss `anwenden` sein**, wenn die Lernkarte eine hat. Heute lässt sich „gelandet“ erreichen, ohne eine einzige Sachaufgabe gerechnet zu haben.
- **`zaehlt` auf zwei Werte kürzen: `ja` / `nein`.** `folge` habe ich in Runde 2 und 3 **kein einziges Mal** gebraucht (0 von 243) **[G]**, und eine halbe Lösung macht „letzte 3 in Folge“ unentscheidbar.

**Widerspruch zum Entwurf:** „Sitzt bleibt ans Rechnen gebunden“ ist zu grob. „Umkehren“, „Verfahren wählen“ und „viele richtige Antworten“ verlangen **mehr** eigenes Rechnen als eine Standardaufgabe, nicht weniger – wer eine Gleichung mit der Lösung x = 6 baut, rechnet und prüft. Nicht zählen darf, was das **Gerüst** vorwegnimmt. Genau das sagt `zaehlt`, und nicht die Art.

## 4. Reicht der Vorrat?

**[G] Nein.** Von 131 belieferten Lernkarten haben **70 weniger als drei** neue Aufgaben (Runde 1: 24 von 37, Runde 2: 16 von 39, Runde 3: 30 von 55). Bei „jede dritte“ und 6 bis 10 Aufgaben je Lernkarte braucht es **drei je Lernkarte**, bei wieder geöffneten Etappen mehr. Bis auf drei je Lernkarte fehlen **105 Aufgaben**.

**[M]** Ziel je Lernkarte: drei, davon mindestens eine mit `zaehlt: ja` auf Stufe 2 oder 3. Auftrag 19 war geliefert, bevor diese Frage kam; das Nachliefern ist ein eigener Auftrag.

## 5. Wiederholungen (1, 3, 7, 14, 30 Lerntage)

**[M]** Tag 1 **rechnen** (Grundform, Stufe wie zuletzt) · Tag 3 und 7 **gemischt** · Tag 14 und 30 **verstehen bevorzugt**. Am Tag 1 wird das frische Verfahren gefestigt; nach 14 Tagen trägt nur, was verstanden ist, und an Tag 14 hängt die Anzeige „sicher“.

Zwei harte Grenzen: **Nie ein Lückenweg in der Wiederholung.** Und: **[G]** Zwei Fehler in einer fälligen Wiederholung öffnen die Etappe überall. Steht dort eine schwere Verstehen-Aufgabe, öffnet sie Etappen, die rechnerisch sitzen. Deshalb **höchstens eine Verstehen-Aufgabe je Etappe und Wiederholung, und sie allein darf nicht öffnen.**

## 6. Zwei Arten oder drei?

**[M] Drei: rechnen · verstehen · anwenden.** Zwei reichen nicht: „aus einer Situation die Rechnung selbst aufstellen“ ist weder Ausführen noch Beurteilen und verschwindet sonst in „rechnen“ – im Bestand immerhin 19 %. Eine vierte Art braucht es nicht.

**Selbstkritisch [G]:** Meine Formbezeichnung „Anwenden“ deckt sich *nicht* mit der Art `anwenden` – von 31 solchen Aufgaben tragen nur 4 ein `g` der Art `anwenden`, der Rest ist `mehrschritt` oder `verknuepfen`. Die Form sagt die Art also nicht vorher; maßgeblich ist `g`.

### Zuordnung der 14 Typen `g`

| Stufe | `g` | Art | Grund |
|---|---|---|---|
| 1 | `direkt` | rechnen | Verfahren ausführen |
| 1 | `erkennen` | verstehen | zuordnen, ablesen, benennen – es wird nichts gerechnet |
| 2 | `mehrschritt` | rechnen | mehrere Schritte desselben Verfahrens |
| 2 | `einkleidung` | **anwenden** | Sachsituation führt auf die Rechnung |
| 2 | `umkehr` | rechnen | gerechnet wird, nur eine andere Größe ist gesucht |
| 2 | `darstellung` | verstehen | Wechsel zwischen Tabelle, Bild und Term |
| 3 | `rueckwaerts` | rechnen | mehrere Schritte rückwärts |
| 3 | `verknuepfen` | rechnen | braucht früheren Stoff, bleibt Rechnen |
| 3 | `begruenden` | verstehen | Aussage prüfen, Gegenbeispiel |
| 3 | `fehler` | verstehen | fremden Weg beurteilen |
| 3 | `transfer` | **anwenden** | Modell selbst aufstellen |
| 3 | `parameter` | verstehen | über die Form der Lösung nachdenken |
| 3 | `pruefung` | **anwenden** | mehrteilige Sachaufgabe |
| Bonus | `knobel` | – | zählt nie, braucht keine Art |

### Zuordnung der acht Formen (Schwerpunkt, gezählt an allen 319 Aufgaben der drei Runden)

| Form | häufigste `g` | Schwerpunkt-Art | zählt für „sitzt“ |
|---|---|---|---|
| Lückenweg | `direkt`, `mehrschritt` | rechnen (33 von 33) | nein |
| Zwei Wege vergleichen | `mehrschritt` | rechnen (16 von 17) | ja |
| Umkehren | `umkehr`, `rueckwaerts` | rechnen (50 von 57) | ja |
| Viele richtige Antworten | `umkehr`, `direkt`, `parameter` | rechnen (56 von 80) | ja |
| Anwenden | `mehrschritt`, `verknuepfen` | rechnen (25 von 31) | ja |
| Brücke | `darstellung`, `direkt` | gemischt (12 verstehen, 11 rechnen) | ja |
| Fehler-Detektiv | `erkennen`, `fehler` | verstehen (40 von 46) | ja |
| Verfahren wählen | `erkennen` | verstehen (27 von 28) | ja |

## 7. Die Regeln, ausformuliert

1. **Takt je Lernkarte:** Jede dritte Aufgabe trägt ein `form`-Kennzeichen, die anderen zwei kommen aus dem Bestand. Gezählt wird je Lernkarte und Kind, nicht je Sitzung.
2. **Mindestmischung je Lernkarte:** Unter den ersten 9 Aufgaben mindestens 3 der Art `verstehen` und mindestens 1 der Art `anwenden`, soweit die Lernkarte sie hat.
3. **Ausnahme leerer Vorrat:** Ist der Vorrat einer Form oder Art leer, geht es ohne Ersatz weiter – die Regel darf nie eine Aufgabe erzwingen, die es nicht gibt, und nie eine schon gelöste wiederholen.
4. **Nach zwei Fehlern in Folge:** Die App senkt schon heute die Stufe **[G]**. Zusätzlich **einmal** ein Lückenweg derselben Lernkarte, falls vorhanden – danach zurück zu gewöhnlichen Aufgaben der gesenkten Stufe. **Nie zwei Gerüst-Aufgaben hintereinander**, sonst rechnet das Kind gar nicht mehr.
5. **„Sitzt“:** 6 eigene Lösungen wie heute, davon keine mit `zaehlt: nein` und mindestens eine der Art `anwenden`. `zaehlt` nur noch `ja`/`nein`.
6. **Flug-Test und Nachtest:** Formen sind erlaubt, Gerüste nicht – also kein Lückenweg und nichts mit `zaehlt: nein`. Im Nachtest zusätzlich **keine neue Form, die das Kind beim Üben nie gesehen hat**: Sonst misst der Test die Form und nicht den Stoff.
7. **Verweis ins Regel-Universum:** **Nein, nicht vor der Aufgabe.** Ein Verweis davor verrät, worauf es ankommt; aus „begründen“ wird „nachschlagen“. Die Regel-Kennung hängt ohnehin an jeder neuen Aufgabe und gehört in die **Rückmeldung** – nach dem ersten Fehlversuch und am Ende. Einzige Ausnahme: der Lückenweg, der ohnehin geführt ist.

## Nicht geprüft

- Die Zahlen stammen aus den Dateien im Repo, nicht aus der Datenbank; dort stehen mehr Aufgaben.
- Kein Kind hat nach diesen Regeln geübt. Der Takt „jede dritte“ ist eine Setzung, keine Messung.
- Wie sich der Form-Takt mit Mischkarten und Expeditionen verträgt, habe ich nicht verfolgt.
