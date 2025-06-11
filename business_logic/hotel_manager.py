import model
from business_logic import BookingManager
from data_access.hotel_dal import HotelDataAccess
from data_access.room_facilities_dal import RoomFacilitiesDataAccess  # Neu hinzufügen


class HotelManager:
    def __init__(self, db_path: str = None):
        self.__hotel_dal = HotelDataAccess(db_path)
        self.__facilities_dal = RoomFacilitiesDataAccess(db_path)
        self.__booking_manager = BookingManager(db_path)

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

    def remove_duplicate_rooms(self, hotel):
        seen_room_ids = set()
        unique_rooms = []
        for room in hotel.rooms:
            if room.room_id not in seen_room_ids:
                unique_rooms.append(room)
                seen_room_ids.add(room.room_id)
        hotel.rooms = unique_rooms
        return hotel

    def get_available_rooms_for_period(self, hotel, check_in=None, check_out=None):
        if not check_in or not check_out:
            return hotel.rooms

        available_rooms = []
        for room in hotel.rooms:
            is_available = True
            for booking in getattr(room, "bookings", []):
                if not booking.is_cancelled:
                    if check_in < booking.check_out_date and check_out > booking.check_in_date:
                        is_available = False
                        break
            if is_available:
                available_rooms.append(room)
        return available_rooms

    def calculate_room_pricing(self, room, check_in=None):
        base_price = room.price_per_night
        dynamic_price = self.__booking_manager.calculate_dynamic_price(base_price, check_in) if check_in else base_price

        return {
            'base_price': base_price,
            'dynamic_price': dynamic_price,
            'price_difference': dynamic_price - base_price if check_in else 0,
            'has_seasonal_adjustment': check_in and dynamic_price != base_price
        }

    def calculate_total_pricing_summary(self, rooms, check_in=None, check_out=None):
        if not rooms:
            return None

        prices = []
        for room in rooms:
            price_info = self.calculate_room_pricing(room, check_in)
            prices.append(price_info['dynamic_price'])

        total_days = (check_out - check_in).days if check_in and check_out else None

        return {
            'min_price': min(prices),
            'max_price': max(prices),
            'total_days': total_days,
            'min_total': min(prices) * total_days if total_days else None,
            'max_total': max(prices) * total_days if total_days else None
        }

    def calculate_seasonal_adjustment(self, price_summary, check_in, nights):
        if not check_in:
            return None

        season_factor = self.__booking_manager.calculate_dynamic_price(1.0, check_in)
        base_min = price_summary['min_price'] / season_factor
        base_max = price_summary['max_price'] / season_factor

        total_min = price_summary['min_price'] * nights
        total_max = price_summary['max_price'] * nights
        base_total_min = base_min * nights
        base_total_max = base_max * nights

        return {
            'min_adjustment': total_min - base_total_min,
            'max_adjustment': total_max - base_total_max,
            'has_adjustment': abs(total_min - base_total_min) > 0.01
        }

    def show_hotel_info(self, hotel):
        print(f"\n--- {hotel.name} ---")
        print(f"Adresse: {hotel.address.street}, {hotel.address.zip_code} {hotel.address.city}")
        print(f"Sterne: {hotel.stars}")
        print(f"Verfügbare Zimmer: {len(hotel.rooms)}")


#Das Projekt enthält im Modul HotelManager Methoden wie read_hotel, read_all_hotels oder update_hotel. Diese Methoden leiten im Wesentlichen nur an die Data‑Access‑Schicht (HotelDataAccess) weiter.
#Im User Interface wird jedoch direkt HotelDataAccess verwendet. So werden Hotels z.B. im Gast-UI eingelesen und ausgewählt,

    # def read_all_hotels_as_df(self) -> pd.DataFrame:
        #return self.__hotel_dal.read_all_hotels_as_df()

    # def read_hotels_by_similar_name_as_df(self, name: str) -> pd.DataFrame:
        #return self.__hotel_dal.read_hotels_like_name_as_df(name)

