// Zeichnungen des Gesetzbuchs. Stil „Heft und Tafel“, zweite Fassung nach den Zeichen-Vorgaben des Mathe-Profis (Auftrag 11).
// Was zu sehen ist, Maße und Beschriftung stammen aus seinen Vorgaben; hier steht nur, WIE es gezeichnet wird.
// Regeln: maßstäblich · die hervorgehobene Stelle ist gelb UND trägt ein Zeichen ohne Farbe (Rahmen oder Strichart) ·
// dieselbe Markierung in der Rechenzeile · Höhen immer mit dem Zeichen für den rechten Winkel · „·“ ist nur Malzeichen.
const ZF = { tinte: 'var(--z-tinte)', leise: 'var(--z-leise)', gelb: 'var(--z-gelb)', gelbFl: 'var(--z-gelb-fl)', blau: 'var(--z-blau)', blauFl: 'var(--z-blau-fl)', papier: 'var(--z-papier)', karo: 'var(--z-karo)', rot: 'var(--z-rot)' };
let zNr = 0;
const zT = (x, y, s, o = {}) => `<text${o.grotesk ? ' class="anm"' : ''} x="${x}" y="${y}" text-anchor="${o.a || 'middle'}" font-family="${o.grotesk ? 'var(--grotesk)' : 'var(--mono)'}" font-size="${o.g || 15}" font-weight="${o.w || 600}" fill="${o.f || ZF.tinte}"${o.dreh ? ` transform="rotate(${o.dreh} ${x} ${y})"` : ''}>${s}</text>`;
const zL = (x1, y1, x2, y2, o = {}) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${o.f || ZF.tinte}" stroke-width="${o.b || 2.5}" stroke-linecap="round"${o.strich ? ` stroke-dasharray="${o.strich}"` : ''}/>`;
const zP = (pkt, o = {}) => `<polygon points="${pkt.map((p) => p.join(',')).join(' ')}" fill="${o.fl || 'none'}" stroke="${o.f || ZF.tinte}" stroke-width="${o.b || 2.5}" stroke-linejoin="round"${o.strich ? ` stroke-dasharray="${o.strich}"` : ''}${o.deck ? ` fill-opacity="${o.deck}"` : ''}/>`;
const zPfad = (d, o = {}) => `<path d="${d}" fill="${o.fl || 'none'}" stroke="${o.f || ZF.tinte}" stroke-width="${o.b || 2.5}" stroke-linecap="round" stroke-linejoin="round"${o.strich ? ` stroke-dasharray="${o.strich}"` : ''}/>`;
function zPfeil(x1, y1, x2, y2, o = {}) { // gerader Pfeil mit gefüllter Spitze
  const f = o.f || ZF.tinte, b = o.b || 3, w = Math.atan2(y2 - y1, x2 - x1), k = o.kopf || 10, bx = x2 - Math.cos(w) * k, by = y2 - Math.sin(w) * k, nx = Math.sin(w) * k * 0.55, ny = -Math.cos(w) * k * 0.55;
  return `<line x1="${x1}" y1="${y1}" x2="${bx}" y2="${by}" stroke="${f}" stroke-width="${b}" stroke-linecap="round"${o.strich ? ` stroke-dasharray="${o.strich}"` : ''}/><polygon points="${x2},${y2} ${bx + nx},${by + ny} ${bx - nx},${by - ny}" fill="${f}" stroke="${f}" stroke-width="1.5" stroke-linejoin="round"/>`;
}
function zBogenPfeil(x1, y1, x2, y2, hoch, o = {}) { // gebogener Pfeil über einen Scheitel
  const f = o.f || ZF.tinte, mx = (x1 + x2) / 2, my = (y1 + y2) / 2 - hoch, w = Math.atan2(y2 - my, x2 - mx), k = 9, bx = x2 - Math.cos(w) * k, by = y2 - Math.sin(w) * k, nx = Math.sin(w) * k * 0.55, ny = -Math.cos(w) * k * 0.55;
  return `<path d="M${x1} ${y1}Q${mx} ${my} ${bx} ${by}" fill="none" stroke="${f}" stroke-width="${o.b || 2.5}" stroke-linecap="round"${o.strich ? ` stroke-dasharray="${o.strich}"` : ''}/><polygon points="${x2},${y2} ${bx + nx},${by + ny} ${bx - nx},${by - ny}" fill="${f}" stroke="${f}" stroke-width="1.5" stroke-linejoin="round"/>`;
}
const zMarke = (x, y, s, o = {}) => { const b = o.breit || Math.max(30, String(s).length * 10 + 14); return `<rect x="${x - b / 2}" y="${y - 15}" width="${b}" height="30" rx="8" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.5"/>${zT(x, y + 5.5, s, { f: '#11161D', w: 700, g: o.g || 16 })}`; };
const zSchild = (x, y, s, o = {}) => { const b = o.breit || String(s).replace(/<[^>]+>/g, '').length * (o.g || 14) * 0.62 + 12; return `<rect x="${o.a === 'start' ? x - 6 : o.a === 'end' ? x - b + 6 : x - b / 2}" y="${y - (o.g || 14)}" width="${b}" height="${(o.g || 14) + 8}" rx="5" fill="${ZF.papier}"/>${zT(x, y, s, o)}`; };
function zBlatt(w, h, innen, titel, karo) {
  const id = 'zk' + (++zNr);
  return `<svg class="z-feld" viewBox="0 0 ${w} ${h}" role="img" aria-label="${titel}">${karo ? `<defs><pattern id="${id}" width="${karo}" height="${karo}" patternUnits="userSpaceOnUse" x="${(karo.x || 0)}"><path d="M${karo} 0H0V${karo}" fill="none" stroke="${ZF.karo}" stroke-width="1"/></pattern><pattern id="${id}s" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" stroke="${ZF.leise}" stroke-width="2"/></pattern></defs><rect width="${w}" height="${h}" fill="url(#${id})"/>` : `<defs><pattern id="${id}s" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" stroke="${ZF.leise}" stroke-width="2"/></pattern></defs>`}${innen.replace(/SCHRAFFUR/g, `url(#${id}s)`)}</svg>`;
}
const zKlammer = (x1, x2, y, s, unten, gr) => { const d = unten ? 1 : -1; return zPfad(`M${x1} ${y}v${d * 7}H${x2}v${-d * 7}`, { f: ZF.leise, b: 1.75 }) + zSchild((x1 + x2) / 2, y + d * 7 + 5, s, { g: gr || 15 }); };
// Rechter Winkel: kleines Quadrat mit Punkt am Fußpunkt (x, y); sx, sy = Richtung der beiden Schenkel (je ±1).
const zRW = (x, y, sx, sy, s = 9) => zPfad(`M${x + sx * s} ${y}v${sy * s}h${-sx * s}`, { b: 1.5 }) + `<circle cx="${x + sx * s * 0.48}" cy="${y + sy * s * 0.48}" r="1.3" fill="${ZF.tinte}"/>`;
// Höhe: Leuchtstift gelb, darauf gestrichelte Linie in Tinte, rechter Winkel am Fuß. Das ist in jeder Figur dasselbe Zeichen.
const zHoehe = (x, yU, yO, sx = 1) => zL(x, yU, x, yO, { f: ZF.gelb, b: 8 }) + zL(x, yU, x, yO, { b: 2, strich: '5 4' }) + zRW(x, yU, sx, -1);
// Rechenzeile im Bild; Teile in [eckigen Klammern] sind hervorgehoben: gelb mit Rahmen.
function zGl(x, y, teile, g = 17) {
  const bw = g * 0.6, rand = 5, breite = teile.reduce((s, t) => s + (Array.isArray(t) ? t[0].length * bw + 2 * rand : t.length * bw), 0); let cx = x - breite / 2, aus = '';
  for (const t of teile) { const s = Array.isArray(t) ? t[0] : t, w = s.length * bw;
    if (Array.isArray(t)) { cx += rand; aus += `<rect x="${cx - 4}" y="${y - g + 1}" width="${w + 8}" height="${g + 7}" rx="5" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.5"/>`; }
    aus += zT(cx + w / 2, y, s, { g, w: 700, f: Array.isArray(t) ? '#11161D' : ZF.tinte }); cx += w + (Array.isArray(t) ? rand : 0); }
  return aus;
}
const bruch = (z, n) => `<span class="br"><i>${z}</i><i>${n}</i></span>`;
const W = (s) => `<b class="w">${s}</b>`;

// ---------- Rechenregel 6 · Ausmultiplizieren: eine Zeichnung, vier Beschriftungen ----------
function zAusmultiplizieren() {
  const feld = (o) => { const u = o.u, br = (o.a + o.b) * u, x0 = o.x0 || 62 + (236 - br) / 2, xt = x0 + o.a * u, x1 = x0 + br, ym = 86, y0 = ym - o.h * u / 2, y1 = ym + o.h * u / 2; let s = '';
    s += `<rect x="${x0}" y="${y0}" width="${xt - x0}" height="${y1 - y0}" fill="${ZF.blauFl}"/><rect x="${xt}" y="${y0}" width="${x1 - xt}" height="${y1 - y0}" fill="${o.weg ? 'SCHRAFFUR' : ZF.blauFl}"${o.weg ? ' fill-opacity=".6"' : ''}/>`;
    if (o.karo) { for (let i = 1; i < o.a + o.b; i++) s += zL(x0 + i * u, y0, x0 + i * u, y1, { b: 0.75, f: ZF.karo }); for (let j = 1; j < o.h; j++) s += zL(x0, y0 + j * u, x1, y0 + j * u, { b: 0.75, f: ZF.karo }); }
    s += zL(x0, y0, xt, y0) + zL(x0, y1, xt, y1) + zL(x0, y0, x0, y1) + zL(xt, y0, xt, y1, o.weg ? { b: 2, strich: '6 5' } : { b: 2 }) + zL(xt, y0, x1, y0, o.weg ? { strich: '6 5' } : {}) + zL(xt, y1, x1, y1, o.weg ? { strich: '6 5' } : {}) + zL(x1, y0, x1, y1, o.weg ? { strich: '6 5' } : {});
    s += `<rect x="${x0 - 11}" y="${y0}" width="7" height="${y1 - y0}" rx="3" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.25"/>` + zMarke(x0 - 34, ym, o.f, { breit: 34, g: o.fG || 16 });
    s += zT((x0 + xt) / 2, y0 - 12, o.ta, { g: 16 }) + zT((xt + x1) / 2, y0 - 12, o.tb, { g: o.tbG || 16 });
    s += zSchild((x0 + xt) / 2, ym + 5, o.ia, { g: 15 }) + (o.ibAussen ? zT(x1 + 7, ym + (o.ibG ? 7 : 5), o.ib, { g: o.ibG || 14, a: 'start' }) : zSchild((xt + x1) / 2, ym + 5, o.ib, { g: o.ibG || 14, breit: Math.min(x1 - xt - 2, 50) }));
    if (o.ganz) s += zKlammer(x0, x1, y1 + 7, o.ganz, true, 15);
    return zBlatt(320, 150, s, o.titel); };
  return { name: 'Ausmultiplizieren und Ausklammern', felder: [
    { svg: feld({ u: 10, h: 6, a: 20, b: 2, karo: 1, f: '6', ta: '20', tb: '2', ia: '120', ib: '12', ibG: 14, titel: 'Rechteck, 6 Kästchen hoch und 22 Kästchen breit, geteilt bei 20: links 120 Kästchen, rechts 12' }), kopf: 'Zahlen', gl: `6 · (20 + 2) = ${W('6 ·')} 20 + ${W('6 ·')} 2`, satz: 'Maßstäblich: 6 Kästchen hoch, 20 + 2 Kästchen breit. Der Faktor 6 gehört zu beiden Feldern.' },
    { svg: feld({ u: 10, h: 6, a: 18, b: 2, karo: 1, weg: 1, x0: 64, f: '6', ta: '20 − 2', tb: '2', ia: '6 · (20 − 2)', ib: '6 · 2', ibAussen: 1, ganz: '20', titel: 'Rechteck, 6 Kästchen hoch und 20 breit; rechts ist ein Stück der Breite 2 gestrichelt abgetrennt' }), kopf: 'Zahlen mit Minus', gl: `6 · (20 − 2) = ${W('6 ·')} 20 − ${W('6 ·')} 2`, satz: 'Dasselbe Rechteck, 20 breit. Das gestrichelte Stück 6 · 2 kommt weg.' },
    { svg: feld({ u: 20, h: 3, a: 8, b: 2, f: '3', ta: 'x', tb: '2', ia: '3x', ib: '6', ibG: 15, titel: 'Rechteck der Höhe 3, geteilt in die Breiten x und 2; x ist deutlich länger als 2' }), kopf: 'mit x', gl: `3 · (x + 2) = ${W('3 ·')} x + ${W('3 ·')} 2`, satz: 'Dieselbe Zeichnung, neue Beschriftung. Rückwärts gelesen ist es das Ausklammern: 3x + 6 = 3 · (x + 2).' },
    { svg: feld({ u: 46, h: 0.5, a: 4, b: 2 / 3, f: '½', fG: 22, ta: '4', tb: '⅔', tbG: 24, ia: '2', ib: '⅓', ibG: 22, ibAussen: 1, titel: 'Rechteck der Höhe ein halb, geteilt in die Breiten 4 und zwei Drittel' }), kopf: 'mit Brüchen', gl: `${bruch(1, 2)} · (4 + ${bruch(2, 3)}) = ${W(bruch(1, 2) + ' ·')} 4 + ${W(bruch(1, 2) + ' ·')} ${bruch(2, 3)}`, satz: 'Auch maßstäblich: ein halb hoch, 4 und zwei Drittel breit.' },
  ] };
}

// ---------- Rechenregel 13 · Gleichung als Waage: dreimal dieselbe Waage, der Balken immer waagerecht ----------
function zWaage() {
  const sack = (x, y, geist) => zPfad(`M${x - 9} ${y - 24}q9 5 18 0l-3 6q9 8 5 18h-22q-4 -10 5 -18z`, { fl: geist ? 'none' : ZF.blauFl, f: geist ? ZF.leise : ZF.tinte, b: 2, strich: geist ? '4 4' : null }) + (geist ? '' : zT(x, y - 4, 'x', { g: 14, w: 700 }));
  const kugel = (x, y, geist, dunkel) => `<circle cx="${x}" cy="${y}" r="5.5" fill="${geist ? 'none' : dunkel ? '#11161D' : ZF.tinte}" stroke="${geist ? ZF.leise : dunkel ? '#11161D' : ZF.tinte}" stroke-width="1.75"${geist ? ' stroke-dasharray="3 3"' : ''}/>`;
  const rahmen = (p) => p.length ? `<rect x="${Math.min(...p.map((e) => e[0])) - 9}" y="${Math.min(...p.map((e) => e[1])) - 9}" width="${Math.max(...p.map((e) => e[0])) - Math.min(...p.map((e) => e[0])) + 18}" height="${Math.max(...p.map((e) => e[1])) - Math.min(...p.map((e) => e[1])) + 18}" rx="9" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.75" stroke-dasharray="5 3"/>` : '';
  const feld = (links, rechts, titel) => { const y = 126, sch = (cx) => zL(cx, 60, cx - 44, y, { b: 1.75, f: ZF.leise }) + zL(cx, 60, cx + 44, y, { b: 1.75, f: ZF.leise }) + zPfad(`M${cx - 50} ${y}H${cx + 50}M${cx - 46} ${y}q46 22 92 0`, { b: 2.5 });
    let l = '', r = '', mL = [], mR = []; let x = 70 - (links.reduce((s, e) => s + (e[0] === 's' ? 24 : 13), 0)) / 2;
    links.forEach((e) => { if (e[0] === 's') { l += sack(x + 12, y - 2, e[1] === 'g'); x += 24; } else { if (e[1] === 'y') mL.push([x + 6.5, y - 7]); l += kugel(x + 6.5, y - 7, e[1] === 'g', e[1] === 'y'); x += 13; } });
    rechts.forEach((e, i) => { if (!e) return; const p = [250 - 32.5 + (i % 6) * 13, y - 7 - Math.floor(i / 6) * 13]; if (e[1] === 'y') mR.push(p); r += kugel(...p, e[1] === 'g', e[1] === 'y'); });
    return zBlatt(320, 196, `${zL(160, 60, 160, 176, { b: 3 })}${zL(124, 176, 196, 176, { b: 3 })}${zL(70, 60, 250, 60, { b: 3 })}${zP([[160, 48], [152, 62], [168, 62]], { fl: ZF.tinte })}
      ${sch(70)}${sch(250)}${rahmen(mL)}${rahmen(mR)}${l}${r}${zSchild(160, 118, '=', { g: 20, w: 800 })}`, titel); };
  const K = ['k'], Y = ['k', 'y'], G = ['k', 'g'], S = ['s'];
  return { name: 'Gleichung als Waage', felder: [
    { svg: feld([S, S, Y, Y], [K, K, K, K, K, Y, K, K, K, K, K, Y], 'Waage im Gleichgewicht: links zwei Säckchen x und zwei Kugeln, rechts zwölf Kugeln; auf jeder Seite sind zwei Kugeln umrahmt'), gl: '2x + 2 = 12', satz: 'Links und rechts liegt gleich viel. Umrahmt: was gleich auf beiden Seiten weggenommen wird.' },
    { svg: feld([S, S, G, G], [K, K, K, K, K, G, K, K, K, K, K, G], 'Waage im Gleichgewicht: links zwei Säckchen, rechts zehn Kugeln'), gl: '2x = 10', satz: 'Auf beiden Seiten 2 Kugeln weg. Die Waage bleibt im Gleichgewicht.', pfeil: `${W('− 2')} auf beiden Seiten` },
    { svg: feld([S, ['s', 'g']], [K, K, K, K, K, null, G, G, G, G, G], 'Waage im Gleichgewicht: links ein Säckchen, rechts fünf Kugeln'), gl: 'x = 5', satz: 'Beide Seiten halbiert: Ein Säckchen wiegt so viel wie 5 Kugeln.', pfeil: `${W(': 2')} auf beiden Seiten` },
  ] };
}

// ---------- Rechenregel 2 · Plus und Minus: zwei Zahlengeraden untereinander, beide Starts genau übereinander bei 3 ----------
function zZahlenstrahl() {
  const X = (v) => 40 + (v + 1) * 34;
  const gerade = (ya, ziel, teile) => { let s = zL(22, ya, 290, ya, { b: 2 }) + zP([[300, ya], [289, ya - 5], [289, ya + 5]], { fl: ZF.tinte, b: 1 });
    for (let v = -1; v <= 6; v++) s += zL(X(v), ya - 6, X(v), ya + 6, { b: v === 0 ? 3 : 1.75 }) + zT(X(v), ya + 24, v < 0 ? '−' + (-v) : v, { g: 15, w: v === 0 || v === 3 || v === ziel ? 800 : 600, f: v === 0 || v === 3 || v === ziel ? ZF.tinte : ZF.leise });
    s += zBogenPfeil(X(3), ya - 9, X(ziel), ya - 9, 58, { f: ZF.gelb, b: 9 }) + zBogenPfeil(X(3), ya - 9, X(ziel), ya - 9, 58, { b: 2.5 });
    s += `<circle cx="${X(3)}" cy="${ya}" r="6" fill="${ZF.tinte}"/><circle cx="${X(ziel)}" cy="${ya}" r="7" fill="${ZF.papier}" stroke="${ZF.tinte}" stroke-width="2.5"/>`;
    return s + zGl(160, ya - 58, teile); };
  const oben = gerade(96, 1, ['3 ', ['+'], ' (', ['−'], '2) = 1']), unten = gerade(222, 5, ['3 ', ['−'], ' (', ['−'], '2) = 5']);
  const lot = zL(X(3), 104, X(3), 180, { f: ZF.leise, b: 1.5, strich: '3 4' });
  return { name: 'Plus und Minus mit negativen Zahlen', felder: [
    { svg: zBlatt(320, 256, oben + lot + unten, 'Zwei Zahlengeraden von minus 1 bis 6 untereinander. Oben: Start bei 3, Pfeil zwei Einheiten nach links, Ziel 1. Unten: Start bei 3, Pfeil zwei Einheiten nach rechts, Ziel 5'),
      mini: zBlatt(320, 130, oben, 'Zahlengerade: Start bei 3, Pfeil zwei Einheiten nach links, Ziel 1'), gl: '', satz: 'Beide Starts liegen bei 3 (voller Punkt), beide Pfeile sind genau zwei Einheiten lang. Nur die Richtung ist verschieden. Der Ring ist das Ziel.' },
  ] };
}

// ---------- Fläche und Raum · Idee 1 · Auslegen und zählen: Rechteck 6 cm mal 4 cm, Quader 5 mal 4 mal 3 ----------
function zAuslegen() {
  const k = 34, x0 = 96, y0 = 34; let s = `<rect x="${x0}" y="${y0 + 3 * k}" width="${6 * k}" height="${k}" fill="${ZF.gelb}"/><rect x="${x0}" y="${y0}" width="${k}" height="${k}" fill="${ZF.blauFl}"/>`;
  for (let i = 1; i < 6; i++) s += zL(x0 + i * k, y0, x0 + i * k, y0 + 4 * k, { b: 1.25, f: ZF.leise });
  for (let j = 1; j < 4; j++) s += zL(x0, y0 + j * k, x0 + 6 * k, y0 + j * k, { b: 1.25, f: ZF.leise });
  s += `<rect x="${x0}" y="${y0}" width="${6 * k}" height="${4 * k}" fill="none" stroke="${ZF.tinte}" stroke-width="2.5" stroke-linejoin="round"/><rect x="${x0}" y="${y0 + 3 * k}" width="${6 * k}" height="${k}" fill="none" stroke="${ZF.tinte}" stroke-width="4" stroke-linejoin="round"/>`;
  s += zT(x0 + 3 * k, y0 + 4 * k + 26, '6 cm', { g: 17 }) + zT(x0 + 6 * k + 9, y0 + 2 * k + 6, '4 cm', { g: 17, a: 'start' });
  s += zPfad(`M${x0 + 4} ${y0 + k / 2}h-14`, { b: 1.5 }) + zT(x0 - 14, y0 + k / 2 + 6, '1 cm²', { g: 16, a: 'end', w: 700 });
  // Quader aus Würfeln im Schrägbild: 45°, Tiefe halb so lang
  const w = 30, t = 10.6, qx = 96, qy = 208, P = (a, b, c) => [qx + a * w + b * t, qy - c * w - b * t]; let q = '';
  q += zP([P(0, 0, 0), P(5, 0, 0), P(5, 0, 3), P(0, 0, 3)], { fl: ZF.blauFl, b: 0.01, f: 'none' }) + zP([P(5, 0, 0), P(5, 4, 0), P(5, 4, 3), P(5, 0, 3)], { fl: ZF.blauFl, b: 0.01, f: 'none' }) + zP([P(0, 0, 3), P(5, 0, 3), P(5, 4, 3), P(0, 4, 3)], { fl: ZF.blauFl, b: 0.01, f: 'none' });
  q += zP([P(0, 0, 0), P(5, 0, 0), P(5, 4, 0), P(5, 4, 1), P(5, 0, 1), P(0, 0, 1)], { fl: ZF.gelb, b: 0.01, f: 'none' });
  for (let i = 1; i < 5; i++) q += zL(...P(i, 0, 0), ...P(i, 0, 3), { b: 1.25, f: ZF.leise }) + zL(...P(i, 0, 3), ...P(i, 4, 3), { b: 1.25, f: ZF.leise });
  for (let j = 1; j < 3; j++) q += zL(...P(0, 0, j), ...P(5, 0, j), { b: 1.25, f: ZF.leise }) + zL(...P(5, 0, j), ...P(5, 4, j), { b: 1.25, f: ZF.leise });
  for (let b = 1; b < 4; b++) q += zL(...P(5, b, 0), ...P(5, b, 3), { b: 1.25, f: ZF.leise }) + zL(...P(0, b, 3), ...P(5, b, 3), { b: 1.25, f: ZF.leise });
  q += zP([P(0, 0, 0), P(5, 0, 0), P(5, 4, 0), P(5, 4, 3), P(0, 4, 3), P(0, 0, 3)]) + zL(...P(0, 0, 3), ...P(5, 0, 3)) + zL(...P(5, 0, 3), ...P(5, 0, 0)) + zL(...P(5, 0, 3), ...P(5, 4, 3));
  q += zP([P(0, 0, 0), P(5, 0, 0), P(5, 4, 0), P(5, 4, 1), P(5, 0, 1), P(0, 0, 1)], { b: 4 }) + zL(...P(5, 0, 0), ...P(5, 0, 1), { b: 4 });
  q += zT(qx + 2.5 * w, qy + 24, '5', { g: 17 }) + zT(P(5, 2, 0)[0] + 12, P(5, 2, 0)[1] + 16, '4', { g: 17, a: 'start' }) + zT(P(5, 4, 1.5)[0] + 10, P(5, 4, 1.5)[1] + 6, '3', { g: 17, a: 'start' });
  q += zPfad(`M${qx + 4} ${qy - 2.5 * w}h-14`, { b: 1.5 }) + zT(qx - 14, qy - 2.5 * w + 6, '1 cm³', { g: 16, a: 'end', w: 700 }) + `<rect x="${qx}" y="${qy - 3 * w}" width="${w}" height="${w}" fill="none" stroke="${ZF.tinte}" stroke-width="2.5"/>`;
  return { name: 'Auslegen und zählen', felder: [
    { svg: zBlatt(360, 208, s, 'Rechteck 6 cm mal 4 cm, ausgelegt mit 24 Einheitsquadraten; die unterste Reihe mit 6 Quadraten ist hervorgehoben'), kopf: 'Fläche', gl: `4 Reihen ${W('zu je 6')} = 24 cm²`, satz: 'Ein Quadrat ist 1 cm². Die umrahmte Reihe wird viermal gezählt.' },
    { svg: zBlatt(360, 250, q, 'Quader aus Würfeln im Schrägbild: 5 breit, 4 tief, 3 hoch; die unterste Schicht ist hervorgehoben'), kopf: 'Körper', gl: `3 Schichten ${W('zu je 5 · 4')} = 60 cm³`, satz: 'Ein Würfel ist 1 cm³. Die umrahmte Schicht wird dreimal gezählt.', pfeil: 'dasselbe im Raum' },
  ] };
}

// ---------- Fläche und Raum · Idee 2 · Aus dem Rechteck: Stammbaum mit zwei eigenen Ästen ----------
function zFlaechen() {
  const k = 18, B = 108, bl = (innen, titel, h = 150) => zBlatt(300, h, innen, titel, k);
  const mk = (off) => [(c) => off + c * k, (r) => B - r * k];
  const unten = (x, s, leise) => zT(x, B + 22, s, { g: 16, f: leise ? ZF.leise : ZF.tinte }), hText = (x, y, a) => zMarke(x, y, '4 cm', { breit: 50, g: 15 });
  let [X, Y] = mk(90);
  const rechteck = zP([[X(0), Y(0)], [X(6), Y(0)], [X(6), Y(4)], [X(0), Y(4)]], { fl: ZF.blauFl }) + zHoehe(X(6), Y(0), Y(4), -1) + unten(X(3), '6 cm') + hText(X(6) + 34, Y(2)) + zSchild(X(3), Y(2) + 5, '24 cm²', { g: 16, w: 700 });
  [X, Y] = mk(54);
  const para = zP([[X(2), Y(0)], [X(6), Y(0)], [X(8), Y(4)], [X(2), Y(4)]], { fl: ZF.blauFl, b: 0.01, f: 'none' }) + zP([[X(6), Y(0)], [X(8), Y(0)], [X(8), Y(4)]], { fl: 'SCHRAFFUR', b: 2, strich: '5 4' })
    + zP([[X(0), Y(0)], [X(2), Y(0)], [X(2), Y(4)]], { fl: 'SCHRAFFUR', b: 2 }) + zP([[X(0), Y(0)], [X(6), Y(0)], [X(8), Y(4)], [X(2), Y(4)]]) + zHoehe(X(2), Y(0), Y(4))
    + zBogenPfeil(X(1), Y(4) - 5, X(7.5), Y(4) - 5, 44, { b: 2.25 }) + unten(X(3), '6 cm') + hText(X(-1.6), Y(2)) + zSchild(X(4.4), Y(1.8) + 5, '24 cm²', { g: 16, w: 700 });
  const dreieck = zP([[X(6), Y(0)], [X(8), Y(4)], [X(2), Y(4)]], { f: ZF.leise, b: 2, strich: '5 4' }) + zP([[X(0), Y(0)], [X(6), Y(0)], [X(2), Y(4)]], { fl: ZF.blauFl }) + zHoehe(X(2), Y(0), Y(4))
    + unten(X(3), '6 cm') + zSchild(X(3.3), Y(0.9) + 5, '12 cm²', { g: 16, w: 700 }) + hText(X(-0.4), Y(3)) + zT(X(5.5), Y(3) + 5, 'andere', { g: 14, grotesk: true, f: ZF.leise, w: 600 }) + zT(X(5.5), Y(3) + 21, 'Hälfte', { g: 14, grotesk: true, f: ZF.leise, w: 600 });
  [X, Y] = mk(18);
  const trapez = zP([[X(9), Y(0)], [X(14), Y(0)], [X(15), Y(4)], [X(6), Y(4)]], { f: ZF.leise, b: 2, strich: '5 4' }) + zP([[X(0), Y(0)], [X(9), Y(0)], [X(6), Y(4)], [X(1), Y(4)]], { fl: ZF.blauFl }) + zHoehe(X(1), Y(0), Y(4))
    + unten(X(4.5), '9 cm') + unten(X(11.5), '5 cm', 1) + zT(X(3.5), Y(4) - 8, '5 cm', { g: 16 }) + zT(X(10.5), Y(4) - 8, '9 cm', { g: 16, f: ZF.leise }) + zSchild(X(5.2), Y(1.2) + 5, '28 cm²', { g: 16, w: 700 }) + hText(X(1) + 46, Y(2.9)) + zT(X(11.4), Y(2) + 5, 'gleiches Trapez', { g: 14, grotesk: true, f: ZF.leise, w: 600 });
  [X, Y] = mk(72);
  const drachen = zP([[X(0), Y(0)], [X(8), Y(0)], [X(8), Y(5)], [X(0), Y(5)]], { f: ZF.leise, b: 2, strich: '5 4' }) + zP([[X(0), Y(2.5)], [X(3), Y(5)], [X(8), Y(2.5)], [X(3), Y(0)]], { fl: ZF.blauFl })
    + zL(X(0), Y(2.5), X(8), Y(2.5), { b: 1.75, strich: '5 4' }) + zL(X(3), Y(0), X(3), Y(5), { b: 1.75, strich: '5 4' }) + zRW(X(3), Y(2.5), 1, -1) + unten(X(4), '8 cm') + zT(X(8) + 9, Y(2.5) + 6, '5 cm', { g: 16, a: 'start' }) + zSchild(X(5.2), Y(1.6) + 5, '20 cm²', { g: 16, w: 700 });
  // Kreis mit r = 3 cm in 12 Tortenstücken, darunter abwechselnd umgelegt
  const r = 3 * k, cx = 150, cy = 64; let kreis = '';
  for (let i = 0; i < 12; i++) { const a = i * Math.PI / 6, b = a + Math.PI / 6; kreis += zPfad(`M${cx} ${cy}L${cx + r * Math.cos(a)} ${cy + r * Math.sin(a)}A${r} ${r} 0 0 1 ${cx + r * Math.cos(b)} ${cy + r * Math.sin(b)}Z`, { fl: i % 2 ? ZF.blauFl : ZF.papier, b: 1.5 }); }
  kreis += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${ZF.tinte}" stroke-width="2.5"/>` + zT(cx + r + 10, cy + 5, 'r = 3 cm', { g: 16, a: 'start' });
  const sn = r * Math.sin(Math.PI / 12), cs = r * Math.cos(Math.PI / 12), yT = 152, xa = (300 - 13 * sn) / 2 + sn;
  for (let i = 0; i < 6; i++) { const x = xa + i * 2 * sn;
    kreis += zPfad(`M${x} ${yT}L${x - sn} ${yT + cs}A${r} ${r} 0 0 0 ${x + sn} ${yT + cs}Z`, { fl: ZF.blauFl, b: 1.5 }) + zPfad(`M${x + sn} ${yT + cs}L${x} ${yT}A${r} ${r} 0 0 1 ${x + 2 * sn} ${yT}Z`, { fl: ZF.papier, b: 1.5 }); }
  kreis += zHoehe(xa - sn - 12, yT + cs, yT, -1) + zMarke(xa - sn - 34, yT + cs / 2, 'r', { breit: 26 }) + zKlammer(xa - sn, xa + 12 * sn, yT + cs + 8, 'etwa π · r', true, 15) + zPfeil(cx, cy + r + 7, cx, yT - 9, { b: 2.25 });
  return { name: 'Aus dem Rechteck', felder: [
    { svg: bl(rechteck, 'Rechteck 6 cm mal 4 cm auf Karopapier, Fläche 24 cm²; die Höhe ist hervorgehoben'), kopf: 'Rechteck', gl: `6 cm · ${W('4 cm')} = 24 cm²`, satz: 'Der Anfang: Länge mal Breite.' },
    { svg: bl(para, 'Parallelogramm mit Grundseite 6 cm und Höhe 4 cm: Das schraffierte Dreieck links wird abgeschnitten und rechts angesetzt, es entsteht das Rechteck'), kopf: 'Parallelogramm', gl: `6 cm · ${W('4 cm')} = 24 cm²`, satz: 'Gleich groß wie das Rechteck. Die Höhe steht senkrecht auf der Grundseite.', pfeil: 'abschneiden und ansetzen' },
    { svg: bl(dreieck, 'Dreieck mit Grundseite 6 cm und Höhe 4 cm: genau die Hälfte des Parallelogramms, die andere Hälfte ist gestrichelt'), kopf: 'Dreieck', gl: `6 cm · ${W('4 cm')} : 2 = 12 cm²`, satz: 'Die Diagonale teilt das Parallelogramm in zwei gleiche Dreiecke.', pfeil: 'halbieren' },
    { svg: bl(trapez, 'Trapez mit den parallelen Seiten 9 cm und 5 cm und der Höhe 4 cm; mit einem gleichen Trapez ergibt es ein Parallelogramm mit der Grundseite 14 cm'), kopf: 'Trapez', gl: `(9 cm + 5 cm) : 2 · ${W('4 cm')} = 28 cm²`, satz: 'Zwei gleiche Trapeze ergeben ein Parallelogramm. Eines ist die Hälfte.', pfeil: 'verdoppeln' },
    { svg: bl(drachen, 'Drachenviereck mit den Diagonalen 8 cm und 5 cm in einem Rechteck 8 cm mal 5 cm, das doppelt so groß ist'), kopf: 'Drachenviereck', gl: '8 cm · 5 cm : 2 = 20 cm²', satz: 'Das Rechteck darum ist doppelt so groß.', neu: 'Zwei eigene Äste, wieder vom Rechteck aus' },
    { svg: bl(kreis, 'Kreis mit Radius 3 cm, in 12 Tortenstücke geschnitten; darunter die Stücke abwechselnd umgelegt zu einem Fast-Rechteck, etwa Pi mal r breit und r hoch', 236), kopf: 'Kreis', gl: `A = π · r · ${W('r')} = π · r²`, satz: '12 Tortenstücke, abwechselnd umgelegt: fast ein Rechteck, etwa π · r breit und r hoch.', pfeil: 'zerschneiden und umlegen' },
  ] };
}

// ---------- Fläche und Raum · Idee 3 · Aus dem Quader: Stammbaum der Körper, alle gleich hoch ----------
function zKoerper() {
  const ox = 30, oy = -18;
  const quaderKanten = (x, y, w, h, o = {}) => { const f = o.f || ZF.tinte, st = o.strich, v = (a, b, c, d, hinten) => zL(a, b, c, d, { f: hinten ? (o.fHinten || ZF.leise) : f, b: hinten ? 1.75 : (o.b || 2.5), strich: hinten ? '4 4' : st });
    return v(x, y, x + ox, y + oy, true) + v(x + ox, y + oy, x + w + ox, y + oy, true) + v(x + ox, y + oy, x + ox, y - h + oy, true)
      + v(x, y, x + w, y) + v(x + w, y, x + w + ox, y + oy) + v(x, y, x, y - h) + v(x + w, y, x + w, y - h) + v(x + w + ox, y + oy, x + w + ox, y - h + oy)
      + v(x, y - h, x + w, y - h) + v(x + w, y - h, x + w + ox, y - h + oy) + v(x, y - h, x + ox, y - h + oy) + v(x + ox, y - h + oy, x + w + ox, y - h + oy); };
  const boden = (x, y, w) => zP([[x, y], [x + w, y], [x + w + ox, y + oy], [x + ox, y + oy]], { fl: ZF.gelb, b: 1.25 });
  const hoehe = (x, y, h, sx = -1, s = 'h') => zL(x, y, x, y - h, { f: ZF.blau, b: 2.5, strich: '6 4' }) + zL(x - sx * 14, y, x + sx * 2, y, { f: ZF.blau, b: 1.5 }) + zPfad(`M${x - sx * 9} ${y}v-9h${sx * 9}`, { f: ZF.blau, b: 1.5 }) + zT(x + sx * 8, y - h / 2 + 5, s, { g: 16, a: sx < 0 ? 'end' : 'start', f: ZF.blau, w: 800 });
  const G = (x, y) => zT(x, y, 'G', { g: 15, f: '#11161D', w: 800 });
  const scheibe = (cx, cy, rx, ry, voll) => `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.25"/>` + zPfad(`M${cx - rx} ${cy}A${rx} ${ry} 0 0 0 ${cx + rx} ${cy}`);
  let q = boden(64, 176, 130);
  for (const i of [1, 2]) q += zP([[64, 176 - i * 34], [194, 176 - i * 34], [194 + ox, 176 - i * 34 + oy], [64 + ox, 176 - i * 34 + oy]], { f: ZF.leise, b: 1.5, strich: '2 4' });
  q += quaderKanten(64, 176, 130, 102) + G(144, 172) + hoehe(46, 176, 102) + zT(236, 132, 'Schicht', { g: 14.5, grotesk: true, f: ZF.leise, a: 'start', w: 500 }) + zT(236, 149, 'auf Schicht', { g: 14.5, grotesk: true, f: ZF.leise, a: 'start', w: 500 });
  const pA = [24, 178], pB = [112, 178], pC = [86, 150], ph = 102, hoch = (p) => [p[0], p[1] - ph];
  let p = zP([pA, pB, pC], { fl: ZF.gelb, b: 1.25 }) + zL(...pA, ...pC, { f: ZF.leise, b: 1.75, strich: '4 4' }) + zL(...pB, ...pC, { f: ZF.leise, b: 1.75, strich: '4 4' }) + zL(...pC, ...hoch(pC), { f: ZF.leise, b: 1.75, strich: '4 4' });
  for (const i of [1, 2]) p += zP([pA, pB, pC].map((e) => [e[0], e[1] - i * ph / 3]), { f: ZF.leise, b: 1.5, strich: '2 4' });
  p += zL(...pA, ...pB) + zL(...pA, ...hoch(pA)) + zL(...pB, ...hoch(pB)) + zP([hoch(pA), hoch(pB), hoch(pC)]) + G(74, 172);
  const cx = 232, rx = 50, ry = 15, cyU = 172, cyO = 70;
  p += scheibe(cx, cyU, rx, ry);
  for (const i of [1, 2]) p += `<ellipse cx="${cx}" cy="${cyU - i * 34}" rx="${rx}" ry="${ry}" fill="none" stroke="${ZF.leise}" stroke-width="1.5" stroke-dasharray="2 4"/>`;
  p += zL(cx - rx, cyU, cx - rx, cyO) + zL(cx + rx, cyU, cx + rx, cyO) + `<ellipse cx="${cx}" cy="${cyO}" rx="${rx}" ry="${ry}" fill="none" stroke="${ZF.tinte}" stroke-width="2.5"/>` + G(cx, cyU + 5) + hoehe(158, 178, 102);
  const bx = 26, by = 180, bw = 92, bh = 102, sp = [bx + bw / 2 + ox / 2, by - bh + oy / 2], fuss = [bx + bw / 2 + ox / 2, by + oy / 2];
  let d = boden(bx, by, bw) + quaderKanten(bx, by, bw, bh, { f: ZF.leise, b: 1.5, strich: '2 4', fHinten: ZF.leise });
  d += zL(bx + ox, by + oy, ...sp, { f: ZF.leise, b: 1.75, strich: '4 4' }) + zL(bx, by, bx + bw, by) + zL(bx + bw, by, bx + bw + ox, by + oy) + zL(bx, by, ...sp) + zL(bx + bw, by, ...sp) + zL(bx + bw + ox, by + oy, ...sp) + G(bx + 22, by - 5) + hoehe(fuss[0], fuss[1], bh, 1);
  const kx = 240, kr = 46, kry = 14, kU = 172, kO = 70;
  d += scheibe(kx, kU, kr, kry) + zL(kx - kr, kU, kx - kr, kO, { f: ZF.leise, b: 1.5, strich: '2 4' }) + zL(kx + kr, kU, kx + kr, kO, { f: ZF.leise, b: 1.5, strich: '2 4' }) + `<ellipse cx="${kx}" cy="${kO}" rx="${kr}" ry="${kry}" fill="none" stroke="${ZF.leise}" stroke-width="1.5" stroke-dasharray="2 4"/>`;
  d += zL(kx - kr, kU, kx, kO) + zL(kx + kr, kU, kx, kO) + G(kx - 26, kU + 6) + hoehe(kx, kU, kU - kO, 1);
  const ux = 150, ur = 51, uU = 176, uO = 74, um = (uU + uO) / 2;
  let u = scheibe(ux, uU, ur, 15) + zL(ux - ur, uU, ux - ur, uO, { f: ZF.leise, b: 1.75, strich: '4 4' }) + zL(ux + ur, uU, ux + ur, uO, { f: ZF.leise, b: 1.75, strich: '4 4' }) + `<ellipse cx="${ux}" cy="${uO}" rx="${ur}" ry="15" fill="none" stroke="${ZF.leise}" stroke-width="1.75" stroke-dasharray="4 4"/>`;
  u += `<circle cx="${ux}" cy="${um}" r="${ur}" fill="${ZF.blauFl}" fill-opacity=".8" stroke="${ZF.tinte}" stroke-width="2.5"/>` + zPfad(`M${ux - ur} ${um}A${ur} 15 0 0 0 ${ux + ur} ${um}`, { b: 1.75 }) + zPfad(`M${ux - ur} ${um}A${ur} 15 0 0 1 ${ux + ur} ${um}`, { b: 1.5, f: ZF.leise, strich: '4 4' }) + G(ux + 30, uU + 9) + hoehe(ux - ur - 22, uU, uU - uO);
  return { name: 'Aus dem Quader', felder: [
    { svg: zBlatt(320, 206, q, 'Quader im Schrägbild: Grundfläche G gelb, Höhe h gestrichelt mit rechtem Winkel, Schichten angedeutet'), kopf: 'Quader', gl: `V = ${W('G')} · <b class="bl">h</b>`, satz: 'Auf der Grundfläche liegt eine Schicht. Davon stapelt man so viele, wie der Körper hoch ist.' },
    { svg: zBlatt(320, 206, p, 'Dreiecksprisma und Zylinder im Schrägbild, gleich hoch wie der Quader, Grundfläche G gelb, Höhe h senkrecht'), kopf: 'Prisma und Zylinder', gl: `V = ${W('G')} · <b class="bl">h</b>`, satz: 'Andere Grundfläche, gleiches Stapeln.', pfeil: 'andere Grundfläche' },
    { svg: zBlatt(320, 206, d, 'Pyramide in ihrem Quader und Kegel in seinem Zylinder: gleiche Grundfläche G, gleiche Höhe h; die Höhe steht senkrecht auf der Grundfläche'), kopf: 'Pyramide und Kegel', gl: `V = ${bruch(1, 3)} · ${W('G')} · <b class="bl">h</b>`, satz: 'Die Spitze füllt ein Drittel des Körpers darum. Die Höhe läuft senkrecht, nie an der schrägen Kante entlang.', pfeil: 'ein Drittel' },
    { svg: zBlatt(320, 206, u, 'Kugel in dem Zylinder, in den sie genau passt'), kopf: 'Kugel', gl: `Kugel = ${bruch(2, 3)} des Zylinders`, satz: 'Die Kugel im genau passenden Zylinder füllt zwei Drittel davon.', pfeil: 'zwei Drittel' },
  ] };
}

// ---------- Fläche und Raum · Idee 4 · Haut des Körpers: Quader 5 cm mal 4 cm mal 3 cm und sein Netz ----------
function zNetz() {
  const F = { a: ZF.gelb, b: ZF.blauFl, c: 'SCHRAFFUR' };
  const w = 30, t = 10.6, qx = 66, qy = 190, P = (a, b, c) => [qx + a * w + b * t, qy - c * w - b * t];
  let q = zP([P(0, 0, 0), P(5, 0, 0), P(5, 0, 3), P(0, 0, 3)], { fl: F.b }) + zP([P(0, 0, 3), P(5, 0, 3), P(5, 4, 3), P(0, 4, 3)], { fl: F.a }) + zP([P(5, 0, 0), P(5, 4, 0), P(5, 4, 3), P(5, 0, 3)], { fl: F.c });
  q += zL(...P(0, 0, 0), ...P(0, 4, 0), { f: ZF.leise, b: 1.75, strich: '4 4' }) + zL(...P(0, 4, 0), ...P(5, 4, 0), { f: ZF.leise, b: 1.75, strich: '4 4' }) + zL(...P(0, 4, 0), ...P(0, 4, 3), { f: ZF.leise, b: 1.75, strich: '4 4' });
  q += zT(qx + 2.5 * w, qy + 24, '5 cm', { g: 16 }) + zT(P(5, 2, 0)[0] + 12, P(5, 2, 0)[1] + 18, '4 cm', { g: 16, a: 'start' }) + zT(P(5, 4, 1.5)[0] + 9, P(5, 4, 1.5)[1] + 6, '3 cm', { g: 16, a: 'start' });
  const k = 15, nx = 62, ny = 10, R = (x, y, b, h, f, s) => `<rect x="${nx + x * k}" y="${ny + y * k}" width="${b * k}" height="${h * k}" fill="${F[f]}" stroke="${ZF.tinte}" stroke-width="2.5" stroke-linejoin="round"/>` + zSchild(nx + (x + b / 2) * k, ny + (y + h / 2) * k + 5, s, { g: 14, w: 700 });
  const n = R(4, 0, 5, 4, 'a', '20 cm²') + R(4, 4, 5, 3, 'b', '15 cm²') + R(4, 7, 5, 4, 'a', '20 cm²') + R(4, 11, 5, 3, 'b', '15 cm²') + R(0, 4, 4, 3, 'c', '12 cm²') + R(9, 4, 4, 3, 'c', '12 cm²');
  return { name: 'Haut des Körpers', felder: [
    { svg: zBlatt(320, 230, q, 'Quader 5 cm mal 4 cm mal 3 cm im Schrägbild; Deckfläche gelb, Vorderfläche blau, Seitenfläche schraffiert, verdeckte Kanten gestrichelt'), kopf: 'Der Körper im Raum', gl: 'Quader 5 cm · 4 cm · 3 cm', satz: 'Schrägbild: Kanten nach hinten unter 45° und halb so lang. Verdeckte Kanten gestrichelt.' },
    { svg: zBlatt(320, 230, n, 'Netz des Quaders in Kreuzform: sechs Rechtecke, je zwei gleiche gleich gefärbt: zweimal 20, zweimal 15, zweimal 12 Quadratzentimeter'), kopf: 'Seine Haut, ausgebreitet', gl: `O = 2 · (${W('20')} + <b class="bl">15</b> + <b class="sf">12</b>) cm² = 94 cm²`, satz: 'Sechs Rechtecke, je zwei gleich: gleiche Farbe im Schrägbild und im Netz.', pfeil: 'aufschneiden und ausbreiten' },
  ] };
}

const ZEICHNUNGEN = { R6: zAusmultiplizieren, R13: zWaage, R2: zZahlenstrahl, 'I-fur-1': zAuslegen, 'I-fur-2': zFlaechen, 'I-fur-3': zKoerper, 'I-fur-4': zNetz };
const MINI_FELD = { R6: 0, R13: 0, R2: 0, 'I-fur-1': 0, 'I-fur-2': 1, 'I-fur-3': 2, 'I-fur-4': 1 };
// Baut eine Zeichnung als Folge von Feldern mit Rechnung und Satz darunter. Ein Feld mit „neu“ beginnt eine neue Reihe (eigener Ast).
function zeichnung(schluessel) {
  const z = ZEICHNUNGEN[schluessel]?.(); if (!z) return '';
  const reihen = []; z.felder.forEach((f) => { if (f.neu || !reihen.length) reihen.push({ titel: f.neu, felder: [] }); reihen[reihen.length - 1].felder.push(f); });
  return `<figure class="zeichnung" data-felder="${z.felder.length}">${reihen.map((r) => `${r.titel ? `<p class="z-ast">${r.titel}</p>` : ''}<div class="z-reihe" data-n="${r.felder.length}">${r.felder.map((f, i) => `${i ? `<div class="z-pfeil${f.pfeil ? '' : ' leer'}" aria-hidden="true"></div>` : ''}<div class="z-teil">${f.pfeil ? `<p class="z-schritt">${f.pfeil}</p>` : ''}${f.kopf ? `<p class="z-kopf">${f.kopf}</p>` : ''}${f.svg}${f.gl ? `<p class="z-gl">${f.gl.includes(' = ') && !f.gl.includes('class="nb"') ? f.gl.replace(' = ', ' <span class="nb">= ') + '</span>' : f.gl}</p>` : ''}<p class="z-satz">${f.satz}</p></div>`).join('')}</div>`).join('')}</figure>`;
}
// Ein Feld ohne Text: als kleines Bild in der Übersicht.
function zeichnungKlein(schluessel) { const z = ZEICHNUNGEN[schluessel]?.(); if (!z) return ''; const f = z.felder[MINI_FELD[schluessel] || 0]; return `<div class="z-mini">${f.mini || f.svg}</div>`; }
