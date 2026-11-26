# Postfach designer (Designer, Chat des Nutzers)

Neueste oben.

## 2026-11-26 04:30 (Berlin) – FERTIG: Regel-Übersicht „Sonnensystem“ und Regel-Karte (Vorgabe RS-H)

Zweig `designer`, ausgehend von `lernen-app` 9c2d316. Kein App-Code, keine Datenbank, keine Namen, alle Zustände und Orte in den Entwürfen erfunden und so gekennzeichnet.

**Geliefert** (alles unter `inhalte/design/regeln-sonnensystem/`)
- `umsetzung.md`: Vorgabe mit Maßen je Breite, Farben hell und dunkel, Texten wörtlich, Antippen, Laden, Fehler, Bewegung mit „weniger Bewegung“, Daten-Bedarf, Prüfliste (15 Muss, 7 Soll, 4 Kann).
- `entwurf/uebersicht-a.html` – Fassung A „Sonnensystem“: Sonne am Rand, Bahnen, Planeten mit einem Mond je Regel, Werkzeug-Gürtel außen.
- `entwurf/uebersicht-b.html` – Fassung B „Planetenreihe“: Sonne und Planeten an einer Linie, alle Regel-Namen sofort lesbar.
- `entwurf/regel-karte.html` – Karten „Verteilen“ und „Minusklammer“ ganz: Satz, Bild, drei Gewänder, Grenze, Probe zum Antippen, Orte, Hauptknopf.
- `entwurf/wege.html` – die drei Wege (Reisekarte nach oben, nach einem Fehler, neues Thema).
- `bilder/`: 25 Bilder bei 360, 400, 820, 1280 px, hell und dunkel. Quellen der Entwürfe in `entwurf/teile/`, zusammengesetzt mit `entwurf/bauen.py`.
- Bildmotiv für alle 15 Regeln (Abschnitt 6.4).

**Empfehlung:** Fassung A als Seite; die Liste aus B steckt in A hinter der Sonne. Begründung in Abschnitt 1.

**Vorschläge zu den offenen Entscheidungen des Nutzers** (Abschnitt 2)
- Schnitt: fünf Regel-Planeten wie vorgeschlagen, dazu die Erde; die Werkzeuge als „Werkzeug-Gürtel“ statt als sechster Planet.
- Sonne: öffnet die Liste aller 15; darunter freiwillig „Gemischte Fünf“.
- Stand: Kinder sehen ihn, in zwei Zuständen („sitzt“, „in Arbeit“) plus neutral „kommt später“; als Mond-Form, ohne Zahl und Balken.

**Offen**
- Entscheidung des Nutzers: A oder B, und die drei Punkte oben.
- An den Mathe-Profi: (1) „Potenz“ im Planeten „Bruch“ lassen oder zu „Verhältnis“? (2) Ist „kommt später“ als drittes Zeichen in Ordnung? (3) Bitte prüfen: umgestellte Beispiel-Zeilen der Regeln 4 und 5 (gleiche Zahlen, gleicher Aufbau in allen drei Zeilen), Sätze der fünf Arbeitsweisen, Planeten-Sätze, die 15 Sätze „Hier hat … geklemmt“.
- Karten für die übrigen 13 Regeln: Aufbau steht, Inhalte und Bilder fehlen.
- Abschnitt 10 nennt, was der Server neu liefern müsste (Zustand je Regel, Regel zum Fehler, Zwillingszeilen zur Etappe). Das gibt es heute nicht.

**Nicht geprüft**
- Echte Geräte, Finger, Safari und Firefox; Vorleser nur als Text gesetzt.
- Bewegung nur im Code festgelegt, nicht als Film angesehen; Rechenlast auf alten Geräten nicht gemessen.
- Platz des Knopfs „Regeln“ auf der echten Reisekarte (im Entwurf ein Platzhalter).
- Kontrast für Text gerechnet (ab 6,2 : 1), nicht am Bildschirm gemessen.

**Geprüft:** alle vier Entwürfe in Chrome bei 360 × 640, 400 × 860, 820 × 1180, 1280 × 800, hell und dunkel: keine Skriptfehler, Klickfolgen durch alle Blätter und Wege, kein Ziel unter 44 px, keine Rechnung läuft über den Rand.

**Annahmen**
- Drei Aufgaben je Regel und die Gemischte Fünf lassen sich mit vorhandenen Aufgabenformen bauen.
- Die Orte in „Diese Regel brauchst du in …“ kommen aus den Regel-Etiketten des Mathe-Profis.
- Kürzel RS-H gewählt, weil „RS“ im Repo schon belegt ist.

## 2026-11-26 02:40 (Berlin) – AUFTRAG vom Projektleiter: Regel-Übersicht „Sonnensystem“ und Regel-Karte

**Wunsch des Nutzers, wörtlich im Kern:** „Wichtig ist mir eine tolle Übersichtsseite für die Regeln. Schön und übersichtlich, nicht einfach hingeklatscht.“ Die Idee des Sonnensystems stammt von ihm. Kein Bau, keine Einspielung – du lieferst Entwurf und Vorgabe.

**Worum es geht**
Über allen Themen stehen wenige Grundregeln, die immer wiederkehren („immer dasselbe, nur anders dargestellt“; Klasse 5 rechnet mit Zahlen, Klasse 8 mit x – dieselbe Regel). Die Kinder sollen diese Regeln jederzeit ansehen können und spüren: Es sind 15 Dinge, nicht 300 Themen.

**Bildsprache**
Die Reisewelt (Flug, Bordkarte, Stadt, Reisekarte) bleibt. Das Sonnensystem ist keine zweite Welt daneben, sondern der Blick nach oben: Die Reisewelt ist die Erde, die Regeln stehen am Himmel. Diese Erweiterung hat der Nutzer selbst gewollt; sie hebt den Satz „keine zweite Bildsprache erfinden“ für diesen Fall auf. Der Übergang Erde ↔ Himmel ist Teil deiner Aufgabe.

**Inhalt, fachlich vorgegeben** (Quelle: `inhalte/mathe-profi/denkpapier-grundregeln.md` auf `origin/mathe-profi`, Abschnitte 1, 2 und 5 – bitte lesen)
- 15 Regeln mit Namen für Kinder, je ein Satz, die Grenze („gilt nicht bei …“), Beispiel mit Zahlen, mit x, mit Brüchen.
- Vorschlag des Projektleiters für die Gruppen (der Nutzer hat ihn gesehen, aber noch nicht bestätigt):
  - Sonne: Übersicht, „15 Regeln“
  - Erde: die Reisewelt
  - Vorzeichen: Richtung, Zeichen-Paar
  - Klammer: Rangfolge, Verteilen, Minusklammer, Tauschen und Bündeln
  - Waage: Waage, Umkehren, Einsetzen und Probe, Nullprodukt
  - Bruch: Wert bleibt, Bruchrechnen, Potenz
  - Verhältnis: Stellenwert, Verhältnis
  - Werkzeuge (Arbeitsweisen, ohne richtig/falsch): Skizze, Überschlag, Einheiten prüfen, Zerlegen und Ergänzen, Darstellung wechseln
- Regeln des Mathe-Profis für die Anzeige: höchstens zwei Zustände je Regel („sitzt“ / „in Arbeit“), **keine Prozentbalken**, kein dauernd sichtbares „wackelt“ (Beschämung), Zustand nie nur über Farbe.

**Was du lieferst**
1. **Übersichtsseite** in zwei deutlich verschiedenen Fassungen zum Anklicken (je eine HTML-Datei): eine mit echtem Sonnensystem-Gefühl (Bahnen, Tiefe, Bewegung sparsam), eine ruhigere, die am Handy auf einen Blick lesbar ist. Sag, welche du empfiehlst und warum.
2. **Regel-Karte** am Beispiel „Verteilen“ (Regel 4) und „Minusklammer“ (Regel 5): Satz, Bild, dieselbe Regel mit Zahlen / mit x / mit Brüchen, die Grenze, die Probe, „Diese Regel brauchst du in …“, Einstieg zu drei Aufgaben. Das Bild je Regel ist wichtig (bei Verteilen das Rechteck) – schlage für alle 15 Regeln ein Bildmotiv in je einer Zeile vor.
3. **Die drei Wege zur Regel:** (a) von der Reisekarte nach oben, (b) nach einem Fehler in einer Aufgabe der Satz „Hier hat die Minusklammer geklemmt“ mit Sprung zur Karte und zurück zur Aufgabe, (c) beim Einstieg in ein neues Thema „Das kennst du schon“.
4. Vorgabe so genau, dass ein Bau-Helfer sie ohne Rückfrage umsetzt: Maße, Farben hell und dunkel, Texte wörtlich, Verhalten bei 360 / 400 / 820 / 1280 px, Antippen, Laden, Fehler, Bewegung mit „weniger Bewegung“-Fassung. Dazu die Prüfliste (Muss / Soll / Kann).

**Als Inhalts-Skizze, nicht als Aussehen:** Der Projektleiter hat dem Nutzer einen schnellen Rohentwurf gezeigt (dunkler Grund, Sonne oben, sechs Planeten als Karten, Regel-Karte „Verteilen“). Der Nutzer will es schöner. Nimm daraus nur, was inhaltlich auf die Seiten gehört.

**Offene Entscheidungen des Nutzers – bitte je einen Vorschlag mitliefern**
- Schnitt der Planeten: sechs wie oben oder anders.
- Ob in der Sonne etwas zu tun ist (z. B. „gemischte Fünf“ quer über alle Regeln).
- Ob die Kinder den Stand je Regel sehen oder nur der Erwachsene.

**Regeln wie immer:** Zweig `designer`, vorher auf `origin/lernen-app` bringen. Öffentliches Repo: keine Namen, keine Lerndaten. Beispiel-Zustände in den Entwürfen sind erfunden und als erfunden gekennzeichnet. Ablage `inhalte/design/regeln-sonnensystem/`, Meldung hier mit „Nicht geprüft“ und „Annahmen“.

## 2026-11-25 02:00 – FERTIG: Bestandsaufnahme

Zweig `designer`, ausgehend von `lernen-app` 4351182 (App 0.93.4). Vorgaben gelesen auf `pruefung-kinderansicht` ab6a9fb. Kein App-Code, keine Datenbank, keine Namen, nichts Neues entworfen.

**Geliefert**
- `inhalte/design/bestandsaufnahme.md`: Stand der Vorgaben, eigene Befunde mit Messwerten, drei Vorschläge.
- `inhalte/design/bestandsaufnahme/bilder/`: 15 Bilder aus einem eigenen Rundgang (als Kind angemeldet, Testdaten der Suite; 400, 820, 1280 px, hell und dunkel; Übung zusätzlich 390 × 664).
- Kern:
  - Alle Vorgaben des Vorgängers sind gebaut, außer FX (nichts im Code) und den Kann-Punkten K1, K3, K5, K8 der Prüfung KJ.
  - Übung: Bei 390 × 664 und 360 × 640 px ist beim Öffnen keine Aufgabe zu sehen (Bordkarte ab 386 px, Tastenfeld ab 385 bzw. 361 px). Bei 400 × 860 sind die Antwortfelder im unteren Drittel und „Tipp“ ganz verdeckt. Bei 1280 × 800 liegt „Prüfen“ unter dem Fensterrand.
  - Nachts wird die Etappen-Kachel unter dem Zeiger hell mit weißer Schrift; der Chip „Expedition wartet“ bleibt hell. Tablet: Schrift im Landungs-Blatt 11–14 px.
- Vorschlag nach Wirkung je Aufwand: 1. Übungs-Bildschirm „Aufgabe zuerst“ · 2. Aufräum-Paket Lesbarkeit · 3. FX erste Stufe (Motor, Legendary Drop, Respawn, Dezember-Saison).

**Offen**
- Entscheidung des Nutzers, was ich zuerst entwerfe.
- FX: Freigabe („warten“ vom 24.11.); Server-Felder für „Etappe sicher“ und „wieder offen“; Prüfliste ohne Muss / Soll / Kann.
- Im Auftrag steht FX „Fassung 2“, im Repo liegt Fassung 4 vom 24.11. Gelesen habe ich Fassung 4.

**Nicht geprüft**
- Echte Geräte, echter Server, echte Daten; Bewegung und Ton.
- Welt- und Land-Ebene der Karte, Expedition, Check-in, „abgelegt“, Flug geschafft, Flug-Test, Knobel: nur Code, Meldungen und Vorschau-Bilder.
- Lehrer- und Eltern-Ansichten (K6), 360 px außer der Übung (K7).

**Annahmen**
- Kinder melden sich mit eigenem Lern-Code an und sehen „Ändern lassen“ nicht (`ctx.leitung`).
- 390 × 664 steht für ein Handy im Browser mit Leisten; die Geräte der Kinder kenne ich nicht.
- Werkstatt-Regeln W1–W7 nicht im Council nachgelesen: nur eigene Dateien auf eigenem Zweig.

**App-Wunsch (für später, nicht Teil dieser Meldung):** keiner. Die Befunde aus 3.1 und 3.2 der Bestandsaufnahme kommen als Vorgabe, sobald der Nutzer die Reihenfolge festlegt.
