// Regel-Universum, siebte Runde: alle Ansichten in einer Datei, umgeschaltet über einfache #-Sprünge.
// #universum (Start, Ebene 0) · #sonne, #gebiet-zahlen, #weisen (Ebene 1) · #klassen, #klassen-7 · #r6 · #idee-geo-1 · #weise-3 · #regel-F17 · #suche · #lehrer-r6
// Inhalt wörtlich aus INHALT (Mathe-Profi). Kurzbeschreibungen aus DATEN.kurz (gekürzt vom Designer, zu prüfen).

// ---------- Hell / dunkel: Variable, gemerkt nur, wenn localStorage geht ----------
let THEMA = 'hell';
try { THEMA = localStorage.getItem('ru-thema') || (matchMedia('(prefers-color-scheme: dark)').matches ? 'nacht' : 'hell'); } catch (e) { /* ohne Speicher: hell */ }
document.body.dataset.g = THEMA;
const setzeThema = (t) => { THEMA = t; document.body.dataset.g = t; try { localStorage.setItem('ru-thema', t); } catch (e) { /* egal */ } };

// ---------- Daten ----------
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const KURZ = DATEN.kurz, LEHRER = DATEN.lehrer, LEITER = INHALT.leitern, KL = [5, 6, 7, 8, 9, 10];
const REGEL = Object.fromEntries(INHALT.regeln.map((r) => [r.id, r]));
const GESETZ = Object.fromEntries(INHALT.gesetze.map((g) => [g.id, g]));
const ETAGE = Object.fromEntries(INHALT.etagen.map((e) => [e.nr, e.name]));
const PLANETEN = INHALT.planeten.filter((p) => PLANET_BILD[p.name]);
const IDEE = {}; for (const p of PLANETEN) p.ideen.forEach((i) => { i.id = `I-${KUERZEL[p.name]}-${i.nr}`; i.planet = p.name; i.von = p.ideen.length; IDEE[i.id] = i; });
const IDEEN = Object.values(IDEE);
const ideeVon = (gid) => IDEEN.find((i) => i.gesetze.includes(gid));
const thema = (k) => (INHALT.themen[k] ? `${INHALT.themen[k].ort} · ${INHALT.themen[k].titel}` : k);
const klasseVon = (g) => (g.gym && g.gym !== '–' ? 'Klasse ' + g.gym : 'Realschule oder IB');
const planetScheibe = (name, gr = 28) => `<svg class="scheibe" width="${gr}" height="${gr}" viewBox="-22 -22 44 44" aria-hidden="true"><circle r="21" fill="${PLANET_BILD[name].farbe}"/><circle r="21" fill="url(#glanz)"/>${PLANET_BILD[name].zeichen}</svg>`;
const ART_KURZ = { Einführung: 'E', Anwendung: 'A', Vorwissen: 'V' }, STUFE_WORT = { E: 'eingeführt', A: 'angewendet', V: 'Vorwissen', N: 'kommt nicht vor' };
const bandStufen = (id) => Object.fromEntries(LEITER[id].stufen.map((s) => [s.klasse, s.text ? ART_KURZ[s.art] : 'N']));
const spanneText = (id) => { const k = LEITER[id].klassen; return k.length === 1 ? `Klasse ${k[0]}` : `Klasse ${k[0]} bis ${k[k.length - 1]}`; };
// Schmales Klassenband: sechs Kästchen ohne Ziffern (die Ziffern stehen einmal je Schicht darüber)
// Achte Runde: drei Zustände, die Klasse steht im Kästchen. neu = eingeführt · da = angewendet oder Vorwissen · nicht = kommt nicht vor
const DREI = { E: 'neu', A: 'da', V: 'da', N: 'nicht' }, DREI_WORT = { neu: 'neu', da: 'kommt vor', nicht: 'kommt nicht vor' };
const band = (id, o = {}) => { const st = bandStufen(id); return `<span class="b6${o.gross ? ' gross' : ''}" role="img" aria-label="Klassen: ${KL.map((k) => `${k} ${DREI_WORT[DREI[st[k]]]}`).join(', ')}">${KL.map((k) => `<i class="${DREI[st[k]]}">${k}</i>`).join('')}</span>`; };
const LEGENDE = `<p class="legende"><span class="b6"><i class="neu">5</i></span>neu <span class="b6"><i class="da">6</i></span>kommt vor <span class="b6"><i class="nicht">9</i></span>kommt nicht vor</p>`;
// Kleines Bild der Schicht: vier Ringe von innen nach außen, die eigene Schicht kräftig, die anderen blass
const SF = ['', 'var(--s1)', 'var(--s2)', 'var(--s3)', 'var(--s4)'];
const ringBild = (nr, gr = 34) => `<svg class="ring" width="${gr}" height="${gr}" viewBox="-22 -22 44 44" aria-hidden="true">${[4, 3, 2, 1].map((k) => `<circle r="${k * 5 + 1}" fill="${SF[k]}" opacity="${k === nr ? 1 : 0.3}"${k === nr ? ' stroke="#11161D" stroke-width="1.6"' : ''}/>`).join('')}</svg>`;
// Schnitt durch die Sonne: Halbkreis, vier Bänder von innen nach außen, beschriftet; Tipp springt zur Schicht
function sonnenSchnitt() {
  const R = [0, 56, 98, 140, 182], cy = 190;
  const ring = (k) => `<path d="M${200 - R[k]} ${cy}A${R[k]} ${R[k]} 0 0 1 ${200 + R[k]} ${cy}Z" fill="${SF[k]}"/>`;
  const schrift = (k, y) => `<g class="sc-ziel" data-schicht="${k}" role="button" tabindex="0" aria-label="Schicht ${k}: ${ETAGE[k]}"><rect x="40" y="${y - 19}" width="320" height="28" fill="transparent"/><text x="200" y="${y}" text-anchor="middle" font-family="var(--grotesk)" font-weight="700" font-size="${k === 1 ? 14 : 15}" fill="#11161D"><tspan font-family="var(--mono)" font-weight="800">${k}</tspan>  ${ETAGE[k]}</text></g>`;
  return `<figure class="schnitt"><svg viewBox="0 0 400 ${cy + 2}" role="img" aria-label="Schnitt durch die Sonne: vier Schichten von innen nach außen">${[4, 3, 2, 1].map(ring).join('')}${[4, 3, 2, 1].map((k) => `<path d="M${200 - R[k]} ${cy}A${R[k]} ${R[k]} 0 0 1 ${200 + R[k]} ${cy}" fill="none" stroke="#11161D" stroke-opacity=".35" stroke-width="1.2"/>`).join('')}
    ${schrift(4, cy - 154)}${schrift(3, cy - 112)}${schrift(2, cy - 70)}${schrift(1, cy - 18)}<line x1="6" y1="${cy + 1}" x2="394" y2="${cy + 1}" stroke="var(--text)" stroke-width="2"/></svg><figcaption>Schnitt durch die Sonne: innen die Grundlage, außen, was darauf aufbaut. Tippe eine Schicht an.</figcaption></figure>`;
}
const satzZeile = (t) => t.replace(/<br>/g, ' ');
const brauchtRegeln = (g) => ((g.sonne || '').match(/\d+/g) || []).map((n) => 'R' + n).filter((id) => REGEL[id]);
const ideeBraucht = (i) => [...new Set(i.gesetze.flatMap((gid) => brauchtRegeln(GESETZ[gid])))].sort((a, b) => a.slice(1) - b.slice(1));
const regelTraegt = (rid) => IDEEN.map((i) => ({ i, n: i.gesetze.filter((gid) => brauchtRegeln(GESETZ[gid]).includes(rid)).length })).filter((x) => x.n);
function verweise(text) { const aus = [], s = text || ''; for (const m of s.matchAll(/\b([A-Z]\d+)\b/g)) if (GESETZ[m[1]]) aus.push(m[1]); for (const m of s.matchAll(/Rechenregel (\d+)/g)) aus.push('R' + m[1]);
  for (const r of INHALT.regeln) if (s.includes(r.name)) aus.push(r.id); return [...new Set(aus)]; }
const erklaertUeber = (rid) => verweise(REGEL[rid].weg).filter((x) => REGEL[x]);
const hilftBei = (rid) => INHALT.regeln.filter((r) => erklaertUeber(r.id).includes(rid)).map((r) => r.id);
// Adressen
const adr = { regel: (id) => '#' + id.toLowerCase(), idee: (id) => '#idee-' + id.slice(2), weise: (n) => '#weise-' + n, gesetz: (id) => '#regel-' + id.toLowerCase(), lehrer: (id) => '#lehrer-' + id.toLowerCase() };
const verweisRegel = (id) => `<a class="verweis" href="${adr.regel(id)}"><span class="nr">Regel ${id.slice(1)}</span>${esc(REGEL[id].name)}</a>`;

// ---------- Rechenzeile mit gelb umrahmter Stelle (Klassenleiter, übernommen aus Runde 6) ----------
const mkText = (text, pos, von, bis) => { let aus = '', p = von; for (const [a, e] of pos) { if (e <= von || a >= bis) continue; aus += esc(text.slice(p, a)) + `<b class="w${e - a <= 13 ? ' fest' : ''}">${esc(text.slice(a, e))}</b>`; p = e; } return aus + esc(text.slice(p, bis)); };
function zeileTeile(s, grenze) { const [a, e] = s.pos[0], vor = s.text.slice(0, a); let schnitt = 0;
  if (vor.length > grenze) { const doppel = vor.lastIndexOf(': '); if (doppel >= 0 && vor.length - doppel - 2 <= grenze) schnitt = doppel + 2;
    else { schnitt = -1; for (const m of vor.matchAll(/ (=|→|\|) /g)) if (vor.length - m.index - m[0].length <= grenze) { schnitt = m.index + m[0].length; break; }
      if (schnitt < 0) { schnitt = vor.length; for (let i = 0; i < vor.length; i++) if (vor[i] === ' ' && vor.length - i - 1 <= grenze) { schnitt = i + 1; break; } } } }
  return { vorsatz: mkText(s.text, [], 0, schnitt).trim(), vor: mkText(s.text, [], schnitt, a), marke: esc(s.text.slice(a, e)), nach: mkText(s.text, s.pos.slice(1), e, s.text.length), nVor: a - schnitt }; }
function klassenLeiter(id, o = {}) {
  const L = LEITER[id]; if (!L) return ''; const wenige = !REGEL[id] && L.klassen.length <= 2, stufen = L.stufen.filter((s) => s.text || !wenige);
  const maxMarke = Math.max(...L.stufen.filter((s) => s.text).map((s) => s.pos[0][1] - s.pos[0][0])), grenze = Math.max(0, Math.min(14, 30 - maxMarke));
  return `<ol class="leiter gl">${stufen.map((s) => { if (!s.text) return `<li class="luecke"><span class="stufe">${s.klasse}</span><p class="ganz">Kommt in Klasse ${s.klasse} nicht vor: ${esc(s.grund)}.</p></li>`;
    const z = zeileTeile(s, grenze), meta = o.ohneMeta ? '' : `<p class="kl ganz">${s.art}${s.thema ? ' · ' + esc(thema(s.thema)) : ''}</p>`;
    return `<li><span class="stufe">${s.klasse}</span>${z.vorsatz ? `<p class="rechnung vorsatz ganz">${z.vorsatz}</p>` : ''}<span class="rechnung vor">${z.vor}</span><span class="rechnung ab"><b class="w mk${s.pos[0][1] - s.pos[0][0] <= 13 ? ' fest' : ''}">${z.marke}</b><span class="nach">${z.nach}</span></span>${meta}</li>`; }).join('')}</ol>`;
}
const beispielListe = (klassen) => `<ol class="leiter">${klassen.map((k) => `<li><span class="stufe">${k.klasse}</span><div><p class="rechnung">${esc(k.text)}</p><p class="kl">${k.art}${k.thema ? ' · ' + esc(thema(k.thema)) : ''}</p></div></li>`).join('')}</ol>`;

// ---------- Zeichnungen: ein Feld (Stufe „Beispiel“) oder die übrigen Felder („Genau erklärt“) ----------
const glText = (f) => (f.gl ? `<p class="z-gl">${f.gl.includes(' = ') && !f.gl.includes('class="nb"') && !f.gl.includes('<br>') ? f.gl.replace(' = ', ' <span class="nb">= ') + '</span>' : f.gl}</p>` : '');
const feldHtml = (f, mitSchritt) => `<div class="z-teil">${mitSchritt && f.pfeil ? `<p class="z-schritt">${f.pfeil}</p>` : ''}${f.kopf ? `<p class="z-kopf">${f.kopf}</p>` : ''}${f.svg}${glText(f)}<p class="z-satz">${f.satz}</p></div>`;
function felderHtml(felder) {
  const reihen = []; felder.forEach((f) => { if (f.neu || !reihen.length) reihen.push({ titel: f.neu, felder: [] }); reihen[reihen.length - 1].felder.push(f); });
  return `<figure class="zeichnung" data-felder="${felder.length}">${reihen.map((r) => `${r.titel ? `<p class="z-ast">${r.titel}</p>` : ''}<div class="z-reihe" data-n="${r.felder.length}">${r.felder.map((f, i) => `${i ? `<div class="z-pfeil${f.pfeil ? '' : ' leer'}" aria-hidden="true"></div>` : ''}${feldHtml(f, true)}`).join('')}</div>`).join('')}</figure>`;
}
const felderVon = (id) => (ZEICHNUNGEN[id] ? ZEICHNUNGEN[id]().felder : []);
function beispiel(id) { // das erste Feld der Hauptzeichnung; ohne Zeichnung das Beispiel der ersten Klasse
  const f = felderVon(id)[0]; if (f) return `<figure class="zeichnung eins" data-felder="1"><div class="z-reihe" data-n="1">${feldHtml(f, false)}</div></figure>`;
  const s = LEITER[id] && LEITER[id].stufen.find((x) => x.text); return s ? `<p class="rechnung gross-r">${mkText(s.text, s.pos, 0, s.text.length)}</p><p class="kl">Klasse ${s.klasse} · ${s.art}</p>` : '<p class="leise">Beispiel folgt.</p>';
}

// ---------- Bausteine der Seiten ----------
const CHEVRON = '<svg class="chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 10l4 4 4-4" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
const stufe = (key, titel, hinweis, inhalt, offen) => `<details class="stufe" data-stufe="${key}"${offen ? ' open' : ''}><summary><span class="st-titel">${titel}</span>${hinweis ? `<span class="st-hinweis">${hinweis}</span>` : ''}${CHEVRON}</summary><div class="st-inhalt">${inhalt}</div></details>`;
const pfad = (...teile) => `<nav class="pfad" aria-label="Brotkrumen"><a href="#universum">‹ Universum</a>${teile.filter(Boolean).map((t) => `<span class="t">›</span>${t}`).join('')}</nav>`;
const blaettern = (vor, nach) => `<nav class="blaettern" aria-label="Blättern">${vor ? `<a class="vor" href="${vor.href}"><small>‹ ${vor.ueber}</small><span>${esc(vor.name)}</span></a>` : '<span></span>'}${nach ? `<a class="nach" href="${nach.href}"><small>${nach.ueber} ›</small><span>${esc(nach.name)}</span></a>` : '<span></span>'}</nav>`;
const merksatz = (satz) => `<div class="merk"><p class="ueber">Merksatz</p><p class="merksatz">${satz}</p></div>`;
const fehlerListe = (t) => `<ul class="fehlerliste">${(t || '').split(/\s*Und:\s*/).filter(Boolean).map((x) => `<li>${x.charAt(0).toUpperCase() + x.slice(1)}</li>`).join('')}</ul>`;
const anzahlFehler = (t) => (t || '').split(/\s*Und:\s*/).filter(Boolean).length;
// Stufe 4 standardmäßig offen? Entscheidung nach Messung bei 400 px (umsetzung7.md, Abschnitt 3): zu.
const VERGLEICH_OFFEN = false;

// ---------- Ebenen: 0 Universum · 1 Sonne / Gebiet / Arbeitsweisen · 2 Regel / Idee · 3 einzelne Regel eines Gebiets ----------
const umschalter = (an) => `<nav class="umschalter" aria-label="Ansicht"><a href="#universum"${an === 'aufbau' ? ' aria-current="page"' : ''}>Aufbau</a><a href="#klassen"${an === 'klassen' ? ' aria-current="page"' : ''}>Durch die Klassen</a></nav>`;
const KUERZEL_ZU = Object.fromEntries(Object.entries(KUERZEL).map(([n, k]) => [k, n]));
const adrGebiet = (name) => '#gebiet-' + KUERZEL[name];
const zahlGesetze = (p) => p.ideen.reduce((a, i) => a + i.gesetze.length, 0);

// Ebene 0: das Universum – nur die großen Teile, je eine antippbare Fläche
function sichtUniversum() {
  const bahnen = PLANETEN.map((p, n) => `<li class="bahn0${n % 2 ? ' rechts' : ''}"><a class="planet0" href="${adrGebiet(p.name)}">${planetScheibe(p.name, 44)}<span><b>${esc(p.name)}</b><small>${p.ideen.length} tragende Ideen</small></span></a></li>`).join('');
  return `<div class="breite schmal start universum"><h1 class="titel">Regel-Universum</h1><p class="lead">Alle festen Regeln der Mathematik, Klasse 5 bis 10. Tippe auf einen Teil.</p>${umschalter('aufbau')}
    <a class="sonne0" href="#sonne"><span class="s0-kreis" aria-hidden="true"></span><span class="s0-text"><small>Die Sonne · die Grundlage</small><b>14 Rechenregeln</b><small>gelten in jedem Gebiet und jeder Klasse</small></span></a>
    <p class="u-zwischen">Darum die sieben Gebiete:</p>
    <ol class="bahnen0">${bahnen}</ol>
    <a class="guertel0" href="#weisen"><b>8 Arbeitsweisen</b><small>wie man vorgeht – gilt überall</small></a>${systemBild()}</div>`;
}

// Rechner (ab 900 px): dasselbe als Sonnensystem. Sonne links angeschnitten, Bahnen als Kreisbögen um sie, Planet und Name auf der Bahn.
function systemBild() {
  const cx = -40, cy = 300, rs = 300, dy = [-150, 95, -40, 175, -205, 40, -95], weg = (r) => `M${cx + Math.sqrt(r * r - 290 * 290)} ${cy - 290}A${r} ${r} 0 0 1 ${cx + Math.sqrt(r * r - 290 * 290)} ${cy + 290}`;
  const bahnR = (n) => 400 + n * 78;
  const pl = PLANETEN.map((p, n) => { const r = bahnR(n), y = cy + dy[n], x = cx + Math.sqrt(r * r - dy[n] * dy[n]);
    return `<path d="${weg(r)}" fill="none" stroke="var(--linie)" stroke-width="1.5"/><a href="${adrGebiet(p.name)}" class="sp"><circle cx="${x}" cy="${y}" r="38" fill="transparent"/><g transform="translate(${x} ${y}) scale(1.25)"><circle r="21" fill="${PLANET_BILD[p.name].farbe}"/><circle r="21" fill="url(#glanz)"/>${PLANET_BILD[p.name].zeichen}</g><text x="${x + 36}" y="${y - 2}" font-family="var(--grotesk)" font-weight="700" font-size="19" fill="var(--text)">${esc(p.name)}</text><text x="${x + 36}" y="${y + 19}" font-family="var(--grotesk)" font-weight="500" font-size="15" fill="var(--leise)">${p.ideen.length} tragende Ideen</text></a>`; }).join('');
  const rw = bahnR(7) - 10;
  return `<div class="system" aria-hidden="false"><svg viewBox="0 0 1100 600" role="img" aria-label="Sonnensystem: die Sonne mit 14 Rechenregeln, darum sieben Gebiete, außen die Arbeitsweisen">
    <defs><radialGradient id="sonnenlicht" cx="0" cy=".5" r="1"><stop offset="0" stop-color="#FFD23F" stop-opacity=".35"/><stop offset="1" stop-color="#FFD23F" stop-opacity="0"/></radialGradient></defs>
    <circle cx="${cx}" cy="${cy}" r="${rs + 120}" fill="url(#sonnenlicht)"/>
    <a href="#sonne" class="sp"><circle cx="${cx}" cy="${cy}" r="${rs}" fill="var(--s4)"/><circle cx="${cx}" cy="${cy}" r="${rs - 64}" fill="var(--s3)"/><circle cx="${cx}" cy="${cy}" r="${rs - 128}" fill="var(--s2)"/><circle cx="${cx}" cy="${cy}" r="${rs - 192}" fill="var(--s1)"/>
      <text x="22" y="${cy - 14}" font-family="var(--grotesk)" font-weight="700" font-size="15" fill="#11161D">Die Sonne · die Grundlage</text><text x="22" y="${cy + 17}" font-family="var(--grotesk)" font-weight="700" font-size="28" fill="#11161D">14 Rechenregeln</text><text x="22" y="${cy + 41}" font-family="var(--grotesk)" font-weight="500" font-size="15" fill="#11161D">in vier Schichten</text></a>
    ${pl}
    <path d="${weg(rw)}" fill="none" stroke="var(--leise)" stroke-width="2" stroke-dasharray="6 6"/>
    <a href="#weisen" class="sp"><rect x="${cx + Math.sqrt(rw * rw - 250 * 250) - 30}" y="${cy + 238}" width="230" height="56" rx="28" fill="var(--flaeche)" stroke="var(--leise)" stroke-width="2" stroke-dasharray="6 5"/><text x="${cx + Math.sqrt(rw * rw - 250 * 250) + 85}" y="${cy + 262}" text-anchor="middle" font-family="var(--grotesk)" font-weight="700" font-size="18" fill="var(--text)">8 Arbeitsweisen</text><text x="${cx + Math.sqrt(rw * rw - 250 * 250) + 85}" y="${cy + 282}" text-anchor="middle" font-family="var(--grotesk)" font-size="14" fill="var(--leise)">gelten überall</text></a></svg></div>`;
}

// Ebene 1: die Sonne – die 14 Rechenregeln in vier Schichten (Nummer, Name, Klassenband)
function sichtSonne() {
  const schichten = [1, 2, 3, 4].map((nr) => `<li class="schicht s${nr}"><div class="schicht-kopf" id="schicht-${nr}">${ringBild(nr)}<span class="sk-nr">Schicht ${nr}</span><b>${ETAGE[nr]}</b></div><ul class="zeilen">${INHALT.regeln.filter((r) => r.etage === nr).map((r) => `<li><a class="zeile mit-satz" href="${adr.regel(r.id)}"><span class="z-nr">${r.nr}</span><span class="z-text"><span class="z-name">${esc(r.name)}</span><span class="z-merk">${satzZeile(r.satz)}</span></span>${band(r.id)}</a></li>`).join('')}</ul></li>`).join('');
  return `<div class="breite schmal start">${pfad()}<header class="e-kopf"><span class="s0-mini" aria-hidden="true"></span><div><p class="ueber">Die Sonne</p><h1>14 Rechenregeln</h1></div></header>
    <p class="lead">In vier Schichten, von den Grundlagen nach außen. Die Schichten ordnen, sie sperren nichts.</p>${sonnenSchnitt()}
    ${LEGENDE}<ol class="schichten">${schichten}</ol>
    <a class="verweis weiter" href="#klassen">Dieselben Regeln durch die Klassen ›</a></div>`;
}

// Ebene 1: ein Gebiet als eigene kleine Welt – seine tragenden Ideen mit je einem Satz
function sichtGebiet(name) {
  const p = PLANETEN.find((x) => x.name === name), n = PLANETEN.indexOf(p), vor = PLANETEN[n - 1], nach = PLANETEN[n + 1];
  return `<div class="breite schmal start">${pfad()}<header class="e-kopf">${planetScheibe(p.name, 48)}<div><p class="ueber">Gebiet ${n + 1} von 7</p><h1>${esc(p.name)}</h1></div></header>
    <p class="lead">${p.ideen.length} tragende Ideen. Hinter ihnen stehen ${zahlGesetze(p)} einzelne Regeln und Formeln.</p>${LEGENDE}
    <ol class="ideen1">${p.ideen.map((i) => `<li><a class="idee1" href="${adr.idee(i.id)}"><span class="z-nr">${i.nr}</span><span class="i1-text"><span class="i1-name">${esc(i.kurz)}</span><span class="i1-satz">${i.satz}</span></span>${band(i.id)}</a></li>`).join('')}</ol>
    ${blaettern(vor && { href: adrGebiet(vor.name), ueber: 'Gebiet ' + n, name: vor.name }, nach && { href: adrGebiet(nach.name), ueber: 'Gebiet ' + (n + 2), name: nach.name })}</div>`;
}

// Ebene 1: die acht Arbeitsweisen
function sichtWeisen() {
  return `<div class="breite schmal start">${pfad()}<header class="e-kopf"><span class="w-zeichen gross" aria-hidden="true"></span><div><p class="ueber">Arbeitsweisen</p><h1>8 Arbeitsweisen</h1></div></header>
    <p class="lead">Keine Rechenregeln, sondern wie man vorgeht. Sie gelten in jedem Gebiet.</p>
    <ol class="ideen1">${INHALT.arbeitsweisen.map((a, n) => `<li><a class="idee1" href="${adr.weise(n + 1)}"><span class="z-nr">${n + 1}</span><span class="i1-text"><span class="i1-name">${esc(a.name)}</span><span class="i1-satz">${a.satz}</span></span></a></li>`).join('')}</ol></div>`;
}

// ---------- C) Übersicht „Durch die Klassen“ ----------
let KLASSE = 5;
const beispielIn = (id, k) => LEITER[id].stufen.find((s) => s.klasse === k);
const rechnungIn = (s) => (s && s.text ? `<span class="rechnung">${mkText(s.text, s.pos, 0, s.text.length)}</span>` : '');
function sichtKlassen() {
  const wahl = `<div class="klassenwahl" role="group" aria-label="Klasse wählen"><span class="kw-text">Klasse</span>${KL.map((k) => `<a href="#klassen-${k}"${k === KLASSE ? ' aria-current="true"' : ''}>${k}</a>`).join('')}</div>`;
  const liste = [1, 2, 3, 4].map((nr) => `<li class="schicht s${nr}"><div class="schicht-kopf"><span class="sk-nr">Schicht ${nr}</span><b>${ETAGE[nr]}</b></div><ul class="kzeilen">${INHALT.regeln.filter((r) => r.etage === nr).map((r) => { const s = beispielIn(r.id, KLASSE);
    return `<li><a class="kzeile${s && s.text ? '' : ' leer'}" href="${adr.regel(r.id)}"><span class="z-nr">${r.nr}</span><span class="kz-name">${esc(r.name)}</span>${s && s.text ? `${rechnungIn(s)}<span class="kz-art">${s.art}</span>` : `<span class="kz-leer">kommt in Klasse ${KLASSE} nicht vor</span>`}</a></li>`; }).join('')}</ul></li>`).join('');
  const ideen = PLANETEN.map((p) => { const da = p.ideen.filter((i) => (beispielIn(i.id, KLASSE) || {}).text); return da.length ? `<li><p class="ki-gebiet">${planetScheibe(p.name, 22)}${esc(p.name)}</p><ul class="kzeilen">${da.map((i) => `<li><a class="kzeile" href="${adr.idee(i.id)}"><span class="z-nr">${i.nr}</span><span class="kz-name">${esc(i.kurz)}</span>${rechnungIn(beispielIn(i.id, KLASSE))}</a></li>`).join('')}</ul></li>` : ''; }).join('');
  const tafel = `<div class="tafel-wrap"><table class="tafel"><thead><tr><th class="r" scope="col">Rechenregel</th>${KL.map((k) => `<th scope="col">Klasse ${k}</th>`).join('')}</tr></thead><tbody>${[1, 2, 3, 4].map((nr) => `<tr class="t-schicht s${nr}"><th colspan="7">Schicht ${nr} · ${ETAGE[nr]}</th></tr>${INHALT.regeln.filter((r) => r.etage === nr).map((r) => `<tr><th class="r" scope="row"><a href="${adr.regel(r.id)}"><span class="z-nr">${r.nr}</span> ${esc(r.name)}</a></th>${KL.map((k) => { const ss = LEITER[r.id].stufen.filter((x) => x.klasse === k && x.text); return ss.length ? `<td>${ss.map(rechnungIn).join('<br>')}</td>` : '<td class="nicht">–</td>'; }).join('')}</tr>`).join('')}`).join('')}</tbody></table></div>`;
  return `<div class="breite schmal start klassen-ansicht">${pfad('<span>Durch die Klassen</span>')}<h1 class="titel">Durch die Klassen</h1><p class="lead">Dieselben 14 Rechenregeln in Klasse 5 bis 10.</p>${umschalter('klassen')}
    <div class="handy-teil"><p class="erkl">Wähle eine Klasse. Zu jeder Regel steht ihr Beispiel aus dieser Klasse; gelb umrahmt ist die Stelle, an der die Regel wirkt.</p>${wahl}
      <ol class="schichten">${liste}</ol>
      <details class="gebiet ideen-klasse"><summary><span class="g-name">Tragende Ideen in Klasse ${KLASSE}</span><span class="st-hinweis">${IDEEN.filter((i) => (beispielIn(i.id, KLASSE) || {}).text).length}</span>${CHEVRON}</summary><ul class="ki-liste">${ideen}</ul></details>
      <p class="hinweis-klein">Eine Regel durch alle Klassen: Regel antippen, dann „Dieselbe Regel in Klasse …“.</p></div>
    <div class="rechner-teil"><p class="erkl">Jede Zeile eine Rechenregel, jede Spalte eine Klasse. Gelb umrahmt: die Stelle, an der die Regel wirkt – in jeder Klasse dieselbe.</p>${tafel}</div></div>`;
}

// ---------- B) Regelseite (gestuft) ----------
function aufbauInhalt(rid) {
  const weg = erklaertUeber(rid), hilft = hilftBei(rid), traegt = regelTraegt(rid);
  let s = '';
  if (weg.length) s += `<h3 class="ueber">Lässt sich erklären über</h3><div class="verweise">${weg.map(verweisRegel).join('')}</div>`;
  if (hilft.length) s += `<h3 class="ueber">Hilft beim Erklären von</h3><div class="verweise">${hilft.map(verweisRegel).join('')}</div>`;
  if (weg.length || hilft.length) s += '<p class="klein leise">Zum Erklären hilfreich – keine Lernvoraussetzung und keine Sperre.</p>';
  if (traegt.length) s += `<h3 class="ueber">Darauf bauen auf: ${traegt.reduce((a, x) => a + x.n, 0)} Regeln in ${new Set(traegt.map((x) => x.i.planet)).size} Gebieten</h3><div class="verweise">${traegt.map((x) => `<a class="verweis" href="${adr.idee(x.i.id)}"><span class="nr">${esc(x.i.planet)}</span>${esc(x.i.kurz)} <span class="leise">(${x.n})</span></a>`).join('')}</div>`;
  return s || '<p class="leise">Keine Verweise hinterlegt.</p>';
}
const aufbauZahl = (rid) => erklaertUeber(rid).length + hilftBei(rid).length + regelTraegt(rid).length;
function genauInhalt(x, id) {
  const rest = felderVon(id).slice(1);
  return `${x.genau ? `<h3 class="ueber">Genau gesagt</h3><p class="fliess">${x.genau}</p>` : ''}${x.warum ? `<h3 class="ueber">Warum das gilt</h3><p class="fliess">${x.warum}</p>` : ''}${x.voraus ? `<h3 class="ueber">Wann sie gilt – und wann nicht</h3><p class="fliess">${x.voraus}</p>` : ''}
    ${rest.length ? `<h3 class="ueber">Weitere Bilder (${rest.length})</h3>${felderHtml(rest)}` : ''}${x.verwandt ? `<h3 class="ueber">Verwandt</h3><p class="fliess">${x.verwandt}</p>` : ''}`;
}
function vergleichInhalt(id) {
  return `<p class="band-zeile">${band(id, { gross: 1 })}</p>${LEGENDE}<p class="markiert"><b>Gelb umrahmt, in jeder Klasse an derselben Stelle:</b> ${esc(LEITER[id].markiert)}</p>${klassenLeiter(id)}`;
}
function sichtRegel(id, lehrer) {
  const r = REGEL[id], n = r.nr, vor = REGEL['R' + (n - 1)], nach = REGEL['R' + (n + 1)];
  const kopf = `<header class="r-kopf"><p class="ueber mit-ring">${ringBild(r.etage, 26)}Rechenregel ${n} von 14 · Schicht ${r.etage}</p><h1>${esc(r.name)}</h1><p class="kurz">${esc(KURZ[id] || '')}</p></header>`;
  if (lehrer) return sichtLehrer(id, kopf);
  return `<article class="breite schmal regelseite">${pfad('<a href="#sonne">Sonne</a>', `<span>Schicht ${r.etage}</span>`)}${kopf}${merksatz(r.satz)}
    <section class="bsp"><p class="ueber">Beispiel</p>${beispiel(id)}</section>
    <div class="stufen">${stufe('klassen', `Dieselbe Regel in ${spanneText(id)}`, band(id), vergleichInhalt(id), VERGLEICH_OFFEN)}
    ${stufe('genau', 'Genau erklärt', 'warum · wann', genauInhalt(r, id))}
    ${stufe('fehler', 'Typische Fehler', anzahlFehler(r.fehler) + '', fehlerListe(r.fehler))}
    ${stufe('aufbau', 'Worauf sie aufbaut, was auf ihr aufbaut', aufbauZahl(id) + '', aufbauInhalt(id))}</div>
    ${blaettern(vor && { href: adr.regel(vor.id), ueber: 'Regel ' + vor.nr, name: vor.name }, nach && { href: adr.regel(nach.id), ueber: 'Regel ' + nach.nr, name: nach.name })}</article>`;
}

// ---------- Seite einer tragenden Idee (dasselbe Stufen-Prinzip) ----------
function sichtIdee(id) {
  const i = IDEE[id], k = IDEEN.indexOf(i), vor = IDEEN[k - 1], nach = IDEEN[k + 1], braucht = ideeBraucht(i);
  const folge = `<ol class="folge">${i.gesetze.map((gid) => { const g = GESETZ[gid]; return `<li><a class="karte" href="${adr.gesetz(gid)}"><span class="f-name"><span class="nr">${gid}</span> ${esc(g.name)}</span><span class="f-satz">${g.satz}</span></a></li>`; }).join('')}</ol>`;
  return `<article class="breite schmal regelseite">${pfad(`<a href="${adrGebiet(i.planet)}">${esc(i.planet)}</a>`)}
    <header class="r-kopf"><p class="ueber">${esc(i.planet)} · tragende Idee ${i.nr} von ${i.von}</p><h1>${esc(i.kurz)}</h1><p class="kurz">${esc(KURZ[id] || '')}</p></header>${merksatz(i.satz)}
    <section class="bsp"><p class="ueber">Beispiel</p>${beispiel(id)}</section>
    <div class="stufen">${stufe('klassen', LEITER[id].klassen.length > 1 ? `Dieselbe Idee in ${spanneText(id)}` : `Kommt nur in Klasse ${LEITER[id].klassen[0]} vor`, band(id), vergleichInhalt(id), VERGLEICH_OFFEN)}
    ${stufe('genau', 'Genau erklärt', 'warum', genauInhalt(i, id))}
    ${stufe('folge', 'Die Regeln und Formeln dahinter', i.gesetze.length + '', folge)}
    ${stufe('aufbau', 'Worauf sie aufbaut', braucht.length + '', braucht.length ? `<h3 class="ueber">Benutzt diese Rechenregeln</h3><div class="verweise">${braucht.map(verweisRegel).join('')}</div>` : '<p class="leise">Keine Rechenregel hinterlegt.</p>')}</div>
    ${blaettern(vor && { href: adr.idee(vor.id), ueber: vor.planet === i.planet ? 'Idee ' + vor.nr : esc(vor.planet), name: vor.kurz }, nach && { href: adr.idee(nach.id), ueber: nach.planet === i.planet ? 'Idee ' + nach.nr : esc(nach.planet), name: nach.kurz })}</article>`;
}

// ---------- Seite einer Arbeitsweise (kürzer: es liegen nur Name und Satz vor) ----------
function sichtWeise(n) {
  const a = INHALT.arbeitsweisen[n - 1], vor = INHALT.arbeitsweisen[n - 2], nach = INHALT.arbeitsweisen[n];
  return `<article class="breite schmal regelseite">${pfad('<a href="#weisen">Arbeitsweisen</a>')}
    <header class="r-kopf"><p class="ueber">Arbeitsweise ${n} von 8 · gilt in jedem Gebiet</p><h1>${esc(a.name)}</h1></header>${merksatz(a.satz)}
    <div class="z-folgt"><p class="ueber">Noch offen</p><p>Kurzbeschreibung, Beispiel und Erklärung liefert der Mathe-Profi. Bisher liegen nur Name und Satz vor.</p></div>
    ${blaettern(vor && { href: adr.weise(n - 1), ueber: 'Arbeitsweise ' + (n - 1), name: vor.name }, nach && { href: adr.weise(n + 1), ueber: 'Arbeitsweise ' + (n + 1), name: nach.name })}</article>`;
}

// ---------- Einzelne Regel eines Gebiets (über Idee oder Suche) ----------
function sichtGesetz(id) {
  const g = GESETZ[id], i = ideeVon(id), br = brauchtRegeln(g), k = g.klassen || [];
  return `<article class="breite schmal regelseite">${pfad(`<a href="${adrGebiet(g.planet)}">${esc(g.planet)}</a>`, i ? `<a href="${adr.idee(i.id)}">${esc(i.kurz)}</a>` : '')}
    <header class="r-kopf"><p class="ueber">Regel ${id} · ${klasseVon(g)}</p><h1>${esc(g.name)}</h1></header>${merksatz(g.satz)}
    ${k.length ? `<section class="bsp"><p class="ueber">Beispiel</p><p class="rechnung gross-r">${esc(k[0].text)}</p><p class="kl">Klasse ${k[0].klasse} · ${k[0].art}</p></section>` : ''}
    <div class="stufen">${k.length > 1 ? stufe('klassen', 'In den Klassen', k.length + '', beispielListe(k)) : ''}
    ${g.warum || g.voraus || g.genau ? stufe('genau', 'Genau erklärt', 'warum · wann', genauInhalt(g, '')) : ''}
    ${g.fehler ? stufe('fehler', 'Typische Fehler', anzahlFehler(g.fehler) + '', fehlerListe(g.fehler)) : ''}
    ${stufe('aufbau', 'Worauf sie aufbaut', (br.length + (i ? 1 : 0)) + '', `${i ? `<h3 class="ueber">Folgt aus der tragenden Idee</h3><div class="verweise"><a class="verweis" href="${adr.idee(i.id)}"><span class="nr">${esc(i.planet)}</span>${esc(i.kurz)}</a></div>` : ''}${br.length ? `<h3 class="ueber">Benutzt diese Rechenregeln</h3><div class="verweise">${br.map(verweisRegel).join('')}</div>` : ''}`)}</div>
    ${k.length || g.warum ? '' : '<div class="z-folgt"><p>Für diese Regel liegen bisher Name, Satz und Klasse vor.</p></div>'}</article>`;
}

// ---------- E) Lehrer-Blatt: alle Stufen offen, Verweise, Rückmeldung ----------
const rueck = (id, abschnitt) => `<button class="rueck" type="button" data-bezug="${LEHRER[id].kennung} · ${abschnitt}">Rückmeldung geben</button>`;
function sichtLehrer(id, kopf) {
  const r = REGEL[id], L = LEHRER[id], kl = L.klassen || {}, nach = (a) => (a && a.length ? a.join(', ') : '–');
  const lp = `<table class="lp"><thead><tr><th scope="col">Schulart</th><th scope="col">Klassen</th></tr></thead><tbody><tr><td>Gymnasium Bayern</td><td>${nach(kl.gym_by)}</td></tr><tr><td>Realschule Bayern</td><td>${nach(kl.rs_by)}</td></tr><tr><td>IB MYP (Jahr)</td><td>${nach(kl.ib_myp)}</td></tr></tbody></table>
    <p class="klein leise">Grundlage: ${esc(L.grundlage)}. Gymnasium: alle Beispiele gegen die Lehrplan-Kopie der App geprüft (Mathe-Profi, lehrplan-pruefung.md). <b>Nicht geprüft:</b> LehrplanPLUS an der Quelle; Realschule und IB nur bis zum Thema.</p>`;
  const themen = `<ul class="lverweise">${L.themen.map((t) => `<li><span>${esc(thema(t))}</span><a class="verweis klein-v" href="#lehrer-${id.toLowerCase()}" data-ohne="1">Lehrer-Seite ›</a></li>`).join('')}</ul>`;
  const aufg = L.aufgaben.length ? `<ol class="aufgaben">${L.aufgaben.map((a) => `<li><p class="a-kopf">${a.kennung} · Klasse ${a.klasse} · Lernkarte „${esc(a.lernkarte)}“</p><p>${esc(a.text)}</p>${a.auswahl ? `<p class="leise">Auswahl: ${a.auswahl.map(esc).join(' · ')}</p>` : ''}<p><b>Lösung:</b> ${esc(a.loesung)}</p><p class="leise">${esc(a.weg)}</p></li>`).join('')}</ol>` : '<p class="leise">Noch keine Aufgabe dieser Regel zugeordnet.</p>';
  const fb = L.fehlbilder.length ? `<ul class="fehlerliste">${L.fehlbilder.map((f) => `<li>${esc(f.beschreibung)} <span class="kl">${f.kennung}</span></li>`).join('')}</ul>` : '<p class="leise">Keine Fehlbilder hinterlegt.</p>';
  const ab = (t, inhalt, knopf) => `<section class="l-abschnitt"><div class="l-kopf"><h2>${t}</h2>${knopf || ''}</div>${inhalt}</section>`;
  return `<article class="breite schmal regelseite lehrer"><div class="lehrer-band"><span>Eltern und Lehrer</span><a class="verweis" href="${adr.regel(id)}">So sieht es das Kind ›</a></div>
    <nav class="pfad" aria-label="Brotkrumen"><a href="#sonne">‹ Regeln</a><span class="t">›</span><span>Schicht ${r.etage} · ${ETAGE[r.etage]}</span></nav>${kopf}
    ${ab('1 Merksatz', merksatz(r.satz) + '<p class="klein leise">Wörtlich wie auf der Seite des Kindes.</p>', rueck(id, 'Merksatz'))}
    ${ab('2 Was das Kind sieht', `<p class="ueber">Beispiel</p>${beispiel(id)}<p class="ueber" style="margin-top:18px">Dieselbe Regel in ${spanneText(id)}</p>${vergleichInhalt(id)}<p class="ueber" style="margin-top:18px">Typische Fehler</p>${fehlerListe(r.fehler)}`, rueck(id, 'Karte des Kindes'))}
    ${ab('3 Fachliche Erklärung', genauInhalt(r, id), rueck(id, 'Erklärung'))}
    ${ab('4 Verweise und Zuordnung', `<h3 class="ueber">Lehrplan</h3>${lp}<h3 class="ueber">In der App: Themen, die diese Regel üben</h3>${themen}<h3 class="ueber">Beispielaufgaben mit Lösung (Kennung ${L.kennung})</h3>${aufg}<h3 class="ueber">Fehlbilder, die die App dieser Regel zuordnet</h3>${fb}<h3 class="ueber">Aufbau</h3>${aufbauInhalt(id)}`, rueck(id, 'Zuordnung'))}
    ${ab('5 Stand je Kind', '<p class="leise">Stand folgt (kommt mit Stufe 2, sobald der Server ihn liefert).</p>')}</article>`;
}

// ---------- Suche (übernommen aus Runde 6, Ziele angepasst) ----------
const wort = (s) => s.toLowerCase().replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss').replace(/<[^>]+>/g, ' ');
const woerter = (s, ab) => wort(s).split(/[^a-z0-9]+/).filter((w) => w.length > ab);
const STICH = {}; INHALT.stichwoerter.forEach((s) => { (STICH[s.ziel] ||= []).push(s.wort); });
const SUCHBAR = [
  ...INHALT.regeln.map((r) => ({ id: r.id, art: 'Rechenregel ' + r.nr, name: r.name, satz: r.satz, mehr: LEITER[r.id].stufen.map((k) => k.text || '').join(' ') + ' ' + r.fehler, ort: 'Sonne · Rechenregeln', ziel: adr.regel(r.id) })),
  ...INHALT.gesetze.map((g) => { const i = ideeVon(g.id); return { id: g.id, art: 'Regel ' + g.id, name: g.name, satz: g.satz, mehr: (g.klassen || []).map((k) => k.text).join(' ') + ' ' + (g.fehler || ''), ort: g.planet + (i ? ' › ' + i.kurz : ''), ziel: adr.gesetz(g.id) }; }),
  ...IDEEN.map((i) => ({ id: i.id, art: 'Tragende Idee', name: i.kurz, satz: i.satz, mehr: '', ort: i.planet, ziel: adr.idee(i.id) })),
  ...INHALT.formeln.map((f) => ({ id: 'formel ' + f.fuer, art: 'Formel', name: f.fuer, satz: f.formel, mehr: '', ort: GESETZ[f.ziel].planet + ' › ' + f.ziel, ziel: adr.gesetz(f.ziel) })),
  ...INHALT.arbeitsweisen.map((a, n) => ({ id: a.name, art: 'Arbeitsweise', name: a.name, satz: a.satz, mehr: '', ort: 'Arbeitsweisen', ziel: adr.weise(n + 1) })),
].map((e) => ({ ...e, stich: STICH[e.id] || [], wn: woerter(e.name, 2), wk: (STICH[e.id] || []).map((s) => woerter(s, 2)), ws: woerter(e.satz, 3), wm: woerter(e.mehr, 3) }));
function suche(q) {
  const teile = woerter(q, 1); if (!teile.length) return [];
  const trifft = (liste, t) => liste.some((w) => w === t || (t.length >= 4 && w.includes(t)) || (w.length >= 5 && t.includes(w)));
  return SUCHBAR.map((e) => { let p = 0, ueber = null; for (const t of teile) { const k = e.wk.findIndex((l) => trifft(l, t)); if (k >= 0) { p += e.wk[k].includes(t) ? 9 : 5; ueber = e.stich[k]; }
    p += (trifft(e.wn, t) ? 6 : 0) + (trifft(e.ws, t) ? 3 : 0) + (trifft(e.wm, t) ? 1 : 0); } return { ...e, p, ueber }; })
    .filter((x) => x.p > 0).sort((a, b) => b.p - a.p || (a.art === 'Formel') - (b.art === 'Formel')).slice(0, 14);
}
let FRAGE = '';
function sichtSuche() {
  const tr = suche(FRAGE);
  return `<div class="breite schmal">${pfad('<span>Suche</span>')}<h1 class="s-titel">${!FRAGE ? 'Suche' : tr.length ? `${tr.length} Treffer für „${esc(FRAGE)}“` : `Nichts gefunden für „${esc(FRAGE)}“`}</h1>
    ${tr.length ? '' : '<p class="leise" style="margin-top:8px">Versuch ein einzelnes Wort, zum Beispiel „Kegel“, „Prozent“ oder „Klammer“.</p>'}
    <ol class="treffer">${tr.map((e) => `<li><a class="karte" href="${e.ziel}"><span class="t-ort">${esc(e.ort)}</span><span class="t-name"><span class="nr">${e.art}</span> ${esc(e.name)}</span>${e.ueber ? `<span class="t-stich">Stichwort „${esc(e.ueber)}“ steht hier</span>` : ''}<span class="t-satz">${e.satz}</span></a></li>`).join('')}</ol></div>`;
}

// ---------- Kopf ----------
const LUPE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21"/></svg>';
document.getElementById('kopf').innerHTML = `<div class="breite schmal-k"><a class="kopf-marke" href="#universum"><i></i><span>Regel-Universum</span></a>
  <form class="suche" role="search"><label><span class="unsichtbar">Im Regel-Universum suchen</span>${LUPE}<input type="search" name="q" placeholder="Suchen" autocomplete="off" enterkeyhint="search"></label></form></div>`;
const suchfeld = document.querySelector('.suche input');
const suchen = () => { FRAGE = suchfeld.value.trim(); if (location.hash !== '#suche') location.hash = '#suche'; else zeige(); };
document.querySelector('.suche').addEventListener('submit', (e) => { e.preventDefault(); suchen(); suchfeld.blur(); });
suchfeld.addEventListener('input', () => { if (suchfeld.value.trim().length >= 3) suchen(); });

// ---------- Weiche ----------
const seite = document.getElementById('seite');
let ZULETZT = '', ZULETZT_EBENE = 0;
// Ebene einer Adresse: 0 Universum · 1 Sonne, Gebiet, Arbeitsweisen, Klassen, Suche · 2 Regel, Idee, Arbeitsweise, Lehrer · 3 einzelne Regel
const ebeneVon = (h) => (h === 'universum' || h === 'aufbau' || !h ? 0 : /^(sonne|weisen|gebiet-|klassen|suche)/.test(h) ? 1 : h.startsWith('regel-') ? 3 : 2);
function zeige() {
  const h = decodeURIComponent(location.hash.replace(/^#/, '')).toLowerCase() || 'universum';
  let m, html;
  if ((m = h.match(/^r(\d+)$/)) && REGEL['R' + m[1]]) html = sichtRegel('R' + m[1]);
  else if ((m = h.match(/^lehrer-r(\d+)$/)) && REGEL['R' + m[1]]) html = sichtRegel('R' + m[1], true);
  else if ((m = h.match(/^idee-([a-z]+-\d+)$/)) && IDEE['I-' + m[1]]) html = sichtIdee('I-' + m[1]);
  else if ((m = h.match(/^weise-(\d)$/)) && INHALT.arbeitsweisen[m[1] - 1]) html = sichtWeise(+m[1]);
  else if ((m = h.match(/^regel-([a-z]+\d+)$/)) && GESETZ[m[1].toUpperCase()]) html = sichtGesetz(m[1].toUpperCase());
  else if (h === 'suche') html = sichtSuche();
  else if (h === 'sonne') html = sichtSonne();
  else if (h === 'weisen') html = sichtWeisen();
  else if ((m = h.match(/^gebiet-([a-z]+)$/)) && KUERZEL_ZU[m[1]]) html = sichtGebiet(KUERZEL_ZU[m[1]]);
  else if ((m = h.match(/^klassen(?:-(\d+))?$/))) { if (m[1] && KL.includes(+m[1])) KLASSE = +m[1]; html = sichtKlassen(); }
  else html = sichtUniversum();
  seite.innerHTML = html;
  const e = ebeneVon(h); document.body.classList.toggle('weltraum', e <= 1);
  if (ZULETZT && e !== ZULETZT_EBENE && !matchMedia('(prefers-reduced-motion: reduce)').matches && seite.animate)
    seite.animate([{ opacity: 0, transform: `scale(${e > ZULETZT_EBENE ? 0.965 : 1.035})` }, { opacity: 1, transform: 'none' }], { duration: 220, easing: 'cubic-bezier(.2,.7,.2,1)' });
  ZULETZT_EBENE = e;
  if (h !== 'suche') { if (document.activeElement !== suchfeld) suchfeld.value = ''; }
  // Beim Wechsel der Klasse bleibt die Seite stehen, sonst nach oben
  if (!(h.startsWith('klassen') && ZULETZT.startsWith('klassen')) && h !== 'suche') scrollTo(0, 0);
  ZULETZT = h;
}
addEventListener('hashchange', zeige);
const zurSchicht = (t) => { const g = t.closest && t.closest('.sc-ziel'); if (g) document.getElementById('schicht-' + g.dataset.schicht).scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' }); return !!g; };
seite.addEventListener('keydown', (e) => { if ((e.key === 'Enter' || e.key === ' ') && zurSchicht(e.target)) e.preventDefault(); });
seite.addEventListener('click', (e) => {
  if (zurSchicht(e.target)) return;
  const b = e.target.closest('.rueck'); if (b) { const alt = b.parentElement.querySelector('.rueck-info'); if (alt) alt.remove(); else b.insertAdjacentHTML('afterend', `<p class="rueck-info">Im Entwurf ohne Funktion. In der App öffnet sich hier die Rückmeldung (Fehler, Vorschlag, Frage) mit dem Bezug „${esc(b.dataset.bezug)}“.</p>`); }
  const o = e.target.closest('[data-ohne]'); if (o) { e.preventDefault(); o.textContent = 'Verweis im Entwurf ohne Ziel'; }
});

// ---------- Entwurfs-Schalter (gehört nicht zur App) ----------
const ew = document.createElement('div'); ew.className = 'entwurf';
ew.innerHTML = `<button type="button" aria-expanded="false">Entwurf ⚙</button><div class="entwurf-feld"><b>Entwurf, nicht die App.</b><a href="#universum">Ebene 0: Universum</a><a href="#sonne">Ebene 1: Sonne (14 Regeln)</a><a href="#gebiet-fur">Ebene 1: Gebiet</a><a href="#weisen">Ebene 1: Arbeitsweisen</a><a href="#klassen">Durch die Klassen</a><a href="#r6">Ebene 2: Regel 6</a><a href="#idee-fur-2">Ebene 2: Idee</a><a href="#regel-f7">Ebene 3: Regel F7</a><a href="#lehrer-r6">Lehrer-Blatt (Regel 6)</a><button type="button" class="thema">hell / dunkel</button></div>`;
ew.querySelector('button').addEventListener('click', () => { ew.classList.toggle('offen'); ew.querySelector('button').setAttribute('aria-expanded', ew.classList.contains('offen')); });
ew.querySelector('.thema').addEventListener('click', () => setzeThema(THEMA === 'hell' ? 'nacht' : 'hell'));
ew.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => ew.classList.remove('offen')));
document.body.append(ew);
document.body.insertAdjacentHTML('afterbegin', '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><radialGradient id="glanz" cx=".34" cy=".3" r=".8"><stop offset="0" stop-color="#fff" stop-opacity=".5"/><stop offset=".55" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".22"/></radialGradient></defs></svg>');
zeige();
