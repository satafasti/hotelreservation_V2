import os
import model
from data_access.room_dal import RoomDataAccess

#TODO Code für Projekt ergänzen
### Code gemäss Referenzprojekt
class RoomManager:
    def __init__(self, db_path: str = None) :
        self.__room_dal = RoomDataAccess(db_path)

#    def create_room(self, hotel_id: int, room_number: str, type_id: int, price_per_night: float, hotel: model.Hotel = None) -> model.Room:
#        return self.__room_dal.create_room(hotel_id, room_number, type_id, price_per_night, hotel)

    def read_hotels_rooms(self, hotel_id: int) -> list[model.Room]:
        return self.__room_dal.read_hotel_rooms_extended_info(hotel_id)

 #   def read_room(self, room_id: int) -> model.Room:
 #       return self.__room_dal.read_room_by_id(room_id)

    def read_hotel_rooms_extended_info(self):
        return self.__hotel_dal.read_hotel_rooms_extended_info()
