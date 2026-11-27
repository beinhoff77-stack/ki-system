// Form-Takt (App 0.94.0): reine Auswahl-Logik der nächsten Bordkarte (lernWaehleBordkarte in lernen.js) – läuft ohne Browser.
// Vorgabe inhalte/plan/form-takt.md (Regeln 2–4, 6). Prüft auch: ohne neue Felder (alter Server) wählt die App genau wie 0.93.8.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const quelle = fs.readFileSync(path.resolve(__dirname, '..', 'lernen.js'), 'utf8');
const stueck = (von, bis) => { const a = quelle.indexOf(von), b = quelle.indexOf(bis, a); assert.ok(a >= 0 && b > a, von); return quelle.slice(a, b); };
const zeile = (von) => { const a = quelle.indexOf(von); assert.ok(a >= 0, von); return quelle.slice(a, quelle.indexOf('\n', a)); };
const code = [stueck('const LERN_TYP = {', '// Stufenzeichen'), zeile('const lernBauplan = '), zeile('const lernIstSchwer = '),
  stueck('const lernSollStufe = ', '// W176 Teil 3: Ist jetzt eine Mischkarte dran?')].join('\n');
// Bezug: die Auswahl, wie sie bis 0.93.8 war (wörtlich), damit „alter Server = unverändert“ prüfbar bleibt
const ALT = String.raw`
// Auswahl der nächsten Bordkarte (stellt sie an den Anfang von warte). Regel „sitzt“ (16.11.): Die Stufe steigt mit den Punkten.
function lernWaehleAlt(warte, e, letzte, gesehenTyp = new Set()) {
  // W176: Stufe nach eigenen Lösungen (anteilig), nach je 2 Fehlern in Folge eine Stufe leichter (stufe_senkung vom Server)
  const ziel = e.ziel || 6, p = e.neueRegel ? e.eigene : e.serie || 0;
  const soll = Math.max(1, (p >= ziel ? 3 : Math.min(3, 1 + Math.floor(p * 3 / ziel))) - (e.neueRegel ? e.stufeSenkung || 0 : 0));
  const vor = (j) => { if (j > 0) warte.unshift(...warte.splice(j, 1)); return j >= 0; };
  // Punkte voll, aber die schwere Aufgabe fehlt noch: dann kommt auf jeden Fall eine schwere
  // F: Abwechslung – nie zweimal hintereinander derselbe Typ (ohne Typ: derselbe Fragetext ohne Zahlen); Typen bevorzugen, die in dieser Etappe noch nicht dran waren
  const anders = (x) => !letzte || (x.typ && letzte.typ ? x.typ !== letzte.typ : lernBauplan(x) !== lernBauplan(letzte));
  const neuTyp = (x) => !x.typ || !gesehenTyp.has(x.typ);
  for (const ex of [(x) => anders(x) && neuTyp(x), anders]) {
    if (p >= ziel && e.schwerNoetig && !e.schwerOk && vor(warte.findIndex((x) => lernIstSchwer(x) && x !== letzte && !x.geloest && ex(x)))) return;
  }
  if (p >= ziel && e.schwerNoetig && !e.schwerOk && vor(warte.findIndex((x) => lernIstSchwer(x) && x !== letzte && !x.geloest))) return;
  if (p >= ziel && e.schwerNoetig && !e.schwerOk && vor(warte.findIndex((x) => lernIstSchwer(x) && x !== letzte))) return;
  const reihe = soll === 3 ? [3, 2, 1] : soll === 2 ? [2, 3, 1] : [1, 2, 3];
  const neuZ = (x) => e.sitzt || !e.gezaehlt || !e.gezaehlt.has(Number(x.id)); // H3: solange es ungezählte gibt, keine schon gezählte
  for (const ok of [(x) => !x.geloest && !x.falschHeute && neuZ(x), (x) => !x.geloest && neuZ(x), (x) => !x.geloest && !x.falschHeute, (x) => !x.geloest, (x) => x !== letzte])
    for (const st of reihe)
      for (const ex of [(x) => anders(x) && neuTyp(x), anders])
        if (vor(warte.findIndex((x) => (x.stufe || 2) === st && ok(x) && ex(x)))) return;
  for (const ok of [(x) => !x.geloest && !x.falschHeute, (x) => !x.geloest, (x) => x !== letzte])
    for (const st of reihe)
      if (vor(warte.findIndex((x) => (x.stufe || 2) === st && ok(x)))) return;
}
`;
const L = new Function(code + '\n' + ALT + '\nreturn { lernWaehleBordkarte, lernWaehleAlt, lernFormPlatz, lernAnwendenFehlt, lernIstAnwenden, LERN_TYP };')();
const { lernWaehleBordkarte: waehle, lernWaehleAlt, lernFormPlatz, lernAnwendenFehlt } = L;

const k = (id, stufe = 1, typ = null, mehr = {}) => ({ id, stufe, typ, frage: { text: `Aufgabe ${id}: rechne ${id} + 3 und dann noch etwas Nummer ${'x'.repeat(id % 7)}.` }, ...mehr });
// Ablauf wie in der App: Auswahl → warte[0] wird bearbeitet (richtig: gelöst, hinten an) → nächster Platz
function ablauf(warte, e, n, { formJede = 3, bearbeitungen = 0, falsch = [] } = {}) {
  const gesehen = new Set(); let letzte = null, fehlFolge = 0, nachFehler = false; const folge = [];
  for (let i = 0; i < n; i++) {
    const grund = waehle(warte, e, letzte, gesehen, { formJede, platz: bearbeitungen + i + 1, nachFehler, letzteFalsch: fehlFolge > 0 });
    const a = warte.shift(); folge.push({ id: a.id, form: a.form || null, grund }); letzte = a; if (a.typ) gesehen.add(a.typ); nachFehler = false;
    const richtig = !falsch.includes(i + 1);
    if (richtig) a.geloest = true; else a.falschHeute = true;
    warte.push(a); fehlFolge = richtig ? 0 : fehlFolge + 1; if (fehlFolge === 2) nachFehler = true;
  }
  return folge;
}
const TYPEN = Object.keys(L.LERN_TYP);

test('Alter Server (keine Aufgabe mit form, keine Sachaufgaben-Felder): Auswahl genau wie 0.93.8 – 4000 Zufallsfälle', () => {
  let s = 12345; const zuf = () => { s = (s * 1103515245 + 12345) % 2147483648; return s / 2147483648; };
  const wahl = (l) => l[Math.floor(zuf() * l.length)];
  for (let fall = 0; fall < 4000; fall++) {
    const n = 1 + Math.floor(zuf() * 9);
    const roh = Array.from({ length: n }, (_, i) => ({ id: i + 1, stufe: wahl([1, 2, 3, undefined]), typ: zuf() < 0.25 ? null : wahl(TYPEN), geloest: zuf() < 0.3, falschHeute: zuf() < 0.2,
      frage: { text: wahl(['Rechne 3 + 4.', 'Rechne 5 + 9.', 'Wie viel ist das Doppelte von 7?', `Text ${i}`]) } }));
    const e = { ziel: wahl([2, 4, 6]), serie: Math.floor(zuf() * 7), neueRegel: zuf() < 0.6, eigene: Math.floor(zuf() * 7), stufeSenkung: wahl([0, 0, 1, 2]), schwerNoetig: zuf() < 0.4, schwerOk: zuf() < 0.5,
      sitzt: zuf() < 0.1, gezaehlt: zuf() < 0.5 ? new Set(roh.filter(() => zuf() < 0.4).map((x) => x.id)) : undefined, folge: 3, folgeZiel: 3 };
    const gesehen = new Set(TYPEN.filter(() => zuf() < 0.2)); const li = zuf() < 0.3 ? -1 : Math.floor(zuf() * n);
    const w1 = roh.map((x) => ({ ...x })), w2 = roh.map((x) => ({ ...x }));
    lernWaehleAlt(w1, e, li < 0 ? null : w1[li], new Set(gesehen));
    waehle(w2, e, li < 0 ? null : w2[li], new Set(gesehen), { formJede: wahl([0, 3, undefined]), platz: 1 + Math.floor(zuf() * 9), nachFehler: zuf() < 0.3, letzteFalsch: zuf() < 0.5 });
    assert.deepEqual(w2.map((x) => x.id), w1.map((x) => x.id), `Fall ${fall}`);
  }
});

test('Takt: form_jede 3 → Platz 3 und 6 mit form, 1, 2, 4, 5 ohne', () => {
  const w = [k(1, 1, 'direkt'), k(2, 1, 'erkennen'), k(3, 1, 'direkt'), k(4, 1, 'erkennen'), k(5, 1, 'direkt'), k(6, 1, 'erkennen'),
    k(21, 1, 'erkennen', { form: 'zwei_wege' }), k(22, 1, 'direkt', { form: 'umkehren' }), k(23, 1, 'direkt', { form: 'bruecke' })];
  const f = ablauf(w, { ziel: 6, neueRegel: true, eigene: 0 }, 6);
  assert.deepEqual(f.map((x) => !!x.form), [false, false, true, false, false, true], JSON.stringify(f));
  assert.deepEqual(f.filter((x) => x.form).map((x) => x.grund), ['form', 'form']);
  // ohne form_jede (alter Server) kommen die Bordkarten mit form nicht vor den ungelösten ohne form
  const w2 = [k(21, 1, 'erkennen', { form: 'zwei_wege' }), k(1, 1, 'direkt'), k(2, 1, 'erkennen'), k(3, 1, 'direkt')];
  assert.deepEqual(ablauf(w2, { ziel: 6, neueRegel: true, eigene: 0 }, 3, { formJede: 0 }).map((x) => x.id), [1, 2, 3]);
  // Vorrat ohne form verbraucht → dann dürfen auch Bordkarten mit form kommen
  const w3 = [k(1, 1, 'direkt'), k(21, 1, 'erkennen', { form: 'zwei_wege' }), k(22, 1, 'direkt', { form: 'umkehren' })];
  assert.deepEqual(ablauf(w3, { ziel: 6, neueRegel: true, eigene: 0 }, 3, { formJede: 0 }).map((x) => x.id), [1, 21, 22]);
});

test('Takt: bearbeitungen vom Server verschieben den Platz (2 → die erste Bordkarte der Sitzung hat form)', () => {
  const w = () => [k(1, 1, 'direkt'), k(2, 1, 'erkennen'), k(3, 1, 'direkt'), k(4, 1, 'erkennen'), k(21, 1, 'erkennen', { form: 'zwei_wege' }), k(22, 1, 'direkt', { form: 'umkehren' })];
  assert.deepEqual(ablauf(w(), { ziel: 6, neueRegel: true, eigene: 0 }, 4, { bearbeitungen: 2 }).map((x) => !!x.form), [true, false, false, true]);
  assert.deepEqual(ablauf(w(), { ziel: 6, neueRegel: true, eigene: 0 }, 3, { bearbeitungen: 7 }).map((x) => !!x.form), [false, true, false]);
  assert.deepEqual([lernFormPlatz(3, 3), lernFormPlatz(4, 3), lernFormPlatz(6, 3), lernFormPlatz(3, 0), lernFormPlatz(3, undefined), lernFormPlatz(4, 2)], [true, false, true, false, false, true]);
});

test('Takt: keine ungelöste Bordkarte mit form in der Stufe, die dran ist → normale Bordkarte, nichts aufgestaut', () => {
  const w = [k(1, 1, 'direkt'), k(2, 1, 'erkennen'), k(3, 1, 'direkt'), k(4, 1, 'erkennen'), k(31, 3, 'begruenden', { form: 'zwei_wege' })];
  const f = ablauf(w, { ziel: 6, neueRegel: true, eigene: 0 }, 4);
  assert.deepEqual(f.map((x) => x.id), [1, 2, 3, 4], 'Stufe 1 ist dran, die Form-Bordkarte ist Stufe 3');
  // gelöste Form-Bordkarte zählt nicht als Vorrat
  const w2 = [k(1, 1, 'direkt'), k(2, 1, 'erkennen'), k(3, 1, 'direkt'), k(21, 1, 'erkennen', { form: 'zwei_wege', geloest: true })];
  assert.equal(ablauf(w2, { ziel: 6, neueRegel: true, eigene: 0 }, 3)[2].form, null);
  // nie zweimal derselbe Typ: die einzige Form-Bordkarte hat den Typ der letzten → normale
  const w3 = [k(1, 1, 'direkt'), k(2, 1, 'erkennen'), k(3, 1, 'direkt'), k(21, 1, 'erkennen', { form: 'zwei_wege' })];
  const f3 = ablauf(w3, { ziel: 6, neueRegel: true, eigene: 0 }, 3);
  assert.equal(f3[1].id, 2); assert.equal(f3[2].form, null, 'nach „erkennen“ nicht die „erkennen“-Form-Bordkarte');
});

test('Nach zwei Fehlern in Folge: einmal ein Lückenweg, nie zwei hintereinander; kein Fehler-Detektiv direkt nach einem Fehler', () => {
  const w = [k(1, 1, 'direkt'), k(2, 1, 'erkennen'), k(3, 1, 'direkt'), k(4, 1, 'erkennen'), k(5, 1, 'direkt'),
    k(41, 2, 'mehrschritt', { form: 'lueckenweg', zaehlt: 'nein' }), k(42, 2, 'mehrschritt', { form: 'lueckenweg', zaehlt: 'nein' })];
  const f = ablauf(w, { ziel: 6, neueRegel: true, eigene: 0 }, 5, { formJede: 0, falsch: [1, 2, 3] });
  assert.equal(f[2].form, 'lueckenweg'); assert.equal(f[2].grund, 'lueckenweg');
  assert.notEqual(f[3].form, 'lueckenweg', 'kein zweiter Lückenweg direkt danach, auch nach dem dritten Fehler');
  // ohne ungelösten Lückenweg: normale Auswahl
  const w2 = [k(1, 1, 'direkt'), k(2, 1, 'erkennen'), k(3, 1, 'direkt'), k(41, 2, 'mehrschritt', { form: 'lueckenweg', geloest: true })];
  assert.notEqual(ablauf(w2, { ziel: 6, neueRegel: true, eigene: 0 }, 3, { formJede: 0, falsch: [1, 2] })[2].id, 41);
  // Fehler-Detektiv: auf dem Form-Platz nach einem Fehler nicht, eine andere Form schon
  const d = () => [k(1, 1, 'direkt'), k(2, 1, 'erkennen'), k(3, 1, 'direkt'), k(51, 1, 'fehler', { form: 'fehler_detektiv' })];
  assert.equal(ablauf(d(), { ziel: 6, neueRegel: true, eigene: 0 }, 3, { falsch: [2] })[2].form, null);
  assert.equal(ablauf(d(), { ziel: 6, neueRegel: true, eigene: 0 }, 3)[2].form, 'fehler_detektiv', 'ohne Fehler davor darf er kommen');
  const d2 = [...d(), k(52, 1, 'umkehr', { form: 'umkehren' })];
  assert.equal(ablauf(d2, { ziel: 6, neueRegel: true, eigene: 0 }, 3, { falsch: [2] })[2].form, 'umkehren');
});

test('Sachaufgabe fehlt noch: nächste Bordkarte ist eine ungelöste, zählende Sachaufgabe; schwere Bordkarte hat Vorrang', () => {
  const voll = { ziel: 2, neueRegel: true, eigene: 2, folge: 2, folgeZiel: 2, typenAnzahl: 2, typenNoetig: 2, anwendenNoetig: true, anwendenOk: false };
  assert.equal(lernAnwendenFehlt(voll), true);
  assert.deepEqual([lernAnwendenFehlt({ ...voll, anwendenOk: true }), lernAnwendenFehlt({ ...voll, eigene: 1 }), lernAnwendenFehlt({ ...voll, folge: 1 }),
    lernAnwendenFehlt({ ...voll, schwerNoetig: true, schwerOk: false }), lernAnwendenFehlt({ ...voll, anwendenNoetig: undefined }), lernAnwendenFehlt({ ...voll, neueRegel: false })],
  [false, false, false, false, false, false]);
  const w = () => [k(1, 3, 'begruenden'), k(2, 2, 'mehrschritt'), k(61, 2, 'einkleidung', { zaehlt: 'nein' }), k(62, 2, 'einkleidung', { geloest: true }), k(63, 3, 'transfer')];
  const w1 = w(); assert.equal(waehle(w1, voll, null, new Set(), {}), 'anwenden'); assert.equal(w1[0].id, 63);
  const w2 = [k(1, 3, 'begruenden'), k(64, 2, 'pruefung', { form: 'anwenden' })]; waehle(w2, voll, null, new Set(), {}); assert.equal(w2[0].id, 64);
  // Vorrang vor dem Takt
  const w3 = [k(1, 3, 'begruenden'), k(21, 3, 'parameter', { form: 'zwei_wege' }), k(65, 2, 'einkleidung')]; waehle(w3, voll, null, new Set(), { formJede: 3, platz: 3 }); assert.equal(w3[0].id, 65);
  // aber nicht vor „schwere Bordkarte noch nötig“
  const w4 = [k(65, 2, 'einkleidung'), k(1, 3, 'begruenden'), k(21, 2, 'umkehr', { form: 'umkehren' })]; const g4 = waehle(w4, { ...voll, schwerNoetig: true, schwerOk: false }, null, new Set(), { formJede: 3, platz: 3 });
  assert.deepEqual([g4, w4[0].id], ['schwer', 1]);
});

// Werkstatt 1039/1040: beide Verbote über alle Vorränge und Rückfälle; Pflicht „schwer“ nur mit zählenden Aufgaben
test('Nie zwei Lückenwege hintereinander – auch auf dem Form-Platz und in der allgemeinen Auswahl', () => {
  const lz = k(40, 1, 'mehrschritt', { form: 'lueckenweg', geloest: true });
  const e = { ziel: 6, neueRegel: true, eigene: 0 };
  // nachgewiesener Fall: Platz 3, ungelöst ein weiterer Lückenweg und eine normale Aufgabe
  const w1 = [k(41, 1, 'direkt', { form: 'lueckenweg' }), k(1, 1, 'erkennen'), lz];
  assert.deepEqual([waehle(w1, e, lz, new Set(), { formJede: 3, platz: 3 }), w1[0].id], ['normal', 1]);
  // mit einer Brücke: die andere Form auf dem Form-Platz
  const w2 = [k(41, 1, 'direkt', { form: 'lueckenweg' }), k(42, 1, 'erkennen', { form: 'bruecke' }), lz];
  assert.deepEqual([waehle(w2, e, lz, new Set(), { formJede: 3, platz: 3 }), w2[0].id], ['form', 42]);
  // allgemeine Auswahl (kein Form-Platz, alle normalen gelöst)
  const w3 = [k(41, 1, 'direkt', { form: 'lueckenweg' }), k(1, 1, 'erkennen', { geloest: true }), lz];
  assert.deepEqual([waehle(w3, e, lz, new Set(), { formJede: 3, platz: 4 }), w3[0].id], ['normal', 1]);
  // Gegenprobe Vorrat leer: nur noch der Lückenweg → er darf kommen (Notfall)
  const w4 = [k(41, 1, 'direkt', { form: 'lueckenweg' }), lz];
  assert.deepEqual([waehle(w4, e, lz, new Set(), { formJede: 3, platz: 3 }), w4[0].id], ['notfall', 41]);
});

test('Kein Fehler-Detektiv nach eigenem Fehler – auch beim Schwer-Vorrang und in jedem Rückfall', () => {
  const e = { ziel: 6, neueRegel: true, eigene: 6, schwerNoetig: true, schwerOk: false };
  const letzte = k(9, 1, 'direkt', { falschHeute: true });
  // nachgewiesener Fall: einzige schwere ist ein Fehler-Detektiv, eine normale leichte ist da
  const w1 = [k(51, 3, 'begruenden', { form: 'fehler_detektiv' }), k(1, 1, 'erkennen'), letzte];
  assert.deepEqual([waehle(w1, e, letzte, new Set(), { formJede: 3, platz: 4, letzteFalsch: true }), w1[0].id], ['normal', 1]);
  // ohne Fehler davor: der Detektiv ist die schwere
  const w2 = [k(1, 1, 'erkennen'), k(51, 3, 'begruenden', { form: 'fehler_detektiv' }), letzte];
  assert.deepEqual([waehle(w2, e, letzte, new Set(), { formJede: 3, platz: 4 }), w2[0].id], ['schwer', 51]);
  // die schwere wird nachgeholt: nach einer richtigen Antwort kommt sie
  const w3 = [k(1, 1, 'erkennen', { geloest: true }), k(51, 3, 'begruenden', { form: 'fehler_detektiv' })];
  assert.deepEqual([waehle(w3, e, w3[0], new Set(), { formJede: 3, platz: 5 }), w3[0].id], ['schwer', 51]);
  // Gegenprobe Vorrat leer: nur der Detektiv (und die gelöste letzte) → er darf kommen (Notfall)
  const l4 = k(9, 1, 'direkt', { geloest: true });
  const w4 = [k(51, 3, 'begruenden', { form: 'fehler_detektiv' }), l4];
  assert.deepEqual([waehle(w4, e, l4, new Set(), { formJede: 3, platz: 4, letzteFalsch: true }), w4[0].id], ['notfall', 51]);
  // Sachaufgabe fehlt: ein Detektiv mit Sachaufgaben-Typ wird nach einem Fehler nicht gezogen
  const voll = { ziel: 2, neueRegel: true, eigene: 2, folge: 2, folgeZiel: 2, typenAnzahl: 2, typenNoetig: 2, anwendenNoetig: true, anwendenOk: false };
  const w5 = [k(66, 2, 'einkleidung', { form: 'fehler_detektiv' }), k(2, 2, 'mehrschritt'), letzte];
  waehle(w5, voll, letzte, new Set(), { letzteFalsch: true }); assert.equal(w5[0].id, 2);
});

test('Pflicht „schwere Aufgabe“: Aufgaben mit zaehlt = nein zählen nicht', () => {
  const e = { ziel: 6, neueRegel: true, eigene: 6, schwerNoetig: true, schwerOk: false };
  // ungelöst: die normale Auswahl darf sie (Stufe 3 ist dran) ziehen, aber nicht als „die schwere“
  const w0 = [k(1, 1, 'erkennen'), k(71, 3, 'begruenden', { zaehlt: 'nein' }), k(21, 1, 'direkt', { form: 'zwei_wege' })];
  assert.notEqual(waehle(w0, e, null, new Set(), {}), 'schwer');
  // gelöst: der Schwer-Vorrang (letzte Stufe nimmt auch gelöste) zog sie bisher; jetzt kommt die ungelöste normale
  const w1 = [k(1, 1, 'erkennen'), k(71, 3, 'begruenden', { zaehlt: 'nein', geloest: true }), k(21, 1, 'direkt', { form: 'zwei_wege', geloest: true })];
  assert.deepEqual([waehle(w1, e, null, new Set(), {}), w1[0].id], ['normal', 1]);
  const w2 = [k(1, 1, 'erkennen'), k(71, 3, 'begruenden', { zaehlt: 'nein' }), k(72, 3, 'begruenden')];
  waehle(w2, e, null, new Set(), {}); assert.equal(w2[0].id, 72, 'die zählende schwere (alter Weg, ohne form)');
  const w2f = [k(1, 1, 'erkennen'), k(71, 3, 'begruenden', { zaehlt: 'nein' }), k(72, 3, 'begruenden', { form: 'zwei_wege' })];
  assert.deepEqual([waehle(w2f, e, null, new Set(), {}), w2f[0].id], ['schwer', 72]);
  // auch auf dem alten Weg (keine form): die nicht zählende schwere ist nicht „die schwere“
  const w3 = [k(1, 1, 'erkennen'), k(71, 3, 'begruenden', { zaehlt: 'nein', geloest: true })];
  waehle(w3, e, null, new Set(), {}); assert.equal(w3[0].id, 1);
});

test('Invarianten über 20000 Zufallslagen mit form: kein Lückenweg nach Lückenweg, kein Detektiv nach Fehler (außer nichts anderes wählbar), schwer zählt', () => {
  let s = 777; const zuf = () => { s = (s * 1103515245 + 12345) % 2147483648; return s / 2147483648; };
  const wahl = (l) => l[Math.floor(zuf() * l.length)];
  const FORMEN = [null, null, 'lueckenweg', 'fehler_detektiv', 'bruecke', 'zwei_wege', 'umkehren', 'anwenden'];
  let notfall = 0, sperrFaelle = 0;
  for (let fall = 0; fall < 20000; fall++) {
    const n = 1 + Math.floor(zuf() * 8);
    const w = Array.from({ length: n }, (_, i) => ({ id: i + 1, stufe: wahl([1, 2, 3, undefined]), typ: zuf() < 0.2 ? null : wahl(TYPEN), form: wahl(FORMEN) || undefined,
      zaehlt: zuf() < 0.2 ? 'nein' : undefined, geloest: zuf() < 0.35, falschHeute: zuf() < 0.2, frage: { text: wahl(['Rechne 3 + 4.', 'Rechne 5 + 9.', `Text ${i}`]) } }));
    if (!w.some((x) => x.form)) w[0].form = wahl(['lueckenweg', 'fehler_detektiv']);
    const e = { ziel: wahl([2, 4, 6]), neueRegel: true, eigene: Math.floor(zuf() * 7), stufeSenkung: wahl([0, 0, 1]), schwerNoetig: zuf() < 0.5, schwerOk: zuf() < 0.3,
      gezaehlt: zuf() < 0.5 ? new Set(w.filter(() => zuf() < 0.4).map((x) => x.id)) : undefined, typenNoetig: 0, typenAnzahl: 0, folge: 3, folgeZiel: 3,
      anwendenNoetig: zuf() < 0.3, anwendenOk: zuf() < 0.5 };
    const letzte = zuf() < 0.15 ? null : w[Math.floor(zuf() * n)];
    const takt = { formJede: wahl([0, 3, 3, 2]), platz: 1 + Math.floor(zuf() * 9), nachFehler: zuf() < 0.3, letzteFalsch: zuf() < 0.5 };
    const grund = waehle(w, e, letzte, new Set(TYPEN.filter(() => zuf() < 0.2)), takt);
    const x = w[0];
    const gesperrt = (y) => (letzte?.form === 'lueckenweg' && y.form === 'lueckenweg') || (takt.letzteFalsch && y.form === 'fehler_detektiv');
    if (gesperrt(x)) {
      sperrFaelle++;
      assert.ok(!w.some((y) => !gesperrt(y) && (y !== letzte || !y.geloest) && [1, 2, 3].includes(y.stufe || 2)), `Fall ${fall}: gesperrte Bordkarte ${x.id}, obwohl eine erlaubte da ist`);
    }
    if (grund === 'notfall') { notfall++; assert.ok(!w.some((y) => !gesperrt(y) && (y !== letzte || !y.geloest)), `Fall ${fall}: Notfall ohne Not`); }
    if (grund === 'schwer') assert.ok(x.zaehlt !== 'nein' && !gesperrt(x), `Fall ${fall}: schwer ${x.id}`);
  }
  assert.ok(notfall > 0 && sperrFaelle > 0, `Notfälle ${notfall}, gesperrte Wahl ${sperrFaelle}: beide Zweige kommen vor`);
});
