// Entwurf Übungsbildschirm am Handy. Zum Anklicken: Tasten tippen, Felder antippen, Prüfen. Geprüft wird hier nur zum Zeigen im Browser –
// in der App prüft der Server; das Kind sieht nach einem Fehlversuch nur Name und Hinweis der ersten verletzten Bedingung, am Ende das Beispiel.
const P = new URLSearchParams(location.search); document.body.dataset.g = P.get('g') === 'hell' ? 'hell' : 'nacht'; if (P.get('bild') === '1') document.body.classList.add('bild');
const app = document.getElementById('app'), R2 = REGEL;
const SYM = { ok: '<svg class="sym" viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="14" fill="none" stroke="currentColor" stroke-width="3"/><path d="M9 16.500l5 5l9 -10" fill="none" stroke="currentColor" stroke-width="3.500" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  nah: '<svg class="sym" viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="14" fill="none" stroke="currentColor" stroke-width="3"/><path d="M16 2a14 14 0 0 0 0 28z" fill="currentColor"/></svg>' };
// Beispiel-Aufgaben. e1 und m6 sind für den Entwurf erfunden; m3 ist das Beispiel aus dem Auftrag.
const AUFGABEN = {
  e1: { text: 'Berechne.', rechnung: '3 − (−2)', felder: 1, tasten: '−', loesung: ['5'], kurz: 'Zwei Minus: zweimal umdrehen. Von 3 geht es zwei Schritte nach rechts.', teil: 2 },
  m3: { text: 'Nenne drei verschiedene ganze Zahlen mit der Summe 0. Genau eine davon ist positiv.', felder: 3, tasten: '−', beispiel: '5, −2, −3', teil: 3,
    bed: [['drei verschiedene Zahlen', (w) => new Set(w).size === 3, () => 'Zwei deiner Zahlen sind gleich.'], ['Summe ist 0', (w) => w.reduce((a, b) => a + b, 0) === 0, (w) => `Deine Summe ist ${String(w.reduce((a, b) => a + b, 0)).replace('-', '−')}.`], ['genau eine positiv', (w) => w.filter((x) => x > 0).length === 1, (w) => `Bei dir sind ${w.filter((x) => x > 0).length} Zahlen positiv.`]] },
  m6: { text: 'Nenne sechs verschiedene ganze Zahlen mit der Summe 0.', felder: 6, tasten: '−', beispiel: '−5, −3, −1, 1, 3, 5', teil: 4,
    bed: [['sechs verschiedene Zahlen', (w) => new Set(w).size === 6, () => 'Zwei deiner Zahlen sind gleich.'], ['Summe ist 0', (w) => w.reduce((a, b) => a + b, 0) === 0, (w) => `Deine Summe ist ${String(w.reduce((a, b) => a + b, 0)).replace('-', '−')}.`]] },
  k2: { text: 'Schreibe als Dezimalzahl und als Bruch: die Hälfte von 1,5.', felder: 2, tasten: '−,/', beispiel: '0,75 und 3/4', teil: 5, bed: [['beide Zahlen sind gleich groß', () => true, () => '']] },
};
// Zustände zum Vorzeigen (Adresse ?s=…)
const VOR = { 'start': { seite: 'start' }, 'erkl': { seite: 'erkl' }, 'erkl-regel': { seite: 'erkl', blatt: 'regel' },
  'e1-leer': { a: 'e1' }, 'e1-tippen': { a: 'e1', w: ['−'] }, 'e1-richtig': { a: 'e1', w: ['5'], phase: 'richtig' }, 'e1-falsch': { a: 'e1', w: ['1'], phase: 'ende' }, 'e1-regel': { a: 'e1', w: ['1'], phase: 'ende', blatt: 'regel' },
  'm3-leer': { a: 'm3' }, 'm3-tippen': { a: 'm3', w: ['4', '−1'], aktiv: 1 }, 'm3-hinweis': { a: 'm3', w: ['4', '−1', '−2'], aktiv: 2, phase: 'hinweis', versuch: 1 }, 'm3-richtig': { a: 'm3', w: ['4', '−1', '−3'], phase: 'richtig' }, 'm3-ende': { a: 'm3', w: ['4', '−1', '−2'], phase: 'ende', versuch: 2 },
  'm6-leer': { a: 'm6' }, 'm6-tippen': { a: 'm6', w: ['−5', '−3', '2', '1'], aktiv: 3 }, 'm6-hinweis': { a: 'm6', w: ['−5', '−3', '2', '1', '4', '5'], aktiv: 5, phase: 'hinweis', versuch: 1 }, 'm6-ende': { a: 'm6', w: ['−5', '−3', '2', '1', '4', '5'], phase: 'ende', versuch: 2 },
  'k2-leer': { a: 'k2', w: ['0,75', '3/'], aktiv: 1 } };
let Z; const setze = (name) => { const v = VOR[name] || VOR['e1-leer']; Z = { seite: v.seite || 'ueben', a: v.a || 'e1', w: [...(v.w || [])], aktiv: v.aktiv || 0, phase: v.phase || 'eingabe', versuch: v.versuch || 0, blatt: v.blatt || null, modus: 'handy', name }; };
const zahl = (s) => Number(String(s).replace('−', '-').replace(',', '.'));
function werte() { const A = AUFGABEN[Z.a]; return Array.from({ length: A.felder }, (_, i) => Z.w[i] || ''); }
function verletzt() { const A = AUFGABEN[Z.a], w = werte().map(zahl); if (!A.bed) return werte()[0] === A.loesung[0] ? null : ['', null, () => '']; return A.bed.find((b) => !b[1](w)) || null; }

function taste(t) {
  const A = AUFGABEN[Z.a], w = werte(); if (Z.phase !== 'eingabe' && Z.phase !== 'hinweis') return;
  if (t === 'los') { const leer = w.findIndex((x) => !x); if (leer >= 0) { Z.aktiv = leer; return zeige(); } const v = verletzt(); Z.versuch++; Z.phase = !v ? 'richtig' : (A.bed && Z.versuch < 2 ? 'hinweis' : 'ende'); return zeige(); }
  let x = w[Z.aktiv];
  if (t === 'weg') { if (!x && Z.aktiv > 0) Z.aktiv--; else x = x.slice(0, -1); }
  else if (t === '−') x = x.startsWith('−') ? x.slice(1) : '−' + x; else if (x.replace('−', '').length < 6) x += t;
  Z.w = w; Z.w[Z.aktiv] = x; zeige();
}
const regelFeld = () => `<button class="regel-feld" data-tu="regel"><i>Regel dahinter</i><b>${R2.satz}</b><span aria-hidden="true">›</span></button>`;
function blattRegel() { return `<div class="schleier" data-tu="zu"></div><section class="blatt regel" role="dialog" aria-label="Regel dahinter"><div class="griff"></div><button class="zu" data-tu="zu" aria-label="Schließen">×</button>
  <p class="ueber">Rechenregel ${R2.nr} · ${R2.name}</p><h2>${R2.satz}</h2><p class="genau"><b>Genau gesagt:</b> ${R2.genau}</p>${zeichnung('R2')}
  <button class="haupt-knopf" data-tu="zu">${Z.seite === 'erkl' ? 'Zurück zur Erklärung' : 'Zurück zur Aufgabe'}</button><button class="neben-knopf" data-tu="universum">Im Regel-Universum ansehen ›</button></section>`; }

function zeige() {
  if (Z.seite === 'start') return app.innerHTML = `<div class="seite"><h1>Wo übst du heute?</h1>
    <div class="wahl" role="radiogroup" aria-label="Wo übst du heute?"><button role="radio" aria-checked="${Z.modus === 'tisch'}" data-modus="tisch"><span class="punkt"></span><b>Am Tisch</b><small>Mit Heft und Stift. Den Rechenweg schreibst du auf.</small></button>
      <button role="radio" aria-checked="${Z.modus === 'handy'}" data-modus="handy"><span class="punkt"></span><b>Nur am Handy</b><small>Ohne Heft. Aufgaben fürs Heft kommen beim nächsten Mal am Tisch.</small></button></div>
    <p class="woche"><i class="an"></i><i></i><i></i> Am Tisch diese Woche: 1 von 3</p><p class="erfunden">Zahl „1 von 3“ für den Entwurf erfunden.</p>
    <div class="unten"><button class="haupt-knopf" data-tu="ueben">Los</button></div></div>`;
  if (Z.seite === 'erkl') return app.innerHTML = `<header class="kopf"><button class="rund" data-tu="start" aria-label="Zurück">‹</button><div style="flex:1;font-weight:700">Erklärung</div></header><p class="kontext">Rom · Negative Zahlen · Etappe 1 von 3</p>
    <div class="seite" id="erkl"><h1>Plus und Minus mit negativen Zahlen</h1><p>Stell dich auf der Zahlengeraden auf die erste Zahl und schau nach rechts.</p><p>Plus heißt: geradeaus gehen. Minus heißt: erst umdrehen, dann gehen.</p>
    ${regelFeld()}<p>Beispiel: 3 − (−2). Zwei Minus, also zweimal umdrehen. Du schaust wieder nach rechts und gehst 2 Schritte: 5.</p><p class="erfunden">Erklärtext für den Entwurf erfunden. Den echten Text schreibt die Erklär-Rolle.</p>
    <div class="unten"><button class="haupt-knopf" data-tu="ueben">Üben</button></div></div>${Z.blatt === 'regel' ? blattRegel() : ''}`;
  const A = AUFGABEN[Z.a], w = werte(), alle = w.every(Boolean), v = Z.phase !== 'eingabe' ? verletzt() : null, t = A.tasten, n = A.felder;
  const felder = w.map((x, i) => `<button class="feld${Z.aktiv === i && (Z.phase === 'eingabe' || Z.phase === 'hinweis') ? ' aktiv' : ''}${x.length > 5 ? ' lang' : ''}${Z.phase === 'richtig' || Z.phase === 'ende' ? ' fest' : ''}" data-feld="${i}" aria-label="Feld ${i + 1} von ${n}${x ? ': ' + x : ', leer'}">${n > 1 ? `<span class="nr">${i + 1}</span>` : ''}<span class="wert">${x || (Z.aktiv === i ? '' : n === 1 ? '<span class="platz">Deine Antwort</span>' : '')}</span></button>`).join('');
  const hinweis = Z.phase === 'hinweis' && v ? `<div class="hinweis" role="status">${SYM.nah}<b>Noch nicht: ${v[0]}</b><p>${v[2](w.map(zahl))} Ändere deine Zahlen. Noch 1 Versuch.</p></div>` : '';
  const k = (z, kl = '') => `<button data-t="${z}" class="${kl}">${z}</button>`, sonder = (z) => (t.includes(z) ? `<button data-t="${z}" aria-label="${{ '−': 'Minus', ',': 'Komma', '/': 'Bruchstrich' }[z]}">${z}</button>` : '<button class="leer" tabindex="-1" aria-hidden="true"></button>');
  const tast = `<div class="tast">${k(1)}${k(2)}${k(3)}<button data-t="weg" aria-label="Löschen">⌫</button>${k(4)}${k(5)}${k(6)}${sonder('−')}${k(7)}${k(8)}${k(9)}${sonder(',')}${t.includes('/') ? k(0) + sonder('/') : k(0, 'zwei')}<button data-t="los" class="haupt zwei">${alle ? 'Prüfen' : n > 1 && w[Z.aktiv] ? 'Nächstes Feld' : 'Prüfen'}</button></div>`;
  let blatt = '';
  if (Z.phase === 'richtig') blatt = `<section class="blatt ok" role="status"><p class="urteil">${SYM.ok}Richtig</p>${A.bed ? `<ul class="bed">${A.bed.map((b) => `<li class="gut">${b[0]}</li>`).join('')}</ul>` : ''}<button class="haupt-knopf" data-tu="weiter">Weiter</button></section>`;
  if (Z.phase === 'ende') blatt = `<section class="blatt nah" role="status"><p class="urteil">${SYM.nah}Nicht ganz</p>${A.bed ? `<p>Deine Zahlen: <b style="font-family:var(--mono)">${w.join(', ')}</b></p><p class="gross">${v ? v[0] + ': ' + v[2](w.map(zahl)) : ''}</p><p class="gross">Zum Beispiel: <b>${A.beispiel}</b></p><div class="kurz"><i>Alle Bedingungen</i><ul class="bed">${A.bed.map((b) => `<li class="${v && b[0] === v[0] ? 'offen' : ''}">${b[0]}</li>`).join('')}</ul></div>` : `<p class="gross">Richtig wäre: <b>${A.loesung[0]}</b></p><div class="kurz"><i>Kurzregel</i>${A.kurz}</div>`}${regelFeld()}<button class="haupt-knopf" data-tu="weiter">Weiter</button></section>`;
  app.innerHTML = `<header class="kopf"><button class="rund" data-tu="pause" aria-label="Pause"><span>×</span></button><div class="leiste" role="img" aria-label="Aufgabe ${A.teil} von 5">${[1, 2, 3, 4, 5].map((i) => `<i class="${i < A.teil ? 'fertig' : i === A.teil ? 'jetzt' : ''}"></i>`).join('')}</div><button class="rund" data-tu="erkl" aria-label="Erklärung ansehen"><span>?</span></button></header>
    <p class="kontext">Rom · Negative Zahlen · Etappe 1 von 3</p><main class="mitte"><div class="aufgabe">${A.text}${A.rechnung ? `<span class="rechnung">${A.rechnung}</span>` : ''}</div><div class="felder n${n}">${felder}</div>${hinweis}</main>
    ${blatt ? '' : tast}${blatt}${Z.blatt === 'regel' ? blattRegel() : ''}`;
  if (hinweis) { const m = app.querySelector('.mitte'); m.scrollTop = m.scrollHeight; } // Felder und Hinweis bleiben über der Tastatur; notfalls rollt die Aufgabe nach oben
}
app.addEventListener('click', (e) => { const b = e.target.closest('[data-t],[data-feld],[data-tu],[data-modus]'); if (!b) return;
  if (b.dataset.t) return taste(b.dataset.t); if (b.dataset.feld && (Z.phase === 'eingabe' || Z.phase === 'hinweis')) { Z.aktiv = +b.dataset.feld; return zeige(); }
  if (b.dataset.modus) { Z.modus = b.dataset.modus; return zeige(); }
  const tu = b.dataset.tu; if (tu === 'regel') { Z.rollen = document.querySelector('#erkl,.mitte')?.scrollTop || 0; Z.blatt = 'regel'; zeige(); }
  else if (tu === 'zu') { Z.blatt = null; zeige(); const s = document.querySelector('#erkl,.mitte'); if (s) s.scrollTop = Z.rollen || 0; }
  else if (tu === 'universum') location.href = '../../gesetzbuch/entwurf/gesetz.html?' + new URLSearchParams({ g: document.body.dataset.g, von: 'uebung' }) + '#/regel/R2';
  else if (tu === 'ueben') { const m = Z.modus; setze('e1-leer'); Z.modus = m; zeige(); } else if (tu === 'erkl') { Z.seite = 'erkl'; zeige(); } else if (tu === 'start') { setze('start'); zeige(); }
  else if (tu === 'weiter') { setze({ e1: 'm3-leer', m3: 'm6-leer', m6: 'k2-leer', k2: 'e1-leer' }[Z.a]); zeige(); } });
setze(P.get('s') || 'start'); zeige();
const wahl = document.createElement('div'); wahl.className = 'entwurf'; wahl.innerHTML = `<select aria-label="Zustand des Entwurfs">${Object.keys(VOR).map((k) => `<option${k === Z.name ? ' selected' : ''}>${k}</option>`).join('')}<option value="_g">hell / dunkel</option></select>`;
wahl.firstChild.addEventListener('change', (e) => { if (e.target.value === '_g') { P.set('g', document.body.dataset.g === 'hell' ? 'nacht' : 'hell'); location.search = P.toString(); } else { setze(e.target.value); zeige(); } }); document.body.append(wahl);
