import json,sys
sys.path.insert(0,'/tmp/lpw'); from db import VOR; import vorschlag as V
D=json.load(open('/tmp/lpw/reise.json'))
B={b[0]:dict(k=b[1],titel=b[2],zk=b[3],rf=b[4]) for b in D['b']}
KL=dict((a,b) for a,b in D['l'])
BT={}
for b,t in D['bt']: BT.setdefault(t,set()).add(b)
def visum(E):
  s=set()
  for a,b,art in E:
    if art!='hart': continue
    for x in BT.get(a,()):
      for y in BT.get(b,()):
        if x!=y: s.add((x,y))
  return s
def reise(lid,vis):
  st={r[1]:r for r in D['r'] if r[0]==lid}
  ok={b for b,r in st.items() if r[2]=='fertig' or r[3]}
  nae={}
  for b,r in sorted(st.items(),key=lambda x:(B[x[0]]['k'],B[x[0]]['rf'])):
    if r[2]!='fertig' and not r[3] and r[4]!='zusatz' and B[b]['k'] not in nae: nae[B[b]['k']]=b
  bew=[]
  for k,b in nae.items():
    fehlt=sorted(y for x,y in vis if x==b and y not in ok)
    rue=B[b]['zk'] is not None and B[b]['zk']<KL[lid]
    bew.append((b,fehlt,rue,st[b][2]))
  pfl=any(r and not f for b,f,r,_ in bew)
  opt=[(b,f) for b,f,r,_ in bew if (not pfl) or r]
  return ('pflicht' if pfl else 'frei'), sorted(opt)
E0=[tuple(x) for x in VOR]
LOE={(t,b) for t,b,_ in V.LOESCHEN}
E1=[e for e in E0 if (e[0],e[1]) not in LOE]+[(a,b,art) for a,b,art,_ in V.NEU]
v0,v1=visum(E0),visum(E1)
print('Visum vorher',len(v0),'nachher',len(v1))
def alle(lid,vis):
  st={r[1]:r for r in D['r'] if r[0]==lid}
  ok={b for b,r in st.items() if r[2]=='fertig' or r[3]}
  return {b:tuple(sorted(y for x,y in vis if x==b and y not in ok)) for b in st if b not in ok}
def neue_visa_kanten(E_basis):
  vb=visum(E_basis); out=[]
  for a,b,art,g in V.NEU:
    if art!='hart': continue
    if any((x,y) not in v0 for x in BT.get(a,()) for y in BT.get(b,()) if x!=y): out.append((a,b))
  return out
