import json,sys,re
from fractions import Fraction as F
SUP=str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻ᵏⁿᵉᵐ','0123456789-knem')
SUPCH='⁰¹²³⁴⁵⁶⁷⁸⁹⁻ᵏⁿᵉᵐ'
def topy(s,var):
  s=s.replace('·','*').replace(':','/').replace('−','-').replace('–','-').replace(',','.')
  out='';i=0
  while i<len(s):
    c=s[i]
    if c in SUPCH:
      j=i
      while j<len(s) and s[j] in SUPCH: j+=1
      e=s[i:j].translate(SUP)
      out+='**('+e+')'; i=j
    else: out+=c; i+=1
  # implicit multiplication like 2x or )(
  out=re.sub(r'(\d)\s*([a-z(])',r'\1*\2',out)
  out=re.sub(r'\)\s*\(',')*(',out)
  return out
def ev(expr,env):
  return eval(expr,{'__builtins__':{}},env)
res={'ok':0,'fehl':[],'nicht':[]}
for fn in sys.argv[1:]:
  d=json.load(open(fn))
  for i,a in enumerate(d['aufgaben']):
    t=a['f']['text'] if isinstance(a['f'],dict) else a['f']
    o=a.get('o',{}); key=f"{fn.split('/')[-1]}#{i}"
    m=re.match(r'^([^=]+?)\s*=\s*([0-9a-z(),./]+)([ᵏⁿᵉᵐ])\.?\s*Wie groß ist ([knem])\?$',t)
    m2=re.match(r'^Berechne(?: geschickt)?:?\s*([^.]*?)(?: und gib| mit dem| \.|\. Gib|$)',t)
    try:
      if m and 'wert' in o:
        lhs,base,_,v=m.groups(); base=base.strip('()')
        good=True
        for vals in ({'a':F(2),'b':F(3),'x':F(5),'y':F(7),'z':F(11)},{'a':F(3),'b':F(2),'x':F(7),'y':F(5),'z':F(13)}):
          L=ev(topy(lhs,0),dict(vals)); B=ev(topy(base,0),dict(vals)); k=F(o['wert']).limit_denominator(1000) if not isinstance(o['wert'],int) else o['wert']
          if L!=B**k: good=False
        (res['ok'].__class__)
        if good: res['ok']+=1
        else: res['fehl'].append((key,t,o))
      elif m2 and 'wert' in o and not re.search(r'[a-z]',m2.group(1)):
        v=ev(topy(m2.group(1),0),{}); w=o['wert']; tol=o.get('toleranz',0) or 1e-9
        if abs(float(v)-float(w))<=max(tol,1e-9): res['ok']+=1
        else: res['fehl'].append((key,t,o,float(v)))
      else: res['nicht'].append(key)
    except Exception as e: res['nicht'].append(key+' ERR '+str(e)[:40])
print('ok',res['ok']); print('fehl',len(res['fehl'])); [print('  ',x) for x in res['fehl']]
print('nicht automatisch',len(res['nicht']))
json.dump(res['nicht'],open('/tmp/ppw/nicht.json','w'))
