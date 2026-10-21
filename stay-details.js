/* Nachweise und Details getrennt von Ranking und persönlicher Auswahl. */
'use strict';
function sucheAbruf(value) {
  if (!value || !['string', 'number'].includes(typeof value)) return 'nicht geliefert';
  const d = new Date(value);
  return Number.isNaN(d.getTime()) ? 'nicht geliefert' : d.toLocaleString('de-DE', { dateStyle: 'short', timeStyle: 'short' });
}
function sucheDeckung(data) {
  const missing = Array.isArray(data?.fehlend) ? data.fehlend : [];
  const complete = data?.vollstaendig === true && !missing.length;
  return el('div', { class: complete ? 'coverage-note small' : 'coverage-note erg-warnung', role: complete ? 'note' : 'status' },
    el('strong', {}, complete ? 'Alle vorgesehenen Quellen sind abgeschlossen.' : data?.vollstaendig === false || missing.length ? 'Keine vollständige Marktsuche.' : 'Quellenabdeckung noch nicht bestätigt.'),
    missing.length ? el('p', {}, 'Offen oder fehlend: ' + missing.map(v => { const key = typeof v === 'string' ? v : v?.quelle || 'unbekannt'; return SUCHE_QUELLEN[key] || key; }).join(', ')) : null,
    data?.hinweis ? el('p', {}, String(data.hinweis)) : null);
}
function sucheVerfuegbarkeit(a) {
  return a?.verfuegbar === 'belegt' || a?.verfuegbar === true ? 'Verfügbarkeit belegt beim Abruf' :
    a?.verfuegbar === false || ['nicht_verfuegbar', 'nein', 'ausgebucht'].includes(a?.verfuegbar) ? 'Laut Quelle nicht verfügbar' : 'Verfügbarkeit unbelegt';
}
function sucheBalkon(t) {
  const parse = value => value === true || value === 'ja' ? true : value === false || value === 'nein' ? false : null;
  const categories = Array.isArray(t.kategorien) ? t.kategorien.filter(k => k && typeof k === 'object') : [];
  const matching = categories.filter(k => k.name && k.name === t.angebot?.kategorie_name);
  const vals = (matching.length ? matching : categories).map(k => parse(k.balkon));
  if (vals.includes(true)) return matching.length || (vals.length && vals.every(v => v === true)) ? 'ja' : 'ja, bei mindestens einer Zimmerkategorie';
  if (vals.length && vals.every(v => v === false)) return 'nein';
  if (vals.some(v => v !== null)) return 'unbekannt';
  const wish = t.bewertung?.filter_ergebnis?.wunsch?.balkon;
  return wish === true ? 'ja' : wish === false ? 'nein' : 'unbekannt';
}
function sucheAngebotsstand(t, a = t.angebot || {}) {
  return el('div', { class: 'offer-evidence small' },
    t.preis_veraltet === true ? el('span', { class: 'suche-warning' }, 'Preis veraltet – älter als 48 Stunden') : null,
    el('div', {}, sucheVerfuegbarkeit(a)), el('div', {}, 'Abruf: ' + sucheAbruf(a.abrufzeit)),
    el('div', { class: 'muted' }, 'Aktuelle Buchbarkeit beim Anbieter prüfen.'));
}
function sucheDetailTabelle(caption, labels, rows) {
  return el('div', { class: 'detail-table-scroll', tabindex: 0, role: 'region', 'aria-label': caption },
    el('table', { class: 'detail-table' }, el('caption', {}, caption),
      el('thead', {}, el('tr', {}, labels.map(label => el('th', { scope: 'col' }, label)))),
      el('tbody', {}, rows.map(row => el('tr', {}, row.map(value => el('td', {}, value == null ? 'unbekannt' : value)))))));
}
function sucheKategorien(t) {
  const rows = Array.isArray(t.kategorien) ? t.kategorien.filter(k => k && typeof k === 'object') : [];
  if (!rows.length) return el('p', {}, 'Noch keine Zimmerkategorien belegt.');
  return sucheDetailTabelle('Zimmerkategorien mit Nachweisen', ['Kategorie', 'm²', 'Schlafzimmer', 'Betten', 'Personen', 'Balkon', 'Quelle', 'Abruf'], rows.map(k => [
    k.name || 'unbekannt', sucheZahl(k.m2), sucheZahl(k.schlafzimmer),
    (sucheZahl(k.betten_anzahl) ?? 'unbekannt') + (k.betten_eindeutig === false ? ' · Art nicht eindeutig' : ''), sucheZahl(k.max_personen),
    ['ja','nein'].includes(k.balkon) ? k.balkon : k.balkon === true ? 'ja' : k.balkon === false ? 'nein' : 'unbekannt',
    SUCHE_QUELLEN[k.quelle] || k.quelle || 'unbekannt', sucheAbruf(k.abrufzeit)
  ]));
}
function sucheKandidat(t, final, suchauftragId) {
  const b = t.bewertung || {}, a = t.angebot || {}, review = b.gegenpruefung?.pruefung;
  const allOffers = [a, ...(Array.isArray(t.weitere_angebote) ? t.weitere_angebote : [])].filter(v => v && typeof v === 'object');
  const dialog = el('dialog', { class: 'stay-candidate', 'aria-label': 'Unterkunft im Detail: ' + (t.name || 'Unterkunft') });
  dialog.append(el('div', { class: 'candidate-header' }, el('h2', {}, t.name || 'Unterkunft'),
    !SUCHE_SCORE_AN && typeof stayIcon === 'function' ? el('button', { type: 'button', class: 'a-zu', 'aria-label': 'Details schließen', onclick: () => dialog.close() }, stayIcon('raus')) : el('button', { type: 'button', onclick: () => dialog.close() }, 'Details schließen')),
    stayGallery(t), ...[sucheViertelLink(t.zone, suchauftragId)].filter(Boolean), el('p', {}, 'Balkon: ' + sucheBalkon(t)), sucheAngebotsstand(t),
    ...(!SUCHE_SCORE_AN ? [] : [el('p', {}, (final ? 'Passung' : 'Vorläufige Passung') + ': ' + (sucheZahl(b.score) ?? 'unbekannt') + '/100 · Datenlage: ' + (sucheDatenlage(t) ?? 'unbekannt') + ' %'),
    sucheDetailTabelle('Teilnoten und Gewichtung', ['Kriterium', 'Note von 10', 'Gewicht (%)'], SUCHE_NOTEN.map(([key, label]) => [label, sucheZahl(b.spaltennoten?.[key]), sucheZahl(b.spaltennoten?.gewichte?.[key])])),
    el('h3', {}, 'Begründung'), el('p', {}, b.begruendung || 'Noch keine Begründung verfügbar.'),
    el('h3', {}, 'Gegenprüfung'), el('p', {}, review?.urteil === 'ok' ? 'Keine Einwände in der Gegenprüfung.' : review?.urteil === 'einwand' ? 'Gegenprüfung hat Einwände.' : 'Noch keine Gegenprüfung vorhanden.'),
    el('ul', {}, (Array.isArray(review?.einwaende) ? review.einwaende : []).map(v => el('li', {}, typeof v === 'string' ? v : renderAny(v))))]),
    ...[review?.hinweis ? el('p', {}, review.hinweis) : null].filter(Boolean),
    el('p', {}, 'Offene Prüfpunkte: ' + (sucheTexte(b.gegenpruefung?.luecken).join(', ') || 'keine angegeben')),
    el('p', {}, 'Ausschlussgrund: ' + (t.ko_grund || (t.status === 'ausgeschlossen' ? 'von dir ausgeschlossen' : 'keiner angegeben'))),
    sucheKategorien(t), el('h3', {}, 'Alle Angebote nach Quelle'), el('p', { class: 'small' }, 'Zimmer und Bedingungen können abweichen. Angebote sind nicht automatisch gleichwertig.'),
    ...allOffers.map((offer, i) => {
      const link = sucheLink(offer.link);
      return el('section', { class: 'candidate-offer' }, el('h4', {}, (offer.anbieter || SUCHE_QUELLEN[offer.quelle || (i === 0 ? t.quelle : '')] || offer.quelle || 'Quelle unbekannt') + (i === 0 ? ' · Hauptangebot' : '')),
        el('p', {}, (offer.preis_art === 'geschaetzt' ? 'ca. ' : '') + sucheEuro(offer.preis_gesamt_eur)),
        sucheAngebotsstand({ preis_veraltet: offer.preis_veraltet === true || (i === 0 && t.preis_veraltet === true) }, offer),
        el('p', {}, 'Zimmer: ' + (offer.kategorie_name || 'unbekannt')), el('p', {}, 'Stornierung: ' + (offer.storno || 'unbekannt')),
        link ? el('a', { href: link, target: '_blank', rel: 'noopener noreferrer' }, 'Beim Anbieter öffnen ↗') : el('p', {}, 'Kein sicherer Angebotslink vorhanden.'));
    }),
    sucheDetailTabelle('Gästenoten nach Quelle', ['Quelle', 'Note', 'Skala', 'Bewertungen'], allOffers.map((offer, i) => [
      offer.anbieter || SUCHE_QUELLEN[offer.quelle || (i === 0 ? t.quelle : '')] || offer.quelle || 'unbekannt',
      sucheZahl(i === 0 ? t.note : offer.note), sucheZahl(i === 0 ? t.note_skala : offer.note_skala), sucheZahl(i === 0 ? t.bewertungen : offer.bewertungen)
    ])), el('p', { class: 'small muted' }, 'Die angezeigte Gästenote ist auf Booking-Niveau geeicht. Die Tabelle zeigt die Originalnoten. Fehlende Noten anderer Quellen werden nicht aus der Hauptquelle übernommen.'),
    el('h3', {}, 'Bildbewertung'), el('p', {}, 'KI-Einschätzung der Bilder; kein Nachweis der Ausstattung.'),
    el('p', {}, b.bild_urteil?.ein_satz || 'Noch keine Bildbewertung vorhanden.'),
    ...[b.bild_urteil ? sucheBalken(b.bild_urteil, [['hell','Hell'],['modern','Modern'],['gepflegt','Gepflegt'],['geraeumig','Geräumig']]) : null].filter(Boolean));
  // W98c D2: ohne Score zuerst die Angaben (Schnell-Infos + Info-Box nach Themen), Technisches eingeklappt darunter
  if (!SUCHE_SCORE_AN && typeof stayReviewInfo === 'function') {
    const gallery = dialog.querySelector(':scope > .stay-gallery'), anchor = gallery || dialog.querySelector(':scope > .candidate-header');
    const rest = []; let n = anchor.nextSibling; while (n) { rest.push(n); n = n.nextSibling; }
    const mehr = el('details', { class: 'candidate-mehr' }, el('summary', {}, 'Mehr: Angebote je Quelle, Zimmerarten, Bildbewertung'));
    mehr.append(...rest);
    anchor.after(typeof stayDetailA === 'function' ? stayDetailA(t, t._trip || {}) : stayReviewInfo(t, t._trip || {}), mehr); // 0.36.4: A-Stil
  }
  return dialog;
}

function sucheMerkliste(entries) {
  if (!Array.isArray(entries) || entries.some(t => !t || !viertelId(t.treffer_id) || !viertelId(t.suchauftrag_id))) throw new Error('Die Antwort ist unvollständig. Bitte erneut lesen.');
  const view = el('div', { class: 'saved-trips' }), groups = new Map();
  if (!entries.length) return el('p', { class: 'stay-empty' }, 'Noch keine Favoriten. Mit „Favorit“ sammelst du Unterkünfte hier über alle Reisen.');
  for (const t of entries) { if (!groups.has(t.suchauftrag_id)) groups.set(t.suchauftrag_id, []); groups.get(t.suchauftrag_id).push(t); }
  for (const [id, rows] of groups) {
    rows.sort((a,b)=>(a.eigener_rang??Infinity)-(b.eigener_rang??Infinity));
    const trip = rows[0];
    const section = el('section', { class: 'saved-trip', 'data-saved-trip': id },
      el('h3', {}, trip.ziel || 'Suche #' + id), el('p', { class: 'small' }, `${fmtDate(trip.anreise)}–${fmtDate(trip.abreise)} · ${rows.length} Favoriten`));
    for (const t of rows) {
      const href = '#/suche/' + id + '?favoriten=1&treffer=' + t.treffer_id, offer = sucheLink(t.link);
      const name = t.name || 'Unterkunft ' + t.treffer_id;
      if (!SUCHE_SCORE_AN) { // 0.36.4 (Sebastian 21.10.): Favoriten kompakt wie die Liste – Foto, Name, Preis, Symbol-Knöpfe
        const note = sucheZahl(t.note) !== null && sucheZahl(t.note_skala) ? Number(t.note) / Number(t.note_skala) * 10 : null;
        const naechte = Math.round((Date.parse(t.abreise) - Date.parse(t.anreise)) / 86400000), preis = sucheZahl(t.preis_gesamt_eur), ca = t.preis_art === 'geschaetzt' ? 'ca. ' : '';
        const euro = x => Math.round(x).toLocaleString('de-DE') + ' €';
        const rund = (attrs, icon) => el(attrs.href ? 'a' : 'button', { ...(attrs.href ? {} : { type: 'button' }), class: 'a-fav-knopf', ...attrs }, stayIcon(icon));
        section.append(el('article', { class: 'saved-stay a-fav', 'data-saved-hit': t.treffer_id },
          el('a', { href, class: 'a-fav-foto', 'aria-label': name + ' im Suchlauf zeigen' }, sucheFoto(t)),
          el('div', { class: 'a-fav-text' }, el('a', { href, class: 'saved-stay-name' }, name),
            el('p', { class: 'a-fav-meta' }, [SUCHE_QUELLEN[t.quelle] || t.quelle, note !== null ? '★ ' + note.toLocaleString('de-DE', { maximumFractionDigits: 1 }) : null, sucheZahl(t.bewertungen) !== null ? '(' + Number(t.bewertungen).toLocaleString('de-DE') + ')' : null].filter(Boolean).join(' · ')),
            el('p', { class: 'a-fav-stand', title: 'Aktuelle Buchbarkeit beim Anbieter prüfen.' }, 'Preisstand ' + sucheAbruf(t.preis_abrufzeit))),
          el('div', { class: 'a-fav-preis' }, el('strong', {}, preis === null ? '? €' : ca + euro(preis)), preis !== null && naechte > 0 ? el('small', {}, euro(preis / naechte) + '/N') : null),
          el('div', { class: 'a-fav-knoepfe' }, offer ? rund({ href: offer, target: '_blank', rel: 'noopener noreferrer', 'aria-label': 'Angebot öffnen', title: 'Angebot öffnen' }, 'extern') : null,
            rund({ href, 'aria-label': 'Im Suchlauf zeigen', title: 'Im Suchlauf zeigen' }, 'liste'),
            rund({ onclick: () => tripBookFromSearch(t, id), 'aria-label': 'Als gebucht markieren', title: 'Als gebucht markieren', class: 'a-fav-knopf is-buchen' }, 'kalender'))));
        continue;
      }
      section.append(el('article', { class: 'saved-stay', 'data-saved-hit': t.treffer_id }, sucheFoto(t),
        el('div', {}, el('a', { href, class: 'saved-stay-name' }, name), t.eigener_rang ? el('p',{},'Dein Rang '+t.eigener_rang) : null,
          el('p', { class: 'small' }, (SUCHE_QUELLEN[t.quelle] || t.quelle || 'Quelle unbekannt') + ' · ' +
            (t.topf === 'ausgeschlossen' ? 'Fachlich ausgeschlossen' : t.topf === 'unbewertet' ? 'Noch nicht vollständig bewertet' : ['A','B'].includes(t.liste) ? (t.liste === 'A' ? 'Passende Treffer' : 'Angaben offen') + (SUCHE_SCORE_AN && sucheZahl(t.rang) !== null ? ' · Rang ' + t.rang : '') : 'Bewertung unbekannt')),
          el('p', {}, (t.preis_art === 'geschaetzt' ? 'ca. ' : '') + sucheEuro(t.preis_gesamt_eur) + (sucheZahl(t.preis_gesamt_eur) !== null ? ' gesamt' : '')),
          el('p', { class: 'small muted' }, 'Preisstand: ' + sucheAbruf(t.preis_abrufzeit) + '. Aktuelle Buchbarkeit beim Anbieter prüfen.'),
          el('details', {}, el('summary', {}, 'Bewertung und Favoritendatum'),
            el('p', { class: 'small' }, (SUCHE_SCORE_AN ? 'Passung: ' + (sucheZahl(t.score) ?? 'unbekannt') + '/100 · ' : '') + 'Gästenote: ' + (sucheZahl(t.note) ?? 'unbekannt') + ' / ' + (sucheZahl(t.note_skala) ?? '?') + ' · ' + (sucheZahl(t.bewertungen) ?? 'unbekannt') + ' Bewertungen'),
            el('p', { class: 'small' }, 'Als Favorit gespeichert: ' + sucheAbruf(t.gemerkt_am))),
          el('div', { class: 'actions' }, el('a', { href }, 'Im Suchlauf zeigen'), el('button',{type:'button',onclick:()=>tripBookFromSearch(t,id)},'Als gebucht markieren'), offer ? el('a', { href: offer, target: '_blank', rel: 'noopener noreferrer' }, 'Angebot öffnen ↗') : null))));
    }
    view.append(section);
  }
  return view;
}
