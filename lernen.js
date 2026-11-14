/* W150: Lernen Schule – Lerneinheiten in der App.
   Spricht mit der Serverfunktion lernen-api (gleiche Anmeldung wie app-api). Die Datenbank prüft Zugriff,
   bewertet Antworten und führt den Lernstand; die App zeigt nur an und schickt Eingaben.
   Ansichten: #/lernen (Kind wählen, Einheiten je Ort) · #/lerneinheit/<kind>-<einheit> (Verstehen · Üben · Test). */
'use strict';

const lernApi = () => API.replace('/app-api', '/lernen-api'); // API kommt aus app.js (wird danach geladen)
const LERN_KIND_KEY = 'lern_kind';
const LZ_STATUS = { offen: 'offen', nachgewiesen: 'geschafft', korrigiert: 'verbessert', gesichert: 'sicher', fehler: 'noch üben' };
const LZ_KLASSE = { offen: '', nachgewiesen: 'neu', korrigiert: 'neu', gesichert: 'neu', fehler: 'fehler' };

async function lernCall(aktion, daten = {}) {
  const headers = { 'Content-Type': 'application/json' };
  if (store.token) headers.Authorization = 'Bearer ' + store.token;
  const r = await fetch(mitRegion(lernApi() + '/aktion'), { method: 'POST', headers, body: JSON.stringify({ aktion, daten }) });
  let j; try { j = await r.json(); } catch { j = { ok: false, fehler: 'Keine Antwort (' + r.status + ')' }; }
  if (r.status === 401) { store.token = null; route('login'); throw new Error('Nicht angemeldet'); }
  if (!j.ok) throw new Error(j.fehler || 'Fehler bei ' + aktion);
  return j.ergebnis;
}
const lernKindMerken = (id) => { try { localStorage.setItem(LERN_KIND_KEY, String(id)); } catch { /* privat */ } };
const lernKindGemerkt = () => { try { return Number(localStorage.getItem(LERN_KIND_KEY)) || null; } catch { return null; } };
const lernCid = () => (crypto.randomUUID ? crypto.randomUUID() : Date.now() + '-' + Math.random().toString(16).slice(2));
const lernText = (t) => String(t ?? '').replace(/(\d) (?=\d{3}(?!\d))/g, '$1\u00a0'); // Zahlen wie 20 000 nicht umbrechen
const lernZahl = (n) => Number(n).toLocaleString('de-DE').replace(/\./g, ' ');

// ---------- Übersicht ----------
async function viewLernen() {
  setChrome('Lernen Schule', { tab: 'lernen' });
  const live = viewGuard();
  loading();
  const u = await lernCall('schule_uebersicht');
  if (!live()) return;
  const kinder = u.lernende || [];
  let kind = kinder.find((k) => k.id === lernKindGemerkt()) || kinder.find((k) => !k.ist_test) || kinder[0];
  const liste = el('div', { class: 'lern-orte' });
  const wahl = el('div', { class: 'lern-kinder', role: 'tablist', 'aria-label': 'Wer lernt?' });
  const zeichne = () => {
    wahl.replaceChildren(...kinder.map((k) => el('button', { type: 'button', role: 'tab', class: 'lern-kind' + (k === kind ? ' on' : ''), 'aria-selected': String(k === kind),
      onclick: () => { kind = k; lernKindMerken(k.id); zeichne(); } }, k.name, k.ist_test ? el('small', {}, ' Prüfung') : null)));
    liste.replaceChildren(...lernOrte(u, kind));
  };
  zeichne();
  main.replaceChildren(
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'LERNEN SCHULE'), el('h2', {}, 'Wer lernt heute?')),
    kinder.length ? wahl : el('p', { class: 'card muted' }, 'Kein Kind freigeschaltet.'),
    liste,
    el('details', { class: 'card lern-merkblatt' }, el('summary', {}, 'Merkblatt Mathe 7/8 (ohne Anmeldung)'),
      el('p', { class: 'small' }, 'Erklärungen und Übungen zum Nachschlagen. Ohne Lernstand.'),
      el('a', { class: 'btn primary', href: 'mathe/', target: '_blank', rel: 'noopener' }, 'Merkblatt öffnen ↗')));
}

function lernOrte(u, kind) {
  if (!kind) return [];
  const stand = new Map((kind.stand || []).map((s) => [s.einheit_id, s]));
  const route = new Map((kind.route || []).map((r) => [r.block_id, r]));
  const einheiten = (u.einheiten || []).filter((e) => e.status !== 'entwurf' || kind.ist_test);
  if (!einheiten.length) return [el('p', { class: 'card muted' }, 'Noch keine freigegebenen Lerneinheiten.')];
  const orte = new Map();
  for (const e of einheiten) { if (!orte.has(e.block_id)) orte.set(e.block_id, []); orte.get(e.block_id).push(e); }
  return [...orte.values()].map((es) => {
    const r = route.get(es[0].block_id);
    const fertig = r?.status === 'fertig';
    return el('section', { class: 'lern-ort' },
      el('h3', {}, es[0].ort_titel, el('span', { class: 'muted small' }, ' · Ort ' + es[0].ort),
        fertig ? el('span', { class: 'pill neu' }, 'abgeschlossen') : r?.kann_schon ? el('span', { class: 'pill' }, 'kann schon') : null),
      ...es.map((e) => {
        const s = stand.get(e.id) || {};
        const n = e.pflicht_anzahl || 0, f = Number(s.fertig || 0);
        const zustand = s.laeuft ? ['laeuft', 'Test läuft'] : n && f >= n ? ['neu', 'geschafft'] : s.fehler ? ['fehler', 'noch üben'] : s.blocktest ? ['wartet', 'Test gemacht'] : null;
        return el('a', { class: 'card lern-einheit', href: `#/lerneinheit/${kind.id}-${e.id}` },
          el('div', { class: 'lern-einheit-kopf' }, el('b', {}, e.titel),
            e.status === 'entwurf' ? el('span', { class: 'pill wartet' }, 'Entwurf') : null,
            zustand ? el('span', { class: 'pill ' + zustand[0] }, zustand[1]) : null),
          e.ziel ? el('p', { class: 'small muted' }, e.ziel) : null,
          n ? el('div', { class: 'lern-balken', role: 'img', 'aria-label': `${f} von ${n} Lernzielen geschafft` },
            el('span', { style: `width:${Math.round(100 * f / n)}%` })) : null,
          n ? el('p', { class: 'small muted' }, `${f} von ${n} Lernzielen geschafft`) : null);
      }));
  });
}

// ---------- Einheit ----------
async function viewLernEinheit(arg) {
  setChrome('Lerneinheit', { back: true, tab: 'lernen' });
  const live = viewGuard();
  const [kindId, einheitId] = String(arg || '').split('-').map(Number);
  if (!kindId || !einheitId) { route('lernen'); return; }
  loading();
  const ctx = { kind: kindId, einheit: einheitId, live };
  ctx.daten = await lernCall('schule_einheit_lesen', { lernender_id: kindId, einheit_id: einheitId });
  if (!live()) return;
  const inh = ctx.daten.inhalt || {};
  $('#title').textContent = (inh.ziel || 'Lerneinheit').split(':')[0];
  const body = el('div', { class: 'lern-body' });
  const reiter = [['verstehen', 'Verstehen'], ['ueben', 'Üben'], ['test', 'Test']];
  const leiste = el('div', { class: 'lern-reiter', role: 'tablist' });
  const zeige = (k) => {
    for (const b of leiste.children) { const on = b.dataset.k === k; b.classList.toggle('on', on); b.setAttribute('aria-selected', String(on)); }
    body.replaceChildren(k === 'verstehen' ? lernVerstehen(inh) : k === 'ueben' ? lernUeben(ctx) : lernTestStart(ctx, body));
  };
  leiste.append(...reiter.map(([k, t]) => el('button', { type: 'button', role: 'tab', 'data-k': k, onclick: () => zeige(k) }, t)));
  main.replaceChildren(el('section', { class: 'lern-kopf' }, el('p', { class: 'eyebrow' }, ctx.daten.status === 'entwurf' ? 'ENTWURF · NUR TESTKIND' : 'LERNEINHEIT'),
    el('p', {}, inh.ziel || '')), lernStandZeile(ctx.daten.stand), leiste, body);
  zeige(ctx.daten.laufender_test ? 'test' : 'verstehen');
}

function lernStandZeile(stand) {
  if (!stand?.length) return null;
  return el('div', { class: 'lern-stand', 'aria-label': 'Lernziele' }, ...stand.filter((s) => s.pflicht).map((s) =>
    el('span', { class: 'pill ' + (LZ_KLASSE[s.status] || ''), title: s.lernziel }, lernZielName(s.lernziel) + ': ' + (LZ_STATUS[s.status] || s.status))));
}
const lernZielName = (k) => String(k).replace(/_/g, ' ').replace(/ae/g, 'ä').replace(/oe/g, 'ö').replace(/ue/g, 'ü').replace(/^./, (c) => c.toUpperCase());

function lernVerstehen(inh) {
  const teile = [];
  for (const v of inh.verstehen || []) teile.push(el('article', { class: 'card lern-karte' }, el('h3', {}, v.titel), el('p', {}, v.text),
    v.beispiel ? el('p', { class: 'lern-beispiel' }, v.beispiel) : null));
  if (inh.merke?.length) teile.push(el('article', { class: 'card lern-merke' }, el('h3', {}, 'Merke'), el('ul', {}, inh.merke.map((m) => el('li', {}, m)))));
  for (const a of inh.alternativ || []) teile.push(el('details', { class: 'card' }, el('summary', {}, 'Anders erklärt: ' + a.titel), el('p', {}, a.text)));
  if (inh.eingabe_hinweis) teile.push(el('p', { class: 'small muted' }, inh.eingabe_hinweis));
  return el('div', { class: 'lern-verstehen' }, ...teile);
}

// ---------- Aufgaben-Darstellung ----------
// Zahlenstrahl: Markierungen 0..abschnitte; bei antworttyp markierung antippbar; pfeil zeigt auf eine Markierung.
function lernZahlenstrahl(g, waehlbar, onWahl) {
  const ns = 'http://www.w3.org/2000/svg', B = 340, L = 30, R = B - 40, Y = 44, n = Math.max(1, Number(g.abschnitte) || 1);
  const x = (i) => L + (R - L) * i / n;
  const svg = document.createElementNS(ns, 'svg');
  svg.setAttribute('viewBox', `0 0 ${B} 84`); svg.setAttribute('class', 'lern-strahl'); svg.setAttribute('role', 'img');
  svg.setAttribute('aria-label', `Zahlenstrahl von ${lernZahl(g.start)} bis ${lernZahl(g.ende)} mit ${n} gleichen Abschnitten`);
  const mk = (tag, a, txt) => { const e = document.createElementNS(ns, tag); for (const [k, v] of Object.entries(a)) e.setAttribute(k, v); if (txt !== undefined) e.textContent = txt; svg.append(e); return e; };
  mk('line', { x1: L - 6, y1: Y, x2: R + 14, y2: Y, class: 'achse' });
  mk('path', { d: `M${R + 14} ${Y} l-7 -4 v8 z`, class: 'spitze' });
  const knoepfe = [];
  for (let i = 0; i <= n; i++) {
    mk('line', { x1: x(i), y1: Y - 8, x2: x(i), y2: Y + 8, class: 'strich' });
    if (waehlbar) {
      const k = mk('circle', { cx: x(i), cy: Y, r: 11, class: 'ziel', tabindex: 0, role: 'button', 'aria-label': `Markierung ${i}` });
      const w = () => { knoepfe.forEach((c, j) => c.classList.toggle('on', j === i)); onWahl(i); };
      k.addEventListener('click', w); k.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); w(); } });
      knoepfe.push(k);
    }
  }
  mk('text', { x: x(0), y: Y + 28, class: 'zahl' }, lernZahl(g.start));
  mk('text', { x: x(n), y: Y + 28, class: 'zahl' }, lernZahl(g.ende));
  if (g.pfeil !== undefined && g.pfeil !== null) mk('path', { d: `M${x(g.pfeil)} ${Y - 12} l-6 -12 h12 z`, class: 'pfeil' });
  return svg;
}

// Liefert { node, antwort(), sperren() }; antwort() ist null, solange nichts eingegeben ist.
function lernAufgabe(a, vorher) {
  const f = a.frage || {};
  let wert = vorher ?? null;
  const teile = [el('p', { class: 'lern-frage' }, lernText(f.text))];
  if (f.hinweis) teile.push(el('p', { class: 'small muted' }, f.hinweis));
  const felder = [];
  if (a.antworttyp === 'markierung') {
    const strahl = lernZahlenstrahl(f.grafik || {}, true, (i) => { wert = { index: i }; });
    if (wert) strahl.querySelectorAll('.ziel')[wert.index]?.classList.add('on');
    teile.push(strahl);
  } else if (f.grafik) teile.push(lernZahlenstrahl(f.grafik, false));
  if (a.antworttyp === 'auswahl') {
    const name = 'a' + a.id + '-' + Math.random().toString(36).slice(2, 7);
    teile.push(el('div', { class: 'lern-auswahl', role: 'radiogroup' }, (a.antworten || []).map((t, i) => {
      const inp = el('input', { type: 'radio', name, value: String(i) });
      if (wert?.index === i) inp.checked = true;
      inp.addEventListener('change', () => { wert = { index: i }; });
      felder.push(inp);
      return el('label', { class: 'lern-option' }, inp, el('span', {}, t));
    })));
  } else if (a.antworttyp === 'zahl' || a.antworttyp === 'text') {
    const inp = el('input', { type: 'text', autocomplete: 'off', autocapitalize: a.antworttyp === 'text' ? 'characters' : 'off',
      spellcheck: 'false', 'aria-label': 'Antwort', class: 'lern-eingabe' });
    if (wert?.wert) inp.value = wert.wert;
    inp.addEventListener('input', () => { wert = inp.value.trim() ? { wert: inp.value } : null; });
    felder.push(inp);
    teile.push(el('div', { class: 'lern-zeile' }, inp, a.einheit ? el('span', { class: 'lern-einheit-zeichen' }, a.einheit) : null));
  } else if (a.antworttyp === 'luecken') {
    const stuecke = String(f.schablone || '□').split('□');
    const werte = Array.isArray(wert?.werte) ? [...wert.werte] : Array(stuecke.length - 1).fill('');
    const zeile = el('div', { class: 'lern-luecken' });
    stuecke.forEach((s, i) => {
      if (s) zeile.append(el('span', {}, s));
      if (i < stuecke.length - 1) {
        const inp = el('input', { type: 'text', inputmode: 'text', autocomplete: 'off', spellcheck: 'false', 'aria-label': `Feld ${i + 1}`, class: 'lern-feld', value: werte[i] || '' });
        inp.addEventListener('input', () => { werte[i] = inp.value; wert = werte.some((x) => String(x).trim()) ? { werte: [...werte] } : null; });
        felder.push(inp); zeile.append(inp);
      }
    });
    teile.push(zeile);
    teile.push(el('div', { class: 'lern-minus' }, el('button', { type: 'button', class: 'secondary', onclick: () => {
      const akt = felder.includes(document.activeElement) ? document.activeElement : felder.find((x) => !x.value) || felder[0];
      if (!akt) return; akt.value = akt.value.startsWith('−') ? akt.value.slice(1) : '−' + akt.value.replace(/^-/, ''); akt.dispatchEvent(new Event('input')); akt.focus();
    } }, '± Vorzeichen')));
  }
  return { node: el('div', { class: 'lern-aufgabe' }, ...teile), antwort: () => wert,
    sperren: (an = true) => felder.forEach((x) => { x.disabled = an; }) };
}

function lernLoesungText(a) {
  const l = a.loesung || {};
  if (a.antworttyp === 'auswahl') return (a.antworten || [])[l.index] ?? '';
  if (a.antworttyp === 'markierung') return `Markierung ${l.index}`;
  if (a.antworttyp === 'luecken') { const s = String(a.frage?.schablone || '').split('□'); return s.map((t, i) => t + (i < s.length - 1 ? String(l.werte?.[i] ?? '').replace('-', '−') : '')).join(''); }
  if (a.antworttyp === 'text') return l.text ?? '';
  return l.wert !== undefined ? lernZahl(l.wert) + (l.einheit ? ' ' + l.einheit : '') : '';
}
function lernAntwortText(a, w) {
  if (!w) return '(keine Antwort)';
  if (a.antworttyp === 'auswahl') return (a.antworten || [])[w.index] ?? '';
  if (a.antworttyp === 'markierung') return `Markierung ${w.index}`;
  if (a.antworttyp === 'luecken') { const s = String(a.frage?.schablone || '').split('□'); return s.map((t, i) => t + (i < s.length - 1 ? (w.werte?.[i] ?? '') : '')).join(''); }
  return w.wert ?? '';
}

// ---------- Üben ----------
function lernUeben(ctx) {
  const alle = ctx.daten.uebungen || [];
  const box = el('div', { class: 'lern-ueben' });
  if (!alle.length) { box.append(el('p', { class: 'card muted' }, 'Keine Übungsaufgaben.')); return box; }
  const ziele = [...new Set(alle.map((a) => a.lernziel))];
  let filter = null, i = 0;
  const auswahl = el('div', { class: 'lern-filter' });
  const karte = el('div');
  const liste = () => alle.filter((a) => !filter || a.lernziel === filter);
  const zeichneFilter = () => auswahl.replaceChildren(
    el('button', { type: 'button', class: 'pill' + (!filter ? ' on' : ''), onclick: () => { filter = null; i = 0; zeichneFilter(); zeige(); } }, 'Alle'),
    ...ziele.map((z) => el('button', { type: 'button', class: 'pill' + (filter === z ? ' on' : ''), onclick: () => { filter = z; i = 0; zeichneFilter(); zeige(); } }, lernZielName(z))));
  const zeige = () => {
    const l = liste(); const a = l[i % l.length];
    const auf = lernAufgabe(a);
    let hilfe = 0; const cid = lernCid();
    const meldung = el('div', { role: 'status', 'aria-live': 'polite' });
    const tipp = a.tipp ? el('button', { type: 'button', class: 'secondary', onclick: () => { hilfe = 1; tipp.replaceWith(el('p', { class: 'lern-tipp' }, '💡 ' + a.tipp)); } }, 'Tipp') : null;
    const pruefen = el('button', { type: 'button', class: 'primary' }, 'Prüfen');
    const weiter = el('button', { type: 'button', class: 'secondary', onclick: () => { i = (i + 1) % l.length; zeige(); } }, 'Nächste Aufgabe');
    pruefen.addEventListener('click', async () => {
      const w = auf.antwort();
      if (!w) { meldung.replaceChildren(el('p', { class: 'lern-hinweis' }, 'Bitte erst antworten.')); return; }
      pruefen.disabled = true;
      try {
        const r = await lernCall('schule_uebung_pruefen', { lernender_id: ctx.kind, aufgabe_id: a.id, antwort: w, client_id: cid, hilfe });
        if (!ctx.live()) return;
        if (!r.format_ok) { meldung.replaceChildren(el('p', { class: 'lern-hinweis' }, r.hinweis)); pruefen.disabled = false; return; }
        auf.sperren(); pruefen.hidden = true;
        a.loesung = r.loesung;
        meldung.replaceChildren(el('div', { class: 'lern-rueck ' + (r.richtig ? 'ok' : 'falsch') },
          el('b', {}, r.richtig ? '✓ Richtig!' : '✗ Noch nicht. Richtig ist: ' + lernLoesungText(a)),
          r.loesungsweg ? el('p', {}, r.loesungsweg) : null));
      } catch (e) { meldung.replaceChildren(el('p', { class: 'err-text' }, e.message)); pruefen.disabled = false; }
    });
    karte.replaceChildren(el('div', { class: 'card' },
      el('p', { class: 'eyebrow' }, `${lernZielName(a.lernziel)} · Aufgabe ${(i % l.length) + 1} von ${l.length}`),
      auf.node, meldung, el('div', { class: 'row lern-knoepfe' }, tipp, pruefen, weiter)));
  };
  zeichneFilter(); zeige();
  box.append(auswahl, karte);
  return box;
}

// ---------- Test ----------
function lernTestStart(ctx, body) {
  const box = el('div', { class: 'lern-test' });
  const stand = ctx.daten.stand || [];
  const offen = ctx.daten.laufender_test;
  const hatFehler = stand.some((s) => s.status === 'fehler');
  const hatNachweis = stand.some((s) => ['nachgewiesen', 'korrigiert'].includes(s.status));
  const blockFertig = stand.some((s) => s.status !== 'offen');
  const start = async (art) => {
    box.replaceChildren(el('div', { class: 'spinner' }, 'Test wird vorbereitet …'));
    try {
      const r = await lernCall('schule_test_starten', { lernender_id: ctx.kind, einheit_id: ctx.einheit, art });
      if (!ctx.live()) return;
      if (!r.ok) {
        const t = r.grund === 'noch_nicht_faellig' ? 'Der nächste Nachtest ist noch nicht dran. ' + (r.noch_nicht_faellig || []).map((x) => `${lernZielName(x.lernziel)}: noch ${x.lerntage_noetig - x.lerntage_seit} Lerntage`).join(' · ')
          : r.grund === 'vorrat_erschoepft' ? 'Für ' + (r.vorrat_erschoepft || []).map(lernZielName).join(', ') + ' gibt es gerade keine neue Aufgabe. Sag Bescheid, dann kommen neue dazu.'
          : 'Gerade gibt es nichts zu testen.';
        box.replaceChildren(el('p', { class: 'card' }, t)); return;
      }
      lernTestLauf(ctx, box, r);
    } catch (e) { box.replaceChildren(el('p', { class: 'card err-text' }, e.message)); }
  };
  const knopf = (t, art, text) => el('div', { class: 'card' }, el('h3', {}, t), el('p', { class: 'small' }, text),
    el('button', { type: 'button', class: 'primary', onclick: () => start(art) }, t + ' starten'));
  if (offen) box.append(el('div', { class: 'card' }, el('h3', {}, 'Angefangener Test'), el('p', { class: 'small' }, 'Deine bisherigen Antworten sind gespeichert.'),
    el('button', { type: 'button', class: 'primary', onclick: () => start(offen.art) }, 'Weitermachen')));
  else {
    if (!blockFertig) box.append(knopf('Test', 'blocktest', 'Eine Aufgabe je Lernziel, ohne Tipps. Die Lösungen siehst du nach dem Abgeben.'));
    if (hatFehler) box.append(knopf('Verbessern', 'korrektur', 'Nur die Lernziele, die noch nicht geklappt haben – mit neuen Aufgaben. Übe sie vorher noch einmal.'));
    if (hatNachweis) box.append(knopf('Nachtest', 'nachtest', 'Prüft nach einigen Lerntagen, ob es noch sitzt. Nach drei Nachtests gilt ein Lernziel als sicher.'));
    if (!box.children.length) box.append(el('p', { class: 'card' }, 'Alles geschafft und gesichert. 🎉'));
  }
  return box;
}

function lernTestLauf(ctx, box, t) {
  const aufg = t.aufgaben || [];
  const antworten = new Map(); const gesendet = new Set(t.beantwortet || []);
  let i = Math.max(0, aufg.findIndex((a) => !gesendet.has(a.id)));
  const art = { blocktest: 'Test', korrektur: 'Verbessern', nachtest: 'Nachtest' }[t.art] || 'Test';
  const zeige = () => {
    const a = aufg[i]; const auf = lernAufgabe(a, antworten.get(a.id));
    const meldung = el('div', { role: 'status', 'aria-live': 'polite' });
    const speichern = async () => {
      const w = auf.antwort();
      if (!w) return gesendet.has(a.id);
      const r = await lernCall('schule_test_antwort', { lernender_id: ctx.kind, sitzung_id: t.sitzung_id, aufgabe_id: a.id, antwort: w, client_id: lernCid() });
      if (!r.format_ok) { meldung.replaceChildren(el('p', { class: 'lern-hinweis' }, r.hinweis)); return null; }
      antworten.set(a.id, w); gesendet.add(a.id); return true;
    };
    const geh = async (d) => {
      try { const ok = await speichern(); if (ok === null) return; i = Math.min(aufg.length - 1, Math.max(0, i + d)); zeige(); }
      catch (e) { meldung.replaceChildren(el('p', { class: 'err-text' }, e.message)); }
    };
    const abgeben = el('button', { type: 'button', class: 'primary', onclick: async () => {
      try {
        const ok = await speichern(); if (ok === null) return;
        const fehlt = aufg.filter((x) => !gesendet.has(x.id)).length;
        if (fehlt && !window.confirm(`${fehlt} Aufgabe(n) ohne Antwort. Sie zählen als falsch. Trotzdem abgeben?`)) return;
        abgeben.disabled = true;
        const r = await lernCall('schule_test_abschliessen', { lernender_id: ctx.kind, sitzung_id: t.sitzung_id });
        if (ctx.live()) lernTestErgebnis(ctx, box, r);
      } catch (e) { abgeben.disabled = false; meldung.replaceChildren(el('p', { class: 'err-text' }, e.message)); }
    } }, 'Abgeben');
    box.replaceChildren(el('div', { class: 'card' },
      el('p', { class: 'eyebrow' }, `${art} · Aufgabe ${i + 1} von ${aufg.length} · ${gesendet.size} beantwortet`),
      el('div', { class: 'lern-punkte' }, aufg.map((x, j) => el('button', { type: 'button', class: (j === i ? 'on ' : '') + (gesendet.has(x.id) ? 'fertig' : ''), 'aria-label': `Aufgabe ${j + 1}`, onclick: () => { i = j; geh(0); } }, String(j + 1)))),
      auf.node, meldung,
      el('div', { class: 'row lern-knoepfe' },
        el('button', { type: 'button', class: 'secondary', disabled: i === 0, onclick: () => geh(-1) }, '‹ Zurück'),
        i < aufg.length - 1 ? el('button', { type: 'button', class: 'primary', onclick: () => geh(1) }, 'Weiter ›') : abgeben),
      i < aufg.length - 1 ? el('p', { class: 'small muted' }, 'Abgeben kannst du bei der letzten Aufgabe. Bis dahin kannst du Antworten ändern.') : null));
  };
  zeige();
}

function lernTestErgebnis(ctx, box, r) {
  const ort = r.ort || {};
  box.replaceChildren(
    el('div', { class: 'card lern-ergebnis' },
      el('h3', {}, `${r.richtig} von ${r.gesamt} richtig`),
      r.einheit_abgeschlossen ? el('p', { class: 'lern-rueck ok' }, el('b', {}, 'Einheit geschafft! 🎉')) : el('p', { class: 'small' }, 'Lernziele mit „noch üben“: erst üben, dann im Reiter Test „Verbessern“.'),
      ort.abgeschlossen ? el('p', { class: 'lern-rueck ok' }, el('b', {}, 'Ort abgeschlossen – weiter zum nächsten Ort.')) : null,
      lernStandZeile(r.lernziele)),
    ...(r.ergebnisse || []).map((x) => {
      const a = { ...x, antworttyp: x.antworttyp || (x.loesung?.werte ? 'luecken' : x.loesung?.index !== undefined ? (x.antworten ? 'auswahl' : 'markierung') : x.loesung?.text !== undefined ? 'text' : 'zahl') };
      return el('div', { class: 'card lern-rueck-karte ' + (x.richtig ? 'ok' : 'falsch') },
        el('p', { class: 'eyebrow' }, lernZielName(x.lernziel) + (x.richtig ? ' · ✓ richtig' : ' · ✗ falsch')),
        el('p', { class: 'lern-frage' }, lernText(x.frage?.text)),
        x.frage?.grafik ? lernZahlenstrahl(x.frage.grafik, false) : null,
        el('p', { class: 'small' }, 'Deine Antwort: ', el('b', {}, lernAntwortText(a, x.antwort))),
        x.richtig ? null : el('p', { class: 'small' }, 'Richtig: ', el('b', {}, lernLoesungText(a))),
        x.loesungsweg && !x.richtig ? el('p', { class: 'small muted' }, x.loesungsweg) : null);
    }),
    el('button', { type: 'button', class: 'primary', onclick: () => render() }, 'Zur Einheit'));
}
