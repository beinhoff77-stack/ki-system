"""Einundzwanzigste Runde, Teil A: Schritte je Thema (Motor: _bereinigen.py). Begründungen im Postfach bereinigen.md."""
from _bereinigen import entfaellt, weg, her, karte_her, vertiefung, neu, knobel, ersetze, karte, inhalt, abschnitt, umschreiben, innen, karte_neu, teilfaehigkeit, pool  # noqa: F401
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


def T(a):
    """Aufgabe für Test/Korrektur/Sicherung: ohne Tipp."""
    a = dict(a); a.pop('h', None); return a


def _drei(n):
    """Test-/Korrektur-/Sicherungsaufgabe „Ist n durch 3 teilbar?“ (Lösung aus der Quersumme berechnet)."""
    z = f'{n:,}'.replace(',', ' ')
    qs = sum(int(c) for c in str(n))
    ja = qs % 3 == 0
    r = f'Ja: Die Quersumme {qs} ist durch 3 teilbar.' if ja else f'Nein: Die Quersumme {qs} ist nicht durch 3 teilbar.'
    f = [f'Nein: Die Quersumme {qs} ist nicht durch 3 teilbar.' if ja else f'Ja: Die Quersumme {qs} ist durch 3 teilbar.',
         f'Das hängt nur von der letzten Ziffer {n % 10} ab.']
    assert (n % 3 == 0) == ja
    return T(A(f'Ist {z} durch 3 teilbar?', r, f, f'Quersumme: {" + ".join(str(n))} = {qs}. ' + (f'{qs} ist durch 3 teilbar, also auch {z}.' if ja else f'{qs} ist nicht durch 3 teilbar, also auch {z} nicht.'), '-'))


# A2: Neunerregel (nicht in M5: nur 2, 3, 5, 10) – kein Thema einer höheren Klasse hat sie → eigene Vertiefungskarte „neunerregel“;
# ggT und kgV → bruch.brueche (M6 1.1: Hauptnenner, auch über die Primfaktorzerlegung; vollständig kürzen).
_NEUNER_KARTE = {
    'titel': 'Teilbar durch 9',
    'einstieg': 'Ein Bäcker hat 2 754 Brötchen und packt immer 9 in eine Tüte. Bleibt etwas übrig? Wieder hilft die ⟦Quersumme⟧, diesmal mit der 9.',
    'woerter': [['Neunerregel', 'Ist die Quersumme durch 9 teilbar, dann auch die Zahl.']],
    'bild': {'typ': 'tabelle', 'kopf': ['Ziffern', 'Quersumme', 'durch 9?'], 'zeilen': [['2 + 7 + 5 + 4', '?', '?']]},
    'schritte': [{'text': 'Quersumme von 2 754: 2 + 7 + 5 + 4 = ⟦18⟧.', 'bild': {'zeilen': [['2 + 7 + 5 + 4', '18', '?']]}},
                 {'text': '18 ist durch 9 teilbar. Nach der Neunerregel ist auch 2 754 durch 9 teilbar.', 'bild': {'zeilen': [['2 + 7 + 5 + 4', '18', '✓']]}},
                 {'text': '2 754 : 9 = ⟦306⟧. Es gibt 306 Tüten, nichts bleibt übrig.'}],
    'fehler': 'Durch 3 teilbar heißt nicht durch 9 teilbar: 12 hat die Quersumme 3. Das ist durch 3 teilbar, aber 12 : 9 geht nicht auf.',
    'fehler_bild': {'zeilen': [['1 + 2', '3', '✗']]},
    'regel': 'Ist die ⟦Quersumme⟧ durch 9 teilbar, dann auch die Zahl. Jede Zahl, die durch 9 teilbar ist, ist auch durch 3 teilbar.',
}
PLAN['zahlen.teilbarkeit'] = [
    karte('quersumme', titel='Teilbar durch 3', regel='Ist die ⟦Quersumme⟧ durch 3 teilbar, dann auch die Zahl.',
          schritte=[{'text': 'Quersumme: 4 + 2 + 5 + 1 = ⟦12⟧.', 'bild': {'typ': 'tabelle', 'kopf': ['Ziffern', 'Quersumme', 'durch 3?'], 'zeilen': [['4 + 2 + 5 + 1', '12', '?']]}},
                    {'text': '12 ist durch 3 teilbar. Also auch 4 251: Jede Klasse bekommt ⟦1 417⟧.', 'bild': {'typ': 'tabelle', 'kopf': ['Ziffern', 'Quersumme', 'durch 3?'], 'zeilen': [['4 + 2 + 5 + 1', '12', '✓']]}}],
          fehler='13 hat die Quersumme 4, ist aber nicht durch 4 teilbar. Die Regel gilt nur für 3 (und, als Vertiefung, für 9).'),
    teilfaehigkeit('quersumme', 'Teilbar durch 3'),
    karte_neu('neunerregel', 'Teilbarkeitsregeln', _NEUNER_KARTE, 'Teilbar durch 9 (Vertiefung)', nach='quersumme', vertiefung=True),
    innen('quersumme', 'neunerregel', r'^(Ist [\d ]+ durch 3 oder durch 9 teilbar\?|Eine Zahl hat eine Quersumme, die durch 9|Kann man 1 233 Bonbons|'
          r'Welche Ziffer muss für □ stehen, damit \d+□ durch 9|Stimmt die Aussage\? „Jede Zahl, die durch 9|Gib die kleinste vierstellige Zahl mit lauter|Aus den Ziffern 1 bis 9)', 22),
    # quersumme (nur noch 3) auffüllen
    neu('quersumme', 'direkt', A('Ist 5 412 durch 3 teilbar?', 'Ja: Quersumme 5 + 4 + 1 + 2 = 12, und 12 ist durch 3 teilbar.',
        ['Nein: Die letzte Ziffer 2 ist nicht durch 3 teilbar.', 'Nein: 5 412 ist gerade.'],
        'Quersumme: 5 + 4 + 1 + 2 = 12. 12 ist durch 3 teilbar, also auch 5 412 (5 412 : 3 = 1 804).', 'Zähle alle Ziffern zusammen.')),
    neu('quersumme', 'mehrschritt', Z('Wie viele der Zahlen 123, 456, 789 und 1 010 sind durch 3 teilbar?', 3,
        '1 - min(123 % 3, 1) + 1 - min(456 % 3, 1) + 1 - min(789 % 3, 1) + 1 - min(1010 % 3, 1)',
        'Quersummen: 6, 15, 24 und 2. 6, 15 und 24 sind durch 3 teilbar, 2 nicht. Also sind es 3 Zahlen.', 'Bilde von jeder Zahl die Quersumme.')),
    neu('quersumme', 'mehrschritt', A('Welche Zahl ist durch 3 teilbar?', '2 451', ['2 450', '2 452', '2 453'],
        'Quersummen: 2 450 → 11, 2 451 → 12, 2 452 → 13, 2 453 → 14. Nur 12 ist durch 3 teilbar.', 'Die Zahlen unterscheiden sich nur in der letzten Ziffer. Vergleiche die Quersummen.')),
    neu('quersumme', 'darstellung', Z('Lies die Zahl aus der Stellenwerttafel ab. Wie groß ist ihre Quersumme?', 12, '4 + 2 + 0 + 6',
        'Die Zahl ist 4 206. Quersumme: 4 + 2 + 0 + 6 = 12 (durch 3 teilbar).', 'Jede Spalte ist eine Ziffer. Auch die 0 zählt mit.',
        grafik={'typ': 'stellentafel', 'stellen': ['T', 'H', 'Z', 'E'], 'ziffern': [4, 2, 0, 6]})),
    neu('quersumme', 'begruenden', A('Stimmt die Aussage? „Vertauscht man die Ziffern einer Zahl, die durch 3 teilbar ist, ist die neue Zahl wieder durch 3 teilbar.“',
        'Ja: Beim Vertauschen bleibt die Quersumme gleich.', ['Nein: Nur wenn die letzte Ziffer gleich bleibt.', 'Nein: Das stimmt nur für gerade Zahlen.'],
        'Die Quersumme hängt nicht von der Reihenfolge der Ziffern ab. Beispiel: 51 und 15 haben beide die Quersumme 6, beide sind durch 3 teilbar.',
        'Was passiert mit der Quersumme, wenn du Ziffern vertauschst?')),
    neu('quersumme', 'parameter', Z('In der Zahl 2a4 steht a für eine Ziffer von 0 bis 9. Für wie viele Ziffern a ist die Zahl durch 3 teilbar?', 4, '(9 - 0) // 3 + 1',
        'Quersumme 2 + a + 4 = 6 + a. Sie ist durch 3 teilbar für a = 0, 3, 6, 9. Das sind 4 Ziffern (204, 234, 264, 294).', 'Schreibe die Quersumme mit a auf. Probiere a = 0, 1, 2, …')),
    neu('quersumme', 'rueckwaerts', Z('Eine dreistellige Zahl ist durch 3 teilbar. Ihre Hunderterziffer ist 7, ihre Einerziffer 2. Die Zehnerziffer ist so klein wie möglich. Wie heißt die Zahl?',
        702, '700 + 10 * ((3 - (7 + 2) % 3) % 3) + 2',
        '7 + 2 = 9 ist schon durch 3 teilbar. Die kleinste passende Zehnerziffer ist also 0: 702 (Quersumme 9, 702 : 3 = 234).', 'Was fehlt der Quersumme 7 + 2 noch bis zu einer Zahl der Dreierreihe?')),
    neu('quersumme', 'pruefung', Z('Prüfe mit der Quersumme, ob 1 245 Vereinsmitglieder ohne Rest in 3 gleich große Gruppen passen. Wie viele sind dann in jeder Gruppe?', 415, '1245 // 3',
        'Quersumme 1 + 2 + 4 + 5 = 12, durch 3 teilbar. 1 245 : 3 = 415.', 'Erst die Quersumme prüfen, dann schriftlich teilen.')),
    knobel('quersumme', Z('Man schreibt die Zahlen von 1 bis 20 hintereinander: 1234567891011…1920. Wie groß ist die Quersumme dieser langen Zahl? (Ist sie durch 3 teilbar?)', 102, '45 + 10 + 45 + 2',
        '1 bis 9: 45. 10 bis 19: zehnmal die 1 (10) und die Einer 0 bis 9 (45). 20: 2. Zusammen 45 + 10 + 45 + 2 = 102. 102 ist durch 3 teilbar, also auch die lange Zahl.',
        'Zähle die Ziffern in Gruppen: erst 1 bis 9, dann die Zehner und Einer von 10 bis 19.')),
    pool('quersumme', 'test', _drei(8214)),
    *[pool('quersumme', 'korrektur', _drei(n)) for n in (5302, 7113, 9104)],
    *[pool('quersumme', 'sicherung', _drei(n)) for n in (3471, 6205, 4812, 2008, 7776, 1999)],
    # neunerregel auffüllen
    neu('neunerregel', 'direkt', A('Ist 3 168 durch 9 teilbar?', 'Ja: Quersumme 18, und 18 ist durch 9 teilbar.', ['Nein: Die Endziffer 8 ist nicht durch 9 teilbar.', 'Nein: 3 168 ist gerade.'],
        'Quersumme: 3 + 1 + 6 + 8 = 18. 18 ist durch 9 teilbar, also auch 3 168 (3 168 : 9 = 352).', 'Bilde die Quersumme.')),
    neu('neunerregel', 'direkt', A('Ist 6 241 durch 9 teilbar?', 'Nein: Quersumme 13, und 13 ist nicht durch 9 teilbar.', ['Ja: 6 + 2 + 4 + 1 hat 4 Summanden.', 'Ja: Die erste Ziffer 6 ist durch 3 teilbar.'],
        'Quersumme: 6 + 2 + 4 + 1 = 13. 13 ist nicht durch 9 teilbar, also auch 6 241 nicht.', 'Bilde die Quersumme.')),
    neu('neunerregel', 'erkennen', A('Welche Zahl ist durch 9 teilbar?', '2 718', ['2 717', '2 719', '2 728'],
        'Quersummen: 2 718 → 18, 2 717 → 17, 2 719 → 19, 2 728 → 19. Nur 18 ist durch 9 teilbar.', 'Vergleiche die Quersummen.')),
    neu('neunerregel', 'umkehr', Z('Eine Zahl ist durch 9 teilbar. Ihre Quersumme ist zweistellig und kleiner als 20. Welche Quersumme hat sie?', 18, '2 * 9',
        'Die Quersumme muss durch 9 teilbar sein: 9, 18, 27, … Zweistellig und kleiner als 20 ist nur 18.', 'Welche Zahlen der Neunerreihe sind zweistellig?')),
    neu('neunerregel', 'darstellung', Z('Lies die Zahl aus der Stellenwerttafel ab und teile sie durch 9. Was kommt heraus?', 270, '2430 // 9',
        'Die Zahl ist 2 430. Quersumme 9, also durch 9 teilbar: 2 430 : 9 = 270.', 'Erst die Zahl ablesen, dann prüfen und teilen.',
        grafik={'typ': 'stellentafel', 'stellen': ['T', 'H', 'Z', 'E'], 'ziffern': [2, 4, 3, 0]})),
    neu('neunerregel', 'einkleidung', Z('Ein Gärtner hat 1 845 Tulpenzwiebeln und pflanzt immer 9 in eine Reihe. Wie viele volle Reihen gibt es?', 205, '1845 // 9',
        'Quersumme 1 + 8 + 4 + 5 = 18: Es geht ohne Rest. 1 845 : 9 = 205 Reihen.', 'Prüfe zuerst mit der Quersumme, ob es aufgeht.')),
    neu('neunerregel', 'fehler', A('Jemand sagt: „Die Quersumme von 6 345 ist 18, also ist 6 345 durch 9, aber nicht durch 3 teilbar.“ Was ist falsch?',
        'Jede durch 9 teilbare Zahl ist auch durch 3 teilbar.', ['Die Quersumme ist 19, nicht 18.', '6 345 ist durch keine der beiden Zahlen teilbar.'],
        'Die Quersumme 6 + 3 + 4 + 5 = 18 stimmt. 18 ist durch 9 und durch 3 teilbar. Weil 9 = 3 · 3 ist, ist jede durch 9 teilbare Zahl auch durch 3 teilbar.',
        'Prüfe zuerst die Quersumme. Dann: Was hat 9 mit 3 zu tun?')),
    neu('neunerregel', 'transfer', A('Welche Summe ist durch 9 teilbar? Rechne geschickt.', '4 444 + 5 555', ['3 333 + 2 222', '1 111 + 6 666'],
        '4 444 + 5 555 = 9 999, Quersumme 36: durch 9 teilbar. 5 555 hat die Quersumme 20, 7 777 die Quersumme 28.', 'Rechne jede Summe aus und bilde die Quersumme.')),
    neu('neunerregel', 'rueckwaerts', Z('Ich denke mir eine Zahl und nehme sie mal 9. Heraus kommt 3□75, eine Ziffer ist verdeckt. Welche Ziffer ist es?', 3, '(9 - (3 + 7 + 5) % 9) % 9',
        'Das Ergebnis ist durch 9 teilbar, also auch seine Quersumme: 3 + □ + 7 + 5 = 15 + □. Die nächste Zahl der Neunerreihe ist 18, also □ = 3. Probe: 3 375 : 9 = 375.',
        'Ein Vielfaches von 9 hat eine Quersumme aus der Neunerreihe.')),
    neu('neunerregel', 'verknuepfen', Z('Wie viele Zahlen zwischen 100 und 200 sind durch 9 teilbar?', 11, '(198 - 108) // 9 + 1',
        'Die erste ist 108 (Quersumme 9), die letzte 198 (Quersumme 18). Von 108 bis 198 in Neunerschritten: (198 − 108) : 9 + 1 = 11.', 'Suche die kleinste und die größte passende Zahl und zähle die Neunerschritte.')),
    knobel('neunerregel', Z('Wie viele vierstellige Zahlen bestehen nur aus den Ziffern 1 und 2 und sind durch 9 teilbar?', 0, '8 // 9',
        'Die Quersumme einer solchen Zahl liegt zwischen 1 + 1 + 1 + 1 = 4 und 2 + 2 + 2 + 2 = 8. Keine Zahl von 4 bis 8 ist durch 9 teilbar. Also gibt es keine einzige.',
        'Wie groß kann die Quersumme höchstens werden?')),
    # ggT und kgV nach bruch.brueche
    entfaellt('ggt'), entfaellt('kgv'),
    inhalt(ziel='Teiler und Vielfache finden, Teilbarkeit durch 2, 3, 5 und 10 erkennen, Primzahlen bestimmen und Zahlen in Primfaktoren zerlegen. Vertiefung: die Neunerregel.',
           merke=['Teiler findest du in Paaren.', 'Durch 2, 5, 10: Endziffer. Durch 3: Quersumme (Vertiefung: auch durch 9).', 'Eine Primzahl hat genau zwei Teiler.']),
]
PLAN['bruch.brueche'] = [
    karte_her('zahlen.teilbarkeit', 'ggt', 'Erweitern und kürzen', vor='kuerzen'),
    karte_her('zahlen.teilbarkeit', 'kgv', 'Vergleichen und darstellen', vor='vergleichen'),
    inhalt(merke=['Bruchteil von: durch den Nenner, mal den Zähler.', 'Anteil = Teil : Ganzes, dann kürzen.', 'Ganzes: durch den Zähler, mal den Nenner.',
                  'ggT: größter gemeinsamer Teiler – damit kürzt du vollständig. kgV: kleinstes gemeinsames Vielfaches – der Hauptnenner.',
                  'Erweitern und Kürzen ändern den Wert nicht.', 'Vergleichen: auf den Hauptnenner bringen, dann Zähler vergleichen.']),
]

# A2: Geradengleichungen („y = 2“) kommen erst in Kl. 8. In geometrie.ortslinien heißt die Gerade jetzt „waagrecht durch (0 | 2)“;
# Lösungen, Grafiken, Stufen und Typen bleiben. Neue Fragetexte → alte in „ersetzt“.
_ORTS = [
    (r'^g: y = (−?\d+) und h: y = (−?\d+) sind parallel', r'Die waagrechten Geraden g durch (0 | \1) und h durch (0 | \2) sind parallel'),
    (r'Die waagrechten Geraden g: y = (−?\d+) und h: y = (−?\d+)', r'Die waagrechten Geraden g durch (0 | \1) und h durch (0 | \2)'),
    (r'g ist die Gerade y = (−?\d+), h (?:ist )?die Gerade y = (−?\d+)', r'g ist die waagrechte Gerade durch (0 | \1), h die waagrechte Gerade durch (0 | \2)'),
    (r'die waagrechte Gerade y = (−?\d+)', r'die waagrechte Gerade durch den Punkt (0 | \1)'),
    (r'senkrechten Linie x = (−?\d+)', r'senkrechten Linie durch (\1 | 0)'),
    (r'zwischen den Linien x = (−?\d+) und x = (−?\d+)', r'zwischen den senkrechten Linien durch (\1 | 0) und (\2 | 0)'),
    (r'^y = □ und y = □$', '(0 | □) und (0 | □)'),
    (r'^y = □$', 'waagrecht durch (0 | □)'),
    (r'Trage den y-Wert ein\.', 'Trage den y-Wert des Punkts auf der y-Achse ein.'),
    (r'\b([xy]) = (−?\d+)', r'\1-Wert \2'),
]
PLAN['geometrie.ortslinien'] = [
    umschreiben('parallelen', r'[xy] = −?\d', _ORTS, 29),
    umschreiben('parallelen', r'^Wie viele Punkte haben von der x-Achse den Abstand 2', _ORTS, 1),
    karte('parallelen',
          schritte=[{'text': 'g ist waagrecht durch (0 | 1). Gesucht sind alle Punkte mit Abstand 2.'},
                    {'text': '2 nach oben: 1 + 2 = 3. Die Parallele geht durch ⟦(0 | 3)⟧.', 'bild': {'waagrecht': [1, 3], 'strecken': [[0, 1, 0, 3, 'gestrichelt']]}},
                    {'text': '2 nach unten: 1 − 2 = −1. Die Parallele geht durch ⟦(0 | −1)⟧.',
                     'bild': {'waagrecht': [1, 3, -1], 'strecken': [[0, 1, 0, 3, 'gestrichelt'], [0, 1, 0, -1, 'gestrichelt']]}}],
          woerter=[['Parallele', 'eine Gerade, die überall gleich weit von g entfernt ist'],
                   ['waagrecht durch (0 | 1)', 'die Gerade liegt waagrecht und geht durch (0 | 1); alle ihre Punkte haben die y-Koordinate 1']]),
]

# A2: Der Stundenzeiger dreht „0,5° pro Minute“ – Dezimalzahlen kommen erst in Kl. 6. Neu: „1° in 2 Minuten“ (alle Ergebnisse sind ganzzahlig).
PLAN['geometrie.winkel'] = [
    karte('uhr', regel='Zwischen zwei Zahlen liegen ⟦30°⟧. Der Minutenzeiger dreht 6° pro Minute, der Stundenzeiger 1° in 2 Minuten.'),
    umschreiben('uhr', r'^(Um wie viel Grad dreht sich der Stundenzeiger in \d+ Minuten|Wie groß ist der kleinere Winkel zwischen den Zeigern um (9:20|3:40) Uhr)',
                [(r'also 0,5° pro Minute: (\d+) · 0,5° =', r'also 1° in 2 Minuten: (\1 : 2)° ='),
                 (r'(\d+) Minuten · 0,5° =', r'(\1 : 2)° ='), (r'(\d+) · 0,5° =', r'(\1 : 2)° =')], 5),
]

# A2: Der Begriff „proportional“ steht nicht in M5 (dort Schlussrechnung/Dreisatz); Gymnasium: Kl. 8 (Funktionen), Realschule: M6 LB 6.
# Kein passendes Thema in Kl. 6/7 → Karte „erkennen“ wird Vertiefung.
PLAN['groessen.proportional'] = [vertiefung('erkennen')]

# ======================= Klasse 6 =======================
# A1: negativer Exponent. Zehnerpotenzen mit negativem Exponenten stehen in zahlen.potenzen_zehner (zuerst, Reihenfolge 6).
# terme.potenzgesetze/negativer_exponent behält nur die allgemeine Basis (M6 1.4: „negative ganzzahlige Exponenten als Bruch mit Zähler 1“)
# und verweist auf die Zehnerpotenzen; Aufgaben mit Basis 10 entfallen dort.
# A2: Potenzgesetze (M7 1.1: Produkte von Potenzen bei gleicher Basis oder gleichem Exponenten, Potenzen von Potenzen) → terme.umformen (Kl. 7).
# Quotienten von Potenzen stehen in M7 nicht (erst Kl. 9, zahlen.rationale_exponenten) → dort Vertiefung, ebenso die gemischte Karte „anwenden“.
# fehler_finden (Grundlagen aus M6 und Fehler bei Potenzgesetzen gemischt) bleibt in Kl. 6, aber als Vertiefung.
PLAN['terme.potenzgesetze'] = [
    weg('negativer_exponent', r'^(Was ergibt 10⁰\?|Schreibe 1/1 000 als Potenz mit der Basis 10\.|Schreibe 1/100 000 als Potenz mit der Basis 10\.)', 3),
    pool('negativer_exponent', 'korrektur', T(Z('Schreibe 1/49 als Potenz mit der Basis 7. Wie heißt der Exponent?', -2, '-2 + 0 * 7**2',
         '49 = 7², also 1/49 = 1/7² = 7⁻². Der Exponent ist −2.', '-'))),
    pool('negativer_exponent', 'sicherung', T(Z('Schreibe 1/36 als Potenz mit der Basis 6. Wie heißt der Exponent?', -2, '-2 + 0 * 6**2',
         '36 = 6², also 1/36 = 1/6² = 6⁻². Der Exponent ist −2.', '-'))),
    karte('negativer_exponent', regel='Ein ⟦negativer Exponent⟧ bedeutet Kehrbruch: a⁻ⁿ = 1/aⁿ, wie bei 10⁻ⁿ. Außerdem gilt a⁰ = 1.'),
    entfaellt('mal_gleiche_basis'), entfaellt('geteilt_gleiche_basis'), entfaellt('gleicher_exponent'), entfaellt('anwenden'),
    vertiefung('fehler_finden'),
    abschnitt('Anwenden und prüfen', 'Vertiefung: Fehler finden'),
    inhalt(ziel='Potenzen mit natürlichen und ganzzahligen Exponenten verstehen und berechnen. Die Potenzgesetze folgen in Klasse 7 (Terme umformen).',
           merke=['aⁿ = a · a · … · a (n Faktoren). a⁰ = 1, a⁻ⁿ = 1/aⁿ.', 'Negative Basis in Klammern: (−2)² = 4, aber −2² = −4.']),
]
PLAN['terme.umformen'] = [
    karte_her('terme.potenzgesetze', 'mal_gleiche_basis', 'Potenzen zusammenfassen', nach='produkte'),
    karte_her('terme.potenzgesetze', 'gleicher_exponent', 'Potenzen zusammenfassen', nach='mal_gleiche_basis'),
    karte_her('terme.potenzgesetze', 'geteilt_gleiche_basis', 'Potenzen zusammenfassen', vertiefung=True, nach='gleicher_exponent'),
    karte_her('terme.potenzgesetze', 'anwenden', 'Potenzen zusammenfassen', vertiefung=True, nach='geteilt_gleiche_basis'),
    inhalt(ziel='Terme vereinfachen: gleichartige Glieder zusammenfassen, Produkte und Potenzen zusammenfassen, Klammern auflösen und ausmultiplizieren, ausklammern, Äquivalenz prüfen und die binomischen Formeln anwenden.',
           merke=['Nur gleichartige Glieder zusammenfassen.', 'Gleiche Basis: aᵐ · aⁿ = aᵐ⁺ⁿ. Gleicher Exponent: aⁿ · bⁿ = (a · b)ⁿ.',
                  'Minus vor der Klammer: jedes Vorzeichen darin wechselt.', 'Ausmultiplizieren: Der Faktor kommt zu jedem Glied.', 'Summe mal Summe: jedes Glied mal jedes Glied.',
                  '(a + b)² = a² + 2ab + b², (a − b)² = a² − 2ab + b², (a + b)(a − b) = a² − b².']),
]

# A1: Zinsen. Der ganze Flug finanzen.zinsen (direkt nach bruch.prozent) behandelt Zinsen; die Karte bruch.prozent/zinsen entfällt,
# ihre besten Aufgaben ziehen in die passenden Karten von finanzen.zinsen (nur, was die Grenzen der Zwanzigsten Runde einhält).
PLAN['bruch.prozent'] = [
    entfaellt('zinsen'),
    inhalt(ziel='Prozentangaben verstehen, Prozentwert, Prozentsatz und Grundwert berechnen und einfache Aufgaben zu Rabatt und Aufschlag lösen. Zinsen folgen im nächsten Flug.',
           merke=['p % = p/100. 50 % = 1/2, 25 % = 1/4, 20 % = 1/5, 10 % = 1/10.', 'W = G · p %   ·   p % = W : G   ·   G = W : p %.',
                  'Rabatt p %: neuer Preis = G · (100 % − p %). Aufschlag: G · (100 % + p %).']),
]
PLAN['finanzen.zinsen'] = [
    her('bruch.prozent', 'zinsen', 'jahreszinsen', r'^(Bank A zahlt 3 %, Bank B zahlt 1 %|Ein Kind rechnet: „4 % Zinsen auf 750|Stimmt die Aussage\? „Doppelt so viel Kapital|1 000 € liegen zwei Jahre)', 4, auto=True),
    her('bruch.prozent', 'zinsen', 'jahreszinsen_komma', r'^(1 650 € werden ein Jahr lang zu 1,5 %|Konto A: 1 000 € zu 3 %)', 2, auto=True),
    her('bruch.prozent', 'zinsen', 'zinssatz', r'^(Ein Guthaben wächst in einem Jahr durch Zinsen von 800|Bei welchem ganzzahligen Zinssatz p)', 2, auto=True),
    her('bruch.prozent', 'zinsen', 'kapital', r'^(Bei einem Zinssatz von 2 % bekommt man|Nach einem Jahr mit 3 % Zinsen sind 1 545)', 2, auto=True),
    her('bruch.prozent', 'zinsen', 'monatszinsen', r'^Ein Kredit über 600 € kostet 9 %', 1, auto=True),
    her('bruch.prozent', 'zinsen', 'zeitanteil', r'^Eine Familie leiht sich 4 800 €', 1, auto=True),
]

# A1 + A2: Median, Modalwert, Spannweite sind nicht in M6 (dort: arithmetisches Mittel), aber in M7 (daten.boxplot: Median als weiterer Mittelwert).
# daten.kennwerte behält die drei Mittelwert-Karten; modal_spannweite, median und verstehen (Mittelwert gegen Median) ziehen nach daten.boxplot.
PLAN['daten.kennwerte'] = [
    entfaellt('modal_spannweite'), entfaellt('median'), entfaellt('verstehen'),
    inhalt(ziel='Das arithmetische Mittel bestimmen und deuten – auch aus Häufigkeitstabellen und rückwärts. Median, Modalwert und Spannweite folgen in Klasse 7.',
           merke=['Mittelwert = Summe : Anzahl.', 'Häufigkeitstabelle: Wert · Häufigkeit addieren, durch Gesamtzahl teilen.', 'Summe = Mittelwert · Anzahl.']),
]
PLAN['daten.boxplot'] = [
    her('daten.kennwerte', 'median', 'median', r'S3:.', auto=True),
    her('daten.kennwerte', 'median', 'median', r'S2:^(Punkte von 13 Kindern|Eine Strichliste zeigt|Jemand sagt: „Der Median von 7, 9, 13, 17)', 3, auto=True),
    her('daten.kennwerte', 'modal_spannweite', 'kennwerte', r'S2:^(Temperaturen am Morgen|Lieblingsfarben: rot|Eine Datenreihe hat die Spannweite 12|Bestimme die Spannweite von −2, 0, 2)', 4, auto=True),
    her('daten.kennwerte', 'modal_spannweite', 'kennwerte', r'S3:.', auto=True),
    her('daten.kennwerte', 'verstehen', 'mittel_median', r'S2:^(Stimmt die Aussage\? „(Taschengeld|Wenn ein sehr großer Wert|Der Mittelwert liegt immer|Verdoppelt man alle)|Ein Kind sagt: „Mein Mittelwert)', 6, auto=True),
    her('daten.kennwerte', 'verstehen', 'mittel_median', r'S3:.', auto=True),
]

# ======================= Klasse 7 =======================
# A1: Winkel an Parallelen und Winkelsumme im Dreieck stehen in geometrie.winkelsaetze (Reihenfolge 4) vor geometrie.konstruktion (8).
# Die Karten konstruktion/parallelen und /winkelsumme entfallen; ihre Stufe-3-Aufgaben, Knobel und besonderen Stufe-2-Aufgaben
# ziehen nach winkelsaetze/stufen_wechsel bzw. /innenwinkelsumme (nur, was die Grenzen einhält).
# A2: Satz des Thales (konstruktion/satz_kehrsatz, /gleichschenklig) → geometrie.kreis; satz_kehrsatz wird aufgefüllt.
PLAN['geometrie.konstruktion'] = [
    entfaellt('parallelen'), entfaellt('winkelsumme'),
    weg('satz_kehrsatz', r'^(Satz des Thales: „Wenn C auf dem Kreis|Beweisschritte \(M Mittelpunkt, A und C auf dem Kreis\))', 2),
    weg('gleichschenklig', r'^In einem Kreis mit Mittelpunkt M ist \[AB\] ein Durchmesser', 1),
    neu('gleichschenklig', 'fehler', A('In einem gleichschenkligen Dreieck ist der Winkel an der Spitze 40°. Jemand rechnet: „Jeder Basiswinkel ist 180° − 40° = 140°.“ Was ist falsch?',
        'Die 140° teilen sich zwei gleich große Basiswinkel: Jeder ist 70°.', ['Die Basiswinkel sind zusammen 40°, also je 20°.', 'Nichts: Jeder Basiswinkel ist 140°.'],
        'Winkelsumme 180°: Für beide Basiswinkel zusammen bleiben 180° − 40° = 140°. Sie sind gleich groß, also je 70°. Ein Winkel von 140° wäre allein schon zu groß.',
        'Wie viele Basiswinkel hat das Dreieck, und was gilt für sie?')),
    neu('satz_kehrsatz', 'transfer', A('Satz: „Wenn zwei Geraden parallel sind, dann sind die Wechselwinkel an einer dritten Geraden gleich groß.“ Wie lautet der Kehrsatz, und ist er wahr?',
        '„Wenn die Wechselwinkel gleich groß sind, dann sind die Geraden parallel.“ – wahr.',
        ['„Wenn die Wechselwinkel gleich groß sind, dann sind die Geraden parallel.“ – falsch.', '„Wenn zwei Geraden parallel sind, dann sind die Wechselwinkel gleich groß.“ – wahr.'],
        'Beim Kehrsatz tauschen Wenn-Teil und Dann-Teil. Er ist wahr: Das ist genau die Umkehrung, mit der man Parallelität prüft (Flug Winkelsätze, „Sind die Geraden parallel?“).',
        'Tausche Wenn und Dann. Woran erkennst du parallele Geraden?')),
    neu('satz_kehrsatz', 'transfer', A('Satz aus dem Alltag: „Wenn es regnet, ist die Straße nass.“ Welcher Fall widerlegt den Kehrsatz?',
        'Die Straße ist nass, weil ein Sprengwagen gefahren ist, es regnet aber nicht.', ['Es regnet, und die Straße ist nass.', 'Es regnet nicht, und die Straße ist trocken.'],
        'Der Kehrsatz lautet: „Wenn die Straße nass ist, dann regnet es.“ Ein Gegenbeispiel braucht eine nasse Straße ohne Regen – etwa nach einem Sprengwagen.',
        'Schreibe zuerst den Kehrsatz auf. Ein Gegenbeispiel erfüllt seinen Wenn-Teil, aber nicht seinen Dann-Teil.')),
]
PLAN['geometrie.winkelsaetze'] = [
    her('geometrie.konstruktion', 'parallelen', 'stufen_wechsel', r'S3:.', auto=True),
    her('geometrie.konstruktion', 'winkelsumme', 'innenwinkelsumme', r'S3:.', auto=True),
    # A2: Innenwinkel regelmäßiger Vielecke (Parkett) erst nach der Winkelsumme im Vieleck → Vertiefungskarte zieht aus abbildungen.kongruenz hierher
    karte_her('abbildungen.kongruenz', 'parkett', 'Winkelsummen', vertiefung=True, nach='vieleck'),
]
PLAN['geometrie.kreis'] = [
    her('geometrie.konstruktion', 'satz_kehrsatz', 'umkehrung', r'^Satz des Thales: „Wenn C auf dem Kreis', 1, auto=True),
    her('geometrie.konstruktion', 'satz_kehrsatz', 'beweis', r'^Beweisschritte \(M Mittelpunkt, A und C auf dem Kreis\)', 1, auto=True),
    her('geometrie.konstruktion', 'gleichschenklig', 'thales', r'^In einem Kreis mit Mittelpunkt M ist \[AB\] ein Durchmesser', 1, auto=True),
]
# A2: Achsenspiegelung ohne Geradengleichungen (erst Kl. 8): Achse als senkrechte/waagrechte Gerade durch einen Punkt der Koordinatenachse
# oder als Gerade durch zwei Punkte. Lösungen, Grafiken (bis auf Namen der Geraden), Stufen und Typen bleiben.
_ACHSE = [
    (r'an der Geraden x = (−?\d+) \(senkrecht zur x-Achse\)', r'an der senkrechten Achse durch (\1 | 0)'),
    (r'an der Geraden y = (−?\d+) \(parallel zur x-Achse\)', r'an der waagrechten Achse durch (0 | \1)'),
    (r'an der Geraden x = (−?\d+) gespiegelt', r'an der senkrechten Achse durch (\1 | 0) gespiegelt'),
    (r'an der Winkelhalbierenden y = x|an der Geraden y = x\b', 'an der Geraden durch (0 | 0) und (1 | 1)'),
    (r'an der Geraden y = −x', 'an der Geraden durch (0 | 0) und (1 | −1)'),
    (r'Gib die Achse an\.', 'Gib den Punkt an, in dem die Achse die Koordinatenachse schneidet.'),
    (r'Eine Symmetrieachse ist parallel zur y-Achse\. Gib sie an\.', 'Eine Symmetrieachse ist parallel zur y-Achse. Gib den Punkt an, in dem sie die x-Achse schneidet.'),
    (r'^y = □$', '(0 | □)'), (r'^x = □$', '(□ | 0)'),
    (r'Bei der Spiegelung an y = x', 'Bei der Spiegelung an dieser Geraden'), (r'An y = −?x werden', 'An dieser Geraden werden'),
    (r'Bei y = x tauschen', 'An dieser Geraden tauschen'), (r'Wie bei y = x tauschen', 'Wie an der Geraden durch (0 | 0) und (1 | 1) tauschen'),
    (r'^y = x$', 'a'), (r'^y = −x$', 'a'),
    (r'(?<![\w|])([xy]) = (−?\d+)', r'\1-Wert \2'),
]
PLAN['abbildungen.kongruenz'] = [
    entfaellt('parkett'),
    umschreiben('achsenspiegelung', r'[xy] = −?\d|y = −?x\b|Gib die Achse an|Symmetrieachse ist parallel', _ACHSE),
    umschreiben('achsenspiegelung', r'^(P\(4 \| −3\) wird erst an der x-Achse|Eine Billardkugel liegt bei A\(1 \| 3\))', _ACHSE, 2),
    umschreiben('achsenspiegelung', r'^Bei einer Achsenspiegelung wird A\(−2 \| 3\) auf A', [(r'links von x = 1,', 'links von der Achse,')], 1),
    karte('achsenspiegelung', schritte=[
        {'text': 'P(4 | 3) wird an der senkrechten Achse durch (1 | 0) gespiegelt.'},
        {'text': 'P liegt 3 Kästchen rechts von der Achse.', 'bild': {'strecken': [[1, 3, 4, 3, 'gestrichelt']]}},
        {'text': "Auf der anderen Seite 3 Kästchen nach links: ⟦P'(−2 | 3)⟧.",
         'bild': {'punkte': [{'x': 4, 'y': 3, 'name': 'P'}, {'x': -2, 'y': 3, 'name': "P'"}], 'strecken': [[-2, 3, 4, 3, 'gestrichelt']]}},
        {'text': "Achse durch O und (1 | 1): x und y tauschen, also P'(3 | 4).",
         'bild': {'typ': 'koordinaten', 'x': [-1, 5], 'y': [-1, 5], 'graphen': [{'art': 'linear', 'm': 1, 't': 0, 'name': 'a'}],
                  'punkte': [{'x': 4, 'y': 3, 'name': 'P'}, {'x': 3, 'y': 4, 'name': "P'"}], 'strecken': [[4, 3, 3, 4, 'gestrichelt']]}}]),
]

# ======================= Klasse 8 =======================
# A1: Indirekte Proportionalität steht in groessen.indirekt (Reihenfolge 5) vor funktionen.gebrochen (6). Dort entfallen die beiden Karten
# indirekt und indirekt_sach; ihre besten Aufgaben ziehen in die passenden Karten von groessen.indirekt.
PLAN['funktionen.gebrochen'] = [
    entfaellt('indirekt'), entfaellt('indirekt_sach'),
    inhalt(ziel='Funktionen f(x) = a/(x + b) + c untersuchen: Definitionsmenge, Asymptoten, Achsenschnittpunkte, Verschiebungen. Grundlage ist die indirekte Proportionalität (voriger Flug).',
           merke=['Grundlage: y = k/x (indirekte Proportionalität).', 'f(x) = a/(x + b) + c: D = ℚ \\ {−b}, Asymptoten x = −b und y = c.', 'x − 3 in der Klammer: 3 nach rechts. + c: c nach oben.']),
]
PLAN['groessen.indirekt'] = [
    her('funktionen.gebrochen', 'indirekt', 'graph', r'S3:(Graph|f\(x\) = 12/x)', auto=True),
    her('funktionen.gebrochen', 'indirekt', 'produkt', r'S3:.', auto=True),
    her('funktionen.gebrochen', 'indirekt_sach', 'sach', r'S3:.', auto=True),
]
# A1: Zylinder. Der Flug messen.prisma_zylinder behandelt den Zylinder ausführlich (Volumen begründet, Oberfläche über das Netz – das Netz
# kommt in messen.koerper_darstellung, Reihenfolge 13, nach messen.kreisberechnung, 12). Die Karte kreisberechnung/zylinder entfällt.
PLAN['messen.kreisberechnung'] = [
    entfaellt('zylinder'),
    inhalt(ziel='Umfang und Flächeninhalt von Kreisen, Kreisausschnitten und Kreisringen berechnen – gerundet und exakt mit π. Der Zylinder folgt im Flug zu Prisma und Zylinder.',
           merke=['u = 2πr = πd, A = πr².', 'Ausschnitt: Anteil α/360° von Umfang bzw. Fläche.']),
]
PLAN['messen.prisma_zylinder'] = [
    her('messen.kreisberechnung', 'zylinder', 'zylinder_volumen', r'S3:.', auto=True),
    her('messen.kreisberechnung', 'zylinder', 'zylinder_oberflaeche', r'S3:.', auto=True),
    # A2 aus gleichungen.formeln: Prisma-Aufgaben
    her('gleichungen.formeln', 'geometrie', 'prisma_umstellen', r'Prisma', auto=True),
]
# A2: gleichungen.formeln (Reihenfolge 9) nutzt Körperformeln, die erst später kommen: Prisma (messen.prisma_zylinder, 14) und Pyramide (Kl. 10).
PLAN['gleichungen.formeln'] = [
    weg('geometrie', r'Prisma|Pyramide'),
    neu('geometrie', 'umkehr', Z('Ein Parallelogramm ist 6 cm hoch und hat den Flächeninhalt 75 cm². Wie lang ist die Grundseite?', 12.5, '75 / 6',
        'A = g · h, umgestellt g = A : h = 75 cm² : 6 cm = 12,5 cm.', 'Stelle A = g · h nach g um.', einheit='cm')),
    neu('geometrie', 'umkehr', Z('Ein Quader ist 5 cm hoch und hat das Volumen 120 cm³. Wie groß ist seine Grundfläche in cm²?', 24, '120 // 5',
        'V = G · h, umgestellt G = V : h = 120 cm³ : 5 cm = 24 cm².', 'Volumen = Grundfläche · Höhe. Stelle nach der Grundfläche um.', einheit='cm²')),
    neu('geometrie', 'pruefung', Z('Aus einem Rechteck (10 cm × 6 cm) wird ein Dreieck mit der Grundseite 10 cm ausgeschnitten. Der Rest ist noch 39 cm² groß. Wie hoch ist das Dreieck in cm?',
        4.2, '2 * (10 * 6 - 39) / 10',
        'Rechteck: 60 cm². Dreieck: 60 − 39 = 21 cm². Aus A = g · h : 2 folgt h = 2 · A : g = 2 · 21 : 10 = 4,2 cm.', 'Wie groß ist das Dreieck? Stelle dann A = g · h : 2 nach h um.', einheit='cm')),
    pool('geometrie', 'sicherung', T(Z('Ein Quader hat das Volumen 270 cm³, die Länge 9 cm und die Breite 5 cm. Wie hoch ist er?', 6, '270 // (9 * 5)',
         'Grundfläche 9 · 5 = 45 cm². Höhe = 270 : 45 = 6 cm.', '-', einheit='cm'))),
]
# A1: Schrägbild (q = 1/2) und Ecken/Kanten/Flächen von Prismen stehen in messen.koerper_darstellung (Kl. 8). In raum.schraegbilder (Kl. 10)
# entfällt die Karte laengen (Schrägbilder von Prismen); ihre Pyramiden-Aufgaben bleiben im Flug (Karte pyramide), die besten Prismen-Aufgaben
# ziehen nach koerper_darstellung/schraegbild.
PLAN['messen.koerper_darstellung'] = [
    her('raum.schraegbilder', 'laengen', 'schraegbild', r'S3:^(?!.*Pyramide)', auto=True),
]

# ======================= Klasse 9 =======================
# A1: Parabel–Gerade gehört in die Karte schnittpunkte.
PLAN['funktionen.quadratisch'] = [
    weg('nullstellen', r'^Die Parabel y = x² − 2x − 3 und die Gerade y = x \+ 1', 1),
    neu('nullstellen', 'parameter', Z('Für welche Zahl c hat die Parabel y = x² − 6x + c genau eine Nullstelle?', 9, '6 * 6 // 4',
        'Genau eine Nullstelle heißt: Die Diskriminante ist 0. (−6)² − 4 · 1 · c = 0, also 36 = 4c und c = 9. Dann ist y = (x − 3)².',
        'Wann hat die Lösungsformel nur eine Lösung?')),
    her('funktionen.quadratisch', 'nullstellen', 'schnittpunkte', r'^Die Parabel y = x² − 2x − 3 und die Gerade y = x \+ 1', 1, auto=True),
]
# A2: LGS mit drei Unbekannten – M9 2.2 verlangt nur einfache Beispiele: pruefen, stufenform, eliminieren werden Vertiefung.
PLAN['gleichungen.lgs3'] = [vertiefung('pruefen'), vertiefung('stufenform'), vertiefung('eliminieren')]
# A2: gleichungen.trig steht jetzt nach trigo.allgemein. Was noch vorgreift (Graphen von sin/cos, Bereiche über 360°: Kl. 10 funktionen.trig),
# zieht nach funktionen.trig; Test-/Sicherungsaufgaben mit Graph werden durch Fassungen ohne Graph ersetzt.
PLAN['gleichungen.trig'] = [
    weg('anzahl', r'^Im Bild siehst du den Graphen'),
    weg('sinus', r'720°'), weg('kosinus', r'720°|−360°'), weg('anzahl', r'720°'),
    pool('anzahl', 'korrektur', T(Z('Wie viele Lösungen hat sin x = 0,67 im Bereich 0° ≤ x < 360°?', 2, '1 + 1',
         '0 < 0,67 < 1: Es gibt einen Winkel im I. Quadranten (x ≈ 42,1°) und einen im II. Quadranten (180° − 42,1° ≈ 137,9°). Also 2 Lösungen.', '-'))),
    pool('anzahl', 'sicherung', T(Z('Wie viele Lösungen hat cos x = −1 im Bereich 0° ≤ x < 360°?', 1, '1',
         'cos x = −1 nur bei x = 180° – am Einheitskreis ist das der Punkt ganz links. Also 1 Lösung.', '-'))),
    pool('anzahl', 'sicherung', T(Z('Wie viele Lösungen hat cos x = −0,65 im Bereich 0° ≤ x < 360°?', 2, '1 + 1',
         '−1 < −0,65 < 0: Ein Winkel liegt im II. Quadranten (x ≈ 130,5°), der andere im III. Quadranten (360° − 130,5° ≈ 229,5°). Also 2 Lösungen.', '-'))),
]
PLAN['funktionen.trig'] = [
    her('gleichungen.trig', 'sinus', 'periode', r'720°', auto=True),
    her('gleichungen.trig', 'kosinus', 'periode', r'720°|−360°', auto=True),
    her('gleichungen.trig', 'anzahl', 'periode', r'720°', auto=True),
    her('gleichungen.trig', 'anzahl', 'werte', r'^Im Bild siehst du den Graphen', auto=True),
]

# ======================= Klasse 10 =======================
# A1: a · b^t = c mit dem Logarithmus lösen. funktionen.exponential_log/zeitpunkt (Reihenfolge 1) übt das, bevor Logarithmus und
# Potenzregel erklärt sind (gleichungen.exponential, 2). Der Stoff bleibt dort, wo er erklärt wird; die Karte zeitpunkt entfällt.
PLAN['funktionen.exponential_log'] = [entfaellt('zeitpunkt')]
PLAN['gleichungen.exponential'] = [
    her('funktionen.exponential_log', 'zeitpunkt', 'wachstum', r'S3:.', auto=True),
    her('funktionen.exponential_log', 'zeitpunkt', 'mit_log_loesen', r'S3:.', auto=True),
]
# A1: π schätzen steht in stochastik.mehrstufig/pi_schaetzen. Die π-Aufgaben aus mehrstufig/simulation und simulation/monte_carlo ziehen dorthin.
PLAN['stochastik.mehrstufig'] = [
    weg('simulation', r'Kreis mit Radius 1', 2),
    neu('simulation', 'verknuepfen', Z('Ein Glücksrad hat 4 gleich große Felder mit 1 €, 2 €, 0 € und 5 €. Wie viel Euro gewinnt man im Mittel pro Drehung, wenn man sehr oft dreht?', 2,
        '(1 + 2 + 0 + 5) / 4', 'Jedes Feld kommt auf lange Sicht gleich oft. Mittelwert: (1 + 2 + 0 + 5) : 4 = 2 €.', 'Bei vielen Drehungen kommt jedes Feld etwa gleich oft.', einheit='€')),
    neu('simulation', 'pruefung', Z('Bei einem Spiel wirft man zwei Münzen. Zweimal Kopf bringt 4 Punkte, sonst gibt es 0. Wie viele Punkte erwartet man bei 200 Spielen insgesamt?', 200,
        '200 * 4 // 4', 'P(zweimal Kopf) = 1/2 · 1/2 = 1/4. Erwartet: 1/4 · 200 = 50 Spiele mit 4 Punkten, zusammen 200 Punkte.', 'Pfadregel: Wie wahrscheinlich ist zweimal Kopf?')),
    her('stochastik.mehrstufig', 'simulation', 'pi_schaetzen', r'Kreis mit Radius 1', auto=True),
    her('stochastik.simulation', 'monte_carlo', 'pi_schaetzen', r'Viertelkreis|Kreis mit Radius', auto=True),
]
PLAN['stochastik.simulation'] = [
    weg('monte_carlo', r'Viertelkreis|Kreis mit Radius'),
    neu('monte_carlo', 'umkehr', Z('Ein Quadrat hat 5 cm Seitenlänge. Eine Figur darin ist 10 cm² groß. Wie viele von 500 Zufallspunkten erwartest du ungefähr in der Figur?', 200, '500 * 10 // (5 * 5)',
        'Die Figur bedeckt 10 : 25 = 0,4 des Quadrats. Erwartet: 0,4 · 500 = 200 Punkte.', 'Welcher Anteil des Quadrats ist die Figur?')),
    neu('monte_carlo', 'darstellung', Z('Die Tabelle zeigt drei Simulationsläufe in einem Quadrat mit 4 cm Seitenlänge. Schätze die Fläche der Figur aus allen Läufen zusammen (in cm²).',
        4, '16 * (50 + 72 + 128) / (200 + 300 + 500)',
        'Zusammen: 1 000 Punkte, davon 50 + 72 + 128 = 250 in der Figur. Anteil 250 : 1 000 = 0,25. Fläche ≈ 0,25 · 16 cm² = 4 cm².',
        'Zähle alle Punkte und alle Treffer zusammen.', einheit='cm²',
        grafik={'typ': 'tabelle', 'kopf': ['Lauf', 'Punkte', 'in der Figur'], 'zeilen': [['1', '200', '50'], ['2', '300', '72'], ['3', '500', '128']]})),
    neu('monte_carlo', 'verknuepfen', Z('In einem Quadrat mit 6 cm Seitenlänge ist ein Dreieck mit der Grundseite 6 cm und der Höhe 6 cm gezeichnet. Wie viele von 800 Zufallspunkten erwartest du im Dreieck?',
        400, '800 * (6 * 6 // 2) // 36', 'Dreieck: 6 · 6 : 2 = 18 cm², Quadrat: 36 cm². Anteil 18 : 36 = 1/2, also etwa 400 Punkte.', 'Berechne zuerst beide Flächen.')),
    neu('monte_carlo', 'pruefung', Z('Ein See liegt auf einer rechteckigen Karte, die 4 km breit und 3 km hoch ist. Von 600 Zufallspunkten auf der Karte liegen 210 im See. Wie groß ist der See ungefähr in km²?',
        4.2, '4 * 3 * 210 / 600', 'Anteil 210 : 600 = 0,35. Karte 12 km². See ≈ 0,35 · 12 km² = 4,2 km².', 'Anteil der Treffer mal Fläche der Karte.', einheit='km²')),
    neu('monte_carlo', 'begruenden', A('Zwei Gruppen schätzen dieselbe Fläche, die eine mit 50, die andere mit 5 000 Zufallspunkten. Welche Aussage stimmt?',
        'Die Schätzung mit 5 000 Punkten ist meist genauer, aber auch nicht exakt.', ['Beide Schätzungen sind gleich gut.', 'Mit 5 000 Punkten erhält man den exakten Wert.'],
        'Mit mehr Punkten schwankt der Anteil der Treffer weniger um den wahren Flächenanteil. Exakt wird er trotzdem nicht, weil der Zufall bleibt.',
        'Was passiert mit relativen Häufigkeiten bei vielen Versuchen?')),
]
# A1: Pyramide. Seitenkante und Höhe der quadratischen Pyramide (Pythagoras) stehen in raum.schraegbilder/pyramide (Reihenfolge 8) –
# in raum.pyramide_kegel_kugel/pyr_volumen entfallen sie.
PLAN['raum.schraegbilder'] = [
    entfaellt('laengen'),
    her('raum.schraegbilder', 'laengen', 'pyramide', r'Pyramide', auto=True),
    her('raum.pyramide_kegel_kugel', 'pyr_volumen', 'pyramide', r'^Eine quadratische Pyramide hat die Grundkante a = \d+ cm(, jede Seitenkante| und die Höhe h = \d+ cm\. Wie lang ist eine Seitenkante)', auto=True),
    abschnitt('Prismen und Pyramiden', 'Pyramiden'),
    inhalt(ziel='Pyramiden beschreiben und ihre Schrägbilder verstehen, Lagebeziehungen im Raum erkennen, Rotationskörper und Axialschnitte beschreiben und Punkte im Raum mit Koordinaten angeben. Schrägbilder von Prismen: Klasse 8.'),
]
PLAN['raum.pyramide_kegel_kugel'] = [
    weg('pyr_volumen', r'^Eine quadratische Pyramide hat die Grundkante a = \d+ cm(, jede Seitenkante| und die Höhe h = \d+ cm\. Wie lang ist eine Seitenkante)', 4),
    her('gleichungen.formeln', 'geometrie', 'pyr_volumen', r'Pyramide', auto=True),
    neu('pyr_volumen', 'verknuepfen', Z('Eine quadratische Pyramide und ein Quader haben dieselbe Grundfläche 36 cm² und dieselbe Höhe 6 cm. Wie viele cm³ fasst der Quader mehr als die Pyramide?',
        144, '36 * 6 - 36 * 6 // 3', 'Quader: 36 · 6 = 216 cm³. Pyramide: 1/3 · 216 = 72 cm³. Unterschied 144 cm³.', 'Eine Pyramide fasst ein Drittel des passenden Prismas.', einheit='cm³')),
    neu('pyr_volumen', 'pruefung', Z('Ein Zelt hat die Form einer quadratischen Pyramide mit 3 m Grundkante und 2,5 m Höhe. Wie viele m³ Luft sind darin?', 7.5, '3 * 3 * 25 / 30',
        'G = 3 m · 3 m = 9 m². V = 1/3 · 9 m² · 2,5 m = 7,5 m³.', 'Erst die Grundfläche, dann V = 1/3 · G · h.', einheit='m³')),
    neu('pyr_volumen', 'rueckwaerts', Z('Eine Pyramide ist 12 cm hoch und hat das Volumen 256 cm³. Wie groß ist ihre Grundfläche?', 64, '3 * 256 // 12',
        'V = 1/3 · G · h, also G = 3 · V : h = 3 · 256 : 12 = 64 cm².', 'Stelle V = 1/3 · G · h nach G um.', einheit='cm²')),
]
# A2: Substitution wird erst in gleichungen.polynom/substitution erklärt.
PLAN['funktionen.ganzrational'] = [
    weg('nullstellen', r'x⁴ − (29|17|5)x²', 3),
    neu('nullstellen', 'verknuepfen', Z('Bestimme die größte Nullstelle von f(x) = x³ − 9x.', 3, '3',
        'Ausklammern: x · (x² − 9) = x · (x − 3) · (x + 3) (dritte binomische Formel). Nullstellen −3, 0, 3; die größte ist 3.',
        'Klammere x aus. Erkennst du im Rest eine binomische Formel?')),
    neu('nullstellen', 'rueckwaerts', Z('Eine Funktion 3. Grades mit dem Leitkoeffizienten 1 hat genau die Nullstellen −2, 1 und 4. Wie groß ist ihr Absolutglied?', 8, '2 * (-1) * (-4)',
        'f(x) = (x + 2)(x − 1)(x − 4). Das Absolutglied ist das Produkt der Zahlen in den Klammern: 2 · (−1) · (−4) = 8.',
        'Schreibe f in Produktform. Was bleibt übrig, wenn du x = 0 einsetzt?')),
    neu('nullstellen', 'pruefung', A('f(x) = x² · (x − 3). Welche Aussage über die Nullstellen stimmt?',
        'x = 0 ist doppelte Nullstelle (der Graph berührt), x = 3 ist einfache Nullstelle (der Graph schneidet).',
        ['x = 0 und x = 3 sind beide einfache Nullstellen.', 'x = 3 ist doppelte Nullstelle, x = 0 einfache.', 'Es gibt nur die Nullstelle x = 3.'],
        'x² steht für den Faktor x zweimal: x = 0 ist doppelte Nullstelle, dort berührt der Graph die x-Achse. (x − 3) kommt einmal vor: einfache Nullstelle, Vorzeichenwechsel.',
        'Wie oft kommt jeder Linearfaktor vor?')),
]
PLAN['gleichungen.polynom'] = [her('funktionen.ganzrational', 'nullstellen', 'substitution', r'x⁴ − (29|17|5)x²', auto=True)]
