/* Gezielte Nachrecherche: Auftrag vorbereiten, niemals automatisch ausführen. */
'use strict';

const LUECKEN_STATUS = { erzeugt: 'Angelegt – wartet auf Claude', in_arbeit: 'In Arbeit', erledigt: 'Erledigt', teilweise: 'Teilweise ergänzt', nicht_moeglich: 'Nicht möglich' };
function sucheLueckenKandidat(t) {
  if (sucheGruppe(t) !== 'B' || !Number.isSafeInteger(t.treffer_id) || t.treffer_id <= 0) return false;
  const b = t.bewertung || {};
  return sucheTexte(b.warnungen).length > 0 || sucheTexte(b.gegenpruefung?.luecken).length > 0 ||
    sucheDatenlage(t) === null || sucheDatenlage(t) < 100 || sucheZahl(t.angebot?.preis_gesamt_eur) === null;
}

function sucheLuecken(id, call, live, changed) {
  let rows = [], orders = [], rowRefs = [], loading = false, writing = false, uncertain = false, attempt = null, loaded = false, handoffId = null;
  const selected = new Set(), fields = new Map();
  const notice = el('p', { class: 'small', role: 'status' });
  const selectionText = el('p', { class: 'small' });
  const selectedNames = el('ul', { class: 'research-selected' });
  const copyNotice = el('p', { class: 'small', role: 'status' });
  const command = el('textarea', { readonly: true, rows: 2, 'aria-label': 'Text für den Claude-Chat' });
  const copyButton = el('button', { type: 'button', onclick: async () => {
    try { await navigator.clipboard.writeText(command.value); if (live()) copyNotice.textContent = 'Kopiert. Füge den Text im Claude-Chat ein.'; }
    catch { if (live()) { command.focus(); command.select(); copyNotice.textContent = 'Bitte den markierten Text von Hand kopieren.'; } }
  } }, 'Text kopieren');
  const handoff = el('div', { class: 'research-handoff', hidden: true },
    el('p', {}, 'Kopiere den Text in den Claude-Chat. Die Recherche startet dort erst, wenn du ihn sendest.'), command, copyButton, copyNotice);
  const refresh = el('button', { type: 'button', onclick: () => load() }, 'Recherche-Status aktualisieren');
  const submit = el('button', { type: 'button', class: 'primary', onclick: () => create() }, 'Lücken füllen (0)');
  const clear = el('button', { type: 'button', onclick: () => { selected.clear(); sync(); } }, 'Auswahl leeren');
  const options = el('fieldset', { class: 'research-fields' }, el('legend', {}, 'Was soll nachrecherchiert werden?'));
  for (const [key, label] of [['zimmerkategorien', 'Zimmer und Betten'], ['gesamtpreis', 'Gesamtpreis'], ['balkon', 'Balkon'], ['storno', 'Stornierung']]) {
    const input = el('input', { type: 'checkbox', onchange: sync }); input.checked = key === 'zimmerkategorien'; fields.set(key, input);
    options.append(el('label', { class: 'check-label' }, input, label));
  }
  const hint = el('textarea', { rows: 2, maxlength: 1000, 'aria-label': 'Hinweis für die Nachrecherche', placeholder: 'Optionaler Hinweis, maximal 1000 Zeichen' });
  const panel = el('details', { class: 'research-panel' }, el('summary', {}, 'Offene Angaben nachrecherchieren'),
    el('p', {}, 'Wähle bis zu 30 Treffer mit offenen Angaben in Liste B. Die Auswahl bleibt beim Filtern und Blättern erhalten.'),
    selectionText, selectedNames, options, hint, el('div', { class: 'actions' }, submit, clear, refresh), notice, handoff,
    el('p', { class: 'small muted' }, 'Status aus den letzten 50 Recherche-Aufträgen. Der Auftrag ergänzt Angaben; er ändert keine Suchkriterien.'));
  const chosenFields = () => [...fields].filter(([, input]) => input.checked).map(([key]) => key);
  const currentOrders = () => orders.filter(o => o.suchauftrag_id === id && Array.isArray(o.treffer_ids));
  function sync() {
    submit.textContent = `Lücken füllen (${selected.size})`;
    submit.disabled = writing || loading || uncertain || !selected.size || !chosenFields().length;
    refresh.disabled = loading || writing; clear.disabled = writing || !selected.size;
    hint.disabled = writing; fields.forEach(input => { input.disabled = writing; });
    selectionText.textContent = `${selected.size} von höchstens 30 ausgewählt.`;
    selectedNames.replaceChildren(...rows.filter(t => selected.has(t.treffer_id)).map(t => el('li', {}, t.name || 'Unterkunft ' + t.treffer_id)));
    for (const { t, checkbox, status } of rowRefs) {
      checkbox.checked = selected.has(t.treffer_id);
      checkbox.disabled = writing || (!checkbox.checked && selected.size >= 30);
      const jobs = currentOrders().filter(o => o.treffer_ids.includes(t.treffer_id)).sort((a, b) => b.id - a.id);
      status.replaceChildren(...jobs.map(o => el('div', {}, `Recherche #${o.id}: ${LUECKEN_STATUS[o.status] || 'Status unbekannt'}`,
        ['erzeugt', 'in_arbeit'].includes(o.status) ? el('button', { type: 'button', onclick: () => { showHandoff(o); panel.scrollIntoView({ block: 'center' }); command.focus({ preventScroll: true }); } }, `Text für Auftrag #${o.id}`) : null)));
      if (!loaded && !jobs.length) status.textContent = 'Recherche-Status noch nicht geladen.';
    }
  }
  function showHandoff(order, text) {
    handoffId = order.id;
    const active = ['erzeugt', 'in_arbeit'].includes(order.status);
    command.value = text || `Lückenfüller Auftrag ${order.id} ausführen`;
    handoff.hidden = !active; copyNotice.textContent = '';
    if (active) panel.open = true;
  }
  async function load() {
    if (loading || writing || !live()) return;
    loading = true; notice.textContent = 'Recherche-Status wird geladen …'; sync();
    try {
      const r = await call('unterkunft_lueckenfueller_lesen');
      if (!live()) return;
      if (r.ok !== true || !Array.isArray(r.auftraege) || r.auftraege.some(o => !o || !Number.isSafeInteger(o.id) || !Array.isArray(o.treffer_ids) || (o.felder != null && !Array.isArray(o.felder)))) throw new Error('Statusantwort unvollständig.');
      orders = r.auftraege; loaded = true; uncertain = false;
      notice.textContent = 'Recherche-Status aktualisiert.';
      if (handoffId !== null) {
        const shown = currentOrders().find(o => o.id === handoffId);
        if (shown) showHandoff(shown); else handoff.hidden = true;
      }
      if (attempt) {
        const match = currentOrders().filter(o => JSON.stringify([...o.treffer_ids].sort((a,b)=>a-b)) === JSON.stringify(attempt.data.treffer_ids) &&
          JSON.stringify([...(o.felder || [])].sort()) === JSON.stringify([...attempt.data.felder].sort())).sort((a,b)=>b.id-a.id)[0];
        if (match) { showHandoff(match); notice.textContent = `Auftrag #${match.id}: ${LUECKEN_STATUS[match.status] || match.status}.`; }
      }
    } catch (e) { if (live()) notice.textContent = 'Recherche-Status nicht geladen: ' + e.message; }
    finally { loading = false; if (live()) { sync(); changed(); } }
  }
  async function create() {
    if (writing || loading || uncertain || !selected.size || selected.size > 30 || !chosenFields().length) return;
    const ids = [...selected].filter(key => rows.some(t => t.treffer_id === key && sucheLueckenKandidat(t))).sort((a,b)=>a-b);
    if (ids.length !== selected.size) { notice.textContent = 'Die Auswahl hat sich geändert. Bitte die Treffer erneut auswählen.'; return; }
    const data = { treffer_ids: ids, felder: chosenFields(), hinweis: hint.value.trim() };
    const key = JSON.stringify(data);
    if (attempt?.key !== key) attempt = { key, data: { ...data, idempotenz: crypto.randomUUID() } };
    writing = true; notice.textContent = 'Recherche-Auftrag wird angelegt …'; sync();
    try {
      const r = await call('unterkunft_lueckenfueller_anlegen', attempt.data);
      if (!live()) return;
      if (r.ok !== true || !Number.isSafeInteger(r.id) || r.id <= 0 || !LUECKEN_STATUS[r.status] || r.vorgefuellter_text !== `Lückenfüller Auftrag ${r.id} ausführen`) throw new Error('Der Auftrag wurde nicht eindeutig bestätigt.');
      const order = { id: r.id, status: r.status, suchauftrag_id: id, treffer_ids: ids, felder: data.felder };
      orders = [order, ...orders.filter(o => o.id !== r.id)]; selected.clear();
      notice.textContent = `Auftrag #${r.id} ${r.schon_vorhanden ? 'bereits vorhanden' : 'angelegt'}. ${LUECKEN_STATUS[r.status]}.`;
      showHandoff(order, r.vorgefuellter_text);
    } catch (e) { if (live()) { uncertain = true; notice.textContent = 'Anlegen nicht bestätigt: ' + e.message + ' Bitte zuerst den Recherche-Status aktualisieren.'; } }
    finally { writing = false; if (live()) { sync(); changed(); } }
  }
  return {
    panel, load,
    update(allRows) {
      rows = allRows; rowRefs = [];
      for (const key of selected) if (!rows.some(t => t.treffer_id === key && sucheLueckenKandidat(t))) selected.delete(key);
      sync();
    },
    row(t) {
      const status = el('div', { class: 'small', 'data-research-status': t.treffer_id });
      const checkbox = el('input', { type: 'checkbox', 'aria-label': 'Für Nachrecherche auswählen: ' + t.name, onchange: () => {
        if (checkbox.checked && selected.size < 30) selected.add(t.treffer_id); else selected.delete(t.treffer_id);
        panel.open = true; sync();
      } });
      const box = el('div', { class: 'stay-research' }, sucheLueckenKandidat(t) ? el('label', { class: 'check-label' }, checkbox, 'Offene Angaben nachrecherchieren') : null, status);
      rowRefs.push({ t, checkbox, status }); sync(); return box;
    }
  };
}
