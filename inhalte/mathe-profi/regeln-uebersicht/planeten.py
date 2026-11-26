"""Mathe-Profi, Auftrag 11: zwei Planeten ausgearbeitet – Fläche und Raum, Geometrie.

Aufruf: python3 -I inhalte/mathe-profi/regeln-uebersicht/planeten.py
Nimmt Gesetze, Sätze und tragende Ideen aus gesetzbuch.py, ergänzt je Idee Begründung und Zeichen-Vorgabe und je Gesetz
Voraussetzung, häufigen Fehler, Verwandtes, Klasse je Schulart und nachgerechnete Beispiele. Schreibt planet-*.md.
Klassen (LP): aus der Lehrplan-Kopie der App gelesen (Datenbank, nur lesend), nicht aus LehrplanPLUS an der Quelle.
"""
import importlib.util
import io
import contextlib
import math
import os
import sys
from fractions import Fraction as F

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("gesetzbuch", os.path.join(HIER, "gesetzbuch.py"))
gb = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(gb)
Z, zeichnung_text, ART, SONNE = gb.sonne.Z, gb.sonne.zeichnung_text, gb.sonne.ART, gb.SONNE
SATZ = {g[0]: g for ab in gb.P.values() for _, gs in ab for g in gs}
PI = math.pi
NG = "nicht genannt"


def nah(a, b, stellen=2):
    return round(a, stellen) == round(b, stellen)


def sind(g):
    return math.sin(math.radians(g))


def cosd(g):
    return math.cos(math.radians(g))


def G(name, lp, warum, vor, fehler, verwandt, bsp, weg=()):
    return dict(name=name, lp=lp, warum=warum, vor=vor, fehler=fehler, verwandt=verwandt, bsp=bsp, weg=list(weg))


# ───────────────────────── Fläche und Raum ─────────────────────────
IDEE_F = [
 dict(warum="Eine Fläche misst man, indem man sie lückenlos mit gleich großen Quadraten auslegt und zählt; einen Körper füllt man mit gleich großen Würfeln. Jede Formel dieses Planeten ist eine Abkürzung für dieses Zählen: 4 Reihen zu je 6 Quadraten sind 6 · 4.",
      z=Z("Links ein Rechteck, vollständig mit Einheitsquadraten ausgelegt; die unterste Reihe ist gefärbt. Rechts ein Quader aus Einheitswürfeln im Schrägbild; die unterste Schicht ist gefärbt.",
          "Rechteck 6 cm mal 4 cm in Originalgröße (24 Quadrate zu 1 cm²). Quader 5 mal 4 mal 3 Würfel.",
          "Am Rechteck: „6 cm“, „4 cm“, „4 Reihen zu je 6 = 24 cm²“. Am Quader: „3 Schichten zu je 5 · 4 = 60 cm³“. Ein einzelnes Quadrat trägt „1 cm²“, ein einzelner Würfel „1 cm³“.",
          "Die eine Reihe und die eine Schicht – das, was beim Zählen wiederholt wird.",
          "Die Quadrate müssen wirklich quadratisch und gleich groß sein und genau aufgehen. Am Quader müssen die Würfel an allen sichtbaren Seiten abzählbar sein (5, 4, 3).",
          "Seiten „x“ und „x + 4“ ohne Gitter (Klasse 7); ein Quadratdezimeter mit 10 mal 10 Gitter für die Umrechnungszahl 100. Für „Fläche ist nicht Umfang“: daneben ein Rechteck 9 cm mal 1 cm mit gleich langem Rand.")),
 dict(warum="Vom Rechteck weiß man die Fläche durch Zählen. Jede andere Figur wird so zerschnitten und neu gelegt, dass ein Rechteck entsteht – oder sie ist die Hälfte einer Figur, deren Fläche man schon kennt. Deshalb muss man die Formeln nicht einzeln lernen: Man kann sie herleiten.",
      z=Z("Ein Stammbaum von links nach rechts. Rechteck → Parallelogramm (links ein Dreieck abgeschnitten, rechts angesetzt) → Dreieck (das Parallelogramm entlang einer Diagonale halbiert) → Trapez (zwei gleiche Trapeze ergeben ein Parallelogramm). Eigener Ast: Rechteck → Drachenviereck (im umschriebenen Rechteck, das doppelt so groß ist). Eigener Ast: Kreis in 12 Tortenstücke geschnitten und abwechselnd umgelegt zu einem „Fast-Rechteck“.",
          "Rechteck, Parallelogramm und Dreieck mit derselben Grundseite 6 cm und derselben Höhe 4 cm. Kreis: Radius 3 cm; das Fast-Rechteck ist π · r breit und r hoch.",
          "An jedem Pfeil, was getan wurde: „abschneiden und ansetzen“, „halbieren“, „verdoppeln“. In jeder Figur die Fläche: 24 cm², 24 cm², 12 cm².",
          "Die Höhe h: in jeder Figur dieselbe Farbe, gestrichelt, mit Zeichen für den rechten Winkel – und dieselbe Farbe für h in der Formel daneben.",
          "Die Höhe darf nie auf der schrägen Seite liegen. Das abgeschnittene und das angesetzte Dreieck müssen gleich aussehen. Beim Dreieck muss erkennbar sein, dass es genau die Hälfte ist.",
          "Dieselben Figuren mit Buchstaben g und h statt Zahlen (ab Klasse 7). Beim Dreieck eine zweite Fassung mit stumpfem Winkel: Die Höhe liegt außerhalb, an der verlängerten Grundseite.")),
 dict(warum="Ein Quader ist ein Stapel gleicher Schichten: Grundfläche mal Höhe. Das bleibt richtig, wenn die Grundfläche ein Dreieck oder ein Kreis ist (Prisma, Zylinder) und sogar, wenn der Stapel schief steht. Läuft der Körper spitz zu, bleibt genau ein Drittel übrig.",
      z=Z("Ein Stammbaum. Quader → Prisma mit dreieckiger Grundfläche → Zylinder (alle drei als Stapel dünner Schichten angedeutet). Darunter: Pyramide, eingezeichnet in den Quader mit derselben Grundfläche und Höhe, daneben Kegel im Zylinder. Abseits: Kugel im genau passenden Zylinder.",
          "Alle Körper gleich hoch. Pyramide und Kegel füllen sichtbar denselben Umriss wie ihr umgebender Körper.",
          "An den oberen drei: „V = G · h“. An Pyramide und Kegel: „⅓ · G · h“. An der Kugel: „⅔ des Zylinders“.",
          "Die Grundfläche G (gefärbt) und die Höhe h (gestrichelt, senkrecht, mit Zeichen für den rechten Winkel) – in jedem Körper dieselben zwei Farben.",
          "Die Höhe muss senkrecht auf der Grundfläche stehen, auch beim schiefen Körper – nie entlang einer schrägen Kante. Pyramide und umgebender Körper müssen dieselbe Grundfläche haben.",
          "Dieselben Körper mit Maßen: Zylinder r = 3 cm, h = 10 cm; Pyramide 6 cm mal 6 cm, h = 4 cm. Für den Satz von Cavalieri: ein gerader und ein schiefer Münzstapel gleicher Höhe.")),
 dict(warum="Schneidet man einen Körper an seinen Kanten auf und klappt ihn flach, sieht man seine ganze Außenfläche auf einmal: das Netz. Die Oberfläche ist die Summe dieser Flächen. Das Schrägbild ist der umgekehrte Weg: ein flaches Bild, das den Körper räumlich zeigt.",
      z=Z("Drei Bilder von links nach rechts: der Quader im Schrägbild; derselbe Quader halb aufgeklappt (Deckel und Seitenwände stehen schräg ab); sein Netz flach: sechs Rechtecke in Kreuzform. Je zwei gleiche Rechtecke haben in allen drei Bildern dieselbe Farbe.",
          "Quader 5 cm mal 4 cm mal 3 cm. Im Schrägbild: Tiefenkanten unter 45° und halb so lang; verdeckte Kanten gestrichelt. Im Netz: alle Rechtecke maßstäblich.",
          "Im Netz in jedem Rechteck seine Fläche: 20 cm², 15 cm², 12 cm², jeweils zweimal. Darunter: „O = 2 · (20 + 15 + 12) cm² = 94 cm²“.",
          "Das mittlere Bild – das Aufklappen – und die drei Farbpaare.",
          "Das Netz muss sich wirklich falten lassen: Kanten, die zusammenstoßen, sind gleich lang. Es müssen genau sechs Flächen sein.",
          "Dieselbe Darstellung für das Dreiecksprisma (Dreieck 3 cm, 4 cm, 5 cm, Höhe 6 cm): drei Rechtecke nebeneinander, zusammen 12 cm breit – so breit wie der Umfang des Dreiecks; zusammenstoßende Kanten gleich markiert. Für den Zylinder: Rechteck mit Breite 2 · π · r und zwei Kreise.")),
]
GESETZE_F = [
 G("Fläche messen", ("5", "5", "5"),
   "Ein Quadratdezimeter ist 10 cm lang und 10 cm breit. Es passen also 10 Reihen zu je 10 Quadratzentimetern hinein: 100.",
   "Gilt zwischen benachbarten Einheiten mm², cm², dm², m² und weiter m², a, ha, km².",
   "Mit 10 umrechnen wie bei Längen: 3 m² = 30 dm².",
   "Längen: Umrechnungszahl 10. Volumen: 1 000. Stellenwert (Rechenregel 1).",
   [(5, "E", "3 m² = 300 dm²", lambda: 3 * 100 == 300), (5, "E", "1 m² = 10 000 cm²", lambda: 100 * 100 == 10000), (8, "A", "5 000 cm² = 0,5 m²", lambda: F(5000, 10000) == F(1, 2))]),
 G("Rechteck", ("5", "5", "5"),
   "In ein Rechteck mit 6 cm Länge und 4 cm Breite passen 4 Reihen zu je 6 Einheitsquadraten.",
   "Beide Seiten in derselben Einheit.",
   "Fläche und Umfang verwechseln; cm statt cm² schreiben.",
   "Quadrat: Seite mal Seite. Ausmultiplizieren am Rechteck (Rechenregel 6).",
   [(5, "E", "6 cm lang, 4 cm breit: A = 6 cm · 4 cm = 24 cm²", lambda: 6 * 4 == 24), (5, "E", "Dasselbe Rechteck: u = 2 · (6 cm + 4 cm) = 20 cm", lambda: 2 * (6 + 4) == 20),
    (7, "A", "Seiten x und x + 4: A = x · (x + 4) = x² + 4x", lambda: all(x * (x + 4) == x * x + 4 * x for x in range(1, 9)))], ["Fläche messen"]),
 G("Fläche ist nicht Umfang", ("5", "5", "5"),
   "Der Umfang misst den Rand (eine Länge), die Fläche das Innere. Ein langes, schmales Rechteck hat viel Rand und wenig Inneres.",
   "Gilt für alle Figuren.",
   "Aus „gleicher Umfang“ auf „gleiche Fläche“ schließen – oder umgekehrt.",
   "Größter Flächeninhalt bei festem Umfang: das Quadrat (Kleinster und größter Wert, Planet Algebra).",
   [(5, "E", "Rechteck 6 cm mal 4 cm: u = 20 cm, A = 24 cm²", lambda: (2 * (6 + 4), 6 * 4) == (20, 24)), (5, "E", "Rechteck 9 cm mal 1 cm: u = 20 cm, A = 9 cm²", lambda: (2 * (9 + 1), 9 * 1) == (20, 9)),
    (9, "A", "Umfang 20 cm: Die größte Fläche hat das Quadrat mit 25 cm²", lambda: max(x * (10 - x) for x in range(0, 11)) == 25)], ["Rechteck"]),
 G("Zerlegen und Ergänzen", ("5", "5", "5"),
   "Beim Zerschneiden und Umlegen geht kein Stück verloren und keines kommt dazu.",
   "Die Teile müssen lückenlos und ohne Überlappung liegen.",
   "Glauben, dass beim Umlegen auch der Umfang gleich bleibt.",
   "Alle Flächenformeln dieses Planeten entstehen so.",
   [(5, "E", "L-Form, zerlegt: 6 cm · 2 cm + 2 cm · 3 cm = 18 cm²", lambda: 6 * 2 + 2 * 3 == 18), (5, "E", "Dieselbe L-Form, ergänzt: 6 cm · 5 cm − 4 cm · 3 cm = 18 cm²", lambda: 6 * 5 - 4 * 3 == 18)], ["Rechteck"]),
 G("Parallelogramm", ("6", "6", "6"),
   "Schneidet man an einer Seite ein Dreieck ab und setzt es an der anderen an, entsteht ein Rechteck mit derselben Grundseite und derselben Höhe.",
   "Die Höhe steht senkrecht auf der gewählten Grundseite.",
   "Die schräge Seite statt der Höhe nehmen.",
   "Rechteck als Sonderfall. Fläche mit Determinante (Planet Geometrie, Realschule).",
   [(6, "E", "g = 7 cm, h = 4 cm: A = 28 cm²", lambda: 7 * 4 == 28), (6, "E", "Dasselbe Parallelogramm, Grundseite 5 cm: zugehörige Höhe 28 cm² : 5 cm = 5,6 cm", lambda: F(28, 5) == F(56, 10))], ["Zerlegen und Ergänzen"]),
 G("Dreieck", ("6", "6", "6"),
   "Zwei gleiche Dreiecke lassen sich zu einem Parallelogramm zusammenlegen. Das Dreieck ist die Hälfte.",
   "Die Höhe gehört zur gewählten Grundseite und steht senkrecht auf ihr. Im stumpfwinkligen Dreieck liegen zwei der drei Höhen außerhalb.",
   "Das „geteilt durch 2“ vergessen. Eine Seite als Höhe nehmen, die nicht senkrecht steht.",
   "Rechtwinkliges Dreieck: halbes Rechteck aus den beiden Katheten. Formeln umstellen (Planet Algebra).",
   [(6, "E", "g = 8 cm, h = 5 cm: A = 8 cm · 5 cm : 2 = 20 cm²", lambda: F(8 * 5, 2) == 20), (8, "A", "A = 20 cm², g = 8 cm: h = 2 · 20 cm² : 8 cm = 5 cm", lambda: F(2 * 20, 8) == 5)], ["Parallelogramm"]),
 G("Trapez", ("6", "6", "6"),
   "Zwei gleiche Trapeze ergeben ein Parallelogramm mit der Grundseite a + c. Das Trapez ist die Hälfte.",
   "a und c sind die beiden parallelen Seiten; h ist ihr Abstand.",
   "Die Schenkel statt der parallelen Seiten mitteln.",
   "Parallelogramm (a = c) und Dreieck (c = 0) sind Sonderfälle.",
   [(6, "E", "a = 9 cm, c = 5 cm, h = 4 cm: A = (9 cm + 5 cm) : 2 · 4 cm = 28 cm²", lambda: F(9 + 5, 2) * 4 == 28)], ["Parallelogramm"]),
 G("Drachenviereck und Raute", ("6 (in der Lehrplan-Kopie nicht eigens genannt)", "6", "6"),
   "Das Rechteck, das man um die beiden Diagonalen legt, ist genau doppelt so groß wie das Viereck.",
   "Die Diagonalen stehen senkrecht aufeinander – das ist bei Drachenviereck, Raute und Quadrat so.",
   "Die Formel auf Vierecke anwenden, deren Diagonalen nicht senkrecht stehen.",
   "Quadrat: halbes Diagonalenquadrat.",
   [(6, "E", "e = 8 cm, f = 5 cm: A = 8 cm · 5 cm : 2 = 20 cm²", lambda: F(8 * 5, 2) == 20)], ["Zerlegen und Ergänzen"]),
 G("Kreis", ("8", "9", "9"),
   "Der Umfang ist bei jedem Kreis dasselbe Vielfache des Durchmessers: π, etwas mehr als 3. Schneidet man den Kreis in Tortenstücke und legt sie abwechselnd um, entsteht fast ein Rechteck: halber Umfang breit, r hoch.",
   "r ist der Radius, nicht der Durchmesser.",
   "Durchmesser statt Radius einsetzen. Meinen, doppelter Radius gebe doppelte Fläche.",
   "π ist irrational (Planet Zahlen). Vergrößern mit Faktor k (Planet Geometrie).",
   [(8, "E", "r = 5 cm: u = 2 · π · 5 cm ≈ 31,4 cm", lambda: nah(2 * PI * 5, 31.4, 1)), (8, "E", "r = 5 cm: A = π · 25 cm² ≈ 78,5 cm²", lambda: nah(PI * 25, 78.5, 1)),
    (8, "A", "r = 10 cm statt 5 cm: Umfang doppelt, Fläche vierfach", lambda: nah(PI * 100 / (PI * 25), 4))], ["Zerlegen und Ergänzen"]),
 G("Kreisausschnitt", ("8 (in der Lehrplan-Kopie nicht eigens genannt)", "9", "9 (nur Überschrift „Kreise“)"),
   "Ein Ausschnitt mit 60° ist ein Sechstel des vollen Kreises – also auch ein Sechstel des Umfangs und ein Sechstel der Fläche.",
   "Der Winkel ist der Mittelpunktswinkel.",
   "Den Winkel nicht durch 360° teilen.",
   "Verhältnis (Rechenregel 11). Kegelmantel: ein Kreisausschnitt.",
   [(8, "E", "r = 6 cm, 60°: Bogen = 1/6 · 2 · π · 6 cm = 2π cm ≈ 6,3 cm", lambda: nah(F(60, 360) * 2 * PI * 6, 6.3, 1)), (8, "E", "r = 6 cm, 60°: A = 1/6 · π · 36 cm² = 6π cm² ≈ 18,8 cm²", lambda: nah(F(60, 360) * PI * 36, 18.8, 1))], ["Kreis"]),
 G("Volumen messen", ("6", "6", "6"),
   "Ein Kubikdezimeter ist 10 cm lang, breit und hoch: 10 Schichten zu je 10 mal 10 Würfeln, also 1 000 Kubikzentimeter.",
   "Gilt zwischen benachbarten Einheiten mm³, cm³, dm³, m³. 1 l = 1 dm³, 1 ml = 1 cm³.",
   "Mit 10 oder 100 umrechnen.",
   "Flächen: Umrechnungszahl 100. Stellenwert (Rechenregel 1).",
   [(6, "E", "2 dm³ = 2 000 cm³", lambda: 2 * 1000 == 2000), (6, "E", "1,5 l = 1,5 dm³ = 1 500 cm³", lambda: F(3, 2) * 1000 == 1500), (6, "E", "1 m³ = 1 000 dm³ = 1 000 l", lambda: 10 ** 3 == 1000)]),
 G("Quader", ("6", "6", "6"),
   "Die unterste Schicht hat Länge mal Breite Würfel; die Höhe sagt, wie viele Schichten es sind.",
   "Alle drei Kanten in derselben Einheit.",
   "Die drei Kantenlängen addieren statt malnehmen.",
   "Würfel: Kante hoch 3. Prisma: Grundfläche mal Höhe.",
   [(5, "V", "Schachtel mit 3 Schichten zu je 5 mal 4 Würfeln: 60 Würfel", lambda: 3 * 5 * 4 == 60), (6, "E", "5 cm · 4 cm · 3 cm = 60 cm³", lambda: 5 * 4 * 3 == 60), (6, "E", "Würfel mit Kante 4 cm: 64 cm³", lambda: 4 ** 3 == 64)], ["Volumen messen"]),
 G("Oberfläche", ("5 (Quader), 6 (einfache Körper)", "6", "6"),
   "Die Oberfläche ist das, was man anmalen müsste. Beim Quader liegen sich je zwei gleiche Rechtecke gegenüber.",
   "Jede Fläche genau einmal zählen.",
   "Nur drei statt sechs Flächen nehmen. Oberfläche (cm²) und Volumen (cm³) verwechseln.",
   "Netz. Mantel von Prisma, Zylinder, Pyramide, Kegel.",
   [(5, "E", "Quader 5 cm, 4 cm, 3 cm: O = 2 · (20 + 15 + 12) cm² = 94 cm²", lambda: 2 * (5 * 4 + 5 * 3 + 4 * 3) == 94), (5, "E", "Würfel mit Kante 3 cm: O = 6 · 9 cm² = 54 cm²", lambda: 6 * 9 == 54)], ["Rechteck"]),
 G("Netz und Schrägbild", ("8 (Prisma, Zylinder), 10 (Pyramide, Kegel)", "5 (Würfel, Quader), 7 (Prisma, Pyramide)", "5 (Würfel, Quader), 8 (Prisma, Pyramide)"),
   "Das Netz entsteht durch Aufschneiden und Aufklappen. Im Schrägbild bleibt die Vorderseite unverzerrt; Kanten nach hinten werden schräg und verkürzt gezeichnet.",
   "Im Netz sind Kanten, die zusammengehören, gleich lang. Im Schrägbild kann man nur an unverzerrten Flächen messen.",
   "Ein Netz zeichnen, das sich nicht falten lässt. Im Schrägbild schräge Kanten in voller Länge zeichnen.",
   "Oberfläche. Lage im Raum.",
   [(5, "V", "Ein Würfelnetz hat 6 Quadrate", lambda: True), (8, "E", "Dreiecksprisma (3 cm, 4 cm, 5 cm; Höhe 6 cm): Das Netz hat 2 Dreiecke und 3 Rechtecke; die Rechtecke sind zusammen 12 cm breit", lambda: 3 + 4 + 5 == 12),
    (8, "E", "Zylinder mit r = 3 cm: Das Mantel-Rechteck ist 2 · π · 3 cm ≈ 18,8 cm breit", lambda: nah(2 * PI * 3, 18.8, 1))], ["Oberfläche"]),
 G("Prisma und Zylinder", ("8", "9", "10"),
   "Der Körper ist ein Stapel gleicher Schichten mit der Form der Grundfläche. Der Mantel, abgerollt, ist ein Rechteck: so breit wie der Umfang der Grundfläche, so hoch wie der Körper.",
   "V = G · h gilt mit der senkrechten Höhe, auch beim schiefen Körper. Die Mantelformel gilt nur beim geraden Körper.",
   "Beim Zylinder den Durchmesser statt des Radius einsetzen. Bei der Oberfläche die zweite Grundfläche vergessen.",
   "Quader ist ein Prisma. Satz von Cavalieri für schiefe Körper.",
   [(8, "E", "Dreiecksprisma mit G = 6 cm², h = 10 cm: V = 60 cm³", lambda: 6 * 10 == 60), (8, "E", "Zylinder mit r = 3 cm, h = 10 cm: V = π · 9 cm² · 10 cm = 90π cm³ ≈ 282,7 cm³", lambda: nah(PI * 9 * 10, 282.7, 1)),
    (8, "E", "Derselbe Zylinder: Mantel = 2 · π · 3 cm · 10 cm = 60π cm² ≈ 188,5 cm²", lambda: nah(2 * PI * 3 * 10, 188.5, 1))], ["Quader", "Kreis"]),
 G("Satz von Cavalieri", ("10", "9", "10"),
   "Ein Stapel Münzen hat dasselbe Volumen, ob er gerade steht oder schief geschoben ist: Jede Schicht ist gleich geblieben.",
   "Die Schnitte liegen parallel zur Grundfläche und werden auf gleicher Höhe verglichen.",
   "Daraus auch gleiche Oberfläche folgern – darüber sagt der Satz nichts.",
   "Schiefes Prisma. Begründung der Formeln für Pyramide und Kugel.",
   [(10, "E", "Schiefes Prisma mit G = 12 cm² und senkrechter Höhe 5 cm: V = 60 cm³ – wie das gerade", lambda: 12 * 5 == 60)], ["Prisma und Zylinder"]),
 G("Pyramide und Kegel", ("10", "9", "10"),
   "Die Schnittfläche schrumpft zur Spitze hin mit dem Quadrat des Abstands von der Spitze; zusammengezählt bleibt genau ein Drittel des Prismas. Zum Anfassen: Ein Würfel zerfällt in drei gleiche Pyramiden.",
   "h ist die senkrechte Höhe, nicht die Seitenkante. Die Mantelformel π · r · s gilt nur für den geraden Kreiskegel.",
   "Das Drittel vergessen. Die Mantellinie s als Höhe einsetzen.",
   "Mantellinie und Seitenhöhe berechnet man mit dem Satz des Pythagoras (Planet Geometrie). Kegelmantel: ein Kreisausschnitt.",
   [(10, "E", "Pyramide, Grundfläche 6 cm mal 6 cm, h = 4 cm: V = 36 cm² · 4 cm : 3 = 48 cm³", lambda: F(36 * 4, 3) == 48),
    (10, "E", "Dieselbe Pyramide: Seitenhöhe 5 cm, Mantel = 4 · (6 cm · 5 cm : 2) = 60 cm²", lambda: 3 ** 2 + 4 ** 2 == 5 ** 2 and 4 * F(6 * 5, 2) == 60),
    (10, "E", "Kegel mit r = 3 cm, h = 4 cm: V = π · 9 cm² · 4 cm : 3 = 12π cm³ ≈ 37,7 cm³", lambda: nah(PI * 9 * 4 / 3, 37.7, 1)),
    (10, "E", "Derselbe Kegel: s = 5 cm, Mantel = π · 3 cm · 5 cm = 15π cm² ≈ 47,1 cm²", lambda: nah(PI * 3 * 5, 47.1, 1))], ["Prisma und Zylinder", "Satz von Cavalieri"]),
 G("Kugel", ("10", "9", "10"),
   "Die Kugel füllt genau zwei Drittel des Zylinders, in den sie gerade hineinpasst. Ihre Oberfläche ist so groß wie der Mantel dieses Zylinders.",
   "r ist der Radius.",
   "Die beiden Formeln verwechseln: r² gehört zur Fläche, r³ zum Volumen.",
   "Kreis. Halbkugel: die Hälfte – bei der Oberfläche kommt die Schnittfläche dazu.",
   [(10, "E", "r = 2 cm: O = 4 · π · 4 cm² = 16π cm² ≈ 50,3 cm²", lambda: nah(4 * PI * 4, 50.3, 1)), (10, "E", "r = 2 cm: V = 4/3 · π · 8 cm³ = 32π/3 cm³ ≈ 33,5 cm³", lambda: nah(4 / 3 * PI * 8, 33.5, 1)),
    (10, "A", "Die Kugel mit r = 2 cm füllt ⅔ des Zylinders mit r = 2 cm, h = 4 cm", lambda: nah((4 / 3 * PI * 8) / (PI * 4 * 4), 2 / 3, 6))], ["Prisma und Zylinder", "Satz von Cavalieri"]),
 G("Lage im Raum", (f"– (in der Lehrplan-Kopie {NG})", "7", f"– ({NG})"),
   "In der Ebene sind zwei verschiedene Geraden parallel oder schneiden sich. Im Raum gibt es eine dritte Möglichkeit: Sie laufen aneinander vorbei, ohne parallel zu sein.",
   "Gilt für zwei verschiedene Geraden.",
   "Im Schrägbild zwei Kanten für schneidend halten, weil sich ihre Bilder kreuzen.",
   "Parallel und senkrecht (Planet Geometrie). Schrägbild.",
   [("R7", "E", "Im Würfel ABCDEFGH sind die Kanten AB und CG windschief: nicht parallel und ohne gemeinsamen Punkt", lambda: True)], ["Netz und Schrägbild"]),
]

# ───────────────────────── Geometrie ─────────────────────────
IDEE_G = [
 dict(warum="Schneidet eine Gerade zwei Parallelen, entstehen an beiden Kreuzungen dieselben Winkel. Zieht man durch die Spitze eines Dreiecks die Parallele zur gegenüberliegenden Seite, liegen dort alle drei Winkel des Dreiecks nebeneinander und füllen genau eine gerade Linie: 180°.",
      z=Z("Ein Dreieck ABC mit waagerechter Seite AB unten. Durch C läuft eine Gerade parallel zu AB. Bei C liegen drei Winkel nebeneinander: links der Winkel α (gleich dem bei A), in der Mitte γ, rechts der Winkel β (gleich dem bei B).",
          "α = 50°, β = 60°, γ = 70°, maßstäblich gezeichnet.",
          "α, β, γ im Dreieck; α und β noch einmal oben bei C. Die beiden Parallelen tragen das Parallel-Zeichen. Darunter: „α + β + γ = 180°“.",
          "α bei A und bei C in derselben Farbe, β bei B und bei C in einer zweiten, γ in einer dritten.",
          "Die Gerade durch C muss parallel aussehen. Die drei Winkel bei C müssen die gerade Linie lückenlos füllen. Die Winkelgrößen müssen stimmen (kein gleichseitiges Dreieck zeichnen).",
          "Nur die zwei Parallelen mit der schneidenden Geraden: Stufen- und Wechselwinkel (70°). Nur eine Kreuzung: Scheitel- und Nebenwinkel (65° und 115°). Viereck, durch eine Diagonale in zwei Dreiecke geteilt: 360°.")),
 dict(warum="Viele Linien der Geometrie sind „alle Punkte mit einer Abstandseigenschaft“: gleich weit von einem Punkt (Kreis), von zwei Punkten (Mittelsenkrechte), von zwei Geraden (Winkelhalbierende). Darum findet man den Umkreismittelpunkt mit Mittelsenkrechten und den Inkreismittelpunkt mit Winkelhalbierenden.",
      z=Z("Eine Hauptzeichnung und zwei kleinere Nebenzeichnungen. Hauptzeichnung (Feld 1, passt zum Merksatz): Kreis um M mit vier Punkten auf der Linie und ihren Radien. Nebenzeichnung Feld 2: Strecke AB mit ihrer Mittelsenkrechten; ein Punkt P darauf ist mit A und B verbunden. Nebenzeichnung Feld 3: ein Winkel mit seiner Winkelhalbierenden; von einem Punkt P darauf gehen zwei Lote zu den Schenkeln.",
          "Radius 3 cm. Strecke AB 4 cm, P liegt 3 cm über der Mitte. Winkel 60°.",
          "Feld 1: „gleich weit von M“. Feld 2: „gleich weit von A und B“. Feld 3: „gleich weit von beiden Schenkeln“.",
          "Die gleich langen Strecken: in jedem Feld mit demselben Strich-Zeichen und derselben Farbe.",
          "In Feld 2 muss die Mittelsenkrechte genau durch die Mitte gehen und senkrecht stehen. In Feld 3 müssen die Abstände Lote sein (Zeichen für den rechten Winkel), nicht irgendwelche Verbindungen.",
          "Feld 1 mit Durchmesser AB und einem Punkt C auf dem Kreis: Satz des Thales (die Radien MA, MB, MC sind gleich lang). Feld 1 mit Tangente: Radius und Tangente bilden 90°. Feld 2 dreimal an einem Dreieck: Umkreis.")),
 dict(warum="Zwei Figuren sind deckungsgleich, wenn man die eine so auf die andere legen kann, dass sie genau passt. Spiegeln, Schieben und Drehen sind genau die Bewegungen, die dabei erlaubt sind. Bei Dreiecken genügen drei passende Angaben, damit nur noch eine Form möglich ist.",
      z=Z("Ein Dreieck und drei Bilder davon: gespiegelt an einer Achse, verschoben längs eines Pfeils, gedreht um einen Punkt. In allen vier Dreiecken tragen gleiche Seiten gleiche Strich-Zeichen und gleiche Winkel gleiche Bögen.",
          "Dreieck mit den Seiten 3 cm, 4 cm, 5 cm – nicht gleichschenklig, damit man die Lage erkennt. Drehung um 90°.",
          "Ecken A, B, C und A', B', C'. Spiegelachse, Verschiebungspfeil und Drehpunkt mit Drehwinkel beschriftet.",
          "Die gleichen Seitenlängen (Strich-Zeichen) – sie bleiben bei allen drei Bewegungen.",
          "Alle vier Dreiecke müssen exakt gleich groß sein. Das gespiegelte Dreieck hat den umgekehrten Umlaufsinn, das verschobene und das gedrehte nicht.",
          "Nur das gespiegelte Paar mit Achse: Symmetrie. Nur das verschobene Paar: Vektor. Für die Kongruenzsätze: drei Stäbe 3 cm, 4 cm, 5 cm, die sich nur zu einem Dreieck fügen lassen – daneben vier Stäbe, die ein verschiebbares Viereck bilden.")),
 dict(warum="Vergrößert man eine Figur wie mit einem Kopierer, bleiben alle Winkel, und jede Länge wird mit demselben Faktor malgenommen. Deshalb sind in ähnlichen Figuren alle Längenverhältnisse gleich – das ist der Dreisatz der Geometrie.",
      z=Z("Zwei Strahlen von einem Punkt S. Zwei parallele Geraden schneiden beide Strahlen; so entstehen ein kleines Dreieck und ein großes, das das kleine enthält.",
          "Auf dem ersten Strahl 2 cm und 4 cm von S; auf dem zweiten 3 cm und 6 cm. Die Parallelen sind 2,5 cm und 5 cm lang (maßstäblich, Faktor 2).",
          "Die Längen an den Abschnitten. Parallel-Zeichen an den beiden Geraden. Daneben: „alles mal 2“.",
          "Die gleichen Winkel in beiden Dreiecken (gleiche Bögen) und der Faktor 2.",
          "Die beiden Geraden müssen parallel sein. Das große Dreieck muss in jeder Länge genau doppelt so groß sein. Alle Längen werden von S aus gemessen.",
          "Dieselbe Figur mit x an einer Stelle: 2 : 3 = 4 : x. Für „Vergrößern mit Faktor k“: ein Einheitsquadrat und ein Quadrat mit doppelter Seite, in 4 Einheitsquadrate geteilt; ein Würfel mit doppelter Kante aus 8 Würfeln.")),
 dict(warum="Der rechte Winkel macht das Dreieck berechenbar. Kennt man zwei Seiten, liefert der Satz des Pythagoras die dritte. Kennt man eine Seite und einen spitzen Winkel, sind alle rechtwinkligen Dreiecke mit diesem Winkel ähnlich – ihre Seitenverhältnisse sind fest und heißen Sinus, Kosinus und Tangens.",
      z=Z("Ein rechtwinkliges Dreieck mit einem Quadrat über jeder Seite; jedes Quadrat ist in Einheitsquadrate geteilt.",
          "Katheten 3 cm und 4 cm, Hypotenuse 5 cm. Quadrate mit 9, 16 und 25 Feldern.",
          "Seiten a, b, c; rechter Winkel markiert. In den Quadraten „9“, „16“, „25“. Darunter: „9 + 16 = 25“.",
          "Der rechte Winkel und die Hypotenuse ihm gegenüber.",
          "Der rechte Winkel muss markiert und wirklich 90° sein. Die Hypotenuse liegt ihm gegenüber und ist die längste Seite. Die Felder müssen abzählbar sein.",
          "Dasselbe Dreieck ohne Quadrate: ein spitzer Winkel α markiert, die Seiten heißen „Gegenkathete“ (gegenüber von α), „Ankathete“ (an α) und „Hypotenuse“; daneben sin α = 3/5, cos α = 4/5, tan α = 3/4. Dasselbe Dreieck im Einheitskreis: Hypotenuse = 1, Katheten = cos α und sin α.")),
]
P7 = "7"
GESETZE_G = [
 G("Koordinatensystem", ("5", "5", "5"),
   "Zwei Zahlengeraden, die sich bei null senkrecht kreuzen, geben jedem Punkt der Ebene eine Adresse aus zwei Zahlen.",
   "Zuerst die x-Koordinate (waagerecht), dann die y-Koordinate (senkrecht).",
   "x und y vertauschen.",
   "Zahlengerade (Planet Zahlen). Graph einer Funktion (Planet Funktionen).",
   [(5, "E", "P(3 | 2): von 0 aus 3 nach rechts, 2 nach oben", lambda: True), (5, "E", "Q(−2 | 1): 2 nach links, 1 nach oben", lambda: True)]),
 G("Parallel, senkrecht, Abstand", ("5", "5", "5"),
   "Von allen Verbindungen eines Punktes zu einer Geraden ist das Lot die kürzeste; jede andere ist die längste Seite eines rechtwinkligen Dreiecks.",
   "Der Abstand wird immer senkrecht gemessen.",
   "Schräg messen.",
   "Höhe in Dreieck und Parallelogramm (Planet Fläche und Raum). Ortslinien.",
   [(5, "E", "P(2 | 5) hat von der x-Achse den Abstand 5", lambda: True), (9, "A", "Der Punkt (3 | 4) hat vom Ursprung den Abstand 5", lambda: 3 ** 2 + 4 ** 2 == 5 ** 2)]),
 G("Winkelarten", ("5", "5", "5"),
   "Ein Winkel misst eine Drehung. Die volle Drehung ist in 360 gleiche Teile geteilt.",
   "Gemessen wird am Scheitel, von einem Schenkel zum anderen.",
   "Am Geodreieck die falsche Skala ablesen.",
   "Winkelsumme. Kreisausschnitt (Planet Fläche und Raum).",
   [(5, "E", "Viertel-Drehung 90°, halbe Drehung 180°, volle Drehung 360°", lambda: 4 * 90 == 2 * 180 == 360), (5, "E", "Spitz: unter 90°. Stumpf: zwischen 90° und 180°. Überstumpf: über 180°", lambda: True)]),
 G("Scheitel- und Nebenwinkel", (P7, "5", "5"),
   "Nebenwinkel liegen nebeneinander auf einer Geraden, zusammen also 180°. Zwei Scheitelwinkel haben denselben Nebenwinkel, sind also gleich groß.",
   "Zwei Geraden, die sich schneiden.",
   "Scheitelwinkel und Nebenwinkel verwechseln.",
   "Stufen- und Wechselwinkel.",
   [(7, "E", "Ein Winkel hat 65°: Scheitelwinkel 65°, Nebenwinkel 115°", lambda: 180 - 65 == 115)], ["Winkelarten"]),
 G("Stufen- und Wechselwinkel", (P7, "7", "7"),
   "Verschiebt man eine Kreuzung längs der schneidenden Geraden auf die andere Parallele, kommen die Winkel zur Deckung.",
   "Gleich groß sind sie nur, wenn die beiden Geraden parallel sind. Umgekehrt: Sind sie gleich groß, sind die Geraden parallel.",
   "Die Winkel für gleich halten, obwohl die Geraden nicht parallel sind.",
   "Winkelsumme. Strahlensätze.",
   [(7, "E", "Parallelen, oben 70°: Stufenwinkel unten 70°, Wechselwinkel 70°", lambda: True), (7, "E", "Stufenwinkel 70° und 72°: Die Geraden sind nicht parallel", lambda: 70 != 72)], ["Scheitel- und Nebenwinkel"]),
 G("Winkelsumme", (P7, "7", "7"),
   "Die Parallele durch eine Ecke legt alle drei Winkel nebeneinander auf eine Gerade. Ein n-Eck lässt sich von einer Ecke aus in n − 2 Dreiecke teilen.",
   "Gilt für jedes Dreieck in der Ebene; die Vielecksformel für die Innenwinkel.",
   "Beim n-Eck n · 180° rechnen.",
   "Außenwinkelsatz. Gleichschenkliges Dreieck.",
   [(5, "V", "Rechteck: 4 · 90° = 360°", lambda: 4 * 90 == 360), (7, "E", "Dreieck mit 50° und 60°: dritter Winkel 70°", lambda: 180 - 50 - 60 == 70), (7, "E", "Fünfeck: (5 − 2) · 180° = 540°", lambda: 3 * 180 == 540),
    (7, "E", "Außenwinkel zu den Innenwinkeln 50° und 60°: 110°", lambda: 180 - 70 == 50 + 60)], ["Stufen- und Wechselwinkel"]),
 G("Besondere Vierecke", ("5 (erkennen), 7 (ordnen)", "5, 8", "5, 8"),
   "Jede Sorte ist durch Eigenschaften festgelegt; wer mehr Eigenschaften hat, gehört auch zu den allgemeineren Sorten.",
   "Die Eigenschaften gelten für die ganze Sorte, nicht nur für das gezeichnete Beispiel.",
   "Meinen, ein Quadrat sei kein Rechteck.",
   "Symmetrie ordnet die Vierecke. Flächenformeln (Planet Fläche und Raum).",
   [(5, "E", "Jedes Quadrat ist ein Rechteck und eine Raute – aber nicht jedes Rechteck ein Quadrat", lambda: True), (7, "A", "Parallelogramm mit einem Winkel von 70°: Nachbarwinkel 110°, Gegenwinkel 70°", lambda: 2 * 70 + 2 * 110 == 360)]),
 G("Ortslinien", ("5 (Abstandsbedingungen), 7 (Mittelsenkrechte, Winkelhalbierende)", "6 (Konstruktion), 7 (Ortslinien)", "6, 7 (nur Überschrift)"),
   "Spiegelt man an der Mittelsenkrechten, tauschen A und B die Plätze; jeder Punkt auf der Achse bleibt liegen und ist deshalb von beiden gleich weit entfernt.",
   "Alle Punkte der Linie haben die Eigenschaft – und kein anderer Punkt hat sie.",
   "Nur einen Punkt einzeichnen statt der ganzen Linie.",
   "Umkreis und Inkreis. Symmetrie.",
   [(5, "E", "Alle Punkte, die 3 cm von M entfernt sind: Kreis um M mit r = 3 cm", lambda: True),
    (7, "E", "A(0 | 0), B(4 | 0): Der Punkt (2 | 3) ist von beiden gleich weit entfernt", lambda: 2 ** 2 + 3 ** 2 == (2 - 4) ** 2 + 3 ** 2)], ["Parallel, senkrecht, Abstand"]),
 G("Gleichschenkliges Dreieck", (P7, "6", "6"),
   "Das Dreieck ist achsensymmetrisch; die Spiegelung an der Achse durch die Spitze legt die Basiswinkel aufeinander.",
   "Zwei Seiten sind gleich lang. Umkehrung: Sind zwei Winkel gleich, sind es auch die gegenüberliegenden Seiten.",
   "Den Winkel an der Spitze für einen Basiswinkel halten.",
   "Symmetrie. Satz des Thales.",
   [(7, "E", "Winkel an der Spitze 40°: Basiswinkel je (180° − 40°) : 2 = 70°", lambda: F(180 - 40, 2) == 70), (7, "E", "Gleichseitiges Dreieck: 3 · 60° = 180°", lambda: 3 * 60 == 180)], ["Winkelsumme", "Symmetrie"]),
 G("Kongruenzsätze", (P7, "7", "nicht eindeutig"),
   "Konstruiert man mit drei passenden Angaben, bleibt beim Zeichnen keine Wahl: Es entsteht immer dasselbe Dreieck.",
   "Bei SsW muss der Winkel der längeren der beiden Seiten gegenüberliegen. Drei Winkel reichen nicht.",
   "WWW oder „zwei Seiten und irgendein Winkel“ für einen Kongruenzsatz halten.",
   "Spiegeln, Verschieben, Drehen. Ähnlichkeit: gleiche Winkel genügen dort.",
   [(7, "E", "3 cm, 4 cm, 5 cm: genau ein Dreieck (SSS)", lambda: 3 + 4 > 5), (7, "E", "2 cm, 3 cm, 6 cm: kein Dreieck, denn 2 + 3 < 6", lambda: 2 + 3 < 6),
    (7, "E", "Winkel 50°, 60°, 70°: beliebig viele verschieden große Dreiecke", lambda: 50 + 60 + 70 == 180)]),
 G("Satz und Kehrsatz", (P7, f"– ({NG})", f"– ({NG})"),
   "„Wenn A, dann B“ sagt nichts darüber, ob aus B auch A folgt.",
   "Jede Umkehrung braucht eine eigene Begründung; ein Gegenbeispiel widerlegt sie.",
   "Aus einem Satz stillschweigend seine Umkehrung machen.",
   "Arbeitsweise Begründen. Aussagenlogik (Entdecker-Inseln).",
   [(7, "E", "Satz: Jedes Quadrat hat vier rechte Winkel. Die Umkehrung ist falsch – Gegenbeispiel: Rechteck 3 cm mal 5 cm", lambda: 3 != 5)]),
 G("Satz des Thales", (P7, f"– (in der Lehrplan-Kopie {NG})", f"– ({NG})"),
   "Die Radien zu den drei Ecken sind gleich lang und teilen das Dreieck in zwei gleichschenklige. Deren Basiswinkel ergeben bei C zusammen die Hälfte von 180°.",
   "Die Seite AB ist ein Durchmesser, C liegt auf dem Kreis und ist weder A noch B.",
   "Den Satz bei einer Sehne anwenden, die kein Durchmesser ist.",
   "Umkehrung: Der Umkreismittelpunkt eines rechtwinkligen Dreiecks ist die Mitte der Hypotenuse.",
   [(7, "E", "A(−5 | 0), B(5 | 0), C(3 | 4) auf dem Kreis um den Ursprung: Der Winkel bei C ist 90°", lambda: 3 ** 2 + 4 ** 2 == 25 and (-5 - 3) * (5 - 3) + (0 - 4) * (0 - 4) == 0)], ["Gleichschenkliges Dreieck", "Winkelsumme"]),
 G("Tangente", (P7, "7", "7 (nur Überschrift)"),
   "Der Berührpunkt ist der Punkt der Tangente, der dem Mittelpunkt am nächsten liegt – und die kürzeste Verbindung steht senkrecht.",
   "Die Gerade berührt den Kreis in genau einem Punkt.",
   "Die Tangente „nach Augenmaß“ anlegen statt senkrecht zum Radius.",
   "Tangente von einem äußeren Punkt: mit dem Thaleskreis. Abstand.",
   [(7, "E", "Kreis um den Ursprung mit r = 5, Berührpunkt (3 | 4): Der Radius hat die Steigung 4/3, die Tangente −¾ – sie stehen senkrecht", lambda: F(4, 3) * F(-3, 4) == -1),
    (9, "A", "Äußerer Punkt 13 cm von M, r = 5 cm: Das Tangentenstück ist 12 cm lang", lambda: 13 ** 2 - 5 ** 2 == 12 ** 2)], ["Parallel, senkrecht, Abstand"]),
 G("Umkreis und Inkreis", (P7, "7", "7 (nur Überschrift)"),
   "Ein Punkt auf zwei Mittelsenkrechten ist von allen drei Ecken gleich weit entfernt. Ein Punkt auf zwei Winkelhalbierenden ist von allen drei Seiten gleich weit entfernt.",
   "Gilt für jedes Dreieck. Der Umkreismittelpunkt kann außerhalb liegen (stumpfwinkliges Dreieck).",
   "Mittelsenkrechte und Winkelhalbierende vertauschen.",
   "Ortslinien. Schwerpunkt: Schnitt der Seitenhalbierenden.",
   [(7, "E", "A(0 | 0), B(6 | 0), C(0 | 8): Umkreismittelpunkt (3 | 4), von jeder Ecke 5 entfernt", lambda: 3 ** 2 + 4 ** 2 == (3 - 6) ** 2 + 4 ** 2 == 3 ** 2 + (4 - 8) ** 2 == 25)], ["Ortslinien"]),
 G("Spiegeln, Verschieben, Drehen", ("7 (Achsen- und Punktspiegelung)", "6 (Achsenspiegelung), 7 (Verschiebung), 8 (Drehung)", f"6, 7; Drehung {NG}"),
   "Die Figur wird als Ganzes bewegt, nicht verformt.",
   "Nur diese Bewegungen und ihre Verkettungen. Vergrößern gehört nicht dazu.",
   "Beim Spiegeln den Abstand zur Achse nicht senkrecht abtragen.",
   "Die Achsenspiegelung kehrt den Umlaufsinn um, Verschiebung und Drehung nicht. Zentrische Streckung: Ähnlichkeit.",
   [(7, "E", "Spiegelung an der y-Achse: A(2 | 1) → A'(−2 | 1), B(5 | 1) → B'(−5 | 1). Die Strecke ist vorher und nachher 3 lang", lambda: 5 - 2 == -2 - (-5) == 3)]),
 G("Symmetrie", (P7, "6", "6"),
   "Eine Figur ist symmetrisch, wenn eine Bewegung sie auf sich selbst abbildet.",
   "Achsensymmetrie: Spiegelung. Punktsymmetrie: Drehung um 180°.",
   "Die Diagonale eines Rechtecks für eine Symmetrieachse halten.",
   "Besondere Vierecke. Symmetrie von Graphen (Planet Funktionen).",
   [(5, "V", "Rechteck: 2 Symmetrieachsen. Quadrat: 4", lambda: True), (7, "E", "Ein Parallelogramm ist punktsymmetrisch, im Allgemeinen aber nicht achsensymmetrisch", lambda: True)], ["Spiegeln, Verschieben, Drehen"]),
 G("Vektoren", ("–", "7", "7"),
   "Eine Verschiebung ist durch „wie weit nach rechts, wie weit nach oben“ vollständig beschrieben – gleich, wo sie ansetzt.",
   "Koordinaten: Spitze minus Fuß.",
   "Fuß minus Spitze rechnen.",
   "Plus und Minus mit negativen Zahlen (Rechenregel 2). Betrag eines Vektors: Satz des Pythagoras.",
   [("R7", "E", "A(1 | 2), B(4 | 6): Der Vektor von A nach B ist (3; 4), der Gegenvektor (−3; −4)", lambda: (4 - 1, 6 - 2) == (3, 4))], ["Spiegeln, Verschieben, Drehen"]),
 G("Fläche mit Determinante", ("–", "7", "7"),
   "Das Parallelogramm lässt sich in ein Rechteck einpassen; zieht man die überstehenden Dreiecke ab, bleibt a · d − b · c.",
   "Die beiden Vektoren (a; b) und (c; d) setzen an derselben Ecke an. Für das Dreieck: die Hälfte.",
   "Das Vorzeichen stehen lassen – eine Fläche ist nie negativ.",
   "Parallelogramm und Dreieck (Planet Fläche und Raum).",
   [("R7", "E", "Vektoren (4; 1) und (2; 3): Parallelogramm 4 · 3 − 1 · 2 = 10, Dreieck 5", lambda: 4 * 3 - 1 * 2 == 10)], ["Vektoren"]),
 G("Matrizen und Skalarprodukt", ("–", "10 (nur Gruppe I)", "–"),
   "Das Skalarprodukt misst, wie sehr zwei Vektoren in dieselbe Richtung zeigen; stehen sie senkrecht, ist es null.",
   "Skalarprodukt von (a; b) und (c; d): a · c + b · d. Beide Vektoren sind nicht der Nullvektor.",
   "Skalarprodukt und Determinante verwechseln.",
   "Senkrechte Geraden (Planet Funktionen). Kosinussatz.",
   [("R10", "E", "(3; 4) und (−4; 3): 3 · (−4) + 4 · 3 = 0, also senkrecht", lambda: 3 * (-4) + 4 * 3 == 0)], ["Vektoren"]),
 G("Ähnlichkeit", ("9", "9", "9 (nur Überschrift „Streckung“)"),
   "Eine zentrische Streckung nimmt jede Länge mit demselben Faktor mal und lässt jeden Winkel, wie er ist.",
   "Für Dreiecke genügt: zwei Winkel stimmen überein. Für andere Vielecke braucht man Winkel und Seitenverhältnisse.",
   "Gleiche Form mit gleicher Größe verwechseln; bei Vierecken nur die Winkel prüfen (Rechteck und Quadrat).",
   "Verhältnis (Rechenregel 11). Maßstab (Planet Geld und Verhältnisse).",
   [(9, "E", "Dreiecke mit 3 cm, 4 cm, 5 cm und 6 cm, 8 cm, 10 cm: alle Seitenverhältnisse 1 : 2, also ähnlich", lambda: F(3, 6) == F(4, 8) == F(5, 10))]),
 G("Strahlensätze", ("9", "9", "9 (nur Überschrift „Streckung“)"),
   "Die Parallelen schneiden aus den Strahlen ähnliche Dreiecke heraus.",
   "Die schneidenden Geraden sind parallel. Wer die Parallelenstücke einbezieht, misst alle Strahlabschnitte vom Scheitel aus.",
   "Beim Satz mit den Parallelenstücken Teilabschnitte statt der Abschnitte vom Scheitel nehmen.",
   "Ähnlichkeit. Bruchgleichungen (Planet Algebra).",
   [(9, "E", "Abschnitte vom Scheitel: 2 cm und 3 cm auf dem einen Strahl, 4 cm und x auf dem anderen: 2 : 3 = 4 : x, also x = 6 cm", lambda: F(2, 3) == F(4, 6))], ["Ähnlichkeit"]),
 G("Vergrößern mit Faktor k", ("9", "9", "9 (nur Überschrift „Streckung“)"),
   "Eine Fläche hat zwei Richtungen, in denen sie wächst, ein Körper drei.",
   "Alle Längen werden mit demselben k > 0 malgenommen.",
   "Meinen, doppelte Länge gebe doppelte Fläche.",
   "Potenzen (Rechenregel 8). Flächen- und Raumeinheiten: k = 10.",
   [(5, "V", "Maßstab 1 : 100: 1 cm im Plan ist 1 m in Wirklichkeit", lambda: True), (9, "E", "k = 3: aus 2 cm werden 6 cm, aus 4 cm² werden 36 cm², aus 8 cm³ werden 216 cm³", lambda: (2 * 3, 4 * 9, 8 * 27) == (6, 36, 216))], ["Ähnlichkeit"]),
 G("Schwerpunkt", ("–", "9 (Gruppe I, auch 7)", "–"),
   "Die Verbindung zweier Seitenmitten ist parallel zur dritten Seite und halb so lang; daraus folgt mit dem Strahlensatz das Verhältnis 2 : 1.",
   "Gilt für jedes Dreieck. Das längere Stück liegt an der Ecke.",
   "Seitenhalbierende und Winkelhalbierende verwechseln.",
   "Koordinaten des Schwerpunkts: Mittelwert der drei Ecken.",
   [("R9", "E", "A(0 | 0), B(6 | 0), C(0 | 9): Schwerpunkt (2 | 3)", lambda: (F(0 + 6 + 0, 3), F(0 + 0 + 9, 3)) == (2, 3))], ["Strahlensätze"]),
 G("Satz des Pythagoras", ("9", "9", "9"),
   "Vier gleiche rechtwinklige Dreiecke lassen sich auf zwei Arten in ein Quadrat mit der Seite a + b legen: Einmal bleibt c² frei, einmal a² und b².",
   "Das Dreieck ist rechtwinklig; c liegt dem rechten Winkel gegenüber. Umkehrung: Gilt a² + b² = c², ist das Dreieck rechtwinklig.",
   "a + b = c rechnen. Die Hypotenuse falsch wählen.",
   "Gegenrechnung Wurzel (Rechenregel 12). Abstand zweier Punkte. Kosinussatz.",
   [(9, "E", "Katheten 3 cm und 4 cm: Hypotenuse 5 cm", lambda: 3 ** 2 + 4 ** 2 == 5 ** 2), (9, "E", "Umkehrung: 5 cm, 12 cm, 13 cm – wegen 25 + 144 = 169 rechtwinklig", lambda: 25 + 144 == 169),
    (9, "A", "Diagonale im Quadrat mit Seite 1 cm: √2 cm ≈ 1,41 cm", lambda: nah(math.sqrt(2), 1.41))]),
 G("Sinus, Kosinus, Tangens", ("9", "9", "9"),
   "Alle rechtwinkligen Dreiecke mit demselben spitzen Winkel sind ähnlich; ihre Seitenverhältnisse hängen deshalb nur vom Winkel ab.",
   "Rechtwinkliges Dreieck, spitzer Winkel. Gegenkathete und Ankathete richten sich nach dem betrachteten Winkel.",
   "Gegenkathete und Ankathete vertauschen. Taschenrechner nicht auf Grad eingestellt.",
   "Ähnlichkeit. Steigung einer Geraden: m = tan α (Planet Funktionen).",
   [(9, "E", "Dreieck 3 cm, 4 cm, 5 cm, Winkel gegenüber der 3-cm-Seite: sin = 3/5, cos = 4/5, tan = 3/4", lambda: nah(math.atan2(3, 4), math.asin(3 / 5), 9)),
    (9, "A", "Leiter 5 m lang, 60° zum Boden: Sie reicht 5 m · sin 60° ≈ 4,33 m hoch", lambda: nah(5 * sind(60), 4.33))], ["Ähnlichkeit"]),
 G("Zusammenhänge der Winkelfunktionen", ("9", "10 (Gruppe I)", NG),
   "Im rechtwinkligen Dreieck mit Hypotenuse 1 sind die Katheten sin α und cos α; der Satz des Pythagoras liefert sin² α + cos² α = 1.",
   "tan α ist nur erklärt, wenn cos α nicht null ist.",
   "sin² α als sin(α²) lesen.",
   "Satz des Pythagoras. Einheitskreis.",
   [(9, "E", "(3/5)² + (4/5)² = 1", lambda: F(3, 5) ** 2 + F(4, 5) ** 2 == 1), (9, "E", "(3/5) : (4/5) = 3/4", lambda: F(3, 5) / F(4, 5) == F(3, 4))], ["Sinus, Kosinus, Tangens", "Satz des Pythagoras"]),
 G("Einheitskreis", ("9", "10 (Gruppe I)", NG),
   "Dreht man den Radius 1 um den Winkel α, hat seine Spitze die Koordinaten (cos α | sin α). So bekommen auch Winkel über 90° einen Sinus und Kosinus.",
   "Radius 1; der Winkel wird von der positiven x-Achse aus gegen den Uhrzeigersinn gemessen.",
   "Das Vorzeichen im zweiten bis vierten Viertel übersehen.",
   "Sinus- und Kosinusfunktion (Planet Funktionen).",
   [(9, "E", "sin 150° = sin 30° = 0,5", lambda: nah(sind(150), 0.5, 9)), (9, "E", "cos 150° = −cos 30° ≈ −0,87", lambda: nah(cosd(150), -0.87))], ["Sinus, Kosinus, Tangens"]),
 G("Sinussatz und Kosinussatz", ("9", "10", "10"),
   "Eine Höhe teilt jedes Dreieck in zwei rechtwinklige; dort gelten Sinus, Kosinus und Pythagoras.",
   "Jedes Dreieck. Kosinussatz: c² = a² + b² − 2 · a · b · cos γ, mit γ zwischen a und b.",
   "Beim Sinussatz übersehen, dass zu einem Sinuswert zwei Winkel gehören können.",
   "Für γ = 90° wird der Kosinussatz zum Satz des Pythagoras. Kongruenzsätze sagen, wann die Angaben reichen.",
   [(9, "E", "a = 5 cm, b = 7 cm, γ = 60°: c² = 25 + 49 − 2 · 5 · 7 · 0,5 = 39, also c ≈ 6,24 cm", lambda: nah(math.sqrt(25 + 49 - 2 * 5 * 7 * cosd(60)), 6.24)),
    (9, "E", "γ = 90°: Wegen cos 90° = 0 bleibt c² = a² + b²", lambda: nah(cosd(90), 0, 9))], ["Satz des Pythagoras", "Sinus, Kosinus, Tangens"]),
 G("Additionstheoreme", ("–", "10 (nur Gruppe I)", "–"),
   "Zerlegt man die Drehung um α + β in zwei Drehungen nacheinander, ergeben sich die Formeln aus rechtwinkligen Dreiecken.",
   "Gilt für alle Winkel.",
   "sin(α + β) = sin α + sin β rechnen.",
   "Einheitskreis.",
   [("R10", "E", "sin(30° + 60°) = sin 30° · cos 60° + cos 30° · sin 60° = ¼ + ¾ = 1", lambda: nah(sind(30) * cosd(60) + cosd(30) * sind(60), 1, 9))], ["Einheitskreis"]),
 G("Winkel aus Sinus oder Kosinus", ("9, 10", "10 (Gruppe I)", NG),
   "Am Einheitskreis liegen zu einer Höhe (Sinus) zwei Punkte, links und rechts; zu einer x-Koordinate (Kosinus) zwei Punkte, oben und unten.",
   "Der Wert liegt zwischen −1 und 1. Bei genau 1 oder −1 gibt es in einer vollen Drehung nur einen Winkel.",
   "Nur den Winkel nennen, den der Taschenrechner anzeigt.",
   "Gegenrechnung (Rechenregel 12). Einheitskreis.",
   [(9, "E", "sin α = 0,5 zwischen 0° und 360°: α = 30° oder α = 150°", lambda: nah(sind(30), 0.5, 9) and nah(sind(150), 0.5, 9))], ["Einheitskreis"]),
]

PLANETEN = [("Fläche und Raum", "planet-flaeche-und-raum.md", IDEE_F, GESETZE_F), ("Geometrie", "planet-geometrie.md", IDEE_G, GESETZE_G)]


def klasse_gym(lp):
    return int(lp[0][:2].strip(" (,")) if lp[0][0].isdigit() else None


def gesetz_text(planet, m):
    name = m["name"]
    satz = SATZ[name]
    ib = gb.klassen(satz[2])[2]
    g, r1, r2 = m["lp"]
    z = [f"#### {gb.NR[name]} · {name}", "", f"> **{gb.tab(satz[1])}**", "",
         f"Gymnasium: {g} · Realschule Gruppe I: {r1} · Realschule Gruppe II/III: {r2} · IB (Planung der App): {'Jahr ' + ib if ib != '–' else '–'}", "",
         f"**Warum das gilt:** {m['warum']}", "", f"**Voraussetzung:** {m['vor']}", "", f"**Häufiger Fehler:** {m['fehler']}", "", f"**Verwandt:** {m['verwandt']}", "",
         "| Klasse | Art | Beispiel |", "|---|---|---|"]
    z += [f"| {k if isinstance(k, int) else 'Realschule ' + k[1:]} | {ART[a]} | {gb.tab(text)} |" for k, a, text, _ in m["bsp"]]
    sonne_r = [f"Rechenregel {s} {SONNE[s - 1]}" for s in satz[3]]
    z += ["", f"**Möglicher Erklärweg über:** {', '.join([gb.NR[w] + ' ' + w for w in m['weg']] + sonne_r) or '–'}"]
    return "\n".join(z)


gesamt_bsp = 0
for planet, datei, ideen_extra, gesetze in PLANETEN:
    ideen = gb.IDEEN[planet]
    namen = [g[0] for _, gs in gb.P[planet] for g in gs]
    assert [m["name"] for m in gesetze] == namen, (planet, set(namen) ^ {m["name"] for m in gesetze})
    assert len(ideen_extra) == len(ideen)
    von = {m["name"]: m for m in gesetze}
    for m in gesetze:
        assert all(m[k] for k in ("warum", "vor", "fehler", "verwandt", "bsp")) and len(m["lp"]) == 3, m["name"]
        assert all(w in von for w in m["weg"]), (m["name"], m["weg"])
        kg = klasse_gym(m["lp"])
        for k, a, text, probe in m["bsp"]:
            assert probe() is True, (m["name"], text)
            assert a in ART
            if isinstance(k, int) and kg:                      # Art passt zur Klasse der Einführung am Gymnasium
                assert (a == "V") == (k < kg), (m["name"], k, a, kg)
            if isinstance(k, str):
                assert kg is None, m["name"]                    # Realschul-Beispiel nur, wo das Gymnasium das Gesetz nicht hat
        gesamt_bsp += len(m["bsp"])
    n_bsp = sum(len(m["bsp"]) for m in gesetze)
    teile = []
    for nr, ((kurz, merk, ns), extra) in enumerate(zip(ideen, ideen_extra), 1):
        teile += [f"## Idee {nr} · {kurz}", "", f"> **{gb.IDEE_SPRUCH[kurz][0]}**", "", f"**Genau gesagt:** {merk}", "", f"**Warum diese Idee trägt:** {extra['warum']}", "", f"**Trägt {len(ns)} Gesetze:** {', '.join(gb.NR[n] + ' ' + n for n in ns)}", "",
                  "**Zeichen-Vorgabe**", zeichnung_text(extra["z"]), "", "### Die Gesetze dieser Idee (Ebene 2)", ""]
        teile += [gesetz_text(planet, von[n]) + "\n" for n in ns]
    open(os.path.join(HIER, datei), "w", encoding="utf-8").write(f"""# Gesetzbuch · Planet „{planet}“ – ausgearbeitet in zwei Ebenen

Mathe-Profi, 26.11.2026 (Auftrag 11). Erzeugt von `planeten.py`; {n_bsp} Beispiele, jedes nachgerechnet (Lauf „OK“).

## Der Planet in einer Minute

**Ebene 1 – {len(ideen)} tragende Ideen:**

{chr(10).join(f"{i}. **{gb.IDEE_SPRUCH[kurz][0]}**  {chr(10)}   *Genau gesagt:* {merk}" for i, (kurz, merk, _) in enumerate(ideen, 1))}

**Ebene 2 – {len(gesetze)} Gesetze**, jedes genau einer Idee zugeordnet.

## Wie die Angaben zu lesen sind

- **Klassen:** aus der Lehrplan-Kopie, die in der App liegt (Gymnasium, Realschule Wahlpflichtfächergruppe I und II/III getrennt). **Nicht an LehrplanPLUS selbst geprüft** – der Abruf war in dieser Sitzung nicht möglich. „{NG}“ heißt: In der Kopie steht dazu kein Eintrag; es heißt nicht sicher, dass es im Lehrplan fehlt. „nur Überschrift“: Die Kopie enthält für diese Gruppe nur die Überschrift des Lernbereichs.
- **IB:** Jahr laut Planung der App. Das IB schreibt keine verbindliche Jahresfolge vor.
- **Art der Beispiele:** Vorwissen (kommt vor, bevor das Gesetz gelehrt wird) · Einführung · Anwendung (später). Klassen der Beispiele: Gymnasium; wo das Gymnasium das Gesetz nicht hat, Realschule.
- **Möglicher Erklärweg:** worüber man das Gesetz erklären kann. Das ist **keine Lernvoraussetzung und keine Sperre**.

{chr(10).join(teile)}
## Nicht geprüft

- Klassen nicht an LehrplanPLUS selbst (siehe oben).
- Die Begründungen sind Schul-Begründungen, keine Beweise.
- Zeichnungen nur in Worten vorgegeben, nichts gezeichnet oder nachgemessen. Merksätze nicht mit einem Kind erprobt.
""")
    print(f"{planet}: {len(ideen)} Ideen, {len(gesetze)} Gesetze, {n_bsp} Beispiele")
print("OK")
