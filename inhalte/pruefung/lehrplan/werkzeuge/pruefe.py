import json,sys
sys.path.insert(0,'/tmp/lpw'); from db import VOR; import vorschlag as V
L=json.load(open('/tmp/lp/inhalte/themenliste.json')); T={x['thema_id']:x for x in L}
# Zustand nach Änderung
kl={i:dict((s,v) for s,v in (T[i]['klasse'] or {}).items() if v is not None) for i in T}
rf={i:dict(T[i].get('reihenfolge') or {}) for i in T}
for i,d in V.KLASSE.items():
  for s,(k,r,_,_) in d.items(): kl[i][s]=k
for k,ids in V.REIHENFOLGE_GYM.items():
  for n,i in enumerate(ids,1): rf[i]['gym_by']=n
alle=[(a,b,art,'') for a,b,art in VOR]+[(a,b,art,g) for a,b,art,g in V.NEU]
paare=set((a,b) for a,b,_ ,_ in alle)
assert len(paare)==len(alle), 'Doppelte Verbindung'
for a,b,_,_ in V.NEU: assert a in T and b in T and a!=b,(a,b)
problem=[]
for a,b,art,g in alle:
  if art!='hart': continue
  for s in ('gym_by','rs_by','ib_myp'):
    if s in kl[a]:
      if s not in kl[b]: problem.append(('fehlt',s,a,b,T[a]['titel'],T[b]['titel'],'neu' if g else 'alt'))
      elif kl[b][s]>kl[a][s] or (kl[b][s]==kl[a][s] and rf[b].get(s,99)>=rf[a].get(s,99)): problem.append(('später',s,a,b,f"{T[a]['titel']} {kl[a][s]}/{rf[a].get(s)}",f"{T[b]['titel']} {kl[b][s]}/{rf[b].get(s)}",'neu' if g else 'alt'))
ohne=[i for i in T if i not in {a for a,*_ in alle} and i not in V.EIGEN]
print('Verbindungen gesamt',len(alle),'neu',len(V.NEU))
print('Themen ohne Voraussetzung und ohne „eigenständig“:',[(i,T[i]['titel']) for i in ohne])
print('Harte Voraussetzung nicht vorher verfügbar:',len(problem)); [print('  ',p) for p in problem]
# Zyklen
import collections
g=collections.defaultdict(list)
for a,b,_,_ in alle: g[a].append(b)
farbe={}
def dfs(u,weg):
  farbe[u]=1
  for v in g[u]:
    if farbe.get(v)==1: print('ZYKLUS',weg+[v]); 
    elif not farbe.get(v): dfs(v,weg+[v])
  farbe[u]=2
for u in list(g): 
  if not farbe.get(u): dfs(u,[u])
# Reihenfolge lückenlos
for s in ('gym_by','rs_by','ib_myp'):
  for k in sorted(set(v[s] for v in kl.values() if s in v)):
    ids=[i for i in T if kl[i].get(s)==k]; r=sorted(rf[i].get(s) for i in ids if rf[i].get(s) is not None)
    if r!=list(range(1,len(ids)+1)): print('LÜCKE',s,k,r,[i for i in ids if rf[i].get(s) is None])
print('Reihenfolge-Prüfung fertig')
