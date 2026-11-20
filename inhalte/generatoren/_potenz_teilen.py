"""Sechsundzwanzigste Runde (Zweig potenz-teilen, 20.11.): Potenzgesetze in zwei eigene Flüge teilen.

Grundlage: inhalte/AUFTRAEGE.md „Sechsundzwanzigste Runde“ und inhalte/postfach/lehrplan-lb.md (AUFTRAGSENTWURF,
ENTSCHEIDUNG SEBASTIAN).

  Flug A  terme.potenzgesetze_natuerlich (thema_id 102, Samarkand 62)  – die vier Potenz-Lernkarten aus terme.umformen,
          Lernziel-Schlüssel unverändert; Aufgaben mit negativen Exponenten → Flug B, ersetzt durch gleichwertige mit
          natürlichen Exponenten; dazu die Aufgaben aus „Fehler finden“ (Gym 6), die ein Potenzgesetz voraussetzen.
  Flug B  terme.potenzgesetze_ganzzahlig (thema_id 103, Mumbai 60)    – neu (M8 4), Startbestand: die Aufgaben mit
          negativen Exponenten aus Flug A (umzug_nach_b); Lernkarten und Aufgaben in _potenz_teilen_b.py.
  terme.umformen       – die vier Lernkarten entfallen (8 bleiben).
  terme.potenzgesetze  – „Fehler finden“ ohne Potenzgesetze, nachgebaut bis zu den Mindestmengen; Karte neu erklärt.

Startbestand von Flug A: dieselben vier karte_her-Schritte wie in _br_plan.PLAN['terme.umformen'], angewendet auf ein leeres
Thema. Das ergibt Zeichen für Zeichen die vier Karten samt Aufgaben (und Reihenfolge), die bis jetzt in terme.umformen
standen (einmal geprüft: 168 Aufgaben gleich; der Generator prüft es nicht erneut, weil terme.umformen sie nicht mehr hat).

Jede Lösung wird beim Bauen nachgerechnet (Z/L über „c“), am Ende läuft das Prüfskript über jede geschriebene Datei.
"""
import collections
import copy
import json
import re
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
THEMEN = HIER.parent / 'themen'
sys.path.insert(0, str(HIER))
import _bereinigen as BR  # noqa: E402
from _befunde import _z, _l  # noqa: E402
from _stufen_kl5 import A as _a  # noqa: E402
from inhalt_pruefen import STUFE_VON, bauplan, pruefe  # noqa: E402  (Pfad setzt _bereinigen)

LZ_A = ('mal_gleiche_basis', 'gleicher_exponent', 'geteilt_gleiche_basis', 'anwenden')
BERICHT = collections.defaultdict(lambda: collections.defaultdict(list))


# ---------- Bausteine ----------
def Z(text, wert, c, w, h='-', **kw): return _z(text, wert, c, w, h, **kw)
def L(text, schablone, werte, c, w, h='-', hinweis='Je Lücke eine ganze Zahl.', grafik=None): return _l(text, schablone, werte, c, w, h, hinweis=hinweis, grafik=grafik)
def A(text, richtig, falsche, w, h='-'): return _a(text, richtig, falsche, w, h)


BRUCH = 'Zähler und Nenner als ganze Zahlen.'
CN = 'Erst die Zahl c, dann den Exponenten n (auch negativ).'


def _ohne_tipp(a):
    a = copy.deepcopy(a); a.pop('h', None); return a


def U(g, a):  return ('uebung', g, a)                 # Übung, Stufe folgt aus dem Typ
def K(a):     return ('bonus', 'knobel', a)           # Knobel-Bordkarte
def T(a):     return ('test', None, _ohne_tipp(a))
def KO(a):    return ('korrektur', None, _ohne_tipp(a))
def SI(a):    return ('sicherung', None, _ohne_tipp(a))


def _aufgabe(lz, p, g, a):
    x = {'l': lz, 't': lz, 'p': p, 's': 2 if p in ('test', 'korrektur', 'sicherung') else (3 if g == 'knobel' else STUFE_VON[g])}
    if g: x['g'] = g
    x.update(copy.deepcopy(a))
    if p in ('uebung', 'bonus'): assert x.get('h') and x['h'] != '-', ('Tipp fehlt', x['f']['text'])
    return x


def _ordnen_karte(d, lz):
    """Übungen der Karte wie in _bereinigen ordnen (nie zweimal derselbe Typ / Satzbau hintereinander);
    Reihenfolge der Karte: Übungen, Knobel, Test, Korrektur, Sicherung – an der Stelle der ersten Aufgabe der Karte."""
    xs = [a for a in d['aufgaben'] if a['l'] == lz]
    i0 = min(i for i, a in enumerate(d['aufgaben']) if a['l'] == lz)
    rest = [a for a in d['aufgaben'] if a['l'] != lz]
    vor = sum(1 for a in d['aufgaben'][:i0] if a['l'] != lz)
    neu = BR._ordnen([a for a in xs if a['p'] == 'uebung'])
    for p in ('bonus', 'test', 'korrektur', 'sicherung'): neu += [a for a in xs if a['p'] == p]
    d['aufgaben'] = rest[:vor] + neu + rest[vor:]


def _regeln(d, lz, je_typ_satzbau=False):
    """Mindestmengen der Zwanzigsten Runde (ohne überzählige): Stufe 1/2/3 mindestens 4/6/8 Übungen mit 2/3/4 Typen,
    Stufe 3 je Typ höchstens 3 (bei je_typ_satzbau: je Typ und Satzbau), 1–3 Knobel, Test ≥ 1, Korrektur ≥ 3, Sicherung ≥ 6."""
    ue = [a for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'uebung' and a.get('g')]
    for s, (anz, typ) in {1: (4, 2), 2: (6, 3), 3: (8, 4)}.items():
        c = collections.Counter(a['g'] for a in ue if a['s'] == s)
        assert sum(c.values()) >= anz and len(c) >= typ, f'{lz}: Stufe {s} {dict(c)}'
        if s == 3:
            zu = (collections.Counter((a['g'], bauplan(a)) for a in ue if a['s'] == 3) if je_typ_satzbau else c)
            assert all(n <= 3 for n in zu.values()), f'{lz}: Stufe 3 je Typ höchstens 3: {dict(zu)}'
    zahl = collections.Counter(a['p'] for a in d['aufgaben'] if a['l'] == lz)
    assert 1 <= zahl['bonus'] <= 3 and zahl['test'] >= 1 and zahl['korrektur'] >= 3 and zahl['sicherung'] >= 6, f'{lz}: {dict(zahl)}'


def _schreiben(thema, d):
    pfad = THEMEN / f'{thema}.json'
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    f, w, info = pruefe(pfad)
    assert not f, f'{thema}: ' + '; '.join(f[:8])
    texte = [a['f']['text'] for a in d['aufgaben']]
    assert len(texte) == len(set(texte)), f'{thema}: Fragetext doppelt'
    print(f'  POTENZ-TEILEN {thema}: {info}')
    (Path('/tmp') / f'potenz_teilen_{thema}.json').write_text(json.dumps(BERICHT[thema], ensure_ascii=False, indent=1))
    return d


def _ersetzen(d, thema, lz, alt_text, neu, felder=None):
    """Aufgabe an gleicher Stelle ersetzen (l, t, p, s, g bleiben). felder: nur diese Felder neu setzen (Fragetext bleibt)."""
    xs = [i for i, a in enumerate(d['aufgaben']) if a['l'] == lz and a['f']['text'] == alt_text]
    assert len(xs) == 1, (thema, lz, alt_text, len(xs))
    i = xs[0]; alt = d['aufgaben'][i]
    if felder:
        for k in felder: alt[k] = neu[k]
        BERICHT[thema]['loesungsweg'].append({'lz': lz, 'text': alt_text, 'felder': sorted(felder)})
        return
    a = {k: alt[k] for k in ('l', 't', 'p', 's', 'g') if k in alt}
    neu = copy.deepcopy(neu)
    if a['p'] not in ('uebung', 'bonus'): neu.pop('h', None)
    else: assert neu.get('h') and neu['h'] != '-', alt_text
    a.update(neu)
    assert a['f']['text'] not in {x['f']['text'] for x in d['aufgaben']}, ('doppelt', a['f']['text'])
    d['aufgaben'][i] = a
    BERICHT[thema]['ersetzt'].append({'lz': lz, 'p': a['p'], 's': a['s'], 'g': a.get('g'), 'alt': alt_text, 'neu': a['f']['text']})


# =====================================================================================================================
# Flug A – Startbestand und Umzug
# =====================================================================================================================
def start_a():
    """Die vier Karten genau so, wie _br_plan sie nach terme.umformen gebracht hat (Stand vor dieser Runde)."""
    d = {'inhalt': {'etappen': [], 'abschnitte': [], 'teilfaehigkeiten': [], 'bewertung': {'lernziele_pflicht': [], 'lernziele_vertiefung': []}},
         'aufgaben': []}
    plan = [BR.karte_her('terme.potenzgesetze', 'mal_gleiche_basis', 'Potenzen zusammenfassen'),
            BR.karte_her('terme.potenzgesetze', 'gleicher_exponent', 'Potenzen zusammenfassen', nach='mal_gleiche_basis'),
            BR.karte_her('terme.potenzgesetze', 'geteilt_gleiche_basis', 'Potenzen zusammenfassen', vertiefung=True, nach='gleicher_exponent'),
            BR.karte_her('terme.potenzgesetze', 'anwenden', 'Potenzen zusammenfassen', vertiefung=True, nach='geteilt_gleiche_basis')]
    alt = BR.BERICHT
    BR.BERICHT = {}
    try: BR.anwenden(d, 'potenz-teilen-start', plan)
    finally: BR.BERICHT = alt
    assert len(d['aufgaben']) == 168, len(d['aufgaben'])
    return d


# Negative Exponenten: im Fragetext oder in den Antworten (22, wie im Auftrag gezählt) …
NEG = re.compile(r'(?<![⁰¹²³⁴⁵⁶⁷⁸⁹ⁿᵏᵐ])⁻')  # Hoch-Minus am Anfang eines Exponenten (nicht: 10⁷⁻³ als Rechnung im Exponenten)


def _mit_minus_exponent(a): return bool(NEG.search(json.dumps([a['f'], a.get('a')], ensure_ascii=False)))


# … und 7 weitere, deren Ergebnis ein negativer Exponent ist (das Gesetz liefert aᵐ⁻ⁿ mit m < n). Das ist Stoff von M8 4.
NEGATIV_ERGEBNIS = ['3⁴ : 3⁸ = 3ᵏ. Wie groß ist k?', '2¹ : 2⁷ = 2ᵏ. Wie groß ist k?', 'Berechne 10¹ : 10⁶ und gib das Ergebnis als Dezimalzahl an.',
                    '5⁴ : 5⁶ = 5ᵏ. Wie groß ist k?', '2¹ : 2⁸ = 2ᵏ. Wie groß ist k?', 'y⁴ : y⁶ = yᵏ. Wie groß ist k?', '10¹ : 10⁹ = 10ᵏ. Wie groß ist k?']


def nach_b(a): return _mit_minus_exponent(a) or a['f']['text'] in NEGATIV_ERGEBNIS


def umzug_nach_b():
    d = start_a()
    xs = [a for a in d['aufgaben'] if nach_b(a)]
    assert sum(1 for a in xs if _mit_minus_exponent(a)) == 22 and len(xs) == 29, len(xs)
    return xs


# Ersatz in Flug A: gleiche Karte, gleicher Pool, gleiche Stufe, gleicher Typ – natürliche Exponenten.
_HK = 'Alle Potenzen haben dieselbe Basis. Was machst du mit den Exponenten?'
ERSATZ_A = {
    'mal_gleiche_basis': [
        ('z³ · z⁻⁵ = zᵏ. Wie groß ist k?', Z('x⁴ · x² · x³ = xᵏ. Wie groß ist k?', 9, '4 + 2 + 3', 'Gleiche Basis x: Exponenten addieren, 4 + 2 + 3 = 9. Also x⁹.', _HK)),
        ('y⁻³ · y⁻¹ = yᵏ. Wie groß ist k?', Z('b² · b⁵ · b = bᵏ. Wie groß ist k?', 8, '2 + 5 + 1', 'b allein ist b¹. Exponenten addieren: 2 + 5 + 1 = 8. Also b⁸.', 'Welchen Exponenten hat b ohne Hochzahl?')),
        ('10⁻¹ · 10⁵ · 10² = 10ᵏ. Wie groß ist k?', Z('10³ · 10 · 10⁴ = 10ᵏ. Wie groß ist k?', 8, '3 + 1 + 4', '10 = 10¹. Exponenten addieren: 3 + 1 + 4 = 8. Also 10⁸.', 'Schreibe die einzelne 10 als Zehnerpotenz.')),
        ('3⁻² · 3⁻³ · 3⁻¹ = 3ᵏ. Wie groß ist k?', Z('2² · 2³ · 2⁴ = 2ᵏ. Wie groß ist k?', 9, '2 + 3 + 4', 'Gleiche Basis 2: Exponenten addieren, 2 + 3 + 4 = 9. Also 2⁹.', _HK)),
        ('Berechne 10⁶ · 10⁻⁸ und gib das Ergebnis als Dezimalzahl an.',
         Z('Berechne 10² · 10⁴ mit dem Potenzgesetz. Gib das Ergebnis als Zahl an.', 1000000, '10 ** (2 + 4)', '10² · 10⁴ = 10²⁺⁴ = 10⁶ = 1 000 000.', 'Fasse zuerst zu einer Zehnerpotenz zusammen.')),
        ('Berechne 10² · 10⁻⁸ und gib das Ergebnis als Dezimalzahl an.',
         Z('Berechne 3² · 3² · 3 mit dem Potenzgesetz. Gib das Ergebnis als Zahl an.', 243, '3 ** (2 + 2 + 1)', '3² · 3² · 3¹ = 3²⁺²⁺¹ = 3⁵ = 243.', 'Fasse zuerst zu einer Potenz von 3 zusammen.')),
        ('3⁴ · 3⁻⁶ = 3ᵏ. Wie groß ist k?', Z('4³ · 4 · 4² = 4ᵏ. Wie groß ist k?', 6, '3 + 1 + 2', '4 = 4¹. Exponenten addieren: 3 + 1 + 2 = 6. Also 4⁶.', 'Welchen Exponenten hat die einzelne 4?')),
        ('b³ · b⁻⁵ = bᵏ. Wie groß ist k?', Z('b⁴ · b³ = bᵏ. Wie groß ist k?', 7, '4 + 3', 'Gleiche Basis b: Exponenten addieren, 4 + 3 = 7.')),
        ('a³ · a⁻⁵ = aᵏ. Wie groß ist k?', Z('a² · a⁷ = aᵏ. Wie groß ist k?', 9, '2 + 7', 'Gleiche Basis a: Exponenten addieren, 2 + 7 = 9.')),
        ('10³ · 10⁻² · 10⁵ = 10ᵏ. Wie groß ist k?', Z('10² · 10³ · 10⁴ = 10ᵏ. Wie groß ist k?', 9, '2 + 3 + 4', 'Gleiche Basis 10: Exponenten addieren, 2 + 3 + 4 = 9.')),
        ('b⁻³ · b⁻¹ = bᵏ. Wie groß ist k?', Z('b⁴ · b · b² = bᵏ. Wie groß ist k?', 7, '4 + 1 + 2', 'b = b¹. Exponenten addieren: 4 + 1 + 2 = 7.')),
        ('b⁻³ · b⁻⁵ = bᵏ. Wie groß ist k?', Z('x³ · x⁵ = xᵏ. Wie groß ist k?', 8, '3 + 5', 'Gleiche Basis x: Exponenten addieren, 3 + 5 = 8.')),
        ('a⁻² · a⁻² = aᵏ. Wie groß ist k?', Z('y⁶ · y⁶ = yᵏ. Wie groß ist k?', 12, '6 + 6', 'Gleiche Basis y: Exponenten addieren, 6 + 6 = 12.')),
    ],
    'gleicher_exponent': [
        ('Berechne geschickt: 2⁻¹ · 5⁻¹ und gib das Ergebnis als Dezimalzahl an.',
         Z('Berechne geschickt: 0,2⁵ · 50⁵', 100000, '(0.2 * 50) ** 5', '0,2⁵ · 50⁵ = (0,2 · 50)⁵ = 10⁵ = 100 000.', 'Gleicher Exponent: Was ergibt 0,2 · 50?')),
        ('Berechne geschickt: 5⁻¹ · 20⁻¹ und gib das Ergebnis als Dezimalzahl an.',
         Z('Berechne geschickt: 2,5² · 4² · 10²', 10000, '(2.5 * 4 * 10) ** 2', '2,5² · 4² · 10² = (2,5 · 4 · 10)² = 100² = 10 000.', 'Alle drei Potenzen haben denselben Exponenten.')),
    ],
    'geteilt_gleiche_basis': [
        ('a⁻³ : a³ = aᵏ. Wie groß ist k?', Z('z⁹ : z² : z³ = zᵏ. Wie groß ist k?', 4, '9 - 2 - 3', 'Von links: z⁹ : z² = z⁷, dann z⁷ : z³ = z⁴. Also k = 9 − 2 − 3 = 4.', 'Teile Schritt für Schritt von links nach rechts.')),
        ('3⁴ : 3⁸ = 3ᵏ. Wie groß ist k?', Z('a⁶ · a⁴ : a⁷ = aᵏ. Wie groß ist k?', 3, '6 + 4 - 7', 'a⁶ · a⁴ = a¹⁰, dann a¹⁰ : a⁷ = a³. Also k = 3.', 'Erst malnehmen (Exponenten addieren), dann teilen (subtrahieren).')),
        ('z⁻² : z⁵ = zᵏ. Wie groß ist k?', Z('2⁴ · 2⁵ : 2⁶ = 2ᵉ. Wie groß ist e?', 3, '4 + 5 - 6', '2⁴ · 2⁵ = 2⁹, dann 2⁹ : 2⁶ = 2³. Also e = 3.', 'Erst malnehmen (Exponenten addieren), dann teilen (subtrahieren).')),
        ('2¹ : 2⁷ = 2ᵏ. Wie groß ist k?', Z('Berechne 10⁷ : 10³. Gib das Ergebnis als Zahl an.', 10000, '10 ** (7 - 3)', '10⁷ : 10³ = 10⁷⁻³ = 10⁴ = 10 000.', 'Fasse zuerst zu einer Zehnerpotenz zusammen.')),
        ('Berechne 10¹ : 10⁶ und gib das Ergebnis als Dezimalzahl an.',
         Z('x¹² : x⁵ : x⁴ = xᵏ. Wie groß ist k?', 3, '12 - 5 - 4', 'x¹² : x⁵ = x⁷, dann x⁷ : x⁴ = x³. Also k = 3.', 'Teile Schritt für Schritt von links nach rechts.')),
        ('b⁻² : b⁶ = bᵏ. Wie groß ist k?', Z('b⁹ : b³ = bᵏ. Wie groß ist k?', 6, '9 - 3', 'Gleiche Basis b: Exponenten subtrahieren, 9 − 3 = 6.')),
        ('5⁴ : 5⁶ = 5ᵏ. Wie groß ist k?', Z('5⁸ : 5³ = 5ᵏ. Wie groß ist k?', 5, '8 - 3', 'Gleiche Basis 5: Exponenten subtrahieren, 8 − 3 = 5.')),
        ('2¹ : 2⁸ = 2ᵏ. Wie groß ist k?', Z('2⁹ : 2² = 2ᵏ. Wie groß ist k?', 7, '9 - 2', 'Gleiche Basis 2: Exponenten subtrahieren, 9 − 2 = 7.')),
        ('y¹ : y⁻² = yᵏ. Wie groß ist k?', Z('y⁷ : y = yᵏ. Wie groß ist k?', 6, '7 - 1', 'y = y¹. Exponenten subtrahieren: 7 − 1 = 6.')),
        ('y⁴ : y⁶ = yᵏ. Wie groß ist k?', Z('y⁸ : y⁵ = yᵏ. Wie groß ist k?', 3, '8 - 5', 'Gleiche Basis y: Exponenten subtrahieren, 8 − 5 = 3.')),
        ('a⁻³ : a⁴ = aᵏ. Wie groß ist k?', Z('a¹⁰ : a⁴ = aᵏ. Wie groß ist k?', 6, '10 - 4', 'Gleiche Basis a: Exponenten subtrahieren, 10 − 4 = 6.')),
        ('y⁷ : y⁻⁴ = yᵏ. Wie groß ist k?', Z('x⁹ : x² = xᵏ. Wie groß ist k?', 7, '9 - 2', 'Gleiche Basis x: Exponenten subtrahieren, 9 − 2 = 7.')),
        ('10¹ : 10⁹ = 10ᵏ. Wie groß ist k?', Z('10⁹ : 10⁵ = 10ᵏ. Wie groß ist k?', 4, '9 - 5', 'Gleiche Basis 10: Exponenten subtrahieren, 9 − 5 = 4.')),
        ('x⁻⁴ : x⁷ = xᵏ. Wie groß ist k?', Z('b¹¹ : b³ = bᵏ. Wie groß ist k?', 8, '11 - 3', 'Gleiche Basis b: Exponenten subtrahieren, 11 − 3 = 8.')),
    ],
}
# Nur Lösungsweg und Tipp neu (Frage und Lösung bleiben): kommen ohne negativen Exponenten aus.
WEG_A = [
    ('geteilt_gleiche_basis', '2¹⁰ : 2ⁿ = 1/4. Wie groß ist n?',
     {'w': '2¹⁰ : 2ⁿ = 1/4 heißt: 2ⁿ ist 4-mal so groß wie 2¹⁰. Also 2ⁿ = 2¹⁰ · 2² = 2¹² und n = 12.',
      'h': 'Wie viel Mal so groß wie 2¹⁰ muss 2ⁿ sein?'}),
    ('geteilt_gleiche_basis', 'Berechne 10⁴ : 10⁴ : 10⁴ · 10⁸.',
     {'w': 'Von links: 10⁴ : 10⁴ = 1, dann 1 : 10⁴ = 1/10 000, dann 1/10 000 · 10⁸ = 10⁸ : 10⁴ = 10⁴ = 10 000.',
      'h': 'Rechne von links nach rechts. Was ergibt 10⁴ : 10⁴?'}),
]

# Aus terme.potenzgesetze/fehler_finden (Gym 6): Aufgaben, die ein Potenzgesetz voraussetzen → Übungen vom Typ „fehler“.
_TF_MAL = 'Schreib beide Potenzen aus und zähle die Faktoren.'
_TF_TEIL = 'Schreib beide Potenzen aus. Wie viele Faktoren kürzen sich weg?'
_TF_GLEICH = 'Bilde Paare aus je einem Faktor jeder Basis.'
GYM6_NACH_A = [
    ('Stimmt die Rechnung? 5² · 5² = 5⁴', 'mal_gleiche_basis', None),
    ('Ein Kind rechnet: 3⁹ : 3³ = 3³. Welcher Satz beschreibt den Fehler richtig?', 'geteilt_gleiche_basis', None),
    ('Stimmt die Rechnung? 4⁵ : 4² = 4³', 'geteilt_gleiche_basis', None),
    ('Stimmt die Rechnung? 4⁴ · 4² = 4⁶', 'mal_gleiche_basis', None),
    ('Stimmt die Rechnung? 2⁴ · 2³ = 2⁷', 'mal_gleiche_basis', None),
    ('Ein Kind rechnet: 2² · 5² = 10⁴. Was ist falsch?', 'gleicher_exponent', None),
    ('Ein Kind rechnet: 2³ · 5³ = 10⁶. Was ist falsch?', 'gleicher_exponent', None),
    ('Ein Kind rechnet: 3³ · 3³ = 9⁶. Welcher Satz beschreibt den Fehler richtig?', 'mal_gleiche_basis', None),
    ('Ein Kind rechnet: 4³ · 4² = 16⁵. Welcher Satz beschreibt den Fehler richtig?', 'mal_gleiche_basis', None),
    ('Stimmt die Rechnung? 5² · 5³ = 5⁶', 'mal_gleiche_basis', _TF_MAL),                       # vorher Test
    ('Ein Kind rechnet: 3⁴ · 3⁴ = 9⁸. Was ist falsch?', 'mal_gleiche_basis', _TF_MAL),          # vorher Korrektur
    ('Ein Kind rechnet: 2⁴ · 5⁴ = 10⁸. Was ist falsch?', 'gleicher_exponent', _TF_GLEICH),      # vorher Korrektur
    ('Stimmt die Rechnung? 4⁷ : 4⁴ = 4³', 'geteilt_gleiche_basis', _TF_TEIL),                  # vorher Sicherung
    ('Stimmt die Rechnung? 5⁵ : 5² = 5³', 'geteilt_gleiche_basis', _TF_TEIL),                  # vorher Sicherung
    ('Ein Kind rechnet: 4⁴ · 4² = 4⁸. Was ist falsch?', 'mal_gleiche_basis', _TF_MAL),          # vorher Sicherung
    ('Ein Kind rechnet: 5⁴ · 5⁴ = 5¹⁶. Was ist falsch?', 'mal_gleiche_basis', _TF_MAL),         # vorher Sicherung
    ('Ein Kind rechnet: 5⁶ : 5² = 5³. Was ist falsch?', 'geteilt_gleiche_basis', _TF_TEIL),     # vorher Sicherung
    ('Ein Kind rechnet: 4³ · 4³ = 4⁹. Welcher Satz beschreibt den Fehler richtig?', 'mal_gleiche_basis', None),
    ('Ein Kind rechnet: 4⁴ · 4² = 16⁶. Welcher Satz beschreibt den Fehler richtig?', 'mal_gleiche_basis', None),
    ('Welche Rechnung ist richtig?', 'anwenden', None),
    ('Die Regel „a² · a³ = a⁶“ ist falsch. Für welche Zahlen a stimmt sie trotzdem?', 'mal_gleiche_basis', None),
    ('Ein Kind hat bei aᵏ · a² die Exponenten malgenommen und a¹² erhalten. Was wäre der richtige Exponent gewesen?', 'mal_gleiche_basis', None),
    ('Ein Kind schreibt 2⁵ + 2⁵ = 2¹⁰. Richtig ist 2ᵏ. Wie groß ist k?', 'mal_gleiche_basis', None),  # vorher Knobel
]
# Antworten dieser Aufgaben, die mit negativen Exponenten argumentieren (Flug A hat nur natürliche Exponenten): durch typische
# Fehler mit natürlichen Exponenten ersetzen. Frage und richtige Antwort bleiben.
ANTWORT_A = {
    'Ein Kind rechnet: 2² · 5² = 10⁴. Was ist falsch?': ('Ein negativer Exponent bedeutet Kehrbruch, keine negative Zahl: 5⁻² = 1/25.', 'Die Basen werden addiert: 7².'),
    'Ein Kind rechnet: 4⁴ · 4² = 4⁸. Was ist falsch?': ('Ein negativer Exponent bedeutet Kehrbruch, keine negative Zahl: 4⁻⁴ = 1/256.', 'Die Basen werden malgenommen: 16⁶.'),
    'Ein Kind rechnet: 5⁴ · 5⁴ = 5¹⁶. Was ist falsch?': ('Ein negativer Exponent bedeutet Kehrbruch, keine negative Zahl: 5⁻⁴ = 1/625.', 'Die Basen werden malgenommen: 25⁸.'),
    'Ein Kind rechnet: 5⁶ : 5² = 5³. Was ist falsch?': ('Ein negativer Exponent bedeutet Kehrbruch, keine negative Zahl: 5⁻³ = 1/125.', 'Die Exponenten werden addiert: 5⁸.'),
}


def gym6_nach_a():
    """Die Aufgaben aus fehler_finden (Stand vor dem Bereinigen = heutiger Stand der Karte), als Übung „fehler“ für Flug A."""
    q = BR.roh('terme.potenzgesetze')
    ff = {a['f']['text']: a for a in q['aufgaben'] if a['l'] == 'fehler_finden'}
    aus = []
    for text, lz, tipp in GYM6_NACH_A:
        a = copy.deepcopy(ff[text])
        alt = {'p': a['p'], 's': a['s'], 'g': a.get('g')}
        a.update({'l': lz, 't': lz, 'p': 'uebung', 's': 3, 'g': 'fehler'})
        if not a.get('h'):
            assert tipp, text
            a['h'] = tipp
        if text in ANTWORT_A:
            vorher, nachher = ANTWORT_A[text]
            a['a'] = [nachher if x == vorher else x for x in a['a']]
            assert nachher in a['a'] and a['o']['index'] != a['a'].index(nachher), text
        aus.append((a, alt))
    assert len(aus) == 23
    return aus


def flug_a():
    thema = 'terme.potenzgesetze_natuerlich'
    d = start_a()
    weg_b = [a['f']['text'] for a in d['aufgaben'] if nach_b(a)]
    for lz, paare in ERSATZ_A.items():
        for alt, neu in paare: _ersetzen(d, thema, lz, alt, neu)
    for lz, text, felder in WEG_A: _ersetzen(d, thema, lz, text, felder, felder=list(felder))
    assert not [a for a in d['aufgaben'] if nach_b(a)], 'negativer Exponent übrig'
    BERICHT[thema]['nach_b'] = weg_b
    for a, alt in gym6_nach_a():
        assert a['f']['text'] not in {x['f']['text'] for x in d['aufgaben']}, a['f']['text']
        d['aufgaben'].append(a)
        BERICHT[thema]['aus_gym6'].append({'lz': a['l'], 'vorher': alt, 'text': a['f']['text']})
    for lz in LZ_A:
        _ordnen_karte(d, lz)
        _regeln(d, lz, je_typ_satzbau=True)
    rest = [a['f']['text'] for a in d['aufgaben'] if NEG.search(json.dumps([a['f'], a.get('a'), a.get('w'), a.get('h')], ensure_ascii=False))]
    assert not rest, f'negativer Exponent in Flug A: {rest}'
    inh = d['inhalt']
    inh['abschnitte'] = [{'titel': 'Potenzen malnehmen', 'lernziele': ['mal_gleiche_basis', 'gleicher_exponent']},
                         {'titel': 'Vertiefung: teilen und geschickt rechnen', 'lernziele': ['geteilt_gleiche_basis', 'anwenden']}]
    out = {'thema_schluessel': thema, 'thema_id': 102, 'block_id': 62, 'klasse': {'gym_by': 7, 'rs_by': 7, 'ib_myp': 4},
           'autor': 'Claude (Sechsundzwanzigste Runde, Generator terme.potenzgesetze_natuerlich.py; Lernkarten aus terme.umformen)',
           'inhalt': {
               'ziel': 'Potenzen mit natürlichen Exponenten zusammenfassen: bei gleicher Basis malnehmen (Vertiefung: teilen), bei gleichem '
                       'Exponenten die Basen zusammenfassen und die Gesetze geschickt nutzen. Vorwissen: Potenzen aus Klasse 6 (Basis, Exponent, '
                       'Hoch 0). Die Gesetze mit negativen Exponenten folgen in Klasse 8 im Flug „Potenzgesetze mit ganzzahligen Exponenten“.',
               'merke': ['Gleiche Basis: aᵐ · aⁿ = aᵐ⁺ⁿ (malnehmen) und aᵐ : aⁿ = aᵐ⁻ⁿ (teilen).', 'Gleicher Exponent: aⁿ · bⁿ = (a · b)ⁿ.',
                         'Erst prüfen: gleiche Basis oder gleicher Exponent? Sonst ausrechnen.'],
               'abschnitte': inh['abschnitte'], 'etappen': inh['etappen'], 'teilfaehigkeiten': inh['teilfaehigkeiten'],
               'bewertung': {**inh['bewertung'], 'testaufgaben_je_lernziel': 1},
               'quellen': {'erklaerungen': 'Lernkarten unverändert aus terme.umformen (dorthin in der Einundzwanzigsten Runde aus terme.potenzgesetze).',
                           'aufgaben': 'Vom Generator erzeugt und berechnet; Umzug und Ersatz: Sechsundzwanzigste Runde.',
                           'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern (Gymnasium, Jahrgangsstufe 7, M7 1.2).'}},
           'aufgaben': d['aufgaben'],
           'offen': ['Sechsundzwanzigste Runde: Die vier Lernkarten stammen aus terme.umformen (Lernziel-Schlüssel unverändert, damit der Lernstand '
                     'umgehängt werden kann). 29 Aufgaben mit negativem Exponenten (22 im Fragetext, 7 mit negativem Ergebnis-Exponenten) sind '
                     'nach terme.potenzgesetze_ganzzahlig umgezogen und hier durch Aufgaben mit natürlichen Exponenten ersetzt (gleiche Karte, '
                     'gleicher Pool, gleiche Stufe, gleicher Typ). Dazu 23 Aufgaben aus „Fehler finden“ von terme.potenzgesetze als Übungen vom Typ „fehler“.',
                     'Lehrplan M7 1.2 nennt auch „Potenzen von Potenzen“ mit natürlichen Exponenten. Dafür gibt es hier (noch) keine Lernkarte; '
                     'die Regel (aᵐ)ⁿ = aᵐ·ⁿ steht in Flug B (Karte exponent_und_potenz). Vorschlag: eigene Karte in Flug A, falls gewünscht.',
                     'Quotienten von Potenzen (geteilt_gleiche_basis) und anwenden bleiben Vertiefung wie bisher.']}
    return _schreiben(thema, out)


# =====================================================================================================================
# terme.umformen – die vier Karten entfallen
# =====================================================================================================================
def umformen_datei():
    thema = 'terme.umformen'
    pfad = THEMEN / f'{thema}.json'
    roh_text = pfad.read_text(encoding='utf-8')
    d = json.loads(roh_text)
    vorher = copy.deepcopy(d)
    for lz in LZ_A:
        xs = BR._karte_entfernen(d, lz)
        BERICHT[thema]['entfaellt'].append({'lz': lz, 'aufgaben': len(xs)})
    assert sum(x['aufgaben'] for x in BERICHT[thema]['entfaellt']) == 168
    inh = d['inhalt']
    inh['ziel'] = ('Terme vereinfachen: gleichartige Glieder zusammenfassen, Produkte vereinfachen, Klammern auflösen und ausmultiplizieren, '
                   'ausklammern, Äquivalenz prüfen und die binomischen Formeln anwenden. Die Potenzgesetze stehen im Flug „Potenzgesetze“.')
    inh['merke'] = [m for m in inh['merke'] if not m.startswith('Gleiche Basis:')]
    d['offen'] = d.get('offen', []) + ['Sechsundzwanzigste Runde (20.11.): Die vier Potenz-Lernkarten (mal_gleiche_basis, gleicher_exponent, '
                                       'geteilt_gleiche_basis, anwenden) sind mit ihren Lernziel-Schlüsseln in den Flug terme.potenzgesetze_natuerlich '
                                       '(thema_id 102) umgezogen. Hier bleiben 8 Lernkarten.']
    # Nachweis: die übrigen 8 Karten und ihre Aufgaben Zeichen für Zeichen gleich
    assert [e for e in vorher['inhalt']['etappen'] if e['lernziel'] not in LZ_A] == inh['etappen']
    assert [a for a in vorher['aufgaben'] if a['l'] not in LZ_A] == d['aufgaben']
    assert len(inh['etappen']) == 8
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh_text.endswith('\n') else ''), encoding='utf-8')
    f, w, info = pruefe(pfad)
    assert not f, '; '.join(f[:8])
    print(f'  POTENZ-TEILEN {thema}: {info}')
    return d


# =====================================================================================================================
# terme.potenzgesetze (Gym 6) – „Fehler finden“ nur noch zu Potenzbegriff, Hoch 0 und negativem Exponenten
# =====================================================================================================================
_FF_B = 'Schreib die Potenz als Produkt aus.'
GYM6_NEU = [
    U('fehler', L('Ein Kind rechnet 3⁻² = −9. Wie heißt das richtige Ergebnis?', '□/□', [1, 9], ['1', '3 ** 2'],
                  '3⁻² ist der Kehrbruch von 3² = 9, also 3⁻² = 1/9. Das Ergebnis ist positiv.', 'Was bedeutet ein Minus im Exponenten?', hinweis=BRUCH)),
    U('fehler', L('Ein Kind rechnet (2/3)² = 4/3. Wie heißt das richtige Ergebnis?', '□/□', [4, 9], ['2 ** 2', '3 ** 2'],
                  '(2/3)² = 2/3 · 2/3 = (2 · 2)/(3 · 3) = 4/9. Das Kind hat den Nenner nicht quadriert.', _FF_B, hinweis=BRUCH)),
    U('rueckwaerts', Z('Ein Kind sollte 2ⁿ ausrechnen. Es hat aus Versehen 2 · n gerechnet und 10 erhalten. Welches Ergebnis wäre richtig gewesen?',
                       32, '2 ** (10 // 2)', '2 · n = 10, also n = 5. Richtig ist 2⁵ = 2 · 2 · 2 · 2 · 2 = 32.', 'Finde zuerst n aus der falschen Rechnung.')),
    U('parameter', Z('Für wie viele natürliche Zahlen n von 1 bis 10 ist (−2)ⁿ negativ?', 5, '(10 + 1) // 2',
                     '(−2)ⁿ ist negativ, wenn n ungerade ist: n = 1, 3, 5, 7, 9. Das sind 5 Zahlen.', 'Probiere n = 1, 2, 3: Wann ist das Ergebnis negativ?')),
    U('transfer', Z('In einem Datenblatt steht: Dicke 10⁻³ m. Ein Kind meint, das sei eine negative Dicke. Wie viele Millimeter sind 10⁻³ m wirklich?',
                    1, '10 ** -3 * 1000', '10⁻³ m = 1/10³ m = 1/1 000 m = 1 mm. Die Dicke ist positiv.', 'Schreibe 10⁻³ als Bruch.', einheit='mm')),
    K(Z('Ein Kind behauptet: (−1)¹⁰⁰ + (−1)¹⁰¹ + 1⁻¹⁰⁰ = 3. Was kommt wirklich heraus?', 1, '(-1) ** 100 + (-1) ** 101 + 1 ** -100',
        '(−1)¹⁰⁰ = 1 (gerader Exponent), (−1)¹⁰¹ = −1 (ungerader Exponent), 1⁻¹⁰⁰ = 1/1¹⁰⁰ = 1. Zusammen: 1 − 1 + 1 = 1.',
        'Wann ist eine Potenz von −1 positiv, wann negativ?')),
    T(A('Ein Kind rechnet: 10⁻² = −100. Was ist falsch?', 'Ein negativer Exponent bedeutet Kehrbruch: 10⁻² = 1/100 = 0,01.',
        ['Nichts, die Rechnung ist richtig.', 'Richtig wäre −20, denn man rechnet 10 · (−2).', 'Richtig wäre 1/20.'],
        '10⁻² = 1/10² = 1/100 = 0,01. Das Ergebnis ist positiv.')),
    KO(Z('Ein Kind rechnet 0,3² = 0,9. Wie heißt das richtige Ergebnis?', 0.09, '0.3 ** 2', '0,3² = 0,3 · 0,3 = 0,09 (zwei Nachkommastellen).')),
    KO(A('Stimmt die Rechnung? 7⁰ = 7', 'Nein, jede Zahl außer 0 hoch 0 ergibt 1: 7⁰ = 1.', ['Ja, das stimmt.', 'Das kann man nicht entscheiden.'],
         'Nein, jede Zahl außer 0 hoch 0 ergibt 1: 7⁰ = 1.')),
    SI(Z('Ein Kind rechnet 2⁻⁴ = −16. Wie heißt das richtige Ergebnis als Dezimalzahl?', 0.0625, '2 ** -4', '2⁻⁴ = 1/2⁴ = 1/16 = 0,0625.')),
    SI(Z('Ein Kind rechnet (−3)² = −9. Wie heißt das richtige Ergebnis?', 9, '(-3) ** 2', '(−3)² = (−3) · (−3) = 9.')),
    SI(Z('Ein Kind rechnet 4³ = 12. Wie heißt das richtige Ergebnis?', 64, '4 ** 3', '4³ = 4 · 4 · 4 = 64. Das Kind hat 4 · 3 gerechnet.')),
    SI(A('Stimmt die Rechnung? (−2)³ = −8', 'Ja, (−2) · (−2) · (−2) = −8.', ['Nein, richtig ist 8.', 'Nein, richtig ist −6.'],
         '(−2) · (−2) = 4 und 4 · (−2) = −8. Ungerader Exponent, negative Basis: negativ.')),
    SI(Z('Ein Kind rechnet −2⁴ = 16. Wie heißt das richtige Ergebnis?', -16, '-(2 ** 4)', '−2⁴ = −(2 · 2 · 2 · 2) = −16. Nur (−2)⁴ wäre 16.')),
]
# Antworten, die Potenzgesetze nennen (in Klasse 6 unbekannt), durch typische Fehler beim negativen Exponenten ersetzen.
GYM6_ANTWORTEN = {
    'Ein Kind rechnet: 4⁻³ = −64. Was ist falsch?': {'Exponenten subtrahieren, nicht teilen: 4⁸.': 'Richtig wäre −12, denn man rechnet 4 · (−3).',
                                                     'Gleicher Exponent: Basen malnehmen, der Exponent bleibt: 10³.': 'Richtig wäre 1/12.'},
    'Ein Kind rechnet: 4⁻⁴ = −256. Was ist falsch?': {'Die Basis bleibt 4, nur die Exponenten werden addiert: 4⁸.': 'Richtig wäre −16, denn man rechnet 4 · (−4).',
                                                      'Gleicher Exponent: Basen malnehmen, der Exponent bleibt: 10⁴.': 'Richtig wäre 1/16.'},
    'Ein Kind rechnet: 5⁻⁴ = −625. Was ist falsch?': {'Exponenten subtrahieren, nicht teilen: 5⁹.': 'Richtig wäre −20, denn man rechnet 5 · (−4).',
                                                      'Gleicher Exponent: Basen malnehmen, der Exponent bleibt: 10⁴.': 'Richtig wäre 1/20.'},
    'Ein Kind rechnet: 5⁻² = −25. Was ist falsch?': {'Die Basis bleibt 5, nur die Exponenten werden addiert: 5⁶.': 'Richtig wäre −10, denn man rechnet 5 · (−2).',
                                                     'Exponenten subtrahieren, nicht teilen: 5⁴.': 'Richtig wäre 1/10.'},
    'Ein Kind rechnet: 2⁻³ = −8. Was ist falsch?': {'Die Exponenten werden addiert, nicht malgenommen: 2⁶.': 'Richtig wäre −6, denn man rechnet 2 · (−3).',
                                                    'Gleicher Exponent: Basen malnehmen, der Exponent bleibt: 10³.': 'Richtig wäre 1/6.'},
}
GYM6_KARTE = {
    'einstieg': 'Ein Freund rechnet 2⁴ = 2 · 4 = 8. Du prüfst das, indem du die Potenz ausschreibst und ausrechnest. '
                'Das ist eine ⟦Zahlenprobe⟧.',
    'woerter': [['Zahlenprobe', 'beide Seiten mit Zahlen ausrechnen und vergleichen']],
    'bild': {'typ': 'tabelle', 'kopf': ['Rechnung', 'Wert'], 'zeilen': [['2 · 4', '?'], ['2⁴', '?']]},
    'schritte': [{'text': 'Der Freund rechnet 2 · 4 = 8.', 'bild': {'zeilen': [['2 · 4', '8'], ['2⁴', '?']]}},
                 {'text': 'Ausgeschrieben ist 2⁴ = 2 · 2 · 2 · 2.', 'bild': {'zeilen': [['2 · 4', '8'], ['2⁴ = 2 · 2 · 2 · 2', '?']]}},
                 {'text': 'Das ergibt ⟦16⟧, nicht 8. Der Exponent zählt die Faktoren.',
                  'bild': {'zeilen': [['2 · 4', '8'], ['2⁴ = 2 · 2 · 2 · 2', '16']]}}],
    'fehler': 'Bei 2⁻³ denken viele an eine negative Zahl. Das ist falsch: 2⁻³ = 1/2³ = 1/8 ist positiv.',
    'fehler_bild': {'zeilen': [['2⁻³', '−8 (falsch)'], ['2⁻³ = 1/2³', '1/8']]},
    'regel': 'Prüfe Potenzen mit einer ⟦Zahlenprobe⟧. Der Exponent zählt die Faktoren, ein Minus davor heißt Kehrbruch.',
}


def gym6_datei():
    thema = 'terme.potenzgesetze'
    pfad = THEMEN / f'{thema}.json'
    roh_text = pfad.read_text(encoding='utf-8')
    d = json.loads(roh_text)
    vorher = copy.deepcopy(d)
    weg_texte = {t for t, _, _ in GYM6_NACH_A}
    weg = [a for a in d['aufgaben'] if a['l'] == 'fehler_finden' and a['f']['text'] in weg_texte]
    assert len(weg) == 23
    d['aufgaben'] = [a for a in d['aufgaben'] if not (a['l'] == 'fehler_finden' and a['f']['text'] in weg_texte)]
    BERICHT[thema]['nach_a'] = [{'p': a['p'], 's': a['s'], 'g': a.get('g'), 'text': a['f']['text']} for a in weg]
    for a in d['aufgaben']:
        if a['l'] == 'fehler_finden' and a['f']['text'] in GYM6_ANTWORTEN:
            ers = GYM6_ANTWORTEN[a['f']['text']]
            assert all(x in a['a'] for x in ers) and a['a'][a['o']['index']] not in ers
            a['a'] = [ers.get(x, x) for x in a['a']]
            BERICHT[thema]['antworten'].append(a['f']['text'])
    assert len(BERICHT[thema]['antworten']) == 5
    texte = {a['f']['text'] for a in d['aufgaben']}
    for p, g, a in GYM6_NEU:
        x = _aufgabe('fehler_finden', p, g, a)
        x['t'] = 'fehler_finden'
        assert x['f']['text'] not in texte, x['f']['text']
        texte.add(x['f']['text'])
        d['aufgaben'].append(x)
        BERICHT[thema]['neu'].append({'p': p, 's': x['s'], 'g': g, 'text': x['f']['text']})
    # Lösungsweg ohne Potenzgesetz (Ergebnis bleibt): negativer_exponent, „Wie viel Mal so groß ist 2² wie 2⁻²?“
    _ersetzen(d, thema, 'negativer_exponent', 'Wie viel Mal so groß ist 2² wie 2⁻²?',
              {'w': '2² = 4 und 2⁻² = 1/4. 4 : 1/4 = 4 · 4 = 16.'}, felder=['w'])
    _ersetzen(d, thema, 'fehler_finden', 'Ein Kind rechnet 2³ + 2³ = 2⁶. Welche Zahl ist richtig?',
              {'h': 'Rechne beide Potenzen aus und addiere dann.'}, felder=['h'])
    e = next(e for e in d['inhalt']['etappen'] if e['lernziel'] == 'fehler_finden')
    e.update(copy.deepcopy(GYM6_KARTE))
    _ordnen_karte(d, 'fehler_finden')
    _regeln(d, 'fehler_finden')
    rest = json.dumps([a for a in d['aufgaben'] if a['l'] == 'fehler_finden'] + [e], ensure_ascii=False)
    assert not re.search(r'Exponenten (werden )?(addier|subtrah|malgenommen)|Gleicher Exponent|Basis bleibt|Potenzgesetz', rest), 'Potenzgesetz übrig'
    inh = d['inhalt']
    inh['ziel'] = ('Potenzen mit natürlichen und negativen ganzzahligen Exponenten verstehen und berechnen, auch mit Brüchen, Dezimalzahlen '
                   'und negativer Basis. Die Potenzgesetze folgen in Klasse 7 im Flug „Potenzgesetze“.')
    d['offen'] = [d['offen'][0], d['offen'][2],
                  'Sechsundzwanzigste Runde (20.11.): Die Potenzgesetze stehen in eigenen Flügen (terme.potenzgesetze_natuerlich, Klasse 7; '
                  'terme.potenzgesetze_ganzzahlig, Klasse 8). Die 23 Aufgaben aus „Fehler finden“, die ein Potenzgesetz voraussetzen, sind nach '
                  'terme.potenzgesetze_natuerlich umgezogen; „Fehler finden“ ist mit 14 neuen Aufgaben zu Potenzbegriff, Hoch 0 und negativem '
                  'Exponenten wieder aufgefüllt, Erklärung der Karte neu (Zahlenprobe 2⁴ statt Potenzgesetz).']
    # Nachweis: die anderen Karten unverändert (bis auf den einen Lösungsweg)
    for e0 in vorher['inhalt']['etappen']:
        if e0['lernziel'] != 'fehler_finden': assert e0 in inh['etappen']
    alt_rest = [a for a in vorher['aufgaben'] if a['l'] != 'fehler_finden']
    neu_rest = [a for a in d['aufgaben'] if a['l'] != 'fehler_finden']
    assert len(alt_rest) == len(neu_rest) and sum(1 for x, y in zip(alt_rest, neu_rest) if x != y) == 1  # nur der Lösungsweg oben
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh_text.endswith('\n') else ''), encoding='utf-8')
    f, w, info = pruefe(pfad)
    assert not f, '; '.join(f[:8])
    print(f'  POTENZ-TEILEN {thema}: {info}')
    (Path('/tmp') / f'potenz_teilen_{thema}.json').write_text(json.dumps(BERICHT[thema], ensure_ascii=False, indent=1))
    return d

