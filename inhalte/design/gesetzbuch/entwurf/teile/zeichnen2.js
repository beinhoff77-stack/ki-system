// Zeichnungen, zweite Runde: die übrigen Rechenregeln, die fünf Ideen der Geometrie, Rechenregel 2 und „Haut des Körpers“ neu.
// Was zu sehen ist, Maße und Beschriftung: Zeichen-Vorgaben des Mathe-Profis (sonne.md, planet-geometrie.md, planet-flaeche-und-raum.md).
// Drei Markierungen, jede auch ohne Farbe erkennbar: Gelb mit Rahmen in Tinte · Blau mit blauem Rahmen · Schraffur.
const BL = (s) => `<b class="bl">${s}</b>`, SCH = (s) => `<b class="sf">${s}</b>`;
const zMarkeB = (x, y, s, o = {}) => { const b = o.breit || Math.max(30, String(s).length * 10 + 14); return `<rect x="${x - b / 2}" y="${y - 15}" width="${b}" height="30" rx="8" fill="${ZF.blauFl}" stroke="${ZF.blau}" stroke-width="2"/>${zT(x, y + 5.5, s, { w: 700, g: o.g || 16 })}`; };
const zBruchT = (x, y, z, n, g = 17, o = {}) => zT(x, y - 4, z, { g, w: 700, ...o }) + zL(x - g * 0.42 * Math.max(String(z).length, String(n).length) - 2, y + 1, x + g * 0.42 * Math.max(String(z).length, String(n).length) + 2, y + 1, { b: 2 }) + zT(x, y + g + 1, n, { g, w: 700, ...o });
const zKasten = (x, y, b, h, o = {}) => `<rect x="${x}" y="${y}" width="${b}" height="${h}" rx="${o.rx ?? 6}" fill="${o.fl || ZF.papier}" stroke="${o.f || ZF.tinte}" stroke-width="${o.b || 2.5}"${o.strich ? ` stroke-dasharray="${o.strich}"` : ''}/>`;
// Strich-Zeichen für „gleich lang“: n kurze Querstriche in der Mitte der Strecke, auf einem gelben Punkt
function zStrich(x1, y1, x2, y2, n = 1) { const mx = (x1 + x2) / 2, my = (y1 + y2) / 2, l = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / l, uy = (y2 - y1) / l; let s = `<circle cx="${mx}" cy="${my}" r="${7 + n}" fill="${ZF.gelb}"/>`;
  for (let i = 0; i < n; i++) { const d = (i - (n - 1) / 2) * 4.5; s += zL(mx + ux * d - uy * 6, my + uy * d + ux * 6, mx + ux * d + uy * 6, my + uy * d - ux * 6, { b: 2 }); } return s; }
const zGleich = (x1, y1, x2, y2, n = 1) => zL(x1, y1, x2, y2, { f: ZF.gelb, b: 7 }) + zL(x1, y1, x2, y2, { b: 2.25 }) + zStrich(x1, y1, x2, y2, n);
// rechter Winkel an (x, y) zwischen den Richtungen u und v (Einheitsvektoren)
const zRWd = (x, y, ux, uy, vx, vy, s = 9) => zPfad(`M${x + ux * s} ${y + uy * s}L${x + (ux + vx) * s} ${y + (uy + vy) * s}L${x + vx * s} ${y + vy * s}`, { b: 1.5 }) + `<circle cx="${x + (ux + vx) * s * 0.5}" cy="${y + (uy + vy) * s * 0.5}" r="1.3" fill="${ZF.tinte}"/>`;
// Winkelfeld: Mittelpunkt, Radius, von Winkel a1 bis a2 in Grad (gegen den Uhrzeigersinn, 0° = nach rechts)
function zWinkel(cx, cy, r, a1, a2, o = {}) { const p = (a) => [cx + r * Math.cos(a * Math.PI / 180), cy - r * Math.sin(a * Math.PI / 180)], [x1, y1] = p(a1), [x2, y2] = p(a2);
  return zPfad(`M${cx} ${cy}L${x1} ${y1}A${r} ${r} 0 0 0 ${x2} ${y2}Z`, { fl: o.fl || 'none', b: o.b || 1.75, f: o.f || ZF.tinte }) + (o.s ? zT(...p((a1 + a2) / 2).map((v, i) => (i ? cy + (v - cy) * (o.ab || 1.55) + 5 : cx + (v - cx) * (o.ab || 1.55))), o.s, { g: 16, w: 800 }) : ''); }
const zDach = (x, y, w, o = {}) => zPfad(`M${x - 5} ${y - 5}L${x + 4} ${y}L${x - 5} ${y + 5}`, { b: 2, f: o.f || ZF.tinte }).replace('<path', `<path transform="rotate(${w} ${x} ${y})"`);

// ---------- Rechenregel 1 · Stellenwert ----------
function zStellen() {
  const b = 40, x0 = 14, yk = 22, y1 = 44, h = 46, sp = ['H', 'Z', 'E', 'z', 'h'], X = (i) => x0 + i * b + b / 2; let s = '';
  s += zKasten(x0, y1, 5 * b, 2 * h, { rx: 0, b: 2 }) + zL(x0, y1 + h, x0 + 5 * b, y1 + h, { b: 1.25, f: ZF.leise });
  for (let i = 1; i < 5; i++) if (i !== 3) s += zL(x0 + i * b, y1, x0 + i * b, y1 + 2 * h, { b: 1.25, f: ZF.leise });
  s += zL(x0 + 3 * b, yk - 14, x0 + 3 * b, y1 + 2 * h + 18, { b: 4 }) + zT(x0 + 3 * b, y1 + 2 * h + 34, 'Komma', { g: 14, grotesk: true, w: 700 });
  sp.forEach((k, i) => { s += zT(X(i), yk + 9, k, { g: 16, w: 700, f: ZF.leise }); });
  const zi = (i, r, t) => zT(X(i), y1 + r * h + h / 2 + 8, t, { g: 24, w: 800 });
  s += zi(2, 0, '2') + zi(3, 0, '5') + zi(1, 1, '2') + zi(2, 1, '5');
  for (const i of [2, 3]) { const a = [X(i) - 9, y1 + h / 2 + 13], e = [X(i - 1) + 10, y1 + h + h / 2 - 12]; s += zPfeil(...a, ...e, { f: ZF.gelb, b: 8, kopf: 13 }) + zPfeil(...a, ...e, { b: 2.25, kopf: 9 }); }
  s += zT(x0 + 5 * b + 12, y1 + h / 2 + 6, '2,5', { g: 17, a: 'start', w: 700 }) + zT(x0 + 5 * b + 12, y1 + h + h / 2 + 6, '· 10 = 25', { g: 17, a: 'start', w: 700 });
  return { name: 'Stellenwert', felder: [{ svg: zBlatt(320, 178, s, 'Stellenwerttafel mit den Spalten H, Z, E, Komma, z, h. Oben 2,5, unten 25: jede Ziffer rückt eine Spalte nach links, das Komma bleibt stehen'), gl: '2,5 · 10 = 25', satz: 'Das Komma bleibt stehen. Beide Ziffern rücken gleich weit: eine Spalte nach links.' }] };
}

// ---------- Rechenregel 2 · Minus heißt umdrehen: Figur am Start, je Minus eine Kehrtwende ----------
function zUmdrehen() {
  const X = (v) => 40 + (v + 1) * 34;
  const wende = (x, y) => `<rect x="${x - 13}" y="${y - 15}" width="26" height="26" rx="7" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.5"/>` + zPfad(`M${x + 6} ${y + 6}V${y - 3}a6 6 0 0 0 -12 0V${y + 3}`, { b: 2.25, f: '#11161D' }) + `<polygon points="${x - 6},${y + 8} ${x - 10.5},${y + 1} ${x - 1.5},${y + 1}" fill="#11161D"/>`;
  const gerade = (ya, ziel, teile, wort, n) => { let s = zL(22, ya, 290, ya, { b: 2 }) + zP([[300, ya], [289, ya - 5], [289, ya + 5]], { fl: ZF.tinte, b: 1 });
    for (let v = -1; v <= 6; v++) s += zL(X(v), ya - 6, X(v), ya + 6, { b: v === 0 ? 3 : 1.75 }) + zT(X(v), ya + 24, v < 0 ? '−' + (-v) : v, { g: 15, w: v === 0 || v === 3 || v === ziel ? 800 : 600, f: v === 0 || v === 3 || v === ziel ? ZF.tinte : ZF.leise });
    s += zBogenPfeil(X(3), ya - 40, X(ziel), ya - 10, 44, { f: ZF.gelb, b: 9 }) + zBogenPfeil(X(3), ya - 40, X(ziel), ya - 10, 44, { b: 2.5 });
    s += `<circle cx="${X(3)}" cy="${ya}" r="6" fill="${ZF.tinte}"/><circle cx="${X(ziel)}" cy="${ya}" r="7" fill="${ZF.papier}" stroke="${ZF.tinte}" stroke-width="2.5"/>`;
    s += zL(X(3), ya - 8, X(3), ya - 24, { b: 3 }) + `<circle cx="${X(3)}" cy="${ya - 30}" r="6" fill="${ZF.papier}" stroke="${ZF.tinte}" stroke-width="2.5"/>` + zPfad(`M${X(3) + 6} ${ya - 30}h7`, { b: 2 }) + `<circle cx="${X(3) + 2.5}" cy="${ya - 31}" r="1.3" fill="${ZF.tinte}"/>`;
    const bw = n * 30, tx = 160 - (bw + 8 + wort.length * 8.2) / 2; for (let i = 0; i < n; i++) s += wende(tx + 13 + i * 30, ya - 70);
    return s + zGl(160, ya - 100, teile) + zT(tx + bw + 8, ya - 64, wort, { g: 15, a: 'start', grotesk: true, w: 700 }); };
  const oben = gerade(130, 1, ['3 + (', ['−'], '2) = 1'], 'einmal umdrehen', 1), unten = gerade(296, 5, ['3 ', ['−'], ' (', ['−'], '2) = 5'], 'zweimal umdrehen', 2);
  return { name: 'Plus und Minus mit negativen Zahlen', felder: [
    { svg: zBlatt(320, 330, oben + zL(X(3), 158, X(3), 180, { f: ZF.leise, b: 1.5, strich: '3 4' }) + unten, 'Zwei Zahlengeraden von minus 1 bis 6 untereinander. Am Start bei 3 steht eine Figur mit Blick nach rechts. Oben ein Minus, eine Kehrtwende: Pfeil zwei Einheiten nach links zur 1. Unten zwei Minus, zwei Kehrtwenden: Pfeil zwei Einheiten nach rechts zur 5'),
      mini: zBlatt(320, 164, oben, 'Zahlengerade: Figur bei 3, eine Kehrtwende, Pfeil zwei Einheiten nach links zur 1'), gl: '', satz: 'Die Figur steht bei 3 und schaut nach rechts. Jedes Minus ist eine Kehrtwende. Einmal umgedreht geht sie nach links, zweimal umgedreht wieder nach rechts. Beide Pfeile sind genau zwei Einheiten lang.' },
  ] };
}

// ---------- Rechenregel 3 · Treppe: der erste Faktor zählt herunter, jede Stufe geht 2 hoch ----------
function zTreppe() {
  const bw = 58, x0 = 16, y0 = 66, e = 13, werte = [-6, -4, -2, 0, 2], fak = ['3', '2', '1', '0', '(−1)'], Y = (v) => y0 - v * e, grund = Y(-6) + 30; let s = '';
  werte.forEach((v, i) => { s += `<rect x="${x0 + i * bw}" y="${Y(v)}" width="${bw}" height="${grund - Y(v)}" fill="${i === 4 ? ZF.gelb : ZF.blauFl}"/>`; });
  let d = `M${x0} ${grund}V${Y(-6)}`; werte.forEach((v, i) => { d += `H${x0 + (i + 1) * bw}` + (i < 4 ? `V${Y(werte[i + 1])}` : `V${grund}`); }); s += zPfad(d + 'Z');
  s += zL(6, y0, 314, y0, { b: 3 }) + zT(8, y0 - 8, 'Null-Linie', { g: 14, a: 'start', grotesk: true, w: 700 }) + `<rect x="${x0 + 4 * bw}" y="${Y(2)}" width="${bw}" height="${grund - Y(2)}" fill="none" stroke="${ZF.tinte}" stroke-width="4"/>`;
  werte.forEach((v, i) => { const x = x0 + i * bw + bw / 2; s += zT(x, Y(v) + (i === 4 ? -8 : 21), v > 0 ? '+2' : v < 0 ? '−' + (-v) : '0', { g: 18, w: 800, f: i === 4 ? ZF.tinte : ZF.tinte });
    if (i) s += zPfeil(x0 + i * bw - 9, Y(werte[i - 1]) - 3, x0 + i * bw - 9, Y(v) + 3, { b: 2, kopf: 8 }) + zT(x0 + i * bw - 17, Y(v) + e + 5, '+2', { g: 14, w: 700, a: 'end' });
    s += zT(x, grund + 22, fak[i], { g: 17, w: 800 }) + zT(x, grund + 42, '· (−2)', { g: 14 }); });
  return { name: 'Vorzeichen bei Mal und Geteilt', felder: [{ svg: zBlatt(320, 238, s, 'Treppe mit fünf gleich hohen Stufen, die nach rechts ansteigt: minus 6, minus 4, minus 2, 0, plus 2. Darunter die Rechnungen 3 mal minus 2 bis minus 1 mal minus 2. Die letzte Stufe liegt über der Null-Linie'), gl: W('(−1) · (−2) = +2'), satz: 'Der erste Faktor zählt herunter: 3, 2, 1, 0, −1. Jede Stufe geht 2 nach oben. Deshalb landet die letzte Stufe über der Null.' }] };
}

// ---------- Rechenregel 4 · Reihenfolge: vier Stufen von oben nach unten ----------
function zReihenfolge() {
  const st = ['Klammer', 'Hoch', 'Punkt  · :', 'Strich  + −'], b = 118, h = 36; let s = '';
  st.forEach((t, i) => { const x = 8 + i * 22, y = 14 + i * h; s += zKasten(x, y, b, h, { rx: 4, fl: i === 2 ? ZF.gelb : ZF.blauFl, b: i === 2 ? 3 : 2 }) + zT(x + 10, y + 24, `${i + 1}`, { g: 15, a: 'start', w: 800, f: i === 2 ? '#11161D' : ZF.leise }) + zT(x + 26, y + 24, t, { g: 15, a: 'start', grotesk: true, w: 700, f: i === 2 ? '#11161D' : ZF.tinte }); });
  s += zT(160, 14 + 4 * h + 26, 'Punkt und Strich: jeweils von links nach rechts', { g: 14, grotesk: true, w: 600, f: ZF.leise });
  const rx = 256; s += zGl(rx, 52, ['2 + ', ['3 · 4']], 16) + zT(rx, 92, '2 + 12', { g: 16, w: 700 }) + zT(rx, 132, '14', { g: 18, w: 800 }) + zPfeil(rx, 60, rx, 74, { b: 1.75, kopf: 7 }) + zPfeil(rx, 100, rx, 114, { b: 1.75, kopf: 7 });
  return { name: 'Reihenfolge beim Rechnen', felder: [{ svg: zBlatt(320, 196, s, 'Vier Stufen von oben nach unten: Klammer, Hoch, Punkt mit Mal und Geteilt, Strich mit Plus und Minus. Rechts die Rechnung 2 plus 3 mal 4: zuerst wird 3 mal 4 eingerahmt, dann 2 plus 12, dann 14'), gl: `2 + ${W('3 · 4')} = 2 + 12 = 14`, satz: 'Die oberste Stufe kommt zuerst. Eingerahmt ist, was zuerst gerechnet wird: hier der Punkt vor dem Strich.' }] };
}

// ---------- Rechenregel 5 · Tauschen, Klammern, Zusammenfassen: Kärtchen mit festem Zeichen ----------
function zKaertchen() {
  const karte = (x, y, z, t, o = {}) => zKasten(x, y, 62, 34, { fl: ZF.papier }) + (z ? `<rect x="${x + 6}" y="${y + 6}" width="20" height="22" rx="5" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.5"/>` + zT(x + 16, y + 23, z, { g: 16, w: 800, f: '#11161D' }) : '') + zT(z ? x + 42 : x + 31, y + 23, t, { g: 16, w: 700 });
  let a = karte(40, 16, '', '25') + karte(129, 16, '·', '37') + karte(218, 16, '·', '4') + karte(40, 96, '', '25') + karte(129, 96, '·', '4') + karte(218, 96, '·', '37');
  a += zPfeil(160, 54, 244, 90, { b: 1.75, f: ZF.leise, kopf: 8 }) + zPfeil(249, 54, 165, 90, { b: 1.75, f: ZF.leise, kopf: 8 }) + zPfeil(71, 54, 71, 90, { b: 1.75, f: ZF.leise, kopf: 8 });
  a += zKlammer(40, 191, 136, '100', true, 17);
  const korb = (x, b) => zPfad(`M${x} 70L${x + 12} 150H${x + b - 12}L${x + b} 70`, { fl: ZF.blauFl }) + zL(x - 6, 70, x + b + 6, 70, { b: 3 });
  let k = korb(22, 164) + korb(212, 88) + karte(36, 84, '+', '3a') + karte(108, 100, '+', '4a') + karte(225, 92, '+', '2b');
  k += zT(104, 176, '7a', { g: 18, w: 800 }) + zT(256, 176, '2b', { g: 18, w: 800 }) + zT(104, 30, 'Korb für a', { g: 15, grotesk: true, w: 700 }) + zT(256, 30, 'Korb für b', { g: 15, grotesk: true, w: 700 }) + zPfeil(104, 38, 104, 62, { b: 1.75, kopf: 8 }) + zPfeil(256, 38, 256, 62, { b: 1.75, kopf: 8 });
  return { name: 'Tauschen, Klammern, Zusammenfassen', felder: [
    { svg: zBlatt(320, 176, a, 'Drei Kärtchen 25, mal 37, mal 4. Darunter umgestellt: 25, mal 4, mal 37; die ersten zwei sind mit einer Klammer zusammengefasst zu 100'), kopf: 'Tauschen und klammern', gl: '25 · 37 · 4 = 25 · 4 · 37 = 3 700', satz: 'Jedes Kärtchen trägt sein Zeichen vorn. Beim Tauschen wandert das Zeichen mit.' },
    { svg: zBlatt(320, 190, k, 'Zwei Körbe: im linken liegen die Kärtchen plus 3a und plus 4a, zusammen 7a; im rechten das Kärtchen plus 2b'), kopf: 'Zusammenfassen', gl: '3a + 2b + 4a = 7a + 2b', satz: 'Nur Gleiches kommt in denselben Korb: a zu a, b zu b.', pfeil: 'mit Buchstaben' },
  ] };
}

// ---------- Rechenregel 7 · Minus vor der Klammer: Kassenzettel und Rechnung ----------
function zZettel() {
  let z = zPfad('M70 12H250V168l-15 10l-15 -10l-15 10l-15 -10l-15 10l-15 -10l-15 10l-15 -10l-15 10l-15 -10l-15 10l-15 -10Z', { fl: ZF.papier, b: 2 });
  const zeile = (y, a, b, o = {}) => zT(o.ein ? 104 : 84, y, a, { g: 15, a: 'start', grotesk: true, w: o.fett ? 700 : 500 }) + (o.m ? (o.m === 'b' ? zMarkeB : zMarke)(210, y - 5, b, { breit: 62, g: 15 }) : zT(236, y, b, { g: 15, a: 'end', w: 700 }));
  z += zeile(42, 'Guthaben', '20 €', { fett: 1 }) + zeile(78, 'Einkauf', '8 €', { ein: 1, m: 'g' }) + zeile(114, 'Rabatt', '−3 €', { ein: 1, m: 'b' }) + zL(84, 130, 236, 130, { b: 1.5, f: ZF.leise }) + zeile(154, 'bleibt', '15 €', { fett: 1 });
  z += zPfad('M98 60h-10v64h10', { b: 2.5 }) + zT(34, 97, '20 −', { g: 16, w: 800 });
  const g = 21, bw = g * 0.8, xa = 160 - 6 * bw, X = (i) => xa + i * bw + bw / 2, r1 = '20 − (8 − 3)', r2 = '20 −  8 + 3 '; let r = '';
  const mark = (i, j, y, blau) => `<rect x="${X(i) - bw / 2 + 1.5}" y="${y - g + 1}" width="${(j - i + 1) * bw - 3}" height="${g + 8}" rx="6" fill="${blau ? ZF.blauFl : ZF.gelb}" stroke="${blau ? ZF.blau : ZF.tinte}" stroke-width="${blau ? 2 : 1.5}"/>`;
  r += mark(6, 6, 50) + mark(8, 10, 50, 1) + mark(3, 6, 120) + mark(8, 10, 120, 1);
  [...r1].forEach((c, i) => { r += zT(X(i), 50, c, { g, w: 700, f: i === 6 ? '#11161D' : ZF.tinte }); }); [...r2].forEach((c, i) => { r += zT(X(i), 120, c, { g, w: 700, f: i >= 3 && i <= 6 ? '#11161D' : ZF.tinte }); });
  r += zPfeil(X(6), 62, X(6), 94, { b: 1.75, kopf: 8 }) + zPfeil(X(9), 62, X(9), 94, { b: 1.75, kopf: 8, f: ZF.blau }) + zT(160, 166, '= 15', { g, w: 800 });
  return { name: 'Minus vor der Klammer', felder: [
    { svg: zBlatt(320, 190, z, 'Kassenzettel: Guthaben 20 Euro. Davon geht eine Klammer ab: Einkauf 8 Euro und Rabatt minus 3 Euro. Es bleiben 15 Euro'), kopf: 'Der Kassenzettel', gl: `20 − (${W('8')} ${BL('− 3')}) = 15`, satz: 'Vom Guthaben geht der Einkauf ab, der Rabatt kommt wieder dazu.' },
    { svg: zBlatt(320, 184, r, 'Zwei Rechenzeilen untereinander: 20 minus Klammer 8 minus 3, darunter 20 minus 8 plus 3. Minus 8 steht unter 8, plus 3 unter minus 3. Ergebnis 15'), kopf: 'Als Rechnung', gl: `20 − (${W('8')} ${BL('− 3')}) = 20 ${W('− 8')} ${BL('+ 3')}`, satz: 'Beide Zeichen drehen sich um: Aus 8 wird − 8, aus − 3 wird + 3.', pfeil: 'Klammer auflösen' },
  ] };
}

// ---------- Rechenregel 8 · Potenzen: fünf Zweien, darunter die Reihe der Hochzahlen ----------
function zPotenz() {
  const X = (i) => 46 + i * 54, y = 52, g = 22; let s = `<rect x="22" y="${y - 27}" width="152" height="40" rx="9" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.75"/>`;
  for (let i = 0; i < 5; i++) s += zT(X(i), y, '2', { g, w: 800, f: i < 3 ? '#11161D' : ZF.tinte }) + (i < 4 && i !== 2 ? zT(X(i) + 27, y, '·', { g, w: 800, f: i < 2 ? '#11161D' : ZF.tinte }) : '');
  s += zT(31, y, '(', { g: 19, w: 600, f: '#11161D' }) + zT(X(2) + 15, y, ')', { g: 19, w: 600, f: '#11161D' }) + zT(X(2) + 28, y, '·', { g: 19, w: 800 }) + zT(X(2) + 40, y, '(', { g: 19, w: 600 }) + zT(X(4) + 15, y, ')', { g: 19, w: 600 });
  s += zPfad(`M26 74v7H176v-7`, { f: ZF.leise, b: 1.75 }) + zMarke(101, 100, '2³', { breit: 44, g: 18 }) + zPfad(`M198 74v7H282v-7`, { f: ZF.leise, b: 1.75 }) + zSchild(240, 106, '2²', { g: 18, w: 700 });
  s += zPfad(`M26 126v7H282v-7`, { f: ZF.leise, b: 1.75 }) + zSchild(154, 158, '2⁵', { g: 18, w: 700 });
  const b = 48, x0 = 16, yr = 46, werte = ['8', '4', '2', '1', '½', '¼'], hoch = ['2³', '2²', '2¹', '2⁰', '2⁻¹', '2⁻²']; let r = '';
  werte.forEach((w, i) => { r += zKasten(x0 + i * b, yr, b, 44, { rx: 0, b: i === 3 ? 3.5 : 2, fl: i === 3 ? ZF.blauFl : ZF.papier, f: i === 3 ? ZF.blau : ZF.tinte }) + zT(x0 + i * b + b / 2, yr + 30, w, { g: i > 3 ? 24 : 20, w: 800 }) + zT(x0 + i * b + b / 2, yr - 12, hoch[i], { g: 17, w: 700 });
    if (i) r += zBogenPfeil(x0 + i * b - 16, yr + 52, x0 + i * b + 16, yr + 52, -22, { b: 1.75 }) + zT(x0 + i * b, yr + 84, ': 2', { g: 14, w: 700 }); });
  return { name: 'Potenzen', felder: [
    { svg: zBlatt(320, 172, s, 'Fünf Zweien in einer Zeile: drei in der ersten Klammer, zwei in der zweiten. Unter der ersten Klammer 2 hoch 3, unter der zweiten 2 hoch 2, unter allen fünf 2 hoch 5'), kopf: 'Hinschreiben und malnehmen', gl: `${W('2³')} · 2² = 2⁵`, satz: 'Hoch 3: drei Zweien, malgenommen. Drei Zweien und zwei Zweien sind fünf Zweien: 3 + 2 = 5.' },
    { svg: zBlatt(320, 142, r, 'Sechs Felder mit 8, 4, 2, 1, ein halb, ein Viertel; darüber 2 hoch 3 bis 2 hoch minus 2; von Feld zu Feld geteilt durch 2. Das Feld 2 hoch 0 gleich 1 ist hervorgehoben'), kopf: 'Die Reihe geht weiter', gl: BL('2⁰ = 1'), satz: 'Jeder Schritt nach rechts teilt durch 2. So wird 2⁰ zu 1 und 2⁻¹ zu ½ – nicht null und nicht negativ.', pfeil: 'Hochzahl 0 und kleiner' },
  ] };
}

// ---------- Rechenregel 9 · Erweitern und Kürzen: zwei gleich lange Streifen ----------
function zStreifen2() {
  const x0 = 70, l = 224, h = 36, y1 = 22, y2 = 118; let s = '';
  s += `<rect x="${x0}" y="${y1}" width="${l / 2}" height="${h}" fill="${ZF.blauFl}"/><rect x="${x0}" y="${y2}" width="${l / 2}" height="${h}" fill="${ZF.blauFl}"/>` + zKasten(x0, y1, l, h, { rx: 0, fl: 'none' }) + zKasten(x0, y2, l, h, { rx: 0, fl: 'none' });
  for (const i of [1, 2, 3]) s += zL(x0 + i * l / 4, y2, x0 + i * l / 4, y2 + h, { b: 2 });
  s += zL(x0 + l / 2, y1 - 12, x0 + l / 2, y2 + h + 12, { f: ZF.gelb, b: 8 }) + zL(x0 + l / 2, y1 - 12, x0 + l / 2, y2 + h + 12, { b: 2.5, strich: '6 4' });
  s += zBruchT(36, y1 + 16, 1, 2, 18) + zBruchT(36, y2 + 16, 2, 4, 18);
  s += zPfeil(x0 + 14, y1 + h + 8, x0 + 14, y2 - 8, { b: 2, kopf: 9 }) + zT(x0 + 24, 84, 'Zähler und', { g: 14, a: 'start', grotesk: true, w: 700 }) + zT(x0 + 24, 102, 'Nenner · 2', { g: 14, a: 'start', grotesk: true, w: 700 });
  s += zPfeil(x0 + l - 14, y2 - 8, x0 + l - 14, y1 + h + 8, { b: 2, kopf: 9 }) + zT(x0 + l - 24, 84, 'Zähler und', { g: 14, a: 'end', grotesk: true, w: 700 }) + zT(x0 + l - 24, 102, 'Nenner : 2', { g: 14, a: 'end', grotesk: true, w: 700 });
  return { name: 'Erweitern und Kürzen', felder: [{ svg: zBlatt(320, 178, s, 'Zwei gleich lange Streifen untereinander. Oben zwei Teile, eines gefärbt. Unten vier Teile, zwei gefärbt. Die gefärbten Flächen enden an derselben senkrechten Linie'), gl: `${bruch(1, 2)} = ${bruch(2, 4)}`, satz: 'Zähler und Nenner mal 2 (nach unten) oder geteilt durch 2 (nach oben): Gefärbt bleibt gleich viel – bis zur selben Linie.' }] };
}

// ---------- Rechenregel 10 · Rechnen mit Brüchen: drei gleich lange Streifen ----------
function zStreifen3() {
  const x0 = 70, l = 228, h = 32, ys = [16, 70, 124], t = l / 6; let s = '';
  s += `<rect x="${x0}" y="${ys[0]}" width="${l / 2}" height="${h}" fill="${ZF.blauFl}"/><rect x="${x0}" y="${ys[1]}" width="${l / 3}" height="${h}" fill="SCHRAFFUR"/>`;
  s += `<rect x="${x0}" y="${ys[2]}" width="${3 * t}" height="${h}" fill="${ZF.blauFl}"/><rect x="${x0 + 3 * t}" y="${ys[2]}" width="${2 * t}" height="${h}" fill="SCHRAFFUR"/>`;
  for (let i = 1; i < 6; i++) s += zL(x0 + i * t, ys[0] + (i === 3 ? h : 0) + (i === 3 ? 0 : 0), x0 + i * t, ys[2], { b: 1, f: ZF.leise, strich: '2 4' }) + zL(x0 + i * t, ys[2], x0 + i * t, ys[2] + h, { b: 2 });
  s += zL(x0 + l / 2, ys[0], x0 + l / 2, ys[0] + h, { b: 2 }) + zL(x0 + l / 3, ys[1], x0 + l / 3, ys[1] + h, { b: 2 }) + zL(x0 + 2 * l / 3, ys[1], x0 + 2 * l / 3, ys[1] + h, { b: 2 });
  ys.forEach((y) => { s += zKasten(x0, y, l, h, { rx: 0, fl: 'none' }); });
  s += `<rect x="${x0}" y="${ys[2]}" width="${5 * t}" height="${h}" fill="none" stroke="${ZF.tinte}" stroke-width="4.5"/>` + zL(x0, ys[2] + h + 10, x0 + 5 * t, ys[2] + h + 10, { f: ZF.gelb, b: 9 }) + zPfad(`M${x0} ${ys[2] + h + 5}v10M${x0 + 5 * t} ${ys[2] + h + 5}v10M${x0} ${ys[2] + h + 10}H${x0 + 5 * t}`, { b: 1.75 });
  s += zBruchT(36, ys[0] + 13, 1, 2, 17) + zBruchT(36, ys[1] + 13, 1, 3, 17) + zBruchT(36, ys[2] + 13, 5, 6, 17) + zT(x0 + 2.5 * t, ys[2] + h + 32, '5 Sechstel', { g: 15, grotesk: true, w: 700 });
  return { name: 'Rechnen mit Brüchen', felder: [{ svg: zBlatt(320, 196, s, 'Drei gleich lange Streifen. Der erste halbiert, eine Hälfte blau. Der zweite gedrittelt, ein Drittel schraffiert. Der dritte in sechs Teilen: drei blau, daneben zwei schraffiert, das sechste leer'), gl: `${bruch(1, 2)} + ${bruch(1, 3)} = ${BL(bruch(3, 6))} + ${SCH(bruch(2, 6))} = ${W(bruch(5, 6))}`, satz: 'Erst gleiche Teile: Aus der Hälfte werden 3 Sechstel, aus dem Drittel 2 Sechstel. Zusammen 5 von 6 Feldern.' }] };
}

// ---------- Rechenregel 11 · Dreisatz: Tabelle mit denselben Pfeilen links und rechts ----------
function zDreisatz() {
  const x0 = 100, b = 60, y0 = 16, hk = 30, h = 42, zl = [['3', '7,50'], ['1', '2,50'], ['5', '12,50']], Y = (i) => y0 + hk + i * h + h / 2; let s = '';
  s += `<rect x="${x0}" y="${y0 + hk + h}" width="${2 * b}" height="${h}" fill="${ZF.gelb}"/>` + zKasten(x0, y0, 2 * b, hk + 3 * h, { rx: 0, fl: 'none' }) + zL(x0 + b, y0, x0 + b, y0 + hk + 3 * h, { b: 1.5 }) + zL(x0, y0 + hk, x0 + 2 * b, y0 + hk, { b: 2.5 });
  s += zL(x0, y0 + hk + h, x0 + 2 * b, y0 + hk + h, { b: 1.25, f: ZF.leise }) + zL(x0, y0 + hk + 2 * h, x0 + 2 * b, y0 + hk + 2 * h, { b: 1.25, f: ZF.leise }) + `<rect x="${x0}" y="${y0 + hk + h}" width="${2 * b}" height="${h}" fill="none" stroke="${ZF.tinte}" stroke-width="4"/>`;
  s += zT(x0 + b / 2, y0 + 21, 'kg', { g: 15, w: 700 }) + zT(x0 + 1.5 * b, y0 + 21, '€', { g: 15, w: 700 });
  zl.forEach((z, i) => { s += zT(x0 + b / 2, Y(i) + 7, z[0], { g: 18, w: 800, f: i === 1 ? '#11161D' : ZF.tinte }) + zT(x0 + 1.5 * b, Y(i) + 7, z[1], { g: 18, w: 800, f: i === 1 ? '#11161D' : ZF.tinte }); });
  for (const [i, t] of [[0, ': 3'], [1, '· 5']]) for (const d of [-1, 1]) { const x = d < 0 ? x0 - 6 : x0 + 2 * b + 6; s += zPfad(`M${x} ${Y(i)}q${d * 26} ${h / 2} ${d * 3} ${h - 5}`, { b: 2 }) + `<polygon points="${x},${Y(i + 1) - 1} ${x + d * 10},${Y(i + 1) - 8} ${x + d * 4},${Y(i + 1) - 13}" fill="${ZF.tinte}"/>` + zMarke(x + d * 44, Y(i) + h / 2, t, { breit: 44 }); }
  s += zT(160, y0 + hk + 3 * h + 24, 'mittlere Zeile: für eins', { g: 15, grotesk: true, w: 700 });
  return { name: 'Verhältnis (Dreisatz)', felder: [{ svg: zBlatt(320, 204, s, 'Tabelle mit den Spalten Kilogramm und Euro: 3 und 7,50, dann 1 und 2,50, dann 5 und 12,50. Links und rechts dieselben Pfeile: geteilt durch 3, dann mal 5. Die mittlere Zeile für eins ist hervorgehoben'), gl: `${W(': 3')} auf eins, dann ${W('· 5')} auf viele`, satz: 'Links und rechts steht dieselbe Rechnung. In der Mitte steht immer der Wert für eins.' }] };
}

// ---------- Rechenregel 12 · Gegenrechnung: hin von links, zurück von rechts ----------
function zRueckweg() {
  const xs = [44, 160, 276], bw = 60, bh = 40, yo = 96, yu = 190; let s = zT(160, 28, '4 · (□ − 12) = −20', { g: 17, w: 700 });
  const box = (x, y, t, o = {}) => zKasten(x - bw / 2, y - bh / 2, bw, bh, { fl: ZF.papier, strich: o.leer ? '5 4' : null, b: o.fett ? 3.5 : 2.5 }) + zT(x, y + 7, t, { g: 19, w: 800 });
  s += box(xs[0], yo, '□') + box(xs[1], yo, '', { leer: 1 }) + box(xs[2], yo, '−20') + box(xs[2], yu, '−20') + box(xs[1], yu, '−5') + box(xs[0], yu, '7', { fett: 1 });
  s += zPfeil(xs[0] + 34, yo, xs[1] - 34, yo, { b: 2.25, kopf: 9 }) + zPfeil(xs[1] + 34, yo, xs[2] - 34, yo, { b: 2.25, kopf: 9 }) + zPfeil(xs[2] - 34, yu, xs[1] + 34, yu, { b: 2.25, kopf: 9 }) + zPfeil(xs[1] - 34, yu, xs[0] + 34, yu, { b: 2.25, kopf: 9 });
  s += zMarkeB(102, yo - 26, '− 12', { breit: 52, g: 15 }) + zMarke(218, yo - 26, '· 4', { breit: 44, g: 15 }) + zMarke(218, yu + 30, ': 4', { breit: 44, g: 15 }) + zMarkeB(102, yu + 30, '+ 12', { breit: 52, g: 15 });
  s += zT(22, yo + 40, 'hin', { g: 14, grotesk: true, w: 700, a: 'start', f: ZF.leise }) + zT(xs[2] - 10, (yo + yu) / 2 + 5, 'zurück', { g: 14, grotesk: true, w: 700, a: 'end', f: ZF.leise }) + zPfeil(xs[2], yo + 24, xs[2], yu - 24, { b: 1.75, kopf: 8, f: ZF.leise, strich: '4 4' }) + zT(160, 256, '□ = 7', { g: 18, w: 800 });
  return { name: 'Gegenrechnung', felder: [{ svg: zBlatt(320, 268, s, 'Obere Reihe von links nach rechts: leeres Kästchen, minus 12, Zwischenkästchen, mal 4, Kästchen minus 20. Untere Reihe von rechts nach links: minus 20, geteilt durch 4, minus 5, plus 12, 7. Geteilt durch 4 steht unter mal 4, plus 12 unter minus 12'), gl: `erst ${W(': 4')}, dann ${BL('+ 12')}`, satz: 'Zurück geht es von rechts: Was zuletzt kam (· 4), wird zuerst rückgängig gemacht (: 4).' }] };
}

// ---------- Rechenregel 14 · Nullprodukt: zwei Kästen, eine Null ----------
function zNullprodukt() {
  const k = (x, t) => `<rect x="${x - 50}" y="50" width="100" height="42" rx="8" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="2.5"/>` + zT(x, 78, t, { g: 18, w: 800, f: '#11161D' });
  let s = zT(160, 30, '(x − 2) · (x + 3) = 0', { g: 16, w: 700 }) + k(66, 'x − 2') + k(196, 'x + 3') + zT(131, 78, '·', { g: 22, w: 800 }) + zT(262, 78, '=', { g: 20, w: 800 }) + zMarke(296, 71, '0', { breit: 30, g: 20 });
  for (const [x, a, b] of [[66, 'x − 2 = 0', 'x = 2'], [196, 'x + 3 = 0', 'x = −3']]) s += zPfeil(x, 98, x, 122, { b: 2.25, kopf: 9 }) + zT(x, 146, a, { g: 15, w: 700 }) + zPfeil(x, 156, x, 172, { b: 1.75, kopf: 7, f: ZF.leise }) + zT(x, 198, b, { g: 19, w: 800 });
  s += zT(131, 197, 'oder', { g: 16, grotesk: true, w: 700 });
  return { name: 'Nullprodukt', felder: [{ svg: zBlatt(320, 214, s, 'Zwei gleich große Kästen x minus 2 und x plus 3 mit Malpunkt, rechts gleich 0. Unter jedem Kasten eine eigene Gleichung: x minus 2 gleich 0, also x gleich 2; x plus 3 gleich 0, also x gleich minus 3. Dazwischen das Wort oder'), gl: 'x = 2 oder x = −3', satz: 'Rechts steht null. Also muss einer der beiden Kästen null sein – der eine oder der andere.' }] };
}

// ---------- Geometrie · Idee 1 · Winkel an Geraden: α = 50°, β = 60°, γ = 70° ----------
function zWinkelsumme() {
  const A = [56, 190], B = [256, 190], ac = 200 * Math.sin(60 * Math.PI / 180) / Math.sin(70 * Math.PI / 180), C = [A[0] + ac * Math.cos(50 * Math.PI / 180), A[1] - ac * Math.sin(50 * Math.PI / 180)]; let s = '';
  s += zWinkel(...A, 34, 0, 50, { fl: ZF.gelb, s: 'α' }) + zWinkel(...B, 34, 120, 180, { fl: ZF.blauFl, f: ZF.blau, s: 'β' }) + zWinkel(...C, 34, 180, 230, { fl: ZF.gelb, s: 'α', ab: 1.5 }) + zWinkel(...C, 34, 230, 300, { fl: 'SCHRAFFUR', s: 'γ', ab: 1.5 }) + zWinkel(...C, 34, 300, 360, { fl: ZF.blauFl, f: ZF.blau, s: 'β', ab: 1.5 });
  s += zL(24, C[1], 300, C[1], { b: 2.5 }) + zL(24, A[1], 300, A[1], { b: 2.5 }) + zP([A, B, C]) + zDach(280, C[1], 0) + zDach(288, C[1], 0) + zDach(280, A[1], 0) + zDach(288, A[1], 0);
  s += zT(A[0] - 8, A[1] + 20, 'A', { g: 16, w: 700 }) + zT(B[0] + 8, B[1] + 20, 'B', { g: 16, w: 700 }) + zT(C[0], C[1] - 10, 'C', { g: 16, w: 700 }) + zT(26, C[1] - 9, 'parallel zu AB', { g: 14, a: 'start', grotesk: true, f: ZF.leise, w: 600 });
  return { name: 'Winkel an Geraden', felder: [{ svg: zBlatt(320, 218, s, 'Dreieck ABC mit den Winkeln Alpha 50 Grad, Beta 60 Grad, Gamma 70 Grad. Durch C läuft eine Parallele zu AB. Bei C liegen Alpha, Gamma und Beta nebeneinander und füllen die Gerade'), gl: `${W('α')} + ${BL('β')} + ${SCH('γ')} = 180°`, satz: 'An der Parallelen kehren α und β oben bei C wieder. Dort füllen α, γ und β lückenlos eine gerade Linie. Hier: 50° + 60° + 70° = 180°.' }] };
}

// ---------- Geometrie · Idee 2 · Gleicher Abstand: Kreis als Hauptzeichnung, zwei Nebenzeichnungen ----------
function zAbstand() {
  const k = 24, M = [160, 104], r = 3 * k; let a = `<circle cx="${M[0]}" cy="${M[1]}" r="${r}" fill="${ZF.blauFl}" fill-opacity=".5" stroke="${ZF.tinte}" stroke-width="2.5"/>`;
  [20, 110, 200, 305].forEach((w) => { const p = [M[0] + r * Math.cos(w * Math.PI / 180), M[1] - r * Math.sin(w * Math.PI / 180)]; a += zGleich(...M, ...p) + `<circle cx="${p[0]}" cy="${p[1]}" r="5" fill="${ZF.tinte}"/>`; });
  a += `<circle cx="${M[0]}" cy="${M[1]}" r="4.5" fill="${ZF.tinte}"/>` + zSchild(M[0] - 14, M[1] + 24, 'M', { g: 16, w: 800 }) + zT(160, 204, '3 cm', { g: 15 });
  const A = [112, 156], B = [208, 156], P = [160, 156 - 3 * k]; let b = zL(160, 30, 160, 186, { b: 2, strich: '6 4' }) + zL(...A, ...B) + zGleich(...P, ...A) + zGleich(...P, ...B) + zRWd(160, 156, 1, 0, 0, -1);
  for (const [p, t, dx, dy] of [[A, 'A', -12, 6], [B, 'B', 12, 6], [P, 'P', 14, -2]]) b += `<circle cx="${p[0]}" cy="${p[1]}" r="5" fill="${ZF.tinte}"/>` + zT(p[0] + dx, p[1] + dy, t, { g: 16, w: 800 });
  b += zL(A[0], 168, 160, 168, { b: 1.5, f: ZF.leise }) + zL(160, 168, B[0], 168, { b: 1.5, f: ZF.leise }) + zT(136, 186, '2 cm', { g: 14 }) + zT(186, 186, '2 cm', { g: 14 });
  const S = [44, 168], w = Math.PI / 6, Pp = [S[0] + 150 * Math.cos(w), S[1] - 150 * Math.sin(w)], F1 = [Pp[0], S[1]], t = 150 * Math.cos(w), F2 = [S[0] + t * Math.cos(2 * w), S[1] - t * Math.sin(2 * w)];
  let c = zWinkel(...S, 30, 0, 60, { fl: ZF.blauFl, f: ZF.blau }) + zL(...S, 292, S[1]) + zL(...S, S[0] + 180 * Math.cos(2 * w), S[1] - 180 * Math.sin(2 * w)) + zL(...S, S[0] + 240 * Math.cos(w), S[1] - 240 * Math.sin(w), { b: 2, strich: '6 4' });
  c += zGleich(...Pp, ...F1) + zGleich(...Pp, ...F2) + zRWd(...F1, -1, 0, 0, -1) + zRWd(...F2, -Math.cos(2 * w), Math.sin(2 * w), Math.sin(2 * w), Math.cos(2 * w)) + `<circle cx="${Pp[0]}" cy="${Pp[1]}" r="5" fill="${ZF.tinte}"/>` + zT(Pp[0] + 14, Pp[1] - 6, 'P', { g: 16, w: 800 }) + zT(S[0] + 46, S[1] - 9, '60°', { g: 14 });
  return { name: 'Gleicher Abstand', felder: [
    { svg: zBlatt(320, 214, a, 'Kreis um M mit Radius 3 cm; vier Punkte auf der Kreislinie sind mit M verbunden, alle vier Strecken tragen dasselbe Strich-Zeichen'), kopf: 'Kreis', gl: 'gleich weit von M', satz: 'Alle Punkte der Kreislinie sind gleich weit von der Mitte: Jede der vier Strecken ist 3 cm lang.' },
    { svg: zBlatt(320, 196, b, 'Strecke AB, 4 cm lang, mit ihrer Mittelsenkrechten. Ein Punkt P darauf, 3 cm über der Mitte, ist mit A und B verbunden; beide Strecken tragen dasselbe Strich-Zeichen'), kopf: 'Mittelsenkrechte', gl: 'gleich weit von A und B', satz: 'Die Mittelsenkrechte geht durch die Mitte von AB und steht senkrecht darauf.', neu: 'Zwei Nebenzeichnungen: dieselbe Idee, andere Linie' },
    { svg: zBlatt(320, 196, c, 'Winkel von 60 Grad mit seiner Winkelhalbierenden. Von einem Punkt P darauf gehen zwei Lote zu den Schenkeln, beide mit rechtem Winkel und demselben Strich-Zeichen'), kopf: 'Winkelhalbierende', gl: 'gleich weit von beiden Schenkeln', satz: 'Der Abstand ist das Lot: Es trifft den Schenkel im rechten Winkel.' },
  ] };
}

// ---------- Geometrie · Idee 3 · Deckungsgleich: Dreieck 3 cm, 4 cm, 5 cm – gespiegelt, verschoben, gedreht ----------
function zDeckung() {
  const dreieck = (A, B, C, n, o = {}) => { const sw = [(A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3], aus = (p, d = 14) => { const l = Math.hypot(p[0] - sw[0], p[1] - sw[1]); return [p[0] + (p[0] - sw[0]) / l * d, p[1] + (p[1] - sw[1]) / l * d + 5]; };
    const bogen = (V, P, Q, r) => { const a1 = Math.atan2(P[1] - V[1], P[0] - V[0]), a2 = Math.atan2(Q[1] - V[1], Q[0] - V[0]); let d = a2 - a1; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI; return zPfad(`M${V[0] + r * Math.cos(a1)} ${V[1] + r * Math.sin(a1)}A${r} ${r} 0 0 ${d > 0 ? 1 : 0} ${V[0] + r * Math.cos(a2)} ${V[1] + r * Math.sin(a2)}`, { b: 1.5 }); };
    const lab = Math.hypot(B[0] - A[0], B[1] - A[1]), lac = Math.hypot(C[0] - A[0], C[1] - A[1]), ua = [(B[0] - A[0]) / lab, (B[1] - A[1]) / lab], va = [(C[0] - A[0]) / lac, (C[1] - A[1]) / lac];
    return zP([A, B, C], { fl: ZF.blauFl }) + bogen(B, A, C, 26) + bogen(C, A, B, 16) + bogen(C, A, B, 21) + zRWd(...A, ...ua, ...va, 9) + zStrich(...A, ...C, 1) + zStrich(...A, ...B, 2) + zStrich(...B, ...C, 3)
      + [[A, 'A'], [B, 'B'], [C, 'C']].map(([p, t]) => (o.ohne || '').includes(t) ? '' : zT(...aus(p), t + n, { g: 15, w: 800 })).join(''); };
  const sp = dreieck([28, 164], [132, 164], [28, 86], '') + dreieck([292, 164], [188, 164], [292, 86], '′') + zL(160, 36, 160, 186, { b: 2, strich: '8 4 2 4' }) + zT(160, 24, 'Spiegelachse', { g: 14, grotesk: true, w: 700 });
  const vs = dreieck([22, 176], [118, 176], [22, 104], '') + dreieck([172, 116], [268, 116], [172, 44], '′') + zPfeil(128, 172, 258, 124, { b: 2.5 }) + zT(214, 172, 'Verschiebung', { g: 14, grotesk: true, w: 700, a: 'start' });
  const D = [106, 178]; const dr = dreieck([162, 178], [258, 178], [162, 106], '') + dreieck([106, 122], [106, 26], [34, 122], '′', { ohne: 'A' }) + zT(120, 118, 'A′', { g: 15, w: 800 }) + zL(...D, 162, 178, { b: 1.5, strich: '4 4', f: ZF.leise }) + zL(...D, 106, 122, { b: 1.5, strich: '4 4', f: ZF.leise })
    + zPfad('M138 178A32 32 0 0 0 106 146', { b: 2 }) + `<polygon points="106,146 116,141 115,152" fill="${ZF.tinte}"/>` + `<circle cx="${D[0]}" cy="${D[1]}" r="5" fill="${ZF.tinte}"/>` + zT(D[0], D[1] + 22, 'Drehpunkt', { g: 14, grotesk: true, w: 700 }) + zT(144, 152, '90°', { g: 14, w: 700 });
  const fuss = 'Ein Strich: 3 cm. Zwei Striche: 4 cm. Drei Striche: 5 cm.';
  return { name: 'Deckungsgleich', felder: [
    { svg: zBlatt(320, 200, sp, 'Dreieck ABC mit den Seiten 3, 4 und 5 cm und sein Spiegelbild an einer senkrechten Achse; gleiche Seiten tragen gleiche Strich-Zeichen, gleiche Winkel gleiche Bögen'), kopf: 'Spiegeln', gl: 'Seiten 3 cm, 4 cm, 5 cm bleiben', satz: 'Gleich groß, aber seitenverkehrt: Der Umlauf A, B, C dreht sich um. ' + fuss },
    { svg: zBlatt(320, 200, vs, 'Dasselbe Dreieck, längs eines Pfeils verschoben; alle Strich-Zeichen und Bögen gleich'), kopf: 'Schieben', gl: 'Seiten 3 cm, 4 cm, 5 cm bleiben', satz: 'Jeder Punkt wandert gleich weit in dieselbe Richtung.', pfeil: 'oder' },
    { svg: zBlatt(320, 206, dr, 'Dasselbe Dreieck, um 90 Grad um einen Punkt gedreht; alle Strich-Zeichen und Bögen gleich'), kopf: 'Drehen', gl: 'Seiten 3 cm, 4 cm, 5 cm bleiben', satz: 'Um den Drehpunkt um 90° gedreht. Längen und Winkel bleiben.', pfeil: 'oder' },
  ] };
}

// ---------- Geometrie · Idee 4 · Ähnlich: zwei Strahlen von S, zwei Parallelen, alles mal 2 ----------
function zAehnlich() {
  const k = 36, S = [34, 222], c = 0.5625, sn = Math.sqrt(1 - c * c), R1 = (d) => [S[0] + d * k, S[1]], R2 = (d) => [S[0] + d * k * c, S[1] - d * k * sn], P1 = R1(2), P2 = R1(4), Q1 = R2(3), Q2 = R2(6); let s = '';
  s += zP([S, P2, Q2], { fl: ZF.blauFl, b: 0.01, f: 'none' }) + zP([S, P1, Q1], { fl: ZF.blau, b: 0.01, f: 'none', deck: 0.28 });
  const wq = Math.atan2(Q1[1] - P1[1], Q1[0] - P1[0]) * -180 / Math.PI;
  for (const P of [P1, P2]) s += zWinkel(...P, 22, wq, 180, { fl: ZF.gelb });
  s += zL(...S, ...R1(5.3)) + zL(...S, ...R2(6.6)) + zL(...P1, ...Q1, { b: 3 }) + zL(...P2, ...Q2, { b: 3 });
  for (const [P, Q] of [[P1, Q1], [P2, Q2]]) { const m = [(P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2]; s += zDach(m[0], m[1], -wq) ; }
  s += `<circle cx="${S[0]}" cy="${S[1]}" r="5" fill="${ZF.tinte}"/>` + zT(S[0] - 14, S[1] + 6, 'S', { g: 16, w: 800 });
  s += zPfad(`M${S[0]} ${S[1] + 10}v6H${P1[0]}v-6`, { f: ZF.leise, b: 1.5 }) + zT((S[0] + P1[0]) / 2, S[1] + 32, '2 cm', { g: 14 }) + zPfad(`M${S[0]} ${S[1] + 38}v6H${P2[0]}v-6`, { f: ZF.leise, b: 1.5 }) + zT((S[0] + P2[0]) / 2 + 30, S[1] + 60, '4 cm', { g: 14 });
  s += zSchild(Q1[0] - 34, Q1[1] + 30, '3 cm', { g: 14 }) + zSchild(Q2[0] - 40, Q2[1] + 26, '6 cm', { g: 14 }) + zSchild((P1[0] + Q1[0]) / 2 + 30, (P1[1] + Q1[1]) / 2 + 12, '2,5 cm', { g: 14 }) + zSchild((P2[0] + Q2[0]) / 2 + 32, (P2[1] + Q2[1]) / 2, '5 cm', { g: 14 });
  s += zMarke(258, 60, 'alles mal 2', { breit: 112, g: 15 });
  return { name: 'Ähnlich', felder: [{ svg: zBlatt(320, 292, s, 'Zwei Strahlen von S. Zwei parallele Geraden schneiden beide: Abschnitte 2 cm und 4 cm auf dem ersten Strahl, 3 cm und 6 cm auf dem zweiten; die Parallelen sind 2,5 cm und 5 cm lang. Das große Dreieck ist in jeder Länge doppelt so groß wie das kleine'), gl: `2 cm ${W('· 2')} = 4 cm`, satz: 'Gleiche Winkel, gleiche Form. Jede Länge des großen Dreiecks ist das Doppelte, von S aus gemessen: 2 und 4, 3 und 6, 2,5 und 5.' }] };
}

// ---------- Geometrie · Idee 5 · Rechtwinkliges Dreieck: Quadrate mit 9, 16 und 25 Feldern ----------
function zPythagoras() {
  const k = 18, C = [118, 150], B = [C[0] + 4 * k, C[1]], A = [C[0], C[1] - 3 * k], n = [54 / 90, -72 / 90], u = [72 / 90, 54 / 90]; let s = '';
  const gitter = (O, e1, e2, m) => { let g = zP([O, [O[0] + e1[0] * m * k, O[1] + e1[1] * m * k], [O[0] + (e1[0] + e2[0]) * m * k, O[1] + (e1[1] + e2[1]) * m * k], [O[0] + e2[0] * m * k, O[1] + e2[1] * m * k]], { fl: ZF.blauFl, b: 2 });
    for (let i = 1; i < m; i++) g += zL(O[0] + e1[0] * i * k, O[1] + e1[1] * i * k, O[0] + e1[0] * i * k + e2[0] * m * k, O[1] + e1[1] * i * k + e2[1] * m * k, { b: 1, f: ZF.leise }) + zL(O[0] + e2[0] * i * k, O[1] + e2[1] * i * k, O[0] + e2[0] * i * k + e1[0] * m * k, O[1] + e2[1] * i * k + e1[1] * m * k, { b: 1, f: ZF.leise }); return g; };
  s += gitter(C, [1, 0], [0, 1], 4) + gitter(A, [-1, 0], [0, 1], 3) + gitter(A, u, n, 5);
  s += zP([A, B, C], { fl: ZF.papier }) + zL(...A, ...B, { f: ZF.gelb, b: 9 }) + zL(...A, ...B, { b: 3.5 }) + `<rect x="${C[0]}" y="${C[1] - 13}" width="13" height="13" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="2"/><circle cx="${C[0] + 6.5}" cy="${C[1] - 6.5}" r="1.5" fill="${ZF.tinte}"/>`;
  s += zSchild(C[0] + 2 * k, C[1] + 2 * k + 6, '16', { g: 18, w: 800 }) + zSchild(A[0] - 1.5 * k, A[1] + 1.5 * k + 6, '9', { g: 18, w: 800 }) + zSchild(A[0] + (u[0] + n[0]) * 2.5 * k, A[1] + (u[1] + n[1]) * 2.5 * k + 6, '25', { g: 18, w: 800 });
  s += zT(C[0] + 2 * k + 6, C[1] - 6, 'b', { g: 15, w: 800 }) + zT(C[0] + 9, C[1] - 1.5 * k - 2, 'a', { g: 15, w: 800, a: 'start' }) + zSchild((A[0] + B[0]) / 2 + 10, (A[1] + B[1]) / 2 - 10, 'c', { g: 16, w: 800 });
  return { name: 'Rechtwinkliges Dreieck', felder: [{ svg: zBlatt(320, 236, s, 'Rechtwinkliges Dreieck mit den Katheten 3 cm und 4 cm und der Hypotenuse 5 cm. Über jeder Seite ein Quadrat aus Einheitsquadraten: 9, 16 und 25 Felder. Der rechte Winkel und die Hypotenuse sind hervorgehoben'), gl: `9 + 16 = ${W('25')}`, satz: 'Die zwei kleinen Quadrate haben zusammen so viele Felder wie das große. Die längste Seite c liegt dem rechten Winkel gegenüber.' }] };
}

// ---------- Fläche und Raum · Idee 4 · Aufklappen: Quader, halb aufgeklappt, Netz ----------
function zAufklappen() {
  const F = { a: ZF.gelb, b: ZF.blauFl, c: 'SCHRAFFUR' };
  const w = 30, t = 10.6, qx = 66, qy = 190, P = (a, b, c) => [qx + a * w + b * t, qy - c * w - b * t];
  let q = zP([P(0, 0, 0), P(5, 0, 0), P(5, 0, 3), P(0, 0, 3)], { fl: F.b }) + zP([P(0, 0, 3), P(5, 0, 3), P(5, 4, 3), P(0, 4, 3)], { fl: F.a }) + zP([P(5, 0, 0), P(5, 4, 0), P(5, 4, 3), P(5, 0, 3)], { fl: F.c });
  q += zL(...P(0, 0, 0), ...P(0, 4, 0), { f: ZF.leise, b: 1.75, strich: '4 4' }) + zL(...P(0, 4, 0), ...P(5, 4, 0), { f: ZF.leise, b: 1.75, strich: '4 4' }) + zL(...P(0, 4, 0), ...P(0, 4, 3), { f: ZF.leise, b: 1.75, strich: '4 4' });
  q += zT(qx + 2.5 * w, qy + 24, '5 cm', { g: 16 }) + zT(P(5, 2, 0)[0] + 12, P(5, 2, 0)[1] + 18, '4 cm', { g: 16, a: 'start' }) + zT(P(5, 4, 1.5)[0] + 9, P(5, 4, 1.5)[1] + 6, '3 cm', { g: 16, a: 'start' });
  // halb aufgeklappt: Boden bleibt liegen, Vorderwand liegt schon flach, Seitenwände und Rückwand stehen schräg ab, der Deckel hängt an der Rückwand
  const u = 21, tt = 7.6, hx = 82, hy = 172, H = (a, b, c) => [hx + a * u + b * tt, hy - c * u - b * tt], dh = 2.9, dz = 0.78, lh = 3.92, lz = 0.8;
  let m = zP([H(0, 4 + dh, dz), H(5, 4 + dh, dz), H(5, 4 + dh + lh, dz + lz), H(0, 4 + dh + lh, dz + lz)], { fl: F.a }) + zP([H(0, 4, 0), H(5, 4, 0), H(5, 4 + dh, dz), H(0, 4 + dh, dz)], { fl: F.b });
  m += zP([H(0, 0, 0), H(0, 4, 0), H(-dh, 4, dz), H(-dh, 0, dz)], { fl: F.c }) + zP([H(0, 0, 0), H(5, 0, 0), H(5, 4, 0), H(0, 4, 0)], { fl: F.a }) + zP([H(5, 0, 0), H(5, 4, 0), H(5 + dh, 4, dz), H(5 + dh, 0, dz)], { fl: F.c }) + zP([H(0, 0, 0), H(5, 0, 0), H(5, -3, 0), H(0, -3, 0)], { fl: F.b });
  m += zT(160, 224, 'Wände und Deckel klappen nach außen', { g: 14, grotesk: true, w: 700 });
  const k = 15, nx = 77, ny = 8, R = (x, y, b, h, f, s) => `<rect x="${nx + x * k}" y="${ny + y * k}" width="${b * k}" height="${h * k}" fill="${F[f]}" stroke="${ZF.tinte}" stroke-width="2.5" stroke-linejoin="round"/>` + zSchild(nx + (x + b / 2) * k, ny + (y + h / 2) * k + 5, s, { g: 14, w: 700, breit: s.length > 3 ? 0 : 30 });
  const n = R(3, 0, 5, 4, 'a', '20 cm²') + R(3, 4, 5, 3, 'b', '15 cm²') + R(3, 7, 5, 4, 'a', '20 cm²') + R(3, 11, 5, 3, 'b', '15 cm²') + R(0, 7, 3, 4, 'c', '12') + R(8, 7, 3, 4, 'c', '12') + zT(nx - 6, ny + 9 * k + 5, 'cm²', { g: 14, a: 'end' }) + zT(nx + 11 * k + 6, ny + 9 * k + 5, 'cm²', { g: 14, a: 'start' });
  return { name: 'Haut des Körpers', felder: [
    { svg: zBlatt(320, 230, q, 'Quader 5 cm mal 4 cm mal 3 cm im Schrägbild; Deckfläche gelb, Vorderfläche blau, Seitenfläche schraffiert, verdeckte Kanten gestrichelt'), kopf: 'Der Körper', gl: 'Quader 5 cm · 4 cm · 3 cm', satz: 'Schrägbild: Kanten nach hinten unter 45° und halb so lang. Verdeckte Kanten gestrichelt.' },
    { svg: zBlatt(320, 232, m, 'Derselbe Quader halb aufgeklappt: Der Boden liegt, die vier Wände kippen nach außen, der Deckel hängt an der Rückwand. Gleiche Flächen haben dieselbe Farbe wie im Schrägbild'), kopf: 'Aufklappen', gl: 'sechs Flächen, je zwei gleich', satz: 'Das ist die Hauptsache: Beim Aufklappen wird aus dem Körper seine Haut.', pfeil: 'aufklappen' },
    { svg: zBlatt(320, 230, n, 'Netz des Quaders in Kreuzform: sechs Rechtecke, je zwei gleiche gleich gefärbt: zweimal 20, zweimal 15, zweimal 12 Quadratzentimeter'), kopf: 'Das Netz', gl: `<span class="nb">O = 2 · (${W('20')} + ${BL('15')} + ${SCH('12')}) cm²</span> <span class="nb">= 94 cm²</span>`, satz: 'Flach ausgebreitet: sechs Rechtecke, je zwei gleich.', pfeil: 'flach legen' },
  ] };
}

Object.assign(ZEICHNUNGEN, { R1: zStellen, R2: zUmdrehen, R3: zTreppe, R4: zReihenfolge, R5: zKaertchen, R7: zZettel, R8: zPotenz, R9: zStreifen2, R10: zStreifen3, R11: zDreisatz, R12: zRueckweg, R14: zNullprodukt,
  'I-geo-1': zWinkelsumme, 'I-geo-2': zAbstand, 'I-geo-3': zDeckung, 'I-geo-4': zAehnlich, 'I-geo-5': zPythagoras, 'I-fur-4': zAufklappen });
Object.assign(MINI_FELD, { R7: 1, 'I-fur-4': 1 });
