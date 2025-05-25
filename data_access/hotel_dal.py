from unittest import result
import pandas as pd
import model
import data_access

### Code gemäss Referenzprojekt
class HotelDAL(data_access.BaseDal):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_hotel(self, name:str, stars: int, address_id: int) -> model.Hotel:
        if name is None:
            raise ValueError("Hotelname wird benötigt.")

        sql = """
        INSERT INTO Hotel (name, stars, address_id) VALUES (?, ?, ?)
        """
        params = tuple([name, stars, address_id])
        last_row_id, row_count = self.execute(sql, params)
        return model.Hotel(hotel_id=last_row_id, name=name, stars=stars, address_id=address_id)

    def read_hotels_by_id(self, hotel_id: int) -> model.Hotel | None:
        if hotel_id is None:
            raise ValueError("hotel_id wird benötigt.")

        sql = """
        SELECT hotel_id = ?, name = ?, stars = ?, address_id = ? FROM Hotel WHERE hotel_id = ?
        """
        params = tuple([hotel_id])
        result = self.fetchone(sql, params)
        if result:
            hotel_id, name, stars, address_id = result
            return model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address_id=address_id)
        else:
            return None

    def read_all_hotels(self) -> list[model.Hotel]:
        sql = """
        SELECT hotel_id = ?, name = ?, stars = ?, address_id = ? FROM Hotel
        """
        hotels = self.fetchall(sql)

        return [model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address_id=address_id) for hotel_id, name, stars, address_id in hotels]

    def read_all_hotels_as_df(self) -> pd.DataFrame:
        sql = """
        SELECT hotel_id = ?, name = ?, stars = ?, address_id = ? FROM Hotel
        """
        return pd.read_sql(sql, self.get_connection(), index_col='hotel_id')

    def read_hotels_like_name(self, name: str) -> list[model.Hotel]:
        sql = """
        SELECT hotel_id = ?, name = ? FROM Hotel WHERE name LIKE ?
        """
        params = tuple([f"%{name}%"])
        hotels = self.fetchall(sql, params)
        return [model.Hotel(hotel_id=hotel_id, name=name) for hotel_id, name in hotels]

    def read_hotels_like_name_as_df(self, name: str) -> pd.DataFrame:
        sql = """
                SELECT hotel_id = ?, name = ? FROM Hotel WHERE name LIKE ?
                """
        params = tuple([f"%{name}%"])
        return pd.read_sql(sql, self.get_connection(), params=params, index_col='hotel_id')

    def update_hotel(self, hotel: model.Hotel) -> None:
        if hotel is None:
            raise ValueError("Hotel kann nicht leer sein.")

        sql = """
        UPDATE Hotel SET name = ?, stars = ?, address_id = ? WHERE hotel_id = ?
        """
        params = tuple([hotel.name, hotel.name, hotel.address_id, hotel.hotel_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_hotel(self, hotel: model.Hotel) -> None:
        if hotel is None:
            raise ValueError("Hotel kann nicht leer sein.")

        sql = """
        DELETE FROM Hotel WHERE hotel_id = ?
        """
        params = tuple([hotel.hotel_id])
        last_row_id, row_count = self.execute(sql, params)