// Gemeinsame Teile der Entwürfe: Einstellungen aus der Adresse, Blätter, Regel-Karte, Entwurfs-Schalter.
const P = new URLSearchParams(location.search);
const EIN = { g: P.get('g') || 'nacht', stand: P.get('stand') || 'bsp5', ruhe: P.get('ruhe') === '1', lage: P.get('lage') || 'normal' };
document.body.dataset.g = EIN.g === 'hell' ? 'hell' : 'nacht';
if (EIN.ruhe || matchMedia('(prefers-reduced-motion: reduce)').matches) document.body.dataset.ruhe = '1';
if (P.get('bild') === '1') document.body.classList.add('bild');
const RUHE = () => document.body.dataset.ruhe === '1';
const STAND = () => (EIN.lage === 'ohnestand' ? {} : (STAENDE[EIN.stand] || STAENDE.aus).z);
const zustand = (nr) => STAND()[nr] || null;
const mond = (nr) => { const z = zustand(nr); return z ? `<span class="mond ${ZUSTAND_KLASSE[z]}" aria-hidden="true"></span><span class="nur-vorleser">${ZUSTAND_TEXT[z]}: </span>` : ''; };
const planetVon = (nr) => PLANETEN.find((p) => p.regeln.includes(nr));
const h = (html) => { const t = document.createElement('template'); t.innerHTML = html.trim(); return t.content.firstElementChild; };
const SYM = {
  zurueck: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>',
  zu: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
  haken: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
  hinweis: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7.5v5.5M12 16.5v.2"/></svg>',
};

// ---------- Blätter ----------
const schleier = h('<div class="schleier"></div>'); const blatt = h('<section class="blatt" role="dialog" aria-modal="true" tabindex="-1"></section>');
document.body.append(schleier, blatt);
let stapel = []; let vorher = null; let beimSchliessen = null;
function zeigeBlatt() {
  const oben = stapel[stapel.length - 1]; if (!oben) return schliesseBlatt();
  blatt.classList.toggle('voll', !!oben.voll); blatt.innerHTML = ''; oben.fuelle(blatt);
  blatt.setAttribute('aria-label', oben.name || 'Blatt');
  requestAnimationFrame(() => { if (!stapel.length) return; blatt.classList.add('offen'); schleier.classList.add('offen'); blatt.querySelector('.blatt-inhalt')?.scrollTo(0, 0); blatt.focus({ preventScroll: true }); });
}
function oeffneBlatt(eintrag, neu = false) { if (!stapel.length) vorher = document.activeElement; if (neu) stapel = []; stapel.push(eintrag); zeigeBlatt(); }
function zurueckBlatt() { stapel.pop(); zeigeBlatt(); }
function schliesseBlatt() { stapel = []; blatt.classList.remove('offen'); schleier.classList.remove('offen'); vorher?.focus?.({ preventScroll: true }); const f = beimSchliessen; beimSchliessen = null; f?.(); }
schleier.addEventListener('click', schliesseBlatt);
document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && stapel.length) schliesseBlatt(); });
const blattKopf = (ueber, titel) => `<header class="blatt-kopf">${stapel.length > 1 ? `<button class="zu" data-zurueck aria-label="Zurück">${SYM.zurueck}</button>` : ''}<div style="flex:1;min-width:0"><p class="ueber">${ueber}</p><h2>${titel}</h2></div><button class="zu" data-zu aria-label="Schließen">${SYM.zu}</button></header>`;
function verdrahte(b) { b.querySelector('[data-zu]')?.addEventListener('click', schliesseBlatt); b.querySelector('[data-zurueck]')?.addEventListener('click', zurueckBlatt); }
const legende = () => (Object.keys(STAND()).length ? `<p class="legende"><span><span class="mond sitzt"></span>sitzt</span><span><span class="mond arbeit"></span>in Arbeit</span><span><span class="mond spaeter"></span>kommt später</span></p>` : '');
const regelZeile = (nr, mitNr = false) => `<button class="zeile" data-regel="${nr}">${mitNr ? `<span class="nr">${nr}</span>` : ''}${mond(nr)}<span class="txt"><b>${REGELN[nr].name}</b><span class="satz">${REGELN[nr].satz}</span></span><span class="pfeil" aria-hidden="true">›</span></button>`;
function verdrahteRegeln(b) { b.querySelectorAll('[data-regel]').forEach((k) => k.addEventListener('click', () => oeffneRegel(+k.dataset.regel))); }

function oeffnePlanet(id) {
  const p = PLANETEN.find((x) => x.id === id); if (!p || p.erde) return;
  oeffneBlatt({ name: 'Planet ' + p.name, fuelle(b) {
    b.innerHTML = blattKopf(`Planet · ${p.regeln.length} Regeln`, p.name) + `<div class="blatt-inhalt"><p class="hinweis" style="margin-top:0;color:var(--text)">${p.kurz}</p>${p.regeln.map((n) => regelZeile(n)).join('')}${legende()}</div>`;
    verdrahte(b); verdrahteRegeln(b);
  } }, true);
}
function oeffneSonne() {
  oeffneBlatt({ name: 'Alle 15 Regeln', fuelle(b) {
    b.innerHTML = blattKopf('Sonne', '15 Regeln. Mehr sind es nicht.') + `<div class="blatt-inhalt"><p class="hinweis" style="margin-top:0;color:var(--text)">Sie kommen in jedem Thema wieder, nur in neuem Gewand: erst mit Zahlen, später mit x.</p>
      ${PLANETEN.filter((p) => !p.erde).map((p) => `<p class="ueber" style="margin:18px 2px 0">${p.name}</p>${p.regeln.map((n) => regelZeile(n, true)).join('')}`).join('')}${legende()}</div>
      <footer class="blatt-fuss"><button class="haupt" data-fuenf>Gemischte Fünf <span aria-hidden="true">›</span></button><p class="rk-fuss-klein">Fünf Aufgaben quer durch deine Regeln. Welche Regel dran ist, steht nicht dabei. (Vorschlag, noch nicht entschieden)</p></footer>`;
    verdrahte(b); verdrahteRegeln(b); b.querySelector('[data-fuenf]').addEventListener('click', () => melde('Hier starten fünf gemischte Aufgaben.'));
  } }, true);
}
function oeffneGuertel() {
  oeffneBlatt({ name: 'Werkzeug-Gürtel', fuelle(b) {
    b.innerHTML = blattKopf('Gürtel · 5 Arbeitsweisen', 'Werkzeug-Gürtel') + `<div class="blatt-inhalt"><p class="hinweis" style="margin-top:0;color:var(--text)">Keine Regeln, sondern Arbeitsweisen. Hier gibt es kein Richtig oder Falsch – sie helfen dir bei jeder Aufgabe.</p>
      ${WERKZEUGE.map((w) => `<div class="zeile" style="cursor:default"><span class="txt"><b>${w.name}</b><span class="satz">${w.satz}</span></span></div>`).join('')}</div>`;
    verdrahte(b);
  } }, true);
}

// ---------- Bilder der Regel-Karte ----------
function bildRechteck(g) {
  const x0 = 62, x1 = 302, y0 = 34, y1 = 124, xt = g.minus ? 238 : 222;
  const strich = 'stroke="var(--text)" stroke-width="2"';
  return `<svg viewBox="0 0 320 150" role="img" aria-label="Rechteck mit der Höhe ${g.f}, geteilt in zwei Breiten ${g.a} und ${g.b}">
    <defs><pattern id="schraffur" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" stroke="var(--leise)" stroke-width="2"/></pattern></defs>
    <rect x="${x0}" y="${y0}" width="${xt - x0}" height="${y1 - y0}" fill="var(--flaeche)" ${strich}/>
    <rect x="${xt}" y="${y0}" width="${x1 - xt}" height="${y1 - y0}" fill="${g.minus ? 'url(#schraffur)' : 'var(--flaeche)'}" ${strich} ${g.minus ? 'stroke-dasharray="6 5"' : ''}/>
    <rect x="12" y="${(y0 + y1) / 2 - 17}" width="36" height="34" rx="8" fill="var(--marke)"/>
    <text x="30" y="${(y0 + y1) / 2 + 6}" text-anchor="middle" font-family="var(--mono)" font-size="18" font-weight="700" fill="var(--marke-text)">${g.f}</text>
    <path d="M52 ${y0 + 4}V${y1 - 4}" stroke="var(--leise)" stroke-width="1.5"/>
    ${g.minus
    ? `<path d="M${x0} 18H${x1}M${x0} 13v10M${x1} 13v10" stroke="var(--leise)" stroke-width="1.5" fill="none"/><rect x="${(x0 + x1) / 2 - 16}" y="8" width="32" height="20" fill="var(--flaeche2)"/><text x="${(x0 + x1) / 2}" y="24" text-anchor="middle" font-family="var(--mono)" font-size="16" font-weight="700" fill="var(--text)">${g.a}</text>
       <text x="${(xt + x1) / 2}" y="142" text-anchor="middle" font-family="var(--mono)" font-size="15" font-weight="700" fill="var(--text)">${g.b} weg</text><text x="${(x0 + xt) / 2}" y="142" text-anchor="middle" font-family="var(--mono)" font-size="15" font-weight="700" fill="var(--text)">${g.rest}</text>
       <text x="${(x0 + xt) / 2}" y="${(y0 + y1) / 2 + 6}" text-anchor="middle" font-family="var(--mono)" font-size="17" font-weight="700" fill="var(--text)">${g.f} · ${g.rest}</text>
       <rect x="${(xt + x1) / 2 - 27}" y="${(y0 + y1) / 2 - 13}" width="54" height="26" rx="6" fill="var(--flaeche2)"/><text x="${(xt + x1) / 2}" y="${(y0 + y1) / 2 + 5}" text-anchor="middle" font-family="var(--mono)" font-size="14" font-weight="700" fill="var(--text)">${g.fb}</text>`
    : `<text x="${(x0 + xt) / 2}" y="24" text-anchor="middle" font-family="var(--mono)" font-size="16" font-weight="700" fill="var(--text)">${g.a}</text><text x="${(xt + x1) / 2}" y="24" text-anchor="middle" font-family="var(--mono)" font-size="16" font-weight="700" fill="var(--text)">${g.b}</text>
       <text x="${(x0 + xt) / 2}" y="${(y0 + y1) / 2 + 6}" text-anchor="middle" font-family="var(--mono)" font-size="17" font-weight="700" fill="var(--text)">${g.fa}</text><text x="${(xt + x1) / 2}" y="${(y0 + y1) / 2 + 6}" text-anchor="middle" font-family="var(--mono)" font-size="16" font-weight="700" fill="var(--text)">${g.fb}</text>
       <text x="${xt}" y="142" text-anchor="middle" font-family="var(--mono)" font-size="14" fill="var(--leise)">zusammen: ${g.fa} + ${g.fb}</text>`}
  </svg>`;
}
function bildStrahl() {
  const X = (v) => 30 + (v - 8) * 20, y = 96; let ticks = '';
  for (let v = 9; v <= 21; v++) ticks += `<path d="M${X(v)} ${y - (v % 5 === 0 || v === 12 ? 7 : 4)}V${y + (v % 5 === 0 || v === 12 ? 7 : 4)}" stroke="var(--leise)" stroke-width="1.5"/>`;
  const zahl = (v) => `<text x="${X(v)}" y="${y + 24}" text-anchor="middle" font-family="var(--mono)" font-size="15" font-weight="700" fill="var(--text)">${v}</text>`;
  const pfeil = (a, b, yy, farbe, text, unten) => { const d = b < a ? -1 : 1; return `<path d="M${X(a)} ${yy}H${X(b) - d * 3}" stroke="${farbe}" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M${X(b)} ${yy}l${-d * 9} -6v12z" fill="${farbe}"/><text x="${(X(a) + X(b)) / 2}" y="${unten ? yy + 18 : yy - 8}" text-anchor="middle" font-family="var(--mono)" font-size="15" font-weight="700" fill="var(--text)">${text}</text>`; };
  return `<svg viewBox="0 0 320 168" role="img" aria-label="Zahlenstrahl: von 20 erst 8 zurück auf 12, dann 3 vor auf 15. Der direkte Weg 20 minus 5 landet auch auf 15.">
    <path d="M20 ${y}H304" stroke="var(--text)" stroke-width="2"/>${ticks}${zahl(12)}${zahl(15)}${zahl(20)}
    <circle cx="${X(15)}" cy="${y}" r="9" fill="var(--marke)" stroke="var(--text)" stroke-width="2"/>
    ${pfeil(20, 12, 34, 'var(--kurs)', '− 8')}${pfeil(12, 15, 66, 'var(--gut)', '+ 3')}
    ${pfeil(20, 15, 136, 'var(--leise)', '− (8 − 3)', true)}
  </svg>`;
}

// ---------- Regel-Karte ----------
function oeffneRegel(nr, kontext = 'frei', neu = false) {
  const r = REGELN[nr], p = planetVon(nr), k = KARTEN[nr], z = zustand(nr);
  oeffneBlatt({ voll: true, name: 'Regel ' + r.name, fuelle(b) {
    let gew = 0, px = 3;
    const ruf = kontext === 'fehler' ? `<p class="rk-ruf">${SYM.hinweis}<span>${GEKLEMMT[nr]}</span></p>`
      : kontext === 'einstieg' ? `<p class="rk-ruf">${SYM.hinweis}<span>Das kennst du schon. Hier kommt die Regel in neuem Gewand.</span></p>` : '';
    const fuss = kontext === 'fehler' ? `<button class="haupt" data-haupt>Zurück zur Aufgabe</button>`
      : kontext === 'einstieg' ? `<button class="haupt" data-haupt>Weiter zur Erklärung <span aria-hidden="true">›</span></button>`
        : z === 'k' ? `<p class="rk-fuss-klein" style="margin:4px 0">Diese Regel kommt später auf deiner Reise.</p>`
          : `<button class="haupt" data-haupt>Drei Aufgaben zu dieser Regel <span aria-hidden="true">›</span></button><p class="rk-fuss-klein">Etwa 3 Minuten.</p>`;
    const male = () => {
      const g = k?.gewand[gew];
      b.innerHTML = blattKopf(`${p.name} · Regel ${nr} von 15`, r.name) + `<div class="blatt-inhalt">${ruf}
        ${z ? `<p class="legende" style="margin:0 0 6px"><span><span class="mond ${ZUSTAND_KLASSE[z]}"></span>${ZUSTAND_TEXT[z]}</span></p>` : ''}
        <p class="rk-satz">${r.satz}</p>${r.satz2 ? `<p class="rk-satz2">${r.satz2}</p>` : ''}
        ${k ? `
        <div class="rk-teil"><figure class="rk-bild" style="margin:0">${k.bild === 'rechteck' ? bildRechteck(g.bild) : bildStrahl()}<figcaption>${k.bild === 'rechteck' && g.bild.minus ? 'Das ganze Rechteck ist 6 · 20. Der Streifen 6 · 2 kommt weg, übrig bleibt 6 · 18.' : k.bildtext}</figcaption></figure></div>
        <div class="rk-teil"><p class="ueber">Dieselbe Regel, drei Gewänder</p><div class="gewand">${k.gewand.map((w, i) => (w.bild
    ? `<button aria-pressed="${i === gew}" data-gewand="${i}"><span class="ueber"><span>${w.art}</span><span class="zeigt leise">${i === gew ? 'im Bild' : 'im Bild zeigen'}</span></span><span class="rechnung">${w.html}</span></button>`
    : `<button aria-pressed="false" style="cursor:default" tabindex="-1"><span class="ueber"><span>${w.art}</span></span><span class="rechnung">${w.html}</span></button>`)).join('')}</div>
          ${k.bild === 'strahl' ? '<p class="hinweis">Das Bild zeigt es mit Zahlen. Mit x und mit Brüchen läuft es genauso.</p>' : ''}</div>
        <div class="rk-teil"><div class="grenze"><p class="ueber">Die Grenze</p><p><b>${k.grenze.satz}</b> ${k.grenze.text}</p><span class="rechnung">${k.grenze.rechnung}</span></div></div>
        <div class="rk-teil"><p class="ueber">Die Probe</p><div class="probe"><p>${k.probe.text}</p>
          <div class="probe-wahl"><span>x =</span>${[2, 3, 4].map((x) => `<button aria-pressed="${x === px}" data-px="${x}">${x}</button>`).join('')}</div>
          <div class="probe-seiten"><div><small>${k.probe.name[0]}</small><span class="rechnung">${k.probe.links(px)[0]}</span><strong>= ${k.probe.links(px)[1]}</strong></div><div><small>${k.probe.name[1]}</small><span class="rechnung">${k.probe.rechts(px)[0]}</span><strong>= ${k.probe.rechts(px)[1]}</strong></div></div>
          <p class="probe-gleich">${SYM.haken}<span>Beide Seiten geben ${k.probe.links(px)[1]}.</span></p></div></div>
        <div class="rk-teil"><p class="ueber">Diese Regel brauchst du in …</p><ul class="orte">${k.orte.map((o) => `<li><span class="ort">${o[0]}</span><span>${o[1]}</span><span class="kl">${o[2]}</span></li>`).join('')}</ul><p class="hinweis" style="font-size:14px">Orte im Entwurf erfunden.</p></div>`
    : `${r.grenze ? `<div class="rk-teil"><div class="grenze"><p class="ueber">Die Grenze</p><p><b>${r.grenze}</b></p></div></div>` : ''}<p class="hinweis" style="margin-top:20px">Der Entwurf zeigt nur „Verteilen“ und „Minusklammer“ ganz. Jede Karte bekommt denselben Aufbau.</p>`}
      </div><footer class="blatt-fuss">${fuss}</footer>`;
      verdrahte(b);
      b.querySelectorAll('[data-gewand]').forEach((e) => e.addEventListener('click', () => { const s = b.querySelector('.blatt-inhalt').scrollTop; gew = +e.dataset.gewand; male(); b.querySelector('.blatt-inhalt').scrollTop = s; }));
      b.querySelectorAll('[data-px]').forEach((e) => e.addEventListener('click', () => { const s = b.querySelector('.blatt-inhalt').scrollTop; px = +e.dataset.px; male(); b.querySelector('.blatt-inhalt').scrollTop = s; b.querySelector(`[data-px="${px}"]`).focus({ preventScroll: true }); }));
      b.querySelector('[data-haupt]')?.addEventListener('click', () => { if (kontext === 'frei') melde('Hier starten drei Aufgaben zu „' + r.name + '“.'); else schliesseBlatt(); });
    };
    male();
  } }, neu);
}

// ---------- Meldung (nur im Entwurf) ----------
function melde(text) { document.querySelector('.meldung')?.remove(); const m = h(`<div class="meldung" role="status" style="position:fixed;left:50%;bottom:76px;transform:translateX(-50%);z-index:60;background:#1f2937;color:#fff;font:14px system-ui;padding:10px 14px;border-radius:12px;max-width:86vw;box-shadow:0 8px 24px #0006">Entwurf: ${text}</div>`); document.body.append(m); setTimeout(() => m.remove(), 2600); }

// ---------- Entwurfs-Schalter ----------
function entwurfsSchalter(seiten) {
  const wahl = (name, werte) => `<label>${name}<select data-p="${name}">${werte.map(([w, t]) => `<option value="${w}">${t}</option>`).join('')}</select></label>`;
  const e = h(`<div class="entwurf"><button aria-expanded="false">Entwurf ⚙</button><div class="entwurf-feld"><p><b>Entwurf, nicht die App.</b> Alle Zustände sind erfunden.</p>
    ${wahl('g', [['nacht', 'Abflug dunkel'], ['hell', 'Abflug hell']])}${wahl('stand', [['bsp5', 'Beispiel A'], ['bsp8', 'Beispiel B'], ['aus', 'ohne Stand']])}${wahl('ruhe', [['0', 'Bewegung an'], ['1', 'weniger Bewegung']])}${wahl('lage', [['normal', 'geladen'], ['laden', 'lädt'], ['fehler', 'Fehler'], ['ohnestand', 'Stand fehlt']])}
    <p style="margin-top:10px">${seiten.map(([d, t]) => `<a href="${d}">${t}</a>`).join(' · ')}</p></div></div>`);
  e.querySelector('button').addEventListener('click', () => e.classList.toggle('offen'));
  const namen = { g: 'Gestaltung', stand: 'Stand', ruhe: 'Bewegung', lage: 'Zustand' };
  e.querySelectorAll('select').forEach((s) => { const k = s.dataset.p; s.previousSibling.textContent = namen[k]; s.value = k === 'ruhe' ? (EIN.ruhe ? '1' : '0') : EIN[k]; s.addEventListener('change', () => { P.set(k, s.value); location.search = P.toString(); }); });
  document.body.append(e);
}
const SEITEN = [['uebersicht-a.html', 'Übersicht A'], ['uebersicht-b.html', 'Übersicht B'], ['regel-karte.html', 'Regel-Karte'], ['wege.html', 'Drei Wege']];
