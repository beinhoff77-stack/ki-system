// Fassung B „Planetenreihe“: Sonne und Planeten an einer Linie, alle Regel-Namen sofort lesbar. Keine Bewegung.
const reihe = document.getElementById('reihe');
function planetBildKlein(p, R, i) {
  const tinte = '#11161D'; let glyph;
  if (p.id === 'bruch') glyph = `<rect x="${-R * 0.5}" y="${-R * 0.07}" width="${R}" height="${R * 0.14}" rx="${R * 0.07}" fill="${tinte}" opacity=".8"/><circle cy="${-R * 0.42}" r="${R * 0.12}" fill="${tinte}" opacity=".8"/><circle cy="${R * 0.42}" r="${R * 0.12}" fill="${tinte}" opacity=".8"/>`;
  else if (p.erde) glyph = `<g clip-path="url(#k${i})" fill="#45E0A0" opacity=".9"><ellipse cx="${-R * 0.35}" cy="${-R * 0.2}" rx="${R * 0.42}" ry="${R * 0.3}"/><ellipse cx="${R * 0.4}" cy="${R * 0.35}" rx="${R * 0.4}" ry="${R * 0.26}"/></g>`;
  else glyph = `<text y="${R * (p.id === 'klammer' ? 0.2 : 0.3)}" text-anchor="middle" font-family="var(--mono)" font-weight="800" font-size="${R * (p.id === 'klammer' ? 0.68 : 0.95)}" fill="${tinte}" opacity=".82">${p.zeichen}</text>`;
  const b = p.id === 'waage' ? R * 1.5 : R, g = (b + 2) * 2;
  return `<svg class="scheibe" width="${g}" height="${(R + 2) * 2}" viewBox="${-b - 2} ${-R - 2} ${g} ${(R + 2) * 2}" aria-hidden="true">${p.id === 'waage' ? `<ellipse rx="${R * 1.5}" ry="${R * 0.3}" fill="none" stroke="${p.hell}" stroke-width="${R * 0.1}"/>` : ''}
    <clipPath id="k${i}"><circle r="${R}"/></clipPath><circle r="${R}" fill="${p.dunkel}"/><circle r="${R}" cx="${p.quer ? -R * 0.36 : 0}" cy="${p.quer ? 0 : -R * 0.36}" fill="${p.hell}" clip-path="url(#k${i})"/>${glyph}<circle r="${R}" fill="none" stroke="var(--planet-rand)" stroke-width="1.25"/>
    ${p.id === 'waage' ? `<path d="M${-R * 1.5} 0A${R * 1.5} ${R * 0.3} 0 0 0 ${R * 1.5} 0" fill="none" stroke="${p.hell}" stroke-width="${R * 0.1}"/>` : ''}</svg>`;
}
const sonneBild = (R) => `<svg class="scheibe" width="${R * 2 + 4}" height="${R * 2 + 4}" viewBox="${-R - 2} ${-R - 2} ${R * 2 + 4} ${R * 2 + 4}" aria-hidden="true"><circle r="${R}" fill="var(--sonne)" stroke="var(--sonne-rand)" stroke-width="2"/><text y="${R * 0.28}" text-anchor="middle" font-weight="700" font-size="${R * 0.8}" fill="#11161D" font-family="Space Grotesk, system-ui">15</text></svg>`;
const steine = `<svg class="scheibe" width="44" height="30" viewBox="-22 -15 44 30" aria-hidden="true" fill="var(--leise)"><path d="M-14 -3l4 -5 6 3 -1 6 -6 2z"/><path d="M2 -9l5 -2 3 4 -4 3z"/><path d="M6 3l6 -2 3 5 -5 4 -5 -2z"/><path d="M-8 7l4 -1 2 3 -4 2z"/></svg>`;
function ansageB(p) { const z = p.regeln.map(zustand), n = (k) => z.filter((x) => x === k).length; return `Planet ${p.name}, ${p.regeln.length} Regeln` + (z[0] ? `: ${n('s')} sitzen, ${n('a')} in Arbeit, ${n('k')} kommen später` : ''); }
function maleReihe() {
  const W = innerWidth, quer = W >= 900, gross = W >= 600, laden = EIN.lage === 'laden';
  if (EIN.lage === 'fehler') { reihe.className = ''; reihe.innerHTML = `<div class="stoerung" role="alert"><p><b>Die Regeln sind gerade nicht zu erreichen.</b></p><p class="leise">Prüfe das Internet und versuch es nochmal.</p><button class="haupt" data-nochmal>Nochmal versuchen</button><button class="zweit" data-reise style="width:100%;margin-top:8px">Zur Reise</button></div>`;
    reihe.querySelector('[data-nochmal]').addEventListener('click', () => { P.set('lage', 'normal'); location.search = P.toString(); }); reihe.querySelector('[data-reise]').addEventListener('click', zurReise); return; }
  const name = (nr) => (laden ? `<span class="eins grau">${REGELN[nr].name}</span>` : `<span class="eins">${mond(nr)}${REGELN[nr].name}</span>`);
  if (!quer) {
    reihe.className = 'reihe';
    reihe.innerHTML = `<button class="r-zeile r-sonne" data-sonne aria-label="Sonne: alle 15 Regeln auf einen Blick">${sonneBild(gross ? 32 : 26)}<span><b>15 Regeln. Mehr sind es nicht.</b>${laden ? '<span class="satz">Die Regeln werden geholt …</span>' : gross ? '<span class="satz">Sie kommen in jedem Thema wieder.</span>' : ''}</span><span class="pfeil" aria-hidden="true">›</span></button>`
      + PLANETEN.map((p, i) => (p.erde ? `<button class="r-zeile r-erde" data-erde aria-label="Erde. Zurück zu deiner Reise.">${planetBildKlein(p, gross ? 19 : 15, i)}<span><b>Erde</b><span class="namen leise">Deine Reise</span></span><span class="pfeil" aria-hidden="true">›</span></button>`
        : `<button class="r-zeile" data-planet="${p.id}" aria-label="${ansageB(p)}">${planetBildKlein(p, gross ? 26 : 20, i)}<span><b>${p.name}</b><span class="namen">${p.regeln.map(name).join('')}</span></span><span class="pfeil" aria-hidden="true">›</span></button>`)).join('')
      + `<button class="r-zeile" data-guertel aria-label="Werkzeug-Gürtel, 5 Arbeitsweisen">${steine}<span><b>Werkzeug-Gürtel</b><span class="namen leise">${WERKZEUGE.map((w) => `<span class="eins">${w.name}</span>`).join('')}</span></span><span class="pfeil" aria-hidden="true">›</span></button>`
      + `<div class="r-fuss">${legende()}</div>`;
  } else {
    reihe.className = 'reihe quer';
    reihe.innerHTML = `<div class="q-kopf"><h1>15 Regeln. Mehr sind es nicht.</h1><p>${laden ? 'Die Regeln werden geholt …' : 'Sie kommen in jedem Thema wieder, nur in neuem Gewand.'}</p></div>
      <div class="q-spalte"><button class="q-planet" data-sonne aria-label="Sonne: alle 15 Regeln auf einen Blick"><span class="platz">${sonneBild(36)}</span><b>Sonne</b></button><button class="q-regel" data-sonne><span>Alle 15 in einer Liste</span></button><button class="q-regel" data-erde>${planetBildKlein(PLANETEN[2], 10, 9)}<span>Zur Erde: deine Reise</span></button></div>`
      + PLANETEN.filter((p) => !p.erde).map((p, i) => `<div class="q-spalte"><button class="q-planet" data-planet="${p.id}" aria-label="${ansageB(p)}"><span class="platz">${planetBildKlein({ ...p, quer: true }, 20 + p.regeln.length * 3, i)}</span><b>${p.name}</b></button>${p.regeln.map((nr) => (laden ? `<div class="q-regel"><span class="grau">${REGELN[nr].name}</span></div>` : `<button class="q-regel" data-regel="${nr}">${mond(nr)}<span>${REGELN[nr].name}</span></button>`)).join('')}</div>`).join('')
      + `<div class="q-spalte"><button class="q-planet" data-guertel aria-label="Werkzeug-Gürtel, 5 Arbeitsweisen"><span class="platz">${steine}</span><b>Werkzeug-Gürtel</b></button>${WERKZEUGE.map((w) => `<div class="q-regel">${w.name}</div>`).join('')}</div>${legende()}`;
    reihe.querySelectorAll('[data-regel]').forEach((k) => k.addEventListener('click', () => oeffneRegel(+k.dataset.regel, 'frei', true)));
  }
  reihe.querySelectorAll('[data-planet]').forEach((e) => e.addEventListener('click', () => oeffnePlanet(e.dataset.planet)));
  reihe.querySelectorAll('[data-sonne]').forEach((e) => e.addEventListener('click', oeffneSonne));
  reihe.querySelectorAll('[data-erde]').forEach((e) => e.addEventListener('click', zurReise));
  reihe.querySelectorAll('[data-guertel]').forEach((e) => e.addEventListener('click', oeffneGuertel));
}
function zurReise() { melde('Hier geht es zurück zur Reisekarte.'); }
document.querySelector('.kopf-zurueck').addEventListener('click', zurReise);
maleReihe(); let t; addEventListener('resize', () => { clearTimeout(t); t = setTimeout(maleReihe, 120); });
entwurfsSchalter(SEITEN);
const auf = P.get('auf'); if (auf) setTimeout(() => (auf === 'sonne' ? oeffneSonne() : auf === 'guertel' ? oeffneGuertel() : /^\d+$/.test(auf) ? oeffneRegel(+auf, 'frei', true) : oeffnePlanet(auf)), 50);
