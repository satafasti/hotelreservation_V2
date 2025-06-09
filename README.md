# B-Team12: Hotelreservationsystem

## Autoren
Tanja Luescher
Sarina Grabherr
Fabia Holzer
Stirling Mulholland

## Deliverables 
- Source Code und Artefakte
o Link zum Deepnote-Projekt mit allen ausführbaren Notebooks, Dateien und der endgültigen Datenbank

	[Deepnote Dokumentation](https://deepnote.com/workspace/FHNW-98157d3c-c139-4c9e-a143-1cabfe774ad5/project/B-Team-12-Hotelreservation-Dokumentation-46c1a4c2-95b4-485b-8dd0-e1e655bdad30/notebook/Dokumentation-4f84071aa5d042e99ec482fafed1425f?utm_content=46c1a4c2-95b4-485b-8dd0-e1e655bdad30)

	[Deepnote Showcase User Stories](https://deepnote.com/workspace/FHNW-98157d3c-c139-4c9e-a143-1cabfe774ad5/project/B-Team-12-Hotelreservation-Dokumentation-46c1a4c2-95b4-485b-8dd0-e1e655bdad30/notebook/Dokumentation-4f84071aa5d042e99ec482fafed1425f?utm_content=46c1a4c2-95b4-485b-8dd0-e1e655bdad30)

	[Deepnote Hotelreservation UI](https://deepnote.com/workspace/FHNW-98157d3c-c139-4c9e-a143-1cabfe774ad5/project/B-Team-12-Hotelreservation-Dokumentation-46c1a4c2-95b4-485b-8dd0-e1e655bdad30/notebook/Dokumentation-4f84071aa5d042e99ec482fafed1425f?utm_content=46c1a4c2-95b4-485b-8dd0-e1e655bdad30)


- o Link zum GitHub-Repository

  [GitHub-Repository](https://github.com/satafasti/hotelreservation_V2)
	
	[Altes GitHub-Repository](https://github.com/satafasti/team12_hotelreservation)


- o Link zum Projekt Board

	[Projekt Board](https://github.com/orgs/satafasti/projects/2/views/1)

- Link zum Präsentationsvideo 

	[Demo Video]()

Unser Deepnote-Projekt ist wie folgt aufgebaut:

- Dokumentation: enthält eine Erklärung zu unseren Layers und Klassen
- Showcase UserStories - 2: enthält alle unsere UI-Funktionen sowie die Erklärungen zu unseren Gedanken und Hintergründen für die Umsetzung der UserStories
- UI - Menü: enthält einen zentralen Einstieg in die verschiedenen verfügbaren UserStories, aufgeteilt in Gäste- und Adminfunktionen

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

Die umgesetzten UserStories haben wir direkt im Deepnote dokumentiert:
[Deepnote Showcase User Stories](https://deepnote.com/workspace/FHNW-98157d3c-c139-4c9e-a143-1cabfe774ad5/project/B-Team-12-Hotelreservation-Dokumentation-46c1a4c2-95b4-485b-8dd0-e1e655bdad30/notebook/Dokumentation-4f84071aa5d042e99ec482fafed1425f?utm_content=46c1a4c2-95b4-485b-8dd0-e1e655bdad30)

## Layers

Projektstruktur und Architekturentscheidungen
Unser Projekt basiert auf einer klassischen Mehrschichtenarchitektur, bestehend aus Model, Data Access Layer (DAL), Business Logic Layer (Manager) und einer einfachen UI-Schicht. Diese Trennung erhöht die Wartbarkeit, Testbarkeit und Wiederverwendbarkeit des Codes.

1. Warum wir uns für diese Schichten entschieden haben
	•	Model-Schicht: Enthält ausschliesslich strukturierte Datenobjekte (wie Hotel, Room, Guest, Booking, Invoice). Alle Attribute sind privat gekapselt, mit Validierung über Getter/Setter. Dadurch stellen wir sicher, dass alle Instanzen in einem konsistenten Zustand bleiben. Beziehungen zwischen Objekten (z. B. Hotel ↔ Room) sind direkt abgebildet, was eine intuitive Navigation im Code ermöglicht.
	•	DAL (Data Access Layer): Kapselt alle direkten Datenbankzugriffe. Jeder Zugriff erfolgt über dedizierte Klassen wie BookingDataAccess oder InvoiceDataAccess. Diese Klassen enthalten ausschliesslich SQL-Operationen und wandeln die Ergebnisse in Model-Objekte um.
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
[Deepnote Dokumentation](https://deepnote.com/workspace/FHNW-98157d3c-c139-4c9e-a143-1cabfe774ad5/project/B-Team-12-Hotelreservation-Dokumentation-46c1a4c2-95b4-485b-8dd0-e1e655bdad30/notebook/Dokumentation-4f84071aa5d042e99ec482fafed1425f?utm_content=46c1a4c2-95b4-485b-8dd0-e1e655bdad30)

Diese Struktur ermöglicht ein robustes, erweiterbares System mit klaren Verantwortlichkeiten pro Schicht und hoher Datenkonsistenz.

## Zusammenarbeit und Projektaufbau

Zu Beginn des Projektes haben wir uns für eine Aufteilung des Aufbau der Klassen (über alle Layers hinweg) entschieden und dabei ein KANBAN-Board direkt in GitHub verwendet zwecks Tracking der Aufgaben.

Initial wurden die Klassen wie folgt aufgeteilt:

Fabia Holzer: Booking, Invoice -> später ergänzt mit Payment
Stirling Mulholland: Address, Guest -> später ergänzt mit Guets_Details
Sarina Grabherr: Room, Roomtype -> später ergänzt mit hotel_review
Tanja Lüscher: Hotel, Facilities -> später diverse Manager- und Data Access-Klassen ergänzt 

Im Weiteren Verlaufe des Projektes wurden sodann auch die UserStories erst einmal aufgeteilt:

Fabia Holzer: UserStory 4, 8, 9 und 10, UserStory mit Datenbankschemaänderung 6
Stirling Mulholland: UserStory 2 und 6, UserStory mit Datenvisualisierung 2
Sarina Grabherr: UserStory 3 und 7, UserStory mit Datenbankschemaänderung 3 und 4
Tanja Lüscher: UserStory 1, 2 und 5

Fabia Holzer hat sich schlussendlich auch noch um das UI-Menü gekümmert.

Allerdings fiel es uns in der Folge immer schwerer eine klare Aufteilung aufrecht zu erhalten, da für die Umsetzung einiger UserStories auch Klassen angepasst werden mussten, welche einem ursprünglich nicht zugeteilt waren. Wir haben uns daher wöchentlich mindestens einmal (im Unterricht am Mittwoch) und vielfach auch weitere Male (oft am Freitag vor Ort oder Abends via Teams) abgesprochen und aufgeteilt, wer welche Aufgaben übernimmt. Das KANBAN-Board 
haben wir ab diesem Zeitpunkt nicht mehr weiterverwendet, da eine klare Aufgabentrennung nicht mehr möglich war. Wir haben es daher präferiert uns regelmässig persönlich oder via Teams auszutauschen und Check-Ins abzuhalten. Ebenso haben wir uns bei der Erarbeitung der UserStories schlussendlich unterstütz und einige der obligatorischen UserStories schliesslich gemeinsam ausgearbeitet. Im Deepnote hat jeder seine eigenen umgesetzten UserStories dokumentiert. 
Die allgemeine Dokumentation / ReadMe haben wir zu Beginn gemeinsam geführt, die Fertigstellung wurde schlussendlich durch Tanja Lüscher sichergestellt. 

Zum Aufbau des Projektes ist speziell zu erwähnen, dass wir bis ca. Mitte Mai etwas "festgefahren" waren und die Implementierung der UserStories nicht gut voranschritt. Wir haben uns daher nach einem intensiven Coaching dazu entschieden noch einmal ein neues GitHub Repository zu erstellen um einen "Neustart" zu simulieren. Für den Neuaufbau der Klassen haben wir uns dazu stark am Beispiel-Projekt orientiert. Dies hat uns tatsächlich geholfen einen "Durchbruch" im Verständnis 
erreichen, zog allerdings in der Folge auch nach sich, dass wir teilweise viel des geschriebenen Codes nicht mehr weiterverwendet haben, weil uns plötzlich klar wurde, wie wir die für unser Projekt nötigen Methoden selbst optimiert schreiben können. Aus zeitlichen Gründen haben wir die nicht verwendeten Code-Blöcke in den Klassen auskommentiert. Im Sinne einer sauberen Codeführung hätten wir mit etwas mehr Zeit diese aber vermutlich komplett bereinigt und entfernt. Da wir
zum jetzigen sehr fortgeschrittenen Projektverlauf allerdings nicht riskieren wollten, versehentlich Methoden zu löschen, welche doch irgendwo verwendet werden, oder welche man idealerweise bei der weiteren Implementierung von zusätzlichen UserStories gut hätte verwenden können, haben wir dies unterlassen.

## Reflexion

„Keep it simple, stupid“ sollte das Motto eines jeden angehenden Programmierers sein und ist es wahrscheinlich auch für viele Erfahrene. 
Dies hat sich schnell als gute Leitidee gezeigt, um das Projekt in einem für unseren Wissensstand übersichtlichen Mass umsetzen zu können.
Unser Ziel war es, zum ersten Mal Computersprache zu sprechen. Wir wollten dem PC sagen, was und wie er etwas machen sollte, 
ohne eine hübsche Benutzeroberfläche bedienen zu müssen.


Angefangen mit einfachen Eingaben und Variablen hat uns die Reise zu Klassen, Funktionen und Listen gebracht.
Mit diesem Wissen konnten wir unsere ersten Zeilen Code in der Modellklasse schreiben. Hier sind die ersten
Probleme einer Gruppenarbeit aufgetaucht. Vier Personen verstehen nicht immer alles gleich schnell.
Es wäre hilfreich gewesen, die Aufgaben aus dem Unterricht gemeinsam zu lösen, um die Theorie gleich zu verstehen wie die anderen Teamkollegen.
Einige von uns hätten es hilfreich gefunden, beim User Interface anzufangen, um einen groben Überblick zu bekommen,
was eigentlich von uns erwartet wurde. Jeder hat seinen Ansatz umgesetzt, ohne zu überprüfen, was die anderen gemacht haben.
Hier waren das Beispielprojekt, das Kanban-Board und GitHub eine grosse Hilfe, um einen gemeinsamen Nenner zu finden.
Die Zusammenarbeit im Team war hervorragend, jeder konnte seinen Teil beitragen und wir konnten uns gegenseitig helfen.
Wie die einzelnen Schichten zusammenhingen, war uns lange Zeit ein Rätsel, bis wir die Datenbank anbinden konnten.
Sobald wir Daten erhalten konnten, wurden schon fleissig die ersten User Stories zum Laufen gebracht.
Eureka! Ein Erfolgserlebnis nach dem anderen!

Nach jeder Gruppenarbeit sollte es heissen: „Ich bin teamfähiger geworden.”
Insbesondere bei dieser komplexen Arbeit, denn das Resultat wurde durch die  Zusammenarbeit und gegenseitige Unterstützung im Team ermöglicht.
Der Erfolg, einen Code selbstständig zu schreiben und diesen nach Trial and Error zum Laufen zu bringen, ist unbeschreiblich.
Unser Zeitmanagement war leider nicht optimal, was auch daran lag, dass wir nicht wussten, wie wir selbstständig vorankommen. 
Dies führte dazu, dass wir keine zusätzlichen User Stories umsetzen konnten.
Es hat sich massiv gelohnt, bei den Coaches Hilfe zu holen, um den Endspurt zu meistern. 
Ein neues GitHub aufzusetzen ist zwar keine gute Lösung, weil dabei die Historie verloren geht. 
Aber es hat uns motiviert, den Code von Grund auf noch einmal anzuschauen und zu korrigieren. 
Weitere Verbesserungen wären in den Klassen „Manager”, „UI” und „Data Access” möglich. Die Funktionen sind
nicht immer korrekt getrennt worden. Manchmal wurden die Daten aus der Datenbank direkt mit SQL-Funktionen wie Joins und Group By geholt.
Anstatt diese als Objekte der Modellklassen zu laden und nachher weiterzuverarbeiten. 
Den gelernten Stoff werden wir in Zukunft sicher im Studium und bei der Arbeit anwenden können.
Besonders nützlich waren die Datenbankanbindung sowie die Möglichkeit, Daten zu verarbeiten und zu visualisieren, um verschiedene Analysen durchzuführen.
Die Fähigkeit, die Logik eines Programms nur anhand des Codes zu verstehen, ist sehr wertvoll.
GitHub ist beim Programmieren unerlässlich, um einen Versionsverlauf zu haben und die Zusammenarbeit des Teams zu ermöglichen.
Unsere erste Erfahrung mit einer IDE war sehr positiv und hat bei allen die Arbeit erleichtert. 
All diese Tools und Fähigkeiten packen wir gerne in unseren wachsenden Werkzeugkoffer.
