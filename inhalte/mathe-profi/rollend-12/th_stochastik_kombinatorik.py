T = "stochastik.kombinatorik"
ST = "id.daten.stufen"

# ───────── systematisch ─────────
neu(T, "systematisch", "zwei_wege", Z(
    "Wie viele verschiedene dreibuchstabige Wörter kann man aus den Buchstaben A, B und C bilden, wenn jeder Buchstabe genau einmal vorkommt? Weg A: Schreibe alle Wörter geordnet nach dem Anfangsbuchstaben auf und zähle. Weg B: Rechne: 3 Möglichkeiten für den ersten Platz, dann 2 für den zweiten, dann 1 für den dritten.",
    6, "3 * 2 * 1", "1 + 1 + 1 + 1 + 1 + 1", "Schreibe zuerst alle Wörter mit A am Anfang auf. Wie viele sind es?",
    "Weg A: ABC, ACB, BAC, BCA, CAB, CBA sind 6 Wörter. Weg B: 3 · 2 · 1 = 6.",
    [(3, None, "nur die Möglichkeiten für den ersten Platz gezählt", "3"), (9, None, "3 · 3 gerechnet (Buchstaben dürfen sich wiederholen)", "3 * 3"), (8, None, "2 · 2 · 2 gerechnet", "2 * 2 * 2")], "Wörter"))
neu(T, "systematisch", "umkehren", Z(
    "Ein Kind hat 5 Hosen und 4 T-Shirts. Mit mehreren Jacken kann es genau 60 verschiedene Outfits aus je einer Hose, einem T-Shirt und einer Jacke zusammenstellen. Wie viele Jacken hat es?",
    3, "60 / (5 * 4)", "60 / 20", "Wie viele Outfits gibt es nur mit Hose und T-Shirt? Wie oft passt das in 60?",
    "Hose und T-Shirt ergeben 5 · 4 = 20 Möglichkeiten. Mit der Jacke: 20 · Jacken = 60, also Jacken = 60 : 20 = 3.",
    [(12, None, "nur durch 5 geteilt", "60 / 5"), (15, None, "nur durch 4 geteilt", "60 / 4"), (20, None, "Hosen mal T-Shirts als Zahl der Jacken genommen", "5 * 4")], "Jacken"), g="rueckwaerts")

# ───────── zaehlprinzip ─────────
neu(T, "zaehlprinzip", "umkehren", Z(
    "Eine Eisdiele bietet 6 Eissorten an. Man kann einen Becher mit genau einer Sorte und genau einer Soße bestellen. So gibt es 42 verschiedene Becher. Wie viele Soßen gibt es?",
    7, "42 / 6", "7", "Jede Sorte lässt sich mit jeder Soße zu einem Becher kombinieren. Mache das Malnehmen rückgängig.",
    "Sorten · Soßen = 42, also Soßen = 42 : 6 = 7. Probe: 6 · 7 = 42.",
    [(36, None, "6 von 42 abgezogen", "42 - 6"), (48, None, "6 zu 42 addiert", "42 + 6"), (252, None, "6 · 42 gerechnet", "6 * 42")], "Soßen"), g="umkehr", regel=ST)
neu(T, "zaehlprinzip", "bruecke", Z(
    "Ein Baumdiagramm hat in der ersten Stufe 3 Äste. An jedem dieser Äste gibt es in der zweiten Stufe 2 Äste und an jedem davon in der dritten Stufe 4 Äste. Wie viele Pfade führen von der Wurzel bis zu den Enden?",
    24, "3 * 2 * 4", "3 * 8", "Jeder Pfad geht durch alle drei Stufen. Wie viele Möglichkeiten gibt es in jeder Stufe?",
    "Die Zahl der Pfade ist das Produkt der Astzahlen: 3 · 2 · 4 = 24.",
    [(9, None, "die Astzahlen addiert", "3 + 2 + 4"), (6, None, "nur die ersten beiden Stufen gezählt", "3 * 2"), (12, None, "die zweite Stufe vergessen: 3 · 4", "3 * 4")], "Pfade"), g="verknuepfen", regel=ST)

# ───────── reihenfolgen ─────────
neu(T, "reihenfolgen", "zwei_wege", Z(
    "Auf wie viele Arten können 4 Kinder in einer Reihe stehen? Weg A: Wähle nacheinander das Kind für den 1., 2., 3. und 4. Platz und multipliziere die Möglichkeiten. Weg B: Schreibe zuerst alle Reihenfolgen für 3 Kinder auf (es sind 6) und überlege, an wie vielen Stellen das vierte Kind eingefügt werden kann.",
    24, "4 * 3 * 2 * 1", "6 * 4", "Wenn 3 Kinder in einer Reihe stehen: An wie vielen Stellen kann sich ein viertes Kind einreihen (auch ganz vorn und ganz hinten)?",
    "Weg A: 4 · 3 · 2 · 1 = 24. Weg B: Bei jeder der 6 Reihenfolgen von 3 Kindern kann das vierte Kind an 4 Stellen stehen (vorn, zwei Lücken, hinten): 6 · 4 = 24.",
    [(10, None, "die Zahlen von 1 bis 4 addiert", "4 + 3 + 2 + 1"), (16, None, "4 · 4 gerechnet", "4 * 4"), (12, None, "nur an 2 Stellen eingefügt: 6 · 2", "6 * 2")], "Möglichkeiten"))
neu(T, "reihenfolgen", "anwenden", Z(
    "Eine Fotografin stellt 6 Kinder in einer Reihe auf. Tim und Eva sollen unmittelbar nebeneinander stehen, und zwar Tim links neben Eva. Wie viele verschiedene Aufstellungen gibt es?",
    120, "5 * 4 * 3 * 2 * 1", "120", "Tim und Eva müssen immer nebeneinander stehen. Wie ändert das, was du anordnest?",
    "Tim und Eva bilden ein festes Paar (Tim links). Es werden 5 Teile angeordnet: das Paar und 4 weitere Kinder. 5 · 4 · 3 · 2 · 1 = 120 Aufstellungen.",
    [(720, None, "alle 6 Kinder frei angeordnet: 6 · 5 · 4 · 3 · 2 · 1", "6 * 5 * 4 * 3 * 2 * 1"), (240, None, "auch die Reihenfolge Eva vor Tim mitgezählt", "2 * 120"), (30, None, "6 · 5 gerechnet", "6 * 5")], "Aufstellungen"), g="transfer")

# ───────── baumdiagramm ─────────
neu(T, "baumdiagramm", "anwenden", Z(
    "Ein Glücksrad hat 4 gleich große Felder A, B, C und D. Es wird einmal gedreht, danach wird eine Münze geworfen (Kopf oder Zahl). Wie viele Pfade hat das Baumdiagramm für diesen Versuch?",
    8, "4 * 2", "4 + 4", "In der ersten Stufe gibt es mehrere Äste, an jedem hängen weitere Äste der zweiten Stufe.",
    "Erste Stufe: 4 Äste (A, B, C, D). An jedem Ast hängen 2 Äste (Kopf, Zahl). 4 · 2 = 8 Pfade.",
    [(6, None, "die Astzahlen addiert", "4 + 2"), (16, None, "4 · 4 gerechnet", "4 * 4"), (4, None, "nur die erste Stufe gezählt", "4")], "Pfade"), regel=ST)
neu(T, "baumdiagramm", "zwei_wege", Z(
    "Eine Münze wird 4-mal geworfen. Bei wie vielen der Ergebnisfolgen kommt genau 1-mal Kopf vor? Weg A: Zeichne den Baum und zähle die passenden Pfade. Weg B: Überlege, an welcher der 4 Stellen der einzige Kopf stehen kann.",
    4, "4", "1 + 1 + 1 + 1", "Alle anderen Würfe sind Zahl. Es kommt nur darauf an, wann der Kopf fällt.",
    "Weg A: KZZZ, ZKZZ, ZZKZ, ZZZK sind die passenden Pfade, das sind 4. Weg B: Der Kopf kann beim 1., 2., 3. oder 4. Wurf fallen: 4 Möglichkeiten.",
    [(16, None, "alle Ergebnisfolgen gezählt: 2 · 2 · 2 · 2", "2 * 2 * 2 * 2"), (1, None, "nur eine Folge gezählt", "1"), (8, None, "2 · 4 gerechnet", "2 * 4")], "Folgen"), g="verknuepfen", regel=ST)

# ───────── bedingungen ─────────
neu(T, "bedingungen", "anwenden", Z(
    "Ein Zahlenschloss hat zwei Rädchen. Am ersten Rädchen steht eine ungerade Ziffer (1, 3, 5, 7 oder 9), am zweiten eine gerade Ziffer (0, 2, 4, 6 oder 8). Wie viele verschiedene Codes sind möglich?",
    25, "5 * 5", "5 + 5 + 5 + 5 + 5", "Wie viele Möglichkeiten gibt es am ersten, wie viele am zweiten Rädchen?",
    "Erstes Rädchen: 5 Möglichkeiten. Zweites Rädchen: 5 Möglichkeiten. Zusammen 5 · 5 = 25 Codes.",
    [(10, None, "die Möglichkeiten addiert", "5 + 5"), (100, None, "alle Ziffern an beiden Rädchen erlaubt: 10 · 10", "10 * 10"), (50, None, "10 · 5 gerechnet (eine Bedingung vergessen)", "10 * 5")], "Codes"))
neu(T, "bedingungen", "umkehren", Z(
    "Aus n verschiedenen Ziffern ohne die Null werden dreistellige Zahlen ohne doppelte Ziffer gebildet. Es gibt genau 60 solche Zahlen. Wie groß ist n?",
    5, "5", "60 / 12", "Wie viele Möglichkeiten gibt es für die erste, die zweite und die dritte Stelle? Probiere kleine Werte für n.",
    "Für die erste Stelle gibt es n Möglichkeiten, für die zweite n − 1, für die dritte n − 2. Für n = 5 ist 5 · 4 · 3 = 60. Für n = 4 wäre es 24, für n = 6 wären es 120. Also ist n = 5.",
    [(6, None, "n = 6 gewählt, das ergäbe aber 120 Zahlen", lambda: 6 * 5 * 4 == 120), (20, None, "60 durch 3 geteilt", "60 / 3"), (4, None, "n = 4 gewählt, das ergäbe nur 24 Zahlen", lambda: 4 * 3 * 2 == 24)]), g="rueckwaerts")

# ───────── grenzen ─────────
neu(T, "grenzen", "zwei_wege", Z(
    "6 Personen begrüßen sich bei einem Treffen, indem jede jeder anderen genau einmal die Hand gibt. Wie viele Handschläge gibt es? Weg A: Zähle der Reihe nach: Die erste Person gibt 5 Handschläge, die zweite noch 4 neue und so weiter. Weg B: Jede der 6 Personen gibt 5 Handschläge; dabei wird jeder Handschlag zweimal gezählt.",
    15, "5 + 4 + 3 + 2 + 1", "6 * 5 / 2", "Bei Weg B: Wie oft wird ein einzelner Handschlag gezählt? Was musst du am Ende tun?",
    "Weg A: 5 + 4 + 3 + 2 + 1 = 15. Weg B: 6 · 5 = 30, aber jeder Handschlag wurde zweimal gezählt: 30 : 2 = 15.",
    [(30, None, "nicht durch 2 geteilt", "6 * 5"), (36, None, "6 · 6 gerechnet", "6 * 6"), (21, None, "5 + 4 + 3 + 2 + 1 + 6 gerechnet", "5 + 4 + 3 + 2 + 1 + 6")], "Handschläge"))
neu(T, "grenzen", "bruecke", Z(
    "Ein Sechseck hat 6 Ecken. Eine Diagonale ist eine Strecke zwischen zwei Ecken, die nicht nebeneinander liegen. Wie viele Diagonalen hat das Sechseck?",
    9, "6 * 5 / 2 - 6", "6 * 3 / 2", "Wie viele Strecken gibt es zwischen allen Paaren von Ecken? Wie viele davon sind Seiten des Sechsecks?",
    "Zwischen 6 Ecken gibt es 6 · 5 : 2 = 15 Strecken. 6 davon sind Seiten des Sechsecks. Die übrigen 15 − 6 = 9 sind Diagonalen.",
    [(15, None, "die Seiten mitgezählt", "6 * 5 / 2"), (6, None, "die Zahl der Ecken genannt", "6"), (18, None, "von jeder Ecke 3 Diagonalen gezählt, nicht halbiert", "6 * 3")], "Diagonalen"), g="verknuepfen")

# ───────── verstehen ─────────
neu(T, "verstehen", "anwenden", W(
    "Ein Eis-Imbiss wirbt: „Über 100 verschiedene Eisbecher!“ Man wählt genau eine von 6 Sorten, genau eine von 4 Soßen und genau eines von 3 Toppings. Stimmt die Werbung?",
    "Nein, es sind nur 72 Becher.",
    [("Nein, es sind nur 13 Becher.", "Die Zahlen wurden addiert statt malgenommen."), ("Ja, es sind 7 · 5 · 4 = 140 Becher.", "„Ohne“ wurde als zusätzliche Möglichkeit mitgezählt, obwohl man aus jeder Gruppe genau eines wählt.")],
    "Aus jeder Gruppe wird genau eines gewählt. Wie viele Kombinationen gibt es nach dem Zählprinzip?",
    "Nach dem Zählprinzip: 6 · 4 · 3 = 72 Becher. 72 ist weniger als 100, die Werbung stimmt nicht.",
    lambda: 6 * 4 * 3 == 72 and 6 + 4 + 3 == 13 and 6 * 4 * 3 * 2 == 144))
neu(T, "verstehen", "zwei_wege", Z(
    "Tim behauptet: „Aus den Ziffern 1 und 2 kann man nur 6 verschiedene dreistellige Zahlen bilden, denn es gibt 3 · 2 · 1 Anordnungen.“ Wie viele dreistellige Zahlen aus den Ziffern 1 und 2 gibt es wirklich, wenn Ziffern mehrfach vorkommen dürfen? Weg A: Schreibe alle Zahlen geordnet auf (111, 112, 121, …) und zähle. Weg B: Rechne mit der Zahl der Möglichkeiten für jede Stelle. Gib die richtige Zahl der dreistelligen Zahlen an.",
    8, "2 * 2 * 2", "1 + 1 + 1 + 1 + 1 + 1 + 1 + 1", "Darf eine Ziffer mehrfach vorkommen? Wie viele Ziffern kommen dann für jede Stelle in Frage?",
    "Weg A: 111, 112, 121, 122, 211, 212, 221, 222 sind 8 Zahlen. Weg B: Jede der 3 Stellen hat 2 Möglichkeiten: 2 · 2 · 2 = 8. Tims Rechnung 3 · 2 · 1 gilt nur, wenn jede Ziffer genau einmal vorkommt.",
    [(6, None, "Tims Zahl 3 · 2 · 1 übernommen (Anordnungen ohne Wiederholung)", "3 * 2 * 1"), (4, None, "nur zwei Stellen gezählt", "2 * 2"), (9, None, "mit 3 Möglichkeiten je Stelle gerechnet, nur für zwei Stellen: 3 · 3", "3 * 3")], "Zahlen"), g="verknuepfen")
