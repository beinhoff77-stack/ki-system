/* W150: Lernen Schule – Lernreise der Kinder in der App.
   Spricht mit der Serverfunktion lernen-api (gleiche Anmeldung wie app-api). Die Datenbank prüft Zugriff,
   bewertet Antworten und führt Lernstand, Sterne und Stempel; die App zeigt nur an und schickt Eingaben.
   Ansichten:
     #/lernen                      Eltern: Mathe-Merkblatt, Lernreisen der Kinder, Belohnungen und Einlösungen
     #/reise/<kind>                Kind: Heute dran (aktueller Ort auf der echten Weltkarte)
     #/weltkarte/<kind>            Kind: Weltkarte, Kontinente und Orte
     #/weg/<kind>                  Kind: Mein Weg – kann ich · gerade dran · kommt noch
     #/merkheft/<kind>             Kind: Merkheft – Spickzettel aller geschafften Etappen, durchsuchbar
     #/reisepass/<kind>            Kind: Stempel, Sterne, Belohnungen, Look wählen
     #/lerneinheit/<kind>-<einheit>[-<etappe>|-test] Kind: Etappen-Weg, Etappe (erklärt → selbst probieren), Test
   Karte: echte Weltkarte (lernen-welt.js), jedes Mathe-Gebiet liegt fest auf einem Erdteil, jeder Ort ist eine echte Stadt. */
'use strict';

const lernApi = () => API.replace('/app-api', '/lernen-api'); // API kommt aus app.js (wird danach geladen)
const LZ_STATUS = { offen: 'offen', nachgewiesen: 'geschafft', korrigiert: 'verbessert', gesichert: 'sicher', fehler: 'noch üben' };
const LZ_KLASSE = { offen: '', nachgewiesen: 'neu', korrigiert: 'neu', gesichert: 'neu', fehler: 'fehler' };
const LERN_ERDTEIL = { zahlen: 'EU', algebra: 'AS', geld: 'NA', geometrie: 'AF', raum: 'SA', daten: 'OC', funktionen: 'AN' };
const LERN_WELTEN = [['Ozean', 'Ozean'], ['Nacht', 'Nacht'], ['Dschungel', 'Dschungel'], ['Wüste', 'Wüste']];
const LERN_STILE = [['entdecker', 'Entdecker', 'verspielt, große Knöpfe'], ['studio', 'Studio', 'klar und sachlich']];

async function lernCall(aktion, daten = {}) {
  const headers = { 'Content-Type': 'application/json' };
  if (store.token) headers.Authorization = 'Bearer ' + store.token;
  const r = await fetch(mitRegion(lernApi() + '/aktion'), { method: 'POST', headers, body: JSON.stringify({ aktion, daten }) });
  let j; try { j = await r.json(); } catch { j = { ok: false, fehler: 'Keine Antwort (' + r.status + ')' }; }
  if (r.status === 401) { store.token = null; route('login'); throw new Error('Nicht angemeldet'); }
  if (!j.ok) throw new Error(j.fehler || 'Fehler bei ' + aktion);
  return j.ergebnis;
}
const lernCid = () => (crypto.randomUUID ? crypto.randomUUID() : Date.now() + '-' + Math.random().toString(16).slice(2));
const lernText = (t) => String(t ?? '').replace(/(\d) (?=\d{3}(?!\d))/g, '$1 '); // Zahlen wie 20 000 nicht umbrechen
const lernZahl = (n) => Number(n).toLocaleString('de-DE').replace(/\./g, ' ');
const lernIcon = (d, size = 24) => {
  const s = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  s.setAttribute('viewBox', '0 0 24 24'); s.setAttribute('width', size); s.setAttribute('height', size); s.setAttribute('aria-hidden', 'true');
  s.setAttribute('fill', 'none'); s.setAttribute('stroke', 'currentColor'); s.setAttribute('stroke-width', '2.2'); s.setAttribute('stroke-linecap', 'round'); s.setAttribute('stroke-linejoin', 'round');
  for (const p of d.split('|')) { const e = document.createElementNS('http://www.w3.org/2000/svg', 'path'); e.setAttribute('d', p); s.append(e); }
  return s;
};
const LI = {
  heute: 'M3 11l9-7 9 7v9H5z', karte: 'M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2z|M9 4v14|M15 6v14', pass: 'M6 3h12a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z|M9 11a3 3 0 1 0 6 0a3 3 0 1 0-6 0|M9 17h6',
  stern: 'M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6L12 16.4 6.7 19.4l1.2-6L3.4 9.3l6-.7z', stempel: 'M12 3a9 9 0 1 0 0 18a9 9 0 1 0 0-18z|M12 8a4 4 0 1 0 0 8a4 4 0 1 0 0-8z',
  tag: 'M4 6h16v14H4z|M4 10h16|M8 3v4|M16 3v4', pfeil: 'M9 6l6 6-6 6', ort: 'M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z|M12 8a2 2 0 1 0 0 4a2 2 0 1 0 0-4z',
  zurueck: 'M3 12a9 9 0 1 0 3-6.7|M3 4v5h5', haken: 'M5 12l5 5 9-10',
  weg: 'M5 19c4 0 3-6 7-6s3-6 7-6|M3 19a2 2 0 1 0 4 0a2 2 0 1 0-4 0|M17 7a2 2 0 1 0 4 0a2 2 0 1 0-4 0', heft: 'M6 3h11a1 1 0 0 1 1 1v16H7a2 2 0 0 1-2-2V4a1 1 0 0 1 1-1z|M9 8h6|M9 12h6',
};

// ---------- Daten je Kind ----------
// Ordnet die Orte eines Kindes: Jetzt dran · Kann schon · Später (nach Route und Klassenstufe); mit Stand je Einheit.
function lernReiseDaten(u, kindId) {
  const kind = (u.lernende || []).find((k) => k.id === kindId);
  if (!kind) return null;
  const stand = new Map((kind.stand || []).map((s) => [s.einheit_id, s]));
  const route = new Map((kind.route || []).filter((r) => r.status !== 'entfernt').sort((a, b) => (a.art === 'rueckreise') - (b.art === 'rueckreise')).map((r) => [r.block_id, r]));
  const einheiten = (u.einheiten || []).filter((e) => e.status !== 'entwurf' || kind.ist_test);
  // Themenplan (Eltern/Lehrer): Gibt es ihn, kommen nur Orte aus dem Plan dran – in seiner Reihenfolge.
  const mitPlan = (kind.route || []).some((r) => r.art === 'normal' && r.status !== 'entfernt');
  const gruppe = (e) => {
    const r = route.get(e.block_id);
    if (kind.ist_test || !kind.route?.length) return 'jetzt';
    if (mitPlan && !r) return 'spaeter';
    if (r?.kann_schon || r?.status === 'fertig') return 'kann'; // geschaffte Orte wandern zu „zum Wiederholen“
    if (mitPlan) return 'jetzt'; // im Plan: Eltern/Lehrer haben es bewusst eingeplant
    if (e.ziel_klasse && kind.klasse && e.ziel_klasse > kind.klasse) return 'spaeter';
    return 'jetzt';
  };
  const pos = (e) => route.get(e.block_id)?.position ?? 1e9;
  const mit = einheiten.map((e) => {
    const s = stand.get(e.id) || {};
    const n = e.pflicht_anzahl || 0, f = Number(s.fertig || 0);
    return { ...e, gruppe: gruppe(e), fertig: f, n, geschafft: n > 0 && f >= n, fehler: Number(s.fehler || 0), laeuft: !!s.laeuft, blocktest: !!s.blocktest, ortFertig: route.get(e.block_id)?.status === 'fertig' };
  }).sort((a, b) => pos(a) - pos(b) || a.id - b.id);
  const ortZustand = (o) => {
    const r = route.get(o.block_id);
    if (r?.status === 'fertig') return 'fertig';
    if (r?.kann_schon) return 'kann';
    if (mit.some((e) => e.block_id === o.block_id && e.gruppe === 'jetzt')) return 'jetzt';
    return 'offen';
  };
  const orte = (u.orte || []).map((o) => ({ ...o, zustand: ortZustand(o) }));
  const jetzt = mit.filter((e) => e.gruppe === 'jetzt');
  const naechste = jetzt.find((e) => !e.geschafft) || jetzt[0] || null;
  return { kind, mit, orte, jetzt, naechste, kann: mit.filter((e) => e.gruppe === 'kann'), spaeter: mit.filter((e) => e.gruppe === 'spaeter') };
}

function lernThema(kind) {
  const welt = String(kind?.welt || 'Ozean').toLowerCase().replace('ü', 'ue');
  const stil = kind?.stil === 'studio' ? 'studio' : 'entdecker';
  return `lr lr-${['ozean', 'nacht', 'dschungel', 'wueste'].includes(welt) ? welt : 'ozean'} lr-${stil}`;
}

// ---------- Karte ----------
function lernProjektion(lon, lat) {
  const W = window.LERN_WELT; const l = lon * Math.PI / 180, f = lat * Math.PI / 180, f2 = f * f, f4 = f2 * f2;
  const x = l * (0.8707 - 0.131979 * f2 + f4 * (-0.013791 + f4 * (0.003971 * f2 - 0.001529 * f4)));
  const y = f * (1.007226 + f2 * (0.015085 + f4 * (-0.044475 + 0.028874 * f2 - 0.005916 * f4)));
  return [W.tx + W.k * x, W.ty - W.k * y];
}
// Karte als SVG: ganze Welt oder Ausschnitt um die gegebenen Orte. hervor = Erdteil-Kürzel, das farbig bleibt.
function lernKarte({ orte = [], fokus = null, hervor = null, route = false, beschriftung = [], label = 'Weltkarte', breite = 360, hoehe = 187 } = {}) {
  const W = window.LERN_WELT; const ns = 'http://www.w3.org/2000/svg';
  const svg = document.createElementNS(ns, 'svg');
  let vb = [0, 0, W.w, W.h];
  if (fokus && fokus.length) {
    const p = fokus.map((o) => lernProjektion(Number(o.lon), Number(o.lat)));
    let x0 = Math.min(...p.map((q) => q[0])), x1 = Math.max(...p.map((q) => q[0])), y0 = Math.min(...p.map((q) => q[1])), y1 = Math.max(...p.map((q) => q[1]));
    const asp = breite / hoehe; let w = Math.max((x1 - x0) * 1.6, 170), h = Math.max((y1 - y0) * 1.7, 70);
    if (w / h > asp) h = w / asp; else w = h * asp;
    vb = [(x0 + x1) / 2 - w / 2, (y0 + y1) / 2 - h / 2, w, h];
  }
  const z = vb[2] / breite; // Kartenmaß je Bildschirmpixel: Punkte, Linien und Schrift bleiben unabhängig vom Ausschnitt gleich groß
  svg.setAttribute('viewBox', vb.map((v) => v.toFixed(1)).join(' ')); svg.setAttribute('preserveAspectRatio', 'xMidYMid slice');
  svg.setAttribute('class', 'lr-karte'); svg.setAttribute('role', 'img'); svg.setAttribute('aria-label', label);
  const mk = (tag, a) => { const e = document.createElementNS(ns, tag); for (const [k, v] of Object.entries(a)) e.setAttribute(k, v); return e; };
  svg.append(mk('rect', { x: vb[0] - 10, y: vb[1] - 10, width: vb[2] + 20, height: vb[3] + 20, class: 'lr-meer' }));
  for (const k of ['AN', 'SA', 'NA', 'AF', 'EU', 'AS', 'OC']) {
    svg.append(mk('path', { d: W.pfade[k], class: 'lr-land lr-land-' + k + (hervor && hervor !== k ? ' lr-land-blass' : ''), 'stroke-width': (1.2 * z).toFixed(2) }));
  }
  const pts = orte.filter((o) => o.lat != null).map((o) => ({ o, p: lernProjektion(Number(o.lon), Number(o.lat)) }));
  if (route && pts.length > 1) {
    svg.append(mk('path', { d: 'M' + pts.map((q) => q.p.map((v) => v.toFixed(1)).join(' ')).join(' L'), class: 'lr-route', 'stroke-width': (2.4 * z).toFixed(2), 'stroke-dasharray': `${(2 * z).toFixed(2)} ${(6 * z).toFixed(2)}` }));
  }
  for (const { o, p } of pts) {
    const r = (o.zustand === 'jetzt' ? 7 : 4.6) * z;
    svg.append(mk('circle', { cx: p[0].toFixed(1), cy: p[1].toFixed(1), r: r.toFixed(2), class: 'lr-punkt lr-punkt-' + (o.zustand || 'offen'), 'stroke-width': (1.6 * z).toFixed(2) }));
  }
  for (const b of beschriftung) {
    const p = lernProjektion(Number(b.lon), Number(b.lat));
    const t = mk('text', { x: (p[0] + (b.dx ?? 9) * z).toFixed(1), y: (p[1] + (b.dy ?? 4) * z).toFixed(1), class: 'lr-ortname' + (b.jetzt ? ' lr-ortname-jetzt' : ''), 'font-size': ((b.gross ? 15 : 12) * z).toFixed(1) });
    t.textContent = b.text; svg.append(t);
  }
  return svg;
}

// ---------- Rahmen der Kinderansicht ----------
function lernRahmen(kind, aktiv, ...inhalt) {
  const nav = el('nav', { class: 'lr-nav', 'aria-label': 'Lernreise' },
    ...[['reise', 'Heute', LI.heute], ['weg', 'Mein Weg', LI.weg], ['merkheft', 'Merkheft', LI.heft], ['weltkarte', 'Karte', LI.karte]].map(([v, t, i]) =>
      el('a', { href: `#/${v}/${kind.id}`, class: v === aktiv ? 'on' : '', ...(v === aktiv ? { 'aria-current': 'page' } : {}) }, lernIcon(i, 24), el('span', {}, t))));
  return el('div', { class: lernThema(kind) }, el('div', { class: 'lr-inhalt' }, ...inhalt), nav);
}
function lernKopf(gruss, titel) {
  return el('header', { class: 'lr-kopf' }, el('p', { class: 'lr-gruss' }, gruss), el('h1', { class: 'lr-titel' }, titel));
}
function lernStats(konto) {
  const s = (icon, wert, text) => el('div', { class: 'lr-stat' }, lernIcon(icon, 22), el('div', {}, el('b', {}, String(wert)), el('span', {}, text)));
  // Antippen erklärt, was die Zahlen bedeuten.
  return el('details', { class: 'lr-stats-box' },
    el('summary', { 'aria-label': 'Stempel, Sterne und Lerntage – antippen für Erklärung' },
      el('div', { class: 'lr-stats' }, s(LI.stempel, konto?.stempel ?? 0, 'Stempel'), s(LI.stern, lernZahl(konto?.sterne ?? 0), 'Sterne'), s(LI.tag, konto?.lerntage ?? 0, 'Lerntage'))),
    el('div', { class: 'lr-stats-erkl' },
      el('p', {}, el('b', {}, 'Sterne: '), '10 für jede Übungsaufgabe, die du zum ersten Mal richtig löst, 20 für jede richtige Testaufgabe. Sterne kannst du später gegen Belohnungen eintauschen.'),
      el('p', {}, el('b', {}, 'Stempel: '), 'Jeder Ort hat mehrere Themen. Hast du alle Themen eines Ortes geschafft, bekommst du seinen Stempel in den Reisepass.'),
      el('p', {}, el('b', {}, 'Lerntage: '), 'Tage, an denen du geübt hast.')));
}
async function lernLadeKind(arg) {
  const kindId = Number(arg);
  if (!kindId) { route('lernen'); return null; }
  const [u, k] = await Promise.all([lernCall('schule_uebersicht'), lernCall('schule_konto', { lernender_id: kindId }).catch(() => null)]);
  const d = lernReiseDaten(u, kindId);
  if (!d) { route('lernen'); return null; }
  if (k?.look) Object.assign(d.kind, k.look);
  d.konto = k?.konto || null; d.belohnungen = k?.belohnungen || []; d.einloesungen = k?.einloesungen || [];
  return d;
}

// ---------- Eltern: Übersicht ----------
async function viewLernen() {
  setChrome('Lernen Schule', { tab: 'lernen' });
  const live = viewGuard();
  loading();
  const [u, eltern, rm] = await Promise.all([lernCall('schule_uebersicht'), lernCall('schule_eltern').catch(() => null),
    lernCall('schule_rueckmeldungen').catch(() => null)]);
  if (!live()) return;
  const seite = typeof LERN_SEITE !== 'undefined';
  const konten = new Map((eltern?.kinder || []).map((k) => [k.id, k.konto]));
  const url = new URL('mathe/', location.href).href;
  const status = el('span', { class: 'muted small', role: 'status' });
  const kopie = el('button', { type: 'button', class: 'secondary' }, 'Link kopieren');
  kopie.addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(url); status.textContent = 'Link kopiert.'; }
    catch { status.textContent = 'Kopieren nicht möglich. Link bitte markieren und kopieren.'; }
  });
  const kinder = (u.lernende || []).map((k) => {
    const d = lernReiseDaten(u, k.id); const n = d?.naechste; const ko = konten.get(k.id);
    return el('a', { class: 'card lern-kindkarte', href: `#/reise/${k.id}` },
      el('div', { class: 'lern-einheit-kopf' }, el('b', {}, k.name), k.ist_test ? el('span', { class: 'pill wartet' }, 'zum Ausprobieren') : null),
      el('p', { class: 'small muted' }, n ? `Jetzt: ${n.stadt || n.ort_titel} · ${n.titel} (${n.fertig}/${n.n})` : 'Gerade nichts offen'),
      ko ? el('p', { class: 'small muted' }, `${ko.stempel} Stempel · ${lernZahl(ko.sterne)} Sterne · ${ko.lerntage} Lerntage`) : null,
      el('span', { class: 'lern-kindkarte-los' }, 'Lernreise öffnen ›'));
  });
  const offen = (rm?.rueckmeldungen || []).filter((r) => ['offen', 'in_arbeit'].includes(r.status)).length;
  const planKarten = u.leitung ? (u.lernende || []).filter((k) => !k.ist_test).map((k) => el('a', { class: 'card lern-kindkarte', href: `#/plan/${k.id}` },
    el('b', {}, `Themenplan ${k.name}`),
    el('p', { class: 'small muted' }, (k.route || []).some((r) => r.art === 'normal' && r.status !== 'entfernt')
      ? `${(k.route || []).filter((r) => r.art === 'normal' && r.status !== 'entfernt').length} Orte im Plan` : 'Noch kein Plan – alle Themen sichtbar'),
    el('span', { class: 'lern-kindkarte-los' }, 'Plan bearbeiten ›'))) : [];
  const steuern = u.leitung ? [
    el('section', { class: 'start-intro lern-neu' }, el('p', { class: 'eyebrow' }, 'ELTERN UND LEHRER'), el('h2', {}, 'Themen und Rückmeldungen')),
    el('div', { class: 'lern-kinderliste' },
      el('a', { class: 'card lern-kindkarte lp-hauptkarte', href: '#/lehrplan' }, el('b', {}, 'Lehrplan-Übersicht'),
        el('p', { class: 'small muted' }, 'Alle Themen je Schulart und Klasse: was fertig ist, was in Prüfung ist, was noch fehlt – mit Inhalten zum Ansehen.'),
        el('span', { class: 'lern-kindkarte-los' }, 'Öffnen ›')),
      ...planKarten,
      el('a', { class: 'card lern-kindkarte', href: '#/rueckmeldungen' }, el('b', {}, 'Rückmeldungen an die Entwicklung'),
        el('p', { class: 'small muted' }, offen ? `${offen} offen` : 'Thema fehlt, zu ungenau, mehr Aufgaben … hier eintragen'), el('span', { class: 'lern-kindkarte-los' }, 'Öffnen ›')),
      eltern ? el('a', { class: 'card lern-kindkarte', href: '#/zugaenge' }, el('b', {}, 'Zugänge'),
        el('p', { class: 'small muted' }, 'Codes für Lehrer, Eltern und Kinder – nur für den Bereich Lernen'), el('span', { class: 'lern-kindkarte-los' }, 'Verwalten ›')) : null,
      !seite ? el('a', { class: 'card lern-kindkarte', href: 'lernen/', target: '_blank', rel: 'noopener' }, el('b', {}, 'Eigene Lernen-Seite'),
        el('p', { class: 'small muted' }, 'Für Lehrer und Kinder: Anmeldung mit Lern-Code, ohne Zugriff auf den Rest der App.'), el('span', { class: 'lern-kindkarte-los' }, 'Öffnen ↗')) : null)] : [];
  main.replaceChildren(...[
    seite ? null : el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'LERNEN SCHULE'), el('h2', {}, 'Mathe Klasse 7/8'),
      el('p', {}, 'Erklärungen, Aufgaben in drei Stufen und typische Fehler zu Zahlen, Termen, Potenzen, Brüchen, Gleichungen und Gleichungssystemen.')),
    seite ? null : el('div', { class: 'card learn-resource' },
      el('p', {}, 'Die Seite öffnet ohne Anmeldung. Du kannst den Link an Leo und die Lehrkraft schicken.'),
      el('div', { class: 'row' }, el('a', { class: 'btn primary', href: 'mathe/', target: '_blank', rel: 'noopener' }, 'Mathe öffnen ↗'), kopie, status),
      el('p', { class: 'muted small learn-url' }, url)),
    el('section', { class: 'start-intro lern-neu' }, el('p', { class: 'eyebrow' }, 'LERNREISE'), el('h2', {}, 'Wer lernt heute?')),
    el('div', { class: 'lern-kinderliste' }, ...(kinder.length ? kinder : [el('p', { class: 'card muted' }, 'Kein Kind freigeschaltet.')])),
    ...steuern,
    eltern ? lernElternBereich(eltern) : null].filter(Boolean));
}

function lernElternBereich(e) {
  const box = el('section', { class: 'lern-eltern' });
  const offen = (e.einloesungen || []).filter((x) => x.status === 'beantragt');
  const meldung = el('p', { class: 'small muted', role: 'status' });
  const entscheide = async (id, status) => {
    try { await lernCall('schule_einloesung_entscheiden', { id, status }); render(); } catch (err) { meldung.textContent = err.message; }
  };
  box.append(el('h2', {}, 'Belohnungen'),
    el('p', { class: 'small muted' }, 'Die Kinder sammeln Sterne (Üben, Tests) und Stempel (geschaffte Orte) und lösen sie hier ein. Du bestätigst. Abgelehnt gibt die Sterne zurück.'));
  if (offen.length) box.append(el('div', { class: 'card' }, el('h3', {}, `Offene Wünsche (${offen.length})`),
    ...offen.map((x) => el('div', { class: 'lern-wunsch' }, el('span', {}, el('b', {}, x.kind), ` möchte „${x.titel}“ (${lernZahl(x.sterne)} Sterne)`),
      el('div', { class: 'row' }, el('button', { type: 'button', class: 'primary', onclick: () => entscheide(x.id, 'bestaetigt') }, 'Bestätigen'),
        el('button', { type: 'button', class: 'secondary', onclick: () => entscheide(x.id, 'abgelehnt') }, 'Ablehnen'))))));
  const liste = (e.belohnungen || []);
  box.append(el('div', { class: 'card' }, el('h3', {}, 'Katalog'),
    liste.length ? el('ul', { class: 'lern-katalog' }, ...liste.map((b) => el('li', { class: b.aktiv ? '' : 'muted' },
      el('span', {}, el('b', {}, b.titel), ` · ${b.kosten_sterne ? lernZahl(b.kosten_sterne) + ' Sterne' : ''}${b.kosten_sterne && b.kosten_stempel ? ' + ' : ''}${b.kosten_stempel ? b.kosten_stempel + ' Stempel' : ''}${b.kosten_sterne || b.kosten_stempel ? '' : 'gratis'}`),
      el('button', { type: 'button', class: 'secondary', onclick: async () => { try { await lernCall('schule_belohnung_setzen', { id: b.id, aktiv: !b.aktiv }); render(); } catch (err) { meldung.textContent = err.message; } } }, b.aktiv ? 'Ausblenden' : 'Wieder anbieten'))))
      : el('p', { class: 'small muted' }, 'Noch keine Belohnungen angelegt.'),
    lernBelohnungFormular(meldung), meldung));
  return box;
}

function lernBelohnungFormular(meldung) {
  const titel = el('input', { type: 'text', id: 'bl-titel', placeholder: 'z. B. Eis, Kinoabend, Ausflug', autocomplete: 'off' });
  const sterne = el('input', { type: 'number', id: 'bl-sterne', min: '0', step: '10', value: '300', inputmode: 'numeric' });
  const stempel = el('input', { type: 'number', id: 'bl-stempel', min: '0', step: '1', value: '0', inputmode: 'numeric' });
  const f = el('form', { class: 'lern-bl-form' },
    el('label', { for: 'bl-titel' }, 'Belohnung'), titel,
    el('div', { class: 'row' }, el('label', { for: 'bl-sterne' }, 'Sterne', sterne), el('label', { for: 'bl-stempel' }, 'Stempel', stempel)),
    el('button', { type: 'submit', class: 'primary' }, 'Hinzufügen'));
  f.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    if (!titel.value.trim()) { meldung.textContent = 'Bitte einen Namen eingeben.'; return; }
    try { await lernCall('schule_belohnung_setzen', { titel: titel.value.trim(), kosten_sterne: Number(sterne.value) || 0, kosten_stempel: Number(stempel.value) || 0 }); render(); }
    catch (err) { meldung.textContent = err.message; }
  });
  return f;
}

// ---------- Kind: Heute dran ----------
async function viewReise(arg) {
  setChrome('Lernreise', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const [merk, wdh] = await Promise.all([lernMerkDaten(d).catch(() => []), lernCall('schule_wiederholung', { lernender_id: d.kind.id, anzahl: 3 }).catch(() => null)]);
  if (!live()) return;
  const { kind, naechste: n } = d;
  $('#title').textContent = 'Lernreise ' + kind.name;
  const ortStand = (blockId) => (d.konto?.orte || []).find((o) => o.block_id === blockId);
  const et = n ? lernEtappenZahl(merk.find((m) => m.einheit_id === n.id)) : { n: 0, f: 0 };
  const teile = [lernKopf(`Hallo ${kind.name}!`, kind.stil === 'studio' ? 'Heute dran' : 'Wohin reist du heute?'), lernStats(d.konto)];
  if (wdh?.aufgaben?.length) teile.push(el('a', { class: 'lr-zeile lr-wdh', href: `#/wiederholen/${kind.id}` },
    el('span', { class: 'lr-zeile-icon' }, lernIcon(LI.weg, 22)),
    el('span', { class: 'lr-zeile-text' }, el('b', {}, `Zuerst: ${wdh.aufgaben.length} ${wdh.aufgaben.length === 1 ? 'Aufgabe' : 'Aufgaben'} zum Wiederholen`),
      el('small', {}, 'Damit nichts vergessen wird – dauert nur kurz.')), lernIcon(LI.pfeil, 20)));
  if (n) {
    const kont = d.orte.filter((o) => o.kontinent === (d.orte.find((x) => x.block_id === n.block_id)?.kontinent));
    const ortN = d.orte.find((o) => o.block_id === n.block_id) || {};
    teile.push(el('section', { class: 'lr-karte-box lr-haupt' },
      el('p', { class: 'lr-ueber' }, `JETZT DRAN · ${(n.erdteil || '').toUpperCase()} · ${(n.kontinent || '').toUpperCase()}`),
      el('div', { class: 'lr-kartenbild' }, lernKarte({ orte: kont, fokus: kont.slice(0, Math.max(3, kont.indexOf(ortN) + 2)), hervor: LERN_ERDTEIL[ortN.kontinent], route: true,
        beschriftung: [{ ...ortN, text: `Du bist in ${n.stadt}`, jetzt: true, gross: true }], label: `Karte: ${n.stadt}, ${n.land}`, breite: 340, hoehe: 130 })),
      el('h2', {}, `${n.stadt}: ${n.titel}`),
      et.n ? el('div', { class: 'lr-fortschritt' }, el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${et.f} von ${et.n} Etappen` }, el('span', { style: `width:${Math.round(100 * et.f / et.n)}%` })), el('b', {}, `${et.f} von ${et.n} Etappen`)) : null,
      el('a', { class: 'lr-knopf', href: `#/lerneinheit/${kind.id}-${n.id}` }, n.laeuft ? 'Test weitermachen' : et.f ? 'Weiter geht’s' : 'Losreisen'),
      (() => { const o = ortStand(n.block_id); return o && o.themen > 1 ? el('p', { class: 'lr-leise lr-ortstand' },
        `${n.stadt} hat ${o.themen} Themen, ${o.erledigt} davon geschafft. Den Stempel gibt es, wenn alle geschafft sind.`) : null; })()));
  } else teile.push(el('section', { class: 'lr-karte-box' }, el('h2', {}, 'Gerade ist nichts offen'), el('p', { class: 'lr-leise' }, 'Neue Orte kommen bald. Schau in deinen Reisepass.')));
  const jg = d.konto?.jahrgang;
  if (jg?.themen) teile.push(el('section', { class: 'lr-karte-box lr-jgstand' },
    el('p', { class: 'lr-ueber' }, `MEIN STAND · ${(LERN_SCHULART[jg.schulart] || '').toUpperCase()} KLASSE ${jg.klasse}`),
    el('div', { class: 'lr-fortschritt' }, el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${jg.geschafft} von ${jg.themen} Themen geschafft` }, el('span', { style: `width:${Math.round(100 * jg.geschafft / jg.themen)}%` })),
      el('b', {}, `${jg.geschafft} von ${jg.themen} Themen`)),
    el('p', { class: 'lr-leise' }, `${jg.mit_inhalt} davon kannst du schon lernen, die anderen kommen nach und nach dazu.`)));
  const weitere = d.jetzt.filter((e) => e !== n);
  if (weitere.length) teile.push(el('h2', { class: 'lr-zwischen' }, 'Auch offen'), ...weitere.map((e) => lernOrtZeile(kind, e)));
  if (d.kann.length) teile.push(el('details', { class: 'lr-mehr' }, el('summary', {}, `Geschafft oder kann schon – zum Wiederholen (${d.kann.length})`), ...d.kann.map((e) => lernOrtZeile(kind, e))));
  if (d.spaeter.length) teile.push(el('details', { class: 'lr-mehr' }, el('summary', {}, `Später – für höhere Klassen (${d.spaeter.length})`), ...d.spaeter.map((e) => lernOrtZeile(kind, e))));
  main.replaceChildren(lernRahmen(kind, 'reise', ...teile));
}

function lernOrtZeile(kind, e) {
  const zustand = e.laeuft ? 'Test läuft' : e.geschafft ? 'geschafft' : e.fehler ? 'noch üben' : e.n ? `${e.fertig}/${e.n}` : '';
  return el('a', { class: 'lr-zeile', href: `#/lerneinheit/${kind.id}-${e.id}` },
    el('span', { class: 'lr-zeile-icon' }, lernIcon(e.geschafft ? LI.haken : LI.ort, 22)),
    el('span', { class: 'lr-zeile-text' }, el('b', {}, `${e.stadt || e.ort_titel}: ${e.titel}`), el('small', {}, `${e.erdteil || ''} · ${e.kontinent || ''}${e.status === 'entwurf' ? ' · Entwurf' : ''}`)),
    zustand ? el('span', { class: 'lr-zeile-zustand' }, zustand) : null, lernIcon(LI.pfeil, 20));
}

// ---------- Kind: Weltkarte ----------
async function viewWeltkarte(arg) {
  setChrome('Weltkarte', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const { kind } = d;
  const konts = [...new Map(d.orte.map((o) => [o.kontinent, o])).values()];
  const zaehl = (k) => { const os = d.orte.filter((o) => o.kontinent === k); return [os.filter((o) => o.zustand === 'fertig' || o.zustand === 'kann').length, os.length]; };
  let wahl = d.orte.find((o) => o.zustand === 'jetzt')?.kontinent || konts[0]?.kontinent;
  const detail = el('section', { class: 'lr-karte-box' });
  const zeigeKontinent = () => {
    const os = d.orte.filter((o) => o.kontinent === wahl); const k0 = os[0] || {};
    detail.replaceChildren(
      el('p', { class: 'lr-ueber' }, `${(k0.erdteil || '').toUpperCase()} · ${(k0.kontinent_titel || '').toUpperCase()}`),
      os.length && k0.erdteil !== 'Antarktis' ? el('div', { class: 'lr-kartenbild' }, lernKarte({ orte: os, fokus: os, hervor: LERN_ERDTEIL[wahl], route: true,
        beschriftung: os.filter((o) => o.zustand === 'jetzt').map((o) => ({ ...o, text: o.stadt, jetzt: true })), label: `Karte ${k0.erdteil}`, breite: 340, hoehe: 150 })) : null,
      el('ol', { class: 'lr-ortliste' }, ...os.map((o, i) => el('li', { class: 'lr-ort-' + o.zustand },
        el('span', { class: 'lr-nr' }, o.zustand === 'fertig' || o.zustand === 'kann' ? lernIcon(LI.haken, 16) : String(i + 1)),
        el('span', { class: 'lr-zeile-text' }, el('b', {}, `${o.stadt}: ${o.titel}`), el('small', {}, `${o.land}${o.ziel_klasse ? ' · Kl. ' + o.ziel_klasse : ''}`)),
        el('span', { class: 'lr-zeile-zustand' }, { fertig: 'Stempel', kann: 'kann schon', jetzt: 'jetzt', offen: o.hat_einheit ? '' : 'bald' }[o.zustand])))));
  };
  const knoepfe = el('div', { class: 'lr-chips', role: 'tablist', 'aria-label': 'Kontinente' });
  const zeichneKnoepfe = () => knoepfe.replaceChildren(...konts.map((o) => {
    const [f, n] = zaehl(o.kontinent);
    return el('button', { type: 'button', role: 'tab', class: o.kontinent === wahl ? 'on' : '', 'aria-selected': String(o.kontinent === wahl),
      onclick: () => { wahl = o.kontinent; zeichneKnoepfe(); zeigeKontinent(); } }, `${o.kontinent_titel} `, el('small', {}, `${f}/${n}`));
  }));
  zeichneKnoepfe(); zeigeKontinent();
  const fertig = d.orte.filter((o) => o.zustand === 'fertig' || o.zustand === 'kann').length;
  main.replaceChildren(lernRahmen(kind, 'weltkarte',
    lernKopf('DEINE MATHE-WELTREISE', `${fertig} von ${d.orte.length} Orten`),
    el('div', { class: 'lr-kartenbild lr-welt' }, lernKarte({ orte: d.orte, label: 'Weltkarte mit allen Orten' })),
    el('p', { class: 'lr-legende' }, el('span', { class: 'lr-dot lr-dot-fertig' }), 'geschafft', el('span', { class: 'lr-dot lr-dot-jetzt' }), 'jetzt dran', el('span', { class: 'lr-dot lr-dot-offen' }), 'noch offen'),
    knoepfe, detail));
}

// ---------- Kind: Reisepass ----------
async function viewReisepass(arg) {
  setChrome('Reisepass', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const { kind, konto } = d;
  const meldung = el('p', { class: 'lr-meldung', role: 'status', 'aria-live': 'polite' });
  const fertigeOrte = new Set((konto?.orte || []).filter((o) => o.abgeschlossen).map((o) => o.block_id));
  const stempel = d.orte.filter((o) => o.zustand === 'fertig' || fertigeOrte.has(o.block_id));
  const belohnungen = d.belohnungen.map((b) => {
    const fehltS = Math.max(0, b.kosten_sterne - (konto?.sterne || 0)), fehltP = Math.max(0, b.kosten_stempel - (konto?.stempel || 0));
    const kann = !fehltS && !fehltP;
    return el('div', { class: 'lr-belohnung' },
      el('div', {}, el('b', {}, b.titel), el('small', {}, [b.kosten_sterne ? `${lernZahl(b.kosten_sterne)} Sterne` : '', b.kosten_stempel ? `${b.kosten_stempel} Stempel` : ''].filter(Boolean).join(' + ') || 'gratis')),
      kann ? el('button', { type: 'button', class: 'lr-knopf lr-knopf-klein', onclick: async (ev) => {
        ev.target.disabled = true;
        try { await lernCall('schule_einloesen', { lernender_id: kind.id, belohnung_id: b.id }); meldung.textContent = `Wunsch „${b.titel}“ ist abgeschickt. Mama oder Papa bestätigen ihn.`; setTimeout(render, 1200); }
        catch (err) { meldung.textContent = err.message; ev.target.disabled = false; }
      } }, 'Einlösen') : el('small', { class: 'lr-fehlt' }, `noch ${[fehltS ? lernZahl(fehltS) + ' Sterne' : '', fehltP ? fehltP + ' Stempel' : ''].filter(Boolean).join(' + ')}`));
  });
  const look = el('div', { class: 'lr-look' });
  const setze = async (stil, welt) => {
    try { await lernCall('schule_look_setzen', { lernender_id: kind.id, stil, welt }); render(); } catch (err) { meldung.textContent = err.message; }
  };
  look.append(el('p', { class: 'lr-ueber' }, 'WELT'), el('div', { class: 'lr-chips' }, ...LERN_WELTEN.map(([w, t]) =>
    el('button', { type: 'button', class: (kind.welt === w ? 'on ' : '') + 'lr-welt-' + w.toLowerCase().replace('ü', 'ue'), 'aria-pressed': String(kind.welt === w), onclick: () => setze(kind.stil || 'entdecker', w) }, t))),
  el('p', { class: 'lr-ueber' }, 'STIL'), el('div', { class: 'lr-chips' }, ...LERN_STILE.map(([s, t, h]) =>
    el('button', { type: 'button', class: kind.stil === s ? 'on' : '', 'aria-pressed': String(kind.stil === s), onclick: () => setze(s, kind.welt || 'Ozean') }, t, el('small', {}, ' · ' + h)))));
  main.replaceChildren(lernRahmen(kind, 'weg',
    lernKopf('REISEPASS', kind.name), lernStats(konto),
    el('section', { class: 'lr-karte-box' }, el('h2', {}, 'Stempel'),
      stempel.length ? el('div', { class: 'lr-stempelraster' }, ...stempel.map((o, i) => el('div', { class: 'lr-stempel', style: `--dreh:${(i * 37) % 17 - 8}deg` }, el('b', {}, o.stadt), el('small', {}, o.kontinent_titel))))
        : el('p', { class: 'lr-leise' }, 'Noch kein Stempel. Den ersten gibt es, wenn du alle Themen eines Ortes geschafft hast.'),
      (konto?.orte || []).filter((o) => !o.abgeschlossen && o.erledigt).map((o) => { const ort = d.orte.find((x) => x.block_id === o.block_id);
        return ort ? el('p', { class: 'lr-leise' }, `${ort.stadt}: ${o.erledigt} von ${o.themen} Themen geschafft`) : null; })),
    el('section', { class: 'lr-karte-box' }, el('h2', {}, 'Belohnungen'),
      belohnungen.length ? el('div', { class: 'lr-belohnungen' }, ...belohnungen) : el('p', { class: 'lr-leise' }, 'Mama oder Papa legen hier bald Belohnungen an.'),
      d.einloesungen.length ? el('ul', { class: 'lr-wuensche' }, ...d.einloesungen.slice(0, 5).map((x) => el('li', {}, `${x.titel}: `, el('b', {}, { beantragt: 'wartet auf Bestätigung', bestaetigt: 'bestätigt', abgelehnt: 'abgelehnt' }[x.status] || x.status)))) : null,
      meldung),
    el('section', { class: 'lr-karte-box' }, el('h2', {}, 'Dein Look'), look)));
}

function lernStandZeile(stand) {
  if (!stand?.length) return null;
  return el('div', { class: 'lern-stand', 'aria-label': 'Lernziele' }, ...stand.filter((s) => s.pflicht).map((s) =>
    el('span', { class: 'pill ' + (LZ_KLASSE[s.status] || ''), title: s.lernziel }, lernZielName(s.lernziel) + ': ' + (LZ_STATUS[s.status] || s.status))));
}
let lernTitel = new Map(); // Lernziel → Etappentitel der zuletzt geöffneten Einheit
const lernZielName = (k) => lernTitel.get(k) || String(k).replace(/_/g, ' ').replace(/ae/g, 'ä').replace(/oe/g, 'ö').replace(/ue/g, 'ü').replace(/^./, (c) => c.toUpperCase());

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

// ---------- Terme lesen (W150) ----------
// Liest einen frei getippten Term und füllt damit die Vorlage der Aufgabe (z. B. „□x(□x + □)“) – die Datenbank prüft wie bisher die Zahlen.
const lernTermNorm = (t) => String(t ?? '').replace(/\s+/g, '').replace(/[−–]/g, '-').replace(/[·*⋅×]/g, '').replace(/\^2/g, '²').replace(/\^3/g, '³')
  .replace(/\+-|-\+/g, '-').replace(/--/g, '+').replace(/\.(?=\d)/g, ',');
function lernMonoKey(v) {
  const m = [...v.matchAll(/([a-z])([²³]?)/g)];
  if (m.map((x) => x[0]).join('') !== v) return null;
  const pot = {};
  for (const [, b, e] of m) pot[b] = (pot[b] || 0) + (e === '²' ? 2 : e === '³' ? 3 : 1);
  return Object.keys(pot).sort().map((b) => b + (pot[b] === 1 ? '' : pot[b] === 2 ? '²' : pot[b] === 3 ? '³' : '^' + pot[b])).join('');
}
function lernMono(t) {
  const m = t.match(/^([+-]?)(\d+(?:,\d+)?)?([a-z²³]*)$/);
  if (!m || (!m[2] && !m[3])) return null;
  const key = lernMonoKey(m[3]); if (key === null) return null;
  let c = m[2] ? Number(m[2].replace(',', '.')) : 1; if (m[1] === '-') c = -c;
  return { key, c };
}
function lernPoly(t) {
  const glieder = t.match(/[+-]?[^+-]+/g);
  if (!glieder || glieder.join('') !== t) return null;
  const map = new Map();
  for (const g of glieder) { const mo = lernMono(g); if (!mo) return null; if (map.has(mo.key)) return { doppelt: true }; map.set(mo.key, mo.c); }
  return map;
}
function lernVorlage(schablone) {
  const s = lernTermNorm(schablone); const k = s.indexOf('(');
  const keys = (x) => (x.match(/[+-]?[^+-]+/g) || []).map((g) => lernMonoKey(g.replace(/^[+-]?□/, '')));
  return k < 0 ? { prefix: null, inner: keys(s) } : { prefix: lernMonoKey(s.slice(0, k).replace('□', '')), inner: keys(s.slice(k + 1, s.lastIndexOf(')'))) };
}
const lernZahlText = (n) => (n < 0 ? '−' : '') + String(Math.abs(Math.round(n * 1e6) / 1e6)).replace('.', ',');
function lernTermWerte(schablone, eingabe) {
  const v = lernVorlage(schablone); const s = lernTermNorm(eingabe); let innen = s; let vor = [];
  if (v.prefix !== null) {
    const k = s.indexOf('(');
    if (k < 0 || !s.endsWith(')')) return { fehler: 'klammer' };
    const p = s.slice(0, k); innen = s.slice(k + 1, -1);
    const mo = p === '' || p === '+' ? { key: '', c: 1 } : p === '-' ? { key: '', c: -1 } : lernMono(p);
    if (!mo || mo.key !== v.prefix) return { fehler: 'form' };
    vor = [mo.c];
  } else if (/[()]/.test(s)) return { fehler: 'ohneklammer' };
  const map = lernPoly(innen);
  if (!map) return { fehler: 'lesen' };
  if (map.doppelt) return { fehler: 'doppelt' };
  for (const k of map.keys()) if (!v.inner.includes(k)) return { fehler: 'form' };
  return { werte: [...vor, ...v.inner.map((k) => (map.has(k) ? map.get(k) : 0))].map(lernZahlText) };
}
// Ist eine (falsche) Antwort zu einer Ausklammer-Vorlage trotzdem gleichwertig zur Lösung? Dann fehlt nur der größte Faktor.
function lernGleichwertigAusgeklammert(schablone, werte, loesung) {
  const v = lernVorlage(schablone);
  if (v.prefix === null || !Array.isArray(werte) || !Array.isArray(loesung)) return false;
  const zahl = (x) => Number(String(x).replace('−', '-').replace(',', '.'));
  const aus = (w) => { const m = new Map(); v.inner.forEach((k, i) => { const key = lernMonoKey(v.prefix + k); m.set(key, (m.get(key) || 0) + zahl(w[0]) * zahl(w[i + 1])); }); return m; };
  const a = aus(werte), b = aus(loesung);
  return [...new Set([...a.keys(), ...b.keys()])].every((k) => Math.abs((a.get(k) || 0) - (b.get(k) || 0)) < 1e-9);
}
// Term-Vorlage (Polynom wie „□x² + □x + □“ oder „□(□x + □)“): frei eintippen. Alles andere: je Lücke ein Feld.
const lernIstTermVorlage = (schablone) => { const t = String(schablone || ''); return /[a-z]/.test(t) && /^[\s□+\-−·()a-z²³]*$/.test(t); };
function lernTermFehler(f, schablone) {
  const form = String(schablone).replace(/□/g, '…');
  return { klammer: `Hier gehört eine Klammer in die Antwort, so: ${form}`, ohneklammer: 'Die Antwort soll ohne Klammer sein. Rechne die Klammer aus.',
    form: `So kann ich das nicht prüfen. Die Antwort soll so aussehen: ${form}`, doppelt: 'Fasse gleiche Glieder noch zusammen.',
    lesen: 'Das kann ich nicht lesen. Schreib zum Beispiel 3x² − 2x + 5.' }[f] || 'Bitte prüfe deine Eingabe.';
}
function lernVorlageFuellen(schablone, werte) {
  const st = String(schablone).split('□');
  return st.map((t, i) => t + (i < st.length - 1 ? String(werte[i] ?? '') : '')).join('').replace(/\+ ?[−-]/g, '− ');
}

// Liefert { node, antwort(), sperren() }; antwort() ist null, solange nichts eingegeben ist.
function lernAufgabe(a, vorher) {
  const f = a.frage || {};
  let wert = vorher ?? null; let fehler = null;
  const teile = [el('p', { class: 'lern-frage' }, lernText(f.text))];
  if (f.hinweis && a.antworttyp !== 'luecken') teile.push(el('p', { class: 'small muted' }, f.hinweis));
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
  } else if (a.antworttyp === 'luecken' && !lernIstTermVorlage(f.schablone)) {
    // W150: allgemeine Lücken (Bruch □/□, Zahlenpaar x = □; y = □, Punkt S(□ | □) …): je Lücke ein kleines Zahlenfeld.
    const st = String(f.schablone || '□').split('□'); const n = st.length - 1;
    const bruch = String(f.schablone).trim() === '□/□';
    const eingaben = Array.from({ length: n }, (_, i) => el('input', { type: 'text', inputmode: 'text', autocomplete: 'off', class: 'lern-luecke',
      'aria-label': bruch ? (i ? 'Nenner' : 'Zähler') : `Lücke ${i + 1}`, value: wert?.werte?.[i] ?? '' }));
    const lies = () => {
      const w = eingaben.map((x) => x.value.trim());
      wert = w.every((x) => x !== '') ? { werte: w } : null;
      fehler = wert ? null : (n > 1 ? 'Bitte fülle alle Felder aus.' : 'Bitte erst antworten.');
    };
    eingaben.forEach((x) => { x.addEventListener('input', lies); felder.push(x); });
    if (f.hinweis) teile.push(el('p', { class: 'small muted' }, f.hinweis));
    teile.push(bruch
      ? el('div', { class: 'lern-bruch', role: 'group', 'aria-label': 'Bruch' }, eingaben[0], el('span', { class: 'lern-bruchstrich', 'aria-hidden': 'true' }), eingaben[1])
      : el('div', { class: 'lern-lueckenzeile' }, ...st.flatMap((t, i) => [t ? el('span', {}, t) : null, i < n ? eingaben[i] : null]).filter(Boolean)));
    lies(); fehler = null;
  } else if (a.antworttyp === 'luecken') {
    // W150: Term frei eintippen (wie im Heft); die App liest daraus die Zahlen für die Vorlage.
    const vorlage = String(f.schablone || '□');
    const inp = el('input', { type: 'text', inputmode: 'text', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', 'aria-label': 'Dein Term', class: 'lern-term',
      placeholder: 'Term eintippen', value: wert?.werte ? lernVorlageFuellen(vorlage, wert.werte) : '' });
    const lies = () => {
      const r = inp.value.trim() ? lernTermWerte(vorlage, inp.value) : null;
      wert = r?.werte ? { werte: r.werte } : null; fehler = r?.fehler ? lernTermFehler(r.fehler, vorlage) : null;
    };
    inp.addEventListener('input', lies);
    felder.push(inp);
    const tippe = (t) => {
      const a0 = inp.selectionStart ?? inp.value.length, b0 = inp.selectionEnd ?? a0;
      inp.value = inp.value.slice(0, a0) + t + inp.value.slice(b0); inp.focus(); inp.setSelectionRange(a0 + t.length, a0 + t.length); lies();
    };
    const buchst = [...new Set((vorlage.match(/[a-z]/g) || []))];
    const tasten = [...buchst, '²', ...(vorlage.includes('(') ? ['(', ')'] : []), '+', '−'];
    teile.push(inp, el('div', { class: 'lern-tasten' }, ...tasten.map((t) => el('button', { type: 'button', class: 'lern-taste', 'aria-label': t === '²' ? 'hoch 2' : t === '−' ? 'minus' : t === '+' ? 'plus' : t === '(' ? 'Klammer auf' : t === ')' ? 'Klammer zu' : t,
      onmousedown: (ev) => ev.preventDefault(), onclick: () => tippe(t) }, t)), el('button', { type: 'button', class: 'lern-taste', 'aria-label': 'löschen',
      onmousedown: (ev) => ev.preventDefault(), onclick: () => { const a0 = inp.selectionStart ?? inp.value.length; if (a0 > 0) { inp.value = inp.value.slice(0, a0 - 1) + inp.value.slice(a0); inp.setSelectionRange(a0 - 1, a0 - 1); lies(); } } }, '⌫')));
    if (wert?.werte) lies();
  }
  return { node: el('div', { class: 'lern-aufgabe' }, ...teile), antwort: () => wert, fehlerText: () => fehler,
    sperren: (an = true) => felder.forEach((x) => { x.disabled = an; }) };
}

// Markierung als Zahl: der i-te Strich nach dem Anfang
function lernStrichText(g, i) {
  if (!g || i === undefined || i === null) return `Strich ${i}`;
  const v = Number(g.start) + i * (Number(g.ende) - Number(g.start)) / (Number(g.abschnitte) || 1);
  return i === 0 ? `${lernZahl(v)} (der Anfang)` : `${lernZahl(v)} (der ${i}. Strich nach dem Anfang)`;
}
function lernLoesungText(a) {
  const l = a.loesung || {};
  if (a.antworttyp === 'auswahl') return (a.antworten || [])[l.index] ?? '';
  if (a.antworttyp === 'markierung') return lernStrichText(a.frage?.grafik, l.index);
  if (a.antworttyp === 'luecken') { const s = String(a.frage?.schablone || '').split('□'); return s.map((t, i) => t + (i < s.length - 1 ? String(l.werte?.[i] ?? '').replace('-', '−') : '')).join(''); }
  if (a.antworttyp === 'text') return l.text ?? '';
  return l.wert !== undefined ? lernZahl(l.wert) + (l.einheit ? ' ' + l.einheit : '') : '';
}
function lernAntwortText(a, w) {
  if (!w) return '(keine Antwort)';
  if (a.antworttyp === 'auswahl') return (a.antworten || [])[w.index] ?? '';
  if (a.antworttyp === 'markierung') return lernStrichText(a.frage?.grafik, w.index);
  if (a.antworttyp === 'luecken') { const s = String(a.frage?.schablone || '').split('□'); return s.map((t, i) => t + (i < s.length - 1 ? (w.werte?.[i] ?? '') : '')).join(''); }
  return w.wert ?? '';
}

// ---------- Kind: Lerneinheit in Etappen ----------
// #/lerneinheit/<kind>-<einheit>         Übersicht: Etappen-Weg, danach Test
// #/lerneinheit/<kind>-<einheit>-<n>     Etappe n: Kurz erklärt → Selbst probieren → geschafft
// #/lerneinheit/<kind>-<einheit>-test    Test / Verbessern / Nachtest
// Eine Etappe ist ein Lernziel; geschafft, wenn ihre Übungsaufgaben einmal richtig gelöst sind (Datenbank: schule.etappen_stand).

// Text mit ⟦markierten⟧ Stellen als Knoten (markierte Teile hervorgehoben).
function lernMarkiert(t) {
  const teile = String(t ?? '').split(/⟦|⟧/);
  return teile.map((s, i) => (i % 2 ? el('mark', {}, lernText(s)) : lernText(s)));
}
function lernStellentafel(b) {
  return el('table', { class: 'lr-stellentafel', 'aria-label': 'Stellenwerttafel' },
    el('tr', {}, ...(b.stellen || []).map((s) => el('th', {}, s))),
    el('tr', {}, ...(b.ziffern || []).map((z, i) => el('td', { class: i === b.markiert ? 'on' : '' }, z))));
}
function lernBild(b) {
  if (!b) return null;
  if (b.typ === 'zahlenstrahl') return el('div', { class: 'lr-bild' }, lernZahlenstrahl(b, false));
  if (b.typ === 'stellentafel') return el('div', { class: 'lr-bild' }, lernStellentafel(b));
  return null;
}
// Erklärung einer Etappe: Regel, vorgerechnetes Beispiel Schritt für Schritt, Probe, typischer Fehler.
function lernErklaerung(e, { kurz = false } = {}) {
  return el('div', { class: 'lr-erklaert' },
    lernBild(e.bild),
    el('p', { class: 'lr-regel' }, ...lernMarkiert(e.regel)),
    e.schritte?.length ? el('div', { class: 'lr-sogehts' }, el('p', { class: 'lr-ueber' }, 'SO GEHT’S'),
      el('ol', {}, ...e.schritte.map((s) => el('li', {}, el('span', {}, ...lernMarkiert(s)))))) : null,
    e.probe ? el('p', { class: 'lr-probe' }, 'Probe: ', ...lernMarkiert(e.probe)) : null,
    e.fehler && !kurz ? el('div', { class: 'lr-fehler' }, el('p', { class: 'lr-ueber' }, 'ACHTUNG, TYPISCHER FEHLER'), el('p', {}, ...lernMarkiert(e.fehler))) : null);
}

// Etappen einer Einheit (Fallback ohne gepflegte Etappen: je Lernziel eine Etappe ohne Erklärung).
function lernEtappen(daten) {
  const inh = daten.inhalt || {};
  const pflicht = new Map((daten.stand || []).map((s) => [s.lernziel, s.pflicht]));
  const st = daten.etappen_stand || {};
  const liste = inh.etappen?.length ? inh.etappen
    : [...new Set((daten.uebungen || []).map((a) => a.lernziel))].map((lz) => ({ lernziel: lz, titel: lernZielName(lz), regel: '' }));
  const abschnitt = new Map();
  for (const ab of inh.abschnitte || []) for (const lz of ab.lernziele || []) abschnitt.set(lz, ab.titel);
  return liste.map((e, i) => {
    const k = st[e.lernziel] || {};
    return { ...e, nr: i + 1, fertig: !!k.fertig, extra: pflicht.get(e.lernziel) === false, abschnitt: abschnitt.get(e.lernziel) || null,
      serie: Number(k.serie || 0), ziel: Number(k.ziel || 4), sitzt: !!k.sitzt, faellig: !!k.faellig, nachgewiesen: !!k.fertig && !k.sitzt,
      aufgaben: (daten.uebungen || []).filter((a) => a.lernziel === e.lernziel) };
  });
}
// Punkte für die Serie: ●●○○ (gefüllt = richtig in Folge), bei „sitzt“ alle gefüllt.
function lernPunkte(e, { gross = false } = {}) {
  const n = Math.max(1, e.ziel || 4), voll = e.sitzt || e.fertig ? n : Math.min(n, e.serie || 0);
  return el('span', { class: 'lr-punkte' + (gross ? ' gross' : ''), role: 'img', 'aria-label': e.sitzt || e.fertig ? 'sitzt' : `${voll} von ${n} richtig in Folge` },
    ...Array.from({ length: n }, (_, i) => el('i', { class: i < voll ? 'voll' : '' })));
}
const lernKartenStatus = (e) => e.faellig ? 'Wiederholen' : e.sitzt || e.fertig ? 'sitzt' : e.serie ? 'am Üben' : 'neu';
// Bereiche: aus inhalt.abschnitte, sonst ein Bereich mit allen Karten.
function lernBereiche(etappen) {
  const map = new Map();
  for (const e of etappen) { const t = e.abschnitt || 'Lernkarten'; if (!map.has(t)) map.set(t, []); map.get(t).push(e); }
  return [...map].map(([titel, karten]) => ({ titel, karten }));
}

async function viewLernEinheit(arg) {
  setChrome('Lerneinheit', { back: true, showTabs: false });
  const live = viewGuard();
  const [kindId, einheitId, teil] = String(arg || '').split('-');
  const k = Number(kindId), eId = Number(einheitId);
  if (!k || !eId) { route('lernen'); return; }
  loading();
  const [daten, konto, uebers] = await Promise.all([lernCall('schule_einheit_lesen', { lernender_id: k, einheit_id: eId }),
    lernCall('schule_konto', { lernender_id: k }).catch(() => null), lernCall('schule_uebersicht').catch(() => null)]);
  if (!live()) return;
  const kind = { id: k, ...(konto?.look || {}) };
  const ort = (uebers?.einheiten || []).find((e) => e.id === eId) || {};
  const titel = ort.stadt ? `${ort.stadt}: ${ort.ort_titel || ort.titel || ''}` : (daten.inhalt?.ziel || 'Lerneinheit').split(/[:;.]/)[0];
  $('#title').textContent = titel;
  const ctx = { kind: k, einheit: eId, live, daten, ort, titel, kindObj: kind, basis: `#/lerneinheit/${k}-${eId}`, leitung: !!uebers?.leitung };
  const etappen = lernEtappen(daten);
  lernTitel = new Map(etappen.filter((e) => daten.inhalt?.etappen?.length).map((e) => [e.lernziel, e.titel]));
  ctx.titelKurz = ort.titel || titel;
  if (teil === 'test' || (!teil && daten.laufender_test)) { lernEinheitTest(ctx); return; }
  // #/lerneinheit/k-e[-erklaeren|-ueben[-n]|-fehler|-n]
  const rest = String(arg).split('-').slice(3);
  const n = Number(teil);
  if (n && etappen[n - 1]) { lernThemaSeite(ctx, etappen, 'ueben', n); return; }
  lernThemaSeite(ctx, etappen, ['ueben', 'fehler'].includes(teil) ? teil : 'erklaeren', Number(rest[0]) || 0);
}

// ---------- Thema: Erklären | Üben | Typische Fehler (Aufbau wie das Mathe-Lernblatt) ----------
function lernTestTeil(ctx, etappen) {
  const { daten } = ctx;
  const pflicht = etappen.filter((e) => !e.extra);
  const offen = pflicht.filter((e) => !e.fertig).length;
  if (daten.laufender_test) return el('a', { class: 'lr-knopf', href: `${ctx.basis}-test` }, 'Angefangenen Test weitermachen');
  if (daten.blocktest_fertig) return el('a', { class: 'lr-zeile', href: `${ctx.basis}-test` }, el('span', { class: 'lr-zeile-icon' }, lernIcon(LI.stempel, 22)),
    el('span', { class: 'lr-zeile-text' }, el('b', {}, 'Test, Verbessern und Nachtests'), el('small', {}, daten.nachtest?.grund === 'faellig' ? 'Ein Nachtest ist jetzt dran.' : 'Hier siehst du, was als Nächstes kommt.')), lernIcon(LI.pfeil, 20));
  if (!offen) return el('a', { class: 'lr-knopf', href: `${ctx.basis}-test` }, 'Alle Lernkarten sitzen – Test starten');
  return el('p', { class: 'lr-gesperrt' }, lernIcon('M6 11h12v10H6z|M9 11V8a3 3 0 0 1 6 0v3', 20), `Der Test kommt, wenn alle Lernkarten sitzen (noch ${offen}).`);
}

function lernThemaSeite(ctx, etappen, start, karteNr) {
  const { daten, kindObj: kind } = ctx;
  // Tabs schreiben die Adresse per replaceState um; die Ansicht bleibt gültig, bis neu gerendert wird.
  const gen = renderGeneration; ctx.live = () => gen === renderGeneration;
  const pflicht = etappen.filter((e) => !e.extra);
  const sitzen = () => pflicht.filter((e) => e.fertig).length;
  const empfohlen = () => etappen.find((e) => e.faellig) || etappen.find((e) => !e.fertig && !e.extra) || etappen.find((e) => !e.fertig) || etappen[0];
  const fehlerKarten = etappen.filter((e) => e.fehler);
  const fortschritt = el('div', { class: 'lr-fortschritt' });
  const zeichneFortschritt = () => fortschritt.replaceChildren(
    el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${sitzen()} von ${pflicht.length} Lernkarten sitzen` }, el('span', { style: `width:${pflicht.length ? Math.round(100 * sitzen() / pflicht.length) : 0}%` })),
    el('b', {}, `${sitzen()} von ${pflicht.length} sitzen`));
  zeichneFortschritt();
  const tabs = { erklaeren: null, ueben: null, fehler: null };
  const panels = { erklaeren: el('section', { class: 'lr-panel', role: 'tabpanel' }), ueben: el('section', { class: 'lr-panel', role: 'tabpanel' }), fehler: el('section', { class: 'lr-panel', role: 'tabpanel' }) };
  const anzahlUeben = etappen.reduce((n, e) => n + e.aufgaben.length, 0);
  const tabLeiste = el('div', { class: 'lr-tabs lr-tabs-3', role: 'tablist', 'aria-label': 'Thema' },
    ...[['erklaeren', 'Erklären', null], ['ueben', 'Üben', anzahlUeben], ['fehler', 'Fehler', fehlerKarten.length]].map(([k, t, n]) => {
      tabs[k] = el('button', { type: 'button', role: 'tab', onclick: () => zeige(k) }, t, n ? el('small', {}, ' ' + n) : null);
      return tabs[k];
    }));
  const zeige = (k, opts = {}) => {
    for (const x of Object.keys(tabs)) { tabs[x].setAttribute('aria-selected', String(x === k)); panels[x].hidden = x !== k; }
    if (k === 'ueben') uebenOeffnen(opts.karte);
    try { history.replaceState(null, '', `${ctx.basis}-${k}${k === 'ueben' && aktKarte ? '-' + aktKarte.nr : ''}`); } catch { /* egal */ }
    if (opts.scrollZu) opts.scrollZu.scrollIntoView({ block: 'start' }); else window.scrollTo(0, 0);
  };

  // --- Erklären: alle Lernkarten untereinander, nach Bereichen
  const kartenBox = new Map();
  const bereiche = lernBereiche(etappen);
  panels.erklaeren.append(...bereiche.map((b) => el('section', { class: 'lr-bereich' },
    bereiche.length > 1 ? el('h2', { class: 'lr-abschnitt' }, b.titel.toUpperCase()) : null,
    ...b.karten.map((e) => {
      const box = el('article', { class: 'lr-karte-box lr-lernkarte' + (e === empfohlen() ? ' jetzt' : '') },
        el('div', { class: 'lr-lernkarte-kopf' }, el('h3', {}, `${e.nr} · ${e.titel}`), el('span', { class: 'lr-lk-status' }, lernPunkte(e), el('small', {}, lernKartenStatus(e)))),
        e.regel ? lernErklaerung(e) : el('p', { class: 'lr-leise' }, 'Für diese Karte gibt es noch keine Erklärung.'),
        e.aufgaben.length ? el('button', { type: 'button', class: 'lr-knopf-zweit lr-dazu', onclick: () => zeige('ueben', { karte: e }) }, 'Dazu üben ▸') : null,
        ctx.leitung ? lernAnmerkung({ einheit_id: ctx.einheit, lernziel: e.lernziel, lernender_id: ctx.kind }, 'Anmerkung zu dieser Erklärung') : null);
      kartenBox.set(e.lernziel, box);
      return box;
    }))),
  lernTestTeil(ctx, etappen),
  ctx.leitung ? lernAnmerkung({ einheit_id: ctx.einheit, lernender_id: ctx.kind }, 'Anmerkung zu diesem Thema') : null);

  // --- Typische Fehler
  const versucht = etappen.flatMap((e) => e.aufgaben.filter((a) => a.versuche && !a.geloest).map((a) => ({ e, a })));
  panels.fehler.append(
    el('p', { class: 'lr-leise' }, 'Die Stellen, an denen es oft schiefgeht.'),
    ...(fehlerKarten.length ? fehlerKarten.map((e) => el('article', { class: 'lr-karte-box lr-fehlerkarte' },
      el('h3', {}, `${e.nr} · ${e.titel}`), el('div', { class: 'lr-fehler' }, el('b', {}, 'Achtung: '), ...lernMarkiert(e.fehler)),
      el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => zeige('erklaeren', { scrollZu: kartenBox.get(e.lernziel) }) }, 'Erklärung ansehen'))) : [el('p', { class: 'lr-leise' }, 'Für dieses Thema sind noch keine typischen Fehler eingetragen.')]),
    versucht.length ? el('section', { class: 'lr-karte-box' }, el('h3', {}, `Hat bei dir noch nicht geklappt (${versucht.length})`),
      el('ul', { class: 'lr-meinefehler' }, ...versucht.slice(0, 8).map(({ e, a }) => el('li', {}, el('span', {}, lernText(a.frage?.text || '')),
        el('button', { type: 'button', class: 'lr-knopf-zweit lr-knopf-klein', onclick: () => zeige('ueben', { karte: e }) }, 'Üben'))))) : null);

  // --- Üben: eine Lernkarte, Aufgaben nacheinander; Erklärung klappt an der Aufgabe auf
  let aktKarte = null, stufe = 0;
  let gezeichnet = null;
  const uebenOeffnen = (karte) => {
    if (karte && karte !== aktKarte) { aktKarte = karte; stufe = 0; }
    if (!aktKarte) aktKarte = (karteNr && etappen[karteNr - 1]) || empfohlen();
    if (gezeichnet !== aktKarte) zeichneUeben(); // sonst bleibt Aufgabe samt Rückmeldung stehen
  };
  const zeichneUeben = () => {
    const e = aktKarte; gezeichnet = e;
    const chipsKarten = el('div', { class: 'lr-chips lr-chips-scroll', role: 'group', 'aria-label': 'Lernkarte' },
      ...etappen.filter((x) => x.aufgaben.length).map((x) => el('button', { type: 'button', class: x === e ? 'on' : '', 'aria-pressed': String(x === e), onclick: () => { aktKarte = x; zeichneUeben(); } }, `${x.nr} · ${x.titel}`)));
    const chipsStufe = el('div', { class: 'lr-chips', role: 'group', 'aria-label': 'Stufe' },
      ...[[0, 'alle'], [1, 'leicht'], [2, 'mittel'], [3, 'schwer']].filter(([n]) => !n || e.aufgaben.some((a) => a.stufe === n))
        .map(([n, t]) => el('button', { type: 'button', class: stufe === n ? 'on' : '', 'aria-pressed': String(stufe === n), onclick: () => { stufe = n; zeichneUeben(); } }, t)));
    const punkte = el('div', { class: 'lr-lk-punkte' });
    const zeichnePunkte = () => punkte.replaceChildren(lernPunkte(e, { gross: true }),
      el('small', {}, e.sitzt || e.fertig ? (e.faellig ? 'Sitzt – heute wiederholen' : 'Sitzt! Du kannst trotzdem weiterüben.') : `${Math.min(e.serie, e.ziel)} von ${e.ziel} richtig hintereinander`));
    zeichnePunkte();
    const flaeche = el('div', { class: 'lr-ueben-flaeche' });
    panels.ueben.replaceChildren(chipsKarten, chipsStufe, el('div', { class: 'lr-karte-box lr-lk-zeile' }, el('b', {}, `${e.nr} · ${e.titel}`), punkte), flaeche);
    const pool = e.aufgaben.filter((a) => !stufe || a.stufe === stufe);
    const warte = [...pool].sort((a, b) => (a.geloest === b.geloest ? 0 : a.geloest ? 1 : -1) || (a.versuche || 0) - (b.versuche || 0) || (a.stufe || 2) - (b.stufe || 2));
    let sterne = 0, nr = 0;
    const naechsteKarte = etappen.slice(e.nr).find((x) => !x.fertig && x.aufgaben.length) || etappen.find((x) => x !== e && !x.fertig && x.aufgaben.length);
    const zeigeAufgabe = () => {
      const a = warte[0];
      if (!a) { flaeche.replaceChildren(el('p', { class: 'lr-leise' }, 'Für diese Auswahl gibt es keine Aufgaben.')); return; }
      nr++;
      const auf = lernAufgabe(a); let hilfe = 0; const cid = lernCid();
      const meldung = el('div', { role: 'status', 'aria-live': 'polite' });
      const hilfeBox = el('div', { class: 'lr-hilfebox' });
      const tipp = a.tipp ? el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { hilfe = 1; tipp.remove(); hilfeBox.append(el('p', { class: 'lr-tipp' }, el('b', {}, 'Tipp: '), lernText(a.tipp), el('small', {}, ' (zählt nicht für die Punkte)'))); } }, 'Tipp') : null;
      const erkl = e.regel ? el('button', { type: 'button', class: 'lr-knopf-zweit', 'aria-expanded': 'false', onclick: () => {
        const offen = erkl.getAttribute('aria-expanded') === 'true';
        erkl.setAttribute('aria-expanded', String(!offen)); erklBox.hidden = offen;
      } }, 'Erklärung') : null;
      const erklBox = el('div', { class: 'lr-karte-box lr-nochmal', hidden: true }, e.regel ? lernErklaerung(e, { kurz: true }) : null);
      const pruefen = el('button', { type: 'button', class: 'lr-knopf' }, 'Prüfen');
      auf.node.addEventListener('input', () => { if (!pruefen.disabled && pruefen.isConnected) meldung.replaceChildren(); });
      pruefen.addEventListener('click', async () => {
        const w = auf.antwort();
        if (!w) { meldung.replaceChildren(el('p', { class: 'lr-hinweis' }, auf.fehlerText() || 'Bitte erst antworten.')); return; }
        pruefen.disabled = true;
        try {
          const r = await lernCall('schule_uebung_pruefen', { lernender_id: ctx.kind, aufgabe_id: a.id, antwort: w, client_id: cid, hilfe });
          if (!ctx.live()) return;
          if (!r.format_ok) { meldung.replaceChildren(el('p', { class: 'lr-hinweis' }, r.hinweis)); pruefen.disabled = false; return; }
          auf.sperren(); a.loesung = r.loesung; warte.shift(); a.versuche = (a.versuche || 0) + 1;
          if (r.richtig) { if (!a.geloest && !r.wiederholt) sterne += 10; a.geloest = true; warte.push(a); }
          else warte.splice(Math.min(3, warte.length), 0, a);
          const warSitzt = e.sitzt;
          if (r.karte) { e.serie = r.karte.serie; e.ziel = r.karte.ziel; e.sitzt = r.karte.sitzt; e.fertig = e.fertig || r.karte.sitzt; if (warSitzt && r.karte.sitzt) e.faellig = false; }
          zeichnePunkte(); zeichneFortschritt();
          const jetztSitzt = !!r.karte?.neu_sitzt || (!warSitzt && e.sitzt);
          const weiter = el('button', { type: 'button', class: 'lr-knopf', onclick: zeigeAufgabe }, 'Nächste Aufgabe');
          pruefen.replaceWith(weiter);
          if (!r.richtig && erkl && erklBox.hidden) { erklBox.hidden = false; erkl.setAttribute('aria-expanded', 'true'); }
          meldung.replaceChildren(r.richtig
            ? el('div', { class: 'lr-rueck lr-rueck-ok' }, el('b', {}, 'Richtig!'), r.loesungsweg ? el('p', {}, lernText(r.loesungsweg)) : null)
            : el('div', { class: 'lr-rueck lr-rueck-falsch' }, el('b', {}, 'Noch nicht. Richtig ist: ' + lernLoesungText(a)),
              a.antworttyp === 'luecken' && lernIstTermVorlage(a.frage?.schablone) && lernGleichwertigAusgeklammert(a.frage?.schablone, w.werte, r.loesung?.werte)
                ? el('p', {}, 'Dein Term ist gleichwertig, aber noch nicht vollständig ausgeklammert: Vor die Klammer gehört der größte gemeinsame Faktor.') : null,
              r.loesungsweg ? el('p', {}, el('b', {}, 'So geht’s: '), lernText(r.loesungsweg)) : null,
              el('p', { class: 'lr-leise' }, 'Die Punkte fangen wieder bei 0 an. Die Erklärung steht oben an der Aufgabe.')));
          if (jetztSitzt) meldung.append(el('section', { class: 'lr-geschafft lr-sitzt' },
            el('div', { class: 'lr-geschafft-haken' }, lernIcon(LI.haken, 48)),
            el('p', { class: 'lr-ueber' }, 'LERNKARTE SITZT'), el('h2', {}, e.titel),
            sterne ? el('p', { class: 'lr-sterne-neu' }, lernIcon(LI.stern, 20), ` +${sterne} Sterne`) : null,
            el('p', { class: 'lr-leise' }, 'Sie kommt in ein paar Tagen zum Wiederholen.'),
            naechsteKarte ? el('button', { type: 'button', class: 'lr-knopf', onclick: () => { aktKarte = naechsteKarte; stufe = 0; zeichneUeben(); window.scrollTo(0, 0); } }, `Nächste Karte: ${naechsteKarte.titel}`)
              : el('button', { type: 'button', class: 'lr-knopf', onclick: () => zeige('erklaeren') }, 'Zur Themen-Übersicht')));
          (jetztSitzt ? meldung : weiter).scrollIntoView?.({ block: 'center', behavior: 'smooth' });
        } catch (err) { meldung.replaceChildren(el('p', { class: 'err-text' }, err.message)); pruefen.disabled = false; }
      });
      flaeche.replaceChildren(
        el('section', { class: 'lr-karte-box lr-aufgabe' },
          el('p', { class: 'lr-ueber' }, `AUFGABE ${nr}` + (a.stufe ? ` · ${['', 'LEICHT', 'MITTEL', 'SCHWER'][a.stufe] || ''}` : '')), auf.node,
          el('div', { class: 'lr-knopfzeile' }, tipp, erkl)),
        hilfeBox, erklBox, meldung, pruefen,
        ctx.leitung ? lernAnmerkung({ einheit_id: ctx.einheit, lernziel: e.lernziel, aufgabe_id: a.id, lernender_id: ctx.kind }, 'Anmerkung zu dieser Aufgabe') : null);
    };
    zeigeAufgabe();
  };

  const flaeche = el('div', { class: 'lr-thema' },
    el('header', { class: 'lr-kopf' },
      el('p', { class: 'lr-pfad' }, el('a', { href: `#/reise/${ctx.kind}` }, 'Heute'), ` › ${ctx.ort.stadt || 'Thema'}`),
      el('h1', { class: 'lr-titel' }, ctx.titelKurz),
      lernJahrgangText(ctx.ort.jahrgang) ? el('p', { class: 'lr-leise lr-jahrgang' }, lernJahrgangText(ctx.ort.jahrgang)) : null),
    fortschritt,
    daten.status === 'entwurf' ? el('p', { class: 'lr-leise' }, 'Entwurf – nur für das Testkind sichtbar.') : null,
    tabLeiste, panels.erklaeren, panels.ueben, panels.fehler);
  main.replaceChildren(lernRahmen(kind, 'weg', flaeche));
  zeige(start);
}
const LERN_SCHULART = { gym_by: 'Gymnasium', rs_by: 'Realschule', ib_myp: 'IB MYP' };
function lernJahrgangText(j) {
  if (!j || !Object.keys(j).length) return '';
  return [['gym_by', 'Gym'], ['rs_by', 'RS'], ['ib_myp', 'IB']].filter(([k]) => j[k]).map(([k, t]) => `${t} ${j[k]}`).join(' · ');
}

function lernEinheitTest(ctx) {
  const body = el('div', { class: 'lern-body' });
  main.replaceChildren(lernRahmen(ctx.kindObj, 'weg',
    el('header', { class: 'lr-kopf' }, el('p', { class: 'lr-ueber' }, 'TEST'), el('h1', { class: 'lr-titel' }, ctx.titel)),
    el('a', { class: 'lr-zurueck', href: ctx.basis }, '‹ Zu den Etappen'), body));
  body.append(lernTestStart(ctx, body));
}

// ---------- Merkheft-Daten ----------
// Je Einheit: Etappen mit Stand. Nutzt schule_merkheft; fehlt die Aktion (Server noch alt), werden die Einheiten einzeln gelesen.
async function lernMerkDaten(d) {
  try { const r = await lernCall('schule_merkheft', { lernender_id: d.kind.id }); return r.einheiten || []; }
  catch (err) {
    if (!/Unbekannte Aktion/.test(err.message)) throw err;
    const liste = await Promise.all(d.mit.map((e) => lernCall('schule_einheit_lesen', { lernender_id: d.kind.id, einheit_id: e.id }).then((x) => ({ e, x })).catch(() => null)));
    return liste.filter((y) => y && y.x.inhalt?.etappen).map(({ e, x }) => ({ einheit_id: e.id, block_id: e.block_id, stadt: e.stadt, ort_titel: e.ort_titel, kontinent: e.kontinent,
      etappen: x.inhalt.etappen, stand: x.etappen_stand || {}, blocktest_fertig: x.blocktest_fertig, nachtest: x.nachtest }));
  }
}
const lernEtappenZahl = (m) => { const n = (m?.etappen || []).length; const f = (m?.etappen || []).filter((e) => m.stand?.[e.lernziel]?.fertig).length; return { n, f }; };

// ---------- Kind: Mein Weg ----------
async function viewWeg(arg) {
  setChrome('Mein Weg', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const merk = await lernMerkDaten(d).catch(() => []);
  if (!live()) return;
  const { kind } = d;
  $('#title').textContent = 'Mein Weg';
  const mm = new Map(merk.map((m) => [m.einheit_id, m]));
  const kann = d.orte.filter((o) => o.zustand === 'fertig' || o.zustand === 'kann');
  const offen = d.orte.filter((o) => o.zustand === 'offen');
  const passt = offen.filter((o) => !o.ziel_klasse || !kind.klasse || o.ziel_klasse <= kind.klasse);
  const zahl = (w, t, cls) => el('div', { class: 'lr-zahl ' + (cls || '') }, el('b', {}, String(w)), el('span', {}, t));
  const dran = d.jetzt.map((e) => {
    const { n, f } = lernEtappenZahl(mm.get(e.id));
    const info = e.laeuft ? 'Test läuft' : e.blocktest ? 'Test geschrieben' : n ? (f >= n ? 'Test offen' : `Etappe ${f + 1}/${n}`) : `${e.fertig}/${e.n}`;
    return el('a', { class: 'lr-dran', href: `#/lerneinheit/${kind.id}-${e.id}` },
      el('div', { class: 'lr-dran-kopf' }, el('b', {}, `${e.stadt}: ${e.ort_titel || e.titel}`), el('span', {}, info + ' ›')),
      el('small', {}, `${e.kontinent || ''} · Kl. ${e.ziel_klasse || '–'}`),
      el('div', { class: 'lr-balken' }, el('span', { style: `width:${n ? Math.round(100 * f / n) : 0}%` })));
  });
  const ortZeile = (o, rechts, icon, href) => el(href ? 'a' : 'div', { class: 'lr-wegzeile', ...(href ? { href } : {}) },
    el('span', { class: 'lr-wegzeile-icon ' + (icon === 'haken' ? 'fertig' : '') }, icon === 'haken' ? lernIcon(LI.haken, 16) : null),
    el('span', { class: 'lr-zeile-text' }, el('b', {}, o.titel), el('small', {}, `${o.kontinent_titel || ''} · ${o.stadt}${o.ziel_klasse ? ' · Kl. ' + o.ziel_klasse : ''}`)),
    rechts ? el('span', { class: 'lr-zeile-zustand' }, rechts) : null);
  const kannZeilen = kann.map((o) => {
    const e = d.mit.find((x) => x.block_id === o.block_id); const m = e && mm.get(e.id);
    const nt = m?.nachtest;
    const info = o.zustand === 'kann' ? 'konnte ich schon' : nt?.grund === 'faellig' ? 'Nachtest dran' : nt?.grund === 'noch_nicht_faellig' ? `Nachtest in ${nt.lerntage_noetig - nt.lerntage_seit} Lerntagen` : nt?.grund === 'gesichert' ? 'sicher' : 'Stempel';
    return ortZeile(o, info, 'haken', m ? `#/merkheft/${kind.id}` : null);
  });
  main.replaceChildren(lernRahmen(kind, 'weg',
    el('header', { class: 'lr-kopf' }, el('p', { class: 'lr-ueber' }, `MATHE${kind.klasse ? ' · KLASSE ' + kind.klasse : ''}`), el('h1', { class: 'lr-titel' }, 'Mein Weg')),
    el('div', { class: 'lr-zahlen' }, zahl(kann.length, 'kann ich', 'gut'), zahl(d.jetzt.length, 'gerade dran'), zahl(offen.length, 'kommen noch')),
    el('h2', { class: 'lr-abschnitt lr-abschnitt-jetzt' }, 'GERADE DRAN'),
    ...(dran.length ? dran : [el('p', { class: 'lr-leise' }, 'Gerade ist nichts offen.')]),
    el('h2', { class: 'lr-abschnitt' }, `KOMMT NOCH${kind.klasse ? ' · BIS KLASSE ' + kind.klasse : ''}`),
    passt.length ? el('div', { class: 'lr-wegliste' }, ...passt.slice(0, 5).map((o) => ortZeile(o, o.hat_einheit ? 'bereit' : 'bald'))) : el('p', { class: 'lr-leise' }, 'Für deine Klasse ist alles verteilt.'),
    passt.length > 5 || offen.length > passt.length ? el('details', { class: 'lr-mehr' }, el('summary', {}, `Alle weiteren Orte (${offen.length - Math.min(5, passt.length)})`),
      el('div', { class: 'lr-wegliste' }, ...[...passt.slice(5), ...offen.filter((o) => !passt.includes(o))].map((o) => ortZeile(o, o.ziel_klasse ? 'Kl. ' + o.ziel_klasse : '')))) : null,
    el('h2', { class: 'lr-abschnitt' }, 'KANN ICH'),
    kannZeilen.length ? el('div', { class: 'lr-wegliste' }, ...kannZeilen.slice(0, 6)) : el('p', { class: 'lr-leise' }, 'Dein erster geschaffter Ort erscheint hier.'),
    kannZeilen.length > 6 ? el('details', { class: 'lr-mehr' }, el('summary', {}, `Alle ${kannZeilen.length} anzeigen`), el('div', { class: 'lr-wegliste' }, ...kannZeilen.slice(6))) : null,
    el('a', { class: 'lr-zeile', href: `#/reisepass/${kind.id}` }, el('span', { class: 'lr-zeile-icon' }, lernIcon(LI.pass, 22)),
      el('span', { class: 'lr-zeile-text' }, el('b', {}, 'Reisepass'), el('small', {}, `${d.konto?.stempel ?? 0} Stempel · ${lernZahl(d.konto?.sterne ?? 0)} Sterne · Belohnungen · Look`)), lernIcon(LI.pfeil, 20))));
}

// ---------- Kind: Merkheft ----------
async function viewMerkheft(arg) {
  setChrome('Merkheft', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const merk = await lernMerkDaten(d).catch(() => []);
  if (!live()) return;
  const { kind } = d;
  $('#title').textContent = 'Merkheft';
  // Einträge: alle Lernkarten der Orte, die gerade dran oder geschafft sind – zum Nachlesen, ohne etwas zu lösen.
  const sichtbar = new Set([...d.jetzt, ...d.kann].map((e) => e.id));
  const eintraege = [];
  for (const m of merk) if (sichtbar.has(m.einheit_id)) (m.etappen || []).forEach((e, i) => {
    const k = m.stand?.[e.lernziel] || {};
    eintraege.push({ m, e, nr: i + 1, status: lernKartenStatus({ ...k, serie: Number(k.serie || 0) }) });
  });
  const suche = el('input', { type: 'search', class: 'lr-suche', placeholder: 'Suchen, z. B. runden', 'aria-label': 'Merkheft durchsuchen', autocomplete: 'off' });
  const liste = el('div', { class: 'lr-merkliste' });
  const norm = (s) => String(s || '').toLowerCase();
  const zeichne = () => {
    const q = norm(suche.value.trim());
    const treffer = eintraege.filter(({ m, e }) => !q || [e.titel, e.regel, ...(e.schritte || []), e.fehler, m.stadt, m.ort_titel].some((t) => norm(t).includes(q)));
    if (!eintraege.length) { liste.replaceChildren(el('p', { class: 'lr-leise' }, 'Noch leer.')); return; }
    if (!treffer.length) { liste.replaceChildren(el('p', { class: 'lr-leise' }, 'Nichts gefunden.')); return; }
    const gruppen = new Map();
    for (const t of treffer) { if (!gruppen.has(t.m.einheit_id)) gruppen.set(t.m.einheit_id, []); gruppen.get(t.m.einheit_id).push(t); }
    liste.replaceChildren(...[...gruppen.values()].map((ts) => el('section', { class: 'lr-merkgruppe' },
      el('h2', { class: 'lr-abschnitt' }, `${ts[0].m.stadt || ''} · ${ts[0].m.ort_titel || ''}`.toUpperCase()),
      ...ts.map(({ m, e, nr, status }) => el('details', { class: 'lr-merk', ...(q && treffer.length <= 3 ? { open: '' } : {}) },
        el('summary', {}, el('b', {}, e.titel), el('small', { class: 'lr-merk-status' }, status), lernIcon(LI.pfeil, 18)),
        el('div', { class: 'lr-merk-inhalt' }, lernErklaerung(e),
          el('a', { class: 'lr-knopf lr-knopf-klein', href: `#/lerneinheit/${kind.id}-${m.einheit_id}-ueben-${nr}` }, 'Üben')))))));
  };
  suche.addEventListener('input', zeichne);
  zeichne();
  main.replaceChildren(lernRahmen(kind, 'merkheft',
    el('header', { class: 'lr-kopf' }, el('h1', { class: 'lr-titel' }, 'Merkheft'), el('p', { class: 'lr-leise' }, 'Alle Erklärungen zum Nachlesen – jederzeit, ohne Aufgaben zu lösen.')),
    eintraege.length ? suche : null, liste));
}

// ---------- Test ----------
const lernNtTitel = (nt) => nt.art === 'wiederholung' ? 'Nachtest wiederholen' : nt.folgerunde ? 'Weiterer Nachtest (bis alles sicher ist)' : `Nachtest ${nt.runde} von 3`;

function lernTestStart(ctx, body) {
  const box = el('div', { class: 'lern-test' });
  const stand = ctx.daten.stand || [];
  const offen = ctx.daten.laufender_test;
  const hatFehler = stand.some((s) => s.status === 'fehler');
  const blockFertig = ctx.daten.blocktest_fertig ?? stand.some((s) => s.status !== 'offen');
  const nt = ctx.daten.nachtest || {};
  const start = async (art) => {
    box.replaceChildren(el('div', { class: 'spinner' }, 'Test wird vorbereitet …'));
    try {
      const r = await lernCall('schule_test_starten', { lernender_id: ctx.kind, einheit_id: ctx.einheit, art });
      if (!ctx.live()) return;
      if (!r.ok) {
        const t = r.grund === 'noch_nicht_faellig' ? 'Der nächste Nachtest ist noch nicht dran. ' + (r.noch_nicht_faellig || []).map((x) => `Noch ${x.lerntage_noetig - x.lerntage_seit} Lerntage.`).join(' ')
          : r.grund === 'erst_korrektur' ? 'Erst die Lernziele mit „noch üben“ verbessern, dann kommt der Nachtest.'
          : r.grund === 'vorrat_erschoepft' ? 'Für ' + (r.vorrat_erschoepft || []).map(lernZielName).join(', ') + ' gibt es gerade keine neue Aufgabe. Sag Bescheid, dann kommen neue dazu.'
          : 'Gerade gibt es nichts zu testen.';
        box.replaceChildren(el('p', { class: 'card' }, t)); return;
      }
      lernTestLauf(ctx, box, r);
    } catch (e) { box.replaceChildren(el('p', { class: 'card err-text' }, e.message)); }
  };
  const knopf = (t, art, text) => el('div', { class: 'card' }, el('h3', {}, t), el('p', { class: 'small' }, text),
    el('button', { type: 'button', class: 'primary', onclick: () => start(art) }, t + ' starten'));
  if (ctx.daten.verblasst) box.append(el('p', { class: 'lern-hinweis' }, 'Rückreise: Diese Einheit sitzt noch nicht sicher. Erst verbessern, dann den Nachtest wiederholen.'));
  if (offen) box.append(el('div', { class: 'card' }, el('h3', {}, 'Angefangener Test'), el('p', { class: 'small' }, 'Deine bisherigen Antworten sind gespeichert.'),
    el('button', { type: 'button', class: 'primary', onclick: () => start(offen.art) }, 'Weitermachen')));
  else {
    if (!blockFertig) box.append(knopf('Test', 'blocktest', 'Eine Aufgabe je Lernziel, ohne Tipps. Die Lösungen siehst du nach dem Abgeben.'));
    if (hatFehler) box.append(knopf('Verbessern', 'korrektur', 'Nur die Lernziele, die noch nicht geklappt haben – mit neuen Aufgaben. Übe sie vorher noch einmal.'));
    if (nt.grund === 'faellig') box.append(knopf(lernNtTitel(nt), 'nachtest',
      'Alle Lernziele der Einheit, ohne Tipps. Ab 80 % zählt die Runde. Unter 60 % geht es auf eine Rückreise zu diesem Ort.'));
    else if (nt.grund === 'noch_nicht_faellig') box.append(el('div', { class: 'card' }, el('h3', {}, lernNtTitel(nt)),
      el('p', { class: 'small' }, `Dran in ${nt.lerntage_noetig - nt.lerntage_seit} Lerntag(en). Ein Lerntag zählt, wenn an dem Tag geübt oder getestet wurde.`)));
    if (nt.grund === 'gesichert') box.append(el('p', { class: 'card' }, 'Alles geschafft und gesichert. 🎉'));
    if (!box.querySelector('.card')) box.append(el('p', { class: 'card' }, 'Gerade gibt es keinen Test. Üb weiter!'));
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
      if (!w && auf.fehlerText()) { meldung.replaceChildren(el('p', { class: 'lern-hinweis' }, auf.fehlerText())); return null; }
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
      r.einheit_abgeschlossen ? el('p', { class: 'lern-rueck ok' }, el('b', {}, 'Einheit geschafft! 🎉')) : el('p', { class: 'small' }, 'Bei „noch üben“: die passenden Etappen noch einmal üben, dann „Verbessern“.'),
      r.nachtest_ergebnis ? el('p', { class: 'lern-rueck ' + (r.nachtest_ergebnis === 'bestanden' ? 'ok' : 'falsch') }, el('b', {}, {
        bestanden: r.nachtest?.folgerunde && r.nachtest_runde >= 3 ? 'Nachtest geschafft (ab 80 %).' : `Nachtest-Runde ${r.nachtest_runde} geschafft (ab 80 %).`,
        wiederholen: 'Unter 80 %: Diese Runde zählt noch nicht. Verbessere die falschen Lernziele, dann kommt der Nachtest noch einmal.',
        rueckreise: 'Unter 60 %: Rückreise zu diesem Ort. Erst üben und verbessern, dann den Nachtest wiederholen.' }[r.nachtest_ergebnis])) : null,
      ort.abgeschlossen ? el('div', { class: 'lr-stempel-gross' }, el('div', { class: 'lr-stempel', style: '--dreh:-8deg' }, el('b', {}, 'GESCHAFFT'), el('small', {}, 'Neuer Stempel')),
        el('p', {}, el('b', {}, 'Ort geschafft! Der Stempel ist jetzt in deinem Reisepass.'))) : null,
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
    el('div', { class: 'row lern-knoepfe' }, el('a', { class: 'btn primary', href: ctx.basis || `#/lerneinheit/${ctx.kind}-${ctx.einheit}` }, 'Zum Thema'),
      el('a', { class: 'btn secondary', href: `#/reise/${ctx.kind}` }, 'Zur Reise')));
}


// ---------- Eltern/Lehrer: Rückmeldungen, Themenplan, Zugänge ----------
const LERN_RM_ARTEN = [['thema_fehlt', 'Thema fehlt'], ['zu_ungenau', 'Zu ungenau'], ['mehr_aufgaben', 'Mehr Aufgaben'], ['schwieriger', 'Schwieriger'],
  ['leichter', 'Leichter'], ['erklaerung', 'Erklärung verbessern'], ['fehler', 'Fehler'], ['sonstiges', 'Sonstiges']];
const LERN_RM_STATUS = { offen: 'offen', in_arbeit: 'in Arbeit', erledigt: 'erledigt', abgelehnt: 'nicht umgesetzt' };

// Kleines Formular für Eltern/Lehrer: Anmerkung an die Entwicklung (Claude liest sie und antwortet).
function lernRueckmeldungForm(bezug, { offen = false, onGesendet } = {}) {
  let art = '';
  const chips = el('div', { class: 'lern-rm-arten', role: 'group', 'aria-label': 'Art der Anmerkung' },
    ...LERN_RM_ARTEN.map(([k, t]) => el('button', { type: 'button', class: 'lern-chip', 'aria-pressed': 'false', 'data-art': k, onclick: (ev) => {
      art = k; for (const b of chips.querySelectorAll('button')) b.setAttribute('aria-pressed', String(b === ev.currentTarget));
    } }, t)));
  const text = el('textarea', { rows: '3', maxlength: '4000', placeholder: 'Was soll anders werden? Je genauer, desto besser.', 'aria-label': 'Deine Anmerkung' });
  const status = el('p', { class: 'small muted', role: 'status' });
  const senden = el('button', { type: 'submit', class: 'primary' }, 'Senden');
  const form = el('form', { class: 'lern-rm-form' + (offen ? '' : ' lern-rm-zu') }, chips, text, el('div', { class: 'row' }, senden, status));
  form.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    if (!text.value.trim()) { status.textContent = 'Bitte kurz beschreiben.'; return; }
    senden.disabled = true; status.textContent = 'Sende …';
    try {
      await lernCall('schule_rueckmeldung_geben', { ...bezug, art: art || 'sonstiges', text: text.value.trim() });
      text.value = ''; status.textContent = 'Danke – ist bei der Entwicklung angekommen.';
      if (onGesendet) onGesendet();
    } catch (err) { status.textContent = err.message; }
    senden.disabled = false;
  });
  return form;
}

function lernAnmerkung(bezug, label) {
  const box = el('details', { class: 'lern-anmerkung' }, el('summary', {}, '✎ ' + label), lernRueckmeldungForm(bezug, { offen: true }));
  return box;
}

async function viewRueckmeldungen() {
  setChrome('Rückmeldungen', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const r = await lernCall('schule_rueckmeldungen');
  if (!live()) return;
  const liste = r.rueckmeldungen || [];
  const artText = Object.fromEntries(LERN_RM_ARTEN);
  const karte = (x) => el('article', { class: 'card lern-rm ' + 'lern-rm-' + x.status },
    el('div', { class: 'lern-einheit-kopf' }, el('b', {}, artText[x.art] || x.art), el('span', { class: 'pill' + (x.status === 'erledigt' ? ' ok' : x.status === 'offen' ? ' wartet' : '') }, LERN_RM_STATUS[x.status] || x.status)),
    el('p', { class: 'small muted' }, [x.ort, x.lernziel ? 'Etappe: ' + (x.lernziel || '') : null, x.aufgabe ? 'Aufgabe: „' + x.aufgabe + '“' : null].filter(Boolean).join(' · ') || 'Allgemein'),
    el('p', { class: 'lern-rm-text' }, x.text),
    x.antwort ? el('p', { class: 'lern-rm-antwort' }, el('b', {}, 'Antwort: '), x.antwort) : null,
    el('p', { class: 'small muted' }, `${String(x.von || '').replace(/^[a-z]+:/, '')} · ${new Date(x.am).toLocaleDateString('de-DE')}`));
  main.replaceChildren(
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'AN DIE ENTWICKLUNG'), el('h2', {}, 'Was soll besser werden?'),
      el('p', {}, 'Allgemeine Wünsche hier. Zu einer bestimmten Einheit, Erklärung oder Aufgabe geht es direkt dort über „✎ Anmerkung“ (am einfachsten über das Testkind, das alle Themen sieht).')),
    el('div', { class: 'card' }, lernRueckmeldungForm({}, { offen: true, onGesendet: () => setTimeout(render, 900) })),
    el('h3', {}, liste.length ? `Bisherige Rückmeldungen (${liste.length})` : 'Noch keine Rückmeldungen'),
    ...liste.map(karte));
}

async function viewPlan(arg) {
  setChrome('Themenplan', { back: true, showTabs: false });
  const live = viewGuard();
  const kindId = Number(arg);
  if (!kindId) { route('lernen'); return; }
  loading();
  const p = await lernCall('schule_plan_lesen', { lernender_id: kindId });
  if (!live()) return;
  $('#title').textContent = 'Themenplan ' + p.kind.name;
  const ortById = new Map((p.orte || []).map((o) => [o.block_id, o]));
  const normal = (p.plan || []).filter((r) => r.art === 'normal');
  const rueck = (p.plan || []).filter((r) => r.art === 'rueckreise');
  // Arbeitskopie: [{ block_id, kann_schon, status }]
  let plan = normal.map((r) => ({ block_id: r.block_id, kann_schon: r.kann_schon, status: r.status }));
  let geaendert = false;
  const status = el('p', { class: 'small muted', role: 'status' });
  const speichern = el('button', { type: 'button', class: 'primary', disabled: true }, 'Plan speichern');
  const liste = el('ol', { class: 'lern-plan' });
  const ortName = (o) => o ? `${o.stadt || o.titel}${o.stadt && o.titel !== o.stadt ? ' – ' + o.titel : ''}` : '?';
  const gymKl = (o) => Math.min(...(o?.themen || []).map((t) => t.jahrgang?.gym_by || 99));
  const standText = { erledigt: 'geschafft', laeuft: 'läuft', offen: 'noch nicht begonnen' };
  const themenListe = (o) => el('ul', { class: 'lern-plan-themen' }, ...(o?.themen || []).map((t) => {
    const z = lernInhaltZustand(t);
    return el('li', { class: 'lp-' + z.k },
      el('i', { class: 'lp-punkt', 'aria-hidden': 'true' }),
      el('span', {}, el('b', {}, t.titel), el('span', { class: 'lern-plan-jg' }, ' · ' + (lernJahrgangText(t.jahrgang) || 'ohne Lehrplan-Zuordnung'))),
      el('small', { class: 'muted' }, z.k === 'leer' ? 'noch kein Inhalt' : z.k === 'pruefung' ? 'Inhalt in Prüfung' : (standText[t.stand] || 'Inhalt fertig')),
      t.einheit ? el('a', { class: 'small', href: `#/inhalte/${t.einheit.id}` }, 'ansehen') : null);
  }));
  const markiere = () => { geaendert = true; speichern.disabled = false; status.textContent = 'Nicht gespeichert.'; };
  const zeichne = () => {
    liste.replaceChildren(...plan.map((x, i) => {
      const o = ortById.get(x.block_id);
      const hoch = el('button', { type: 'button', class: 'iconbtn', 'aria-label': `${ortName(o)} nach oben`, disabled: i === 0, onclick: () => { [plan[i - 1], plan[i]] = [plan[i], plan[i - 1]]; markiere(); zeichne(); } }, '↑');
      const runter = el('button', { type: 'button', class: 'iconbtn', 'aria-label': `${ortName(o)} nach unten`, disabled: i === plan.length - 1, onclick: () => { [plan[i + 1], plan[i]] = [plan[i], plan[i + 1]]; markiere(); zeichne(); } }, '↓');
      const kann = el('label', { class: 'lern-plan-kann' }, el('input', { type: 'checkbox', checked: !!x.kann_schon, onchange: (ev) => { x.kann_schon = ev.target.checked; markiere(); } }), ' kann es schon');
      const weg = el('button', { type: 'button', class: 'lern-plan-weg', 'aria-label': `${ortName(o)} aus dem Plan nehmen`, onclick: () => { plan.splice(i, 1); markiere(); zeichne(); zeichneVorrat(); } }, 'Entfernen');
      return el('li', { class: 'lern-plan-zeile' + (x.status === 'fertig' ? ' fertig' : '') },
        el('span', { class: 'lern-plan-nr' }, String(i + 1)),
        el('div', { class: 'lern-plan-text' }, el('b', {}, ortName(o)), el('small', {}, [o?.kontinent, x.status === 'fertig' ? 'geschafft' : null].filter(Boolean).join(' · ')),
          themenListe(o)),
        el('div', { class: 'lern-plan-knoepfe' }, hoch, runter, kann, weg));
    }));
    if (!plan.length) liste.append(el('li', { class: 'muted' }, 'Der Plan ist leer. Ohne Plan sieht das Kind alle Themen. Füge unten Themen hinzu.'));
  };
  const suche = el('input', { type: 'search', placeholder: 'Thema oder Ort suchen …', 'aria-label': 'Thema suchen' });
  const nurMitEinheit = el('input', { type: 'checkbox' });
  const vorrat = el('div', { class: 'lern-plan-vorrat' });
  const zeichneVorrat = () => {
    const q = suche.value.trim().toLowerCase();
    const drin = new Set(plan.map((x) => x.block_id));
    const treffer = (p.orte || []).filter((o) => !drin.has(o.block_id) && (o.themen || []).length && (!nurMitEinheit.checked || o.themen.some((t) => t.einheit))
      && (!q || `${o.stadt} ${o.titel} ${o.kontinent} ${(o.themen || []).map((t) => t.titel).join(' ')}`.toLowerCase().includes(q)));
    const gruppen = new Map();
    for (const o of treffer.sort((a, b) => gymKl(a) - gymKl(b))) { const g = gymKl(o); if (!gruppen.has(g)) gruppen.set(g, []); gruppen.get(g).push(o); }
    const kk = p.kind.klasse;
    vorrat.replaceChildren(...[...gruppen].map(([g, os]) => el('details', { open: !!q || g === kk },
      el('summary', {}, `${g === 99 ? 'Nicht im Gymnasium-Lehrplan' : `Gymnasium Klasse ${g}`}${g === kk ? ` – ${p.kind.name}s Klasse` : ''} (${os.length} ${os.length === 1 ? 'Ort' : 'Orte'})`),
      el('ul', { class: 'lern-plan-auswahl' }, ...os.map((o) => el('li', {},
        el('button', { type: 'button', class: 'lern-chip', onclick: () => { plan.push({ block_id: o.block_id, kann_schon: false, status: 'offen' }); markiere(); zeichne(); zeichneVorrat(); } }, '+ ' + ortName(o)),
        themenListe(o)))))));
    if (!treffer.length) vorrat.append(el('p', { class: 'muted small' }, 'Nichts gefunden.'));
  };
  suche.addEventListener('input', zeichneVorrat); nurMitEinheit.addEventListener('change', zeichneVorrat);
  speichern.addEventListener('click', async () => {
    speichern.disabled = true; status.textContent = 'Speichere …';
    try {
      await lernCall('schule_plan_setzen', { lernender_id: kindId, revision: p.revision, eintraege: plan.map((x) => ({ block_id: x.block_id, kann_schon: !!x.kann_schon })) });
      geaendert = false; status.textContent = 'Gespeichert.'; setTimeout(render, 700);
    } catch (err) { status.textContent = err.message; speichern.disabled = false; }
  });
  const notiz = el('textarea', { rows: '2', maxlength: '2000', placeholder: 'Notiz zum Kind (z. B. Prüfung am …, braucht mehr Zeit bei …)', 'aria-label': 'Notiz' });
  const notizStatus = el('span', { class: 'small muted', role: 'status' });
  const notizForm = el('form', { class: 'lern-rm-form' }, notiz, el('div', { class: 'row' }, el('button', { type: 'submit', class: 'secondary' }, 'Notiz speichern'), notizStatus));
  notizForm.addEventListener('submit', async (ev) => {
    ev.preventDefault(); if (!notiz.value.trim()) return;
    try { await lernCall('schule_notiz_setzen', { lernender_id: kindId, text: notiz.value.trim() }); notizStatus.textContent = 'Gespeichert.'; setTimeout(render, 700); }
    catch (err) { notizStatus.textContent = err.message; }
  });
  zeichne(); zeichneVorrat();
  const klIn = el('input', { type: 'number', min: '1', max: '13', value: p.kind.klasse || '', inputmode: 'numeric', 'aria-label': 'Klasse' });
  const kindStatus = el('span', { class: 'small muted', role: 'status' });
  const kindForm = el('form', { class: 'card lp-kindform' }, el('h3', {}, 'Klasse'), el('div', { class: 'row' }, klIn,
    el('button', { type: 'submit', class: 'secondary' }, 'Speichern'), kindStatus),
    el('p', { class: 'small muted' }, 'Gymnasium. Bestimmt, welche Themen beim Kind als „seine Klasse“ zählen.'));
  kindForm.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    try { await lernCall('schule_kind_setzen', { lernender_id: kindId, klasse: Number(klIn.value) || null }); kindStatus.textContent = 'Gespeichert.'; setTimeout(render, 700); }
    catch (err) { kindStatus.textContent = err.message; }
  });
  main.replaceChildren(...[
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, `THEMENPLAN · GYMNASIUM KLASSE ${p.kind.klasse || '?'}`), el('h2', {}, p.kind.name),
      el('p', {}, 'Reihenfolge = Reihenfolge in der Lernreise. Hinter jedem Thema steht, in welcher Klasse es laut Lehrplan dran ist (Gym = Gymnasium, RS = Realschule, IB = MYP-Jahr). Punkt: grün = Inhalt fertig, gelb = in Prüfung, grau = noch kein Inhalt.')),
    el('p', { class: 'small' }, el('a', { href: '#/lehrplan' }, 'Welche Themen gibt es für welche Klasse? → Lehrplan-Übersicht')),
    rueck.length ? el('p', { class: 'card small' }, `Automatische Rückreise: ${rueck.map((r) => ortName(ortById.get(r.block_id))).join(', ')} – wird zuerst wiederholt, bis der Nachtest bestanden ist.`) : null,
    liste,
    el('div', { class: 'row lern-plan-speichern' }, speichern, status),
    el('section', { class: 'card' }, el('h3', {}, 'Thema hinzufügen'),
      el('div', { class: 'row' }, suche, el('label', { class: 'small' }, nurMitEinheit, ' nur Orte mit Inhalt')), vorrat,
      el('details', { class: 'lern-anmerkung' }, el('summary', {}, '✎ Thema fehlt in der Liste?'), lernRueckmeldungForm({ lernender_id: kindId }, { offen: true }))),
    kindForm,
    el('section', { class: 'card' }, el('h3', {}, 'Notizen'), notizForm,
      ...(p.notizen || []).map((n) => el('p', { class: 'small' }, el('b', {}, String(n.von || '').replace(/^[a-z]+:/, '') + ': '), n.text, el('span', { class: 'muted' }, ' · ' + new Date(n.am).toLocaleDateString('de-DE'))))),
    (p.verlauf || []).length ? el('details', { class: 'card' }, el('summary', {}, 'Verlauf'),
      ...(p.verlauf || []).map((v) => el('p', { class: 'small muted' }, `${new Date(v.am).toLocaleString('de-DE')} · ${String(v.akteur).replace(/^[a-z]+:/, '')} · ${v.anlass === 'plan' ? 'Plan geändert' : v.anlass === 'rueckreise' ? 'Rückreise nach Test' : v.anlass}`))) : null].filter(Boolean));
}

async function viewZugaenge() {
  setChrome('Zugänge', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const [z, u] = await Promise.all([lernCall('schule_zugaenge'), lernCall('schule_uebersicht')]);
  if (!live()) return;
  const rollenText = { eltern: 'Eltern', lehrer: 'Lehrer', kind: 'Kind' };
  const name = el('input', { type: 'text', maxlength: '60', placeholder: 'Name, z. B. Herr Müller', 'aria-label': 'Name' });
  const rolle = el('select', { 'aria-label': 'Rolle' }, el('option', { value: 'lehrer' }, 'Lehrer – alle Themen, Plan, Rückmeldungen'),
    el('option', { value: 'eltern' }, 'Eltern – zusätzlich Belohnungen und Zugänge'), el('option', { value: 'kind' }, 'Kind – nur die eigene Lernreise'));
  const kind = el('select', { 'aria-label': 'Kind', hidden: true }, ...(u.lernende || []).filter((k) => !k.ist_test).map((k) => el('option', { value: k.id }, k.name)));
  rolle.addEventListener('change', () => { kind.hidden = rolle.value !== 'kind'; });
  const status = el('div', { role: 'status' });
  const form = el('form', { class: 'card lern-rm-form' }, el('h3', {}, 'Neuen Zugang anlegen'), name, rolle, kind, el('button', { type: 'submit', class: 'primary' }, 'Code erzeugen'), status);
  form.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    if (!name.value.trim()) { status.replaceChildren(el('p', { class: 'small' }, 'Bitte einen Namen eingeben.')); return; }
    try {
      const r = await lernCall('schule_zugang_anlegen', { name: name.value.trim(), rolle: rolle.value, lernender_id: rolle.value === 'kind' ? Number(kind.value) : null });
      const link = new URL(typeof LERN_SEITE !== 'undefined' ? './' : 'lernen/', location.href).href.replace(/#.*$/, '');
      status.replaceChildren(el('div', { class: 'lern-code-box' },
        el('p', {}, el('b', {}, 'Code (wird nur jetzt angezeigt):')), el('p', { class: 'lern-code' }, r.code),
        el('p', { class: 'small' }, 'Anmelden unter: ', el('a', { href: link, target: '_blank', rel: 'noopener' }, link)),
        el('p', { class: 'small muted' }, 'Code und Link getrennt oder persönlich weitergeben. Verloren? Zugang sperren und neu anlegen.')));
      name.value = '';
      lernZugangListe(liste, (await lernCall('schule_zugaenge')).zugaenge, rollenText);
    } catch (err) { status.replaceChildren(el('p', { class: 'err-text' }, err.message)); }
  });
  const liste = el('div');
  lernZugangListe(liste, z.zugaenge, rollenText);
  main.replaceChildren(
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'NUR BEREICH LERNEN'), el('h2', {}, 'Zugänge'),
      el('p', {}, 'Ein Lern-Code öffnet nur die Lernen-Seite. Der Server lehnt ihn für alle anderen Bereiche der App ab.')),
    form, liste);
}

function lernZugangListe(box, zugaenge, rollenText) {
  box.replaceChildren(el('h3', {}, 'Bestehende Zugänge'), ...(zugaenge.length ? zugaenge.map((g) => el('div', { class: 'card lern-zugang' + (g.aktiv ? '' : ' aus') },
    el('div', { class: 'lern-einheit-kopf' }, el('b', {}, g.name), el('span', { class: 'pill' }, rollenText[g.rolle] + (g.kind ? ' · ' + g.kind : ''))),
    el('p', { class: 'small muted' }, g.aktiv ? (g.zuletzt ? 'Zuletzt angemeldet ' + new Date(g.zuletzt).toLocaleDateString('de-DE') : 'Noch nie angemeldet') : 'Gesperrt'),
    g.aktiv ? el('button', { type: 'button', class: 'secondary', onclick: async (ev) => {
      if (!window.confirm(`Zugang „${g.name}“ sperren? Alle Geräte mit diesem Code werden abgemeldet.`)) return;
      try { await lernCall('schule_zugang_sperren', { id: g.id }); ev.target.closest('.lern-zugang').classList.add('aus'); ev.target.remove(); } catch (err) { window.alert(err.message); }
    } }, 'Sperren') : null)) : [el('p', { class: 'muted' }, 'Noch keine Zugänge.')]));
}


// ---------- Eltern/Lehrer: Lehrplan-Übersicht (alle Themen je Schulart und Klasse, mit Inhaltsstand) ----------
const LERN_STAND = { erledigt: ['geschafft', 'ok'], laeuft: ['läuft', 'laeuft'], offen: ['offen', ''], keine_einheit: ['–', 'leer'] };
function lernInhaltZustand(t) {
  const e = t.einheit;
  if (!e) return { k: 'leer', text: 'Noch kein Inhalt' };
  if (['geprueft', 'freigegeben'].includes(e.status)) return { k: 'fertig', text: `Fertig · ${e.karten} Karten · ${e.aufgaben} Aufgaben${e.neu ? ` (${e.neu} neu in Prüfung)` : ''}` };
  return { k: 'pruefung', text: `In Prüfung · ${e.karten} Karten · ${e.aufgaben} Aufgaben` };
}
let lernLpFilter = null;
async function viewLehrplan() {
  setChrome('Lehrplan', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernCall('schule_lehrplan_uebersicht');
  if (!live()) return;
  const kinder = d.kinder || [];
  const f = lernLpFilter || (lernLpFilter = { kl: '', inhalt: '', q: '' });
  const gk = (t) => t.jahrgang?.gym_by || 99; // Gruppe: Klasse im Gymnasium (alle Kinder sind am Gymnasium)
  const kacheln = el('div', { class: 'lp-kacheln' });
  const liste = el('div', { class: 'lp-liste' });
  const klSel = el('select', { 'aria-label': 'Klasse' });
  const klName = (k) => k === 99 ? 'Nicht im Gymnasium-Lehrplan' : `Klasse ${k}` + kinder.filter((c) => c.klasse === k).map((c) => ' · ' + c.name).join('');
  const fuelleKlassen = () => {
    const ks = [...new Set((d.themen || []).map(gk))].sort((a, b) => a - b);
    klSel.replaceChildren(el('option', { value: '' }, 'Alle Klassen'), ...ks.map((k) => el('option', { value: k, selected: String(k) === String(f.kl) }, klName(k))));
  };
  klSel.addEventListener('change', () => { f.kl = klSel.value; zeichne(); });
  const inhSel = el('select', { 'aria-label': 'Inhalt' }, ...[['', 'Alle Themen'], ['fertig', 'Fertig'], ['pruefung', 'In Prüfung'], ['leer', 'Noch kein Inhalt']]
    .map(([v, t]) => el('option', { value: v, selected: f.inhalt === v }, t)));
  inhSel.addEventListener('change', () => { f.inhalt = inhSel.value; zeichne(); });
  const suche = el('input', { type: 'search', placeholder: 'Thema suchen …', 'aria-label': 'Thema suchen', value: f.q });
  suche.addEventListener('input', () => { f.q = suche.value; zeichne(); });
  const status = el('p', { class: 'small muted', role: 'status' });
  const bauen = async (t, knopf) => {
    knopf.disabled = true;
    try {
      await lernCall('schule_rueckmeldung_geben', { art: 'thema_fehlt', block_id: t.block_id,
        text: `Bitte Inhalte bauen: „${t.titel}“ (${t.ort || t.gebiet}, ${lernJahrgangText(t.jahrgang)}).` });
      knopf.textContent = 'Angefragt ✓'; status.textContent = 'Anfrage ist bei der Entwicklung angekommen.';
    } catch (err) { status.textContent = err.message; knopf.disabled = false; }
  };
  const zeile = (t) => {
    const z = lernInhaltZustand(t);
    const stand = kinder.map((c) => {
      const s = t.stand?.[c.id] || 'keine_einheit'; const [txt, kl] = LERN_STAND[s] || [s, ''];
      const geplant = (t.geplant || []).includes(c.id);
      return el('span', { class: 'lp-stand ' + kl }, `${c.name}: ${txt}${geplant ? ' · im Plan' : ''}`);
    });
    return el('article', { class: 'lp-zeile lp-' + z.k },
      el('div', { class: 'lp-text' }, el('b', {}, t.titel),
        el('span', { class: 'lern-plan-jg' }, lernJahrgangText(t.jahrgang) || 'ohne Lehrplan-Zuordnung'),
        t.beschreibung ? el('small', {}, t.beschreibung) : null,
        (t.gliederung || []).length ? el('ol', { class: 'lp-gliederung' }, ...t.gliederung.map((x) => el('li', {}, x))) : null,
        t.ort ? el('small', { class: 'muted' }, 'Ort der Lernreise: ' + t.ort) : null,
        el('span', { class: 'lp-inhalt' }, el('i', { class: 'lp-punkt', 'aria-hidden': 'true' }), z.text),
        el('div', { class: 'lp-staende' }, ...stand),
        t.rueckmeldungen ? el('small', { class: 'muted' }, `${t.rueckmeldungen} offene Anmerkung${t.rueckmeldungen > 1 ? 'en' : ''}`) : null),
      el('div', { class: 'lp-aktionen' },
        t.einheit ? el('a', { class: 'btn secondary', href: `#/inhalte/${t.einheit.id}` }, 'Inhalte ansehen')
          : el('button', { type: 'button', class: 'secondary', onclick: (ev) => bauen(t, ev.currentTarget) }, 'Bauen lassen')));
  };
  const zeichne = () => {
    const q = f.q.trim().toLowerCase();
    const basis = (d.themen || []).filter((t) => !f.kl || String(gk(t)) === String(f.kl));
    const zahl = (k) => basis.filter((t) => lernInhaltZustand(t).k === k).length;
    kacheln.replaceChildren(
      el('div', { class: 'lp-kachel' }, el('b', {}, String(basis.length)), el('small', {}, 'Themen')),
      el('div', { class: 'lp-kachel lp-fertig' }, el('b', {}, String(zahl('fertig'))), el('small', {}, 'fertig')),
      el('div', { class: 'lp-kachel lp-pruefung' }, el('b', {}, String(zahl('pruefung'))), el('small', {}, 'in Prüfung')),
      el('div', { class: 'lp-kachel lp-leer' }, el('b', {}, String(zahl('leer'))), el('small', {}, 'ohne Inhalt')));
    const treffer = basis.filter((t) => (!f.inhalt || lernInhaltZustand(t).k === f.inhalt)
      && (!q || `${t.titel} ${t.ort} ${t.gebiet}`.toLowerCase().includes(q)));
    const gruppen = new Map();
    for (const t of treffer.sort((a, b) => gk(a) - gk(b))) {
      const g = gk(t); if (!gruppen.has(g)) gruppen.set(g, []); gruppen.get(g).push(t);
    }
    liste.replaceChildren(...[...gruppen].map(([kl, ts]) => el('section', { class: 'lp-gruppe' },
      el('h3', {}, klName(kl), el('small', { class: 'muted' }, ` · ${ts.length} ${ts.length === 1 ? 'Thema' : 'Themen'}`)),
      ...[...ts.reduce((m, t) => m.set(t.gebiet || 'Weitere', [...(m.get(t.gebiet || 'Weitere') || []), t]), new Map())].flatMap(([g, gs]) => [
        el('h4', { class: 'lp-gebiet' }, g, el('small', { class: 'muted' }, ` · ${gs.filter((t) => lernInhaltZustand(t).k === 'fertig').length} von ${gs.length} mit Inhalt`)),
        ...gs.map(zeile)]))));
    if (!treffer.length) liste.append(el('p', { class: 'muted' }, 'Keine Themen für diese Auswahl.'));
  };
  fuelleKlassen(); zeichne();
  main.replaceChildren(
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'ELTERN UND LEHRER'), el('h2', {}, 'Lehrplan-Übersicht'),
      el('p', {}, 'Alle Mathe-Themen, sortiert nach Klasse im Gymnasium. Hinter jedem Thema steht, wann es laut Lehrplan dran ist: Gym = Gymnasium, RS = Realschule, IB = MYP-Jahr. Grün = Inhalt fertig, gelb = gebaut und in Prüfung, grau = noch nichts da.')),
    el('div', { class: 'card lp-filter' }, el('div', { class: 'row' }, klSel, inhSel, suche)),
    kacheln, status, liste);
}

// ---------- Eltern/Lehrer: Inhalte einer Einheit prüfen (Erklärungen, Fehler, alle Aufgaben mit Lösung) ----------
async function viewInhalte(arg) {
  setChrome('Inhalte', { back: true, showTabs: false });
  const live = viewGuard();
  const id = Number(arg);
  if (!id) { route('lehrplan'); return; }
  loading();
  const d = await lernCall('schule_inhalt_lesen', { einheit_id: id });
  if (!live()) return;
  const titel = d.thema?.titel || d.inhalt?.ziel || 'Einheit';
  $('#title').textContent = titel;
  const aufgaben = d.aufgaben || [];
  const etappen = lernEtappen({ inhalt: d.inhalt, uebungen: aufgaben.filter((a) => a.pool === 'uebung') });
  lernTitel = new Map(etappen.map((e) => [e.lernziel, e.titel]));
  const rmJe = (lz) => (d.rueckmeldungen || []).filter((r) => r.lernziel === lz);
  const stufeText = (a) => a.pool === 'uebung' ? (['', 'leicht', 'mittel', 'schwer'][a.stufe] || '–') : a.pool === 'test' ? 'Test' : a.pool === 'nachtest' ? 'Nachtest' : a.pool;
  const tabelle = (as) => el('div', { class: 'lp-tabelle-rahmen' }, el('table', { class: 'lp-tabelle' },
    el('thead', {}, el('tr', {}, el('th', {}, 'Stufe'), el('th', {}, 'Aufgabe'), el('th', {}, 'Lösung'), el('th', {}, 'Lösungsweg'), el('th', {}, 'Status'))),
    el('tbody', {}, ...as.map((a) => el('tr', {},
      el('td', {}, stufeText(a)),
      el('td', {}, lernText(a.frage?.text || a.frage?.schablone || ''), a.antworttyp === 'auswahl' ? el('small', { class: 'muted' }, ' (' + (a.antworten || []).join(' | ') + ')') : null),
      el('td', { class: 'lp-loesung' }, lernLoesungText(a)),
      el('td', { class: 'muted' }, lernText(a.loesungsweg || '')),
      el('td', {}, a.freigegeben ? el('span', { class: 'lp-ok' }, 'frei') : el('span', { class: 'lp-warte' }, 'in Prüfung')))))));
  const karten = etappen.map((e) => {
    const as = aufgaben.filter((a) => a.lernziel === e.lernziel);
    const rm = rmJe(e.lernziel);
    return el('details', { class: 'card lp-karte', id: 'k' + e.nr },
      el('summary', {}, el('b', {}, `${e.nr} · ${e.titel}`), el('small', { class: 'muted' }, ` · ${as.length} ${as.length === 1 ? 'Aufgabe' : 'Aufgaben'}${as.some((a) => !a.freigegeben) ? ` (${as.filter((a) => !a.freigegeben).length} in Prüfung)` : ''}${rm.length ? ` · ${rm.length} ${rm.length === 1 ? 'Anmerkung' : 'Anmerkungen'}` : ''}`)),
      el('div', { class: 'lp-karte-innen' },
        el('div', { class: 'lp-erkl' }, el('p', { class: 'eyebrow' }, 'ERKLÄRUNG, WIE DAS KIND SIE SIEHT'), e.regel ? lernErklaerung(e) : el('p', { class: 'muted' }, 'Keine Erklärung hinterlegt.')),
        lernAnmerkung({ einheit_id: id, lernziel: e.lernziel }, 'Anmerkung zu dieser Karte'),
        ...rm.map((r) => el('p', { class: 'small' }, el('b', {}, (LERN_RM_STATUS[r.status] || r.status) + ': '), r.text, r.antwort ? el('span', { class: 'muted' }, ' → ' + r.antwort) : null)),
        as.length ? tabelle(as) : el('p', { class: 'muted small' }, 'Keine Aufgaben.')));
  });
  const ohneKarte = aufgaben.filter((a) => !etappen.some((e) => e.lernziel === a.lernziel));
  const zahl = (fn) => aufgaben.filter(fn).length;
  main.replaceChildren(...[
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, [d.ort?.stadt, lernJahrgangText(d.thema?.jahrgang)].filter(Boolean).join(' · ').toUpperCase() || 'INHALTE'),
      el('h2', {}, titel),
      el('p', {}, `${['geprueft', 'freigegeben'].includes(d.status) ? 'Fertig' : 'In Prüfung'} · ${etappen.length} Lernkarten · ${zahl((a) => a.pool === 'uebung')} Übungen · ${zahl((a) => a.pool !== 'uebung')} Test- und Nachtestaufgaben`
        + (zahl((a) => !a.freigegeben) ? ` · ${zahl((a) => !a.freigegeben)} noch in Prüfung (nur für das Testkind sichtbar)` : '')),
      d.inhalt?.ziel ? el('p', { class: 'small muted' }, 'Ziel: ' + d.inhalt.ziel) : null),
    el('nav', { class: 'lp-sprung', 'aria-label': 'Lernkarten' }, ...etappen.map((e) => el('a', { href: '#', class: 'lern-chip', onclick: (ev) => {
      ev.preventDefault(); const k = document.getElementById('k' + e.nr); k.open = true; k.scrollIntoView({ block: 'start' });
    } }, `${e.nr} · ${e.titel}`))),
    lernAnmerkung({ einheit_id: id }, 'Anmerkung zum ganzen Thema'),
    ...karten,
    ohneKarte.length ? el('details', { class: 'card lp-karte' }, el('summary', {}, el('b', {}, `Test- und Nachtestaufgaben ohne Karte (${ohneKarte.length})`)), tabelle(ohneKarte)) : null].filter(Boolean));
}

// ---------- Wiederholen: fällige Lernkarten, je eine Aufgabe ----------
async function viewWiederholen(arg) {
  setChrome('Wiederholen', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const r = await lernCall('schule_wiederholung', { lernender_id: d.kind.id, anzahl: 3 });
  if (!live()) return;
  const { kind } = d; const liste = r.aufgaben || [];
  const flaeche = el('div', { class: 'lr-etappe-flaeche' });
  let i = 0, richtig = 0;
  const zeige = () => {
    const a = liste[i];
    if (!a) {
      flaeche.replaceChildren(el('section', { class: 'lr-geschafft' }, el('div', { class: 'lr-geschafft-haken' }, lernIcon(LI.haken, 64)),
        el('p', { class: 'lr-ueber' }, 'WIEDERHOLT'), el('h1', { class: 'lr-titel' }, `${richtig} von ${liste.length} richtig`),
        el('p', { class: 'lr-leise' }, richtig === liste.length ? 'Super – das sitzt noch.' : 'Was nicht geklappt hat, kommt bald nochmal dran. Die Erklärung findest du im Merkheft.')),
        el('a', { class: 'lr-knopf', href: `#/reise/${kind.id}` }, 'Weiter zu Heute'));
      return;
    }
    const auf = lernAufgabe(a); const cid = lernCid();
    const meldung = el('div', { role: 'status', 'aria-live': 'polite' });
    const pruefen = el('button', { type: 'button', class: 'lr-knopf' }, 'Prüfen');
    pruefen.addEventListener('click', async () => {
      const w = auf.antwort();
      if (!w) { meldung.replaceChildren(el('p', { class: 'lr-hinweis' }, auf.fehlerText() || 'Bitte erst antworten.')); return; }
      pruefen.disabled = true;
      try {
        const x = await lernCall('schule_uebung_pruefen', { lernender_id: kind.id, aufgabe_id: a.id, antwort: w, client_id: cid, hilfe: 0 });
        if (!x.format_ok) { meldung.replaceChildren(el('p', { class: 'lr-hinweis' }, x.hinweis)); pruefen.disabled = false; return; }
        auf.sperren(); a.loesung = x.loesung; if (x.richtig) richtig++;
        meldung.replaceChildren(x.richtig ? el('div', { class: 'lr-rueck lr-rueck-ok' }, el('b', {}, 'Richtig!'))
          : el('div', { class: 'lr-rueck lr-rueck-falsch' }, el('b', {}, 'Noch nicht. Richtig ist: ' + lernLoesungText(a)), x.loesungsweg ? el('p', {}, lernText(x.loesungsweg)) : null,
            el('a', { href: `#/lerneinheit/${kind.id}-${a.einheit_id}` }, 'Zur Lernkarte')));
        i++; pruefen.replaceWith(el('button', { type: 'button', class: 'lr-knopf', onclick: zeige }, i < liste.length ? 'Nächste' : 'Fertig'));
      } catch (err) { meldung.replaceChildren(el('p', { class: 'err-text' }, err.message)); pruefen.disabled = false; }
    });
    flaeche.replaceChildren(el('header', { class: 'lr-etappe-oben' }, el('p', { class: 'lr-ueber' }, `WIEDERHOLEN ${i + 1} VON ${liste.length} · ${(a.stadt || '').toUpperCase()}`),
      el('h1', { class: 'lr-titel' }, a.etappe || 'Aufgabe')),
      el('section', { class: 'lr-karte-box lr-aufgabe' }, auf.node), meldung, pruefen);
    window.scrollTo(0, 0);
  };
  if (!liste.length) flaeche.replaceChildren(el('p', { class: 'lr-leise' }, 'Gerade ist nichts zum Wiederholen dran.'), el('a', { class: 'lr-knopf', href: `#/reise/${kind.id}` }, 'Zu Heute'));
  else zeige();
  main.replaceChildren(lernRahmen(kind, 'reise', flaeche));
}
