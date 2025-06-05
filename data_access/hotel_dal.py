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

        print(f"Raum hinzugefügt: {room.room_number} ({room.room_type.description}, {room.price_per_night}/Nacht)")
        return model.Hotel(hotel_id=hotel_id, name=hotel.name, stars=hotel.stars, address_id=address_id, )

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

    def read_all_hotels_extended_info(self) -> list[model.Hotel]:
        sql = """
              SELECT h.hotel_id,
                     h.name,
                     h.stars,
                     a.address_id,
                     a.street,
                     a.city,
                     a.zip_code,
                     r.room_id,
                     r.room_number,
                     r.price_per_night,
                     rt.type_id,
                     rt.description,
                     rt.max_guests,
                     b.booking_id,
                     b.guest_id,
                     b.check_in_date,
                     b.check_out_date,
                     b.is_cancelled,
                     b.total_amount
              FROM Hotel h
                       JOIN Address a ON h.address_id = a.address_id
                       LEFT JOIN Room r ON h.hotel_id = r.hotel_id
                       LEFT JOIN Room_Type rt ON r.type_id = rt.type_id
                       LEFT JOIN Booking b ON r.room_id = b.room_id
              ORDER BY h.hotel_id, r.room_id, b.booking_id \
              """

        results = self.fetchall(sql)

        hotels = {}
        for row in results:
            (
                hotel_id, name, stars,
                address_id, street, city, zip_code,
                room_id, room_number, price_per_night,
                type_id, description, max_guests,
                booking_id, guest_id, check_in_date, check_out_date,
                is_cancelled, total_amount
            ) = row

            # Adresse
            address = model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)

            # Hotel nur einmal anlegen
            if hotel_id not in hotels:
                hotels[hotel_id] = model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address_id=address_id)
                hotels[hotel_id].address = address
                hotels[hotel_id].rooms = []

            hotel = hotels[hotel_id]

            # Room anlegen (nur wenn nicht None)
            if room_id is not None:
                room_type = model.Room_Type(type_id=type_id, description=description, max_guests=max_guests)
                room = next((r for r in hotel.rooms if r.room_id == room_id), None)
                if not room:
                    room = model.Room(
                        room_id=room_id,
                        hotel=hotel,
                        room_number=room_number,
                        room_type=room_type,
                        price_per_night=price_per_night
                    )
                    room.bookings = []

                    # Ausstattung (Facilities) abrufen
                    with self.connection as conn:
                        facility_rows = conn.execute("""
                                                     SELECT f.facility_name
                                                     FROM Room_Facilities rf
                                                              JOIN Facilities f ON rf.facility_id = f.facility_id
                                                     WHERE rf.room_id = ?
                                                     """, (room_id,)).fetchall()
                        room.features = [row[0] for row in facility_rows] if facility_rows else []

                    hotel.rooms.append(room)

                # Booking anlegen (nur wenn nicht None)
                if booking_id is not None:
                    is_cancelled = bool(is_cancelled) if is_cancelled is not None else False
                    booking = model.Booking(
                        booking_id=booking_id,
                        room_id=room_id,
                        guest_id=guest_id,
                        check_in_date=check_in_date,
                        check_out_date=check_out_date,
                        is_cancelled=is_cancelled,
                        total_amount=total_amount
                    )
                    room.bookings.append(booking)

        return list(hotels.values())