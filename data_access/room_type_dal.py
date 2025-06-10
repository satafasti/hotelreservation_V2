import model

from data_access.base_dal import BaseDataAccess
from typing import Optional

class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)


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

# Die beiden Funktionen create_new_room_type und delete_room_type sind zwar im Data‑Access-Layer
# definiert, werden jedoch im restlichen# Projekt nirgends aufgerufen. Auch im User‑Interface (ui_folder) und in der Business-Logic gibt es
# keine Verweise darauf (Suche nach den Funktionsnamen liefert keine weiteren Treffer).
#
# Im README wird beschrieben, dass bei der erneuten Repository-Erstellung einige Methoden zwar
# implementiert, später aber nicht mehr genutzt wurden. Aus Zeitgründen hat man diese Methoden
# im Code belassen, um mögliche versehentliche Löschungen zu vermeiden.


# def delete_room_type(self, type_id: int):
#     if type_id is None:
#         raise ValueError("Room type ID wird benötigt")
#
#     sql = """
#     DELETE FROM Room_Type
#     WHERE type_id = ?
#     """

# def create_new_room_type(self, type_id: int, description: str, max_guests: int) -> model.Room_Type:
#     # if type_id is None:
#     #     raise ValueError("Room type ID wird benötigt") -> sollte nicht passieren da autoincrement
#     if not description:
#         raise ValueError("Room type description wird benötigt")
#     if max_guests is None:
#         raise ValueError("Max guests wird benötigt")
#
#     sql = """
#     INSERT INTO Room_Type (type_id, description, max_guests)
#     VALUES (?, ?, ?)
#     """
#     params = (type_id, description, max_guests)
#     self.execute(sql, params)
#
#     return model.Room_Type(type_id=type_id, description=description, max_guests=max_guests)
