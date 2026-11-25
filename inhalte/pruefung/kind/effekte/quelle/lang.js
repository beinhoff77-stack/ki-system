// ---------- Ton (nur nach Antippen, nur wenn eingeschaltet) ----------
let AC = null; const ton = () => { if (!S.ton) return null; try { AC = AC || new (window.AudioContext || window.webkitAudioContext)(); if (AC.state === 'suspended') AC.resume(); return AC; } catch { return null; } };
function piep(f = 880, d = 0.12, typ = 'square', vol = 0.08) { const c = ton(); if (!c) return; const o = c.createOscillator(), g = c.createGain(); o.type = typ; o.frequency.value = f; g.gain.setValueAtTime(vol, c.currentTime); g.gain.exponentialRampToValueAtTime(0.0001, c.currentTime + d); o.connect(g).connect(c.destination); o.start(); o.stop(c.currentTime + d); }
function rauschen(d = 1, vol = 0.25, tief = 400) { const c = ton(); if (!c) return; const n = c.createBuffer(1, c.sampleRate * d, c.sampleRate), x = n.getChannelData(0); for (let i = 0; i < x.length; i++) x[i] = (Math.random() * 2 - 1) * (1 - i / x.length);
  const s = c.createBufferSource(), f = c.createBiquadFilter(), g = c.createGain(); f.type = 'lowpass'; f.frequency.value = tief; g.gain.value = vol; s.buffer = n; s.connect(f).connect(g).connect(c.destination); s.start(); }
function sirene(d = 1.6) { const c = ton(); if (!c) return; const o = c.createOscillator(), g = c.createGain(); o.type = 'sawtooth'; g.gain.value = 0.05; for (let t = 0; t < d; t += 0.4) { o.frequency.setValueAtTime(660, c.currentTime + t); o.frequency.linearRampToValueAtTime(990, c.currentTime + t + 0.2); o.frequency.linearRampToValueAtTime(660, c.currentTime + t + 0.4); } o.connect(g).connect(c.destination); o.start(); o.stop(c.currentTime + d); }
// ---------- Hilfen ----------
const wackeln = async (ms, px = 6) => { const a = app(); const t0 = performance.now(); while (!abbruch && performance.now() - t0 < ms) { a.style.transform = `translate(${(Math.random() - .5) * px * 2}px,${(Math.random() - .5) * px}px)`; await warte(40); } a.style.transform = ''; };
function teilchen(x, y, n, opt = {}) { // einfache Schwerkraft-Teilchen (DOM)
  const a = app(), R = a.getBoundingClientRect(), liste = [];
  for (let i = 0; i < n; i++) { const inhalt = opt.inhalt ? opt.inhalt[i % opt.inhalt.length] : ''; const el = h('div', { style: `position:absolute;z-index:${opt.z || 26};left:0;top:0;font:900 ${opt.gross || 24}px system-ui;color:${opt.farbe || '#FFD23F'};pointer-events:none;${opt.punkt ? `width:${opt.punkt}px;height:${opt.punkt}px;border-radius:50%;background:${opt.farbe || '#FFD23F'};box-shadow:0 0 10px ${opt.farbe || '#FFD23F'}` : ''}` }, inhalt);
    a.append(el); const w = Math.random() * Math.PI * (opt.rund ? 2 : 1) + (opt.rund ? 0 : Math.PI); const v = (opt.kraft || 9) * (0.5 + Math.random());
    liste.push({ el, x, y, vx: Math.cos(w) * v, vy: Math.sin(w) * v - (opt.hoch || 0), r: Math.random() * 360, vr: (Math.random() - .5) * 20 }); }
  const g = opt.schwer ?? 0.45, boden = R.height - 30; let lauf = true;
  (function schritt() { if (!lauf) return; for (const p of liste) { p.vy += g; p.x += p.vx; p.y += p.vy; p.r += p.vr; if (opt.prall && p.y > boden) { p.y = boden; p.vy *= -0.45; p.vx *= 0.8; } p.el.style.transform = `translate(${p.x}px,${p.y}px) rotate(${p.r}deg)`; } requestAnimationFrame(schritt); })();
  return { liste, stopp: () => { lauf = false; }, weg: () => { lauf = false; liste.forEach((p) => p.el.remove()); } };
}
function sterneHimmel(n = 70) { const c = h('canvas', { style: 'position:absolute;inset:0;width:100%;height:100%;z-index:21' }); const a = app(); a.append(c); const R = a.getBoundingClientRect(); c.width = R.width; c.height = R.height; const k = c.getContext('2d');
  const st = Array.from({ length: n }, () => ({ x: Math.random() * R.width, y: Math.random() * R.height * 0.8, r: Math.random() * 1.6 + .3, p: Math.random() * 6 })); let lauf = true;
  (function mal(t) { if (!lauf) return; k.clearRect(0, 0, c.width, c.height); for (const s of st) { k.globalAlpha = .5 + .5 * Math.sin(t / 400 + s.p); k.fillStyle = '#fff'; k.beginPath(); k.arc(s.x, s.y, s.r, 0, 7); k.fill(); } requestAnimationFrame(mal); })(0);
  return { c, stopp: () => { lauf = false; } };
}
// ---------- 1) FÜR IMMER – Raketenstart ins eigene Sternbild (≈ 7,5 s) ----------
FX.tresor = async function (e) {
  const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const nacht = h('div', { style: 'position:absolute;inset:0;z-index:20;background:linear-gradient(#020617,#0B1640 55%,#1E1B4B);animation:ein .5s both' }); a.append(nacht); const himmel = sterneHimmel(); rauschen(0.6, 0.08, 200); await warte(500);
  // Sternbild: 11 alte Sterne + Linien
  const alt = [[.14, .2], [.24, .12], [.34, .22], [.44, .15], [.55, .26], [.64, .14], [.74, .22], [.82, .12], [.3, .34], [.5, .36], [.68, .34]].map(([x, y]) => [x * W, y * H]);
  const bild = h('div', { style: 'position:absolute;inset:0;z-index:22' }); bild.innerHTML = `<svg width="${W}" height="${H}" style="position:absolute;inset:0"><polyline points="${alt.map((p) => p.join(',')).join(' ')}" fill="none" stroke="#FDE68A55" stroke-width="1.5" stroke-dasharray="4 4"/>${alt.map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3.5" fill="#FDE68A"/>`).join('')}<line id="neu" x1="${alt[10][0]}" y1="${alt[10][1]}" x2="${alt[10][0]}" y2="${alt[10][1]}" stroke="#FFD23F" stroke-width="2.5"/></svg>`; a.append(bild);
  // Rakete auf der Rampe
  const rak = h('div', { style: `position:absolute;z-index:24;left:${W / 2 - 34}px;top:${H - 210}px;width:68px;height:170px;transition:transform 1.9s cubic-bezier(.55,0,.85,.35)` });
  rak.innerHTML = `<svg viewBox="0 0 68 170" width="68" height="170"><path d="M34 2 C54 26 58 60 56 112 L12 112 C10 60 14 26 34 2Z" fill="#F8FAFC" stroke="#334155" stroke-width="3"/><circle cx="34" cy="56" r="12" fill="#60A5FA" stroke="#334155" stroke-width="3"/><path d="M12 88 L0 124 L14 118Z M56 88 L68 124 L54 118Z" fill="#EF4444" stroke="#334155" stroke-width="3"/><rect x="18" y="80" width="32" height="14" rx="3" fill="#FFD23F"/><text x="34" y="91" font-size="9" font-weight="900" text-anchor="middle" fill="#1B0C3A">RUNDEN</text><g class="flamme" style="transform-origin:34px 114px"><path d="M18 112 Q34 170 50 112Z" fill="#FB923C"/><path d="M25 112 Q34 150 43 112Z" fill="#FDE047"/></g></svg>`;
  const rampe = h('div', { style: `position:absolute;z-index:23;left:0;right:0;bottom:0;height:46px;background:repeating-linear-gradient(90deg,#334155 0 22px,#475569 22px 26px)` });
  a.append(rampe, rak); const flamme = rak.querySelector('.flamme'); flamme.style.opacity = 0;
  // Countdown
  const zahl = h('div', { style: 'position:absolute;z-index:27;left:0;right:0;top:34%;text-align:center;font:900 120px/1 system-ui;color:#FFD23F;text-shadow:0 0 30px #FFD23F88' }); a.append(zahl);
  for (const z of ['3', '2', '1']) { if (abbruch) break; zahl.textContent = z; zahl.animate([{ transform: 'scale(1.8)', opacity: 0 }, { transform: 'scale(1)', opacity: 1 }, { transform: 'scale(.9)', opacity: 0 }], { duration: 650 }); piep(z === '1' ? 990 : 660, .15); await warte(650); }
  zahl.textContent = 'START!'; zahl.style.fontSize = '64px'; zahl.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 700, fill: 'forwards' }); piep(1320, .3, 'sawtooth');
  // Start: Rauch, Wackeln, Aufstieg
  flamme.style.opacity = 1; flamme.animate([{ transform: 'scaleY(1)' }, { transform: 'scaleY(1.35)' }], { duration: 90, iterations: 40, direction: 'alternate' }); rauschen(2.4, 0.35, 300);
  const rauch = teilchen(W / 2, H - 60, 26, { inhalt: ['☁️'], gross: 34, kraft: 7, schwer: -0.02, z: 23 });
  wackeln(1200, 7); await warte(250); rak.style.transform = `translateY(${-(H + 40)}px)`; await warte(1700); rauch.weg(); rampe.remove();
  // Explosion zum Stern, Linie zum neuen Stern
  const ziel = [.86 * W, .3 * H]; const stern = h('div', { style: `position:absolute;z-index:25;left:${ziel[0] - 14}px;top:${ziel[1] - 14}px;width:28px;height:28px;background:#FFD23F;clip-path:polygon(50% 0,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%);filter:drop-shadow(0 0 12px #FFD23F);animation:pop .5s both` });
  const funken = teilchen(ziel[0], ziel[1], 34, { punkt: 6, rund: true, kraft: 7, schwer: 0.12 }); a.append(stern); piep(1568, .5, 'triangle', .1); piep(2093, .7, 'sine', .07);
  const neu = bild.querySelector('#neu'); neu.animate([{ x2: alt[10][0], y2: alt[10][1] }, { x2: ziel[0], y2: ziel[1] }], { duration: 600, fill: 'forwards' }); neu.setAttribute('x2', ziel[0]); neu.setAttribute('y2', ziel[1]);
  await warte(700); funken.weg();
  // Text
  const t = h('div', { style: 'position:absolute;z-index:27;left:16px;right:16px;top:44%;text-align:center;color:#fff' }, h('div', { style: 'font:900 44px/1 system-ui;color:#FFD23F;letter-spacing:.04em;text-shadow:0 0 24px #FFD23F66' }, 'FÜR IMMER'),
    h('div', { style: 'font-size:19px;font-weight:800;margin-top:10px' }, 'Runden sitzt – und leuchtet jetzt in deinem Sternbild.'), h('div', { style: 'opacity:.8;margin-top:6px' }, 'Muss nie wieder geübt werden.'), h('div', { style: 'margin-top:14px;font:800 14px ui-monospace,monospace;color:#FDE68A' }, '★ 12 Etappen für immer'));
  t.animate([{ opacity: 0, transform: 'translateY(12px)' }, { opacity: 1, transform: 'none' }], { duration: 450, fill: 'both' }); a.append(t); await warte(2000);
  sticker(e.sticker, 3, 'right:16px;bottom:26px'); await warte(900);
  if (S.ende !== false) { [nacht, bild, t, rak].forEach((x) => x.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 500, fill: 'forwards' })); himmel.c.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 500, fill: 'forwards' }); await warte(520); [nacht, bild, t, rak, himmel.c, stern].forEach((x) => x.remove()); himmel.stopp(); }
};
// ---------- 2) KOFFER – Gepäck-Chaos (≈ 6,5 s) ----------
FX.koffer = async function (e) {
  const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const halle = h('div', { style: 'position:absolute;inset:0;z-index:20;background:linear-gradient(#1F2937,#111827);animation:ein .3s both' }); a.append(halle);
  const licht = h('div', { style: 'position:absolute;z-index:22;left:50%;top:-140px;width:280px;height:280px;margin-left:-140px;border-radius:50%;background:conic-gradient(from 0deg,#F9731600 0 300deg,#F97316cc 330deg,#F9731600 360deg);animation:dreh .8s linear infinite' });
  const lampe = h('div', { style: 'position:absolute;z-index:23;left:50%;top:6px;width:34px;height:22px;margin-left:-17px;border-radius:17px 17px 4px 4px;background:#F97316;box-shadow:0 0 20px #F97316' });
  const banner = h('div', { style: 'position:absolute;z-index:23;left:0;right:0;top:40px;background:repeating-linear-gradient(45deg,#FACC15 0 18px,#111 18px 36px);padding:4px 0' }, h('div', { style: 'background:#FACC15;margin:0 10px;text-align:center;font:900 15px ui-monospace,monospace;color:#111;letter-spacing:.12em;padding:4px' }, '⚠ STÖRUNG · GEPÄCKBAND 3 ⚠'));
  if (!document.getElementById('dreh-k')) document.head.append(h('style', { id: 'dreh-k' }, '@keyframes dreh{to{transform:rotate(360deg)}}'));
  a.append(licht, lampe, banner); sirene(1.8); await warte(700);
  // Band mit drei Koffern
  const bandY = H * 0.62; const band = h('div', { style: `position:absolute;z-index:22;left:0;right:0;top:${bandY}px;height:16px;background:repeating-linear-gradient(90deg,#334155 0 18px,#64748B 18px 22px);animation:band .25s linear infinite` }); a.append(band);
  const kofferSvg = (farbe, tag) => `<svg viewBox="0 0 96 74" width="96" height="74"><rect x="34" y="2" width="28" height="10" rx="4" fill="none" stroke="#1F2937" stroke-width="4"/><rect x="2" y="10" width="92" height="62" rx="9" fill="${farbe}" stroke="#1F2937" stroke-width="3"/><rect class="deckel" x="2" y="10" width="92" height="22" rx="9" fill="${farbe}" stroke="#1F2937" stroke-width="3" style="filter:brightness(1.15)"/><rect x="20" y="10" width="8" height="62" fill="#0003"/><rect x="68" y="10" width="8" height="62" fill="#0003"/>${tag ? `<rect x="58" y="40" width="36" height="16" rx="3" fill="#FFF" stroke="#1F2937" stroke-width="2"/><text x="76" y="52" font-size="9" font-weight="900" text-anchor="middle">${tag}</text>` : ''}</svg>`;
  const k = [['#64748B', ''], ['#EA580C', 'RUNDEN'], ['#0EA5E9', '']].map(([f, t], i) => { const el = h('div', { style: `position:absolute;z-index:24;top:${bandY - 74}px;left:${-110 - i * 130}px;transition:left 1.4s linear` }); el.innerHTML = kofferSvg(f, t); a.append(el); return el; });
  await warte(30); k.forEach((el, i) => { el.style.left = `${W / 2 - 48 + (1 - i) * 125}px`; }); await warte(1400);
  // der mittlere wackelt und bläht sich auf
  const m = k[1]; m.style.transition = 'transform .1s'; for (let i = 0; i < 10 && !abbruch; i++) { m.style.transform = `rotate(${i % 2 ? -6 : 6}deg) scale(${1 + i * 0.035})`; piep(200 + i * 30, .06, 'square', .04); await warte(80); }
  // KABUMM
  const blitz = h('div', { style: 'position:absolute;inset:0;z-index:28;background:#fff;opacity:.85' }); a.append(blitz); setTimeout(() => blitz.remove(), 110); rauschen(0.7, 0.5, 900); wackeln(500, 8);
  const mr = m.getBoundingClientRect(); const mx = mr.left - R.left + 48, my = mr.top - R.top + 30; m.remove();
  const deckel = h('div', { style: `position:absolute;z-index:26;left:${mx - 46}px;top:${my - 20}px;width:92px;height:22px;border-radius:9px;background:#F97316;border:3px solid #1F2937` }); a.append(deckel); deckel.animate([{ transform: 'none' }, { transform: `translate(${W * .3}px,${-H * .5}px) rotate(720deg)`, opacity: 0 }], { duration: 1200, easing: 'cubic-bezier(.2,.7,.4,1)', fill: 'forwards' });
  const zeug = teilchen(mx, my, 30, { inhalt: ['🧦', '👕', '🦆', '3', '7', '¾', '🩳', '9', '½', '🪥', '2', '%'], gross: 28, kraft: 13, hoch: 6, prall: true, schwer: .5 });
  await warte(800);
  // Socke klebt an der Scheibe
  const socke = h('div', { style: 'position:absolute;z-index:29;left:18%;top:16%;font-size:120px;transform:rotate(-18deg) scale(.2);transition:transform .18s cubic-bezier(.3,1.6,.5,1)' }, '🧦'); a.append(socke); await warte(20); socke.style.transform = 'rotate(-18deg) scale(1)'; piep(140, .2, 'sine', .15);
  const text = h('div', { style: 'position:absolute;z-index:30;left:16px;right:16px;top:43%;background:#fff;color:#111;border-radius:14px;padding:12px;text-align:center;font-weight:800;box-shadow:0 8px 24px #0006' }, '🧳 Dein Koffer ist aufgegangen!', h('div', { style: 'font-weight:500;margin-top:4px' }, 'Sammeln wir’s wieder ein.'));
  a.append(text); text.animate([{ opacity: 0, transform: 'scale(.9)' }, { opacity: 1, transform: 'none' }], { duration: 300, fill: 'both' });
  socke.style.transition = 'transform 2.2s ease-in'; await warte(200); socke.style.transform = 'rotate(-6deg) translateY(380px)'; await warte(1000);
  // Zahlen fliegen in drei Kreise = „3 in Folge“
  zeug.stopp(); const kreise = h('div', { style: `position:absolute;z-index:31;left:0;right:0;top:${H * 0.62}px;display:flex;justify-content:center;gap:16px` }, ...[0, 1, 2].map(() => h('div', { style: 'width:46px;height:46px;border-radius:50%;border:4px solid #FDBA74;background:#0006' })));
  const kt = h('div', { style: `position:absolute;z-index:31;left:0;right:0;top:${H * 0.62 + 56}px;text-align:center;color:#FED7AA;font-weight:800` }, '3 richtige in Folge – dann ist alles wieder drin.'); a.append(kreise, kt);
  for (const p of zeug.liste) { p.el.style.transition = 'transform .6s cubic-bezier(.5,0,.3,1),opacity .6s'; p.el.style.transform = `translate(${W / 2}px,${H * 0.62 + 12}px) scale(.2)`; p.el.style.opacity = 0; }
  await warte(650); [...kreise.children].forEach((c, i) => setTimeout(() => { c.style.background = '#FDBA7433'; piep(523 + i * 130, .12, 'triangle'); }, i * 120)); await warte(900);
  if (S.ende !== false) { [halle, licht, lampe, banner, band, text, kreise, kt].forEach((x) => x.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 400, fill: 'forwards' })); k.forEach((x) => x.remove()); await warte(420);
    zeug.weg(); [halle, licht, lampe, banner, band, text, kreise, kt, socke, deckel].forEach((x) => x.remove()); const nb = abflug(true)[1]; nb.style.animation = 'pop2 .45s both'; a.children[0].after(nb); }
};
// ---------- 3) GEHACKT! – Matrix-Einbruch (≈ 6 s) ----------
FX.hacker = async function (e) {
  const a = app(), R = a.getBoundingClientRect();
  a.animate([{ filter: 'none' }, { filter: 'hue-rotate(90deg) saturate(3)', transform: 'skewX(4deg)' }, { filter: 'invert(1)', transform: 'translateX(-6px)' }, { filter: 'none' }], { duration: 380 });
  piep(120, .3, 'sawtooth', .06); await warte(380);
  const s = h('div', { class: 'fx', style: 'background:#000' }); a.append(s); const c = h('canvas', { style: 'position:absolute;inset:0;width:100%;height:100%;opacity:.55' }); s.append(c); c.width = R.width; c.height = R.height; const k = c.getContext('2d');
  const zeichen = '0123456789+−×÷=√π∑%½¾<>'.split(''), sp = Math.floor(R.width / 16), y = Array(sp).fill(0).map(() => Math.random() * -40); let lauf = true;
  (function regen() { if (!lauf) return; k.fillStyle = '#0006'; k.fillRect(0, 0, c.width, c.height); k.fillStyle = '#22FF88'; k.font = '15px monospace'; y.forEach((v, i) => { k.fillText(zeichen[(Math.random() * zeichen.length) | 0], i * 16, v * 16); y[i] = v * 16 > c.height && Math.random() > .96 ? 0 : v + 1; }); setTimeout(() => requestAnimationFrame(regen), 45); })();
  const term = h('div', { class: 'term', style: 'top:14%;background:#000c;padding:10px;border:1px solid #22FF8855;border-radius:8px' }); s.append(term);
  const zeile = async (txt, ms = 10) => { const d = h('div'); term.append(d); for (const ch of txt) { d.textContent += ch; if (ch !== ' ') piep(1800 + Math.random() * 600, .015, 'square', .02); await warte(ms); } };
  await zeile('> VERBINDE MIT MATHE-ZENTRALE …'); await zeile('> UMGEHE FIREWALL … OK', 8); await zeile('> ENTSCHLÜSSELE BRÜCHE … OK', 8);
  const balken = h('div', { style: 'margin-top:6px' }); term.append(balken);
  for (let p = 0; p <= 100 && !abbruch; p += 4) { const n = Math.round(p / 5); balken.textContent = `[${'█'.repeat(n)}${'░'.repeat(20 - n)}] ${p}%`; await warte(40); }
  // Warnung
  const warn = h('div', { style: 'position:absolute;left:12px;right:12px;top:56%;background:#F59E0B;color:#111;text-align:center;font:900 22px ui-monospace,monospace;letter-spacing:.08em;padding:12px;border-radius:8px;box-shadow:0 0 40px #F59E0B88' }, '⚠ FIREWALL DURCHBROCHEN'); s.append(warn); piep(440, .25, 'square', .08); await warte(260); piep(440, .25, 'square', .08); wackeln(500, 5); await warte(700);
  warn.style.background = '#22FF88'; warn.style.boxShadow = '0 0 40px #22FF8888'; warn.textContent = 'ZUGRIFF GEWÄHRT'; piep(988, .15, 'triangle'); await warte(150); piep(1319, .3, 'triangle');
  await zeile('> HACKER IDENTIFIZIERT: DU', 12); await zeile('> GRUND: 10 VON 10 RICHTIG', 12);
  sticker(e.sticker, 3, 'left:50%;top:76%;translate:-50% 0'); await warte(1300); lauf = false;
  if (S.ende !== false) { s.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 350, fill: 'forwards' }); await warte(360); s.remove(); sticker(e.sticker, 3, 'right:20px;bottom:150px'); }
};
const LANG = ['tresor', 'koffer', 'hacker'];
