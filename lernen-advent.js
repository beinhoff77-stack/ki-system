/* Adventskalender (Kind und Eltern) und Weihnachts-Ebene „Winternacht“ der Reisekarte.
   Nachgeladen von lernen.js (lernAdventLaden) – nur im Advent-Fenster (1.12.–6.1.) bzw. auf den Advent-Seiten. Kein Netz außer lernen-api.
   Vorgaben: inhalte/design/advent/server.md (Schnittstelle), entwurf2 (Grafik, abgenommen), entwurf1/umsetzung1.md (Einhänge-Stellen).
   Grafik (Motive, Tür, Karten, Karten-Ebene) übernommen aus inhalte/design/advent/entwurf2/teile/*.js – gleiche Formen und Farben.
   Texte der Eltern (Titel, Text) kommen nie als HTML in die Seite (DOM-Text); innerHTML nur für feste Grafiken. */
(function () {
'use strict';
const nurDa = (x) => x !== null && x !== undefined && x !== false;
const grafik = (html, cls, tag = 'div') => { const d = el(tag, { class: cls, 'aria-hidden': 'true' }); d.innerHTML = html; return d; };
let uNr = 0; const uid = (p) => p + (++uNr).toString(36);
const zahlS = (n) => lernZahl(Number(n) || 0); // „1 111“ wie überall in der App

// ================= Motive (Entwurf 2, teile/v_motive2.js) =================
const ML = (u, id, st, x2 = 0, y2 = 1, x1 = 0, y1 = 0) => `<linearGradient id="${u}${id}" x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}">${st.map(([o, c, a = 1]) => `<stop offset="${o}" stop-color="${c}" stop-opacity="${a}"/>`).join('')}</linearGradient>`;
const MR = (u, id, st, cx = .5, cy = .5, r = .6) => `<radialGradient id="${u}${id}" cx="${cx}" cy="${cy}" r="${r}">${st.map(([o, c, a = 1]) => `<stop offset="${o}" stop-color="${c}" stop-opacity="${a}"/>`).join('')}</radialGradient>`;
const FU = (x, y, r, c = '#FFF3C4', o = 1) => `<path d="M${x} ${y - r}C${x + r * .14} ${y - r * .14} ${x + r * .14} ${y - r * .14} ${x + r} ${y}C${x + r * .14} ${y + r * .14} ${x + r * .14} ${y + r * .14} ${x} ${y + r}C${x - r * .14} ${y + r * .14} ${x - r * .14} ${y + r * .14} ${x - r} ${y}C${x - r * .14} ${y - r * .14} ${x - r * .14} ${y - r * .14} ${x} ${y - r}Z" fill="${c}" opacity="${o}"/>`;
const PK = (pts, c = '#fff', o = .8) => `<g fill="${c}" opacity="${o}">${pts.map(([x, y, r = 1.2]) => `<circle cx="${x}" cy="${y}" r="${r}"/>`).join('')}</g>`;
const ST5 = (cx, cy, r, ri = .45, rot = 0) => { let d = ''; for (let i = 0; i < 10; i++) { const a = (i * 36 - 90 + rot) * Math.PI / 180; const rr = i % 2 ? r * ri : r; d += (i ? 'L' : 'M') + (cx + Math.cos(a) * rr).toFixed(1) + ' ' + (cy + Math.sin(a) * rr).toFixed(1); } return d + 'Z'; };
const ST5H = (cx, cy, r, ri = .45, rot = 0) => { let d = `M${cx} ${cy}`; for (let i = 0; i <= 5; i++) { const a = (i * 36 - 90 + rot) * Math.PI / 180; const rr = i % 2 ? r * ri : r; d += 'L' + (cx + Math.cos(a) * rr).toFixed(1) + ' ' + (cy + Math.sin(a) * rr).toFixed(1); } return d + 'Z'; };
// Mütze (gleiche Form wie auf der Karte), x/y = Kopfmitte, s = Kopfradius/10
const MU = (x, y, s, rot = -10) => `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})"><g transform="translate(0 1.1)"><path d="M7.4 -9.6C7.2 -16 4.6 -22.2 -.6 -24.6C-5.8 -26.8 -11 -25.2 -14 -20.6C-11 -21.6 -7.2 -21 -4.2 -18.6C-6 -15.4 -7.1 -12.4 -7.4 -9.6Z" fill="#E5243B"/><path d="M7.4 -9.6C7.2 -16 4.6 -22.2 -.6 -24.6C2.6 -20.4 3.8 -15 3.8 -9.6Z" fill="#B3122B"/><path d="M-14 -20.6C-11 -21.6 -7.2 -21 -4.2 -18.6C-7 -19.4 -10.4 -19.8 -14 -20.6Z" fill="#8E0E22"/><path d="M-1.2 -24.4C-6 -26.4 -10.6 -25 -13.4 -21.2C-10.2 -23.4 -6 -24.2 -2.4 -23.2Z" fill="#FF8A95"/><circle cx="-14.6" cy="-19.4" r="3.6" fill="#fff"/><path d="M-11.2 -18.4a3.6 3.6 0 0 1 -6.4 1.6a3.6 3.6 0 0 0 6.4 -1.6Z" fill="#D5DEEA"/></g><path d="M-7.9 -6.2A10 10 0 0 1 7.9 -6.2" stroke="#fff" stroke-width="4.2" fill="none" stroke-linecap="round"/><path d="M-6.4 -5.4A8.4 8.4 0 0 1 6.4 -5.4" stroke="#D5DEEA" stroke-width="1.3" fill="none" stroke-linecap="round"/></g>`;
const AUGE = (x, y, r = 3.2) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#1B0C3A"/><circle cx="${x - r * .35}" cy="${y - r * .4}" r="${r * .32}" fill="#fff"/>`;
const PAKET = (x, y, w, h, f, fs, b) => `<g><rect x="${x}" y="${y}" width="${w}" height="${h}" rx="2" fill="${f}"/><rect x="${x + w * .7}" y="${y}" width="${w * .3}" height="${h}" rx="2" fill="${fs}"/><rect x="${x + w / 2 - 2}" y="${y}" width="4" height="${h}" fill="${b}"/><rect x="${x}" y="${y + h * .32}" width="${w}" height="3.4" fill="${b}"/><path d="M${x + w / 2} ${y}c-6 -8 -13 -3 -8 1zM${x + w / 2} ${y}c6 -8 13 -3 8 1z" fill="${b}"/></g>`;
const BAND = (u, text, y, a = '#FFE27A', b = '#E0A40E') => `<g><path d="M20 ${y + 4} L8 ${y + 4} L14 ${y + 13} L8 ${y + 22} L28 ${y + 22}Z M180 ${y + 4} L192 ${y + 4} L186 ${y + 13} L192 ${y + 22} L172 ${y + 22}Z" fill="${b}"/><path d="M20 ${y + 22} L28 ${y + 26} L28 ${y + 22}Z M180 ${y + 22} L172 ${y + 26} L172 ${y + 22}Z" fill="#7A5200"/>
  <rect x="20" y="${y}" width="160" height="22" rx="2" fill="url(#${u}band)"/><rect x="20" y="${y}" width="160" height="5" fill="#fff" opacity=".25"/><text x="100" y="${y + 15.6}" text-anchor="middle" font-family="Space Grotesk, system-ui, sans-serif" font-size="12.5" font-weight="700" letter-spacing="3" fill="#3A2600">${text}</text></g>${ML(u, 'band', [[0, a], [1, b]])}`;
const LICHTER = (pts, farben = ['#FFC94A', '#FF5A5F', '#FFF3D1', '#3DDC84'], r = 3) => pts.map(([x, y], i) => `<circle cx="${x}" cy="${y + r}" r="${r * 3}" fill="${farben[i % farben.length]}" opacity=".22"/><circle cx="${x}" cy="${y + r}" r="${r}" fill="${farben[i % farben.length]}"/><circle cx="${x - r * .35}" cy="${y + r * .6}" r="${r * .35}" fill="#fff" opacity=".8"/>`).join('');
const SV = (inner) => `<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">${inner}</svg>`;

const M2 = {
  koala: (u) => SV(`<defs>${ML(u, 'h', [[0, '#2A1B5E'], [.45, '#7B1E6E'], [.8, '#F0522B'], [1, '#FF9A3C']])}${ML(u, 'gl', [[0, '#3B1D5E'], [.5, '#1B0C3A'], [1, '#5A2A7A']], 1, 1)}${MR(u, 'so', [[0, '#FFF1A8'], [.6, '#FFD23F'], [1, '#FF9A3C']])}</defs>
    <rect width="200" height="200" fill="url(#${u}h)"/>${PK([[18, 20], [52, 12, 1], [88, 26, 1], [170, 16], [140, 34, 1], [190, 52, 1]], '#FFF3C4', .7)}
    <circle cx="156" cy="136" r="36" fill="url(#${u}so)"/><rect y="136" width="200" height="64" fill="#3B1D5E"/><rect y="164" width="200" height="36" fill="#2A1250"/>
    <g fill="#FFD23F">${[[138, 142, 36], [144, 150, 24], [150, 158, 14], [153, 168, 8]].map(([x, y, w]) => `<rect x="${x}" y="${y}" width="${w}" height="2.6" rx="1.3" opacity=".8"/>`).join('')}</g>
    <path d="M-10 182 C40 168 120 150 214 116" stroke="#3E281C" stroke-width="13" fill="none" stroke-linecap="round"/><path d="M-10 180 C40 166 120 148 214 114" stroke="#6B4530" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M-10 177 C40 163 120 145 214 111" stroke="#8A5E44" stroke-width="2" fill="none" stroke-linecap="round"/>
    ${[[18, 172, -40, 24], [40, 168, 30, 22], [170, 128, -60, 26], [186, 122, 24, 22], [150, 140, 40, 20]].map(([x, y, r, l]) => `<g transform="translate(${x} ${y}) rotate(${r})"><path d="M0 0C${l * .3} ${-l * .3} ${l * .7} ${-l * .3} ${l} 0C${l * .7} ${l * .22} ${l * .3} ${l * .22} 0 0Z" fill="#7FB59A"/><path d="M0 0C${l * .3} ${l * .22} ${l * .7} ${l * .22} ${l} 0Z" fill="#4E7F69"/></g>`).join('')}
    ${LICHTER([[30, 170], [56, 163], [150, 133], [176, 123]], undefined, 2.4)}
    <ellipse cx="102" cy="140" rx="36" ry="30" fill="#9AA3B5"/><path d="M128 120 C142 136 136 162 112 169 C128 158 132 140 128 120Z" fill="#7A849B"/><ellipse cx="98" cy="148" rx="19" ry="16" fill="#DCE1EA"/>
    <ellipse cx="80" cy="160" rx="13" ry="8" fill="#A7B0C1" transform="rotate(-14 80 160)"/><ellipse cx="124" cy="152" rx="13" ry="8" fill="#8892A8" transform="rotate(-14 124 152)"/><path d="M72 164l-2 4M77 166l-1 4M82 166l0 4" stroke="#1B0C3A" stroke-width="1.6" stroke-linecap="round"/>
    <circle cx="70" cy="76" r="18" fill="#A7B0C1"/><circle cx="132" cy="76" r="18" fill="#8892A8"/><circle cx="71" cy="78" r="11" fill="#EEF1F6"/><circle cx="131" cy="78" r="11" fill="#DCE1EA"/>${[[62, 70], [64, 86], [77, 88]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3" fill="#EEF1F6"/>`).join('')}
    <circle cx="101" cy="96" r="31" fill="#A7B0C1"/><path d="M126 78 C138 98 128 122 104 127 C120 116 128 98 126 78Z" fill="#8892A8"/><path d="M78 84 C80 74 88 68 96 66" stroke="#C3CAD7" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M74 86 Q74 80 80 80 H95 Q99 80 98 86 L96 95 Q95 100 89 100 H82 Q76 100 75 95Z" fill="url(#${u}gl)"/><path d="M104 86 Q103 80 108 80 H122 Q128 80 127 86 L126 95 Q125 100 119 100 H112 Q106 100 105 95Z" fill="url(#${u}gl)"/>
    <path d="M97 84 H105" stroke="#1B0C3A" stroke-width="3"/><path d="M79 92 L88 82 M84 96 L92 87" stroke="#FF8AD8" stroke-width="2" stroke-linecap="round" opacity=".7"/><path d="M110 92 L118 83" stroke="#5DF2FF" stroke-width="2" stroke-linecap="round" opacity=".7"/>
    <ellipse cx="101" cy="109" rx="9.5" ry="11.5" fill="#2A2D42"/><ellipse cx="98" cy="104" rx="3" ry="4" fill="#5A5E78"/><path d="M94 122 Q101 127 108 122" stroke="#2A2D42" stroke-width="2.4" fill="none" stroke-linecap="round"/>
    ${MU(101, 82, 2.1, -16)}`),

  surf: (u) => SV(`<defs>${ML(u, 'h', [[0, '#4FC3F0'], [1, '#D6F3FC']])}${ML(u, 'w', [[0, '#2FA4E7'], [1, '#0A5A9E']])}${MR(u, 'so', [[0, '#FFF6C8'], [.7, '#FFD23F'], [1, '#FFD23F', 0]])}</defs>
    <rect width="200" height="200" fill="url(#${u}h)"/><circle cx="162" cy="38" r="34" fill="url(#${u}so)"/><circle cx="162" cy="38" r="15" fill="#FFE27A"/>
    <g fill="#fff"><path d="M18 52 C18 44 28 42 32 46 C36 38 50 40 50 50 C56 50 58 58 52 60 H20 C14 60 14 52 18 52Z"/></g><path d="M20 60 H52 C56 58 56 56 54 55 C46 58 30 58 18 56Z" fill="#BFE6F6"/>
    <rect y="112" width="200" height="88" fill="#1E8FD6"/><path d="M0 122 Q30 118 60 122 T120 122 T200 120" stroke="#7FD3F7" stroke-width="2" fill="none" opacity=".8"/>
    <path d="M-10 200 L-10 92 C8 60 64 50 92 78 C106 92 104 112 88 118 C76 122 68 112 74 104 C60 100 48 114 52 130 C58 152 92 162 124 152 L210 152 V200Z" fill="url(#${u}w)"/>
    <path d="M-10 110 C10 80 50 70 76 84 C60 82 40 90 30 104 C20 120 26 150 50 166 C20 160 0 140 -10 110Z" fill="#7FD3F7" opacity=".55"/>
    <path d="M-6 96 C14 66 62 58 88 80 C98 90 98 106 88 112" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M-6 96 C14 66 62 58 88 80" stroke="#CFEFFB" stroke-width="2" fill="none" transform="translate(2 5)"/>
    ${PK([[94, 74, 2.4], [100, 84, 1.8], [84, 66, 1.6], [104, 96, 1.4], [70, 60, 1.4]], '#fff', .95)}
    <path d="M0 176 Q40 168 80 176 T160 176 T220 172 V200 H0Z" fill="#0A5A9E"/><path d="M0 176 Q40 168 80 176 T160 176" stroke="#7FD3F7" stroke-width="2" fill="none" opacity=".6"/>
    <g transform="rotate(-10 130 148)"><path d="M70 150 C100 138 164 132 192 142 C164 154 104 160 70 150Z" fill="#E5243B"/><path d="M70 150 C104 160 164 154 192 142 C160 150 110 154 74 152Z" fill="#B3122B"/><path d="M84 147 C110 141 156 138 180 142" stroke="#fff" stroke-width="3" fill="none"/>
      ${PAKET(96, 118, 28, 26, '#FFC94A', '#E0A40E', '#E5243B')}${PAKET(126, 108, 32, 36, '#3DDC84', '#1F9A5E', '#7B1E6E')}${PAKET(110, 90, 22, 20, '#E5243B', '#B3122B', '#FFC94A')}${MU(121, 96, 1, 8)}</g>
    ${PK([[190, 150, 2], [196, 140, 1.4], [184, 160, 1.6]], '#fff', .9)}`),

  neonbaum: (u) => { const neon = (d, c, w = 4.2) => `<path d="${d}" stroke="${c}" stroke-width="${w * 3}" opacity=".18" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="${d}" stroke="${c}" stroke-width="${w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="${d}" stroke="#fff" stroke-width="${w * .32}" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity=".85"/>`;
    return SV(`<defs>${MR(u, 'g', [[0, '#3DFFB0', .28], [1, '#3DFFB0', 0]], .5, .55, .55)}</defs><rect width="200" height="200" fill="#170C30"/>
    <g fill="none" stroke="#24164A" stroke-width="2">${Array.from({ length: 11 }, (_, r) => `<path d="M0 ${r * 18 + 9} H200"/>${Array.from({ length: 6 }, (_, c) => `<path d="M${c * 40 + (r % 2) * 20} ${r * 18 + 9} V${r * 18 + 27}"/>`).join('')}`).join('')}</g>
    <rect width="200" height="200" fill="url(#${u}g)"/><ellipse cx="100" cy="190" rx="70" ry="8" fill="#3DFFB0" opacity=".12"/>
    <path d="M100 184 C120 188 150 182 168 192 L210 196" stroke="#2A1B5E" stroke-width="3.4" fill="none"/><rect x="176" y="188" width="10" height="7" rx="1.5" fill="#3A2E66" transform="rotate(6 181 191)"/>
    ${neon('M100 44 L70 90 H86 L58 132 H78 L48 168 H152 L122 132 H142 L114 90 H130 Z', '#3DFFB0')}${neon('M92 168 V182 H108 V168', '#FF9A3C', 3.4)}
    ${neon('M100 18 L104.5 29.5 L116.6 30.2 L107.2 38 L110.3 49.8 L100 43 L89.7 49.8 L92.8 38 L83.4 30.2 L95.5 29.5 Z', '#FFD23F', 3.4)}
    ${neon('M76 120 Q100 130 128 112', '#FF4FA3', 2.8)}${neon('M64 156 Q100 168 140 148', '#2DE2F0', 2.8)}
    ${[[88, 82, '#FF4FA3'], [114, 102, '#2DE2F0'], [82, 142, '#FFD23F'], [122, 140, '#C77DFF'], [100, 124, '#FFD23F']].map(([x, y, c]) => `<circle cx="${x}" cy="${y}" r="9" fill="${c}" opacity=".2"/><circle cx="${x}" cy="${y}" r="4.2" fill="${c}"/><circle cx="${x - 1.2}" cy="${y - 1.2}" r="1.4" fill="#fff"/>`).join('')}
    ${[[70, 90], [130, 90], [48, 168], [152, 168]].map(([x, y]) => `<rect x="${x - 3}" y="${y - 2}" width="6" height="4" rx="1" fill="#5A5A78"/>`).join('')}${PK([[22, 26], [176, 30], [160, 74, 1], [30, 110, 1], [184, 122]], '#fff', .4)}`); },

  pinguin: (u) => SV(`<defs>${ML(u, 'h', [[0, '#0E1A55'], [1, '#2A4BB0']])}</defs><rect width="200" height="200" fill="url(#${u}h)"/>${PK([[20, 22], [60, 14, 1], [154, 20], [186, 50, 1], [36, 64, 1], [120, 36, 1]], '#fff', .8)}
    <path d="M118 140 L140 92 L156 104 L172 80 L200 128 V150 H118Z" fill="#BFE3F7"/><path d="M156 104 L172 80 L200 128 V150 H170Z" fill="#8FC3E6"/><path d="M140 92 L146 100 L141 104Z" fill="#fff"/>
    <path d="M0 160 Q50 146 100 156 T200 150 V200 H0Z" fill="#EEF6FC"/><path d="M0 160 Q50 146 100 156 T200 150" stroke="#fff" stroke-width="3" fill="none"/><path d="M120 176 Q160 168 200 172 V200 H110Z" fill="#CFE2F0"/>
    <ellipse cx="100" cy="164" rx="40" ry="6" fill="#8FB4D6" opacity=".6"/>
    <path d="M58 118 C52 132 54 146 62 150 C66 138 66 126 64 116Z" fill="#141A2E"/><path d="M142 118 C148 132 146 146 138 150 C134 138 134 126 136 116Z" fill="#141A2E"/>
    <ellipse cx="100" cy="116" rx="40" ry="50" fill="#1F2640"/><path d="M128 82 C146 110 138 152 108 164 C130 146 136 112 128 82Z" fill="#141A2E"/>
    <ellipse cx="100" cy="128" rx="27" ry="34" fill="#FFF6E2"/><path d="M118 104 C128 124 124 150 104 160 C118 146 122 124 118 104Z" fill="#E6DCC4"/>
    <path d="M84 158 C76 162 74 168 82 168 H92 C94 164 92 160 84 158Z M116 158 C124 162 126 168 118 168 H108 C106 164 108 160 116 158Z" fill="#FF9A3C"/>
    <ellipse cx="88" cy="94" rx="8.5" ry="7.5" fill="#FFF6E2"/><ellipse cx="112" cy="94" rx="8.5" ry="7.5" fill="#FFF6E2"/><path d="M83 95 Q88 99 93 95 M107 95 Q112 99 117 95" stroke="#1B0C3A" stroke-width="2.4" fill="none" stroke-linecap="round"/>
    <path d="M93 104 Q100 100 107 104 L100 114Z" fill="#FF9A3C"/><path d="M100 114 L107 104 Q104 103 102 103Z" fill="#E0742A"/><circle cx="80" cy="106" r="4" fill="#FF8AA5" opacity=".5"/><circle cx="120" cy="106" r="4" fill="#FF8AA5" opacity=".5"/>
    <path d="M70 128 Q100 138 130 128 L132 138 Q100 148 68 138Z" fill="#E5243B"/><path d="M76 131 l4 10 M90 134 l2 10 M106 134 l-1 10 M120 131 l-3 10" stroke="#fff" stroke-width="2.4"/><path d="M114 140 L122 166 L130 162 L124 138Z" fill="#B3122B"/><path d="M118 152 h8 M120 160 h7" stroke="#fff" stroke-width="2"/>
    <path d="M64 104 C62 62 138 62 136 104" stroke="#1E2B5E" stroke-width="8" fill="none"/><path d="M64 104 C62 62 138 62 136 104" stroke="#2DE2F0" stroke-width="5" fill="none"/><path d="M70 86 C74 70 90 64 104 64" stroke="#B5F7FF" stroke-width="1.6" fill="none" stroke-linecap="round"/>
    <rect x="54" y="92" width="18" height="28" rx="8" fill="#FF4FA3"/><rect x="64" y="94" width="8" height="24" rx="4" fill="#C8287A"/><rect x="128" y="92" width="18" height="28" rx="8" fill="#C8287A"/><rect x="128" y="94" width="8" height="24" rx="4" fill="#FF4FA3"/><path d="M57 96 v8" stroke="#FFB3D9" stroke-width="2" stroke-linecap="round"/>
    <g fill="#FFD23F"><path d="M152 66 v-16 l12 -3 v14" stroke="#FFD23F" stroke-width="2.4" fill="none"/><ellipse cx="149" cy="67" rx="4.4" ry="3.4"/><ellipse cx="161" cy="64" rx="4.4" ry="3.4"/><path d="M34 84 v-14 l8 -2" stroke="#FFD23F" stroke-width="2.2" fill="none"/><ellipse cx="31" cy="85" rx="3.8" ry="3"/></g>`),

  polarlicht: (u) => SV(`<defs>${ML(u, 'h', [[0, '#050A2A'], [1, '#14246B']])}${ML(u, 'a', [[0, '#3DFFB0', 0], [.45, '#3DFFB0', .9], [1, '#A78BFA', 0]])}${ML(u, 'b', [[0, '#2DE2F0', 0], [.5, '#2DE2F0', .6], [1, '#F472B6', 0]])}<filter id="${u}bl" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>${MR(u, 'fe', [[0, '#FFE27A', .9], [1, '#FFE27A', 0]])}</defs>
    <rect width="200" height="200" fill="url(#${u}h)"/>${PK([[14, 16], [44, 30, 1], [82, 10, 1], [124, 22], [164, 12, 1], [190, 34], [60, 60, .9], [150, 64, .9]], '#fff', .8)}
    <g filter="url(#${u}bl)"><path d="M-10 70 C30 30 70 90 110 50 S180 40 210 60 L210 104 C170 84 140 110 100 92 S20 96 -10 110Z" fill="url(#${u}a)"/><path d="M-10 46 C40 70 80 20 130 44 S190 40 210 30 L210 60 C160 74 120 50 80 70 S10 60 -10 76Z" fill="url(#${u}b)"/></g>
    <g opacity=".35">${Array.from({ length: 24 }, (_, i) => `<rect x="${i * 8.6}" y="${40 + (i % 3) * 6}" width="1.6" height="${30 + (i * 7) % 22}" fill="${i % 2 ? '#3DFFB0' : '#A78BFA'}"/>`).join('')}</g>
    <path d="M-4 150 L40 102 L62 124 L96 82 L134 132 L156 112 L204 156 V200 H-4Z" fill="#1C2A6B"/><path d="M96 82 L134 132 L118 132 L100 104Z M40 102 L62 124 L50 124Z M156 112 L204 156 L184 156Z" fill="#141F52"/>
    <path d="M96 82 L106 96 L99 94 L92 100 L88 92Z M40 102 L48 112 L42 111 L36 116 L34 108Z M156 112 L163 120 L157 119 L152 122Z" fill="#E8F1FF"/><path d="M96 82 L106 96 L99 94Z" fill="#B8CCF0"/>
    <path d="M0 168 Q100 150 200 170 V200 H0Z" fill="#DDE8F7"/><path d="M0 168 Q100 150 200 170" stroke="#fff" stroke-width="2.4" fill="none"/><path d="M110 186 Q160 176 200 180 V200 H100Z" fill="#BDD0EA"/>
    ${[[22, 172, 1], [40, 168, .8], [176, 174, 1.1], [190, 178, .8]].map(([x, y, k]) => `<g transform="translate(${x} ${y}) scale(${k})"><path d="M0 -30 L9 -14 H4 L12 0 H-12 L-4 -14 H-9Z" fill="#0A1240"/><path d="M0 -30 L9 -14 H4 L12 0 H0Z" fill="#060B2E"/></g>`).join('')}
    <g transform="translate(112 146)"><rect x="0" y="0" width="34" height="22" fill="#5A2E18"/><rect x="22" y="0" width="12" height="22" fill="#40200F"/><path d="M-5 2 L17 -16 L39 2Z" fill="#3A1D10"/><path d="M-6 2 L17 -17 L40 2 L36 4 L17 -12 L-2 4Z" fill="#fff"/>
      <circle cx="11" cy="11" r="14" fill="url(#${u}fe)"/><rect x="6" y="6" width="10" height="9" rx="1" fill="#FFD23F"/><path d="M11 6 V15 M6 10.5 H16" stroke="#C98A0A" stroke-width="1.2"/><rect x="26" y="-14" width="5" height="10" fill="#40200F"/><path d="M28 -16 C24 -24 34 -26 30 -34 C28 -38 34 -40 32 -46" stroke="#C9D6EA" stroke-width="2.4" fill="none" opacity=".55" stroke-linecap="round"/></g>`),

  flieger: (u) => SV(`<defs>${ML(u, 'h', [[0, '#1B0C3A'], [.55, '#7B1E6E'], [.85, '#F0522B'], [1, '#FF9A3C']], .4, 1)}</defs><rect width="200" height="200" fill="url(#${u}h)"/>${PK([[16, 18], [60, 30, 1], [110, 14, 1], [170, 26], [30, 70, 1]], '#FFF3C4', .7)}
    ${[[26, 150, 1.2], [150, 168, 1], [130, 118, .6]].map(([x, y, k]) => `<g transform="translate(${x} ${y}) scale(${k})"><path d="M0 0 C0 -10 12 -14 18 -8 C22 -18 40 -18 42 -4 C50 -6 54 2 50 6 H2 C-4 6 -4 0 0 0Z" fill="#F7A6C0"/><path d="M2 6 H50 C53 4 53 2 52 1 C40 6 16 6 -1 3Z" fill="#D4799A"/></g>`).join('')}
    <path d="M100 86 C80 120 50 140 -4 150" stroke="#2A1B5E" stroke-width="1.6" fill="none"/>${LICHTER([[88, 104], [76, 117], [62, 128], [46, 137], [30, 143], [12, 147]], undefined, 3.4)}
    <g transform="translate(60 150)"><path d="M0 -18 V0" stroke="#2A1B5E" stroke-width="1.2"/>${PAKET(-9, 0, 18, 16, '#3DDC84', '#1F9A5E', '#FFC94A')}</g>
    <g transform="translate(66 100) rotate(-24)"><path d="M74 2 L58 30 L68 30 L96 4Z" fill="#D9DEEB"/><path d="M76 -4 L64 -26 L72 -26 L92 -4Z" fill="#C9CFE0"/>
      <path d="M40 0 C40 -6 48 -9 60 -9 H112 C124 -9 132 -4 134 0 C132 4 124 8 112 8 H52 C44 8 40 5 40 0Z" fill="#fff"/><path d="M42 4 C46 8 50 8 52 8 H112 C124 8 132 4 134 0 C128 3 120 4 112 4 H52 C48 4 44 4 42 4Z" fill="#C9CFE0"/>
      <path d="M44 -6 L36 -24 L46 -24 L60 -9Z" fill="#FFD23F"/><path d="M44 -6 L36 -24 L40 -24 L52 -9Z" fill="#E0A40E"/><path d="M122 -6 C126 -6 130 -3 131 -1 H120Z" fill="#2A1B5E"/>
      ${[66, 76, 86, 96, 106].map((x) => `<circle cx="${x}" cy="-2" r="2" fill="#2A4BB0"/>`).join('')}<path d="M60 -6 H112" stroke="#fff" stroke-width="1.4" opacity=".9"/></g>`),

  kaenguru: (u) => SV(`<defs>${ML(u, 'h', [[0, '#5A1A6E'], [.55, '#F0522B'], [1, '#FFC46B']])}${ML(u, 'so', [[0, '#FFE27A'], [1, '#FF9A3C']])}</defs><rect width="200" height="200" fill="url(#${u}h)"/>
    <g><circle cx="148" cy="122" r="42" fill="url(#${u}so)"/>${[104, 114, 124, 134, 144].map((y, i) => `<rect x="100" y="${y + i * 1.5}" width="100" height="${1.6 + i * .9}" fill="#F0522B" opacity=".9"/>`).join('')}</g>
    <path d="M110 150 L120 132 H168 L176 150Z" fill="#A8432A"/><path d="M150 132 H168 L176 150 H156Z" fill="#8A3420"/>
    <rect y="150" width="200" height="50" fill="#C2532E"/><path d="M0 168 Q100 160 200 170 V200 H0Z" fill="#9A3A1F"/>${[[24, 156], [60, 172], [176, 160], [150, 182]].map(([x, y]) => `<path d="M${x - 8} ${y} q4 -10 8 0 q2 -12 6 0 q4 -8 6 0Z" fill="#8A9A3A"/>`).join('')}
    <ellipse cx="96" cy="166" rx="40" ry="5" fill="#6B2A14" opacity=".55"/>
    <path d="M54 92 h-22 M50 104 h-28 M56 116 h-18" stroke="#FFE7C2" stroke-width="2.4" stroke-linecap="round" opacity=".6"/>
    <path d="M74 126 C54 132 30 142 12 152 C34 148 56 144 80 138Z" fill="#B86A3C"/><path d="M12 152 C34 148 56 144 80 138 L78 134 C58 140 34 146 12 152Z" fill="#8A4A26"/>
    <path d="M74 140 C62 120 68 94 88 84 C102 78 118 82 124 94 C130 108 126 124 118 134 C110 144 90 150 74 140Z" fill="#B86A3C"/><path d="M120 94 C130 108 126 124 118 134 C110 144 92 148 80 144 C100 142 116 130 120 94Z" fill="#8A4A26"/>
    <path d="M96 100 C104 98 112 104 112 116 C112 128 104 136 94 134 C100 124 100 110 96 100Z" fill="#E8B98A"/>
    <ellipse cx="84" cy="134" rx="20" ry="14" fill="#A85E32" transform="rotate(-24 84 134)"/><path d="M74 144 C66 150 56 156 42 158 C40 160 44 163 50 163 C64 161 78 156 88 148Z" fill="#8A4A26"/>
    ${PAKET(96, 104, 18, 15, '#3DDC84', '#1F9A5E', '#FFC94A')}<path d="M92 118 Q104 124 116 116" stroke="#8A4A26" stroke-width="2.4" fill="none" stroke-linecap="round"/>
    <path d="M116 108 C122 112 128 114 134 110" stroke="#A85E32" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path d="M114 88 C112 76 120 66 132 66 C142 66 150 72 152 78 C154 82 150 86 144 86 C136 86 130 90 126 96Z" fill="#B86A3C"/><path d="M126 96 C130 90 136 86 144 86 C150 86 154 82 152 78 C150 84 140 82 132 86 C128 88 126 92 126 96Z" fill="#8A4A26"/>
    <path d="M118 72 C112 58 114 48 120 44 C124 52 126 62 126 70Z" fill="#A85E32"/><path d="M124 70 C122 56 126 46 132 42 C134 50 134 62 130 70Z" fill="#B86A3C"/><path d="M127 66 C126 56 128 50 131 47" stroke="#E8B98A" stroke-width="2" fill="none" stroke-linecap="round"/>
    <circle cx="152" cy="79" r="2.4" fill="#1B0C3A"/>${AUGE(136, 74, 2.6)}${MU(130, 72, 1.15, 18)}`),

  sandmann: (u) => SV(`<defs>${ML(u, 'h', [[0, '#5CC8F2'], [1, '#E6F7FC']])}${MR(u, 'sa', [[0, '#F6D896'], [1, '#E2B866']], .4, .35, .7)}</defs><rect width="200" height="200" fill="url(#${u}h)"/>
    <rect y="108" width="200" height="22" fill="#2FA4E7"/><path d="M0 112 H200" stroke="#9EE0FA" stroke-width="2"/><path d="M0 124 Q50 118 100 124 T200 122 V132 H0Z" fill="#fff" opacity=".8"/>
    <path d="M0 128 Q60 120 120 128 T200 126 V200 H0Z" fill="#F3D48A"/><path d="M110 168 Q160 158 200 164 V200 H100Z" fill="#D9AE5C"/>${PK([[20, 150, 1], [44, 170, 1], [150, 150, 1], [176, 186, 1], [70, 190, 1]], '#C99A4E', .6)}
    <g transform="translate(-6 -6)">${[[-10, 30, 0], [-4, 20, 30], [4, 14, 60], [-14, 44, -24]].map(([x, y, r]) => `<path d="M0 0 C20 -6 40 -2 56 8 C40 6 20 6 0 0Z" fill="#1F8A55" transform="translate(${x} ${y}) rotate(${r})"/>`).join('')}</g>
    <ellipse cx="100" cy="186" rx="44" ry="6" fill="#C99A4E" opacity=".6"/>
    <circle cx="100" cy="158" r="34" fill="url(#${u}sa)"/><path d="M124 134 C140 154 132 184 104 190 C124 176 130 156 124 134Z" fill="#C99A4E"/>
    <circle cx="100" cy="112" r="24" fill="url(#${u}sa)"/><path d="M117 96 C128 110 122 132 102 136 C116 126 120 112 117 96Z" fill="#C99A4E"/>
    <circle cx="100" cy="76" r="18" fill="url(#${u}sa)"/><path d="M113 64 C120 76 116 92 100 94 C110 86 114 76 113 64Z" fill="#C99A4E"/>${PK([[88, 150, 1], [110, 168, 1], [94, 174, 1], [86, 118, .9], [108, 104, .9], [92, 70, .8]], '#B88A40', .7)}
    <path d="M78 104 L56 92 M60 95 L54 88 M122 106 L146 92 M140 96 L146 102" stroke="#7A5A3A" stroke-width="3" stroke-linecap="round"/>
    <path d="M86 72 Q86 68 90 68 H97 Q99 68 99 72 L98 77 Q97 80 93 80 H90 Q86 80 86 76Z M101 72 Q101 68 103 68 H110 Q114 68 114 72 L114 76 Q113 80 110 80 H106 Q102 80 102 77Z" fill="#1B0C3A"/><path d="M89 76 L94 70" stroke="#5DF2FF" stroke-width="1.4" opacity=".8"/>
    <path d="M100 82 l7 3 -7 2Z" fill="#FF8AA5"/><path d="M93 89 Q100 93 107 89" stroke="#7A5A3A" stroke-width="2" fill="none" stroke-linecap="round"/>
    ${[[100, 108], [100, 120], [100, 150]].map(([x, y]) => `<path d="M${x - 4} ${y + 3} Q${x} ${y - 5} ${x + 4} ${y + 3}Z" fill="#FFE2D6"/><path d="M${x - 2} ${y + 3} L${x} ${y - 2} L${x + 2} ${y + 3}" stroke="#E8A898" stroke-width=".8" fill="none"/>`).join('')}
    <g transform="rotate(-12 100 56)"><path d="M84 58 L88 38 H112 L116 58Z" fill="#E5243B"/><path d="M104 38 H112 L116 58 H106Z" fill="#B3122B"/><rect x="82" y="56" width="36" height="5" rx="2.5" fill="#C8172F"/><path d="M88 40 C88 28 112 28 112 40" stroke="#FFC94A" stroke-width="1.8" fill="none"/><path d="M89 44 V54" stroke="#FF8A95" stroke-width="2" stroke-linecap="round"/></g>
    <g transform="translate(160 162) rotate(14)"><path d="M0 -14 L3 -4 L14 -4 L5 2 L8 12 L0 6 L-8 12 L-5 2 L-14 -4 L-3 -4Z" fill="#FF7A59"/><path d="M0 -14 L3 -4 L14 -4 L5 2 L8 12 L0 6Z" fill="#E0553A"/></g>
    <g transform="translate(30 176) rotate(-18)"><rect x="-2" y="-28" width="4" height="26" fill="#3DDC84"/><path d="M-8 -2 H8 L6 12 H-6Z" fill="#3DDC84"/><path d="M2 -2 H8 L6 12 H2Z" fill="#1F9A5E"/></g>`),

  erdkugel: (u) => SV(`<defs>${MR(u, 'h', [[0, '#3B1D5E'], [1, '#14082A']], .5, .55, .7)}<clipPath id="${u}c"><circle cx="100" cy="118" r="52"/></clipPath>${ML(u, 'kap', [[0, '#FFF1A8'], [.5, '#FFD23F'], [1, '#B57A06']], 1, 0)}</defs><rect width="200" height="200" fill="url(#${u}h)"/>
    ${[[30, 150, 16, '#FFD23F'], [170, 60, 12, '#2DE2F0'], [168, 168, 20, '#FF4FA3'], [24, 60, 10, '#FFD23F']].map(([x, y, r, c]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${c}" opacity=".14"/>`).join('')}
    <path d="M-10 22 C40 10 120 14 210 30" stroke="#0F5E39" stroke-width="7" fill="none"/>${Array.from({ length: 26 }, (_, i) => { const x = i * 8.4 - 4, y = 20 + Math.sin(i / 3) * 2 + (i * 8.4 > 100 ? (i * 8.4 - 100) * .1 : 0); return `<path d="M${x} ${y} l${-4 + (i % 3)} ${10 + (i % 4)} M${x + 3} ${y} l${3 - (i % 2)} ${11 - (i % 3)}" stroke="${i % 2 ? '#1F8A55' : '#2FA36A'}" stroke-width="2.2" stroke-linecap="round"/>`; }).join('')}
    <path d="M100 26 V56" stroke="#FFD23F" stroke-width="1.4"/><path d="M100 50 C92 50 92 42 100 42 C108 42 108 50 100 50" stroke="#FFD23F" stroke-width="2" fill="none"/>
    <circle cx="100" cy="118" r="52" fill="#2FA4E7"/><g clip-path="url(#${u}c)"><path d="M54 88 C64 76 82 74 90 84 C98 94 86 104 76 104 C70 112 60 114 52 106Z M104 74 C116 70 132 76 140 88 C144 96 136 100 128 98 C122 104 112 100 110 92 C102 90 98 80 104 74Z M80 128 C92 120 110 124 116 136 C120 150 110 164 96 166 C88 160 90 148 82 142 C76 138 74 132 80 128Z M134 120 C142 118 150 124 150 132 C146 138 136 136 134 128Z" fill="#3DDC84"/>
      <path d="M100 66 A52 52 0 0 1 100 170 A44 52 0 0 0 100 66Z" fill="#0A3F7A" opacity=".45"/><path d="M60 100 C64 84 76 74 92 70" stroke="#fff" stroke-width="5" fill="none" opacity=".35" stroke-linecap="round"/></g>
    <rect x="76" y="76" width="12" height="18" rx="4" fill="#fff" opacity=".28" transform="rotate(-28 82 85)"/>
    <rect x="86" y="54" width="28" height="14" rx="3" fill="url(#${u}kap)"/><path d="M92 55 V67 M100 55 V67 M108 55 V67" stroke="#B57A06" stroke-width="1.4"/><path d="M88 66 H112" stroke="#8A5A00" stroke-width="1.6"/>
    <ellipse cx="100" cy="118" rx="76" ry="22" fill="none" stroke="#FFF3C4" stroke-width="1.4" stroke-dasharray="2 5" transform="rotate(-14 100 118)" opacity=".8"/>
    <g transform="translate(166 98) rotate(-30)"><path d="M-8 0 H8 C10 0 10 2 8 2 H-8Z M0 0 L-4 -6 H-1 L4 0Z M0 2 L-4 8 H-1 L4 2Z M-8 0 L-10 -3 H-8 L-6 0Z" fill="#fff"/></g>${FU(34, 104, 6)}${FU(160, 158, 5)}${FU(150, 36, 4, '#FFF3C4', .8)}`),

  rentier: (u) => SV(`<defs>${ML(u, 'h', [[0, '#1B0C3A'], [.6, '#5A1A6E'], [1, '#C2185B']])}${ML(u, 'vr', [[0, '#2DE2F0'], [1, '#A78BFA']], 1, 1)}</defs><rect width="200" height="200" fill="url(#${u}h)"/>
    <g><circle cx="100" cy="132" r="54" fill="#FF9A3C" opacity=".85"/>${[124, 136, 148, 160, 172].map((y, i) => `<rect x="40" y="${y}" width="120" height="${2 + i}" fill="#7B1E6E"/>`).join('')}</g>
    <rect y="160" width="200" height="40" fill="#1B0C3A"/><g stroke="#FF4FA3" stroke-width="1.2" opacity=".7">${[-60, -20, 20, 60, 100, 140, 180, 220, 260].map((x) => `<path d="M100 160 L${x} 200"/>`).join('')}${[166, 174, 186].map((y) => `<path d="M0 ${y} H200"/>`).join('')}</g>
    <g stroke-linecap="round" fill="none"><path d="M82 66 C70 50 66 34 72 20 M76 44 L58 38 M72 30 L60 20 M118 66 C130 50 134 34 128 20 M124 44 L142 38 M128 30 L140 20" stroke="#B8996E" stroke-width="7"/><path d="M82 66 C70 50 66 34 72 20 M76 44 L58 38 M72 30 L60 20 M118 66 C130 50 134 34 128 20 M124 44 L142 38 M128 30 L140 20" stroke="#E8D7B2" stroke-width="4"/></g>
    ${LICHTER([[66, 30], [74, 48], [62, 38], [132, 30], [126, 48], [138, 38]], ['#FFC94A', '#3DDC84', '#FF5A5F'], 2.2)}
    <path d="M64 82 C48 76 40 82 44 90 C52 94 60 92 70 88Z" fill="#A0643A"/><path d="M136 82 C152 76 160 82 156 90 C148 94 140 92 130 88Z" fill="#7A4A28"/><path d="M50 86 C56 84 62 86 66 87" stroke="#E8A88A" stroke-width="3" stroke-linecap="round"/>
    <path d="M70 92 C70 70 84 58 100 58 C116 58 130 70 130 92 C130 114 124 134 114 146 C108 152 92 152 86 146 C76 134 70 114 70 92Z" fill="#A0643A"/><path d="M120 66 C130 78 132 102 124 128 C118 144 108 150 98 150 C112 138 122 110 120 66Z" fill="#7A4A28"/>
    <ellipse cx="100" cy="136" rx="17" ry="13" fill="#E8C49A"/><ellipse cx="100" cy="128" rx="9" ry="5.6" fill="#2A1810"/><ellipse cx="97" cy="126.4" rx="3" ry="1.6" fill="#6A4A3A"/><path d="M93 141 Q100 146 107 141" stroke="#5A3020" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M64 90 Q64 82 72 82 H128 Q136 82 136 90 V104 Q136 114 126 114 H110 L104 108 H96 L90 114 H74 Q64 114 64 104Z" fill="#2A2D42"/><path d="M68 92 Q68 86 74 86 H126 Q132 86 132 92 V102 Q132 110 124 110 H111 L105 104 H95 L89 110 H76 Q68 110 68 102Z" fill="url(#${u}vr)"/>
    <path d="M76 104 L90 88 M86 106 L98 92 M116 104 L126 92" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".5"/>${FU(82, 96, 3, '#fff', .9)}${FU(118, 98, 2.4, '#fff', .9)}<path d="M64 96 H56 M136 96 H144" stroke="#2A2D42" stroke-width="5" stroke-linecap="round"/>
    <path d="M78 156 Q100 166 122 156 L126 168 Q100 180 74 168Z" fill="#E5243B"/><path d="M84 159 l3 11 M100 162 v11 M116 159 l-3 11" stroke="#fff" stroke-width="3"/>`),

  bordkarte: (u) => SV(`<defs>${ML(u, 'h', [[0, '#0E1A55'], [1, '#2A1B5E']])}</defs><rect width="200" height="200" fill="url(#${u}h)"/>${PK([[20, 20], [170, 16], [186, 70, 1], [16, 170, 1], [60, 186, 1], [150, 182]], '#fff', .6)}
    <path d="M10 160 C50 40 150 40 190 150" stroke="#FFF3C4" stroke-width="1.4" stroke-dasharray="2 6" fill="none" opacity=".6"/>${FU(100, 46, 5)}
    <g transform="rotate(-7 100 108)"><rect x="24" y="66" width="156" height="86" rx="10" fill="#000" opacity=".3" transform="translate(3 6)"/><rect x="24" y="66" width="156" height="86" rx="10" fill="#FFFBEF"/><rect x="132" y="66" width="48" height="86" rx="10" fill="#FFF4D6"/>
      <path d="M24 76 Q24 66 34 66 H170 Q180 66 180 76 V84 H24Z" fill="#FFD23F"/><text x="34" y="80" font-family="ui-monospace, Menlo, monospace" font-size="8.5" font-weight="800" letter-spacing="1.4" fill="#1B0C3A">BORDKARTE</text><text x="137" y="80" font-family="ui-monospace, Menlo, monospace" font-size="6.2" font-weight="800" letter-spacing=".6" fill="#7B1E6E">RENTIER</text>
      <path d="M132 86 V150" stroke="#1B0C3A" stroke-width="1.2" stroke-dasharray="1.5 3" opacity=".5"/>
      <g font-family="ui-monospace, Menlo, monospace" font-weight="800" fill="#7B1E6E" font-size="6.4" letter-spacing="1"><text x="34" y="98">VON</text><text x="94" y="98">NACH</text><text x="34" y="134">GATE</text><text x="64" y="134">SITZ</text><text x="94" y="134">BOARDING</text></g>
      <g font-family="Space Grotesk, system-ui, sans-serif" font-weight="700" fill="#1B0C3A"><text x="33" y="120" font-size="22">AUS</text><text x="93" y="120" font-size="22">NP</text><text x="34" y="146" font-size="11">N0</text><text x="64" y="146" font-size="11">24A</text><text x="94" y="146" font-size="11">JETZT</text></g>
      <path d="M72 110 H86 M82 106 L87 110 L82 114" stroke="#E5243B" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      <g fill="#1B0C3A">${[0, 2, 3, 5, 8, 9, 11, 14, 15, 17, 20].map((y, i) => `<rect x="${140 + (i % 3)}" y="${90 + y * 1.7}" width="${22 + (i % 4) * 3}" height="${i % 2 ? 1.2 : 2}"/>`).join('')}</g>
      <g transform="translate(156 136) rotate(-16)" opacity=".85"><circle r="14" fill="none" stroke="#E5243B" stroke-width="1.8"/><circle r="10.6" fill="none" stroke="#E5243B" stroke-width=".8"/><path d="${ST5(0, 0, 6)}" fill="#E5243B"/></g></g>`),

  controller: (u) => SV(`<defs>${ML(u, 'h', [[0, '#2A1B5E'], [1, '#4A1A6E']], 1, 1)}<mask id="${u}biss"><rect width="200" height="200" fill="#fff"/><circle cx="156" cy="78" r="14" fill="#000"/><circle cx="167" cy="94" r="11" fill="#000"/><circle cx="142" cy="69" r="9" fill="#000"/></mask></defs><rect width="200" height="200" fill="url(#${u}h)"/>
    <g opacity=".22" fill="#7B1E6E">${Array.from({ length: 7 }, (_, i) => `<path d="M${i * 34 - 40} 200 L${i * 34 + 10} 0 H${i * 34 + 26} L${i * 34 - 24} 200Z"/>`).join('')}</g>${FU(28, 30, 6)}${FU(176, 160, 5)}${FU(170, 30, 3.4)}
    <ellipse cx="100" cy="158" rx="62" ry="8" fill="#14082A" opacity=".6"/>
    <g mask="url(#${u}biss)"><path d="M42 96 C42 78 58 70 76 72 H124 C142 70 158 78 158 96 C162 120 168 140 158 152 C148 160 134 154 126 138 H74 C66 154 52 160 42 152 C32 140 38 120 42 96Z" fill="#C27A3E"/>
      <path d="M158 96 C162 120 168 140 158 152 C148 160 134 154 126 138 H74 C66 154 52 160 42 152 C48 154 58 150 66 134 H128 C136 148 148 152 154 146 C160 136 156 118 152 96Z" fill="#9A5A28"/><path d="M50 92 C52 82 62 78 74 78 H96" stroke="#E0A06A" stroke-width="4" fill="none" stroke-linecap="round"/>
      <path d="M50 98 C50 84 62 80 76 80 H124 C138 80 150 84 150 98 C154 118 158 134 152 144 C146 150 138 146 132 132 H68 C62 146 54 150 48 144 C42 134 46 118 50 98Z" fill="none" stroke="#FFF6E2" stroke-width="2.6" stroke-dasharray="5 3" stroke-linecap="round"/><g fill="none" stroke="#8A4A1E" stroke-width="5"><circle cx="156" cy="78" r="14"/><circle cx="167" cy="94" r="11"/><circle cx="142" cy="69" r="9"/></g></g>
    <g transform="translate(76 106)"><path d="M-5 -15 H5 V-5 H15 V5 H5 V15 H-5 V5 H-15 V-5 H-5Z" fill="#FFF6E2"/><path d="M-5 -15 H5 V-5 H15 V5 H5 V15 H-5 V5 H-15 V-5 H-5Z" fill="none" stroke="#E8D8BA" stroke-width="1.2" transform="translate(1 1)"/><circle r="4" fill="#E5243B"/><circle cx="-1.2" cy="-1.2" r="1.2" fill="#fff"/></g>
    ${[[124, 96, '#3DDC84'], [138, 108, '#E5243B'], [110, 108, '#2FA4E7'], [124, 120, '#FFC94A']].map(([x, y, c]) => `<circle cx="${x}" cy="${y}" r="6.4" fill="${c}"/><path d="M${x + 6.4} ${y}A6.4 6.4 0 0 1 ${x - 4.5} ${y + 4.5}A6.4 5 0 0 0 ${x + 6.4} ${y}Z" fill="#000" opacity=".2"/><circle cx="${x - 2}" cy="${y - 2.2}" r="1.8" fill="#fff" opacity=".85"/>`).join('')}
    <path d="M92 124 h6 M102 124 h6" stroke="#FFF6E2" stroke-width="3" stroke-linecap="round"/>${PK([[172, 118, 2.4], [178, 130, 1.6], [164, 128, 1.8], [182, 110, 1.4], [160, 140, 1.4]], '#C27A3E', 1)}`),

  strandfeuer: (u) => SV(`<defs>${ML(u, 'h', [[0, '#14082A'], [.55, '#3B1D5E'], [1, '#7B1E6E']])}${ML(u, 'sa', [[0, '#E9C27A'], [1, '#C99A4E']])}</defs><rect width="200" height="200" fill="url(#${u}h)"/>${PK([[20, 20], [56, 34, 1], [100, 14, 1], [150, 28], [186, 16, 1], [130, 52, .9]], '#fff', .75)}
    <circle cx="160" cy="40" r="12" fill="#FFF3C4"/><circle cx="166" cy="36" r="11" fill="#2A1450"/>
    <rect y="112" width="200" height="30" fill="#2A1B5E"/>${[[150, 118, 18], [154, 126, 12], [157, 134, 6]].map(([x, y, w]) => `<rect x="${x}" y="${y}" width="${w}" height="2" rx="1" fill="#FFF3C4" opacity=".6"/>`).join('')}<path d="M0 138 Q50 132 100 138 T200 136" stroke="#9EE0FA" stroke-width="1.6" fill="none" opacity=".5"/>
    <path d="M0 140 Q60 132 120 140 T200 138 V200 H0Z" fill="url(#${u}sa)"/><path d="M0 140 Q60 132 120 140 T200 138" stroke="#F6D896" stroke-width="2" fill="none"/>
    ${[[24, 150, -8, 1], [182, 150, 10, -1]].map(([x, y, r, m]) => `<g transform="translate(${x} ${y}) scale(${m} 1)"><path d="M0 0 C-2 -30 4 -60 14 -80" stroke="#6B4A2A" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M0 0 C-2 -30 4 -60 14 -80" stroke="#8A6A44" stroke-width="7" fill="none" stroke-dasharray="3 5"/>
      ${[[-30, 20], [-10, 34], [20, 40], [40, 26], [30, -6]].map(([dx, dy]) => `<path d="M14 -80 Q${14 + dx * .5} ${-80 - 12} ${14 + dx} ${-80 + dy * .4} Q${14 + dx * .5} ${-80 - 2} 14 -80Z" fill="#0F3D28"/>`).join('')}</g>`).join('')}
    <path d="M36 74 Q100 104 168 74" stroke="#14082A" stroke-width="1.4" fill="none"/>${LICHTER([[48, 79], [64, 86], [82, 90], [100, 91], [118, 90], [136, 86], [152, 79]], undefined, 3)}
    <g transform="translate(100 176) scale(1.45)">${[[0, -46, 2], [0, -36, 10], [0, -26, 16], [0, -16, 22], [0, -6, 28]].map(([x, y, w], i) => `<rect x="${-w}" y="${y}" width="${w * 2}" height="5" rx="2.5" fill="${i % 2 ? '#B8996E' : '#D9C09A'}" transform="rotate(${i % 2 ? 4 : -4})"/>`).join('')}<rect x="-2" y="-46" width="4" height="48" fill="#8A6A44"/>
      <path d="${ST5(0, -54, 7)}" fill="#FFD23F"/>${LICHTER([[-8, -40], [8, -32], [-14, -22], [12, -14], [-20, -6], [20, -4]], undefined, 2)}</g>
    ${PAKET(134, 164, 18, 14, '#E5243B', '#B3122B', '#FFC94A')}<g fill="#C99A4E" opacity=".8">${[[40, 186], [52, 178], [64, 190], [76, 182]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="3" ry="5" transform="rotate(-30 ${x} ${y})"/>`).join('')}</g>`),

  kompass: (u) => SV(`<defs>${MR(u, 'p', [[0, '#FBF1D8'], [1, '#D9C29A']], .5, .5, .75)}${ML(u, 'ring', [[0, '#FFF1A8'], [.5, '#FFC94A'], [1, '#9A6A08']], 1, 1)}</defs><rect width="200" height="200" fill="url(#${u}p)"/>
    <g stroke="#B8996E" stroke-width="1.2" fill="none" opacity=".55"><path d="M0 40 C40 30 60 60 100 50 S170 20 200 40"/><path d="M0 60 C40 50 60 80 100 70 S170 40 200 60"/><path d="M0 170 C40 160 70 190 110 176 S170 160 200 176"/></g>
    <path d="M20 184 C40 150 30 120 50 100" stroke="#E5243B" stroke-width="2" stroke-dasharray="3 4" fill="none"/><path d="M14 178 l10 10 M24 178 l-10 10" stroke="#E5243B" stroke-width="2.4" stroke-linecap="round"/>
    <g>${[0, 45, 90, 135].map((a) => `<path d="M100 8 L102 22 L100 26 L98 22Z" fill="#FFD23F" transform="rotate(${a} 100 22)" opacity=".7"/>`).join('')}<path d="${ST5(100, 22, 11)}" fill="#FFD23F"/><path d="${ST5H(100, 22, 11)}" fill="#E0A40E"/></g>
    <circle cx="103" cy="112" r="60" fill="#5A3A00" opacity=".25"/><circle cx="100" cy="108" r="60" fill="url(#${u}ring)"/><circle cx="100" cy="108" r="50" fill="#FFFBEF"/><circle cx="100" cy="108" r="50" fill="none" stroke="#9A6A08" stroke-width="1.4"/>
    <g stroke="#1B0C3A" stroke-width="1.4">${Array.from({ length: 24 }, (_, i) => `<path d="M100 ${i % 6 ? 62 : 60} V${i % 6 ? 66 : 70}" transform="rotate(${i * 15} 100 108)"/>`).join('')}</g>
    <g font-family="Space Grotesk, system-ui, sans-serif" font-weight="700" font-size="12" fill="#1B0C3A" text-anchor="middle"><text x="100" y="84">N</text><text x="100" y="142">S</text><text x="130" y="112">O</text><text x="70" y="112">W</text></g>
    <path d="M100 74 L109 108 L100 108Z" fill="#E5243B"/><path d="M100 74 L91 108 L100 108Z" fill="#FF5A6B"/><path d="M100 142 L109 108 H100Z" fill="#9AA3B5"/><path d="M100 142 L91 108 H100Z" fill="#DCE1EA"/>
    <circle cx="100" cy="108" r="5" fill="url(#${u}ring)"/><path d="M62 88 A44 44 0 0 1 96 64" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".7"/><circle cx="100" cy="44" r="6" fill="none" stroke="url(#${u}ring)" stroke-width="4"/>`),

  schneeflocke: (u) => { const px = new Set(); const add = (x, y) => px.add(x + ',' + y);
    for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { for (let k = 0; k <= 6; k++) add(dx * k, dy * k); for (const s of [1, -1]) { add(dx * 4 + dy * s, dy * 4 + dx * s); add(dx * 5 + dy * s * 2, dy * 5 + dx * s * 2); add(dx * 2 + dy * s, dy * 2 + dx * s); } }
    for (const [dx, dy] of [[1, 1], [1, -1], [-1, 1], [-1, -1]]) for (let k = 1; k <= 3; k++) add(dx * k, dy * k);
    const P2 = 9; const ox = 100 - P2 / 2, oy = 104 - P2 / 2;
    const zelle = (col, sx = 0, sy = 0) => [...px].map((s) => { const [x, y] = s.split(',').map(Number); return `<rect x="${ox + x * P2 + sx}" y="${oy + y * P2 + sy}" width="${P2}" height="${P2}" fill="${typeof col === 'function' ? col(x, y) : col}"/>`; }).join('');
    return SV(`<rect width="200" height="200" fill="#0E1A55"/><g shape-rendering="crispEdges"><g fill="#1B2A70">${Array.from({ length: 10 }, (_, i) => `<rect x="0" y="${i * 20}" width="200" height="10"/>`).join('')}</g>
    ${[[18, 22], [170, 18], [40, 170], [176, 160], [24, 96], [150, 40], [60, 40]].map(([x, y], i) => `<rect x="${x}" y="${y}" width="${i % 2 ? 4 : 6}" height="${i % 2 ? 4 : 6}" fill="${i % 3 ? '#fff' : '#FFD23F'}"/>`).join('')}
    <g opacity=".55">${zelle('#FF4FA3', -3, 0)}</g><g opacity=".55">${zelle('#2DE2F0', 3, 0)}</g>${zelle((x, y) => x + y < 0 ? '#FFFFFF' : x + y === 0 ? '#DDF0FB' : '#9FD0F0')}
    <rect x="${ox}" y="${oy}" width="${P2}" height="${P2}" fill="#FFD23F"/><rect x="${ox}" y="${oy}" width="4" height="4" fill="#FFF6C8"/>
    <rect x="12" y="176" width="64" height="12" fill="#1B0C3A"/><text x="16" y="185.4" font-family="ui-monospace, Menlo, monospace" font-size="8.6" font-weight="800" fill="#2DE2F0">LVL -24°C</text></g>`); },

  stern: (u) => SV(`<defs>${ML(u, 'h', [[0, '#0B1440'], [1, '#2A1B5E']])}${ML(u, 'sw', [[0, '#FFD23F', 0], [.7, '#FFD23F', .55], [1, '#FFF6C8', .95]], 1, 0, 0, 1)}${MR(u, 'ha', [[0, '#FFE27A', .6], [1, '#FFE27A', 0]])}</defs><rect width="200" height="200" fill="url(#${u}h)"/>${PK([[16, 24], [50, 60, 1], [90, 22, 1], [176, 90], [30, 110, 1], [160, 140, 1], [110, 60, .9]], '#fff', .8)}
    <path d="M-6 170 C40 140 90 100 132 70 L146 84 C100 112 50 150 -6 182Z" fill="url(#${u}sw)"/><path d="M10 168 C50 140 96 104 134 76" stroke="#FFF6C8" stroke-width="1.6" fill="none" opacity=".6"/>
    ${FU(60, 128, 5)}${FU(90, 106, 3.4)}${FU(34, 150, 3)}${FU(112, 96, 2.4)}
    <circle cx="146" cy="70" r="40" fill="url(#${u}ha)"/><path d="${ST5(146, 70, 26, .46, 12)}" fill="#FFD23F"/><path d="${ST5H(146, 70, 26, .46, 12)}" fill="#E0A40E"/><path d="M140 52 L146 46" stroke="#FFF6C8" stroke-width="3" stroke-linecap="round"/>
    <path d="M0 200 V168 H18 V156 L30 146 L42 156 V166 H58 V150 H74 V170 H92 V160 L104 150 L116 160 V172 H134 V158 H152 V174 H170 V162 L184 152 L198 162 V200Z" fill="#0A0F2E"/>
    <path d="M18 156 L30 146 L42 156 L40 158 L30 150 L20 158Z M92 160 L104 150 L116 160 L114 162 L104 154 L94 162Z M170 162 L184 152 L198 162 L196 164 L184 156 L172 164Z M58 150 H74 V153 H58Z M134 158 H152 V161 H134Z" fill="#E8F1FF"/>
    ${[[26, 162], [34, 162], [64, 158], [100, 164], [108, 164], [140, 166], [180, 168], [188, 168], [66, 176]].map(([x, y], i) => `<rect x="${x}" y="${y}" width="4" height="5" fill="${i % 3 ? '#FFD23F' : '#FF9A3C'}"/>`).join('')}`),

  krampus: (u) => SV(`<defs>${MR(u, 'h', [[0, '#6B1E26'], [1, '#1C0A0E']], .5, .45, .7)}${ML(u, 'horn', [[0, '#F6ECD6'], [1, '#B89B6A']], 1, 1)}</defs><rect width="200" height="200" fill="url(#${u}h)"/>${PK([[24, 26, 1.6], [176, 34, 1.4], [168, 170, 1.6], [20, 140, 1.2]], '#FF8A7A', .45)}
    <path d="M154 196 L178 64" stroke="#7A5228" stroke-width="7" stroke-linecap="round"/><path d="M155 196 L179 64" stroke="#A0703C" stroke-width="3" stroke-linecap="round"/><path d="M168 58 C174 40 190 40 196 50 L186 74 C180 70 172 66 166 66Z" fill="#D9B26F"/><path d="M178 46 L172 66 M186 48 L178 70 M192 52 L184 72" stroke="#B08A4A" stroke-width="1.6"/><path d="M186 74 L196 50 C198 54 196 64 190 76Z" fill="#B08A4A"/>
    <path d="M60 196 C56 166 70 150 100 150 C130 150 144 166 140 196Z" fill="#5A3A2A"/><path d="M120 152 C136 160 142 176 140 196 H118 C126 180 126 164 120 152Z" fill="#3E281C"/>
    <path d="M66 62 C52 46 50 28 60 16 C60 30 66 42 78 52Z" fill="url(#${u}horn)"/><path d="M134 62 C148 46 150 28 140 16 C140 30 134 42 122 52Z" fill="url(#${u}horn)"/><path d="M58 30 q5 0 8 3 M58 42 q5 -1 9 3 M142 30 q-5 0 -8 3 M142 42 q-5 -1 -9 3" stroke="#9C7E52" stroke-width="1.4" fill="none" stroke-linecap="round"/>
    <path d="M52 92 C40 88 34 76 38 70 C46 72 54 80 58 88Z M148 92 C160 88 166 76 162 70 C154 72 146 80 142 88Z" fill="#A8323A"/><path d="M148 92 C160 88 166 76 162 70 C160 78 154 84 146 88Z" fill="#7E1F28"/>
    <circle cx="100" cy="100" r="48" fill="#B83A42"/><path d="M134 66 C154 92 146 134 112 146 C136 128 144 98 134 66Z" fill="#8E2430"/><path d="M66 78 C70 66 82 58 96 56" stroke="#D85A62" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path d="M56 116 C60 140 80 156 100 156 C120 156 140 140 144 116 C138 126 132 122 128 132 C124 122 118 130 114 138 C110 128 104 136 100 142 C96 136 90 128 86 138 C82 130 76 122 72 132 C68 122 62 126 56 116Z" fill="#5A3A2A"/>
    <path d="M58 60 C66 50 76 54 80 60 C86 50 96 52 100 58 C104 52 114 50 120 60 C124 54 134 50 142 60 C136 50 120 42 100 44 C80 42 64 50 58 60Z" fill="#5A3A2A"/>
    <path d="M70 86 Q80 78 92 86" stroke="#2A0B0B" stroke-width="4.4" fill="none" stroke-linecap="round"/><path d="M108 84 Q120 74 132 82" stroke="#2A0B0B" stroke-width="4.4" fill="none" stroke-linecap="round"/>
    <ellipse cx="82" cy="98" rx="9" ry="10" fill="#FFF6E2"/>${AUGE(84, 99, 4.6)}<path d="M112 98 Q120 104 128 98" stroke="#2A0B0B" stroke-width="3.6" fill="none" stroke-linecap="round"/>
    <ellipse cx="100" cy="112" rx="8" ry="6" fill="#6E1F1F"/><ellipse cx="98" cy="110" rx="3" ry="2" fill="#A85050"/>
    <path d="M74 122 Q100 148 126 122 Q100 134 74 122Z" fill="#2A0B0B"/><path d="M82 125 L86 134 L90 127Z M112 127 L116 133 L119 125Z" fill="#FFF6E2"/><path d="M94 134 Q101 142 108 134 Q101 137 94 134Z" fill="#FF7A8A"/>
    <g transform="translate(16 132) rotate(-12)"><rect width="50" height="58" rx="5" fill="#FFFBEF"/><rect x="40" width="10" height="58" rx="5" fill="#EFE6CF"/><rect x="15" y="-5" width="20" height="10" rx="3" fill="#E5243B"/><g stroke="#3A2A55" stroke-width="2" stroke-linecap="round"><path d="M20 20 H40 M20 32 H36 M20 44 H40"/></g>
      ${[18, 30, 42].map((y, i) => `<rect x="7" y="${y - 4}" width="8" height="8" rx="1.5" fill="none" stroke="#3A2A55" stroke-width="1.6"/>${i === 0 ? `<path d="M8 ${y} l2.4 2.6 L15 ${y - 5}" stroke="#0E9F6E" stroke-width="2.2" fill="none" stroke-linecap="round"/>` : ''}`).join('')}</g>
    <ellipse cx="44" cy="164" rx="9" ry="7" fill="#B83A42"/><ellipse cx="150" cy="156" rx="9" ry="7" fill="#8E2430"/>`),

  nikolaus: (u) => SV(`<defs>${ML(u, 'h', [[0, '#0B1440'], [1, '#3B1D5E']])}${MR(u, 'mo', [[0, '#FFF6C8', .9], [1, '#FFF6C8', 0]])}${MR(u, 'or', [[0, '#FFC46B'], [1, '#F07A1A']], .35, .3, .8)}</defs><rect width="200" height="200" fill="url(#${u}h)"/>
    <circle cx="156" cy="38" r="30" fill="url(#${u}mo)"/><circle cx="156" cy="38" r="15" fill="#FFF6C8"/><circle cx="163" cy="33" r="13" fill="#152060"/>${PK([[22, 22], [60, 16, 1], [104, 30, 1], [36, 64, 1], [190, 80, 1], [120, 60, .9]], '#fff', .8)}${FU(84, 46, 4)}
    <path d="M0 156 H200 V200 H0Z" fill="#E8F1FF"/><path d="M0 156 Q30 148 60 154 T120 152 T200 154 V160 H0Z" fill="#fff"/><path d="M0 166 H200 V172 H0Z" fill="#BDD0EA"/><path d="M0 172 H200 V200 H0Z" fill="#5A3A2A"/><path d="M0 172 H200 V176 H0Z" fill="#3E281C"/>
    <ellipse cx="104" cy="158" rx="40" ry="5" fill="#8FA6C2" opacity=".6"/>
    <circle cx="80" cy="66" r="13" fill="url(#${u}or)"/><path d="M80 53 c2 -6 8 -6 10 -4 c-4 0 -6 2 -10 4Z" fill="#1F8A55"/><circle cx="76" cy="62" r="3" fill="#FFE2B0" opacity=".7"/>
    <g transform="rotate(-14 120 60)"><rect x="114" y="22" width="9" height="52" rx="4.5" fill="#fff"/><path d="M114 30 l9 -6 M114 42 l9 -6 M114 54 l9 -6 M114 66 l9 -6" stroke="#E5243B" stroke-width="3.6"/><path d="M114 26 C114 12 132 10 132 24 V30" stroke="#fff" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M118 16 l6 6 M126 14 l2 8" stroke="#E5243B" stroke-width="3.6"/></g>
    ${PAKET(92, 50, 22, 22, '#3DDC84', '#1F9A5E', '#FFC94A')}<circle cx="106" cy="76" r="9" fill="#FFD23F"/><circle cx="106" cy="76" r="6" fill="none" stroke="#C98A0A" stroke-width="1.2"/><path d="M102 72 q3 -2 6 -1" stroke="#FFF6C8" stroke-width="1.4" fill="none"/>
    <path d="M70 80 H128 V128 L156 136 C172 140 174 160 156 160 H70Z" fill="#E5243B"/><path d="M112 80 H128 V128 L156 136 C172 140 174 160 156 160 H112 C134 156 136 140 120 132 L112 128Z" fill="#B3122B"/><path d="M76 88 V150" stroke="#FF8A95" stroke-width="3" stroke-linecap="round" opacity=".8"/>
    <path d="M70 150 H160" stroke="#8E0E22" stroke-width="2" opacity=".5"/><rect x="64" y="74" width="70" height="16" rx="8" fill="#fff"/><path d="M68 86 H130" stroke="#D5DEEA" stroke-width="2.4" stroke-linecap="round"/>${PK([[72, 79, 1.6], [86, 78, 1.6], [102, 79, 1.6], [118, 78, 1.6]], '#E8EEF6', 1)}
    ${BAND(u, '6. DEZEMBER', 176)}`),

  heiligabend: (u) => SV(`<defs>${ML(u, 'h', [[0, '#0B1440'], [.55, '#2A1B5E'], [.82, '#7B1E6E'], [1, '#F0522B']])}${MR(u, 'ha', [[0, '#FFF6C8', .85], [1, '#FFE27A', 0]])}${ML(u, 'sa', [[0, '#E9C27A'], [1, '#C99A4E']])}</defs><rect width="200" height="200" fill="url(#${u}h)"/>
    ${PK([[16, 20], [44, 52, 1], [160, 22], [184, 58, 1], [130, 44, .9], [22, 90, 1]], '#fff', .8)}<circle cx="100" cy="34" r="34" fill="url(#${u}ha)"/>${[0, 90, 180, 270].map((a) => `<path d="M100 34 L102 34 L100 ${34 - 30} L98 34Z" transform="rotate(${a} 100 34)" fill="#FFF6C8" opacity=".85"/>`).join('')}<path d="${ST5(100, 34, 11)}" fill="#FFE27A"/><path d="${ST5H(100, 34, 11)}" fill="#F2B417"/>
    <rect y="118" width="200" height="26" fill="#3B1D5E"/>${[[92, 124, 16], [95, 131, 10], [97, 138, 6]].map(([x, y, w]) => `<rect x="${x}" y="${y}" width="${w}" height="2" rx="1" fill="#FFE27A" opacity=".7"/>`).join('')}
    <path d="M0 142 Q60 134 120 142 T200 140 V200 H0Z" fill="url(#${u}sa)"/><path d="M0 142 Q60 134 120 142 T200 140" stroke="#F6D896" stroke-width="2" fill="none"/>
    <g transform="translate(30 156)"><path d="M0 0 C-2 -30 4 -60 14 -82" stroke="#6B4A2A" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M0 0 C-2 -30 4 -60 14 -82" stroke="#8A6A44" stroke-width="7" fill="none" stroke-dasharray="3 5"/>${[[-34, 22], [-14, 36], [20, 40], [40, 26], [30, -8]].map(([dx, dy]) => `<path d="M14 -82 Q${14 + dx * .5} ${-94} ${14 + dx} ${-82 + dy * .4} Q${14 + dx * .5} ${-84} 14 -82Z" fill="#0F3D28"/>`).join('')}
      ${LICHTER([[4, -24], [6, -42], [9, -58], [12, -72]], undefined, 2.2)}</g>
    <ellipse cx="128" cy="172" rx="40" ry="5" fill="#A87A36" opacity=".6"/>
    <g transform="translate(128 170)"><rect x="-4" y="-6" width="8" height="8" fill="#6B4A2A"/><path d="M0 -84 L18 -58 H9 L26 -32 H13 L32 -6 H-32 L-13 -32 H-26 L-9 -58 H-18Z" fill="#1F8A55"/><path d="M0 -84 L18 -58 H9 L26 -32 H13 L32 -6 H0Z" fill="#0D5232"/><path d="M-18 -58 H-9 M-26 -32 H-13 M-32 -6 H-4" stroke="#3FA66B" stroke-width="2" stroke-linecap="round"/>
      <path d="M-14 -50 Q0 -42 14 -52 M-22 -24 Q0 -16 22 -26" stroke="#FFD23F" stroke-width="1.4" fill="none"/>${LICHTER([[-8, -50], [8, -50], [-16, -24], [0, -22], [16, -26], [-22, -6], [10, -8]], undefined, 2.4)}<path d="${ST5(0, -88, 8)}" fill="#FFD23F"/><path d="${ST5H(0, -88, 8)}" fill="#E0A40E"/></g>
    ${PAKET(84, 160, 20, 16, '#E5243B', '#B3122B', '#FFC94A')}${PAKET(160, 158, 18, 18, '#3DDC84', '#1F9A5E', '#FFF3D1')}${PAKET(108, 166, 14, 10, '#FFC94A', '#E0A40E', '#7B1E6E')}
    ${BAND(u, '24. DEZEMBER', 176)}`),
};
const MOTIV_NAME = { koala: 'Koala im Sommer-Dezember', surf: 'Surf-Schlitten', neonbaum: 'Neon-Baum', pinguin: 'Pinguin mit Kopfhörern', polarlicht: 'Polarlicht', flieger: 'Flieger mit Lichterkette',
  kaenguru: 'Känguru mit Geschenk', sandmann: 'Schneemann aus Sand', erdkugel: 'Weltkugel als Christbaumkugel', rentier: 'Rentier mit VR-Brille', bordkarte: 'Bordkarte zum Nordpol',
  controller: 'Lebkuchen-Controller', strandfeuer: 'Lichter am Strand', kompass: 'Kompass mit Stern', schneeflocke: 'Pixel-Schneeflocke', stern: 'Kometen-Stern',
  krampus: 'Krampus mit Besen', nikolaus: 'Karte: Nikolaus-Stiefel', heiligabend: 'Karte: Heiligabend' };
const MOTIVE_ALLGEMEIN = ['koala', 'surf', 'neonbaum', 'pinguin', 'polarlicht', 'flieger', 'kaenguru', 'sandmann', 'erdkugel', 'rentier', 'bordkarte', 'controller', 'strandfeuer', 'kompass', 'schneeflocke', 'stern'];
// Ein Objekt mit allen Motiven als SVG-Text (Schlüssel wie auf dem Server, server.md 3.9)
const LERN_ADVENT_MOTIVE = Object.fromEntries(Object.keys(MOTIV_NAME).map((k) => [k, { name: MOTIV_NAME[k], svg: (u) => M2[k](u || uid('m' + k)), sonder: !MOTIVE_ALLGEMEIN.includes(k) }]));
const motivSvg = (id, slice = false) => { const m = LERN_ADVENT_MOTIVE[id]; if (!m) return null; const s = m.svg(); return slice ? s.replace('<svg ', '<svg preserveAspectRatio="xMidYMid slice" ') : s; };
const motivFuer = (t) => (t?.motiv && LERN_ADVENT_MOTIVE[t.motiv] ? t.motiv : t?.art === 'karte' ? (Number(t.nr) === 6 ? 'nikolaus' : 'heiligabend') : t?.art === 'krampus' ? 'krampus' : null);

// ================= Tür und Inhaltskarten (Entwurf 2, teile/tuer2.js) =================
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

const PRAEGUNG = (id) => `<svg class="praegung" viewBox="0 0 80 80" aria-hidden="true"><defs><path id="${id}" d="M40 40 m-29 0 a29 29 0 1 1 58 0 a29 29 0 1 1 -58 0"/></defs>
  <g fill="none" stroke-width="1.4"><circle cx="40" cy="40" r="36" stroke="#fff"/><circle cx="40" cy="40" r="36" stroke="#A8873A" opacity=".35" transform="translate(.9 .9)"/><circle cx="40" cy="40" r="22" stroke="#fff"/><circle cx="40" cy="40" r="22" stroke="#A8873A" opacity=".35" transform="translate(.9 .9)"/></g>
  <text font-family="ui-monospace, Menlo, monospace" font-size="7.4" font-weight="800" letter-spacing="2.2" fill="#A8873A" opacity=".45"><textPath href="#${id}">ADVENTSKALENDER · 2026 · ECHT ·</textPath></text>
  <path d="M40 27 l3.6 8 8.7 .8 -6.6 5.8 2 8.6 -7.7 -4.6 -7.7 4.6 2 -8.6 -6.6 -5.8 8.7 -.8z" fill="#A8873A" opacity=".3" transform="translate(.8 .8)"/><path d="M40 27 l3.6 8 8.7 .8 -6.6 5.8 2 8.6 -7.7 -4.6 -7.7 4.6 2 -8.6 -6.6 -5.8 8.7 -.8z" fill="#FFF9E6"/></svg>`;
const GUILLOCHE = `<svg class="guilloche" viewBox="0 0 320 160" preserveAspectRatio="none" aria-hidden="true"><g fill="none" stroke="#E7D39A" stroke-width=".7">${Array.from({ length: 9 }, (_, i) => `<path d="M0 ${18 + i * 16} ${Array.from({ length: 16 }, (_, j) => `Q${j * 20 + 10} ${18 + i * 16 + (j % 2 ? -7 : 7)} ${j * 20 + 20} ${18 + i * 16}`).join(' ')}"/>`).join('')}</g></svg>`;
const HUF = `<svg viewBox="0 0 40 40" aria-hidden="true"><g fill="currentColor"><path d="M8 4 C3 6 2 16 6 20 C9 22 13 20 14 16 C15 10 13 3 8 4Z"/><path d="M26 4 C31 6 32 16 28 20 C25 22 21 20 20 16 C19 10 21 3 26 4Z"/><path d="M12 26 C9 28 9 34 12 36 C14 37 16 35 16 33 C16 30 15 25 12 26Z" opacity=".7"/><path d="M22 26 C25 28 25 34 22 36 C20 37 18 35 18 33 C18 30 19 25 22 26Z" opacity=".7"/></g></svg>`;
const WALZEN_STERN = (u) => `<svg viewBox="0 0 60 60" aria-hidden="true"><defs><linearGradient id="${u}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF6C8"/><stop offset=".45" stop-color="#FFD23F"/><stop offset="1" stop-color="#B57A06"/></linearGradient></defs><path d="M30 9 l6 13.2 14.4 1.4 -10.9 9.6 3.2 14.2 -12.7 -7.5 -12.7 7.5 3.2 -14.2 -10.9 -9.6 14.4 -1.4z" fill="url(#${u})"/><path d="M30 9 l6 13.2 14.4 1.4 -10.9 9.6 3.2 14.2 -12.7 -7.5z" fill="#8A5A00" opacity=".22"/><path d="M30 13 l4.4 9.6" stroke="#FFFBEA" stroke-width="1.4" stroke-linecap="round" opacity=".8"/></svg>`;
const NIETE_HTML = () => {
  return `<div class="niete2" role="img" aria-label="Niete mit Trostpreis: plus 1 Stern"><div class="nt-stempel2"><span>NIETE</span></div><div class="nt-trost">…aber nicht ganz.</div>
    <div class="nt-preis"><svg class="nt-stern" viewBox="0 0 80 80" aria-hidden="true"><path d="M40 6 l9.4 20.6 22.6 2.2 -17 15 5 22.2 -20 -11.8 -20 11.8 5 -22.2 -17 -15 22.6 -2.2z" fill="#FFD23F"/><path d="M40 6 l9.4 20.6 22.6 2.2 -17 15 5 22.2 -20 -11.8z" fill="#E0A40E"/>
      <g transform="rotate(-32 40 42)"><rect x="18" y="35" width="44" height="14" rx="7" fill="#F4C9A8"/><rect x="33" y="36.5" width="14" height="11" rx="2" fill="#E8B48E"/>${[[23, 39], [26, 45], [53, 39], [56, 45], [36, 39], [41, 44], [44, 39]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r=".9" fill="#C98E66"/>`).join('')}</g>
      <circle cx="33" cy="36" r="2.2" fill="#3A2A12"/><circle cx="47" cy="36" r="2.2" fill="#3A2A12"/><path d="M34 52 q6 -4 12 0" stroke="#3A2A12" stroke-width="2" fill="none" stroke-linecap="round"/></svg>
      <div><div class="nt-zahl">+1 ★</div><div class="nt-klein">TROSTPREIS</div></div></div></div>`;
}
const STERNE_HTML = (u, n = 0) => {
  return `<div class="sterne2" role="img" aria-label="Plus ${n} Sterne"><svg class="muenze" viewBox="0 0 160 160" aria-hidden="true"><defs><radialGradient id="${u}g" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#FFF6C8"/><stop offset=".5" stop-color="#FFD23F"/><stop offset="1" stop-color="#B57A06"/></radialGradient><linearGradient id="${u}r" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE27A"/><stop offset="1" stop-color="#8A5A00"/></linearGradient></defs>
    <circle cx="82" cy="84" r="70" fill="#000" opacity=".28"/><circle cx="80" cy="80" r="70" fill="url(#${u}r)"/><circle cx="80" cy="80" r="66" fill="none" stroke="#FFF1A8" stroke-width="3" stroke-dasharray="2 4" opacity=".7"/><circle cx="80" cy="80" r="58" fill="url(#${u}g)"/>
    <circle cx="80" cy="80" r="58" fill="none" stroke="#8A5A00" stroke-width="1.5" opacity=".5"/><path d="M80 38 l11 24 26 2.6 -19.6 17.2 5.8 25.6 -23.2 -13.6 -23.2 13.6 5.8 -25.6 -19.6 -17.2 26 -2.6z" fill="#E0A40E"/><path d="M80 38 l11 24 26 2.6 -19.6 17.2 5.8 25.6 -23.2 -13.6z" fill="#B57A06" opacity=".7"/><path d="M80 44 l8.6 18.8" stroke="#FFF6C8" stroke-width="2" stroke-linecap="round"/>
    <path d="M38 52 A50 50 0 0 1 70 26" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" opacity=".55"/></svg><div class="st-zahl">+${n}<i>★</i></div><div class="st-klein">GUTGESCHRIEBEN</div></div>`;
}


const GESCHENK_ICO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="8" width="18" height="13" rx="2"/><path d="M12 8v13M3 12h18M12 8c-2-4-6-4-6-1s4 1 6 1c2 0 6 2 6-1s-4-3-6 1"/></svg>';
const HORN_ICO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 11C3 8 3 4 5 2c0 4 2 6 4 7M18 11c3-3 3-7 1-9 0 4-2 6-4 7"/><path d="M12 8c-4 0-6 3-6 7 0 4 3 7 6 7s6-3 6-7c0-4-2-7-6-7z"/><path d="M9.5 17c1.5 1.2 3.5 1.2 5 0"/></svg>';
const STERN_ICO = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l2.9 6.6 7.1.6-5.4 4.7 1.6 7L12 17.3 5.8 21l1.6-7L2 9.2l7.1-.6z"/></svg>';
const MOND_ICO = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M10.5 1.5a6.5 6.5 0 1 0 4 11.6A7 7 0 0 1 10.5 1.5z" fill="currentColor"/></svg>';
const UHR_ICO = '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 4.6V8l2.4 1.6" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>';
const SCHLEIFE_KL = (gold) => `<svg class="k-schleife" viewBox="0 0 40 20" aria-hidden="true"><path d="M20 9 C14 0 3 1 4 8 C5 13 14 12 20 10 Z M20 9 C26 0 37 1 36 8 C35 13 26 12 20 10 Z" fill="${gold ? '#C98A0A' : '#E5243B'}"/><path d="M20 9 C15 4 9 4 7 7 C11 7 15 8 20 10Z M20 9 C25 4 31 4 33 7 C29 7 25 8 20 10Z" fill="#000" opacity=".2"/><path d="M18 10 L14 19 M22 10 L26 19" stroke="${gold ? '#C98A0A' : '#E5243B'}" stroke-width="3" stroke-linecap="round"/><rect x="16.5" y="6.5" width="7" height="6" rx="2.5" fill="${gold ? '#E0A40E' : '#C8172F'}"/></svg>`;

// ---------- Datum ----------
const WT = ['SO', 'MO', 'DI', 'MI', 'DO', 'FR', 'SA'];
const MON = ['JANUAR', 'FEBRUAR', 'MÄRZ', 'APRIL', 'MAI', 'JUNI', 'JULI', 'AUGUST', 'SEPTEMBER', 'OKTOBER', 'NOVEMBER', 'DEZEMBER'];
const tagDatum = (iso) => { const m = String(iso || '').match(/^(\d{4})-(\d{2})-(\d{2})/); return m ? new Date(Number(m[1]), Number(m[2]) - 1, Number(m[3]), 12) : new Date(); };
const datumOben = (iso) => { const d = tagDatum(iso); return `${WT[d.getDay()]}, ${d.getDate()}. ${MON[d.getMonth()]}`; };
const datumKurz = (iso) => { const d = tagDatum(iso); return `${d.getDate()}.${d.getMonth() + 1}.`; };
const zeitpunkt = (iso) => { if (!iso) return ''; const d = new Date(iso); if (Number.isNaN(d.getTime())) return ''; return `${d.getDate()}.${d.getMonth() + 1}. um ${String(d.getHours()).padStart(2, '0')}:${String(d.getMinutes()).padStart(2, '0')} Uhr`; };

// ---------- Inhaltskarten als DOM (Texte der Eltern als Text) ----------
function gutscheinKarte({ nr, titel, text, sterne, tausch = false }) {
  const w = el('div', { class: 'ticket-w' });
  const t = el('div', { class: 'ticket', role: 'img', 'aria-label': `${tausch ? 'Tauschkarte' : 'Gutschein'}: ${titel || ''}. Hol dir bei Mama oder Papa ab.` },
    el('div', { class: 'tk-kopf' }, grafik(STERN_ICO + (tausch ? 'TAUSCHKARTE' : 'GUTSCHEIN'), 'tk-marke', 'span'), el('span', {}, `TÜR ${nr} · NR. ${String(nr).padStart(2, '0')}/24`)),
    el('div', { class: 'tk-koerper' }, grafik(GUILLOCHE, 'guilloche-w'), el('small', {}, 'HOL DIR BEI MAMA ODER PAPA AB'), el('h3', {}, titel || (tausch ? 'Tauschkarte' : 'Gutschein')), text ? el('p', {}, text) : null, grafik(PRAEGUNG(uid('pr')), 'praegung-w')),
    el('div', { class: 'tk-perf', 'aria-hidden': 'true' }),
    el('div', { class: 'tk-fuss' }, grafik(GESCHENK_ICO, 'tk-ico', 'span'), el('span', {}, 'Liegt jetzt in „Meine Gutscheine“.'), sterne ? el('b', { class: 'tk-st' }, `+${zahlS(sterne)}`, el('i', {}, '★')) : null));
  w.append(t); return w;
}
function krampusKarte({ nr, titel, text }) {
  return el('div', { class: 'kr-karte', role: 'img', 'aria-label': `Krampus-Karte: ${titel || ''}. Erledigt bestätigen Mama oder Papa.` },
    el('div', { class: 'kr-kopf' }, el('span', {}, 'KRAMPUS WAR DA'), el('span', {}, `TÜR ${nr}`), grafik('<svg class="kr-kratz" viewBox="0 0 90 40"><path d="M10 38 L30 2 M28 38 L48 2 M46 38 L66 2" stroke="#1C0A0E" stroke-width="6" stroke-linecap="round"/></svg>', 'kr-kratz-w', 'span')),
    el('div', { class: 'kr-in' }, grafik(motivSvg('krampus'), 'kr-bild'), el('div', {}, el('small', {}, 'DEINE AUFGABE'), el('h3', {}, titel || 'Eine kleine Aufgabe'), text ? el('p', {}, text) : null)),
    el('div', { class: 'kr-perf', 'aria-hidden': 'true' }),
    el('div', { class: 'kr-fuss' }, el('span', { class: 'kr-box', 'aria-hidden': 'true' }), el('span', {}, 'Erledigt? Bestätigen Mama oder Papa.'), grafik(HUF, 'kr-huf', 'span')));
}
function jackpotKarte(n) {
  const walze = (i) => `<span class="jp-walze"><span class="jp-zeile weg">${WALZEN_STERN(uid('jw'))}</span><span class="jp-zeile">${WALZEN_STERN(uid('jw'))}</span><span class="jp-zeile weg">${WALZEN_STERN(uid('jw'))}</span></span>`;
  const d = el('div', { class: 'jackpot2', role: 'img', 'aria-label': `Jackpot: plus ${n} Sterne` });
  d.innerHTML = `<div class="jp-fenster" aria-hidden="true"><i class="jp-linie"></i>${[0, 1, 2].map(walze).join('')}</div><div class="jp-wort2" aria-hidden="true"><span>JACKPOT</span></div>`;
  d.append(el('div', { class: 'jp-zahl2', 'aria-hidden': 'true' }, `+${zahlS(n)}`, el('i', {}, '★'))); return d;
}
function nieteKarte(n) {
  const d = el('div', {}); d.innerHTML = NIETE_HTML(); const k = d.firstElementChild; k.setAttribute('aria-label', `Niete mit Trostpreis: plus ${n} ${Number(n) === 1 ? 'Stern' : 'Sterne'}`);
  const z = k.querySelector('.nt-zahl'); if (z) z.textContent = `+${zahlS(n)} ★`; return k;
}
function sterneKarte(n) { const d = el('div', {}); d.innerHTML = STERNE_HTML(uid('mz')); const k = d.firstElementChild; k.setAttribute('aria-label', `Plus ${n} Sterne`); k.querySelector('.st-zahl').firstChild.textContent = `+${zahlS(n)}`; return k; }

// ---------- Inhalt eines offenen Türchens ----------
const sorteVon = (t) => (t.art === 'krampus' ? 'krampus' : t.art === 'sterne' ? (t.variante === 'jackpot' ? 'jackpot' : t.variante === 'niete' ? 'niete' : 'sterne') : t.art === 'karte' ? 'karte' : t.art === 'bild' ? 'bild' : t.art === 'gutschein' ? 'gutschein' : 'leer');
function inhaltEl(t) {
  const n = Number(t.sterne) || 0; const sorte = sorteVon(t); const kids = [];
  if (sorte === 'bild') { const m = motivFuer(t); kids.push(m ? grafik(motivSvg(m), 'motiv-gross2') : el('div', { class: 'leer-licht2', 'aria-hidden': 'true' }, el('b', {}, 'Licht.')));
    if (m) { kids[0].removeAttribute('aria-hidden'); kids[0].setAttribute('role', 'img'); kids[0].setAttribute('aria-label', 'Bild: ' + LERN_ADVENT_MOTIVE[m].name); }
    if (t.titel) kids.push(el('p', { class: 'adv-satz' }, el('b', {}, t.titel))); if (t.text) kids.push(el('p', { class: 'adv-satz' }, t.text)); }
  else if (sorte === 'gutschein') kids.push(gutscheinKarte({ nr: t.nr, titel: t.titel, text: t.text, sterne: n, tausch: t.variante === 'tausch' }));
  else if (sorte === 'krampus') kids.push(krampusKarte(t));
  else if (sorte === 'jackpot') kids.push(jackpotKarte(n), el('p', { class: 'adv-satz' }, t.text || 'Schon gutgeschrieben. Einfach so.'));
  else if (sorte === 'niete') kids.push(nieteKarte(n || 1), el('p', { class: 'adv-satz' }, t.text || 'Morgen wartet ein neues Türchen.'));
  else if (sorte === 'sterne') { kids.push(sterneKarte(n)); if (t.text) kids.push(el('p', { class: 'adv-satz' }, t.text)); }
  else if (sorte === 'karte') { const m = motivFuer(t); const k = grafik(motivSvg(m), 'karte-gross2 ' + m); k.removeAttribute('aria-hidden'); k.setAttribute('role', 'img'); k.setAttribute('aria-label', 'Karte: ' + (LERN_ADVENT_MOTIVE[m]?.name || 'Weihnachten'));
    kids.push(k); if (t.text || t.titel) kids.push(el('p', { class: 'adv-satz karte-satz' }, `„${t.text || t.titel}“`, el('small', {}, '– Mama und Papa')));
    if (n) kids.push(el('div', { class: 'adv-dazu', role: 'img', 'aria-label': `Dazu plus ${n} Sterne` }, el('span', {}, `+${zahlS(n)} ★`), el('small', {}, n >= 1000 ? 'JACKPOT · GUTGESCHRIEBEN' : 'GUTGESCHRIEBEN'))); }
  else { kids.push(el('div', { class: 'leer-licht2', role: 'img', 'aria-label': 'Nur Licht' }, el('b', { 'aria-hidden': 'true' }, 'nur Licht.')), el('p', { class: 'adv-satz' }, t.text || 'Hier ist heute nichts versteckt. Aber die Etappe hast du – und die bleibt.')); }
  if (n && ['bild', 'krampus', 'leer'].includes(sorte)) kids.push(el('span', { class: 'adv-plus' }, `+${zahlS(n)} ★`));
  return el('div', { class: 'adv-inhalt' }, ...kids);
}
function inhaltText(t) {
  const n = Number(t.sterne) || 0; const sorte = sorteVon(t); const st = n ? ` ${n === 1 ? '1 Stern ist' : `${zahlS(n)} Sterne sind`} schon auf deinem Konto.` : '';
  if (sorte === 'krampus') return 'Steht in „Meine Gutscheine“ unter „Vom Krampus“. Mama oder Papa haken ab, wenn’s erledigt ist.';
  if (sorte === 'jackpot' || sorte === 'sterne') return st.trim();
  if (sorte === 'niete') return `${st.trim()} Nicht jedes Türchen ist ein Jackpot.`;
  if (sorte === 'karte') return (Number(t.nr) === 6 ? 'Heute nur eine Karte – das Geschenk gibt’s von Mama und Papa.' : 'Heute nur eine Karte – die Geschenke gibt’s unterm Baum.') + st;
  if (sorte === 'gutschein') return 'Einlösen, wann du willst: Menü › Meine Gutscheine.' + st;
  return 'Bleibt im Adventskalender – du kannst es jederzeit wieder ansehen.' + st;
}
const ansageText = (t) => { const s = sorteVon(t); const n = Number(t.sterne) || 0;
  return `Türchen ${t.nr} ist offen: ` + (s === 'gutschein' ? `Gutschein „${t.titel || ''}“` : s === 'krampus' ? `Krampus war da – Aufgabe „${t.titel || ''}“` : s === 'jackpot' ? `Jackpot, plus ${n} Sterne` : s === 'niete' ? `Niete, plus ${n} Stern Trostpreis` : s === 'sterne' ? `plus ${n} Sterne` : s === 'karte' ? 'eine Karte von Mama und Papa' : s === 'bild' ? `ein Bild${t.text ? ': ' + t.text : ''}` : 'nur Licht') + (n && !['jackpot', 'niete', 'sterne'].includes(s) ? `, plus ${n} Sterne` : '') + '.'; };
const stickerAnlass = (t) => (sorteVon(t) === 'niete' ? 'advent_niete' : sorteVon(t) === 'krampus' ? 'advent_krampus' : 'advent');

// ================= A1: Tür nach der Etappe / „bereit“ im Kalender =================
const tuerSorte = (nr, art) => (art === 'krampus' ? 'krampus' : Number(nr) === 6 ? 't6' : Number(nr) === 24 ? 't24' : 'normal');
function tuerRahmen(nr, sorte, label) {
  const klappe = el('button', { type: 'button', class: 'adv-klappe', 'aria-label': label });
  klappe.innerHTML = tuerSvg(nr, sorte); klappe.append(el('span', { class: 'adv-klappe-schatten', 'aria-hidden': 'true' }));
  const r = el('div', { class: `adv-rahmen tuer-${sorte}` }, el('div', { class: 'adv-licht', 'aria-hidden': 'true' }, el('i', {})), klappe); r.klappe = klappe; return r;
}
const funkenEl = () => el('div', { class: 'adv-funken', 'aria-hidden': 'true' }, ...Array.from({ length: 14 }, (_, i) => el('i', { style: `left:${10 + ((i * 37) % 80)}%;top:${16 + ((i * 53) % 52)}%;opacity:${0.35 + ((i * 7) % 6) / 10};transform:scale(${0.6 + (i % 3) * 0.3})` })));
const FEHLER_KIND = [[/nur in der App des Kindes/, 'Türchen öffnen geht nur in der App des Kindes.'], [/Nicht angemeldet/, 'Bitte neu anmelden.'], [/Kein Zugriff|nicht gefunden/, 'Dieses Türchen gehört nicht hierher.']];
const freundlich = (e) => (FEHLER_KIND.find(([re]) => re.test(String(e?.message || '')))?.[1] || 'Das Türchen klemmt gerade. Versuch es gleich noch einmal.');
// st: Stand (bereit, naechste_nr, heute, tag_nr, offen_heute …); weiter(): ursprüngliches Ziel; quelle: 'etappe' | 'kalender'
function tuerZeigen({ kindObj, kindId, stand, weiter, weiterText = 'Weiter', quelle = 'etappe', zeigeTuer = null }) {
  const kid = Number(kindId); const nr0 = Number(stand.naechste_nr); const wenig = lernWenigBewegung();
  const tok0 = store.token; const cid = lernCid(); let sperre = false; let fertig = false;
  const nachgeholt = stand.phase !== 'laeuft' || nr0 < Number(stand.tag_nr);
  const zweite = Number(stand.offen_heute) >= 1;
  const rahmen = tuerRahmen(nr0, tuerSorte(nr0), `Türchen ${nr0} öffnen`);
  const oben = el('div', { class: 'lr-ab-oben' }, `${zweite ? '2. TÜRCHEN HEUTE' : 'ADVENTSKALENDER'} · ${datumOben(stand.heute)}`);
  const titel = el('h2', { class: 'lr-ab-titel' }, `Türchen ${nr0}`, nachgeholt ? el('span', { class: 'adv-badge' }, 'NACHGEHOLT') : null);
  const zeile = el('p', { class: 'adv-zeile' }, zweite ? `Zweite Etappe heute – mehr als 2 Türchen am Tag gehen nicht.` : 'Für deine Etappe. Tippen zum Öffnen.');
  const buehne = el('div', { class: 'adv-buehne' }, el('div', {}, rahmen, el('p', { class: 'adv-antippen', 'aria-hidden': 'true' }, '▲ TIPPEN ZUM ÖFFNEN')));
  const ansage = el('p', { class: 'sr-only', role: 'status', 'aria-live': 'polite' });
  const szene = el('div', { class: 'lr-ab-szene' }, oben, titel, zeile, buehne, ansage);
  const meldung = el('p', { class: 'adv-fehler', role: 'alert', hidden: true });
  const oeffnenK = lernGrossKnopf(`Türchen ${nr0} öffnen`, null, { class: 'adv-tuer-knopf', onclick: () => oeffne() });
  const spaeter = el('button', { type: 'button', class: 'lr-ab-pause adv-spaeter', onclick: () => { if (!sperre) weiter(); } }, quelle === 'etappe' ? `Später öffnen – weiter zu: ${weiterText}` : 'Später öffnen');
  const blatt = el('div', { class: 'lr-ab-blatt' }, el('p', { class: 'adv-klein' }, quelle === 'etappe' ? 'Etappe gelandet ✓' : 'Adventskalender'),
    el('p', { class: 'adv-txt' }, 'Dahinter ist ein Bild oder ein Geschenk von Mama und Papa.'), meldung, oeffnenK, spaeter);
  const app = el('div', { class: 'lr-ab-app lr-advent sorte-' + (tuerSorte(nr0) === 't24' ? 't24' : 'tuer') + (wenig ? '' : ' lr-adv-bewegt'), 'data-nr': String(nr0) }, szene, blatt);
  rahmen.klappe.addEventListener('click', () => oeffne());
  const huelle = lernAbschlussZeigen(kindObj, app, { label: `Türchen ${nr0}` });
  setTimeout(() => { if (!fertig) oeffnenK.focus({ preventScroll: true }); }, 60);
  const gesperrt = (an) => { sperre = an; oeffnenK.disabled = an; rahmen.klappe.disabled = an; oeffnenK.toggleAttribute('aria-busy', an); spaeter.disabled = an; };
  async function oeffne() {
    if (sperre || fertig) return; gesperrt(true); meldung.hidden = true; // synchron vor dem ersten await: Doppeltipp/Tastatur öffnet einmal
    let r;
    try { r = await lernCall('schule_advent_oeffnen', { lernender_id: kid, client_id: cid }); } // Netz-Wiederholung: dieselbe client_id
    catch (e) { if (!huelle.isConnected || store.token !== tok0) return; gesperrt(false); meldung.hidden = false; meldung.textContent = freundlich(e); return; }
    if (!huelle.isConnected || store.token !== tok0) return; // Antwort gehört zu dieser Ansicht und diesem Zugang
    lernAdventVergessen(kid);
    if (!r || r.aktiv === false || r.geoeffnet === false) { // erwartbare Zustände: still weiter; zweites Gerät – das zuletzt geöffnete zeigen
      if (r?.letzte_nr) { try { const x = await lernCall('schule_advent_tuer_lesen', { lernender_id: kid, nr: Number(r.letzte_nr) });
        if (huelle.isConnected && store.token === tok0 && x?.tuer) { zeige(x.tuer, { schon: true }); return; } } catch { /* still weiter */ } }
      if (huelle.isConnected) weiter(); return;
    }
    if (r.sterne_gutgeschrieben) lernVergessen(kid); // Konto und Sterne-Chip neu laden
    zeige(r.tuer, { r });
  }
  function zeige(t, { r = null, schon = false } = {}) {
    fertig = true; const sorte = sorteVon(t); const nr = Number(t.nr) || nr0;
    app.className = app.className.replace(/sorte-\S+/, 'sorte-' + (sorte === 'bild' || sorte === 'gutschein' || sorte === 'leer' ? (nr === 24 ? 't24' : 'tuer') : sorte));
    lernErsetze(titel, `Türchen ${nr}`, t.nachgeholt ? el('span', { class: 'adv-badge' }, 'NACHGEHOLT') : null);
    oben.textContent = `${sorte === 'krampus' ? 'KRAMPUS WAR DA' : 'ADVENTSKALENDER'} · ${datumOben(t.tag || stand.heute)}`;
    zeile.textContent = sorte === 'krampus' ? 'Kein Sterne-Abzug. Nur eine kleine Aufgabe.' : sorte === 'karte' && nr === 24 ? 'Frohe Weihnachten!' : schon ? 'Schon offen – auf einem anderen Gerät.' : '';
    zeile.hidden = !zeile.textContent;
    const inhaltZeigen = () => { if (!huelle.isConnected) return; lernErsetze(buehne, inhaltEl(t)); szene.prepend(funkenEl());
      const st0 = lernJwPlatz(kid, stickerAnlass(t)); if (st0) { szene.classList.add('lr-jw-mit'); szene.append(st0); } };
    if (wenig) inhaltZeigen(); // Bewegung reduzieren: keine Drehung, der Inhalt steht sofort da
    else { if (sorte === 'krampus') { const neu = tuerRahmen(nr, 'krampus', `Türchen ${nr}`); rahmen.replaceWith(neu); requestAnimationFrame(() => neu.classList.add('auf')); }
      else rahmen.classList.add('auf'); setTimeout(inhaltZeigen, 650); }
    const naechst = r ? (Number(r.frei_heute) > 0 ? `Türchen ${r.naechste_nr} ist auch bereit – im Adventskalender.` : Number(r.moeglich_heute) > 0 ? 'Heute geht noch ein Türchen – nach deiner nächsten Etappe.' : nr < 24 && stand.phase === 'laeuft' ? 'Das nächste Türchen gibt’s morgen – nach deiner nächsten Etappe.' : '') : '';
    const weiterK = lernGrossKnopf(quelle === 'etappe' ? `Weiter: ${weiterText}` : 'Zurück zum Kalender', null, { onclick: () => weiter() });
    lernErsetze(blatt, el('p', { class: 'adv-klein' }, `Türchen ${nr} ist offen`), el('p', { class: 'adv-txt' }, inhaltText(t)), naechst ? el('p', { class: 'lr-ab-leise' }, naechst) : null, weiterK,
      quelle === 'etappe' ? el('a', { class: 'lr-ab-pause', href: `#/advent/${kid}` }, 'Adventskalender ansehen') : null);
    ansage.textContent = ansageText({ ...t, nr }); setTimeout(() => weiterK.focus({ preventScroll: true }), wenig ? 30 : 700);
  }
  if (zeigeTuer) zeige(zeigeTuer, { schon: false });
  return huelle;
}

// ================= Hinweiszeile in „Gerade dran“ (A3) und Menü =================
const wartendeNr = (st) => (st.tueren || []).filter((x) => ['bereit', 'heute', 'nachholen'].includes(x.zustand)).map((x) => Number(x.nr)).sort((a, b) => a - b);
const geschlosseneFaellige = (st) => (st.tueren || []).some((x) => ['bereit', 'heute', 'nachholen'].includes(x.zustand));
function lernAdventZeile(kindId, st) {
  if (!st?.aktiv || !['laeuft', 'nachholen'].includes(st.phase)) return null;
  const tuer = (n, g) => el('span', { class: 'lr-adv-mtuer' + (g ? ' g' : ''), 'aria-hidden': 'true' }, String(n));
  if (st.bereit && st.naechste_nr) return el('a', { class: 'rk-adv-zeile bereit', href: `#/advent/${kindId}-oeffnen` }, tuer(st.naechste_nr), el('span', {}, el('b', {}, `Türchen ${st.naechste_nr} ist bereit`), ' – jetzt öffnen'), el('span', { class: 'pf', 'aria-hidden': 'true' }, '›'));
  const w = wartendeNr(st);
  if (st.braucht_etappe && w.length) { const z = w.slice(0, 3); const t = z.length === 1 ? `Türchen ${z[0]} wartet` : `Türchen ${z.slice(0, -1).join(', ')} + ${z.at(-1)} warten`;
    return el('a', { class: 'rk-adv-zeile', href: `#/advent/${kindId}` }, tuer(z[0]), el('span', {}, el('b', {}, t), ' – je Etappe eins'), el('span', { class: 'pf', 'aria-hidden': 'true' }, '›')); }
  if (Number(st.moeglich_heute) === 0 && geschlosseneFaellige(st)) return el('a', { class: 'rk-adv-zeile morgen', href: `#/advent/${kindId}` }, tuer(w[0] || st.naechste_nr || ''), el('span', {}, `${Number(st.offen_heute) || 2} Türchen heute offen – `, el('b', {}, 'morgen geht’s weiter')), el('span', { class: 'pf', 'aria-hidden': 'true' }, '›'));
  return null;
}
function lernAdventMenue(st, kind, aktiv, zu) {
  const out = []; const w = st.aktiv ? wartendeNr(st).length : 0; const g = st.gutscheine || {};
  if (st.menue?.kalender) out.push(el('a', { href: `#/advent/${kind.id}`, class: 'lr-adv-menue' + (aktiv === 'advent' ? ' on' : ''), ...(aktiv === 'advent' ? { 'aria-current': 'page' } : {}), onclick: zu },
    el('span', { class: 'lr-adv-mtuer', 'aria-hidden': 'true' }, String(Math.min(24, Number(st.tag_nr) || 1))), 'Adventskalender', w ? el('span', { class: 'lr-adv-zahl' }, `${w} ${w === 1 ? 'wartet' : 'warten'}`) : null));
  const offen = (Number(g.offen) || 0) + (Number(g.tauschkarten) || 0);
  if (st.menue?.gutscheine) out.push(el('a', { href: `#/gutscheine/${kind.id}`, class: 'lr-adv-menue' + (aktiv === 'gutscheine' ? ' on' : ''), ...(aktiv === 'gutscheine' ? { 'aria-current': 'page' } : {}), onclick: zu },
    grafik(GESCHENK_ICO, 'lr-adv-mtuer g', 'span'), 'Meine Gutscheine', offen ? el('span', { class: 'lr-adv-zahl g' }, String(offen)) : null));
  return out;
}

// Kopfzeile der Kinderseiten im App-Kopf (wie die Reisekarte): Titel · ★ · ≡ – ersetzt Titel und obere Menüzeile
function kopfOben(d, titel) {
  const g = lernGestaltung(d.kind); const n = lernZahl(d.konto?.sterne ?? 0);
  const kopf = el('div', { class: 'lr-adv-hkopf lr-abflug-' + g }, el('b', {}, titel),
    el('a', { class: 'lr-chip-stern', href: `#/reisepass/${d.kind.id}`, 'aria-label': `${n} Sterne – zum Reisepass` }, '★ ' + n),
    el('button', { type: 'button', class: 'rk-menue', 'aria-label': 'Menü', 'aria-haspopup': 'dialog', onclick: () => { const dlg = main.querySelector('dialog.lr-blatt'); if (dlg && !dlg.open) dlg.showModal(); } }, '≡'));
  const h = document.querySelector('header.top'); if (h) { h.querySelectorAll(':scope > .lr-adv-hkopf').forEach((x) => x.remove()); const tt = h.querySelector('#title'); if (tt) tt.after(kopf); else h.prepend(kopf); document.body.classList.add('lr-adv-oben'); }
  addEventListener('hashchange', () => { kopf.remove(); if (!document.querySelector('.lr-adv-hkopf')) document.body.classList.remove('lr-adv-oben'); }, { once: true });
}
// ================= A2: Kalender (Kind) =================
const UMORDNUNG = [11, 4, 19, 1, 23, 8, 14, 6, 17, 2, 21, 9, 13, 24, 5, 16, 3, 20, 10, 7, 15, 22, 12, 18];
const ZUSTAND_TEXT = { nachholen: 'nachholen', heute: 'heute dran, nach deiner nächsten Etappe', bereit: 'bereit, jetzt öffnen', morgen: 'morgen', zu: 'noch zu', verfallen: 'verpasst' };
function kachelTitel(t) { const s = sorteVon(t);
  return s === 'krampus' ? 'Krampus' : s === 'jackpot' ? 'Jackpot' : s === 'niete' ? 'Trostpreis' : s === 'sterne' ? 'Sterne' : s === 'leer' ? 'nur Licht' : s === 'karte' ? 'Karte' : s === 'bild' ? (t.titel || LERN_ADVENT_MOTIVE[t.motiv]?.name || 'Bild') : (t.titel || (t.variante === 'tausch' ? 'Tauschkarte' : 'Gutschein')); }
function kachel(t, beiTipp) {
  const nr = Number(t.nr); const z = t.zustand || 'zu';
  if (z === 'offen') { const s = sorteVon(t); const kl = s === 'bild' || s === 'karte' ? 'bild' : s === 'gutschein' ? 'geschenk' : s;
    const m = s === 'bild' || s === 'karte' ? motivFuer(t) : null;
    const fach = m ? grafik(motivSvg(m, true), 'fach') : s === 'krampus' ? grafik(`<span class="gico">${HORN_ICO}</span>`, 'fach') : s === 'gutschein' ? grafik(`<span class="gico">${GESCHENK_ICO}</span>`, 'fach')
      : el('span', { class: 'fach', 'aria-hidden': 'true' }, ['jackpot', 'niete', 'sterne'].includes(s) ? el('span', { class: 'gross-z' }, `+${zahlS(t.sterne)}`, el('i', {}, '★')) : null);
    return el('button', { type: 'button', class: `td2 offen ${kl}`, 'data-nr': String(nr), 'aria-label': `Türchen ${nr}, offen: ${s === 'krampus' ? 'Krampus – ' + (t.titel || 'Aufgabe') : kachelTitel(t)}`, onclick: () => beiTipp(t) },
      fach, el('span', { class: 'fluegel', 'aria-hidden': 'true' }), el('span', { class: 'n', 'aria-hidden': 'true' }, String(nr)), el('span', { class: 's', 'aria-hidden': 'true' }, kachelTitel(t))); }
  const lab = { nachholen: UHR_ICO + 'nachholen', heute: 'heute · nach Etappe', bereit: 'öffnen!', morgen: MOND_ICO + 'morgen', zu: '', verfallen: 'verpasst' }[z] || '';
  const s = grafik(lab, 's', 'span');
  return el('button', { type: 'button', class: `td2 ${z}`, 'data-nr': String(nr), 'aria-label': `Türchen ${nr}, ${ZUSTAND_TEXT[z] || 'noch zu'}`, onclick: () => beiTipp(t) },
    z === 'heute' || z === 'bereit' ? grafik(SCHLEIFE_KL(z === 'bereit'), 'k-schleife-w', 'span') : null, el('span', { class: 'n', 'aria-hidden': 'true' }, String(nr)), s);
}
function blattTuer(t, kind) {
  const nacht = lernGestaltung(kind) === 'nacht'; const nr = Number(t.nr);
  const dlg = el('dialog', { class: 'adv-blatt ' + (nacht ? 'lr-abflug-nacht' : 'lr-abflug-tag'), 'aria-label': `Türchen ${nr}` });
  const zu = () => { dlg.close(); dlg.remove(); };
  dlg.addEventListener('click', (ev) => { if (ev.target === dlg) zu(); }); dlg.addEventListener('close', () => dlg.remove());
  const innen = inhaltEl(t); const dunkel = ['jackpot', 'sterne', 'karte', 'leer', 'niete'].includes(sorteVon(t));
  lernAnhaengen(dlg, el('div', { class: 'griff', 'aria-hidden': 'true' }), el('p', { class: 'ober' }, `TÜRCHEN ${nr}${t.tag ? ` · GEÖFFNET AM ${datumKurz(t.tag)}` : ''}`),
    el('h2', {}, sorteVon(t) === 'krampus' ? 'Krampus war da' : kachelTitel(t)), dunkel ? el('div', { class: 'adv-dunkel' }, innen) : innen,
    el('button', { type: 'button', class: 'knopf2', onclick: zu }, 'Schließen'));
  document.body.append(dlg); dlg.showModal(); return dlg;
}
async function lernAdventKalenderSeite(arg) {
  const [kArg, modus] = String(arg || '').split('-'); const live = viewGuard();
  const d = await lernLadeKind(kArg); if (!d || !live()) return;
  const { kind } = d; const kid = kind.id; const tok0 = store.token;
  if (!lernNeu(kind)) { lernErsetze(main, lernRahmen(kind, 'advent', el('p', { class: 'lr-karte-box' }, 'Den Adventskalender gibt es in der neuen Ansicht (Menü › Ansicht).'))); return; }
  const st = await lernAdventStand(kid, { frisch: true, immer: true }); if (!live() || store.token !== tok0) return;
  $('#title').textContent = 'Adventskalender';
  const ansage = el('p', { class: 'adv-ansage', role: 'status', 'aria-live': 'polite' });
  const kopf = el('h1', { class: 'sr-only' }, 'Adventskalender'); kopfOben(d, 'Adventskalender');
  if (!st?.aktiv || !st.tueren) {
    const t = st?.grund === 'vor_start' ? `Ab ${datumKurz(st.start)} geht nach jeder geschafften Etappe ein Türchen auf.` : st?.grund === 'vorbei' ? 'Der Adventskalender ist vorbei. Deine Gutscheine bleiben.' : 'Der Adventskalender ist gerade nicht da.';
    lernErsetze(main, lernRahmen(kind, 'advent', el('div', { class: 'lr-adv' }, kopf, el('div', { class: 'kal-held lr-adv-leer' }, el('h2', {}, 'Adventskalender'), el('p', {}, t)),
      st?.menue?.gutscheine ? el('p', {}, el('a', { href: `#/gutscheine/${kid}` }, 'Meine Gutscheine ›')) : null))); return;
  }
  const tueren = new Map((st.tueren || []).map((t) => [Number(t.nr), t]));
  const offen = (st.tueren || []).filter((t) => t.zustand === 'offen').length; const w = wartendeNr(st);
  const limit = Number(st.moeglich_heute) === 0 && geschlosseneFaellige(st);
  let h, p, banner = null;
  if (st.phase === 'nur_ansehen') { h = 'Adventskalender'; p = 'Nachholen ist vorbei. Der Kalender bleibt zum Ansehen bis 6. Januar.'; }
  else if (!w.length && offen >= 24) { h = 'Frohe Weihnachten'; p = 'Alle 24 Türchen sind offen.'; }
  else if (st.bereit) { h = 'Adventskalender'; p = `Türchen ${st.naechste_nr} ist bereit – du hast heute schon eine Etappe geschafft. Tippen und öffnen.`; }
  else if (limit) { h = 'Für heute: alles raus.'; p = `Du hast heute ${Number(st.offen_heute) || 2} Türchen geöffnet – mehr geht an einem Tag nicht.`;
    banner = el('div', { class: 'kal-banner' }, el('span', { class: 'sym', 'aria-hidden': 'true' }, '☾'), el('span', {}, el('b', {}, 'Morgen geht’s weiter. '), 'Deine Etappen zählen trotzdem – nur Türchen gibt’s höchstens 2 am Tag.')); }
  else if (w.length) { h = st.phase === 'nachholen' ? 'Frohe Weihnachten' : 'Adventskalender'; const z = w.length === 1 ? `Türchen ${w[0]} wartet.` : `Türchen ${w.slice(0, -1).join(', ')} und ${w.at(-1)} warten.`;
    p = `${z} Je geschaffte Etappe geht eins auf – höchstens 2 am Tag, das älteste zuerst.${st.phase === 'nachholen' ? ' Nachholen geht bis 6. Januar.' : ''}`; }
  else { h = 'Adventskalender'; p = 'Nach jeder geschafften Etappe geht ein Türchen auf.'; }
  const chips = el('div', { class: 'kal-status' }, el('span', {}, `${offen} offen`), w.length ? el('span', { class: 'gold' }, `${w.length} ${w.length === 1 ? 'wartet' : 'warten'}`) : null);
  const held = el('div', { class: 'kal-held' }, el('div', { class: 'licht', 'aria-hidden': 'true' }), el('p', { class: 'ober' }, datumOben(st.heute)), el('h2', {}, h), el('p', {}, p), chips);
  const tuerAuf = () => { const t0 = tueren.get(Number(st.naechste_nr)) || { nr: st.naechste_nr };
    tuerZeigen({ kindObj: kind, kindId: kid, stand: st, quelle: 'kalender', weiter: () => { lernAbschlussZu(); if (location.hash !== `#/advent/${kid}`) location.hash = `#/advent/${kid}`; else render(); } }); return t0; };
  const beiTipp = async (t) => {
    const z = t.zustand; const nr = Number(t.nr);
    if (z === 'offen') { try { const x = await lernCall('schule_advent_tuer_lesen', { lernender_id: kid, nr }); if (!live() || store.token !== tok0) return; blattTuer({ ...t, ...(x?.tuer || {}) }, kind); }
      catch { ansage.textContent = `Türchen ${nr} lässt sich gerade nicht ansehen. Versuch es gleich noch einmal.`; } return; }
    if (z === 'bereit') { tuerAuf(); return; }
    ansage.textContent = z === 'morgen' ? `Türchen ${nr} ist morgen dran.` : z === 'verfallen' ? `Türchen ${nr} ist verpasst.` : ['heute', 'nachholen'].includes(z) ? (limit ? `Heute sind schon 2 Türchen offen – Türchen ${nr} geht morgen auf.` : `Türchen ${nr} geht nach deiner nächsten Etappe auf.`) : `Türchen ${nr} ist noch zu.`;
  };
  const tafel = el('div', { class: 'tafel' }, el('div', { class: 'tafel-deko', 'aria-hidden': 'true' }),
    el('div', { class: 'tueren2', role: 'group', 'aria-label': '24 Türchen' }, ...UMORDNUNG.map((n) => kachel(tueren.get(n) || { nr: n, zustand: 'zu' }, beiTipp))));
  const legende = el('div', { class: 'legende2', 'aria-hidden': 'true' }, ...[['o', 'offen'], ['b', 'bereit'], ['h', 'heute'], ['n', 'nachholen'], ['m', 'morgen'], ['z', 'noch zu']].map(([c, t]) => el('span', {}, el('i', { class: c }), t)));
  const g = st.gutscheine || {}; const eo = (Number(g.offen) || 0) + (Number(g.tauschkarten) || 0);
  const gsKarte = st.menue?.gutscheine ? el('a', { class: 'karte2 gs-link', href: `#/gutscheine/${kid}` }, el('h2', {}, 'MEINE GUTSCHEINE'),
    el('div', { class: 'abholen-z' }, grafik(GESCHENK_ICO, 'gi', 'span'), el('span', {}, el('b', {}, eo ? `${eo} einlösbar` : 'Noch keiner offen'), g.krampus_offen ? el('small', {}, `${g.krampus_offen} vom Krampus`) : el('small', {}, 'Ansehen ›')))) : null;
  const regeln = el('div', { class: 'karte2' }, el('h2', {}, 'SO GEHT’S'), el('ul', { class: 'regel-l' }, ...['Etappe geschafft → ein Türchen geht auf.', 'Verpasst? Holst du nach – das älteste zuerst.', 'Höchstens 2 am Tag, dann braucht’s 2 Etappen.', 'Morgen-Türchen bleiben zu bis morgen.', 'Nachholen geht bis 6. Januar.'].map((x) => el('li', {}, x))));
  const seite = el('div', { class: 'lr-adv' + (lernWenigBewegung() ? '' : ' lr-adv-bewegt') }, kopf, el('div', { class: 'lr-adv-inhalt' }, el('div', {}, held, banner, ansage, tafel, legende), el('div', { class: 'seite-r' }, gsKarte, regeln)));
  lernErsetze(main, lernRahmen(kind, 'advent', seite));
  // Neu laden nach Mitternacht (Tag wechselt) bzw. wenn die Seite wieder sichtbar wird und der Tag ein anderer ist
  const tag0 = lernAdventTag(); const sicht = () => { if (!document.hidden && live() && lernAdventTag() !== tag0) render(); if (!live()) document.removeEventListener('visibilitychange', sicht); };
  document.addEventListener('visibilitychange', sicht);
  if (modus === 'oeffnen' && st.bereit) { history.replaceState(history.state, '', `#/advent/${kid}`); tuerAuf(); }
}

// ================= Meine Gutscheine (Kind) =================
async function lernAdventGutscheinSeite(arg) {
  const live = viewGuard(); const d = await lernLadeKind(arg); if (!d || !live()) return;
  const { kind } = d; const kid = kind.id; const tok0 = store.token;
  let g; try { g = await lernCall('schule_advent_gutscheine', { lernender_id: kid }); } catch { g = null; }
  if (!live() || store.token !== tok0) return;
  $('#title').textContent = 'Meine Gutscheine';
  const kopf = el('h1', { class: 'sr-only' }, 'Meine Gutscheine'); kopfOben(d, 'Meine Gutscheine');
  const ansage = el('p', { class: 'sr-only', role: 'status', 'aria-live': 'polite' });
  const liste = el('ul', { class: 'gs-liste' }); const kListe = el('ul', { class: 'gs-liste' }); const kTeil = el('div', {}, el('h2', { class: 'gs-h' }, 'VOM KRAMPUS'), kListe);
  const tauschAn = !!(LERN_ADVENT.tausch && g?.tausch?.aktiv);
  if (!g || g.aktiv === false) {
    lernErsetze(main, lernRahmen(kind, 'gutscheine', el('div', { class: 'lr-adv gs-seite' }, kopf, el('p', { class: 'gs-unter' }, 'Gerade gibt es hier nichts zu sehen.')))); return;
  }
  const sperren = new Set();
  const zeichne = () => {
    const alle = (g.gutscheine || []).slice().sort((a, b) => (a.zustand === 'offen' ? 0 : 1) - (b.zustand === 'offen' ? 0 : 1) || Number(a.nr) - Number(b.nr));
    lernErsetze(liste, ...(alle.length ? alle.map(karte) : [el('li', { class: 'gs-unter' }, 'Noch kein Gutschein. Er kommt hinter einem Türchen.')]));
    const kr = (g.krampus || []).slice().sort((a, b) => (a.zustand === 'offen' ? 0 : 1) - (b.zustand === 'offen' ? 0 : 1) || Number(a.nr) - Number(b.nr));
    lernErsetze(kListe, ...kr.map(krampusTicket)); kTeil.hidden = !kr.length;
  };
  const kopfZeile = (x, wort) => el('div', { class: 'gk' }, grafik(STERN_ICO + wort, 'gk-l', 'span'), el('span', {}, `TÜR ${x.nr}${x.getauscht ? ' · GETAUSCHT' : ''}`));
  function karte(x) {
    const tausch = x.art === 'tausch'; const ein = x.zustand === 'eingeloest'; const verbr = x.zustand === 'verbraucht';
    const fuss = el('div', { class: 'gs-fuss' });
    const li = el('li', { class: `gs2 ${x.zustand}`, 'data-id': String(x.id), ...(ein || verbr ? { 'aria-disabled': 'true' } : {}) },
      kopfZeile(x, tausch && tauschAn ? 'TAUSCHKARTE' : 'GUTSCHEIN'),
      el('div', { class: 'gs-in' }, el('h3', {}, x.titel || (tausch ? 'Tauschkarte' : 'Gutschein')), x.text ? el('p', {}, x.text) : tausch && tauschAn ? el('p', {}, 'Tausch einen deiner Gutscheine gegen einen vom Geschwister.') : null),
      el('div', { class: 'gs-perf', 'aria-hidden': 'true' }), fuss);
    if (ein) lernErsetze(fuss, el('span', { class: 'gs-status' }, `✓ Eingelöst${x.eingeloest_am ? ' am ' + datumKurz(x.eingeloest_am) : ''}`), el('span', { class: 'gs-stempel', 'aria-hidden': 'true' }, 'EINGELÖST'));
    else if (verbr) lernErsetze(fuss, el('span', { class: 'gs-status' }, '✓ Getauscht'), el('span', { class: 'gs-stempel', 'aria-hidden': 'true' }, 'VERBRAUCHT'));
    else if (tausch && tauschAn) lernErsetze(fuss, el('span', { class: 'gs-status' }, 'Gegen einen Gutschein vom Geschwister'), el('button', { type: 'button', class: 'gs-ein', onclick: () => tauschPanel(li, x) }, 'Tauschen'));
    else if (tausch) lernErsetze(fuss, el('span', { class: 'gs-status' }, 'Zeig ihn Mama oder Papa.'));
    else lernErsetze(fuss, el('button', { type: 'button', class: 'gs-ein', 'aria-label': `Eingelöst: ${x.titel || 'Gutschein'}`, onclick: () => frage(fuss, x) }, 'Eingelöst'));
    return li;
  }
  function krampusTicket(x) {
    const erl = x.zustand === 'erledigt';
    return el('li', { class: 'gs2 krampus' + (erl ? ' erledigt' : '') }, el('div', { class: 'gk' }, el('span', {}, 'KRAMPUS WAR DA'), el('span', {}, `TÜR ${x.nr}`)),
      el('div', { class: 'gs-in' }, grafik(HUF, 'kr-huf2', 'span'), el('h3', {}, x.titel || 'Aufgabe'), x.text ? el('p', {}, x.text) : null), el('div', { class: 'gs-perf', 'aria-hidden': 'true' }),
      el('div', { class: 'gs-fuss' }, el('span', { class: 'gs-status' }, erl ? '✓ Erledigt – Mama oder Papa haben abgehakt.' : '☐ Erledigt? Mama oder Papa haken ab.'))); // kein Knopf für das Kind
  }
  function frage(fuss, x) { // kurze Rückfrage in der Seite (kein confirm())
    const ja = el('button', { type: 'button', class: 'gs-ein', onclick: () => einloesen(fuss, x, ja) }, 'Ja, eingelöst');
    const nein = el('button', { type: 'button', class: 'gs-ein zweit', onclick: () => { zeichne(); liste.querySelector(`[data-id="${x.id}"] .gs-ein`)?.focus(); } }, 'Doch nicht');
    lernErsetze(fuss, el('p', { class: 'gs-frage', id: 'gsf' + x.id }, `„${x.titel || 'Gutschein'}“ schon bei Mama oder Papa eingelöst?`), ja, nein); ja.focus();
  }
  async function einloesen(fuss, x, knopf) {
    if (sperren.has(x.id)) return; sperren.add(x.id); knopf.disabled = true; knopf.setAttribute('aria-busy', 'true'); // synchron vor dem await
    try {
      const r = await lernCall('schule_advent_einloesen', { lernender_id: kid, gutschein_id: x.id });
      if (!live() || store.token !== tok0) return;
      if (r?.gutschein) Object.assign(x, r.gutschein, { zustand: r.gutschein.zustand || 'eingeloest' }); else x.zustand = 'eingeloest';
      if (r?.zaehler) g.zaehler = r.zaehler; lernAdventVergessen(kid);
      zeichne(); ansage.textContent = `„${x.titel || 'Gutschein'}“ ist eingelöst.`;
      lernCall('schule_advent_gutscheine', { lernender_id: kid }).then((n) => { if (n && live() && store.token === tok0 && n.aktiv !== false) { g = n; zeichne(); } }).catch(() => { /* bleibt */ });
    } catch (e) {
      if (!live() || store.token !== tok0) return;
      lernAnhaengen(fuss, el('p', { class: 'gs-fehler', role: 'alert' }, /nicht gefunden/.test(e.message) ? 'Den Gutschein gibt es so nicht mehr. Die Liste wird neu geladen.' : /Krampus/.test(e.message) ? 'Krampus-Aufgaben haken nur Mama oder Papa ab.' : 'Das hat gerade nicht geklappt. Versuch es gleich noch einmal.'));
      knopf.disabled = false; knopf.removeAttribute('aria-busy');
      if (/nicht gefunden/.test(e.message)) setTimeout(() => { if (live()) render(); }, 1200);
    } finally { sperren.delete(x.id); }
  }
  function tauschPanel(li, x) { // klein und abschaltbar (LERN_ADVENT.tausch und Server-Schalter advent_tausch)
    li.querySelector('.gs-tausch')?.remove();
    const meine = (g.gutscheine || []).filter((y) => y.art === 'gutschein' && y.zustand === 'offen');
    const fremd = (g.tausch?.geschwister || []).flatMap((k) => (k.gutscheine || []).map((y) => ({ ...y, von: k.name })));
    const wahl = (name, liste2, text) => el('fieldset', {}, el('legend', {}, text), ...liste2.map((y, i) => el('label', {}, el('input', { type: 'radio', name, value: String(y.id), ...(i === 0 ? { checked: true } : {}) }), `${y.titel || 'Gutschein'}${y.von ? ` (${y.von})` : ''}`)));
    const meld = el('p', { class: 'gs-fehler', role: 'alert' }); const cid = lernCid();
    if (!meine.length || !fremd.length) { li.append(el('div', { class: 'gs-tausch' }, el('p', {}, !meine.length ? 'Du hast gerade keinen offenen Gutschein zum Tauschen.' : 'Beim Geschwister ist gerade kein Gutschein offen.'))); return; }
    const los = el('button', { type: 'button', class: 'gs-ein' }, 'Jetzt tauschen'); let sp = false;
    const panel = el('div', { class: 'gs-tausch' }, wahl('mein' + x.id, meine, 'Du gibst ab:'), wahl('fremd' + x.id, fremd, 'Du bekommst:'), los, meld);
    los.addEventListener('click', async () => {
      if (sp) return; sp = true; los.disabled = true;
      const mein = Number(panel.querySelector(`input[name="mein${x.id}"]:checked`)?.value); const fr = Number(panel.querySelector(`input[name="fremd${x.id}"]:checked`)?.value);
      try { const r = await lernCall('schule_advent_tauschen', { lernender_id: kid, tauschkarte_id: x.id, mein_gutschein_id: mein, fremder_gutschein_id: fr, client_id: cid });
        if (!live() || store.token !== tok0) return;
        if (r?.getauscht === false) { meld.textContent = 'Tauschen ist gerade aus.'; return; }
        lernAdventVergessen(kid); render();
      } catch (e) { if (!live()) return; meld.textContent = String(e.message || '').replace(/^.*?…\s*/, '') || 'Das hat nicht geklappt.'; sp = false; los.disabled = false; }
    });
    li.append(panel);
  }
  zeichne();
  lernErsetze(main, lernRahmen(kind, 'gutscheine', el('div', { class: 'lr-adv gs-seite' }, kopf,
    el('p', { class: 'gs-unter' }, 'Aus deinem Adventskalender. Sie gelten, bis du sie einlöst – auch nach Weihnachten.'), ansage, liste, kTeil,
    el('p', { class: 'gs-unter klein' }, 'Hast du einen bei Mama oder Papa eingelöst, tipp auf „Eingelöst“. ', lernAdventFenster() ? el('a', { href: `#/advent/${kid}` }, 'Zum Adventskalender') : null))));
}

// ================= A4: Eltern-Seite (#/adventeltern) =================
// Übersicht beider Kinder, Gutscheine mit wer/wann (Zurückholen), Krampus Erledigt/Noch nicht, Belegung ansehen und einzelne geschlossene Türen ändern.
// Keine Zeile in „Zu tun“, kein Mischen (die Belegung spielt der Projektleiter per Paket ein). Daten nur aus Eltern-Aktionen; nichts davon wird gemerkt.
const ARTEN = [['bild', 'Bild + Satz'], ['gutschein', 'Gutschein'], ['sterne', 'Sterne'], ['karte', 'Karte'], ['krampus', 'Krampus'], ['leer', 'Leer (nur Licht)']];
const ART_KURZ = { bild: 'Bild', gutschein: 'Gutschein', sterne: 'Sterne', karte: 'Karte', krampus: 'Krampus', leer: 'leer' };
const belegTitel = (b) => (!b ? 'nur Licht' : b.art === 'sterne' ? `${b.variante === 'jackpot' ? 'Jackpot' : b.variante === 'niete' ? 'Niete' : 'Sterne'} +${zahlS(b.sterne)}`
  : b.art === 'bild' ? (b.text || LERN_ADVENT_MOTIVE[b.motiv]?.name || 'Bild') : b.art === 'leer' ? 'nur Licht' : b.titel || b.text || ART_KURZ[b.art] || '');
const vonText = (v) => { const s = String(v || ''); return s.startsWith('kind:') ? s.slice(5) || 'Kind' : s.startsWith('eltern:') ? `${s.slice(7) || 'Eltern'} (Eltern)` : s === 'kind' ? 'Kind' : s === 'eltern' ? 'Eltern' : s; };
// Mischregeln (server.md 3.9: hält die Eltern-Seite ein): Tür 6/24 Karte; Krampus nie auf 1/24 und nie zwei hintereinander (auch nicht über Tür 6 hinweg)
function regelFehler(nr, art, raster) {
  if ([6, 24].includes(nr) && art !== 'karte') return `Tür ${nr} ist fest eine Karte.`;
  if (art === 'karte' && ![6, 24].includes(nr)) return 'Karten gibt es nur hinter Tür 6 und Tür 24.';
  if (art === 'krampus') { if ([1, 24].includes(nr)) return 'Der Krampus kommt nie hinter Tür 1 oder 24.';
    const krampus = (n) => raster?.get(n)?.belegung?.art === 'krampus' || raster?.get(n)?.inhalt_beim_oeffnen?.art === 'krampus';
    const nb = [nr - 1, nr + 1, ...(nr === 5 ? [7] : nr === 7 ? [5] : nr === 23 ? [25] : [])].filter((n) => n >= 1 && n <= 24 && krampus(n));
    if (nb.length) return `Nicht zwei Krampus-Türen hintereinander (Tür ${nb.join(', ')}).`; }
  return null;
}
async function lernAdventElternSeite() {
  const live = viewGuard(); const tok0 = store.token;
  let el0, bl;
  try { [el0, bl] = await Promise.all([lernCall('schule_advent_eltern', { protokoll: 20 }), lernCall('schule_advent_belegung_lesen', {})]); }
  catch (e) { if (!live()) return; lernErsetze(main, el('div', { class: 'lr-adv-el' }, el('h1', {}, 'Adventskalender'),
    el('p', { class: 'card muted' }, /Nur Eltern/.test(e.message) ? 'Diese Seite ist nur für Mama und Papa.' : /Unbekannte Aktion/.test(e.message) ? 'Der Adventskalender ist auf dem Server noch nicht eingerichtet.' : 'Der Adventskalender lädt gerade nicht. ' + e.message))); return; }
  if (!live() || store.token !== tok0) return;
  const kinder = el0?.kinder || []; const einst = el0?.einstellung || {};
  const raster = new Map((bl?.kinder || []).map((k) => [Number(k.lernender_id), new Map((k.tueren || []).map((t) => [Number(t.nr), t]))]));
  const meldung = el('p', { class: 'meldung', role: 'status', 'aria-live': 'polite' });
  const melde = (t, fehler = false) => { meldung.textContent = t; meldung.classList.toggle('fehler', fehler); };
  const sperren = new Set();
  const gsAktion = async (knopf, x, aktion, fertigText) => {
    if (sperren.has(x.id)) return; sperren.add(x.id); knopf.disabled = true; knopf.setAttribute('aria-busy', 'true'); // synchron vor dem await
    try { const r = await lernCall('schule_advent_gutschein_eltern', { gutschein_id: x.id, aktion }); if (!live() || store.token !== tok0) return;
      melde(r?.unveraendert ? 'War schon so – nichts geändert.' : fertigText); render(); }
    catch (e) { if (!live()) return; melde(/getauscht|neu laden/.test(e.message) ? 'Der Gutschein wurde gerade getauscht – die Seite lädt neu.' : e.message, true); knopf.disabled = false; knopf.removeAttribute('aria-busy');
      if (/getauscht|neu laden/.test(e.message)) setTimeout(() => { if (live()) render(); }, 1200); }
    finally { sperren.delete(x.id); }
  };
  const knopf = (text, cls, fn, label) => { const b = el('button', { type: 'button', class: cls + ' klein', ...(label ? { 'aria-label': label } : {}) }, text); b.addEventListener('click', () => fn(b)); return b; };
  // 1. Heute je Kind
  const schalterText = einst.aktiv === 0 || einst.aktiv === '0' ? 'Für die Kinder ist der Kalender noch aus.' : String(einst.aktiv) === '2' ? 'Gerade sieht nur das Testkind den Kalender.' : null;
  const heute = el('section', { class: 'teil' }, el('div', { class: 'teil-kopf' }, el('h2', {}, 'Heute'), el('span', { class: 'zahl' }, `je Kind · höchstens ${einst.max_pro_tag || 2} Türchen am Tag`)),
    el('div', { class: 'karte' }, ...kinder.map((k) => { const l = k.lage || {}; const r = raster.get(Number(k.lernender_id));
      const offen = Number(k.offen) || [...(r?.values() || [])].filter((t) => t.offen).length;
      const zeile2 = l.grund === 'zeitzone_fehlt' ? el('span', { class: 'warn' }, 'Zeitzone fehlt – der Kalender zählt erst, wenn sie gesetzt ist.')
        : `heute ${Number(l.offen_heute) || 0} von ${einst.max_pro_tag || 2} · ${Number(l.frei_heute) > 0 ? `Türchen ${l.naechste_nr} ist bereit` : Number(l.moeglich_heute) > 0 ? 'nächstes nach einer Etappe' : 'für heute fertig'}`;
      return el('div', { class: 'heute-z' }, el('b', {}, k.name), el('div', { class: 'heute-t' }, `${offen} von 24 offen · ${k.belegt ?? '?'} belegt`, el('small', {}, zeile2),
        el('div', { class: 'punkte24', 'aria-hidden': 'true' }, ...Array.from({ length: 24 }, (_, i) => el('i', { class: r?.get(i + 1)?.offen ? 'o' : '' }))))); }),
      ...(el0?.ohne_teilnahme || []).map((k) => el('div', { class: 'heute-z' }, el('b', {}, k.name), el('div', { class: 'heute-t' }, 'noch nichts belegt'))),
      !kinder.length && !(el0?.ohne_teilnahme || []).length ? el('p', { class: 'ab-leer' }, 'Noch kein Kind mit Belegung.') : null),
    schalterText ? el('p', { class: 'meldung' }, schalterText) : null);
  // 2. Gutscheine (wer was wann) und 3. Krampus
  const gsZeilen = [], krZeilen = [];
  for (const k of kinder) for (const x of k.gutscheine || []) {
    const titel = x.titel || (x.art === 'tausch' ? 'Tauschkarte' : 'Gutschein');
    if (x.art === 'krampus') { const erl = x.zustand === 'erledigt';
      krZeilen.push(el('div', { class: 'ab-z krampus-z' }, el('div', {}, el('div', { class: 'wer' }, el('b', {}, k.name), ` · Tür ${x.nr} · Krampus`), el('div', { class: 'was' + (erl ? ' durch' : '') }, titel),
        erl ? el('div', { class: 'wer' }, `erledigt${x.erledigt_am ? ' am ' + zeitpunkt(x.erledigt_am) : ''}`) : null),
        el('div', { class: 'knr' }, erl ? knopf('Noch nicht', 'secondary', (b) => gsAktion(b, x, 'noch_nicht', `„${titel}“ ist wieder offen.`), `Noch nicht: ${k.name} – ${titel}`)
          : knopf('Erledigt ✓', 'primary', (b) => gsAktion(b, x, 'erledigt', `„${titel}“ ist erledigt.`), `Erledigt: ${k.name} – ${titel}`)))); continue; }
    const ein = x.zustand === 'eingeloest', verbr = x.zustand === 'verbraucht';
    const info = ein ? `${vonText(x.eingeloest_von) || k.name} hat eingelöst${x.eingeloest_am ? ' am ' + zeitpunkt(x.eingeloest_am) : ''}` : verbr ? `beim Tauschen verbraucht${x.verbraucht_am ? ' am ' + zeitpunkt(x.verbraucht_am) : ''}`
      : `offen${x.zurueckgeholt_am ? ` · zurückgeholt am ${zeitpunkt(x.zurueckgeholt_am)}` : ''}${x.getauscht ? ' · getauscht' : ''}`;
    gsZeilen.push({ ein, z: el('div', { class: 'ab-z' }, el('div', {}, el('div', { class: 'wer' }, el('b', {}, k.name), ` · Tür ${x.nr}${x.art === 'tausch' ? ' · Tauschkarte' : ''}`), el('div', { class: 'was' + (ein || verbr ? ' durch' : '') }, titel), el('div', { class: 'wer' }, info)),
      el('div', { class: 'knr' }, ein ? knopf('Zurückholen', 'secondary', (b) => gsAktion(b, x, 'zurueckholen', `„${titel}“ ist wieder offen.`), `Zurückholen: ${k.name} – ${titel}`)
        : verbr ? null : knopf('Eingelöst', 'secondary', (b) => gsAktion(b, x, 'einloesen', `„${titel}“ ist eingelöst.`), `Als eingelöst markieren: ${k.name} – ${titel}`))) });
  }
  gsZeilen.sort((a, b) => (a.ein ? 1 : 0) - (b.ein ? 1 : 0));
  const gutscheine = el('section', { class: 'teil' }, el('div', { class: 'teil-kopf' }, el('h2', {}, 'Gutscheine'), el('span', { class: 'zahl' }, 'wer was wann eingelöst hat')),
    el('div', { class: 'karte' }, ...(gsZeilen.length ? gsZeilen.map((x) => x.z) : [el('p', { class: 'ab-leer' }, 'Noch kein Gutschein geöffnet.')])));
  const krampus = el('section', { class: 'teil' }, el('div', { class: 'teil-kopf' }, el('h2', {}, 'Vom Krampus'), el('span', { class: 'zahl' }, 'nur ihr hakt ab')),
    el('div', { class: 'karte' }, ...(krZeilen.length ? krZeilen : [el('p', { class: 'ab-leer' }, 'Noch keine Krampus-Aufgabe.')])));
  // 4. Belegung: Raster je Kind, geschlossene Türen änderbar
  const ids = [...raster.keys()]; let wahl = ids[0];
  const name = (id) => kinder.find((k) => Number(k.lernender_id) === id)?.name || (bl?.kinder || []).find((k) => Number(k.lernender_id) === id)?.name || `Kind ${id}`;
  const seg = el('div', { class: 'seg', role: 'group', 'aria-label': 'Kind wählen' });
  const rasterEl = el('div', {});
  const zeichneRaster = () => {
    lernErsetze(seg, ...ids.map((id) => el('button', { type: 'button', 'aria-pressed': String(id === wahl), onclick: () => { wahl = id; zeichneRaster(); } }, name(id))));
    const r = raster.get(wahl); if (!r) { lernErsetze(rasterEl, el('p', { class: 'ab-leer' }, 'Keine Belegung.')); return; }
    lernErsetze(rasterEl, el('div', { class: 'raster-kopf' }, el('h3', {}, name(wahl)), el('small', {}, 'Tippe eine geschlossene Tür an, um sie zu ändern.')),
      el('div', { class: 'raster' }, ...Array.from({ length: 24 }, (_, i) => { const nr = i + 1; const t = r.get(nr) || { nr }; const b = t.offen ? (t.inhalt_beim_oeffnen || t.belegung) : t.belegung;
        const cls = 'platz' + (t.offen ? ' offen' : '') + (!b || b.art === 'leer' ? ' leer' : '') + (b?.art === 'krampus' ? ' krampus' : '') + ([6, 24].includes(nr) ? ' fest' : '');
        return el('button', { type: 'button', class: cls, 'aria-label': `Tür ${nr}: ${b ? ART_KURZ[b.art] || b.art : 'leer'}${b && belegTitel(b) ? ' – ' + belegTitel(b) : ''}${t.offen ? ', schon offen' : ', ändern'}`,
          onclick: () => (t.offen ? melde(`Tür ${nr} ist schon offen – sie bleibt, wie sie ist.`) : bearbeiten(nr, t)) },
          el('span', { class: 'nr' }, String(nr)), el('span', { class: 'art' }, b ? ART_KURZ[b.art] || b.art : 'leer'), el('span', { class: 't' }, belegTitel(b))); })),
      el('div', { class: 'raster-fuss' }, el('span', {}, '✓ = schon offen'), el('span', {}, 'Goldrand = Tür 6 und 24 (Karte)')));
  };
  function bearbeiten(nr, t) {
    const b = t.belegung || { art: 'leer' }; const r = raster.get(wahl);
    const dlg = el('dialog', { class: 'adv-el-blatt', 'aria-label': `Tür ${nr} ändern` });
    const zu = () => { dlg.close(); dlg.remove(); }; dlg.addEventListener('close', () => dlg.remove());
    let art = [6, 24].includes(nr) ? 'karte' : b.art || 'leer'; let motiv = b.motiv || null; let beide = false;
    const fehler = el('p', { class: 'meldung fehler', role: 'alert' });
    const titelI = el('input', { type: 'text', maxlength: '80', value: b.titel || '' }); const textI = el('textarea', { maxlength: '300' }, b.text || '');
    const sterneI = el('input', { type: 'number', min: '0', max: '5000', step: '1', value: String(b.sterne ?? 0), inputmode: 'numeric' });
    const variante = el('div', { class: 'arten' }); const motivWahl = el('div', { class: 'motiv-wahl' });
    const felder = el('div', {});
    const artWahl = el('div', { class: 'arten', role: 'radiogroup', 'aria-label': 'Art' }, ...ARTEN.map(([a, l]) => { const f = regelFehler(nr, a, r);
      const inp = el('input', { type: 'radio', name: 'art' + nr, value: a, ...(a === art ? { checked: true } : {}), ...(f ? { disabled: true } : {}) });
      inp.addEventListener('change', () => { art = a; zeige(); }); return el('label', { title: f || '' }, inp, l); }));
    const feld = (label, inp, hilfe) => el('div', { class: 'feld' }, el('label', {}, label, inp), hilfe ? el('small', {}, hilfe) : null);
    const varWahl = (liste, akt) => lernErsetze(variante, ...liste.map(([v, l]) => { const inp = el('input', { type: 'radio', name: 'var' + nr, value: v, ...(v === akt ? { checked: true } : {}) });
      inp.addEventListener('change', () => { if (art === 'sterne') sterneI.value = v === 'jackpot' ? '1111' : v === 'niete' ? '1' : sterneI.value; }); return el('label', {}, inp, l); }));
    const zeigeMotive = (liste) => lernErsetze(motivWahl, ...liste.map((m) => { const k = el('button', { type: 'button', class: 'mw', 'aria-pressed': String(m === motiv), 'aria-label': LERN_ADVENT_MOTIVE[m].name, title: LERN_ADVENT_MOTIVE[m].name,
      onclick: () => { motiv = motiv === m ? null : m; zeigeMotive(liste); motivWahl.querySelector(`[aria-label="${CSS.escape(LERN_ADVENT_MOTIVE[m].name)}"]`)?.focus(); } }); k.innerHTML = motivSvg(m, true); return k; }));
    const sterneZ = el('div', { class: 'sterne-z' }, el('button', { type: 'button', class: 'secondary', 'aria-label': 'Weniger Sterne', onclick: () => { sterneI.value = String(Math.max(0, (Number(sterneI.value) || 0) - 10)); } }, '−'), sterneI,
      el('button', { type: 'button', class: 'secondary', 'aria-label': 'Mehr Sterne', onclick: () => { sterneI.value = String(Math.min(5000, (Number(sterneI.value) || 0) + 10)); } }, '+'),
      ...[0, 50, 100, 500].map((n) => el('button', { type: 'button', class: 'secondary klein', onclick: () => { sterneI.value = String(n); } }, String(n))));
    const schalter = el('button', { type: 'button', class: 'schalter', role: 'switch', 'aria-checked': 'false', 'aria-label': 'Beide am selben Tag' }, el('i', {}));
    schalter.addEventListener('click', () => { beide = !beide; schalter.setAttribute('aria-checked', String(beide)); });
    function zeige() {
      const kids = [];
      if (art === 'sterne') { varWahl([['normal', 'normal'], ['jackpot', 'Jackpot'], ['niete', 'Niete (+1 Trost)']], b.art === 'sterne' ? b.variante || 'normal' : 'normal'); kids.push(el('div', { class: 'feld' }, el('span', {}, 'Sorte'), variante)); }
      if (art === 'gutschein') { varWahl([['normal', 'Gutschein'], ['tausch', 'Tauschkarte']], b.art === 'gutschein' ? b.variante || 'normal' : 'normal'); kids.push(el('div', { class: 'feld' }, el('span', {}, 'Sorte'), variante)); }
      if (['gutschein', 'krampus', 'karte', 'bild'].includes(art)) kids.push(feld(art === 'krampus' ? 'Aufgabe (Titel)' : 'Titel', titelI, art === 'gutschein' || art === 'krampus' ? 'Pflicht, höchstens 80 Zeichen' : 'freiwillig, höchstens 80 Zeichen'));
      if (art !== 'leer') kids.push(feld(art === 'bild' || art === 'karte' ? 'Satz von Mama und Papa' : 'Text', textI, 'höchstens 300 Zeichen'));
      if (art === 'bild' || art === 'karte') { zeigeMotive(art === 'karte' ? ['nikolaus', 'heiligabend', ...MOTIVE_ALLGEMEIN] : MOTIVE_ALLGEMEIN); kids.push(el('div', { class: 'feld' }, el('span', {}, art === 'bild' ? 'Motiv (Pflicht)' : 'Motiv'), motivWahl)); }
      kids.push(el('div', { class: 'feld' }, el('label', { for: 'st' + nr }, 'Sterne beim Öffnen (0–5000)'), sterneZ)); sterneI.id = 'st' + nr;
      lernErsetze(felder, ...kids);
    }
    const speichern = el('button', { type: 'button', class: 'primary' }, 'Speichern'); let sp = false;
    speichern.addEventListener('click', async () => {
      if (sp) return; fehler.textContent = '';
      const v = felder.querySelector(`input[name="var${nr}"]:checked`)?.value || null; const n = Number(sterneI.value);
      const tuer = { nr, art };
      if (art === 'sterne' || art === 'gutschein') tuer.variante = v || 'normal';
      if (['gutschein', 'krampus', 'karte', 'bild'].includes(art) && titelI.value.trim()) tuer.titel = titelI.value.trim();
      if (art !== 'leer' && textI.value.trim()) tuer.text = textI.value.trim();
      if ((art === 'bild' || art === 'karte') && motiv) tuer.motiv = motiv;
      if (art !== 'leer') tuer.sterne = n;
      const f = regelFehler(nr, art, r) || (!Number.isInteger(n) || n < 0 || n > 5000 ? 'Sterne: ganze Zahl von 0 bis 5000.' : null) || (art === 'bild' && !motiv ? 'Bitte ein Motiv wählen.' : null)
        || (['gutschein', 'krampus'].includes(art) && !tuer.titel ? 'Bitte einen Titel eingeben.' : null);
      if (f) { fehler.textContent = f; return; }
      sp = true; speichern.disabled = true; speichern.setAttribute('aria-busy', 'true'); // synchron vor dem await
      const daten = beide ? { lernender_ids: ids, tueren: [tuer], nur_geschlossene: true } : { lernender_id: wahl, tueren: [tuer] };
      try { const x = await lernCall('schule_advent_belegung_setzen', daten); if (!live() || store.token !== tok0) return;
        const ueber = (x?.kinder || []).filter((k) => (k.uebersprungen_offen || []).length).map((k) => name(Number(k.lernender_id)));
        zu(); melde(`Tür ${nr} gespeichert${beide ? ' für beide' : ''}.${ueber.length ? ` Bei ${ueber.join(', ')} war sie schon offen und bleibt.` : ''}`); render(); }
      catch (e) { if (!live()) return; fehler.textContent = /schon offen/.test(e.message) ? 'Diese Tür ist inzwischen schon offen – sie bleibt, wie sie ist.' : e.message; sp = false; speichern.disabled = false; speichern.removeAttribute('aria-busy'); }
    });
    zeige();
    lernAnhaengen(dlg, el('div', { class: 'griff', 'aria-hidden': 'true' }), el('h2', {}, `Tür ${nr} · ${name(wahl)}`), el('p', { class: 'unter' }, [6, 24].includes(nr) ? 'Tür 6 und 24 sind fest Karten – dazu dürfen Sterne.' : 'Nur geschlossene Türen lassen sich ändern.'),
      el('div', { class: 'feld' }, el('span', {}, 'Art'), artWahl), felder,
      ids.length > 1 ? el('div', { class: 'schalter-z' }, el('span', {}, el('b', {}, 'Beide am selben Tag'), el('small', {}, 'Gleicher Inhalt hinter dieser Tür bei allen Kindern (schon offene bleiben).')), schalter) : null,
      fehler, el('div', { class: 'adv-el-fuss' }, speichern, el('button', { type: 'button', class: 'secondary', onclick: zu }, 'Abbrechen')));
    document.body.append(dlg); dlg.showModal(); dlg.querySelector('input:checked')?.focus();
  }
  zeichneRaster();
  const belegung = el('section', { class: 'teil' }, el('div', { class: 'teil-kopf' }, el('h2', {}, 'Türchen'), el('span', { class: 'zahl' }, 'Belegung ansehen, einzelne Türen ändern'), el('div', { class: 'rechts' }, seg)), el('div', { class: 'karte' }, rasterEl));
  const prot = (el0?.protokoll || []).length ? el('details', { class: 'karte adv-prot teil' }, el('summary', {}, 'Was zuletzt passiert ist'),
    el('ul', {}, ...(el0.protokoll || []).map((p) => el('li', {}, `${zeitpunkt(p.am)} · ${name(Number(p.lernender_id))} · ${{ oeffnen: 'Türchen geöffnet', einloesen: 'Gutschein eingelöst', eltern_einloesen: 'als eingelöst markiert', eltern_zurueckholen: 'zurückgeholt', eltern_erledigt: 'Krampus erledigt', eltern_noch_nicht: 'Krampus noch nicht', tausch: 'getauscht', getauscht_von_geschwister: 'vom Geschwister getauscht', belegung: 'Belegung geändert' }[p.aktion] || p.aktion}${p.nr ? ` · Tür ${p.nr}` : ''}`)))) : null;
  lernErsetze(main, el('div', { class: 'lr-adv-el' }, el('h1', {}, 'Adventskalender'), el('p', { class: 'unter' }, `Türchen ${einst.start ? datumKurz(einst.start) : '1.12.'} bis 24.12., nachholen bis ${einst.nachholen_bis ? datumKurz(einst.nachholen_bis) : '6.1.'}`), meldung,
    el('div', { class: 'el-zwei' }, el('div', {}, heute, gutscheine, krampus), el('div', {}, belegung)), prot));
}


const FEST_LICHT = ['#FFC94A', '#FF5A5F', '#FFF3D1', '#3DDC84']; // Gold · Rot · Warmweiß · Grün – feste Folge, keine Würfelei
const zz = (n) => { const x = Math.sin(n * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); }; // fester Zufall je Zahl
const f1 = (v) => Math.round(v * 10) / 10;
// ---------- Bausteine (Einheiten: Pin-Kopf mit Radius 10, Mitte 0/0) ----------
function festDefs(u, nacht) {
  const fell = nacht ? ['#FFFFFF', '#C9D6EA'] : ['#FFFFFF', '#C7D3E3'];
  return `<linearGradient id="${u}kegel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF5A6B"/><stop offset=".55" stop-color="#E5243B"/><stop offset="1" stop-color="#B3122B"/></linearGradient>
    <radialGradient id="${u}bommel" cx=".38" cy=".34" r=".7"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".6" stop-color="#F3F6FA"/><stop offset="1" stop-color="${fell[1]}"/></radialGradient>
    <linearGradient id="${u}eis" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".45" stop-color="#DDF0FB"/><stop offset="1" stop-color="#A9D7F2" stop-opacity=".75"/></linearGradient>
    <linearGradient id="${u}schnee" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#F1F7FC"/></linearGradient>
    ${FEST_LICHT.map((c, i) => `<radialGradient id="${u}gl${i}"><stop offset="0" stop-color="${c}" stop-opacity="${nacht ? .95 : .7}"/><stop offset=".35" stop-color="${c}" stop-opacity="${nacht ? .45 : .28}"/><stop offset="1" stop-color="${c}" stop-opacity="0"/></radialGradient>
    <radialGradient id="${u}bi${i}" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".35" stop-color="${c}"/><stop offset="1" stop-color="${dunkler(c, .32)}"/></radialGradient>`).join('')}`;
}
function dunkler(hex, k) { const n = parseInt(hex.slice(1), 16); const r = (n >> 16) & 255, g = (n >> 8) & 255, b = n & 255; const f = (v) => Math.round(v * (1 - k)).toString(16).padStart(2, '0'); return '#' + f(r) + f(g) + f(b); }
const bogen = (r, a0, a1) => { const p = (a) => [f1(Math.cos(a * Math.PI / 180) * r), f1(Math.sin(a * Math.PI / 180) * r)]; const [x0, y0] = p(a0), [x1, y1] = p(a1); return `M${x0} ${y0} A${r} ${r} 0 0 1 ${x1} ${y1}`; };

// Mütze: sitzt mit dem Fellrand auf dem oberen Kopfrand, Zipfel fällt nach links (Abzeichen sitzen rechts oben).
function festMuetze(u, x, y, r, rot, k = 1, nacht = false) {
  const s = (r / 10) * k; const schatten = nacht ? 'rgba(0,0,0,.35)' : 'rgba(40,10,20,.22)';
  return `<g transform="translate(${f1(x)} ${f1(y)}) rotate(${f1(rot)}) scale(${f1(s * 100) / 100})">
    <path d="${bogen(8.3, -140, -40)}" stroke="${schatten}" stroke-width="1.6" fill="none" stroke-linecap="round"/><g transform="translate(0 1.1)">
    <path d="M7.4 -9.6 C7.2 -16 4.6 -22.2 -.6 -24.6 C-5.8 -26.8 -11 -25.2 -14 -20.6 C-11 -21.6 -7.2 -21 -4.2 -18.6 C-6 -15.4 -7.1 -12.4 -7.4 -9.6 Z" fill="url(#${u}kegel)"/>
    <path d="M7.4 -9.6 C7.2 -16 4.6 -22.2 -.6 -24.6 C2.6 -20.4 3.8 -15 3.8 -9.6 Z" fill="#9E0F27" opacity=".55"/>
    <path d="M-14 -20.6 C-11 -21.6 -7.2 -21 -4.2 -18.6 C-7 -19.4 -10.4 -19.8 -14 -20.6 Z" fill="#7E0B1F" opacity=".7"/>
    <path d="M-1.2 -24.4 C-6 -26.4 -10.6 -25 -13.4 -21.2 C-10.2 -23.4 -6 -24.2 -2.4 -23.2 Z" fill="#FF9AA5" opacity=".75"/>
    </g><path d="${bogen(10, -142, -38)}" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path d="${bogen(8.6, -136, -44)}" stroke="${nacht ? '#B8C7DD' : '#C7D3E3'}" stroke-width="1.3" fill="none" stroke-linecap="round"/>
    ${[-128, -108, -88, -68, -50].map((a) => `<circle cx="${f1(Math.cos(a * Math.PI / 180) * 11.7)}" cy="${f1(Math.sin(a * Math.PI / 180) * 11.7)}" r=".95" fill="#fff"/>`).join('')}
    <circle cx="-14.6" cy="-18.3" r="3.5" fill="url(#${u}bommel)"/><circle cx="-13.4" cy="-16.5" r="1.4" fill="${nacht ? '#B8C7DD' : '#C7D3E3'}" opacity=".6"/></g>`;
}
// Schneehäubchen für kleine Pins (statt Mütze): weißer Bogen mit zwei Tropfen, Schattenkante unten
function festHaeubchen(x, y, r, nacht) {
  const s = r / 10;
  return `<g transform="translate(${f1(x)} ${f1(y)}) scale(${f1(s * 100) / 100})"><path d="${bogen(10.4, -152, -28)}" stroke="${nacht ? '#8FA6C2' : '#A9C3D6'}" stroke-width="3.6" fill="none" stroke-linecap="round" transform="translate(0 .9)"/>
    <path d="${bogen(10.4, -152, -28)}" stroke="#fff" stroke-width="3.4" fill="none" stroke-linecap="round"/><path d="M-4.6 -9 q.7 3.2 1.6 0Z M3.2 -9.6 q.8 4.2 1.7 0Z" fill="#fff"/></g>`;
}
// Tanne (Einheit: Höhe ~22, Fuß bei 0)
function festTanne(x, y, k) {
  return `<g transform="translate(${f1(x)} ${f1(y)}) scale(${f1(k * 100) / 100})"><ellipse cx="0" cy=".6" rx="7" ry="1.6" fill="#0B2A1A" opacity=".18"/><rect x="-1.4" y="-2.4" width="2.8" height="3" rx=".6" fill="#7A4A26"/>
    <path d="M0 -21 L5.4 -13.4 Q2.6 -12.6 0 -13 Q-2.6 -12.6 -5.4 -13.4 Z M0 -16 L7.2 -7.6 Q3.4 -6.6 0 -7 Q-3.4 -6.6 -7.2 -7.6 Z M0 -10.4 L9 -1.8 Q4.4 -.6 0 -1 Q-4.4 -.6 -9 -1.8 Z" fill="#1F7A4C"/>
    <path d="M0 -21 L5.4 -13.4 Q2.6 -12.6 0 -13 Z M0 -16 L7.2 -7.6 Q3.4 -6.6 0 -7 Z M0 -10.4 L9 -1.8 Q4.4 -.6 0 -1 Z" fill="#11532F"/>
    <path d="M-5.4 -13.4 Q-2.6 -12.6 0 -13 M-7.2 -7.6 Q-3.4 -6.6 0 -7 M-9 -1.8 Q-4.4 -.6 0 -1" stroke="#E9F6EF" stroke-width="1.1" fill="none" stroke-linecap="round"/>
    <circle cx="-2.6" cy="-9.2" r="1.1" fill="#FF5A5F"/><circle cx="3" cy="-4" r="1.1" fill="#FFC94A"/><circle cx="-3.6" cy="-3.2" r="1" fill="#FFF3D1"/>
    <path d="M0 -24.6 l1.1 2.3 2.5 .3 -1.9 1.7 .6 2.5 -2.3 -1.3 -2.3 1.3 .6 -2.5 -1.9 -1.7 2.5 -.3z" fill="#FFC94A"/><path d="M0 -24.6 l1.1 2.3 2.5 .3 -1.9 1.7 .6 2.5 -2.3 -1.3z" fill="#E09E16"/></g>`;
}
// Geschenk in 2,5D: Vorderseite, Seite im Schatten, Deckel, Band, Schleife
function festPaket(x, y, farbe, band, k) {
  const d = dunkler(farbe, .3);
  return `<g transform="translate(${f1(x)} ${f1(y)}) scale(${f1(k * 100) / 100})"><ellipse cx="1.4" cy=".4" rx="7.4" ry="1.4" fill="#000" opacity=".14"/>
    <path d="M-5 -8 H5 V0 H-5Z" fill="${farbe}"/><path d="M5 -8 L7.6 -9.6 V-1.6 L5 0Z" fill="${d}"/><path d="M-5.6 -10.4 H5.6 L8.2 -12 H-3Z" fill="${dunkler(farbe, -.25 > 0 ? 0 : .08)}"/><path d="M-5.6 -10.4 H5.6 V-8 H-5.6Z" fill="${farbe}"/><path d="M5.6 -10.4 L8.2 -12 V-9.6 L5.6 -8Z" fill="${d}"/>
    <path d="M-1 -10.4 H1 V0 H-1Z" fill="${band}"/><path d="M1 -10.4 L3.4 -12 H5.2 L2.4 -10.4Z" fill="${band}" opacity=".85"/>
    <path d="M.2 -12.2 C-3.6 -16.4 -6.6 -12.6 -1.2 -11.6 Z M.2 -12.2 C3.8 -16.6 7 -13 1.6 -11.6 Z" fill="${band}"/><circle cx=".2" cy="-11.9" r="1.1" fill="${dunkler(band, .2)}"/></g>`;
}
// Schlitten mit zwei Rentieren als klare Scherenschnitt-Illustration (Blick nach rechts, Ursprung Mitte)
function festSchlitten(nacht, k) {
  const fell = nacht ? '#E2C9A0' : '#4A2E1F', fellS = nacht ? '#B8996E' : '#2E1B12', geweih = nacht ? '#F6E7C8' : '#8A5A33', gold = '#F2C14E';
  const tier = (x, y, phase) => `<g transform="translate(${x} ${y})">
    <path d="M-9 1.2 C-12 2.6 -15 3 -18 ${phase ? 1.8 : 2.6} M-8 2.4 C-10 4.8 -12.6 6 -15.4 ${phase ? 6.8 : 6}" stroke="${fellS}" stroke-width="1.7" fill="none" stroke-linecap="round"/>
    <path d="M7 2.4 C9.6 3.4 12.6 3.4 15.6 ${phase ? 1.6 : 2.4} M6.4 3.4 C8.4 5.6 11 6.8 13.4 ${phase ? 8 : 7.2}" stroke="${fellS}" stroke-width="1.7" fill="none" stroke-linecap="round"/>
    <path d="M-10.4 -.4 C-10.4 -4.6 -5 -6 1 -6 C6 -6 9 -4.8 10.8 -2.2 C12.4 -5 14 -8.4 15.4 -11.6 C16.2 -13.6 18.6 -14.4 20.6 -13 C22 -12 23.4 -11.6 24.6 -10.6 C25.6 -9.8 25 -8.6 23.8 -8.6 C22 -8.6 20.6 -8.6 19.4 -9 C18 -6.6 16 -2.4 13.2 .8 C11.2 3.2 7.4 4 2 4 C-5 4 -10.4 3.4 -10.4 -.4 Z" fill="${fell}"/>
    <path d="M-10.4 -.4 C-10.4 1.8 -6 3.6 2 3.6 C6.6 3.6 10 3 12.2 1.4 C10 2 6 2.2 2 2.2 C-4 2.2 -8.6 1.6 -10.4 -.4Z" fill="${fellS}" opacity=".7"/>
    <path d="M-10.2 -1.6 l-3.4 -2.6 1.2 3.8z" fill="${fell}"/><path d="M18.4 -13.2 l-2.4 -2.6 3.4 1.2z" fill="${fellS}"/>
    <path d="M19.4 -14 C18.8 -17.6 17 -19.6 14.8 -21 M17.8 -16.8 l-3 .4 M16.4 -19 l-1.4 -2.4 M20.6 -14 C21.6 -17.4 23.4 -19.2 25.4 -20.2 M22.4 -17.4 l2.6 -.6" stroke="${geweih}" stroke-width="1.15" fill="none" stroke-linecap="round"/>
    <circle cx="21.4" cy="-11.4" r=".75" fill="${nacht ? '#3A2418' : '#F6E7C8'}"/>
    <path d="M9.6 -4.4 C11 -3.4 12.4 -3 13.8 -3.6" stroke="${gold}" stroke-width="1.3" fill="none"/><circle cx="12.2" cy="-2.4" r="1.2" fill="${gold}"/></g>`;
  return `<g transform="scale(${k}) translate(-34 2)">
    <g fill="#FFE27A">${[[-30, 2, 1.2, .9], [-38, 5, .9, .7], [-46, 3, .7, .5], [-54, 7, .6, .35], [-25, 8, .7, .6], [-60, 2, .5, .25]].map(([x, y, r, o]) => `<circle cx="${x}" cy="${y}" r="${r}" opacity="${o}"/>`).join('')}<path d="M-34 -2 l.8 2 2 .8 -2 .8 -.8 2 -.8 -2 -2 -.8 2 -.8z" opacity=".9"/></g>
    <path d="M14 -1 C22 -3 30 -4 38 -3 M38 -3 C46 -4 54 -7 62 -8" stroke="${gold}" stroke-width=".9" fill="none" opacity=".95"/>
    ${tier(44, 0, 0)}${tier(70, -6, 1)}
    <path d="M-9 -3 C-11 -10 -6 -14.6 -1.6 -12.6 C1 -14.8 5 -12.4 4 -3 Z" fill="${nacht ? '#C08A55' : '#8A5A33'}"/><path d="M-1.6 -12.6 C1 -14.8 5 -12.4 4 -3 L1.4 -3 C2.4 -8 1 -11.4 -1.6 -12.6Z" fill="#000" opacity=".2"/>
    <rect x="-6.6" y="-17.4" width="6" height="5.6" rx=".8" fill="#3DDC84" transform="rotate(-10 -3.6 -14.6)"/><rect x="-4.4" y="-17.6" width="1.4" height="5.8" fill="#FFF3D1" transform="rotate(-10 -3.6 -14.6)"/>
    <rect x=".4" y="-16.4" width="5" height="4.6" rx=".8" fill="#FFC94A" transform="rotate(8 2.9 -14.1)"/><rect x="2.3" y="-16.6" width="1.2" height="4.8" fill="#E5243B" transform="rotate(8 2.9 -14.1)"/>
    <path d="M-15 -11 C-17.6 -12.6 -19.4 -9.6 -17 -8.2 C-15.4 -7.4 -14 -8.6 -14.2 -10 L-14 2.6 C-14 5 -12.6 6.4 -10 6.4 H8.4 C11.8 6.4 13.4 3.8 13.4 0 V-3 H-6 C-9.4 -3 -10.6 -5.4 -10.8 -8.6 C-11 -11.6 -12.8 -12.6 -15 -11 Z" fill="#E5243B"/>
    <path d="M-14 2.6 C-14 5 -12.6 6.4 -10 6.4 H8.4 C11.8 6.4 13.4 3.8 13.4 0 V1 C12 3.6 10.4 4.4 8 4.4 H-10 C-12 4.4 -13.4 3.6 -14 2.6Z" fill="#9E0F27"/>
    <path d="M-12.6 -8.6 C-12.4 -10.4 -11.6 -11 -10.8 -9.6" stroke="#FF9AA5" stroke-width=".8" fill="none" stroke-linecap="round"/><path d="M-6 -3 H13.4" stroke="${gold}" stroke-width="1.2"/>
    <path d="M-10 6.4 V10 M6 6.4 V10" stroke="${gold}" stroke-width="1.2"/><path d="M-17 10 H14 C18.6 10 20.4 7.6 20 5.2 C19.6 3.4 17.6 3.6 17.8 5.2" stroke="${gold}" stroke-width="1.6" fill="none" stroke-linecap="round"/></g>`;
}
// Lichterkette: echtes Kabel (Kettenlinie), Fassungen, Glühbirnen, weiches Leuchten in 3 Gruppen (3 animierte Knoten)
function festLichterkette(u, anf, ende, y0, s, nacht) {
  const n = Math.max(2, Math.round((ende - anf) / (92 * s))); const w = (ende - anf) / n; const kabel = [], birnen = [], glanz = [[], [], []];
  let d = `M${f1(anf)} ${f1(y0)}`; let idx = 0;
  for (let i = 0; i < n; i++) {
    const a = anf + i * w, b = a + w, sag = (17 + (i % 2) * 3) * s;
    const c1 = [a + w * .28, y0 + sag * 1.33], c2 = [b - w * .28, y0 + sag * 1.33];
    d += ` C${f1(c1[0])} ${f1(c1[1])} ${f1(c2[0])} ${f1(c2[1])} ${f1(b)} ${f1(y0)}`;
    const P = (t) => { const m = 1 - t; return [m * m * m * a + 3 * m * m * t * c1[0] + 3 * m * t * t * c2[0] + t * t * t * b, m * m * m * y0 + 3 * m * m * t * c1[1] + 3 * m * t * t * c2[1] + t * t * t * y0]; };
    for (const t of [.22, .41, .59, .78]) {
      const [x, y] = P(t), [x2, y2] = P(t + .01); const tang = Math.atan2(y2 - y, x2 - x) * 180 / Math.PI; const c = idx % 4; const g = idx % 3; idx++;
      const kipp = f1(tang * .55 + (zz(idx) - .5) * 14);
      glanz[g].push(`<circle cx="${f1(x)}" cy="${f1(y + 8.5 * s)}" r="${f1((nacht ? 13 : 9) * s)}" fill="url(#${u}gl${c})"/>`);
      birnen.push(`<g transform="translate(${f1(x)} ${f1(y)}) rotate(${kipp}) scale(${f1(s * 1.22 * 100) / 100})"><rect x="-1.7" y="-.6" width="3.4" height="3.6" rx=".7" fill="${nacht ? '#4B6B57' : '#24402F'}"/><path d="M-1.7 .6 H1.7 M-1.7 1.8 H1.7" stroke="${nacht ? '#6F927C' : '#3E6450'}" stroke-width=".5"/>
        <path d="M-2.3 3 C-3.4 5 -3.6 8.6 0 11.2 C3.6 8.6 3.4 5 2.3 3 Z" fill="url(#${u}bi${c})"/><ellipse cx="-1" cy="6" rx=".7" ry="1.6" fill="#fff" opacity=".8" transform="rotate(14 -1 6)"/></g>`);
    }
  }
  kabel.push(`<path d="${d}" stroke="${nacht ? '#5E7D68' : '#24402F'}" stroke-width="${f1(1.7 * s)}" fill="none" stroke-linecap="round"/><path d="${d}" stroke="${nacht ? '#9FC0AA' : '#4E7A62'}" stroke-width="${f1(.5 * s)}" fill="none" transform="translate(0 ${f1(-.5 * s)})" opacity=".8"/>`);
  return `<g class="fk">${glanz.map((g, i) => `<g class="fk-glanz fk${i}">${g.join('')}</g>`).join('')}${kabel.join('')}${birnen.join('')}</g>`;
}
// Schneehaube mit Volumen: Körper, Schattenkante, Glanz oben, Eiszapfen an den tiefsten Stellen
function festHaube(u, x0, x1, y0, tiefe, s, nacht, seed, frei = [], topAmp = 0) {
  const pkte = []; let x = x0; let i = 0;
  while (x < x1) { const q = zz(seed + i); const b = (q < .25 ? 38 + q * 30 : 12 + q * 26) * s; const t = (tiefe * (q < .25 ? .35 : .5 + zz(seed + i * 3) * .7)) * s; pkte.push([x, Math.min(x + b, x1), t]); x += b; i++; }
  let d; const zapfen = [];
  if (!topAmp) d = `M${f1(x0)} ${f1(y0 - 30 * s)} H${f1(x1)} V${f1(y0)}`;
  else { d = `M${f1(x0)} ${f1(y0)} C${f1(x0)} ${f1(y0 - topAmp * .8 * s)} ${f1(x0 + 6 * s)} ${f1(y0 - topAmp * s)} ${f1(x0 + 12 * s)} ${f1(y0 - topAmp * s)}`; let x = x0 + 12 * s, k = 0;
    while (x < x1 - 30 * s) { const b = (22 + zz(seed + k * 5) * 26) * s; const h = topAmp * (.75 + zz(seed + k * 9) * .5) * s; d += ` Q${f1(x + b / 2)} ${f1(y0 - h - 3 * s)} ${f1(x + b)} ${f1(y0 - topAmp * .8 * s)}`; x += b; k++; }
    d += ` C${f1(x1 - 4 * s)} ${f1(y0 - topAmp * .8 * s)} ${f1(x1)} ${f1(y0 - topAmp * .4 * s)} ${f1(x1)} ${f1(y0)}`; }
  for (let j = pkte.length - 1; j >= 0; j--) { const [a, b, t] = pkte[j]; const m = (a + b) / 2;
    d += ` C${f1(b - (b - a) * .15)} ${f1(y0 + t)} ${f1(m + (b - a) * .2)} ${f1(y0 + t * 1.15)} ${f1(m)} ${f1(y0 + t * 1.1)} C${f1(m - (b - a) * .2)} ${f1(y0 + t * 1.05)} ${f1(a + (b - a) * .15)} ${f1(y0 + t)} ${f1(a)} ${f1(y0 + t * .25)}`;
    if (zz(seed + j * 7) > .42 && !frei.some(([fa, fb]) => m > fa && m < fb)) { const n = zz(seed + j) > .6 ? 2 : 1; for (let q = 0; q < n; q++) zapfen.push([m + (q ? 3.2 : -1) * s, y0 + t * 1.05, (5 + zz(seed + j * 11 + q) * 9) * s * (q ? .6 : 1)]); } }
  d += topAmp ? ' Z' : ` V${f1(y0 - 30 * s)} Z`;
  const kante = nacht ? '#7F9BB8' : '#B5CFE2';
  const z = zapfen.map(([zx, zy, h]) => { const w = 1.9 * s; return `<path d="M${f1(zx - w)} ${f1(zy - 1)} C${f1(zx - w * .8)} ${f1(zy + h * .45)} ${f1(zx - w * .2)} ${f1(zy + h * .85)} ${f1(zx + .2)} ${f1(zy + h)} C${f1(zx + w * .35)} ${f1(zy + h * .7)} ${f1(zx + w * .8)} ${f1(zy + h * .35)} ${f1(zx + w)} ${f1(zy - 1)} Z" fill="url(#${u}eis)"/><path d="M${f1(zx - w * .45)} ${f1(zy + 1)} L${f1(zx - w * .1)} ${f1(zy + h * .65)}" stroke="#fff" stroke-width="${f1(.6 * s)}" stroke-linecap="round" opacity=".9"/>`; }).join('');
  return `<path d="${d}" fill="#0B2A44" opacity="${nacht ? .35 : .12}" transform="translate(0 ${f1(2.4 * s)})"/><path d="${d}" fill="${kante}" transform="translate(0 ${f1(1.3 * s)})"/>${z}<path d="${d}" fill="url(#${u}schnee)"/>
    ${topAmp ? '' : `<path d="M${f1(x0)} ${f1(y0 - 1.2 * s)} H${f1(x1)}" stroke="#fff" stroke-width="${f1(1 * s)}" opacity=".9"/>`}`;
}
// Schneewehe (Ecke unten rechts): zwei Hügel, Schatten rechts unten, Glanz oben links, ein Funkeln
function festWehe(W, H, s, nacht) {
  const kante = nacht ? '#7F9BB8' : '#B5CFE2';
  const a = `M${f1(W - 128 * s)} ${H} C${f1(W - 112 * s)} ${f1(H - 13 * s)} ${f1(W - 88 * s)} ${f1(H - 19 * s)} ${f1(W - 66 * s)} ${f1(H - 15 * s)} C${f1(W - 52 * s)} ${f1(H - 28 * s)} ${f1(W - 22 * s)} ${f1(H - 34 * s)} ${W} ${f1(H - 30 * s)} V${H} Z`;
  return `<path d="${a}" fill="#0B2A44" opacity="${nacht ? .3 : .1}" transform="translate(${f1(-2 * s)} ${f1(-1 * s)})"/><path d="${a}" fill="${kante}"/><path d="${a}" fill="#fff" transform="translate(${f1(2 * s)} ${f1(2.6 * s)})"/>
    <path d="M${f1(W - 112 * s)} ${f1(H - 8 * s)} C${f1(W - 96 * s)} ${f1(H - 15 * s)} ${f1(W - 82 * s)} ${f1(H - 16 * s)} ${f1(W - 70 * s)} ${f1(H - 13 * s)} M${f1(W - 58 * s)} ${f1(H - 22 * s)} C${f1(W - 44 * s)} ${f1(H - 30 * s)} ${f1(W - 26 * s)} ${f1(H - 31 * s)} ${f1(W - 12 * s)} ${f1(H - 28.5 * s)}" stroke="#fff" stroke-width="${f1(1.4 * s)}" fill="none" stroke-linecap="round" opacity=".95"/>
    <path d="M${f1(W - 36 * s)} ${f1(H - 22 * s)} l${f1(.9 * s)} ${f1(2.2 * s)} ${f1(2.2 * s)} ${f1(.9 * s)} ${f1(-2.2 * s)} ${f1(.9 * s)} ${f1(-.9 * s)} ${f1(2.2 * s)} ${f1(-.9 * s)} ${f1(-2.2 * s)} ${f1(-2.2 * s)} ${f1(-.9 * s)} ${f1(2.2 * s)} ${f1(-.9 * s)}z" fill="${nacht ? '#FFE27A' : '#8FC3E6'}"/>`;
}
// Stern mit Strahlen (v5, über dem Ziel)
function festStern(u, x, y, R, nacht) {
  const strahl = (a, l, b) => `<path d="M0 ${-b} L${l} 0 L0 ${b} Z" transform="rotate(${a})" fill="url(#${u}strahl2)"/>`;
  return `<g transform="translate(${f1(x)} ${f1(y)})"><circle class="halo" r="${f1(R * 2.3)}" fill="url(#${u}halo2)"/>
    ${[0, 90, 180, 270].map((a) => strahl(a, R * 2.6, R * .13)).join('')}${[45, 135, 225, 315].map((a) => strahl(a, R * 1.5, R * .09)).join('')}
    <path d="M0 ${-R} C${R * .14} ${-R * .3} ${R * .3} ${-R * .14} ${R} 0 C${R * .3} ${R * .14} ${R * .14} ${R * .3} 0 ${R} C${-R * .14} ${R * .3} ${-R * .3} ${R * .14} ${-R} 0 C${-R * .3} ${-R * .14} ${-R * .14} ${-R * .3} 0 ${-R} Z" fill="#FFE27A" stroke="${nacht ? '#FFF6CC' : '#9A6A08'}" stroke-width="${nacht ? .6 : 1}" stroke-linejoin="round"/>
    <path d="M0 ${-R} C${R * .14} ${-R * .3} ${R * .3} ${-R * .14} ${R} 0 L0 0 Z M0 ${R} C${-R * .14} ${R * .3} ${-R * .3} ${R * .14} ${-R} 0 L0 0Z" fill="#F2B417"/>
    <circle r="${f1(R * .28)}" fill="#FFFDF0"/></g>`;
}
// Nordlicht: weiche, mehrfarbige Bänder + feine Vorhang-Strahlen (ein Unschärfe-Filter, einmal gerechnet)
function festNordlicht(u, W, H, s, nacht) {
  const op = nacht ? 1 : .8; const c = nacht ? ['#3DFFB0', '#2DD4E6', '#A78BFA', '#F472B6'] : ['#10B981', '#0EA5C6', '#8B5CF6', '#EC4899'];
  const band = (y, a, f, o) => `<path d="M${-20} ${f1(y * H)} C${f1(W * .2)} ${f1((y + a) * H)} ${f1(W * .38)} ${f1((y - a * .6) * H)} ${f1(W * .58)} ${f1((y + a * .4) * H)} S${f1(W * .9)} ${f1((y - a) * H)} ${W + 20} ${f1((y + a * .2) * H)} L${W + 20} ${f1((y + a * .2) * H - 26 * s)} C${f1(W * .85)} ${f1((y - a) * H - 30 * s)} ${f1(W * .6)} ${f1((y + a * .4) * H - 34 * s)} ${f1(W * .4)} ${f1((y - a * .6) * H - 24 * s)} S${f1(W * .1)} ${f1((y + a) * H - 30 * s)} -20 ${f1(y * H - 22 * s)} Z" fill="${f}" opacity="${o}"/>`;
  const strahlen = Array.from({ length: Math.round(W / (9 * s)) }, (_, i) => { const x = i * 9 * s + zz(i) * 4 * s; const l = (20 + zz(i + 40) * 26) * s; return `<rect x="${f1(x)}" y="${f1(.03 * H)}" width="${f1(1.6 * s)}" height="${f1(l)}" fill="${c[i % 2]}" opacity="${f1(.25 + zz(i + 80) * .35)}"/>`; }).join('');
  return `<g mask="url(#${u}nlm)" opacity="${op}"><g class="nordlicht" filter="url(#${u}nlb)">${band(.1, .04, c[0], .85)}${band(.075, .05, c[1], .55)}${band(.05, .03, c[2], .6)}${band(.035, .025, c[3], .3)}</g><g filter="url(#${u}nlb2)" opacity=".8">${strahlen}</g></g>`;
}

// 6.12.: Nikolaus-Stiefel mit Goldtalern und Zuckerstange
function festStiefel(x, y, s) {
  return `<g transform="translate(${f1(x)} ${f1(y)}) scale(${s})"><ellipse cx="6" cy="1" rx="12" ry="2" fill="#000" opacity=".15"/>
    <path d="M2.2 -14 C1 -20 2 -24 3.4 -27 L4.6 -26 C3.6 -23 3 -20 4 -14Z" fill="#fff"/><path d="M2.2 -27 C2 -30 5.6 -31 6 -28" stroke="#E5243B" stroke-width="2" fill="none" stroke-linecap="round"/>
    ${[[5, -19, '#FFC94A'], [9.6, -18, '#FFD86B'], [7.4, -21.6, '#F2B417']].map(([cx, cy, f]) => `<ellipse cx="${cx}" cy="${cy}" rx="3" ry="2.6" fill="${f}"/><ellipse cx="${cx}" cy="${cy}" rx="1.8" ry="1.5" fill="none" stroke="#C98A0A" stroke-width=".5"/><path d="M${cx - 1.6} ${cy - 1.2} q1 -1 2 -.6" stroke="#FFF6CC" stroke-width=".6" fill="none"/>`).join('')}
    <path d="M0 -14 H13 V-4 L19.6 -2.6 C23 -1.8 23.4 1.6 20 1.6 H0Z" fill="#E5243B"/><path d="M13 -14 V-4 L19.6 -2.6 C23 -1.8 23.4 1.6 20 1.6 H11 C14 1 15 -1 10 -4 V-14Z" fill="#B3122B"/>
    <path d="M1 -12.5 V-2" stroke="#FF8A95" stroke-width="1" stroke-linecap="round" opacity=".8"/>
    <rect x="-1.4" y="-17.2" width="16" height="4.6" rx="2.3" fill="#fff"/><path d="M0 -13.4 H13.4" stroke="#C7D3E3" stroke-width="1" stroke-linecap="round"/></g>`;
}
// 31.12.: drei Feuerwerks-Bouquets neben dem Ziel (verjüngte Strahlen, heller Kern, fallende Funken)
function festFeuerwerk(orte) {
  const farben = [['#FFC94A', '#FFF3D1'], ['#FF5A5F', '#FFD0D2'], ['#3DDC84', '#D7FBE7']];
  return orte.map(([bx, by, r], i) => [bx, by, farben[i % 3], r]).map(([bx, by, [f, h], r], i) => `<path d="M${f1(bx + 6)} ${f1(by + r * 2.6)} Q${f1(bx + 3)} ${f1(by + r * 1.4)} ${f1(bx)} ${f1(by + r * .3)}" stroke="${h}" stroke-width="1" fill="none" stroke-dasharray="1 2.4" opacity=".7"/><g class="feuerwerk f${i}" transform="translate(${f1(bx)} ${f1(by)})"><circle r="${r * .5}" fill="${h}" opacity=".35"/>
    ${Array.from({ length: 14 }, (_, j) => { const a = j / 14 * 360 + i * 9; const l = r * (j % 2 ? .78 : 1); return `<path d="M0 -.7 L${l} 0 L0 .7Z" transform="rotate(${a}) translate(${r * .22} 0)" fill="${f}"/><circle cx="${f1(Math.cos(a * Math.PI / 180) * (l + r * .38))}" cy="${f1(Math.sin(a * Math.PI / 180) * (l + r * .38))}" r=".9" fill="${h}"/>`; }).join('')}
    <circle r="2" fill="#fff"/>${[[-3, r + 4], [4, r + 7], [-6, r + 10]].map(([fx2, fy2], q) => `<circle cx="${fx2}" cy="${fy2}" r="${.8 - q * .15}" fill="${f}" opacity="${.8 - q * .2}"/>`).join('')}</g>`).join('');
}
// ================= Reisekarte: Weihnachts-Ebene „Winternacht“ (Entwurf 2, Variante v5) =================
// Drei Ebenen, alle pointer-events none und aria-hidden (fangen keine Tipps ab):
//  unter – Tönung, Frost-Rand, Nordlicht: in der Karten-SVG zwischen Ländern und Routen, fest am Kartenrand (Transformation folgt dem Ausschnitt, setzeVb)
//  oben  – Mützen/Schneehäubchen, Stern über „gerade dran“, Tannen/Pakete, Stiefel (6.12.), Feuerwerk (31.12.): nach den Pins, bewegt sich mit der Karte
//  rand  – Lichterkette (zwischen Sonne und Zoom-Knöpfen), Schneehaube mit Eiszapfen, Schneewehe, Schnee (Canvas) und Schlitten: fest über dem Kartenbild
// Bewegung: 3 Lampen-Gruppen + Nordlicht + Stern-Halo (CSS) und EINE rAF-Schleife (Schnee + Schlitten); „Bewegung reduzieren“ → alles still; Hintergrund-Tab → keine Zeichenarbeit.
const FEST_SVG = 'http://www.w3.org/2000/svg';
const hashZahl = (t) => { let h = 7; for (const c of String(t)) h = (h * 31 + c.charCodeAt(0)) % 100003; return h; };
const datenUrl = (svg) => `url("data:image/svg+xml,${encodeURIComponent(svg)}")`;
function festUnterZeichnen(fest, W, H, s, nacht) {
  const u = 'rkfu'; const op = nacht ? 1 : .8;
  const tint = `<rect x="-60" y="-60" width="${W + 120}" height="${H + 120}" fill="${nacht ? '#3D6FD6' : '#8DB8E6'}" opacity="${nacht ? .18 : .26}"/>`;
  const frost = `<defs><radialGradient id="${u}frost" cx=".5" cy=".55" r=".75"><stop offset=".62" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="${nacht ? '#9CC8FF' : '#FFFFFF'}" stop-opacity="${nacht ? .3 : .8}"/></radialGradient></defs><rect width="${W}" height="${H}" fill="url(#${u}frost)"/>`;
  fest.unter.innerHTML = tint + frost + '<image class="nordlicht" x="0" y="0" width="' + W + '" height="' + H + '" preserveAspectRatio="none"/>';
  // Nordlicht einmal gerastert (Unschärfe-Filter nur einmal gerechnet, beim Ziehen nicht neu) – Bild statt Live-Filter
  const nl = `<svg xmlns="${FEST_SVG}" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}"><defs><filter id="${u}nlb" x="-10%" y="-50%" width="120%" height="200%"><feGaussianBlur stdDeviation="${f1(7 * s)}"/></filter><filter id="${u}nlb2" x="-10%" y="-50%" width="120%" height="200%"><feGaussianBlur stdDeviation="${f1(1.6 * s)}"/></filter>
    <linearGradient id="${u}nlmaske" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".2" stop-color="#fff" stop-opacity=".15"/><stop offset=".42" stop-color="#fff" stop-opacity="1"/><stop offset=".9" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity=".5"/></linearGradient>
    <mask id="${u}nlm"><rect width="${W}" height="${H * .36}" fill="url(#${u}nlmaske)"/></mask></defs>${festNordlicht(u, W, H, s, nacht)}</svg>`;
  const bild = new Image(); const nr = (fest.nlNr = (fest.nlNr || 0) + 1);
  bild.onload = () => { if (fest.nlNr !== nr) return; try { const c = document.createElement('canvas'); c.width = W; c.height = H; c.getContext('2d').drawImage(bild, 0, 0);
    const img = fest.unter.querySelector('image.nordlicht'); img?.setAttribute('href', c.toDataURL('image/png')); img?.setAttribute('opacity', String(op)); } catch { /* ohne Nordlicht */ } };
  bild.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(nl);
}
function festRandZeichnen(fest, L, s, nacht) {
  const { W, H } = L; const u = 'rkfr'; const g = [];
  const uni = L.uni && L.uni[1] < 60 ? L.uni : null; const zoom = L.zoom;
  const zapfFrei = [uni ? [uni[0] - 6, uni[0] + uni[2] + 6] : null, zoom ? [zoom[0] - 6, zoom[0] + zoom[2] + 6] : null].filter(Boolean);
  const anf = uni ? uni[0] + uni[2] + 4 * s : 12, ende = zoom ? zoom[0] - 8 * s : W - 12;
  if (ende - anf > 70 * s) g.push(festLichterkette(u, anf, ende, 5 * s, s, nacht)); // Lichterkette nur zwischen Sonne und Zoom-Knöpfen
  g.push(festHaube(u, -4, W + 4, 7 * s, 8, s, nacht, 3, zapfFrei));
  g.push(`<g transform="translate(0 ${-Math.max(0, L.unten)})">${festWehe(W, H, s, nacht)}</g>`); // Wehe unten rechts, über der Schwebekarte
  const tag24 = L.tag.getMonth() === 11 && L.tag.getDate() === 24;
  if (tag24) { const d = `M${f1(-70 * s)} ${f1(H * .64)} C${f1(W * .25)} ${f1(H * .2)} ${f1(W * .7)} ${f1(H * .12)} ${f1(W + 80 * s)} ${f1(H * .36)}`;
    g.push(`<path id="rkf-weltbahn" d="${d}" fill="none" stroke="none"/><path d="${d}" fill="none" stroke="#FFD23F" stroke-width="${f1(2.2 * s)}" stroke-dasharray="${f1(.1 * s)} ${f1(9 * s)}" stroke-linecap="round" opacity=".95"/><path d="${d}" fill="none" stroke="#FFF3D1" stroke-width="${f1(1.2 * s)}" stroke-dasharray="${f1(.1 * s)} ${f1(23 * s)}" stroke-dashoffset="${f1(5 * s)}" stroke-linecap="round"/>`); }
  g.push(`<path id="rkf-bahn" d="" fill="none" stroke="none"/><g class="rkf-schlitten" style="display:none">${festSchlitten(nacht, (tag24 ? 1.9 : 1.15) * s)}</g>`);
  const mask = `<mask id="${u}frei" maskUnits="userSpaceOnUse" x="-20" y="-20" width="${W + 40}" height="${H + 40}"><rect x="-20" y="-20" width="${W + 40}" height="${H + 40}" fill="#fff"/>${zoom ? `<rect x="${zoom[0]}" y="${zoom[1]}" width="${zoom[2]}" height="${zoom[3]}" rx="12" fill="#000"/>` : ''}${uni ? `<circle cx="${uni[0] + uni[2] / 2}" cy="${uni[1] + 29}" r="30" fill="#000"/>` : ''}</mask>`;
  fest.rand.innerHTML = `<canvas class="rkf-schnee" width="${Math.round(W * 2)}" height="${Math.round(H * 2)}"></canvas><svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}"><defs>${festDefs(u, nacht)}${mask}</defs><g mask="url(#${u}frei)">${g.join('')}</g></svg>`;
  fest.bahnTag24 = tag24;
}
// Mützen-Regel (grafik-bericht.md): nur große Pins (Kopfradius ≥ 12) bekommen eine Mütze; kleine und bedrängte Pins ein Schneehäubchen; die Mütze weicht
// Beschriftungen und Kartenknöpfen aus (kleiner bis 80 %, dann nur Häubchen); am Pin „gerade dran“ sitzt der Stern statt der Mütze.
function festObenZeichnen(fest, L, s, nacht) {
  const { pins, belegt = [], koepfe = [] } = L; const o = []; const k = L.k;
  const namen = belegt.filter((b) => !koepfe.includes(b)); const zoom = L.zoom;
  const trifft = (pts) => pts.some(([px, py]) => namen.some(([x0, y0, x1, y1]) => px > x0 && px < x1 && py > y0 && py < y1) || (zoom && px > zoom[0] - 2 && px < zoom[0] + zoom[2] + 2 && py > zoom[1] - 2 && py < zoom[1] + zoom[3] + 2));
  const huelle = (x, y, r, rot, kk) => [[-14.6, -19.4], [-.6, -24.6], [7.4, -9.6], [-8, -8], [-18, -19.4], [-14.6, -23]].map(([a, b]) => { const c = Math.cos(rot * Math.PI / 180), sn = Math.sin(rot * Math.PI / 180); const q = (r / 10) * kk; return [x + (a * c - b * sn) * q, y + (a * sn + b * c) * q]; });
  const frei = (b) => !belegt.some((x) => !(b[2] < x[0] || b[0] > x[2] || b[3] < x[1] || b[1] > x[3])) && b[0] > 0 && b[1] > 0 && b[2] < L.W && b[3] < L.H - (L.unten || 0);
  const use = (id, x, y, rot, sk) => `<use href="#${id}" transform="translate(${f1(x)} ${f1(y)})${rot ? ` rotate(${f1(rot)})` : ''} scale(${f1(sk * 100) / 100})"/>`;
  let mz = 0, hb = 0; const dranPin = pins.find((p) => p.dran);
  for (const p of pins) {
    if (p.r < 12) { o.push(use('rkf-hb', p.x, p.y, 0, p.r / 10)); hb++; continue; }
    if (p === dranPin) continue; // Stern statt Mütze
    const bedraengt = pins.some((q) => q !== p && Math.abs(q.x - p.x) < p.r * 1.7 && p.y - q.y > 0 && p.y - q.y < p.r * 2.9);
    if (bedraengt) { o.push(use('rkf-hb', p.x, p.y, 0, p.r / 10)); hb++; continue; }
    const seed = hashZahl(p.id || `${p.spitze?.[0]}`) / 997;
    let rot = p.abz ? -24 - zz(seed) * 8 : -6 - zz(seed + 3) * 18; let kk = 1.04, ok = false;
    for (const k0 of [1.04, .92, .8]) { if (!trifft(huelle(p.x, p.y, p.r, rot, k0))) { kk = k0; ok = true; break; } if (!trifft(huelle(p.x, p.y, p.r, rot - 10, k0))) { kk = k0; rot -= 10; ok = true; break; } }
    if (!ok) { o.push(use('rkf-hb', p.x, p.y, 0, p.r / 10)); hb++; continue; }
    o.push(use('rkf-mu', p.x, p.y, rot, (p.r / 10) * kk)); mz++;
    const pts = huelle(p.x, p.y, p.r, rot, kk); belegt.push([Math.min(...pts.map((q) => q[0])), Math.min(...pts.map((q) => q[1])), Math.max(...pts.map((q) => q[0])), Math.max(...pts.map((q) => q[1]))]);
  }
  fest.zahl = { muetzen: mz, haeubchen: hb };
  // Tannen und Pakete an gelandeten Ländern, nur auf freien Plätzen (höchstens 6)
  let deko = 0; const paketF = [['#E5243B', '#FFC94A'], ['#7B1E6E', '#FFF3D1'], ['#0E9F6E', '#FFC94A']];
  for (const p of pins.filter((x) => x.gelandet)) { if (deko >= 6) break;
    for (const [dx, dy] of [[p.r + 8, 2], [-p.r - 8, 2], [p.r + 10, 16]]) { const x = p.spitze[0] + dx, y = p.spitze[1] + dy; const b = [x - 9, y - 22, x + 9, y + 2];
      if (frei(b)) { belegt.push(b); o.push(deko % 2 ? festPaket(x, y, ...paketF[deko % 3], s * .78) : festTanne(x, y, s * .82)); deko++; break; } } }
  // Stern über dem Ziel (v5), weicher Lichtkegel zum Pin
  const ziel = dranPin ? [dranPin.x, dranPin.y, dranPin.r] : L.hier ? [L.hier[0], L.hier[1], 6] : null;
  if (ziel) { const [x0, y0, r0] = ziel; const R = 13 * s; const sy = y0 - r0 - 26 * s;
    o.push(`<path d="M${f1(x0 - 5 * s)} ${f1(sy + 6 * s)} L${f1(x0 - r0 * .7)} ${f1(y0 - r0 * .4)} L${f1(x0 + r0 * .7)} ${f1(y0 - r0 * .4)} L${f1(x0 + 5 * s)} ${f1(sy + 6 * s)} Z" fill="url(#rkfkegelL)"/>`, festStern('rkf', x0, sy, R, nacht));
    belegt.push([x0 - R * 1.5, sy - R * 1.5, x0 + R * 1.5, sy + R * 1.5]); }
  // Tages-Sonderfälle: 6.12. Stiefel, 31.12. Feuerwerk – nur auf freien Flächen neben dem Ziel
  const m = L.tag.getMonth(), d = L.tag.getDate();
  if (ziel && m === 11 && d === 6) { const [x0, y0] = ziel;
    for (const [dx, dy] of [[34, 26], [-58, 26], [40, -10], [-64, -8], [20, 52], [-40, 54]]) { const x = x0 + dx * s, y = y0 + dy * s; const b = [x - 4, y - 36 * s, x + 30 * s, y + 4];
      if (frei(b)) { belegt.push(b); o.push(festStiefel(x, y, s * 1.25)); fest.sonder = 'stiefel'; break; } } }
  if (ziel && m === 11 && d === 31) { const [x0, y0] = ziel; const dicht = (cx, cy) => pins.filter((p) => Math.hypot(p.x - cx, p.y - cy) < 80).length;
    const kand = [[-110, 40], [110, 40], [-100, -70], [100, -70], [0, 110], [-150, 0], [150, 0]].map(([dx, dy]) => [x0 + dx * s, y0 + dy * s]).filter(([cx, cy]) => cx > 30 && cy > 40 && cx < L.W - 30 && cy < L.H - (L.unten || 0) - 30)
      .sort((a, b) => dicht(...a) - dicht(...b));
    const ort = kand.find(([cx, cy]) => frei([cx - 22 * s, cy - 22 * s, cx + 22 * s, cy + 22 * s])) || kand[0];
    if (ort) { const [cx, cy] = ort; const seite = cx < x0 ? -1 : 1; o.push(festFeuerwerk([[cx, cy, 18 * s], [cx + seite * 50 * s, cy + 16 * s, 14 * s], [cx + seite * 86 * s, cy + 42 * s, 11 * s]])); fest.sonder = 'feuerwerk'; } }
  return o.join('');
}
function festDefsOben(nacht) {
  return `<defs>${festDefs('rkf', nacht)}<radialGradient id="rkfhalo2"><stop offset="0" stop-color="#FFE27A" stop-opacity="${nacht ? .75 : .6}"/><stop offset=".4" stop-color="#FFD23F" stop-opacity="${nacht ? .25 : .18}"/><stop offset="1" stop-color="#FFD23F" stop-opacity="0"/></radialGradient>
    <linearGradient id="rkfstrahl2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFF6CC"/><stop offset="1" stop-color="#FFD23F" stop-opacity="0"/></linearGradient>
    <linearGradient id="rkfkegelL" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE27A" stop-opacity=".55"/><stop offset="1" stop-color="#FFE27A" stop-opacity="0"/></linearGradient>
    <g id="rkf-mu">${festMuetze('rkf', 0, 0, 10, 0, 1, nacht)}</g><g id="rkf-hb">${festHaeubchen(0, 0, 10, nacht)}</g></defs>`;
}
// Eine gemeinsame Schleife für Schnee (Canvas, 3 Tiefen) und Schlitten. Läuft nur, solange die Karte im Dokument und die Seite sichtbar ist.
function festLaufStarten(fest, L, s, nacht) {
  festLaufStop(fest);
  const c = fest.rand.querySelector('canvas.rkf-schnee'); const ctx = c?.getContext('2d'); if (!ctx) return;
  if (lernWenigBewegung()) { ctx.clearRect(0, 0, c.width, c.height); return; } // Bewegung reduzieren: kein Schnee, kein Schlitten
  const W2 = c.width, H2 = c.height; const s2 = s * 2; let sd = 11; const zf = () => (sd = (sd * 16807) % 2147483647) / 2147483647;
  const sprite = (r, weich) => { const q = document.createElement('canvas'); const d = Math.ceil(r * 2 + 6); q.width = q.height = d; const x = q.getContext('2d'); const m = d / 2;
    const gr = x.createRadialGradient(m, m, 0, m, m, r + (weich ? 2 : .6)); gr.addColorStop(0, 'rgba(255,255,255,1)'); gr.addColorStop(weich ? .25 : .7, 'rgba(255,255,255,.95)'); gr.addColorStop(1, 'rgba(255,255,255,0)');
    if (!nacht) { x.beginPath(); x.arc(m, m + .6, r + .3, 0, 7); x.fillStyle = weich ? 'rgba(70,110,150,.18)' : 'rgba(70,110,150,.42)'; x.fill(); }
    x.fillStyle = gr; x.beginPath(); x.arc(m, m, r + (weich ? 2 : .6), 0, 7); x.fill(); return q; };
  const breit = L.W >= 700;
  const T = [{ n: breit ? 70 : 34, r: [.9, 1.5], v: [.22, .38], a: nacht ? .7 : .85, weich: false }, { n: breit ? 30 : 15, r: [1.9, 2.6], v: [.5, .7], a: .95, weich: false }, { n: breit ? 9 : 5, r: [4.2, 6], v: [1, 1.3], a: nacht ? .6 : .75, weich: true }];
  const fl = []; T.forEach((l, li) => { for (let i = 0; i < l.n; i++) { const r = (l.r[0] + zf() * (l.r[1] - l.r[0])) * s2; fl.push({ x: zf() * W2, y: zf() * H2, r, v: (l.v[0] + zf() * (l.v[1] - l.v[0])) * s2 * .5, p: zf() * 6, a: l.a, sp: sprite(r, l.weich), li }); } });
  const fz = [L.uni, L.zoom, L.quelle].filter(Boolean).map(([x, y, w, h]) => [x * 2, y * 2, w * 2, h * 2]);
  const male = () => { ctx.clearRect(0, 0, W2, H2); for (const p of fl) { if (fz.some(([x, y, w, h]) => p.x > x - 6 && p.x < x + w + 6 && p.y > y - 6 && p.y < y + h + 6)) continue; ctx.globalAlpha = p.a; ctx.drawImage(p.sp, p.x - p.sp.width / 2, p.y - p.sp.height / 2); } ctx.globalAlpha = 1; };
  const g = fest.rand.querySelector('.rkf-schlitten');
  const pfad = () => fest.rand.querySelector(fest.bahnTag24 ? '#rkf-weltbahn' : '#rkf-bahn');
  const setze = (t) => { const pf = pfad(); const PL = pf?.getTotalLength?.() || 0; if (!PL) { g.style.display = 'none'; return; }
    const p = pf.getPointAtLength(PL * t), q = pf.getPointAtLength(Math.min(PL, PL * t + 2)); let r = Math.atan2(q.y - p.y, q.x - p.x) * 180 / Math.PI; const flip = q.x < p.x; if (flip) r += 180; if (r > 180) r -= 360; r = Math.max(-16, Math.min(16, r));
    g.style.display = ''; g.setAttribute('transform', `translate(${f1(p.x)} ${f1(p.y - 8)}) rotate(${f1(r)})${flip ? ' scale(-1 1)' : ''}`); };
  let einmal24 = false; if (fest.bahnTag24) { const schl = 'lern.fest.24'; const heute = lernAdventTag(L.tag); try { einmal24 = localStorage.getItem(schl) !== heute; localStorage.setItem(schl, heute); } catch { einmal24 = true; } }
  const dauer = fest.bahnTag24 ? 7000 : 6000, pause = fest.bahnTag24 ? 1e9 : 8000; const t0 = performance.now() - (fest.bahnTag24 ? 0 : dauer + pause - 1500);
  const lauf = (t) => {
    if (!document.body.contains(fest.rand)) { festLaufStop(fest); return; }
    for (const p of fl) { p.y += p.v; p.x += Math.sin((p.y / s2 + p.p * 40) / 40) * .18 * (p.li + 1); if (p.y > H2 + 12) { p.y = -12; p.x = zf() * W2; } } male();
    if (g) { const x = (t - t0) % (dauer + pause); if ((fest.bahnTag24 && (!einmal24 || t - t0 > dauer)) || x > dauer) g.style.display = 'none'; else setze(x / dauer); }
    fest.lauf = requestAnimationFrame(lauf);
  };
  fest.sicht = () => { if (document.hidden) { cancelAnimationFrame(fest.lauf); fest.lauf = 0; } else if (!fest.lauf && document.body.contains(fest.rand)) fest.lauf = requestAnimationFrame(lauf); };
  document.addEventListener('visibilitychange', fest.sicht);
  if (!document.hidden) fest.lauf = requestAnimationFrame(lauf); // Hintergrund-Tab: keine Zeichenarbeit
}
function festLaufStop(fest) { if (fest.lauf) cancelAnimationFrame(fest.lauf); fest.lauf = 0; if (fest.sicht) document.removeEventListener('visibilitychange', fest.sicht); fest.sicht = null; }
function lernFestZeichnen(fest, L) {
  const nacht = !!fest.nacht; const s = L.W >= 700 ? 1.2 : 1; const wenig = lernWenigBewegung();
  L.wurzel?.classList.toggle('lr-adv-bewegt', !wenig);
  if (!fest.css && L.wurzel) { fest.css = true; // Schneehaube auf „Gerade dran“, Mütze am Jugendwort-Schild (CSS, pointer-events none)
    L.wurzel.style.setProperty('--rk-fest-haube', datenUrl(`<svg xmlns="${FEST_SVG}" viewBox="0 0 120 22" width="120" height="22" preserveAspectRatio="none"><defs>${festDefs('h', nacht)}</defs>${festHaube('h', -2, 122, 9, 4, .8, nacht, 17, [], 5)}</svg>`));
    L.wurzel.style.setProperty('--rk-fest-muetze', datenUrl(`<svg xmlns="${FEST_SVG}" viewBox="-21 -29 32 32"><defs>${festDefs('m', nacht)}</defs>${festMuetze('m', 0, 0, 10, 0, 1, nacht)}</svg>`)); }
  // unter: nur bei neuer Größe neu; Transformation hält sie am Kartenrand
  const schlU = [Math.round(L.W), Math.round(L.H), nacht].join('|');
  if (fest.schlUnter !== schlU) { fest.schlUnter = schlU; festUnterZeichnen(fest, L.W, L.H, s, nacht); }
  fest.vb = (vb, W0) => fest.unter.setAttribute('transform', `translate(${f1(vb[0])} ${f1(vb[1])}) scale(${(vb[2] / W0).toFixed(5)})`);
  if (L.vb) fest.vb(L.vb, L.W);
  // rand: neu bei Größe, Lage von Sonne/Knöpfen/Quelle, Höhe „Gerade dran“, Tag
  const schlR = [schlU, JSON.stringify([L.uni, L.zoom, L.quelle].map((r) => r && r.map(Math.round))), Math.round(L.unten || 0), lernAdventTag(L.tag), wenig].join('|');
  if (fest.schlRand !== schlR) { fest.schlRand = schlR; festRandZeichnen(fest, L, s, nacht); festLaufStarten(fest, L, s, nacht); }
  // Bahn des Schlittens: die letzten drei Stationen der Route (Bildschirm)
  const r = L.route || []; const bahn = fest.rand.querySelector('#rkf-bahn');
  if (bahn) { const n = r.length; const a = r[Math.max(0, n - 3)], b = r[Math.max(0, n - 2)], c = r[n - 1]; bahn.setAttribute('d', n >= 2 ? `M${f1(a[0])} ${f1(a[1])} Q${f1(b[0])} ${f1(b[1])} ${f1(c[0])} ${f1(c[1])}` : ''); }
  // oben: bewegt sich mit der Karte (Inhalt in Bildschirm-Pixeln, Transformation = Ausschnitt beim Zeichnen)
  if (fest.defsNacht !== nacht || !fest.oben.querySelector('#rkf-mu')) { fest.defsNacht = nacht; fest.oben.innerHTML = festDefsOben(nacht) + '<g class="rkf-inhalt"></g>'; }
  const inhalt = fest.oben.querySelector('.rkf-inhalt'); fest.sonder = null;
  inhalt.innerHTML = festObenZeichnen(fest, L, s, nacht);
  if (L.vb) inhalt.setAttribute('transform', `translate(${f1(L.vb[0])} ${f1(L.vb[1])}) scale(${(L.vb[2] / L.W).toFixed(5)})`);
}


Object.assign(window, { LERN_ADVENT_DA: true, LERN_ADVENT_MOTIVE, lernAdventTuerZeigen: tuerZeigen, lernAdventZeile, lernAdventMenue, lernAdventKalenderSeite, lernAdventGutscheinSeite, lernAdventElternSeite, lernFestZeichnen });
})();
