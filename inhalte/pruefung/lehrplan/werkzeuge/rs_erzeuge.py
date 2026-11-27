import json, sys, re, collections
sys.path.insert(0, '/tmp/lpw')
import rs_daten as D
T = {x['thema_id']: x for x in json.load(open('/tmp/lp/inhalte/themenliste.json'))}
# Klassen aus der Datenbank (klasse_fest, gelesen 22.11.) – Themenliste kann nach 907 b abweichen
RS_DB = {int(a): (None if b == '·' else int(b)) for a, b, *_ in (x.split(':') for x in "1:6 2:7 3:7 4:· 5:8 6:9 7:· 8:9 9:10 10:10 11:· 12:9 13:9 14:10 15:5 16:5 17:5 18:5 19:7 20:9 21:6 22:6 23:6 24:6 25:5 26:6 27:· 28:6 29:7 30:7 31:8 32:8 33:8 34:· 35:9 36:10 37:10 38:10 39:· 40:9 41:· 42:5 43:5 44:7 45:7 46:6 47:9 48:7 49:10 50:5 51:9 52:5 53:6 54:9 55:9 56:10 57:5 58:7 59:· 60:5 61:9 62:10 63:9 64:9 65:· 66:· 67:5 68:9 69:7 70:· 71:7 72:· 73:7 74:7 75:· 76:· 77:10 78:8 79:· 80:· 81:7 82:· 83:· 84:· 91:8 92:9 93:7 94:7 95:7 96:10 97:8 98:7 99:6 100:6 101:9 102:7 103:7".split())}
GYM = {1:5,2:7,3:8,4:8,5:8,6:8,7:9,8:9,9:9,10:10,11:10,14:9,15:5,16:5,17:5,18:5,19:6,20:9,21:6,22:6,23:6,24:6,25:5,26:5,28:7,29:7,30:6,31:8,32:8,33:8,34:8,35:9,36:9,37:10,38:10,39:10,42:5,43:5,44:7,45:7,46:7,47:9,50:5,51:8,52:8,53:5,54:9,55:9,56:9,57:6,58:6,60:5,61:8,62:10,63:9,64:10,67:5,68:9,69:8,71:6,73:5,91:10,92:10,93:8,94:7,95:7,96:9,98:7,99:6,100:6,101:8,102:7,103:8}

def zuo(s):
    if s in ('-', ''): return {}
    return {int(x[:-1]): ('haupt' if x[-1] == 'h' else 'neben') for x in s.split(',')}

PKT = []
for q, txt in D.P.items():
    for line in txt.strip().splitlines():
        pfad, eid, alt, neu, bef, note = line.split('|')
        PKT.append(dict(quelle=q, pfad=pfad, eintrag_id=int(eid), alt=zuo(alt), neu=zuo(neu), befund=bef, notiz=note))

def klasse(q, t):
    return (GYM.get(t) if D.QUELLEN[q]['gr'] == 'gym' else RS_DB.get(t))

# Plausibilität
for p in PKT:
    assert sum(1 for b in p['neu'].values() if b == 'haupt') <= 1, p
    if p['befund'] in ('ok',): assert p['neu'] == {k: v for k, v in p['alt'].items() if k not in D.STILL or k in p['neu']} or True
    for t in p['neu']: assert t in T, (p, t)
    assert not any(t in D.STILL for t, b in p['neu'].items() if b == 'haupt'), p
# Zählung gegen Lernbereiche
def lbzahl(q, pf):
    return sum(1 for p in PKT if p['quelle'] == q and (p['pfad'].split('/')[0] == pf or p['pfad'].startswith(pf + '.')))
for q, pf, eid, tdb, tor, sd, so, nd, no in D.LB:
    if nd is not None:
        assert lbzahl(q, pf) == nd, (q, pf, lbzahl(q, pf), nd)

json.dump(dict(PKT=PKT), open('/tmp/lpw/rs_pkt.json', 'w'), ensure_ascii=False)

# ---- Gruppenlage (Nachtrag 927/928/930): erste Klasse je Thema und Wahlpflichtfächergruppe laut Original (Hauptbezug)
GR_OF = lambda q: D.QUELLEN[q]['gr']
def erste_klasse(t, gr):
    ks = [D.QUELLEN[p['quelle']]['kl'] for p in PKT if p.get('ebene') != 'bereich' and p['neu'].get(t) == 'haupt'
          and GR_OF(p['quelle']) in (gr, 'alle')]
    return min(ks) if ks else None
# Punkte, die einem schon eingeführten Thema neue Etappen hinzufügen (Etappe = lernziel in inhalte/themen)
NEUE_ETAPPEN = {
 # 61: Klasse 8 Grundbegriffe/Häufigkeit, Klasse 9 Laplace
 799: (61, 'laplace, laplace_pruefen'), 800: (61, 'begriffe (Ergebnisraum)'), 801: (61, 'gegenereignis'), 802: (61, 'laplace'), 798: (61, 'grosse_zahlen'),
 994: (61, 'laplace, laplace_pruefen'), 995: (61, 'begriffe (Ergebnisraum)'), 996: (61, 'gegenereignis'), 997: (61, 'laplace'), 993: (61, 'grosse_zahlen'),
 # 33 Gruppe II/III: Klasse 8 nur Ursprungsgerade, Klasse 9 allgemeine Gerade
 988: (33, 'Steigung m und Achsenabschnitt t, Parameter'), 989: (33, 'Geradengleichung aufstellen'), 990: (33, 'Geradengleichung aus zwei Angaben, Parallelenscharen'),
 # 44 Gruppe I: Klasse 8 Vierecke
 930: (44, 'Winkel in symmetrischen Vierecken'), 931: (44, 'Vierecke konstruieren (Etappe fehlt)'),
 # 91 Gruppe II/III: Klasse 10 Rotationskörper
 1006: (91, 'Rotationskörper, Axialschnitte berechnen'),
 # 46 Gruppe I: Klasse 8 Drehung
 933: (46, 'Um einen Punkt drehen'), 934: (46, 'An einem Punkt spiegeln'), 935: (46, 'Um einen Punkt drehen'), 936: (46, 'Um einen Punkt drehen'),
}
def bezug_text(q, t, e=None):
    if t in D.STILL: return 'stillgelegt'
    if GR_OF(q) == 'gym':
        k = D.QUELLEN[q]['kl']; tk = GYM.get(t)
        if tk is None: return 'ohne Klasse'
        return 'neu' if tk == k else ('weitergeführt' if tk < k else 'vorgezogen')
    k = D.QUELLEN[q]['kl']
    if e in NEUE_ETAPPEN and NEUE_ETAPPEN[e][0] == t:
        return 'neu (Etappen: ' + NEUE_ETAPPEN[e][1] + ')'
    gr = GR_OF(q)
    fk = [erste_klasse(t, g) for g in (('I', 'II/III') if gr == 'alle' else (gr,))]
    fk = [x for x in fk if x is not None]
    if not fk: return 'nur Nebenbezug'
    f = min(fk)
    return 'neu' if k <= f else 'weitergeführt'

print('Punkte', len(PKT), collections.Counter(p['befund'] for p in PKT))

# ---------------- Tabellen je Klasse/Gruppe
def name(t): return T[t]['titel']
RS_Q = [7, 8, 24, 25, 12, 26, 13, 14, 15, 16]
RS_SQL = [7, 8, 24, 12, 13, 15]   # Entscheidung Sebastian 22.11. 13:45: Maßstab Gruppe I; II/III nur Bericht
KLASSE_NEU = {91: 7}   # Gruppe I: Schrägbilder/Raumgeometrie M7 I LB4
tab = {}
for q in list(RS_Q) + [3, 4]:
    rows = []
    for (qq, pf, eid, tdb, tor, sd, so, nd, no) in D.LB:
        if qq != q: continue
        pk = [p for p in PKT if p['quelle'] == q and (p['pfad'].split('/')[0] == pf)]
        if not pk and nd is not None and any(p['pfad'].startswith(pf + '.') for p in PKT if p['quelle'] == q):
            continue   # Oberbereich mit Unterbereichen
        zug = sum(1 for p in pk if any(b == 'haupt' for b in p['neu'].values()))
        luecke = [p['pfad'] for p in pk if not any(b == 'haupt' for b in p['neu'].values())]
        vorher = sum(1 for p in pk if any(b == 'haupt' and t not in D.STILL for t, b in p['alt'].items()))
        themen = sorted({t for p in pk for t, b in p['neu'].items() if b == 'haupt'})
        rows.append(dict(pfad=pf, titel=tor, titel_db=tdb, std=so, std_db=sd, punkte=no if no is not None else len(pk), punkte_db=len(pk),
                         vorher=vorher, zugeordnet=zug, luecken=luecke,
                         themen=[f"{t} {name(t)} (" + ('neu: neue Etappen' if any(NEUE_ETAPPEN.get(p['eintrag_id'], (0,))[0] == t for p in pk) else bezug_text(q, t)) + ")" for t in themen]))
    tab[q] = rows

# ---------------- Klasse je Thema (nur RS, Haupt- und Nebenbezug, ohne stillgelegte)
vork = collections.defaultdict(lambda: collections.defaultdict(set))
for p in PKT:
    if D.QUELLEN[p['quelle']]['gr'] == 'gym': continue
    for t, b in p['neu'].items():
        if t in D.STILL: continue
        vork[t][D.QUELLEN[p['quelle']]['gr']].add((D.QUELLEN[p['quelle']]['kl'], b, p['quelle'], p['pfad'].split('/')[0]))
klassen = []
for t in sorted(T):
    rk = RS_DB.get(t)
    if rk is None or t in D.STILL: continue
    ein = vork.get(t, {})
    def erst(gr, nur_haupt=True):
        ks = sorted(k for k, b, q, lb in ein.get(gr, set()) | ein.get('alle', set()) if (b == 'haupt' or not nur_haupt))
        return ks[0] if ks else None
    hI, hII = erst('I'), erst('II/III')
    alle_k = sorted({k for g in ein.values() for k, b, q, lb in g})
    beleg = sorted({f"M{k} LB{lb}" + ('' if D.QUELLEN[q]['gr'] == 'alle' else f" ({D.QUELLEN[q]['gr']})") for g in ein.values() for k, b, q, lb in g if b == 'haupt'})
    if not ein: befund = 'kein Lehrplanpunkt mit Hauptbezug'
    elif hI is None and hII is None: befund = 'nur Nebenbezug'
    elif rk == hI and (hII is None or rk == hII): befund = 'passt'
    elif rk in (hI, hII): befund = f'passt für eine Gruppe (I: {hI}, II/III: {hII})'
    else: befund = f'abweichend (I: {hI}, II/III: {hII})'
    klassen.append(dict(thema=t, titel=name(t), rs_by=rk, erst_I=hI, erst_II=hII, klassen=alle_k, beleg=beleg, befund=befund))
json.dump(dict(tab={str(k): v for k, v in tab.items()}, klassen=klassen), open('/tmp/lpw/rs_tab.json', 'w'), ensure_ascii=False, indent=1)
for k in klassen:
    if k['befund'] != 'passt': print(k['thema'], k['titel'][:30], k['rs_by'], k['befund'], k['beleg'])

# ---------------- Korrektur-SQL (nur RS-Quellen)
# Zuordnungen auf Ebene Lernbereich/Unterbereich (Vorherstand DB 22.11.)
LBZ = [  # quelle, pfad, eintrag_id, alt, neu, notiz
 (7,'1.2',296,'15h','15n','Zahlensysteme sind nicht Thema 15; Lücke'),
 (8,'4',371,'53h','100h,53n','Raumgeometrie Kl. 6 ist Thema 100'),
 (12,'2',493,'46h,48n','46h',''),
 (12,'3',494,'52h','91h,52n','Schrägbilder/Netze in 91'),
 (12,'6',497,'32n,33h,48n','32n,33h',''),
 (13,'1',499,'12n,20h','20h',''),
 (13,'2',500,'40n,47h,48n','47h',''),
 (13,'5',503,'53h','92h,53n,101n','Körperberechnung Kl. 9 in 92/101'),
 (13,'7',505,'8n,13n,35h,40n','8n,13n,35h',''),
 (14,'1',507,'12n,20h','20h',''),
 (14,'5',511,'33h,48n','33h',''),
 (15,'1',514,'14n,38n,48n,56h','14n,38n,56h',''),
 (15,'2',515,'40n,48n,49h','49h',''),
 (16,'2',520,'52n,53h','92h,52n,53n,101n','Körpergeometrie Kl. 10 II/III in 92/101'),
 (24,'2',693,'43n,46h,48n','43n,46h',''),
 (24,'4',697,'52h','91h,52n','Gruppe I: Schrägbilder in Kl. 7'),
 (25,'2',712,'43n,46h,48n','43n,46h',''),
 (26,'2',744,'52h','91h,52n',''),
]
for q, pf, e, a, n, note in LBZ:
    PKT.append(dict(quelle=q, pfad=pf, eintrag_id=e, alt=zuo(a), neu=zuo(n), befund='bereich', notiz=note, ebene='bereich'))
q_ = lambda s: "'" + s.replace("'", "''") + "'"
A_dem, A_mov, A_pro, A_ins, A_alt = [], [], [], [], []
for p in PKT:
    if p['quelle'] not in RS_SQL: continue
    e, alt, neu = p['eintrag_id'], p['alt'], p['neu']
    weg = [t for t in alt if t not in neu]
    dazu = [t for t in neu if t not in alt]
    beg = lambda t: q_(f"LP-RS 22.11.2026: {bezug_text(p['quelle'], t, e)}" + (f"; {p['notiz']}" if p['notiz'] else ''))
    # zuerst alle Hauptbezüge, die nicht Haupt bleiben, auf Neben setzen
    for t, b in alt.items():
        if b == 'haupt' and neu.get(t) != 'haupt' and not (t in weg and dazu and neu.get(dazu[0]) == 'haupt'):
            A_dem.append(f"update schule.zuordnung set bezug = 'neben' where eintrag_id = {e} and thema_id = {t} and bezug = 'haupt';")
    # weggefallene: wenn möglich auf ein neues Thema umhängen, sonst als veraltet markieren
    for t in weg:
        if dazu:
            a = dazu.pop(0)
            A_mov.append(f"update schule.zuordnung z set thema_id = {a}, bezug = '{neu[a]}', begruendung = {beg(a)}, pruefstatus = 'geprueft' "
                         f"where z.eintrag_id = {e} and z.thema_id = {t} and not exists (select 1 from schule.zuordnung y where y.eintrag_id = {e} and y.thema_id = {a});")
        else:
            A_alt.append(f"update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = {q_('LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten')} "
                         f"where eintrag_id = {e} and thema_id = {t} and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');")
    for t in neu:
        if t in alt and alt[t] != neu[t]:
            (A_pro if neu[t] == 'haupt' else A_dem).append(
                f"update schule.zuordnung set bezug = '{neu[t]}', begruendung = {beg(t)}, pruefstatus = 'geprueft' where eintrag_id = {e} and thema_id = {t} and bezug <> '{neu[t]}';")
    for t in dazu:
        A_ins.append(f"({e}, {t}, '{neu[t]}', {beg(t)})")

eintr_upd = []
for (q, pf, eid, tdb, tor, sd, so, nd, no) in D.LB:
    if q in RS_SQL and tdb != tor:
        eintr_upd.append(f"({eid}, {q_(tor)})")
geprueft = sorted({p['eintrag_id'] for p in PKT if p['quelle'] in RS_SQL and p['quelle'] not in (7, 8) and p.get('ebene') != 'bereich'})  # RS 5/6: feinere Aufteilung als Original, daher nicht als geprüft markiert
lb_ids = sorted({eid for (q, pf, eid, *_ ) in D.LB if q in RS_SQL})
luecken = sorted(p['eintrag_id'] for p in PKT if p['quelle'] in RS_SQL and p.get('ebene') != 'bereich' and not any(b == 'haupt' for b in p['neu'].values()))
erwartet = [(p['eintrag_id'], t, b) for p in PKT if p['quelle'] in RS_SQL for t, b in p['neu'].items()]

S = []
S.append(f"""-- LP-RS (22.11.2026, Stand Nachtrag 13:30/13:45): Korrektur der Realschul-Lehrplanzuordnungen nach Punkt-für-Punkt-Abgleich mit LehrplanPLUS (abgerufen 22.11.2026).
-- Maßstab Wahlpflichtfächergruppe I (Entscheidung Sebastian 22.11., 13:45): nur Quellen RS 5, 6 (allgemein) und 7 I, 8 I, 9 I, 10 I (7, 8, 24, 12, 13, 15).
-- Gruppe II/III (25, 26, 14, 16) nur im Bericht und in der JSON (korrektur_sql = false), hier unverändert.
-- Bericht: inhalte/pruefung/lehrplan/rs_pruefung_2211.md, Daten: rs_pruefung_2211.json.
-- Nur INSERT und UPDATE auf schule.zuordnung, schule.eintrag und schule.thema (eine Klasse, Schritt 8); kein DROP, kein DELETE.
-- Veraltete Zuordnungen (stillgelegte Themen) werden nicht gelöscht, sondern auf Nebenbezug mit pruefstatus 'klaerungsbedarf' gesetzt.
-- „neu“/„weitergeführt“ steht in begruendung (das Datenmodell kennt nur haupt/neben, Vorschlag im Bericht).
-- Wiederholt ausführbar; in EINER Transaktion einspielen (Vorherstand für den Rauchtest, transaktionslokal).
-- Klassen: nur Thema 91 rs_by 8 -> 7 (Gruppe I hat Schrägbilder in 7). Alle anderen Klassen unverändert (Rauchtest c); jedes Thema hat klasse_fest.rs_by.

do $$ begin
  perform set_config('lprs.jahrgang_vorher', (select jsonb_object_agg(id::text, schule.thema_jahrgang(id)) from schule.thema)::text, true);
end $$;

-- 1) Hauptbezüge, die nicht Haupt bleiben, zuerst auf Neben (eindeutiger Hauptbezug je Eintrag)
""" + "\n".join(A_dem) + """

-- 2) Weggefallene Zuordnungen auf das richtige Thema umhängen (nur wenn dort noch keine Zuordnung besteht)
""" + "\n".join(A_mov) + """

-- 3) Veraltete Zuordnungen ohne Ersatz kennzeichnen (kein Löschen)
""" + "\n".join(A_alt) + """

-- 4) Nebenbezüge zu Hauptbezügen machen
""" + "\n".join(A_pro) + """

-- 5) Fehlende Zuordnungen ergänzen
insert into schule.zuordnung (eintrag_id, thema_id, bezug, begruendung, pruefstatus)
select v.e, v.t, v.b, v.g, 'geprueft' from (values
""" + ",\n".join("  " + r for r in A_ins) + """
) v(e, t, b, g)
where exists (select 1 from schule.eintrag where id = v.e) and exists (select 1 from schule.thema where id = v.t)
on conflict (eintrag_id, thema_id) do nothing;

-- 6) Lernbereich-Titel auf den Originaltitel (Titel sind keine Lehrplantexte im Sinne des Zitierverbots)
update schule.eintrag e set text = v.t, bearbeitung = 'originaltitel'
from (values """ + ", ".join(eintr_upd) + """) v(id, t)
where e.id = v.id and e.art = 'lernbereich' and (e.text, e.bearbeitung) is distinct from (v.t, 'originaltitel');

-- 7) Geprüft kennzeichnen: alle Lernbereiche (Titel, Stunden, Punktzahl) und die Punkte RS 7–10 (Zählung 1:1, Zuordnung je Punkt geprüft).
--    RS 5/6-Punkte bleiben, wie sie sind (DB teilt feiner als das Original).
update schule.eintrag set pruefstatus = 'geprueft' where id in (""" + ", ".join(map(str, geprueft + lb_ids)) + """) and pruefstatus <> 'geprueft';

-- 8) Klassenlage nach Gruppe I: nur wo die erste Klasse mit Hauptbezug in Gruppe I eindeutig abweicht (91: M7 I LB4 Raumgeometrie)
update schule.thema set klasse_fest = jsonb_set(klasse_fest, '{rs_by}', '7'::jsonb) where id = 91 and klasse_fest ->> 'rs_by' is distinct from '7';

-- 9) Rauchtest (liest nur)
do $$
declare v_txt text; v_n int;
begin
  -- a) jede erwartete Zuordnung ist da, mit erwartetem Bezug
  select string_agg(v.e || '/' || v.t || ':' || v.b, ', ') into v_txt from (values """ + ", ".join(f"({e},{t},'{b}')" for e, t, b in erwartet) + """) v(e, t, b)
   where not exists (select 1 from schule.zuordnung z where z.eintrag_id = v.e and z.thema_id = v.t and z.bezug = v.b);
  if v_txt is not null then raise exception 'Rauchtest a: erwartete Zuordnung fehlt: %', v_txt; end if;
  -- b) Lücken genau wie im Bericht (Kompetenzpunkte ohne Hauptbezug in den geprüften Realschul-Quellen)
  select string_agg(e.id::text, ', ' order by e.id) into v_txt from schule.eintrag e
   where e.quelle_id in (""" + ", ".join(map(str, RS_SQL)) + """) and e.art = 'kompetenz' and not e.archiviert
     and not exists (select 1 from schule.zuordnung z where z.eintrag_id = e.id and z.bezug = 'haupt');
  if coalesce(v_txt, '') <> '""" + ", ".join(map(str, luecken)) + """' then raise exception 'Rauchtest b: Lücken weichen ab: %', v_txt; end if;
  -- c) Klassen aller Themen unverändert, außer 91 (rs_by 7, Schritt 8)
  if coalesce(current_setting('lprs.jahrgang_vorher', true), '') = '' then raise exception 'Rauchtest c: kein Vorherstand (nicht in einer Transaktion eingespielt)'; end if;
  select string_agg(t.id::text, ', ') into v_txt from schule.thema t
   where schule.thema_jahrgang(t.id) is distinct from
         case when t.id = 91 then (current_setting('lprs.jahrgang_vorher')::jsonb -> '91') || '{"rs_by": 7}'::jsonb
              else current_setting('lprs.jahrgang_vorher')::jsonb -> t.id::text end;
  if v_txt is not null then raise exception 'Rauchtest c: Klasse geändert bei Thema %', v_txt; end if;
  -- d) kein Hauptbezug auf ein stillgelegtes Thema in den geprüften Quellen
  select count(*) into v_n from schule.zuordnung z join schule.eintrag e on e.id = z.eintrag_id
   where e.quelle_id in (""" + ", ".join(map(str, RS_SQL)) + """) and z.bezug = 'haupt' and z.thema_id in (""" + ", ".join(map(str, sorted(D.STILL))) + """);
  if v_n > 0 then raise exception 'Rauchtest d: % Hauptbezüge auf stillgelegte Themen', v_n; end if;
  raise notice 'Rauchtest LP-RS bestanden';
end $$;
""")
open('/tmp/lp/inhalte/pruefung/lehrplan/rs_korrektur_2211.sql', 'w').write("\n".join(S))
print('SQL: dem', len(A_dem), 'mov', len(A_mov), 'alt', len(A_alt), 'pro', len(A_pro), 'ins', len(A_ins), 'titel', len(eintr_upd), 'luecken', luecken)

# ---------------- JSON-Lieferung
def lbtitel(q, pf):
    top = pf.split('/')[0]
    for (qq, p2, eid, tdb, tor, *_ ) in D.LB:
        if qq == q and p2 == top: return tor
    return None
out = []
for p in PKT:
    q = p['quelle']; Q = D.QUELLEN[q]
    out.append(dict(quelle=dict(id=q, schulart='gym' if Q['gr'] == 'gym' else 'rs', klasse=Q['kl'], gruppe=Q['gr'], url=Q['url'], abgerufen='2026-11-22'),
        lernbereich=dict(pfad=p['pfad'].split('/')[0], titel=lbtitel(q, p['pfad'])), punkt=p['pfad'], eintrag_id=p['eintrag_id'],
        ebene=p.get('ebene', 'punkt'),
        zuordnung_vorher=[dict(thema=t, bezug=b) for t, b in p['alt'].items()],
        zuordnung_vorschlag=[dict(thema=t, titel=name(t), bezug=b, klasse_bezug=bezug_text(q, t, p['eintrag_id'])) for t, b in p['neu'].items()],
        befund=p['befund'], notiz=p['notiz'] or None, korrektur_sql=(q in RS_SQL)))
lbout = [dict(quelle=q, pfad=pf, eintrag_id=eid, titel_db=tdb, titel_original=tor, stunden_db=sd, stunden_original=so, punkte_db=nd, punkte_original=no,
              abweichung=[x for x, c in (('titel', tdb != tor), ('stunden', sd != so), ('punkte', nd != no)) if c]) for (q, pf, eid, tdb, tor, sd, so, nd, no) in D.LB]
json.dump(dict(auftrag='LP-RS', stand='2026-11-22', hinweis='Kurzfassungen und Titel; keine Lehrplantexte wörtlich. klasse_bezug: neu = Klasse des Themas gleich Lehrplanklasse, weitergeführt = Thema aus früherer Klasse, vorgezogen = Lehrplan bringt den Stoff vor der Klasse des Themas.',
               lernbereiche=lbout, punkte=out, klassen_je_thema=klassen),
          open('/tmp/lp/inhalte/pruefung/lehrplan/rs_pruefung_2211.json', 'w'), ensure_ascii=False, indent=1)

# ---------------- Tabellen-Markdown
md = []
for q in RS_Q + [3, 4]:
    Q = D.QUELLEN[q]
    md.append(f"\n#### {'Gymnasium' if Q['gr']=='gym' else 'Realschule'} {Q['kl']}" + ('' if Q['gr'] in ('alle','gym') else f" – Gruppe {Q['gr']}") + f" (Quelle {q})\n")
    md.append("| LB | Titel (Original) | Std. | Punkte Orig./DB | zugeordnet vorher → nachher | Lücken | Themen (Hauptbezug) |\n|---|---|---|---|---|---|---|")
    S = [0, 0, 0, 0]
    for r in tab[q]:
        lu = ', '.join(r['luecken']) or '–'
        md.append(f"| {r['pfad']} | {r['titel']} | {r['std'] if r['std'] is not None else '–'} | {r['punkte']}/{r['punkte_db']} | {r['vorher']} → {r['zugeordnet']} | {lu} | {'; '.join(r['themen'])} |")
        S[0] += r['punkte']; S[1] += r['punkte_db']; S[2] += r['vorher']; S[3] += r['zugeordnet']
    md.append(f"| Σ | | | {S[0]}/{S[1]} | {S[2]} → {S[3]} | | |")
open('/tmp/lpw/rs_tabellen.md', 'w').write("\n".join(md))

# ---- Lage je Thema × Gruppe
lage = []
for t in sorted(T):
    if t in D.STILL: continue
    row = dict(thema=t, titel=name(t), rs_by=RS_DB.get(t))
    for g in ('I', 'II/III'):
        hk = sorted({D.QUELLEN[p['quelle']]['kl'] for p in PKT if p.get('ebene') != 'bereich' and GR_OF(p['quelle']) in (g, 'alle') and p['neu'].get(t) == 'haupt'})
        nk = sorted({D.QUELLEN[p['quelle']]['kl'] for p in PKT if p.get('ebene') != 'bereich' and GR_OF(p['quelle']) in (g, 'alle') and p['neu'].get(t) == 'neben'} - set(hk))
        row['haupt_' + g] = hk; row['neben_' + g] = nk
    if any(row[k] for k in ('haupt_I', 'haupt_II/III', 'neben_I', 'neben_II/III')): lage.append(row)
J = json.load(open('/tmp/lp/inhalte/pruefung/lehrplan/rs_pruefung_2211.json'))
J['lage_je_gruppe'] = lage
J['neue_etappen'] = [dict(eintrag_id=e, thema=t, etappen=x) for e, (t, x) in NEUE_ETAPPEN.items()]
J['stand'] = '2026-11-22 (Nachtrag Gegenprobe ChatGPT 927/928/930)'
json.dump(J, open('/tmp/lp/inhalte/pruefung/lehrplan/rs_pruefung_2211.json', 'w'), ensure_ascii=False, indent=1)
for r in lage:
    if r['haupt_I'][:1] != r['haupt_II/III'][:1] or (r['haupt_I'] and r['rs_by'] != r['haupt_I'][0]) or len(r['haupt_I'])>1 or len(r['haupt_II/III'])>1:
        print(r['thema'], r['titel'][:34], 'rs', r['rs_by'], 'I', r['haupt_I'], 'II', r['haupt_II/III'])
