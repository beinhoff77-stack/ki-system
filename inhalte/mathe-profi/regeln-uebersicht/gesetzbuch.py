"""Mathe-Profi, Aufträge 10 und 11: Gesetzbuch – alle Gesetze je Gebiet (Ebene 2), tragende Ideen (Ebene 1), Verzeichnis.

Aufruf: python3 -I inhalte/mathe-profi/regeln-uebersicht/gesetzbuch.py
- hält alle Gesetze je Gebiet als Daten, jedes mit den Themen der App, in denen es vorkommt,
- leitet Klasse und Schulart je Gesetz aus inhalte/themenliste.json ab (Gymnasium, Realschule, IB),
- prüft, dass jedes Thema der App von mindestens einem Gesetz oder einer Rechenregel der Sonne erfasst ist,
- ordnet jedes Gesetz genau einer tragenden Idee seines Planeten zu (IDEEN) und prüft das,
- schreibt inhalt.md (Nachschlagen: Stichwörter und alle Gesetze) und ebene1.md (alle Sätze der Ebene 1).
Die ausgearbeiteten Planeten erzeugt planeten.py.
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
   ("Primzahlen und Primfaktoren", "Jede natürliche Zahl größer als 1 lässt sich in Primzahlen zerlegen – bis auf die Reihenfolge auf genau eine Weise.", ["zahlen.teilbarkeit"], []),
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
   ("Hoch null und negative Hochzahl", "Für a ≠ 0 gilt: a⁰ = 1, und eine negative Hochzahl heißt Kehrwert: a⁻ⁿ = 1 : aⁿ.", ["terme.potenzgesetze", "terme.potenzgesetze_ganzzahlig"], [8]),
   ("Zehnerpotenzen", "10ⁿ ist eine 1 mit n Nullen, 10⁻ⁿ hat n Stellen hinter dem Komma. Kilo, Mega, Milli, Mikro sind Zehnerpotenzen.", ["zahlen.potenzen_zehner", "zahlen.potenzen_basis"], [1, 8]),
   ("Potenzgesetze", "Mal bei gleicher Basis: Hochzahlen addieren. Mal bei gleicher Hochzahl: Basen malnehmen. Potenz einer Potenz: Hochzahlen malnehmen.", ["terme.potenzgesetze_natuerlich", "terme.potenzgesetze_ganzzahlig", "zahlen.rationale_exponenten"], [8]),
   ("Quadratwurzel", "Die Wurzel aus a ist die Zahl ab null, deren Quadrat a ist. Aus negativen Zahlen gibt es keine.", ["zahlen.wurzeln_basis"], [12]),
   ("Wurzelgesetze", "Für a ≥ 0 und b ≥ 0 ist Wurzel mal Wurzel die Wurzel aus dem Produkt; für b > 0 gilt dasselbe beim Teilen. Bei Plus und Minus gilt es nicht.", ["zahlen.reell"], [8]),
   ("Irrationale und reelle Zahlen", "Manche Zahlen sind kein Bruch, zum Beispiel √2. Brüche und diese Zahlen zusammen heißen reelle Zahlen.", ["zahlen.reell"], []),
   ("n-te Wurzel und Bruch als Hochzahl", "a hoch 1/n ist die n-te Wurzel aus a.", ["zahlen.rationale_exponenten"], [8, 12]),
   ("Logarithmus", "Für b > 0, b ≠ 1 und x > 0 ist der Logarithmus von x zur Basis b die Hochzahl, mit der aus b die Zahl x wird. Aus Mal wird Plus, aus Hoch wird Mal.", ["gleichungen.exponential", "funktionen.exponential_log"], [8, 12]),
  ]),
 ],
 "Algebra": [
  ("Terme", [
   ("Term und Variable", "Ein Buchstabe steht für eine Zahl. Die zuletzt ausgeführte Rechnung gibt dem Term seinen Namen.", ["terme.aufstellen"], [4]),
   ("Gleichwertige Terme", "Zwei Terme sind gleichwertig, wenn sie für jede Zahl ihrer gemeinsamen Definitionsmenge denselben Wert haben.", ["terme.umformen"], []),
   ("Summe mal Summe", "Jedes Glied der ersten Klammer mal jedes Glied der zweiten.", ["terme.umformen"], [6]),
   ("Binomische Formeln", "(a + b)² = a² + 2ab + b² · (a − b)² = a² − 2ab + b² · (a + b)(a − b) = a² − b²", ["terme.umformen", "terme.quadratische_extreme"], [6]),
   ("Definitionsmenge", "Ein Nenner darf nie null sein. Diese Zahlen werden vorher ausgeschlossen.", ["terme.bruchterme", "gleichungen.bruch", "funktionen.gebrochen"], [14]),
   ("Bruchterme", "Mit Bruchtermen rechnet man wie mit Brüchen: erst faktorisieren, dann kürzen.", ["terme.bruchterme"], [9, 10]),
   ("Kleinster und größter Wert", "(x − d)² + e hat den kleinsten Wert e; er wird bei x = d erreicht.", ["terme.quadratische_extreme"], [6]),
  ]),
  ("Gleichungen ersten Grades", [
   ("Äquivalenzumformung", "Dieselbe umkehrbare Rechnung auf beiden Seiten ändert die Lösungsmenge nicht. Haupteintrag: Rechenregel 13 „Gleichung als Waage“.", ["gleichungen.einfach", "gleichungen.linear"], [13]),
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
   ("Lösungsformel", "a·x² + b·x + c = 0 mit a ≠ 0 hat die Lösungen x = (−b ± √(b² − 4ac)) : (2a). Der Ausdruck unter der Wurzel entscheidet: positiv zwei Lösungen, null eine, negativ keine.", ["gleichungen.quadratisch"], [12]),
   ("Wurzelgleichungen", "Quadrieren kann falsche Lösungen erzeugen. Die Probe ist Pflicht.", ["gleichungen.wurzel"], [12]),
   ("Potenzgleichungen", "xⁿ = c: bei ungerader Hochzahl genau eine Lösung. Bei gerader Hochzahl zwei Lösungen für c > 0, eine für c = 0, keine für c < 0.", ["gleichungen.potenz"], [3, 12]),
   ("Exponentialgleichungen", "Gleiche Basis: Hochzahlen gleichsetzen. Sonst hilft der Logarithmus.", ["gleichungen.exponential"], [12]),
   ("Polynomgleichungen", "Ausklammern oder x² ersetzen. Eine doppelte Lösung berührt die Achse nur.", ["gleichungen.polynom"], [6, 14]),
  ]),
 ],
 "Geld und Verhältnisse": [
  ("Größen", [
   ("Größe und Einheit", "Eine Größe ist Zahl mal Einheit. Umrechnungszahlen: Längen 10 (m zu km: 1 000), Massen 1 000, Zeit 60 (Tag zu Stunde: 24).", ["groessen.einheiten"], [1]),
   ("Maßstab", "1 : n heißt: 1 cm im Plan sind n cm in Wirklichkeit.", ["groessen.einheiten"], [11]),
  ]),
  ("Proportionalität", [
   ("Direkte Proportionalität", "Doppelt so viel von dem einen, doppelt so viel von dem anderen. Der Quotient bleibt gleich.", ["groessen.proportional", "funktionen.linear"], [11]),
   ("Dreisatz", "Erst auf eins, dann auf viele. Haupteintrag: Rechenregel 11 „Verhältnis (Dreisatz)“.", ["groessen.proportional"], [11]),
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
   ("Parallel, senkrecht, Abstand", "Der Abstand eines Punktes von einer Geraden ist die Länge des Lots – das ist die kürzeste Verbindung.", ["geometrie.grundbegriffe"], []),
   ("Winkelarten", "Voller Winkel 360°, gestreckter 180°, rechter 90°.", ["geometrie.grundbegriffe", "geometrie.winkel"], []),
   ("Scheitel- und Nebenwinkel", "Scheitelwinkel sind gleich groß. Nebenwinkel ergeben zusammen 180°.", ["geometrie.winkel", "geometrie.winkelsaetze"], []),
   ("Stufen- und Wechselwinkel", "An parallelen Geraden sind Stufenwinkel und Wechselwinkel gleich groß – und umgekehrt.", ["geometrie.winkelsaetze"], []),
   ("Winkelsumme", "Im Dreieck 180°, im Viereck 360°, im n-Eck (n − 2) mal 180°. Ein Außenwinkel ist so groß wie die beiden anderen Innenwinkel zusammen.", ["geometrie.winkelsaetze"], []),
  ]),
  ("Figuren und Konstruktion", [
   ("Besondere Vierecke", "Quadrat, Rechteck, Raute, Parallelogramm, Trapez, Drachenviereck: Jedes hat seine festen Eigenschaften.", ["geometrie.grundbegriffe", "geometrie.konstruktion"], []),
   ("Ortslinien", "Kreis: gleich weit von einem Punkt. Mittelsenkrechte: gleich weit von zwei Punkten. Winkelhalbierende: gleich weit von zwei Schenkeln.", ["geometrie.ortslinien", "abbildungen.kongruenz"], []),
   ("Gleichschenkliges Dreieck", "Gleiche Schenkel, gleiche Basiswinkel – und umgekehrt. Gleichseitig: dreimal 60°.", ["geometrie.konstruktion"], []),
   ("Kongruenzsätze", "Drei passende Angaben legen ein Dreieck fest: SSS, SWS, WSW, SsW (der Winkel liegt der längeren Seite gegenüber). Zwei Seiten sind zusammen immer länger als die dritte.", ["geometrie.konstruktion"], []),
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
   ("Satz des Pythagoras", "Im rechtwinkligen Dreieck mit den Katheten a, b und der Hypotenuse c gilt a² + b² = c² – und nur dort.", ["trigo.pythagoras"], [12]),
   ("Sinus, Kosinus, Tangens", "Sinus = Gegenkathete durch Hypotenuse, Kosinus = Ankathete durch Hypotenuse, Tangens = Gegenkathete durch Ankathete.", ["trigo.rechtwinklig"], [11]),
   ("Zusammenhänge der Winkelfunktionen", "sin² α + cos² α = 1. Für cos α ≠ 0 gilt tan α = sin α : cos α.", ["trigo.rechtwinklig"], []),
   ("Einheitskreis", "Am Kreis mit Radius 1 sind Kosinus und Sinus die Koordinaten des Punktes – für jeden Winkel.", ["trigo.allgemein"], []),
   ("Sinussatz und Kosinussatz", "In jedem Dreieck: Seite durch Sinus des Gegenwinkels ist für alle drei gleich. Der Kosinussatz ist Pythagoras mit Korrektur.", ["trigo.allgemein"], []),
   ("Additionstheoreme", "Der Sinus einer Summe ist nicht die Summe der Sinus: sin(α + β) = sin α · cos β + cos α · sin β.", ["trigo.allgemein"], []),
   ("Winkel aus Sinus oder Kosinus", "Zu einem Wert gehören in einer vollen Drehung meist zwei Winkel.", ["gleichungen.trig"], [12]),
  ]),
 ],
 "Fläche und Raum": [
  ("Flächen", [
   ("Fläche messen", "Flächeninhalt heißt: Wie viele Einheitsquadrate passen hinein? Wird die Längeneinheit zehnmal kleiner, braucht man 100-mal so viele.", ["messen.flaechen"], [1]),
   ("Rechteck", "Fläche = Länge mal Breite. Umfang = einmal außen herum.", ["messen.flaechen"], []),
   ("Fläche ist nicht Umfang", "Derselbe Rand kann verschieden viel Fläche einschließen.", ["messen.flaechen", "terme.quadratische_extreme"], []),
   ("Zerlegen und Ergänzen", "Lückenlos und ohne Überlappung neu legen: Der Flächeninhalt bleibt, der Umfang kann sich ändern.", ["messen.flaechen", "messen.flaechen_vielecke"], []),
   ("Parallelogramm", "Fläche = Grundseite mal zugehörige Höhe. Zu jeder gewählten Grundseite gehört ihre senkrechte Höhe.", ["messen.flaechen_vielecke"], []),
   ("Dreieck", "Fläche = Grundseite mal zugehörige Höhe, geteilt durch 2.", ["messen.flaechen_vielecke", "gleichungen.formeln"], []),
   ("Trapez", "Fläche = Mittelwert der beiden parallelen Seiten mal Höhe.", ["messen.flaechen_vielecke", "gleichungen.formeln"], []),
   ("Drachenviereck und Raute", "Bei senkrechten Diagonalen ist die Fläche ihr halbes Produkt.", ["messen.flaechen_vielecke"], []),
   ("Kreis", "Der Umfang misst π Durchmesser: u = 2 · π · r. Die Fläche ist π mal Radius zum Quadrat: A = π · r².", ["messen.kreisberechnung"], []),
   ("Kreisausschnitt", "Der Winkelanteil bestimmt den Anteil am Kreisbogen und an der Kreisfläche.", ["messen.kreisberechnung"], [11]),
  ]),
  ("Körper", [
   ("Volumen messen", "Volumen heißt: Wie viele Einheitswürfel passen hinein? Wird die Längeneinheit zehnmal kleiner, braucht man 1 000-mal so viele. 1 Liter = 1 dm³.", ["messen.volumen"], [1]),
   ("Quader", "Volumen = Länge mal Breite mal Höhe.", ["messen.volumen"], []),
   ("Oberfläche", "Die Oberfläche misst die gesamte Außenfläche. Beim Quader addierst du die sechs Rechtecksflächen.", ["messen.koerper_berechnung", "messen.flaechen_vielecke"], []),
   ("Netz und Schrägbild", "Das Netz zeigt die aufgefaltete Oberfläche; das Schrägbild zeigt den Körper räumlich.", ["messen.koerper_darstellung", "raum.schraegbilder"], []),
   ("Prisma und Zylinder", "Bei Prisma und Zylinder gilt V = G · h mit senkrechter Höhe. Beim geraden Körper ist der Mantel: Umfang der Grundfläche mal Höhe.", ["messen.prisma_zylinder"], []),
   ("Satz von Cavalieri", "Haben zwei Körper gleiche Höhe und in jeder Höhe gleich große parallele Schnittflächen, haben sie gleiches Volumen.", ["messen.prisma_zylinder"], []),
   ("Pyramide und Kegel", "Volumen = ein Drittel von Grundfläche mal Höhe. Mantel des geraden Kreiskegels: π · r · s (s = Mantellinie). Mantel der Pyramide: Summe der Seitendreiecke.", ["raum.pyramide_kegel_kugel"], []),
   ("Kugel", "Die Kugelhaut hat die Fläche von vier Großkreisen: O = 4 · π · r². Volumen: V = 4/3 · π · r³.", ["raum.pyramide_kegel_kugel"], []),
   ("Lage im Raum", "Zwei verschiedene Geraden im Raum sind parallel, schneiden sich oder sind windschief.", ["raum.schraegbilder"], []),
  ]),
 ],
 "Funktionen": [
  ("Grundbegriffe", [
   ("Funktion", "Zu jedem x gehört genau ein y.", ["funktionen.grundbegriffe"], []),
   ("Punktprobe", "Ein Punkt liegt auf dem Graphen, wenn seine Koordinaten die Gleichung erfüllen. Die Probe als Vorgehen: siehe Arbeitsweisen.", ["funktionen.grundbegriffe", "funktionen.quadratisch"], []),
   ("Nullstelle und Achsenabschnitt", "Eine Nullstelle ist ein x-Wert mit f(x) = 0. Den Schnitt mit der y-Achse liefert x = 0.", ["funktionen.grundbegriffe", "funktionen.gebrochen"], [13]),
   ("Schnittpunkt", "Im Schnittpunkt haben beide Funktionen denselben Wert: gleichsetzen.", ["funktionen.linear", "funktionen.quadratisch"], [13]),
   ("Graphen verschieben und strecken", "Plus e schiebt nach oben, (x − d) schiebt nach rechts, mal a streckt, ein Minus davor spiegelt.", ["funktionen.transformation", "funktionen.quadratisch", "funktionen.gebrochen", "funktionen.trig"], []),
   ("Umkehrfunktion", "x und y tauschen; der Graph wird an der Geraden y = x gespiegelt. Geht nur, wenn zu jedem y genau ein x gehört.", ["funktionen.umkehr", "funktionen.potenz"], [12]),
  ]),
  ("Funktionsarten", [
   ("Lineare Funktion", "y = m · x + t: m ist die Steigung (Höhenunterschied durch Längenunterschied), t der Abschnitt auf der y-Achse.", ["funktionen.linear"], [11]),
   ("Ursprungsgerade", "Proportional heißt: Gerade durch den Ursprung.", ["funktionen.linear"], [11]),
   ("Parallel und senkrecht", "Parallele Geraden haben dieselbe Steigung. Geraden mit den Steigungen m₁ und m₂ stehen senkrecht, wenn m₁ · m₂ = −1; eine waagerechte und eine senkrechte Gerade stehen ebenfalls senkrecht.", ["funktionen.linear"], []),
   ("Geradenscharen", "Ein Parameter in m dreht die Gerade, ein Parameter in t verschiebt sie.", ["funktionen.scharen", "funktionen.linear"], []),
   ("Hyperbel", "y = a : x: doppeltes x, halbes y. Der Graph kommt den Asymptoten beliebig nahe, erreicht sie aber nie.", ["funktionen.gebrochen", "groessen.indirekt"], [11]),
   ("Parabel", "y = a · (x − d)² + e hat den Scheitel (d | e). a entscheidet über Öffnung und Breite.", ["funktionen.quadratisch"], [6]),
   ("Potenzfunktionen", "Gerade Hochzahl: symmetrisch zur y-Achse. Ungerade Hochzahl: symmetrisch zum Ursprung.", ["funktionen.potenz"], [8]),
   ("Exponentialfunktion", "Exponentiell: In gleichen Schritten wird mit derselben Zahl malgenommen. Linear: Es kommt dieselbe Zahl dazu.", ["funktionen.exponential_log"], [8]),
   ("Logarithmusfunktion", "Sie ist die Umkehrung der Exponentialfunktion.", ["funktionen.exponential_log", "funktionen.umkehr"], [12]),
   ("Sinus- und Kosinusfunktion", "Sie wiederholen sich nach 360° (im Bogenmaß 2π). Die Amplitude ist die größte Auslenkung. 180° entsprechen π.", ["funktionen.trig"], []),
   ("Ganzrationale Funktionen", "Grad und Vorzeichen der höchsten Potenz bestimmen, wohin der Graph außen läuft. Die Produktform zeigt die Nullstellen.", ["funktionen.ganzrational"], [14]),
   ("Betragsfunktion", "Der Graph von |x| hat einen Knick. |x| = a hat für a > 0 die Lösungen a und −a, für a = 0 nur die Lösung 0, für a < 0 keine.", ["funktionen.betrag"], [2]),
   ("Folgen", "Arithmetisch: immer dieselbe Zahl dazu. Geometrisch: immer mit derselben Zahl mal.", ["funktionen.folgen", "funktionen.reihen"], []),
   ("Reihen", "Arithmetische Reihe: Anzahl mal Mittelwert aus erstem und letztem Glied. Für die geometrische gibt es eine eigene Summenformel.", ["funktionen.reihen"], []),
  ]),
 ],
 "Daten und Zufall": [
  ("Daten", [
   ("Häufigkeit", "Absolute Häufigkeit: wie oft. Relative Häufigkeit: Anzahl durch Gesamtzahl.", ["daten.darstellen", "stochastik.grundbegriffe"], [11]),
   ("Diagramme lesen", "Im Kreisdiagramm gehört zu jedem Anteil derselbe Anteil von 360°. Eine Achse, die nicht bei 0 beginnt, übertreibt Unterschiede.", ["daten.darstellen"], [11]),
   ("Mittelwert", "Alle Werte addieren, durch die Anzahl teilen.", ["daten.kennwerte"], []),
   ("Median, Modalwert, Spannweite", "Median: der mittlere Wert der geordneten Liste – bei gerader Anzahl der Mittelwert der beiden mittleren. Modalwert: der häufigste. Spannweite: größter minus kleinster.", ["daten.boxplot"], []),
   ("Mittelwert oder Median", "Ein Ausreißer zieht den Mittelwert stark mit; der Median ist robuster.", ["daten.boxplot"], []),
   ("Quartile und Boxplot", "Die Box enthält die mittlere Hälfte der Werte.", ["daten.boxplot"], []),
   ("Stichprobe", "Von einer Stichprobe darf man nur aufs Ganze schließen, wenn sie zufällig gezogen ist; je größer sie ist, desto genauer.", ["daten.stichproben"], [11]),
   ("Zusammenhang ist nicht Ursache", "Zwei Größen können zusammen steigen, ohne dass die eine die andere bewirkt.", ["daten.zweidimensional"], []),
   ("Streuung", "Die Standardabweichung ist die Wurzel aus dem Mittelwert der quadrierten Abweichungen vom Mittelwert – ein Maß für die typische Abweichung.", ["daten.standardabweichung"], [12]),
   ("Normalverteilung", "Etwa 68 % der Werte liegen höchstens eine Standardabweichung vom Mittelwert entfernt, 95 % höchstens zwei.", ["daten.normalverteilung"], []),
  ]),
  ("Zählen und Zufall", [
   ("Zählprinzip", "Die Möglichkeiten der einzelnen Stufen werden malgenommen.", ["stochastik.kombinatorik"], []),
   ("Ergebnis und Ereignis", "Ein Ereignis ist eine Menge von Ergebnissen.", ["stochastik.grundbegriffe"], []),
   ("Laplace-Wahrscheinlichkeit", "Günstige durch mögliche Ergebnisse – nur wenn alle gleich wahrscheinlich sind.", ["stochastik.grundbegriffe"], [11]),
   ("Gegenereignis", "Jede Wahrscheinlichkeit liegt zwischen 0 und 1. Gegenereignis: 1 minus die Wahrscheinlichkeit.", ["stochastik.grundbegriffe", "stochastik.mehrstufig"], []),
   ("Gesetz der großen Zahlen", "Bei vielen unabhängigen Wiederholungen desselben Versuchs liegt die relative Häufigkeit meist nahe bei der Wahrscheinlichkeit.", ["stochastik.grundbegriffe", "stochastik.simulation"], []),
   ("Additionssatz", "A oder B, einschließlich beider: P(A) + P(B) − P(A und B).", ["stochastik.verknuepft", "mengen.grundbegriffe"], []),
   ("Vierfeldertafel", "Zeilen und Spalten ergeben die Randsummen; ein Feld folgt aus den anderen.", ["stochastik.verknuepft"], []),
   ("Bedingte Wahrscheinlichkeit", "Für P(B) > 0: Unter der Bedingung B zählt nur noch, was in B liegt – P(A unter B) = P(A und B) : P(B). Unabhängig heißt: Die Bedingung ändert nichts.", ["stochastik.verknuepft", "stochastik.bedingt"], [11]),
   ("Pfadregeln", "Entlang eines Pfades malnehmen, mehrere Pfade addieren.", ["stochastik.mehrstufig"], [10]),
   ("Simulation", "Ein Zufallsversuch lässt sich mit Zufallszahlen nachspielen; viele Durchgänge ergeben einen Schätzwert.", ["stochastik.simulation"], []),
  ]),
 ],
 "Entdecker-Inseln": [
  ("Zusatzthemen – Kür", [
   ("Mengen", "Schnittmenge: in beiden. Vereinigungsmenge: in mindestens einer.", ["mengen.grundbegriffe"], []),
   ("Aussagenlogik", "„Und“ ist nur wahr, wenn beide wahr sind. „Wenn A, dann B“ ist nur falsch, wenn A wahr und B falsch ist.", ["sonder.logik"], []),
   ("Graphen", "Jede Kante zählt an zwei Knoten. Ein Rundweg über alle Kanten geht nur, wenn jeder Knoten gerade viele Kanten hat.", ["sonder.graphentheorie"], []),
   ("Lineare Optimierung", "Gibt es einen besten Wert, wird er in mindestens einer Ecke des erlaubten Bereichs erreicht; sind zwei Ecken gleich gut, ist es auch die ganze Kante dazwischen.", ["sonder.optimierung"], []),
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
sonnen_themen = {t for r in sonne.R for _, _, t, _, _ in r["bsp"]}
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

# ── Ebene 1: tragende Ideen je Planet. (Kurzname, Merksatz, [Gesetze]) – jedes Gesetz genau einmal ──
IDEEN = {
 "Zahlen": [
  ("Zahlengerade", "Jede Zahl hat genau einen Platz auf der Zahlengeraden – links ist kleiner.",
   ["Ordnung auf der Zahlengeraden", "Betrag und Gegenzahl", "Brüche vergleichen", "Irrationale und reelle Zahlen"]),
  ("Bündeln in Zehnern", "Zehn von einer Sorte ergeben eins von der nächstgrößeren.",
   ["Stellenwertsystem", "Runden", "Andere Zahlschriften", "Rechnen mit Komma", "Zehnerpotenzen"]),
  ("Bausteine", "Jede natürliche Zahl ab 2 ist aus Primzahlen gebaut.",
   ["Teiler und Vielfache", "Teilbarkeitsregeln", "Primzahlen und Primfaktoren", "ggT und kgV"]),
  ("Schreibweisen", "Bruch, Dezimalzahl und Prozent sind drei Schreibweisen derselben Zahl.",
   ["Bruch als Anteil", "Drei Schreibweisen einer Zahl", "Periodische Dezimalzahlen"]),
  ("Hoch und zurück", "Potenz, Wurzel und Logarithmus gehören zusammen: Die eine rechnet hoch, die beiden anderen fragen zurück.",
   ["Quadratzahlen", "Potenz mit negativer Basis", "Hoch null und negative Hochzahl", "Potenzgesetze", "Quadratwurzel", "Wurzelgesetze", "n-te Wurzel und Bruch als Hochzahl", "Logarithmus"]),
 ],
 "Algebra": [
  ("Term", "Ein Term ist eine Rechenvorschrift; gleichwertige Terme liefern für jede erlaubte Zahl dasselbe.",
   ["Term und Variable", "Gleichwertige Terme", "Summe mal Summe", "Binomische Formeln", "Kleinster und größter Wert"]),
  ("Erlaubte Zahlen", "Kläre zuerst, welche Zahlen du einsetzen darfst: Kein Nenner wird null, unter keiner Wurzel steht etwas Negatives.",
   ["Definitionsmenge", "Bruchterme", "Bruchgleichungen", "Wurzelgleichungen"]),
  ("Gleichung lösen", "Eine Gleichung lösen heißt: alle Zahlen finden, die sie wahr machen.",
   ["Äquivalenzumformung", "Wie viele Lösungen?", "Ungleichungen", "Intervalle", "Formeln umstellen", "Gleichungssystem mit zwei Unbekannten", "Gleichungssystem mit drei Unbekannten"]),
  ("Höherer Grad", "Bei höherem Grad: alles auf eine Seite bringen und in Faktoren zerlegen – oder die Gegenrechnung nutzen.",
   ["x² = a", "Faktorisieren", "Quadratische Ergänzung", "Lösungsformel", "Potenzgleichungen", "Exponentialgleichungen", "Polynomgleichungen"]),
 ],
 "Geld und Verhältnisse": [
  ("Größe", "Eine Größe ist Zahl mal Einheit – wechselt die Einheit, wechselt die Zahl.",
   ["Größe und Einheit", "Maßstab"]),
  ("Wert für eins", "Proportional heißt: Der Wert für eine Einheit bleibt immer gleich.",
   ["Direkte Proportionalität", "Dreisatz", "Verhältnisse", "Indirekte Proportionalität", "Änderungsrate"]),
  ("Prozent als Faktor", "Prozent heißt Hundertstel; um p Prozent verändern heißt mit einem Faktor malnehmen.",
   ["Grundgleichung der Prozentrechnung", "Wachstumsfaktor", "Zinsen", "Zinseszins"]),
 ],
 "Geometrie": [
  ("Winkel an Geraden", "An parallelen Geraden kehren dieselben Winkel wieder – deshalb ergeben die Winkel im Dreieck zusammen 180°.",
   ["Winkelarten", "Scheitel- und Nebenwinkel", "Stufen- und Wechselwinkel", "Winkelsumme"]),
  ("Gleicher Abstand", "Alle Punkte mit gleichem Abstand bilden eine Linie: Kreis, Mittelsenkrechte, Winkelhalbierende.",
   ["Koordinatensystem", "Parallel, senkrecht, Abstand", "Ortslinien", "Satz des Thales", "Tangente", "Umkreis und Inkreis"]),
  ("Deckungsgleich", "Spiegeln, Schieben und Drehen ändern weder Längen noch Winkel; drei passende Angaben legen ein Dreieck fest.",
   ["Besondere Vierecke", "Gleichschenkliges Dreieck", "Kongruenzsätze", "Satz und Kehrsatz", "Spiegeln, Verschieben, Drehen", "Symmetrie", "Vektoren", "Fläche mit Determinante", "Matrizen und Skalarprodukt"]),
  ("Ähnlich", "Ähnliche Figuren haben gleiche Winkel und alle Längen im selben Verhältnis.",
   ["Ähnlichkeit", "Strahlensätze", "Vergrößern mit Faktor k", "Schwerpunkt"]),
  ("Rechtwinkliges Dreieck", "Im rechtwinkligen Dreieck legen zwei Angaben alles fest: Pythagoras verbindet die Seiten, Sinus, Kosinus und Tangens verbinden Seiten und Winkel.",
   ["Satz des Pythagoras", "Sinus, Kosinus, Tangens", "Zusammenhänge der Winkelfunktionen", "Einheitskreis", "Sinussatz und Kosinussatz", "Additionstheoreme", "Winkel aus Sinus oder Kosinus"]),
 ],
 "Fläche und Raum": [
  ("Auslegen und zählen", "Messen heißt auslegen und zählen: Flächen mit Einheitsquadraten, Körper mit Einheitswürfeln.",
   ["Fläche messen", "Rechteck", "Fläche ist nicht Umfang", "Volumen messen", "Quader"]),
  ("Aus dem Rechteck", "Aus dem Rechteck entsteht jede Fläche: zerschneiden, neu legen, halbieren.",
   ["Zerlegen und Ergänzen", "Parallelogramm", "Dreieck", "Trapez", "Drachenviereck und Raute", "Kreis", "Kreisausschnitt"]),
  ("Aus dem Quader", "Aus dem Quader entsteht jeder Körper: Grundfläche mal Höhe – bei spitzen Körpern ein Drittel davon.",
   ["Prisma und Zylinder", "Satz von Cavalieri", "Pyramide und Kegel", "Kugel"]),
  ("Haut des Körpers", "Die Oberfläche ist die Haut des Körpers: Das Netz zeigt sie ausgebreitet, das Schrägbild zeigt den Körper im Raum.",
   ["Oberfläche", "Netz und Schrägbild", "Lage im Raum"]),
 ],
 "Funktionen": [
  ("Zuordnung", "Eine Funktion ordnet jedem x genau ein y zu; Tabelle, Graph und Gleichung zeigen dasselbe.",
   ["Funktion", "Punktprobe", "Nullstelle und Achsenabschnitt", "Schnittpunkt", "Umkehrfunktion"]),
  ("Wachstum", "Linear wächst in gleichen Schritten um gleich viel, exponentiell um den gleichen Faktor.",
   ["Lineare Funktion", "Ursprungsgerade", "Parallel und senkrecht", "Geradenscharen", "Exponentialfunktion", "Logarithmusfunktion", "Folgen", "Reihen"]),
  ("Gleichung und Form", "Die Gleichung verrät die Form des Graphen – und jede Änderung der Gleichung verschiebt oder streckt ihn.",
   ["Graphen verschieben und strecken", "Hyperbel", "Parabel", "Potenzfunktionen", "Sinus- und Kosinusfunktion", "Ganzrationale Funktionen", "Betragsfunktion"]),
 ],
 "Daten und Zufall": [
  ("Kennzahl", "Eine Kennzahl fasst viele Daten in einer Zahl zusammen – und verschweigt dabei immer etwas.",
   ["Häufigkeit", "Diagramme lesen", "Mittelwert", "Median, Modalwert, Spannweite", "Mittelwert oder Median", "Quartile und Boxplot", "Streuung", "Normalverteilung"]),
  ("Vom Teil aufs Ganze", "Von wenigen auf alle schließen geht nur, wenn zufällig und oft genug gezogen wurde.",
   ["Stichprobe", "Zusammenhang ist nicht Ursache", "Gesetz der großen Zahlen", "Simulation"]),
  ("Anteil", "Sind alle Ergebnisse gleich wahrscheinlich, ist die Wahrscheinlichkeit ein Anteil: günstige durch mögliche.",
   ["Zählprinzip", "Ergebnis und Ereignis", "Laplace-Wahrscheinlichkeit", "Gegenereignis", "Additionssatz"]),
  ("Stufen", "Bei mehreren Stufen: entlang eines Pfades malnehmen, verschiedene Pfade addieren.",
   ["Vierfeldertafel", "Bedingte Wahrscheinlichkeit", "Pfadregeln"]),
 ],
}
IDEE_VON = {}
for planet, ideen in IDEEN.items():
    assert 3 <= len(ideen) <= 5, planet
    soll = [g[0] for _, gs in P[planet] for g in gs]
    ist = [n for _, _, ns in ideen for n in ns]
    assert sorted(ist) == sorted(soll), (planet, set(soll) ^ set(ist), [n for n in ist if ist.count(n) > 1])   # jedes Gesetz genau einer Idee
    for nr, (kurz, merk, ns) in enumerate(ideen, 1):
        assert len(merk) <= 170, (kurz, len(merk))
        for n in ns:
            IDEE_VON[n] = (nr, kurz)
N_IDEEN = sum(len(v) for v in IDEEN.values())
EBENE1 = len(SONNE) + N_IDEEN
KURZ = {"Zahlen": "Z", "Algebra": "A", "Geld und Verhältnisse": "V", "Geometrie": "G", "Fläche und Raum": "F", "Funktionen": "U", "Daten und Zufall": "D", "Entdecker-Inseln": "E"}
NR = {}
for planet, abschnitte in P.items():
    n = 0
    for _, gesetze in abschnitte:
        for g in gesetze:
            n += 1
            NR[g[0]] = f"{KURZ[planet]}{n}"
# Einträge, die kein Gesetz im engen Sinn sind (Gegenprüfung): bleiben auffindbar, werden aber gekennzeichnet
ART_EINTRAG = {"Andere Zahlschriften": "Thema", "Diagramme lesen": "Verfahren", "Simulation": "Verfahren"}
# Doppelt vorkommende Inhalte: ein Haupteintrag, der andere verweist
VERWEIS = {"Äquivalenzumformung": "Rechenregel 13", "Dreisatz": "Rechenregel 11", "Punktprobe": "Arbeitsweise Probe (das Vorgehen)", "Stellenwertsystem": "Rechenregel 1"}
# Hinweise zur Klasse aus der Lehrplan-Kopie der App, wo sie der Themenliste widerspricht oder sie ergänzt
LP_HINWEIS = {
 "Bedingte Wahrscheinlichkeit": "Gymnasium 5–10: in der Lehrplan-Kopie der App kein Eintrag; laut Gegenprüfung Klasse 11",
 "Satz von Cavalieri": "Gymnasium: Klasse 10 (Lehrplan-Kopie der App, 10/5), nicht 8",
 "Mengen": "in der App keiner Klasse zugeordnet",
 "Vektoren": "in der Themenliste ohne Klasse; Lehrplan-Kopie der App: Realschule 7",
}
STICHWORT = [
 ("Abstand Punkt–Gerade, Lot", NR["Parallel, senkrecht, Abstand"]), ("Assoziativgesetz (Verbindungsgesetz)", "Rechenregel 5"), ("abc-Formel, Mitternachtsformel", NR["Lösungsformel"]),
 ("Distributivgesetz", "Rechenregel 6"), ("Dreisatz", "Rechenregel 11"), ("Kegelmantel", NR["Pyramide und Kegel"]), ("Kommutativgesetz (Vertauschungsgesetz)", "Rechenregel 5"),
 ("Kürzen", "Rechenregel 9"), ("Mantel von Prisma und Zylinder", NR["Prisma und Zylinder"]), ("Minus vor der Klammer", "Rechenregel 7"),
 ("Neutrale Zahlen: 0 beim Addieren, 1 beim Malnehmen", "Rechenregel 5"), ("Probe", "Arbeitsweise Probe"), ("Punkt vor Strich", "Rechenregel 4"),
 ("Pyramidenmantel", NR["Pyramide und Kegel"]), ("Prozent", NR["Grundgleichung der Prozentrechnung"]), ("Runden", NR["Runden"]), ("Waage", "Rechenregel 13"),
 ("Windschief", NR["Lage im Raum"]), ("Zinseszins", NR["Zinseszins"]),
]


def tab(text):
    return text.replace("|", "&#124;")


if __name__ == "__main__":
    verz = []
    for planet, abschnitte in P.items():
        verz.append(f"\n### {planet} – {zahl[planet]} Einträge\n")
        if planet in IDEEN:
            verz += [f"{i}. *{kurz}:* {merk}" for i, (kurz, merk, _) in enumerate(IDEEN[planet], 1)] + [""]
        verz += ["| Nr. | Gesetz | In einem Satz | Idee | G | R | I | Sonne | Hinweis |", "|---|---|---|---|---|---|---|---|---|"]
        for abschnitt, gesetze in abschnitte:
            verz.append(f"| | *{abschnitt}* | | | | | | | |")
            for name, satz, themen, regeln in gesetze:
                g, r, i = klassen(themen)
                hin = "; ".join(x for x in (ART_EINTRAG.get(name) and f"kein Gesetz, sondern {ART_EINTRAG[name]}", name in VERWEIS and f"Haupteintrag: {VERWEIS[name]}", LP_HINWEIS.get(name)) if x)
                verz.append(f"| {NR[name]} | **{name}** | {tab(satz)} | {IDEE_VON[name][0] if name in IDEE_VON else '–'} | {g} | {r} | {i} | {', '.join(str(x) for x in regeln) or '–'} | {hin} |")
    GESAMT = len(SONNE) + GES + len(ARBEIT)
    ebene1 = []
    for planet, ideen in IDEEN.items():
        ebene1.append(f"\n### {planet} – {len(ideen)} tragende Ideen\n")
        for i, (kurz, merk, ns) in enumerate(ideen, 1):
            ebene1.append(f"{i}. **{merk}**  \n   *{kurz}* – trägt {len(ns)} Gesetze: {', '.join(NR[n] + ' ' + n for n in ns)}")
    zaehl = " · ".join(f"{p} {len(v)}" for p, v in IDEEN.items())
    open(os.path.join(HIER, "ebene1.md"), "w", encoding="utf-8").write(f"""# Gesetzbuch · Ebene 1: alle Sätze zum Auswendigwissen

Mathe-Profi, 26.11.2026 (Auftrag 11). Erzeugt von `gesetzbuch.py`.

**Ebene 1 hat {EBENE1} Sätze:** {len(SONNE)} Rechenregeln (Sonne) und {N_IDEEN} tragende Ideen ({zaehl}). [G, gezählt]
Die Entdecker-Inseln haben keine tragende Idee; sie stehen nur in Ebene 2.
Jedes der {GES - zahl['Entdecker-Inseln']} Gesetze der sieben Planeten ist genau einer Idee zugeordnet ([G], `gesetzbuch.py` prüft es).

## Die Sonne – {len(SONNE)} Rechenregeln

{chr(10).join(f"{i}. **{r['merk']}**  {chr(10)}   *{r['name']}*" for i, r in enumerate(sonne.R, 1))}

## Die Planeten – {N_IDEEN} tragende Ideen
{chr(10).join(ebene1)}

## Was ich am Vorschlag des Projektleiters für Geometrie geändert habe

| Vorschlag | Urteil | Was daraus wurde |
|---|---|---|
| Winkelsumme 180° | trägt, aber ist selbst eine Folge | Idee 1 nennt die Ursache mit: gleiche Winkel an Parallelen – daraus folgt die Winkelsumme |
| Drei passende Angaben legen ein Dreieck fest | trägt | mit dem nächsten zu **einer** Idee „Deckungsgleich“ vereint: Beides sagt, wann zwei Figuren in allen Längen und Winkeln übereinstimmen |
| Spiegeln, Schieben, Drehen ändert weder Längen noch Winkel | trägt | siehe oben |
| Ähnliche Figuren | trägt | unverändert Idee 4 |
| Pythagoras | zu eng: ein einzelner Satz, der Sinus, Kosinus und Tangens nicht trägt | erweitert zu „Rechtwinkliges Dreieck: zwei Angaben legen alles fest“ |
| – (fehlte) | sechs Gesetze hatten keine Heimat: Abstand, Ortslinien, Thales, Tangente, Umkreis und Inkreis, Koordinatensystem | neue Idee 2 „Gleicher Abstand“ |

## Wo die Zuordnung nur lose passt [M]

- **Fläche und Raum, Idee 4:** „Lage im Raum“ (windschief) hat mit der Oberfläche nichts zu tun; es steht dort, weil es wie das Schrägbild vom Sehen im Raum handelt.
- **Geometrie, Idee 3:** „Fläche mit Determinante“ und „Matrizen und Skalarprodukt“ (nur Realschule) hängen nur über die Vektoren an der Idee. „Satz und Kehrsatz“ ist eher eine Denkweise als ein Geometrie-Gesetz.
- **Geometrie, Idee 2:** „Koordinatensystem“ ist ein Werkzeug; es steht dort, weil Abstände und Kreise darin beschrieben werden.
- **Geld und Verhältnisse, Idee 2:** Die indirekte Proportionalität ist das Gegenstück (das Produkt bleibt gleich), nicht ein Fall der Idee.
- **Daten und Zufall, Idee 2:** „Zusammenhang ist nicht Ursache“ passt nur als zweite Vorsichtsregel beim Schließen aus Daten.

## Nicht geprüft

- Ob die Sätze für ein Kind der Klasse 5 verständlich und merkbar sind – nicht erprobt.
- Die fünf übrigen Planeten (Zahlen, Algebra, Geld und Verhältnisse, Funktionen, Daten und Zufall) haben Ideen und Zuordnung, aber noch keine Zeichen-Vorgabe und keine Ausarbeitung.
""")
    open(os.path.join(HIER, "inhalt.md"), "w", encoding="utf-8").write(f"""# Gesetzbuch · Ebene 2: Nachschlagen – Stichwörter und alle Einträge

Mathe-Profi, 26.11.2026 (Auftrag 11, zweite Fassung nach der Gegenprüfung). Erzeugt von `gesetzbuch.py`.
**[G]** gesichert · **[A]** Annahme · **[M]** Meinung.

| Datei | Inhalt |
|---|---|
| `ebene1.md` | Ebene 1: die {EBENE1} Sätze zum Auswendigwissen ({len(SONNE)} Rechenregeln, {N_IDEEN} tragende Ideen) und die Zuordnung jedes Gesetzes |
| `sonne.md` | die {len(SONNE)} Rechenregeln ausgearbeitet, je mit Zeichen-Vorgabe |
| `planet-flaeche-und-raum.md`, `planet-geometrie.md` | zwei Planeten ausgearbeitet: Ideen mit Zeichen-Vorgabe, darunter jedes Gesetz |
| `inhalt.md` (diese Datei) | Ebene 2: Stichwörter und alle {GESAMT} Einträge |

## So ist Ebene 2 gedacht

Einstieg ist die **Suche** und daneben neun Türen: Sonne, sieben Gebiete, Arbeitsweisen. Kein Raster über alle Einträge.
Maßstab: Ein Kind findet „Kegelmantel“ und „Minus vor der Klammer“, ohne zu wissen, auf welchem Planeten sie stehen.

## Stichwörter, die auf einen anderen Eintrag führen

Für die Suche: Fachnamen und Formeln, die keinen eigenen Eintrag haben. Die Liste ist ein Anfang, nicht vollständig. [A]

| Suchwort | steht bei |
|---|---|
{chr(10).join(f"| {a} | {b} |" for a, b in sorted(STICHWORT))}

## Die Zahl, ehrlich

- {GESAMT} Einträge: {len(SONNE)} Rechenregeln, {GES} Einträge auf den Planeten und Inseln, {len(ARBEIT)} Arbeitsweisen. Das ist eine **Zählung meines Zuschnitts**, keine Naturkonstante: Manche Einträge bündeln mehrere Formeln.
- {len(ART_EINTRAG)} Einträge sind kein Gesetz, sondern Thema oder Verfahren ({', '.join(ART_EINTRAG)}); sie bleiben, damit das zugehörige Thema der App auffindbar ist, und sind gekennzeichnet.
- {len(VERWEIS)} Einträge sind Verweise auf einen Haupteintrag.
- Geprüft ist: Jedes der {len(LISTE)} Themen der App kommt in mindestens einem Eintrag vor. **Das beweist keine Vollständigkeit** – weder gegen den Lehrplan noch innerhalb eines Themas.

## Alle Einträge

Spalten **G / R**: Klasse laut Themenliste der App – Gymnasium Bayern / Realschule Bayern (Wahlpflichtfächergruppe I; II/III weicht ab, in den ausgearbeiteten Planeten eigens gezeigt).
Spalte **I**: IB-MYP-Jahr laut App. Das ist **Planung der App**, keine verbindliche Jahresfolge – das IB schreibt keine vor.
„5–8“: kommt in mehreren Themen von Klasse 5 bis 8 vor. „–“: in dieser Schulart laut App nicht. Spalte **Idee**: Nummer der tragenden Idee des Planeten. Spalte **Sonne**: Rechenregeln, die das Gesetz braucht.
{chr(10).join(verz)}

## Die Arbeitsweisen – eigener Ort

| Arbeitsweise | Merksatz |
|---|---|
{chr(10).join(f"| {n} | **{m}** |" for n, m in ARBEIT)}

## Einträge, die auf einem anderen Planeten stehen als ihr Thema in der App

| Planet im Gesetzbuch | Eintrag | Gebiet des Themas in der App |
|---|---|---|
{chr(10).join(f"| {p} | {n} | {', '.join(g)} |" for p, n, g in fremd)}

## Nicht geprüft

- **Lehrplan an der Quelle:** Der Abruf von LehrplanPLUS war in dieser Sitzung nicht möglich (keine Freigabe). Die Spalten G / R / I stammen aus `inhalte/themenliste.json`. Für die zwei ausgearbeiteten Planeten habe ich zusätzlich die Lehrplan-Kopie der App gelesen (Datenbank, nur lesend); für die übrigen fünf nicht.
- Vollständigkeit gegen den Lehrplan und innerhalb eines Themas.
- Die Sätze der fünf noch nicht ausgearbeiteten Planeten sind an den Stellen berichtigt, die die Gegenprüfung genannt hat; eine zweite Durchsicht aller Sätze steht aus.
""")
    print(f"Ebene 1: {EBENE1} Sätze ({len(SONNE)} + {N_IDEEN}) · Ebene 2: {GESAMT} Einträge {zahl}")
    print("OK")
