import model
from model.booking import Booking
from data_access.base_dal import BaseDataAccess
from typing import Optional


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None): super().__init__(db_path); self.db_path = db_path

    def create_new_booking(self, booking: model.Booking) -> model.Booking:
        if not booking or not all([booking.guest_id, booking.room_id, booking.check_in_date, booking.check_out_date, booking.total_amount]) or booking.is_cancelled is None:
            raise ValueError("Unvollständige Buchungsdaten.")
        sql = "INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount) VALUES (?, ?, ?, ?, ?, ?)"
        last_row_id, _ = self.execute(sql, (booking.guest_id, booking.room_id, booking.check_in_date, booking.check_out_date, booking.is_cancelled, booking.total_amount))
        return model.Booking(last_row_id, booking.guest_id, booking.room_id, booking.check_in_date, booking.check_out_date, booking.is_cancelled, booking.total_amount)

    def read_booking_by_id(self, booking_id: int) -> model.Booking | None:
        if booking_id is None: raise ValueError("booking_id ist erforderlich")
        result = self.fetchone("SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking WHERE booking_id = ?", (booking_id,))
        return model.Booking(*result) if result else None

    def read_booking_by_guest_id(self, guest_id: int) -> list[model.Booking]:
        if guest_id is None: raise ValueError("guest_id ist erforderlich")
        return [model.Booking(*row) for row in self.fetchall("SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking WHERE guest_id = ?", (guest_id,))]

    def read_booking_by_room_id(self, room_id: int) -> list[model.Booking]:
        if room_id is None: raise ValueError("room_id ist erforderlich")
        return [model.Booking(*row) for row in self.fetchall("SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking WHERE room_id = ?", (room_id,))]

    def read_all_bookings(self): return self.fetchall("""
        SELECT b.booking_id, g.first_name || ' ' || g.last_name AS guest_name, h.name AS hotel_name,
               r.room_number, b.check_in_date, b.check_out_date, b.total_amount, b.is_cancelled
        FROM Booking b
        JOIN Guest g ON b.guest_id = g.guest_id
        JOIN Room r ON b.room_id = r.room_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        ORDER BY b.booking_id
    """)

    def update_booking(self, booking: Booking):
        self.execute("UPDATE Booking SET guest_id = ?, room_id = ?, check_in_date = ?, check_out_date = ?, is_cancelled = ?, total_amount = ? WHERE booking_id = ?",
                     (booking.guest_id, booking.room_id, booking.check_in_date, booking.check_out_date, booking.is_cancelled, booking.total_amount, booking.booking_id))

    def delete_booking(self, booking: Booking): self.execute("DELETE FROM Booking WHERE booking_id = ?", (booking.booking_id,))

    def find_available_room(self, room_type_description: str, check_in: str, check_out: str) -> Optional[model.Room]:
        sql = """
            SELECT r.room_id, r.room_number, r.price_per_night,
                   rt.type_id, rt.description, rt.max_guests,
                   h.hotel_id, h.name, h.address_id, h.stars
            FROM Room r
            JOIN Room_Type rt ON r.type_id = rt.type_id
            JOIN Hotel h ON r.hotel_id = h.hotel_id
            WHERE rt.description = ?
              AND r.room_id NOT IN (
                  SELECT b.room_id FROM Booking b
                  WHERE b.is_cancelled = 0
                    AND NOT (b.check_out_date <= ? OR b.check_in_date >= ?)
              )
            LIMIT 1
        """
        result = self.fetchone(sql, (room_type_description, check_in, check_out))
        return model.Room(result[0], model.Hotel(result[6], result[7], result[8], result[9]), result[1], model.Room_Type(result[3], result[4], result[5]), result[2]) if result else None
