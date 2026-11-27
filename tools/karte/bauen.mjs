// RK-App (0.92.0): Umrisse der Reisekarte im Build vorrechnen – nur Werkzeug, nicht in der App.
// Aufruf (im Ordner tools/karte): npm ci && node bauen.mjs
// Schreibt nach karte/ (Repo-Wurzel): welt.json (Welt, 1:110 m), kontinent-<id>.json (je Reise-Kontinent eine Datei, 1:50 m, Landesteile 1:10 m),
// flaggen/<iso>.svg (nur die gebrauchten, quadratisch) und LIZENZEN.md.
// Quellen: Natural Earth (gemeinfrei) über world-atlas; Natural-Earth-Landesteile und -Hauptstädte (GitHub nvkelso/natural-earth-vector, werden nach
// tools/karte/quellen/ geladen, nicht im Repo); Ländernamen deutsch: i18n-iso-countries (MIT); Kontinent-Zuordnung für Länder ohne Reise: countries-list (MIT);
// Flaggen: flag-icons (MIT). Welche Länder zu welchem Reise-Kontinent gehören, steht in inhalte/reise/aufbau-vorschlag.json – die App nimmt Zustand und Städte
// aus schule_reise_karte; diese Dateien enthalten nur Umrisse, Namen und Hauptstädte (Kartendaten und Belegung getrennt).
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const HIER = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(HIER, '..', '..');
const ZIEL = path.join(REPO, 'karte');
const require = createRequire(path.join(HIER, 'package.json'));
const d3 = require('d3-geo');
const topo = require('topojson-client');
const server = require('topojson-server');
const vereinfache = require('topojson-simplify');
const ISO = require('i18n-iso-countries'); ISO.registerLocale(require('i18n-iso-countries/langs/de.json'));
const { countries: LISTE } = require('countries-list');

// ---------- Quellen ----------
const QUELLEN = path.join(HIER, 'quellen'); fs.mkdirSync(QUELLEN, { recursive: true });
const NE = 'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/';
function quelle(name) {
  const p = path.join(QUELLEN, name);
  if (!fs.existsSync(p)) execFileSync('curl', ['-sSfL', '-o', p, NE + name], { stdio: 'inherit' });
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}
const ADMIN1 = quelle('ne_10m_admin_1_states_provinces.geojson');
const ORTE = quelle('ne_10m_populated_places_simple.geojson');
const atlas = (n) => JSON.parse(fs.readFileSync(require.resolve(`world-atlas/countries-${n}.json`), 'utf8'));
const T110 = atlas('110m'); const T50 = atlas('50m');
const L110 = topo.feature(T110, T110.objects.countries).features;
const L50 = topo.feature(T50, T50.objects.countries).features;
const AUFBAU = JSON.parse(fs.readFileSync(path.join(REPO, 'inhalte/reise/aufbau-vorschlag.json'), 'utf8'));

// ---------- Zuordnung ----------
const a2Von = (f) => { const n = f.properties.name; if (n === 'Kosovo') return 'XK'; if (n === 'N. Cyprus') return 'CY'; if (n === 'Somaliland') return 'SO'; return f.id ? ISO.numericToAlpha2(f.id) || null : null; };
const schl = (iso, region) => (region ? `${iso}:${region}` : iso);
const MITGLIED = new Map(); // Schlüssel → { k, iso, region, name, hs, flug }
for (const k of AUFBAU.kontinente) for (const f of k.fluege) MITGLIED.set(schl(f.iso, f.region), { k: k.kontinent_id, iso: f.iso, region: f.region || null, name: f.land, hs: f.region ? (f.hauptort_landesteil ? { name: f.hauptort_landesteil.stadt, breite: f.hauptort_landesteil.breite, laenge: f.hauptort_landesteil.laenge } : null) : f.hauptstadt, flug: true });
for (const r of AUFBAU.reserve) for (const l of r.laender) if (!MITGLIED.has(schl(l.iso, l.region))) MITGLIED.set(schl(l.iso, l.region), { k: r.kontinent_id, iso: l.iso, region: l.region || null, name: l.land, hs: l.region ? null : l.hauptstadt, flug: false });
const KONT_IDS = AUFBAU.kontinente.map((k) => k.kontinent_id);
const isoKont = new Map(); for (const m of MITGLIED.values()) if (!m.region && !isoKont.has(m.iso)) isoKont.set(m.iso, m.k);
for (const m of MITGLIED.values()) if (m.region && !isoKont.has(m.iso)) isoKont.set(m.iso, m.k); // Land nur mit Landesteilen (AU, BR, NZ)
const ORIENT = ['TR', 'SY', 'IQ', 'IR', 'SA', 'JO', 'IL', 'LB', 'YE', 'OM', 'AE', 'QA', 'KW', 'BH', 'GE', 'AM', 'AZ', 'PS', 'CY'];
const MELANESIEN = ['PG', 'FJ', 'SB', 'VU', 'NC', 'NZ', 'AU', 'FM', 'GU', 'PW', 'MH', 'NR', 'MP'];
const POLYNESIEN = ['WS', 'TO', 'PF', 'TV', 'CK', 'NU', 'WF', 'AS', 'KI', 'PN', 'TK'];
const kontVon = (a2) => {
  if (!a2) return 0; if (a2 === 'AQ') return 'ant'; if (isoKont.has(a2)) return isoKont.get(a2);
  if (ORIENT.includes(a2)) return 4; if (MELANESIEN.includes(a2)) return 7; if (POLYNESIEN.includes(a2)) return 8; if (a2 === 'RU') return 3;
  return { EU: 1, NA: 2, AS: 3, AF: 5, SA: 6, OC: 7, AN: 'ant' }[LISTE[a2]?.continent] || 0;
};
const nameDe = (a2, fallback) => (a2 === 'XK' ? 'Kosovo' : (a2 && ISO.getName(a2, 'de', { select: 'official' }) && ISO.getName(a2, 'de')) || fallback);
// Hauptstädte: aus dem Reise-Aufbau (deutsche Namen), sonst Natural Earth (Admin-0 capital) mit kurzer deutscher Liste
const HS_DE = { Rome: 'Rom', Warsaw: 'Warschau', Prague: 'Prag', Vienna: 'Wien', Brussels: 'Brüssel', Lisbon: 'Lissabon', Copenhagen: 'Kopenhagen', Athens: 'Athen', Bucharest: 'Bukarest', Belgrade: 'Belgrad', Kyiv: 'Kiew', Kiev: 'Kiew', Moscow: 'Moskau', Cairo: 'Kairo', Beijing: 'Peking', Tokyo: 'Tokio', 'Mexico City': 'Mexiko-Stadt', Washington: 'Washington, D.C.', 'Washington, D.C.': 'Washington, D.C.', Algiers: 'Algier', Tripoli: 'Tripolis', Khartoum: 'Khartum', 'Addis Ababa': 'Addis Abeba', Damascus: 'Damaskus', Baghdad: 'Bagdad', Tehran: 'Teheran', 'New Delhi': 'Neu-Delhi', Pyongyang: 'Pjöngjang', 'Ulaanbaatar': 'Ulaanbaatar', Nicosia: 'Nikosia', Luxembourg: 'Luxemburg', Chisinau: 'Chișinău', Reykjavik: 'Reykjavík', Tbilisi: 'Tiflis', Yerevan: 'Jerewan', Tashkent: 'Taschkent', Bishkek: 'Bischkek', Dushanbe: 'Duschanbe', Ashgabat: 'Aşgabat', Riyadh: 'Riad', Sanaa: 'Sanaa', "Sana'a": 'Sanaa', Muscat: 'Maskat', 'Kuwait City': 'Kuwait', Kuwait: 'Kuwait', Havana: 'Havanna', Bogota: 'Bogotá', Brasilia: 'Brasília', Asuncion: 'Asunción', 'Panama City': 'Panama-Stadt', 'Guatemala City': 'Guatemala-Stadt', Singapore: 'Singapur', Mogadishu: 'Mogadischu', Djibouti: 'Dschibuti', Yaounde: 'Jaunde', "N'Djamena": 'N’Djamena', Vatican: 'Vatikanstadt', 'Vatican City': 'Vatikanstadt', Bern: 'Bern', 'Kuala Lumpur': 'Kuala Lumpur', Astana: 'Astana', 'Nur-Sultan': 'Astana', Valletta: 'Valletta', Vilnius: 'Vilnius', Riga: 'Riga', Tallinn: 'Tallinn', Helsinki: 'Helsinki', Stockholm: 'Stockholm', Oslo: 'Oslo', Dublin: 'Dublin', London: 'London', Paris: 'Paris', Madrid: 'Madrid', Amsterdam: 'Amsterdam', Berlin: 'Berlin', Budapest: 'Budapest', Bratislava: 'Bratislava', Ljubljana: 'Ljubljana', Zagreb: 'Zagreb', Sarajevo: 'Sarajevo', Podgorica: 'Podgorica', Pristina: 'Pristina', Tirana: 'Tirana', Skopje: 'Skopje', Sofia: 'Sofia', Minsk: 'Minsk', Ankara: 'Ankara', Beirut: 'Beirut', Amman: 'Amman', Jerusalem: 'Jerusalem', Manila: 'Manila', Hanoi: 'Hanoi', Bangkok: 'Bangkok', Vientiane: 'Vientiane', 'Phnom Penh': 'Phnom Penh', Seoul: 'Seoul', Taipei: 'Taipeh', Dhaka: 'Dhaka', Kathmandu: 'Kathmandu', Thimphu: 'Thimphu', Islamabad: 'Islamabad', Kabul: 'Kabul', Colombo: 'Colombo', 'Sri Jayewardenepura Kotte': 'Colombo', Jakarta: 'Jakarta', Dili: 'Dili', Canberra: 'Canberra', Wellington: 'Wellington', Ottawa: 'Ottawa', Lima: 'Lima', Quito: 'Quito', Caracas: 'Caracas', Santiago: 'Santiago de Chile', 'Buenos Aires': 'Buenos Aires', Montevideo: 'Montevideo', 'La Paz': 'La Paz', Sucre: 'Sucre', Georgetown: 'Georgetown', Paramaribo: 'Paramaribo', Cayenne: 'Cayenne', Nairobi: 'Nairobi', Kampala: 'Kampala', Kigali: 'Kigali', Lusaka: 'Lusaka', Harare: 'Harare', Pretoria: 'Pretoria', Windhoek: 'Windhuk', Gaborone: 'Gaborone', Maputo: 'Maputo', Antananarivo: 'Antananarivo', Luanda: 'Luanda', Kinshasa: 'Kinshasa', Abuja: 'Abuja', Accra: 'Accra', Dakar: 'Dakar', Rabat: 'Rabat', Tunis: 'Tunis', Nouakchott: 'Nouakchott', Bamako: 'Bamako', Niamey: 'Niamey', Ouagadougou: 'Ouagadougou' };
const HAUPTSTADT = new Map();
for (const f of ORTE.features) { const p = f.properties; if (!/^Admin-0 capital/.test(p.featurecla)) continue; const a2 = p.iso_a2 === '-99' ? null : p.iso_a2; if (!a2) continue;
  if (HAUPTSTADT.has(a2) && p.featurecla !== 'Admin-0 capital') continue; // „alt“-Hauptstädte nur, wenn nichts anderes da ist
  HAUPTSTADT.set(a2, { name: HS_DE[p.name] || p.name, breite: p.latitude, laenge: p.longitude }); }
// Hauptorte abhängiger Gebiete (Natural Earth „Admin-0 region capital“ bzw. „Admin-1 capital“), damit auch diese Gebiete Flagge und Hauptort zeigen.
// Bewusst nur eine geprüfte Liste (ISO → Name in Natural Earth → Anzeige). Nicht aufgenommen: PS (Ramallah/Gaza – Hauptstadt umstritten), HK/MO (Sonderverwaltungs-
// zonen, keine Hauptstadt), XK (Natural Earth ohne ISO-Code, Anerkennung umstritten), MP (Sitz Saipan/Capitol Hill uneinheitlich), JE/GG/SH (nicht in der Quelle).
const HS_GEBIET = { AX: ['Mariehamn'], KY: ['George Town'], TC: ['Grand Turk', 'Cockburn Town'], IM: ['Douglas'], CW: ['Willemstad'], AW: ['Oranjestad'], GI: ['Gibraltar'],
  NC: ['Nouméa'], BM: ['Hamilton'], GL: ['Nuuk'], FK: ['Stanley'], FO: ['Tórshavn'], PR: ['San Juan'], CK: ['Avarua'], NU: ['Alofi'] };
for (const [a2, [ne, anzeige]] of Object.entries(HS_GEBIET)) { if (HAUPTSTADT.has(a2)) continue;
  const f = ORTE.features.find((x) => x.properties.name === ne && /capital/.test(x.properties.featurecla) && (x.properties.iso_a2 === a2 || x.properties.adm0name === { NU: 'Niue', CK: 'Cook Islands' }[a2]));
  if (f) HAUPTSTADT.set(a2, { name: anzeige || ne, breite: f.properties.latitude, laenge: f.properties.longitude }); else console.warn('Hauptort fehlt in der Quelle:', a2, ne); }

// ---------- Landesteile (AU nach Bundesstaaten, NZ Nord/Süd, BR Großregionen, US Hawaii) – nur die, die im Reise-Aufbau vorkommen ----------
const BR_REGION = { Norte: 'BR_NORD', Nordeste: 'BR_NORDOST', 'Centro-Oeste': 'BR_MITTELWEST', Sudeste: 'BR_SUEDOST', Sul: 'BR_SUED' };
const NZ_REGION = { 'North Island': 'NORD', 'South Island': 'SUED' };
const regionVon = (p) => {
  if (p.iso_a2 === 'AU') return /^AS0\d$/.test(p.fips || '') ? p.fips.slice(2) : null;
  if (p.iso_a2 === 'NZ') return NZ_REGION[p.region] || null;
  if (p.iso_a2 === 'BR') return BR_REGION[p.region] || null;
  if (p.iso_a2 === 'US') return p.postal === 'HI' ? 'HI' : null;
  return null;
};
const teile = ADMIN1.features.filter((f) => regionVon(f.properties) && MITGLIED.has(schl(f.properties.iso_a2, regionVon(f.properties))));
const tTopo = vereinfache.presimplify(server.topology({ a: { type: 'FeatureCollection', features: teile } }, 1e6));
const tVer = vereinfache.simplify(tTopo, vereinfache.quantile(tTopo, 0.12)); // 1:10 m → etwa so fein wie 1:50 m
const REGIONEN = new Map(); // Schlüssel → GeoJSON-Geometrie
{ const gruppen = new Map(); tVer.objects.a.geometries.forEach((g, i) => { const p = teile[i].properties; const s = schl(p.iso_a2, regionVon(p)); if (!gruppen.has(s)) gruppen.set(s, []); gruppen.get(s).push(g); });
  for (const [s, gs] of gruppen) REGIONEN.set(s, topo.merge(tVer, gs)); }
const regionIsos = new Set([...REGIONEN.keys()].map((s) => s.split(':')[0]));

// ---------- Hilfen ----------
const r1 = (v) => Math.round(v * 10) / 10;
const wrap = (l) => ((l + 540) % 360) - 180;
const kreisMittel = (lons) => { let x = 0, y = 0; for (const l of lons) { x += Math.cos(l * Math.PI / 180); y += Math.sin(l * Math.PI / 180); } return Math.atan2(y, x) * 180 / Math.PI; };
function groesstes(geo) { if (geo.type !== 'MultiPolygon') return geo; let best = null, ba = -1; for (const c of geo.coordinates) { const g = { type: 'Polygon', coordinates: c }; const a = d3.geoArea(g); if (a > ba) { ba = a; best = g; } } return best; }
const projDaten = (p, art, rot) => ({ art, k: r1(p.scale() * 1000) / 1000, tx: r1(p.translate()[0] * 1000) / 1000, ty: r1(p.translate()[1] * 1000) / 1000, rot });

// ---------- Welt ----------
const WW = 1000, WH = 520;
const pW = d3.geoNaturalEarth1().fitExtent([[4, 4], [WW - 4, WH - 4]], { type: 'Sphere' });
const gW = d3.geoPath(pW).digits(1);
const welt = { stand: new Date().toISOString().slice(0, 10), w: WW, h: WH, proj: projDaten(pW, 'ne1', 0), gebiete: [], kontinente: [] };
for (const f of L110) { const a2 = a2Von(f); const k = kontVon(a2); const d = gW(f); if (!d) continue;
  welt.gebiete.push({ id: a2 || f.properties.name, iso: a2, k, n: nameDe(a2, f.properties.name), d, lp: pW(d3.geoCentroid(groesstes(f.geometry))).map(r1) }); }
for (const k of AUFBAU.kontinente) {
  const pts = [...k.fluege.map((f) => f.mitte), ...(AUFBAU.reserve.find((r) => r.kontinent_id === k.kontinent_id)?.laender || []).map((l) => l.mitte)].filter(Boolean);
  const c = kreisMittel(pts.map((p) => p.laenge)); const b = pts.reduce((s, p) => s + p.breite, 0) / pts.length;
  welt.kontinente.push({ id: k.kontinent_id, mitte: pW([c, b]).map(r1) });
}
welt.antarktis = { mitte: pW([0, -80]).map(r1) };
welt.graticule = d3.geoPath(pW).digits(0)(d3.geoGraticule10());
welt.kugel = d3.geoPath(pW).digits(1)({ type: 'Sphere' });

// ---------- je Reise-Kontinent ----------
const KW = 1600;
const dateien = [];
const flaggen = new Set();
for (const k of AUFBAU.kontinente) {
  const res = AUFBAU.reserve.find((r) => r.kontinent_id === k.kontinent_id)?.laender || [];
  const pts = [];
  for (const x of [...k.fluege, ...res]) { if (x.mitte) pts.push(x.mitte); if (x.hauptstadt && !x.region) pts.push(x.hauptstadt); if (x.hauptort_landesteil) pts.push(x.hauptort_landesteil);
    for (const s of x.staedte || []) pts.push(s); }
  const c = kreisMittel(pts.map((p) => p.laenge));
  const rl = pts.map((p) => wrap(p.laenge - c)); const br = pts.map((p) => p.breite);
  let [l0, l1, b0, b1] = [Math.min(...rl), Math.max(...rl), Math.min(...br), Math.max(...br)];
  const pl = Math.max(4, (l1 - l0) * 0.18), pb = Math.max(3, (b1 - b0) * 0.18); l0 -= pl; l1 += pl; b0 = Math.max(-75, b0 - pb); b1 = Math.min(80, b1 + pb);
  const ecken = { type: 'MultiPoint', coordinates: [[l0 + c, b0], [l1 + c, b0], [l0 + c, b1], [l1 + c, b1], [c, b0], [c, b1]] };
  const p0 = d3.geoMercator().rotate([-c, 0]).fitWidth(KW, ecken); const bb = d3.geoPath(p0).bounds(ecken);
  const KH = Math.max(700, Math.min(2600, Math.round(bb[1][1] - bb[0][1])));
  const p = d3.geoMercator().rotate([-c, 0]).fitExtent([[0, 0], [KW, KH]], ecken);
  p.clipExtent([[-40, -40], [KW + 40, KH + 40]]);
  const g = d3.geoPath(p).digits(1);
  const gebiete = [];
  const dazu = (id, iso, region, geo, kont, n) => {
    const d = g(geo); if (!d || d.length < 12) return; const b = g.bounds(geo); if (!Number.isFinite(b[0][0])) return;
    const gr = groesstes(geo); const lp = p(d3.geoCentroid(gr)); const m = MITGLIED.get(id);
    let hs = m?.hs || (!region ? HAUPTSTADT.get(iso) : null) || null; const hp = hs ? p([hs.laenge, hs.breite]) : null;
    if (hp && (hp[0] < -40 || hp[0] > KW + 40 || hp[1] < -40 || hp[1] > KH + 40)) hs = null;
    if (iso) flaggen.add(iso.toLowerCase());
    gebiete.push({ id, iso, ...(region ? { region } : {}), k: kont, n, d, b: b.flat().map(r1), lp: lp ? lp.map(r1) : null, a: Math.round(g.area(geo)), ...(hs && hp ? { hs: { n: hs.name, p: hp.map(r1) } } : {}) });
  };
  for (const f of L50) { const a2 = a2Von(f); if (a2 === 'AQ') continue;
    const hatTeile = a2 && regionIsos.has(a2) && [...REGIONEN.keys()].some((s) => s.startsWith(a2 + ':') && MITGLIED.get(s)?.k === k.kontinent_id);
    if (hatTeile) continue;
    dazu(a2 || f.properties.name, a2, null, f.geometry, kontVon(a2), MITGLIED.get(a2)?.name || nameDe(a2, f.properties.name)); }
  for (const [s, geo] of REGIONEN) { const m = MITGLIED.get(s); if (m.k !== k.kontinent_id) continue; dazu(s, m.iso, m.region, geo, m.k, m.name); }
  const datei = { id: k.kontinent_id, reise: k.reise, w: KW, h: KH, proj: projDaten(p, 'merc', c), gebiete };
  const name = `kontinent-${k.kontinent_id}.json`;
  fs.mkdirSync(ZIEL, { recursive: true }); fs.writeFileSync(path.join(ZIEL, name), JSON.stringify(datei));
  dateien.push([name, fs.statSync(path.join(ZIEL, name)).size, gebiete.length]);
  // Probe: Formel der App (unten) = d3
  for (const q of pts.slice(0, 20)) { const a = p([q.laenge, q.breite]); const b2 = projApp(datei.proj, q.laenge, q.breite); if (Math.hypot(a[0] - b2[0], a[1] - b2[1]) > 0.6) throw new Error(`Projektion weicht ab (${name}): ${a} ≠ ${b2}`); }
}
fs.writeFileSync(path.join(ZIEL, 'welt.json'), JSON.stringify(welt));
dateien.unshift(['welt.json', fs.statSync(path.join(ZIEL, 'welt.json')).size, welt.gebiete.length]);
for (const q of [[12.5, 41.9], [-150, -17], [151, -33], [-70, -50]]) { const a = pW(q); const b2 = projApp(welt.proj, q[0], q[1]); if (Math.hypot(a[0] - b2[0], a[1] - b2[1]) > 0.6) throw new Error(`Projektion Welt weicht ab: ${a} ≠ ${b2}`); }

// ---------- Flaggen (quadratisch, nur die gebrauchten) ----------
const FL = path.join(ZIEL, 'flaggen'); fs.rmSync(FL, { recursive: true, force: true }); fs.mkdirSync(FL, { recursive: true });
let flagBytes = 0, flagN = 0; const ohneFlagge = [];
for (const iso of [...flaggen].sort()) { const q = path.join(HIER, 'node_modules', 'flag-icons', 'flags', '1x1', iso + '.svg');
  if (!fs.existsSync(q)) { ohneFlagge.push(iso); continue; } fs.copyFileSync(q, path.join(FL, iso + '.svg')); flagBytes += fs.statSync(q).size; flagN++; }

// ---------- Lizenzen ----------
const lic = (pkg) => { const d = path.join(HIER, 'node_modules', pkg); const f = fs.readdirSync(d).find((x) => /^licen[sc]e/i.test(x)); return f ? fs.readFileSync(path.join(d, f), 'utf8').trim() : '(Lizenztext nicht gefunden)'; };
fs.writeFileSync(path.join(ZIEL, 'LIZENZEN.md'), `# Quellen und Lizenzen der Reisekarte

Erzeugt von \`tools/karte/bauen.mjs\` (${welt.stand}).

- **Natural Earth** (Ländergrenzen 1:110 m und 1:50 m über das npm-Paket world-atlas; Landesteile und Hauptstädte 1:10 m): gemeinfrei (public domain), https://www.naturalearthdata.com/
- **GeoNames** (Städte der Reise, Lage und Namen; kommen aus der Datenbank, \`schule_reise_karte\`): CC BY 4.0, https://www.geonames.org/
- **COMNAP Antarctic Facilities** (Stationen der Expeditionen): Nutzung nur privat, nicht kommerziell, zu Bildungszwecken, mit Quellenangabe, https://www.comnap.aq/
- **flag-icons** (Flaggen), **i18n-iso-countries** (Ländernamen deutsch), **countries-list** (Kontinente): MIT, Lizenztexte unten.

## flag-icons

${lic('flag-icons')}

## i18n-iso-countries

${lic('i18n-iso-countries')}

## countries-list

${lic('countries-list')}
`);

console.log('Dateien:'); for (const [n, s, g] of dateien) console.log(`  ${n.padEnd(18)} ${(s / 1024).toFixed(0).padStart(5)} KB  ${g} Gebiete`);
console.log(`  flaggen/          ${(flagBytes / 1024).toFixed(0).padStart(5)} KB  ${flagN} Flaggen${ohneFlagge.length ? ' (ohne: ' + ohneFlagge.join(', ') + ')' : ''}`);

// Projektion wie in der App (lernen.js, lernKarteProj) – zur Probe gegen d3
function projApp(q, lon, lat) {
  const rad = Math.PI / 180; let l = ((lon + q.rot + 540) % 360 - 180) * rad; if (q.art === 'merc') l = ((lon - q.rot + 540) % 360 - 180) * rad; const f = lat * rad;
  let x, y;
  if (q.art === 'merc') { x = l; y = Math.log(Math.tan(Math.PI / 4 + f / 2)); }
  else { const f2 = f * f, f4 = f2 * f2; x = l * (0.8707 - 0.131979 * f2 + f4 * (-0.013791 + f4 * (0.003971 * f2 - 0.001529 * f4))); y = f * (1.007226 + f2 * (0.015085 + f4 * (-0.044475 + 0.028874 * f2 - 0.005916 * f4))); }
  return [q.tx + q.k * x, q.ty - q.k * y];
}
