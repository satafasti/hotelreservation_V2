import model
from data_access.base_dal import BaseDataAccess


class RoomFacilitiesDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_facility_to_room(self, room: model.Room, facilities: model.Facilities):
        sql = """
              INSERT INTO Room_Facilities (room_id, facility_id) VALUES (?, ?)
              """
        params = (room.room_id, facilities.facility_id)
        self.execute(sql, params)


    def read_facilities_by_room_id(self, room: model.Room):
        sql = """
              SELECT f.facility_id, f.facility_name
              FROM Facilities f
                       JOIN Room_Facilities rf ON f.facility_id = rf.facility_id
              WHERE rf.room_id = ? \
              """
        params = (room.room_id,)
        results = self.fetchall(sql, params)

        facilities = []
        if results:
            for row in results:
                facility_id, facility_name = row
                facilities.append(model.Facilities(facility_id, facility_name))

        return facilities


    def read_all_facilities(self) -> list[model.Facilities]:
        sql = "SELECT facility_id, facility_name FROM Facilities ORDER BY facility_name"
        results = self.fetchall(sql)
        return [model.Facilities(facility_id, facility_name) for facility_id, facility_name in results]


# neu aktivierter Code 11.06.2025
def delete_facility_from_room(self, room: model.Room, facilities: model.Facilities):
    sql = """
          DELETE FROM Room_Facilities WHERE room_id = ? AND facility_id = ?
          """
    params = (room.room_id, facilities.facility_id)
    self.execute(sql, params)


def read_rooms_by_facility_id(self, facilities: model.Facilities):
    sql = """
          SELECT r.room_id, r.room_number, r.price_per_night, rt.type_id, rt.description, rt.max_guests, h.hotel_id, h.name, h.address_id, h.stars
          FROM Room r
                   JOIN Room_Facilities rf ON r.room_id = rf.room_id
                   JOIN Room_Type rt ON r.type_id = rt.type_id
                   JOIN Hotel h ON r.hotel_id = h.hotel_id
          WHERE rf.facility_id = ?
          """
    params = (facilities.facility_id,)
    results = self.fetchall(sql, params)

    rooms = []
    if results:
        for row in results:
            room_id, room_number, price_per_night, type_id, description, max_guests, hotel_id, hotel_name, address_id, stars = row
            hotel = model.Hotel(hotel_id, hotel_name, stars, address_id)
            room_type = model.Room_Type(type_id, description, max_guests)
            rooms.append(model.Room(room_id, hotel, room_number, room_type, price_per_night))
    return rooms


def has_facility(self, room: model.Room, facilities: model.Facilities):
    sql = """
          SELECT COUNT(*) FROM Room_Facilities WHERE room_id = ? AND facility_id = ?
          """
    params = (room.room_id, facilities.facility_id)
    result = self.fetchone(sql, params)

    return result[0] > 0 if result else False


def delete_room_facilities(self, room: model.Room):
    sql = """
          DELETE FROM Room_Facilities WHERE room_id = ?
          """
    params = (room.room_id,)
    self.execute(sql, params)