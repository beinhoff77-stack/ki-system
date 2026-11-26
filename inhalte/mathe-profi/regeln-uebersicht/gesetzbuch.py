"""Mathe-Profi, Auftrag 10 (nach der Klarstellung „Gesetzbuch“): vollständiges Inhaltsverzeichnis und Muster-Planet.

Aufruf: python3 -I inhalte/mathe-profi/regeln-uebersicht/gesetzbuch.py
- hält alle Gesetze je Gebiet als Daten, jedes mit den Themen der App, in denen es vorkommt,
- leitet Klasse und Schulart je Gesetz aus inhalte/themenliste.json ab (Gymnasium, Realschule, IB),
- prüft, dass jedes Thema der App von mindestens einem Gesetz oder einer Rechenregel der Sonne erfasst ist,
- rechnet die Beispiele des Muster-Planeten nach,
- schreibt inhalt.md (Landkarte und Inhaltsverzeichnis) und planet-flaeche-und-raum.md.
Die Sonne (14 Rechenregeln) steht in sonne.md, erzeugt von bauen.py.
"""
import importlib.util
import sys
import io
import json
import os
import contextlib
from fractions import Fraction as F

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
LISTE = {t["thema_schluessel"]: t for t in json.load(open(os.path.join(WURZEL, "inhalte", "themenliste.json"), encoding="utf-8"))}
spec = importlib.util.spec_from_file_location("sonne", os.path.join(HIER, "bauen.py"))
sonne = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(sonne)          # prüft dabei die 14 Rechenregeln und schreibt sonne.md
SONNE = [r["name"] for r in sonne.R]

# Planet → Abschnitte → Gesetze: (Name, Satz in einem Atemzug, [Themen], [Rechenregeln der Sonne, aus denen es folgt oder die es braucht])
P = {
 "Zahlen": [
  ("Zahlen schreiben und ordnen", [
   ("Stellenwertsystem", "Jede Stelle ist zehnmal so viel wert wie die Stelle rechts daneben – auch hinter dem Komma.", ["zahlen.natuerlich", "bruch.dezimal"], [1]),
   ("Runden", "Die Ziffer rechts von der Rundungsstelle entscheidet: 0 bis 4 abrunden, 5 bis 9 aufrunden.", ["zahlen.natuerlich", "bruch.dezimal"], [1]),
   ("Andere Zahlschriften", "Römische Zahlen reihen Zeichen aneinander; das Zweiersystem bündelt in Zweiern statt in Zehnern.", ["zahlen.natuerlich"], []),
   ("Ordnung auf der Zahlengeraden", "Was weiter links liegt, ist kleiner – auch bei negativen Zahlen und Brüchen.", ["zahlen.ganz", "bruch.brueche"], [2]),
   ("Betrag und Gegenzahl", "Der Betrag ist der Abstand zur Null. Die Gegenzahl liegt gleich weit auf der anderen Seite.", ["zahlen.ganz", "funktionen.betrag"], [2]),
  ]),
  ("Teilbarkeit", [
   ("Teiler und Vielfache", "a ist Teiler von b, wenn b geteilt durch a ohne Rest aufgeht.", ["zahlen.teilbarkeit"], []),
   ("Teilbarkeitsregeln", "Durch 2, 5 und 10: letzte Ziffer ansehen. Durch 3 und 9: Quersumme ansehen.", ["zahlen.teilbarkeit"], [1]),
   ("Primzahlen und Primfaktoren", "Jede Zahl größer als 1 lässt sich auf genau eine Weise in Primzahlen zerlegen.", ["zahlen.teilbarkeit"], []),
   ("ggT und kgV", "Der größte gemeinsame Teiler kürzt vollständig, das kleinste gemeinsame Vielfache ist der Hauptnenner.", ["bruch.brueche"], [9]),
  ]),
  ("Brüche und Dezimalzahlen", [
   ("Bruch als Anteil", "Der Nenner teilt, der Zähler zählt. Anteil = Teil durch Ganzes.", ["bruch.brueche"], []),
   ("Brüche vergleichen", "Bei gleichem Nenner ist der Bruch mit dem größeren Zähler größer; sonst erst gleichnamig machen.", ["bruch.brueche"], [9]),
   ("Drei Schreibweisen einer Zahl", "Bruch, Dezimalzahl und Prozent sagen dasselbe: ½ = 0,5 = 50 %.", ["bruch.dezimal", "bruch.prozent"], [1]),
   ("Periodische Dezimalzahlen", "Jeder Bruch wird als Dezimalzahl endlich oder periodisch – nie etwas anderes.", ["bruch.dezimal"], []),
   ("Rechnen mit Komma", "Mal: Nachkommastellen zusammenzählen. Geteilt: das Komma in beiden Zahlen gleich weit verschieben.", ["bruch.rechnen"], [1]),
  ]),
  ("Potenzen, Wurzeln, Logarithmen", [
   ("Quadratzahlen", "Hoch 2 heißt Zahl mal sich selbst; die Quadratzahlen bis 20² weiß man auswendig.", ["zahlen.potenzen_basis"], [8]),
   ("Potenz mit negativer Basis", "Gerade Hochzahl: Ergebnis positiv. Ungerade Hochzahl: Ergebnis negativ.", ["zahlen.potenzen_basis"], [3, 8]),
   ("Hoch null und negative Hochzahl", "a⁰ = 1. Eine negative Hochzahl heißt Kehrwert: a⁻ⁿ = 1 : aⁿ.", ["terme.potenzgesetze", "terme.potenzgesetze_ganzzahlig"], [8]),
   ("Zehnerpotenzen", "10ⁿ ist eine 1 mit n Nullen, 10⁻ⁿ hat n Stellen hinter dem Komma. Kilo, Mega, Milli, Mikro sind Zehnerpotenzen.", ["zahlen.potenzen_zehner", "zahlen.potenzen_basis"], [1, 8]),
   ("Potenzgesetze", "Gleiche Basis: Hochzahlen addieren. Gleiche Hochzahl: Basen malnehmen. Potenz der Potenz: Hochzahlen malnehmen.", ["terme.potenzgesetze_natuerlich", "terme.potenzgesetze_ganzzahlig", "zahlen.rationale_exponenten"], [8]),
   ("Quadratwurzel", "Die Wurzel aus a ist die Zahl ab null, deren Quadrat a ist. Aus negativen Zahlen gibt es keine.", ["zahlen.wurzeln_basis"], [12]),
   ("Wurzelgesetze", "Wurzel mal Wurzel ist Wurzel aus dem Produkt, Wurzel durch Wurzel ist Wurzel aus dem Quotienten – nicht bei Plus und Minus.", ["zahlen.reell"], [8]),
   ("Irrationale und reelle Zahlen", "Manche Zahlen sind kein Bruch, zum Beispiel √2. Brüche und diese Zahlen zusammen heißen reelle Zahlen.", ["zahlen.reell"], []),
   ("n-te Wurzel und Bruch als Hochzahl", "a hoch 1/n ist die n-te Wurzel aus a.", ["zahlen.rationale_exponenten"], [8, 12]),
   ("Logarithmus", "Der Logarithmus ist die gesuchte Hochzahl. Aus Mal wird Plus, aus Hoch wird Mal.", ["gleichungen.exponential", "funktionen.exponential_log"], [8, 12]),
  ]),
 ],
 "Algebra": [
  ("Terme", [
   ("Term und Variable", "Ein Buchstabe steht für eine Zahl. Die zuletzt ausgeführte Rechnung gibt dem Term seinen Namen.", ["terme.aufstellen"], [4]),
   ("Gleichwertige Terme", "Zwei Terme sind gleichwertig, wenn sie für jede eingesetzte Zahl denselben Wert haben.", ["terme.umformen"], []),
   ("Summe mal Summe", "Jedes Glied der ersten Klammer mal jedes Glied der zweiten.", ["terme.umformen"], [6]),
   ("Binomische Formeln", "(a + b)² = a² + 2ab + b² · (a − b)² = a² − 2ab + b² · (a + b)(a − b) = a² − b²", ["terme.umformen", "terme.quadratische_extreme"], [6]),
   ("Definitionsmenge", "Ein Nenner darf nie null sein. Diese Zahlen werden vorher ausgeschlossen.", ["terme.bruchterme", "gleichungen.bruch", "funktionen.gebrochen"], [14]),
   ("Bruchterme", "Mit Bruchtermen rechnet man wie mit Brüchen: erst faktorisieren, dann kürzen.", ["terme.bruchterme"], [9, 10]),
   ("Kleinster und größter Wert", "(x − d)² + e ist nie kleiner als e und wird es genau bei x = d.", ["terme.quadratische_extreme"], [6]),
  ]),
  ("Gleichungen ersten Grades", [
   ("Äquivalenzumformung", "Dieselbe Rechnung auf beiden Seiten ändert die Lösung nicht – außer mal null und geteilt durch null.", ["gleichungen.einfach", "gleichungen.linear"], [13]),
   ("Wie viele Lösungen?", "Eine lineare Gleichung hat genau eine Lösung, keine oder jede Zahl als Lösung.", ["gleichungen.einfach", "gleichungen.linear"], []),
   ("Ungleichungen", "Mal oder geteilt durch eine negative Zahl dreht das Ungleichheitszeichen um.", ["gleichungen.ungleichungen"], [3, 13]),
   ("Intervalle", "Eckige Klammer: Die Grenze gehört dazu. Nach außen gedrehte oder runde Klammer: Sie gehört nicht dazu.", ["zahlen.intervalle"], []),
   ("Bruchgleichungen", "Mit dem Hauptnenner malnehmen; die Lösung muss in der Definitionsmenge liegen. Bruch gleich Bruch: über Kreuz.", ["gleichungen.bruch"], [10, 13]),
   ("Formeln umstellen", "Eine Formel ist eine Gleichung mit mehreren Buchstaben: nach dem gesuchten auflösen.", ["gleichungen.formeln"], [12, 13]),
   ("Gleichungssystem mit zwei Unbekannten", "Gesucht ist das Zahlenpaar, das beide Gleichungen erfüllt: einsetzen, gleichsetzen oder addieren. Zwei Geraden schneiden sich, sind parallel oder gleich.", ["gleichungen.lgs2"], [13]),
   ("Gleichungssystem mit drei Unbekannten", "Erst eine Unbekannte entfernen, dann von unten nach oben einsetzen.", ["gleichungen.lgs3"], [13]),
  ]),
  ("Gleichungen höheren Grades", [
   ("x² = a", "Zwei Lösungen, wenn a positiv ist (Wurzel und Gegenzahl), eine bei a = 0, keine bei negativem a.", ["gleichungen.reinquadratisch", "gleichungen.quadratisch"], [12]),
   ("Faktorisieren", "Alles auf eine Seite, ausklammern, dann jeden Faktor gleich null setzen.", ["gleichungen.quadratisch", "gleichungen.polynom"], [6, 14]),
   ("Quadratische Ergänzung", "Zum Binom ergänzen, was fehlt – und es gleich wieder abziehen.", ["gleichungen.quadratisch", "terme.quadratische_extreme"], [6]),
   ("Lösungsformel", "Die Lösungsformel löst jede quadratische Gleichung. Der Ausdruck unter der Wurzel entscheidet: positiv zwei Lösungen, null eine, negativ keine.", ["gleichungen.quadratisch"], [12]),
   ("Wurzelgleichungen", "Quadrieren kann falsche Lösungen erzeugen. Die Probe ist Pflicht.", ["gleichungen.wurzel"], [12]),
   ("Potenzgleichungen", "xⁿ = c: bei gerader Hochzahl zwei Lösungen oder keine, bei ungerader genau eine.", ["gleichungen.potenz"], [3, 12]),
   ("Exponentialgleichungen", "Gleiche Basis: Hochzahlen gleichsetzen. Sonst hilft der Logarithmus.", ["gleichungen.exponential"], [12]),
   ("Polynomgleichungen", "Ausklammern oder x² ersetzen. Eine doppelte Lösung berührt die Achse nur.", ["gleichungen.polynom"], [6, 14]),
  ]),
 ],
 "Geld und Verhältnisse": [
  ("Größen", [
   ("Größe und Einheit", "Eine Größe ist Zahl mal Einheit. Umrechnungszahlen: Längen 10 (und 1 000 bis km), Massen 1 000, Zeit 60.", ["groessen.einheiten"], [1]),
   ("Maßstab", "1 : n heißt: 1 cm im Plan sind n cm in Wirklichkeit.", ["groessen.einheiten"], [11]),
  ]),
  ("Proportionalität", [
   ("Direkte Proportionalität", "Doppelt so viel von dem einen, doppelt so viel von dem anderen. Der Quotient bleibt gleich.", ["groessen.proportional", "funktionen.linear"], [11]),
   ("Dreisatz", "Erst auf eins, dann auf viele.", ["groessen.proportional"], [11]),
   ("Verhältnisse", "a : b lässt sich kürzen wie ein Bruch. Aufteilen im Verhältnis: erst die Teile zusammenzählen.", ["groessen.verhaeltnisse", "bruch.brueche"], [9]),
   ("Indirekte Proportionalität", "Doppelt so viel von dem einen, halb so viel von dem anderen. Das Produkt bleibt gleich.", ["groessen.indirekt"], [11]),
   ("Änderungsrate", "Änderung je Einheit: Unterschied der Werte durch Unterschied der Schritte.", ["groessen.proportional", "groessen.verhaeltnisse"], [11]),
  ]),
  ("Prozent und Zins", [
   ("Grundgleichung der Prozentrechnung", "Prozentwert = Prozentsatz mal Grundwert. Zwei der drei Größen bestimmen die dritte.", ["bruch.prozent"], [1, 12]),
   ("Wachstumsfaktor", "Plus p % heißt mal (1 + p/100), minus p % heißt mal (1 − p/100). Erst plus 10 %, dann minus 10 % ist nicht wieder der Anfang.", ["bruch.prozent_grundwert"], [1]),
   ("Zinsen", "Jahreszinsen = Kapital mal Zinssatz. Für Monate nimmt man den Anteil am Jahr.", ["finanzen.zinsen"], [1]),
   ("Zinseszins", "Kapital nach n Jahren = Anfangskapital mal Wachstumsfaktor hoch n.", ["finanzen.zinseszins", "bruch.prozent_grundwert"], [8]),
  ]),
 ],
 "Geometrie": [
  ("Lage und Winkel", [
   ("Koordinatensystem", "Punkt (x | y): erst nach rechts oder links, dann nach oben oder unten.", ["geometrie.grundbegriffe"], []),
   ("Parallel, senkrecht, Abstand", "Der Abstand ist die kürzeste Verbindung – sie steht senkrecht.", ["geometrie.grundbegriffe"], []),
   ("Winkelarten", "Voller Winkel 360°, gestreckter 180°, rechter 90°.", ["geometrie.grundbegriffe", "geometrie.winkel"], []),
   ("Scheitel- und Nebenwinkel", "Scheitelwinkel sind gleich groß. Nebenwinkel ergeben zusammen 180°.", ["geometrie.winkel", "geometrie.winkelsaetze"], []),
   ("Stufen- und Wechselwinkel", "An parallelen Geraden sind Stufenwinkel und Wechselwinkel gleich groß – und umgekehrt.", ["geometrie.winkelsaetze"], []),
   ("Winkelsumme", "Im Dreieck 180°, im Viereck 360°, im n-Eck (n − 2) mal 180°. Ein Außenwinkel ist so groß wie die beiden anderen Innenwinkel zusammen.", ["geometrie.winkelsaetze"], []),
  ]),
  ("Figuren und Konstruktion", [
   ("Besondere Vierecke", "Quadrat, Rechteck, Raute, Parallelogramm, Trapez, Drachenviereck: Jedes hat seine festen Eigenschaften.", ["geometrie.grundbegriffe", "geometrie.konstruktion"], []),
   ("Ortslinien", "Kreis: gleich weit von einem Punkt. Mittelsenkrechte: gleich weit von zwei Punkten. Winkelhalbierende: gleich weit von zwei Schenkeln.", ["geometrie.ortslinien", "abbildungen.kongruenz"], []),
   ("Gleichschenkliges Dreieck", "Gleiche Schenkel, gleiche Basiswinkel – und umgekehrt. Gleichseitig: dreimal 60°.", ["geometrie.konstruktion"], []),
   ("Kongruenzsätze", "Drei passende Angaben legen ein Dreieck fest: SSS, SWS, WSW, SsW. Zwei Seiten sind zusammen immer länger als die dritte.", ["geometrie.konstruktion"], []),
   ("Satz und Kehrsatz", "Die Umkehrung eines Satzes ist ein neuer Satz und muss eigens begründet werden.", ["geometrie.konstruktion", "geometrie.kreis"], []),
   ("Satz des Thales", "Liegt die Ecke auf dem Halbkreis über einer Seite, hat das Dreieck dort einen rechten Winkel – und umgekehrt.", ["geometrie.kreis"], []),
   ("Tangente", "Die Tangente steht senkrecht auf dem Radius zum Berührpunkt.", ["geometrie.kreis"], []),
   ("Umkreis und Inkreis", "Umkreis-Mittelpunkt: Schnitt der Mittelsenkrechten. Inkreis-Mittelpunkt: Schnitt der Winkelhalbierenden.", ["geometrie.kreis"], []),
  ]),
  ("Abbilden", [
   ("Spiegeln, Verschieben, Drehen", "Diese Abbildungen ändern weder Längen noch Winkel: Bild und Original sind deckungsgleich.", ["abbildungen.kongruenz"], []),
   ("Symmetrie", "Achsensymmetrisch: Spiegeln an der Achse ändert nichts. Punktsymmetrisch: halbe Drehung ändert nichts.", ["abbildungen.kongruenz"], []),
   ("Vektoren", "Ein Vektor ist eine Verschiebung: Spitze minus Fuß. Der Gegenvektor führt zurück.", ["abbildungen.vektoren", "abbildungen.kongruenz"], [2]),
   ("Fläche mit Determinante", "Zwei Vektoren spannen ein Parallelogramm auf; seine Fläche ist der Betrag von a·d − b·c.", ["abbildungen.determinanten2"], []),
   ("Matrizen und Skalarprodukt", "Eine Matrix beschreibt eine Abbildung. Skalarprodukt null heißt senkrecht.", ["abbildungen.matrizen"], []),
  ]),
  ("Ähnlichkeit und rechtwinkliges Dreieck", [
   ("Ähnlichkeit", "Ähnliche Figuren haben gleiche Winkel und alle Seiten im selben Verhältnis.", ["abbildungen.aehnlichkeit"], [11]),
   ("Strahlensätze", "Schneiden Parallelen zwei Strahlen, stehen die Abschnitte im selben Verhältnis.", ["abbildungen.aehnlichkeit"], [11]),
   ("Vergrößern mit Faktor k", "Längen mal k, Flächen mal k², Volumen mal k³.", ["abbildungen.aehnlichkeit", "messen.kreisberechnung"], [8]),
   ("Schwerpunkt", "Die Seitenhalbierenden schneiden sich im Schwerpunkt; er teilt sie im Verhältnis 2 : 1.", ["abbildungen.aehnlichkeit"], [11]),
   ("Satz des Pythagoras", "Im rechtwinkligen Dreieck gilt a² + b² = c² – und nur dort.", ["trigo.pythagoras"], [12]),
   ("Sinus, Kosinus, Tangens", "Sinus = Gegenkathete durch Hypotenuse, Kosinus = Ankathete durch Hypotenuse, Tangens = Gegenkathete durch Ankathete.", ["trigo.rechtwinklig"], [11]),
   ("Zusammenhänge der Winkelfunktionen", "sin² + cos² = 1 und tan = sin : cos.", ["trigo.rechtwinklig"], []),
   ("Einheitskreis", "Am Kreis mit Radius 1 sind Kosinus und Sinus die Koordinaten des Punktes – für jeden Winkel.", ["trigo.allgemein"], []),
   ("Sinussatz und Kosinussatz", "In jedem Dreieck: Seite durch Sinus des Gegenwinkels ist für alle drei gleich. Der Kosinussatz ist Pythagoras mit Korrektur.", ["trigo.allgemein"], []),
   ("Additionstheoreme", "Der Sinus einer Summe ist nicht die Summe der Sinus: sin(α + β) = sin α · cos β + cos α · sin β.", ["trigo.allgemein"], []),
   ("Winkel aus Sinus oder Kosinus", "Zu einem Wert gehören in einer vollen Drehung meist zwei Winkel.", ["gleichungen.trig"], [12]),
  ]),
 ],
 "Fläche und Raum": [
  ("Flächen", [
   ("Fläche messen", "Flächeninhalt heißt: Wie viele Einheitsquadrate passen hinein? Umrechnungszahl 100.", ["messen.flaechen"], [1]),
   ("Rechteck", "Fläche = Länge mal Breite. Umfang = einmal außen herum.", ["messen.flaechen"], []),
   ("Fläche ist nicht Umfang", "Gleicher Umfang heißt nicht gleiche Fläche.", ["messen.flaechen", "terme.quadratische_extreme"], []),
   ("Zerlegen und Ergänzen", "Zerschneiden und neu zusammenlegen ändert die Fläche nicht.", ["messen.flaechen", "messen.flaechen_vielecke"], []),
   ("Parallelogramm", "Fläche = Grundseite mal Höhe. Die Höhe steht senkrecht.", ["messen.flaechen_vielecke"], []),
   ("Dreieck", "Fläche = Grundseite mal Höhe, geteilt durch 2.", ["messen.flaechen_vielecke", "gleichungen.formeln"], []),
   ("Trapez", "Fläche = Mittelwert der beiden parallelen Seiten mal Höhe.", ["messen.flaechen_vielecke", "gleichungen.formeln"], []),
   ("Drachenviereck und Raute", "Fläche = Diagonale mal Diagonale, geteilt durch 2.", ["messen.flaechen_vielecke"], []),
   ("Kreis", "Umfang = 2 · π · r. Fläche = π · r². π ist etwas mehr als 3.", ["messen.kreisberechnung"], []),
   ("Kreisausschnitt", "Der Anteil am vollen Winkel ist der Anteil an Umfang und Fläche.", ["messen.kreisberechnung"], [11]),
  ]),
  ("Körper", [
   ("Volumen messen", "Volumen heißt: Wie viele Einheitswürfel passen hinein? Umrechnungszahl 1 000. 1 Liter = 1 dm³.", ["messen.volumen"], [1]),
   ("Quader", "Volumen = Länge mal Breite mal Höhe.", ["messen.volumen"], []),
   ("Oberfläche", "Die Oberfläche ist die Summe aller Flächen des Netzes. Quader: sechs Rechtecke, je zwei gleich.", ["messen.koerper_berechnung", "messen.flaechen_vielecke"], []),
   ("Netz und Schrägbild", "Das Netz ist der aufgeklappte Körper. Im Schrägbild werden Kanten nach hinten schräg und verkürzt gezeichnet.", ["messen.koerper_darstellung", "raum.schraegbilder"], []),
   ("Prisma und Zylinder", "Volumen = Grundfläche mal Höhe. Oberfläche = zwei Grundflächen plus Mantel.", ["messen.prisma_zylinder"], []),
   ("Satz von Cavalieri", "Gleiche Höhe und auf jeder Höhe gleich große Schnittfläche: gleiches Volumen.", ["messen.prisma_zylinder"], []),
   ("Pyramide und Kegel", "Volumen = ein Drittel von Grundfläche mal Höhe.", ["raum.pyramide_kegel_kugel"], []),
   ("Kugel", "Volumen = 4/3 · π · r³. Oberfläche = 4 · π · r².", ["raum.pyramide_kegel_kugel"], []),
   ("Lage im Raum", "Zwei Geraden im Raum sind parallel, schneiden sich oder laufen windschief aneinander vorbei.", ["raum.schraegbilder"], []),
  ]),
 ],
 "Funktionen": [
  ("Grundbegriffe", [
   ("Funktion", "Zu jedem x gehört genau ein y.", ["funktionen.grundbegriffe"], []),
   ("Punktprobe", "Ein Punkt liegt auf dem Graphen, wenn seine Koordinaten die Gleichung erfüllen.", ["funktionen.grundbegriffe", "funktionen.quadratisch"], []),
   ("Nullstelle und Achsenabschnitt", "Nullstelle: y = 0. Schnitt mit der y-Achse: x = 0.", ["funktionen.grundbegriffe", "funktionen.gebrochen"], [13]),
   ("Schnittpunkt", "Im Schnittpunkt haben beide Funktionen denselben Wert: gleichsetzen.", ["funktionen.linear", "funktionen.quadratisch"], [13]),
   ("Graphen verschieben und strecken", "Plus e schiebt nach oben, (x − d) schiebt nach rechts, mal a streckt, ein Minus davor spiegelt.", ["funktionen.transformation", "funktionen.quadratisch", "funktionen.gebrochen", "funktionen.trig"], []),
   ("Umkehrfunktion", "x und y tauschen; der Graph wird an der Geraden y = x gespiegelt. Geht nur, wenn zu jedem y genau ein x gehört.", ["funktionen.umkehr", "funktionen.potenz"], [12]),
  ]),
  ("Funktionsarten", [
   ("Lineare Funktion", "y = m · x + t: m ist die Steigung (Höhenunterschied durch Längenunterschied), t der Abschnitt auf der y-Achse.", ["funktionen.linear"], [11]),
   ("Ursprungsgerade", "Proportional heißt: Gerade durch den Ursprung.", ["funktionen.linear"], [11]),
   ("Parallel und senkrecht", "Parallele Geraden haben dieselbe Steigung. Senkrechte: Die Steigungen ergeben malgenommen −1.", ["funktionen.linear"], []),
   ("Geradenscharen", "Ein Parameter in m dreht die Gerade, ein Parameter in t verschiebt sie.", ["funktionen.scharen", "funktionen.linear"], []),
   ("Hyperbel", "y = a : x: doppeltes x, halbes y. Der Graph kommt den Asymptoten beliebig nahe, erreicht sie aber nie.", ["funktionen.gebrochen", "groessen.indirekt"], [11]),
   ("Parabel", "y = a · (x − d)² + e hat den Scheitel (d | e). a entscheidet über Öffnung und Breite.", ["funktionen.quadratisch"], [6]),
   ("Potenzfunktionen", "Gerade Hochzahl: symmetrisch zur y-Achse. Ungerade Hochzahl: symmetrisch zum Ursprung.", ["funktionen.potenz"], [8]),
   ("Exponentialfunktion", "Exponentiell: In gleichen Schritten wird mit derselben Zahl malgenommen. Linear: Es kommt dieselbe Zahl dazu.", ["funktionen.exponential_log"], [8]),
   ("Logarithmusfunktion", "Sie ist die Umkehrung der Exponentialfunktion.", ["funktionen.exponential_log", "funktionen.umkehr"], [12]),
   ("Sinus- und Kosinusfunktion", "Sie wiederholen sich nach 360° (im Bogenmaß 2π). Die Amplitude ist die größte Auslenkung. 180° entsprechen π.", ["funktionen.trig"], []),
   ("Ganzrationale Funktionen", "Die höchste Hochzahl bestimmt, wohin der Graph außen läuft. Die Produktform zeigt die Nullstellen.", ["funktionen.ganzrational"], [14]),
   ("Betragsfunktion", "Der Graph hat einen Knick. |x| = a hat die Lösungen a und −a.", ["funktionen.betrag"], [2]),
   ("Folgen", "Arithmetisch: immer dieselbe Zahl dazu. Geometrisch: immer mit derselben Zahl mal.", ["funktionen.folgen", "funktionen.reihen"], []),
   ("Reihen", "Arithmetische Reihe: Anzahl mal Mittelwert aus erstem und letztem Glied. Für die geometrische gibt es eine eigene Summenformel.", ["funktionen.reihen"], []),
  ]),
 ],
 "Daten und Zufall": [
  ("Daten", [
   ("Häufigkeit", "Absolute Häufigkeit: wie oft. Relative Häufigkeit: Anzahl durch Gesamtzahl.", ["daten.darstellen", "stochastik.grundbegriffe"], [11]),
   ("Diagramme lesen", "Im Kreisdiagramm gehört zu jedem Anteil derselbe Anteil von 360°. Eine Achse, die nicht bei 0 beginnt, übertreibt Unterschiede.", ["daten.darstellen"], [11]),
   ("Mittelwert", "Alle Werte addieren, durch die Anzahl teilen.", ["daten.kennwerte"], []),
   ("Median, Modalwert, Spannweite", "Median: der Wert in der Mitte der geordneten Liste. Modalwert: der häufigste. Spannweite: größter minus kleinster.", ["daten.boxplot"], []),
   ("Mittelwert oder Median", "Ein Ausreißer zieht den Mittelwert mit, den Median nicht.", ["daten.boxplot"], []),
   ("Quartile und Boxplot", "Die Box enthält die mittlere Hälfte der Werte.", ["daten.boxplot"], []),
   ("Stichprobe", "Eine Stichprobe taugt nur, wenn sie zufällig gezogen und groß genug ist.", ["daten.stichproben"], [11]),
   ("Zusammenhang ist nicht Ursache", "Zwei Größen können zusammen steigen, ohne dass die eine die andere bewirkt.", ["daten.zweidimensional"], []),
   ("Streuung", "Die Standardabweichung misst, wie weit die Werte im Mittel vom Mittelwert entfernt liegen.", ["daten.standardabweichung"], [12]),
   ("Normalverteilung", "Etwa 68 % der Werte liegen höchstens eine Standardabweichung vom Mittelwert entfernt, 95 % höchstens zwei.", ["daten.normalverteilung"], []),
  ]),
  ("Zählen und Zufall", [
   ("Zählprinzip", "Die Möglichkeiten der einzelnen Stufen werden malgenommen.", ["stochastik.kombinatorik"], []),
   ("Ergebnis und Ereignis", "Ein Ereignis ist eine Menge von Ergebnissen.", ["stochastik.grundbegriffe"], []),
   ("Laplace-Wahrscheinlichkeit", "Günstige durch mögliche Ergebnisse – nur wenn alle gleich wahrscheinlich sind.", ["stochastik.grundbegriffe"], [11]),
   ("Gegenereignis", "Jede Wahrscheinlichkeit liegt zwischen 0 und 1. Gegenereignis: 1 minus die Wahrscheinlichkeit.", ["stochastik.grundbegriffe", "stochastik.mehrstufig"], []),
   ("Gesetz der großen Zahlen", "Bei sehr vielen Versuchen nähert sich die relative Häufigkeit der Wahrscheinlichkeit.", ["stochastik.grundbegriffe", "stochastik.simulation"], []),
   ("Additionssatz", "Entweder-oder: Wahrscheinlichkeiten addieren und das doppelt Gezählte abziehen.", ["stochastik.verknuepft", "mengen.grundbegriffe"], []),
   ("Vierfeldertafel", "Zeilen und Spalten ergeben die Randsummen; ein Feld folgt aus den anderen.", ["stochastik.verknuepft"], []),
   ("Bedingte Wahrscheinlichkeit", "Unter der Bedingung B zählt nur noch, was in B liegt. Unabhängig heißt: Die Bedingung ändert nichts.", ["stochastik.verknuepft", "stochastik.bedingt"], [11]),
   ("Pfadregeln", "Entlang eines Pfades malnehmen, mehrere Pfade addieren.", ["stochastik.mehrstufig"], [10]),
   ("Simulation", "Ein Zufallsversuch lässt sich mit Zufallszahlen nachspielen; viele Durchgänge ergeben einen Schätzwert.", ["stochastik.simulation"], []),
  ]),
 ],
 "Entdecker-Inseln": [
  ("Nur IB – Kür", [
   ("Mengen", "Schnittmenge: in beiden. Vereinigungsmenge: in mindestens einer.", ["mengen.grundbegriffe"], []),
   ("Aussagenlogik", "„Und“ ist nur wahr, wenn beide wahr sind. „Wenn A, dann B“ ist nur falsch, wenn A wahr und B falsch ist.", ["sonder.logik"], []),
   ("Graphen", "Jede Kante zählt an zwei Knoten. Ein Rundweg über alle Kanten geht nur, wenn jeder Knoten gerade viele Kanten hat.", ["sonder.graphentheorie"], []),
   ("Lineare Optimierung", "Der beste Wert liegt in einer Ecke des erlaubten Bereichs.", ["sonder.optimierung"], []),
   ("Schranken", "Ein gerundeter Messwert kann eine halbe Einheit größer oder kleiner sein.", ["zahlen.schranken"], [1]),
  ]),
 ],
}
ARBEIT = [
 ("Probe", "Setz ein und rechne nach."), ("Überschlag", "Erst grob, dann genau."), ("Einheiten", "Rechne mit Einheiten – die Einheit des Ergebnisses prüft die Rechnung."),
 ("Skizze", "Zeichne, was du weißt."), ("Ansatz", "Gegeben, gesucht, Rechnung, Antwort."), ("Begründen", "Nenne den Satz, dann wende ihn an. Für „stimmt nicht“ genügt ein Gegenbeispiel."),
 ("Ablesen und Darstellen", "Erst Achsen und Einheiten lesen, dann die Werte."), ("Formel anwenden", "Formel hinschreiben, einsetzen, auflösen."),
]
SCHULE = (("gym_by", "G"), ("rs_by", "R"), ("ib_myp", "I"))


def klassen(themen):
    out = []
    for key, kurz in SCHULE:
        ks = sorted({LISTE[t]["klasse"].get(key) for t in themen} - {None})
        out.append("–" if not ks else (str(ks[0]) if len(ks) == 1 else f"{ks[0]}–{ks[-1]}"))
    return out


# ── Prüfen: Vollständigkeit ──
erfasst = set()
namen = set()
zahl = {}
for planet, abschnitte in P.items():
    n = 0
    for _, gesetze in abschnitte:
        for name, satz, themen, regeln in gesetze:
            assert name not in namen and satz and themen, name
            namen.add(name)
            assert all(t in LISTE for t in themen), (name, themen)
            assert all(1 <= r <= len(SONNE) for r in regeln), name
            erfasst |= set(themen)
            n += 1
    zahl[planet] = n
sonnen_themen = {t for r in sonne.R for _, t, _, _ in r["bsp"]}
fehlt = sorted(set(LISTE) - erfasst - sonnen_themen)
assert fehlt == [], fehlt                       # jedes der 97 Themen der App ist von einem Gesetz oder einer Rechenregel erfasst
nur_sonne = sorted(set(LISTE) - erfasst)
# stimmt die Zuordnung Planet ↔ Gebiet der App? (Wie viele Themen eines Gesetzes liegen im gleichnamigen Gebiet?)
fremd = []
for planet, abschnitte in P.items():
    for _, gesetze in abschnitte:
        for name, _, themen, _ in gesetze:
            if not any(LISTE[t]["gebiet"] == planet for t in themen):
                fremd.append((planet, name, sorted({LISTE[t]["gebiet"] for t in themen})))
mehrfach = sum(1 for p, ab in P.items() for _, gs in ab for g in gs if len({LISTE[t]['gebiet'] for t in g[2]}) > 1)
GES = sum(zahl.values())
assert GES == len(namen)

# ── Muster-Planet: Fläche und Raum, ausgearbeitet ──
PI = "π"
M = [
 dict(name="Fläche messen", warum="Eine Fläche misst man, indem man sie mit gleich großen Quadraten auslegt und zählt. Ein Quadratdezimeter ist 10 cm lang und 10 cm breit, also passen 10 mal 10 = 100 Quadratzentimeter hinein. Deshalb ist die Umrechnungszahl bei Flächen 100 und nicht 10.",
      grenze="Bei Längen ist die Umrechnungszahl 10, bei Flächen 100, bei Volumen 1 000 – wer sie verwechselt, liegt um das Zehn- oder Hundertfache daneben. Von m² zu a und ha ist sie ebenfalls 100.",
      bild="Ein Quadratdezimeter in Originalgröße, in 10 mal 10 Kästchen geteilt; eines davon ist gefärbt: 1 cm².", baut=[], sonne=[1],
      bsp=[(5, "3 m² = 300 dm²", lambda: 3 * 100 == 300), (5, "2,5 dm² = 250 cm²", lambda: F(5, 2) * 100 == 250), (8, "5 000 cm² = 0,5 m²", lambda: F(5000, 100 * 100) == F(1, 2))]),
 dict(name="Rechteck", warum="In ein Rechteck mit 6 cm Länge und 4 cm Breite passen 4 Reihen mit je 6 Einheitsquadraten. Das sind 6 mal 4. Der Umfang ist der Weg einmal außen herum: zweimal die Länge und zweimal die Breite.",
      grenze="Beide Seiten müssen in derselben Einheit stehen. Fläche und Umfang sind verschiedene Größen: Die Fläche hat cm², der Umfang cm.",
      bild="Rechteck 6 mal 4 mit Kästchengitter; daneben dasselbe Rechteck nur als Rand, mit einem Pfeil, der außen herumläuft.", baut=["Fläche messen"], sonne=[],
      bsp=[(5, "6 cm lang, 4 cm breit: Fläche 24 cm², Umfang 20 cm", lambda: 6 * 4 == 24 and 2 * (6 + 4) == 20),
           (7, "Seiten x und x + 4: Fläche x · (x + 4) = x² + 4x", lambda: all(x * (x + 4) == x * x + 4 * x for x in range(1, 9))),
           (8, "Grundfläche eines Quaders oder Prismas", lambda: True),
           (9, "Fläche 60, eine Seite 4 länger als die andere: x² + 4x = 60, also x = 6", lambda: 6 * 6 + 4 * 6 == 60)]),
 dict(name="Fläche ist nicht Umfang", warum="Der Umfang zählt den Rand, die Fläche das Innere. Ein langes, schmales Rechteck hat viel Rand und wenig Inneres. Unter allen Rechtecken mit gleichem Umfang hat das Quadrat die größte Fläche.",
      grenze="Umgekehrt gilt es genauso: Gleiche Fläche heißt nicht gleicher Umfang.",
      bild="Zwei Rechtecke aus derselben Schnur gelegt: 5 mal 5 und 8 mal 2. Beide haben den Umfang 20, die Flächen 25 und 16.", baut=["Rechteck"], sonne=[],
      bsp=[(5, "5 · 5 und 8 · 2: beide Umfang 20, Flächen 25 und 16", lambda: 2 * (5 + 5) == 2 * (8 + 2) == 20 and 5 * 5 == 25 and 8 * 2 == 16),
           (8, "Umfang 20: Fläche x · (10 − x) ist am größten bei x = 5 (Realschule)", lambda: max(range(0, 11), key=lambda x: x * (10 - x)) == 5)]),
 dict(name="Zerlegen und Ergänzen", warum="Beim Zerschneiden geht nichts verloren und kommt nichts dazu. Deshalb darf man eine unbekannte Figur in bekannte Stücke zerlegen oder zu einer bekannten ergänzen und das Zuviel abziehen. Alle Flächenformeln dieses Planeten entstehen so aus dem Rechteck.",
      grenze="Der Umfang ändert sich beim Zerlegen sehr wohl.",
      bild="Eine L-Form: einmal in zwei Rechtecke zerschnitten, einmal zum großen Rechteck ergänzt, mit dem fehlenden Eck gestrichelt.", baut=["Rechteck"], sonne=[],
      bsp=[(5, "L-Form: 6 · 4 minus die Ecke 2 · 2 ergibt 20", lambda: 6 * 4 - 2 * 2 == 20 == 6 * 2 + 4 * 2),
           (6, "Parallelogramm: Dreieck links abschneiden, rechts ansetzen – es entsteht ein Rechteck", lambda: True),
           (9, "Pythagoras lässt sich durch Zerlegen zweier gleich großer Quadrate begründen", lambda: 3 * 3 + 4 * 4 == 5 * 5)]),
 dict(name="Parallelogramm", warum="Schneidet man an einer Seite ein Dreieck ab und setzt es an der anderen wieder an, entsteht ein Rechteck mit derselben Grundseite und derselben Höhe.",
      grenze="Gemeint ist die Höhe senkrecht zur Grundseite, nicht die schräge Seite. Die schräge Seite braucht man nur für den Umfang.",
      bild="Parallelogramm mit gestrichelter Höhe; das abgeschnittene Dreieck wandert mit einem Pfeil auf die andere Seite.", baut=["Zerlegen und Ergänzen"], sonne=[],
      bsp=[(6, "Grundseite 8 cm, Höhe 5 cm: 40 cm² – egal, wie lang die schräge Seite ist", lambda: 8 * 5 == 40),
           (8, "Fläche 40 und Grundseite 8: Höhe 40 : 8 = 5", lambda: F(40, 8) == 5)]),
 dict(name="Dreieck", warum="Zwei gleiche Dreiecke lassen sich immer zu einem Parallelogramm zusammenlegen. Ein Dreieck ist also ein halbes Parallelogramm mit derselben Grundseite und Höhe.",
      grenze="Das „geteilt durch 2“ wird am häufigsten vergessen. Bei stumpfen Dreiecken liegt die Höhe außerhalb – die Formel gilt trotzdem.",
      bild="Ein Dreieck und sein gedrehter Zwilling ergeben ein Parallelogramm; eines der beiden ist gefärbt.", baut=["Parallelogramm"], sonne=[],
      bsp=[(6, "Grundseite 14 cm, Höhe 15 cm: 14 · 15 : 2 = 105 cm²", lambda: F(14 * 15, 2) == 105),
           (8, "Fläche 36 und Grundseite 9: erst mal 2, dann durch 9, Höhe 8", lambda: F(2 * 36, 9) == 8),
           (9, "Rechtwinklig mit den Katheten 6 und 8: 24 – die Katheten sind Grundseite und Höhe", lambda: F(6 * 8, 2) == 24)]),
 dict(name="Trapez", warum="Zwei gleiche Trapeze ergeben zusammen ein Parallelogramm mit der Grundseite a + c. Ein Trapez ist die Hälfte davon. Anders gesagt: Man rechnet mit einem Rechteck, das so breit ist wie der Mittelwert der beiden parallelen Seiten.",
      grenze="a und c sind die parallelen Seiten, nicht irgendwelche. Die Klammer um a + c ist nötig.",
      bild="Trapez und gedrehter Zwilling als Parallelogramm; darunter das gleich große Rechteck mit der mittleren Breite.", baut=["Parallelogramm"], sonne=[4],
      bsp=[(6, "a = 7, c = 11, h = 6: (7 + 11) · 6 : 2 = 54", lambda: F((7 + 11) * 6, 2) == 54),
           (8, "Fläche 60, a = 9, c = 11: Höhe 2 · 60 : 20 = 6", lambda: F(2 * 60, 9 + 11) == 6)]),
 dict(name="Drachenviereck und Raute", warum="Die Diagonalen stehen senkrecht aufeinander. Das umschließende Rechteck hat die Seiten e und f und ist genau doppelt so groß wie das Viereck.",
      grenze="Gilt nur, wenn die Diagonalen senkrecht aufeinander stehen – also nicht für jedes Viereck.",
      bild="Drachen im Rechteck: Die vier Ecken-Dreiecke außen sind genauso groß wie die vier innen.", baut=["Dreieck"], sonne=[],
      bsp=[(6, "Diagonalen 8 cm und 5 cm: 8 · 5 : 2 = 20 cm²", lambda: F(8 * 5, 2) == 20)]),
 dict(name="Kreis", warum="Bei jedem Kreis ist der Umfang gleich oft so lang wie der Durchmesser: etwa 3,14-mal. Diese Zahl heißt π. Schneidet man den Kreis in viele Tortenstücke und legt sie abwechselnd nebeneinander, entsteht fast ein Rechteck: so hoch wie der Radius, so breit wie der halbe Umfang – also π · r mal r.",
      grenze="r ist der Radius, nicht der Durchmesser. Doppelter Radius: doppelter Umfang, aber vierfache Fläche. π ist kein Bruch; 3,14 ist gerundet.",
      bild="Kreis in zwölf Tortenstücke geschnitten und zum „Rechteck“ umgelegt; an den Seiten stehen r und π · r.", baut=["Rechteck", "Zerlegen und Ergänzen"], sonne=[8],
      bsp=[(8, f"r = 5 cm: Umfang 10 · {PI} ≈ 31,4 cm, Fläche 25 · {PI} ≈ 78,5 cm²", lambda: 2 * 5 == 10 and 5 ** 2 == 25 and round(10 * 3.14159, 1) == 31.4 and round(25 * 3.14159, 1) == 78.5),
           (8, f"Radius von 3 auf 6: Fläche von 9 · {PI} auf 36 · {PI} – das Vierfache", lambda: 6 ** 2 == 4 * 3 ** 2),
           (10, "Grundfläche von Zylinder und Kegel", lambda: True)]),
 dict(name="Kreisausschnitt", warum="Ein Viertelkreis hat ein Viertel des Umfangs und ein Viertel der Fläche. Für jeden anderen Winkel gilt dasselbe mit dem Anteil am vollen Winkel von 360°.",
      grenze="Der Bogen ist nur der gekrümmte Teil; zum Umfang des Ausschnitts kommen zwei Radien dazu.",
      bild="Pizza mit einem herausgezogenen Stück; am Stück stehen der Winkel 90° und „ein Viertel“.", baut=["Kreis"], sonne=[11],
      bsp=[(8, f"90° bei r = 4: Bogen 2 · {PI}, Fläche 4 · {PI}", lambda: F(90, 360) * 2 * 4 == 2 and F(90, 360) * 4 ** 2 == 4)]),
 dict(name="Volumen messen", warum="Ein Volumen misst man mit gleich großen Würfeln. In einen Würfel mit 1 dm Kantenlänge passen 10 mal 10 mal 10 = 1 000 Zentimeterwürfel. Ein Liter ist genau so ein Dezimeterwürfel.",
      grenze="Umrechnungszahl 1 000, nicht 10 und nicht 100. Milliliter und cm³ sind dasselbe.",
      bild="Dezimeterwürfel aus 1 000 kleinen Würfeln, eine Schicht (100 Stück) herausgezogen; daneben eine Literflasche.", baut=["Fläche messen"], sonne=[1],
      bsp=[(6, "2 dm³ = 2 000 cm³ = 2 Liter", lambda: 2 * 1000 == 2000), (6, "750 ml = 0,75 l = 750 cm³", lambda: F(750, 1000) == F(3, 4)), (8, "1 m³ = 1 000 Liter", lambda: 10 ** 3 == 1000)]),
 dict(name="Quader", warum="Auf dem Boden liegen Länge mal Breite Würfel. Davon stapelt man so viele Schichten, wie der Quader hoch ist.",
      grenze="Alle drei Kanten in derselben Einheit. Für den Würfel wird daraus a · a · a.",
      bild="Quader aus Schichten: unten eine Lage 5 mal 4 Würfel, darüber zwei weitere Lagen leicht angehoben.", baut=["Volumen messen", "Rechteck"], sonne=[],
      bsp=[(5, "Oberfläche und Kanten eines Quaders 5 · 4 · 3 (das Volumen kommt in Klasse 6)", lambda: True),
           (6, "5 cm · 4 cm · 3 cm = 60 cm³", lambda: 5 * 4 * 3 == 60),
           (6, "60 Liter in ein Becken mit 50 cm mal 40 cm Boden: 30 cm hoch", lambda: F(60 * 1000, 50 * 40) == 30)]),
 dict(name="Oberfläche", warum="Klappt man einen Körper auf, liegen alle seine Flächen nebeneinander: das Netz. Die Oberfläche ist deren Summe. Beim Quader sind es drei Paare gleicher Rechtecke.",
      grenze="Oberfläche ist eine Fläche (cm²), Volumen ein Rauminhalt (cm³). Bei offenen Gefäßen fehlt der Deckel.",
      bild="Quader und daneben sein aufgeklapptes Netz, die drei Paare in drei Farben.", baut=["Rechteck"], sonne=[4],
      bsp=[(5, "Quader 5 · 4 · 3: 2 · (20 + 15 + 12) = 94 cm²", lambda: 2 * (5 * 4 + 5 * 3 + 4 * 3) == 94),
           (8, "Zylinder: zwei Kreise und ein Rechteck als Mantel", lambda: True)]),
 dict(name="Netz und Schrägbild", warum="Ein Körper hat drei Ausdehnungen, das Papier nur zwei. Das Netz zeigt alle Flächen in wahrer Größe, aber nicht den Zusammenhang. Das Schrägbild zeigt den Zusammenhang, aber verkürzt die Kanten nach hinten. Für das Schrägbild gibt es eine feste Vereinbarung (meist 45° und halbe Länge).",
      grenze="Im Schrägbild darf man nach hinten laufende Längen und Winkel nicht abmessen.",
      bild="Würfel dreimal: als Körper, als Netz (Kreuzform) und als Schrägbild mit gestrichelten verdeckten Kanten.", baut=[], sonne=[],
      bsp=[(5, "Ein Würfelnetz besteht aus 6 Quadraten (Realschule Klasse 5)", lambda: True),
           (8, "Quader: 8 Ecken, 12 Kanten, 6 Flächen – 8 − 12 + 6 = 2", lambda: 8 - 12 + 6 == 2),
           (10, "Im Schrägbild einer Pyramide erscheint die Höhe unverkürzt, die Grundkante nach hinten halb", lambda: True)]),
 dict(name="Prisma und Zylinder", warum="Wie beim Quader: Auf der Grundfläche liegt eine Schicht, und davon stapelt man so viele, wie der Körper hoch ist. Welche Form die Grundfläche hat, ist dafür gleichgültig. Der Mantel ist abgerollt ein Rechteck: Umfang der Grundfläche mal Höhe.",
      grenze="Die Höhe steht senkrecht auf der Grundfläche. Die Grundfläche ist die Fläche, die oben und unten gleich ist – sie muss nicht unten liegen.",
      bild="Münzstapel als Zylinder und ein Stapel dreieckiger Bierdeckel als Prisma; daneben das abgerollte Etikett einer Dose.", baut=["Quader", "Dreieck", "Kreis"], sonne=[],
      bsp=[(6, "Quader ist der einfachste Fall: Grundfläche 20 cm², Höhe 3 cm, 60 cm³", lambda: 20 * 3 == 60),
           (8, "Dreiecksprisma: Grundfläche 24 cm², Höhe 10 cm, Volumen 240 cm³", lambda: 24 * 10 == 240),
           (8, f"Zylinder r = 3, h = 10: Volumen 90 · {PI}, Mantel 60 · {PI}", lambda: 3 ** 2 * 10 == 90 and 2 * 3 * 10 == 60)]),
 dict(name="Satz von Cavalieri", warum="Verschiebt man in einem Münzstapel die Münzen gegeneinander, wird der Stapel schief – aber es bleiben dieselben Münzen. Zwei Körper, die auf jeder Höhe gleich große Schnittflächen haben, haben deshalb dasselbe Volumen.",
      grenze="Die Schnittflächen müssen auf jeder Höhe gleich groß sein, nicht nur unten und oben. Die Oberfläche ändert sich beim Schiefstellen.",
      bild="Ein gerader und ein schiefer Münzstapel aus denselben Münzen.", baut=["Prisma und Zylinder"], sonne=[],
      bsp=[(8, "Ein schiefes Prisma mit Grundfläche 24 cm² und Höhe 10 cm hat ebenfalls 240 cm³", lambda: 24 * 10 == 240)]),
 dict(name="Pyramide und Kegel", warum="Ein Würfel lässt sich in drei gleiche Pyramiden zerlegen, deren Spitzen in einer Ecke zusammenlaufen. Jede füllt also ein Drittel. Mit Cavalieri gilt das für jede Pyramide und jeden Kegel: ein Drittel des Prismas oder Zylinders mit gleicher Grundfläche und Höhe.",
      grenze="Die Höhe geht senkrecht von der Spitze zur Grundfläche – nicht entlang der schrägen Seitenkante oder Mantellinie.",
      bild="Ein Kegel wird dreimal mit Wasser gefüllt und in einen Zylinder mit gleicher Grundfläche und Höhe gegossen: genau voll.", baut=["Prisma und Zylinder", "Satz von Cavalieri"], sonne=[10],
      bsp=[(10, "Pyramide: Grundfläche 36 cm², Höhe 10 cm, Volumen 120 cm³ (Realschule Klasse 9)", lambda: F(36 * 10, 3) == 120),
           (10, f"Kegel r = 3, h = 4: Volumen 12 · {PI}; Mantellinie 5 (Pythagoras), Mantel 15 · {PI}", lambda: F(3 ** 2 * 4, 3) == 12 and 3 * 3 + 4 * 4 == 5 * 5 and 3 * 5 == 15)]),
 dict(name="Kugel", warum="Eine Halbkugel hat dasselbe Volumen wie ein Zylinder gleicher Höhe, aus dem ein Kegel herausgebohrt ist – das zeigt Cavalieri. Daraus folgen zwei Drittel des umschließenden Zylinders für die ganze Kugel. Die Oberfläche ist genau viermal so groß wie der größte Kreis durch die Kugel.",
      grenze="Hoch 3 beim Volumen, hoch 2 bei der Oberfläche. Doppelter Radius: achtfaches Volumen.",
      bild="Kugel in einem genau passenden Zylinder: Sie füllt zwei Drittel davon.", baut=["Kreis", "Pyramide und Kegel"], sonne=[8],
      bsp=[(10, f"r = 3: Volumen 36 · {PI}, Oberfläche 36 · {PI} (Realschule Klasse 9)", lambda: F(4, 3) * 3 ** 3 == 36 and 4 * 3 ** 2 == 36),
           (10, "Radius verdoppelt: Volumen mal 8", lambda: 2 ** 3 == 8)]),
 dict(name="Lage im Raum", warum="In der Ebene schneiden sich zwei Geraden oder sie sind parallel. Im Raum gibt es eine dritte Möglichkeit: Sie laufen aneinander vorbei, ohne parallel zu sein. Am Quader sieht man alle drei Fälle an den Kanten.",
      grenze="Windschief gibt es nur im Raum. Im Schrägbild können sich windschiefe Geraden scheinbar schneiden.",
      bild="Quader mit drei Kantenpaaren in drei Farben: parallel, schneidend, windschief.", baut=["Netz und Schrägbild"], sonne=[],
      bsp=[(10, "Am Quader: Eine Bodenkante und die Deckenkante quer darüber sind windschief (Realschule Klasse 7)", lambda: True)]),
]
planet_gesetze = [g for _, gs in P["Fläche und Raum"] for g in gs]
assert [m["name"] for m in M] != [] and {m["name"] for m in M} == {g[0] for g in planet_gesetze}
pos = {m["name"]: i for i, m in enumerate(M)}
for m in M:
    assert all(b in pos and pos[b] < pos[m["name"]] for b in m["baut"]), (m["name"], m["baut"])
    for k, text, probe in m["bsp"]:
        assert probe() is True, (m["name"], text)
SATZ = {g[0]: g for g in planet_gesetze}
n_bsp = sum(len(m["bsp"]) for m in M)

# ── Schreiben: Inhaltsverzeichnis ──
ORT = {"Zahlen": "innerster Planet", "Algebra": "zweiter Planet", "Geld und Verhältnisse": "dritter Planet", "Geometrie": "vierter Planet", "Fläche und Raum": "fünfter Planet",
       "Funktionen": "sechster Planet", "Daten und Zufall": "siebter Planet", "Entdecker-Inseln": "Kleinplaneten am Rand"}
verz = []
for planet, abschnitte in P.items():
    verz.append(f"\n### {planet} – {zahl[planet]} Gesetze ({ORT[planet]})\n")
    verz.append("| Nr. | Gesetz | In einem Satz | G | R | I | braucht aus der Sonne |")
    verz.append("|---|---|---|---|---|---|---|")
    kurz = "".join(w[0] for w in planet.replace("und ", "").split())[:2].upper() if planet != "Funktionen" else "FU"
    kurz = {"Zahlen": "Z", "Algebra": "A", "Geld und Verhältnisse": "V", "Geometrie": "G", "Fläche und Raum": "F", "Funktionen": "U", "Daten und Zufall": "D", "Entdecker-Inseln": "E"}[planet]
    n = 0
    for abschnitt, gesetze in abschnitte:
        verz.append(f"| | *{abschnitt}* | | | | | |")
        for name, satz, themen, regeln in gesetze:
            n += 1
            g, r, i = klassen(themen)
            verz.append(f"| {kurz}{n} | **{name}** | {satz} | {g} | {r} | {i} | {', '.join(str(x) for x in regeln) or '–'} |")
uebersicht = "\n".join(f"| {p} | {zahl[p]} | {ORT[p]} | {', '.join(a for a, _ in ab)} |" for p, ab in P.items())
sonnenliste = "\n".join(f"{i}. **{r['name']}:** {r['merk']}" for i, r in enumerate(sonne.R, 1))
je_klasse = {}
for planet, abschnitte in P.items():
    for _, gesetze in abschnitte:
        for name, _, themen, _ in gesetze:
            ks = sorted({LISTE[t]["klasse"].get("gym_by") for t in themen} - {None})
            je_klasse.setdefault(ks[0] if ks else "nicht Gymnasium", []).append(name)
klassenzeile = " · ".join(f"Klasse {k}: {len(v)}" for k, v in sorted(je_klasse.items(), key=lambda x: (isinstance(x[0], str), x[0])) if not isinstance(k, str)) + f" · ohne Gymnasium-Zuordnung (nur Realschule oder IB): {len(je_klasse.get('nicht Gymnasium', []))}"
GESAMT = len(SONNE) + GES + len(ARBEIT)

open(os.path.join(HIER, "inhalt.md"), "w", encoding="utf-8").write(f"""# Gesetzbuch der Mathematik, Klasse 5 bis 10 – Landkarte und vollständiges Inhaltsverzeichnis

Mathe-Profi, 26.11.2026 (Auftrag 10, nach der Klarstellung „Gesetzbuch“). Erzeugt von `gesetzbuch.py`.
Für ChatGPT zum Angreifen und für den Designer als Stoff. Noch keine Darstellung.
**[G]** gesichert · **[A]** Annahme · **[M]** Meinung.

| Datei | Inhalt | Stand |
|---|---|---|
| `inhalt.md` (diese Datei) | Landkarte, ehrliche Gesamtzahl, alle Gesetze je Gebiet mit Klasse und Schulart | vollständig |
| `sonne.md` | die {len(SONNE)} Rechenregeln, ausgearbeitet | Muster 1 |
| `planet-flaeche-und-raum.md` | ein Planet, ausgearbeitet | Muster 2 |
| `gesetzbuch.py`, `bauen.py` | Daten, Prüfungen, Erzeugung | Lauf „OK“ |

## Die Antwort in einer Minute

- **Das Gesetzbuch hat {GESAMT} Einträge:** {len(SONNE)} Rechenregeln (die Sonne), {GES} Gesetze in sieben Gebieten und auf den Entdecker-Inseln (die Planeten), {len(ARBEIT)} Arbeitsweisen (eigener Ort).
- **Die Sonne** sind die Rechenregeln, weil sie in jedem Gebiet wiederkehren: {sum(1 for p in P.values() for _, gs in p for g in gs if g[3])} der {GES} Gesetze brauchen mindestens eine von ihnen ([G], gezählt).
- **Die Planeten sind die Gebiete der App.** Der Schnitt trägt – mit einer Einschränkung, siehe unten.
- Jedes der {len(LISTE)} Themen der App ist von mindestens einem Gesetz oder einer Rechenregel erfasst ([G], `gesetzbuch.py` prüft es).
- **Ehrlich zur Zahl:** {GES} ist die Zahl der Gesetze, wie ich sie geschnitten habe. Manche Einträge bündeln mehrere Formeln (die drei binomischen Formeln, die drei Potenzgesetze, vier Kongruenzsätze). Zählt man jede Formel einzeln, sind es deutlich mehr. Wer feiner oder gröber schneidet, kommt auf eine andere Zahl; an der Größenordnung ändert das nichts.

## Die Landkarte

| Ort | Gesetze | Lage | Abschnitte |
|---|---|---|---|
| **Sonne: Rechenregeln** | {len(SONNE)} | Mitte | Zahlen · Klammern und Potenzen · Brüche und Verhältnis · Gleichungen |
{uebersicht}
| **Arbeitsweisen** | {len(ARBEIT)} | eigener Ort – Vorschlag: die Raumstation, die jeden Planeten anfliegt | – |

**Trägt der Schnitt „Planet = Gebiet der App“?** Ja, mit drei Anmerkungen:
1. **Zahlen und Algebra liegen der Sonne am nächsten.** Viele ihrer Gesetze sind Rechenregeln in einem bestimmten Gewand oder folgen aus ihnen (Spalte „braucht aus der Sonne“). Das ist kein Fehler des Schnitts, sondern der Grund für die Reihenfolge der Planeten: von innen (nah am Rechnen) nach außen (eigene Sätze).
2. **Die Grenzen sind an wenigen Stellen unscharf.** {len(fremd)} Gesetz steht bei mir auf einem anderen Planeten als alle seine Themen in der App ([G], Liste unten); weitere {mehrfach} Gesetze greifen auf Themen aus zwei Gebieten zu (zum Beispiel die Hyperbel: Funktionen und Verhältnisse). Ich habe nach dem Inhalt geordnet, nicht nach dem Flug.
3. **Die Entdecker-Inseln** sind kein Gebiet, sondern fünf einzelne IB-Themen. Im Gesetzbuch sind sie Kleinplaneten am Rand, ausdrücklich Kür.

Wann die Gesetze dazukommen (Gymnasium, erste Klasse, in der das Gesetz vorkommt) [G]: {klassenzeile}.

## Die Sonne: {len(SONNE)} Rechenregeln

{sonnenliste}

Ausgearbeitet in `sonne.md`: je Regel Merksatz, Warum, Wo es nicht gilt, ein Beispiel je Klasse, Aufbau, Bild.

## Das vollständige Inhaltsverzeichnis

Spalten **G / R / I**: Klasse, in der das Gesetz laut App vorkommt – Gymnasium Bayern / Realschule Bayern (Wahlpflichtfächergruppe I) / IB-MYP-Jahr. „5–8“ heißt: Es kommt in mehreren Themen von Klasse 5 bis 8 vor. „–“ heißt: in dieser Schulart nicht zugeordnet.
Die Zahlen in der letzten Spalte sind die Nummern der Rechenregeln.
{chr(10).join(verz)}

## Die Arbeitsweisen – eigener Ort

| Arbeitsweise | Merksatz |
|---|---|
{chr(10).join(f"| {n} | **{m}** |" for n, m in ARBEIT)}

Sie sind keine Gesetze, sondern Vorgehen, und gelten auf jedem Planeten. „Einheiten“ ist neu dabei, wie im Auftrag genannt.

## Was bewusst nicht im Gesetzbuch steht

- **Rechenverfahren** (schriftliches Malnehmen und Teilen, Heron-Verfahren, Konstruktionsschritte): Das sind Abläufe, keine Gesetze. Sie gehören in die Lernreise.
- **Reine Begriffe** (Was ist ein Trapez, was ist ein Ereignis): nur dort aufgenommen, wo aus dem Begriff eine Regel folgt.
- **Einzelne Formeln ohne eigene Idee** (Kreisring, Kreisabschnitt, Mantel der Pyramide): Sie entstehen aus den aufgeführten Gesetzen durch Zerlegen.

## Gesetze, die auf einem anderen Planeten stehen als ihr Thema in der App

| Planet im Gesetzbuch | Gesetz | Gebiet des Themas in der App |
|---|---|---|
{chr(10).join(f"| {p} | {n} | {', '.join(g)} |" for p, n, g in fremd)}

## Vorschlag für die weitere Ausarbeitung

1. Diese Datei, `sonne.md` und `planet-flaeche-und-raum.md` an ChatGPT (Schritt 2).
2. Nach dem Einarbeiten die übrigen Planeten in dieser Reihenfolge [M]: Geometrie (dort sind beide Kinder als Nächstes), Geld und Verhältnisse, Daten und Zufall, Zahlen, Algebra, Funktionen, Entdecker-Inseln.
3. Je Planet dasselbe Muster wie beim Muster-Planeten: Merksatz, Warum, Wo es nicht gilt, Beispiele je Klasse, baut auf, Bild.

## Nicht geprüft

- **Lehrplan:** Klasse und Schulart stammen aus `inhalte/themenliste.json` (Zuordnung der App), **nicht aus den Lehrplänen an der Quelle**. Die bekannten Zweifel (vier Widersprüche zur App, mehrere Realschul-Zuordnungen) gelten hier weiter.
- **Vollständigkeit gegen den Lehrplan:** Geprüft ist, dass jedes Thema der App erfasst ist. Ob in den Lehrplänen ein Gesetz steht, zu dem die App kein Thema hat, ist nicht geprüft.
- Vollständigkeit innerhalb eines Themas: Ich habe die Titel aller Etappen gelesen, nicht jede Erklärung.
- Merksätze und Bilder nicht mit einem Kind erprobt; Bilder nur beschrieben.

## Annahmen

- Sonne = Rechenregeln, Planeten = Gebiete der App (Lesart des Projektleiters, hier übernommen und geprüft).
- Ein Gesetz ist, was fest gilt und was man wissen muss: Regel, Satz, Formel oder feste Vereinbarung.
- Reihenfolge der Planeten von innen nach außen nach Nähe zum Rechnen – ein Vorschlag für den Designer.
""")

# ── Schreiben: Muster-Planet ──
def gesetz_text(i, m):
    g, r, ib = klassen(SATZ[m["name"]][2])
    z = [f"### F{i} · {m['name']}", "", f"> **{SATZ[m['name']][1]}**", "", f"Gymnasium Klasse {g} · Realschule Klasse {r} · IB-Jahr {ib}", "",
         f"**Warum das gilt:** {m['warum']}", "", f"**Wo es nicht gilt:** {m['grenze']}", "", "| Klasse | Dasselbe Gesetz in diesem Jahr |", "|---|---|"]
    z += [f"| {k} | {text} |" for k, text, _ in m["bsp"]]
    auf = [f"F{pos[b] + 1} {b}" for b in m["baut"]] + [f"Rechenregel {s} {SONNE[s - 1]}" for s in m["sonne"]]
    z += ["", f"**Baut auf:** {' · '.join(auf) or 'nichts – Anfang'}", f"**Bild:** {m['bild']}"]
    return "\n".join(z)


kette = "\n".join(f"- **F{pos[m['name']] + 1} {m['name']}** braucht: {', '.join('F' + str(pos[b] + 1) + ' ' + b for b in m['baut'])}" for m in M if m["baut"])
open(os.path.join(HIER, "planet-flaeche-und-raum.md"), "w", encoding="utf-8").write(f"""# Gesetzbuch · Planet „Fläche und Raum“ – ausgearbeitet als Muster

Mathe-Profi, 26.11.2026. Erzeugt von `gesetzbuch.py`; {n_bsp} Beispiele, alle mit Zahlen nachgerechnet (Lauf „OK“).
So soll jeder Planet aussehen: je Gesetz Merksatz, Warum, Wo es nicht gilt, dasselbe Gesetz in mehreren Klassen, worauf es aufbaut, ein Bild.

## Der Planet in einer Minute

- **{len(M)} Gesetze:** zehn für Flächen, neun für Körper.
- **Eine Idee trägt alle:** *Messen heißt auslegen und zählen* – Flächen mit Einheitsquadraten, Körper mit Einheitswürfeln. Jede Formel ist eine Abkürzung für dieses Zählen.
- **Ein Gesetz erzeugt die anderen:** Aus dem Rechteck entstehen durch Zerlegen Parallelogramm, Dreieck, Trapez, Drachen und Kreis. Aus dem Quader entstehen durch Stapeln Prisma und Zylinder, daraus durch „ein Drittel“ Pyramide und Kegel.
- Der Planet begleitet die Kinder von Klasse 5 (Rechteck) bis Klasse 10 (Kugel).

## Aufbau

{kette}

Vorschlag für das Bild des Planeten [M]: **zwei Stammbäume nebeneinander** – links wächst aus dem Rechteck jede Flächenformel, rechts aus dem Quader jede Volumenformel; an jedem Ast steht, was getan wurde („abschneiden und ansetzen“, „halbieren“, „stapeln“, „ein Drittel“).

## Die Gesetze

{(chr(10) + chr(10)).join(gesetz_text(i, m) for i, m in enumerate(M, 1))}

## Nicht geprüft

- Klassen aus `inhalte/themenliste.json`, nicht aus dem Lehrplan an der Quelle. Die Zuordnung von Netzen und Schrägbildern (Realschule 5 und 7, Gymnasium 8 und 10) gehört zu den Zuordnungen, an denen ich zweifle.
- Die Begründungen sind Schul-Begründungen, keine Beweise (Kreisfläche über Tortenstücke, Pyramide über den Würfel, Kugel über Cavalieri).
- Bilder nur beschrieben. Merksätze nicht mit einem Kind erprobt.
""")
print(f"Sonne {len(SONNE)} · Planeten {GES} {zahl} · Arbeitsweisen {len(ARBEIT)} · gesamt {GESAMT}")
print("Themen nur über die Sonne erfasst:", nur_sonne)
print("Gesetze auf anderem Planeten als ihr Thema:", len(fremd))
print(f"Muster-Planet: {len(M)} Gesetze, {n_bsp} Beispiele")
print("OK")
