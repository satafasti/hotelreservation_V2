import model
from data_access.hotel_dal import HotelDataAccess

class HotelManager:
    def __init__(self, db_path: str = None):
        self.__hotel_dal = HotelDataAccess(db_path)

    def create_hotel(self, hotel: model.Hotel, address: model.Address, room: model.Room):
        return self.__hotel_dal.create_new_hotel(hotel, address, room)

    def read_hotels_by_similar_name(self, name: str) -> list[model.Hotel]:
        return self.__hotel_dal.read_hotels_like_name(name)

    def delete_hotel(self, hotel: model.Hotel) -> None:
        self.__hotel_dal.delete_hotel(hotel)

    def read_all_hotels_extended_info(self):
        return self.__hotel_dal.read_all_hotels_extended_info()


#Das Projekt enthält im Modul HotelManager Methoden wie read_hotel, read_all_hotels oder update_hotel. Diese Methoden leiten im Wesentlichen nur an die Data‑Access‑Schicht (HotelDataAccess) weiter.
#Im User Interface wird jedoch direkt HotelDataAccess verwendet. So werden Hotels z.B. im Gast-UI eingelesen und ausgewählt,

    #def read_hotel(self, hotel_id: int):
        #return self.__hotel_dal.read_hotel_by_id(hotel_id)

    #def read_all_hotels(self) -> list[model.Hotel]:
        #return self.__hotel_dal.read_all_hotels()

    # def read_all_hotels_as_df(self) -> pd.DataFrame:
        #return self.__hotel_dal.read_all_hotels_as_df()

    # def read_hotels_by_similar_name_as_df(self, name: str) -> pd.DataFrame:
        #return self.__hotel_dal.read_hotels_like_name_as_df(name)

    #def update_hotel(self, hotel: model.Hotel) -> None:
        #self.__hotel_dal.update_hotel(hotel)
