import sys, json, glob, collections
sys.path.insert(0, '/tmp/lpw')
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import lk_proc as L
ETT = {}
for f in glob.glob('/tmp/lp/inhalte/themen/*.json'):
    d = json.load(open(f)); ETT[d['thema_id']] = {e['lernziel']: e['titel'] for e in d['inhalt'].get('etappen', [])}
SP_ALL = ('gym_by', 'rs_I', 'rs_II_III', 'ib_standard', 'ib_extended')
def ek(sp, t, et):
    k = L.ERST.get((sp, t, et)); return None if k in (None, 99) else k
# --- Teilung: feinste gemeinsame Teilung über Gym und RS I
TEIL = {}     # t -> list of parts: dict(etappen, gym, rs_I)
OHNE = {}     # Etappen ohne Klasse in beiden Maßstab-Spuren
for t in sorted(L.TT):
    if t in L.STILL: continue
    ets = L.ET.get(t, [])
    gk = {et: ek('gym_by', t, et) for et in ets}; rk = {et: ek('rs_I', t, et) for et in ets}
    if len({v for v in gk.values() if v}) < 2 and len({v for v in rk.values() if v}) < 2: continue
    # Kombinationen; Platzhalter auffüllen
    combos = sorted({(gk[e], rk[e]) for e in ets if gk[e] and rk[e]})
    teile = []
    for c in combos: teile.append(dict(gym=c[0], rs_I=c[1], etappen=[e for e in ets if (gk[e], rk[e]) == c]))
    ohne = []
    for e in ets:
        if gk[e] and rk[e]: continue
        cand = [p for p in teile if (gk[e] is None or p['gym'] == gk[e]) and (rk[e] is None or p['rs_I'] == rk[e])]
        if gk[e] is None and rk[e] is None:
            ohne.append(e); continue
        if cand: cand[0]['etappen'].append(e)
        else:
            teile.append(dict(gym=gk[e], rs_I=rk[e], etappen=[e]))
    # Reihenfolge: nach (min Klasse über beide, gym, rs)
    def key(p): return (min(x for x in (p['gym'], p['rs_I']) if x), p['gym'] or 0, p['rs_I'] or 0)
    teile.sort(key=key)
    # Etappen ohne Lehrplanbezug: zum Teil der vorigen Etappe in Dateireihenfolge (sonst Teil 1)
    for e in ohne:
        i = ets.index(e); ziel = teile[0]
        for prev in reversed(ets[:i]):
            pz = next((p for p in teile if prev in p['etappen']), None)
            if pz: ziel = pz; break
        ziel['etappen'].append(e); ziel.setdefault('ohne_lehrplan', []).append(e)
    for p in teile: p['etappen'] = [e for e in ets if e in p['etappen']]
    if len(teile) >= 2: TEIL[t] = teile
# Fehlende Maßstab-Klasse eines Teils (Etappen nur in einer Schulart): Klasse der anderen Schulart offen -> aus Nachbar ableiten
for t, ts in TEIL.items():
    for sp in ('gym', 'rs_I'):
        for i, p in enumerate(ts):
            if p[sp] is None:
                if not any(q[sp] for q in ts): continue
                vor = [q[sp] for q in ts[:i] if q[sp]]
                p[sp + '_abgeleitet'] = True
                p[sp] = max(vor) if vor else min(q[sp] for q in ts if q[sp])
    for p in ts:
        for sp in ('rs_II_III', 'ib_standard', 'ib_extended'):
            ks = sorted({ek(sp, t, e) for e in p['etappen'] if ek(sp, t, e)})
            p[sp] = ks
print('geteilt:', {t: [(p['gym'], p['rs_I'], len(p['etappen'])) for p in ts] for t, ts in TEIL.items()})

# ---------- Knoten (Thema oder Teil) und Klassen je Spur
def knoten(t):
    return [(t, i) for i in range(len(TEIL[t]))] if t in TEIL else [(t, None)]
def klasse(n, sp):
    t, i = n
    if i is None:
        return L.klasse_ab(sp, t)
    p = TEIL[t][i]
    if sp == 'gym_by': return p['gym']
    if sp == 'rs_I': return p['rs_I']
    ks = p[sp]
    if ks: return ks[0]
    # Etappen dieses Teils in der Spur nicht verlangt: Thema dort insgesamt?
    return None
def name(n):
    t, i = n
    if i is None: return f"{t} {L.TT[t]}"
    return f"{t} {L.TT[t]} – Teil {i + 1} von {len(TEIL[t])}"
def passt(src, dst):
    for sp in ('gym_by', 'rs_I'):
        a, b = klasse(src, sp), klasse(dst, sp)
        if a is not None and b is not None and b > a: return False
    return True
KANTEN = []   # (src, dst, art, herkunft)
# inhaltliche Zuordnung (Annahme), wo die Klassenregel einen späteren Teil wählen würde, der Inhalt aber nur Teil 1 braucht
INHALT = {(47, 46): 0, (44, 46): 0, (4, 29): 0}
for v in L.V:
    t, b, art = v['t'], v['b'], v['art']
    if t in L.STILL or b in L.STILL: continue
    if (t, b) in INHALT:
        KANTEN.append((knoten(t)[0], (b, INHALT[(t, b)]), art, 'bisher (inhaltlich zugeordnet)')); continue
    gesetzt = False
    for p in knoten(t):
        qs = [q for q in knoten(b) if passt(p, q)]
        if qs:
            KANTEN.append((p, qs[-1], art, 'bisher')); gesetzt = True; break
    if not gesetzt: KANTEN.append((knoten(t)[0], knoten(b)[0], art, 'bisher'))
for t in TEIL:
    for i in range(1, len(TEIL[t])): KANTEN.append(((t, i), (t, i - 1), 'hart', 'Teilung'))
HART_NUTZER = {(102, 30)}
VERSTOSS = []
for src, dst, art, her in KANTEN:
    for sp in SP_ALL:
        a, b = klasse(src, sp), klasse(dst, sp)
        if a is None: continue
        if b is None:
            VERSTOSS.append(dict(spur=sp, braucht_von=name(src), braucht=name(dst), art=art, herkunft=her, klasse=a, klasse_vor=None, befund='Voraussetzung in dieser Spur kein Lehrplanstoff'))
        elif b > a:
            VERSTOSS.append(dict(spur=sp, braucht_von=name(src), braucht=name(dst), art=art, herkunft=her, klasse=a, klasse_vor=b, befund='Voraussetzung liegt später'))
for x in VERSTOSS:
    t = int(x['braucht_von'].split()[0]); b = int(x['braucht'].split()[0])
    x['nutzer_hart'] = (t, b) in HART_NUTZER
print('Kanten', len(KANTEN), 'Verstöße', collections.Counter((x['spur'], x['befund'][:22]) for x in VERSTOSS))
for x in VERSTOSS:
    if x['spur'] in ('gym_by', 'rs_I'): print(x)
if len(sys.argv) > 1:
    for x in VERSTOSS:
        if x['spur'] in ('rs_II_III', 'ib_standard'): print(x['spur'], x['braucht_von'], '<-', x['braucht'], x['art'], x['herkunft'], x['klasse'], x['klasse_vor'])
    for s, d, a, h in KANTEN:
        if s[0] in TEIL or d[0] in TEIL: print('K', name(s), '<-', name(d), a, h)
for t, ts in TEIL.items():
    for i, p in enumerate(ts):
        st = {k: (len(set(p['etappen']) & L.ERL[(k, t)]), len(p['etappen'])) for k in (1, 2)}
        p['stand'] = st
if len(sys.argv) > 1 and sys.argv[1] == 'teile':
    for t, ts in TEIL.items():
        print(t, L.TT[t], 'Flug:', [k for k in (1, 2) if (k, t) in L.FLUG])
        for i, p in enumerate(ts):
            print('  T', i + 1, 'gym', p['gym'], p.get('gym_abgeleitet', ''), 'rsI', p['rs_I'], p.get('rs_I_abgeleitet', ''), 'II', p['rs_II_III'], 'IB', p['ib_standard'], p['ib_extended'], p['stand'])
            print('     ', [(e, ETT[t][e]) for e in p['etappen']], 'ohne LP:', p.get('ohne_lehrplan'))

# ---------- Ausgabe
UT = {26: ['Dreisatz', 'proportionale Zuordnungen erkennen'], 29: ['zusammenfassen und ausmultiplizieren', 'Summe mal Summe, binomische Formeln, Gleichungen mit Klammern'],
      44: ['Dreiecke konstruieren, Kongruenz', 'Vierecke'], 46: ['Spiegeln und Symmetrie', 'Verschieben und Vektoren', 'Drehen und Punktspiegelung'],
      61: ['Ergebnis, Ereignis, relative Häufigkeit', 'Laplace-Wahrscheinlichkeit'], 91: ['Schrägbilder und Lage im Raum', 'Raumkoordinaten, Körpersymmetrie, Rotationskörper'],
      101: ['gerade Prismen und Zylinder', 'schiefe Körper und Cavalieri']}
def kl_txt(n):
    out = {}
    for sp in SP_ALL:
        t, i = n
        if i is not None and sp in ('rs_II_III', 'ib_standard', 'ib_extended'):
            ks = TEIL[t][i][sp]; out[sp] = ks or None
        else:
            k = klasse(n, sp); out[sp] = [k] if k else None
    return out
def kurz(n):
    k = kl_txt(n)
    g = k['gym_by'][0] if k['gym_by'] else '–'; r = k['rs_I'][0] if k['rs_I'] else '–'
    return f"{name(n)} (Gym {g} · RS I {r})"
EIN = collections.defaultdict(list); AUS = collections.defaultdict(list)
for s, d, a, h in KANTEN:
    EIN[s].append((d, a, h)); AUS[d].append((s, a, h))
LISTE = []
for t, ts in TEIL.items():
    teile = []
    for i, p in enumerate(ts):
        n = (t, i)
        teile.append(dict(teil=i + 1, von=len(ts), titel=f"{L.TT[t]} – Teil {i + 1} von {len(ts)}", untertitel=UT[t][i],
                          etappen=[dict(lernziel=e, titel=ETT[t][e]) for e in p['etappen']], etappen_ohne_lehrplanpunkt=p.get('ohne_lehrplan', []),
                          klasse=dict(gym=p['gym'], gym_ohne_eigenen_punkt=bool(p.get('gym_abgeleitet')), rs_I=p['rs_I'], rs_I_ohne_eigenen_punkt=bool(p.get('rs_I_abgeleitet')),
                                      rs_II_III=p['rs_II_III'] or None, ib_standard=p['ib_standard'] or None, ib_extended=p['ib_extended'] or None),
                          zu_duenn=len(p['etappen']) <= 2,
                          stand_je_kind={str(k): dict(erledigt=v[0], etappen=v[1], vollstaendig=v[0] == v[1]) for k, v in p['stand'].items()},
                          baut_auf=[dict(knoten=kurz(d), art=a, herkunft=h) for d, a, h in EIN[n]],
                          wird_gebraucht_von=[dict(knoten=kurz(s), art=a, herkunft=h) for s, a, h in AUS[n]]))
    LISTE.append(dict(thema=t, titel=L.TT[t], teile=teile, flug_geschafft_kinder=[k for k in (1, 2) if (k, t) in L.FLUG]))

# ---------- LK-D 4 B1: Pflicht/Kür je Etappe, Schulart und Gruppe mit Quellen-Punkt
sys.path.insert(0, '/tmp/lpw'); import lk_kuer_entscheid as KE
ENT = KE.lesen()
DATEN0 = json.load(open('/tmp/lp/inhalte/pruefung/lehrplan/lk_daten_2211.json'))
PKT = {p['eintrag_id']: p for p in DATEN0['punkte']}
SCH_SP = {'gym': 'gym_by', 'rs_I': 'rs_I', 'rs_II_III': 'rs_II_III', 'ib_standard': 'ib_standard', 'ib_extended': 'ib_extended'}
GRUPPE = {'gym': 'Gymnasium', 'rs_I': 'Realschule Gruppe I', 'rs_II_III': 'Realschule Gruppe II/III', 'ib_standard': 'IB MYP Standard', 'ib_extended': 'IB MYP Extended'}
HP = collections.defaultdict(list); NP = collections.defaultdict(list)
for p in DATEN0['punkte']:
    for sp in p['spuren']:
        if p['bezug'] == 'haupt': HP[(p['thema'], sp)].append(p)
        for n in p['neben']: NP[(n, sp)].append(p)
STATUS = {}
OFFEN_ENT = []
for t in sorted(L.TT):
    if t in L.STILL: continue
    for e in L.ET.get(t, []):
        for sch, sp in SCH_SP.items():
            zug = [p for p in HP[(t, sp)] if e in p['etappen']]
            if zug:
                k0 = min(p['klasse'] for p in zug)
                st = dict(status='pflicht', art='zugeordnet', quelle=[p['eintrag_id'] for p in zug], klasse=k0, grund='Lehrplanpunkt verlangt die Etappe (Zuordnung)')
            elif (sch, t, e) in ENT:
                x, g = ENT[(sch, t, e)]
                if x == 'K': st = dict(status='kuer', art='entschieden', quelle=[], klasse=None, grund=g)
                else:
                    pid = int(x[1:]); st = dict(status='pflicht', art='integrativ', quelle=[pid], klasse=PKT[pid]['klasse'], grund=g)
            elif not HP[(t, sp)] and not NP[(t, sp)]:
                st = dict(status='kuer', art='kein_lehrplanstoff', quelle=[], klasse=None, grund='Thema hat in dieser Schulart/Gruppe keinen Haupt- oder Nebenbezug')
            elif sch.startswith('ib'):
                q = (HP[(t, sp)] or NP[(t, sp)])
                q0 = min(q, key=lambda p: (p['klasse'], p['eintrag_id']))
                st = dict(status='pflicht', art='integrativ_ib', quelle=[q0['eintrag_id']], klasse=q0['klasse'], grund='IB-Orientierung: das Kapitel umfasst die Etappe (Annahme, nicht einzeln geprüft)')
            else:
                st = dict(status='offen', art='offen', quelle=[], klasse=None, grund='nicht entschieden'); OFFEN_ENT.append((sch, t, e))
            st['gruppe'] = GRUPPE[sch]
            STATUS[(t, e, sch)] = st
assert not OFFEN_ENT, OFFEN_ENT[:20]
# ---------- Zusatz-Regel (Entscheidung 16:20): Teil ohne Lehrplanpunkt in der Schulart = Zusatz
SCHULEN = ('gym', 'rs_I', 'rs_II_III', 'ib_standard', 'ib_extended')
def zusatz(t, i, sch):   # LK-D 4: Teil ohne Pflicht-Etappe (nach B1) = Zusatz
    return not any(STATUS[(t, e, sch)]['status'] == 'pflicht' for e in TEIL[t][i]['etappen'])
KANTEN_SCHULART = []
for th in LISTE:
    t = th['thema']
    for i, tp in enumerate(th['teile']):
        tp['zusatz'] = {sch: zusatz(t, i, sch) for sch in SCHULEN}
    for sch in SCHULEN:
        for i in range(1, len(TEIL[t])):
            if zusatz(t, i, sch): continue   # Zusatz-Teil selbst: nichts Pflicht
            vor = [j for j in range(i) if not zusatz(t, j, sch)]
            if zusatz(t, i - 1, sch):
                KANTEN_SCHULART.append(dict(schulart=sch, braucht_von=name((t, i)), braucht=name((t, i - 1)), art='empfohlen', grund='Vorgänger ist in dieser Schulart Zusatz'))
                if vor:
                    KANTEN_SCHULART.append(dict(schulart=sch, braucht_von=name((t, i)), braucht=name((t, vor[-1])), art='hart', grund='letzter Pflicht-Teil davor'))
            else:
                KANTEN_SCHULART.append(dict(schulart=sch, braucht_von=name((t, i)), braucht=name((t, i - 1)), art='hart', grund='Teilung'))
# bisherige Voraussetzungen auf einen Zusatz-Teil: in dieser Schulart nur empfohlen
for s_, d_, a_, h_ in KANTEN:
    if d_[1] is None or a_ != 'hart' or h_ == 'Teilung': continue
    for sch in SCHULEN:
        if zusatz(d_[0], d_[1], sch):
            KANTEN_SCHULART.append(dict(schulart=sch, braucht_von=name(s_), braucht=name(d_), art='empfohlen', grund='Voraussetzung ist in dieser Schulart Zusatz'))

# ---------- F2: Art jeder Kante je Schulart (hart / empfohlen / Zusatz)
def zus(n, sch):
    return n[1] is not None and zusatz(n[0], n[1], sch)
KANTEN_OUT = []
for s_, d_, a_, h_ in KANTEN:
    je = {}
    for sch in SCHULEN:
        if zus(s_, sch): je[sch] = 'Zusatz'          # Teil selbst ist Zusatz: nichts Pflicht, sperrt nichts
        elif zus(d_, sch): je[sch] = 'empfohlen'      # Voraussetzung ist Zusatz
        else: je[sch] = a_
    KANTEN_OUT.append(dict(braucht_von=name(s_), braucht=name(d_), art=a_, herkunft=h_, art_je_schulart=je))
# zusätzliche Teilungskanten über einen Zusatz-Teil hinweg (z. B. Gym 46 Teil 3 ← Teil 1 hart)
for k in KANTEN_SCHULART:
    if k['grund'] == 'letzter Pflicht-Teil davor':
        x = next((o for o in KANTEN_OUT if o['braucht_von'] == k['braucht_von'] and o['braucht'] == k['braucht']), None)
        if not x:
            x = dict(braucht_von=k['braucht_von'], braucht=k['braucht'], art=None, herkunft='Teilung über Zusatz-Teil hinweg', art_je_schulart={})
            KANTEN_OUT.append(x)
        x['art_je_schulart'][k['schulart']] = 'hart'
for x in KANTEN_OUT:
    for sch in SCHULEN: x['art_je_schulart'].setdefault(sch, None)
# kanten_je_schulart: Zusatz-Teile ausdrücklich mit art „Zusatz“
for th in LISTE:
    t = th['thema']
    for sch in SCHULEN:
        for i in range(1, len(TEIL[t])):
            if zusatz(t, i, sch):
                KANTEN_SCHULART.append(dict(schulart=sch, braucht_von=name((t, i)), braucht=name((t, i - 1)), art='Zusatz', grund='Teil ist in dieser Schulart Zusatz: keine Pflicht, sperrt nichts'))
    for i, tp in enumerate(th['teile']):
        tp['status_je_schulart'] = {sch: ('Zusatz' if zusatz(t, i, sch) else 'Pflicht') for sch in SCHULEN}

# ---------- LK-D 4 (Entscheidung 17:05, Punkt 1): Kür je Etappe und Schulart
SCH_SP = {'gym': 'gym_by', 'rs_I': 'rs_I', 'rs_II_III': 'rs_II_III', 'ib_standard': 'ib_standard', 'ib_extended': 'ib_extended'}
VERT = {}
for f in glob.glob('/tmp/lp/inhalte/themen/*.json'):
    d = json.load(open(f)); VERT[d['thema_id']] = set(d['inhalt'].get('bewertung', {}).get('lernziele_vertiefung', []))
def kuer_in(t, e):
    return [sch for sch in SCHULEN if STATUS[(t, e, sch)]['status'] == 'kuer']
KIND_SCH = {1: 'gym', 2: 'gym'}   # beide echten Kinder: Gymnasium
for th in LISTE:
    t = th['thema']
    for i, tp in enumerate(th['teile']):
        for e in tp['etappen']:
            e['kuer_in'] = kuer_in(t, e['lernziel'])
            e['klasse_je_schulart'] = {sch: STATUS[(t, e['lernziel'], sch)]['klasse'] for sch in SCHULEN}
            e['status_je_schulart'] = {sch: STATUS[(t, e['lernziel'], sch)] for sch in SCHULEN}
        tp['pflicht_etappen_je_schulart'] = {sch: [e['lernziel'] for e in tp['etappen'] if sch not in e['kuer_in']] for sch in SCHULEN}
        alt = tp['stand_je_kind']
        tp['stand_je_kind_vorher'] = alt
        neu = {}
        for k, sch in KIND_SCH.items():
            pf = tp['pflicht_etappen_je_schulart'][sch]
            erl = [x for x in pf if x in L.ERL[(k, t)]]
            neu[str(k)] = dict(schulart=sch, pflicht=len(pf), erledigt=len(erl), vollstaendig=bool(pf) and len(erl) == len(pf),
                               nur_kuer=not pf, fehlt=[x for x in pf if x not in L.ERL[(k, t)]],
                               kuer_erledigt=len([e['lernziel'] for e in tp['etappen'] if sch in e['kuer_in'] and e['lernziel'] in L.ERL[(k, t)]]))
        tp['stand_je_kind'] = neu
# alle übrigen Themen (ungeteilt): Kür je Etappe und Stand je Kind
ETAPPEN_KUER = []
STAND_ALLE = []
for t in sorted(L.TT):
    if t in L.STILL or not L.ET.get(t): continue
    ets = [dict(lernziel=e, titel=ETT[t][e], kuer_in=kuer_in(t, e), klasse_je_schulart={sch: STATUS[(t, e, sch)]['klasse'] for sch in SCHULEN}, status_je_schulart={sch: STATUS[(t, e, sch)] for sch in SCHULEN},
                im_inhalt_vertiefung=e in VERT.get(t, set())) for e in L.ET[t]]
    ETAPPEN_KUER.append(dict(thema=t, titel=L.TT[t], geteilt=t in TEIL, etappen=ets))
    if t in TEIL: continue
    for k, sch in KIND_SCH.items():
        if not L.ERL[(k, t)] and (k, t) not in L.FLUG: continue
        pf = [e['lernziel'] for e in ets if sch not in e['kuer_in']]
        if not pf: continue   # Thema in der Schulart ohne Lehrplanpunkt
        erl = [x for x in pf if x in L.ERL[(k, t)]]
        alle = len(set(L.ET[t]) & L.ERL[(k, t)]) == len(L.ET[t])
        STAND_ALLE.append(dict(kind=k, thema=t, titel=L.TT[t], schulart=sch, pflicht=len(pf), erledigt=len(erl), vollstaendig=len(erl) == len(pf),
                               vorher_alle_etappen=alle, flug_geschafft=(k, t) in L.FLUG, fehlt=[x for x in pf if x not in L.ERL[(k, t)]]))
# Widerspruch Inhalt ↔ Lehrplan: Etappe im Inhalt als Vertiefung (für alle Kür), hat aber in einer Schulart einen Lehrplanpunkt
VERT_PFLICHT = [dict(thema=x['thema'], lernziel=e['lernziel'], pflicht_in=[s for s in SCHULEN if s not in e['kuer_in']])
                for x in ETAPPEN_KUER for e in x['etappen'] if e['im_inhalt_vertiefung'] and len(e['kuer_in']) < len(SCHULEN)]
# Grenzfälle: II/III oder IB verteilen (ohne Teilung durch Gym/RS I) bzw. ein Teil liegt dort in mehreren Klassen
GRENZ = []
for r in L.LAGE:
    t = r['thema']
    for sp in ('rs_II_III', 'ib_standard', 'ib_extended'):
        if t in TEIL:
            for i, p in enumerate(TEIL[t]):
                if len(p[sp]) > 1: GRENZ.append(dict(thema=t, titel=L.TT[t], teil=i + 1, spur=sp, klassen=p[sp], empfehlung='nicht teilen (löst keine Teilung aus); Anzeige „weitergeführt“'))
        else:
            ek_ = {int(k): v for k, v in r[sp]['etappen_je_klasse'].items()}
            if len(ek_) > 1: GRENZ.append(dict(thema=t, titel=L.TT[t], teil=None, spur=sp, klassen=sorted(ek_), etappen_je_klasse={str(k): v for k, v in ek_.items()}, empfehlung='nicht teilen (löst keine Teilung aus); Anzeige „weitergeführt“'))

# ---------- F1 (LK-D 3, Rückläufer 939/940): alle Themen mit Hauptpunkten in mehreren Klassen je Spur, gezählt gegen lk_daten_2211.json
DATEN = json.load(open('/tmp/lp/inhalte/pruefung/lehrplan/lk_daten_2211.json'))
SP_SCH = {'gym_by': 'gym', 'rs_I': 'rs_I', 'rs_II_III': 'rs_II_III', 'ib_standard': 'ib_standard', 'ib_extended': 'ib_extended'}
HK = collections.defaultdict(lambda: collections.defaultdict(list))
for p in DATEN['punkte']:
    if p['bezug'] != 'haupt': continue
    for sp in p['spuren']: HK[(p['thema'], sp)][p['klasse']].append(p)
BEGR = {
    (57, 'rs_I'): 'Kl. 7 (8 I 8/K4) verlangt dieselbe Fähigkeit wie Kl. 5 (6/k3, verzerrte Diagramme erkennen/berichtigen) auf höherem Niveau; die Etappe irrefuehrend deckt beides. Keine neue Etappe → kein eigener Flug.',
    (57, 'rs_II_III'): 'wie RS I: Kl. 7 (6/K4) = Kl. 5 (6/k3) auf höherem Niveau; Etappe irrefuehrend.',
    (46, 'rs_II_III'): 'Kl. 8 (Vierecke nach Eigenschaften unterscheiden) steckt in vierecke_ordnen aus Kl. 6; RS II/III löst ohnehin keine Teilung aus.',
}
MEHR = []
for (t, sp), kl in sorted(HK.items()):
    if len(kl) < 2 or t in L.STILL: continue
    gesehen = set(); kls = sorted(kl)
    for j, k in enumerate(kls):
        ets = [e for p in kl[k] for e in p['etappen']]
        neu_ = sorted(set(ets) - gesehen); gesehen |= set(ets)
        if j == 0: continue
        e = dict(thema=t, titel=L.TT[t], spur=sp, erste_klasse=kls[0], klasse=k, punkte=[p['eintrag_id'] for p in kl[k]], neue_etappen=neu_)
        if not neu_:
            e.update(entscheidung='wiederholung', anzeige=f'wird in Kl. {k} wieder aufgegriffen', neuer_flug=False)
        elif sp in ('gym_by', 'rs_I'):
            sch = SP_SCH[sp]; ti = [i for i, q in enumerate(TEIL.get(t, [])) if q[sch] == k and not q.get(sch + '_abgeleitet')]
            assert ti, (t, sp, k)   # Gym/RS I mit neuer Etappe muss geteilt sein
            e.update(entscheidung='geteilt', teil=ti[0] + 1, anzeige=f'eigener Teil {ti[0] + 1} von {len(TEIL[t])} in Kl. {k}', neuer_flug=True)
        else:
            e.update(entscheidung='grenzfall', anzeige=f'wird in Kl. {k} weitergeführt', neuer_flug=False)
        e['begruendung'] = BEGR.get((t, sp)) or {'wiederholung': 'In dieser Klasse ist keine Etappe zum ersten Mal verlangt: Wiederholung ohne neue Etappe, Grenzfall mit Anzeige.',
                                                  'geteilt': 'Die spätere Klasse verlangt eigene Etappen; Gym/RS I sind Maßstab der Teilung.',
                                                  'grenzfall': f'{sp} löst keine Teilung aus (Regel 15:30/15:35); neue Etappen dort nur als Anzeige „weitergeführt“.'}[e['entscheidung']]
        MEHR.append(e)
# Themen, die in älteren Daten zwei Klassen hatten, jetzt aber nicht mehr (ausdrücklich begründet)
NICHT_MEHR = [dict(thema=2, titel=L.TT[2], spur='rs_I und rs_II_III', klassen_vorher=[7, 8], klassen_jetzt=[7], punkte=[734, 749],
                   entscheidung='nicht teilen', anzeige='wird in Kl. 8 in „29 Terme umformen – Teil 2 von 2“ wieder aufgegriffen',
                   begruendung='Der Kl.-8-Punkt verlangt Gleichungen mit Summenprodukten und binomischen Ausdrücken. Das braucht binomische Formeln aus 29 Teil 2; die eigene Etappe gleichungen_binomisch steht deshalb seit LK-D 2 in 29 Teil 2 (Hauptthema 29, 2 bleibt Nebenthema). 2 hat damit nur noch Hauptpunkte in Kl. 7 – kein zweiter Teil, kein zusätzlicher Flug.')]
WIEDER = [dict(thema=e['thema'], spur=e['spur'], klasse=e['klasse'], anzeige=e['anzeige']) for e in MEHR if e['entscheidung'] == 'wiederholung'] + \
         [dict(thema=2, spur=sp, klasse=8, anzeige=NICHT_MEHR[0]['anzeige']) for sp in ('rs_I', 'rs_II_III')]
# Aufbau-Kette für alle Knoten (Anzeige)
KETTE = []
for t in sorted(L.TT):
    if t in L.STILL: continue
    for n in knoten(t):
        if not EIN[n] and not AUS[n] and n[1] is None: continue
        KETTE.append(dict(knoten=name(n), klassen=kl_txt(n),
                          baut_auf='; '.join(kurz(d) + (' (hart)' if a == 'hart' else '') for d, a, h in EIN[n]) or '–',
                          geht_weiter_in='; '.join(kurz(s) for s, a, h in AUS[n]) or '–'))
json.dump(dict(auftrag='LK-D 4 mit Ergänzung 942/943 (A1, B1)', stand='2026-11-22', regel='Teilungsregel 15:30/15:35/15:40: feinste gemeinsame Teilung über Gymnasium und RS Gruppe I; IB und RS II/III lösen keine Teilung aus.',
               hinweis='Kinder nur als Nummern. Klasse je Teil: erste Klasse, in der ein Lehrplanpunkt eine Etappe des Teils als Hauptthema verlangt; *_ohne_eigenen_punkt = Klasse aus der Reihenfolge abgeleitet.',
               teilungsliste=LISTE, zusatz_regel='Teil ohne Lehrplanpunkt in der Schulart = Zusatz: keine Pflicht, sperrt nichts; Voraussetzungen auf ihn nur empfohlen (Entscheidung 22.11., 16:20).', kanten_je_schulart=KANTEN_SCHULART, grenzfaelle=GRENZ, kuer_regel='Etappe ohne Lehrplanpunkt in der Schulart = Kür: zählt dort nicht für Flug-Abschluss, Flug-Test, Stempel (Entscheidung 22.11., 17:05).', etappen_kuer=ETAPPEN_KUER, stand_je_kind_ungeteilt=STAND_ALLE, vertiefung_aber_lehrplanpunkt=VERT_PFLICHT, mehrere_klassen=MEHR, nicht_mehr_mehrere_klassen=NICHT_MEHR, wiederholung_anzeige=WIEDER, kanten=KANTEN_OUT,
               verstoesse=VERSTOSS, aufbau_kette=KETTE), open('/tmp/lp/inhalte/pruefung/lehrplan/lk_teilung_2211.json', 'w'), ensure_ascii=False, indent=1)
print('Grenzfälle', [(g['thema'], g['teil'], g['spur'], g['klassen']) for g in GRENZ])
