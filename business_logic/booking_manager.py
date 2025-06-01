from data_access.booking_dal import BookingDataAccess
from model.room import Room
from model.booking import Booking
from typing import Optional, List
from datetime import datetime


class BookingManager:
    def __init__(self, db_path: str = None): self.__dal = BookingDataAccess(db_path)

    def create_new_booking(self, guest_id: int, room_id: int, check_in_date: str, check_out_date: str, price_per_night: float) -> Booking:
        check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
        num_nights = (check_out - check_in).days
        dynamic_price = self.calculate_dynamic_price(price_per_night, check_in_date)
        total_price = num_nights * dynamic_price

        booking = Booking(
            booking_id=None,
            guest_id=guest_id,
            room_id=room_id,
            check_in_date=check_in.strftime("%Y-%m-%d"),
            check_out_date=check_out.strftime("%Y-%m-%d"),
            is_cancelled=False,
            total_amount=total_price
        )
        return self.__dal.create_new_booking(booking)

    def calculate_dynamic_price(self, base_price: float, check_in: str) -> float:
        month = datetime.strptime(check_in, "%Y-%m-%d").month
        return base_price * 1.3 if month in [6, 7, 8, 12] else base_price * 0.9 if month in [1, 2, 3, 11] else base_price

    def read_booking_by_id(self, booking_id: int) -> Optional[Booking]: return self.__dal.read_booking_by_id(booking_id)

    def read_all_bookings(self) -> List[Booking]: return self.__dal.read_all_bookings()

    def update_booking(self, booking: Booking): self.__dal.update_booking(booking)

    def delete_booking(self, booking: Booking): self.__dal.delete_booking(booking)

    def cancel_booking(self, booking_id: int):
        booking = self.__dal.read_booking_by_id(booking_id)
        if booking is None: raise ValueError("Booking not found.")
        booking.is_cancelled = True
        self.__dal.update_booking(booking)

    def find_available_room(self, room_type_description: str, check_in: str, check_out: str) -> Optional[Room]:
        return self.__dal.find_available_room(room_type_description, check_in, check_out)
