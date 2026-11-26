"""Mathe-Profi, Aufträge 8 und 9: individueller Lehrplan beider Kinder (zweite Fassung nach Gegenprüfung).

Aufruf: python3 -I inhalte/mathe-profi/lehrplan-kinder/plan.py
Hält Flüge, Themen, Routen und die Voraussetzungen der App als Daten, prüft die Routen dagegen und schreibt
route.md, einstell-liste.md (vollständige Soll-Liste je Kind) und diagnose-regel.md.
Nur Plan-Daten. Keine Namen, keine Quoten, keine Ergebnisse.
"""
import json
import os
import re

HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))

# Etappen je Thema (aus der App gelesen, 26.11.2026)
ET = {"zahlen.natuerlich": 13, "zahlen.ganz": 11, "zahlen.rechengesetze": 14, "zahlen.potenzen_basis": 7, "zahlen.teilbarkeit": 7, "bruch.brueche": 14, "bruch.dezimal": 8, "bruch.rechnen": 12,
      "zahlen.potenzen_zehner": 7, "terme.potenzgesetze": 3, "zahlen.wurzeln_basis": 6, "zahlen.reell": 8, "groessen.einheiten": 8, "groessen.proportional": 5, "groessen.proportional_teil2": 3,
      "bruch.prozent": 6, "finanzen.zinsen": 8, "groessen.verhaeltnisse": 6, "groessen.indirekt": 7, "bruch.prozent_grundwert": 8, "gleichungen.einfach": 5, "terme.aufstellen": 6,
      "terme.potenzgesetze_natuerlich": 5, "terme.umformen": 5, "gleichungen.linear": 6, "terme.umformen_teil2": 4, "gleichungen.ungleichungen": 7, "zahlen.intervalle": 4, "terme.bruchterme": 7,
      "terme.potenzgesetze_ganzzahlig": 5, "gleichungen.bruch": 7, "gleichungen.formeln": 5, "gleichungen.lgs2": 9, "terme.quadratische_extreme": 5, "gleichungen.reinquadratisch": 6,
      "gleichungen.quadratisch": 8, "funktionen.grundbegriffe": 9, "funktionen.linear": 11, "funktionen.scharen": 6, "funktionen.gebrochen": 5, "funktionen.quadratisch": 9,
      "funktionen.transformation": 6, "geometrie.grundbegriffe": 7, "geometrie.ortslinien": 6, "abbildungen.kongruenz": 6, "abbildungen.kongruenz_teil2": 3, "abbildungen.kongruenz_teil3": 3,
      "geometrie.winkel": 7, "geometrie.winkelsaetze": 9, "geometrie.konstruktion": 5, "geometrie.konstruktion_teil2": 2, "geometrie.kreis": 6, "abbildungen.aehnlichkeit": 9, "trigo.pythagoras": 6,
      "abbildungen.vektoren": 6, "abbildungen.determinanten2": 6, "messen.flaechen": 7, "messen.koerper_darstellung": 6, "messen.prisma_zylinder": 7, "messen.prisma_zylinder_teil2": 1,
      "messen.koerper_berechnung": 5, "messen.kreisberechnung": 6, "messen.flaechen_vielecke": 8, "messen.volumen": 7, "daten.darstellen": 6, "stochastik.kombinatorik": 7, "daten.kennwerte": 3,
      "daten.stichproben": 5, "stochastik.grundbegriffe": 3, "stochastik.grundbegriffe_teil2": 4, "stochastik.verknuepft": 11, "daten.boxplot": 6, "mengen.grundbegriffe": 5}

# Flug (block.schluessel): (Titel, Jahrgang des Flugs in der App, Themen in der Reihenfolge der App, Schularten)
FLUG = {
    "z1": ("Natürliche und ganze Zahlen", 5, ["zahlen.natuerlich", "zahlen.ganz", "zahlen.rechengesetze", "zahlen.potenzen_basis"], "G5 R5 I1–2"),
    "z2": ("Teilbarkeit", 5, ["zahlen.teilbarkeit"], "G5 R5 I1"), "z3": ("Brüche", 6, ["bruch.brueche"], "G6 R6 I1"), "z4": ("Dezimalzahlen", 6, ["bruch.dezimal"], "G6 R6 I1"),
    "z5": ("Rechnen mit Brüchen", 6, ["bruch.rechnen"], "G6 R6 I2"), "z6": ("Potenzen", 6, ["zahlen.potenzen_zehner", "terme.potenzgesetze"], "G6 R7 I3–4"),
    "z7": ("Wurzeln und reelle Zahlen", 9, ["zahlen.wurzeln_basis", "zahlen.reell"], "G9 R9 I1/4"),
    "g1": ("Größen und Einheiten", 5, ["groessen.einheiten"], "G5 R5 I2"), "g2": ("Dreisatz und direkte Proportionalität", 5, ["groessen.proportional"], "G5 R5 I2"),
    "g2-teil2": ("Dreisatz · Teil 2", 5, ["groessen.proportional_teil2"], "G5 R6 I2"), "g3": ("Prozent", 6, ["bruch.prozent"], "G6 R6 I1"), "g4": ("Zinsen", 6, ["finanzen.zinsen"], "R7 I4"),
    "g5": ("Verhältnisse und Raten", None, ["groessen.verhaeltnisse"], "I2"), "g7": ("Indirekte Proportionalität", 8, ["groessen.indirekt"], "G8 R7 I4"),
    "g8": ("Prozent mit verändertem Grundwert", 7, ["bruch.prozent_grundwert"], "G7 R7 I3"),
    "a1": ("Einfache Gleichungen", 5, ["gleichungen.einfach"], "G5 R6 I1"), "a2": ("Terme aufstellen", 7, ["terme.aufstellen"], "G7 R6 I1"),
    "a3": ("Terme umformen", 7, ["terme.potenzgesetze_natuerlich", "terme.umformen", "gleichungen.linear"], "G7 R7 I1–3"), "a3-teil2": ("Terme umformen · Teil 2", 7, ["terme.umformen_teil2"], "G7 R8 I4"),
    "a4": ("Lineare Ungleichungen", 8, ["gleichungen.ungleichungen", "zahlen.intervalle"], "G8 R7 I4"),
    "a5": ("Bruchterme und Formeln", 8, ["terme.bruchterme", "terme.potenzgesetze_ganzzahlig", "gleichungen.bruch", "gleichungen.formeln"], "G8 R7–8 I4"),
    "a6": ("Gleichungssysteme", 8, ["gleichungen.lgs2"], "G8 R9 I4"), "a10": ("Quadratische Terme und Extremwerte", 8, ["terme.quadratische_extreme"], "R8"),
    "a7": ("Quadratische Gleichungen", 9, ["gleichungen.reinquadratisch", "gleichungen.quadratisch"], "G9 R9 I4"),
    "f1": ("Funktionsbegriff", 8, ["funktionen.grundbegriffe"], "G8 R8 I3"), "f2": ("Lineare Funktionen", 8, ["funktionen.linear", "funktionen.scharen"], "G8 R8 I3"),
    "f3": ("Hyperbeln", 8, ["funktionen.gebrochen"], "G8 I4"), "f4": ("Parabeln", 9, ["funktionen.quadratisch", "funktionen.transformation"], "G9 R9 I4"),
    "ge1": ("Formen und Grundbegriffe", 5, ["geometrie.grundbegriffe", "geometrie.ortslinien"], "G5 R5/7 I1"), "ge2": ("Spiegeln und Symmetrie", 7, ["abbildungen.kongruenz"], "G7 R6 I3"),
    "ge2-teil2": ("Spiegeln und Symmetrie · Teil 2", 7, ["abbildungen.kongruenz_teil2"], "G7 R7 I3"), "ge2-teil3": ("Spiegeln und Symmetrie · Teil 3", 7, ["abbildungen.kongruenz_teil3"], "G7 R8 I3"),
    "ge3": ("Winkel", 5, ["geometrie.winkel"], "G5/7 R5 I1"), "ge4": ("Dreiecke, Vierecke und Konstruktion", 7, ["geometrie.winkelsaetze", "geometrie.konstruktion"], "G7 R7 I2"),
    "ge4-teil2": ("Dreiecke, Vierecke und Konstruktion · Teil 2", 7, ["geometrie.konstruktion_teil2"], "G7 R8"), "ge5": ("Kreis", 7, ["geometrie.kreis"], "G7 R7 I4"),
    "ge6": ("Ähnlichkeit", 9, ["abbildungen.aehnlichkeit"], "G9 R9 I3"), "ge7": ("Pythagoras", 9, ["trigo.pythagoras"], "G9 R9 I3"),
    "ge9": ("Vektoren, Verschiebung und Drehung", 7, ["abbildungen.vektoren", "abbildungen.determinanten2"], "R7"),
    "r1": ("Umfang und Fläche", 5, ["messen.flaechen"], "G5 R5 I1"), "r2": ("Körper und Netze", 8, ["messen.koerper_darstellung", "messen.prisma_zylinder"], "G8 R5/9 I3"),
    "r2-teil2": ("Körper und Netze · Teil 2", 8, ["messen.prisma_zylinder_teil2"], "R9"), "r3": ("Volumen und Oberfläche", 5, ["messen.koerper_berechnung"], "G5 R6 I1"),
    "r4": ("Kreis und Zylinder", 8, ["messen.kreisberechnung"], "G8 R9 I3"), "r7": ("Flächen und Volumen", 6, ["messen.flaechen_vielecke", "messen.volumen"], "G6 R6"),
    "d1": ("Daten darstellen", 6, ["daten.darstellen"], "G6 R5 I1"), "d2": ("Zählen", 5, ["stochastik.kombinatorik"], "G5 R5 I2"), "d3": ("Mittelwert", 6, ["daten.kennwerte"], "G6 R7 I2"),
    "d4": ("Stichproben", 7, ["daten.stichproben"], "R7 I2"), "d5": ("Zufall und Laplace", 8, ["stochastik.grundbegriffe"], "G8 R8 I2"),
    "d5-teil2": ("Zufall und Laplace · Teil 2", 8, ["stochastik.grundbegriffe_teil2"], "G8 R9 I2"), "d6": ("Verknüpfte Ereignisse", 9, ["stochastik.verknuepft"], "G9 R9 I4"),
    "d10": ("Median, Quartile, Boxplot", 7, ["daten.boxplot"], "G7 R7 I4"), "e1": ("Mengen und Venn-Diagramme", None, ["mengen.grundbegriffe"], "I1"),
}
assert all(t in ET for f in FLUG.values() for t in f[2])
THEMA_FLUG = {t: f for f, v in FLUG.items() for t in v[2]}

# Voraussetzungen laut App (Tabelle voraussetzung, gelesen 26.11.2026): Thema → [(braucht, h = hart / e = empfohlen)]. Nur Themen der Routen.
V_APP = """zahlen.ganz:zahlen.natuerlich h|zahlen.rechengesetze:zahlen.natuerlich h|zahlen.potenzen_basis:zahlen.rechengesetze h|geometrie.ortslinien:geometrie.grundbegriffe h
zahlen.teilbarkeit:zahlen.rechengesetze e|gleichungen.einfach:zahlen.rechengesetze h|groessen.einheiten:zahlen.rechengesetze e|geometrie.winkel:geometrie.grundbegriffe e
messen.flaechen:geometrie.grundbegriffe e|groessen.proportional:groessen.einheiten h|groessen.proportional_teil2:groessen.proportional h|messen.koerper_berechnung:messen.flaechen h
messen.koerper_darstellung:geometrie.grundbegriffe e|terme.aufstellen:zahlen.rechengesetze e|bruch.brueche:zahlen.rechengesetze e,zahlen.teilbarkeit e|bruch.dezimal:bruch.brueche e
daten.kennwerte:bruch.dezimal e,daten.darstellen e|bruch.rechnen:bruch.brueche h,bruch.dezimal e,zahlen.ganz e|abbildungen.kongruenz:geometrie.grundbegriffe e
bruch.prozent:bruch.brueche h,bruch.dezimal e|messen.flaechen_vielecke:messen.flaechen e|messen.volumen:groessen.einheiten e,messen.flaechen e
zahlen.potenzen_zehner:bruch.dezimal e,zahlen.potenzen_basis h|terme.potenzgesetze:bruch.brueche e,zahlen.potenzen_basis h,zahlen.rechengesetze h|finanzen.zinsen:bruch.prozent h
terme.bruchterme:bruch.rechnen h,terme.umformen_teil2 h|terme.potenzgesetze_ganzzahlig:terme.potenzgesetze e,terme.potenzgesetze_natuerlich h
gleichungen.bruch:gleichungen.linear h,terme.bruchterme h|gleichungen.formeln:gleichungen.linear h,terme.umformen e|gleichungen.ungleichungen:gleichungen.linear h
zahlen.intervalle:zahlen.ganz e|bruch.prozent_grundwert:bruch.prozent h|funktionen.grundbegriffe:terme.aufstellen h|geometrie.winkelsaetze:geometrie.winkel e
geometrie.konstruktion:abbildungen.kongruenz e,geometrie.winkel e,geometrie.winkelsaetze e|funktionen.linear:funktionen.grundbegriffe h,gleichungen.linear h
gleichungen.lgs2:funktionen.linear e,gleichungen.linear h|groessen.indirekt:groessen.proportional_teil2 h|funktionen.gebrochen:funktionen.grundbegriffe e,groessen.indirekt e
stochastik.grundbegriffe:bruch.brueche h|geometrie.kreis:geometrie.grundbegriffe e,geometrie.ortslinien e,geometrie.winkelsaetze e|stochastik.grundbegriffe_teil2:stochastik.grundbegriffe h
messen.kreisberechnung:messen.flaechen h|messen.prisma_zylinder:messen.flaechen_vielecke e,messen.kreisberechnung e,messen.volumen e|terme.quadratische_extreme:terme.umformen_teil2 h
daten.boxplot:daten.kennwerte h|geometrie.konstruktion_teil2:geometrie.konstruktion h|abbildungen.kongruenz_teil2:abbildungen.kongruenz h
abbildungen.kongruenz_teil3:abbildungen.kongruenz h,abbildungen.kongruenz_teil2 h|messen.prisma_zylinder_teil2:messen.prisma_zylinder h|daten.stichproben:daten.darstellen e,daten.kennwerte e
abbildungen.determinanten2:abbildungen.kongruenz_teil2 e,messen.flaechen e|zahlen.wurzeln_basis:zahlen.potenzen_basis e|zahlen.reell:zahlen.wurzeln_basis h|trigo.pythagoras:zahlen.wurzeln_basis h
gleichungen.quadratisch:gleichungen.linear h,terme.umformen_teil2 h,zahlen.wurzeln_basis h|funktionen.quadratisch:funktionen.grundbegriffe h,funktionen.linear e,terme.umformen_teil2 e
abbildungen.aehnlichkeit:abbildungen.kongruenz e|stochastik.verknuepft:stochastik.grundbegriffe h|terme.umformen:terme.aufstellen h,terme.potenzgesetze_natuerlich h
terme.umformen_teil2:terme.umformen h|gleichungen.linear:gleichungen.einfach h,terme.aufstellen h,zahlen.ganz e|terme.potenzgesetze_natuerlich:terme.aufstellen h,terme.potenzgesetze h"""
V = {}
for eintrag in V_APP.replace("\n", "|").split("|"):
    thema, rest = eintrag.split(":")
    V[thema] = [tuple(x.split(" ")) for x in rest.split(",")]
    assert thema in ET and all(b in ET and a in "he" for b, a in V[thema]), eintrag
# Bei abbildungen.kongruenz_teil3 nennt die App je Schulart verschiedene Stärken (voraussetzung_schulart); hier beide als hart – die strengere Lesart.

P, K = "Pflicht", "Kür"
# Route: (Abschnitt, Prüfpunkt, [(Flug, Art, heute, Änderung, ausgelassene Themen, Warum)])
KIND1 = [
    ("1 · Rechnen festmachen, Geometrie beginnen", "Blatt B des Papier-Tests (Auftrag 5) – wenn Blatt A am Anfang geschrieben wurde", [
        ("z1", P, "läuft", "bleibt", [], "Zu Ende bringen. Hier liegen die Regeln 1 bis 6 an Zahlen – das Fundament für alles Weitere."),
        ("ge1", P, "Platz 4", "vorgezogen", [], "Erster Geometrie-Flug, braucht nichts vorher. Wechsel nach viel Rechnen; Zeichnen kam bisher gar nicht vor."),
        ("z2", P, "Platz 2", "bleibt", [], "Braucht Mal und Geteilt aus z1. Voraussetzung für das Kürzen in den Brüchen."),
        ("a1", P, "Platz 3", "bleibt", [], "Regeln 7 Waage und 8 Umkehren an Zahlen. Die Brücke zu den späteren Gleichungen mit x."),
        ("d1", P, "Platz 17", "vorgezogen", [], "Realschule Klasse 5 (Gymnasium 6). Leicht, eigenständig, bringt Diagramme – die fehlen bisher."),
    ]),
    ("2 · Messen und Verhältnis", "eigener Papier-Test „Messen“ (noch zu bauen): Einheiten, Winkel, Fläche, Dreisatz", [
        ("g1", P, "Platz 6", "bleibt", [], "Einheiten umrechnen ist Voraussetzung für Fläche, Volumen und Dreisatz (Regel 13 Stellenwert)."),
        ("ge3", P, "Platz 5", "bleibt", [], "Baut auf ge1. Winkel messen und zeichnen – am Tisch mit Geodreieck."),
        ("r1", P, "Platz 9", "vorgezogen", [], "Braucht ge1. Erste Formeln (Rechteck) – Formel-Koffer beginnt."),
        ("g2", P, "Platz 7", "bleibt", [], "Regel 14 Verhältnis an Zahlen. Braucht Einheiten."),
        ("g2-teil2", P, "Platz 8", "bleibt", [], "Schließt den Dreisatz ab (Realschule Klasse 6)."),
        ("d2", P, "Platz 11", "bleibt", [], "Eigenständig, kein Rechenweg. Auflockerung zum Abschluss des Abschnitts."),
    ]),
    ("3 · Abschluss Klasse 5 und Vorgriff", "Abschluss-Arbeit Klasse 5 auf Papier (noch zu bauen), danach Entscheidung über Klasse 6", [
        ("r3", P, "Platz 10", "bleibt", [], "Braucht r1. Letzter Pflicht-Flug Gymnasium Klasse 5."),
        ("r2", P, "entfernt", "neu im Plan", ["messen.prisma_zylinder"], "Realschule Klasse 5 (Gymnasium 8): Körper, Netze, Ansichten. Nur dieser Teil; Prisma und Zylinder bleiben für später."),
        ("a2", P, "entfernt", "neu im Plan", [], "Realschule Klasse 6, IB Jahr 1 (Gymnasium 7). Führt die Variable ein – die Brücke von der Zahl zum Buchstaben."),
        ("e1", K, "Zusatz", "bleibt Zusatz", [], "IB Jahr 1. Kurz, eigenständig, als Abwechslung."),
    ]),
    ("4 · Klasse 6: Brüche", "Papier-Test „Brüche“ (noch zu bauen)", [
        ("z3", P, "Platz 12", "bleibt", [], "Braucht Teilbarkeit. Regel 10 Wert bleibt."),
        ("z4", P, "Platz 13", "bleibt", [], "Braucht z3. Regel 13 Stellenwert."),
        ("d3", P, "Platz 18", "vorgezogen", [], "Braucht Dezimalzahlen. Kurz (drei Etappen), Wechsel zwischen zwei Bruch-Flügen."),
        ("z5", P, "Platz 14", "bleibt", [], "Braucht z3. Regel 11 Bruchrechnen – der schwerste Flug der Klasse 6."),
        ("ge2", P, "entfernt", "neu im Plan", [], "Realschule Klasse 6 (Gymnasium 7). Geometrie zwischen den Rechen-Flügen."),
    ]),
    ("5 · Klasse 6: Anwenden", "Abschluss-Arbeit Klasse 6 auf Papier (noch zu bauen)", [
        ("g3", P, "Platz 19", "bleibt", [], "Braucht Brüche und Dezimalzahlen."),
        ("r7", P, "Platz 16", "bleibt", [], "Braucht r1 und Einheiten. Dreieck, Parallelogramm, Trapez – Formel-Koffer."),
        ("z6", P, "Platz 15", "bleibt", [], "Regel 12 Potenz. Gymnasium 6, Realschule 7."),
        ("g5", K, "Zusatz", "bleibt Zusatz", [], "IB Jahr 2. Passt hinter Dreisatz und Brüche."),
        ("g4", K, "Platz 20", "bleibt letzter Platz, gilt als Kür", [], "Realschule 7, IB Jahr 4; laut App kein Gymnasium-Stoff der Klasse 6. Braucht Prozent."),
    ]),
]
KIND2 = [
    ("1 · Klasse-8-Algebra abschließen, Geometrie öffnen", "Blatt B des Papier-Tests (Auftrag 5). Am Anfang des Abschnitts: Blatt A und der amtliche Test als Eingangsdiagnose", [
        ("a5", P, "läuft", "bleibt", [], "Zu Ende bringen: Bruchgleichungen und Formeln. Regeln 7, 8, 10, 14."),
        ("ge2", P, "Platz 20", "vorgezogen", [], "Klasse 7. Spiegeln und Grundkonstruktionen (Mittelsenkrechte, Lot, Winkelhalbierende): Die App empfiehlt sie vor der Konstruktion in ge4. Öffnet die Geometrie."),
        ("a4", P, "Platz 3", "bleibt", [], "Gymnasium 8, Realschule 7. Braucht nur lineare Gleichungen. Regeln 1 und 2 in neuem Gewand."),
        ("g8", P, "Platz 23", "vorgezogen", [], "Klasse 7. Prozent mit verändertem Grundwert ist im Jahrgangsstufentest jedes Jahr dabei."),
        ("g2-teil2", P, "Platz 24", "vorgezogen", [], "Drei Etappen. Die App verlangt ihn zwingend vor g7; er ist offen und nicht als gekonnt belegt. Passt hinter Prozent (Verhältnis)."),
        ("f1", P, "Platz 26", "vorgezogen", [], "Einstieg in das größte Gebiet der Klasse 8. Früh beginnen, damit es nicht am Ende gedrängt kommt."),
    ]),
    ("2 · Funktionen und Dreiecke", "amtlicher Test der Jahrgangsstufe 8, zweiter Jahrgang – Vergleich mit dem ersten", [
        ("ge4", P, "entfernt", "wieder im Plan", [], "Klasse 7. Winkelsätze und Konstruktion. Steht hinter ge2 und – falls die Diagnose es verlangt – hinter ge3. Bis hierher liegt das Ergebnis der Diagnose vor."),
        ("f2", P, "Platz 27", "bleibt hinter f1", ["funktionen.scharen"], "Braucht f1. Kern der Klasse 8 in allen drei Schularten. Regel 14 Verhältnis als Steigung."),
        ("a6", P, "Platz 4", "nach hinten", [], "Die App empfiehlt f2 davor (Lösen am Graphen). Gymnasium 8, Realschule 9."),
        ("g7", P, "Platz 25", "bleibt", [], "Gymnasium 8, Realschule 7. Braucht g2-teil2 (Abschnitt 1). Voraussetzung für Hyperbeln."),
        ("f3", P, "Platz 28", "bleibt", [], "Braucht g7 und f1. Schließt an Bruchterme an."),
        ("d5", P, "entfernt", "wieder im Plan", [], "Gymnasium 8. Kurz (drei Etappen). Daten und Zufall fehlen sonst in Klasse 8 ganz."),
    ]),
    ("3 · Kreis, Raum und Abschluss Klasse 8", "Abschluss-Arbeit Klasse 8 auf Papier (noch zu bauen)", [
        ("ge5", P, "entfernt", "wieder im Plan", [], "Klasse 7. Braucht Winkelsätze (ge4). Thaleskreis – typisch für Begründungsaufgaben."),
        ("d5-teil2", P, "entfernt", "neu im Plan", [], "Schließt Laplace ab (Realschule 9)."),
        ("r4", P, "entfernt", "wieder im Plan", [], "Gymnasium 8. Kreisumfang und Kreisfläche – Formel-Koffer. Vor r2, weil der Zylinder die Kreisfläche braucht."),
        ("r2", P, "entfernt", "wieder im Plan", [], "Gymnasium 8. Netze, Prisma, Zylinder – beide Themen."),
        ("a10", P, "Platz 5", "nach hinten", [], "Realschule 8. Braucht die binomischen Formeln; bereitet Parabeln vor."),
        ("d10", P, "entfernt", "wieder im Plan", [], "Klasse 7. Eigenständig; braucht nur den Mittelwert."),
    ]),
    ("4 · Ergänzung Realschule und IB", "keiner – Ergänzung und Kür", [
        ("ge4-teil2", P, "entfernt", "neu im Plan", [], "Schließt die Konstruktion ab (Realschule 8)."),
        ("ge2-teil2", P, "Platz 21", "nach hinten", [], "Realschule 7."),
        ("ge2-teil3", P, "Platz 22", "nach hinten", [], "Realschule 8."),
        ("r2-teil2", K, "entfernt", "neu, gilt als Kür", [], "Realschule 9. Eine Etappe."),
        ("d4", K, "entfernt", "wieder im Plan, gilt als Kür", [], "Realschule 7, IB Jahr 2. Eigenständig."),
        ("ge9", K, "Platz 6 und Zusatz", "aus der normalen Route nehmen, bleibt Zusatz", ["abbildungen.determinanten2"], "Nur Realschule 7. Drin ist die Verschiebung mit Vektoren; die Determinanten bleiben ausgelassen, bis die Lehrplan-Stelle geprüft ist."),
    ]),
]
KIND2_SPAETER = [  # Abschnitt 5: nicht jetzt einstellen
    ("z7", [], "Einstieg Klasse 9 in allen drei Schularten."), ("ge7", [], "Braucht Wurzeln. Geometrie im Wechsel."),
    ("a7", [], "Beide Themen: erst x² = a (reinquadratisch), dann die allgemeine quadratische Gleichung. Braucht Wurzeln und binomische Formeln. Regel 15 Nullprodukt."),
    ("f4", ["funktionen.transformation"], "Drin ist die quadratische Funktion – das sind die Parabeln. Ausgelassen wird die Transformation (kein Lehrplan-Jahrgang in der App)."),
    ("ge6", [], "Regel 14 Verhältnis in der Geometrie. Die App empfiehlt Spiegeln (ge2) davor."), ("d6", [], "Braucht Laplace."),
]
# Kind 2: Einträge außerhalb der Abschnitte, die in der normalen Route stehen bleiben müssen (sonst entfernt die Plan-Funktion sie)
KS, KW, ER = "kann schon", "kann – wiederholen", "erledigt"
KIND2_BESTAND = [
    ("a3", ER, [], "bleibt"), ("a3-teil2", ER, [], "bleibt"), ("a2", KS, [], "bleibt"),
    ("z6", KW, [], "bleibt – Wiederholung gesetzt für beide Themen"), ("g3", KW, [], "bleibt – Wiederholung gesetzt"), ("d1", KW, [], "bleibt – Wiederholung gesetzt"),
    ("d3", KW, [], "bleibt – Wiederholung gesetzt"), ("r7", KW, [], "bleibt – Wiederholung gesetzt für beide Themen"), ("g4", KW, [], "bleibt – Wiederholung gesetzt"),
    ("z1", KS, [], "bleibt"), ("z2", KS, [], "bleibt"), ("z3", KS, [], "bleibt"), ("z4", KS, [], "bleibt"), ("z5", KS, [], "bleibt"), ("g1", KS, [], "bleibt"), ("g2", KS, [], "bleibt"),
    ("a1", KS, [], "bleibt"), ("ge1", KS, [], "bleibt"), ("r1", KS, [], "bleibt"), ("r3", KS, [], "bleibt"), ("d2", KS, [], "bleibt"),
    ("ge3", KW, [], "**neu: von „offen“ auf „kann – wiederholen“** – gilt bis zum Ergebnis der Diagnose, siehe diagnose-regel.md"),
]


def themen(f, aus):
    assert all(a in FLUG[f][2] for a in aus), (f, aus)
    return [t for t in FLUG[f][2] if t not in aus]


def etappen(f, aus=()):
    return sum(ET[t] for t in themen(f, list(aus)))


def pruefe(route, bestand=(), spaeter=()):
    """Jeder Flug höchstens einmal; jede Voraussetzung der App (hart und empfohlen) steht vorher oder ist Bestand; Abschnitte 4–6 Flüge."""
    da, fluege, meld = set(), [], []
    for f, art, aus, _ in bestand:
        da |= set(themen(f, aus))
        fluege.append(f)
    folge = [(f, aus) for _, _, fl in route for f, _, _, _, aus, _ in fl] + [(f, aus) for f, aus, _ in spaeter]
    for titel, _, fl in route:
        assert 4 <= len(fl) <= 6, titel
    for f, aus in folge:
        assert f not in fluege, f
        fluege.append(f)
        for t in themen(f, aus):                       # Themen in der Reihenfolge der App
            for b, staerke in V.get(t, []):
                if b not in da:
                    meld.append((f, t, b, staerke))
            da.add(t)
    return fluege, meld


f1, m1 = pruefe(KIND1)
f2, m2 = pruefe(KIND2, KIND2_BESTAND, KIND2_SPAETER)
assert m1 == [], m1
assert m2 == [], m2          # keine harte und keine empfohlene Voraussetzung der App wird verletzt
# Gegenprobe: Die alte Lage – g7 ohne g2-teil2 – muss der Prüfer finden.
_, probe = pruefe([("x", "", [("a5", P, "", "", [], "w"), ("f1", P, "", "", [], "w"), ("g7", P, "", "", [], "w"), ("f3", P, "", "", [], "w")])], KIND2_BESTAND)
assert ("g7", "groessen.indirekt", "groessen.proportional_teil2", "h") in probe
# Parabeln sind im sichtbaren Inhalt von f4, beide Themen in a7, Vektoren in ge9
assert themen("f4", ["funktionen.transformation"]) == ["funktionen.quadratisch"] and len(themen("a7", [])) == 2 and themen("ge9", ["abbildungen.determinanten2"]) == ["abbildungen.vektoren"]

T = lambda liste: ", ".join(f"`{t}`" for t in liste) or "–"


def tabelle(route):
    out, gesamt, n = [], [], 0
    for titel, pruefpunkt, fl in route:
        et = sum(etappen(f, aus) for f, _, _, _, aus, _ in fl)
        pfl = sum(etappen(f, aus) for f, art, _, _, aus, _ in fl if art == P)
        gesamt.append((titel, len(fl), et, pfl))
        out.append(f"\n### Abschnitt {titel}\n\n{len(fl)} Flüge, {et} Etappen (davon Pflicht {pfl}).\n\n| Nr. | Flug | Themen im Flug | ausgelassen | Etappen | Schulart | Art | Warum an dieser Stelle |\n|---|---|---|---|---|---|---|---|")
        for f, art, heute, aenderung, aus, warum in fl:
            n += 1
            out.append(f"| {n} | **{f}** {FLUG[f][0]} | {T(themen(f, aus))} | {T(aus)} | {etappen(f, aus)} | {FLUG[f][3]} | {art} | {warum} |")
        out.append(f"\n**Prüfpunkt nach dem Abschnitt:** {pruefpunkt}.")
    return "\n".join(out), gesamt


def umfang(ab):
    z = ["| Abschnitt | Flüge | Etappen | Lerntage bei 1 / 1,5 / 2 neuen Etappen je Lerntag |", "|---|---|---|---|"]
    for titel, nf, et, _ in ab:
        z.append(f"| {titel} | {nf} | {et} | {round(et)} / {round(et / 1.5)} / {round(et / 2)} |")
    s_f, s_e = sum(a[1] for a in ab), sum(a[2] for a in ab)
    z.append(f"| **Summe** | **{s_f}** | **{s_e}** | **{round(s_e)} / {round(s_e / 1.5)} / {round(s_e / 2)}** |")
    return "\n".join(z)


def jahr(eintraege):
    je = {}
    for f, aus in eintraege:
        k = FLUG[f][1] or 0
        a, b = je.get(k, (0, 0))
        je[k] = (a + 1, b + etappen(f, aus))
    return je


def jahrtab(eintraege):
    je = jahr(eintraege)
    z = ["| Jahrgang des Flugs in der App | Flüge | Etappen |", "|---|---|---|"]
    for k in sorted(je):
        z.append(f"| {k or 'ohne Jahrgang (IB)'} | {je[k][0]} | {je[k][1]} |")
    return "\n".join(z)


t1, a1 = tabelle(KIND1)
t2, a2 = tabelle(KIND2)
e1 = [(f, aus) for _, _, fl in KIND1 for f, _, _, _, aus, _ in fl]
e2 = [(f, aus) for _, _, fl in KIND2 for f, _, _, _, aus, _ in fl]
e2s = [(f, aus) for f, aus, _ in KIND2_SPAETER]
spaeter_tab = "\n".join(f"| **{f}** {FLUG[f][0]} | {T(themen(f, aus))} | {T(aus)} | {etappen(f, aus)} | {FLUG[f][3]} | {w} |" for f, aus, w in KIND2_SPAETER)
open(os.path.join(HIER, "route.md"), "w", encoding="utf-8").write(f"""# Routen beider Kinder (Aufträge 8 und 9, zweite Fassung)

Erzeugt von `plan.py`. Schulart: G = Gymnasium Bayern, R = Realschule Bayern (Wahlpflichtfächergruppe I), I = IB-MYP-Jahr; die Zahl ist die Klasse laut App.
Etappen = alle Etappen der Themen im Flug (ohne ausgelassene), nicht die noch offenen. Zahlen zum Stand der Kinder stehen nicht im Repo.
Geprüft gegen die Tabelle `voraussetzung` der App: Keine harte und keine empfohlene Voraussetzung steht hinter dem Flug, der sie braucht.

## Kind 1 (Klasse 5)
{t1}

**Umfang**

{umfang(a1)}

{jahrtab(e1)}

## Kind 2 (Klasse 8)
{t2}

**Umfang der Abschnitte 1 bis 4**

{umfang(a2)}

{jahrtab(e2)}

### Abschnitt 5 · Vorgriff Klasse 9 – **noch nicht einstellen**

Erst nach der Abschluss-Arbeit Klasse 8. {len(KIND2_SPAETER)} Flüge, {sum(etappen(f, aus) for f, aus in e2s)} Etappen. Prüfpunkt danach: Papier-Test „Wurzeln und quadratische Gleichungen“ (noch zu bauen).

| Flug | Themen im Flug | ausgelassen | Etappen | Schulart | Warum |
|---|---|---|---|---|---|
{spaeter_tab}
""")

# ── vollständige Soll-Liste ──
ART = {P: "normal", K: "normal (gilt als Kür: steht hinter allen Pflicht-Flügen)"}


def soll_kind1():
    z = ["| Platz | Flug | Art | Themen im Flug | ausgelassen | heute | Änderung |", "|---|---|---|---|---|---|---|"]
    normal = [(f, art, heute, aend, aus) for _, _, fl in KIND1 for f, art, heute, aend, aus, _ in fl if heute != "Zusatz"]
    pflicht = [x for x in normal if x[1] == P] + [x for x in normal if x[1] == K]
    for n, (f, art, heute, aend, aus) in enumerate(pflicht, 1):
        fett = "" if aend.startswith("bleibt") and "Kür" not in aend else "**"
        z.append(f"| {n} | {f} | {ART[art]} | {T(themen(f, aus))} | {T(aus)} | {heute} | {fett}{aend}{fett} |")
    return "\n".join(z), len(pflicht)


def soll_kind2():
    z = ["| Platz | Flug | Art | Themen im Flug | ausgelassen | heute | Änderung |", "|---|---|---|---|---|---|---|"]
    normal = [(f, art, heute, aend, aus) for _, _, fl in KIND2 for f, art, heute, aend, aus, _ in fl if f != "ge9"]
    reihe = [x for x in normal if x[1] == P]
    kuer = [x for x in normal if x[1] == K]
    n = 0
    for f, art, heute, aend, aus in reihe:
        n += 1
        fett = "" if aend.startswith("bleibt") else "**"
        z.append(f"| {n} | {f} | normal | {T(themen(f, aus))} | {T(aus)} | {heute} | {fett}{aend}{fett} |")
    for f, art, aus, aend in KIND2_BESTAND:
        n += 1
        z.append(f"| {n} | {f} | {art} | {T(themen(f, aus))} | – | im Plan | {aend} |")
    for f, art, heute, aend, aus in kuer:
        n += 1
        z.append(f"| {n} | {f} | {ART[K]} | {T(themen(f, aus))} | {T(aus)} | {heute} | **{aend}** |")
    return "\n".join(z), n


s1, n1 = soll_kind1()
s2, n2 = soll_kind2()
open(os.path.join(HIER, "einstell-liste.md"), "w", encoding="utf-8").write(f"""# Vollständige Soll-Liste je Kind (Auftrag 9)

Erzeugt von `plan.py`. **Das ist die ganze normale Route nach dem Einstellen** – nicht nur die Änderungen. Was hier nicht steht, soll aus der normalen Route verschwinden (Status „entfernt“).
Flug-Kürzel = `block.schluessel`. **Fett** = Änderung gegenüber dem Plan in der App vom 26.11.2026. Einstellen erst nach Gegenprüfung, Probelauf und ausdrücklichem Satz des Nutzers.
Die Reihenfolge der Themen in einem Flug bleibt die der App.

## Kind 1 (Klasse 5) – {n1} Einträge in der normalen Route

{s1}

**Zusatz-Flüge bleiben unverändert** (Art `zusatz`, heutige Plätze): `g5`, `g6`, `f9`, `ge9`, `ge10`, `d8`, `d9`, `e1`, `e2`, `e3`. Davon sind `e1` und `g5` die Kür der Abschnitte 3 und 5.
Alle übrigen Flüge der Klassen 7 bis 10 bleiben „entfernt“.

## Kind 2 (Klasse 8) – {n2} Einträge in der normalen Route

{s2}

**Zusatz-Flüge bleiben unverändert** (Art `zusatz`): `g5`, `g6`, `f9`, `ge9`, `ge10`, `d8`, `d9`, `e1`, `e2`, `e3`.
**`ge9` verschwindet aus der normalen Route** (heute Platz 6, dort mit ausgelassenem `abbildungen.determinanten2`) und bleibt nur als Zusatz – das ist die Kür aus Abschnitt 4. Fachlich sollen im Zusatz-Eintrag `abbildungen.vektoren` drin und `abbildungen.determinanten2` ausgelassen sein; der heutige Zusatz-Eintrag lässt nichts aus. Kann die Plan-Funktion Zusatz-Einträge nicht ändern, bleibt er, wie er ist – dann kommen die Determinanten nach den Vektoren, was die Reihenfolge der App ohnehin vorgibt.
**`g2-teil2` steht jetzt als normaler Flug auf Platz 5** und nicht mehr unter „kann schon“.
**Abschnitt 5 (Klasse 9: `z7`, `ge7`, `a7`, `f4`, `ge6`, `d6`) wird jetzt nicht eingestellt** und bleibt „entfernt“. Beim späteren Einstellen: `a7` mit beiden Themen (heute ist `gleichungen.quadratisch` ausgelassen – das muss weg), `f4` mit `funktionen.quadratisch` und ausgelassenem `funktionen.transformation` (heute ist es umgekehrt).
Alle übrigen Flüge der Klassen 9 und 10 bleiben „entfernt“.

## Wie „Kür“ und „Klasse 9 später“ ohne eigenes Feld abgebildet werden

| Wunsch | Abbildung mit den vorhandenen Mitteln |
|---|---|
| Kür, für die es schon einen Zusatz-Eintrag gibt (`e1`, `g5`, `ge9`) | nicht in die normale Route aufnehmen; der Zusatz-Eintrag bleibt |
| Kür ohne Zusatz-Eintrag (Kind 1: `g4`; Kind 2: `r2-teil2`, `d4`) | als normaler Flug **hinter den letzten Pflicht-Flug** setzen. Die App bietet ihn dann erst an, wenn alles andere erledigt ist. |
| Klasse 9 erst nach Abschluss Klasse 8 | Abschnitt 5 **jetzt nicht einstellen**. Zweites Einstellen nach der Abschluss-Arbeit, wieder über die Plan-Funktion, mit der Liste aus `route.md`. |
| Regel bis zur Diagnose (Kind 2, `ge3`) | „kann – wiederholen“. Nach dem Ergebnis nach `diagnose-regel.md` umstellen. |
""")

# ── Diagnose: amtlicher Test Klasse 8 → Flüge ──
kat = json.load(open(os.path.join(WURZEL, "inhalte", "pruefmaterial", "gym", "katalog.json"), encoding="utf-8"))
status2 = {f: art for f, art, _, _ in KIND2_BESTAND}
status2.update({f: "Route" for f, _ in e2})
zeilen = []
for jahrgang in ("G8-B2025", "G8-B2024", "G8-B2023"):
    je = {}
    for a in kat["aufgaben"]:
        if a["arbeit_id"] == jahrgang:
            thema = a.get("thema_schluessel")
            flug = THEMA_FLUG.get(thema, "?")
            je.setdefault((flug, thema), []).append((a["aufgabe"], a["punkte"]))
    assert sum(p for v in je.values() for _, p in v) == 21, jahrgang
    zeilen.append(f"\n### Jahrgang {jahrgang[-4:]}\n\n| Flug | Thema | Teilaufgaben | Punkte | bei Kind 2 heute |\n|---|---|---|---|---|")
    for (flug, thema), v in sorted(je.items(), key=lambda x: (x[0][0], str(x[0][1]))):
        zeilen.append(f"| {flug} | `{thema}` | {', '.join(n for n, _ in v)} | {sum(p for _, p in v)} | {status2.get(flug, 'nicht im Plan')} |")
open(os.path.join(HIER, "diagnose-regel.md"), "w", encoding="utf-8").write(f"""# Eingangsdiagnose Kind 2: Was gilt bis zum Ergebnis, was danach (Auftrag 9)

Erzeugt von `plan.py`. Die Zuordnung der Teilaufgaben zu den Themen stammt aus `inhalte/pruefmaterial/gym/katalog.json`; die Zuordnung Thema → Flug aus der App.
Keine Aufgabe ist hier wiedergegeben, nur ihre Nummer.

## Bis zum Ergebnis gilt

1. Die Soll-Liste aus `einstell-liste.md`, so wie sie ist.
2. `ge3` (Winkel) steht auf **„kann – wiederholen“**: Er blockiert nichts, erscheint aber in den Wiederholungen.
3. `ge2` (Spiegeln) steht in Abschnitt 1 **vor** `ge4`. `ge4` steht am Anfang von Abschnitt 2 – bis dahin ist die Diagnose geschrieben und ausgewertet.
4. `g2-teil2` wird regulär geflogen (drei Etappen), unabhängig vom Ergebnis.

## Nach dem Ergebnis: Regel je Flug

Der Erwachsene bewertet nach dem amtlichen Schema und zählt je Flug die erreichten Punkte (Tabellen unten). Dann gilt – **nur für Flüge, die heute „kann schon“ oder „kann – wiederholen“ sind**:

| Erreicht im Flug | Folge |
|---|---|
| alle Punkte | bleibt, wie es ist |
| mindestens die Hälfte, aber nicht alle | „kann schon“ wird zu **„kann – wiederholen“**; „kann – wiederholen“ bleibt |
| weniger als die Hälfte, und der Flug hat im Test mindestens 2 Punkte | wird **normaler Flug**: direkt vor dem ersten Flug der Route, der ihn laut App braucht; braucht ihn keiner, an den Anfang des nächsten Abschnitts |
| weniger als die Hälfte bei nur 1 Punkt im Test | keine Umstellung; Notiz für die Tischzeit (ein Punkt ist zu wenig für eine Entscheidung) |

Flüge, die in der Route stehen, bleiben unabhängig vom Ergebnis an ihrem Platz. Ausnahme: Erreicht das Kind bei `ge4` und `ge5` zusammen alle Punkte, darf `ge5` hinter `r4` rücken (mehr Luft für Klasse-8-Stoff); sonst nicht.

**Sonderfall `ge3` (Winkel):** Winkel messen und zeichnen kommt im Test meist nur mittelbar vor. Deshalb zählt hier: Fehlen bei den Aufgaben zu `geometrie.winkelsaetze` mehr als die Hälfte der Punkte **oder** misst oder zeichnet das Kind in der Arbeit einen Winkel sichtbar falsch, dann wird `ge3` normaler Flug **direkt vor `ge4`**. Sonst bleibt `ge3` „kann – wiederholen“.

## Welche Teilaufgabe gehört zu welchem Flug
{''.join(z + chr(10) for z in zeilen)}
„?“ in der Spalte Flug: Die Teilaufgabe hat im Katalog kein Thema der App; sie zählt für keine Regel.
""")
print("Kind 1:", [(t.split(' · ')[0], nf, et) for t, nf, et, _ in a1], sum(x[1] for x in a1), sum(x[2] for x in a1), jahr(e1), "Soll-Einträge", n1)
print("Kind 2:", [(t.split(' · ')[0], nf, et) for t, nf, et, _ in a2], sum(x[1] for x in a2), sum(x[2] for x in a2), jahr(e2), "später", jahr(e2s), "Soll-Einträge", n2)
print("OK")
