import model
from model.booking import Booking
from data_access.base_dal import BaseDataAccess


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.db_path = db_path

    def create_new_booking( self, booking: model.Booking) -> model.Booking:
        if booking is None:
            raise ValueError("booking ist erforderlich")
        if booking.guest_id is None:
            raise ValueError("guest_id ist erforderlich")
        if booking.room_id is None:
            raise ValueError("room_id ist erforderlich")
        if booking.check_in_date is None:
            raise ValueError("check_in_date ist erforderlich")
        if booking.check_out_date is None:
            raise ValueError("check_out_date ist erforderlich")
        if booking.is_cancelled is None:
            raise ValueError("is_cancelled ist erforderlich")
        if booking.total_amount is None:
            raise ValueError("total_amount ist erforderlich")

        sql = """
        INSERT INTO Booking (
            guest_id,
            room_id,
            check_in_date,
            check_out_date,
            is_cancelled,
            total_amount
            )
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (
            booking.guest_id,
            booking.room_id,
            booking.check_in_date,
            booking.check_out_date,
            booking.is_cancelled,
            booking.total_amount
        )

        last_row_id, row_count = self.execute(sql, params)

        return model.Booking(
            booking_id=last_row_id,
            guest_id=booking.guest_id,
            room_id=booking.room_id,
            check_in_date=booking.check_in_date,
            check_out_date=booking.check_out_date,
            is_cancelled=booking.is_cancelled,
            total_amount=booking.total_amount
        )

    def read_booking_by_id(self, booking_id: int) -> model.Booking | None:
        if booking_id is None:
            raise ValueError("booking_id ist erforderlich")

        sql = """
        SELECT 
            booking_id,
            guest_id,
            room_id,
            check_in_date,
            check_out_date,
            is_cancelled,
            total_amount
        FROM Booking
        WHERE booking_id = ?
        """
        params = (booking_id,)
        result = self.fetchone(sql, params)
        if result:
            (
                booking_id,
                guest_id,
                room_id,
                check_in_date,
                check_out_date,
                is_cancelled,
                total_amount
            ) = result
            return model.Booking(
                booking_id,
                guest_id,
                room_id,
                check_in_date,
                check_out_date,
                is_cancelled,
                total_amount
            )
        else:
            return None

    def read_booking_by_guest_id(self, guest_id: int) -> list[model.Booking]:
        if guest_id is None:
            raise ValueError("guest_id ist erforderlich")

        sql = """
        SELECT 
            booking_id,
            guest_id,
            room_id,
            check_in_date,
            check_out_date,
            is_cancelled,
            total_amount
        FROM Booking WHERE guest_id = ?
        """
        params = (guest_id,)
        bookings = self.fetchall(sql, params)

        return [
            model.Booking(
                booking_id,
                guest_id,
                room_id,
                check_in_date,
                check_out_date,
                is_cancelled,
                total_amount
            )
            for (
                booking_id,
                guest_id,
                room_id,
                check_in_date,
                check_out_date,
                is_cancelled,
                total_amount
            )
            in bookings
        ]

    def read_booking_by_room_id(self, room_id: int) -> list[model.Booking]:
        if room_id is None:
            raise ValueError("room_id ist erforderlich")

        sql = """
        SELECT 
            booking_id,
            guest_id,
            room_id,
            check_in_date,
            check_out_date,
            is_cancelled,
            total_amount
        FROM Booking WHERE room_id = ?
        """
        params = (room_id,)
        bookings = self.fetchall(sql, params)

        return [
            model.Booking(
                booking_id,
                guest_id,
                room_id,
                check_in_date,
                check_out_date,
                is_cancelled,
                total_amount
            )
            for (
                booking_id,
                guest_id,
                room_id,
                check_in_date,
                check_out_date,
                is_cancelled,
                total_amount
            )
            in bookings
        ]

    def read_all_bookings(self):
        sql = """
            SELECT 
                b.booking_id,
                g.first_name || ' ' || g.last_name AS guest_name,
                h.name AS hotel_name,
                r.room_number,
                b.check_in_date,
                b.check_out_date,
                b.total_amount,
                b.is_cancelled
            FROM Booking b
            JOIN Guest g ON b.guest_id = g.guest_id
            JOIN Room r ON b.room_id = r.room_id
            JOIN Hotel h ON r.hotel_id = h.hotel_id
            ORDER BY b.booking_id
        """
        return self.fetchall(sql)

    def update_booking(self, booking: Booking):
        sql = """
            UPDATE Booking
            SET
                guest_id = ?,
                room_id = ?,
                check_in_date = ?,
                check_out_date = ?,
                is_cancelled = ?,
                total_amount = ?
            WHERE booking_id = ?
        """
        params = (
            booking.guest_id,
            booking.room_id,
            booking.check_in_date,
            booking.check_out_date,
            booking.is_cancelled,
            booking.total_amount,
            booking.booking_id
        )
        self.execute(sql, params)

    def delete_booking(self, booking: Booking):
        sql = "DELETE FROM Booking WHERE booking_id = ?"
        params = (booking.booking_id,)
        self.execute(sql, params)
