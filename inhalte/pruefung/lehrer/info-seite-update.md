# „So funktioniert’s“ (Info-Seite Eltern/Lehrer) – Aktualisierung nach 0.82.2

Gelesen: `viewInfo` und `LERN_INFO_FRAGEN` in `lernen.js` auf `main` 24f59ec (App 0.82.2). LB (vier Stufen, Plan als Cockpit, „Kann er – aber wiederholen“, Auswählen) steht schon drin. Veraltet oder fehlend sind die folgenden Stellen. Neue Texte wörtlich.

## 1. Erste Schritte, Schritt 1 „Flugplan prüfen“ – veraltet
Heute: „… wähle Flüge ab, die nicht dran sind, und hake ab, was es schon kann. … ‚Nach Klasse (Lehrplan)‘ die Orte einer Klasse …“ (Häkchen gibt es nicht mehr; „Nach Klasse“ zeigt Flüge, nicht Orte).
Neu:
> Reiter „Plan“ auf der Seite des Kindes – das ist dein Arbeitsplatz. Links „Unser Lehrplan“ nach Stufen (▶ Gerade dran · ○ Kommt noch · ↻ In Wiederholung · ◉ Kann er komplett); Reihenfolge mit ⠿ ziehen oder ↑ ↓. Einen Ort antippen: je Flug die Knöpfe „Lernen“, „Kann er – aber wiederholen“, „Kann er komplett“, „Aus dem Plan nehmen“. Rechts der Lehrplan: „Nach Themengebiet“ (alle Flüge eines Gebiets von leicht nach schwer, auch über der Klasse des Kindes) oder „Nach Klasse“ (die Flüge einer Klasse in der Reihenfolge des Lehrplans, gegliedert nach Lernbereich). „+“ oder Ziehen plant ein. Viele auf einmal: „Auswählen“. Jede Änderung wird sofort gespeichert.

## 2. Frage „Was kann ich selbst ändern?“ – „Auswählen“ ungenau, doppelte Einträge
- Im Eintrag „Plan je Kind“ ersetzen: „‚Auswählen‘ setzt Häkchen je Flug …“ durch
  > „Auswählen“: je Ort ein Häkchen (alle seine Flüge), „▸ einzeln“ für einzelne Flüge, je Abschnitt „alle auswählen“; oben dann die Knöpfe für alle ausgewählten auf einmal (z. B. 6 Flüge aus Klasse 7 auf „wiederholen“).
- Die alten Einträge **„Lernstand:“** und **„Was wackelt?:“** am Ende der Liste löschen – sie wiederholen „Was wackelt“ weiter oben und Schritt 2.

## 3. „Kann er – aber wiederholen“ – wann ist es fertig? fehlt
Im Eintrag „Plan je Kind“ nach „(keine Übung, nur die Wiederholungen; zwei Fehler hintereinander → wieder offen)“ ergänzen:
> Für so gesetzte Flüge gibt es keinen Flug-Test und keine Nachtests. Ist die Wiederholung nach 14 Lerntagen bestanden (und eine Mischkarte richtig, falls eine kam), steht der Flug auf ◉. „Wieder in die Wiederholung“ holt einen ◉-Flug zurück; die Wiederholungen beginnen dann wieder nach 1 Lerntag.

## 4. Frage „Wie wird gelernt?“ – Flug-Test und Verbessern veraltet (seit 0.82.1)
Eintrag „Flug-Test:“ ersetzen durch:
> **Flug-Test:** Ist die letzte Pflicht-Etappe gelandet, führt der Landebildschirm nur noch zum Test („Jetzt zum Test ›“): eine Bordkarte je Etappe, ohne Tipps. Im Ergebnis ist jede Antwort deutlich als RICHTIG oder FALSCH markiert. Bei Fehlern zwei Wege: „Erst üben: ‹Etappe›“ oder „Gleich verbessern“. Alles richtig verbessert → Flug geschafft.

## 5. Knobel-Bordkarten – Ablauf veraltet (seit 0.82.1)
Im Eintrag „Knobel-Bordkarten:“ ersetzen „Sie erscheinen, wenn eine Etappe sitzt, und höchstens einmal am Tag als ‚Knobeln des Tages‘.“ durch:
> Nach jeder Landung kommt von selbst eine Knobel-Bordkarte der Etappe (überspringbar mit „Heute keine Knobel-Bordkarte“), außerdem höchstens einmal am Tag „Knobeln des Tages“.

## 6. Frage „Wie entstehen die Inhalte …“ – Lehrplan-Übersicht veraltet
Satz „Die Lehrplan-Übersicht … zeigt je Schulart und Klasse eine Tabelle aller Flüge: Ort, andere Schularten, Inhalt …“ ersetzen durch:
> Die Lehrplan-Übersicht (Nachschlagen auf der Startseite) zeigt je Schulart und Klasse alle Flüge in der Reihenfolge des Lehrplans, gegliedert nach Lernbereich (z. B. „M8 2 Lineare Funktionen“): andere Schularten, Inhalt (● fertig, ◐ in Prüfung, ○ fehlt) und die Stufe je Kind (◉ ↻ ▶ ○ +). Eine Zeile antippen öffnet „Inhalte ansehen“.

## 7. Frage „Worauf baut die App auf?“ – Lehrpläne je Schulart fehlen
Als dritten Punkt ergänzen:
> Für jede Schulart ist die Reihenfolge des Lehrplans und der Lernbereich hinterlegt (Gymnasium und Realschule nach LehrplanPLUS Bayern, IB nach dem MYP-Rahmenplan). Beim IB sind manche Zuordnungen als „Annahme“ gekennzeichnet, weil der Rahmenplan dort nicht genau festlegt, in welchem Jahr ein Thema dran ist. Den Lehrplan-Bezug eines Flugs sieht man, wenn man ihn im Lehrplan aufklappt.

## 8. Später (nach Bau-Auftrag AB)
Wenn die Abschluss-Ansichten gebaut sind: in „Wie wird gelernt?“ einen Eintrag „Abschluss einer Etappe“ (Direktflug · Saubere Landung · Sturmflug, Abzeichen im Reisepass) ergänzen. Jetzt noch nicht – die Seite soll nur beschreiben, was live ist.
