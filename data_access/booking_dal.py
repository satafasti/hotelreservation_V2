import model
import sqlite3
from model.booking import Booking
from typing import Optional, List
from model.room import Room
from model.booking import Booking


from data_access.base_dal import BaseDataAccess


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

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
                booking_id=booking_id,
                guest_id=guest_id,
                room_id=room_id,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                is_cancelled=bool(is_cancelled),  # Konvertierung zu boolean
                total_amount=total_amount
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

    def read_all_bookings(self) -> list[Booking]:
        sql = """
            SELECT booking_id, check_in_date, check_out_date, is_cancelled, total_amount, guest_id, room_id
            FROM Booking
        """
        rows = self.fetchall(sql)

        return [
            Booking(
                booking_id=row[0],
                check_in_date=row[1],
                check_out_date=row[2],
                is_cancelled=bool(row[3]),
                total_amount=row[4],
                guest_id=row[5],
                room_id=row[6]
            )
            for row in rows
        ]

    def find_available_room(self, room_type_description: str, check_in: str, check_out: str) -> Optional[Room]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        query = """
        SELECT r.room_id, r.type_id, r.hotel_id, rt.description, rt.max_guests
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE rt.description = ?
        AND r.room_id NOT IN (
            SELECT room_id FROM Booking
            WHERE NOT (
                check_out_date <= ? OR check_in_date >= ?
            )
        )
        LIMIT 1
        """

        params = (room_type_description, check_in, check_out)
        cursor.execute(query, params)
        row = cursor.fetchone()

        conn.close()

        if row:
            return Room(
                room_id=row[0],
                room_type_id=row[1],
                hotel_id=row[2],
                room_type_description=row[3],
                max_guests=row[4],
                price_per_night=0  # Fill as needed
            )
        return None

    def cancel_booking_by_id(self, booking_id: int) -> bool:


        sql = """
        UPDATE Booking 
        SET is_cancelled = 1 
        WHERE booking_id = ?
        """
        params = (booking_id,)
        last_row_id, row_count = self.execute(sql, params)

        return row_count > 0