import model
from data_access.base_dal import BaseDAL
from model.booking import Booking
from typing import Optional, List


class BookingDAL(BaseDAL):
    def __init__(self, db_path: str):
        super().__init__(db_path)

    def create_booking(self, booking: Booking) -> int:
        self.connect()
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (
            booking.guest_id,
            booking.room_id,
            booking.check_in_date,
            booking.check_out_date,
            int(booking.is_cancelled),
            booking.total_amount
        )
        self.execute_query(sql, params)
        booking_id = self.execute("SELECT last_insert_rowid()")[0][0]
        self.disconnect()
        return booking_id

    def get_booking_by_id(self, booking_id: int) -> Optional[Booking]:
        self.connect()
        sql = "SELECT * FROM Booking WHERE booking_id = ?"
        result = self.fetch_one(sql, (booking_id,))
        self.disconnect()
        if result:
            return Booking(*result)
        return None

    def get_all_bookings(self) -> List[Booking]:
        self.connect()
        sql = "SELECT * FROM Booking"
        results = self.fetch_all(sql)
        self.disconnect()
        return [Booking(*row) for row in results]

    def get_bookings_by_guest(self, guest_id: int) -> List[Booking]:
        self.connect()
        sql = "SELECT * FROM Booking WHERE guest_id = ?"
        results = self.fetch_all(sql, (guest_id,))
        self.disconnect()
        return [Booking(*row) for row in results]

    def update_booking(self, booking: Booking):
        self.connect()
        sql = """
        UPDATE Booking
        SET guest_id = ?, room_id = ?, check_in_date = ?, check_out_date = ?, is_cancelled = ?, total_amount = ?
        WHERE booking_id = ?
        """
        params = (
            booking.guest_id,
            booking.room_id,
            booking.check_in_date,
            booking.check_out_date,
            int(booking.is_cancelled),
            booking.total_amount,
            booking.booking_id
        )
        self.execute_query(sql, params)
        self.disconnect()

    def cancel_booking(self, booking_id: int):
        self.connect()
        sql = "UPDATE Booking SET is_cancelled = 1 WHERE booking_id = ?"
        self.execute_query(sql, (booking_id,))
        self.disconnect()

    def delete_booking(self, booking_id: int):
        self.connect()
        sql = "DELETE FROM Booking WHERE booking_id = ?"
        self.execute_query(sql, (booking_id,))
        self.disconnect()


def show_all_bookings(self):
        sql = "SELECT * FROM Booking"
        results = self.fetch_all(sql)  # commit aus BaseDAL
        bookings = []

        for row in results:
            booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount = row
            bookings.append(model.Booking(booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount))
        return bookings