// Fassung A „Sonnensystem“: Sonne am Rand, Bahnen als Bögen, Planeten mit Monden (ein Mond je Regel).
const himmel = document.getElementById('himmel');
function zufall(saat) { let s = saat; return () => { s = (s * 1664525 + 1013904223) % 4294967296; return s / 4294967296; }; }

function lage(W, Hfenster) {
  const hoch = W < 900; const L = { hoch, W };
  const klein = [24, 31, 22, 31, 28, 24]; // Radius nach Zahl der Regeln (2, 4, Erde, 4, 3, 2)
  if (hoch) {
    const u = Math.min(W / 360, 1.57); L.u = u; L.sonneR = 118 * u; L.C = { x: W / 2, y: -L.sonneR * 0.42 };
    const r1 = L.sonneR + 128 * u, schritt = 84 * u, muster = [-0.72, 0.74, -0.5, 0.78, -0.7, 0.62];
    L.bahnen = klein.map((_, i) => r1 + i * schritt); L.guertel = L.bahnen[5] + schritt * 0.92;
    L.planeten = L.bahnen.map((r, i) => { const hw = Math.min(W / 2 - 62 * u, r * 0.55), x = muster[i] * hw; return { x: L.C.x + x, y: L.C.y + Math.sqrt(r * r - x * x), R: klein[i] * Math.min(u, 1.35) }; });
    L.H = L.C.y + L.guertel + 86; L.guertelPunkt = { x: W / 2, y: L.C.y + L.guertel };
    L.sonneText = { x: W / 2, y: L.sonneR * 0.58 * 0.5 + 4 }; L.titel = { x: W / 2, y: L.sonneR * 0.58 + 30 * u, anker: 'middle' };
  } else {
    const u = Math.max(0.72, Math.min(W / 1280, 1.25)); L.u = u; L.H = Math.max(Hfenster, 560); L.sonneR = 150 * u; L.C = { x: -L.sonneR * 0.38, y: L.H / 2 };
    const r1 = L.sonneR + 150 * u, schritt = 150 * u, muster = [-0.55, 0.6, -0.3, 0.7, -0.62, 0.5];
    L.bahnen = klein.map((_, i) => r1 + i * schritt); L.guertel = L.bahnen[5] + schritt * 0.93;
    L.planeten = L.bahnen.map((r, i) => { const hh = Math.min(L.H / 2 - 120, r * 0.5), y = muster[i] * hh; return { x: L.C.x + Math.sqrt(r * r - y * y), y: L.C.y + y, R: klein[i] * 1.2 * Math.max(u, 0.9) }; });
    L.guertelPunkt = { x: L.C.x + L.guertel, y: L.C.y };
    L.sonneText = { x: L.sonneR * 0.62 * 0.46, y: L.C.y + 2 }; L.titel = { x: 66, y: 36, anker: 'start' };
  }
  return L;
}

function planetBild(p, q, C, i) {
  const R = q.R, dx = C.x - q.x, dy = C.y - q.y, d = Math.hypot(dx, dy), lx = dx / d, ly = dy / d, tinte = '#11161D';
  let extra = '', glyph = '';
  if (p.id === 'waage') extra = `<ellipse rx="${R * 1.5}" ry="${R * 0.3}" fill="none" stroke="${p.hell}" stroke-width="${R * 0.09}" opacity=".85"/>`;
  if (p.id === 'bruch') glyph = `<rect x="${-R * 0.5}" y="${-R * 0.07}" width="${R}" height="${R * 0.14}" rx="${R * 0.07}" fill="${tinte}" opacity=".8"/><circle cy="${-R * 0.42}" r="${R * 0.12}" fill="${tinte}" opacity=".8"/><circle cy="${R * 0.42}" r="${R * 0.12}" fill="${tinte}" opacity=".8"/>`;
  else if (p.erde) glyph = `<g clip-path="url(#cp${i})" fill="#45E0A0" opacity=".9"><ellipse cx="${-R * 0.35}" cy="${-R * 0.2}" rx="${R * 0.42}" ry="${R * 0.3}"/><ellipse cx="${R * 0.4}" cy="${R * 0.35}" rx="${R * 0.4}" ry="${R * 0.26}"/><ellipse cx="${R * 0.45}" cy="${-R * 0.55}" rx="${R * 0.25}" ry="${R * 0.14}"/></g>`;
  else glyph = `<text y="${R * (p.id === 'klammer' ? 0.2 : 0.3)}" text-anchor="middle" font-family="var(--mono)" font-weight="800" font-size="${R * (p.id === 'klammer' ? 0.68 : 0.95)}" fill="${tinte}" opacity=".82">${p.zeichen}</text>`;
  return `${extra}<clipPath id="cp${i}"><circle r="${R}"/></clipPath><circle r="${R}" fill="${p.dunkel}"/><circle r="${R}" cx="${lx * R * 0.36}" cy="${ly * R * 0.36}" fill="${p.hell}" clip-path="url(#cp${i})"/>
    ${glyph}<circle r="${R}" fill="none" stroke="var(--planet-rand)" stroke-width="1.25"/>
    ${p.id === 'waage' ? `<path d="M${-R * 1.5} 0A${R * 1.5} ${R * 0.3} 0 0 0 ${R * 1.5} 0" fill="none" stroke="${p.hell}" stroke-width="${R * 0.09}"/>` : ''}`;
}
function monde(p, q) {
  if (p.erde) return `<g class="kreisen" style="animation-duration:38s"><path transform="translate(${q.R + 13} 0) rotate(180) scale(.62)" d="M0 -13c1.6 0 2.4 2 2.4 4.5v4L13 2v3L2.4 2.5v5L6 10.5V13L0 11.5 -6 13v-2.5l3.6 -3v-5L-13 5V2l10.600 -6.500v-4C-2.4 -11 -1.6 -13 0 -13z" fill="var(--text)" stroke="var(--himmel-unten)" stroke-width="1.5"/></g>`;
  const n = p.regeln.length, rr = q.R + 12;
  return `<g class="kreisen" style="animation-duration:${44 + n * 9}s">${p.regeln.map((nr, j) => { const w = -1.2 + j * (Math.PI * 2 / n), x = Math.cos(w) * rr, y = Math.sin(w) * rr, z = zustand(nr);
    return z === 's' ? `<circle cx="${x}" cy="${y}" r="5.5" fill="var(--text)"/>` : z === 'a' ? `<circle cx="${x}" cy="${y}" r="4.6" fill="var(--himmel-unten)" stroke="var(--text)" stroke-width="2.3"/>`
      : z === 'k' ? `<circle cx="${x}" cy="${y}" r="4.6" fill="var(--himmel-unten)" stroke="var(--leise)" stroke-width="1.7" stroke-dasharray="2 2.6"/>` : `<circle cx="${x}" cy="${y}" r="3.6" fill="var(--leise)"/>`; }).join('')}</g>`;
}
function ansage(p) {
  if (p.erde) return 'Erde. Zurück zu deiner Reise.';
  const z = p.regeln.map(zustand), n = (k) => z.filter((x) => x === k).length;
  return `Planet ${p.name}, ${p.regeln.length} Regeln` + (z[0] ? `: ${n('s')} sitzen, ${n('a')} in Arbeit, ${n('k')} kommen später.` : '.');
}

function maleHimmel() {
  const W = himmel.clientWidth, L = lage(W, innerHeight), C = L.C, z = zufall(7), nacht = document.body.dataset.g === 'nacht';
  himmel.style.height = L.H + 'px';
  let sterne = ''; const zahl = Math.round(W * L.H / (nacht ? 5200 : 9000));
  for (let i = 0; i < zahl; i++) { const x = z() * W, y = z() * L.H, r = 0.5 + z() * (nacht ? 1.1 : 0.9), o = 0.25 + z() * 0.6; sterne += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${r.toFixed(2)}" opacity="${o.toFixed(2)}"${nacht && z() < 0.12 ? ` class="funkeln" style="animation-delay:${(z() * 6).toFixed(1)}s"` : ''}/>`; }
  const laden = EIN.lage === 'laden', fehler = EIN.lage === 'fehler';
  const bahnen = L.bahnen.map((r) => `<circle cx="${C.x}" cy="${C.y}" r="${r}"/>`).join('');
  const planeten = (laden || fehler) ? (laden ? L.planeten.map((q) => `<circle class="warten" cx="${q.x}" cy="${q.y}" r="${q.R}" fill="none" stroke="var(--bahn)" stroke-width="2" stroke-dasharray="4 5"/>`).join('') : '')
    : PLANETEN.map((p, i) => { const q = L.planeten[i]; let tx, anker, ty;
      if (L.hoch) { const links = q.x < W / 2; tx = links ? q.R + 26 : -(q.R + 26); anker = links ? 'start' : 'end'; ty = -2; } else { tx = 0; anker = 'middle'; ty = q.R + 38; }
      return `<g class="planet" role="button" tabindex="0" data-planet="${p.id}" aria-label="${ansage(p)}" transform="translate(${q.x.toFixed(1)} ${q.y.toFixed(1)})">
        <circle r="${Math.max(q.R + 20, 34)}" fill="transparent"/>${p.erde && P.get('von') === 'erde' ? `<circle class="ankunft" r="${q.R}" fill="none" stroke="var(--text)" stroke-width="2"/>` : ''}<g class="anflug" style="animation-delay:${i * 70}ms;transform-origin:${(C.x - q.x).toFixed(1)}px ${(C.y - q.y).toFixed(1)}px">${planetBild(p, q, C, i)}${monde(p, q)}</g>
        <g class="schild" style="animation-delay:${500 + i * 70}ms"><text class="name" x="${tx}" y="${ty}" text-anchor="${anker}">${p.name}</text><text class="unter" x="${tx}" y="${ty + 22}" text-anchor="${anker}">${p.erde ? 'Deine Reise ›' : p.regeln.length + ' Regeln'}</text></g></g>`; }).join('');
  const g = L.guertelPunkt, steine = [[-124, -9, 5], [-112, 8, 3.5], [112, -10, 4], [126, 7, 5.5], [-142, 5, 3]].map(([x, y, r]) => (L.hoch ? `<path transform="translate(${g.x + x} ${g.y + y - Math.abs(x) * Math.abs(x) / (2 * L.guertel)})" d="M${-r} ${-r * 0.3}L${-r * 0.2} ${-r}L${r} ${-r * 0.4}L${r * 0.7} ${r * 0.8}L${-r * 0.5} ${r}z"/>` : `<path transform="translate(${g.x + y - x * x / (2 * L.guertel)} ${g.y + x * 1.25})" d="M${-r} ${-r * 0.3}L${-r * 0.2} ${-r}L${r} ${-r * 0.4}L${r * 0.7} ${r * 0.8}L${-r * 0.5} ${r}z"/>`)).join('');
  const guertel = (laden || fehler) ? '' : `<g class="planet guertel" role="button" tabindex="0" data-guertel aria-label="Werkzeug-Gürtel, 5 Arbeitsweisen"><g fill="var(--leise)">${steine}</g>
      <g transform="translate(${g.x} ${g.y})"><rect x="-100" y="-29" width="200" height="58" rx="29" fill="var(--flaeche)" stroke="var(--linie)" stroke-width="1.5"/><text class="name" y="-3" text-anchor="middle" style="font-size:18px;stroke:none">Werkzeug-Gürtel</text><text class="unter" y="18" text-anchor="middle" style="font-size:16px;stroke:none">5 Arbeitsweisen</text></g></g>`;
  himmel.innerHTML = `<svg width="${W}" height="${L.H}" viewBox="0 0 ${W} ${L.H}" role="group" aria-label="Sonnensystem der Regeln">
    <defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--himmel-oben)"/><stop offset="1" stop-color="var(--himmel-unten)"/></linearGradient>
      <radialGradient id="sg"><stop offset=".55" stop-color="var(--sonne)" stop-opacity=".5"/><stop offset="1" stop-color="var(--sonne)" stop-opacity="0"/></radialGradient></defs>
    <rect width="${W}" height="${L.H}" fill="url(#hg)"/><g fill="var(--stern)">${sterne}</g>
    <g fill="none" stroke="var(--bahn)" stroke-width="1.25">${bahnen}</g>
    <g fill="none" stroke="var(--leise)" stroke-linecap="round" opacity=".55"><circle cx="${C.x}" cy="${C.y}" r="${L.guertel - 5}" stroke-width="3.5" stroke-dasharray="0.1 17"/><circle cx="${C.x}" cy="${C.y}" r="${L.guertel + 6}" stroke-width="2.5" stroke-dasharray="0.1 29"/><circle cx="${C.x}" cy="${C.y}" r="${L.guertel + 1}" stroke-width="5" stroke-dasharray="0.1 53"/></g>
    <circle class="schein" cx="${C.x}" cy="${C.y}" r="${L.sonneR * 1.75}" fill="url(#sg)"/>
    <g class="planet sonne" role="button" tabindex="0" data-sonne aria-label="Sonne: alle 15 Regeln auf einen Blick"><circle cx="${C.x}" cy="${C.y}" r="${L.sonneR}" fill="var(--sonne)" stroke="var(--sonne-rand)" stroke-width="2"/>
      <text x="${L.sonneText.x}" y="${L.sonneText.y}" text-anchor="middle" font-size="${32 * Math.min(L.u, 1.3)}" font-weight="700" fill="#11161D">15</text><text x="${L.sonneText.x}" y="${L.sonneText.y + 19 * Math.min(L.u, 1.3)}" text-anchor="middle" font-family="var(--mono)" font-size="${12.5 * Math.min(L.u, 1.2)}" font-weight="700" letter-spacing="1.6" fill="#11161D">REGELN</text></g>
    ${fehler ? '' : `<text class="titel" x="${L.titel.x}" y="${L.titel.y}" text-anchor="${L.titel.anker}">${L.hoch ? 'Mehr sind es nicht.' : '15 Regeln. Mehr sind es nicht.'}</text><text class="unter" x="${L.titel.x}" y="${L.titel.y + 25}" text-anchor="${L.titel.anker}">${laden ? 'Die Regeln werden geholt …' : 'Tippe auf einen Planeten.'}</text>`}
    ${planeten}${guertel}</svg>
    ${(laden || fehler) ? '' : `<div class="a-legende">${legende()}</div>`}
    ${fehler ? `<div class="stoerung" role="alert"><p><b>Die Regeln sind gerade nicht zu erreichen.</b></p><p class="leise">Prüfe das Internet und versuch es nochmal.</p><button class="haupt" data-nochmal>Nochmal versuchen</button><button class="zweit" data-reise style="width:100%;margin-top:8px">Zur Reise</button></div>` : ''}`;
  const druck = (wahl, f) => himmel.querySelectorAll(wahl).forEach((e) => { e.addEventListener('click', () => f(e)); e.addEventListener('keydown', (ev) => { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); f(e); } }); });
  druck('[data-planet]', (e) => (e.dataset.planet === 'erde' ? zurReise() : oeffnePlanet(e.dataset.planet)));
  druck('[data-sonne]', oeffneSonne); druck('[data-guertel]', oeffneGuertel);
  himmel.querySelector('[data-nochmal]')?.addEventListener('click', () => { P.set('lage', 'normal'); location.search = P.toString(); });
  himmel.querySelector('[data-reise]')?.addEventListener('click', zurReise);
}
function zurReise() { melde('Hier fliegt die Ansicht zurück zur Reisekarte (siehe „Drei Wege“).'); }
document.querySelector('.kopf-zurueck').addEventListener('click', zurReise);
maleHimmel(); let t; addEventListener('resize', () => { clearTimeout(t); t = setTimeout(() => { document.body.classList.add('still'); maleHimmel(); }, 120); });
entwurfsSchalter(SEITEN);
const auf = P.get('auf'); if (auf) setTimeout(() => (auf === 'sonne' ? oeffneSonne() : auf === 'guertel' ? oeffneGuertel() : /^\d+$/.test(auf) ? oeffneRegel(+auf, 'frei', true) : oeffnePlanet(auf)), 50);
