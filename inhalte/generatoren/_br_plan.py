"""Einundzwanzigste Runde, Teil A: Schritte je Thema (Motor: _bereinigen.py). Begründungen im Postfach bereinigen.md."""
from _bereinigen import entfaellt, weg, her, karte_her, vertiefung, neu, knobel, ersetze, karte, inhalt, abschnitt  # noqa: F401
from _befunde import _z as Z, _l as L  # noqa: F401
from _stufen_kl5 import A  # noqa: F401

PLAN = {}

# ======================= Klasse 5 =======================
# A1: Umkehraufgaben stehen zuerst in zahlen.ganz (Plus/Minus) und zahlen.rechengesetze (Mal/Geteilt).
PLAN['zahlen.ganz'] = [
    her('gleichungen.einfach', 'umkehr_plus', 'umkehraufgabe',
        r'^(Löse 63 = x − 28\.|Welche Rechnung führt zur Lösung von (47 − x = 18|x − 177 = 362)\?|Welche Zahl muss man von 1 000 subtrahieren|'
        r'Fülle die Lücke: 2 345|Löse x \+ 44 = 52 \+ 64\.|Ich denke mir eine Zahl\. Ziehe ich 99)', 7),
]
PLAN['zahlen.rechengesetze'] = [
    her('gleichungen.einfach', 'umkehr_mal', 'umkehraufgabe_mal',
        r'^(Löse x : 4 = 10\.|Löse 72 : x = 9\.|Welche Rechnung führt zur Lösung von x : 6 = 27\?|Ich denke mir eine Zahl, teile sie durch 7|'
        r'Stimmt die Aussage\? „Bei x : 8 = 5|Eine Zahl wird verdoppelt, das Ergebnis verdreifacht)', 6),
]
PLAN['gleichungen.einfach'] = [
    entfaellt('umkehr_plus'),
    entfaellt('umkehr_mal'),
    karte('zwei_schritte', woerter=[['Rechenkette', 'mehrere Rechenschritte hintereinander'],
                                    ['umkehren', 'rückgängig machen: aus plus wird minus, aus mal wird geteilt (Umkehraufgaben, Flüge zu den ganzen Zahlen und zu den Rechengesetzen)']]),
]

# A1: Volumen ist Stoff der Klasse 6 (messen.volumen). Vertiefung „volumen“ in messen.koerper_berechnung entfällt;
# die Volumen-Aussagen der Pflichtkarte „verstehen“ ziehen aus und werden durch Aussagen zu Oberfläche und Kanten ersetzt.
PLAN['messen.volumen'] = [
    her('messen.koerper_berechnung', 'volumen', 'quader', r'^Ein Schuhkarton ist 30 cm lang', 1),
    her('messen.koerper_berechnung', 'volumen', 'einheitswuerfel', r'^Eine Schachtel ist innen 6 cm lang', 1),
    her('messen.koerper_berechnung', 'verstehen', 'verstehen',
        r'^(Jemand gibt das Volumen eines Würfels mit 3 cm|Stimmt die Aussage\? „Ein Würfel mit dem Volumen 27 cm³)', 2),
]
_VOL = (r'^(Stimmt die Aussage\? „(Verdoppelt man die Kantenlänge eines Würfels, wird das Volumen|Zwei Quader mit gleichem Volumen|'
        r'Ein Quader mit 2 cm, 3 cm und 4 cm hat das Volumen|Ein Würfel mit dem Volumen 27|Ein Quader mit größerem Volumen)|'
        r'Bei welchem Würfel haben Oberfläche|Jemand gibt das Volumen eines Würfels|Ein Quader hat ganzzahlige Kantenlängen\. Alle Kanten zusammen sind 24)')
PLAN['messen.koerper_berechnung'] = [
    entfaellt('volumen'),
    abschnitt('Volumen und Verstehen', 'Verstehen'),
    inhalt(ziel='Quader und Würfel beschreiben und ihren Oberflächeninhalt berechnen – auch bei zusammengesetzten Körpern und im Alltag. Das Volumen kommt in Klasse 6.',
           merke=['Quader: 6 Flächen, 12 Kanten, 8 Ecken. Kantenlänge gesamt: 4 · (a + b + c).', 'Oberfläche Quader: O = 2ab + 2ac + 2bc. Würfel: O = 6a².',
                  'Zusammengesetzt: Berührflächen fallen weg (je zweimal).']),
    weg('verstehen', _VOL, 8),
    neu('verstehen', 'umkehr', A('Ein Würfel hat die Oberfläche 54 cm². Stimmt die Aussage? „Seine Kanten sind 3 cm lang.“',
        'Ja: 54 cm² : 6 = 9 cm² je Fläche, und 3 cm · 3 cm = 9 cm².',
        ['Nein: 54 : 6 = 9, also sind die Kanten 9 cm lang.', 'Nein: 54 : 4 = 13,5, also sind die Kanten 13,5 cm lang.'],
        'Ein Würfel hat 6 gleiche Quadrate: 54 cm² : 6 = 9 cm². Ein Quadrat mit 9 cm² hat 3 cm lange Seiten (3 · 3 = 9). Die Aussage stimmt.',
        'Wie viele gleiche Flächen hat ein Würfel? Wie groß ist dann eine davon?')),
    neu('verstehen', 'einkleidung', A('Stimmt die Aussage? „Für das Kantenmodell eines Würfels mit 6 cm Kantenlänge reicht ein 70 cm langer Draht.“',
        'Nein: 12 · 6 cm = 72 cm, es fehlen 2 cm.', ['Ja: 8 · 6 cm = 48 cm reichen.', 'Ja: 6 · 6 cm = 36 cm reichen.'],
        'Ein Würfel hat 12 Kanten, jede 6 cm lang: 12 · 6 cm = 72 cm. 70 cm reichen also nicht.',
        'Zähle die Kanten eines Würfels – nicht die Ecken und nicht die Flächen.')),
    neu('verstehen', 'begruenden', A('Stimmt die Aussage? „Schneidet man einen Würfel parallel zu einer Fläche genau in der Mitte durch, hat jede Hälfte die halbe Oberfläche.“',
        'Nein: Jede Hälfte bekommt eine neue Schnittfläche dazu.', ['Ja: Halber Würfel, halbe Oberfläche.', 'Ja, aber nur bei Würfeln mit gerader Kantenlänge.'],
        'Beispiel mit 2 cm Kante: Der Würfel hat 6 · 4 cm² = 24 cm². Eine Hälfte ist ein Quader 2 cm × 2 cm × 1 cm mit 2 · (4 + 2 + 2) cm² = 16 cm², nicht 12 cm². Die Schnittfläche kommt dazu.',
        'Rechne ein Beispiel: Würfel mit 2 cm Kante. Welcher Quader ist eine Hälfte?')),
    neu('verstehen', 'begruenden', A('Stimmt die Aussage? „Bei jedem Quader sind alle Kanten zusammen viermal so lang wie Länge + Breite + Höhe.“',
        'Ja: Jede der drei Längen kommt als Kante genau viermal vor.', ['Nein: Es ist nur doppelt so lang.', 'Nein: Das gilt nur für Würfel.'],
        'Ein Quader hat 12 Kanten: 4 Kanten sind so lang wie die Länge, 4 wie die Breite und 4 wie die Höhe. Zusammen 4 · (Länge + Breite + Höhe).',
        'Wie viele Kanten hat ein Quader, und wie viele davon sind gleich lang?')),
    neu('verstehen', 'rueckwaerts', Z('Ein Quader ist 4 cm lang und 3 cm breit. Seine Oberfläche ist 94 cm². Wie hoch ist er in cm?', 5, '(94 - 2*4*3) // (2*(4 + 3))',
        'Boden und Deckel: 2 · 4 · 3 = 24 cm². Für die vier Seitenflächen bleiben 94 − 24 = 70 cm². Sie haben zusammen die Breite 2 · (4 + 3) = 14 cm, also Höhe 70 : 14 = 5 cm.',
        'Rechne zuerst Boden und Deckel aus. Wie viel Fläche bleibt für die Seiten?', einheit='cm')),
    neu('verstehen', 'parameter', Z('Ein Quader ist a cm lang, 2 cm breit und 1 cm hoch. Für welche Zahl a ist seine Oberfläche 28 cm²?', 4, '(28 // 2 - 2) // 3',
        'Oberfläche = 2 · (2a + a + 2) = 6a + 4. Aus 6a + 4 = 28 folgt 6a = 24, also a = 4. Probe: 2 · (8 + 4 + 2) = 28.',
        'Schreibe die drei Flächen auf: a · 2, a · 1 und 2 · 1. Jede kommt zweimal vor.')),
    neu('verstehen', 'verknuepfen', Z('Ein Würfel hat 3 cm lange Kanten. Wie viele mm² beträgt seine Oberfläche?', 5400, '6*3*3*100',
        'Oberfläche: 6 · 3 cm · 3 cm = 54 cm². 1 cm² = 100 mm², also 54 cm² = 5 400 mm².',
        'Rechne die Oberfläche erst in cm² aus. Wie viele mm² hat 1 cm²?', einheit='mm²')),
    knobel('verstehen', Z('Zwei gleiche Quader mit 1 cm, 2 cm und 3 cm Kantenlänge werden so zusammengestellt, dass eine Fläche des einen genau auf einer gleich großen Fläche des anderen liegt. '
        'Wie groß ist die kleinste mögliche Oberfläche des neuen Körpers in cm²?', 32, '2*2*(1*2 + 1*3 + 2*3) - 2*2*3',
        'Ein Quader hat 2 · (2 + 3 + 6) cm² = 22 cm², zwei also 44 cm². Beim Zusammenstellen verschwinden zwei aufeinanderliegende Flächen. Am meisten spart man mit der größten Fläche 2 cm · 3 cm = 6 cm²: 44 − 2 · 6 = 32 cm².',
        'Was passiert mit den beiden Flächen, die aufeinanderliegen? Welche Fläche ist die größte?', einheit='cm²')),
]
