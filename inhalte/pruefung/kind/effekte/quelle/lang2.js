// ---------- Zweite Varianten je Anlass (Abwechslung) ----------
const ebene = (stil) => { const d = h('div', { style: 'position:absolute;inset:0;z-index:20;pointer-events:none;' + (stil || '') }); app().append(d); return d; };
const raus = async (...els) => { els.forEach((x) => x?.animate?.([{ opacity: 1 }, { opacity: 0 }], { duration: 350, fill: 'forwards' })); await warte(360); els.forEach((x) => x?.remove?.()); };
const grossText = (txt, farbe = '#FFD23F', top = '30%', gr = 56) => { const t = h('div', { style: `position:absolute;z-index:27;left:0;right:0;top:${top};text-align:center;font:900 ${gr}px/1 system-ui;color:${farbe};letter-spacing:.03em;text-shadow:0 4px 0 #0005,0 0 30px ${farbe}88` }, txt); app().append(t); t.animate([{ transform: 'scale(2.4)', opacity: 0 }, { transform: 'scale(.92)', opacity: 1, offset: .7 }, { transform: 'scale(1)' }], { duration: 420, easing: 'cubic-bezier(.3,1.4,.5,1)', fill: 'both' }); return t; };
const konfetti = (x, y, n = 60, hoch = 10) => { const farben = ['#FFD23F', '#F472B6', '#60A5FA', '#34D399', '#F97316', '#A78BFA']; const t = [];
  for (const f of farben) t.push(teilchen(x, y, Math.ceil(n / farben.length), { punkt: 8, farbe: f, kraft: 10, hoch, schwer: .32, z: 26 })); return { weg: () => t.forEach((x) => x.weg()) }; };

// 1) Direktflug: Kampfjet-Überflug
FX.jet = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const jetSvg = '<svg viewBox="0 0 120 40" width="120" height="40"><path d="M4 20 L70 14 L92 2 L98 2 L88 16 L114 18 L118 20 L114 22 L88 24 L98 38 L92 38 L70 26Z" fill="#CBD5E1" stroke="#1E293B" stroke-width="2.5"/><path d="M70 17 L84 19 L70 21Z" fill="#38BDF8"/></svg>';
  rauschen(1.6, .25, 700);
  for (const [i, y] of [[0, .22], [1, .36]].entries()) { const j = h('div', { style: `position:absolute;z-index:25;left:-140px;top:${y[1] * H}px;transform:rotate(-8deg)` }); j.innerHTML = jetSvg; a.append(j);
    const spur = h('div', { style: `position:absolute;z-index:24;left:0;top:${y[1] * H + 18}px;height:4px;width:0;background:linear-gradient(90deg,#fff0,#fffd);transform:rotate(-8deg);transform-origin:left;border-radius:4px` }); a.append(spur);
    j.animate([{ transform: 'translateX(0) rotate(-8deg)' }, { transform: `translateX(${W + 300}px) rotate(-8deg)` }], { duration: 900, delay: i * 180, easing: 'cubic-bezier(.4,0,.8,1)', fill: 'forwards' });
    spur.animate([{ width: '0px', opacity: 1 }, { width: `${W + 80}px`, opacity: 1, offset: .6 }, { width: `${W + 80}px`, opacity: 0 }], { duration: 1600, delay: i * 180, fill: 'forwards' }); setTimeout(() => { j.remove(); spur.remove(); }, 1900); }
  await warte(700); const ring = h('div', { style: `position:absolute;z-index:26;left:${W / 2 - 20}px;top:${H * .3}px;width:40px;height:40px;border-radius:50%;border:5px solid #fff` }); a.append(ring);
  ring.animate([{ transform: 'scale(1)', opacity: 1 }, { transform: 'scale(14)', opacity: 0 }], { duration: 700, fill: 'forwards' }); rauschen(.5, .5, 160); wackeln(500, 7);
  const t = grossText('ÜBERSCHALL!', '#fff', '24%', 50); await warte(1300); await raus(t, ring); sticker('PEAK', 3); };

// 2) Saubere Landung: Applaus an Bord
FX.applaus = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const reihe = h('div', { style: `position:absolute;z-index:24;left:0;right:0;bottom:-80px;height:80px;display:flex;justify-content:space-around;align-items:flex-end;transition:bottom .35s cubic-bezier(.3,1.4,.5,1)` }, ...Array.from({ length: 6 }, (_, i) => h('div', { style: `font-size:${34 + (i % 2) * 6}px` }, ['🙂', '😃', '🤩', '😄', '😎', '🥳'][i])));
  a.append(reihe); await warte(30); reihe.style.bottom = '0px'; const k1 = konfetti(10, H - 40, 50, 14), k2 = konfetti(W - 10, H - 40, 50, 14); rauschen(1.8, .12, 2500);
  const haende = []; for (let i = 0; i < 14; i++) { setTimeout(() => { const x = h('div', { style: `position:absolute;z-index:25;left:${Math.random() * (W - 40)}px;bottom:${40 + Math.random() * 120}px;font-size:30px` }, '👏'); a.append(x); haende.push(x); x.animate([{ transform: 'scale(.3)', opacity: 0 }, { transform: 'scale(1.2)', opacity: 1 }, { transform: 'scale(1)', opacity: 0 }], { duration: 700, fill: 'forwards' }); piep(1200 + Math.random() * 600, .03, 'square', .03); }, i * 110); }
  const t = h('div', { class: 'blase', style: 'top:14%;text-align:center' }, 'Die Passagiere klatschen!'); a.append(t); await warte(2600); k1.weg(); k2.weg(); haende.forEach((x) => x.remove()); await raus(reihe, t); sticker('Süper!', 2); };

// 3) Knobel: Big Brain
FX.gehirn = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const d = ebene('background:radial-gradient(circle at 50% 42%,#7C3AEDcc,#0B0620ee 70%)'); d.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 300, fill: 'both' });
  const g = h('div', { style: `position:absolute;z-index:25;left:${W / 2 - 50}px;top:${H * .42 - 50}px;font-size:100px;line-height:1;filter:drop-shadow(0 0 20px #F0ABFC)` }, '🧠'); a.append(g);
  for (let i = 0; i < 6 && !abbruch; i++) { g.animate([{ transform: `scale(${1 + i * .25})` }, { transform: `scale(${1.15 + i * .25})` }], { duration: 160, direction: 'alternate', iterations: 2, fill: 'forwards' }); piep(300 + i * 120, .1, 'sine', .08);
    const b = h('div', { style: `position:absolute;z-index:26;left:${W / 2 + (Math.random() - .5) * 220}px;top:${H * .42 + (Math.random() - .5) * 220}px;font-size:26px` }, '⚡'); a.append(b); setTimeout(() => b.remove(), 300); await warte(300); }
  const blitz = ebene('background:#fff;opacity:.8;z-index:28'); setTimeout(() => blitz.remove(), 100); g.remove(); rauschen(.5, .4, 1200); const k = konfetti(W / 2, H * .42, 90, 4);
  const t = grossText('BIG BRAIN', '#F0ABFC', '30%', 54); await warte(1500); k.weg(); await raus(t, d); sticker('Çüş!', 3); };

// 4) Serie 5: Nitro-Combo
FX.nitro = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const lin = ebene('background:repeating-conic-gradient(from 0deg at 50% 50%,#fff0 0 4deg,#ffffff30 4deg 5deg);mix-blend-mode:overlay'); lin.animate([{ transform: 'scale(1) rotate(0)', opacity: 0 }, { transform: 'scale(1.6) rotate(6deg)', opacity: 1 }], { duration: 900, fill: 'forwards' });
  a.animate([{ transform: 'scale(1)' }, { transform: 'scale(1.04)' }, { transform: 'scale(1)' }], { duration: 900 }); rauschen(1.2, .2, 500);
  const combo = h('div', { style: 'position:absolute;z-index:27;right:14px;top:22%;text-align:right;font:900 italic 54px/1 system-ui;color:#22D3EE;text-shadow:3px 3px 0 #0E7490,0 0 24px #22D3EE' }, '5×', h('div', { style: 'font-size:22px;letter-spacing:.1em' }, 'COMBO'));
  a.append(combo); combo.animate([{ transform: 'translateX(160px) skewX(-20deg)' }, { transform: 'translateX(-10px) skewX(-8deg)', offset: .7 }, { transform: 'none' }], { duration: 450, fill: 'both' }); piep(660, .08); await warte(90); piep(880, .08); await warte(90); piep(1320, .2);
  const flammen = teilchen(20, H * .55, 40, { inhalt: ['🔥'], gross: 26, kraft: 9, schwer: -.1, z: 25 }); for (const p of flammen.liste) { p.vx = Math.abs(p.vx) + 6; p.vy *= .3; }
  await warte(1700); flammen.weg(); await raus(lin, combo); sticker('Locked in.', 2); };

// 5) Comeback: Phönix
FX.phoenix = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const d = ebene('background:linear-gradient(0deg,#7C2D12ee,#1C0A04cc 60%,#0000)'); d.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 300, fill: 'both' });
  const feuer = teilchen(W / 2, H, 60, { inhalt: ['🔥'], gross: 30, kraft: 6, hoch: 10, schwer: .12, z: 24 }); rauschen(2, .2, 600);
  const v = h('div', { style: `position:absolute;z-index:26;left:${W / 2 - 80}px;top:${H}px;width:160px;height:110px` }); v.innerHTML = '<svg viewBox="0 0 160 110" width="160" height="110"><path d="M80 30 C60 0 20 10 0 30 C30 30 40 40 50 60 C30 60 20 80 30 100 C50 80 65 75 80 80 C95 75 110 80 130 100 C140 80 130 60 110 60 C120 40 130 30 160 30 C140 10 100 0 80 30Z" fill="url(#g)"/><defs><linearGradient id="g" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#F97316"/><stop offset="1" stop-color="#FDE047"/></linearGradient></defs><circle cx="80" cy="30" r="8" fill="#FDE047"/></svg>';
  a.append(v); v.animate([{ transform: 'translateY(0) scale(.6)' }, { transform: `translateY(${-H * .75}px) scale(1.3)` }], { duration: 1400, easing: 'cubic-bezier(.2,.8,.3,1)', fill: 'forwards' });
  await warte(500); piep(523, .15, 'triangle'); await warte(150); piep(659, .15, 'triangle'); await warte(150); piep(784, .4, 'triangle');
  const t = grossText('AUFERSTANDEN', '#FDE047', '58%', 40); await warte(1500); feuer.weg(); await raus(v, t, d); sticker('Comeback.', 2); };

// 6) Fehler: Kapitän niest
FX.niesen = async function (e) { const a = app(), bk = a.querySelector('.bk');
  const b1 = h('div', { class: 'blase', style: 'top:8px' }, 'Haaa… haaaa…'); a.append(b1); await warte(700); b1.textContent = 'TSCHI!'; b1.style.fontSize = '26px'; wackeln(250, 4); rauschen(.35, .3, 3000);
  const r = bk.getBoundingClientRect(), A = a.getBoundingClientRect(); const tropfen = [];
  for (let i = 0; i < 26; i++) { const x = h('div', { style: `position:absolute;z-index:23;left:${r.left - A.left + Math.random() * r.width}px;top:${r.top - A.top + Math.random() * 60}px;width:${6 + Math.random() * 12}px;height:${6 + Math.random() * 12}px;border-radius:50%;background:#BAE6FDcc;box-shadow:inset -2px -2px 0 #fff8` }); a.append(x); tropfen.push(x); }
  await warte(600); const wisch = h('div', { style: `position:absolute;z-index:24;left:${A.width / 2}px;top:${r.top - A.top}px;width:6px;height:150px;background:#1E293B;border-radius:3px;transform-origin:bottom center;transform:rotate(-70deg)` }); a.append(wisch);
  wisch.animate([{ transform: 'rotate(-70deg)' }, { transform: 'rotate(70deg)' }, { transform: 'rotate(-70deg)' }], { duration: 900 }); setTimeout(() => tropfen.forEach((x) => x.remove()), 450);
  b1.textContent = 'Gesundheit! Daran lag’s. Nächste!'; b1.style.fontSize = ''; await warte(1000); await raus(wisch, b1); };

// 7) Sturmflug: Tornado
FX.tornado = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const d = ebene('background:#1F2937dd'); d.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 300, fill: 'both' }); rauschen(2.4, .3, 500);
  const wirbel = h('div', { style: `position:absolute;z-index:24;left:${W / 2 - 110}px;top:${H * .1}px;width:220px;height:${H * .7}px;background:conic-gradient(from 0deg,#94A3B800,#94A3B8aa,#94A3B800 30%,#CBD5E1aa 60%,#94A3B800);clip-path:polygon(0 0,100% 0,60% 100%,40% 100%);animation:dreh .35s linear infinite;filter:blur(2px)` });
  if (!document.getElementById('dreh-k')) document.head.append(h('style', { id: 'dreh-k' }, '@keyframes dreh{to{transform:rotate(360deg)}}')); a.append(wirbel);
  const sachen = ['🐄', '🧳', '📐', '🌵', '🪑', '🐓']; const fl = sachen.map((s, i) => { const x = h('div', { style: `position:absolute;z-index:25;left:${W / 2}px;top:${H * (.2 + i * .1)}px;font-size:36px` }, s); a.append(x);
    x.animate([{ transform: 'translateX(-110px) rotate(0)' }, { transform: 'translateX(110px) rotate(360deg)' }, { transform: 'translateX(-110px) rotate(720deg)' }], { duration: 700 + i * 90, iterations: 3 }); return x; });
  wackeln(1800, 4); await warte(1900); fl.forEach((x, i) => x.animate([{ transform: 'none' }, { transform: `translate(${(i % 2 ? 1 : -1) * W}px,${-H * .4}px) rotate(900deg)` }], { duration: 600, fill: 'forwards' }));
  await raus(wirbel, d); piep(784, .2, 'triangle'); const t = grossText('DURCHGEZOGEN', '#7EF0C2', '30%', 40); await warte(900); await raus(t, ...fl); sticker('Macher-Modus', 2); };

// 8) Flug geschafft: Feuerwerk
FX.feuerwerk = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height; const alle = [];
  for (let i = 0; i < 5 && !abbruch; i++) { const x = W * (.2 + Math.random() * .6), y = H * (.12 + Math.random() * .25);
    const r = h('div', { style: `position:absolute;z-index:25;left:${x}px;top:${H}px;width:4px;height:16px;border-radius:2px;background:#FDE68A;box-shadow:0 0 8px #FDE68A` }); a.append(r);
    piep(300, .3, 'sawtooth', .03); r.animate([{ transform: 'none' }, { transform: `translateY(${y - H}px)` }], { duration: 520, easing: 'cubic-bezier(.2,.7,.4,1)', fill: 'forwards' }); await warte(520); r.remove();
    const f = ['#F472B6', '#60A5FA', '#FDE047', '#34D399', '#F97316'][i]; alle.push(teilchen(x, y, 36, { punkt: 5, farbe: f, rund: true, kraft: 6, schwer: .08, z: 26 })); rauschen(.5, .35, 250); await warte(260); }
  await warte(900); alle.forEach((t) => t.weg()); sticker('Peak-Flug', 3); };

// Gruppen: welcher Effekt gehört zu welchem Anlass
const FX_GRUND = { jet: () => landung('direkt'), applaus: () => landung('sauber'), gehirn: () => uebung('ok', 'Knobel-Bordkarte im 1. Versuch.'), nitro: () => uebung('ok', '5 richtig in Folge.'), phoenix: () => uebung('ok', '3 richtig in Folge nach dem Fehler.'), niesen: () => uebung('falsch'), tornado: () => landung('sturm'), feuerwerk: flug };
