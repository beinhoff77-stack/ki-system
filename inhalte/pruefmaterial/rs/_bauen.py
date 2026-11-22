#!/usr/bin/env python3
"""Baut aus erfassung.txt den Katalog (katalog.json, katalog.md) und Kennzahlen für auswertung.md.

Aufruf (aus dem Repo-Wurzelverzeichnis):  python3 -I inhalte/pruefmaterial/rs/_bauen.py
Liest nur Repo-Dateien; schreibt nur unter inhalte/pruefmaterial/rs/ (Kennzahlen zusätzlich nach stdout).
Keine Aufgabentexte: erfassung.txt enthält nur eigene Kurzbeschreibungen.
"""
import collections
import glob
import json
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[3]
HIER = Path(__file__).resolve().parent

KOPF = ['id', 'titel', 'herausgeber', 'art', 'klasse_geschrieben', 'stoff_klasse', 'gruppe', 'jahr', 'nr_im_jahr',
        'zeit_min', 'punkte', 'hilfsmittel', 'frei', 'lizenz', 'url', 'abruf', 'zeitpunkt']
ZEILE = ['nr', 'pkt', 'kompetenz', 'typ', 'niveau', 'lernbereich', 'thema', 'etappe', 'besonderheit']
TYP_NORM = {'konstruieren': 'zeichnen/konstruieren', 'zeichnen': 'zeichnen/konstruieren', 'Lücke': 'Lücke/ergänzen',
            'beschreiben': 'beschreiben (Fachsprache)', 'zuordnen': 'ankreuzen/zuordnen', 'ankreuzen': 'ankreuzen/zuordnen'}


def lesen():
    arbeiten, cur = [], None
    for z in (HIER / 'erfassung.txt').read_text(encoding='utf-8').splitlines():
        if not z.strip() or z.startswith('#'):
            continue
        teile = [t.strip() for t in z.split('|')]
        if z.startswith('@'):
            teile[0] = teile[0][1:].strip()
            assert len(teile) == len(KOPF), (len(teile), z)
            cur = dict(zip(KOPF, teile))
            cur['aufgaben'] = []
            arbeiten.append(cur)
        else:
            while len(teile) < len(ZEILE):
                teile.append('')
            assert len(teile) == len(ZEILE), z
            a = dict(zip(ZEILE, teile))
            if a['etappe'] == '?':  # Grundwissen-Rechenaufgabe ohne erkennbare Feinetappe
                a['etappe'] = 'gemischt'
            cur['aufgaben'].append(a)
    return arbeiten


def lehrplanstand(a):
    z = a['zeitpunkt']
    if 'unklar' in z:
        return 'unklar'
    if 'alter Lehrplan' in z or 'altem Lehrplan' in z or 'vor LehrplanPLUS' in z:
        return 'alt (vor LehrplanPLUS)'
    return 'LehrplanPLUS'


def themen_laden():
    et = {}
    for f in glob.glob(str(WURZEL / 'inhalte/themen/*.json')):
        th = json.loads(Path(f).read_text(encoding='utf-8'))
        et[th['thema_schluessel']] = {
            'id': th['thema_id'],
            'etappen': [e['lernziel'] for e in th['inhalt'].get('etappen', [])],
            'titel': {e['lernziel']: e.get('titel', '') for e in th['inhalt'].get('etappen', [])},
            'aufgaben': th.get('aufgaben', []),
        }
    return et


def lehrplan_rs78(themen):
    """Themen je (Stoff-Klasse, Gruppe) laut rs_pruefung_2211.json (Hauptzuordnung)."""
    d = json.loads((WURZEL / 'inhalte/pruefung/lehrplan/rs_pruefung_2211.json').read_text(encoding='utf-8'))
    id2key = {v['id']: k for k, v in themen.items()}
    res = collections.defaultdict(set)
    for p in d['punkte']:
        q = p['quelle']
        if q['schulart'] != 'rs' or q['klasse'] not in (7, 8):
            continue
        for z in p['zuordnung_vorschlag']:
            if z['bezug'] == 'haupt' and z['thema'] in id2key:
                res[(q['klasse'], q['gruppe'])].add(id2key[z['thema']])
    return res


def pruefen(arbeiten, themen):
    fehler = []
    for a in arbeiten:
        for x in a['aufgaben']:
            if x['thema'] == 'LÜCKE':
                if not x['besonderheit'].startswith('Vorschlag') and 'Vorschlag' not in x['besonderheit'] and 'wie ' not in x['besonderheit']:
                    fehler.append(f"{a['id']} {x['nr']}: Lücke ohne Vorschlag")
                continue
            if x['thema'] not in themen:
                fehler.append(f"{a['id']} {x['nr']}: unbekanntes Thema {x['thema']}")
            elif x['etappe'] not in ('–', '') and x['etappe'] not in themen[x['thema']]['etappen']:
                fehler.append(f"{a['id']} {x['nr']}: Etappe {x['etappe']} fehlt in {x['thema']}")
            if x['typ'] != 'Themenebene' and x['niveau'] not in ('I', 'II', 'III'):
                fehler.append(f"{a['id']} {x['nr']}: Niveau {x['niveau']}")
    return fehler


def zahl(p):
    try:
        return float(p.replace(',', '.'))
    except ValueError:
        return None


def main():
    themen = themen_laden()
    arbeiten = lesen()
    fehler = pruefen(arbeiten, themen)
    if fehler:
        print('\n'.join(fehler))
        sys.exit(1)
    lp = lehrplan_rs78(themen)

    # ---------- katalog.json ----------
    zeilen_arb, zeilen_auf = [], []
    for a in arbeiten:
        meta = {k: a[k] for k in KOPF}
        meta['lehrplanstand'] = lehrplanstand(a)
        meta['nur_themenebene'] = all(x['typ'] == 'Themenebene' for x in a['aufgaben'])
        meta['anzahl_aufgaben'] = sum(1 for x in a['aufgaben'] if x['typ'] != 'Themenebene')
        meta['themen_zusammen'] = sorted({x['thema'] for x in a['aufgaben'] if x['thema'] != 'LÜCKE'})
        zeilen_arb.append(meta)
        for x in a['aufgaben']:
            zeilen_auf.append({
                'arbeit': a['id'], 'stoff_klasse': a['stoff_klasse'], 'klasse_geschrieben': a['klasse_geschrieben'],
                'gruppe': a['gruppe'], 'art': a['art'], 'jahr': a['jahr'], 'lehrplanstand': meta['lehrplanstand'],
                'nr': x['nr'], 'punkte': x['pkt'], 'kompetenz': x['kompetenz'], 'typ': x['typ'], 'niveau': x['niveau'],
                'lernbereich': x['lernbereich'], 'thema': x['thema'], 'etappe': x['etappe'],
                'luecke': x['thema'] == 'LÜCKE', 'besonderheit': x['besonderheit'],
            })
    out = ['{', '"stand": "2026-11-22",',
           '"hinweis": "Katalog, keine Kopie: Kurzbeschreibungen in eigenen Worten; Aufgaben selbst nur über den Link. Niveau I/II/III und Zuordnung Thema/Etappe sind eigene Einschätzung. Quelle der Daten: erfassung.txt, gebaut mit _bauen.py.",',
           '"arbeiten": [']
    out += [json.dumps(z, ensure_ascii=False) + (',' if i < len(zeilen_arb) - 1 else '') for i, z in enumerate(zeilen_arb)]
    out += ['],', '"aufgaben": [']
    out += [json.dumps(z, ensure_ascii=False) + (',' if i < len(zeilen_auf) - 1 else '') for i, z in enumerate(zeilen_auf)]
    out += [']', '}']
    (HIER / 'katalog.json').write_text('\n'.join(out) + '\n', encoding='utf-8')
    json.loads((HIER / 'katalog.json').read_text(encoding='utf-8'))

    # ---------- katalog.md ----------
    md = ['# Katalog Prüfungsmaterial Mathematik Realschule Bayern, Klasse 7 und 8',
          '',
          'Stand 22.11.2026 · Chat `pruefmaterial-rs` · erzeugt aus `erfassung.txt` mit `_bauen.py`.',
          '',
          '**Katalog, keine Kopie:** Je Aufgabe nur eine eigene Kurzbeschreibung. Aufgaben und Lösungen stehen beim Herausgeber (Link). '
          'Niveau (I reproduzieren · II Zusammenhänge · III verallgemeinern/begründen) und die Zuordnung zu Thema/Etappe sind eigene Einschätzung.',
          '',
          '**Klasse geschrieben vs. Stoff-Klasse:** Die amtlichen ISB-Tests werden zu Schuljahresbeginn geschrieben und prüfen den Stoff des Vorjahres '
          '(Jahrgangsstufentest 8 → Stoff 7; Grundwissentest 9 → Stoff bis 8; Grundwissentest 7 → Stoff bis 6). Gezählt wird nach **Stoff-Klasse**.',
          '']
    def schluessel(a):
        return (a['stoff_klasse'], a['gruppe'], a['art'], a['id'])
    for stoff in ('6', '7', '8'):
        sel = [a for a in arbeiten if a['stoff_klasse'] == stoff]
        if not sel:
            continue
        md.append(f'## Stoff Klasse {stoff} ({len(sel)} Arbeiten)')
        md.append('')
        md.append('| Arbeit | Art | Gruppe | Jahr | Nr. | Zeit | Punkte | Lehrplan | Aufg. | Themen zusammen | Zeitpunkt | Link |')
        md.append('|---|---|---|---|---|---|---|---|---|---|---|---|')
        for a in sorted(sel, key=schluessel):
            m = next(z for z in zeilen_arb if z['id'] == a['id'])
            th = ', '.join(t.split('.', 1)[1] for t in m['themen_zusammen'])
            aufg = 'nur Themen' if m['nur_themenebene'] else str(m['anzahl_aufgaben'])
            md.append(f"| {a['id']} | {a['art']} | {a['gruppe']} | {a['jahr']} | {a['nr_im_jahr']} | {a['zeit_min']} | {a['punkte']} | "
                      f"{m['lehrplanstand']} | {aufg} | {th} | {a['zeitpunkt']} | [Link]({a['url']}) |")
        md.append('')
    md.append('## Aufgaben je Arbeit')
    md.append('')
    for a in sorted(arbeiten, key=schluessel):
        if all(x['typ'] == 'Themenebene' for x in a['aufgaben']):
            continue
        md.append(f"### {a['id']} – {a['titel']}")
        md.append('')
        md.append(f"{a['herausgeber']} · {a['art']} · geschrieben in Kl. {a['klasse_geschrieben']}, Stoff Kl. {a['stoff_klasse']} · Gruppe {a['gruppe']} · "
                  f"{a['zeit_min']} min · {a['punkte']} Punkte · Hilfsmittel: {a['hilfsmittel']} · frei zugänglich: {a['frei']} · Lizenz: {a['lizenz']} · "
                  f"abgerufen {a['abruf']} · [Quelle]({a['url']})")
        md.append('')
        md.append('| Nr | P. | Kompetenz (eigene Worte) | Typ | Niv. | Lernbereich | Thema · Etappe | Besonderheit |')
        md.append('|---|---|---|---|---|---|---|---|')
        for x in a['aufgaben']:
            te = f"**Lücke**" if x['thema'] == 'LÜCKE' else f"{x['thema']} · {x['etappe']}"
            md.append(f"| {x['nr']} | {x['pkt']} | {x['kompetenz']} | {x['typ']} | {x['niveau']} | {x['lernbereich']} | {te} | {x['besonderheit']} |")
        md.append('')
    (HIER / 'katalog.md').write_text('\n'.join(md) + '\n', encoding='utf-8')

    # ---------- Kennzahlen ----------
    k = []
    def gruppe_norm(g):
        return 'I' if g.startswith('I') and not g.startswith('II') else ('II/III' if g.startswith('II') else g)
    for stoff in ('7', '8'):
        for gr in ('I', 'II/III', 'unbekannt'):
            arb = [a for a in arbeiten if a['stoff_klasse'] == stoff and gruppe_norm(a['gruppe']) == gr]
            if gr == 'unbekannt':
                arb = [a for a in arbeiten if a['stoff_klasse'] == stoff and gruppe_norm(a['gruppe']) not in ('I', 'II/III')]
            auf = [(a, x) for a in arb for x in a['aufgaben'] if x['typ'] != 'Themenebene']
            if not arb:
                continue
            k.append(f'\n### Stoff {stoff} · Gruppe {gr}: {len(arb)} Arbeiten, davon {sum(1 for a in arb if any(x["typ"] != "Themenebene" for x in a["aufgaben"]))} mit Einzelaufgaben, {len(auf)} Aufgaben')
            lpc = collections.Counter(lehrplanstand(a) for a in arb)
            k.append('Lehrplanstand: ' + ', '.join(f'{v} {n}' for n, v in lpc.most_common()))
            arten = collections.Counter(a['art'].split(' (')[0].split(' –')[0] for a in arb)
            k.append('Arten: ' + ', '.join(f'{n} {v}' for n, v in arten.most_common()))
            if not auf:
                continue
            niv = collections.Counter(x['niveau'] for _, x in auf)
            k.append('Niveau: ' + ', '.join(f'{n} {round(100 * niv[n] / len(auf))} %' for n in ('I', 'II', 'III')))
            typ = collections.Counter(TYP_NORM.get(x['typ'], x['typ']) for _, x in auf)
            k.append('Aufgabentyp: ' + ', '.join(f'{n} {v}' for n, v in typ.most_common()))
            bes = collections.Counter()
            for _, x in auf:
                for b in ('Fehler finden', 'rückwärts', 'Term aus Text', 'Term aus Figur', 'Gegenbeispiel', 'Fachsprache', 'Diagramm', 'Graph', 'Modellieren', 'offen', 'Grundwissen', 'alter Lehrplan', 'mehrere Bedingungen', 'Ortsbereich', 'binomisch', 'Knobel'):
                    if b.lower() in x['besonderheit'].lower():
                        bes[b] += 1
                if x['typ'] == 'begründen':
                    bes['begründen (Typ)'] += 1
            k.append('Besonderheiten: ' + ', '.join(f'{n} {v}' for n, v in bes.most_common()))
            thc = collections.Counter(x['thema'] for _, x in auf)
            k.append('Themen: ' + ', '.join(f'{n} {v}' for n, v in thc.most_common()))
            etc = collections.Counter(f"{x['thema']}·{x['etappe']}" for _, x in auf if x['thema'] != 'LÜCKE')
            k.append('Etappen (Top 25): ' + ', '.join(f'{n} {v}' for n, v in etc.most_common(25)))
            lu = collections.Counter(x['besonderheit'].split(';')[0] for _, x in auf if x['thema'] == 'LÜCKE')
            k.append('Lücken: ' + ' | '.join(f'{v}× {n}' for n, v in lu.most_common()))
            if gr in ('I', 'II/III'):
                soll = lp.get((int(stoff), gr), set())
                gesehen = {(x['thema'], x['etappe']) for a in arbeiten if a['stoff_klasse'] in ('7', '8', '6') for x in a['aufgaben']}
                gesehen_gr = {(x['thema'], x['etappe']) for _, x in auf}
                nie = []
                for t in sorted(soll):
                    for e in themen[t]['etappen']:
                        if (t, e) not in gesehen:
                            nie.append(f'{t}·{e}')
                k.append(f'Etappen der Lehrplan-Themen (Stoff {stoff}, {gr}) ohne jedes Vorkommen im ganzen Katalog: ' + ', '.join(nie))
                nur_gr = [f'{t}·{e}' for t in sorted(soll) for e in themen[t]['etappen'] if (t, e) not in gesehen_gr and (t, e) in gesehen]
                k.append(f'… in dieser Gruppe nicht, aber anderswo: ' + ', '.join(nur_gr))
            # Aufbau echte Schulaufgaben mit Punkten
            sa = [a for a in arb if a['art'].startswith(('Schulaufgabe', 'Übungs-Schulaufgabe')) and any(x['typ'] != 'Themenebene' for x in a['aufgaben'])]
            for a in sa:
                pk = [zahl(x['pkt']) for x in a['aufgaben'] if x['typ'] != 'Themenebene']
                hauptnr = {x['nr'].rstrip('abcdefghαβ').split('.')[0] for x in a['aufgaben']}
                k.append(f"Schulaufgabe {a['id']}: Zeit {a['zeit_min']}, Punkte {a['punkte']}, Teilaufgaben {len(pk)}, Hauptaufgaben {len(hauptnr)}, Themen {len({x['thema'] for x in a['aufgaben']})}")
    # Themenkombinationen
    k.append('\n### Themenkombinationen je Arbeit (alle Arbeiten mit ≥ 2 Themen)')
    for a in sorted(arbeiten, key=schluessel):
        th = sorted({x['thema'] for x in a['aufgaben'] if x['thema'] != 'LÜCKE'})
        if a['art'].startswith(('Schulaufgabe', 'Übungs-Schulaufgabe', 'Übungs-Stegreif', 'Klassenarbeit')):
            k.append(f"{a['id']} ({a['zeitpunkt'].split(';')[0]}): {', '.join(th)}")
    # Flug-Test-Abgleich: Testaufgaben unserer Themen
    k.append('\n### Unsere Flug-Tests (Pool test) für die RS-7/8-Themen')
    alle = set().union(*[lp.get((s, g), set()) for s in (7, 8) for g in ('I', 'II/III')])
    for t in sorted(alle):
        auf = themen[t]['aufgaben']
        test = [x for x in auf if x.get('p') == 'test']
        y = collections.Counter(x.get('y') for x in test)
        k.append(f"{t}: {len(themen[t]['etappen'])} Etappen, {len(test)} Testaufgaben, Antwortformen {dict(y)}")
    yall = collections.Counter(x.get('y') for t in alle for x in themen[t]['aufgaben'])
    k.append('Antwortformen aller Aufgaben dieser Themen: ' + str(dict(yall)))
    print('\n'.join(k))
    print(f"\nOK: {len(arbeiten)} Arbeiten, {len(zeilen_auf)} Zeilen (davon Themenebene {sum(1 for z in zeilen_auf if z['typ'] == 'Themenebene')})")


if __name__ == '__main__':
    main()
