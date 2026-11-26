// Die drei Wege zur Regel. Reisekarte, Rückmeldung und Themen-Einstieg sind PLATZHALTER der heutigen App, nur die neuen Teile sind Entwurf.
const weg = document.getElementById('weg');
const mini = '<span class="mini-planet" aria-hidden="true">( )</span>';
const WEGE = {
  a() {
    weg.innerHTML = `<header class="kopf"><h1 class="kopf-titel" style="padding:0;text-align:left;padding-left:10px">Abflüge</h1></header><div class="bild-schirm">
      <div class="karte"><svg viewBox="0 0 400 520" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
        <path d="M40 120q60 -50 130 -20t90 -30q60 -20 100 30v120q-50 40 -110 20t-100 30q-70 20 -110 -30z" fill="#2B3A4D"/><path d="M90 330q50 -30 110 0t100 -10q40 30 20 90t-90 60q-80 10 -130 -40t-10 -100z" fill="#24443D"/>
        <path d="M120 170C170 210 200 300 250 380" stroke="#FFD23F" stroke-width="2.5" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>
        <circle cx="120" cy="170" r="10" fill="#45E0A0"/><circle cx="188" cy="262" r="10" fill="#FFD23F" stroke="#11161D" stroke-width="2"/><circle cx="250" cy="380" r="9" fill="none" stroke="#A9B3C1" stroke-width="2"/></svg>
        <button class="sonnen-knopf" data-hoch aria-label="Regeln am Himmel ansehen"><i>15</i>Regeln</button>
        <div class="schwebe"><p>Rom · Natürliche Zahlen</p><button class="haupt">Weiter: Zahlenstrahl <span aria-hidden="true">›</span></button></div></div>
      <p class="platzhalter">Platzhalter für die heutige Reisekarte. Neu ist nur der Knopf „Regeln“ oben rechts. Antippen: Die Karte schrumpft zur Erde, der Himmel geht auf.</p></div>`;
    weg.querySelector('[data-hoch]').addEventListener('click', () => { document.body.classList.add('steigt'); P.set('von', 'erde'); setTimeout(() => { location.href = 'uebersicht-a.html?' + P.toString(); }, RUHE() ? 180 : 760); });
  },
  b() {
    weg.innerHTML = `<header class="kopf"><button class="kopf-zurueck" aria-label="Schließen">${SYM.zu}</button><h1 class="kopf-titel">Lima · Terme vereinfachen</h1></header><div class="bild-schirm">
      <div class="bord"><p class="ueber">Bordkarte 4 · Lima</p><p class="frage">Vereinfache: 5x − (3x − 2)</p>
        <p class="ueber" style="color:var(--kurs)">Noch nicht · Kurs korrigieren</p>
        <div class="dz" style="margin-top:8px"><div><small>DU</small><strong>2x − 2</strong></div><div><small>ZIEL</small><strong>2x + 2</strong></div></div>
        <button class="geklemmt" data-regel="5">${mini}<span class="txt"><b>${GEKLEMMT[5]}</b><span class="mehr">Regel ansehen</span></span><span class="pfeil" aria-hidden="true">›</span></button></div>
      <button class="haupt" style="margin-top:14px" data-weiter>Neue Bordkarte <span aria-hidden="true">›</span></button>
      <p class="platzhalter">Platzhalter für die heutige Rückmeldung. Neu ist nur die Zeile mit dem Planeten. Sie erscheint nur, wenn der Server das Fehlbild einer Regel erkannt hat. Die Karte öffnet sich über der Aufgabe; „Zurück zur Aufgabe“ schließt sie, die Aufgabe steht unverändert da.</p></div>`;
    weg.querySelector('[data-regel]').addEventListener('click', () => oeffneRegel(5, 'fehler', true));
    weg.querySelector('[data-weiter]').addEventListener('click', () => melde('Hier kommt die nächste Bordkarte.'));
  },
  c() {
    weg.innerHTML = `<header class="kopf"><button class="kopf-zurueck" aria-label="Schließen">${SYM.zu}</button><h1 class="kopf-titel">Lima · Terme mit Klammern</h1></header><div class="bild-schirm">
      <p class="ueber" style="margin-top:6px">Neuer Flug · Etappe 1 von 6</p><h1>Klammern auflösen</h1>
      <div class="kennst"><p class="ueber">Das kennst du schon</p><h2>Bisher mit Zahlen. Jetzt mit x.</h2>
        <div class="zwilling"><small>Das kannst du</small><span class="rechnung"><span class="f">6</span> · (20 − 2) = <span class="f">6</span> · 20 − <span class="f">6</span> · 2</span></div>
        <div class="zwilling"><small>Das kommt jetzt</small><span class="rechnung"><span class="f">3</span> · (x + 2) = <span class="f">3</span> · x + <span class="f">3</span> · 2</span></div>
        <button class="regel-link" data-regel="4">${mini}Regel: Verteilen <span aria-hidden="true">›</span></button></div>
      <button class="haupt" data-weiter>Erklärung starten <span aria-hidden="true">›</span></button>
      <p class="platzhalter">Platzhalter für den Einstieg in eine Etappe. Neu ist der Kasten „Das kennst du schon“ mit den Zwillingszeilen. Er steht nur da, wenn in der Etappe eine Regel in neuem Gewand kommt.</p></div>`;
    weg.querySelector('[data-regel]').addEventListener('click', () => oeffneRegel(4, 'einstieg', true));
    weg.querySelector('[data-weiter]').addEventListener('click', () => melde('Hier startet die Erklärung der Etappe.'));
  },
};
function zeigeWeg(w) { document.body.classList.remove('steigt'); WEGE[w](); document.querySelectorAll('[data-weg]').forEach((k) => k.setAttribute('aria-pressed', k.dataset.weg === w)); }
document.querySelectorAll('[data-weg]').forEach((k) => k.addEventListener('click', () => { P.set('weg', k.dataset.weg); history.replaceState(null, '', '?' + P.toString()); zeigeWeg(k.dataset.weg); }));
zeigeWeg(P.get('weg') || 'a'); entwurfsSchalter(SEITEN);
if (P.get('auf')) setTimeout(() => weg.querySelector('[data-regel]')?.click(), 50);
addEventListener('pageshow', () => document.body.classList.remove('steigt'));
