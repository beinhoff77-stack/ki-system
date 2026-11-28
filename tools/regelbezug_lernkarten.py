#!/usr/bin/env python3
"""RB-S: Zuordnung Lernkarte (Etappe) -> Regel(n) des Regel-Universums. Erzeugt inhalte/plan/regelbezug-lernkarten.json.

Gebraucht für (1) die Erklärkarte einer Lernkarte (Verweis auf die Regel) und (2) die Fehler-Rückmeldung bei Aufgaben OHNE eigene Regel
(Bestand vor den rollend-Runden und neue Aufgaben mit leerem Feld „regel“). Keine Regel wird geraten.

Regeln (in dieser Reihenfolge; die erste, die greift, entscheidet):
  quelle „aufgaben“: Unter den neuen Aufgaben dieser Lernkarte (inhalte/mathe-profi/rollend-*/*.json, Felder thema + lernkarte; _teilN zählt zum
                     Grundthema) haben mindestens 2 eine Regel und die häufigste Regel hat mindestens 2/3 der Aufgaben MIT Regel
                     -> Hauptregel. Weitere Regeln (höchstens 2): andere Regeln, die mindestens 2-mal vorkommen, nach Häufigkeit.
  quelle „thema“:    sonst, wenn das Thema in der Themenliste („themen“) GENAU EINER Kennung in kennungen.json steht und keine Aufgabe
                     dieser Lernkarte eine ANDERE Regel trägt -> diese Regel als Hauptregel, keine weiteren.
  quelle „offen“:    sonst. Keine Regel; die Lernkarte steht in „redaktion“ mit dem Grund und den Kandidaten (nur zur Ansicht, nicht zu verwenden).
Lernkarten des Bestands: inhalte/themen/<thema>.json -> inhalt.etappen[].lernziel. Ein geteiltes Thema (Datenbank: <thema>_teilN) hat
dieselben Lernkarten-Namen wie das Grundthema: nachschlagen unter dem Grundthema (Feld „teile“ listet die bekannten Teile).

Aufruf:  python3 -I tools/regelbezug_lernkarten.py            -> schreibt die Datei und druckt die Auszählung
         python3 -I tools/regelbezug_lernkarten.py --pruefen  -> schreibt nichts; Rückgabe 1, wenn die Datei nicht dem Stand entspricht
         python3 -I tools/regelbezug_lernkarten.py --zahlen   -> nur die Auszählung (JSON)
"""
import glob
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
ZIEL = WURZEL / 'inhalte/plan/regelbezug-lernkarten.json'
KLASSEN = (5, 8)   # die Jahrgänge, die gerade gelernt werden (Auszählung getrennt); Klasse nach gym_by


def grundthema(s):
    return re.sub(r'_teil\d+$', '', s or '')


GRUNDSTAND_BIS = 14   # Runden bis hier stehen für die Zuordnung „wie eingespielt“ fest (Auflage Werkstatt 1209: Runde 15 darf keiner Lernkarte die Regel entziehen)


def entscheiden(c, tr):
    """Regel einer Lernkarte aus den Regel-Zählungen c (Regel oder None -> Anzahl) und den Regeln tr, deren Themenliste das Thema nennt. -> (Eintrag, Grund)."""
    mit = Counter({r: n for r, n in c.items() if r})
    n_mit = sum(mit.values())
    e = None
    grund = None
    if n_mit >= 2:
        (top, n_top), = mit.most_common(1)
        gleich = [r for r, n in mit.items() if n == n_top]
        if len(gleich) == 1 and 3 * n_top >= 2 * n_mit:
            weitere = [r for r, n in mit.most_common() if r != top and n >= 2][:2]
            e = {'regel': top, 'weitere': weitere, 'quelle': 'aufgaben', 'aufgaben': n_mit, 'anteil': f'{n_top}/{n_mit}'}
        else:
            grund = f'Aufgaben uneinig ({", ".join(f"{r} {n}" for r, n in mit.most_common())})'
    if e is None and grund is None:
        if len(tr) == 1 and all(r == tr[0] for r in mit):
            e = {'regel': tr[0], 'weitere': [], 'quelle': 'thema'}
        elif len(tr) == 1:
            grund = f'Thema hat genau {tr[0]}, eine Aufgabe trägt aber {", ".join(r for r in mit if r != tr[0])}'
        elif not tr:
            grund = 'Thema steht in keiner Themenliste' + (f'; Aufgaben: {", ".join(mit)} (zu wenige)' if mit else '')
        else:
            grund = f'Thema steht bei {len(tr)} Regeln' + (f'; Aufgaben: {", ".join(f"{r} {n}" for r, n in mit.items())} (zu wenige)' if mit else '')
    if e is None:
        e = {'regel': None, 'weitere': [], 'quelle': 'offen'}
    return e, grund


def bauen():
    kenn = json.loads((WURZEL / 'inhalte/mathe-profi/regeln-uebersicht/kennungen.json').read_text(encoding='utf-8'))
    gueltig = {k['kennung'] for k in kenn['kennungen']}
    thema_regeln = defaultdict(set)
    for k in kenn['kennungen']:
        for t in k.get('themen') or []:
            thema_regeln[t].add(k['kennung'])
    themen = {}
    for p in sorted(glob.glob(str(WURZEL / 'inhalte/themen/*.json'))):
        d = json.loads(Path(p).read_text(encoding='utf-8'))
        themen[d['thema_schluessel']] = d
    # Regeln der neuen Aufgaben je (Grundthema, Lernkarte)
    aufg_alle, aufg_fest = defaultdict(Counter), defaultdict(Counter)   # Regel oder None; fest = nur Runden bis GRUNDSTAND_BIS
    for p in sorted(glob.glob(str(WURZEL / 'inhalte/mathe-profi/rollend-*/*.json'))):
        for e in json.loads(Path(p).read_text(encoding='utf-8'))['aufgaben']:
            r = e.get('regel') or None
            if r is not None and r not in gueltig: raise SystemExit(f'{e["kennung"]}: Regel {r} steht nicht in kennungen.json')
            aufg_alle[(grundthema(e.get('thema')), e['aufgabe']['l'])][r] += 1
            if int(re.search(r'rollend-(\d+)', p).group(1)) <= GRUNDSTAND_BIS: aufg_fest[(grundthema(e.get('thema')), e['aufgabe']['l'])][r] += 1
    plan = json.loads((WURZEL / 'inhalte/plan/rollend-einheiten.json').read_text(encoding='utf-8'))
    teile = {k: grundthema(k) for k in sorted(plan['einheiten']) if grundthema(k) != k}

    eintraege, redaktion = {}, []
    zahl = {'gesamt': Counter(), 'klasse5': Counter(), 'klasse8': Counter(), 'rest': Counter()}
    unbekannt = []
    for (t, l), c in aufg_alle.items():
        if t not in themen or l not in [x['lernziel'] for x in themen[t]['inhalt'].get('etappen', [])]:
            unbekannt.append(f'{t}/{l}')
    for t in sorted(themen):
        d = themen[t]
        kl = (d.get('klasse') or {}).get('gym_by')
        gruppe = 'klasse5' if kl == 5 else 'klasse8' if kl == 8 else 'rest'
        tr = sorted(thema_regeln.get(t, ()))
        lks = {}
        for et in d['inhalt'].get('etappen', []):
            l = et['lernziel']
            e, grund = entscheiden(aufg_alle.get((t, l), Counter()), tr)
            fest, _ = entscheiden(aufg_fest.get((t, l), Counter()), tr)
            if fest['regel'] is not None:
                # Eine eingespielte Zuordnung bleibt unverändert (Auflage 1209): Aufgaben späterer Runden ändern weder Hauptregel noch weitere Regeln dieser Karte,
                # auch wenn sie eine andere (Teil-)Regel tragen; sie zählen nur für Karten, die bis dahin offen waren.
                e, grund = fest, None
            if e['quelle'] == 'offen':
                redaktion.append({'thema': t, 'lernkarte': l, 'grund': grund, 'kandidaten': sorted(set(tr) | set(r for r in aufg_alle.get((t, l), Counter()) if r))})
            lks[l] = e
            for g in ('gesamt', gruppe): zahl[g][e['quelle']] += 1
        eintraege[t] = {'thema_id': d.get('thema_id'), 'klasse_gym_by': kl, 'lernkarten': lks}
    out = {
        'stand': 'erzeugt von tools/regelbezug_lernkarten.py – nicht von Hand ändern',
        'hinweis': 'Je Thema und Lernkarte (Etappe, lernziel): Hauptregel (Kennung aus kennungen.json) und bis zu zwei weitere. quelle: aufgaben | thema | offen '
                   '(offen = keine Regel, siehe redaktion). Geteilte Themen (<thema>_teilN) unter dem Grundthema nachschlagen.',
        'regeln_fuer_die_zuordnung': 'aufgaben: mindestens 2 neue Aufgaben der Lernkarte mit Regel und die häufigste hat mindestens 2/3; '
                                     'thema: das Thema steht in der Themenliste genau einer Kennung und keine Aufgabe der Lernkarte widerspricht; sonst offen.',
        'teile': teile,
        'themen': eintraege,
        'redaktion': redaktion,
    }
    zahlen = {g: {'lernkarten': sum(c.values()), 'aufgaben': c['aufgaben'], 'thema': c['thema'], 'offen': c['offen']} for g, c in zahl.items()}
    return out, zahlen, unbekannt


def main():
    out, zahlen, unbekannt = bauen()
    if unbekannt:
        print('Neue Aufgaben mit Lernkarte, die es im Themenbestand nicht gibt (nicht gezählt):', ', '.join(sorted(set(unbekannt))), file=sys.stderr)
    text = json.dumps(out, ensure_ascii=False, indent=1) + '\n'
    if '--zahlen' in sys.argv:
        print(json.dumps(zahlen, ensure_ascii=False)); return
    if '--pruefen' in sys.argv:
        if not ZIEL.exists() or ZIEL.read_text(encoding='utf-8') != text:
            print('regelbezug-lernkarten.json ist nicht auf dem Stand – neu erzeugen', file=sys.stderr); sys.exit(1)
        print('OK'); return
    ZIEL.write_text(text, encoding='utf-8')
    for g, z in zahlen.items():
        print(f'{g:8} Lernkarten {z["lernkarten"]:4}: aus Aufgaben {z["aufgaben"]:4}, aus Thema {z["thema"]:4}, offen {z["offen"]:4}')
    print(f'geschrieben: {ZIEL.relative_to(WURZEL)} ({len(out["redaktion"])} Lernkarten zur Redaktion)')


if __name__ == '__main__':
    main()
