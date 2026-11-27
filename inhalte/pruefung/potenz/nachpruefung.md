# Nachprüfung der Potenz-Nachbesserung (Achtundzwanzigste Runde)

Auftrag: `inhalte/AUFTRAEGE.md`, „Nachträge 20.11. nachmittags“, Teil C. Geprüft auf `lernen-app` e8450e0. Die Themendateien dort sind gleich dem Stand des Berichts „FERTIG: Potenz nachgebessert“ (9260c6c).

Nur geprüft: nichts an Inhalten geändert, nichts in die Datenbank, kein App-Code, keine Kinderdaten.

> **Wichtig zur Unabhängigkeit:** Diese Nachprüfung lief im selben Chat, der die Nachbesserung gebaut hat. Sie ist also **keine unabhängige Prüfung** im strengen Sinn.
> Was ich dagegen getan habe:
> - Nachgerechnet habe ich mit dem Skript des Prüf-Chats (`nachrechnen.py`, nicht mit meinem eigenen).
> - Die Liste der Änderungen habe ich direkt aus den Dateien gewonnen: alter Stand 72abf97 gegen jetzt, nicht aus dem Bericht.
> - Alle Aufgaben der neuen Karte habe ich einzeln von Hand nachgerechnet.
>
> Wenn eine wirklich fremde Sicht gewünscht ist, sollte der Chat `pruefung-potenz` oder ChatGPT diesen Bericht gegenlesen.

## Ergebnis in Kürze

- **Rechenfehler:** keiner.
  - Flug A, alle 226 Aufgaben: 115 automatisch geprüft (Skript des Prüf-Chats, 0 Fehler), dazu die übrigen der neuen Karte und alle geänderten Aufgaben von Hand.
  - Neue Karte `potenz_von_potenz`: alle 35 Aufgaben einzeln von Hand nachgerechnet, mit Lösung, falschen Antworten, Lösungsweg und Tipp.
- **Muss 1–2:** erledigt.
- **Sollte 1–6:** erledigt, siehe Tabelle. Zu Sollte 4 gibt es einen neuen Befund (Sollte 1 unten).
- **Prüfskript:** `inhalt_pruefen.py --alle` meldet 118 × OK, Rückgabewert 0. Flug A hat keine Hinweise zu den Karten.
- **Trennung Flug A:** In Text, Antworten, Lösungsweg, Tipp und Karten steht kein negativer Exponent, kein „negativ“ und kein „Kehrbruch“. Jede Teilung hat einen größeren ersten Exponenten, auch im Rechenweg. Das einzige Bruch-Ergebnis ist „(3/4)² · (4/9)²“, ein Bruch als Basis, kein negativer Exponent.
- **Liste alt → neu im Bericht:** vollständig und richtig. Der Abgleich der Dateien zeigt genau die gemeldeten Änderungen und keine weiteren:
  - Flug A: 3 Aufgaben ersetzt, 25 geändert, 1 Kartenfeld.
  - Gym 6: 3 Tipps.
  - Flug B: 4 Fragetexte, 2 Aufgaben aus Flug A dazu, 1 Karte.
  - `terme.umformen`: unverändert.

## Erledigt? (Muss und Sollte aus `bericht.md`)

| Punkt | Stand | Beleg |
|---|---|---|
| Muss 1 (Gym 6, „2² wie 2⁻²“, Tipp) | erledigt | Tipp: „Rechne beide Potenzen aus und teile.“ Der Lösungsweg kommt ohne Gesetz aus. |
| Muss 2 (Flug A, „a⁵ · a¹“, Tipp) | erledigt | Tipp: „a¹ ist a mit dem Exponenten 1. Addiere die Exponenten.“ |
| Sollte 1 (Gym 6, Tipps zu Hoch 0) | erledigt | Beide Tipps arbeiten über das Muster 2², 2¹, 2⁰, wie das Muster der Lernkarte (8, 4, 2, 1 …). In Gym 6 ist per Suchmuster kein Potenzgesetz mehr zu finden. |
| Sollte 2 (zwei Aufgaben nach Flug B) | erledigt | Beide stehen jetzt in Flug B, `gleiche_basis_ganz`, und nicht mehr in Flug A. Die Ersatzaufgaben in Flug A sind richtig: „2¹⁰ : 2ⁿ = 16“ → n = 6; Rechner 10³ · 10⁸ : 10⁹ = 10² → k = 2. Erster Exponent nie kleiner. |
| Sollte 3 (sechs Ablenker) | erledigt | Alle sechs Aufgaben haben neue falsche Antworten. Sie sind wirklich falsch, und die richtige Antwort ist unverändert. Rest siehe Kann 2. |
| Sollte 4 (Stufe/Typ der 23) | erledigt, mit Befund | Die sechs richtigen Rechnungen sind Stufe 1 `erkennen`; 26 → `parameter`, 31 → `rueckwaerts`, 178 → `begruenden`; 43 ersetzt. Dazu 8 weitere Umstufungen (Entscheidung 1), siehe Sollte 1 unten. |
| Sollte 5 (IB) | erledigt | MYP 3: Gym-6-Flug 1, Flug A 2, `terme.umformen` 3. MYP 3 (13 Themen) und MYP 4 (28) lückenlos. In Themendatei und Themenliste steht `ib_myp` 3. Als Annahme gekennzeichnet. |
| Sollte 6 (Typen) | erledigt, mit Hinweis | 75 und 76 sind `direkt`. Die zwei Spiegelbilder haben keinen Typ mehr (Entscheidung 3). 30 ist Stufe 2 `darstellung`, 154 und 156 bleiben Stufe 1 `direkt` (Kann 3). |
| Kann 1, 2, 3, 4, 5, 7 | erledigt | „Bruch“ statt „Bruchterm“ in Karte und vier Aufgaben von Flug B (Antworten gleich, nur neu gemischt). Hinweis-Satz in der Regel von „Gleiche Basis: teilen“. `offen` in Gym 6 ohne „rationale Exponenten im umfang“ und ohne das Beispiel 2³ · 2⁴. `lehrplan_rs` von `terme.umformen` angepasst. `kurz` in Gym 6. Neuer Einstieg von `terme_vereinfachen`. |

## Neue Pflichtkarte `potenz_von_potenz`

- **Lösungen:** alle 35 nachgerechnet, alle richtig.
  - Übungen 23 Aufgaben: Stufe 1: 6, Stufe 2: 8, Stufe 3: 9.
  - Dazu 2 Knobel, 1 Test, 3 Korrektur und 6 Sicherung.
  - Beispiele: „(2³)² und (2²)³“ sind beide 64. Zuckerwürfel (2⁴ · 2²)³ = 2¹⁸. „9² · 27³ = 3¹³“. „(2ⁿ)² höchstens 2²⁰“ ergibt 10 Zahlen. „((2ᵏ)²)³ = 2¹⁸“ ergibt k = 3.
  - Keine falsche Antwort ist versehentlich richtig. Ich habe besonders geprüft, dass bei „(3²)³ = 9⁶“ die richtige Umformung 9³ nicht als falsche Antwort angeboten wird.
- **Erklärung:** fachlich richtig.
  - Die Würfel-Situation braucht nur das Würfelvolumen (Klasse 5/6).
  - Die Schritte zeigen erst das Ausschreiben (2 + 2 + 2), dann die Kurzform 2 · 3.
  - Der typische Fehler (2²)³ = 2⁵ ist genau der häufige Fehler.
  - Probe, Bild und Fehlerbild stimmen.
  - Längen und Wörter sind ohne Hinweis des Prüfskripts.
- **Negative Exponenten:** keine.
- **Lehrplan M7 1.2:** Die Karte deckt „Potenzen von Potenzen mit natürlichen Exponenten“ ab. Pflicht ist richtig.
- **Voraussetzungen:** Die Karte nutzt nur `mal_gleiche_basis` (Pflicht, vorher), nie das Teilen (Vertiefung). Typen, Mindestmengen und höchstens 3 je Typ auf Stufe 3 sind eingehalten.

## Muss

Keins.

## Sollte

1. **Entscheidung 1 widerspricht der README-Definition der Typen.**
   - Sieben Aufgaben der Form „Ein Kind rechnet: … Was ist falsch?“ bzw. „Welcher Satz beschreibt den Fehler richtig?“ sind jetzt Stufe 1 `erkennen`. Sechs stehen in `mal_gleiche_basis`, eine in `gleicher_exponent` (2² · 5² = 10⁴).
   - Die README nennt genau diese Form als Beispiel für `fehler`: „Lea rechnet … Was hat sie falsch gemacht?“. `erkennen` heißt „zuordnen, ablesen, benennen“.
   - Das Ziel ist richtig (Stufe 3 nicht mehr von leichten Aufgaben beherrscht, Grund des Nutzers). Aber der Typ beschreibt jetzt nicht mehr den Gedanken der Aufgabe.
   - Folge: In `mal_gleiche_basis` besteht Stufe 1 aus 11 × `erkennen` gegen 8 × `direkt`. Gut die Hälfte der leichten Stufe ist damit „Fehler benennen“.
   - Die achte Umstufung („Stimmt die Rechnung? 5² · 5³ = 5⁶“, Antwort Nein) halte ich für vertretbar: Das ist ein Urteil über eine Rechnung, wie bei den sechs richtigen Rechnungen.
   - Vorschlag zur Entscheidung (Nutzer oder Haupt-Chat):
     - **(a)** Die sieben Aufgaben bekommen keinen Typ, sind also überzählig und werden beim Einspielen gesperrt. Stufe 3 behält 3 × `fehler`, und keine Aufgabe trägt einen falschen Typ. Die Karte hat genug andere Übungen.
     - **(b)** Es bleibt so, aber die README bekommt den Satz: „Auswahl mit Regelnamen (‚Was ist falsch?‘) zählt als `erkennen`.“ Dann gilt das auch für andere Flüge.
2. **Lernstand: Die neue Pflichtkarte öffnet Flug A wieder.**
   - Das betroffene Kind hat die vier Karten in `terme.umformen` gelandet. Nach dem Umhängen fehlt ihm in Flug A die Pflichtkarte `potenz_von_potenz`.
   - Der Flug ist dann nicht mehr fertig, und das Ziel „der abgeschlossene Ort bleibt abgeschlossen“ (Sechsundzwanzigste Runde) gilt nicht mehr ohne Weiteres.
   - Das ist kein Inhaltsfehler, aber der Haupt-Chat muss es vor dem Umhängen entscheiden: neue Karte als offen zeigen, oder sie für dieses Kind als „Kann er – aber wiederholen“ setzen (LB-3).

## Kann

1. **Entscheidung 3 (zwei Spiegelbilder ohne Typ):** vertretbar.
   - Mit Typ hätten 75 und 76 je drei gleich gebaute Aufgaben auf Stufe 1 ergeben, und das verbietet das Prüfskript.
   - „4² · 25²“ und „2³ · 50³“ sind fast dieselben Aufgaben wie „25² · 4²“ und „50³ · 2³“.
   - Die Zahl der aktiven Übungen bleibt gleich. Nichts wird gelöscht.
2. **Ablenker, die eine Basis verlieren:**
   - „Ein Kind rechnet: 2³ · 5³ = 10⁶“: „Die Exponenten werden addiert, nicht malgenommen: 2⁵“.
   - „… 2⁴ · 5⁴ = 10⁸“: „… nicht malgenommen: 5⁶“.
   - Beide sind falsch, aber leicht auszuschließen, weil eine Basis fehlt. Sie waren nicht Teil von Sollte 3 im ersten Bericht. Ein Ersatz wäre zum Beispiel „Die Basen werden addiert: 7³“ bzw. „7⁴“.
3. **Entscheidung 4 („27 · 3⁵“ jetzt Stufe 2 `darstellung`, die gleich gebauten in `anwenden` Stufe 1):**
   - Die Begründung (Grundform der jeweiligen Karte) trägt, und die Spanne ist von zwei Stufen auf eine geschrumpft.
   - Ganz einheitlich, wie im ersten Bericht verlangt, ist es nicht. „darstellung“ ist laut README der Wechsel zwischen Tabelle, Bild und Term; „Zahl als Potenz schreiben“ ist eher eine Grenzfall-Lesart.
4. **Ersatzaufgabe „2¹⁰ : 2ⁿ = 16“** ist Stufe 3 `rueckwaerts` wie die alte. Sie braucht aber nur einen Schritt (10 − n = 4). Das ist eher Stufe 2 `umkehr`.
5. **Neue Karte, Aufgabe 199** („(2³)² und (2²)³ sind gleich groß“, Antwort Ja): Sie steht als Stufe 3 `begruenden`, während die „Stimmt die Rechnung?“-Aufgaben mit richtiger Rechnung auf Stufe 1 gingen. Sie verlangt aber einen Vergleich mit Begründung, deshalb ist Stufe 3 vertretbar.
6. **Neue Karte, Wort „potenziert“:** Die Erklärung „mit einem Exponenten versehen, also mehrmals mit sich selbst malgenommen“ ist etwas umständlich. Kürzer wäre: „hoch eine Zahl genommen“.
7. **Flug B, Karte `exponent_und_potenz`:** Sie führt „Potenz einer Potenz“ noch als neues Wort ein und erklärt es von Grund auf. In allen drei Schularten steht Flug A jetzt davor. Einstieg und Wörter könnten darauf verweisen („kennst du aus Klasse 7“). Kein Fehler.
8. **Themenliste Flug A, `lehrplan_rs`:** Dort steht nur „Potenzgesetze anwenden, zuerst mit natürlichen Exponenten …“. Ob R7 M7 1 „Potenzen von Potenzen“ ausdrücklich nennt, habe ich nicht geprüft.

## Nicht geprüft

- **Lehrplantexte im Original:** M7 1.2 nur über das Zitat in `inhalte/pruefung/aufbau/klasse6.json`; R7 M7 1 und das IB-Framework gar nicht.
- **Anzeige in der App:** Tabellenbilder der neuen Karte, Lücken.
- **Unveränderte Aufgaben:** nur über das Skript nachgerechnet (115 in Flug A) und über den Dateivergleich als unverändert bestätigt. Die übrigen unveränderten Aufgaben von Flug A und Flug B habe ich in dieser Runde nicht erneut von Hand gerechnet; das hat der erste Prüfbericht getan.
- **Datenbank:** nicht angesehen. Ob dort für die vier alten Lernziele weitere Aufgaben liegen, ist offen, wie im ersten Bericht.

FERTIG: Nachprüfung Potenz
