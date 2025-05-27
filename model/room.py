from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.hotel import Hotel
    from model.room_type import Room_Type
    from model.room_facilities import Room_Facilities

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

        self.__room_id: int = room_id
        self.__room_number: str = room_number
        self.__hotel: Hotel = hotel
        if hotel is not None:
            hotel.add_room(self)
        self.__room_facilities: list[Room_Facilities] = [] #TODO Room_Facilities erstellen

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
            if hotel is not None and self not in hotel.room:
                hotel.add_room(self)

    @property
    def room_facilities(self) -> list[Room_Facilities]:
        return self.__room_facilities.copy()

    def add_room_facilities(self, room_facilities: Room_Facilities) -> None:
        from model import Room_Facilities

        if not room_facilities:
            raise ValueError("room_facilities wird benötigt.")
        if not isinstance(room_facilities, Room_Facilities):
            raise ValueError("room_facilities muss Bestandteil von Room_Facilities sein.")
        if room_facilities not in self.__room_facilities:
            self.__room_facilities.append(room_facilities)
            room_facilities.room = self

    def remove_room_facilities(self, room_facilities: Room_Facilities) -> None:
        from model import Room_Facilities

        if not room_facilities:
            raise ValueError("room_facilities wird benötigt.")
        if not isinstance(room_facilities, Room_Facilities):
            raise ValueError("room_facilities muss Bestandteil von Room_Facilities sein.")
        if room_facilities in self.__room_facilities:
            self.__room_facilities.remove(room_facilities)
            room_facilities.room = None
