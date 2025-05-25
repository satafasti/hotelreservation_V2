import data_access
from model import Room
from model import Room_Type


class HotelManager:
    def __init__(self) -> None:
        self.__hotel_dal = data_access.HotelDAL()
        self.__room_dal = data_access.RoomDAL()
        self.__rooms = []

    def get_hotel_details(self, hotel_id : int):
        hotel = self.__hotel_dal.show_hotel_by_id(hotel_id)
        if hotel:
            return f"Hotel name: {hotel.name}, Stars: {hotel.stars}"
        else:
            return "Hotel nicht gefunden."

    def add_room(self, room_id: int, room_number: int, price_per_night: float, type_id: Room_Type):
        room = Room(room_id, room_number, price_per_night, type_id)
        self.__rooms.append(room)

    def remove_room(self, room: Room) -> None:
        from model import Room

        if not room:
            raise   ValueError ("room cannot be None")
        if not isinstance(room, Room):
            raise ValueError ("room must be an instance of Room")
        if room in self.__rooms:
            self.__rooms.remove(room)


    def get_room_details(self, room_id : int, room_type : Room_Type):
        room = self.__room_dal.show_room_by_id(room_id)
        if room:
            return f"Room ID: {room.room_id}, Room Number: {room.room_number}, Price per Night: {room.price_per_night}, Room Type: {room_type.description}"
        else:
            return "Zimmer nicht gefunden."

    def search_hotels(self, city=None, stars=None, guests=None):
        results = []

        hotel = self.__hotel_dal.show_all_hotels()

        for hotel in hotel:  # wir haben keine Liste von Hotels, muss zwingend auf hotel_id referenziert werden?
            if city and hotel.address.city.lower() != city.lower():
                continue
            if stars and hotel.stars < stars:
                continue

            for room in hotel.rooms:
                if guests and room.description.max_guests < guests:
                    continue
                if getattr(room, "room_available", True) is False:
                    continue

                # Sobald ein passender Raum gefunden wurde, reicht es – Hotel ist relevant
                results.append(hotel)
                break  # keine weiteren Zimmer prüfen

        return results



    #def show_room_details(self):
     #   print(f"Hotel name: {room.name}, {self.__stars} Stars")
      #  for room in self.__rooms:
       #     print(room.get_room_details())

    ## unclear if the show_room_details goes here, and it is correct? because we want to show the hotel details incl. the room details , only the room details will already be covered by the same function in the room class

###
    #def add_new_hotel(self, hotel_id: int, name: str, stars: int, address: str) -> Hotel:
        #if not name:
         #   raise ValueError("Hotel name cannot be empty.")
        #if not isinstance(name, str):
        #   raise ValueError("Hotel name must be a str")
        #if name not in self.__name: # irgendwie noch nicht ganz so logisch, daher wohl falsch
        #    self.__name.append(name)
        #    hotel.name = self
        #if not address:
        #    raise ValueError("Address cannot be empty.")
        #if not isinstance(name, str):
        #    raise ValueError("Address must be a str")
        #if address not in self.__address: # irgendwie noch nicht ganz so logisch, daher wohl falsch
        #    self.__address.append(address)
    #    hotel.address = self
###

