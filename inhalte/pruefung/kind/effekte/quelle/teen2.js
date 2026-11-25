// ================= Streiche (lang, glaubhaft) + Opa =================
function pups() { const c = ton(); if (!c) return; const o = c.createOscillator(), g = c.createGain(), f = c.createBiquadFilter(); o.type = 'sawtooth'; f.type = 'lowpass'; f.frequency.value = 380;
  const t = c.currentTime; o.frequency.setValueAtTime(95, t); for (let i = 0; i < 14; i++) o.frequency.setValueAtTime(70 + (i % 2) * 25 - i * 2, t + i * .055); g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(.35, t + .04); g.gain.setValueAtTime(.3, t + .6); g.gain.exponentialRampToValueAtTime(.0001, t + .85);
  o.connect(f).connect(g).connect(c.destination); o.start(); o.stop(t + .9); rauschen(.8, .12, 250); }
function textNoten(wurzel) { const w = document.createTreeWalker(wurzel, NodeFilter.SHOW_TEXT); const l = []; while (w.nextNode()) if (w.currentNode.textContent.trim()) l.push(w.currentNode); return l; }

// ---------- ABSTURZ (Direktflug, ≈ 10 s) – das Kind soll glauben, es hat etwas kaputt gemacht ----------
FX.absturz = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  // 1) feine Störungen: Buchstaben verrutschen, Knöpfe zittern
  const noten = textNoten(a), orig = noten.map((n) => n.textContent); const zeichen = '▓░▒#%&@$?¿¡ʘ¤§'; const t0 = performance.now();
  while (!abbruch && performance.now() - t0 < 1500) { noten.forEach((n, i) => { if (Math.random() < .12) n.textContent = orig[i].split('').map((c) => (c !== ' ' && Math.random() < .25 ? zeichen[(Math.random() * zeichen.length) | 0] : c)).join(''); else n.textContent = orig[i]; });
    a.querySelectorAll('.knopf').forEach((k) => { k.style.transform = `translate(${(Math.random() - .5) * 4}px,0)`; }); if (Math.random() < .3) piep(3000 + Math.random() * 2000, .02, 'square', .02); await warte(90); }
  noten.forEach((n, i) => { n.textContent = orig[i]; }); a.querySelectorAll('.knopf').forEach((k) => { k.style.transform = ''; });
  // 2) Einfrieren: nichts reagiert
  const frost = h('div', { style: 'position:absolute;inset:0;z-index:30;background:#0000;cursor:wait' }); a.append(frost); const sp = h('div', { style: 'position:absolute;z-index:31;left:50%;top:46%;width:34px;height:34px;margin:-17px;border-radius:50%;border:3px solid #ffffff33;border-top-color:#fff;animation:dreh .8s linear infinite' });
  const hin = h('div', { style: 'position:absolute;z-index:31;left:0;right:0;top:calc(46% + 30px);text-align:center;color:#fff;font:600 13px system-ui;text-shadow:0 1px 3px #000' }, 'Reagiert nicht …'); a.append(sp, hin);
  frost.onpointerdown = (ev) => { const r = a.getBoundingClientRect(); const w = h('div', { style: `position:absolute;z-index:31;left:${ev.clientX - r.left - 20}px;top:${ev.clientY - r.top - 20}px;width:40px;height:40px;border-radius:50%;background:#ffffff55` }); a.append(w); w.animate([{ transform: 'scale(.3)', opacity: 1 }, { transform: 'scale(1.4)', opacity: 0 }], { duration: 400 }); setTimeout(() => w.remove(), 400); };
  a.animate([{ filter: 'none' }, { filter: 'brightness(.7) saturate(.6)' }], { duration: 1800, fill: 'forwards' }); await warte(1900);
  // 3) Absturz-Protokoll
  sp.remove(); hin.remove(); a.animate([{ filter: 'brightness(.7) saturate(.6)' }, { filter: 'none' }], { duration: 10, fill: 'forwards' });
  const log = h('div', { style: 'position:absolute;inset:0;z-index:32;background:#000;color:#D4D4D4;font:500 11px/1.45 ui-monospace,Menlo,monospace;padding:12px;overflow:hidden' }); a.append(log); bass(.4, 40, .6);
  const zeilen = ['FATAL  lernen.js:404  Bordkarte 7: unerwarteter Zustand', '       fehler === 0  (erwartet: ≥ 1)', 'at rechne (lernen.js:1881)', 'at landung (lernen.js:2993)', 'at zuGut (lernen.js:0)', 'WARN   Stern-Zähler: Überlauf', 'WARN   Speicher: 99 % belegt', 'ERROR  Etappe „Runden“: Prüfsumme falsch', 'ERROR  Prozess 7 beendet (Signal 11)', 'dump: 0x0BADF00D 0xDEADBEEF 0x00C0FFEE', 'Sitzung wird beendet …'];
  for (const z of zeilen) { if (abbruch) break; log.append(h('div', { style: z.startsWith('FATAL') || z.startsWith('ERROR') ? 'color:#F87171' : z.startsWith('WARN') ? 'color:#FBBF24' : '' }, z)); piep(4000, .01, 'square', .02); await warte(170); }
  for (let i = 0; i < 18 && !abbruch; i++) { log.append(h('div', {}, Array.from({ length: 6 }, () => '0x' + ((Math.random() * 0xffffffff) >>> 0).toString(16).padStart(8, '0').toUpperCase()).join(' '))); log.scrollTop = log.scrollHeight; await warte(35); }
  // 4) Beendet-Tafel mit Countdown
  const tafel = h('div', { style: 'position:absolute;z-index:33;left:18px;right:18px;top:30%;background:#18181B;border:1px solid #3F3F46;border-radius:14px;padding:16px;color:#E4E4E7;box-shadow:0 20px 60px #000' },
    h('div', { style: 'font:800 17px system-ui' }, 'Die App musste beendet werden.'), h('div', { style: 'margin-top:6px;color:#A1A1AA;font-size:14px' }, 'Ursache: Bordkarte 7 – unerwarteter Zustand (0 Fehler).'), h('div', { class: 'cd', style: 'margin-top:12px;font:700 13px ui-monospace,monospace;color:#FBBF24' }, 'Neustart in 3 …'));
  a.append(tafel); const cd = tafel.querySelector('.cd'); for (const n of [3, 2, 1]) { if (abbruch) break; cd.textContent = `Neustart in ${n} …`; piep(440, .08, 'square', .05); await warte(800); }
  // 5) Schwarz, Neustart
  const schwarz = h('div', { style: 'position:absolute;inset:0;z-index:34;background:#000' }); a.append(schwarz); await warte(800);
  const boot = h('div', { style: 'position:absolute;inset:0;z-index:35;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;background:#000' }, h('div', { style: "font:900 italic 30px 'Arial Black',system-ui;color:#F8FAFC;letter-spacing:.02em" }, 'LERNREISE'), h('div', { style: 'width:140px;height:4px;border-radius:2px;background:#27272A;overflow:hidden' }, h('div', { class: 'p', style: 'height:100%;width:0;background:#F8FAFC' })));
  a.append(boot); boot.querySelector('.p').animate([{ width: '0' }, { width: '100%' }], { duration: 1100, fill: 'forwards' }); await warte(1200);
  // 6) Auflösung
  await rest(boot, schwarz, tafel, log, frost); const t = typo('Reingelegt.', { g: 48, farbe: NEON.cyan, top: '20%' }); rein(t); bass(.7, 40, .7);
  const z = toast('ALLES HEIL', 'Nichts kaputt. Nur ein Direktflug.', NEON.cyan, H * .8); await warte(1800); await rest(t, z); sticker('PEAK', 3); };

// ---------- GEHACKT (10 in Folge, ≈ 11 s) – „Account übernommen“, Sterne laufen weg, dann: der Hacker bist du ----------
FX.hacker = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const chat = h('div', { style: 'position:absolute;z-index:33;left:12px;right:12px;top:14px;background:#0B0F19f2;border:1px solid #ffffff1a;border-radius:14px;padding:10px 12px;color:#E2E8F0' }, h('div', { style: 'font:700 11px ui-monospace,monospace;letter-spacing:.12em;color:#94A3B8' }, 'UNBEKANNT · jetzt'), h('div', { class: 'msg', style: 'margin-top:4px;font-size:15px' }, 'nice serie.'));
  a.append(chat); chat.animate([{ transform: 'translateY(-120%)' }, { transform: 'none' }], { duration: 300, fill: 'both' }); piep(1568, .06, 'sine', .06); const msg = chat.querySelector('.msg');
  await warte(1300); msg.textContent = 'wär schade um deine sterne.'; herz(); await warte(1500);
  // Übernahme
  a.animate([{ filter: 'none' }, { filter: 'hue-rotate(90deg) saturate(3)', transform: 'skewX(4deg)' }, { filter: 'invert(1)', transform: 'translateX(-6px)' }, { filter: 'none' }], { duration: 380 }); piep(120, .3, 'sawtooth', .06); await warte(380); chat.remove();
  const s = h('div', { class: 'fx', style: 'background:#000' }); a.append(s); const c = h('canvas', { style: 'position:absolute;inset:0;width:100%;height:100%;opacity:.45' }); s.append(c); c.width = W; c.height = H; const k = c.getContext('2d');
  const zch = '0123456789+−×÷=√π∑%½¾<>'.split(''), sp = Math.floor(W / 16), y = Array(sp).fill(0).map(() => Math.random() * -40); let lauf = true;
  (function regen() { if (!lauf) return; k.fillStyle = '#0006'; k.fillRect(0, 0, c.width, c.height); k.fillStyle = '#22FF88'; k.font = '15px monospace'; y.forEach((v, i) => { k.fillText(zch[(Math.random() * zch.length) | 0], i * 16, v * 16); y[i] = v * 16 > c.height && Math.random() > .96 ? 0 : v + 1; }); setTimeout(() => requestAnimationFrame(regen), 45); })();
  const kopf = h('div', { style: `position:absolute;left:0;right:0;top:12%;text-align:center;font:${FONT.replace('{g}', 34)};color:#F8FAFC;text-transform:uppercase;text-shadow:-3px 0 #FF2D55aa,3px 0 #22D3EEaa` }, 'Account übernommen'); s.append(kopf); rein(kopf); bass(.8, 34, .9); wackeln(400, 8);
  const stern = h('div', { style: `position:absolute;left:0;right:0;top:30%;text-align:center;font:900 64px/1 ui-monospace,monospace;color:${NEON.gold};font-variant-numeric:tabular-nums;text-shadow:0 0 20px ${NEON.gold}88` }, '★ 1.240'); s.append(stern);
  const ueb = h('div', { style: 'position:absolute;left:24px;right:24px;top:calc(30% + 80px);font:700 12px ui-monospace,monospace;color:#94A3B8;text-align:center' }, 'ÜBERTRAGE STERNE AN: x_sh4dow_x', h('div', { style: 'margin-top:8px;height:6px;border-radius:3px;background:#1F2937;overflow:hidden' }, h('div', { class: 'p', style: 'height:100%;width:0;background:#F43F5E' }))); s.append(ueb);
  const p = ueb.querySelector('.p'); const t0 = performance.now(); while (!abbruch && performance.now() - t0 < 2600) { const q = Math.min(1, (performance.now() - t0) / 2600); stern.textContent = '★ ' + Math.round(1240 * (1 - q)).toLocaleString('de-DE'); p.style.width = q * 100 + '%'; if (Math.random() < .5) piep(900 + Math.random() * 300, .015, 'square', .03); await warte(45); }
  stern.textContent = '★ 0'; stern.style.color = '#F43F5E'; herz(); await warte(700);
  // Terminal: der Spieß dreht sich
  ueb.remove(); kopf.remove(); const term = h('div', { class: 'term', style: 'top:48%;background:#000c;padding:10px;border:1px solid #22FF8855;border-radius:8px' }); s.append(term);
  const zeile = async (txt, ms = 9) => { const d = h('div'); term.append(d); for (const ch of txt) { d.textContent += ch; if (ch !== ' ') piep(1800 + Math.random() * 600, .012, 'square', .02); await warte(ms); } };
  await zeile('> RÜCKVERFOLGUNG …'); await zeile('> QUELLE GEFUNDEN'); await zeile('> HACKER IDENTIFIZIERT: DU'); await zeile('> GRUND: 10 VON 10 RICHTIG');
  const t1 = performance.now(); stern.style.color = NEON.gold; while (!abbruch && performance.now() - t1 < 900) { const q = Math.min(1, (performance.now() - t1) / 900); stern.textContent = '★ ' + Math.round(1240 * q).toLocaleString('de-DE'); await warte(30); } stern.textContent = '★ 1.240';
  const g = h('div', { style: `position:absolute;left:12px;right:12px;top:14%;background:${NEON.gruen};color:#052E16;text-align:center;font:900 24px ui-monospace,monospace;letter-spacing:.08em;padding:10px;border-radius:8px;box-shadow:0 0 40px ${NEON.gruen}88` }, 'ZUGRIFF GEWÄHRT'); s.append(g); piep(988, .15, 'triangle'); await warte(150); piep(1319, .3, 'triangle');
  sticker(e.sticker, 3, 'left:50%;top:80%;translate:-50% 0'); await warte(1500); lauf = false; s.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 350, fill: 'forwards' }); await warte(360); s.remove(); sticker(e.sticker, 3, 'right:20px;bottom:150px'); };

// ---------- OPA (5 in Folge, ≈ 4,5 s) ----------
const OPA = `<svg viewBox="0 0 120 220" width="120" height="220"><g stroke="#1F2937" stroke-width="3" stroke-linejoin="round">
 <rect class="bein1" x="40" y="140" width="16" height="66" rx="6" fill="#57534E"/><rect class="bein2" x="62" y="140" width="16" height="66" rx="6" fill="#57534E"/>
 <ellipse cx="46" cy="210" rx="14" ry="7" fill="#292524"/><ellipse cx="72" cy="210" rx="14" ry="7" fill="#292524"/>
 <path d="M30 80 Q60 66 90 80 L92 150 L28 150Z" fill="#A16207"/><path d="M50 80 L60 120 L70 80" fill="#FEF3C7"/>
 <circle cx="60" cy="50" r="24" fill="#FDE2C8"/><path d="M38 44 Q60 18 82 44" fill="#E7E5E4"/><rect x="34" y="20" width="52" height="10" rx="4" fill="#44403C"/><rect x="42" y="4" width="36" height="20" rx="5" fill="#44403C"/>
 <circle cx="52" cy="52" r="6" fill="#fff"/><circle cx="68" cy="52" r="6" fill="#fff"/><circle cx="53" cy="52" r="2" fill="#111"/><circle cx="69" cy="52" r="2" fill="#111"/><path d="M50 66 Q60 72 70 66" fill="none"/><path d="M44 60 Q60 58 76 60" stroke="#E7E5E4" stroke-width="5"/>
 <path d="M94 90 L104 206" stroke="#78350F" stroke-width="5"/><path d="M88 92 Q96 86 100 94" fill="none" stroke-width="5"/></g></svg>`;
const OPA_HINTEN = `<svg viewBox="0 0 120 220" width="120" height="220"><g stroke="#1F2937" stroke-width="3" stroke-linejoin="round">
 <rect x="40" y="150" width="16" height="56" rx="6" fill="#57534E"/><rect x="62" y="150" width="16" height="56" rx="6" fill="#57534E"/><ellipse cx="46" cy="210" rx="14" ry="7" fill="#292524"/><ellipse cx="72" cy="210" rx="14" ry="7" fill="#292524"/>
 <path d="M26 64 Q60 54 94 64 L96 120 L24 120Z" fill="#A16207" transform="rotate(-28 60 120)"/>
 <path class="popo" d="M22 118 Q24 98 60 100 Q96 98 98 118 Q100 156 60 156 Q20 156 22 118Z" fill="#57534E"/><path d="M60 104 L60 154" stroke-width="2.5"/>
 <circle cx="30" cy="40" r="20" fill="#E7E5E4" transform="translate(-10 18)"/><rect x="2" y="30" width="40" height="8" rx="3" fill="#44403C" transform="rotate(-28 22 34)"/></g></svg>`;
FX.opa = async function (e) { const a = app(), R = a.getBoundingClientRect(), W = R.width, H = R.height;
  const opa = h('div', { style: `position:absolute;z-index:30;left:-130px;top:${H - 250}px;width:120px;height:220px` }); opa.innerHTML = OPA; a.append(opa);
  const geh = opa.animate([{ transform: 'translateY(0) rotate(-2deg)' }, { transform: 'translateY(-6px) rotate(2deg)' }], { duration: 260, iterations: Infinity, direction: 'alternate' });
  opa.animate([{ left: '-130px' }, { left: `${W / 2 - 60}px` }], { duration: 1500, easing: 'linear', fill: 'forwards' }); for (let i = 0; i < 6; i++) { piep(140, .05, 'sine', .08); await warte(250); }
  geh.cancel(); await warte(250); // stehen bleiben, umdrehen
  opa.animate([{ transform: 'scaleX(1)' }, { transform: 'scaleX(0)' }], { duration: 140, fill: 'forwards' }); await warte(140); opa.innerHTML = OPA_HINTEN; opa.animate([{ transform: 'scaleX(0)' }, { transform: 'scaleX(1)' }], { duration: 140, fill: 'forwards' }); await warte(400);
  const popo = opa.querySelector('.popo'); popo.animate([{ transform: 'none' }, { transform: 'translateY(-3px) scale(1.04)' }, { transform: 'none' }], { duration: 150, iterations: 2, transformOrigin: '60px 128px' });
  await warte(250); pups(); wackeln(500, 5);
  const wolke = h('div', { style: `position:absolute;z-index:29;left:${W / 2 - 80}px;top:${H - 190}px;width:160px;height:120px;border-radius:50%;background:radial-gradient(#A3E635aa,#65A30D55 60%,#0000 70%);filter:blur(3px)` }); a.append(wolke);
  wolke.animate([{ transform: 'scale(.2)', opacity: 1 }, { transform: `scale(${W / 90}) translateY(-30px)`, opacity: .85, offset: .6 }, { transform: `scale(${W / 70}) translateY(-40px)`, opacity: 0 }], { duration: 2200, fill: 'forwards' });
  const p = typo('Pffrrrt', { g: 44, farbe: NEON.gruen, top: '30%', split: false }); p.animate([{ transform: 'scale(.4) rotate(-8deg)', opacity: 0 }, { transform: 'scale(1.1) rotate(4deg)', opacity: 1 }, { transform: 'scale(1) rotate(-2deg)' }], { duration: 350, fill: 'both' });
  a.animate([{ filter: 'none' }, { filter: 'sepia(.6) hue-rotate(40deg) saturate(1.6)' }, { filter: 'none' }], { duration: 1800 }); await warte(900);
  const sorry = h('div', { class: 'blase ohne', style: 'top:auto;bottom:16px;text-align:center' }, '„’tschuldigung. 5 in Folge – da musste was raus.“'); a.append(sorry); await warte(900);
  opa.innerHTML = OPA; const geh2 = opa.animate([{ transform: 'translateY(0)' }, { transform: 'translateY(-6px)' }], { duration: 260, iterations: Infinity, direction: 'alternate' }); opa.animate([{ left: `${W / 2 - 60}px` }, { left: `${W + 20}px` }], { duration: 1100, fill: 'forwards' });
  await warte(1100); geh2.cancel(); await rest(opa, wolke, p, sorry); sticker('Locked in.', 2); };

Object.assign(FX_GRUND, { absturz: () => landung('direkt'), opa: () => uebung('ok', '5 richtig in Folge.') });
LANG.push('absturz', 'hacker');
