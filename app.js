/* KI-System – Rohbau der Web-/Handy-App (Werkstatt #4).
   Spricht ausschließlich mit app-api (Supabase). Kein Schlüssel im Code.
   Schreibende Aktionen laufen nur nach einem Klick von Sebastian. */
'use strict';

const APP_VERSION = '0.5.0';
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
  teilfragen: { titel: 'Teilfragen',
    text: 'Die Start-KI zerlegt deine Frage in einzelne, konkret beantwortbare Teilfragen. Jeder Teilnehmer muss jede Teilfrage ausdrücklich beantworten, das Ergebnis zeigt die Antwort je Teilfrage, und ein neutraler Prüfer stuft ein: voll / teilweise / offen beantwortet. Bleibt etwas offen, läuft automatisch genau eine Nachrunde dafür.',
    rang: ['2–4 Teilfragen – das, was du wirklich wissen willst', 'Fehlende ergänzen, unpassende löschen – das steuert, was geprüft wird'] },
  websuche: { titel: 'Websuche',
    text: 'Die Teilnehmer bekommen über OpenRouter eine Websuche (5 Treffer je Anfrage, ca. 0,02 USD) und müssen konkrete Angaben – Anbieter, Preise, Regeln – im Netz prüfen und mit Quelle (URL, Datum) belegen. Ohne Websuche bleibt alles Zeitkritische „ungeprüft“. Datenschutz: Teilnehmer, die freigegebene Stammdaten im Text haben, suchen nicht; alle anderen sehen ohnehin nur Platzhalter.',
    rang: ['An – Standard; bei Recherchefragen Pflicht', 'Aus – reine Abwägungs- oder Strukturfragen ohne aktuelle Fakten'] },
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

async function http(path, { method = 'GET', body, auth = true, signal } = {}) {
  const headers = { 'Content-Type': 'application/json' };
  if (auth && store.token) headers.Authorization = 'Bearer ' + store.token;
  const r = await fetch(API + path, { method, headers, body: body ? JSON.stringify(body) : undefined, signal });
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
let disposeSuche = () => {};

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
  disposeSuche();
  disposeSuche = () => {};
  current = parseHash();
  if (!store.token && current.view !== 'login') { route('login'); return; }
  const views = { login: viewLogin, auftraege: viewAuftraege, auftrag: viewAuftrag, neu: viewNeu, einstellungen: viewEinstellungen, werkstatt: viewWerkstatt, suche: viewSuche };
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
let detailTab = 'ergebnis';
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
  const tabsDef = [['ergebnis', 'Ergebnis'], ['uebersicht', 'Noten'], ['verlauf', 'Verlauf'], ['belege', 'Belege'], ['bewertung', 'Bewertung'], ['rahmen', 'Rahmen']];
  for (const [k, l] of tabsDef) sub.append(el('button', { class: k === detailTab ? 'on' : '', onclick: () => { detailTab = k; for (const b of sub.children) b.classList.toggle('on', b.textContent === l); zeige(); } }, l));

  const plaene = (r.teilnehmer || []).map((t) => t.plan_label).filter(Boolean);
  async function zeige() {
    inhalt.replaceChildren(el('div', { class: 'spinner' }, 'Lade …'));
    try {
      if (detailTab === 'ergebnis') {
        if (!r.ergebnis_vorhanden) { inhalt.replaceChildren(el('div', { class: 'card muted' }, r.status === 'laeuft' ? 'Das Council arbeitet noch – Zwischenstände unter „Verlauf“.' : 'Noch kein Ergebnis.')); return; }
        const e = await aktion('ergebnis_lesen', { rahmen_id: id });
        const entsch = entscheidungsBlock(id, e.nutzer_entscheidung);
        inhalt.replaceChildren(...ergebnisAnsicht(e, entsch), entsch, urteilBlock(id, e.nutzer_urteil));
      } else if (detailTab === 'uebersicht') {
        if (!r.ergebnis_vorhanden) { inhalt.replaceChildren(el('div', { class: 'card muted' }, 'Noch kein Ergebnis.')); return; }
        const v = await aktion('verlauf_lesen', { rahmen_id: id, ebene: 'uebersicht' });
        inhalt.replaceChildren(el('div', { class: 'card' }, md(v.markdown)));
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

// ---------- Ergebnis mit Ampel (Werkstatt #12) ----------
const AMPEL = {
  einig: { cls: 'ampel-gruen', text: 'alle einig' },
  teils: { cls: 'ampel-gelb', text: 'teilweise einig' },
  uneinig: { cls: 'ampel-rot', text: 'uneinig' },
  offen: { cls: 'ampel-grau', text: 'nicht eingestuft' },
};
function ampel(stufe) { const a = AMPEL[stufe] || AMPEL.offen; return el('span', { class: 'ampel ' + a.cls }, el('span', { class: 'ampel-punkt' }), a.text); }

// ---------- Präsentation (Werkstatt #13/#14, Motor v11): Antwort · Uneinigkeit · Weiter ----------
// Die Seite für Sebastian steht zuerst; das Protokoll des Zusammenfassers folgt aufklappbar darunter.
function praesentationAnsicht(e, entsch) {
  const p = e.praesentation;
  const teile = [];
  if (!p) {
    if (e.praesentation_status === 'offen') teile.push(el('div', { class: 'card muted small' }, 'Die Kurzfassung für dich wird gerade erstellt (dauert ca. eine Minute) – unten steht schon das Protokoll.'));
    else if (e.praesentation_status === 'fehler') teile.push(el('div', { class: 'card err-text small' }, 'Kurzfassung konnte nicht erstellt werden: ' + (e.praesentation_hinweis || 'unbekannter Fehler') + '. Das Protokoll steht unten.'));
    return teile;
  }
  // 1 Deine Antwort
  const aus = Array.isArray(p.aussagen) ? p.aussagen : [];
  teile.push(el('div', { class: 'card pr-antwort' },
    el('h2', {}, 'Deine Antwort'),
    el('p', { class: 'pr-text' }, p.antwort || ''),
    aus.length ? el('ul', { class: 'pr-aussagen' }, aus.map((a) => el('li', { class: a.belegt === 'ja' ? 'belegt' : 'annahme' },
      el('span', { class: 'pr-mark', title: a.belegt === 'ja' ? 'belegt (Quelle im Protokoll)' : 'Annahme / Schätzung' }, a.belegt === 'ja' ? '✓' : '~'), el('span', {}, a.text)))) : null,
    aus.length ? el('p', { class: 'muted small pr-legende' }, '✓ belegt (Quelle unter „Belege & Protokoll“) · ~ Annahme oder Schätzung') : null,
    p.hinweis ? el('div', { class: 'erg-warnung' }, el('b', {}, 'Hinweis: '), p.hinweis) : null,
  ));
  // 2 Wo die KIs uneinig sind
  const st = Array.isArray(p.streit) ? p.streit : [];
  const stBox = el('div', { class: 'card' }, el('h2', {}, 'Wo die KIs uneinig sind'));
  if (!st.length) stBox.append(el('p', { class: 'muted small' }, 'Keine entscheidungsrelevante Uneinigkeit.'));
  for (const s of st) stBox.append(el('div', { class: 'sp sp-ampel-rot' },
    el('b', {}, s.thema || ''),
    s.mehrheit ? el('p', { class: 'small pr-pos' }, el('span', { class: 'pr-label' }, 'Die meisten: '), s.mehrheit) : null,
    s.gegenstimme ? el('p', { class: 'small pr-pos' }, el('span', { class: 'pr-label' }, 'Gegenstimme: '), s.gegenstimme) : null,
    s.bedeutung ? el('p', { class: 'pr-bedeutung' }, el('b', {}, 'Für dich: '), s.bedeutung) : null));
  teile.push(stBox);
  // 3 So geht es weiter
  const w = Array.isArray(p.weiter) ? p.weiter : [];
  if (w.length) teile.push(el('div', { class: 'card pr-weiter' }, el('h2', {}, 'So geht es weiter'),
    el('ol', { class: 'pr-schritte' }, w.map((x) => el('li', {}, el('span', {}, x.schritt), x.sofort ? el('span', { class: 'pill neu' }, 'sofort') : null))),
    el('p', { class: 'muted small' }, 'Antippen eines Schritts übernimmt ihn ins Entscheidungsfeld.'),
  ));
  for (const li of teile[teile.length - 1].querySelectorAll('.pr-schritte li')) li.addEventListener('click', () => {
    const ta = entsch.querySelector('textarea'); ta.value = li.firstChild.textContent; entsch.scrollIntoView({ behavior: 'smooth', block: 'center' }); ta.focus();
  });
  return teile;
}

function ergebnisAnsicht(e, entsch) {
  const praes = praesentationAnsicht(e, entsch);
  const protokoll = protokollAnsicht(e, entsch);
  if (!e.praesentation) return [...praes, ...protokoll];
  // Mit Präsentation: Entscheidungsvorschläge bleiben sichtbar, der Rest des Protokolls ist aufklappbar
  const ev = protokoll.find((x) => x.dataset.block === 'entscheidungen');
  const rest = protokoll.filter((x) => x.dataset.block !== 'entscheidungen');
  const det = el('details', { class: 'card pr-details' }, el('summary', {}, el('b', {}, 'Belege & Protokoll'), el('span', { class: 'muted small' }, ' – Empfehlung des Zusammenfassers, Ampel, Quellen, alle Streitpunkte')), ...rest);
  return [...praes, ev, det].filter(Boolean);
}

function protokollAnsicht(e, entsch) {
  const basis = Array.isArray(e.gemeinsame_basis) ? e.gemeinsame_basis : [];
  const sp = Array.isArray(e.streitpunkte) ? e.streitpunkte : [];
  const stufe = (x) => (x?.einigkeit === 'teils' || x?.einigkeit === 'uneinig') ? x.einigkeit : 'offen';
  const nTeils = sp.filter((x) => stufe(x) === 'teils').length, nUneinig = sp.filter((x) => stufe(x) === 'uneinig').length, nOffen = sp.length - nTeils - nUneinig;
  const alt = !basis.length && sp.length && nOffen === sp.length; // Ergebnis vor Motor v9: keine Einigkeits-Auswertung
  const teile = [];

  // Kopf: Antwort + Zähler
  teile.push(el('div', { class: 'card erg-antwort' },
    el('div', { class: 'row ampel-leiste' },
      el('span', { class: 'ampel ampel-gruen' }, el('span', { class: 'ampel-punkt' }), `${basis.length} einig`),
      el('span', { class: 'ampel ampel-gelb' }, el('span', { class: 'ampel-punkt' }), `${nTeils} teils`),
      el('span', { class: 'ampel ampel-rot' }, el('span', { class: 'ampel-punkt' }), `${nUneinig} uneinig`),
      nOffen ? el('span', { class: 'ampel ampel-grau' }, el('span', { class: 'ampel-punkt' }), `${nOffen} ohne Einstufung`) : null),
    el('h2', {}, e.praesentation ? 'Empfehlung des Zusammenfassers' : 'Antwort des Councils'),
    el('p', { class: 'erg-empfehlung' }, e.empfehlung || '(keine Empfehlung)'),
    e.uebergabe && e.uebergabe !== e.empfehlung ? el('details', {}, el('summary', { class: 'muted small' }, 'Übergabe (Kurzfassung für die Weiterarbeit)'), el('p', { class: 'small', style: 'white-space:pre-wrap' }, e.uebergabe)) : null,
    alt ? el('p', { class: 'muted small' }, 'Dieses Ergebnis entstand vor der Einigkeits-Auswertung (Motor v9) – Ampel nur für neue Aufträge.') : null,
  ));

  // Antwort je Teilfrage mit Abdeckung (Prüfer) – Werkstatt #13a
  const ajt = Array.isArray(e.antworten_je_teilfrage) ? e.antworten_je_teilfrage : [];
  const abd = Array.isArray(e.abdeckung) ? e.abdeckung : [];
  const ABD = { voll: ['ampel-gruen', 'voll beantwortet'], teilweise: ['ampel-gelb', 'teilweise beantwortet'], offen: ['ampel-rot', 'offen'] };
  if (ajt.length) {
    const statusText = { bestanden: 'Alle Teilfragen sind konkret beantwortet.', teilweise: 'Einige Teilfragen sind nur allgemein beantwortet.', nicht_bestanden: 'Mindestens eine Teilfrage ist unbeantwortet.' }[e.abdeckung_status] || 'Prüfung durch die Bewerter-KI steht noch aus.';
    const box = el('div', { class: 'card' },
      el('h2', {}, 'Deine Fragen – einzeln beantwortet'),
      el('p', { class: 'muted small' }, statusText + (e.nachlauf ? ' Eine Nachrunde für offene Teilfragen wurde durchgeführt.' : '')));
    for (const a of ajt) {
      const pr = abd.find((x) => Number(x.nr) === Number(a.nr));
      const st = pr?.stufe || a.abdeckung || 'offen';
      const [cls, txt] = ABD[st] || ABD.offen;
      box.append(el('div', { class: 'sp sp-' + cls },
        el('div', { class: 'row' }, el('span', { class: 'ampel ' + cls }, el('span', { class: 'ampel-punkt' }), txt), el('b', { class: 'grow' }, `${a.nr}. ${a.frage || ''}`)),
        el('p', { class: 'sp-kern' }, a.antwort || '–'),
        pr?.begruendung ? el('p', { class: 'muted small' }, 'Prüfer: ' + pr.begruendung) : null));
    }
    teile.push(box);
  }

  // Grün: gemeinsame Basis
  teile.push(el('div', { class: 'card erg-gruen' },
    el('h2', {}, ampel('einig'), ' Darauf sind sich alle einig – deine Arbeitsgrundlage'),
    basis.length
      ? el('ul', { class: 'erg-liste' }, basis.map((b) => el('li', {}, el('span', {}, b.aussage || String(b)),
          b.belegt !== undefined ? el('span', { class: 'pill ' + (String(b.belegt) === 'ja' || b.belegt === true ? 'neu' : 'wartet') }, String(b.belegt) === 'ja' || b.belegt === true ? 'belegt' : 'unbelegt') : null,
          b.grund ? el('div', { class: 'muted small' }, b.grund) : null)))
      : el('p', { class: 'muted small' }, alt ? 'Keine Auswertung vorhanden.' : 'Keinen Punkt tragen alle Pläne gemeinsam.'),
    e.konsens_warnung ? el('div', { class: 'erg-warnung' }, el('b', {}, 'Konsens-Warnung: '), e.konsens_warnung) : null,
  ));

  // Gelb/Rot: Streitpunkte
  const spBox = el('div', { class: 'card' }, el('h2', {}, 'Streitpunkte'));
  if (!sp.length) spBox.append(el('p', { class: 'muted small' }, 'Keine Streitpunkte.'));
  for (const x of [...sp].sort((a, b) => ({ uneinig: 0, teils: 1, offen: 2 })[stufe(a)] - ({ uneinig: 0, teils: 1, offen: 2 })[stufe(b)])) {
    const st = stufe(x);
    spBox.append(el('div', { class: 'sp sp-' + (AMPEL[st].cls) },
      el('div', { class: 'row' }, ampel(st), el('b', { class: 'grow' }, x.thema || '')),
      x.kern ? el('p', { class: 'sp-kern' }, x.kern) : null,
      el('details', {}, el('summary', { class: 'small' }, 'Positionen der Pläne'),
        x.plan_a ? el('p', { class: 'small' }, el('b', {}, 'Plan A: '), x.plan_a) : null,
        x.plan_b ? el('p', { class: 'small' }, el('b', {}, 'Plan B: '), x.plan_b) : null,
        x.weitere ? el('p', { class: 'small' }, el('b', {}, 'Weitere: '), x.weitere) : null)));
  }
  teile.push(spBox);

  // Alternativen mit Vor-/Nachteilen
  const alts = Array.isArray(e.alternativen) ? e.alternativen : [];
  if (alts.length) teile.push(el('div', { class: 'card' }, el('h2', {}, 'Alternativen'),
    el('div', { class: 'ev-liste' }, alts.map((a) => el('div', { class: 'sp sp-ampel-grau' }, el('b', {}, a.name || ''),
      el('div', { class: 'row', style: 'align-items:flex-start;gap:16px;margin-top:6px' },
        el('div', { class: 'grow small' }, el('span', { class: 'ampel ampel-gruen' }, 'dafür'), el('ul', { class: 'erg-liste' }, (a.vorteile || []).map((v) => el('li', {}, v)))),
        el('div', { class: 'grow small' }, el('span', { class: 'ampel ampel-rot' }, 'dagegen'), el('ul', { class: 'erg-liste' }, (a.nachteile || []).map((v) => el('li', {}, v))))))))));

  // Entscheidungsvorschläge -> füllen das Entscheidungsfeld
  const ev = Array.isArray(e.entscheidungsvorschlaege) ? e.entscheidungsvorschlaege : [];
  if (ev.length) teile.push(el('div', { class: 'card', 'data-block': 'entscheidungen' }, el('h2', {}, 'Entscheidungsvorschläge'),
    el('p', { class: 'muted small' }, 'Antippen übernimmt den Vorschlag ins Entscheidungsfeld unten – du kannst ihn dort noch ändern.'),
    el('div', { class: 'ev-liste' }, ev.map((v) => el('button', { type: 'button', class: 'ev', onclick: () => { const ta = entsch.querySelector('textarea'); ta.value = (v.label || '') + (v.beschreibung ? ' – ' + v.beschreibung : ''); entsch.scrollIntoView({ behavior: 'smooth', block: 'center' }); ta.focus(); } },
      el('b', {}, v.label || ''), v.beschreibung ? el('span', { class: 'small muted' }, ' ' + v.beschreibung) : null)))));

  // Fakten / Annahmen / offene Fragen (zugeklappt)
  const fakten = Array.isArray(e.fakten) ? e.fakten : [], annahmen = Array.isArray(e.annahmen) ? e.annahmen : [], fragen = Array.isArray(e.offene_fragen) ? e.offene_fragen : [];
  teile.push(el('div', { class: 'card' },
    el('details', { open: fakten.length ? true : null }, el('summary', {}, el('b', {}, `Fakten (${fakten.length})`), el('span', { class: 'muted small' }, ' – mit Quelle und Stand')),
      fakten.length ? el('ul', { class: 'erg-liste' }, fakten.map((f) => el('li', {}, f.aussage || String(f), (f.quelle || f.stand) ? el('div', { class: 'muted small' }, [f.quelle, f.stand].filter(Boolean).join(' · ')) : null))) : el('p', { class: 'muted small' }, 'keine')),
    el('details', {}, el('summary', {}, el('b', {}, `Annahmen (${annahmen.length})`), el('span', { class: 'muted small' }, ' – nicht belegt')),
      annahmen.length ? el('ul', { class: 'erg-liste' }, annahmen.map((a) => el('li', {}, typeof a === 'string' ? a : (a.aussage || JSON.stringify(a))))) : el('p', { class: 'muted small' }, 'keine')),
    el('details', {}, el('summary', {}, el('b', {}, `Offene Fragen (${fragen.length})`)),
      fragen.length ? el('ul', { class: 'erg-liste' }, fragen.map((f) => el('li', {}, typeof f === 'string' ? f : JSON.stringify(f)))) : el('p', { class: 'muted small' }, 'keine')),
  ));
  return teile;
}

function entscheidungsBlock(id, bisher) {
  const ta = el('textarea', { placeholder: 'Deine Entscheidung zum Ergebnis, z. B. „Plan B übernehmen, Probewoche ab 20.10.“' });
  return el('div', { class: 'card' }, el('h2', {}, 'Entscheidung festhalten'),
    bisher ? el('p', { class: 'small' }, el('b', {}, 'Bisher festgehalten: '), bisher) : null,
    el('p', { class: 'muted small' }, 'Wird im System gespeichert und setzt das Ergebnis im Posteingang auf erledigt.'),
    ta, el('div', { class: 'actions' }, confirmButton('Entscheidung speichern', async () => {
      if (!ta.value.trim()) { toast('Bitte Text eingeben', true); return; }
      try { await aktion('nutzer_entscheidung', { rahmen_id: id, entscheidung: ta.value.trim() }); toast('Gespeichert'); ta.value = ''; } catch (e) { toast(e.message, true); }
    }, 'primary')));
}
function urteilBlock(id, bisher) {
  const kom = el('input', { type: 'text', placeholder: 'Kommentar (optional)' });
  const row = el('div', { class: 'actions' });
  if (bisher) row.append(el('span', { class: 'muted small' }, `Dein Urteil bisher: ${bisher}`));
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
    websuche: el('input', { type: 'checkbox', style: 'width:auto;margin-right:8px' }),
  };
  f.websuche.checked = d.websuche_standard !== false;
  const rb = ent.recherchebedarf || 'teilweise';
  const rbText = { keine: 'Die Frage braucht kaum aktuelle Fakten aus dem Netz.', teilweise: 'Einige Angaben sollten die Teilnehmer im Netz prüfen.', hoch: 'Die Antwort hängt stark von aktuellen Fakten ab (Anbieter, Preise, Regeln) – Websuche dringend empfohlen.' }[rb];
  const websucheBlock = el('div', { class: 'card ' + (rb === 'hoch' ? 'erg-warnung' : '') },
    el('h2', {}, 'Websuche ', hilfeKnopf('websuche')),
    el('p', { class: 'small' }, el('b', {}, 'Recherchebedarf laut Start-KI: ' + rb + '. '), rbText),
    el('label', { style: 'display:flex;align-items:center;color:inherit' }, f.websuche, 'Teilnehmer dürfen im Netz suchen (ca. 0,02 USD je Aufruf)'),
    el('p', { class: 'muted small', id: 'websuche-hinweis' }, 'Teilnehmer, die freigegebene Stammdaten sehen, suchen nicht im Netz – so gelangen keine persönlichen Angaben in Suchanfragen.'));
  f.haltbarkeit.value = 'projekt';
  // Projekt: erkanntes vorwählen, neues anlegen lassen
  if (ent.projekt && (d.projekte || []).includes(ent.projekt)) f.projekt.value = ent.projekt;
  else if (ent.projekt) { f.projekt.value = '__neu'; f.projektNeu.hidden = false; f.projektNeu.value = ent.projekt; }
  f.projekt.addEventListener('change', () => { f.projektNeu.hidden = f.projekt.value !== '__neu'; });

  // Teilfragen (atomar, jede muss im Ergebnis beantwortet werden)
  const tfBox = el('div');
  const addTf = (frage = '') => tfBox.append(el('div', { class: 'row', style: 'margin-bottom:6px' },
    el('span', { class: 'muted small tf-nr' }, String(tfBox.children.length + 1) + '.'),
    el('input', { class: 'tf-frage grow', type: 'text', value: frage, placeholder: 'Teilfrage' }),
    el('button', { type: 'button', onclick: (e) => { e.target.closest('.row').remove(); [...tfBox.querySelectorAll('.tf-nr')].forEach((n, i) => n.textContent = (i + 1) + '.'); } }, '✕')));
  for (const t of ent.teilfragen || []) addTf(t);

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
    const teilfragen = [...tfBox.querySelectorAll('.tf-frage')].map((i) => i.value.trim()).filter((t) => t.length > 5);
    const daten = {
      titel: f.titel.value.trim(), originalfrage: ent.originalfrage, kostenlimit_usd: kostenlimit, teilnehmer, teilfragen,
      projekt: projekt || undefined, ziel: f.ziel.value.trim() || undefined, vorgaben: f.vorgaben.value.trim() || undefined,
      grenzen: f.grenzen.value.trim() || undefined, ergebnisform: f.ergebnisform.value.trim() || undefined,
      haltbarkeit: f.haltbarkeit.value, automatisierungsstufe: Number(f.stufe.value), max_kritikrunden: Number(f.runden.value),
      websuche: !!f.websuche.checked,
      vorschlaege_stamm_ki: { start_ki: d.start_ki, hinweise: ent.hinweise || '', kostenlimit_vorschlag: ent.kostenlimit_vorschlag, recherchebedarf: rb },
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
      el('label', {}, 'Teilfragen ', hilfeKnopf('teilfragen')), tfBox,
      el('button', { type: 'button', class: 'link', onclick: () => addTf() }, '+ Teilfrage'),
      el('label', {}, 'Ziel', f.ziel), el('label', {}, 'Vorgaben', f.vorgaben), el('label', {}, 'Grenzen', f.grenzen), el('label', {}, 'Ergebnisform', f.ergebnisform)),
    el('div', { class: 'card' }, el('h2', {}, 'Pflichtfragen an dich ', hilfeKnopf('pflichtfragen')), el('p', { class: 'muted small' }, 'Je besser die Antworten, desto besser das Ergebnis. Leere Antworten sind erlaubt.'), pfBox,
      el('button', { type: 'button', class: 'link', onclick: () => addPf() }, '+ Frage')),
    el('div', { class: 'card' }, el('h2', {}, 'Besetzung (Vorschlag) ', hilfeKnopf('besetzung')), tnBox, el('button', { type: 'button', class: 'link', onclick: () => addTn() }, '+ Teilnehmer')),
    websucheBlock,
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

// ---------- Unterkunftssuche (Werkstatt #41) ----------
const SUCHE_ENDE = new Set(['fertig', 'fehler', 'gestoppt_budget', 'abgebrochen', 'gestoppt']);
const SUCHE_QUELLEN = { hasdata_booking: 'Booking', apify_airbnb: 'Airbnb', rakuten_travel: 'Rakuten Travel', trivago_mcp: 'Trivago' };
const SUCHE_WARNUNGEN = {
  futon: 'Futon', schlafsofa: 'Schlafsofa', etagenbett: 'Etagenbett', schlafplatz_wohnzimmer: 'Schlafplatz im Wohnzimmer',
  steuern_unklar: 'Steuern unklar', wenig_bewertungen: 'Wenige Bewertungen', weit_vom_ziel: 'Weit vom Ziel',
  preis_geschaetzt: 'Preis geschätzt', zwei_zimmer: 'Zwei Zimmer', '2_zimmer': 'Zwei Zimmer',
  preis_2zimmer_unklar: 'Preis für zwei Zimmer unklar', betten_unklar: 'Betten unklar', zimmer_unbekannt: 'Zimmer unbekannt', ueber_budget: 'Über Budget',
};
const sucheZahl = (v) => v === null || v === undefined || v === '' || !Number.isFinite(Number(v)) ? null : Number(v);
const sucheEuro = (v) => sucheZahl(v) === null ? 'Preis unbekannt' : Number(v).toLocaleString('de-DE', { style: 'currency', currency: 'EUR' });
function sucheLink(value) {
  try { const u = new URL(value); return ['https:', 'http:'].includes(u.protocol) ? u.href : null; } catch { return null; }
}
function sucheVergleich(a, b, key, direction) {
  const value = (t) => key === 'name' ? t.name : key === 'preis' ? sucheZahl(t.angebot?.preis_gesamt_eur) :
    key === 'bewertungen' ? sucheZahl(t.bewertungen) : key === 'entfernung' ? sucheZahl(t.luftlinie_ziel_m) : sucheZahl(t.bewertung?.[key]);
  const x = value(a), y = value(b);
  // Fehlende Angaben stehen in beiden Sortierrichtungen hinten.
  if (x == null || y == null) return x == null && y == null ? 0 : x == null ? 1 : -1;
  return (typeof x === 'string' ? x.localeCompare(String(y), 'de') : x - y) * direction;
}
function sucheFormDaten(form) {
  const f = new FormData(form), get = (key) => String(f.get(key) ?? '').trim();
  const kinder = get('kinder_alter');
  if (kinder && !/^\d{1,2}(\s*,\s*\d{1,2})*$/.test(kinder)) throw new Error('Kinderalter bitte durch Kommas trennen, z. B. 13, 11.');
  const alter = kinder ? kinder.split(',').map(Number) : [];
  if (alter.some((n) => n > 17)) throw new Error('Kinderalter muss zwischen 0 und 17 liegen.');
  const datum = (s) => /^\d{4}-\d{2}-\d{2}$/.test(s) && !isNaN(Date.parse(s)) && new Date(s).toISOString().slice(0, 10) === s;
  if (!datum(get('anreise')) || !datum(get('abreise')) || get('abreise') <= get('anreise')) throw new Error('Abreise muss nach der Anreise liegen.');
  const d = { ziel: get('ziel'), anreise: get('anreise'), abreise: get('abreise'), erwachsene: Number(get('erwachsene')),
    kinder_alter: alter, schlafzimmer_min: Number(get('schlafzimmer_min')), max_je_quelle: Number(get('max_je_quelle')), limit_usd: Number(get('limit_usd')) };
  if (d.ziel.length < 2) throw new Error('Bitte einen Zielort angeben.');
  for (const [key, min, max, integer] of [['erwachsene', 1, 10, true], ['schlafzimmer_min', 0, 6, true], ['max_je_quelle', 5, 100, true], ['limit_usd', 0, 10, false]]) {
    if (!get(key) || !Number.isFinite(d[key]) || d[key] < min || d[key] > max || (integer && !Number.isInteger(d[key]))) throw new Error('Bitte die Zahlenfelder innerhalb der angegebenen Grenzen ausfüllen.');
  }
  if (get('budget_eur')) { d.budget_eur = Number(get('budget_eur')); if (!Number.isFinite(d.budget_eur) || d.budget_eur <= 0) throw new Error('Das Aufenthaltsbudget muss größer als 0 sein.'); }
  if (get('land')) { d.land = get('land').toUpperCase(); if (!/^[A-Z]{2}$/.test(d.land)) throw new Error('Land bitte als zweistelligen Code angeben, z. B. JP.'); }
  return d;
}

async function viewSuche(idStr) {
  setChrome('Unterkunft suchen', { tab: 'suche', back: !!idStr });
  let disposed = false, timer, busy = false, snapshot = null;
  const requests = new Set();
  let sort = { key: 'score', direction: -1 };
  const scope = el('div', { class: 'suche' });
  main.replaceChildren(scope);
  disposeSuche = () => { disposed = true; clearTimeout(timer); requests.forEach((c) => c.abort()); };
  const live = () => !disposed && scope.isConnected && parseHash().view === 'suche' && parseHash().arg === idStr;
  async function call(name, daten = {}) {
    const requestController = new AbortController();
    requests.add(requestController);
    const timeout = setTimeout(() => requestController.abort(), 25000);
    try {
      const j = await http('/aktion', { method: 'POST', body: { aktion: name, daten }, signal: requestController.signal });
      if (!j.ok || j.ergebnis?.ok === false) throw new Error(j.fehler || j.ergebnis?.fehler || 'Die Schnittstelle konnte die Anfrage nicht ausführen.');
      return j.ergebnis;
    } catch (e) {
      if (e.name === 'AbortError') throw new Error('Keine Antwort innerhalb von 25 Sekunden. Bitte den gespeicherten Suchlauf prüfen.');
      throw e;
    } finally { clearTimeout(timeout); requests.delete(requestController); }
  }
  const notice = el('p', { role: 'status', 'aria-live': 'polite', class: 'small' });
  if (!idStr) {
    const form = el('form', { class: 'card suche-form' });
    const fields = el('fieldset');
    const grid = el('div', { class: 'suche-grid' });
    const input = (name, label, attrs) => grid.append(el('label', {}, label, el('input', { name, ...attrs })));
    input('ziel', 'Zielort', { required: true, minlength: 2, maxlength: 200, placeholder: 'z. B. Tokyo' });
    input('land', 'Land (optional, z. B. JP)', { maxlength: 2, pattern: '[A-Za-z]{2}', placeholder: 'Automatisch erkennen' });
    input('anreise', 'Anreise', { type: 'date', required: true });
    input('abreise', 'Abreise', { type: 'date', required: true });
    input('erwachsene', 'Erwachsene', { type: 'number', min: 1, max: 10, value: 2, required: true });
    input('kinder_alter', 'Kinderalter (mit Kommas)', { placeholder: 'z. B. 13, 11' });
    input('budget_eur', 'Gesamtbudget Aufenthalt (€)', { type: 'number', min: 0.01, step: 0.01, placeholder: 'Optional' });
    input('schlafzimmer_min', 'Schlafzimmer mindestens', { type: 'number', min: 0, max: 6, value: 2, required: true });
    input('max_je_quelle', 'Treffer je Quelle (5–100)', { type: 'number', min: 5, max: 100, value: 50, required: true });
    input('limit_usd', 'Suchkostenlimit (USD, 0–10)', { type: 'number', min: 0, max: 10, step: 0.01, value: 1.5, required: true });
    const submit = el('button', { type: 'submit', class: 'primary' }, 'Anlegen und Suche starten');
    fields.append(el('legend', {}, 'Deine Reise'), grid,
      el('p', { class: 'muted small' }, 'Booking, Airbnb und Trivago; in Japan zusätzlich Rakuten. Die Suche nutzt externe Quellen und kann Suchkosten sowie Anbieter-Credits verbrauchen. Ergebnisse und Preise werden vorläufig geprüft.'), submit);
    form.append(fields, notice);
    scope.append(form);
    form.addEventListener('submit', async (event) => {
      event.preventDefault(); if (busy || !form.reportValidity()) return;
      let daten; try { daten = sucheFormDaten(form); } catch (e) { notice.textContent = e.message; return; }
      busy = true; fields.disabled = true; notice.textContent = 'Suchauftrag wird angelegt …';
      let id = null;
      try {
        const created = await call('unterkunft_suchauftrag_anlegen', daten);
        id = Number(created?.id);
        if (!Number.isSafeInteger(id) || id <= 0) throw new Error('Die Schnittstelle hat keine gültige Auftragsnummer geliefert. Bitte letzte Suchaufträge prüfen.');
        if (!live()) return;
        notice.replaceChildren('Auftrag angelegt. Suche wird gestartet … ', el('a', { href: '#/suche/' + id }, 'Auftrag #' + id));
        await call('unterkunft_suche_starten', { suchauftrag_id: id });
        if (live()) route('suche', id);
      } catch (e) {
        if (!live()) return;
        if (id) {
          // Nicht erneut anlegen: auch bei verlorener Start-Antwort bleibt die ID zugänglich.
          notice.replaceChildren(e.message + ' ', el('a', { href: '#/suche/' + id }, 'Gespeicherten Auftrag #' + id + ' öffnen'));
          submit.hidden = true;
        } else {
          notice.textContent = e.message + ' Vor erneutem Anlegen die letzten Suchaufträge aktualisieren; die Anfrage könnte bereits gespeichert sein.';
          fields.disabled = false;
        }
      } finally { busy = false; }
    });
    const recent = el('section', { class: 'card' }, el('h2', {}, 'Letzte Suchaufträge'));
    const list = el('div');
    const refresh = el('button', { type: 'button', onclick: loadRecent }, 'Suchaufträge aktualisieren');
    recent.append(refresh, list); scope.append(recent);
    async function loadRecent() {
      if (busy) return;
      refresh.disabled = true;
      try {
        const r = await call('unterkunft_suchlauf_lesen'); if (!live()) return;
        const rows = Array.isArray(r) ? r : r?.suchauftraege;
        if (!Array.isArray(rows)) throw new Error('Unerwartete Antwort beim Lesen der letzten Suchaufträge.');
        list.replaceChildren(...rows.map((a) => el('p', {}, el('a', { href: '#/suche/' + a.id }, `#${a.id} ${a.ziel} · ${fmtDate(a.anreise)}–${fmtDate(a.abreise)} · ${a.status}`))));
        if (!rows.length) list.textContent = 'Noch keine Suchaufträge.';
      } catch (e) { if (live()) list.textContent = e.message; }
      finally { refresh.disabled = false; }
    }
    await loadRecent(); return;
  }
  const id = Number(idStr);
  if (!Number.isSafeInteger(id) || id <= 0) { scope.append(el('p', {}, 'Ungültige Suchauftragsnummer.')); return; }
  const summary = el('section', { class: 'card' });
  const results = el('section', { 'aria-label': 'Suchergebnisse' });
  const refresh = el('button', { onclick: () => poll() }, 'Aktualisieren');
  const start = el('button', { class: 'primary', hidden: true, onclick: async () => {
    if (busy) return; busy = true; start.disabled = refresh.disabled = true;
    try { await call('unterkunft_suche_starten', { suchauftrag_id: id }); }
    catch (e) { if (live()) notice.textContent = e.message + ' Status vor einem weiteren Start aktualisieren.'; }
    finally { busy = false; if (live()) await poll(); }
  } }, 'Diesen Entwurf starten');
  scope.append(el('div', { class: 'actions' }, el('a', { href: '#/suche' }, 'Neue Suche / letzte Aufträge'), refresh, start), notice, summary, results);
  function draw() {
    const openDetails = new Set([...results.querySelectorAll('details[open][data-detail]')].map((n) => n.dataset.detail));
    const a = snapshot.suchauftrag, k = snapshot.kosten || {}, steps = Array.isArray(a.schrittkette) ? a.schrittkette : [];
    start.hidden = a.status !== 'entwurf'; start.disabled = busy;
    summary.replaceChildren(el('h2', {}, `${a.ziel} · #${a.id}`),
      el('p', {}, `${fmtDate(a.anreise)}–${fmtDate(a.abreise)} · ${a.erwachsene} Erwachsene · ${(a.kinder_alter || []).length} Kinder`),
      el('p', {}, 'Status: ', el('strong', {}, a.status), ' · ', snapshot.treffer.length, ' Treffer'),
      el('p', { class: 'small' }, `Suchkosten: ${fmtUsd(k.ist_usd) || 'unbekannt'} · reserviert: ${fmtUsd(k.reserviert_usd) || 'unbekannt'} · Limit: ${fmtUsd(k.limit_usd ?? a.limit_usd) || 'unbekannt'} · Anbieter-Einheiten: ${k.ist_einheiten ?? 'unbekannt'} / ${k.limit_einheiten ?? 'unbekannt'}`),
      el('ul', { class: 'suche-progress' }, steps.map((s) => el('li', {},
        `${SUCHE_QUELLEN[s.quelle] || s.quelle}: ${s.status} · ${s.treffer ?? 0} Treffer`,
        s.kosten_usd != null ? ` · ${fmtUsd(s.kosten_usd)}` : '', s.credits != null ? ` · ${s.credits} Credits` : '',
        s.fehler ? el('p', { class: 'err-text' }, String(s.fehler)) : null))),
      el('p', { class: 'erg-warnung' }, 'Vorläufig: A/B beruhen auf der Vorprüfung. Der Score ist eine nach Bewertungsanzahl gewichtete Bewertungsnote (0–100), noch kein Endranking. Fehlende Teilnoten werden nicht erfunden.'));
    results.replaceChildren();
    const rows = snapshot.treffer;
    const groups = [
      ['A', 'Liste A – vorläufig', rows.filter((t) => t.topf !== 'ausgeschlossen' && t.bewertung?.liste === 'A')],
      ['B', 'Liste B – vorläufig, Angaben prüfen', rows.filter((t) => t.topf !== 'ausgeschlossen' && t.bewertung?.liste === 'B')],
      ['offen', 'Noch ohne Listenzuordnung', rows.filter((t) => t.topf !== 'ausgeschlossen' && !['A', 'B'].includes(t.bewertung?.liste))],
      ['ausgeschlossen', 'Ausgeschlossene Treffer', rows.filter((t) => t.topf === 'ausgeschlossen')],
    ];
    for (const [key, title, items] of groups) {
      if (!items.length && !['A', 'B'].includes(key)) continue;
      const section = el(key === 'ausgeschlossen' ? 'details' : 'section', { class: 'card suche-results' });
      section.append(el(key === 'ausgeschlossen' ? 'summary' : 'h2', {}, `${title} (${items.length})`));
      if (!items.length) section.append(el('p', { class: 'muted' }, 'Noch keine Treffer in dieser Liste.'));
      else section.append(sucheTabelle(items, sort, (sortKey) => {
        const wasOpen = section.open;
        sort = { key: sortKey, direction: sort.key === sortKey ? -sort.direction : ['name', 'preis', 'entfernung'].includes(sortKey) ? 1 : -1 };
        draw();
        const replacement = results.querySelector(`[data-group="${key}"]`);
        if (wasOpen) replacement.open = true;
        replacement.querySelector(`[data-sort="${sortKey}"]`)?.focus({ preventScroll: true });
      }));
      section.dataset.group = key; results.append(section);
      if (key === 'ausgeschlossen') section.dataset.detail = 'ausgeschlossen';
    }
    results.querySelectorAll('details[data-detail]').forEach((n) => { n.open = openDetails.has(n.dataset.detail); });
    if (rows.some((t) => t.quelle === 'rakuten_travel')) results.append(el('p', { class: 'small' }, 'Supported by Rakuten Developers'));
  }
  async function poll() {
    if (!live() || busy) return;
    clearTimeout(timer); busy = true; refresh.disabled = start.disabled = true;
    try {
      const r = await call('unterkunft_suchlauf_lesen', { suchauftrag_id: id });
      if (!live()) return;
      if (!r?.suchauftrag || !Array.isArray(r.treffer)) throw new Error('Suchlauf nicht gefunden oder Antwort unvollständig.');
      snapshot = r; draw();
      const running = !SUCHE_ENDE.has(r.suchauftrag.status) && r.suchauftrag.status !== 'entwurf';
      notice.textContent = running ? 'Suche läuft. Automatische Aktualisierung alle 7 Sekunden.' : 'Stand aktualisiert. ' + (r.suchauftrag.status === 'fehler' ? 'Die Suche meldet einen Fehler; vorhandene Treffer bleiben sichtbar.' : r.suchauftrag.status === 'gestoppt_budget' ? 'Kostenlimit erreicht. Vorhandene Treffer bleiben sichtbar.' : '');
      if (running) timer = setTimeout(poll, 7000);
    } catch (e) {
      if (live()) notice.textContent = e.message + ' Die automatische Aktualisierung pausiert. Mit „Aktualisieren“ erneut lesen; es wird keine neue Suche gestartet.';
    } finally { busy = false; if (live()) { refresh.disabled = false; start.disabled = false; } }
  }
  await poll();
}

function sucheTabelle(items, sort, onSort) {
  const table = el('table', { class: 'suche-table' });
  const headings = [['name', 'Unterkunft'], ['preis', 'Gesamtpreis'], ['score', 'Score (vorläufig)'], ['datenlage', 'Datenlage (%)'], ['bewertungen', 'Bewertungen'], ['entfernung', 'Luftlinie zum Ziel']];
  table.append(el('thead', {}, el('tr', {}, headings.map(([key, title]) => el('th', { scope: 'col', 'aria-sort': sort.key === key ? sort.direction === 1 ? 'ascending' : 'descending' : 'none' },
    el('button', { type: 'button', 'data-sort': key, onclick: () => onSort(key) }, title, sort.key === key ? sort.direction === 1 ? ' ↑' : ' ↓' : ' ↕'))), el('th', { scope: 'col' }, 'Hinweise / Details'))));
  const tbody = el('tbody');
  for (const t of [...items].sort((a, b) => sucheVergleich(a, b, sort.key, sort.direction))) {
    const a = t.angebot || {}, b = t.bewertung || {};
    const warnings = [...new Set([...(Array.isArray(b.warnungen) ? b.warnungen : []), ...(a.preis_art === 'geschaetzt' || b.preis_geschaetzt ? ['preis_geschaetzt'] : [])])];
    const url = sucheLink(a.link), estimated = warnings.includes('preis_geschaetzt');
    const info = el('details', { 'data-detail': String(t.treffer_id) }, el('summary', {}, 'Angaben und Teilnoten'),
      el('p', {}, b.begruendung || 'Noch keine Begründung verfügbar.'),
      el('p', {}, 'Offene Prüfpunkte: ' + (b.gegenpruefung?.luecken?.join(', ') || 'keine angegeben')),
      el('p', {}, 'Preisstand: ' + (fmtDate(a.abrufzeit) || 'unbekannt')),
      a.schaetz_basis ? el('p', {}, 'Schätzung: ' + a.schaetz_basis) : null,
      a.kurs != null ? el('p', {}, `Umrechnung ${a.waehrung}: ${a.kurs} · Kursdatum ${fmtDate(a.kurs_datum)}`) : null,
      el('p', {}, 'Kategorie: ' + (a.kategorie_name || 'unbekannt')),
      el('p', {}, 'Ausschlussgrund: ' + (t.ko_grund || 'keiner angegeben')),
      el('h3', {}, 'Zimmerangaben'), renderAny(t.kategorien || []),
      el('h3', {}, 'Teilnoten'), Object.keys(b.spaltennoten || {}).length ? renderAny(b.spaltennoten) : el('p', {}, 'Noch nicht verfügbar (Endranking folgt).'));
    const td = (label, ...content) => el('td', { 'data-label': label }, ...content);
    tbody.append(el('tr', {},
      td('Unterkunft', el('strong', {}, t.name || 'Ohne Namen'), el('div', { class: 'muted small' }, SUCHE_QUELLEN[t.quelle] || t.quelle || 'Quelle unbekannt'),
        url ? el('a', { href: url, target: '_blank', rel: 'noopener noreferrer' }, 'Angebot öffnen ↗') : el('span', { class: 'muted small' }, 'Kein Angebotslink')),
      td('Gesamtpreis', (estimated && sucheZahl(a.preis_gesamt_eur) !== null ? 'ca. ' : '') + sucheEuro(a.preis_gesamt_eur) + (estimated ? ' (geschätzt)' : '')),
      td('Score (vorläufig)', sucheZahl(b.score) ?? '–'), td('Datenlage (%)', sucheZahl(b.datenlage) ?? '–'),
      td('Bewertungen', sucheZahl(t.bewertungen) ?? '–', el('div', { class: 'small' }, t.note != null ? `${t.note} / ${t.note_skala ?? '?'}` : 'Note unbekannt')),
      td('Luftlinie zum Ziel', sucheZahl(t.luftlinie_ziel_m) === null ? 'unbekannt' : (t.luftlinie_ziel_m / 1000).toLocaleString('de-DE', { maximumFractionDigits: 1 }) + ' km'),
      td('Hinweise / Details', el('div', { class: 'suche-badges' },
        el('span', { class: 'pill' }, t.topf === 'unbewertet' ? 'Unbewertet' : t.topf === 'ausgeschlossen' ? 'Ausgeschlossen' : 'Shortlist'),
        el('span', { class: 'pill' }, 'Ampel: ' + (b.ampel || 'unbekannt')),
        warnings.map((w) => el('span', { class: 'suche-warning' }, SUCHE_WARNUNGEN[w] || w))), info)));
  }
  table.append(tbody);
  return el('div', { class: 'suche-table-scroll', tabindex: 0, role: 'region', 'aria-label': 'Sortierbare Unterkunftstabelle' }, table);
}

// ---------- Start ----------
$('#ver').textContent = 'v' + APP_VERSION;
if ('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js').catch(() => { /* ohne Offline-Hülle weiter */ });
render();
