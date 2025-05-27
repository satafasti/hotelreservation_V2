from typing import List
from model.booking import Booking

class Invoice:

    def __init__(self, invoice_id: int, issue_date: str, booking_id:int, total_amount:float):
        if invoice_id is not None and invoice_id <= 0:
            raise ValueError("invoice_id must be positive or None")
        if not issue_date:
            raise ValueError("issue_date must not be empty")

        self.__invoice_id = invoice_id
        self.__issue_date = issue_date
        self.__booking_id = booking_id
        self.__bookings = []
        self.__total_amount = total_amount

    def __repr__(self) -> str:
        return f"Invoice(id={self.invoice_id}, booking_id={self.booking_id}, amount={self.get_total_amount():.2f})"

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def invoice_id(self) -> int:
        return self.__invoice_id

    @property
    def issue_date(self) -> str:
        return self.__issue_date

    @property
    def bookings(self) -> List[Booking]:
        return self.__bookings

    def add_booking(self, booking):
        if not isinstance(booking, Booking):
            raise TypeError("booking must be a Booking instance")
        self.__bookings.append(booking)

    def get_total_amount(self) -> float:
        return sum(b.total_amount for b in self.__bookings)


