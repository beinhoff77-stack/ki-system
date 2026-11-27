#!/usr/bin/env node
// RU-App (0.95.0): baut die Daten des Regel-Universums für die App (daten/regeln-universum.json) aus den Quellen.
//   node tools/regeln_bauen.cjs            schreibt die Datei, endet mit „OK“
//   node tools/regeln_bauen.cjs --pruefen  schreibt nichts, prüft nur, ob die abgelegte Datei zum Bau passt (sonst Fehler)
// Quellen (nur gelesen):
//   inhalte/design/gesetzbuch/entwurf/teile/inhalt.json   Mathe-Inhalt (Regeln, Ideen, Leitern, Gesetze, Arbeitsweisen)
//   inhalte/design/gesetzbuch/entwurf/teile/ideen.js, zeichnen*.js   Zeichnungen des Entwurfs (hier einmal gezeichnet, in der App nur noch SVG-Text)
//   inhalte/design/gesetzbuch/entwurf7/teile/kurz.json   Kurzbeschreibungen (Designer)
//   inhalte/mathe-profi/regeln-uebersicht/texte8/*.json  Berichtigungen und Ergänzungen des Mathe-Profis (README dort, Punkte 1–6)
//   inhalte/mathe-profi/regeln-uebersicht/kennungen.json, inhalte/mathe-profi/schritt1/*, inhalte/themen/*.json   Lehrer-Blatt
// Entscheidungen des Projektleiters (27.11.): Regel 10 bekommt die kürzere Merksatz-Fassung; Regel 6 und 7 (1112): Merksatz = Kurzbeschreibung (inhalt.json).
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');

const repo = path.resolve(__dirname, '..');
const lies = (...p) => fs.readFileSync(path.join(repo, ...p), 'utf8');
const json = (...p) => JSON.parse(lies(...p));
const ZIEL = path.join(repo, 'daten', 'regeln-universum.json');
const ALT = ['inhalte', 'design', 'gesetzbuch', 'entwurf', 'teile'];
const T8 = ['inhalte', 'mathe-profi', 'regeln-uebersicht', 'texte8'];

function bauen() {
  const inhalt = json(...ALT, 'inhalt.json');
  const kurzAlt = json('inhalte', 'design', 'gesetzbuch', 'entwurf7', 'teile', 'kurz.json').texte;
  const kurzT8 = json(...T8, 'kurzbeschreibungen.json').eintraege;
  const merkT8 = json(...T8, 'merksaetze.json').regeln;
  const weisenT8 = json(...T8, 'arbeitsweisen.json').arbeitsweisen;
  const einzelT8 = json(...T8, 'einzelregeln.json');
  const lehrplanT8 = json(...T8, 'lehrplan.json').regeln;
  const aufgT8 = json(...T8, 'beispielaufgaben.json');

  // ---------- Zeichnungen des Entwurfs einmal ausführen (ohne Browser: sie bauen nur SVG-Text) ----------
  const ctx = vm.createContext({});
  vm.runInContext(['ideen.js', 'zeichnen.js', 'zeichnen2.js', 'zeichnen3.js'].map((f) => lies(...ALT, f)).join('\n;\n') +
    '\n;globalThis.__z = { KUERZEL, PLANET_BILD, ZEICHNUNGEN };', ctx);
  const { KUERZEL, PLANET_BILD, ZEICHNUNGEN } = ctx.__z;

  // ---------- Texte, achte Runde ----------
  const kurz = Object.fromEntries(Object.entries(kurzAlt).map(([k, v]) => [k, v.text]));
  for (const e of kurzT8) kurz[e.entwurf_schluessel] = e.endfassung; // nur die Endfassungen aus texte8 (berichtigte und unveränderte)
  assert.equal(kurzT8.length, 42); assert.deepEqual(Object.keys(kurz).sort(), kurzT8.map((e) => e.entwurf_schluessel).sort(), 'jede Kurzbeschreibung kommt aus texte8');
  // Klassenbeispiele kommen aus EINER Quelle: inhalt.leitern (= klassenleiter.json). regeln[].klassen wird nicht in die App-Daten übernommen.
  const regeln = inhalt.regeln.map((r) => { const { klassen, ...rest } = r; return rest; });
  const regel = Object.fromEntries(regeln.map((r) => [r.id, r]));
  const anhaengen = (x, feld, text) => { const alt = (x[feld] || '').trim();
    x[feld] = !alt ? text : feld === 'fehler' ? `${alt} Und: ${text.charAt(0).toLowerCase()}${text.slice(1)}` : `${alt} ${text}`; };
  let luecken = 0;
  for (const m of merkT8) { const r = regel[m.entwurf_schluessel]; assert.ok(r, m.entwurf_schluessel);
    for (const l of m.luecken) { assert.ok(['genau', 'voraus', 'fehler'].includes(l.wo), l.wo); anhaengen(r, l.wo, l.text); luecken++; } }
  const r10 = merkT8.find((m) => m.entwurf_schluessel === 'R10');
  regel.R10.satz = r10.kurzfassung.haupt; // Entscheidung Projektleiter: kürzere Fassung
  const arbeitsweisen = inhalt.arbeitsweisen.map((a, i) => { const w = weisenT8[i]; assert.equal(w.name, a.name);
    return { name: a.name, satz: a.satz, kurz: w.kurz, beispiel: { klasse: w.beispiel.klasse, text: w.beispiel.text }, erklaerung: w.erklaerung }; });
  const gesetze = inhalt.gesetze.map((g) => ({ ...g }));
  const gesetz = Object.fromEntries(gesetze.map((g) => [g.id, g]));
  const einzel = [...einzelT8.klasse5, ...einzelT8.klasse8];
  for (const e of einzel) { const g = gesetz[e.id]; assert.ok(g, e.id);
    g.beispiel = e.beispiel.text;
    if (e.grenze.art === 'gilt nicht') anhaengen(g, 'voraus', e.grenze.text); else anhaengen(g, 'fehler', e.grenze.text);
    g.ausgearbeitet = 8; }

  // ---------- Planeten und Ideen (nur, was die App zeigt) ----------
  const planeten = inhalt.planeten.filter((p) => PLANET_BILD[p.name]).map((p) => ({ name: p.name, kuerzel: KUERZEL[p.name], farbe: PLANET_BILD[p.name].farbe, zeichen: PLANET_BILD[p.name].zeichen,
    ideen: p.ideen.map((i) => ({ id: `I-${KUERZEL[p.name]}-${i.nr}`, nr: i.nr, kurz: i.kurz, satz: i.satz, genau: i.genau, warum: i.warum, voraus: i.voraus, fehler: i.fehler, verwandt: i.verwandt, gesetze: i.gesetze })) }));

  // ---------- Zeichnungen: Felder als fertiger SVG-Text ----------
  const zeichnungen = {};
  for (const id of Object.keys(ZEICHNUNGEN).sort()) {
    const z = ZEICHNUNGEN[id](); zeichnungen[id] = z.felder.map((f) => Object.fromEntries(['neu', 'pfeil', 'kopf', 'svg', 'gl', 'satz'].filter((k) => f[k]).map((k) => [k, f[k]])));
  }

  // ---------- Lehrer-Blatt ----------
  const mp = ['inhalte', 'mathe-profi'];
  const ken = Object.fromEntries(json(...mp, 'regeln-uebersicht', 'kennungen.json').kennungen.map((k) => [k.kennung, k]));
  const etik = json(...mp, 'schritt1', 'etiketten.json').aufgaben;
  const zuord = Object.fromEntries(json(...mp, 'schritt1', 'kennungen-zuordnung.json').aufgaben.map((a) => [a.kennung_aufgabe, a.regel]));
  Object.assign(zuord, aufgT8.umhaengen.regel_von_aufgabe); // Korrekturen des Mathe-Profis (Gegenprüfung): texte8/beispielaufgaben.json
  const stich = Object.fromEntries(aufgT8.stichprobe_bestehende_zuordnung.ergebnis.map((s) => [s.regel, s]));
  const themenIds = {};
  for (const f of fs.readdirSync(path.join(repo, 'inhalte', 'themen')).filter((f) => f.endsWith('.json')).sort()) {
    try { const d = json('inhalte', 'themen', f); if (d.thema_schluessel && d.thema_id) themenIds[d.thema_schluessel] = d.thema_id; } catch { /* keine Themen-Datei */ }
  }
  const loesungVon = (a) => { const o = a.o || {}; return 'werte' in o ? o.werte.join(', ') : 'wert' in o ? String(o.wert) : 'index' in o && a.a ? a.a[o.index] : ''; };
  const vorn = aufgT8.umhaengen.text_voranstellen || {}; // Ausschlüsse der Definitionsmenge stehen vor der Aufgabe (Gegenprüfung 1090)
  const aufgabe = (a, kopf, kennung) => ({ kopf, text: (vorn[kennung] || '') + a.f.text, auswahl: a.a || null, loesung: loesungVon(a), weg: a.w || '' });
  const dateien = {};
  const lehrer = {};
  for (const r of regeln) {
    const L = inhalt.leitern[r.id], k = ken[L.kennung] || {}, s = stich[L.kennung];
    const aufgaben = [];
    for (const e of etik) { // Reihenfolge in etiketten.json = Reihenfolge in <thema>.neu.json (wie entwurf7/bauen.py)
      if (zuord[e.kennung] !== L.kennung || aufgaben.length >= 3) continue;
      if (s && s.befund === 'passt nicht') continue; // Stichprobe des Mathe-Profis: Zuordnung falsch → nicht als Beispiel zeigen
      if (!(e.thema in dateien)) { const p = path.join(repo, ...mp, 'schritt1', e.thema + '.neu.json'); dateien[e.thema] = fs.existsSync(p) ? JSON.parse(fs.readFileSync(p, 'utf8')) : []; }
      const liste = etik.filter((x) => x.thema === e.thema), a = dateien[e.thema][liste.indexOf(e)];
      if (a) aufgaben.push(aufgabe(a, `${e.kennung} · Klasse ${e.klasse} · Lernkarte „${e.lernkarte}“`, e.kennung));
    }
    const z = aufgT8.zuordnung.find((x) => x.entwurf_schluessel === r.id);
    if (z) for (const x of z.aufgaben.slice(0, 3 - aufgaben.length)) {
      const d = JSON.parse(fs.readFileSync(path.join(repo, x.datei), 'utf8')), a = d.aufgaben[x.index_in_aufgaben];
      assert.ok(a && a.l === x.lernkarte, `${x.datei} Stelle ${x.index_in_aufgaben}`);
      aufgaben.push(aufgabe(a, `${path.basename(x.datei, '.json')} · Stelle ${x.index_in_aufgaben} · Klasse ${x.klasse} · Lernkarte „${x.lernkarte}“`, `${path.basename(x.datei, '.json')}#${x.index_in_aufgaben}`));
    }
    const lp = lehrplanT8.find((x) => x.entwurf_schluessel === r.id);
    lehrer[r.id] = { kennung: L.kennung, klassen: k.klassen || {}, grundlage: k.klassen_grundlage || '',
      themen: (k.themen || []).map((t) => ({ schluessel: t, titel: inhalt.themen[t] ? inhalt.themen[t].titel : t, ort: inhalt.themen[t] ? inhalt.themen[t].ort : '', thema_id: themenIds[t] || null })),
      fehlbilder: k.fehlbilder || [], aufgaben,
      zuordnung: s && s.befund !== 'passt' ? { befund: s.befund, text: s.text } : null,
      lehrplan: lp ? { einfuehrung: lp.einfuehrung, neu_in_jahr: lp.lehrplan_kopie_neu_in_jahr, klassen: lp.klassen_in_denen_die_regel_vorkommt, befund: lp.befund, nicht_geprueft: lp.nicht_geprueft } : null };
  }

  const daten = {
    hinweis: 'Erzeugt mit tools/regeln_bauen.cjs – nicht von Hand ändern. Mathe-Inhalt vom Mathe-Profi (inhalt.json Stand ' + inhalt.stand + ', texte8), Darstellung vom Designer (entwurf7).',
    etagen: inhalt.etagen, regeln, leitern: inhalt.leitern, planeten, gesetze, stichwoerter: inhalt.stichwoerter, formeln: inhalt.formeln, arbeitsweisen, themen: inhalt.themen,
    kurz, zeichnungen, lehrer,
  };
  // Klassen der Daten-HTML bekommen das Präfix der App (ru-), damit keine Stilregel der App hineinwirkt
  const text = JSON.stringify(daten).replace(/class=\\"([^"\\]*)\\"/g, (_, c) => `class=\\"${c.split(/\s+/).filter(Boolean).map((x) => 'ru-' + x).join(' ')}\\"`);
  const zahlen = { regeln: regeln.length, schichten: inhalt.etagen.length, gebiete: planeten.length, ideen: planeten.reduce((n, p) => n + p.ideen.length, 0), arbeitsweisen: arbeitsweisen.length,
    gesetze: gesetze.length, zeichnungen: Object.keys(zeichnungen).length, luecken, einzelregeln: einzel.length, kurz: Object.keys(kurz).length,
    aufgaben: Object.fromEntries(Object.entries(lehrer).map(([k, v]) => [k, v.aufgaben.length])) };
  assert.deepEqual([zahlen.regeln, zahlen.schichten, zahlen.gebiete, zahlen.ideen, zahlen.arbeitsweisen, zahlen.luecken, zahlen.einzelregeln, zahlen.kurz], [14, 4, 7, 28, 8, 25, 30, 42]);
  return { text: text + '\n', zahlen };
}

if (require.main === module) {
  const { text, zahlen } = bauen();
  if (process.argv.includes('--pruefen')) {
    const da = fs.existsSync(ZIEL) ? fs.readFileSync(ZIEL, 'utf8') : '';
    if (da !== text) { console.error('daten/regeln-universum.json passt nicht zum Bau – bitte node tools/regeln_bauen.cjs ausführen'); process.exit(1); }
  } else fs.writeFileSync(ZIEL, text);
  console.log(JSON.stringify(zahlen), Math.round(text.length / 1024) + ' kB');
  console.log('OK');
}
module.exports = { bauen, ZIEL };
