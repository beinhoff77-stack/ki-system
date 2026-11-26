// Zeichnungen, dritte Runde: die 19 tragenden Ideen der Planeten Zahlen, Algebra, Geld und Verhältnisse, Funktionen, Daten und Zufall
// (Vorgaben: zeichen-vorgaben-fuenf-planeten.md) und die zwei Nebenfelder zu Rechenregel 10.
const zPunkt = (x, y, o = {}) => (o.gelb ? `<circle cx="${x}" cy="${y}" r="10" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.5"/>` : '') + `<circle cx="${x}" cy="${y}" r="${o.r || 5}" fill="${o.offen ? ZF.papier : ZF.tinte}" stroke="${ZF.tinte}" stroke-width="2.5"/>`;
// Zahlengerade: von a bis b, X(v) = x0 + (v - a) * e
function zStrahl(x0, y, a, b, e, o = {}) { const X = (v) => x0 + (v - a) * e; let s = zL(x0 - 14, y, X(b) + 12, y, { b: o.b || 2 }) + (o.ohnePfeil ? '' : zP([[X(b) + 22, y], [X(b) + 11, y - 5], [X(b) + 11, y + 5]], { fl: ZF.tinte, b: 1 }));
  for (let v = a; v <= b; v += o.schritt || 1) s += zL(X(v), y - 6, X(v), y + 6, { b: v === 0 && !o.nullGleich ? 3 : 1.75 }) + (o.ohneZahl ? '' : zT(X(v), y + 24, (o.text || ((n) => String(n).replace('-', '−')))(v), { g: o.g || 15, w: v === 0 ? 800 : 600, f: (o.fett || []).includes(v) || v === 0 ? ZF.tinte : ZF.leise }));
  return { s, X }; }
// Koordinatensystem mit Gitter; liefert X, Y und die Zeichnung der Achsen
function zKoord(x0, y0, ex, ey, xa, xb, ya, yb, o = {}) { const X = (v) => x0 + (v - xa) * ex, Y = (v) => y0 - (v - ya) * ey; let s = '';
  for (let v = xa; v <= xb; v += o.sx || 1) s += zL(X(v), Y(ya), X(v), Y(yb), { b: 0.75, f: ZF.karo }); for (let v = ya; v <= yb; v += o.sy || 1) s += zL(X(xa), Y(v), X(xb), Y(v), { b: 0.75, f: ZF.karo });
  s += zPfeil(X(xa), Y(0), X(xb) + 12, Y(0), { b: 2, kopf: 8 }) + zPfeil(X(0), Y(ya), X(0), Y(yb) - 12, { b: 2, kopf: 8 }) + zT(X(xb) + 10, Y(0) + 18, 'x', { g: 14, w: 700 }) + zT(X(0) - 12, Y(yb) - 6, 'y', { g: 14, w: 700 });
  for (const v of o.zx || []) s += zL(X(v), Y(0) - 4, X(v), Y(0) + 4, { b: 1.75 }) + zT(X(v), Y(0) + 19, String(v).replace('-', '−'), { g: 14, f: ZF.leise });
  for (const v of o.zy || []) s += zL(X(0) - 4, Y(v), X(0) + 4, Y(v), { b: 1.75 }) + zT(X(0) - 9, Y(v) + 5, String(v).replace('-', '−'), { g: 14, a: 'end', f: ZF.leise });
  return { s, X, Y }; }
const zKurve = (K, f, a, b, o = {}) => { let d = ''; for (let i = 0; i <= 60; i++) { const x = a + (b - a) * i / 60; d += `${i ? 'L' : 'M'}${K.X(x).toFixed(1)} ${K.Y(f(x)).toFixed(1)}`; } return zPfad(d, { b: o.b || 3, f: o.f }); };
const zHaken = (x, y) => zPfad(`M${x - 7} ${y}l5 6l9 -12`, { b: 3 }), zKreuz = (x, y) => zPfad(`M${x - 6} ${y - 6}l12 12M${x + 6} ${y - 6}l-12 12`, { b: 2.5, f: ZF.leise });
const zHundert = (x0, y0, k, voll) => { let s = ''; for (let c = 0; c < 10; c++) for (let r = 0; r < 10; r++) if (voll(c, r)) s += `<rect x="${x0 + c * k}" y="${y0 + r * k}" width="${k}" height="${k}" fill="${ZF.blauFl}"/>`;
  for (let i = 0; i <= 10; i++) s += zL(x0 + i * k, y0, x0 + i * k, y0 + 10 * k, { b: i % 10 ? 1 : 2.5, f: i % 10 ? ZF.leise : ZF.tinte }) + zL(x0, y0 + i * k, x0 + 10 * k, y0 + i * k, { b: i % 10 ? 1 : 2.5, f: i % 10 ? ZF.leise : ZF.tinte }); return s; };

// ---------- Zahlen 1 · Zahlengerade ----------
function zOrdnung() {
  const G = zStrahl(30, 96, -3, 3, 43, { fett: [] }); let s = G.s; for (let v = -2.5; v <= 2.5; v += 1) s += zL(G.X(v), 91, G.X(v), 101, { b: 1.25 });
  for (const [v, t, hv] of [[-2.5, '−2,5', 1], [-1, '−1', 1], [0.5, '½', 0], [2, '2', 0]]) s += zPunkt(G.X(v), 96, { gelb: hv }) + (hv ? zMarke(G.X(v), 62, t, { breit: t.length * 11 + 14 }) : zT(G.X(v), 68, t, { g: t === '½' ? 22 : 17, w: 800 }));
  s += zPfeil(40, 146, 280, 146, { b: 2.5, kopf: 11 }) + zT(160, 168, 'nach rechts wird es größer', { g: 15, grotesk: true, w: 700 });
  return { name: 'Zahlengerade', felder: [{ svg: zBlatt(320, 180, s, 'Zahlengerade von minus 3 bis 3 mit den Punkten minus 2,5, minus 1, ein halb und 2. Minus 2,5 liegt links von minus 1. Ein langer Pfeil zeigt nach rechts: nach rechts wird es größer'), gl: `${W('−2,5 < −1')} < ½ < 2`, satz: 'Die −2,5 liegt weiter links als die −1, ist also kleiner – obwohl 2,5 mehr ist als 1.' }] };
}
// ---------- Zahlen 2 · Bündeln in Zehnern ----------
function zBuendeln() {
  const tausch = (y) => zPfeil(160, y, 160, y + 30, { b: 2.5, kopf: 10 }) + zMarke(202, y + 15, '10', { breit: 38 });
  let a = zT(160, 22, '10 Einer', { g: 15, grotesk: true, w: 700 }); for (let i = 0; i < 10; i++) a += zKasten(64 + i * 19.6, 32, 15, 15, { rx: 2, fl: ZF.blauFl, b: 2 }) + zKasten(64 + i * 19.1, 100, 19.1, 19, { rx: 0, fl: ZF.blauFl, b: 2 });
  a += tausch(58) + zT(160, 144, '1 Zehner', { g: 15, grotesk: true, w: 700 });
  let b = zT(160, 22, '1 Einer', { g: 15, grotesk: true, w: 700 }) + zKasten(64, 30, 191, 22, { rx: 0, fl: ZF.blauFl }) + tausch(60); for (let i = 0; i < 10; i++) b += zKasten(64 + i * 19.1, 100, 19.1, 22, { rx: 0, fl: ZF.blauFl, b: 2 });
  b += zT(160, 146, '10 Zehntel', { g: 15, grotesk: true, w: 700 });
  return { name: 'Bündeln in Zehnern', felder: [
    { svg: zBlatt(320, 158, a, 'Zehn einzelne Einerwürfel, ein Pfeil mit der Zahl 10, darunter eine Zehnerstange aus zehn Würfeln, gleich lang'), kopf: 'Nach links: größer', gl: '10 Einer = 1 Zehner', satz: 'Zehn gleiche werden zu einem von der nächsten Sorte.' },
    { svg: zBlatt(320, 158, b, 'Ein Einer als Streifen, ein Pfeil mit der Zahl 10, darunter derselbe Streifen in zehn gleiche Zehntel geschnitten'), kopf: 'Nach rechts: feiner', gl: '1 Einer = 10 Zehntel', satz: 'Derselbe Tausch in die andere Richtung, auch hinter dem Komma.', pfeil: 'derselbe Tausch' },
  ] };
}
// ---------- Zahlen 3 · Bausteine: zwei Bäume für 60 ----------
function zBausteine() {
  const baum = (x, m, l1, l2) => { const kn = (px, py, t, prim) => (prim ? `<circle cx="${px}" cy="${py}" r="15" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="2"/>` : '') + zT(px, py + 6, t, { g: 18, w: 800, f: prim ? '#11161D' : ZF.tinte });
    const ast = (x1, y1, x2, y2) => zL(x1, y1 + 10, x2, y2 - 17, { b: 2 });
    return ast(x, 22, x - 38, 78) + ast(x, 22, x + 38, 78) + ast(x - 38, 78, x - 58, 136) + ast(x - 38, 78, x - 20, 136) + ast(x + 38, 78, x + 20, 136) + ast(x + 38, 78, x + 58, 136)
      + kn(x, 24, '60') + kn(x - 38, 80, m[0]) + kn(x + 38, 80, m[1]) + kn(x - 58, 138, l1[0], 1) + kn(x - 20, 138, l1[1], 1) + kn(x + 20, 138, l2[0], 1) + kn(x + 58, 138, l2[1], 1); };
  return { name: 'Bausteine', felder: [{ svg: zBlatt(320, 166, baum(82, ['6', '10'], ['2', '3'], ['2', '5']) + baum(238, ['4', '15'], ['2', '2'], ['3', '5']) + zL(160, 14, 160, 152, { b: 1.25, f: ZF.leise, strich: '3 5' }), 'Zwei Zerlegungsbäume für 60. Links: 6 mal 10, dann 2, 3, 2, 5. Rechts: 4 mal 15, dann 2, 2, 3, 5. Die Primzahlen stehen in Kreisen, in beiden Bäumen dieselben vier'), gl: `60 = ${W('2 · 2 · 3 · 5')}`, satz: 'Zwei Wege, dieselben vier Bausteine. In den Kreisen stehen nur Primzahlen.' }] };
}
// ---------- Zahlen 4 · Schreibweisen: ½ = 0,5 = 50 % ----------
function zSchreibweisen() {
  const x0 = 50, l = 230; let a = `<rect x="${x0}" y="24" width="${l / 2}" height="34" fill="${ZF.blauFl}"/>` + zKasten(x0, 24, l, 34, { rx: 0, fl: 'none' }) + zL(x0 + l / 2, 24, x0 + l / 2, 58, { b: 2 });
  const G = zStrahl(x0, 120, 0, 10, l / 10, { ohneZahl: 1, ohnePfeil: 1, nullGleich: 1 }); a += G.s + zT(x0, 144, '0', { g: 15, w: 700 }) + zT(x0 + l, 144, '1', { g: 15, w: 700 }) + zT(x0 + l / 2, 146, '0,5', { g: 17, w: 800 });
  a += zL(x0 + l / 2, 14, x0 + l / 2, 120, { f: ZF.gelb, b: 8 }) + zL(x0 + l / 2, 14, x0 + l / 2, 120, { b: 2.5, strich: '6 4' }) + zPunkt(x0 + l / 2, 120) + zBruchT(24, 38, 1, 2, 18);
  const b = zHundert(85, 10, 15, (c) => c < 5);
  return { name: 'Schreibweisen', felder: [
    { svg: zBlatt(320, 158, a, 'Ein Streifen, zur Hälfte gefärbt, und genau darunter eine Zahlengerade von 0 bis 1 in Zehnteln mit einem Punkt bei 0,5. Die Färbung endet genau über dem Punkt'), kopf: 'Bruch und Dezimalzahl', gl: `${bruch(1, 2)} = 0,5`, satz: 'Die Färbung des Streifens endet genau über dem Punkt 0,5.' },
    { svg: zBlatt(320, 170, b, 'Hunderterfeld aus 10 mal 10 Feldern, fünf volle Spalten gefärbt: 50 von 100'), kopf: 'Prozent', gl: `${bruch(1, 2)} = 0,5 = 50 %`, satz: '50 von 100 Feldern: wieder genau die Hälfte.', pfeil: 'dieselbe Zahl' },
  ] };
}
// ---------- Zahlen 5 · Hoch und zurück ----------
function zHochZurueck() {
  const k = 32, x0 = 178, y0 = 44; let s = `<rect x="${x0}" y="${y0}" width="${3 * k}" height="${3 * k}" fill="${ZF.blauFl}"/>`; for (let i = 1; i < 3; i++) s += zL(x0 + i * k, y0, x0 + i * k, y0 + 3 * k, { b: 1.25, f: ZF.leise }) + zL(x0, y0 + i * k, x0 + 3 * k, y0 + i * k, { b: 1.25, f: ZF.leise });
  s += zKasten(x0, y0, 3 * k, 3 * k, { rx: 0, fl: 'none' }) + zSchild(x0 + 1.5 * k, y0 + 1.5 * k + 7, '9', { g: 22, w: 800 }) + zPfad(`M${x0 - 8} ${y0}h-6v${3 * k}h6`, { b: 1.75, f: ZF.leise }) + zT(46, y0 + 1.5 * k + 9, '3', { g: 26, w: 800 }) + zT(x0 - 22, y0 + 1.5 * k + 6, '3', { g: 16 });
  s += zBogenPfeil(62, y0 + 30, x0 - 34, y0 + 30, 50, { b: 2.5 }) + zMarke(106, y0 + 2, 'hoch 2', { breit: 70, g: 15 }) + zBogenPfeil(x0 - 34, y0 + 70, 62, y0 + 70, -50, { b: 2.5 }) + zMarke(106, y0 + 98, 'Wurzel', { breit: 70, g: 15 });
  return { name: 'Hoch und zurück', felder: [{ svg: zBlatt(320, 180, s, 'Quadrat aus 3 mal 3 Einheitsquadraten, Fläche 9. Ein Pfeil hoch 2 führt von der Seitenlänge 3 zur Fläche 9, ein Pfeil Wurzel führt zurück'), gl: `3² = 9<br>√9 = 3`, satz: 'Hin: Seite 3, Fläche 9. Zurück: Fläche 9, Seite 3. Die beiden Pfeile gehören zusammen.' }] };
}
// ---------- Algebra 1 · Term: zwei Rechenketten, dieselben Ausgaben ----------
function zTerm() {
  const kette = (y, titel, schritte) => { const n = schritte.length, bw = 38, pw = (300 - (n + 1) * bw) / n; let s = zT(10, y - 30, titel, { g: 16, a: 'start', w: 800 });
    for (let i = 0; i <= n; i++) { const x = 10 + i * (bw + pw); s += zKasten(x, y - 17, bw, 34, { fl: i ? ZF.papier : ZF.blauFl }) + (i ? '' : zT(x + bw / 2, y + 6, 'x', { g: 18, w: 800 })) + (i === n ? zT(x + bw / 2, y + 6, '?', { g: 16, f: ZF.leise }) : '');
      if (i < n) s += zPfeil(x + bw + 4, y, x + bw + pw - 4, y, { b: 2, kopf: 8 }) + zT(x + bw + pw / 2, y - 9, schritte[i], { g: 14, w: 800 }); } return s; };
  const a = kette(52, '2 · x + 3', ['· 2', '+ 3']) + kette(136, '2 · (x + 1) + 1', ['+ 1', '· 2', '+ 1']);
  const sp = [10, 60, 170, 310], zl = [['1', '5', '5'], ['2', '7', '7'], ['5', '13', '13']]; let t = `<rect x="${sp[1]}" y="12" width="${sp[3] - sp[1]}" height="156" fill="${ZF.gelb}" fill-opacity=".45"/>`;
  t += zKasten(10, 12, 300, 156, { rx: 0, fl: 'none' }) + zL(sp[1], 12, sp[1], 168, { b: 1.5 }) + zL(sp[2], 12, sp[2], 168, { b: 1.5 }) + zL(10, 48, 310, 48, { b: 2.5 }) + zL(10, 88, 310, 88, { b: 1, f: ZF.leise }) + zL(10, 128, 310, 128, { b: 1, f: ZF.leise });
  t += zT(35, 36, 'x', { g: 15, w: 800 }) + zT(115, 36, '2 · x + 3', { g: 14, w: 700 }) + zT(240, 36, '2 · (x + 1) + 1', { g: 14, w: 700 }) + `<rect x="${sp[1]}" y="12" width="${sp[3] - sp[1]}" height="156" fill="none" stroke="${ZF.tinte}" stroke-width="4"/>`;
  zl.forEach((z, i) => { t += zT(35, 76 + i * 40, z[0], { g: 18, w: 700 }) + zT(115, 76 + i * 40, z[1], { g: 19, w: 800 }) + zT(240, 76 + i * 40, z[2], { g: 19, w: 800 }); });
  return { name: 'Term', felder: [
    { svg: zBlatt(320, 166, a, 'Zwei Rechenketten. Kette 1: x, mal 2, plus 3. Kette 2: x, plus 1, mal 2, plus 1'), kopf: 'Zwei Rezepte', gl: '2 · x + 3 und 2 · (x + 1) + 1', satz: 'Zahl hinein, Schritt für Schritt rechnen, Ergebnis heraus. Die Klammer kommt zuerst.' },
    { svg: zBlatt(320, 180, t, 'Tabelle mit x gleich 1, 2 und 5. Beide Rechenketten liefern 5, 7 und 13 – Zeile für Zeile dieselbe Zahl'), kopf: 'Dieselben Ergebnisse', gl: `2 · x + 3 = 2 · (x + 1) + 1`, satz: 'Zeile für Zeile dieselbe Zahl: Die beiden Terme sind gleichwertig.', pfeil: 'einsetzen' },
  ] };
}
// ---------- Algebra 2 · Erlaubte Zahlen: Loch bei 2 ----------
function zErlaubt() {
  const G = zStrahl(40, 112, -1, 5, 40, { b: 4 }); let s = zT(160, 28, '1 : (x − 2)', { g: 19, w: 800 }) + G.s + `<circle cx="${G.X(2)}" cy="112" r="11" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.5"/><circle cx="${G.X(2)}" cy="112" r="6.5" fill="${ZF.papier}" stroke="${ZF.tinte}" stroke-width="2.5"/>`;
  s += zL(G.X(2), 98, G.X(2), 84, { b: 1.5 }) + zT(160, 58, 'x = 2 ist nicht erlaubt:', { g: 15, grotesk: true, w: 700 }) + zT(160, 77, 'Der Nenner wäre 0', { g: 15, grotesk: true, w: 700 });
  const sp = [20, 113, 206, 300]; s += zKasten(20, 156, 280, 64, { rx: 0, fl: 'none', b: 2 }) + zL(113, 156, 113, 220, { b: 1.25 }) + zL(206, 156, 206, 220, { b: 1.25 }) + zL(20, 186, 300, 186, { b: 1.25 });
  [['x = 1', '−1'], ['x = 2', 'geht nicht'], ['x = 3', '1']].forEach((z, i) => { const x = (sp[i] + sp[i + 1]) / 2; s += zT(x, 177, z[0], { g: 15, w: 700 }) + (i === 1 ? zT(x, 208, z[1], { g: 14, grotesk: true, w: 700 }) : zT(x, 209, z[1], { g: 18, w: 800 })); });
  return { name: 'Erlaubte Zahlen', felder: [{ svg: zBlatt(320, 232, s, 'Zahlengerade von minus 1 bis 5, durchgezogen, nur bei 2 ein offener Ring. Darüber der Term 1 geteilt durch x minus 2. Tabelle: x gleich 1 ergibt minus 1, x gleich 2 geht nicht, x gleich 3 ergibt 1'), gl: `1 : (x − 2) für x ≠ ${W('2')}`, satz: 'Überall ist die Gerade durchgezogen, nur bei 2 ist ein Loch: Dort müsste man durch null teilen.' }] };
}
// ---------- Algebra 3 · Gleichung lösen: einsetzen und prüfen ----------
function zEinsetzen() {
  const G = zStrahl(46, 78, 2, 7, 46, { nullGleich: 1, fett: [5] }); let s = zT(160, 30, '2 · x + 2 = 12', { g: 19, w: 800 }) + G.s;
  [[3, '8'], [4, '10'], [5, '12'], [6, '14']].forEach(([v, t]) => { const x = G.X(v), ok = v === 5; s += (ok ? `<rect x="${x - 20}" y="112" width="40" height="62" rx="9" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.75"/>` : '') + zT(x, 136, t, { g: 18, w: 800, f: ok ? '#11161D' : ZF.tinte }) + (ok ? zHaken(x - 1, 158).replace(/stroke="[^"]*"/, 'stroke="#11161D"') : zKreuz(x, 158)); });
  s += zPunkt(G.X(5), 78, { gelb: 1 });
  return { name: 'Gleichung lösen', felder: [{ svg: zBlatt(320, 186, s, 'Zahlengerade von 2 bis 7. Unter 3 steht 8 mit Kreuz, unter 4 steht 10 mit Kreuz, unter 5 steht 12 mit Haken, unter 6 steht 14 mit Kreuz'), gl: `Lösung: ${W('x = 5')}`, satz: 'Unter jeder Zahl steht, was links herauskommt, wenn man sie einsetzt. Nur bei 5 stimmt die Gleichung.' }] };
}
// ---------- Algebra 4 · Höherer Grad: null auf eine Seite, zerlegen ----------
function zHoeherGrad() {
  const null0 = (x, y) => `<rect x="${x - 12}" y="${y - 19}" width="24" height="26" rx="6" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.5"/>` + zT(x, y, '0', { g: 18, w: 800, f: '#11161D' });
  let a = zT(160, 30, 'x² + x = 6', { g: 18, w: 800 }) + zPfeil(160, 40, 160, 62, { b: 2, kopf: 8 }) + zT(172, 56, '− 6 auf beiden Seiten', { g: 14, a: 'start', grotesk: true, w: 700 }).replace('x="172"', 'x="170"');
  a += zT(148, 88, 'x² + x − 6 =', { g: 18, w: 800 }) + null0(232, 88) + zPfeil(160, 98, 160, 120, { b: 2, kopf: 8 }) + zT(170, 114, 'zerlegen', { g: 14, a: 'start', grotesk: true, w: 700 });
  a += zKasten(34, 130, 92, 38, { fl: ZF.blauFl, rx: 8 }) + zT(80, 155, 'x − 2', { g: 17, w: 800 }) + zT(139, 156, '·', { g: 20, w: 800 }) + zKasten(152, 130, 92, 38, { fl: ZF.blauFl, rx: 8 }) + zT(198, 155, 'x + 3', { g: 17, w: 800 }) + zT(260, 155, '=', { g: 18, w: 800 }) + null0(288, 155);
  a += zPfeil(80, 172, 80, 190, { b: 1.75, kopf: 7 }) + zPfeil(198, 172, 198, 190, { b: 1.75, kopf: 7 }) + zT(80, 214, 'x = 2', { g: 18, w: 800 }) + zT(139, 213, 'oder', { g: 15, grotesk: true, w: 700 }) + zT(204, 214, 'x = −3', { g: 18, w: 800 });
  const K = zKoord(34, 204, 37, 17, -4, 3, -7, 4, { zx: [-2, -1, 1], zy: [-6, -4, -2, 2] }); const f = (x) => x * x + x - 6;
  let b = K.s + zKurve(K, f, -3.7, 2.7) + zPunkt(K.X(-3), K.Y(0), { gelb: 1 }) + zPunkt(K.X(2), K.Y(0), { gelb: 1 }) + zSchild(K.X(-3) + 22, K.Y(0) - 14, '−3', { g: 16, w: 800 }) + zSchild(K.X(2) - 18, K.Y(0) - 14, '2', { g: 16, w: 800 }) + zPunkt(K.X(-0.5), K.Y(-6.25), { r: 3.5 });
  return { name: 'Höherer Grad', felder: [
    { svg: zBlatt(320, 228, a, 'Drei Rechenzeilen: x Quadrat plus x gleich 6; minus 6 auf beiden Seiten; x Quadrat plus x minus 6 gleich 0; zerlegen in die Kästen x minus 2 mal x plus 3 gleich 0. Darunter x gleich 2 oder x gleich minus 3'), kopf: 'Null auf eine Seite, dann zerlegen', gl: `(x − 2) · (x + 3) = ${W('0')}`, satz: 'Erst steht rechts die Null. Dann liefert jeder Kasten eine Lösung – die eine oder die andere.' },
    { svg: zBlatt(320, 232, b, 'Parabel im Koordinatensystem, sie schneidet die x-Achse bei minus 3 und bei 2 und die y-Achse bei minus 6'), kopf: 'Dasselbe als Bild', gl: 'y = x² + x − 6', satz: 'Die Parabel schneidet die x-Achse genau bei −3 und bei 2: Das sind die beiden Lösungen.', pfeil: 'als Graph' },
  ] };
}
// ---------- Geld und Verhältnisse 1 · Größe: 3 m = 30 dm ----------
function zGroesse() {
  const x0 = 40, l = 240; let s = zKasten(x0, 70, l, 26, { rx: 0, fl: ZF.blauFl });
  s += zL(x0, 50, x0 + l, 50, { b: 2 }) + zL(x0, 116, x0 + l, 116, { b: 2 }); for (let i = 0; i <= 3; i++) s += zL(x0 + i * 80, 40, x0 + i * 80, 60, { b: 2.5 }); for (let i = 0; i <= 30; i++) s += zL(x0 + i * 8, 108, x0 + i * 8, i % 10 ? 122 : 128, { b: i % 10 ? 1.25 : 2.5 });
  for (let i = 0; i < 3; i++) s += zT(x0 + 40 + i * 80, 34, '1 m', { g: 14, f: ZF.leise }) + zT(x0 + 40 + i * 80, 146, '10 dm', { g: 14, f: ZF.leise });
  s += zMarke(20, 50, '3', { breit: 28 }).replace(/x="6"/, 'x="4"') + zMarke(20, 116, '30', { breit: 34 }) + zT(302, 55, 'm', { g: 15, w: 700 }) + zT(302, 121, 'dm', { g: 15, w: 700 });
  return { name: 'Größe', felder: [{ svg: zBlatt(320, 160, s, 'Ein Balken von 3 Metern Länge. Darüber ein Maßband in Metern mit 3 Abschnitten, darunter eines in Dezimetern mit 30 Abschnitten; je 10 untere passen unter einen oberen'), gl: `${W('3')} m = ${W('30')} dm = 300 cm`, satz: 'Dieselbe Länge: Mit der kleineren Einheit braucht man mehr davon.' }] };
}
// ---------- Geld und Verhältnisse 2 · Wert für eins: doppelte Zahlengerade ----------
function zDoppelgerade() {
  const X = (v) => 22 + v * 46, yo = 86, yu = 150, pr = ['0', '2,50', '5', '7,50', '10', '12,50', '15']; let s = `<rect x="${X(1) - 22}" y="${yo - 32}" width="44" height="${yu - yo + 62}" rx="9" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.75"/>`;
  s += zL(X(0), yo, X(6) + 12, yo, { b: 2 }) + zL(X(0), yu, X(6) + 12, yu, { b: 2 });
  for (let v = 0; v <= 6; v++) s += zL(X(v), yo, X(v), yu, { b: 1, f: ZF.leise, strich: '2 4' }) + zL(X(v), yo - 6, X(v), yo + 6, { b: 2 }) + zL(X(v), yu - 6, X(v), yu + 6, { b: 2 }) + zT(X(v), yo - 12, v, { g: 15, w: 800, f: v === 1 ? '#11161D' : ZF.tinte }) + zT(X(v), yu + 23, pr[v], { g: 14, w: 700, f: v === 1 ? '#11161D' : ZF.tinte });
  s += zT(310, yo - 12, 'kg', { g: 14, w: 700, a: 'end' }).replace(`y="${yo - 12}"`, `y="${yo + 20}"`) + zT(310, yu - 10, '€', { g: 14, w: 700, a: 'end' });
  s += zBogenPfeil(X(3), yo - 30, X(6), yo - 30, 44, { b: 2.25 }) + zMarke(X(4.5), yo - 62, '· 2', { breit: 44, g: 15 }) + zBogenPfeil(X(3), yu + 32, X(6), yu + 32, -44, { b: 2.25 }) + zMarke(X(4.5), yu + 64, '· 2', { breit: 44, g: 15 });
  return { name: 'Wert für eins', felder: [{ svg: zBlatt(320, 236, s, 'Doppelte Zahlengerade: oben 0 bis 6 Kilogramm, unten 0 bis 15 Euro, beide beginnen bei 0 genau übereinander. 1 Kilogramm und 2,50 Euro sind hervorgehoben. Von 3 nach 6 Kilogramm mal 2, von 7,50 nach 15 Euro mal 2'), gl: `1 kg kostet ${W('2,50 €')}`, satz: 'Der Wert für eins bleibt immer gleich. Darum: doppelte Menge, doppelter Preis.' }] };
}
// ---------- Geld und Verhältnisse 3 · Prozent: von hundert ----------
function zProzent() {
  const a = zHundert(85, 10, 15, (c, r) => c < 2 || (c === 2 && r >= 5)) + `<path d="M85 10H115V85H130V160H85Z" fill="none" stroke="${ZF.tinte}" stroke-width="4" stroke-linejoin="round"/>`;
  const x0 = 34, l = 250, X = (p) => x0 + p * l / 100; let b = `<rect x="${x0}" y="70" width="${l * 0.8}" height="30" fill="${ZF.blauFl}"/>` + zKasten(x0, 70, l, 30, { rx: 0, fl: 'none' });
  for (let p = 0; p <= 100; p += 10) b += zL(X(p), 62, X(p), 70, { b: 1.75 }) + (p % 20 === 0 && p !== 80 ? zT(X(p), 54, p, { g: 14, f: ZF.leise }) : '') + zL(X(p), 100, X(p), 108, { b: 1.75 });
  b += zT(X(0) - 12, 126, '0', { g: 14, f: ZF.leise }) + zT(X(100), 126, '60', { g: 14, f: ZF.leise }) + zT(X(50), 126, '30', { g: 14, f: ZF.leise }) + zT(12, 54, '%', { g: 14, w: 700 }) + zT(12, 126, '€', { g: 14, w: 700 });
  b += zL(X(80), 34, X(80), 148, { f: ZF.gelb, b: 8 }) + zL(X(80), 34, X(80), 148, { b: 2.5, strich: '6 4' }) + zMarke(X(80), 22, '80 %', { breit: 60, g: 15 }) + zMarke(X(80), 162, '48 €', { breit: 60, g: 15 });
  b += zL(X(1), 62, X(1), 108, { b: 2 }) + zPfad(`M${X(1)} 108v34h8`, { b: 1.5 }) + zT(X(1) + 12, 147, '1 % = 0,60 €', { g: 14, a: 'start', w: 700 });
  return { name: 'Prozent als Faktor', felder: [
    { svg: zBlatt(320, 170, a, 'Hunderterfeld aus 10 mal 10 Feldern; zweieinhalb Spalten, also 25 Felder, sind gefärbt und umrahmt'), kopf: 'Von hundert', gl: `${W('25')} von 100 = 25 %`, satz: 'Hundert gleiche Felder, 25 davon gefärbt.' },
    { svg: zBlatt(320, 184, b, 'Ein Streifen mit zwei Skalen: oben 0 bis 100 Prozent, unten 0 bis 60 Euro. Markiert sind 1 Prozent mit 0,60 Euro und 80 Prozent mit 48 Euro'), kopf: 'Prozent und Euro', gl: `${W('80 %')} von 60 € sind ${W('48 €')}`, satz: 'Beide Skalen beginnen bei 0; 100 % steht genau über 60 €.', pfeil: 'mit Geld' },
  ] };
}
// ---------- Funktionen 1 · Zuordnung: Tabelle, Graph, Gleichung ----------
function zZuordnung() {
  let t = zKasten(100, 12, 120, 170, { rx: 0, fl: 'none' }) + zL(160, 12, 160, 182, { b: 1.5 }) + zL(100, 46, 220, 46, { b: 2.5 }) + zT(130, 36, 'x', { g: 16, w: 800 }) + zT(190, 36, 'y', { g: 16, w: 800 });
  [[0, 1], [1, 3], [2, 5], [3, 7]].forEach(([x, y], i) => { const yy = 46 + i * 34; t += (x === 2 ? `<rect x="100" y="${yy}" width="120" height="34" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="4"/>` : i ? zL(100, yy, 220, yy, { b: 1, f: ZF.leise }) : '') + zT(130, yy + 24, x, { g: 18, w: 800, f: x === 2 ? '#11161D' : ZF.tinte }) + zT(190, yy + 24, y, { g: 18, w: 800, f: x === 2 ? '#11161D' : ZF.tinte }); });
  const K = zKoord(100, 214, 24, 24, -1, 4, -1, 8, { zx: [1, 2, 3], zy: [1, 3, 5, 7] }); let g = K.s + zL(K.X(2), K.Y(-1), K.X(2), K.Y(8), { b: 2, strich: '6 4', f: ZF.blau }) + zKurve(K, (x) => 2 * x + 1, -1, 3.5);
  [[0, 1], [1, 3], [2, 5], [3, 7]].forEach(([x, y]) => { g += zPunkt(K.X(x), K.Y(y), { gelb: x === 2 }); }); g += zSchild(K.X(2) + 42, K.Y(5) + 5, '(2 | 5)', { g: 14, w: 700 });
  const e = zT(160, 38, 'y = 2 · x + 1', { g: 20, w: 800 }) + zGl(160, 88, [['2 · 2 + 1 = 5']], 18);
  return { name: 'Zuordnung', felder: [
    { svg: zBlatt(320, 194, t, 'Tabelle mit den Wertepaaren 0 und 1, 1 und 3, 2 und 5, 3 und 7; die Zeile 2 und 5 ist umrahmt'), kopf: 'Tabelle', gl: `zu ${W('x = 2')} gehört ${W('y = 5')}`, satz: 'Zu jedem x steht genau ein y.' },
    { svg: zBlatt(320, 250, g, 'Koordinatensystem mit vier Punkten auf einer Geraden. Eine gestrichelte senkrechte Linie bei x gleich 2 trifft die Gerade genau einmal, im Punkt 2 und 5'), kopf: 'Graph', gl: `Punkt ${W('(2 | 5)')}`, satz: 'Die senkrechte Linie bei x = 2 trifft den Graphen genau einmal.', pfeil: 'als Graph' },
    { svg: zBlatt(320, 112, e, 'Die Gleichung y gleich 2 mal x plus 1; eingesetzt: 2 mal 2 plus 1 gleich 5'), kopf: 'Gleichung', gl: '', satz: 'Dieselbe Zuordnung als Rechenrezept: 2 einsetzen ergibt 5.', pfeil: 'als Gleichung' },
  ] };
}
// ---------- Funktionen 2 · Wachstum: immer plus 2, immer mal 2 ----------
function zWachstum() {
  const K = zKoord(44, 250, 58, 13.5, 0, 4, 0, 16, { sy: 2, zx: [1, 2, 3, 4], zy: [4, 8, 12, 16] }), lin = (x) => 2 * x + 1, ex = (x) => 2 ** x; let s = K.s;
  for (let x = 0; x < 4; x++) { s += zPfad(`M${K.X(x)} ${K.Y(lin(x))}H${K.X(x + 1)}V${K.Y(lin(x + 1))}`, { b: 1.5, f: ZF.blau, strich: '4 3' }) + zPfad(`M${K.X(x)} ${K.Y(ex(x))}H${K.X(x + 1)}V${K.Y(ex(x + 1))}`, { b: 1.5, strich: '4 3' }); }
  s += zKurve(K, lin, 0, 4, { f: ZF.blau }) + zKurve(K, ex, 0, 4);
  for (let x = 0; x <= 4; x++) s += `<circle cx="${K.X(x)}" cy="${K.Y(lin(x))}" r="5" fill="${ZF.blau}" stroke="${ZF.papier}" stroke-width="1.5"/>` + zPunkt(K.X(x), K.Y(ex(x)));
  for (let x = 1; x <= 4; x++) { s += zT(K.X(x) - 7, K.Y((lin(x) + lin(x - 1)) / 2) + 5 - (x < 3 ? 9 : 0), '+2', { g: 14, w: 800, a: 'end', f: ZF.blau });
    const my = K.Y((ex(x) + ex(x - 1)) / 2) + (x < 3 ? 12 : 0); s += `<rect x="${K.X(x) + 5}" y="${my - 11}" width="30" height="22" rx="6" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.5"/>` + zT(K.X(x) + 20, my + 5, '·2', { g: 14, w: 800, f: '#11161D' }); }
  s += zSchild(K.X(2.1), K.Y(14.6), 'immer mal 2', { g: 14, grotesk: true, w: 700 }) + zSchild(K.X(1.2), K.Y(8.4), 'immer plus 2', { g: 14, grotesk: true, w: 700, f: ZF.blau });
  return { name: 'Wachstum', felder: [{ svg: zBlatt(320, 284, s, 'Koordinatensystem mit zwei Graphen, die beide im Punkt 0 und 1 beginnen. Die Gerade steigt in jedem Schritt um 2 bis auf 9. Die Kurve verdoppelt sich in jedem Schritt: 1, 2, 4, 8, 16. Ab x gleich 3 liegt die Kurve höher'), gl: `${BL('+ 2')} gibt eine Gerade<br>${W('· 2')} gibt eine steile Kurve`, satz: 'Beide beginnen bei 1. Bis x = 2 liegt die Gerade höher, ab x = 3 die Kurve: 3, 5, 7, 9 gegen 2, 4, 8, 16.' }] };
}
// ---------- Funktionen 3 · Gleichung und Form ----------
function zFormen() {
  const feld = (f, ya, yb, teile, titel, o = {}) => { const K = zKoord(56, o.y0 || 196, 34, 34 * 6 / (yb - ya) * (o.st || 1), -3, 3, ya, yb, { zx: o.zx || [-2, 2], zy: o.zy || [2] }); let s = K.s;
    for (const [a, b] of teile) s += zKurve(K, f, a, b); return zBlatt(320, 216, s, titel); };
  return { name: 'Gleichung und Form', felder: [
    { svg: feld((x) => x, -3, 3, [[-3, 3]], 'Koordinatensystem mit der Geraden y gleich x durch den Ursprung', { y0: 196, zy: [-2, 2] }), kopf: 'Gerade', gl: `y = ${W('x')}`, satz: 'x allein: eine Gerade.' },
    { svg: feld((x) => x * x, -2, 4, [[-2, 2]], 'Koordinatensystem mit der Parabel y gleich x Quadrat, symmetrisch zur y-Achse, durch 0 und 0, 1 und 1, 2 und 4', { zy: [2, 4] }), kopf: 'Parabel', gl: `y = ${W('x²')}`, satz: 'x²: eine Parabel, links und rechts gleich.' },
    { svg: feld((x) => 1 / x, -3, 3, [[0.34, 3], [-3, -0.34]], 'Koordinatensystem mit der Hyperbel y gleich 1 geteilt durch x in zwei Ästen; sie berührt keine Achse', { zy: [2], zx: [2] }), kopf: 'Hyperbel', gl: `y = 1 : ${W('x')}`, satz: 'x unter dem Bruchstrich: zwei Äste, keiner berührt eine Achse.' },
    { svg: feld((x) => Math.abs(x), -2, 4, [[-3, 0], [0, 3]], 'Koordinatensystem mit dem Graphen von Betrag x: ein Knick genau im Ursprung', { zy: [2, 4] }), kopf: 'Knick', gl: `y = ${W('|x|')}`, satz: 'Betragsstriche: ein Knick genau im Ursprung.' },
  ] };
}
// ---------- Daten und Zufall 1 · Kennzahl: gleicher Mittelwert, andere Daten ----------
function zKennzahl() {
  const reihe = (y, name, werte) => { const G = zStrahl(40, y, 0, 10, 25, { g: 14, nullGleich: 1, ohnePfeil: 1 }); let s = G.s + zT(14, y - 20, name, { g: 18, w: 800 }); const hoch = {};
    for (const v of werte) { hoch[v] = (hoch[v] || 0) + 1; s += zPunkt(G.X(v), y - 2 - hoch[v] * 14, { r: 6 }); }
    return s + `<polygon points="${G.X(5)},${y + 32} ${G.X(5) - 11},${y + 52} ${G.X(5) + 11},${y + 52}" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="2" stroke-linejoin="round"/>`; };
  const s = reihe(52, 'A', [4, 5, 5, 6]) + reihe(170, 'B', [1, 2, 8, 9]) + zL(165, 108, 165, 198, { b: 1.5, f: ZF.leise, strich: '3 4' }) + zT(200, 100, 'Mittelwert 5', { g: 14, grotesk: true, w: 700, a: 'start' }) + zT(200, 218, 'Mittelwert 5', { g: 14, grotesk: true, w: 700, a: 'start' });
  return { name: 'Kennzahl', felder: [{ svg: zBlatt(320, 236, s, 'Zwei Punktreihen über derselben Zahlengeraden von 0 bis 10. Reihe A: Punkte bei 4, 5, 5 und 6. Reihe B: Punkte bei 1, 2, 8 und 9. In beiden steht bei 5 ein Dreieck für den Mittelwert, genau untereinander'), gl: `A: 4, 5, 5, 6 – Mittelwert ${W('5')}<br>B: 1, 2, 8, 9 – Mittelwert ${W('5')}`, satz: 'Derselbe Mittelwert, ganz verschiedene Daten: Wie weit die Punkte auseinanderliegen, verrät der Mittelwert nicht.' }] };
}
// ---------- Daten und Zufall 2 · Vom Teil aufs Ganze ----------
function zStichprobe() {
  const k = 20, x0 = 66, y0 = 18, bunt = (r, c) => (r === 9 && (c <= 3 || c === 5 || c === 6)) || (r === 8 && (c <= 1 || (c >= 3 && c <= 6))) || (r >= 5 && r <= 7 && c <= 5);
  const zug = [[0, 2], [1, 7], [2, 4], [3, 9], [4, 1], [5, 8], [6, 3], [7, 1], [8, 8], [9, 6]], P = (r, c) => [x0 + c * k, y0 + r * k]; let s = '', n = 0;
  s += zPfad('M' + [[0, 2], [2, 4], [1, 7], [3, 9], [5, 8], [8, 8], [9, 6], [6, 3], [7, 1], [4, 1]].map(([r, c]) => P(r, c).join(' ')).join('L') + 'Z', { b: 1.25, f: ZF.leise });
  s += `<rect x="${x0 - 11}" y="${y0 + 8 * k - 11}" width="${4 * k + 22}" height="${k + 22}" rx="9" fill="${ZF.blauFl}" stroke="${ZF.blau}" stroke-width="2.5"/>`;
  for (const [r, c] of zug) s += `<circle cx="${P(r, c)[0]}" cy="${P(r, c)[1]}" r="9.500" fill="${ZF.gelb}" stroke="${ZF.tinte}" stroke-width="1.75"/>`;
  for (let r = 0; r < 10; r++) for (let c = 0; c < 10; c++) { const b = bunt(r, c); n += b; s += `<circle cx="${P(r, c)[0]}" cy="${P(r, c)[1]}" r="5" fill="${b ? ZF.tinte : ZF.papier}" stroke="${ZF.tinte}" stroke-width="1.75"/>`; }
  if (n !== 30 || zug.filter(([r, c]) => bunt(r, c)).length !== 3 || [8, 9].flatMap((r) => [0, 1, 2, 3, 4].map((c) => bunt(r, c))).filter(Boolean).length !== 8) throw new Error('Stichprobe: Zahlen stimmen nicht');
  s += zT(160, 236, '30 von 100 Punkten sind gefüllt: 30 %', { g: 15, grotesk: true, w: 700 });
  return { name: 'Vom Teil aufs Ganze', felder: [{ svg: zBlatt(320, 250, s, 'Feld mit 100 Punkten, 30 davon gefüllt, gehäuft links unten. Zehn verstreute Punkte sind gelb umringt und verbunden: 3 davon gefüllt. Ein blauer Rahmen fasst zehn Punkte in der linken unteren Ecke: 8 davon gefüllt'), gl: `zufällig gezogen: ${W('3 von 10')} = 30 %<br>aus einer Ecke: ${BL('8 von 10')} = 80 %`, satz: 'Die zufällig gezogenen zehn treffen das Ganze. Die zehn aus der Ecke täuschen.' }] };
}
// ---------- Daten und Zufall 3 · Anteil: günstige durch mögliche ----------
function zWuerfel() {
  const augen = { 1: [[0, 0]], 2: [[-1, -1], [1, 1]], 3: [[-1, -1], [0, 0], [1, 1]], 4: [[-1, -1], [1, -1], [-1, 1], [1, 1]], 5: [[-1, -1], [1, -1], [0, 0], [-1, 1], [1, 1]], 6: [[-1, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [1, 1]] }; let s = '';
  for (let n = 1; n <= 6; n++) { const x = 14 + (n - 1) * 50, g = n % 2 === 0; s += zKasten(x, 30, 42, 42, { rx: 8, fl: g ? ZF.gelb : ZF.papier, b: g ? 4 : 2 }) + augen[n].map(([a, b]) => `<circle cx="${x + 21 + a * 11}" cy="${51 + b * 11}" r="3.800" fill="${g ? '#11161D' : ZF.tinte}"/>`).join('') + (g ? zHaken(x + 21, 92) : ''); }
  return { name: 'Anteil', felder: [{ svg: zBlatt(320, 112, s, 'Sechs gleich große Würfelflächen mit 1 bis 6 Augen in einer Reihe. Die Flächen mit 2, 4 und 6 Augen sind hervorgehoben'), gl: `gerade Zahl: ${W('3')} von 6 = ${bruch(1, 2)}`, satz: 'Sechs gleich wahrscheinliche Ergebnisse, drei davon sind günstig.' }] };
}
// ---------- Daten und Zufall 4 · Stufen: Baum für zwei Münzwürfe ----------
function zBaum() {
  const W0 = [26, 110], K1 = [124, 58], Z1 = [124, 162], E = { KK: [222, 26], KZ: [222, 88], ZK: [222, 132], ZZ: [222, 194] }; let s = '';
  s += `<rect x="${E.KZ[0] + 10}" y="${E.KZ[1] - 20}" width="84" height="${E.ZK[1] - E.KZ[1] + 40}" rx="10" fill="${ZF.blauFl}" stroke="${ZF.blau}" stroke-width="2.5"/>`;
  s += zL(...W0, ...K1, { f: ZF.gelb, b: 10 }) + zL(...K1, ...E.KZ, { f: ZF.gelb, b: 10 });
  const ast = (a, b, o = {}) => zL(...a, ...b, { b: o.b || 2.25 }) + zSchild((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + (o.dy || -8), '½', { g: 19, w: 800 });
  s += ast(W0, K1, { b: 3.5 }) + ast(W0, Z1, { dy: 22 }) + ast(K1, E.KK) + ast(K1, E.KZ, { b: 3.5, dy: 22 }) + ast(Z1, E.ZK) + ast(Z1, E.ZZ, { dy: 22 });
  s += zPunkt(...W0) + zPunkt(...K1) + zPunkt(...Z1) + zT(K1[0], K1[1] - 14, 'Kopf', { g: 14, grotesk: true, w: 700 }) + zT(Z1[0], Z1[1] + 26, 'Zahl', { g: 14, grotesk: true, w: 700 });
  for (const [n, p] of Object.entries(E)) s += zPunkt(...p) + zT(p[0] + 18, p[1] + 6, n, { g: 16, w: 800, a: 'start' }) + zT(p[0] + 64, p[1] + 7, '¼', { g: 20, w: 800, a: 'start' });
  return { name: 'Stufen', felder: [{ svg: zBlatt(320, 220, s, 'Baumdiagramm für zwei Münzwürfe: von der Wurzel zwei Äste zu Kopf und Zahl, von jedem wieder zwei. An jedem Ast ein halb, an den vier Enden KK, KZ, ZK, ZZ je ein Viertel. Der Pfad Kopf–Zahl ist gelb hinterlegt; die Enden KZ und ZK sind gemeinsam blau umrahmt'), gl: `Pfad Kopf–Zahl: ${W('½ · ½')} = ¼<br>genau einmal Kopf: ${BL('¼ + ¼')} = ½`, satz: 'Gelb: einen Pfad entlang wird malgenommen. Blau: zwei Enden zusammen werden addiert.' }] };
}
// ---------- Rechenregel 10 · zwei Nebenfelder: Mal und Geteilt ----------
function zBruchMal() { const x0 = 88, y0 = 14, k = 144; let s = `<rect x="${x0}" y="${y0}" width="${k}" height="${k * 3 / 4}" fill="${ZF.blauFl}"/><rect x="${x0}" y="${y0}" width="${k * 2 / 3}" height="${k * 3 / 4}" fill="${ZF.gelb}"/>`;
  for (let i = 1; i < 4; i++) s += zL(x0, y0 + i * k / 4, x0 + k, y0 + i * k / 4, { b: 1.5 }); for (let i = 1; i < 3; i++) s += zL(x0 + i * k / 3, y0, x0 + i * k / 3, y0 + k, { b: 1.5 });
  s += zKasten(x0, y0, k, k, { rx: 0, fl: 'none' }) + `<rect x="${x0}" y="${y0}" width="${k * 2 / 3}" height="${k * 3 / 4}" fill="none" stroke="${ZF.tinte}" stroke-width="4.500"/>` + zPfad(`M${x0 - 8} ${y0}h-6v${k * 3 / 4}h6`, { b: 1.75, f: ZF.leise }) + zBruchT(56, y0 + k * 3 / 8 - 4, 3, 4, 17) + zPfad(`M${x0} ${y0 + k + 8}v6h${k * 2 / 3}v-6`, { b: 1.75, f: ZF.leise }) + zBruchT(x0 + k / 3, y0 + k + 30, 2, 3, 17);
  return s; }
function zBruchGeteilt() { let s = ''; for (let i = 0; i < 6; i++) { const y = 12 + i * 27; s += zKasten(70, y, 180, 21, { rx: 0, fl: ZF.blauFl, b: 2 }) + zL(160, y, 160, y + 21, { b: 2 }) + zT(115, y + 16, 2 * i + 1, { g: 14, w: 700 }) + zT(205, y + 16, 2 * i + 2, { g: 14, w: 700 }) + zT(52, y + 16, i + 1, { g: 14, f: ZF.leise }); }
  return s + zL(160, 6, 160, 176, { f: ZF.gelb, b: 7 }) + zL(160, 6, 160, 176, { b: 2.5, strich: '6 4' }); }
{ const alt = ZEICHNUNGEN.R10; ZEICHNUNGEN.R10 = () => { const z = alt(); z.felder[0].kopf = 'Plus und Minus'; z.felder.push(
  { svg: zBlatt(320, 216, zBruchMal(), 'Ein Quadrat, waagerecht in Viertel und senkrecht in Drittel geteilt, 12 Felder. Drei Viertel sind hell gefärbt, davon zwei Drittel kräftig und umrahmt: 6 von 12 Feldern'), kopf: 'Mal', gl: `${bruch(2, 3)} · ${bruch(3, 4)} = ${W(bruch(6, 12))} = ${bruch(1, 2)}`, satz: 'Zwei Drittel von drei Vierteln: 6 von 12 Feldern, also die Hälfte.', neu: 'Zwei Nebenzeichnungen: Mal und Geteilt' },
  { svg: zBlatt(320, 184, zBruchGeteilt(), 'Sechs ganze Streifen untereinander, jeder halbiert: zusammen 12 Hälften, durchnummeriert'), kopf: 'Geteilt', gl: `6 : ${bruch(1, 2)} = 6 ${W('· 2')} = 12`, satz: 'Wie oft passt ein Halbes in 6 Ganze? In jedes zweimal, also zwölfmal.' }); return z; }; }

Object.assign(ZEICHNUNGEN, { 'I-zahlen-1': zOrdnung, 'I-zahlen-2': zBuendeln, 'I-zahlen-3': zBausteine, 'I-zahlen-4': zSchreibweisen, 'I-zahlen-5': zHochZurueck, 'I-algebra-1': zTerm, 'I-algebra-2': zErlaubt, 'I-algebra-3': zEinsetzen, 'I-algebra-4': zHoeherGrad,
  'I-geld-1': zGroesse, 'I-geld-2': zDoppelgerade, 'I-geld-3': zProzent, 'I-funktionen-1': zZuordnung, 'I-funktionen-2': zWachstum, 'I-funktionen-3': zFormen, 'I-daten-1': zKennzahl, 'I-daten-2': zStichprobe, 'I-daten-3': zWuerfel, 'I-daten-4': zBaum });
Object.assign(MINI_FELD, { 'I-algebra-1': 1, 'I-algebra-4': 1, 'I-funktionen-1': 1, 'I-funktionen-3': 1 });
