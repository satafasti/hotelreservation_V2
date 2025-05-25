from __future__ import annotations
import model
from data_access.base_dal import BaseDAL



class HotelDAL(BaseDAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_hotel(self, hotel: model.Hotel):
        sql = """
        INSERT INTO Hotel(hotel_id, name, stars, address_id) VALUES (?, ?, ?, ?)
        """
        params = (hotel.hotel_id if hotel else None, hotel.name, hotel.stars, hotel.address_id)
        self.execute(sql, params)


    def show_all_hotels(self):
        sql = "SELECT * FROM Hotel"
        results = self.fetch_all(sql)  # kommt aus BaseDAL
        hotels = []

        for row in results:
            hotel_id, name, stars, address_id = row
            address = self.get_address_by_id(address_id) #Tanja: hier hats jetzt neue error drin, weil get_address_by_id und rooms nirgends definiert ist
            rooms = self.get_rooms_by_hotel(hotel_id)  # brauchst du auch

            hotel = model.Hotel(hotel_id, name, stars, address, rooms, address_id)
            hotels.append(hotel)

        return hotels

    def update_hotel(self, hotel_id : int, name:str, stars: int, address_id: int):
        sql = """
        UPDATE Hotel SET name = ? AND stars = ? WHERE hotel_id = ?
        """
        params = (name, stars, hotel_id, address_id)
        self.execute(sql, params)

    def delete_hotel(self, hotel: model.Hotel):
        sql = """
        DELETE FROM Hotel WHERE hotel_id = ?
        """
        params = (hotel.hotel_id,)
        self.execute(sql, params)

    def show_hotel_by_id(self, hotel_id : int):
        sql = """
        SELECT * FROM Hotel WHERE hotel_id = ?
        """
        params = (hotel_id,)
        result = self.fetch_one(sql, params)
        if result:
            hotel_id, name, stars, address_id = result
            return model.Hotel(hotel_id, name, stars, address_id)
        else:
            return None