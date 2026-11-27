"""Datenquelle für den Reise-Aufbau-Vorschlag (22.11.2026, fortgeschrieben „Reise-Aufbau 2“).
Nur Vorschlag – kein App-Code, nichts in der Datenbank.
Format je Stadt: "Anzeigename" oder ("Anzeigename", "Suchname für die Prüfung (GeoNames)").
Flug-Schlüssel: thema_id (ungeteilt) oder "thema-teil" (geteilt nach lk_teilung_2211.json).
Städte stehen in der Reihenfolge der Etappen: ungeteilt = Etappen der Themendatei (inkl. neuer LK-D-Etappen),
geteilt = Etappen des Teils laut Teilungsliste.
"""

# Heutiger Stand (DB, nur lesend): Orte mit Lernaktivität oder Status „fertig“ – ohne Kindernamen
BEGONNENE_ORTE = {
    # block_id: (heutige Stadt, Flug/thema_id, der das Land behält, Begründung)
    49: ("Rom", 15, "flug_erstabschluss: Thema 15 zuerst abgeschlossen"),
    62: ("Samarkand", 102, "flug_erstabschluss: Thema 102 zuerst abgeschlossen"),
    44: ("Paris", 30, "ANNAHME: kein Erstabschluss gespeichert; nur Thema 30 hat Karten-Aktivität"),
    60: ("Mumbai", 31, "ANNAHME: kein Erstabschluss; Thema 31 und 5 haben Karten-Aktivität, 31 kommt im Lehrplan zuerst"),
    114: ("Quito", 99, "ANNAHME: kein Erstabschluss; beide Themen mit Karten-Aktivität, 99 kommt im Lehrplan zuerst"),
    52: ("New York", 71, "einziger Flug des Orts"),
    53: ("Mexiko-Stadt", 24, "einziger Flug des Orts"),
    79: ("Alexandria", 45, "einziger Flug des Orts"),
    96: ("Adelaide", 57, "einziger Flug des Orts"),
}

# Reise-Kontinente in Reihenfolge; kontinent_id = heutige schule.kontinent.id (Orient übernimmt id 4)
KONTINENTE = [
 {"kontinent_id": 1, "themengebiet": "Zahlen", "reise": "Europa", "fluege": {
   15: ("Italien", "IT", None, ["Rom", ("Neapel","Naples"), "Pompei", "Bari", "Bologna", ("Venedig","Venice"), "Verona", ("Mailand","Milan"), ("Turin","Turin"), ("Genua","Genoa"), "Pisa", ("Florenz","Florence"), "Siena"]),
   16: ("Österreich", "AT", None, [("Wien","Vienna"), "St. Pölten", "Linz", "Salzburg", "Kitzbühel", "Innsbruck", "Bregenz", "Villach", "Klagenfurt", "Graz", "Eisenstadt"]),
   18: ("Schweiz", "CH", None, ["Basel", ("Zürich","Zurich"), "Winterthur", "St. Gallen", "Chur", "Lugano", "Locarno", "Sion", "Montreux", "Lausanne", ("Genf","Geneva"), ("Freiburg im Üechtland","Fribourg"), "Bern", "Luzern"]),
   67: ("Slowenien", "SI", None, ["Ljubljana", "Kranj", "Bled", "Postojna", "Koper", "Piran", "Maribor"]),
   17: ("Griechenland", "GR", None, [("Athen","Athens"), ("Korinth","Corinth"), "Nafplio", ("Olympia","Archaia Olympia"), "Patras", ("Delphi","Delfoi"), ("Thessaloniki","Thessaloniki")]),
   21: ("Deutschland", "DE", None, [("München","Munich"), "Augsburg", "Stuttgart", "Heidelberg", ("Frankfurt am Main","Frankfurt am Main"), ("Köln","Cologne"), "Münster", "Bremen", "Hamburg", ("Lübeck","Luebeck"), "Berlin", "Dresden", "Leipzig", ("Nürnberg","Nuremberg")]),
   22: ("Belgien", "BE", None, [("Brüssel","Brussels"), ("Antwerpen","Antwerpen"), ("Gent","Gent"), ("Brügge","Brugge"), ("Ostende","Oostende"), "Namur", ("Lüttich","Liège"), ("Löwen","Leuven")]),
   23: ("Vereinigtes Königreich", "GB", None, ["London", "Oxford", "Bath", "Bristol", "Cardiff", "Liverpool", "Manchester", "York", ("Newcastle upon Tyne","Newcastle upon Tyne"), "Edinburgh", "Glasgow", "Belfast"]),
   19: ("Spanien", "ES", None, ["Barcelona", "Valencia", "Granada", "Sevilla", ("Córdoba","Cordoba"), "Toledo", "Madrid"]),
   30: ("Frankreich", "FR", None, ["Paris", "Lyon", "Marseille"]),
   68: ("Niederlande", "NL", None, ["Amsterdam", "Haarlem", "Leiden", ("Den Haag","The Hague"), "Rotterdam", "Utrecht"]),
   20: ("Polen", "PL", None, [("Warschau","Warsaw"), ("Danzig","Gdańsk"), ("Thorn","Toruń"), ("Posen","Poznań"), ("Breslau","Wrocław"), ("Krakau","Kraków"), "Zakopane", "Wieliczka"]),
   96: ("Norwegen", "NO", None, ["Oslo", "Lillehammer", "Trondheim", ("Ålesund","Ålesund"), "Bergen", "Stavanger"]),
 }},
 {"kontinent_id": 2, "themengebiet": "Geld und Verhältnisse", "reise": "Nordamerika (mit Mittelamerika und Karibik)", "fluege": {
   25: ("Kanada", "CA", None, ["Victoria", "Vancouver", "Banff", "Calgary", "Winnipeg", "Toronto", "Ottawa", ("Montreal","Montréal")]),
   "26-1": ("Kuba", "CU", None, [("Viñales","Viñales"), ("Havanna","Havana"), "Varadero", "Santa Clara", "Cienfuegos"]),
   "26-2": ("Jamaika", "JM", None, ["Montego Bay", "Ocho Rios", "Kingston"]),
   24: ("Mexiko", "MX", None, ["Guadalajara", "Guanajuato", ("Mexiko-Stadt","Mexico City"), "Puebla", ("Oaxaca","Oaxaca"), "Veracruz"]),
   71: ("USA", "US", None, ["Boston", "New York", ("Washington, D.C.","Washington"), "Chicago", "Denver", "Phoenix", "Los Angeles", "San Francisco"]),
   94: ("Guatemala", "GT", None, [("Guatemala-Stadt","Guatemala City"), "Antigua Guatemala", "Panajachel", "Chichicastenango", "Quetzaltenango", ("Cobán","Coban"), "Flores", "Puerto Barrios"]),
   93: ("Costa Rica", "CR", None, ["San José", "Alajuela", "La Fortuna", "Liberia", "Puntarenas", "Quepos", "Cartago"]),
 }},
 {"kontinent_id": 3, "themengebiet": "Algebra", "reise": "Asien (ohne Orient)", "fluege": {
   1: ("Kambodscha", "KH", None, ["Siem Reap", "Battambang", ("Phnom Penh","Phnom Penh"), "Kampot", "Sihanoukville"]),
   28: ("Vietnam", "VN", None, ["Hanoi", ("Ha Long","Ha Long"), ("Hue","Huế"), ("Da Nang","Da Nang"), ("Hoi An","Hội An"), ("Ho-Chi-Minh-Stadt","Ho Chi Minh City")]),
   102: ("Usbekistan", "UZ", None, [("Fergana","Fergana"), ("Taschkent","Tashkent"), "Samarkand", ("Buchara","Bukhara"), ("Chiwa","Khiva")]),
   "29-1": ("Kasachstan", "KZ", None, ["Almaty", ("Taras","Taraz"), ("Schymkent","Shymkent"), ("Türkistan","Turkestan"), ("Kysylorda","Kyzylorda")]),
   "29-2": ("Turkmenistan", "TM", None, [("Daschoguz","Dashoguz"), ("Türkmenabat","Turkmenabat"), "Mary", ("Aschgabat","Ashgabat")]),
   2: ("Kirgisistan", "KG", None, [("Bischkek","Bishkek"), ("Tscholpon-Ata","Cholpon-Ata"), "Karakol", "Naryn", ("Dschalal-Abad","Jalal-Abad"), ("Osch","Osh")]),
   69: ("Mongolei", "MN", None, ["Ulaanbaatar", ("Darchan","Darhan"), "Erdenet", ("Charchorin (Karakorum)","Kharkhorin")]),
   3: ("Indonesien", "ID", None, ["Jakarta", "Bandung", "Yogyakarta", ("Solo","Surakarta"), "Surabaya", "Malang", "Denpasar"]),
   31: ("Indien", "IN", None, [("Delhi","New Delhi"), "Agra", "Jaipur", "Udaipur", "Ahmedabad", "Mumbai", ("Panaji (Goa)","Panaji")]),
   103: ("Nepal", "NP", None, ["Bhaktapur", ("Lalitpur (Patan)","Patan"), ("Kathmandu","Kathmandu"), "Pokhara", "Bharatpur"]),
   5: ("Sri Lanka", "LK", None, ["Colombo", "Galle", "Nuwara Eliya", "Kandy", "Dambulla", "Anuradhapura", "Trincomalee"]),
   4: ("Bhutan", "BT", None, ["Paro", "Thimphu", "Punakha", ("Wangdue Phodrang","Wangdue Phodrang"), ("Jakar","Jakar")]),
   6: ("China", "CN", None, [("Peking","Beijing"), ("Xi'an","Xi'an"), "Chengdu", "Chongqing", "Guilin", ("Guangzhou","Guangzhou"), "Hangzhou", "Shanghai", "Nanjing"]),
   8: ("Südkorea", "KR", None, ["Incheon", "Seoul", "Suwon", "Daejeon", "Jeonju", "Gwangju", "Busan", "Gyeongju"]),
   7: ("Malaysia", "MY", None, ["Johor Bahru", ("Malakka","Malacca"), "Kuala Lumpur", "Ipoh", "George Town", "Alor Setar"]),
   9: ("Japan", "JP", None, [("Tokio","Tokyo"), "Kamakura", ("Kyoto","Kyoto"), "Nara", ("Osaka","Osaka"), "Hiroshima"]),
   10: ("Thailand", "TH", None, ["Phuket", "Hua Hin", "Bangkok", "Ayutthaya", "Sukhothai", "Chiang Mai"]),
   11: ("Laos", "LA", None, ["Luang Prabang", "Vang Vieng", "Vientiane", "Thakhek", "Pakse"]),
   97: ("Philippinen", "PH", None, ["Baguio", "Manila", ("Legazpi","Legaspi"), ("Cebu","Cebu City"), "Tagbilaran"]),
   13: ("Bangladesch", "BD", None, ["Rajshahi", "Khulna", ("Dhaka","Dhaka"), "Sylhet", ("Chittagong","Chattogram"), "Cox's Bazar"]),
 }},
 {"kontinent_id": 4, "themengebiet": "Funktionen", "reise": "Orient (Naher Osten und Kaukasus) – neu, ersetzt Antarktis", "fluege": {
   32: ("Georgien", "GE", None, [("Tiflis","Tbilisi"), ("Stepanzminda","Stepantsminda"), ("Mzcheta","Mtskheta"), "Gori", "Borjomi", "Batumi", ("Kutaissi","Kutaisi"), ("Telawi","Telavi"), ("Sighnaghi","Sighnaghi")]),
   33: ("Türkei", "TR", None, ["Istanbul", "Bursa", ("Çanakkale","Çanakkale"), ("Izmir","Izmir"), ("Selçuk","Selçuk"), "Bodrum", "Antalya", "Konya", ("Göreme","Göreme"), "Ankara", "Safranbolu"]),
   34: ("Armenien", "AM", None, [("Jerewan","Yerevan"), ("Etschmiadsin","Vagharshapat"), ("Gjumri","Gyumri"), ("Dilidschan","Dilijan"), ("Sewan","Sevan")]),
   35: ("Irak", "IQ", None, ["Bagdad", "Samarra", ("Mossul","Mosul"), "Erbil", ("Sulaimaniyya","Sulaymaniyah"), "Basra", ("Nadschaf","Najaf"), ("Kerbela","Karbala"), ("Hilla (Babylon)","Al Hillah")]),
   36: ("Iran", "IR", None, [("Teheran","Tehran"), ("Rascht","Rasht"), ("Täbris","Tabriz"), "Hamadan", ("Isfahan","Isfahan"), ("Schiras","Shiraz"), "Bandar Abbas", "Kerman", "Yazd", ("Kaschan","Kashan")]),
   37: ("Vereinigte Arabische Emirate", "AE", None, ["Abu Dhabi", "Dubai", ("Schardscha","Sharjah"), ("Adschman","Ajman"), ("Umm al-Qaiwain","Umm al Qaywayn"), ("Ras al-Chaima","Ras al-Khaimah"), ("Fudschaira","Fujairah")]),
   38: ("Saudi-Arabien", "SA", None, [("Riad","Riyadh"), ("Hail","Ḩā'il"), ("AlUla","Al-`Ula"), ("Tabuk","Tabuk"), ("Medina","Medina"), ("Dschidda","Jeddah"), ("Taif","Ta’if"), "Abha"]),
   39: ("Oman", "OM", None, [("Maskat","Muscat"), "Barka", "Sohar", "Ibri", "Bahla", "Nizwa", "Sur"]),
   75: ("Jordanien", "JO", None, ["Amman", ("Dscherasch","Jerash"), "Madaba", ("Wadi Musa (Petra)","Wadi Musa"), "Aqaba"]),
   76: ("Aserbaidschan", "AZ", None, ["Baku", "Quba", ("Schamachy","Shamakhi"), ("Gabala","Qabala"), ("Scheki","Shaki"), ("Gandscha","Ganja"), ("Mingətschevir","Mingelchaur"), ("Lənkəran","Lankaran")]),
 }},
 {"kontinent_id": 5, "themengebiet": "Geometrie", "reise": "Afrika", "fluege": {
   42: ("Tunesien", "TN", None, [("Sidi Bou Saïd","Sidi Bou Said"), "Tunis", "Sousse", "Monastir", "El Djem", "Tozeur", "Kairouan"]),
   73: ("Senegal", "SN", None, ["Saint-Louis", ("Thiès","Thiès"), "Dakar", "Mbour", ("Joal-Fadiouth","Joal"), "Kaolack"]),
   43: ("Ghana", "GH", None, ["Accra", "Ho", "Tamale", "Kumasi", "Takoradi", "Elmina", "Cape Coast"]),
   "46-1": ("Marokko", "MA", None, ["Casablanca", "Rabat", "Tanger", "Chefchaouen", ("Fès","Fès"), "Oujda"]),
   "46-2": ("Algerien", "DZ", None, ["Tlemcen", "Oran", ("Algier","Algiers")]),
   "46-3": ("Mauretanien", "MR", None, ["Nouadhibou", "Nouakchott", "Atar"]),
   98: ("Tansania", "TZ", None, [("Sansibar-Stadt","Zanzibar"), ("Daressalam","Dar es Salaam"), "Bagamoyo", "Tanga", "Moshi", "Arusha", "Mwanza", "Dodoma", "Morogoro"]),
   "44-1": ("Ruanda", "RW", None, ["Kigali", "Musanze", ("Rubavu (Gisenyi)","Gisenyi"), ("Karongi (Kibuye)","Kibuye"), ("Huye","Butare")]),
   "44-2": ("Burundi", "BI", None, ["Bujumbura", "Gitega"]),
   45: ("Ägypten", "EG", None, ["Alexandria", ("Gizeh","Giza"), ("Kairo","Cairo"), "Hurghada", ("Luxor","Luxor"), ("Assuan","Aswan")]),
   47: ("Kenia", "KE", None, ["Malindi", "Mombasa", "Nairobi", "Naivasha", "Nakuru", "Kisumu", "Eldoret", "Nanyuki", "Nyeri"]),
   54: ("Simbabwe", "ZW", None, ["Harare", "Mutare", "Masvingo", "Bulawayo", "Hwange", "Victoria Falls"]),
   55: ("Namibia", "NA", None, ["Windhoek", "Otjiwarongo", "Tsumeb", "Swakopmund", "Walvis Bay", ("Lüderitz","Lüderitz"), "Keetmanshoop"]),
   56: ("Südafrika", "ZA", None, [("Kapstadt","Cape Town"), "Stellenbosch", "Mossel Bay", "Knysna", ("Gqeberha (Port Elizabeth)","Port Elizabeth"), "Durban", "Pretoria", "Johannesburg", "Bloemfontein"]),
   14: ("Mauritius", "MU", None, ["Port Louis", "Grand Baie", "Flic en Flac", "Quatre Bornes", "Curepipe", ("Mahébourg","Mahébourg")]),
   74: ("Uganda", "UG", None, ["Entebbe", "Kampala", "Jinja", "Mbale", "Fort Portal", "Mbarara"]),
   49: ("Madagaskar", "MG", None, ["Toamasina", "Moramanga", "Antananarivo", "Antsirabe", "Ambositra", "Fianarantsoa", "Toliara"]),
 }},
 {"kontinent_id": 6, "themengebiet": "Fläche und Raum", "reise": "Südamerika", "fluege": {
   50: ("Peru", "PE", None, ["Lima", "Paracas", ("Nazca","Nazca"), "Arequipa", "Puno", "Cusco", ("Aguas Calientes (Machupicchu)","Machupicchu")]),
   53: ("Uruguay", "UY", None, ["Colonia del Sacramento", "Montevideo", "Punta del Este", "Salto", ("Paysandú","Paysandú")]),
   99: ("Ecuador", "EC", None, ["Otavalo", "Quito", ("Baños","Baños"), "Riobamba", "Cuenca", "Guayaquil", "Manta", "Portoviejo"]),
   100: ("Kolumbien", "CO", None, ["Cartagena", "Barranquilla", "Santa Marta", ("Medellín","Medellín"), "Salento", "Cali", ("Bogotá","Bogotá")]),
   51: ("Argentinien", "AR", None, ["Buenos Aires", "Rosario", "Mendoza", ("San Miguel de Tucumán","San Miguel de Tucumán"), "Salta", ("Puerto Iguazú","Puerto Iguazú")]),
   52: ("Bolivien", "BO", None, ["Copacabana", "La Paz", "Uyuni", ("Potosí","Potosí"), "Sucre", "Cochabamba"]),
   "101-1": ("Brasilien – Südosten", "BR", "BR_SUEDOST", ["Santos", ("São Paulo","São Paulo"), "Campinas", "Belo Horizonte", "Ouro Preto", ("Petrópolis","Petropolis"), "Rio de Janeiro"]),
   "101-2": ("Brasilien – Mittelwesten", "BR", "BR_MITTELWEST", [("Brasília","Brasilia")]),
   "91-1": ("Paraguay", "PY", None, [("Asunción","Asunción"), "San Bernardino", ("Encarnación","Encarnación"), "Ciudad del Este"]),
   "91-2": ("Brasilien – Süden", "BR", "BR_SUED", [("Foz do Iguaçu","Foz do Iguaçu"), "Curitiba", ("Florianópolis","Florianopolis"), "Porto Alegre"]),
   92: ("Chile", "CL", None, [("San Pedro de Atacama","San Pedro de Atacama"), "Antofagasta", ("Copiapó","Copiapó"), "La Serena", ("Viña del Mar","Viña del Mar"), ("Valparaíso","Valparaíso"), "Santiago de Chile"]),
 }},
 {"kontinent_id": 7, "themengebiet": "Daten und Zufall", "reise": "Australien (nach Bundesstaaten) und Ozeanien", "fluege": {
   60: ("Victoria", "AU", "07", ["Melbourne", ("Cowes (Phillip Island)","Cowes"), "Geelong", "Lorne", "Warrnambool", "Ballarat", "Bendigo"]),
   57: ("South Australia", "AU", "05", ["Adelaide", "Hahndorf", "Victor Harbor", "Kingscote", "Port Augusta", "Coober Pedy"]),
   58: ("Tasmanien", "AU", "06", ["Hobart", "Launceston", "Devonport"]),
   95: ("Western Australia", "AU", "08", ["Perth", "Fremantle", "Margaret River", "Albany", "Esperance", "Kalgoorlie"]),
   "61-1": ("Neuseeland – Nordinsel", "NZ", "NORD", ["Auckland", "Rotorua", "Wellington"]),
   "61-2": ("Salomonen", "SB", None, ["Honiara", "Tulagi", "Auki", "Kirakira"]),
   63: ("Queensland", "AU", "04", ["Gold Coast", "Brisbane", "Noosa Heads", "Hervey Bay", "Bundaberg", "Rockhampton", "Mackay", "Airlie Beach", "Townsville", "Cairns", "Port Douglas"]),
   62: ("New South Wales", "AU", "02", ["Sydney", "Wollongong", ("Katoomba","Katoomba"), "Bathurst", "Dubbo", "Tamworth", "Coffs Harbour", "Port Macquarie", "Newcastle"]),
   64: ("Northern Territory", "AU", "03", ["Darwin", "Jabiru", "Katherine", "Tennant Creek", "Alice Springs", "Yulara"]),
   81: ("Neuseeland – Südinsel", "NZ", "SUED", ["Picton", ("Kaikōura","Kaikoura"), "Christchurch", "Dunedin", "Queenstown"]),
   59: ("Fidschi", "FJ", None, ["Nadi", "Lautoka", "Sigatoka", ("Navua (Pacific Harbour)","Navua"), "Suva"]),
   79: ("Vanuatu", "VU", None, [("Port Vila","Port-Vila"), "Luganville", "Norsup", "Lakatoro", "Isangel"]),
   80: ("Papua-Neuguinea", "PG", None, ["Port Moresby", "Lae", "Madang", "Goroka", "Mount Hagen"]),
 }},
 {"kontinent_id": 8, "themengebiet": "Entdecker-Inseln", "reise": "Pazifik", "fluege": {
   65: ("Französisch-Polynesien", "PF", None, ["Papeete", "Afareaitu", "Fare", "Uturoa", "Vaitape"]),
   84: ("Hawaii", "US", "HI", ["Honolulu", "Kailua", "Kahului", "Hilo", ("Līhuʻe","Lihue")]),
   66: ("Samoa", "WS", None, ["Apia", "Leulumoega", "Mulifanua", "Palauli", "Asau"]),
   70: ("Tonga", "TO", None, [("Nukuʻalofa","Nuku'alofa"), "Kolonga", "Pangai", "Neiafu", ("ʻOhonua","Ohonua")]),
 }},
]

# Landesteile: GeoNames-admin1-Codes (Prüfung „Stadt liegt im Landesteil“) und Natural-Earth-Kürzel (Mittelpunkt)
REGIONEN = {
 "02": {"admin1": {"02"}, "ne": ["AU-NSW"], "hauptort": ("Sydney", "Sydney")},
 "03": {"admin1": {"03"}, "ne": ["AU-NT"], "hauptort": ("Darwin", "Darwin")},
 "04": {"admin1": {"04"}, "ne": ["AU-QLD"], "hauptort": ("Brisbane", "Brisbane")},
 "05": {"admin1": {"05"}, "ne": ["AU-SA"], "hauptort": ("Adelaide", "Adelaide")},
 "06": {"admin1": {"06"}, "ne": ["AU-TAS"], "hauptort": ("Hobart", "Hobart")},
 "07": {"admin1": {"07"}, "ne": ["AU-VIC"], "hauptort": ("Melbourne", "Melbourne")},
 "08": {"admin1": {"08"}, "ne": ["AU-WA"], "hauptort": ("Perth", "Perth")},
 "01": {"admin1": {"01"}, "ne": ["AU-ACT"], "hauptort": ("Canberra", "Canberra")},
 "HI": {"admin1": {"HI"}, "ne": ["US-HI"], "hauptort": ("Honolulu", "Honolulu")},
 "NORD": {"admin1": {"E7", "E8", "F1", "F2", "F3", "F6", "F9", "G1", "G2"}, "ne": [], "hauptort": ("Wellington", "Wellington")},
 "SUED": {"admin1": {"E9", "F4", "F5", "F7", "F8", "G3", "G4"}, "ne": [], "hauptort": ("Christchurch", "Christchurch"), "hauptort_art": "größte Stadt (keine Hauptstadt)"},
 # Brasilien nach den amtlichen Großregionen (IBGE); Großregionen haben keine Hauptstadt → größte Stadt
 "BR_SUEDOST": {"admin1": {"27", "21", "15", "08"}, "ne": ["BR-SP", "BR-RJ", "BR-MG", "BR-ES"], "hauptort": ("São Paulo", "São Paulo"), "hauptort_art": "größte Stadt (Großregion)"},
 "BR_SUED": {"admin1": {"18", "26", "23"}, "ne": ["BR-PR", "BR-SC", "BR-RS"], "hauptort": ("Curitiba", "Curitiba"), "hauptort_art": "größte Stadt (Großregion)"},
 "BR_NORDOST": {"admin1": {"05", "30", "06", "22", "17", "02", "28", "20", "13"}, "ne": ["BR-BA", "BR-PE", "BR-CE", "BR-RN", "BR-PB", "BR-AL", "BR-SE", "BR-PI", "BR-MA"], "hauptort": ("Salvador", "Salvador"), "hauptort_art": "größte Stadt (Großregion)"},
 "BR_MITTELWEST": {"admin1": {"07", "29", "14", "11"}, "ne": ["BR-DF", "BR-GO", "BR-MT", "BR-MS"], "hauptort": ("Brasília", "Brasília"), "hauptort_art": "Hauptstadt Brasiliens"},
 "BR_NORD": {"admin1": {"04", "16", "24", "25", "03", "01", "31"}, "ne": ["BR-AM", "BR-PA", "BR-RO", "BR-RR", "BR-AP", "BR-AC", "BR-TO"], "hauptort": ("Manaus", "Manaus"), "hauptort_art": "größte Stadt (Großregion)"},
}

# Neue Teile (Teilung 22.11., 16:20): Art der Nachbarschaft zum ersten Teil – von Hand, im Bericht begründet
NACHBARSCHAFT = {
 "26-2": "Kuba ↔ Jamaika: über die Jamaikastraße (ca. 150 km), keine Landgrenze",
 "29-2": "Kasachstan ↔ Turkmenistan: gemeinsame Landgrenze",
 "44-2": "Ruanda ↔ Burundi: gemeinsame Landgrenze",
 "46-2": "Marokko ↔ Algerien: gemeinsame Landgrenze",
 "46-3": "Marokko ↔ Mauretanien: nur über das umstrittene Westsahara-Gebiet; Nachbar von Teil 2 (Algerien) mit Landgrenze",
 "61-2": "Insel-Ausnahme (kein Nachbarland): Neuseeland – Nordinsel → Salomonen über das Meer; Entscheidung des Nutzers 22.11. 17:05 – keine strittigen Gebiete, Neuseelands Nachbarn sonst belegt",
 "101-2": "Brasilien – Südosten ↔ Brasilien – Mittelwesten: gemeinsame Grenze (Minas Gerais ↔ Goiás/Distrito Federal)",
 "91-2": "Paraguay ↔ Brasilien – Süden: gemeinsame Landgrenze (Ciudad del Este ↔ Foz do Iguaçu)",
}

# Weitere Teilungen sind möglich (lehrplan-lb prüft 2, 57; 101 ist seit LK-D 3 geteilt). Vorgemerkte Nachbarländer – erst eintragen, wenn
# lk_teilung_2211.json die Teilung enthält: Flug-Schlüssel "thema-1" (bisheriges Land) und "thema-2" … (neues Land),
# Städte je Teil in der Etappen-Reihenfolge des Teils, Eintrag in NACHBARSCHAFT; das Neue aus RESERVE nehmen.
VORGEMERKT = {
 2: "Kirgisistan → Tadschikistan (Reserve Asien, gemeinsame Landgrenze)",
 57: "South Australia → KEIN freier Nachbar: WA, NT, QLD, NSW, VIC sind belegt. Möglich: Australian Capital Territory "
     "(Reserve, kein Nachbar, 4 Orte) oder Kangaroo Island als eigener Landesteil – Entscheidung nötig. Adelaide (begonnen) bleibt in Teil 1.",
}

# Städte, die durch die Teilung frei werden – bleiben dem Land als Reserve-Städte
RESERVE_STAEDTE = {
 "Kuba": ["Trinidad", ("Camagüey","Camagüey"), "Santiago de Cuba"],
 "Kasachstan": [("Karaganda","Karaganda"), "Astana", ("Pawlodar","Pavlodar")],
 "Marokko": [("Meknès","Meknès"), "Essaouira", "Agadir", "Ouarzazate", ("Marrakesch","Marrakesh")],
 "Ruanda": ["Nyanza"],
 "Paraguay": [("Concepción","Concepción"), "Pilar", "Villarrica"],
 "Neuseeland – Nordinsel": ["Hamilton", ("Taupō","Taupo"), "Napier"],
 "Salomonen": [("Gizo","Gizo"), "Noro", "Buala"],
 "Brasilien – Mittelwesten": [("Pirenópolis","Pirenopolis"), ("Goiânia","Goiania"), ("Cuiabá","Cuiaba"), "Campo Grande", ("Corumbá","Corumba")],
}

# Reserve-Länder je Kontinent (frei für neue Themen); (Land, ISO, Landesteil, Städte als fahrbare Strecke)
RESERVE = {
 1: [("Portugal", "PT", None, ["Porto", "Braga", "Coimbra", ("Lissabon","Lisbon"), "Sintra", ("Évora","Evora"), "Lagos", "Faro"]),
     ("Schweden", "SE", None, ["Kiruna", "Uppsala", "Stockholm", "Visby", "Kalmar", "Lund", ("Malmö","Malmo"), ("Göteborg","Gothenburg")]),
     ("Tschechien", "CZ", None, [("Prag","Prague"), ("Kuttenberg","Kutna Hora"), ("Krumau","Cesky Krumlov"), ("Pilsen","Pilsen"), ("Karlsbad","Karlovy Vary"), ("Brünn","Brno"), ("Olmütz","Olomouc")]),
     ("Kroatien", "HR", None, ["Zagreb", "Rijeka", "Pula", "Zadar", "Split", "Dubrovnik"]),
     ("Irland", "IE", None, ["Dublin", "Kilkenny", "Cork", "Killarney", "Limerick", "Galway", "Sligo"])],
 2: [("Panama", "PA", None, [("Panama-Stadt","Panama City"), ("Colón","Colon"), ("Penonomé","Penonome"), "Santiago de Veraguas", "David", "Boquete"]),
     ("Dominikanische Republik", "DO", None, ["Santo Domingo", ("San Pedro de Macorís","San Pedro de Macoris"), "La Romana", ("Higüey","Higuey"), "Punta Cana", "Santiago de los Caballeros", "Puerto Plata"]),
     ("El Salvador", "SV", None, ["San Salvador", "Suchitoto", "San Miguel", "La Libertad", "Sonsonate", ("Juayúa","Juayua"), "Santa Ana"])],
 3: [("Tadschikistan", "TJ", None, [("Chudschand","Khujand"), ("Istarawschan","Istaravshan"), ("Pandschakent","Panjakent"), ("Duschanbe","Dushanbe"), ("Bochtar","Bokhtar"), ("Kulob","Kulob"), ("Chorugh","Khorugh")]),
     ("Pakistan", "PK", None, [("Gilgit","Gilgit"), "Peshawar", "Islamabad", "Lahore", "Multan", "Hyderabad", "Karachi"]),
     ("Osttimor", "TL", None, ["Dili", ("Baucau","Baucau"), "Lospalos", "Viqueque", "Same", "Suai", "Maliana"])],
 4: [("Katar", "QA", None, [("Doha","Doha"), ("Ar-Rayyan","Ar Rayyan"), ("Dukhan","Dukhan"), ("Umm Salal Muhammad","Umm Salal Muhammad"), ("Al-Chaur","Al Khor"), ("Al-Wakra","Al Wakrah"), ("Mesaieed","Mesaieed")]),
     ("Kuwait", "KW", None, [("Kuwait-Stadt","Kuwait City"), ("Hawalli","Hawalli"), ("Al-Farwaniya","Al Farwaniyah"), ("Al-Dschahra","Al Jahra"), ("Al-Ahmadi","Al Ahmadi"), ("Fahaheel","Fahaheel")]),
     ("Bahrain", "BH", None, [("Manama","Manama"), ("Muharraq","Muharraq"), ("Sitra","Sitra"), ("Isa Town","Isa Town"), ("Riffa","Riffa"), ("Hamad Town","Hamad Town")]),
     ("Zypern", "CY", None, [("Nikosia","Nicosia"), ("Larnaka","Larnaca"), ("Ayia Napa","Ayia Napa"), ("Paralimni","Paralimni"), ("Limassol","Limassol"), ("Paphos","Paphos")])],
 5: [("Botswana", "BW", None, ["Gaborone", "Lobatse", "Serowe", "Palapye", "Francistown", "Maun", "Kasane"]),
     ("Sambia", "ZM", None, ["Livingstone", "Mongu", "Lusaka", "Kabwe", "Ndola", "Kitwe", "Chipata"]),
     ("Malawi", "MW", None, ["Blantyre", "Zomba", "Mangochi", "Salima", "Lilongwe", "Nkhata Bay", "Mzuzu"])],
 6: [("Brasilien – Nordosten", "BR", "BR_NORDOST", ["Salvador", "Aracaju", ("Maceió","Maceio"), "Recife", "Olinda", ("João Pessoa","Joao Pessoa"), "Natal", "Fortaleza"]),
     ("Brasilien – Norden", "BR", "BR_NORD", [("Macapá","Macapa"), ("Belém","Belem"), ("Santarém","Santarem"), "Manaus", "Boa Vista", "Porto Velho"]),
     ("Suriname", "SR", None, ["Nieuw Nickerie", "Paramaribo", "Lelydorp", "Brownsweg", "Moengo", "Albina"])],
 7: [("Australian Capital Territory", "AU", "01", ["Canberra", "Gungahlin", "Belconnen", "Tuggeranong"]),
     ("Mikronesien", "FM", None, [("Colonia (Yap)","Colonia"), "Weno", "Kolonia", "Palikir", "Tofol", "Lelu"]),
     ("Guam", "GU", None, [("Hagåtña","Hagatna"), ("Tamuning","Tamuning"), ("Dededo","Dededo Village"), ("Yigo","Yigo Village"), ("Mangilao","Mangilao Village"), ("Inarajan","Inarajan Village"), ("Umatac","Umatac Village"), ("Agat","Agat Village")]),
     ("Palau", "PW", None, ["Koror", "Kloulklubed", "Ngerkeai"])],
 8: [("Amerikanisch-Samoa", "AS", None, ["Pago Pago", ("Aūa","Aua"), ("Tāfuna","Tafuna"), "Faleniu", "Vaitogi", "Leone"]),
     ("Wallis und Futuna", "WF", None, ["Mata-Utu", "Liku", "Alele", "Halalo", "Utufua", ("Leava (Futuna)","Leava"), ("Alo (Futuna)","Alo")]),
     ("Tuvalu", "TV", None, ["Funafuti", ("Vaiaku","Vaiaku Village"), ("Fakaifou","Fakaifou Village"), ("Alapi","Alapi Village"), ("Senala","Senala Village"), ("Teone","Teone Village")])],
}

# Deutsche Hauptstadt-Namen je ISO-Code (von Hand; das Prüfskript gleicht mit den GeoNames-Namen der Hauptstadt ab)
HAUPTSTADT_DE = {
 "IT": "Rom", "AT": "Wien", "CH": "Bern", "SI": "Ljubljana", "GR": "Athen", "DE": "Berlin", "BE": "Brüssel", "GB": "London",
 "ES": "Madrid", "FR": "Paris", "NL": "Amsterdam", "PL": "Warschau", "NO": "Oslo", "PT": "Lissabon", "SE": "Stockholm",
 "CZ": "Prag", "HR": "Zagreb", "IE": "Dublin",
 "CA": "Ottawa", "CU": "Havanna", "MX": "Mexiko-Stadt", "US": "Washington, D.C.", "GT": "Guatemala-Stadt", "CR": "San José",
 "JM": "Kingston", "PA": "Panama-Stadt", "DO": "Santo Domingo", "SV": "San Salvador",
 "KH": "Phnom Penh", "VN": "Hanoi", "UZ": "Taschkent", "KZ": "Astana", "KG": "Bischkek", "MN": "Ulaanbaatar", "ID": "Jakarta",
 "IN": "Neu-Delhi", "NP": "Kathmandu", "LK": "Colombo", "BT": "Thimphu", "CN": "Peking", "KR": "Seoul", "MY": "Kuala Lumpur",
 "JP": "Tokio", "TH": "Bangkok", "LA": "Vientiane", "PH": "Manila", "BD": "Dhaka", "TM": "Aschgabat", "TJ": "Duschanbe",
 "PK": "Islamabad", "TL": "Dili",
 "GE": "Tiflis", "TR": "Ankara", "AM": "Jerewan", "IQ": "Bagdad", "IR": "Teheran", "AE": "Abu Dhabi", "SA": "Riad", "OM": "Maskat",
 "JO": "Amman", "AZ": "Baku", "QA": "Doha", "KW": "Kuwait-Stadt", "BH": "Manama", "CY": "Nikosia",
 "TN": "Tunis", "SN": "Dakar", "GH": "Accra", "MA": "Rabat", "TZ": "Dodoma", "RW": "Kigali", "EG": "Kairo", "KE": "Nairobi",
 "ZW": "Harare", "NA": "Windhoek", "ZA": "Pretoria", "MU": "Port Louis", "UG": "Kampala", "MG": "Antananarivo", "BI": "Gitega",
 "DZ": "Algier", "MR": "Nouakchott", "BW": "Gaborone", "ZM": "Lusaka", "MW": "Lilongwe",
 "PE": "Lima", "UY": "Montevideo", "EC": "Quito", "CO": "Bogotá", "AR": "Buenos Aires", "BO": "Sucre", "BR": "Brasília",
 "PY": "Asunción", "CL": "Santiago de Chile", "SR": "Paramaribo",
 "AU": "Canberra", "NZ": "Wellington", "FJ": "Suva", "VU": "Port Vila", "PG": "Port Moresby", "NC": "Nouméa", "SB": "Honiara",
 "PF": "Papeete", "WS": "Apia", "TO": "Nukuʻalofa", "FM": "Palikir", "AS": "Pago Pago", "PW": "Ngerulmud",
 "GU": "Hagåtña", "WF": "Mata-Utu", "TV": "Funafuti",
}
# Wo GeoNames (geonamescache) eine andere oder veraltete Hauptstadt führt: englischer Suchname der richtigen Hauptstadt
HAUPTSTADT_SUCHE = {"KZ": "Astana", "PW": "Ngerulmud", "US": "Washington"}
# Hauptstadt-Fälle mit Mehrdeutigkeit (für den Bericht)
HAUPTSTADT_HINWEIS = {
 "CH": "Bern ist „Bundesstadt“ (keine Hauptstadt im Gesetz)",
 "NL": "Hauptstadt Amsterdam, Regierungssitz Den Haag",
 "BO": "Verfassungs-Hauptstadt Sucre, Regierungssitz La Paz",
 "ZA": "drei Hauptstädte; Pretoria = Regierungssitz",
 "LK": "Amtssitz Sri Jayewardenepura Kotte, größte Stadt Colombo; GeoNames führt Colombo",
 "KZ": "seit 2022 wieder Astana (geonamescache führt noch „Nur-Sultan“)",
 "PW": "Ngerulmud (Melekeok); geonamescache führt „Melekeok“",
 "NC": "französisches Überseegebiet, Hauptort Nouméa", "PF": "französisches Überseegebiet, Hauptort Papeete",
 "AS": "US-Außengebiet, Hauptort Pago Pago", "GU": "US-Außengebiet, Hauptort Hagåtña",
 "WF": "französisches Überseegebiet, Hauptort Mata-Utu", "TV": "Hauptstadt Funafuti (Atoll); Regierungssitz Vaiaku",
}

# Antarktis = Heimat der Expeditionen: je Expedition eine echte Forschungsstation (Betreiberland in Klammern)
EXPEDITIONEN = {
 # Expedition: (Station, Betreiber, Breite, Länge) – Koordinaten aus COMNAP Antarctic Facilities (Stand 2024; frei für Bildung/nicht kommerziell, Quelle „COMNAP 2024“)
 "5-aquarium": ("Palmer-Station", "USA", -64.774167, -64.053056),
 "5-flug_toronto": ("McMurdo-Station", "USA", -77.85, 166.666667),
 "5-kettennachricht": ("Amundsen-Scott-Südpolstation", "USA", -89.983333, 142.266667),
 "5-oase": ("Maitri-Station (Schirmacher-Oase)", "Indien", -70.766834, 11.730783),
 "5-pyramide": ("Princess-Elisabeth-Station", "Belgien", -71.949858, 23.346891),
 "5-roemerstrasse": ("Mario-Zucchelli-Station", "Italien", -74.694807, 164.113268),
 "5-schatzsuche": ("Esperanza-Station", "Argentinien", -63.396959, -56.998054),
 "5-uhrturm": ("Halley-VI-Station", "Vereinigtes Königreich", -75.571111, -25.473889),
 "5-wetterstation": ("Neumayer-Station III", "Deutschland", -70.660516, -8.284148),
 "5-zeltplatz": ("Kohnen-Station", "Deutschland", -75.001909, 0.066336),
 "8-garten": ("Troll-Station", "Norwegen", -72.011946, 2.53307),
 "8-handytarif": ("Rothera-Station", "Vereinigtes Königreich", -67.569529, -68.124888),
 "8-kerzen": ("Wostok-Station", "Russland", -78.464182, 106.836882),
 "8-klassenfahrt": ("Dumont-d’Urville-Station", "Frankreich", -66.662833, 140.001333),
 "8-pool": ("Davis-Station", "Australien", -68.575938, 77.969516),
 "8-radtour": ("Casey-Station", "Australien", -66.282343, 110.526792),
 "8-roller": ("Mawson-Station", "Australien", -67.602644, 62.873028),
 "8-saftbar": ("Syowa-Station", "Japan", -69.004122, 39.581836),
 "8-schuelerzeitung": ("Zhongshan-Station", "China", -69.373206, 76.371871),
 "8-schulfest": ("Arctowski-Station", "Polen", -62.159773, -58.473322),
 "8-zelt": ("Scott Base", "Neuseeland", -77.849437, 166.767281),
}
