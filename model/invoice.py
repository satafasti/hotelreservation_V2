from typing import List
from model.booking import Booking

class Invoice:
    def __init__(self, invoice_id: int, booking_id: int, issue_date: str, total_amount: float):
        if invoice_id is not None and invoice_id <= 0:
            raise ValueError("invoice_id must be positive or None")
        if not issue_date:
            raise ValueError("issue_date must not be empty")

        self.__invoice_id = invoice_id
        self.__booking_id = booking_id
        self.__issue_date = issue_date
        self.__total_amount = total_amount

    @property
    def invoice_id(self) -> int:
        return self.__invoice_id

    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @property
    def issue_date(self) -> str:
        return self.__issue_date

# Wird total amount berechnet?
    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value: float):
        if value < 0:
            raise ValueError("Total amount must be non-negative")
        self.__total_amount = value

    def __repr__(self) -> str:
        return f"Invoice(id={self.invoice_id}, booking_id={self.booking_id}, amount={self.total_amount:.2f})"



