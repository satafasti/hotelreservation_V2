from data_access.room_facilities_dal import RoomFacilitiesDataAccess
import model
from typing import List

class RoomFacilitiesManager:
    def __init__(self, db_path: str = None):
        self.__dal = RoomFacilitiesDataAccess(db_path)


#neu erstellte Funktionen 11.06.2025
    def add_facility_to_room(self, room: model.Room, facility: model.Facilities):
        self.__dal.create_facility_to_room(room, facility)

    def remove_facility_from_room(self, room: model.Room, facility: model.Facilities):
        self.__dal.delete_facility_from_room(room, facility)

    def read_facilities_by_room(self, room: model.Room) -> List[model.Facilities]:
        return self.__dal.read_facilities_by_room_id(room)

    def read_rooms_by_facility(self, facility: model.Facilities) -> List[model.Room]:
        return self.__dal.read_rooms_by_facility_id(facility)

    def has_facility(self, room: model.Room, facility: model.Facilities) -> bool:
        return self.__dal.has_facility(room, facility)

    def delete_facilities_from_room(self, room: model.Room):
        self.__dal.delete_room_facilities(room)

    def read_all_facilities(self) -> List[model.Facilities]:
        return self.__dal.read_all_facilities()