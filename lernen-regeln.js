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
  const wort = (s) => String(s).toLowerCase().replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss').replace(/<[^>]+>/g, ' ');
  const woerter = (s, ab) => wort(s).split(/[^a-z0-9]+/).filter((w) => w.length > ab);
  const STICH = {}; D.stichwoerter.forEach((s) => { (STICH[s.ziel] ||= []).push(s.wort); });
  const SUCHBAR = [
    ...D.regeln.map((r) => ({ id: r.id, art: 'Rechenregel ' + r.nr, name: r.name, satz: r.satz, mehr: LEITER[r.id].stufen.map((k) => k.text || '').join(' ') + ' ' + r.fehler, ort: 'Sonne · Rechenregeln', ziel: adr.regel(r.id) })),
    ...D.gesetze.map((g) => { const i = ideeVon(g.id); return { id: g.id, art: 'Regel ' + g.id, name: g.name, satz: g.satz, mehr: (g.klassen || []).map((k) => k.text).join(' ') + ' ' + (g.fehler || '') + ' ' + (g.beispiel || ''), ort: g.planet + (i ? ' › ' + i.kurz : ''), ziel: adr.gesetz(g.id) }; }),
    ...IDEEN.map((i) => ({ id: i.id, art: 'Tragende Idee', name: i.kurz, satz: i.satz, mehr: '', ort: i.planet, ziel: adr.idee(i.id) })),
    ...D.formeln.map((f) => ({ id: 'formel ' + f.fuer, art: 'Formel', name: f.fuer, satz: f.formel, mehr: '', ort: GESETZ[f.ziel].planet + ' › ' + f.ziel, ziel: adr.gesetz(f.ziel) })),
    ...D.arbeitsweisen.map((a, n) => ({ id: a.name, art: 'Arbeitsweise', name: a.name, satz: a.satz, mehr: (a.kurz || '') + ' ' + ((a.beispiel || {}).text || ''), ort: 'Arbeitsweisen', ziel: adr.weise(n + 1) })),
  ].map((e) => ({ ...e, stich: STICH[e.id] || [], wn: woerter(e.name, 2), wk: (STICH[e.id] || []).map((s) => woerter(s, 2)), ws: woerter(e.satz, 3), wm: woerter(e.mehr, 3) }));
  function suche(q) {
    const teile = woerter(q, 1); if (!teile.length) return [];
    const trifft = (liste, t) => liste.some((w) => w === t || (t.length >= 4 && w.includes(t)) || (w.length >= 5 && t.includes(w)));
    return SUCHBAR.map((e) => { let p = 0, ueber = null; for (const t of teile) { const k = e.wk.findIndex((l) => trifft(l, t)); if (k >= 0) { p += e.wk[k].includes(t) ? 9 : 5; ueber = e.stich[k]; }
      p += (trifft(e.wn, t) ? 6 : 0) + (trifft(e.ws, t) ? 3 : 0) + (trifft(e.wm, t) ? 1 : 0); } return { ...e, p, ueber }; })
      .filter((x) => x.p > 0).sort((a, b) => b.p - a.p || (a.art === 'Formel') - (b.art === 'Formel')).slice(0, 14);
  }
  return { D, LEITER, KURZ, LEHRER, REGEL, GESETZ, ETAGE, PLANETEN, PLANET, KUERZEL_ZU, IDEE, IDEEN, ideeVon, thema, klasseVon, bandStufen, spanneText,
    brauchtRegeln, ideeBraucht, regelTraegt, erklaertUeber, hilftBei, zahlGesetze, felder, adr, suche };
}

// Ebene einer Adresse: 0 Universum · 1 Sonne, Gebiet, Arbeitsweisen, Klassen, Suche · 2 Regel, Idee, Arbeitsweise, Lehrer · 3 einzelne Regel
const ruEbene = (h) => (h === 'universum' || !h ? 0 : /^(sonne|weisen|gebiet-|klassen|suche|liste)/.test(h) ? 1 : h.startsWith('regel-') ? 3 : 2);

// ===================== Seiten als HTML (aus dem Entwurf entwurf7/teile/app.js, Klassen mit Präfix ru-) =====================
// I: ruIndex · ziel(adresse) → href · zustand: { klasse, frage } · ansicht: 'kind' | 'ansicht' (Eltern sehen die Kinderseite) | 'lehrer'
function ruSichten(I, ziel, zustand, ansicht = 'kind') {
  const { D, LEITER, KURZ, LEHRER, REGEL, GESETZ, ETAGE, PLANETEN, PLANET, KUERZEL_ZU, IDEE, IDEEN, adr } = I;
  const esc = ruEsc, KL = RU_KL, Z = ziel;
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
  function klassenLeiter(id) {
    const L = LEITER[id]; if (!L) return ''; const wenige = !REGEL[id] && L.klassen.length <= 2, stufen = L.stufen.filter((s) => s.text || !wenige);
    const maxMarke = Math.max(...L.stufen.filter((s) => s.text).map((s) => s.pos[0][1] - s.pos[0][0])), grenze = Math.max(0, Math.min(14, 30 - maxMarke));
    return `<ol class="ru-leiter ru-gl">${stufen.map((s) => { if (!s.text) return `<li class="ru-luecke"><span class="ru-stufe">${s.klasse}</span><p class="ru-ganz">Kommt in Klasse ${s.klasse} nicht vor: ${esc(s.grund)}.</p></li>`;
      const z = zeileTeile(s, grenze), meta = `<p class="ru-kl ru-ganz">${s.art}${s.thema ? ' · ' + esc(I.thema(s.thema)) : ''}</p>`;
      return `<li><span class="ru-stufe">${s.klasse}</span>${z.vorsatz ? `<p class="ru-rechnung ru-vorsatz ru-ganz">${z.vorsatz}</p>` : ''}<span class="ru-rechnung ru-vor">${z.vor}</span><span class="ru-rechnung ru-ab"><b class="ru-w ru-mk${s.pos[0][1] - s.pos[0][0] <= 13 ? ' ru-fest' : ''}">${z.marke}</b><span class="ru-nach">${z.nach}</span></span>${meta}</li>`; }).join('')}</ol>`;
  }
  const beispielListe = (klassen) => `<ol class="ru-leiter">${klassen.map((k) => `<li><span class="ru-stufe">${k.klasse}</span><div><p class="ru-rechnung">${esc(k.text)}</p><p class="ru-kl">${k.art}${k.thema ? ' · ' + esc(I.thema(k.thema)) : ''}</p></div></li>`).join('')}</ol>`;

  // ---------- Zeichnungen: ein Feld (Stufe „Beispiel“) oder die übrigen Felder („Genau erklärt“) ----------
  const glText = (f) => (f.gl ? `<p class="ru-z-gl">${f.gl.includes(' = ') && !f.gl.includes('class="ru-nb"') && !f.gl.includes('<br>') ? f.gl.replace(' = ', ' <span class="ru-nb">= ') + '</span>' : f.gl}</p>` : '');
  const feldHtml = (f, mitSchritt) => `<div class="ru-z-teil">${mitSchritt && f.pfeil ? `<p class="ru-z-schritt">${f.pfeil}</p>` : ''}${f.kopf ? `<p class="ru-z-kopf">${f.kopf}</p>` : ''}${f.svg}${glText(f)}<p class="ru-z-satz">${f.satz}</p></div>`;
  function felderHtml(felder) {
    const reihen = []; felder.forEach((f) => { if (f.neu || !reihen.length) reihen.push({ titel: f.neu, felder: [] }); reihen[reihen.length - 1].felder.push(f); });
    return `<figure class="ru-zeichnung" data-felder="${felder.length}">${reihen.map((r) => `${r.titel ? `<p class="ru-z-ast">${r.titel}</p>` : ''}<div class="ru-z-reihe" data-n="${r.felder.length}">${r.felder.map((f, i) => `${i ? `<div class="ru-z-pfeil${f.pfeil ? '' : ' ru-leer'}" aria-hidden="true"></div>` : ''}${feldHtml(f, true)}`).join('')}</div>`).join('')}</figure>`;
  }
  function beispiel(id) { // das erste Feld der Hauptzeichnung; ohne Zeichnung das Beispiel der ersten Klasse
    const f = I.felder(id)[0]; if (f) return `<figure class="ru-zeichnung ru-eins" data-felder="1"><div class="ru-z-reihe" data-n="1">${feldHtml(f, false)}</div></figure>`;
    const s = LEITER[id] && LEITER[id].stufen.find((x) => x.text); return s ? `<p class="ru-rechnung ru-gross-r">${mkText(s.text, s.pos, 0, s.text.length)}</p><p class="ru-kl">Klasse ${s.klasse} · ${s.art}</p>` : '';
  }

  // ---------- Bausteine ----------
  const CHEVRON = '<svg class="ru-chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 10l4 4 4-4" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  const stufe = (key, titel, hinweis, inhalt, offen) => `<details class="ru-stufe" data-stufe="${key}"${offen ? ' open' : ''}><summary><span class="ru-st-titel">${titel}</span>${hinweis ? `<span class="ru-st-hinweis">${hinweis}</span>` : ''}${CHEVRON}</summary><div class="ru-st-inhalt">${inhalt}</div></details>`;
  const pfad = (...teile) => `<nav class="ru-pfad" aria-label="Brotkrumen"><a href="${Z('universum')}">‹ Universum</a>${teile.filter(Boolean).map((t) => `<span class="ru-t">›</span>${t}`).join('')}</nav>`;
  const blaettern = (vor, nach) => `<nav class="ru-blaettern" aria-label="Blättern">${vor ? `<a class="ru-vor" href="${vor.href}"><small>‹ ${vor.ueber}</small><span>${esc(vor.name)}</span></a>` : '<span></span>'}${nach ? `<a class="ru-nach" href="${nach.href}"><small>${nach.ueber} ›</small><span>${esc(nach.name)}</span></a>` : '<span></span>'}</nav>`;
  const merksatz = (satz) => `<div class="ru-merk"><p class="ru-ueber">Merksatz</p><p class="ru-merksatz">${satz}</p></div>`;
  const fehlerTeile = (t) => (t || '').split(/\s*Und:\s*/).filter(Boolean);
  const fehlerListe = (t) => `<ul class="ru-fehlerliste">${fehlerTeile(t).map((x) => `<li>${x.charAt(0).toUpperCase() + x.slice(1)}</li>`).join('')}</ul>`;
  const VERGLEICH_OFFEN = false; // Stufe 4 standardmäßig zu (umsetzung7.md, Abschnitt 3: gemessen fast oder mehr als eine Bildschirmhöhe)
  const umschalter = (an) => `<nav class="ru-umschalter" aria-label="Ansicht"><a href="${Z('universum')}"${an === 'aufbau' ? ' aria-current="page"' : ''}>Aufbau</a><a href="${Z('klassen')}"${an === 'klassen' ? ' aria-current="page"' : ''}>Durch die Klassen</a></nav>`;
  // Eltern/Lehrer sehen die Kinderseite: schmale Leiste mit dem Weg zurück zum Blatt
  const elternBand = (rid) => (ansicht === 'ansicht' ? `<div class="ru-lehrer-band ru-band-kind"><span>So sieht es das Kind</span><a class="ru-verweis" href="${rid ? '#/regeln/lehrer-' + rid.toLowerCase() : '#/regeln'}">${rid ? 'Blatt für Eltern und Lehrer ›' : 'Alle Regeln (Eltern und Lehrer) ›'}</a></div>` : '');

  // Ebene 0: das Universum – nur die großen Teile, je eine antippbare Fläche
  function sichtUniversum() {
    const bahnen = PLANETEN.map((p, n) => `<li class="ru-bahn0${n % 2 ? ' ru-rechts' : ''}"><a class="ru-planet0" href="${Z(adr.gebiet(p.name))}">${planetScheibe(p.name, 44)}<span><b>${esc(p.name)}</b><small>${p.ideen.length} tragende Ideen</small></span></a></li>`).join('');
    return `<div class="ru-breite ru-schmal ru-start ru-universum">${elternBand()}<h1 class="ru-titel">Regel-Universum</h1><p class="ru-lead">Alle festen Regeln der Mathematik, Klasse 5 bis 10. Tippe auf einen Teil.</p>${umschalter('aufbau')}
      <a class="ru-sonne0" href="${Z('sonne')}"><span class="ru-s0-kreis" aria-hidden="true"></span><span class="ru-s0-text"><small>Die Sonne · die Grundlage</small><b>14 Rechenregeln</b><small>gelten in jedem Gebiet und jeder Klasse</small></span></a>
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
    const schichten = [1, 2, 3, 4].map((nr) => `<li class="ru-schicht ru-s${nr}"><div class="ru-schicht-kopf" id="ru-schicht-${nr}">${ringBild(nr)}<span class="ru-sk-nr">Schicht ${nr}</span><b>${esc(ETAGE[nr])}</b></div><ul class="ru-zeilen">${D.regeln.filter((r) => r.etage === nr).map((r) => `<li><a class="ru-zeile ru-mit-satz" href="${Z(adr.regel(r.id))}"><span class="ru-z-nr">${r.nr}</span><span class="ru-z-text"><span class="ru-z-name">${esc(r.name)}</span><span class="ru-z-merk">${satzZeile(r.satz)}</span></span>${band(r.id)}</a></li>`).join('')}</ul></li>`).join('');
    return `<div class="ru-breite ru-schmal ru-start">${elternBand()}${pfad()}<header class="ru-e-kopf"><span class="ru-s0-mini" aria-hidden="true"></span><div><p class="ru-ueber">Die Sonne</p><h1>14 Rechenregeln</h1></div></header>
      <p class="ru-lead">In vier Schichten, von den Grundlagen nach außen. Die Schichten ordnen, sie sperren nichts.</p>${sonnenSchnitt()}
      ${LEGENDE}<ol class="ru-schichten">${schichten}</ol>
      <a class="ru-verweis ru-weiter" href="${Z('klassen')}">Dieselben Regeln durch die Klassen ›</a></div>`;
  }
  // Ebene 1: ein Gebiet – seine tragenden Ideen mit Merksatz und Band
  function sichtGebiet(name) {
    const p = PLANET[name], n = PLANETEN.indexOf(p), vor = PLANETEN[n - 1], nach = PLANETEN[n + 1];
    return `<div class="ru-breite ru-schmal ru-start">${elternBand()}${pfad()}<header class="ru-e-kopf">${planetScheibe(p.name, 48)}<div><p class="ru-ueber">Gebiet ${n + 1} von 7</p><h1>${esc(p.name)}</h1></div></header>
      <p class="ru-lead">${p.ideen.length} tragende Ideen. Hinter ihnen stehen ${I.zahlGesetze(p)} einzelne Regeln und Formeln.</p>${LEGENDE}
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
  function genauInhalt(x, id) {
    const rest = id ? I.felder(id).slice(1) : [];
    return `${x.genau ? `<h3 class="ru-ueber">Genau gesagt</h3><p class="ru-fliess">${x.genau}</p>` : ''}${x.warum ? `<h3 class="ru-ueber">Warum das gilt</h3><p class="ru-fliess">${x.warum}</p>` : ''}${x.voraus ? `<h3 class="ru-ueber">Wann sie gilt – und wann nicht</h3><p class="ru-fliess">${x.voraus}</p>` : ''}
      ${rest.length ? `<h3 class="ru-ueber">Weitere Bilder (${rest.length})</h3>${felderHtml(rest)}` : ''}${x.verwandt ? `<h3 class="ru-ueber">Verwandt</h3><p class="ru-fliess">${x.verwandt}</p>` : ''}`;
  }
  const vergleichInhalt = (id) => `<p class="ru-band-zeile">${band(id, { gross: 1 })}</p>${LEGENDE}<p class="ru-markiert"><b>Gelb umrahmt, in jeder Klasse an derselben Stelle:</b> ${esc(LEITER[id].markiert)}</p>${klassenLeiter(id)}`;
  const regelKopf = (r) => `<header class="ru-r-kopf"><p class="ru-ueber ru-mit-ring">${ringBild(r.etage, 26)}Rechenregel ${r.nr} von 14 · Schicht ${r.etage}</p><h1>${esc(r.name)}</h1><p class="ru-kurz">${esc(KURZ[r.id] || '')}</p></header>`;
  function sichtRegel(id) {
    const r = REGEL[id], n = r.nr, vor = REGEL['R' + (n - 1)], nach = REGEL['R' + (n + 1)];
    return `<article class="ru-breite ru-schmal ru-regelseite">${elternBand(id)}${pfad(`<a href="${Z('sonne')}">Sonne</a>`, `<span>Schicht ${r.etage}</span>`)}${regelKopf(r)}${merksatz(r.satz)}
      <section class="ru-bsp"><p class="ru-ueber">Beispiel</p>${beispiel(id)}</section>
      <div class="ru-stufen">${stufe('klassen', `Dieselbe Regel in ${I.spanneText(id)}`, band(id), vergleichInhalt(id), VERGLEICH_OFFEN)}
      ${stufe('genau', 'Genau erklärt', 'warum · wann', genauInhalt(r, id))}
      ${stufe('fehler', 'Typische Fehler', fehlerTeile(r.fehler).length + '', fehlerListe(r.fehler))}
      ${stufe('aufbau', 'Worauf sie aufbaut, was auf ihr aufbaut', aufbauZahl(id) + '', aufbauInhalt(id))}</div>
      ${blaettern(vor && { href: Z(adr.regel(vor.id)), ueber: 'Regel ' + vor.nr, name: vor.name }, nach && { href: Z(adr.regel(nach.id)), ueber: 'Regel ' + nach.nr, name: nach.name })}</article>`;
  }
  // ---------- Seite einer tragenden Idee ----------
  function sichtIdee(id) {
    const i = IDEE[id], k = IDEEN.indexOf(i), vor = IDEEN[k - 1], nach = IDEEN[k + 1], braucht = I.ideeBraucht(i);
    const folge = `<ol class="ru-folge">${i.gesetze.map((gid) => { const g = GESETZ[gid]; return `<li><a class="ru-karte" href="${Z(adr.gesetz(gid))}"><span class="ru-f-name"><span class="ru-nr">${gid}</span> ${esc(g.name)}</span><span class="ru-f-satz">${g.satz}</span></a></li>`; }).join('')}</ol>`;
    return `<article class="ru-breite ru-schmal ru-regelseite">${elternBand()}${pfad(`<a href="${Z(adr.gebiet(i.planet))}">${esc(i.planet)}</a>`)}
      <header class="ru-r-kopf"><p class="ru-ueber">${esc(i.planet)} · tragende Idee ${i.nr} von ${i.von}</p><h1>${esc(i.kurz)}</h1><p class="ru-kurz">${esc(KURZ[id] || '')}</p></header>${merksatz(i.satz)}
      <section class="ru-bsp"><p class="ru-ueber">Beispiel</p>${beispiel(id)}</section>
      <div class="ru-stufen">${stufe('klassen', LEITER[id].klassen.length > 1 ? `Dieselbe Idee in ${I.spanneText(id)}` : `Kommt nur in Klasse ${LEITER[id].klassen[0]} vor`, band(id), vergleichInhalt(id), VERGLEICH_OFFEN)}
      ${stufe('genau', 'Genau erklärt', 'warum', genauInhalt(i, id))}
      ${stufe('folge', 'Die Regeln und Formeln dahinter', i.gesetze.length + '', folge)}
      ${stufe('aufbau', 'Worauf sie aufbaut', braucht.length + '', braucht.length ? `<h3 class="ru-ueber">Benutzt diese Rechenregeln</h3><div class="ru-verweise">${braucht.map(verweisRegel).join('')}</div>` : '<p class="ru-leise">Keine Rechenregel hinterlegt.</p>')}</div>
      ${blaettern(vor && { href: Z(adr.idee(vor.id)), ueber: vor.planet === i.planet ? 'Idee ' + vor.nr : esc(vor.planet), name: vor.kurz }, nach && { href: Z(adr.idee(nach.id)), ueber: nach.planet === i.planet ? 'Idee ' + nach.nr : esc(nach.planet), name: nach.kurz })}</article>`;
  }
  // ---------- Seite einer Arbeitsweise (achte Runde: Kurzbeschreibung, Beispiel, Erklärung vom Mathe-Profi; „Noch offen“ entfällt) ----------
  function sichtWeise(n) {
    const a = D.arbeitsweisen[n - 1], vor = D.arbeitsweisen[n - 2], nach = D.arbeitsweisen[n];
    return `<article class="ru-breite ru-schmal ru-regelseite">${elternBand()}${pfad(`<a href="${Z('weisen')}">Arbeitsweisen</a>`)}
      <header class="ru-r-kopf"><p class="ru-ueber">Arbeitsweise ${n} von 8 · gilt in jedem Gebiet</p><h1>${esc(a.name)}</h1><p class="ru-kurz">${esc(a.kurz)}</p></header>${merksatz(a.satz)}
      <section class="ru-bsp"><p class="ru-ueber">Beispiel</p><p class="ru-fliess ru-bsp-text">${esc(a.beispiel.text)}</p><p class="ru-kl">Klasse ${a.beispiel.klasse}</p></section>
      <div class="ru-stufen">${stufe('genau', 'Genau erklärt', 'wann · worauf achten', `<p class="ru-fliess">${esc(a.erklaerung)}</p>`)}</div>
      ${blaettern(vor && { href: Z(adr.weise(n - 1)), ueber: 'Arbeitsweise ' + (n - 1), name: vor.name }, nach && { href: Z(adr.weise(n + 1)), ueber: 'Arbeitsweise ' + (n + 1), name: nach.name })}</article>`;
  }
  // ---------- Ebene 3: einzelne Regel eines Gebiets ----------
  function sichtGesetz(id) {
    const g = GESETZ[id], i = I.ideeVon(id), br = I.brauchtRegeln(g), k = g.klassen || [];
    const bsp = g.beispiel ? `<p class="ru-fliess ru-bsp-text">${esc(g.beispiel)}</p>` : k.length ? `<p class="ru-rechnung ru-gross-r">${esc(k[0].text)}</p><p class="ru-kl">Klasse ${k[0].klasse} · ${k[0].art}</p>` : '';
    return `<article class="ru-breite ru-schmal ru-regelseite">${elternBand()}${pfad(PLANET[g.planet] ? `<a href="${Z(adr.gebiet(g.planet))}">${esc(g.planet)}</a>` : `<span>${esc(g.planet)}</span>`, i ? `<a href="${Z(adr.idee(i.id))}">${esc(i.kurz)}</a>` : '')}
      <header class="ru-r-kopf"><p class="ru-ueber">Regel ${id} · ${esc(I.klasseVon(g))}</p><h1>${esc(g.name)}</h1></header>${merksatz(g.satz)}
      ${bsp ? `<section class="ru-bsp"><p class="ru-ueber">Beispiel</p>${bsp}</section>` : ''}
      <div class="ru-stufen">${k.length > 1 || (g.beispiel && k.length) ? stufe('klassen', 'In den Klassen', k.length + '', beispielListe(k)) : ''}
      ${g.warum || g.voraus || g.genau ? stufe('genau', 'Genau erklärt', 'warum · wann', genauInhalt(g, '')) : ''}
      ${g.fehler ? stufe('fehler', 'Typische Fehler', fehlerTeile(g.fehler).length + '', fehlerListe(g.fehler)) : ''}
      ${stufe('aufbau', 'Worauf sie aufbaut', (br.length + (i ? 1 : 0)) + '', `${i ? `<h3 class="ru-ueber">Folgt aus der tragenden Idee</h3><div class="ru-verweise"><a class="ru-verweis" href="${Z(adr.idee(i.id))}"><span class="ru-nr">${esc(i.planet)}</span>${esc(i.kurz)}</a></div>` : ''}${br.length ? `<h3 class="ru-ueber">Benutzt diese Rechenregeln</h3><div class="ru-verweise">${br.map(verweisRegel).join('')}</div>` : ''}`)}</div>
      ${bsp || g.warum || g.voraus ? '' : '<div class="ru-z-folgt"><p>Für diese Regel liegen bisher Name, Satz und Klasse vor.</p></div>'}</article>`;
  }

  // ---------- Suche ----------
  function sichtSuche() {
    const FRAGE = zustand.frage, tr = I.suche(FRAGE);
    return `<div class="ru-breite ru-schmal ru-start">${elternBand()}${pfad('<span>Suche</span>')}<h1 class="ru-s-titel">${!FRAGE ? 'Suche' : tr.length ? `${tr.length} Treffer für „${esc(FRAGE)}“` : `Nichts gefunden für „${esc(FRAGE)}“`}</h1>
      ${tr.length ? '' : '<p class="ru-leise ru-s-tipp">Versuch ein einzelnes Wort, zum Beispiel „Kegel“, „Prozent“ oder „Klammer“.</p>'}
      <ol class="ru-treffer">${tr.map((e) => `<li><a class="ru-karte" href="${Z(e.ziel)}"><span class="ru-t-ort">${esc(e.ort)}</span><span class="ru-t-name"><span class="ru-nr">${e.art}</span> ${esc(e.name)}</span>${e.ueber ? `<span class="ru-t-stich">Stichwort „${esc(e.ueber)}“ steht hier</span>` : ''}<span class="ru-t-satz">${e.satz}</span></a></li>`).join('')}</ol></div>`;
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
      <section class="ru-l-abschnitt"><h2>Arbeitsweisen (8)</h2>${weisen}</section></div>`;
  }

  // ---------- Eltern und Lehrer: Blatt einer Rechenregel (regeln-lehrer.md Regel 2, alle Abschnitte offen) ----------
  const rueck = (id, abschnitt) => `<button class="ru-rueck" type="button" data-regel="${id}" data-abschnitt="${abschnitt}" aria-expanded="false">Rückmeldung geben</button>`;
  function sichtLehrer(id) {
    const r = REGEL[id], L = LEHRER[id], kl = L.klassen || {}, liste = (a) => (a && a.length ? a.join(', ') : '–'), lp = L.lehrplan, e = lp ? lp.einfuehrung : {};
    const lpTab = `<table class="ru-lp"><thead><tr><th scope="col">Schulart</th><th scope="col">Eingeführt in</th><th scope="col">Kommt vor in</th></tr></thead><tbody>
      <tr><td>Gymnasium Bayern</td><td>${e.klasse_gymnasium ? `Klasse ${e.klasse_gymnasium}<br><span class="ru-leise">${esc(e.lernbereich_gymnasium)}</span>` : '–'}</td><td>${liste(kl.gym_by)}</td></tr>
      <tr><td>Realschule Bayern</td><td>${e.realschule_klasse ? `Klasse ${e.realschule_klasse}<br><span class="ru-leise">${esc(e.lernbereich_realschule)}</span>` : '–'}</td><td>${liste(kl.rs_by)}</td></tr>
      <tr><td>IB MYP (Jahr)</td><td>${e.ib_myp_jahr ? `Jahr ${e.ib_myp_jahr}<br><span class="ru-leise">${esc(e.lernbereich_ib)}</span>` : '–'}</td><td>${liste(kl.ib_myp)}</td></tr></tbody></table>`;
    const lpMehr = lp ? `${(e.lehrplan_stichworte_gymnasium || []).length ? `<p class="ru-klein ru-lp-zeile"><b>Stichworte im Lehrplan (Gymnasium, Thema ${esc(e.titel)}):</b> ${e.lehrplan_stichworte_gymnasium.map(esc).join(' · ')}</p>` : ''}
      <ul class="ru-lp-klassen">${lp.klassen.map((k) => `<li><span class="ru-stufe-k">${k.klasse}</span><span>${esc(k.art)} · ${esc(I.thema(k.thema))}<br><span class="ru-leise">${esc(k.lernbereich_gymnasium || '')}</span></span></li>`).join('')}</ul>
      <p class="ru-klein ru-leise">${esc(lp.befund)} <b>Nicht geprüft:</b> ${lp.nicht_geprueft.map(esc).join('; ')}. Quelle: Mathe-Profi (texte8/lehrplan.json, Stand 27.11.2026) aus themenliste.json und der Lehrplan-Kopie der App.</p>` : '<p class="ru-klein ru-leise"><b>Nicht geprüft:</b> kein Lehrplan-Bezug hinterlegt.</p>';
    const themen = `<ul class="ru-lverweise">${L.themen.map((t) => `<li><span>${esc(t.ort ? t.ort + ' · ' + t.titel : t.titel)}</span><a class="ru-verweis ru-klein-v" href="#/lehrplan"${t.thema_id ? ` data-thema-id="${t.thema_id}"` : ''}>Lehrer-Seite ›</a></li>`).join('')}</ul>`;
    const aufg = L.aufgaben.length ? `<ol class="ru-aufgaben">${L.aufgaben.map((a) => `<li><p class="ru-a-kopf">${esc(a.kopf)}</p><p>${esc(a.text)}</p>${a.auswahl ? `<p class="ru-leise">Auswahl: ${a.auswahl.map(esc).join(' · ')}</p>` : ''}<p><b>Lösung:</b> ${esc(a.loesung)}</p>${a.weg ? `<p class="ru-leise">${esc(a.weg)}</p>` : ''}</li>`).join('')}</ol>` : '<p class="ru-leise">Noch keine passende Aufgabe dieser Regel zugeordnet.</p>';
    const zuo = L.zuordnung ? `<p class="ru-klein ru-zuordnung"><b>Zuordnung ${L.zuordnung.befund === 'passt nicht' ? 'passt nicht' : 'nur teilweise geprüft'} (Stichprobe des Mathe-Profis):</b> ${esc(L.zuordnung.text)}</p>` : '';
    const fb = L.fehlbilder.length ? `<ul class="ru-fehlerliste">${L.fehlbilder.map((f) => `<li>${esc(f.beschreibung)} <span class="ru-kl">${esc(f.kennung)}</span></li>`).join('')}</ul>` : '<p class="ru-leise">Keine Fehlbilder hinterlegt.</p>';
    const ab = (t, inhalt, knopf) => `<section class="ru-l-abschnitt"><div class="ru-l-kopf"><h2>${t}</h2>${knopf || ''}</div>${inhalt}</section>`;
    const n = r.nr, vor = REGEL['R' + (n - 1)], nach = REGEL['R' + (n + 1)];
    return `<article class="ru-breite ru-schmal ru-regelseite ru-lehrer"><div class="ru-lehrer-band"><span>Eltern und Lehrer</span><a class="ru-verweis" href="${Z(adr.regel(id))}">So sieht es das Kind ›</a></div>
      <nav class="ru-pfad" aria-label="Brotkrumen"><a href="#/regeln">‹ Regeln</a><span class="ru-t">›</span><span>Schicht ${r.etage} · ${esc(ETAGE[r.etage])}</span></nav>${regelKopf(r)}
      <p class="ru-klein ru-leise ru-kennung">Kennung ${esc(L.kennung)}</p>
      ${ab('1 Merksatz', merksatz(r.satz) + '<p class="ru-klein ru-leise">Wörtlich wie auf der Seite des Kindes.</p>', rueck(id, 'Merksatz'))}
      ${ab('2 Was das Kind sieht', `<p class="ru-ueber">Beispiel</p>${beispiel(id)}<p class="ru-ueber ru-abstand">Dieselbe Regel in ${I.spanneText(id)}</p>${vergleichInhalt(id)}<p class="ru-ueber ru-abstand">Typische Fehler</p>${fehlerListe(r.fehler)}`, rueck(id, 'Karte'))}
      ${ab('3 Fachliche Erklärung', genauInhalt(r, id), rueck(id, 'Erklärung'))}
      ${ab('4 Verweise und Zuordnung', `<h3 class="ru-ueber">Lehrplan</h3>${lpTab}${lpMehr}<h3 class="ru-ueber">In der App: Themen, die diese Regel üben</h3>${themen}<h3 class="ru-ueber">Beispielaufgaben mit Lösung</h3>${zuo}${aufg}<h3 class="ru-ueber">Fehlbilder, die die App dieser Regel zuordnet</h3>${fb}<h3 class="ru-ueber">Aufbau</h3>${aufbauInhalt(id)}`, rueck(id, 'Zuordnung'))}
      ${ab('5 Stand je Kind', '<p class="ru-leise">Stand folgt (kommt mit Stufe 2, sobald der Server ihn liefert).</p>')}
      ${blaettern(vor && { href: '#/regeln/' + adr.lehrer(vor.id), ueber: 'Regel ' + vor.nr, name: vor.name }, nach && { href: '#/regeln/' + adr.lehrer(nach.id), ueber: 'Regel ' + nach.nr, name: nach.name })}</article>`;
  }

  // ---------- Weiche: Adresse → HTML (unbekannte Adresse → Universum) ----------
  function seite(h) {
    let m;
    if ((m = h.match(/^r(\d+)$/)) && REGEL['R' + m[1]]) return sichtRegel('R' + m[1]);
    if ((m = h.match(/^lehrer-r(\d+)$/)) && REGEL['R' + m[1]]) return sichtLehrer('R' + m[1]);
    if (h === 'liste') return sichtListe();
    if ((m = h.match(/^idee-([a-z]+-\d+)$/)) && IDEE['I-' + m[1]]) return sichtIdee('I-' + m[1]);
    if ((m = h.match(/^weise-(\d)$/)) && D.arbeitsweisen[m[1] - 1]) return sichtWeise(+m[1]);
    if ((m = h.match(/^regel-([a-z]+\d+)$/)) && GESETZ[m[1].toUpperCase()]) return sichtGesetz(m[1].toUpperCase());
    if (h === 'suche') return sichtSuche();
    if (h === 'sonne') return sichtSonne();
    if (h === 'weisen') return sichtWeisen();
    if ((m = h.match(/^gebiet-([a-z]+)$/)) && KUERZEL_ZU[m[1]]) return sichtGebiet(KUERZEL_ZU[m[1]]);
    if ((m = h.match(/^klassen(?:-(\d+))?$/))) { if (m[1] && KL.includes(+m[1])) zustand.klasse = +m[1]; return sichtKlassen(); }
    return sichtUniversum();
  }
  return { seite };
}

// ===================== In der App: Laden, Kopf, Rahmen, Rückmeldung =====================
let ruDaten = null, ruLadeP = null, ruAktiv = null, ruLetzte = { h: '', e: 0 };
const ruZustand = { klasse: 5, frage: '' };
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
// Rückmeldung (Lehrer-Blatt): vorhandener Weg schule_rueckmeldung_geben, ohne Einheit, bezug „allgemein“; Regel und Abschnitt stehen am Anfang des Textes.
const RU_ARTEN = [['fehler', 'Fehler', 'fehler', []], ['vorschlag', 'Vorschlag', 'sonstiges', []], ['frage', 'Frage', 'sonstiges', []]];
const ruRueckVorsatz = (r, kennung, abschnitt) => (art) => `Regel ${r.nr} · ${r.name} (${kennung}) · ${abschnitt} · ${art}: `;

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
  const sichten = ruSichten(I, ziel, ruZustand, k.art === 'kind' ? 'kind' : 'ansicht');
  ruLetzte = { h: '', e: 0 };
  const lupe = el('span', { class: 'ru-lupe', 'aria-hidden': 'true' }); lupe.innerHTML = ruLupe;
  const feld = el('input', { type: 'search', name: 'q', placeholder: 'Suchen', autocomplete: 'off', enterkeyhint: 'search' });
  const suchen = () => { ruZustand.frage = feld.value.trim(); if (location.hash !== ziel('suche')) location.hash = ziel('suche'); else ruZeigen('suche'); };
  feld.addEventListener('input', () => { if (feld.value.trim().length >= 3) suchen(); });
  const kopf = el('header', { class: 'ru-kopf' }, el('div', { class: 'ru-breite ru-schmal-k' },
    el('a', { class: 'ru-kopf-marke', href: ziel('universum') }, el('i', { 'aria-hidden': 'true' }), el('span', {}, 'Regel-Universum')),
    el('form', { class: 'ru-suche', role: 'search', onsubmit: (ev) => { ev.preventDefault(); suchen(); feld.blur(); } },
      el('label', {}, el('span', { class: 'ru-unsichtbar' }, 'Im Regel-Universum suchen'), lupe, feld))));
  const seite = el('div', { class: 'ru-seite' });
  // Menü verkürzt: das Merkheft gehört zum Regel-Universum – beim Kind ein Einstieg „Mein Merkheft“ in der Kopfzeile (neben Suche und Menü)
  if (k.art === 'kind' && kind?.id) kopf.firstChild.append(el('a', { class: 'ru-merkheft-link', href: `#/merkheft/${kind.id}` }, el('span', { 'aria-hidden': 'true' }, '📒 '), 'Mein Merkheft'));
  const wurzel = el('div', { class: 'ru' + (k.art === 'kind' ? ' ru-im-kind' : ' ru-in-app'), 'data-ru-g': g }, kopf, seite);
  wurzel.insertAdjacentHTML('afterbegin', RU_DEFS);
  const zurSchicht = (t) => { const s = t.closest && t.closest('.ru-sc-ziel'); if (s) wurzel.querySelector('#ru-schicht-' + s.dataset.schicht)?.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' }); return !!s; };
  seite.addEventListener('keydown', (ev) => { if ((ev.key === 'Enter' || ev.key === ' ') && zurSchicht(ev.target)) ev.preventDefault(); });
  seite.addEventListener('click', (ev) => {
    if (zurSchicht(ev.target)) return;
    const t = ev.target.closest('[data-thema-id]');
    if (t && typeof lernMx !== 'undefined') { const id = Number(t.dataset.themaId); if (lernMx) lernMx.sel = id; else lernMx = { sa: 'gym_by', kind: null, sel: id, q: '', inhalt: '' }; return; }
    const b = ev.target.closest('.ru-rueck'); if (!b) return;
    const kopfZeile = b.closest('.ru-l-kopf'), offen = kopfZeile.nextElementSibling?.classList.contains('ru-rueck-form');
    if (offen) { kopfZeile.nextElementSibling.remove(); b.setAttribute('aria-expanded', 'false'); return; }
    const r = I.REGEL[b.dataset.regel], kennung = I.LEHRER[r.id].kennung, abschnitt = b.dataset.abschnitt;
    kopfZeile.after(el('div', { class: 'ru-rueck-form' }, lernAuftragForm({}, { bezug: 'allgemein', wo: `Regel ${r.nr} · ${r.name} · ${abschnitt}`, arten: RU_ARTEN, art: 'vorschlag', vorsatz: ruRueckVorsatz(r, kennung, abschnitt) })));
    b.setAttribute('aria-expanded', 'true');
  });
  const rahmen = kind ? lernRahmen(kind, 'regeln', wurzel) : wurzel;
  // Werkstatt 1079: kein doppelter Kopf beim Kind – der Menüknopf der Kinderseite (obere Menüzeile) wandert in die Zeile der Suche
  const menue = kind && rahmen.querySelector('.lr-menue-zeile:not(.unten) .lr-menue');
  if (menue) { const zeile = menue.closest('.lr-menue-zeile'); kopf.firstChild.append(el('span', { class: 'ru-menue-ort' }, menue)); zeile.remove(); }
  lernErsetze(main, rahmen);
  return { schluessel, wurzel, seite, sichten, feld, ziel };
}
function ruZeigen(h) {
  const { seite, sichten, feld } = ruAktiv;
  seite.innerHTML = sichten.seite(h);
  const e = ruEbene(h), vorher = ruLetzte;
  ruAktiv.wurzel.classList.toggle('ru-weltraum', e <= 1 && h !== 'liste');
  if (vorher.h && e !== vorher.e && !matchMedia('(prefers-reduced-motion: reduce)').matches && seite.animate)
    seite.animate([{ opacity: 0, transform: `scale(${e > vorher.e ? 0.965 : 1.035})` }, { opacity: 1, transform: 'none' }], { duration: 220, easing: 'cubic-bezier(.2,.7,.2,1)' });
  if (h !== 'suche' && document.activeElement !== feld) feld.value = '';
  // Beim Wechsel der Klasse und in der Suche bleibt die Seite stehen, sonst nach oben
  if (!(h.startsWith('klassen') && vorher.h.startsWith('klassen')) && h !== 'suche') scrollTo(0, 0);
  ruLetzte = { h, e };
}
