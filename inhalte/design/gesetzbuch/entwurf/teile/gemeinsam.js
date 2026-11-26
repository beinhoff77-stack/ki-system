// Gesetzbuch – gemeinsame Teile: Daten, Kopf mit Suche, „ein Gesetz aufgeschlagen“, „Idee und ihre Gesetze“, Suche.
const P = new URLSearchParams(location.search);
document.body.dataset.g = P.get('g') === 'hell' ? 'hell' : 'nacht';
if (P.get('bild') === '1') document.body.classList.add('bild');
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const REGEL = Object.fromEntries(INHALT.regeln.map((r) => [r.id, r]));
const GESETZ = Object.fromEntries(INHALT.gesetze.map((g) => [g.id, g]));
const ETAGE = Object.fromEntries(INHALT.etagen.map((e) => [e.nr, e.name]));
const PLANETEN = INHALT.planeten.filter((p) => PLANET_BILD[p.name]);
const IDEE = {}; for (const p of PLANETEN) p.ideen.forEach((i) => { i.id = `I-${KUERZEL[p.name]}-${i.nr}`; i.planet = p.name; i.von = p.ideen.length; IDEE[i.id] = i; });
const ideeVon = (gid) => Object.values(IDEE).find((i) => i.gesetze.includes(gid));
const spanne = (zahlen) => { const a = Math.min(...zahlen), b = Math.max(...zahlen); return a === b ? 'Klasse ' + a : `Klasse ${a}–${b}`; };
const regelSpanne = (r) => spanne(r.klassen.map((k) => k.klasse));
const gymZahlen = (g) => (g.gym.match(/\d+/g) || []).map(Number);
const planetSpanne = (name) => { const z = INHALT.gesetze.filter((g) => g.planet === name).flatMap(gymZahlen); return z.length ? spanne(z) : ''; };
const klasseVon = (g) => (g.gym && g.gym !== '–' ? 'Klasse ' + g.gym : 'Realschule oder IB');
const thema = (k) => (INHALT.themen[k] ? `${INHALT.themen[k].ort} · ${INHALT.themen[k].titel}` : '');
const planetScheibe = (name, gr = 44) => `<svg class="scheibe" width="${gr}" height="${gr}" viewBox="-22 -22 44 44" aria-hidden="true"><circle r="21" fill="${PLANET_BILD[name].farbe}"/>${PLANET_BILD[name].zeichen}</svg>`;
const LUPE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.500 15.500L21 21"/></svg>';
const seite = document.getElementById('seite');
// Zwei Zeilen je Satz (Auftrag 12 an den Mathe-Profi): Merksatz groß, „Genau gesagt“ klein darunter. Solange „genau“ fehlt, steht nur der Satz.
const genau = (x) => (x.genau ? `<span class="genau"><i>Genau gesagt:</i> ${x.genau}</span>` : '');
const markiert = (id, text) => WIRKSTELLE[id]?.bsp[text] || esc(text);

// ---------- Kopf ----------
document.getElementById('kopf').innerHTML = `<div class="breite"><a class="kopf-marke" href="#/"><i></i><span class="lang">Gesetzbuch der Mathematik</span><span class="kurz">Gesetzbuch</span></a>
  <form class="suche" role="search"><label><span style="position:absolute;left:-9999px">Im Gesetzbuch suchen</span>${LUPE}<input type="search" name="q" placeholder="Suchen, z. B. Kegelmantel" autocomplete="off" enterkeyhint="search"></label></form></div>`;
const suchfeld = document.querySelector('.suche input');
document.querySelector('.suche').addEventListener('submit', (e) => { e.preventDefault(); if (suchfeld.value.trim()) location.hash = '#/suche/' + encodeURIComponent(suchfeld.value.trim()); });
suchfeld.addEventListener('input', () => { if (suchfeld.value.trim().length >= 3) history.replaceState(null, '', '#/suche/' + encodeURIComponent(suchfeld.value.trim())), zeige(); });

// ---------- Suche: Name, Satz, Beispiele – und die Stichwörter des Mathe-Profis (z. B. „Kegelmantel“ steht bei F17) ----------
const wort = (s) => s.toLowerCase().replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss').replace(/<[^>]+>/g, ' ');
const woerter = (s, ab) => wort(s).split(/[^a-z0-9]+/).filter((w) => w.length > ab);
const STICH = {}; INHALT.stichwoerter.forEach((s) => { (STICH[s.ziel] ||= []).push(s.wort); });
const SUCHBAR = [
  ...INHALT.regeln.map((r) => ({ id: r.id, art: 'Rechenregel ' + r.nr, name: r.name, satz: r.satz, mehr: r.klassen.map((k) => k.text).join(' ') + ' ' + r.fehler, ort: ['Sonne', ETAGE[r.etage]], kl: regelSpanne(r), ziel: '#/regel/' + r.id })),
  ...INHALT.gesetze.map((g) => { const i = ideeVon(g.id); return { id: g.id, art: 'Gesetz ' + g.id, name: g.name, satz: g.satz, mehr: (g.klassen || []).map((k) => k.text).join(' ') + ' ' + (g.fehler || '') + ' ' + (g.warum || ''), ort: [g.planet, i ? i.kurz : ''], kl: klasseVon(g), ziel: '#/gesetz/' + g.id }; }),
  ...Object.values(IDEE).map((i) => ({ id: i.id, art: 'Tragende Idee', name: i.kurz, satz: i.satz, mehr: '', ort: [i.planet], kl: `${i.gesetze.length} Gesetze`, ziel: '#/idee/' + i.id })),
  ...INHALT.arbeitsweisen.map((a) => ({ id: a.name, art: 'Arbeitsweise', name: a.name, satz: a.satz, mehr: '', ort: ['Arbeitsweisen'], kl: 'jede Klasse', ziel: '#/' })),
].map((e) => ({ ...e, stich: STICH[e.id] || [], wn: woerter(e.name, 2), wk: (STICH[e.id] || []).map((s) => woerter(s, 2)), ws: woerter(e.satz, 3), wm: woerter(e.mehr, 3) }));
function suche(q) {
  const teile = woerter(q, 1); if (!teile.length) return [];
  const trifft = (liste, t) => liste.some((w) => w === t || (t.length >= 4 && w.includes(t)) || (w.length >= 5 && t.includes(w)));
  return SUCHBAR.map((e) => { let p = 0, ueber = null; for (const t of teile) { const k = e.wk.findIndex((l) => trifft(l, t)); if (k >= 0) { p += e.wk[k].includes(t) ? 9 : 5; ueber = e.stich[k]; }
    p += (trifft(e.wn, t) ? 6 : 0) + (trifft(e.ws, t) ? 3 : 0) + (trifft(e.wm, t) ? 1 : 0); } return { ...e, p, ueber }; })
    .filter((x) => x.p > 0).sort((a, b) => b.p - a.p).slice(0, 12);
}
function sichtSuche(q) {
  const tr = suche(q); if (suchfeld.value !== q && document.activeElement !== suchfeld) suchfeld.value = q;
  return `<div class="breite schmal"><nav class="pfad"><a href="#/">Übersicht</a><span class="t">›</span><span>Suche</span></nav>
    <h1 class="s-titel">${tr.length ? `${tr.length} Treffer für „${esc(q)}“` : `Nichts gefunden für „${esc(q)}“`}</h1>
    ${tr.length ? '' : '<p class="leise" style="margin-top:8px">Versuch ein einzelnes Wort, zum Beispiel „Kegel“, „Prozent“ oder „Klammer“.</p>'}
    <ol class="treffer">${tr.map((e) => `<li><a class="karte" href="${e.ziel}"><span class="t-ort">${e.ort.filter(Boolean).map(esc).join(' › ')}</span><span class="t-name"><span class="nr">${e.art}</span> ${esc(e.name)}</span>${e.ueber ? `<span class="t-stich">Stichwort „${esc(e.ueber)}“ steht hier</span>` : ''}<span class="t-satz">${e.satz}</span><span class="kl">${e.kl}</span></a></li>`).join('')}</ol></div>`;
}

// ---------- Ein Gesetz aufgeschlagen ----------
function verweise(text) { // „F15 Prisma und Zylinder · Rechenregel 12 Gegenrechnung“ oder der bloße Name einer Rechenregel -> Verweise
  return (text || '').split(' · ').map((t) => { const f = t.match(/^([A-Z]+\d+) /), r = t.match(/^Rechenregel (\d+)/), n = INHALT.regeln.find((x) => t.startsWith(x.name));
    const id = f ? f[1] : r ? 'R' + r[1] : n ? n.id : null; return id && (GESETZ[id] || REGEL[id]) ? { id, name: (GESETZ[id] || REGEL[id]).name } : null; }).filter(Boolean);
}
const verweisKnopf = (v) => `<a class="verweis" href="#/${v.id[0] === 'R' && REGEL[v.id] ? 'regel' : 'gesetz'}/${v.id}"><span class="nr">${REGEL[v.id] ? 'Regel ' + v.id.slice(1) : v.id}</span>${esc(v.name)}</a>`;
const vorgabe = (z, titel) => `<div class="z-folgt"><p class="ueber">${titel}</p>${z ? `<p><b>Zu sehen sein wird:</b> ${esc(z['Zu sehen'])}</p><p class="klein leise" style="margin-top:6px">Vorgabe des Mathe-Profis. Gezeichnet wird, sobald der Zeichenstil freigegeben ist.</p>` : '<p>Für diesen Planeten liegt noch keine Zeichen-Vorgabe des Mathe-Profis vor.</p>'}</div>`;
function sichtGesetz(id) {
  const r = REGEL[id], g = r || GESETZ[id]; if (!g) return sichtSuche(id);
  const idee = r ? null : ideeVon(id), ws = WIRKSTELLE[id], weg = verweise(g.weg), klassen = g.klassen || [], stufen = new Set(klassen.map((k) => k.klasse)).size;
  const pfad = r ? `<a href="#/">Übersicht</a><span class="t">›</span><span>Sonne</span><span class="t">›</span><span>Schicht ${r.etage}: ${ETAGE[r.etage]}</span>`
    : `<a href="#/">Übersicht</a><span class="t">›</span><span>${g.planet}</span>${idee ? `<span class="t">›</span><a href="#/idee/${idee.id}">${idee.kurz}</a>` : ''}`;
  const zeich = ZEICHNUNGEN[id] ? zeichnung(id) : idee && ZEICHNUNGEN[idee.id] ? `<p class="klein leise" style="margin-bottom:8px">Zeichnung der tragenden Idee „${idee.kurz}“, aus der dieses Gesetz folgt</p>` + zeichnung(idee.id) : vorgabe(g.zeichen || (idee && idee.zeichen), 'Zeichnung folgt');
  return `<article class="breite gesetz"><nav class="pfad">${pfad}</nav>
    <header class="g-kopf"><p class="ueber">${r ? 'Rechenregel ' + r.nr + ' von 14 · ' + regelSpanne(r) : 'Gesetz ' + id + ' · ' + (g.schulart || klasseVon(g))}</p><h1>${esc(g.name)}</h1><p class="merksatz">${g.satz}${genau(g)}</p></header>
    <div class="g-spalten"><div class="g-links">
      <section><h2 class="ueber">Die Zeichnung</h2>${zeich}</section>
      ${g.warum ? `<section><h2 class="ueber">Warum das gilt</h2><p class="fliess">${g.warum}</p></section>` : ''}
    </div><div class="g-rechts">
      ${klassen.length ? `<section><h2 class="ueber">${r ? `Dieselbe Regel in ${stufen} Klassen` : 'Beispiele'}</h2>${ws ? `<p class="leise klein">${ws.was}</p>` : ''}<ol class="leiter">${klassen.map((k) => `<li><span class="stufe">${k.klasse}</span><div><p class="rechnung">${markiert(id, k.text)}</p><p class="kl">${k.art}${k.thema && thema(k.thema) ? ' · ' + thema(k.thema) : ''}</p></div></li>`).join('')}</ol></section>` : '<section><div class="z-folgt"><p class="ueber">Ausarbeitung folgt</p><p>Für dieses Gesetz liegen bisher Name, Satz und Klasse vor. Ausgearbeitet sind die Sonne und die Planeten „Fläche und Raum“ und „Geometrie“.</p></div></section>'}
      ${g.voraus ? `<section><h2 class="ueber">Voraussetzung: wann es gilt</h2><p class="fliess">${g.voraus}</p></section>` : ''}
      ${g.fehler ? `<section><div class="fehler"><h2 class="ueber">Häufiger Fehler</h2><p>${g.fehler}</p></div></section>` : ''}
      ${g.verwandt ? `<section><h2 class="ueber">Verwandt</h2><p class="fliess">${g.verwandt}</p></section>` : ''}
      ${weg.length ? `<section><h2 class="ueber">Möglicher Erklärweg über</h2><div class="verweise">${weg.map(verweisKnopf).join('')}</div><p class="klein leise" style="margin-top:8px">Zum Erklären hilfreich. Keine Lernvoraussetzung und keine Sperre.</p></section>` : ''}
    </div></div></article>`;
}

// ---------- Eine tragende Idee und die Gesetze dahinter ----------
function sichtIdee(id) {
  const i = IDEE[id]; if (!i) return sichtSuche(id);
  return `<article class="breite gesetz"><nav class="pfad"><a href="#/">Übersicht</a><span class="t">›</span><span>${i.planet}</span></nav>
    <header class="g-kopf"><p class="ueber">${i.planet} · tragende Idee ${i.nr} von ${i.von} · ${esc(i.kurz)}</p><h1 class="merksatz gross">${i.satz}${genau(i)}</h1>${i.warum ? `<p class="fliess" style="max-width:46em">${i.warum}</p>` : ''}</header>
    <section><h2 class="ueber">Die Zeichnung</h2>${ZEICHNUNGEN[id] ? zeichnung(id) : vorgabe(i.zeichen, 'Zeichnung folgt')}</section>
    <section><h2 class="ueber">${i.gesetze.length} Gesetze und Formeln, die daraus folgen</h2><ol class="folge">${i.gesetze.map((gid) => { const g = GESETZ[gid]; return `<li><a class="karte" href="#/gesetz/${gid}"><span class="f-name"><span class="nr">${gid}</span> ${esc(g.name)}</span><span class="f-satz">${g.satz}</span><span class="kl">${klasseVon(g)}</span></a></li>`; }).join('')}</ol></section></article>`;
}

// ---------- Die Zeichnungen und der Stil ----------
function sichtZeichnungen() {
  const blatt = [['R6', 'Rechenregel 6'], ['R13', 'Rechenregel 13'], ['R2', 'Rechenregel 2'], ['I-fur-1', 'Fläche und Raum · Idee 1'], ['I-fur-2', 'Fläche und Raum · Idee 2'], ['I-fur-3', 'Fläche und Raum · Idee 3'], ['I-fur-4', 'Fläche und Raum · Idee 4 (zusätzlich)']];
  return `<div class="breite gesetz"><nav class="pfad"><a href="#/">Übersicht</a><span class="t">›</span><span>Zeichenstil</span></nav>
    <header class="g-kopf"><p class="ueber">Zeichenstil „Heft und Tafel“ · zweite Fassung nach den Zeichen-Vorgaben des Mathe-Profis</p><h1>Sechs Zeichnungen und eine siebte, ein Stil</h1>
      <ul class="stil"><li><i style="background:var(--z-tinte)"></i>Strich in Tinte, Hilfslinien gestrichelt</li><li><i class="rahmen"></i>Gelb mit Rahmen: hier wirkt das Gesetz – in der Zeichnung und in der Rechenzeile</li><li><i style="background:var(--z-blau-fl);border:2px solid var(--z-blau)"></i>Blau: die Fläche oder Größe, um die es geht</li><li><i class="karo"></i>Karos nur, wo gezählt wird – ein Karo ist eine Einheit</li><li><i class="winkel"></i>Höhen immer mit dem Zeichen für den rechten Winkel</li></ul></header>
    ${blatt.map(([k, ueber]) => { const x = REGEL[k] || IDEE[k]; return `<section class="z-blatt"><p class="ueber">${ueber}</p><h2>${esc(x.name || x.kurz)}</h2><p class="merksatz klein-m">${x.satz}</p>${zeichnung(k)}</section>`; }).join('')}</div>`;
}

// ---------- Planeten-Karte (Übersicht A und B) ----------
function planetKarte(p, n) {
  const sp = planetSpanne(p.name), bild = p.ideen.some((i) => ZEICHNUNGEN[i.id]);
  return `<li class="bahn"><div class="breite bahn-innen"><div class="planet-kopf">${planetScheibe(p.name, 52)}<div><h3>${esc(p.name)}</h3><p>${n + 1}. Planet · ${p.ideen.length} tragende Ideen · ${p.zahl} Gesetze${sp ? ' · ' + sp : ''}</p></div></div>
    <ul class="ideen n${p.ideen.length}${bild ? ' mit-bild' : ''}">${p.ideen.map((i) => `<li><a class="idee" href="#/idee/${i.id}">${ZEICHNUNGEN[i.id] ? zeichnungKlein(i.id) : ''}<span class="i-kurz">${esc(i.kurz)}</span><b>${i.satz}</b>${genau(i)}<span class="mehr">${i.gesetze.length} Gesetze dahinter</span></a></li>`).join('')}</ul></div></li>`;
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
e.innerHTML = `<button aria-expanded="false">Entwurf ⚙</button><div class="entwurf-feld"><b>Entwurf, nicht die App.</b><a href="uebersicht-a.html?${P}">Übersicht A „Schnitt“</a><a href="uebersicht-b.html?${P}">Übersicht B „Durch die Klassen“</a><a href="gesetz.html?${P}">Ein Gesetz aufgeschlagen</a><a href="zeichnungen.html?${P}">Zeichnungen</a><button>hell / dunkel</button></div>`;
e.querySelector('button').addEventListener('click', () => e.classList.toggle('offen'));
e.querySelector('.entwurf-feld button').addEventListener('click', () => { P.set('g', document.body.dataset.g === 'hell' ? 'nacht' : 'hell'); location.search = P.toString(); });
document.body.append(e);
