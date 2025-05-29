from __future__ import annotations
from typing import TYPE_CHECKING
from model.room_type import Room_Type
from model.facilities import Facilities

if TYPE_CHECKING:
    from model.hotel import Hotel

#TODO Code für Projekt ergänzen
### Code gemäss Referenzprojekt
class Room:
    def __init__(self, room_id: int, hotel: Hotel, room_number: str, room_type: Room_Type, price_per_night: float):
        if not room_id:
            raise ValueError("room_id wird benötigt.") #wird das benötigt? sollte eigentlich automatisch erstellt werden durch DB.
        if not isinstance(room_id, int):
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
        if not isinstance(room_type, Room_Type):
            raise ValueError("room_type muss integer sein.")

        self.__room_id: int = room_id
        self.__room_number: str = room_number
        self.__hotel: Hotel = hotel
        if hotel is not None:
            hotel.add_room(self)
        self.__facilities: list[Facilities] = []
        self.__room_type: Room_Type = room_type

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
    def hotel(self) -> Hotel:
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel: Hotel) -> None:
        from model import Hotel
        if hotel is not None and not isinstance(hotel, Hotel):
            raise ValueError("hotel muss Bestandteil von Hotel sein.")
        if self.__hotel is not hotel:
            if self.__hotel is not None:
                self.__hotel.remove_room(self)
            self.__hotel = hotel
            if hotel is not None and self not in hotel:
                hotel.add_room(self)

    @property
    def facilities(self) -> list[Facilities]:
        return self.__facilities.copy()

    def add_room_facilities(self, facilities: Facilities) -> None:

        if not facilities:
            raise ValueError("facilities wird benötigt.")
        if not isinstance(facilities, Facilities):
            raise ValueError("facilities muss Bestandteil von Facilities sein.")
        if facilities not in self.__facilities:
            self.__facilities.append(facilities)
            facilities.room = self

    def remove_room_facilities(self, facilities: Facilities) -> None:

        if not facilities:
            raise ValueError("room_facilities wird benötigt.")
        if not isinstance(facilities, Facilities):
            raise ValueError("room_facilities muss Bestandteil von Room_Facilities sein.")
        if facilities in self.__facilities:
            self.__facilities.remove(facilities)
            facilities.room = None
