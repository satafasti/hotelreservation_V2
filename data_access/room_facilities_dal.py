import model
from data_access.base_dal import BaseDAL


class RoomFacilitiesDAL(BaseDAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_facility_to_room(self, room: model.Room, facilities: model.Facilities):
        sql = """
              INSERT INTO Room_Facilities (room_id, facility_id) VALUES (?, ?)
              """
        params = (room.room_id, facilities.facility_id)
        self.execute(sql, params)

    def delete_facility_from_room(self, room: model.Room, facilities: model.Facilities):
        sql = """
              DELETE FROM Room_Facilities WHERE room_id = ? AND facility_id = ?
              """
        params = (room.room_id, facilities.facility_id)
        self.execute(sql, params)

    def show_facilities_by_room_id(self, room: model.Room):
        sql = """
              SELECT f.facility_id, f.facility_name
              FROM Facilities f
                       JOIN Room_Facilities rf ON f.facility_id = rf.facility_id
              WHERE rf.room_id = ? \
              """
        params = (room.room_id,)
        results = self.fetch_all(sql, params)

        facilities = []
        if results:
            for row in results:
                facility_id, facility_name = row
                facilities.append(model.Facilities(facility_id, facility_name))

        return facilities

    def show_rooms_by_facility_id(self, facilities: model.facilities):
        sql = """
              SELECT room.room_id, room.room_number, room.price_per_night FROM Room room JOIN Room_Facilities roomfacilities ON room.room_id = roomfacilities.room_id
              WHERE roomfacilities.facility_id = ?
              """
        params = (facilities.facility_id,)
        results = self.fetch_all(sql, params)

        rooms = []
        if results:
            for row in results:
                room_id, room_number, price_per_night, description = row
                rooms.append(model.Room(room_id, room_number, price_per_night, description))

        return rooms

    def has_facility(self, room: model.room, facilities: model.facilities):
        sql = """
              SELECT COUNT(*) FROM Room_Facilities WHERE room_id = ? AND facility_id = ?
              """
        params = (room.room_id, facilities.facility_id)
        result = self.fetch_one(sql, params)

        return result[0] > 0 if result else False

    def delete_room_facilities(self, room: model.room):
        sql = """
              DELETE FROM Room_Facilities WHERE room_id = ?
              """
        params = (room.room_id,)
        self.execute(sql, params)