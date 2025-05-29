import model
from data_access.base_dal import BaseDataAccess

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_hotel(self, hotel: model.Hotel, address: model.Address, room: model.Room) -> model.Hotel:
        address_sql = """
                      INSERT INTO Address (street, city, zip_code)
                      VALUES (?, ?, ?) 
                      """
        address_params = (address.street, address.city, address.zip_code)
        address_id, _ = self.execute(address_sql, address_params)

        hotel_sql = """
                    INSERT INTO Hotel (name, stars, address_id)
                    VALUES (?, ?, ?) 
                    """
        hotel_params = (hotel.name, hotel.stars, address_id)
        hotel_id, _ = self.execute(hotel_sql, hotel_params)

        room_type_sql = """
                   INSERT INTO Room_Type (description, max_guests)
                   VALUES (?, ?) 
                   """
        room_type_params = (room.room_type.description, room.room_type.max_guests)
        type_id, _ = self.execute(room_type_sql, room_type_params)

        room_sql = """
                   INSERT INTO Room (hotel_id, room_number, type_id, price_per_night)
                   VALUES (?, ?, ?, ?) 
                   """
        room_params = (hotel_id, room.room_number, type_id, room.price_per_night)
        self.execute(room_sql, room_params)


        return model.Hotel(hotel_id=hotel_id, name=hotel.name, stars=hotel.stars, address_id=address_id)

    def read_hotel_by_id(self, hotel_id: int) -> model.Hotel | None:
        if hotel_id is None:
            raise ValueError("hotel_id wird benötigt.")

        sql = """
        SELECT hotel_id, name, stars, address_id FROM Hotel WHERE hotel_id = ?
        """
        params = (hotel_id,)
        result = self.fetchone(sql, params)
        if result:
            hotel_id, name, stars, address_id = result
            return model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address_id=address_id)
        else:
            return None

    def read_all_hotels(self) -> list[model.Hotel]:
        sql = """
        SELECT hotel_id, name, stars, address_id FROM Hotel
        """
        hotels = self.fetchall(sql)
        return [model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address_id=address_id)
                for hotel_id, name, stars, address_id in hotels]


    #def read_all_hotels_as_df(self) -> pd.DataFrame:
    #    sql = """
    #    SELECT hotel_id = ?, name = ?, stars = ?, address_id = ? FROM Hotel
    #    """
    #    return pd.read_sql(sql, self.get_connection(), index_col='hotel_id')

    def read_hotels_like_name(self, name: str) -> list[model.Hotel]:
        sql = """
        SELECT hotel_id, name, stars, address_id FROM Hotel WHERE name LIKE ?
        """
        params = (f"%{name}%",)
        hotels = self.fetchall(sql, params)
        return [model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address_id=address_id)
                for hotel_id, name, stars, address_id in hotels]

    #def read_hotels_like_name_as_df(self, name: str) -> pd.DataFrame:
    #    sql = """
    #            SELECT hotel_id = ?, name = ? FROM Hotel WHERE name LIKE ?
    #            """
    #    params = tuple([f"%{name}%"])
    #    return pd.read_sql(sql, self.get_connection(), params=params, index_col='hotel_id')

    def update_hotel(self, hotel: model.Hotel) -> None:
        if hotel is None:
            raise ValueError("Hotel kann nicht leer sein.")

        sql = """
        UPDATE Hotel SET name = ?, stars = ?, address_id = ? WHERE hotel_id = ?
        """
        params = (hotel.name, hotel.stars, hotel.address_id, hotel.hotel_id)
        last_row_id, row_count = self.execute(sql, params)

    def delete_hotel(self, hotel: model.Hotel) -> None:
        if hotel is None:
            raise ValueError("Hotel kann nicht leer sein.")

        sql = """
        DELETE FROM Hotel WHERE hotel_id = ?
        """
        params = (hotel.hotel_id,)
        last_row_id, row_count = self.execute(sql, params)

    def search_hotel(self, hotel: model.Hotel) -> list[model.Hotel]:
        return []