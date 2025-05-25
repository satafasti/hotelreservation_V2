from __future__ import annotations

import model
from data_access.base_dal import BaseDal
from model import Room_Type


#TODO Code für Projekt ergänzen
### Code gemäss Referenzprojekt
class RoomDAL(BaseDal):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_room(self, hotel_id: int, room_number: int, type_id: Room_Type, price_per_night: float, hotel: model.Hotel = None) -> model.Room: #TODO Verknüpfungen prüfen
        sql = """
        INSERT INTO Room(hotel_id, room_number, type_id, price_per_night) VALUES (?, ?, ?, ?)
        """
        params = (hotel_id, room_number, type_id, price_per_night,
            hotel.hotel_id if hotel else None,
        )

        last_row_id, row_count = self.execute(sql, params)
        return model.Room(last_row_id, hotel_id, room_number, type_id, price_per_night)

    def read_room_by_id(self, room_id: int) -> model.Room | None: #TODO Code prüfen
        sql = """
        SELECT room_id FROM Room WHERE room_id = ?
        """
        params = tuple([room_id])
        result = self.fetchone(sql, params)
        if result:
            room_id = result
            return model.Room(room_id)
        else:
            return None

    def read_rooms_by_hotel(self, hotel: model.Hotel) -> list[model.Room]:
        sql = """
        SELECT room_id FROM Room WHERE hotel_id = ?
        """
        if hotel is None:
            raise ValueError("hotel kann nicht leer sein.")

        params = tuple([hotel.hotel_id])
        rooms = self.fetchall(sql, params)
        return [
            model.Room(room_id, hotel)
            for room_id in rooms
        ]
