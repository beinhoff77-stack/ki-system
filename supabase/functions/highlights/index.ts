// highlights (Werkstatt #149): Reisen › Highlights – vom Reisewunsch zum Spot.
// Zugang wie app-api: Sitzungs-Token der App -> app.sitzung() -> Schlüssel; alle Lese-/Schreibaktionen laufen über api.highlights_* als council_mcp.
// V2 (W154): Stufe 1 Regionen (bis 15) -> automatisch Stufe 2 je Region (bis 12 Highlights) -> Stufe 3 nur auf Ansage (bis 8).
// Vorschläge: je Portion Steckbrief-Karten von einem KI-Modell über OpenRouter mit Websuche (ZDR + data_collection deny).
//   Die Websuche fällt NICHT unter ZDR – deshalb enthält der Prompt keine Namen, kein Alter, keine Stammdaten.
// Belege: Eine Angabe gilt nur als belegt, wenn ihre URL unter den tatsächlich abgerufenen Suchtreffern (url_citation) ist.
// Bilder: Wikipedia-Titelbild + Commons-Kandidaten (nur freie Lizenz), Bildmodell wählt das aussagekräftigste; Foto nur, wenn ein passendes gefunden wird.
// Wege: POST /highlights/aktion { aktion, daten }  (Bearer = App-Token)
//   lesen {suche_id?, knoten_id?, mit_weg?} · merkliste {suche_id?} · suche_speichern {id?, wunsch?, vorlieben?, loeschen?}
//   entscheiden {knoten_id, status offen|gemerkt|weg} · portion {suche_id, parent_id?, art start|mehr|aehnlich|anders|frage, linse?, text?, vorlage_knoten_id?}
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
import postgres from 'npm:postgres@3.4.5'

const VERSION = '0.4.4'
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

// ---------- KI (V2, W154) ----------
// Drei Stufen: (1) Regionen des Wunsches mit ihren Highlights als Namen · (2) je Region automatisch alle starken Highlights mit Steckbrief
// · (3) nur auf Ansage: „Hier weitersuchen“ an einem Highlight/Ort (Essen, Wohnen, Nähe, Kinder, Frage).
const TYPEN = ['region', 'ort', 'stadt', 'viertel', 'tauchen', 'tiere', 'natur', 'tempel', 'altstadt', 'museum', 'restaurant', 'unterkunft', 'erlebnis']
const THEMEN = ['tauchen', 'tiere', 'natur', 'kultur', 'essen', 'ort', 'erlebnis']
const FACH: Record<string, string> = {
  tauchen: 'Tiefe/Wasser/Sicht · Begegnung', tiere: 'Was man sieht · Wie nah', natur: 'Strecke/Höhenmeter · Schwierigkeit',
  tempel: 'Eintritt/Regeln · Führung nötig?', altstadt: 'Echtheit · Dauer zu Fuß', museum: 'Schwerpunkt · Dauer',
  viertel: 'Essen · Ruhe', restaurant: 'Küche/Stil · Reservierung', unterkunft: 'Preis/Nacht für 4 in € · Stil',
  ort: 'Charakter · Lage', stadt: 'Charakter · Wie viele Tage', erlebnis: 'Anbieter · Buchung',
}
const LINSEN: Record<string, string> = {
  essen: 'Essen & Trinken: konkrete Lokale, Märkte, Weingüter mit Charakter in der Nähe (Name, Küche, warum)',
  wohnen: 'Wohnen: konkrete, besondere Unterkünfte in der Nähe, die für 4 Personen passen (Name, Stil, ca. Preis pro Nacht für 4 in €)',
  naehe: 'Was gibt es sonst in höchstens ca. 30 Min. Umkreis (Natur, Tiere, Spots, Orte) – nichts, was schon gezeigt wurde',
  kinder: 'Was Kinder im Schulalter hier besonders begeistert',
  tauchen: 'Tauchen und Schnorcheln hier', tiere: 'Tierbegegnungen in freier Natur hier', natur: 'Natur, Wandern, Landschaft hier',
  kultur: 'Kultur, Geschichte, Architektur hier', abend: 'Abende und Ausgehen hier',
}
const PERSONA = `Du bist ein erfahrener, stilsicherer Reiseberater. Ihr beratet eine Familie: 2 Erwachsene, 2 Kinder im Schulalter. Alle tauchen gern – Tauchen ist aber nur EIN Interesse unter vielen.
Mische ehrlich: Natur & Landschaft, Tiere, Meer & Tauchen, Kultur, Essen & Trinken, besondere Orte. Tauchen nur, wo es wirklich herausragt; nicht jeder Vorschlag braucht Wasser.
Geschmack: individuell, beeindruckend, kein Massentourismus, Stil statt Protz; gutes Budget, wenn es sich lohnt. Erfinde nichts.`

function stufe(k: any): 1 | 2 | 3 { return !k.eltern ? 1 : k.eltern.typ === 'region' ? 2 : 3 }

function kontext(k: any): string {
  const v = k.vorlieben ?? {}, vorhanden = (k.vorhanden ?? []).map((x: any) => `${x.titel} [${x.status}]`)
  return `Reisewunsch: „${k.wunsch}“
${v.reisezeit ? `Reisezeit (für die Saison-Einschätzung): ${v.reisezeit}.` : 'Reisezeit unbekannt: Saison allgemein beschreiben, status "passt" nur wenn ganzjährig.'}
${v.andrang_max ? `Vorliebe: Andrang höchstens ${v.andrang_max}/5 – solche nach vorn sortieren. NICHTS ausschließen: ein großes Highlight mit mehr Andrang darf kommen, dann mit gutem „ruhig“-Tipp.` : 'Nichts ausschließen; Reihenfolge = was am besten passt.'}
Schon gezeigt (nicht wiederholen): ${vorhanden.length ? vorhanden.join('; ') : 'nichts'}
„Will ich“ (Geschmackssignal – mehr in diese Richtung): ${(k.gemerkt_sonst ?? []).join('; ') || 'noch nichts'}
„Erstmal nicht“ (eher weniger davon, aber nicht ausschließen): ${(k.weg_sonst ?? []).join('; ') || 'noch nichts'}
Andrang-Skala: 1 kaum touristisch · 2 lokaler Alltag · 3 bekannter Stopp · 4 Busgruppen · 5 Massentourismus.`
}

const BILD_FELDER = `"bild_motiv":"englischer Suchbegriff für das, was man dort SIEHT (Motiv + Ort), z. B. 'Remarkable Rocks Kangaroo Island', 'weedy seadragon Tasmania'; bei Restaurant/Unterkunft/Anbieter: Name + Ort","wiki_titel":"exakter Titel des passenden englischen Wikipedia-Artikels oder null"`

function promptRegionen(k: any): string {
  const p = k.portion
  const auftrag = p.art === 'frage' ? `Beantworte diese Frage mit passenden Regionen: „${p.text}“.`
    : (k.vorhanden ?? []).length ? 'Liefere WEITERE lohnende Regionen, die noch nicht gezeigt wurden (so viele, wie es wirklich gibt, max. 8).'
    : 'Liefere ALLE wirklich lohnenden Regionen dieses Wunsches – typisch 8–15, nicht weniger, nur weil es bequem ist, aber auch keine Füller.'
  return `${PERSONA}
${kontext(k)}
STUFE 1 = REGIONEN. Gliedere den Wunsch in Regionen/Gebiete (Insel, Halbinsel, Küstenabschnitt, Nationalpark-Gebiet, Stadt mit Umland). KEINE einzelnen Spots als Region.
Decke den GANZEN Raum des Wunsches ab – alle Teile (Norden, Süden, Osten, Westen, Inland, Inseln), auch Natur-/Bergregionen ohne Meer – und sortiere erst danach. Regionen überschneiden sich nicht: jedes Highlight gehört genau zu einer Region.
Je Region: Hauptort/Basis, Lage + Anfahrt, warum hin, und ALLE starken Highlights dort als kurze Namen mit Thema (3–8, gemischt).
AUFTRAG: ${auftrag}
Nutze die Websuche für aktuelle Fakten (Saison, Sperrungen). "warnung" NUR bei echter aktueller Sperre/Einschränkung einer ganzen Region (sonst null). Eine *_quelle nur angeben, wenn genau diese Seite die Angabe enthält, sonst null.
Antworte ausschließlich mit JSON:
{"fazit":"1 Satz: wie die Regionen zusammenhängen (z. B. Reihenfolge/Route)","ende":false,"ende_hinweis":null,
"karten":[{"titel":"Name der Region","typ":"region","hauptort":"Hauptort/Basis, z. B. 'Kingscote'","wo":"1 Satz Lage + Anfahrt, z. B. 'Insel vor Adelaide, 45 Min. Fähre ab Cape Jervis (2 h Fahrt von Adelaide)'",
"warum":"1–2 Sätze, warum ihr dorthin solltet – konkret","besonders":"1 Satz: was es so nur hier gibt",
"highlights":[{"name":"konkreter Name (max. 6 Wörter)","thema":"${THEMEN.join('|')}"}],
"tage":"empfohlene Aufenthaltsdauer, z. B. '3–4 Tage'","wow":1-5,"andrang":1-5,"andrang_quelle":"URL oder null",
"saison":{"text":"kurz","status":"passt|grenzwertig|falsch|unbekannt"},
"warnung":null,"warnung_art":"gesperrt|eingeschraenkt|null","warnung_quelle":null,
"lat":Breitengrad des Hauptorts,"lon":Längengrad des Hauptorts,${BILD_FELDER},"quellen":["https://…"]}]}`
}

function karteJson(mitOrt: boolean) {
  return `{"titel":"Eigenname des Ortes/Anbieters, max. 6 Wörter, ohne Werbezusatz (z. B. 'Killiecrankie Bay', nicht 'Einsamkeit pur: Killiecrankie Bay')","typ":"${TYPEN.filter((t) => t !== 'region').join('|')}",${BILD_FELDER},
${mitOrt ? '"ort":"wo genau: nächster Ort + Fahrzeit ab Hauptort, z. B. \'bei Penneshaw · 25 Min. ab Kingscote\'",' : ''}
"moment":"1 Satz: was man dort erlebt, bildhaft",
"besonders":"1 Satz, konkret: was daran einzigartig ist und den WOW-Wert begründet (z. B. 'einziger Ort weltweit, an dem …'); keine Werbesprache",
"wow":1-5,"andrang":1-5,"andrang_quelle":"URL oder null",
"zeit":"z. B. 3 h, halber Tag","kosten_4":"Betrag für 4 Personen in EURO, gerundet, z. B. 'ca. 620 €'; oder 'frei'; bei Unterkunft: 'ca. 380 € / Nacht'","kosten_quelle":"URL oder null",
"mindestalter":null oder Zahl,"familie_hinweis":"nur falls ein Familienmitglied nicht mitkann/eingeschränkt ist, sonst null",
"saison":{"text":"kurz, z. B. Mai–Aug, Höhepunkt Juni","status":"passt|grenzwertig|falsch|unbekannt"},"tageszeit":"beste Tageszeit kurz",
"fach":[{"label":"…","wert":"…"},{"label":"…","wert":"…"}],
"lohnt":"Lohnt sich, wenn … (1 Satz)","eher_nicht":"Eher nicht, wenn … (1 Satz)",
"frage":"die entscheidende offene Frage vor dem Buchen","pruefen":{"text":"was/wo prüfen","url":"URL oder null"},
"ruhig":"1 Tipp, wie man es ruhiger erlebt","warnung":"NUR echte aktuelle Einschränkung mit Datum, sonst null","warnung_art":"gesperrt|eingeschraenkt|null","warnung_quelle":"URL oder null",
"lat":Breitengrad des Spots,"lon":Längengrad des Spots,"quellen":["https://…"]}`
}
const REGELN = `Nutze die Websuche für aktuelle Fakten (Preise, Saison, Regeln, Mindestalter). Suche je Vorschlag nach aktuellen Sperrungen (offizielle Park-, Behörden- oder Anbieterseite). "warnung" NUR bei echter aktueller Einschränkung (gesperrt, pausiert, nicht buchbar, Saison geschlossen) – Entwarnungen und allgemeine Hinweise gehören in "pruefen". Eine *_quelle nur angeben, wenn genau diese Seite die Angabe enthält, sonst null.
Koordinaten: echte Lage des Spots (nicht des Hauptorts), auf ca. 3 Nachkommastellen.
Fachwerte je Typ (genau 2, label + wert): ${Object.entries(FACH).map(([t, f]) => `${t}: ${f}`).join(' | ')}.`

function promptHighlights(k: any): string {
  const e = k.eltern, p = k.portion
  const kandidaten = (Array.isArray(e.highlights) ? e.highlights : []).map((h: any) => typeof h === 'string' ? h : h?.name).filter(Boolean)
  const auftrag = p.art === 'frage' ? `Beantworte diese Frage mit passenden Highlights in der Region: „${p.text}“.`
    : (k.vorhanden ?? []).length ? 'Liefere WEITERE starke Highlights dieser Region, die noch nicht gezeigt wurden (max. 8). Gibt es keine mehr, liefere weniger und setze "ende": true.'
    : `Liefere ALLE wirklich starken Highlights dieser Region – Ziel 8–12, gemischt nach Themen (Natur, Tiere, Meer/Tauchen, Kultur, Essen, besondere Orte). Die Übersicht nannte vorab nur grob: ${kandidaten.join('; ') || '(nichts)'} – das ist KEINE Obergrenze, nur ein Startpunkt: konkretisiere diese (echte Namen statt Sammelbegriffe) und ergänze alles weitere Starke der Region. Weniger als 8 nur, wenn die Region wirklich nicht mehr hergibt.`
  return `${PERSONA}
${kontext(k)}
STUFE 2 = HIGHLIGHTS IN DER REGION „${e.titel}“ (Hauptort: ${e.hauptort ?? 'unbekannt'}; ${e.wo ?? ''}).
Konkrete Orte, Naturerlebnisse, Tierbegegnungen, Tauchplätze, besondere Orte/Städtchen, herausragendes Essen – je mit genauer Lage.
Jedes Highlight ist ein konkreter, benennbarer Ort oder ein konkretes Erlebnis mit Anbieter/Ort – keine Sammelbegriffe wie „über 35 Tauchplätze“ oder „regionale Produkte“ (dann den besten konkreten nennen).
Nur Highlights INNERHALB dieser Region. Diese anderen Regionen werden separat behandelt – deren Highlights NICHT hier nennen: ${(k.geschwister ?? []).join('; ') || '(keine)'}.
AUFTRAG: ${auftrag}
${REGELN}
Antworte ausschließlich mit JSON:
{"fazit":"1 Satz: wie man die Region am besten erlebt (Route/Reihenfolge)","ende":false,"ende_hinweis":null,"karten":[${karteJson(true)}]}`
}

function promptWeiter(k: any): string {
  const e = k.eltern, p = k.portion, pfad = (k.pfad ?? []).map((x: any) => x.titel)
  const linse = p.linse && LINSEN[p.linse] ? LINSEN[p.linse] : null
  const auftrag = p.art === 'frage' ? `Beantworte diese Frage: „${p.text}“ – mit konkreten Vorschlägen (max. 8).`
    : linse ? `${linse}. Max. 8, nur wirklich gute.` : 'Was lohnt sich hier noch in der Nähe? Max. 8, nur wirklich gute.'
  return `${PERSONA}
${kontext(k)}
STUFE 3 = HIER WEITERSUCHEN bei „${e.titel}“ (${e.ort ?? ''}; Pfad: ${pfad.join(' › ')}).
AUFTRAG: ${auftrag}
${REGELN}
Antworte ausschließlich mit JSON:
{"fazit":"1 Satz Überblick","ende":false,"ende_hinweis":null,"karten":[${karteJson(true)}]}`
}

function prompt(k: any): string {
  const s = stufe(k)
  return s === 1 ? promptRegionen(k) : s === 2 ? promptHighlights(k) : promptWeiter(k)
}

async function kiPortion(k: any) {
  const r = await fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST', signal: AbortSignal.timeout(280_000),
    headers: { Authorization: `Bearer ${OR_KEY}`, 'Content-Type': 'application/json', 'X-Title': 'Highlights' },
    body: JSON.stringify({ model: MODELL, messages: [{ role: 'user', content: prompt(k) }], max_tokens: 16000, reasoning: { effort: stufe(k) === 3 ? 'low' : 'medium' },
      plugins: [{ id: 'web', max_results: 10 }], provider: { zdr: true, data_collection: 'deny' }, usage: { include: true } }),
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

function karteBauen(c: any, zitate: Set<string>, stufeNr = 2) {
  const typ = stufeNr === 1 ? 'region' : TYPEN.includes(c?.typ) && c.typ !== 'region' ? c.typ : 'erlebnis'
  const aq = url(c?.andrang_quelle), kq = url(c?.kosten_quelle), pu = url(c?.pruefen?.url)
  const st = ['passt', 'grenzwertig', 'falsch', 'unbekannt'].includes(c?.saison?.status) ? c.saison.status : 'unbekannt'
  const fach = (Array.isArray(c?.fach) ? c.fach : []).slice(0, 2).map((f: any) => ({ label: txt(f?.label, 40), wert: txt(f?.wert, 120) })).filter((f: any) => f.label && f.wert)
  const quellen = [...new Set([...(Array.isArray(c?.quellen) ? c.quellen : []), aq, kq, pu, c?.warnung_quelle].map(url).filter(Boolean))].slice(0, 8)
  return {
    titel: txt(c?.titel, 120), typ, bild_motiv: c?.bild_motiv === null ? null : txt(c?.bild_motiv, 120), wiki_titel: txt(c?.wiki_titel, 120),
    steckbrief: {
      moment: txt(c?.moment, 240), wow: zahl(c?.wow, 1, 5), andrang: zahl(c?.andrang, 1, 5), andrang_quelle: aq, andrang_belegt: belegt(aq, zitate),
      zeit: txt(c?.zeit, 40), kosten_4: txt(c?.kosten_4, 90), kosten_quelle: kq, kosten_belegt: belegt(kq, zitate),
      mindestalter: zahl(c?.mindestalter, 0, 25), familie_hinweis: txt(c?.familie_hinweis, 200),
      saison: { text: txt(c?.saison?.text, 80), status: st }, tageszeit: txt(c?.tageszeit, 80), fach,
      lohnt: txt(c?.lohnt, 200), eher_nicht: txt(c?.eher_nicht, 200), frage: txt(c?.frage, 200),
      pruefen: { text: txt(c?.pruefen?.text, 160), url: pu, belegt: belegt(pu, zitate) }, ruhig: txt(c?.ruhig, 200),
      ...(['gesperrt', 'eingeschraenkt'].includes(c?.warnung_art) && txt(c?.warnung, 240)
        ? { warnung: txt(c?.warnung, 240), warnung_art: c.warnung_art, warnung_quelle: url(c?.warnung_quelle), warnung_belegt: belegt(url(c?.warnung_quelle), zitate) } : {}),
      besonders: txt(c?.besonders, 240), wo: txt(c?.wo, 200), warum: txt(c?.warum, 320), tage: txt(c?.tage, 40),
      // V2: Highlights der Region als {name, thema}; ältere Läufe lieferten reine Texte
      highlights: (Array.isArray(c?.highlights) ? c.highlights : []).map((h: any) => typeof h === 'string' ? { name: txt(h, 90), thema: null }
        : { name: txt(h?.name, 90), thema: THEMEN.includes(h?.thema) ? h.thema : null }).filter((h: any) => h.name).slice(0, 10),
      hauptort: txt(c?.hauptort, 80), ort: txt(c?.ort, 120),
      lat: Number.isFinite(Number(c?.lat)) && Number(c.lat) !== 0 ? Number(c.lat) : null, lon: Number.isFinite(Number(c?.lon)) && Number(c.lon) !== 0 ? Number(c.lon) : null,
      geprueft_am: new Date().toISOString().slice(0, 10), bild_motiv: c?.bild_motiv === null ? null : txt(c?.bild_motiv, 120), wiki_titel: txt(c?.wiki_titel, 120),
    },
    quellen: quellen.map((u) => ({ url: u, abgerufen: belegt(u as string, zitate) })),
  }
}

// ---------- Bilder (0.2.0): echte, aussagekräftige Fotos nur dort, wo ein Foto Sinn ergibt ----------
// Kandidaten: Titelbild des passenden Wikipedia-Artikels (en/de, nur freie Lizenz) + Commons-Suche nach dem Motiv.
// Ein Bildmodell (Gemini 3.8 Flash) sieht die Kandidaten und wählt das Foto, das das Highlight so zeigt, wie man es erlebt – oder keins.
// Auch Restaurant/Unterkunft/Tauchbasis bekommen ein Foto, wenn ein passendes da ist (Ansicht, Lage, Blick); sonst keins.
const BILDMODELL = 'google/gemini-3.8-flash'
const ohneHtml = (s: unknown) => String(s ?? '').replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim().slice(0, 120)
const UNPASSEND = /\b(map|karte|modis|satellite|landsat|sentinel|engraving|lithograph|drawing|illustration|logo|diagram|chart|stamp|coat of arms|sign|signage|plaque|1[6-8]\d\d)\b/i
const warte = (ms: number) => new Promise((ok) => setTimeout(ok, ms))
// Wikimedia drosselt bei vielen parallelen Abrufen (429) – einmal mit Pause wiederholen
async function holeMitWdh(u: string | URL, ms: number) {
  for (let i = 0; i < 3; i++) {
    const r = await fetch(u, { headers: { 'User-Agent': UA }, signal: AbortSignal.timeout(ms) })
    if (r.ok || (r.status !== 429 && r.status < 500)) return r
    await warte(1500 * (i + 1) + Math.random() * 1000)
  }
  return await fetch(u, { headers: { 'User-Agent': UA }, signal: AbortSignal.timeout(ms) })
}
// Fehlerstatus wird weitergegeben (z. B. 429 = Wikimedia drosselt), damit der Grund je Highlight sichtbar ist
const holeJson = async (u: URL) => { const r = await holeMitWdh(u, 12_000); if (!r.ok) throw new Error(`Wikimedia ${u.hostname.split('.')[0]} ${r.status}`); return await r.json() }
function lizenzOk(m: any) { const l = ohneHtml(m?.LicenseShortName?.value); return /^(cc|public domain|pd)/i.test(l) && !/nc|nd/i.test(l) ? l : null }
function kandidatAus(titel: string, ii: any) {
  const m = ii?.extmetadata ?? {}, lizenz = lizenzOk(m)
  if (!lizenz || !ii?.thumburl || !/jpeg|png|webp/.test(ii.mime ?? '') || (ii.width ?? 0) < 800 || (ii.width ?? 0) < (ii.height ?? 0) * 0.9) return null
  if (UNPASSEND.test(titel.replace(/[_-]/g, ' '))) return null
  return { datei: titel, url: ii.thumburl, quelle_url: ii.descriptionurl, urheber: ohneHtml(m.Artist?.value) || 'unbekannt', lizenz, lizenz_url: url(m.LicenseUrl?.value), quelle: 'Wikimedia Commons' }
}
async function commonsInfo(dateien: string[]) {
  if (!dateien.length) return []
  const q = new URL('https://commons.wikimedia.org/w/api.php')
  for (const [k, v] of Object.entries({ action: 'query', format: 'json', titles: dateien.map((d) => d.startsWith('File:') ? d : 'File:' + d).join('|'), prop: 'imageinfo', iiprop: 'url|extmetadata|size|mime', iiurlwidth: '960', origin: '*' })) q.searchParams.set(k, v)
  const j = await holeJson(q)
  return Object.values(j?.query?.pages ?? {}).map((p: any) => kandidatAus(String(p.title ?? ''), p?.imageinfo?.[0])).filter(Boolean)
}
async function wikiTitelbilder(sprache: string, suche: string, direkt: boolean) {
  const q = new URL(`https://${sprache}.wikipedia.org/w/api.php`)
  const basis: Record<string, string> = { action: 'query', format: 'json', prop: 'pageimages', piprop: 'name', pilicense: 'free', redirects: '1', origin: '*' }
  if (direkt) basis.titles = suche; else Object.assign(basis, { generator: 'search', gsrsearch: suche, gsrlimit: '3' })
  for (const [k, v] of Object.entries(basis)) q.searchParams.set(k, v)
  const j = await holeJson(q)
  return Object.values(j?.query?.pages ?? {}).map((p: any) => p?.pageimage).filter(Boolean) as string[]
}
async function commonsSuche(suche: string) {
  const q = new URL('https://commons.wikimedia.org/w/api.php')
  for (const [k, v] of Object.entries({ action: 'query', format: 'json', generator: 'search', gsrnamespace: '6', gsrsearch: `${suche} filetype:bitmap`, gsrlimit: '10',
    prop: 'imageinfo', iiprop: 'url|extmetadata|size|mime', iiurlwidth: '960', origin: '*' })) q.searchParams.set(k, v)
  const j = await holeJson(q)
  return (Object.values(j?.query?.pages ?? {}) as any[]).sort((a, b) => (a.index ?? 0) - (b.index ?? 0)).map((p) => kandidatAus(String(p.title ?? ''), p?.imageinfo?.[0])).filter(Boolean)
}
async function alsDaten(u: string) {
  const klein = u.replace(/\/\d+px-/, '/500px-') // Wikimedia liefert nur Standardgrößen
  const r = await holeMitWdh(klein, 15_000)
  if (!r.ok) throw new Error('Bild ' + r.status)
  const b = new Uint8Array(await r.arrayBuffer())
  let s = ''; for (let i = 0; i < b.length; i += 0x8000) s += String.fromCharCode(...b.subarray(i, i + 0x8000))
  return `data:${r.headers.get('content-type') ?? 'image/jpeg'};base64,${btoa(s)}`
}
async function bildWaehlen(karte: any, kand: any[]) {
  const geladen = (await Promise.allSettled(kand.map((k) => alsDaten(k.url)))).map((x, i) => (x.status === 'fulfilled' ? { k: kand[i], d: x.value } : null)).filter(Boolean) as any[]
  if (!geladen.length) return { bild: null, kosten: 0, info: `0/${kand.length} Kandidaten ladbar` }
  const text = `Reise-Highlight: „${karte.titel}“. ${karte.steckbrief?.moment ?? ''}
Wähle unter den ${geladen.length} Fotos (Nummer 1–${geladen.length}) das eine, das genau dieses Highlight am aussagekräftigsten und schönsten zeigt – so, wie ein Besucher es erlebt (Ort, Landschaft, Tier, Unterwasserszene, Bauwerk). Bei Restaurant, Unterkunft oder Anbieter genügt eine Ansicht des Hauses, der Lage oder des Blicks. Ungeeignet: anderer Ort (nennt der Dateiname einen anderen Ort, z. B. eine andere Höhle oder Insel → ungeeignet), Schilder, Karten, Parkplätze, Personenporträts, unscharf, dunkel, sichtbar alt.
Antworte nur mit einer Zeile JSON: {"wahl": Nummer oder null, "note": 1-10, "grund": "max 8 Wörter Deutsch"}`
  const r = await fetch('https://openrouter.ai/api/v1/chat/completions', { method: 'POST', signal: AbortSignal.timeout(60_000),
    headers: { Authorization: `Bearer ${OR_KEY}`, 'Content-Type': 'application/json', 'X-Title': 'Highlights Bildwahl' },
    body: JSON.stringify({ model: BILDMODELL, temperature: 0, max_tokens: 2000, usage: { include: true }, provider: { data_collection: 'deny' },
      messages: [{ role: 'user', content: [{ type: 'text', text }, ...geladen.flatMap((g, i) => [{ type: 'text', text: `Foto ${i + 1} (Datei: ${String(g.k.datei ?? '').replace(/^File:/, '').slice(0, 120)}):` }, { type: 'image_url', image_url: { url: g.d } }])] }] }) })
  const j = await r.json().catch(() => null)
  const t = String(j?.choices?.[0]?.message?.content ?? '')
  const kosten = Number(j?.usage?.cost ?? 0) || 0
  const wahl = Number(t.match(/"wahl"\s*:\s*(\d+)/)?.[1]), note = Number(t.match(/"note"\s*:\s*(\d+)/)?.[1])
  if (!(wahl >= 1 && wahl <= geladen.length) || !(note >= 6)) return { bild: null, kosten, info: `${geladen.length} Kandidaten, Antwort: ${t.slice(0, 160) || JSON.stringify(j?.error ?? '').slice(0, 160)}` }
  const k = geladen[wahl - 1].k
  return { bild: { ...k, datei: undefined, note, grund: ohneHtml(t.match(/"grund"\s*:\s*"([^"]*)/)?.[1]) }, kosten }
}
async function bildFuer(karte: any, pfad: string[]) {
  if (karte.bild_motiv === null) return { bild: null, kosten: 0 }
  const t = String(karte.titel ?? '').replace(/\(.*?\)/g, '').replace(/[:&]/g, ' ').trim()
  const ort = String(pfad.at(-1) ?? '').replace(/\(.*?\)/g, '').trim()
  const motiv = karte.bild_motiv || karte.bild_suche || `${t} ${ort}`.trim()
  try {
    const titel = new Set<string>()
    const listen = await Promise.all([
      karte.wiki_titel ? wikiTitelbilder('en', karte.wiki_titel, true) : Promise.resolve([]),
      wikiTitelbilder('en', `${t} ${ort}`.trim(), false), wikiTitelbilder('de', t, false)])
    for (const l of listen) for (const d of l) titel.add(d)
    const ausWiki = await commonsInfo([...titel].slice(0, 6))
    const ausSuche = await commonsSuche(motiv)
    const kand: any[] = []
    for (const k of [...ausWiki, ...ausSuche]) if (!kand.some((x) => x.datei === k.datei)) kand.push(k)
    if (!kand.length) return { bild: null, kosten: 0, info: `keine Kandidaten (Wiki ${titel.size}, Suche ${ausSuche.length})` }
    return await bildWaehlen(karte, kand.slice(0, 6))
  } catch (e) { console.error('bild', karte.titel, (e as any)?.message); return { bild: null, kosten: 0, info: String((e as any)?.message ?? e).slice(0, 160) } }
}

const km = (a: number, b: number, c: number, d: number) => {
  const r = Math.PI / 180, x = Math.sin((c - a) * r / 2) ** 2 + Math.cos(a * r) * Math.cos(c * r) * Math.sin((d - b) * r / 2) ** 2
  return 12742 * Math.asin(Math.sqrt(x))
}
// Regionen ohne Highlights und ohne laufende Recherche bekommen eine Stufe-2-Portion; jede läuft in einem eigenen Funktionsaufruf.
async function regionenVertiefen(sucheId: number) {
  const [{ heute }] = await sql`select coalesce(sum(kosten_usd), 0)::float as heute from highlights.portion where erstellt_am > now() - interval '24 hours'`
  if (heute >= 10) { console.error('highlights: Tageslimit, Stufe 2 übersprungen', sucheId); return 0 }
  const neu = await sql`insert into highlights.portion (suche_id, parent_id, art)
    select r.suche_id, r.id, 'start' from highlights.knoten r
    where r.suche_id = ${sucheId} and r.parent_id is null and r.typ = 'region' and r.status <> 'weg'
      and not exists (select 1 from highlights.knoten c where c.parent_id = r.id)
      and not exists (select 1 from highlights.portion p where p.parent_id = r.id and (p.status in ('wartet','laeuft') and p.erstellt_am > now() - interval '8 minutes' or p.status = 'fertig'))
    returning id`
  const [{ token }] = await sql`select token from core.motor_geheimnis where id = 1`
  const ziel = `${Deno.env.get('SUPABASE_URL')}/functions/v1/highlights/fuellen`
  await Promise.allSettled(neu.map((p: any) => fetch(ziel, { method: 'POST', signal: AbortSignal.timeout(15_000),
    headers: { 'Content-Type': 'application/json', 'x-motor-token': token }, body: JSON.stringify({ portion_id: Number(p.id), async: true }) })))
  return neu.length
}

// Fehlende Fotos einer Suche nachholen: höchstens 24 je Lauf, 2 parallel, je Highlight max. 3 Versuche; Grund wird gespeichert.
async function bilderNachholen(sucheId: number, neu = false) {
  const ks = await sql`select id, titel, typ, steckbrief, highlights.pfad(parent_id) as pfad from highlights.knoten
    where suche_id = ${sucheId} and (bild is null or ${neu}) and coalesce((steckbrief->>'bild_versuche')::int, 0) < 3
      and (steckbrief->>'bild_versuch_am' is null or (steckbrief->>'bild_versuch_am')::timestamptz < now() - interval '5 minutes')
    order by coalesce((steckbrief->>'bild_versuche')::int, 0), id limit 24`
  let ni = 0
  await Promise.all([0, 1].map(async () => { while (ni < ks.length) { const k: any = ks[ni++]
    const sb = k.steckbrief ?? {}
    const r = await bildFuer({ titel: k.titel, typ: k.typ, steckbrief: sb, bild_motiv: sb.bild_motiv, bild_suche: sb.bild_suche, wiki_titel: sb.wiki_titel }, (k.pfad ?? []).map((x: any) => x.titel))
    const info = { bild_versuche: (Number(sb.bild_versuche) || 0) + 1, bild_versuch_am: new Date().toISOString(), bild_info: r.bild ? null : String((r as any).info ?? 'kein Foto vorgesehen').slice(0, 200) }
    if (r.bild) await sql`update highlights.knoten set bild = ${JSON.stringify(r.bild)}::text::jsonb, steckbrief = steckbrief || ${JSON.stringify(info)}::text::jsonb where id = ${k.id}`
    else await sql`update highlights.knoten set steckbrief = steckbrief || ${JSON.stringify(info)}::text::jsonb where id = ${k.id}`
    if (r.kosten) await sql`update highlights.portion set kosten_usd = coalesce(kosten_usd, 0) + ${r.kosten} where id = (select portion_id from highlights.knoten where id = ${k.id})`
  } }))
  return ks.length
}
// Nach der letzten Recherche einer Suche: fehlende Fotos in Ruhe nachholen (dann ohne parallele Wikimedia-Last)
async function nachholenWennFertig(sucheId: number) {
  const [{ laufen }] = await sql`select count(*)::int as laufen from highlights.portion where suche_id = ${sucheId} and status in ('wartet','laeuft') and erstellt_am > now() - interval '8 minutes'`
  if (laufen === 0) await bilderNachholen(sucheId)
}

async function portionFuellen(id: number) {
  const [{ k }] = await sql`select highlights.portion_kontext(${id}) as k`
  await sql`update highlights.portion set status = 'laeuft' where id = ${id}`
  let kosten = 0, modell = MODELL
  try {
    if (!OR_KEY) throw new Error('OPENROUTER_API_KEY fehlt')
    const ki = await kiPortion(k); kosten = ki.kosten; modell = ki.modell
    const st = stufe(k)
    const karten = (Array.isArray(ki.daten?.karten) ? ki.daten.karten : []).slice(0, st === 1 ? 15 : st === 2 ? 12 : 8).map((c: any) => karteBauen(c, ki.zitate, st)).filter((c: any) => c.titel)
    // Koordinaten-Plausibilität: Spot mehr als 300 km vom Elternort entfernt -> Koordinaten verwerfen (Karte nutzt dann den Elternort)
    const elat = Number(k.eltern?.lat), elon = Number(k.eltern?.lon)
    if (st > 1 && Number.isFinite(elat) && Number.isFinite(elon)) for (const c of karten) {
      const sb = c.steckbrief
      if (sb.lat !== null && sb.lon !== null && km(sb.lat, sb.lon, elat, elon) > 300) { sb.lat = null; sb.lon = null; sb.ort_unsicher = true }
    }
    const pfad = (k.pfad ?? []).map((x: any) => x.titel)
    const bilder: any[] = new Array(karten.length)
    let naechstes = 0
    await Promise.all([0, 1, 2].map(async () => { while (naechstes < karten.length) { const i = naechstes++; bilder[i] = await bildFuer(karten[i], pfad) } }))
    karten.forEach((c: any, i: number) => { c.bild = bilder[i].bild; kosten += bilder[i].kosten
      if (!c.bild) Object.assign(c.steckbrief, { bild_versuche: 1, bild_versuch_am: new Date().toISOString(), bild_info: String(bilder[i].info ?? 'kein Foto vorgesehen').slice(0, 200) }) })
    await sql`select highlights.portion_abschliessen(${id}, ${JSON.stringify({ karten, fazit: txt(ki.daten?.fazit, 400), ende: !!ki.daten?.ende,
      ende_hinweis: txt(ki.daten?.ende_hinweis, 400), kosten_usd: kosten, modell })}::text::jsonb)`
    // Stufe 1 fertig -> Stufe 2 für jede neue Region automatisch (eigene Aufrufe, parallel)
    if (st === 1) await regionenVertiefen(Number(k.portion.suche_id))
    else await nachholenWennFertig(Number(k.portion.suche_id))
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
      // fehlende Bilder nachholen – im Hintergrund, Grund je Highlight gespeichert (steckbrief.bild_info)
      // @ts-ignore EdgeRuntime gibt es in Supabase Edge Functions
      EdgeRuntime.waitUntil(bilderNachholen(Number(b.bilder_suche_id), !!b.neu))
      return antwort({ ok: true, async: true })
    }
    if (b.regionen_suche_id) return antwort({ ok: true, gestartet: await regionenVertiefen(Number(b.regionen_suche_id)) })
    if (b.async) {
      // @ts-ignore EdgeRuntime gibt es in Supabase Edge Functions
      EdgeRuntime.waitUntil(portionFuellen(Number(b.portion_id)))
      return antwort({ ok: true, portion_id: Number(b.portion_id), async: true })
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
