from Tanja_Test import Address


class Hotel:
    def __init__ (self, hotel_id:int, name:str, stars:int, address: Address, rooms: list, address_id:int): #address als str oder address_id?
        if not hotel_id:
            raise ValueError("hotel_id must be set")
        if not isinstance(hotel_id , int):
            raise TypeError("hotel_id must be a int")
        if not name:
            raise ValueError("name must be set")
        if not isinstance(name , str):
            raise TypeError("name must be a string")
        if not address:
            raise ValueError("address must be set")
        if not isinstance(address, Address):
            raise TypeError("address must be an Address instance")

        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__rooms = rooms
        self.__address_id = address_id #single instance of class Address, as of now no backwards link from address -> hotel necessary, to find all hotels in a city loop through existing instances by city

    @property    
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("name must be set")
        if not isinstance(new_name, str):
            raise TypeError("name must be a string")
        self.__name = new_name

    @property
    def hotel_id(self):
        return self.__hotel_id
    
    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, new_stars):
        if not isinstance(new_stars, int):
            raise TypeError("new_stars must be a integer")
        elif 0 < new_stars <= 5:
            self.__stars = new_stars
        else:
            print("Stars must be a number between 1 and 5.")

    @property
    def address_id(self):
        return self.__address_id
















