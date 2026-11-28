T = "geometrie.winkelsaetze"
R = "id.geometrie.winkel"
# ───────── scheitel_neben ─────────
neu(T, "scheitel_neben", "anwenden", Z(
    "Zwei gerade Straßen kreuzen sich. Einer der vier Winkel zwischen ihnen misst 83°. Wie groß ist jeder der beiden Winkel, die an diesen Winkel angrenzen?",
    97, "180 - 83", "180 - 83", "Winkel, die nebeneinander an einer Geraden liegen, bilden zusammen einen gestreckten Winkel.",
    "Die angrenzenden Winkel sind Nebenwinkel des 83°-Winkels. Nebenwinkel ergeben zusammen 180°: 180° − 83° = 97°.",
    [B("83", "den Scheitelwinkel genannt statt des Nebenwinkels", "fb.winkel.neben_statt_scheitel"), B("360 - 83", "vom ganzen Kreis (360°) abgezogen", "fb.winkel.teil_der_drehung"), B("90 - 83", "von 90° statt von 180° abgezogen")], einheit="°"), g="einkleidung", regel=R)
neu(T, "scheitel_neben", "lueckenweg", L(
    "Zwei Geraden schneiden sich. Der Winkel α ist dreimal so groß wie sein Nebenwinkel β. Zusammen ergeben α und β ①°. Dann ist β = ②° und α = ③°.",
    "① = □; ② = □; ③ = □", [180, 45, 135], ["180", "{1} / 4", "{1} - {2}"], ["180", "45", "135"],
    "Nebenwinkel liegen nebeneinander an einer Geraden. Wenn α das Dreifache von β ist, besteht die Summe aus 4 gleich großen Teilen.",
    "Nebenwinkel ergeben 180°. Die Summe besteht aus 3 Teilen für α und 1 Teil für β, zusammen 4 Teile. β = 180° : 4 = 45°. α = 180° − 45° = 135° (das ist 3 · 45°).",
    {0: [(360, "fb.winkel.teil_der_drehung", "die Summe der Nebenwinkel mit dem Vollwinkel verwechselt", "360")], 1: [(60, None, "die Summe nur durch 3 geteilt", "{1} / 3")], 2: [(90, None, "die Hälfte der Summe als α genommen", "{1} / 2")]}), g="direkt", regel=R)
# ───────── stufen_wechsel ─────────
neu(T, "stufen_wechsel", "anwenden", Z(
    "Die Geraden g und h sind parallel. Die Gerade q schneidet beide. An g liegt ein Winkel α = 73°. Sein Wechselwinkel an h heißt β, und der Nebenwinkel von β heißt γ. Wie groß ist γ?",
    107, "180 - 73", "180 - 73", "Wechselwinkel an Parallelen sind gleich groß. Danach brauchst du noch den Nebenwinkel.",
    "Wechselwinkel an Parallelen sind gleich groß: β = α = 73°. Der Nebenwinkel von β ergänzt zu 180°: γ = 180° − 73° = 107°.",
    [B("73", "nur den Wechselwinkel β angegeben"), B("180 + 73", "zu 180° addiert statt subtrahiert"), B("90 - 73", "von 90° statt von 180° abgezogen")], einheit="°"), g="mehrschritt", regel=R)
neu(T, "stufen_wechsel", "fehler_detektiv", FD(
    "Die Geraden g und h sind parallel, q schneidet beide. Der Winkel α an g misst 68°. Kim bestimmt weitere Winkel an h:",
    [("α und β sind Stufenwinkel, also gilt β = 68°.", True, True),
     ("Der Winkel γ ist der Nebenwinkel von β, also gilt γ = 68°.", False, True),
     ("Der Winkel δ ist der Scheitelwinkel von γ, also gilt δ = 68°.", True, True)],
    "Nebenwinkel liegen nebeneinander an einer Geraden. Wie groß ist die Summe zweier Nebenwinkel?",
    "Nebenwinkel ergeben zusammen 180°, also γ = 180° − 68° = 112°. Der Fehler steckt in Zeile 2. Zeile 3 ist richtig weitergerechnet: Scheitelwinkel sind gleich groß, δ = γ. Mit dem richtigen γ wäre δ = 112°.",
    rueck={2: "Diese Zeile ist für sich richtig: Scheitelwinkel sind gleich groß. Der Fehler steckt schon in Zeile 2, deshalb stimmt auch δ nicht."}), g="fehler", regel=R)
# ───────── parallel_pruefen ─────────
neu(T, "parallel_pruefen", "anwenden", W(
    "Zwei Wanderwege werden von einem Querweg geschnitten. Kim misst zwei Stufenwinkel: 78° und 82°. Was folgt daraus?",
    "Die Wege sind nicht parallel, denn Stufenwinkel an Parallelen müssten gleich groß sein.",
    [("Die Wege sind parallel, denn 78° und 82° liegen nur 4° auseinander.", "ein kleiner Unterschied reicht nicht, Stufenwinkel müssen genau gleich sein"), ("Die Wege sind parallel, denn 78° + 82° = 160° liegt nahe bei 180°.", "die Summe geprüft, die nur bei Nebenwinkeln wichtig ist"),
     ("Man kann nichts sagen, weil nur zwei Winkel gemessen wurden.", "zwei gemessene Stufenwinkel reichen für die Prüfung")],
    "Prüfe: Müssen gleich liegende Stufenwinkel bei parallelen Geraden gleich groß sein?",
    "Bei parallelen Geraden sind Stufenwinkel gleich groß. Hier ist 78° ≠ 82°. Deshalb sind die beiden Wege nicht parallel.",
    lambda: 78 != 82 and 78 + 82 == 160), g="einkleidung", regel=R)
neu(T, "parallel_pruefen", "umkehren", Z(
    "Die Geraden g und h werden von einer Geraden q geschnitten. Ein Paar Wechselwinkel misst (5x − 20)° und (3x + 14)°. Für welchen Wert von x sind g und h parallel?",
    17, "34 // 2", next(x for x in range(1, 100) if 5 * x - 20 == 3 * x + 14), "Parallel heißt: Die Wechselwinkel sind gleich groß. Stelle eine Gleichung auf und löse sie.",
    "Parallele Geraden haben gleich große Wechselwinkel: 5x − 20 = 3x + 14. Es folgt 2x = 34 und x = 17. Probe: Beide Winkel messen 65°.",
    [B("34", "bei 2x = 34 nicht durch 2 geteilt"), B("20 / 2", "die Zahlen 14 und 20 falsch zusammengefasst und halbiert"), B("(180 + 20 - 14) / 8", "die Winkel zu 180° ergänzt, als wären es Nebenwinkel")], einheit=None), g="pruefung", regel=R)
# ───────── innenwinkelsumme ─────────
neu(T, "innenwinkelsumme", "anwenden", Z(
    "Drei Wanderwege bilden ein Dreieck. Die Winkel verhalten sich wie 5 : 6 : 7. Wie groß ist der größte Winkel in Grad?",
    70, "180 * 7 / (5 + 6 + 7)", "7 * 180 // 18", "Die Winkelsumme im Dreieck ist 180°. Wie viele gleich große Teile entstehen insgesamt?",
    "Es sind 5 + 6 + 7 = 18 Teile. Ein Teil ist 180° : 18 = 10°. Der größte Winkel hat 7 Teile: 7 · 10° = 70°.",
    [B("180 / 7", "den Winkelsatz vergessen und 180° durch die größte Zahl geteilt"), B("180 / 18", "nur einen Teil ausgerechnet"), B("360 * 7 / 18", "mit 360° statt 180° gerechnet")], einheit="°"), g="mehrschritt", regel=R)
neu(T, "innenwinkelsumme", "verfahren_waehlen", W(
    "Welche Begründung zeigt für jedes Dreieck, dass die Winkelsumme 180° beträgt?",
    "Man zeichnet durch eine Ecke die Parallele zur gegenüberliegenden Seite. Wechselwinkel zeigen, dass die drei Winkel zusammen einen gestreckten Winkel bilden.",
    [("Kim hat in drei Dreiecken die Winkel gemessen und jedes Mal etwa 180° erhalten.", "Messen an Beispielen beweist nichts für jedes Dreieck"), ("Ein Dreieck hat drei Ecken, und 3 · 60° = 180°.", "gilt nur für das gleichseitige Dreieck")],
    "Ein Beweis muss für jedes Dreieck gelten und sich auf bekannte Sätze stützen, etwa Wechselwinkel an Parallelen.",
    "Die Parallele durch eine Ecke bildet mit den Dreiecksseiten zwei Paare von Wechselwinkeln. Zusammen mit dem dritten Winkel liegen alle drei Winkel an einer Geraden und ergeben 180°. Das gilt für jedes Dreieck. Messungen und der Sonderfall des gleichseitigen Dreiecks zeigen das nicht allgemein.",
    lambda: 3 * 60 == 180), g="begruenden", regel=R)
# ───────── aussenwinkel ─────────
neu(T, "aussenwinkel", "anwenden", Z(
    "Ein Dreieck ABC hat die Innenwinkel α = 47° und β = 65°. Kim verlängert die Seite [AC] über C hinaus. Wie groß ist der Außenwinkel an C, der an γ angrenzt?",
    112, "47 + 65", "180 - (180 - 47 - 65)", "Der Außenwinkel ist so groß wie die beiden Innenwinkel zusammen, die nicht an ihm liegen.",
    "Der Außenwinkel an C ist so groß wie die beiden anderen Innenwinkel zusammen: 47° + 65° = 112°. Probe: γ = 180° − 47° − 65° = 68°, und 180° − 68° = 112°.",
    [B("47 + 65 + 68", "alle drei Innenwinkel addiert"), B("180 - 47 - 65", "den Innenwinkel γ statt des Außenwinkels angegeben"), B("65 - 47", "die beiden Winkel subtrahiert")], einheit="°"), g="einkleidung", regel=R)
neu(T, "aussenwinkel", "lueckenweg", L(
    "In einem Dreieck misst der Innenwinkel α genau 38°, und der Außenwinkel an C misst 121°. Nach dem Außenwinkelsatz ist β = ①°. Der Innenwinkel an C ist ②°. Alle drei Innenwinkel zusammen sind ③°.",
    "① = □; ② = □; ③ = □", [83, 59, 180], ["121 - 38", "180 - 121", "38 + {1} + {2}"], ["83", "59", "180"],
    "Der Außenwinkel ist so groß wie die beiden nicht anliegenden Innenwinkel zusammen. Der Innenwinkel an C ist sein Nebenwinkel.",
    "β = 121° − 38° = 83°. Der Innenwinkel an C ist der Nebenwinkel des Außenwinkels: 180° − 121° = 59°. Die Summe 38° + 83° + 59° = 180° bestätigt die Rechnung.",
    {0: [(159, None, "die beiden Winkel addiert", "121 + 38")], 1: [(121, "fb.winkel.neben_statt_scheitel", "den Außenwinkel selbst als Innenwinkel genommen", "121")], 2: [(242, None, "den Außenwinkel noch einmal dazugezählt", "38 + {1} + {2} + 62")]}), g="direkt", regel=R)
# ───────── vieleck ─────────
neu(T, "vieleck", "anwenden", Z(
    "Ein Gartenhaus hat als Grundriss ein regelmäßiges Zwölfeck. Wie groß ist jeder Innenwinkel des Grundrisses in Grad?",
    150, "(12 - 2) * 180 / 12", "180 - 360 / 12", "Wie groß ist die Winkelsumme im Zwölfeck? Wie viele gleich große Winkel hat es?",
    "Die Winkelsumme im Zwölfeck ist (12 − 2) · 180° = 1 800°. Alle 12 Winkel sind gleich groß: 1 800° : 12 = 150°.",
    [B("12 * 180 / 12", "die Winkelsumme mit n statt mit n − 2 Dreiecken gerechnet"), B("(12 - 2) * 180", "die Winkelsumme angegeben statt eines einzelnen Winkels"), B("360 / 12", "den Außenwinkel statt des Innenwinkels angegeben")], einheit="°"), g="einkleidung", regel=R)
neu(T, "vieleck", "umkehren", Z(
    "Die Winkelsumme eines Vielecks beträgt 2 340°. In wie viele Dreiecke lässt sich das Vieleck von einer Ecke aus zerlegen?",
    13, "2340 // 180", next(n - 2 for n in range(3, 60) if (n - 2) * 180 == 2340), "Jedes Dreieck bringt 180° zur Winkelsumme. Wie oft passen 180° in 2 340°?",
    "Bei der Zerlegung von einer Ecke aus entstehen (n − 2) Dreiecke, jedes bringt 180°. Aus (n − 2) · 180° = 2 340° folgt n − 2 = 13. Es sind 13 Dreiecke.",
    [B("13 + 2", "die Zahl der Ecken statt der Dreiecke angegeben"), B("2340 / 360", "durch 360° statt durch 180° geteilt"), B("2340 / 180 - 1", "n − 1 Dreiecke statt n − 2")], einheit="Dreiecke"), g="rueckwaerts", regel=R)
# ───────── parkett ─────────
neu(T, "parkett", "anwenden", Z(
    "Ein Platz in Lissabon wird mit zwei regelmäßigen Zwölfecken und einer dritten Sorte regelmäßiger Vielecke so gepflastert, dass sich um jeden Eckpunkt genau diese drei Vielecke lückenlos treffen. Wie groß ist der Innenwinkel der dritten Sorte in Grad?",
    60, "360 - 2 * (12 - 2) * 180 / 12", "360 - 2 * 150", "Wie groß ist der Innenwinkel eines regelmäßigen Zwölfecks? Um einen Punkt herum ergeben alle Winkel 360°.",
    "Der Innenwinkel des regelmäßigen Zwölfecks ist 150°. Zwei davon sind 300°. Es fehlen 360° − 300° = 60°. Das ist der Innenwinkel eines gleichseitigen Dreiecks.",
    [B("360 - 150", "nur ein Zwölfeck abgezogen"), B("360 - 2 * 30", "den Außenwinkel 30° statt des Innenwinkels abgezogen"), B("360 / 3", "den Vollwinkel einfach durch 3 geteilt")], einheit="°"), g="mehrschritt", regel=R)
neu(T, "parkett", "verfahren_waehlen", W(
    "Kim sagt: „Mit regelmäßigen Fünfecken allein kann man den Boden lückenlos auslegen, denn 360° : 5 = 72° ist eine ganze Zahl.“ Welche Prüfung ist richtig?",
    "Der Innenwinkel des regelmäßigen Fünfecks ist 108°. Die Zahl 360 lässt sich nicht ganzzahlig durch 108 teilen. Die Fünfecke passen nicht lückenlos.",
    [("Die Prüfung stimmt: 360° wird durch die Zahl der Ecken geteilt, das geht auf.", "die Zahl der Ecken statt den Innenwinkel genommen"), ("Der Innenwinkel ist 72°, und 360° : 72° = 5. Die Fünfecke passen lückenlos.", "den Außenwinkel als Innenwinkel gelesen"),
     ("Der Innenwinkel ist 108°. Weil 108° + 108° + 108° = 324° fast 360° ergibt, passen sie nach etwas Schieben.", "ein Rest bleibt, es ist kein lückenloses Auslegen")],
    "Entscheidend ist der Innenwinkel der Fläche, nicht die Zahl der Ecken. Teilt er 360° ohne Rest?",
    "Der Innenwinkel des regelmäßigen Fünfecks ist (5 − 2) · 180° : 5 = 108°. 360° : 108° ist nicht ganzzahlig (3,33 ...). Um einen Punkt bleibt eine Lücke. Fünfecke allein passen nicht lückenlos.",
    lambda: (5 - 2) * 180 / 5 == 108 and 360 % 108 != 0 and 360 / 5 == 72), g="pruefung", regel=R)
# ───────── figuren ─────────
neu(T, "figuren", "anwenden", Z(
    "Ein Segel hat die Form eines Vierecks ABCD mit α = 80°, β = 95° und γ = 70°. Die Seite [AD] wird über D hinaus verlängert. Wie groß ist der Winkel, den die Verlängerung mit [DC] einschließt?",
    65, "180 - (360 - 80 - 95 - 70)", "80 + 95 + 70 - 180", "Berechne zuerst δ im Viereck. Die Verlängerung bildet mit [DA] einen gestreckten Winkel.",
    "Die Winkelsumme im Viereck ist 360°. δ = 360° − 80° − 95° − 70° = 115°. Die Verlängerung von [AD] und die Seite [DA] liegen auf einer Geraden, der gesuchte Winkel ist der Nebenwinkel von δ: 180° − 115° = 65°.",
    [B("360 - 80 - 95 - 70", "den Innenwinkel δ statt seines Nebenwinkels angegeben"), B("180 - 80 - 95 - 70", "im Viereck mit der Winkelsumme 180° gerechnet"), B("360 - 115", "von 360° statt von 180° abgezogen")], einheit="°"), g="mehrschritt", regel=R)
neu(T, "figuren", "anwenden", Z(
    "In einem Trapez ABCD mit AB ∥ CD gilt α = 70° und β = 80°. Wie groß ist die Summe der beiden Winkel γ und δ?",
    210, "(180 - 80) + (180 - 70)", "360 - 70 - 80", "Winkel an den beiden Schenkeln zwischen den Parallelen ergeben jeweils 180°.",
    "Zwischen den Parallelen AB und CD gilt: α + δ = 180° und β + γ = 180°. Also δ = 110° und γ = 100°, zusammen 210°. Probe über die Winkelsumme im Viereck: 360° − 70° − 80° = 210°.",
    [B("180 - 70 + 80", "nur einen der beiden Winkel richtig ergänzt"), B("70 + 80", "α und β addiert statt γ und δ bestimmt"), B("360 - 70", "nur α von der Winkelsumme abgezogen")], einheit="°"), g="verknuepfen", regel=R)
# ───────── beweisen ─────────
neu(T, "beweisen", "bruecke", W(
    "Du willst beweisen, dass die Winkelsumme in jedem Viereck 360° beträgt. Welcher Ablauf ist ein richtiger Beweis?",
    "Man zeichnet eine Diagonale und zerlegt das Viereck in zwei Dreiecke. Jedes Dreieck hat die Winkelsumme 180°. Die Winkel der Dreiecke bilden zusammen die Viereckswinkel: 180° + 180° = 360°.",
    [("Man misst bei einem Viereck alle Winkel und addiert. Es kommt 360° heraus, also gilt es immer.", "Messen an einem Beispiel beweist nichts"), ("Ein Viereck hat 4 Ecken. Jede Ecke hat 90°. Also 4 · 90° = 360°.", "gilt nur für das Rechteck oder Quadrat"),
     ("Man zeichnet beide Diagonalen. Es entstehen 4 Dreiecke zu je 180°, also 4 · 180° = 720° für das Viereck.", "die Winkel am Schnittpunkt der Diagonalen wurden mitgezählt")],
    "Ein Beweis gilt für jedes Viereck. Welcher Satz über Dreiecke kann dabei helfen?",
    "Eine Diagonale zerlegt jedes Viereck in zwei Dreiecke. Die Winkel der Dreiecke ergeben genau die vier Winkel des Vierecks: 2 · 180° = 360°. Der Ablauf stützt sich auf den bekannten Satz über die Winkelsumme im Dreieck.",
    lambda: 2 * 180 == 360 and 4 * 180 == 720), g="darstellung", regel=R)
neu(T, "beweisen", "fehler_detektiv", FD(
    "Alex beweist, dass die drei Außenwinkel eines Dreiecks zusammen 360° ergeben, und schreibt auf:",
    [("An jeder Ecke ergeben Innenwinkel und Außenwinkel zusammen 180°.", True, True),
     ("An den drei Ecken ergibt das 3 · 180° = 540°.", True, True),
     ("Die drei Innenwinkel ergeben zusammen 180°.", True, True),
     ("Die Außenwinkel ergeben also die Summe aus den 540° und den 180° der Innenwinkel, das sind 720°.", False, False)],
    "Von den 540° gehören 180° zu den Innenwinkeln. Was bleibt für die Außenwinkel übrig?",
    "Von den 540° gehören 180° zu den Innenwinkeln. Die Außenwinkel sind der Rest: 540° − 180° = 360°. Alex hat in Zeile 4 addiert statt subtrahiert. Die Zeilen 1 bis 3 sind richtig."), g="fehler", regel=R)
