from __future__ import annotations
import model
from data_access.base_dal import BaseDataAccess
from typing import List



class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None): super().__init__(db_path)

    def read_room_by_id(self, room_id: int) -> model.Room | None:
        sql = """
            SELECT r.room_id, r.room_number, r.price_per_night,
                   rt.type_id, rt.description, rt.max_guests,
                   h.hotel_id, h.name, h.address_id, h.stars
            FROM Room r
            JOIN Room_Type rt ON r.type_id = rt.type_id
            JOIN Hotel h ON r.hotel_id = h.hotel_id
            WHERE r.room_id = ?
        """
        result = self.fetchone(sql, (room_id,))
        return model.Room(result[0], model.Hotel(result[6], result[7], result[8], result[9]), result[1],
                          model.Room_Type(result[3], result[4], result[5]), result[2]) if result else None

    def read_room_details(self, type_id: int) -> List[model.Room]:
        sql = """
              SELECT r.room_id, \
                     r.room_number, \
                     r.price_per_night,
                     rt.type_id, \
                     rt.description, \
                     rt.max_guests,
                     h.hotel_id, \
                     h.name, \
                     h.address_id, \
                     h.stars
              FROM Room r
                       JOIN Room_Type rt ON r.type_id = rt.type_id
                       JOIN Hotel h ON r.hotel_id = h.hotel_id
              WHERE r.type_id = ? \
              """
        return [model.Room(row[0], model.Hotel(row[6], row[7], row[8], row[9]), row[1],
                           model.Room_Type(row[3], row[4], row[5]), row[2]) for row in self.fetchall(sql, (type_id,))]

# Aktuell sind diese Methoden nicht im Einsatz, werden aber für potenzielle Systemerweiterungen bereitgehalten.

# def create_new_room(self, hotel_id: int, room_number: int, type_id: int, price_per_night: float) -> model.Room:
#     sql = "INSERT INTO Room(hotel_id, room_number, type_id, price_per_night) VALUES (?, ?, ?, ?)"
#     last_row_id, _ = self.execute(sql, (hotel_id, room_number, type_id, price_per_night))
#     return model.Room(last_row_id, model.Hotel(hotel_id, "", 0, 0), room_number, model.Room_Type(type_id, "", 0), price_per_night)

# def read_rooms_by_hotel(self, hotel: model.Hotel) -> list[model.Room]:
#     if hotel is None: raise ValueError("hotel kann nicht leer sein.")
#     sql = """
#         SELECT r.room_id, r.room_number, r.price_per_night,
#                rt.type_id, rt.description, rt.max_guests,
#                h.hotel_id, h.name, h.address_id, h.stars
#         FROM Room r
#         JOIN Room_Type rt ON r.type_id = rt.type_id
#         JOIN Hotel h ON r.hotel_id = h.hotel_id
#         WHERE r.hotel_id = ?
#     """
#     return [model.Room(row[0], model.Hotel(row[6], row[7], row[8], row[9]), row[1], model.Room_Type(row[3], row[4], row[5]), row[2]) for row in self.fetchall(sql, (hotel.hotel_id,))]

# def read_all_rooms(self) -> list[Room]:
#     sql = "SELECT room_id FROM Room"
#     rows = self.fetchall(sql)
#     return [self.read_room_by_id(row[0]) for row in rows]

# def update_room(self, room: Room) -> None:
#     sql = """
#         UPDATE Room
#         SET room_number = ?, price_per_night = ?
#         WHERE room_id = ?
#     """
#     params = (room.room_number, room.price_per_night, room.room_id)
#     self.execute(sql, params)
