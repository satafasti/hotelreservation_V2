from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.room import Room

class Hotel:
    def __init__(self, hotel_id: int, name:str, stars: int, address_id: int):
        if not hotel_id:
           raise ValueError("hotel_id wird benötigt.")
        if not isinstance(hotel_id, int):
            raise ValueError("hotel_id muss integer sein.")
        if not name:
            raise ValueError("name wird benötigt.")
        if not isinstance(name, str):
            raise ValueError("name must be a string.")
        if not stars:
            raise ValueError("stars wird benötigt.")
        if not isinstance(stars, int):
            raise ValueError("stars must be an integer.")
        if not address_id:
            raise ValueError("address_id wird benötigt.")
        if not isinstance(address_id, int):
            raise ValueError("address_id must be an integer.")

        self.__hotel_id: int = hotel_id
        self.__name: str = name
        self.__stars: int = stars
        self.__address_id: int = address_id
        self.__rooms: list[Room] = []

    def __repr__(self):
        return f"Hotel(id={self.__hotel_id!r}, name={self.__name!r}), stars={self.__stars!r}, address={self.__address_id!r}, rooms={self.__rooms!r}"

    @property
    def hotel_id(self) -> int:
        return self.__hotel_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name:
            raise ValueError("name is required.")
        if not isinstance(name, str):
            raise ValueError("name must be a string.")
        self.__name = name

    @property
    def stars(self) -> int:
        return self.__stars

    @stars.setter
    def stars(self, stars: int) -> None:
        if stars is None:
            raise ValueError("stars wird benötigt.")
        if not isinstance(stars, int):
            raise ValueError("stars muss integer sein.")
        if not (1 <= stars <= 5):
            raise ValueError("stars muss zwischen 1 und 5 sein.")
        self.__stars = stars

    @property
    def address_id(self) -> int:
        return self.__address_id

    @address_id.setter
    def address_id(self, address_id: int) -> None:
        if not address_id:
            raise ValueError("address_id wird benötigt.")
        if not isinstance(address_id, int):
            raise ValueError("address_id muss integer sein.")
        self.__address_id = address_id

    @property
    def rooms(self) -> list[Room]:
        # Return a copy so that the caller cannot modify the private list directly.
        return self.__rooms.copy()

    def add_room(self, room: Room) -> None:
        from model import Room

        if not room:
            raise ValueError("room is required.")
        if not isinstance(room, Room):
            raise ValueError("room must be part of a hotel.")
        if room not in self.__rooms:
            self.__rooms.append(room)
            room.hotel = self

    def remove_room(self, room: Room) -> None:
        from model.room import Room

        if not room:
            raise ValueError("room is required.")
        if not isinstance(room, Room):
            raise ValueError("room must be part of a hotel.")
        if room in self.__rooms:
            self.__rooms.remove(room)
            room.hotel = None
















