/* Reisen › Highlights (Werkstatt #149): vom Reisewunsch zum Spot.
   Server: Edge Function „highlights“ (api.highlights_*). Kosten entstehen nur nach Klick auf „Vorschläge holen“, „Mehr“, „Andere Richtung“, „Mehr wie das“ oder eine Frage.
   Nichts wird automatisch ausgeschlossen: Vorlieben sortieren nur, „Weg“ blendet aus und ist jederzeit zurückholbar. */
'use strict';

const hlApi = () => API.replace(/app-api$/, 'highlights'); // API stammt aus app.js (lädt danach)
const HL_FAMILIE = [{ k: 'E', alter: 99 }, { k: 'E', alter: 99 }, { k: '13', alter: 13 }, { k: '11', alter: 11 }];
const HL_TYP = { region: ['Region', '◍'], ort: ['Ort', '⌖'], stadt: ['Stadt', '▦'], viertel: ['Viertel', '▤'], tauchen: ['Tauchen', '≈'], tiere: ['Tiere', '❦'], natur: ['Natur', '▲'], tempel: ['Tempel', '⛩'], altstadt: ['Altstadt', '⌂'], museum: ['Museum', '▥'], restaurant: ['Restaurant', '◐'], unterkunft: ['Unterkunft', '⌂'], erlebnis: ['Erlebnis', '✦'] };
const HL_ANDRANG = ['', 'kaum touristisch', 'lokaler Alltag', 'bekannter Stopp', 'Busgruppen', 'Massentourismus'];
const HL_LINSEN = [['highlights', 'Highlights'], ['tauchen', 'Tauchen'], ['tiere', 'Tiere'], ['natur', 'Natur'], ['kinder', 'Mit Kindern'], ['wohnen', 'Wo wohnen'], ['essen', 'Essen'], ['kultur', 'Kultur'], ['abend', 'Abend']];
const HL_KOSTEN = 'ca. 0,10–0,30 USD · 1–2 Min.';
// Darstellung der Karten (W149, zum Aussuchen): gleiche Inhalte, sehr unterschiedliche Gestaltung
const HL_STILE = [['steckbrief', 'Steckbrief'], ['poster', 'Poster'], ['kompakt', 'Kompakt'], ['postkarte', 'Postkarte'], ['nacht', 'Nacht']];
const hlStil = () => { const s = hlLese('hl_stil', 'steckbrief'); return HL_STILE.some(x => x[0] === s) ? s : 'steckbrief'; };
let hlFly = null;            // Kopfbild-Zoom: Startposition des Kartenfotos
const hlVergleich = new Set();

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
  const wunsch = el('textarea', { id: 'hl-wunsch', rows: 2, maxlength: 500, placeholder: 'z. B. Südaustralien: Meer, Tiere, Tauchen – ruhig und besonders' });
  const zeit = el('input', { type: 'text', maxlength: 60, placeholder: 'z. B. Dez 2026 – Jan 2027' });
  const andrang = el('select', {}, el('option', { value: '' }, 'egal'), [1, 2, 3, 4].map(n => el('option', { value: n }, 'bis ' + n + '/5 · ' + HL_ANDRANG[n])));
  andrang.value = '3';
  const status = el('p', { class: 'small muted', role: 'status' }, 'Erst der Klick holt Vorschläge (' + HL_KOSTEN + ').');
  const los = el('button', { class: 'primary', type: 'submit' }, '5 Vorschläge holen');
  const form = el('form', { class: 'hl-wish' },
    el('p', { class: 'eyebrow' }, 'REISEN · HIGHLIGHTS'),
    el('h2', {}, 'Wohin zieht es euch?'),
    el('div', { class: 'hl-wish-row' }, wunsch, hlDiktat(wunsch)),
    el('div', { class: 'hl-wish-opts' }, el('label', {}, 'Reisezeit', zeit), el('label', {}, 'Andrang', andrang)),
    el('p', { class: 'small muted' }, 'Vorlieben sortieren nur – nichts wird ausgeschlossen. Ändern geht jederzeit.'),
    el('div', { class: 'row' }, los, el('a', { href: '#/highlights/merk' }, 'Merkliste →')), status);
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
    weiter ? el('a', { class: 'hl-continue', href: hlHref(weiter.sid, weiter.kid) }, el('span', { class: 'eyebrow' }, 'WEITER BEI'), el('strong', {}, weiter.titel || 'letzter Ebene'), el('span', { 'aria-hidden': true }, '→')) : null,
    el('h3', { class: 'start-theme-title' }, 'Eure Wünsche'), liste);
  try {
    const r = await hlCall('lesen', {});
    if (!live()) return;
    hlFill(liste, ...(r.suchen.length ? r.suchen.map(s => el('a', { class: 'hl-wish-card', href: hlHref(s.id) },
      hlBild(s.bild, 'region', 'hl-wish-img'),
      el('div', {}, el('strong', {}, s.wunsch), el('span', { class: 'small muted' }, s.vorschlaege + ' Vorschläge · ' + s.gemerkt + ' gemerkt')))) : [el('p', { class: 'muted' }, 'Noch kein Wunsch. Schreib oben, worauf ihr Lust habt.')]));
  } catch (e) { if (live()) hlFill(liste, el('p', { class: 'err-text' }, e.message)); }
}

// ---------- Bild ----------
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
  box.dataset.glyph = (HL_TYP[typ] || HL_TYP.erlebnis)[1];
  return box;
}

// ---------- Steckbrief ----------
const hlPunkte = (n, max = 5) => el('span', { class: 'hl-dots', 'aria-label': n ? n + ' von ' + max : 'unbekannt' }, n ? Array.from({ length: max }, (_, i) => el('i', { class: i < n ? 'an' : '' })) : '–');
const hlBeleg = (ok, url) => ok ? el('a', { class: 'hl-beleg ok', href: hlSicher(url) || '#', target: '_blank', rel: 'noopener noreferrer', title: 'Belegt: Quelle abgerufen' }, '✓') : el('span', { class: 'hl-beleg', title: 'Schätzung, keine abgerufene Quelle' }, '○');

function hlFamilie(sb, alter) {
  const fam = alter ? HL_FAMILIE.map((p, i) => (i > 1 && alter[i - 2] ? { k: String(alter[i - 2]), alter: alter[i - 2] } : p)) : HL_FAMILIE;
  const min = Number(sb.mindestalter) || 0;
  const kreise = fam.map(p => el('i', { class: 'hl-person' + (min && p.alter < min ? ' nein' : ''), title: p.alter < 99 ? p.k + ' Jahre' : 'Erwachsen' }, p.k));
  const unterschied = (min && fam.some(p => p.alter < min)) || sb.familie_hinweis;
  return el('div', { class: 'hl-fam' }, el('span', { class: 'hl-kreise' }, kreise),
    unterschied ? el('span', { class: 'hl-fam-txt' }, [min ? 'ab ' + min + ' J.' : null, sb.familie_hinweis].filter(Boolean).join(' · ')) : null);
}

function hlKarte(k, ctx) {
  const sb = k.steckbrief || {}, [typName] = HL_TYP[k.typ] || HL_TYP.erlebnis;
  const art = el('article', { class: 'hl-card' + (k.status === 'gemerkt' ? ' gemerkt' : '') + (k.status === 'weg' ? ' weg' : ''), 'data-id': k.id });
  const saison = sb.saison || {};
  const krit = el('dl', { class: 'hl-krit' },
    el('div', {}, el('dt', {}, 'WOW'), el('dd', {}, hlPunkte(sb.wow))),
    el('div', {}, el('dt', {}, 'Andrang'), el('dd', {}, el('b', {}, sb.andrang ? sb.andrang + '/5' : '–'), ' ', hlBeleg(sb.andrang_belegt, sb.andrang_quelle), el('small', {}, HL_ANDRANG[sb.andrang] || ''))),
    el('div', {}, el('dt', {}, 'Zeit'), el('dd', {}, sb.zeit || '–')),
    el('div', {}, el('dt', {}, 'Kosten für 4'), el('dd', {}, sb.kosten_4 || '–', ' ', hlBeleg(sb.kosten_belegt, sb.kosten_quelle))),
    el('div', { class: 'hl-krit-fam' }, el('dt', {}, 'Familie'), el('dd', {}, hlFamilie(sb, ctx.alter))));
  const merk = el('button', { type: 'button', class: 'hl-merk' + (k.status === 'gemerkt' ? ' an' : ''), 'aria-pressed': k.status === 'gemerkt' }, k.status === 'gemerkt' ? '♥ Gemerkt' : '♡ Merken');
  merk.onclick = () => hlEntscheiden(k, k.status === 'gemerkt' ? 'offen' : 'gemerkt', ctx);
  const weg = el('button', { type: 'button', class: 'hl-weg' }, k.status === 'weg' ? 'Zurückholen' : 'Weg');
  weg.onclick = () => hlEntscheiden(k, k.status === 'weg' ? 'offen' : 'weg', ctx);
  const vgl = el('input', { type: 'checkbox', 'aria-label': 'Vergleichen' }); vgl.checked = hlVergleich.has(k.id);
  vgl.onchange = () => { if (vgl.checked) { if (hlVergleich.size >= 3) { vgl.checked = false; toast('Höchstens 3 vergleichen.'); return; } hlVergleich.add(k.id); } else hlVergleich.delete(k.id); ctx.vergleichLeiste(); };
  const bild = k.bild || !['restaurant', 'unterkunft'].includes(k.typ) ? hlBild(k.bild, k.typ) : null;
  const tiefer = el('a', { class: 'hl-tiefer primary-link', href: hlHref(ctx.sid, k.id) }, 'Mehr dazu', el('span', { 'aria-hidden': true }, ' →'), k.kinder ? el('small', {}, ' · ' + k.kinder) : null);
  tiefer.addEventListener('click', () => { const img = bild?.querySelector('img'); if (img) hlFly = { src: img.src, rect: img.getBoundingClientRect() }; });
  art.append(...(bild ? [bild] : []),
    el('div', { class: 'hl-body' },
      el('p', { class: 'eyebrow' }, typName),
      el('h3', {}, k.titel),
      sb.moment ? el('p', { class: 'hl-moment' }, sb.moment) : null,
      sb.warnung ? el('p', { class: 'hl-warnung' }, '⚠ ', sb.warnung, ' ', hlBeleg(sb.warnung_belegt, sb.warnung_quelle)) : null,
      krit,
      el('p', { class: 'hl-saison' }, el('span', { class: 'pill hl-s-' + (saison.status || 'unbekannt') }, { passt: 'Saison passt', grenzwertig: 'Saison grenzwertig', falsch: 'Falsche Saison', unbekannt: 'Saison ?' }[saison.status || 'unbekannt']), ' ', saison.text || '', sb.tageszeit ? ' · ' + sb.tageszeit : ''),
      (sb.fach || []).length ? el('dl', { class: 'hl-fach' }, sb.fach.map(f => el('div', {}, el('dt', {}, f.label), el('dd', {}, f.wert)))) : null,
      sb.lohnt || sb.eher_nicht ? el('div', { class: 'hl-wenn' }, sb.lohnt ? el('p', { class: 'ja' }, sb.lohnt) : null, sb.eher_nicht ? el('p', { class: 'nein' }, sb.eher_nicht) : null) : null,
      sb.frage ? el('p', { class: 'hl-frage' }, el('b', {}, 'Entscheidende Frage: '), sb.frage, sb.pruefen?.text ? el('span', { class: 'small' }, ' · Prüfen: ', hlSicher(sb.pruefen.url) ? el('a', { href: sb.pruefen.url, target: '_blank', rel: 'noopener noreferrer' }, sb.pruefen.text) : sb.pruefen.text) : null) : null,
      sb.ruhig ? el('p', { class: 'hl-ruhig' }, el('b', {}, 'Ruhiger erleben: '), sb.ruhig) : null,
      (k.quellen || []).length ? el('details', { class: 'hl-quellen' }, el('summary', {}, 'Quellen (' + k.quellen.length + ') · Stand ' + fmtDate(sb.geprueft_am)),
        el('ul', {}, k.quellen.map(q => hlSicher(q.url) ? el('li', {}, el('a', { href: q.url, target: '_blank', rel: 'noopener noreferrer' }, new URL(q.url).hostname.replace(/^www\./, '')), q.abgerufen ? ' ✓' : ' ○') : null))) : null,
      el('div', { class: 'hl-actions' }, merk, weg, el('label', { class: 'hl-vgl' }, vgl, 'Vgl.'),
        el('button', { type: 'button', class: 'link', onclick: () => ctx.portion('aehnlich', { vorlage_knoten_id: k.id }) }, 'Mehr wie das'), tiefer)));
  hlWisch(art, () => { if (k.status !== 'weg') hlEntscheiden(k, 'weg', ctx); });
  // Kompakt: Antippen klappt den vollen Steckbrief auf
  art.addEventListener('click', e => { if (art.closest('.stil-kompakt') && !e.target.closest('a,button,input,label,summary,details')) art.classList.toggle('offen'); });
  return art;
}

function hlWisch(node, links) {
  let x0 = null, y0 = 0;
  node.addEventListener('touchstart', e => { const t = e.touches[0]; x0 = t.clientX; y0 = t.clientY; }, { passive: true });
  node.addEventListener('touchend', e => {
    if (x0 === null) return; const t = e.changedTouches[0], dx = t.clientX - x0, dy = t.clientY - y0; x0 = null;
    if (dx < -90 && Math.abs(dy) < 50 && !e.target.closest('a,button,input,select,textarea,summary')) links();
  });
}

async function hlEntscheiden(k, status, ctx) {
  const vorher = k.status;
  try {
    await hlCall('entscheiden', { knoten_id: k.id, status });
    if (status === 'weg') { hlVergleich.delete(k.id); hlRueckgaengig(k, vorher, ctx); } else toast(status === 'gemerkt' ? 'Gemerkt.' : 'Gespeichert.');
    await ctx.neu();
  } catch (e) { toast(e.message, true); }
}
function hlRueckgaengig(k, vorher, ctx) {
  const t = $('#toast');
  t.replaceChildren('„' + k.titel + '“ ausgeblendet. ', el('button', { type: 'button', class: 'link', onclick: async () => { t.hidden = true; await hlCall('entscheiden', { knoten_id: k.id, status: vorher }).catch(e => toast(e.message, true)); await ctx.neu(); } }, 'Rückgängig'));
  t.className = 'toast'; t.hidden = false; clearTimeout(toastTimer); toastTimer = setTimeout(() => { t.hidden = true; }, 6000);
}

// ---------- Ebene ----------
async function hlEbene(sid, kid) {
  setChrome('Highlights', { tab: 'highlights', back: true });
  const live = viewGuard();
  let timer = null, linse = sessionStorage.getItem('hl_linse_' + sid + '_' + (kid || 0)) || '', mitWeg = false, daten = null;
  disposeSuche = () => { clearTimeout(timer); };
  const pfad = el('nav', { class: 'hl-pfad', 'aria-label': 'Pfad' });
  const kopf = el('header', { class: 'hl-kopf' });
  const chips = el('div', { class: 'hl-chips' });
  const fazit = el('p', { class: 'hl-fazit' });
  const lauf = el('div', { class: 'hl-lauf', role: 'status' });
  const karten = el('div', { class: 'hl-grid stil-' + hlStil() });
  const stilWahl = el('div', { class: 'hl-stile', role: 'group', 'aria-label': 'Darstellung' }, el('span', { class: 'small muted' }, 'Darstellung'),
    HL_STILE.map(([key, label]) => { const b = el('button', { type: 'button', class: 'hl-chip' + (hlStil() === key ? ' an' : ''), 'aria-pressed': hlStil() === key }, label);
      b.onclick = () => { hlSchreibe('hl_stil', key); karten.className = 'hl-grid stil-' + key; stilWahl.querySelectorAll('button').forEach(x => { const on = x === b; x.classList.toggle('an', on); x.setAttribute('aria-pressed', on); }); }; return b; }));
  const unten = el('div', { class: 'hl-unten' });
  const vgl = el('div', { class: 'hl-vgl-leiste', hidden: true });
  hlFill(main, pfad, kopf, chips, stilWahl, fazit, lauf, karten, unten, vgl);
  const ctx = { sid, alter: null, neu: () => lesen(), portion: (art, extra = {}) => portion(art, extra), vergleichLeiste: () => leiste() };

  async function portion(art, extra = {}) {
    hlFill(lauf, el('div', { class: 'spinner' }, 'Wird angefragt …'));
    try { await hlCall('portion', { suche_id: sid, parent_id: kid, art, linse: linse || null, ...extra }); await lesen(); }
    catch (e) { hlFill(lauf, el('p', { class: 'hl-ende' }, e.message)); }
  }
  function leiste() {
    const ids = [...hlVergleich].filter(id => daten?.karten.some(k => k.id === id));
    vgl.hidden = ids.length < 2;
    hlFill(vgl, el('span', {}, ids.length + ' ausgewählt'), el('button', { class: 'primary', type: 'button', onclick: () => hlVergleichen(daten.karten.filter(k => ids.includes(k.id)), ctx) }, 'Vergleichen'), el('button', { type: 'button', class: 'link', onclick: () => { hlVergleich.clear(); lesen(); } }, 'Leeren'));
  }

  async function lesen() {
    clearTimeout(timer);
    let r;
    try { r = await hlCall('lesen', { suche_id: sid, knoten_id: kid, mit_weg: mitWeg }); }
    catch (e) { if (live()) hlFill(lauf, el('p', { class: 'err-text' }, e.message)); return; }
    if (!live()) return;
    daten = r;
    const v = r.suche.vorlieben || {};
    ctx.alter = Array.isArray(v.familie_alter) ? v.familie_alter : null;
    const titel = r.knoten ? r.knoten.titel : r.suche.wunsch;
    hlSchreibe('hl_last', { sid, kid, titel });
    setChrome(titel, { tab: 'highlights', back: true });
    // Pfadleiste
    hlFill(pfad, el('a', { href: '#/highlights' }, 'Highlights'), el('span', { 'aria-hidden': true }, '›'),
      ...(r.pfad.length ? [el('a', { href: hlHref(sid) }, hlKurz(r.suche.wunsch)), ...r.pfad.flatMap((p, i) => [el('span', { 'aria-hidden': true }, '›'), i === r.pfad.length - 1 ? el('strong', {}, p.titel) : el('a', { href: hlHref(sid, p.id) }, p.titel)])] : [el('strong', {}, hlKurz(r.suche.wunsch))]));
    // Kopf
    const kb = r.knoten ? hlBild(r.knoten.bild, r.knoten.typ, 'hl-kopf-img') : null;
    hlFill(kopf, ...[kb, el('div', { class: 'hl-kopf-text' }, el('p', { class: 'eyebrow' }, r.knoten ? (HL_TYP[r.knoten.typ] || HL_TYP.erlebnis)[0] + ' · Ebene ' + (r.knoten.ebene + 1) : 'Euer Wunsch'),
      el('h2', {}, titel), r.knoten?.steckbrief?.moment ? el('p', {}, r.knoten.steckbrief.moment) : null,
      r.knoten ? el('div', { class: 'row' }, el('button', { type: 'button', class: 'hl-merk' + (r.knoten.status === 'gemerkt' ? ' an' : ''), onclick: () => hlEntscheiden(r.knoten, r.knoten.status === 'gemerkt' ? 'offen' : 'gemerkt', ctx) }, r.knoten.status === 'gemerkt' ? '♥ Gemerkt' : '♡ Merken')) : null)].filter(Boolean));
    kopf.classList.toggle('mit-bild', !!kb);
    if (kb && hlFly) hlZoom(kb);
    // Chips: Vorlieben (änderbar) + Linsen
    const andr = el('button', { type: 'button', class: 'hl-chip pref' }, 'Andrang ' + (v.andrang_max ? 'bis ' + v.andrang_max + '/5' : 'egal') + ' ✎');
    andr.onclick = async () => { const n = v.andrang_max ? (v.andrang_max % 5) + 1 : 3; const neu = { ...v, andrang_max: n === 5 ? null : n }; await hlCall('suche_speichern', { id: sid, vorlieben: neu }).catch(e => toast(e.message, true)); toast('Gilt für die nächsten Vorschläge.'); lesen(); };
    const zeitChip = el('button', { type: 'button', class: 'hl-chip pref' }, 'Reisezeit ' + (v.reisezeit || 'offen') + ' ✎');
    zeitChip.onclick = () => hlZeitDialog(v, async neu => { await hlCall('suche_speichern', { id: sid, vorlieben: neu }); lesen(); });
    hlFill(chips, andr, zeitChip, el('span', { class: 'hl-chip-sep', 'aria-hidden': true }),
      ...HL_LINSEN.map(([key, label]) => { const b = el('button', { type: 'button', class: 'hl-chip' + (linse === key ? ' an' : ''), 'aria-pressed': linse === key }, label); b.onclick = () => { linse = linse === key ? '' : key; sessionStorage.setItem('hl_linse_' + sid + '_' + (kid || 0), linse); lesen(); }; return b; }));
    // Portionen
    const ps = r.portionen, letzte = ps[ps.length - 1];
    const laeuft = letzte && ['wartet', 'laeuft'].includes(letzte.status) && Date.now() - new Date(letzte.erstellt_am) < 6 * 60e3;
    const fertige = ps.filter(p => p.status === 'fertig');
    fazit.textContent = fertige.length ? fertige[fertige.length - 1].fazit || '' : '';
    fazit.hidden = !fazit.textContent;
    hlFill(karten, ...r.karten.map(k => hlKarte(k, ctx)));
    const ende = r.anzahl >= 20 || fertige.some(p => p.ende);
    const kosten = ps.reduce((s, p) => s + (Number(p.kosten_usd) || 0), 0);
    if (laeuft) {
      hlFill(lauf, el('div', { class: 'spinner' }, { start: 'Die ersten 5 Vorschläge', mehr: '5 weitere Vorschläge', aehnlich: 'Ähnliche Vorschläge', anders: 'Eine andere Richtung', frage: 'Antwort auf deine Frage' }[letzte.art] + ' werden recherchiert … (1–2 Min., mit Websuche)'));
      timer = setTimeout(lesen, 4000);
    } else if (letzte?.status === 'fehler') hlFill(lauf, el('p', { class: 'err-text' }, 'Letzte Anfrage fehlgeschlagen: ' + (letzte.fehler || 'unbekannt') + '. Du kannst es erneut versuchen.'));
    else hlFill(lauf, );
    // Steuerung unten
    const frage = el('input', { type: 'text', maxlength: 400, placeholder: 'Direkt fragen, z. B. „Wo sieht man Seedrachen?“' });
    const fragen = el('form', { class: 'hl-frage-form' }, frage, hlDiktat(frage), el('button', { type: 'submit' }, 'Fragen'));
    fragen.onsubmit = e => { e.preventDefault(); if (frage.value.trim().length >= 3) portion('frage', { text: frage.value.trim() }); };
    const leer = !r.karten.length && !r.weg;
    hlFill(unten, 
      ende ? el('p', { class: 'hl-ende' }, (fertige.find(p => p.ende)?.ende_hinweis || 'Das waren die starken Vorschläge für diese Ebene.') + ' Weitere wären Füller – probier „Andere Richtung“ oder frag gezielt.') : null,
      el('div', { class: 'hl-mehr' },
        leer ? el('button', { class: 'primary', type: 'button', disabled: laeuft, onclick: () => portion(kid ? 'mehr' : 'start') }, '5 Vorschläge holen') : el('button', { class: 'primary', type: 'button', disabled: laeuft || r.anzahl >= 20, onclick: () => portion('mehr') }, 'Mehr anzeigen (+5)'),
        leer ? null : el('button', { type: 'button', disabled: laeuft, onclick: () => portion('anders') }, 'Andere Richtung'),
        el('span', { class: 'small muted' }, HL_KOSTEN + (linse ? ' · Linse: ' + HL_LINSEN.find(l => l[0] === linse)[1] : ''))),
      fragen,
      r.weg ? el('button', { type: 'button', class: 'link', onclick: () => { mitWeg = !mitWeg; lesen(); } }, mitWeg ? 'Ausgeblendete verbergen' : 'Ausgeblendet (' + r.weg + ') zeigen') : null,
      el('p', { class: 'small muted' }, r.anzahl + ' Vorschläge auf dieser Ebene' + (kosten ? ' · bisher ' + kosten.toFixed(2) + ' USD' : '') + ' · ', el('a', { href: '#/highlights/merk' }, 'Merkliste')));
    leiste();
  }
  hlRandWischen();
  await lesen();
}
// Zurück per Wischen vom linken Rand (nur in einer Highlights-Ebene, Listener einmalig)
let hlRandAktiv = false;
function hlRandWischen() {
  if (hlRandAktiv) return; hlRandAktiv = true;
  let sx = null;
  main.addEventListener('touchstart', e => { sx = current.view === 'highlights' && e.touches[0].clientX < 28 ? e.touches[0].clientX : null; }, { passive: true });
  main.addEventListener('touchend', e => { if (sx !== null && e.changedTouches[0].clientX - sx > 90) history.back(); sx = null; });
}
const hlFill = (node, ...kids) => node.replaceChildren(...kids.flat().filter(k => k !== null && k !== undefined && k !== false)); // replaceChildren schreibt sonst „null“
const hlKurz = s => (s.length > 34 ? s.slice(0, 32) + '…' : s);

function hlZoom(ziel) {
  const f = hlFly; hlFly = null;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const img = ziel.querySelector('img'); if (!img) return;
  const to = ziel.getBoundingClientRect();
  const clone = el('img', { class: 'hl-fly', src: f.src, alt: '' });
  Object.assign(clone.style, { left: f.rect.left + 'px', top: f.rect.top + 'px', width: f.rect.width + 'px', height: f.rect.height + 'px' });
  document.body.append(clone); img.style.opacity = '0';
  requestAnimationFrame(() => { Object.assign(clone.style, { left: to.left + 'px', top: to.top + 'px', width: to.width + 'px', height: to.height + 'px' }); });
  setTimeout(() => { img.style.opacity = ''; clone.remove(); }, 420);
}

function hlZeitDialog(v, speichern) {
  const d = el('dialog', { class: 'trip-dialog' }), f = el('input', { type: 'text', maxlength: 60, value: v.reisezeit || '', placeholder: 'z. B. Dez 2026 – Jan 2027' });
  const ok = el('button', { class: 'primary', type: 'button' }, 'Übernehmen');
  ok.onclick = async () => { ok.disabled = true; try { await speichern({ ...v, reisezeit: f.value.trim() || null }); d.close(); } catch (e) { toast(e.message, true); ok.disabled = false; } };
  d.append(el('h2', {}, 'Reisezeit'), el('p', { class: 'small muted' }, 'Nur für die Saison-Einschätzung. Leer = offen.'), f, el('div', { class: 'row' }, ok, el('button', { type: 'button', onclick: () => d.close() }, 'Abbrechen')));
  main.append(d); d.addEventListener('close', () => d.remove()); d.showModal(); f.focus();
}

function hlVergleichen(liste, ctx) {
  const d = el('dialog', { class: 'trip-dialog hl-vgl-dialog', 'aria-label': 'Vergleich' });
  const z = (label, f) => el('tr', {}, el('th', {}, label), liste.map(k => el('td', {}, f(k.steckbrief || {}, k))));
  d.append(el('h2', {}, 'Vergleich'), el('div', { class: 'hl-vgl-scroll' }, el('table', { class: 'hl-vgl-table' },
    el('thead', {}, el('tr', {}, el('th', {}), liste.map(k => el('th', {}, k.titel)))),
    el('tbody', {},
      z('WOW', s => hlPunkte(s.wow)), z('Andrang', s => (s.andrang ? s.andrang + '/5 ' + HL_ANDRANG[s.andrang] : '–')),
      z('Zeit', s => s.zeit || '–'), z('Kosten für 4', s => s.kosten_4 || '–'), z('Familie', s => hlFamilie(s, ctx.alter)),
      z('Saison', s => (s.saison?.text || '–') + (s.saison?.status ? ' (' + s.saison.status + ')' : '')),
      z('Fachwert', s => (s.fach?.[0] ? s.fach[0].label + ': ' + s.fach[0].wert : '–')), z('Eher nicht', s => (s.eher_nicht || '–').replace(/^Eher nicht,? wenn /i, '… wenn '))))),
    el('button', { type: 'button', onclick: () => d.close() }, 'Schließen'));
  main.append(d); d.addEventListener('close', () => d.remove()); d.showModal();
}

// ---------- Merkliste ----------
async function hlMerkliste() {
  setChrome('Merkliste', { tab: 'highlights', back: true });
  const live = viewGuard();
  loading();
  const r = await hlCall('merkliste', {});
  if (!live()) return;
  const weiter = hlLese('hl_last');
  const gruppen = new Map();
  for (const k of r.gemerkt) { const g = k.pfad.length > 1 ? k.pfad[0].titel : k.wunsch; if (!gruppen.has(g)) gruppen.set(g, []); gruppen.get(g).push(k); }
  hlFill(main, 
    el('section', { class: 'hl-merk-kopf' }, el('p', { class: 'eyebrow' }, 'HIGHLIGHTS'), el('h2', {}, 'Merkliste'), el('p', { class: 'muted' }, r.gemerkt.length + ' gemerkt · nach Region')),
    weiter ? el('a', { class: 'hl-continue', href: hlHref(weiter.sid, weiter.kid) }, el('span', { class: 'eyebrow' }, 'WEITER BEI'), el('strong', {}, weiter.titel), el('span', { 'aria-hidden': true }, '→')) : null,
    ...(r.gemerkt.length ? [...gruppen].map(([g, ks]) => el('section', { class: 'hl-merk-gruppe' }, el('h3', {}, g + ' · ' + ks.length),
      el('div', { class: 'hl-merk-liste' }, ks.map(k => el('a', { class: 'hl-merk-row', href: hlHref(k.suche_id, k.id) }, hlBild(k.bild, k.typ, 'hl-merk-img'),
        el('div', {}, el('strong', {}, k.titel), el('span', { class: 'small muted' }, k.pfad.slice(0, -1).map(p => p.titel).join(' › ') || k.wunsch),
          el('span', { class: 'small' }, ['WOW ' + (k.steckbrief?.wow ?? '–'), 'Andrang ' + (k.steckbrief?.andrang ?? '–') + '/5', k.steckbrief?.zeit, k.steckbrief?.kosten_4].filter(Boolean).join(' · ')))))))) : [el('p', { class: 'muted' }, 'Noch nichts gemerkt. ', el('a', { href: '#/highlights' }, 'Zu den Highlights →'))]));
}
