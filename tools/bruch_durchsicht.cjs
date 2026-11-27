#!/usr/bin/env node
// Durchsicht der Bruch-Erkennung über alle echten Texte (liest nur, schreibt nichts).
// Vergleicht lernBruchTeile aus dem Stand HEAD (git show HEAD:lernen.js) mit dem Arbeitsstand (lernen.js).
// Aufruf: node tools/bruch_durchsicht.cjs [--alt <git-Stand>] [--alle]   (--alle: jede Änderung ungekürzt ausgeben)
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');

const wurzel = path.resolve(__dirname, '..');
const arg = process.argv.slice(2);
const altStand = arg.includes('--alt') ? arg[arg.indexOf('--alt') + 1] : 'HEAD';
const alle = arg.includes('--alle');

function ladeFunktion(quelle) {
  const a = quelle.indexOf('const LERN_BUCHST = '); const b = quelle.indexOf('function lernBruchKnoten(s) {');
  if (a < 0 || b < 0) throw new Error('Block der Bruch-Erkennung nicht gefunden');
  return new Function(quelle.slice(a, b) + '\nreturn [lernBruchTeile, LERN_HOCH];')();
}
const [alt] = ladeFunktion(execFileSync('git', ['show', `${altStand}:lernen.js`], { cwd: wurzel, encoding: 'utf8' }));
// Zeichenliste der Hochzeichen kommt aus dem Arbeitsstand (dieselbe wie in lernBruchTeile, keine eigene engere Liste).
const [neu, HOCH] = ladeFunktion(fs.readFileSync(path.join(wurzel, 'lernen.js'), 'utf8'));

// Kurzform: Bruch als [Zähler|Nenner], Trenner sichtbar (· = U+00A0, ˙ = U+202F).
const zeig = (t) => t.replace(/ /g, '·').replace(/ /g, '˙');
const kurz = (teile) => zeig(teile.map((t) => (typeof t === 'string' ? t : `${t.vz || ''}[${t.z}|${t.n}]`)).join(''));
const brueche = (teile) => teile.filter((t) => typeof t !== 'string').length;

// Verdächtige Reste: Bruch, auf den direkt Ziffer, Trenner + genau 3 Ziffern, Hochzahl oder ^ folgt;
// Bruch, dem direkt Ziffer + Trenner vorausgeht und dessen Zähler mit genau 3 Ziffern beginnt (Tausendergruppe).
function verdaechtig(teile) {
  const funde = [];
  teile.forEach((t, k) => {
    if (typeof t === 'string') return;
    const nach = typeof teile[k + 1] === 'string' ? teile[k + 1] : '';
    const vor = typeof teile[k - 1] === 'string' ? teile[k - 1] : '';
    if (/^\d/.test(nach)) funde.push('Ziffer danach');
    if (/^[   ]\d{3}(?!\d)/.test(nach)) funde.push('Tausendergruppe danach');
    if (new RegExp(`^[${HOCH}^]`).test(nach)) funde.push('Hochzahl danach');
    if (!t.vz && /\d[   ]$/.test(vor) && /^\d{3}(?!\d)/.test(t.z)) funde.push('Tausendergruppe davor');
  });
  return funde;
}

function* texte(datei, d) {
  for (const [i, a] of (d.aufgaben || []).entries()) {
    if (typeof a.f?.text === 'string') yield [`aufgaben[${i}].f.text`, a.f.text];
    for (const feld of ['a', 'c']) {
      const v = a[feld];
      if (typeof v === 'string') yield [`aufgaben[${i}].${feld}`, v];
      else if (Array.isArray(v)) for (const [j, x] of v.entries()) {
        if (typeof x === 'string') yield [`aufgaben[${i}].${feld}[${j}]`, x];
        else if (x && typeof x === 'object') for (const [k, y] of Object.entries(x)) if (typeof y === 'string') yield [`aufgaben[${i}].${feld}[${j}].${k}`, y];
      }
    }
    for (const feld of ['h', 'w']) if (typeof a[feld] === 'string') yield [`aufgaben[${i}].${feld}`, a[feld]];
  }
  // Lernkarten: alle Texte einer Etappe (regel, schritte, fehler, einstieg, probe, woerter, Bild-Beschriftungen …)
  const lauf = function* (o, pfad) {
    if (typeof o === 'string') { yield [pfad, o]; return; }
    if (Array.isArray(o)) { for (const [j, x] of o.entries()) yield* lauf(x, `${pfad}[${j}]`); return; }
    if (o && typeof o === 'object') for (const [k, x] of Object.entries(o)) yield* lauf(x, `${pfad}.${k}`);
  };
  for (const [i, e] of (d.inhalt?.etappen || []).entries()) yield* lauf(e, `etappen[${i}]`);
}

const ordner = path.join(wurzel, 'inhalte', 'themen');
const sum = { texte: 0, mitStrich: 0, altBr: 0, neuBr: 0, geaendert: 0, verdAlt: 0, verdNeu: 0, weniger: 0, mehr: 0, zweideutig: 0 };
const aenderungen = []; const restNeu = []; const zweideutigeTexte = [];
// Zweideutige Gruppe im Zähler: 1–3 Ziffern, Trenner, genau 3 Ziffern, Schrägstrich (2 125/128 oder 1 200/x) – bleibt bewusst Text,
// außer der Nenner hat auch eine Tausendergruppe (11 880/20 736).
const ZWEIDEUTIG = /(?:^|[^\d,.])\d{1,3}[ \u00a0\u202f]\d{3}\//;
const kuerze = (t) => (alle || t.length <= 160 ? t : t.slice(0, 157) + '…');
for (const datei of fs.readdirSync(ordner).filter((f) => f.endsWith('.json')).sort()) {
  const d = JSON.parse(fs.readFileSync(path.join(ordner, datei), 'utf8'));
  for (const [pos, t] of texte(datei, d)) {
    sum.texte++;
    if (!t.includes('/')) continue;
    sum.mitStrich++;
    if (ZWEIDEUTIG.test(t)) { sum.zweideutig++; zweideutigeTexte.push(`${datei} ${pos}\n    ${kuerze(kurz(neu(t)))}`); }
    const ta = alt(t); const tn = neu(t);
    const ba = brueche(ta); const bn = brueche(tn);
    sum.altBr += ba; sum.neuBr += bn;
    const va = verdaechtig(ta); const vn = verdaechtig(tn);
    sum.verdAlt += va.length; sum.verdNeu += vn.length;
    if (vn.length) restNeu.push(`${datei} ${pos}: ${vn.join(', ')}\n    ${kuerze(kurz(tn))}`);
    const ka = kurz(ta); const kn = kurz(tn);
    if (ka !== kn) {
      sum.geaendert++; if (bn < ba) sum.weniger++; if (bn > ba) sum.mehr++;
      aenderungen.push(`${datei} ${pos} (Brüche ${ba} → ${bn})\n  alt: ${kuerze(ka)}\n  neu: ${kuerze(kn)}`);
    }
  }
}
console.log(`Geänderte Texte (${aenderungen.length}):`);
for (const z of aenderungen) console.log(z);
console.log(`\nVerdächtige Reste im NEUEN Stand (${restNeu.length} Texte):`);
for (const z of restNeu) console.log('  ' + z);
console.log(`\nZweideutige Gruppe im Zähler (${zweideutigeTexte.length} Texte):`);
for (const z of zweideutigeTexte) console.log('  ' + z);
console.log('\nZusammenfassung');
console.log(`  Texte gesamt: ${sum.texte}, davon mit „/“: ${sum.mitStrich}`);
console.log(`  Gestapelte Brüche alt/neu: ${sum.altBr} / ${sum.neuBr}`);
console.log(`  Texte mit geändertem Ergebnis: ${sum.geaendert} (weniger Brüche: ${sum.weniger}, mehr: ${sum.mehr}, gleich viele: ${sum.geaendert - sum.weniger - sum.mehr})`);
console.log(`  Verdächtige Reste alt/neu: ${sum.verdAlt} / ${sum.verdNeu}`);
console.log(`  Zweideutige Gruppe im Zähler (Texte): ${sum.zweideutig}`);
