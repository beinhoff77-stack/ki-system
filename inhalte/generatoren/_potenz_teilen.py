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


# … und (Achtundzwanzigste Runde, Prüfbericht Sollte 2) 2 weitere mit kleinerem erstem Exponenten im Rechenweg (2⁻² bzw. 10⁻⁴).
ERSTER_KLEINER = ['2¹⁰ : 2ⁿ = 1/4. Wie groß ist n?', 'Berechne 10⁴ : 10⁴ : 10⁴ · 10⁸.']


def nach_b(a): return _mit_minus_exponent(a) or a['f']['text'] in NEGATIV_ERGEBNIS + ERSTER_KLEINER


def umzug_nach_b():
    d = start_a()
    xs = [a for a in d['aufgaben'] if nach_b(a)]
    assert sum(1 for a in xs if _mit_minus_exponent(a)) == 22 and len(xs) == 31, len(xs)
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
        # Achtundzwanzigste Runde (Sollte 2): erster Exponent nie kleiner
        ('2¹⁰ : 2ⁿ = 1/4. Wie groß ist n?', Z('2¹⁰ : 2ⁿ = 16. Wie groß ist n?', 6, '10 - 4', '16 = 2⁴. Also 10 − n = 4 und n = 6. Probe: 2¹⁰ : 2⁶ = 2⁴ = 16.',
                                                'Schreibe 16 als Potenz von 2.')),
        ('Berechne 10⁴ : 10⁴ : 10⁴ · 10⁸.',
         Z('Ein Rechner schafft 10⁹ Rechenschritte pro Sekunde. 10³ Programme brauchen je 10⁸ Rechenschritte. Wie lange braucht er für alle? '
           'Gib die Zeit als 10ᵏ Sekunden an. Wie groß ist k?', 2, '3 + 8 - 9',
           'Alle Programme zusammen: 10³ · 10⁸ = 10¹¹ Rechenschritte. Geteilt durch 10⁹ pro Sekunde: 10¹¹ : 10⁹ = 10² = 100 Sekunden.',
           'Rechne erst alle Rechenschritte zusammen, dann teile durch die Schritte pro Sekunde.')),
    ],
}
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


# =====================================================================================================================
# Achtundzwanzigste Runde (20.11.): Nachbesserung nach der Prüfung (inhalte/pruefung/potenz/bericht.md)
# Schritte auf Aufgaben, gesucht über Lernkarte + genauen Fragetext. Jede Änderung kommt mit alt → neu in den Bericht.
#   ('h', lz, text, tipp)                 Tipp neu
#   ('typ', lz, text, g)                  Typ neu, Stufe folgt aus dem Typ
#   ('ohne_typ', lz, text)                Typ weg (überzählig, beim Einspielen gesperrt, nicht gelöscht)
#   ('antwort', lz, text, {alt: neu})     falsche Antworten ersetzen (Frage und richtige Antwort bleiben)
#   ('ersetze', lz, text, aufgabe)        Aufgabe an gleicher Stelle ersetzen (Pool, Stufe, Typ bleiben)
#   ('karte', lz, {feld: wert})           Felder der Lernkarte
# =====================================================================================================================
_ERK = 'erkennen'
NB_A = [
    # Muss 2
    ('h', 'mal_gleiche_basis', 'a⁵ · a¹ = aᵏ. Wie groß ist k?', 'a¹ ist a mit dem Exponenten 1. Addiere die Exponenten.'),
    # Sollte 3: Ablenker passend zur Rechnung (typische Fehler)
    ('antwort', 'mal_gleiche_basis', 'Ein Kind rechnet: 3⁴ · 3⁴ = 9⁸. Was ist falsch?',
     {'Gleicher Exponent: Basen malnehmen, der Exponent bleibt: 10⁴.': 'Die Exponenten werden malgenommen: 3¹⁶.',
      'Exponenten subtrahieren, nicht teilen: 3¹².': 'Die Exponenten werden subtrahiert: 3⁰.'}),
    ('antwort', 'mal_gleiche_basis', 'Ein Kind rechnet: 4⁴ · 4² = 4⁸. Was ist falsch?',
     {'Gleicher Exponent: Basen malnehmen, der Exponent bleibt: 10⁴.': 'Die Exponenten werden subtrahiert: 4².'}),
    ('antwort', 'mal_gleiche_basis', 'Ein Kind rechnet: 5⁴ · 5⁴ = 5¹⁶. Was ist falsch?',
     {'Gleicher Exponent: Basen malnehmen, der Exponent bleibt: 10⁴.': 'Die Basen werden addiert: 10⁸.'}),
    ('antwort', 'gleicher_exponent', 'Ein Kind rechnet: 2² · 5² = 10⁴. Was ist falsch?',
     {'Exponenten subtrahieren, nicht teilen: 5⁴.': 'Verschiedene Basen darf man nie zusammenfassen.'}),
    ('antwort', 'gleicher_exponent', 'Ein Kind rechnet: 2⁴ · 5⁴ = 10⁸. Was ist falsch?',
     {'Exponenten subtrahieren, nicht teilen: 5⁶.': 'Verschiedene Basen darf man nie zusammenfassen.'}),
    ('antwort', 'geteilt_gleiche_basis', 'Ein Kind rechnet: 5⁶ : 5² = 5³. Was ist falsch?',
     {'Die Exponenten werden addiert, nicht malgenommen: 5⁵.': 'Die Basen werden geteilt: 1⁴.'}),
    # Sollte 4: Stufe und Typ der 23 aus Gym 6 umgezogenen Aufgaben
    ('typ', 'mal_gleiche_basis', 'Stimmt die Rechnung? 5² · 5² = 5⁴', _ERK),
    ('typ', 'mal_gleiche_basis', 'Stimmt die Rechnung? 4⁴ · 4² = 4⁶', _ERK),
    ('typ', 'mal_gleiche_basis', 'Stimmt die Rechnung? 2⁴ · 2³ = 2⁷', _ERK),
    ('typ', 'geteilt_gleiche_basis', 'Stimmt die Rechnung? 4⁵ : 4² = 4³', _ERK),
    ('typ', 'geteilt_gleiche_basis', 'Stimmt die Rechnung? 4⁷ : 4⁴ = 4³', _ERK),
    ('typ', 'geteilt_gleiche_basis', 'Stimmt die Rechnung? 5⁵ : 5² = 5³', _ERK),
    ('typ', 'mal_gleiche_basis', 'Die Regel „a² · a³ = a⁶“ ist falsch. Für welche Zahlen a stimmt sie trotzdem?', 'parameter'),
    ('typ', 'mal_gleiche_basis', 'Ein Kind hat bei aᵏ · a² die Exponenten malgenommen und a¹² erhalten. Was wäre der richtige Exponent gewesen?', 'rueckwaerts'),
    ('typ', 'anwenden', 'Welche Rechnung ist richtig?', 'begruenden'),
    ('ersetze', 'mal_gleiche_basis', 'Ein Kind schreibt 2⁵ + 2⁵ = 2¹⁰. Richtig ist 2ᵏ. Wie groß ist k?',
     Z('Ein Kind rechnet 2³ · 2⁴ · 2 = 2¹². Richtig ist 2ᵏ. Wie groß ist k?', 8, '3 + 4 + 1',
       'Das Kind hat die Exponenten malgenommen: 3 · 4 · 1 = 12. Richtig ist addieren: 3 + 4 + 1 = 8. Die einzelne 2 ist 2¹.',
       'Welchen Exponenten hat die einzelne 2? Malnehmen oder addieren?')),
    # Sollte 4, Folge: Stufe 3 je Karte höchstens 3 × „fehler“ (Regel der Zwanzigsten Runde, Entscheidung des Nutzers: keine leichten
    # Aufgaben auf Stufe 3). Auswahl-Aufgaben, die nur den verletzten Rechenweg benennen lassen, werden Stufe 1 „erkennen“.
    ('typ', 'mal_gleiche_basis', 'Stimmt die Rechnung? 5² · 5³ = 5⁶', _ERK),
    ('typ', 'mal_gleiche_basis', 'Ein Kind rechnet: 3⁴ · 3⁴ = 9⁸. Was ist falsch?', _ERK),
    ('typ', 'mal_gleiche_basis', 'Ein Kind rechnet: 4⁴ · 4² = 4⁸. Was ist falsch?', _ERK),
    ('typ', 'mal_gleiche_basis', 'Ein Kind rechnet: 5⁴ · 5⁴ = 5¹⁶. Was ist falsch?', _ERK),
    ('typ', 'mal_gleiche_basis', 'Ein Kind rechnet: 4³ · 4² = 16⁵. Welcher Satz beschreibt den Fehler richtig?', _ERK),
    ('typ', 'mal_gleiche_basis', 'Ein Kind rechnet: 4³ · 4³ = 4⁹. Welcher Satz beschreibt den Fehler richtig?', _ERK),
    ('typ', 'mal_gleiche_basis', 'Ein Kind rechnet: 4⁴ · 4² = 16⁶. Welcher Satz beschreibt den Fehler richtig?', _ERK),
    ('typ', 'gleicher_exponent', 'Ein Kind rechnet: 2² · 5² = 10⁴. Was ist falsch?', _ERK),
    # Sollte 6: Typen vereinheitlichen
    ('typ', 'gleicher_exponent', 'Berechne geschickt: 2² · 50²', 'direkt'),
    ('typ', 'gleicher_exponent', 'Berechne geschickt: 2³ · 5³', 'direkt'),
    ('ohne_typ', 'gleicher_exponent', 'Berechne geschickt: 4² · 25²'),   # Spiegelbild von „25² · 4²“; sonst 3 gleich gebaute „direkt“
    ('ohne_typ', 'gleicher_exponent', 'Berechne geschickt: 2³ · 50³'),   # Spiegelbild von „50³ · 2³“
    ('typ', 'mal_gleiche_basis', '27 · 3⁵ = 3ᵏ. Wie groß ist k?', 'darstellung'),
    # Kann 2: Hinweis für das Kind, dass hier der erste Exponent immer größer ist
    ('karte', 'geteilt_gleiche_basis', {'regel': 'Bei ⟦gleicher Basis⟧ subtrahierst du beim Teilen die Exponenten. Hier ist der erste immer größer; '
                                                 'den anderen Fall lernst du später.'}),
]

# Kann 6 (Nutzer: Ja): neue Pflichtkarte „Potenzen von Potenzen“ (M7 1.2), natürliche Exponenten.
def _tab(kopf, zeilen): return {'typ': 'tabelle', 'kopf': kopf, 'zeilen': zeilen}


_HP = 'Potenz einer Potenz: Was machst du mit den Exponenten?'
KARTE_PVP = {
    'lernziel': 'potenz_von_potenz', 'titel': 'Potenzen von Potenzen',
    'regel': 'Bei einer ⟦Potenz einer Potenz⟧ nimmst du die Exponenten mal. So gilt: (aᵐ)ⁿ = aᵐ·ⁿ.',
    'einstieg': 'Ein Würfel hat 2² cm lange Kanten. Sein Volumen ist (2²)³ cm³. '
                'Hier wird eine Potenz noch einmal potenziert: eine ⟦Potenz einer Potenz⟧.',
    'woerter': [['Potenz einer Potenz', 'eine Potenz in Klammern mit noch einem Exponenten, z. B. (2²)³'],
                ['potenziert', 'mit einem Exponenten versehen, also mehrmals mit sich selbst malgenommen']],
    'bild': _tab(['Term', 'ausgeschrieben', 'Faktoren 2'], [['(2²)³', '2² · 2² · 2²', '?']]),
    'schritte': [{'text': '(2²)³ heißt: dreimal 2² malnehmen.'},
                 {'text': 'Das sind 2 + 2 + 2 = 6 Faktoren 2.', 'bild': {'zeilen': [['(2²)³', '2² · 2² · 2²', '2 + 2 + 2 = 6']]}},
                 {'text': 'Kürzer: Exponenten malnehmen, 2 · 3 = 6. Also ⟦2⁶ = 64 cm³⟧.',
                  'bild': {'zeilen': [['(2²)³', '2² · 2² · 2²', '2 + 2 + 2 = 6'], ['kürzer', '2 · 3', '6']]}}],
    'probe': '(2²)³ = 4³ = 64 und 2⁶ = 64 ✓',
    'fehler': '(2²)³ = 2⁵ ist falsch. Es sind drei Gruppen mit je 2 Faktoren, also 2⁶. Addiert wird nur bei 2² · 2³.',
    'fehler_bild': {'zeilen': [['(2²)³', '2⁵ (falsch)', '2 + 3 = 5'], ['(2²)³', '2² · 2² · 2²', '2 · 3 = 6']]},
}
AUFGABEN_PVP = [
    U('direkt', Z('(3²)⁴ = 3ᵏ. Wie groß ist k?', 8, '2 * 4', 'Exponenten malnehmen: 2 · 4 = 8. Also 3⁸.', _HP)),
    U('direkt', Z('(x³)⁵ = xᵏ. Wie groß ist k?', 15, '3 * 5', 'Exponenten malnehmen: 3 · 5 = 15. Also x¹⁵.', _HP)),
    U('direkt', Z('(10²)³ = 10ᵏ. Wie groß ist k?', 6, '2 * 3', 'Exponenten malnehmen: 2 · 3 = 6. Also 10⁶ = 1 000 000.', _HP)),
    U('direkt', Z('(a⁴)² = aᵏ. Wie groß ist k?', 8, '4 * 2', 'Exponenten malnehmen: 4 · 2 = 8. Also a⁸.', _HP)),
    U('erkennen', A('Welche Regel gilt bei (b⁵)²?', 'Exponenten malnehmen: b¹⁰', ['Exponenten addieren: b⁷', 'Exponent hoch Exponent: b²⁵'],
                    '(b⁵)² = b⁵ · b⁵ = b¹⁰: Potenz einer Potenz, Exponenten malnehmen.', 'Schreib (b⁵)² als Produkt aus.')),
    U('erkennen', A('Welcher Term ist gleich 2³ · 2³ · 2³ · 2³?', '(2³)⁴', ['2⁷', '(2³)³', '4 · 2³'],
                    'Viermal derselbe Faktor 2³ ist (2³)⁴ = 2¹². 2⁷ wäre 2³ · 2⁴, und 4 · 2³ ist eine Summe aus vier gleichen Summanden.',
                    'Wie oft kommt 2³ als Faktor vor?')),
    U('mehrschritt', Z('Berechne (2³)² mit dem Potenzgesetz. Gib das Ergebnis als Zahl an.', 64, '2 ** (3 * 2)', '(2³)² = 2⁶ = 64. Probe: 8² = 64.',
                       'Erst die Exponenten malnehmen, dann ausrechnen.')),
    U('mehrschritt', Z('(a²)³ · a⁴ = aᵏ. Wie groß ist k?', 10, '2 * 3 + 4', '(a²)³ = a⁶, dann a⁶ · a⁴ = a¹⁰.', 'Erst die Klammer, dann gleiche Basis.')),
    U('mehrschritt', Z('(2³)² · 2 = 2ᵏ. Wie groß ist k?', 7, '3 * 2 + 1', '(2³)² = 2⁶, dann 2⁶ · 2¹ = 2⁷.', 'Erst die Klammer, dann gleiche Basis.')),
    U('umkehr', Z('(5ᵏ)³ = 5¹². Wie groß ist k?', 4, '12 // 3', 'k · 3 = 12, also k = 4. Probe: (5⁴)³ = 5¹².', 'Welche Zahl mal 3 ergibt 12?')),
    U('umkehr', Z('(y²)ᵏ = y¹⁰. Wie groß ist k?', 5, '10 // 2', '2 · k = 10, also k = 5.', 'Welche Zahl mal 2 ergibt 10?')),
    U('einkleidung', Z('Ein Würfel hat die Kantenlänge 10² cm. Wie groß ist sein Volumen? Gib es als 10ᵏ cm³ an. Wie groß ist k?', 6, '2 * 3',
                       'Volumen = (10²)³ cm³ = 10⁶ cm³. Das ist 1 m³.', 'Volumen eines Würfels: Kantenlänge hoch 3.')),
    U('einkleidung', Z('Ein quadratisches Feld hat die Seitenlänge 3³ m. Wie groß ist seine Fläche? Gib sie als Zahl an.', 729, '3 ** (3 * 2)',
                       'Fläche = (3³)² m² = 3⁶ m² = 729 m². Probe: 27 · 27 = 729.', 'Fläche eines Quadrats: Seite hoch 2.', einheit='m²')),
    U('darstellung', A('Ein Würfel hat die Kantenlänge 5² cm. Welcher Term gibt sein Volumen in cm³ an?', '(5²)³ = 5⁶', ['5⁵', '5² · 3', '(5²)² = 5⁴'],
                       'Volumen = Kante hoch 3: (5²)³ = 5⁶. 5² · 3 wäre dreimal die Kante, (5²)² die Fläche einer Seite.', 'Volumen eines Würfels: Kante hoch 3.')),
    U('begruenden', A('Stimmt die Aussage? „(2³)² und (2²)³ sind gleich groß.“', 'Ja: Beides ist 2⁶ = 64, denn 3 · 2 = 2 · 3.',
                      ['Nein: (2³)² = 2⁵ und (2²)³ = 2⁶.', 'Nein: (2³)² ist größer, weil 3 größer als 2 ist.', 'Nein, das kann man nicht vergleichen.'],
                      '(2³)² = 8² = 64 und (2²)³ = 4³ = 64. Mit dem Gesetz: 3 · 2 = 6 und 2 · 3 = 6.', 'Rechne beide aus.')),
    U('begruenden', A('Warum gilt (a⁴)³ = a¹²? Welche Begründung stimmt?', 'a⁴ · a⁴ · a⁴ hat 4 + 4 + 4 = 12 Faktoren a.',
                      ['Weil man 4 und 3 addiert.', 'Weil man nur die Basis mit 3 malnimmt.', 'Weil a⁴ = 4a ist und 4a · 3 = 12a.'],
                      '(a⁴)³ heißt dreimal a⁴ als Faktor. Jedes a⁴ hat 4 Faktoren a, zusammen 12. Darum Exponenten malnehmen.',
                      'Schreib (a⁴)³ als Produkt aus.')),
    U('fehler', Z('Ein Kind rechnet (x⁴)³ = x⁷. Richtig ist xᵏ. Wie groß ist k?', 12, '4 * 3',
                  'Das Kind hat die Exponenten addiert. Bei einer Potenz einer Potenz wird malgenommen: 4 · 3 = 12.', 'Schreib (x⁴)³ als Produkt aus.')),
    U('fehler', A('Ein Kind rechnet (3²)³ = 9⁶. Was ist falsch?', 'Die Basis bleibt 3, die Exponenten werden malgenommen: 3⁶.',
                  ['Nichts, die Rechnung ist richtig.', 'Die Exponenten werden addiert: 3⁵.', 'Richtig wäre 9⁵.'],
                  '(3²)³ = 3² · 3² · 3² = 3⁶ = 729. Das Kind hat zusätzlich die Basis quadriert: 9⁶ wäre viel größer.', 'Schreib (3²)³ als Produkt aus.')),
    U('parameter', Z('Für wie viele natürliche Zahlen n von 1 bis 20 ist (2ⁿ)² höchstens 2²⁰?', 10, '20 // 2',
                     '(2ⁿ)² = 2²ⁿ. Höchstens 2²⁰ heißt 2n ≤ 20, also n ≤ 10. Das sind n = 1, 2, …, 10, also 10 Zahlen.', 'Schreibe (2ⁿ)² als eine Potenz.')),
    U('rueckwaerts', Z('Eine Zahl 2ᵏ wird erst quadriert und das Ergebnis dann hoch 3 genommen. Heraus kommt 2¹⁸. Wie groß ist k?', 3, '18 // 6',
                       '((2ᵏ)²)³ = 2ᵏ·²·³ = 2⁶ᵏ. 6k = 18, also k = 3. Probe: (2³)² = 2⁶, (2⁶)³ = 2¹⁸.', 'Fasse beide Schritte zu einem Exponenten zusammen.')),
    U('verknuepfen', Z('Ein Würfel hat 3² cm lange Kanten. Wie viele Würfel mit 1 cm Kantenlänge passen hinein?', 729, '(3 ** 2) ** 3',
                       'Volumen: (3²)³ cm³ = 3⁶ cm³ = 729 cm³. Jeder kleine Würfel hat 1 cm³, also 729 Würfel. Probe: 9 · 9 · 9 = 729.',
                       'Volumen eines Würfels: Kante hoch 3.')),
    U('transfer', Z('Ein Würfel aus Zuckerstücken hat 2⁴ Stücke an jeder Kante. Aus solchen Würfeln baut man einen großen Würfel mit 2² Würfeln '
                    'an jeder Kante. Wie viele Zuckerstücke sind es? Gib die Anzahl als 2ᵏ an. Wie groß ist k?', 18, '(4 + 2) * 3',
                    'An jeder Kante des großen Würfels liegen 2⁴ · 2² = 2⁶ Stücke. Anzahl: (2⁶)³ = 2¹⁸.', 'Wie viele Stücke liegen an einer Kante des großen Würfels?')),
    U('pruefung', Z('a) Vereinfache (x²)⁴ · x³. b) Berechne den Wert für x = 2. Gib den Wert aus b) an.', 2048, '2 ** (2 * 4 + 3)',
                    'a) (x²)⁴ = x⁸, x⁸ · x³ = x¹¹. b) 2¹¹ = 2 048.', 'Erst vereinfachen, dann einsetzen.')),
    K(Z('Welche Zahl ist größer: (2³)⁴ oder (3²)³? Gib die größere Zahl an.', 4096, 'max(2 ** 12, 3 ** 6)',
        '(2³)⁴ = 2¹² = 4 096 und (3²)³ = 3⁶ = 729. Größer ist 4 096, obwohl die Basis 2 kleiner ist als 3.', 'Fasse jede Zahl zu einer Potenz zusammen.')),
    K(Z('Schreibe 9² · 27³ als Dreierpotenz 3ᵏ. Wie groß ist k?', 13, '2 * 2 + 3 * 3',
        '9 = 3² und 27 = 3³. 9² = (3²)² = 3⁴ und 27³ = (3³)³ = 3⁹. Zusammen 3⁴ · 3⁹ = 3¹³.', 'Schreibe 9 und 27 als Potenzen von 3.')),
    T(Z('(7²)³ = 7ᵏ. Wie groß ist k?', 6, '2 * 3', 'Exponenten malnehmen: 2 · 3 = 6.')),
    KO(Z('(b³)⁴ = bᵏ. Wie groß ist k?', 12, '3 * 4', 'Exponenten malnehmen: 3 · 4 = 12.')),
    KO(Z('(2⁵)² = 2ᵏ. Wie groß ist k?', 10, '5 * 2', 'Exponenten malnehmen: 5 · 2 = 10.')),
    KO(A('Welche Regel gilt bei (y²)⁵?', 'Exponenten malnehmen: y¹⁰', ['Exponenten addieren: y⁷', 'Basen malnehmen: (5y)²'], 'Potenz einer Potenz: 2 · 5 = 10.')),
    SI(Z('(10⁴)² = 10ᵏ. Wie groß ist k?', 8, '4 * 2', 'Exponenten malnehmen: 4 · 2 = 8.')),
    SI(Z('(a³)³ = aᵏ. Wie groß ist k?', 9, '3 * 3', 'Exponenten malnehmen: 3 · 3 = 9.')),
    SI(Z('(x⁶)² = xᵏ. Wie groß ist k?', 12, '6 * 2', 'Exponenten malnehmen: 6 · 2 = 12.')),
    SI(Z('(4²)² = 4ᵏ. Wie groß ist k?', 4, '2 * 2', 'Exponenten malnehmen: 2 · 2 = 4.')),
    SI(Z('Berechne (3²)² mit dem Potenzgesetz und gib den Wert an.', 81, '3 ** (2 * 2)', '(3²)² = 3⁴ = 81.')),
    SI(Z('(5²)³ = 5ᵏ. Wie groß ist k?', 6, '2 * 3', 'Exponenten malnehmen: 2 · 3 = 6.')),
]


# Neunundzwanzigste Runde (21.11., Entscheidung des Nutzers Punkt 2; Nachprüfung Kann 2, 4, 6)
NB29_A = [
    # die sieben „Fehler benennen“-Auswahlaufgaben: kein Typ (überzählig, beim Einspielen gesperrt, nicht gelöscht)
    ('ohne_typ', 'mal_gleiche_basis', 'Ein Kind rechnet: 3⁴ · 3⁴ = 9⁸. Was ist falsch?'),
    ('ohne_typ', 'mal_gleiche_basis', 'Ein Kind rechnet: 4⁴ · 4² = 4⁸. Was ist falsch?'),
    ('ohne_typ', 'mal_gleiche_basis', 'Ein Kind rechnet: 5⁴ · 5⁴ = 5¹⁶. Was ist falsch?'),
    ('ohne_typ', 'mal_gleiche_basis', 'Ein Kind rechnet: 4³ · 4² = 16⁵. Welcher Satz beschreibt den Fehler richtig?'),
    ('ohne_typ', 'mal_gleiche_basis', 'Ein Kind rechnet: 4³ · 4³ = 4⁹. Welcher Satz beschreibt den Fehler richtig?'),
    ('ohne_typ', 'mal_gleiche_basis', 'Ein Kind rechnet: 4⁴ · 4² = 16⁶. Welcher Satz beschreibt den Fehler richtig?'),
    ('ohne_typ', 'gleicher_exponent', 'Ein Kind rechnet: 2² · 5² = 10⁴. Was ist falsch?'),
    # Kann 2: Ablenker, die eine Basis verlieren
    ('antwort', 'gleicher_exponent', 'Ein Kind rechnet: 2³ · 5³ = 10⁶. Was ist falsch?',
     {'Die Exponenten werden addiert, nicht malgenommen: 2⁵.': 'Die Basen werden addiert: 7³.'}),
    ('antwort', 'gleicher_exponent', 'Ein Kind rechnet: 2⁴ · 5⁴ = 10⁸. Was ist falsch?',
     {'Die Exponenten werden addiert, nicht malgenommen: 5⁶.': 'Die Basen werden addiert: 7⁴.'}),
    # Kann 4: ein Schritt (10 − n = 4) → Stufe 2 umkehr
    ('typ', 'geteilt_gleiche_basis', '2¹⁰ : 2ⁿ = 16. Wie groß ist n?', 'umkehr'),
    # Kann 6: Wort „potenziert“ einfacher
    ('karte', 'potenz_von_potenz', {'woerter': [['Potenz einer Potenz', 'eine Potenz in Klammern mit noch einem Exponenten, z. B. (2²)³'],
                                                ['potenziert', 'hoch eine Zahl genommen']]}),
]


def _kurz(a):
    x = {k: a.get(k) for k in ('p', 's', 'g')}
    return f"{x['p']}, Stufe {x['s']}, {x['g'] or 'ohne Typ'}"


def nachbessern(d, thema, schritte):
    nb = BERICHT[thema]['nachbessern']
    for op in schritte:
        art, lz = op[0], op[1]
        if art == 'karte':
            e = next(e for e in d['inhalt']['etappen'] if e['lernziel'] == lz)
            for k, v in op[2].items():
                nb.append({'lz': lz, 'was': f'Lernkarte, {k}', 'alt': e.get(k), 'neu': v}); e[k] = v
            continue
        text = op[2]
        xs = [a for a in d['aufgaben'] if a['l'] == lz and a['f']['text'] == text]
        assert len(xs) == 1, (thema, lz, text, len(xs))
        a = xs[0]
        if art == 'h':
            nb.append({'lz': lz, 'text': text, 'was': 'Tipp', 'alt': a.get('h'), 'neu': op[3]}); a['h'] = op[3]
        elif art == 'typ':
            alt = _kurz(a); a['g'] = op[3]; a['s'] = STUFE_VON[op[3]]
            nb.append({'lz': lz, 'text': text, 'was': 'Stufe/Typ', 'alt': alt, 'neu': _kurz(a)})
        elif art == 'ohne_typ':
            alt = _kurz(a); a.pop('g')
            nb.append({'lz': lz, 'text': text, 'was': 'Stufe/Typ', 'alt': alt, 'neu': _kurz(a) + ' (überzählig)'})
        elif art == 'antwort':
            richtig = a['a'][a['o']['index']]
            for alt, neu in op[3].items():
                assert alt in a['a'] and alt != richtig and neu not in a['a'], (text, alt)
                a['a'] = [neu if x == alt else x for x in a['a']]
                nb.append({'lz': lz, 'text': text, 'was': 'falsche Antwort', 'alt': alt, 'neu': neu})
            assert a['a'][a['o']['index']] == richtig
        elif art == 'ersetze':
            i = d['aufgaben'].index(a)
            n = {k: a[k] for k in ('l', 't', 'p', 's', 'g') if k in a}
            n.update(copy.deepcopy(op[3]))
            assert n['f']['text'] not in {x['f']['text'] for x in d['aufgaben']}
            d['aufgaben'][i] = n
            nb.append({'lz': lz, 'text': text, 'was': 'Aufgabe ersetzt', 'alt': text, 'neu': n['f']['text']})
        else:
            raise ValueError(art)


def karte_pvp(d, thema):
    """Kann 6: Pflichtkarte potenz_von_potenz hinter gleicher_exponent."""
    lz = 'potenz_von_potenz'
    et = d['inhalt']['etappen']
    et.insert(next(i for i, e in enumerate(et) if e['lernziel'] == 'gleicher_exponent') + 1, copy.deepcopy(KARTE_PVP))
    d['inhalt']['teilfaehigkeiten'].append({'k': lz, 'text': KARTE_PVP['titel'], 'lernziele': [lz]})
    d['inhalt']['bewertung']['lernziele_pflicht'].append(lz)
    texte = {a['f']['text'] for a in d['aufgaben']}
    neu = []
    for p, g, a in AUFGABEN_PVP:
        x = _aufgabe(lz, p, g, a)
        assert x['f']['text'] not in texte, x['f']['text']
        texte.add(x['f']['text']); neu.append(x)
    i = max(i for i, a in enumerate(d['aufgaben']) if a['l'] == 'gleicher_exponent') + 1
    d['aufgaben'][i:i] = neu
    BERICHT[thema]['karte_neu'] = [{'lz': lz, 'p': x['p'], 's': x['s'], 'g': x.get('g'), 'text': x['f']['text']} for x in neu]


def flug_a():
    thema = 'terme.potenzgesetze_natuerlich'
    d = start_a()
    weg_b = [a['f']['text'] for a in d['aufgaben'] if nach_b(a)]
    for lz, paare in ERSATZ_A.items():
        for alt, neu in paare: _ersetzen(d, thema, lz, alt, neu)
    assert not [a for a in d['aufgaben'] if nach_b(a)], 'negativer Exponent übrig'
    BERICHT[thema]['nach_b'] = weg_b
    for a, alt in gym6_nach_a():
        assert a['f']['text'] not in {x['f']['text'] for x in d['aufgaben']}, a['f']['text']
        d['aufgaben'].append(a)
        BERICHT[thema]['aus_gym6'].append({'lz': a['l'], 'vorher': alt, 'text': a['f']['text']})
    nachbessern(d, thema, NB_A)          # Achtundzwanzigste Runde
    karte_pvp(d, thema)                  # Achtundzwanzigste Runde, Kann 6
    nachbessern(d, thema, NB29_A)        # Neunundzwanzigste Runde
    for lz in LZ_A + ('potenz_von_potenz',):
        _ordnen_karte(d, lz)
        _regeln(d, lz)
        assert sum(1 for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'uebung' and a['s'] == 3 and a.get('g') == 'fehler') <= 3, lz
    rest = [a['f']['text'] for a in d['aufgaben'] if NEG.search(json.dumps([a['f'], a.get('a'), a.get('w'), a.get('h')], ensure_ascii=False))]
    assert not rest, f'negativer Exponent in Flug A: {rest}'
    inh = d['inhalt']
    inh['abschnitte'] = [{'titel': 'Potenzen malnehmen', 'lernziele': ['mal_gleiche_basis', 'gleicher_exponent', 'potenz_von_potenz']},
                         {'titel': 'Vertiefung: teilen und geschickt rechnen', 'lernziele': ['geteilt_gleiche_basis', 'anwenden']}]
    out = {'thema_schluessel': thema, 'thema_id': 102, 'block_id': 62, 'klasse': {'gym_by': 7, 'rs_by': 7, 'ib_myp': 3},
           'autor': 'Claude (Sechsundzwanzigste und Achtundzwanzigste Runde, Generator terme.potenzgesetze_natuerlich.py; vier Lernkarten aus terme.umformen)',
           'inhalt': {
               'ziel': 'Potenzen mit natürlichen Exponenten zusammenfassen: bei gleicher Basis malnehmen (Vertiefung: teilen), bei gleichem '
                       'Exponenten die Basen zusammenfassen, Potenzen von Potenzen vereinfachen und die Gesetze geschickt nutzen. Vorwissen: Potenzen aus Klasse 6 (Basis, Exponent, '
                       'Hoch 0). Die Gesetze mit negativen Exponenten folgen in Klasse 8 im Flug „Potenzgesetze mit ganzzahligen Exponenten“.',
               'merke': ['Gleiche Basis: aᵐ · aⁿ = aᵐ⁺ⁿ (malnehmen) und aᵐ : aⁿ = aᵐ⁻ⁿ (teilen).', 'Gleicher Exponent: aⁿ · bⁿ = (a · b)ⁿ.', 'Potenz einer Potenz: (aᵐ)ⁿ = aᵐ·ⁿ.',
                         'Erst prüfen: gleiche Basis oder gleicher Exponent? Sonst ausrechnen.'],
               'abschnitte': inh['abschnitte'], 'etappen': inh['etappen'], 'teilfaehigkeiten': inh['teilfaehigkeiten'],
               'bewertung': {**inh['bewertung'], 'testaufgaben_je_lernziel': 1},
               'quellen': {'erklaerungen': 'Vier Lernkarten aus terme.umformen (dorthin in der Einundzwanzigsten Runde aus terme.potenzgesetze); '
                                           'potenz_von_potenz eigene Fassung (Achtundzwanzigste Runde).',
                           'aufgaben': 'Vom Generator erzeugt und berechnet; Umzug und Ersatz: Sechsundzwanzigste Runde.',
                           'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern (Gymnasium, Jahrgangsstufe 7, M7 1.2).'}},
           'aufgaben': d['aufgaben'],
           'offen': ['Sechsundzwanzigste Runde: Die vier Lernkarten stammen aus terme.umformen (Lernziel-Schlüssel unverändert, damit der Lernstand '
                     'umgehängt werden kann). 31 Aufgaben mit negativem Exponenten (22 im Fragetext, 7 mit negativem Ergebnis-Exponenten, 2 mit kleinerem '
                     'erstem Exponenten im Rechenweg) sind nach terme.potenzgesetze_ganzzahlig umgezogen und hier durch Aufgaben mit natürlichen '
                     'Exponenten ersetzt (gleiche Karte, gleicher Pool, gleiche Stufe, gleicher Typ). Dazu 23 Aufgaben aus „Fehler finden“ von '
                     'terme.potenzgesetze; Stufe und Typ nach der Prüfung (Achtundzwanzigste Runde) je Aufgabe gesetzt.',
                     'Achtundzwanzigste Runde: neue Pflichtkarte potenz_von_potenz (M7 1.2 „Potenzen von Potenzen“, Entscheidung des Nutzers).',
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


_H0 = 'Denk an das Muster 2² = 4, 2¹ = 2, 2⁰ = ?: Es wird jedes Mal durch 2 geteilt.'
NB_GYM6 = [
    ('h', 'negativer_exponent', 'Wie viel Mal so groß ist 2² wie 2⁻²?', 'Rechne beide Potenzen aus und teile.'),   # Muss 1
    ('h', 'negativer_exponent', 'Was ergibt a⁰?', _H0),                                                       # Sollte 1
    ('h', 'negativer_exponent', 'Was ergibt 12⁰?', _H0),
]


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
    nachbessern(d, thema, NB_GYM6)       # Achtundzwanzigste Runde
    e = next(e for e in d['inhalt']['etappen'] if e['lernziel'] == 'fehler_finden')
    e.update(copy.deepcopy(GYM6_KARTE))
    _ordnen_karte(d, 'fehler_finden')
    _regeln(d, 'fehler_finden')
    rest = json.dumps([a for a in d['aufgaben'] if a['l'] == 'fehler_finden'] + [e], ensure_ascii=False)
    assert not re.search(r'Exponenten (werden )?(addier|subtrah|malgenommen)|Gleicher Exponent|Basis bleibt|Potenzgesetz', rest), 'Potenzgesetz übrig'
    inh = d['inhalt']
    inh['ziel'] = ('Potenzen mit natürlichen und negativen ganzzahligen Exponenten verstehen und berechnen, auch mit Brüchen, Dezimalzahlen '
                   'und negativer Basis. Die Potenzgesetze folgen in Klasse 7 im Flug „Potenzgesetze“.')
    d['offen'] = ['Rationale Exponenten stehen nicht in diesem Flug (Stoff Kl. 9, eigenes Thema zahlen.rationale_exponenten).',
                  'Exponenten werden als Zahl abgefragt (z. B. „2ᵏ = 1/16, k = ?“), weil die App keine Hochstellung eingeben kann.',
                  'Sechsundzwanzigste Runde (20.11.): Die Potenzgesetze stehen in eigenen Flügen (terme.potenzgesetze_natuerlich, Klasse 7; '
                  'terme.potenzgesetze_ganzzahlig, Klasse 8). Die 23 Aufgaben aus „Fehler finden“, die ein Potenzgesetz voraussetzen, sind nach '
                  'terme.potenzgesetze_natuerlich umgezogen; „Fehler finden“ ist mit 14 neuen Aufgaben zu Potenzbegriff, Hoch 0 und negativem '
                  'Exponenten wieder aufgefüllt, Erklärung der Karte neu (Zahlenprobe 2⁴ statt Potenzgesetz).']
    # Nachweis: die anderen Karten unverändert (bis auf den einen Lösungsweg)
    for e0 in vorher['inhalt']['etappen']:
        if e0['lernziel'] != 'fehler_finden': assert e0 in inh['etappen']
    alt_rest = [a for a in vorher['aufgaben'] if a['l'] != 'fehler_finden']
    neu_rest = [a for a in d['aufgaben'] if a['l'] != 'fehler_finden']
    assert len(alt_rest) == len(neu_rest) and sum(1 for x, y in zip(alt_rest, neu_rest) if x != y) == 3  # Lösungsweg/Tipp „2² wie 2⁻²“, Tipps zu a⁰ und 12⁰
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh_text.endswith('\n') else ''), encoding='utf-8')
    f, w, info = pruefe(pfad)
    assert not f, '; '.join(f[:8])
    print(f'  POTENZ-TEILEN {thema}: {info}')
    (Path('/tmp') / f'potenz_teilen_{thema}.json').write_text(json.dumps(BERICHT[thema], ensure_ascii=False, indent=1))
    return d

