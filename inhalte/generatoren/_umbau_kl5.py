"""Umbau der Lernkarten Klasse 5 auf das neue Muster (Achte Runde, Vorgabe 16.11., Paket U5).

Jeder Generator hat einen Abschnitt KARTEN: je Lernziel einstieg, woerter, bild, schritte ({text, bild}), fehler, fehler_bild, regel.
Die Felder werden ERST NACH dem Erzeugen der Aufgaben eingesetzt: Die Generatoren meiden die alten Beispieltexte (schritte)
beim Erzeugen der Aufgaben. So bleiben alle Aufgaben wörtlich gleich.

pruefe_karte() prüft die Regeln aus inhalte/README.md („Vorgabe seit 16.11.“) streng: Was tools/inhalt_pruefen.py nur als
Hinweis meldet, bricht hier ab. So bleibt kein Längenhinweis übrig.
"""
import json
import re

FELDER = {'einstieg', 'woerter', 'bild', 'schritte', 'fehler', 'fehler_bild', 'regel'}
PFLICHT = FELDER - {'fehler_bild'}
BILDER = ('zahlenstrahl', 'stellentafel', 'koordinaten', 'figur', 'saeulen', 'kreisdiagramm', 'tabelle', 'boxplot', 'baum', 'thermometer', 'bruchstreifen')
VERBOTEN = re.compile(r'\b(offensichtlich|einfach|trivial)\w*', re.I)
SMAX = 15  # Satzlänge Klasse 5/6

wz = lambda t: len(re.findall(r'\S+', re.sub(r'[⟦⟧]', '', str(t or ''))))
saetze = lambda t: [x for x in re.split(r'(?<=[.!?])\s+', re.sub(r'[⟦⟧]', '', str(t or ''))) if x.strip()]


def pruefe_bild(b, ok):
    if b.get('typ') == 'zahlenstrahl':
        lo, hi = b['start'], b['ende']
        werte = [p['wert'] for p in b.get('punkte') or []] + [v for g in b.get('boegen') or [] for v in (g['von'], g['bis'])]
        ber = b.get('bereich') or []
        werte += [v for r in (ber if isinstance(ber, list) else [ber]) for v in (r['von'], r['bis'])]
        ok(all(lo <= v <= hi for v in werte), f'Wert außerhalb {lo}..{hi}: {werte}')
        if b.get('pfeil') is not None:
            ok(0 <= b['pfeil'] <= b['abschnitte'], 'pfeil außerhalb')
    if b.get('typ') == 'thermometer' and b.get('stand') is not None:
        ok(b['start'] <= b['stand'] <= b['ende'], 'stand außerhalb')
    if b.get('typ') == 'bruchstreifen':
        ok(0 <= b.get('gefaerbt', 0) <= b['teile'], 'gefaerbt > teile')
    if b.get('typ') == 'figur':
        namen = set(b.get('punkte') or {})
        refs = [x for l in b.get('linien') or [] for x in l[:2]] + list(b.get('flaeche') or []) + [x for w in (b.get('winkel') or []) + (b.get('rechter_winkel') or []) for x in w[:3]]
        refs += [kr['m'] for kr in b.get('kreise') or []]
        ok(all(isinstance(r, list) or r in namen for r in refs), f'Figur: unbekannter Punkt {[r for r in refs if not isinstance(r, list) and r not in namen]}')
    if b.get('typ') == 'tabelle':
        ok(all(len(z) == len(b['kopf']) for z in b['zeilen']), 'Tabelle: Zeilenlänge ≠ Kopf')


def pruefe_karte(lz, k, fehler):
    def ok(bed, text):
        if not bed:
            fehler.append(f'{lz}: {text}')
    ok(set(k) <= FELDER, f'unbekannte Felder {set(k) - FELDER}')
    ok(PFLICHT <= set(k), f'fehlt {PFLICHT - set(k)}')
    ok(k['bild'].get('typ') in BILDER, 'Kartenbild ohne gültigen typ')
    ok(2 <= wz(k['einstieg']) and wz(k['einstieg']) <= 35, f'einstieg {wz(k["einstieg"])} Wörter')
    ok(2 <= len(saetze(k['einstieg'])) <= 3, f'einstieg {len(saetze(k["einstieg"]))} Sätze (2–3)')
    ok(len(k['einstieg']) >= 60, 'einstieg unter 60 Zeichen')
    ok(1 <= len(k['woerter']) <= 3, f'{len(k["woerter"])} Wörter (1–3)')
    sch = k['schritte']
    ok(2 <= len(sch) <= 5, f'{len(sch)} Schritte')
    texte = ' '.join([k['einstieg']] + [s['text'] for s in sch]).lower()
    for w in k['woerter']:
        ok(isinstance(w, list) and len(w) == 2 and all(isinstance(x, str) and x for x in w), f'woerter-Eintrag {w}')
        kern = w[0].split(' (')[0].strip().lower()
        ok(kern in texte, f'Wort „{w[0]}“ kommt in einstieg/schritten nicht vor')
    for i, s in enumerate(sch, 1):
        ok(isinstance(s, dict) and set(s) <= {'text', 'bild'} and s.get('text'), f'Schritt {i} Format')
        ok(wz(s['text']) <= 15, f'Schritt {i} hat {wz(s["text"])} Wörter: {s["text"]}')
        ok(s['text'].count('⟦') == s['text'].count('⟧') and s['text'].count('⟦') <= 2, f'Schritt {i} Markierung')
        if 'bild' in s:
            ok(isinstance(s['bild'], dict) and s['bild'].get('typ', k['bild']['typ']) in BILDER, f'Schritt {i} bild')
    ok(any('⟦' in s['text'] for s in sch), 'kein Ergebnis in ⟦…⟧')
    zustand = k['bild']  # Bildzustände wie in der App (lernSchrittBild): ergänzen oder bei anderem typ ersetzen
    for i, b in enumerate([s.get('bild') for s in sch] + [k.get('fehler_bild')], 1):
        if b:
            zustand = b if b.get('typ') and b['typ'] != zustand.get('typ') else {**zustand, **b}
        pruefe_bild(zustand, lambda bed, t, i=i: ok(bed, f'Bild {i}: {t}'))
    ok(wz(k['fehler']) <= 30, f'fehler {wz(k["fehler"])} Wörter')
    ok(wz(k['regel']) <= 25, f'regel {wz(k["regel"])} Wörter')
    ok(wz(saetze(k['regel'])[0]) <= 12, f'Kurz gesagt {wz(saetze(k["regel"])[0])} Wörter: {saetze(k["regel"])[0]}')
    for f in ('einstieg', 'fehler', 'regel'):
        for sa in saetze(k[f]):
            ok(wz(sa) <= SMAX, f'Satz in {f} hat {wz(sa)} Wörter: {sa}')
        ok(k[f].count('⟦') == k[f].count('⟧') and k[f].count('⟦') <= 2, f'Markierung in {f}')
    for f in ['einstieg'] + [s['text'] for s in sch]:
        ok(not VERBOTEN.search(k.get(f, f)), f'verbotenes Wort in {f[:40]}')
    ok(not re.search('[¼½¾⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞]', json.dumps(k, ensure_ascii=False)), 'Unicode-Bruchzeichen')


def umbau(datei, karten, offen=()):
    """Setzt die neuen Felder in die Lernkarten von `datei` (nach dem Erzeugen der Aufgaben)."""
    etappen = datei['inhalt']['etappen']
    namen = [e['lernziel'] for e in etappen]
    assert sorted(karten) == sorted(namen), ('KARTEN passt nicht zu den Lernkarten', sorted(set(namen) ^ set(karten)))
    fehler = []
    for e in etappen:  # bild 'BEHALTEN': das bisherige Kartenbild bleibt (z. B. vom Generator berechnete Figuren)
        if karten[e['lernziel']].get('bild') == 'BEHALTEN':
            karten[e['lernziel']]['bild'] = e['bild']
    for e in etappen:
        pruefe_karte(e['lernziel'], karten[e['lernziel']], fehler)
    assert not fehler, 'Regeln verletzt:\n' + '\n'.join(fehler)
    for e in etappen:
        k = karten[e['lernziel']]
        for alt in ('probe', 'fehler_bild', 'bild', 'einstieg', 'woerter'):
            e.pop(alt, None)
        e.update(k)
    if offen:
        datei['offen'] = list(datei.get('offen') or []) + [o for o in offen if o not in (datei.get('offen') or [])]
    return datei


def mit_umbau(baue, karten, offen=()):
    """Für Generatoren mit baue(...) aus _nachbau.py (z. B. gleichungen.einfach): baue erzeugt die Aufgaben (mit den ALTEN
    Beispieltexten) und schreibt die Datei; danach werden die Karten umgebaut und die Datei neu geschrieben."""
    from _nachbau import THEMEN

    def baue_umbau(meta, *args, **kwargs):
        d = baue(meta, *args, **kwargs)
        umbau(d, karten, offen)
        (THEMEN / f"{meta['thema_schluessel']}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        return d
    return baue_umbau
