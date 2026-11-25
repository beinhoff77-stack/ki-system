import json,collections,sys
d=json.load(open('/tmp/lp/inhalte/pruefung/lehrplan/lk_daten_2211.json'))
t=json.load(open('/tmp/lp/inhalte/pruefung/lehrplan/lk_teilung_2211.json'))
T=json.load(open('/tmp/lpw/punkttexte.json'))
SP={'gym':'gym_by','rs_I':'rs_I','rs_II_III':'rs_II_III','ib_standard':'ib_standard','ib_extended':'ib_extended'}
sch=sys.argv[1]
H=collections.defaultdict(list)
for p in d['punkte']:
    if p['bezug']=='haupt' and SP[sch] in p['spuren']: H[p['thema']].append(p)
for th in t['etappen_kuer']:
    un=[e for e in th['etappen'] if sch in e['kuer_in']]
    if not un or not H[th['thema']]: continue
    print(f"## {th['thema']} {th['titel']}")
    for p in H[th['thema']]: print(f"  P{p['eintrag_id']} K{p['klasse']}: {T.get(str(p['eintrag_id']),'?')[:110]} -> {','.join(p['etappen'])}")
    print('  KÜR?: '+' | '.join(f"{e['lernziel']}={e['titel']}" for e in un))
