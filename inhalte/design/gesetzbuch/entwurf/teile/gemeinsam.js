// Gesetzbuch – gemeinsame Teile: Daten, Kopf mit Suche, „ein Gesetz aufgeschlagen“, „Idee und ihre Gesetze“, Suche.
const P = new URLSearchParams(location.search);
document.body.dataset.g = P.get('g') === 'hell' ? 'hell' : 'nacht';
if (P.get('bild') === '1') document.body.classList.add('bild');
const bruch = (z, n) => `<span class="br"><i>${z}</i><i>${n}</i></span>`;
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const REGEL = Object.fromEntries(INHALT.regeln.map((r) => [r.id, r]));
const GESETZ = Object.fromEntries(INHALT.gesetze.map((g) => [g.id, g]));
const ETAGE = Object.fromEntries(INHALT.etagen.map((e) => [e.nr, e.name]));
const PLANETEN = INHALT.planeten.filter((p) => PLANET_BILD[p.name]);
const IDEE = {}; for (const [planet, liste] of Object.entries(IDEEN)) liste.forEach((i, n) => { IDEE[i.id] = { ...i, planet, nr: n + 1 }; });
const ideeVon = (gid) => Object.values(IDEE).find((i) => i.gesetze.includes(gid));
const spanne = (zahlen) => { const a = Math.min(...zahlen), b = Math.max(...zahlen); return a === b ? 'Klasse ' + a : `Klasse ${a}–${b}`; };
const regelSpanne = (r) => spanne(r.klassen.map((k) => k.klasse));
const gymZahlen = (g) => (g.gym.match(/\d+/g) || []).map(Number);
const planetSpanne = (name) => { const z = INHALT.gesetze.filter((g) => g.planet === name).flatMap(gymZahlen); return z.length ? spanne(z) : ''; };
const thema = (k) => (INHALT.themen[k] ? `${INHALT.themen[k].ort} · ${INHALT.themen[k].titel}` : '');
const planetScheibe = (name, gr = 44) => `<svg class="scheibe" width="${gr}" height="${gr}" viewBox="-22 -22 44 44" aria-hidden="true"><circle r="21" fill="${PLANET_BILD[name].farbe}"/>${PLANET_BILD[name].zeichen}</svg>`;
const LUPE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.500 15.500L21 21"/></svg>';
const seite = document.getElementById('seite');

// ---------- Kopf ----------
document.getElementById('kopf').innerHTML = `<div class="breite"><a class="kopf-marke" href="#/"><i></i><span class="lang">Gesetzbuch der Mathematik</span><span class="kurz">Gesetzbuch</span></a>
  <form class="suche" role="search"><label><span style="position:absolute;left:-9999px">Im Gesetzbuch suchen</span>${LUPE}<input type="search" name="q" placeholder="Suchen, z. B. Kegelmantel" autocomplete="off" enterkeyhint="search"></label></form></div>`;
const suchfeld = document.querySelector('.suche input');
document.querySelector('.suche').addEventListener('submit', (e) => { e.preventDefault(); if (suchfeld.value.trim()) location.hash = '#/suche/' + encodeURIComponent(suchfeld.value.trim()); });
suchfeld.addEventListener('input', () => { if (suchfeld.value.trim().length >= 3) history.replaceState(null, '', '#/suche/' + encodeURIComponent(suchfeld.value.trim())), zeige(); });

// ---------- Suche ----------
const wort = (s) => s.toLowerCase().replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss').replace(/<[^>]+>/g, ' ');
const SUCHBAR = [
  ...INHALT.regeln.map((r) => ({ id: r.id, art: 'Rechenregel ' + r.nr, name: r.name, satz: r.merksatz, mehr: r.klassen.map((k) => k.text).join(' ') + ' ' + r.nicht, ort: ['Sonne', ETAGE[r.etage]], kl: regelSpanne(r), ziel: '#/regel/' + r.id })),
  ...INHALT.gesetze.map((g) => { const i = ideeVon(g.id); return { id: g.id, art: 'Gesetz ' + g.id, name: g.name, satz: g.merksatz || g.satz, mehr: (g.klassen || []).map((k) => k.text).join(' ') + ' ' + (g.nicht || '') + ' ' + (g.warum || ''), ort: [g.planet, i ? i.satz : g.abschnitt], kl: g.gym && g.gym !== '–' ? 'Klasse ' + g.gym : 'Realschule oder IB', ziel: '#/gesetz/' + g.id }; }),
  ...INHALT.arbeitsweisen.map((a) => ({ id: a.name, art: 'Arbeitsweise', name: a.name, satz: a.satz, mehr: '', ort: ['Arbeitsweisen'], kl: 'jede Klasse', ziel: '#/' })),
].map((e) => ({ ...e, wn: wort(e.name).split(/[^a-z0-9]+/).filter((w) => w.length > 2), ws: wort(e.satz).split(/[^a-z0-9]+/).filter((w) => w.length > 3), wm: wort(e.mehr).split(/[^a-z0-9]+/).filter((w) => w.length > 3) }));
function suche(q) {
  const teile = wort(q).split(/[^a-z0-9]+/).filter((w) => w.length > 1); if (!teile.length) return [];
  const trifft = (liste, t) => liste.some((w) => w === t || (t.length >= 4 && w.includes(t)) || (w.length >= 5 && t.includes(w))); // „kegelmantel“ findet „kegel“ und „mantel“
  return SUCHBAR.map((e) => { let p = 0; for (const t of teile) { const zerlegt = e.wn.filter((w) => w.length >= 5 && t.includes(w) && w !== t).length; p += (trifft(e.wn, t) ? 6 : 0) + zerlegt * 2 + (trifft(e.ws, t) ? 3 : 0) + (trifft(e.wm, t) ? 1 : 0) + (e.wm.filter((w) => w.length >= 5 && t.includes(w)).length ? 1 : 0); } return { e, p }; })
    .filter((x) => x.p > 0).sort((a, b) => b.p - a.p).slice(0, 12).map((x) => x.e);
}
function sichtSuche(q) {
  const tr = suche(q); if (suchfeld.value !== q && document.activeElement !== suchfeld) suchfeld.value = q;
  return `<div class="breite schmal"><nav class="pfad"><a href="#/">Übersicht</a><span class="t">›</span><span>Suche</span></nav>
    <h1 class="s-titel">${tr.length ? `${tr.length} Treffer für „${esc(q)}“` : `Nichts gefunden für „${esc(q)}“`}</h1>
    ${tr.length ? '' : '<p class="leise" style="margin-top:8px">Versuch ein einzelnes Wort, zum Beispiel „Kegel“, „Prozent“ oder „Klammer“.</p>'}
    <ol class="treffer">${tr.map((e) => `<li><a class="karte" href="${e.ziel}"><span class="t-ort">${e.ort.filter(Boolean).map(esc).join(' › ')}</span><span class="t-name"><span class="nr">${e.art}</span> ${esc(e.name)}</span><span class="t-satz">${e.satz}</span><span class="kl">${e.kl}</span></a></li>`).join('')}</ol></div>`;
}

// ---------- Ein Gesetz aufgeschlagen ----------
function verweise(text) { // „F4 Zerlegen und Ergänzen · Rechenregel 8 Potenzen“ -> Liste von Verweisen
  return text.split(' · ').map((t) => { const f = t.match(/^([A-Z]+\d+) /), r = t.match(/^Rechenregel (\d+) /); const id = f ? f[1] : r ? 'R' + r[1] : null; return id && (GESETZ[id] || REGEL[id]) ? { id, name: (GESETZ[id] || REGEL[id]).name } : null; }).filter(Boolean);
}
const verweisKnopf = (v) => `<a class="verweis" href="#/${v.id[0] === 'R' ? 'regel' : 'gesetz'}/${v.id}"><span class="nr">${v.id[0] === 'R' ? 'Regel ' + v.id.slice(1) : v.id}</span>${esc(v.name)}</a>`;
function sichtGesetz(id) {
  const r = REGEL[id], g = r || GESETZ[id]; if (!g) return sichtSuche(id);
  const idee = r ? null : ideeVon(id), ws = WIRKSTELLE[id] || {};
  const voraus = r ? r.braucht.map((b) => ({ id: b, name: REGEL[b].name })) : verweise(g.baut || '');
  const darauf = r ? INHALT.regeln.filter((x) => x.braucht.includes(id)).map((x) => ({ id: x.id, name: x.name })) : INHALT.gesetze.filter((x) => x.baut && verweise(x.baut).some((v) => v.id === id)).map((x) => ({ id: x.id, name: x.name }));
  const pfad = r ? `<a href="#/">Übersicht</a><span class="t">›</span><span>Sonne</span><span class="t">›</span><span>Schicht ${r.etage}: ${ETAGE[r.etage]}</span>`
    : `<a href="#/">Übersicht</a><span class="t">›</span><span>${g.planet}</span>${idee ? `<span class="t">›</span><a href="#/idee/${idee.id}">${idee.satz}</a>` : `<span class="t">›</span><span>${g.abschnitt}</span>`}`;
  const ausIdee = { F1: 'I-fur-1', F2: 'I-fur-1', F5: 'I-fur-2', F6: 'I-fur-2', F7: 'I-fur-2', F12: 'I-fur-3', F15: 'I-fur-3', F17: 'I-fur-3' }[id];
  const zeich = ZEICHNUNGEN[id] ? zeichnung(id) : ausIdee ? `<p class="klein leise" style="margin-bottom:8px">Zeichnung der tragenden Idee „${IDEE[ausIdee].satz}“</p>` + zeichnung(ausIdee) : `<div class="z-folgt"><p class="ueber">Zeichnung folgt</p><p>${g.bild ? esc(g.bild) : 'Der Mathe-Profi legt fest, was zu sehen sein muss.'}</p></div>`;
  const klassen = (g.klassen || []);
  return `<article class="breite gesetz"><nav class="pfad">${pfad}</nav>
    <header class="g-kopf"><p class="ueber">${r ? 'Rechenregel ' + r.nr + ' von 14 · ' + regelSpanne(r) : 'Gesetz ' + id + (g.gym && g.gym !== '–' ? ' · Gymnasium Klasse ' + g.gym : '')}</p><h1>${esc(g.name)}</h1><p class="merksatz">${g.merksatz || g.satz}</p></header>
    <div class="g-spalten"><div class="g-links">
      <section><h2 class="ueber">Die Zeichnung</h2>${zeich}</section>
      ${g.warum ? `<section><h2 class="ueber">Warum das gilt</h2><p class="fliess">${g.warum}</p></section>` : ''}
    </div><div class="g-rechts">
      ${klassen.length ? `<section><h2 class="ueber">${r ? 'Dieselbe Regel' : 'Dasselbe Gesetz'} in jeder Klasse</h2>${ws.was ? `<p class="leise klein">${ws.was}</p>` : ''}<ol class="leiter">${klassen.map((k) => `<li><span class="stufe">${k.klasse}</span><div><p class="rechnung">${ws[k.klasse] && !klassen.some((x) => x !== k && x.klasse === k.klasse) ? ws[k.klasse] : esc(k.text)}</p>${k.thema && thema(k.thema) ? `<p class="kl">${thema(k.thema)}</p>` : ''}</div></li>`).join('')}</ol></section>` : '<section><div class="z-folgt"><p class="ueber">Ausarbeitung folgt</p><p>Für dieses Gesetz liegen bisher Name, Satz und Klasse vor.</p></div></section>'}
      ${g.nicht ? `<section><div class="fehler"><h2 class="ueber">Wo es nicht gilt · häufiger Fehler</h2><p>${g.nicht}</p></div></section>` : ''}
      <section><h2 class="ueber">Voraussetzung</h2>${voraus.length ? `<p class="klein leise">Das musst du vorher können:</p><div class="verweise">${voraus.map(verweisKnopf).join('')}</div>` : '<p class="fliess">Keine. Dieses Gesetz ist ein Anfang.</p>'}
        ${darauf.length ? `<p class="klein leise" style="margin-top:14px">Darauf bauen auf:</p><div class="verweise">${darauf.map(verweisKnopf).join('')}</div>` : ''}</section>
    </div></div></article>`;
}

// ---------- Eine tragende Idee und die Gesetze dahinter ----------
function sichtIdee(id) {
  const i = IDEE[id]; if (!i) return sichtSuche(id);
  return `<article class="breite gesetz"><nav class="pfad"><a href="#/">Übersicht</a><span class="t">›</span><span>${i.planet}</span></nav>
    <header class="g-kopf"><p class="ueber">${i.planet} · tragende Idee ${i.nr} von ${IDEEN[i.planet].length}</p><h1 class="merksatz gross">${i.satz}</h1>${i.dazu ? `<p class="fliess" style="max-width:46em">${i.dazu}</p>` : ''}</header>
    <section><h2 class="ueber">Die Zeichnung</h2>${ZEICHNUNGEN[id] ? zeichnung(id) : `<div class="z-folgt"><p class="ueber">Zeichnung folgt</p><p>${i.bild ? 'Vorschlag des Designers: ' + i.bild : ''}</p></div>`}</section>
    <section><h2 class="ueber">${i.gesetze.length} Gesetze und Formeln, die daraus folgen</h2><ol class="folge">${i.gesetze.map((gid) => { const g = GESETZ[gid]; return `<li><a class="karte" href="#/gesetz/${gid}"><span class="f-name"><span class="nr">${gid}</span> ${esc(g.name)}</span><span class="f-satz">${g.merksatz || g.satz}</span><span class="kl">${g.gym && g.gym !== '–' ? 'Klasse ' + g.gym : 'Realschule oder IB'}</span></a></li>`; }).join('')}</ol></section></article>`;
}

// ---------- Die sechs Zeichnungen und der Stil ----------
function sichtZeichnungen() {
  const blatt = [['R6', 'Rechenregel 6', 'Ausmultiplizieren und Ausklammern', REGEL.R6.merksatz], ['R13', 'Rechenregel 13', 'Gleichung als Waage', REGEL.R13.merksatz], ['R2', 'Rechenregel 2', 'Plus und Minus mit negativen Zahlen', REGEL.R2.merksatz],
    ['I-fur-1', 'Fläche und Raum · Idee 1', IDEE['I-fur-1'].satz, ''], ['I-fur-2', 'Fläche und Raum · Idee 2', IDEE['I-fur-2'].satz, ''], ['I-fur-3', 'Fläche und Raum · Idee 3', IDEE['I-fur-3'].satz, '']];
  return `<div class="breite gesetz"><nav class="pfad"><a href="#/">Übersicht</a><span class="t">›</span><span>Zeichenstil</span></nav>
    <header class="g-kopf"><p class="ueber">Zeichenstil „Heft und Tafel“</p><h1>Sechs Zeichnungen, ein Stil</h1>
      <ul class="stil"><li><i style="background:var(--z-tinte)"></i>Strich in Tinte, Hilfslinien gestrichelt</li><li><i style="background:var(--z-gelb)"></i>Gelb: hier wirkt das Gesetz</li><li><i style="background:var(--z-blau-fl);border:2px solid var(--z-blau)"></i>Blau: die Fläche oder Größe, um die es geht</li><li><i class="karo"></i>Karos nur, wo gezählt wird</li></ul></header>
    ${blatt.map(([k, ueber, name, satz]) => `<section class="z-blatt"><p class="ueber">${ueber}</p><h2>${name}</h2>${satz ? `<p class="merksatz klein-m">${satz}</p>` : ''}${zeichnung(k)}</section>`).join('')}</div>`;
}

// ---------- Planeten-Karte (Übersicht A und B) ----------
function planetKarte(p, n) {
  const ideen = IDEEN[p.name], sp = planetSpanne(p.name);
  return `<li class="bahn"><div class="breite bahn-innen"><div class="planet-kopf">${planetScheibe(p.name, 52)}<div><h3>${esc(p.name)}</h3><p>${n + 1}. Planet · ${p.zahl} Gesetze${sp ? ' · ' + sp : ''}</p></div></div>
    ${ideen ? `<ul class="ideen n${ideen.length}">${ideen.map((i) => `<li><a class="idee" href="#/idee/${i.id}">${ZEICHNUNGEN[i.id] ? zeichnungKlein(i.id, i.id === 'I-fur-1' ? 0 : 1) : '<span class="z-platz">Zeichnung folgt</span>'}<b>${i.satz}</b><span class="mehr">${i.gesetze.length} Gesetze dahinter</span></a></li>`).join('')}</ul>`
    : `<p class="offen"><b>Tragende Ideen folgen.</b> Abschnitte: ${p.abschnitte.map(esc).join(' · ')}.</p>`}</div></li>`;
}

// ---------- Weiche ----------
function zeige() {
  const h = decodeURIComponent(location.hash.replace(/^#\/?/, '')) || START, [art, ...rest] = h.split('/'), wert = rest.join('/');
  seite.innerHTML = art === 'regel' || art === 'gesetz' ? sichtGesetz(wert) : art === 'idee' ? sichtIdee(wert) : art === 'suche' ? sichtSuche(wert) : art === 'zeichnungen' ? sichtZeichnungen() : UEBERSICHT();
  if (art !== 'suche') { suchfeld.value = ''; scrollTo(0, 0); }
  document.title = 'Entwurf: Gesetzbuch der Mathematik';
}
addEventListener('hashchange', zeige);
const e = document.createElement('div'); e.className = 'entwurf';
e.innerHTML = `<button aria-expanded="false">Entwurf ⚙</button><div class="entwurf-feld"><b>Entwurf, nicht die App.</b><a href="uebersicht-a.html?${P}">Übersicht A „Schnitt“</a><a href="uebersicht-b.html?${P}">Übersicht B „Durch die Klassen“</a><a href="gesetz.html?${P}">Ein Gesetz aufgeschlagen</a><a href="zeichnungen.html?${P}">Sechs Zeichnungen</a><button>hell / dunkel</button></div>`;
e.querySelector('button').addEventListener('click', () => e.classList.toggle('offen'));
e.querySelector('.entwurf-feld button').addEventListener('click', () => { P.set('g', document.body.dataset.g === 'hell' ? 'nacht' : 'hell'); location.search = P.toString(); });
document.body.append(e);
