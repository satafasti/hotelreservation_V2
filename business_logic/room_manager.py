import data_access
from typing import List
import model


class RoomManager:
    def __init__(self) -> None:
        self.__room_dal = data_access.RoomDataAccess()

    # Aktuell sind diese Methoden nicht im Einsatz, werden aber für potenzielle Systemerweiterungen bereitgehalten.
    # def create_room(self, hotel_id: int, room_number: str, type_id: int, price_per_night: float, hotel: model.Hotel = None) -> model.Room:
    #     return self.__room_dal.create_room(hotel_id, room_number, type_id, price_per_night, hotel)

    # def read_hotels_rooms(self, hotel: model.Hotel) -> None:
    #     return self.__room_dal.read_rooms_by_hotel(hotel)

    # def read_room(self, room_id: int) -> model.Room:
    #     return self.__room_dal.read_room_by_id(room_id)

    def read_room_details(self, type_id: int) -> List[model.Room]:
        return self.__room_dal.read_room_details(type_id)

    def show_room_info(self, room, price_info, check_in=None, check_out=None):
        print(f"  - Zimmer {room.room_number}")
        print(f"    Typ: {room.room_type.description}")
        print(f"    Basispreis: {price_info['base_price']:.2f} CHF/Nacht")
        print(f"    Aktueller Preis: {price_info['dynamic_price']:.2f} CHF/Nacht")

        if price_info['has_seasonal_adjustment']:
            price_diff = price_info['price_difference']
            if price_diff > 0:
                print(f"    Saison-Aufschlag: +{price_diff:.2f} CHF")
            else:
                print(f"    Saison-Rabatt: {price_diff:.2f} CHF")
        else:
            print(f"    Keine Saison-Anpassung")

        if check_in:
            print(f"    Check-in Datum: {check_in}")
            if check_out:
                print(f"    Check-out Datum: {check_out}")
        else:
            print(f"    Kein Check-in Datum verfügbar")

        features = ', '.join(room.features) if hasattr(room, "features") and room.features else "Keine Angaben"
        print(f"    Ausstattung: {features}")
        print()

    def get_room_input(self):
        room_number = input("Gib eine Zimmernummer ein: ")
        description = input(
            "Gib den Zimmertyp an (Single, Double, Suite, Family Room, Penthouse): ")
        max_guests = int(input("Maximale Anzahl Gäste für das Zimmer (Single (max.1), Double (max.2), Suite (max.4), Family Room (max.5), Penthouse (max.6): "))
        price_per_night = float(input("Gib den Preis pro Nacht für das Zimmer an: "))
        return room_number, description, max_guests, price_per_night