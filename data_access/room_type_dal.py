import model

from data_access.base_dal import BaseDataAccess
from typing import Optional

class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_room_type(self, type_id: int, description: str, max_guests: int) -> model.Room_Type:
        #if type_id is None:
           # raise ValueError("Room type ID wird benötigt") -> sollte nicht passieren da autoincrement
        if not description:
            raise ValueError("Room type description wird benötigt")
        if max_guests is None:
            raise ValueError("Max guests wird benötigt")

        sql = """
        INSERT INTO Room_Type (type_id, description, max_guests)
        VALUES (?, ?, ?)
        """
        params = (type_id, description, max_guests)
        self.execute(sql, params)

        return model.Room_Type(type_id=type_id, description=description, max_guests=max_guests)

    def read_room_type_by_id(self, type_id: int) -> Optional[model.Room_Type]:
        if type_id is None:
            raise ValueError("Room type ID wird benötigt")

        sql = """
        SELECT type_id, description, max_guests
        FROM Room_Type
        WHERE type_id = ?
        """
        result = self.fetchone(sql, (type_id,))
        if result:
            type_id, description, max_guests = result
            return model.Room_Type(type_id=type_id, description=description, max_guests=max_guests)
        else:
            return None

    def read_all_room_types(self) -> list[model.Room_Type]:
        sql = """
        SELECT type_id, description, max_guests
        FROM Room_Type
        """
        results = self.fetchall(sql)

        return [
            model.Room_Type(type_id=type_id, description=description, max_guests=max_guests)
            for type_id, description, max_guests in results
        ]

    def update_room_type(self, type_id: int, description: str, max_guests: int):
        if type_id is None:
           raise ValueError("Room type ID wird benötigt")
        sql = """
        UPDATE Room_Type
        SET description = ?, max_guests = ?
        WHERE type_id = ?
        """
        params = (description, max_guests, type_id)
        self.execute(sql, params)

    def delete_room_type(self, type_id: int):
        if type_id is None:
            raise ValueError("Room type ID wird benötigt")

        sql = """
        DELETE FROM Room_Type
        WHERE type_id = ?
        """
        self.execute(sql, (type_id,))