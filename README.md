# B-Team12: Hotelreservationsystem

## Autoren
Tanja Luescher
Sarina Grabherr
Fabia Holzer
Stirling Mulholland

## Deliverables -> KORRIGIEREN !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!¨
- Source Code und Artefakte
o Link zum Deepnote-Projekt mit allen ausführbaren Notebooks, Dateien und der
endgültigen Datenbank,
  (https://deepnote.com/workspace/fhnw-7ab7-98157d3c-c139-4c9e-a143-1cabfe774ad5/project/B-Team-12-Hotelreservation-Dokumentation-46c1a4c2-95b4-485b-8dd0-e1e655bdad30?utm_content=46c1a4c2-95b4-485b-8dd0-e1e655bdad30
o Link zum GitHub-Repository,
[GitHub-Repository](https://github.com/satafasti/team12_hotelreservation)
o Link zu einer Projekt Board
[Projekt Board](https://www.notion.so/1a62a269cd5a805f8983f8caf82b576a?v=1a62a269cd5a80769d6d000c6d5a6a27 )
- Dokumentation/Bericht (Link zu GitHub Markdown-Datei(en))
- Link zum Präsentationsvideo (das auf Microsoft Stream, SWITCHtube oder YouTube
gehostet wird; eingeschränkter/ungelisteter Zugang möglich und empfohlen). Es wird
empfohlen, dass jedes Teammitglied an der Videopräsentation beiträgt.

#  Einleitung

Dieses Projekt implementiert eine einfache Hotelbuchungs-Plattform auf Basis einer SQLite-Datenbank. Die Anwendung ermöglicht die Suche nach Hotels anhand
flexibler Kriterien wie zum Beispiel die Stadt, Anzahl Sterne eines Hotels, gewünschter Reisezeitraum oder Anzahl Gäste. Die zugrunde liegende Datenbank
beinhaltet im wesentlichen Informationen zu den Hotels, Zimmern, Ausstattung der Zimmer, Gäste, Buchungen und Rechnungen mit realistischen Beispieldaten.
Die Datenstruktur bildet unter Anderem Beziehungen zwischen Hotels, Zimmern und Gästen ab und erlaubt es die Buchungen mit Check-in /  Check-out-Daten und Stornierungen
zu verwalten. Die Anwendung nutzt Python zur Abfrage und Verarbeitung der Daten sowie einer benutzerfreundlichen Darstellung für den User. Ziel des Projektes
ist es die Anwendungsentwicklung mit Python in einem praxisnahen Szenario zu erlernen und vertiefen.

## Kontext

Für dieses Projekt wird den Autoren eine SQLite Datenkbank mit realistischen Beispieldaten zu zum Beispiel Hotels, Räumen und Gästen zur Verfügung gestellt. 
Diese soll als Basis dienen die im Unterricht erlernten Konzepte zur objektorientierten Entwicklung mit Python anhand eines realistischen Beispieles umzusetzen. 
Die im Rahmen des Projektes entwickelten UserStories sind die Folgenden. 

## User Stories

Die umgesetzten UserStories haben wir direkt im Deepnote dokumentiert: *Link einfügen*

## Layers

Projektstruktur und Architekturentscheidungen
Unser Projekt basiert auf einer klassischen Mehrschichtenarchitektur, bestehend aus Model, Data Access Layer (DAL), Business Logic Layer (Manager) und einer einfachen UI-Schicht. Diese Trennung erhöht die Wartbarkeit, Testbarkeit und Wiederverwendbarkeit des Codes.

1. Warum wir uns für diese Schichten entschieden haben
	•	Model-Schicht: Enthält ausschließlich strukturierte Datenobjekte (wie Hotel, Room, Guest, Booking, Invoice). Alle Attribute sind privat gekapselt, mit Validierung über Getter/Setter. Dadurch stellen wir sicher, dass alle Instanzen in einem konsistenten Zustand bleiben. Beziehungen zwischen Objekten (z. B. Hotel ↔ Room) sind direkt abgebildet, was eine intuitive Navigation im Code ermöglicht.
	•	DAL (Data Access Layer): Kapselt alle direkten Datenbankzugriffe. Jeder Zugriff erfolgt über dedizierte Klassen wie BookingDataAccess oder InvoiceDataAccess. Diese Klassen enthalten ausschließlich SQL-Operationen und wandeln die Ergebnisse in Model-Objekte um.
	•	Manager-Schicht (Business Logic): Vermittelt zwischen UI/DAL und zentralisiert die Geschäftslogik. Zum Beispiel prüft der InvoiceManager, ob eine Rechnung zu einer Buchung existiert, bevor eine neue erstellt wird. Manager nutzen jeweils die passenden DAL-Klassen, um mit der Datenbank zu interagieren, und wenden zusätzliche Regeln an (z. B. keine Rechnung bei stornierten Buchungen).
	•	UI-Schicht: Dient der Benutzereingabe und Ausgabe. Sie ist vollständig getrennt von der Logik. Die Ergebnisse werden strukturiert formatiert und mögliche Mehrfachausgaben durch Korrekturen im Manager- und DAL-Bereich vermieden.

2. Warum wir die Manager so gestaltet haben
	•	Manager bündeln zusammengehörige Operationen (z. B. create_invoice, read_invoice, cancel_invoice im InvoiceManager).
	•	Die Manager prüfen Eingaben zusätzlich zur DAL-Validierung (z. B. ob eine Buchung storniert wurde oder ob bereits eine Rechnung existiert).
	•	Manager verwenden jeweils nur die DALs, die sie wirklich benötigen (InvoiceManager nutzt z. B. zusätzlich BookingDataAccess, um Buchungsdaten zu lesen).

3. Modellverknüpfungen
	•	Verknüpfungen sind objektorientiert modelliert, z. B. referenziert ein Room sein Hotel-Objekt direkt, nicht nur dessen ID.
	•	Komposition wird verwendet (ein Hotel enthält Räume; ein Raum enthält Ausstattung).
	•	Bidirektionale Beziehungen wie Room ↔ Hotel werden gepflegt, indem z. B. beim Setzen eines Hotels im Room automatisch das Hotel den Room ergänzt (hotel.add_room(self)).
Details zu den Modellverknüpfungen lassen sich direkt in der Dokumentation im Abschnitt "Modell Schicht" finden: 
https://deepnote.com/workspace/FHNW-98157d3c-c139-4c9e-a143-1cabfe774ad5/project/Hotelreservationv2-46c1a4c2-95b4-485b-8dd0-e1e655bdad30/notebook/Dokumentation-4f84071aa5d042e99ec482fafed1425f?utm_content=46c1a4c2-95b4-485b-8dd0-e1e655bdad30

Diese Struktur ermöglicht ein robustes, erweiterbares System mit klaren Verantwortlichkeiten pro Schicht und hoher Datenkonsistenz.

## Zusammenarbeit und Projektaufbau

Zu Beginn des Projektes haben wir uns für eine Aufteilung des Aufbau der Klassen (über alle Layers hinweg) entschieden und dabei ein KANBAN-Board direkt in GitHub verwendet zwecks Tracking der Aufgaben.

Initial wurden die Klassen wie folgt aufgeteilt:

Fabia Holzer: Booking, Invoice -> später ergänzt mit Payment
Stirling Mulholland: Address, Guest -> später ergänzt mit Guets_Details
Sarina Grabherr: Room, Roomtype -> später ergänzt mit hotel_review
Tanja Lüscher: Hotel, Facilities

Im Weiteren Verlaufe des Projektes wurden sodann auch die UserStories erst einmal aufgeteilt:

Fabia Holzer: UserStory 4, 8, 9 und 10, UserStory mit Datenbankschemaänderung 6
Stirling Mulholland: UserStory 2 und 6, UserStory mit Datenvisualisierung 2
Sarina Grabherr: UserStory 3 und 7, UserStory mit Datenbankschemaänderung 3 und 4
Tanja Lüscher: UserStory 1, 2 und 5

Allerdings fiel es uns in der Folge immer schwerer eine klare Aufteilung aufrecht zu erhalten, da für die Umsetzung einiger UserStories auch Klassen angepasst werden mussten, welche einem ursprünglich nicht zugeteilt waren. Wir haben uns daher wöchentlich mindestens einmal (im Unterricht am Mittwoch) und vielfach auch weitere Male (oft am Freitag vor Ort oder Abends via Teams) abgesprochen und aufgeteilt, wer welche Aufgaben übernimmt. Das KANBAN-Board 
haben wir ab diesem Zeitpunkt nicht mehr weiterverwendet, da eine klare Aufgabentrennung nicht mehr möglich war. Wir haben es daher präferiert uns regelmässig persönlich oder via Teams auszutauschen und Check-Ins abzuhalten. Ebenso haben wir uns bei der Erarbeitung der UserStories schlussendlich unterstütz und einige der obligatorischen UserStories schliesslich gemeinsam ausgearbeitet. Im Deepnote hat jeder seine eigenen umgesetzten UserStories dokumentiert. 
Die allgemeine Dokumentation / ReadMe haben wir zu Beginn gemeinsam geführt, die Fertigstellung wurde schlussendlich durch Tanja Lüscher sichergestellt. 

