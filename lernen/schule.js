/* W150: Eigene Lernen-Seite (/lernen/) für Lehrer, Eltern-Codes und Kinder.
   Kennt nur die Schnittstelle lernen-api. Anmeldung mit einem Lern-Code; diese Sitzung gilt ausschließlich für
   die Lernen-Funktionen – der Server lehnt sie für alle anderen Bereiche ab. Kein Code der Hauptapp.
   Stellt die Hilfen bereit, die lernen.js erwartet (el, store, route, render, setChrome …). */
'use strict';

const APP_VERSION = '0.66.0';
// lernen.js leitet daraus die lernen-api ab; app-api selbst wird von dieser Seite nie aufgerufen.
const API = 'https://sdgzwxiqcijxfpcjpydw.supabase.co/functions/v1/app-api';
const mitRegion = (u) => u + (u.includes('?') ? '&' : '?') + 'forceFunctionRegion=eu-west-1';
const TOKEN_KEY = 'lern_token';
const LERN_SEITE = true; // lernen.js: eigene Seite (keine Hauptapp-Links)

const $ = (sel, root = document) => root.querySelector(sel);
const el = (tag, attrs = {}, ...kids) => {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === 'class') n.className = v;
    else if (k.startsWith('on')) n.addEventListener(k.slice(2), v);
    else if (v !== null && v !== undefined && (v !== false || k.startsWith('aria-'))) n.setAttribute(k, typeof v === 'boolean' && k.startsWith('aria-') ? String(v) : v === true ? '' : v);
  }
  for (const k of kids.flat()) if (k !== null && k !== undefined) n.append(k.nodeType ? k : document.createTextNode(String(k)));
  return n;
};

const store = {
  get token() { try { return localStorage.getItem(TOKEN_KEY); } catch { return null; } },
  set token(v) { try { v ? localStorage.setItem(TOKEN_KEY, v) : localStorage.removeItem(TOKEN_KEY); } catch { /* privater Modus */ } },
};
let lernIch = null; // { rolle, name, lernender_id }

const main = $('#main');
let current = { view: null, arg: null };
let renderGeneration = 0;
function viewGuard() {
  const generation = renderGeneration, hash = location.hash;
  return () => generation === renderGeneration && hash === location.hash;
}
function route(view, arg = null) {
  const h = arg !== null ? `#/${view}/${arg}` : `#/${view}`;
  if (location.hash !== h) { location.hash = h; return; }
  render();
}
function parseHash() {
  const m = location.hash.match(/^#\/([a-z]+)(?:\/(.+))?$/);
  return m ? { view: m[1], arg: m[2] ?? null } : { view: 'lernen', arg: null };
}
window.addEventListener('hashchange', render);

const KIND_ANSICHTEN = ['reise', 'weltkarte', 'reisepass', 'lerneinheit', 'weg', 'merkheft', 'wiederholen'];
function setChrome(title, { back = false } = {}) {
  document.body.dataset.area = 'lernen';
  document.body.toggleAttribute('data-kindmodus', KIND_ANSICHTEN.includes(current.view));
  $('#title').textContent = title; $('#title').classList.remove('t-reise');
  // Kinder-Code: Startseite ist die eigene Lernreise, dort gibt es kein Zurück.
  $('#btn-back').hidden = !back || (lernIch?.rolle === 'kind' && current.view === 'reise');
  $('#btn-abmelden').hidden = current.view === 'login';
}
$('#btn-back').addEventListener('click', () => { if (history.length > 1) history.back(); else route('lernen'); });
$('#btn-abmelden').addEventListener('click', async () => {
  if (!window.confirm('Auf diesem Gerät abmelden?')) return;
  try { await fetch(mitRegion(lernApi() + '/abmelden'), { method: 'POST', headers: { Authorization: 'Bearer ' + store.token } }); } catch { /* egal */ }
  store.token = null; lernIch = null; route('login');
});

function loading(text = 'Lade …') { main.replaceChildren(el('div', { class: 'spinner' }, text)); }
function showError(e) { main.append(el('div', { class: 'card err-text' }, 'Fehler: ' + (e?.message || e))); }

function viewLogin() {
  setChrome('Lernen');
  const code = el('input', { type: 'text', id: 'lern-code', autocomplete: 'one-time-code', autocapitalize: 'characters', spellcheck: 'false', placeholder: 'XXXX-XXXX-XXXX', maxlength: '20', required: true });
  const status = el('p', { class: 'small muted', role: 'status' });
  const form = el('form', { class: 'card narrow lern-login' },
    el('h2', {}, 'Anmelden'),
    el('p', { class: 'muted' }, 'Gib deinen Lern-Code ein. Du bekommst ihn von den Eltern.'),
    el('label', {}, 'Lern-Code', code),
    el('button', { type: 'submit', class: 'primary' }, 'Anmelden'), status,
    el('p', { class: 'muted small' }, 'Die Anmeldung bleibt auf diesem Gerät gespeichert. Sie gilt nur für den Bereich Lernen.'));
  form.addEventListener('submit', async (e) => {
    e.preventDefault(); status.textContent = 'Prüfe …';
    try {
      const r = await fetch(mitRegion(lernApi() + '/anmelden'), { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ code: code.value }) });
      const j = await r.json().catch(() => ({ ok: false, fehler: 'Keine Antwort' }));
      if (!j.ok) { status.textContent = j.fehler || 'Anmeldung fehlgeschlagen.'; return; }
      store.token = j.ergebnis.token; lernIch = { rolle: j.ergebnis.rolle, name: j.ergebnis.name, lernender_id: j.ergebnis.lernender_id };
      route(lernIch.rolle === 'kind' ? 'reise' : 'lernen', lernIch.rolle === 'kind' ? lernIch.lernender_id : null);
    } catch (err) { status.textContent = err.message; }
  });
  main.replaceChildren(form);
  code.focus();
}

async function render() {
  renderGeneration++;
  const live = viewGuard();
  current = parseHash();
  if (!store.token && current.view !== 'login') { route('login'); return; }
  if (store.token && !lernIch && current.view !== 'login') {
    try { lernIch = await lernCall('schule_ich'); } catch (e) { if (!store.token) return; main.replaceChildren(el('div', { class: 'card err-text' }, 'Fehler: ' + e.message)); return; }
    if (!live()) return;
  }
  // Kinder kommen nur in ihre eigene Lernreise.
  if (lernIch?.rolle === 'kind' && !KIND_ANSICHTEN.includes(current.view)) { route('reise', lernIch.lernender_id); return; }
  const views = { login: viewLogin, lernen: viewLernen, lerneinheit: viewLernEinheit, reise: viewReise, weltkarte: viewWeltkarte, reisepass: viewReisepass,
    weg: viewWeg, merkheft: viewMerkheft, wiederholen: viewWiederholen, plan: viewPlan, rueckmeldungen: viewRueckmeldungen, zugaenge: viewZugaenge };
  const fn = views[current.view] || (() => route('lernen'));
  try { await fn(current.arg); } catch (e) { if (live()) showError(e); }
}

$('#ver').textContent = 'v' + APP_VERSION;
render();
