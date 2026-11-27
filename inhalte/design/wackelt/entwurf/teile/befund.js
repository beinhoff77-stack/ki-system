/* Die Voranalyse: Was die Seite aus den vorhandenen Daten rechnet, bevor der Lehrer etwas antippt.
   Hier wird NICHTS geraten und nichts gedeutet, was nicht in den Daten steht. Jede Zeile unten
   lässt sich aus schule_lernstand und schule_wackelt_lesen ausrechnen – ohne neue Serverfunktion, ohne KI. */
'use strict';

// ---------- 1. Fehlerart in Worte fassen ----------
// Die Gründe kommen schon heute vom Server (antwort_bewerten: vorzeichen, komma, vertauscht, gerundet, falsche_einheit).
// Je Grund ein fester Satz. Platzhalter: {n} = so oft erkannt, {m} = falsche Antworten im Thema.
const BEFUND_TEXT = {
  vorzeichen: 'das Vorzeichen kippt – richtiger Betrag, falsches Vorzeichen',
  komma: 'das Komma sitzt falsch – richtige Ziffern an der falschen Stelle',
  vertauscht: 'richtig gerechnet, aber verdreht',
  gerundet: 'falsch gerundet – dicht daneben',
  falsche_einheit: 'richtige Zahl, falsche Einheit',
};
const BEFUND_KURZ = { vorzeichen: 'Vorzeichen', komma: 'Komma', vertauscht: 'vertauscht', gerundet: 'gerundet', falsche_einheit: 'Einheit' };

// Ein Muster gilt erst ab 2 gleichen Gründen – darunter ist es Zufall.
function haeufigsterGrund(etappen) {
  const summe = {};
  for (const e of etappen) for (const [g, n] of Object.entries(e.fehler_gruende || {})) summe[g] = (summe[g] || 0) + n;
  const [grund, n] = Object.entries(summe).sort((a, b) => b[1] - a[1])[0] || [];
  return n >= 2 ? { grund, n } : null;
}

// Der Satz sagt genau so viel, wie die Zahlen hergeben: bei wenigen Treffern bleibt er vorsichtig.
function befundSatz(t) {
  const m = t.etappen.reduce((s, e) => s + e.falsch, 0);
  const h = haeufigsterGrund(t.etappen);
  if (!h) return { satz: `Kein Muster: Die ${m} falschen Antworten liegen jede anders daneben. Hier helfen die Aufgaben selbst mehr als eine Regel.`, kurz: null, stark: false };
  const anteil = h.n / m;
  const was = BEFUND_TEXT[h.grund];
  if (anteil >= 2 / 3) return { satz: `Fast immer dasselbe: ${was}. ${h.n} von ${m} falschen Antworten.`, kurz: BEFUND_KURZ[h.grund], stark: true };
  if (anteil >= 1 / 3) return { satz: `Oft, aber nicht immer: ${was}. ${h.n} von ${m} falschen Antworten – die übrigen ${m - h.n} liegen anders daneben.`, kurz: BEFUND_KURZ[h.grund], stark: true };
  return { satz: `Ein kleinerer Teil der Fehler passt zusammen: ${was} (${h.n} von ${m}). Für ein Muster ist das noch wenig.`, kurz: null, stark: false };
}

// Die Regel gehört zu der Etappe, in der die meisten Fehler stecken – nicht einfach zur ersten.
function hauptEtappe(t) { return t.etappen.slice().sort((a, b) => b.falsch - a.falsch)[0]; }

// ---------- 2. Reihenfolge: das Dringendste zuerst, und zwar nachvollziehbar ----------
// Rang 1 bekommt, was am lautesten ruft. Der Grund steht als Wort an der Karte, damit die Reihenfolge nicht geraten wirkt.
function dringlichkeit(t) {
  const falsch = t.etappen.reduce((s, e) => s + e.falsch, 0);
  const richtig = t.etappen.reduce((s, e) => s + e.richtig, 0);
  const tage = tageSeit(t.letzter_fehler_am);
  let punkte = falsch * 2;
  let grund = `${falsch} falsche Antworten`;
  // Der Grund nennt genau das Kriterium, das diesen Rang bringt – ohne zu wiederholen, was schon als Marke danebensteht.
  if (t.wieder_offen) { punkte += 100; grund = `${falsch} falsche Antworten, ${richtig} richtige`; }
  else if (falsch >= 3 && falsch > richtig) { punkte += 50; grund = `mehr falsch als richtig: ${falsch} von ${falsch + richtig}`; }
  if (t.fehler_neu > 0) punkte += 20;
  if (tage <= 1) punkte += 10;
  return { punkte, grund };
}

function tageSeit(iso) {
  if (!iso) return 999;
  const d = new Date(iso); d.setHours(0, 0, 0, 0);
  const h = new Date('2026-11-27T09:00:00+01:00'); h.setHours(0, 0, 0, 0);
  return Math.round((h - d) / 864e5);
}
function wann(iso) { const t = tageSeit(iso); return t <= 0 ? 'heute' : t === 1 ? 'gestern' : `vor ${t} Tagen`; }

// ---------- 3. Die Lage in einem Satz (Kopf der Seite) ----------
function lage(themen) {
  const offen = themen.filter((t) => t.status === 'zu_besprechen');
  const falsch = offen.reduce((s, t) => s + t.etappen.reduce((x, e) => x + e.falsch, 0), 0);
  const summe = {};
  for (const t of offen) for (const e of t.etappen) for (const [g, n] of Object.entries(e.fehler_gruende || {})) summe[g] = (summe[g] || 0) + n;
  const top = Object.entries(summe).sort((a, b) => b[1] - a[1])[0];
  const aelteste = offen.map((t) => tageSeit(t.letzter_fehler_am)).sort((a, b) => b - a)[0] || 0;
  return {
    themen: offen.length, falsch, tage: aelteste,
    muster: top && top[1] >= 2 ? { wort: BEFUND_KURZ[top[0]], n: top[1] } : null,
    quer: top && top[1] >= 2 && offen.filter((t) => t.etappen.some((e) => (e.fehler_gruende || {})[top[0]])).length >= 2,
  };
}

// ---------- 4. Was der Lehrer zuerst ansehen sollte ----------
// Die eine Aufgabe, an der das Muster am deutlichsten wird: die jüngste falsche Antwort der Etappe mit den meisten Fehlern.
function aufhaenger(t) {
  const e = t.etappen.slice().sort((a, b) => b.falsch - a.falsch)[0];
  return e && e.fehler.length ? { etappe: e, fehler: e.fehler[0] } : null;
}
