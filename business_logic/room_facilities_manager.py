from data_access.room_facilities_dal import RoomFacilitiesDataAccess
from model.room import Room
from model.facilities import Facilities
from typing import List

class RoomFacilitiesManager:
    def __init__(self, db_path: str = None):
        self.__dal = RoomFacilitiesDataAccess(db_path)

#Es wird zwar eine Klasse RoomFacilitiesManager  definiert, ihre Methoden werden jedoch nirgends aufgerufen. Stattdessen greift die UI direkt auf den Data-Access-Layer zu.
#In ui_folder/admin_ui.py wird beispielsweise ein RoomFacilitiesDataAccess‐Objekt erstellt und dessen Methoden verwendet.
    # def add_facility_to_room(self, room: Room, facility: Facilities):
    #     self.__dal.create_facility_to_room(room, facility)

    # def remove_facility_from_room(self, room: Room, facility: Facilities):
    #     self.__dal.delete_facility_from_room(room, facility)

    # def read_facilities_by_room(self, room: Room) -> List[Facilities]:
    #     return self.__dal.read_facilities_by_room_id(room)

    # def read_rooms_by_facility(self, facility: Facilities) -> List[Room]:
    #     return self.__dal.read_rooms_by_facility_id(facility)

    # def has_facility(self, room: Room, facility: Facilities) -> bool:
    #     return self.__dal.has_facility(room, facility)

    # def delete_facilities_from_room(self, room: Room):
    #     self.__dal.delete_room_facilities(room)

