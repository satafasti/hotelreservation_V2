from business_logic.hotel_manager import HotelManager
from business_logic.booking_manager import BookingManager
from business_logic.guest_manager import GuestManager
from business_logic.room_manager import RoomManager
from business_logic.room_facilities_manager import RoomFacilitiesManager
from business_logic.room_type_manager import RoomTypeManager
from business_logic.facilities_manager import FacilitiesManager
from business_logic.address_manager import AddressManager

from data_access.facilities_dal import FacilityDataAccess
from data_access.room_type_dal import RoomTypeDataAccess



from model.address import Address
from model.booking import Booking
from model.hotel import Hotel
from model.room import Room
from model.room_type import Room_Type

from typing import List
from datetime import datetime
import pandas as pd
import sqlite3
import plotly.express as px
import matplotlib.pyplot as plt

class AdminUI:
    def __init__(self, db_path: str | None = None) -> None:
        self.__hotel_manager = HotelManager(db_path)
        self.__booking_manager = BookingManager(db_path)
        self.__guest_manager = GuestManager(db_path)
        self.__room_manager = RoomManager()
        self.__room_facilities_manager = RoomFacilitiesManager(db_path)
        self.__room_type_manager = RoomTypeManager(RoomTypeDataAccess())
        self.__facilities_manager = FacilitiesManager(FacilityDataAccess())
        self.__address_manager = AddressManager(db_path)


#3. Als Admin des Buchungssystems möchte ich die Möglichkeit haben, Hotelinformationen zu pflegen, um aktuelle Informationen im System zu haben.
#3.1. Ich möchte neue Hotels zum System hinzufügen
    def admin_create_hotel_ui(self) -> None:
        print("Hallo - Bitte erstellen Sie ein neues Hotel.")
        street = input("Gib die Strasse des Hotels ein: ")
        city = input("Gib den Ort des Hotels ein: ")
        zip_code = input("Gib den Zip-Code des Hotels ein: ")
        name = input("Gib den Hotelname ein: ")
        stars = int(input("Gib die Anzahl Hotelsterne ein: "))

        print("Du musst zuerst ein Zimmer erstellen.")
        room_number = input("Gib eine Zimmernummer ein: ")
        description = input(
            "Gib den Zimmertyp an (Single (max.1), Double (max.2), Suite (max.4), Family Room (max.5), Penthouse (max.6)): ")
        max_guests = int(input(
            "Maximale Anzahl Gäste für das Zimmer (Single (max.1), Double (max.2), Suite (max.4), Family Room (max.5), Penthouse (max.6): "))
        price_per_night = float(input("Gib den Preis pro Nacht für das Zimmer an: "))

        manager = HotelManager()
        all_facilities = manager.get_all_facilities()

        selected_facility_ids_first_room = []
        if all_facilities:
            add_facilities = input("\nMöchtest du Ausstattung hinzufügen? (ja/nein): ").lower()
            if add_facilities == "ja":
                print("\nVerfügbare Ausstattung:")
                for i, facility in enumerate(all_facilities, 1):
                    print(f"{i}. {facility.facility_name}")

                print("\nGib die Nummern der gewünschten Ausstattung ein (durch Komma getrennt, z.B. 1,3,5):")
                print("Oder drücke Enter um keine Ausstattung hinzuzufügen")

                facility_input = input("Auswahl: ").strip()
                if facility_input:
                    try:
                        facility_numbers = [int(x.strip()) for x in facility_input.split(",")]
                        for num in facility_numbers:
                            if 1 <= num <= len(all_facilities):
                                selected_facility_ids_first_room.append(all_facilities[num - 1].facility_id)

                        if selected_facility_ids_first_room:
                            selected_names = [all_facilities[num - 1].facility_name for num in facility_numbers if
                                              1 <= num <= len(all_facilities)]
                            print(f"Ausgewählte Ausstattung: {', '.join(selected_names)}")
                    except ValueError:
                        print("Ungültige Eingabe - keine Ausstattung hinzugefügt")

        address_id = 1
        hotel_id = 1
        room_id = 1
        type_id = 1

        address = Address(address_id, street, city, zip_code)
        hotel = Hotel(hotel_id, name, stars, address_id)
        room_type = Room_Type(type_id, description, max_guests)
        room = Room(room_id, hotel, room_number, room_type, price_per_night)

        manager = HotelManager()
        result = manager.create_hotel(hotel, address, room)
        print(f"Hotel '{result.name}' erfolgreich erstellt")

        if selected_facility_ids_first_room:
            added = manager.add_facilities_to_first_room(result.hotel_id, selected_facility_ids_first_room)
            if added:
                print(f"{added} Facilities für erstes Zimmer hinzugefügt.")

        while True:
            add_more_rooms = input("\nMöchtst du ein weiteres Zimmer hinzufügen? (ja/nein): ").lower()
            if add_more_rooms != "ja":
                break

            print("\nNeues Zimmer hinzufügen:")
            room_number = input("Gib eine Zimmernummer ein: ")
            description = input(
                "Gib den Zimmertyp an (Single (max.1), Double (max.2), Suite (max.4), Family Room (max.5), Penthouse (max.6)): ")
            max_guests = int(input(
                "Maximale Anzahl Gäste für das Zimmer (Single (max.1), Double (max.2), Suite (max.4), Family Room (max.5), Penthouse (max.6): "))
            price_per_night = float(input("Gib den Preis pro Nacht für das Zimmer an: "))

            selected_facility_ids = []
            if all_facilities:
                add_facilities = input("\nMöchtest du Ausstattung hinzufügen? (ja/nein): ").lower()
                if add_facilities == "ja":
                    print("\nVerfügbare Ausstattung:")
                    for i, facility in enumerate(all_facilities, 1):
                        print(f"{i}. {facility.facility_name}")

                    print("\nGib die Nummern der gewünschten Ausstattung ein (durch Komma getrennt, z.B. 1,3,5):")
                    print("Oder drücke Enter um keine Ausstattung hinzuzufügen")

                    facility_input = input("Auswahl: ").strip()
                    if facility_input:
                        try:
                            facility_numbers = [int(x.strip()) for x in facility_input.split(",")]
                            for num in facility_numbers:
                                if 1 <= num <= len(all_facilities):
                                    selected_facility_ids.append(all_facilities[num - 1].facility_id)

                            if selected_facility_ids:
                                selected_names = [all_facilities[num - 1].facility_name for num in facility_numbers if
                                                  1 <= num <= len(all_facilities)]
                                print(f"Ausgewählte Ausstattung: {', '.join(selected_names)}")
                        except ValueError:
                            print("Ungültige Eingabe - keine Ausstattung hinzugefügt")

            manager.add_room_to_hotel(result.hotel_id, room_number, description, max_guests, price_per_night,
                                      selected_facility_ids)

        print(f"\nHotel '{result.name}' mit allen Zimmern erfolgreich erstellt.")


    # 3.2. Ich möchte Hotels aus dem System entfernen
    def admin_delete_hotel_ui(self) -> None:
        manager = HotelManager()
        while True:
            hotel_name = input("Gib den Namen des Hotels an, dass du löschen möchtest: ")
            found_hotels = manager.read_hotels_by_similar_name(hotel_name)

            if not found_hotels:
                print("Keine Hotels mit diesem Namen gefunden.")
                continue

            for i, hotel in enumerate(found_hotels, 1):
                print(f"{i}. Hotel ID: {hotel.hotel_id}, Hotelname: {hotel.name}, Address ID: {hotel.address_id}")

            try:
                choice = int(input(f"Wähle Hotel (1-{len(found_hotels)}): "))
                if not (1 <= choice <= len(found_hotels)):
                    print("Ungültige Auswahl. Bitte eine Zahl zwischen 1 und {len(found_hotels)} eingeben.")
                    continue
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")
                continue

            selected_hotel = found_hotels[choice - 1]

            if input(f"'{selected_hotel.name}' löschen? (ja/nein): ") == "ja":
                try:
                    manager.delete_hotel(selected_hotel)
                    print(f"Hotel '{selected_hotel.name}' erfolgreich gelöscht.")
                except Exception as e:
                    print(f"Fehler beim Löschen: {e}")

            if input("Weiteres Hotel löschen? (ja/nein): ") != "ja":
                break


    # 3.3. Ich möchte die Informationen bestimmter Hotels aktualisieren, z. B. den Namen, die Sterne usw.
    #Szenario 1
    def update_hotel_details_ui(self) -> None:
        manager = HotelManager()
        while True:
            hotel_name = input("Gib den Namen des Hotels an, dass du aktualisieren möchtest: ")
            found_hotels = manager.read_hotels_by_similar_name(hotel_name)

            if not found_hotels:
                print("Keine Hotels mit diesem Namen gefunden.")
                continue

            for i, hotel in enumerate(found_hotels, 1):
                print(f"{i}. Hotel ID: {hotel.hotel_id}, Hotelname: {hotel.name}, Address ID: {hotel.address_id}")

            try:
                choice = int(input(f"Wähle Hotel (1-{len(found_hotels)}): "))
                if not (1 <= choice <= len(found_hotels)):
                    print(f"Ungültige Auswahl. Bitte eine Zahl zwischen 1 und {len(found_hotels)} eingeben.")
                    continue
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")
                continue

            selected_hotel = found_hotels[choice - 1]

            if input(f"'{selected_hotel.name}' aktualisieren? (ja/nein): ") == "ja":
                try:
                    new_name = input(
                        f"Gib den neuen Hotelnamen ein oder lass es leer, wenn du '{selected_hotel.name}' behalten möchtest: ")
                    if new_name:
                        selected_hotel.name = new_name
                    else:
                        print("Kein Name eingegeben.")

                    new_stars = input(
                        f"Gib die neuen Sterne an (1–5, aktuell: {selected_hotel.stars}) oder lass es leer, wenn du die aktuellen Sterne behalten willst: ")
                    if new_stars:
                        try:
                            selected_hotel.stars = int(new_stars)
                        except ValueError:
                            print("Bitte eine gültige Zahl für Sterne eingeben (1-5).")
                            continue
                    else:
                        print("Keine Sterne eingegeben.")

                    address_manager = AddressManager()
                    current_address = address_manager.read_address_by_id(selected_hotel.address_id)

                    new_street = input(
                        f"Gib die neue Strasse des Hotels ein oder lass es leer, wenn du '{current_address.street}' behalten möchtest: ")
                    if new_street:
                        current_address.street = new_street
                    else:
                        print("Keine Strasse eingegeben.")

                    new_city = input(
                        f"Gib den neuen Ort des Hotels ein oder lass es leer, wenn du '{current_address.city}' behalten möchtest: ")
                    if new_city:
                        current_address.city = new_city
                    else:
                        print("Kein Ort eingegeben.")

                    new_zip_code = input(
                        f"Gib den neuen Zip-Code des Hotels ein oder lass es leer, wenn du '{current_address.zip_code}' behalten möchtest: ")
                    if new_zip_code:
                        current_address.zip_code = new_zip_code
                    else:
                        print("Kein Zip Code eingegeben.")

                    manager.update_hotel(selected_hotel)
                    address_manager.update_address(current_address)
                    print(
                        f"Hotel wurde erfolgreich aktualisiert. Hotel ID: {selected_hotel.hotel_id}, Hotelname: {selected_hotel.name}, Sterne: {selected_hotel.stars}, Address ID: {selected_hotel.address_id}")

                except Exception as e:
                    print(f"Fehler beim Aktualisieren: {e}")

            if input("Weiteres Hotel aktualisieren? (ja/nein): ") != "ja":
                break


    #Szenario 2
    def update_hotel_details_without_address_ui(self) -> None:
        manager = HotelManager()
        while True:
            hotel_name = input("Gib den Namen des Hotels an, dass du aktualisieren möchtest: ")
            found_hotels = manager.read_hotels_by_similar_name(hotel_name)

            if not found_hotels:
                print("Keine Hotels mit diesem Namen gefunden.")
                continue

            for i, hotel in enumerate(found_hotels, 1):
                print(f"{i}. Hotel ID: {hotel.hotel_id}, Hotelname: {hotel.name}, Address ID: {hotel.address_id}")

            try:
                choice = int(input(f"Wähle Hotel (1-{len(found_hotels)}): "))
                if not (1 <= choice <= len(found_hotels)):
                    print(f"Ungültige Auswahl. Bitte eine Zahl zwischen 1 und {len(found_hotels)} eingeben.")
                    continue
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")
                continue

            selected_hotel = found_hotels[choice - 1]

            if input(f"'{selected_hotel.name}' aktualisieren? (ja/nein): ") == "ja":
                try:
                    new_name = input(
                        f"Gib den neuen Hotelnamen ein oder lass es leer, wenn du '{selected_hotel.name}' behalten möchtest: ")
                    if new_name:
                        selected_hotel.name = new_name
                    else:
                        print("Kein Name eingegeben.")

                    new_stars = input(
                        f"Gib die neuen Sterne an (1–5, aktuell: {selected_hotel.stars}) oder lass es leer, wenn du die aktuellen Sterne behalten willst: ")
                    if new_stars:
                        try:
                            selected_hotel.stars = int(new_stars)
                        except ValueError:
                            print("Bitte eine gültige Zahl für Sterne eingeben (1-5).")
                            continue
                    else:
                        print("Keine Sterne eingegeben.")

                    manager.update_hotel(selected_hotel)
                    print(
                        f"Hotel wurde erfolgreich aktualisiert. Hotel ID: {selected_hotel.hotel_id}, Hotelname: {selected_hotel.name}, Sterne: {selected_hotel.stars}")

                except Exception as e:
                    print(f"Fehler beim Aktualisieren: {e}")

            if input("Weiteres Hotel aktualisieren? (ja/nein): ") != "ja":
                break



    #8. Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.

    def read_all_bookings_ui(self) -> None:

        df = self.__booking_manager.get_all_bookings_as_dataframe()

        print("\n=== ÜBERSICHT ALLER BUCHUNGEN ===")

        if df.empty:
            print("Keine Buchungen gefunden.")
            return

        print(f"Insgesamt {len(df)} Buchungen gefunden:\n")


        display_df = df.copy()
        display_df.columns = ['ID', 'Gast', 'Hotel', 'Zimmer', 'Typ', 'Check-in', 'Check-out', 'Betrag (CHF)', 'Status']


        display_df['Betrag (CHF)'] = display_df['Betrag (CHF)'].apply(lambda x: f"{x:.2f}")

        print(display_df.to_string(index=False, max_colwidth=20))
        print(f"\nGesamtanzahl: {len(df)} Buchungen")

    #9. Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.

    def show_rooms_with_facilities_by_hotel_ui(self) -> None:

        hotels = self.__hotel_manager.read_all_hotels()
        if not hotels:
            print("Keine Hotels gefunden.")
            return

        print("Verfügbare Hotels:")
        for h in hotels:
            print(f"{h.hotel_id}: {h.name}")

        try:
            hotel_id = int(input("Bitte Hotel-ID eingeben: "))
        except ValueError:
            print("Ungültige Eingabe.")
            return

        hotel = self.__hotel_manager.read_hotel(hotel_id)
        if not hotel:
            print("Hotel nicht gefunden.")
            return

        rooms = self.__room_manager.read_rooms_by_hotel(hotel)
        if not rooms:
            print("Keine Zimmer für dieses Hotel gefunden.")
            return

        print(f"Zimmer im Hotel '{hotel.name}':")
        for room in rooms:
            facilities = self.__room_facilities_manager.read_facilities_by_room(room)
            names = [f.facility_name for f in facilities]
            ausstattung = ", ".join(names) if names else "Keine Ausstattung"
            print(f"- Zimmernummer: {room.room_number}, Zimmer-ID: {room.room_id}, Ausstattung: {ausstattung}")


    #10. Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat.
    def admin_main_menu_ui(self) -> None:
        room_type_manager = RoomTypeManager(RoomTypeDataAccess())
        facility_manager = FacilitiesManager(FacilityDataAccess())
        room_manager = RoomManager()
        hotel_manager = HotelManager()
        guest_manager = GuestManager()

        while True:
            print("\nAdmin-Menü – Stammdaten verwalten:")
            print("1. Zimmertyp ändern")
            print("2. Ausstattung umbenennen")
            print("3. Zimmerpreis oder Nummer ändern")
            print("4. Hotelname oder Sterne ändern")
            print("5. Gastinformationen ändern")
            print("6. Zimmerpreise nach Zimmertyp ändern")
            print("0. Beenden")
            auswahl = input("Wähle eine Option: ")

            if auswahl == "1":
                try:
                    type_id = int(input("Zimmertyp-ID: "))
                    room_type = room_type_manager.read_room_type_by_id(type_id)
                    if not room_type:
                        print("Zimmertyp nicht gefunden.")
                        continue
                    print(f"Aktuell: {room_type.description} für max. {room_type.max_guests} Gäste")
                    new_description = input("Neue Beschreibung (leer lassen für keine Änderung): ")
                    max_guest_input = input("Neue max. Gästeanzahl (leer lassen für keine Änderung): ")
                    description = new_description if new_description.strip() else room_type.description
                    max_guests = int(max_guest_input) if max_guest_input.strip() else room_type.max_guests
                    room_type_manager.update_room_type(type_id, description, max_guests)
                    updated = room_type_manager.read_room_type_by_id(type_id)
                    print(f"Zimmertyp aktualisiert: {updated.description} für max. {updated.max_guests} Gäste")
                except Exception as e:
                    print("Fehler:", e)

            elif auswahl == "2":
                try:
                    facility_id = int(input("Ausstattungs-ID: "))
                    facility = facility_manager.read_facility_by_id(facility_id)
                    if not facility:
                        print("Ausstattung nicht gefunden.")
                        continue
                    print(f"Aktuell: {facility.facility_name}")
                    new_name = input("Neuer Name")
                    if new_name.strip():
                        facility_manager.update_facility(facility_id, new_name)
                    else:
                        updated = facility_manager.read_facility_by_id(facility_id)
                        print(f"Ausstattung aktualisiert: {updated.facility_name}")
                except Exception as e:
                    print("Fehler:", e)

            elif auswahl == "3":
                try:
                    room_id = int(input("Zimmer-ID: "))
                    room = room_manager.read_room_by_id(room_id)
                    if not room:
                        print("Zimmer nicht gefunden.")
                        continue

                    print(f"Aktuell: Nummer {room.room_number}, Preis {room.price_per_night:.2f}")

                    new_number = input("Neue Zimmernummer (leer lassen für keine Änderung): ")
                    new_price_input = input(
                        "Neuer Preis pro Nacht (leer lassen für keine Änderung): "
                    )

                    if new_number.strip():
                        room.room_number = new_number
                    if new_price_input.strip():
                        room.price_per_night = float(new_price_input)

                    room_manager.update_room(room)
                    print(f"Zimmer aktualisiert: Nummer {room.room_number}, Preis {room.price_per_night:.2f}")

                except Exception as e:
                    print("Fehler:", e)


            elif auswahl == "4":
                try:
                    hotel_id = int(input("Hotel-ID: "))
                    hotel = hotel_manager.read_hotel(hotel_id)
                    if not hotel:
                        print("Hotel nicht gefunden.")
                        continue
                    print(f"Aktuell: {hotel.name}, {hotel.stars} Sterne")
                    new_name = input("Neuer Hotelname (leer lassen für keine Änderung): ")
                    stars_input = input("Neue Sterneanzahl (1-5, leer lassen für keine Änderung): ")
                    if new_name.strip():
                        hotel.name = new_name
                    if stars_input.strip():
                        hotel.stars = int(stars_input)
                    hotel_manager.update_hotel(hotel)
                    updated = hotel_manager.read_hotel(hotel_id)
                    print(f"Hotel aktualisiert: {updated.name}, {updated.stars} Sterne")
                except Exception as e:
                    print("Fehler:", e)

            elif auswahl == "5":
                try:
                    guest_id = int(input("Gast-ID: "))
                    guest = guest_manager.get_guest_by_id(guest_id)
                    if not guest:
                        print("Gast nicht gefunden.")
                        continue
                    print(f"Aktuell: {guest.first_name} {guest.last_name}, {guest.email}")
                    new_first = input("Neuer Vorname (leer lassen für keine Änderung): ")
                    new_last = input("Neuer Nachname (leer lassen für keine Änderung): ")
                    new_email = input("Neue E-Mail (leer lassen für keine Änderung): ")
                    if new_first.strip():
                        guest.first_name = new_first
                    if new_last.strip():
                        guest.last_name = new_last
                    if new_email.strip():
                        guest.email = new_email
                    guest_manager.update_guest(guest)
                    updated = guest_manager.get_guest_by_id(guest_id)
                    print(f"Gast aktualisiert: {updated.first_name} {updated.last_name}, {updated.email}")

                except Exception as e:
                    print("Fehler:", e)

            elif auswahl == "6":
                try:
                    type_id = int(input("Zimmertyp-ID: "))
                    room_type = room_type_manager.read_room_type_by_id(type_id)
                    if not room_type:
                        print("Zimmertyp nicht gefunden.")
                        continue
                    rooms = room_manager.read_room_details(type_id)
                    if not rooms:
                        print("Keine Zimmer mit diesem Zimmertyp gefunden.")
                        continue
                    print(f"Zimmertyp: {room_type.description} - {len(rooms)} Zimmer")
                    for room in rooms:
                        print(f"- Zimmer-ID: {room.room_id}, Nummer {room.room_number}, Preis {room.price_per_night:.2f}")
                    price_input = input("Neuer Preis pro Nacht für alle diese Zimmer (leer lassen für keine Änderung): ")
                    if price_input.strip():
                        new_price = float(price_input)
                        for room in rooms:
                            room.price_per_night = new_price
                            room_manager.update_room(room)
                        print(f"Preis aller Zimmer vom Typ '{room_type.description}' auf {new_price:.2f} gesetzt.")
                    else:
                        print("Keine Preisänderung vorgenommen.")
                except Exception as e:
                    print("Fehler:", e)

            elif auswahl == "0":
                print("Admin-Menü wird beendet.")
                break
            else:
                print("Ungültige Auswahl.")


    # User Stories mit Datenvisualisierung
    # 2. Als Admin möchte ich eine Aufschlüsselung der demografischen Merkmale meiner Gäste sehen, damit ich gezieltes Marketing planen kann. Hint: Wählt ein geeignetes Diagramm, um die Verteilung der Gäste nach verschiedenen Merkmalen darzustellen (z. B. Altersspanne, Nationalität, wiederkehrende Gäste). Möglicherweise müssen Sie der Tabelle „Gäste“ einige Spalten hinzufügen.

    def demographics_ui(self) -> None:

        print("DEMOGRAFISCHE ANALYSE")
        print("-" * 30)

        guest_manager = GuestManager()
        hotel_manager = HotelManager()
        allhotels = hotel_manager.read_all_hotels()
        for hotel in allhotels:
            print(f"• {hotel.name} ({hotel.stars} stars) - ID: {hotel.hotel_id}")

        hotel_id = int(input("Hotel-ID: "))

        guest_details = guest_manager.get_all_guest_details_for_hotel(hotel_id)
        main_df = guest_manager.calculate_age_and_convert_to_dataframe(guest_details)
        print(f"Gäste gefunden: {len(main_df)}")

        print("\nMerkmale:")
        print("1=Städte  2=Nationalitäten  3=Geschlecht  4=Familienstand  5=Alter")
        choice = input("Wählen (1-5): ")

        if choice == "1":
            count_df = guest_manager.create_city_count_dataframe(main_df)
            name = "Städte"
        elif choice == "2":
            count_df = guest_manager.create_nationality_count_dataframe(main_df)
            name = "Nationalitäten"
        elif choice == "3":
            count_df = guest_manager.create_gender_count_dataframe(main_df)
            name = "Geschlecht"
        elif choice == "4":
            count_df = guest_manager.create_marital_status_count_dataframe(main_df)
            name = "Familienstand"
        elif choice == "5":
            count_df = guest_manager.create_age_group_count_dataframe(main_df)
            name = "Altersgruppen"
        else:
            print("Ungültige Wahl")
            return

        print(f"\n{name}:")
        print(count_df.to_string(index=False))

        chart = input("\nDiagramm (p=Pie, b=Bar): ").lower()
        title = f"Hotel {hotel_id}: {name}"

        if chart == "p":
            guest_manager.create_universal_pie_chart(count_df, title)
        elif chart == "b":
            guest_manager.create_universal_bar_chart(count_df, title)
