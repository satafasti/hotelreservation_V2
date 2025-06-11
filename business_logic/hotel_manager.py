import model
from data_access.hotel_dal import HotelDataAccess
from data_access.room_facilities_dal import RoomFacilitiesDataAccess  # Neu hinzufügen


class HotelManager:
    def __init__(self, db_path: str = None):
        self.__hotel_dal = HotelDataAccess(db_path)
        self.__facilities_dal = RoomFacilitiesDataAccess(db_path)

    def create_hotel(self, hotel: model.Hotel, address: model.Address, room: model.Room):
        return self.__hotel_dal.create_new_hotel(hotel, address, room)

    def read_hotels_by_similar_name(self, name: str) -> list[model.Hotel]:
        return self.__hotel_dal.read_hotels_like_name(name)

    def delete_hotel(self, hotel: model.Hotel) -> None:
        self.__hotel_dal.delete_hotel(hotel)

    def read_all_hotels_extended_info(self):
        return self.__hotel_dal.read_all_hotels_extended_info()

#neu ergänzter Code 11.06.2025
    def add_room_to_hotel(self, hotel_id, room_number, description, max_guests, price_per_night, selected_facility_ids):
        return self.__hotel_dal.add_room_to_hotel(hotel_id, room_number, description, max_guests, price_per_night, selected_facility_ids)

    def get_all_facilities(self):
        return self.__facilities_dal.read_all_facilities()

    def add_facilities_to_first_room(self, hotel_id, selected_facility_ids):
        if not selected_facility_ids:
            return 0

        room_id_sql = "SELECT room_id FROM Room WHERE hotel_id = ? ORDER BY room_id LIMIT 1"
        room_result = self.__facilities_dal.fetchone(room_id_sql, (hotel_id,))

        if room_result:
            first_room_id = room_result[0]

            for facility_id in selected_facility_ids:
                facility_insert_sql = "INSERT INTO Room_Facilities (room_id, facility_id) VALUES (?, ?)"
                self.__facilities_dal.execute(facility_insert_sql, (first_room_id, facility_id))

            return len(selected_facility_ids)
        return 0

#neu aktivierter Code 11.06.2025
    def read_hotel(self, hotel_id: int):
        return self.__hotel_dal.read_hotel_by_id(hotel_id)

    def read_all_hotels(self) -> list[model.Hotel]:
        return self.__hotel_dal.read_all_hotels()

    def update_hotel(self, hotel: model.Hotel) -> None:
        self.__hotel_dal.update_hotel(hotel)


#Das Projekt enthält im Modul HotelManager Methoden wie read_hotel, read_all_hotels oder update_hotel. Diese Methoden leiten im Wesentlichen nur an die Data‑Access‑Schicht (HotelDataAccess) weiter.
#Im User Interface wird jedoch direkt HotelDataAccess verwendet. So werden Hotels z.B. im Gast-UI eingelesen und ausgewählt,

    # def read_all_hotels_as_df(self) -> pd.DataFrame:
        #return self.__hotel_dal.read_all_hotels_as_df()

    # def read_hotels_by_similar_name_as_df(self, name: str) -> pd.DataFrame:
        #return self.__hotel_dal.read_hotels_like_name_as_df(name)

