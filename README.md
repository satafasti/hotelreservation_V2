# B-Team12: Hotelreservationsystem

## Autoren
Tanja Luescher
Sarina Grabherr
Fabia Holzer
Stirling Mulholland

## Deliverables
Der Abgabetermin 15.06.2025  für die Projektarbeit ist auf Moodle angegeben. Dabei gibt jedes Team
Folgendes an:
- Source Code und Artefakte
o Link zum Deepnote-Projekt mit allen ausführbaren Notebooks, Dateien und der
endgültigen Datenbank,
[Deepnote-Projekt](https://deepnote.com/workspace/FHNW-98157d3c-c139-4c9e-a143-1cabfe774ad5/project/B-Team12-hotelreservation-c198bb5c-da9b-4a42-90aa-865b4b8bde28/notebook/520bcd201f574cfcb10519b35812afcf)
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

Fabia Holzer: Booking, Invoice
Stirling Mulholland: 
Sarina Grabherr: Room, Roomtype
Tanja Lüscher: Hotel, Address

Im Weiteren Verlaufe des Projektes wurden sodann auch die UserStories erst einmal aufgeteilt:t

Fabia Holzer: UserStory 4, 8, 9, 10
Stirling Mulholland: UserStory 2 und 6
Sarina Grabherr: UserStory 3 und 7
Tanja Lüscher: UserStory 1 und 5

Allerdings fiel es uns in der Folge immer schwerer eine klare Aufteilung aufrecht zu erhalten, da für die Umsetzung einiger UserStories auch Klassen angepasst werden mussten, welche einem ursprünglich nicht zugeteilt waren. Wir haben uns daher wöchentlich mindestens einmal (im Unterricht am Mittwoch) und vielfach auch weitere Male (oft am Freitag vor Ort oder Abends via Teams) abgesprochen und aufgeteilt, wer welche Aufgaben übernimmt. Das KANBAN-Board 
haben wir ab diesem Zeitpunkt nicht mehr weiterverwendet, da eine klare Aufgabentrennung nicht mehr möglich war. Wir haben es daher präferiert uns regelmässig persönlich oder via Teams auszutauschen und Check-Ins abzuhalten. Ebenso haben wir uns bei der Erarbeitung der UserStories schlussendlich unterstütz und einige der obligatorischen UserStories schliesslich gemeinsam ausgearbeitet. 


## Zusammenfassung Unterrichtseinheit 1 Iteration 1
In der ersten Unterrichtseinheit haben wir grundlegende Programmierkonzepte in Python kennengelernt und diese durch praktische Anwendungen vertieft. Ein zentraler Bestandteil war das **Input-Process-Output (IPO)-Modell**, das den Ablauf einer Anwendung in **Datenaufnahme (Input), Verarbeitung (Process) und Ausgabe (Output)** unterteilt. Dieses Modell haben wir direkt in unseren Übungen angewendet.
Wir haben eine **fiktive Musikdatenbank** erstellt, in der Musiktracks mit Variablen gespeichert wurden. Dabei haben wir unterschiedliche **Datentypen** kennengelernt, darunter Strings (*str*) für Namen und Kategorien sowie *float* für Preise. Mit der *type()*-Funktion konnten wir die Datentypen überprüfen.
Um die Daten für den Nutzer verständlich auszugeben, haben wir uns mit der *print()*-Funktion und **formatierten Strings (*f"..."*)** beschäftigt. Zusätzlich haben wir die **Benutzereingabe mit *input()*** integriert, sodass der Nutzer angeben konnte, wie viele Tracks er kaufen möchte. Basierend auf dieser Eingabe wurde der **Gesamtpreis berechnet**. 
Eine weitere wichtige Anwendung war die **Preisberechnung mit Rabatten**. Falls der Nutzer das gesamte Album kaufte, wurde automatisch ein **10 %-Rabatt** gewährt. Zudem haben wir gelernt, wie man **Dezimalzahlen formatiert** (*{:.2f}*), um Preise korrekt darzustellen.
Diese Übungen gaben uns einen ersten Einblick in die Entwicklung datengetriebener Anwendungen. Besonders wichtig war dabei, den Programmablauf durch **Debugging und Testen mit *print()*** besser zu verstehen.

## Zusammenfassung Unterrichtseinheit 1 Iteration 2
In der zweiten Unterrichtseinheit haben wir uns intensiv mit **Bedingungen und Geschäftslogik** in Python beschäftigt. Dabei haben wir gelernt, wie Programme mithilfe von *if*, *elif* und *else* unterschiedliche Entscheidungen treffen können, um dynamisch auf verschiedene Szenarien zu reagieren.
Die wichtigste Erkenntnis ist, dass Programme basierend auf Bedingungen verschiedene Aktionen ausführen können. Eine *if*-Bedingung prüft, ob eine Aussage wahr ist, und führt dann einen bestimmten Codeblock aus. Falls die Bedingung nicht zutrifft, greift *else* und es wird ein alternativer Code ausgeführt. Durch *elif* können mehrere Bedingungen nacheinander geprüft werden, um verschiedene Fälle zu unterscheiden. Diese Strukturen ermöglichen es, dass Programme flexibel auf unterschiedliche Situationen reagieren können, beispielsweise um nur digitale Musiktracks anzuzeigen.
Ein weiterer wichtiger Aspekt war die Kombination von Bedingungen mit Datenverarbeitung. In den Übungen haben wir geprüft, welche Musiktracks digital verfügbar sind, und nur diese angezeigt. Dabei haben wir auch gelernt, wie *or* und *and* genutzt werden, um Mehrfachbedingungen zu definieren. Dies ist besonders wichtig, wenn Programme komplexere Entscheidungen treffen sollen, beispielsweise ob mindestens eine oder mehrere Bedingungen erfüllt sein müssen.
Zusätzlich haben wir die **Interaktion mit Benutzern** durch *input()* kennengelernt. Damit kann ein Programm Eingaben vom Nutzer abfragen und darauf reagieren. Ein Beispiel dafür war die Entscheidung, ob ein Nutzer das gesamte Album kaufen möchte, wodurch ein Rabatt gewährt wurde. Falls der Nutzer nur einzelne Tracks kaufen wollte, wurde die Anzahl abgefragt und der Preis entsprechend berechnet. Dies zeigt, wie Programme mit Nutzern kommunizieren können, anstatt nur statische Daten auszugeben.
Unsere Übungen haben auch gezeigt, dass **Geschäftslogik** eine zentrale Rolle in der Programmierung spielt. Wir haben gelernt, wie man Regeln in Code umsetzt, zum Beispiel Rabatte berechnet, den Lagerbestand überprüft oder zwischen digitalen und physischen Medien unterscheidet. Diese Konzepte sind essenziell für reale Anwendungen, wie Online-Shops oder Buchungssysteme.
Ein weiteres wichtiges Konzept, das wir kennengelernt haben, war die **Verwendung von Tuples**. Tuples sind eine effiziente Möglichkeit, **unveränderliche Daten** zu speichern, da sie nicht nachträglich verändert werden können. Dies ist besonders nützlich für feste Datensätze, wie Album- oder Trackinformationen.

*Reflexion über Relevanz für unser Projekt:*
Die ersten beiden Unterrichtseinheiten gaben uns einen grundlegenden Einblick in die Anwendungsentwicklung mit Python. Wir haben die Syntax, den Umgang mit verschiedenen Datentypen sowie die Interaktion mit User und die Überprüfung auf Bedingungen kennengelernt. Alle diese Inputs werden für unser Projekt wichtig sein, da wir z.B. für die Abfrage von verfügbaren Hotels in einem bestimmten Zeitraum einen User-Input benötigen werden, in welchem dieser seine Wünsche definiert.
Diese werden in Bezug auf den gewünschten Buchungszeitraum Datums-Eingaben enthalten, welche wir korrekt weiterverarbeiten können müssen um z.B. abzugleichen ob im gewünschten Zeitraum bereits Buchungen bestehen, aufgrund welcher ein bestimmtes Hotel oder bestimmte Räume in diesem Hotel nicht angezeigt werden dürfte, da sie nicht verfügbar sind. Für die Umsetzung dieser UserStories werden wir entsprechend zwingend mit User-Input, Bedingungen und verschiedenen Datentypen müssen umgehen können.

## Zusammenfassung Unterrichtseinheit 1 Iteration 3 

### Liste
- Im Gegensatz zu Tupeln sind Listen veränderbar, d.h. die Elemente in Listen können hinzugefügt, aktualisiert oder entfernt werden
- Liste in Listen
- Index/Element einer Liste beginnt mit 0
- Bei der Iteration in umgekehrter Reihenfolge können wir -1 als letztes Element in der Liste verwenden

### Hinzufügen, Entfernen, Aktualisieren und Löschen von Listenelementen
list.append(elem) -- fügt ein einzelnes Element an das Ende der Liste an. Häufiger Fehler: gibt nicht die neue Liste zurück, sondern ändert nur das Original.
list.insert(index, elem) -- fügt das Element am angegebenen Index ein, wobei Elemente nach rechts verschoben werden.
list.extend(list2) fügt die Elemente in list2 an das Ende der Liste an. Die Verwendung von + oder += auf eine Liste ist ähnlich wie die Verwendung von extend().
list.index(elem) -- sucht das angegebene Element am Anfang der Liste und gibt seinen Index zurück. Wirft einen ValueError, wenn das Element nicht vorkommt (verwenden Sie „in“, um ohne ValueError zu prüfen).
list.remove(elem) -- sucht nach der ersten Instanz des angegebenen Elements und entfernt es (wirft einen ValueError, wenn es nicht vorhanden ist)
list.reverse() -- kehrt die Liste an Ort und Stelle um (gibt sie nicht zurück)
list.pop(index) -- Entfernt das Element am angegebenen Index und gibt es zurück. Gibt das ganz rechte Element zurück, wenn index weggelassen wird (ungefähr das Gegenteil von append()).

### For-Schleife
Die For-Schleife wird verwendet um ein Stück Code für eine bestimmte Anzahl von Iterationen zu wiederholen. So kann zum Beispiel durch eine Liste iteriert werden um für jedes Element in der Liste den gleichen Code auszuführen. 
Sobald durch das letzte Eltement iteriert wurde, endet die Schleife automatisch.

Mit der Funktion variable.lower() kann man eine Zeichenkette in Kleinbuchstaben umzuwandeln. Dies kann hilfreich sein, wenn man den sicherstellen möchte, dass es für den User-Input keine Rolle spielt ob dieser gewisse Begriffe in Gross- oder Kleinbuchstaben eingibt. 
Mit der Funktion len(), kann die Anzahl von Elementen in einer Liste geprüft werden. 
Mit der „in“-Klausel, kann man sicherstellen, dass z.B. Suchergebnisse zurückgegeben werden, welche teilweise mit dem Input übereinstimmen.

### While-Schleife
Eine while-Schleife wird oft verwendet, um einen Codeblock zu wiederholen, solange eine bestimmte Bedingung erfüllt ist. Anders als bei der For-Schleife, gibt es für die While-Schleife kein automatische Ende. Sie wird solange ausgeführt, bis die Bedingung nicht mehr erfüllt ist.
Es muss also sichergestellt werden, dass die Bedingung, welche den Loop unterbricht *innterhalb* des Loops definiert wird, da die Schleife ansonsten endlos weiterläuft.

### K.I.S.S. Principle
Keep It Simple, Stupid or Keep It Super Simple
Das K.I.S.S. Principle besagt, dass der Code so einfach wie möglich gehalten werden soll. Unnötig komplexe Lösungen erschweren nicht nur die Readability des Codes sondern erschweren auch die Zusammenarbeit mit anderen Developern. Der Code sollte so geschrieben werden, dass dieser von 
jedem verstanden und unterhalten / gewartet werden kann.

### DRY Principle
Don't repeat yourself
Dieses Prinzip besagt, dass man sich nicht wiederholen soll. Es ist sinnvoll sich Gedanken darüber zu machen welche Teile eines Codes universal gestaltet werden sollten, so dass diese in anderen Teilen der Applikation wiederverwendet und angepasst werden können, anstatt die gleichen Codeteile 
wiederholt zu schreiben. Dies unterstütz die Maintainability des Codes, denn je nach Umständen müsste ein Developer ansonsten bei einer Anpassung sicherstellen können, dass an jedem einzelnen Ort im Code diese Anpassung ebenso reflektiert wird. Dies ist enorm fehleranfällig und sollte daher vermieden werden.

### Funktionen
Funktionen stellen sicher, dass eine gewisse Modularität im Code gewährleistet werden kann. Sie unterstützen das DRY Prinzip, da Funktionen "Aktionen" darstellen, welche wiederverwendet werden können. 

*Reflexion über Relevanz für unser Projekt:*
In den letzten Unterrichtseinheiten haben wir uns mit Listen, Loops, Funktionen und den K.I.S.S- und DRY Prinzipien beschäftigt. Für unser Projekt dürfte insbesondere der For-Loop wichtig werden, wenn wir z.B. herausfinden möchten, welche Hotels sich alle in einer bestimmten Stadt befinden und daher über alle Hotels iterieren
möchten, oder wenn geprüft werden soll ob ein bestimmter Raum im gewünschten Reisezeitraum vergübar ist oder nicht und dazu die Buchungen überprüft werden müssen. Genauso wichtig dürften auch die Funktionen werden, da wir irgendwie Code schreiben können müssen, der es uns erlaubt z.B. neue Hotels und Räume zu kreieren oder Daten 
von bestehenden Instanzen anzupassen. 

### Errors and Exceptions

Errors und Exceptions sind Probmele, welche von Python nicht interpretiert werden können und verhindern, dass das Programm überhaupt ausgeführt wird (Errors) oder während der Programmausführung auftauchen (Exceptions). Häufig deutet es darauf hin, dass im Code etwas fehlt oder unvollständig ist.
Häufige Beispiele für Errors sind:
SyntaxError: Dies können z.B. fehlende Klammern, ein fehlender Doppelpunkt in einer Funktion oder fehlende Schlüsselwörter sein.
IndentationError: Hierbei handelt es sich um einen Fehler in der Anzahl Leerschläge oder Tabs bevor der Code geschrieben wird. Die richtige Indentation ist wichtig, damit klar definiert ist zu welchen "Code-Block" der Code gehört. Alles was z.B. in den gleichen Loop gehört, muss sich "innerhalb" des Loops befinden und kann
daher nicht auf der gleichen Zeile wie der Loop selbst beginnen -> es braucht eine Indentation.
NameError: Die Verwendung von Variablen bevor diese überhaupt definiert wurden
Exceptions können mit "try" "except" gut behandelt werden. Hier wird sodann unter "try" derjenige Codeblock vermerkt, der potentiell zu einer Exception führen könnte und unter "except" derjenige Code, welcher beim Eintreten einer solchen Exception stattdessen ausgeführt werden soll.

*Reflexion über Relevanz für unser Projekt:*
Den "Try - Except" Approach können wir für unser Projekt noch nicht genau einordnen, es erscheint zur Zeit noch etwas unklar in welchem Kontext wir diesen genau einsetzen können. Allerdings ist es für den Aufbau unserer Klassen unerlässlich, dass wir z.B. prüfen ob ein eingegebenes Value dem erwarteten Datentyp entspricht oder non-nullable Felder auch tatsächlich
einen Wert enthalten bei der Erstellung von neuen Objekten aus der jeweiligen Klasse. So können wir z.B. sicherstellen, dass keine ValueError oder TypeError entstehen.

## Zusammenfassung Unterrichtseinheit 2 Iteration 1

In dieser Unterrichtseinheit haben wir uns mit den Grundlagen von Object Oriented Programming (OOP) beschaeftigt. Wir haben gelernt, dass eine **class** ein Bauplan ist, in dem festgelegt wird, welche **attribute** (z. B. name, age, city) und **methoden** (z. B. eat(), sleep(), play()) ein Objekt besitzen soll. Eine **class** selbst fuehrt noch keinen Code aus, sondern dient als Vorlage fuer die Erstellung von **objects**. Ein **object** ist eine konkrete Instanz einer **class** mit eigenen Werten und kann die in der Klasse definierten **methoden** nutzen.
Ein zentrales Element ist der **__init__**-Konstruktor. Er wird automatisch ausgefuehrt, wenn ein Objekt erstellt wird, und dient zur Initialisierung der **attribute**. Der **self**-Parameter verweist dabei auf das aktuelle Objekt und ist notwendig, um innerhalb der Klasse auf die **attribute** und **methoden** zuzugreifen. Ohne **self** koennen innerhalb einer Methode keine objektbezogenen Daten verwendet werden.

## Zusammenfassung Unterrichtseinheit 2 Iteration 2

Der Schwerpunkt dieser Unterrichtseinheit lag auf Encapsulation, Data Hiding und Private/Public Attributes. So können Attribute als "privat" oder "public" definiert werden. Ist ein Attribut "privat" ist es ausserhalb der Klasse nicht direkt zugänglich für einen Client. In Python wird ein privates Attribut durch zwei Unterstriche "__" vor dem Attributnamen definiert. Wenn Attribute einer Klasse als privat definiert sind, müssen Methoden zum Abrufen oder Ändern des Attributwerts integriert werden. Mit dem Befehl "self." können die Attribute innerhalb der Klasse abgefragt werden. Solche Methoden heissen Getter- und Setter-Methoden. In Python werden sie mit @property (Getter) und @nameDerEigenschaft.setter geschrieben oder alternativ mit get_nameDerEigenschaft() und set_nameDerEigenschaft(). Verfügt eine Klasse über eine konstante Variable, kann diese in Grossbuchstaben an erster Stelle geschrieben werden (class Track: MIN_PRICE = 2.99). 
In unserem Projekt haben wird die voraussichtlich benötigten Klassen erstellt und uns überlegt, welche Aktionen diese benötige. Dabei haben wir darüber diskutiert, welche unserer Klassen "privat", welche "public" sein sollten. Aus unserer Sicht macht es Sinn, wenn alle Klassen "privat" sind, da keine der Klassen direkt geändert werden sollten. In einem kurzen Austausch bestätigte uns Charuta, dass wir grundsätzlich alle Klassen "privat" machen können. Wir haben uns dazu entschieden allen Klassen eine Getter- und Setter-Funktion zu geben. Ein weiterer Diskussionspunkt war die Adresse. In der Datenbank sind Strasse, PLZ und Ort als eigenständige Felder vorhanden. Wir haben uns aber überlegt, eine Funktion zu machen wo alle Felder direkt abgefragt werden. Ähnlich dem Bespiel def get_track_details(self): return f"Title: {self.title}, Price: {self.__price:.2f}.

## Zusammenfassung Unterrichtseinheit 2 Iteration 3

In der heutigen Unterrichtseinheit haben wir die verschiedenen Beziehungsarten der Klassen angeschaut. Association: eine lose Beziehung, beide können unabhängig voneinander existieren benötigen aber einander (Mensch - Haustier). Aggregation: Die Parent-Class ist ein Container für die Child-Class. (Bibliothek - Büchern). Auch diese beiden können ohne einander existieren. Composition: Teil-von-Beziehung (Haus - Zimmer). Die Existenz der Teilobjekte ist abhängig von der Existenz des Hauptobjektes. Ohne Haus gibt es keine Zimmer. Im Anschluss an die Vorlesung haben wir im VP überprüft, welche Beziehungen unsere Classes untereinander haben. Einige waren relativ einfach wie z.B. die Beziehung zwischen Address und Hotel. Aus unserer Sicht handelt es sich dabei um eine Association, da nur eine lose Beziehung zwischen den beiden Classes besteht. Hingegen waren wir uns bei der Beziehung zwischen den Facilities und der Class Room unsicher. Haben uns aber schlussendlich für eine Aggregation entschieden, da wir der Meinung sind, dass der Raum als Container für die Facilities dient und die Facilities auch ohne einen Raum existieren kann. Wir haben dann versucht die Beziehungen in Code umzusetzen, haben aber dabei gemerkt, dass wir die verschiedenen Beziehungen nochmals überprüfen müssen.

*Gruppenbesprechung und Reflexion zu den Beziehungen in unserem Projekt:*

- Gast und Booking Klassen haben eine "composition"-Beziehung, weil die Person kein "Gast" ist, wenn sie keine Buchung hat, entsprechent gibt es den "Gast" auch nicht bzw. wir haben von der Person keine Daten. Wir gehen hierbei davon aus, dass eine Buchung nie gelöscht wird, sondern nur storniert werden kann. Es kann daher nicht vorkommen, dass ein "Gast" beim Löschen einer Buchung plötzlich ebenfalls gelöscht wäre.
- Booking und Invoice haben eine eine "composition"-Beziehung, weil es keine Rechnung geben kann ohne Buchung. Die Buchung wird nie gelöscht, höchstens storniert. Die Rechnung kann aber gelöscht werden ohne dass dies die Buchung löscht.
- Room und Booking haben eine "aggregation"-Beziehung. Hier wurde ursprünglich eine "composition" angedacht, da es keine Buchung geben kann für einen Raum wenn es den Raum nicht gibt. Diese Überlegung haben wir allerdings verworfen, da wir es nicht für relevant befinden ob der Raum an sich existiert, sondern ob dieser Raum gebucht werden soll oder nicht. Es kann diesen Raum auch geben, ohne dass er je gebucht wurde. Eine Aggregation macht aus unserer Sicht daher mehr Sinn, da wir den Raum bei einer Buchung "in die Buchung" einfügen möchten.
- Address und Hotel sowie Address und Gast. Hier ist eine Association völlig ausreichend, da die Objekte dieser Klassen vollständig unabhängig voneinander existieren können, allerdings trotzdem verbunden sind (ein Hotel hat eine Adresse, ein Gast hat eine Adresse).
- Room und Roomtype haben ebenfalls eine "association"-Beziehung, weil sie unabhängig voneinander existieren können. Nicht jedes HOtel hat zwingend Räume eines bestimmten Roomtypen. Ausserdem soll verhindert werden, dass ein Roomtype gelöscht wird, wenn ein Raum gelöscht wird, da derselbe Raumtyp anderen Räumen zugeordnet sein kann. Eine Aggregation erachten wir als nicht sinnvoll, da wir den Raumtype nicht "wörtlich" *in* den Raum hineinlegen, sondern ihn damit lediglich beschreiben.
- Room und Facilities haben eine "aggregation"-Beziehung, weil die Objekte zwar unabhänging voneinander existieren können (z.B. gibt es Räume ohne Föhn und es gibt einen Föhn ohne Raum), aber wir legen den Föhn *in* den Raum für diejenigen Räume, welche einen haben.

Das Ausarbeiten der Beziehungen zwischen den Klassen erachten wir als komplex. In vielen Konstellationen gibt es mehrere, teils gute, Begründungen weshalb die eine oder andere Beziehungsform valide sein könnte. In der Realität hängt dies stark vom Verwendungszweck der Klassen ab. Es ist wichtig zu versuchen vorauschauend zu denken, so dass bei zukünftigen Anpassungen oder Erweiterungen keine Probleme enstehen, allerdings empfinden wir dies nicht als "straight-forward". Die Beziehungen unserer Klassen haben wir daher auch mehrmals angepasst, bis wir uns auf eine Lösung für unser Projekt geeinigt haben. 

