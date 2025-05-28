import model
from data_access.base_dal import BaseDataAccess


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_booking(
            self,
            booking: model.Booking
    ) -> model.Booking:
        if booking is None:
            raise ValueError("booking is required")
        if booking.guest_id is None:
            raise ValueError("guest_id is required")
        if booking.room_id is None:
            raise ValueError("room_id is required")
        if booking.check_in_date is None:
            raise ValueError("check_in_date is required")
        if booking.check_out_date is None:
            raise ValueError("check_out_date is required")
        if booking.is_cancelled is None:
            raise ValueError("is_cancelled is required")
        if booking.total_amount is None:
            raise ValueError("total_amount is required")

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
            raise ValueError("booking_id is required")

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
            raise ValueError("guest_id is required")

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
            raise ValueError("room_id is required")

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