// Zeichnungen des Gesetzbuchs. Stil „Heft und Tafel“: Strich 2,5 in Tinte, Hilfslinien gestrichelt,
// Gelb = die Stelle, an der das Gesetz wirkt. Blau = die Fläche oder Größe, um die es geht. Karos nur, wo gezählt wird.
// Jede Zeichnung ist eine Folge von Feldern (je 320 Einheiten breit), die am Handy untereinander rutschen.
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
const zMarke = (x, y, s, o = {}) => { const b = o.breit || Math.max(30, String(s).length * 10 + 14); return `<rect x="${x - b / 2}" y="${y - 15}" width="${b}" height="30" rx="8" fill="${ZF.gelb}"/>${zT(x, y + 5.5, s, { f: '#11161D', w: 700, g: o.g || 16 })}`; };
const zSchild = (x, y, s, o = {}) => { const b = o.breit || String(s).replace(/<[^>]+>/g, '').length * (o.g || 14) * 0.62 + 12; return `<rect x="${o.a === 'start' ? x - 6 : o.a === 'end' ? x - b + 6 : x - b / 2}" y="${y - (o.g || 14)}" width="${b}" height="${(o.g || 14) + 8}" rx="5" fill="${ZF.papier}"/>${zT(x, y, s, o)}`; };
function zBlatt(w, h, innen, titel, karo) {
  const id = 'zk' + (++zNr);
  return `<svg class="z-feld" viewBox="0 0 ${w} ${h}" role="img" aria-label="${titel}">${karo ? `<defs><pattern id="${id}" width="${karo}" height="${karo}" patternUnits="userSpaceOnUse" x="${(karo.x || 0)}"><path d="M${karo} 0H0V${karo}" fill="none" stroke="${ZF.karo}" stroke-width="1"/></pattern><pattern id="${id}s" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" stroke="${ZF.leise}" stroke-width="2"/></pattern></defs><rect width="${w}" height="${h}" fill="url(#${id})"/>` : `<defs><pattern id="${id}s" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" stroke="${ZF.leise}" stroke-width="2"/></pattern></defs>`}${innen.replace(/SCHRAFFUR/g, `url(#${id}s)`)}</svg>`;
}
const zKlammer = (x1, x2, y, s, unten, gr) => { const d = unten ? 1 : -1; return zPfad(`M${x1} ${y}v${d * 7}H${x2}v${-d * 7}`, { f: ZF.leise, b: 1.75 }) + zSchild((x1 + x2) / 2, y + d * 7 + 5, s, { g: gr || 15 }); };

// ---------- 1 Ausmultiplizieren: ein Rechteck, drei Beschriftungen ----------
function zAusmultiplizieren() {
  const feld = (o) => { const x0 = 74, xt = 232, x1 = 292, y0 = 56, y1 = 152, ym = (y0 + y1) / 2;
    return zBlatt(320, 200, `
      <rect x="${x0}" y="${y0}" width="${xt - x0}" height="${y1 - y0}" fill="${ZF.blauFl}"/>
      <rect x="${xt}" y="${y0}" width="${x1 - xt}" height="${y1 - y0}" fill="${o.weg ? 'SCHRAFFUR' : ZF.blauFl}"${o.weg ? ' fill-opacity=".55"' : ''}/>
      ${zL(x0, y0, x1, y0)}${zL(x0, y1, x1, y1)}${zL(x0, y0, x0, y1)}${zL(x1, y0, x1, y1, o.weg ? { strich: '6 5' } : {})}${zL(xt, y0, xt, y1, { b: 2 })}
      ${o.weg ? zL(xt, y0, x1, y0, { f: ZF.papier, b: 3.5 }) + zL(xt, y0, x1, y0, { strich: '6 5' }) + zL(xt, y1, x1, y1, { f: ZF.papier, b: 3.5 }) + zL(xt, y1, x1, y1, { strich: '6 5' }) : ''}
      <rect x="56" y="${y0}" width="7" height="${y1 - y0}" rx="3.5" fill="${ZF.gelb}"/>${zMarke(30, ym, o.f, { breit: 40 })}
      ${zT((x0 + xt) / 2, 42, o.a, { g: o.gr || 15 })}${zT((xt + x1) / 2, 42, o.b, { g: o.gr || 15 })}
      ${zSchild((x0 + xt) / 2, ym + 5, o.ia, { g: o.gr || 15 })}${zSchild((xt + x1) / 2, ym + 5, o.ib, { g: o.gr ? 16 : 14, breit: 54 })}
      ${zKlammer(x0, x1, y1 + 8, o.ganz, true, o.gr)}`, o.titel); };
  return { name: 'Ausmultiplizieren', felder: [
    { svg: feld({ f: '6', a: '20 − 2', b: '2', ia: '6 · (20 − 2)', ib: '6 · 2', ganz: '6 · 20', weg: true, titel: 'Rechteck mit der Höhe 6 und der Breite 20; ein Streifen der Breite 2 wird weggenommen' }), kopf: 'Zahlen', gl: '<b class="w">6</b> · (20 − 2) = <b class="w">6</b> · 20 − <b class="w">6</b> · 2', satz: 'Das ganze Rechteck ist 6 · 20. Der schraffierte Streifen 6 · 2 kommt weg.' },
    { svg: feld({ f: '3', a: 'x', b: '2', ia: '3 · x', ib: '3 · 2', ganz: '3 · (x + 2)', titel: 'Rechteck mit der Höhe 3, geteilt in die Breiten x und 2' }), kopf: 'mit x', gl: '<b class="w">3</b> · (x + 2) = <b class="w">3</b> · x + <b class="w">3</b> · 2', satz: 'Dieselbe Zeichnung. Nur die Beschriftung ist neu.' },
    { svg: feld({ f: '½', a: '4', b: '⅔', ia: '½ · 4', ib: '½ · ⅔', ganz: '½ · (4 + ⅔)', gr: 18, titel: 'Rechteck mit der Höhe ein halb, geteilt in die Breiten 4 und zwei Drittel' }), kopf: 'mit Brüchen', gl: `<b class="w">${bruch(1, 2)}</b> · (4 + ${bruch(2, 3)}) = <b class="w">${bruch(1, 2)}</b> · 4 + <b class="w">${bruch(1, 2)}</b> · ${bruch(2, 3)}`, satz: 'Und noch einmal dieselbe Zeichnung.' },
  ] };
}

// ---------- 2 Gleichung als Waage ----------
function zWaage() {
  const sack = (x, y, o = {}) => zPfad(`M${x - 9} ${y - 24}q9 5 18 0l-3 6q9 8 5 18h-22q-4 -10 5 -18z`, { fl: o.geist ? 'none' : ZF.blauFl, f: o.geist ? ZF.leise : ZF.tinte, b: 2, strich: o.geist ? '4 4' : null }) + (o.geist ? '' : zT(x, y - 4, 'x', { g: 14, w: 700 }));
  const kugel = (x, y, o = {}) => `<circle cx="${x}" cy="${y}" r="5.5" fill="${o.geist ? 'none' : ZF.tinte}" stroke="${o.geist ? (o.gelb ? ZF.gelb : ZF.leise) : ZF.tinte}" stroke-width="${o.gelb ? 2.5 : 1.75}"${o.geist ? ' stroke-dasharray="3 3"' : ''}/>`;
  const feld = (links, rechts, titel) => { const y = 126, sch = (cx) => zL(cx, 60, cx - 44, y, { b: 1.75, f: ZF.leise }) + zL(cx, 60, cx + 44, y, { b: 1.75, f: ZF.leise }) + zPfad(`M${cx - 50} ${y}H${cx + 50}M${cx - 46} ${y}q46 22 92 0`, { b: 2.5 });
    let l = '', r = ''; let x = 70 - (links.reduce((s, e) => s + (e[0] === 's' ? 24 : 13), 0)) / 2;
    links.forEach((e) => { if (e[0] === 's') { l += sack(x + 12, y - 2, { geist: e[1] === 'g' }); x += 24; } else { l += kugel(x + 6.5, y - 7, { geist: !!e[1], gelb: e[1] === 'y' }); x += 13; } });
    rechts.forEach((e, i) => { const sp = i % 6, ze = Math.floor(i / 6); r += kugel(250 - 32.5 + sp * 13, y - 7 - ze * 13, { geist: !!e[1], gelb: e[1] === 'y' }); });
    return zBlatt(320, 196, `${zL(160, 60, 160, 176, { b: 3 })}${zL(124, 176, 196, 176, { b: 3 })}${zL(70, 60, 250, 60, { b: 3 })}${zP([[160, 48], [152, 62], [168, 62]], { fl: ZF.tinte })}
      ${sch(70)}${sch(250)}${l}${r}${zMarke(160, 112, '=', { breit: 30 })}`, titel); };
  const K = ['k'], Y = ['k', 'y'], G = ['k', 'g'];
  return { name: 'Gleichung als Waage', felder: [
    { svg: feld([['s'], ['s'], K, K], Array(12).fill(K), 'Waage im Gleichgewicht: links zwei Säckchen x und zwei Kugeln, rechts zwölf Kugeln'), gl: '2x + 2 = 12', satz: 'Links und rechts liegt gleich viel.' },
    { svg: feld([['s'], ['s'], Y, Y], [...Array(10).fill(K), Y, Y], 'Auf beiden Seiten werden zwei Kugeln weggenommen'), gl: '2x = 10', satz: 'Auf beiden Seiten 2 Kugeln weg. Die Waage bleibt im Gleichgewicht.', pfeil: 'beide Seiten − 2' },
    { svg: feld([['s'], ['s', 'g']], [...Array(5).fill(K), ...Array(5).fill(G)], 'Beide Seiten werden halbiert: ein Säckchen wiegt so viel wie fünf Kugeln'), gl: 'x = 5', satz: 'Beide Seiten halbiert: Ein Säckchen wiegt so viel wie 5 Kugeln.', pfeil: 'beide Seiten : 2' },
  ] };
}

// ---------- 3 Plus und Minus mit negativen Zahlen ----------
function zZahlenstrahl() {
  const X = (v) => 40 + (v + 1) * 34, ya = 150;
  const feld = (o) => { let s = zL(22, ya, 290, ya, { b: 2 }) + zP([[300, ya], [289, ya - 5], [289, ya + 5]], { fl: ZF.tinte, b: 1 });
    for (let v = -1; v <= 6; v++) s += zL(X(v), ya - 6, X(v), ya + 6, { b: v === 0 ? 2.5 : 1.75 }) + zT(X(v), ya + 24, v < 0 ? '−' + (-v) : v, { g: 14, w: v === 0 ? 800 : 600, f: v === 3 || v === o.ziel ? ZF.tinte : ZF.leise });
    const d = o.blick, x3 = X(3), xz = X(o.ziel), y1 = 56, y2 = 104;
    s += zL(x3, y2 + 10, x3, ya, { f: ZF.leise, b: 1.5, strich: '3 4' }) + zL(xz, y2 + 10, xz, ya, { f: ZF.leise, b: 1.5, strich: '3 4' });
    s += zPfeil(x3, y1, x3 + d * 46, y1, { f: ZF.leise, b: 2.5, strich: '5 4' }) + zT(x3 + d * 20, y1 - 12, o.blickText, { g: 14.5, f: ZF.leise, grotesk: true, w: 600 });
    s += zPfad(`M${x3 + d * 52} ${y1}q${d * 20} ${(y2 - y1) / 2} 0 ${y2 - y1 - 14}`, { f: ZF.tinte, b: 2, strich: '2 4' }) + zT(x3 + d * 70, (y1 + y2) / 2 + 1, 'umdrehen', { g: 14.5, a: d > 0 ? 'start' : 'end', grotesk: true, w: 600 });
    s += zPfeil(x3, y2, xz, y2, { f: ZF.gelb, b: 6, kopf: 14 }) + zT((x3 + xz) / 2, y2 - 11, '2 Schritte', { g: 14.5, grotesk: true });
    s += `<circle cx="${x3}" cy="${ya}" r="5.5" fill="${ZF.tinte}"/><circle cx="${xz}" cy="${ya}" r="8" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="2"/>`;
    return zBlatt(320, 186, s, o.titel); };
  return { name: 'Plus und Minus mit negativen Zahlen', felder: [
    { svg: feld({ blick: 1, ziel: 1, blickText: 'Plus: Blick nach rechts', titel: 'Zahlenstrahl: Start bei 3. Plus schaut nach rechts, das Minus in der Klammer dreht um, zwei Schritte nach links auf 1' }), gl: '3 + (<b class="w">−</b>2) = 1', satz: 'Plus schaut nach rechts. Das Minus in der Klammer dreht um: 2 Schritte nach links.' },
    { svg: feld({ blick: -1, ziel: 5, blickText: 'Minus: Blick nach links', titel: 'Zahlenstrahl: Start bei 3. Minus schaut nach links, das Minus in der Klammer dreht um, zwei Schritte nach rechts auf 5' }), gl: '3 − (<b class="w">−</b>2) = 5', satz: 'Minus schaut nach links. Das Minus in der Klammer dreht um: 2 Schritte nach rechts.' },
  ] };
}

// ---------- 4 Messen heißt auslegen und zählen ----------
function zAuslegen() {
  const k = 34, x0 = 84, y0 = 52; let s = `<rect x="${x0}" y="${y0}" width="${6 * k}" height="${k}" fill="${ZF.blauFl}"/><rect x="${x0}" y="${y0 + 3 * k}" width="${k}" height="${k}" fill="${ZF.gelb}"/>`;
  for (let i = 1; i < 6; i++) s += zL(x0 + i * k, y0, x0 + i * k, y0 + 4 * k, { b: 1.25, f: ZF.leise });
  for (let j = 1; j < 4; j++) s += zL(x0, y0 + j * k, x0 + 6 * k, y0 + j * k, { b: 1.25, f: ZF.leise });
  s += `<rect x="${x0}" y="${y0}" width="${6 * k}" height="${4 * k}" fill="none" stroke="${ZF.tinte}" stroke-width="2.5" stroke-linejoin="round"/>`;
  s += zT(x0 + 3 * k, y0 - 12, '6 Quadrate in einer Reihe', { g: 16, grotesk: true, f: ZF.blau, w: 700 });
  s += zPfad(`M${x0 - 12} ${y0}h-7V${y0 + 4 * k}h7`, { f: ZF.leise, b: 1.75 }) + zT(x0 - 30, y0 + 2 * k, '4 Reihen', { g: 16, grotesk: true, dreh: -90, w: 700 });
  s += zT(x0 + 3 * k, y0 + 4 * k + 24, '6 cm', { g: 17 }) + zT(x0 + 6 * k + 10, y0 + 2 * k + 5, '4 cm', { g: 17, a: 'start' });
  s += zPfad(`M${x0 + k / 2} ${y0 + 4 * k + 4}q0 22 -22 26`, { f: ZF.tinte, b: 1.5 }) + zT(x0 + k / 2 - 28, y0 + 4 * k + 36, '1 cm²', { g: 16, a: 'end', w: 700 });
  return { name: 'Messen heißt auslegen und zählen', felder: [{ svg: zBlatt(360, 250, s, 'Rechteck 6 cm mal 4 cm, ausgelegt mit 24 Einheitsquadraten in 4 Reihen zu je 6'), gl: '4 · 6 = 24 Quadrate, also 24 cm²', satz: 'Ein Quadrat ist 1 cm². In jeder Reihe liegen 6, es sind 4 Reihen.' }] };
}

// ---------- 5 Aus dem Rechteck entsteht jede Fläche ----------
function zFlaechen() {
  const k = 20, B = 130, X = (c) => 30 + c * k, Y = (r) => B - r * k, bl = (innen, titel) => zBlatt(280, 160, innen, titel, k);
  const rechteck = zP([[X(0), Y(0)], [X(6), Y(0)], [X(6), Y(4)], [X(0), Y(4)]], { fl: ZF.blauFl }) + zT(X(3), B + 21, '6', { g: 16 }) + zT(X(6) + 12, Y(2) + 5, '4', { g: 16, a: 'start' });
  const para = zP([[X(2), Y(0)], [X(6), Y(0)], [X(8), Y(4)], [X(2), Y(4)]], { fl: ZF.blauFl, b: 0.01, f: 'none' }) + zP([[X(6), Y(0)], [X(8), Y(0)], [X(8), Y(4)]], { fl: ZF.blauFl, f: ZF.tinte, b: 2, strich: '5 4' })
    + zP([[X(0), Y(0)], [X(2), Y(0)], [X(2), Y(4)]], { fl: ZF.gelb, b: 2 }) + zP([[X(0), Y(0)], [X(6), Y(0)], [X(8), Y(4)], [X(2), Y(4)]]) + zL(X(2), Y(0), X(2), Y(4), { strich: '5 4', b: 2 })
    + zBogenPfeil(X(1.2), Y(1.2), X(7), Y(1.4), 62, { b: 2.25 }) + zT(X(3), B + 21, '6', { g: 16 }) + zSchild(X(2) + 14, Y(2) + 5, '4', { g: 16 });
  const dreieck = zP([[X(6), Y(0)], [X(8), Y(4)], [X(2), Y(4)]], { f: ZF.leise, b: 2, strich: '5 4' }) + zP([[X(0), Y(0)], [X(6), Y(0)], [X(2), Y(4)]], { fl: ZF.blauFl }) + zL(X(2), Y(0), X(2), Y(4), { strich: '5 4', b: 2, f: ZF.tinte })
    + zT(X(3), B + 21, '6', { g: 16 }) + zSchild(X(2) + 14, Y(1.6) + 5, '4', { g: 16 }) + zT(X(5.7), Y(3) + 5, 'Zwilling', { g: 15, grotesk: true, f: ZF.leise, w: 600 });
  const trapez = zP([[X(6), Y(0)], [X(9), Y(0)], [X(11), Y(4)], [X(5), Y(4)]], { f: ZF.leise, b: 2, strich: '5 4' }) + zP([[X(0), Y(0)], [X(6), Y(0)], [X(5), Y(4)], [X(2), Y(4)]], { fl: ZF.blauFl })
    + zL(X(2), Y(0), X(2), Y(4), { strich: '5 4', b: 2 }) + zT(X(3), B + 21, '6', { g: 16 }) + zT(X(7.5), B + 21, '3', { g: 16, f: ZF.leise }) + zT(X(3.5), Y(4) - 8, '3', { g: 16 }) + zSchild(X(2) + 14, Y(1.6) + 5, '4', { g: 16 }) + zT(X(8), Y(3) + 5, 'Zwilling', { g: 15, grotesk: true, f: ZF.leise, w: 600 });
  return { name: 'Aus dem Rechteck entsteht jede Fläche', felder: [
    { svg: bl(rechteck, 'Rechteck 6 mal 4 auf Karopapier'), kopf: 'Rechteck', gl: '6 · 4 = 24', satz: 'Länge mal Breite.' },
    { svg: bl(para, 'Parallelogramm: Das gelbe Dreieck links wird abgeschnitten und rechts angesetzt, es entsteht ein Rechteck 6 mal 4'), kopf: 'Parallelogramm', gl: '6 · 4 = 24', satz: 'Grundseite mal Höhe.', pfeil: 'abschneiden und ansetzen' },
    { svg: bl(dreieck, 'Dreieck mit Grundseite 6 und Höhe 4; mit seinem gedrehten Zwilling ergibt es ein Parallelogramm'), kopf: 'Dreieck', gl: '6 · 4 : 2 = 12', satz: 'Die Hälfte vom Parallelogramm.', pfeil: 'halbieren' },
    { svg: bl(trapez, 'Trapez mit den parallelen Seiten 6 und 3 und der Höhe 4; mit seinem gedrehten Zwilling ergibt es ein Parallelogramm mit der Grundseite 9'), kopf: 'Trapez', gl: '(6 + 3) · 4 : 2 = 18', satz: 'Zwei gleiche Trapeze ergeben ein Parallelogramm. Eines ist die Hälfte.', pfeil: 'auch halbieren' },
  ] };
}

// ---------- 6 Aus dem Quader entsteht jeder Körper ----------
function zKoerper() {
  const ox = 30, oy = -18; // Schrägbild: nach hinten 30 nach rechts, 18 nach oben
  const quaderKanten = (x, y, w, h, o = {}) => { const f = o.f || ZF.tinte, st = o.strich, v = (a, b, c, d, hinten) => zL(a, b, c, d, { f: hinten ? (o.fHinten || ZF.leise) : f, b: hinten ? 1.75 : (o.b || 2.5), strich: hinten ? '4 4' : st });
    return v(x, y, x + ox, y + oy, true) + v(x + ox, y + oy, x + w + ox, y + oy, true) + v(x + ox, y + oy, x + ox, y - h + oy, true)
      + v(x, y, x + w, y) + v(x + w, y, x + w + ox, y + oy) + v(x, y, x, y - h) + v(x + w, y, x + w, y - h) + v(x + w + ox, y + oy, x + w + ox, y - h + oy)
      + v(x, y - h, x + w, y - h) + v(x + w, y - h, x + w + ox, y - h + oy) + v(x, y - h, x + ox, y - h + oy) + v(x + ox, y - h + oy, x + w + ox, y - h + oy); };
  const boden = (x, y, w) => zP([[x, y], [x + w, y], [x + w + ox, y + oy], [x + ox, y + oy]], { fl: ZF.gelb, f: 'none', b: 0.01, deck: 0.85 });
  const hoehe = (x, y, h, s = 'h') => zL(x, y, x, y - h, { f: ZF.blau, b: 2, strich: '5 4' }) + zT(x - 8, y - h / 2 + 5, s, { g: 15, a: 'end', f: ZF.blau, w: 700 });
  const G = (x, y) => zT(x, y, 'G', { g: 15, f: '#11161D', w: 800 });
  // Quader mit Schichten
  let q = boden(60, 176, 130);
  for (const i of [1, 2]) q += zP([[60, 176 - i * 34], [190, 176 - i * 34], [190 + ox, 176 - i * 34 + oy], [60 + ox, 176 - i * 34 + oy]], { f: ZF.leise, b: 1.5, strich: '2 4' });
  q += quaderKanten(60, 176, 130, 102) + G(140, 172) + hoehe(46, 176, 102) + zT(232, 132, 'Schicht', { g: 14.5, grotesk: true, f: ZF.leise, a: 'start', w: 500 }) + zT(232, 149, 'auf Schicht', { g: 14.5, grotesk: true, f: ZF.leise, a: 'start', w: 500 });
  // Prisma (dreieckige Grundfläche) und Zylinder
  const pA = [24, 178], pB = [112, 178], pC = [86, 150], ph = 100, hoch = (p) => [p[0], p[1] - ph];
  let p = zP([pA, pB, pC], { fl: ZF.gelb, f: 'none', b: 0.01, deck: 0.85 }) + zL(...pA, ...pC, { f: ZF.leise, b: 1.75, strich: '4 4' }) + zL(...pB, ...pC, { f: ZF.leise, b: 1.75, strich: '4 4' }) + zL(...pC, ...hoch(pC), { f: ZF.leise, b: 1.75, strich: '4 4' });
  for (const i of [1, 2]) p += zP([pA, pB, pC].map((e) => [e[0], e[1] - i * ph / 3]), { f: ZF.leise, b: 1.5, strich: '2 4' });
  p += zL(...pA, ...pB) + zL(...pA, ...hoch(pA)) + zL(...pB, ...hoch(pB)) + zP([hoch(pA), hoch(pB), hoch(pC)]) + G(74, 172);
  const cx = 226, rx = 50, ry = 15, cyU = 172, cyO = 72;
  p += `<ellipse cx="${cx}" cy="${cyU}" rx="${rx}" ry="${ry}" fill="${ZF.gelb}" fill-opacity=".85"/>` + zPfad(`M${cx - rx} ${cyU}A${rx} ${ry} 0 0 1 ${cx + rx} ${cyU}`, { f: ZF.leise, b: 1.75, strich: '4 4' }) + zPfad(`M${cx - rx} ${cyU}A${rx} ${ry} 0 0 0 ${cx + rx} ${cyU}`);
  for (const i of [1, 2]) p += `<ellipse cx="${cx}" cy="${cyU - i * 100 / 3}" rx="${rx}" ry="${ry}" fill="none" stroke="${ZF.leise}" stroke-width="1.5" stroke-dasharray="2 4"/>`;
  p += zL(cx - rx, cyU, cx - rx, cyO) + zL(cx + rx, cyU, cx + rx, cyO) + `<ellipse cx="${cx}" cy="${cyO}" rx="${rx}" ry="${ry}" fill="none" stroke="${ZF.tinte}" stroke-width="2.5"/>` + G(cx, cyU + 5) + hoehe(160, 178, 100);
  // Pyramide im Quader, Kegel im Zylinder
  const bx = 22, by = 180, bw = 92, bh = 100, sp = [bx + bw / 2 + ox / 2, by - bh + oy / 2];
  let d = boden(bx, by, bw) + quaderKanten(bx, by, bw, bh, { f: ZF.leise, b: 1.5, strich: '2 4', fHinten: ZF.leise });
  d += zL(bx + ox, by + oy, ...sp, { f: ZF.leise, b: 1.75, strich: '4 4' }) + zL(bx, by, bx + ox, by + oy, { f: ZF.leise, b: 1.75, strich: '4 4' }) + zL(bx + ox, by + oy, bx + bw + ox, by + oy, { f: ZF.leise, b: 1.75, strich: '4 4' });
  d += zL(bx, by, bx + bw, by) + zL(bx + bw, by, bx + bw + ox, by + oy) + zL(bx, by, ...sp) + zL(bx + bw, by, ...sp) + zL(bx + bw + ox, by + oy, ...sp) + G(bx + bw / 2 + 12, by - 4);
  const kx = 236, kr = 46, kry = 14, kU = 172, kO = 72;
  d += `<ellipse cx="${kx}" cy="${kU}" rx="${kr}" ry="${kry}" fill="${ZF.gelb}" fill-opacity=".85"/>` + zPfad(`M${kx - kr} ${kU}A${kr} ${kry} 0 0 1 ${kx + kr} ${kU}`, { f: ZF.leise, b: 1.75, strich: '4 4' }) + zPfad(`M${kx - kr} ${kU}A${kr} ${kry} 0 0 0 ${kx + kr} ${kU}`);
  d += zL(kx - kr, kU, kx - kr, kO, { f: ZF.leise, b: 1.5, strich: '2 4' }) + zL(kx + kr, kU, kx + kr, kO, { f: ZF.leise, b: 1.5, strich: '2 4' }) + `<ellipse cx="${kx}" cy="${kO}" rx="${kr}" ry="${kry}" fill="none" stroke="${ZF.leise}" stroke-width="1.5" stroke-dasharray="2 4"/>`;
  d += zL(kx - kr, kU, kx, kO) + zL(kx + kr, kU, kx, kO) + G(kx - 20, kU + 6) + zL(kx, kU, kx, kO, { f: ZF.blau, b: 2, strich: '5 4' }) + zT(kx + 8, 130, 'h', { g: 15, a: 'start', f: ZF.blau, w: 700 });
  return { name: 'Aus dem Quader entsteht jeder Körper', felder: [
    { svg: zBlatt(320, 206, q, 'Quader im Schrägbild, Grundfläche gelb, darüber Schichten bis zur Höhe h'), kopf: 'Quader', gl: 'Volumen = <b class="w">G</b> · h', satz: 'Auf der Grundfläche liegt eine Schicht. Davon stapelt man so viele, wie der Körper hoch ist.' },
    { svg: zBlatt(320, 206, p, 'Dreiecksprisma und Zylinder im Schrägbild, Grundfläche gelb, gleiche Höhe'), kopf: 'Prisma und Zylinder', gl: 'Volumen = <b class="w">G</b> · h', satz: 'Andere Grundfläche, gleiches Stapeln.', pfeil: 'andere Grundfläche' },
    { svg: zBlatt(320, 206, d, 'Pyramide in ihrem Quader und Kegel in seinem Zylinder, Grundfläche gelb'), kopf: 'Pyramide und Kegel', gl: `Volumen = ${bruch(1, 3)} · <b class="w">G</b> · h`, satz: 'Die Spitze füllt genau ein Drittel des Körpers darum.', pfeil: 'ein Drittel' },
  ] };
}

const ZEICHNUNGEN = { R6: zAusmultiplizieren, R13: zWaage, R2: zZahlenstrahl, 'I-fur-1': zAuslegen, 'I-fur-2': zFlaechen, 'I-fur-3': zKoerper };
// Baut eine Zeichnung als Folge von Feldern mit Rechnung und Satz darunter.
function zeichnung(schluessel, o = {}) {
  const z = ZEICHNUNGEN[schluessel]?.(); if (!z) return '';
  return `<figure class="zeichnung${o.klein ? ' klein' : ''}" data-felder="${z.felder.length}"><div class="z-reihe">${z.felder.map((f, i) => `${i ? `<div class="z-pfeil${f.pfeil ? '' : ' leer'}" aria-hidden="true"></div>` : ''}<div class="z-teil">${f.pfeil ? `<p class="z-schritt">${f.pfeil}</p>` : ''}${f.kopf ? `<p class="z-kopf">${f.kopf}</p>` : ''}${f.svg}${o.klein ? '' : `<p class="z-gl">${f.gl}</p><p class="z-satz">${f.satz}</p>`}</div>`).join('')}</div></figure>`;
}
// Nur das erste Feld, ohne Text: als kleines Bild in der Übersicht.
function zeichnungKlein(schluessel, feld = 0) { const z = ZEICHNUNGEN[schluessel]?.(); return z ? `<div class="z-mini">${z.felder[feld].svg}</div>` : ''; }
