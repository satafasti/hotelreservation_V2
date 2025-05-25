from __future__ import annotations
#from typing import TYPE_CHECKING #Referenzprojekt
import model.room_type
import model.facilities
#from Sarina_Test import Room_Type #=> wird noch benötigt?


#if TYPE_CHECKING: #Referenzprojekt
    #from model.artist import Artist #Referenzprojekt
    #from model.track import Track #Referenzprojekt

class Room:
    def __init__(self, room_id : int, room_number : int, price_per_night : float,  description: model.room_type.Room_Type, room_available=True): #ID ist in SQL enthalten?
        if not room_id:
            raise ValueError("room_id must be set")
        if not isinstance(room_id, int):
            raise TypeError("room_id must be a int")
        if not room_number:
            raise ValueError("room_number must be set")
        if not isinstance(room_id, int):
            raise TypeError("room_number must be a int")
        if not price_per_night:
            raise ValueError("price_per_night must be set")
        if not isinstance(price_per_night, float):
            raise TypeError("price_per_night must be a float")

        self.__room_id = room_id
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__description = description #Description von Class room_type soll übergeben werden
        self.__facility_name = [] #Liste für Facilities des Raumes
        self.room_available = room_available


    @property
    def room_id(self):
        return self.__room_id

    @room_id.setter
    def room_id(self,new_room_id):
        self.__room_id = new_room_id

#room_number
    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self,new_room_number):
        self.__room_number = new_room_number

#price per night
    @property
    def price_per_night(self):
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, new_price_per_night):
        self.__price_per_night = new_price_per_night


#description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,new_description):
        self.__description = new_description


#facility_name
    @property
    def facility_name(self):
        return self.__facility_name

    @facility_name.setter
    def facility_name(self,new_facility_name):
        self.__facility_name = new_facility_name