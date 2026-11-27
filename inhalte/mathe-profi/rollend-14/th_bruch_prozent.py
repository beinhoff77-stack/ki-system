T = "bruch.prozent"
# ───────── prozent_bedeutung ─────────
a1(T, "prozent_bedeutung", Z(
    "Der Ladebalken eines Tablets ist zu 3/5 gefüllt. Wie viel Prozent sind das?",
    60, "3 / 5 * 100", "3 * 20", "Prozent heißt Hundertstel. Erweitere den Bruch auf den Nenner 100.",
    "3/5 = 60/100 (mit 20 erweitert). 60/100 sind 60 %. Der Akku ist zu 60 % geladen.",
    [B("3 / 5", "als Dezimalzahl 0,6 angegeben und nicht in Prozent umgerechnet"), B("3 * 5", "Zähler und Nenner malgenommen"), B("3 * 10", "mit 10 statt mit 20 erweitert")], "%"))
a2(T, "prozent_bedeutung", Z(
    "Ein Fruchtsaft besteht zu 35 % aus Orangensaft und zu 0,4 aus Apfelsaft. Der Rest ist Wasser. Wie viel Prozent des Safts sind Wasser?",
    25, "100 - 35 - 0.4 * 100", "100 - 75", "Schreibe alle Anteile als Prozentzahlen. Der ganze Saft sind 100 %.",
    "0,4 = 40/100 = 40 %. Orangensaft und Apfelsaft zusammen: 35 % + 40 % = 75 %. Wasser: 100 % − 75 % = 25 %.",
    [B("100 - 35 - 0.4", "0,4 als 0,4 % statt als 40 % gelesen"), B("100 - 35", "den Apfelsaft vergessen"), B("35 + 40", "die beiden Anteile angegeben statt den Rest")], "%"))
a3(T, "prozent_bedeutung", Z(
    "Eine Wanderstrecke ist 80 m lang. Davon sind 0,25 asphaltiert und 15 % geschottert. Ein Fünftel der Strecke ist Wiese. Der Rest ist ein Waldweg. Wie viele Meter ist der Waldweg lang?",
    32, "80 * (1 - 0.25 - 15 / 100 - 1 / 5)", "80 * 40 / 100", "Schreibe alle Anteile als Prozent. Wie viel Prozent bleiben für den Waldweg?",
    "0,25 = 25 %, 15 %, 1/5 = 20 %. Zusammen 25 % + 15 % + 20 % = 60 %. Der Waldweg ist 40 % der Strecke: 40 % von 80 m = 0,4 · 80 = 32 m.",
    [B("80 * (1 - 0.25 - 0.15 - 0.5)", "ein Fünftel als 0,5 gelesen"), B("80 * (0.25 + 0.15 + 1 / 5)", "den befestigten Teil statt des Waldwegs berechnet"), B("100 - 60", "den Anteil 40 % als 40 m angegeben")], "m"), g="verknuepfen")
# ───────── prozentwert ─────────
a1(T, "prozentwert", Z(
    "In einer Schule mit 480 Kindern fahren 35 % mit dem Fahrrad zur Schule. Wie viele Kinder fahren mit dem Fahrrad?",
    168, "480 * 35 / 100", "480 / 100 * 35", "Berechne zuerst 1 % der Kinder. Nimm das Ergebnis mal 35.",
    "1 % von 480 sind 4,8 Kinder. 35 % sind 35 · 4,8 = 168 Kinder. Probe: 168 : 480 = 0,35.",
    [B("480 * 0.035", "35 % als 0,035 gerechnet"), B("480 - 168", "die Kinder ohne Fahrrad angegeben"), B("480 / 35", "durch 35 geteilt statt mit 35 % gerechnet")], "Kinder"))
a2(T, "prozentwert", Z(
    "Ein Obsthändler hat 250 kg Äpfel. 12 % davon sind angefault und werden aussortiert. Wie viele Kilogramm Äpfel kann er verkaufen?",
    220, "250 - 250 * 12 / 100", "250 * 88 / 100", "Berechne zuerst, wie viele Kilogramm aussortiert werden. Oder: Wie viel Prozent bleiben?",
    "Aussortiert: 12 % von 250 kg = 30 kg. Es bleiben 250 − 30 = 220 kg. Oder: 88 % von 250 kg = 220 kg.",
    [B("250 * 12 / 100", "die aussortierten Äpfel statt der verkaufbaren angegeben"), B("250 - 12", "12 kg statt 12 % abgezogen"), B("250 + 250 * 12 / 100", "die aussortierten Äpfel dazugezählt")], "kg"))
a3(T, "prozentwert", Z(
    "In einem Chor mit 40 Kindern sind 60 % Mädchen. Von den Mädchen singen 25 % Alt. Wie viele Mädchen singen Alt?",
    6, "40 * 60 / 100 * 25 / 100", "24 / 4", "Bestimme zuerst, wie viele Mädchen im Chor sind. Von dieser Zahl nimmst du dann 25 %.",
    "Mädchen: 60 % von 40 = 24. Davon 25 % = ein Viertel von 24 = 6. Sechs Mädchen singen Alt. Wichtig: Die 25 % beziehen sich auf die Mädchen, nicht auf alle 40 Kinder.",
    [B("40 * 25 / 100", "25 % von allen 40 Kindern genommen"), B("40 * (60 + 25) / 100", "die beiden Prozentsätze addiert"), B("40 * 60 / 100", "nur die Zahl der Mädchen angegeben")], "Mädchen"), g="verknuepfen")
# ───────── prozentsatz ─────────
a1(T, "prozentsatz", Z(
    "Noa löst in einem Test 34 von 40 Aufgaben richtig. Wie viel Prozent der Aufgaben hat Noa richtig gelöst?",
    85, "34 / 40 * 100", "34 * 2.5", "Teile die richtigen Aufgaben durch alle Aufgaben. Dann rechnest du in Prozent um.",
    "34 : 40 = 0,85 = 85 %. Oder: 34/40 = 85/100 = 85 %.",
    [B("34 / 40", "als Dezimalzahl angegeben und nicht in Prozent umgerechnet"), B("6 / 40 * 100", "die Fehler statt der richtigen Aufgaben genommen"), B("40 - 34", "die Zahl der Fehler angegeben")], "%"))
a2(T, "prozentsatz", Z(
    "Der Preis einer Eintrittskarte steigt von 250 € auf 280 €. Um wie viel Prozent ist der Preis gestiegen?",
    12, "(280 - 250) / 250 * 100", "30 / 2.5", "Wie viel Euro ist der Preis gestiegen? Auf welchen Preis bezieht sich der Prozentsatz?",
    "Die Erhöhung ist 280 − 250 = 30 €. Bezogen auf den alten Preis: 30 : 250 = 0,12 = 12 %.",
    [B("280 - 250", "die Erhöhung in Euro als Prozentsatz angegeben"), B("280 / 250 * 100", "den neuen Preis in Prozent des alten Preises angegeben"), B("(280 - 250) / 250", "als Dezimalzahl angegeben und nicht in Prozent umgerechnet")], "%"))
a3(T, "prozentsatz", Z(
    "Bei einer Umfrage unter 150 Kindern wählen 36 Kinder „Fußball“ und 45 Kinder „Schwimmen“. Alle anderen Kinder wählen „Sonstiges“. Wie viel Prozent der Kinder haben „Sonstiges“ gewählt?",
    46, "(150 - 36 - 45) / 150 * 100", "100 - 24 - 30", "Wie viele Kinder haben „Sonstiges“ gewählt? Bezogen auf wie viele Kinder?",
    "Sonstiges: 150 − 36 − 45 = 69 Kinder. 69 : 150 = 0,46 = 46 %. Kontrolle: Fußball 24 %, Schwimmen 30 %, Sonstiges 46 %, zusammen 100 %.",
    [B("(36 + 45) / 150 * 100", "den Anteil von Fußball und Schwimmen statt von Sonstiges berechnet"), B("150 - 36 - 45", "die Zahl der Kinder als Prozentzahl angegeben"), B("100 - 36 - 45", "die Zahlen der Kinder von 100 abgezogen")], "%"), g="verknuepfen")
# ───────── grundwert ─────────
a1(T, "grundwert", Z(
    "In einem Orchester spielen 18 Kinder Geige. Das sind 30 % aller Kinder im Orchester. Wie viele Kinder spielen insgesamt im Orchester?",
    60, "18 / 30 * 100", "18 * 10 / 3", "Wenn 30 % die Zahl 18 sind: Wie viele Kinder sind 1 %? Wie viele sind 100 %?",
    "30 % sind 18 Kinder. 1 % sind 18 : 30 = 0,6 Kinder. 100 % sind 0,6 · 100 = 60 Kinder. Probe: 30 % von 60 = 18.",
    [B("18 * 30 / 100", "30 % von 18 gerechnet statt des Grundwerts"), B("18 + 30", "die beiden Zahlen addiert"), B("18 * 30", "die beiden Zahlen malgenommen")], "Kinder"))
a2(T, "grundwert", Z(
    "In einem Wald sind 144 Bäume Buchen. Das sind 45 % aller Bäume. 15 % aller Bäume im Wald sind erkrankt. Wie viele Bäume sind erkrankt?",
    48, "144 / 45 * 100 * 15 / 100", "320 * 0.15", "Berechne zuerst, wie viele Bäume es im Wald insgesamt gibt. Danach rechnest du mit 15 %.",
    "45 % sind 144 Bäume, also 1 % = 3,2 Bäume und 100 % = 320 Bäume. 15 % von 320 = 48 Bäume sind erkrankt.",
    [B("144 * 15 / 100", "15 % von den Buchen genommen statt von allen Bäumen"), B("144 / 45 * 100", "nur die Zahl aller Bäume angegeben"), B("144 * 45 / 100", "45 % von 144 gerechnet statt den Grundwert zu bestimmen")], "Bäume"))
a3(T, "grundwert", Z(
    "Ein Dorf ist in den letzten Jahren um 12 % gewachsen. Heute hat es 1 120 Einwohner. Um wie viele Einwohner ist das Dorf gewachsen?",
    120, "1120 - 1120 / 112 * 100", "1000 * 12 / 100", "Heute sind 112 % des früheren Werts. Berechne zuerst die frühere Einwohnerzahl.",
    "Heute: 100 % + 12 % = 112 % sind 1 120 Einwohner. 1 % sind 10 Einwohner, 100 % sind 1 000. Gewachsen ist das Dorf um 1 120 − 1 000 = 120 Einwohner (12 % von 1 000).",
    [B("1120 * 12 / 100", "12 % von der heutigen Einwohnerzahl genommen"), B("1120 / 112 * 100", "die frühere Einwohnerzahl angegeben"), B("1120 - 12", "12 statt 12 % abgezogen")], "Einwohner"), g="rueckwaerts")
# ───────── rabatt_aufschlag ─────────
a1(T, "rabatt_aufschlag", Z(
    "Ein Paar Schuhe kostet 60 €. Beim Schlussverkauf gibt es 15 % Rabatt. Wie viel Euro kosten die Schuhe jetzt?",
    51, "60 * 85 / 100", "60 - 9", "Wie viel Prozent vom alten Preis bezahlst du noch? Oder berechne den Rabatt in Euro und ziehe ihn ab.",
    "Rabatt: 15 % von 60 € = 9 €. Neuer Preis: 60 − 9 = 51 €. Oder: 85 % von 60 € = 51 €.",
    [B("60 * 15 / 100", "den Rabatt in Euro statt des neuen Preises angegeben"), B("60 - 15", "15 € statt 15 % abgezogen"), B("60 * 115 / 100", "den Rabatt aufgeschlagen")], "€"))
a2(T, "rabatt_aufschlag", Z(
    "Ein Händler kauft einen Fernseher für 400 € ein und schlägt 30 % auf. Beim Verkauf gibt er dem Kunden 10 % Rabatt auf den Verkaufspreis. Wie viel Euro zahlt der Kunde?",
    468, "400 * 130 / 100 * 90 / 100", "520 - 52", "Berechne zuerst den Verkaufspreis nach dem Aufschlag. Der Rabatt bezieht sich auf diesen neuen Preis.",
    "Aufschlag: 30 % von 400 € = 120 €, Verkaufspreis 520 €. Rabatt: 10 % von 520 € = 52 €. Der Kunde zahlt 520 − 52 = 468 €.",
    [B("400 * 120 / 100", "30 % Aufschlag und 10 % Rabatt zu 20 % Aufschlag zusammengefasst"), B("400 * 130 / 100", "den Rabatt vergessen"), B("400 * 130 / 100 * 110 / 100", "den Rabatt aufgeschlagen statt abgezogen")], "€"))
a3(T, "rabatt_aufschlag", Z(
    "Alex zahlt für eine Jacke nach einem Rabatt von 25 % genau 90 €. Wie viel Euro hat Alex durch den Rabatt gespart?",
    30, "90 / 75 * 100 - 90", "120 - 90", "Die 90 € sind nicht 100 %. Wie viel Prozent des alten Preises sind 90 €? Berechne den alten Preis.",
    "90 € sind 75 % des alten Preises. 1 % sind 1,20 €, 100 % sind 120 €. Gespart: 120 − 90 = 30 € (das sind 25 % von 120 €).",
    [B("90 * 25 / 100", "25 % vom bezahlten Preis genommen"), B("90 / 75 * 100", "den alten Preis statt der Ersparnis angegeben"), B("90 / 25", "durch 25 geteilt")], "€"), g="rueckwaerts")
# ───────── verstehen ─────────
a1(T, "verstehen", Z(
    "Kim sagt: „Beide Läden geben 20 % Rabatt auf eine Jacke, also spare ich in beiden Läden gleich viel.“ Im Laden A kostet die Jacke 80 €, im Laden B kostet sie 120 €. Wie viel Euro spart man in Laden B mehr als in Laden A?",
    8, "120 * 20 / 100 - 80 * 20 / 100", "24 - 16", "20 % sind immer 20 % von einem Preis. Berechne die Ersparnis für beide Jacken einzeln.",
    "Laden A: 20 % von 80 € = 16 €. Laden B: 20 % von 120 € = 24 €. Unterschied: 24 − 16 = 8 €. Gleiche Prozentzahl heißt nicht gleich viel Euro, wenn die Preise verschieden sind.",
    [B("120 - 80", "den Unterschied der Preise angegeben"), B("20 - 20", "weil beide Prozentsätze gleich sind, einen Unterschied von 0 angenommen"), B("120 * 20 / 100", "nur die Ersparnis in Laden B angegeben")], "€"))
a2(T, "verstehen", Z(
    "Die Mannschaft A gewinnt 12 von 15 Spielen. Die Mannschaft B gewinnt 18 von 25 Spielen. Um wie viele Prozentpunkte ist der Anteil gewonnener Spiele bei A größer als bei B?",
    8, "12 / 15 * 100 - 18 / 25 * 100", "80 - 72", "B hat mehr Spiele gewonnen, hat aber auch mehr gespielt. Vergleiche die Anteile in Prozent.",
    "A: 12 : 15 = 0,8 = 80 %. B: 18 : 25 = 0,72 = 72 %. Unterschied: 80 − 72 = 8 Prozentpunkte. A gewinnt anteilig öfter, obwohl B mehr Siege hat.",
    [B("18 - 12", "die Zahl der Siege verglichen"), B("12 / 15 - 18 / 25", "den Unterschied als Dezimalzahl angegeben und nicht in Prozentpunkten"), B("80 + 72", "die beiden Prozentsätze addiert")], "Prozentpunkte"))
a3(T, "verstehen", Z(
    "Ein Preis von 50 € wird erst um 20 % erhöht. Danach wird der neue Preis um 20 % gesenkt. Kim sagt: „Dann ist der Preis wieder 50 €.“ Wie viel Euro kostet es wirklich am Ende?",
    48, "50 * 120 / 100 * 80 / 100", "60 - 12", "Die zweiten 20 % beziehen sich auf den neuen Preis, nicht auf 50 €. Rechne in zwei Schritten.",
    "Erhöhung: 20 % von 50 € = 10 €, neuer Preis 60 €. Senkung: 20 % von 60 € = 12 €. Endpreis: 60 − 12 = 48 €. Der Preis ist niedriger als am Anfang, weil sich die zweiten 20 % auf den größeren Preis 60 € beziehen.",
    [B("50", "wie Kim angenommen, der Preis sei wieder derselbe"), B("50 * 120 / 100", "nur die Erhöhung gerechnet"), B("50 * 80 / 100", "nur die Senkung gerechnet")], "€"), g="pruefung")
