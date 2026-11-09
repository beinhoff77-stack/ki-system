/* Reisen › Highlights V2 (Werkstatt #154): Karte zuerst → Regionen mit fertigen Highlights → Detail → „Hier weitersuchen“.
   Server: Edge Function „highlights“ (api.highlights_*). Kosten entstehen nur nach Klick: ein Wunsch holt die Regionen und danach automatisch
   die Highlights je Region; tiefer wird nur auf Ansage gesucht („Hier weitersuchen“, Frage).
   Nichts wird automatisch ausgeschlossen: „Erstmal nicht“ verschiebt nur in eine eigene Ansicht und ist jederzeit zurückholbar.
   „Ich bin hier“ nutzt den Standort nur im Gerät (nächster bekannter Punkt) – er wird nicht gesendet. */
'use strict';

const hlApi = () => API.replace(/app-api$/, 'highlights'); // API stammt aus app.js (lädt danach)
const HL_FAMILIE = [{ k: 'E', alter: 99 }, { k: 'E', alter: 99 }, { k: '13', alter: 13 }, { k: '11', alter: 11 }];
const HL_TYP = { region: ['Region', '◍'], ort: ['Ort', '⌖'], stadt: ['Stadt', '▦'], viertel: ['Viertel', '▤'], tauchen: ['Tauchen', '≈'], tiere: ['Tiere', '❦'], natur: ['Natur', '▲'], tempel: ['Tempel', '⛩'], altstadt: ['Altstadt', '⌂'], museum: ['Museum', '▥'], restaurant: ['Restaurant', '◐'], unterkunft: ['Unterkunft', '⌂'], erlebnis: ['Erlebnis', '✦'] };
// Themen: Farbe + Zeichen für Chips und Kartenpunkte
const HL_THEMA = { tauchen: ['Meer & Tauchen', '≈', '#2a6f97'], tiere: ['Tiere', '❦', '#8a6420'], natur: ['Natur', '▲', '#3f7d3a'], kultur: ['Kultur', '⌂', '#7b4b94'], essen: ['Essen & Trinken', '◐', '#c0662b'], wohnen: ['Wohnen', '⌂', '#1f8585'], ort: ['Ort', '⌖', '#5a6878'], erlebnis: ['Erlebnis', '✦', '#a8801a'] };
const hlThemaVon = (typ) => ({ tauchen: 'tauchen', tiere: 'tiere', natur: 'natur', tempel: 'kultur', altstadt: 'kultur', museum: 'kultur', restaurant: 'essen', unterkunft: 'wohnen', ort: 'ort', stadt: 'ort', viertel: 'ort' })[typ] || 'erlebnis';
const hlThema = (t) => HL_THEMA[t] || HL_THEMA.erlebnis;
const HL_ANDRANG = ['', 'kaum touristisch', 'lokaler Alltag', 'bekannter Stopp', 'Busgruppen', 'Massentourismus'];
const HL_WEITER = [['essen', 'Essen & Trinken hier'], ['wohnen', 'Wohnen hier'], ['naehe', 'In der Nähe (≤ 30 Min.)'], ['kinder', 'Für die Kinder']];
const HL_KOSTEN_START = 'ca. 1–2 USD · 3–5 Min.: erst die Regionen, danach automatisch die Highlights je Region';
const HL_KOSTEN_KLEIN = 'ca. 0,10 USD · 1–2 Min.';
// W155: Recherche wahlweise automatisch (Server, kostet) oder im Chat (Claude/ChatGPT über den Council, ohne Serverkosten)
const hlModus = () => (hlLese('hl2_modus', 'auto') === 'chat' ? 'chat' : 'auto');
const hlKostenKlein = () => (hlModus() === 'chat' ? 'ohne Serverkosten · erledigt Claude oder ChatGPT im Chat' : HL_KOSTEN_KLEIN);
function hlModusWahl(neu) {
  const m = hlModus();
  const knopf = (wert, text) => el('button', { type: 'button', class: 'hl2-modus-k' + (m === wert ? ' an' : ''), 'aria-pressed': m === wert,
    onclick: () => { hlSchreibe('hl2_modus', wert); neu(); } }, text);
  return el('div', { class: 'hl2-modus', role: 'group', 'aria-label': 'Recherche' }, el('span', { class: 'small muted' }, 'Recherche:'),
    knopf('auto', '⚡ Automatisch'), knopf('chat', '💬 Im Chat'));
}
function hlChatKasten(auftraege) {
  return el('div', { class: 'hl2-chat' }, auftraege.map(a => {
    const satz = 'Highlights Auftrag ' + a.portion_id + ' ausführen';
    const kopie = el('button', { type: 'button', class: 'link', onclick: async () => { try { await navigator.clipboard.writeText(satz); toast('Kopiert – im Chat einfügen.'); } catch { toast(satz); } } }, 'Kopieren');
    return el('div', { class: 'hl2-chat-z' }, el('p', {}, el('b', {}, a.status === 'chat_arbeit' ? '💬 Wird gerade im Chat recherchiert' : '💬 Wartet auf den Chat'),
      a.linse || a.text ? ' · ' + ({ essen: 'Essen & Trinken', wohnen: 'Wohnen', naehe: 'In der Nähe', kinder: 'Für die Kinder' }[a.linse] || ('„' + a.text + '“')) : ''),
      el('p', { class: 'small' }, 'Schreib Claude oder ChatGPT: ', el('code', {}, satz), ' ', kopie),
      el('p', { class: 'small muted' }, 'Das Ergebnis erscheint hier von selbst.'));
  }));
}

async function hlCall(aktionName, daten = {}) {
  const r = await fetch(hlApi() + '/aktion', { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + (store.token || '') }, body: JSON.stringify({ aktion: aktionName, daten }) });
  let j; try { j = await r.json(); } catch { j = { ok: false, fehler: 'Keine Antwort (' + r.status + ')' }; }
  if (r.status === 401) { store.token = null; route('login'); throw new Error('Nicht angemeldet'); }
  if (!j.ok) throw new Error(j.fehler || 'Anfrage fehlgeschlagen');
  return j.ergebnis;
}
const hlLese = (k, fb = null) => { try { return JSON.parse(localStorage.getItem(k)) ?? fb; } catch { return fb; } };
const hlSchreibe = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* privat */ } };
const hlHref = (sid, kid) => '#/highlights/' + sid + (kid ? '/' + kid : '');
const hlSicher = (u) => (typeof u === 'string' && /^https:\/\/[^\s"<>@]+$/.test(u) ? u : null);
const hlFill = (node, ...kids) => node.replaceChildren(...kids.flat().filter(k => k !== null && k !== undefined && k !== false)); // replaceChildren schreibt sonst „null“
const hlKurz = s => (s.length > 34 ? s.slice(0, 32) + '…' : s);
const hlZahl = (x) => (x === null || x === undefined || x === '' ? null : (Number.isFinite(Number(x)) ? Number(x) : null));
const hlKm = (a, b, c, d) => { const r = Math.PI / 180, x = Math.sin((c - a) * r / 2) ** 2 + Math.cos(a * r) * Math.cos(c * r) * Math.sin((d - b) * r / 2) ** 2; return 12742 * Math.asin(Math.sqrt(x)); };
const hlHlName = (h) => (typeof h === 'string' ? h : h?.name || '');
const hlHlThema = (h) => (typeof h === 'object' && h?.thema && HL_THEMA[h.thema] ? h.thema : 'erlebnis');

// ---------- Einstieg ----------
async function viewHighlights(arg) {
  if (arg === 'merk') return hlMerkliste();
  const [sid, kid] = String(arg || '').split('/').map(x => (/^\d+$/.test(x) ? Number(x) : null));
  if (sid) return hlEbene(sid, kid);
  return hlStart();
}

function hlDiktat(feld) {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) return null;
  const btn = el('button', { type: 'button', class: 'hl-mic', 'aria-label': 'Diktieren' }, '🎙');
  let rec = null;
  btn.onclick = () => {
    if (rec) { rec.stop(); return; }
    rec = new SR(); rec.lang = 'de-DE'; rec.interimResults = true;
    const vorher = feld.value ? feld.value.trim() + ' ' : '';
    rec.onresult = e => { feld.value = vorher + [...e.results].map(x => x[0].transcript).join(''); };
    rec.onend = () => { rec = null; btn.classList.remove('an'); };
    btn.classList.add('an'); rec.start();
  };
  return btn;
}

async function hlStart() {
  setChrome('Highlights', { tab: 'highlights' });
  const live = viewGuard();
  const wunsch = el('textarea', { id: 'hl-wunsch', rows: 2, maxlength: 500, placeholder: 'z. B. Südaustralien und Tasmanien: Meer, Tiere, Natur – ruhig und besonders' });
  const zeit = el('input', { type: 'text', maxlength: 60, placeholder: 'z. B. Dez 2026 – Jan 2027' });
  const andrang = el('select', {}, el('option', { value: '' }, 'egal'), [1, 2, 3, 4].map(n => el('option', { value: n }, 'bis ' + n + '/5 · ' + HL_ANDRANG[n])));
  andrang.value = '3';
  const status = el('p', { class: 'small muted', role: 'status' }, 'Erst der Klick startet die Recherche (' + HL_KOSTEN_START + ').');
  const los = el('button', { class: 'primary', type: 'submit' }, 'Regionen & Highlights holen');
  const form = el('form', { class: 'hl-wish' },
    el('p', { class: 'eyebrow' }, 'REISEN · HIGHLIGHTS'),
    el('h2', {}, 'Wohin zieht es euch?'),
    el('div', { class: 'hl-wish-row' }, wunsch, hlDiktat(wunsch)),
    el('div', { class: 'hl-wish-opts' }, el('label', {}, 'Reisezeit', zeit), el('label', {}, 'Andrang', andrang)),
    el('p', { class: 'small muted' }, 'Vorlieben sortieren nur – nichts wird ausgeschlossen. Ändern geht jederzeit.'),
    el('div', { class: 'row' }, los, el('a', { href: '#/highlights/merk' }, '♥ Will ich →')), status);
  form.addEventListener('submit', async e => {
    e.preventDefault();
    if (wunsch.value.trim().length < 2) { wunsch.focus(); return; }
    los.disabled = true; status.textContent = 'Wird angelegt …';
    try {
      const vorlieben = {}; if (zeit.value.trim()) vorlieben.reisezeit = zeit.value.trim(); if (andrang.value) vorlieben.andrang_max = Number(andrang.value);
      const s = await hlCall('suche_speichern', { wunsch: wunsch.value.trim(), vorlieben });
      await hlCall('portion', { suche_id: s.id, art: 'start' });
      route('highlights', String(s.id));
    } catch (err) { status.textContent = err.message; los.disabled = false; }
  });
  const liste = el('div', { class: 'hl-wishes' }, el('div', { class: 'spinner' }, 'Lade …'));
  const weiter = hlLese('hl_last');
  hlFill(main, form,
    weiter ? el('a', { class: 'hl-continue', href: hlHref(weiter.sid, weiter.kid) }, el('span', { class: 'eyebrow' }, 'WEITER BEI'), el('strong', {}, weiter.titel || 'letzter Ansicht'), el('span', { 'aria-hidden': true }, '→')) : null,
    el('h3', { class: 'start-theme-title' }, 'Eure Wünsche'), liste);
  try {
    const r = await hlCall('lesen', {});
    if (!live()) return;
    hlFill(liste, ...(r.suchen.length ? r.suchen.map(s => el('a', { class: 'hl-wish-card', href: hlHref(s.id) },
      hlBild(s.bild, 'region', 'hl-wish-img'),
      el('div', {}, el('strong', {}, s.wunsch), el('span', { class: 'small muted' }, s.vorschlaege + ' Orte & Highlights · ♥ ' + s.gemerkt)))) : [el('p', { class: 'muted' }, 'Noch kein Wunsch. Schreib oben, worauf ihr Lust habt.')]));
  } catch (e) { if (live()) hlFill(liste, el('p', { class: 'err-text' }, e.message)); }
}

// ---------- Bausteine ----------
function hlBild(b, typ, cls = 'hl-img') {
  const box = el('figure', { class: cls });
  const url = hlSicher(b?.url);
  if (url) {
    const img = document.createElement('img');
    img.referrerPolicy = 'no-referrer'; img.loading = 'lazy'; img.decoding = 'async'; img.alt = ''; img.src = url;
    img.onerror = () => { img.remove(); box.classList.add('leer'); };
    box.append(img);
    if (b.urheber || b.lizenz) box.append(el('figcaption', {}, el('a', { href: hlSicher(b.quelle_url) || '#', target: '_blank', rel: 'noopener noreferrer' }, 'Foto: ' + (b.urheber || 'unbekannt') + ' · ' + (b.lizenz || '') + ' · ' + (b.quelle || ''))));
  } else box.classList.add('leer');
  box.dataset.glyph = typ === 'region' ? '◍' : hlThema(hlThemaVon(typ))[1];
  return box;
}
const hlBeleg = (ok, url) => ok ? el('a', { class: 'hl-beleg ok', href: hlSicher(url) || '#', target: '_blank', rel: 'noopener noreferrer', title: 'Belegt: Quelle abgerufen' }, '✓') : el('span', { class: 'hl-beleg', title: 'Schätzung, keine abgerufene Quelle' }, '○');

// Familie: nur eine Zeile, wenn jemand nicht mitkann oder es einen Hinweis gibt (kein Hinweis heißt NICHT „alle geeignet“).
function hlFamilieText(sb, alter) {
  const kinder = (Array.isArray(alter) && alter.length ? alter : HL_FAMILIE.filter(p => p.alter < 99).map(p => p.alter)).map(Number).filter(Boolean);
  const min = Number(sb.mindestalter) || 0;
  const zuJung = min ? kinder.filter(a => a < min) : [];
  const teile = [];
  if (zuJung.length) teile.push((zuJung.length === kinder.length && kinder.length > 1 ? 'Beide Kinder' : zuJung.map(a => a + '-Jährige/r').join(' und ')) + ' zu jung (ab ' + min + ' J.)');
  if (sb.familie_hinweis) teile.push(sb.familie_hinweis);
  return teile.length ? teile.join(' · ') : null;
}
// Rot nur bei echter Sperre/Einschränkung
const hlWarnung = (sb) => sb.warnung && sb.warnung_art ? el('p', { class: 'hl-warnung' }, '⚠ ', sb.warnung_art === 'gesperrt' ? 'Gesperrt: ' : 'Eingeschränkt: ', sb.warnung, ' ', hlBeleg(sb.warnung_belegt, sb.warnung_quelle)) : null;
// WOW (W155): Sterne + Begründung als Fließtext, keine Box. 5 = weltweit einzigartig … 1 = Füller (Skala im Server)
const HL_WOW = { 5: 'weltweit einzigartig', 4: 'Top des Landes', 3: 'schöner Programmpunkt', 2: 'nett', 1: 'Füller' };
const hlWow = (sb) => {
  const n = Number(sb.wow) >= 1 && Number(sb.wow) <= 5 ? Math.round(Number(sb.wow)) : null;
  if (!n && !sb.besonders) return null;
  return el('p', { class: 'hl2-wow' },
    n ? el('span', { class: 'hl2-sterne', title: 'WOW ' + n + '/5 – ' + HL_WOW[n], 'aria-label': 'WOW ' + n + ' von 5: ' + HL_WOW[n] }, '★'.repeat(n), el('span', { class: 'aus' }, '★'.repeat(5 - n))) : null,
    n ? el('span', { class: 'hl2-wow-stufe' }, HL_WOW[n]) : null,
    sb.besonders ? el('span', { class: 'hl2-wow-text' }, sb.besonders) : null);
};
// Weiterlesen-Knöpfe (W155): Google Maps (Suche nach Name + Region, kein Kartenschlüssel nötig), Wikipedia (Suche -> Artikel), erste belegte Quelle
function hlLinks(k, ortHinweis, klein) {
  const sb = k.steckbrief || {};
  const knopf = (href, sym, text, titel) => el('a', { class: 'hl2-link', href, target: '_blank', rel: 'noopener noreferrer', title: titel }, el('span', { 'aria-hidden': true }, sym), ' ', text);
  const ort = [sb.hauptort, ortHinweis].filter(Boolean).find(x => !String(k.titel).includes(x)) || '';
  const maps = 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent([k.titel, ort].filter(Boolean).join(', '));
  const wiki = sb.wiki_titel ? 'https://en.wikipedia.org/w/index.php?search=' + encodeURIComponent(sb.wiki_titel) : null;
  const qs = (k.quellen || []).filter(q => hlSicher(q.url));
  const q = qs.find(x => x.abgerufen) || qs[0];
  let host = ''; try { host = q ? new URL(q.url).hostname.replace(/^www\./, '') : ''; } catch { host = ''; }
  return el('div', { class: 'hl2-links' + (klein ? ' klein' : '') },
    knopf(maps, '📍', 'Google Maps', 'In Google Maps öffnen'),
    wiki ? knopf(wiki, '📖', 'Wikipedia', 'Wikipedia: ' + sb.wiki_titel) : null,
    q && host ? knopf(q.url, '🌐', klein ? 'Mehr lesen' : 'Mehr lesen · ' + host, host + (q.abgerufen ? ' (von der Recherche abgerufen)' : '')) : null);
}

// Will ich / Erstmal nicht – zweimal tippen setzt zurück auf offen
function hlStatusKnoepfe(k, ctx, klein = false) {
  const will = el('button', { type: 'button', class: 'hl2-will' + (k.status === 'gemerkt' ? ' an' : ''), 'aria-pressed': k.status === 'gemerkt', 'aria-label': 'Will ich: ' + k.titel }, klein ? (k.status === 'gemerkt' ? '♥' : '♡') : (k.status === 'gemerkt' ? '♥ Will ich' : '♡ Will ich'));
  will.onclick = e => { e.preventDefault(); e.stopPropagation(); hlEntscheiden(k, k.status === 'gemerkt' ? 'offen' : 'gemerkt', ctx); };
  const nicht = el('button', { type: 'button', class: 'hl2-nicht' + (k.status === 'weg' ? ' an' : ''), 'aria-pressed': k.status === 'weg', 'aria-label': 'Erstmal nicht: ' + k.titel }, klein ? '✕' : (k.status === 'weg' ? '✕ Erstmal nicht' : 'Erstmal nicht'));
  nicht.onclick = e => { e.preventDefault(); e.stopPropagation(); hlEntscheiden(k, k.status === 'weg' ? 'offen' : 'weg', ctx); };
  return el('div', { class: 'hl2-status' + (klein ? ' klein' : '') }, will, nicht);
}
async function hlEntscheiden(k, status, ctx) {
  const vorher = k.status;
  try {
    await hlCall('entscheiden', { knoten_id: k.id, status });
    if (status === 'weg') hlRueckgaengig(k, vorher, ctx); else toast(status === 'gemerkt' ? '♥ Will ich' : 'Zurück auf offen.');
    await ctx.neu();
  } catch (e) { toast(e.message, true); }
}
function hlRueckgaengig(k, vorher, ctx) {
  const t = $('#toast');
  t.replaceChildren('„' + k.titel + '“ → Erstmal nicht. ', el('button', { type: 'button', class: 'link', onclick: async () => { t.hidden = true; await hlCall('entscheiden', { knoten_id: k.id, status: vorher }).catch(e => toast(e.message, true)); await ctx.neu(); } }, 'Rückgängig'));
  t.className = 'toast'; t.hidden = false; clearTimeout(toastTimer); toastTimer = setTimeout(() => { t.hidden = true; }, 6000);
}
function hlWisch(node, links) {
  let x0 = null, y0 = 0;
  node.addEventListener('touchstart', e => { const t = e.touches[0]; x0 = t.clientX; y0 = t.clientY; }, { passive: true });
  node.addEventListener('touchend', e => {
    if (x0 === null) return; const t = e.changedTouches[0], dx = t.clientX - x0, dy = t.clientY - y0; x0 = null;
    if (dx < -90 && Math.abs(dy) < 50 && !e.target.closest('a,button,input,select,textarea,summary')) links();
  });
}

// Ansichten: Alle (ohne „Erstmal nicht“) · Will ich · Erstmal nicht
const hlFilter = (liste, ansicht) => liste.filter(x => (ansicht === 'will' ? x.status === 'gemerkt' : ansicht === 'nicht' ? x.status === 'weg' : x.status !== 'weg'));
function hlTabs(aktiv, zahlen, wahl) {
  return el('div', { class: 'hl2-tabs', role: 'tablist', 'aria-label': 'Ansicht' },
    [['alle', 'Alle', zahlen.alle], ['will', '♥ Will ich', zahlen.will], ['nicht', '✕ Erstmal nicht', zahlen.nicht]].map(([k, l, n]) =>
      el('button', { type: 'button', role: 'tab', 'aria-selected': aktiv === k, class: 'hl2-tab' + (aktiv === k ? ' an' : ''), onclick: () => wahl(k) }, l, ' ', el('span', { class: 'hl2-n' }, String(n)))));
}

// ---------- Karte (Leaflet) ----------
function hlKarteBox(hoch = false) {
  const canvas = el('div', { class: 'hl2-map' + (hoch ? ' hoch' : ''), role: 'region', 'aria-label': 'Karte' });
  const box = { canvas, map: null, layer: null, anzahl: 0, bewegt: false };
  box.zeichne = (punkte) => {
    if (!window.L) { hlFill(canvas, el('p', { class: 'small muted' }, 'Karte gerade nicht verfügbar.')); return; }
    if (!box.map) {
      box.map = L.map(canvas, { scrollWheelZoom: false, zoomSnap: 0.5 }).setView([-30, 135], 3);
      L.tileLayer('https://tile.openstreetmap.de/{z}/{x}/{y}.png', { minZoom: 2, maxZoom: 18, keepBuffer: 1,
        attribution: '© <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap-Mitwirkende</a>' }).addTo(box.map);
      box.layer = L.layerGroup().addTo(box.map);
      box.map.on('dragstart', () => { box.bewegt = true; });
    }
    box.layer.clearLayers();
    const ll = [];
    // Highlights zuerst, Regionen darüber
    for (const p of [...punkte].sort((a, b) => (a.art === 'region') - (b.art === 'region'))) {
      const lat = hlZahl(p.lat), lon = hlZahl(p.lon);
      if (lat === null || lon === null) continue;
      const pos = [lat, lon]; ll.push(pos);
      let m;
      if (p.art === 'region' || p.art === 'ort') {
        m = L.marker(pos, { title: p.titel, alt: p.titel, keyboard: true, zIndexOffset: 500,
          icon: L.divIcon({ className: 'hl2-pin' + (p.art === 'ort' ? ' ort' : '') + (p.status === 'gemerkt' ? ' will' : '') + (p.status === 'weg' ? ' nicht' : ''), html: el('span', {}, p.nr ? String(p.nr) : '★'), iconSize: [30, 30], iconAnchor: [15, 15] }) });
      } else {
        const farbe = p.status === 'weg' ? '#9aa5b1' : hlThema(p.thema)[2];
        m = L.circleMarker(pos, { radius: p.status === 'gemerkt' ? 9 : 6.5, color: p.status === 'gemerkt' ? '#c0392b' : '#fff', weight: p.status === 'gemerkt' ? 3 : 2, fillColor: farbe, fillOpacity: p.status === 'weg' ? 0.45 : 0.95 });
      }
      m.bindTooltip(el('span', {}, (p.status === 'gemerkt' ? '♥ ' : '') + p.titel), { direction: 'top' });
      if (p.klick) m.on('click', p.klick);
      m.addTo(box.layer);
    }
    setTimeout(() => box.map && box.map.invalidateSize(), 0);
    if (ll.length > box.anzahl && !box.bewegt) {
      if (ll.length === 1) box.map.setView(ll[0], 11); else box.map.fitBounds(ll, { padding: [26, 26], maxZoom: 12 });
    }
    box.anzahl = Math.max(box.anzahl, ll.length);
  };
  box.weg = () => { if (box.map) { box.map.remove(); box.map = null; } };
  return box;
}

function hlIchBinHier(punkte, sid) {
  if (!navigator.geolocation) { toast('Standort ist hier nicht verfügbar.', true); return; }
  toast('Standort wird bestimmt …');
  navigator.geolocation.getCurrentPosition(pos => {
    const a = pos.coords.latitude, b = pos.coords.longitude;
    let best = null, bd = Infinity;
    for (const p of punkte) { const lat = hlZahl(p.lat), lon = hlZahl(p.lon); if (lat === null || lon === null || !p.id) continue; const d = hlKm(a, b, lat, lon); if (d < bd) { bd = d; best = p; } }
    if (!best) { toast('Noch keine Orte mit Lage.', true); return; }
    toast('Am nächsten: ' + best.titel + ' (' + (bd < 10 ? bd.toFixed(1).replace('.', ',') : Math.round(bd)) + ' km)');
    location.hash = hlHref(sid, best.id);
  }, () => toast('Standort nicht freigegeben.', true), { enableHighAccuracy: false, timeout: 10000, maximumAge: 300000 });
}

// ---------- Ansicht: Übersicht · Region · Detail ----------
async function hlEbene(sid, kid) {
  setChrome('Highlights', { tab: 'highlights', back: true });
  const live = viewGuard();
  const ansichtKey = 'hl2_ansicht_' + sid + '_' + (kid || 0);
  let timer = null, ansicht = sessionStorage.getItem(ansichtKey) || 'alle';
  const karte = hlKarteBox(!kid);
  disposeSuche = () => { clearTimeout(timer); karte.weg(); };
  const pfad = el('nav', { class: 'hl-pfad', 'aria-label': 'Pfad' });
  const kopf = el('header', { class: 'hl2-kopf' });
  const mitte = el('div', { class: 'hl2-mitte' });
  const kartenZeile = el('div', { class: 'hl2-map-zeile' });
  const lauf = el('div', { class: 'hl-lauf', role: 'status' });
  const chatBox = el('div');
  const tabs = el('div');
  const liste = el('div', { class: 'hl2-liste' });
  const unten = el('div', { class: 'hl2-unten' });
  hlFill(main, pfad, kopf, mitte, el('section', { class: 'hl2-map-wrap' }, karte.canvas, kartenZeile), chatBox, lauf, tabs, liste, unten);
  const ctx = { sid, alter: null, neu: () => lesen() };
  const setAnsicht = (a) => { ansicht = a; sessionStorage.setItem(ansichtKey, a); lesen(); };

  async function portion(art, extra = {}) {
    hlFill(lauf, el('div', { class: 'spinner' }, 'Wird angefragt …'));
    try { await hlCall('portion', { suche_id: sid, parent_id: kid, art, modus: hlModus(), ...extra }); await lesen(); }
    catch (e) { hlFill(lauf, el('p', { class: 'hl-ende' }, e.message)); }
  }
  function frageForm(platzhalter) {
    const frage = el('input', { type: 'text', maxlength: 400, placeholder: platzhalter });
    const f = el('form', { class: 'hl-frage-form' }, frage, hlDiktat(frage), el('button', { type: 'submit' }, 'Fragen'));
    f.onsubmit = e => { e.preventDefault(); if (frage.value.trim().length >= 3) portion('frage', { text: frage.value.trim() }); };
    return f;
  }

  async function lesen() {
    clearTimeout(timer);
    let r;
    try { r = await hlCall('lesen', { suche_id: sid, knoten_id: kid, mit_weg: true }); }
    catch (e) { if (live()) hlFill(lauf, el('p', { class: 'err-text' }, e.message)); return; }
    if (!live()) return;
    const v = r.suche.vorlieben || {};
    ctx.alter = Array.isArray(v.familie_alter) ? v.familie_alter : null;
    const titel = r.knoten ? r.knoten.titel : r.suche.wunsch;
    hlSchreibe('hl_last', { sid, kid, titel });
    setChrome(hlKurz(titel), { tab: 'highlights', back: true });
    const sep = () => el('span', { 'aria-hidden': true }, '›');
    hlFill(pfad, el('a', { href: '#/highlights' }, 'Highlights'), sep(),
      ...(r.pfad.length ? [el('a', { href: hlHref(sid) }, hlKurz(r.suche.wunsch)), ...r.pfad.flatMap((p, i) => [sep(), i === r.pfad.length - 1 ? el('strong', {}, p.titel) : el('a', { href: hlHref(sid, p.id) }, p.titel)])] : [el('strong', {}, hlKurz(r.suche.wunsch))]));
    const laufend = (r.laufend || []).map(x => (x === null ? 0 : Number(x)));
    if (!r.knoten) uebersicht(r, v, laufend);
    else if (r.knoten.typ === 'region') region(r, laufend);
    else detail(r, laufend);
    const chatHier = (r.chat_offen || []).filter(a => (a.parent_id ?? null) === (kid ?? null));
    hlFill(chatBox, chatHier.length ? hlChatKasten(chatHier) : null);
    if (laufend.length) timer = setTimeout(lesen, 5000);
    else if (chatHier.length) timer = setTimeout(lesen, 15000);
  }

  // ----- Übersicht: Karte + Regionen mit ihren Highlights -----
  function uebersicht(r, v, laufend) {
    const regionen = r.karten, nr = new Map(regionen.map((k, i) => [k.id, i + 1]));
    const unterVon = new Map(regionen.map(k => [k.id, r.unter.filter(u => u.parent_id === k.id)]));
    const fertige = r.portionen.filter(p => p.status === 'fertig'), letzte = r.portionen[r.portionen.length - 1];
    const fazit = fertige.length ? fertige[0].fazit : null;
    // Vorlieben (änderbar, sortieren nur)
    const andr = el('button', { type: 'button', class: 'hl-chip pref' }, 'Andrang ' + (v.andrang_max ? 'bis ' + v.andrang_max + '/5' : 'egal') + ' ✎');
    andr.onclick = async () => { const n = v.andrang_max ? (v.andrang_max % 5) + 1 : 3; await hlCall('suche_speichern', { id: sid, vorlieben: { ...v, andrang_max: n === 5 ? null : n } }).catch(e => toast(e.message, true)); toast('Gilt für die nächsten Vorschläge.'); lesen(); };
    const zeitChip = el('button', { type: 'button', class: 'hl-chip pref' }, 'Reisezeit ' + (v.reisezeit || 'offen') + ' ✎');
    zeitChip.onclick = () => hlZeitDialog(v, async neu => { await hlCall('suche_speichern', { id: sid, vorlieben: neu }); lesen(); });
    hlFill(kopf, el('p', { class: 'eyebrow' }, 'EUER WUNSCH'), el('h2', {}, r.suche.wunsch), el('div', { class: 'hl-chips' }, andr, zeitChip), fazit ? el('p', { class: 'hl-fazit' }, fazit) : null);
    hlFill(mitte);
    // Karte: Regionen als Nummern, Highlights als Punkte (umschaltbar)
    const mitPunkten = hlLese('hl2_punkte', true);
    const punkte = [];
    for (const k of regionen) {
      const sb = k.steckbrief || {};
      punkte.push({ art: 'region', id: k.id, nr: nr.get(k.id), titel: k.titel, lat: sb.lat, lon: sb.lon, status: k.status, klick: () => { location.hash = hlHref(sid, k.id); } });
      if (mitPunkten) for (const u of unterVon.get(k.id)) punkte.push({ art: 'hl', id: u.id, titel: u.titel + ' · ' + k.titel, lat: u.lat, lon: u.lon, status: u.status, thema: hlThemaVon(u.typ), klick: () => { location.hash = hlHref(sid, u.id); } });
    }
    karte.zeichne(punkte.filter(p => p.status !== 'weg' || ansicht === 'nicht'));
    const schalter = el('input', { type: 'checkbox' }); schalter.checked = mitPunkten;
    schalter.onchange = () => { hlSchreibe('hl2_punkte', schalter.checked); lesen(); };
    const alle = [...regionen.map(k => ({ ...k, steckbrief: k.steckbrief })), ...r.unter];
    hlFill(kartenZeile, el('label', { class: 'hl2-schalter' }, schalter, ' Highlights auf der Karte'),
      el('button', { type: 'button', class: 'link', onclick: () => hlIchBinHier([...regionen.map(k => ({ id: k.id, titel: k.titel, lat: k.steckbrief?.lat, lon: k.steckbrief?.lon })), ...r.unter], sid) }, '📍 Ich bin hier'),
      el('span', { class: 'hl2-legende' }, ['tauchen', 'tiere', 'natur', 'kultur', 'essen'].map(t => el('span', {}, el('i', { style: 'background:' + hlThema(t)[2] }), hlThema(t)[0]))));
    // Laufende Recherchen
    const regionenLaufen = laufend.filter(x => x && nr.has(x)).length;
    if (laufend.includes(0)) hlFill(lauf, el('div', { class: 'spinner' }, regionen.length ? 'Weitere Regionen werden recherchiert … (1–3 Min.)' : 'Die Regionen werden recherchiert … (2–4 Min., mit Websuche). Danach kommen automatisch die Highlights je Region.'));
    else if (regionenLaufen) hlFill(lauf, el('div', { class: 'spinner' }, 'Highlights für ' + regionenLaufen + (regionenLaufen === 1 ? ' Region' : ' Regionen') + ' werden recherchiert … – die Übersicht füllt sich von selbst.'));
    else if (letzte?.status === 'fehler') hlFill(lauf, el('p', { class: 'err-text' }, 'Letzte Anfrage fehlgeschlagen: ' + (letzte.fehler || 'unbekannt') + '. Du kannst es erneut versuchen.'));
    else hlFill(lauf);
    // Ansichten
    hlFill(tabs, hlTabs(ansicht, { alle: hlFilter(regionen, 'alle').length, will: hlFilter(alle, 'will').length, nicht: hlFilter(alle, 'nicht').length }, setAnsicht));
    if (ansicht === 'alle') {
      hlFill(liste, ...hlFilter(regionen, 'alle').map(k => hlRegionKarte(k, nr.get(k.id), unterVon.get(k.id), laufend.includes(k.id), ctx)),
        !regionen.length && !laufend.length ? el('p', { class: 'muted' }, 'Noch keine Regionen.') : null);
    } else {
      // Will ich / Erstmal nicht: nach Region gruppiert – Regionen selbst und ihre Highlights
      const gruppen = regionen.map(k => ({ k, eintraege: [...(hlFilter([k], ansicht).length ? [k] : []), ...hlFilter(unterVon.get(k.id), ansicht)] })).filter(g => g.eintraege.length);
      hlFill(liste, ...(gruppen.length ? gruppen.map(g => el('section', { class: 'hl2-gruppe' },
        el('h3', {}, el('span', { class: 'hl2-nr' }, String(nr.get(g.k.id))), el('a', { href: hlHref(sid, g.k.id) }, g.k.titel)),
        g.eintraege.map(x => hlKurzZeile(x, x.id === g.k.id, ctx)))) : [el('p', { class: 'muted' }, ansicht === 'will' ? 'Noch nichts mit ♥ markiert.' : 'Nichts aussortiert.')]));
    }
    hlFill(unten, hlModusWahl(lesen), el('div', { class: 'hl-mehr' },
      el('button', { type: 'button', class: regionen.length ? '' : 'primary', disabled: laufend.includes(0), onclick: () => portion(regionen.length ? 'mehr' : 'start') }, regionen.length ? 'Weitere Regionen suchen' : 'Regionen holen'),
      el('span', { class: 'small muted' }, regionen.length ? (hlModus() === 'chat' ? hlKostenKlein() : HL_KOSTEN_KLEIN + ' (+ Highlights je neuer Region)') : HL_KOSTEN_START)),
      frageForm('Frage zum ganzen Wunsch, z. B. „Wo sieht man Seelöwen?“'),
      el('p', { class: 'small muted' }, regionen.length + ' Regionen · ' + r.unter.length + ' Highlights' + hlKostenText(r)));
  }

  // ----- Region: alle Highlights der Region, sofort da -----
  function region(r, laufend) {
    const k = r.knoten, sb = k.steckbrief || {}, kinder = r.karten;
    const saison = sb.saison || {};
    hlFill(kopf, el('div', { class: 'hl2-kopf-grid' }, hlBild(k.bild, 'region', 'hl2-kopf-img'),
      el('div', { class: 'hl2-kopf-text' }, el('p', { class: 'eyebrow' }, 'REGION'), el('h2', {}, k.titel),
        el('p', { class: 'hl2-meta' }, [sb.hauptort ? 'Basis: ' + sb.hauptort : null, sb.tage, saison.text ? 'Beste Zeit: ' + saison.text : null, sb.andrang ? 'Andrang ' + sb.andrang + '/5 · ' + HL_ANDRANG[sb.andrang] : null].filter(Boolean).join(' · ')),
        sb.wo ? el('p', { class: 'hl2-wo' }, el('b', {}, 'Wo & Anfahrt: '), sb.wo) : null,
        el('p', { class: 'hl2-warum' }, el('b', {}, 'Warum hin: '), sb.warum || sb.moment || ''),
        sb.besonders ? el('p', { class: 'hl2-besonders' }, el('b', {}, 'Nur hier: '), sb.besonders) : null,
        hlWarnung(sb), hlStatusKnoepfe(k, ctx))));
    hlFill(mitte);
    const punkte = [{ art: 'ort', titel: (sb.hauptort || k.titel), lat: sb.lat, lon: sb.lon, status: 'offen' },
      ...hlFilter(kinder, ansicht === 'nicht' ? 'nicht' : 'alle').map(c => ({ art: 'hl', id: c.id, titel: c.titel, lat: c.steckbrief?.lat, lon: c.steckbrief?.lon, status: c.status, thema: hlThemaVon(c.typ), klick: () => { location.hash = hlHref(sid, c.id); } }))];
    karte.zeichne(punkte);
    hlFill(kartenZeile, el('button', { type: 'button', class: 'link', onclick: () => hlIchBinHier(kinder.map(c => ({ id: c.id, titel: c.titel, lat: c.steckbrief?.lat, lon: c.steckbrief?.lon })), sid) }, '📍 Ich bin hier'),
      el('span', { class: 'small muted' }, '★ = Basis ' + (sb.hauptort || '')));
    const hierLaeuft = laufend.includes(k.id), letzte = r.portionen[r.portionen.length - 1];
    if (hierLaeuft) hlFill(lauf, el('div', { class: 'spinner' }, kinder.length ? 'Weitere Highlights werden recherchiert … (1–2 Min.)' : 'Die Highlights von ' + k.titel + ' werden gerade recherchiert … (1–2 Min.)'),
      !kinder.length && (sb.highlights || []).length ? el('div', { class: 'hl2-hchips' }, sb.highlights.map(h => hlVorabChip(h))) : null);
    else if (letzte?.status === 'fehler') hlFill(lauf, el('p', { class: 'err-text' }, 'Letzte Anfrage fehlgeschlagen: ' + (letzte.fehler || 'unbekannt') + '.'));
    else hlFill(lauf);
    const fazit = r.portionen.find(p => p.status === 'fertig' && p.fazit)?.fazit;
    hlFill(tabs, fazit ? el('p', { class: 'hl-fazit' }, fazit) : null, hlTabs(ansicht, { alle: hlFilter(kinder, 'alle').length, will: hlFilter(kinder, 'will').length, nicht: hlFilter(kinder, 'nicht').length }, setAnsicht));
    const sicht = hlFilter(kinder, ansicht);
    hlFill(liste, ...(sicht.length ? sicht.map(c => hlZeile(c, ctx, k.titel)) : [!hierLaeuft ? el('p', { class: 'muted' }, ansicht === 'alle' ? 'Noch keine Highlights.' : ansicht === 'will' ? 'Noch nichts mit ♥ markiert.' : 'Nichts aussortiert.') : null]));
    const ende = r.portionen.some(p => p.ende);
    hlFill(unten, ende ? el('p', { class: 'hl-ende' }, 'Das waren die starken Highlights hier. Frag gezielt, wenn dir etwas fehlt.') : null, hlModusWahl(lesen),
      el('div', { class: 'hl-mehr' },
        el('button', { type: 'button', class: kinder.length ? '' : 'primary', disabled: hierLaeuft, onclick: () => portion(kinder.length ? 'mehr' : 'start') }, kinder.length ? 'Mehr Highlights in ' + hlKurz(k.titel) : 'Highlights recherchieren'),
        el('span', { class: 'small muted' }, hlKostenKlein())),
      frageForm('In ' + hlKurz(k.titel) + ' fragen, z. B. „Wo Seedrachen sehen?“'),
      el('p', { class: 'small muted' }, kinder.length + ' Highlights' + hlKostenText(r)));
  }

  // ----- Detail: ein Highlight + „Hier weitersuchen“ -----
  function detail(r, laufend) {
    const k = r.knoten, sb = k.steckbrief || {}, th = hlThemaVon(k.typ), kinder = r.karten, eltern = r.eltern;
    const saison = sb.saison || {};
    const ortText = sb.ort || (eltern ? (eltern.steckbrief?.hauptort ? eltern.titel + ' · Basis ' + eltern.steckbrief.hauptort : eltern.titel) : '');
    const fakt = (label, ...wert) => el('div', {}, el('dt', {}, label), el('dd', {}, ...wert));
    const famText = hlFamilieText(sb, ctx.alter);
    const bild = k.bild || !['restaurant', 'unterkunft'].includes(k.typ) ? hlBild(k.bild, k.typ, 'hl2-kopf-img') : null;
    hlFill(kopf, el('div', { class: 'hl2-kopf-grid' + (bild ? '' : ' ohne-bild') }, bild,
      el('div', { class: 'hl2-kopf-text' },
        el('p', { class: 'hl2-thema t-' + th }, hlThema(th)[1] + ' ' + hlThema(th)[0]),
        el('h2', {}, k.titel),
        ortText ? el('p', { class: 'hl2-ort' }, '⌖ ', ortText) : null,
        sb.moment ? el('p', { class: 'hl2-moment' }, sb.moment) : null,
        hlWow(sb), hlWarnung(sb),
        hlLinks(k, eltern?.titel),
        el('dl', { class: 'hl-krit' }, fakt('Zeit', sb.zeit || '–'), fakt('Kosten für 4', sb.kosten_4 || '–', ' ', hlBeleg(sb.kosten_belegt, sb.kosten_quelle)),
          fakt('Andrang', el('b', {}, sb.andrang ? sb.andrang + '/5' : '–'), ' ', hlBeleg(sb.andrang_belegt, sb.andrang_quelle), el('small', {}, HL_ANDRANG[sb.andrang] || '')),
          fakt('Saison', el('span', { class: 'pill hl-s-' + (saison.status || 'unbekannt') }, { passt: 'passt', grenzwertig: 'grenzwertig', falsch: 'falsche Zeit', unbekannt: '?' }[saison.status || 'unbekannt']), ' ', saison.text || '')),
        famText ? el('p', { class: 'hl-familie' }, el('b', {}, 'Familie: '), famText) : null,
        hlStatusKnoepfe(k, ctx),
        el('details', { class: 'hl-mehrinfo' }, el('summary', {}, 'Mehr Infos'),
          sb.frage ? el('p', { class: 'hl-frage' }, el('b', {}, 'Vor dem Buchen klären: '), sb.frage, sb.pruefen?.text ? el('span', { class: 'small' }, ' · Prüfen: ', hlSicher(sb.pruefen.url) ? el('a', { href: sb.pruefen.url, target: '_blank', rel: 'noopener noreferrer' }, sb.pruefen.text) : sb.pruefen.text) : null) : null,
          (sb.fach || []).length ? el('dl', { class: 'hl-fach' }, sb.fach.map(f => el('div', {}, el('dt', {}, f.label), el('dd', {}, f.wert)))) : null,
          sb.lohnt || sb.eher_nicht ? el('div', { class: 'hl-wenn' }, sb.lohnt ? el('p', { class: 'ja' }, sb.lohnt) : null, sb.eher_nicht ? el('p', { class: 'nein' }, sb.eher_nicht) : null) : null,
          sb.tageszeit ? el('p', { class: 'small' }, el('b', {}, 'Beste Tageszeit: '), sb.tageszeit) : null,
          sb.ruhig ? el('p', { class: 'hl-ruhig' }, el('b', {}, 'Ruhiger erleben: '), sb.ruhig) : null,
          (k.quellen || []).length ? el('p', { class: 'hl-quellen small' }, 'Quellen (Stand ' + fmtDate(sb.geprueft_am) + '): ', k.quellen.filter(q => hlSicher(q.url)).map((q, i) => [i ? ' · ' : '', el('a', { href: q.url, target: '_blank', rel: 'noopener noreferrer' }, new URL(q.url).hostname.replace(/^www\./, '')), q.abgerufen ? ' ✓' : ' ○'])) : null))));
    // Hier weitersuchen
    const hierLaeuft = laufend.includes(k.id);
    hlFill(mitte, el('section', { class: 'hl2-weiter' }, el('h3', {}, 'Hier weitersuchen'),
      el('div', { class: 'hl2-weiter-knoepfe' }, HL_WEITER.map(([linse, label]) => el('button', { type: 'button', disabled: hierLaeuft, onclick: () => portion('mehr', { linse }) }, label))),
      frageForm('Frei fragen, z. B. „Wo gibt es hier guten Fisch?“'),
      hlModusWahl(lesen), el('p', { class: 'small muted' }, 'Je Suche ' + hlKostenKlein() + ' – Ergebnisse erscheinen unten.')));
    const sbE = eltern?.steckbrief || {};
    const lat = hlZahl(sb.lat) ?? hlZahl(sbE.lat), lon = hlZahl(sb.lon) ?? hlZahl(sbE.lon);
    karte.zeichne([{ art: 'ort', titel: k.titel + (hlZahl(sb.lat) === null ? ' (Lage ungefähr: ' + (eltern?.titel || '') + ')' : ''), lat, lon, status: k.status },
      ...hlFilter(kinder, 'alle').map(c => ({ art: 'hl', id: c.id, titel: c.titel, lat: c.steckbrief?.lat, lon: c.steckbrief?.lon, status: c.status, thema: hlThemaVon(c.typ), klick: () => { location.hash = hlHref(sid, c.id); } }))]);
    hlFill(kartenZeile, hlZahl(sb.lat) === null ? el('span', { class: 'small muted' }, 'Genaue Lage unbekannt – Karte zeigt die Region.') : null);
    const letzte = r.portionen[r.portionen.length - 1];
    if (hierLaeuft) hlFill(lauf, el('div', { class: 'spinner' }, { essen: 'Essen & Trinken', wohnen: 'Unterkünfte', naehe: 'Was es in der Nähe gibt', kinder: 'Was die Kinder begeistert' }[letzte?.linse] ? ({ essen: 'Essen & Trinken', wohnen: 'Unterkünfte', naehe: 'Was es in der Nähe gibt', kinder: 'Was die Kinder begeistert' }[letzte.linse] + ' wird recherchiert … (1–2 Min.)') : 'Wird recherchiert … (1–2 Min.)'));
    else if (letzte?.status === 'fehler') hlFill(lauf, el('p', { class: 'err-text' }, 'Letzte Anfrage fehlgeschlagen: ' + (letzte.fehler || 'unbekannt') + '.'));
    else hlFill(lauf);
    hlFill(tabs, kinder.length ? [el('h3', { class: 'hl2-h3' }, 'Gefunden bei ' + k.titel), hlTabs(ansicht, { alle: hlFilter(kinder, 'alle').length, will: hlFilter(kinder, 'will').length, nicht: hlFilter(kinder, 'nicht').length }, setAnsicht)] : []);
    hlFill(liste, ...hlFilter(kinder, ansicht).map(c => hlZeile(c, ctx, eltern?.titel || k.titel)));
    hlFill(unten, eltern ? el('p', {}, el('a', { href: hlHref(sid, eltern.id) }, '← Alle Highlights in ' + eltern.titel)) : null);
  }

  hlRandWischen();
  await lesen();
}
const hlKostenText = (r) => { const s = r.portionen.reduce((a, p) => a + (Number(p.kosten_usd) || 0), 0); return s ? ' · bisher ' + s.toFixed(2).replace('.', ',') + ' USD' : ''; };

// Region-Karte in der Übersicht: Wo · Warum · Highlights dort (Chips) – keine Kosten
function hlRegionKarte(k, nr, kinder, laeuft, ctx) {
  const sb = k.steckbrief || {}, href = hlHref(ctx.sid, k.id);
  const sichtbar = kinder.filter(c => c.status !== 'weg');
  const chips = kinder.length
    ? sichtbar.map(c => el('a', { class: 'hl2-hchip' + (c.status === 'gemerkt' ? ' will' : ''), href: hlHref(ctx.sid, c.id), style: '--t:' + hlThema(hlThemaVon(c.typ))[2] }, el('i', { 'aria-hidden': true }, c.status === 'gemerkt' ? '♥' : hlThema(hlThemaVon(c.typ))[1]), c.titel))
    : (sb.highlights || []).map(h => hlVorabChip(h));
  const art = el('article', { class: 'hl2-region' + (k.status === 'gemerkt' ? ' will' : '') },
    el('a', { class: 'hl2-region-kopf', href }, hlBild(k.bild, 'region', 'hl2-region-img'),
      el('div', {}, el('h3', {}, el('span', { class: 'hl2-nr' }, String(nr)), k.titel),
        el('p', { class: 'hl2-meta' }, [sb.hauptort ? '⌖ ' + sb.hauptort : null, sb.tage, sb.andrang ? 'Andrang ' + sb.andrang + '/5' : null].filter(Boolean).join(' · ')))),
    el('div', { class: 'hl2-region-text' },
      sb.wo ? el('p', { class: 'hl2-wo' }, el('b', {}, 'Wo: '), sb.wo) : null,
      el('p', { class: 'hl2-warum' }, el('b', {}, 'Warum hin: '), sb.warum || sb.moment || ''),
      hlWarnung(sb),
      el('p', { class: 'hl2-hl-titel' }, el('b', {}, 'Highlights dort'), kinder.length ? ' · ' + sichtbar.length + (kinder.length > sichtbar.length ? ' (' + (kinder.length - sichtbar.length) + ' erstmal nicht)' : '') : laeuft ? ' · werden gerade recherchiert …' : ' · Vorschau'),
      el('div', { class: 'hl2-hchips' }, chips)),
    el('div', { class: 'hl2-region-fuss' }, hlStatusKnoepfe(k, ctx, true), el('a', { class: 'hl2-oeffnen', href }, 'Region öffnen', el('span', { 'aria-hidden': true }, ' →'))));
  return art;
}
const hlVorabChip = (h) => { const t = hlHlThema(h); return el('span', { class: 'hl2-hchip vorab', style: '--t:' + hlThema(t)[2] }, el('i', { 'aria-hidden': true }, hlThema(t)[1]), hlHlName(h)); };

// Highlight-Zeile (Region/Detail): Foto · Thema/Ort · Name · Moment · WOW-Begründung · Will ich/Erstmal nicht
function hlZeile(c, ctx, ortHinweis) {
  const sb = c.steckbrief || {}, th = hlThemaVon(c.typ);
  const art = el('article', { class: 'hl2-zeile' + (c.status === 'gemerkt' ? ' will' : '') + (c.status === 'weg' ? ' nicht' : '') },
    el('a', { class: 'hl2-zeile-link', href: hlHref(ctx.sid, c.id) },
      c.bild || !['restaurant', 'unterkunft'].includes(c.typ) ? hlBild(c.bild, c.typ, 'hl2-zeile-img') : el('div', { class: 'hl2-zeile-img leer-typ', style: '--t:' + hlThema(th)[2] }, hlThema(th)[1]),
      el('div', { class: 'hl2-zeile-text' },
        el('p', { class: 'hl2-thema', style: '--t:' + hlThema(th)[2] }, hlThema(th)[1] + ' ' + hlThema(th)[0] + (sb.ort ? ' · ' + sb.ort : '')),
        el('h4', {}, c.titel),
        sb.moment ? el('p', { class: 'hl2-moment' }, sb.moment) : null,
        hlWow(sb), hlWarnung(sb),
        c.kinder ? el('p', { class: 'small muted' }, c.kinder + ' weitere Funde hier') : null)),
    hlStatusKnoepfe(c, ctx, true),
    hlLinks(c, ortHinweis, true));
  hlWisch(art, () => { if (c.status !== 'weg') hlEntscheiden(c, 'weg', ctx); });
  return art;
}
// Kurzzeile in „Will ich“/„Erstmal nicht“ der Übersicht
function hlKurzZeile(x, istRegion, ctx) {
  const th = istRegion ? null : hlThemaVon(x.typ);
  return el('div', { class: 'hl2-kurz' }, el('a', { href: hlHref(ctx.sid, x.id) },
    el('span', { class: 'hl2-kurz-t', style: th ? '--t:' + hlThema(th)[2] : '' }, istRegion ? '◍ Region' : hlThema(th)[1] + ' ' + hlThema(th)[0]), el('strong', {}, x.titel),
    !istRegion && x.moment ? el('span', { class: 'small muted' }, x.moment) : null), hlStatusKnoepfe(x, ctx, true));
}

// Zurück per Wischen vom linken Rand (Listener einmalig)
let hlRandAktiv = false;
function hlRandWischen() {
  if (hlRandAktiv) return; hlRandAktiv = true;
  let sx = null;
  main.addEventListener('touchstart', e => { sx = current.view === 'highlights' && e.touches[0].clientX < 28 ? e.touches[0].clientX : null; }, { passive: true });
  main.addEventListener('touchend', e => { if (sx !== null && e.changedTouches[0].clientX - sx > 90) history.back(); sx = null; });
}

function hlZeitDialog(v, speichern) {
  const d = el('dialog', { class: 'trip-dialog' }), f = el('input', { type: 'text', maxlength: 60, value: v.reisezeit || '', placeholder: 'z. B. Dez 2026 – Jan 2027' });
  const ok = el('button', { class: 'primary', type: 'button' }, 'Übernehmen');
  ok.onclick = async () => { ok.disabled = true; try { await speichern({ ...v, reisezeit: f.value.trim() || null }); d.close(); } catch (e) { toast(e.message, true); ok.disabled = false; } };
  d.append(el('h2', {}, 'Reisezeit'), el('p', { class: 'small muted' }, 'Nur für die Saison-Einschätzung. Leer = offen.'), f, el('div', { class: 'row' }, ok, el('button', { type: 'button', onclick: () => d.close() }, 'Abbrechen')));
  main.append(d); d.addEventListener('close', () => d.remove()); d.showModal(); f.focus();
}

// ---------- Will ich (über alle Wünsche) ----------
async function hlMerkliste() {
  setChrome('Will ich', { tab: 'highlights', back: true });
  const live = viewGuard();
  loading();
  const r = await hlCall('merkliste', {});
  if (!live()) return;
  const gruppen = new Map();
  for (const k of r.gemerkt) { const g = k.pfad.length > 1 ? k.pfad[0].titel : k.wunsch; if (!gruppen.has(g)) gruppen.set(g, []); gruppen.get(g).push(k); }
  hlFill(main,
    el('section', { class: 'hl-merk-kopf' }, el('p', { class: 'eyebrow' }, 'HIGHLIGHTS'), el('h2', {}, '♥ Will ich'), el('p', { class: 'muted' }, r.gemerkt.length + ' markiert · nach Region')),
    ...(r.gemerkt.length ? [...gruppen].map(([g, ks]) => el('section', { class: 'hl-merk-gruppe' }, el('h3', {}, g + ' · ' + ks.length),
      el('div', { class: 'hl-merk-liste' }, ks.map(k => el('a', { class: 'hl-merk-row', href: hlHref(k.suche_id, k.id) }, hlBild(k.bild, k.typ, 'hl-merk-img'),
        el('div', {}, el('strong', {}, k.titel), el('span', { class: 'small muted' }, k.pfad.slice(0, -1).map(p => p.titel).join(' › ') || k.wunsch),
          el('span', { class: 'small' }, [k.steckbrief?.ort, k.steckbrief?.zeit].filter(Boolean).join(' · ')))))))) : [el('p', { class: 'muted' }, 'Noch nichts mit ♥ markiert. ', el('a', { href: '#/highlights' }, 'Zu den Highlights →'))]));
}
