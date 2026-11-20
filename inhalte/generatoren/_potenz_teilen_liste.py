"""Sechsundzwanzigste Runde (Zweig potenz-teilen): Themenliste und kann-Texte nachziehen, mit Selbstprüfung.

Aufruf (einmal, nach den Generatoren): python3 -I inhalte/generatoren/_potenz_teilen_liste.py
Ändert nur gezielt: zwei neue Einträge (102, 103), Reihenfolgen der betroffenen Klassen, Titel/Umfang/Lehrplan von
terme.potenzgesetze; kann-Dateien der vier Flüge. Ein zweiter Lauf ändert nichts mehr (prüft nur).
Format der Themenliste bleibt: json.dumps(indent=1), nur einzeilige "klasse"-Objekte wie bisher einzeilig.
"""
import json
import re
import sys
from pathlib import Path

INHALTE = Path(__file__).resolve().parent.parent
LISTE = INHALTE / 'themenliste.json'
KANN = INHALTE / 'kann'
THEMEN = INHALTE / 'themen'
IB = 'MYP 4 Numerical and abstract reasoning (Zahl und Algebra)'

NEU_A = {
    'thema_id': 102, 'thema_schluessel': 'terme.potenzgesetze_natuerlich', 'block_id': 62, 'ort': 'Samarkand', 'gebiet': 'Algebra',
    'titel': 'Potenzgesetze', 'klasse': {'gym_by': 7, 'rs_by': 7, 'ib_myp': 4}, 'reihenfolge': {'gym_by': 2, 'rs_by': 2, 'ib_myp': 1},
    'lernbereich': {'gym_by': 'M7 1 Terme mit Variablen', 'rs_by': 'M7 1 Potenzen', 'ib_myp': IB},
    'umfang': 'Potenzen mit natürlichen Exponenten zusammenfassen: bei gleicher Basis malnehmen und teilen, bei gleichem Exponenten die Basen '
              'zusammenfassen, die Gesetze geschickt nutzen.',
    'lehrplan_gym': ['M7 1.2 Produkte von Potenzen mit natürlichen Exponenten bei gleicher Basis oder gleichem Exponenten zusammenfassen'],
    'lehrplan_rs': ['Potenzgesetze anwenden, zuerst mit natürlichen Exponenten (Aufteilung auf zwei Flüge: Annahme)'],
    'lehrplan_ib': ['MYP 4–5 Standard (Annahme): Potenzgesetze, hier mit natürlichen Exponenten'],
    'datei': 'inhalte/themen/terme.potenzgesetze_natuerlich.json'}
NEU_B = {
    'thema_id': 103, 'thema_schluessel': 'terme.potenzgesetze_ganzzahlig', 'block_id': 60, 'ort': 'Mumbai', 'gebiet': 'Algebra',
    'titel': 'Potenzgesetze mit ganzzahligen Exponenten', 'klasse': {'gym_by': 8, 'rs_by': 7, 'ib_myp': 4},
    'reihenfolge': {'gym_by': 8, 'rs_by': 3, 'ib_myp': 2},
    'lernbereich': {'gym_by': 'M8 4 Bruchterme und Bruchgleichungen', 'rs_by': 'M7 1 Potenzen', 'ib_myp': IB},
    'umfang': 'Potenzgesetze für ganzzahlige Exponenten plausibel machen und anwenden: gleiche Basis malnehmen und teilen, gleicher Exponent, '
              'Potenz einer Potenz, Terme mit Variablen vereinfachen und als Bruchterm schreiben.',
    'lehrplan_gym': ['M8 4 Rechengesetze für Potenzen mit ganzzahligen Exponenten plausibel machen und in einfachen Fällen anwenden'],
    'lehrplan_rs': ['Potenzen mit negativen ganzzahligen Exponenten; Potenzgesetze auch mit negativen Exponenten anwenden'],
    'lehrplan_ib': ['MYP 4–5 Standard: Potenzgesetze mit ganzzahligen und negativen Exponenten'],
    'datei': 'inhalte/themen/terme.potenzgesetze_ganzzahlig.json'}
# Verschiebung: (Schulart, Klasse, ab Nummer, um) – nur Themen mit genau dieser Klasse in dieser Schulart, ohne die neuen.
SCHIEBEN = [('gym_by', 7, 2, 1), ('gym_by', 8, 8, 1), ('rs_by', 7, 2, 2), ('ib_myp', 4, 1, 2)]
POTENZ6 = {
    'titel': 'Potenzen und negative Exponenten',
    'umfang': 'Potenzen mit natürlichen und negativen ganzzahligen Exponenten berechnen, auch mit Brüchen, Dezimalzahlen und negativer Basis; '
              'Hoch 0; typische Fehler mit einer Zahlenprobe finden.',
    'lehrplan_gym': ['Negative ganzzahlige Exponenten als Kehrbruch deuten und anwenden',
                     'Potenzen mit rationaler Basis und natürlichen Exponenten berechnen',
                     'Typische Fehler bei Potenzen mit einer Zahlenprobe erkennen (Vertiefung)'],
    'lehrplan_rs': ['Potenzen mit negativen ganzzahligen Exponenten (die Potenzgesetze stehen in eigenen Flügen)'],
    'lehrplan_ib': ['Annahme: Potenzen und negative Exponenten (die Potenzgesetze stehen in eigenen Flügen)']}

KANN_A = {'thema_schluessel': 'terme.potenzgesetze_natuerlich',
          'kurz': 'Du lernst, Potenzen mit gleicher Basis oder gleichem Exponenten geschickt zusammenzufassen.',
          'etappen': None}  # die vier Texte unverändert aus kann/terme.umformen.json
KANN_B = {'thema_schluessel': 'terme.potenzgesetze_ganzzahlig',
          'kurz': 'Du lernst, warum die Regeln für Potenzen auch mit negativen Hochzahlen gelten, und rechnest damit.',
          'etappen': {'warum_gilt': 'mit Zahlenproben zeigen, dass die Potenzgesetze auch für negative Exponenten gelten',
                      'gleiche_basis_ganz': 'Potenzen mit gleicher Basis malnehmen und teilen, auch mit negativen Exponenten',
                      'exponent_und_potenz': 'Potenzen mit gleichem Exponenten zusammenfassen und Potenzen von Potenzen vereinfachen',
                      'terme_vereinfachen': 'Terme wie 6x³ · x⁻⁵ vereinfachen und ohne negativen Exponenten als Bruch schreiben',
                      'fehler_ganz': 'Fehler mit negativen Exponenten finden und mit einer Zahlenprobe prüfen'}}
KANN_POTENZ6 = {'fehler_finden': 'Fehler bei Potenzen und negativen Exponenten finden und mit einer Zahlenprobe prüfen'}
LZ_A = ('mal_gleiche_basis', 'gleicher_exponent', 'geteilt_gleiche_basis', 'anwenden')


def _dump(d):
    t = json.dumps(d, ensure_ascii=False, indent=1) + '\n'
    return t


def _liste_text(d, alt_text):
    """Wie json.dumps(indent=1); "klasse"-Objekte, die im alten Text einzeilig standen, bleiben einzeilig."""
    t = _dump(d)
    # Einträge, deren "klasse" im alten Text einzeilig stand (Schlüssel steht vor "klasse" im selben Eintrag)
    einzeilig = re.findall(r'"thema_schluessel": "([^"]+)",(?:(?!"thema_schluessel")[\s\S])*?"klasse": (\{[^\n{}]*\})', alt_text)
    for schl, e in einzeilig:
        lang = '"klasse": ' + json.dumps(json.loads(e), ensure_ascii=False, indent=1).replace('\n', '\n  ')
        i = t.index(f'"thema_schluessel": "{schl}"')
        j = t.index(lang, i)
        assert '"thema_schluessel"' not in t[i + 1:j], schl
        t = t[:j] + '"klasse": ' + e + t[j + len(lang):]
    return t


def themenliste():
    alt_text = LISTE.read_text(encoding='utf-8')
    d = json.loads(alt_text)
    schl = [x['thema_schluessel'] for x in d]
    if NEU_A['thema_schluessel'] in schl:
        print('Themenliste: schon nachgezogen, nur Prüfung')
        return d
    for sa, kl, ab, um in SCHIEBEN:
        for x in d:
            if x['klasse'].get(sa) == kl and x['reihenfolge'].get(sa, 0) >= ab: x['reihenfolge'][sa] += um
    p6 = next(x for x in d if x['thema_schluessel'] == 'terme.potenzgesetze')
    p6.update(POTENZ6)
    i = schl.index('terme.umformen')
    d.insert(i, NEU_A)
    j = [x['thema_schluessel'] for x in d].index('terme.bruchterme')
    d.insert(j + 1, NEU_B)
    neu_text = _liste_text(d, alt_text)
    # Nur die erwarteten Stellen geändert: alte Einträge bis auf Reihenfolge und terme.potenzgesetze gleich
    alt = {x['thema_schluessel']: x for x in json.loads(alt_text)}
    for x in json.loads(neu_text):
        a = alt.get(x['thema_schluessel'])
        if a is None: continue
        if x['thema_schluessel'] == 'terme.potenzgesetze':
            assert {k: v for k, v in x.items() if k not in POTENZ6} == {k: v for k, v in a.items() if k not in POTENZ6}
        else:
            assert {k: v for k, v in x.items() if k != 'reihenfolge'} == {k: v for k, v in a.items() if k != 'reihenfolge'}, x['thema_schluessel']
    LISTE.write_text(neu_text, encoding='utf-8')
    return json.loads(neu_text)


def selbstpruefung(d):
    fehler = []
    zeilen = []
    for sa in ('gym_by', 'rs_by', 'ib_myp'):
        for kl in sorted({x['klasse'][sa] for x in d if sa in x['klasse']}):
            xs = sorted([x for x in d if x['klasse'].get(sa) == kl], key=lambda x: x['reihenfolge'].get(sa, 0))
            nr = [x['reihenfolge'].get(sa) for x in xs]
            lueckenlos = nr == list(range(1, len(xs) + 1))
            lb = [x['lernbereich'].get(sa) for x in xs]
            folge = [b for i, b in enumerate(lb) if i == 0 or b != lb[i - 1]]
            zus = len(folge) == len(set(folge))
            zeilen.append(f'{sa:7} Kl. {kl:2}: {len(xs):2} Themen · Nummern 1–{len(xs)} lückenlos/eindeutig: {"ja" if lueckenlos else "NEIN"} · '
                          f'Lernbereiche zusammenhängend: {"ja" if zus else "NEIN"} ({len(set(lb))} Überschriften)')
            if not lueckenlos: fehler.append(f'{sa} {kl}: Nummern {nr}')
            if not zus and not (sa == 'gym_by' and kl == 6): fehler.append(f'{sa} {kl}: Lernbereich unterbrochen {folge}')
    for x in d:
        f = INHALTE.parent / x['datei']
        if not f.exists(): fehler.append(f'Datei fehlt: {x["datei"]}')
    for n in (NEU_A, NEU_B):
        x = next(x for x in d if x['thema_schluessel'] == n['thema_schluessel'])
        t = json.loads((THEMEN / f'{n["thema_schluessel"]}.json').read_text(encoding='utf-8'))
        assert (t['thema_id'], t['block_id'], t['klasse']) == (x['thema_id'], x['block_id'], x['klasse'])
        assert set(x) == set(next(y for y in d if y['thema_schluessel'] == 'terme.umformen')), sorted(set(x))
    return zeilen, fehler


def kann():
    um = json.loads((KANN / 'terme.umformen.json').read_text(encoding='utf-8'))
    if any(k in um['etappen'] for k in LZ_A):
        texte_a = {k: um['etappen'][k] for k in LZ_A}
        um['etappen'] = {k: v for k, v in um['etappen'].items() if k not in LZ_A}
        (KANN / 'terme.umformen.json').write_text(_dump(um), encoding='utf-8')
        ka = dict(KANN_A, etappen=texte_a)
        (KANN / 'terme.potenzgesetze_natuerlich.json').write_text(_dump(ka), encoding='utf-8')
        (KANN / 'terme.potenzgesetze_ganzzahlig.json').write_text(_dump(KANN_B), encoding='utf-8')
        p6 = json.loads((KANN / 'terme.potenzgesetze.json').read_text(encoding='utf-8'))
        p6['etappen'].update(KANN_POTENZ6)
        (KANN / 'terme.potenzgesetze.json').write_text(_dump(p6), encoding='utf-8')
    # Selbstprüfung wie AB-I: jede Etappe genau ein Eintrag, keine überzähligen, Längen
    zeilen, fehler = [], []
    for t in ('terme.potenzgesetze_natuerlich', 'terme.potenzgesetze_ganzzahlig', 'terme.umformen', 'terme.potenzgesetze'):
        k = json.loads((KANN / f'{t}.json').read_text(encoding='utf-8'))
        lz = [e['lernziel'] for e in json.loads((THEMEN / f'{t}.json').read_text(encoding='utf-8'))['inhalt']['etappen']]
        if k['thema_schluessel'] != t: fehler.append(f'{t}: thema_schluessel')
        if sorted(k['etappen']) != sorted(lz): fehler.append(f'{t}: Etappen {sorted(k["etappen"])} ≠ {sorted(lz)}')
        if len(k['kurz']) > 110: fehler.append(f'{t}: kurz {len(k["kurz"])} Zeichen')
        for l, s in k['etappen'].items():
            if len(s) > 90 or s.endswith('.'): fehler.append(f'{t}/{l}: „{s}“ ({len(s)} Zeichen)')
        zeilen.append(f'{t}: kurz {len(k["kurz"])} Zeichen, {len(k["etappen"])} Etappen, längster kann-Text '
                      f'{max(len(s) for s in k["etappen"].values())} Zeichen')
    return zeilen, fehler


if __name__ == '__main__':
    d = themenliste()
    z1, f1 = selbstpruefung(d)
    z2, f2 = kann()
    print('\n'.join(z1 + z2))
    if f1 + f2:
        print('FEHLER:\n- ' + '\n- '.join(f1 + f2)); sys.exit(1)
    print('Selbstprüfung: OK')
