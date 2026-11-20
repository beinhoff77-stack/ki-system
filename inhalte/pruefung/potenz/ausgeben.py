import json,sys
d=json.load(open(sys.argv[1]))
A=d['aufgaben']; flt=sys.argv[2] if len(sys.argv)>2 else None
for i,a in enumerate(A):
  if flt and a.get('l')!=flt: continue
  f=a.get('f',{}); t=f.get('text') if isinstance(f,dict) else f
  print(f"#{i} [{a.get('l')}|{a.get('p')}|S{a.get('s')}|{a.get('g')}|{a.get('y')}] {t}")
  if isinstance(f,dict) and (f.get('grafik') or f.get('schablone')): print('   F+', json.dumps({k:v for k,v in f.items() if k!='text'},ensure_ascii=False)[:300])
  if a.get('a'): print('   A:', ' | '.join(map(str,a['a'])))
  print('   O:', json.dumps(a.get('o'),ensure_ascii=False), ' C:', a.get('c'))
  print('   W:', a.get('w')); 
  if a.get('h'): print('   H:', a.get('h'))
