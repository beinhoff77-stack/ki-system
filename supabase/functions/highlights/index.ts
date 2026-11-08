// highlights (Werkstatt #149): Reisen › Highlights – vom Reisewunsch zum Spot.
// Zugang wie app-api: Sitzungs-Token der App -> app.sitzung() -> Schlüssel; alle Lese-/Schreibaktionen laufen über api.highlights_* als council_mcp.
// Vorschläge: je Portion 5 Steckbrief-Karten von einem KI-Modell über OpenRouter mit Websuche (ZDR + data_collection deny).
//   Die Websuche fällt NICHT unter ZDR – deshalb enthält der Prompt keine Namen, kein Alter, keine Stammdaten.
// Belege: Eine Angabe gilt nur als belegt, wenn ihre URL unter den tatsächlich abgerufenen Suchtreffern (url_citation) ist.
// Bilder: nur Wikimedia Commons mit freier Lizenz (Urheber, Lizenz, Quelle werden mitgespeichert), sonst kein Bild.
// Wege: POST /highlights/aktion { aktion, daten }  (Bearer = App-Token)
//   lesen {suche_id?, knoten_id?, mit_weg?} · merkliste {suche_id?} · suche_speichern {id?, wunsch?, vorlieben?, loeschen?}
//   entscheiden {knoten_id, status offen|gemerkt|weg} · portion {suche_id, parent_id?, art start|mehr|aehnlich|anders|frage, linse?, text?, vorlage_knoten_id?}
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
import postgres from 'npm:postgres@3.4.5'

const VERSION = '0.1.2'
const sql = postgres(Deno.env.get('SUPABASE_DB_URL')!, { prepare: false, max: 3, idle_timeout: 20 })
const OR_KEY = Deno.env.get('OPENROUTER_API_KEY') ?? ''
const MODELL = 'anthropic/claude-sonnet-5.5'
const UA = 'ki-system-highlights/0.1 (https://github.com/beinhoff77-stack/ki-system)'
const CORS = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Content-Type, Authorization', 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS' }
const antwort = (body: unknown, status = 200) => new Response(JSON.stringify(body), { status, headers: { ...CORS, 'Content-Type': 'application/json' } })

const API: Record<string, string> = {
  lesen: 'highlights_lesen', merkliste: 'highlights_merkliste', suche_speichern: 'highlights_suche_speichern',
  entscheiden: 'highlights_entscheiden', portion: 'highlights_portion_anlegen',
}
async function api(fn: string, h: string, daten: unknown): Promise<any> {
  return await sql.begin(async (tx) => {
    await tx`set local role council_mcp`
    const z = await tx.unsafe(`select api.${fn}($1::text, $2::text::jsonb) as r`, [h, JSON.stringify(daten ?? {})])
    return z[0].r
  })
}
function fehlertext(e: any): string {
  if (e?.code === 'P0001') return String(e.message)
  console.error('highlights', e?.code, e?.message)
  return 'Interner Fehler – bitte später erneut versuchen.'
}

// ---------- KI ----------
const TYPEN = ['region', 'ort', 'stadt', 'viertel', 'tauchen', 'tiere', 'natur', 'tempel', 'altstadt', 'museum', 'restaurant', 'unterkunft', 'erlebnis']
const FACH: Record<string, string> = {
  tauchen: 'Tiefe/Wasser/Sicht · Begegnung', tiere: 'Was man sieht · Wie nah', natur: 'Strecke/Höhenmeter · Schwierigkeit',
  tempel: 'Eintritt/Regeln · Führung nötig?', altstadt: 'Echtheit · Dauer zu Fuß', museum: 'Schwerpunkt · Dauer',
  viertel: 'Essen · Ruhe', restaurant: 'Gästenote+Anzahl · Reservierung', unterkunft: 'Preis/Nacht · Lage',
  region: 'Charakter · Anreise', ort: 'Charakter · Lage', stadt: 'Charakter · Wie viele Tage', erlebnis: 'Anbieter · Buchung',
}
const LINSEN: Record<string, string> = {
  highlights: 'die stärksten Highlights jeder Art', tauchen: 'Tauchen und Schnorcheln', tiere: 'Tierbegegnungen in freier Natur',
  wohnen: 'wo man stilvoll wohnt (Orte/Viertel, keine Einzelbuchung)', kinder: 'was Kinder im Schulalter begeistert', essen: 'Essen und Restaurants',
  abend: 'Abende und Ausgehen', natur: 'Natur, Wandern, Landschaft', kultur: 'Kultur, Geschichte, Architektur',
}

function prompt(k: any): string {
  const p = k.portion, v = k.vorlieben ?? {}, pfad = (k.pfad ?? []).map((x: any) => x.titel)
  const eltern = k.eltern ? `${k.eltern.titel} (${k.eltern.typ})` : null
  const vorhanden = (k.vorhanden ?? []).map((x: any) => `${x.titel} [${x.status}]`)
  let auftrag = ''
  if (p.art === 'start' || p.art === 'mehr') auftrag = vorhanden.length ? 'Liefere die nächsten 5 starken Vorschläge, die noch NICHT in der Liste „schon gezeigt“ stehen.' : 'Liefere die 5 stärksten Vorschläge.'
  if (p.art === 'aehnlich') auftrag = `Liefere 5 Vorschläge, die ähnlich begeistern wie „${k.vorlage?.titel}“ (${k.vorlage?.moment ?? k.vorlage?.typ}), aber nicht in „schon gezeigt“ stehen.`
  if (p.art === 'anders') auftrag = `Liefere 5 Vorschläge einer bewusst ANDEREN Art als die bisherigen (bisherige Typen: ${[...new Set((k.vorhanden ?? []).map((x: any) => x.typ))].join(', ') || 'keine'}).`
  if (p.art === 'frage') auftrag = `Beantworte diese Frage mit bis zu 5 passenden Vorschlägen: „${p.text}“.`
  const linse = p.linse && LINSEN[p.linse] ? `Schwerpunkt (Linse): ${LINSEN[p.linse]}.` : ''
  const ebene = !eltern
    ? 'Ebene: oberste Ebene zu diesem Wunsch. Ist der Wunsch ein Land oder größerer Raum, schlage Regionen/Inseln/Orte vor; ist er schon eine Region, schlage Orte und Erlebnisse darin vor.'
    : `Ebene: eine Stufe feiner als „${eltern}“, ausschließlich innerhalb davon. Region → Orte/Erlebnisse; Stadt/Ort → Viertel, Spots, Restaurants; Erlebnis/Spot → konkrete Anbieter/Touren, beste Plätze, Essen/Wohnen in der Nähe.`
  return `Du bist ein erfahrener, stilsicherer Reiseberater für eine Taucherfamilie (2 Erwachsene, 2 Kinder im Schulalter, alle tauchen). Geschmack: individuell, beeindruckend, kein Massentourismus, Stil statt Protz; gutes Budget, wenn es sich lohnt.
Reisewunsch: „${k.wunsch}“
Pfad: ${pfad.length ? pfad.join(' › ') : '(oberste Ebene)'}
${ebene}
${linse}
${v.reisezeit ? `Reisezeit (nur für Saison-Einschätzung): ${v.reisezeit}.` : 'Reisezeit unbekannt: Saison allgemein beschreiben, status "passt" nur wenn ganzjährig.'}
${v.andrang_max ? `Vorliebe: Andrang höchstens ${v.andrang_max}/5 – solche Vorschläge nach vorn sortieren. NICHTS ausschließen: ein großes Highlight mit mehr Andrang darf trotzdem kommen, dann mit gutem „ruhig“-Tipp.` : 'Nichts ausschließen; Reihenfolge = was am besten passt.'}
Schon gezeigt (nicht wiederholen): ${vorhanden.length ? vorhanden.join('; ') : 'nichts'}
Gemerkt (Signal für Geschmack): ${(k.gemerkt_sonst ?? []).join('; ') || 'nichts'}
Weggewischt (eher weniger davon, aber nicht ausschließen): ${(k.weg_sonst ?? []).join('; ') || 'nichts'}
AUFTRAG: ${auftrag}
Nutze die Websuche für aktuelle Fakten (Preise, Saison, Regeln, Mindestalter). Suche je Vorschlag ausdrücklich nach aktuellen Sperrungen/Warnhinweisen (offizielle Park-, Behörden- oder Anbieterseite); findest du welche, schreibe sie in "warnung". Erfinde nichts. Eine *_quelle nur angeben, wenn genau diese Seite die Angabe enthält, sonst null.
Gibt es keine 5 wirklich starken Vorschläge mehr, liefere weniger und setze "ende": true mit kurzem "ende_hinweis". Niemals auffüllen.
Andrang-Skala: 1 kaum touristisch · 2 lokaler Alltag · 3 bekannter Stopp · 4 Busgruppen · 5 Massentourismus.
Fachwerte je Typ (genau 2, label + wert): ${Object.entries(FACH).map(([t, f]) => `${t}: ${f}`).join(' | ')}.
Antworte ausschließlich mit JSON:
{"fazit":"1 Satz: warum diese Reihenfolge (beginnt mit 'Für euch vorn: ')","ende":false,"ende_hinweis":null,
"karten":[{"titel":"kurzer Name","typ":"${TYPEN.join('|')}","bild_suche":"englischer Suchbegriff für ein aktuelles Foto auf Wikimedia Commons: konkretes Motiv + Ort, z. B. 'Australian sea lion Seal Bay' (keine Karten/Satellitenbilder)",
"moment":"1 Satz: was man dort erlebt, bildhaft",
"wow":1-5,"andrang":1-5,"andrang_quelle":"URL oder null",
"zeit":"z. B. 3 h, 1 Tag, 2–3 Tage","kosten_4":"Betrag für 4 Personen in Landeswährung, gerundet, z. B. ca. 620 AUD; oder 'frei'","kosten_quelle":"URL oder null",
"mindestalter":null oder Zahl (für Kinder, z. B. Tauch-/Tourregel),"familie_hinweis":"nur falls ein Familienmitglied nicht mitkann/eingeschränkt ist, sonst null",
"saison":{"text":"kurz, z. B. Mai–Aug, Höhepunkt Juni","status":"passt|grenzwertig|falsch|unbekannt"},"tageszeit":"beste Tageszeit kurz",
"fach":[{"label":"…","wert":"…"},{"label":"…","wert":"…"}],
"lohnt":"Lohnt sich, wenn … (1 Satz)","eher_nicht":"Eher nicht, wenn … (1 Satz)",
"frage":"die entscheidende offene Frage vor dem Buchen","pruefen":{"text":"was/wo prüfen","url":"URL oder null"},
"ruhig":"1 Tipp, wie man es ruhiger erlebt","warnung":"aktuelle Sperrung/Einschränkung mit Datum oder null","warnung_quelle":"URL oder null","lat":0.0,"lon":0.0,"quellen":["https://…"]}]}`
}

async function kiPortion(k: any) {
  const r = await fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST', signal: AbortSignal.timeout(200_000),
    headers: { Authorization: `Bearer ${OR_KEY}`, 'Content-Type': 'application/json', 'X-Title': 'Highlights' },
    body: JSON.stringify({ model: MODELL, messages: [{ role: 'user', content: prompt(k) }], max_tokens: 9000, reasoning: { effort: 'low' },
      plugins: [{ id: 'web', max_results: 8 }], provider: { zdr: true, data_collection: 'deny' }, usage: { include: true } }),
  })
  const text = await r.text()
  if (!r.ok) throw new Error(`OpenRouter ${r.status}: ${text.slice(0, 200)}`)
  const j = JSON.parse(text)
  const msg = j?.choices?.[0]?.message
  const inhalt = String(Array.isArray(msg?.content) ? msg.content.map((x: any) => x?.text ?? '').join('') : msg?.content ?? '').replace(/```(?:json)?/gi, '')
  const s = inhalt.indexOf('{'), e = inhalt.lastIndexOf('}')
  let daten: any = null
  if (s >= 0 && e > s) { try { daten = JSON.parse(inhalt.slice(s, e + 1)) } catch { daten = null } }
  const zitate = new Set<string>(((msg?.annotations ?? []) as any[]).map((a) => a?.url_citation?.url).filter((u: any) => typeof u === 'string'))
  const kosten = Number(j?.usage?.cost ?? 0) || 0
  if (!daten) throw Object.assign(new Error('KI hat kein gültiges JSON geliefert' + (j?.choices?.[0]?.finish_reason === 'length' ? ' (abgeschnitten)' : '')), { kosten })
  return { daten, zitate, kosten, modell: `${j?.model ?? MODELL}${j?.provider ? ' via ' + j.provider : ''}` }
}

const url = (u: unknown) => (typeof u === 'string' && /^https?:\/\/[^\s"<>]+$/.test(u) && !/@/.test(u.split('/')[2] ?? '') ? u : null)
const txt = (s: unknown, n: number) => (typeof s === 'string' && s.trim() ? s.trim().slice(0, n) : null)
const zahl = (x: unknown, lo: number, hi: number) => { const n = Math.round(Number(x)); return Number.isFinite(n) && n >= lo && n <= hi ? n : null }
// belegt nur, wenn die URL wirklich unter den abgerufenen Suchtreffern war (gleiche Adresse ohne #/? oder gleicher Host+Pfad)
function belegt(u: string | null, zitate: Set<string>): boolean {
  if (!u) return false
  const norm = (x: string) => x.replace(/[#?].*$/, '').replace(/\/$/, '').toLowerCase()
  const n = norm(u)
  for (const z of zitate) if (norm(z) === n) return true
  return false
}

function karteBauen(c: any, zitate: Set<string>) {
  const typ = TYPEN.includes(c?.typ) ? c.typ : 'erlebnis'
  const aq = url(c?.andrang_quelle), kq = url(c?.kosten_quelle), pu = url(c?.pruefen?.url)
  const st = ['passt', 'grenzwertig', 'falsch', 'unbekannt'].includes(c?.saison?.status) ? c.saison.status : 'unbekannt'
  const fach = (Array.isArray(c?.fach) ? c.fach : []).slice(0, 2).map((f: any) => ({ label: txt(f?.label, 40), wert: txt(f?.wert, 120) })).filter((f: any) => f.label && f.wert)
  const quellen = [...new Set([...(Array.isArray(c?.quellen) ? c.quellen : []), aq, kq, pu, c?.warnung_quelle].map(url).filter(Boolean))].slice(0, 8)
  return {
    titel: txt(c?.titel, 120), typ, bild_suche: txt(c?.bild_suche, 120),
    steckbrief: {
      moment: txt(c?.moment, 240), wow: zahl(c?.wow, 1, 5), andrang: zahl(c?.andrang, 1, 5), andrang_quelle: aq, andrang_belegt: belegt(aq, zitate),
      zeit: txt(c?.zeit, 40), kosten_4: txt(c?.kosten_4, 90), kosten_quelle: kq, kosten_belegt: belegt(kq, zitate),
      mindestalter: zahl(c?.mindestalter, 0, 25), familie_hinweis: txt(c?.familie_hinweis, 200),
      saison: { text: txt(c?.saison?.text, 80), status: st }, tageszeit: txt(c?.tageszeit, 80), fach,
      lohnt: txt(c?.lohnt, 200), eher_nicht: txt(c?.eher_nicht, 200), frage: txt(c?.frage, 200),
      pruefen: { text: txt(c?.pruefen?.text, 160), url: pu, belegt: belegt(pu, zitate) }, ruhig: txt(c?.ruhig, 200),
      warnung: txt(c?.warnung, 240), warnung_quelle: url(c?.warnung_quelle), warnung_belegt: belegt(url(c?.warnung_quelle), zitate),
      lat: Number.isFinite(Number(c?.lat)) && Number(c.lat) !== 0 ? Number(c.lat) : null, lon: Number.isFinite(Number(c?.lon)) && Number(c.lon) !== 0 ? Number(c.lon) : null,
      geprueft_am: new Date().toISOString().slice(0, 10), bild_suche: txt(c?.bild_suche, 120),
    },
    quellen: quellen.map((u) => ({ url: u, abgerufen: belegt(u as string, zitate) })),
  }
}

// ---------- Bilder: Wikimedia Commons, nur freie Lizenzen ----------
const ohneHtml = (s: unknown) => String(s ?? '').replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim().slice(0, 120)
// Karten, Satellitenbilder, alte Stiche, Logos usw. sind keine guten Kartenfotos
const UNPASSEND = /\b(map|karte|modis|satellite|landsat|sentinel|engraving|lithograph|drawing|illustration|logo|diagram|chart|stamp|coat of arms|1[6-8]\d\d)\b/i
async function commons(suche: string) {
  const q = new URL('https://commons.wikimedia.org/w/api.php')
  for (const [k, v] of Object.entries({ action: 'query', format: 'json', generator: 'search', gsrnamespace: '6', gsrsearch: `${suche} filetype:bitmap`, gsrlimit: '8',
    prop: 'imageinfo', iiprop: 'url|extmetadata|size|mime', iiurlwidth: '960', origin: '*' })) q.searchParams.set(k, v)
  const r = await fetch(q, { headers: { 'User-Agent': UA }, signal: AbortSignal.timeout(12_000) })
  if (!r.ok) return null
  const j = await r.json()
  const seiten = Object.values(j?.query?.pages ?? {}).sort((a: any, b: any) => (a.index ?? 0) - (b.index ?? 0)) as any[]
  for (const s of seiten) {
    const ii = s?.imageinfo?.[0], m = ii?.extmetadata ?? {}
    const lizenz = ohneHtml(m.LicenseShortName?.value)
    if (!ii?.thumburl || !/jpeg|png|webp/.test(ii.mime ?? '') || (ii.width ?? 0) < 800 || (ii.width ?? 0) < (ii.height ?? 0) * 0.9) continue
    if (UNPASSEND.test(String(s.title ?? '').replace(/[_-]/g, ' '))) continue
    if (!/^(cc|public domain|pd)/i.test(lizenz) || /nc|nd/i.test(lizenz)) continue
    return { url: ii.thumburl, quelle_url: ii.descriptionurl, urheber: ohneHtml(m.Artist?.value) || 'unbekannt', lizenz, lizenz_url: url(m.LicenseUrl?.value), quelle: 'Wikimedia Commons' }
  }
  return null
}
async function bildFuer(karte: any, pfad: string[]) {
  const t = String(karte.titel ?? '').replace(/\(.*?\)/g, '').replace(/[:&]/g, ' ').trim()
  const versuche = [...new Set([karte.bild_suche, `${t} ${String(pfad.at(-1) ?? '').replace(/\(.*?\)/g, '')}`.trim(), t].filter(Boolean))]
  for (const v of versuche) { try { const b = await commons(v); if (b) return b } catch { /* nächster Versuch */ } }
  return null
}

async function portionFuellen(id: number) {
  const [{ k }] = await sql`select highlights.portion_kontext(${id}) as k`
  await sql`update highlights.portion set status = 'laeuft' where id = ${id}`
  let kosten = 0, modell = MODELL
  try {
    if (!OR_KEY) throw new Error('OPENROUTER_API_KEY fehlt')
    const ki = await kiPortion(k); kosten = ki.kosten; modell = ki.modell
    const karten = (Array.isArray(ki.daten?.karten) ? ki.daten.karten : []).slice(0, 5).map((c: any) => karteBauen(c, ki.zitate)).filter((c: any) => c.titel)
    const pfad = (k.pfad ?? []).map((x: any) => x.titel)
    const bilder = await Promise.all(karten.map((c: any) => bildFuer(c, pfad)))
    karten.forEach((c: any, i: number) => { c.bild = bilder[i] })
    await sql`select highlights.portion_abschliessen(${id}, ${JSON.stringify({ karten, fazit: txt(ki.daten?.fazit, 400), ende: !!ki.daten?.ende,
      ende_hinweis: txt(ki.daten?.ende_hinweis, 400), kosten_usd: kosten, modell })}::text::jsonb)`
  } catch (e) {
    console.error('highlights portion', id, (e as any)?.message)
    await sql`select highlights.portion_abschliessen(${id}, ${JSON.stringify({ fehler: String((e as any)?.message ?? e).slice(0, 300), kosten_usd: (e as any)?.kosten ?? kosten, modell })}::text::jsonb)`
  }
}

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: CORS })
  const pfad = new URL(req.url).pathname.replace(/^.*\/highlights/, '')
  if (req.method === 'GET') return antwort({ ok: true, version: VERSION, aktionen: Object.keys(API) })
  // Interner Weg (Motor-Token, z. B. per pg_net): Portion erneut füllen bzw. Test ohne App-Sitzung
  if (req.method === 'POST' && pfad === '/fuellen') {
    const mt = req.headers.get('x-motor-token') ?? ''
    const [ok] = mt ? await sql`select (token = ${mt}) as ok from core.motor_geheimnis where id = 1` : [null]
    if (!ok?.ok) return antwort({ ok: false, fehler: 'Nicht erlaubt' }, 401)
    const b = await req.json().catch(() => ({}))
    if (b.bilder_suche_id) {
      // fehlende Bilder einer Suche nachholen (Wikimedia, nur freie Lizenzen)
      const ks = await sql`select id, titel, steckbrief->>'bild_suche' as bild_suche, highlights.pfad(parent_id) as pfad from highlights.knoten where suche_id = ${Number(b.bilder_suche_id)} and bild is null limit 25`
      let n = 0
      for (const k of ks) {
        const bild = await bildFuer({ titel: k.titel, bild_suche: k.bild_suche }, (k.pfad ?? []).map((x: any) => x.titel))
        if (bild) { await sql`update highlights.knoten set bild = ${JSON.stringify(bild)}::text::jsonb where id = ${k.id}`; n++ }
      }
      return antwort({ ok: true, bilder: n, von: ks.length })
    }
    await portionFuellen(Number(b.portion_id))
    return antwort({ ok: true, portion_id: Number(b.portion_id) })
  }
  if (req.method !== 'POST' || pfad !== '/aktion') return antwort({ ok: false, fehler: 'Nicht gefunden' }, 404)
  const t = (req.headers.get('authorization') ?? '').replace(/^Bearer\s+/i, '').trim()
  const [row] = t ? await sql`select app.sitzung(${t}) as h` : [null]
  const h = row?.h
  if (!h) return antwort({ ok: false, fehler: 'Nicht angemeldet' }, 401)
  let b: any
  try { b = await req.json() } catch { return antwort({ ok: false, fehler: 'Ungültiges JSON' }, 400) }
  const fn = API[String(b?.aktion ?? '')]
  if (!fn) return antwort({ ok: false, fehler: `Unbekannte Aktion "${b?.aktion}"` }, 400)
  try {
    const r = await api(fn, h, b.daten ?? {})
    if (b.aktion === 'portion' && r?.portion_id) {
      // @ts-ignore EdgeRuntime gibt es in Supabase Edge Functions
      EdgeRuntime.waitUntil(portionFuellen(Number(r.portion_id)))
    }
    return antwort({ ok: true, ergebnis: r })
  } catch (e) { return antwort({ ok: false, fehler: fehlertext(e) }, 400) }
})
