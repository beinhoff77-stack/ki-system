// ================= ENTWURF 2 · Kalender (Tafel mit Klappen) und „Meine Gutscheine“ =================
function kindSeite(s) {
  const g = P.g;
  if (['tuer', 'inhalt-bild', 'inhalt-geschenk', 'zweite', 'leer', 'tuer-krampus', 'inhalt-krampus', 'inhalt-jackpot', 'inhalt-niete', 'inhalt-karte6', 'inhalt-karte24', 'inhalt-sterne'].includes(s)) return `<div class="kd" data-g="${g}">${tuerAnsicht(s)}</div>`;
  if (s === 'gutscheine') return `<div class="kd" data-g="${g}">${gutscheinSeite()}</div>`;
  if (['hinweis', 'hinweis-bereit', 'hinweis-limit', 'menue'].includes(s)) return `<div class="kd" data-g="${g}">${karteHinweis(s)}</div>`;
  return `<div class="kd" data-g="${g}">${kalender(s)}</div>`;
}
const SCHLEIFE_KL = (gold) => `<svg class="k-schleife" viewBox="0 0 40 20" aria-hidden="true"><path d="M20 9 C14 0 3 1 4 8 C5 13 14 12 20 10 Z M20 9 C26 0 37 1 36 8 C35 13 26 12 20 10 Z" fill="${gold ? '#C98A0A' : '#E5243B'}"/><path d="M20 9 C15 4 9 4 7 7 C11 7 15 8 20 10Z M20 9 C25 4 31 4 33 7 C29 7 25 8 20 10Z" fill="#000" opacity=".2"/><path d="M18 10 L14 19 M22 10 L26 19" stroke="${gold ? '#C98A0A' : '#E5243B'}" stroke-width="3" stroke-linecap="round"/><rect x="16.5" y="6.5" width="7" height="6" rx="2.5" fill="${gold ? '#E0A40E' : '#C8172F'}"/></svg>`;
const MOND_ICO = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M10.5 1.5a6.5 6.5 0 1 0 4 11.6A7 7 0 0 1 10.5 1.5z" fill="currentColor"/></svg>';
const UHR_ICO = '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 4.6V8l2.4 1.6" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>';
function kalender(s) {
  const szen = s === 'kalender' || s === 'kalender-tuer' ? 'kalender' : s === 'kalender-bereit' ? 'bereit' : s;
  const st = stand(1, szen, P.tag); const z = st.z;
  const offen = z.filter((x) => x === 'offen').length;
  const nach = z.map((x, i) => (x === 'nach' || x === 'bereit' ? i : 0)).filter(Boolean);
  let ober, h1, p, chips, banner = '';
  if (szen === 'vor1') { ober = 'SAMSTAG, 28. NOVEMBER'; h1 = 'Adventskalender'; p = 'Ab Dienstag, 1. Dezember: Nach jeder geschafften Etappe geht ein Türchen auf. Dahinter: ein Bild oder ein Geschenk von Mama und Papa.'; chips = '<span class="gold">Noch 3 Tage</span>'; }
  else if (szen === 'nach24') { ober = 'SAMSTAG, 26. DEZEMBER'; h1 = 'Frohe Weihnachten'; p = '22 von 24 Türchen sind offen. Türchen 23 und 24 holst du bis 31. Dezember nach – eins je Etappe, höchstens 2 am Tag.'; chips = '<span>22 offen</span><span class="gold">2 nachholen</span>'; }
  else if (szen === 'limit') { ober = datumText(P.tag).toUpperCase(); h1 = 'Für heute: alles raus.'; p = 'Du hast heute 2 Türchen geöffnet – mehr geht an einem Tag nicht. Türchen 7 wartet morgen auf dich.'; chips = `<span>${offen} offen</span><span>heute 2 von 2</span>`; banner = `<div class="kal-banner mond"><span class="sym">☾</span><span><b>Morgen geht’s weiter.</b> Deine Etappen zählen trotzdem – nur Türchen gibt’s höchstens 2 am Tag.</span></div>`; }
  else { ober = datumText(P.tag).toUpperCase(); h1 = 'Adventskalender'; chips = `<span>${offen} offen</span>${nach.length ? `<span class="gold">${nach.length + (z[P.tag] === 'heute' ? 1 : 0)} warten</span>` : ''}`;
    p = szen === 'bereit' ? 'Türchen 6 ist bereit – du hast heute schon eine Etappe geschafft. Tippen und öffnen.' : `Türchen 6 und ${P.tag} warten. Je geschaffte Etappe geht eins auf – höchstens 2 am Tag, das älteste zuerst.`; }
  const kachel = (n) => { const zs = z[n]; const i = inhalt(K1[n]);
    if (zs === 'offen') { const innen = i.art === 'bild' || i.art === 'karte' ? motivSvg(i.id).replace('<svg ', '<svg preserveAspectRatio="xMidYMid slice" ')
        : i.art === 'krampus' ? `<span class="gico">${HORN_ICO}</span>` : i.art === 'jackpot' || i.art === 'niete' ? `<span class="gross-z">+${i.sterne}<i>★</i></span>` : i.art === 'leer' ? '' : `<span class="gico">${GESCHENK_ICO}</span>`;
      const kl = i.art === 'bild' || i.art === 'karte' ? 'bild' : i.art === 'krampus' ? 'krampus' : i.art === 'jackpot' ? 'jackpot' : i.art === 'niete' ? 'niete' : i.art === 'leer' ? 'leer' : 'geschenk';
      const titel = i.art === 'krampus' ? 'Krampus' : i.art === 'jackpot' ? 'Jackpot' : i.art === 'niete' ? 'Trostpreis' : i.art === 'leer' ? 'nur Licht' : i.titel;
      return `<button type="button" class="td2 offen ${kl}" aria-label="Türchen ${n}, offen: ${esc(i.art === 'krampus' ? 'Krampus – ' + i.titel : i.titel)}" data-tuer="${n}"><span class="fach">${innen}</span><span class="fluegel" aria-hidden="true"></span><span class="n">${n}</span><span class="s">${esc(titel)}</span></button>`; }
    const lab = { nach: `${UHR_ICO}nachholen`, heute: 'heute · nach Etappe', bereit: 'öffnen!', morgen: `${MOND_ICO}morgen`, zu: '' }[zs];
    const aria = { nach: 'nachholen', heute: 'heute dran, nach deiner nächsten Etappe', bereit: 'bereit, jetzt öffnen', morgen: 'morgen', zu: 'noch zu' }[zs];
    const deko = zs === 'heute' || zs === 'bereit' ? SCHLEIFE_KL(zs === 'bereit') : '';
    return `<button type="button" class="td2 ${zs}" aria-label="Türchen ${n}, ${aria}"${zs === 'bereit' ? ` data-go="tuer"` : ''}>${deko}<span class="n">${n}</span><span class="s">${lab}</span></button>`; };
  const abholen = szen === 'vor1' ? '' : `<a class="karte2 gs-link" href="#s=gutscheine&g=${P.g}"><h2>MEINE GUTSCHEINE</h2><div class="abholen-z"><span class="gi">${GESCHENK_ICO}</span><span><b>2 einlösbar · 1 angefragt</b><small>Eis oder Bubble Tea, Einmal Abwasch frei …</small></span></div></a>`;
  const regeln = `<div class="karte2"><h2>SO GEHT’S</h2><ul class="regel-l"><li>Etappe geschafft → ein Türchen geht auf.</li><li>Verpasst? Holst du nach – das älteste zuerst.</li><li>Höchstens 2 am Tag, dann braucht’s 2 Etappen.</li><li>Morgen-Türchen bleiben zu bis morgen.</li></ul></div>`;
  const legende = `<div class="legende2"><span><i class="o"></i>offen</span><span><i class="b"></i>bereit</span><span><i class="h"></i>heute</span><span><i class="n"></i>nachholen</span><span><i class="m"></i>morgen</span><span><i class="z"></i>noch zu</span></div>`;
  const links = `<div><div class="kal-held"><div class="licht"></div><div class="ober">${ober}</div><h1>${h1}</h1><p>${p}</p><div class="kal-status">${chips}</div></div>${banner}<div class="tafel"><div class="tafel-deko" aria-hidden="true"></div><div class="tueren2">${UMORDNUNG.map(kachel).join('')}</div></div>${legende}</div>`;
  const rechts = `<div class="seite-r">${abholen}${regeln}</div>`;
  let blatt = '';
  if (s === 'kalender-tuer') { const i = inhalt(K1[5]); blatt = `<div class="kd-blatt-hg"><div class="kd-blatt" role="dialog" aria-modal="true" aria-label="Türchen 5"><div class="griff"></div><div class="ober">TÜRCHEN 5 · GEÖFFNET AM 5.12.</div><h2>${esc(i.titel)}</h2><div class="motiv-gross2" style="margin:10px auto 0">${motivSvg(i.id)}</div><p class="satz" style="margin:14px auto 0">${esc(i.text)}</p><a class="knopf2" href="#s=kalender&g=${P.g}">Schließen</a></div></div>`; }
  return `<div class="kd-seite"><div class="kd-kopf"><a class="zur" href="#s=hinweis&g=${P.g}" aria-label="Zurück zur Reisekarte">‹</a><b>Adventskalender</b><span class="stern-chip">★ 340</span><button class="menue-k" type="button" aria-label="Menü">≡</button></div><div class="kd-inhalt">${links}${rechts}</div>${blatt}</div>`;
}
function gutscheinSeite() {
  const L = GUTSCHEINE[1]; const W = { offen: 0, spaeter: 0, angefragt: 1, eingeloest: 2 };
  const liste = [...L].sort((a, b) => W[a.z] - W[b.z]);
  const karte = (x) => { const ein = x.z === 'eingeloest';
    const unten = x.z === 'angefragt' ? `<span class="gs-status wartet"><i class="sanduhr" aria-hidden="true"></i>Angefragt – wartet auf Mama oder Papa</span>`
      : ein ? `<span class="gs-status">✓ Eingelöst am ${x.ein}</span>`
      : `${x.z === 'spaeter' ? '<span class="gs-status spaeter">Heute nicht – ein andermal. Bleibt gültig.</span>' : ''}<button type="button" class="gs-ein" aria-label="Einlösen: ${esc(x.t)}">Einlösen</button>`;
    const stempel = ein ? '<span class="gs-stempel" aria-hidden="true">EINGELÖST</span>' : x.z === 'angefragt' ? '<span class="gs-stempel blau" aria-hidden="true">ANGEFRAGT</span>' : '';
    return `<li class="gs2 ${x.z}" ${ein ? 'aria-disabled="true"' : ''}><div class="gk"><span>${STERN_ICO}GUTSCHEIN${x.neu ? ' · NEU' : ''}</span><span>TÜR ${x.n} · ${x.am}</span></div><div class="gs-in"><h3>${esc(x.t)}</h3><p>${esc(x.x || Object.values(G).find((v) => x.t.startsWith(v[0].slice(0, 10)))?.[1] || '')}</p></div><div class="gs-perf" aria-hidden="true"></div><div class="gs-fuss">${unten}${stempel}</div></li>`; };
  return `<div class="kd-seite"><div class="kd-kopf"><a class="zur" href="#s=kalender&g=${P.g}" aria-label="Zurück">‹</a><b>Meine Gutscheine</b><span class="stern-chip">★ 390</span><button class="menue-k" type="button" aria-label="Menü">≡</button></div>
    <div class="kd-inhalt gs-seite"><div><p class="gs-unter">Aus deinem Adventskalender. Gelten, bis du sie einlöst – auch nach Weihnachten.</p><ul class="gs-liste">${liste.map(karte).join('')}</ul>
    <h2 class="gs-h">VOM KRAMPUS</h2><ul class="gs-liste"><li class="gs2 krampus"><div class="gk"><span>KRAMPUS WAR DA</span><span>TÜR 5 · 5.12.</span></div><div class="gs-in"><span class="kr-huf2" aria-hidden="true">${HUF}</span><h3>Zimmer aufräumen – heute noch.</h3><p>Bis zum Abendessen.</p></div><div class="gs-perf" aria-hidden="true"></div><div class="gs-fuss"><span class="gs-status kr">☐ Erledigt? Mama oder Papa haken ab.</span></div></li></ul>
    <p class="gs-unter klein">Einlösen = Mama oder Papa bekommen Bescheid und bestätigen. Bilder aus den Türchen findest du im <a href="#s=kalender&g=${P.g}">Adventskalender</a>.</p></div></div></div>`;
}
