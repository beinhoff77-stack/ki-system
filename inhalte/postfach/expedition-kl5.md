# Postfach expedition-kl5 (Expeditionen Klasse 5, Werkstatt-Wunsch 176)

Neueste Meldung oben.

## 2026-11-20 01:28 – FERTIG: Korrekturen 853

Stand von lernen-app vorher in expedition-kl5 geholt (Merge von origin/lernen-app, ohne Konflikte). Geändert nur die vier genannten Expeditionen und ihre Generatoren; JSON neu erzeugt, Dateien und Generatoren stimmen überein. `python3 -I tools/inhalt_pruefen.py --alle`: keine Fehler (nur die bekannten Hinweise zu Lernkarten anderer Themen).

- Fakt: Alle Rechnungen und Lösungen sind gleich geblieben (24 Outfits, 20 Dollar, 12 Codes, 213 km 120 m, 289, 2 300 000 usw.).
- Fakt, eine Abweichung von „nur Texte“: `5-flug_toronto` Teil d ist jetzt eine Auswahl statt einer Zahl-Eingabe, weil die Frage jetzt eine Entscheidung verlangt (Schafft ihr die Wäscherei noch?) und den Preis. Die Rechnung (12 : 3 · 5 = 20 Dollar) ist unverändert, der Generator prüft beide Teile der richtigen Antwort und dass die vier Antworten verschieden sind.

### 1. 5-flug_toronto (Muss): durchgehender Zusammenhang, Zeitverschiebung als Annahme

**Einleitung** – alt: „Deine Familie fliegt von Berlin nach Toronto. Du kümmerst dich um die Uhrzeiten, um deinen Koffer und um die Wäsche. Im Flugzeug sind 23 kg Gepäck erlaubt.“
neu: „Deine Familie fliegt von Berlin nach Toronto. Du planst den Reisetag: Wann landet ihr, wann seid ihr im Hotel, schafft ihr es noch zur Wäscherei – und passt am Ende alles wieder in den Koffer? Im Flugzeug sind 23 kg Gepäck erlaubt.“

**Teil b** – alt: „In Toronto gehen die Uhren anders: Toronto-Zeit = Berliner Zeit + (−6 h). In Berlin ist es 19:55 Uhr. Wie spät ist es in Toronto?“
neu: „In Toronto gehen die Uhren anders. Für diesen Reisetag gilt (Annahme): Toronto-Zeit = Berliner Zeit + (−6 h), also 6 Stunden weniger. In Berlin ist es bei der Landung 19:55 Uhr. Wie spät ist es in Toronto?“

**Teil d** – alt: „Im Hotel in Toronto kostet das Waschen von 3 kg Wäsche 12 Dollar. Was kostet das Waschen von 5 kg?“
neu: „Ihr landet um 13:55 Uhr Toronto-Zeit. Die Fahrt zum Hotel dauert 1 h 30 min. Die Hotelwäscherei nimmt nur bis 16:00 Uhr Wäsche an; 3 kg Wäsche kosten dort 12 Dollar. Ihr wollt noch heute 5 kg Wäsche abgeben. Schafft ihr das, und was kostet es?“
Antwortform alt: Zahl (20 Dollar); neu: Auswahl – „Ja: Ihr seid um 15:25 Uhr im Hotel, das Waschen kostet 20 Dollar.“ / „Nein: Ihr seid erst um 16:25 Uhr im Hotel.“ / „Ja: Ihr seid um 15:25 Uhr im Hotel, das Waschen kostet 60 Dollar.“ / „Ja: Ihr seid um 15:25 Uhr im Hotel, das Waschen kostet 14 Dollar.“ (richtig: „Ja: Ihr seid um 15:25 Uhr im Hotel, das Waschen kostet 20 Dollar.“). Lösungsweg neu: Ankunft im Hotel: 13:55 Uhr + 1 h 30 min = 15:25 Uhr – vor 16:00 Uhr. 1 kg kostet 12 : 3 = 4 Dollar, 5 kg kosten 5 · 4 = 20 Dollar.

**Teil e** – alt: „Am Rückflug wiegt der Koffer 25 kg 300 g, erlaubt sind 23 kg. Du kannst herausnehmen: Schuhe (1 kg 200 g), Hose (900 g), Pullover (600 g), Buch (500 g). Du willst so wenig Gewicht wie möglich herausnehmen. Was nimmst du heraus?“
neu: „Nach der Reise wiegt der Koffer mit der gewaschenen Wäsche und den Andenken für den Rückflug 25 kg 300 g, erlaubt sind 23 kg. Du kannst herausnehmen: Schuhe (1 kg 200 g), Hose (900 g), Pullover (600 g), Buch (500 g). Du willst so wenig Gewicht wie möglich herausnehmen. Was nimmst du heraus?“

Zusammenhang jetzt: Teil d braucht die Landezeit aus Teil b (13:55 Uhr Toronto-Zeit, im Text genannt) und entscheidet, ob die Wäscherei noch erreicht wird; Teil e knüpft an die gewaschene Wäsche an. Jeder Teil nennt seine Zahlen selbst, kein Folgefehler.

### 2. 5-schatzsuche (Muss): 9er-Regel ausdrücklich

**Teil d** – alt: „Auf einem Zettel steht: „Der Code ist durch 9 teilbar.“ Wie viele dreistellige Codes aus drei verschiedenen Ziffern von 1 bis 5 sind durch 9 teilbar?“
neu: „Auf einem Zettel steht: „Der Code ist durch 9 teilbar.“ Dazu gibt es eine Regel: Eine Zahl ist durch 9 teilbar, wenn ihre Quersumme durch 9 teilbar ist. Wie viele dreistellige Codes aus drei verschiedenen Ziffern von 1 bis 5 sind durch 9 teilbar?“

### 3. 5-roemerstrasse (Sollte): 144 Meilen = Strecke ab Meile 0

**Teil b** – alt: „Eine römische Meile ist etwa 1 480 m lang. Wie lang sind 144 Meilen? Gib das Ergebnis in km und m an.“
neu: „Der Meilenstein zeigt, wie weit diese Stelle vom Anfang der Straße (Meile 0) entfernt ist – gewandert bist du selbst nur ein kurzes Stück. Eine römische Meile ist etwa 1 480 m lang. Wie weit ist es von Meile 0 bis zu diesem Stein? Gib das Ergebnis in km und m an.“

### 4. 5-pyramide (Sollte): Übergang vom Modell zur großen Pyramide

**Teil a** – alt: „Eine große Modellpyramide hat unten eine Schicht aus 17 · 17 Würfeln. Wie viele Würfel sind das (17²)?“
neu: „Neben deinem kleinen Modell steht im Museum ein großes Modell aus denselben Holzwürfeln. Es hat unten eine Schicht aus 17 · 17 Würfeln. Wie viele Würfel sind das (17²)?“

**Teil c** – alt: „Eine erfundene Riesenpyramide hätte 2 347 819 Steine. Runde diese Zahl auf Hunderttausender.“
neu: „Die echten Pyramiden sind nicht aus Holzwürfeln, sondern aus riesigen Steinblöcken gebaut – und haben viel mehr Schichten als jedes Modell. Eine erfundene Riesenpyramide hätte 2 347 819 Steine. Runde diese Zahl auf Hunderttausender.“


## 2026-11-18 04:55 – FERTIG: Expeditionen Klasse 5

### Kurz
- 10 Expeditionen in `inhalte/expeditionen/5-*.json`, je ein Generator `inhalte/generatoren/expedition_<name>.py`; gemeinsame Bausteine in `_expedition_kl5.py`. Eine Expedition = ein Commit auf `expedition-kl5`.
- `tools/inhalt_pruefen.py` meldet für alle 10 Dateien OK. Alle Lösungen rechnet der Generator (Fraction), jede Zahl- und Lückenlösung prüft er zusätzlich mit dem Rechner des Prüfskripts. Bei „wie viele / höchstens / mindestens / so wenig wie möglich“ geht der Generator alle Fälle durch und bricht ab, wenn die Lösung nicht eindeutig ist (z. B. Koffer: alle Teilmengen der Sachen; Schatzsuche: alle 60 Codes; Abstände: nur Punkte auf derselben Gitterlinie, damit kein Satz des Pythagoras nötig ist).
- Zusatzregeln Klasse 5: keine Buchstaben als Unbekannte (auch nicht in der Gleichung beim Aquarium: dort „3 · □ + 41 = 59“); Punkte heißen Z, B, P, F, S wie auf einer Karte. Keine Zählweise „k. Strich“; der Zahlenstrahl der Römerstraße fragt nach dem Pfeil, der Lösungsweg sagt „5 Abschnitte nach der 0“.
- Reihenfolge 1–5 (und 6) nur mit früh liegenden Themen (Rom, Kairo, Timbuktu, Athen, Toronto); 7–10 nutzen auch Kombinatorik, Gleichungen, Dreisatz, Flächen und Quader.
- Kein Folgefehler-Domino: Jeder Teil nennt die Werte, die er braucht (z. B. Aquarium d nennt die 9 000 cm², Schatzsuche e die 12 Codes).

### Übersicht

| Nr. | Expedition | Situation | Teile (Thema/Lernkarte) | Antwortformen | Grafik |
|---|---|---|---|---|---|
| 1 | Die Wetterstation (`5-wetterstation`) | Wetterstation in den Bergen: Tiefstwerte einer Woche | a) zahlen.ganz/ordnen · b) zahlen.ganz/sach · c) zahlen.rechengesetze/geteilt_ganz · d) groessen.einheiten/zeit | Auswahl, Zahl, Lücken | a) tabelle |
| 2 | Die Römerstraße (`5-roemerstrasse`) | Wanderung auf einer Römerstraße bei Rom | a) zahlen.natuerlich/roemisch_system · b) groessen.einheiten/laenge · c) zahlen.natuerlich/strahl_ablesen · d) zahlen.teilbarkeit/vielfache | Zahl, Lücken | c) zahlenstrahl |
| 3 | In der Oase (`5-oase`) | Wüstentour bei Kairo mit Karte im Koordinatensystem | a) geometrie.grundbegriffe/koordinaten · b) groessen.einheiten/massstab · c) geometrie.winkel/drehungen · d) geometrie.ortslinien/kreislinie · e) geometrie.ortslinien/zwei_kreise | Lücken, Zahl, Auswahl | a) koordinaten |
| 4 | Der Uhrturm (`5-uhrturm`) | Uhrturm in Timbuktu mit Glocke und Lampe | a) geometrie.winkel/uhr · b) groessen.einheiten/zeit · c) zahlen.teilbarkeit/vielfache · d) geometrie.winkel/uhr | Zahl, Lücken, Auswahl | – |
| 5 | Die Stufenpyramide (`5-pyramide`) | Stufenpyramide aus Holzwürfeln im Museum | a) zahlen.potenzen_basis/quadrat · b) zahlen.rechengesetze/vorteil · c) zahlen.natuerlich/runden_regel · d) zahlen.potenzen_basis/zehner · e) zahlen.rechengesetze/schriftlich | Zahl, Auswahl | a) tabelle |
| 6 | Die Kettennachricht (`5-kettennachricht`) | Foto wird im Reise-Chat weitergeleitet | a) zahlen.potenzen_basis/schreibweise · b) zahlen.potenzen_basis/berechnen · c) zahlen.natuerlich/ziffern_zu_zahlwort · d) groessen.einheiten/zeit · e) zahlen.natuerlich/vergleichen | Auswahl, Zahl, Lücken | a) tabelle |
| 7 | Flug nach Toronto (`5-flug_toronto`) | Flug Berlin–Toronto: Uhrzeiten, Koffer, Wäsche | a) groessen.einheiten/zeit · b) zahlen.ganz/sach · c) stochastik.kombinatorik/zaehlprinzip · d) groessen.proportional/dreisatz · e) groessen.einheiten/masse | Lücken, Zahl, Auswahl | – |
| 8 | Der Zeltplatz (`5-zeltplatz`) | Zeltplatz mit Plan im Koordinatensystem | a) geometrie.grundbegriffe/koordinaten · b) messen.flaechen/rechteck · c) groessen.proportional/dreisatz · d) geometrie.ortslinien/kreislinie · e) geometrie.ortslinien/parallelen | Lücken, Zahl, Auswahl | a) koordinaten |
| 9 | Die Schatzsuche (`5-schatzsuche`) | Schatzkarte und Zahlenschloss auf einer Insel | a) geometrie.grundbegriffe/koordinaten · b) geometrie.winkel/drehungen · c) stochastik.kombinatorik/reihenfolgen · d) zahlen.teilbarkeit/neunerregel · e) groessen.einheiten/zeit | Lücken, Auswahl, Zahl | a) koordinaten |
| 10 | Das Aquarium (`5-aquarium`) | Aquarium planen im Zoogeschäft | a) messen.koerper_berechnung/quader · b) messen.koerper_berechnung/sachaufgaben · c) gleichungen.einfach/aufstellen · d) groessen.proportional/einheit | Zahl, Auswahl | – |

### Themenmischung (in wie vielen Expeditionen)

- groessen.einheiten: 7 (Nr. 1, 2, 3, 4, 6, 7, 9)
- zahlen.natuerlich: 3 (Nr. 2, 5, 6)
- zahlen.teilbarkeit: 3 (Nr. 2, 4, 9)
- geometrie.grundbegriffe: 3 (Nr. 3, 8, 9)
- geometrie.winkel: 3 (Nr. 3, 4, 9)
- groessen.proportional: 3 (Nr. 7, 8, 10)
- zahlen.ganz: 2 (Nr. 1, 7)
- zahlen.rechengesetze: 2 (Nr. 1, 5)
- geometrie.ortslinien: 2 (Nr. 3, 8)
- zahlen.potenzen_basis: 2 (Nr. 5, 6)
- stochastik.kombinatorik: 2 (Nr. 7, 9)
- messen.flaechen: 1 (Nr. 8)
- messen.koerper_berechnung: 1 (Nr. 10)
- gleichungen.einfach: 1 (Nr. 10)
- Fakt: Jedes früh liegende Thema (natuerlich, ganz, rechengesetze, potenzen_basis, grundbegriffe, ortslinien, winkel, teilbarkeit, einheiten) kommt mindestens zweimal vor. groessen.einheiten kommt siebenmal vor (Zeit, Länge, Masse, Maßstab) – Meinung: passt, weil Größen in fast jeder Sachsituation stecken.

### Je Expedition ein Teil im Wortlaut

1. **Die Wetterstation d)** „Am Mittwoch um 6:40 Uhr misst die Station −9 °C. Danach wird es jede Stunde gleichmäßig 3 Grad wärmer. Eine Wandergruppe will erst losgehen, wenn das Thermometer 0 °C erreicht. Um wie viel Uhr ist das frühestens?“ → **9 / 40**. Lösungsweg: Bis 0 °C fehlen 9 Grad. Bei 3 Grad pro Stunde dauert das 9 : 3 = 3 Stunden. 6:40 Uhr + 3 h = 9:40 Uhr.
2. **Die Römerstraße d)** „Ab Meile 0 steht alle 12 Meilen ein Brunnen und alle 18 Meilen ein Wachposten. Du willst die erste Nacht an einer Stelle verbringen, an der es beides gibt – aber nicht schon bei Meile 0. Bei welcher Meile ist das?“ → **36**. Lösungsweg: Brunnen: 12, 24, 36, 48, … Wachposten: 18, 36, 54, … Die erste Zahl in beiden Listen ist 36.
3. **In der Oase e)** „Dein Funkgerät am Zelt reicht 500 m weit, das Funkgerät am Brunnen ebenfalls 500 m. Zelt und Brunnen sind 800 m voneinander entfernt. Auf dem geraden Weg zwischen ihnen: Wie lang ist das Stück, auf dem man beide Funkgeräte empfängt?“ → **200 m**. Lösungsweg: Gemessen vom Zelt: Das Zelt-Funkgerät reicht von 0 m bis 500 m. Das Brunnen-Funkgerät reicht vom Brunnen 500 m zurück, also ab 800 − 500 = 300 m. Beide gibt es zwischen 300 m und 500 m: 500 − 300 = 200 m.
4. **Der Uhrturm d)** „Für ein Foto sollen die beiden Zeiger genau einen rechten Winkel bilden. Welche Uhrzeit passt?“ → **3:00 Uhr**. Lösungsweg: Um 3:00 Uhr: 3 Abstände · 30° = 90°. Um halb steht der Stundenzeiger schon in der Mitte zwischen zwei Zahlen (15° weiter): 3:30 Uhr ergibt 75°, 9:30 Uhr 105°. Um 6:15 Uhr steht der Stundenzeiger ein Viertel hinter der 6 (7,5°), es sind 97,5°.
5. **Die Stufenpyramide e)** „Ein Bautrupp setzt jeden Tag 300 Steine, ein Jahr hat 365 Tage. Reichen 20 Jahre für 2 300 000 Steine?“ → **Nein, es fehlen 110 000 Steine.**. Lösungsweg: 300 · 365 = 109 500 Steine im Jahr. · 20 = 2 190 000 Steine. Das ist weniger als 2 300 000: Es fehlen 2 300 000 − 2 190 000 = 110 000 Steine. Die Zeit reicht nicht.
6. **Die Kettennachricht e)** „Eine Stadt hat 600 000 Einwohner. In Runde 12 bekommen 531 441 Personen das Foto, in Runde 13 wären es 1 594 323. Kann die Kettennachricht bis Runde 13 weiterlaufen, wenn nur Menschen aus dieser Stadt mitmachen?“ → **Nein: In Runde 13 bräuchte man 1 594 323 neue Personen – mehr, als die Stadt Einwohner hat.**. Lösungsweg: 1 594 323 hat sieben Stellen, 600 000 nur sechs: 1 594 323 > 600 000. Allein in Runde 13 bräuchte man mehr neue Personen, als die Stadt Einwohner hat – die Kette muss vorher abbrechen.
7. **Flug nach Toronto e)** „Am Rückflug wiegt der Koffer 25 kg 300 g, erlaubt sind 23 kg. Du kannst herausnehmen: Schuhe (1 kg 200 g), Hose (900 g), Pullover (600 g), Buch (500 g). Du willst so wenig Gewicht wie möglich herausnehmen. Was nimmst du heraus?“ → **Schuhe, Pullover und Buch**. Lösungsweg: Herausnehmen musst du mindestens 25 300 g − 23 000 g = 2 300 g. Schuhe und Hose: 2 100 g – zu wenig. Hose und Pullover: 1 500 g – zu wenig. Schuhe, Hose und Buch: 2 600 g – reicht, ist aber mehr als nötig. Schuhe, Pullover und Buch: 1 200 g + 600 g + 500 g = 2 300 g – genau so viel wie nötig.
8. **Der Zeltplatz e)** „Am unteren Rand (auf der x-Achse) fließt ein Bach. Zelte brauchen mindestens 20 m Abstand zum Bach und mindestens 30 m zur Feuerstelle F (6 | 3). Welcher Platz erfüllt beide Regeln?“ → **(1 | 3)**. Lösungsweg: Abstand zum Bach = y-Koordinate · 10 m. 20 m Abstand heißt: y mindestens 2 – alle Punkte auf oder über der Parallelen y = 2. (2 | 1) und (6 | 0) liegen zu nah am Bach. (4 | 3) ist nur 2 Kästchen (20 m) von F entfernt. (1 | 3) liegt 30 m vom Bach und 5 Kästchen (50 m) von F entfernt – beides erfüllt.
9. **Die Schatzsuche d)** „Auf einem Zettel steht: „Der Code ist durch 9 teilbar.“ Wie viele dreistellige Codes aus drei verschiedenen Ziffern von 1 bis 5 sind durch 9 teilbar?“ → **12**. Lösungsweg: Durch 9 teilbar heißt: Die Quersumme ist durch 9 teilbar. Drei verschiedene Ziffern von 1 bis 5 ergeben höchstens 5 + 4 + 3 = 12, also muss die Quersumme 9 sein. Das geht nur mit 1, 3, 5 oder mit 2, 3, 4. Jede dieser Gruppen kann man auf 3 · 2 · 1 = 6 Arten anordnen: 2 · 6 = 12 Codes (z. B. 135, 153, …, 234, 243, …).
10. **Das Aquarium c)** „Für 3 gleich teure Wasserpflanzen und eine Pumpe für 41 € zahlst du zusammen 59 €. Wie viel kostet eine Pflanze?“ → **6 €**. Lösungsweg: Gleichung: 3 · □ + 41 = 59. Rückwärts: 59 − 41 = 18, dann 18 : 3 = 6. Eine Pflanze kostet 6 €. Probe: 3 · 6 + 41 = 59.

### Nicht geprüft / offen
- Nicht geprüft: wie die App die Grafiken zeichnet (Tabelle, Koordinatensystem mit Punkten und Rechteck, Zahlenstrahl mit Pfeil) und ob die Lücken-Schablonen „□:□ Uhr“, „(□ | □)“, „□ km □ m“, „□ h □ min“ gut eintippbar sind; das Format gibt es in Bordkarten schon.
- Nicht geprüft: ob die Reihenfolge der Expeditionen in der App überhaupt eine Rolle spielt (die Datei hat kein Feld für eine Reihenfolge; Nr. 1–10 oben ist meine Zählung).
- Annahme: „Toronto liegt 6 Stunden hinter Berlin“ gilt für den größten Teil des Jahres (Toronto UTC−5/−4, Berlin UTC+1/+2); in den wenigen Wochen, in denen nur eine Seite die Uhr umstellt, sind es 5 Stunden. Die Aufgabe nennt die −6 h ausdrücklich, das Kind rechnet nur damit.
- Annahme: Die Länge der römischen Meile (1 480 m) ist als „etwa“ angegeben; sie dient nur als Rechenwert.
- Kein Merge, keine Datenbank-, App- oder Server-Änderung.

## 2026-11-18 04:54 – STATUS: Expedition 10 „Das Aquarium“ (5-aquarium) fertig
4 Teile, Themen: gleichungen.einfach, groessen.proportional, messen.koerper_berechnung. Prüfskript OK, alle Lösungen vom Generator berechnet und nachgerechnet.

## 2026-11-18 04:54 – STATUS: Expedition 9 „Die Schatzsuche“ (5-schatzsuche) fertig
5 Teile, Themen: geometrie.grundbegriffe, geometrie.winkel, groessen.einheiten, stochastik.kombinatorik, zahlen.teilbarkeit. Prüfskript OK, alle Lösungen vom Generator berechnet und nachgerechnet.

## 2026-11-18 04:54 – STATUS: Expedition 8 „Der Zeltplatz“ (5-zeltplatz) fertig
5 Teile, Themen: geometrie.grundbegriffe, geometrie.ortslinien, groessen.proportional, messen.flaechen. Prüfskript OK, alle Lösungen vom Generator berechnet und nachgerechnet.

## 2026-11-18 04:54 – STATUS: Expedition 7 „Flug nach Toronto“ (5-flug_toronto) fertig
5 Teile, Themen: groessen.einheiten, groessen.proportional, stochastik.kombinatorik, zahlen.ganz. Prüfskript OK, alle Lösungen vom Generator berechnet und nachgerechnet.

## 2026-11-18 04:54 – STATUS: Expedition 6 „Die Kettennachricht“ (5-kettennachricht) fertig
5 Teile, Themen: groessen.einheiten, zahlen.natuerlich, zahlen.potenzen_basis. Prüfskript OK, alle Lösungen vom Generator berechnet und nachgerechnet.

## 2026-11-18 04:54 – STATUS: Expedition 5 „Die Stufenpyramide“ (5-pyramide) fertig
5 Teile, Themen: zahlen.natuerlich, zahlen.potenzen_basis, zahlen.rechengesetze. Prüfskript OK, alle Lösungen vom Generator berechnet und nachgerechnet.

## 2026-11-18 04:54 – STATUS: Expedition 4 „Der Uhrturm“ (5-uhrturm) fertig
4 Teile, Themen: geometrie.winkel, groessen.einheiten, zahlen.teilbarkeit. Prüfskript OK, alle Lösungen vom Generator berechnet und nachgerechnet.

## 2026-11-18 04:54 – STATUS: Expedition 3 „In der Oase“ (5-oase) fertig
5 Teile, Themen: geometrie.grundbegriffe, geometrie.ortslinien, geometrie.winkel, groessen.einheiten. Prüfskript OK, alle Lösungen vom Generator berechnet und nachgerechnet.

## 2026-11-18 04:54 – STATUS: Expedition 2 „Die Römerstraße“ (5-roemerstrasse) fertig
4 Teile, Themen: groessen.einheiten, zahlen.natuerlich, zahlen.teilbarkeit. Prüfskript OK, alle Lösungen vom Generator berechnet und nachgerechnet.

## 2026-11-18 04:54 – STATUS: Expedition 1 „Die Wetterstation“ (5-wetterstation) fertig
4 Teile, Themen: groessen.einheiten, zahlen.ganz, zahlen.rechengesetze. Prüfskript OK, alle Lösungen vom Generator berechnet und nachgerechnet.
