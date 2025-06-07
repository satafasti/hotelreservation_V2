from business_logic.hotel_manager import HotelManager

from data_access.address_dal import AddressDataAccess
from data_access.booking_dal import BookingDataAccess
from data_access.facilities_dal import FacilityDataAccess
from data_access.guest_dal import GuestDataAccess
from data_access.hotel_dal import HotelDataAccess
from data_access.room_dal import RoomDataAccess
from data_access.room_type_dal import RoomTypeDataAccess
from data_access.room_facilities_dal import RoomFacilitiesDataAccess

from model.address import Address
from model.booking import Booking
from model.hotel import Hotel
from model.room import Room
from model.room_type import Room_Type

from typing import List
from datetime import datetime


#3. Als Admin des Buchungssystems möchte ich die Möglichkeit haben, Hotelinformationen zu pflegen, um aktuelle Informationen im System zu haben.
#3.1. Ich möchte neue Hotels zum System hinzufügen
def admin_create_hotel_ui():
    print("Hallo - Bitte erstellen Sie ein neues Hotel.")
    street = input("Gib die Strasse des Hotels ein: ")
    city = input("Gib den Ort des Hotels ein: ")
    zip_code = input("Gib den Zip-Code des Hotels ein: ")
    name = input("Gib den Hotelname ein: ")
    stars = int(input("Gib die Anzahl Hotelsterne ein: "))
    print("Du musst zuerst ein Zimmer erstellen.")
    room_number = input("Gib eine Zimmernummer ein: ")
    description = input("Gib den Zimmertyp an: ")
    max_guests = int(input("Maximale Anzahl Gäste für das Zimmer: "))
    price_per_night = float(input("Gib den Preis pro Nacht für das Zimmer an: "))
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
    print("Hotel erfolgreich erstellt:", result)



# 3.2. Ich möchte Hotels aus dem System entfernen
def admin_delete_hotel_ui():
    hotel_name = input("Gib den Namen des Hotels an, dass du löschen möchtest: ")
    manager = HotelManager()
    found_hotels = manager.read_hotels_by_similar_name(hotel_name)
    for i, hotel in enumerate(found_hotels, 1):
        print(f"{i}. Hotel ID: {hotel.hotel_id}, Hotelname: {hotel.name}, Address ID: {hotel.address_id}")
    choice = int(input(f"Wähle Hotel (1-{len(found_hotels)}): "))
    selected_hotel = found_hotels[choice - 1]
    if input(f"'{selected_hotel.name}' löschen? (ja/nein): ") == "ja":
        manager.delete_hotel(selected_hotel)
        print(f"Hotel '{selected_hotel.name}' wurde gelöscht.")


# 3.3. Ich möchte die Informationen bestimmter Hotels aktualisieren, z. B. den Namen, die Sterne usw.
#Szenario 1
def update_hotel_details_ui():
    hotel_name = input("Gib den Namen des Hotels an, dass du aktualisieren möchtest: ")
    manager = HotelManager()
    found_hotels = manager.read_hotels_by_similar_name(hotel_name)
    for i, hotel in enumerate(found_hotels, 1):
        print(f"{i}. Hotel ID: {hotel.hotel_id}, Hotelname: {hotel.name}, Address ID {hotel.address_id}")
    choice = int(input(f"Wähle Hotel (1-{len(found_hotels)}): "))
    selected_hotel = found_hotels[choice - 1]
    if input(f"'{selected_hotel.name}' aktualisieren? (ja/nein): ") == "ja":
        new_name = input(f"Gib den neuen Hotelnamen ein oder lass es leer, wenn du '{hotel.name}' behalten möchtest: ")
        if new_name:
            selected_hotel.name = new_name
        else:
            print("Kein Name eingegeben.")
        new_stars = input(f"Gib die neuen Sterne an (1–5, aktuell: {hotel.stars}) oder lass es leer, wenn du die aktuellen Sterne behalten willst: ")
        if new_stars:
            selected_hotel.stars = int(new_stars)
        else:
            print("Keine Sterne eingeben.")

        address_dal = AddressDataAccess()
        hotel_dal = HotelDataAccess()
        current_address = address_dal.read_address_by_id(selected_hotel.address_id)

        new_street = input(f"Gib die neue Strasse des Hotels ein oder lass es leer, wenn du '{current_address.street} behalten möchtest: ")
        if new_street:
            current_address.street = new_street
        else:
            print("Keine Strasse eingegeben.")

        new_city = input(f"Gib den neuen Ort des Hotels ein oder lass es leer, wenn du '{current_address.city} behalten möchtest: ")
        if new_city:
            current_address.city = new_city
        else:
            print("Kein Ort eingegeben.")
        new_zip_code = input(f"Gib den neuen Zip-Code des Hotels ein oder lass es leer, wenn du {current_address.zip_code} behalten möchtest: ")
        if new_zip_code:
            current_address.zip_code = new_zip_code
        else:
            print("Kein Zip Code eingegeben.")
    hotel_dal.update_hotel(selected_hotel)
    address_dal.update_address(current_address)
    print(f"Hotel wurde erfolgreich aktualisiert. Hotel ID: {selected_hotel.hotel_id}, Hotelname: {selected_hotel.name}, Sterne: {selected_hotel.stars}, Address ID: {selected_hotel.address_id}")


#Szenario 2
def update_hotel_details_without_address_ui():
    hotel_name = input("Gib den Namen des Hotels an, dass du aktualisieren möchtest: ")
    manager = HotelManager()
    found_hotels = manager.read_hotels_by_similar_name(hotel_name)
    for i, hotel in enumerate(found_hotels, 1):
        print(f"{i}. Hotel ID: {hotel.hotel_id}, Hotelname: {hotel.name}, Address ID {hotel.address_id}")
    choice = int(input(f"Wähle Hotel (1-{len(found_hotels)}): "))
    selected_hotel = found_hotels[choice - 1]
    if input(f"'{selected_hotel.name}' aktualisieren? (ja/nein): ") == "ja":
        new_name = input(f"Gib den neuen Hotelnamen ein oder lass es leer, wenn du '{hotel.name}' behalten möchtest: ")
    if new_name:
        selected_hotel.name = new_name
    else:
        print("Kein Name eingegeben.")
    new_stars = input(f"Gib die neuen Sterne an (1–5, aktuell: {hotel.stars}) oder lass es leer, wenn du die aktuellen Sterne behalten willst: ")
    if new_stars:
        selected_hotel.stars = int(new_stars)
    else:
        print("Keine Sterne eingeben.")
    manager.update_hotel(selected_hotel)
    print("Hotel wurde erfolgreich aktualisiert. Hotel ID: {hotel.hotel_id}, Hotelname: {hotel.name}, Sterne: {hotel.satrs}, Address ID {hotel.address_id}")


#8. Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.
def read_all_bookings_ui ():
    booking_dal = BookingDataAccess()
    guest_dal = GuestDataAccess()
    room_dal = RoomDataAccess()
    bookings: List[Booking] = booking_dal.read_all_bookings()

    print("Übersicht aller Buchungen:")
    if not bookings:
        print("Keine Buchungen gefunden.")
        return

    for b in bookings:
        status = "storniert" if b.is_cancelled else "aktiv"
        guest = guest_dal.read_guest_by_id(b.guest_id)
        if guest:
            guest_info = f"{guest.first_name} {guest.last_name} (ID: {b.guest_id})"
        else:
            guest_info = f"ID: {b.guest_id}"

        room = room_dal.read_room_by_id(b.room_id)
        if room and room.hotel:
            hotel_info = f"{room.hotel.name} (ID: {room.hotel.hotel_id})"
        else:
            hotel_info = "Unbekanntes Hotel"

        print(
            f"  - Buchung ID: {b.booking_id}, Gast ID: {b.guest_id}, "
            f"Zimmer ID: {b.room_id}, "
            f"  - Buchung ID: {b.booking_id}, Gast: {guest_info}, "
            f"Hotel: {hotel_info}, Zimmer ID: {b.room_id}, "
            f"von {b.check_in_date} bis {b.check_out_date}, "
            f"Betrag: {b.total_amount:.2f} CHF, Status: {status}"
        )


#9. Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.
def show_rooms_with_facilities_by_hotel_ui():
    hotel_dal = HotelDataAccess()
    room_dal = RoomDataAccess()
    room_fac_dal = RoomFacilitiesDataAccess()

    hotels = hotel_dal.read_all_hotels()
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

    hotel = hotel_dal.read_hotel_by_id(hotel_id)
    if not hotel:
        print("Hotel nicht gefunden.")
        return

    rooms = room_dal.read_rooms_by_hotel(hotel)
    if not rooms:
        print("Keine Zimmer für dieses Hotel gefunden.")
        return

    print(f"Zimmer im Hotel '{hotel.name}':")
    for room in rooms:
        facilities = room_fac_dal.read_facilities_by_room_id(room)
        names = [f.facility_name for f in facilities]
        ausstattung = ", ".join(names) if names else "Keine Ausstattung"
        print(f"- Zimmernummer: {room.room_number}, Zimmer-ID: {room.room_id}, Ausstattung: {ausstattung}")



#10. Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat.
def admin_main_menu_ui():
    room_type_dal = RoomTypeDataAccess()
    facility_dal = FacilityDataAccess()
    room_dal = RoomDataAccess()
    hotel_dal = HotelDataAccess()
    guest_dal = GuestDataAccess()

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
                room_type = room_type_dal.read_room_type_by_id(type_id)
                if not room_type:
                    print("Zimmertyp nicht gefunden.")
                    continue
                print(f"Aktuell: {room_type.description} für max. {room_type.max_guests} Gäste")
                new_description = input("Neue Beschreibung: ")
                new_max_guests = int(input("Neue max. Gästeanzahl: "))
                room_type_dal.update_room_type(type_id, new_description, new_max_guests)
                updated = room_type_dal.read_room_type_by_id(type_id)
                print(
                    f"Zimmertyp aktualisiert: {updated.description} für max. {updated.max_guests} Gäste"
                )
            except Exception as e:
                print("Fehler:", e)

        elif auswahl == "2":
            try:
                facility_id = int(input("Ausstattungs-ID: "))
                facility = facility_dal.read_facility_by_id(facility_id)
                if not facility:
                    print("Ausstattung nicht gefunden.")
                    continue
                print(f"Aktuell: {facility.facility_name}")
                new_name = input("Neuer Name: ")
                facility_dal.update_facility(facility_id, new_name)
                updated = facility_dal.read_facility_by_id(facility_id)
                print(f"Ausstattung aktualisiert: {updated.facility_name}")
            except Exception as e:
                print("Fehler:", e)

        elif auswahl == "3":
            try:
                room_id = int(input("Zimmer-ID: "))
                room = room_dal.read_room_by_id(room_id)
                if not room:
                    print("Zimmer nicht gefunden.")
                    continue

                print(
                    f"Aktuell: Nummer {room.room_number}, Preis {room.price_per_night:.2f}"
                )

                new_number = input("Neue Zimmernummer (leer lassen für keine Änderung): ")
                new_price_input = input(
                    "Neuer Preis pro Nacht (leer lassen für keine Änderung): "
                )

                if new_number.strip():
                    room.room_number = new_number
                if new_price_input.strip():
                    room.price_per_night = float(new_price_input)

                room_dal.update_room(room)
                print(
                    f"Zimmer aktualisiert: Nummer {room.room_number}, Preis {room.price_per_night:.2f}"
                )

            except Exception as e:
                print("Fehler:", e)


        elif auswahl == "4":
            try:
                hotel_id = int(input("Hotel-ID: "))
                hotel = hotel_dal.read_hotel_by_id(hotel_id)
                if not hotel:
                    print("Hotel nicht gefunden.")
                    continue
                print(f"Aktuell: {hotel.name}, {hotel.stars} Sterne")
                new_name = input("Neuer Hotelname: ")
                new_stars = int(input("Neue Sterneanzahl (1-5): "))
                hotel.name = new_name
                hotel.stars = new_stars
                hotel_dal.update_hotel(hotel)
                updated = hotel_dal.read_hotel_by_id(hotel_id)
                print(f"Hotel aktualisiert: {updated.name}, {updated.stars} Sterne")
            except Exception as e:
                print("Fehler:", e)

        elif auswahl == "5":
            try:
                guest_id = int(input("Gast-ID: "))
                guest = guest_dal.read_guest_by_id(guest_id)
                if not guest:
                    print("Gast nicht gefunden.")
                    continue
                print(f"Aktuell: {guest.first_name} {guest.last_name}, {guest.email}")
                new_first = input("Neuer Vorname: ")
                new_last = input("Neuer Nachname: ")
                new_email = input("Neue E-Mail: ")
                guest.first_name = new_first
                guest.last_name = new_last
                guest.email = new_email
                guest_dal.update_guest(guest)
                updated = guest_dal.read_guest_by_id(guest_id)
                print(
                    f"Gast aktualisiert: {updated.first_name} {updated.last_name}, {updated.email}"
                )
            except Exception as e:
                print("Fehler:", e)

        elif auswahl == "6":
            try:
                type_id = int(input("Zimmertyp-ID: "))
                room_type = room_type_dal.read_room_type_by_id(type_id)
                if not room_type:
                    print("Zimmertyp nicht gefunden.")
                    continue
                rooms = room_dal.read_room_details(type_id)
                if not rooms:
                    print("Keine Zimmer mit diesem Zimmertyp gefunden.")
                    continue
                print(f"Zimmertyp: {room_type.description} - {len(rooms)} Zimmer")
                for room in rooms:
                    print(
                        f"- Zimmer-ID: {room.room_id}, Nummer {room.room_number}, Preis {room.price_per_night:.2f}"
                    )
                new_price = float(
                    input("Neuer Preis pro Nacht für alle diese Zimmer: ")
                )
                for room in rooms:
                    room.price_per_night = new_price
                    room_dal.update_room(room)
                print(
                    f"Preis aller Zimmer vom Typ '{room_type.description}' auf {new_price:.2f} gesetzt."
                )
            except Exception as e:
                print("Fehler:", e)

        elif auswahl == "0":
            print("Admin-Menü wird beendet.")
            break
        else:
            print("Ungültige Auswahl.")


## User Stories mit DB-Schemaänderung