// Übersicht A „Schnitt von innen nach außen“: die Sonne in vier Schichten, darum die sieben Planeten.
const VARIANTE = 'a';
function schichtBaut(nr) { // aus den Abhängigkeiten gerechnet, nicht behauptet
  const tiefer = new Set(); INHALT.regeln.filter((r) => r.etage === nr).forEach((r) => r.braucht.forEach((b) => { if (REGEL[b].etage < nr) tiefer.add(REGEL[b].etage); }));
  const l = [...tiefer].sort(); return l.length ? 'baut auf Schicht ' + l.join(' und ') + ' auf' : 'der Kern: Darauf baut alles auf';
}
const regelKarte = (r) => `<a class="regel" href="#/regel/${r.id}">${ZEICHNUNGEN[r.id] ? zeichnungKlein(r.id, r.id === 'R13' ? 0 : 1) : '<span class="z-platz">Zeichnung folgt</span>'}<span class="kopfz"><span class="nr">REGEL ${r.nr}</span><span class="name">${esc(r.name)}</span></span><span class="satz">${r.merksatz}</span><span class="fuss"><span class="kl">${regelSpanne(r)}</span>${r.braucht.length ? `<span class="kl">braucht ${r.braucht.map((b) => b.slice(1)).join(', ')}</span>` : ''}</span></a>`;
const SONNE_BILD = `<svg viewBox="-50 -50 100 100" aria-hidden="true"><circle r="48" fill="var(--s4)" stroke="#11161D" stroke-width="1.5"/><circle r="37" fill="var(--s3)"/><circle r="26" fill="var(--s2)"/><circle r="15" fill="var(--s1)"/><g font-family="var(--mono)" font-weight="800" font-size="10" fill="#11161D" text-anchor="middle"><text y="3.500">1</text><text y="-16.500">2</text><text y="-27.500">3</text><text y="-38.500">4</text></g></svg>`;
const beweis = () => { const r = REGEL.R6, w = WIRKSTELLE.R6; return `<aside class="beweis"><p class="ueber">Ein Beispiel</p><h2>Dieselbe Regel in sechs Klassen</h2><p class="leise">${r.merksatz}</p><ol class="leiter">${r.klassen.map((k) => `<li><span class="stufe">${k.klasse}</span><div><p class="rechnung">${(w[k.klasse] || esc(k.text)).split('<br>')[0]}</p></div></li>`).join('')}</ol></aside>`; };
function einstieg() {
  return `<section class="breite einstieg"><div><h1>Gesetzbuch der Mathematik</h1>
    <p class="lead">Mathe von Klasse 5 bis 10 steht auf <b>14 Rechenregeln</b>. Sie gelten in jeder Klasse und in jedem Gebiet. Darum liegen <b>sieben Gebiete</b>, jedes mit wenigen tragenden Ideen. Alle Formeln dahinter findest du über die Suche.</p>
    <ul class="wegweiser"><li><i style="background:var(--s3);box-shadow:0 0 0 4px rgba(255,210,63,.3)"></i><span><b>Die Sonne:</b> 14 Rechenregeln in vier Schichten, von innen nach außen aufeinander aufgebaut.</span></li>
      <li><i style="background:#5AAEFF"></i><span><b>Sieben Planeten:</b> die Gebiete, von der Sonne aus immer weiter weg vom reinen Rechnen.</span></li>
      <li><i style="border:2px dashed var(--leise)"></i><span><b>Acht Arbeitsweisen:</b> wie man vorgeht. Sie gelten überall.</span></li></ul></div>${beweis()}</section>`;
}
function UEBERSICHT() {
  const schichten = [1, 2, 3, 4].map((nr) => { const rs = INHALT.regeln.filter((r) => r.etage === nr); return `<div class="band s${nr}"><div class="breite">${nr === 1 ? `<div class="sonne-kopf">${SONNE_BILD}<div><h2>Die Sonne: 14 Rechenregeln</h2><p>Ein Schnitt von innen nach außen. Jede Regel gilt von der genannten Klasse an unverändert, nur die Zahlen werden zu Brüchen und Buchstaben.</p></div></div>` : ''}
    <div class="band-titel"><span class="schicht">Schicht ${nr}</span><h3>${ETAGE[nr]}</h3><span class="baut">${schichtBaut(nr)}</span></div><div class="regeln${rs.length === 3 ? ' drei' : ''}">${rs.map(regelKarte).join('')}</div></div></div>`; }).join('');
  return `${einstieg()}<section class="sonne" aria-label="Die Sonne: 14 Rechenregeln">${schichten}</section>
    <section class="raum"><div class="breite"><div class="raum-kopf"><h2>Sieben Planeten: die Gebiete</h2><p>Jedes Gebiet hat wenige tragende Ideen. Aus ihnen folgen die einzelnen Gesetze und Formeln – zusammen ${INHALT.gesetze.length}.</p></div></div><ol class="bahnen">${PLANETEN.map(planetKarte).join('')}</ol></section>
    <section class="station"><div class="breite"><h2>Acht Arbeitsweisen</h2><p>Keine Gesetze, sondern Vorgehen. Sie gelten auf jedem Planeten.</p><ul class="weisen">${INHALT.arbeitsweisen.map((a) => `<li><span>${esc(a.name)}</span><b>${a.satz}</b></li>`).join('')}</ul></div></section>`;
}
