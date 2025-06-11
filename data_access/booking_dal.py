import model
from model.booking import Booking



from data_access.base_dal import BaseDataAccess


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self._db_path = db_path

    def create_booking(self, booking: model.Booking) -> model.Booking:
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


    def cancel_booking_by_id(self, booking_id: int) -> bool:
        sql = """
        UPDATE Booking 
        SET is_cancelled = 1 
        WHERE booking_id = ?
        """
        params = (booking_id,)
        last_row_id, row_count = self.execute(sql, params)

        return row_count > 0

    #Im Projekt existieren im BookingDataAccess zwar mehrere Funktionen wie update_booking, read_booking_by_room_id, read_booking_by_guest_id und find_available_room, jedoch werden sie von keiner anderen Komponente aufgerufen.
    # In business_logic/booking_manager.py ist dokumentiert, dass viele der definierten Methoden letztlich nicht benötigt wurden.
    # def update_booking(self, booking):
    #     # Platzhalter: Logik zum Aktualisieren einer Buchung implementieren
    #     pass

    # def read_booking_by_room_id(self, room_id: int) -> list[model.Booking]:
    #     self._validate_id(room_id, "room_id")
    #     sql, params = self._get_booking_query("room_id", room_id)
    #     results = self.fetchall(sql, params)
    #     return self._map_to_bookings(results)

    # def read_booking_by_guest_id(self, guest_id: int) -> list[model.Booking]:
    #     self._validate_id(guest_id, "guest_id")
    #     sql, params = self._get_booking_query("guest_id", guest_id)
    #     results = self.fetchall(sql, params)
    #     return self._map_to_bookings(results)

    # def find_available_room(self, room_type_description: str, check_in: date, check_out: date) -> Optional[Room]:
    #     conn = sqlite3.connect(self.db_path)
    #     cursor = conn.cursor()
    #     query = self._get_available_room_query()
    #     params = (room_type_description, check_in, check_out)
    #     cursor.execute(query, params)
    #     row = cursor.fetchone()
    #     conn.close()
    #     return self._map_to_room(row)

    # --- Hilfsmethoden ---

    # def _validate_id(self, value: int, field_name: str) -> None:
    #     if value is None:
    #         raise ValueError(f"{field_name} ist erforderlich")

    # def _get_booking_query(self, filter_field: str, value: int) -> tuple[str, tuple]:
    #     sql = f"""
    #     SELECT
    #         booking_id,
    #         guest_id,
    #         room_id,
    #         check_in_date,
    #         check_out_date,
    #         is_cancelled,
    #         total_amount
    #     FROM Booking WHERE {filter_field} = ?
    #     """
    #     return sql, (value,)

    # def _map_to_bookings(self, rows: list[tuple]) -> list[model.Booking]:
    #     return [
    #         model.Booking(*row)
    #         for row in rows
    #     ]

    # def _get_available_room_query(self) -> str:
    #     return """
    #     SELECT r.room_id, r.type_id, r.hotel_id, rt.description, rt.max_guests
    #     FROM Room r
    #     JOIN Room_Type rt ON r.type_id = rt.type_id
    #     WHERE rt.description = ?
    #     AND r.room_id NOT IN (
    #         SELECT room_id FROM Booking
    #         WHERE NOT (
    #             check_out_date <= ? OR check_in_date >= ?
    #         )
    #     )
    #     LIMIT 1
    #     """

    # def _map_to_room(self, row: Optional[tuple]) -> Optional[Room]:
    #     if row:
    #         return Room(
    #             room_id=row[0],
    #             room_type_id=row[1],
    #             hotel_id=row[2],
    #             room_type_description=row[3],
    #             max_guests=row[4],
    #             price_per_night=0  # Manuell ergänzen bei Bedarf
    #         )
    #     return None
