import model
from data_access.base_dal import BaseDataAccess
from typing import Optional


class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_guest(self, guest: model.Guest) -> model.Guest:
        sql = """
        INSERT INTO Guest(first_name, last_name, email, address_id)
        VALUES (?, ?, ?, ?)
        """
        params = (guest.first_name, guest.last_name, guest.email, guest.address_id)
        guest_id, _ = self.execute(sql, params)
        guest._Guest__guest_id = guest_id
        return guest

    def read_guest_by_id(self, guest_id: int) -> Optional[model.Guest]:
        sql = "SELECT guest_id, first_name, last_name, email, address_id FROM Guest WHERE guest_id = ?"
        result = self.fetchone(sql, (guest_id,))
        if result:
            return model.Guest(*result)
        else:
            return None

    def read_guest_by_email(self, email: str) -> Optional[model.Guest]:
        sql = (
            "SELECT guest_id, first_name, last_name, email, address_id "
            "FROM Guest WHERE email = ?"
        )
        result = self.fetchone(sql, (email,))
        if result:
            return model.Guest(*result)
        return None

    def update_guest(self, guest: model.Guest):
        sql = """
        UPDATE Guest SET first_name = ?, last_name = ?, email = ?, address_id = ? WHERE guest_id = ?
        """
        params = ( guest.first_name, guest.last_name, guest.email, guest.address_id, guest.guest_id)
        self.execute(sql, params)

    def delete_guest(self, guest: model.Guest):
        sql = """
        DELETE FROM Guest WHERE guest_id = ?
        """
        params = (guest.guest_id,)
        self.execute(sql, params)
        _, rowcount = self.execute(sql, params)
        if rowcount == 0:
            raise LookupError(f"No guest found with id {guest.guest_id}")

    def read_all_guests(self) -> list[model.Guest]:
        sql = """SELECT guest_id, first_name, last_name, email, address_id FROM Guest"""
        results = self.fetchall(sql)
        return [model.Guest(*row) for row in results]

    def get_all_guest_details_by_hotel(self, hotel_id: int) -> list[dict]:
        if hotel_id is None:
            raise ValueError("hotel_id ist erforderlich")
        if not isinstance(hotel_id, int):
            raise TypeError("hotel_id muss ein integer sein")

        sql = """
        SELECT DISTINCT
            g.guest_id,
            a.city,
            gd.nationality,
            gd.birthdate,
            gd.gender,
            gd.marital_status
        FROM Guest g
        JOIN Address a ON g.address_id = a.address_id
        JOIN Guest_Details gd ON g.guest_id = gd.guest_id
        JOIN Booking b ON g.guest_id = b.guest_id
        JOIN Room r ON b.room_id = r.room_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        WHERE h.hotel_id = ?
        ORDER BY g.guest_id
        """
        results = self.fetchall(sql, (hotel_id,))
        guest_details = []
        for row in results:
            guest_id, city, nationality, birthdate, gender, marital_status = row
            guest_details.append({
                'guest_id': guest_id,
                'city': city,
                'nationality': nationality,
                'birthdate': birthdate,
                'gender': gender,
                'marital_status': marital_status
            })
        return guest_details