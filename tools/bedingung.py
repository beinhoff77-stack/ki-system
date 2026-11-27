"""Antworttyp „bedingung“ – Referenz in Python (Schritt 2 der Bau-Reihenfolge, nur Arbeitsstand).

Eine Aufgabe dieses Typs hat mehrere Zahlenfelder und eine Liste von Bedingungen. Richtig ist jede Antwort,
die alle Bedingungen erfüllt. Die Bedingungen stehen als DATEN in der Aufgabe (kleine feste Rechensprache),
nicht als Programm. Diese Datei ist die Referenz, gegen die die Datenbank-Fassung geprüft wird:
beide müssen für die Fälle in tools/tests/bedingung_faelle.json dasselbe liefern.

Aufruf:  python3 -I tools/bedingung.py            (rechnet alle Fälle nach, Ausgabe „OK“ oder Fehlerliste)
Format und Grenzen: inhalte/plan/bedingung-format.md
"""
import json
import re
import sys
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

MAX_FELDER = 6
MAX_BEDINGUNGEN = 8
MAX_KNOTEN = 60           # je Bedingung, „pruefe“ und „zeige“ zusammen
MAX_TIEFE = 8
MAX_EXPONENT = 6
MAX_ZAHL = 10 ** 30       # Zähler und Nenner jedes Zwischenwerts
FELD_MIN, FELD_MAX = -999999, 999999
ARTEN = ('ganz', 'rational')
MAX_ROH = 40             # Zeichen einer rohen Eingabe, vor dem Putzen

# Bewusst [0-9] und eine feste Leerraum-Liste: Die Datenbank-Fassung muss Zeichen für Zeichen dasselbe annehmen.
# Genau ein freiwilliges Vorzeichen: „+3“ und „-3“ gelten, „+-3“ und „--3“ nicht.
GANZ = re.compile(r'^[+-]?[0-9]{1,6}$')
KOMMA = re.compile(r'^[+-]?[0-9]{1,6}(,[0-9]{1,3})?$')
BRUCH = re.compile(r'^([+-]?[0-9]{1,6})/([0-9]{1,6})$')
LEER = re.compile('[ \t\n\r\f\v\u00a0\u202f]')


def putzen(roh):
    """Leerraum weg, typografisches Minus zu Minus. Für die Leer-Prüfung und das Lesen."""
    return LEER.sub('', str(roh)).replace('−', '-').replace('–', '-')


class Grenze(Exception):
    """Rechnung nicht definiert (Division durch null, unerlaubter Exponent): Die Bedingung gilt als verletzt."""


class ZuGross(Exception):
    """Ein Zwischenwert überschreitet die Lastgrenze: Die Eingabe wird abgewiesen, nichts wird gewertet."""


class Kommazahl(float):
    """JSON-Zahl mit Komma oder Exponent, gelesen mit lade_json(): rechnet überall wie float, merkt sich aber ihre Schreibweise.
    So urteilt die Referenz exakt wie die Datenbank (1.00000000000000001 ist nicht 1), ohne dass anderer Code etwas merkt."""
    def __new__(cls, roh):
        o = super().__new__(cls, roh)
        o.roh = roh
        return o


def ganzwert(v):
    """JSON-Zahl mit ganzem Wert -> int, sonst None. Es zählt der Wert, nicht die Schreibweise (5, 5.0 und 5e0 sind dasselbe).
    Wer Antworten oder Aufgaben aus JSON liest und exakt wie die Datenbank urteilen will, liest mit lade_json(): Dann kommen
    Kommazahlen als Decimal an und 1.00000000000000001 wird nicht still zu 1 gerundet."""
    if isinstance(v, bool):
        return None
    if isinstance(v, int):
        return v
    if isinstance(v, Kommazahl):
        v = Decimal(v.roh)
    if isinstance(v, Decimal):
        return int(v) if v.is_finite() and v == v.to_integral_value() else None
    if isinstance(v, float) and v == v and abs(v) != float('inf') and v.is_integer():
        return int(v)
    return None


def lade_json(text):
    """JSON lesen wie die Datenbank: Zahlen mit Komma oder Exponent behalten ihre Schreibweise (Kommazahl)."""
    return json.loads(text, parse_float=Kommazahl)


def schreibe_json(v):
    """JSON schreiben ohne Verlust: Kommazahl und Decimal in ihrer Schreibweise. Für die Weitergabe an die Datenbank."""
    if isinstance(v, dict):
        return '{' + ','.join(json.dumps(str(k), ensure_ascii=False) + ':' + schreibe_json(x) for k, x in v.items()) + '}'
    if isinstance(v, (list, tuple)):
        return '[' + ','.join(schreibe_json(x) for x in v) + ']'
    if isinstance(v, Kommazahl):
        return v.roh
    if isinstance(v, Decimal):
        return str(v)
    return json.dumps(v, ensure_ascii=False)


def eingabe(roh, art):
    """Liest ein Antwortfeld oder eine Konstante. Rückgabe Fraction oder None (Format falsch).
    Erlaubt sind Text und JSON-Zahlen mit ganzem Wert; alles andere (Wahrheitswert, Liste, Kommazahl als JSON-Zahl) ist Format falsch."""
    if isinstance(roh, (int, float, Decimal)) and not isinstance(roh, bool):
        g = ganzwert(roh)
        if g is None:
            return None
        roh = str(g)
    if not isinstance(roh, str) or len(roh) > MAX_ROH:
        return None
    s = putzen(roh)
    if len(s) > 14:
        return None
    if GANZ.match(s):
        return Fraction(int(s))
    if art != 'rational':
        return None
    if KOMMA.match(s):
        return Fraction(s.replace(',', '.'))
    m = BRUCH.match(s)
    if m and int(m.group(2)) != 0:
        return Fraction(int(m.group(1)), int(m.group(2)))
    return None


def deutsch(w):
    """Zahl für den Hinweis: Minuszeichen, Dezimalkomma, sonst Bruch."""
    if isinstance(w, bool):
        return 'ja' if w else 'nein'
    if w.denominator == 1:
        s = str(abs(w.numerator))
    elif 1000 % w.denominator == 0:
        t = abs(w.numerator) * (1000 // w.denominator)   # exakt, ohne Gleitkomma
        s = f'{t // 1000},{t % 1000:03d}'.rstrip('0')
    else:
        s = f'{abs(w.numerator)}/{w.denominator}'
    return ('−' if w < 0 else '') + s


def _zahl(v):
    if isinstance(v, bool) or not isinstance(v, Fraction):
        raise ValueError('Zahl erwartet')
    if abs(v.numerator) > MAX_ZAHL or v.denominator > MAX_ZAHL:
        raise ZuGross('zu groß')
    return v


def _liste(v):
    if not isinstance(v, list) or not v:
        raise ValueError('Liste erwartet')
    return [_zahl(x) for x in v]


def _wahr(v):
    if not isinstance(v, bool):
        raise ValueError('Wahrheitswert erwartet')
    return v


def _median(xs):
    s = sorted(xs)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def _geteilt(a, b):
    if b == 0:
        raise Grenze('nicht definiert')
    return a / b


def _hoch(a, b):
    if b.denominator != 1 or abs(b) > MAX_EXPONENT:
        raise Grenze('Exponent nicht erlaubt')
    if b < 0 and a == 0:
        raise Grenze('nicht definiert')
    return a ** int(b)


def _teilbar(a, b):
    if a.denominator != 1 or b.denominator != 1 or b == 0:
        raise Grenze('Teilbarkeit nur für ganze Zahlen, Teiler nicht null')
    return a.numerator % b.numerator == 0


# Name -> (Mindestzahl Argumente, Höchstzahl, Funktion). Das ist die ganze Sprache; sonst ist nichts erlaubt.
OPS = {
    '+': (2, 6, lambda *a: sum((_zahl(x) for x in a), Fraction(0))),
    '-': (2, 2, lambda a, b: _zahl(a) - _zahl(b)),
    '*': (2, 6, lambda *a: _produkt(a)),
    '/': (2, 2, lambda a, b: _geteilt(_zahl(a), _zahl(b))),
    'hoch': (2, 2, lambda a, b: _hoch(_zahl(a), _zahl(b))),
    'neg': (1, 1, lambda a: -_zahl(a)),
    'betrag': (1, 1, lambda a: abs(_zahl(a))),
    'liste': (1, 6, lambda *a: [_zahl(x) for x in a]),
    'summe': (1, 1, lambda l: sum(_liste(l), Fraction(0))),
    'produkt': (1, 1, lambda l: _produkt(_liste(l))),
    'min': (1, 1, lambda l: min(_liste(l))),
    'max': (1, 1, lambda l: max(_liste(l))),
    'median': (1, 1, lambda l: _median(_liste(l))),
    'mittelwert': (1, 1, lambda l: sum(_liste(l), Fraction(0)) / len(l)),
    'anzahl': (1, 1, lambda l: Fraction(len(_liste(l)))),
    'anzahl_positiv': (1, 1, lambda l: Fraction(sum(1 for x in _liste(l) if x > 0))),
    'anzahl_negativ': (1, 1, lambda l: Fraction(sum(1 for x in _liste(l) if x < 0))),
    'verschieden': (1, 1, lambda l: len(set(_liste(l))) == len(l)),
    'ganzzahlig': (1, 1, lambda a: _zahl(a).denominator == 1),
    'teilbar': (2, 2, lambda a, b: _teilbar(_zahl(a), _zahl(b))),
    '=': (2, 2, lambda a, b: _zahl(a) == _zahl(b)),
    '!=': (2, 2, lambda a, b: _zahl(a) != _zahl(b)),
    '<': (2, 2, lambda a, b: _zahl(a) < _zahl(b)),
    '<=': (2, 2, lambda a, b: _zahl(a) <= _zahl(b)),
    '>': (2, 2, lambda a, b: _zahl(a) > _zahl(b)),
    '>=': (2, 2, lambda a, b: _zahl(a) >= _zahl(b)),
    'und': (2, 6, lambda *a: all([_wahr(x) for x in a])),      # Liste, nicht Generator: jeder Operand wird geprüft
    'oder': (2, 6, lambda *a: any([_wahr(x) for x in a])),
    'nicht': (1, 1, lambda a: not _wahr(a)),
}


# Typen: Name -> (Typ der Argumente, Typ des Ergebnisses). 'zahl', 'wahr' oder 'liste'.
TYP = {n: ('zahl', 'zahl') for n in ('+', '-', '*', '/', 'hoch', 'neg', 'betrag')}
TYP.update({'liste': ('zahl', 'liste'), 'verschieden': ('liste', 'wahr'), 'ganzzahlig': ('zahl', 'wahr')})
TYP.update({n: ('liste', 'zahl') for n in ('summe', 'produkt', 'min', 'max', 'median', 'mittelwert', 'anzahl', 'anzahl_positiv', 'anzahl_negativ')})
TYP.update({n: ('zahl', 'wahr') for n in ('teilbar', '=', '!=', '<', '<=', '>', '>=')})
TYP.update({n: ('wahr', 'wahr') for n in ('und', 'oder', 'nicht')})


def typ(baum):
    """Typ eines (schon von knoten() geprüften) Baums. ValueError, wenn ein Operand den falschen Typ hat – in jedem Ast."""
    if isinstance(baum, (int, float, Decimal)):
        return 'zahl'
    if isinstance(baum, str):
        return 'liste' if baum == '$alle' else 'zahl'
    soll, ergebnis = TYP[baum[0]]
    for a in baum[1:]:
        if typ(a) != soll:
            raise ValueError(f'{baum[0]}: Operand muss {soll} sein')
    return ergebnis


def _produkt(xs):
    p = Fraction(1)
    for x in xs:
        p = _zahl(p * _zahl(x))
    return p


def knoten(baum, tiefe=1, felder=MAX_FELDER):
    """Zählt die Knoten eines Baums und prüft Tiefe, Namen, Feldnummern und Argumentzahl. ValueError bei Formfehler."""
    if tiefe > MAX_TIEFE:
        raise ValueError('Baum zu tief')
    if isinstance(baum, bool):
        raise ValueError('Wahrheitswerte stehen nicht als Konstante im Baum')
    if isinstance(baum, (int, float, Decimal)):
        g = ganzwert(baum)
        if g is None or abs(g) > FELD_MAX:
            raise ValueError('Konstante muss eine ganze Zahl bis 999 999 sein')
        return 1
    if isinstance(baum, str):
        if re.fullmatch(r'\$[1-6]', baum):
            if int(baum[1:]) > felder:
                raise ValueError(f'{baum}: so viele Felder gibt es nicht')
            return 1
        m = BRUCH.match(baum)
        if baum == '$alle' or KOMMA.match(baum) or (m and int(m.group(2)) != 0):
            return 1
        raise ValueError(f'unbekannter Name {baum!r}')
    if isinstance(baum, list) and baum and isinstance(baum[0], str) and baum[0] in OPS:
        lo, hi, _ = OPS[baum[0]]
        if not lo <= len(baum) - 1 <= hi:
            raise ValueError(f'{baum[0]}: falsche Zahl von Argumenten')
        return 1 + sum(knoten(a, tiefe + 1, felder) for a in baum[1:])
    raise ValueError(f'nicht erlaubt: {str(baum)[:40]}')


def wert(baum, werte):
    """Rechnet einen Baum mit den Feldwerten aus. Ergebnis Fraction, bool oder Liste."""
    if isinstance(baum, (int, float, Decimal)):
        return Fraction(ganzwert(baum))
    if isinstance(baum, str):
        if baum == '$alle':
            return list(werte)
        if baum.startswith('$'):
            i = int(baum[1:])
            if i > len(werte):
                raise ValueError(f'{baum}: so viele Felder gibt es nicht')
            return werte[i - 1]
        w = eingabe(baum, 'rational')
        if w is None:
            raise ValueError(f'Konstante {baum!r} nicht lesbar')
        return w
    f = OPS[baum[0]][2]
    r = f(*[wert(a, werte) for a in baum[1:]])
    return _zahl(r) if isinstance(r, Fraction) else r


def bewerte(aufgabe, antwort):
    """Wie schule.antwort_bewerten: {format_ok, richtig, verletzt?, hinweis?}.
    aufgabe = {'f': {'felder': [...]}, 'o': {'bedingungen': [...]}}, antwort = {'werte': [...]}."""
    felder = aufgabe['f']['felder']
    beds = aufgabe['o']['bedingungen']
    if not (isinstance(felder, list) and 1 <= len(felder) <= MAX_FELDER and isinstance(beds, list) and 1 <= len(beds) <= MAX_BEDINGUNGEN):
        raise ValueError('Aufgabe ungültig: 1 bis 6 Felder und 1 bis 8 Bedingungen nötig')   # Inhaltsfehler, kein „richtig“
    roh = antwort.get('werte') if isinstance(antwort, dict) else None
    if not isinstance(roh, list) or len(roh) != len(felder):
        return {'format_ok': False, 'hinweis': 'Bitte fülle alle Felder aus.'}
    werte = []
    for r, feld in zip(roh, felder):
        if r is None:
            return {'format_ok': False, 'hinweis': 'Bitte fülle alle Felder aus.'}
        # Länge zuerst: Ein Text über 40 Zeichen wird gar nicht erst geputzt (auch 41 Leerzeichen sind „Format falsch“, nicht „leer“).
        if isinstance(r, str) and len(r) <= MAX_ROH and putzen(r) == '':
            return {'format_ok': False, 'hinweis': 'Bitte fülle alle Felder aus.'}
        w = eingabe(r, feld['art'])
        if w is None:
            return {'format_ok': False, 'hinweis': 'In dieses Feld gehört eine ganze Zahl, zum Beispiel −3.' if feld['art'] == 'ganz'
                    else 'Bitte gib eine Zahl ein, zum Beispiel −3, 2,5 oder 3/4.'}
        if not feld.get('min', FELD_MIN) <= w <= feld.get('max', FELD_MAX):
            return {'format_ok': False, 'hinweis': 'Diese Zahl liegt außerhalb des erlaubten Bereichs.'}
        werte.append(w)
    zu_gross = {'format_ok': False, 'hinweis': 'Mit diesen Zahlen wird die Rechnung zu groß. Nimm kleinere Zahlen.'}
    for bed in beds:
        try:
            ok = _wahr(wert(bed['pruefe'], werte))
        except Grenze:
            ok = False
        except ZuGross:
            return zu_gross
        if not ok:
            aus = {'format_ok': True, 'richtig': False, 'verletzt': bed['name']}
            if bed.get('hinweis'):
                text = bed['hinweis']
                if '{}' in text:
                    try:
                        text = text.replace('{}', deutsch(wert(bed['zeige'], werte)))
                    except Grenze:
                        text = None
                    except ZuGross:
                        return zu_gross
                if text:
                    aus['hinweis'] = text
            return aus
    return {'format_ok': True, 'richtig': True}


LOESUNG_SCHLUESSEL = {'bedingungen', 'beispiel', 'gut', 'gegenbeispiele'}


def pruefe_aufgabe(a, nur_form=False):
    """Prüft eine Aufgabe beim Einlesen der Inhalte. Rückgabe: Liste von Fehlertexten (leer = in Ordnung).
    nur_form=True prüft genau das, was auch die Datenbank prüft (schule.bed_gueltig): Aufbau, Grenzen, Typen und das Beispiel –
    ohne „gut“ und Gegenbeispiele. Beide müssen dabei für jede Aufgabe zum selben Urteil kommen."""
    fehler = []
    felder = (a.get('f') or {}).get('felder')
    o = a.get('o') or {}
    if not nur_form and isinstance(o, dict) and set(o) - LOESUNG_SCHLUESSEL:  # die Datenbank prüft das im Constraint aufgabe_bedingung_gueltig
        fehler.append('Lösung: nur ' + ', '.join(sorted(LOESUNG_SCHLUESSEL)) + ' erlaubt, nicht ' + ', '.join(sorted(set(o) - LOESUNG_SCHLUESSEL)))
    beds = o.get('bedingungen')
    if not isinstance(felder, list) or not 1 <= len(felder) <= MAX_FELDER:
        return [f'felder: 1 bis {MAX_FELDER} Felder nötig']
    for i, f in enumerate(felder, 1):
        if not isinstance(f, dict) or f.get('art') not in ARTEN:
            fehler.append(f'Feld {i}: art muss {" oder ".join(ARTEN)} sein')
        elif ganzwert(f.get('min', FELD_MIN)) is None or ganzwert(f.get('max', FELD_MAX)) is None:
            fehler.append(f'Feld {i}: min/max müssen ganze Zahlen sein')
        elif not FELD_MIN <= f.get('min', FELD_MIN) <= f.get('max', FELD_MAX) <= FELD_MAX:
            fehler.append(f'Feld {i}: min/max außerhalb der Grenzen')
    if not isinstance(beds, list) or not 1 <= len(beds) <= MAX_BEDINGUNGEN:
        return fehler + [f'bedingungen: 1 bis {MAX_BEDINGUNGEN} nötig']
    namen = set()
    for b in beds:
        name = b.get('name') if isinstance(b, dict) else None
        if not isinstance(name, str) or not name or name in namen:
            fehler.append(f'Bedingung ohne eigenen Namen (nichtleerer Text): {str(name)[:40]!r}')
            continue
        namen.add(name)
        if 'hinweis' in b and not isinstance(b['hinweis'], str):
            fehler.append(f'{name}: hinweis muss Text sein')
            continue
        try:
            n = knoten(b.get('pruefe'), 1, len(felder))
            if typ(b.get('pruefe')) != 'wahr':
                raise ValueError('pruefe muss wahr oder falsch liefern')
            if '{}' in (b.get('hinweis') or ''):
                n += knoten(b.get('zeige'), 1, len(felder))
                if typ(b.get('zeige')) != 'zahl':
                    raise ValueError('zeige muss eine Zahl liefern')
            elif 'zeige' in b:
                fehler.append(f'{name}: zeige ohne {{}} im hinweis')
            if n > MAX_KNOTEN:
                fehler.append(f'{name}: mehr als {MAX_KNOTEN} Knoten')
        except ValueError as e:
            fehler.append(f'{name}: {e}')
    if fehler:
        return fehler

    def lauf(werte, was):
        try:
            return bewerte(a, {'werte': werte})
        except ValueError as e:
            fehler.append(f'{was} {werte}: {e}')
            return None

    gut = [o.get('beispiel')] + ([] if nur_form else list(o.get('gut') or []))
    if not isinstance(o.get('beispiel'), list):
        fehler.append('beispiel fehlt (eine richtige Antwort, die dem Kind als „Zum Beispiel“ gezeigt wird)')
        gut = gut[1:]
    for g in gut:
        r = lauf(g, 'beispiel')
        if r is not None and not (r['format_ok'] and r.get('richtig')):
            fehler.append(f'beispiel {g} besteht nicht: {r}')
    if nur_form:
        return fehler
    gegen = o.get('gegenbeispiele') or []
    if not gegen:
        fehler.append('gegenbeispiele fehlen (mindestens eine falsche Antwort mit der Bedingung, an der sie scheitert)')
    for g in gegen:
        r = lauf(g.get('werte'), 'gegenbeispiel')
        if r is not None and not (r['format_ok'] and r.get('richtig') is False and r.get('verletzt') == g.get('verletzt')):
            fehler.append(f'gegenbeispiel {g.get("werte")} soll an „{g.get("verletzt")}“ scheitern, liefert aber {r}')
    offen = namen - {g.get('verletzt') for g in gegen}
    if gegen and offen:
        fehler.append('ohne Gegenbeispiel: ' + ', '.join(sorted(offen)))
    return fehler


def haupt():
    datei = Path(__file__).resolve().parent / 'tests' / 'bedingung_faelle.json'
    daten = lade_json(datei.read_text(encoding='utf-8'))
    fehler, n = [], 0
    for a in daten['aufgaben']:
        for f in pruefe_aufgabe(a):
            fehler.append(f'{a["id"]}: {f}')
        n += 1 + len(a['o'].get('gut') or []) + len(a['o'].get('gegenbeispiele') or [])
    for fall in daten['format']:
        a = next(x for x in daten['aufgaben'] if x['id'] == fall['aufgabe'])
        r = bewerte(a, fall['antwort'])
        n += 1
        if r['format_ok'] is not fall['format_ok']:
            fehler.append(f'Format {fall["antwort"]} bei {fall["aufgabe"]}: erwartet format_ok={fall["format_ok"]}, ist {r}')
    for fall in daten['hinweise']:
        a = next(x for x in daten['aufgaben'] if x['id'] == fall['aufgabe'])
        r = bewerte(a, {'werte': fall['werte']})
        n += 1
        if r.get('hinweis') != fall['hinweis']:
            fehler.append(f'Hinweis {fall["werte"]} bei {fall["aufgabe"]}: erwartet {fall["hinweis"]!r}, ist {r.get("hinweis")!r}')
    for fall in daten['unzulaessig']:
        n += 1
        if not pruefe_aufgabe(fall['aufgabe']):
            fehler.append(f'Unzulässige Aufgabe wird nicht abgewiesen: {fall["warum"]}')
    if fehler:
        print('\n'.join(fehler))
        sys.exit(1)
    print(f'OK – {len(daten["aufgaben"])} Aufgaben, {n} Prüfungen')


if __name__ == '__main__':
    haupt()
