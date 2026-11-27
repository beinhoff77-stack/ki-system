/* Klickmuster „Was wackelt?“ – zeigt, wie die Seite aussehen und sich anfühlen soll.
   Kein App-Code: kein Netz, kein Speichern. Die Knöpfe ändern nur, was auf dem Bildschirm steht. */
'use strict';

const el = (tag, attrs = {}, ...kids) => {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === 'class') n.className = v;
    else if (k.startsWith('on')) n.addEventListener(k.slice(2), v);
    else if (v !== null && v !== undefined && v !== false) n.setAttribute(k, v === true ? '' : v);
  }
  for (const k of kids.flat()) if (k !== null && k !== undefined && k !== false) n.append(k.nodeType ? k : document.createTextNode(String(k)));
  return n;
};
const leer = (n) => { while (n.firstChild) n.removeChild(n.firstChild); return n; };

const P = new URLSearchParams(location.search);
if (P.get('g') === 'nacht') document.body.classList.add('nacht');

// ?s=leer zeigt die Seite an einem guten Tag: nichts zu besprechen.
let themen = P.get('s') === 'leer'
  ? THEMEN.filter((t) => t.status === 'besprochen').map((t) => ({ ...t }))
  : THEMEN.map((t) => ({ ...t }));
const mehrOffen = new Set();   // Themen, bei denen alle falschen Aufgaben gezeigt werden
const GRUPPEN = [['zu_besprechen', 'Zu besprechen'], ['beobachten', 'Beobachten'], ['besprochen', 'Besprochen']];
const MAX_AUFGABEN = 3;

// ---------- Kopf: die Lage ----------
function zeichneLage() {
  const l = lage(themen);
  const satz = l.themen === 0
    ? el('p', { class: 'lage-satz' }, el('b', {}, 'Nichts zu besprechen.'), ' Seit dem letzten Blick ist keine Antwort falsch gewesen.')
    : el('p', { class: 'lage-satz' },
        l.themen === 1 ? el('span', {}, el('b', {}, 'Ein'), ' Thema wackelt') : el('span', {}, el('b', {}, l.themen), ' Themen wackeln'),
        ' – zusammen ', el('b', {}, l.falsch), ' falsche Antworten',
        l.tage ? `, die älteste vor ${l.tage} Tagen.` : '.',
        l.muster ? el('span', {}, ' Am häufigsten: ', el('b', {}, l.muster.wort), ` (${l.muster.n}×).`) : null);

  const zahlen = el('div', { class: 'lage-zahlen' },
    el('div', { class: 'lage-zahl' }, el('i', {}, WOCHE.aufgaben), el('small', {}, 'Bordkarten diese Woche')),
    el('div', { class: 'lage-zahl' }, el('i', {}, `${Math.round(WOCHE.richtig / WOCHE.aufgaben * 100)} %`), el('small', {}, 'davon richtig')),
    el('div', { class: 'lage-zahl' }, el('i', {}, WOCHE.mit_tipp), el('small', {}, 'mal mit Tipp')),
    el('div', { class: 'lage-zahl' }, el('i', {}, WOCHE.lerntage), el('small', {}, WOCHE.lerntage === 1 ? 'Lerntag' : 'Lerntage')));

  return el('section', { class: 'lage' },
    el('div', { class: 'lage-kopf' }, el('h1', {}, 'Was wackelt?'), el('span', { class: 'lage-stand' }, 'Stand: heute, 9:00')),
    satz, zahlen,
    l.quer ? el('p', { class: 'lage-quer' }, '↗ Dasselbe Muster taucht in mehreren Themen auf. Ein Gespräch darüber hilft allen drei Themen auf einmal.') : null);
}

// ---------- Eine Themenkarte ----------
function karte(t, rang) {
  const falsch = t.etappen.reduce((s, e) => s + e.falsch, 0);
  const richtig = t.etappen.reduce((s, e) => s + e.richtig, 0);
  const b = befundSatz(t);
  const d = dringlichkeit(t);
  const kl = t.status === 'zu_besprechen' ? 'dringend' : t.status;
  const alleFehler = t.etappen.flatMap((e) => (e.fehler || []).map((f) => ({ ...f, etappe: e })))
    .sort((x, y) => String(y.am).localeCompare(String(x.am)));
  const zeigeAlle = mehrOffen.has(t.thema_id);
  const sichtbar = zeigeAlle ? alleFehler : alleFehler.slice(0, MAX_AUFGABEN);

  // Die Etappe steht nur dabei, wenn das Thema mehrere hat – sonst wiederholt sie nur die Zeile oben.
  const mehrereEtappen = t.etappen.length > 1;
  const aufgabe = (f) => el('div', { class: 'auf' },
    mehrereEtappen ? el('div', { class: 'auf-etappe' }, f.etappe.titel) : null,
    el('div', { class: 'auf-frage' }, f.frage),
    el('div', { class: 'auf-zeile' },
      el('span', { class: 'auf-falsch' }, el('small', {}, 'geantwortet'), el('b', {}, f.antwort)),
      el('span', { class: 'auf-richtig' }, el('small', {}, 'richtig'), el('b', {}, f.loesung))),
    el('div', { class: 'auf-wann' }, wann(f.am)));

  const tun = [];
  if (t.status !== 'besprochen') tun.push(el('button', { class: 'knopf knopf-haupt', onclick: () => setzen(t, 'besprochen') }, '✓ Besprochen'));
  if (t.status === 'zu_besprechen') tun.push(el('button', { class: 'knopf', onclick: () => setzen(t, 'beobachten') }, 'Nur beobachten'));
  if (t.status === 'beobachten') tun.push(el('button', { class: 'knopf', onclick: () => setzen(t, 'zu_besprechen') }, 'Doch besprechen'));
  if (t.status === 'besprochen') tun.push(el('button', { class: 'knopf', onclick: () => setzen(t, 'zu_besprechen') }, 'Wieder aufnehmen'));
  tun.push(el('button', { class: 'knopf knopf-link', onclick: () => {} }, 'Erklärung ansehen ›'));
  tun.push(el('button', { class: 'knopf knopf-link', onclick: () => {} }, 'Im Lehrplan ›'));
  if (t.status === 'besprochen' && t.besprochen_am) tun.push(el('span', { class: 'wann' }, 'besprochen ' + wann(t.besprochen_am)));

  return el('article', { class: 'thema ' + kl },
    el('div', { class: 't-kopf' },
      el('div', { class: 't-rang' }, rang),
      el('div', { class: 't-titel' },
        el('h3', {}, t.titel),
        el('div', { class: 't-ort' }, t.ort + ' · ' + t.etappen.map((e) => e.titel).join(' · ')),
        el('div', { class: 't-warum' }, t.status === 'besprochen' ? 'Seitdem keine neuen Fehler.' : d.grund),
        el('div', { class: 't-marken' },
          t.wieder_offen ? el('span', { class: 'marke marke-w' }, 'wieder offen') : null,
          t.fehler_neu > 0 && t.status !== 'besprochen' ? el('span', { class: 'marke marke-n' }, `${t.fehler_neu} neu seit dem letzten Blick`) : null,
          t.status === 'besprochen' ? el('span', { class: 'marke marke-b' }, 'besprochen') : null))),
    el('div', { class: 't-balken' },
      el('div', { class: 'balken' },
        el('i', { class: 'r', style: `width:${richtig / (richtig + falsch) * 100}%` }),
        el('i', { class: 'f', style: `width:${falsch / (richtig + falsch) * 100}%` })),
      el('small', {}, `${richtig} richtig · ${falsch} falsch · zuletzt ${wann(t.letzter_fehler_am)}`)),
    el('div', { class: 't-inhalt' },
      el('div', { class: 'befund' },
        el('div', { class: 'befund-kopf' }, el('b', {}, 'Das Muster'), b.kurz ? el('span', { class: 'befund-art' }, b.kurz) : null),
        el('p', {}, b.satz),
        hauptEtappe(t).regel ? el('p', { class: 'regel' }, el('b', {}, 'Kurz gesagt: '), hauptEtappe(t).regel) : null),
      el('div', { class: 'aufgaben' },
        // Ehrlich bleiben: Gespeichert sind nur die letzten falschen Antworten, nicht alle. Die Zahl sagt beides.
        el('b', { class: 'kopf' }, alleFehler.length < falsch
          ? `Die letzten falschen Antworten (${alleFehler.length} von ${falsch})`
          : `Diese Aufgaben waren falsch (${alleFehler.length})`),
        el('div', { class: 'auf-liste' }, ...sichtbar.map(aufgabe)),
        alleFehler.length > MAX_AUFGABEN
          ? el('button', { class: 'auf-mehr', onclick: () => { if (zeigeAlle) mehrOffen.delete(t.thema_id); else mehrOffen.add(t.thema_id); zeichne(); } },
              zeigeAlle ? '▴ Weniger zeigen' : `▾ Alle ${alleFehler.length} gespeicherten Antworten zeigen`)
          : null)),
    el('div', { class: 't-tun' }, ...tun));
}

// ---------- Umschalten (im Klickmuster nur auf dem Bildschirm) ----------
function setzen(t, status) {
  themen = themen.map((x) => (x.thema_id === t.thema_id
    ? { ...x, status, besprochen_am: status === 'besprochen' ? new Date('2026-11-27T09:00:00+01:00').toISOString() : null, fehler_neu: status === 'zu_besprechen' ? x.fehler_neu : 0 }
    : x));
  zeichne();
}

// ---------- Die ganze Seite ----------
function zeichne() {
  const main = document.getElementById('seite');
  const gruppen = GRUPPEN.map(([st, titel]) => {
    const l = themen.filter((t) => t.status === st)
      .map((t) => ({ t, d: dringlichkeit(t) }))
      .sort((a, b) => b.d.punkte - a.d.punkte);
    return el('section', { class: 'gruppe' },
      el('div', { class: 'gruppe-kopf' }, el('h2', {}, titel), el('i', {}, l.length)),
      l.length ? el('div', {}, ...l.map(({ t }, i) => karte(t, st === 'zu_besprechen' ? i + 1 : '·')))
        : el('p', { class: 'gruppe-leer' }, st === 'zu_besprechen' ? 'Nichts zu besprechen.' : st === 'beobachten' ? 'Nichts im Auge zu behalten.' : 'Noch nichts besprochen.'));
  });

  leer(main).append(
    el('p', { class: 'erfunden' }, 'Entwurf des Designers. Alle Zahlen, Aufgaben und Antworten auf dieser Seite sind erfunden – es ist kein echter Lernstand.'),
    zeichneLage(), ...gruppen,
    el('details', { class: 'rest' },
      el('summary', {}, `Alle Etappen mit Stand (${ETAPPEN_GESAMT})`),
      el('div', { class: 'rest-inhalt' },
        el('p', {}, 'Hier steht wie bisher die vollständige Liste: jede Etappe mit richtig/falsch, „sitzt“, „sicher“ und dem letzten Übungstag. Sie bleibt zugeklappt, weil sie zum Nachschlagen da ist, nicht zum Besprechen.'))),
    el('p', { class: 'fuss' }, 'Neue falsche Antworten holen ein Thema von selbst zurück nach „Zu besprechen“. „Besprochen ✓“ nimmt es heraus, bis wieder etwas falsch ist.'));
}

zeichne();
