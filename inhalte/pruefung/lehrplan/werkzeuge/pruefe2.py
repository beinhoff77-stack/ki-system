import json,sys,collections
sys.path.insert(0,'/tmp/lpw'); from db import VOR; import vorschlag as V
T={x['thema_id']:x for x in json.load(open('/tmp/lp/inhalte/themenliste.json'))}
kl=lambda i:{k:v for k,v in T[i]['klasse'].items() if v}
rf=lambda i,s:T[i]['reihenfolge'].get(s)
E=[(a,b,art) for a,b,art in VOR]+[(a,b,art) for a,b,art,_ in V.NEU]
assert len(set((a,b) for a,b,_ in E))==len(E)
ohne=[i for i in T if kl(i) and i not in {a for a,_,_ in E} and 'eigenstaendig' not in T[i]]
print('R1 ohne Verbindung/eigenständig:',ohne)
print('R2 spätere Klasse:',[(a,b,s) for a,b,_ in E for s,k in kl(a).items() if kl(b).get(s,0)>k])
print('R3 100–103:',{i:any(a==i for a,_,_ in E) for i in (100,101,102,103)})
print('hart, gleiche Klasse, später gereiht:',[(a,b,s) for a,b,art in E if art=='hart' for s,k in kl(a).items() if kl(b).get(s)==k and rf(b,s)>rf(a,s)])
print('hart, Voraussetzung ohne Klasse in Schulart:',[(a,b,s) for a,b,art in E if art=='hart' for s in kl(a) if s not in kl(b)])
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
print('Verbindungen',len(E),'neu',len(V.NEU),'fertig')
