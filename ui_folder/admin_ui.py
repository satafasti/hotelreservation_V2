
from business_logic.booking_manager import BookingManager
from business_logic.facilities_manager import FacilitiesManager
from data_access.room_dal import RoomDAL
from data_access.room_facilities_dal import RoomFacilitiesDAL
from data_access.hotel_dal import HotelDAL
from business_logic.room_manager import RoomManager
from business_logic.room_type_manager import RoomTypeManager

##8.Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.
def read_all_bookings_ui():
    manager = BookingManager()
    results = manager.read_all_bookings()

    print("Übersicht aller Buchungen:\n")
    for b in results:
        booking_id, guest_name, hotel_name, room_number, check_in, check_out, amount, cancelled = b
        status = "Storniert" if cancelled else "Aktiv"
        print(f"Buchungs-ID: {booking_id} | Gast: {guest_name} | Hotel: {hotel_name} | Zimmer: {room_number}")
        print(f"Zeitraum: {check_in} bis {check_out} | Betrag: {amount:.2f} CHF | Status: {status}")
        print("-" * 80)

#9. Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.
def show_rooms_with_facilities_ui():
    print(" Zimmer mit Ausstattung\n")

    room_dal = RoomDAL()
    facilities_dal = RoomFacilitiesDAL()
    hotel_dal = HotelDAL()

    rooms = room_dal.read_all_rooms()

    if not rooms:
        print("Keine Zimmer gefunden.")
        return

    for room in rooms:
        facilities = facilities_dal.read_facilities_by_room_id(room)
        hotel = hotel_dal.read_hotel_by_id(room.hotel_id)

        print(f"Zimmer-ID: {room.room_id} | Zimmernummer: {room.room_number} | Hotel: {hotel.name}")
        print(f"Preis pro Nacht: {room.price_per_night:.2f} CHF")
        print("Ausstattung:", ", ".join([f.facility_name for f in facilities]) or "Keine")
        print("-" * 60)

#10. Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat. 3 Hint: Stammdaten sind alle Daten, die nicht von anderen Daten abhängen.
def manage_facilities_ui():
    manager = FacilitiesManager()

    while True:
        print("\n--- Einrichtungen verwalten ---")
        print("1) Alle Einrichtungen anzeigen")
        print("2) Neue Einrichtung erstellen")
        print("3) Einrichtung umbenennen")
        print("4) Einrichtung löschen")
        print("0) Zurück")

        choice = input("Auswahl: ").strip()

        if choice == "1":
            facilities = manager.read_all_facilities()
            for f in facilities:
                print(f"{f.facility_id}: {f.facility_name}")

        elif choice == "2":
            name = input("Name der neuen Einrichtung: ").strip()
            manager.create_facility(name)

        elif choice == "3":
            id_ = int(input("Facility-ID: "))
            name = input("Neuer Name: ")
            facility = manager.read_facility_by_id(id_)
            facility.facility_name = name
            manager.update_facility(facility)

        elif choice == "4":
            id_ = int(input("Facility-ID: "))
            facility = manager.read_facility_by_id(id_)
            manager.delete_facility(facility)

        elif choice == "0":
            break
        else:
            print("Ungültige Eingabe.")

from business_logic.room_type_manager import RoomTypeManager

def manage_room_types_ui():
    manager = RoomTypeManager()

    while True:
        print("\n--- Zimmertypen verwalten ---")
        print("1) Alle anzeigen")
        print("2) Neuen erstellen")
        print("3) Beschreibung bearbeiten")
        print("4) Löschen")
        print("0) Zurück")

        choice = input("Auswahl: ").strip()

        if choice == "1":
            for rt in manager.read_all_room_types():
                print(f"{rt.type_id}: {rt.description}")

        elif choice == "2":
            description = input("Beschreibung: ")
            manager.create_room_type(description)

        elif choice == "3":
            id_ = int(input("Type-ID: "))
            new_desc = input("Neue Beschreibung: ")
            room_type = manager.read_room_type_by_id(id_)
            room_type.description = new_desc
            manager.update_room_type(room_type)

        elif choice == "4":
            id_ = int(input("Type-ID: "))
            room_type = manager.read_room_type_by_id(id_)
            manager.delete_room_type(room_type)

        elif choice == "0":
            break

def manage_room_prices_ui():
    manager = RoomManager()

    while True:
        print("\n--- Zimmerpreise verwalten ---")
        print("1) Alle Zimmer anzeigen")
        print("2) Preis bearbeiten")
        print("0) Zurück")

        choice = input("Auswahl: ").strip()

        if choice == "1":
            for r in manager.read_all_rooms():
                print(f"{r.room_id}: Zimmer {r.room_number} | Preis: {r.price_per_night:.2f} CHF")

        elif choice == "2":
            id_ = int(input("Zimmer-ID: "))
            new_price = float(input("Neuer Preis pro Nacht: "))
            room = manager.read_room_by_id(id_)
            room.price_per_night = new_price
            manager.update_room(room)

        elif choice == "0":
            break
