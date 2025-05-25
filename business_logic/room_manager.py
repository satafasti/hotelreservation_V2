#import os
import data_access
from model.room import Room
from model.room_type import Room_Type
from model.facilities import Facilities


class RoomManager:
    def __init__(self) -> None:
        self.__room_dal = data_access.RoomDAL()
        self.__description = []
        self.__facilities = []

    def create_room(self, room_id : int, room_number : int, price_per_night : float, description : Room_Type) -> Room:
        room = Room(room_id, room_number, price_per_night, description.type_id)
        self.__room_dal.create_room(room)
        return room

    def add_description(self, room: Room, description: Room_Type):
        if not description:
            raise ValueError("Description cannot be empty")
        if not isinstance(description, Room_Type):
            raise ValueError("Description must be a Room_Type")
        if description not in self.__description:
            self.__description.append(description)
            room.description = description

    def add_facilities(self, room: Room, facility: Facilities):
        if not facility:
            raise ValueError("Facility cannot be empty")
        if not isinstance(facility, Facilities):
            raise ValueError("facility must be a Facilities")
        if not hasattr(room, "facility_name"):
            room.facility_name = []
        if facility not in room.facility_name:
            room.facility_name.append(facility)

    def show_room_facilities(self, rooms : list[Room]):
        print("Zimmerausstattung:")
        for r in rooms:
            facilities = ", ".join(f.name for f in getattr(r, "facility_name", [])) or "Keine"
            print(f" - Zimmer {r.room_number}: {facilities}")

    def is_available(self, hotel, room_id: int) -> bool:
        if not hasattr(hotel, "rooms"):
            raise AttributeError("Das übergebene Hotelobjekt enthält keine Räume.")
        for room in hotel.rooms:
            if room.room_id == room_id and getattr(room, "room_available", False):
                return True
        return False
