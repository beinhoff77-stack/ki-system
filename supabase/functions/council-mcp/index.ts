// Council-Zugang: eigener MCP-Server, der ausschließlich die api-Funktionen anbietet.
// Authentifizierung: geheimer Schlüssel im Pfad (/council-mcp/<schluessel>), in der DB nur als SHA-256-Hash.
// Jeder DB-Aufruf läuft als eingeschränkte Rolle council_mcp (nur EXECUTE auf api.*). Rechte prüft die Datenbank.
// Version 0.8.0 (Bauschritt 12): Universal-Tür (council_hilfe + council_aktion) und Recht 'daten'.
// Version 0.9.0 (Bauschritt 13): bewertung_lesen, nutzer_urteil, bewertung_anstossen (nur über die Tür).
// Version 0.10.0 (Bauschritt 14): Werkstatt – Absprache der KIs über Programmierwünsche (nur über die Tür).
// Version 0.11.0 (Bauschritt 18): verlauf_lesen – Darstellung in drei Ebenen als fertiges Markdown (nur über die Tür).
// Version 0.12.0 (Bauschritt 23, Werkstatt #15): Fach-Tool unterkunft – Kandidaten einreichen/lesen/bewerten, Nutzer-Urteil (nur über die Tür).
// Version 0.12.1 (Bauschritt 23b): angebot, Preisnachweis, preis_alternativen, Bewertungsarten pruefung/eignung.
// Version 0.13.0 (Suchtool Bauschritt 1, Werkstatt #36): Zimmerkategorien, Lückenfüller-Aufträge, Treffer-Status, Suchlauf lesen (nur über die Tür).
// Version 0.14.0 (Suchtool Bauschritt 2, Werkstatt #39): Suchauftrag anlegen, Suche starten (Sammler suche-sammeln), nur über die Tür.
// Version 0.15.0 (Suchtool Bauschritt 5, Werkstatt #46): Suche Status (leicht) und Suche abbrechen, nur über die Tür.
// Version 0.16.0 (Suchtool Bauschritt 7, Werkstatt #47): Rückmeldung geben und Rückmelde-Report, nur über die Tür.
// Version 0.17.0 (Suchtool Ausbau 3a, Werkstatt #52): Suchauftrag mit Nebenart/Unterkunftsform/Kriterien/Qualitätsfilter/Suchprofil; Suchprofile speichern/lesen.
// Version 0.18.0 (Ortswissen, Werkstatt #60): Viertel lesen/ermitteln, Zonen lesen/entscheiden; Kriterium mit werte (Viertel-Auswahl), nur über die Tür.
// Version 0.18.1 (Werkstatt #83): werkstatt_nachricht kennt art entscheidung und fertig (Handy-Meldung an Sebastian).
// Version 0.19.0 (Werkstatt #155): Highlights – Recherche-Aufträge aus der App im Chat erledigen (highlights_chat_offen/abholen/abschliessen), nur über die Tür.
// REGEL FÜR KÜNFTIGE ERWEITERUNGEN: neue Aktionen mit nurTuer = true anlegen, damit sich die Werkzeugliste
// in den Apps nicht ändert und niemand neu verbinden muss.
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
import { McpServer } from 'npm:@modelcontextprotocol/sdk@1.25.3/server/mcp.js'
import { WebStandardStreamableHTTPServerTransport } from 'npm:@modelcontextprotocol/sdk@1.25.3/server/webStandardStreamableHttp.js'
import { Hono } from 'npm:hono@^4.9.7'
import { z } from 'npm:zod@^4.1.13'
import postgres from 'npm:postgres@3.4.5'

const sql = postgres(Deno.env.get('SUPABASE_DB_URL')!, { prepare: false, max: 3, idle_timeout: 20 })

const SIGNATUREN: Record<string, string[]> = {
  wer_bin_ich: ['text'],
  systemregeln: ['text'],
  meine_aufgaben: ['text'],
  rahmen_lesen: ['text', 'bigint'],
  beitrag_einreichen: ['text', 'bigint', 'int', 'text', 'text', 'text', 'text', 'numeric'],
  beitraege_lesen: ['text', 'bigint', 'int'],
  ergebnis_lesen: ['text', 'bigint'],
  erkenntnisse_suchen: ['text', 'text', 'text', 'boolean'],
  stammdaten_lesen: ['text', 'text', 'text'],
  stammdaten_vorschlagen: ['text', 'jsonb'],
  rahmen_anlegen: ['text', 'jsonb'],
  rahmen_status_setzen: ['text', 'bigint', 'text'],
  runde_starten: ['text', 'bigint', 'text', 'text', 'timestamptz'],
  ausfall_entscheiden: ['text', 'bigint', 'int', 'text', 'timestamptz', 'text'],
  fristen_pruefen: ['text'],
  angaben_setzen: ['text', 'bigint', 'jsonb'],
  ergebnis_speichern: ['text', 'bigint', 'jsonb'],
  nutzer_entscheidung: ['text', 'bigint', 'text'],
  erkenntnis_speichern: ['text', 'jsonb'],
  erkenntnis_ueberholt: ['text', 'bigint', 'bigint'],
  aufraeumen: ['text'],
  stammdaten_setzen: ['text', 'jsonb'],
  stammdaten_art_anlegen: ['text', 'jsonb'],
  stammdaten_vorschlaege_lesen: ['text'],
  stammdaten_vorschlag_entscheiden: ['text', 'bigint', 'text', 'jsonb'],
  bewertung_abgeben: ['text', 'bigint', 'text', 'text', 'jsonb', 'text'],
  leistung_lesen: ['text', 'text', 'text'],
  rollen_lesen: ['text', 'text', 'text'],
  rolle_vorschlagen: ['text', 'jsonb'],
  rolle_entscheiden: ['text', 'bigint', 'text', 'jsonb'],
  rolle_archivieren: ['text', 'text', 'text'],
  rollen_erkenntnis_speichern: ['text', 'jsonb'],
  besetzung_grundlage: ['text', 'bigint'],
  besetzung_speichern: ['text', 'bigint', 'jsonb', 'text', 'text'],
  besetzung_entscheiden: ['text', 'bigint', 'text', 'jsonb'],
  einstellungen_lesen: ['text'],
  einstellung_setzen: ['text', 'text', 'jsonb'],
  posteingang: ['text', 'boolean'],
  uebergabe_laden: ['text', 'text'],
  auftraege_suchen: ['text', 'text', 'text', 'text'],
  modelle_lesen: ['text', 'text', 'boolean'],
  mein_modell_setzen: ['text', 'jsonb'],
  stammdaten_freigeben: ['text', 'bigint', 'bigint[]'],
  auftrag_starten: ['text', 'bigint', 'int'],
  auftrag_weiter: ['text', 'bigint', 'numeric'],
  bewertung_lesen: ['text', 'bigint'],
  nutzer_urteil: ['text', 'bigint', 'text', 'text'],
  bewertung_anstossen: ['text', 'bigint'],
  werkstatt_lesen: ['text', 'boolean'],
  werkstatt_wunsch_lesen: ['text', 'bigint'],
  werkstatt_wunsch_anlegen: ['text', 'jsonb'],
  werkstatt_wunsch_status: ['text', 'bigint', 'text', 'boolean', 'text', 'text'],
  werkstatt_nachricht: ['text', 'bigint', 'text', 'text', 'text'],
  werkstatt_sperre: ['text', 'text', 'bigint', 'numeric', 'boolean'],
  werkstatt_aenderung: ['text', 'jsonb'],
  verlauf_lesen: ['text', 'bigint', 'text', 'text', 'int'],
  unterkunft_kandidat_einreichen: ['text', 'jsonb'],
  unterkunft_kandidaten_lesen: ['text', 'bigint', 'text', 'boolean'],
  unterkunft_kandidat_bewerten: ['text', 'bigint', 'text', 'int', 'text'],
  unterkunft_urteil: ['text', 'bigint', 'text', 'text'],
  unterkunft_zimmerkategorien_setzen: ['text', 'jsonb'],
  unterkunft_lueckenfueller_anlegen: ['text', 'jsonb'],
  unterkunft_lueckenfueller_abholen: ['text', 'bigint'],
  highlights_chat_offen: ['text'],
  highlights_chat_abholen: ['text', 'bigint'],
  highlights_chat_abschliessen: ['text', 'bigint', 'jsonb'],
  unterkunft_lueckenfueller_abschliessen: ['text', 'bigint', 'text', 'jsonb'],
  unterkunft_lueckenfueller_lesen: ['text', 'text'],
  unterkunft_treffer_status_setzen: ['text', 'bigint', 'text'],
  unterkunft_suchlauf_lesen: ['text', 'bigint'],
  unterkunft_suchauftrag_anlegen: ['text', 'jsonb'],
  unterkunft_suche_starten: ['text', 'bigint'],
  unterkunft_suche_status: ['text', 'bigint'],
  unterkunft_suche_abbrechen: ['text', 'bigint'],
  unterkunft_rueckmeldung_geben: ['text', 'bigint', 'text', 'text'],
  unterkunft_rueckmeldung_report: ['text'],
  unterkunft_suchprofil_speichern: ['text', 'jsonb'],
  unterkunft_suchprofile_lesen: ['text'],
  unterkunft_zonen_lesen: ['text', 'text'],
  unterkunft_zone_entscheiden: ['text', 'bigint', 'text', 'text', 'text'],
  unterkunft_viertel_lesen: ['text', 'text', 'bigint'],
  unterkunft_viertel_erstellen: ['text', 'text', 'boolean'],
}

async function sha256Hex(s: string): Promise<string> {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s))
  return Array.from(new Uint8Array(buf)).map((b) => b.toString(16).padStart(2, '0')).join('')
}

async function api(fn: string, args: unknown[]): Promise<unknown> {
  const typen = SIGNATUREN[fn]
  if (!typen || typen.length !== args.length) throw new Error('unbekannte Funktion')
  const platzhalter = typen.map((t, i) => (t === 'jsonb' ? `$${i + 1}::text::jsonb` : `$${i + 1}::${t}`)).join(', ')
  return await sql.begin(async (tx) => {
    await tx`set local role council_mcp`
    const zeilen = await tx.unsafe(`select api.${fn}(${platzhalter}) as r`, args.map((a) => (a === undefined ? null : a)) as any[])
    return zeilen[0].r
  })
}

function fehlertext(e: any): string {
  if (e?.code === 'P0001') return String(e.message)
  console.error('council-mcp interner Fehler', e?.code, e?.message)
  return 'Interner Fehler – bitte später erneut versuchen.'
}
function antwort(r: unknown) {
  return { content: [{ type: 'text' as const, text: JSON.stringify(r, null, 1) }] }
}
function fehler(e: unknown) {
  return { content: [{ type: 'text' as const, text: 'Fehler: ' + fehlertext(e) }], isError: true }
}
function fehlerText(t: string) {
  return { content: [{ type: 'text' as const, text: 'Fehler: ' + t }], isError: true }
}

const NUR_LESEN = { readOnlyHint: true, destructiveHint: false, idempotentHint: true, openWorldHint: false }
const SCHREIBT = { readOnlyHint: false, destructiveHint: false, openWorldHint: false }
const LOESCHT = { readOnlyHint: false, destructiveHint: true, openWorldHint: false }

const ANLEITUNG = `Council-Zugang des persönlichen KI-Systems.
UNIVERSAL-TÜR: council_hilfe zeigt ALLE Aktionen, die du ausführen darfst, mit Parametern. council_aktion führt jede davon aus (aktion + daten). Findest du für etwas kein eigenes Werkzeug, schau zuerst in council_hilfe – neue Funktionen kommen nur dort hinzu.
SAGT DER NUTZER NUR "Council" (oder fragt nach neuen Ergebnissen): rufe posteingang auf und zeige ihm die Kurznamen. Nennt er einen, lade ihn mit uebergabe_laden und arbeite direkt damit weiter. Entscheidet er etwas, schreibe es mit nutzer_entscheidung zurück (wenn du das Recht daten oder leiten hast).
ERGEBNIS ANZEIGEN: council_aktion verlauf_lesen {rahmen_id, ebene} liefert fertiges Markdown – unverändert anzeigen, nicht zusammenfassen. ebene uebersicht (Standard: Tabelle Plan/Rolle/Modell/Linie/Note + Empfehlung + Streitpunkte), "zeig Plan X" -> verlauf + plan, "Belege zu Plan X" -> belege + plan, "Plan X Runde N ganz" -> volltext + plan + runde_nr.
SAGT DER NUTZER "Werkstatt" (oder geht es um Programmierwünsche am System): council_aktion werkstatt_lesen aufrufen, neue Nachrichten und offene Wünsche zeigen, Regeln W1-W7 befolgen. Vor jeder Änderung an Datenbank, Serverfunktionen oder App: werkstatt_sperre holen.
UNTERKUNFTSSUCHE: Bei Aufträgen mit Unterkunfts-Kandidaten gehen Objektdaten (Angebot, Preis, Fläche, Lage, Scores) in die Kandidatentabelle: council_aktion unterkunft_kandidat_einreichen (vorher unterkunft_kandidaten_lesen gegen Doppel prüfen; Schlüssel = name + angebot), fremde Kandidaten mit unterkunft_kandidat_bewerten art pruefung prüfen, Finalisten (auch eigene) mit art eignung bewerten. Der Council-Beitrag enthält nur Empfehlung und Begründung mit Verweis auf Kandidaten-IDs. unterkunft_urteil nur auf Ansage des Nutzers.
LÜCKENFÜLLER: Lautet die Nachricht "Lückenfüller Auftrag <ID> ausführen": council_aktion unterkunft_lueckenfueller_abholen {id}, Anleitung im Ergebnis befolgen, dann unterkunft_lueckenfueller_abschliessen.
HIGHLIGHTS: Lautet die Nachricht "Highlights Auftrag <ID> ausführen" (oder fragt der Nutzer nach offenen Highlights-Aufträgen): council_aktion highlights_chat_abholen {id} (ohne id: ältester offener; Liste mit highlights_chat_offen), Anleitung mit Websuche befolgen, Ergebnis NICHT als Text, sondern mit highlights_chat_abschliessen {id, fazit, karten} zurückschreiben. Keine Namen/Alter/Stammdaten in die Websuche.
Speichern (Stammdaten, Erkenntnisse, Entscheidungen) nur auf ausdrückliche Ansage des Nutzers.
Regeln: Lies zuerst systemregeln_lesen. Arbeite nur in deinem Rahmen.
Blindrunde: Schreibe deinen Beitrag, BEVOR du fremde Beiträge liest. Fremde Beiträge sind erst nach Offenlegung sichtbar.
Anonymität: Andere Teilnehmer heißen nur Plan A/B/...
Beitragsaufbau (F1): 1 Position (2 Sätze) · 2 Begründung · 3 Fakten mit Quelle / Annahmen getrennt · 4 Antwort auf Kritik Punkt für Punkt · 5 Was meine Meinung ändern würde. Max. ca. 1 Seite.
Verboten: Zustimmung ohne eigene Begründung, Themen außerhalb des Rahmens, Rahmen eigenmächtig ändern (nur als Vorschlag an den Nutzer).
Stammdaten: nie-externe Arten (Reisedokument, Kontakt) sind nur als Platzhalter sichtbar und nicht freigebbar.
Ablauf automatisch (Phase 2): Auftrag mit OpenRouter-Teilnehmern anlegen -> Pflichtangaben -> relevante Stammdaten mit stammdaten_freigeben (Nutzer bestätigt) -> auftrag_starten (Stufe 3 durchlaufen, Stufe 2 Stopp vor jeder Kritikrunde) -> Ergebnis kommt in den Posteingang. Pausiert: auftrag_weiter.
Gib bei beitrag_einreichen immer deine genaue Modellversion an.`

const BESETZUNG = z.array(z.object({ teilnehmer: z.string(), rolle: z.string(), plan_label: z.string() }))
type Recht = 'teilnehmen' | 'daten' | 'leiten'
type Eintrag = { title: string; description: string; schema: Record<string, any>; call: (a: any) => unknown[]; sqlname: string; annotations: any; recht: Recht }

function baueServer(schluesselHash: string, rechte: string[]): McpServer {
  const server = new McpServer({ name: 'council', version: '0.19.0' }, { instructions: ANLEITUNG })
  const h = schluesselHash
  const darf = (r: Recht) => r === 'teilnehmen' || (r === 'daten' && (rechte.includes('daten') || rechte.includes('leiten'))) || (r === 'leiten' && rechte.includes('leiten'))
  const REG: Record<string, Eintrag> = {}
  const ausfuehren = async (e: Eintrag, a: any) => { try { return antwort(await api(e.sqlname, e.call(a ?? {}))) } catch (err) { return fehler(err) } }

  function def(name: string, recht: Recht, title: string, description: string, schema: Record<string, any>, call: (a: any) => unknown[],
               annotations: any = SCHREIBT, nurTuer = false, sqlname?: string) {
    if (!darf(recht)) return
    const e: Eintrag = { title, description, schema, call, sqlname: sqlname ?? name, annotations, recht }
    REG[name] = e
    if (!nurTuer) server.registerTool(name, { title, description, inputSchema: schema, annotations }, async (a: any) => ausfuehren(e, a))
  }
  const lese = (name: string, recht: Recht, title: string, description: string, schema: Record<string, any>, call: (a: any) => unknown[], nurTuer = false, sqlname?: string) =>
    def(name, recht, title, description, schema, call, NUR_LESEN, nurTuer, sqlname)

  // ---------- Lesen (alle) ----------
  lese('posteingang', 'teilnehmen', 'Council-Posteingang', 'Nur lesen. Neue Council-Ergebnisse mit Kurznamen. Aufrufen, wenn der Nutzer "Council" sagt oder nach neuen Ergebnissen fragt.',
    { alle_offenen: z.boolean().optional().describe('true zeigt auch schon abgeholte, noch nicht erledigte') }, (a) => [h, a.alle_offenen ?? false])
  lese('auftraege_suchen', 'teilnehmen', 'Aufträge suchen', 'Nur lesen. Sucht Council-Aufträge nach Stichwort, Bereich oder Status; neueste zuerst, mit Kurzname und Ergebnis-Status.',
    { suche: z.string().optional(), bereich: z.string().optional(), status: z.string().optional() }, (a) => [h, a.suche ?? null, a.bereich ?? null, a.status ?? null])
  lese('modelle_lesen', 'teilnehmen', 'Modelle lesen', 'Nur lesen. "Meine Modelle" aus OpenRouter mit Preis (USD pro 1 Mio. Tokens), Kontext, ZDR, Stammdaten-Freigabe, Warnungen. Mit suche und nur_meine=false auch Katalogtreffer.',
    { suche: z.string().optional(), nur_meine: z.boolean().optional().describe('Standard true') }, (a) => [h, a.suche ?? null, a.nur_meine ?? true])
  lese('systemregeln_lesen', 'teilnehmen', 'Systemregeln lesen', 'Nur lesen. Hausregeln, beschlossene Entscheidungen und Rollendatenbank des Systems.', {}, () => [h], false, 'systemregeln')
  lese('meine_aufgaben', 'teilnehmen', 'Meine offenen Aufgaben', 'Nur lesen. Runden, in denen von dir noch ein Beitrag erwartet wird.', {}, () => [h])
  lese('rahmen_lesen', 'teilnehmen', 'Rahmen eines Auftrags lesen', 'Nur lesen. Originalfrage, Ziel, Vorgaben, Grenzen, Rollen, Runden, Pflichtangaben, passende Erkenntnisse aus dem Archiv, Status, Kosten und Pausengrund eines Council-Auftrags.',
    { rahmen_id: z.number().int() }, (a) => [h, a.rahmen_id])
  lese('beitraege_lesen', 'teilnehmen', 'Beiträge lesen', 'Nur lesen. Offengelegte Beiträge (anonym als Plan A/B) plus eigene noch verdeckte Beiträge und Stand der verdeckten Runden.',
    { rahmen_id: z.number().int(), runde_nr: z.number().int().optional() }, (a) => [h, a.rahmen_id, a.runde_nr ?? null])
  lese('ergebnis_lesen', 'teilnehmen', 'Ergebnis vollständig lesen', 'Nur lesen. Vollständiges Ergebnis (Empfehlung, Streitpunkte, Fakten mit Quellen, Annahmen, offene Fragen, Entscheidungsvorschläge). Für den Normalfall reicht uebergabe_laden.',
    { rahmen_id: z.number().int() }, (a) => [h, a.rahmen_id])
  lese('erkenntnisse_suchen', 'teilnehmen', 'Wissensarchiv durchsuchen', 'Nur lesen. Sucht Erkenntnisse im Wissensarchiv nach Suchwort und/oder Bereich. Jede Erkenntnis hat Quelle, Quellenstand, Gegenargument, Unsicherheit und Prüfstand.', {
    suche: z.string().optional(), bereich: z.string().optional(), nur_gueltig: z.boolean().optional().describe('Standard true'),
  }, (a) => [h, a.suche ?? null, a.bereich ?? null, a.nur_gueltig ?? true])
  lese('stammdaten_lesen', 'teilnehmen', 'Stammdaten lesen', 'Nur lesen. Bekannte Stammdaten (Personen, Vorlieben, Haushalt) mit id. Nie-externe Arten erscheinen nur als Platzhalter mit Ablaufdatum.',
    { art: z.string().optional(), person: z.string().optional() }, (a) => [h, a.art ?? null, a.person ?? null])
  lese('leistung_lesen', 'teilnehmen', 'Leistung lesen', 'Nur lesen. Bewertungen je Modell x Rolle x Bereich x Kriterium und Gesamtnote je Modell.',
    { bereich: z.string().optional(), rolle: z.string().optional() }, (a) => [h, a.bereich ?? null, a.rolle ?? null])
  lese('rollen_lesen', 'teilnehmen', 'Rollen lesen', 'Nur lesen. Rollen mit Status (aktiv/vorschlag/archiviert), Version, Basisrolle, Zahl der Erkenntnisse und bewerteten Aufträge.', {
    status: z.enum(['aktiv', 'vorschlag', 'archiviert', 'alle']).optional(), suche: z.string().optional(),
  }, (a) => [h, a.status ?? 'aktiv', a.suche ?? null])
  lese('besetzung_grundlage', 'teilnehmen', 'Grundlage für Besetzungsvorschlag', 'Nur lesen. Passende Rollen, offene Rollen-Erkenntnisse, Leistung je Modell x Rolle x Bereich, verfügbare Teilnehmer und Datenlage.',
    { rahmen_id: z.number().int() }, (a) => [h, a.rahmen_id])
  lese('einstellungen_lesen', 'teilnehmen', 'Einstellungen lesen', 'Nur lesen. Systemeinstellungen (Start-KI, Ergebnis-Modell, ZDR-Pflicht, Token-Grenze, Schwelle für belastbare Bewertungen).', {}, () => [h])
  lese('stammdaten_vorschlaege_lesen', 'daten', 'Offene Stammdaten-Vorschläge', 'Nur lesen. Vorschläge, über die der Nutzer noch entscheiden muss.', {}, () => [h])
  lese('bewertung_lesen', 'teilnehmen', 'Bewertung eines Auftrags lesen', 'Nur lesen. Je Teilnehmer: Modell, Rolle, Noten der neutralen Bewerter-KI (bewertet_von system), der Stamm-KI und des Nutzers mit Begründung, Befunde (abgeschnitten, Regelverstöße), Kosten; dazu Bewertungsstatus und Gesamturteil des Nutzers.',
    { rahmen_id: z.number().int() }, (a) => [h, a.rahmen_id], true)

  // ---------- Schreiben als Teilnehmer ----------
  def('uebergabe_laden', 'teilnehmen', 'Übergabe-Paket laden', 'Lädt das kompakte Übergabe-Paket eines Ergebnisses (Kurzname, Teil davon oder Auftragsnummer) zum Weiterarbeiten und markiert es als abgeholt.',
    { name: z.string().min(1).describe('Kurzname, Stichwort oder Auftragsnummer') }, (a) => [h, a.name])
  def('beitrag_einreichen', 'teilnehmen', 'Beitrag einreichen', 'Reicht deinen Beitrag für eine Runde ein (Aufbau F1). Nur einmal pro Runde. Vorher KEINE fremden Beiträge dieser Runde lesen.', {
    rahmen_id: z.number().int(), runde_nr: z.number().int(), modellversion: z.string().min(1),
    position: z.string().describe('Position in max. 2 Sätzen'), inhalt: z.string().min(1).describe('Vollständiger Beitrag nach Aufbau F1'),
    plan_label: z.string().optional().describe('Nur nötig, wenn du mehrere Rollen im Auftrag hast'), kosten_usd: z.number().optional(),
  }, (a) => [h, a.rahmen_id, a.runde_nr, a.modellversion, a.position, a.inhalt, a.plan_label ?? null, a.kosten_usd ?? 0])
  def('stammdaten_vorschlagen', 'teilnehmen', 'Stammdatum vorschlagen', 'Schlägt eine dauerhaft nützliche Angabe als Stammdatum vor. Wird dem Nutzer zur Entscheidung vorgelegt.', {
    art: z.string().min(1), bezeichnung: z.string().min(1), daten: z.record(z.string(), z.unknown()).optional(),
    begruendung: z.string().optional(), quelle: z.string().optional(), rahmen_id: z.number().int().optional(),
  }, (a) => [h, JSON.stringify(a)])
  def('rolle_vorschlagen', 'teilnehmen', 'Rolle vorschlagen', 'Schlägt eine neue Rolle oder eine Variante (abgeleitet_von) vor. Wird erst aktiv, wenn der Nutzer zustimmt. Neuer, eindeutiger Name nötig.', {
    name: z.string().min(1), typ: z.enum(['grund', 'zusatz', 'fach']).optional(), stellenbeschreibung: z.string().min(1),
    arbeitsmuster: z.array(z.string()).optional(), pflichtfragen: z.array(z.string()).optional(), schlagworte: z.array(z.string()).optional(),
    abgeleitet_von: z.string().optional(), begruendung: z.string().min(1),
  }, (a) => [h, JSON.stringify(a)])

  // ---------- Daten schreiben (Recht daten oder leiten) ----------
  def('stammdaten_setzen', 'daten', 'Stammdatum speichern', 'Nur auf Ansage des Nutzers. Legt ein Stammdatum an oder ersetzt es; die alte Fassung bleibt erhalten.', {
    art: z.string().min(1), bezeichnung: z.string().min(1), daten: z.record(z.string(), z.unknown()), person: z.string().optional(),
    nie_extern: z.boolean().optional(), gueltig_von: z.string().optional(), gueltig_bis: z.string().optional(), quelle: z.string().optional(),
  }, (a) => [h, JSON.stringify(a)])
  def('stammdaten_art_anlegen', 'daten', 'Neue Stammdaten-Art anlegen', 'Nur nach ausdrücklichem Nutzer-Okay.', {
    name: z.string().min(1), beschreibung: z.string().optional(),
    felder: z.array(z.object({ name: z.string(), typ: z.string(), pflicht: z.boolean().optional() })).optional(),
    nie_extern: z.boolean().optional(), personenbezogen: z.boolean().optional(),
  }, (a) => [h, JSON.stringify(a)])
  def('stammdaten_vorschlag_entscheiden', 'daten', 'Stammdaten-Vorschlag entscheiden', 'Nur auf Entscheidung des Nutzers: annehmen (optional mit Korrektur) oder ablehnen.', {
    id: z.number().int(), entscheidung: z.enum(['annehmen', 'ablehnen']),
    korrektur: z.object({ art: z.string().optional(), bezeichnung: z.string().optional(), daten: z.record(z.string(), z.unknown()).optional(), person: z.string().optional(), quelle: z.string().optional() }).optional(),
  }, (a) => [h, a.id, a.entscheidung, a.korrektur ? JSON.stringify(a.korrektur) : null])
  def('nutzer_entscheidung', 'daten', 'Nutzerentscheidung festhalten', 'Nur auf Ansage des Nutzers: hält seine Entscheidung zum Ergebnis fest und setzt es im Posteingang auf erledigt.',
    { rahmen_id: z.number().int(), entscheidung: z.string().min(1) }, (a) => [h, a.rahmen_id, a.entscheidung])
  def('erkenntnis_speichern', 'daten', 'Erkenntnis ins Wissensarchiv', 'Speichert eine Erkenntnis. Nur nach Bestätigung des Nutzers.', {
    bereich: z.string().min(1), titel: z.string().min(1), erkenntnis: z.string().min(1), schlagworte: z.array(z.string()).optional(),
    quelle: z.string().optional(), quellenstand: z.string().optional(), gegenargument: z.string().optional(),
    unsicherheit: z.enum(['niedrig', 'mittel', 'hoch']).optional(), vom_nutzer_bestaetigt: z.boolean().optional(), rahmen_id: z.number().int().optional(),
  }, (a) => [h, JSON.stringify(a)])
  def('erkenntnis_ueberholt', 'daten', 'Erkenntnis als überholt markieren', 'Markiert eine Erkenntnis als überholt (nie löschen).',
    { id: z.number().int(), ersetzt_durch: z.number().int().optional() }, (a) => [h, a.id, a.ersetzt_durch ?? null])
  def('rahmen_anlegen', 'daten', 'Rahmen anlegen', 'Legt einen neuen Council-Auftrag im Status entwurf an. Nur nach ausdrücklicher Ansage des Nutzers. Danach Pflichtangaben mit angaben_setzen. Für automatische Runden nur OpenRouter-Teilnehmer verwenden.', {
    titel: z.string().min(1), originalfrage: z.string().min(1), kostenlimit_usd: z.number().min(0),
    projekt: z.string().optional(), ziel: z.string().optional(), vorgaben: z.string().optional(), grenzen: z.string().optional(),
    ergebnisform: z.string().optional(), methoden: z.array(z.string()).optional(),
    vorschlaege_stamm_ki: z.record(z.string(), z.unknown()).optional(),
    haltbarkeit: z.enum(['einmalig', 'projekt', 'dauerhaft']).optional(),
    automatisierungsstufe: z.number().int().min(1).max(3).optional(), max_kritikrunden: z.number().int().min(0).max(10).optional(),
    teilnehmer: z.array(z.object({ teilnehmer: z.string(), rolle: z.string().optional(), plan_label: z.string() })),
  }, (a) => [h, JSON.stringify(a)])
  def('angaben_setzen', 'daten', 'Pflichtangaben setzen', 'Legt die Checkliste der Pflichtangaben an oder trägt Antworten ein.', {
    rahmen_id: z.number().int(),
    angaben: z.array(z.object({ frage: z.string().min(1), antwort: z.string().optional(), pflicht: z.boolean().optional() })),
  }, (a) => [h, a.rahmen_id, JSON.stringify(a.angaben)])
  def('stammdaten_freigeben', 'daten', 'Stammdaten für Auftrag freigeben', 'Legt fest, welche Stammdaten (ids aus stammdaten_lesen) die KIs in diesem Auftrag sehen dürfen. Ersetzt die bisherige Auswahl. Nur relevante Einträge, vom Nutzer bestätigt. Nie-extern-Daten sind gesperrt.', {
    rahmen_id: z.number().int(), ids: z.array(z.number().int()).describe('Leere Liste = keine Stammdaten'),
  }, (a) => [h, a.rahmen_id, '{' + (a.ids ?? []).map((x: number) => Math.trunc(x)).join(',') + '}'])
  def('auftrag_starten', 'daten', 'Auftrag automatisch starten', 'Nur nach Okay des Nutzers: startet den automatischen Ablauf über OpenRouter (Entwurf blind, Kritik, Ergebnis in den Posteingang). Stufe 3 = durchlaufen, Stufe 2 = Stopp vor jeder Kritikrunde. Nur OpenRouter-Teilnehmer, mindestens 2, Kostenlimit Pflicht.', {
    rahmen_id: z.number().int(), stufe: z.number().int().min(2).max(3).optional().describe('Standard 3'),
  }, (a) => [h, a.rahmen_id, a.stufe ?? 3])
  def('auftrag_weiter', 'daten', 'Pausierten Auftrag fortsetzen', 'Nur nach Okay des Nutzers: setzt einen pausierten Auftrag fort (Stufe-2-Freigabe, nach Fehler). Bei erreichtem Kostenlimit ein höheres neues_kostenlimit angeben.', {
    rahmen_id: z.number().int(), neues_kostenlimit: z.number().optional(),
  }, (a) => [h, a.rahmen_id, a.neues_kostenlimit ?? null])
  def('rahmen_status_setzen', 'daten', 'Auftragsstatus setzen', 'bestaetigt nur nach Nutzer-Okay; laeuft, ruhend, abgeschlossen, abgebrochen.',
    { rahmen_id: z.number().int(), status: z.enum(['bestaetigt', 'laeuft', 'ruhend', 'abgeschlossen', 'abgebrochen']) }, (a) => [h, a.rahmen_id, a.status])
  def('runde_starten', 'daten', 'Runde starten (Handbetrieb)', 'Startet die nächste Runde (entwurf, kritik, zusatz, ergebnis) im Handbetrieb.', {
    rahmen_id: z.number().int(), typ: z.enum(['entwurf', 'kritik', 'zusatz', 'ergebnis']),
    schwerpunkt: z.string().optional(), frist: z.string().optional(),
  }, (a) => [h, a.rahmen_id, a.typ, a.schwerpunkt ?? null, a.frist ?? null])
  def('ergebnis_speichern', 'daten', 'Ergebnis speichern', 'Speichert das Ergebnis eines Auftrags und legt es in den Posteingang (Status neu). Kurzname und Übergabe sind Pflicht.', {
    rahmen_id: z.number().int(),
    kurzname: z.string().min(1).describe('2-3 Worte, z. B. "Tokio-Unterkunft"'),
    uebergabe: z.string().min(1).describe('5-10 Zeilen: Ergebnis, was zu entscheiden ist, offene Fragen, empfohlener nächster Schritt'),
    empfehlung: z.string().min(1),
    streitpunkte: z.array(z.object({ thema: z.string(), plan_a: z.string().optional(), plan_b: z.string().optional(), weitere: z.string().optional() })).optional(),
    fakten: z.array(z.object({ aussage: z.string(), quelle: z.string().optional(), stand: z.string().optional() })).optional(),
    annahmen: z.array(z.string()).optional(), offene_fragen: z.array(z.string()).optional(),
    entscheidungsvorschlaege: z.array(z.object({ label: z.string(), beschreibung: z.string().optional() })).optional(),
    konsens_warnung: z.string().optional(),
  }, (a) => { const { rahmen_id, ...rest } = a; return [h, rahmen_id, JSON.stringify(rest)] })
  def('ausfall_entscheiden', 'daten', 'Ausfall entscheiden', 'Nur auf Entscheidung des Nutzers: erneut_versuchen, teilnehmer_ausschliessen, abbrechen.', {
    rahmen_id: z.number().int(), runde_nr: z.number().int(), entscheidung: z.enum(['erneut_versuchen', 'teilnehmer_ausschliessen', 'abbrechen']),
    neue_frist: z.string().optional(), plan_label: z.string().optional(),
  }, (a) => [h, a.rahmen_id, a.runde_nr, a.entscheidung, a.neue_frist ?? null, a.plan_label ?? null])
  def('fristen_pruefen', 'daten', 'Fristen prüfen', 'Pausiert Aufträge mit abgelaufener Frist und fehlenden Beiträgen.', {}, () => [h])
  def('besetzung_speichern', 'daten', 'Besetzungsvorschlag speichern', 'Speichert den Vorschlag, welche KI welche Rolle übernimmt, mit Begründung und Datenlage. Danach dem Nutzer vorlegen.', {
    rahmen_id: z.number().int(), vorschlag: BESETZUNG.min(1), begruendung: z.string().min(1),
    datenlage: z.enum(['zu_wenig_daten', 'teilweise_belastbar']).optional(),
  }, (a) => [h, a.rahmen_id, JSON.stringify(a.vorschlag), a.begruendung, a.datenlage ?? null])
  def('besetzung_entscheiden', 'daten', 'Besetzung entscheiden', 'Nur auf Entscheidung des Nutzers: uebernommen, geaendert (mit gewählter Besetzung) oder verworfen. Nur solange keine Runde läuft.', {
    id: z.number().int(), entscheidung: z.enum(['uebernommen', 'geaendert', 'verworfen']), gewaehlt: BESETZUNG.optional(),
  }, (a) => [h, a.id, a.entscheidung, a.gewaehlt ? JSON.stringify(a.gewaehlt) : null])

  // ---------- Nur Leitung ----------
  def('bewertung_abgeben', 'leiten', 'Bewertung abgeben (Leitung)', 'Noten 1-5 je Kriterium für einen Teilnehmer (Plan A/B). bewertet_von nutzer = nur auf Ansage des Nutzers (überschreibt die KI-Note); stamm_ki = eigene Einschätzung (Gewicht 0,5).', {
    rahmen_id: z.number().int(), plan_label: z.string().min(1), bewertet_von: z.enum(['nutzer', 'stamm_ki']),
    noten: z.record(z.string(), z.number().int().min(1).max(5)), kommentar: z.string().optional(),
  }, (a) => [h, a.rahmen_id, a.plan_label, a.bewertet_von, JSON.stringify(a.noten), a.kommentar ?? null])
  def('nutzer_urteil', 'leiten', 'Gesamturteil des Nutzers (Leitung)', 'Nur auf Ansage des Nutzers: hält fest, ob ihm das Ergebnis geholfen hat (ja / teilweise / nein), optional mit Kommentar.', {
    rahmen_id: z.number().int(), urteil: z.enum(['ja', 'teilweise', 'nein']), kommentar: z.string().optional(),
  }, (a) => [h, a.rahmen_id, a.urteil, a.kommentar ?? null], SCHREIBT, true)
  def('bewertung_anstossen', 'leiten', 'Bewertung anstoßen (Leitung)', 'Startet die neutrale Bewerter-KI für ein vorhandenes Ergebnis (erneut). Läuft im Hintergrund (1-5 Minuten); danach bewertung_lesen.', {
    rahmen_id: z.number().int(),
  }, (a) => [h, a.rahmen_id], SCHREIBT, true)
  def('rollen_erkenntnis_speichern', 'leiten', 'Rollen-Erkenntnis speichern (Leitung)', 'Hält nach einer Bewertung fest, was über eine Rolle gelernt wurde (Stärke, Schwäche, Verbesserung, Beobachtung).', {
    rolle: z.string().min(1), art: z.enum(['staerke', 'schwaeche', 'verbesserung', 'beobachtung']), erkenntnis: z.string().min(1),
    quelle: z.enum(['nutzer', 'stamm_ki']), modell: z.string().optional(), bereich: z.string().optional(), rahmen_id: z.number().int().optional(),
  }, (a) => [h, JSON.stringify(a)])
  def('rolle_entscheiden', 'leiten', 'Rollenvorschlag entscheiden (Leitung)', 'Nur auf Entscheidung des Nutzers: aktivieren, ersetzen (Basisrolle überarbeiten, alte Fassung bleibt als Version) oder ablehnen.', {
    id: z.number().int(), entscheidung: z.enum(['aktivieren', 'ersetzen', 'ablehnen']),
    korrektur: z.object({ name: z.string().optional(), typ: z.enum(['grund', 'zusatz', 'fach']).optional(), stellenbeschreibung: z.string().optional(),
      arbeitsmuster: z.array(z.string()).optional(), pflichtfragen: z.array(z.string()).optional(), schlagworte: z.array(z.string()).optional(), grund: z.string().optional() }).optional(),
  }, (a) => [h, a.id, a.entscheidung, a.korrektur ? JSON.stringify(a.korrektur) : null])
  def('rolle_archivieren', 'leiten', 'Rolle archivieren (Leitung)', 'Nur auf Ansage des Nutzers: nimmt eine aktive Rolle aus dem Einsatz. Nichts wird gelöscht.',
    { name: z.string().min(1), grund: z.string().min(1) }, (a) => [h, a.name, a.grund])
  def('einstellung_setzen', 'leiten', 'Einstellung setzen (Leitung)', 'Nur auf Ansage des Nutzers: ändert eine vorhandene Einstellung (start_ki, ergebnis_modell, zdr_pflicht, max_tokens_beitrag, min_auftraege_fuer_vorschlag, bewerter_modelle, bewertung_automatisch).',
    { name: z.string().min(1), wert: z.unknown() }, (a) => [h, a.name, JSON.stringify(a.wert)])
  def('mein_modell_setzen', 'leiten', 'Meine Modelle pflegen (Leitung)', 'Nur auf Ansage des Nutzers: nimmt ein OpenRouter-Modell in "Meine Modelle" auf oder ändert es (mein_modell false = entfernen). Legt den passenden Teilnehmer automatisch an. Stammdaten nur bei ZDR-Modellen.', {
    openrouter_id: z.string().min(1), mein_modell: z.boolean().optional(), stammdaten_erlaubt: z.boolean().optional(), staerken: z.string().optional(),
  }, (a) => [h, JSON.stringify(a)])
  def('aufraeumen', 'leiten', 'Aufräumrunde (Leitung)', 'Löscht fällige Verläufe einmaliger, abgeschlossener Aufträge nach 30 Tagen (Ergebnis und Archiv bleiben) und listet ruhende Aufträge.', {}, () => [h], LOESCHT)

  // ---------- Werkstatt (Bauschritt 14) ----------
  lese('werkstatt_lesen', 'teilnehmen', 'Werkstatt: Überblick', 'Werkstatt = Absprache zwischen Claude und ChatGPT über Programmierwünsche von Sebastian am System. Zeigt Regeln W1-W7, neue Nachrichten an dich (danach als gelesen markiert), offene Wünsche, aktive Sperren, letzte Änderungen. Aufrufen, wenn Sebastian "Werkstatt" sagt, und bevor du am System etwas änderst.',
    { alle: z.boolean().optional().describe('true zeigt auch erledigte/verworfene Wünsche') }, (a) => [h, a.alle ?? false], true)
  lese('werkstatt_wunsch_lesen', 'teilnehmen', 'Werkstatt: Wunsch im Detail', 'Nur lesen. Ein Programmierwunsch mit Beschreibung, allen Nachrichten, Änderungen und Sperren.',
    { id: z.number().int() }, (a) => [h, a.id], true)
  def('werkstatt_wunsch_anlegen', 'daten', 'Werkstatt: Wunsch anlegen', 'Legt einen Programmierwunsch an. im_auftrag_nutzer = true NUR, wenn Sebastian ihn selbst geäußert hat (dann sofort freigegeben); eigene Ideen bleiben Vorschlag. Zuständig standardmäßig: datenbank/motor/zugang = Claude, app = ChatGPT.', {
    titel: z.string().min(3), beschreibung: z.string().optional(),
    bereich: z.enum(['datenbank', 'motor', 'zugang', 'app', 'sonstiges']).optional(),
    prioritaet: z.number().int().min(1).max(3).optional().describe('1 = hoch, 3 = niedrig'),
    im_auftrag_nutzer: z.boolean().optional(), zustaendig: z.string().optional().describe('Claude oder ChatGPT; nur auf Ansage von Sebastian abweichend vom Standard'),
  }, (a) => [h, JSON.stringify(a)], SCHREIBT, true)
  def('werkstatt_wunsch_status', 'daten', 'Werkstatt: Status ändern', 'Status eines Wunsches setzen: in_arbeit/pruefung (nur zuständige KI, nur freigegebene Wünsche), erledigt (zuständige KI), freigegeben/verworfen und Zuständigkeitswechsel NUR mit nutzer_ansage = true auf Sebastians ausdrückliche Ansage. Erzeugt automatisch eine Nachricht.', {
    id: z.number().int(), status: z.enum(['vorschlag', 'freigegeben', 'in_arbeit', 'pruefung', 'erledigt', 'verworfen']),
    nutzer_ansage: z.boolean().optional(), zustaendig: z.string().optional(), notiz: z.string().optional(),
  }, (a) => [h, a.id, a.status, a.nutzer_ansage ?? false, a.zustaendig ?? null, a.notiz ?? null], SCHREIBT, true)
  def('werkstatt_nachricht', 'teilnehmen', 'Werkstatt: Nachricht schreiben', 'Nachricht an die andere KI (oder an alle), optional zu einem Wunsch: frage, antwort, info, vorschlag, uebergabe, pruefbitte, pruefergebnis; an Sebastian: entscheidung (er muss entscheiden – kurz, Optionen, Empfehlung) oder fertig (Paket geprüft, bereit zur Live-Freigabe) – beide erzeugen eine Handy-Meldung. Keine Schlüssel oder Stammdaten-Inhalte.', {
    text: z.string().min(1).max(8000), wunsch_id: z.number().int().optional(),
    an: z.string().optional().describe('Claude, ChatGPT oder alle (Standard)'),
    art: z.enum(['frage', 'antwort', 'info', 'vorschlag', 'uebergabe', 'pruefbitte', 'pruefergebnis', 'entscheidung', 'fertig']).optional(),
  }, (a) => [h, a.wunsch_id ?? null, a.an ?? null, a.art ?? 'info', a.text], SCHREIBT, true)
  def('werkstatt_sperre', 'daten', 'Werkstatt: Objekt sperren/freigeben', 'Vor jeder Änderung das Objekt sperren (z. B. db:api.werkstatt_lesen, db:schema-council, edge:council-motor, app:repo), nach Abschluss mit freigeben = true lösen. Nur für freigegebene Wünsche. Abgelaufene Sperren (Standard 4 h, max. 24 h) gelten als frei.', {
    objekt: z.string().regex(/^(db|edge|app|einstellung|sonstiges):.+/).describe('Präfix db:, edge:, app:, einstellung: oder sonstiges:'),
    wunsch_id: z.number().int().optional(), stunden: z.number().min(0.25).max(24).optional(), freigeben: z.boolean().optional(),
  }, (a) => [h, a.objekt, a.wunsch_id ?? null, a.stunden ?? 4, a.freigeben ?? false], SCHREIBT, true)
  def('werkstatt_aenderung', 'daten', 'Werkstatt: Änderung protokollieren', 'Nach jeder Änderung am System festhalten, was geändert wurde (Migration, Deploy, Einstellung, Commit), mit Version.', {
    objekt: z.string().min(1), art: z.enum(['migration', 'deploy', 'einstellung', 'commit', 'sonstiges']), beschreibung: z.string().min(3),
    wunsch_id: z.number().int().optional(), version: z.string().optional(),
  }, (a) => [h, JSON.stringify(a)], SCHREIBT, true)

  // ---------- Darstellung (Bauschritt 18) ----------
  lese('verlauf_lesen', 'teilnehmen', 'Ergebnis darstellen (Markdown)', 'Nur lesen. Liefert die Darstellung eines Auftrags als fertiges Markdown, das UNVERÄNDERT angezeigt wird (nicht zusammenfassen, nicht umformulieren). ebene: uebersicht (Tabelle Plan/Rolle/Modell/Linie/Note, Empfehlung, Streitpunkte), verlauf (Positionen je Runde, optional plan), belege (geprüfte Belegliste, optional plan), volltext (ein Beitrag: plan + runde_nr).', {
    rahmen_id: z.number().int(), ebene: z.enum(['uebersicht', 'verlauf', 'belege', 'volltext']).optional().describe('Standard uebersicht'),
    plan: z.string().optional().describe('z. B. "A" oder "Plan A"'), runde_nr: z.number().int().optional(),
  }, (a) => [h, a.rahmen_id, a.ebene ?? 'uebersicht', a.plan ?? null, a.runde_nr ?? null], true)

  // ---------- Fach-Tool unterkunft (Bauschritt 23/23b, Werkstatt #15) ----------
  const KANDIDAT_FELDER = {
    rahmen_id: z.number().int(), id: z.number().int().optional().describe('Nur zum Aktualisieren; fremder Kandidat: nur zweitquelle_url, zweitquelle_preis_eur, notizen'),
    name: z.string().optional().describe('Objektname (Hotel/Haus)'), angebot: z.string().optional().describe('Konkretes Angebot, z. B. "Suite 55 m²", "Familienzimmer 4P", "ganzes Haus", "2× Standard (Notlösung)". Pflicht bei Neuanlage; Doppelschlüssel = name + angebot'),
    typ: z.enum(['haus', 'machiya', 'apartment', 'aparthotel', 'hotel', 'sonstiges']).optional(),
    quelle: z.string().optional().describe('Plattform, z. B. Booking.com, Airbnb'), url: z.string().optional().describe('Direktlink zur Detailseite, selbst aufgerufen'),
    strasse: z.string().optional(), stadtteil: z.string().optional(), stadt: z.string().optional(),
    checkin: z.string().optional().describe('JJJJ-MM-TT'), checkout: z.string().optional().describe('JJJJ-MM-TT'),
    preis_gesamt_eur: z.number().optional().describe('Endpreis für 4 Personen inkl. aller Gebühren/Steuern'), preis_waehrung_original: z.string().optional(), preis_original: z.number().optional(),
    preis_stand: z.string().optional().describe('Zeitstempel des Preisabrufs, ISO'),
    preis_vollstaendig: z.enum(['ja', 'unklar']).optional().describe('ja = alle Pflichtkosten enthalten; unklar = etwas offen (dann preis_hinweis)'),
    preis_hinweis: z.string().optional().describe('Tarif, Belegung, was im Preis fehlt oder unklar ist'),
    preis_alternativen: z.array(z.object({ checkin: z.string(), checkout: z.string(), naechte: z.number().int().optional(), preis_gesamt_eur: z.number().optional(), hinweis: z.string().optional() })).optional().describe('Weitere geprüfte Zeiträume: 14-N-Fenster, 7/10/4-N-Abschnitte'),
    flaeche_qm: z.number().optional().describe('Nur wenn angegeben; bei 2 Zimmern Summe, Einzelwerte in betten_beschreibung'), schlafbereiche: z.number().int().optional(), betten_beschreibung: z.string().optional(), max_personen: z.number().int().optional(),
    kueche: z.enum(['ja', 'kitchenette', 'nein']).optional(), waschmaschine: z.enum(['ja', 'im_haus', 'nein']).optional(), bad_anzahl: z.number().optional(), parkplatz: z.enum(['ja', 'kostenpflichtig', 'nein']).optional(),
    bahn_station: z.string().optional(), bahn_gehminuten: z.number().int().optional(), min_kyoto_station: z.number().int().optional(), min_gion: z.number().int().optional(), min_arashiyama: z.number().int().optional(), supermarkt_gehminuten: z.number().int().optional(),
    lizenz_oder_belegung_ok: z.enum(['ja', 'nein', 'unklar']).optional().describe('Lizenz UND Belegung für 4 getrennt geprüft; nur ja wenn beides belegt'), storno_kostenlos_bis: z.string().optional(), bewertung_plattform: z.string().optional(), bewertungen_anzahl: z.number().int().optional(),
    lage_score: z.number().int().min(1).max(5).optional(), lage_begruendung: z.string().optional(), ausstattung_score: z.number().int().min(1).max(5).optional(),
    charme_score: z.number().int().min(1).max(5).optional(), charme_begruendung: z.string().optional().describe('Meinung, ein Satz'),
    szenario_fit: z.array(z.enum(['A', 'B', 'C'])).optional(), zweitquelle_url: z.string().optional(), zweitquelle_preis_eur: z.number().optional(), notizen: z.string().optional(),
  }
  def('unterkunft_kandidat_einreichen', 'teilnehmen', 'Unterkunft: Kandidat einreichen/aktualisieren', 'Legt einen Unterkunfts-Kandidaten zu einem Auftrag an oder aktualisiert den eigenen (mit id). Neu: name, angebot, typ, quelle, url, stadt sind Pflicht; gleiches Objekt + Angebot im Auftrag wird als Doppel abgewiesen (dann mit id nur Zweitquelle/Notizen ergänzen); anderes Angebot desselben Hauses = eigener Eintrag. Vorher unterkunft_kandidaten_lesen. Kein Eintrag ohne selbst aufgerufene URL.', KANDIDAT_FELDER,
    (a) => [h, JSON.stringify(a)], SCHREIBT, true)
  lese('unterkunft_kandidaten_lesen', 'teilnehmen', 'Unterkunft: Kandidaten lesen', 'Nur lesen. Alle Kandidaten eines Auftrags mit berechneten Feldern (naechte, preis_pro_nacht_eur, preis_pro_qm_nacht, note_pruefung, note_eignung, bewertungen). Recherche offen; fremde Eignungsnoten erst nach Offenlegung der Entwurfsrunde. Sortierung: preis_pro_nacht_eur (Standard), preis_pro_qm_nacht, flaeche_qm, lage_score, charme_score, ausstattung_score, note_pruefung, note_eignung, note_schnitt, erstellt_am, stadt, name.', {
    rahmen_id: z.number().int(), sortierung: z.string().optional(), nur_eigene: z.boolean().optional(),
  }, (a) => [h, a.rahmen_id, a.sortierung ?? null, a.nur_eigene ?? false], true)
  def('unterkunft_kandidat_bewerten', 'teilnehmen', 'Unterkunft: Kandidaten bewerten', 'art pruefung (Standard): Note 1-10 + Kommentar für einen FREMDEN Kandidaten – Preis bei eigenem Aufruf bestätigt? URL erreichbar? Lage/Gehminuten korrekt? Für 4 zugelassen? Fehler hart benennen. art eignung: Note 1-10 für die Eignung für die Familie, auch eigene Kandidaten (Finalisten). Erneuter Aufruf überschreibt.', {
    id: z.number().int(), art: z.enum(['pruefung', 'eignung']).optional().describe('Standard pruefung'), note: z.number().int().min(1).max(10), kommentar: z.string().optional(),
  }, (a) => [h, a.id, a.art ?? 'pruefung', a.note, a.kommentar ?? null], SCHREIBT, true)
  def('unterkunft_urteil', 'daten', 'Unterkunft: Urteil des Nutzers', 'Nur auf Ansage des Nutzers: ja, vielleicht, nein oder zu_teuer je Kandidat, optional Kommentar.', {
    id: z.number().int(), urteil: z.enum(['ja', 'vielleicht', 'nein', 'zu_teuer']), kommentar: z.string().optional(),
  }, (a) => [h, a.id, a.urteil, a.kommentar ?? null], SCHREIBT, true)

  // ---------- Unterkunftssuchtool (Suchtool Bauschritt 1, Werkstatt #36) ----------
  const QUELLEN_KAT = ['rakuten', 'hotelseite', 'booking_plugin', 'serpapi', 'trivago', 'manuell'] as const
  def('unterkunft_zimmerkategorien_setzen', 'daten', 'Suchtool: Zimmerkategorien speichern', 'Speichert den Zimmerkatalog eines Objekts (stamm_id) aus EINER Quelle. Nur Katalogdaten (Name, m², Betten, Belegung, Schlafzimmer, Balkon) – KEINE Preise. Betten nur mit betten_eindeutig true, wenn Zahl und Art eindeutig angegeben sind. Vorhandene Kategorien gleicher Quelle bleiben stehen, außer ueberschreiben true. Unplausible Angaben (unter 6 m² je Person, Belegung passt nicht zu Betten) werden als konflikt markiert.', {
    stamm_id: z.number().int(), quelle: z.enum(QUELLEN_KAT), ueberschreiben: z.boolean().optional(),
    kategorien: z.array(z.object({
      name: z.string().min(1), quell_kategorie_id: z.string().optional(), m2: z.number().optional(),
      betten_anzahl: z.number().int().optional(), betten_art: z.string().optional(), betten_text: z.string().optional().describe('Originaltext der Bettangabe'),
      betten_eindeutig: z.boolean().optional(), max_personen: z.number().int().optional(), schlafzimmer: z.number().int().optional(),
      balkon: z.enum(['ja', 'nein', 'unklar']).optional(), konflikt_hinweis: z.string().optional(), quelle_url: z.string().optional(),
    })).min(1).max(40),
  }, (a) => [h, JSON.stringify(a)], SCHREIBT, true)
  def('unterkunft_lueckenfueller_anlegen', 'daten', 'Suchtool: Lückenfüller-Auftrag anlegen', 'Legt einen Auftrag an, fehlende Zimmerdaten für 1-30 Treffer nachzuholen (App-Knopf). Gleiche Treffer + Felder = derselbe offene Auftrag (kein Doppel). Liefert id und den vorgefüllten Text für die Claude-Sitzung.', {
    treffer_ids: z.array(z.number().int()).min(1).max(30), felder: z.array(z.enum(['zimmerkategorien', 'gesamtpreis', 'balkon', 'storno'])).optional().describe('Standard zimmerkategorien'),
    hinweis: z.string().optional(), idempotenz: z.string().optional(),
  }, (a) => [h, JSON.stringify(a)], SCHREIBT, true)
  def('unterkunft_lueckenfueller_abholen', 'leiten', 'Suchtool: Lückenfüller-Auftrag abholen (Leitung)', 'Holt einen offenen Lückenfüller-Auftrag (mit id gezielt, sonst den ältesten) und setzt ihn auf in_arbeit. Liefert Treffer mit Objektdaten und Anleitung. Hängende Aufträge werden nach 30 Minuten wieder abholbar, höchstens 3 Versuche.', {
    id: z.number().int().optional(),
  }, (a) => [h, a.id ?? null], SCHREIBT, true)
  def('unterkunft_lueckenfueller_abschliessen', 'leiten', 'Suchtool: Lückenfüller-Auftrag abschließen (Leitung)', 'Schließt einen abgeholten Auftrag ab: erledigt, teilweise oder nicht_moeglich, mit Ergebnis (z. B. je Treffer was gefunden wurde, was fehlt).', {
    id: z.number().int(), status: z.enum(['erledigt', 'teilweise', 'nicht_moeglich']), ergebnis: z.record(z.string(), z.unknown()).optional(),
  }, (a) => [h, a.id, a.status, JSON.stringify(a.ergebnis ?? {})], SCHREIBT, true)
  // ---------- Highlights: Recherche per Chat (Werkstatt #155) ----------
  lese('highlights_chat_offen', 'teilnehmen', 'Highlights: offene Chat-Aufträge', 'Nur lesen. Recherche-Aufträge aus der App (Reisen › Highlights), die im Chat erledigt werden sollen: Nummer, Wunsch, wo (Region/Highlight), Art (z. B. Essen, Wohnen, Nähe, Frage).', {}, () => [h], true)
  def('highlights_chat_abholen', 'daten', 'Highlights: Chat-Auftrag abholen', 'Holt einen Recherche-Auftrag (mit id gezielt, sonst den ältesten) und setzt ihn auf in Arbeit. Liefert Kontext (Wunsch, Pfad, schon vorhandene, Will ich / Erstmal nicht) und die Anleitung mit dem Kartenformat. Danach mit Websuche recherchieren und highlights_chat_abschliessen aufrufen.', {
    id: z.number().int().optional(),
  }, (a) => [h, a.id ?? null], SCHREIBT, true)
  def('highlights_chat_abschliessen', 'daten', 'Highlights: Chat-Ergebnis zurückschreiben', 'Schreibt die recherchierten Karten in die App (höchstens 15). Felder je Karte wie in der Anleitung: titel, typ, ort, moment, besonders (WOW-Begründung), wow 1-5, andrang 1-5, zeit, kosten_4 (Euro, für 4 Personen), saison {text,status}, lat, lon, bild_motiv (englisch), wiki_titel, quellen [URLs], optional fach, lohnt, eher_nicht, frage, ruhig, mindestalter, familie_hinweis, warnung + warnung_art (nur echte Sperre). Fotos holt das System danach selbst (nur frei lizenziert).', {
    id: z.number().int(), fazit: z.string().optional(), ende: z.boolean().optional().describe('true, wenn es hier nichts Starkes mehr gibt'),
    karten: z.array(z.record(z.string(), z.unknown())).min(1).max(15),
  }, (a) => [h, a.id, JSON.stringify({ karten: a.karten, fazit: a.fazit ?? null, ende: a.ende ?? false })], SCHREIBT, true)
  lese('unterkunft_lueckenfueller_lesen', 'teilnehmen', 'Suchtool: Lückenfüller-Aufträge lesen', 'Nur lesen. Die letzten 50 Lückenfüller-Aufträge, optional nach Status.', {
    status: z.enum(['erzeugt', 'in_arbeit', 'erledigt', 'teilweise', 'nicht_moeglich']).optional(),
  }, (a) => [h, a.status ?? null], true)
  def('unterkunft_treffer_status_setzen', 'daten', 'Suchtool: Treffer merken/ausschließen', 'Setzt den Status eines Suchtreffers: aktiv, ausgeschlossen oder favorit.', {
    treffer_id: z.number().int(), status: z.enum(['aktiv', 'ausgeschlossen', 'favorit']),
  }, (a) => [h, a.treffer_id, a.status], SCHREIBT, true)
  lese('unterkunft_suchlauf_lesen', 'teilnehmen', 'Suchtool: Suchlauf lesen', 'Nur lesen. Ohne suchauftrag_id: die letzten 10 Suchaufträge. Mit id: Suchauftrag, Kostenstand, Kartendaten (karte: ziel, stationen) und alle Treffer mit Foto (bild), primärem Angebot, Bewertung (inkl. filter_ergebnis), Gehzeit zur Station, letzter Rückmeldung und Zimmerkategorien, sortiert nach Score.', {
    suchauftrag_id: z.number().int().optional(),
  }, (a) => [h, a.suchauftrag_id ?? null], true)

  // ---------- Unterkunftssuchtool Sammler (Suchtool Bauschritt 2, Werkstatt #39; erweitert Ausbau 3a, #52) ----------
  const KRITERIUM = z.object({ modus: z.enum(['pflicht', 'wunsch', 'egal']), wert: z.number().optional(), werte: z.array(z.number()).optional().describe('nur viertel_auswahl: Zonen-IDs') })
  const SUCH_FELDER = {
    erwachsene: z.number().int().min(1).max(10).optional(), kinder_alter: z.array(z.number().int().min(0).max(17)).optional(),
    budget_eur: z.number().optional().describe('Gesamtbudget für den Aufenthalt (harte Grenze bei belegtem Preis)'), schlafzimmer_min: z.number().int().min(0).max(6).optional().describe('Standard 2'),
    land: z.string().optional().describe('ISO-Code, z. B. JP'), quellen: z.array(z.string()).optional(),
    max_je_quelle: z.number().int().min(5).max(100).optional().describe('Standard 50'), limit_usd: z.number().min(0).max(10).optional().describe('Kostenlimit, Standard 1,50 USD'),
    profil: z.enum(['staedte']).optional().describe('Hauptart: in V1 nur Städtereise'),
    nebenart: z.enum(['erholung', 'strand', 'tauchen', 'natur', 'roadtrip']).optional(), nebenart_anteil: z.number().int().min(10).max(50).optional().describe('Prozent, Standard 30'),
    unterkunftsform: z.enum(['alle', 'hotel', 'apartment', 'haus']).optional(), suite: z.boolean().optional().describe('Suite als Wunsch'),
    qualitaetsfilter: z.boolean().optional().describe('false = kein K.o. wegen Note (Standard true)'), note_min: z.number().min(0).max(10).optional(), bewertungen_min: z.number().int().min(0).optional(),
    kriterien: z.record(z.string(), KRITERIUM).optional().describe('Kriterien aus unterkunft_suchprofile_lesen.kriterien_katalog, je {modus pflicht|wunsch|egal, wert bei Zahlen}; Viertel: viertel_auswahl {werte:[zone_id]}, viertel_ruhig, viertel_<merkmal>_min {wert 0-10}'),
  }
  def('unterkunft_suchauftrag_anlegen', 'daten', 'Suchtool: Suchauftrag anlegen', 'Nur auf Ansage des Nutzers. Legt einen Suchauftrag an (Status entwurf). Hauptart Städtereise, optional Nebenart mit Anteil (Gewichte werden gemischt, Dauer passt sie an), Unterkunftsform, Kriterien Pflicht/Wunsch/Egal, Qualitätsfilter, optional suchprofil (Name) als Voreinstellung. Quellen-Standard: JP -> hasdata_booking, apify_airbnb, rakuten_travel, trivago_mcp; sonst hasdata_booking, apify_airbnb, trivago_mcp. Starten mit unterkunft_suche_starten.', {
    ziel: z.string().min(2).describe('Ort, z. B. "Tokyo"'), anreise: z.string().describe('JJJJ-MM-TT'), abreise: z.string().describe('JJJJ-MM-TT'),
    suchprofil: z.string().optional().describe('Name eines gespeicherten Suchprofils'),
    zielpunkte: z.array(z.object({ name: z.string(), lat: z.number(), lon: z.number() })).max(5).optional(),
    ...SUCH_FELDER,
  }, (a) => [h, JSON.stringify(a)], SCHREIBT, true)
  def('unterkunft_suche_starten', 'daten', 'Suchtool: Suche starten', 'Nur auf Ansage des Nutzers. Startet den Sammler für einen Suchauftrag im Hintergrund (1-3 Minuten Sammeln, danach 1-2 Minuten Bewerten). Läuft schon eine andere Suche, wartet diese in der Warteschlange und startet automatisch. Stand mit unterkunft_suche_status.', {
    suchauftrag_id: z.number().int(),
  }, (a) => [h, a.suchauftrag_id], SCHREIBT, true)

  // ---------- Unterkunftssuchtool Ablaufsteuerung (Suchtool Bauschritt 5, Werkstatt #46) ----------
  lese('unterkunft_suche_status', 'teilnehmen', 'Suchtool: Status einer Suche', 'Nur lesen. Leichter Stand einer Suche ohne Trefferliste: status (wartet/laeuft/fertig/fehler/abgebrochen), phase (warteschlange/sammeln/bewerten), Warteschlangen-Position, Fortschritt als Text, Schritte je Quelle, Zähler (gesammelt, Liste A/B, unbewertet, Top 10), Kosten (ist/reserviert/limit). Ergebnisliste danach mit unterkunft_suchlauf_lesen.', {
    suchauftrag_id: z.number().int(),
  }, (a) => [h, a.suchauftrag_id], true)
  def('unterkunft_suche_abbrechen', 'daten', 'Suchtool: Suche abbrechen', 'Nur auf Ansage des Nutzers. Bricht eine laufende oder wartende Suche ab. Bereits gesammelte Treffer bleiben lesbar.', {
    suchauftrag_id: z.number().int(),
  }, (a) => [h, a.suchauftrag_id], SCHREIBT, true)

  // ---------- Unterkunftssuchtool Rückmeldung (Suchtool Bauschritt 7, Werkstatt #47) ----------
  def('unterkunft_rueckmeldung_geben', 'daten', 'Suchtool: Rückmeldung zu einem Treffer', 'Nur auf Ansage des Nutzers. Hält sein Urteil zu einem Suchtreffer fest: passt, passt_nicht, zu_teuer oder gebucht, optional mit Grund. Ein neues Urteil zum selben Treffer ersetzt das alte im Report. Ändert die Rangliste nicht.', {
    treffer_id: z.number().int(), urteil: z.enum(['passt', 'passt_nicht', 'zu_teuer', 'gebucht']), grund: z.string().max(1000).optional(),
  }, (a) => [h, a.treffer_id, a.urteil, a.grund ?? null], SCHREIBT, true)
  lese('unterkunft_rueckmeldung_report', 'teilnehmen', 'Suchtool: Rückmelde-Report', 'Nur lesen. Ab 20 Urteilen (Einstellung report_min_urteile): Vergleich der Bildmerkmale (hell, modern, gepflegt, geräumig) und Spaltennoten nach Urteil (gefällt / gefällt nicht / zu teuer) als fertiges Markdown in text, dazu Gründe. Darunter nur der Zählerstand. Keine automatische Gewichtsänderung.', {},
    () => [h], true)

  // ---------- Unterkunftssuchtool Suchprofile (Ausbau 3a, Werkstatt #52) ----------
  def('unterkunft_suchprofil_speichern', 'daten', 'Suchtool: Suchprofil speichern', 'Nur auf Ansage des Nutzers. Speichert ein Suchprofil (Name + Voreinstellungen) oder ersetzt das gleichnamige. Erlaubte Felder wie beim Suchauftrag ohne Ziel und Daten.', {
    name: z.string().min(1).max(60), felder: z.object(SUCH_FELDER),
  }, (a) => [h, JSON.stringify(a)], SCHREIBT, true)
  lese('unterkunft_suchprofile_lesen', 'teilnehmen', 'Suchtool: Suchprofile und Kriterienkatalog', 'Nur lesen. Gespeicherte Suchprofile, erlaubte Reisearten (Haupt/Neben), Unterkunftsformen, Kriterienkatalog je Block (Raum, Lage, Preis, Bewertungen, Ausstattung) und Regeln für Pflicht/Wunsch/Egal.', {},
    () => [h], true)

  // ---------- Unterkunftssuchtool Ortswissen / Viertel (Werkstatt #60) ----------
  lese('unterkunft_viertel_lesen', 'teilnehmen', 'Suchtool: Viertel-Übersicht', 'Nur lesen. Viertel einer Stadt oder eines Suchauftrags: Name, Lage (lat/lon/radius_m), Charakter, Beschreibung, Lärm, Familien-Hinweis, Noten 0-10 (Nahversorgung, Gastronomie, Sehenswürdigkeiten, Grün, ÖPNV, Zentrumsnähe, Ruhe, Strand), Quellen, Status (vorschlag/bestaetigt/gestrichen) und mit Suchauftrag die Trefferzahl je Viertel. Dazu Filterkatalog für Viertel-Kriterien.', {
    stadt: z.string().optional(), suchauftrag_id: z.number().int().optional(),
  }, (a) => [h, a.stadt ?? null, a.suchauftrag_id ?? null], true)
  def('unterkunft_viertel_erstellen', 'daten', 'Suchtool: Viertel ermitteln', 'Nur auf Ansage des Nutzers. Ermittelt Viertel einer Stadt oder Insel ohne Suche: KI-Websuche (Sonnet 5.5, ZDR) plus OpenStreetMap-Merkmale, ca. 6 US-Cent je Stadt, Dauer 1-5 Minuten. erneut=true ermittelt neu (bestätigte Viertel bleiben). Danach unterkunft_viertel_lesen.', {
    stadt: z.string().min(2), erneut: z.boolean().optional(),
  }, (a) => [h, a.stadt, a.erneut ?? false], SCHREIBT, true)
  lese('unterkunft_zonen_lesen', 'teilnehmen', 'Suchtool: Zonen (Viertel) roh lesen', 'Nur lesen. Alle Zonen einer Stadt (auch gestrichene) mit Merkmalen und Status.', {
    stadt: z.string().optional(),
  }, (a) => [h, a.stadt ?? null], true)
  def('unterkunft_zone_entscheiden', 'daten', 'Suchtool: Viertel bestätigen/streichen/umbenennen', 'Nur auf Ansage des Nutzers. Setzt den Status eines Viertels (bestaetigt, gestrichen, vorschlag), optional neuer Name und Notiz. Gestrichene Viertel werden bei der Zuordnung nicht mehr genutzt.', {
    id: z.number().int(), status: z.enum(['bestaetigt', 'gestrichen', 'vorschlag']), name: z.string().max(80).optional(), notiz: z.string().max(500).optional(),
  }, (a) => [h, a.id, a.status, a.name ?? null, a.notiz ?? null], SCHREIBT, true)

  // ---------- Universal-Tür ----------
  server.registerTool('council_hilfe', {
    title: 'Council: alle Aktionen anzeigen',
    description: 'Nur lesen. Listet alle Aktionen, die du mit deinem Zugang ausführen darfst, mit Beschreibung und Parametern. Neue Funktionen erscheinen nur hier. Ausführen mit council_aktion.',
    inputSchema: { suche: z.string().optional().describe('Optional: Stichwort, um die Liste zu filtern') },
    annotations: NUR_LESEN,
  }, async ({ suche }: any) => {
    const s = (suche ?? '').toLowerCase()
    const liste = Object.entries(REG)
      .filter(([n, e]) => !s || n.includes(s) || e.title.toLowerCase().includes(s) || e.description.toLowerCase().includes(s))
      .map(([n, e]) => {
        let parameter: unknown = null
        try { parameter = (z as any).toJSONSchema(z.object(e.schema)) } catch { parameter = Object.keys(e.schema) }
        return { aktion: n, titel: e.title, beschreibung: e.description, nur_lesen: e.annotations === NUR_LESEN, recht: e.recht, parameter }
      })
    return antwort({ meine_rechte: rechte, anzahl: liste.length, aktionen: liste, hinweis: 'Ausführen mit council_aktion { aktion, daten }.' })
  })
  server.registerTool('council_aktion', {
    title: 'Council: Aktion ausführen',
    description: 'Führt eine Council-Aktion aus (Namen und Parameter aus council_hilfe). Schreibende Aktionen nur im Sinne des Nutzers bzw. auf seine Ansage. Die Datenbank prüft deine Rechte bei jeder Aktion.',
    inputSchema: {
      aktion: z.string().min(1).describe('Name der Aktion aus council_hilfe'),
      daten: z.record(z.string(), z.unknown()).optional().describe('Parameter der Aktion als Objekt'),
    },
    annotations: SCHREIBT,
  }, async ({ aktion, daten }: any) => {
    const e = REG[aktion]
    if (!e) return fehlerText(`Unbekannte oder nicht erlaubte Aktion "${aktion}". Mit council_hilfe die erlaubten Aktionen anzeigen.`)
    const p = z.object(e.schema).safeParse(daten ?? {})
    if (!p.success) return fehlerText(`Ungültige Parameter für ${aktion}: ` + p.error.issues.map((i: any) => `${i.path.join('.') || '(Objekt)'}: ${i.message}`).join('; '))
    return await ausfuehren(e, p.data)
  })
  return server
}

const app = new Hono().basePath('/council-mcp')

async function behandle(c: any) {
  const schluessel = c.req.param('schluessel') ?? ''
  if (schluessel.length < 32) return c.text('Nicht gefunden', 404)
  const hash = await sha256Hex(schluessel)
  let wer: { teilnehmer: string; rechte: string[] }
  try {
    wer = (await api('wer_bin_ich', [hash])) as any
  } catch (_e) {
    return c.text('Nicht gefunden', 404)
  }
  const server = baueServer(hash, wer.rechte)
  const transport = new WebStandardStreamableHTTPServerTransport()
  await server.connect(transport)
  return transport.handleRequest(c.req.raw)
}

app.all('/:schluessel', behandle)
app.all('/:schluessel/*', behandle)
app.all('*', (c) => c.text('Nicht gefunden', 404))

Deno.serve(app.fetch)
