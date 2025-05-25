import model
from data_access.base_dal import BaseDAL

class RoomTypeDAL(BaseDAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_room_facilities(self, room_type: model.Room_Type):
        sql = """
        INSERT INTO Room_Type (type_id, description, max_guests) VALUES (?, ?, ?)
        """
        params = (room_type.type_id if room_type else None, room_type.description, room_type.max_guests)
        self.execute(sql, params)

    def show_room_type_by_id(self, room_type: model.Room_Type):
        sql = """
        SELECT * FROM Room_Type WHERE type_id = ?
        """
        params = (room_type.type_id,)
        result = self.fetch_one(sql, params)
        if result:
            type_id, description, max_guests = result
            return model.Room_Type(type_id, description, max_guests)
        else:
            return None

    def update_room_type(self, room_type: model.Room_Type):
        sql = """
        UPDATE Room_Type SET description = ?, max_guests = ? WHERE type_id = ?
        """
        params = (room_type.description, room_type.max_guests)
        self.execute(sql, params)

    def delete_room_type(self, room_type: model.Room_Type):
        sql = """
        DELETE FROM Room_Type WHERE type_id = ?
        """
        params = (room_type.type_id,)
        self.execute(sql, params)