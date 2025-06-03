from typing import Optional

class Payment:
    def __init__(self, payment_id: Optional[int], booking_id: int, payment_date: str, amount: float, payment_method: str):
        if payment_id is not None:
            if not isinstance(payment_id, int):
                raise TypeError("payment_id must be an integer")
            if payment_id <= 0:
                raise ValueError("payment_id must be positive")
        if not isinstance(booking_id, int) or booking_id <= 0:
            raise ValueError("booking_id must be a positive integer")
        if not payment_date:
            raise ValueError("payment_date is required")
        if not isinstance(payment_date, str):
            raise TypeError("payment_date must be a string")
        if amount is None or amount < 0:
            raise ValueError("amount must be non-negative")
        if not isinstance(amount, float):
            raise TypeError("amount must be a float")
        if not payment_method:
            raise ValueError("payment_method is required")
        if not isinstance(payment_method, str):
            raise TypeError("payment_method must be a string")

        self.__payment_id = payment_id
        self.__booking_id = booking_id
        self.__payment_date = payment_date
        self.__amount = amount
        self.__payment_method = payment_method

    def __repr__(self) -> str:
        return f"Payment(id={self.payment_id}, booking_id={self.booking_id}, amount={self.amount:.2f}, method='{self.payment_method}')"

    @property
    def payment_id(self) -> Optional[int]:
        return self.__payment_id

    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @property
    def payment_date(self) -> str:
        return self.__payment_date

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, value: float):
        if value < 0:
            raise ValueError("amount must be non-negative")
        self.__amount = value

    @property
    def payment_method(self) -> str:
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, method: str):
        if not method:
            raise ValueError("payment_method is required")
        if not isinstance(method, str):
            raise TypeError("payment_method must be a string")
        self.__payment_method = method