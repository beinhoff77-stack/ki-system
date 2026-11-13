/* W171: Reisen › Highlights › Roadbook – echte Route für einen Roadtrip.
   Pro Nacht ein Schlafbereich (mit Booking-/Airbnb-Suche für genau diese Daten) oder eine eingetragene Unterkunft;
   die Highlights der Suche (highlights.knoten) ordnen sich selbst ein: auf dem Weg · ab Unterkunft · abseits.
   Entfernungen kommen aus einem vereinfachten Straßennetz im Roadtrip (daten.netz), nicht aus einem Routendienst.
   Gespeichert wird der ganze Plan als JSON (api.highlights_roadtrip_speichern); „Raus“ setzt den Highlight-Status wie überall. */
'use strict';

const RB_STATUS_WARN = ['eingeschraenkt', 'unklar', 'grenzwertig', 'falsch', 'unbekannt', 'schlecht'];
const RB_WT = ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa'], RB_MO = ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'];
const rbEsc = (t) => String(t ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const rbAddD = (d, n) => { const x = new Date(d); x.setDate(x.getDate() + n); return x; };
const rbFmt = (d) => d.getDate() + '.' + (d.getMonth() + 1) + '.';
const rbIso = (d) => d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
const rbH = (h) => { const m = Math.round(h * 60 / 5) * 5; return Math.floor(m / 60) + ':' + String(m % 60).padStart(2, '0') + ' h'; };
const rbKomma = (x) => String(Math.round(x * 10) / 10).replace('.', ',');
const rbGm = (o, d, w = []) => 'https://www.google.com/maps/dir/?api=1&travelmode=driving&origin=' + o.join(',') + '&destination=' + d.join(',') + (w.length ? '&waypoints=' + w.slice(0, 9).map(x => x.join(',')).join('%7C') : '');
const rbGs = (q) => 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(q);
const rbBooking = (q, a, b) => `https://www.booking.com/searchresults.html?ss=${encodeURIComponent(q)}&checkin=${rbIso(a)}&checkout=${rbIso(b)}&group_adults=2&group_children=2&no_rooms=1`;
const rbAirbnb = (q, a, b) => `https://www.airbnb.com/s/${encodeURIComponent(q.replace(/, /g, '--').replace(/ /g, '-'))}/homes?checkin=${rbIso(a)}&checkout=${rbIso(b)}&adults=2&children=2`;

// Dauer vor Ort aus dem Steckbrief-Text („3 Std.“, „1–2 h“, „halber Tag“ …)
function rbDauer(t) {
  const s = String(t || '').toLowerCase().replace(/,/g, '.');
  let m = s.match(/(\d+(?:\.\d+)?)\s*[–-]\s*(\d+(?:\.\d+)?)\s*(std|h\b)/); if (m) return (+m[1] + +m[2]) / 2;
  m = s.match(/(\d+(?:\.\d+)?)\s*(std|h\b)/); if (m) return +m[1];
  m = s.match(/(\d+)\s*(?:[–-]\s*(\d+))?\s*min/); if (m) return (m[2] ? (+m[1] + +m[2]) / 2 : +m[1]) / 60;
  if (/halbe/.test(s)) return 4; if (/ganze|tag/.test(s)) return 6; if (/abend/.test(s)) return 1.5;
  return 1.5;
}
// Koordinaten aus Google-Maps-Link oder „lat, lon“
function rbKoord(t) {
  if (!t) return null; t = t.trim();
  const m = t.match(/!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)/) || t.match(/@(-?\d+\.\d+),(-?\d+\.\d+)/) || t.match(/[?&](?:q|query|ll|destination)=(-?\d+\.\d+)(?:,|%2C)(-?\d+\.\d+)/) || t.match(/^(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)$/);
  if (!m) return null; const a = +m[1], b = +m[2]; return Math.abs(a) > 90 || Math.abs(b) > 180 ? null : [a, b];
}

// ---------- Straßennetz ----------
function rbNetz(netz) {
  const N = netz.knoten, ADJ = {}, SP = {};
  Object.keys(N).forEach(k => { ADJ[k] = []; });
  for (const [a, b, km, g] of netz.kanten) { if (!ADJ[a] || !ADJ[b]) continue; const t = km / (g ? 50 : 85); ADJ[a].push([b, km, t, !!g]); ADJ[b].push([a, km, t, !!g]); }
  const npt = k => [N[k][1], N[k][2]];
  const km = (a, b) => hlKm(a[0], a[1], b[0], b[1]);
  function dij(s) {
    if (SP[s]) return SP[s];
    const d = {}, p = {}, t = {}, q = new Set(Object.keys(N)); Object.keys(N).forEach(k => { d[k] = Infinity; }); d[s] = 0; t[s] = 0;
    while (q.size) { let u = null; q.forEach(k => { if (u === null || d[k] < d[u]) u = k; }); q.delete(u); if (d[u] === Infinity) break;
      for (const [v, kmv, tt] of ADJ[u]) if (d[u] + kmv < d[v]) { d[v] = d[u] + kmv; t[v] = t[u] + tt; p[v] = u; } }
    return (SP[s] = { d, p, t });
  }
  const pfad = (a, b) => { const { p } = dij(a); const r = [b]; let c = b; while (c !== a) { c = p[c]; if (!c) return [a, b]; r.unshift(c); } return r; };
  const ort = (c) => { let best = null, bd = 1e9; for (const k of Object.keys(N)) { const d = km(c, npt(k)); if (d < bd) { bd = d; best = k; } } return { c, k: best, zu: bd * 1.3, luft: bd }; };
  const weg = (A, B) => {
    if (A.k === B.k) { const x = km(A.c, B.c) * 1.3; return { km: x, h: x / 55 }; }
    const s = dij(A.k); return { km: A.zu + s.d[B.k] + B.zu, h: A.zu / 55 + s.t[B.k] + B.zu / 55 };
  };
  const knoten = (k) => ({ c: npt(k), k, zu: 0 });
  const piste = (pa) => { let g = 0; for (let i = 0; i < pa.length - 1; i++) { const e = ADJ[pa[i]].find(x => x[0] === pa[i + 1]); if (e && e[3]) g += e[1]; } return g; };
  return { N, npt, ort, weg, pfad, knoten, piste };
}

// ---------- Highlights einordnen ----------
function rbZuordnen(ctx) {
  const { netz, D, his } = ctx; const B = rbBloecke(ctx);
  const start = netz.knoten(D.start || 'adl'), ende = netz.knoten(D.ende || D.start || 'adl');
  const pts = [start, ...B.map(b => rbBlockOrt(ctx, b)), ende];
  const legs = pts.slice(0, -1).map((a, i) => ({ a, b: pts[i + 1], stops: [] }));
  const bases = B.map(() => ({ abst: [] })); const abseits = [];
  for (const h of his) {
    if (h.status === 'weg') continue;
    const P = h.P; const ov = (D.ov || {})[h.id];
    let bi = -1, bd = 1e9; B.forEach((b, i) => { const w = netz.weg(pts[i + 1], P).km; if (w < bd - 1 || (Math.abs(w - bd) <= 1 && bi >= 0 && b.n > B[bi].n)) { bd = w; bi = i; } });
    let li = -1, ld = 1e9; legs.forEach((l, i) => { const det = netz.weg(l.a, P).km + netz.weg(P, l.b).km - netz.weg(l.a, l.b).km; if (det < ld) { ld = det; li = i; } });
    if (ov !== 'basis' && bd > 35 && ld <= 50 && ld <= 2 * bd) legs[li].stops.push({ h, P, von: netz.weg(legs[li].a, P).km });
    else if (bd <= 110) bases[bi].abst.push({ h, P, km: bd, std: netz.weg(pts[bi + 1], P).h });
    else abseits.push({ h, P, km: bd, bi });
  }
  legs.forEach(l => l.stops.sort((x, y) => x.von - y.von));
  return { B, pts, legs, bases, abseits };
}
function rbBloecke(ctx) {
  const D = ctx.D; if (!D.plan) D.plan = {};
  if (!D.aktiv || !D.plan[D.aktiv]) D.aktiv = Object.keys(D.plan)[0] || 'A';
  if (!D.plan[D.aktiv]) D.plan[D.aktiv] = [];
  return D.plan[D.aktiv];
}
const rbBlockOrt = (ctx, b) => (b.own && b.own.lat != null ? ctx.netz.ort([b.own.lat, b.own.lon]) : ctx.netz.knoten(b.z));
const rbName = (ctx, b) => (b.own ? b.own.name : ctx.netz.N[b.z]?.[0] || b.z);

// ---------- Ansicht ----------
async function viewRoadbook(sid, rid) {
  setChrome('Roadbook', { tab: 'highlights', back: true });
  const live = viewGuard();
  loading();
  const r = await hlCall('roadtrip_lesen', { id: rid });
  if (!live()) return;
  const rt = r.roadtrip, D = rt.daten || {};
  const netz = rbNetz(D.netz);
  // Highlights im Gebiet des Netzes; nichts aus Regionen, die ganz raus sind; nichts direkt am Start-/Zielort (Stadt-Highlights)
  const ks = Object.values(D.netz.knoten); const lat = ks.map(k => k[1]), lon = ks.map(k => k[2]);
  const box = [Math.min(...lat) - .3, Math.max(...lat) + .3, Math.min(...lon) - .3, Math.max(...lon) + .3];
  const startK = D.start || 'adl';
  const his = (r.highlights || []).filter(h => h.lat >= box[0] && h.lat <= box[1] && h.lon >= box[2] && h.lon <= box[3] && h.region_status !== 'weg' && h.typ !== 'unterkunft')
    .map(h => ({ ...h, P: netz.ort([Number(h.lat), Number(h.lon)]), dauer: rbDauer(h.zeit), warn: RB_STATUS_WARN.includes(h.saison?.status) ? (h.saison?.text || '') : '' }))
    .filter(h => !(h.P.k === startK && h.P.luft < 40));
  const ctx = { sid, rid, rt, D, netz, his, offen: null, karte: null, timer: null, gespeichert: true };
  const wrap = el('div', { class: 'rb' });
  main.replaceChildren(wrap);
  disposeSuche = () => { clearTimeout(ctx.timer); if (ctx.timer) rbSpeichern(ctx, true); if (ctx.karte) ctx.karte.remove(); };
  wrap.addEventListener('click', e => rbKlick(ctx, e));
  wrap.addEventListener('change', e => { const s = e.target.closest('[data-zone]'); if (!s) return; const b = rbBloecke(ctx)[+s.dataset.zone]; b.z = s.value; b.own = null; b.st = null; rbAenderung(ctx); });
  wrap.addEventListener('submit', e => rbForm(ctx, e));
  ctx.wrap = wrap;
  rbRender(ctx);
}

function rbRender(ctx) {
  const { D, rt, netz } = ctx; const Zu = rbZuordnen(ctx); const B = Zu.B;
  const start = new Date(rt.start_datum + 'T00:00:00');
  const tot = B.reduce((s, b) => s + b.n, 0), ziel = rt.ziel_naechte, end = rbAddD(start, tot);
  const diff = ziel ? ziel - tot : 0, geb = B.filter(b => b.st === 'gebucht').length;
  const chips = `<span class="rb-chip">${rbFmt(start)} → ${rbFmt(end)} ${RB_WT[end.getDay()]}</span>` +
    (ziel ? `<span class="rb-chip ${diff === 0 ? 'ok' : diff > 0 ? 'unter' : 'ueber'}">${diff === 0 ? 'passt: ' + ziel + ' Nächte' : diff > 0 ? diff + ' Nacht' + (diff > 1 ? 'e' : '') + ' frei' : (-diff) + ' Nacht' + (-diff > 1 ? 'e' : '') + ' zu viel'}</span>` : '') +
    `<span class="rb-chip">${B.length} Nachtlager · ${geb} gebucht</span><span class="rb-chip rb-save" id="rb-save">${ctx.gespeichert ? 'gespeichert' : 'speichert …'}</span>`;
  const tabs = Object.entries(D.vorlagen || {}).map(([k, v]) => `<button type="button" class="rb-tab" aria-pressed="${k === D.aktiv}" data-v="${rbEsc(k)}">${rbEsc(v.name)}<small>${rbEsc(v.sub || '')}</small></button>`).join('');
  let tl = '', day = 0;
  B.forEach((b, i) => {
    const d = rbAddD(start, day), e = rbAddD(start, day + b.n);
    tl += rbFahrt(ctx, d, Zu.legs[i], i === 0 ? netz.N[D.start || 'adl'][0] : rbName(ctx, B[i - 1]), rbName(ctx, b));
    tl += rbLager(ctx, b, i, d, e, Zu.bases[i], B.length);
    tl += `<div class="rb-ins"><button type="button" data-ins="${i}">+ Nachtlager danach einfügen</button></div>`;
    day += b.n;
  });
  if (B.length) tl += rbFahrt(ctx, rbAddD(start, day), Zu.legs[B.length], rbName(ctx, B[B.length - 1]), netz.N[D.ende || D.start || 'adl'][0]);
  else tl += `<p class="muted">Noch kein Nachtlager. <button type="button" class="link" data-ins="-1">Erstes Nachtlager anlegen</button></p>`;
  if (Zu.abseits.length) tl += `<section class="rb-off"><h3>Abseits der Route</h3>${Zu.abseits.map(a => { const w = netz.weg(Zu.pts[a.bi + 1], a.P);
    return `<div class="rb-offz"><div>${rbHlName(ctx, a.h)}<small>${Math.round(w.km)} km · ${rbH(w.h)} einfach ab ${rbEsc(rbName(ctx, B[a.bi]))}${a.h.warn ? ' · <span class="rb-w">⚠ ' + rbEsc(a.h.warn) + '</span>' : ''}</small></div><span class="rb-nowrap"><button type="button" class="rb-btn ghost" data-dort="${a.h.id}">Nacht dort einplanen</button><button type="button" class="rb-x" data-raus="${a.h.id}" aria-label="Raus">✕</button></span></div>`; }).join('')}</section>`;
  const raus = ctx.his.filter(h => h.status === 'weg');
  if (raus.length) tl += `<details class="rb-off"><summary>Raus (${raus.length}) – zurückholen</summary><div class="rb-stops">${raus.map(h => `<span class="rb-stop">${rbEsc(h.titel)}<button type="button" data-back="${h.id}" aria-label="zurückholen">↺</button></span>`).join('')}</div></details>`;
  const scroll = window.scrollY;
  ctx.wrap.innerHTML = `
    <header class="rb-kopf"><p class="eyebrow"><a href="${hlHref(ctx.sid)}">Highlights</a> › ROADBOOK</p><h2>${rbEsc(rt.titel)}</h2><div class="rb-chips">${chips}</div></header>
    <details class="rb-how"><summary><b>So geht’s</b></summary><p>Pro Nacht einen <b>Schlafbereich</b> wählen und über Booking/Airbnb suchen. Gefunden? <b>Unterkunft eintragen</b> (mit Google-Maps-Link wird ab genau dort gerechnet). Die Highlights ordnen sich selbst ein: <b>auf dem Weg</b>, <b>ab Unterkunft</b> oder <b>abseits</b>. ⤴ legt einen Stopp auf die Unterkunft, ✕ setzt ein Highlight auf Raus.</p></details>
    ${tabs ? `<div class="rb-tabs" role="group" aria-label="Variante">${tabs}</div>` : ''}
    <div class="rb-grid"><div class="rb-mapbox"><div class="rb-map" id="rb-map" role="region" aria-label="Karte"></div>
      <div class="rb-legende"><span><i class="l-fahrt"></i>Fahrt</span><span><i class="l-lager"></i>Nachtlager</span><span><i class="l-geb"></i>gebucht</span><span><i class="l-weg"></i>auf dem Weg</span><span><i class="l-ab"></i>ab Unterkunft</span><span><i class="l-off"></i>abseits</span><span><i class="l-zone"></i>Schlafbereich</span></div>
      <p class="small muted">Kilometer und Zeiten: Schätzung aus vereinfachtem Straßennetz (Asphalt ~85, Piste ~50 km/h). Genaue Strecke über die Maps-Links.</p></div>
    <div class="rb-tl">${tl}</div></div>`;
  window.scrollTo(0, scroll);
  rbKarte(ctx, Zu);
  if (ctx.offen !== null) { const f = document.getElementById('rb-n-' + ctx.offen); if (f) f.focus({ preventScroll: false }); }
}
const rbHlName = (ctx, h) => `<a href="${hlHref(ctx.sid, h.id)}">${h.status === 'muss' ? '◆ ' : h.status === 'gemerkt' ? '♡ ' : ''}${rbEsc(h.titel)}</a>${h.wow ? ` <span class="rb-wow" aria-label="${rbEsc(h.wow)} von 5">${'★'.repeat(Math.max(0, Math.min(5, +h.wow || 0)))}</span>` : ''}`;

function rbFahrt(ctx, d, l, von, nach) {
  const { netz } = ctx;
  let km = 0, h = 0, prev = l.a, pis = 0;
  for (const s of [...l.stops.map(x => x.P), l.b]) { const w = netz.weg(prev, s); km += w.km; h += w.h; if (prev.k !== s.k) pis += netz.piste(netz.pfad(prev.k, s.k)); prev = s; }
  const vor = l.stops.reduce((s, x) => s + x.h.dauer, 0);
  return `<div class="rb-drive"><div class="rb-date"><b>${d.getDate()}</b><span>${RB_WT[d.getDay()]} ${RB_MO[d.getMonth()]}</span></div>
   <div><div class="rb-sign"><span class="rb-to">${rbEsc(von)} → ${rbEsc(nach)}</span><span class="rb-km">${Math.round(km)} km · ${rbH(h)}</span></div>
   <div class="rb-dbody"><div class="small muted">${pis > 0 ? 'davon ca. ' + Math.round(pis) + ' km Piste' : 'Asphalt'}${vor ? ' · plus ca. ' + rbKomma(vor) + ' h Stopps' : ''}</div>
   ${l.stops.length ? `<div class="rb-stops">${l.stops.map(s => `<span class="rb-stop"><span class="rb-dot"></span>${rbHlName(ctx, s.h)}${s.h.warn ? ` <span class="rb-w" title="${rbEsc(s.h.warn)}">⚠</span>` : ''}<button type="button" data-basis="${s.h.id}" title="lieber ab Unterkunft" aria-label="lieber ab Unterkunft">⤴</button><button type="button" data-raus="${s.h.id}" aria-label="Raus">✕</button></span>`).join('')}</div>` : ''}
   ${h + vor > 9 ? `<div class="rb-w">⚠ Langer Tag: ca. ${Math.round(h + vor)} h mit Stopps – Stopps per ⤴ auf die Unterkunft legen oder ✕.</div>` : ''}
   <div><a class="rb-maps" target="_blank" rel="noopener" href="${rbGm(l.a.c, l.b.c, l.stops.map(s => s.P.c))}">Fahrt in Google Maps</a></div></div></div></div>`;
}

function rbLager(ctx, b, i, d, e, ba, len) {
  const { D, netz } = ctx; const zonen = D.zonen || {}; const z = zonen[b.z] || { q: (netz.N[b.z]?.[0] || '') , bet: '' }; const O = rbBlockOrt(ctx, b);
  const opts = Object.keys(zonen).map(k => ({ k, km: netz.weg(netz.knoten(b.z), netz.knoten(k)).km })).sort((x, y) => x.km - y.km);
  const sumH = ba.abst.reduce((s, a) => s + a.std * 2 + a.h.dauer, 0), tage = b.n - 1 + .5;
  const st = b.own ? `<div class="rb-stay">Unterkunft: <b>${rbEsc(b.own.name)}</b> · ${b.own.lat != null ? '<span class="rb-ok">genaue Lage</span>' : '<span class="rb-w">Lage = ' + rbEsc(netz.N[b.z]?.[0] || '') + '</span>'}
      <span class="rb-pills">${['idee', 'angefragt', 'gebucht'].map(s => `<button type="button" class="rb-pill${b.st === s ? ' an' : ''}" data-st="${i}" data-s="${s}">${s === 'idee' ? 'Idee' : s}</button>`).join('')}</span>
      ${b.own.link ? `<a class="link" target="_blank" rel="noopener" href="${rbEsc(hlSicher(b.own.link) || rbGs(b.own.name))}">Link</a> · ` : ''}<button type="button" class="link" data-edit="${i}">ändern</button> · <button type="button" class="link" data-clear="${i}">entfernen</button></div>`
    : `<div><button type="button" class="rb-btn" data-edit="${i}">Unterkunft eintragen</button></div>`;
  const form = ctx.offen === i ? `<form class="rb-own" data-form="${i}">
      <label for="rb-n-${i}">Name der Unterkunft</label><input id="rb-n-${i}" name="n" value="${rbEsc(b.own?.name || '')}" placeholder="z. B. Prairie Hotel" autocomplete="off">
      <label for="rb-l-${i}">Google-Maps-Link oder Koordinaten (optional)</label><input id="rb-l-${i}" name="l" value="${rbEsc(b.own?.link || '')}" placeholder="lange Google-Maps-Adresse oder -31.13, 138.39" autocomplete="off">
      <small class="muted">Ohne Lage zählt die Mitte des Schlafbereichs. Kurzlinks (maps.app.goo.gl) enthalten keine Koordinaten – im Browser öffnen und die lange Adresse kopieren.</small>
      <div class="rb-row"><button type="submit" class="rb-btn">Übernehmen</button><button type="button" class="link" data-cancel="1">Abbrechen</button></div><div class="err-text small" id="rb-e-${i}"></div></form>` : '';
  return `<section class="rb-base"><div class="rb-bhead"><div><h3>${rbEsc(rbName(ctx, b))}</h3><div class="small muted">${RB_WT[d.getDay()]} ${rbFmt(d)} – ${RB_WT[e.getDay()]} ${rbFmt(e)}</div></div>
     <div class="rb-row"><div class="rb-step"><button type="button" data-i="${i}" data-d="-1" aria-label="Eine Nacht weniger" ${b.n <= 1 ? 'disabled' : ''}>−</button><output>${b.n} ${b.n > 1 ? 'Nächte' : 'Nacht'}</output><button type="button" data-i="${i}" data-d="1" aria-label="Eine Nacht mehr">+</button></div>
     <span class="rb-tools"><button type="button" data-mv="${i}" data-dir="-1" aria-label="nach oben" ${i === 0 ? 'disabled' : ''}>↑</button><button type="button" data-mv="${i}" data-dir="1" aria-label="nach unten" ${i === len - 1 ? 'disabled' : ''}>↓</button><button type="button" data-del="${i}" aria-label="Nachtlager entfernen">✕</button></span></div></div>
   <div><div class="rb-sec">Schlafbereich</div><div class="rb-row"><select data-zone="${i}" aria-label="Schlafbereich">${opts.map(o => `<option value="${rbEsc(o.k)}"${o.k === b.z ? ' selected' : ''}>${rbEsc(netz.N[o.k]?.[0] || o.k)}${o.k === b.z ? '' : ' (' + Math.round(o.km) + ' km)'}</option>`).join('')}</select><span class="small muted">${rbEsc(z.bet || '')}</span></div></div>
   <div class="rb-search"><a class="bk" target="_blank" rel="noopener" href="${rbBooking(z.q, d, e)}">Booking ${rbFmt(d)}–${rbFmt(e)}</a><a target="_blank" rel="noopener" href="${rbAirbnb(z.q, d, e)}">Airbnb</a><a target="_blank" rel="noopener" href="${rbGs('accommodation near ' + z.q)}">Google Maps</a></div>
   ${st}${form}
   <div><div class="rb-sec">Ab Unterkunft</div>${ba.abst.length ? `<div class="rb-spokes">${ba.abst.sort((x, y) => x.km - y.km).map((a, j) => `<div class="rb-spoke"><span class="rb-ico">${j + 1}</span><div>${rbHlName(ctx, a.h)}<small>${Math.round(a.km)} km · ${rbH(a.std)} einfach · ${rbKomma(a.h.dauer)} h vor Ort${a.h.warn ? ' · <span class="rb-w">⚠ ' + rbEsc(a.h.warn) + '</span>' : ''}</small></div><span class="rb-nowrap">${(D.ov || {})[a.h.id] === 'basis' ? `<button type="button" class="rb-x" data-unbasis="${a.h.id}" title="wieder auf dem Weg einplanen" aria-label="wieder auf dem Weg">⤵</button>` : ''}<a class="rb-maps" target="_blank" rel="noopener" href="${rbGm(O.c, O.c, [a.P.c])}">Maps</a><button type="button" class="rb-x" data-raus="${a.h.id}" aria-label="Raus">✕</button></span></div>`).join('')}</div>
     <div class="small ${sumH > tage * 7 ? 'rb-w' : 'muted'}">Abstecher zusammen ca. ${Math.round(sumH)} h · Zeit vor Ort: ${b.n === 1 ? 'Abend + Morgen' : (b.n - 1) + ' volle' + (b.n - 1 > 1 ? ' Tage' : 'r Tag') + ' + Anreisetag'}${sumH > tage * 7 ? ' – mehr als machbar: auswählen oder Nacht dazu' : ''}</div>` : '<div class="small muted">Keine Highlights in Reichweite – reines Nachtlager.</div>'}</div>
  </section>`;
}

function rbKarte(ctx, Zu) {
  const box = document.getElementById('rb-map');
  if (ctx.karte) { ctx.karte.remove(); ctx.karte = null; }
  if (!window.L || !box) { if (box) box.textContent = 'Karte gerade nicht verfügbar.'; return; }
  const { netz, D } = ctx;
  const m = L.map(box, { scrollWheelZoom: false, zoomSnap: 0.5 });
  L.tileLayer('https://tile.openstreetmap.de/{z}/{x}/{y}.png', { minZoom: 4, maxZoom: 16, keepBuffer: 1, attribution: '© <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap-Mitwirkende</a>' }).addTo(m);
  const css = getComputedStyle(document.body); const erde = '#b4472a', grau = '#7d8b8f', gruen = '#1f5f46', ink = css.getPropertyValue('--text').trim() || '#14343b';
  Object.keys(D.zonen || {}).forEach(z => { if (netz.N[z]) L.circle(netz.npt(z), { radius: 15000, color: grau, weight: 1, dashArray: '4 4', fill: false, interactive: false }).addTo(m); });
  const alle = [];
  Zu.legs.forEach(l => { const seq = [l.a, ...l.stops.map(s => s.P), l.b];
    for (let i = 0; i < seq.length - 1; i++) { const a = seq[i], b = seq[i + 1]; const pa = a.k === b.k ? [] : netz.pfad(a.k, b.k); const pts = [a.c, ...pa.map(netz.npt), b.c]; alle.push(...pts);
      L.polyline(pts, { color: erde, weight: 4, opacity: .85 }).addTo(m); } });
  Zu.bases.forEach((ba, i) => { const O = Zu.pts[i + 1]; ba.abst.forEach(a => { L.polyline([O.c, a.P.c], { color: erde, weight: 2, dashArray: '5 6' }).addTo(m);
    L.circleMarker(a.P.c, { radius: 6, color: erde, weight: 2, fillColor: '#fff', fillOpacity: 1 }).bindTooltip(rbEsc(a.h.titel)).addTo(m); alle.push(a.P.c); }); });
  Zu.legs.forEach(l => l.stops.forEach(s => { L.circleMarker(s.P.c, { radius: 6, color: erde, weight: 1, fillColor: erde, fillOpacity: 1 }).bindTooltip(rbEsc(s.h.titel)).addTo(m); }));
  Zu.abseits.forEach(a => { L.circleMarker(a.P.c, { radius: 5, color: grau, weight: 1, fillColor: grau, fillOpacity: .9 }).bindTooltip(rbEsc(a.h.titel) + ' (abseits)').addTo(m); });
  const seen = new Map();
  Zu.B.forEach((b, i) => { const O = Zu.pts[i + 1]; const id = O.c.join(); const v = seen.get(id) || { c: O.c, n: 0, name: rbName(ctx, b), gb: false }; v.n += b.n; if (b.st === 'gebucht') v.gb = true; seen.set(id, v); });
  for (const v of seen.values()) L.marker(v.c, { icon: L.divIcon({ className: 'rb-pin' + (v.gb ? ' geb' : ''), html: `<b>${v.n}</b><span>${rbEsc(v.name)}</span>`, iconSize: null, iconAnchor: [13, 13] }) }).addTo(m);
  const st = netz.npt(D.start || 'adl'); L.marker(st, { icon: L.divIcon({ className: 'rb-pin start', html: `<b>⚑</b><span>${rbEsc(netz.N[D.start || 'adl'][0])}</span>`, iconSize: null, iconAnchor: [13, 13] }) }).addTo(m);
  alle.push(st);
  if (ctx.bounds) m.fitBounds(ctx.bounds, { animate: false }); else if (alle.length) { ctx.bounds = L.latLngBounds(alle).pad(.05); m.fitBounds(ctx.bounds, { animate: false }); }
  m.on('moveend', () => { ctx.bounds = m.getBounds(); });
  ctx.karte = m;
}

// ---------- Bedienung ----------
function rbAenderung(ctx, neuZeichnen = true) {
  ctx.gespeichert = false; if (neuZeichnen) rbRender(ctx);
  clearTimeout(ctx.timer); ctx.timer = setTimeout(() => rbSpeichern(ctx), 900);
}
async function rbSpeichern(ctx, still = false) {
  ctx.timer = null;
  try { await hlCall('roadtrip_speichern', { id: ctx.rid, daten: ctx.D }); ctx.gespeichert = true; const s = document.getElementById('rb-save'); if (s) s.textContent = 'gespeichert'; }
  catch (e) { if (!still) toast('Roadbook nicht gespeichert: ' + (e.message || e), true); }
}
async function rbStatus(ctx, id, status) {
  try { await hlCall('entscheiden', { knoten_id: id, status }); const h = ctx.his.find(x => x.id === id); if (h) h.status = status; HL_CACHE?.clear?.(); rbRender(ctx); }
  catch (e) { toast(e.message || String(e), true); }
}
function rbKlick(ctx, e) {
  const T = s => e.target.closest(s); let t; const D = ctx.D, B = rbBloecke(ctx);
  if ((t = T('[data-v]'))) { D.aktiv = t.dataset.v; ctx.offen = null; return rbAenderung(ctx); }
  if ((t = T('[data-i]'))) { const b = B[+t.dataset.i]; b.n = Math.max(1, b.n + +t.dataset.d); return rbAenderung(ctx); }
  if ((t = T('[data-mv]'))) { const i = +t.dataset.mv, j = i + +t.dataset.dir; if (!B[j]) return; [B[i], B[j]] = [B[j], B[i]]; ctx.offen = null; return rbAenderung(ctx); }
  if ((t = T('[data-del]'))) { const i = +t.dataset.del; if (ctx.loeschen !== i) { ctx.loeschen = i; t.textContent = '?'; t.title = 'Nochmal tippen zum Entfernen'; toast('Nochmal ✕ tippen, um das Nachtlager zu entfernen.'); return; } ctx.loeschen = null; B.splice(i, 1); ctx.offen = null; return rbAenderung(ctx); }
  if ((t = T('[data-ins]'))) { const i = +t.dataset.ins; const z = B[i]?.z || Object.keys(D.zonen || {})[0]; B.splice(i + 1, 0, { z, n: 1, own: null, st: null }); ctx.offen = null; return rbAenderung(ctx); }
  if ((t = T('[data-edit]'))) { ctx.offen = +t.dataset.edit; return rbRender(ctx); }
  if ((t = T('[data-cancel]'))) { ctx.offen = null; return rbRender(ctx); }
  if ((t = T('[data-clear]'))) { const b = B[+t.dataset.clear]; b.own = null; b.st = null; ctx.offen = null; return rbAenderung(ctx); }
  if ((t = T('[data-st]'))) { B[+t.dataset.st].st = t.dataset.s; return rbAenderung(ctx); }
  if ((t = T('[data-basis]'))) { D.ov = D.ov || {}; D.ov[t.dataset.basis] = 'basis'; return rbAenderung(ctx); }
  if ((t = T('[data-unbasis]'))) { if (D.ov) delete D.ov[t.dataset.unbasis]; return rbAenderung(ctx); }
  if ((t = T('[data-raus]'))) return rbStatus(ctx, +t.dataset.raus, 'weg');
  if ((t = T('[data-back]'))) return rbStatus(ctx, +t.dataset.back, 'offen');
  if ((t = T('[data-dort]'))) {
    const h = ctx.his.find(x => x.id === +t.dataset.dort); if (!h) return;
    let zb = null, zd = 1e9; Object.keys(D.zonen || {}).forEach(z => { const w = ctx.netz.weg(ctx.netz.knoten(z), h.P).km; if (w < zd) { zd = w; zb = z; } });
    const Zu = rbZuordnen(ctx); let bi = 0, bd = 1e9; B.forEach((b, i) => { const w = ctx.netz.weg(Zu.pts[i + 1], ctx.netz.knoten(zb)).km; if (w < bd) { bd = w; bi = i; } });
    B.splice(bi + 1, 0, { z: zb, n: 1, own: null, st: null }); toast('Nachtlager ' + (ctx.netz.N[zb]?.[0] || zb) + ' eingefügt.'); return rbAenderung(ctx);
  }
}
function rbForm(ctx, e) {
  const f = e.target.closest('[data-form]'); if (!f) return; e.preventDefault();
  const i = +f.dataset.form, n = f.n.value.trim(), l = f.l.value.trim(), err = document.getElementById('rb-e-' + i);
  if (!n) { err.textContent = 'Bitte einen Namen eingeben.'; return; }
  const c = rbKoord(l);
  if (l && !c && !/^https:\/\//.test(l)) { err.textContent = 'Keine Koordinaten erkannt. Lange Google-Maps-Adresse oder „-31.13, 138.39“ eingeben – oder leer lassen.'; return; }
  const b = rbBloecke(ctx)[i];
  b.own = { name: n, link: l || null, lat: c ? c[0] : null, lon: c ? c[1] : null }; if (!b.st) b.st = 'idee';
  if (l && !c) toast('Link gespeichert – Lage bleibt Mitte des Schlafbereichs (Kurzlink ohne Koordinaten).');
  ctx.offen = null; rbAenderung(ctx);
}

// Kachel auf der Highlights-Seite einer Suche
async function rbEinstieg(sid, ziel) {
  try {
    const liste = await hlCall('roadtrip_liste', { suche_id: sid });
    if (!liste?.length) return;
    ziel.replaceChildren(...liste.map(r => el('a', { class: 'rb-entry', href: '#/highlights/' + sid + '/roadbook/' + r.id },
      el('span', { class: 'rb-entry-ic', 'aria-hidden': true }, '🚙'), el('span', {}, el('b', {}, r.titel), el('small', {}, 'Roadbook · ab ' + new Date(r.start_datum + 'T00:00:00').toLocaleDateString('de-DE', { day: 'numeric', month: 'numeric' }) + (r.ziel_naechte ? ' · ' + r.ziel_naechte + ' Nächte' : ''))),
      el('span', { class: 'rb-entry-go', 'aria-hidden': true }, '→'))));
  } catch { /* Roadbook ist optional */ }
}
