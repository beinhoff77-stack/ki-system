#!/usr/bin/env python3
"""Thema stochastik.verknuepft – Verknüpfte Ereignisse (Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(914)

PRIM = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
EREIG = [
    ('gerade', lambda k: k % 2 == 0),
    ('ungerade', lambda k: k % 2 == 1),
    ('durch 3 teilbar', lambda k: k % 3 == 0),
    ('durch 4 teilbar', lambda k: k % 4 == 0),
    ('durch 5 teilbar', lambda k: k % 5 == 0),
    ('eine Primzahl', lambda k: k in PRIM),
    ('eine Quadratzahl', lambda k: int(k ** 0.5) ** 2 == k),
]
SZEN = [  # (Gesamtheit, Merkmal A, Merkmal B)
    ('Schülerinnen und Schüler einer Schule', 'hat ein Haustier', 'fährt mit dem Rad zur Schule'),
    ('Besucher eines Freibads', 'ist Erwachsener', 'hat eine Jahreskarte'),
    ('Teilnehmende einer Umfrage', 'liest täglich Nachrichten', 'ist älter als 40 Jahre'),
    ('Mitglieder eines Fußballvereins', 'spielt in einer Mannschaft', 'ist jünger als 18 Jahre'),
    ('Fahrgäste eines Zuges', 'hat einen Sitzplatz reserviert', 'fährt in der 1. Klasse'),
    ('Kunden eines Online-Shops', 'zahlt per Rechnung', 'bestellt zum ersten Mal'),
]


def tafel_text(aa, ab, ba, bb, A='A', B='B'):
    return (f'Vierfeldertafel (Anzahlen): {A} und {B}: {dz(aa)}; {A} und nicht {B}: {dz(ab)}; '
            f'nicht {A} und {B}: {dz(ba)}; nicht {A} und nicht {B}: {dz(bb)}.')


def zufalls_tafel(N):
    while True:
        cuts = sorted(R.sample(range(1, N), 3))
        t = [cuts[0], cuts[1] - cuts[0], cuts[2] - cuts[1], N - cuts[2]]
        if min(t) >= max(2, N // 25): return t


SZEN_W = {  # Gesamtheit -> (Einzelner, Merkmal A kurz, nicht A, Merkmal B kurz, nicht B)
    'Schülerinnen und Schüler einer Schule': ('ein Kind dieser Schule', 'Haustier', 'kein Haustier', 'Rad', 'kein Rad'),
    'Besucher eines Freibads': ('ein Besucher', 'erwachsen', 'Kind', 'Jahreskarte', 'keine Jahreskarte'),
    'Teilnehmende einer Umfrage': ('eine teilnehmende Person', 'liest täglich', 'liest nicht täglich', 'über 40', 'höchstens 40'),
    'Mitglieder eines Fußballvereins': ('ein Vereinsmitglied', 'Mannschaft', 'keine Mannschaft', 'unter 18', 'mindestens 18'),
    'Fahrgäste eines Zuges': ('ein Fahrgast', 'reserviert', 'nicht reserviert', '1. Klasse', '2. Klasse'),
    'Kunden eines Online-Shops': ('eine Kundin oder ein Kunde', 'Rechnung', 'andere Zahlung', 'Erstbestellung', 'Stammkunde'),
}


def tafel(aa, ab, ba, bb, zeige, frage=None, kopfA=('A', 'nicht A'), kopfB=('B', 'nicht B'), fmt=None):
    """Vierfeldertafel als Tabelle. zeige: Menge der sichtbaren Felder aus aa ab ba bb A nA B nB N; frage: Feld mit '?'."""
    fmt = fmt or dz
    w = {'aa': aa, 'ab': ab, 'ba': ba, 'bb': bb, 'A': aa + ab, 'nA': ba + bb, 'B': aa + ba, 'nB': ab + bb, 'N': aa + ab + ba + bb}
    z = lambda k: '?' if k == frage else (fmt(w[k]) if k in zeige else '')  # noqa: E731
    return {'typ': 'tabelle', 'kopf': ['', kopfB[0], kopfB[1], 'Summe'],
            'zeilen': [[kopfA[0], z('aa'), z('ab'), z('A')], [kopfA[1], z('ba'), z('bb'), z('nA')], ['Summe', z('B'), z('nB'), z('N')]]}


def cf(x):
    return str(float(x)) if Fr(x).denominator != 1 else str(int(x))


ETAPPEN = [
    {'lernziel': 'verknuepfen', 'titel': 'Schnitt, Vereinigung, Gegenereignis',
     'regel': '⟦A ∩ B⟧ („A und B“): beide treten ein. ⟦A ∪ B⟧ („A oder B“): mindestens eines tritt ein. ⟦Ā⟧ („nicht A“): A tritt nicht ein. Bei Laplace-Experimenten: P = Anzahl günstiger : Anzahl möglicher Ergebnisse.',
     'schritte': ['Zahl aus 1–20, A: gerade, B: durch 3 teilbar. A ∩ B = {6, 12, 18}.', 'P(A ∩ B) = 3 : 20 = ⟦0,15⟧.'],
     'probe': '6, 12, 18 sind gerade und durch 3 teilbar ✓',
     'bild': {'typ': 'figur', 'punkte': {'_M1': [0, 0], '_M2': [4, 0], 'A': [-2.6, 2.6], 'B': [6.6, 2.6], '6, 12, 18': [2, 0]}, 'kreise': [{'m': '_M1', 'r': 3.5}, {'m': '_M2', 'r': 3.5}]},
     'fehler': 'A ∪ B mit „beide“ zu übersetzen ist falsch: ⟦∪ heißt „oder“⟧ (mindestens eines), ⟦∩ heißt „und“⟧ (beide).'},
    {'lernziel': 'additionssatz', 'titel': 'Der Additionssatz',
     'regel': '⟦P(A ∪ B) = P(A) + P(B) − P(A ∩ B)⟧. Die Schnittmenge wird einmal abgezogen, weil sie sonst ⟦doppelt gezählt⟧ würde. Sind A und B ⟦unvereinbar⟧ (A ∩ B = ∅), gilt P(A ∪ B) = P(A) + P(B).',
     'schritte': ['P(A) = 0,5, P(B) = 0,3, P(A ∩ B) = 0,1.', 'P(A ∪ B) = 0,5 + 0,3 − 0,1 = ⟦0,7⟧.'],
     'probe': 'P(Ā ∩ B̄) = 1 − 0,7 = 0,3 ≥ 0 ✓',
     'bild': {'typ': 'figur', 'punkte': {'_M1': [0, 0], '_M2': [4, 0], 'A': [-2.6, 2.6], 'B': [6.6, 2.6], '6, 12, 18': [2, 0]}, 'kreise': [{'m': '_M1', 'r': 3.5}, {'m': '_M2', 'r': 3.5}]},
     'fehler': 'P(A ∪ B) = 0,5 + 0,3 = 0,8 ist falsch, wenn A und B gemeinsame Ergebnisse haben: Die ⟦Schnittmenge⟧ wurde doppelt gezählt.'},
    {'lernziel': 'vierfeld', 'titel': 'Vierfeldertafel ergänzen',
     'regel': 'Eine ⟦Vierfeldertafel⟧ ordnet nach zwei Merkmalen. ⟦Zeilen- und Spaltensummen⟧ müssen stimmen; unten rechts steht die Gesamtzahl. Fehlende Felder durch Ergänzen zur Summe.',
     'schritte': ['200 Befragte, 80 haben Merkmal A, davon 30 auch Merkmal B.', 'A und nicht B: 80 − 30 = ⟦50⟧; nicht A: 200 − 80 = 120.'],
     'probe': '30 + 50 = 80 ✓',
     'bild': {'typ': 'tabelle', 'kopf': ['', 'B', 'nicht B', 'Summe'], 'zeilen': [['A', '30', '?', '80'], ['nicht A', '', '', '?'], ['Summe', '', '', '200']]},
     'fehler': 'Das Feld „A und nicht B“ als 200 − 30 zu berechnen ist falsch: Man ergänzt innerhalb der ⟦Zeile A⟧ zu deren Summe 80.'},
    {'lernziel': 'tafel_wkeit', 'titel': 'Wahrscheinlichkeiten aus der Tafel',
     'regel': 'Teilt man jede Anzahl durch die ⟦Gesamtzahl⟧, erhält man eine Vierfeldertafel mit Wahrscheinlichkeiten. ⟦P(A) = P(A ∩ B) + P(A ∩ B̄)⟧ (Randsumme).',
     'schritte': ['Gesamt 400, A und B: 60, A und nicht B: 100.', 'P(A ∩ B) = 60 : 400 = 0,15; P(A) = 160 : 400 = ⟦0,4⟧.'],
     'probe': '0,15 + 0,25 = 0,4 ✓',
     'bild': {'typ': 'tabelle', 'kopf': ['', 'B', 'nicht B', 'Summe'], 'zeilen': [['A', '60 → 0,15', '100 → 0,25', '160 → 0,4'], ['Summe', '', '', '400 → 1']]},
     'fehler': 'P(A ∩ B) = 60 : 160 ist falsch, wenn nach der Wahrscheinlichkeit unter ⟦allen⟧ gefragt ist: Man teilt durch die ⟦Gesamtzahl⟧ 400.'},
    {'lernziel': 'bedingt', 'titel': 'Bedingte Wahrscheinlichkeit',
     'regel': '⟦P_B(A)⟧ ist die Wahrscheinlichkeit von A, ⟦wenn man schon weiß⟧, dass B eingetreten ist: ⟦P_B(A) = P(A ∩ B) : P(B)⟧. In der Tafel: nur die ⟦Spalte B⟧ betrachten.',
     'schritte': ['200 Personen, davon 50 mit B. Von diesen 50 haben 20 auch A.', 'Du weißt schon: B ist eingetreten. Dann zählt nur die ⟦Spalte B⟧ mit 50 Personen.', 'P_B(A) = 20 : 50 = ⟦0,4⟧.'],
     'probe': 'Man teilt durch die Anzahl in B, nicht durch alle ✓',
     'fehler': 'P_B(A) und P_A(B) verwechseln. P_B(A) = 20 : 50 = 0,4 (unter allen mit B). P_A(B) = 20 : 80 = 0,25 (unter allen mit A). Die ⟦Bedingung⟧ unten bestimmt, ⟦durch welche Summe⟧ du teilst.',
     'bild': {'typ': 'tabelle', 'kopf': ['', 'B', 'nicht B', 'Summe'], 'zeilen': [['A', '20', '60', '80'], ['nicht A', '30', '90', '120'], ['Summe', '50', '150', '200']]}},
    {'lernziel': 'verstehen', 'titel': 'Aussagen über Ereignisse prüfen',
     'regel': 'Prüfe Aussagen mit Mengen und Zahlen: ⟦unvereinbar⟧ heißt A ∩ B = ∅. Das ⟦Gegenereignis⟧ von „mindestens eins“ ist „keins“. Wahrscheinlichkeiten liegen zwischen ⟦0 und 1⟧.',
     'schritte': ['Behauptung: P(A) = 0,7 und P(B) = 0,6, also sind A und B unvereinbar.', 'Wären sie unvereinbar, wäre P(A ∪ B) = 1,3 > 1 – unmöglich. ⟦A und B müssen sich überschneiden⟧.'],
     'probe': 'P(A ∩ B) ≥ 0,7 + 0,6 − 1 = 0,3 ✓',
     'fehler': 'Das Gegenereignis von „mindestens ein Treffer“ ist nicht „mindestens ein Fehlschuss“, sondern ⟦„kein Treffer“⟧.'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'verknuepfen': {
  'einstieg': 'Beim Schulfest zieht man ein Los mit einer Zahl von 1 bis 20. Einen Preis gibt es für gerade Zahlen, einen Sonderpreis für Zahlen, die durch 3 teilbar sind. Wer gewinnt beides? Wer gewinnt mindestens einen Preis? Solche Fragen verbinden zwei Ereignisse – man ⟦verknüpft Ereignisse⟧.',
  'woerter': [['Ereignis A, B', 'eine Menge von Ergebnissen, z. B. A = gerade Zahl'],
              ['A ∩ B („A und B“, Schnitt)', 'beide Ereignisse treten ein'],
              ['A ∪ B („A oder B“, Vereinigung)', 'mindestens eines der Ereignisse tritt ein'],
              ['Ā („nicht A“, Gegenereignis)', 'A tritt nicht ein'],
              ['Laplace-Experiment', 'alle Ergebnisse sind gleich wahrscheinlich, wie beim Losziehen'],
              ['P(…)', 'die Wahrscheinlichkeit, eine Zahl von 0 bis 1']],
  'bild': {'typ': 'figur', 'punkte': {'_M1': [0, 0], '_M2': [4, 0], 'A: gerade': [-2.6, 2.6], 'B: durch 3 teilbar': [6.6, 2.6], 'A ∩ B: 6, 12, 18': [2, 0]}, 'kreise': [{'m': '_M1', 'r': 3.5}, {'m': '_M2', 'r': 3.5}]},
  'schritte': ['Lose 1 bis 20. A: Die Zahl ist gerade. B: Die Zahl ist durch 3 teilbar.',
               'Beide Preise gibt es für Zahlen, die gerade und durch 3 teilbar sind: A ∩ B = {6, 12, 18}.',
               'Das sind 3 günstige von 20 möglichen Losen.',
               'P(A ∩ B) = 3 : 20 = ⟦0,15⟧.'],
  'regel': 'So übersetzt du: ⟦A ∩ B⟧ heißt „A und B“, beide treten ein. ⟦A ∪ B⟧ heißt „A oder B“, mindestens eines tritt ein. ⟦Ā⟧ heißt „nicht A“. Bei Laplace-Experimenten gilt: P = Anzahl günstiger : Anzahl möglicher Ergebnisse.',
  'fehler': 'A ∪ B mit „beide“ zu übersetzen ist falsch: Für A ∪ B reicht schon ein Preis. ⟦∪ heißt „oder“⟧ (mindestens eines), ⟦∩ heißt „und“⟧ (beide).'},
 'additionssatz': {
  'einstieg': 'Wie wahrscheinlich ist mindestens ein Preis? Zählt man nur die Gewinner von Preis A und Preis B zusammen, zählt man die Doppelgewinner zweimal. Diese müssen einmal wieder abgezogen werden. Die Regel dafür heißt ⟦Additionssatz⟧.',
  'woerter': [['Additionssatz', 'P(A ∪ B) = P(A) + P(B) − P(A ∩ B)'],
              ['Schnittmenge', 'die Ergebnisse, die zu A und zu B gehören'],
              ['unvereinbar', 'A und B haben kein gemeinsames Ergebnis'],
              ['∅', 'die leere Menge']],
  'bild': {'typ': 'figur', 'punkte': {'_M1': [0, 0], '_M2': [4, 0], 'A: P = 0,5': [-2.6, 2.6], 'B: P = 0,3': [6.6, 2.6], 'A ∩ B: 0,1': [2, 0]}, 'kreise': [{'m': '_M1', 'r': 3.5}, {'m': '_M2', 'r': 3.5}]},
  'schritte': ['Gegeben: P(A) = 0,5, P(B) = 0,3 und P(A ∩ B) = 0,1.',
               'P(A) + P(B) = 0,8 enthält den Teil A ∩ B zweimal.',
               'Einmal abziehen: 0,8 − 0,1.',
               'Also P(A ∪ B) = ⟦0,7⟧.'],
  'regel': 'So rechnest du mit dem ⟦Additionssatz⟧: ⟦P(A ∪ B) = P(A) + P(B) − P(A ∩ B)⟧. Die Schnittmenge wird einmal abgezogen, weil sie sonst ⟦doppelt gezählt⟧ würde. Sind A und B ⟦unvereinbar⟧ (A ∩ B = ∅), gilt P(A ∪ B) = P(A) + P(B).',
  'fehler': 'P(A ∪ B) = 0,5 + 0,3 = 0,8 ist falsch, wenn A und B gemeinsame Ergebnisse haben: Die Doppelgewinner, also die ⟦Schnittmenge⟧, wurden doppelt gezählt.'},
 'vierfeld': {
  'einstieg': 'Nach dem Schulfest werden 200 Gäste befragt: Haben sie gegessen (A)? Haben sie am Losstand gespielt (B)? Jeder Gast passt in genau eines von vier Feldern. So eine Tabelle mit zwei Merkmalen heißt ⟦Vierfeldertafel⟧.',
  'woerter': [['Vierfeldertafel', 'eine Tabelle mit zwei Merkmalen, je „ja“ und „nein“, also vier Feldern'],
              ['Merkmal', 'eine Eigenschaft, z. B. „hat gegessen“'],
              ['Zeilensumme / Spaltensumme', 'die Summe einer Zeile bzw. Spalte, am Rand'],
              ['Gesamtzahl', 'unten rechts: alle Befragten']],
  'bild': {'typ': 'tabelle', 'kopf': ['', 'B (Los gespielt)', 'nicht B', 'Summe'], 'zeilen': [['A (gegessen)', '30', '?', '80'], ['nicht A', '', '', '?'], ['Summe', '', '', '200']]},
  'schritte': ['200 Befragte, 80 haben gegessen (A). Von diesen 80 haben 30 auch gespielt (B).',
               'Die Zeile A muss 80 ergeben. Das Feld „A und nicht B“ ist der Rest: 80 − 30 = ⟦50⟧.',
               'Die Spalte Summe muss 200 ergeben. „Nicht A“ ist der Rest: 200 − 80 = 120.',
               'So lassen sich alle Felder Schritt für Schritt zur jeweiligen Summe ergänzen.'],
  'regel': 'So ergänzt du eine ⟦Vierfeldertafel⟧: ⟦Zeilen- und Spaltensummen⟧ müssen stimmen; unten rechts steht die Gesamtzahl. Ein fehlendes Feld ist die Summe seiner Zeile oder Spalte minus die bekannten Felder.',
  'fehler': 'Das Feld „A und nicht B“ als 200 − 30 zu berechnen ist falsch: Dann hätten mehr Gäste gegessen als die 80 in Zeile A. Man ergänzt innerhalb der ⟦Zeile A⟧ zu deren Summe 80.'},
 'tafel_wkeit': {
  'einstieg': 'Aus Anzahlen werden Anteile: Hat von 400 Gästen ein Viertel etwas getan, ist die Wahrscheinlichkeit 0,25, dass ein zufällig gewählter Gast es getan hat. Teilt man jedes Feld durch die Gesamtzahl, liest man ⟦Wahrscheinlichkeiten aus der Tafel⟧ ab.',
  'woerter': [['Gesamtzahl', 'die Zahl aller Befragten, unten rechts'],
              ['Randsumme', 'die Summe einer Zeile oder Spalte'],
              ['B̄', '„nicht B“'],
              ['60 → 0,15', '60 Personen entsprechen der Wahrscheinlichkeit 0,15']],
  'bild': {'typ': 'tabelle', 'kopf': ['', 'B (Los gespielt)', 'nicht B', 'Summe'], 'zeilen': [['A (gegessen)', '60 → 0,15', '100 → 0,25', '160 → 0,4'], ['Summe', '', '', '400 → 1']]},
  'schritte': ['Gesamt 400 Gäste. A und B: 60 Gäste, A und nicht B: 100 Gäste.',
               'Jedes Feld durch 400 teilen: P(A ∩ B) = 60 : 400 = 0,15 und P(A ∩ B̄) = 100 : 400 = 0,25.',
               'Die Randsumme der Zeile A: 60 + 100 = 160 Gäste.',
               'P(A) = 160 : 400 = ⟦0,4⟧.'],
  'regel': 'So erhältst du Wahrscheinlichkeiten: Teile jede Anzahl durch die ⟦Gesamtzahl⟧. Die Randsummen ergeben sich wie vorher: ⟦P(A) = P(A ∩ B) + P(A ∩ B̄)⟧.',
  'fehler': 'P(A ∩ B) = 60 : 160 ist falsch, wenn nach der Wahrscheinlichkeit unter ⟦allen⟧ Gästen gefragt ist: Man teilt durch die ⟦Gesamtzahl⟧ 400.'},
 'bedingt': {
  'einstieg': 'Ein Gast erzählt, dass er am Losstand gespielt hat. Wie wahrscheinlich ist es, dass er auch gegessen hat? Jetzt zählen nicht mehr alle 200 Gäste, sondern nur die Spieler. Wissen verkleinert die Gruppe, durch die man teilt. Das heißt ⟦bedingte Wahrscheinlichkeit⟧.',
  'woerter': [['bedingte Wahrscheinlichkeit', 'eine Wahrscheinlichkeit, wenn schon etwas bekannt ist'],
              ['P_B(A)', 'Wahrscheinlichkeit von A, wenn man weiß, dass B eingetreten ist'],
              ['Bedingung', 'das, was man schon weiß – der Buchstabe unten'],
              ['Spalte B', 'nur die Gäste mit Merkmal B']],
  'bild': {'typ': 'tabelle', 'kopf': ['', 'B (Los gespielt)', 'nicht B', 'Summe'], 'zeilen': [['A (gegessen)', '20', '60', '80'], ['nicht A', '30', '90', '120'], ['Summe', '50', '150', '200']]},
  'schritte': ['200 Gäste, davon haben 50 gespielt (B). Von diesen 50 haben 20 auch gegessen (A).',
               'Bekannt ist: Der Gast hat gespielt. Also zählt nur die Spalte B mit 50 Gästen.',
               'Davon haben 20 gegessen.',
               'P_B(A) = 20 : 50 = ⟦0,4⟧.'],
  'regel': 'So berechnest du ⟦P_B(A)⟧, die Wahrscheinlichkeit von A, ⟦wenn man schon weiß⟧, dass B eingetreten ist: ⟦P_B(A) = P(A ∩ B) : P(B)⟧. In der Tafel betrachtest du nur die ⟦Spalte B⟧ und teilst durch ihre Summe.',
  'fehler': 'P_B(A) und P_A(B) zu verwechseln ist falsch. P_B(A) = 20 : 50 = 0,4 (unter allen Spielern). P_A(B) = 20 : 80 = 0,25 (unter allen, die gegessen haben). Die ⟦Bedingung⟧ unten bestimmt, ⟦durch welche Summe⟧ du teilst.'},
 'verstehen': {
  'einstieg': 'Jemand behauptet: „70 % der Gäste haben gegessen, 60 % haben gespielt – das waren bestimmt verschiedene Leute.“ Kann das stimmen? Mit Mengen und ein wenig Rechnen lassen sich solche Behauptungen prüfen. So kann man ⟦Aussagen über Ereignisse prüfen⟧.',
  'woerter': [['unvereinbar', 'A und B haben nichts gemeinsam: A ∩ B = ∅'],
              ['Gegenereignis', 'alles, was nicht zum Ereignis gehört'],
              ['„mindestens eins“', 'eins oder mehr'],
              ['P zwischen 0 und 1', 'keine Wahrscheinlichkeit ist negativ oder größer als 1']],
  'schritte': ['Behauptung: P(A) = 0,7 und P(B) = 0,6, und A und B sind unvereinbar.',
               'Wären sie unvereinbar, wäre P(A ∪ B) = 0,7 + 0,6 = 1,3.',
               'Eine Wahrscheinlichkeit kann nicht größer als 1 sein – mehr als alle Gäste gibt es nicht.',
               'Also stimmt die Behauptung nicht: ⟦A und B müssen sich überschneiden⟧.'],
  'regel': 'So prüfst du Aussagen: Übersetze sie in Mengen und Zahlen. ⟦Unvereinbar⟧ heißt A ∩ B = ∅. Das ⟦Gegenereignis⟧ von „mindestens eins“ ist „keins“. Jede Wahrscheinlichkeit liegt zwischen ⟦0 und 1⟧.',
  'fehler': 'Das Gegenereignis von „mindestens ein Treffer“ ist nicht „mindestens ein Fehlschuss“, sondern ⟦„kein Treffer“⟧. Beides zusammen muss genau alle Möglichkeiten abdecken.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
_KR = [{'m': '_M1', 'r': 3.5}, {'m': '_M2', 'r': 3.5}]
_V = lambda a, b, s=None: {'_M1': [0, 0], '_M2': [4, 0], a: [-2.6, 2.6], b: [6.6, 2.6], **({s: [2, 0]} if s else {})}
_KOPF = ['', 'B (gespielt)', 'nicht B', 'Summe']
UMBAU = {
 'verknuepfen': {
  'einstieg': 'Beim Schulfest ziehst du ein Los von 1 bis 20. Gerade Zahlen gewinnen einen Preis, durch 3 teilbare einen Sonderpreis. Wer gewinnt beides? Dafür ⟦verknüpfst⟧ du Ereignisse.',
  'woerter': [['A ∩ B', '„A und B“: beide Ereignisse treten ein'],
              ['A ∪ B', '„A oder B“: mindestens eines tritt ein'],
              ['Ereignisse', 'Mengen von Ergebnissen, z. B. A = gerade Zahl']],
  'bild': {'typ': 'figur', 'punkte': _V('A: gerade', 'B: durch 3'), 'kreise': _KR},
  'schritte': [{'text': 'A: Die Zahl ist gerade. B: Die Zahl ist durch 3 teilbar.'},
               {'text': 'Beide Preise heißt A ∩ B: die Lose 6, 12 und 18.',
                'bild': {'punkte': _V('A: gerade', 'B: durch 3', 'A ∩ B: 6, 12, 18')}},
               {'text': 'Das sind 3 von 20 Losen: P(A ∩ B) = ⟦0,15⟧.'},
               {'text': 'Mindestens ein Preis hieße dagegen A ∪ B.'}],
  'fehler': 'A ∪ B heißt nicht „beide“. Für A ∪ B reicht schon ein Preis. ∩ heißt und, ∪ heißt oder.',
  'regel': '∩ heißt ⟦und⟧, ∪ heißt ⟦oder⟧ (mindestens eins). P = günstige : mögliche Ergebnisse.'},
 'additionssatz': {
  'einstieg': 'Wie wahrscheinlich ist mindestens ein Preis? Zählst du die Gewinner von A und B zusammen, zählst du die Doppelgewinner zweimal. Das korrigiert der ⟦Additionssatz⟧.',
  'woerter': [['Additionssatz', 'P(A ∪ B) = P(A) + P(B) − P(A ∩ B)'],
              ['Schnittmenge', 'der Teil, der zu A und zu B gehört']],
  'bild': {'typ': 'figur', 'punkte': _V('A: 0,5', 'B: 0,3', 'beide: 0,1'), 'kreise': _KR},
  'schritte': [{'text': 'P(A) = 0,5 und P(B) = 0,3. Die Schnittmenge hat P(A ∩ B) = 0,1.'},
               {'text': '0,5 + 0,3 = 0,8 zählt die Schnittmenge doppelt.'},
               {'text': 'Einmal abziehen: P(A ∪ B) = 0,8 − 0,1 = ⟦0,7⟧.'}],
  'fehler': 'P(A ∪ B) = 0,5 + 0,3 = 0,8 ist falsch. Die Doppelgewinner wurden zweimal gezählt.',
  'regel': '⟦P(A ∪ B) = P(A) + P(B) − P(A ∩ B)⟧. Ohne gemeinsame Ergebnisse fällt der letzte Teil weg.'},
 'vierfeld': {
  'einstieg': 'Nach dem Fest werden 200 Gäste befragt: gegessen oder nicht, gespielt oder nicht. Jeder Gast passt in genau ein Feld der ⟦Vierfeldertafel⟧.',
  'woerter': [['Vierfeldertafel', 'eine Tabelle mit zwei Merkmalen, je ja oder nein'],
              ['Zeilensumme', 'die Summe einer Zeile, ganz rechts']],
  'bild': {'typ': 'tabelle', 'kopf': _KOPF, 'zeilen': [['A (gegessen)', '30', '?', '80'], ['nicht A', '', '', '?'], ['Summe', '', '', '200']]},
  'schritte': [{'text': '200 Gäste, 80 haben gegessen, davon 30 auch gespielt.'},
               {'text': 'Die Zeilensumme von A ist 80. Rest: 80 − 30 = ⟦50⟧.',
                'bild': {'zeilen': [['A (gegessen)', '30', '50', '80'], ['nicht A', '', '', '?'], ['Summe', '', '', '200']]}},
               {'text': 'Nicht gegessen haben 200 − 80 = 120 Gäste.',
                'bild': {'zeilen': [['A (gegessen)', '30', '50', '80'], ['nicht A', '', '', '120'], ['Summe', '', '', '200']]}}],
  'fehler': '„A und nicht B“ ist nicht 200 − 30. Dann hätten mehr gegessen als die 80 in der Zeile.',
  'fehler_bild': {'zeilen': [['A (gegessen)', '30', '170?', '80'], ['nicht A', '', '', '?'], ['Summe', '', '', '200']]},
  'regel': 'Jede Zeile und Spalte muss ihre ⟦Summe⟧ ergeben. Fehlendes ist Summe minus Bekanntes.'},
 'tafel_wkeit': {
  'einstieg': 'Aus Anzahlen werden Anteile. Teilst du jedes Feld durch die Gesamtzahl, liest du ⟦Wahrscheinlichkeiten⟧ ab.',
  'woerter': [['Gesamtzahl', 'alle Befragten, unten rechts'],
              ['Randsumme', 'die Summe einer Zeile oder Spalte']],
  'bild': {'typ': 'tabelle', 'kopf': _KOPF, 'zeilen': [['A (gegessen)', '60', '100', '160'], ['Summe', '', '', '400']]},
  'schritte': [{'text': '400 Gäste: 60 haben gegessen und gespielt, 100 nur gegessen.'},
               {'text': 'Durch die Gesamtzahl teilen: 60 : 400 = 0,15 und 100 : 400 = 0,25.',
                'bild': {'zeilen': [['A (gegessen)', '60 → 0,15', '100 → 0,25', '160'], ['Summe', '', '', '400 → 1']]}},
               {'text': 'Randsumme der Zeile: 160 : 400 = ⟦0,4⟧ = P(A).',
                'bild': {'zeilen': [['A (gegessen)', '60 → 0,15', '100 → 0,25', '160 → 0,4'], ['Summe', '', '', '400 → 1']]}}],
  'fehler': 'P(A ∩ B) ist nicht 60 : 160. Gefragt ist unter allen Gästen, also durch 400 teilen.',
  'regel': 'Teile jedes Feld durch die ⟦Gesamtzahl⟧. P(A) ist dann die Randsumme der Zeile.'},
 'bedingt': {
  'einstieg': 'Ein Gast erzählt, dass er gespielt hat. Wie wahrscheinlich hat er auch gegessen? Jetzt zählen nur die Spieler. Das ist eine ⟦bedingte Wahrscheinlichkeit⟧.',
  'woerter': [['bedingte Wahrscheinlichkeit', 'eine Wahrscheinlichkeit, wenn schon etwas bekannt ist'],
              ['P_B(A)', 'Wahrscheinlichkeit von A, wenn B schon eingetreten ist']],
  'bild': {'typ': 'tabelle', 'kopf': _KOPF, 'zeilen': [['A (gegessen)', '20', '60', '80'], ['nicht A', '30', '90', '120'], ['Summe', '50', '150', '200']]},
  'schritte': [{'text': 'Bekannt: Der Gast hat gespielt. Es zählt nur die Spalte B.',
                'bild': {'kopf': ['', 'B: nur diese Spalte', 'nicht B', 'Summe']}},
               {'text': 'In Spalte B sind 50 Gäste, davon haben 20 gegessen.'},
               {'text': 'P_B(A) = 20 : 50 = ⟦0,4⟧.'}],
  'fehler': 'P_B(A) und P_A(B) nicht verwechseln. 20 : 80 = 0,25 gilt unter allen, die gegessen haben.',
  'regel': 'Bei ⟦P_B(A)⟧ nur in der Gruppe B zählen. Es gilt P_B(A) = P(A ∩ B) : P(B).'},
 'verstehen': {
  'einstieg': 'Jemand sagt: 70 % haben gegessen, 60 % gespielt, und das waren verschiedene Leute. Kann das stimmen? Mit Zahlen ⟦prüfst du solche Aussagen⟧.',
  'woerter': [['unvereinbar', 'A und B haben kein gemeinsames Ergebnis']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 1.4, 'abschnitte': 7, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'Behauptung: P(A) = 0,7, P(B) = 0,6, A und B sind unvereinbar.'},
               {'text': 'Unvereinbar hieße: P(A ∪ B) = 0,7 + 0,6 = 1,3.',
                'bild': {'boegen': [{'von': 0, 'bis': 0.7, 'name': 'gegessen'}, {'von': 0.7, 'bis': 1.3, 'name': 'gespielt'}]}},
               {'text': 'Mehr als alle Gäste gibt es nicht: 1,3 ist größer als 1.', 'bild': {'punkte': [{'wert': 1, 'name': 'alle'}]}},
               {'text': 'Also ⟦überschneiden sich A und B⟧. Die Behauptung ist falsch.'}],
  'fehler': 'Das Gegenteil von „mindestens ein Treffer“ ist nicht „mindestens ein Fehlschuss“, sondern „kein Treffer“.',
  'regel': 'Wahrscheinlichkeiten liegen ⟦zwischen 0 und 1⟧. Unvereinbar heißt: keine gemeinsamen Ergebnisse.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def g_verknuepfen(s):
    N = R.choice([20, 25, 50, 100]) if s > 1 else 20
    (ta, fa), (tb, fb) = R.sample(EREIG, 2)
    om = range(1, N + 1)
    A = [k for k in om if fa(k)]
    B = [k for k in om if fb(k)]
    art = R.choice({1: ['schnitt', 'gegen', 'wort'], 2: ['schnitt', 'vereinigung', 'symbol', 'symbol'], 3: ['ohne', 'weder', 'anzahl']}[s])
    vor = f'Aus den Zahlen 1 bis {N} wird zufällig eine gezogen. A: „Die Zahl ist {ta}.“ B: „Die Zahl ist {tb}.“'
    if art == 'wort':
        r = f'Die Zahl ist {ta} oder {tb} (oder beides).'
        return auswahl(vor + ' Was bedeutet das Ereignis A ∪ B?', r,
                       [f'Die Zahl ist {ta} und {tb}.', f'Die Zahl ist weder {ta} noch {tb}.', f'Die Zahl ist {ta}, aber nicht {tb}.'],
                       'A ∪ B: mindestens eines der Ereignisse tritt ein („oder“ im einschließenden Sinn).', '∪ steht für „oder“, ∩ für „und“.')
    if art == 'symbol':
        sz, ma, mb = R.choice(SZEN)
        varianten = [(f'{ma} und {mb}', 'A ∩ B'), (f'{ma}, aber nicht: {mb}', 'A ∩ B̄'), (f'nicht: {ma}, aber: {mb}', 'Ā ∩ B'),
                     (f'weder „{ma}“ noch „{mb}“', 'Ā ∩ B̄'), (f'mindestens eines von beiden', 'A ∪ B')]
        wort, r = R.choice(varianten)
        return auswahl(f'Untersucht werden {sz}. A: „{ma}“, B: „{mb}“. Wie schreibt man das Ereignis „{wort}“?', r,
                       ['A ∩ B', 'A ∪ B', 'Ā ∩ B', 'A ∩ B̄', 'Ā ∩ B̄', 'Ā ∪ B̄'],
                       f'Der Strich bedeutet „nicht“, ∩ „und“, ∪ „oder“. „{wort}“ ist {r}.',
                       'Übersetze Wort für Wort: „nicht“ = Strich, „und“ = ∩, „oder“ = ∪.')
    if art == 'schnitt':
        M, name = [k for k in A if k in B], 'A ∩ B'
    elif art == 'vereinigung':
        M, name = sorted(set(A) | set(B)), 'A ∪ B'
    elif art == 'gegen':
        vor = f'Aus den Zahlen 1 bis {N} wird zufällig eine gezogen. A: „Die Zahl ist {ta}.“'
        M, name = [k for k in om if k not in A], 'Ā („nicht A“)'
    elif art == 'ohne':
        M, name = [k for k in A if k not in B], 'A ∩ B̄ („A, aber nicht B“)'
    elif art == 'weder':
        M, name = [k for k in om if k not in A and k not in B], 'Ā ∩ B̄ („weder A noch B“)'
    else:
        wahl = R.choice(['A ∩ B', 'A ∩ B̄', 'Ā ∩ B'])
        M = {'A ∩ B': [k for k in A if k in B], 'A ∩ B̄': [k for k in A if k not in B], 'Ā ∩ B': [k for k in B if k not in A]}[wahl]
        if not M or len(M) > 15: return None
        return luecken(vor + f' Wie viele Zahlen liegen in {wahl}?', 'Anzahl: □', 'Anzahl der Zahlen', [len(M)],
                       f'{wahl}: {", ".join(map(str, M))} – das sind {len(M)} Zahlen.', 'Schreibe die passenden Zahlen auf und zähle.', c=[str(len(M))])
    if not M or len(M) == N: return None
    p = Fr(len(M), N)
    zeig = ', '.join(map(str, M)) if len(M) <= 12 else f'{len(M)} Zahlen'
    return zahl(vor + f' Berechne P({name}) als Dezimalzahl.', f'{name.split(" (")[0]}: {zeig}. P = {len(M)} : {N} = {dz(p)}.',
                {'schnitt': 'Welche Zahlen erfüllen beide Bedingungen?', 'vereinigung': 'Zähle alle, die mindestens eine Bedingung erfüllen – keine doppelt.',
                 'gegen': 'Gegenereignis: P(Ā) = 1 − P(A).', 'ohne': 'Nimm die Zahlen aus A und streiche die, die auch in B liegen.',
                 'weder': 'Zähle die Zahlen, die keine der beiden Bedingungen erfüllen.'}[art],
                p, f'{len(M)} / {N}')


def g_vierfeld(s):
    N = R.choice([100, 120, 150, 200, 250, 300, 400, 500])
    aa, ab, ba, bb = zufalls_tafel(N)
    szen, ma, mb = R.choice(SZEN)
    A_, B_ = aa + ab, aa + ba
    vor = f'Untersucht werden {dz(N)} {szen}. A: „{ma}“, B: „{mb}“.'
    W = {'aa': aa, 'ab': ab, 'ba': ba, 'bb': bb, 'A': A_, 'nA': N - A_, 'B': B_, 'nB': N - B_, 'N': N}
    NAME = {'aa': 'A und B', 'ab': 'A und nicht B', 'ba': 'nicht A und B', 'bb': 'nicht A und nicht B', 'A': 'Summe A', 'nA': 'Summe nicht A',
            'B': 'Summe B', 'nB': 'Summe nicht B'}
    if s == 1:
        frage, zeige, w = R.choice([('ab', {'aa', 'A'}, f'Zeile A: {dz(A_)} − {dz(aa)} = {dz(ab)}.'),
                                    ('ba', {'aa', 'B'}, f'Spalte B: {dz(B_)} − {dz(aa)} = {dz(ba)}.'),
                                    ('nA', {'A', 'N'}, f'Gesamt − A: {dz(N)} − {dz(A_)} = {dz(N - A_)}.'),
                                    ('aa', {'ab', 'A'}, f'Zeile A: {dz(A_)} − {dz(ab)} = {dz(aa)}.')])
        return bild(zahl(vor + f' Ergänze das Feld „?“ ({NAME[frage]}).', w, 'Ergänze innerhalb einer Zeile oder Spalte zu ihrer Summe.', W[frage],
                         {'ab': f'{A_} - {aa}', 'ba': f'{B_} - {aa}', 'nA': f'{N} - {A_}', 'aa': f'{A_} - {ab}'}[frage]),
                    tafel(aa, ab, ba, bb, zeige | {'N'}, frage))
    if s == 2:
        if R.random() < 0.5:
            return bild(zahl(vor + f' Ergänze das Feld „?“ (weder A noch B).',
                             f'Nicht A: {dz(N)} − {dz(A_)} = {dz(N - A_)}; nicht A und B: {dz(B_)} − {dz(aa)} = {dz(ba)}; weder noch: {dz(N - A_)} − {dz(ba)} = {dz(bb)}.',
                             'Fülle die Tafel Schritt für Schritt: erst Randsummen, dann die inneren Felder.', bb, f'{N} - {A_} - ({B_} - {aa})'),
                        tafel(aa, ab, ba, bb, {'aa', 'A', 'B', 'N'}, 'bb'))
        return zahl(vor + f' {dz(A_)} haben A, {dz(B_)} haben B, {dz(aa)} haben beides. Wie viele haben weder A noch B?',
                    f'Nicht A: {dz(N - A_)}; davon mit B: {dz(B_)} − {dz(aa)} = {dz(ba)}; weder noch: {dz(N - A_)} − {dz(ba)} = {dz(bb)}.',
                    'Lege eine Vierfeldertafel an: erst Randsummen, dann die inneren Felder.', bb, f'{N} - {A_} - ({B_} - {aa})')
    typ = R.random()
    if typ < 0.35:
        falsch = R.choice(['nA', 'nB'])
        d = R.choice([-10, -5, 5, 10])
        if W[falsch] + d <= 0: return None
        t = tafel(aa, ab, ba, bb, set(W))
        zi, sp = (1, 3) if falsch == 'nA' else (2, 2)
        t['zeilen'][zi][sp] = dz(W[falsch] + d)
        r = f'Die {"Zeilensumme „nicht A“" if falsch == "nA" else "Spaltensumme „nicht B“"} muss {dz(W[falsch])} sein.'
        return bild(auswahl(vor + ' In der Tafel ist genau eine Summe falsch. Welche?', r,
                            [f'Die Zeilensumme „A“ muss {dz(A_ + 10)} sein.', f'Die Spaltensumme „B“ muss {dz(B_ - 10)} sein.',
                             f'Die Gesamtzahl muss {dz(N + d)} sein.', 'Die Zeilensumme „nicht A“ muss ' + dz(W['nA'] + 5) + ' sein.' if falsch == 'nB' else 'Die Spaltensumme „nicht B“ muss ' + dz(W['nB'] + 5) + ' sein.'],
                            f'Prüfe jede Zeile und Spalte: {dz(ba)} + {dz(bb)} = {dz(W["nA"])} (nicht A), {dz(ab)} + {dz(bb)} = {dz(W["nB"])} (nicht B).',
                            'Addiere die inneren Felder jeder Zeile und Spalte und vergleiche mit der Summe.'), t)
    if typ < 0.65:
        return bild(zahl(vor + ' Ergänze das Feld „?“.',
                         f'Gesamt − die drei anderen inneren Felder: {dz(N)} − {dz(ab)} − {dz(ba)} − {dz(bb)} = {dz(aa)}.', 'Die vier inneren Felder ergeben zusammen die Gesamtzahl.',
                         aa, f'{N} - {ab} - {ba} - {bb}'), tafel(aa, ab, ba, bb, {'ab', 'ba', 'bb', 'N'}, 'aa'))
    proz = R.choice([20, 25, 30, 40, 45, 50, 60, 70, 75, Fr(125, 10), Fr(375, 10)])
    A2 = N * Fr(proz) / 100
    if A2.denominator != 1 or A2 <= aa: return None
    A2 = int(A2)
    return zahl(vor + f' {dz(proz)} % haben A. Unter denen mit A haben {dz(aa)} auch B. Wie viele haben A, aber nicht B?',
                f'A: {dz(proz)} % von {dz(N)} = {dz(A2)}; A ohne B: {dz(A2)} − {dz(aa)} = {dz(A2 - aa)}.', 'Rechne zuerst den Prozentsatz in eine Anzahl um.', A2 - aa,
                f'{N} * {cf(Fr(proz) / 100)} - {aa}')


def g_tafel_wkeit(s):
    if s == 2 and R.random() < 0.35:
        pa = Fr(R.randint(2, 7), 10)
        pab = Fr(R.randint(1, int(pa * 100) - 1), 100)
        pb = Fr(R.randint(int(pab * 100) + 1, 90), 100)
        if pa + pb - pab >= 1: return None
        aa, ab, ba = pab, pa - pab, pb - pab
        bb = 1 - aa - ab - ba
        frage, zeige, w, c = R.choice([
            ('ab', {'aa', 'A'}, f'P(A ∩ B̄) = P(A) − P(A ∩ B) = {dz(pa)} − {dz(pab)} = {dz(ab)}.', f'{cf(pa)} - {cf(pab)}'),
            ('bb', {'ab', 'ba', 'aa', 'N'}, f'P(Ā ∩ B̄) = 1 − {dz(aa)} − {dz(ab)} − {dz(ba)} = {dz(bb)}.', f'1 - {cf(aa)} - {cf(ab)} - {cf(ba)}'),
            ('ba', {'aa', 'B'}, f'P(Ā ∩ B) = P(B) − P(A ∩ B) = {dz(pb)} − {dz(pab)} = {dz(ba)}.', f'{cf(pb)} - {cf(pab)}')])
        return bild(zahl('Die Tafel enthält Wahrscheinlichkeiten. Berechne den Wert im Feld „?“.', w,
                         'Auch mit Wahrscheinlichkeiten gilt: Innere Felder ergeben die Randsumme, alles zusammen 1.',
                         {'ab': ab, 'bb': bb, 'ba': ba}[frage], c), tafel(aa, ab, ba, bb, zeige | {'N'}, frage))
    N = R.choice([100, 200, 250, 400, 500, 1000])
    aa, ab, ba, bb = zufalls_tafel(N)
    sz, ma, mb = R.choice(SZEN)
    ein, ka, kna, kb, knb = SZEN_W[sz]
    frage = R.choice({1: ['ab', 'aa', 'bb'], 2: ['A', 'B', 'nA'], 3: ['vereinigung', 'genau', 'nAnB']}[s])
    T = {'aa': (aa, f'„{ma}“ und „{mb}“', f'{dz(aa)} : {dz(N)}'),
         'ab': (ab, f'„{ma}“, aber nicht „{mb}“', f'{dz(ab)} : {dz(N)}'),
         'bb': (bb, f'weder „{ma}“ noch „{mb}“', f'{dz(bb)} : {dz(N)}'),
         'A': (aa + ab, f'„{ma}“', f'({dz(aa)} + {dz(ab)}) : {dz(N)}'),
         'B': (aa + ba, f'„{mb}“', f'({dz(aa)} + {dz(ba)}) : {dz(N)}'),
         'nA': (ba + bb, f'nicht „{ma}“', f'({dz(ba)} + {dz(bb)}) : {dz(N)}'),
         'vereinigung': (aa + ab + ba, f'„{ma}“ oder „{mb}“ (mindestens eines)', f'({dz(aa)} + {dz(ab)} + {dz(ba)}) : {dz(N)}'),
         'genau': (ab + ba, f'genau eines von beiden', f'({dz(ab)} + {dz(ba)}) : {dz(N)}'),
         'nAnB': (N - bb, f'mindestens eines von beiden', f'1 − {dz(bb)} : {dz(N)}')}
    z, name, w = T[frage]
    p = Fr(z, N)
    return bild(zahl(f'Die Tafel zeigt {dz(N)} {sz}. A: „{ma}“, B: „{mb}“. {ein[0].upper() + ein[1:]} wird zufällig ausgewählt. Mit welcher Wahrscheinlichkeit gilt: {name}? Gib das Ergebnis als Dezimalzahl an.',
                     f'P = {w} = {dz(p)}.', 'Welche Felder gehören zum Ereignis? Teile ihre Summe durch die Gesamtzahl.', p, f'{z} / {N}'),
                tafel(aa, ab, ba, bb, {'aa', 'ab', 'ba', 'bb', 'A', 'nA', 'B', 'nB', 'N'}, kopfA=('A', 'nicht A'), kopfB=('B', 'nicht B')))


def g_additionssatz(s):
    pa, pb = Fr(R.randint(2, 7), 10), Fr(R.randint(2, 7), 10)
    pab = Fr(R.randint(1, min(int(pa * 10), int(pb * 10)) * 10 - 1), 100) if s > 1 else Fr(R.randint(1, min(int(pa * 10), int(pb * 10)) - 1 or 1), 10)
    if pab <= 0 or pab >= min(pa, pb) or pa + pb - pab > 1: return None
    pu = pa + pb - pab
    if s == 1:
        return zahl(f'Es gilt P(A) = {dz(pa)}, P(B) = {dz(pb)} und P(A ∩ B) = {dz(pab)}. Berechne P(A ∪ B).',
                    f'P(A ∪ B) = {dz(pa)} + {dz(pb)} − {dz(pab)} = {dz(pu)}.', 'Additionssatz: die Schnittmenge einmal abziehen.', pu,
                    f'{cf(pa)} + {cf(pb)} - {cf(pab)}')
    if s == 2:
        if R.random() < 0.5:
            return zahl(f'Es gilt P(A) = {dz(pa)}, P(B) = {dz(pb)} und P(A ∪ B) = {dz(pu)}. Berechne P(A ∩ B).',
                        f'P(A ∩ B) = P(A) + P(B) − P(A ∪ B) = {dz(pa)} + {dz(pb)} − {dz(pu)} = {dz(pab)}.', 'Stelle den Additionssatz nach P(A ∩ B) um.', pab,
                        f'{cf(pa)} + {cf(pb)} - {cf(pu)}')
        return zahl(f'Es gilt P(A) = {dz(pa)}, P(B) = {dz(pb)} und P(A ∩ B) = {dz(pab)}. Mit welcher Wahrscheinlichkeit tritt keines der beiden Ereignisse ein?',
                    f'P(A ∪ B) = {dz(pu)}; keines: 1 − {dz(pu)} = {dz(1 - pu)}.', '„Keines“ ist das Gegenereignis von A ∪ B.', 1 - pu,
                    f'1 - ({cf(pa)} + {cf(pb)} - {cf(pab)})')
    if R.random() < 0.5:
        if R.random() < 0.5:
            i_, sp, bd = R.choice([(40, 50, 15), (30, 45, 10), (35, 60, 20), (25, 40, 5), (50, 55, 25), (45, 30, 15)])
            k = 100 - (i_ + sp - bd)
            return zahl(f'In einer Klasse spielen {i_} % ein Instrument, {sp} % machen Sport im Verein und {bd} % beides. Wie viel Prozent machen keins von beiden?',
                        f'Instrument oder Sport: {i_} % + {sp} % − {bd} % = {i_ + sp - bd} %. Keins: 100 % − {i_ + sp - bd} % = {k} %.',
                        'Erst P(A ∪ B) mit dem Additionssatz, dann das Gegenereignis.', k, f'100 - ({i_} + {sp} - {bd})', einheit='%')
        pr, pg, prg = R.choice([(Fr(3, 10), Fr(1, 2), Fr(1, 10)), (Fr(2, 5), Fr(1, 2), Fr(1, 5)), (Fr(1, 4), Fr(1, 2), Fr(1, 8)), (Fr(3, 10), Fr(2, 5), Fr(1, 10))])
        return zahl(f'Bei einem Glücksrad ist P(rot) = {dz(pr)}, P(Zahl gerade) = {dz(pg)} und P(rot und gerade) = {dz(prg)}. Man gewinnt bei „rot oder gerade“. Mit welcher Wahrscheinlichkeit gewinnt man?',
                    f'P = {dz(pr)} + {dz(pg)} − {dz(prg)} = {dz(pr + pg - prg)}.', 'Additionssatz: „rot und gerade“ ist in beiden enthalten.', pr + pg - prg,
                    f'{cf(pr)} + {cf(pg)} - {cf(prg)}')
    N = R.choice([20, 25, 50])
    (ta, fa), (tb, fb) = R.sample(EREIG, 2)
    A = [k for k in range(1, N + 1) if fa(k)]
    B = [k for k in range(1, N + 1) if fb(k)]
    AB = [k for k in A if k in B]
    if not AB: return None
    U = len(A) + len(B) - len(AB)
    return zahl(f'Aus 1 bis {N} wird zufällig eine Zahl gezogen. A: „{ta}“, B: „{tb}“. Berechne P(A ∪ B) mit dem Additionssatz als Dezimalzahl.',
                f'P(A) = {len(A)}/{N}, P(B) = {len(B)}/{N}, P(A ∩ B) = {len(AB)}/{N} ({", ".join(map(str, AB))}). P(A ∪ B) = {U}/{N} = {dz(Fr(U, N))}.',
                'Bestimme P(A), P(B) und P(A ∩ B) einzeln.', Fr(U, N), f'{len(A)} / {N} + {len(B)} / {N} - {len(AB)} / {N}')


def g_bedingt(s):
    if s == 3:
        typ = R.random()
        if typ < 0.4:
            if R.random() < 0.5:
                n, br_, bm, m = R.choice([(200, 50, 20, 90), (300, 60, 24, 150), (100, 30, 12, 40), (250, 50, 15, 120)])
                return auswahl(f'Von {n} Schülerinnen und Schülern tragen {br_} eine Brille; {bm} davon sind Mädchen. Insgesamt sind es {m} Mädchen. Was ist P_Mädchen(Brille), also die Wahrscheinlichkeit für eine Brille, wenn es ein Mädchen ist?',
                               f'{bm}/{m}', [f'{bm}/{br_}', f'{bm}/{n}', f'{br_}/{m}'],
                               f'Bedingung: Mädchen ({m}). Davon tragen {bm} eine Brille: {bm}/{m}. ({bm}/{br_} wäre P_Brille(Mädchen).)',
                               'Durch welche Anzahl teilst du? Die Bedingung bestimmt die Gesamtheit.')
            k, pk, g, pg = R.choice([(20, 18, 180, 9), (10, 9, 190, 19), (50, 45, 950, 19), (40, 36, 160, 12)])
            pos = pk + pg
            return auswahl(f'Ein Test zeigt bei {pk} von {k} Kranken und bei {pg} von {g} Gesunden ein positives Ergebnis. Wie groß ist P_positiv(krank)?',
                           f'{pk}/{pos}', [f'{pk}/{k}', f'{pk}/{k + g}', f'{pg}/{pos}'],
                           f'Bedingung: positiv – das sind {pk} + {pg} = {pos}. Davon krank: {pk}. P = {pk}/{pos}. ({pk}/{k} ist P_krank(positiv) – die Verwechslung ist der typische Fehler.)',
                           'Zähle zuerst alle positiven Ergebnisse.')
        pa = Fr(R.choice([2, 3, 4, 5, 6]), 10)
        pba = Fr(R.choice([1, 2, 3, 4]), 4) if R.random() < 0.5 else Fr(R.choice([1, 2, 3, 4]), 5)
        pbna = Fr(R.choice([1, 2, 3]), 4) if R.random() < 0.5 else Fr(R.choice([1, 2]), 5)
        pb = pa * pba + (1 - pa) * pbna
        g = {'typ': 'baum', 'aeste': [{'text': 'A', 'p': br(pa), 'aeste': [{'text': 'B', 'p': br(pba)}, {'text': 'B̄', 'p': br(1 - pba)}]},
                                      {'text': 'Ā', 'p': br(1 - pa), 'aeste': [{'text': 'B', 'p': br(pbna)}, {'text': 'B̄', 'p': br(1 - pbna)}]}]}
        if typ < 0.7:
            if not endlich(pb): return None
            return bild(zahl('Berechne mit dem Baumdiagramm P(B) als Dezimalzahl.',
                             f'P(B) = {br(pa)} · {br(pba)} + {br(1 - pa)} · {br(pbna)} = {dz(pa * pba)} + {dz((1 - pa) * pbna)} = {dz(pb)}.',
                             'Addiere die Pfadwahrscheinlichkeiten aller Pfade, die bei B enden.', pb,
                             f'{cf(pa)} * {cf(pba)} + (1 - {cf(pa)}) * {cf(pbna)}' if endlich(pba) and endlich(pbna) else f'{pb.numerator} / {pb.denominator}'), g)
        q = pa * pba / pb
        return bild(luecken('Berechne mit dem Baumdiagramm P_B(A) als gekürzten Bruch.', '□/□', 'Zähler / Nenner', [q.numerator, q.denominator],
                            f'P(A ∩ B) = {br(pa)} · {br(pba)} = {br(pa * pba)}; P(B) = {br(pa * pba)} + {br((1 - pa) * pbna)} = {br(pb)}. P_B(A) = {br(pa * pba)} : {br(pb)} = {br(q)}.',
                            'P_B(A) = P(A ∩ B) : P(B). Bestimme beide aus dem Baum.', c=[str(q.numerator), str(q.denominator)]), g)
    for _ in range(50):
        N = R.choice([100, 200, 400, 500])
        aa, ab, ba, bb = zufalls_tafel(N)
        B_ = aa + ba
        A_ = aa + ab
        kurz = lambda q: endlich(q) and 1000 % q.denominator == 0  # noqa: E731
        if kurz(Fr(aa, B_)) and kurz(Fr(aa, A_)): break
    else:
        return None
    if s == 1:
        return bild(zahl('Berechne P_B(A), also die Wahrscheinlichkeit für A unter der Bedingung B, als Dezimalzahl.',
                         f'Nur Spalte B betrachten: {dz(B_)} Fälle, davon {dz(aa)} mit A. P_B(A) = {dz(aa)} : {dz(B_)} = {dz(Fr(aa, B_))}.',
                         'Teile durch die Anzahl in der Bedingung B, nicht durch alle.', Fr(aa, B_), f'{aa} / ({aa} + {ba})'),
                    tafel(aa, ab, ba, bb, {'aa', 'ab', 'ba', 'bb', 'A', 'nA', 'B', 'nB', 'N'}))
    sz, ma, mb = R.choice(SZEN)
    ein = SZEN_W[sz][0]
    return bild(zahl(f'Die Tafel zeigt {dz(N)} {sz}. A: „{ma}“, B: „{mb}“. {ein[0].upper() + ein[1:]} mit Merkmal A wird zufällig ausgewählt. Mit welcher Wahrscheinlichkeit gilt dann auch B? Gib P_A(B) als Dezimalzahl an.',
                     f'Bedingung A: Nur Zeile A mit {dz(A_)} Fällen, davon {dz(aa)} mit B. P_A(B) = {dz(aa)} : {dz(A_)} = {dz(Fr(aa, A_))}.',
                     'Die Bedingung steht unten: hier A. Teile durch die Zeilensumme A.', Fr(aa, A_), f'{aa} / ({aa} + {ab})'),
                tafel(aa, ab, ba, bb, {'aa', 'ab', 'ba', 'bb', 'A', 'nA', 'B', 'nB', 'N'}))


def g_verstehen(s):
    typ = R.choice({1: 'ab', 2: 'bcd', 3: 'cdeff'}[s])
    if typ == 'f':
        pa, pb = Fr(R.randint(4, 8), 10), Fr(R.randint(3, 7), 10)
        if R.random() < 0.5:
            lo, hi = max(Fr(0), pa + pb - 1), min(pa, pb)
            if hi - lo < Fr(2, 10): return None
            r = (lo + hi) / 2
            r = Fr(round(r * 20), 20)
            if not (lo < r < hi): return None
            falsch = [dz(max(lo - Fr(5, 100), Fr(1, 100))) if lo > 0 else dz(hi + Fr(5, 100)), dz(hi + Fr(5, 100)), dz(pa + pb)]
            return auswahl(f'P(A) = {dz(pa)}, P(B) = {dz(pb)}. Welcher Wert ist für P(A ∩ B) möglich?', dz(r), falsch,
                           f'P(A ∩ B) ist höchstens so groß wie die kleinere der beiden ({dz(hi)}) und mindestens P(A) + P(B) − 1 = {dz(lo)}, weil P(A ∪ B) ≤ 1.',
                           'Kann die Schnittmenge größer sein als A oder B? Wie groß muss sie mindestens sein?')
        lo, hi = max(pa, pb), min(Fr(1), pa + pb)
        if hi - lo < Fr(2, 10): return None
        r = Fr(round((lo + hi) / 2 * 20), 20)
        if not (lo < r < hi): return None
        return auswahl(f'P(A) = {dz(pa)}, P(B) = {dz(pb)}. Welcher Wert ist für P(A ∪ B) möglich?', dz(r),
                       [dz(min(pa, pb) - Fr(1, 10)) if min(pa, pb) > Fr(1, 10) else '0', dz(pa + pb + Fr(1, 10)), dz(lo - Fr(5, 100))],
                       f'P(A ∪ B) ist mindestens so groß wie die größere ({dz(lo)}) und höchstens P(A) + P(B) bzw. 1, also höchstens {dz(hi)}.',
                       'A ∪ B enthält A und B. Wie groß kann es höchstens werden?')
    if typ == 'a':
        pa, pb = Fr(R.randint(1, 5), 10), Fr(R.randint(1, 5), 10)
        return auswahl(f'A und B sind unvereinbar, P(A) = {dz(pa)}, P(B) = {dz(pb)}. Was gilt für P(A ∪ B)?', f'P(A ∪ B) = {dz(pa + pb)}',
                       [f'P(A ∪ B) = {dz(pa * pb)}', f'P(A ∪ B) = {dz(pa + pb - pa * pb)}', 'Das kann man nicht berechnen.'],
                       f'Unvereinbar: A ∩ B = ∅, P(A ∩ B) = 0. Also P(A ∪ B) = {dz(pa)} + {dz(pb)} = {dz(pa + pb)}.', 'Was bedeutet „unvereinbar“ für A ∩ B?')
    if typ == 'b':
        n = R.randint(2, 6)
        ding = R.choice(['Würfelwürfen', 'Münzwürfen', 'Torschüssen', 'Losen'])
        ziel = {'Würfelwürfen': 'eine Sechs', 'Münzwürfen': 'Kopf', 'Torschüssen': 'ein Treffer', 'Losen': 'ein Gewinn'}[ding]
        nicht = {'Würfelwürfen': 'keine Sechs', 'Münzwürfen': 'nicht Kopf', 'Torschüssen': 'kein Treffer', 'Losen': 'kein Gewinn'}[ding]
        return auswahl(f'Bei {n} {ding} ist A: „mindestens einmal {ziel}“. Was ist das Gegenereignis Ā?', f'„kein einziges Mal {ziel}“',
                       [f'„höchstens einmal {ziel}“', f'„genau einmal {ziel}“', f'„mindestens einmal {nicht}“'],
                       'Das Gegenereignis umfasst genau die Ergebnisse, die nicht zu A gehören. Nicht „mindestens einmal“ heißt „keinmal“.',
                       'Welche Ergebnisse gehören nicht zu A?')
    if typ == 'c':
        pa, pb = Fr(R.randint(5, 9), 10), Fr(R.randint(3, 9), 10)
        if pa + pb <= 1: return None
        return auswahl(f'Jemand behauptet: „P(A) = {dz(pa)} und P(B) = {dz(pb)}; A und B können unvereinbar sein.“ Was stimmt?',
                       f'Falsch: Dann wäre P(A ∪ B) = {dz(pa + pb)} > 1. Es gilt P(A ∩ B) ≥ {dz(pa + pb - 1)}.',
                       ['Richtig, das ist möglich.', f'Falsch: P(A ∩ B) = {dz(pa * pb)} muss gelten.', 'Falsch: Wahrscheinlichkeiten kann man nicht addieren.'],
                       f'Bei unvereinbaren Ereignissen addieren sich die Wahrscheinlichkeiten: {dz(pa)} + {dz(pb)} = {dz(pa + pb)} > 1 ist unmöglich.',
                       'Kann eine Wahrscheinlichkeit größer als 1 sein?')
    if typ == 'd':
        N = R.choice([100, 200, 400])
        aa, ab, ba, bb = zufalls_tafel(N)
        if not (endlich(Fr(aa, aa + ba)) and endlich(Fr(aa, aa + ab))) or aa + ba == aa + ab: return None
        return auswahl(f'{tafel_text(aa, ab, ba, bb)} Jemand berechnet P_B(A) = {dz(aa)} : {dz(aa + ab)} = {dz(Fr(aa, aa + ab))}. Was stimmt?',
                       f'Falsch: Das ist P_A(B). Richtig: P_B(A) = {dz(aa)} : {dz(aa + ba)} = {dz(Fr(aa, aa + ba))}.',
                       ['Richtig.', f'Falsch: P_B(A) = {dz(aa)} : {dz(N)} = {dz(Fr(aa, N))}.', f'Falsch: P_B(A) = {dz(aa + ba)} : {dz(N)} = {dz(Fr(aa + ba, N))}.'],
                       f'Bei P_B(A) ist B die Bedingung: Man teilt durch alle Fälle mit B ({dz(aa + ba)}).', 'Wer steht unten als Bedingung?')
    pa, pb = Fr(R.randint(2, 6), 10), Fr(R.randint(2, 6), 10)
    pab = Fr(R.randint(1, 9), 100)
    if pab >= min(pa, pb): return None
    return auswahl(f'P(A) = {dz(pa)}, P(B) = {dz(pb)}, P(A ∩ B) = {dz(pab)}. Jemand rechnet P(A ∪ B) = {dz(pa + pb)}. Was stimmt?',
                   f'Falsch: Die Schnittmenge wurde doppelt gezählt; P(A ∪ B) = {dz(pa + pb - pab)}.',
                   ['Richtig.', f'Falsch: P(A ∪ B) = {dz(pa + pb + pab)}.', f'Falsch: P(A ∪ B) = {dz(pab)}.'],
                   f'Additionssatz: {dz(pa)} + {dz(pb)} − {dz(pab)} = {dz(pa + pb - pab)}.', 'Sind A und B unvereinbar?')


GEN = {'verknuepfen': g_verknuepfen, 'vierfeld': g_vierfeld, 'tafel_wkeit': g_tafel_wkeit, 'additionssatz': g_additionssatz,
       'bedingt': g_bedingt, 'verstehen': g_verstehen}

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9914, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Bayerischer Mathematik-Test 10 (ISB; 2023: Vierfeldertafel
# ergänzen, P(A ∪ B) in Prozent, Mengenausdruck einer Beschreibung zuordnen; 2024: Ereignisse bei nummerierten Kugeln,
# A ∩ B und A ∪ B; 2025: Bedingung für ein Laplace-Experiment), Abschlussprüfung Realschule Bayern Mathematik I
# (2023: Baumdiagramm mit Prozentangaben; 2025: Gegenwahrscheinlichkeit, Anteil aus einer Gleichung), Illustrierende
# Aufgaben Realschule 9 (I) (Behauptung „bestimmt 4-mal Rot“ beurteilen), IQB-Lernaufgabe Grippetest (Vierfeldertafel,
# bedingte Wahrscheinlichkeit). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402
from _kl9 import K as _K  # noqa: E402


def schwer():
    P, Kn, O = 'pruefung', 'knobel', ''
    tab = lambda z: {'typ': 'tabelle', 'kopf': ['', 'B', 'B̄', 'Summe'], 'zeilen': z}
    test = 0.02 * 0.9 / (0.02 * 0.9 + 0.98 * 0.05) * 100
    baum = {'typ': 'baum', 'aeste': [{'text': 'A', 'p': '0,4', 'aeste': [{'text': 'B', 'p': '0,5'}, {'text': 'B̄', 'p': '0,5'}]},
                                     {'text': 'Ā', 'p': '0,6', 'aeste': [{'text': 'B', 'p': '0,25'}, {'text': 'B̄', 'p': '0,75'}]}]}
    return [
        # verknuepfen
        ('verknuepfen', 3, P, zahl('Aus 50 Kugeln mit den Nummern 1 bis 50 wird eine gezogen. A: „Die Nummer ist durch 4 teilbar.“ B: „Die Nummer ist einstellig.“ Wie viele Nummern gehören zu A ∪ B?',
                                   'A: 4, 8, …, 48 (12 Nummern). B: 1 bis 9 (9 Nummern). A ∩ B: 4 und 8 (2 Nummern). A ∪ B: 12 + 9 − 2 = 19.',
                                   'Zähle A und B einzeln. Welche Nummern hast du dabei doppelt gezählt?', 19, '12 + 9 - 2')),
        ('verknuepfen', 3, P, auswahl('S: „Ein Kind spielt Schach.“ M: „Ein Kind macht Musik.“ Welche Beschreibung passt zu (S ∩ M̄) ∪ (S̄ ∩ M)?', 'Das Kind macht genau eines von beidem.',
                                      ['Das Kind macht beides.', 'Das Kind macht mindestens eines von beidem.', 'Das Kind macht keines von beidem.'],
                                      'S ∩ M̄: Schach, aber keine Musik. S̄ ∩ M: Musik, aber kein Schach. Die Vereinigung: genau eines von beiden.',
                                      'Übersetze die beiden Klammern einzeln in Worte.')),
        ('verknuepfen', 3, Kn, zahl('Beim Würfeln ist A = {2; 4; 6} und B = {4; 5; 6}. Wie viele Ergebnisse gehören zu Ā ∪ B̄?',
                                    'Ā ∪ B̄ heißt „nicht A oder nicht B“ – das ist das Gegenteil von „A und B“. A ∩ B = {4; 6}, also Ā ∪ B̄ = {1; 2; 3; 5}: 4 Ergebnisse.',
                                    'Was ist das Gegenteil von „beide treten ein“?', 4, '6 - 2')),
        ('verknuepfen', 3, O, auswahl('In zwei verschiedenen Spielen gilt: A: „Team Rot gewinnt.“ B: „Team Blau gewinnt.“ Was bedeutet Ā ∩ B̄?', 'Weder Team Rot noch Team Blau gewinnt.',
                                      ['Nicht beide Teams gewinnen.', 'Genau ein Team gewinnt.', 'Mindestens ein Team verliert.'],
                                      'Ā ∩ B̄: A tritt nicht ein und B tritt nicht ein. „Mindestens ein Team verliert“ wäre Ā ∪ B̄.', '∩ heißt „und“, der Strich heißt „nicht“.')),
        ('verknuepfen', 2, O, luecken('Beim Würfeln ist A: „gerade Zahl“ und B: „Zahl größer als 3“. Berechne P(A ∩ B) als gekürzten Bruch.', '□/□', 'Zähler und Nenner eintragen', [1, 3],
                                      'A ∩ B = {4; 6}: 2 von 6 Ergebnissen, also 2/6 = 1/3.', 'Welche Zahlen sind gerade und größer als 3?', ['2 // 2', '6 // 2'])),
        ('verknuepfen', 2, O, luecken('Aus den Zahlen 1 bis 20 wird eine gezogen. A: „durch 2 teilbar“, B: „durch 5 teilbar“. Wie viele Zahlen liegen in A ∩ B?', 'Anzahl: □', 'Anzahl eintragen', [2],
                                      'Durch 2 und durch 5 teilbar heißt durch 10 teilbar: 10 und 20.', 'Welche Zahlen sind durch 2 und durch 5 teilbar?', ['20 // 10'])),
        # additionssatz
        ('additionssatz', 3, P, zahl('Von 800 geprüften Fahrrädern haben 120 einen Mangel an der Bremse, 200 einen Mangel am Licht und 60 beide Mängel. Mit welcher Wahrscheinlichkeit hat ein zufällig gewähltes Rad mindestens einen dieser Mängel? Gib sie in Prozent an.',
                                     'P(B ∪ L) = (120 + 200 − 60) : 800 = 260 : 800 = 0,325 = 32,5 %.', '„Mindestens einer“ heißt ∪. Die 60 sind in beiden Zahlen enthalten.', 32.5,
                                     '(120 + 200 - 60) / 800 * 100', einheit='%')),
        ('additionssatz', 3, P, zahl('Es gilt P(A) = 0,45, P(A ∪ B) = 0,7 und P(A ∩ B) = 0,15. Berechne P(B).', 'Additionssatz: 0,7 = 0,45 + P(B) − 0,15 ⇒ P(B) = 0,7 − 0,45 + 0,15 = 0,4.',
                                     'Setze in den Additionssatz ein und löse nach P(B) auf.', 0.4, '0.7 - 0.45 + 0.15')),
        ('additionssatz', 3, Kn, zahl('Es gilt P(A) = 0,6 und P(B) = 0,7. Wie groß ist P(A ∩ B) mindestens?', 'P(A ∪ B) ≤ 1, also P(A ∩ B) = P(A) + P(B) − P(A ∪ B) ≥ 0,6 + 0,7 − 1 = 0,3.',
                                      'P(A ∪ B) kann höchstens 1 sein. Setze das in den Additionssatz ein.', 0.3, '0.6 + 0.7 - 1')),
        ('additionssatz', 3, O, zahl('A und B sind unvereinbar, P(A) = 0,35 und P(B) = 0,25. Berechne P(Ā ∩ B̄).', 'P(A ∪ B) = 0,35 + 0,25 = 0,6 (keine Schnittmenge). „Weder noch“ ist das Gegenteil: 1 − 0,6 = 0,4.',
                                     'Ā ∩ B̄ ist das Gegenereignis von A ∪ B.', 0.4, '1 - (0.35 + 0.25)')),
        ('additionssatz', 2, O, zahl('Es gilt P(A) = 0,4, P(B) = 0,35 und P(A ∩ B) = 0,15. Berechne P(A ∪ B).', 'P(A ∪ B) = 0,4 + 0,35 − 0,15 = 0,6.', 'Additionssatz.', 0.6, '0.4 + 0.35 - 0.15')),
        ('additionssatz', 2, O, luecken('Beim Würfeln ist A: „1 oder 2“ und B: „gerade Zahl“. Berechne P(A ∪ B) als gekürzten Bruch.', '□/□', 'Zähler und Nenner eintragen', [2, 3],
                                        'A ∪ B = {1; 2; 4; 6}: 4 von 6, also 2/3. Mit dem Additionssatz: 2/6 + 3/6 − 1/6 = 4/6.', 'Die 2 gehört zu beiden Ereignissen.', ['4 // 2', '6 // 2'])),
        # vierfeld
        ('vierfeld', 3, P, bild(zahl('Untersucht werden 800 gebrauchte Handys. A: „Akku ist schwach“, B: „Display ist beschädigt“. Ergänze das Feld „?“ (weder schwacher Akku noch beschädigtes Display).',
                                     'Nur A: 100 − 60 = 40. Nur B: 150 − 60 = 90. Weder noch: 800 − 60 − 40 − 90 = 610.', 'Fülle zuerst die Felder, die direkt über Summen folgen.', 610,
                                     '800 - 100 - 150 + 60'), tab([['A', '60', '', '100'], ['Ā', '', '?', ''], ['Summe', '150', '', '800']]))),
        ('vierfeld', 3, P, zahl('Von 400 Befragten sind 35 % Kinder. Von den Kindern essen 60 % gern Fisch, von den Erwachsenen 40 %. Wie viele Befragte essen gern Fisch?',
                                'Kinder: 140, davon 84 mit Fisch. Erwachsene: 260, davon 104. Zusammen 84 + 104 = 188.', 'Erst die Randsummen (Kinder/Erwachsene), dann die Prozente innerhalb jeder Gruppe.',
                                188, '140 * 0.6 + 260 * 0.4')),
        ('vierfeld', 3, Kn, zahl('In einer Vierfeldertafel mit 100 Personen haben 40 das Merkmal A und 30 das Merkmal B. A ∩ B ist doppelt so groß wie Ā ∩ B. Wie groß ist Ā ∩ B̄?',
                                 'Spalte B: (A ∩ B) + (Ā ∩ B) = 30 und A ∩ B = 2 · (Ā ∩ B) ⇒ Ā ∩ B = 10, A ∩ B = 20. Ā hat 60, also Ā ∩ B̄ = 60 − 10 = 50.',
                                 'Teile die Spalte B im Verhältnis 2 : 1 auf.', 50, '60 - 10')),
        ('vierfeld', 3, O, zahl('120 Jugendliche wurden befragt. 45 % haben ein Haustier (A). 50 Jugendliche fahren mit dem Rad (B), 20 davon haben ein Haustier. Wie viele haben weder ein Haustier noch fahren sie Rad?',
                                'A: 54, Ā: 66. Ā ∩ B = 50 − 20 = 30. Ā ∩ B̄ = 66 − 30 = 36.', 'Rechne 45 % von 120 aus und fülle die Tafel Schritt für Schritt.', 36, '120 - 54 - 30')),
        ('vierfeld', 2, O, zahl('In einer Vierfeldertafel ist die Gesamtzahl 200; A hat 80, B hat 70 und A ∩ B hat 30. Wie groß ist Ā ∩ B̄?', 'A ∪ B = 80 + 70 − 30 = 120, also Ā ∩ B̄ = 200 − 120 = 80.',
                                'Erst A ∪ B, dann der Rest.', 80, '200 - (80 + 70 - 30)')),
        ('vierfeld', 2, O, zahl('In einer Vierfeldertafel ist A ∩ B = 12 und A ∩ B̄ = 8. Wie groß ist die Randsumme von A?', 'Zeile A: 12 + 8 = 20.', 'Die Zeile A besteht aus A ∩ B und A ∩ B̄.', 20, '12 + 8')),
        # tafel_wkeit
        ('tafel_wkeit', 3, P, bild(zahl('Die Tafel zeigt 250 Jugendliche. A: „hat einen Hund“, B: „reitet“. Mit welcher Wahrscheinlichkeit hat eine zufällig gewählte Person einen Hund oder reitet? Gib sie in Prozent an.',
                                        'A ∪ B: 20 + 55 + 25 = 100 von 250 = 0,4 = 40 %.', 'Zähle alle Felder, in denen A oder B (oder beides) vorkommt.', 40, '(20 + 55 + 25) / 250 * 100', einheit='%'),
                                   tab([['A', '20', '55', '75'], ['Ā', '25', '150', '175'], ['Summe', '45', '205', '250']]))),
        ('tafel_wkeit', 3, P, bild(zahl('Die Tafel zeigt 200 Jugendliche. A: „hat einen Hund“, B: „reitet“. Eine Person wird zufällig gewählt. Mit welcher Wahrscheinlichkeit hat sie keinen Hund und reitet nicht?',
                                        'Ā ∩ B̄: 104 von 200 = 0,52. Kontrolle über das Gegenereignis: 1 − (12 + 48 + 36) : 200 = 0,52.', 'Gesucht ist ein Innenfeld geteilt durch die Gesamtzahl.', 0.52,
                                        '104 / 200'), tab([['A', '12', '48', '60'], ['Ā', '36', '104', '140'], ['Summe', '48', '152', '200']]))),
        ('tafel_wkeit', 3, Kn, zahl('Es gilt P(A) = 0,4, P(B) = 0,5 und P(Ā ∩ B̄) = 0,3. Berechne P(A ∩ B).', 'P(A ∪ B) = 1 − 0,3 = 0,7. Additionssatz rückwärts: P(A ∩ B) = 0,4 + 0,5 − 0,7 = 0,2.',
                                    '„Weder noch“ ist das Gegenteil von „mindestens eins“.', 0.2, '0.4 + 0.5 - (1 - 0.3)')),
        ('tafel_wkeit', 3, O, zahl('In einer Tafel mit relativen Häufigkeiten gilt P(A ∩ B) = 0,12, P(A) = 0,3 und P(B̄) = 0,6. Berechne P(Ā ∩ B̄).',
                                   'P(A ∩ B̄) = 0,3 − 0,12 = 0,18. Spalte B̄: P(Ā ∩ B̄) = 0,6 − 0,18 = 0,42.', 'Arbeite mit Zeilen- und Spaltensummen wie bei Anzahlen.', 0.42, '0.6 - (0.3 - 0.12)')),
        ('tafel_wkeit', 2, O, zahl('Von 250 Personen gehören 75 zu A ∩ B. Wie groß ist P(A ∩ B)?', 'P(A ∩ B) = 75 : 250 = 0,3.', 'Durch die Gesamtzahl teilen.', 0.3, '75 / 250')),
        ('tafel_wkeit', 2, O, zahl('In einer Tafel gilt P(A ∩ B) = 0,1 und P(A ∩ B̄) = 0,25. Berechne P(A).', 'P(A) = 0,1 + 0,25 = 0,35 (Zeilensumme).', 'Die Zeile A addieren.', 0.35, '0.1 + 0.25')),
        # bedingt
        ('bedingt', 3, P, zahl('Ein Test erkennt eine Krankheit bei 90 % der Kranken. Bei Gesunden zeigt er in 5 % der Fälle fälschlich „positiv“. 2 % der Bevölkerung sind krank. Wie groß ist die Wahrscheinlichkeit, dass eine positiv getestete Person wirklich krank ist? Gib sie in Prozent auf eine Nachkommastelle an.',
                               'P(krank ∩ pos) = 0,02 · 0,9 = 0,018. P(pos) = 0,018 + 0,98 · 0,05 = 0,067. P_pos(krank) = 0,018 : 0,067 ≈ 26,9 % – viel weniger als 90 %.',
                               'Denke an 10 000 Personen: Wie viele sind krank und positiv, wie viele gesund und positiv?', round(test, 1), f'round({_K(test)}, 1)', einheit='%')),
        ('bedingt', 3, P, bild(zahl('Berechne mit dem Baumdiagramm P(B).', 'Pfadregeln: P(B) = 0,4 · 0,5 + 0,6 · 0,25 = 0,2 + 0,15 = 0,35.',
                                    'Multipliziere entlang der Pfade zu B und addiere die Pfade.', 0.35, '0.4 * 0.5 + 0.6 * 0.25'), baum)),
        ('bedingt', 3, Kn, zahl('Es gilt P(A ∩ B) = 0,12 und P_B(A) = 0,4. Wie groß ist P(B)?', 'P_B(A) = P(A ∩ B) : P(B) ⇒ P(B) = 0,12 : 0,4 = 0,3.', 'Stelle die Formel für P_B(A) nach P(B) um.',
                                0.3, '0.12 / 0.4')),
        ('bedingt', 3, O, zahl('In einer Lostrommel sind 40 Lose, 10 davon gewinnen; 4 der Gewinne sind Hauptgewinne. Du hast schon gesehen, dass dein Los gewinnt. Mit welcher Wahrscheinlichkeit ist es ein Hauptgewinn?',
                               'Bedingung „Gewinn“: Es zählen nur die 10 Gewinnlose, 4 davon Hauptgewinne: 4 : 10 = 0,4.', 'Die Bedingung verkleinert die Grundmenge.', 0.4, '4 / 10')),
        ('bedingt', 2, O, zahl('In der Spalte B einer Vierfeldertafel stehen 60 Personen, 15 davon gehören auch zu A. Berechne P_B(A).', 'P_B(A) = 15 : 60 = 0,25.', 'Nur in der Spalte B zählen.', 0.25, '15 / 60')),
        ('bedingt', 2, O, auswahl('Was bedeutet P_B(A)?', 'die Wahrscheinlichkeit für A, wenn man schon weiß, dass B eingetreten ist',
                                  ['die Wahrscheinlichkeit, dass A und B eintreten', 'die Wahrscheinlichkeit für B, wenn A eingetreten ist', 'die Wahrscheinlichkeit für A oder B'],
                                  'Das tiefgestellte B ist die Bedingung: Man zählt nur in der Gruppe B.', 'Wofür steht der kleine Buchstabe unten?')),
        # verstehen
        ('verstehen', 3, P, auswahl('Ein Glücksrad hat die Felder 1, 2, 3 und 4. Welche zusätzliche Angabe sichert, dass P(1) = 1/4 gilt?', 'Alle vier Felder sind gleich groß.',
                                    ['Das Rad wird sehr oft gedreht.', 'Die Felder sind fortlaufend nummeriert.', 'Die 1 ist schon einmal gekommen.'],
                                    'P = günstige : mögliche Ergebnisse gilt nur, wenn alle Ergebnisse gleich wahrscheinlich sind (Laplace-Experiment) – beim Glücksrad: gleich große Felder.',
                                    'Wann darf man „1 von 4“ rechnen?')),
        ('verstehen', 3, P, auswahl('In einer Urne liegen 2 rote und 3 blaue Kugeln. Jemand sagt: „Bei 10 Ziehungen mit Zurücklegen ziehe ich bestimmt genau 4-mal Rot.“ Was stimmt?',
                                    'Falsch: 4-mal Rot ist nur der Erwartungswert; es kann auch öfter oder seltener kommen.',
                                    ['Richtig, denn 2/5 von 10 sind 4.', 'Richtig, wenn man gut mischt.', 'Falsch: Es kommt bestimmt 5-mal Rot.'],
                                    '10 · 2/5 = 4 ist ein Durchschnittswert für viele Versuchsreihen. Einzelne Reihen weichen ab; erst bei sehr vielen Ziehungen nähert sich der Anteil 0,4.',
                                    'Unterscheide zwischen „zu erwarten“ und „sicher“.')),
        ('verstehen', 3, Kn, auswahl('Es gilt P(A) = 0,6 und P(B) = 0,5. Welche Aussage ist sicher richtig?', 'A und B haben gemeinsame Ergebnisse.',
                                     ['A und B sind unvereinbar.', 'P(A ∪ B) = 1,1', 'P(A ∩ B) = 0,3'],
                                     'Wären A und B unvereinbar, wäre P(A ∪ B) = 1,1 > 1 – unmöglich. Also gilt P(A ∩ B) ≥ 0,1. Wie groß genau, weiß man nicht.',
                                     'Was wäre bei unvereinbaren Ereignissen mit P(A ∪ B)?')),
        ('verstehen', 3, O, auswahl('Welche Angaben sind unmöglich?', 'P(A) = 0,3; P(B) = 0,4; P(A ∩ B) = 0,5',
                                    ['P(A) = 0,3; P(B) = 0,4; P(A ∩ B) = 0,1', 'P(A) = 0,5; P(B) = 0,5; P(A ∩ B) = 0', 'P(A) = 0,8; P(B) = 0,7; P(A ∩ B) = 0,6'],
                                    'A ∩ B ist ein Teil von A, also P(A ∩ B) ≤ P(A) = 0,3. 0,5 ist zu groß. Bei 0,8/0,7/0,6 ist P(A ∪ B) = 0,9 – möglich.',
                                    'Die Schnittmenge kann nicht größer sein als jedes der beiden Ereignisse.')),
        ('verstehen', 2, O, auswahl('Was ist das Gegenereignis zu „mindestens eine Sechs bei zwei Würfen“?', 'keine Sechs', ['genau eine Sechs', 'zwei Sechsen', 'höchstens eine Sechs'],
                                    'Das Gegenteil von „mindestens eine“ ist „keine“.', 'Was bleibt übrig, wenn „mindestens eine“ nicht eintritt?')),
        ('verstehen', 2, O, auswahl('Welcher Wert kann keine Wahrscheinlichkeit sein?', '1,2', ['0', '1', '0,05'], 'Wahrscheinlichkeiten liegen zwischen 0 und 1 (einschließlich).', 'Grenzen 0 und 1.')),
    ]


if __name__ == '__main__':
    d = bauen('stochastik.verknuepft',
          'Ereignisse verknüpfen (und, oder, nicht), Vierfeldertafeln nutzen und Wahrscheinlichkeiten mit dem Additionssatz und als bedingte Wahrscheinlichkeit berechnen.',
          ['A ∩ B: A und B. A ∪ B: A oder B (mindestens eines). Ā: nicht A, P(Ā) = 1 − P(A).', 'Vierfeldertafel: Zeilen- und Spaltensummen.',
           'P(A ∪ B) = P(A) + P(B) − P(A ∩ B).', 'P_B(A) = P(A ∩ B) : P(B).'],
          [('Ereignisse verknüpfen', ['verknuepfen', 'additionssatz']), ('Vierfeldertafel', ['vierfeld', 'tafel_wkeit']),
           ('Bedingte Wahrscheinlichkeit und Verstehen', ['bedingt', 'verstehen'])],
          ETAPPEN, GEN, vertiefung=('bedingt',),
          meiden={'verknuepfen': [], 'additionssatz': ['P(A) = 0,5, P(B) = 0,3 und P(A ∩ B) = 0,1.']},
          offen=['Vierfeldertafeln werden jetzt als Tabelle (f.grafik) gezeigt, das Venn-Diagramm als „figur“ mit zwei Kreisen (die Beschriftung der Schnittmenge ist ein Punkt mit Namen). Reihenfolge der Lernkarten an die Abschnitte angepasst (Additionssatz direkt nach „verknuepfen“).',
                 'Bedingte Wahrscheinlichkeit P_B(A) ist im „umfang“ genannt, im LehrplanPLUS der 9. Klasse aber nicht ausdrücklich; Lernkarte „bedingt“ deshalb als Vertiefung (nicht Pflicht) markiert. Schreibweise P_B(A) im Text (Tiefstellung nicht möglich).',
                 'Ā und B̄ stehen jetzt auch in Aufgaben (Prüfvorschlag „Ereignis in Symbolen“); bitte in der App prüfen, ob der Strich über B (B̄) sauber dargestellt wird.'])
    anhaengen(d, 9914, schwer)
