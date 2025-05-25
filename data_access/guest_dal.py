from __future__ import annotations

import model
from data_access.base_dal import BaseDAL


class GuestDAL(BaseDAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_guest(self, guest: model.Guest):
        sql = """
        INSERT INTO Guest(guest_id, first_name, last_name, email, address_id) VALUES (?, ?, ?, ?, ?) 
        """
        params = (guest.guest_id if guest else None, guest.first_name, guest.last_name, guest.email, guest.address_id)
        self.execute(sql, params)

    def show_guest_by_id(self, guest: model.Guest):
        sql = """
        SELECT * FROM Guest WHERE guest_id = ?
        """
        params = (guest.guest_id,)
        result = self.fetch_one(sql, params)
        if result:
            guest_id, first_name, last_name, email, address_id = result
            return model.Guest(guest_id, first_name, last_name, email, address_id)
        else:
            return None

    def update_guest(self, guest: model.Guest):
        sql = """
        UPDATE Guest SET first_name = ? AND last_name = ? WHERE guest_id = ?
        """
        params = (guest.first_name, guest.last_name, guest.guest_id)
        self.execute(sql, params)

    def delete_guest(self, guest: model.Guest):
        sql = """
        DELETE FROM Guest WHERE guest_id = ?
        """
        params = (guest.guest_id,)
        self.execute(sql, params)

    def show_all_guests(self):
        sql = "SELECT * FROM Guest"
        results = self.fetch_all(sql)  # kommt aus BaseDAL
        guests = []

        for row in results:
            guest_id, first_name, last_name, email, address_id = row
            guests.append(model.Guest(guest_id, first_name, last_name, email, address_id))

        return guests

