// Baut je Richtung eine einzige entwurf.html: Kern, Weltkarte und Schriften werden eingebettet (keine fremden Abhängigkeiten).
// Aufruf: node inhalte/pruefung/design/werkzeug/bauen.cjs
const fs = require('node:fs'); const path = require('node:path');
const w = __dirname, ziel = path.resolve(w, '..');
const kern = fs.readFileSync(path.join(w, 'kern.js'), 'utf8').replace('__WELT__', fs.readFileSync(path.join(w, 'welt.json'), 'utf8'));
for (const r of ['heft', 'abflug', 'linien']) {
  let h = fs.readFileSync(path.join(w, r + '.html'), 'utf8');
  h = h.replace(/\/\*SCHRIFT:([a-z0-9-]+)\*\//g, (_, n) => 'data:font/woff2;base64,' + fs.readFileSync(path.join(w, 'schriften', n + '.woff2')).toString('base64'));
  h = h.replace('/*KERN*/', () => kern);
  fs.mkdirSync(path.join(ziel, r), { recursive: true });
  fs.writeFileSync(path.join(ziel, r, 'entwurf.html'), h);
  console.log(r, Math.round(h.length / 1024) + ' KB');
}
