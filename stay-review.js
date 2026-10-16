/* Gemeinsame, quellengebundene Kurzansicht und persönliches Durchsehen. */
'use strict';

function sucheBettenDeutsch(value) {
  return String(value || '').replace(/\bBedroom\b/gi,'Schlafzimmer').replace(/\bLiving room\b/gi,'Wohnzimmer').replace(/\bsofa beds?\b/gi, 'Schlafsofa').replace(/\b(?:double|full) beds?\b/gi, 'Doppelbett')
    .replace(/\b(?:single|twin) beds?\b/gi, 'Einzelbett').replace(/\bqueen beds?\b/gi, 'Queensize-Bett')
    .replace(/\bking beds?\b/gi, 'Kingsize-Bett').replace(/\bbunk beds?\b/gi, 'Etagenbett')
    .replace(/\bfuton beds?\b/gi, 'Futon').replace(/\bfutons?\b/gi, 'Futon').replace(/\btwin\b/gi,'Einzelbett').replace(/\bdouble\b/gi,'Doppelbett').replace(/\band\b/gi, 'und');
}
function sucheWegText(t) {
  const min = sucheZahl(t.gehzeit_min), rawStation = typeof t.station_name === 'string' && t.station_name.trim();
  const station = rawStation && !/^(station|bahnhof|unknown|unbekannt)$/i.test(rawStation) ? rawStation : null;
  if (min === null || min < 0) return station ? 'Fußweg zu ' + station + ' unbekannt' : 'Fußweg und Station unbekannt';
  const rounded = Math.round(min), time = rounded >= 60 ? Math.floor(rounded / 60) + ' Std. ' + rounded % 60 + ' Min.' : rounded + ' Min.';
  return (t.gehzeit_art === 'geschaetzt' ? 'ca. ' : '') + time + ' zu Fuß · ' + (station || 'Zielstation nicht angegeben') +
    (t.gehzeit_art === 'geschaetzt' ? ' (geschätzt)' : !['route', 'ors'].includes(t.gehzeit_art) ? ' (Berechnung unbekannt)' : '');
}
function sucheAnbieterLink(t) {
  const original = sucheLink(t.angebot?.link);
  if (!original) return null;
  const u = new URL(original), id = u.searchParams.get('f_no');
  // Rakuten API redirects may lead to login. The hotel ID identifies the public overview, not an offer.
  if (['img.travel.rakuten.co.jp', 'hotel.travel.rakuten.co.jp'].includes(u.hostname) && /^[1-9]\d*$/.test(id || '')) {
    return { url: 'https://travel.rakuten.co.jp/HOTEL/' + id + '/' + id + '.html', label: 'Hotel bei Rakuten ansehen ↗', overview: true };
  }
  return { url: original, label: 'Bei ' + (t.angebot?.anbieter || SUCHE_QUELLEN[t.quelle] || 'Anbieter') + ' ansehen ↗', overview: false };
}
function sucheKernDaten(t, nights) {
  const room = sucheZimmerKurz(t), category = sucheAngebotsKategorie(t), a = t.angebot || {};
  const total = sucheZahl(a.preis_gesamt_eur), estimated = a.preis_art === 'geschaetzt' || t.bewertung?.preis_geschaetzt;
  const area = room.m2 === null ? 'Fläche unbekannt' : room.m2.toLocaleString('de-DE') + ' m²';
  const bedrooms = room.schlafzimmer === null ? 'Schlafzimmer unbekannt' : room.schlafzimmer + ' Schlafzimmer laut Anbieter';
  const hotel = ['hotel','ryokan'].includes(t.typ);
  return el('div', { class: 'stay-key-facts' },
    el('p', { class: 'stay-total' }, (estimated && total !== null ? 'ca. ' : '') + sucheEuro(total), el('span', {}, ' gesamt für alle Reisenden')),
    nights > 0 && total !== null ? el('p', { class: 'small' }, (estimated ? 'ca. ' : '') + sucheEuro(total / nights) + ' pro Nacht · ' + nights + ' Nächte' + (estimated ? ' · geschätzt' : '')) : null,
    el('p', { class: 'stay-space' }, el('strong', {}, area), ' · ', bedrooms),
    hotel ? el('p', { class: 'small' }, 'Hotelzimmer · Zimmeraufteilung und Verbindung prüfen') : null,
    el('p', {}, sucheBettenDeutsch(room.typen) || 'Bettentypen unbekannt'),
    category?.konflikt ? el('p', { class: 'warning' }, 'Zimmerangaben widersprüchlich') : null,
    el('p', {}, sucheWegText(t)),
    t.zone?.name ? el('p', {}, 'Viertel: ' + t.zone.name) : null,
    el('p', { class: 'small' }, sucheZahl(t.note) === null ? 'Noch keine Gästenote bekannt' : 'Gäste: ' + t.note + ' / ' + (t.note_skala ?? '?') + ' · ' + (SUCHE_QUELLEN[t.quelle] || t.quelle || 'Quelle unbekannt') + (t.bewertungen != null ? ' · ' + t.bewertungen + ' Bewertungen' : '')),
    sucheWarnungen(t).length ? el('details', { class: 'stay-key-warnings' }, el('summary', {}, sucheWarnungen(t).length + ' Hinweise zum Angebot'), el('ul', {}, sucheWarnungen(t).map(w => el('li', {}, SUCHE_WARNUNGEN[w] || 'Weiterer Prüfhinweis: ' + w)))) : null);
}
function sucheDurchsehen(rows, { call, live, changed, uncertain, nights, parent }) {
  const verdict = t => ({ favorit: 'favorit', vielleicht: 'vielleicht', ausgeschlossen: 'weg' }[t.status] || 'offen');
  const active = rows.filter(t => !['ausgeschlossen','unbewertet'].includes(t.topf) && ['A','B'].includes(t.bewertung?.liste));
  const prior = active.filter(t => ['favorit','weg'].includes(verdict(t)) && !t.urteil_uebernommen?.hinweis);
  const eligible = active.filter(t => !prior.includes(t));
  const ordered = eligible.sort((a,b) => Number(verdict(a) === 'vielleicht') - Number(verdict(b) === 'vielleicht') ||
    Number(!!a.urteil_uebernommen) - Number(!!b.urteil_uebernommen) ||
    Number(a.bewertung?.liste === 'B') - Number(b.bewertung?.liste === 'B') || sucheVergleich(a,b,'rang',1));
  let queue = [...ordered], index = 0, pending = false, blocked = false, last = null, providerReturn = null, removed = false;
  const revisited = new Set(ordered.filter(t => verdict(t) === 'vielleicht').map(t => t.treffer_id));
  const dialog = el('dialog', { class: 'stay-review', 'aria-label': 'Unterkünfte durchsehen' });
  const content = el('div',{class:'review-content'}), decisions = el('div',{class:'review-decisions'}), message = el('p', {role:'status', class:'review-message'}), reasonBox = el('div', {class:'review-reasons'});
  const close = el('button', {type:'button', onclick:() => dialog.close()}, 'Durchsehen beenden');
  const undo = el('button', {type:'button', hidden:true, onclick:() => save(last.t, last.before, true, last.beforeReasons)}, 'Letzte Entscheidung rückgängig');
  dialog.append(el('div',{class:'review-toolbar'},close,undo), message, reasonBox, content, decisions);
  function cleanup() { removed = true; document.removeEventListener('visibilitychange', returned); dialog.remove(); }
  dialog.addEventListener('close', cleanup, {once:true});
  function returned() {
    if (document.visibilityState === 'visible' && providerReturn && !removed) {
      message.textContent = 'Zurück von der Anbieter-Seite: Wie gefällt dir ' + providerReturn.name + '? Favorit, Na ja oder Weg?';
      providerReturn = null;
    }
  }
  document.addEventListener('visibilitychange', returned);
  async function save(t, choice, isUndo = false, reasons = []) {
    if (pending || blocked || !t || removed) return;
    pending = true; const before = verdict(t), beforeReasons = t.urteil_gruende || [];
    message.textContent = 'Entscheidung wird gespeichert …'; setDisabled();
    try {
      const r = await call('unterkunft_durchsehen_urteil', {treffer_id:t.treffer_id, urteil:choice, gruende:reasons});
      if (!live() || removed) return;
      const status = {favorit:'favorit', vielleicht:'vielleicht', weg:'ausgeschlossen', offen:'aktiv'}[choice];
      if (r?.ok !== true || r.treffer_id !== t.treffer_id || r.urteil !== choice || r.status !== status) throw new Error('Keine eindeutige Bestätigung erhalten.');
      t.status = status; t.urteil_gruende = reasons; changed(t);
      if (isUndo) { index = last.index; queue = last.queue; revisited.clear(); last.revisited.forEach(id=>revisited.add(id)); last = null; reasonBox.replaceChildren(); }
      else if (!reasons.length) {
        last = {t, before, beforeReasons, index, queue:[...queue], revisited:[...revisited]};
        if (choice === 'vielleicht' && !revisited.has(t.treffer_id)) { queue.push(t); revisited.add(t.treffer_id); }
        index++; showReasons(t, choice);
      }
      message.textContent = isUndo ? 'Entscheidung zurückgenommen.' : 'Gespeichert: ' + ({favorit:'Favorit',vielleicht:'Na ja',weg:'Weg',offen:'Offen'}[choice]) + ' · ' + t.name;
    } catch(e) { blocked = true; uncertain?.(t); message.textContent = 'Speichern nicht bestätigt: ' + e.message + ' Durchsehen beenden und die Suche aktualisieren, bevor du erneut entscheidest.'; }
    finally { pending = false; if (!removed && live()) render(); }
  }
  function showReasons(t, choice) {
    const plus = choice === 'favorit';
    const reasons = plus ? [['plus_groesse','Größe'],['plus_lage','Lage'],['plus_stil','Stil'],['plus_preis','Preis'],['plus_ausstattung','Ausstattung'],['plus_fotos','Fotos'],['plus_betten','Betten']] : [['zu_klein','Zu klein'],['lage','Lage'],['stil','Stil'],['preis','Preis'],['betten','Betten'],['fotos','Fotos'],['sonstiges','Sonstiges']];
    reasonBox.replaceChildren(el('span',{},'Optionaler Grund für ' + t.name + ': '), ...reasons.map(([id,label]) => el('button',{type:'button',onclick:async()=>{await save(t, choice, false, [id]); if(!blocked) reasonBox.replaceChildren();}},label)), el('button',{type:'button',onclick:()=>reasonBox.replaceChildren()},'Überspringen'));
  }
  function setDisabled() { dialog.querySelectorAll('button').forEach(b => { if(b !== close) b.disabled = pending || blocked; }); close.disabled = pending; }
  function render() {
    undo.hidden = !last;
    content.replaceChildren();
    decisions.replaceChildren();
    const t = queue[index];
    if (!t) content.append(el('h2', {}, 'Alles durchgesehen'), el('p', {}, 'Deine Favoriten findest du über „Nur Gemerkte“. „Na ja“ bleibt für später erhalten.'));
    else {
      const link = sucheAnbieterLink(t), inherited = t.urteil_uebernommen;
      content.append(el('div',{},el('p',{class:'review-progress'}, (index + 1) + ' / ' + queue.length + ' · ' + eligible.filter(row=>!row.urteil_uebernommen && verdict(row)==='offen').length + ' neu · ' + prior.length + ' bereits entschieden'),
        sucheFoto(t), el('h2',{},t.name || 'Unterkunft'),
        el('p',{class:'small'},'Liste ' + t.bewertung.liste + (t.bewertung.rang != null ? ' · Rang ' + t.bewertung.rang : '') + (verdict(t) === 'vielleicht' ? ' · letztes Mal: Na ja' : '')),
        inherited?.hinweis ? el('p',{class:'warning'},String(inherited.hinweis)) : null,
        sucheKernDaten(t,nights),
        el('details',{},el('summary',{},'Zimmerangaben und Begründung'),sucheZimmerDetails(t),el('p',{},t.bewertung?.begruendung || 'Keine Begründung vorhanden.')),
        link ? el('a',{href:link.url,target:'_blank',rel:'noopener noreferrer',onclick:()=>{providerReturn=t;}},link.label) : el('p',{},'Kein Anbieter-Link vorhanden'),
        link?.overview ? el('p',{class:'small'},'Hotelübersicht; Reisedaten und konkretes Angebot dort prüfen.') : null));
      decisions.append(...[['weg','Weg'],['vielleicht','Na ja'],['favorit','★ Favorit']].map(([choice,label])=>el('button',{type:'button',class:choice==='favorit'?'primary':'',onclick:()=>{reasonBox.replaceChildren(); save(t,choice);}},label)));
    }
    setDisabled();
    content.scrollTop=0;
  }
  // Prevent dismissal during an uncertain write; no optimistic removal of an accommodation.
  dialog.addEventListener('cancel',e=>{if(pending)e.preventDefault();});
  parent.append(dialog); render(); dialog.showModal();
  return {destroy:()=>{if(dialog.open)dialog.close();else cleanup();}};
}
