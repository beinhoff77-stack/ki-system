# Reise-Aufbau – Vorschlag (Stand 22.11.2026)

**Nur Vorschlag.** Kein App-Code, nichts in der Datenbank geändert. Datenbank nur lesend genutzt (`schule.kontinent`, `block`, `block_thema`, `thema`, `einheit.inhalt.etappen`; `route`, `flug_erstabschluss`, `karte_stand`, `testsitzung` nur gezählt je Ort – ohne Namen). Grundlage: die acht Festlegungen in `inhalte/AUFTRAEGE.md` („Vorarbeit ‚Reise-Aufbau‘ (22.11.)“).

Dateien:
- `aufbau-vorschlag.json` – maschinenlesbar (je Flug: `thema_id`, `einheit_id`, Land, Etappe-Nr. → Stadt; Expeditionen → Station; Ergebnis der Selbstprüfung)
- `aufbau_daten.py` – die Zuordnung selbst (eine Stelle zum Ändern)
- `aufbau_pruefen.py` – baut die JSON und prüft (`python3 -I inhalte/reise/aufbau_pruefen.py`, Ortsprüfung braucht `pip install geonamescache`)
- `db_stand.json` – gelesener DB-Stand (Thema → Einheit, Anzahl Etappen)

## Neuer Aufbau

| Ebene | Kinderseite | Eltern/Lehrer (Festlegung 8) |
|---|---|---|
| Kontinent | Reise-Kontinent | Themengebiet |
| Flug | ein Land | Thema |
| Etappe | eine Stadt im Land | Etappe |
| Aufgabe | Highlight der Stadt (ohne Namen) | Aufgabe |

Die Ebene „Ort“ (heute `schule.block` mit Stadt) entfällt. Länder je Kontinent in der Reihenfolge der Klassen (Gymnasium Bayern; ohne Gym-Klasse: Realschule, dann IB), Städte je Land als fahrbare Strecke.

## Ergebnis der Selbstprüfung (Skript)

| Prüfung | Ergebnis |
|---|---|
| Flüge (freigegebene Einheiten) | 87 von 87 zugeordnet |
| Jedes Land/Region einmal | 87 verschiedene ✔ |
| Jede Stadt einmal | 606 verschiedene ✔ |
| Städte = Etappen je Flug | bei allen 87 ✔ (Summe 606) |
| Stadt liegt im Land | 606/606 in GeoNames im richtigen Land gefunden ✔ (Australien/Hawaii zusätzlich im richtigen Bundesstaat, Neuseeland auf der richtigen Insel) |
| Heutige Städte begonnener Orte bleiben | 9/9 ✔ |
| Expeditionen | 21 Expeditionen, 21 verschiedene Stationen ✔ |

Grenzen der Prüfung: GeoNames prüft „es gibt einen Ort dieses Namens in diesem Land“, nicht „es ist der gemeinte Ort“. Die Reihenfolge wurde per Luftlinie geprüft; 13 Teilstrecken sind länger als 700 km (alle per Straße verbunden, aber lange Fahrten: Kanada, USA, Kasachstan, China, Argentinien, Brasilien – große Länder). Die Antarktis-Stationen sind nicht per Skript geprüft (Wissen, Stand Juni 2026).

## Begonnene Orte – was bleibt (Festlegung 6)

Gezählt aus `route` (fertig), `flug_erstabschluss`, `karte_stand`, `testsitzung`; keine Kinderdaten übernommen.

| heutiger Ort | Flug, der das Land behält | Land | Grund |
|---|---|---|---|
| Rom | Natürliche Zahlen | Italien | zuerst abgeschlossen |
| Samarkand | Potenzgesetze | Usbekistan | zuerst abgeschlossen |
| Paris | Potenzen und negative Exponenten | Frankreich | **Annahme:** kein Erstabschluss gespeichert, nur dieses Thema hat Übungsstand |
| Mumbai | Bruchterme | Indien | **Annahme:** kein Erstabschluss; Bruchterme und Bruchgleichungen haben Übungsstand, Bruchterme kommt im Lehrplan zuerst |
| Quito | Flächen von Parallelogramm, Dreieck, Trapez | Ecuador | **Annahme:** kein Erstabschluss; beide Themen mit Übungsstand, dieses kommt zuerst |
| New York, Mexiko-Stadt, Alexandria, Adelaide | jeweils einziger Flug | USA, Mexiko, Ägypten, South Australia | – |

Nachbarländer für die übrigen Flüge begonnener Orte: Rom → Österreich, Schweiz, Slowenien; Samarkand → Kasachstan, Kirgisistan; Mumbai → Nepal, Sri Lanka, Bhutan; Paris → Spanien; Quito → Kolumbien.

## Sonderfälle – je zwei Lösungen

**1. Funktionen (heute Antarktis, keine Länder)**
- **A (gewählt, Festlegung 2):** Funktionen zieht in den neuen Reise-Kontinent **Orient** (Naher Osten und Kaukasus), 10 Länder. Antarktis wird Heimat der Expeditionen (21 Forschungsstationen). In der Antarktis hat noch kein Kind gelernt – nichts geht verloren.
- B: Funktionen bleibt in der Antarktis, Flüge = Forschungsstationen, Etappen = Regionen/Stützpunkte. Nachteil: Station ist kein Land, 5–11 „Städte“ je Station gibt es nicht; widerspricht dem neuen Prinzip.

**2. Daten und Zufall (12 Flüge) und Entdecker-Inseln (4 Flüge) überschneiden sich im Pazifik**
- **A (gewählt, Festlegungen 4/5):** Daten und Zufall = Australien nach Bundesstaaten + Neuseeland (Nord/Süd) + Melanesien; Entdecker-Inseln = Polynesien (Hawaii, Französisch-Polynesien, Samoa, Tonga). Keine Überschneidung.
- B: Daten und Zufall nur Australien + Neuseeland (9 Gebiete) und drei Flüge nach Südostasien; Nachteil: Asien ist durch Algebra belegt.

**3. Befund zu Festlegung 4: Die Zählung „zusammen 12“ stimmt nicht.** 7 Bundesstaaten/Territorien + 2 Inseln Neuseelands + Papua-Neuguinea + Fidschi = **11**. Für den 12. Flug:
- **A (gewählt):** **Vanuatu** (Melanesien, Nachbar von Fidschi; 5 Etappen: Port Vila, Luganville, Norsup, Lakatoro, Isangel – kleine Orte, Inselhüpfen per Fähre/Flug).
- B: Salomonen (Honiara u. a.) – noch weniger bekannte Orte. (Neukaledonien gemieden: französisches Gebiet mit umstrittener Unabhängigkeitsfrage.)

**4. Hawaii ist kein eigenes Land, sondern US-Bundesstaat; die USA sind schon Land eines Flugs (Zinsen).** Vorschlag: Hawaii wie die australischen Bundesstaaten als Gebiet zählen (Festlegung 5 nennt es so). Alternative: statt Hawaii die Cookinseln oder Tuvalu – kaum Orte.

**5. Flüge mit mehr als 12 Etappen** (Auftrag sagt 3–12): Natürliche Zahlen (13), Grundrechenarten (14), Brüche (14). Gelöst mit großen Ländern: Italien, Schweiz, Deutschland. Alternative: diese Flüge in der App teilen (Inhaltsänderung – nicht Teil dieses Vorschlags).

## Weitere Annahmen und Unsicherheiten

- **Nordamerika** schließt Mittelamerika und Karibik ein (Kuba, Guatemala, Costa Rica), weil 6 Länder gebraucht werden und nur USA/Kanada/Mexiko groß sind. Geografisch üblich, aber Kinder denken bei „Nordamerika“ oft nur an USA/Kanada.
- **Singapur** entfällt (Stadtstaat, keine 6 Städte); der Flug „Gleichungssysteme mit 3 Unbekannten“ geht nach Malaysia.
- **Vereinigtes Königreich** als ein Land (heute steht „Schottland“ bei Edinburgh). Edinburgh und Glasgow bleiben als Städte erhalten.
- **Kindgerecht, aber wenig bekannt:** Kasachstan, Kirgisistan, Mongolei, Bhutan, Bangladesch, Laos, Aserbaidschan, Papua-Neuguinea, Vanuatu, Samoa, Tonga, Französisch-Polynesien. In Polynesien sind die „Städte“ kleine Hauptorte (500–30 000 Einwohner).
- **Irak, Iran, Saudi-Arabien** gehören laut Festlegung 2 dazu. Inhaltlich gibt es dort gute Highlights (Babylon, Persepolis/Isfahan, AlUla), real gelten aber Reisewarnungen. Mekka ist bewusst nicht dabei (für Nicht-Muslime gesperrt).
- **Strittige Gebiete gemieden:** kein Kaschmir, Tibet, Xinjiang, Taiwan, Krim, Westsahara, Abchasien/Südossetien, Bergkarabach, Kirkuk; kein Sabah (Anspruch der Philippinen), Mindanao, Belize. Bewusst nicht gewählt wegen Krieg/Krise: Ukraine, Russland, Israel/Palästina, Syrien, Jemen, Libyen, Sudan, Mali (heute Timbuktu), Myanmar, Venezuela, Afghanistan.
- **Fahrbar** heißt Straße oder Fähre (z. B. Sansibar, Kangaroo Island, Bali, Philippinen, Fidschi/Samoa/Tonga). Hawaii, Französisch-Polynesien, Vanuatu, Papua-Neuguinea (Port Moresby hat keine Straße nach Lae) brauchen Inselflüge – **Annahme:** für Inselgebiete zulässig.
- **Reihenfolge innerhalb eines Landes** ist eine Strecke, nicht immer ein geschlossener Ring.
- Städtenamen auf Deutsch, wo gebräuchlich (Mailand, Breslau, Täbris); sonst Landesschreibweise.
- Die heutigen Orte, an denen niemand gelernt hat (z. B. Bagdad, Teheran, Timbuktu, Singapur, Göttingen, Brügge), sind frei verwendet; Bagdad, Brügge, Pisa, Florenz u. a. tauchen als Städte wieder auf.

## Zuordnung im Einzelnen

### Zahlen → Europa  (13 Flüge, 115 Etappen)

| # | Thema (Flug) | Kl. | heute | Land | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Natürliche Zahlen | Gym 5 | Rom | **Italien** | 13: Rom → Neapel → Pompei → Bari → Bologna → Venedig → Verona → Mailand → Turin → Genua → Pisa → Florenz → Siena |
| 2 | Ganze Zahlen | Gym 5 | Rom | **Österreich** | 11: Wien → St. Pölten → Linz → Salzburg → Kitzbühel → Innsbruck → Bregenz → Villach → Klagenfurt → Graz → Eisenstadt |
| 3 | Grundrechenarten und Rechengesetze | Gym 5 | Rom | **Schweiz** | 14: Basel → Zürich → Winterthur → St. Gallen → Chur → Lugano → Locarno → Sion → Montreux → Lausanne → Genf → Freiburg im Üechtland → Bern → Luzern |
| 4 | Potenzen als Schreibweise | Gym 5 | Rom | **Slowenien** | 7: Ljubljana → Kranj → Bled → Postojna → Koper → Piran → Maribor |
| 5 | Teilbarkeit | Gym 5 | Athen | **Griechenland** | 7: Athen → Korinth → Nafplio → Olympia → Patras → Delphi → Thessaloniki |
| 6 | Brüche und Anteile | Gym 6 | Pisa | **Deutschland** | 14: München → Augsburg → Stuttgart → Heidelberg → Frankfurt am Main → Köln → Münster → Bremen → Hamburg → Lübeck → Berlin → Dresden → Leipzig → Nürnberg |
| 7 | Dezimalzahlen | Gym 6 | Brügge | **Belgien** | 8: Brüssel → Antwerpen → Gent → Brügge → Ostende → Namur → Lüttich → Löwen |
| 8 | Rechnen mit rationalen Zahlen | Gym 6 | Florenz | **Vereinigtes Königreich** | 12: London → Oxford → Bath → Bristol → Cardiff → Liverpool → Manchester → York → Newcastle upon Tyne → Edinburgh → Glasgow → Belfast |
| 9 | Zehnerpotenzen und wissenschaftliche Schreibweise | Gym 6 | Paris | **Spanien** | 7: Barcelona → Valencia → Granada → Sevilla → Córdoba → Toledo → Madrid |
| 10 | Potenzen und negative Exponenten | Gym 6 | Paris | **Frankreich** | 3: Paris → Lyon → Marseille |
| 11 | Elementare Wurzeln | Gym 9 | Göttingen | **Niederlande** | 6: Amsterdam → Haarlem → Leiden → Den Haag → Rotterdam → Utrecht |
| 12 | Wurzeln und reelle Zahlen | Gym 9 | Göttingen | **Polen** | 7: Warschau → Danzig → Thorn → Posen → Breslau → Krakau → Zakopane |
| 13 | Rationale Exponenten und n-te Wurzel | Gym 9 | Edinburgh | **Norwegen** | 6: Oslo → Lillehammer → Trondheim → Ålesund → Bergen → Stavanger |

### Geld und Verhältnisse → Nordamerika (mit Mittelamerika und Karibik)  (6 Flüge, 45 Etappen)

| # | Thema (Flug) | Kl. | heute | Land | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Größen und Einheiten | Gym 5 | Toronto | **Kanada** | 8: Victoria → Vancouver → Banff → Calgary → Winnipeg → Toronto → Ottawa → Montreal |
| 2 | Direkte Proportionalität und Dreisatz | Gym 5 | Chicago | **Kuba** | 8: Havanna → Viñales → Varadero → Santa Clara → Cienfuegos → Trinidad → Camagüey → Santiago de Cuba |
| 3 | Prozent- und Zinsrechnung | Gym 6 | Mexiko-Stadt | **Mexiko** | 6: Guadalajara → Guanajuato → Mexiko-Stadt → Puebla → Oaxaca → Veracruz |
| 4 | Zinsen | Gym 6 | New York | **USA** | 8: Boston → New York → Washington, D.C. → Chicago → Denver → Phoenix → Los Angeles → San Francisco |
| 5 | Vermehrter und verminderter Grundwert | Gym 7 | Los Angeles | **Guatemala** | 8: Guatemala-Stadt → Antigua Guatemala → Panajachel → Chichicastenango → Quetzaltenango → Cobán → Flores → Puerto Barrios |
| 6 | Indirekte Proportionalität | Gym 8 | Vancouver | **Costa Rica** | 7: San José → Alajuela → La Fortuna → Liberia → Puntarenas → Quepos → Cartago |

### Algebra → Asien (ohne Orient)  (19 Flüge, 116 Etappen)

| # | Thema (Flug) | Kl. | heute | Land | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Einfache Gleichungen | Gym 5 | Bagdad | **Kambodscha** | 5: Siem Reap → Battambang → Phnom Penh → Kampot → Sihanoukville |
| 2 | Terme aufstellen und deuten | Gym 7 | Teheran | **Vietnam** | 6: Hanoi → Ha Long → Hue → Da Nang → Hoi An → Ho-Chi-Minh-Stadt |
| 3 | Potenzgesetze | Gym 7 | Samarkand | **Usbekistan** | 5: Fergana → Taschkent → Samarkand → Buchara → Chiwa |
| 4 | Terme umformen | Gym 7 | Samarkand | **Kasachstan** | 8: Almaty → Taras → Schymkent → Türkistan → Kysylorda → Karaganda → Astana → Pawlodar |
| 5 | Lineare Gleichungen | Gym 7 | Samarkand | **Kirgisistan** | 6: Bischkek → Tscholpon-Ata → Karakol → Naryn → Dschalal-Abad → Osch |
| 6 | Intervalle | Gym 8 | Delhi | **Mongolei** | 4: Ulaanbaatar → Darchan → Erdenet → Charchorin (Karakorum) |
| 7 | Lineare Ungleichungen | Gym 8 | Delhi | **Indonesien** | 7: Jakarta → Bandung → Yogyakarta → Solo → Surabaya → Malang → Denpasar |
| 8 | Bruchterme | Gym 8 | Mumbai | **Indien** | 7: Delhi → Agra → Jaipur → Udaipur → Ahmedabad → Mumbai → Panaji (Goa) |
| 9 | Potenzgesetze mit ganzzahligen Exponenten | Gym 8 | Mumbai | **Nepal** | 5: Bhaktapur → Lalitpur (Patan) → Kathmandu → Pokhara → Bharatpur |
| 10 | Bruch- und Verhältnisgleichungen | Gym 8 | Mumbai | **Sri Lanka** | 7: Colombo → Galle → Nuwara Eliya → Kandy → Dambulla → Anuradhapura → Trincomalee |
| 11 | Formeln umstellen | Gym 8 | Mumbai | **Bhutan** | 5: Paro → Thimphu → Punakha → Wangdue Phodrang → Jakar |
| 12 | Gleichungssysteme mit 2 Unbekannten | Gym 8 | Peking | **China** | 9: Peking → Xi'an → Chengdu → Chongqing → Guilin → Guangzhou → Hangzhou → Shanghai → Nanjing |
| 13 | Quadratische Gleichungen (allgemein) | Gym 9 | Seoul | **Südkorea** | 8: Incheon → Seoul → Suwon → Daejeon → Jeonju → Gwangju → Busan → Gyeongju |
| 14 | Gleichungssysteme mit 3 Unbekannten | Gym 9 | Singapur | **Malaysia** | 6: Johor Bahru → Malakka → Kuala Lumpur → Ipoh → George Town → Alor Setar |
| 15 | Potenzgleichungen | Gym 9 | Tokio | **Japan** | 6: Tokio → Kamakura → Kyoto → Nara → Osaka → Hiroshima |
| 16 | Exponentialgleichungen | Gym 10 | Bangkok | **Thailand** | 6: Phuket → Hua Hin → Bangkok → Ayutthaya → Sukhothai → Chiang Mai |
| 17 | Polynomgleichungen | Gym 10 | Bangkok | **Laos** | 5: Luang Prabang → Vang Vieng → Vientiane → Thakhek → Pakse |
| 18 | Quadratische Terme und Extremwerte | RS 8 | Shanghai | **Philippinen** | 5: Baguio → Manila → Legazpi → Cebu → Tagbilaran |
| 19 | Wurzelgleichungen | RS 9 | Tokio | **Bangladesch** | 6: Rajshahi → Khulna → Dhaka → Sylhet → Chittagong → Cox's Bazar |

### Funktionen → Orient (Naher Osten und Kaukasus) – neu, ersetzt Antarktis  (10 Flüge, 79 Etappen)

| # | Thema (Flug) | Kl. | heute | Land | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Zuordnung und Funktion | Gym 8 | McMurdo-Station | **Georgien** | 9: Tiflis → Stepanzminda → Mzcheta → Gori → Borjomi → Batumi → Kutaissi → Telawi → Sighnaghi |
| 2 | Lineare Funktionen | Gym 8 | Neumayer-Station III | **Türkei** | 11: Istanbul → Bursa → Çanakkale → Izmir → Selçuk → Bodrum → Antalya → Konya → Göreme → Ankara → Safranbolu |
| 3 | Gebrochen-rationale Funktionen | Gym 8 | Amundsen-Scott-Südpolstation | **Armenien** | 5: Jerewan → Etschmiadsin → Gjumri → Dilidschan → Sewan |
| 4 | Quadratische Funktionen | Gym 9 | Wostok-Station | **Irak** | 9: Bagdad → Samarra → Mossul → Erbil → Sulaimaniyya → Basra → Nadschaf → Kerbela → Hilla (Babylon) |
| 5 | Potenzfunktionen | Gym 9 | Rothera-Station | **Iran** | 10: Teheran → Rascht → Täbris → Hamadan → Isfahan → Schiras → Bandar Abbas → Kerman → Yazd → Kaschan |
| 6 | Exponential- und Logarithmusfunktionen | Gym 10 | Halley-Station | **Vereinigte Arabische Emirate** | 7: Abu Dhabi → Dubai → Schardscha → Adschman → Umm al-Qaiwain → Ras al-Chaima → Fudschaira |
| 7 | Sinus- und Kosinusfunktion | Gym 10 | Concordia-Station | **Saudi-Arabien** | 8: Riad → Hail → AlUla → Tabuk → Medina → Dschidda → Taif → Abha |
| 8 | Ganzrationale Funktionen | Gym 10 | Casey-Station | **Oman** | 7: Maskat → Barka → Sohar → Ibri → Bahla → Nizwa → Sur |
| 9 | Reihen | IB 5 | Palmer-Station | **Aserbaidschan** | 8: Baku → Quba → Schamachy → Gabala → Scheki → Gandscha → Mingətschevir → Lənkəran |
| 10 | Betragsfunktion | IB 5 | Palmer-Station | **Jordanien** | 5: Amman → Dscherasch → Madaba → Wadi Musa (Petra) → Aqaba |

### Geometrie → Afrika  (14 Flüge, 100 Etappen)

| # | Thema (Flug) | Kl. | heute | Land | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Grundbegriffe und Figuren | Gym 5 | Kairo | **Tunesien** | 7: Sidi Bou Saïd → Tunis → Sousse → Monastir → El Djem → Tozeur → Kairouan |
| 2 | Ortslinien und Ortsbereiche | Gym 5 | Kairo | **Senegal** | 6: Saint-Louis → Thiès → Dakar → Mbour → Joal-Fadiouth → Kaolack |
| 3 | Mit Winkeln rechnen | Gym 5 | Timbuktu | **Ghana** | 7: Accra → Ho → Tamale → Kumasi → Takoradi → Elmina → Cape Coast |
| 4 | Kongruenzabbildungen | Gym 7 | Marrakesch | **Marokko** | 10: Tanger → Chefchaouen → Fès → Meknès → Rabat → Casablanca → Essaouira → Agadir → Ouarzazate → Marrakesch |
| 5 | Winkelsätze | Gym 7 | Addis Abeba | **Tansania** | 9: Sansibar-Stadt → Daressalam → Bagamoyo → Tanga → Moshi → Arusha → Mwanza → Dodoma → Morogoro |
| 6 | Konstruktionen, Kongruenz und Beweise | Gym 7 | Addis Abeba | **Ruanda** | 6: Kigali → Musanze → Rubavu (Gisenyi) → Karongi (Kibuye) → Huye → Nyanza |
| 7 | Kreis und Tangenten | Gym 7 | Alexandria | **Ägypten** | 6: Alexandria → Gizeh → Kairo → Hurghada → Luxor → Assuan |
| 8 | Ähnlichkeit und Strahlensätze | Gym 9 | Nairobi | **Kenia** | 8: Malindi → Mombasa → Nairobi → Naivasha → Nakuru → Kisumu → Eldoret → Nanyuki |
| 9 | Satz des Pythagoras | Gym 9 | Kapstadt | **Simbabwe** | 6: Harare → Mutare → Masvingo → Bulawayo → Hwange → Victoria Falls |
| 10 | Trigonometrie im rechtwinkligen Dreieck | Gym 9 | Sansibar | **Namibia** | 7: Windhoek → Otjiwarongo → Tsumeb → Swakopmund → Walvis Bay → Lüderitz → Keetmanshoop |
| 11 | Allgemeine Trigonometrie | Gym 9 | Sansibar | **Südafrika** | 9: Kapstadt → Stellenbosch → Mossel Bay → Knysna → Gqeberha (Port Elizabeth) → Durban → Pretoria → Johannesburg → Bloemfontein |
| 12 | Trigonometrische Gleichungen | Gym 9 | Sansibar | **Mauritius** | 6: Port Louis → Grand Baie → Flic en Flac → Quatre Bornes → Curepipe → Mahébourg |
| 13 | Zweireihige Determinanten | RS 7 | Lagos | **Uganda** | 6: Entebbe → Kampala → Jinja → Mbale → Fort Portal → Mbarara |
| 14 | Matrizen und Abbildungen mit Matrizen | RS 10 | Dakar | **Madagaskar** | 7: Toamasina → Moramanga → Antananarivo → Antsirabe → Ambositra → Fianarantsoa → Toliara |

### Fläche und Raum → Südamerika  (9 Flüge, 57 Etappen)

| # | Thema (Flug) | Kl. | heute | Land | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Umfang und Flächeninhalt | Gym 5 | Lima | **Peru** | 7: Lima → Paracas → Nazca → Arequipa → Puno → Cusco → Aguas Calientes (Machupicchu) |
| 2 | Volumen und Oberfläche | Gym 5 | Rio de Janeiro | **Uruguay** | 5: Colonia del Sacramento → Montevideo → Punta del Este → Salto → Paysandú |
| 3 | Flächen von Parallelogramm, Dreieck und Trapez | Gym 6 | Quito | **Ecuador** | 7: Otavalo → Quito → Baños → Riobamba → Cuenca → Guayaquil → Manta |
| 4 | Volumen | Gym 6 | Quito | **Kolumbien** | 7: Cartagena → Barranquilla → Santa Marta → Medellín → Salento → Cali → Bogotá |
| 5 | Kreisberechnungen | Gym 8 | Buenos Aires | **Argentinien** | 6: Buenos Aires → Rosario → Mendoza → San Miguel de Tucumán → Salta → Puerto Iguazú |
| 6 | Körper darstellen | Gym 8 | Cusco | **Bolivien** | 6: Copacabana → La Paz → Uyuni → Potosí → Sucre → Cochabamba |
| 7 | Prismen und Zylinder | Gym 8 | Cusco | **Brasilien** | 7: Rio de Janeiro → São Paulo → Curitiba → Foz do Iguaçu → Brasília → Belo Horizonte → Salvador |
| 8 | Schrägbilder und Raumdarstellung | Gym 10 | Brasília | **Paraguay** | 5: Asunción → San Bernardino → Encarnación → Ciudad del Este → Concepción |
| 9 | Pyramide, Kegel, Kugel | Gym 10 | Santiago de Chile | **Chile** | 7: San Pedro de Atacama → Antofagasta → Copiapó → La Serena → Viña del Mar → Valparaíso → Santiago de Chile |

### Daten und Zufall → Australien (nach Bundesstaaten) und Ozeanien  (12 Flüge, 74 Etappen)

| # | Thema (Flug) | Kl. | heute | Land | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Zählen und Kombinatorik | Gym 5 | Melbourne | **Victoria** | 7: Melbourne → Cowes (Phillip Island) → Geelong → Lorne → Warrnambool → Ballarat → Bendigo |
| 2 | Daten erfassen und darstellen | Gym 6 | Adelaide | **South Australia** | 6: Adelaide → Hahndorf → Victor Harbor → Kingscote → Port Augusta → Coober Pedy |
| 3 | Mittelwert und Häufigkeiten | Gym 6 | Sydney | **Tasmanien** | 3: Hobart → Launceston → Devonport |
| 4 | Median, Quartile, Boxplot | Gym 7 | Brisbane | **Western Australia** | 6: Perth → Fremantle → Margaret River → Albany → Esperance → Kalgoorlie |
| 5 | Zufall und Laplace | Gym 8 | Auckland | **Neuseeland – Nordinsel** | 6: Auckland → Hamilton → Rotorua → Taupō → Napier → Wellington |
| 6 | Verknüpfte Ereignisse | Gym 9 | Wellington | **Queensland** | 11: Gold Coast → Brisbane → Noosa Heads → Hervey Bay → Bundaberg → Rockhampton → Mackay → Airlie Beach → Townsville → Cairns → Port Douglas |
| 7 | Mehrstufige Zufallsexperimente | Gym 10 | Darwin | **New South Wales** | 9: Sydney → Wollongong → Katoomba → Bathurst → Dubbo → Tamworth → Coffs Harbour → Port Macquarie → Newcastle |
| 8 | Simulation | Gym 10 | Darwin | **Northern Territory** | 6: Darwin → Jabiru → Katherine → Tennant Creek → Alice Springs → Yulara |
| 9 | Stichproben und Aussagekraft | RS 7 | Perth | **Neuseeland – Südinsel** | 5: Picton → Kaikōura → Christchurch → Dunedin → Queenstown |
| 10 | Standardabweichung | IB 5 | Suva | **Vanuatu** | 5: Port Vila → Luganville → Norsup → Lakatoro → Isangel |
| 11 | Zweidimensionale Daten | IB 5 | Hobart | **Fidschi** | 5: Nadi → Lautoka → Sigatoka → Navua (Pacific Harbour) → Suva |
| 12 | Normalverteilung | IB 5 | Suva | **Papua-Neuguinea** | 5: Port Moresby → Lae → Madang → Goroka → Mount Hagen |

### Entdecker-Inseln → Pazifik  (4 Flüge, 20 Etappen)

| # | Thema (Flug) | Kl. | heute | Land | Etappen = Städte (Reihenfolge) |
|---|---|---|---|---|---|
| 1 | Aussagenlogik | IB 4 | Honolulu | **Hawaii** | 5: Honolulu → Kailua → Kahului → Hilo → Līhuʻe |
| 2 | Graphentheorie | IB 4 | Tahiti | **Französisch-Polynesien** | 5: Papeete → Afareaitu → Fare → Uturoa → Vaitape |
| 3 | Schranken und Genauigkeit | IB 5 | Honolulu | **Tonga** | 5: Nukuʻalofa → Kolonga → Pangai → Neiafu → ʻOhonua |
| 4 | Lineare Optimierung | IB 5 | Tahiti | **Samoa** | 5: Apia → Leulumoega → Mulifanua → Palauli → Asau |

### Antarktis → Expeditionen (je Expedition eine Forschungsstation)

| Expedition | Station | Betreiber |
|---|---|---|
| 5-aquarium | Palmer-Station | USA |
| 5-flug_toronto | McMurdo-Station | USA |
| 5-kettennachricht | Amundsen-Scott-Südpolstation | USA |
| 5-oase | Maitri-Station (Schirmacher-Oase) | Indien |
| 5-pyramide | Princess-Elisabeth-Station | Belgien |
| 5-roemerstrasse | Mario-Zucchelli-Station | Italien |
| 5-schatzsuche | Esperanza-Station | Argentinien |
| 5-uhrturm | Halley-VI-Station | Vereinigtes Königreich |
| 5-wetterstation | Neumayer-Station III | Deutschland |
| 5-zeltplatz | Kohnen-Station | Deutschland |
| 8-garten | Troll-Station | Norwegen |
| 8-handytarif | Rothera-Station | Vereinigtes Königreich |
| 8-kerzen | Wostok-Station | Russland |
| 8-klassenfahrt | Dumont-d’Urville-Station | Frankreich |
| 8-pool | Davis-Station | Australien |
| 8-radtour | Casey-Station | Australien |
| 8-roller | Mawson-Station | Australien |
| 8-saftbar | Syowa-Station | Japan |
| 8-schuelerzeitung | Zhongshan-Station | China |
| 8-schulfest | Arctowski-Station | Polen |
| 8-zelt | Scott Base | Neuseeland |
