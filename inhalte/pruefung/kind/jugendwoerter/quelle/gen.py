import json
Q = {
 'Z26': ('ZDFheute: Jugendwort 2026 – die Top Ten und was sie bedeuten', 'https://www.zdfheute.de/panorama/jugendwort-2026-langenscheidt-100.html'),
 'F26': ('familie.de: Jugendwort des Jahres 2026 „Ragebait“', 'https://www.familie.de/schulkind/jugendwort-des-jahres-2026-endlich-ein-begriff-den-jugendliche-wirklich-verwenden--01H7FQ1559Y3HGP8SMJWFP9NDZ'),
 'D26': ('drohnen.de: Jugendwort 2026 – warum „Mehrzweckeier“ ausgeschlossen wurde', 'https://www.drohnen.de/?p=87349'),
 'S25': ('SRF: Top 10 Jugendwörter 2025', 'https://www.srf.ch/kultur/gesellschaft-religion/top-10-jugendwoerter-2025-wissen-sie-was-tuff-oder-sybau-bedeutet'),
 'W24': ('web.de: Top 10 zum Jugendwort 2024', 'https://web.de/magazine/unterhaltung/tv-shows/tagesschau-sprecherin-susanne-daubner-hoert-jugendwort-jahres-39949050'),
 'Q24': ('QuillBot: Jugendwort 2024 – Top 3 und Top 10', 'https://quillbot.com/de/blog/jugendsprache/jugendwort-2024/'),
 'Z24': ('ZDFheute: Was „Talahon“ und „Akh“ bedeuten', 'https://www.zdfheute.de/panorama/jugendwort-des-jahres-2024-100.html'),
 'QY': ('QuillBot: Yurr – Bedeutung', 'https://quillbot.com/de/blog/jugendsprache/yurr/'),
 'U23': ('Uni Zürich (Pressespiegel): Jugendwort 2023 – die Top 10', 'https://www.ds.uzh.ch/apps/_files/uploads/presse/872.pdf'),
 'Q23': ('QuillBot: Jugendwort 2023', 'https://quillbot.com/de/blog/jugendsprache/jugendwort-2023/'),
 'N22': ('nau.ch: Jugendwort 2022 – Top 10', 'https://www.nau.ch/news/europa/jugendwort-des-jahres-2022-bodenlos-smash-wild-und-gommemode-66239800'),
 'M22': ('mein-mmo: Top 10 Jugendwort 2022 mit Bedeutungen', 'https://mein-mmo.de/journalist-sich-mit-falscher-verwendung-des-jugendwort-des-jahres-2022/'),
 'T22': ('Tagesspiegel: Jugendwort 2022 – die drei Kandidaten', 'https://www.tagesspiegel.de/gesellschaft/jugendwort-des-jahres-2022-das-sind-die-drei-kandidaten-8662300.html'),
 'Q22': ('QuillBot: Jugendwort 2022', 'https://quillbot.com/de/blog/jugendsprache/jugendwort-2022/'),
 'Q21': ('QuillBot: Jugendwort 2021', 'https://quillbot.com/de/blog/jugendsprache/jugendwort-2021/'),
 'M21': ('mein-mmo: Jugendwort 2021 – Top 10', 'https://mein-mmo.de/was-bedeutet-sus-jugendwort-2021/'),
 'SY': ('Stuttgarter Zeitung: Sheesh – Bedeutung', 'https://www.stuttgarter-zeitung.de/wissen/sheesh-bedeutung-und-verwendung-mhsd-79028244.html'),
 'QL': ('QuillBot: Jugendwörter der letzten Jahre (alle Gewinner seit 2008)', 'https://quillbot.com/de/blog/jugendsprache/jugendwoerter/'),
 'QC': ('QuillBot: Cüs – Bedeutung', 'https://quillbot.com/de/blog/jugendsprache/cues/'),
 'GC': ('GIGA: Çüş – Bedeutung (Tschüsch)', 'https://www.giga.de/artikel/cues-was-heisst-das-bedeutung-uebersetzung-tschuesch/'),
 'DC': ('desired: Çüş – richtige Verwendung', 'https://www.desired.de/artikel/cues-alles-zur-richtigen-verwendung-des-trendwortes-gibt-s-hier--wpvgjf2hxf'),
 'NW': ('netzwelt: Çüş, AMK, Alman', 'https://www.netzwelt.de/abkuerzung/177769-bedeutet-ue-bedeutung-verwendung.html'),
 'GH': ('GIGA: Netz- und Gamingbegriffe (u. a. „Hawk Tuah“)', 'https://www.giga.de/themen/netz-und-gamingbegriffe/?page=6'),
 'PC': ('PC-Welt: Jugendwörter (u. a. Delulu)', 'https://www.pcwelt.de/?p=2692026'),
}
B = ['beide']
W = []
def w(id, wort, sw, bed, ton, jahr, q, einsatz, staerke, alter, verfall, neben, grund=None, **x):
    d = {'id': id, 'wort': wort, 'schreibweisen': sw, 'bedeutung': bed, 'tonlage': ton, 'jahr': jahr}
    if q:
        d['quelle'] = {'titel': Q[q][0], 'link': Q[q][1]}; d['beleg'] = 'Quelle'
    else:
        d['quelle'] = None; d['beleg'] = 'Annahme – kein Listenwort, Bedeutung nicht mit Quelle geprüft'
    if einsatz == 'ungeeignet':
        d['einsatz'] = 'ungeeignet'; d['grund'] = grund
    else:
        d['einsatz'] = einsatz; d['staerke'] = staerke
    d['nebenbedeutung'] = neben; d['verfall'] = verfall
    d.update(x); W.append(d)

# ---------- geeignet ----------
w('cues', 'Çüş', ['Çüş', 'Cüs', 'Cüüüs'], 'Ausruf des Staunens: „boah“, „krass“, „oha“.', 'staunen', None, 'QC', ['staunen'], 3, B, '2028-05',
  'Türkisch ursprünglich Halte-Ruf für Esel und Pferde; kann auch „mach mal halblang“ oder „igitt“ heißen (desired). Nur nach klar gutem Ergebnis, nie bei Fehlern.', gesprochen='Tschüsch', quelle2={'titel': Q['DC'][0], 'link': Q['DC'][1]})
w('digga', 'Digga', ['Digga', 'Diggah', 'Digger'], 'Kumpel, Bro; Anrede für jeden, auch Ausruf.', 'locker', 2021, 'Z26', ['anrede', 'lob_klein'], 2, B, '2028-11',
  'Seit 2021 jedes Jahr in den Top 10. Festgelegte Anrede der App für beide Kinder (Entscheidung des Nutzers 23.11.2026). Nie in Fehler-Sprüchen allein als Vorwurf, nur freundlich („Schere, Digga.“).')
w('peak', 'Peak', ['Peak', 'PEAK'], 'Das Beste vom Besten, absoluter Höhepunkt.', 'lob', 2026, 'Z26', ['lob_gross'], 3, B, '2027-11',
  'Wird auch ironisch gesteigert („peak cringe“). Nie mit einem negativen Wort kombinieren, nur bei wirklich bestem Ergebnis.')
w('gute_kaese', 'Gute Käse', ['Gute Käse', 'Gute Käses'], 'Etwas ist richtig gut oder stabil; Lob oder Zustimmung, ohne wörtlichen Sinn.', 'lob', 2026, 'Z26', ['lob_klein'], 1, B, '2027-11',
  'Absichtlich schiefe Grammatik – nie „verbessern“ in „Guter Käse“.')
w('sueper', 'Süper', ['Süper', 'Süpeeer'], '„Super“ auf Türkisch; bekannt durch das Video eines Ultramarathon-Läufers.', 'lob', 2026, 'Z26', ['lob_klein', 'lob_gross'], 2, B, '2027-11', 'Keine bekannt.')
w('das_crazy', 'Das crazy', ['Das crazy', 'Das crazy!'], 'Antwort, wenn einem die Worte fehlen – Staunen, aber auch gelangweiltes „aha, okay“.', 'staunen', 2025, 'S25', ['staunen'], 2, B, '2027-05',
  'Kann Desinteresse ausdrücken. Darum nur mit Ausrufezeichen und nur bei Staunens-Anlässen (Knobel richtig, Expedition), nie bei kleinem Lob.')
w('schere', 'Schere', ['Schere'], '„Mein Fehler!“ – digitaler Handschlag aus der Gaming-Szene, um einen dummen Fehler zuzugeben.', 'locker', 2024, 'Z26', ['fehler_mild'], 1, B, '2027-11',
  'Wörtlich das Werkzeug. Ist ein Eingeständnis dessen, der spricht: die App spricht es als Stimme des Kindes („Schere – passiert“), nie als Vorwurf („deine Schere“). Für 11 beim ersten Mal die Bedeutung zeigen.')
w('tuff', 'tuff', ['tuff', 'Tuff', 'tough'], 'Krass, cool – man ist beeindruckt.', 'lob', 2025, 'S25', ['lob_gross'], 2, ['14'], '2027-05',
  'Englisch „tough“ = hart, schwierig – passt deshalb doppelt beim Sturmflug.')
w('lowkey', 'lowkey', ['lowkey', 'low key'], '„Ein bisschen“, unauffällig, ohne Drama.', 'locker', 2025, 'S25', ['lob_klein'], 1, ['14'], '2027-05',
  'Auch „insgeheim“. Nur als Zusatz vor einem Lobwort („lowkey stark“), nie allein.')
w('rede', 'Rede!', ['Rede!', 'Rede'], 'Sinngemäß „Lauter!“ – starke Zustimmung zu dem, was gerade gesagt wurde.', 'lob', 2025, 'S25', ['lob_klein'], 1, ['14'], '2027-05',
  'Wörtlich „Ansprache“. Braucht etwas, dem man zustimmt – darum zurzeit in keinem Spruch; Reserve, falls das Kind eigene Lösungswege eintippt.')
w('aura', 'Aura', ['Aura', '+1000 Aura', 'Aura +1000'], 'Ausstrahlung, Charisma, Status; oft scherzhaft mit Punkten („+1000 Aura“).', 'lob', 2024, 'Q24', ['lob_gross'], 3, B, '2027-05',
  'Esoterischer Ursprung; Spott-Form „minus Aura“ / „Aura-Verlust“ – nur die Plus-Form verwenden.')
w('yurr', 'Yurr', ['Yurr', 'Yurrr'], 'Lockere Begrüßung wie „yo“, „hey“; auch Zustimmung.', 'locker', 2024, 'QY', ['anrede'], 1, ['14'], '2027-05', 'Keine bekannt; klingt schnell veraltet.')
w('sheesh', 'Sheesh', ['Sheesh', 'Sheeesh'], 'Ausruf des Erstaunens: „wow“, „oha“.', 'staunen', 2021, 'Q21', ['staunen'], 3, B, '2027-05',
  'Kann auch Erschrecken oder Ärger ausdrücken (Stuttgarter Zeitung). Nur nach klar gutem Ergebnis.', quelle2={'titel': Q['SY'][0], 'link': Q['SY'][1]})
w('wild', 'wild', ['wild', 'wyld'], 'Krass, beeindruckend.', 'staunen', 2021, 'N22', ['staunen'], 2, ['14'], '2027-05', 'Auch „unkontrolliert“ – nur staunend verwenden.')
w('slay', 'Slay', ['Slay', 'slay'], 'Ausdruck der Zustimmung: richtig stark gemacht.', 'lob', 2022, 'U23', ['lob_gross'], 2, ['14'], '2027-05', 'Englisch wörtlich „töten, erschlagen“ – deshalb nur für 14.')
w('macher', 'Macher', ['Macher', 'Macher-Modus'], 'Jemand, der Dinge anpackt und umsetzt, ohne zu zögern.', 'lob', 2022, 'T22', ['lob_gross'], 2, B, '2027-11',
  'Männliche Form. Die App nutzt nur die neutrale Form „Macher-Modus“.')
w('gommemode', 'Gommemode', ['Gommemode', 'Gomme-Mode'], 'Unendlich stark, unbesiegbar (nach einem Gaming-YouTuber).', 'lob', 2022, 'N22', ['lob_gross'], 3, B, '2027-05',
  'Bezug auf eine reale Person (YouTuber). Älteres Wort – auf Probe, bei der Halbjahresprüfung als Erstes streichen.', probe=True)
w('siu', 'SIU', ['SIU', 'SIUUU'], 'Jubelruf, wenn etwas unfassbar Gutes passiert (Torjubel von Cristiano Ronaldo).', 'lob', 2022, 'M22', ['lob_gross'], 3, ['11'], '2027-05',
  'Bezug auf einen Fußballer – nicht jedes Kind mag ihn; darum gut ausblendbar.')
w('auf_lock', 'Auf Lock', ['Auf Lock', 'auf lock'], 'Abkürzung von „auf locker“: die Dinge entspannt angehen.', 'locker', 2023, 'U23', ['fehler_mild'], 1, B, '2027-05', 'Keine bekannt.')
w('akkurat', 'Akkurat', ['Akkurat', 'akkurat'], 'Ausdruck der Zustimmung: genau so.', 'lob', 2021, 'Q21', ['lob_klein'], 1, B, '2027-05', 'Im Standarddeutsch „genau, sorgfältig“ – passt beim Rechnen doppelt.')
w('laeuft', 'Läuft bei dir', ['Läuft bei dir', 'Läuft'], 'Du hast Erfolg, es klappt.', 'lob', 2014, 'QL', ['lob_klein'], 1, ['11'], '2027-05', 'Kann ironisch gemeint sein; für 14 wirkt es alt.')
w('ohne_witz', 'Ohne Witz', ['Ohne Witz', 'ohne Witz'], 'Ernsthaft, wirklich (staunend).', 'staunen', None, None, ['staunen'], 2, B, '2028-05', 'Keine bekannt.')
w('w', 'W', ['W', 'Big W'], 'Abkürzung für „Win“: ein Sieg, ein Erfolg.', 'lob', None, None, ['lob_klein'], 1, ['14'], '2027-05', 'Gegenstück „L“ (Niederlage) wird zum Spotten benutzt – „L“ nie verwenden.')
w('goat', 'GOAT', ['GOAT', 'G.O.A.T.'], '„Greatest of all time“ – der/die Beste überhaupt.', 'lob', None, None, ['lob_gross'], 3, B, '2027-11', 'Englisch „Ziege“ – für 11 mit kleiner Ziege witzig.')
w('locked_in', 'Locked in', ['Locked in', 'locked in'], 'Voll konzentriert, im Tunnel.', 'lob', None, None, ['lob_gross'], 2, ['14'], '2027-05', 'Wörtlich „eingesperrt“; nur in der Serie verwenden.')
w('nice', 'Nice', ['Nice', 'nice'], 'Schön, gut gemacht.', 'lob', None, None, ['lob_klein'], 1, B, '2028-11', 'Keine; fast Standardsprache.')
w('krass', 'krass', ['krass', 'Krass'], 'Beeindruckend, heftig.', 'staunen', None, None, ['staunen'], 2, B, '2028-11', 'Auch negativ („krass schlecht“) – nur positiv.')
w('stabil', 'stabil', ['stabil', 'Stabil'], 'Gut, verlässlich, beeindruckend.', 'lob', None, None, ['lob_klein'], 1, B, '2027-11', 'Wörtlich „fest“ – passt zu „sitzt“ bei Wiederholungen.')
w('safe', 'safe', ['safe', 'Safe'], 'Sicher, auf jeden Fall.', 'lob', None, None, ['lob_klein'], 1, ['14'], '2027-05', 'Englisch „sicher“ – keine schlechte Nebenbedeutung.')
w('ehrenmann', 'Ehrenmann / Ehrenfrau', ['Ehrenmann', 'Ehrenfrau'], 'Jemand, der sich anständig und vorbildlich verhält.', 'lob', 2018, 'QL', ['lob_gross'], 2, B, '2027-05',
  'Braucht die passende Form zum Kind. Zurzeit in keinem Spruch (keine Formwahl geplant) – Reserve.')

# ---------- ungeeignet ----------
u = lambda id, wort, bed, jahr, q, grund, neben='—': w(id, wort, [wort], bed, 'ungeeignet', jahr, q, 'ungeeignet', None, None, '—', neben, grund)
u('bro', 'Bro', 'Anrede für einen Freund.', 2022, 'N22', 'Nicht nötig: Anrede der App ist festgelegt auf „Digga“.')
u('du_bist_gut_genug', 'Du bist gut genug', 'Refrain eines viralen Songs (Kitschkrieg mit Shirin David), viel parodiert.', 2026, 'Z26', 'Meme-Ironie: wirkt nach einem Fehler schnell spöttisch.')
u('ragebait', 'Ragebait', 'Inhalte, die absichtlich Wut provozieren, um Reichweite zu bekommen. Jugendwort 2026.', 2026, 'Z26', 'Wut und Provokation – laut Auftrag ausgeschlossen.')
u('crashout', 'Crashout', 'Die Fassung verlieren, extrem emotional reagieren.', 2026, 'Z26', 'Wut und Kontrollverlust – laut Auftrag ausgeschlossen.')
u('goonen', 'goonen', 'Slang für Selbstbefriedigung.', 2025, 'S25', 'Sexuell – ausgeschlossen.')
u('sybau', 'sybau', 'Abkürzung für eine englische Beleidigung („halt die Klappe“).', 2025, 'S25', 'Beleidigend – ausgeschlossen.')
u('67', '67', 'Insider ohne feste Bedeutung („six seven“), oft mit Handgeste.', 2026, 'Z26', 'Kein Sinn, den die App tragen kann; nervt schnell und verfällt schnell. Bei Ergebnis 67 % NICHT als Gag einsetzen (Annahme: wirkt bemüht).')
u('macker', 'Macker', 'Freund, Kumpel oder Schwarm, oft ironisch.', 2026, 'Z26', 'Nebenbedeutung „Schwarm“ und älteres „Macho“ – passt nicht als Lob vom Lernprogramm.')
u('mehrzweckeier', 'Mehrzweckeier', 'Von der Langenscheidt-Jury 2026 ausgeschlossen; Bedeutung von mir nicht geprüft.', 2026, 'D26', 'Ausgeschlossen von der Jury, Bedeutung unklar – nicht prüfbar, also nicht verwenden.')
u('checkst_du', 'Checkst du', 'Nachfrage „Verstehst du?“, ob jemand wirklich zugehört hat.', 2025, 'S25', 'Klingt bei einer Rückmeldung wie „Hast du’s jetzt endlich kapiert?“ – belehrend.')
u('tot', 'tot', 'Etwas ist daneben, lahm, peinlich.', 2025, 'S25', 'Abwertend; Wort „tot“ in einer Kinder-App unpassend.')
u('talahon', 'Talahon', 'Bezeichnung für junge Männer mit bestimmtem Auftreten; oft abwertend.', 2024, 'Z24', 'Abwertend und klischeehaft gegenüber einer Gruppe – ausgeschlossen.')
u('akh', 'Akh', 'Arabisch „Bruder“, Anrede für Freunde.', 2024, 'Z24', 'Gruppen- und herkunftsbezogene Anrede; vom Lernprogramm gesprochen wirkt es aufgesetzt.')
u('hoelle_nein', 'Hölle nein', 'Starke Ablehnung („hell no“).', 2024, 'Q24', 'Ablehnung – es gibt keinen Anlass in der App, bei dem die App „nein“ ruft.')
u('nein_pascal', 'Nein Pascal, ich denke nicht', 'Ablehnung, Meme.', 2024, 'W24', 'Ablehnung mit Namensbezug – Kinder mit diesem Namen werden gehänselt.')
u('pyrotechnik', 'Pyrotechnik ist doch kein Verbrechen', 'Fan-Spruch aus Fußballstadien.', 2024, 'W24', 'Bezug zu verbotenem Feuerwerk im Stadion – kein Anlass, falsches Signal.')
u('yolo', 'Yolo', '„You only live once“ – Chancen nutzen, Risiken eingehen.', 2012, 'U23', 'Risiko-Botschaft passt nicht zum sorgfältigen Rechnen; zudem alt.')
u('smash', 'Smash', 'Man findet jemanden attraktiv und würde gern etwas mit ihm anfangen.', 2022, 'Q22', 'Sexuelle Bedeutung – ausgeschlossen.')
u('bodenlos', 'bodenlos', 'Schlecht, mies, unglaublich.', 2022, 'T22', 'Abwertend.')
u('sus', 'sus', 'Verdächtig, suspekt.', 2021, 'Q21', 'Misstrauen/Vorwurf – bei Fehlern verletzend („deine Antwort ist sus“).')
u('cringe', 'cringe', 'Extrem peinlich, Fremdscham.', 2021, 'Q21', 'Als Rückmeldung beschämend.')
u('goofy', 'goofy', 'Albern, tollpatschig, dämlich.', 2023, 'Q23', 'Abwertend über eine Person – bei Fehlern verletzend.')
u('npc', 'NPC', 'Person, die nur passiv am Geschehen teilnimmt.', 2023, 'QL', 'Abwertend.')
u('side_eye', 'Side eye', 'Seitenblick, drückt Verachtung oder Missbilligung aus.', 2023, 'Q23', 'Verachtung.')
u('rizz', 'Rizz', 'Charisma, Charme – meist beim Flirten.', 2023, 'QL', 'Flirt-Bezug.')
u('lost', 'lost', 'Ahnungslos, nicht mitkommen. Jugendwort 2020.', 2020, 'QL', 'Bei Fehlern abwertend („du bist lost“).')
u('geringverdiener', 'Geringverdiener', 'Spott über jemanden, der wenig hat oder kann.', 2021, 'M21', 'Abwertend (Einkommen).')
u('mittwoch', 'Mittwoch (meine Kerle)', 'Frosch-Meme zum Wochentag.', 2021, 'M21', 'Meme ohne Lern-Anlass; veraltet.')
u('papatastisch', 'papatastisch', 'Kaum bekanntes Kunstwort aus der Top 10 2021.', 2021, 'M21', 'Kaum bekannt, Bedeutung nicht geprüft.')
u('same', 'same', 'Geht mir genauso.', 2021, 'M21', 'Kein Anlass in der App.')
u('kerl_in', 'Kerl*in', 'Anrede für einen Freund, meist nur in männlicher Form.', 2023, 'U23', 'Kaum noch gebraucht; Genderstern wirkt bemüht.')
u('i_bims', 'I bims', '„Ich bin’s“ in verdrehter Schreibweise. Jugendwort 2017.', 2017, 'QL', 'Veraltet – wirkt peinlich.')
u('fly', 'fly', 'Abgehoben, besonders. Jugendwort 2016.', 2016, 'QL', 'Veraltet.')
u('delulu', 'delulu', 'Von „delusional“: wahnhaft, realitätsfern.', None, 'PC', 'Abwertend.')
u('amk', 'AMK', 'Vulgäre türkische Abkürzung.', None, 'NW', 'Vulgär und beleidigend – ausgeschlossen.')
u('alman', 'Alman', 'Bezeichnung für Deutsche, oft spöttisch.', None, 'NW', 'Spott über eine Gruppe.')
u('hawk_tuah', 'Hawk Tuah', 'Anzügliches Meme.', None, 'GH', 'Sexuell – ausgeschlossen.')
u('sigma', 'Sigma', 'Meme-Wort für den „einsamen, überlegenen“ Mann (Alpha/Sigma).', None, None, 'Männlichkeits-Kult-Meme; Nebenbedeutung problematisch.')
u('skibidi', 'Skibidi', 'Meme ohne feste Bedeutung (Toiletten-Videos).', None, None, 'Kein Sinn, wirkt kindisch bzw. bemüht; verfällt schnell.')
u('brainrot', 'Brainrot', 'Hirnverrottung durch sinnlose Inhalte.', None, None, 'Abwertend.')
u('cooked', 'cooked', '„Erledigt“, keine Chance mehr.', None, None, 'Entmutigend – bei Fehlern das Gegenteil von dem, was die App will.')
u('l', 'L', 'Niederlage, Verlust; wird zum Spotten benutzt.', None, None, 'Spott – nie bei Fehlern.')
u('vallah', 'Vallah / Wallah', 'Arabisch „bei Gott“, Beteuerung.', None, None, 'Religiöse Formel – nicht vom Lernprogramm.')
u('mashallah', 'Mashallah', 'Arabisch, Ausdruck der Bewunderung mit religiösem Bezug.', None, None, 'Religiöse Formel – nicht vom Lernprogramm.')

# ---------- Sprüche ----------
S = []
def s(id, anlass, staerke, sticker, woerter, **x):
    d = {'id': id, 'anlass': anlass, 'staerke': staerke, 'sticker': sticker, 'woerter': woerter}
    d.update(x); S.append(d)
L = [
 ('landung_direkt', 3, [('PEAK', 'peak'), ('Das war Peak.', 'peak'), ('GOAT', 'goat'), ('+1000 Aura', 'aura'), ('SIUUU!', 'siu'), ('Çüş – auf Anhieb!', 'cues')]),
 ('landung_sauber', 2, [('Tuff.', 'tuff'), ('Süper!', 'sueper'), ('Slay.', 'slay'), ('Gute Käse', 'gute_kaese'), ('Sauber, Digga.', 'digga'), ('Nice gelandet!', 'nice')]),
 ('landung_leicht', 1, [('Lowkey stark.', 'lowkey'), ('Akkurat.', 'akkurat'), ('W', 'w'), ('Läuft, Digga.', 'laeuft')]),
 ('landung_sturm', 2, [('Tuff durchgezogen.', 'tuff'), ('Macher-Modus', 'macher'), ('Locked in.', 'locked_in'), ('Stabil durchgehalten.', 'stabil')]),
 ('knobel_richtig', 3, [('Çüş!', 'cues'), ('Sheesh!', 'sheesh'), ('Das crazy!', 'das_crazy'), ('Wild.', 'wild'), ('Ohne Witz – geknackt.', 'ohne_witz')]),
 ('serie_5', 2, [('5 in Folge – locked in', 'locked_in'), ('5 am Stück, Digga.', 'digga')]),
 ('serie_10', 3, [('Gommemode', 'gommemode'), ('Krass – 10 am Stück', 'krass')]),
 ('wiederholung', 1, [('Hält stabil.', 'stabil'), ('Safe gekonnt.', 'safe'), ('Noch drin. Nice.', 'nice'), ('Süper – noch gewusst.', 'sueper')]),
 ('flug_geschafft', 3, [('Peak-Flug', 'peak'), ('GOAT-Flug', 'goat'), ('SIUUU!', 'siu'), ('Aura +1000', 'aura')]),
 ('expedition_geschafft', 2, [('Çüş, Expedition!', 'cues'), ('Tuff, Polarprofi.', 'tuff')]),
 ('expedition_fehlerfrei', 3, [('GOAT der Antarktis', 'goat'), ('Peak. Null Fehler.', 'peak')]),
 ('nachbessern', 2, [('Macher-Modus: repariert', 'macher'), ('Süper repariert!', 'sueper'), ('Stabil zurück.', 'stabil'), ('Wieder drin – nice.', 'nice')]),
 ('fehler', 1, [('Schere.', 'schere'), ('Kleine Schere – passiert.', 'schere'), ('Auf Lock. Nächste.', 'auf_lock'), ('Schere, Digga. Nächste.', 'schere')]),
 ('anrede', 1, [('Yo Digga!', 'digga'), ('Yurr, Digga!', 'yurr'), ('Digga, los geht’s.', 'digga')]),
]
n = 0
for anlass, st, liste in L:
    for t, wid in liste:
        n += 1; ws = [wid] + (['digga'] if 'Digga' in t and wid != 'digga' else [])
        s('J%02d' % n, anlass, st, t, ws, **({'zeile': '{Ansage der Abflugtafel, unverändert}'} if anlass == 'anrede' else {}))
ids = {x['id'] for x in W}
for x in S:
    for i in x['woerter']:
        assert i in ids and W[[y['id'] for y in W].index(i)]['einsatz'] != 'ungeeignet', (x, i)

ANL = {
 'landung_direkt': 'Landung einer Etappe – Direktflug (kein Fehler, kein Tipp)',
 'landung_sauber': 'Landung – Saubere Landung ohne Tipp',
 'landung_leicht': 'Landung – Saubere Landung mit Tipp oder „Wieder gelandet“',
 'landung_sturm': 'Landung – Sturmflug gemeistert (Ausdauer)',
 'knobel_richtig': 'Knobel-Bordkarte im ersten Versuch richtig',
 'serie_5': 'Serie: 5 Bordkarten in Folge richtig',
 'serie_10': 'Serie: 10 Bordkarten in Folge richtig',
 'wiederholung': 'Wiederholung bestanden',
 'flug_geschafft': 'Flug geschafft',
 'expedition_geschafft': 'Expedition geschafft',
 'expedition_fehlerfrei': 'Expedition fehlerfrei',
 'nachbessern': '„Nachbessern“ geschafft (wieder offene Stadt wieder abgelegt)',
 'fehler': 'Fehler-Rückmeldung (falsche Antwort)',
 'anrede': 'Begrüßung auf der Abflugtafel (Anrede Digga)',
}
out = {
 'stand': '2026-11-23', 'naechste_pruefung': '2027-05-15', 'pruefrhythmus': 'halbjährlich (Mai, November, nach der Langenscheidt-Wahl)',
 'hinweis': 'Vorgabe JW – Daten für die App. Wörter mit verfall < heute oder einsatz „ungeeignet“ werden nie gezogen. Keine Einstellungen, keine Altersunterscheidung.',
 'anlaesse': ANL,
 'regeln': {'erfolg': 'jede Geschafft-Ansicht bekommt genau einen Sticker', 'fehler': 'Sticker beim 1., 3., 5. … Fehler eines Lerntags; nie ab dem 2. Fehler in Folge', 'anrede': 'einmal je Lerntag auf der Abflugtafel, immer „Digga“',
            'nie_wiederholen_letzte': 1, 'wort_sperre_letzte_sticker': 4, 'einstellungen': 'keine – festgelegt (Nutzer, 23.11.2026)'},
 'woerter': W, 'sprueche': S,
}
import sys
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
g = [x for x in W if x['einsatz'] != 'ungeeignet']
print(len(W), 'Wörter,', len(g), 'geeignet,', len(S), 'Sprüche')
