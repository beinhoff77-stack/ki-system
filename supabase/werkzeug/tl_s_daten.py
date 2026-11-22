# TL-S: Datenblock (v_daten) der Migration 20261123_tl_s_teilung.sql aus lk_teilung_2211.json erzeugen.
# Aufruf: python3 -I supabase/werkzeug/tl_s_daten.py inhalte/pruefung/lehrplan/lk_teilung_2211.json > daten.json – danach den $json$-Block ersetzen.
# erzeugt den Datenblock für TL-S aus inhalte/pruefung/lehrplan/lk_teilung_2211.json
import json, re, sys
j = json.load(open(sys.argv[1]))
SA = {'gym': 'gym_by', 'rs_I': 'rs_by', 'ib_standard': 'ib_myp'}          # DB kennt nur gym_by / rs_by / ib_myp
def kl(v): return v[0] if isinstance(v, list) and v else (v if not isinstance(v, list) else None)
plan = []
for t in j['teilungsliste']:
    teile = []
    for p in t['teile']:
        et = [e['lernziel'] for e in p['etappen']]
        zus = sorted({SA[k] for k, v in p['zusatz'].items() if v and k in SA})
        # Kür je Etappe und Schulart (LK-D 4: etappen[].kuer_in) → Pflicht-Etappen je Schulart; ohne Angabe: keine Abweichung
        pj = {}
        if any('kuer_in' in e for e in p['etappen']):   # Schlüssel je Gruppe (Regel: Gruppe vor Schulart)
            for k, s in {'gym': 'gym_by', 'rs_I': 'rs_I', 'rs_II_III': 'rs_II_III', 'ib_standard': 'myp_standard', 'ib_extended': 'myp_extended'}.items():
                pj[s] = [e['lernziel'] for e in p['etappen'] if k not in (e.get('kuer_in') or [])]
        teile.append({'teil': p['teil'], 'untertitel': p['untertitel'], 'etappen': et,
                      'klasse': {'gym_by': p['klasse'].get('gym'), 'rs_by': p['klasse'].get('rs_I'), 'ib_myp': kl(p['klasse'].get('ib_standard'))},
                      'zusatz': zus, 'pflicht_je_schulart': pj})
    plan.append({'thema': t['thema'], 'titel': t['titel'], 'teile': teile})
def knoten(s):
    m = re.match(r'(\d+) .*?(?: – Teil (\d+) von \d+)?$', s)
    return int(m.group(1)), (int(m.group(2)) if m.group(2) else None)
ids = {t['thema'] for t in plan}
kanten = []
for k in j['kanten']:
    a, at = knoten(k['braucht_von']); b, bt = knoten(k['braucht'])
    if a in ids or b in ids:
        # „Zusatz“ heißt: der abhängige Teil ist in dieser Schulart Zusatz – die Kante bleibt wie sie ist (kein Abweichen nach „empfohlen“);
        # nur ausdrückliches „hart“/„empfohlen“ weicht je Schulart ab. Voraussetzung Zusatz → empfohlen regelt die Migration selbst.
        js = {SA[s_]: v for s_, v in (k.get('art_je_schulart') or {}).items() if v in ('hart', 'empfohlen') and s_ in SA}
        kanten.append({'thema': a, 'thema_teil': at, 'braucht': b, 'braucht_teil': bt, 'art': k['art'] or 'empfohlen',   # ohne Gesamt-Art: global empfohlen, je Schulart laut Liste
                       'herkunft': 'Teilung' if k['herkunft'] == 'Teilung' else k['herkunft'], 'art_je_schulart': js})
print(json.dumps({'plan': plan, 'kanten': kanten}, ensure_ascii=False))
