// Gesetzbuch – gemeinsame Teile: Daten, Kopf mit Suche, „ein Gesetz aufgeschlagen“, „Idee und ihre Gesetze“, Suche.
const P = new URLSearchParams(location.search);
document.body.dataset.g = P.get('g') === 'hell' ? 'hell' : 'nacht';
if (P.get('bild') === '1') document.body.classList.add('bild');
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const REGEL = Object.fromEntries(INHALT.regeln.map((r) => [r.id, r]));
const GESETZ = Object.fromEntries(INHALT.gesetze.map((g) => [g.id, g]));
const ETAGE = Object.fromEntries(INHALT.etagen.map((e) => [e.nr, e.name]));
const PLANETEN = INHALT.planeten.filter((p) => PLANET_BILD[p.name]);
const IDEE = {}; for (const p of PLANETEN) p.ideen.forEach((i) => { i.id = `I-${KUERZEL[p.name]}-${i.nr}`; i.planet = p.name; i.von = p.ideen.length; IDEE[i.id] = i; });
const ideeVon = (gid) => Object.values(IDEE).find((i) => i.gesetze.includes(gid));
const spanne = (zahlen) => { const a = Math.min(...zahlen), b = Math.max(...zahlen); return a === b ? 'Klasse ' + a : `Klasse ${a}–${b}`; };
const regelSpanne = (r) => spanne(r.klassen.map((k) => k.klasse));
const gymZahlen = (g) => (g.gym.match(/\d+/g) || []).map(Number);
const planetSpanne = (name) => { const z = INHALT.gesetze.filter((g) => g.planet === name).flatMap(gymZahlen); return z.length ? spanne(z) : ''; };
const klasseVon = (g) => (g.gym && g.gym !== '–' ? 'Klasse ' + g.gym : 'Realschule oder IB');
const thema = (k) => (INHALT.themen[k] ? `${INHALT.themen[k].ort} · ${INHALT.themen[k].titel}` : '');
const planetScheibe = (name, gr = 44) => `<svg class="scheibe" width="${gr}" height="${gr}" viewBox="-22 -22 44 44" aria-hidden="true"><circle r="21" fill="${PLANET_BILD[name].farbe}"/>${PLANET_BILD[name].zeichen}</svg>`;
const LUPE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.500 15.500L21 21"/></svg>';
const seite = document.getElementById('seite');
// Zwei Zeilen je Satz (Auftrag 12 an den Mathe-Profi): Merksatz groß, „Genau gesagt“ klein darunter. Solange „genau“ fehlt, steht nur der Satz.
const genau = (x) => (x.genau ? `<span class="genau"><i>Genau gesagt:</i> ${x.genau}</span>` : '');
// Klassenleiter: die Beispiele einer Regel untereinander, die wirkende Stelle gelb umrahmt und senkrecht übereinander.
// Auszeichnung in teile/wirkstelle.json: [[…]] = wirkende Stelle, [[!…]] = diese Stelle richtet die Zeile aus (sonst die erste),
// || = davor steht ein Vorsatz, der in einer eigenen Zeile über der Rechnung läuft.
const mk = (s) => esc(s).replace(/\[\[!?(.*?)\]\]/g, '<b class="w">$1</b>');
function zeileTeile(id, text) { const m = WIRKSTELLE[id]?.bsp[text]; if (!m) return null; const [vorsatz, rest] = m.includes('||') ? m.split('||') : ['', m];
  const a = rest.includes('[[!') ? rest.indexOf('[[!') : rest.indexOf('[['), e = rest.indexOf(']]', a); return { vorsatz: mk(vorsatz), vor: mk(rest.slice(0, a)), marke: esc(rest.slice(a, e).replace(/^\[\[!?/, '')), nach: mk(rest.slice(e + 2)), lang: rest.slice(0, a).replace(/\[\[!?|\]\]/g, '').length }; }
function klassenLeiter(id, klassen, o = {}) {
  const r = REGEL[id], zeilen = klassen.map((k) => ({ k, t: zeileTeile(id, k.text) })), lang = Math.max(0, ...zeilen.map((z) => (z.t ? z.t.lang : 0))) + Math.max(0, ...zeilen.map((z) => (z.t ? z.t.marke.length : 0))) > 20;
  const luecken = r && !o.ohneLuecken ? [5, 6, 7, 8, 9, 10].filter((n) => !klassen.some((k) => k.klasse === n)).map((n) => ({ luecke: n })) : [];
  const alle = [...zeilen, ...luecken].sort((a, b) => (a.luecke || a.k.klasse) - (b.luecke || b.k.klasse));
  const breit = Math.max(0, ...zeilen.map((z) => (z.t ? z.t.marke.length : 0))) > 6;
  return `<ol class="leiter gl${lang ? ' lang' : ''}${breit ? ' breit' : ''}">${alle.map((z) => { if (z.luecke) return `<li class="luecke"><span class="stufe">${z.luecke}</span><p class="ganz">Noch kein Beispiel hinterlegt. Ob die Regel in Klasse ${z.luecke} vorkommt, klärt der Mathe-Profi.</p></li>`;
    const meta = o.ohneMeta ? '' : `<p class="kl ganz">${z.k.art}${z.k.thema && thema(z.k.thema) ? ' · ' + thema(z.k.thema) : ''}${r && !z.t ? ' · <i>wirkende Stelle steht nicht in dieser Zeile</i>' : ''}</p>`;
    return `<li><span class="stufe">${z.k.klasse}</span>${z.t ? `${z.t.vorsatz ? `<p class="rechnung vorsatz ganz">${z.t.vorsatz}</p>` : ''}<span class="rechnung vor">${z.t.vor}</span><b class="w rechnung mk">${z.t.marke}</b><span class="rechnung nach">${z.t.nach}</span>` : `<p class="rechnung ganz">${esc(z.k.text)}</p>`}${meta}</li>`; }).join('')}</ol>`;
}
const OHNE_GENAU = P.get('genau') === '0';

// ---------- Kopf ----------
document.getElementById('kopf').innerHTML = `<div class="breite"><a class="kopf-marke" href="#/"><i></i><span class="lang">Regel-Universum</span><span class="kurz">Regel-Universum</span></a>
  <form class="suche" role="search"><label><span style="position:absolute;left:-9999px">Im Regel-Universum suchen</span>${LUPE}<input type="search" name="q" placeholder="Regel suchen, z. B. Kegelmantel" autocomplete="off" enterkeyhint="search"></label></form></div>`;
const suchfeld = document.querySelector('.suche input');
document.querySelector('.suche').addEventListener('submit', (e) => { e.preventDefault(); if (suchfeld.value.trim()) location.hash = '#/suche/' + encodeURIComponent(suchfeld.value.trim()); });
suchfeld.addEventListener('input', () => { if (suchfeld.value.trim().length >= 3) history.replaceState(null, '', '#/suche/' + encodeURIComponent(suchfeld.value.trim())), zeige(); });

// ---------- Suche: Name, Satz, Beispiele – und die Stichwörter des Mathe-Profis (z. B. „Kegelmantel“ steht bei F17) ----------
const wort = (s) => s.toLowerCase().replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss').replace(/<[^>]+>/g, ' ');
const woerter = (s, ab) => wort(s).split(/[^a-z0-9]+/).filter((w) => w.length > ab);
const STICH = {}; INHALT.stichwoerter.forEach((s) => { (STICH[s.ziel] ||= []).push(s.wort); });
const SUCHBAR = [
  ...INHALT.regeln.map((r) => ({ id: r.id, art: 'Rechenregel ' + r.nr, name: r.name, satz: r.satz, mehr: r.klassen.map((k) => k.text).join(' ') + ' ' + r.fehler, ort: ['Sonne', ETAGE[r.etage]], kl: regelSpanne(r), ziel: '#/regel/' + r.id })),
  ...INHALT.gesetze.map((g) => { const i = ideeVon(g.id); return { id: g.id, art: 'Regel ' + g.id, name: g.name, satz: g.satz, mehr: (g.klassen || []).map((k) => k.text).join(' ') + ' ' + (g.fehler || '') + ' ' + (g.warum || ''), ort: [g.planet, i ? i.kurz : ''], kl: klasseVon(g), ziel: '#/gesetz/' + g.id }; }),
  ...Object.values(IDEE).map((i) => ({ id: i.id, art: 'Tragende Idee', name: i.kurz, satz: i.satz, mehr: '', ort: [i.planet], kl: `${i.gesetze.length} Regeln`, ziel: '#/idee/' + i.id })),
  ...INHALT.formeln.map((f) => ({ id: 'formel ' + f.fuer, art: 'Formel', name: f.fuer, satz: f.formel + (f.bedingung && f.bedingung !== '–' ? ' <span class="leise">(' + f.bedingung + ')</span>' : ''), mehr: '', ort: [GESETZ[f.ziel].planet, 'steht bei ' + f.ziel + ' ' + GESETZ[f.ziel].name], kl: klasseVon(GESETZ[f.ziel]), ziel: '#/gesetz/' + f.ziel })),
  ...INHALT.arbeitsweisen.map((a) => ({ id: a.name, art: 'Arbeitsweise', name: a.name, satz: a.satz, mehr: '', ort: ['Arbeitsweisen'], kl: 'jede Klasse', ziel: '#/' })),
].map((e) => ({ ...e, stich: STICH[e.id] || [], wn: woerter(e.name, 2), wk: (STICH[e.id] || []).map((s) => woerter(s, 2)), ws: woerter(e.satz, 3), wm: woerter(e.mehr, 3) }));
function suche(q) {
  const teile = woerter(q, 1); if (!teile.length) return [];
  const trifft = (liste, t) => liste.some((w) => w === t || (t.length >= 4 && w.includes(t)) || (w.length >= 5 && t.includes(w)));
  return SUCHBAR.map((e) => { let p = 0, ueber = null; for (const t of teile) { const k = e.wk.findIndex((l) => trifft(l, t)); if (k >= 0) { p += e.wk[k].includes(t) ? 9 : 5; ueber = e.stich[k]; }
    p += (trifft(e.wn, t) ? 6 : 0) + (trifft(e.ws, t) ? 3 : 0) + (trifft(e.wm, t) ? 1 : 0); } return { ...e, p, ueber }; })
    .filter((x) => x.p > 0).sort((a, b) => b.p - a.p || (a.art === 'Formel') - (b.art === 'Formel')).slice(0, 14);
}
function sichtSuche(q) {
  const tr = suche(q); if (suchfeld.value !== q && document.activeElement !== suchfeld) suchfeld.value = q;
  return `<div class="breite schmal"><nav class="pfad"><a href="#/">Übersicht</a><span class="t">›</span><span>Suche</span></nav>
    <h1 class="s-titel">${tr.length ? `${tr.length} Treffer für „${esc(q)}“` : `Nichts gefunden für „${esc(q)}“`}</h1>
    ${tr.length ? '' : '<p class="leise" style="margin-top:8px">Versuch ein einzelnes Wort, zum Beispiel „Kegel“, „Prozent“ oder „Klammer“.</p>'}
    <ol class="treffer">${tr.map((e) => `<li><a class="karte" href="${e.ziel}"><span class="t-ort">${e.ort.filter(Boolean).map(esc).join(' › ')}</span><span class="t-name"><span class="nr">${e.art}</span> ${esc(e.name)}</span>${e.ueber ? `<span class="t-stich">Stichwort „${esc(e.ueber)}“ steht hier</span>` : ''}<span class="t-satz">${e.satz}</span><span class="kl">${e.kl}</span></a></li>`).join('')}</ol></div>`;
}

// ---------- Ein Gesetz aufgeschlagen ----------
function verweise(text) { // „F15 Prisma und Zylinder, Rechenregel 12 Gegenrechnung“ oder der bloße Name einer Rechenregel -> Verweise
  const aus = [], s = text || ''; for (const m of s.matchAll(/\b([A-Z]\d+)\b/g)) if (GESETZ[m[1]]) aus.push(m[1]); for (const m of s.matchAll(/Rechenregel (\d+)/g)) aus.push('R' + m[1]);
  for (const r of INHALT.regeln) if (s.includes(r.name)) aus.push(r.id); return [...new Set(aus)].map((id) => ({ id, name: (GESETZ[id] || REGEL[id]).name }));
}
// Dieselbe Regel in vielen Klassen: sechs Kästchen 5 bis 10. E = eingeführt (voll), A = angewendet (halb), V = Vorwissen (gestrichelt).
const STUFE_WORT = { E: 'eingeführt', A: 'angewendet', V: 'Vorwissen' };
const klassenBand = (r) => `<span class="band6" role="img" aria-label="Klassen: ${[5, 6, 7, 8, 9, 10].filter((k) => r.stufen[k]).map((k) => `${k} ${STUFE_WORT[r.stufen[k]]}`).join(', ')}">${[5, 6, 7, 8, 9, 10].map((k) => `<i class="${r.stufen[k] || ''}">${k}</i>`).join('')}</span>`;
const BAND_LEGENDE = '<span class="band-legende"><span class="band6"><i class="E">5</i></span> eingeführt <span class="band6"><i class="A">7</i></span> angewendet <span class="band6"><i class="V">5</i></span> Vorwissen <span class="band6"><i>9</i></span> kein Beispiel hinterlegt</span>';
// Worauf es aufbaut: Jede Regel der Planeten nennt die Rechenregeln der Sonne, die sie braucht (Spalte „Sonne“ des Mathe-Profis).
const brauchtRegeln = (g) => (g.sonne.match(/\d+/g) || []).map((n) => 'R' + n).filter((id) => REGEL[id]);
const ideeBraucht = (i) => [...new Set(i.gesetze.flatMap((gid) => brauchtRegeln(GESETZ[gid])))].sort((a, b) => a.slice(1) - b.slice(1));
const regelTraegt = (rid) => Object.values(IDEE).map((i) => ({ i, n: i.gesetze.filter((gid) => brauchtRegeln(GESETZ[gid]).includes(rid)).length })).filter((x) => x.n);
const erklaerung = (k) => `../../uebung/entwurf/uebung.html?s=erkl&g=${document.body.dataset.g}&thema=${encodeURIComponent(k)}`;
const verweisKnopf = (v) => `<a class="verweis" href="#/${v.id[0] === 'R' && REGEL[v.id] ? 'regel' : 'gesetz'}/${v.id}"><span class="nr">${REGEL[v.id] ? 'Regel ' + v.id.slice(1) : v.id}</span>${esc(v.name)}</a>`;
const vorgabe = (z, titel) => `<div class="z-folgt"><p class="ueber">${titel}</p>${z ? `<p><b>Zu sehen sein wird:</b> ${esc(z['Zu sehen'])}</p><p class="klein leise" style="margin-top:6px">Vorgabe des Mathe-Profis. Gezeichnet wird, sobald der Zeichenstil freigegeben ist.</p>` : '<p>Für diesen Planeten liegt noch keine Zeichen-Vorgabe des Mathe-Profis vor.</p>'}</div>`;
function sichtGesetz(id) {
  const r = REGEL[id], g = r || GESETZ[id]; if (!g) return sichtSuche(id);
  const idee = r ? null : ideeVon(id), ws = WIRKSTELLE[id], weg = verweise(g.weg), braucht = r ? [] : brauchtRegeln(g), traegt = r ? regelTraegt(id) : [], themen = r ? [...new Set(r.klassen.map((k) => k.thema).filter((k) => k && thema(k)))] : [], klassen = g.klassen || [], stufen = new Set(klassen.map((k) => k.klasse)).size;
  const pfad = r ? `<a href="#/">Übersicht</a><span class="t">›</span><span>Sonne</span><span class="t">›</span><span>Schicht ${r.etage}: ${ETAGE[r.etage]}</span>`
    : `<a href="#/">Übersicht</a><span class="t">›</span><span>${g.planet}</span>${idee ? `<span class="t">›</span><a href="#/idee/${idee.id}">${idee.kurz}</a>` : ''}`;
  const zeich = ZEICHNUNGEN[id] ? zeichnung(id) : idee && ZEICHNUNGEN[idee.id] ? `<p class="klein leise" style="margin-bottom:8px">Zeichnung der tragenden Idee „${idee.kurz}“, aus der diese Regel folgt</p>` + zeichnung(idee.id) : vorgabe(g.zeichen || (idee && idee.zeichen), 'Zeichnung folgt');
  return `<article class="breite gesetz"><nav class="pfad">${pfad}</nav>
    <header class="g-kopf"><p class="ueber">${r ? 'Rechenregel ' + r.nr + ' von 14 · ' + regelSpanne(r) : 'Regel ' + id + ' · ' + (g.schulart || klasseVon(g))}</p><h1>${esc(g.name)}</h1><p class="merksatz">${g.satz}${genau(g)}</p></header>
    <div class="g-spalten"><div class="g-links">
      <section><h2 class="ueber">Die Zeichnung</h2>${zeich}</section>
      ${g.warum ? `<section><h2 class="ueber">Warum das gilt</h2><p class="fliess">${g.warum}</p></section>` : ''}
    </div><div class="g-rechts">
      ${klassen.length ? `<section><h2 class="ueber">${r ? `Dieselbe Regel in ${stufen} Klassen` : 'Beispiele'}</h2>${r ? `<p class="band-zeile">${klassenBand(r)}</p>${BAND_LEGENDE}` : ''}${g.wirkstelle ? `<p class="leise klein" style="margin-top:8px"><b>Gelb umrahmt ist die wirkende Stelle:</b> ${g.wirkstelle} Sie steht in jeder Klasse an derselben Stelle untereinander.</p>` : ''}${klassenLeiter(id, klassen)}</section>` : '<section><div class="z-folgt"><p class="ueber">Ausarbeitung folgt</p><p>Für diese Regel liegen bisher Name, Satz und Klasse vor. Ausgearbeitet sind die Sonne und die Planeten „Fläche und Raum“ und „Geometrie“.</p></div></section>'}
      ${g.voraus ? `<section><h2 class="ueber">Voraussetzung: wann es gilt</h2><p class="fliess">${g.voraus}</p></section>` : ''}
      ${g.fehler ? `<section><div class="fehler"><h2 class="ueber">Häufiger Fehler</h2><p>${g.fehler}</p></div></section>` : ''}
      ${braucht.length ? `<section><h2 class="ueber">Baut auf diesen Rechenregeln auf</h2><div class="verweise">${braucht.map((b) => verweisKnopf({ id: b, name: REGEL[b].name })).join('')}</div></section>` : ''}
      ${traegt.length ? `<section><h2 class="ueber">Darauf bauen auf: ${traegt.reduce((s, x) => s + x.n, 0)} Regeln auf ${new Set(traegt.map((x) => x.i.planet)).size} Planeten</h2><div class="verweise">${traegt.map((x) => `<a class="verweis" href="#/idee/${x.i.id}"><span class="nr">${x.i.planet}</span>${esc(x.i.kurz)} <span class="leise">(${x.n})</span></a>`).join('')}</div></section>` : ''}
      ${themen.length ? `<section><h2 class="ueber">Kommt vor in diesen Themen</h2><div class="verweise">${themen.map((k) => `<a class="verweis" href="${erklaerung(k)}">${esc(thema(k))} <span class="leise">· zur Erklärung ›</span></a>`).join('')}</div><p class="klein leise" style="margin-top:8px">Im Entwurf führt jeder Sprung zur selben Beispiel-Erklärung.</p></section>` : ''}
      ${g.verwandt ? `<section><h2 class="ueber">Verwandt</h2><p class="fliess">${g.verwandt}</p></section>` : ''}
      ${weg.length ? `<section><h2 class="ueber">Lässt sich erklären über</h2><div class="verweise">${weg.map(verweisKnopf).join('')}</div><p class="klein leise" style="margin-top:8px">Zum Erklären hilfreich. Keine Lernvoraussetzung und keine Sperre.</p></section>` : ''}
    </div></div></article>`;
}

// ---------- Eine tragende Idee und die Gesetze dahinter ----------
function sichtIdee(id) {
  const i = IDEE[id]; if (!i) return sichtSuche(id);
  return `<article class="breite gesetz"><nav class="pfad"><a href="#/">Übersicht</a><span class="t">›</span><span>${i.planet}</span></nav>
    <header class="g-kopf"><p class="ueber">${i.planet} · tragende Idee ${i.nr} von ${i.von} · ${esc(i.kurz)}</p><h1 class="merksatz gross">${i.satz}${genau(i)}</h1>${i.warum ? `<p class="fliess" style="max-width:46em">${i.warum}</p>` : ''}</header>
    <section><h2 class="ueber">Die Zeichnung</h2>${ZEICHNUNGEN[id] ? zeichnung(id) : vorgabe(i.zeichen, 'Zeichnung folgt')}</section>
    ${ideeBraucht(i).length ? `<section><h2 class="ueber">Baut auf diesen Rechenregeln auf</h2><div class="verweise">${ideeBraucht(i).map((b) => verweisKnopf({ id: b, name: REGEL[b].name })).join('')}</div></section>` : ''}
    ${(() => { const nach = {}; i.gesetze.forEach((gid) => { const k = gymZahlen(GESETZ[gid])[0] || 'RS / IB'; (nach[k] ||= []).push(gid); }); const kl = Object.keys(nach).filter((k) => +k).map(Number).sort((a, b) => a - b);
      return `<section><h2 class="ueber">${kl.length > 1 ? `Diese Idee läuft von Klasse ${kl[0]} bis ${kl[kl.length - 1]}` : kl.length ? `Diese Idee kommt in Klasse ${kl[0]} vor` : 'Diese Idee'}: ${i.gesetze.length} Regeln und Formeln</h2>
      <p class="leise klein" style="margin-bottom:10px">Geordnet nach der Klasse am Gymnasium, in der die Regel zuerst vorkommt. Ein Rechenbeispiel je Klasse folgt, sobald der Mathe-Profi es liefert.</p>
      <ol class="leiter ideen-leiter">${[...kl, ...(nach['RS / IB'] ? ['RS / IB'] : [])].map((k) => `<li><span class="stufe${+k ? '' : ' breit'}">${+k ? k : 'RS IB'}</span><div class="folge">${nach[k].map((gid) => { const g = GESETZ[gid]; return `<a class="karte" href="#/gesetz/${gid}"><span class="f-name"><span class="nr">${gid}</span> ${esc(g.name)}</span><span class="f-satz">${g.satz}</span></a>`; }).join('')}</div></li>`).join('')}</ol></section>`; })()}</article>`;
}

// ---------- Die Zeichnungen und der Stil ----------
function sichtZeichnungen() {
  const blatt = [...INHALT.regeln.map((r) => [r.id, 'Rechenregel ' + r.nr]), ...Object.values(IDEE).filter((i) => ZEICHNUNGEN[i.id]).map((i) => [i.id, `${i.planet} · Idee ${i.nr}`])];
  return `<div class="breite gesetz"><nav class="pfad"><a href="#/">Übersicht</a><span class="t">›</span><span>Zeichenstil</span></nav>
    <header class="g-kopf"><p class="ueber">Zeichenstil „Heft und Tafel“ · alle Zeichnungen nach den Zeichen-Vorgaben des Mathe-Profis</p><h1>${blatt.length} Zeichnungen, ein Stil</h1>
      <ul class="stil"><li><i style="background:var(--z-tinte)"></i>Strich in Tinte, Hilfslinien gestrichelt</li><li><i class="rahmen"></i>Gelb mit Rahmen: hier wirkt die Regel – in der Zeichnung und in der Rechenzeile</li><li><i style="background:var(--z-blau-fl);border:2px solid var(--z-blau)"></i>Blau: die Fläche oder Größe, um die es geht – und das zweite Paar, wenn zwei Dinge zusammengehören</li><li><i class="sf"></i>Schraffur: das dritte Paar</li><li><i class="karo"></i>Karos nur, wo gezählt wird – ein Karo ist eine Einheit</li><li><i class="winkel"></i>Höhen immer mit dem Zeichen für den rechten Winkel</li></ul></header>
    ${blatt.map(([k, ueber]) => { const x = REGEL[k] || IDEE[k]; return `<section class="z-blatt"><p class="ueber">${ueber}</p><h2>${esc(x.name || x.kurz)}</h2><p class="merksatz klein-m">${x.satz}${genau(x)}</p>${zeichnung(k)}</section>`; }).join('')}</div>`;
}

// ---------- Planeten-Karte (Übersicht A und B) ----------
function planetKarte(p, n) {
  const sp = planetSpanne(p.name), bild = p.ideen.some((i) => ZEICHNUNGEN[i.id]);
  return `<li class="bahn"><div class="breite bahn-innen"><div class="planet-kopf">${planetScheibe(p.name, 52)}<div><h3>${esc(p.name)}</h3><p>${n + 1}. Planet · ${p.ideen.length} tragende Ideen · ${p.zahl} Regeln${sp ? ' · ' + sp : ''}</p></div></div>
    <ul class="ideen n${p.ideen.length}${bild ? ' mit-bild' : ''}">${p.ideen.map((i) => `<li><a class="idee" href="#/idee/${i.id}">${ZEICHNUNGEN[i.id] ? zeichnungKlein(i.id) : ''}<span class="i-kurz">${esc(i.kurz)}</span><b>${i.satz}</b>${genau(i)}<span class="mehr">${i.gesetze.length} Regeln dahinter${ideeBraucht(i).length ? ` · braucht ${ideeBraucht(i).length > 1 ? 'die Rechenregeln' : 'Rechenregel'} ${ideeBraucht(i).map((x) => x.slice(1)).join(', ')}` : ''}</span></a></li>`).join('')}</ul></div></li>`;
}

// ---------- Weiche ----------
function zeige() {
  const h = decodeURIComponent(location.hash.replace(/^#\/?/, '')) || START, [art, ...rest] = h.split('/'), wert = rest.join('/');
  seite.innerHTML = art === 'regel' || art === 'gesetz' ? sichtGesetz(wert) : art === 'idee' ? sichtIdee(wert) : art === 'suche' ? sichtSuche(wert) : art === 'zeichnungen' ? sichtZeichnungen() : UEBERSICHT();
  document.body.classList.toggle('ohne-genau', OHNE_GENAU && !['regel', 'gesetz', 'idee', 'suche', 'zeichnungen'].includes(art));
  if (art !== 'suche') { suchfeld.value = ''; scrollTo(0, 0); }
  document.title = 'Entwurf: Regel-Universum';
}
addEventListener('hashchange', zeige);
if (P.get('von') === 'uebung') { const z = document.createElement('a'); z.className = 'zurueck-leiste'; z.href = `../../uebung/entwurf/uebung.html?s=erkl-regel&g=${document.body.dataset.g}`; z.textContent = '‹ Zurück zur Erklärung'; document.body.prepend(z); }
const e = document.createElement('div'); e.className = 'entwurf';
e.innerHTML = `<button aria-expanded="false">Entwurf ⚙</button><div class="entwurf-feld"><b>Entwurf, nicht die App.</b><a href="../../uebung/entwurf/uebung.html">Übungsbildschirm</a><a href="uebersicht-a.html?${P}">Übersicht A „Schnitt“</a><a href="uebersicht-a.html?genau=0&g=${document.body.dataset.g}">Übersicht A ohne „Genau gesagt“</a><a href="uebersicht-b.html?${P}">Übersicht B „Durch die Klassen“</a><a href="gesetz.html?${P}">Eine Regel aufgeschlagen</a><a href="zeichnungen.html?${P}">Zeichnungen</a><button>hell / dunkel</button></div>`;
e.querySelector('button').addEventListener('click', () => e.classList.toggle('offen'));
e.querySelector('.entwurf-feld button').addEventListener('click', () => { P.set('g', document.body.dataset.g === 'hell' ? 'nacht' : 'hell'); location.search = P.toString(); });
document.body.append(e);
