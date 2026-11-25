import json,sys,collections
sys.path.insert(0,'/tmp/lpw'); from db import VOR; import vorschlag as V
T={x['thema_id']:x for x in json.load(open('/tmp/lp/inhalte/themenliste.json'))}
AUF=V.AUF_SET; LOE={(t,b) for t,b,_ in V.LOESCHEN}
kl=lambda i:{k:v for k,v in T[i]['klasse'].items() if v}
rf=lambda i,s:T[i]['reihenfolge'].get(s)
E=[(a,b,art) for a,b,art in VOR if (a,b) not in LOE]+[(a,b,art) for a,b,art,_ in V.NEU]
assert len(set((a,b) for a,b,_ in E))==len(E)
assert all((t,b) in {(a,b_) for a,b_,_ in VOR} for t,b in LOE),'Löschzeile nicht vorhanden'
print('i  Verbindung mit aufgelöstem Thema:',[(a,b) for a,b,_ in E if a in AUF or b in AUF])
print('b  ohne Verbindung/eigenständig (freigegeben):',[i for i in T if kl(i) and i not in AUF and i not in {a for a,_,_ in E} and 'eigenstaendig' not in T[i]])
print('g  spätere Klasse:',[(a,b,s) for a,b,_ in E for s,k in kl(a).items() if kl(b).get(s,0)>k])
print('h  100–103:',all(any(a==i for a,_,_ in E) for i in (100,101,102,103)))
print('a  12 gym:', 'gym_by' in kl(12))
print('   hart, gleiche Klasse später:',[(a,b,s) for a,b,art in E if art=='hart' for s,k in kl(a).items() if kl(b).get(s)==k and rf(b,s)>rf(a,s)])
for s in ('gym_by','rs_by','ib_myp'):
  for k in sorted({kl(i)[s] for i in T if s in kl(i)}):
    ids=[i for i in T if kl(i).get(s)==k]
    if sorted(rf(i,s) or 0 for i in ids)!=list(range(1,len(ids)+1)): print('LÜCKE',s,k)
g=collections.defaultdict(list)
for a,b,_ in E: g[a].append(b)
st={}
def d(u):
  st[u]=1
  for v in g[u]:
    if st.get(v)==1: print('ZYKLUS',u,v)
    elif not st.get(v): d(v)
  st[u]=2
for u in list(g):
  if not st.get(u): d(u)
print('Verbindungen nachher',len(E),'(vorher 70, gelöscht',len(LOE),', neu',len(V.NEU),')')
print('Aufgelöste mit Klasse:',{i:kl(i) for i in sorted(AUF)})
