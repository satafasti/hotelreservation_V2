from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.hotel import Hotel
    from model.room_type import Room_Type
    from model.facilities import Facilities

class Room:
    def __init__(self, room_id: int, hotel: Hotel, room_number: str, room_type: Room_Type, price_per_night: float):
        if room_id is not None and not isinstance(room_id, int):
            raise ValueError("room_id muss integer sein.")
        if not room_number:
            raise ValueError("room_number wird benötigt.")
        if not isinstance(room_number, str):
            raise ValueError("room_number muss string sein.")
        if not price_per_night:
            raise ValueError("price_per_night wird benötigt.")
        if not isinstance(price_per_night, float):
            raise ValueError("price_per_night muss float sein.")
        if not room_type:
            raise ValueError("room_type wird benötigt.")
        if not self._is_room_type(room_type):
            raise ValueError("room_type muss Room_Type Instanz sein.")

        self.__room_id: int = room_id
        self.__room_number: str = room_number
        self.__hotel: Hotel = hotel
        self.__price_per_night: float = price_per_night
        self.__room_type: Room_Type = room_type
        self.__facilities: list[Facilities] = []

        if hotel is not None:
            hotel.add_room(self)

    def _is_room_type(self, obj) -> bool:
        try:
            from model.room_type import Room_Type
            return isinstance(obj, Room_Type)
        except ImportError:
            return obj.__class__.__name__ == 'Room_Type'

    def _is_facilities(self, obj) -> bool:
        try:
            from model.facilities import Facilities
            return isinstance(obj, Facilities)
        except ImportError:
            return obj.__class__.__name__ == 'Facilities'

    def __repr__(self):
        return f"Room(id={self.__room_id!r}, room_number={self.__room_number!r}, hotel={self.__hotel!r})"

    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def room_number(self) -> str:
        return self.__room_number

    @room_number.setter
    def room_number(self, room_number: str) -> None:
        if not room_number:
            raise ValueError("room_number wird benötigt.")
        if not isinstance(room_number, str):
            raise ValueError("room_number muss string sein.")
        self.__room_number = room_number

    @property
    def price_per_night(self) -> float:
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, price_per_night: float) -> None:
        if not price_per_night:
            raise ValueError("price_per_night wird benötigt.")
        if not isinstance(price_per_night, float):
            raise ValueError("price_per_night muss float sein.")
        self.__price_per_night = price_per_night

    @property
    def room_type(self) -> Room_Type:
        return self.__room_type

    @room_type.setter
    def room_type(self, room_type: Room_Type) -> None:
        if not room_type:
            raise ValueError("room_type wird benötigt.")
        if not self._is_room_type(room_type):
            raise ValueError("room_type muss Room_Type Instanz sein.")
        self.__room_type = room_type

    @property
    def hotel(self) -> Hotel:
        return self.__hotel

    @property
    def hotel_id(self) -> int:
        return self.__hotel.hotel_id if self.__hotel else None

    @hotel.setter
    def hotel(self, hotel: Hotel) -> None:
        if hotel is not None and not self._is_hotel(hotel):
            raise ValueError("hotel muss Hotel Instanz sein.")
        if self.__hotel is not hotel:
            if self.__hotel is not None:
                self.__hotel.remove_room(self)
            self.__hotel = hotel
            if hotel is not None:
                hotel.add_room(self)

    def _is_hotel(self, obj) -> bool:
        try:
            from model.hotel import Hotel
            return isinstance(obj, Hotel)
        except ImportError:
            return obj.__class__.__name__ == 'Hotel'

    @property
    def facilities(self) -> list[Facilities]:
        return self.__facilities.copy()

    def add_room_facilities(self, facilities: Facilities) -> None:
        if not facilities:
            raise ValueError("facilities wird benötigt.")
        if not self._is_facilities(facilities):
            raise ValueError("facilities muss Facilities Instanz sein.")
        if facilities not in self.__facilities:
            self.__facilities.append(facilities)
            if hasattr(facilities, 'room'):
                facilities.room = self

    def remove_room_facilities(self, facilities: Facilities) -> None:
        if not facilities:
            raise ValueError("room_facilities wird benötigt.")
        if not self._is_facilities(facilities):
            raise ValueError("room_facilities muss Facilities Instanz sein.")
        if facilities in self.__facilities:
            self.__facilities.remove(facilities)
            if hasattr(facilities, 'room'):
                facilities.room = None
