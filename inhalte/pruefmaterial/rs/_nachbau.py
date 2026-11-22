#!/usr/bin/env python3
"""Auftrag PM 2, Teil B: nachgebaute Schulaufgaben zu jeder katalogisierten RS-Arbeit mit Einzelaufgaben.

Aufruf (Repo-Wurzel):  python3 inhalte/pruefmaterial/rs/_nachbau.py      (benötigt sympy: pip install sympy)
Liest katalog.json, inhalte/themen/*.json und inhalte/pruefung/lehrplan/lk_teilung_2211.json.
Schreibt nur nach inhalte/pruefmaterial/rs/nachbau/ (<arbeit_id>.md, README.md) und nachbau.json.
Jede Aufgabe wird neu erzeugt (eigene Zahlen, eigene Kontexte); jede Lösung wird im Skript nachgerechnet.
"""
import collections
import glob
import hashlib
import json
import math
import random
import sys
from fractions import Fraction as Fr
from pathlib import Path

HIER = Path(__file__).resolve().parent
WURZEL = HIER.parents[2]
sys.path.insert(0, str(HIER))

from _nachbau_kern import Kern, check, formen, punkte_weg, z  # noqa: E402
import _nachbau_fam_zahl as FZ  # noqa: E402
import _nachbau_fam_alg as FA  # noqa: E402
import _nachbau_fam_geo as FG  # noqa: E402
import _nachbau_fam_daten as FD  # noqa: E402

AUS = HIER / 'nachbau'


# ---------- Zuordnung Katalogzeile → Aufgabenfamilie ----------
def erzeuge(rng, x):
    t, e, niv = x['thema'], x['etappe'], x['niveau'] if x['niveau'] in ('I', 'II', 'III') else 'II'
    info = {'typ': x['typ'], 'besonderheit': x['besonderheit'], 'kompetenz': x['kompetenz']}
    if t == 'LÜCKE':
        return luecke(rng, niv, info), luecke_zuordnung(x)
    if t == 'bruch.rechnen':
        return (FZ.f_ganz_sach(rng, niv, info, e) if e == 'sach' else FZ.f_qterm(rng, niv, info, e)), None
    if t == 'zahlen.ganz':
        if e in ('ketten', 'addieren'):
            return FZ.f_qterm(rng, niv, info, e), None
        if e in ('ordnen', 'zahlengerade', 'betrag'):
            return FZ.f_ordnen(rng, niv, info, e), None
        if e == 'umkehraufgabe':
            return FZ.f_umkehr(rng, niv, info, e), None
        return FZ.f_ganz_sach(rng, niv, info, e), None
    if t == 'bruch.dezimal':
        return (FZ.f_ordnen(rng, niv, info, e) if e == 'vergleichen_ordnen' else FZ.f_dezimal(rng, niv, info, e)), None
    if t == 'bruch.brueche':
        return FZ.f_brueche(rng, niv, info, e), None
    if t in ('bruch.prozent', 'bruch.prozent_grundwert'):
        return FZ.f_prozent(rng, niv, info, e), None
    if t == 'finanzen.zinsen':
        return FZ.f_zins(rng, niv, info, e), None
    if t in ('groessen.proportional', 'groessen.indirekt'):
        return FZ.f_prop(rng, niv, info, e, t == 'groessen.indirekt'), None
    if t == 'groessen.einheiten':
        return FZ.f_einheiten(rng, niv, info, e), None
    if t == 'zahlen.natuerlich':
        return FZ.f_stellenwert(rng, niv, info, e), None
    if t == 'zahlen.potenzen_zehner':
        return FZ.f_zehner(rng, niv, info, e), None
    if t in ('terme.potenzgesetze', 'terme.potenzgesetze_natuerlich'):
        return FZ.f_potenz(rng, niv, info, e, t), None
    if t == 'terme.umformen':
        return FA.f_umformen(rng, niv, info, e), None
    if t == 'terme.aufstellen':
        return FA.f_aufstellen(rng, niv, info, e), None
    if t in ('gleichungen.linear', 'gleichungen.einfach'):
        return FA.f_gleichung(rng, niv, info, 'waage' if t == 'gleichungen.einfach' else e), None
    if t == 'gleichungen.ungleichungen':
        return FA.f_ungl(rng, niv, info, e), None
    if t in ('gleichungen.bruch', 'terme.bruchterme'):
        return FA.f_bruch_alg(rng, niv, info, e, t), None
    if t == 'terme.quadratische_extreme':
        return FA.f_quad(rng, niv, info, e), None
    if t.startswith('funktionen.'):
        return FA.f_funktion(rng, niv, info, e, t), None
    if t in ('geometrie.winkelsaetze', 'geometrie.winkel'):
        e2 = {'kreuzung': 'stufen_wechsel', 'beweisen': 'figuren'}.get(e, e)
        return FG.f_winkel(rng, niv, info, e2), None
    if t == 'abbildungen.kongruenz':
        if e in ('vektor_koordinaten', 'gegenvektor', 'verschiebung', 'vektor_drehen'):
            return FG.f_vektor(rng, niv, info, e), None
        return FG.f_abbildung(rng, niv, info, e), None
    if t == 'abbildungen.determinanten2':
        return FG.f_det(rng, niv, info, e), None
    if t == 'geometrie.konstruktion':
        return FG.f_konstruktion(rng, niv, info, e), None
    if t == 'geometrie.kreis':
        return FG.f_kreis(rng, niv, info, e), None
    if t == 'geometrie.ortslinien':
        return FG.f_ort(rng, niv, info, e), None
    if t == 'geometrie.grundbegriffe':
        return FG.f_raum(rng, niv, info, 'lage', t), None
    if t == 'messen.kreisberechnung':
        return FG.f_kreisber(rng, niv, info, e), None
    if t in ('messen.flaechen', 'messen.flaechen_vielecke'):
        return FG.f_flaeche(rng, niv, info, e, t), None
    if t in ('messen.volumen', 'messen.prisma_zylinder'):
        return FG.f_volumen(rng, niv, info, e, t), None
    if t in ('raum.schraegbilder', 'messen.koerper_darstellung'):
        return FG.f_raum(rng, niv, info, e, t), None
    if t.startswith('daten.'):
        return FD.f_daten(rng, niv, info, {'kennwerte': 'kennwerte'}.get(e, e)), None
    if t.startswith('stochastik.'):
        return FD.f_stoch(rng, niv, info, e), None
    raise KeyError(f'keine Familie für {t}·{e}')


def luecke(rng, niv, info):
    b = info['besonderheit'] + ' ' + info['kompetenz']
    if 'Mittelpunkt' in b or 'Streckenmitte' in b or 'Endpunkt' in b or 'Eckpunkt' in b:
        if 'Endpunkt' in b or 'Eckpunkt' in b or 'rückwärts' in b:
            info = dict(info, besonderheit=info['besonderheit'] + ' rückwärts')
        return FG.f_mittelpunkt(rng, niv, info)
    if 'Vektoraddition' in b or 'verketten' in b:
        return FG.f_vektoraddition(rng, niv, info)
    if 'Seiten-Winkel' in b:
        return FG.f_konstruktion(rng, niv, info, 'seiten_winkel')
    if 'Teilbarkeit' in b:
        return teilbarkeit(rng, niv, info)
    if 'Würfel' in b:
        return wuerfel(rng, niv, info)
    if 'Parabel' in b or 'Graph des Terms' in b or 'wie 8a' in b:
        return parabel(rng, niv, info)
    raise KeyError(b)


def luecke_zuordnung(x):
    b = x['besonderheit'] + ' ' + x['kompetenz']
    if 'Mittelpunkt' in b or 'Streckenmitte' in b or 'Endpunkt' in b or 'Eckpunkt' in b:
        return ('abbildungen.kongruenz', 'LÜCKE: Mittelpunkt einer Strecke (vorgeschlagen)')
    if 'Vektoraddition' in b or 'verketten' in b:
        return ('abbildungen.kongruenz', 'LÜCKE: Verschiebungen verketten (vorgeschlagen)')
    if 'Seiten-Winkel' in b:
        return ('geometrie.konstruktion', 'LÜCKE: Seiten-Winkel-Beziehung (vorgeschlagen)')
    if 'Teilbarkeit' in b:
        return ('zahlen.natuerlich', 'LÜCKE: Teilbarkeitsregeln (vorgeschlagen)')
    if 'Würfel' in b:
        return ('messen.koerper_darstellung', 'LÜCKE: Würfel kippen / Würfelbau (vorgeschlagen)')
    return ('terme.quadratische_extreme', 'LÜCKE: Graph eines quadratischen Terms skizzieren (vorgeschlagen)')


def teilbarkeit(rng, niv, info):
    if 'begründen' in info['typ'] or rng.random() < .4:
        a = rng.choice(NAMEN_T)
        return Kern('', f'{a} behauptet: „Die Summe von drei aufeinanderfolgenden natürlichen Zahlen ist immer durch 3 teilbar.“ Stimmt das? Begründe allgemein.',
                    'Ja: n + (n + 1) + (n + 2) = 3n + 3 = 3(n + 1)', ['Zahlen allgemein mit n, n + 1, n + 2 bezeichnen.', 'Summe = 3(n + 1) ist ein Vielfaches von 3.'],
                    [('Nein', 'nur an Beispielen geprüft')], [check('Beispiele 1..50', all((n + n + 1 + n + 2) % 3 == 0 for n in range(50)))],
                    aussage=(f'{a} behauptet: „Die Summe von drei aufeinanderfolgenden natürlichen Zahlen ist immer durch 3 teilbar.“ Stimmt das? Begründe allgemein.', True,
                             'n + (n + 1) + (n + 2) = 3n + 3 = 3 · (n + 1) ist immer ein Vielfaches von 3.'))
    t1, t2 = rng.choice([(3, 4), (3, 5), (2, 9), (4, 9), (6, 7)])
    kand = [n for n in range(100, 1000) if n % t1 == 0 and n % t2 == 0 and n % 10 != 0]
    n = rng.choice(kand)
    return Kern('', f'Gib eine dreistellige Zahl an, die durch {t1} und durch {t2} teilbar ist, aber nicht auf 0 endet. Begründe mit Teilbarkeitsregeln.', f'z. B. {n}',
                [f'Teilbar durch {t1} und {t2} heißt teilbar durch {t1 * t2 // math.gcd(t1, t2)}.', f'{n} : {t1 * t2 // math.gcd(t1, t2)} = {n // (t1 * t2 // math.gcd(t1, t2))}'],
                [(str(n + 1), 'Regel nicht geprüft')], [check('Teilbarkeit', n % t1 == 0 and n % t2 == 0)])


NAMEN_T = ['Mila', 'Jonas', 'Ella', 'Timo', 'Nora']


def wuerfel(rng, niv, info):
    a, b, c = rng.randint(2, 4), rng.randint(2, 4), rng.randint(2, 3)
    innen = max(a - 2, 0) * max(b - 2, 0) * max(c - 2, 0)
    gesamt = a * b * c
    return Kern(f'Aus kleinen Würfeln wird ein Quader mit {a} × {b} × {c} Würfeln gebaut und anschließend außen rot angemalt.',
                'Wie viele kleine Würfel werden verwendet? Wie viele davon haben gar keine rote Fläche?', f'{gesamt} Würfel; {innen} ohne Farbe',
                [f'{a} · {b} · {c} = {gesamt}', f'Innen liegen ({a} − 2) · ({b} − 2) · ({c} − 2) = {innen} Würfel'], [(f'{gesamt}; {gesamt - 2 * (a * b + b * c + a * c)}', 'Kanten und Ecken doppelt abgezogen')],
                [check('Abzählen', innen == sum(1 for i in range(a) for j in range(b) for k in range(c) if 0 < i < a - 1 and 0 < j < b - 1 and 0 < k < c - 1))])


def parabel(rng, niv, info):
    h, k = rng.randint(-3, 3), rng.randint(-4, 3)
    xs = [h - 2, h - 1, h, h + 1, h + 2]
    ys = [(x - h) ** 2 + k for x in xs]
    return Kern(f'Gegeben ist T(x) = (x {"−" if h > 0 else "+"} {abs(h)})² {"+" if k >= 0 else "−"} {abs(k)}.', 'Lege eine Wertetabelle für fünf passende x-Werte an, skizziere den Graphen und gib den Tiefpunkt an.',
                f'Tiefpunkt S({z(h)} | {z(k)}); Werte: ' + '; '.join(f'({z(x)} | {z(y)})' for x, y in zip(xs, ys)), ['Scheitel aus der Klammer ablesen: x = ' + str(h), 'symmetrisch dazu je zwei Werte einsetzen'],
                [(f'S({z(-h)} | {z(k)})', 'Vorzeichen in der Klammer falsch gedeutet')], [check('Werte', all(y >= k for y in ys) and ys[2] == k)])


# ---------- Teile nach lk_teilung_2211.json ----------
def teil_karte():
    ids = {}
    titel = {}
    for f in glob.glob(str(WURZEL / 'inhalte/themen/*.json')):
        th = json.loads(Path(f).read_text(encoding='utf-8'))
        ids[th['thema_schluessel']] = th['thema_id']
        titel[th['thema_schluessel']] = {e['lernziel']: e.get('titel', '') for e in th['inhalt'].get('etappen', [])}
    lk = json.loads((WURZEL / 'inhalte/pruefung/lehrplan/lk_teilung_2211.json').read_text(encoding='utf-8'))
    teil = {}
    for t in lk['teilungsliste']:
        for tt in t['teile']:
            for e in tt['etappen']:
                teil[(t['thema'], e['lernziel'])] = f"Teil {tt['teil']} von {tt['von']} ({tt.get('untertitel', '')})"
    return ids, titel, teil


# ---------- Punkte und Zeit ----------
GEWICHT = {'I': 2, 'II': 3, 'III': 4}


def zahl(s):
    try:
        return Fr(s.replace(',', '.'))
    except (ValueError, AttributeError):
        return None


def punkte_verteilen(arbeit, zeilen):
    gesamt = zahl(arbeit['punkte'].split()[0]) if arbeit['punkte'] else None
    p = [zahl(x['punkte']) for x in zeilen]
    fehlend = [i for i, v in enumerate(p) if v is None]
    if not fehlend:
        if gesamt is not None and sum(p) != gesamt:
            diff = gesamt - sum(p)
            if diff > 0:
                reihen = sorted(range(len(p)), key=lambda i: -GEWICHT.get(zeilen[i]['niveau'], 3))
                i = 0
                while diff > 0:
                    schritt = min(Fr(1), diff)
                    p[reihen[i % len(p)]] += schritt
                    diff -= schritt
                    i += 1
            else:
                p = halbpunkte(p, gesamt, zeilen)
        return p, sum(p), gesamt is not None
    gew = [GEWICHT.get(zeilen[i]['niveau'], 3) for i in fehlend]
    if gesamt is not None:
        rest = gesamt - sum(v for v in p if v is not None)
        if rest <= 0:
            rest = Fr(len(fehlend))
        roh = [Fr(rest) * g / sum(gew) for g in gew]
        ger = [Fr(max(1, round(r * 2)), 2) for r in roh]
        ger[-1] += rest - sum(ger)
        if ger[-1] <= 0:
            ger = [Fr(1)] * len(fehlend)
        for i, v in zip(fehlend, ger):
            p[i] = v
        return p, sum(p), True
    for i, g in zip(fehlend, gew):
        p[i] = Fr(g)
    return p, sum(p), False


def halbpunkte(gewichte, gesamt, zeilen):
    """Gesamtpunkte in halben Punkten nach Gewichten verteilen (größter Rest, mindestens ½ Punkt je Aufgabe)."""
    T = int(gesamt * 2)
    W = sum(gewichte)
    roh = [g * T / W for g in gewichte]
    ein = [max(1, int(r)) for r in roh]
    rest = T - sum(ein)
    reihen = sorted(range(len(ein)), key=lambda i: (-(roh[i] - int(roh[i])), -GEWICHT.get(zeilen[i]['niveau'], 3)))
    i = 0
    while rest > 0:
        ein[reihen[i % len(ein)]] += 1
        rest -= 1
        i += 1
    while rest < 0:
        j = max(range(len(ein)), key=lambda k: ein[k])
        ein[j] -= 1
        rest += 1
    return [Fr(e, 2) for e in ein]


def zeit(arbeit):
    try:
        return int(arbeit['zeit_min']), False
    except ValueError:
        art = arbeit['art'].lower()
        if any(w in art for w in ('stegreif', 'kurzprobe', 'test')):
            return 20, True
        return 45, True


# ---------- Ausgabe ----------
def bauen():
    kat = json.loads((HIER / 'katalog.json').read_text(encoding='utf-8'))
    ids, et_titel, teil = teil_karte()
    zeilen_je = collections.defaultdict(list)
    for x in kat['aufgaben']:
        if x['typ'] != 'Themenebene':
            zeilen_je[x['arbeit']].append(x)
    arbeiten = [a for a in kat['arbeiten'] if zeilen_je.get(a['id'])]
    reihen = {'7': 0, '8': 1, '6': 2}
    arbeiten.sort(key=lambda a: (reihen.get(a['stoff_klasse'], 9), a['gruppe'], a['id']))
    AUS.mkdir(exist_ok=True)
    ergebnis, fehler, n_pruef = [], [], 0
    for a in arbeiten:
        zeilen = zeilen_je[a['id']]
        pkt, summe, summe_wie_original = punkte_verteilen(a, zeilen)
        zmin, zannahme = zeit(a)
        aufg, gesehen = [], set()
        for x, p in zip(zeilen, pkt):
            for versuch in range(30):
                seed = int(hashlib.sha256(f"{a['id']}|{x['nr']}|{versuch}".encode()).hexdigest()[:12], 16)
                rng = random.Random(seed)
                kern, zuo = erzeuge(rng, x)
                text, loes, weg, form = formen(kern, x['typ'], rng)
                if text not in gesehen and kern.ok():
                    break
            gesehen.add(text)
            n_pruef += len(kern.pruef)
            if not kern.ok() or not kern.pruef:
                fehler.append(f"{a['id']} {x['nr']}: {[b for b, ok in kern.pruef if not ok] or 'keine Prüfung'}")
            thema, etappe = zuo if zuo else (x['thema'], x['etappe'])
            tid = ids.get(thema)
            aufg.append({
                'nr': x['nr'], 'punkte': float(p), 'niveau': x['niveau'], 'typ_original': x['typ'], 'form': form,
                'thema': thema, 'thema_id': tid, 'etappe': etappe,
                'etappe_titel': et_titel.get(thema, {}).get(etappe, ''),
                'teil': teil.get((tid, etappe), 'ungeteilt') if tid else 'ungeteilt',
                'lernbereich_lehrplan': x['lernbereich'], 'text': text, 'abbildung': kern.abb, 'antwort': loes,
                'weg': [{'schritt': w, 'punkte': float(pp) if pp is not None else None} for w, pp in zip(weg, punkte_weg(weg, p))],
                'pruefung': [{'was': b, 'ok': ok} for b, ok in kern.pruef],
            })
        gesamt_orig = zahl(a['punkte'].split()[0]) if a['punkte'] else None
        if gesamt_orig is not None and summe != gesamt_orig:
            fehler.append(f"{a['id']}: Punktesumme {summe} ≠ Original {gesamt_orig}")
        for x_ in aufg:
            if sum(Fr(w['punkte']).limit_denominator(2) for w in x_['weg'] if w['punkte'] is not None) != Fr(x_['punkte']).limit_denominator(2):
                fehler.append(f"{a['id']} {x_['nr']}: Teilpunkte ≠ Aufgabenpunkte")
        eintrag = {'id': f"NB-{a['id']}", 'original': a['id'], 'original_titel': a['titel'], 'original_link': a['url'], 'art': a['art'],
                   'klasse_geschrieben': a['klasse_geschrieben'], 'stoff_klasse': a['stoff_klasse'], 'gruppe': a['gruppe'], 'lehrplanstand_original': a['lehrplanstand'],
                   'zeit_min': zmin, 'zeit_annahme': zannahme, 'punkte': float(summe), 'punkte_wie_original': summe_wie_original,
                   'hilfsmittel': a['hilfsmittel'], 'zeitpunkt': a['zeitpunkt'],
                   'niveau_verteilung': dict(collections.Counter(x['niveau'] for x in zeilen)),
                   'themen': sorted({t['thema'] for t in aufg}), 'aufgaben': aufg}
        ergebnis.append(eintrag)
        (AUS / f"{a['id']}.md").write_text(markdown(eintrag), encoding='utf-8')
    # JSON: eine Arbeit je Zeile
    zeilen_json = [json.dumps(e, ensure_ascii=False) for e in ergebnis]
    (HIER / 'nachbau.json').write_text('{\n"stand": "2026-11-22",\n"hinweis": "Nachbau (Auftrag PM 2 B): eigene Aufgaben gleichen Typs, gleicher Kompetenz und gleichen Niveaus; keine Originaltexte, keine Originalzahlen. Erzeugt und nachgerechnet mit _nachbau.py.",\n"arbeiten": [\n'
                                       + ',\n'.join(zeilen_json) + '\n]\n}\n', encoding='utf-8')
    json.loads((HIER / 'nachbau.json').read_text(encoding='utf-8'))
    (AUS / 'README.md').write_text(uebersicht(ergebnis), encoding='utf-8')
    n_auf = sum(len(e['aufgaben']) for e in ergebnis)
    print(f'{len(ergebnis)} Arbeiten, {n_auf} Aufgaben, {n_pruef} Prüfungen, Fehler: {len(fehler)}')
    for f in fehler[:40]:
        print('  FEHLER', f)
    return 1 if fehler else 0


def pkt(v):
    v = Fr(v).limit_denominator(2)
    return z(v)


def markdown(e):
    gr = {'I': 'Wahlpflichtfächergruppe I', 'II/III': 'Wahlpflichtfächergruppe II/III'}.get(e['gruppe'], 'Gruppe nicht angegeben')
    niv = ', '.join(f"{k}: {v}" for k, v in sorted(e['niveau_verteilung'].items()))
    s = [f"# Nachbau {e['original']} – Mathematik Realschule, Stoff Klasse {e['stoff_klasse']}, {gr}", '',
         f"**{e['art']}** · Arbeitszeit {e['zeit_min']} min{' (Annahme)' if e['zeit_annahme'] else ''} · {pkt(e['punkte'])} Punkte"
         f"{'' if e['punkte_wie_original'] else ' (Original ohne Punkteangabe; Punkte nach Niveau verteilt)'} · Hilfsmittel: {e['hilfsmittel']}", '',
         f"Name: ______________________  Klasse: ______  Datum: __________  Punkte: ____ / {pkt(e['punkte'])}", '',
         '> Nachgebaute Aufgaben: gleicher Typ, gleiche Kompetenz und gleiches Niveau wie im Original, aber eigene Texte, Zahlen und Sachkontexte. '
         f"Vorbild: [{e['original']}]({e['original_link']}) (nicht kopiert). Zeitpunkt im Schuljahr laut Vorbild: {e['zeitpunkt']}. Niveauverteilung: {niv}.", '',
         '## Aufgaben', '']
    for a in e['aufgaben']:
        s.append(f"**Aufgabe {a['nr']}** ({pkt(a['punkte'])} P.)  ")
        s.append(a['text'])
        s.append('')
    s += ['---', '', '<div style="page-break-before: always"></div>', '', f"## Lösungsblatt {e['original']}", '']
    for a in e['aufgaben']:
        s.append(f"**{a['nr']}** ({pkt(a['punkte'])} P.) – {a['antwort']}  ")
        for w in a['weg']:
            s.append(f"- {w['schritt']}" + (f" *({pkt(w['punkte'])} P.)*" if w['punkte'] else ''))
        s.append('')
    s += ['## Zuordnung', '', '| Nr | P. | Niveau | Form | Thema · Etappe | Teil | Lehrplan |', '|---|---|---|---|---|---|---|']
    for a in e['aufgaben']:
        s.append(f"| {a['nr']} | {pkt(a['punkte'])} | {a['niveau']} | {a['form']} | {a['thema']} · {a['etappe']} | {a['teil']} | {a['lernbereich_lehrplan']} |")
    s.append('')
    return '\n'.join(s)


def uebersicht(erg):
    s = ['# Nachgebaute Prüfungen – Mathematik Realschule Bayern (Stoff 7 und 8)', '',
         'Auftrag PM 2, Teil B · Stand 22.11.2026 · erzeugt mit `../_nachbau.py` aus `../katalog.json`.', '',
         'Je Original-Arbeit mit Einzelaufgaben eine nachgebaute Arbeit: gleiche Arbeitszeit, gleiche Punktesumme (wo bekannt), gleiche Niveauverteilung und gleicher Themenmix. '
         'Alle Aufgaben haben eigene Texte, Zahlen und Kontexte; jede Lösung ist im Skript nachgerechnet (Prüfspalte in `../nachbau.json`). '
         'Zeichnungen und Konstruktionen werden beschrieben; ihre Kontrollwerte (Winkel, Koordinaten, Längen) sind nachgerechnet, die Zeichnung selbst nicht.', '']
    for st, titel in (('7', 'Stoff Klasse 7'), ('8', 'Stoff Klasse 8'), ('6', 'Stoff bis Klasse 6 (Grundwissentest 7)')):
        for gr in ('I', 'II/III', 'unbekannt'):
            sel = [e for e in erg if e['stoff_klasse'] == st and (e['gruppe'] == gr or (gr == 'unbekannt' and e['gruppe'] not in ('I', 'II/III')))]
            if not sel:
                continue
            s += [f'## {titel} · {"Gruppe " + gr if gr != "unbekannt" else "Gruppe nicht angegeben"} ({len(sel)})', '',
                  '| Nachbau | Art | Zeit | Punkte | Aufgaben | Themen |', '|---|---|---|---|---|---|']
            for e in sel:
                s.append(f"| [{e['original']}]({e['original']}.md) | {e['art']} | {e['zeit_min']} min{' (A)' if e['zeit_annahme'] else ''} | {pkt(e['punkte'])} | {len(e['aufgaben'])} | "
                         + ', '.join(f'`{t}`' for t in e['themen']) + ' |')
            s.append('')
    s.append('(A) = Arbeitszeit im Original nicht angegeben, Annahme: Schulaufgabe/Klassenarbeit 45 min, Stegreifaufgabe/Test 20 min.')
    return '\n'.join(s) + '\n'


if __name__ == '__main__':
    sys.exit(bauen())
