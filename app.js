/* KI-System – Rohbau der Web-/Handy-App (Werkstatt #4).
   Spricht ausschließlich mit app-api (Supabase). Kein Schlüssel im Code.
   Schreibende Aktionen laufen nur nach einem Klick von Sebastian. */
'use strict';

const APP_VERSION = '0.2.1';
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


// ---------- Hilfetexte (ⓘ-Knöpfe) ----------
const HILFE = {
  kostenlimit: { titel: 'Kostenlimit',
    text: 'Obergrenze in USD für den ganzen Auftrag (alle Runden, Ergebnis, Belege, Bewertung). Der Motor rechnet vor jeder Runde die Höchstkosten aus; würde das Limit reißen, pausiert er – du kannst dann mit höherem Limit fortsetzen. Dein Wert wird als Vorgabe für künftige Aufträge gespeichert.',
    rang: ['2 USD – normale Frage, 3 Teilnehmer (Standard)', '3–5 USD – lange Vorgaben, 4 Teilnehmer oder 3 Kritikrunden', '1 USD – kurze Frage, schnelle Zweitmeinung'] },
  runden: { titel: 'Max. Kritikrunden',
    text: 'Nach der blinden Entwurfsrunde prüfen die Pläne sich gegenseitig. Jede Kritikrunde kostet etwa so viel wie die Entwurfsrunde. Endet früher, wenn niemand mehr neue Einwände meldet.',
    rang: ['2 – Standard: Kritik und Antwort darauf', '1 – schnell und günstig, nur eine Prüfschleife', '3 – strittige oder teure Entscheidungen', '0 – nur Entwürfe und Zusammenfassung, keine Prüfung'] },
  stufe: { titel: 'Stufe',
    text: 'Stufe 3: läuft automatisch bis zum Ergebnis durch. Stufe 2: stoppt vor jeder Kritikrunde; du siehst die Zwischenstände unter „Verlauf“ und gibst mit „Fortsetzen“ frei – oder brichst ab.',
    rang: ['Stufe 3 – Standard, du bekommst das fertige Ergebnis', 'Stufe 2 – bei hohem Kostenlimit oder wenn du die Richtung früh prüfen willst'] },
  haltbarkeit: { titel: 'Haltbarkeit',
    text: 'Wie lange der Verlauf (alle Beiträge der Runden) aufbewahrt wird. Ergebnis, Bewertung und gespeicherte Erkenntnisse bleiben immer erhalten.',
    rang: ['projekt – Standard: bleibt, solange das Projekt läuft', 'dauerhaft – Verlauf nie löschen (Grundsatzfragen, Vorlagen)', 'einmalig – Verlauf wird 30 Tage nach Abschluss gelöscht'] },
  stammdaten: { titel: 'Stammdaten freigeben',
    text: 'Gespeicherte Angaben zu Personen und Haushalt, die die KIs nur für diesen Auftrag sehen dürfen. Modelle ohne Stammdaten-Freigabe (z. B. Mistral) bekommen stattdessen Platzhalter wie [Person 1] oder [Jahr]. Nie-externe Daten (Reisedokumente, Kontakte) sind gesperrt.',
    rang: ['Nur anhaken, was die Frage wirklich braucht', 'Nichts anhaken, wenn die Frage allgemein ist'] },
  besetzung: { titel: 'Besetzung',
    text: 'Welches Modell welche Rolle spielt. Jede Zeile wird ein Plan (A, B, C …). Planer liefern Lösungen, Gegenanwalt/Kritiker greifen an, Fachrollen bringen Spezialwissen. Verschiedene Modellfamilien bringen verschiedene Sichtweisen. Das System sammelt Noten je Modell und Rolle – die Start-KI nutzt sie für den Vorschlag.',
    rang: ['3 Teilnehmer: 2 Planer + 1 Gegenanwalt (Standard)', '4 Teilnehmer: zusätzlich eine Fachrolle', 'Mindestens 2 Teilnehmer, sonst kein Council'] },
  pflichtfragen: { titel: 'Pflichtfragen',
    text: 'Fragen der Start-KI an dich, deren Antwort die Qualität spürbar verbessert. Die Antworten gehen als Pflichtangaben in den Auftrag. Leer lassen ist erlaubt – dann arbeiten die KIs mit Annahmen und kennzeichnen sie.',
    rang: ['Kurz antworten reicht – Stichworte genügen', 'Fragen löschen, die nicht passen; eigene mit „+ Frage“ ergänzen'] },
  projekt: { titel: 'Projekt',
    text: 'Ordnet den Auftrag einem Bereich zu. Erkenntnisse aus früheren Aufträgen desselben Projekts werden den KIs mitgegeben, und die Haltbarkeit „projekt“ bezieht sich darauf. Die Start-KI hat es aus deiner Frage erkannt; du kannst es ändern oder ein neues anlegen.' },
  frage: { titel: 'Frage',
    text: 'Schreib so, wie du es einem Berater sagen würdest: Was willst du entscheiden, was weißt du schon (Zahlen, Termine, Rahmen), was ist dir wichtig? Je mehr Kontext, desto weniger Pflichtfragen und desto besser der Entwurf.' },
};
function hilfeKnopf(key) {
  const h = HILFE[key]; if (!h) return null;
  const btn = el('button', { type: 'button', class: 'info-btn', 'aria-label': 'Erklärung: ' + h.titel, title: h.titel }, 'i');
  btn.addEventListener('click', (e) => {
    e.preventDefault(); e.stopPropagation();
    const alt = document.querySelector('.hint-box'); if (alt) { const same = alt.dataset.key === key; alt.remove(); if (same) return; }
    const box = el('div', { class: 'hint-box', 'data-key': key },
      el('div', { class: 'row' }, el('b', {}, h.titel), el('button', { type: 'button', class: 'link right', onclick: () => box.remove() }, 'Schließen')),
      el('p', {}, h.text),
      h.rang ? el('ol', { class: 'hint-rang' }, h.rang.map((r) => el('li', {}, r))) : null);
    const anker = btn.closest('label, h2, .row, .card') || btn.parentElement;
    anker.insertAdjacentElement(anker.tagName === 'LABEL' || anker.tagName === 'H2' ? 'afterend' : 'beforeend', box);
  });
  return btn;
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

// ---------- Ansicht: Neuer Auftrag (Werkstatt #11: Frage rein, Entwurf raus) ----------
let neuEntwurf = null; // letzter Entwurf der Start-KI (bleibt beim Tabwechsel erhalten)

async function viewNeu() {
  setChrome('Neuer Auftrag', { tab: 'neu' });
  if (neuEntwurf) { zeigeEntwurf(neuEntwurf); return; }
  loading();
  const einst = await aktion('einstellungen_lesen', {});
  const standardLimit = Number(einst?.standard_kostenlimit?.wert ?? 2) || 2;

  const frage = el('textarea', { required: true, placeholder: 'Deine Frage so, wie du sie stellen würdest – mit allem, was du schon weißt (Rahmen, Zahlen, Termine).', style: 'min-height:140px' });
  const limit = el('input', { type: 'number', step: '0.5', min: '0.5', value: String(standardLimit) });
  const btn = el('button', { type: 'submit', class: 'primary' }, 'Auftrag vorbereiten');
  const form = el('form', { class: 'card' },
    el('h2', {}, 'Was soll das Council klären?'),
    el('label', {}, 'Frage ', hilfeKnopf('frage'), frage),
    el('div', { class: 'row' },
      el('label', { class: 'grow' }, 'Kostenlimit (USD) – bleibt als Vorgabe gespeichert ', hilfeKnopf('kostenlimit'), limit)),
    el('p', { class: 'muted small' }, 'Die Start-KI erkennt das Projekt, baut Titel, Ziel, Vorgaben, Grenzen und Ergebnisform, stellt dir Pflichtfragen und schlägt die Besetzung vor. Du prüfst alles und startest dann per Klick. Kosten der Vorbereitung: meist unter 0,05 USD.'),
    el('div', { class: 'actions' }, btn),
  );
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (frage.value.trim().length < 5) { toast('Bitte eine Frage eingeben', true); return; }
    btn.disabled = true; btn.textContent = 'Start-KI arbeitet …';
    try {
      const r = await http('/vorbereiten', { method: 'POST', body: { frage: frage.value.trim(), kostenlimit: Number(limit.value) } });
      if (!r.ok) throw new Error(r.fehler || 'Vorbereitung fehlgeschlagen');
      neuEntwurf = { ...r, kostenlimit: Number(limit.value) || standardLimit, standardLimit };
      toast(`Entwurf erstellt (${r.start_ki}${r.kosten_usd != null ? ', ' + Number(r.kosten_usd).toFixed(3) + ' USD' : ''})`);
      zeigeEntwurf(neuEntwurf);
    } catch (err) { toast(err.message, true); btn.disabled = false; btn.textContent = 'Auftrag vorbereiten'; }
  });
  main.replaceChildren(form);
}

async function zeigeEntwurf(d) {
  const ent = d.entwurf;
  const f = {
    projekt: el('select', {}, (d.projekte || []).map((p) => el('option', { value: p }, p)), el('option', { value: '__neu' }, '+ Neues Projekt …')),
    projektNeu: el('input', { type: 'text', placeholder: 'Name des neuen Projekts', hidden: true }),
    titel: el('input', { type: 'text', value: ent.titel || '', maxlength: 120 }),
    ziel: el('textarea', {}, ent.ziel || ''),
    vorgaben: el('textarea', { style: 'min-height:110px' }, ent.vorgaben || ''),
    grenzen: el('textarea', {}, ent.grenzen || ''),
    ergebnisform: el('textarea', {}, ent.ergebnisform || ''),
    limit: el('input', { type: 'number', step: '0.5', min: '0.5', value: String(d.kostenlimit) }),
    runden: el('input', { type: 'number', min: '0', max: '10', value: String(ent.max_kritikrunden ?? 2) }),
    stufe: el('select', {}, el('option', { value: '3' }, 'Stufe 3 – durchlaufen'), el('option', { value: '2' }, 'Stufe 2 – vor jeder Kritikrunde stoppen')),
    haltbarkeit: el('select', {}, ['einmalig', 'projekt', 'dauerhaft'].map((h) => el('option', { value: h, selected: h === 'projekt' ? true : null }, h))),
  };
  f.haltbarkeit.value = 'projekt';
  // Projekt: erkanntes vorwählen, neues anlegen lassen
  if (ent.projekt && (d.projekte || []).includes(ent.projekt)) f.projekt.value = ent.projekt;
  else if (ent.projekt) { f.projekt.value = '__neu'; f.projektNeu.hidden = false; f.projektNeu.value = ent.projekt; }
  f.projekt.addEventListener('change', () => { f.projektNeu.hidden = f.projekt.value !== '__neu'; });

  // Pflichtfragen mit Antwortfeldern
  const pfBox = el('div');
  const addPf = (frage = '', antwort = '') => pfBox.append(el('div', { class: 'card', style: 'padding:10px 12px' },
    el('div', { class: 'row' }, el('input', { class: 'pf-frage grow', type: 'text', value: frage, placeholder: 'Frage' }), el('button', { type: 'button', onclick: (e) => e.target.closest('.card').remove() }, '✕')),
    el('input', { class: 'pf-antwort', type: 'text', value: antwort, placeholder: 'Deine Antwort', style: 'margin-top:6px' })));
  for (const p of ent.pflichtfragen || []) addPf(p.frage, p.antwort_vorschlag || '');

  // Besetzung
  const tnBox = el('div');
  const addTn = (teilnehmer = '', rolle = '', begruendung = '') => {
    const row = el('div', { class: 'card', style: 'padding:10px 12px' },
      el('div', { class: 'teilnehmer-row' },
        el('select', { class: 'tn-modell' }, el('option', { value: '' }, '– Modell –'), (d.teilnehmer || []).map((t) => el('option', { value: t.name, selected: t.name === teilnehmer ? true : null }, t.name + (t.stammdaten_erlaubt ? '' : ' (keine Stammdaten)')))),
        el('select', { class: 'tn-rolle' }, el('option', { value: '' }, '– Rolle (Standard: Planer) –'), (d.rollen || []).map((r) => el('option', { value: r.name, selected: r.name === rolle ? true : null }, r.name))),
        el('button', { type: 'button', onclick: () => row.remove() }, '✕')),
      begruendung ? el('div', { class: 'muted small' }, begruendung) : null);
    tnBox.append(row);
  };
  for (const b of ent.besetzung || []) addTn(b.teilnehmer, b.rolle || '', b.begruendung);
  if (!(ent.besetzung || []).length) { addTn(); addTn(); addTn(); }

  // Stammdaten
  const sdBox = el('div', { class: 'muted small' }, 'Lade Stammdaten …');
  aktion('stammdaten_lesen', {}).then((sd) => {
    const eintraege = Array.isArray(sd) ? sd : (sd.stammdaten || sd.eintraege || []);
    sdBox.replaceChildren();
    if (!eintraege.length) { sdBox.append('Keine Stammdaten vorhanden.'); return; }
    for (const s of eintraege) sdBox.append(el('label', { style: 'display:flex;align-items:center;color:inherit;margin:4px 0' },
      el('input', { type: 'checkbox', class: 'sd', value: s.id, style: 'width:auto;margin-right:8px', disabled: s.nie_extern ? true : null }),
      `${s.art || ''}: ${s.bezeichnung || ''}${s.person ? ' (' + s.person + ')' : ''}${s.nie_extern ? ' – gesperrt' : ''}`));
  }).catch((e) => sdBox.replaceChildren(el('span', { class: 'err-text' }, e.message)));

  const limitHinweis = ent.kostenlimit_vorschlag && Number(ent.kostenlimit_vorschlag) !== Number(d.kostenlimit)
    ? el('p', { class: 'small', style: 'color:var(--warn)' }, `Die Start-KI schlägt ${Number(ent.kostenlimit_vorschlag).toFixed(2)} USD vor (deine Vorgabe: ${Number(d.kostenlimit).toFixed(2)} USD).`) : null;

  async function anlegen(starten) {
    const teilnehmer = [...tnBox.querySelectorAll('.teilnehmer-row')].map((row, i) => ({
      teilnehmer: row.querySelector('.tn-modell').value, rolle: row.querySelector('.tn-rolle').value || undefined, plan_label: 'Plan ' + String.fromCharCode(65 + i),
    })).filter((t) => t.teilnehmer);
    if (teilnehmer.length < 2) throw new Error('Mindestens 2 Teilnehmer wählen');
    if (!f.titel.value.trim()) throw new Error('Titel fehlt');
    const projekt = f.projekt.value === '__neu' ? f.projektNeu.value.trim() : f.projekt.value;
    const kostenlimit = Number(f.limit.value) || d.kostenlimit;
    if (kostenlimit !== Number(d.standardLimit)) {
      await aktion('einstellung_setzen', { name: 'standard_kostenlimit', wert: kostenlimit }).catch(() => { /* Vorgabe nicht gespeichert – Auftrag trotzdem anlegen */ });
    }
    const daten = {
      titel: f.titel.value.trim(), originalfrage: ent.originalfrage, kostenlimit_usd: kostenlimit, teilnehmer,
      projekt: projekt || undefined, ziel: f.ziel.value.trim() || undefined, vorgaben: f.vorgaben.value.trim() || undefined,
      grenzen: f.grenzen.value.trim() || undefined, ergebnisform: f.ergebnisform.value.trim() || undefined,
      haltbarkeit: f.haltbarkeit.value, automatisierungsstufe: Number(f.stufe.value), max_kritikrunden: Number(f.runden.value),
      vorschlaege_stamm_ki: { start_ki: d.start_ki, hinweise: ent.hinweise || '', kostenlimit_vorschlag: ent.kostenlimit_vorschlag },
    };
    for (const k of Object.keys(daten)) if (daten[k] === undefined) delete daten[k];
    const r = await aktion('rahmen_anlegen', daten);
    const id = r?.rahmen_id;
    if (!id) throw new Error('Auftrag angelegt, aber keine Nummer erhalten');
    const angaben = [...pfBox.querySelectorAll('.card')].map((c) => ({ frage: c.querySelector('.pf-frage').value.trim(), antwort: c.querySelector('.pf-antwort').value.trim(), pflicht: true })).filter((a) => a.frage);
    if (angaben.length) await aktion('angaben_setzen', { rahmen_id: id, angaben });
    const ids = [...sdBox.querySelectorAll('input.sd:checked')].map((c) => Number(c.value));
    if (ids.length) await aktion('stammdaten_freigeben', { rahmen_id: id, ids });
    if (starten) await aktion('auftrag_starten', { rahmen_id: id, stufe: Number(f.stufe.value) });
    neuEntwurf = null;
    toast(starten ? `Auftrag ${id} gestartet` : `Entwurf ${id} gespeichert`);
    route('auftrag', id);
  }

  const seite = el('div', {},
    el('div', { class: 'card' },
      el('h2', {}, 'Entwurf der Start-KI – bitte prüfen'),
      el('p', { class: 'muted small' }, `${d.start_ki || ''}${d.kosten_usd != null ? ' · ' + Number(d.kosten_usd).toFixed(3) + ' USD' : ''}`),
      ent.hinweise ? el('p', { class: 'small' }, el('b', {}, 'Hinweis der Start-KI: '), ent.hinweise) : null,
      el('label', {}, 'Projekt ', hilfeKnopf('projekt'), f.projekt), f.projektNeu,
      el('label', {}, 'Titel', f.titel),
      el('label', {}, 'Originalfrage'), el('p', { class: 'small', style: 'white-space:pre-wrap;margin:0' }, ent.originalfrage),
      el('label', {}, 'Ziel', f.ziel), el('label', {}, 'Vorgaben', f.vorgaben), el('label', {}, 'Grenzen', f.grenzen), el('label', {}, 'Ergebnisform', f.ergebnisform)),
    el('div', { class: 'card' }, el('h2', {}, 'Pflichtfragen an dich ', hilfeKnopf('pflichtfragen')), el('p', { class: 'muted small' }, 'Je besser die Antworten, desto besser das Ergebnis. Leere Antworten sind erlaubt.'), pfBox,
      el('button', { type: 'button', class: 'link', onclick: () => addPf() }, '+ Frage')),
    el('div', { class: 'card' }, el('h2', {}, 'Besetzung (Vorschlag) ', hilfeKnopf('besetzung')), tnBox, el('button', { type: 'button', class: 'link', onclick: () => addTn() }, '+ Teilnehmer')),
    el('div', { class: 'card' }, el('h2', {}, 'Ablauf und Kosten'),
      el('div', { class: 'row' }, el('label', { class: 'grow' }, 'Kostenlimit (USD) ', hilfeKnopf('kostenlimit'), f.limit), el('label', { class: 'grow' }, 'Max. Kritikrunden ', hilfeKnopf('runden'), f.runden)),
      limitHinweis,
      el('div', { class: 'row' }, el('label', { class: 'grow' }, 'Stufe ', hilfeKnopf('stufe'), f.stufe), el('label', { class: 'grow' }, 'Haltbarkeit ', hilfeKnopf('haltbarkeit'), f.haltbarkeit))),
    el('div', { class: 'card' }, el('h2', {}, 'Stammdaten freigeben ', hilfeKnopf('stammdaten')), el('p', { class: 'muted small' }, 'Nur anhaken, was die KIs für diese Frage brauchen.'), sdBox),
    el('div', { class: 'actions', style: 'margin-bottom:24px' },
      confirmButton('Anlegen und starten', async () => { try { await anlegen(true); } catch (e) { toast(e.message, true); } }, 'primary'),
      el('button', { onclick: async () => { try { await anlegen(false); } catch (e) { toast(e.message, true); } } }, 'Nur als Entwurf speichern'),
      el('button', { class: 'danger', onclick: () => { neuEntwurf = null; render(); } }, 'Verwerfen')),
  );
  main.replaceChildren(seite);
  window.scrollTo(0, 0);
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
