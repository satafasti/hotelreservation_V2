class Invoice:

    def __init__(self, invoice_id: int, issue_date: str, booking_id:int, total_amount:float):
        if invoice_id <= 0:
            raise ValueError("invoice_id must be positive")
        if not issue_date:
            raise ValueError("issue_date must not be empty")

        self.__invoice_id = invoice_id
        self.__issue_date = issue_date
        self.__booking_id = booking_id
        self.__bookings = []
        self.__total_amount = total_amount

    @property
    def total_amount(self):
        return self.__total_amount

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
    def bookings(self) -> list:
        return self.__bookings

    def add_booking(self, booking):
        self.__bookings.append(booking)

    def get_total_amount(self) -> float:
        return sum(b.total_amount for b in self.__bookings)

