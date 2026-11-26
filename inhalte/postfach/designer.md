# Postfach designer (Designer, Chat des Nutzers)

Neueste oben.

## 2026-11-26 09:05 (Berlin) – RÜCKMELDUNG und AUFTRAG vom Projektleiter: Gesetzbuch, zweite Runde
Vorgabe GB gelesen und die Bilder angesehen (Zeichenstil, Übersicht A, Gesetz aufgeschlagen). Urteil des Projektleiters: Der Zeichenstil „Heft und Tafel“ trifft, was der Nutzer wollte – die Zeichnung zeigt die Regel, dieselbe Zeichnung trägt Zahlen, x und Brüche. Dein eigenes Urteil teile ich: als fertig zeigen wir es erst, wenn die Platzhalter weg sind. Die sechs Zeichnungen und die Gesetz-Seite zeige ich dem Nutzer als Zwischenstand.

Inzwischen neu auf `origin/mathe-profi`: Auftrag 11 (42 Sätze auf Ebene 1: 14 Rechenregeln, 28 tragende Ideen für alle sieben Planeten; 23 Zeichen-Vorgaben für die Sonne und die Planeten Fläche und Raum und Geometrie) und Auftrag 12 (jeder Satz zweizeilig: **Merksatz** oben, **„Genau gesagt“** klein darunter; vier Zeichen-Vorgaben geändert – steht oben in deinem Postfach auf seinem Zweig).

Bitte:
1. Inhalt neu einlesen (`ebene1.md`, `sonne.md`, beide Planeten). Auf jeder Karte der Merksatz groß, „Genau gesagt“ klein darunter.
2. Die fehlenden Zeichnungen nach seinen Vorgaben: 11 Rechenregeln, 5 Ideen Geometrie, Idee 4 Fläche und Raum. Keine Karte mit „Zeichnung folgt“ in Sonne und diesen zwei Planeten.
3. Die tragenden Ideen der übrigen fünf Planeten in die Übersicht aufnehmen (Sätze stehen in `ebene1.md`); dort sind Zeichnungen noch nicht verlangt – die Karten ohne leeren Zeichnungs-Rahmen setzen, bis die Vorgaben kommen.
4. Deine acht Fragen beantwortet der Mathe-Profi (Auftrag 13 in seinem Postfach); wo seine Antwort noch fehlt, triff eine Annahme und nenne sie.
Meldung hier. Danach liest ChatGPT gegen, dann geht es an den Nutzer.

## 2026-11-26 09:05 (Berlin) – FERTIG: Gesetzbuch, Fassung 2 nach den Zeichen-Vorgaben des Mathe-Profis (Vorgabe GB)

Zweig `designer`, Stand `lernen-app` d6752b7 übernommen. Inhalt wörtlich aus `origin/mathe-profi` dc6817d. Kein App-Code, keine Datenbank, kein Lernstand, keine Namen.

**Geliefert** (alles unter `inhalte/design/gesetzbuch/`)
- `umsetzung.md`, neuer Abschnitt **F2** oben: was sich geändert hat, Regeln für alle Zeichnungen, Maße jeder Zeichnung, Antworten an den Mathe-Profi.
- Die sechs Zeichnungen neu nach den Zeichen-Vorgaben: Ausmultiplizieren maßstäblich mit vier Beschriftungen (6 · (20 + 2), 6 · (20 − 2), 3 · (x + 2), ½ · (4 + ⅔)); Waage dreimal mit waagerechtem Balken; zwei Zahlengeraden untereinander, Starts bei 3 übereinander; Auslegen mit Rechteck und Würfel-Quader 5 · 4 · 3; Stammbaum Fläche mit Ästen Drachenviereck und Kreis; Stammbaum Körper mit Kugel im Zylinder. Zusätzlich eine siebte: Quader und Netz („Haut des Körpers“).
- Hervorhebung überall Gelb **mit Rahmen**, dieselbe Markierung in der Rechenzeile; jede Höhe mit Zeichen für den rechten Winkel.
- Beide Übersichten mit den 42 Sätzen aus `ebene1.md`: alle sieben Planeten zeigen ihre tragenden Ideen (28). Zuordnung Gesetz → Idee vom Mathe-Profi.
- Gesetz aufgeschlagen: Voraussetzung, häufiger Fehler, Verwandt, möglicher Erklärweg („keine Sperre“) aus den neuen Dateien. Suche mit den Stichwörtern des Mathe-Profis.
- `entwurf/inhalt_lesen.py` liest das neue Format; `bauen.py` prüft, dass markierte Beispiele wörtlich die des Mathe-Profis sind. 22 Bilder in `bilder/`.

**Antworten an den Mathe-Profi** (ausführlich in `umsetzung.md` F2.4; in seinen Zweig darf ich nicht schreiben)
1. Feste Grundform mit austauschbarer Beschriftung: ja, so gebaut. Aber „dieselbe Form“ und „maßstäblich“ schließen sich bei anderen Zahlen aus – ich habe maßstäblich gewählt. Bitte entscheiden.
2. Originalgröße geht am Bildschirm nicht. Ein Karo steht für 1 cm.
3. Am Handy ist alles lesbar, weil die Felder untereinander stehen. Bitte höchstens vier Felder je Reihe, Nebenzeichnungen als eigene Reihe; „Gleicher Abstand“ als drei getrennte Felder.
4. Vorgaben für die anderen fünf Planeten: später ist recht.

**Offen**
- Entscheidung des Nutzers: Trägt der Zeichenstil? Übersicht A oder B?
- 7 von 23 Zeichen-Vorgaben sind gezeichnet. Es fehlen 11 Rechenregeln und 5 Ideen der Geometrie; dort steht „Zeichnung folgt“ mit dem Text der Vorgabe.
- Auftrag 12 (Merksatz + „Genau gesagt“) ist noch nicht geliefert. Der Entwurf zeigt die zweite Zeile, sobald sie da ist; die Sätze ändern sich also noch.
- Einige Varianten aus den Vorgaben fehlen (Liste in F2.5). Die Abschnitte 1, 2, 5, 9, 11 der `umsetzung.md` beschreiben in Einzelheiten noch Fassung 1.

**Nicht geprüft**
- Ob ein Erwachsener ohne Vorwissen die Seite in einer Minute versteht – das kann nur der Nutzer sagen.
- Echte Geräte, Safari, Firefox. Gemessen nur in Chrome bei 360, 400, 820, 1280 px, hell und dunkel: 112 Seitenaufrufe, kein Querrollen, keine Schrift unter 13 px, keine Skriptfehler.
- Kontrastwerte nicht nachgerechnet. Mathematische Richtigkeit der Zeichnungen nicht vom Mathe-Profi gegengelesen (Kreis-Umlegung, Schrägbilder, Kugel im Zylinder sind von mir konstruiert).

**Annahmen**
- Trapez und Drachenviereck tragen die Zahlen aus den Beispielen F7 und F8, weil die Zeichen-Vorgabe keine nennt.
- Die grauen Sätze unter den Bildern sind von mir.
- Bei 3 · (x + 2) ist x viermal so lang wie 2 gezeichnet.

## 2026-11-26 08:50 (Berlin) – FERTIG: Gesetzbuch der Mathematik – Zeichenstil, Übersicht, ein Gesetz aufgeschlagen (Vorgabe GB)

Zweig `designer`, ausgehend von `lernen-app` 01b103d. Kein App-Code, keine Datenbank, kein Lernstand, keine Namen. Mathe-Inhalt wörtlich aus `origin/mathe-profi` df14ade; der Designer hat keinen Mathe-Inhalt erfunden.

**Geliefert** (alles unter `inhalte/design/gesetzbuch/`)
- `umsetzung.md`: Vorgabe mit Zeichenstil, Maßen je Breite, Farben hell und dunkel, Texten, Verhalten, Prüfliste (14 Muss, 5 Soll, 3 Kann).
- `entwurf/zeichnungen.html`: Zeichenstil „Heft und Tafel“ an den sechs verlangten Zeichnungen (Ausmultiplizieren mit drei Beschriftungen, Waage, Zahlenstrahl, Auslegen und Zählen, Rechteck → Parallelogramm → Dreieck → Trapez, Quader → Prisma und Zylinder → Pyramide und Kegel).
- `entwurf/uebersicht-a.html`: Übersicht A „Schnitt von innen nach außen“ – die Sonne als vier Schichten mit allen 14 Merksätzen, darunter die sieben Planeten mit ihren tragenden Ideen, dann die acht Arbeitsweisen.
- `entwurf/uebersicht-b.html`: Übersicht B „Durch die Klassen“ – jede Regel als Zeile von Klasse 5 bis 10 mit ihrem Beispiel in jeder Klasse.
- `entwurf/gesetz.html`: ein Gesetz aufgeschlagen (Regel 6): Merksatz, Zeichnung, dieselbe Regel in sechs Klassen mit gelber Wirkstelle, wo es nicht gilt, Voraussetzung. Dazu der Weg Idee → Gesetze dahinter und die Suche über alle 174 Einträge („Kegelmantel“ → „Pyramide und Kegel“).
- `bilder/`: 20 Bilder bei 360, 400, 820, 1280 px, hell und dunkel. Quellen in `entwurf/teile/`; `inhalt_lesen.py` liest den Inhalt des Mathe-Profis, `bauen.py` setzt die Seiten zusammen.

**Empfehlung:** Übersicht A als Seite; die Tabelle aus B als zweite Ansicht am Rechner. Begründung in Abschnitt 3.3.

**Mein Urteil in einem Satz:** Ich halte Zeichenstil, Übersicht A und die Gesetz-Seite für gut, weil die Merksätze selbst groß dastehen, der Aufbau eine einzige Leserichtung hat und „dieselbe Regel in vielen Klassen“ an echten Rechnungen zu sehen ist – ich bin aber nicht einverstanden, es dem Nutzer als fertig zu zeigen, solange 11 von 14 Regeln und die fünf Geometrie-Ideen „Zeichnung folgt“ zeigen.

**Offen**
- Für die erste Lieferung fehlen noch: Zeichnungen zu den fünf Geometrie-Ideen und zu 11 Rechenregeln; tragende Ideen für fünf Planeten (Zahlen, Algebra, Geld und Verhältnisse, Funktionen, Daten und Zufall). Im Entwurf steht an diesen Stellen „folgt“.
- Entscheidung des Nutzers: A oder B.
- **An den Mathe-Profi – acht Fragen in Abschnitt 11 der Vorgabe**, die wichtigsten: (1) Zahlen-Feld der Zeichnung 1 mit Minus wie im Auftrag oder mit Plus, damit alle drei Felder gleich sind? (3) Zuordnung der Gesetze zu den Ideen bestätigen. (4) Zwei Beispiele je Klasse bitte als zwei Einträge, nicht mit „ · “ getrennt. (5) Mantel und Oberfläche als eigene Einträge, wenn die Suche Formeln finden soll. (6) Schicht 1 und Planet 1 heißen beide „Zahlen“. (7) Wirkstelle je Regel festlegen. (8) Was genau die fünf Geometrie-Zeichnungen zeigen müssen.

**Nicht geprüft**
- Der Maßstab „ein Erwachsener versteht es in einer Minute“: mit niemandem erprobt.
- Fachliche Richtigkeit der Zeichnungen durch den Mathe-Profi; seine genauen Vorgaben je Zeichnung lagen noch nicht vor.
- Echte Geräte, Finger, Safari und Firefox; Vorleser nur als Text gesetzt; Kontrast nicht gemessen.
- Gegenlesen durch ChatGPT.

**Geprüft:** alle vier Entwürfe in Chrome bei 360 × 640, 400 × 860, 820 × 1180, 1280 × 800, hell und dunkel: keine Skriptfehler, 14 Regeln und 7 Planeten auf beiden Übersichten, Klickfolgen durch Gesetz, Idee und Suche, sieben Suchwörter, nichts ragt seitlich hinaus, keine Tippfläche unter 44 px. Alle Zahlen in den Zeichnungen nachgerechnet.

**Annahmen**
- Welche Gesetze hinter welcher Idee stehen, habe ich zugeordnet (Fläche und Raum: 3 / 8 / 8; Geometrie nach den vier Abschnitten).
- Die fünf Geometrie-Sätze sind der Vorschlag des Projektleiters, formuliert mit den Sätzen der Gesetze G6, G10, G15, G20, G24.
- Der Inhalt wird als feste Datei mit der App ausgeliefert; dann braucht die Seite keinen Ladezustand.
- Die Vorgabe RS-H ist als abgelehnt gekennzeichnet; ihre Dateien bleiben nur zum Nachlesen im Zweig `designer`.

## 2026-11-26 08:40 (Berlin) – AUFTRAG vom Projektleiter: Gesetzbuch der Mathematik – Zeichnungen und Übersicht (jetzt, gleichzeitig mit dem Mathe-Profi)
Der Nutzer will dich ausdrücklich dabeihaben und erwartet echte Zeichnungen. Bitte lies `inhalte/plan/regeln-uebersicht-auftrag.md` ganz; **der letzte Abschnitt ist maßgeblich** (zwei Ebenen). Die frühere Vorgabe RS-H ist abgelehnt.

**Die Idee:** Ein „Gesetzbuch“ neben der Lernreise – in der Mitte die Sonne mit 14 Rechenregeln, darum sieben Planeten (die Gebiete der App), je Planet 3 bis 5 tragende Ideen; dahinter zum Nachschlagen die einzelnen Formeln.

**Abgelehnt wurde:** Etiketten statt Inhalt, erfundene Namen, Lernstand im Mittelpunkt, Seiten, die man erst durch Antippen versteht. **Gewünscht ist:** übersichtlich der gesamte Aufbau; sichtbar, dass dieselbe Regel in vielen Klassen gilt; sehr anschaulich; aufeinander aufbauend; einprägsame Bilder.

**Deine Aufgabe**
1. **Zeichenstil festlegen** und an sechs Zeichnungen zeigen – jede zeigt die Idee, keine schmückt:
   - Ausmultiplizieren: ein zerlegtes Rechteck – dieselbe Zeichnung beschriftet mit 6 · (20 − 2), mit 3 · (x + 2) und mit Brüchen.
   - Gleichung als Waage.
   - Plus und Minus mit negativen Zahlen am Zahlenstrahl (zweimal von 3 aus: 3 + (−2) = 1 und 3 − (−2) = 5).
   - „Messen heißt auslegen und zählen“: Rechteck 6 cm mal 4 cm mit Einheitsquadraten.
   - „Aus dem Rechteck entsteht jede Fläche“: Stammbaum Rechteck → Parallelogramm → Dreieck → Trapez.
   - „Aus dem Quader entsteht jeder Körper“: Quader → Prisma und Zylinder → Pyramide und Kegel.
   Genaue Vorgaben je Zeichnung liefert der Mathe-Profi; bis dahin gelten die Abschnitte „Bild“ in `sonne.md` und `planet-flaeche-und-raum.md` auf `origin/mathe-profi`.
2. **Die Übersicht (Ebene 1)** in zwei Fassungen: Sonne und sieben Planeten, auf denen die Merksätze selbst lesbar stehen. Ein Erwachsener ohne Vorwissen muss nach einer Minute sagen können, was die Seite ihm sagt. Rechner und Handy; ohne Antippen verständlich.
3. **Ein Gesetz aufgeschlagen:** Merksatz, Zeichnung, dieselbe Regel in mehreren Klassen mit gleich hervorgehobener Wirkstelle, Voraussetzung, häufiger Fehler. Dazu der Weg von einer tragenden Idee zu den Formeln dahinter und eine Suche (z. B. „Kegelmantel“).
4. Kein Lernstand, keine Monde, keine Prozentbalken in dieser Fassung.

**Abstimmung:** Der Mathe-Profi arbeitet gleichzeitig (Auftrag 11) und schreibt Fragen und Antworten an dich hier oben hinein. Erste gemeinsame Lieferung: Sonne und zwei Planeten (Fläche und Raum, Geometrie). Ablage `inhalte/design/gesetzbuch/`, Meldung hier mit „Nicht geprüft“ und „Annahmen“.

## 2026-11-26 05:40 (Berlin) – RÜCKMELDUNG und neuer AUFTRAG vom Projektleiter: Regel-Übersicht
Der Nutzer hat die Vorgabe RS-H abgelehnt („Katastrophal. Verstehe nicht einmal ich, was ihr mir sagen wollt“) und ebenso meinen eigenen Gegenentwurf. Die Ursache liegt vor allem im Inhalt, den ich dir gegeben habe (erfundene Namen, Lernstand im Mittelpunkt), nicht in deinem Handwerk. Der gemeinsame Auftrag steht in `inhalte/plan/regeln-uebersicht-auftrag.md` – bitte ganz lesen. **Du bist erst in Schritt 4 dran**, wenn Mathe-Profi und ChatGPT den Inhalt abgestimmt haben; ich melde mich dann hier. Bis dahin nichts bauen. Wenn du vorab Bedenken oder Ideen zur Darstellung „dieselbe Regel in vielen Klassen, aufeinander aufbauend“ hast: kurz hier notieren.

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

