# from model import guest, room
from datetime import datetime, date

class Booking:

    def __init__(
        self,
        booking_id: int,
        guest_id: int,
        room_id: int,
        check_in_date: str,
        check_out_date: str,
        is_cancelled: bool,
        total_amount: float,

    ):
        if booking_id <= 0:
            raise ValueError("booking_id muss eine positive Ganzzahl sein")
        if booking_id is None:
            raise ValueError("booking_id ist erforderlich")
        if not isinstance(booking_id, int):
            raise ValueError("booking_id muss eine Ganzzahl sein")

        if not check_in_date:
            raise ValueError("check_in_date darf nicht leer sein")
        if not isinstance(check_in_date, (str, date, datetime)):
            raise ValueError("check_in_date muss ein String oder Datum sein")

        if not check_out_date:
            raise ValueError("check_out_date darf nicht leer sein")
        if not isinstance(check_out_date, (str, date, datetime)):
            raise ValueError("check_out_date muss ein String oder Datum sein")

        if total_amount < 0:
            raise ValueError("total_amount darf nicht negativ sein")
        if not total_amount:
            raise ValueError("total_amount ist erforderlich")
        if not isinstance(total_amount, float):
            raise TypeError("total_amount muss ein Gleitkommawert sein")

        if guest_id <= 0:
            raise ValueError("guest_id muss eine positive Ganzzahl sein")
        if not guest_id:
            raise ValueError("guest_id ist erforderlich")
        if not isinstance(guest_id, int):
            raise ValueError("guest_id muss eine Ganzzahl sein")

        if room_id <= 0:
            raise ValueError("room_id muss eine positive Ganzzahl sein")
        if not room_id:
            raise ValueError("room_id ist erforderlich")
        if not isinstance(room_id, int):
            raise ValueError("room_id muss eine Ganzzahl sein")

        if not isinstance(is_cancelled, bool):
            raise TypeError("is_cancelled muss ein boolescher Wert sein")

        self.__booking_id = booking_id
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__is_cancelled = is_cancelled
        self.__total_amount = total_amount
        self.__guest_id = guest_id
        self.__room_id = room_id
#        self.__invoice = None
#        self.__guest = None
 #       self.__room = None

    @property
    def booking_id(self) -> int:
        return self.__booking_id



    @property
    def check_in_date(self) -> str:
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, check_in_date) -> None:
        if isinstance(check_in_date, str):
            try:
                datetime.strptime(check_in_date, '%Y-%m-%d')
                self.__check_in_date = check_in_date
            except ValueError:
                raise ValueError("Datum muss im Format YYYY-MM-DD sein")
        elif isinstance(check_in_date, (date, datetime)):
            self.__check_in_date = check_in_date.strftime('%Y-%m-%d')
        else:
            raise TypeError("Datum muss ein String, date oder datetime Objekt sein")

    @property
    def check_out_date(self) -> str:
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, check_out_date) -> None:
        if isinstance(check_out_date, str):
            try:
                datetime.strptime(check_out_date, '%Y-%m-%d')
                self.__check_out_date = check_out_date
            except ValueError:
                raise ValueError("Datum muss im Format YYYY-MM-DD sein")
        elif isinstance(check_out_date, (date, datetime)):
            self.__check_out_date = check_out_date.strftime('%Y-%m-%d')
        else:
            raise TypeError("Datum muss ein String, date oder datetime Objekt sein")

    @property
    def is_cancelled(self) -> bool:
        return self.__is_cancelled



    @is_cancelled.setter
    def is_cancelled(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("is_cancelled muss ein boolescher Wert sein")
        self.__is_cancelled = value

    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value: float):
        if value < 0:
            raise ValueError("total_amount darf nicht negativ sein")
        self.__total_amount = value

    @property
    def guest_id(self) -> int:
        return self.__guest_id

    @property
    def room_id(self) -> int:
        return self.__room_id



 ####   def add_invoice(self, invoice: 'invoice'):
 ###       if not isinstance(invoice, invoice):
  ##          raise TypeError("invoice must be an instance of Invoice")
  #      self.__invoice = invoice
  #      invoice.add_booking(self)

  #  def add_guest(self, guest: 'guest'):
  #      if not isinstance(guest, guest):
 #           raise TypeError("guest must be an instance of Guest")
 #       self.__guest = guest

 #  def add_room(self, room: 'room'):
 #       if not isinstance(room, room):
   #         raise TypeError("room must be an instance of Room")
   #     self.__room = room
