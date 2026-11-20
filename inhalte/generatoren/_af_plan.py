"""Plan der Vierundzwanzigsten Runde (Zweig aufloesen) – je Zielthema die Schritte für _aufloesen.aufloesen_datei.

Bausteine wie in _bereinigen (karte_her, karte_neu, neu, knobel, pool, karte, weg, ersetze, umschreiben).
Neue Aufgaben: Z (Zahl), L (Lücken) aus _befunde, A (Auswahl, Position fest aus dem Text gemischt) aus _stufen_kl5.
Jede Lösung wird beim Bauen nachgerechnet (c bzw. Lückenausdrücke).
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bereinigen import (karte, karte_her, karte_neu, ersetze, umschreiben, weg, neu, knobel, pool, abschnitt, vertiefung)  # noqa: E402,F401
from _befunde import _z as Z, _l as L  # noqa: E402,F401
from _stufen_kl5 import A  # noqa: E402,F401

PLAN = {}


def W(lz, anfang, neuer_weg, n=1):
    """Nur den Lösungsweg einer umgezogenen Aufgabe neu schreiben (z. B. ohne Gleichung mit Buchstaben)."""
    return umschreiben(lz, '^' + re.escape(anfang), [(r'(?s)\A.*\Z', neuer_weg)], n, felder=('w',))


# =====================================================================================================================
# bruch.brueche (Kl. 6) ← groessen.verhaeltnisse: kuerzen (B, als verhaeltnis_kuerzen), gleichwertig (B). Vertiefung (nur IB).
# Lösungswege mit Buchstaben-Gleichungen (lineare Gleichungen erst Kl. 7) umgeschrieben; 40 % (Prozent erst später in Kl. 6) ersetzt.
# =====================================================================================================================
PLAN['bruch.brueche'] = [
    karte_her('groessen.verhaeltnisse', 'verhaeltnis_kuerzen', 'Erweitern und kürzen', vertiefung=True, nach='kuerzen'),
    karte_her('groessen.verhaeltnisse', 'gleichwertig', 'Erweitern und kürzen', vertiefung=True, nach='verhaeltnis_kuerzen'),
    W('verhaeltnis_kuerzen', 'In einer Gruppe ist das Verhältnis Mädchen : Jungen = 2 : 3. Kommen 2 Mädchen dazu',
      'Bei 2 : 3 haben die Jungen 1 Teil mehr als die Mädchen. Mit 2 neuen Mädchen sind es gleich viele, also ist 1 Teil = 2 Kinder. '
      'Vorher: 2 · 2 = 4 Mädchen und 3 · 2 = 6 Jungen, zusammen 10. Probe: 6 : 6 = 1 : 1.'),
    W('verhaeltnis_kuerzen', 'Zwei Zahlen stehen im Verhältnis 3 : 5. Addiert man zu jeder 4',
      'Probiere gleichwertige Paare zu 3 : 5 und addiere jeweils 4: 3 und 5 → 7 : 9; 6 und 10 → 10 : 14 = 5 : 7; '
      '9 und 15 → 13 : 19; 12 und 20 → 16 : 24 = 2 : 3. Also 12 und 20.'),
    W('gleichwertig', 'Sirup und Wasser wurden im Verhältnis 1 : 5 gemischt.',
      'Der Sirup bleibt gleich, nur das Wasser wächst: vorher 5 Teile, nachher 7 Teile. Die 2 Teile mehr sind 100 ml, '
      'also ist 1 Teil = 50 ml. Das ist der Sirup. Probe: 50 : 350 = 1 : 7.'),
    W('gleichwertig', 'Für welche positive Zahl x sind x : 6 und 6 : (x + 5) gleichwertig?',
      'Probiere kleine Zahlen: x = 2 → 2 : 6 = 1 : 3, aber 6 : 7 nicht. x = 3 → 3 : 6 = 1 : 2, aber 6 : 8 = 3 : 4. '
      'x = 4 → 4 : 6 = 2 : 3 und 6 : 9 = 2 : 3. Also x = 4.'),
    ersetze('gleichwertig', r'^Ein Teil ist 40 % des Ganzen', L(
        'In einer Klasse sind 2/5 der Kinder Mädchen, die anderen sind Jungen. Gib das Verhältnis Mädchen : Jungen an.', '□ : □', [2, 3], ['2', '5 - 2'],
        'Von 5 gleichen Teilen der Klasse sind 2 Teile Mädchen und 5 − 2 = 3 Teile Jungen. Also Mädchen : Jungen = 2 : 3.',
        'Teile die Klasse in 5 gleiche Teile. Wie viele davon sind Jungen?', hinweis='Zwei ganze Zahlen, vollständig gekürzt.')),
]


# =====================================================================================================================
# groessen.proportional (Kl. 5) ← groessen.verhaeltnisse: aenderung (B). Vertiefung (nur IB), am Ende hinter sach.
# Ersetzt: Prozentpunkte (Prozent erst Kl. 6) und Ungleichung mit r (Ungleichungen erst Kl. 8). Knobel-Lösungsweg ohne Gleichung.
# =====================================================================================================================
PLAN['groessen.proportional'] = [
    karte_her('groessen.verhaeltnisse', 'aenderung', 'Anwenden', vertiefung=True, nach='sach'),
    ersetze('aenderung', r'^Ein Handyakku zeigt 80 %', Z(
        'Eine Seilbahn fährt von der Talstation auf 600 m Höhe zur Bergstation auf 1 800 m Höhe. Sie steigt jede Sekunde um 5 m. Wie viele Minuten dauert die Fahrt?',
        4, '(1800 - 600) / 5 / 60', 'Höhenunterschied: 1 800 m − 600 m = 1 200 m. Bei 5 m pro Sekunde: 1 200 : 5 = 240 Sekunden. 240 s = 4 min.',
        'Rechne zuerst aus, wie viele Meter die Bahn insgesamt steigt. Achte auf Sekunden und Minuten.', einheit='min')),
    ersetze('aenderung', r'^Ein Becken enthält 100 l\. Für welche Zuflussraten r', Z(
        'Ein Becken enthält 100 l. Es fließen r Liter pro Minute zu. Für welchen Wert von r sind nach 10 Minuten genau 150 l darin?',
        5, '(150 - 100) / 10', 'In 10 Minuten müssen 150 − 100 = 50 l dazukommen. 50 : 10 = 5, also r = 5 Liter pro Minute.',
        'Wie viele Liter müssen in den 10 Minuten insgesamt dazukommen?')),
    W('aenderung', 'Kerze A ist 20 cm hoch und brennt in 4 Stunden ganz ab',
      'A wird pro Stunde 20 : 4 = 5 cm kürzer, B nur 15 : 5 = 3 cm. A holt also jede Stunde 2 cm auf. Am Anfang ist A 5 cm höher: '
      '5 : 2 = 2,5 Stunden. Dann sind beide 7,5 cm hoch (20 − 12,5 und 15 − 7,5).'),
]


# =====================================================================================================================
# stochastik.verknuepft (Kl. 9) ← mengen.grundbegriffe: elemente (C), schnitt, venn, verstehen (B; als mengen_verstehen)
#                                ← stochastik.bedingt: rueckschluss (B). Alle Vertiefung (nur IB).
# elemente/schnitt als Einstieg vor verknuepfen (doppelt-rsib: Einstiegskarte vor verknuepfen); venn und mengen_verstehen nach
# additionssatz (∪ ist dann aus verknuepfen bekannt; die Karte vereinigung mit n(A) entfällt, daher n(A) als neues Wort).
# =====================================================================================================================
PLAN['stochastik.verknuepft'] = [
    karte_her('mengen.grundbegriffe', 'elemente', 'Ereignisse verknüpfen', vertiefung=True, vor='verknuepfen'),
    karte_her('mengen.grundbegriffe', 'schnitt', 'Ereignisse verknüpfen', vertiefung=True, vor='verknuepfen'),
    karte_her('mengen.grundbegriffe', 'venn', 'Ereignisse verknüpfen', vertiefung=True, nach='additionssatz'),
    karte_her('mengen.grundbegriffe', 'mengen_verstehen', 'Ereignisse verknüpfen', vertiefung=True, nach='venn'),
    karte('mengen_verstehen', woerter=[['n(A)', 'die Anzahl der Elemente von A'],
                                       ['Gegenbeispiel', 'ein Beispiel, bei dem die Aussage nicht stimmt'],
                                       ['Teilmenge', 'A ⊆ B: Jedes Element von A liegt auch in B']]),
    karte_her('stochastik.bedingt', 'rueckschluss', 'Bedingte Wahrscheinlichkeit und Verstehen', vertiefung=True, nach='bedingt'),
    karte('rueckschluss', woerter=[['gemeldet', 'das Prüfgerät schlägt Alarm'],
                                   ['P(A | B)', 'andere Schreibweise für P_B(A): Wahrscheinlichkeit von A, wenn B schon eingetreten ist']]),
    abschnitt('Ereignisse verknüpfen', 'Mengen und Ereignisse verknüpfen'),
]


# =====================================================================================================================
# abbildungen.kongruenz (Kl. 7) ← abbildungen.vektoren: gegenvektor (B). PFLICHT (RS alle Zweige, M7 LB2).
# Achtung: Die Gym-Karte verschiebung davor ist Vertiefung (Gym M7 ohne Verschiebung) – im Bericht gemeldet.
# „Vektor“ kam bisher nur in der entfallenen Karte vektor_bestimmen → als Wort ergänzt. Knobel mit Gleichung 2 · v = …
# (lineare Gleichungen erst nach diesem Flug) durch eine Knobel ohne Gleichung ersetzt.
# =====================================================================================================================
PLAN['abbildungen.kongruenz'] = [
    karte_her('abbildungen.vektoren', 'gegenvektor', 'Verschieben und Drehen', vertiefung=True, nach='verschiebung'),  # Vertiefung (Sebastian 18.11.): Grundkarte verschiebung ist auch Vertiefung
    karte('gegenvektor', woerter=[['Vektor', 'anderes Wort für den Verschiebungspfeil v = (x | y)'],
                                  ['Gegenvektor', 'gleich lang, aber genau entgegengesetzt; zu v gehört −v'],
                                  ['Urpunkt', 'der Punkt vor der Verschiebung']]),
    ersetze('gegenvektor', r'^Für welchen Vektor v ist der Gegenvektor −v genauso groß wie', L(
        'Ein Punkt P wird mit v verschoben und landet bei P′(1 | 4). Derselbe Punkt P wird mit dem Gegenvektor −v verschoben und landet bei Q′(7 | 0). Gib v an.',
        'v = (□ | □)', [-3, 2], ['1 - (1 + 7) // 2', '4 - (4 + 0) // 2'],
        'P′ und Q′ liegen gleich weit von P weg, aber in entgegengesetzter Richtung. Also liegt P genau in der Mitte: P((1 + 7) : 2 | (4 + 0) : 2) = P(4 | 2). '
        'Dann ist v = (1 − 4 | 4 − 2) = (−3 | 2). Probe: (4 | 2) mit −v = (3 | −2) verschoben ergibt (7 | 0).',
        'Wo liegt P im Vergleich zu P′ und Q′?', hinweis='Zwei ganze Zahlen, auch negative.')),
]


# =====================================================================================================================
# funktionen.linear (Kl. 8) ← funktionen.scharen: einsetzen, wirkung (B), bueschel (C). Vertiefung (RS Gruppe I bzw. ohne Beleg).
# Nach lage, weil wirkung „parallel zu …“ braucht. Hinweis Vorwissen: wirkung fragt „Für welche k fallen die Geraden?“
# (k − 4 < 0 ⇒ k < 4). Das ist Vorzeichen-Denken, keine Umformung von Ungleichungen; formal kommt gleichungen.ungleichungen
# erst zwei Flüge später. Bewusst so gelassen (Bericht).
# =====================================================================================================================
PLAN['funktionen.linear'] = [
    karte_her('funktionen.scharen', 'einsetzen', 'Geraden bestimmen', vertiefung=True, nach='lage'),
    karte_her('funktionen.scharen', 'wirkung', 'Geraden bestimmen', vertiefung=True, nach='einsetzen'),
    karte_her('funktionen.scharen', 'bueschel', 'Geraden bestimmen', vertiefung=True, nach='wirkung'),
]

# gleichungen.lgs2 (Kl. 8) ← funktionen.scharen: loesung_parameter (B). Vertiefung, nach loesbarkeit.
PLAN['gleichungen.lgs2'] = [
    karte_her('funktionen.scharen', 'loesung_parameter', 'Verstehen und Anwenden', vertiefung=True, nach='loesbarkeit'),
]


# =====================================================================================================================
# funktionen.reihen (IB, Plan Kl. 10) ← funktionen.folgen: rekursiv (C), arithmetisch, geometrisch (B) als erste drei Karten.
# Pflicht innerhalb des Flugs: Der ganze Flug ist freiwillig (Entscheidung 2), und arith/geom bauen auf diesen Karten auf.
# Die entfallene Karte explizit hat „Folge“, „aₙ“ und „explizite Formel“ eingeführt → als Wörter in rekursiv bzw. arithmetisch.
# =====================================================================================================================
PLAN['funktionen.reihen'] = [
    karte_her('funktionen.folgen', 'rekursiv', 'Schreibweise', vertiefung=False, vor='summenzeichen'),
    karte_her('funktionen.folgen', 'arithmetisch', 'Schreibweise', vertiefung=False, vor='summenzeichen'),
    karte_her('funktionen.folgen', 'geometrisch', 'Schreibweise', vertiefung=False, vor='summenzeichen'),
    karte('rekursiv', woerter=[['Folge', 'eine geordnete Liste von Zahlen a₁, a₂, a₃, …; aₙ ist das Glied an Platz n'],
                               ['rekursiv', 'jedes Glied wird aus dem vorigen berechnet'],
                               ['aₙ₊₁', 'das Glied direkt nach aₙ; a₁ heißt Startwert']]),
    karte('arithmetisch', woerter=[['arithmetische Folge', 'immer dieselbe Zahl d kommt dazu'],
                                   ['d', 'die Differenz zweier Nachbarglieder'],
                                   ['explizite Formel', 'aₙ direkt aus der Platznummer n berechnen, z. B. aₙ = 2n + 14']]),
    abschnitt('Schreibweise', 'Folgen und Schreibweise'),
]


# =====================================================================================================================
# bruch.prozent_grundwert (Kl. 7) ← finanzen.zinseszins: formel (B). Vertiefung (nur IB), nach mehrfach.
# q und „Zinseszins“ führte die entfallene Karte faktor bzw. der Flug ein → als Wörter ergänzt (Potenz ist aus Kl. 5 bekannt).
# =====================================================================================================================
PLAN['bruch.prozent_grundwert'] = [
    karte_her('finanzen.zinseszins', 'formel', 'Komplexere Aufgaben', vertiefung=True, nach='mehrfach'),
    karte('formel', woerter=[['Zinseszins', 'die Zinsen bleiben auf dem Konto und bringen im nächsten Jahr selbst Zinsen'],
                             ['q', 'der Zinsfaktor: q = 1 + p/100, bei 2 % also 1,02'],
                             ['K₀, Kₙ', 'das Anfangskapital und das Kapital nach n Jahren']]),
]


# =====================================================================================================================
# funktionen.quadratisch (Kl. 9)
#  Teil A ← funktionen.transformation: spiegeln (B), Vertiefung (RS Gruppe I), nach parameter.
#  Teil C: umformen und extremwert werden zur Wiederholung des Flugs terme.quadratische_extreme (Klasse 8):
#          Titel und Einstieg verweisen darauf; Beispiel, Merksatz, Fehler, Bild bleiben. Übungen auf die Mindestmengen der
#          Zwanzigsten Runde gekürzt (Stufe 1/2/3: 4/6/8 mit 2/3/4 Typen, 2 Knobel); Test/Korrektur/Sicherung bleiben.
#          Behalten wird, was über Klasse 8 hinausgeht (Parabel, Graph, −b/(2a), Faktor vor x², alle Stufe-3-Aufgaben).
# =====================================================================================================================
def _weg_alle(lz, texte):
    return [weg(lz, '^' + re.escape(t) + '$', 1) for t in texte]


_UMFORMEN_WEG = [
    'Bestimme den Scheitel von y = x² − 4x + 7.', 'Bestimme den Scheitel von y = x² + 14x + 55.',
    'Bestimme den Scheitel von y = x² + 14x + 42.', 'Bei y = x² + 10x + 29 liegt der Scheitel bei x = −b/(2a). Berechne die x-Koordinate des Scheitels.',
    'Bestimme den Scheitel von y = x² − 4x + 4.', 'Bestimme den Scheitel von y = x² − 14x + 42.',  # Stufe 1 (2 davon überzählig)
    'Bestimme den Scheitel von y = −x² − 2x + 1.', 'Bestimme den Scheitel von y = −x² + 14x − 47.', 'Bestimme den Scheitel von y = −x² − 8x − 16.',
    'Bestimme den Scheitel von y = −x² + 2x + 5.', 'Bestimme den Scheitel von y = 3x² − 36x + 113.', 'Bestimme den Scheitel von y = −2x² + 12x − 17.',
    'Bestimme den Scheitel von y = 2x² − 8x.', 'Bestimme den Scheitel von y = −x² + 2x − 10.', 'Bestimme den Scheitel von y = 2x² + 4x + 7.',
]
_EXTREMWERT_WEG = [
    'Welchen kleinsten Wert nimmt f(x) = x² + 4x an?', 'Welchen größten Wert nimmt f(x) = −2x² − 8x − 2 an?',
    'Welchen kleinsten Wert nimmt f(x) = x² − 4x + 4 an?', 'Welchen größten Wert nimmt f(x) = −x² − 6x − 4 an?',
    'Ein rechteckiges Gehege soll mit 108 m Zaun umgeben werden. Welchen größten Flächeninhalt kann es haben?',
    'Zwei Zahlen haben die Summe 36. Wie groß ist ihr Produkt höchstens?',  # überzählig
    'Ein rechteckiges Gehege soll mit 12 m Zaun umgeben werden. Welchen größten Flächeninhalt kann es haben?',  # überzählig
    'An einer Hauswand soll ein rechteckiger Auslauf mit 76 m Zaun abgegrenzt werden (die Wand ersetzt eine Seite). Welche Fläche ist höchstens möglich?',  # überzählig
    'An einer Hauswand soll ein rechteckiger Auslauf mit 96 m Zaun abgegrenzt werden (die Wand ersetzt eine Seite). Welche Fläche ist höchstens möglich?',  # überzählig
]

PLAN['funktionen.quadratisch'] = [
    karte_her('funktionen.transformation', 'spiegeln', 'Parabeln lesen', vertiefung=True, nach='parameter'),
    karte('umformen', titel='Wiederholung: Scheitelform bestimmen',
          einstieg='Die quadratische Ergänzung kennst du aus dem Flug „Quadratische Terme und Extremwerte“ (Klasse 8). '
                   'Hier nutzt du sie für Parabeln: Die Scheitelform zeigt dir sofort den ⟦Scheitel⟧.'),
    karte('extremwert', titel='Wiederholung: Extremwertprobleme',
          einstieg='Das größte Gehege mit festem Zaun kennst du aus dem Flug „Quadratische Terme und Extremwerte“ (Klasse 8). '
                   'Neu ist der Blick auf die Parabel: Ihr Scheitel ist der ⟦Extremwert⟧.'),
    *_weg_alle('umformen', _UMFORMEN_WEG),
    *_weg_alle('extremwert', _EXTREMWERT_WEG),
]


# funktionen.exponential_log (Kl. 10) ← funktionen.transformation: punkte (C). Vertiefung (RS Gruppe I Kl. 10), nach graph.
PLAN['funktionen.exponential_log'] = [
    karte_her('funktionen.transformation', 'punkte', 'Graphen und Logarithmus', vertiefung=True, nach='graph'),
]


# =====================================================================================================================
# funktionen.potenz (Kl. 9) ← funktionen.umkehr: umkehrbar, linear (C) vor wurzelfunktion; quadratisch, spiegeln (B) danach.
# Vertiefung (RS Gruppe I Kl. 10; Gym-Lehrplan nicht geprüft). Exponentialfunktionen kommen erst in Klasse 10:
# 5 Aufgaben mit 2ˣ/0,5ˣ/3ˣ ersetzt (gleicher Typ, gleiche Stufe), Beispiel von spiegeln auf y = x² und √x umgestellt.
# Die entfallene Karte werte führte „Umkehrfunktion“ und „f⁻¹“ ein → als Wörter in linear (wurzelfunktion kommt erst danach).
# =====================================================================================================================
_JA_NEIN = ['Das hängt vom x-Wert ab.']
PLAN['funktionen.potenz'] = [
    karte_her('funktionen.umkehr', 'umkehrbar', 'Erweiterung des Potenzbegriffs', vertiefung=True, vor='wurzelfunktion'),
    karte_her('funktionen.umkehr', 'linear', 'Erweiterung des Potenzbegriffs', vertiefung=True, vor='wurzelfunktion'),
    karte_her('funktionen.umkehr', 'quadratisch', 'Erweiterung des Potenzbegriffs', vertiefung=True, nach='wurzelfunktion'),
    karte_her('funktionen.umkehr', 'spiegeln', 'Erweiterung des Potenzbegriffs', vertiefung=True, nach='quadratisch'),
    karte('linear', woerter=[['Umkehrfunktion', 'rechnet rückwärts: aus f(a) = b wird f⁻¹(b) = a'],
                             ['f⁻¹', 'gelesen „f hoch minus eins“: die Umkehrfunktion, kein Kehrwert'],
                             ['nach y auflösen', 'umformen, bis y allein auf einer Seite steht']]),
    ersetze('umkehrbar', r'^Ist f\(x\) = 0,5ˣ', A('Ist f(x) = −x³ (x ∈ ℝ) umkehrbar?', 'Ja', ['Nein'] + _JA_NEIN,
        'Der Graph von −x³ fällt überall. Jede waagrechte Gerade trifft ihn genau einmal.', 'Kommt ein y-Wert mehrmals vor?')),
    ersetze('umkehrbar', r'^Ist f\(x\) = 2ˣ', A('Ist f(x) = 0,5x² (x ∈ ℝ) umkehrbar?', 'Nein', ['Ja'] + _JA_NEIN,
        '0,5x² macht aus 2 und aus −2 dieselbe Zahl 2. Die waagrechte Gerade y = 2 trifft den Graphen zweimal.', 'Kommt ein y-Wert mehrmals vor?')),
    ersetze('umkehrbar', r'^Jemand behauptet: „f\(x\) = 2ˣ', A(
        'Jemand behauptet: „f(x) = x³ (x ∈ ℝ) ist umkehrbar, weil zu jedem x genau ein y gehört.“ Was stimmt?',
        'Ergebnis stimmt, Begründung nicht: Es kommt darauf an, dass jeder y-Wert nur einmal vorkommt.',
        ['Richtig, genau so begründet man es.', 'Falsch: Umkehrbar sind nur Geraden.', 'Falsch: Keine Funktion ist umkehrbar.'],
        'x³ steigt überall, also kommt jeder y-Wert nur einmal vor. Dass zu jedem x genau ein y gehört, gilt für jede Funktion.',
        'Was muss für die Umkehrung eindeutig sein?')),
    ersetze('umkehrbar', r'^Warum ist f\(x\) = 2 · 0,5ˣ \+ 1', A(
        'Warum ist f(x) = −2x⁵ + 1 (x ∈ ℝ) umkehrbar?', 'Weil der Graph überall fällt: Jeder y-Wert kommt nur einmal vor.',
        ['Weil zu jedem x genau ein y gehört.', 'Weil der Graph die y-Achse bei 1 schneidet.', 'Weil der Exponent 5 größer als 1 ist.'],
        'x⁵ steigt überall. Mal −2 fällt der Graph überall, + 1 schiebt ihn nur nach oben. Eine waagrechte Gerade trifft ihn höchstens einmal.',
        'Steigt oder fällt der Graph überall?')),
    ersetze('umkehrbar', r'^Wie viele der Funktionen x, x², x³, x⁴, x⁵, 2ˣ', Z(
        'Wie viele der Funktionen x, x², x³, x⁴, x⁵, x⁻¹ und x⁻² (bei x⁻¹ und x⁻² ist x ≠ 0) sind auf ihrer ganzen Definitionsmenge umkehrbar?',
        4, '4', 'Umkehrbar: x, x³, x⁵ (steigen überall) und x⁻¹ = 1/x (jeder y-Wert ≠ 0 kommt genau einmal vor). '
        'Nicht umkehrbar: x², x⁴ und x⁻² (x und −x haben denselben y-Wert). Also 4.',
        'Prüfe bei jeder Funktion, ob ein y-Wert doppelt vorkommt.')),
    ersetze('spiegeln', r'^f\(x\) = 3ˣ \+ 1', L(
        'f(x) = x³ + 2. Wo schneidet der Graph von f⁻¹ die x-Achse?', 'N(□ | □)', [2, 0], ['0**3 + 2', '0'],
        'f(0) = 0 + 2 = 2, also liegt (0 | 2) auf f. Gespiegelt an y = x: (2 | 0) liegt auf f⁻¹.', 'Berechne zuerst f(0).',
        hinweis='Trage die Zahlen ein.')),
    karte('spiegeln',
          bild={'typ': 'koordinaten', 'x': [-1, 6], 'y': [-1, 6],
                'graphen': [{'art': 'poly', 'k': [0, 0, 1], 'bereich': [0, 2.4], 'name': 'y = x²'}, {'art': 'linear', 'm': 1, 't': 0, 'name': 'y = x'}]},
          schritte=[{'text': 'P(2 | 4) liegt auf y = x² (nur x ≥ 0).', 'bild': {'punkte': [{'x': 2, 'y': 4, 'name': 'P'}]}},
                    {'text': 'Spiegeln an der Winkelhalbierenden heißt: x und y tauschen.'},
                    {'text': 'So entsteht ⟦P′(4 | 2)⟧ auf y = √x.',
                     'bild': {'graphen': [{'art': 'poly', 'k': [0, 0, 1], 'bereich': [0, 2.4], 'name': 'y = x²'}, {'art': 'linear', 'm': 1, 't': 0, 'name': 'y = x'},
                                          {'art': 'wurzel', 'bereich': [0, 6], 'name': '√x'}],
                              'punkte': [{'x': 2, 'y': 4, 'name': 'P'}, {'x': 4, 'y': 2, 'name': 'P′'}], 'strecken': [[2, 4, 4, 2, 'gestrichelt']]}}],
          fehler='P′(−2 | −4) ist falsch, das wäre am ⟦Ursprung⟧ gespiegelt. An y = x werden die Koordinaten getauscht.'),
]


# stochastik.mehrstufig (Kl. 10) ← stochastik.bedingt: unabhaengig (C). Vertiefung (nur IB), nach ohne_zuruecklegen.
# P(A | B) ist im Gym-Flug stochastik.verknuepft als P_B(A) geschrieben → als Wort ergänzt.
PLAN['stochastik.mehrstufig'] = [
    karte_her('stochastik.bedingt', 'unabhaengig', 'Pfadregeln', vertiefung=True, nach='ohne_zuruecklegen'),
    karte('unabhaengig', woerter=[['unabhängig', 'das Wissen über B ändert die Wahrscheinlichkeit von A nicht'],
                                  ['abhängig', 'das Wissen über B ändert die Wahrscheinlichkeit von A'],
                                  ['P(A | B)', 'andere Schreibweise für P_B(A): Wahrscheinlichkeit von A, wenn B schon eingetreten ist']]),
]


# =====================================================================================================================
# Teil B: neue Lernkarten (Definitionen in _af_neu.py)
# =====================================================================================================================
from _af_neu import DUAL, BILDGERADE, SCHWERPUNKT, SCHNITTWINKEL, ADDITION, ABSTAND  # noqa: E402

PLAN['zahlen.natuerlich'] = DUAL
PLAN['abbildungen.aehnlichkeit'] = BILDGERADE + SCHWERPUNKT
PLAN['trigo.rechtwinklig'] = SCHNITTWINKEL
PLAN['trigo.allgemein'] = ADDITION
PLAN['abbildungen.matrizen'] = ABSTAND
