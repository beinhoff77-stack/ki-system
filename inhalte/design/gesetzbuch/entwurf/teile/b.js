// Übersicht B „Durch die Klassen“: jede Regel als Strahl von Klasse 5 bis 10, in jeder Klasse steht ihr Beispiel.
const VARIANTE = 'b';
const SF = { 1: 'var(--s1)', 2: 'var(--s2)', 3: 'var(--s3)', 4: 'var(--s4)' };
function einstiegB() {
  return `<section class="breite" style="padding-top:30px;padding-bottom:6px"><h1 style="font-size:34px;line-height:1.1">Gesetzbuch der Mathematik</h1>
    <p style="font-size:19px;line-height:1.45;margin-top:12px;max-width:44em">Mathe von Klasse 5 bis 10 steht auf <b>14 Rechenregeln</b>. Jede Zeile ist eine Regel, jede Spalte eine Klasse: In jeder Klasse steht <b>dieselbe Regel</b> in neuem Gewand. Darunter die <b>sieben Gebiete</b> mit ihren tragenden Ideen.</p></section>`;
}
function tafel() {
  const kl = [5, 6, 7, 8, 9, 10]; let z = '';
  for (const nr of [1, 2, 3, 4]) { z += `<tr class="schicht" style="--sf:${SF[nr]}"><th colspan="7">Schicht ${nr} · ${ETAGE[nr]}</th></tr>`;
    for (const r of INHALT.regeln.filter((x) => x.etage === nr)) { const von = Math.min(...r.klassen.map((k) => k.klasse)), bis = Math.max(...r.klassen.map((k) => k.klasse));
      z += `<tr><th class="r" scope="row"><a href="#/regel/${r.id}"><span class="nr">REGEL ${r.nr}</span> <span class="name">${esc(r.name)}</span><span class="satz">${r.merksatz}</span></a></th>${kl.map((k) => { const b = r.klassen.filter((x) => x.klasse === k); return `<td class="z${k >= von && k <= bis ? ' voll' : ''}">${b.map((x) => esc(x.text)).join('<br>')}</td>`; }).join('')}</tr>`; } }
  return `<div class="tafel-wrap"><table class="tafel"><thead><tr><th class="r">Die Sonne: 14 Rechenregeln</th>${kl.map((k) => `<th>Klasse ${k}</th>`).join('')}</tr></thead><tbody>${z}</tbody></table></div>`;
}
function karten() {
  let s = '';
  for (const nr of [1, 2, 3, 4]) { s += `<p class="b-schicht" style="background:${SF[nr]}">Schicht ${nr} · ${ETAGE[nr]}</p><div class="b-karten">`;
    for (const r of INHALT.regeln.filter((x) => x.etage === nr)) s += `<a class="karte b-karte" href="#/regel/${r.id}"><span class="nr">REGEL ${r.nr}</span> <span class="leise" style="font-size:15px;font-weight:600">${esc(r.name)}</span><span class="satz">${r.merksatz}</span>
      <span class="streifen" aria-label="${regelSpanne(r)}">${[5, 6, 7, 8, 9, 10].map((k) => `<i class="${r.klassen.some((x) => x.klasse === k) ? 'an' : ''}">${k}</i>`).join('')}</span><ul>${r.klassen.map((k) => `<li><span>Kl. ${k.klasse}</span>${esc(k.text)}</li>`).join('')}</ul></a>`;
    s += '</div>'; }
  return s;
}
function UEBERSICHT() {
  const breit = innerWidth >= 900;
  return `${einstiegB()}<section class="breite" style="padding-bottom:10px">${breit ? tafel() : '<h2 style="font-size:24px;margin-top:14px">Die Sonne: 14 Rechenregeln</h2>' + karten()}</section>
    <section class="raum" style="padding-top:34px"><div class="breite"><div class="raum-kopf"><h2>Sieben Planeten: die Gebiete</h2><p>Jedes Gebiet hat wenige tragende Ideen. Aus ihnen folgen die einzelnen Gesetze und Formeln – zusammen ${INHALT.gesetze.length}.</p></div></div><ol class="bahnen">${PLANETEN.map(planetKarte).join('')}</ol></section>
    <section class="station"><div class="breite"><h2>Acht Arbeitsweisen</h2><p>Keine Gesetze, sondern Vorgehen. Sie gelten auf jedem Planeten.</p><ul class="weisen">${INHALT.arbeitsweisen.map((a) => `<li><span>${esc(a.name)}</span><b>${a.satz}</b></li>`).join('')}</ul></div></section>`;
}
let bT; addEventListener('resize', () => { clearTimeout(bT); bT = setTimeout(() => { if (!location.hash || location.hash === '#/') zeige(); }, 150); });
