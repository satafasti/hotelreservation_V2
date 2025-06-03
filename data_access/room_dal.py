from __future__ import annotations

import model
from data_access.base_dal import BaseDataAccess
from model import Hotel
from model import Room_Type


#TODO Code für Projekt ergänzen
### Code gemäss Referenzprojekt
class RoomDataAccess(BaseDataAccess):
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

    def read_rooms_by_hotel_id(self, hotel: Hotel) -> list[model.Room]:
        """Read all rooms for a specific hotel by hotel ID"""
        if hotel is None:
            raise ValueError("hotel_id cannot be None")

        sql = """
        SELECT room_id, hotel_id, room_number, type_id, price_per_night 
        FROM Room 
        WHERE hotel_id = ?
        """
        params = tuple(hotel.hotel_id,)
        results = self.fetchall(sql, params)

        return [
            model.Room(room_id, hotel.hotel_id, room_number, type_id, price_per_night)
            for room_id, hotel_id, room_number, type_id, price_per_night in results
        ]

    def read_rooms_by_hotel(self, hotel: model.Hotel) -> list[model.Room]:
        sql = """
        SELECT room_id FROM Room WHERE hotel_id = ?
        """
        if hotel is None:
            raise ValueError("hotel kann nicht leer sein.")

        params = tuple([hotel.hotel_id])
        rooms = self.fetchall(sql, params)
        return [
            model.Room(row[0], hotel)
            for row in rooms
        ]

def read_hotel_rooms_extended_info(self, hotel_id: int) -> list[model.Room]:
    sql = """
          SELECT h.hotel_id,
                 h.name,
                 h.stars,
                 h.address_id,
                 r.room_id,
                 r.room_number,
                 r.price_per_night,
                 rt.type_id,
                 rt.description,
                 rt.max_guests,
                 b.booking_id,
                 b.guest_id,
                 b.check_in_date,
                 b.check_out_date,
                 b.is_cancelled,
                 b.total_amount
          FROM Room r
                   JOIN Hotel h ON r.hotel_id = h.hotel_id
                   JOIN Room_Type rt ON r.type_id = rt.type_id
                   LEFT JOIN Booking b ON r.room_id = b.room_id
          WHERE r.hotel_id = ?
          ORDER BY r.room_id, b.booking_id
          """

    results = self.fetchall(sql, (hotel_id,))

    if not results:
        return []

    # Get hotel info from first row
    first_row = results[0]
    hotel = model.Hotel(
        hotel_id=first_row[0],
        name=first_row[1],
        stars=first_row[2],
        address_id=first_row[3]
    )

    rooms = {}
    for row in results:
        (
            hotel_id, name, stars, address_id,
            room_id, room_number, price_per_night,
            type_id, description, max_guests,
            booking_id, guest_id, check_in_date, check_out_date,
            is_cancelled, total_amount
        ) = row

        # Room nur einmal anlegen
        if room_id not in rooms:
            room_type = model.Room_Type(type_id=type_id, description=description, max_guests=max_guests)
            rooms[room_id] = model.Room(
                room_id=room_id,
                hotel=hotel,
                room_number=room_number,
                room_type=room_type,
                price_per_night=price_per_night
            )
            rooms[room_id].bookings = []

        room = rooms[room_id]

        # Booking anlegen (nur wenn nicht None)
        if booking_id is not None:
            is_cancelled = bool(is_cancelled) if is_cancelled is not None else False
            booking = model.Booking(
                booking_id=booking_id,
                room_id=room_id,
                guest_id=guest_id,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                is_cancelled=is_cancelled,
                total_amount=total_amount
            )
            room.bookings.append(booking)

    return list(rooms.values())