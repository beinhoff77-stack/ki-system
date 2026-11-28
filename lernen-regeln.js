/* RU-App (0.95.0): Regel-Universum, Stufe 1 (ohne Datenbank, ohne Lernstand).
   Vorgabe inhalte/design/gesetzbuch/umsetzung7.md (Abschnitt 10 „Achte Runde“), Entwurf entwurf7/ (app.js, stil.css); Lehrer-Ansicht inhalte/plan/regeln-lehrer.md.
   Daten: daten/regeln-universum.json, erzeugt mit tools/regeln_bauen.cjs (Mathe-Profi + Designer), erst beim Öffnen geladen (Service Worker hält sie offline vor).
   Ansichten (eine Route „regeln“, Unteradresse wie im Entwurf):
     #/regeln/<kind>[-<adresse>]   Kind: Ebene 0 universum · 1 sonne, gebiet-<k>, weisen · 2 r<n>, idee-<k>-<n>, weise-<n> · 3 regel-<id> · klassen[-<k>] · suche
     #/regeln                      Eltern/Lehrer: nüchterne Liste aller Regeln und Arbeitsweisen
     #/regeln/lehrer-r<n>          Eltern/Lehrer: Blatt einer Rechenregel (alle Stufen offen, Verweise, Rückmeldung)
     #/regeln/kind[-<adresse>]     Eltern/Lehrer: „So sieht es das Kind“ (ohne Kind, ohne Lernstand)
   Der Mathe-Inhalt enthält Auszeichnung (Bruch-Schreibweise, Hervorhebung, SVG der Zeichnungen) und wird deshalb als HTML eingesetzt –
   ausschließlich aus der eigenen, im Repo erzeugten Datendatei; alle übrigen Texte gehen durch ruEsc. Bausteine der App (Kopf, Rahmen, Formular) mit el. */
'use strict';

// ===================== Datenteil (ohne Browser prüfbar: tests/lernen-regeln.test.cjs) =====================
const ruEsc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const RU_KL = [5, 6, 7, 8, 9, 10];
function ruIndex(D) {
  const LEITER = D.leitern, KURZ = D.kurz, LEHRER = D.lehrer;
  const REGEL = Object.fromEntries(D.regeln.map((r) => [r.id, r]));
  const GESETZ = Object.fromEntries(D.gesetze.map((g) => [g.id, g]));
  const ETAGE = Object.fromEntries(D.etagen.map((e) => [e.nr, e.name]));
  const PLANETEN = D.planeten, PLANET = Object.fromEntries(PLANETEN.map((p) => [p.name, p]));
  const KUERZEL_ZU = Object.fromEntries(PLANETEN.map((p) => [p.kuerzel, p.name]));
  const IDEE = {}; for (const p of PLANETEN) for (const i of p.ideen) IDEE[i.id] = { ...i, planet: p.name, von: p.ideen.length };
  const IDEEN = Object.values(IDEE);
  const ideeVon = (gid) => IDEEN.find((i) => i.gesetze.includes(gid));
  const thema = (k) => (D.themen[k] ? `${D.themen[k].ort} · ${D.themen[k].titel}` : k);
  const klasseVon = (g) => (g.gym && g.gym !== '–' ? 'Klasse ' + g.gym : 'Realschule oder IB');
  const ART_KURZ = { Einführung: 'E', Anwendung: 'A', Vorwissen: 'V' };
  const bandStufen = (id) => Object.fromEntries(LEITER[id].stufen.map((s) => [s.klasse, s.text ? ART_KURZ[s.art] : 'N']));
  const spanneText = (id) => { const k = LEITER[id].klassen; return k.length === 1 ? `Klasse ${k[0]}` : `Klasse ${k[0]} bis ${k[k.length - 1]}`; };
  const brauchtRegeln = (g) => ((g.sonne || '').match(/\d+/g) || []).map((n) => 'R' + n).filter((id) => REGEL[id]);
  const ideeBraucht = (i) => [...new Set(i.gesetze.flatMap((gid) => brauchtRegeln(GESETZ[gid])))].sort((a, b) => a.slice(1) - b.slice(1));
  const regelTraegt = (rid) => IDEEN.map((i) => ({ i, n: i.gesetze.filter((gid) => brauchtRegeln(GESETZ[gid]).includes(rid)).length })).filter((x) => x.n);
  function verweise(text) { const aus = [], s = text || ''; for (const m of s.matchAll(/\b([A-Z]\d+)\b/g)) if (GESETZ[m[1]]) aus.push(m[1]); for (const m of s.matchAll(/Rechenregel (\d+)/g)) aus.push('R' + m[1]);
    for (const r of D.regeln) if (s.includes(r.name)) aus.push(r.id); return [...new Set(aus)]; }
  const erklaertUeber = (rid) => verweise(REGEL[rid].weg).filter((x) => REGEL[x]);
  const hilftBei = (rid) => D.regeln.filter((r) => erklaertUeber(r.id).includes(rid)).map((r) => r.id);
  const zahlGesetze = (p) => p.ideen.reduce((a, i) => a + i.gesetze.length, 0);
  const felder = (id) => D.zeichnungen[id] || [];
  // Adressen innerhalb des Universums (ohne Präfix; die Ansicht macht daraus #/regeln/…)
  const adr = { regel: (id) => id.toLowerCase(), idee: (id) => 'idee-' + id.slice(2), weise: (n) => 'weise-' + n, gesetz: (id) => 'regel-' + id.toLowerCase(), lehrer: (id) => 'lehrer-' + id.toLowerCase(), gebiet: (name) => 'gebiet-' + PLANET[name].kuerzel };
  // Suche (aus dem Entwurf übernommen, Ziele angepasst; Arbeitsweisen auch über Kurzbeschreibung und Beispiel)
  // Wörter: klein, Umlaute ausgeschrieben, ohne Auszeichnung. Buchstaben und Ziffern getrennt („5cm“ → 5, cm), Hochzahl bleibt am Wort („cm²“),
  // Zeichen wie % und ° sind eigene Wörter – so findet die Suche auch Einheiten und Zeichen (cm, kg, m, h, %).
  const wort = (s) => String(s).toLowerCase().replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss').replace(/<[^>]+>/g, ' ').replace(/&(?:[a-z]+|#\d+);/g, ' ');
  const woerter = (s) => wort(s).match(/[a-z]+[²³]?|\d+|[%‰°€]/g) || [];
  // Suchwörter: „m2“/„cm3“ wie „m²“/„cm³“; kurze Füllwörter zählen nicht, solange die Frage noch ein anderes Wort hat
  const FUELL = new Set(['in', 'im', 'am', 'an', 'um', 'zu', 'ab', 'es', 'so', 'da', 'wo', 'je', 'ob', 'du', 'er', 'ja', 'ist', 'der', 'die', 'das', 'und', 'mit', 'von', 'den', 'ein']);
  const frageWoerter = (q) => { const t = (woerter(String(q).replace(/\b([a-z]{1,3})([23])\b/gi, (x, e, h) => e + (h === '2' ? '²' : '³')))); const ohne = t.filter((w) => !FUELL.has(w)); return ohne.length ? ohne : t; };
  const STICH = {}; D.stichwoerter.forEach((s) => { (STICH[s.ziel] ||= []).push(s.wort); });
  // Fließtext: Klassenbeispiele (Leiter) und die aufgeschlagenen Texte (genau, warum, wann, verwandt)
  const fliess = (x, id) => [...((LEITER[id] || {}).stufen || []).map((k) => k.text || ''), x.genau, x.warum, x.voraus, x.verwandt].filter(Boolean).join(' ');
  const SUCHBAR = [
    ...D.regeln.map((r) => ({ id: r.id, art: 'Rechenregel ' + r.nr, name: r.name, satz: r.satz, mehr: fliess(r, r.id) + ' ' + r.fehler, ort: 'Sonne · Rechenregeln', ziel: adr.regel(r.id), ae: ['Rechenregel', `${r.id} (${LEHRER[r.id].kennung})`] })),
    ...D.gesetze.map((g) => { const i = ideeVon(g.id); return { id: g.id, art: 'Regel ' + g.id, name: g.name, satz: g.satz, mehr: (g.klassen || []).map((k) => k.text).join(' ') + ' ' + (g.fehler || '') + ' ' + (g.beispiel || '') + ' ' + fliess(g, g.id), ort: g.planet + (i ? ' › ' + i.kurz : ''), ziel: adr.gesetz(g.id), ae: ['Einzelregel', g.id] }; }),
    ...IDEEN.map((i) => ({ id: i.id, art: 'Tragende Idee', name: i.kurz, satz: i.satz, mehr: (KURZ[i.id] || '') + ' ' + fliess(i, i.id), ort: i.planet, ziel: adr.idee(i.id), ae: ['Idee', i.id] })),
    ...D.formeln.map((f) => ({ id: 'formel ' + f.fuer, art: 'Formel', name: f.fuer, satz: f.formel, mehr: '', ort: GESETZ[f.ziel].planet + ' › ' + f.ziel, ziel: adr.gesetz(f.ziel), ae: ['Formel', 'zu ' + f.ziel] })),
    ...D.arbeitsweisen.map((a, n) => ({ id: a.name, art: 'Arbeitsweise', name: a.name, satz: a.satz, mehr: (a.kurz || '') + ' ' + ((a.beispiel || {}).text || '') + ' ' + (a.erklaerung || ''), ort: 'Arbeitsweisen', ziel: adr.weise(n + 1), ae: ['Arbeitsweise', String(n + 1)] })),
  ].map((e) => ({ ...e, stich: STICH[e.id] || [], wn: woerter(e.name), wk: (STICH[e.id] || []).map((s) => woerter(s)), ws: woerter(e.satz), wm: woerter(e.mehr) }));
  // Kurze Suchwörter (bis 3 Zeichen, Zeichen wie %) nur als ganzes Wort („m“ trifft „m“ und „m²“, nicht „mal“); lange auch als Teil eines Wortes
  const ohneHoch = (w) => w.replace(/[²³]$/, '');
  const trifft = (liste, t) => (t.length <= 3 || !/^[a-z]/.test(t) ? liste.some((w) => w === t || (!/[²³]$/.test(t) && ohneHoch(w) === t))
    : liste.some((w) => w === t || w.includes(t) || (w.length >= 5 && t.includes(w))));
  // ---------- Tafeln zum Nachschlagen (D.tafeln, gebaut von tools/tafeln_bauen.cjs) ----------
  // Adresse: tafeln (Übersicht) · tafel-<id> · tafel-<id>.<anker> (springt an die Stelle; eine Zeile mit Einzelheiten klappt dabei auf)
  const TAFELN = D.tafeln || [], TAFEL = Object.fromEntries(TAFELN.map((t) => [t.id, t]));
  adr.tafeln = () => 'tafeln'; adr.tafel = (id, anker) => 'tafel-' + id + (anker ? '.' + anker : '');
  const kennVon = (liste) => (liste || []).map((r) => r.kennung);
  // Abschnitte je Tafel: Anker, Titel, Klasse, Stichwörter, Kennungen im Universum (für Verweise); „wo“: Tafel und Anker, an denen der Abschnitt steht
  function tafelTeile(t) {
    if (t.id === 'formeln') return [{ anker: 'flaechen', titel: 'Ebene Figuren: Umfang und Flächeninhalt', stich: [], kenn: [] }, { anker: 'koerper', titel: 'Körper: Oberfläche und Volumen', stich: [], kenn: [] },
      { anker: 'sonst', titel: 'Was man sonst noch braucht', stich: [], kenn: [] }];
    if (t.arten) { const v = t.arten.find((x) => x.anker === 'volumen'), w = ((v && v.weitere_treppen) || [])[0];
      return [...t.arten.map((x) => ({ anker: x.anker, titel: x.art, kl: x.kl, stich: x.stich, kenn: kennVon(x.regeln), vorschau: x.darstellung })),
        ...(w ? [{ anker: 'hohlmass', titel: w.name, kl: v.kl, stich: [w.name, ...w.treppe.flatMap((s) => [s.einheit, s.name])], kenn: [], vorschau: w.darstellung }] : [])]; }
    // Formeln der Figuren und Körper stehen in der Gesamtübersicht (Zeile klappt auf); die Tafel selbst ist die Detailansicht
    if (t.karten) return t.karten.map((k) => ({ anker: k.anker, titel: k.name, kl: k.kl, stich: k.stich, wo: ['formeln', k.anker], vorschau: k.zeilen.map((z) => z.formel).join(' · '),
      kenn: [...new Set([...k.zeilen, ...k.zusatz].flatMap((z) => [z.ziel, ...kennVon(z.regeln)]).filter(Boolean))] }));
    // haupt: das eigene Zeichen der Zeile (Zeichen, griechischer Buchstabe, Kürzel der Vorsilbe) – die Zeichensuche stellt diese Zeile vor Zeilen, bei denen es nur Suchwort ist
    return t.eintraege.map((e) => ({ anker: e.kennung, titel: e.titel, kl: e.kl, stich: e.stich, kenn: kennVon(e.regeln), haupt: [e.zeichen, e.buchstabe, e.art === 'vorsilbe' ? e.kurz : null].filter(Boolean),
      vorschau: e.formel || e.merksatz || e.regel_text || e.bedeutung || e.satz || e.verwendung || e.definition || e.bereich || e.gegeben || '' }));
  }
  const TEILE = Object.fromEntries(TAFELN.map((t) => [t.id, tafelTeile(t)]));
  const tafelZiel = (t, teil) => (teil && teil.wo ? adr.tafel(...teil.wo) : adr.tafel(t.id, teil && teil.anker));
  // Flächen und Körper: Einstieg ist die Gesamtübersicht der Formeln (die Tafeln selbst sind die Detailansichten)
  const tafelStart = (t) => (t.id === 'formeln-flaechen' ? adr.tafel('formeln', 'flaechen') : t.id === 'formeln-koerper' ? adr.tafel('formeln', 'koerper') : adr.tafel(t.id));
  const ZU_TAFEL = {};
  for (const t of TAFELN) { if (t.richtung) (ZU_TAFEL[t.richtung.kennung] ||= []).push({ t, teil: null }); for (const x of TEILE[t.id]) for (const k of x.kenn) (ZU_TAFEL[k] ||= []).push({ t, teil: x }); }
  // Verweise einer Regel, Idee oder Einzelregel auf Tafeln: je Tafel eine Stelle (mehrere Abschnitte derselben Tafel → Anfang der Tafel)
  function tafelnZu(ids) {
    const je = new Map(); for (const id of ids) for (const v of ZU_TAFEL[id] || []) { const a = je.get(v.t.id) || { t: v.t, teile: new Set() }; a.teile.add(v.teil); je.set(v.t.id, a); }
    return [...je.values()].map(({ t, teile }) => { const tl = [...teile]; const teil = tl.length === 1 ? tl[0] : null; return { t, teil, ziel: teil ? tafelZiel(t, teil) : tafelStart(t) }; });
  }
  // Suche in den Tafeln: alle Suchwörter müssen treffen; genaues Stichwort vor Wort im Namen vor Wortteil. Die ganze Tafel gewinnt bei Gleichstand.
  const TSUCH = TAFELN.flatMap((t) => [{ t, teil: null, name: t.titel, stich: t.stich, vorschau: t.kurz }, ...TEILE[t.id].filter((x) => x.stich.length).map((x) => ({ t, teil: x, name: x.titel, stich: x.stich, vorschau: x.vorschau }))])
    .map((e) => ({ ...e, wn: woerter(e.name), wk: e.stich.map((s) => woerter(s)) }));
  const tafelTreffer = (e) => ({ id: 'tafel ' + e.t.id + (e.teil ? ' ' + e.teil.anker : ''), art: 'Tafel', tafel: true, name: e.name, satz: ruEsc(e.vorschau || ''), ort: 'Tafeln · ' + e.t.titel,
    ziel: e.teil ? tafelZiel(e.t, e.teil) : tafelStart(e.t), ae: ['Tafel', e.t.id + (e.teil ? ' ' + e.teil.anker : '')] });
  // roh: die Eingabe, wie sie getippt wurde. Ein einzelner Buchstabe trifft ein einbuchstabiges Suchwort nur in derselben Schreibung (M Mega ≠ m Milli, N ℕ ≠ n Nano).
  function tafelSuche(teile, roh = '') {
    const r = String(roh).trim(), einB = /^[A-Za-zÄÖÜäöüß]$/.test(r), ganz = woerter(r).join(' ');
    const liste = TSUCH.map((e, i) => { let p = 0; const wk = einB ? e.wk.filter((l, j) => l.length !== 1 || l[0] !== r.toLowerCase() || e.stich[j].trim() === r) : e.wk;
      for (const w of teile) { const q = wk.some((l) => l.length === 1 && l[0] === w) ? 10 : e.wn.includes(w) ? 9 : wk.some((l) => l.includes(w)) ? 6 : trifft(e.wn, w) ? 4 : wk.some((l) => trifft(l, w)) ? 3 : 0;
        if (!q) return null; p += q; }
      return { e, p: p + (e.teil ? 0 : 0.5), i, genau: !!ganz && wk.some((l) => l.join(' ') === ganz) }; }).filter(Boolean).sort((a, b) => b.p - a.p || a.i - b.i);
    // Auflagen aus Werkstatt 1156: Die Wortsuche zeigt die vier besten Tafel-Treffer; eine Zeile, deren Stichwort genau der Eingabe entspricht
    // („Prozent“, „Winkel“, „deckungsgleich“, „ist kongruent zu“), kommt immer dazu (hinter die vier, in derselben Reihenfolge).
    // Sammelbegriff: Haben fünf oder mehr Zeilen eines Abschnitts dasselbe genaue Stichwort („griechischer Buchstabe“), steht statt der einzelnen Zeilen
    // ein Treffer für den ganzen Abschnitt (das vollständige Verzeichnis) an erster Stelle.
    const sammel = new Map();
    for (const x of liste) if (x.genau && x.e.teil) { const ab = (x.e.t.abschnitte || []).find((a) => a.kennungen.includes(x.e.teil.anker)); if (ab) { const k = x.e.t.id + ' ' + ab.art; (sammel.get(k) || sammel.set(k, { t: x.e.t, ab, n: 0 }).get(k)).n++; } }
    const gross = [...sammel.values()].filter((g) => g.n >= 5), imSammel = (x) => x.genau && x.e.teil && gross.some((g) => g.t === x.e.t && g.ab.kennungen.includes(x.e.teil.anker));
    const rest = liste.filter((x) => !imSammel(x)), oben = rest.slice(0, 4);
    return [...gross.map(({ t, ab }) => ({ id: 'tafel ' + t.id + ' ab-' + ab.art, art: 'Tafel', tafel: true, name: ab.name, satz: ruEsc(`alle ${ab.kennungen.length} im Verzeichnis`), ort: 'Tafeln · ' + t.titel,
      ziel: adr.tafel(t.id, 'ab-' + ab.art), ae: ['Tafel', t.id + ' ab-' + ab.art], sammel: ab.kennungen.slice() })),
      ...oben.map(({ e }) => tafelTreffer(e)), ...rest.slice(4).filter((x) => x.genau).map(({ e }) => tafelTreffer(e))];
  }
  // ---------- Zeichensuche (Auflagen aus Werkstatt 1152) ----------
  // Die Wortzerlegung kennt nur a–z, Ziffern, %, ‰, °, € – mathematische Zeichen und griechische Buchstaben fielen dort weg (≤, π, ∈, ∢ ohne Treffer, „µm“ wurde zu „m“).
  // Darum wird die Eingabe VOR der Zerlegung als Ganzes (und je Teil zwischen Leerzeichen) exakt gegen die Suchwörter der Tafeln gesucht, die ein Zeichen enthalten
  // (alles außer Buchstaben, Ziffern, Leerzeichen) oder aus ein bis drei Großbuchstaben bestehen (N, M, AB, XIV). Groß/klein bleibt dabei erhalten (Δ ≠ δ, Σ ≠ σ, ℕ ≠ n);
  // µ (Mikrozeichen) und μ (griechisch) gelten als gleich, Leerzeichen zählen nicht („{ }“ = „{}“). Zuerst die Zeile, deren eigenes Zeichen es ist, dann Zeilen mit dem Zeichen als Suchwort.
  const zNorm = (s) => String(s ?? '').normalize('NFC').replace(/\u00b5/g, '\u03bc').replace(/\s+/g, '');
  const zeichenWort = (s) => /[^A-Za-zÄÖÜäöüß0-9\s]/.test(s) || /^[A-ZÄÖÜ]{1,3}$/.test(String(s).trim());
  // Was man auf der Tastatur tippt, wenn das Zeichen fehlt → Zeichen der Tafel (∢ und „pi“, „alpha“ … stehen schon in den Suchwörtern der Tafel)
  const Z_ALIAS = { '<=': '≤', '=<': '≤', '>=': '≥', '!=': '≠', '<>': '≠', '=/=': '≠', '+-': '±', '+/-': '±', '~=': '≈', '=>': '⇒', '<=>': '⇔', '*': '·', '∡': '∠' };
  // haupt: 2 = eigenes Zeichen genau so geschrieben, 1 = eigenes Zeichen nach Angleichung (µ/μ), 0 = nur Suchwort
  const zRoh = (s) => String(s ?? '').normalize('NFC').replace(/\s+/g, '');
  const ZSUCH = TSUCH.flatMap((e, i) => { const h = (e.teil && e.teil.haupt) || [], haupt = new Set(h.map(zNorm)), roh = new Set(h.map(zRoh));
    return [...new Set([...e.stich, ...h].filter(zeichenWort).map(zRoh))].filter(Boolean).map((r) => ({ key: zNorm(r), roh: r, e, i, haupt: haupt.has(zNorm(r)) ? 1 : 0, hroh: roh })); });
  // Regeln, in deren Name, Merksatz oder Stichwörtern das Zeichen wörtlich steht (nur für Zeichen außerhalb der Tastatur, z. B. π, √, ≤ – nicht für „:“ oder „=“)
  const klar = (t) => String(t || '').replace(/<[^>]+>/g, ' ').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&').replace(/\u00b5/g, '\u03bc');
  const ZREGEL = SUCHBAR.map((e) => ({ e, kopf: klar(e.name + ' ' + e.stich.join(' ')), text: klar(e.satz) }));
  function zeichenSuche(q) {
    const roh = String(q ?? '').trim(); if (!roh) return { tafel: [], regeln: [] };
    const teile = [roh, ...(/\s/.test(roh) ? roh.split(/\s+/) : [])].map(zRoh).map((k) => Z_ALIAS[k] || k).filter(Boolean);
    const gesehen = new Set(), tafel = [], regeln = [];
    for (const r of new Set(teile)) { const k = zNorm(r), rang = (x) => x.haupt + (x.hroh.has(r) ? 1 : 0);
      for (const z of ZSUCH.filter((x) => x.key === k).sort((a, b) => rang(b) - rang(a) || a.i - b.i)) { if (gesehen.has(z.i)) continue; gesehen.add(z.i); tafel.push(tafelTreffer(z.e)); }
      if (/[^\x00-\x7F·]/.test(k)) regeln.push(...ZREGEL.filter((x) => x.kopf.includes(k) || x.text.includes(k)).sort((a, b) => b.kopf.includes(k) - a.kopf.includes(k)).map((x) => x.e));
    }
    return { tafel, regeln: [...new Set(regeln)].slice(0, 8) };
  }
  // Ein- und Zweizeichen-Eingaben: sofort suchen, wenn es ein Tafel-Zeichen, eine Einheit oder ein bekanntes Kurzwort ist (cm, kg, m, %, π, ≤ …); sonst ab drei Zeichen
  const kurzForm = (s) => (/^[A-Za-zÄÖÜäöüß]+$/.test(s) ? s.toLowerCase() : s); // Buchstabenwörter ohne Groß/klein (cm = CM), Zeichen genau (π ≠ Π)
  const KURZ_BEKANNT = new Set(TSUCH.flatMap((e) => e.stich.map((s) => kurzForm(String(s).trim()))).filter((s) => s.length <= 2));
  const sofort = (q) => { const r = String(q ?? '').trim(); return r.length >= 3 || (!!r && (KURZ_BEKANNT.has(kurzForm(r)) || zeichenSuche(r).tafel.length > 0)); };
  function suche(q) {
    const z = zeichenSuche(q), teile = frageWoerter(q); if (!teile.length && !z.tafel.length && !z.regeln.length) return [];
    // Zeichen zuerst (die eigene Zeile der Tafel), dann Tafeln (Nachschlagen: „cm“, „Kreis“, „Volumen“ landen auf der passenden Tafel), danach Regeln, Ideen, Formeln
    const schon = new Set(z.tafel.map((x) => x.id)), tafel = teile.length ? tafelSuche(teile, q).filter((x) => !schon.has(x.id)) : [];
    // Regeln mit dem Zeichen im Wortlaut nur, wenn die Eingabe keine Wörter hat (π, √, ≤); sonst wie bisher über die Wörter („m²“ = „m2“)
    const regeln = teile.length ? sucheRegeln(teile) : z.regeln;
    return [...z.tafel, ...tafel, ...regeln].slice(0, 16);
  }
  function sucheRegeln(teile) {
    return SUCHBAR.map((e) => { let p = 0, kopf = 0, ueber = null; for (const t of teile) { const k = e.wk.findIndex((l) => trifft(l, t)); if (k >= 0) { p += e.wk[k].includes(t) ? 9 : 5; ueber = e.stich[k]; kopf++; }
      const n = trifft(e.wn, t); if (n) kopf++; p += (n ? 6 : 0) + (trifft(e.ws, t) ? 3 : 0) + (trifft(e.wm, t) ? 1 : 0); } return { ...e, p, kopf, ueber }; })
      // Treffer in Name oder Stichwort vor Treffern nur im Text
      .filter((x) => x.p > 0).sort((a, b) => b.kopf - a.kopf || b.p - a.p || (a.art === 'Formel') - (b.art === 'Formel')).slice(0, 14);
  }
  return { D, LEITER, KURZ, LEHRER, REGEL, GESETZ, ETAGE, PLANETEN, PLANET, KUERZEL_ZU, IDEE, IDEEN, ideeVon, thema, klasseVon, bandStufen, spanneText,
    brauchtRegeln, ideeBraucht, regelTraegt, erklaertUeber, hilftBei, zahlGesetze, felder, adr, suche, sofort, TAFELN, TAFEL, TEILE, tafelnZu };
}

// „Ändern lassen“ (Eltern/Lehrer): ein Knopf an jedem Element. Die Fundstelle steht vollständig im Knopf (data-wo) und später am Anfang des Auftrags:
// Regel-Universum · <Art> <Kennung> · <Name> · Feld <Feld>. Neue Elemente (z. B. Tafeln) bekommen den Knopf mit einer Zeile: ae('Tafel', id, titel, feld).
const ruFundstelle = (art, kennung, name, feld) => ['Regel-Universum', [art, kennung].filter((x) => x !== '' && x != null).join(' '), name, feld ? 'Feld ' + feld : ''].filter(Boolean).join(' · ');
const RU_STIFT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16v4z"/><path d="M13.5 6.5l4 4"/></svg>';
const ruAendernKnopf = (wo) => `<button class="ru-ae" type="button" data-wo="${ruEsc(wo)}" aria-expanded="false" title="${ruEsc(wo)}">${RU_STIFT}<span>Ändern lassen</span></button>`;

// Ebene einer Adresse: 0 Universum · 1 Sonne, Gebiet, Arbeitsweisen, Klassen, Suche · 2 Regel, Idee, Arbeitsweise, Lehrer · 3 einzelne Regel
const ruEbene = (h) => (h === 'universum' || !h ? 0 : /^(sonne|weisen|gebiet-|klassen|suche|liste)/.test(h) ? 1 : h.startsWith('regel-') ? 3 : 2);

// ===================== Seiten als HTML (aus dem Entwurf entwurf7/teile/app.js, Klassen mit Präfix ru-) =====================
// I: ruIndex · ziel(adresse) → href · zustand: { klasse, frage, bis } · ansicht: 'kind' (Kind angemeldet) | 'leitung' (Erwachsener in der Ansicht eines Kindes) | 'ansicht' (Eltern sehen die Kinderseite) | 'lehrer'
function ruSichten(I, ziel, zustand, ansicht = 'kind') {
  const { D, LEITER, KURZ, LEHRER, REGEL, GESETZ, ETAGE, PLANETEN, PLANET, KUERZEL_ZU, IDEE, IDEEN, adr } = I;
  const esc = ruEsc, KL = RU_KL, Z = ziel;
  // „Ändern lassen“ nur für Eltern und Lehrer (Kinderseite ansehen, Liste, Blatt); das Kind sieht den Knopf nie
  const ERW = ansicht !== 'kind';
  const ae = (art, kennung, name, feld) => (ERW ? ruAendernKnopf(ruFundstelle(art, kennung, name, feld)) : '');
  const aeW = (w, feld) => (w ? ae(w.art, w.kennung, w.name, feld) : '');
  const aeZeile = (knopf) => (knopf ? `<div class="ru-ae-zeile">${knopf}</div>` : '');
  const aeKopf = (titel, knopf) => (knopf ? `<div class="ru-ae-kopf">${titel}${knopf}</div>` : titel);
  const ohneTags = (t) => String(t || '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
  const wer = { regel: (id) => ({ art: 'Rechenregel', kennung: `${id} (${LEHRER[id].kennung})`, name: REGEL[id].name, id }), idee: (id) => ({ art: 'Idee', kennung: id, name: IDEE[id].kurz, id }),
    gesetz: (id) => ({ art: 'Einzelregel', kennung: id, name: GESETZ[id].name, id }), weise: (n) => ({ art: 'Arbeitsweise', kennung: String(n), name: D.arbeitsweisen[n - 1].name, id: D.arbeitsweisen[n - 1].name }) };
  // Nur für Eltern und Lehrer: Formeln und Stichwörter (Suche) eines Elements, je mit Knopf
  function erwBlock(w) {
    if (!ERW) return '';
    const fo = D.formeln.filter((f) => f.ziel === w.id), st = D.stichwoerter.filter((x) => x.ziel === w.id);
    if (!fo.length && !st.length) return '';
    return `<section class="ru-erw"><p class="ru-ueber">Für Eltern und Lehrer</p>${fo.length ? `<h3 class="ru-ueber">Formeln (${fo.length})</h3><ul class="ru-erw-liste">${fo.map((f) => `<li><span class="ru-erw-text"><b>${esc(f.fuer)}</b> <span class="ru-rechnung">${esc(f.formel)}</span>${f.bedingung && f.bedingung !== '–' ? ` <span class="ru-leise">(${esc(f.bedingung)})</span>` : ''}</span>${ae('Formel', 'zu ' + w.id, f.fuer, 'formel')}</li>`).join('')}</ul>` : ''}
      ${st.length ? `<h3 class="ru-ueber">Stichwörter der Suche (${st.length})</h3><ul class="ru-erw-liste">${st.map((x) => `<li><span class="ru-erw-text">${esc(x.wort)}</span>${ae('Stichwort', 'zu ' + w.kennung, x.wort, 'wort')}</li>`).join('')}</ul>` : ''}</section>`;
  }
  const planetScheibe = (name, gr = 28) => `<svg class="ru-scheibe" width="${gr}" height="${gr}" viewBox="-22 -22 44 44" aria-hidden="true"><circle r="21" fill="${PLANET[name].farbe}"/><circle r="21" fill="url(#ru-glanz)"/>${PLANET[name].zeichen}</svg>`;
  // Achte Runde: drei Zustände, die Klasse steht im Kästchen. neu = eingeführt · da = angewendet oder Vorwissen · nicht = kommt nicht vor
  const DREI = { E: 'neu', A: 'da', V: 'da', N: 'nicht' }, DREI_WORT = { neu: 'neu', da: 'kommt vor', nicht: 'kommt nicht vor' };
  const band = (id, o = {}) => { const st = I.bandStufen(id); return `<span class="ru-b6${o.gross ? ' ru-gross' : ''}" role="img" aria-label="Klassen: ${KL.map((k) => `${k} ${DREI_WORT[DREI[st[k]]]}`).join(', ')}">${KL.map((k) => `<i class="ru-${DREI[st[k]]}">${k}</i>`).join('')}</span>`; };
  const LEGENDE = '<p class="ru-legende"><span class="ru-b6"><i class="ru-neu">5</i></span>neu <span class="ru-b6"><i class="ru-da">6</i></span>kommt vor <span class="ru-b6"><i class="ru-nicht">9</i></span>kommt nicht vor</p>';
  const SF = ['', 'var(--s1)', 'var(--s2)', 'var(--s3)', 'var(--s4)'];
  const ringBild = (nr, gr = 34) => `<svg class="ru-ring" width="${gr}" height="${gr}" viewBox="-22 -22 44 44" aria-hidden="true">${[4, 3, 2, 1].map((k) => `<circle r="${k * 5 + 1}" fill="${SF[k]}" opacity="${k === nr ? 1 : 0.3}"${k === nr ? ' stroke="#11161D" stroke-width="1.6"' : ''}/>`).join('')}</svg>`;
  function sonnenSchnitt() { // Halbkreis, vier Bänder von innen nach außen, beschriftet; Tipp springt zur Schicht
    const R = [0, 56, 98, 140, 182], cy = 190;
    const ring = (k) => `<path d="M${200 - R[k]} ${cy}A${R[k]} ${R[k]} 0 0 1 ${200 + R[k]} ${cy}Z" fill="${SF[k]}"/>`;
    // Tippfläche = das ganze Band (nicht nur die Schriftzeile), damit sie mindestens 44 px hoch ist; innere Bänder liegen oben
    const schrift = (k, y) => `<g class="ru-sc-ziel" data-schicht="${k}" role="button" tabindex="0" aria-label="Schicht ${k}: ${esc(ETAGE[k])}">${ring(k)}<text x="200" y="${y}" text-anchor="middle" font-family="var(--grotesk)" font-weight="700" font-size="${k === 1 ? 14 : 15}" fill="#11161D"><tspan font-family="var(--mono)" font-weight="800">${k}</tspan>  ${esc(ETAGE[k])}</text></g>`;
    return `<figure class="ru-schnitt"><svg viewBox="0 0 400 ${cy + 2}" aria-label="Schnitt durch die Sonne: vier Schichten von innen nach außen">${schrift(4, cy - 154)}${schrift(3, cy - 112)}${schrift(2, cy - 70)}${schrift(1, cy - 18)}${[4, 3, 2, 1].map((k) => `<path d="M${200 - R[k]} ${cy}A${R[k]} ${R[k]} 0 0 1 ${200 + R[k]} ${cy}" fill="none" stroke="#11161D" stroke-opacity=".35" stroke-width="1.2" pointer-events="none"/>`).join('')}<line x1="6" y1="${cy + 1}" x2="394" y2="${cy + 1}" stroke="var(--ru-text)" stroke-width="2"/></svg><figcaption>Schnitt durch die Sonne: innen die Grundlage, außen, was darauf aufbaut. Tippe eine Schicht an.</figcaption></figure>`;
  }
  const satzZeile = (t) => t.replace(/<br>/g, ' ');
  const verweisRegel = (id) => `<a class="ru-verweis" href="${Z(adr.regel(id))}"><span class="ru-nr">Regel ${id.slice(1)}</span>${esc(REGEL[id].name)}</a>`;

  // ---------- Rechenzeile mit gelb umrahmter Stelle (Klassenleiter) ----------
  const mkText = (text, pos, von, bis) => { let aus = '', p = von; for (const [a, e] of pos) { if (e <= von || a >= bis) continue; aus += esc(text.slice(p, a)) + `<b class="ru-w${e - a <= 13 ? ' ru-fest' : ''}">${esc(text.slice(a, e))}</b>`; p = e; } return aus + esc(text.slice(p, bis)); };
  function zeileTeile(s, grenze) { const [a, e] = s.pos[0], vor = s.text.slice(0, a); let schnitt = 0;
    if (vor.length > grenze) { const doppel = vor.lastIndexOf(': '); if (doppel >= 0 && vor.length - doppel - 2 <= grenze) schnitt = doppel + 2;
      else { schnitt = -1; for (const m of vor.matchAll(/ (=|→|\|) /g)) if (vor.length - m.index - m[0].length <= grenze) { schnitt = m.index + m[0].length; break; }
        if (schnitt < 0) { schnitt = vor.length; for (let i = 0; i < vor.length; i++) if (vor[i] === ' ' && vor.length - i - 1 <= grenze) { schnitt = i + 1; break; } } } }
    return { vorsatz: mkText(s.text, [], 0, schnitt).trim(), vor: mkText(s.text, [], schnitt, a), marke: esc(s.text.slice(a, e)), nach: mkText(s.text, s.pos.slice(1), e, s.text.length) }; }
  function klassenLeiter(id, w) {
    const L = LEITER[id]; if (!L) return '';
    const knopf = (s, feld) => aeW(w && { art: 'Leiter', kennung: leiterKennung(id, L.stufen, s), name: w.name }, feld + (s.thema ? ` (Thema ${s.thema})` : '')); const wenige = !REGEL[id] && L.klassen.length <= 2, stufen = L.stufen.filter((s) => s.text || !wenige);
    const maxMarke = Math.max(...L.stufen.filter((s) => s.text).map((s) => s.pos[0][1] - s.pos[0][0])), grenze = Math.max(0, Math.min(14, 30 - maxMarke));
    return `<ol class="ru-leiter ru-gl">${stufen.map((s) => { if (!s.text) return `<li class="ru-luecke"><span class="ru-stufe">${s.klasse}</span><p class="ru-ganz${ERW ? ' ru-ae-in' : ''}"><span>Kommt in Klasse ${s.klasse} nicht vor: ${esc(s.grund)}.</span>${knopf(s, 'Lücke (kommt nicht vor)')}</p></li>`;
      const z = zeileTeile(s, grenze), meta = `<p class="ru-kl ru-ganz${ERW ? ' ru-ae-in' : ''}"><span>${s.art}${s.thema ? ' · ' + esc(I.thema(s.thema)) : ''}</span>${knopf(s, 'Beispiel')}</p>`;
      return `<li><span class="ru-stufe">${s.klasse}</span>${z.vorsatz ? `<p class="ru-rechnung ru-vorsatz ru-ganz">${z.vorsatz}</p>` : ''}<span class="ru-rechnung ru-vor">${z.vor}</span><span class="ru-rechnung ru-ab"><b class="ru-w ru-mk${s.pos[0][1] - s.pos[0][0] <= 13 ? ' ru-fest' : ''}">${z.marke}</b><span class="ru-nach">${z.nach}</span></span>${meta}</li>`; }).join('')}</ol>`;
  }
  // Kennung einer Leiterstufe: Element, Klasse und – bei mehreren Beispielen in einer Klasse – deren Nummer
  const leiterKennung = (id, alle, s) => { const gleich = alle.filter((x) => x.klasse === s.klasse); return `${id} Klasse ${s.klasse}${gleich.length > 1 ? ' Beispiel ' + (gleich.indexOf(s) + 1) : ''}`; };
  const beispielListe = (klassen, w) => `<ol class="ru-leiter">${klassen.map((k) => `<li><span class="ru-stufe">${k.klasse}</span><div><p class="ru-rechnung">${esc(k.text)}</p><p class="ru-kl${ERW ? ' ru-ae-in' : ''}"><span>${k.art}${k.thema ? ' · ' + esc(I.thema(k.thema)) : ''}</span>${aeW(w && { art: 'Leiter', kennung: leiterKennung(w.id, klassen, k), name: w.name }, 'Beispiel' + (k.thema ? ` (Thema ${k.thema})` : ''))}</p></div></li>`).join('')}</ol>`;

  // ---------- Zeichnungen: ein Feld (Stufe „Beispiel“) oder die übrigen Felder („Genau erklärt“) ----------
  const glText = (f) => (f.gl ? `<p class="ru-z-gl">${f.gl.includes(' = ') && !f.gl.includes('class="ru-nb"') && !f.gl.includes('<br>') ? f.gl.replace(' = ', ' <span class="ru-nb">= ') + '</span>' : f.gl}</p>` : '');
  // knopf: „Ändern lassen“ für dieses Bild (unten im Feld; das Formular erscheint unter der ganzen Zeichnung)
  const feldHtml = (f, mitSchritt, knopf = '') => `<div class="ru-z-teil">${mitSchritt && f.pfeil ? `<p class="ru-z-schritt">${f.pfeil}</p>` : ''}${f.kopf ? `<p class="ru-z-kopf">${f.kopf}</p>` : ''}${f.svg}${glText(f)}<p class="ru-z-satz">${f.satz}</p>${aeZeile(knopf)}</div>`;
  const bildKnopf = (w, id, n, f) => aeW(w && { art: 'Zeichnung', kennung: `${id} Bild ${n}`, name: w.name }, f && f.kopf ? 'Bild „' + ohneTags(f.kopf) + '“' : 'Bild');
  function felderHtml(felder, w, id, ab = 1) {
    const reihen = []; felder.forEach((f) => { if (f.neu || !reihen.length) reihen.push({ titel: f.neu, felder: [] }); reihen[reihen.length - 1].felder.push(f); });
    return `<figure class="ru-zeichnung" data-felder="${felder.length}">${reihen.map((r) => `${r.titel ? `<p class="ru-z-ast">${r.titel}</p>` : ''}<div class="ru-z-reihe" data-n="${r.felder.length}">${r.felder.map((f, i) => `${i ? `<div class="ru-z-pfeil${f.pfeil ? '' : ' ru-leer'}" aria-hidden="true"></div>` : ''}${feldHtml(f, true, bildKnopf(w, id, ab + felder.indexOf(f), f))}`).join('')}</div>`).join('')}</figure>`;
  }
  function beispiel(id, w) { // das erste Feld der Hauptzeichnung; ohne Zeichnung das Beispiel der ersten Klasse
    const f = I.felder(id)[0]; if (f) return `<figure class="ru-zeichnung ru-eins" data-felder="1"><div class="ru-z-reihe" data-n="1">${feldHtml(f, false, bildKnopf(w, id, 1, f))}</div></figure>`;
    const s = LEITER[id] && LEITER[id].stufen.find((x) => x.text); return s ? `<p class="ru-rechnung ru-gross-r">${mkText(s.text, s.pos, 0, s.text.length)}</p><p class="ru-kl">Klasse ${s.klasse} · ${s.art}</p>` : '';
  }

  // ---------- Bausteine ----------
  const CHEVRON = '<svg class="ru-chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 10l4 4 4-4" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  const stufe = (key, titel, hinweis, inhalt, offen) => `<details class="ru-stufe" data-stufe="${key}"${offen ? ' open' : ''}><summary><span class="ru-st-titel">${titel}</span>${hinweis ? `<span class="ru-st-hinweis">${hinweis}</span>` : ''}${CHEVRON}</summary><div class="ru-st-inhalt">${inhalt}</div></details>`;
  const pfad = (...teile) => `<nav class="ru-pfad" aria-label="Brotkrumen"><a href="${Z('universum')}">‹ Universum</a>${teile.filter(Boolean).map((t) => `<span class="ru-t">›</span>${t}`).join('')}</nav>`;
  const blaettern = (vor, nach) => `<nav class="ru-blaettern" aria-label="Blättern">${vor ? `<a class="ru-vor" href="${vor.href}"><small>‹ ${vor.ueber}</small><span>${esc(vor.name)}</span></a>` : '<span></span>'}${nach ? `<a class="ru-nach" href="${nach.href}"><small>${nach.ueber} ›</small><span>${esc(nach.name)}</span></a>` : '<span></span>'}</nav>`;
  const merksatz = (satz, knopf = '') => `<div class="ru-merk">${aeKopf('<p class="ru-ueber">Merksatz</p>', knopf)}<p class="ru-merksatz">${satz}</p></div>`;
  const fehlerTeile = (t) => (t || '').split(/\s*Und:\s*/).filter(Boolean);
  const fehlerListe = (t) => `<ul class="ru-fehlerliste">${fehlerTeile(t).map((x) => `<li>${x.charAt(0).toUpperCase() + x.slice(1)}</li>`).join('')}</ul>`;
  const VERGLEICH_OFFEN = false; // Stufe 4 standardmäßig zu (umsetzung7.md, Abschnitt 3: gemessen fast oder mehr als eine Bildschirmhöhe)
  const umschalter = (an) => `<nav class="ru-umschalter" aria-label="Ansicht"><a href="${Z('universum')}"${an === 'aufbau' ? ' aria-current="page"' : ''}>Aufbau</a><a href="${Z('klassen')}"${an === 'klassen' ? ' aria-current="page"' : ''}>Durch die Klassen</a></nav>`;
  // Tafeln zum Nachschlagen (Wunsch des Nutzers 28.11.): kein eigener Reiter mehr – jede Tafel steht ganz oben in ihrem Gebiet („Auf einen Blick“, Zuordnung aus den Daten: tafel.gebiete)
  // Eltern/Lehrer sehen die Kinderseite: schmale Leiste mit dem Weg zurück zum Blatt
  const elternBand = (rid) => (ansicht === 'ansicht' ? `<div class="ru-lehrer-band ru-band-kind"><span>So sieht es das Kind</span><a class="ru-verweis" href="${rid ? '#/regeln/lehrer-' + rid.toLowerCase() : '#/regeln'}">${rid ? 'Blatt für Eltern und Lehrer ›' : 'Alle Regeln (Eltern und Lehrer) ›'}</a></div>` : '');

  // Ebene 0: das Universum – nur die großen Teile, je eine antippbare Fläche
  function sichtUniversum() {
    const bahnen = PLANETEN.map((p, n) => `<li class="ru-bahn0${n % 2 ? ' ru-rechts' : ''}"><a class="ru-planet0" href="${Z(adr.gebiet(p.name))}">${planetScheibe(p.name, 44)}<span><b>${esc(p.name)}${blickHinweis(p.name)}</b><small>${p.ideen.length} tragende Ideen</small></span></a></li>`).join('');
    return `<div class="ru-breite ru-schmal ru-start ru-universum">${elternBand()}<h1 class="ru-titel">Regel-Universum</h1><p class="ru-lead">Alle festen Regeln der Mathematik, Klasse 5 bis 10. Tippe auf einen Teil.</p>${umschalter('aufbau')}
      <a class="ru-sonne0" href="${Z('sonne')}"><span class="ru-s0-kreis" aria-hidden="true"></span><span class="ru-s0-text"><small>Die Sonne · die Grundlage</small><b>14 Rechenregeln</b><small>gelten in jedem Gebiet und jeder Klasse${blickHinweis('Sonne')}</small></span></a>
      <p class="ru-u-zwischen">Darum die sieben Gebiete:</p>
      <ol class="ru-bahnen0">${bahnen}</ol>
      <a class="ru-guertel0" href="${Z('weisen')}"><b>8 Arbeitsweisen</b><small>wie man vorgeht – gilt überall</small></a>${systemBild()}</div>`;
  }
  // Rechner (ab 900 px): dasselbe als Sonnensystem. Sonne links angeschnitten, Bahnen als Kreisbögen um sie, Planet und Name auf der Bahn.
  function systemBild() {
    const cx = -40, cy = 300, rs = 300, dy = [-150, 95, -40, 175, -205, 40, -95], weg = (r) => `M${cx + Math.sqrt(r * r - 290 * 290)} ${cy - 290}A${r} ${r} 0 0 1 ${cx + Math.sqrt(r * r - 290 * 290)} ${cy + 290}`;
    const bahnR = (n) => 400 + n * 78;
    const pl = PLANETEN.map((p, n) => { const r = bahnR(n), y = cy + dy[n], x = cx + Math.sqrt(r * r - dy[n] * dy[n]);
      return `<path d="${weg(r)}" fill="none" stroke="var(--ru-linie)" stroke-width="1.5"/><a href="${Z(adr.gebiet(p.name))}" class="ru-sp"><circle cx="${x}" cy="${y}" r="38" fill="transparent"/><g transform="translate(${x} ${y}) scale(1.25)"><circle r="21" fill="${p.farbe}"/><circle r="21" fill="url(#ru-glanz)"/>${p.zeichen}</g><text x="${x + 36}" y="${y - 2}" font-family="var(--grotesk)" font-weight="700" font-size="19" fill="var(--ru-text)">${esc(p.name)}</text><text x="${x + 36}" y="${y + 19}" font-family="var(--grotesk)" font-weight="500" font-size="15" fill="var(--ru-leise)">${p.ideen.length} tragende Ideen</text></a>`; }).join('');
    const rw = bahnR(7) - 10, kx = cx + Math.sqrt(rw * rw - 250 * 250);
    return `<div class="ru-system"><svg viewBox="0 0 1100 600" role="img" aria-label="Sonnensystem: die Sonne mit 14 Rechenregeln, darum sieben Gebiete, außen die Arbeitsweisen">
      <defs><radialGradient id="ru-sonnenlicht" cx="0" cy=".5" r="1"><stop offset="0" stop-color="#FFD23F" stop-opacity=".35"/><stop offset="1" stop-color="#FFD23F" stop-opacity="0"/></radialGradient></defs>
      <circle cx="${cx}" cy="${cy}" r="${rs + 120}" fill="url(#ru-sonnenlicht)"/>
      <a href="${Z('sonne')}" class="ru-sp ru-sp-sonne"><circle cx="${cx}" cy="${cy}" r="${rs}" fill="var(--s4)"/><circle cx="${cx}" cy="${cy}" r="${rs - 64}" fill="var(--s3)"/><circle cx="${cx}" cy="${cy}" r="${rs - 128}" fill="var(--s2)"/><circle cx="${cx}" cy="${cy}" r="${rs - 192}" fill="var(--s1)"/>
        <text x="22" y="${cy - 14}" font-family="var(--grotesk)" font-weight="700" font-size="15" fill="#11161D">Die Sonne · die Grundlage</text><text x="22" y="${cy + 17}" font-family="var(--grotesk)" font-weight="700" font-size="28" fill="#11161D">14 Rechenregeln</text><text x="22" y="${cy + 41}" font-family="var(--grotesk)" font-weight="500" font-size="15" fill="#11161D">in vier Schichten</text></a>
      ${pl}
      <path d="${weg(rw)}" fill="none" stroke="var(--ru-leise)" stroke-width="2" stroke-dasharray="6 6"/>
      <a href="${Z('weisen')}" class="ru-sp"><rect x="${kx - 30}" y="${cy + 238}" width="230" height="56" rx="28" fill="var(--ru-flaeche)" stroke="var(--ru-leise)" stroke-width="2" stroke-dasharray="6 5"/><text x="${kx + 85}" y="${cy + 262}" text-anchor="middle" font-family="var(--grotesk)" font-weight="700" font-size="18" fill="var(--ru-text)">8 Arbeitsweisen</text><text x="${kx + 85}" y="${cy + 282}" text-anchor="middle" font-family="var(--grotesk)" font-size="14" fill="var(--ru-leise)">gelten überall</text></a></svg></div>`;
  }

  // Ebene 1: die Sonne – die 14 Rechenregeln in vier Schichten (Name, Band, Merksatz)
  function sichtSonne() {
    const schichten = [1, 2, 3, 4].map((nr) => `<li class="ru-schicht ru-s${nr}"><div class="ru-schicht-kopf" id="ru-schicht-${nr}">${ringBild(nr)}<span class="ru-sk-nr">Schicht ${nr}</span><b>${esc(ETAGE[nr])}</b>${ae('Schicht', nr, ETAGE[nr], 'name')}</div><ul class="ru-zeilen">${D.regeln.filter((r) => r.etage === nr).map((r) => `<li><a class="ru-zeile ru-mit-satz" href="${Z(adr.regel(r.id))}"><span class="ru-z-nr">${r.nr}</span><span class="ru-z-text"><span class="ru-z-name">${esc(r.name)}</span><span class="ru-z-merk">${satzZeile(r.satz)}</span></span>${band(r.id)}</a></li>`).join('')}</ul></li>`).join('');
    return `<div class="ru-breite ru-schmal ru-start">${elternBand()}${pfad()}<header class="ru-e-kopf"><span class="ru-s0-mini" aria-hidden="true"></span><div><p class="ru-ueber">Die Sonne</p><h1>14 Rechenregeln</h1></div></header>${aufEinenBlick('Sonne')}
      <p class="ru-lead">In vier Schichten, von den Grundlagen nach außen. Die Schichten ordnen, sie sperren nichts.</p>${sonnenSchnitt()}
      ${LEGENDE}<ol class="ru-schichten">${schichten}</ol>
      <a class="ru-verweis ru-weiter" href="${Z('klassen')}">Dieselben Regeln durch die Klassen ›</a></div>`;
  }
  // Ebene 1: ein Gebiet – seine tragenden Ideen mit Merksatz und Band
  function sichtGebiet(name) {
    const p = PLANET[name], n = PLANETEN.indexOf(p), vor = PLANETEN[n - 1], nach = PLANETEN[n + 1];
    return `<div class="ru-breite ru-schmal ru-start">${elternBand()}${pfad()}<header class="ru-e-kopf">${planetScheibe(p.name, 48)}<div><p class="ru-ueber">Gebiet ${n + 1} von 7</p><h1>${esc(p.name)}</h1></div></header>${aufEinenBlick(p.name)}
      <p class="ru-lead">${p.ideen.length} tragende Ideen. Hinter ihnen stehen ${I.zahlGesetze(p)} einzelne Regeln und Formeln.</p>${aeZeile(ae('Gebiet', p.kuerzel, p.name, 'name und Ideen'))}${LEGENDE}
      <ol class="ru-ideen1">${p.ideen.map((i) => `<li><a class="ru-idee1" href="${Z(adr.idee(i.id))}"><span class="ru-z-nr">${i.nr}</span><span class="ru-i1-text"><span class="ru-i1-name">${esc(i.kurz)}</span><span class="ru-i1-satz">${i.satz}</span></span>${band(i.id)}</a></li>`).join('')}</ol>
      ${blaettern(vor && { href: Z(adr.gebiet(vor.name)), ueber: 'Gebiet ' + n, name: vor.name }, nach && { href: Z(adr.gebiet(nach.name)), ueber: 'Gebiet ' + (n + 2), name: nach.name })}</div>`;
  }
  // Ebene 1: die acht Arbeitsweisen
  function sichtWeisen() {
    return `<div class="ru-breite ru-schmal ru-start">${elternBand()}${pfad()}<header class="ru-e-kopf"><span class="ru-w-zeichen ru-gross" aria-hidden="true"></span><div><p class="ru-ueber">Arbeitsweisen</p><h1>8 Arbeitsweisen</h1></div></header>
      <p class="ru-lead">Keine Rechenregeln, sondern wie man vorgeht. Sie gelten in jedem Gebiet.</p>
      <ol class="ru-ideen1">${D.arbeitsweisen.map((a, n) => `<li><a class="ru-idee1" href="${Z(adr.weise(n + 1))}"><span class="ru-z-nr">${n + 1}</span><span class="ru-i1-text"><span class="ru-i1-name">${esc(a.name)}</span><span class="ru-i1-satz">${a.satz}</span></span></a></li>`).join('')}</ol></div>`;
  }

  // ---------- Durch die Klassen: Handy eine Klasse, Rechner die Tabelle ----------
  const beispielIn = (id, k) => LEITER[id].stufen.find((s) => s.klasse === k);
  const rechnungIn = (s) => (s && s.text ? `<span class="ru-rechnung">${mkText(s.text, s.pos, 0, s.text.length)}</span>` : '');
  function sichtKlassen() {
    const KLASSE = zustand.klasse;
    const wahl = `<div class="ru-klassenwahl" role="group" aria-label="Klasse wählen"><span class="ru-kw-text">Klasse</span>${KL.map((k) => `<a href="${Z('klassen-' + k)}"${k === KLASSE ? ' aria-current="true"' : ''}>${k}</a>`).join('')}</div>`;
    const liste = [1, 2, 3, 4].map((nr) => `<li class="ru-schicht ru-s${nr}"><div class="ru-schicht-kopf"><span class="ru-sk-nr">Schicht ${nr}</span><b>${esc(ETAGE[nr])}</b></div><ul class="ru-kzeilen">${D.regeln.filter((r) => r.etage === nr).map((r) => { const s = beispielIn(r.id, KLASSE);
      return `<li><a class="ru-kzeile${s && s.text ? '' : ' ru-leer'}" href="${Z(adr.regel(r.id))}"><span class="ru-z-nr">${r.nr}</span><span class="ru-kz-name">${esc(r.name)}</span>${s && s.text ? `${rechnungIn(s)}<span class="ru-kz-art">${s.art}</span>` : `<span class="ru-kz-leer">kommt in Klasse ${KLASSE} nicht vor</span>`}</a></li>`; }).join('')}</ul></li>`).join('');
    const ideen = PLANETEN.map((p) => { const da = p.ideen.filter((i) => (beispielIn(i.id, KLASSE) || {}).text); return da.length ? `<li><p class="ru-ki-gebiet">${planetScheibe(p.name, 22)}${esc(p.name)}</p><ul class="ru-kzeilen">${da.map((i) => `<li><a class="ru-kzeile" href="${Z(adr.idee(i.id))}"><span class="ru-z-nr">${i.nr}</span><span class="ru-kz-name">${esc(i.kurz)}</span>${rechnungIn(beispielIn(i.id, KLASSE))}</a></li>`).join('')}</ul></li>` : ''; }).join('');
    const tafel = `<div class="ru-tafel-wrap"><table class="ru-tafel"><thead><tr><th class="ru-r" scope="col">Rechenregel</th>${KL.map((k) => `<th scope="col">Klasse ${k}</th>`).join('')}</tr></thead><tbody>${[1, 2, 3, 4].map((nr) => `<tr class="ru-t-schicht ru-s${nr}"><th colspan="7">Schicht ${nr} · ${esc(ETAGE[nr])}</th></tr>${D.regeln.filter((r) => r.etage === nr).map((r) => `<tr><th class="ru-r" scope="row"><a href="${Z(adr.regel(r.id))}"><span class="ru-z-nr">${r.nr}</span> ${esc(r.name)}</a></th>${KL.map((k) => { const ss = LEITER[r.id].stufen.filter((x) => x.klasse === k && x.text); return ss.length ? `<td>${ss.map(rechnungIn).join('<br>')}</td>` : '<td class="ru-nicht">–</td>'; }).join('')}</tr>`).join('')}`).join('')}</tbody></table></div>`;
    return `<div class="ru-breite ru-schmal ru-start ru-klassen-ansicht">${elternBand()}${pfad('<span>Durch die Klassen</span>')}<h1 class="ru-titel">Durch die Klassen</h1><p class="ru-lead">Dieselben 14 Rechenregeln in Klasse 5 bis 10.</p>${umschalter('klassen')}
      <div class="ru-handy-teil"><p class="ru-erkl">Wähle eine Klasse. Zu jeder Regel steht ihr Beispiel aus dieser Klasse; gelb umrahmt ist die Stelle, an der die Regel wirkt.</p>${wahl}
        <ol class="ru-schichten">${liste}</ol>
        <details class="ru-gebiet ru-ideen-klasse"><summary><span class="ru-g-name">Tragende Ideen in Klasse ${KLASSE}</span><span class="ru-st-hinweis">${IDEEN.filter((i) => (beispielIn(i.id, KLASSE) || {}).text).length}</span>${CHEVRON}</summary><ul class="ru-ki-liste">${ideen}</ul></details>
        <p class="ru-hinweis-klein">Eine Regel durch alle Klassen: Regel antippen, dann „Dieselbe Regel in Klasse …“.</p></div>
      <div class="ru-rechner-teil"><p class="ru-erkl">Jede Zeile eine Rechenregel, jede Spalte eine Klasse. Gelb umrahmt: die Stelle, an der die Regel wirkt – in jeder Klasse dieselbe.</p>${tafel}</div></div>`;
  }

  // ---------- Regelseite (gestuft) ----------
  function aufbauInhalt(rid) {
    const weg = I.erklaertUeber(rid), hilft = I.hilftBei(rid), traegt = I.regelTraegt(rid);
    let s = '';
    if (weg.length) s += `<h3 class="ru-ueber">Lässt sich erklären über</h3><div class="ru-verweise">${weg.map(verweisRegel).join('')}</div>`;
    if (hilft.length) s += `<h3 class="ru-ueber">Hilft beim Erklären von</h3><div class="ru-verweise">${hilft.map(verweisRegel).join('')}</div>`;
    if (weg.length || hilft.length) s += '<p class="ru-klein ru-leise">Zum Erklären hilfreich – keine Lernvoraussetzung und keine Sperre.</p>';
    if (traegt.length) s += `<h3 class="ru-ueber">Darauf bauen auf: ${traegt.reduce((a, x) => a + x.n, 0)} Regeln in ${new Set(traegt.map((x) => x.i.planet)).size} Gebieten</h3><div class="ru-verweise">${traegt.map((x) => `<a class="ru-verweis" href="${Z(adr.idee(x.i.id))}"><span class="ru-nr">${esc(x.i.planet)}</span>${esc(x.i.kurz)} <span class="ru-leise">(${x.n})</span></a>`).join('')}</div>`;
    return s || '<p class="ru-leise">Keine Verweise hinterlegt.</p>';
  }
  const aufbauZahl = (rid) => I.erklaertUeber(rid).length + I.hilftBei(rid).length + I.regelTraegt(rid).length;
  function genauInhalt(x, id, w) {
    const rest = id ? I.felder(id).slice(1) : [], h = (t, feld) => aeKopf(`<h3 class="ru-ueber">${t}</h3>`, aeW(w, feld));
    return `${x.genau ? `${h('Genau gesagt', 'genau')}<p class="ru-fliess">${x.genau}</p>` : ''}${x.warum ? `${h('Warum das gilt', 'warum')}<p class="ru-fliess">${x.warum}</p>` : ''}${x.voraus ? `${h('Wann sie gilt – und wann nicht', 'voraus')}<p class="ru-fliess">${x.voraus}</p>` : ''}
      ${rest.length ? `<h3 class="ru-ueber">Weitere Bilder (${rest.length})</h3>${felderHtml(rest, w, id, 2)}` : ''}${x.verwandt ? `${h('Verwandt', 'verwandt')}<p class="ru-fliess">${x.verwandt}</p>` : ''}`;
  }
  const vergleichInhalt = (id, w) => `<p class="ru-band-zeile">${band(id, { gross: 1 })}</p>${LEGENDE}<p class="ru-markiert"><b>Gelb umrahmt, in jeder Klasse an derselben Stelle:</b> ${esc(LEITER[id].markiert)}</p>${klassenLeiter(id, w)}`;
  const kurzZeile = (w, text) => `<p class="ru-kurz">${esc(text)}</p>${aeZeile(aeW(w, 'kurz'))}`;
  const bspKopf = (w) => aeKopf('<p class="ru-ueber">Beispiel</p>', aeW(w, 'beispiel'));
  const regelKopf = (r, w) => `<header class="ru-r-kopf"><p class="ru-ueber ru-mit-ring">${ringBild(r.etage, 26)}Rechenregel ${r.nr} von 14 · Schicht ${r.etage}</p><h1>${esc(r.name)}</h1>${kurzZeile(w, KURZ[r.id] || '')}</header>`;
  function sichtRegel(id) {
    const r = REGEL[id], n = r.nr, vor = REGEL['R' + (n - 1)], nach = REGEL['R' + (n + 1)], w = wer.regel(id);
    return `<article class="ru-breite ru-schmal ru-regelseite">${elternBand(id)}${pfad(`<a href="${Z('sonne')}">Sonne</a>`, `<span>Schicht ${r.etage}</span>`)}${regelKopf(r, w)}${merksatz(r.satz, aeW(w, 'satz'))}
      <section class="ru-bsp">${bspKopf(I.felder(id)[0] ? null : w)}${beispiel(id, w)}</section>${tafelVerweis([id])}
      <div class="ru-stufen">${stufe('klassen', `Dieselbe Regel in ${I.spanneText(id)}`, band(id), vergleichInhalt(id, w), VERGLEICH_OFFEN)}
      ${stufe('genau', 'Genau erklärt', 'warum · wann', genauInhalt(r, id, w))}
      ${stufe('fehler', 'Typische Fehler', fehlerTeile(r.fehler).length + '', aeZeile(aeW(w, 'fehler')) + fehlerListe(r.fehler))}
      ${stufe('aufbau', 'Worauf sie aufbaut, was auf ihr aufbaut', aufbauZahl(id) + '', aeZeile(aeW(w, 'weg (Aufbau, Verweise)')) + aufbauInhalt(id))}</div>${erwBlock(w)}
      ${blaettern(vor && { href: Z(adr.regel(vor.id)), ueber: 'Regel ' + vor.nr, name: vor.name }, nach && { href: Z(adr.regel(nach.id)), ueber: 'Regel ' + nach.nr, name: nach.name })}</article>`;
  }
  // ---------- Seite einer tragenden Idee ----------
  function sichtIdee(id) {
    const i = IDEE[id], k = IDEEN.indexOf(i), vor = IDEEN[k - 1], nach = IDEEN[k + 1], braucht = I.ideeBraucht(i), w = wer.idee(id);
    const folge = `<ol class="ru-folge">${i.gesetze.map((gid) => { const g = GESETZ[gid]; return `<li><a class="ru-karte" href="${Z(adr.gesetz(gid))}"><span class="ru-f-name"><span class="ru-nr">${gid}</span> ${esc(g.name)}</span><span class="ru-f-satz">${g.satz}</span></a></li>`; }).join('')}</ol>`;
    return `<article class="ru-breite ru-schmal ru-regelseite">${elternBand()}${pfad(`<a href="${Z(adr.gebiet(i.planet))}">${esc(i.planet)}</a>`)}
      <header class="ru-r-kopf"><p class="ru-ueber">${esc(i.planet)} · tragende Idee ${i.nr} von ${i.von}</p><h1>${esc(i.kurz)}</h1>${kurzZeile(w, KURZ[id] || '')}</header>${merksatz(i.satz, aeW(w, 'satz'))}
      <section class="ru-bsp">${bspKopf(I.felder(id)[0] ? null : w)}${beispiel(id, w)}</section>${tafelVerweis([id, ...i.gesetze])}
      <div class="ru-stufen">${stufe('klassen', LEITER[id].klassen.length > 1 ? `Dieselbe Idee in ${I.spanneText(id)}` : `Kommt nur in Klasse ${LEITER[id].klassen[0]} vor`, band(id), vergleichInhalt(id, w), VERGLEICH_OFFEN)}
      ${stufe('genau', 'Genau erklärt', 'warum', genauInhalt(i, id, w))}
      ${stufe('folge', 'Die Regeln und Formeln dahinter', i.gesetze.length + '', aeZeile(aeW(w, 'gesetze (Auswahl, Reihenfolge)')) + folge)}
      ${stufe('aufbau', 'Worauf sie aufbaut', braucht.length + '', braucht.length ? `<h3 class="ru-ueber">Benutzt diese Rechenregeln</h3><div class="ru-verweise">${braucht.map(verweisRegel).join('')}</div>` : '<p class="ru-leise">Keine Rechenregel hinterlegt.</p>')}</div>${erwBlock(w)}
      ${blaettern(vor && { href: Z(adr.idee(vor.id)), ueber: vor.planet === i.planet ? 'Idee ' + vor.nr : esc(vor.planet), name: vor.kurz }, nach && { href: Z(adr.idee(nach.id)), ueber: nach.planet === i.planet ? 'Idee ' + nach.nr : esc(nach.planet), name: nach.kurz })}</article>`;
  }
  // ---------- Seite einer Arbeitsweise (achte Runde: Kurzbeschreibung, Beispiel, Erklärung vom Mathe-Profi; „Noch offen“ entfällt) ----------
  function sichtWeise(n) {
    const a = D.arbeitsweisen[n - 1], vor = D.arbeitsweisen[n - 2], nach = D.arbeitsweisen[n], w = wer.weise(n);
    return `<article class="ru-breite ru-schmal ru-regelseite">${elternBand()}${pfad(`<a href="${Z('weisen')}">Arbeitsweisen</a>`)}
      <header class="ru-r-kopf"><p class="ru-ueber">Arbeitsweise ${n} von 8 · gilt in jedem Gebiet</p><h1>${esc(a.name)}</h1>${kurzZeile(w, a.kurz)}</header>${merksatz(a.satz, aeW(w, 'satz'))}
      <section class="ru-bsp">${bspKopf(w)}<p class="ru-fliess ru-bsp-text">${esc(a.beispiel.text)}</p><p class="ru-kl">Klasse ${a.beispiel.klasse}</p></section>
      <div class="ru-stufen">${stufe('genau', 'Genau erklärt', 'wann · worauf achten', aeZeile(aeW(w, 'erklaerung')) + `<p class="ru-fliess">${esc(a.erklaerung)}</p>`)}</div>${erwBlock(w)}
      ${blaettern(vor && { href: Z(adr.weise(n - 1)), ueber: 'Arbeitsweise ' + (n - 1), name: vor.name }, nach && { href: Z(adr.weise(n + 1)), ueber: 'Arbeitsweise ' + (n + 1), name: nach.name })}</article>`;
  }
  // ---------- Ebene 3: einzelne Regel eines Gebiets ----------
  function sichtGesetz(id) {
    const g = GESETZ[id], i = I.ideeVon(id), br = I.brauchtRegeln(g), k = g.klassen || [], w = wer.gesetz(id);
    const bsp = g.beispiel ? `<p class="ru-fliess ru-bsp-text">${esc(g.beispiel)}</p>` : k.length ? `<p class="ru-rechnung ru-gross-r">${esc(k[0].text)}</p><p class="ru-kl">Klasse ${k[0].klasse} · ${k[0].art}</p>` : '';
    return `<article class="ru-breite ru-schmal ru-regelseite">${elternBand()}${pfad(PLANET[g.planet] ? `<a href="${Z(adr.gebiet(g.planet))}">${esc(g.planet)}</a>` : `<span>${esc(g.planet)}</span>`, i ? `<a href="${Z(adr.idee(i.id))}">${esc(i.kurz)}</a>` : '')}
      <header class="ru-r-kopf"><p class="ru-ueber">Regel ${id} · ${esc(I.klasseVon(g))}</p><h1>${esc(g.name)}</h1>${aeZeile(aeW(w, 'name'))}</header>${merksatz(g.satz, aeW(w, 'satz'))}
      ${bsp ? `<section class="ru-bsp">${bspKopf(w)}${bsp}</section>` : ''}${tafelVerweis([id])}
      <div class="ru-stufen">${k.length > 1 || (g.beispiel && k.length) ? stufe('klassen', 'In den Klassen', k.length + '', beispielListe(k, w)) : ''}
      ${g.warum || g.voraus || g.genau ? stufe('genau', 'Genau erklärt', 'warum · wann', genauInhalt(g, '', w)) : ''}
      ${g.fehler ? stufe('fehler', 'Typische Fehler', fehlerTeile(g.fehler).length + '', aeZeile(aeW(w, 'fehler')) + fehlerListe(g.fehler)) : ''}
      ${stufe('aufbau', 'Worauf sie aufbaut', (br.length + (i ? 1 : 0)) + '', `${i ? `<h3 class="ru-ueber">Folgt aus der tragenden Idee</h3><div class="ru-verweise"><a class="ru-verweis" href="${Z(adr.idee(i.id))}"><span class="ru-nr">${esc(i.planet)}</span>${esc(i.kurz)}</a></div>` : ''}${br.length ? `<h3 class="ru-ueber">Benutzt diese Rechenregeln</h3><div class="ru-verweise">${br.map(verweisRegel).join('')}</div>` : ''}`)}</div>
      ${bsp || g.warum || g.voraus ? '' : '<div class="ru-z-folgt"><p>Für diese Regel liegen bisher Name, Satz und Klasse vor.</p></div>'}${erwBlock(w)}</article>`;
  }

  // ---------- Suche ----------
  function sichtSuche() {
    const FRAGE = zustand.frage, tr = I.suche(FRAGE);
    return `<div class="ru-breite ru-schmal ru-start">${elternBand()}${pfad('<span>Suche</span>')}<h1 class="ru-s-titel">${!FRAGE ? 'Suche' : tr.length ? `${tr.length} Treffer für „${esc(FRAGE)}“` : `Nichts gefunden für „${esc(FRAGE)}“`}</h1>
      ${tr.length ? '' : '<p class="ru-leise ru-s-tipp">Versuch ein einzelnes Wort, zum Beispiel „Kegel“, „Prozent“ oder „Klammer“.</p>'}
      <ol class="ru-treffer">${tr.map((e) => `<li><a class="ru-karte" href="${Z(e.ziel)}"><span class="ru-t-ort">${esc(e.ort)}</span><span class="ru-t-name"><span class="ru-nr">${e.art}</span> ${esc(e.name)}</span>${e.ueber ? `<span class="ru-t-stich">Stichwort „${esc(e.ueber)}“ steht hier</span>` : ''}<span class="ru-t-satz">${e.satz}</span></a>${aeZeile(e.ueber ? ae('Stichwort', 'zu ' + e.ae[1], e.ueber, 'wort') : ae(e.ae[0], e.ae[1], e.name, `Treffer der Suche „${FRAGE}“`))}</li>`).join('')}</ol></div>`;
  }

  // ---------- Eltern und Lehrer: Liste aller Regeln (regeln-lehrer.md Regel 1) ----------
  function sichtListe() {
    const zeile = (href, nr, name, satz, art) => `<li><a class="ru-lz" href="${href}"><span class="ru-z-nr">${nr}</span><span class="ru-lz-text"><b>${esc(name)}</b><span>${satz}</span></span><span class="ru-lz-art">${art} ›</span></a></li>`;
    const sonne = [1, 2, 3, 4].map((nr) => `<h3 class="ru-ueber ru-lz-schicht">${ringBild(nr, 22)}Schicht ${nr} · ${esc(ETAGE[nr])}</h3><ul class="ru-lz-liste">${D.regeln.filter((r) => r.etage === nr).map((r) => zeile('#/regeln/' + adr.lehrer(r.id), r.nr, r.name, satzZeile(r.satz), 'Blatt')).join('')}</ul>`).join('');
    const gebiete = PLANETEN.map((p, n) => `<h3 class="ru-ueber ru-lz-schicht">${planetScheibe(p.name, 22)}Gebiet ${n + 1} · ${esc(p.name)}</h3><ul class="ru-lz-liste">${p.ideen.map((i) => zeile(Z(adr.idee(i.id)), i.nr, i.kurz, i.satz, 'Seite des Kindes')).join('')}</ul>`).join('');
    const weisen = `<ul class="ru-lz-liste">${D.arbeitsweisen.map((a, n) => zeile(Z(adr.weise(n + 1)), n + 1, a.name, a.satz, 'Seite des Kindes')).join('')}</ul>`;
    return `<div class="ru-breite ru-schmal ru-start ru-lehrer"><div class="ru-lehrer-band"><span>Eltern und Lehrer</span><a class="ru-verweis" href="${Z('universum')}">So sieht es das Kind ›</a></div>
      <h1 class="ru-titel ru-lz-titel">Regeln</h1><p class="ru-lead">Alle festen Regeln der Lern-App, Klasse 5 bis 10: 14 Rechenregeln (die Sonne), 28 tragende Ideen in sieben Gebieten und 8 Arbeitsweisen. Je Rechenregel gibt es ein Blatt mit Erklärung, Lehrplan-Bezug und Rückmeldung.</p>
      <section class="ru-l-abschnitt"><h2>Rechenregeln (14)</h2>${sonne}</section>
      <section class="ru-l-abschnitt"><h2>Tragende Ideen der Gebiete (28)</h2><p class="ru-klein ru-leise">Stufe 1: Für die Ideen gibt es noch kein eigenes Blatt; der Verweis öffnet die Seite des Kindes (mit Erklärung, Klassen und den Regeln dahinter).</p>${gebiete}</section>
      <section class="ru-l-abschnitt"><h2>Arbeitsweisen (8)</h2>${weisen}</section>
      ${I.TAFELN.length ? `<section class="ru-l-abschnitt"><h2>Tafeln zum Nachschlagen (${I.TAFELN.length})</h2><ul class="ru-lz-liste">${I.TAFELN.map((t, n) => zeile(Z(adr.tafel(t.id)), n + 1, t.titel, esc(t.kurz), 'Tafel')).join('')}</ul></section>` : ''}</div>`;
  }

  // ---------- Eltern und Lehrer: Blatt einer Rechenregel (regeln-lehrer.md Regel 2, alle Abschnitte offen) ----------
  function sichtLehrer(id) {
    const r = REGEL[id], L = LEHRER[id], kl = L.klassen || {}, liste = (a) => (a && a.length ? a.join(', ') : '–'), lp = L.lehrplan, e = lp ? lp.einfuehrung : {}, w = wer.regel(id);
    const rueck = (abschnitt) => aeW(w, 'Abschnitt ' + abschnitt);
    const lpTab = `<table class="ru-lp"><thead><tr><th scope="col">Schulart</th><th scope="col">Eingeführt in</th><th scope="col">Kommt vor in</th></tr></thead><tbody>
      <tr><td>Gymnasium Bayern</td><td>${e.klasse_gymnasium ? `Klasse ${e.klasse_gymnasium}<br><span class="ru-leise">${esc(e.lernbereich_gymnasium)}</span>` : '–'}</td><td>${liste(kl.gym_by)}</td></tr>
      <tr><td>Realschule Bayern</td><td>${e.realschule_klasse ? `Klasse ${e.realschule_klasse}<br><span class="ru-leise">${esc(e.lernbereich_realschule)}</span>` : '–'}</td><td>${liste(kl.rs_by)}</td></tr>
      <tr><td>IB MYP (Jahr)</td><td>${e.ib_myp_jahr ? `Jahr ${e.ib_myp_jahr}<br><span class="ru-leise">${esc(e.lernbereich_ib)}</span>` : '–'}</td><td>${liste(kl.ib_myp)}</td></tr></tbody></table>`;
    const lpMehr = lp ? `${(e.lehrplan_stichworte_gymnasium || []).length ? `<p class="ru-klein ru-lp-zeile"><b>Stichworte im Lehrplan (Gymnasium, Thema ${esc(e.titel)}):</b> ${e.lehrplan_stichworte_gymnasium.map(esc).join(' · ')}</p>` : ''}
      <ul class="ru-lp-klassen">${lp.klassen.map((k) => `<li><span class="ru-stufe-k">${k.klasse}</span><span>${esc(k.art)} · ${esc(I.thema(k.thema))}<br><span class="ru-leise">${esc(k.lernbereich_gymnasium || '')}</span></span></li>`).join('')}</ul>
      <p class="ru-klein ru-leise">${esc(lp.befund)} <b>Nicht geprüft:</b> ${lp.nicht_geprueft.map(esc).join('; ')}. Quelle: Mathe-Profi (texte8/lehrplan.json, Stand 27.11.2026) aus themenliste.json und der Lehrplan-Kopie der App.</p>` : '<p class="ru-klein ru-leise"><b>Nicht geprüft:</b> kein Lehrplan-Bezug hinterlegt.</p>';
    const themen = `<ul class="ru-lverweise">${L.themen.map((t) => `<li><span>${esc(t.ort ? t.ort + ' · ' + t.titel : t.titel)}</span><span class="ru-lv-knoepfe"><a class="ru-verweis ru-klein-v" href="#/lehrplan"${t.thema_id ? ` data-thema-id="${t.thema_id}"` : ''}>Lehrer-Seite ›</a>${ae('Thema', t.schluessel || '', t.titel, 'Zuordnung zu Rechenregel ' + id)}</span></li>`).join('')}</ul>`;
    const aufg = L.aufgaben.length ? `<ol class="ru-aufgaben">${L.aufgaben.map((a) => `<li><p class="ru-a-kopf">${esc(a.kopf)}</p><p>${esc(a.text)}</p>${a.auswahl ? `<p class="ru-leise">Auswahl: ${a.auswahl.map(esc).join(' · ')}</p>` : ''}<p><b>Lösung:</b> ${esc(a.loesung)}</p>${a.weg ? `<p class="ru-leise">${esc(a.weg)}</p>` : ''}</li>`).join('')}</ol>` : '<p class="ru-leise">Noch keine passende Aufgabe dieser Regel zugeordnet.</p>';
    const zuo = L.zuordnung ? `<p class="ru-klein ru-zuordnung"><b>Zuordnung ${L.zuordnung.befund === 'passt nicht' ? 'passt nicht' : 'nur teilweise geprüft'} (Stichprobe des Mathe-Profis):</b> ${esc(L.zuordnung.text)}</p>` : '';
    const fb = L.fehlbilder.length ? `<ul class="ru-fehlerliste">${L.fehlbilder.map((f) => `<li>${esc(f.beschreibung)} <span class="ru-kl">${esc(f.kennung)}</span></li>`).join('')}</ul>` : '<p class="ru-leise">Keine Fehlbilder hinterlegt.</p>';
    const ab = (t, inhalt, knopf) => `<section class="ru-l-abschnitt"><div class="ru-l-kopf"><h2>${t}</h2>${knopf || ''}</div>${inhalt}</section>`;
    const n = r.nr, vor = REGEL['R' + (n - 1)], nach = REGEL['R' + (n + 1)];
    return `<article class="ru-breite ru-schmal ru-regelseite ru-lehrer"><div class="ru-lehrer-band"><span>Eltern und Lehrer</span><a class="ru-verweis" href="${Z(adr.regel(id))}">So sieht es das Kind ›</a></div>
      <nav class="ru-pfad" aria-label="Brotkrumen"><a href="#/regeln">‹ Regeln</a><span class="ru-t">›</span><span>Schicht ${r.etage} · ${esc(ETAGE[r.etage])}</span></nav>${regelKopf(r, w)}
      <p class="ru-klein ru-leise ru-kennung">Kennung ${esc(L.kennung)}</p>
      ${ab('1 Merksatz', merksatz(r.satz) + '<p class="ru-klein ru-leise">Wörtlich wie auf der Seite des Kindes.</p>', rueck('Merksatz'))}
      ${ab('2 Was das Kind sieht', `<p class="ru-ueber">Beispiel</p>${beispiel(id, w)}<p class="ru-ueber ru-abstand">Dieselbe Regel in ${I.spanneText(id)}</p>${vergleichInhalt(id, w)}<p class="ru-ueber ru-abstand">Typische Fehler</p>${fehlerListe(r.fehler)}`, rueck('Karte'))}
      ${ab('3 Fachliche Erklärung', genauInhalt(r, id, w), rueck('Erklärung'))}
      ${ab('4 Verweise und Zuordnung', `<h3 class="ru-ueber">Lehrplan</h3>${lpTab}${lpMehr}<h3 class="ru-ueber">In der App: Themen, die diese Regel üben</h3>${themen}<h3 class="ru-ueber">Beispielaufgaben mit Lösung</h3>${zuo}${aufg}<h3 class="ru-ueber">Fehlbilder, die die App dieser Regel zuordnet</h3>${fb}<h3 class="ru-ueber">Aufbau</h3>${aufbauInhalt(id)}`, rueck('Zuordnung'))}
      ${erwBlock(w)}
      ${ab('5 Stand je Kind', '<p class="ru-leise">Stand folgt (kommt mit Stufe 2, sobald der Server ihn liefert).</p>')}
      ${blaettern(vor && { href: '#/regeln/' + adr.lehrer(vor.id), ueber: 'Regel ' + vor.nr, name: vor.name }, nach && { href: '#/regeln/' + adr.lehrer(nach.id), ueber: 'Regel ' + nach.nr, name: nach.name })}</article>`;
  }

  // ===================== Tafeln zum Nachschlagen =====================
  // Vorgabe: inhalte/design/tafeln/entwurf1/umsetzung1.md, Kurskorrektur des Nutzers (27.11.): zuerst die Schnellübersicht als Matrix, Einzelheiten beim Antippen.
  // Bausteine (alle Klassen ru-tafel-…, Optik nur in lernen-regeln.css): Karte, Matrix (eigener Rollbereich, erste Spalte fest, Zeile klappt auf), Aufklapper, Kette.
  const { TAFEL } = I;
  let tfNr = 0;
  // Zahlen deutsch: Tausender mit geschütztem Leerzeichen, Dezimalkomma („3,6“, nicht „3.6“; Auflagen aus Werkstatt 1152)
  const tfZahl = (n) => { const [g, d] = String(n).split('.'); return g.replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + (d ? ',' + d : ''); };
  // Text der Vorschläge mit geschütztem Leerzeichen in Zahlen und vor Einheiten („3 500 m“ bricht nicht um; einheiten/vorschlag.md, Abschnitt 5.6)
  const nb = (s) => esc(s).replace(/(\d) (?=\d{3}(?!\d))/g, '$1 ').replace(/(\d) (?=(?:[A-Za-zµ²³/]{1,6}|€|%|°)(?![A-Za-zäöüß]))/g, '$1 ');
  // Formel mit Umbruchstellen nur vor Rechenzeichen außerhalb von Klammern (auf dem Handy zwei, drei Zeilen statt waagrecht rollen)
  function formel(text) {
    // Formel aus Wörtern („Summe aller Werte : Anzahl“) bricht wie Text um
    const [l, ...r] = String(text).split(' = '); if (!r.length || !/ [·+−:] /.test(r.join(' = ')) || /[A-Za-zäöüß]{4,}/.test(r.join(' = '))) return nb(text);
    const gruppen = [], toks = r.join(' = ').split(' '); let g = '', tiefe = 0;
    for (const tk of toks) { const op = /^[·+−:=<>≤≥-]$/.test(tk);
      if (g && op && (g + ' ' + tk).length > (tiefe ? 12 : 8)) { gruppen.push(g); g = tk; } else g = g ? g + ' ' + tk : tk;
      tiefe += (tk.match(/\(/g) || []).length - (tk.match(/\)/g) || []).length; }
    if (g) gruppen.push(g);
    return [l + ' = ' + gruppen[0], ...gruppen.slice(1)].map((x) => `<span class="ru-tafel-fg">${nb(x)}</span>`).join(' ');
  }
  // Mini-Zeichnung in der ersten Spalte: ohne Beschriftung (zu klein zum Lesen), die volle Zeichnung steht in den Einzelheiten
  const miniSvg = (x) => x.replace('<svg ', '<svg class="ru-tafel-mini" aria-hidden="true" ').replace(/ role="img" aria-label="[^"]*"/, '').replace(/<text[^>]*>[^<]*<\/text>/g, '');
  const tfKl = (kl) => `<span class="ru-tafel-kl">${kl ? 'ab Kl. ' + kl : 'Kl. offen'}</span>`;
  const dkl = (kl) => (kl != null ? ` data-kl="${kl}"` : '');
  const tfErw = (t) => (ERW && t ? `<p class="ru-tafel-erw"><b>Für Eltern:</b> ${esc(t)}</p>` : '');
  const tfMerk = (t) => (t ? `<p class="ru-tafel-merk">${nb(t)}</p>` : '');
  const tfListe = (a, tag = 'ul') => (a && a.length ? `<${tag} class="ru-tafel-liste">${a.map((x) => `<li>${nb(x)}</li>`).join('')}</${tag}>` : '');
  const tfH3 = (t) => `<h3 class="ru-tafel-h3">${t}</h3>`;
  const tfBruch = (b) => { const [z, n] = String(b).split('/'); return n ? `<span class="ru-br" aria-label="${esc(b)}"><i>${esc(z)}</i><i>${esc(n)}</i></span>` : esc(b); };
  // „Warum?“: Verweise auf Regeln, Ideen und Einzelregeln des Universums
  const tfRegeln = (kenn) => { const z = [...new Set(kenn.filter(Boolean))].map((k) => (GESETZ[k] ? [adr.gesetz(k), GESETZ[k].name] : IDEE[k] ? [adr.idee(k), IDEE[k].kurz] : REGEL[k] ? [adr.regel(k), REGEL[k].name] : null)).filter(Boolean);
    return z.length ? `<p class="ru-tafel-warum-zeile">${z.map(([h, n]) => `<a class="ru-tafel-warum" href="${Z(h)}">Warum? ${esc(n)} ›</a>`).join('')}</p>` : ''; };
  const tfAe = (t, anker, name, feld) => ae('Tafel', t.id + (anker ? ' ' + anker : ''), ohneTags(name), feld);
  // Karte: Überschrift mit „Ändern lassen“ (Abschnitt), Inhalt
  const tfKarte = (t, anker, titel, inhalt, o = {}) => `<section class="ru-tafel-karte${o.klasse ? ' ' + o.klasse : ''}" id="ru-tf-${anker}"${dkl(o.kl)}>${aeKopf(`<h2 class="ru-tafel-h2">${titel}${o.kl !== undefined ? ' ' + tfKl(o.kl) : ''}</h2>`, tfAe(t, anker, titel, 'Abschnitt'))}${inhalt}</section>`;
  const tfMehr = (titel, inhalt, o = {}) => `<details class="ru-tafel-mehr"${o.anker ? ` id="ru-tf-${o.anker}"` : ''}${dkl(o.kl)}${o.offen ? ' open' : ''}><summary><span class="ru-tafel-mehr-t">${titel}</span>${CHEVRON}</summary><div class="ru-tafel-mehr-in">${inhalt}</div></details>`;
  const tfAnker = (...a) => a.map((x) => `<span class="ru-tafel-anker" id="ru-tf-${x}"></span>`).join('');
  // Matrix: kopf = Spaltenköpfe; zeilen: { anker, kl, kopf (erste Spalte, HTML), zellen (HTML), detail (HTML, klappt beim Antippen auf) } oder { gruppe }
  function matrix(kopf, zeilen, o = {}) {
    const n = kopf.length;
    const koerper = zeilen.map((z) => {
      if (z.gruppe) return `<tbody class="ru-tafel-gruppe"${dkl(z.kl)}><tr><th colspan="${n}" scope="colgroup">${z.gruppe}</th></tr></tbody>`;
      const did = 'ru-tfd-' + (z.anker || 'z' + (++tfNr));
      const erste = z.detail ? `<button type="button" class="ru-tafel-auf" aria-expanded="false" aria-controls="${did}"><span class="ru-tafel-zk">${z.kopf}</span>${CHEVRON}</button>` : `<span class="ru-tafel-zk">${z.kopf}</span>`;
      return `<tbody class="ru-tafel-z${z.klasse ? ' ' + z.klasse : ''}"${z.anker ? ` id="ru-tf-${z.anker}"` : ''}${dkl(z.kl)}><tr><th scope="row" class="ru-tafel-fest">${erste}</th>${z.zellen.map((c) => `<td>${c}</td>`).join('')}</tr>${z.detail ? `<tr class="ru-tafel-detail" id="${did}" hidden><td colspan="${n}"><div class="ru-tafel-d">${z.detail}</div></td></tr>` : ''}</tbody>`;
    }).join('');
    return `<div class="ru-tafel-roll${o.klasse ? ' ' + o.klasse : ''}" role="region" aria-label="${esc(o.titel || 'Tabelle')}" tabindex="0"><table class="ru-tafel-matrix"><thead><tr>${kopf.map((k, i) => `<th scope="col"${i ? '' : ' class="ru-tafel-fest"'}>${k}</th>`).join('')}</tr></thead>${koerper}</table></div>`;
  }
  const werkzeug = () => `<div class="ru-tafel-werkzeug"><div class="ru-tafel-kf" role="group" aria-label="Zeigen bis Klasse"><span>bis Klasse</span>${['5', '6', '7', '8', '9', '10', 'alle'].map((k) => `<button type="button" data-bis="${k}" aria-pressed="${k === 'alle'}">${k}</button>`).join('')}</div><button type="button" class="ru-tafel-drucken">Drucken</button></div>`;
  const tfGebiet = (t) => (PLANET[t.gebiet] ? PLANET[t.gebiet].kuerzel : '');
  function tafelSeite(t, inhalt, lead, eltern) {
    tfNr = 0;
    return `<div class="ru-breite ru-schmal ru-start ru-tafel-seite" data-tafel="${t.id}" data-gebiet="${tfGebiet(t)}">${elternBand()}${pfad(gebietKrume(t), eltern ? `<a href="${Z(adr.tafel('formeln'))}">Formeln</a>` : '', `<span aria-current="page">${esc(t.titel)}</span>`)}
      <header class="ru-tafel-kopf">${aeKopf(`<h1 class="ru-titel">${esc(t.titel)}</h1>`, tfAe(t, '', t.titel, 'ganze Tafel'))}${lead ? `<p class="ru-lead">${lead}</p>` : ''}${werkzeug()}</header>${inhalt}</div>`;
  }

  // ---------- „Auf einen Blick“: Tafeln im Gebiet (bzw. bei der Sonne) – Zuordnung aus den Daten (tafel.gebiete, tafel.unter) ----------
  // Dazu die Zeilen aus „Was man sonst noch braucht“ (Formeln), deren Einzelregel in diesem Gebiet liegt und deren Tafel nicht schon hier steht.
  const blickTafeln = (name) => I.TAFELN.filter((t) => (t.gebiete || []).includes(name) && !t.unter);
  const blickSonst = (name) => (TAFEL.formeln && !blickTafeln(name).includes(TAFEL.formeln) ? (TAFEL.formeln.sonst || []).filter((z) => z.gesetz && GESETZ[z.gesetz] && GESETZ[z.gesetz].planet === name) : []);
  const blickZahl = (name) => blickTafeln(name).length + (blickSonst(name).length ? 1 : 0);
  const TAFEL_SYM = '<svg class="ru-blick-sym" viewBox="0 0 16 12" aria-hidden="true"><rect x="1" y="1" width="14" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M1 4.5H15M6 4.5V11" stroke="currentColor" stroke-width="1.4"/></svg>';
  // Startseite: kleines Tafel-Zeichen mit Zahl in der Zeile des Gebiets (ausgeschrieben für Screenreader und als Titel) – die Zeile bleibt einzeilig, alle Gebiete im ersten Bildschirm
  const blickHinweis = (name) => { const n = blickZahl(name); const w = `${n} ${n === 1 ? 'Übersicht' : 'Übersichten'}`; return n ? ` <span class="ru-blick-hinweis" title="${w}">${TAFEL_SYM}${n}<span class="ru-unsichtbar"> ${n === 1 ? 'Übersicht' : 'Übersichten'}</span></span>` : ''; };
  const gebietFarbe = (name) => (PLANET[name] ? PLANET[name].kuerzel : 'sonne');
  function aufEinenBlick(name) {
    const tl = blickTafeln(name), so = blickSonst(name); if (!tl.length && !so.length) return '';
    const karte = (href, t, titel, klein, chip) => `<a class="ru-blick-k" href="${href}">${t.ikon}<span class="ru-blick-t"><b>${esc(titel)}</b><small>${klein}</small>${chip ? `<span class="ru-tafel-chip">${esc(chip)}</span>` : ''}</span><span class="ru-tafel-pf" aria-hidden="true">›</span></a>`;
    const eintraege = tl.map((t) => { const unter = I.TAFELN.filter((u) => u.unter === t.id && (u.gebiete || []).includes(name));
      return `<li class="ru-blick-e">${karte(Z(adr.tafel(t.id)), t, t.titel, esc(t.kurz), t.chip)}${unter.length ? `<p class="ru-blick-unter">${unter.map((u) => `<a href="${Z(adr.tafel(u.id))}">${esc(u.titel.replace(/^Formeln: /, ''))} im Einzelnen ›</a>`).join('')}</p>` : ''}</li>`; });
    if (so.length) { const f = TAFEL.formeln, ziel = so.length === 1 ? adr.tafel('formeln', 'so-' + so[0].gesetz.toLowerCase()) : adr.tafel('formeln', 'sonst');
      eintraege.push(`<li class="ru-blick-e">${karte(Z(ziel), f, f.titel + ' · Was man sonst noch braucht', so.map((z) => esc(GESETZ[z.gesetz].name)).join(' · '), '')}</li>`); }
    return `<section class="ru-blick" data-gebiet="${esc(gebietFarbe(name))}" aria-labelledby="ru-blick-kopf"><h2 class="ru-ueber" id="ru-blick-kopf">${TAFEL_SYM}Auf einen Blick</h2><ul class="ru-blick-liste">${eintraege.join('')}</ul></section>`;
  }
  // Brotkrumen einer Tafel: das Gebiet, aus dem man kam (wenn die Tafel dort steht), sonst das erste ihrer Gebiete
  const gebietKrume = (t) => { const gs = t.gebiete || []; const von = zustand.gebiet && (gs.includes(zustand.gebiet) || (t.id === 'formeln' && blickSonst(zustand.gebiet).length)) ? zustand.gebiet : gs[0];
    return !von ? '' : von === 'Sonne' ? `<a href="${Z('sonne')}">Sonne</a>` : PLANET[von] ? `<a href="${Z(adr.gebiet(von))}">${esc(von)}</a>` : ''; };
  // Verweis von Regel, Idee oder Einzelregel auf die passende Tafel
  const tafelVerweis = (ids) => { const v = I.tafelnZu(ids); return v.length ? `<nav class="ru-tafel-verweise" aria-label="Tafeln zum Nachschlagen">${v.map((x) => `<a class="ru-verweis ru-tafel-v" href="${Z(x.ziel)}"><span class="ru-nr">Tafel</span>${esc(x.t.id === 'formeln-flaechen' || x.t.id === 'formeln-koerper' ? TAFEL.formeln.titel : x.t.titel)}${x.teil ? ' › ' + esc(x.teil.titel) : ''}</a>`).join('')}</nav>` : ''; };

  // ---------- Maßeinheiten: Schnellübersicht (Matrix aller Größen) + je Größe „1 … = …“ ----------
  const fZahl = (s) => Number(String(s).replace(/\s/g, '').replace(',', '.'));
  // Treppe (groß → klein) zu Einheiten mit Umrechnungszahl zur nächsten; ohne Zusatz-Stufen werden deren Zahlen zusammengerechnet
  function kette(treppe, mitZusatz) {
    const aus = []; let f = 1;
    for (const s of treppe) { if (mitZusatz || !s.zusatz) { if (aus.length) aus[aus.length - 1].f = f; aus.push({ e: s.einheit, name: s.name, zusatz: !!s.zusatz, f: null }); f = 1; } f *= s.zur_naechsten ? fZahl(s.zur_naechsten) : 1; }
    return aus;
  }
  // Zeile der Schnellübersicht: klein → groß, dazwischen die Zahl („mm ·10 cm“: 1 cm = 10 mm)
  // Zahl und Einheit bleiben zusammen („·10 cm“), die Kette darf zwischen den Paaren umbrechen
  const ketteHtml = (k) => `<span class="ru-tafel-kette">${[...k].reverse().map((u, i, r) => `<span class="ru-tafel-paar">${i ? `<span class="ru-tafel-fak" title="1 ${esc(u.e)} = ${tfZahl(u.f)} ${esc(r[i - 1].e)}">·${tfZahl(u.f)}</span>` : ''}<b class="ru-tafel-eh${u.zusatz ? ' ru-tafel-zus' : ''}" title="${esc(u.name)}">${esc(u.e)}</b></span>`).join('')}</span>`;
  // Kreuztabelle „1 … = …“: alle Einheiten als Zeile und Spalte, Diagonale 1. Zur kleineren Einheit die Umrechnungszahl (ab einer Million als „Mio.“, „Mrd.“, „Bio.“),
  // zur größeren der Bruchteil: Zehnerbruch als Dezimalzahl (0,1 · 0,01 · 0,001), sonst als Bruch (1/60); kleiner als ein Tausendstel bleibt die Zelle leer.
  const gross = (n) => { for (const [z, w] of [[1e12, 'Bio.'], [1e9, 'Mrd.'], [1e6, 'Mio.']]) if (n >= z && n % z === 0) return `${tfZahl(n / z)}\u00a0${w}`; return tfZahl(n); };
  const teilwert = (p) => (p > 1000 ? '' : /^10*$/.test(String(p)) ? '0,' + '0'.repeat(String(p).length - 2) + '1' : '1/' + tfZahl(p));
  function kreuz(k, titel) {
    const prod = (a, b) => { let p = 1; for (let j = a; j < b; j++) p *= k[j].f; return p; };
    const zeilen = k.map((u, r) => ({ kopf: `1\u00a0${esc(u.e)}\u00a0=`, klasse: u.zusatz ? 'ru-tafel-zus' : '',
      zellen: k.map((v, c) => { const w = c === r ? '1' : c > r ? gross(prod(r, c)) : teilwert(prod(c, r));
        return w ? `<span class="ru-tafel-wert${c === r ? ' ru-tafel-eins' : ''}" title="1 ${esc(u.e)} = ${w.replace(/\u00a0/g, ' ')} ${esc(v.e)}">${w}</span>` : '<span class="ru-tafel-leer" aria-hidden="true">·</span>'; }) }));
    return matrix(['1 … =', ...k.map((v) => `<span class="${v.zusatz ? 'ru-tafel-zus' : ''}">${esc(v.e)}</span>`)], zeilen, { titel, klasse: 'ru-tafel-kreuz' });
  }
  function einheitDetails(t, x) {
    const b0 = x.beispiele[0];
    return `${(x.so_gehts || []).length ? tfH3('So geht’s') + tfListe(x.so_gehts, 'ol') : ''}
      ${tfH3('Beispiele')}<ul class="ru-tafel-liste ru-tafel-bsp-liste">${x.beispiele.map((y) => `<li><span class="ru-rechnung">${nb(y.von)} = ${nb(y.nach)}</span>, denn ${nb(y.denn)}.${y.achtung ? ' ' + nb(y.achtung) : ''}</li>`).join('')}</ul>
      ${(x.stolperstellen || []).length ? tfH3('Stolperstellen') + `<ul class="ru-tafel-liste">${x.stolperstellen.map((y) => `<li><b>${nb(y.fehler)}</b> ${nb(y.richtig)}</li>`).join('')}</ul>` : ''}
      ${(x.hinweise || []).length ? tfH3('Gut zu wissen') + tfListe(x.hinweise) : ''}${(x.herleitung || []).length ? tfH3('Warum?') + tfListe(x.herleitung.map((h) => h.text)) : ''}
      ${tfRegeln(kennVonT(x.regeln))}${tfErw(x.ab_klasse_hinweis)}${b0 ? '' : ''}`;
  }
  const kennVonT = (l) => (l || []).map((r) => r.kennung);
  function einheitAbschnitt(t, x, offen) {
    const k = kette(x.treppe, true), w = (x.weitere_treppen || [])[0], b0 = x.beispiele[0];
    // mehr als fünf Einheiten (Fläche): zwei Tafeln, die sich in der mittleren Einheit treffen – so passt jede aufs Handy
    const m = Math.floor((k.length - 1) / 2), teile = k.length > 5 ? [k.slice(0, m + 1), k.slice(m)] : [k];
    const inhalt = `${aeZeile(tfAe(t, x.anker, x.art, 'Abschnitt (Umrechnung, Beispiele, Stolperstellen)'))}${teile.map((kk) => `${teile.length > 1 ? tfH3(`${esc(kk[0].e)} bis ${esc(kk[kk.length - 1].e)}`) : ''}${kreuz(kk, '1 … = … ' + x.art)}`).join('')}
      ${w ? `${tfAnker('hohlmass')}${tfH3(esc(w.name))}${kreuz(kette(w.treppe, true), '1 … = … ' + w.name)}` : ''}
      ${(x.verbindung || []).length ? `<p class="ru-tafel-verb">${x.verbindung.map((v) => `<b>${nb(v.links)} = ${nb(v.rechts)}</b>`).join(' · ')}</p>` : ''}
      ${k.some((u) => u.zusatz) || (w && w.treppe.some((u) => u.zusatz)) ? '<p class="ru-tafel-hinweis">Grau: kommt in den Lernkarten nicht vor, ist aber gebräuchlich.</p>' : ''}
      ${tfMerk(x.merksatz)}${b0 ? `<p class="ru-tafel-bsp"><span class="ru-rechnung">${nb(b0.von)} = ${nb(b0.nach)}</span> <small>denn ${nb(b0.denn)}</small></p>` : ''}
      ${tfMehr('So geht’s · Beispiele · Stolperstellen', einheitDetails(t, x))}`;
    return tfMehr(`${esc(x.art)} ${tfKl(x.kl)}`, inhalt, { anker: x.anker, kl: x.kl, offen });
  }
  const KURZNAME = { 'Volumen und Hohlmaße': 'Volumen', 'Hohlmaße': 'Hohlmaß' };
  function tafelEinheiten(t) {
    const A = Object.fromEntries(t.arten.map((x) => [x.anker, x])), v = A.volumen, w = v && (v.weitere_treppen || [])[0];
    const reihen = [['laenge', A.laenge], ['flaeche', A.flaeche], ['volumen', v], ['hohlmass', w && { art: w.name, treppe: w.treppe, kl: v.kl }], ['masse', A.masse], ['zeit', A.zeit], ['geld', A.geld]].filter(([, x]) => x);
    const schnell = matrix(['Größe', 'Einheiten von klein nach groß'], reihen.map(([a, x]) => ({ kl: x.kl, kopf: `<span class="ru-tafel-zk-text"><a class="ru-tafel-sprung" href="${Z(adr.tafel(t.id, a))}">${esc(KURZNAME[x.art] || x.art)}</a>${tfKl(x.kl)}</span>`, zellen: [ketteHtml(kette(x.treppe, false)) + (a === 'hohlmass' && (v.verbindung || []).length ? `<small class="ru-tafel-verb-k">${[...v.verbindung].reverse().map((y) => `${nb(y.links)} = ${nb(y.rechts)}`).join(' · ')}</small>` : '')] })), { titel: 'Schnellübersicht Maßeinheiten', klasse: 'ru-tafel-schnell' });
    const hoeher = ['tempo', 'dichte'].map((a) => A[a]).filter(Boolean);
    return `${tfKarte(t, 'schnell', 'Schnellübersicht', `<p class="ru-tafel-leitsatz"><b>Zur größeren Einheit teilen, zur kleineren malnehmen.</b> <span>${nb(t.richtung.merksatz)}</span></p>${schnell}
        <p class="ru-tafel-hinweis">Die Zahl zwischen zwei Einheiten sagt, wie viele kleine eine große sind: <b class="ru-rechnung">mm ·10 cm</b> heißt 1 cm = 10 mm.${w && (w.treppe || []).some((s) => s.zusatz) ? ' hl, dl und cl stehen unten bei Volumen.' : ''}</p>`, { klasse: 'ru-tafel-erste' })}
      ${tfKarte(t, 'je-groesse', '1 … = … je Größe', `<p class="ru-tafel-hinweis">Zeile lesen: 1 m = 10 dm = 100 cm = 1 000 mm, und 1 m = 0,001 km. Leer: kleiner als ein Tausendstel.</p>${t.arten.filter((x) => !['tempo', 'dichte'].includes(x.anker)).map((x) => einheitAbschnitt(t, x, ['laenge', 'masse'].includes(x.anker))).join('')}`)}
      ${hoeher.length ? tfKarte(t, 'hoeher', 'Für höhere Klassen', hoeher.map((x) => tfMehr(`${esc(x.art)} ${tfKl(x.kl)}`, `${aeZeile(tfAe(t, x.anker, x.art, 'Abschnitt'))}<p class="ru-tafel-kette-z">${ketteHtml(kette(x.treppe, true))}</p>${x.zusammengesetzt ? '<p class="ru-tafel-hinweis">Keine Tabelle: zusammengesetzte Einheit – rechne über die Kette.</p>' : ''}${tfMerk(x.merksatz)}${(x.so_gehts || []).length ? tfListe(x.so_gehts, 'ol') : ''}${tfMehr('Beispiele · Stolperstellen', einheitDetails(t, { ...x, so_gehts: [] }))}`, { anker: x.anker, kl: x.kl })).join('')) : ''}
      ${ERW && (t.nicht_aufgenommen || []).length ? `<p class="ru-tafel-erw"><b>Für Eltern – nicht aufgenommen:</b> ${t.nicht_aufgenommen.map((n) => `${esc(n.art)} (${esc(n.grund)})`).join(' ')}</p>` : ''}`;
  }

  // ---------- Formeln: Figuren und Körper ----------
  const SPALTEN = { 'formeln-flaechen': [['Umfang', /Umfang|Bogen/], ['Flächeninhalt', /./]], 'formeln-koerper': [['Oberfläche', /Mantel|Oberfläche/], ['Volumen', /./]] };
  const teilName = (f) => f.fuer.split(' – ').slice(1).join(' – ');
  // kleine Beschriftung einer Formel, wenn sie nicht die erwartete Größe der Spalte ist (Bogen, Mantel, Raute …)
  function formelLabel(f, karte, spalte) {
    const rest = f.figur !== karte.name ? (f.figur.startsWith(karte.name + ' ') ? f.figur.slice(karte.name.length + 1) : f.figur) : '';
    // Sonderfall aus der Quelle (fk-19: „gerade quadratische Pyramide“) steht direkt an der Formel (Auflagen aus Werkstatt 1152)
    if (f.sonderfall) return 'Sonderfall: ' + f.sonderfall;
    const teil = teilName(f), std = ['Fläche', 'Umfang', 'Volumen', 'Oberfläche'].includes(teil) && (spalte === teil || (spalte === 'Flächeninhalt' && teil === 'Fläche'));
    return [std ? '' : teil, rest].filter(Boolean).join(', ');
  }
  const formelHtml = (f, lab) => `<span class="ru-tafel-fz"${dkl(f.kl)}>${lab ? `<small>${esc(lab)}</small>` : ''}<span class="ru-tafel-f">${formel(f.formel)}</span></span>`;
  function karteSpalten(t, k, ohneMantel) {
    const sp = SPALTEN[t.id], zellen = sp.map(() => []);
    // Gesamtübersicht (ohneMantel): in der Körper-Matrix nur O und V, der Mantel steht in den Einzelheiten
    for (const f of k.zeilen) { if (ohneMantel && /^Mantel/.test(teilName(f))) continue; const i = sp.findIndex(([, re]) => re.test(teilName(f))); zellen[i].push(formelHtml(f, formelLabel(f, k, sp[i][0]))); }
    return zellen.map((z) => (z.length ? z.join('') : '<span class="ru-tafel-leer" aria-label="keine Formel auf der Tafel">–</span>'));
  }
  function bezeichnungen(k) {
    const seen = new Map();
    for (const f of [...k.zeilen, ...k.zusatz]) for (const g of [f.ergebnis, ...(f.groessen || [])]) { const key = g.zeichen + '|' + g.name; if (![...seen.keys()].some((x) => x === key)) seen.set(key, g); }
    return `<dl class="ru-tafel-bez">${[...seen.values()].map((g) => `<div><dt>${esc(g.zeichen)}</dt><dd>${esc(g.name)}${g.einheit ? ` <span class="ru-leise">(in ${esc(g.einheit)})</span>` : ''}</dd></div>`).join('')}</dl>`;
  }
  const bedingungen = (liste, k) => { const b = liste.filter((f) => f.bedingung && f.bedingung !== '–'); return b.length ? `<ul class="ru-tafel-liste ru-tafel-bed">${b.map((f) => `<li><b>${esc(teilName(f))}${f.figur !== k.name ? ' (' + esc(f.figur) + ')' : ''}:</b> ${nb(f.bedingung)}</li>`).join('')}</ul>` : ''; };
  const beispiele = (liste) => `<ul class="ru-tafel-liste ru-tafel-bsp-liste">${liste.filter((f) => f.beispiel).map((f) => `<li><span class="ru-rechnung">${nb(f.beispiel.rechnung)}</span>${f.beispiel.hilfe ? ` <small>${nb(f.beispiel.hilfe)}</small>` : ''}</li>`).join('')}</ul>`;
  const zusatzHtml = (k) => (k.zusatz.length ? `${tfH3('Zusatz')}<ul class="ru-tafel-liste">${k.zusatz.map((f) => `<li${dkl(f.kl)}><b>${esc(teilName(f))}:</b> <span class="ru-tafel-f">${formel(f.formel)}</span> ${tfKl(f.kl)}${f.beispiel ? `<br><span class="ru-rechnung ru-leise">${nb(f.beispiel.rechnung)}</span>` : ''}</li>`).join('')}</ul>` : '');
  const karteErw = (k) => [...k.zeilen, ...k.zusatz].map((f) => [f.ab_klasse_hinweis, f.regeln_hinweis].filter(Boolean).map((h) => tfErw(`${f.fuer}: ${h}`)).join('')).join('');
  const karteKenn = (k) => [...k.zeilen, ...k.zusatz].flatMap((f) => [f.ziel, ...kennVonT(f.regeln)]);
  const miniBild = (k) => miniSvg(k.bild);
  // Zeile der Gesamtübersicht (Matrix): Mini-Zeichnung, Name, Klasse; beim Antippen Zeichnung, Bezeichnungen, Bedingungen, Verweise
  const mantel = (k) => { const m = k.zeilen.filter((f) => /^Mantel/.test(teilName(f))); return m.length ? `${tfH3('Mantel')}<p>${m.map((f) => `<span class="ru-tafel-f">${formel(f.formel)}</span>`).join('<br>')}</p>` : ''; };
  const formelZeile = (t, k) => ({ anker: k.anker, kl: k.kl, kopf: `${miniBild(k)}<span class="ru-tafel-zk-text"><b>${esc(k.name)}</b>${tfKl(k.kl)}</span>`, zellen: karteSpalten(t, k, true),
    detail: `<div class="ru-tafel-d-kopf"><div class="ru-tafel-bild">${k.bild}</div><div>${mantel(k)}${tfH3('Bezeichnungen')}${bezeichnungen(k)}</div></div>${bedingungen([...k.zeilen], k)}${zusatzHtml(k)}
      <p class="ru-tafel-d-fuss"><a class="ru-tafel-warum" href="${Z(adr.tafel(t.id, k.anker))}">Alle Einzelheiten und Beispiele ›</a></p>${tfRegeln(karteKenn(k))}${karteErw(k)}${aeZeile(tfAe(t, k.anker, k.name, 'Zeile (Formeln, Bezeichnungen)'))}` });
  const formelMatrix = (t, kopf) => matrix([kopf, ...SPALTEN[t.id].map(([s]) => s)], t.karten.map((k) => formelZeile(t, k)), { titel: t.titel, klasse: 'ru-tafel-formeln' });
  // „Was man sonst noch braucht“: Formeln der Tafeln (Prozent, Zinsen, Winkelsumme) und Einzelregeln mit Formel im Merksatz
  function sonstZeile(z) {
    if (z.gesetz) { const g = GESETZ[z.gesetz]; if (!g) return null; const kl = Number(((g.gym || '').match(/\d+/) || [])[0]) || null;
      const zelle = z.kurz ? `${z.kurz.map((x) => `<span class="ru-tafel-fz"><span class="ru-tafel-f">${formel(x)}</span></span>`).join('')}${z.bed ? `<small class="ru-tafel-bed-k">${nb(z.bed)}</small>` : ''}` : `<span class="ru-tafel-satz">${g.satz}</span>`;
      return { anker: 'so-' + z.gesetz.toLowerCase(), kl, kopf: `<span class="ru-tafel-zk-text"><b>${esc(g.name)}</b>${tfKl(kl)}</span>`, zellen: [zelle],
        detail: `${z.kurz ? `${tfH3('Merksatz')}<p>${g.satz}</p>` : ''}${z.mehr && z.mehr.length ? `${tfH3('Darauf achten')}${tfListe(z.mehr)}` : ''}${g.beispiel ? `${tfH3('Beispiel')}<p>${nb(g.beispiel)}</p>` : ''}${tfRegeln([z.gesetz])}${aeZeile(ae('Einzelregel', z.gesetz, g.name, 'satz (Tafel Formeln)'))}` }; }
    const q = TAFEL[z.tafel], e = q && q.eintraege.find((x) => x.kennung === z.kennung); if (!e) return null;
    return { anker: 'so-' + e.kennung, kl: e.kl, kopf: `<span class="ru-tafel-zk-text"><b>${esc(e.titel)}</b>${tfKl(e.kl)}</span>`, zellen: [`<span class="ru-tafel-f">${formel(e.formel)}</span>${e.bedingung && e.bedingung !== '–' ? `<small class="ru-tafel-bed-k">${nb(e.bedingung)}</small>` : ''}`],
      detail: `${eintragFormelDetail(e)}<p class="ru-tafel-d-fuss"><a class="ru-tafel-warum" href="${Z(adr.tafel(q.id, e.kennung))}">Auf der Tafel „${esc(q.titel)}“ ›</a></p>${tfRegeln(kennVonT(e.regeln))}${aeZeile(tfAe(q, e.kennung, e.titel, 'Zeile (Tafel Formeln)'))}` };
  }
  function eintragFormelDetail(e) {
    const b = e.beispiel || {};
    return `${(e.groessen || []).length ? `${tfH3('Bezeichnungen')}<dl class="ru-tafel-bez">${e.groessen.map((g) => `<div><dt>${esc(g.zeichen)}</dt><dd>${esc(g.name)}</dd></div>`).join('')}</dl>` : ''}
      ${e.aufgabe ? `${tfH3('Aufgabe')}<p>${nb(e.aufgabe)}</p>` : ''}${(e.so_gehts || []).length ? tfH3('So geht’s') + tfListe(e.so_gehts, 'ol') : ''}
      ${b.rechnung || b.q_rechnung ? `${tfH3('Beispiel')}<ul class="ru-tafel-liste ru-tafel-bsp-liste">${[b.q_rechnung, ...(b.schritte || []), b.rechnung, b.danach, b.probe ? 'Probe: ' + b.probe : '', b.zinsen_gesamt].filter(Boolean).map((r) => `<li><span class="ru-rechnung">${nb(r)}</span></li>`).join('')}</ul>${b.achtung ? `<p class="ru-tafel-achtung">${nb(b.achtung)}</p>` : ''}` : ''}`;
  }
  function tafelFormeln(t) {
    const F = TAFEL['formeln-flaechen'], K = TAFEL['formeln-koerper'];
    const legende = (q) => (q && q.groessenarten ? `<p class="ru-tafel-hinweis">${Object.entries(q.groessenarten).filter(([k]) => k !== 'Winkel').map(([k, v]) => `${esc(k)}: ${esc(v)}`).join(' · ')}. Tippe auf eine Zeile für Bezeichnungen und Bedingungen.</p>` : '');
    return `${F ? tfKarte(t, 'flaechen', 'Ebene Figuren', `${formelMatrix(F, 'Figur')}${legende(F)}<p class="ru-tafel-weiter"><a class="ru-tafel-warum" href="${Z(adr.tafel(F.id))}">Alle Figuren mit Beispielen ›</a></p>`, { klasse: 'ru-tafel-erste' }) : ''}
      ${K ? tfKarte(t, 'koerper', 'Körper', `${formelMatrix(K, 'Körper')}<p class="ru-tafel-hinweis">Volumen in cm³, Oberfläche und Mantel in cm². G ist der Flächeninhalt der Grundfläche, M der Mantelflächeninhalt des Körpers.</p><p class="ru-tafel-weiter"><a class="ru-tafel-warum" href="${Z(adr.tafel(K.id))}">Alle Körper mit Beispielen ›</a></p>`) : ''}
      ${tfKarte(t, 'sonst', 'Was man sonst noch braucht', matrix(['Wofür', 'Formel oder Regel'], (t.sonst || []).map(sonstZeile).filter(Boolean), { titel: 'Weitere Formeln', klasse: 'ru-tafel-sonst' }))}`;
  }
  // Detailansicht Flächen bzw. Körper: je Figur eine Karte mit Zeichnung, Formeln, Bezeichnungen, Beispielen (entwurf1, Bild 04/05)
  function tafelFormelKarten(t) {
    const sp = SPALTEN[t.id];
    return `<div class="ru-tafel-figuren">${t.karten.map((k) => { const zellen = karteSpalten(t, k);
      return `<section class="ru-tafel-figur" id="ru-tf-${k.anker}"${dkl(k.kl)}><div class="ru-tafel-bild">${k.bild}</div><div class="ru-tafel-figur-kt">${aeKopf(`<h2 class="ru-tafel-h2">${esc(k.name)}</h2>`, tfAe(t, k.anker, k.name, 'Karte'))}${tfKl(k.kl)}</div>
        <dl class="ru-tafel-fdl">${sp.map(([s], i) => `<dt>${s}</dt><dd>${zellen[i]}</dd>`).join('')}</dl>
        ${tfH3('Bezeichnungen')}${bezeichnungen(k)}${bedingungen(k.zeilen, k)}${tfMehr('Beispiele', beispiele(k.zeilen) + zusatzHtml(k))}${tfRegeln(karteKenn(k))}${karteErw(k)}</section>`; }).join('')}</div>`;
  }

  // ---------- Zahlen ----------
  function tafelZahlen(t) {
    const E = Object.fromEntries(t.eintraege.map((e) => [e.kennung, e])), q = E['zz-01'], k3 = E['zz-02'], z2 = E['zz-03'];
    const ns = [...new Set([...z2.liste.map((x) => x.exponent), ...q.liste.map((x) => x.n), ...k3.liste.map((x) => x.n)])].sort((a, b) => a - b);
    const wert = (l, n, f, key) => { const x = l.find((y) => y[key] === n); return x ? `<span class="ru-tafel-wert">${tfZahl(x[f])}</span>` : ''; };
    const pot = matrix(['n', 'n²', 'n³', '2ⁿ'], ns.map((n) => ({ kopf: String(n), zellen: [wert(q.liste, n, 'quadrat', 'n'), wert(k3.liste, n, 'kubik', 'n'), wert(z2.liste, n, 'wert', 'exponent')] })), { titel: 'Quadrat-, Kubik- und Zweierpotenzen', klasse: 'ru-tafel-zahlen' });
    const pr = E['zz-06'], prim = new Set(pr.liste);
    const gitter = `<div class="ru-tafel-gitter" role="img" aria-label="Zahlen 1 bis 100, die ${pr.anzahl} Primzahlen hervorgehoben: ${pr.liste.join(', ')}">${Array.from({ length: 100 }, (_, i) => `<span${prim.has(i + 1) ? ' class="ru-tafel-prim"' : ''}>${i + 1}</span>`).join('')}</div>`;
    const teil = t.eintraege.filter((e) => e.art === 'teilbarkeit');
    const tb = matrix(['Teilbar durch', 'Sieh an', 'Regel'], teil.map((e) => ({ anker: e.kennung, kl: e.kl, kopf: `<span class="ru-tafel-zk-text"><b class="ru-tafel-gross">${e.teiler}</b>${tfKl(e.kl)}</span>`, zellen: [esc(e.sieh_an), nb(e.regel_text)],
      detail: `<p><b>Ja:</b> <span class="ru-rechnung">${nb(e.ja.zahl)}</span> – ${nb(e.ja.weg)}</p><p><b>Nein:</b> <span class="ru-rechnung">${nb(e.nein.zahl)}</span> – ${nb(e.nein.weg)}</p>${tfRegeln(kennVonT(e.regeln))}${tfErw(e.ab_klasse_hinweis)}${tfErw(e.regeln_hinweis)}${aeZeile(tfAe(t, e.kennung, e.titel, 'Zeile'))}` })), { titel: 'Teilbarkeitsregeln', klasse: 'ru-tafel-teilbar' });
    const zp = [E['zz-04'], E['zz-05']].filter(Boolean);
    const zehn = matrix(['Potenz', 'Zahl', 'Name'], zp.flatMap((e) => (e.kennung === 'zz-04' ? [...e.liste].reverse() : e.liste).map((x) => ({ kl: e.kl, kopf: esc(x.potenz), zellen: [`<span class="ru-tafel-wert">${nb(x.zahl)}</span>`, esc(x.name)] }))), { titel: 'Zehnerpotenzen', klasse: 'ru-tafel-zehn' });
    return `${tfKarte(t, 'zz-01', 'Quadrat-, Kubik- und Zweierpotenzen', `${tfAnker('zz-02', 'zz-03')}${pot}${tfMehr('Merksätze und Trick', `${[q, k3, z2].map((e) => tfMerk(e.merksatz)).join('')}${q.trick ? `<p class="ru-tafel-bsp">${nb(q.trick.text)}</p>` : ''}${tfRegeln([q, k3, z2].flatMap((e) => kennVonT(e.regeln)))}`)}`, { kl: q.kl, klasse: 'ru-tafel-erste' })}
      ${tfKarte(t, 'zz-06', esc(pr.titel), `${gitter}${tfMerk(pr.merksatz)}<p>${nb(pr.so_testest_du)}</p>${tfMehr('Warum nur bis 7? · Beispiele', `<p>${nb(pr.warum_nur_bis_7)}</p>${tfListe(pr.beispiele.map((b) => b.weg))}${tfRegeln(kennVonT(pr.regeln))}`)}`, { kl: pr.kl })}
      ${tfKarte(t, 'teilbarkeit', 'Teilbarkeitsregeln', `${tb}<p class="ru-tafel-hinweis">Tippe auf eine Zeile: ein Beispiel, das teilbar ist, und eins, das es nicht ist.</p>`)}
      ${tfKarte(t, 'zz-04', 'Zehnerpotenzen mit Namen', `${tfAnker('zz-05')}${zehn}${tfMehr('Merksätze', zp.map((e) => tfMerk(e.merksatz)).join('') + tfRegeln(zp.flatMap((e) => kennVonT(e.regeln))) + zp.map((e) => tfErw(e.ab_klasse_hinweis)).join(''))}`)}`;
  }

  // ---------- Stellenwert, Runden, römische Zahlen, Vorsilben ----------
  function tafelStellenwert(t) {
    const E = Object.fromEntries(t.eintraege.map((e) => [e.kennung, e])), s1 = E['sw-01'], s2 = E['sw-02'], s3 = E['sw-03'];
    const zeilen = []; let gruppe = null;
    for (const s of [...s1.stellen].reverse()) { if (s.gruppe !== gruppe) { gruppe = s.gruppe; zeilen.push({ gruppe: esc(gruppe) }); } zeilen.push({ kopf: `<span class="ru-tafel-zk-text"><b>${esc(s.name)}</b><small class="ru-tafel-kurz">${esc(s.kurz)}</small></span>`, zellen: [`<span class="ru-tafel-wert">${nb(s.wert)}</span><small class="ru-tafel-pot">= ${esc(s.potenz)}</small>`] }); }
    if (s2) { zeilen.push({ gruppe: 'Komma – hinter dem Komma', kl: s2.kl }); for (const s of s2.stellen) zeilen.push({ kl: s2.kl, kopf: `<span class="ru-tafel-zk-text"><b>${esc(s.name)}</b><small class="ru-tafel-kurz">${esc(s.kurz)}</small></span>`, zellen: [`<span class="ru-tafel-wert">${nb(s.wert)}</span><small class="ru-tafel-pot">= ${esc(s.potenz)}</small>`] }); }
    const stellen = matrix(['Stelle', 'Wert'], zeilen, { titel: 'Stellenwerttafel', klasse: 'ru-tafel-stellen' });
    const runden = t.eintraege.filter((e) => e.art === 'runden');
    const rm = matrix(['Zahl', 'runden auf', 'Ergebnis'], runden.flatMap((e) => e.beispiele.map((b, i) => ({ kl: e.kl, kopf: `<span class="ru-rechnung">${nb(b.zahl)}</span>`, zellen: [esc(b.stelle), `<b class="ru-rechnung">${nb(b.ergebnis)}</b>`], detail: `<p>${nb(b.grund)}</p>` }))), { titel: 'Runden: Beispiele' });
    const ro = E['sw-06'];
    const roem = ro ? `${matrix(['Zeichen', ...ro.zeichen.map((z) => `<b class="ru-tafel-gross">${esc(z.zeichen)}</b>`)], [{ kopf: 'Wert', zellen: ro.zeichen.map((z) => nb(z.wert)) }], { titel: 'Römische Zahlzeichen', klasse: 'ru-tafel-roem' })}
      ${tfH3('Nur diese sechs Abzüge')}${matrix(['Paar', ...ro.abzuege.map((z) => `<b>${esc(z.paar)}</b>`)], [{ kopf: 'Wert', zellen: ro.abzuege.map((z) => tfZahl(z.wert)) }], { titel: 'Erlaubte Abzüge', klasse: 'ru-tafel-roem' })}
      ${tfMehr('Regeln · Beispiele · Fehler', `<p>${nb(ro.addieren)}</p><p>${nb(ro.abziehen)} ${nb(ro.abzug_merkregel)}</p>${tfH3('Beispiele')}${tfListe(ro.beispiele.map((b) => b.rechnung))}${tfH3('So nicht')}<ul class="ru-tafel-liste">${ro.falsch.map((f) => `<li><s>${esc(f.falsch)}</s> → <b>${esc(f.richtig)}</b> = ${tfZahl(f.zahl)}</li>`).join('')}</ul><p class="ru-tafel-hinweis">${nb(ro.hinweis)}</p>${tfRegeln(kennVonT(ro.regeln))}`)}` : '';
    const vs = t.eintraege.filter((e) => e.art === 'vorsilbe').sort((a, b) => b.exponent - a.exponent);
    const vm = matrix(['Vorsilbe', 'Faktor', 'Beispiel'], vs.map((e) => ({ anker: e.kennung, kl: e.kl, kopf: `<span class="ru-tafel-zk-text"><b>${esc(e.vorsilbe)} <span class="ru-tafel-gross">${esc(e.kurz)}</span></b><small>${esc(e.bedeutet)}</small>${tfKl(e.kl)}</span>`,
      zellen: [`<span class="ru-tafel-wert">${nb(e.faktor)}</span><small class="ru-tafel-pot">= ${esc(e.potenz)}</small>`, `<span class="ru-rechnung">${nb(e.beispiel.text)}</span>`] })), { titel: 'Vorsilben', klasse: 'ru-tafel-vorsilben' });
    const vsErw = vs.map((e) => [e.ab_klasse_hinweis, e.regeln_hinweis].filter(Boolean).map((h) => tfErw(`${e.vorsilbe}: ${h}`)).join('')).join('');
    return `${tfKarte(t, 'sw-01', 'Stellenwerttafel', `${tfAnker('sw-02')}${stellen}${tfMerk(s1.merksatz)}${s2 ? tfMerk(s2.merksatz) : ''}
        ${tfMehr('Beispiele', `<p class="ru-tafel-bsp"><span class="ru-rechnung">${nb(s1.beispiel.text)}</span><small>${esc(s1.beispiel.wort)}</small></p>${s2 ? `<p class="ru-tafel-bsp"><span class="ru-rechnung">${nb(s2.beispiel.text)}</span><small>${esc(s2.beispiel.lesen)}</small></p>` : ''}${tfRegeln([s1, s2].filter(Boolean).flatMap((e) => kennVonT(e.regeln)))}${[s1, s2].filter(Boolean).map((e) => tfErw(e.ab_klasse_hinweis)).join('')}`)}
        ${s3 ? tfMehr(esc(s3.titel), `${tfListe(s3.so_gehts, 'ol')}${matrix(['Zahl', 'gelesen'], s3.beispiele.map((b) => ({ kopf: `<span class="ru-tafel-wert">${nb(b.zahl)}</span>`, zellen: [esc(b.wort)] })), { titel: 'Große Zahlen lesen', klasse: 'ru-tafel-lesen' })}<p class="ru-tafel-hinweis">${nb(s3.hinweis)}</p>`, { anker: 'sw-03', kl: s3.kl }) : ''}`, { klasse: 'ru-tafel-erste' })}
      ${tfKarte(t, 'sw-04', 'Runden', `${tfAnker('sw-05')}${runden.map((e) => `<p class="ru-tafel-merk"${dkl(e.kl)}><b>${esc(e.titel.replace(/^Runden: /, ''))}:</b> ${nb(e.merksatz)}</p>`).join('')}${rm}${tfMehr('Schritt für Schritt', `${tfListe(runden[0].schritte, 'ol')}<p>${nb(runden[0].zeichen)}</p>${tfRegeln(kennVonT(runden[0].regeln))}`)}`)}
      ${ro ? tfKarte(t, 'sw-06', 'Römische Zahlen', roem, { kl: ro.kl }) : ''}
      ${tfKarte(t, 'vorsilben', 'Vorsilben', `${vm}${tfRegeln(vs.flatMap((e) => kennVonT(e.regeln)))}${vsErw}`)}`;
  }

  // ---------- Bruch, Dezimalzahl, Prozent ----------
  function tafelProzent(t) {
    const E = Object.fromEntries(t.eintraege.map((e) => [e.kennung, e])), tb = E['bd-01'];
    // Periode mit Strich darüber (CSS) statt des kombinierenden Zeichens, das in Festbreitenschrift verrutscht; Ziffern aus den Feldern ganz, vor, periode
    const zahlMitPeriode = (x, prozent) => (x && x.ganz != null ? `${esc(x.ganz)}${x.vor || x.periode ? ',' + esc(x.vor) + (x.periode ? `<span class="ru-tafel-periode">${esc(x.periode)}</span>` : '') : ''}${prozent ? '\u00a0%' : ''}` : nb(x && x.text));
    const um = matrix(['Bruch', 'Dezimalzahl', 'Prozent'], tb.zeilen.map((z) => ({ kopf: tfBruch(z.bruch), zellen: [`<span class="ru-tafel-wert" aria-label="${esc(z.dezimal.text)}">${zahlMitPeriode(z.dezimal)}</span>`, `<span class="ru-tafel-wert" aria-label="${esc(z.prozent.text)}">${zahlMitPeriode(z.prozent, true)}</span>`] })), { titel: 'Bruch, Dezimalzahl, Prozent', klasse: 'ru-tafel-bdp' });
    const fo = t.eintraege.filter((e) => e.formel);
    const fm = matrix(['Gesucht', 'Formel'], fo.map((e) => ({ anker: e.kennung, kl: e.kl, kopf: `<span class="ru-tafel-zk-text"><b>${esc(e.titel)}</b>${tfKl(e.kl)}</span>`, zellen: [`<span class="ru-tafel-f">${formel(e.formel)}</span><small class="ru-tafel-bed-k">${nb(e.bedingung)}</small>`],
      detail: `${eintragFormelDetail(e)}${tfRegeln(kennVonT(e.regeln))}${aeZeile(tfAe(t, e.kennung, e.titel, 'Zeile'))}` })), { titel: 'Prozent und Zinsen', klasse: 'ru-tafel-prozent' });
    return `${tfKarte(t, 'bd-01', 'Umrechnen', `${um}<p class="ru-tafel-hinweis">${nb(tb.hinweis)}</p>${tfMehr('So rechnest du um', tfListe(tb.so_gehts, 'ol') + tfRegeln(kennVonT(tb.regeln)))}`, { kl: tb.kl, klasse: 'ru-tafel-erste' })}
      ${tfKarte(t, 'prozent', 'Prozent und Zinsen', `${tfAnker(...fo.map((e) => 'p-' + e.kennung))}${fm}<p class="ru-tafel-hinweis">Tippe auf eine Zeile: Bezeichnungen, Rechenweg und Beispiel.</p>`)}`;
  }

  // ---------- Figuren: Winkel, Dreiecke, Vierecke, Kongruenz ----------
  const VIER_SPALTEN = [['parallele_paare_mindestens', 'parallele Seiten&shy;paare (mindestens)'], ['alle_seiten_gleich_lang', 'alle Seiten gleich'], ['gegenseiten_gleich_lang', 'Gegen&shy;seiten gleich'],
    ['nachbarseitenpaare_gleich_lang', 'Nachbar&shy;seiten paarweise gleich'], ['vier_rechte_winkel', '4 rechte Winkel'], ['gegenueberliegende_winkel_gleich', 'beide Paare gegenüber&shy;liegender Winkel gleich'],
    ['diagonalen_gleich_lang', 'Diago&shy;nalen gleich lang'], ['diagonalen_senkrecht', 'Diago&shy;nalen senk&shy;recht'], ['diagonalen_halbieren_sich', 'Diago&shy;nalen halbieren sich'],
    ['symmetrieachsen_mindestens', 'Symmetrie&shy;achsen (mindestens)'], ['punktsymmetrisch', 'punkt&shy;symme&shy;trisch']];
  const jaNein = (v) => (v === true ? '<span class="ru-tafel-ja" role="img" aria-label="gilt immer">✓</span>' : v === false ? '<span class="ru-tafel-nein" role="img" aria-label="gilt nicht immer">–</span>' : `<b>${esc(v)}</b>`);
  function tafelFiguren(t) {
    const nach = (a) => t.eintraege.filter((e) => e.art === a), E = Object.fromEntries(t.eintraege.map((e) => [e.kennung, e]));
    const winkel = matrix(['Winkel', 'Größe', 'So erkennst du ihn'], nach('winkelart').map((e) => ({ anker: e.kennung, kl: e.kl, kopf: `${miniSvg(e.bild)}<span class="ru-tafel-zk-text"><b>${esc(e.titel)}</b>${tfKl(e.kl)}</span>`, zellen: [`<span class="ru-tafel-f">${nb(e.bereich)}</span>`, nb(e.so_erkennst_du)] })), { titel: 'Winkelarten', klasse: 'ru-tafel-winkel' });
    const ws = E['fg-07'], dr = nach('dreieck');
    const dreiecke = matrix(['Dreieck', 'Merkmal'], [['seiten', 'nach den Seiten'], ['winkel', 'nach den Winkeln']].flatMap(([n, g]) => [{ gruppe: g }, ...dr.filter((e) => e.nach === n).map((e) => ({ anker: e.kennung, kl: e.kl,
      kopf: `${miniSvg(e.bild)}<span class="ru-tafel-zk-text"><b>${esc(e.titel)}</b>${tfKl(e.kl)}</span>`, zellen: [nb(e.definition)],
      detail: `<div class="ru-tafel-d-kopf"><div class="ru-tafel-bild">${e.bild}</div><div>${tfListe(e.eigenschaften)}<p class="ru-rechnung">${nb(e.winkelsumme)}</p></div></div>${tfRegeln(kennVonT(e.regeln))}${tfErw(e.ab_klasse_hinweis)}${aeZeile(tfAe(t, e.kennung, e.titel, 'Zeile'))}` }))]), { titel: 'Dreiecke', klasse: 'ru-tafel-dreiecke' });
    const vier = nach('viereck');
    const vm = matrix(['Viereck', ...VIER_SPALTEN.map(([, s]) => s)], vier.map((e) => ({ anker: e.kennung, kl: e.kl, kopf: `${miniSvg(e.bild)}<span class="ru-tafel-zk-text"><b>${esc(e.titel)}</b>${tfKl(e.kl)}</span>`,
      zellen: VIER_SPALTEN.map(([k]) => jaNein(e.immer ? e.immer[k] : null)),
      detail: `<div class="ru-tafel-d-kopf"><div class="ru-tafel-bild">${e.bild}</div><dl class="ru-tafel-eig"><div><dt>Seiten</dt><dd>${nb(e.seiten)}</dd></div><div><dt>Winkel</dt><dd>${nb(e.winkel)}</dd></div><div><dt>Diagonalen</dt><dd>${nb(e.diagonalen)}</dd></div><div><dt>Symmetrieachsen</dt><dd>${nb(e.achsen_text)}${e.punktsymmetrisch ? '; punktsymmetrisch' : ''}</dd></div>${e.sonderfall_von.length ? `<div><dt>Sonderfall von</dt><dd>${e.sonderfall_von.map(esc).join(', ')}</dd></div>` : ''}</dl></div>${tfRegeln(kennVonT(e.regeln))}${tfErw(e.regeln_hinweis)}${aeZeile(tfAe(t, e.kennung, e.titel, 'Zeile'))}` })), { titel: 'Vierecke: Eigenschaften', klasse: 'ru-tafel-vierecke' });
    const haus = E['fg-22'];
    const hausHtml = haus ? `<div class="ru-tafel-haus" id="ru-tf-fg-22"${dkl(haus.kl)}>${tfH3('Haus der Vierecke ' + tfKl(haus.kl))}<ol class="ru-tafel-haus-l" aria-label="Von oben (am meisten Eigenschaften) nach unten (am wenigsten)">${haus.geschichtet.map((r) => `<li>${r.map((n) => `<span>${esc(n)}</span>`).join('')}</li>`).join('')}</ol>${tfMerk(haus.merksatz)}
      ${tfMehr('Wer ist Sonderfall von wem?', `<ul class="ru-tafel-liste">${haus.beziehungen.map((b) => `<li>Jedes <b>${esc(b.sonderfall)}</b> ist ein ${esc(b.von)}.</li>`).join('')}</ul><p class="ru-tafel-hinweis">${nb(haus.definition_trapez)}</p>${tfRegeln(kennVonT(haus.regeln))}${aeZeile(tfAe(t, 'fg-22', haus.titel, 'Haus der Vierecke'))}`)}</div>` : '';
    const ko = [...nach('kongruenzsatz'), ...nach('kongruenz_nicht')];
    const km = matrix(['Satz', 'Gegeben', 'Bedingung'], ko.map((e) => ({ anker: e.kennung, kl: e.kl, kopf: `<b class="ru-tafel-gross">${esc(e.kuerzel || 'WWW')}</b>`, klasse: e.art === 'kongruenz_nicht' ? 'ru-tafel-nicht' : '',
      zellen: e.art === 'kongruenz_nicht' ? [`<b>Reicht nicht.</b> ${nb(e.merksatz)}`, ''] : [nb(e.gegeben), nb(e.bedingung)],
      detail: `${e.name ? `<p><b>${esc(e.name)}</b></p>` : ''}${e.art === 'kongruenz_nicht' ? '' : tfMerk(e.merksatz)}${tfH3('Beispiel')}<p class="ru-rechnung">${nb(e.beispiel)}</p>${tfRegeln(kennVonT(e.regeln))}${aeZeile(tfAe(t, e.kennung, e.titel, 'Zeile'))}` })), { titel: 'Kongruenzsätze', klasse: 'ru-tafel-kongruenz' });
    return `${tfKarte(t, 'winkel', 'Winkelarten', `${tfAnker(...nach('winkelart').map((e) => 'w-' + e.kennung))}${winkel}`, { klasse: 'ru-tafel-erste' })}
      ${tfKarte(t, 'dreiecke', 'Dreiecke', `${ws ? `<div class="ru-tafel-formelzeile" id="ru-tf-fg-07"${dkl(ws.kl)}><span class="ru-tafel-f ru-tafel-f-gross">${formel(ws.formel)}</span>${tfKl(ws.kl)}<small>${nb(ws.bedingung)}</small></div>${tfMehr('So rechnest du den dritten Winkel aus', eintragFormelDetail(ws) + tfRegeln(kennVonT(ws.regeln)))}` : ''}${dreiecke}`)}
      ${tfKarte(t, 'vierecke', 'Vierecke', `${vm}<p class="ru-tafel-hinweis ru-tafel-legende"><b>✓</b> = gilt immer, <b>–</b> = gilt nicht immer. Zahlen: so viele mindestens. Tippe auf ein Viereck für Bild und Beschreibung.</p>${hausHtml}`)}
      ${tfKarte(t, 'kongruenz', 'Kongruenzsätze', `${km}<p class="ru-tafel-hinweis">Kongruent heißt deckungsgleich. Tippe auf einen Satz für ein Beispiel.</p>`)}`;
  }

  // ---------- Zeichen und Wörter ----------
  function tafelZeichen(t) {
    const E = Object.fromEntries(t.eintraege.map((e) => [e.kennung, e]));
    const bsp = (l) => (l && l.length ? `<ul class="ru-tafel-liste ru-tafel-bsp-liste">${l.map((b) => `<li><span class="ru-rechnung">${nb(b.text)}</span>${b.gilt === true ? ' <span class="ru-tafel-ja">stimmt</span>' : b.gilt === false ? ' <span class="ru-tafel-falsch">stimmt nicht</span>' : ''}</li>`).join('')}</ul>` : '');
    const ARTEN = {
      zeichen: [['Zeichen', 'Sprechweise', 'Bedeutung'], (e) => ({ kopf: `<b class="ru-tafel-zeichen">${esc(e.zeichen)}</b>`, zellen: [esc(e.sprechweise), nb(e.bedeutung)],
        detail: `${bsp(e.beispiele)}${e.merke ? `<p><b>Merke:</b> ${nb(e.merke)}</p>` : ''}${e.bedingung ? `<p><b>Bedingung:</b> ${nb(e.bedingung)}</p>` : ''}${e.auch ? `<p>Auch: <b>${esc(e.auch)}</b></p>` : ''}${e.hinweis ? `<p class="ru-tafel-hinweis">${nb(e.hinweis)}</p>` : ''}` })],
      griechisch: [['Buchstabe', 'Name', 'Wofür'], (e) => ({ kopf: `<b class="ru-tafel-zeichen">${esc(e.buchstabe)}</b>`, zellen: [esc(e.name), nb(e.verwendung)], detail: `<p class="ru-rechnung">${nb(e.beispiel)}</p>${e.schreibung ? `<p class="ru-tafel-hinweis">${esc(e.schreibung === 'klein' ? 'Kleinbuchstabe' : e.schreibung === 'groß' ? 'Großbuchstabe' : e.schreibung)}</p>` : ''}` })],
      fachwort: [['Wort', 'Bedeutung'], (e) => ({ kopf: `<b>${esc(e.begriff)}</b>`, zellen: [nb(e.satz)], detail: `<p class="ru-rechnung">${nb(e.beispiel)}</p>${(e.rolle_im_beispiel || []).length ? `<p class="ru-tafel-rollen">${e.rolle_im_beispiel.map((r) => `<span>${nb(r)}</span>`).join('')}</p>` : ''}` })],
    };
    return (t.abschnitte || []).map((a, i) => { const [kopf, fn] = ARTEN[a.art] || ARTEN.fachwort;
      let liste = a.kennungen.map((k) => E[k]).filter(Boolean); if (a.art === 'fachwort') liste = [...liste].sort((x, y) => x.begriff.localeCompare(y.begriff, 'de'));
      return tfKarte(t, 'ab-' + a.art, esc(a.name), `${matrix(kopf, liste.map((e) => { const z = fn(e); return { ...z, anker: e.kennung, kl: e.kl, detail: z.detail + tfRegeln(kennVonT(e.regeln)) + tfErw(e.ab_klasse_hinweis) + aeZeile(tfAe(t, e.kennung, e.titel, 'Zeile')) }; }), { titel: a.name, klasse: 'ru-tafel-m-' + a.art })}`, { klasse: i ? '' : 'ru-tafel-erste' });
    }).join('') + '<p class="ru-tafel-hinweis">Tippe auf eine Zeile für Beispiele.</p>';
  }

  const TAFEL_SICHT = { formeln: [tafelFormeln, 'Ebene Figuren, Körper und was man sonst noch braucht – auf einen Blick. Tippe auf eine Zeile für Einzelheiten.'],
    einheiten: [tafelEinheiten, ''], 'formeln-flaechen': [tafelFormelKarten, 'Jede Figur mit Zeichnung, Formeln, Bezeichnungen und Beispielen.', true],
    'formeln-koerper': [tafelFormelKarten, 'Jeder Körper mit Schrägbild, Formeln, Bezeichnungen und Beispielen.', true], zahlen: [tafelZahlen, ''], stellenwert: [tafelStellenwert, ''],
    'bruch-dezimal-prozent': [tafelProzent, ''], figuren: [tafelFiguren, ''], 'zeichen-woerter': [tafelZeichen, ''] };
  const sichtTafel = (id) => { const [fn, lead, eltern] = TAFEL_SICHT[id] || [() => '', '']; return tafelSeite(TAFEL[id], fn(TAFEL[id]), lead, eltern); };

  // ---------- Weiche: Adresse → HTML (unbekannte Adresse → Universum) ----------
  function seite(h) {
    let m;
    if ((m = h.match(/^r(\d+)$/)) && REGEL['R' + m[1]]) return sichtRegel('R' + m[1]);
    if ((m = h.match(/^lehrer-r(\d+)$/)) && REGEL['R' + m[1]]) return sichtLehrer('R' + m[1]);
    if (h === 'liste') return sichtListe();
    if ((m = h.match(/^idee-([a-z]+-\d+)$/)) && IDEE['I-' + m[1]]) return sichtIdee('I-' + m[1]);
    if ((m = h.match(/^weise-(\d)$/)) && D.arbeitsweisen[m[1] - 1]) return sichtWeise(+m[1]);
    if ((m = h.match(/^regel-([a-z]+\d+)$/)) && GESETZ[m[1].toUpperCase()]) return sichtGesetz(m[1].toUpperCase());
    if (h === 'tafeln') return sichtUniversum(); // alte Übersicht der Tafeln (Reiter entfallen): Startseite des Universums (ruZeigen setzt die Adresse um)
    if ((m = h.match(/^tafel-([a-z-]+?)(?:\.[a-z0-9-]+)?$/)) && TAFEL[m[1]]) return sichtTafel(m[1]);
    if (h === 'suche') return sichtSuche();
    if (h === 'sonne') return sichtSonne();
    if (h === 'weisen') return sichtWeisen();
    if ((m = h.match(/^gebiet-([a-z]+)$/)) && KUERZEL_ZU[m[1]]) return sichtGebiet(KUERZEL_ZU[m[1]]);
    if ((m = h.match(/^klassen(?:-(\d+))?$/))) { if (m[1] && KL.includes(+m[1])) zustand.klasse = +m[1]; return sichtKlassen(); }
    return sichtUniversum();
  }
  return { seite, gebietName: (k) => KUERZEL_ZU[k] || null };
}

// ===================== In der App: Laden, Kopf, Rahmen, Rückmeldung =====================
let ruDaten = null, ruLadeP = null, ruAktiv = null, ruLetzte = { h: '', e: 0 };
const ruZustand = { klasse: 5, frage: '', bis: 'alle' };
const ruDatenUrl = () => (typeof LERN_SEITE !== 'undefined' && LERN_SEITE ? '../' : '') + 'daten/regeln-universum.json?v=' + APP_VERSION;
function ruDatenHolen() {
  if (ruDaten) return Promise.resolve(ruDaten);
  if (!ruLadeP) ruLadeP = fetch(ruDatenUrl()).then((r) => { if (!r.ok) throw new Error('Das Regel-Universum ist gerade nicht erreichbar (' + r.status + ').'); return r.json(); })
    .then((d) => (ruDaten = ruIndex(d))).finally(() => { ruLadeP = null; });
  return ruLadeP;
}
// Unteradresse: <kind>[-adresse] (Kind) · kind[-adresse] (Eltern sehen die Kinderseite) · lehrer-r<n> · leer = Liste
function ruKontext(arg) {
  const a = String(arg || '').toLowerCase(); let m;
  const nurKind = (h) => (!h || h === 'liste' || h.startsWith('lehrer') ? 'universum' : h); // Kinderseiten zeigen nie das Lehrer-Blatt
  if ((m = a.match(/^(\d+)(?:-(.+))?$/))) return { art: 'kind', kindId: Number(m[1]), h: nurKind(m[2]), praefix: m[1] + '-' };
  if ((m = a.match(/^kind(?:-(.+))?$/))) return { art: 'ansicht', h: nurKind(m[1]), praefix: 'kind-' };
  if ((m = a.match(/^lehrer-(r\d+)$/))) return { art: 'lehrer', h: 'lehrer-' + m[1], praefix: 'kind-' };
  return { art: 'lehrer', h: 'liste', praefix: 'kind-' };
}
const ruLupe = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21"/></svg>';
const RU_DEFS = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><radialGradient id="ru-glanz" cx=".34" cy=".3" r=".8"><stop offset="0" stop-color="#fff" stop-opacity=".5"/><stop offset=".55" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".22"/></radialGradient></defs></svg>';
// „Ändern lassen“: vorhandener Weg schule_rueckmeldung_geben, ohne Einheit, bezug „allgemein“; die Fundstelle (ruFundstelle) und die Art stehen am Anfang des Textes.
const RU_ARTEN = [['fehler', 'Fehler', 'fehler', []], ['vorschlag', 'Vorschlag', 'sonstiges', []], ['frage', 'Frage', 'sonstiges', []]];
const ruVorsatz = (wo) => (art) => `${wo} · ${art}: `;
let ruAeNr = 0;
// Knopf auf/zu: das Formular steht direkt unter der Zeile des Knopfs (im Listeneintrag am Ende), nach dem Senden kurze Bestätigung, dann zu
function ruAendernUmschalten(b, wurzel) {
  const id = b.dataset.aeId || (b.dataset.aeId = String(++ruAeNr));
  const offen = wurzel.querySelector(`.ru-rueck-form[data-fuer="${id}"]`);
  if (offen) { offen.remove(); b.setAttribute('aria-expanded', 'false'); return; }
  const wo = b.dataset.wo, box = el('div', { class: 'ru-rueck-form ru-ganz', 'data-fuer': id });
  const fertig = () => { if (!box.isConnected) return; const mitFokus = box.contains(document.activeElement); box.remove(); b.setAttribute('aria-expanded', 'false'); if (mitFokus) b.focus({ preventScroll: true }); b.classList.add('ru-ae-ok'); b.lastChild.textContent = 'Gesendet';
    const ansage = wurzel.querySelector('.ru-ae-ansage'); if (ansage) ansage.textContent = 'Auftrag gesendet: ' + wo;
    setTimeout(() => { b.classList.remove('ru-ae-ok'); b.lastChild.textContent = 'Ändern lassen'; }, 4000); };
  box.append(lernAuftragForm({}, { bezug: 'allgemein', wo, arten: RU_ARTEN, art: 'vorschlag', vorsatz: ruVorsatz(wo), onGesendet: () => setTimeout(fertig, 1400) }));
  const ort = b.closest('.ru-zeichnung, .ru-ae-kopf, .ru-ae-zeile, .ru-l-kopf, .ru-ae-in, .ru-schicht-kopf, li') || b;
  if (ort.tagName === 'LI') ort.append(box); else ort.after(box);
  b.setAttribute('aria-expanded', 'true');
  box.querySelector('textarea')?.focus({ preventScroll: true });
}

async function viewRegeln(arg) {
  const k = ruKontext(arg);
  // Kinder-Zugang (eigene Lernen-Seite): nur die eigene Kinderansicht
  if (typeof lernIch !== 'undefined' && lernIch?.rolle === 'kind' && (k.art !== 'kind' || k.kindId !== Number(lernIch.lernender_id))) { route('regeln', String(lernIch.lernender_id)); return; }
  const istKind = k.art === 'kind';
  setChrome(k.art === 'lehrer' ? 'Regeln' : 'Regel-Universum', { back: true, showTabs: false });
  document.body.toggleAttribute('data-kindmodus', istKind);
  const live = viewGuard();
  const schluessel = istKind ? 'kind:' + k.kindId : 'eltern'; // Eltern: Liste, Blatt und Kinderansicht teilen Kopf und Suchfeld
  const weiter = ruAktiv && ruAktiv.schluessel === schluessel && ruAktiv.wurzel.isConnected;
  if (!weiter && !ruDaten) loading('Regel-Universum wird geladen …');
  const kindP = istKind && !weiter ? lernLadeKind(k.kindId, { still: true }).then((d) => d?.kind || null).catch(() => null) : Promise.resolve(null);
  let I; try { I = await ruDatenHolen(); } catch (err) { if (live()) ruFehler(err, istKind ? (await kindP) || { id: k.kindId } : null); return; }
  const kind = await kindP;
  if (!live()) return;
  if (!weiter) ruAktiv = ruAufbauen(I, k, kind || (istKind ? { id: k.kindId } : null), schluessel);
  ruZeigen(k.h);
}
// Daten nicht geladen (kein Netz, Serverfehler): verständliche Meldung mit „Noch einmal versuchen“; beim Kind im eigenen Rahmen (Menü bleibt)
function ruFehler(err, kind) {
  ruAktiv = null;
  const box = el('section', { class: 'card lern-fehlerseite ru-fehler', role: 'alert' }, el('h2', {}, 'Das Regel-Universum lädt gerade nicht.'),
    el('p', {}, 'Prüfe das Internet und versuch es noch einmal.'),
    el('button', { type: 'button', class: 'primary', onclick: () => render() }, 'Noch einmal versuchen'),
    el('p', { class: 'small muted' }, String(err?.message || err)));
  lernErsetze(main, kind ? lernRahmen(kind, 'regeln', box) : box);
}
function ruAufbauen(I, k, kind, schluessel) {
  const ziel = (h) => (h === 'liste' ? '#/regeln' : h.startsWith('lehrer-') ? '#/regeln/' + h : '#/regeln/' + k.praefix + h);
  const g = kind ? (lernGestaltung(kind) === 'tag' ? 'hell' : lernGestaltung(kind) === 'nacht' ? 'nacht' : matchMedia('(prefers-color-scheme: dark)').matches ? 'nacht' : 'hell')
    : matchMedia('(prefers-color-scheme: dark)').matches ? 'nacht' : 'hell';
  // Rolle wie in der übrigen App (lernRolle): Ist ein Kind angemeldet, gibt es nie „Ändern lassen“. Öffnet ein angemeldeter Erwachsener
  // in der Eltern-App die Universum-Ansicht eines Kindes (#/regeln/<id>-…), sieht er den Knopf – wie auf den Flugseiten (leitung). Entscheidung des Nutzers 27.11.
  const alsKind = typeof lernRolle !== 'function' || lernRolle() === 'kind';
  const sichten = ruSichten(I, ziel, ruZustand, alsKind ? 'kind' : k.art === 'kind' ? 'leitung' : 'ansicht');
  ruLetzte = { h: '', e: 0 };
  const lupe = el('span', { class: 'ru-lupe', 'aria-hidden': 'true' }); lupe.innerHTML = ruLupe;
  const feld = el('input', { type: 'search', name: 'q', placeholder: 'Suchen', autocomplete: 'off', enterkeyhint: 'search' });
  const suchen = () => { ruZustand.frage = feld.value.trim(); if (location.hash !== ziel('suche')) location.hash = ziel('suche'); else ruZeigen('suche'); };
  feld.addEventListener('input', () => { if (I.sofort(feld.value)) suchen(); }); // ab drei Zeichen; kürzer nur Tafel-Zeichen, Einheiten, Kurzwörter (π, ≤, cm, %)
  const kopf = el('header', { class: 'ru-kopf' }, el('div', { class: 'ru-breite ru-schmal-k' },
    el('a', { class: 'ru-kopf-marke', href: ziel('universum') }, el('i', { 'aria-hidden': 'true' }), el('span', {}, 'Regel-Universum')),
    el('form', { class: 'ru-suche', role: 'search', onsubmit: (ev) => { ev.preventDefault(); suchen(); feld.blur(); } },
      el('label', {}, el('span', { class: 'ru-unsichtbar' }, 'Im Regel-Universum suchen'), lupe, feld))));
  const seite = el('div', { class: 'ru-seite' });
  // Menü verkürzt: das Merkheft gehört zum Regel-Universum – beim Kind ein Einstieg „Mein Merkheft“ in der Kopfzeile (neben Suche und Menü)
  if (k.art === 'kind' && kind?.id) kopf.firstChild.append(el('a', { class: 'ru-merkheft-link', href: `#/merkheft/${kind.id}` }, el('span', { 'aria-hidden': 'true' }, '📒 '), 'Mein Merkheft'));
  const wurzel = el('div', { class: 'ru' + (k.art === 'kind' ? ' ru-im-kind' : ' ru-in-app'), 'data-ru-g': g }, kopf, seite, el('p', { class: 'ru-unsichtbar ru-ae-ansage', role: 'status' }));
  wurzel.insertAdjacentHTML('afterbegin', RU_DEFS);
  const zurSchicht = (t) => { const s = t.closest && t.closest('.ru-sc-ziel'); if (s) wurzel.querySelector('#ru-schicht-' + s.dataset.schicht)?.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' }); return !!s; };
  seite.addEventListener('keydown', (ev) => { if ((ev.key === 'Enter' || ev.key === ' ') && zurSchicht(ev.target)) ev.preventDefault(); });
  seite.addEventListener('click', (ev) => {
    if (zurSchicht(ev.target)) return;
    if (ruTafelKlick(ev.target, seite)) return;
    const t = ev.target.closest('[data-thema-id]');
    if (t && typeof lernMx !== 'undefined') { const id = Number(t.dataset.themaId); if (lernMx) lernMx.sel = id; else lernMx = { sa: 'gym_by', kind: null, sel: id, q: '', inhalt: '' }; return; }
    const b = ev.target.closest('.ru-ae'); if (!b || alsKind) return;
    ruAendernUmschalten(b, wurzel);
  });
  const rahmen = kind ? lernRahmen(kind, 'regeln', wurzel) : wurzel;
  // Werkstatt 1079: kein doppelter Kopf beim Kind – der Menüknopf der Kinderseite (obere Menüzeile) wandert in die Zeile der Suche
  const menue = kind && rahmen.querySelector('.lr-menue-zeile:not(.unten) .lr-menue');
  if (menue) { const zeile = menue.closest('.lr-menue-zeile'); kopf.firstChild.append(el('span', { class: 'ru-menue-ort' }, menue)); zeile.remove(); }
  lernErsetze(main, rahmen);
  return { schluessel, wurzel, seite, sichten, feld, ziel };
}
// Tafeln: Zeile aufklappen, Klassenfilter („bis Klasse“, bleibt beim Blättern zwischen Tafeln stehen), Drucken (alles aufgeklappt)
function ruTafelZeile(knopf, auf) {
  const d = knopf && document.getElementById(knopf.getAttribute('aria-controls')); if (!d) return;
  const offen = auf ?? d.hidden; d.hidden = !offen; knopf.setAttribute('aria-expanded', String(offen));
}
function ruTafelFilter(seite) {
  const bis = ruZustand.bis || 'alle';
  for (const b of seite.querySelectorAll('.ru-tafel-kf button')) b.setAttribute('aria-pressed', String(b.dataset.bis === bis));
  for (const x of seite.querySelectorAll('.ru-tafel-seite [data-kl]')) x.toggleAttribute('data-aus', bis !== 'alle' && Number(x.dataset.kl) > Number(bis));
}
function ruTafelKlick(ziel, seite) {
  const auf = ziel.closest('.ru-tafel-auf'); if (auf) { ruTafelZeile(auf); return true; }
  const kf = ziel.closest('.ru-tafel-kf button'); if (kf) { ruZustand.bis = kf.dataset.bis; ruTafelFilter(seite); return true; }
  if (ziel.closest('.ru-tafel-drucken')) {
    const zu = [...seite.querySelectorAll('.ru-tafel-seite details:not([open])')], knoepfe = [...seite.querySelectorAll('.ru-tafel-auf[aria-expanded="false"]')];
    zu.forEach((d) => { d.open = true; }); knoepfe.forEach((k) => ruTafelZeile(k, true));
    addEventListener('afterprint', () => { zu.forEach((d) => { d.open = false; }); knoepfe.forEach((k) => ruTafelZeile(k, false)); }, { once: true });
    print(); return true;
  }
  return false;
}
// Sprung an eine Stelle der Tafel (Suche, Verweis): Abschnitt aufklappen, Zeile mit Einzelheiten öffnen, hinrollen, kurz hervorheben
function ruTafelSprung(seite, anker) {
  const x = seite.querySelector('#ru-tf-' + CSS.escape(anker)); if (!x) return false;
  if (x.closest('[data-aus]')) { ruZustand.bis = 'alle'; ruTafelFilter(seite); }
  for (let d = x.closest('details'); d; d = d.parentElement.closest('details')) d.open = true;
  if (x.tagName === 'DETAILS') x.open = true;
  const knopf = x.querySelector(':scope > tr .ru-tafel-auf'); if (knopf) ruTafelZeile(knopf, true);
  x.scrollIntoView({ block: 'start' });
  x.classList.add('ru-tafel-ziel'); setTimeout(() => x.classList.remove('ru-tafel-ziel'), 2200);
  return true;
}
function ruZeigen(h) {
  const { seite, sichten, feld } = ruAktiv;
  if (h === 'tafeln') { history.replaceState(null, '', ruAktiv.ziel('universum')); h = 'universum'; } // alte Route der Tafel-Übersicht → Startseite
  // Gebiet, aus dem man kommt (Brotkrumen der Tafeln): Gebiet oder Sonne; Tafel-Seiten behalten es, alles andere setzt es zurück
  const gm = h.match(/^gebiet-([a-z]+)$/);
  if (gm) ruZustand.gebiet = (ruAktiv.sichten.gebietName || (() => null))(gm[1]); else if (h === 'sonne') ruZustand.gebiet = 'Sonne'; else if (!h.startsWith('tafel-')) ruZustand.gebiet = null;
  seite.innerHTML = sichten.seite(h);
  const e = ruEbene(h), vorher = ruLetzte;
  ruAktiv.wurzel.classList.toggle('ru-weltraum', e <= 1 && h !== 'liste');
  if (vorher.h && e !== vorher.e && !matchMedia('(prefers-reduced-motion: reduce)').matches && seite.animate)
    seite.animate([{ opacity: 0, transform: `scale(${e > vorher.e ? 0.965 : 1.035})` }, { opacity: 1, transform: 'none' }], { duration: 220, easing: 'cubic-bezier(.2,.7,.2,1)' });
  if (h !== 'suche' && document.activeElement !== feld) feld.value = '';
  // Beim Wechsel der Klasse und in der Suche bleibt die Seite stehen, sonst nach oben
  if (seite.querySelector('.ru-tafel-seite')) ruTafelFilter(seite);
  const anker = (h.match(/^tafel-[a-z-]+?\.([a-z0-9-]+)$/) || [])[1];
  if (anker && ruTafelSprung(seite, anker)) { ruLetzte = { h, e }; return; }
  if (!(h.startsWith('klassen') && vorher.h.startsWith('klassen')) && h !== 'suche') scrollTo(0, 0);
  ruLetzte = { h, e };
}
