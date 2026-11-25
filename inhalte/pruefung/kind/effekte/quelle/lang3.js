// ---------- Horror (ohne Blut, mit Pointe) ----------
function spieluhr(noten = [659, 784, 880, 784, 659, 587, 659, 523], tempo = 0.28) { const c = ton(); if (!c) return; noten.forEach((f, i) => { const o = c.createOscillator(), g = c.createGain(); o.type = 'triangle';
  const t = c.currentTime + i * tempo; o.frequency.setValueAtTime(f * (1 - i * 0.006), t); g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.09, t + 0.01); g.gain.exponentialRampToValueAtTime(0.0001, t + tempo * 1.6); o.connect(g).connect(c.destination); o.start(t); o.stop(t + tempo * 1.7); }); }
function hupe() { const c = ton(); if (!c) return; const o = c.createOscillator(), g = c.createGain(); o.type = 'square'; o.frequency.setValueAtTime(330, c.currentTime); o.frequency.exponentialRampToValueAtTime(180, c.currentTime + .25); g.gain.value = .08; o.connect(g).connect(c.destination); o.start(); o.stop(c.currentTime + .28); }
const CLOWN = `<svg viewBox="0 0 220 250" width="100%" height="100%">
 <defs><radialGradient id="cg" cx=".5" cy=".45" r=".6"><stop offset="0" stop-color="#F8FAFC"/><stop offset="1" stop-color="#CBD5E1"/></radialGradient></defs>
 <circle cx="40" cy="120" r="30" fill="#7C3AED"/><circle cx="26" cy="146" r="22" fill="#6D28D9"/><circle cx="180" cy="120" r="30" fill="#7C3AED"/><circle cx="194" cy="146" r="22" fill="#6D28D9"/>
 <ellipse cx="110" cy="140" rx="74" ry="88" fill="url(#cg)" stroke="#1E1B4B" stroke-width="4"/>
 <rect x="58" y="10" width="104" height="62" rx="6" fill="#111827"/><rect x="40" y="66" width="140" height="14" rx="7" fill="#111827"/><rect x="58" y="50" width="104" height="12" fill="#7C3AED"/>
 <path d="M70 92 l12 -22 l12 22 l-12 22z M126 92 l12 -22 l12 22 l-12 22z" fill="#7C3AED" opacity=".75"/>
 <ellipse class="aug" cx="82" cy="112" rx="15" ry="18" fill="#0B0620"/><ellipse class="aug" cx="138" cy="112" rx="15" ry="18" fill="#0B0620"/>
 <circle class="pup" cx="85" cy="114" r="4.5" fill="#FDE047"/><circle class="pup" cx="135" cy="114" r="4.5" fill="#FDE047"/>
 <circle class="nase" cx="110" cy="140" r="15" fill="#E11D48" stroke="#881337" stroke-width="3"/><circle cx="105" cy="135" r="4" fill="#fff8"/>
 <path d="M54 158 Q110 236 166 158 Q110 196 54 158Z" fill="#3B0764" stroke="#1E1B4B" stroke-width="4"/>
 <path d="M70 166 l6 12 l6 -10 l6 14 l6 -12 l6 14 l6 -12 l6 14 l6 -12 l6 14 l6 -12 l6 12 l6 -10 l4 8" fill="#F8FAFC" stroke="#1E1B4B" stroke-width="1.5"/>
 <path d="M60 150 l-10 6 M160 150 l10 6" stroke="#1E1B4B" stroke-width="3" stroke-linecap="round"/></svg>`;

// G) Der Clown – Direktflug (≈ 6,5 s)
FX.clown = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const d = ebene('background:radial-gradient(ellipse at 50% 55%,#1E1B4Bdd,#000 75%)'); d.style.zIndex = 21; d.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 600, fill: 'both' }); spieluhr(); await warte(600);
  const ballon = h('div', { style: `position:absolute;z-index:23;left:${W / 2 - 30}px;top:${H}px;width:60px;height:150px` }); ballon.innerHTML = '<svg viewBox="0 0 60 150" width="60" height="150"><ellipse cx="30" cy="34" rx="26" ry="32" fill="#E11D48"/><ellipse cx="21" cy="22" rx="6" ry="9" fill="#fff6"/><path d="M27 66 l3 6 l3 -6z" fill="#BE123C"/><path d="M30 72 Q20 95 32 115 Q42 132 28 150" stroke="#E2E8F0" stroke-width="1.5" fill="none"/></svg>';
  a.append(ballon); ballon.animate([{ transform: 'translateY(0)' }, { transform: `translateY(${-H * .62}px) rotate(-4deg)` }, { transform: `translateY(${-H * .6}px) rotate(4deg)` }], { duration: 2000, easing: 'ease-out', fill: 'forwards' });
  const t1 = h('div', { style: 'position:absolute;z-index:24;left:0;right:0;bottom:16%;text-align:center;color:#C4B5FD;font:italic 600 18px Georgia,serif;letter-spacing:.06em' }, 'Psst … ganz ohne Fehler?'); a.append(t1); t1.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 900, delay: 600, fill: 'both' });
  await warte(2300); t1.remove();
  // Stille, einmal Flackern
  d.style.background = '#000'; await warte(250); d.style.background = 'radial-gradient(ellipse at 50% 55%,#1E1B4Bdd,#000 75%)'; await warte(500);
  // SCHOCK
  const c = h('div', { style: `position:absolute;z-index:30;left:${W / 2 - W * .55}px;top:${H * .02}px;width:${W * 1.1}px;height:${H * .9}px` }); c.innerHTML = CLOWN; a.append(c);
  c.animate([{ transform: 'scale(.15)', opacity: 0 }, { transform: 'scale(1.15)', opacity: 1, offset: .6 }, { transform: 'scale(1)' }], { duration: 260, easing: 'cubic-bezier(.2,1.6,.4,1)', fill: 'both' });
  const buh = grossText('BUH!', '#FDE047', '72%', 70); buh.style.zIndex = 31; rauschen(.45, .6, 2500); piep(90, .4, 'sawtooth', .12); wackeln(450, 10); ballon.remove(); await warte(900);
  // Pointe: lacht, Nase hupt
  buh.remove(); c.animate([{ transform: 'none' }, { transform: `translateY(${H * .18}px) scale(.62)` }], { duration: 400, easing: 'ease-in-out', fill: 'forwards' }); await warte(420);
  const lach = h('div', { style: 'position:absolute;z-index:31;left:0;right:0;top:12%;text-align:center;font:900 34px system-ui;color:#C4B5FD;letter-spacing:.1em' }, ...'HAHAHA'.split('').map((b, i) => { const s = h('span', { style: 'display:inline-block' }, b); s.animate([{ transform: 'translateY(0)' }, { transform: 'translateY(-14px)' }], { duration: 180, delay: i * 60, iterations: 6, direction: 'alternate' }); return s; }));
  a.append(lach); const nase = c.querySelector('.nase'); for (let i = 0; i < 2; i++) { nase.animate([{ transform: 'scale(1)' }, { transform: 'scale(.7)' }, { transform: 'scale(1)' }], { duration: 220, transformOrigin: '110px 140px' }); hupe(); await warte(300); }
  const schild = h('div', { style: 'position:absolute;z-index:32;left:16px;right:16px;bottom:9%;background:#FDE047;color:#1E1B4B;border:3px solid #1E1B4B;border-radius:10px;padding:10px;text-align:center;font:900 20px system-ui;transform:rotate(-2deg)' }, 'Direktflug? Respekt. 🎩'); a.append(schild);
  schild.animate([{ transform: 'translateY(120px) rotate(-2deg)' }, { transform: 'rotate(-2deg)' }], { duration: 300, easing: 'cubic-bezier(.3,1.5,.5,1)', fill: 'both' }); const k = konfetti(W / 2, H * .45, 70, 6); await warte(1500);
  k.weg(); await raus(c, lach, schild, d); sticker('PEAK', 3); };

// G) Stromausfall – Flug geschafft (≈ 5,8 s)
FX.stromausfall = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const dunkel = ebene('background:#000'); dunkel.style.zIndex = 24; dunkel.style.opacity = 0;
  for (const o of [.9, 0, .95, 0.2, 1]) { dunkel.style.opacity = o; if (o > .5) piep(60, .08, 'sawtooth', .05); await warte(170); } // ≤ 3 Wechsel/s
  await warte(400);
  const lampe = ebene(''); lampe.style.zIndex = 25; let lx = W * .2, ly = H * .4; const setz = () => { lampe.style.background = `radial-gradient(circle 95px at ${lx}px ${ly}px,#0000 0,#0000 55%,#000f 100%)`; }; setz(); dunkel.style.opacity = 0;
  const folgen = (ev) => { const r = a.getBoundingClientRect(); lx = ev.clientX - r.left; ly = ev.clientY - r.top; setz(); }; a.addEventListener('pointermove', folgen);
  const augen = h('div', { style: `position:absolute;z-index:26;left:${W * .72}px;top:${H * .7}px;font:900 22px system-ui;color:#FDE047;text-shadow:0 0 12px #FDE047;letter-spacing:8px` }, '● ●'); a.append(augen);
  augen.animate([{ opacity: 1 }, { opacity: 0 }, { opacity: 1 }], { duration: 300, delay: 700, iterations: 2 });
  const t0 = performance.now(); while (!abbruch && performance.now() - t0 < 1700) { const p = (performance.now() - t0) / 1700; lx = W * (.2 + .5 * p); ly = H * (.4 + .3 * Math.sin(p * 3)); setz(); await warte(30); }
  // Schock: Geist
  augen.remove(); a.removeEventListener('pointermove', folgen); lampe.remove();
  const geist = h('div', { style: `position:absolute;z-index:30;left:${W / 2 - 110}px;top:${H * .14}px;width:220px;height:260px` }); geist.innerHTML = '<svg viewBox="0 0 220 260" width="220" height="260"><path d="M20 120 Q20 10 110 10 Q200 10 200 120 L200 240 Q185 220 170 240 Q155 260 140 240 Q125 220 110 240 Q95 260 80 240 Q65 220 50 240 Q35 260 20 240Z" fill="#F8FAFC" stroke="#94A3B8" stroke-width="4"/><ellipse cx="80" cy="100" rx="16" ry="24" fill="#0B0620"/><ellipse cx="140" cy="100" rx="16" ry="24" fill="#0B0620"/><ellipse class="mund" cx="110" cy="165" rx="26" ry="34" fill="#0B0620"/></svg>';
  a.append(geist); geist.animate([{ transform: 'scale(.2)', opacity: 0 }, { transform: 'scale(1.2)', opacity: 1, offset: .65 }, { transform: 'scale(1)' }], { duration: 260, easing: 'cubic-bezier(.2,1.6,.4,1)', fill: 'both' });
  const buh = grossText('BUUUH!', '#fff', '70%', 58); buh.style.zIndex = 31; rauschen(.4, .6, 1800); wackeln(400, 9); await warte(800);
  // Licht an, Pointe
  dunkel.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 300, fill: 'forwards' }); buh.remove(); geist.querySelector('.mund').setAttribute('ry', '10'); geist.animate([{ transform: 'none' }, { transform: 'translateY(-10px) rotate(-6deg) scale(.8)' }], { duration: 300, fill: 'forwards' });
  const t = h('div', { class: 'blase ohne', style: 'top:auto;bottom:16%;text-align:center;font-size:17px' }, '👻 Hihi – erschrocken? Glückwunsch zum Flug!'); a.append(t); piep(784, .15, 'triangle'); await warte(150); piep(988, .25, 'triangle'); const k = konfetti(W / 2, H * .35, 80, 6);
  await warte(1700); k.weg(); await raus(geist, t, dunkel); sticker('Peak-Flug', 3); };

// G) Krake – Expedition geschafft (≈ 5,6 s)
FX.krake = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const wasser = h('div', { style: `position:absolute;z-index:22;left:-10%;right:-10%;bottom:0;height:0;background:linear-gradient(#0EA5E9cc,#0C4A6Eee);border-radius:40% 40% 0 0 / 18px 18px 0 0;transition:height .7s ease-out` }); a.append(wasser); piep(70, 1.2, 'sine', .15); await warte(30); wasser.style.height = '34%'; await warte(750);
  const arm = (x, spiegeln, verz) => { const t = h('div', { style: `position:absolute;z-index:24;left:${x}px;bottom:-20px;width:90px;height:${H * .75}px;transform-origin:50% 100%;${spiegeln ? 'scale:-1 1;' : ''}` });
    t.innerHTML = `<svg viewBox="0 0 90 400" width="90" height="100%" preserveAspectRatio="none"><path d="M30 400 C10 300 70 260 50 180 C35 120 80 80 60 30 C55 10 40 8 38 22 C50 40 30 90 40 140 C50 210 0 260 15 400Z" fill="#7C3AED" stroke="#4C1D95" stroke-width="4"/>${[60, 110, 170, 230, 290, 340].map((y, i) => `<circle cx="${32 + (i % 2) * 6}" cy="${y}" r="6" fill="#DDD6FE"/>`).join('')}</svg>`;
    a.append(t); t.animate([{ transform: 'translateY(100%) rotate(0)' }, { transform: 'translateY(0) rotate(8deg)' }], { duration: 700, delay: verz, easing: 'cubic-bezier(.3,1.3,.5,1)', fill: 'both' });
    setTimeout(() => t.animate([{ transform: 'rotate(8deg)' }, { transform: 'rotate(-10deg)' }], { duration: 600, iterations: 4, direction: 'alternate', easing: 'ease-in-out' }), 700 + verz); return t; };
  const arme = [arm(-10, false, 0), arm(W - 80, true, 150), arm(W * .22, false, 300), arm(W * .6, true, 420)]; rauschen(1, .15, 300); await warte(1300);
  // Schock: Arm klatscht an die Scheibe
  const klatsch = h('div', { style: `position:absolute;z-index:29;left:${W * .1}px;top:${H * .18}px;width:${W * .8}px;height:${H * .22}px;border-radius:50px;background:#7C3AED;border:5px solid #4C1D95;box-shadow:inset 0 0 0 12px #8B5CF6` },
    ...[0, 1, 2, 3, 4].map((i) => h('div', { style: `position:absolute;top:30%;left:${10 + i * 18}%;width:34px;height:34px;border-radius:50%;background:#DDD6FE;border:4px solid #A78BFA` })));
  a.append(klatsch); klatsch.animate([{ transform: 'scale(1.6)', opacity: 0 }, { transform: 'scale(1)', opacity: 1 }], { duration: 160, fill: 'both' }); rauschen(.4, .7, 900); wackeln(450, 10);
  const t1 = grossText('KLATSCH!', '#FDE047', '44%', 50); t1.style.zIndex = 31; await warte(800);
  klatsch.animate([{ transform: 'none' }, { transform: `translateY(${H}px)` }], { duration: 900, easing: 'ease-in', fill: 'forwards' }); t1.remove();
  // Kopf taucht auf mit Schild
  const kopf = h('div', { style: `position:absolute;z-index:25;left:${W / 2 - 80}px;top:${H * .5}px;width:160px;height:120px` }); kopf.innerHTML = '<svg viewBox="0 0 160 120" width="160" height="120"><path d="M10 120 Q0 10 80 6 Q160 10 150 120Z" fill="#8B5CF6" stroke="#4C1D95" stroke-width="4"/><circle cx="55" cy="62" r="18" fill="#FDE047"/><rect x="51" y="48" width="8" height="28" rx="4" fill="#111"/><circle cx="105" cy="62" r="18" fill="#FDE047"/><rect x="101" y="48" width="8" height="28" rx="4" fill="#111"/></svg>';
  a.append(kopf); kopf.animate([{ transform: 'translateY(140px)' }, { transform: 'none' }], { duration: 500, easing: 'cubic-bezier(.3,1.4,.5,1)', fill: 'both' });
  const schild = h('div', { style: 'position:absolute;z-index:26;left:16px;right:16px;top:30%;background:#fff;color:#111;border:3px solid #4C1D95;border-radius:10px;padding:10px;text-align:center;font:900 19px system-ui' }, '🐙 Respekt, Polarprofi. Ich tauche wieder ab.'); a.append(schild);
  schild.animate([{ opacity: 0, transform: 'scale(.8)' }, { opacity: 1, transform: 'none' }], { duration: 300, delay: 300, fill: 'both' }); await warte(1700);
  arme.forEach((x) => x.animate([{ transform: 'none' }, { transform: 'translateY(100%)' }], { duration: 500, fill: 'forwards' })); kopf.animate([{ transform: 'none' }, { transform: 'translateY(160px)' }], { duration: 500, fill: 'forwards' }); wasser.style.transition = 'height .6s ease-in'; wasser.style.height = '0';
  await warte(550); [...arme, kopf, wasser, klatsch].forEach((x) => x.remove()); await raus(schild); sticker('Tuff, Polarprofi.', 2); };

// k) Knochenhand – saubere Landung (≈ 2,8 s)
FX.knochenhand = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const riss = h('div', { style: `position:absolute;z-index:23;left:${W / 2 - 70}px;bottom:0;width:140px;height:40px` }); riss.innerHTML = '<svg viewBox="0 0 140 40" width="140" height="40"><path d="M0 38 L20 30 L32 36 L48 22 L62 32 L74 14 L88 30 L100 20 L118 34 L140 26" fill="none" stroke="#1E293B" stroke-width="4"/></svg>'; a.append(riss); rauschen(.6, .3, 200); wackeln(400, 5);
  const hand = h('div', { style: `position:absolute;z-index:24;left:${W / 2 - 50}px;bottom:-200px;width:100px;height:200px` });
  hand.innerHTML = '<svg viewBox="0 0 100 200" width="100" height="200"><g fill="#F1F5F9" stroke="#475569" stroke-width="3" stroke-linecap="round"><rect x="38" y="120" width="10" height="80" rx="5"/><rect x="54" y="120" width="10" height="80" rx="5"/><path d="M26 92 Q50 128 76 92 L76 120 L26 120Z"/><rect x="28" y="40" width="9" height="50" rx="4.5"/><rect x="41" y="30" width="9" height="60" rx="4.5"/><rect x="54" y="34" width="9" height="56" rx="4.5"/><rect x="67" y="46" width="9" height="44" rx="4.5"/><rect class="daumen" x="4" y="80" width="30" height="10" rx="5" transform="rotate(-40 20 85)"/></g></svg>';
  a.append(hand); hand.animate([{ transform: 'none' }, { transform: 'translateY(-235px)' }], { duration: 280, easing: 'cubic-bezier(.2,1.5,.4,1)', fill: 'forwards' }); piep(110, .3, 'sawtooth', .07); await warte(500);
  hand.animate([{ transform: 'translateY(-235px) rotate(0)' }, { transform: 'translateY(-235px) rotate(-12deg)' }], { duration: 160, iterations: 4, direction: 'alternate', fill: 'forwards' });
  const t = h('div', { class: 'blase ohne', style: 'top:18%;text-align:center' }, '💀 Saubere Landung? Knochenstark.'); a.append(t); await warte(1300);
  hand.animate([{ transform: 'translateY(-235px)' }, { transform: 'none' }], { duration: 400, easing: 'ease-in', fill: 'forwards' }); await warte(420); await raus(hand, riss, t); sticker('Süper!', 2); };

// k) Spinne – Wiederholung bestanden (≈ 2,8 s)
FX.spinne = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const netz = h('div', { style: 'position:absolute;z-index:22;right:0;top:0;width:120px;height:120px;opacity:.7' }); netz.innerHTML = '<svg viewBox="0 0 120 120" width="120" height="120" fill="none" stroke="#94A3B8" stroke-width="1.5"><path d="M120 0 L0 120 M120 0 L40 120 M120 0 L0 40 M120 0 L80 120 M120 0 L0 80"/><path d="M90 0 Q95 25 120 30 M60 0 Q70 50 120 60 M30 0 Q45 75 120 90"/></svg>'; a.append(netz);
  const sp = h('div', { style: `position:absolute;z-index:26;left:${W * .62}px;top:-60px;width:60px` }); sp.innerHTML = '<div style="position:absolute;left:29px;bottom:40px;width:2px;height:600px;background:#CBD5E1"></div><svg viewBox="0 0 60 50" width="60" height="50"><g stroke="#111827" stroke-width="3" fill="none" class="beine"><path d="M22 24 L6 12 L0 20 M22 28 L4 28 L0 38 M22 32 L8 42 L4 50 M38 24 L54 12 L60 20 M38 28 L56 28 L60 38 M38 32 L52 42 L56 50"/></g><ellipse cx="30" cy="28" rx="13" ry="14" fill="#111827"/><circle cx="25" cy="24" r="3.5" fill="#FDE047"/><circle cx="35" cy="24" r="3.5" fill="#FDE047"/></svg>';
  a.append(sp); sp.animate([{ transform: 'none' }, { transform: `translateY(${H * .42}px)` }], { duration: 320, easing: 'cubic-bezier(.3,1.5,.5,1)', fill: 'forwards' }); piep(1400, .08, 'square', .05); await warte(350);
  sp.querySelector('.beine').animate([{ transform: 'scaleX(1)' }, { transform: 'scaleX(.8)' }], { duration: 120, iterations: 8, direction: 'alternate', transformOrigin: '30px 28px' });
  const schild = h('div', { style: `position:absolute;z-index:27;left:${W * .62 - 70}px;top:${H * .42 + 70}px;background:#fff;color:#111;border:2px solid #111;border-radius:8px;padding:6px 10px;font:800 15px system-ui;transform:rotate(3deg)` }, '🕸️ Sitzt noch!'); a.append(schild); await warte(1300);
  sp.animate([{ transform: `translateY(${H * .42}px)` }, { transform: 'none' }], { duration: 600, easing: 'ease-in', fill: 'forwards' }); await raus(schild); await warte(250); await raus(sp, netz); sticker('Hält stabil.', 1); };

Object.assign(FX_GRUND, { clown: () => landung('direkt'), stromausfall: flug, krake: expedition, knochenhand: () => landung('sauber'), spinne: () => wdh('ok') });
function expedition() { return [h('div', { class: 'szene', style: 'background:linear-gradient(180deg,#E0F2FE,#93C5FD);color:#0B2545;min-height:300px' }, h('div', { class: 'oben' }, '⛯ STATION 4 VON 16 · TROLL-STATION'), h('div', { class: 'titel' }, 'Expedition geschafft'), h('div', { class: 'riesig' }, '150 ★'), h('p', { class: 'unter' }, 'Alle Teile gelöst.')),
  h('div', { class: 'blatt' }, h('div', { class: 'kann' }, h('b', {}, 'DU KANNST JETZT'), 'Trapez, Proportionen, Funktionswerte'), h('button', { class: 'knopf' }, 'Weiter ›'))]; }
LANG.push('clown', 'stromausfall', 'krake', 'gehirn', 'phoenix', 'tornado', 'feuerwerk');
