import model

from data_access.room_type_dal import RoomTypeDataAccess
from typing import Optional


class RoomTypeManager:
    def __init__(self, room_type_dal: RoomTypeDataAccess):
        self._dal = room_type_dal

    def create_room_type(self, type_id: int, description: str, max_guests: int) -> model.Room_Type:
        if max_guests <= 0:
            raise ValueError("Die Anzahl maximaler Gäste muss grösser als 0 sein")
        return self._dal.create_new_room_type(type_id, description, max_guests)

    def get_room_type_by_id(self, type_id: int) -> Optional[model.Room_Type]:
        return self._dal.read_room_type_by_id(type_id)

    def get_all_room_types(self) -> list[model.Room_Type]:
        return self._dal.read_all_room_types()

    def update_room_type(self, type_id: int, description: str, max_guests: int):
        if max_guests <= 0:
            raise ValueError("Max guests must be greater than zero")
        self._dal.update_room_type(type_id, description, max_guests)

    def delete_room_type(self, type_id: int):
        self._dal.delete_room_type(type_id)

    def is_suitable_for_guests(self, type_id: int, guest_count: int) -> bool:
        room_type = self._dal.read_room_type_by_id(type_id)
        if room_type is None:
            return False
        return guest_count <= room_type.max_guests