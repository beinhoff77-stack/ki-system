// ================= ENTWURF 2 · Tür, Inhalte, Kalender, Gutscheine =================
// Tür als gezeichnete Klappe (SVG): Rahmen-Fase, zwei Füllungen, Stanzlinie, Scharniere links, Zahl als Goldprägung.
// Sorten: normal (grün) · krampus (dunkles Holz, Hörner, Kratzer, Schwanzspitze) · t6 (Stiefel am Knauf) · t24 (Festtür blau-gold)
function tuerSvg(nr, sorte) {
  const u = 'td' + sorte; const kr = sorte === 'krampus', t24 = sorte === 't24';
  const f = kr ? { a: '#5A1F26', b: '#2A0A0F', hell: '#8A3A42', dunkel: '#16050A', fuell: '#3A1016', linie: '#F1E4C8' }
    : t24 ? { a: '#2A4BB0', b: '#0E1A55', hell: '#6C8CF0', dunkel: '#070D33', fuell: '#16287A', linie: '#FFE9A8' }
    : { a: '#22935A', b: '#0D5232', hell: '#5FD39A', dunkel: '#062E1B', fuell: '#0F5E39', linie: '#C9F5DD' };
  const ziffer = String(nr); const gr = ziffer.length > 1 ? 96 : 112;
  const zahl = kr ? ['#FFF6E2', '#E8D7B2', '#B89B6A'] : ['#FFF6C8', '#FFD23F', '#C98A0A'];
  const fuellung = (x, y, w, h) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="9" fill="${f.dunkel}" opacity=".85"/><rect x="${x + 2}" y="${y + 2}" width="${w - 2}" height="${h - 2}" rx="8" fill="${f.hell}" opacity=".55"/><rect x="${x + 2.5}" y="${y + 2.5}" width="${w - 4.5}" height="${h - 4.5}" rx="7.5" fill="${f.fuell}"/><rect x="${x + 2.5}" y="${y + 2.5}" width="${w - 4.5}" height="${(h - 4.5) * .5}" rx="7.5" fill="url(#${u}glanz)"/>`;
  const maserung = kr ? `<g stroke="#6E2A31" stroke-width="1.4" fill="none" opacity=".55">${[18, 44, 70, 104, 132, 160, 182].map((x, i) => `<path d="M${x} 6 C${x + 6} 60 ${x - 6} 120 ${x + 4} 170 S${x - 2} 230 ${x + 2} 240"/>`).join('')}<ellipse cx="128" cy="96" rx="5" ry="11" opacity=".8"/></g>` : '';
  const muster = t24 ? `<g fill="#FFE9A8" opacity=".5">${[[30, 40], [160, 52], [44, 204], [150, 196], [100, 26], [24, 120], [172, 124]].map(([x, y]) => `<path d="M${x} ${y - 4} l1.2 2.8 2.8 1.2 -2.8 1.2 -1.2 2.8 -1.2 -2.8 -2.8 -1.2 2.8 -1.2z"/>`).join('')}</g>` : `<rect width="196" height="246" fill="url(#${u}lein)" opacity="${kr ? .0 : .07}"/>`;
  const knauf = kr ? `<g transform="translate(174 128)"><circle r="8.5" fill="none" stroke="#2A2A2E" stroke-width="3.4"/><circle r="8.5" fill="none" stroke="#6B6B73" stroke-width="1.2" stroke-dasharray="10 40" transform="rotate(200)"/><circle cy="-8.5" r="3.4" fill="#3A3A40"/><circle cx="-1" cy="-9.4" r="1.1" fill="#8A8A92"/></g>`
    : `<g transform="translate(174 126)"><ellipse cx="1.5" cy="3" rx="8" ry="7" fill="#000" opacity=".25"/><circle r="8" fill="url(#${u}messing)"/><circle r="4.2" fill="none" stroke="#9A6A08" stroke-width="1.2" opacity=".8"/><ellipse cx="-2.6" cy="-3" rx="2.2" ry="1.4" fill="#FFF6C8" opacity=".9" transform="rotate(-35 -2.6 -3)"/></g>`;
  const scharnier = (y) => `<rect x="-3" y="${y}" width="9" height="22" rx="2" fill="url(#${u}messing)"/><path d="M-3 ${y + 7} H6 M-3 ${y + 15} H6" stroke="#9A6A08" stroke-width="1"/>`;
  const horn = (m) => `<g transform="scale(${m} 1)"><path d="M-36 8 C-47 0 -52 -16 -45 -34 C-44 -36 -42 -36 -42 -33 C-42 -20 -36 -10 -18 6 Z" fill="url(#${u}horn)"/><path d="M-42 -33 C-42 -20 -36 -10 -18 6 L-24 7 C-34 -2 -40 -14 -42 -33Z" fill="#9C7E52" opacity=".45"/>
      <path d="M-44.6 -24 q4 0 6.4 2.4 M-46 -13 q5 -.6 8 2.6 M-44 -2 q5 -1 8.4 2.6" stroke="#9C7E52" stroke-width="1.4" fill="none" stroke-linecap="round"/><path d="M-46.4 -28 C-48 -14 -44 -4 -36 4" stroke="#FFFBEF" stroke-width="1.5" fill="none" opacity=".7" stroke-linecap="round"/></g>`;
  const oben = kr ? `<g transform="translate(98 -1)">${horn(1)}${horn(-1)}</g>`
    : `<g transform="translate(98 2)"><path d="M-3 4 L-14 30 L-8 28 L-5 35 L2 8Z" fill="${t24 ? '#C98A0A' : '#B3122B'}"/><path d="M3 4 L14 32 L8 29 L6 36 L-1 8Z" fill="${t24 ? '#E0A40E' : '#C8172F'}"/>
      <path d="M0 2 C-10 -14 -30 -14 -30 -3 C-30 7 -14 8 0 3 Z" fill="url(#${u}band)"/><path d="M0 2 C10 -14 30 -14 30 -3 C30 7 14 8 0 3 Z" fill="url(#${u}band)"/>
      <path d="M0 2 C-8 -6 -18 -8 -24 -4 C-16 -4 -8 -1 0 3Z M0 2 C8 -6 18 -8 24 -4 C16 -4 8 -1 0 3Z" fill="#000" opacity=".22"/><path d="M-26 -8 C-22 -12 -14 -11 -9 -7" stroke="#fff" stroke-width="1.6" fill="none" opacity=".55" stroke-linecap="round"/>
      <rect x="-6" y="-4" width="12" height="11" rx="4" fill="${t24 ? '#E0A40E' : '#C8172F'}"/><path d="M-4 -2 h5" stroke="#fff" stroke-width="1.2" opacity=".5" stroke-linecap="round"/></g>`;
  const extra = kr ? `<g transform="translate(118 198)" stroke-linecap="round"><path d="M0 0 L22 -30 M10 6 L33 -24 M20 12 L43 -18" stroke="#16050A" stroke-width="5.6"/><path d="M0 0 L22 -30 M10 6 L33 -24 M20 12 L43 -18" stroke="#C25A5A" stroke-width="2.2"/><path d="M1 -1 L21 -29 M11 5 L32 -23 M21 11 L42 -17" stroke="#FFC2B8" stroke-width=".7" opacity=".7"/></g>
      <path d="M192 206 C200 204 206 210 205 218 C204 226 210 230 216 226" stroke="#8A1A26" stroke-width="3.4" fill="none" stroke-linecap="round"/><path d="M213 219 L224 222 L216 232 Z" fill="#8A1A26"/><path d="M213 219 L224 222 L218 225Z" fill="#B3263A"/>`
    : sorte === 't6' ? `<g transform="translate(174 126)"><path d="M0 4 C-2 14 2 22 -1 30" stroke="#FFF3D1" stroke-width="1.2" fill="none"/><g transform="translate(-13 30) rotate(6) scale(1.35)"><rect x="-1" y="-1" width="15" height="5" rx="2.5" fill="#fff"/><path d="M0 4 H12 V16 L18 18 C21 19 21 23 18 23 H0Z" fill="#E5243B"/><path d="M12 4 V16 L18 18 C21 19 21 23 18 23 H11 C13 22 14 20 10 18 V4Z" fill="#B3122B"/><circle cx="5" cy="-3" r="2.6" fill="#FFC94A"/><circle cx="9" cy="-4" r="2.2" fill="#F2B417"/></g></g>` : '';
  return `<svg class="tuer-svg" viewBox="-6 -40 208 300" aria-hidden="true"><defs>
    <linearGradient id="${u}holz" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${f.a}"/><stop offset="1" stop-color="${f.b}"/></linearGradient>
    <linearGradient id="${u}zahl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${zahl[0]}"/><stop offset=".45" stop-color="${zahl[1]}"/><stop offset="1" stop-color="${zahl[2]}"/></linearGradient>
    <radialGradient id="${u}messing" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#FFF1A8"/><stop offset=".5" stop-color="#FFC94A"/><stop offset="1" stop-color="#9A6A08"/></radialGradient>
    <linearGradient id="${u}band" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${t24 ? '#FFE27A' : '#FF5A6B'}"/><stop offset="1" stop-color="${t24 ? '#E0A40E' : '#C8172F'}"/></linearGradient>
    <linearGradient id="${u}horn" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#E8D7B2"/><stop offset=".7" stop-color="#F6ECD6"/><stop offset="1" stop-color="#B89B6A"/></linearGradient>
    <linearGradient id="${u}glanz" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".1"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient><linearGradient id="${u}sheen" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".16"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <pattern id="${u}lein" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(35)"><path d="M0 0 V6" stroke="#fff" stroke-width="1"/></pattern></defs>
    <rect width="196" height="246" rx="14" fill="url(#${u}holz)"/>${maserung}${muster}<rect width="196" height="246" rx="14" fill="url(#${u}sheen)"/>
    <path d="M2 232 V14 Q2 2 14 2 H182" stroke="${f.hell}" stroke-width="3" fill="none" opacity=".7"/><path d="M194 14 V232 Q194 244 182 244 H14" stroke="${f.dunkel}" stroke-width="4" fill="none" opacity=".8"/>
    <rect x="9" y="9" width="178" height="228" rx="9" fill="none" stroke="${f.linie}" stroke-width="1.6" stroke-dasharray=".1 5.2" stroke-linecap="round" opacity="${kr ? .35 : .5}"/>
    ${kr ? `<rect x="0" y="48" width="196" height="12" fill="#1C1C22"/><rect x="0" y="186" width="196" height="12" fill="#1C1C22"/><path d="M0 49 H196 M0 187 H196" stroke="#55555E" stroke-width="1"/>${[14, 60, 136, 182].flatMap((x) => [[x, 54], [x, 192]]).map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3" fill="#3A3A42"/><circle cx="${x - .8}" cy="${y - .9}" r="1" fill="#9A9AA6"/>`).join('')}`
      : `${fuellung(28, 28, 140, 82)}${fuellung(28, 128, 140, 92)}`}
    ${scharnier(30)}${scharnier(194)}
    <g font-family="Space Grotesk, system-ui, sans-serif" font-weight="700" font-size="${gr}" text-anchor="middle" letter-spacing="-4">
      <text x="${98 + 1}" y="${160 + 5}" fill="${f.dunkel}" opacity=".8">${ziffer}</text><text x="98" y="160" fill="url(#${u}zahl)">${ziffer}</text>
      <text x="98" y="160" fill="none" stroke="${kr ? '#FFFFFF' : '#FFFBE0'}" stroke-width="1" opacity=".45" transform="translate(-.8 -.8)">${ziffer}</text></g>
    ${knauf}${extra}${oben}</svg>`;
}

function tuerAnsicht(s) {
  const nacht = P.g === 'nacht'; const nr = { zweite: 6, 'tuer-krampus': 5, 'inhalt-krampus': 5, 'inhalt-jackpot': 13, 'inhalt-niete': 19, 'inhalt-karte6': 6, 'inhalt-karte24': 24, 'inhalt-sterne': 11 }[s] || P.tag;
  const tagD = { 'tuer-krampus': 5, 'inhalt-krampus': 5, 'inhalt-karte6': 6, 'inhalt-karte24': 24, 'inhalt-jackpot': 13, 'inhalt-niete': 19, 'inhalt-sterne': 11 }[s] || P.tag;
  const sorte = s.includes('krampus') ? 'krampus' : s === 'inhalt-jackpot' ? 'jackpot' : s === 'inhalt-niete' ? 'niete' : s.includes('karte') ? 'karte' : s === 'inhalt-sterne' ? 'sterne' : '';
  const zu = s === 'tuer' || s === 'zweite' || s === 'tuer-krampus';
  const tuerSorte = s === 'tuer-krampus' ? 'krampus' : nr === 6 ? 't6' : nr === 24 ? 't24' : 'normal';
  const ober = s === 'zweite' ? `2. TÜRCHEN HEUTE · ${datumText(P.tag).toUpperCase()}` : sorte === 'krampus' && !zu ? `KRAMPUS WAR DA · ${datumText(tagD).toUpperCase()}` : `ADVENTSKALENDER · ${datumText(tagD).toUpperCase()}`;
  const zeile = s === 'tuer-krampus' ? 'Hm. Diese Tür sieht anders aus …' : s === 'inhalt-krampus' ? 'Kein Sterne-Abzug. Nur eine kleine Aufgabe.' : s === 'inhalt-karte24' ? 'Frohe Weihnachten!' : s === 'tuer' ? 'Für deine Etappe. Tippen zum Öffnen.' : s === 'zweite' ? 'Zweite Etappe heute – du holst Türchen 6 nach. Mehr als 2 am Tag gehen nicht.' : '';
  const halb = P.auf === '1';
  const tuer = `<div class="rahmen2 ${halb ? 'auf halb' : ''} tuer-${tuerSorte}" id="rahmen"><div class="licht2" aria-hidden="true"><i></i></div><button type="button" class="klappe" id="tuerknopf" aria-label="Türchen ${nr} öffnen">${tuerSvg(nr, tuerSorte)}<span class="klappe-schatten" aria-hidden="true"></span></button></div>`;
  let buehne;
  if (zu) buehne = `${tuer}<div class="antippen">${halb ? 'STANDBILD · BEWEGUNG REDUZIERT' : '▲ TIPPEN ZUM ÖFFNEN'}</div>`;
  else if (s === 'inhalt-bild') buehne = `<div class="inhalt-r"><div class="motiv-gross2" role="img" aria-label="Bild: Koala mit Sonnenbrille und Weihnachtsmütze">${motivSvg('koala')}</div><p class="satz">31 Grad, Mütze trotzdem. Stil ist Stil.</p></div>`;
  else if (s === 'inhalt-geschenk') buehne = `<div class="inhalt-r">${gutscheinKarte({ nr, titel: 'Du bestimmst das Abendessen.', text: 'An einem Abend deiner Wahl. Sag einfach Bescheid.', sterne: 50 })}</div>`;
  else if (s === 'inhalt-krampus') buehne = `<div class="inhalt-r">${krampusKarte(5)}</div>`;
  else if (s === 'inhalt-jackpot') buehne = `<div class="inhalt-r">${jackpotKarte()}<p class="satz">Schon gutgeschrieben. Einfach so.</p></div>`;
  else if (s === 'inhalt-niete') buehne = `<div class="inhalt-r">${nieteKarte()}<p class="satz">Morgen wartet ein neues Türchen.</p></div>`;
  else if (s === 'inhalt-sterne') buehne = `<div class="inhalt-r">${sterneKarte(500)}</div>`;
  else if (s === 'inhalt-karte6' || s === 'inhalt-karte24') { const m = s === 'inhalt-karte6' ? 'nikolaus' : 'heiligabend'; buehne = `<div class="inhalt-r"><div class="karte-gross2 ${m}" role="img" aria-label="Karte ${m === 'nikolaus' ? 'Nikolaus' : 'Heiligabend'}">${motivSvg(m)}</div><p class="satz karte-satz">„${esc(MOTIVE.find((x) => x.id === m).satz)}“<small>– Mama und Papa</small></p></div>`; }
  else buehne = `<div class="inhalt-r"><div class="leer-licht2"><b>nur Licht.</b></div><p class="satz">Hier ist heute nichts versteckt. Aber die Etappe hast du – und die bleibt.</p></div>`;
  const funken = zu ? '' : `<div class="funken" aria-hidden="true">${Array.from({ length: 14 }, (_, i) => `<i style="left:${(10 + ((i * 37) % 80))}%;top:${(16 + ((i * 53) % 52))}%;opacity:${0.35 + ((i * 7) % 6) / 10};transform:scale(${.6 + (i % 3) * .3})"></i>`).join('')}</div>`;
  const badge = s === 'zweite' ? '<span class="badge">NACHGEHOLT</span>' : '';
  const STK = { ...STICKER, 'inhalt-sterne': ['Sheesh!', 's3'] };
  const st = STK[s] ? `<div class="sticker ${STK[s][1]}" aria-hidden="true">${STK[s][0]}</div>` : '';
  const weiter = `<a class="gross" href="#s=kalender&g=${P.g}"><span>Weiter: Zahlenstrahl<small>Etappe 3 von 6</small></span><span class="pf">›</span></a>`;
  const blatt = zu
    ? `<div class="blatt-ab"><p class="klein">Etappe gelandet ✓</p><p class="txt">${sorte === 'krampus' ? 'Diese Tür riecht nach … Aufgabe. Trotzdem aufmachen?' : 'Dahinter ist ein Bild oder ein Geschenk von Mama und Papa.'}</p><button type="button" class="gross gold" id="oeffnenknopf"><span>Türchen ${nr} öffnen</span><span class="pf">›</span></button><a class="textlink" href="#s=kalender-bereit&g=${P.g}">Später öffnen – weiter zu: Zahlenstrahl</a></div>`
    : `<div class="blatt-ab"><p class="klein">Türchen ${nr} ist offen</p><p class="txt">${sorte === 'krampus' ? 'Steht in „Meine Gutscheine“ unter „Vom Krampus“. Mama oder Papa haken ab, wenn’s erledigt ist.' : sorte === 'jackpot' ? '1.111 Sterne sind schon auf deinem Konto.' : sorte === 'niete' ? '1 Stern ist schon auf deinem Konto. Nicht jedes Türchen ist ein Jackpot.' : sorte === 'sterne' ? '500 Sterne sind schon auf deinem Konto.' : sorte === 'karte' ? (nr === 6 ? 'Heute nur eine Karte – das Geschenk gibt’s von Mama und Papa.' : 'Heute nur eine Karte – die Geschenke gibt’s unterm Baum.') : s === 'inhalt-geschenk' ? 'Einlösen, wann du willst: Menü › Meine Gutscheine. Die 50 Sterne sind schon gutgeschrieben.' : 'Bleibt im Adventskalender – du kannst es jederzeit wieder ansehen.'}</p>${nr < 24 ? `<p class="leise">Türchen ${nr + 1} wartet morgen – nach deiner nächsten Etappe.</p>` : ''}${weiter}<a class="textlink" href="#s=kalender&g=${P.g}">Adventskalender ansehen</a></div>`;
  const band = P.vorschau === '1' ? '<div class="vorschau-band">Vorschau – so sieht es Kind 1 · <a href="#s=eltern">zurück</a></div>' : '';
  const sorteKl = sorte ? 'sorte-' + sorte : tuerSorte === 't24' ? 'sorte-t24' : '';
  return `${band}<div class="ab ab2 ${nacht ? 'nacht' : 'hell'} ${sorteKl}" role="dialog" aria-modal="true" aria-label="Türchen ${nr}"><div class="szene">${funken}<div class="oben">${ober}</div><h2 class="titel">Türchen ${nr}${badge}</h2>${zeile ? `<p class="zeile">${zeile}</p>` : ''}<div class="buehne">${buehne}</div>${st}</div>${blatt}</div>`;
}

// ---------- Inhaltskarten ----------
const PRAEGUNG = (id) => `<svg class="praegung" viewBox="0 0 80 80" aria-hidden="true"><defs><path id="${id}" d="M40 40 m-29 0 a29 29 0 1 1 58 0 a29 29 0 1 1 -58 0"/></defs>
  <g fill="none" stroke-width="1.4"><circle cx="40" cy="40" r="36" stroke="#fff"/><circle cx="40" cy="40" r="36" stroke="#A8873A" opacity=".35" transform="translate(.9 .9)"/><circle cx="40" cy="40" r="22" stroke="#fff"/><circle cx="40" cy="40" r="22" stroke="#A8873A" opacity=".35" transform="translate(.9 .9)"/></g>
  <text font-family="ui-monospace, Menlo, monospace" font-size="7.4" font-weight="800" letter-spacing="2.2" fill="#A8873A" opacity=".45"><textPath href="#${id}">ADVENTSKALENDER · 2026 · ECHT ·</textPath></text>
  <path d="M40 27 l3.6 8 8.7 .8 -6.6 5.8 2 8.6 -7.7 -4.6 -7.7 4.6 2 -8.6 -6.6 -5.8 8.7 -.8z" fill="#A8873A" opacity=".3" transform="translate(.8 .8)"/><path d="M40 27 l3.6 8 8.7 .8 -6.6 5.8 2 8.6 -7.7 -4.6 -7.7 4.6 2 -8.6 -6.6 -5.8 8.7 -.8z" fill="#FFF9E6"/></svg>`;
const GUILLOCHE = `<svg class="guilloche" viewBox="0 0 320 160" preserveAspectRatio="none" aria-hidden="true"><g fill="none" stroke="#E7D39A" stroke-width=".7">${Array.from({ length: 9 }, (_, i) => `<path d="M0 ${18 + i * 16} ${Array.from({ length: 16 }, (_, j) => `Q${j * 20 + 10} ${18 + i * 16 + (j % 2 ? -7 : 7)} ${j * 20 + 20} ${18 + i * 16}`).join(' ')}"/>`).join('')}</g></svg>`;
function gutscheinKarte({ nr, titel, text, sterne }) {
  return `<div class="ticket-w"><div class="ticket" role="img" aria-label="Gutschein: ${esc(titel)} Hol dir bei Mama oder Papa ab."><div class="tk-kopf"><span class="tk-marke">${STERN_ICO}GUTSCHEIN</span><span>TÜR ${nr} · NR. ${String(nr).padStart(2, '0')}/24</span></div>
    <div class="tk-koerper">${GUILLOCHE}<small>HOL DIR BEI MAMA ODER PAPA AB</small><h3>${esc(titel)}</h3><p>${esc(text)}</p>${PRAEGUNG('pr' + nr)}</div>
    <div class="tk-perf" aria-hidden="true"></div><div class="tk-fuss"><span class="tk-ico">${GESCHENK_ICO}</span><span>Liegt jetzt in „Meine Gutscheine“.</span>${sterne ? `<b class="tk-st">+${sterne}<i>★</i></b>` : ''}</div></div></div>`;
}
const HUF = `<svg viewBox="0 0 40 40" aria-hidden="true"><g fill="currentColor"><path d="M8 4 C3 6 2 16 6 20 C9 22 13 20 14 16 C15 10 13 3 8 4Z"/><path d="M26 4 C31 6 32 16 28 20 C25 22 21 20 20 16 C19 10 21 3 26 4Z"/><path d="M12 26 C9 28 9 34 12 36 C14 37 16 35 16 33 C16 30 15 25 12 26Z" opacity=".7"/><path d="M22 26 C25 28 25 34 22 36 C20 37 18 35 18 33 C18 30 19 25 22 26Z" opacity=".7"/></g></svg>`;
function krampusKarte(nr) {
  return `<div class="kr-karte" role="img" aria-label="Krampus-Karte: Zimmer aufräumen, heute noch. Erledigt bestätigen Mama oder Papa.">
    <div class="kr-kopf"><span>KRAMPUS WAR DA</span><span>TÜR ${nr}</span><svg class="kr-kratz" viewBox="0 0 90 40" aria-hidden="true"><path d="M10 38 L30 2 M28 38 L48 2 M46 38 L66 2" stroke="#1C0A0E" stroke-width="6" stroke-linecap="round"/></svg></div>
    <div class="kr-in"><div class="kr-bild">${motivSvg('krampus')}</div><div><small>DEINE AUFGABE</small><h3>Zimmer aufräumen – heute noch.</h3><p>Bis zum Abendessen.</p></div></div>
    <div class="kr-perf" aria-hidden="true"></div><div class="kr-fuss"><span class="kr-box" aria-hidden="true"></span><span>Erledigt? Bestätigen Mama oder Papa.</span><span class="kr-huf" aria-hidden="true">${HUF}</span></div></div>`;
}
const WALZEN_STERN = (u) => `<svg viewBox="0 0 60 60" aria-hidden="true"><defs><linearGradient id="${u}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF6C8"/><stop offset=".45" stop-color="#FFD23F"/><stop offset="1" stop-color="#B57A06"/></linearGradient></defs><path d="M30 9 l6 13.2 14.4 1.4 -10.9 9.6 3.2 14.2 -12.7 -7.5 -12.7 7.5 3.2 -14.2 -10.9 -9.6 14.4 -1.4z" fill="url(#${u})"/><path d="M30 9 l6 13.2 14.4 1.4 -10.9 9.6 3.2 14.2 -12.7 -7.5z" fill="#8A5A00" opacity=".22"/><path d="M30 13 l4.4 9.6" stroke="#FFFBEA" stroke-width="1.4" stroke-linecap="round" opacity=".8"/></svg>`;
function jackpotKarte() {
  const walze = (i) => `<span class="jp-walze"><span class="jp-zeile weg">${WALZEN_STERN('jw' + i + 'a')}</span><span class="jp-zeile">${WALZEN_STERN('jw' + i + 'b')}</span><span class="jp-zeile weg">${WALZEN_STERN('jw' + i + 'c')}</span></span>`;
  return `<div class="jackpot2" role="img" aria-label="Jackpot: plus 1111 Sterne"><div class="jp-fenster"><i class="jp-linie"></i>${[0, 1, 2].map(walze).join('')}</div><div class="jp-wort2"><span>JACKPOT</span></div><div class="jp-zahl2">+1.111<i>★</i></div></div>`;
}
function nieteKarte() {
  return `<div class="niete2" role="img" aria-label="Niete mit Trostpreis: plus 1 Stern"><div class="nt-stempel2"><span>NIETE</span></div><div class="nt-trost">…aber nicht ganz.</div>
    <div class="nt-preis"><svg class="nt-stern" viewBox="0 0 80 80" aria-hidden="true"><path d="M40 6 l9.4 20.6 22.6 2.2 -17 15 5 22.2 -20 -11.8 -20 11.8 5 -22.2 -17 -15 22.6 -2.2z" fill="#FFD23F"/><path d="M40 6 l9.4 20.6 22.6 2.2 -17 15 5 22.2 -20 -11.8z" fill="#E0A40E"/>
      <g transform="rotate(-32 40 42)"><rect x="18" y="35" width="44" height="14" rx="7" fill="#F4C9A8"/><rect x="33" y="36.5" width="14" height="11" rx="2" fill="#E8B48E"/>${[[23, 39], [26, 45], [53, 39], [56, 45], [36, 39], [41, 44], [44, 39]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r=".9" fill="#C98E66"/>`).join('')}</g>
      <circle cx="33" cy="36" r="2.2" fill="#3A2A12"/><circle cx="47" cy="36" r="2.2" fill="#3A2A12"/><path d="M34 52 q6 -4 12 0" stroke="#3A2A12" stroke-width="2" fill="none" stroke-linecap="round"/></svg>
      <div><div class="nt-zahl">+1 ★</div><div class="nt-klein">TROSTPREIS</div></div></div></div>`;
}
function sterneKarte(n) {
  return `<div class="sterne2" role="img" aria-label="Plus ${n} Sterne"><svg class="muenze" viewBox="0 0 160 160" aria-hidden="true"><defs><radialGradient id="mzg" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#FFF6C8"/><stop offset=".5" stop-color="#FFD23F"/><stop offset="1" stop-color="#B57A06"/></radialGradient><linearGradient id="mzr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE27A"/><stop offset="1" stop-color="#8A5A00"/></linearGradient></defs>
    <circle cx="82" cy="84" r="70" fill="#000" opacity=".28"/><circle cx="80" cy="80" r="70" fill="url(#mzr)"/><circle cx="80" cy="80" r="66" fill="none" stroke="#FFF1A8" stroke-width="3" stroke-dasharray="2 4" opacity=".7"/><circle cx="80" cy="80" r="58" fill="url(#mzg)"/>
    <circle cx="80" cy="80" r="58" fill="none" stroke="#8A5A00" stroke-width="1.5" opacity=".5"/><path d="M80 38 l11 24 26 2.6 -19.6 17.2 5.8 25.6 -23.2 -13.6 -23.2 13.6 5.8 -25.6 -19.6 -17.2 26 -2.6z" fill="#E0A40E"/><path d="M80 38 l11 24 26 2.6 -19.6 17.2 5.8 25.6 -23.2 -13.6z" fill="#B57A06" opacity=".7"/><path d="M80 44 l8.6 18.8" stroke="#FFF6C8" stroke-width="2" stroke-linecap="round"/>
    <path d="M38 52 A50 50 0 0 1 70 26" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" opacity=".55"/></svg><div class="st-zahl">+${n}<i>★</i></div><div class="st-klein">GUTGESCHRIEBEN</div></div>`;
}
