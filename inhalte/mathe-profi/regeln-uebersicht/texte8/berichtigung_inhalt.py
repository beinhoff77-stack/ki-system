#!/usr/bin/env python3
"""Berichtigt einzelne Texte in inhalt.json (Entwurf, nur Texte; Gegenprüfung 1078). Jede Ersetzung prüft den alten Text und ist wiederholbar.
Aufruf: python3 -I inhalte/mathe-profi/regeln-uebersicht/texte8/berichtigung_inhalt.py"""
import json, pathlib
repo = pathlib.Path(__file__).resolve().parents[4]
P = repo / 'inhalte/design/gesetzbuch/entwurf/teile/inhalt.json'
d = json.loads(P.read_text(encoding='utf-8'))
regel = {r['id']: r for r in d['regeln']}; gesetz = {g['id']: g for g in d['gesetze']}
AENDERUNGEN = [
 (regel, 'R11', 'voraus', 'Gilt nur bei direkter Proportionalität: doppelte Menge, doppelter Wert; zur Menge null gehört der Wert null.',
  'Gilt, wenn zwei Größen im selben Verhältnis wachsen (direkte Proportionalität): doppelte Menge, doppelter Wert; zur Menge null gehört der Wert null.'),
 (regel, 'R11', 'fehler', 'Den Dreisatz anwenden, obwohl ein fester Betrag dazukommt (Grundgebühr) oder obwohl mehr von dem einen weniger von dem anderen bedeutet.',
  'Den Dreisatz anwenden, obwohl ein fester Betrag dazukommt (Grundgebühr). Oder wie bei direkter Proportionalität rechnen, obwohl mehr von dem einen weniger von dem anderen bedeutet: Dann rechnet man umgekehrt.'),
 (gesetz, 'V7', 'satz', 'Änderung je Einheit: Unterschied der Werte durch Unterschied der Schritte.',
  'Änderung je Einheit: Unterschied der Werte durch Unterschied der Schritte. In Klasse 5 heißt das: Wert je Einheit bei direkter Proportionalität, zum Beispiel Preis je Kilogramm.'),
 (gesetz, 'D9', 'satz', 'Die Standardabweichung ist die Wurzel aus dem Mittelwert der quadrierten Abweichungen vom Mittelwert – ein Maß für die typische Abweichung.',
  'Die Standardabweichung ist die Wurzel aus dem Mittelwert der quadrierten Abweichungen vom Mittelwert (Formel für die Grundgesamtheit, Nenner n) – ein Maß für die typische Abweichung. Bei einer Stichprobe teilt man durch n − 1.'),
 (gesetz, 'Z20', 'satz', 'Die Wurzel aus a ist die Zahl ab null, deren Quadrat a ist. Aus negativen Zahlen gibt es keine.',
  'Die Wurzel aus a ist die Zahl ab null, deren Quadrat a ist. Aus negativen Zahlen gibt es über den reellen Zahlen keine.'),
 (gesetz, 'Z23', 'satz', 'a hoch 1/n ist die n-te Wurzel aus a.', 'Für a ≥ 0 ist a hoch (1/n) die n-te Wurzel aus a.'),
 (gesetz, 'E3', 'satz', 'Jede Kante zählt an zwei Knoten. Ein Rundweg über alle Kanten geht nur, wenn jeder Knoten gerade viele Kanten hat.',
  'Jede Kante zählt an zwei Knoten. In einem zusammenhängenden Graphen gibt es einen Rundweg über alle Kanten genau dann, wenn jeder Knoten gerade viele Kanten hat.'),
 (gesetz, 'G6', 'voraus', 'Gilt für jedes Dreieck in der Ebene; die Vielecksformel für die Innenwinkel.',
  'Gilt für jedes Dreieck in der Ebene. Die Vielecksformel gilt für die Innenwinkel jedes n-Ecks, dessen Seiten sich nicht überschneiden.'),
]
idee = {('%s' % p['name'], i['nr']): i for p in d['planeten'] for i in p['ideen']}
AENDERUNGEN += [
 (idee, ('Algebra', 2), 'genau', 'Kläre zuerst, welche Zahlen du einsetzen darfst: Kein Nenner wird null, unter keiner Wurzel steht etwas Negatives.',
  'Kläre zuerst, welche Zahlen du einsetzen darfst: Kein Nenner wird null, unter keiner Quadratwurzel steht etwas Negatives (über den reellen Zahlen).'),
 (idee, ('Algebra', 2), 'warum', 'Nicht jede Zahl darf in jeden Term: Durch null kann man nicht teilen, und aus einer negativen Zahl gibt es keine Quadratwurzel. Wer das vor dem Rechnen klärt, erkennt Scheinlösungen.',
  'Nicht jede Zahl darf in jeden Term: Durch null kann man nicht teilen, und aus einer negativen Zahl gibt es über den reellen Zahlen keine Quadratwurzel (eine dritte Wurzel aus −8 gibt es dagegen: −2). Wer das vor dem Rechnen klärt, erkennt Scheinlösungen.'),
]

AENDERUNGEN += [
 (idee, ('Geld und Verhältnisse', 2), 'satz', 'Doppelt so viel kostet doppelt so viel.', 'Bei gleichem Preis je Einheit kostet doppelt so viel doppelt so viel.'),
 (idee, ('Fläche und Raum', 2), 'satz', 'Aus dem Rechteck entsteht jede Fläche.', 'Aus dem Rechteck entstehen die Flächen vieler Figuren.'),
 (idee, ('Fläche und Raum', 2), 'genau', 'Aus dem Rechteck entsteht jede Fläche: zerschneiden, neu legen, halbieren.',
  'Aus dem Rechteck entstehen die Formeln für Parallelogramm, Dreieck und Trapez: zerschneiden, neu legen, halbieren. Beim Kreis nähert man sich dem Rechteck nur an.'),
 (idee, ('Fläche und Raum', 2), 'warum', 'Vom Rechteck weiß man die Fläche durch Zählen. Jede andere Figur wird so zerschnitten und neu gelegt, dass ein Rechteck entsteht – oder sie ist die Hälfte einer Figur, deren Fläche man schon kennt. Deshalb muss man die Formeln nicht einzeln lernen: Man kann sie herleiten.',
  'Vom Rechteck weiß man die Fläche durch Zählen. Viele andere Figuren werden so zerschnitten und neu gelegt, dass ein Rechteck entsteht – oder sie sind die Hälfte einer Figur, deren Fläche man schon kennt. Deshalb muss man diese Formeln nicht einzeln lernen: Man kann sie herleiten. Beim Kreis geht das nur als Annäherung.'),
 (idee, ('Fläche und Raum', 3), 'genau', 'Aus dem Quader entsteht jeder Körper: Grundfläche mal Höhe – bei spitzen Körpern ein Drittel davon.',
  'Bei Prisma und Zylinder gilt Grundfläche mal Höhe, bei spitz zulaufenden Körpern (Pyramide, Kegel) ein Drittel davon.'),
 (idee, ('Fläche und Raum', 3), 'warum', 'Ein Quader ist ein Stapel gleicher Schichten: Grundfläche mal Höhe. Das bleibt richtig, wenn die Grundfläche ein Dreieck oder ein Kreis ist (Prisma, Zylinder) und sogar, wenn der Stapel schief steht. Läuft der Körper spitz zu, bleibt genau ein Drittel übrig.',
  'Ein Quader ist ein Stapel gleicher Schichten: Grundfläche mal Höhe. Das bleibt richtig, wenn die Grundfläche ein Dreieck oder ein Kreis ist (Prisma, Zylinder) und sogar, wenn der Stapel schief steht. Läuft ein Körper spitz zu (Pyramide, Kegel), bleibt genau ein Drittel übrig.'),
 (idee, ('Fläche und Raum', 1), 'warum', 'Eine Fläche misst man, indem man sie lückenlos mit gleich großen Quadraten auslegt und zählt; einen Körper füllt man mit gleich großen Würfeln. Jede Formel dieses Planeten ist eine Abkürzung für dieses Zählen: 4 Reihen zu je 6 Quadraten sind 6 · 4.',
  'Eine Fläche misst man, indem man sie lückenlos mit gleich großen Quadraten auslegt und zählt; einen Körper füllt man mit gleich großen Würfeln. Die Formeln für Fläche und Rauminhalt sind Abkürzungen für dieses Zählen: 4 Reihen zu je 6 Quadraten sind 6 · 4.'),
 (idee, ('Funktionen', 2), 'satz', 'Plus gleich viel gibt eine Gerade, mal gleich viel eine steile Kurve.', 'Immer plus dasselbe gibt eine Gerade, immer mal denselben Faktor eine Kurve.'),
 (idee, ('Funktionen', 2), 'warum', 'Es gibt zwei Grundarten zu wachsen. Kommt in jedem Schritt gleich viel dazu, liegen die Punkte auf einer Geraden. Wird in jedem Schritt mit derselben Zahl malgenommen, wird die Kurve immer steiler und überholt jede Gerade.',
  'Es gibt zwei Grundarten zu wachsen. Kommt in jedem Schritt gleich viel dazu, liegen die Punkte auf einer Geraden. Wird in jedem Schritt mit derselben Zahl malgenommen und ist diese Zahl größer als 1, wird die Kurve immer steiler und überholt jede Gerade; ist sie kleiner als 1, fällt die Kurve.'),
 (idee, ('Funktionen', 3), 'genau', 'Die Gleichung verrät die Form des Graphen – und jede Änderung der Gleichung verschiebt oder streckt ihn.',
  'Bei bekannten Funktionstypen verrät die Gleichung die Form des Graphen – und bestimmte Änderungen der Gleichung verschieben, strecken oder spiegeln ihn.'),
 (idee, ('Funktionen', 3), 'warum', 'An der Gleichung erkennt man, wie der Graph aussieht, bevor man einen einzigen Punkt berechnet: x allein gibt eine Gerade, x² eine Parabel, x im Nenner eine Hyperbel. Ändert man die Gleichung an einer Stelle, bewegt sich der Graph auf eine vorhersagbare Weise.',
  'Bei bekannten Funktionstypen erkennt man an der Gleichung, wie der Graph aussieht, bevor man einen einzigen Punkt berechnet: x allein gibt eine Gerade, x² eine Parabel, x im Nenner eine Hyperbel. Ändert man die Gleichung an einer Stelle, bewegt sich der Graph auf eine vorhersagbare Weise.'),
 (idee, ('Geometrie', 5), 'satz', 'Rechter Winkel im Dreieck: a² plus b² ist c².', 'Rechter Winkel im Dreieck: a² plus b² ist c² – c liegt dem rechten Winkel gegenüber.'),
 (idee, ('Geometrie', 2), 'warum', 'Viele Linien der Geometrie sind „alle Punkte mit einer Abstandseigenschaft“: gleich weit von einem Punkt (Kreis), von zwei Punkten (Mittelsenkrechte), von zwei Geraden (Winkelhalbierende). Darum findet man den Umkreismittelpunkt mit Mittelsenkrechten und den Inkreismittelpunkt mit Winkelhalbierenden.',
  'Viele Linien der Geometrie bestehen aus allen Punkten, die von etwas gleich weit entfernt sind: von einem Punkt (Kreis), von zwei Punkten (Mittelsenkrechte), von zwei Geraden (Winkelhalbierende). Darum findet man den Umkreismittelpunkt mit Mittelsenkrechten und den Inkreismittelpunkt mit Winkelhalbierenden.'),
 (regel, 'R9', 'fehler', 'Aus Summen kürzen: (x + 6) : (x + 2) zu 3 machen. Erst ausklammern, dann kürzen.',
  'Aus Summen kürzen: (x + 6)/(x + 2) zu 3 machen – hier lässt sich nichts kürzen. Bei (3x + 6)/(x + 2) hilft erst ausklammern: 3 · (x + 2)/(x + 2) = 3.'),
]
n = 0
for tab, k, feld, alt, neu in AENDERUNGEN:
    t = tab[k]
    assert t[feld] in (alt, neu), (k, feld, t[feld])
    if t[feld] == alt: t[feld] = neu; n += 1
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8')
print('inhalt.json: %d Texte berichtigt (%d insgesamt vorgesehen)' % (n, len(AENDERUNGEN)))
