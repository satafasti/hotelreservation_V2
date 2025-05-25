import model
from data_access.base_dal import BaseDAL


class RoomDAL(BaseDAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_room(self, room: model.Room):
        sql = """
        INSERT INTO Room (room_id, room_number, price_per_night) VALUES ( ?, ?, ?)
        """
        params = (room.room_id if room else None, room.room_number, room.price_per_night, room.hotel_id, room.type_id
                  )
        self.execute(sql, params)

    def show_room_by_id(self, room_id : int):
        sql = """
        SELECT * FROM Room WHERE room_id = ?
        """
        params = (room_id,)
        result = self.fetch_one(sql, params)
        if result:
            room_id, room_number, price_per_night = result
            return model.Room(room_id, room_number, price_per_night)
        else:
            return None

    def update_room(self, room: model.Room):
        sql = """
        UPDATE Room SET room_number = ?, price_per_night = ? WHERE room_id = ?
        """
        params = (room.room_number, room.price_per_night, room.room_id)
        self.execute(sql, params)

    def delete_room(self, room: model.Room):
        sql = """
        DELETE FROM Room WHERE room_id = ?
        """
        params = (room.room_id,)
        self.execute(sql, params)

    def show_all_rooms(self):
        sql = "SELECT * FROM Room"
        results = self.fetch_all(sql)  # kommt aus BaseDAL
        rooms = []

        for row in results:
            room_id, hotel_id, room_number, type_id, price_per_night = row
            rooms.append(model.Room(room_id, hotel_id, room_number, type_id, price_per_night))
        return rooms


