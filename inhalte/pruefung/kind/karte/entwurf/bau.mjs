import {readFileSync,writeFileSync} from 'fs';
import * as topo from 'topojson-client';
import * as d3 from 'd3-geo';
const t50=JSON.parse(readFileSync('node_modules/world-atlas/countries-50m.json'));
const t110=JSON.parse(readFileSync('node_modules/world-atlas/countries-110m.json'));
const L50=topo.feature(t50,t50.objects.countries).features;
const L110=topo.feature(t110,t110.objects.countries).features;
// Europa: englischer Name -> [deutsch, Hauptstadt, lat, lon]
const EU={'Iceland':['Island','Reykjavík',64.15,-21.94],'Ireland':['Irland','Dublin',53.35,-6.26],'United Kingdom':['Vereinigtes Königreich','London',51.51,-0.13],'Portugal':['Portugal','Lissabon',38.72,-9.14],'Spain':['Spanien','Madrid',40.42,-3.70],'France':['Frankreich','Paris',48.86,2.35],'Belgium':['Belgien','Brüssel',50.85,4.35],'Netherlands':['Niederlande','Amsterdam',52.37,4.90],'Luxembourg':['Luxemburg','Luxemburg',49.61,6.13],'Germany':['Deutschland','Berlin',52.52,13.40],'Switzerland':['Schweiz','Bern',46.95,7.45],'Austria':['Österreich','Wien',48.21,16.37],'Italy':['Italien','Rom',41.90,12.50],'Slovenia':['Slowenien','Ljubljana',46.06,14.51],'Croatia':['Kroatien','Zagreb',45.81,15.98],'Bosnia and Herz.':['Bosnien und Herzegowina','Sarajevo',43.86,18.41],'Montenegro':['Montenegro','Podgorica',42.44,19.26],'Serbia':['Serbien','Belgrad',44.79,20.45],'Kosovo':['Kosovo','Pristina',42.66,21.17],'Albania':['Albanien','Tirana',41.33,19.82],'Macedonia':['Nordmazedonien','Skopje',41.99,21.43],'North Macedonia':['Nordmazedonien','Skopje',41.99,21.43],'Greece':['Griechenland','Athen',37.98,23.73],'Bulgaria':['Bulgarien','Sofia',42.70,23.32],'Romania':['Rumänien','Bukarest',44.43,26.10],'Moldova':['Moldau','Chișinău',47.01,28.86],'Hungary':['Ungarn','Budapest',47.50,19.04],'Slovakia':['Slowakei','Bratislava',48.15,17.11],'Czechia':['Tschechien','Prag',50.08,14.44],'Poland':['Polen','Warschau',52.23,21.01],'Denmark':['Dänemark','Kopenhagen',55.68,12.57],'Norway':['Norwegen','Oslo',59.91,10.75],'Sweden':['Schweden','Stockholm',59.33,18.07],'Finland':['Finnland','Helsinki',60.17,24.94],'Estonia':['Estland','Tallinn',59.44,24.75],'Latvia':['Lettland','Riga',56.95,24.11],'Lithuania':['Litauen','Vilnius',54.69,25.28],'Belarus':['Belarus','Minsk',53.90,27.56],'Ukraine':['Ukraine','Kiew',50.45,30.52],'Malta':['Malta','Valletta',35.90,14.51],'Cyprus':['Zypern','Nikosia',35.17,33.36],'Andorra':['Andorra','Andorra la Vella',42.51,1.52],'Liechtenstein':['Liechtenstein','Vaduz',47.14,9.52],'Monaco':['Monaco','Monaco',43.74,7.42],'San Marino':['San Marino','San Marino',43.94,12.45]};
// Flüge Europa aus aufbau-vorschlag (Reihenfolge = Klassen)
const FL=[['Italy','Natürliche Zahlen',13,5],['Austria','Ganze Zahlen',11,5],['Switzerland','Grundrechenarten und Rechengesetze',14,5],['Slovenia','Potenzen als Schreibweise',7,5],['Greece','Teilbarkeit',7,5],['Germany','Brüche und Anteile',14,6],['Belgium','Dezimalzahlen',8,6],['United Kingdom','Rechnen mit rationalen Zahlen',12,6],['Spain','Zehnerpotenzen',7,6],['France','Potenzen und negative Exponenten',3,6],['Netherlands','Elementare Wurzeln',6,9],['Poland','Wurzeln und reelle Zahlen',7,9],['Norway','Rationale Exponenten',6,9]];
const W=1700,H=1150;
const eurBox={type:'MultiPoint',coordinates:[[-11,36],[32,36],[-11,63],[32,63],[10,35],[10,64.5]]};
const pE=d3.geoConicConformal().rotate([-12,0]).parallels([40,60]).fitExtent([[360,25],[1340,1125]],eurBox);
pE.clipExtent([[-5,-5],[W+5,H+5]]);const gpE=d3.geoPath(pE);
const r=n=>Math.round(n*10)/10;
const clip=(p)=>p; 
const eur=L50.map(f=>{const n=f.properties.name;const d=gpE(f);if(!d)return null;const b=gpE.bounds(f);if(b[1][0]<-50||b[0][0]>W+50||b[1][1]<-50||b[0][1]>H+50)return null;
 const e=EU[n];const fl=FL.findIndex(x=>x[0]===n);return {n,de:e?e[0]:null,hs:e?e[1]:null,hp:e?pE([e[3],e[2]]).map(r):null,c:gpE.centroid(f).map(r),d:d.replace(/X/g,'$1'),eu:!!e,fl:fl}}).filter(Boolean);
// Italien
const IT=[['Rom',41.90,12.50],['Neapel',40.85,14.27],['Pompei',40.75,14.50],['Bari',41.12,16.87],['Bologna',44.49,11.34],['Venedig',45.44,12.33],['Verona',45.44,10.99],['Mailand',45.46,9.19],['Turin',45.07,7.69],['Genua',44.41,8.93],['Pisa',43.72,10.40],['Florenz',43.77,11.25],['Siena',43.32,11.33]];
const WI=1700,HI=1300;const itF=L50.find(f=>f.properties.name==='Italy');
const pI=d3.geoConicConformal().rotate([-12,0]).parallels([38,46]).fitExtent([[450,60],[1250,1240]],itF);pI.clipExtent([[-5,-5],[WI+5,HI+5]]);const gpI=d3.geoPath(pI);
const ita=L50.map(f=>{const d=gpI(f);if(!d)return null;const b=gpI.bounds(f);if(b[1][0]<-50||b[0][0]>WI+50||b[1][1]<-50||b[0][1]>HI+50)return null;const e=EU[f.properties.name];return{n:f.properties.name,de:e?e[0]:f.properties.name,c:gpI.centroid(f).map(r),d:d.replace(/X/g,'$1')}}).filter(Boolean);
const itS=IT.map(([n,la,lo])=>({n,p:pI([lo,la]).map(r)}));
// Welt
const WW=1000,HW=560;const pW=d3.geoNaturalEarth1().fitExtent([[5,5],[WW-5,HW-5]],{type:'Sphere'});const gpW=d3.geoPath(pW);
const OR=['Turkey','Syria','Iraq','Iran','Saudi Arabia','Jordan','Israel','Lebanon','Yemen','Oman','United Arab Emirates','Qatar','Kuwait','Bahrain','Georgia','Armenia','Azerbaijan','Palestine','Cyprus','N. Cyprus'];
const MEL=['Papua New Guinea','Fiji','Solomon Is.','Vanuatu','New Caledonia','New Zealand','Australia'];
function kont(f){const n=f.properties.name;if(n==='Antarctica')return'ant';if(OR.includes(n))return'or';if(MEL.includes(n))return'au';if(EU[n]||n==='Russia')return n==='Russia'?'as':'eu';const [lo,la]=d3.geoCentroid(f);
 if(lo<-25)return la>13?'na':(la>8&&lo<-60?'na':'sa');if(lo<60&&la<37&&lo>-25&&!(lo>34&&la>12))return'af';if(lo>110&&la<-10)return'au';if(lo>-25&&lo<45&&la>34)return'eu';return'as'}
const welt=L110.map(f=>({k:kont(f),n:f.properties.name,d:gpW(f).replace(/X/g,'$1')}));
const grat=gpW(d3.geoGraticule10()).replace(/X/g,'$1'),sph=gpW({type:'Sphere'});
const LP={'Norway':[9,61.5],'Sweden':[15.5,62.5],'Finland':[26.5,62.8],'United Kingdom':[-1.8,53.2],'France':[2.4,46.6],'Croatia':[16.3,45.6],'Greece':[22,39.6],'Italy':[13.2,43.0],'Germany':[10.3,51.0],'Spain':[-3.6,39.4],'Portugal':[-8.2,39.6],'Poland':[19.3,52.0],'Austria':[14.4,47.5],'Switzerland':[8.2,46.75],'Ireland':[-8,53.2],'Denmark':[9.2,56.1],'Iceland':[-18.5,64.9],'Belarus':[28,53.5],'Ukraine':[31.5,49.0],'Romania':[24.8,45.9],'Bulgaria':[25.3,42.75],'Hungary':[19.4,47.1],'Czechia':[15.4,49.8],'Slovakia':[19.5,48.75],'Serbia':[20.8,43.9],'Lithuania':[23.9,55.3],'Latvia':[25.6,56.9],'Estonia':[25.8,58.7],'Netherlands':[5.6,52.3],'Belgium':[4.6,50.6],'Slovenia':[14.8,46.1],'Bosnia and Herz.':[17.8,44.2],'Albania':[20.1,41.1],'Macedonia':[21.7,41.6],'North Macedonia':[21.7,41.6],'Turkey':[33,39.2],'Russia':[36,57],'Morocco':[-6,32.5],'Algeria':[3,32.5],'Tunisia':[9.5,34.2],'Libya':[17,31]};
eur.forEach(x=>{if(LP[x.n])x.lp=pE(LP[x.n]).map(r)});
const WL=[['eu','Europa','Zahlen',[15,52],4,13],['as','Asien','Algebra',[95,45],1,19],['or','Orient','Funktionen',[48,30],0,10],['af','Afrika','Geometrie',[20,3],1,14],['na','Nordamerika','Geld und Verhältnisse',[-100,45],2,6],['sa','Südamerika','Fläche und Raum',[-60,-15],1,9],['au','Australien','Daten und Zufall',[134,-26],1,12],['po','Polynesien','Entdecker-Inseln',[-150,-12],0,4]].map(([k,n,g,ll,a,b])=>({k,n,g,p:pW(ll).map(r),a,b}));
const weltDu=pW([11.34,44.49]).map(r);const poly=pW([-150,-12]).map(r);
writeFileSync('geo.json',JSON.stringify({WL,weltDu,poly,eur,eurWH:[W,H],ita,itS,itWH:[WI,HI],welt,grat,sph,weltWH:[WW,HW]}));
console.log(eur.length,ita.length,welt.length,(JSON.stringify({eur,ita,welt}).length/1024|0)+'KB', eur.filter(x=>x.eu).map(x=>x.n).join(','));
