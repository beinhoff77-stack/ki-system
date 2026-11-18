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


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('stochastik.verknuepft', 13_9_14)
# c) FEHLER: Angaben unmöglich (P(A) + P(B) = 1,1 verlangt P(A ∩ B) ≥ 0,1), markierte Antwort P(A ∪ B) = 1,03 > 1
#    → Aufgabe mit möglichen Angaben (P(A) + P(B) − 1 ≤ P(A ∩ B) ≤ min(P(A), P(B))); alle übrigen Aufgaben dieses Typs nachgeprüft: möglich
BF.ersetze('verstehen', 'P(A) = 0,6, P(B) = 0,5, P(A ∩ B) = 0,07. Jemand rechnet P(A ∪ B) = 1,1. Was stimmt?', BF.A(
    'P(A) = 0,6, P(B) = 0,5, P(A ∩ B) = 0,2. Jemand rechnet P(A ∪ B) = 1,1. Was stimmt?',
    'Falsch: Die Schnittmenge wurde doppelt gezählt; P(A ∪ B) = 0,9.',
    ['Falsch: P(A ∪ B) = 1,3.', 'Falsch: P(A ∪ B) = 0,2.', 'Richtig.'],
    'Additionssatz: P(A ∪ B) = 0,6 + 0,5 − 0,2 = 0,9. Schon 1,1 > 1 zeigt den Fehler: Eine Wahrscheinlichkeit ist nie größer als 1.',
    'Sind A und B unvereinbar?'))
# a) sechsmal derselbe Typ bzw. Routine auf Stufe 3 → je drei davon Stufe 2
BF.stufe('verknuepfen', 'Aus den Zahlen 1 bis 25 wird zufällig eine gezogen. A: „Die Zahl ist durch 3 teilbar.“ B: „Die Zahl ist eine Quadratzahl.“ Wie viele Zahlen liegen in A ∩ B̄?', 2)
BF.stufe('verknuepfen', 'Aus den Zahlen 1 bis 50 wird zufällig eine gezogen. A: „Die Zahl ist durch 5 teilbar.“ B: „Die Zahl ist eine Primzahl.“ Wie viele Zahlen liegen in Ā ∩ B?', 2)
BF.stufe('verknuepfen', 'Aus den Zahlen 1 bis 25 wird zufällig eine gezogen. A: „Die Zahl ist eine Primzahl.“ B: „Die Zahl ist durch 4 teilbar.“ Berechne P(A ∩ B̄ („A, aber nicht B“)) als Dezimalzahl.', 2)
BF.stufe('tafel_wkeit', 'Die Tafel zeigt 250 Besucher eines Freibads. A: „ist Erwachsener“, B: „hat eine Jahreskarte“. Ein Besucher wird zufällig ausgewählt. Mit welcher Wahrscheinlichkeit gilt: mindestens eines von beiden? Gib das Ergebnis als Dezimalzahl an.', 2)
BF.stufe('tafel_wkeit', 'Die Tafel zeigt 100 Kunden eines Online-Shops. A: „zahlt per Rechnung“, B: „bestellt zum ersten Mal“. Eine Kundin oder ein Kunde wird zufällig ausgewählt. Mit welcher Wahrscheinlichkeit gilt: „zahlt per Rechnung“ oder „bestellt zum ersten Mal“ (mindestens eines)? Gib das Ergebnis als Dezimalzahl an.', 2)
BF.stufe('tafel_wkeit', 'Die Tafel zeigt 500 Kunden eines Online-Shops. A: „zahlt per Rechnung“, B: „bestellt zum ersten Mal“. Eine Kundin oder ein Kunde wird zufällig ausgewählt. Mit welcher Wahrscheinlichkeit gilt: „zahlt per Rechnung“ oder „bestellt zum ersten Mal“ (mindestens eines)? Gib das Ergebnis als Dezimalzahl an.', 2)

# ---- BEFUNDE ENDE ----

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
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden


# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl9) ----
from _durchsicht_kl9 import Befunde as _DSB, durchsicht  # noqa: E402

DS = _DSB('stochastik.verknuepft', 19_9_6)
# verknuepfen: A ∩ B̄ zählen wie auf Stufe 2
DS.stufe('verknuepfen', 'Aus den Zahlen 1 bis 25 wird zufällig eine gezogen. A: „Die Zahl ist ungerade.“ B: „Die Zahl ist durch 3 teilbar.“ Berechne P(A ∩ B̄ („A, aber nicht B“)) als Dezimalzahl.', 2)
# vierfeld: „Gesamt minus drei Felder“ ist Ergänzen wie Stufe 1/2 → Stufe 2
for _n in ('200', '120'):
    DS.stufe('vierfeld', f'Untersucht werden {_n} Schülerinnen und Schüler einer Schule. A: „hat ein Haustier“, B: „fährt mit dem Rad zur Schule“. Ergänze das Feld „?“.', 2)
DS.stufe('vierfeld', 'Untersucht werden 500 Mitglieder eines Fußballvereins. A: „spielt in einer Mannschaft“, B: „ist jünger als 18 Jahre“. Ergänze das Feld „?“.', 2)
# tafel_wkeit: „mindestens eines“ steht schon auf Stufe 2 → Stufe 2
for _t in ('Die Tafel zeigt 400 Besucher eines Freibads. A: „ist Erwachsener“, B: „hat eine Jahreskarte“. Ein Besucher wird zufällig ausgewählt. Mit welcher Wahrscheinlichkeit gilt: „ist Erwachsener“ oder „hat eine Jahreskarte“ (mindestens eines)? Gib das Ergebnis als Dezimalzahl an.',
           'Die Tafel zeigt 500 Teilnehmende einer Umfrage. A: „liest täglich Nachrichten“, B: „ist älter als 40 Jahre“. Eine teilnehmende Person wird zufällig ausgewählt. Mit welcher Wahrscheinlichkeit gilt: mindestens eines von beiden? Gib das Ergebnis als Dezimalzahl an.',
           'Die Tafel zeigt 250 Jugendliche. A: „hat einen Hund“, B: „reitet“. Mit welcher Wahrscheinlichkeit hat eine zufällig gewählte Person einen Hund oder reitet? Gib sie in Prozent an.'):
    DS.stufe('tafel_wkeit', _t, 2)
# verstehen: Gegenereignis „mindestens einmal“ ist Stufe 1 (jetzt in Schritt 5 erklärt); je eine Wiederholung von Stufe 3 auf 2
for _t in ('Bei 6 Würfelwürfen ist A: „mindestens einmal eine Sechs“. Was ist das Gegenereignis Ā?', 'Bei 3 Torschüssen ist A: „mindestens einmal ein Treffer“. Was ist das Gegenereignis Ā?',
           'Bei 6 Münzwürfen ist A: „mindestens einmal Kopf“. Was ist das Gegenereignis Ā?', 'Was ist das Gegenereignis zu „mindestens eine Sechs bei zwei Würfen“?'):
    DS.stufe('verstehen', _t, 1)
DS.stufe('verstehen', 'Bei 4 Würfelwürfen ist A: „mindestens einmal eine Sechs“. Was ist das Gegenereignis Ā?', 1)
DS.stufe('verstehen', 'P(A) = 0,5, P(B) = 0,4, P(A ∩ B) = 0,07. Jemand rechnet P(A ∪ B) = 0,9. Was stimmt?', 2)
DS.stufe('verstehen', 'P(A) = 0,7, P(B) = 0,4. Welcher Wert ist für P(A ∪ B) möglich?', 2)

DS_KARTEN = {
    'verstehen': {
        'woerter': [['unvereinbar', 'A und B haben kein gemeinsames Ergebnis'],
                    ['Gegenereignis', 'Ā: alles, was nicht zu A gehört']],
        'schritte': [{'text': 'Behauptung: P(A) = 0,7, P(B) = 0,6, A und B sind unvereinbar.'},
                     {'text': 'Unvereinbar hieße: P(A ∪ B) = 0,7 + 0,6 = 1,3.',
                      'bild': {'boegen': [{'von': 0, 'bis': 0.7, 'name': 'gegessen'}, {'von': 0.7, 'bis': 1.3, 'name': 'gespielt'}]}},
                     {'text': 'Mehr als alle Gäste gibt es nicht: 1,3 ist größer als 1.', 'bild': {'punkte': [{'wert': 1, 'name': 'alle'}]}},
                     {'text': 'Also ⟦überschneiden sich A und B⟧. Die Behauptung ist falsch.'},
                     {'text': 'Das Gegenereignis zu „mindestens einmal“ heißt ⟦„keinmal“⟧.',
                      'bild': {'typ': 'tabelle', 'kopf': ['Ereignis A', 'Gegenereignis Ā'], 'zeilen': [['mindestens ein Treffer', 'kein Treffer']]}}],
    },
}

if __name__ == '__main__':
    durchsicht('stochastik.verknuepft', DS, DS_KARTEN)


# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl9) ----
from _stufen_kl9 import Stufen, stufen  # noqa: E402

ST = Stufen('stochastik.verknuepft', 20_9_6)
Z, A, L = ST.Z, ST.A, ST.L

# verknuepfen
ST.stufenleiter('verknuepfen', 'A ∩ B, A ∪ B und Ā in Worten deuten und bei Zahlen 1 bis 20 abzählen.',
                'Ereignisse in Zeichen schreiben, „A, aber nicht B“ abzählen, Sachsituation mit zwei Merkmalen.',
                '„Weder noch“ und Gegenereignisse von Verknüpfungen, Bedingungen an Teiler, Fehler bei „oder“, Beschreibungen beurteilen.')
ST.typ('verknuepfen', '/Was bedeutet das Ereignis/', 'erkennen')
ST.typ('verknuepfen', '/weder A/', 'verknuepfen')
ST.typ('verknuepfen', 'Aus den Zahlen 1 bis 20 wird zufällig eine gezogen.', 'direkt', s=1)
ST.typ('verknuepfen', '/Wie schreibt man das Ereignis/', 'darstellung')
ST.typ('verknuepfen', 'Aus 50 Kugeln', 'transfer')
ST.typ('verknuepfen', '/^(S: |In zwei verschiedenen)/', 'begruenden')
ST.typ('verknuepfen', 'Beim Würfeln ist A = {2; 4; 6}', 'verknuepfen')
ST.typ('verknuepfen', '/^(Aus den Zahlen|Beim Würfeln)/', 'mehrschritt')
ST.neu('verknuepfen', 'einkleidung', Z('In einer Klasse mit 25 Kindern spielen 10 Fußball, 8 Handball und 3 beides. Wie viele Kinder spielen Fußball, aber nicht Handball?', 7, '10 - 3',
       'Fußball, aber nicht Handball ist F ∩ H̄: alle Fußballer ohne die, die beides spielen: 10 − 3 = 7.', 'Wer spielt beides? Diese Kinder musst du abziehen.'))
ST.neu('verknuepfen', 'fehler', A('Jemand sagt: „A ∪ B heißt: A und B treten beide ein.“ Was stimmt?', 'Falsch: A ∪ B heißt mindestens eines tritt ein; beide zugleich ist A ∩ B.',
       ['Richtig.', 'Falsch: A ∪ B heißt keines tritt ein.', 'Falsch: A ∪ B heißt genau eines tritt ein.'], 'Vereinigung (∪) = „oder“ = mindestens eines. Schnitt (∩) = „und“ = beide.', 'Denk an das Beispiel der Lernkarte.'))
ST.neu('verknuepfen', 'parameter', A('Aus den Zahlen 1 bis 20 wird eine gezogen. A: „durch k teilbar“, B: „gerade“. Für welches k gilt A ∩ B = A, also jede Zahl aus A ist auch gerade?', 'k = 4', ['k = 3', 'k = 5', 'k = 7'],
       'A ∩ B = A heißt: A liegt ganz in B. Alle Vielfachen von 4 sind gerade. Bei 3, 5 und 7 gibt es ungerade Vielfache (3, 5, 7).', 'Suche ein ungerades Vielfaches.'))
ST.knobel('verknuepfen', Z('Wie viele der Zahlen von 1 bis 100 sind weder durch 2 noch durch 3 teilbar?', 33, '100 - 50 - 33 + 16',
          'Durch 2 teilbar: 50, durch 3: 33, durch beide (also durch 6): 16. Mindestens durch eine: 50 + 33 − 16 = 67. Weder noch: 100 − 67 = 33.',
          'Zähle erst die Zahlen, die durch 2 oder 3 teilbar sind – ohne doppelt zu zählen.'))
ST.knobel('verknuepfen', Z('Aus 1 bis 30 wird gezogen. A: „durch 2 teilbar“, B: „durch 3 teilbar“, C: „durch 5 teilbar“. Wie viele Zahlen liegen in A ∩ B ∩ C̄?', 4, '30 // 6 - 1',
          'A ∩ B sind die Vielfachen von 6: 6, 12, 18, 24, 30. Davon ist nur 30 auch durch 5 teilbar. Also bleiben 4 Zahlen.',
          'Was haben Zahlen gemeinsam, die durch 2 und durch 3 teilbar sind?'))

# additionssatz
ST.stufenleiter('additionssatz', 'P(A ∪ B) = P(A) + P(B) − P(A ∩ B) mit gegebenen Werten.',
                'Rückwärts P(A ∩ B) finden, „keines“ berechnen, Prozentangaben und Glücksräder.',
                'Fehlende Einzelwahrscheinlichkeit, Grenzen für P(A ∩ B), Fehler ohne Schnitt, Parameter p, Mängel-Statistik, mehrteilige Aufgabe.')
ST.typ('additionssatz', '/^Es gilt P\\(A\\) = [\\d,]+, P\\(B\\) = [\\d,]+ und P\\(A ∩ B\\) = [\\d,]+\\. Berechne P\\(A ∪ B\\)/', 'direkt')
ST.typ('additionssatz', '/und P\\(A ∪ B\\) = .* Berechne P\\(A ∩ B\\)/', 'umkehr')
ST.typ('additionssatz', '/Mit welcher Wahrscheinlichkeit tritt keines/', 'mehrschritt')
ST.typ('additionssatz', '/^(Beim Würfeln|In einer Klasse|Bei einem Glücksrad)/', 'einkleidung')
ST.typ('additionssatz', '/^Aus 1 bis/', 'mehrschritt')
ST.typ('additionssatz', 'Von 800', 'transfer')
ST.typ('additionssatz', 'Es gilt P(A) = 0,45', 'rueckwaerts')
ST.typ('additionssatz', 'Es gilt P(A) = 0,6 und', 'begruenden')
ST.typ('additionssatz', 'A und B sind unvereinbar', 'verknuepfen')
ST.neu('additionssatz', 'erkennen', A('Warum zieht man im Additionssatz P(A ∩ B) ab?', 'Weil P(A) + P(B) die Ergebnisse in A ∩ B doppelt zählt.', ['Weil A ∩ B nie eintreten kann.', 'Weil man immer etwas abziehen muss.', 'Weil P(A ∩ B) größer als 1 ist.'],
       'Die Ergebnisse, die in A und in B liegen, stecken in P(A) und in P(B). Einmal abziehen korrigiert das.', 'Denk an die Schnittmenge im Bild.'))
ST.neu('additionssatz', 'direkt', Z('Bei einer Umfrage ist P(A) = 0,3, P(B) = 0,4 und P(A ∩ B) = 0,1. Berechne P(A ∪ B).', 0.6, '0.3 + 0.4 - 0.1',
       'P(A ∪ B) = 0,3 + 0,4 − 0,1 = 0,6.', 'Addieren und die Schnittmenge einmal abziehen.'))
ST.neu('additionssatz', 'einkleidung', Z('In einer Klasse tragen 30 % eine Brille, 20 % eine Zahnspange und 5 % beides. Wie viel Prozent tragen mindestens eines davon?', 45, '30 + 20 - 5',
       '30 % + 20 % − 5 % = 45 %.', 'Mindestens eines heißt „oder“.', einheit='%'))
ST.neu('additionssatz', 'fehler', A('Jemand rechnet bei P(A) = 0,5 und P(B) = 0,7: P(A ∪ B) = 0,5 + 0,7 = 1,2. Was stimmt?', 'Falsch: Eine Wahrscheinlichkeit ist höchstens 1; P(A ∩ B) muss abgezogen werden.',
       ['Richtig.', 'Falsch: P(A ∪ B) = 0,35.', 'Falsch: P(A ∪ B) = 0,2.'], 'Ohne Schnittmenge zählt man doppelt. Hier ist P(A ∩ B) mindestens 0,2, also P(A ∪ B) höchstens 1.', 'Kann eine Wahrscheinlichkeit größer als 1 sein?'))
ST.neu('additionssatz', 'parameter', Z('Es gilt P(A) = P(B) = p, P(A ∩ B) = 0,1 und P(A ∪ B) = 0,7. Wie groß ist p?', 0.4, '(0.7 + 0.1) / 2',
       '0,7 = p + p − 0,1 ⇒ 2p = 0,8 ⇒ p = 0,4.', 'Setze in den Additionssatz ein.'))
ST.neu('additionssatz', 'pruefung', L('Von 200 Gästen trinken 120 Kaffee, 90 essen Kuchen, 50 tun beides. a) Wie viele haben mindestens eines davon? b) Wie viele weder noch?', 'a) □; b) □', [160, 40], ['120 + 90 - 50', '200 - 160'],
       'a) 120 + 90 − 50 = 160. b) 200 − 160 = 40.', 'Erst „oder“, dann der Rest.'))
ST.neu('additionssatz', 'transfer', Z('Bei einem Versand sind 8 % der Pakete zu spät, 5 % beschädigt und 2 % beides. Mit welcher Wahrscheinlichkeit ist ein Paket pünktlich und unbeschädigt?', 0.89, '1 - (0.08 + 0.05 - 0.02)',
       'Mindestens ein Problem: 0,08 + 0,05 − 0,02 = 0,11. Kein Problem: 1 − 0,11 = 0,89.', 'Bilde das Gegenereignis von „mindestens ein Problem“.'))
ST.knobel('additionssatz', Z('Es gilt P(A) = 0,6 und P(B) = 0,7. Wie groß kann P(A ∩ B) höchstens sein?', 0.6, 'min(0.6, 0.7)',
          'A ∩ B liegt ganz in A, also P(A ∩ B) ≤ P(A) = 0,6. Der Wert 0,6 ist möglich, wenn A ganz in B liegt; dann ist P(A ∪ B) = 0,7 ≤ 1.',
          'Kann der Schnitt größer sein als eines der beiden Ereignisse?'))
ST.knobel('additionssatz', Z('Wie viele Zahlen von 1 bis 30 sind durch 2, 3 oder 5 teilbar?', 22, '15 + 10 + 6 - 5 - 3 - 2 + 1',
          'Einzeln: 15 + 10 + 6. Doppelt gezählt sind Vielfache von 6 (5), 10 (3) und 15 (2): abziehen. Die 30 (durch alle drei) wurde dreimal addiert und dreimal abgezogen: einmal dazu. 31 − 10 + 1 = 22.',
          'Wie beim Additionssatz, nur mit drei Ereignissen. Achte auf Zahlen, die in allen dreien liegen.'))

# vierfeld
ST.stufenleiter('vierfeld', 'Ein fehlendes Feld aus Zeilen- oder Spaltensumme ergänzen.',
                'Mehrere Felder nacheinander ergänzen, aus drei Angaben die ganze Tafel bauen, ein inneres Feld rückwärts bestimmen.',
                'Falsche Summen finden, Prozentangaben verketten, Bedingungen wie „doppelt so groß“, Unmögliches erkennen.')
ST.typ('vierfeld', 'Untersucht werden', 'direkt', s=1)
ST.typ('vierfeld', '/In der Tafel ist genau eine Summe falsch/', 'fehler')
ST.typ('vierfeld', '/% haben A\\. Unter denen mit A/', 'verknuepfen')
ST.typ('vierfeld', '/Ergänze das Feld „\\?“/', 'darstellung')
ST.typ('vierfeld', '/^(Untersucht werden|In einer Vierfeldertafel ist)/', 'mehrschritt')
ST.typ('vierfeld', 'Von 400 Befragten', 'transfer')
ST.typ('vierfeld', 'In einer Vierfeldertafel mit 100 Personen', 'rueckwaerts')
ST.typ('vierfeld', '120 Jugendliche', 'verknuepfen')
ST.neu('vierfeld', 'erkennen', A('In welchem Feld einer Vierfeldertafel stehen die Personen „A, aber nicht B“?', 'A ∩ B̄', ['A ∩ B', 'Ā ∩ B', 'Ā ∩ B̄'],
       '„nicht B“ heißt B̄. Zusammen mit A: A ∩ B̄.', 'Übersetze „nicht B“ in Zeichen.'))
ST.neu('vierfeld', 'umkehr', Z('In einer Tafel mit 200 Personen ist B = 70 (Randsumme) und Ā ∩ B̄ = 90. Wie groß ist A ∩ B̄?', 40, '(200 - 70) - 90',
       'B̄ = 200 − 70 = 130. In der Spalte B̄: A ∩ B̄ = 130 − 90 = 40.', 'Bestimme zuerst die Randsumme von B̄.'))
ST.neu('vierfeld', 'begruenden', A('Kann es in einer Tafel mit 100 Personen A = 70, B = 20 und A ∩ B = 30 geben?', 'Nein, A ∩ B kann nicht größer als B sein.', ['Ja.', 'Nein, A + B muss 100 sein.', 'Nur wenn Ā ∩ B̄ = 0 ist.'],
       'A ∩ B ist ein Teil von B. 30 > 20 ist unmöglich.', 'Vergleiche A ∩ B mit B.'))
ST.neu('vierfeld', 'pruefung', L('Von 300 Gästen trinken 180 Kaffee, 120 davon essen auch Kuchen. 60 Gäste nehmen weder Kaffee noch Kuchen. a) Wie viele essen Kuchen, ohne Kaffee zu trinken? b) Wie viele essen insgesamt Kuchen?', 'a) □; b) □', [60, 180],
       ['(300 - 180) - 60', '120 + 60'], 'Ohne Kaffee: 300 − 180 = 120 Gäste, davon 60 ohne alles, also 60 mit Kuchen. Kuchen insgesamt: 120 + 60 = 180.', 'Lege eine Vierfeldertafel an: Kaffee ja/nein, Kuchen ja/nein.'))
ST.knobel('vierfeld', Z('In einer Gruppe hat jeder Vierte mit A auch B, jeder Dritte mit B auch A. 80 von 200 Personen haben weder A noch B. Wie viele haben A?', 80, '4 * 20',
          'A ∩ B = A/4 = B/3. Mit A = 4k ist A ∩ B = k und B = 3k. Mindestens eines: 4k + 3k − k = 6k = 200 − 80 = 120, also k = 20 und A = 80.',
          'Nenne die Zahl in A ∩ B einfach k.'))
ST.knobel('vierfeld', Z('In einer Gruppe hat genau die Hälfte das Merkmal A und genau ein Drittel das Merkmal B. 10 Personen haben beides, 40 keines. Wie groß ist die Gruppe?', 180, '(40 - 10) * 6',
          'Mindestens eines: n/2 + n/3 − 10 = 5n/6 − 10. Keines: n − (5n/6 − 10) = n/6 + 10 = 40. Also n/6 = 30, n = 180.',
          'Stelle eine Gleichung für „keines“ auf.'))

# tafel_wkeit
ST.stufenleiter('tafel_wkeit', 'Ein inneres Feld oder eine Randsumme durch die Gesamtzahl teilen.',
                'Wahrscheinlichkeiten aus Tafeln mit Anzahlen oder Wahrscheinlichkeiten, „oder“ aus der Tafel, ein Feld rückwärts.',
                'Fehlende Felder über den Additionssatz, Fehler beim Lesen eines Feldes, Summe der Felder begründen, Parameter p, mehrteilige Aufgabe.')
ST.typ('tafel_wkeit', 'Die Tafel zeigt', 'direkt', s=1)
ST.typ('tafel_wkeit', '/^(Die Tafel|Die Tafel enthält)/', 'darstellung', s=2)
ST.typ('tafel_wkeit', '/^(Von 250|In einer Tafel gilt P\\(A ∩ B\\) = 0,1 )/', 'mehrschritt')
ST.typ('tafel_wkeit', '/^Die Tafel zeigt/', 'verknuepfen')
ST.typ('tafel_wkeit', 'Es gilt P(A) = 0,4, P(B) = 0,5', 'rueckwaerts')
ST.typ('tafel_wkeit', 'In einer Tafel mit relativen', 'verknuepfen')
ST.neu('tafel_wkeit', 'erkennen', A('Was erhältst du, wenn du die Randsumme der Zeile A durch die Gesamtzahl teilst?', 'P(A)', ['P(A ∩ B)', 'P(B)', 'P(A ∪ B)'],
       'Die Zeilensumme zählt alle mit A. Geteilt durch alle: P(A).', 'Welche Personen zählt die Zeile A?'))
ST.neu('tafel_wkeit', 'umkehr', Z('Es gilt P(A) = 0,4 und P(A ∩ B̄) = 0,25. Berechne P(A ∩ B).', 0.15, '0.4 - 0.25',
       'Die Zeile A besteht aus A ∩ B und A ∩ B̄: P(A ∩ B) = 0,4 − 0,25 = 0,15.', 'Die beiden Felder der Zeile ergeben zusammen P(A).'))
ST.neu('tafel_wkeit', 'fehler', A('Jemand liest P(A ∩ B) = 0,15 aus der Tafel und sagt: „Also haben 15 % das Merkmal A.“ Was stimmt?', 'Falsch: 15 % haben A und B; für P(A) braucht man die Randsumme.',
       ['Richtig.', 'Falsch: 15 % haben B.', 'Falsch: 85 % haben A.'], 'P(A) = P(A ∩ B) + P(A ∩ B̄). Das innere Feld zeigt nur einen Teil von A.', 'Welche Personen stehen in diesem Feld?'))
ST.neu('tafel_wkeit', 'begruenden', A('Stimmt: Die vier inneren Felder einer Tafel mit Wahrscheinlichkeiten ergeben zusammen immer 1?', 'Ja, jedes Ergebnis liegt in genau einem der vier Felder.', ['Nein, nur die Randsummen ergeben 1.', 'Nein, sie ergeben 2.', 'Nur wenn A und B unvereinbar sind.'],
       'Jede Person hat A oder nicht, B oder nicht – genau eine der vier Kombinationen. Zusammen sind das alle: 1.', 'Kann eine Person in zwei Feldern stehen?'))
ST.neu('tafel_wkeit', 'parameter', Z('In einer Tafel ist P(A ∩ B) = p, P(A ∩ B̄) = 2p, P(Ā ∩ B) = 3p und P(Ā ∩ B̄) = 4p. Wie groß ist P(A)?', 0.3, '3 * 0.1',
       'Alle Felder zusammen: 10p = 1, also p = 0,1. P(A) = p + 2p = 0,3.', 'Was ergeben alle vier Felder zusammen?'))
ST.neu('tafel_wkeit', 'pruefung', L('Von 500 Gästen haben 200 gegessen (A), 150 gespielt (B), 50 beides. a) P(A) in Prozent? b) P(A ∪ B) in Prozent?', 'a) □ %; b) □ %', [40, 60], ['200 * 100 // 500', '(200 + 150 - 50) * 100 // 500'],
       'a) 200 : 500 = 0,4 = 40 %. b) 200 + 150 − 50 = 300, 300 : 500 = 60 %.', 'Erst Anzahlen, dann durch 500.'))
ST.knobel('tafel_wkeit', Z('In einer Tafel gilt P(A ∩ B) = 0,2, P(Ā ∩ B̄) = 0,4 und P(A) = P(B). Wie groß ist P(A)?', 0.4, '0.2 + 0.2',
          'Die beiden anderen Felder sind gleich groß, weil P(A) = P(B): A ∩ B̄ = Ā ∩ B = y. 0,2 + 2y + 0,4 = 1, also y = 0,2. P(A) = 0,2 + 0,2 = 0,4.',
          'Was folgt aus P(A) = P(B) für die beiden übrigen Felder?'))
ST.knobel('tafel_wkeit', Z('In einer Tafel mit Anzahlen gilt P(A) = 0,35 und P(A ∩ B) = 0,12. Wie viele Personen sind es mindestens?', 100, '100',
          '0,35 · n und 0,12 · n müssen ganze Zahlen sein. 0,35 = 7/20 verlangt ein Vielfaches von 20, 0,12 = 3/25 ein Vielfaches von 25. Das kleinste gemeinsame Vielfache ist 100.',
          'Schreibe die Wahrscheinlichkeiten als gekürzte Brüche.'))

# bedingt
ST.stufenleiter('bedingt', 'P_B(A) in einer Tafel ablesen: nur die Spalte B zählt.',
                'Die Bedingung aus einem Text erkennen, Tafeln mit Merkmal A als Bedingung, P(B) im Baum.',
                'Test-Aufgaben, Baumdiagramme rückwärts, P(B) aus P(A ∩ B) und P_B(A), Verwechslung von Zeile und Spalte finden.')
ST.typ('bedingt', 'Berechne P_B(A), also', 'direkt')
ST.typ('bedingt', 'Was bedeutet P_B(A)', 'erkennen')
ST.typ('bedingt', 'Die Tafel zeigt', 'darstellung')
ST.typ('bedingt', 'In der Spalte B', 'mehrschritt')
ST.typ('bedingt', 'Berechne mit dem Baumdiagramm P(B)', 'mehrschritt')
ST.typ('bedingt', '/^(Berechne mit dem Baumdiagramm P_B|Von 200 Schülerinnen)/', 'verknuepfen')
ST.typ('bedingt', '/^(Ein Test|In einer Lostrommel)/', 'transfer')
ST.typ('bedingt', 'Es gilt P(A ∩ B)', 'rueckwaerts')
ST.neu('bedingt', 'direkt', Z('Von 40 Personen mit dem Merkmal B haben 10 auch das Merkmal A. Berechne P_B(A) als Dezimalzahl.', 0.25, '10 / 40',
       'Bedingung B: nur die 40 Personen zählen. P_B(A) = 10 : 40 = 0,25.', 'Teile durch die Anzahl mit B.'))
ST.neu('bedingt', 'einkleidung', L('In einer Klasse tragen 12 von 30 Kindern eine Brille; 4 der Brillenträger sind Linkshänder. Ein Brillenträger wird zufällig gewählt. Mit welcher Wahrscheinlichkeit ist er Linkshänder?', '□/□', [1, 3], ['1', '3'],
       'Bedingung: Brille. Nur die 12 Brillenträger zählen: 4/12 = 1/3.', 'Wer zählt, wenn man schon weiß, dass das Kind eine Brille trägt?'))
ST.neu('bedingt', 'fehler', A('Spalte B hat 50 Personen, Zeile A hat 80, A ∩ B = 20. Jemand rechnet P_B(A) = 20/80. Was stimmt?', 'Falsch: Bei der Bedingung B zählt die Spalte B: P_B(A) = 20/50 = 0,4.',
       ['Richtig.', 'Falsch: P_B(A) = 50/80.', 'Falsch: P_B(A) = 20/130.'], '20/80 = 0,25 wäre P_A(B), also die Bedingung A. Bei P_B(A) teilt man durch die Anzahl in B.', 'Was steht unten im Bruch bei der Bedingung B?'))
ST.knobel('bedingt', Z('In einer Klasse sind 60 % Mädchen. 50 % der Mädchen und 25 % der Jungen spielen ein Instrument. Ein Kind mit Instrument wird zufällig gewählt. Mit welcher Wahrscheinlichkeit ist es ein Mädchen?', 0.75, '30 / (30 + 10)',
          'Stell dir 100 Kinder vor: 60 Mädchen und 40 Jungen. 50 % von 60 sind 30 Mädchen mit Instrument, 25 % von 40 sind 10 Jungen mit Instrument. Bedingung Instrument: Nur diese 40 Kinder zählen, davon 30 Mädchen. 30 : 40 = 0,75.',
          'Rechne mit 100 Kindern: Wie viele Mädchen und wie viele Jungen spielen ein Instrument?'))
ST.knobel('bedingt', L('Zwei Münzen werden geworfen. Du erfährst: Mindestens eine zeigt Kopf. Mit welcher Wahrscheinlichkeit zeigen beide Kopf?', '□/□', [1, 3], ['1', '3'],
          'Ergebnisse: KK, KZ, ZK, ZZ. Mindestens einmal Kopf lässt KK, KZ, ZK übrig – drei gleich wahrscheinliche. Nur KK hat zweimal Kopf: 1/3, nicht 1/2.',
          'Schreib alle Ergebnisse auf und streiche, was nicht passt.'))

# verstehen
ST.stufenleiter('verstehen', 'Gegenereignis von „mindestens einmal“ benennen und Grenzen 0 ≤ P ≤ 1 kennen.',
                'Behauptungen über Unvereinbarkeit prüfen, mögliche Werte für P(A ∪ B) finden, Alltagsaussagen und Tafeln deuten.',
                'Fehler im Additionssatz und bei „bestimmt“ finden, sichere Aussagen begründen, Bedingungen an P(B), unmögliche Angaben erkennen.')
ST.typ('verstehen', '/^(Bei \\d+ |A und B sind unvereinbar|Was ist das Gegenereignis|Welcher Wert kann keine)/', 'erkennen')
ST.typ('verstehen', 'Jemand behauptet', 'mehrschritt')
ST.typ('verstehen', '/Jemand rechnet/', 'fehler')
ST.typ('verstehen', 'In einer Urne', 'fehler')
ST.typ('verstehen', '/Welcher Wert ist für P\\(A ∪ B\\) möglich/', 'umkehr', s=2)
ST.typ('verstehen', '/Welcher Wert ist für P\\(A ∪ B\\) möglich/', 'verknuepfen')
ST.typ('verstehen', '/^(Ein Glücksrad|Es gilt P\\(A\\) = 0,6 und P\\(B\\) = 0,5)/', 'begruenden')
ST.typ('verstehen', 'Welche Angaben sind unmöglich', 'verknuepfen')
ST.neu('verstehen', 'direkt', Z('Eine Münze wird zweimal geworfen. Berechne P(mindestens einmal Kopf) über das Gegenereignis.', 0.75, '1 - 0.25',
       'Gegenereignis: keinmal Kopf, also ZZ mit 1/4 = 0,25. Gesucht: 1 − 0,25 = 0,75.', 'Was ist das Gegenteil von „mindestens einmal“?'))
ST.neu('verstehen', 'einkleidung', A('Im Wetterbericht: Regen 60 %, Sonne 70 % am selben Tag. Jemand sagt: „Regen und Sonne schließen sich heute aus.“ Kann das stimmen?', 'Nein: Unvereinbar hieße 60 % + 70 % = 130 % > 100 %.',
       ['Ja.', 'Ja, wenn es abends regnet.', 'Nein, Regen und Sonne treten nie zusammen auf.'], 'Bei unvereinbaren Ereignissen addieren sich die Wahrscheinlichkeiten, die Summe dürfte höchstens 1 sein.', 'Wie bei der Behauptung auf der Lernkarte.'))
ST.neu('verstehen', 'darstellung', A('In einer Tafel mit Wahrscheinlichkeiten steht im Feld A ∩ B eine 0. Was bedeutet das?', 'A und B sind unvereinbar.', ['A ist das Gegenereignis von B.', 'A tritt nie ein.', 'B tritt sicher ein.'],
       'P(A ∩ B) = 0: A und B treten nie gemeinsam ein. Das heißt unvereinbar. Gegenereignis wäre zusätzlich P(Ā ∩ B̄) = 0.', 'Was bedeutet das Feld A ∩ B?'))
ST.neu('verstehen', 'einkleidung', A('Beim Würfeln: A „Augenzahl mindestens 5“, B „Augenzahl höchstens 2“. Was stimmt?', 'A und B sind unvereinbar, aber B ist nicht das Gegenereignis von A.',
       ['B ist das Gegenereignis von A.', 'A und B sind nicht unvereinbar.', 'A und B treten immer gemeinsam ein.'], 'A = {5; 6}, B = {1; 2}: kein gemeinsames Ergebnis. Ā wäre {1; 2; 3; 4}, also mehr als B.', 'Schreib A und B als Mengen.'))
ST.neu('verstehen', 'parameter', A('Für welche Werte von P(B) können A und B mit P(A) = 0,45 unvereinbar sein?', 'für 0 ≤ P(B) ≤ 0,55', ['für alle P(B)', 'nur für P(B) = 0,55', 'für P(B) ≥ 0,45'],
       'Unvereinbar heißt P(A ∪ B) = P(A) + P(B) ≤ 1, also P(B) ≤ 0,55.', 'Die Summe darf 1 nicht übersteigen.'))
ST.knobel('verstehen', L('Eine Münze wird viermal geworfen. Mit welcher Wahrscheinlichkeit kommt mindestens zweimal Kopf?', '□/□', [11, 16], ['16 - 1 - 4', '16'],
          '16 gleich wahrscheinliche Ergebnisse. Gegenereignis: keinmal Kopf (1 Ergebnis) oder genau einmal Kopf (4 Ergebnisse). P = 1 − 5/16 = 11/16.',
          'Zähle das Gegenereignis: höchstens einmal Kopf.'))
ST.knobel('verstehen', A('A ist mit B und mit C unvereinbar. P(A) = 0,3, P(B) = 0,4, P(C) = 0,5. Können B und C unvereinbar sein?', 'Nein, sie überschneiden sich mit mindestens 0,2.',
          ['Ja.', 'Nein, B und C müssen gleich sein.', 'Das kann man nicht entscheiden.'],
          'B und C liegen beide in Ā mit P(Ā) = 0,7. P(B ∪ C) ≤ 0,7, aber P(B) + P(C) = 0,9. Also P(B ∩ C) = 0,9 − P(B ∪ C) ≥ 0,2 > 0.',
          'Wo liegen B und C, wenn sie A nie treffen?'))

if __name__ == '__main__':
    stufen('stochastik.verknuepft', ST)
