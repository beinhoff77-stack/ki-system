"""NT-D 3 (23.11.2026): Vorrat für Nachtests auffüllen (drei Runden ohne Wiederholung).

Nachgerechnet mit schule.nachtest_vorrat (je Gruppe, echte DB, lesend): einzige Lücke heute
„Schrägbilder und Raumdarstellung – Teil 1 von 2“ in RS II/III (pyramide, wahre_groesse: 6 von 9).
Vorsorge für die Pflichtlisten aus LK-D 4 (noch nicht in der DB): Thema 31 RS I/II/III (definitionsmenge,
termwert: 8 von 9) und Thema 1 Gymnasium (zwei_schritte, probe: 6 von 9).

Nur Sicherungs-Aufgaben an bestehende Etappen; Texte selbst formuliert, Lösungen hier berechnet.
  python3 _nt_2311.py [thema …]   – anhängen (zweiter Lauf hängt nichts doppelt an)
  python3 _nt_2311.py --sql       – inhalte/pruefung/lehrplan/nt_einspiel_2311.sql schreiben
"""
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lk_etappen_2211 import wahl, z, _schluessel
from _nt_2211 import S, L_, THEMEN, sql as _sql

SQL = Path(__file__).resolve().parent.parent / 'pruefung' / 'lehrplan' / 'nt_einspiel_2311.sql'


# ------------------------------------------------------------------ 91 pyramide (+3), wahre_groesse (+3)
def pyramide():
    l = 'pyramide'
    return [
        S(l, 'zahl', 'Die Grundfläche einer Pyramide ist ein Siebeneck. Wie viele Kanten hat die Pyramide?',
          '7 Kanten in der Grundfläche und 7 Seitenkanten zur Spitze: 7 + 7 = 14.', o={'wert': 14}, c='2 * 7'),
        S(l, 'zahl', 'Eine Pyramide hat 10 Kanten. Wie viele Flächen hat sie?',
          'Bei einem n-Eck als Grundfläche hat die Pyramide 2n Kanten: n = 10 : 2 = 5. Flächen: Grundfläche + 5 Seitenflächen = 6.', o={'wert': 6}, c='10 / 2 + 1'),
        L_(l, 2, 'luecken', 'Die Grundfläche einer Pyramide ist ein Neuneck. Gib die Anzahl der Ecken, Kanten und Flächen an.',
           'Ecken: 9 + Spitze = 10. Kanten: 9 unten + 9 zur Spitze = 18. Flächen: 9 Seitenflächen + Grundfläche = 10.',
           'Ecken □ · Kanten □ · Flächen □', 'je eine ganze Zahl', [10, 18, 10]),
    ]


def wahre_groesse():
    l = 'wahre_groesse'
    return [
        S(l, 'zahl', 'Im Schrägbild mit q = 0,5 ist eine Kante nach hinten 4,5 cm lang gezeichnet. Wie lang ist sie in Wirklichkeit?',
          'Nach hinten wird halbiert, also zurückrechnen: 4,5 cm : 0,5 = 9 cm.', o={'wert': 9, 'einheit': 'cm'}, c='4.5 / 0.5'),
        S(l, 'auswahl', 'Ein Würfel wird als Schrägbild mit q = 0,5 und 45° gezeichnet. Welche Kanten erscheinen in wahrer Länge?',
          'Kanten parallel zur Zeichenebene (Breite und Höhe) bleiben in wahrer Länge; nur die Kanten nach hinten werden mit q verkürzt.',
          **wahl('die Kanten nach rechts und nach oben', ['nur die Kanten nach hinten', 'alle Kanten', 'keine Kante'], 0)),
        L_(l, 2, 'luecken', 'Ein Quader ist 8 cm breit, 3 cm hoch und 6 cm tief. Zeichne ihn mit q = 0,5. Wie lang werden Breite, Höhe und Tiefe gezeichnet?',
           'Breite und Höhe bleiben: 8 cm und 3 cm. Die Tiefe geht nach hinten: 6 cm · 0,5 = 3 cm.',
           'Breite □ cm · Höhe □ cm · Tiefe □ cm', 'je eine ganze Zahl', [8, 3, 3]),
    ]


# ------------------------------------------------------------------ 31 definitionsmenge (+1), termwert (+1)
def definitionsmenge():
    l = 'definitionsmenge'
    return [S(l, 'zahl', 'Für welche Zahl ist der Term 12/(3x − 9) nicht definiert?',
              'Der Nenner darf nicht 0 sein: 3x − 9 = 0, also x = 3. Für x = 3 ist der Term nicht definiert.', o={'wert': 3}, c='9 / 3')]


def termwert():
    l = 'termwert'
    x = 4
    w = Fr(3 * x - 2, x + 6)
    return [S(l, 'zahl', 'Berechne T(4) für T(x) = (3x − 2)/(x + 6).',
              f'Einsetzen: (3 · 4 − 2)/(4 + 6) = 10/10 = {z(w)}.', o={'wert': int(w)}, c='(3 * 4 - 2) / (4 + 6)')]


# ------------------------------------------------------------------ 1 zwei_schritte (+3), probe (+3)
def zwei_schritte():
    l = 'zwei_schritte'
    A = []
    for a, b, x in ((6, 17, 13), (9, 25, 8)):
        A.append(S(l, 'zahl', f'Löse {a} · x + {b} = {a * x + b}.',
                   f'Rückwärts: erst − {b}: {a * x + b} − {b} = {a * x}, dann : {a}: {a * x} : {a} = {x}.', o={'wert': x}, c=f'({a * x + b} - {b}) / {a}'))
    A.append(S(l, 'auswahl', 'Welcher Rechenweg löst x · 4 − 15 = 33?',
               'Rückwärts rechnen heißt: die letzte Rechnung zuerst umkehren. Erst + 15 (33 + 15 = 48), dann : 4 (48 : 4 = 12).',
               **wahl('erst + 15, dann : 4', ['erst : 4, dann + 15', 'erst − 15, dann · 4', 'erst · 4, dann − 15'], 2)))
    return A


def probe():
    l = 'probe'
    return [
        S(l, 'auswahl', 'So wurde 3 · x + 8 = 35 gelöst: Schritt 1: 35 − 8 = 27. Schritt 2: 27 · 3 = 81. Ergebnis: x = 81. Wo steckt der Fehler?',
          'In Schritt 2 muss geteilt werden: 27 : 3 = 9. Probe: 3 · 9 + 8 = 35 ✓. Mit 81 wäre 3 · 81 + 8 = 251.',
          **wahl('In Schritt 2: Es muss 27 : 3 heißen.', ['In Schritt 1: Es muss 35 + 8 heißen.', 'Es gibt keinen Fehler.', 'Beide Schritte sind falsch.'], 1)),
        S(l, 'zahl', 'Bei x : 4 − 6 = 9 hat jemand x = 12 herausbekommen. Die Probe geht nicht auf. Wie heißt die richtige Lösung?',
          'Probe: 12 : 4 − 6 = −3, nicht 9. Richtig rückwärts: 9 + 6 = 15, 15 · 4 = 60. Probe: 60 : 4 − 6 = 9 ✓.', o={'wert': 60}, c='(9 + 6) * 4'),
        S(l, 'auswahl', 'Welche Zahl ist die Lösung von 5 · x − 12 = 43? Mache die Probe.',
          'Probe mit 11: 5 · 11 − 12 = 55 − 12 = 43 ✓. Die anderen Zahlen ergeben nicht 43.',
          **wahl('11', ['9', '12', '6'], 2)),
    ]


NT = {'raum.schraegbilder': [pyramide, wahre_groesse], 'terme.bruchterme': [definitionsmenge, termwert],
      'gleichungen.einfach': [zwei_schritte, probe]}
TID = {'raum.schraegbilder': 91, 'terme.bruchterme': 31, 'gleichungen.einfach': 1}


TF = {('gleichungen.einfach', 'zwei_schritte'): 'umkehren', ('gleichungen.einfach', 'probe'): 'verstehen'}   # Teilfähigkeit wie in der Datei


def _mit_tf(thema, A):
    for a in A:
        a['t'] = TF.get((thema, a['l']), a['t'])
    return A


def nt_anhaengen(thema):
    pfad = THEMEN / f'{thema}.json'
    roh = pfad.read_text(encoding='utf-8')
    d = json.loads(roh)
    lz = [e['lernziel'] for e in d['inhalt']['etappen']]
    da = {_schluessel(a) for a in d['aufgaben']}
    n = 0
    for fn in NT[thema]:
        for a in _mit_tf(thema, fn()):
            assert a['l'] in lz, (thema, a['l'])
            if _schluessel(a) in da:
                continue
            d['aufgaben'].append(a); da.add(_schluessel(a)); n += 1
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
    print(f'  NT-D 3 {thema}: {n} neue Aufgaben')


if __name__ == '__main__':
    if '--sql' in sys.argv:
        NTS = {th: [(lambda f, th=th: (lambda: _mit_tf(th, f())))(f) for f in fs] for th, fs in NT.items()}
        _sql(NTS, TID, SQL, 'NT-D 3 (23.11.2026): Vorrat für Nachtests auffüllen – drei Runden ohne Wiederholung (91 Teil 1 RS II/III; Vorsorge 31 RS, 1 Gym).', '_nt_2311.py')
        t = SQL.read_text(encoding='utf-8')
        alt = t[t.index('-- Reihenfolge:'):t.index('-- Die neuen Aufgaben')]
        t = t.replace(alt, '-- Reihenfolge: unabhängig von TL-S; das SQL sucht die Einheit, deren Etappen-Katalog die Etappe enthält (Thema oder Teil über teil_stamm).\n'
                           '--   Abbruch mit Hinweis, wenn eine Etappe in keiner Einheit steht. Nach NT-S 2 einspielen (wirkt sonst nur als Vorrat).\n')
        SQL.write_text(t, encoding='utf-8')
    else:
        for t in (sys.argv[1:] or list(NT)):
            nt_anhaengen(t)
