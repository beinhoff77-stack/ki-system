/* Reisen › Highlights V2 (Werkstatt #154): Karte zuerst → Regionen mit fertigen Highlights → Detail → „Hier weitersuchen“.
   Server: Edge Function „highlights“ (api.highlights_*). Kosten entstehen nur nach Klick: ein Wunsch holt die Regionen und danach automatisch
   die Highlights je Region; tiefer wird nur auf Ansage gesucht („Hier weitersuchen“, Frage).
   Nichts wird automatisch ausgeschlossen: „Raus“ verschiebt nur in eine eigene Ansicht und ist jederzeit zurückholbar.
   W158: Entscheidung Muss (◆) / Vielleicht (♡, intern 'gemerkt') / Raus (✕, intern 'weg'); „Erlebt“ (✓) ist ein eigener Haken.
   „Ich bin hier“ nutzt den Standort nur im Gerät (nächster bekannter Punkt) – er wird nicht gesendet. */
'use strict';

const hlApi = () => API.replace(/app-api$/, 'highlights'); // API stammt aus app.js (lädt danach)
const HL_FAMILIE = [{ k: 'E', alter: 99 }, { k: 'E', alter: 99 }, { k: '13', alter: 13 }, { k: '11', alter: 11 }];
const HL_TYP = { region: ['Region', '◍'], ort: ['Ort', '⌖'], stadt: ['Stadt', '▦'], viertel: ['Viertel', '▤'], tauchen: ['Tauchen', '≈'], tiere: ['Tiere', '❦'], natur: ['Natur', '▲'], tempel: ['Tempel', '⛩'], altstadt: ['Altstadt', '⌂'], museum: ['Museum', '▥'], restaurant: ['Restaurant', '◐'], unterkunft: ['Unterkunft', '⌂'], erlebnis: ['Erlebnis', '✦'] };
// Themen: Farbe + Zeichen für Chips und Kartenpunkte
const HL_THEMA = { tauchen: ['Meer & Tauchen', '≈', '#2a6f97'], tiere: ['Tiere', '❦', '#8a6420'], natur: ['Natur & Wandern', '▲', '#3f7d3a'], kultur: ['Kultur', '⌂', '#7b4b94'], essen: ['Essen & Trinken', '◐', '#c0662b'], wohnen: ['Wohnen', '⌂', '#1f8585'], ort: ['Ort', '⌖', '#5a6878'], erlebnis: ['Erlebnis', '✦', '#a8801a'] };
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
  const r = await fetch(mitRegion(hlApi() + '/aktion'), { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + (store.token || '') }, body: JSON.stringify({ aktion: aktionName, daten }) });
  let j; try { j = await r.json(); } catch { j = { ok: false, fehler: 'Keine Antwort (' + r.status + ')' }; }
  if (r.status === 401) { store.token = null; route('login'); throw new Error('Nicht angemeldet'); }
  if (!j.ok) throw new Error(j.fehler || 'Anfrage fehlgeschlagen');
  return j.ergebnis;
}
const hlLese = (k, fb = null) => { try { return JSON.parse(localStorage.getItem(k)) ?? fb; } catch { return fb; } };
const hlSchreibe = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* privat */ } };
const hlHref = (sid, kid) => '#/highlights/' + sid + (kid ? '/' + kid : '');
const hlBlockHref = (sid, b) => '#/highlights/' + sid + '/b/' + encodeURIComponent(b);
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
  const teile = String(arg || '').split('/');
  const [sid, kid] = teile.map(x => (/^\d+$/.test(x) ? Number(x) : null));
  if (sid && teile[1] === 'b' && teile[2]) return hlEbene(sid, null, decodeURIComponent(teile[2])); // W160: Block-Ebene
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
  const form = el('form', { class: 'hl-wish hl-wish-neu' },
    el('div', { class: 'hl-wish-row' }, wunsch, hlDiktat(wunsch)),
    el('div', { class: 'hl-wish-opts' }, el('label', {}, 'Reisezeit', zeit), el('label', {}, 'Andrang', andrang)),
    el('p', { class: 'small muted' }, 'Vorlieben sortieren nur – nichts wird ausgeschlossen. Ändern geht jederzeit.'),
    el('div', { class: 'row' }, los), status);
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
  // W157: Startseite = eure Reisen (weitermachen), der neue Wunsch ist nur noch ein zugeklappter Knopf
  const neu = el('details', { class: 'hl-neu' }, el('summary', {}, el('span', { 'aria-hidden': true }, '+'), ' Neuer Wunsch'), form);
  neu.addEventListener('toggle', () => { if (neu.open) wunsch.focus(); });
  const liste = el('div', { class: 'hl-reisen' }, el('div', { class: 'spinner' }, 'Lade …'));
  const weiter = hlLese('hl_last');
  hlFill(main, el('div', { class: 'hl-start-kopf' }, el('h2', {}, 'Eure Reisen'),
      el('a', { class: 'hl-start-merk', href: '#/highlights/merk' }, '◆ Meine Auswahl')),
    liste, neu);
  try {
    const r = await hlCall('lesen', {});
    if (!live()) return;
    if (!r.suchen.length) { neu.open = true; hlFill(liste, el('p', { class: 'muted' }, 'Noch kein Wunsch. Leg unten los, worauf ihr Lust habt.')); return; }
    hlFill(liste, ...r.suchen.map((s, i) => hlReiseKarte(s, weiter && weiter.sid === s.id ? weiter : null, i === 0)));
    // Must-Sees der obersten Reise nachladen (landet zugleich im Zwischenspeicher für die Übersicht)
    const erste = r.suchen[0];
    const daten = HL_CACHE.get(erste.id + '_0') || await hlCall('lesen', { suche_id: erste.id, mit_weg: true }).catch(() => null);
    if (!daten || !live()) return;
    HL_CACHE.set(erste.id + '_0', daten);
    const ziel = liste.querySelector('[data-must="' + erste.id + '"]');
    if (ziel) hlFill(ziel, hlMustSee(daten, erste.id));
  } catch (e) { if (live()) hlFill(liste, el('p', { class: 'err-text' }, e.message)); }
}
// Reise-Karte auf der Startseite: Foto, Wunsch, Stand, „Weiter bei …“ und Platz für die Must-Sees
function hlReiseKarte(s, weiter, gross) {
  return el('article', { class: 'hl-reise' + (gross ? ' gross' : '') },
    el('a', { class: 'hl-reise-link', href: hlHref(s.id) }, hlBild(s.bild, 'region', 'hl-reise-img'),
      el('div', { class: 'hl-reise-text' }, el('strong', {}, s.wunsch),
        el('span', { class: 'small muted' }, s.vorschlaege + ' Regionen & Highlights · ausgewählt ' + s.gemerkt))),
    gross ? el('div', { 'data-must': s.id }) : null,
    weiter && weiter.kid ? el('a', { class: 'hl-reise-weiter', href: hlHref(weiter.sid, weiter.kid) }, 'Weiter bei ', el('b', {}, weiter.titel || 'letzter Ansicht'), el('span', { 'aria-hidden': true }, ' →')) : null);
}
// W157: Must-Sees (★5) einer Reise als eigene, auffällige Leiste – Regionen und Highlights
function hlMustSee(r, sid, block) {
  const regionTitel = new Map((r.karten || []).map(k => [k.id, k.titel]));
  const alle = [...(r.unter || []).map(u => ({ id: u.id, titel: u.titel, wow: Number(u.wow), status: u.status, typ: u.typ, ort: regionTitel.get(u.parent_id) || '' })),
    ...(r.karten || []).map(k => ({ id: k.id, titel: k.titel, wow: Number(k.steckbrief?.wow), status: k.status, typ: 'region', ort: 'Region' }))];
  const top = alle.filter(x => x.wow >= 5 && x.status !== 'weg').sort((a, b) => (a.typ === 'region') - (b.typ === 'region'));
  if (!top.length) return null;
  return el('section', { class: 'hl-must', 'aria-label': 'Must-See' },
    el('p', { class: 'hl-must-titel' }, el('span', { class: 'hl-must-stern' }, '★★★★★'), block ? ' Must-See in ' + block : ' Must-See · weltweit einzigartig'),
    el('div', { class: 'hl-must-reihe' }, top.map(x => el('a', { class: 'hl-must-k' + hlKl(x.status), href: hlHref(sid, x.id) },
      el('b', {}, hlSym(x.status) + x.titel), el('span', {}, x.typ === 'region' ? '◍ Region' : hlThema(hlThemaVon(x.typ))[1] + ' ' + x.ort)))));
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
const hlWow = (sb, kompakt = false) => {
  const n = Number(sb.wow) >= 1 && Number(sb.wow) <= 5 ? Math.round(Number(sb.wow)) : null;
  if (!n && !sb.besonders) return null;
  return el('p', { class: 'hl2-wow' },
    n ? el('span', { class: 'hl2-sterne', title: 'WOW ' + n + '/5 – ' + HL_WOW[n], 'aria-label': 'WOW ' + n + ' von 5: ' + HL_WOW[n] }, '★'.repeat(n), el('span', { class: 'aus' }, '★'.repeat(5 - n))) : null,
    n && !kompakt ? el('span', { class: 'hl2-wow-stufe' }, HL_WOW[n]) : null,
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
    knopf(maps, '📍', klein ? 'Maps' : 'Google Maps', 'In Google Maps öffnen'),
    wiki ? knopf(wiki, '📖', klein ? 'Wiki' : 'Wikipedia', 'Wikipedia: ' + sb.wiki_titel) : null,
    q && host ? knopf(q.url, '🌐', klein ? 'Mehr' : 'Mehr lesen · ' + host, host + (q.abgerufen ? ' (von der Recherche abgerufen)' : '')) : null);
}

// W156: kurze Ortsangabe für Listen („ca. 1,5 Std. ab Kingscote“ statt Parkname · Ort · Fahrzeit)
const hlOrtKurz = (ort) => {
  const teile = String(ort || '').split('·').map(x => x.trim()).filter(Boolean);
  if (!teile.length) return '';
  const fahrt = teile.find(x => /\d\s*(Std|Min|h\b)|Stunde|Minute/i.test(x));
  const t = fahrt || teile[0];
  return t.length > 40 ? t.slice(0, 38).replace(/\s+\S*$/, '') + ' …' : t;
};
// Saison-Text wird serverseitig bei 80 Zeichen gekappt – sauber am Satz- oder Wortende enden
const hlSaisonText = (t) => {
  t = String(t || '').trim();
  if (t.length < 78) return t;
  const s = Math.max(t.lastIndexOf('. '), t.lastIndexOf('; '), t.lastIndexOf(', '));
  return s > 25 ? t.slice(0, s) + ' …' : t.replace(/\s+\S*$/, '') + ' …';
};
// Themen-Zähler einer Region (≈3 ▲4 ❦2)
function hlZaehler(kinder) {
  const n = {};
  for (const c of kinder) if (c.status !== 'weg') { const t = hlThemaVon(c.typ); n[t] = (n[t] || 0) + 1; }
  const themen = Object.keys(HL_THEMA).filter(t => n[t]);
  return themen.length ? el('p', { class: 'hl2-zaehler' }, themen.map(t => el('span', { style: '--t:' + hlThema(t)[2], title: hlThema(t)[0] + ': ' + n[t] }, el('i', { 'aria-hidden': true }, hlThema(t)[1]), String(n[t])))) : null;
}
const hlSterne = (wow) => { const n = Number(wow) >= 1 && Number(wow) <= 5 ? Math.round(Number(wow)) : null;
  return n ? el('span', { class: 'hl2-sterne', title: 'WOW ' + n + '/5 – ' + HL_WOW[n], 'aria-label': 'WOW ' + n + ' von 5' }, '★'.repeat(n), el('span', { class: 'aus' }, '★'.repeat(5 - n))) : null; };

// W158: Muss / Vielleicht / Raus – nochmal tippen setzt zurück auf offen; „Erlebt“ ist ein eigener Haken
const HL_STATUS = { muss: ['◆', 'Muss'], gemerkt: ['♡', 'Vielleicht'], weg: ['✕', 'Raus'] };
const hlKl = (st) => (st === 'muss' ? ' will muss' : st === 'gemerkt' ? ' will vielleicht' : '');
const hlSym = (st) => (st === 'muss' ? '◆ ' : st === 'gemerkt' ? '♡ ' : '');
function hlStatusKnoepfe(k, ctx, klein = false) {
  const knopf = (st) => {
    const an = k.status === st, [sym, text] = HL_STATUS[st];
    const b = el('button', { type: 'button', class: 'hl2-st hl2-st-' + st + (an ? ' an' : ''), 'aria-pressed': an, 'aria-label': text + ': ' + k.titel, title: text }, klein ? sym : sym + ' ' + text);
    b.onclick = e => { e.preventDefault(); e.stopPropagation(); hlEntscheiden(k, an ? 'offen' : st, ctx); };
    return b;
  };
  return el('div', { class: 'hl2-status' + (klein ? ' klein' : '') }, knopf('muss'), knopf('gemerkt'), knopf('weg'));
}
function hlErlebtKnopf(k, ctx) {
  const b = el('button', { type: 'button', class: 'hl2-erlebt' + (k.erlebt_am ? ' an' : ''), 'aria-pressed': !!k.erlebt_am },
    k.erlebt_am ? '✓ Erlebt am ' + fmtDate(k.erlebt_am) : '✓ Als erlebt abhaken');
  b.onclick = async () => { b.disabled = true; try { await hlCall('entscheiden', { knoten_id: k.id, erlebt: !k.erlebt_am }); toast(k.erlebt_am ? 'Haken entfernt.' : '✓ Erlebt'); await ctx.neu(); } catch (e) { toast(e.message, true); b.disabled = false; } };
  return b;
}
async function hlEntscheiden(k, status, ctx) {
  const vorher = k.status;
  try {
    await hlCall('entscheiden', { knoten_id: k.id, status });
    if (status === 'weg') hlRueckgaengig(k, vorher, ctx); else toast(status === 'offen' ? 'Zurück auf offen.' : HL_STATUS[status].join(' '));
    await ctx.neu();
  } catch (e) { toast(e.message, true); }
}
function hlRueckgaengig(k, vorher, ctx) {
  const t = $('#toast');
  t.replaceChildren('„' + k.titel + '“ → Raus. ', el('button', { type: 'button', class: 'link', onclick: async () => { t.hidden = true; await hlCall('entscheiden', { knoten_id: k.id, status: vorher }).catch(e => toast(e.message, true)); await ctx.neu(); } }, 'Rückgängig'));
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

// Ansichten: Alle (ohne „Raus“) · Muss · Vielleicht · Raus
const hlFilter = (liste, ansicht) => liste.filter(x => (ansicht === 'muss' ? x.status === 'muss' : ansicht === 'will' ? x.status === 'gemerkt' : ansicht === 'nicht' ? x.status === 'weg' : x.status !== 'weg'));
const hlZahlen = (liste, alleZahl) => ({ alle: alleZahl ?? hlFilter(liste, 'alle').length, muss: hlFilter(liste, 'muss').length, will: hlFilter(liste, 'will').length, nicht: hlFilter(liste, 'nicht').length });
function hlTabs(aktiv, zahlen, wahl) {
  return el('div', { class: 'hl2-tabs', role: 'tablist', 'aria-label': 'Ansicht' },
    [['alle', 'Alle', zahlen.alle], ['muss', '◆ Muss', zahlen.muss], ['will', '♡ Vielleicht', zahlen.will], ['nicht', '✕ Raus', zahlen.nicht]].map(([k, l, n]) =>
      el('button', { type: 'button', role: 'tab', 'aria-selected': aktiv === k, class: 'hl2-tab' + (aktiv === k ? ' an' : ''), onclick: () => wahl(k) }, l, ' ', el('span', { class: 'hl2-n' }, String(n)))));
}

// Themen-Filter (W155b): nur Themen, die es hier gibt, mit Anzahl; gilt für Liste und Karte
function hlThemenLeiste(eintraege, aktiv, wahl) {
  const n = {};
  for (const x of eintraege) if (x.status !== 'weg') { const t = hlThemaVon(x.typ); n[t] = (n[t] || 0) + 1; }
  const themen = Object.keys(HL_THEMA).filter(t => n[t]);
  if (themen.length < 2 && !aktiv) return null;
  const knopf = (t, text) => el('button', { type: 'button', class: 'hl2-thema-chip' + ((aktiv || '') === t ? ' an' : ''), 'aria-pressed': (aktiv || '') === t, style: t ? '--t:' + hlThema(t)[2] : '', onclick: () => wahl(aktiv === t ? '' : t) }, text);
  return el('div', { class: 'hl2-themen', role: 'group', 'aria-label': 'Nach Thema filtern' },
    knopf('', 'Alle Themen'), themen.map(t => knopf(t, [el('i', { 'aria-hidden': true }, hlThema(t)[1]), ' ', hlThema(t)[0], ' ', el('span', { class: 'hl2-n' }, String(n[t]))])));
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
    const ll = [], marker = [];
    // W156: Punkte mit (fast) gleicher Lage leicht auffächern, damit keine Nummer verdeckt ist
    const gruppen = new Map();
    for (const p of punkte) { const lat = hlZahl(p.lat), lon = hlZahl(p.lon); if (lat === null || lon === null) continue;
      const g = lat.toFixed(3) + ',' + lon.toFixed(3); if (!gruppen.has(g)) gruppen.set(g, []); gruppen.get(g).push(p); }
    const lage = new Map();
    for (const liste of gruppen.values()) liste.forEach((p, i) => { const lat = hlZahl(p.lat), lon = hlZahl(p.lon);
      if (liste.length < 2 || p.art === 'ziel') { lage.set(p, [lat, lon]); return; }
      const w = (2 * Math.PI * i) / liste.length, r = 0.0016; lage.set(p, [lat + r * Math.sin(w), lon + r * Math.cos(w) / Math.cos(lat * Math.PI / 180)]); });
    // Reihenfolge = Ebene: Basis-Stern ganz unten, dann Punkte, Regionen, das gewählte Highlight oben
    const rang = (p) => ({ ort: 0, hl: 1, region: 2, ziel: 3 })[p.art] ?? 1;
    for (const p of [...punkte].filter(p => lage.has(p)).sort((a, b) => rang(a) - rang(b))) {
      const pos = lage.get(p); ll.push(pos);
      let m;
      if (p.art === 'ziel') {
        const farbe = hlThema(p.thema)[2];
        m = L.marker(pos, { title: p.titel, alt: p.titel, keyboard: true, zIndexOffset: 1000,
          icon: L.divIcon({ className: 'hl2-pin ziel' + hlKl(p.status), html: '<span style="background:' + farbe + '">' + hlThema(p.thema)[1] + '</span>', iconSize: [36, 36], iconAnchor: [18, 18] }) });
      } else if (p.art === 'region' || p.art === 'ort') {
        m = L.marker(pos, { title: p.titel, alt: p.titel, keyboard: true, zIndexOffset: p.art === 'ort' ? -500 : 500,
          icon: L.divIcon({ className: 'hl2-pin' + (p.art === 'ort' ? ' ort' : '') + (p.klasse || '') + hlKl(p.status) + (p.status === 'weg' ? ' nicht' : ''), html: el('span', {}, p.nr ? String(p.nr) : p.klasse ? '' : '★'), iconSize: p.art === 'ort' ? [22, 22] : [30, 30], iconAnchor: p.art === 'ort' ? [11, 11] : [15, 15] }) });
      } else if (p.nr) {
        // Region/Detail: Nummer im Punkt = Nummer in der Liste
        const farbe = p.status === 'weg' ? '#9aa5b1' : hlThema(p.thema)[2];
        m = L.marker(pos, { title: p.titel, alt: p.titel, keyboard: true, zIndexOffset: p.top ? 400 : p.status === 'muss' ? 350 : p.status === 'gemerkt' ? 300 : 0,
          icon: L.divIcon({ className: 'hl2-pin hl' + hlKl(p.status) + (p.erlebt ? ' erlebt' : '') + (p.top ? ' top' : '') + (p.blass ? ' blass' : ''), html: '<span style="background:' + farbe + '">' + p.nr + '</span>', iconSize: [26, 26], iconAnchor: [13, 13] }) });
      } else {
        const farbe = p.status === 'weg' ? '#9aa5b1' : hlThema(p.thema)[2];
        m = L.circleMarker(pos, { radius: p.top || p.status === 'muss' ? 10 : p.status === 'gemerkt' ? 8.5 : 6.5, color: p.status === 'muss' ? '#c0392b' : p.status === 'gemerkt' ? '#2a6f97' : p.top ? '#e0a800' : '#fff', weight: p.top || hlKl(p.status) ? 3 : 2, fillColor: p.erlebt ? '#9aa5b1' : farbe, fillOpacity: p.status === 'weg' || p.erlebt ? 0.45 : 0.95 });
        if (p.top) setTimeout(() => m.bringToFront?.(), 0); // ★5 über die anderen Punkte
      }
      m.bindTooltip(el('span', {}, hlSym(p.status) + p.titel + (p.erlebt ? ' ✓' : '')), { direction: 'top' });
      marker.push({ m, pos });
      // Tipp auf einen Punkt in einem Gedränge: erst hineinzoomen, dann öffnen
      m.on('click', () => {
        const map = box.map, pt = map.latLngToContainerPoint(pos);
        const nah = marker.filter(o => o.m !== m && map.latLngToContainerPoint(o.pos).distanceTo(pt) < 22);
        if (nah.length && map.getZoom() < 15) { box.bewegt = true; map.fitBounds([pos, ...nah.map(o => o.pos)], { padding: [70, 70], maxZoom: Math.min(16, map.getZoom() + 4) }); return; }
        if (p.klick) p.klick();
      });
      m.addTo(box.layer);
    }
    setTimeout(() => box.map && box.map.invalidateSize(), 0);
    if (ll.length > box.anzahl && !box.bewegt) {
      // ohne Animation: schnelles Neuzeichnen (Zwischenspeicher, Filter) bricht sonst eine laufende Zoom-Animation ab (_leaflet_pos)
      if (ll.length === 1) box.map.setView(ll[0], 11, { animate: false }); else box.map.fitBounds(ll, { padding: [26, 26], maxZoom: 12, animate: false });
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
const HL_CACHE = new Map(), HL_SCROLL = new Map(), HL_OFFEN = new Map(), HL_REGION_BLOCK = new Map(); // nur im Speicher, je Sitzung
// W159: Regionen in Blöcke (Bundesstaaten) gruppieren – aus der Lage abgeleitet, Reihenfolge = eure Route (Adelaide → Roadtrip Victoria → Tasmanien, Abflug Hobart)
const HL_BLOECKE = ['Südaustralien', 'Victoria', 'Tasmanien', 'New South Wales', 'Weitere'];
function hlBlock(k) {
  const lat = hlZahl(k.steckbrief?.lat), lon = hlZahl(k.steckbrief?.lon);
  if (lat === null || lon === null) return 'Weitere';
  if (lon < 110 || lon > 155 || lat > -10 || lat < -45) return 'Weitere'; // außerhalb Australiens: kein Bundesstaat
  if (lat < -39.4 && lon > 143.4) return 'Tasmanien';
  if (lon < 141) return 'Südaustralien';
  // Grenze Victoria/New South Wales: Murray-Fluss bis zur Quelle, dann Gerade zum Cape Howe (grob, für Gruppierung genügt das)
  const grenze = [[141.0, -34.0], [142.0, -34.1], [142.3, -34.15], [143.4, -35.2], [144.6, -36.1], [146.0, -36.0], [147.0, -36.1], [148.2, -36.8], [149.98, -37.5]];
  if (lon <= 150 && lat > -39.4) {
    let gl = grenze[grenze.length - 1][1];
    for (let i = 0; i < grenze.length - 1; i++) { const [a, b] = grenze[i], [c, e] = grenze[i + 1]; if (lon >= a && lon <= c) { gl = b + (e - b) * (lon - a) / (c - a); break; } }
    if (lat < gl) return 'Victoria';
  }
  return 'New South Wales';
}
async function hlEbene(sid, kid, block = null) {
  setChrome('Highlights', { tab: 'highlights', back: true });
  const live = viewGuard();
  const ansichtKey = 'hl2_ansicht_' + sid + '_' + (kid || 0) + (block ? '_' + block : '');
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
  const weiterBox = el('div');
  hlFill(main, pfad, kopf, mitte, el('section', { class: 'hl2-map-wrap' }, karte.canvas, kartenZeile), weiterBox, chatBox, lauf, tabs, liste, unten);
  // W156: im Detail per Wischen über den Kopf zum vorigen/nächsten Highlight der Region
  let wischZiel = { vor: null, zurueck: null };
  { let x0 = null, y0 = 0;
    kopf.addEventListener('touchstart', e => { const t = e.touches[0]; x0 = t.clientX > 28 ? t.clientX : null; y0 = t.clientY; }, { passive: true });
    kopf.addEventListener('touchend', e => { if (x0 === null) return; const t = e.changedTouches[0], dx = t.clientX - x0, dy = t.clientY - y0; x0 = null;
      if (Math.abs(dx) > 80 && Math.abs(dy) < 50 && !e.target.closest('a,button,input,summary,.leaflet-container')) { const z = dx < 0 ? wischZiel.vor : wischZiel.zurueck; if (z) location.hash = z; } }); }
  if (!HL_OFFEN.has(sid)) HL_OFFEN.set(sid, new Set());
  const offen = HL_OFFEN.get(sid);
  let sortierung = hlLese('hl2_sort', 'route') === 'wow' ? 'wow' : 'route';
  const setSortierung = (x) => { sortierung = x; hlSchreibe('hl2_sort', x); lesen(); };
  const ctx = { sid, alter: null, neu: () => lesen() };
  const setAnsicht = (a) => { ansicht = a; sessionStorage.setItem(ansichtKey, a); lesen(); };
  const themaKey = 'hl2_thema_' + sid;
  let thema = (() => { try { return sessionStorage.getItem(themaKey) || ''; } catch { return ''; } })();
  const setThema = (t) => { thema = t; try { sessionStorage.setItem(themaKey, t); } catch { /* privat */ } HL_SCROLL.delete(cacheKey); lesen(); };
  const passt = (x) => !thema || hlThemaVon(x.typ) === thema;

  // Sofortige Rückmeldung (W155b): Knöpfe sperren, Hinweis direkt am Knopf und oben, Toast beim Start
  async function portion(art, extra = {}) {
    const hinweis = el('div', { class: 'spinner hl2-am-knopf' }, 'Wird angefragt …');
    hlFill(lauf, el('div', { class: 'spinner' }, 'Wird angefragt …'));
    for (const b of [...unten.querySelectorAll('button'), ...mitte.querySelectorAll('button')]) b.disabled = true;
    (unten.querySelector('.hl-mehr') || mitte.querySelector('.hl2-weiter-knoepfe'))?.after(hinweis);
    try {
      await hlCall('portion', { suche_id: sid, parent_id: kid, art, modus: hlModus(), ...extra });
      toast(hlModus() === 'chat' ? 'Auftrag liegt für Claude/ChatGPT bereit.' : 'Recherche läuft – dauert 1–3 Min., die Seite aktualisiert sich selbst.');
      await lesen();
    } catch (e) { hinweis.remove(); hlFill(lauf, el('p', { class: 'hl-ende' }, e.message)); await lesen(); }
  }
  function frageForm(platzhalter, vorsatz = '') {
    const frage = el('input', { type: 'text', maxlength: 400, placeholder: platzhalter });
    const f = el('form', { class: 'hl-frage-form' }, frage, hlDiktat(frage), el('button', { type: 'submit' }, 'Fragen'));
    f.onsubmit = e => { e.preventDefault(); if (frage.value.trim().length >= 3) portion('frage', { text: vorsatz + frage.value.trim() }); };
    return f;
  }

  // Zurück/Vor (W155b): letzter Stand sofort aus dem Zwischenspeicher zeigen, Scrollposition wiederherstellen, dann still aktualisieren
  const cacheKey = sid + '_' + (kid || 0) + (block ? '_' + block : '');
  let ersterLauf = true;
  const scrollMerken = () => HL_SCROLL.set(cacheKey, window.scrollY);
  window.addEventListener('scroll', scrollMerken, { passive: true });
  const altDispose = disposeSuche;
  disposeSuche = () => { window.removeEventListener('scroll', scrollMerken); altDispose(); };
  async function lesen() {
    clearTimeout(timer);
    if (ersterLauf && HL_CACHE.has(cacheKey)) {
      ersterLauf = false;
      zeigen(HL_CACHE.get(cacheKey));
      const y = HL_SCROLL.get(cacheKey);
      if (y) requestAnimationFrame(() => window.scrollTo(0, y));
      clearTimeout(timer);
      return lesen();
    }
    ersterLauf = false;
    let r;
    try { r = await hlCall('lesen', { suche_id: sid, knoten_id: kid, mit_weg: true }); }
    catch (e) { if (live()) hlFill(lauf, el('p', { class: 'err-text' }, e.message)); return; }
    if (!live()) return;
    HL_CACHE.set(cacheKey, r);
    const y = window.scrollY;
    zeigen(r);
    if (Math.abs(window.scrollY - y) > 2) window.scrollTo(0, y);
  }
  function zeigen(r) {
    const v = r.suche.vorlieben || {};
    ctx.alter = Array.isArray(v.familie_alter) ? v.familie_alter : null;
    const titel = r.knoten ? r.knoten.titel : block || r.suche.wunsch;
    hlSchreibe('hl_last', { sid, kid, titel });
    // Block der aktuellen Region (für den Pfad): aus der Region selbst, sonst aus der Übersicht gemerkt
    const regionId = r.pfad.length ? r.pfad[0].id : null;
    const blockHier = block || (r.knoten && r.knoten.typ === 'region' && !r.knoten.parent_id ? hlBlock(r.knoten) : HL_REGION_BLOCK.get(regionId) || null);
    const mitBlock = blockHier && HL_REGION_BLOCK.get('mehr_' + sid) !== false;
    setChrome(hlKurz(titel), { tab: 'highlights', back: true });
    const sep = () => el('span', { 'aria-hidden': true }, '›');
    // W156: Pfad nur mit den Ebenen darüber – der aktuelle Titel steht schon oben und als Überschrift
    hlFill(pfad, el('a', { href: '#/highlights' }, 'Highlights'),
      ...(r.pfad.length || block ? [sep(), el('a', { href: hlHref(sid) }, hlKurz(r.suche.wunsch))] : []),
      ...(mitBlock && !block ? [sep(), el('a', { href: hlBlockHref(sid, blockHier) }, blockHier)] : []),
      ...r.pfad.slice(0, -1).flatMap(p => [sep(), el('a', { href: hlHref(sid, p.id) }, hlKurz(p.titel))]));
    hlFill(weiterBox);
    wischZiel = { vor: null, zurueck: null };
    const laufend = (r.laufend || []).map(x => (x === null ? 0 : Number(x)));
    if (!r.knoten) uebersicht(r, v, laufend, block);
    else if (r.knoten.typ === 'region') region(r, laufend);
    else detail(r, laufend);
    const chatHier = (r.chat_offen || []).filter(a => (a.parent_id ?? null) === (kid ?? null));
    hlFill(chatBox, chatHier.length ? hlChatKasten(chatHier) : null);
    if (laufend.length) timer = setTimeout(lesen, 5000);
    else if (chatHier.length) timer = setTimeout(lesen, 15000);
  }

  // ----- Übersicht: Karte + Regionen mit ihren Highlights -----
  // W160: Ebene „Block“ (Südaustralien / Victoria / Tasmanien …) zwischen Wunsch und Region.
  // Wunsch mit mehreren Blöcken → Block-Karten (Ansicht „Alle“); Block → nur dessen Regionen, Karte und Must-Sees.
  function uebersicht(r, v, laufend, block) {
    const regionenAlle = [...r.karten].sort((a, b) => HL_BLOECKE.indexOf(hlBlock(a)) - HL_BLOECKE.indexOf(hlBlock(b)));
    for (const k of regionenAlle) HL_REGION_BLOCK.set(k.id, hlBlock(k));
    const blockListe = HL_BLOECKE.filter(b => regionenAlle.some(k => hlBlock(k) === b));
    HL_REGION_BLOCK.set('mehr_' + sid, blockListe.length > 1);
    const blockAnsicht = !block && blockListe.length > 1;
    const regionen = block ? regionenAlle.filter(k => hlBlock(k) === block) : regionenAlle, nr = new Map(regionen.map((k, i) => [k.id, i + 1]));
    const unterVon = new Map(regionen.map(k => [k.id, r.unter.filter(u => u.parent_id === k.id)]));
    const unterHier = regionen.flatMap(k => unterVon.get(k.id));
    const fertige = r.portionen.filter(p => p.status === 'fertig'), letzte = r.portionen[r.portionen.length - 1];
    const fazit = fertige.length ? fertige[0].fazit : null;
    // Vorlieben (änderbar, sortieren nur)
    const andr = el('button', { type: 'button', class: 'hl-chip pref' }, 'Andrang ' + (v.andrang_max ? 'bis ' + v.andrang_max + '/5' : 'egal') + ' ✎');
    andr.onclick = async () => { const n = v.andrang_max ? (v.andrang_max % 5) + 1 : 3; await hlCall('suche_speichern', { id: sid, vorlieben: { ...v, andrang_max: n === 5 ? null : n } }).catch(e => toast(e.message, true)); toast('Gilt für die nächsten Vorschläge.'); lesen(); };
    const zeitChip = el('button', { type: 'button', class: 'hl-chip pref' }, 'Reisezeit ' + (v.reisezeit || 'offen') + ' ✎');
    zeitChip.onclick = () => hlZeitDialog(v, async neu => { await hlCall('suche_speichern', { id: sid, vorlieben: neu }); lesen(); });
    if (block) hlFill(kopf, el('p', { class: 'eyebrow' }, hlKurz(r.suche.wunsch).toUpperCase()), el('h2', {}, block),
      el('p', { class: 'hl2-meta' }, regionen.length + (regionen.length === 1 ? ' Region' : ' Regionen') + ' · ' + unterHier.filter(u => u.status !== 'weg').length + ' Highlights'),
      hlMustSee({ karten: regionen, unter: unterHier }, sid, block));
    else hlFill(kopf, el('p', { class: 'eyebrow' }, 'EUER WUNSCH'), el('h2', {}, r.suche.wunsch), el('div', { class: 'hl-chips' }, andr, zeitChip), blockAnsicht ? null : hlMustSee(r, sid), blockAnsicht ? null : hlFazit(fazit)); // bei Blöcken: Must-Sees und Wege je Block
    hlFill(mitte);
    // Karte: Regionen als Nummern, Highlights als Punkte (umschaltbar)
    const mitPunkten = hlLese('hl2_punkte', true);
    const punkte = [];
    for (const k of regionen) {
      const sb = k.steckbrief || {};
      punkte.push({ art: 'region', id: k.id, nr: blockAnsicht ? '' : nr.get(k.id), klasse: blockAnsicht ? ' blk blk-' + blockListe.indexOf(hlBlock(k)) : '', titel: (blockAnsicht ? hlBlock(k) + ' · ' : '') + k.titel, lat: sb.lat, lon: sb.lon, status: k.status, klick: () => { location.hash = blockAnsicht ? hlBlockHref(sid, hlBlock(k)) : hlHref(sid, k.id); } });
      if (mitPunkten && !blockAnsicht) for (const u of unterVon.get(k.id).filter(passt)) punkte.push({ art: 'hl', id: u.id, erlebt: !!u.erlebt_am, top: Number(u.wow) >= 5, titel: (Number(u.wow) >= 5 ? '★ ' : '') + u.titel + ' · ' + k.titel, lat: u.lat, lon: u.lon, status: u.status, thema: hlThemaVon(u.typ), klick: () => { location.hash = hlHref(sid, u.id); } });
    }
    karte.zeichne(punkte.filter(p => p.status !== 'weg' || ansicht === 'nicht'));
    const schalter = el('input', { type: 'checkbox' }); schalter.checked = mitPunkten;
    schalter.onchange = () => { hlSchreibe('hl2_punkte', schalter.checked); lesen(); };
    const alle = [...regionen.map(k => ({ ...k, steckbrief: k.steckbrief })), ...unterHier];
    hlFill(kartenZeile, blockAnsicht ? el('span', { class: 'hl2-legende' }, blockListe.map((b, i) => el('span', {}, el('i', { class: 'blk-' + i }), b))) : el('label', { class: 'hl2-schalter' }, schalter, ' Highlights auf der Karte'),
      el('button', { type: 'button', class: 'link', onclick: () => hlIchBinHier([...regionen.map(k => ({ id: k.id, titel: k.titel, lat: k.steckbrief?.lat, lon: k.steckbrief?.lon })), ...r.unter], sid) }, '📍 Ich bin hier'));
    // Laufende Recherchen
    const regionenLaufen = laufend.filter(x => x && nr.has(x)).length;
    if (laufend.includes(0)) hlFill(lauf, el('div', { class: 'spinner' }, regionen.length ? 'Weitere Regionen werden recherchiert … (1–3 Min.)' : 'Die Regionen werden recherchiert … (2–4 Min., mit Websuche). Danach kommen automatisch die Highlights je Region.'));
    else if (regionenLaufen) hlFill(lauf, el('div', { class: 'spinner' }, 'Highlights für ' + regionenLaufen + (regionenLaufen === 1 ? ' Region' : ' Regionen') + ' werden recherchiert … – die Übersicht füllt sich von selbst.'));
    else if (letzte?.status === 'fehler') hlFill(lauf, el('p', { class: 'err-text' }, 'Letzte Anfrage fehlgeschlagen: ' + (letzte.fehler || 'unbekannt') + '. Du kannst es erneut versuchen.'));
    else hlFill(lauf);
    // Ansichten
    hlFill(tabs, hlTabs(ansicht, hlZahlen(alle, blockAnsicht ? blockListe.length : hlFilter(regionen, 'alle').length), setAnsicht), blockAnsicht ? null : hlThemenLeiste(unterHier, thema, setThema));
    if (ansicht === 'alle' && blockAnsicht) {
      hlFill(liste, ...blockListe.map((b, i) => hlBlockKarte(b, i, regionenAlle.filter(k => hlBlock(k) === b), r.unter, sid)));
    } else if (ansicht === 'alle') {
      const regionenSicht = hlFilter(regionen, 'alle').filter(k => !thema || unterVon.get(k.id).some(u => passt(u) && u.status !== 'weg'));
      if (sortierung === 'wow') regionenSicht.sort((a, b) => (Number(b.steckbrief?.wow) || 0) - (Number(a.steckbrief?.wow) || 0) || nr.get(a.id) - nr.get(b.id));
      const sortKnopf = (x, text) => el('button', { type: 'button', class: 'hl2-sort-k' + (sortierung === x ? ' an' : ''), 'aria-pressed': sortierung === x, onclick: () => setSortierung(x) }, text);
      hlFill(liste, el('div', { class: 'hl2-sort' }, el('span', { class: 'small muted' }, thema ? regionenSicht.length + ' Regionen mit ' + hlThema(thema)[0] + ' · ' : regionenSicht.length + ' Regionen · '),
          sortKnopf('route', 'Route'), sortKnopf('wow', '★ WOW'),
          el('button', { type: 'button', class: 'link small hl2-alle-auf', onclick: () => { const zu = regionenSicht.every(k => offen.has(k.id)); for (const k of regionenSicht) zu ? offen.delete(k.id) : offen.add(k.id); zeigen(HL_CACHE.get(cacheKey) || r); } }, regionenSicht.length && regionenSicht.every(k => offen.has(k.id)) ? 'alle zu' : 'alle auf')),
        ...regionenSicht.map(k => hlRegionKarte(k, nr.get(k.id), unterVon.get(k.id).filter(passt), laufend.includes(k.id), ctx, offen)),
        !regionen.length && !laufend.length ? el('p', { class: 'muted' }, 'Noch keine Regionen.') : null);
    } else {
      // Muss / Vielleicht / Raus: nach Region gruppiert – Regionen selbst und ihre Highlights
      const gruppen = regionen.map(k => ({ k, eintraege: [...(hlFilter([k], ansicht).length ? [k] : []), ...hlFilter(unterVon.get(k.id), ansicht)] })).filter(g => g.eintraege.length);
      hlFill(liste, ...(gruppen.length ? gruppen.map(g => el('section', { class: 'hl2-gruppe' },
        el('h3', {}, blockAnsicht ? null : el('span', { class: 'hl2-nr' }, String(nr.get(g.k.id))), el('a', { href: hlHref(sid, g.k.id) }, g.k.titel), blockAnsicht ? el('span', { class: 'small muted' }, ' · ' + hlBlock(g.k)) : null),
        g.eintraege.map(x => hlKurzZeile(x, x.id === g.k.id, ctx)))) : [el('p', { class: 'muted' }, ansicht === 'muss' ? 'Noch nichts als ◆ Muss markiert.' : ansicht === 'will' ? 'Noch nichts als ♡ Vielleicht markiert.' : 'Nichts aussortiert.')]));
    }
    hlFill(unten, hlMehrSuchen(!regionen.length || laufend.includes(0), block ? 'Mehr suchen in ' + block : 'Mehr suchen · weitere Regionen oder eine Frage',
      el('div', { class: 'hl-mehr' },
        el('button', { type: 'button', class: regionen.length ? '' : 'primary', disabled: laufend.includes(0),
          onclick: () => block ? portion('frage', { text: 'Weitere wirklich lohnende Regionen in ' + block + ' (nur ' + block + '), die noch nicht gezeigt wurden.' }) : portion(regionen.length ? 'mehr' : 'start') },
          laufend.includes(0) ? '⏳ Regionen werden gesucht … (1–3 Min.)' : block ? 'Weitere Regionen in ' + block : regionen.length ? 'Weitere Regionen suchen' : 'Regionen holen'),
        el('span', { class: 'small muted' }, regionen.length ? (hlModus() === 'chat' ? hlKostenKlein() : HL_KOSTEN_KLEIN + ' (+ Highlights je neuer Region)') : HL_KOSTEN_START)),
      block ? frageForm('Frage zu ' + block + ', z. B. „Wo sieht man Pinguine?“', 'In ' + block + ': ') : frageForm('Frage zum ganzen Wunsch, z. B. „Wo sieht man Seelöwen?“'), hlModusWahl(lesen)),
      el('p', { class: 'small muted' }, regionen.length + ' Regionen · ' + unterHier.length + ' Highlights' + (block ? '' : hlKostenText(r))));
  }

  // ----- Region: alle Highlights der Region, sofort da -----
  function region(r, laufend) {
    const k = r.knoten, sb = k.steckbrief || {}, kinderAlle = r.karten, kinder = kinderAlle.filter(passt);
    const nrVon = new Map(hlFilter(kinder, 'alle').map((c, i) => [c.id, i + 1]));
    const saison = sb.saison || {};
    hlFill(kopf, el('div', { class: 'hl2-kopf-grid' }, hlBild(k.bild, 'region', 'hl2-kopf-img'),
      el('div', { class: 'hl2-kopf-text' }, el('p', { class: 'eyebrow' }, 'REGION'), el('h2', {}, k.titel),
        el('p', { class: 'hl2-meta' }, [sb.hauptort ? 'Basis: ' + sb.hauptort : null, sb.tage, sb.andrang ? 'Andrang ' + sb.andrang + '/5 · ' + HL_ANDRANG[sb.andrang] : null].filter(Boolean).join(' · ')),
        saison.text ? el('p', { class: 'hl2-meta' }, 'Beste Zeit: ' + hlSaisonText(saison.text)) : null,
        sb.wo ? el('p', { class: 'hl2-wo' }, el('b', {}, 'Wo & Anfahrt: '), sb.wo) : null,
        el('p', { class: 'hl2-warum' }, el('b', {}, 'Warum hin: '), sb.warum || sb.moment || ''),
        hlWow(sb), hlWarnung(sb), hlLinks(k), hlStatusKnoepfe(k, ctx))));
    hlFill(mitte);
    const punkte = [{ art: 'ort', titel: (sb.hauptort || k.titel), lat: sb.lat, lon: sb.lon, status: 'offen' },
      ...hlFilter(kinder, ansicht === 'nicht' ? 'nicht' : 'alle').map(c => ({ art: 'hl', id: c.id, nr: nrVon.get(c.id), erlebt: !!c.erlebt_am, top: Number(c.steckbrief?.wow) >= 5, titel: (nrVon.get(c.id) ? nrVon.get(c.id) + ' · ' : '') + c.titel, lat: c.steckbrief?.lat, lon: c.steckbrief?.lon, status: c.status, thema: hlThemaVon(c.typ), klick: () => { location.hash = hlHref(sid, c.id); } }))];
    karte.zeichne(punkte);
    hlFill(kartenZeile, el('button', { type: 'button', class: 'link', onclick: () => hlIchBinHier(kinder.map(c => ({ id: c.id, titel: c.titel, lat: c.steckbrief?.lat, lon: c.steckbrief?.lon })), sid) }, '📍 Ich bin hier'),
      el('span', { class: 'small muted' }, '★ = Basis ' + (sb.hauptort || '')));
    const hierLaeuft = laufend.includes(k.id), letzte = r.portionen[r.portionen.length - 1];
    if (hierLaeuft) hlFill(lauf, el('div', { class: 'spinner' }, kinder.length ? 'Weitere Highlights werden recherchiert … (1–2 Min.)' : 'Die Highlights von ' + k.titel + ' werden gerade recherchiert … (1–2 Min.)'),
      !kinder.length && (sb.highlights || []).length ? el('div', { class: 'hl2-hchips' }, sb.highlights.map(h => hlVorabChip(h))) : null);
    else if (letzte?.status === 'fehler') hlFill(lauf, el('p', { class: 'err-text' }, 'Letzte Anfrage fehlgeschlagen: ' + (letzte.fehler || 'unbekannt') + '.'));
    else hlFill(lauf);
    const fazit = r.portionen.find(p => p.status === 'fertig' && p.fazit)?.fazit;
    hlFill(tabs, hlFazit(fazit), hlTabs(ansicht, hlZahlen(kinder), setAnsicht), hlThemenLeiste(kinderAlle, thema, setThema));
    const sicht = hlFilter(kinder, ansicht);
    hlFill(liste, ...(sicht.length ? sicht.map(c => hlZeile(c, ctx, k.titel, nrVon.get(c.id))) : [!hierLaeuft ? el('p', { class: 'muted' }, ansicht === 'alle' ? 'Noch keine Highlights.' : ansicht === 'muss' ? 'Noch nichts als ◆ Muss markiert.' : ansicht === 'will' ? 'Noch nichts als ♡ Vielleicht markiert.' : 'Nichts aussortiert.') : null]));
    const ende = r.portionen.some(p => p.ende);
    hlFill(unten, ende ? el('p', { class: 'hl-ende' }, 'Das waren die starken Highlights hier. Frag gezielt, wenn dir etwas fehlt.') : null,
      hlMehrSuchen(!kinderAlle.length || hierLaeuft, 'Mehr suchen · weitere Highlights oder eine Frage',
        el('div', { class: 'hl-mehr' },
          el('button', { type: 'button', class: kinderAlle.length ? '' : 'primary', disabled: hierLaeuft, onclick: () => portion(kinderAlle.length ? 'mehr' : 'start') }, hierLaeuft ? '⏳ Wird recherchiert … (1–2 Min.)' : kinderAlle.length ? 'Mehr Highlights in ' + hlKurz(k.titel) : 'Highlights recherchieren'),
          el('span', { class: 'small muted' }, hlKostenKlein())),
        frageForm('In ' + hlKurz(k.titel) + ' fragen, z. B. „Wo Seedrachen sehen?“'), hlModusWahl(lesen)),
      el('p', { class: 'small muted' }, kinderAlle.length + ' Highlights' + hlKostenText(r)));
  }

  // ----- Detail: ein Highlight + „Hier weitersuchen“ -----
  function detail(r, laufend) {
    const k = r.knoten, sb = k.steckbrief || {}, th = hlThemaVon(k.typ), kinderAlle = r.karten, kinder = kinderAlle.filter(passt), eltern = r.eltern;
    const nrVon = new Map(hlFilter(kinder, 'alle').map((c, i) => [c.id, i + 1]));
    const saison = sb.saison || {};
    const ortText = sb.ort || (eltern ? (eltern.steckbrief?.hauptort ? eltern.titel + ' · Basis ' + eltern.steckbrief.hauptort : eltern.titel) : '');
    const fakt = (label, ...wert) => el('div', {}, el('dt', {}, label), el('dd', {}, ...wert));
    const famText = hlFamilieText(sb, ctx.alter);
    const bild = k.bild || !['restaurant', 'unterkunft'].includes(k.typ) ? hlBild(k.bild, k.typ, 'hl2-kopf-img') : null;
    // Geschwister (Highlights derselben Region) für Blättern und Karte – aus dem Zwischenspeicher, sonst einmal nachladen
    const elternDaten = eltern ? HL_CACHE.get(sid + '_' + eltern.id) : null;
    if (eltern && !elternDaten && !detail.holt) {
      detail.holt = true;
      hlCall('lesen', { suche_id: sid, knoten_id: eltern.id, mit_weg: true }).then(r2 => { HL_CACHE.set(sid + '_' + eltern.id, r2); if (live() && HL_CACHE.has(cacheKey)) zeigen(HL_CACHE.get(cacheKey)); }).catch(() => {}).finally(() => { detail.holt = false; });
    }
    const geschwister = elternDaten ? hlFilter(elternDaten.karten.filter(passt), 'alle') : [];
    const gNr = new Map(geschwister.map((c, i) => [c.id, i + 1]));
    const idx = geschwister.findIndex(c => c.id === k.id);
    const vor = idx >= 0 ? geschwister[idx + 1] : null, zurueck = idx > 0 ? geschwister[idx - 1] : null;
    wischZiel = { vor: vor ? hlHref(sid, vor.id) : null, zurueck: zurueck ? hlHref(sid, zurueck.id) : null };
    const blaettern = idx >= 0 && geschwister.length > 1 ? el('nav', { class: 'hl2-blaettern', 'aria-label': 'Highlights in ' + eltern.titel },
      zurueck ? el('a', { href: hlHref(sid, zurueck.id), rel: 'prev', title: zurueck.titel }, '‹ ', el('span', {}, zurueck.titel)) : el('span'),
      el('b', {}, (idx + 1) + ' / ' + geschwister.length),
      vor ? el('a', { href: hlHref(sid, vor.id), rel: 'next', title: vor.titel }, el('span', {}, vor.titel), ' ›') : el('span')) : null;
    hlFill(kopf, blaettern, el('div', { class: 'hl2-kopf-grid' + (bild ? '' : ' ohne-bild') }, bild,
      el('div', { class: 'hl2-kopf-text' + (Number(sb.wow) >= 5 ? ' top' : '') },
        Number(sb.wow) >= 5 ? el('p', { class: 'hl2-top-band' }, '★ MUST-SEE · weltweit einzigartig') : null,
        el('p', { class: 'hl2-thema t-' + th }, hlThema(th)[1] + ' ' + hlThema(th)[0]),
        el('h2', {}, gNr.get(k.id) ? el('span', { class: 'hl2-znr', style: '--t:' + hlThema(th)[2], title: 'Nummer auf der Karte der Region' }, String(gNr.get(k.id))) : null, k.titel),
        ortText ? el('p', { class: 'hl2-ort' }, '⌖ ', ortText) : null,
        hlStatusKnoepfe(k, ctx), hlErlebtKnopf(k, ctx),
        sb.moment ? el('p', { class: 'hl2-moment' }, sb.moment) : null,
        hlWow(sb), hlWarnung(sb),
        el('dl', { class: 'hl-krit' }, fakt('Zeit', sb.zeit || '–'), fakt('Kosten für 4', sb.kosten_4 || '–', ' ', hlBeleg(sb.kosten_belegt, sb.kosten_quelle)),
          fakt('Andrang', el('b', {}, sb.andrang ? sb.andrang + '/5' : '–'), ' ', hlBeleg(sb.andrang_belegt, sb.andrang_quelle), el('small', {}, HL_ANDRANG[sb.andrang] || '')),
          fakt('Saison', el('span', { class: 'pill hl-s-' + (saison.status || 'unbekannt') }, { passt: 'passt', grenzwertig: 'grenzwertig', falsch: 'falsche Zeit', unbekannt: '?' }[saison.status || 'unbekannt']), ' ', saison.text || '')),
        famText ? el('p', { class: 'hl-familie' }, el('b', {}, 'Familie: '), famText) : null,
        hlLinks(k, eltern?.titel),
        el('details', { class: 'hl-mehrinfo' }, el('summary', {}, 'Mehr Infos'),
          sb.frage ? el('p', { class: 'hl-frage' }, el('b', {}, 'Vor dem Buchen klären: '), sb.frage, sb.pruefen?.text ? el('span', { class: 'small' }, ' · Prüfen: ', hlSicher(sb.pruefen.url) ? el('a', { href: sb.pruefen.url, target: '_blank', rel: 'noopener noreferrer' }, sb.pruefen.text) : sb.pruefen.text) : null) : null,
          (sb.fach || []).length ? el('dl', { class: 'hl-fach' }, sb.fach.map(f => el('div', {}, el('dt', {}, f.label), el('dd', {}, f.wert)))) : null,
          sb.lohnt || sb.eher_nicht ? el('div', { class: 'hl-wenn' }, sb.lohnt ? el('p', { class: 'ja' }, sb.lohnt) : null, sb.eher_nicht ? el('p', { class: 'nein' }, sb.eher_nicht) : null) : null,
          sb.tageszeit ? el('p', { class: 'small' }, el('b', {}, 'Beste Tageszeit: '), sb.tageszeit) : null,
          sb.ruhig ? el('p', { class: 'hl-ruhig' }, el('b', {}, 'Ruhiger erleben: '), sb.ruhig) : null,
          (k.quellen || []).length ? el('p', { class: 'hl-quellen small' }, 'Quellen (Stand ' + fmtDate(sb.geprueft_am) + '): ', k.quellen.filter(q => hlSicher(q.url)).map((q, i) => [i ? ' · ' : '', el('a', { href: q.url, target: '_blank', rel: 'noopener noreferrer' }, new URL(q.url).hostname.replace(/^www\./, '')), q.abgerufen ? ' ✓' : ' ○'])) : null))));
    // Hier weitersuchen
    const hierLaeuft = laufend.includes(k.id);
    hlFill(mitte);
    hlFill(weiterBox, el('section', { class: 'hl2-weiter' }, el('h3', {}, 'Hier weitersuchen'),
      el('div', { class: 'hl2-weiter-knoepfe' }, HL_WEITER.map(([linse, label]) => el('button', { type: 'button', disabled: hierLaeuft, onclick: () => portion('mehr', { linse }) }, label))),
      frageForm('Frei fragen, z. B. „Wo gibt es hier guten Fisch?“'),
      el('details', { class: 'hl2-weiter-opt' }, el('summary', { class: 'small muted' }, 'Je Suche ' + hlKostenKlein() + ' · Art der Recherche'), hlModusWahl(lesen))));
    const sbE = eltern?.steckbrief || {};
    const lat = hlZahl(sb.lat) ?? hlZahl(sbE.lat), lon = hlZahl(sb.lon) ?? hlZahl(sbE.lon);
    // Karte: dieses Highlight groß, die anderen der Region blass mit ihrer Listennummer, Funde hier mit eigener Nummer
    karte.zeichne([{ art: 'ziel', titel: k.titel + (hlZahl(sb.lat) === null ? ' (Lage ungefähr: ' + (eltern?.titel || '') + ')' : ''), lat, lon, status: k.status, thema: th },
      ...geschwister.filter(c => c.id !== k.id).map(c => ({ art: 'hl', blass: true, id: c.id, nr: gNr.get(c.id), titel: gNr.get(c.id) + ' · ' + c.titel, lat: c.steckbrief?.lat, lon: c.steckbrief?.lon, status: c.status, thema: hlThemaVon(c.typ), klick: () => { location.hash = hlHref(sid, c.id); } })),
      ...hlFilter(kinder, 'alle').map(c => ({ art: 'hl', id: c.id, nr: nrVon.get(c.id), titel: nrVon.get(c.id) + ' · ' + c.titel, lat: c.steckbrief?.lat, lon: c.steckbrief?.lon, status: c.status, thema: hlThemaVon(c.typ), klick: () => { location.hash = hlHref(sid, c.id); } }))]);
    hlFill(kartenZeile, hlZahl(sb.lat) === null ? el('span', { class: 'small muted' }, 'Genaue Lage unbekannt – Karte zeigt die Region.') : geschwister.length ? el('span', { class: 'small muted' }, 'Blass: weitere Highlights in ' + eltern.titel) : null);
    const letzte = r.portionen[r.portionen.length - 1];
    if (hierLaeuft) hlFill(lauf, el('div', { class: 'spinner' }, { essen: 'Essen & Trinken', wohnen: 'Unterkünfte', naehe: 'Was es in der Nähe gibt', kinder: 'Was die Kinder begeistert' }[letzte?.linse] ? ({ essen: 'Essen & Trinken', wohnen: 'Unterkünfte', naehe: 'Was es in der Nähe gibt', kinder: 'Was die Kinder begeistert' }[letzte.linse] + ' wird recherchiert … (1–2 Min.)') : 'Wird recherchiert … (1–2 Min.)'));
    else if (letzte?.status === 'fehler') hlFill(lauf, el('p', { class: 'err-text' }, 'Letzte Anfrage fehlgeschlagen: ' + (letzte.fehler || 'unbekannt') + '.'));
    else hlFill(lauf);
    hlFill(tabs, kinder.length ? [el('h3', { class: 'hl2-h3' }, 'Gefunden bei ' + k.titel), hlTabs(ansicht, hlZahlen(kinder), setAnsicht), hlThemenLeiste(kinderAlle, thema, setThema)] : []);
    hlFill(liste, ...hlFilter(kinder, ansicht).map(c => hlZeile(c, ctx, eltern?.titel || k.titel, nrVon.get(c.id))));
    hlFill(unten, eltern ? el('p', {}, el('a', { href: hlHref(sid, eltern.id) }, '← Alle Highlights in ' + eltern.titel)) : null);
  }

  hlRandWischen();
  await lesen();
}
// Routen-Fazit ohne Koordinaten anzeigen (die KI bekommt sie zur Reihenfolge und wiederholt sie manchmal)
const hlFazit = (t) => t ? el('p', { class: 'hl-fazit' }, String(t).replace(/\s*[([]\s*-?\d{1,3}\.\d+(\s*,\s*-?\d{1,3}\.\d+)?\s*[)\]]/g, '').replace(/\s+([,.;:])/g, '$1')) : null;
const hlKostenText = (r) => { const s = r.portionen.reduce((a, p) => a + (Number(p.kosten_usd) || 0), 0); return s ? ' · bisher ' + s.toFixed(2).replace('.', ',') + ' USD' : ''; };

// W160: Block-Karte auf der Wunsch-Ebene: Fotos der Regionen, Zahlen, Must-Sees, Regionen – antippen öffnet den Block
function hlBlockKarte(b, i, regionen, unter, sid) {
  const ids = new Set(regionen.map(k => k.id));
  const hls = unter.filter(u => ids.has(u.parent_id) && u.status !== 'weg');
  const top = hls.filter(u => Number(u.wow) >= 5), vier = hls.filter(u => Number(u.wow) === 4);
  const muss = hls.filter(u => u.status === 'muss').length + regionen.filter(k => k.status === 'muss').length;
  const viel = hls.filter(u => u.status === 'gemerkt').length + regionen.filter(k => k.status === 'gemerkt').length;
  const fotos = regionen.filter(k => k.bild).slice(0, 3);
  const zeigen = (top.length ? top : vier).slice(0, 4);
  return el('a', { class: 'hl2-blockkarte blk-rand-' + i, href: hlBlockHref(sid, b) },
    el('div', { class: 'hl2-blockkarte-fotos' }, (fotos.length ? fotos : [null]).map(k => hlBild(k?.bild, 'region', 'hl2-blockkarte-img'))),
    el('div', { class: 'hl2-blockkarte-text' },
      el('h3', {}, el('i', { class: 'blk-' + i, 'aria-hidden': true }), b, el('span', { 'aria-hidden': true }, ' →')),
      el('p', { class: 'hl2-meta' }, [regionen.length + (regionen.length === 1 ? ' Region' : ' Regionen'), hls.length + ' Highlights', muss ? '◆ ' + muss + ' Muss' : null, viel ? '♡ ' + viel : null].filter(Boolean).join(' · ')),
      hlZaehler(hls),
      zeigen.length ? el('div', { class: 'hl2-blockkarte-top' }, el('span', { class: 'hl2-sterne' }, top.length ? '★★★★★' : '★★★★'), zeigen.map(u => el('span', { class: 'hl2-blockkarte-chip' + (top.length ? ' top' : '') }, u.titel))) : null,
      el('p', { class: 'small muted hl2-blockkarte-regionen' }, regionen.map(k => k.titel).join(' · '))));
}

// Region-Karte in der Übersicht: Wo · Warum · Highlights dort (Chips) – keine Kosten
// W156: eine Zeile je Region (Foto · Nummer · Name · Sterne · Tage · Themen-Zähler), Antippen klappt Wo/Warum/Highlights auf
function hlRegionKarte(k, nr, kinder, laeuft, ctx, offen) {
  const sb = k.steckbrief || {}, href = hlHref(ctx.sid, k.id);
  const sichtbar = kinder.filter(c => c.status !== 'weg');
  const chips = kinder.length
    ? [...sichtbar].sort((a, b) => (Number(b.wow) >= 5) - (Number(a.wow) >= 5)).map(c => el('a', { class: 'hl2-hchip' + (Number(c.wow) >= 5 ? ' top' : '') + hlKl(c.status) + (c.erlebt_am ? ' erlebt' : ''), href: hlHref(ctx.sid, c.id), style: '--t:' + hlThema(hlThemaVon(c.typ))[2] }, el('i', { 'aria-hidden': true }, c.erlebt_am ? '✓' : hlKl(c.status) ? hlSym(c.status).trim() : Number(c.wow) >= 5 ? '★' : hlThema(hlThemaVon(c.typ))[1]), c.titel))
    : (sb.highlights || []).map(h => hlVorabChip(h));
  const art = el('details', { class: 'hl2-region' + (Number(sb.wow) >= 5 ? ' top' : '') + hlKl(k.status) });
  art.open = offen.has(k.id);
  art.addEventListener('toggle', () => { if (art.open) offen.add(k.id); else offen.delete(k.id); });
  art.append(el('summary', { class: 'hl2-region-zeile' }, hlBild(k.bild, 'region', 'hl2-region-img'),
      el('div', { class: 'hl2-region-info' },
        el('h3', {}, el('span', { class: 'hl2-nr' }, String(nr)), el('span', { class: 'hl2-region-name' }, k.titel), hlKl(k.status) ? el('span', { class: 'hl2-herz' + hlKl(k.status), title: HL_STATUS[k.status][1] }, HL_STATUS[k.status][0]) : null),
        el('p', { class: 'hl2-meta' }, hlSterne(sb.wow), ' ', [sb.tage, sichtbar.length ? sichtbar.length + (sichtbar.length === 1 ? ' Highlight' : ' Highlights') : laeuft ? 'wird recherchiert …' : null].filter(Boolean).join(' · ')),
        hlZaehler(kinder)),
      el('span', { class: 'hl2-auf', 'aria-hidden': true }, '›')),
    el('div', { class: 'hl2-region-text' },
      el('p', { class: 'hl2-meta' }, [sb.hauptort ? '⌖ Basis ' + sb.hauptort : null, sb.andrang ? 'Andrang ' + sb.andrang + '/5' : null].filter(Boolean).join(' · ')),
      sb.wo ? el('p', { class: 'hl2-wo' }, el('b', {}, 'Wo: '), sb.wo) : null,
      el('p', { class: 'hl2-warum' }, el('b', {}, 'Warum hin: '), sb.warum || sb.moment || ''),
      hlWarnung(sb),
      el('p', { class: 'hl2-hl-titel' }, el('b', {}, 'Highlights dort'), kinder.length ? ' · ' + sichtbar.length + (kinder.length > sichtbar.length ? ' (' + (kinder.length - sichtbar.length) + ' erstmal nicht)' : '') : laeuft ? ' · werden gerade recherchiert …' : ' · Vorschau'),
      el('div', { class: 'hl2-hchips' }, chips)),
    el('div', { class: 'hl2-region-fuss' }, hlStatusKnoepfe(k, ctx, true), el('a', { class: 'hl2-oeffnen', href }, 'Region öffnen', el('span', { 'aria-hidden': true }, ' →'))));
  return art;
}
// W156: Recherche-Knopf, Frage und Recherche-Art unten gebündelt (zugeklappt, solange es schon Ergebnisse gibt)
function hlMehrSuchen(auf, titel, ...inhalt) {
  const d = el('details', { class: 'hl2-mehr-suchen' }, el('summary', {}, '🔎 ', titel), el('div', { class: 'hl2-mehr-inhalt' }, ...inhalt));
  d.open = !!auf;
  return d;
}
const hlVorabChip = (h) => { const t = hlHlThema(h); return el('span', { class: 'hl2-hchip vorab', style: '--t:' + hlThema(t)[2] }, el('i', { 'aria-hidden': true }, hlThema(t)[1]), hlHlName(h)); };

// Highlight-Zeile (Region/Detail), W156 kompakt: Foto · Nummer + Name · Thema + kurze Lage · Sterne + Begründung (max. 3 Zeilen) · Fußzeile ◆ ♡ ✕ Links
function hlZeile(c, ctx, ortHinweis, nr) {
  const sb = c.steckbrief || {}, th = hlThemaVon(c.typ), ortK = hlOrtKurz(sb.ort);
  const top = Number(sb.wow) >= 5;
  const art = el('article', { class: 'hl2-zeile' + (top ? ' top' : '') + hlKl(c.status) + (c.erlebt_am ? ' erlebt' : '') + (c.status === 'weg' ? ' nicht' : '') },
    top ? el('p', { class: 'hl2-top-band' }, '★ MUST-SEE · weltweit einzigartig') : null,
    el('a', { class: 'hl2-zeile-link', href: hlHref(ctx.sid, c.id) },
      c.bild || !['restaurant', 'unterkunft'].includes(c.typ) ? hlBild(c.bild, c.typ, 'hl2-zeile-img') : el('div', { class: 'hl2-zeile-img leer-typ', style: '--t:' + hlThema(th)[2] }, hlThema(th)[1]),
      el('div', { class: 'hl2-zeile-text' },
        el('h4', {}, nr ? el('span', { class: 'hl2-znr', style: '--t:' + hlThema(th)[2], title: 'Nummer auf der Karte' }, String(nr)) : null, c.titel, c.erlebt_am ? el('span', { class: 'hl2-erlebt-mini', title: 'Erlebt am ' + fmtDate(c.erlebt_am) }, ' ✓ erlebt') : null),
        el('p', { class: 'hl2-thema', style: '--t:' + hlThema(th)[2] }, hlThema(th)[1] + ' ' + hlThema(th)[0] + (ortK ? ' · ' + ortK : '')),
        hlWow(sb.besonders ? sb : { ...sb, besonders: sb.moment }, true), hlWarnung(sb),
        c.kinder ? el('p', { class: 'small muted' }, c.kinder + ' weitere Funde hier') : null)),
    el('div', { class: 'hl2-zeile-fuss' }, hlStatusKnoepfe(c, ctx, true), hlLinks(c, ortHinweis, true)));
  hlWisch(art, () => { if (c.status !== 'weg') hlEntscheiden(c, 'weg', ctx); });
  return art;
}
// Kurzzeile in „Muss“/„Vielleicht“/„Raus“ der Übersicht
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

// ---------- Meine Auswahl: Muss + Vielleicht (über alle Wünsche) ----------
async function hlMerkliste() {
  setChrome('Meine Auswahl', { tab: 'highlights', back: true });
  const live = viewGuard();
  loading();
  const r = await hlCall('merkliste', {});
  if (!live()) return;
  const gruppen = new Map();
  for (const k of r.gemerkt) { const g = k.pfad.length > 1 ? k.pfad[0].titel : k.wunsch; if (!gruppen.has(g)) gruppen.set(g, []); gruppen.get(g).push(k); }
  hlFill(main,
    el('section', { class: 'hl-merk-kopf' }, el('p', { class: 'eyebrow' }, 'HIGHLIGHTS'), el('h2', {}, 'Meine Auswahl'), el('p', { class: 'muted' }, r.gemerkt.filter(k => k.status === 'muss').length + ' ◆ Muss · ' + r.gemerkt.filter(k => k.status === 'gemerkt').length + ' ♡ Vielleicht · nach Region')),
    ...(r.gemerkt.length ? [...gruppen].map(([g, ks]) => el('section', { class: 'hl-merk-gruppe' }, el('h3', {}, g + ' · ' + ks.length),
      el('div', { class: 'hl-merk-liste' }, ks.map(k => el('a', { class: 'hl-merk-row', href: hlHref(k.suche_id, k.id) }, hlBild(k.bild, k.typ, 'hl-merk-img'),
        el('div', {}, el('strong', {}, el('span', { class: 'hl-merk-st' + hlKl(k.status), title: HL_STATUS[k.status]?.[1] || '' }, hlSym(k.status)), k.titel, k.erlebt_am ? ' ✓' : ''), el('span', { class: 'small muted' }, k.pfad.slice(0, -1).map(p => p.titel).join(' › ') || k.wunsch),
          el('span', { class: 'small' }, [k.steckbrief?.ort, k.steckbrief?.zeit].filter(Boolean).join(' · ')))))))) : [el('p', { class: 'muted' }, 'Noch nichts als ◆ Muss oder ♡ Vielleicht markiert. ', el('a', { href: '#/highlights' }, 'Zu den Highlights →'))]));
}
