"""Mathe-Profi, Auftrag 8: individueller Lehrplan beider Kinder.

Aufruf: python3 -I inhalte/mathe-profi/lehrplan-kinder/plan.py
Hält die Routen als Daten, prüft sie (jeder Flug höchstens einmal, Voraussetzungen vor dem Flug, Abschnitte mit 4–6 Flügen)
und schreibt route.md und einstell-liste.md mit gezählten Flügen und Etappen.
Nur Plan-Daten. Keine Namen, keine Quoten, keine Ergebnisse.
"""
import os
import re

HIER = os.path.dirname(os.path.abspath(__file__))

# Flug: (Titel, Jahrgang des Flugs in der App, Etappen, Themen, Schularten "G5 R5 I1" = Gymnasium/Realschule I/IB-MYP-Jahr)
F = {
    "z1": ("Natürliche und ganze Zahlen", 5, 45, "zahlen.natuerlich, zahlen.ganz, zahlen.rechengesetze, zahlen.potenzen_basis", "G5 R5 I1–2"),
    "z2": ("Teilbarkeit", 5, 7, "zahlen.teilbarkeit", "G5 R5 I1"),
    "z3": ("Brüche", 6, 14, "bruch.brueche", "G6 R6 I1"),
    "z4": ("Dezimalzahlen", 6, 8, "bruch.dezimal", "G6 R6 I1"),
    "z5": ("Rechnen mit Brüchen", 6, 12, "bruch.rechnen", "G6 R6 I2"),
    "z6": ("Potenzen", 6, 10, "zahlen.potenzen_zehner, terme.potenzgesetze", "G6 R7 I3–4"),
    "z7": ("Wurzeln und reelle Zahlen", 9, 14, "zahlen.wurzeln_basis, zahlen.reell", "G9 R9 I1/4"),
    "g1": ("Größen und Einheiten", 5, 8, "groessen.einheiten", "G5 R5 I2"),
    "g2": ("Dreisatz und direkte Proportionalität", 5, 5, "groessen.proportional", "G5 R5 I2"),
    "g2-teil2": ("Dreisatz · Teil 2", 5, 3, "groessen.proportional_teil2", "G5 R6 I2"),
    "g3": ("Prozent", 6, 6, "bruch.prozent", "G6 R6 I1"),
    "g4": ("Zinsen", 6, 8, "finanzen.zinsen", "R7 I4"),
    "g5": ("Verhältnisse und Raten", None, 6, "groessen.verhaeltnisse", "I2"),
    "g7": ("Indirekte Proportionalität", 8, 7, "groessen.indirekt", "G8 R7 I4"),
    "g8": ("Prozent mit verändertem Grundwert", 7, 8, "bruch.prozent_grundwert", "G7 R7 I3"),
    "a1": ("Einfache Gleichungen", 5, 5, "gleichungen.einfach", "G5 R6 I1"),
    "a2": ("Terme aufstellen", 7, 6, "terme.aufstellen", "G7 R6 I1"),
    "a3": ("Terme umformen", 7, 16, "terme.potenzgesetze_natuerlich, terme.umformen, gleichungen.linear", "G7 R7 I1–3"),
    "a3-teil2": ("Terme umformen · Teil 2", 7, 4, "terme.umformen_teil2", "G7 R8 I4"),
    "a4": ("Lineare Ungleichungen", 8, 11, "gleichungen.ungleichungen, zahlen.intervalle", "G8 R7 I4"),
    "a5": ("Bruchterme und Formeln", 8, 24, "terme.bruchterme, terme.potenzgesetze_ganzzahlig, gleichungen.bruch, gleichungen.formeln", "G8 R7–8 I4"),
    "a6": ("Gleichungssysteme", 8, 9, "gleichungen.lgs2", "G8 R9 I4"),
    "a10": ("Quadratische Terme und Extremwerte", 8, 5, "terme.quadratische_extreme", "R8"),
    "a7": ("Quadratische Gleichungen", 9, 14, "gleichungen.reinquadratisch, gleichungen.quadratisch", "G9 R9 I4"),
    "f1": ("Funktionsbegriff", 8, 9, "funktionen.grundbegriffe", "G8 R8 I3"),
    "f2": ("Lineare Funktionen", 8, 11, "funktionen.linear (ohne funktionen.scharen)", "G8 R8 I3"),
    "f3": ("Hyperbeln", 8, 5, "funktionen.gebrochen", "G8 I4"),
    "f4": ("Parabeln", 9, 9, "funktionen.quadratisch (ohne funktionen.transformation)", "G9 R9 I4"),
    "ge1": ("Formen und Grundbegriffe", 5, 13, "geometrie.grundbegriffe, geometrie.ortslinien", "G5 R5/7 I1"),
    "ge2": ("Spiegeln und Symmetrie", 7, 6, "abbildungen.kongruenz", "G7 R6 I3"),
    "ge2-teil2": ("Spiegeln und Symmetrie · Teil 2", 7, 3, "abbildungen.kongruenz_teil2", "G7 R7 I3"),
    "ge2-teil3": ("Spiegeln und Symmetrie · Teil 3", 7, 3, "abbildungen.kongruenz_teil3", "G7 R8 I3"),
    "ge3": ("Winkel", 5, 7, "geometrie.winkel", "G5/7 R5 I1"),
    "ge4": ("Dreiecke, Vierecke und Konstruktion", 7, 14, "geometrie.winkelsaetze, geometrie.konstruktion", "G7 R7 I2"),
    "ge4-teil2": ("Dreiecke, Vierecke und Konstruktion · Teil 2", 7, 2, "geometrie.konstruktion_teil2", "G7 R8"),
    "ge5": ("Kreis", 7, 6, "geometrie.kreis", "G7 R7 I4"),
    "ge6": ("Ähnlichkeit", 9, 9, "abbildungen.aehnlichkeit", "G9 R9 I3"),
    "ge7": ("Pythagoras", 9, 6, "trigo.pythagoras", "G9 R9 I3"),
    "ge9": ("Vektoren, Verschiebung und Drehung", 7, 6, "abbildungen.determinanten2 (ohne abbildungen.vektoren)", "R7"),
    "r1": ("Umfang und Fläche", 5, 7, "messen.flaechen", "G5 R5 I1"),
    "r2": ("Körper und Netze", 8, 13, "messen.koerper_darstellung, messen.prisma_zylinder", "G8 R5/9 I3"),
    "r2k": ("Körper und Netze (nur Körper darstellen)", 8, 6, "messen.koerper_darstellung (ohne messen.prisma_zylinder)", "G8 R5 I3"),
    "r2-teil2": ("Körper und Netze · Teil 2", 8, 1, "messen.prisma_zylinder_teil2", "R9"),
    "r3": ("Volumen und Oberfläche", 5, 5, "messen.koerper_berechnung", "G5 R6 I1"),
    "r4": ("Kreis und Zylinder", 8, 6, "messen.kreisberechnung", "G8 R9 I3"),
    "r5": ("Schrägbilder und Raumdarstellung", 10, 4, "raum.schraegbilder", "G10 R7"),
    "r7": ("Flächen und Volumen", 6, 15, "messen.flaechen_vielecke, messen.volumen", "G6 R6"),
    "d1": ("Daten darstellen", 6, 6, "daten.darstellen", "G6 R5 I1"),
    "d2": ("Zählen", 5, 7, "stochastik.kombinatorik", "G5 R5 I2"),
    "d3": ("Mittelwert", 6, 3, "daten.kennwerte", "G6 R7 I2"),
    "d4": ("Stichproben", 7, 5, "daten.stichproben", "R7 I2"),
    "d5": ("Zufall und Laplace", 8, 3, "stochastik.grundbegriffe", "G8 R8 I2"),
    "d5-teil2": ("Zufall und Laplace · Teil 2", 8, 4, "stochastik.grundbegriffe_teil2", "G8 R9 I2"),
    "d6": ("Verknüpfte Ereignisse", 9, 11, "stochastik.verknuepft", "G9 R9 I4"),
    "d10": ("Median, Quartile, Boxplot", 7, 6, "daten.boxplot", "G7 R7 I4"),
    "e1": ("Mengen und Venn-Diagramme", None, 5, "mengen.grundbegriffe", "I1"),
}

# Voraussetzungen (Flug braucht Flug) – nur die, die für die Routen zählen. „kann“ = gilt beim Kind als vorhanden.
BRAUCHT = {"z2": ["z1"], "a1": ["z1"], "z3": ["z2"], "z4": ["z3"], "z5": ["z3"], "g3": ["z5", "z4"], "r1": ["g1"], "r3": ["r1"], "g2": ["g1"], "g2-teil2": ["g2"],
           "ge3": ["ge1"], "r7": ["r1", "r3", "z4"], "a2": ["a1"], "z6": ["z1"], "d3": ["z4"], "r2k": ["ge1"], "g5": ["g2", "z3"], "ge2": ["ge3"],
           "a4": ["a3"], "a6": ["f2"], "f2": ["f1"], "f3": ["g7", "f1"], "ge5": ["ge4"], "a10": ["a3-teil2"], "r4": ["r7"], "r2": ["r7"], "r2-teil2": ["r2"],
           "d5-teil2": ["d5"], "ge2-teil2": ["ge2"], "ge2-teil3": ["ge2-teil2"], "ge4-teil2": ["ge4"], "a7": ["z7", "a3-teil2"], "f4": ["a7", "f2"], "ge7": ["z7"], "ge6": ["g2"],
           "d6": ["d5-teil2"], "g8": ["g3"]}

# Route: Abschnitt → Liste (Flug, Pflicht/Kür, heute im Plan?, Änderung, Warum hier)
P, K = "Pflicht", "Kür"
KIND1 = [
    ("1 · Rechnen festmachen, Geometrie beginnen", "Blatt B des Papier-Tests (Auftrag 5) – frühestens hier, wenn Blatt A am Anfang geschrieben wurde", [
        ("z1", P, "läuft", "bleibt", "Zu Ende bringen. Hier liegen die Regeln 1 bis 6 an Zahlen – das Fundament für alles Weitere."),
        ("ge1", P, "Platz 4", "vorgezogen", "Erster Geometrie-Flug, braucht nichts vorher. Wechsel nach viel Rechnen; Zeichnen kam bisher gar nicht vor."),
        ("z2", P, "Platz 2", "bleibt", "Braucht Mal und Geteilt aus z1. Voraussetzung für das Kürzen in den Brüchen."),
        ("a1", P, "Platz 3", "bleibt", "Regeln 7 Waage und 8 Umkehren an Zahlen. Die Brücke zu den späteren Gleichungen mit x."),
        ("d1", P, "Platz 17", "vorgezogen", "Realschule Klasse 5 (Gymnasium 6). Leicht, eigenständig, bringt Diagramme – die fehlen bisher."),
    ]),
    ("2 · Messen und Verhältnis", "eigener Papier-Test „Messen“ (noch zu bauen): Einheiten, Winkel, Fläche, Dreisatz", [
        ("g1", P, "Platz 6", "bleibt", "Einheiten umrechnen ist Voraussetzung für Fläche, Volumen und Dreisatz (Regel 13 Stellenwert)."),
        ("ge3", P, "Platz 5", "bleibt", "Baut auf ge1. Winkel messen und zeichnen – am Tisch mit Geodreieck."),
        ("r1", P, "Platz 9", "vorgezogen", "Braucht g1. Erste Formeln (Rechteck) – Formel-Koffer beginnt."),
        ("g2", P, "Platz 7", "bleibt", "Regel 14 Verhältnis an Zahlen. Braucht Einheiten."),
        ("g2-teil2", P, "Platz 8", "bleibt", "Schließt den Dreisatz ab (Realschule Klasse 6)."),
        ("d2", P, "Platz 11", "bleibt", "Eigenständig, kein Rechenweg. Auflockerung zum Abschluss des Abschnitts."),
    ]),
    ("3 · Abschluss Klasse 5 und Vorgriff", "Abschluss-Arbeit Klasse 5 auf Papier (noch zu bauen), danach Entscheidung über Klasse 6", [
        ("r3", P, "Platz 10", "bleibt", "Braucht r1. Letzter Pflicht-Flug Gymnasium Klasse 5."),
        ("r2k", P, "nicht im Plan", "neu im Plan", "Realschule Klasse 5 (Gymnasium 8): Körper, Netze, Ansichten. Nur dieser Teil; Prisma und Zylinder bleiben für später."),
        ("a2", P, "nicht im Plan", "neu im Plan", "Realschule Klasse 6, IB Jahr 1 (Gymnasium 7). Führt die Variable ein – die Brücke von der Zahl zum Buchstaben."),
        ("e1", K, "Zusatz", "bleibt Kür", "IB Jahr 1. Kurz, eigenständig, als Abwechslung."),
    ]),
    ("4 · Klasse 6: Brüche", "Papier-Test „Brüche“ (noch zu bauen)", [
        ("z3", P, "Platz 12", "bleibt", "Braucht Teilbarkeit. Regel 10 Wert bleibt."),
        ("z4", P, "Platz 13", "bleibt", "Braucht z3. Regel 13 Stellenwert."),
        ("d3", P, "Platz 18", "vorgezogen", "Braucht Dezimalzahlen. Kurz (drei Etappen), Wechsel zwischen zwei Bruch-Flügen."),
        ("z5", P, "Platz 14", "bleibt", "Braucht z3. Regel 11 Bruchrechnen – der schwerste Flug der Klasse 6."),
        ("ge2", P, "nicht im Plan", "neu im Plan", "Realschule Klasse 6 (Gymnasium 7). Geometrie zwischen den Rechen-Flügen."),
    ]),
    ("5 · Klasse 6: Anwenden", "Abschluss-Arbeit Klasse 6 auf Papier (noch zu bauen)", [
        ("g3", P, "Platz 19", "bleibt", "Braucht Brüche und Dezimalzahlen."),
        ("r7", P, "Platz 16", "bleibt", "Braucht r1, r3 und Dezimalzahlen. Dreieck, Parallelogramm, Trapez – Formel-Koffer."),
        ("z6", P, "Platz 15", "bleibt", "Regel 12 Potenz. Gymnasium 6, Realschule 7."),
        ("g5", K, "Zusatz", "bleibt Kür", "IB Jahr 2. Passt hinter Dreisatz und Brüche."),
        ("g4", K, "Platz 20", "wird Kür", "Realschule 7, IB Jahr 4; laut App kein Gymnasium-Stoff der Klasse 6. Nicht vor Prozent."),
    ]),
]
KIND2 = [
    ("1 · Klasse-8-Algebra abschließen, Geometrie öffnen", "Blatt B des Papier-Tests (Auftrag 5). Am Anfang des Abschnitts: Blatt A und ein ganzer amtlicher Test der Jahrgangsstufe 8 als Eingangsdiagnose", [
        ("a5", P, "läuft", "bleibt", "Zu Ende bringen: Bruchgleichungen und Formeln. Regeln 7, 8, 10, 14."),
        ("ge4", P, "herausgenommen", "wieder im Plan", "Klasse 7. Winkelsätze und Konstruktion: Geometrie fehlt bisher ganz, und das Begründen an Figuren ist im Jahrgangsstufentest der schwächste Teil."),
        ("a4", P, "Platz 3", "bleibt", "Gymnasium 8, Realschule 7. Braucht nur lineare Gleichungen. Regeln 1 und 2 in neuem Gewand (mal Minus dreht das Zeichen)."),
        ("g8", P, "Platz 23", "vorgezogen", "Klasse 7. Prozent mit verändertem Grundwert ist im Jahrgangsstufentest jedes Jahr dabei."),
        ("f1", P, "Platz 26", "vorgezogen", "Einstieg in das größte Gebiet der Klasse 8. Früh beginnen, damit es nicht am Ende gedrängt kommt."),
    ]),
    ("2 · Funktionen", "ganzer amtlicher Test der Jahrgangsstufe 8, zweiter Jahrgang – Vergleich mit dem ersten", [
        ("f2", P, "Platz 27", "vorgezogen", "Braucht f1. Kern der Klasse 8 in allen drei Schularten. Regel 14 Verhältnis als Steigung."),
        ("ge5", P, "herausgenommen", "wieder im Plan", "Klasse 7. Braucht ge4. Thaleskreis – typisch für Begründungsaufgaben."),
        ("a6", P, "Platz 4", "nach hinten", "Braucht f2 (Lösen am Graphen). Gymnasium 8, Realschule 9."),
        ("g7", P, "Platz 25", "bleibt", "Gymnasium 8, Realschule 7. Voraussetzung für Hyperbeln."),
        ("f3", P, "Platz 28", "bleibt", "Braucht g7 und f1. Schließt an Bruchterme an."),
        ("d5", P, "herausgenommen", "wieder im Plan", "Gymnasium 8. Kurz (drei Etappen). Daten und Zufall fehlen sonst in Klasse 8 ganz."),
    ]),
    ("3 · Raum, Kreis und Abschluss Klasse 8", "Abschluss-Arbeit Klasse 8 auf Papier (noch zu bauen)", [
        ("d5-teil2", P, "nicht im Plan", "neu im Plan", "Schließt Laplace ab (Realschule 9)."),
        ("r4", P, "herausgenommen", "wieder im Plan", "Gymnasium 8. Kreisumfang und Kreisfläche – Formel-Koffer."),
        ("r2", P, "herausgenommen", "wieder im Plan", "Gymnasium 8. Netze, Prisma, Zylinder."),
        ("a10", P, "Platz 5", "nach hinten", "Realschule 8. Braucht die binomischen Formeln; bereitet Parabeln vor."),
        ("d10", P, "herausgenommen", "wieder im Plan", "Klasse 7. Eigenständig; Diagramm lesen."),
        ("ge2", P, "Platz 20", "bleibt", "Klasse 7 Gymnasium. Spiegeln und Symmetrie – vor dem Papier-Test nur, wenn die Eingangsdiagnose dort eine Lücke zeigt, sonst hier."),
    ]),
    ("4 · Ergänzung Realschule und IB", "keiner – Kür und Ergänzung", [
        ("ge4-teil2", P, "nicht im Plan", "neu im Plan", "Schließt die Konstruktion ab (Realschule 8)."),
        ("ge2-teil2", P, "Platz 21", "nach hinten", "Realschule 7."),
        ("ge2-teil3", P, "Platz 22", "nach hinten", "Realschule 8."),
        ("ge9", K, "Platz 6", "nach hinten, wird Kür", "Nur Realschule 7 – und an dieser Zuordnung zweifle ich. Erst nach Prüfung der Lehrplan-Stelle."),
        ("r2-teil2", K, "nicht im Plan", "neu als Kür", "Realschule 9. Eine Etappe."),
        ("d4", K, "herausgenommen", "wieder im Plan als Kür", "Realschule 7, IB Jahr 2. Eigenständig."),
    ]),
    ("5 · Vorgriff Klasse 9", "Papier-Test „Wurzeln und quadratische Gleichungen“ (noch zu bauen)", [
        ("z7", P, "herausgenommen", "wieder im Plan", "Einstieg Klasse 9 in allen drei Schularten."),
        ("ge7", P, "herausgenommen", "wieder im Plan", "Braucht Wurzeln. Geometrie im Wechsel."),
        ("a7", P, "herausgenommen", "wieder im Plan", "Braucht Wurzeln und binomische Formeln. Regel 15 Nullprodukt."),
        ("f4", P, "herausgenommen", "wieder im Plan", "Braucht quadratische Gleichungen und lineare Funktionen."),
        ("ge6", P, "herausgenommen", "wieder im Plan", "Regel 14 Verhältnis in der Geometrie."),
        ("d6", P, "herausgenommen", "wieder im Plan", "Braucht Laplace."),
    ]),
]
# Kind 2: Flüge, die nicht in der Route stehen, mit Einordnung (Ergebnis, keine Zahlen)
KIND2_SONST = [
    ("a3", "erledigt – läuft in den Wiederholungen mit", "Klasse 7"), ("a3-teil2", "erledigt – läuft in den Wiederholungen mit", "Klasse 7"),
    ("a2", "kann schon – nicht nachholen", "Klasse 7"),
    ("z6", "kann – wiederholen", "Klasse 6"), ("g3", "kann – wiederholen", "Klasse 6"), ("d1", "kann – wiederholen", "Klasse 6"), ("d3", "kann – wiederholen", "Klasse 6"),
    ("r7", "kann – wiederholen", "Klasse 6"), ("g4", "kann – wiederholen", "Klasse 6"),
    ("z1", "kann schon – nicht nachholen", "Klasse 5"), ("z2", "kann schon – nicht nachholen", "Klasse 5"), ("z3", "kann schon – nicht nachholen", "Klasse 6"),
    ("z4", "kann schon – nicht nachholen", "Klasse 6"), ("z5", "kann schon – nicht nachholen", "Klasse 6"), ("g1", "kann schon – nicht nachholen", "Klasse 5"),
    ("g2", "kann schon – nicht nachholen", "Klasse 5"), ("a1", "kann schon – nicht nachholen", "Klasse 5"), ("ge1", "kann schon – nicht nachholen", "Klasse 5"),
    ("r1", "kann schon – nicht nachholen", "Klasse 5"), ("r3", "kann schon – nicht nachholen", "Klasse 5"), ("d2", "kann schon – nicht nachholen", "Klasse 5"),
    ("ge3", "heute offen im Plan – auf „kann schon“ setzen, wenn die Eingangsdiagnose bei Winkeln nichts zeigt; sonst vor ge4", "Klasse 5"),
    ("g2-teil2", "heute offen im Plan – auf „kann schon“ setzen (Dreisatz gilt als gekonnt)", "Klasse 5"),
]


def pruefe(route, kann=()):
    gesehen = list(kann)
    for titel, _, fluege in route:
        assert 4 <= len(fluege) <= 6, titel
        for f, art, heute, aenderung, warum in fluege:
            assert f in F and f not in gesehen and art in (P, K) and warum, f
            for b in BRAUCHT.get(f, []):
                basis = {"r2k": "r2"}.get(b, b)
                assert b in gesehen or basis in gesehen or (f == "r2" and b == "r7") and "r7" in kann, (f, "braucht", b)
            gesehen.append(f)
            if f == "r2k":
                gesehen.append("r2")
    return gesehen


g1 = pruefe(KIND1)
kann2 = [f for f, _, _ in KIND2_SONST]
g2 = pruefe(KIND2, kann=kann2)
assert len(set(kann2)) == len(kann2)


def tabelle(route):
    out, gesamt = [], []
    n = 0
    for titel, pruefpunkt, fluege in route:
        et = sum(F[f][2] for f, *_ in fluege)
        pfl = sum(F[f][2] for f, a, *_ in fluege if a == P)
        gesamt.append((titel, len(fluege), et, pfl))
        out.append(f"\n### Abschnitt {titel}\n\n{len(fluege)} Flüge, {et} Etappen (davon Pflicht {pfl}).\n\n| Nr. | Flug | Themen | Etappen | Schulart | Art | Warum an dieser Stelle |\n|---|---|---|---|---|---|---|")
        for f, art, heute, aenderung, warum in fluege:
            n += 1
            t = F[f]
            code = {"r2k": "r2"}.get(f, f)
            themen = re.sub(r"([a-z]+\.[a-z0-9_]+)", r"`\1`", t[3])
            out.append(f"| {n} | **{code}** {t[0]} | {themen} | {t[2]} | {t[4]} | {art} | {warum} |")
        out.append(f"\n**Prüfpunkt nach dem Abschnitt:** {pruefpunkt}.")
    return "\n".join(out), gesamt


def jahr(route, nur_pflicht=False):
    je = {}
    for _, _, fluege in route:
        for f, art, *_ in fluege:
            if nur_pflicht and art != P:
                continue
            k = F[f][1] or "ohne Jahrgang (IB)"
            a, b = je.get(k, (0, 0))
            je[k] = (a + 1, b + F[f][2])
    return je


t1, a1 = tabelle(KIND1)
t2, a2 = tabelle(KIND2)
ETAPPEN_JE_TAG = (1, 1.5, 2)


def umfang(abschnitte):
    z = ["| Abschnitt | Flüge | Etappen | Lerntage bei 1 / 1,5 / 2 neuen Etappen je Lerntag |", "|---|---|---|---|"]
    for titel, nf, et, _ in abschnitte:
        z.append(f"| {titel} | {nf} | {et} | {round(et / 1)} / {round(et / 1.5)} / {round(et / 2)} |")
    s_f, s_e = sum(a[1] for a in abschnitte), sum(a[2] for a in abschnitte)
    z.append(f"| **Summe** | **{s_f}** | **{s_e}** | **{round(s_e)} / {round(s_e / 1.5)} / {round(s_e / 2)}** |")
    return "\n".join(z)


def jahrtab(route):
    je = jahr(route)
    z = ["| Jahrgang des Flugs in der App | Flüge in der Route | Etappen |", "|---|---|---|"]
    for k in sorted(je, key=lambda x: (isinstance(x, str), x)):
        z.append(f"| {k} | {je[k][0]} | {je[k][1]} |")
    return "\n".join(z)


route_md = f"""# Routen beider Kinder (Auftrag 8)

Erzeugt von `plan.py`. Schulart-Spalte: G = Gymnasium Bayern, R = Realschule Bayern (Wahlpflichtfächergruppe I), I = IB-MYP-Jahr; die Zahl ist die Klasse laut App.
Etappen = alle Etappen des Flugs, nicht die noch offenen. Zahlen zum Stand der Kinder stehen nicht im Repo.

## Kind 1 (Klasse 5)
{t1}

**Umfang**

{umfang(a1)}

{jahrtab(KIND1)}

## Kind 2 (Klasse 8)
{t2}

**Umfang**

{umfang(a2)}

{jahrtab(KIND2)}

**Nicht in der Route von Kind 2**

| Flug | Jahrgang | Einordnung |
|---|---|---|
""" + "\n".join(f"| **{f}** {F[f][0]} | {kl} | {e} |" for f, e, kl in KIND2_SONST) + "\n"
open(os.path.join(HIER, "route.md"), "w", encoding="utf-8").write(route_md)


def einstell(route, sonst=()):
    z = ["| Platz neu | Flug | Art | heute | Änderung | Hinweis zum Einstellen |", "|---|---|---|---|---|---|"]
    n = 0
    for titel, _, fluege in route:
        z.append(f"| | *Abschnitt {titel}* | | | | |")
        for f, art, heute, aenderung, _ in fluege:
            n += 1
            code = {"r2k": "r2"}.get(f, f)
            hinweis = {"r2k": "`messen.prisma_zylinder` auslassen", "f2": "`funktionen.scharen` bleibt ausgelassen", "f4": "`funktionen.transformation` bleibt ausgelassen",
                       "ge9": "`abbildungen.vektoren` bleibt ausgelassen", "a7": "`gleichungen.reinquadratisch` bleibt ausgelassen, falls so eingestellt"}.get(f, "")
            fett = "**" if aenderung not in ("bleibt", "bleibt Kür") else ""
            z.append(f"| {n} | {code} | {art} | {heute} | {fett}{aenderung}{fett} | {hinweis} |")
    for f, e, _ in sonst:
        z.append(f"| – | {f} | – | – | {e} | |")
    return "\n".join(z)


einstell_md = f"""# Einstell-Liste für den Projektleiter (Auftrag 8)

Erzeugt von `plan.py`. **Fett** = Änderung gegenüber dem heutigen Plan in der App (gelesen am 26.11.2026). Einstellen erst nach Gegenprüfung und ausdrücklichem Satz des Nutzers.
Flug-Kürzel wie in der App (`block.schluessel`).

## Kind 1 (Klasse 5)

{einstell(KIND1)}

Alles, was heute bei Kind 1 „entfernt“ ist (Klasse 7 bis 10) und hier nicht steht, bleibt entfernt. Zusatz-Flüge, die hier nicht stehen (g6, f9, ge9, ge10, d8, d9, e2, e3), bleiben Zusatz.

## Kind 2 (Klasse 8)

{einstell(KIND2, KIND2_SONST)}

Alles, was heute bei Kind 2 „entfernt“ ist und hier nicht steht (übrige Flüge der Klassen 9 und 10), bleibt entfernt. Zusatz-Flüge, die hier nicht stehen (g5, g6, f9, ge10, d8, d9, e1, e2, e3), bleiben Zusatz.

## Zusammenfassung der Änderungen

- **Kind 1:** {sum(1 for _, _, fl in KIND1 for x in fl if x[3] not in ('bleibt', 'bleibt Kür'))} von {sum(len(fl) for _, _, fl in KIND1)} Flügen ändern Platz oder Status; neu im Plan: r2 (nur Körper darstellen), a2, ge2.
- **Kind 2:** {sum(1 for _, _, fl in KIND2 for x in fl if x[3] not in ('bleibt', 'bleibt Kür'))} von {sum(len(fl) for _, _, fl in KIND2)} Flügen ändern Platz oder Status; wieder im Plan aus „entfernt“: ge4, ge5, d5, r4, r2, d10, d4 und sechs Flüge der Klasse 9; neu: d5-teil2, ge4-teil2, r2-teil2.
"""
open(os.path.join(HIER, "einstell-liste.md"), "w", encoding="utf-8").write(einstell_md)
for name, ab, r in (("Kind 1", a1, KIND1), ("Kind 2", a2, KIND2)):
    print(name, "Abschnitte:", [(t.split(" · ")[0], nf, et) for t, nf, et, _ in ab], "Summe", sum(x[1] for x in ab), sum(x[2] for x in ab), "| je Jahrgang", jahr(r))
print("OK")
