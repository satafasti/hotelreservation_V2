import os
import model
import data_access

#TODO Code für Projekt ergänzen
### Code gemäss Referenzprojekt
class RoomManager():
    def __init__(self) -> None:
        self.__room_dal = data_access.RoomDataccess()

    def create_room(self, hotel_id: int, room_number: str, type_id: int, price_per_night: float, hotel: model.Hotel = None) -> model.Room:
        return self.__room_dal.create_room(hotel_id, room_number, type_id, price_per_night, hotel)

    def read_hotels_rooms(self, hotel: model.Hotel) -> None:
        self.__room_dal.read_rooms_by_hotel(hotel)

    def read_room(self, room_id: int) -> model.Room:
        return self.__room_dal.read_room_by_id(room_id)
