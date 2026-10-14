/* KI-System – Rohbau der Web-/Handy-App (Werkstatt #4).
   Spricht ausschließlich mit app-api (Supabase). Kein Schlüssel im Code.
   Schreibende Aktionen laufen nur nach einem Klick von Sebastian. */
'use strict';

const APP_VERSION = '0.1.0';
const API = 'https://sdgzwxiqcijxfpcjpydw.supabase.co/functions/v1/app-api';
const TOKEN_KEY = 'ks_token';

// ---------- Hilfen ----------
const $ = (sel, root = document) => root.querySelector(sel);
const el = (tag, attrs = {}, ...kids) => {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === 'class') n.className = v;
    else if (k === 'html') n.innerHTML = v;
    else if (k.startsWith('on')) n.addEventListener(k.slice(2), v);
    else if (v !== null && v !== undefined && v !== false) n.setAttribute(k, v === true ? '' : v);
  }
  for (const k of kids.flat()) if (k !== null && k !== undefined) n.append(k.nodeType ? k : document.createTextNode(String(k)));
  return n;
};
const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const fmtDate = (s) => { if (!s) return ''; const d = new Date(s); return isNaN(d) ? String(s) : d.toLocaleDateString('de-DE'); };
const fmtUsd = (n) => (n === null || n === undefined) ? '' : Number(n).toFixed(2) + ' USD';

let toastTimer = null;
function toast(msg, err = false) {
  const t = $('#toast');
  t.textContent = msg; t.className = 'toast' + (err ? ' err' : ''); t.hidden = false;
  clearTimeout(toastTimer); toastTimer = setTimeout(() => { t.hidden = true; }, err ? 6000 : 2500);
}

function md(text) {
  const box = el('div', { class: 'md' });
  if (window.marked) box.innerHTML = marked.parse(String(text ?? ''), { breaks: true });
  else box.append(el('pre', {}, String(text ?? '')));
  return box;
}

// Unbekannte Datenstrukturen lesbar darstellen (Rohbau).
function renderAny(v, depth = 0) {
  if (v === null || v === undefined) return el('span', { class: 'muted' }, '–');
  if (Array.isArray(v)) {
    if (!v.length) return el('span', { class: 'muted' }, 'keine');
    return el('ul', {}, v.map((x) => el('li', {}, renderAny(x, depth + 1))));
  }
  if (typeof v === 'object') {
    const dl = el('dl', { class: 'kv' });
    for (const [k, x] of Object.entries(v)) dl.append(el('dt', {}, k), el('dd', {}, renderAny(x, depth + 1)));
    return dl;
  }
  if (typeof v === 'boolean') return v ? 'ja' : 'nein';
  return String(v);
}

// Zwei-Schritt-Bestätigung ohne Browser-Dialog.
function confirmButton(label, onYes, cls = '') {
  const wrap = el('span');
  const btn = el('button', { class: cls, onclick: () => {
    wrap.replaceChildren(
      el('span', { class: 'muted small' }, 'Wirklich? '),
      el('button', { class: 'primary', onclick: async () => { btn.disabled = true; wrap.replaceChildren(btn); await onYes(); btn.disabled = false; } }, 'Ja'),
      el('button', { onclick: () => wrap.replaceChildren(btn) }, 'Nein'),
    );
  } }, label);
  wrap.append(btn);
  return wrap;
}

// ---------- Zugang ----------
const store = {
  get token() { try { return localStorage.getItem(TOKEN_KEY); } catch { return null; } },
  set token(v) { try { v ? localStorage.setItem(TOKEN_KEY, v) : localStorage.removeItem(TOKEN_KEY); } catch { /* privater Modus */ } },
};

async function http(path, { method = 'GET', body, auth = true } = {}) {
  const headers = { 'Content-Type': 'application/json' };
  if (auth && store.token) headers.Authorization = 'Bearer ' + store.token;
  const r = await fetch(API + path, { method, headers, body: body ? JSON.stringify(body) : undefined });
  let j; try { j = await r.json(); } catch { j = { ok: false, fehler: 'Keine Antwort (' + r.status + ')' }; }
  if (r.status === 401 && auth) { store.token = null; route('login'); throw new Error(j.fehler || 'Nicht angemeldet'); }
  return j;
}

async function aktion(name, daten = {}) {
  const j = await http('/aktion', { method: 'POST', body: { aktion: name, daten } });
  if (!j.ok) throw new Error(j.fehler || 'Fehler bei ' + name);
  return j.ergebnis;
}

// ---------- Navigation ----------
const main = $('#main');
const tabs = $('#tabs');
let current = { view: null, arg: null };

function route(view, arg = null) {
  const h = arg !== null ? `#/${view}/${arg}` : `#/${view}`;
  if (location.hash !== h) { location.hash = h; return; }
  render();
}
function parseHash() {
  const m = location.hash.match(/^#\/([a-z]+)(?:\/(.+))?$/);
  return m ? { view: m[1], arg: m[2] ?? null } : { view: 'auftraege', arg: null };
}
window.addEventListener('hashchange', render);

function setChrome(title, { back = false, showTabs = true, tab = null } = {}) {
  $('#title').textContent = title;
  $('#btn-back').hidden = !back;
  tabs.hidden = !showTabs;
  for (const b of tabs.querySelectorAll('button')) b.classList.toggle('on', b.dataset.view === tab);
}
$('#btn-back').addEventListener('click', () => (history.length > 1 ? history.back() : route('auftraege')));
tabs.addEventListener('click', (e) => { const b = e.target.closest('button'); if (b) route(b.dataset.view); });

function loading(text = 'Lade …') { main.replaceChildren(el('div', { class: 'spinner' }, text)); }
function showError(e) { main.append(el('div', { class: 'card err-text' }, 'Fehler: ' + (e?.message || e))); }

async function render() {
  current = parseHash();
  if (!store.token && current.view !== 'login') { route('login'); return; }
  const views = { login: viewLogin, auftraege: viewAuftraege, auftrag: viewAuftrag, neu: viewNeu, einstellungen: viewEinstellungen, werkstatt: viewWerkstatt };
  const fn = views[current.view] || viewAuftraege;
  try { await fn(current.arg); } catch (e) { showError(e); }
}

// ---------- Ansicht: Login ----------
async function viewLogin() {
  setChrome('KI-System', { showTabs: false });
  main.replaceChildren($('#t-login').content.cloneNode(true));
  $('#einrichten-link').href = API + '/';
  const status = $('#login-status');
  try {
    const s = await http('/status', { auth: false });
    status.textContent = s.eingerichtet ? 'Verbindung steht. Bitte Passwort eingeben.' : 'Noch kein Passwort eingerichtet – siehe unten.';
  } catch { status.textContent = 'Schnittstelle nicht erreichbar. Internet prüfen.'; }
  $('#login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = e.target.querySelector('button'); btn.disabled = true;
    try {
      const geraet = $('#login-geraet').value.trim() || (navigator.userAgent.includes('iPhone') ? 'iPhone' : navigator.userAgent.includes('Android') ? 'Android' : 'Browser');
      const r = await http('/login', { method: 'POST', body: { passwort: $('#login-pw').value, geraet }, auth: false });
      if (!r.ok || !r.token) throw new Error(r.fehler || 'Anmeldung fehlgeschlagen');
      store.token = r.token;
      toast('Angemeldet bis ' + fmtDate(r.laeuft_ab));
      route('auftraege');
    } catch (err) { toast(err.message, true); } finally { btn.disabled = false; }
  });
}

// ---------- Ansicht: Aufträge ----------
let auftragFilter = 'alle';
function statusPill(a) {
  if (a.posteingang === 'neu') return el('span', { class: 'pill neu' }, 'neues Ergebnis');
  if (a.status === 'pausiert') return el('span', { class: 'pill wartet' }, 'wartet auf dich');
  if (a.status === 'laeuft') return el('span', { class: 'pill laeuft' }, 'läuft');
  if (a.status === 'abgebrochen') return el('span', { class: 'pill fehler' }, 'abgebrochen');
  if (a.posteingang === 'abgeholt') return el('span', { class: 'pill wartet' }, 'Entscheidung offen');
  return el('span', { class: 'pill' }, a.status || '');
}
function wartetAufDich(a) { return a.posteingang === 'neu' || a.posteingang === 'abgeholt' || a.status === 'pausiert' || a.status === 'entwurf' || a.status === 'bestaetigt'; }

async function viewAuftraege() {
  setChrome('Aufträge', { tab: 'auftraege' });
  loading();
  const liste = await aktion('auftraege_suchen', {});
  const neu = liste.filter((a) => a.posteingang === 'neu').length;
  const badge = $('#badge-neu'); badge.hidden = !neu; badge.textContent = neu;

  const filter = el('div', { class: 'filter' });
  const defs = [['alle', 'Alle'], ['wartet', 'Wartet auf dich'], ['laeuft', 'Läuft'], ['fertig', 'Fertig']];
  for (const [k, l] of defs) filter.append(el('button', { class: k === auftragFilter ? 'on' : '', onclick: () => { auftragFilter = k; render(); } }, l));

  const ul = el('ul', { class: 'list' });
  const gefiltert = liste.filter((a) =>
    auftragFilter === 'alle' ? true :
    auftragFilter === 'wartet' ? wartetAufDich(a) :
    auftragFilter === 'laeuft' ? a.status === 'laeuft' :
    (a.status === 'abgeschlossen' || a.status === 'ruhend') && !wartetAufDich(a));
  if (!gefiltert.length) ul.append(el('li', { class: 'muted' }, 'Keine Aufträge in dieser Ansicht.'));
  for (const a of gefiltert) {
    ul.append(el('li', { onclick: () => route('auftrag', a.rahmen_id) },
      el('div', { class: 't' }, a.kurzname || a.titel, statusPill(a)),
      el('div', { class: 's' }, [a.titel !== a.kurzname ? a.titel : null, a.bereich, 'Nr. ' + a.rahmen_id, 'zuletzt ' + fmtDate(a.zuletzt)].filter(Boolean).join(' · ')),
    ));
  }
  main.replaceChildren(filter, ul,
    el('div', { class: 'actions' }, el('button', { class: 'primary', onclick: () => route('neu') }, '+ Neuer Auftrag'), el('button', { onclick: render }, 'Aktualisieren')));
}

// ---------- Ansicht: Auftrag (Detail) ----------
let detailTab = 'uebersicht';
async function viewAuftrag(idStr) {
  const id = Number(idStr);
  setChrome('Auftrag ' + id, { back: true, tab: 'auftraege' });
  loading();
  const r = await aktion('rahmen_lesen', { rahmen_id: id });
  setChrome(r.titel || 'Auftrag ' + id, { back: true, tab: 'auftraege' });

  const kopf = el('div', { class: 'card' },
    el('div', { class: 'row' }, statusPill(r), el('span', { class: 'muted small' },
      `Nr. ${r.id} · Status ${r.status} · ${r.runden?.length ?? 0} Runden · Kosten ${fmtUsd(r.kosten_bisher_usd)} von ${fmtUsd(r.kostenlimit_usd)}`)),
    r.pause_grund ? el('p', { class: 'small' }, el('b', {}, 'Hinweis: '), r.pause_grund) : null,
  );

  // Aktionen je Zustand – jede schreibende Aktion nur per Klick.
  const akt = el('div', { class: 'actions' });
  if (r.status === 'entwurf' || r.status === 'bestaetigt') {
    const stufe = el('select', {}, el('option', { value: '3' }, 'Stufe 3 – durchlaufen'), el('option', { value: '2' }, 'Stufe 2 – Stopp vor jeder Kritikrunde'));
    akt.append(stufe, confirmButton('Auftrag starten', async () => {
      try { await aktion('auftrag_starten', { rahmen_id: id, stufe: Number(stufe.value) }); toast('Gestartet'); render(); } catch (e) { toast(e.message, true); }
    }, 'primary'));
    akt.append(el('button', { onclick: () => stammdatenDialog(id) }, 'Stammdaten freigeben'));
  }
  if (r.status === 'pausiert') {
    const limit = el('input', { type: 'number', step: '0.5', min: '0', placeholder: 'neues Kostenlimit (optional)', style: 'max-width:220px' });
    akt.append(limit, confirmButton('Fortsetzen', async () => {
      try { await aktion('auftrag_weiter', { rahmen_id: id, ...(limit.value ? { neues_kostenlimit: Number(limit.value) } : {}) }); toast('Fortgesetzt'); render(); } catch (e) { toast(e.message, true); }
    }, 'primary'));
  }
  if (!['abgeschlossen', 'abgebrochen'].includes(r.status)) {
    akt.append(confirmButton('Abbrechen', async () => {
      try { await aktion('rahmen_status_setzen', { rahmen_id: id, status: 'abgebrochen' }); toast('Abgebrochen'); render(); } catch (e) { toast(e.message, true); }
    }, 'danger'));
  }
  if (akt.childElementCount) kopf.append(akt);

  const sub = el('div', { class: 'subtabs' });
  const inhalt = el('div');
  const tabsDef = [['uebersicht', 'Übersicht'], ['verlauf', 'Verlauf'], ['belege', 'Belege'], ['bewertung', 'Bewertung'], ['rahmen', 'Rahmen']];
  for (const [k, l] of tabsDef) sub.append(el('button', { class: k === detailTab ? 'on' : '', onclick: () => { detailTab = k; for (const b of sub.children) b.classList.toggle('on', b.textContent === l); zeige(); } }, l));

  const plaene = (r.teilnehmer || []).map((t) => t.plan_label).filter(Boolean);
  async function zeige() {
    inhalt.replaceChildren(el('div', { class: 'spinner' }, 'Lade …'));
    try {
      if (detailTab === 'uebersicht') {
        if (!r.ergebnis_vorhanden) { inhalt.replaceChildren(el('div', { class: 'card muted' }, 'Noch kein Ergebnis.')); return; }
        const v = await aktion('verlauf_lesen', { rahmen_id: id, ebene: 'uebersicht' });
        inhalt.replaceChildren(el('div', { class: 'card' }, md(v.markdown)), entscheidungsBlock(id));
      } else if (detailTab === 'verlauf' || detailTab === 'belege') {
        const sel = el('select', {}, el('option', { value: '' }, 'alle Pläne'), plaene.map((p) => el('option', { value: p }, p)));
        const box = el('div', { class: 'card' });
        const lade = async () => {
          box.replaceChildren(el('div', { class: 'spinner' }, 'Lade …'));
          try { const v = await aktion('verlauf_lesen', { rahmen_id: id, ebene: detailTab, ...(sel.value ? { plan: sel.value } : {}) }); box.replaceChildren(md(v.markdown)); }
          catch (e) { box.replaceChildren(el('span', { class: 'err-text' }, e.message)); }
        };
        sel.addEventListener('change', lade);
        inhalt.replaceChildren(el('div', { class: 'row', style: 'margin-bottom:8px' }, sel), box);
        await lade();
      } else if (detailTab === 'bewertung') {
        const b = await aktion('bewertung_lesen', { rahmen_id: id });
        inhalt.replaceChildren(el('div', { class: 'card' }, renderAny(b)), urteilBlock(id));
      } else {
        const { runden, teilnehmer, pflichtangaben, passende_erkenntnisse, ...rest } = r;
        inhalt.replaceChildren(
          el('div', { class: 'card' }, el('h2', {}, 'Rahmen'), renderAny(rest)),
          el('div', { class: 'card' }, el('h2', {}, 'Teilnehmer'), renderAny(teilnehmer)),
          el('div', { class: 'card' }, el('h2', {}, 'Pflichtangaben'), renderAny(pflichtangaben)),
          el('div', { class: 'card' }, el('h2', {}, 'Runden'), renderAny(runden)),
          el('div', { class: 'card' }, el('h2', {}, 'Passende Erkenntnisse'), renderAny(passende_erkenntnisse)),
        );
      }
    } catch (e) { inhalt.replaceChildren(el('div', { class: 'card err-text' }, e.message)); }
  }
  main.replaceChildren(kopf, sub, inhalt);
  await zeige();
}

function entscheidungsBlock(id) {
  const ta = el('textarea', { placeholder: 'Deine Entscheidung zum Ergebnis, z. B. „Plan B übernehmen, Probewoche ab 20.10.“' });
  return el('div', { class: 'card' }, el('h2', {}, 'Entscheidung festhalten'),
    el('p', { class: 'muted small' }, 'Wird im System gespeichert und setzt das Ergebnis im Posteingang auf erledigt.'),
    ta, el('div', { class: 'actions' }, confirmButton('Entscheidung speichern', async () => {
      if (!ta.value.trim()) { toast('Bitte Text eingeben', true); return; }
      try { await aktion('nutzer_entscheidung', { rahmen_id: id, entscheidung: ta.value.trim() }); toast('Gespeichert'); ta.value = ''; } catch (e) { toast(e.message, true); }
    }, 'primary')));
}
function urteilBlock(id) {
  const kom = el('input', { type: 'text', placeholder: 'Kommentar (optional)' });
  const row = el('div', { class: 'actions' });
  for (const u of ['ja', 'teilweise', 'nein']) row.append(confirmButton('Geholfen: ' + u, async () => {
    try { await aktion('nutzer_urteil', { rahmen_id: id, urteil: u, ...(kom.value ? { kommentar: kom.value } : {}) }); toast('Urteil gespeichert'); } catch (e) { toast(e.message, true); }
  }));
  return el('div', { class: 'card' }, el('h2', {}, 'Hat dir das Ergebnis geholfen?'), kom, row);
}

async function stammdatenDialog(id) {
  const box = el('div', { class: 'card' }, el('h2', {}, 'Stammdaten für diesen Auftrag freigeben'), el('div', { class: 'spinner' }, 'Lade …'));
  main.insertBefore(box, main.children[1]);
  try {
    const sd = await aktion('stammdaten_lesen', {});
    const eintraege = Array.isArray(sd) ? sd : (sd.stammdaten || sd.eintraege || []);
    const form = el('div');
    for (const s of eintraege) {
      const cb = el('input', { type: 'checkbox', value: s.id, style: 'width:auto;margin-right:8px', disabled: s.nie_extern ? true : null });
      form.append(el('label', { style: 'display:flex;align-items:center;color:inherit' }, cb,
        `${s.art || ''}: ${s.bezeichnung || ''}${s.person ? ' (' + s.person + ')' : ''}${s.nie_extern ? ' – gesperrt' : ''}`));
    }
    box.replaceChildren(el('h2', {}, 'Stammdaten für diesen Auftrag freigeben'),
      el('p', { class: 'muted small' }, 'Nur anhaken, was die KIs für diese Frage wirklich brauchen. Ersetzt die bisherige Auswahl.'),
      form, el('div', { class: 'actions' },
        confirmButton('Freigabe speichern', async () => {
          const ids = [...form.querySelectorAll('input:checked')].map((c) => Number(c.value));
          try { await aktion('stammdaten_freigeben', { rahmen_id: id, ids }); toast(`${ids.length} freigegeben`); box.remove(); } catch (e) { toast(e.message, true); }
        }, 'primary'),
        el('button', { onclick: () => box.remove() }, 'Schließen')));
  } catch (e) { box.replaceChildren(el('span', { class: 'err-text' }, e.message)); }
}

// ---------- Ansicht: Neuer Auftrag ----------
async function viewNeu() {
  setChrome('Neuer Auftrag', { tab: 'neu' });
  loading();
  const [modelle, rollen] = await Promise.all([aktion('modelle_lesen', {}), aktion('rollen_lesen', { status: 'aktiv' })]);
  const teilnehmerModelle = (modelle.meine_modelle || []).filter((m) => !/NIE Teilnehmer/i.test(m.staerken || ''));
  const rollenListe = Array.isArray(rollen) ? rollen : (rollen.rollen || []);
  const rollenNamen = rollenListe.map((r) => r.name || r.rolle).filter(Boolean);

  const f = {
    titel: el('input', { type: 'text', required: true, maxlength: 120 }),
    frage: el('textarea', { required: true, placeholder: 'Die Frage so, wie du sie stellen würdest.' }),
    projekt: el('input', { type: 'text', placeholder: 'z. B. Weltreise / Homeschooling' }),
    ziel: el('textarea', { placeholder: 'Was soll am Ende herauskommen?' }),
    vorgaben: el('textarea', { placeholder: 'Fakten, Rahmenbedingungen, geprüfte Angaben' }),
    grenzen: el('textarea', { placeholder: 'Was die KIs nicht tun sollen' }),
    ergebnisform: el('input', { type: 'text', placeholder: 'z. B. R3 (Empfehlung; Streitpunkte; Fakten vs. Annahmen; offene Fragen)' }),
    limit: el('input', { type: 'number', step: '0.5', min: '0.5', value: '2' }),
    runden: el('input', { type: 'number', min: '0', max: '10', value: '2' }),
    haltbarkeit: el('select', {}, ['einmalig', 'projekt', 'dauerhaft'].map((h) => el('option', { value: h }, h))),
  };
  f.haltbarkeit.value = 'projekt';

  const tnBox = el('div');
  const addRow = (modell = '', rolle = '') => {
    const row = el('div', { class: 'teilnehmer-row' },
      el('select', { class: 'tn-modell' }, el('option', { value: '' }, '– Modell –'), teilnehmerModelle.map((m) => el('option', { value: m.name, selected: m.name === modell ? true : null }, m.name))),
      el('input', { class: 'tn-rolle', type: 'text', list: 'rollen-liste', placeholder: 'Rolle (z. B. Planer)', value: rolle }),
      el('button', { type: 'button', onclick: () => row.remove() }, '✕'));
    tnBox.append(row);
  };
  addRow('', 'Planer'); addRow('', 'Planer'); addRow('', 'Gegenanwalt');

  const angabenBox = el('div');
  const addAngabe = () => angabenBox.append(el('div', { class: 'teilnehmer-row' },
    el('input', { class: 'pa-frage', type: 'text', placeholder: 'Pflichtangabe (Frage)' }),
    el('input', { class: 'pa-antwort', type: 'text', placeholder: 'Antwort' }),
    el('button', { type: 'button', onclick: (e) => e.target.parentElement.remove() }, '✕')));

  const form = el('form', { class: 'card' },
    el('h2', {}, 'Council-Auftrag anlegen'),
    el('p', { class: 'muted small' }, 'Der Auftrag wird als Entwurf angelegt. Gestartet wird er erst auf der Auftragsseite per Klick.'),
    el('label', {}, 'Titel', f.titel), el('label', {}, 'Originalfrage', f.frage), el('label', {}, 'Projekt / Bereich', f.projekt),
    el('label', {}, 'Ziel', f.ziel), el('label', {}, 'Vorgaben', f.vorgaben), el('label', {}, 'Grenzen', f.grenzen), el('label', {}, 'Ergebnisform', f.ergebnisform),
    el('div', { class: 'row' }, el('label', { class: 'grow' }, 'Kostenlimit (USD)', f.limit), el('label', { class: 'grow' }, 'Max. Kritikrunden', f.runden), el('label', { class: 'grow' }, 'Haltbarkeit', f.haltbarkeit)),
    el('label', {}, 'Teilnehmer (nur OpenRouter-Modelle, mindestens 2)'), tnBox,
    el('datalist', { id: 'rollen-liste' }, rollenNamen.map((n) => el('option', { value: n }))),
    el('button', { type: 'button', class: 'link', onclick: () => addRow() }, '+ Teilnehmer'),
    el('label', {}, 'Pflichtangaben (optional)'), angabenBox,
    el('button', { type: 'button', class: 'link', onclick: addAngabe }, '+ Pflichtangabe'),
    el('div', { class: 'actions' }, el('button', { type: 'submit', class: 'primary' }, 'Entwurf anlegen')),
  );
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const teilnehmer = [...tnBox.querySelectorAll('.teilnehmer-row')].map((row, i) => ({
      teilnehmer: row.querySelector('.tn-modell').value, rolle: row.querySelector('.tn-rolle').value.trim() || undefined, plan_label: 'Plan ' + String.fromCharCode(65 + i),
    })).filter((t) => t.teilnehmer);
    if (teilnehmer.length < 2) { toast('Mindestens 2 Teilnehmer wählen', true); return; }
    const daten = {
      titel: f.titel.value.trim(), originalfrage: f.frage.value.trim(), kostenlimit_usd: Number(f.limit.value), teilnehmer,
      projekt: f.projekt.value.trim() || undefined, ziel: f.ziel.value.trim() || undefined, vorgaben: f.vorgaben.value.trim() || undefined,
      grenzen: f.grenzen.value.trim() || undefined, ergebnisform: f.ergebnisform.value.trim() || undefined,
      haltbarkeit: f.haltbarkeit.value, automatisierungsstufe: 3, max_kritikrunden: Number(f.runden.value),
    };
    for (const k of Object.keys(daten)) if (daten[k] === undefined) delete daten[k];
    const btn = form.querySelector('button[type=submit]'); btn.disabled = true;
    try {
      const r = await aktion('rahmen_anlegen', daten);
      const id = r?.rahmen_id ?? r?.id ?? (typeof r === 'number' ? r : null);
      const angaben = [...angabenBox.querySelectorAll('.teilnehmer-row')].map((row) => ({ frage: row.querySelector('.pa-frage').value.trim(), antwort: row.querySelector('.pa-antwort').value.trim(), pflicht: true })).filter((a) => a.frage);
      if (id && angaben.length) await aktion('angaben_setzen', { rahmen_id: id, angaben });
      toast('Entwurf angelegt' + (id ? ' (Nr. ' + id + ')' : ''));
      if (id) route('auftrag', id); else { main.append(el('div', { class: 'card' }, renderAny(r))); }
    } catch (err) { toast(err.message, true); } finally { btn.disabled = false; }
  });
  main.replaceChildren(form);
}

// ---------- Ansicht: Einstellungen ----------
async function viewEinstellungen() {
  setChrome('Einstellungen', { tab: 'einstellungen' });
  loading();
  const [einst, modelle, rollen] = await Promise.all([aktion('einstellungen_lesen', {}), aktion('modelle_lesen', {}), aktion('rollen_lesen', { status: 'aktiv' })]);
  const mList = el('ul', { class: 'list' });
  for (const m of modelle.meine_modelle || []) mList.append(el('li', { style: 'cursor:default' },
    el('div', { class: 't' }, m.name, m.zdr ? el('span', { class: 'pill' }, 'ZDR') : null, m.stammdaten_erlaubt ? el('span', { class: 'pill' }, 'Stammdaten') : null),
    el('div', { class: 's' }, `${m.preis_eingabe_mtok} / ${m.preis_ausgabe_mtok} USD je Mio. Tokens · ${m.staerken || ''}`)));
  const rollenListe = Array.isArray(rollen) ? rollen : (rollen.rollen || []);

  const alt = el('input', { type: 'password', autocomplete: 'current-password' });
  const neu = el('input', { type: 'password', autocomplete: 'new-password', minlength: 10 });
  const pwForm = el('form', {}, el('label', {}, 'Altes Passwort', alt), el('label', {}, 'Neues Passwort (mind. 10 Zeichen)', neu),
    el('div', { class: 'actions' }, el('button', { type: 'submit' }, 'Passwort ändern')));
  pwForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    try { const r = await http('/passwort', { method: 'POST', body: { alt: alt.value, neu: neu.value } }); if (!r.ok) throw new Error(r.fehler); toast('Passwort geändert'); alt.value = neu.value = ''; }
    catch (err) { toast(err.message, true); }
  });

  main.replaceChildren(
    el('div', { class: 'card' }, el('h2', {}, 'Council-Einstellungen'), renderAny(einst), el('p', { class: 'muted small' }, 'Änderungen an Einstellungen bitte vorerst im Chat (Claude) – kommt in einer späteren Stufe in die App.')),
    el('div', { class: 'card' }, el('h2', {}, 'Meine Modelle'), mList),
    el('div', { class: 'card' }, el('h2', {}, 'Aktive Rollen'), renderAny(rollenListe.map((r) => r.name ? `${r.name}${r.typ ? ' (' + r.typ + ')' : ''}` : r))),
    el('div', { class: 'card' }, el('h2', {}, 'Zugang'), pwForm,
      el('div', { class: 'actions' }, confirmButton('Auf diesem Gerät abmelden', async () => { try { await http('/logout', { method: 'POST' }); } catch { /* egal */ } store.token = null; route('login'); }, 'danger'))),
    el('p', { class: 'muted small' }, `App-Version ${APP_VERSION} · Schnittstelle: app-api`),
  );
}

// ---------- Ansicht: Werkstatt ----------
async function viewWerkstatt(idStr) {
  setChrome('Werkstatt', { tab: 'werkstatt', back: !!idStr });
  loading();
  if (idStr) {
    const w = await aktion('werkstatt_wunsch_lesen', { id: Number(idStr) });
    setChrome('#' + w.id + ' ' + w.titel, { tab: 'werkstatt', back: true });
    const nachrichten = el('div');
    for (const n of w.nachrichten || []) nachrichten.append(el('div', { class: 'card' },
      el('div', { class: 'muted small' }, `${n.von} → ${n.an} · ${n.art} · ${fmtDate(n.am)}`), md(n.text)));
    main.replaceChildren(
      el('div', { class: 'card' }, el('div', { class: 'row' }, el('span', { class: 'pill' }, w.status), el('span', { class: 'muted small' }, `${w.bereich} · Priorität ${w.prioritaet} · zuständig ${w.zustaendig}`)), el('p', {}, w.beschreibung || '')),
      el('h2', { style: 'font-size:1rem;margin:12px 0 6px' }, 'Nachrichten'), nachrichten,
      el('div', { class: 'card' }, el('h2', {}, 'Änderungen'), renderAny(w.aenderungen)),
    );
    return;
  }
  const w = await aktion('werkstatt_lesen', {});
  const ul = el('ul', { class: 'list' });
  for (const x of w.wuensche || []) ul.append(el('li', { onclick: () => route('werkstatt', x.id) },
    el('div', { class: 't' }, `#${x.id} ${x.titel}`, el('span', { class: 'pill' }, x.status)),
    el('div', { class: 's' }, `${x.bereich} · Priorität ${x.prioritaet} · zuständig ${x.zustaendig}`)));
  const aend = el('ul', { class: 'list' });
  for (const a of (w.letzte_aenderungen || []).slice(0, 8)) aend.append(el('li', { style: 'cursor:default' },
    el('div', { class: 't' }, `${a.art} · ${a.objekt}`), el('div', { class: 's' }, `${fmtDate(a.am)} · ${a.von}${a.version ? ' · ' + a.version : ''}`), el('div', { class: 'small' }, a.beschreibung)));
  main.replaceChildren(
    el('h2', { style: 'font-size:1rem;margin:0 0 6px' }, 'Offene Wünsche'), ul,
    el('h2', { style: 'font-size:1rem;margin:12px 0 6px' }, 'Letzte Änderungen'), aend,
    el('p', { class: 'muted small' }, 'Neue Wünsche und Nachrichten bitte im Chat – Schreiben in der Werkstatt kommt in einer späteren Stufe.'),
  );
}

// ---------- Start ----------
$('#ver').textContent = 'v' + APP_VERSION;
if ('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js').catch(() => { /* ohne Offline-Hülle weiter */ });
render();
