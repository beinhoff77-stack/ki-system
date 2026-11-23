# Prüfung KJ – App 0.93.0 (lernen-app 7fec897), 23.11.2026

Geprüft gegen `kind/jugendwoerter/umsetzung.md` (Fassung 2) und `kind/karten/umsetzung.md`. Grundlage: Meldung `bau-motivation.md` „FERTIG: KJ (App 0.93.0)“, Bilder `docs/previews/la/jw-*`, `kj-*`, `rk3-kopf-land-360-tag`. Selbst angesehen in der App bei 360 × 740, 400 × 860 und 820 × 1180, Tag und Nacht. Dafür habe ich die Testdaten der Suite benutzt (Testkind, erfundene Zahlen), dazu Messungen per Kasten und Farbe. Eigene Bilder liegen in `nachpruefung_kj/`.

## Urteil

**Live erst nach M1 und M2.** Beides sind kleine Änderungen (Farbe eines Knopfs, eine Zeile weg). Die Soll-Punkte können im nächsten Schritt kommen.

## Muss

- **M1 – „Zur Reisekarte ›“ ist nachts unlesbar.**
  - Gemessen: Abflugtafel, Nacht, 360/400/820. Der Knopf hat weißen Grund (255, 254, 250) und fast weiße Schrift (242, 244, 247). Man sieht einen leeren weißen Kasten (Bild `tafel-400-nacht-unten.png`).
  - Ursache: Der Knopf ist ein `button` mit der Klasse `lr-textlink` (`lernen.js` Z. 1460). Bei Nacht bekommt er den Browser-Grund. Das ist seit RK-App 0.92.0 so, aber noch nicht live.
  - **Änderung:** `.rk-zur-karte` durchsichtig, ohne Rand, Schrift wie die übrigen Textlinks (unterstrichen). Test: Nacht, Kontrast Schrift/Grund ≥ 4,5 : 1.
- **M2 – Zwei widersprüchliche Zahlen auf der Kinderseite.**
  - Direkt unter „Mein Schuljahr“ (`2 von 15 Flügen · 29 von 112 Etappen`, 26 %) stehen die alten Mini-Linien `GYM 5 · 0/1 gelandet`, `RS 5 · keine Flüge`, `noch kein MYP-Jahr` (`lernMiniLinien`, Z. 815 ff.; Bild `kj-start-400-tag`).
  - Ein Kind liest „2 Flüge geschafft“ und gleich darunter „0/1 gelandet“. Die Vorgabe sagt: gleiche Rechnung wie der Ring, Nachbarklassen nur als schmale Balken in der Karte.
  - **Änderung:** Mini-Linien auf der Abflugtafel weglassen. Unter „Meine Route 5–10 ›“ bzw. im Linienplan dürfen sie bleiben, dort sind sie ein Vergleich der Schularten.

## Soll

- **S1 – Anrede-Sticker in der Titelzeile (Frage 2).**
  - Bei 360 und 400 bricht „Abflüge · Kind A“ wegen des Stickers zweizeilig um. „Digga, los geht’s.“ ist 120–137 px breit. Bei 820 passt es (Bild `tafel-360-tag-oben.png`).
  - **Änderung:** Unter 600 px steht der Sticker nicht in der Titelzeile. Er klebt schräg auf der rechten oberen Ecke der ersten Karte (Nachbessern bzw. Abflugtafel) und ragt etwa 12 px über deren Rand – wie ein Aufkleber. Der Titel bleibt einzeilig. Ab 600 px bleibt es wie jetzt.
- **S2 – Fortschrittslinie von „Gerade dran“ hängt unter dem Zusatz.**
  - Die Zeile `●●○ ✈ Noch 1 Etappe bis ›Natürliche Zahlen‹ gelandet` steht nach der Karte „Zusatz · eingeplant“. Damit liest sie sich wie der Stand des Zusatzes (Bild `kj-start-400-tag`).
  - **Änderung:** Die Zeile direkt unter die Abflugtafel, vor die Zusatz-Karte (Vorgabe §0.3: Check-in-Zeile bleibt in „Gerade dran“).
- **S3 – Nachbessern-Übung: zwei Zähler gleichzeitig.**
  - Oben steht die normale Etappen-Leiste `Etappe 1/3 · … ○○ 0 von 2 richtig`, darunter die Nachbessern-Leiste `1 von 3 in Folge` (Bild `kj-nb-uebung-400`). „0 von 2“ und „1 von 3“ widersprechen sich für das Kind.
  - **Änderung:** Beim Nachbessern ersetzt die Nachbessern-Leiste den Zähler der Etappen-Leiste. Etappen-Name und Blättern ‹ › bleiben, „x von 2 richtig“ entfällt.
- **S4 – Nachbessern- und Zusatz-Karte bleiben nachts hell.**
  - Gemessen: Nachbessern hat Grund (255, 241, 230), Zusatz (246, 239, 226) – auch in der dunklen Ansicht. Mein Schuljahr wird dunkel. Lesbar ist alles, aber nachts sind das zwei grelle Blöcke (Bild `tafel-400-nacht-oben.png`).
  - **Änderung, Nacht:**
    - Nachbessern: Grund `#2E1D14`, Rand `#8A4A26`, Kopf und Knopf orange wie am Tag, Text `#F6E3D6`.
    - Zusatz: Grund `#27231A`, Rand gestrichelt `#8C7A55`, Text `#EDE3CF`.
    - Zweitknopf: dunkel mit hellem Rand.
- **S5 – Lehrer-Ansicht, drei Kleinigkeiten (Frage 8):**
  - a) 1280: Der Fahrplan-Kopf bricht als „Fahrpla / n“ um, weil „8 Plätze · 10 Themen · + 1 Zusatz“ daneben zu breit ist (`kj-lehrer-lehrplan-1280`). Zahl-Zeile unter das Wort „Fahrplan“ oder kleiner setzen.
  - b) Detail-Blatt: Der Stand-Satz läuft rechts aus dem Blatt. Zu sehen ist „… sobald alle gelandet (“ und darunter „Flug-Test) · dann …“; „ohne“ wird abgeschnitten (`kj-lehrer-lehrplan-1280`). Umbruch statt Abschneiden.
  - c) In der Matrix ist „Bruchterme“ als `Zusatz · eingeplant · Platz 3a` markiert. Im Fahrplan steht derselbe Platz als normaler Eintrag „3 Bruchterme und 3 weitere“ ohne Zusatz-Marke.
    - Entweder steht der Zusatz-Teil als eigener Platz (Vorgabe §3: eigener Platz, gestrichelt), oder die Gruppe zeigt die Marke `+ 1 Zusatz`.
    - Vermutung: Das kommt aus den Testdaten (Zusatz-Teil liegt in einer Gruppe). Mit echten Daten prüfen.
- **S6 – 360 px: Die schwebende „Einsteigen“-Leiste verdeckt auf dem ersten Bildschirm die Abflugtafel.**
  - Gemessen: Tafel 628–734 px, Leiste 656–740 px (Bild `tafel-360-tag-oben.png`). Das Kind sieht „Einsteigen ROM ›“, aber die Tafel mit dem eigenen gelben „EINSTEIGEN“ liegt darunter.
  - **Änderung:** Die Leiste erst einblenden, wenn die Tafel aus dem Bild gescrollt ist. So steht nie zweimal derselbe Knopf übereinander. Gilt für alle Breiten.

## Kann

- **K1 – Sticker etwas größer.** Die Vorgabe hat Stärke 3 bei 26 px vorgesehen, gebaut sind 20 px (kurz) bzw. 16 px (lang). Bei 360/400 wirkt „PEAK“ dadurch eher wie ein Etikett. Stärke 3: 24 px, Stärke 2: 20 px, lang −4 px.
- **K2 – Bedeutungs-Blatt.**
  - a) Nachts bleibt das Blatt weiß. Das ist lesbar (dunkle Schrift auf Weiß), aber grell. Dunkle Fassung wie die übrigen Blätter.
  - b) Bei Çüş stand „gesprochen „Tschüsch““ doppelt, weil es auch in der Bedeutung stand. Das ist mein Fehler in `woerter.json`; ich habe es in meinem Zweig korrigiert. **Bau: `daten/jugendwoerter.json` neu kopieren** – der Gleichheits-Test zeigt das an.
- **K3 – 820 zweispaltig (Frage 9):** nach dem Live. Einspaltig steht „Gerade dran“ bei 820 im ersten Bildschirm (Tafel 577–666 px), die Seite ist 1,7 Bildschirme lang. Das ist nicht störend.
- **K4 – „Sitzt wieder!“:** „Weiter nachbessern: Zahlenstrahl ›“ ist ein Textlink. Die Vorgabe sieht einen Knopf vor; ein großer Knopf wie bei der Landung wäre besser.
- **K5 – Zusatz-Karte:** Flagge und „– Teil x von y“ fehlen (Vorgabe §3). In den Testdaten gibt es keinen Teil; mit Teil-Daten prüfen.
- **K6 – Lehrer-Überblick 400:** Ringe und Tabelle stehen doppelt. Die Vorgabe sagt: auf dem Handy nur die Tabelle.
- **K7 – Nebenbefund, nicht durch KJ:** Bei 360 überdeckt das Direkt-Abzeichen (Sechseck) das Ende von „DIREKTFLUG“ (Bild `landung-direkt-360-nacht.png`).
- **K8 – Unteres Ende der Abflugtafel aufräumen:** Unter Mein Schuljahr folgen noch sechs Zeilen: Stempel, „Abflug, wann es dir passt“, Erklärungen, Route, Später, Was kommt wann. Zusammenfassen oder hinter „Mehr ▾“ legen.

## Antworten auf die Fragen

1. **Sticker:**
   - **Ort und Verdecken:** unten rechts in der Szene. Er verdeckt in keiner der 18 Landungen (direkt/sauber/sturm × 360/400/820 × Tag/Nacht) einen Text; gemessen an allen Text-Elementen der Szene. Beim Sturmflug liegt er über der Blitz-Zeichnung, beim sauberen über der Landebahn – nur Bild, kein Text.
   - **Wirkung:** cool, nicht aufgesetzt (Meinung). Schräg, weißer Rand, kurze Ausrufe; der erklärende Satz bleibt Deutsch. Etwas klein (K1).
   - **Stärke:** passt. Direkt Gold (PEAK, GOAT, SIUUU!, Çüş – auf Anhieb!), sauber Mint (Tuff., Süper!, Nice gelandet!), Sturm nur Ausdauer-Wörter (Locked in., Stabil durchgehalten., Tuff durchgezogen., Macher-Modus), Flug geschafft Gold (GOAT-Flug, SIUUU!, Aura +1000).
   - **Bedeutungs-Blatt:** gut lesbar, groß, „Schließen“ deutlich. Nachts grell weiß (K2a).
   - Fehler-Sticker und Knobel habe ich nicht selbst nachgestellt; das deckt der Test des Bau-Chats ab.
2. **„Yo Digga!“ im Kopf:** Ja, auf dem Handy anders – siehe S1. Der Titel soll nicht umbrechen; der Sticker gehört auf die Ecke der ersten Karte.
3. **Gelber „Einsteigen“-Balken über „Zusatz · eingeplant“:**
   - Im Ganzseiten-Bild ist es vor allem eine Täuschung. Die Leiste ist `sticky` und klebt unten am Bildschirm; im Ganzseiten-Bild landet sie mitten auf der Seite.
   - In der echten Ansicht schiebt sich beim Scrollen jede Karte kurz unter die Leiste (mit Verlauf). Das ist normal und bei 400 nicht störend; am Seitenende liegt nichts darunter.
   - Störend ist es bei 360 auf dem ersten Bildschirm, weil die Leiste die Abflugtafel selbst verdeckt (S6).
4. **Erster Bildschirm und Länge:**
   - 400 × 860: Abflugtafel mit ROM bei 609–715 px, also im ersten Bildschirm, dazu die Leiste „Einsteigen ROM ›“. Das Kind sieht, was dran ist.
   - 360 × 740: Die Tafel liegt unter der Leiste. Die Leiste sagt es trotzdem (S6).
   - Länge: 2,6 Bildschirme (400), 3,1 (360), 1,7 (820). Noch vertretbar; Kürzen geht über K8, nicht über die Reihenfolge.
5. **Nachbessern:**
   - Ohne Erklärung verständlich: „eingerostet“, drei Kreise, „Mit 3 richtigen in Folge sitzt sie wieder“.
   - Wirkt nicht wie Strafe: orange statt rot, „Deine Sterne und Stempel bleiben“, „Kein Problem – neuer Anlauf.“. „Sitzt wieder!“ mit drei Haken und Sticker („Süper repariert!“) fühlt sich nach Erfolg an.
   - Einziger Stolperstein ist der doppelte Zähler in der Übung (S3).
6. **Mein Schuljahr:**
   - Die Zahlen sind auf einen Blick verständlich, weil das Geschaffte zuerst steht und das Ziel klein ist („nur noch 5 Etappen“ bzw. „nur noch 1 Etappe“).
   - Text: zwei Sätze mit vier Zahlen – an der Grenze, aber in Ordnung.
   - Das eigentliche Problem sind die widersprechenden Mini-Linien direkt darunter (M2).
7. **Zusatz · eingeplant:** klar als Extra erkennbar – gestrichelt, Sandfarbe, weißer Zweitknopf, „von deinen Eltern eingeplant“, kein gelber Knopf. Er konkurriert nicht mit dem Pflicht-Flug, solange die Fortschrittslinie von „Gerade dran“ nicht unter ihm hängt (S2). Nachts zu hell (S4).
8. **Lehrer:**
   - Stimmig mit der Vorgabe: Stand-Karte mit „Kl. 8 Gymnasium · 9 % · noch 15 von 16 Flügen · noch 88 von 97 Etappen“, Hauptklasse hinterlegt, Zusatz-Zeile mit ⓘ; Matrix-Karte gestrichelt sand mit „Platz n · x/y Etappen“; Fahrplan „ZUSATZ · EINGEPLANT 2 von 5 Etappen · ohne Flug-Test“ und Kopf „+ 1 Zusatz“.
   - Abweichungen: S5 (Kopf bricht um, Detail-Satz abgeschnitten, Gruppe ohne Zusatz-Marke) und K6.
9. **820 einspaltig:** nicht vor dem Live (K3).

## Nicht geprüft

Echter Server und echte Kinderdaten, echte Geräte. Fehler- und Knobel-Sticker sowie die Regel „Anrede einmal je Lerntag“ habe ich nur über den Test des Bau-Chats geprüft, nicht selbst nachgestellt.

FERTIG: Prüfung KJ (App 0.93.0) – 2 Muss (Zur-Reisekarte-Knopf nachts unlesbar, widersprüchliche Mini-Linien unter Mein Schuljahr), 6 Soll, 8 Kann; live erst nach M1 und M2.
