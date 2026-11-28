// ================= ENTWURF 2 · Weihnachts-Ebene v4/v5, grafisch überarbeitet =================
// Stil: flache Formen mit dunklerer Unterkante (wie die Planeten im Regel-Universum), Licht von oben links,
// eine Schattenfarbe je Fläche, kleine Glanzkante. Keine Umrisslinien außer bei sehr kleinen Formen.
// Alles bleibt reine Grafik: pointer-events none, aria-hidden, keine Knöpfe.

// Beschriftungen im Standbild (Kasten x, y, b, h). In der App überflüssig: dort liegt die Tönung als Gruppe UNTER Pins und Namen.
KARTEN[390].namen = [[26,139,101,16],[219,163,71,13],[251,220,61,24],[186,276,91,25],[255,312,42,13],[12,325,59,12],[150,335,53,14],[128,369,79,13],[278,378,79,15],[95,400,57,25],[259,414,73,24],[238,475,48,25],[63,496,54,14],[357,530,21,14],[130,561,54,24],[22,597,57,24],[238,611,42,24]];
KARTEN[1280].namen = [[35,154,101,16],[480,136,72,25],[592,163,62,23],[700,136,57,24],[660,196,52,24],[687,234,57,24],[506,270,61,23],[638,298,47,23],[742,319,52,23],[330,320,87,25],[209,334,42,23],[401,346,92,26],[642,354,55,25],[121,372,159,25],[380,389,54,25],[788,408,50,23],[535,417,68,24],[348,439,79,24],[569,453,78,25],[428,483,58,25],[540,503,73,25],[630,540,49,23],[719,548,58,24],[675,587,62,24],[509,595,48,25],[252,625,55,25],[163,668,58,25],[686,675,95,26],[354,714,53,24],[465,712,55,24]];
// Pins mit Abzeichen oben rechts (Zahl, Haken, Stern, Flieger): Mütze kippt dann weiter nach links, damit das Abzeichen frei bleibt.
KARTEN[390].abzeichen = [[231, 315], [168, 411], [243, 424], [263, 388], [221, 485], [341, 540]];
KARTEN[1280].abzeichen = [[508, 356], [413, 492], [524, 513], [553, 463], [492, 605], [669, 683]];

// Einzelne Kartenknöpfe im Standbild (nur für das Freistellen in v5)
KARTEN[390].knoepfe = [[325, 87, 43, 45], [325, 142, 43, 45], [325, 197, 43, 45], [325, 250, 43, 45], [325, 305, 43, 45]];
KARTEN[1280].knoepfe = [[835, 103, 43, 46], [835, 158, 43, 46], [835, 211, 43, 46], [835, 265, 43, 46]];
KARTEN[390].karte = [24, 699, 212, 126]; KARTEN[390].still = .6; KARTEN[1280].still = .6; KARTEN[1280].karteNacht = [916, 138, 150, 208];
const FEST_LICHT = ['#FFC94A', '#FF5A5F', '#FFF3D1', '#3DDC84']; // Gold · Rot · Warmweiß · Grün – feste Folge, keine Würfelei
const zz = (n) => { const x = Math.sin(n * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); }; // fester Zufall je Zahl
const f1 = (v) => Math.round(v * 10) / 10;

// ---------- Bausteine (Einheiten: Pin-Kopf mit Radius 10, Mitte 0/0) ----------
function festDefs(u, nacht) {
  const fell = nacht ? ['#FFFFFF', '#C9D6EA'] : ['#FFFFFF', '#C7D3E3'];
  return `<linearGradient id="${u}kegel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF5A6B"/><stop offset=".55" stop-color="#E5243B"/><stop offset="1" stop-color="#B3122B"/></linearGradient>
    <radialGradient id="${u}bommel" cx=".38" cy=".34" r=".7"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".6" stop-color="#F3F6FA"/><stop offset="1" stop-color="${fell[1]}"/></radialGradient>
    <linearGradient id="${u}eis" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".45" stop-color="#DDF0FB"/><stop offset="1" stop-color="#A9D7F2" stop-opacity=".75"/></linearGradient>
    <linearGradient id="${u}schnee" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#F1F7FC"/></linearGradient>
    ${FEST_LICHT.map((c, i) => `<radialGradient id="${u}gl${i}"><stop offset="0" stop-color="${c}" stop-opacity="${nacht ? .95 : .7}"/><stop offset=".35" stop-color="${c}" stop-opacity="${nacht ? .45 : .28}"/><stop offset="1" stop-color="${c}" stop-opacity="0"/></radialGradient>
    <radialGradient id="${u}bi${i}" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".35" stop-color="${c}"/><stop offset="1" stop-color="${dunkler(c, .32)}"/></radialGradient>`).join('')}`;
}
function dunkler(hex, k) { const n = parseInt(hex.slice(1), 16); const r = (n >> 16) & 255, g = (n >> 8) & 255, b = n & 255; const f = (v) => Math.round(v * (1 - k)).toString(16).padStart(2, '0'); return '#' + f(r) + f(g) + f(b); }
const bogen = (r, a0, a1) => { const p = (a) => [f1(Math.cos(a * Math.PI / 180) * r), f1(Math.sin(a * Math.PI / 180) * r)]; const [x0, y0] = p(a0), [x1, y1] = p(a1); return `M${x0} ${y0} A${r} ${r} 0 0 1 ${x1} ${y1}`; };

// Mütze: sitzt mit dem Fellrand auf dem oberen Kopfrand, Zipfel fällt nach links (Abzeichen sitzen rechts oben).
function festMuetze(u, x, y, r, rot, k = 1, nacht = false) {
  const s = (r / 10) * k; const schatten = nacht ? 'rgba(0,0,0,.35)' : 'rgba(40,10,20,.22)';
  return `<g transform="translate(${f1(x)} ${f1(y)}) rotate(${f1(rot)}) scale(${f1(s * 100) / 100})">
    <path d="${bogen(8.3, -140, -40)}" stroke="${schatten}" stroke-width="1.6" fill="none" stroke-linecap="round"/><g transform="translate(0 1.1)">
    <path d="M7.4 -9.6 C7.2 -16 4.6 -22.2 -.6 -24.6 C-5.8 -26.8 -11 -25.2 -14 -20.6 C-11 -21.6 -7.2 -21 -4.2 -18.6 C-6 -15.4 -7.1 -12.4 -7.4 -9.6 Z" fill="url(#${u}kegel)"/>
    <path d="M7.4 -9.6 C7.2 -16 4.6 -22.2 -.6 -24.6 C2.6 -20.4 3.8 -15 3.8 -9.6 Z" fill="#9E0F27" opacity=".55"/>
    <path d="M-14 -20.6 C-11 -21.6 -7.2 -21 -4.2 -18.6 C-7 -19.4 -10.4 -19.8 -14 -20.6 Z" fill="#7E0B1F" opacity=".7"/>
    <path d="M-1.2 -24.4 C-6 -26.4 -10.6 -25 -13.4 -21.2 C-10.2 -23.4 -6 -24.2 -2.4 -23.2 Z" fill="#FF9AA5" opacity=".75"/>
    </g><path d="${bogen(10, -142, -38)}" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path d="${bogen(8.6, -136, -44)}" stroke="${nacht ? '#B8C7DD' : '#C7D3E3'}" stroke-width="1.3" fill="none" stroke-linecap="round"/>
    ${[-128, -108, -88, -68, -50].map((a) => `<circle cx="${f1(Math.cos(a * Math.PI / 180) * 11.7)}" cy="${f1(Math.sin(a * Math.PI / 180) * 11.7)}" r=".95" fill="#fff"/>`).join('')}
    <circle cx="-14.6" cy="-18.3" r="3.5" fill="url(#${u}bommel)"/><circle cx="-13.4" cy="-16.5" r="1.4" fill="${nacht ? '#B8C7DD' : '#C7D3E3'}" opacity=".6"/></g>`;
}
// Schneehäubchen für kleine Pins (statt Mütze): weißer Bogen mit zwei Tropfen, Schattenkante unten
function festHaeubchen(x, y, r, nacht) {
  const s = r / 10;
  return `<g transform="translate(${f1(x)} ${f1(y)}) scale(${f1(s * 100) / 100})"><path d="${bogen(10.4, -152, -28)}" stroke="${nacht ? '#8FA6C2' : '#A9C3D6'}" stroke-width="3.6" fill="none" stroke-linecap="round" transform="translate(0 .9)"/>
    <path d="${bogen(10.4, -152, -28)}" stroke="#fff" stroke-width="3.4" fill="none" stroke-linecap="round"/><path d="M-4.6 -9 q.7 3.2 1.6 0Z M3.2 -9.6 q.8 4.2 1.7 0Z" fill="#fff"/></g>`;
}
// Tanne (Einheit: Höhe ~22, Fuß bei 0)
function festTanne(x, y, k) {
  return `<g transform="translate(${f1(x)} ${f1(y)}) scale(${f1(k * 100) / 100})"><ellipse cx="0" cy=".6" rx="7" ry="1.6" fill="#0B2A1A" opacity=".18"/><rect x="-1.4" y="-2.4" width="2.8" height="3" rx=".6" fill="#7A4A26"/>
    <path d="M0 -21 L5.4 -13.4 Q2.6 -12.6 0 -13 Q-2.6 -12.6 -5.4 -13.4 Z M0 -16 L7.2 -7.6 Q3.4 -6.6 0 -7 Q-3.4 -6.6 -7.2 -7.6 Z M0 -10.4 L9 -1.8 Q4.4 -.6 0 -1 Q-4.4 -.6 -9 -1.8 Z" fill="#1F7A4C"/>
    <path d="M0 -21 L5.4 -13.4 Q2.6 -12.6 0 -13 Z M0 -16 L7.2 -7.6 Q3.4 -6.6 0 -7 Z M0 -10.4 L9 -1.8 Q4.4 -.6 0 -1 Z" fill="#11532F"/>
    <path d="M-5.4 -13.4 Q-2.6 -12.6 0 -13 M-7.2 -7.6 Q-3.4 -6.6 0 -7 M-9 -1.8 Q-4.4 -.6 0 -1" stroke="#E9F6EF" stroke-width="1.1" fill="none" stroke-linecap="round"/>
    <circle cx="-2.6" cy="-9.2" r="1.1" fill="#FF5A5F"/><circle cx="3" cy="-4" r="1.1" fill="#FFC94A"/><circle cx="-3.6" cy="-3.2" r="1" fill="#FFF3D1"/>
    <path d="M0 -24.6 l1.1 2.3 2.5 .3 -1.9 1.7 .6 2.5 -2.3 -1.3 -2.3 1.3 .6 -2.5 -1.9 -1.7 2.5 -.3z" fill="#FFC94A"/><path d="M0 -24.6 l1.1 2.3 2.5 .3 -1.9 1.7 .6 2.5 -2.3 -1.3z" fill="#E09E16"/></g>`;
}
// Geschenk in 2,5D: Vorderseite, Seite im Schatten, Deckel, Band, Schleife
function festPaket(x, y, farbe, band, k) {
  const d = dunkler(farbe, .3);
  return `<g transform="translate(${f1(x)} ${f1(y)}) scale(${f1(k * 100) / 100})"><ellipse cx="1.4" cy=".4" rx="7.4" ry="1.4" fill="#000" opacity=".14"/>
    <path d="M-5 -8 H5 V0 H-5Z" fill="${farbe}"/><path d="M5 -8 L7.6 -9.6 V-1.6 L5 0Z" fill="${d}"/><path d="M-5.6 -10.4 H5.6 L8.2 -12 H-3Z" fill="${dunkler(farbe, -.25 > 0 ? 0 : .08)}"/><path d="M-5.6 -10.4 H5.6 V-8 H-5.6Z" fill="${farbe}"/><path d="M5.6 -10.4 L8.2 -12 V-9.6 L5.6 -8Z" fill="${d}"/>
    <path d="M-1 -10.4 H1 V0 H-1Z" fill="${band}"/><path d="M1 -10.4 L3.4 -12 H5.2 L2.4 -10.4Z" fill="${band}" opacity=".85"/>
    <path d="M.2 -12.2 C-3.6 -16.4 -6.6 -12.6 -1.2 -11.6 Z M.2 -12.2 C3.8 -16.6 7 -13 1.6 -11.6 Z" fill="${band}"/><circle cx=".2" cy="-11.9" r="1.1" fill="${dunkler(band, .2)}"/></g>`;
}
// Schlitten mit zwei Rentieren als klare Scherenschnitt-Illustration (Blick nach rechts, Ursprung Mitte)
function festSchlitten(nacht, k) {
  const fell = nacht ? '#E2C9A0' : '#4A2E1F', fellS = nacht ? '#B8996E' : '#2E1B12', geweih = nacht ? '#F6E7C8' : '#8A5A33', gold = '#F2C14E';
  const tier = (x, y, phase) => `<g transform="translate(${x} ${y})">
    <path d="M-9 1.2 C-12 2.6 -15 3 -18 ${phase ? 1.8 : 2.6} M-8 2.4 C-10 4.8 -12.6 6 -15.4 ${phase ? 6.8 : 6}" stroke="${fellS}" stroke-width="1.7" fill="none" stroke-linecap="round"/>
    <path d="M7 2.4 C9.6 3.4 12.6 3.4 15.6 ${phase ? 1.6 : 2.4} M6.4 3.4 C8.4 5.6 11 6.8 13.4 ${phase ? 8 : 7.2}" stroke="${fellS}" stroke-width="1.7" fill="none" stroke-linecap="round"/>
    <path d="M-10.4 -.4 C-10.4 -4.6 -5 -6 1 -6 C6 -6 9 -4.8 10.8 -2.2 C12.4 -5 14 -8.4 15.4 -11.6 C16.2 -13.6 18.6 -14.4 20.6 -13 C22 -12 23.4 -11.6 24.6 -10.6 C25.6 -9.8 25 -8.6 23.8 -8.6 C22 -8.6 20.6 -8.6 19.4 -9 C18 -6.6 16 -2.4 13.2 .8 C11.2 3.2 7.4 4 2 4 C-5 4 -10.4 3.4 -10.4 -.4 Z" fill="${fell}"/>
    <path d="M-10.4 -.4 C-10.4 1.8 -6 3.6 2 3.6 C6.6 3.6 10 3 12.2 1.4 C10 2 6 2.2 2 2.2 C-4 2.2 -8.6 1.6 -10.4 -.4Z" fill="${fellS}" opacity=".7"/>
    <path d="M-10.2 -1.6 l-3.4 -2.6 1.2 3.8z" fill="${fell}"/><path d="M18.4 -13.2 l-2.4 -2.6 3.4 1.2z" fill="${fellS}"/>
    <path d="M19.4 -14 C18.8 -17.6 17 -19.6 14.8 -21 M17.8 -16.8 l-3 .4 M16.4 -19 l-1.4 -2.4 M20.6 -14 C21.6 -17.4 23.4 -19.2 25.4 -20.2 M22.4 -17.4 l2.6 -.6" stroke="${geweih}" stroke-width="1.15" fill="none" stroke-linecap="round"/>
    <circle cx="21.4" cy="-11.4" r=".75" fill="${nacht ? '#3A2418' : '#F6E7C8'}"/>
    <path d="M9.6 -4.4 C11 -3.4 12.4 -3 13.8 -3.6" stroke="${gold}" stroke-width="1.3" fill="none"/><circle cx="12.2" cy="-2.4" r="1.2" fill="${gold}"/></g>`;
  return `<g transform="scale(${k}) translate(-34 2)">
    <g fill="#FFE27A">${[[-30, 2, 1.2, .9], [-38, 5, .9, .7], [-46, 3, .7, .5], [-54, 7, .6, .35], [-25, 8, .7, .6], [-60, 2, .5, .25]].map(([x, y, r, o]) => `<circle cx="${x}" cy="${y}" r="${r}" opacity="${o}"/>`).join('')}<path d="M-34 -2 l.8 2 2 .8 -2 .8 -.8 2 -.8 -2 -2 -.8 2 -.8z" opacity=".9"/></g>
    <path d="M14 -1 C22 -3 30 -4 38 -3 M38 -3 C46 -4 54 -7 62 -8" stroke="${gold}" stroke-width=".9" fill="none" opacity=".95"/>
    ${tier(44, 0, 0)}${tier(70, -6, 1)}
    <path d="M-9 -3 C-11 -10 -6 -14.6 -1.6 -12.6 C1 -14.8 5 -12.4 4 -3 Z" fill="${nacht ? '#C08A55' : '#8A5A33'}"/><path d="M-1.6 -12.6 C1 -14.8 5 -12.4 4 -3 L1.4 -3 C2.4 -8 1 -11.4 -1.6 -12.6Z" fill="#000" opacity=".2"/>
    <rect x="-6.6" y="-17.4" width="6" height="5.6" rx=".8" fill="#3DDC84" transform="rotate(-10 -3.6 -14.6)"/><rect x="-4.4" y="-17.6" width="1.4" height="5.8" fill="#FFF3D1" transform="rotate(-10 -3.6 -14.6)"/>
    <rect x=".4" y="-16.4" width="5" height="4.6" rx=".8" fill="#FFC94A" transform="rotate(8 2.9 -14.1)"/><rect x="2.3" y="-16.6" width="1.2" height="4.8" fill="#E5243B" transform="rotate(8 2.9 -14.1)"/>
    <path d="M-15 -11 C-17.6 -12.6 -19.4 -9.6 -17 -8.2 C-15.4 -7.4 -14 -8.6 -14.2 -10 L-14 2.6 C-14 5 -12.6 6.4 -10 6.4 H8.4 C11.8 6.4 13.4 3.8 13.4 0 V-3 H-6 C-9.4 -3 -10.6 -5.4 -10.8 -8.6 C-11 -11.6 -12.8 -12.6 -15 -11 Z" fill="#E5243B"/>
    <path d="M-14 2.6 C-14 5 -12.6 6.4 -10 6.4 H8.4 C11.8 6.4 13.4 3.8 13.4 0 V1 C12 3.6 10.4 4.4 8 4.4 H-10 C-12 4.4 -13.4 3.6 -14 2.6Z" fill="#9E0F27"/>
    <path d="M-12.6 -8.6 C-12.4 -10.4 -11.6 -11 -10.8 -9.6" stroke="#FF9AA5" stroke-width=".8" fill="none" stroke-linecap="round"/><path d="M-6 -3 H13.4" stroke="${gold}" stroke-width="1.2"/>
    <path d="M-10 6.4 V10 M6 6.4 V10" stroke="${gold}" stroke-width="1.2"/><path d="M-17 10 H14 C18.6 10 20.4 7.6 20 5.2 C19.6 3.4 17.6 3.6 17.8 5.2" stroke="${gold}" stroke-width="1.6" fill="none" stroke-linecap="round"/></g>`;
}
// Lichterkette: echtes Kabel (Kettenlinie), Fassungen, Glühbirnen, weiches Leuchten in 3 Gruppen (3 animierte Knoten)
function festLichterkette(u, anf, ende, y0, s, nacht) {
  const n = Math.max(2, Math.round((ende - anf) / (92 * s))); const w = (ende - anf) / n; const kabel = [], birnen = [], glanz = [[], [], []];
  let d = `M${f1(anf)} ${f1(y0)}`; let idx = 0;
  for (let i = 0; i < n; i++) {
    const a = anf + i * w, b = a + w, sag = (17 + (i % 2) * 3) * s;
    const c1 = [a + w * .28, y0 + sag * 1.33], c2 = [b - w * .28, y0 + sag * 1.33];
    d += ` C${f1(c1[0])} ${f1(c1[1])} ${f1(c2[0])} ${f1(c2[1])} ${f1(b)} ${f1(y0)}`;
    const P = (t) => { const m = 1 - t; return [m * m * m * a + 3 * m * m * t * c1[0] + 3 * m * t * t * c2[0] + t * t * t * b, m * m * m * y0 + 3 * m * m * t * c1[1] + 3 * m * t * t * c2[1] + t * t * t * y0]; };
    for (const t of [.22, .41, .59, .78]) {
      const [x, y] = P(t), [x2, y2] = P(t + .01); const tang = Math.atan2(y2 - y, x2 - x) * 180 / Math.PI; const c = idx % 4; const g = idx % 3; idx++;
      const kipp = f1(tang * .55 + (zz(idx) - .5) * 14);
      glanz[g].push(`<circle cx="${f1(x)}" cy="${f1(y + 7 * s)}" r="${f1((nacht ? 11 : 8) * s)}" fill="url(#${u}gl${c})"/>`);
      birnen.push(`<g transform="translate(${f1(x)} ${f1(y)}) rotate(${kipp}) scale(${s})"><rect x="-1.7" y="-.6" width="3.4" height="3.6" rx=".7" fill="${nacht ? '#4B6B57' : '#24402F'}"/><path d="M-1.7 .6 H1.7 M-1.7 1.8 H1.7" stroke="${nacht ? '#6F927C' : '#3E6450'}" stroke-width=".5"/>
        <path d="M-2.3 3 C-3.4 5 -3.6 8.6 0 11.2 C3.6 8.6 3.4 5 2.3 3 Z" fill="url(#${u}bi${c})"/><ellipse cx="-1" cy="6" rx=".7" ry="1.6" fill="#fff" opacity=".8" transform="rotate(14 -1 6)"/></g>`);
    }
  }
  kabel.push(`<path d="${d}" stroke="${nacht ? '#5E7D68' : '#24402F'}" stroke-width="${f1(1.7 * s)}" fill="none" stroke-linecap="round"/><path d="${d}" stroke="${nacht ? '#9FC0AA' : '#4E7A62'}" stroke-width="${f1(.5 * s)}" fill="none" transform="translate(0 ${f1(-.5 * s)})" opacity=".8"/>`);
  return `<g class="fk">${glanz.map((g, i) => `<g class="fk-glanz fk${i}">${g.join('')}</g>`).join('')}${kabel.join('')}${birnen.join('')}</g>`;
}
// Schneehaube mit Volumen: Körper, Schattenkante, Glanz oben, Eiszapfen an den tiefsten Stellen
function festHaube(u, x0, x1, y0, tiefe, s, nacht, seed, frei = [], topAmp = 0) {
  const pkte = []; let x = x0; let i = 0;
  while (x < x1) { const q = zz(seed + i); const b = (q < .25 ? 38 + q * 30 : 12 + q * 26) * s; const t = (tiefe * (q < .25 ? .35 : .5 + zz(seed + i * 3) * .7)) * s; pkte.push([x, Math.min(x + b, x1), t]); x += b; i++; }
  let d; const zapfen = [];
  if (!topAmp) d = `M${f1(x0)} ${f1(y0 - 30 * s)} H${f1(x1)} V${f1(y0)}`;
  else { d = `M${f1(x0)} ${f1(y0)} C${f1(x0)} ${f1(y0 - topAmp * .8 * s)} ${f1(x0 + 6 * s)} ${f1(y0 - topAmp * s)} ${f1(x0 + 12 * s)} ${f1(y0 - topAmp * s)}`; let x = x0 + 12 * s, k = 0;
    while (x < x1 - 30 * s) { const b = (22 + zz(seed + k * 5) * 26) * s; const h = topAmp * (.75 + zz(seed + k * 9) * .5) * s; d += ` Q${f1(x + b / 2)} ${f1(y0 - h - 3 * s)} ${f1(x + b)} ${f1(y0 - topAmp * .8 * s)}`; x += b; k++; }
    d += ` C${f1(x1 - 4 * s)} ${f1(y0 - topAmp * .8 * s)} ${f1(x1)} ${f1(y0 - topAmp * .4 * s)} ${f1(x1)} ${f1(y0)}`; }
  for (let j = pkte.length - 1; j >= 0; j--) { const [a, b, t] = pkte[j]; const m = (a + b) / 2;
    d += ` C${f1(b - (b - a) * .15)} ${f1(y0 + t)} ${f1(m + (b - a) * .2)} ${f1(y0 + t * 1.15)} ${f1(m)} ${f1(y0 + t * 1.1)} C${f1(m - (b - a) * .2)} ${f1(y0 + t * 1.05)} ${f1(a + (b - a) * .15)} ${f1(y0 + t)} ${f1(a)} ${f1(y0 + t * .25)}`;
    if (zz(seed + j * 7) > .42 && !frei.some(([fa, fb]) => m > fa && m < fb)) { const n = zz(seed + j) > .6 ? 2 : 1; for (let q = 0; q < n; q++) zapfen.push([m + (q ? 3.2 : -1) * s, y0 + t * 1.05, (5 + zz(seed + j * 11 + q) * 9) * s * (q ? .6 : 1)]); } }
  d += topAmp ? ' Z' : ` V${f1(y0 - 30 * s)} Z`;
  const kante = nacht ? '#7F9BB8' : '#B5CFE2';
  const z = zapfen.map(([zx, zy, h]) => { const w = 1.9 * s; return `<path d="M${f1(zx - w)} ${f1(zy - 1)} C${f1(zx - w * .8)} ${f1(zy + h * .45)} ${f1(zx - w * .2)} ${f1(zy + h * .85)} ${f1(zx + .2)} ${f1(zy + h)} C${f1(zx + w * .35)} ${f1(zy + h * .7)} ${f1(zx + w * .8)} ${f1(zy + h * .35)} ${f1(zx + w)} ${f1(zy - 1)} Z" fill="url(#${u}eis)"/><path d="M${f1(zx - w * .45)} ${f1(zy + 1)} L${f1(zx - w * .1)} ${f1(zy + h * .65)}" stroke="#fff" stroke-width="${f1(.6 * s)}" stroke-linecap="round" opacity=".9"/>`; }).join('');
  return `<path d="${d}" fill="#0B2A44" opacity="${nacht ? .35 : .12}" transform="translate(0 ${f1(2.4 * s)})"/><path d="${d}" fill="${kante}" transform="translate(0 ${f1(1.3 * s)})"/>${z}<path d="${d}" fill="url(#${u}schnee)"/>
    ${topAmp ? '' : `<path d="M${f1(x0)} ${f1(y0 - 1.2 * s)} H${f1(x1)}" stroke="#fff" stroke-width="${f1(1 * s)}" opacity=".9"/>`}`;
}
// Schneewehe (Ecke unten rechts): zwei Hügel, Schatten rechts unten, Glanz oben links, ein Funkeln
function festWehe(W, H, s, nacht) {
  const kante = nacht ? '#7F9BB8' : '#B5CFE2';
  const a = `M${f1(W - 128 * s)} ${H} C${f1(W - 112 * s)} ${f1(H - 13 * s)} ${f1(W - 88 * s)} ${f1(H - 19 * s)} ${f1(W - 66 * s)} ${f1(H - 15 * s)} C${f1(W - 52 * s)} ${f1(H - 28 * s)} ${f1(W - 22 * s)} ${f1(H - 34 * s)} ${W} ${f1(H - 30 * s)} V${H} Z`;
  return `<path d="${a}" fill="#0B2A44" opacity="${nacht ? .3 : .1}" transform="translate(${f1(-2 * s)} ${f1(-1 * s)})"/><path d="${a}" fill="${kante}"/><path d="${a}" fill="#fff" transform="translate(${f1(2 * s)} ${f1(2.6 * s)})"/>
    <path d="M${f1(W - 112 * s)} ${f1(H - 8 * s)} C${f1(W - 96 * s)} ${f1(H - 15 * s)} ${f1(W - 82 * s)} ${f1(H - 16 * s)} ${f1(W - 70 * s)} ${f1(H - 13 * s)} M${f1(W - 58 * s)} ${f1(H - 22 * s)} C${f1(W - 44 * s)} ${f1(H - 30 * s)} ${f1(W - 26 * s)} ${f1(H - 31 * s)} ${f1(W - 12 * s)} ${f1(H - 28.5 * s)}" stroke="#fff" stroke-width="${f1(1.4 * s)}" fill="none" stroke-linecap="round" opacity=".95"/>
    <path d="M${f1(W - 36 * s)} ${f1(H - 22 * s)} l${f1(.9 * s)} ${f1(2.2 * s)} ${f1(2.2 * s)} ${f1(.9 * s)} ${f1(-2.2 * s)} ${f1(.9 * s)} ${f1(-.9 * s)} ${f1(2.2 * s)} ${f1(-.9 * s)} ${f1(-2.2 * s)} ${f1(-2.2 * s)} ${f1(-.9 * s)} ${f1(2.2 * s)} ${f1(-.9 * s)}z" fill="${nacht ? '#FFE27A' : '#8FC3E6'}"/>`;
}
// Stern mit Strahlen (v5, über dem Ziel)
function festStern(u, x, y, R, nacht) {
  const strahl = (a, l, b) => `<path d="M0 ${-b} L${l} 0 L0 ${b} Z" transform="rotate(${a})" fill="url(#${u}strahl2)"/>`;
  return `<g transform="translate(${f1(x)} ${f1(y)})"><circle class="halo" r="${f1(R * 2.3)}" fill="url(#${u}halo2)"/>
    ${[0, 90, 180, 270].map((a) => strahl(a, R * 2.6, R * .13)).join('')}${[45, 135, 225, 315].map((a) => strahl(a, R * 1.5, R * .09)).join('')}
    <path d="M0 ${-R} C${R * .14} ${-R * .3} ${R * .3} ${-R * .14} ${R} 0 C${R * .3} ${R * .14} ${R * .14} ${R * .3} 0 ${R} C${-R * .14} ${R * .3} ${-R * .3} ${R * .14} ${-R} 0 C${-R * .3} ${-R * .14} ${-R * .14} ${-R * .3} 0 ${-R} Z" fill="#FFE27A"/>
    <path d="M0 ${-R} C${R * .14} ${-R * .3} ${R * .3} ${-R * .14} ${R} 0 L0 0 Z M0 ${R} C${-R * .14} ${R * .3} ${-R * .3} ${R * .14} ${-R} 0 L0 0Z" fill="#F2B417"/>
    <circle r="${f1(R * .28)}" fill="#FFFDF0"/></g>`;
}
// Nordlicht: weiche, mehrfarbige Bänder + feine Vorhang-Strahlen (ein Unschärfe-Filter, einmal gerechnet)
function festNordlicht(u, W, H, s, nacht) {
  const op = nacht ? 1 : .8; const c = nacht ? ['#3DFFB0', '#2DD4E6', '#A78BFA', '#F472B6'] : ['#10B981', '#0EA5C6', '#8B5CF6', '#EC4899'];
  const band = (y, a, f, o) => `<path d="M${-20} ${f1(y * H)} C${f1(W * .2)} ${f1((y + a) * H)} ${f1(W * .38)} ${f1((y - a * .6) * H)} ${f1(W * .58)} ${f1((y + a * .4) * H)} S${f1(W * .9)} ${f1((y - a) * H)} ${W + 20} ${f1((y + a * .2) * H)} L${W + 20} ${f1((y + a * .2) * H - 26 * s)} C${f1(W * .85)} ${f1((y - a) * H - 30 * s)} ${f1(W * .6)} ${f1((y + a * .4) * H - 34 * s)} ${f1(W * .4)} ${f1((y - a * .6) * H - 24 * s)} S${f1(W * .1)} ${f1((y + a) * H - 30 * s)} -20 ${f1(y * H - 22 * s)} Z" fill="${f}" opacity="${o}"/>`;
  const strahlen = Array.from({ length: Math.round(W / (9 * s)) }, (_, i) => { const x = i * 9 * s + zz(i) * 4 * s; const l = (20 + zz(i + 40) * 26) * s; return `<rect x="${f1(x)}" y="${f1(.03 * H)}" width="${f1(1.6 * s)}" height="${f1(l)}" fill="${c[i % 2]}" opacity="${f1(.25 + zz(i + 80) * .35)}"/>`; }).join('');
  return `<g mask="url(#${u}nlm)" opacity="${op}"><g class="nordlicht" filter="url(#${u}nlb)">${band(.1, .04, c[0], .85)}${band(.075, .05, c[1], .55)}${band(.05, .03, c[2], .6)}${band(.035, .025, c[3], .3)}</g><g filter="url(#${u}nlb2)" opacity=".8">${strahlen}</g></g>`;
}

function karteSeite() {
  const breit = innerWidth >= 1000; const K = KARTEN[breit ? 1280 : 390]; const nacht = P.g === 'nacht';
  const src = BILD[(breit ? 'k1280' : 'k390') + (nacht ? 'd' : 'h')];
  const v = Number(P.v) || 4; const [fx, fy, fw, fh] = K.rahmen;
  const frei = P.frei === '1' ? Object.entries(K.frei).map(([n, [x, y, w, h]]) => `<div class="kt-frei" style="left:${x}px;top:${y}px;width:${w}px;height:${h}px">${n}</div>`).join('') : '';
  const schild = P.foto === '1' ? '' : `<div class="kt-schild">Entwurf 2 · Variante ${v} · ${['', 'dezent', 'verspielt', 'Neon-Nordlicht', 'volle Weihnacht', 'Winternacht'][v]}${P.tag !== 7 ? ' · ' + P.tag + '.12.' : ''}</div>`;
  const neu = v >= 4;
  app.innerHTML = `<div class="kd" data-g="${P.g}" style="background:${nacht ? '#0B0F14' : '#F3F1EA'};min-height:100vh"><div class="kt-buehne" style="width:${K.w}px">${schild}<img src="${src}" alt="Reisekarte, Standbild" width="${K.w}" height="${K.h}">
    <div class="kt-ebene" style="left:${fx}px;top:${fy}px;width:${fw}px;height:${fh}px;border-radius:${K.r}px" aria-hidden="true">${neu ? fest2Svg(K, v, nacht, src, 'unter') : ''}<canvas id="schnee" width="${fw * 2}" height="${fh * 2}"></canvas>${neu ? fest2Svg(K, v, nacht, src, 'ober') : festSvg(K, v, nacht)}</div>${neu ? voll2Svg(K, nacht) : ''}${frei}</div></div>`;
  if (neu) { festLauf(K, nacht, v); return; }
  if (v === 1 || P.tag === 24) schnee(document.getElementById('schnee'), K, nacht, v === 1 ? 26 : 0, false);
  if (v === 2 || P.tag === 24) schlitten(K, false);
}

// Zwei Gruppen wie in der App: 'unter' (zwischen Ländern und Routen: Tönung, Nordlicht) und 'ober' (über den Pins: alles andere).
// Im Standbild wird für 'unter' der Vordergrund (Pins, Namen, Sonne, Knöpfe) aus dem Bild wieder darübergelegt – so färbt die Tönung nichts davon ein.
function fest2Svg(K, v, nacht, src, teil) {
  const [fx, fy, W, H] = K.rahmen; const s = K.w === 390 ? 1 : 1.2; const u = 'f' + teil[0];
  const frei = (n) => { const [x, y, w, h] = K.frei[n]; return [x - fx, y - fy, w, h]; };
  if (teil === 'unter') {
    if (v !== 5) return '';
    const pins = K.alle.map(([x, y, r]) => { const px = x - fx, py = y - fy; return `<circle cx="${px}" cy="${py}" r="${f1(r * 1.22)}"/><path d="M${f1(px - r * .8)} ${f1(py + r * .5)} L${px} ${f1(py + r * 2.5)} L${f1(px + r * .8)} ${f1(py + r * .5)}Z"/><circle cx="${px}" cy="${f1(py + r * 2.45)}" r="${f1(r * .35)}"/>`; }).join('');
    const abz = K.abzeichen.map(([x, y]) => `<circle cx="${x - fx + 11 * s}" cy="${y - fy - 11 * s}" r="${8 * s}"/>`).join('');
    const namen = K.namen.map(([x, y, w, h]) => `<rect x="${x - fx - 1}" y="${y - fy - 1}" width="${w + 2}" height="${h + 2}"/>`).join('');
    const [zx, zy, zw, zh] = frei('Zoom-Knöpfe'); const [sx, sy] = [K.sonne[0] - fx, K.sonne[1] - fy];
    const vorne = `<mask id="${u}vorne" maskUnits="userSpaceOnUse" x="-10" y="-10" width="${W + 20}" height="${H + 20}"><g clip-path="url(#${u}nk)"><image href="${src}" x="${-fx}" y="${-fy}" width="${K.w}" height="${K.h}" filter="url(#${u}schrift)"/></g><g fill="#fff" filter="url(#${u}weich)">${pins}${abz}<circle cx="${sx}" cy="${sy}" r="${K.sonne[2] - 4 * s}"/>${K.knoepfe.map(([x, y, w, h]) => `<rect x="${x - fx}" y="${y - fy}" width="${w}" height="${h}" rx="11"/>`).join('')}</g></mask>`;
    return `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}"><defs><filter id="${u}weich" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="1.2"/></filter><clipPath id="${u}nk">${namen}</clipPath>
      <filter id="${u}schrift" x="0" y="0" width="100%" height="100%"><feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  ${nacht ? '.3 .59 .11 0 0' : '-.3 -.59 -.11 0 1'}"/><feComponentTransfer><feFuncA type="linear" slope="${nacht ? 3.2 : 2.4}" intercept="${nacht ? -.95 : -.55}"/></feComponentTransfer><feMorphology operator="dilate" radius=".7"/><feGaussianBlur stdDeviation=".5"/></filter><filter id="${u}nlb" x="-10%" y="-50%" width="120%" height="200%"><feGaussianBlur stdDeviation="${f1(7 * s)}"/></filter><filter id="${u}nlb2" x="-10%" y="-50%" width="120%" height="200%"><feGaussianBlur stdDeviation="${f1(1.6 * s)}"/></filter>
      <radialGradient id="${u}frost" cx=".5" cy=".55" r=".75"><stop offset=".62" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="${nacht ? '#9CC8FF' : '#FFFFFF'}" stop-opacity="${nacht ? .3 : .8}"/></radialGradient>
      <linearGradient id="${u}nlmaske" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".2" stop-color="#fff" stop-opacity=".15"/><stop offset=".42" stop-color="#fff" stop-opacity="1"/><stop offset=".9" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity=".5"/></linearGradient>
      <linearGradient id="${u}nlv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset=".55" stop-color="#fff" stop-opacity=".8"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
      <mask id="${u}nlm"><rect width="${W}" height="${H * .36}" fill="url(#${u}nlmaske)"/></mask>${vorne}</defs>
      <rect width="${W}" height="${H}" fill="${nacht ? '#3D6FD6' : '#9CC3EA'}" opacity="${nacht ? .2 : .45}" style="mix-blend-mode:${nacht ? 'screen' : 'multiply'}"/>
      <rect width="${W}" height="${H}" fill="url(#${u}frost)"/>${festNordlicht(u, W, H, s, nacht)}
      <image href="${src}" x="${-fx}" y="${-fy}" width="${K.w}" height="${K.h}" mask="url(#${u}vorne)"/></svg>`;
  }
  // ---------- ober ----------
  const o = []; const [zx, zy, zw, zh] = frei('Zoom-Knöpfe'); const so = frei('Regel-Universum-Sonne'); const [ux, uy] = [K.sonne[0] - fx, K.sonne[1] - fy];
  o.push(`<defs>${festDefs(u, nacht)}<mask id="${u}frei" maskUnits="userSpaceOnUse" x="-20" y="-20" width="${W + 40}" height="${H + 40}"><rect x="-20" y="-20" width="${W + 40}" height="${H + 40}" fill="#fff"/><rect x="${zx}" y="${zy}" width="${zw}" height="${zh}" rx="12" fill="#000"/><circle cx="${ux}" cy="${uy}" r="${K.sonne[2] + 2}" fill="#000"/></mask>
    <radialGradient id="${u}halo2"><stop offset="0" stop-color="#FFE27A" stop-opacity="${nacht ? .75 : .6}"/><stop offset=".4" stop-color="#FFD23F" stop-opacity="${nacht ? .25 : .18}"/><stop offset="1" stop-color="#FFD23F" stop-opacity="0"/></radialGradient>
    <linearGradient id="${u}strahl2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFF6CC"/><stop offset="1" stop-color="#FFD23F" stop-opacity="0"/></linearGradient>
    <linearGradient id="${u}kegelL" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE27A" stop-opacity=".55"/><stop offset="1" stop-color="#FFE27A" stop-opacity="0"/></linearGradient></defs>`);
  const g = [];
  // Freie Streifen für Eiszapfen (keine über Sonne und Zoom-Knöpfen)
  const zapfFrei = [[so[0] - 6, so[0] + so[2] + 6], [zx - 6, zx + zw + 6]];
  // Lichterkette zwischen Sonne und Zoom-Knöpfen; die Haken stecken in der Schneehaube (Haube wird danach gezeichnet)
  const anf = so[0] + so[2] + 4 * s, ende = zx - 8 * s;
  g.push(festLichterkette(u, anf, ende, 5 * s, s, nacht));
  g.push(festHaube(u, -4, W + 4, 7 * s, 8, s, nacht, 3, zapfFrei));
  g.push(festWehe(W, H, s, nacht));
  // Deko an gelandeten Ländern
  const paketF = { '#E11D48': ['#E5243B', '#FFC94A'], '#7B1E6E': ['#7B1E6E', '#FFF3D1'] };
  for (const [t, x, y, f, k = 1] of K.deko) g.push(t === 't' ? festTanne(x - fx, y - fy + 4 * s, s * .82) : festPaket(x - fx, y - fy + 3 * s, (paketF[f] || ['#0E9F6E'])[0], (paketF[f] || [, '#FFC94A'])[1], s * .78 * k));
  // Mützen: große Pins bekommen eine Mütze, kleine ein Schneehäubchen. Ein Pin, über dem dicht ein anderer steht, bekommt nur das Häubchen (kein roter Klumpen).
  // Kollision mit Beschriftung: Mütze wird kleiner, sonst Häubchen. Aktueller Pin in v5: Stern statt Mütze.
  const gross = (r) => r >= (K.w === 390 ? 12 : 15); const akt = K.pins[AKTUELL];
  const namen = K.namen.map(([x, y, w, h]) => [x - fx, y - fy, w, h]);
  const trifft = (pts) => pts.some(([px, py]) => namen.some(([x, y, w, h]) => px > x && px < x + w && py > y && py < y + h) || (px > zx - 2 && px < zx + zw + 2 && py > zy - 2 && py < zy + zh + 2));
  const huelle = (x, y, r, rot, k) => [[-14.6, -19.4], [-.6, -24.6], [7.4, -9.6], [-8, -8], [-18, -19.4], [-14.6, -23]].map(([a, b]) => { const c = Math.cos(rot * Math.PI / 180), sn = Math.sin(rot * Math.PI / 180); const q = (r / 10) * k; return [x + (a * c - b * sn) * q, y + (a * sn + b * c) * q]; });
  let mz = 0, hb = 0;
  for (const [x, y, r] of K.alle) {
    const px = x - fx, py = y - fy;
    if (!gross(r)) { g.push(festHaeubchen(px, py, r, nacht)); hb++; continue; }
    if (v === 5 && Math.abs(x - akt[0]) < 4 && Math.abs(y - akt[1]) < 4) continue;
    const bedraengt = K.alle.some(([x2, y2, r2]) => (x2 !== x || y2 !== y) && Math.abs(x2 - x) < r * 1.7 && y - y2 > 0 && y - y2 < r * 2.9);
    if (bedraengt) { g.push(festHaeubchen(px, py, r, nacht)); hb++; continue; }
    const abz = K.abzeichen.some(([ax, ay]) => Math.abs(ax - x) < 3 && Math.abs(ay - y) < 3);
    let rot = abz ? -24 - zz(x) * 8 : -6 - zz(x + y) * 18; let k = 1.04, ok = false;
    for (const kk of [1.04, .92, .8]) { if (!trifft(huelle(px, py, r, rot, kk))) { k = kk; ok = true; break; } if (!trifft(huelle(px, py, r, rot - 10, kk))) { k = kk; rot -= 10; ok = true; break; } }
    if (!ok) { g.push(festHaeubchen(px, py, r, nacht)); hb++; continue; }
    g.push(festMuetze(u, px, py, r, rot, k, nacht)); mz++;
  }
  g.push(`<!-- Mützen ${mz}, Häubchen ${hb} -->`);
  // v5: Stern mit Strahlen über dem Ziel, weicher Lichtkegel bis zum Pin
  if (v === 5) { const [x0, y0] = [akt[0] - fx, akt[1] - fy]; const R = 11 * s; const sy = y0 - K.kopfR - 24 * s;
    g.push(`<path d="M${f1(x0 - 5 * s)} ${f1(sy + 6 * s)} L${f1(x0 - K.kopfR * .7)} ${f1(y0 - K.kopfR * .4)} L${f1(x0 + K.kopfR * .7)} ${f1(y0 - K.kopfR * .4)} L${f1(x0 + 5 * s)} ${f1(sy + 6 * s)} Z" fill="url(#${u}kegelL)"/>`, festStern(u, x0, sy, R, nacht)); }
  // Tages-Sonderfälle
  if (P.tag === 6) g.push(festStiefel(akt[0] - fx - K.kopfR - 20 * s, akt[1] - fy + 18 * s, s));
  if (P.tag === 31) g.push(festFeuerwerk(akt[0] - fx, akt[1] - fy, s));
  // Schlitten: Flugbahn entlang der Route bzw. am 24.12. groß quer über die Karte
  const [a, b, c] = K.route.map(([x, y]) => [x - fx, y - fy]);
  if (P.tag === 24) { const d = `M${f1(-70 * s)} ${f1(H * .64)} C${f1(W * .25)} ${f1(H * .2)} ${f1(W * .7)} ${f1(H * .12)} ${f1(W + 80 * s)} ${f1(H * .36)}`;
    g.push(`<path id="weltbahn" d="${d}" fill="none" stroke="none"/><path d="${d}" fill="none" stroke="#FFD23F" stroke-width="${f1(2.2 * s)}" stroke-dasharray="${f1(.1 * s)} ${f1(9 * s)}" stroke-linecap="round" opacity=".95"/><path d="${d}" fill="none" stroke="#FFF3D1" stroke-width="${f1(1.2 * s)}" stroke-dasharray="${f1(.1 * s)} ${f1(23 * s)}" stroke-dashoffset="${f1(5 * s)}" stroke-linecap="round"/>`); }
  else g.push(`<path id="sroute" d="M${a[0]} ${a[1]} Q${b[0]} ${b[1]} ${c[0]} ${c[1]}" fill="none" stroke="none"/>`);
  g.push(`<g id="schlitten">${festSchlitten(nacht, (P.tag === 24 ? 1.9 : 1.15) * s)}</g>`);
  o.push(`<g mask="url(#${u}frei)">${g.join('')}</g>`);
  return `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}">${o.join('')}</svg>`;
}
// 6.12.: Nikolaus-Stiefel mit Goldtalern und Zuckerstange
function festStiefel(x, y, s) {
  return `<g transform="translate(${f1(x)} ${f1(y)}) scale(${s})"><ellipse cx="6" cy="1" rx="12" ry="2" fill="#000" opacity=".15"/>
    <path d="M2.2 -14 C1 -20 2 -24 3.4 -27 L4.6 -26 C3.6 -23 3 -20 4 -14Z" fill="#fff"/><path d="M2.2 -27 C2 -30 5.6 -31 6 -28" stroke="#E5243B" stroke-width="2" fill="none" stroke-linecap="round"/>
    ${[[5, -19, '#FFC94A'], [9.6, -18, '#FFD86B'], [7.4, -21.6, '#F2B417']].map(([cx, cy, f]) => `<ellipse cx="${cx}" cy="${cy}" rx="3" ry="2.6" fill="${f}"/><ellipse cx="${cx}" cy="${cy}" rx="1.8" ry="1.5" fill="none" stroke="#C98A0A" stroke-width=".5"/><path d="M${cx - 1.6} ${cy - 1.2} q1 -1 2 -.6" stroke="#FFF6CC" stroke-width=".6" fill="none"/>`).join('')}
    <path d="M0 -14 H13 V-4 L19.6 -2.6 C23 -1.8 23.4 1.6 20 1.6 H0Z" fill="#E5243B"/><path d="M13 -14 V-4 L19.6 -2.6 C23 -1.8 23.4 1.6 20 1.6 H11 C14 1 15 -1 10 -4 V-14Z" fill="#B3122B"/>
    <path d="M1 -12.5 V-2" stroke="#FF8A95" stroke-width="1" stroke-linecap="round" opacity=".8"/>
    <rect x="-1.4" y="-17.2" width="16" height="4.6" rx="2.3" fill="#fff"/><path d="M0 -13.4 H13.4" stroke="#C7D3E3" stroke-width="1" stroke-linecap="round"/></g>`;
}
// 31.12.: drei Feuerwerks-Bouquets neben dem Ziel (verjüngte Strahlen, heller Kern, fallende Funken)
function festFeuerwerk(x, y, s) {
  const b = [[x - 50 * s, y - 14 * s, ['#FFC94A', '#FFF3D1'], 15], [x - 80 * s, y + 20 * s, ['#FF5A5F', '#FFD0D2'], 12], [x - 40 * s, y + 34 * s, ['#3DDC84', '#D7FBE7'], 11]];
  return b.map(([bx, by, [f, h], r], i) => `<g class="feuerwerk f${i}" transform="translate(${f1(bx)} ${f1(by)}) scale(${s})"><circle r="${r * .5}" fill="${h}" opacity=".35"/>
    ${Array.from({ length: 14 }, (_, j) => { const a = j / 14 * 360 + i * 9; const l = r * (j % 2 ? .78 : 1); return `<path d="M0 -.7 L${l} 0 L0 .7Z" transform="rotate(${a}) translate(${r * .22} 0)" fill="${f}"/><circle cx="${f1(Math.cos(a * Math.PI / 180) * (l + r * .38))}" cy="${f1(Math.sin(a * Math.PI / 180) * (l + r * .38))}" r=".9" fill="${h}"/>`; }).join('')}
    <circle r="2" fill="#fff"/>${[[-3, r + 4], [4, r + 7], [-6, r + 10]].map(([fx2, fy2], q) => `<circle cx="${fx2}" cy="${fy2}" r="${.8 - q * .15}" fill="${f}" opacity="${.8 - q * .2}"/>`).join('')}</g>`).join('');
}
// Zweite Ebene über dem ganzen Bild: Schneehaube auf „Gerade dran“, Mütze am Jugendwort-Schild (in der App: CSS/SVG am Element selbst, pointer-events: none)
function voll2Svg(K, nacht) {
  const s = K.w === 390 ? 1 : 1.2; const [x, y, w] = (nacht && K.karteNacht) || K.karte; const [sx, sy] = nacht ? K.schildNacht : K.schild; const u = 'fv';
  return `<svg class="kt-voll" viewBox="0 0 ${K.w} ${K.h}" width="${K.w}" height="${K.h}" style="position:absolute;inset:0;pointer-events:none;overflow:visible" aria-hidden="true"><defs>${festDefs(u, nacht)}
    </defs>
    ${festHaube(u, x + 2, x + w - 4, y + 1.5 * s, 5, s, nacht, 17, [], 5)}
    ${festMuetze(u, sx + 4 * s, sy + 15 * s, 8.6 * s, -18, 1, nacht)}</svg>`;
}
// Eine gemeinsame Schleife für Schnee (Canvas) und Schlitten. Bei „Bewegung reduzieren“: kein Schnee, kein Schlitten.
function festLauf(K, nacht, v) {
  const c = document.getElementById('schnee'); const ctx = c.getContext('2d'); const W = c.width, H = c.height; const s = (K.w === 390 ? 1 : 1.2) * 2;
  let sd = 11; const zf = () => (sd = (sd * 16807) % 2147483647) / 2147483647;
  // drei Tiefen: hinten viele kleine, Mitte, vorn wenige große unscharfe
  const sprite = (r, weich, rand) => { const q = document.createElement('canvas'); const d = Math.ceil(r * 2 + 6); q.width = q.height = d; const x = q.getContext('2d'); const m = d / 2;
    const gr = x.createRadialGradient(m, m, 0, m, m, r + (weich ? 2 : .6)); gr.addColorStop(0, 'rgba(255,255,255,1)'); gr.addColorStop(weich ? .25 : .7, 'rgba(255,255,255,.95)'); gr.addColorStop(1, 'rgba(255,255,255,0)');
    if (rand && !nacht) { x.beginPath(); x.arc(m, m + .6, r + .3, 0, 7); x.fillStyle = weich ? 'rgba(70,110,150,.18)' : 'rgba(70,110,150,.42)'; x.fill(); }
    x.fillStyle = gr; x.beginPath(); x.arc(m, m, r + (weich ? 2 : .6), 0, 7); x.fill(); return q; };
  const L = [{ n: K.w === 390 ? 34 : 70, r: [.9, 1.5], v: [.22, .38], a: nacht ? .7 : .85, weich: false }, { n: K.w === 390 ? 15 : 30, r: [1.9, 2.6], v: [.5, .7], a: .95, weich: false }, { n: K.w === 390 ? 5 : 9, r: [4.2, 6], v: [1, 1.3], a: nacht ? .6 : .75, weich: true }];
  const fl = []; L.forEach((l, li) => { for (let i = 0; i < l.n; i++) { const r = (l.r[0] + zf() * (l.r[1] - l.r[0])) * s; fl.push({ x: zf() * W, y: zf() * H, r, v: (l.v[0] + zf() * (l.v[1] - l.v[0])) * s * .5, p: zf() * 6, a: l.a, sp: sprite(r, l.weich, true), li }); } });
  const fz = ['Regel-Universum-Sonne', 'Zoom-Knöpfe', 'Quelle'].map((n) => K.frei[n]).map(([x, y, w, h]) => [(x - K.rahmen[0]) * 2, (y - K.rahmen[1]) * 2, w * 2, h * 2]);
  const male = () => { ctx.clearRect(0, 0, W, H); for (const p of fl) { if (fz.some(([x, y, w, h]) => p.x > x - 6 && p.x < x + w + 6 && p.y > y - 6 && p.y < y + h + 6)) continue; ctx.globalAlpha = p.a; ctx.drawImage(p.sp, p.x - p.sp.width / 2, p.y - p.sp.height / 2); } ctx.globalAlpha = 1; };
  const g = document.getElementById('schlitten'); const pfad = document.getElementById(P.tag === 24 ? 'weltbahn' : 'sroute');
  const PL = pfad ? pfad.getTotalLength() : 0;
  const setze = (t) => { const p = pfad.getPointAtLength(PL * t), q = pfad.getPointAtLength(Math.min(PL, PL * t + 2)); let r = Math.atan2(q.y - p.y, q.x - p.x) * 180 / Math.PI; const flip = q.x < p.x; if (flip) r += 180; if (r > 180) r -= 360; r = Math.max(-16, Math.min(16, r)); g.setAttribute('transform', `translate(${f1(p.x)} ${f1(p.y - 8)}) rotate(${f1(r)})${flip ? ' scale(-1 1)' : ''}`); };
  const ruhig = wenigBewegung() && P.foto !== '1';
  if (ruhig) { if (g) g.style.display = 'none'; return; } // Bewegung reduzieren: alles still, kein Schnee, kein Schlitten
  male(); if (g && pfad) setze(P.tag === 24 ? .5 : (K.still || .5));
  if (P.foto === '1') return;
  const dauer = P.tag === 24 ? 7000 : 6000, pause = P.tag === 24 ? 1e9 : 8000; const t0 = performance.now() - (dauer + pause) + 600; let id;
  const lauf = (t) => { if (document.hidden) { id = requestAnimationFrame(lauf); return; }
    for (const p of fl) { p.y += p.v; p.x += Math.sin((p.y / s + p.p * 40) / 40) * .18 * (p.li + 1); if (p.y > H + 12) { p.y = -12; p.x = zf() * W; } } male();
    if (g && pfad) { const x = (t - t0) % (dauer + pause); if (P.tag === 24 && t - t0 > dauer + pause) g.style.display = 'none'; else if (x > dauer) g.style.display = 'none'; else { g.style.display = ''; setze(x / dauer); } }
    id = requestAnimationFrame(lauf); };
  id = requestAnimationFrame(lauf); kartenLauf.push(() => cancelAnimationFrame(id));
}
