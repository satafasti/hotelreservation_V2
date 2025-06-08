# Hotel-Reservierungssystem Demo-Skripte

## Skript 1: Gäste-Buchungsdemo
**Personen:** Stirling (Kunde) und Tanja (seine Partnerin)
**Dauer:** ca. 3-4 Minuten
**Szenario:** Paar sucht und bucht ein Hotel für ein Wochenende in der Schweiz

---

### Szene 1: Hotelsuche
**Stirling:** (am Computer) "Tanja, komm mal her! Ich schaue gerade nach Hotels für unser Wochenende in der Schweiz."

**Tanja:** "Super Idee! Was hast du denn gefunden?"

**Stirling:** (klickt im System) "Ich gehe ins Hauptmenü... hier, Gäste-Funktionen... und jetzt auf '1. Hotels suchen'."

**System zeigt:** *Suchmaske mit Datum, Ort, Anzahl Personen*

**Stirling:** "Ich gebe Zürich ein, 2 Personen, vom 20. bis 22. Juni..."

**Tanja:** "Schau mal, da kommen schon Ergebnisse! Das Hotel Baur au Lac sieht luxuriös aus - 5 Sterne!"

### Szene 2: Hotel auswählen und Preise vergleichen
**Stirling:** "Lass uns die Details anschauen. Ich klicke auf '5. Hotel wählen mit Preisinformation'..."

**System zeigt:** *Hotelliste mit echten Daten*
- Hotel Baur au Lac, Zürich (5★): Single CHF 250/Nacht, Double CHF 400/Nacht
- Four Seasons Hôtel des Bergues, Genève (5★): Suite CHF 650/Nacht
- Grand Hotel National, Luzern (5★): Family Room CHF 900/Nacht

**Tanja:** "CHF 400 pro Nacht für das Doppelzimmer im Baur au Lac - das ist angemessen für diese Qualität!"

**Stirling:** "Perfekt! Lass uns auch die Bewertungen anschauen..."

**Stirling:** (klickt auf "7. Hotelbewertungen ansehen")

**System zeigt:** *Bewertungen anderer Gäste*

**Tanja:** "Die Bewertungen sind ausgezeichnet - das überzeugt mich!"

### Szene 3: Buchung durchführen
**Stirling:** "Dann buchen wir das Doppelzimmer! Ich gehe auf '2. Buchung inkl. Zahlung'..."

**System zeigt:** *Buchungsformular für Zimmer 102, Hotel Baur au Lac*

**Stirling:** (tippt) "Stirling Weber, tanja.mueller@email.ch, Telefon..."

**Tanja:** "Schau, das Zimmer hat WiFi und TV - perfekt!"

**Stirling:** "Ja! So... Kreditkartendaten eingeben... Gesamtbetrag CHF 800 für 2 Nächte... und bestätigen!"

**System:** *"Buchung erfolgreich! Buchungsnummer: BK-2025-036"*

**Stirling & Tanja:** "Geschafft! Ich freue mich schon auf Zürich!"

### Szene 4: Rechnung abrufen
**Stirling:** "Ach, ich hole mir schnell die Rechnung für die Steuerunterlagen..."

**Stirling:** (klickt auf "3. Rechnung erstellen")

**System:** *PDF-Rechnung wird generiert - Invoice ID: 36, Total: CHF 800*

**Tanja:** "Super praktisch, dass das System automatisch die Rechnung erstellt!"

---

## Skript 2: Admin-Demo
**Personen:** Sarina (Hotelchefin) und Fabia (IT-Administratorin)
**Dauer:** ca. 4-5 Minuten
**Szenario:** Verwaltung bestehender Hotels und Buchungsanalyse

---

### Szene 1: Buchungsübersicht analysieren
**Sarina:** "Fabia, können Sie mir eine Übersicht unserer aktuellen Buchungssituation zeigen?"

**Fabia:** "Selbstverständlich, Sarina! Ich zeige Ihnen unsere Live-Daten."

**Fabia:** (am Computer) "Ich logge mich ins Admin-System ein... Hauptmenü, Admin-Funktionen..."

**System zeigt:** *Admin-Menü mit allen Optionen*

**Fabia:** "Hier klicke ich auf '5. Alle Buchungen anzeigen'..."

### Szene 2: Echte Buchungsdaten analysieren
**System zeigt:** *Buchungsübersicht aus der Datenbank*
- Booking ID 35: Guest_ID 10 (Julia Hofmann), Hotel Baur au Lac, CHF 750
- Booking ID 34: Guest_ID 9 (Stefan Wagner), Bellevue Palace Penthouse, CHF 6000
- Booking ID 33: Guest_ID 8 (Laura Bauer), Grand Hotel National, CHF 3600

**Sarina:** "Ich sehe, das Bellevue Palace Penthouse für CHF 1500/Nacht läuft sehr gut!"

**Fabia:** "Genau! Stefan Wagner hat 4 Nächte gebucht. Unsere Premium-Zimmer sind sehr gefragt."

### Szene 3: Zimmerausstattung verwalten
**Sarina:** "Können Sie mir die Zimmerdetails zeigen?"

**Fabia:** "Option 6: 'Zimmer mit Ausstattung anzeigen'..."

**System zeigt:** *Echte Zimmerdetails aus der DB*
- Zimmer 101 (Single): WiFi, TV - CHF 250/Nacht
- Zimmer 102 (Double): WiFi - CHF 400/Nacht  
- Zimmer 201 (Suite): Air Conditioning - CHF 650/Nacht
- Zimmer 301 (Family Room): Mini Bar - CHF 900/Nacht

**Fabia:** "Wie Sie sehen, hat jedes Zimmer unterschiedliche Ausstattung. WiFi ist Standard in den Baur au Lac Zimmern."

### Szene 4: Hotelinformationen aktualisieren
**Sarina:** "Wir müssen die Preise für das Grand Hotel National anpassen - die Nachfrage ist hoch."

**Fabia:** "Kein Problem! Option 3: 'Hotelinformationen aktualisieren'..."

**Fabia:** (demonstriert) "Ich wähle Grand Hotel National aus... erhöhe den Preis von CHF 900 auf CHF 950 für die Family Room..."

**System:** *"Hotel erfolgreich aktualisiert!"*

### Szene 5: Neue Hotelausstattung hinzufügen
**Sarina:** "Können wir dem Four Seasons in Genève einen Balkon hinzufügen?"

**Fabia:** "Selbstverständlich! Über die Stammdaten-Verwaltung..."

**Fabia:** (klickt auf "7. Stammdaten verwalten")

**System zeigt:** *Facilities: WiFi, TV, Air Conditioning, Mini Bar, Balcony*

**Fabia:** "Ich weise Zimmer 201 in Genève zusätzlich 'Balcony' zu... Fertig!"

### Szene 6: Stornierungen verwalten
**Sarina:** "Ich sehe hier einige stornierte Buchungen. Wie handhaben wir die?"

**System zeigt:** *Booking ID 13, 19, 28 mit is_cancelled = 1, total_amount = 0.00*

**Fabia:** "Stornierte Buchungen werden automatisch auf CHF 0 gesetzt. Das sehen Sie bei Booking IDs 13, 19 und 28."

**Sarina:** "Excellent! Das System behält die Historie, aber verrechnet nichts."

### Szene 7: Adressverwaltung
**Sarina:** "Was ist, wenn sich eine Hoteladresse ändert?"

**Fabia:** "Option 4: 'Hotelinformationen aktualisieren mit Adresse'... Hier kann ich sowohl Hotel- als auch Adressdaten zentral verwalten."

**Fabia:** (zeigt Beispiel) "Hotel Baur au Lac, Bahnhofstrasse 1, 8001 Zürich - alles synchronisiert sich automatisch."

### Szene 8: Abschluss
**Sarina:** "Perfekt! Die Integration zwischen Buchungen, Rechnungen und Stammdaten funktioniert nahtlos."

**Fabia:** "Genau! Jede Buchung generiert automatisch eine Invoice, und alle Änderungen sind sofort live."

**Sarina:** "Vielen Dank für die Demonstration, Fabia. Unser System ist wirklich professionell!"

---

## Technische Hinweise für die Videoaufnahme:

### Für beide Videos:
- **Screen Recording** der Systemoberfläche parallel zu den Gesprächen
- **Split-Screen** oder **Picture-in-Picture** für Personen + System
- **Cursor-Highlighting** für bessere Nachvollziehbarkeit
- **Zoom-Effekte** bei wichtigen Systemnachrichten

### Gäste-Video:
- Fokus auf **Benutzerfreundlichkeit**
- Realistische **Suchkriterien** und **Entscheidungsfindung**
- **Erfolgs-Feedback** des Systems hervorheben

### Admin-Video:
- Fokus auf **Effizienz** und **Kontrolle**
- **Datenübersicht** und **Management-Features** betonen
- **Sicherheitsaspekte** (Bestätigungen) erwähnen

### Nachbearbeitung:
- **Untertitel** für wichtige Systemfunktionen
- **Highlight-Boxen** um relevante Menüpunkte
- **Fade-Übergänge** zwischen Szenen
- **Call-to-Action** am Ende jedes Videos