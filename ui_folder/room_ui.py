#2. Als Gast möchte ich Details zu verschiedenen Zimmertypen (Single, Double, Suite usw.), die in einem Hotel verfügbar sind, sehen, einschliesslich der maximalen Anzahl von Gästen für dieses Zimmer, Beschreibung, Preis und Ausstattung, um eine fundierte Entscheidung zu treffen.
#2.1. Ich möchte die folgenden Informationen pro Zimmer sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung, Ausstattung, Preis pro Nacht und Gesamtpreis.
#2.2. Ich möchte nur die verfügbaren Zimmer sehen, sofern ich meinen Aufenthalt (von – bis) spezifiziert habe.

from .address import Address
from .hotel import Hotel
from .guest import Guest
from .room_type import Room_Type
from .room import Room
from .booking import Booking
from .invoice import Invoice
from .facilities import Facilities
from .hotel_review import HotelReview


class Address:
    def __init__(self, address_id: int, street: str, city: str, zip_code: str):

        if address_id is None:
            raise ValueError("Address ID ist erforderlich")
        if not isinstance(address_id, int):
            raise TypeError("Address ID muss eine ganze Zahl sein")

        if not street:
            raise ValueError("Street ist erforderlich")
        if not isinstance(street, str):
            raise TypeError("Street muss ein String sein")

        if not city:
            raise ValueError("City ist erforderlich")
        if not isinstance(city, str):
            raise TypeError("City muss ein String sein")

        if not zip_code:
            raise ValueError("zip_code ist erforderlich")
        if not isinstance(zip_code, str):
            raise TypeError("zip_code muss ein String sein")

        self.__address_id: int = address_id
        self.__street: str = street
        self.__city: str = city
        self.__zip_code: str = zip_code

    @property
    def address_id(self) -> int:
        return self.__address_id

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        if not street:
            raise ValueError("Street ist erforderlich")
        if not isinstance(street, str):
            raise TypeError("Street muss ein String sein")
        self.__street = street

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        if not city:
            raise ValueError("City ist erforderlich")
        if not isinstance(city, str):
            raise TypeError("City muss ein String sein")
        self.__city = city

    @property
    def zip_code(self) -> str:
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, zip_code: str):
        if not zip_code:
            raise ValueError("Zip code ist erforderlich")
        if not isinstance(zip_code, str):
            raise TypeError("Zip code muss ein String sein")
        self.__zip_code = zip_code
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
                if booking_id is not None:
                    if not isinstance(booking_id, int):
                        raise ValueError("booking_id muss eine Ganzzahl sein")
                    if booking_id <= 0:
                        raise ValueError("booking_id muss eine positive Ganzzahl sein")

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
                if total_amount is None:
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

            def __repr__(self):
                return f"<Booking ID={self.booking_id}, Guest={self.guest_id}, Room={self.room_id}, From={self.check_in_date} To={self.check_out_date}>"

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

class Facilities:

    def __init__(self, facility_id : int, facility_name : str):

        if not facility_name:
            raise ValueError ("facility_name is required")
        if not isinstance(facility_name, str):
             raise TypeError("facility_name must be a string")

        self.__facility_id = facility_id
        self.__facility_name = facility_name

    @property
    def facility_id(self):
        return self.__facility_id

    @property
    def facility_name(self):
        return self.__facility_name

    def __repr__(self) -> str:
        return f"Facility(id={self.facility_id}, name='{self.facility_name}')"

    @facility_name.setter
    def facility_name(self, facility_name: str):
        if not facility_name:
            raise ValueError("facility_name is required")
        if not isinstance(facility_name, str):
            raise TypeError("facility_name must be a string")
        self.__facility_name = facility_name


from typing import Optional


class Guest:
    def __init__(self, guest_id: Optional[int], first_name: str, last_name: str, email: str, address_id: int):
        if guest_id is not None and not isinstance(guest_id, int):
            raise TypeError("Guest ID must be an integer")
        if not isinstance(guest_id, int):
            raise TypeError("Guest ID must be an integer")
        if not first_name:
            raise ValueError("First name is required")
        if not isinstance(first_name, str):
            raise TypeError("First name must be a string")
        if not last_name:
            raise ValueError("Last name is required")
        if not isinstance(last_name, str):
            raise TypeError("Last name must be a string")
        if not email:
            raise ValueError("Email is required")
        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        if address_id is not None and not isinstance(address_id, int):
            raise TypeError("Address ID must be an integer")

        self.__guest_id: int = guest_id
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__email: str = email
        self.__address_id: int = address_id

    def __repr__(self) -> str:
        return f"Guest(id={self.guest_id}, name='{self.first_name} {self.last_name}', email='{self.email}')"

    @property
    def guest_id(self) -> int:
        return self.__guest_id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, new_first_name: str):
        if not new_first_name:
            raise ValueError("First name required")
        if not isinstance(new_first_name, str):
            raise TypeError("First name must be a string")
        self.__first_name = new_first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @last_name.setter
    def last_name(self, new_last_name: str):
        if not new_last_name:
            raise ValueError("Last name required")
        if not isinstance(new_last_name, str):
            raise TypeError("Last name must be a string")
        self.__last_name = new_last_name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, new_email: str):
        if not new_email:
            raise ValueError("Email required")
        if not isinstance(new_email, str):
            raise TypeError("Email must be a string")
        self.__email = new_email

    @property
    def address_id(self) -> int:
        return self.__address_id

    @address_id.setter
    def address_id(self, new_address_id: int):
        if not new_address_id:
            raise ValueError("Address ID is required")
        if not isinstance(new_address_id, int):
            raise TypeError("Address ID must be an integer")
        self.__address_id = new_address_id

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.room import Room

class Hotel:
    def __init__(self, hotel_id: int, name:str, stars: int, address_id: int):
        if not hotel_id:
           raise ValueError("hotel_id wird benötigt.")
        if not isinstance(hotel_id, int):
            raise ValueError("hotel_id muss ein integer sein.")
        if not name:
            raise ValueError("name wird benötigt.")
        if not isinstance(name, str):
            raise ValueError("name must be a string.")
        if stars is None:
            raise ValueError("stars wird benötigt.")
        if not isinstance(stars, int):
            raise ValueError("stars muss ein integer sein.")
        if not (1 <= stars <= 5):
            raise ValueError("stars muss zwischen 1 und 5 sein.")
        if not address_id:
            raise ValueError("address_id wird benötigt.")
        if not isinstance(address_id, int):
            raise ValueError("address_id muss ein integer sein.")

        self.__hotel_id: int = hotel_id
        self.__name: str = name
        self.__stars: int = stars
        self.__address_id: int = address_id
        self.__rooms: list[Room] = []

    def __repr__(self):
        return f"Hotel(id={self.__hotel_id!r}, name={self.__name!r}), stars={self.__stars!r}, address={self.__address_id!r}, rooms={self.__rooms!r}"

    @property
    def hotel_id(self) -> int:
        return self.__hotel_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name:
            raise ValueError("name wird benötigt.")
        if not isinstance(name, str):
            raise ValueError("name muss ein string sein.")
        self.__name = name

    @property
    def stars(self) -> int:
        return self.__stars

    @stars.setter
    def stars(self, stars: int) -> None:
        if stars is None:
            raise ValueError("stars wird benötigt.")
        if not isinstance(stars, int):
            raise ValueError("stars muss integer sein.")
        if not (1 <= stars <= 5):
            raise ValueError("stars muss zwischen 1 und 5 sein.")
        self.__stars = stars

    @property
    def address_id(self) -> int:
        return self.__address_id

    @address_id.setter
    def address_id(self, address_id: int) -> None:
        if not address_id:
            raise ValueError("address_id wird benötigt.")
        if not isinstance(address_id, int):
            raise ValueError("address_id muss integer sein.")
        self.__address_id = address_id

    @property
    def rooms(self) -> list:
        return self.__rooms

    @rooms.setter
    def rooms(self, new_rooms: list):
        if not isinstance(new_rooms, list):
            raise ValueError("rooms muss eine Liste sein.")
        self.__rooms = new_rooms

    def add_room(self, room: Room) -> None:
        from model import Room

        if not room:
            raise ValueError("room is required.")
        if not self._is_room(room):
            raise ValueError("room must be a Room instance.")
        if room not in self.__rooms:
            self.__rooms.append(room)

    def remove_room(self, room: Room) -> None:
        if not room:
            raise ValueError("room is required.")
        if not self._is_room(room):
            raise ValueError("room must be a Room instance.")
        if room in self.__rooms:
            self.__rooms.remove(room)

    def _is_room(self, obj) -> bool:
        try:
            from model.room import Room
            return isinstance(obj, Room)
        except ImportError:
            return obj.__class__.__name__ == 'Room'


from __future__ import annotations
from typing import TYPE_CHECKING

class HotelReview:
    def __init__(self, review_id = None, guest_id = None, hotel_id = None, booking_id = None, rating = None, comment = None, review_date = None):
        self.review_id = review_id
        self.guest_id = guest_id
        self.hotel_id = hotel_id
        self.booking_id = booking_id
        self.rating = rating
        self.comment = comment
        self.review_date = review_date

from typing import Optional

class Invoice:
    def __init__(self, invoice_id: Optional[int], booking_id: int, issue_date: str, total_amount: float):
        if invoice_id is not None and invoice_id <= 0:
            raise ValueError("invoice_id must be positive or None")
        if not issue_date:
            raise ValueError("issue_date must not be empty")

        self.__invoice_id = invoice_id
        self.__booking_id = booking_id
        self.__issue_date = issue_date
        self.__total_amount = total_amount

    @property
    def invoice_id(self) -> Optional[int]:
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



from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.hotel import Hotel
    from model.room_type import Room_Type
    from model.facilities import Facilities

class Room:
    def __init__(self, room_id: int, hotel: Hotel, room_number: str, room_type: Room_Type, price_per_night: float):
        if room_id is not None and not isinstance(room_id, int):
            raise ValueError("room_id muss integer sein.")
        if not room_number:
            raise ValueError("room_number wird benötigt.")
        if not isinstance(room_number, str):
            raise ValueError("room_number muss string sein.")
        if not price_per_night:
            raise ValueError("price_per_night wird benötigt.")
        if not isinstance(price_per_night, float):
            raise ValueError("price_per_night muss float sein.")
        if not room_type:
            raise ValueError("room_type wird benötigt.")
        if not self._is_room_type(room_type):
            raise ValueError("room_type muss Room_Type Instanz sein.")

        self.__room_id: int = room_id
        self.__room_number: str = room_number
        self.__hotel: Hotel = hotel
        self.__price_per_night: float = price_per_night
        self.__room_type: Room_Type = room_type
        self.__facilities: list[Facilities] = []

        if hotel is not None:
            hotel.add_room(self)

    def _is_room_type(self, obj) -> bool:
        try:
            from model.room_type import Room_Type
            return isinstance(obj, Room_Type)
        except ImportError:
            return obj.__class__.__name__ == 'Room_Type'

    def _is_facilities(self, obj) -> bool:
        try:
            from model.facilities import Facilities
            return isinstance(obj, Facilities)
        except ImportError:
            return obj.__class__.__name__ == 'Facilities'

    def __repr__(self):
        return f"Room(id={self.__room_id!r}, room_number={self.__room_number!r}, hotel={self.__hotel!r})"

    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def room_number(self) -> str:
        return self.__room_number

    @room_number.setter
    def room_number(self, room_number: str) -> None:
        if not room_number:
            raise ValueError("room_number wird benötigt.")
        if not isinstance(room_number, str):
            raise ValueError("room_number muss string sein.")
        self.__room_number = room_number

    @property
    def price_per_night(self) -> float:
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, price_per_night: float) -> None:
        if not price_per_night:
            raise ValueError("price_per_night wird benötigt.")
        if not isinstance(price_per_night, float):
            raise ValueError("price_per_night muss float sein.")
        self.__price_per_night = price_per_night

    @property
    def room_type(self) -> Room_Type:
        return self.__room_type

    @room_type.setter
    def room_type(self, room_type: Room_Type) -> None:
        if not room_type:
            raise ValueError("room_type wird benötigt.")
        if not self._is_room_type(room_type):
            raise ValueError("room_type muss Room_Type Instanz sein.")
        self.__room_type = room_type

    @property
    def hotel(self) -> Hotel:
        return self.__hotel

    @property
    def hotel_id(self) -> int:
        return self.__hotel.hotel_id if self.__hotel else None

    @hotel.setter
    def hotel(self, hotel: Hotel) -> None:
        if hotel is not None and not self._is_hotel(hotel):
            raise ValueError("hotel muss Hotel Instanz sein.")
        if self.__hotel is not hotel:
            if self.__hotel is not None:
                self.__hotel.remove_room(self)
            self.__hotel = hotel
            if hotel is not None:
                hotel.add_room(self)

    def _is_hotel(self, obj) -> bool:
        try:
            from model.hotel import Hotel
            return isinstance(obj, Hotel)
        except ImportError:
            return obj.__class__.__name__ == 'Hotel'

    @property
    def facilities(self) -> list[Facilities]:
        return self.__facilities.copy()

    def add_room_facilities(self, facilities: Facilities) -> None:
        if not facilities:
            raise ValueError("facilities wird benötigt.")
        if not self._is_facilities(facilities):
            raise ValueError("facilities muss Facilities Instanz sein.")
        if facilities not in self.__facilities:
            self.__facilities.append(facilities)
            if hasattr(facilities, 'room'):
                facilities.room = self

    def remove_room_facilities(self, facilities: Facilities) -> None:
        if not facilities:
            raise ValueError("room_facilities wird benötigt.")
        if not self._is_facilities(facilities):
            raise ValueError("room_facilities muss Facilities Instanz sein.")
        if facilities in self.__facilities:
            self.__facilities.remove(facilities)
            if hasattr(facilities, 'room'):
                facilities.room = None


class Room_Type:

    def __init__(self, type_id: int, description: str, max_guests: int):
        if type_id is None:
            raise ValueError("type_id wird benötigt.")
        if not isinstance(type_id, int):
            raise TypeError("type_id muss ein integer sein.")
        if not description:
            raise ValueError("Description wird benötigt.")
        if not isinstance(description, str):
            raise TypeError("Description muss string sein.")
        if max_guests is None:
            raise ValueError("max_guests wird benötigt.")
        if not isinstance(max_guests, int):
            raise TypeError("max_guests muss integer sein.")
        if max_guests < 0:
            raise ValueError("max_guests kann nicht negativ sein.")

        self.__type_id = type_id
        self.__description = description  # z.B. Einzelzimmer
        self.__max_guests = max_guests

    @property
    def type_id(self):
        return self.__type_id

    @type_id.setter
    def type_id(self, new_type_id):
        self.__type_id = new_type_id

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def max_guests(self):
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, max_guests: int) -> None:
        if max_guests is None:
            raise ValueError("max_guests wird benötigt.")
        if not isinstance(max_guests, int):
            raise TypeError("max_guests muss integer sein.")
        if max_guests < 0:
            raise ValueError("max_guests kann nicht negativ sein.")
        self.__max_guests = max_guests



---------------------------------------------------------------------------------
from datetime import date, datetime
import sqlite3

from .base_dal import BaseDataAccess
from .address_dal import AddressDataAccess
from .booking_dal import BookingDataAccess
from .facilities_dal import FacilityDataAccess
from .guest_dal import GuestDataAccess
from .hotel_dal import HotelDataAccess
from .invoice_dal import InvoiceDataAccess
from .room_dal import RoomDataAccess
from .room_type_dal import RoomTypeDataAccess
from .room_facilities_dal import RoomFacilitiesDataAccess
from .hotel_review_dal import HotelReviewDataAccess


from data_access.base_dal import BaseDataAccess
import model.address

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_address(self, address: model.Address) -> model.Address:
        sql = """
        INSERT INTO Address (street, city, zip_code) VALUES (?, ?, ?)
        """
        params = (address.street, address.city, address.zip_code)

        last_row_id, row_count = self.execute(sql, params)
        return model.Address(last_row_id, address.street, address.city, address.zip_code)

    def read_address_by_id(self, address_id: int) -> model.Address | None:
        sql = """
        SELECT address_id, street, city, zip_code FROM Address WHERE address_id = ?
        """
        params = (address_id,)
        result = self.fetchone(sql, params)

        if result:
            address_id, street, city, zip_code = result
            return model.Address(address_id, street, city, zip_code)
        return None

    def read_address_by_city(self, city: str) -> list[model.Address]:
        if city is None:
            raise ValueError("city cannot be None")

        sql = """
        SELECT address_id, street, city, zip_code FROM Address WHERE city = ?
        """
        params = (city,)
        results = self.fetchall(sql, params)

        return [
            model.Address(address_id, street, city, zip_code)
            for address_id, street, city, zip_code in results
        ]

    def update_address(self, address: model.Address) -> None:
        if address is None:
            raise ValueError("Address kann nicht leer sein.")

        sql = """
              UPDATE Address SET street   = ?, city     = ?, zip_code = ? WHERE address_id = ? 
              """
        params = (address.street, address.city, address.zip_code, address.address_id)
        last_row_id, row_count = self.execute(sql, params)

    def get_address_by_fields(self, street: str, city: str, zip_code: str) -> model.Address | None:
        sql = """
        SELECT address_id, street, city, zip_code FROM Address
        WHERE street = ? AND city = ? AND zip_code = ?
        """
        params = (street, city, zip_code)
        row = self.fetchone(sql, params)

        return model.Address(*row) if row else None
import os
import sqlite3


class BaseDataAccess:
    def __init__(self, db_connection_str: str = None):
        if db_connection_str is None:
            self.__db_connection_str = os.environ.get("DB_FILE")
            if self.__db_connection_str is None:
                raise Exception("DB_FILE environment variable and parameter path is not set.")
        else:
            self.__db_connection_str = db_connection_str

    def _connect(self):
        return sqlite3.connect(self.__db_connection_str, detect_types=sqlite3.PARSE_DECLTYPES)

    def fetchone(self, sql: str, params: tuple | None = ()):
        with self._connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                result = cur.fetchone()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            finally:
                cur.close()
        return result

    def fetchall(self, sql: str, params: tuple | None = ()) -> list:
        with self._connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                result = cur.fetchall()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            finally:
                cur.close()
        return result

    def execute(self, sql: str, params: tuple | None = ()) -> (int, int):
        with self._connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            else:
                conn.commit()
            finally:
                cur.close()
        return cur.lastrowid, cur.rowcount

import sqlite3
from model.booking import Booking
from typing import Optional, List
from model.room import Room
from model.booking import Booking


from data_access.base_dal import BaseDataAccess


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_booking( self, booking: model.Booking) -> model.Booking:
        if booking is None:
            raise ValueError("booking ist erforderlich")
        if booking.guest_id is None:
            raise ValueError("guest_id ist erforderlich")
        if booking.room_id is None:
            raise ValueError("room_id ist erforderlich")
        if booking.check_in_date is None:
            raise ValueError("check_in_date ist erforderlich")
        if booking.check_out_date is None:
            raise ValueError("check_out_date ist erforderlich")
        if booking.is_cancelled is None:
            raise ValueError("is_cancelled ist erforderlich")
        if booking.total_amount is None:
            raise ValueError("total_amount ist erforderlich")

        sql = """
        INSERT INTO Booking (
            guest_id,
            room_id,
            check_in_date,
            check_out_date,
            is_cancelled,
            total_amount
            )
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (
            booking.guest_id,
            booking.room_id,
            booking.check_in_date,
            booking.check_out_date,
            booking.is_cancelled,
            booking.total_amount
        )

        last_row_id, row_count = self.execute(sql, params)

        return model.Booking(
            booking_id=last_row_id,
            guest_id=booking.guest_id,
            room_id=booking.room_id,
            check_in_date=booking.check_in_date,
            check_out_date=booking.check_out_date,
            is_cancelled=booking.is_cancelled,
            total_amount=booking.total_amount
        )

    def read_booking_by_id(self, booking_id: int) -> model.Booking | None:
        if booking_id is None:
            raise ValueError("booking_id ist erforderlich")

        sql = """
        SELECT 
            booking_id,
            guest_id,
            room_id,
            check_in_date,
            check_out_date,
            is_cancelled,
            total_amount
        FROM Booking
        WHERE booking_id = ?
        """
        params = (booking_id,)
        result = self.fetchone(sql, params)
        if result:
            (
                booking_id,
                guest_id,
                room_id,
                check_in_date,
                check_out_date,
                is_cancelled,
                total_amount
            ) = result
            return model.Booking(
                booking_id=booking_id,
                guest_id=guest_id,
                room_id=room_id,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                is_cancelled=bool(is_cancelled),  # Konvertierung zu boolean
                total_amount=total_amount
            )
        else:
            return None

    def read_booking_by_guest_id(self, guest_id: int) -> list[model.Booking]:
        if guest_id is None:
            raise ValueError("guest_id ist erforderlich")

        sql = """
        SELECT 
            booking_id,
            guest_id,
            room_id,
            check_in_date,
            check_out_date,
            is_cancelled,
            total_amount
        FROM Booking WHERE guest_id = ?
        """
        params = (guest_id,)
        bookings = self.fetchall(sql, params)

        return [
            model.Booking(
                booking_id,
                guest_id,
                room_id,
                check_in_date,
                check_out_date,
                is_cancelled,
                total_amount
            )
            for (
                booking_id,
                guest_id,
                room_id,
                check_in_date,
                check_out_date,
                is_cancelled,
                total_amount
            )
            in bookings
        ]

    def read_booking_by_room_id(self, room_id: int) -> list[model.Booking]:
        if room_id is None:
            raise ValueError("room_id ist erforderlich")

        sql = """
        SELECT 
            booking_id,
            guest_id,
            room_id,
            check_in_date,
            check_out_date,
            is_cancelled,
            total_amount
        FROM Booking WHERE room_id = ?
        """
        params = (room_id,)
        bookings = self.fetchall(sql, params)

        return [
            model.Booking(
                booking_id,
                guest_id,
                room_id,
                check_in_date,
                check_out_date,
                is_cancelled,
                total_amount
            )
            for (
                booking_id,
                guest_id,
                room_id,
                check_in_date,
                check_out_date,
                is_cancelled,
                total_amount
            )
            in bookings
        ]

    def read_all_bookings(self) -> list[Booking]:
        sql = """
            SELECT booking_id, check_in_date, check_out_date, is_cancelled, total_amount, guest_id, room_id
            FROM Booking
        """
        rows = self.fetchall(sql)

        return [
            Booking(
                booking_id=row[0],
                check_in_date=row[1],
                check_out_date=row[2],
                is_cancelled=bool(row[3]),
                total_amount=row[4],
                guest_id=row[5],
                room_id=row[6]
            )
            for row in rows
        ]

    def find_available_room(self, room_type_description: str, check_in: str, check_out: str) -> Optional[Room]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        query = """
        SELECT r.room_id, r.type_id, r.hotel_id, rt.description, rt.max_guests
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE rt.description = ?
        AND r.room_id NOT IN (
            SELECT room_id FROM Booking
            WHERE NOT (
                check_out_date <= ? OR check_in_date >= ?
            )
        )
        LIMIT 1
        """

        params = (room_type_description, check_in, check_out)
        cursor.execute(query, params)
        row = cursor.fetchone()

        conn.close()

        if row:
            return Room(
                room_id=row[0],
                room_type_id=row[1],
                hotel_id=row[2],
                room_type_description=row[3],
                max_guests=row[4],
                price_per_night=0  # Fill as needed
            )
        return None

    def cancel_booking_by_id(self, booking_id: int) -> bool:


        sql = """
        UPDATE Booking 
        SET is_cancelled = 1 
        WHERE booking_id = ?
        """
        params = (booking_id,)
        last_row_id, row_count = self.execute(sql, params)

        return row_count > 0

    from __future__ import annotations

    import model
    from data_access.base_dal import BaseDataAccess
    from typing import Optional

    class FacilityDataAccess(BaseDataAccess):
        def __init__(self, db_path: str = None):
            super().__init__(db_path)

        def create_new_facility(self, facility_id: int, facility_name: str) -> model.Facilities:
            # if facility_id is None:
            # raise ValueError("Facility ID wird benötigt") -> sollte nicht passieren da autoincrement
            if not facility_name:
                raise ValueError("Facility name wird benötigt")

            sql = """
                  INSERT INTO Facilities (facility_id, facility_name)
                  VALUES (?, ?) \
                  """
            params = (facility_id, facility_name)

            self.execute(sql, params)

            return model.Facilities(facility_id=facility_id, facility_name=facility_name)

        def read_facility_by_id(self, facility_id: int) -> Optional[model.Facilities]:
            if facility_id is None:
                raise ValueError("Facility ID wird benötigt")

            sql = """
            SELECT facility_id, facility_name
            FROM Facilities
            WHERE facility_id = ?
            """
            result = self.fetchone(sql, (facility_id,))
            if result:
                (facility_id, facility_name) = result
                return model.Facilities(facility_id=facility_id, facility_name=facility_name)
            else:
                return None

        def read_all_facilities(self) -> list[model.Facilities]:
            sql = """
                  SELECT facility_id, facility_name
                  FROM Facilities \
                  """
            results = self.fetchall(sql)

            return [
                model.Facilities(facility_id=facility_id, facility_name=facility_name)
                for facility_id, facility_name in results
            ]

        def update_facility(self, facility_id: int, facility_name: str) -> model.Facilities:
            if facility_id is None:
                raise ValueError("Facility ID wird benötigt")

            sql = """
            UPDATE Facilities \
            SET facility_name = ?
            WHERE facility_id = ?
            """
            params = (facility_name, facility_id)
            self.execute(sql, params)

        def delete_facility(self, facility_id: int):
            if facility_id is None:
                raise ValueError("Facility ID wird benötigt")

            sql = """
                  DELETE \
                  FROM Facilities \
                  WHERE facility_id = ? \
                  """
            self.execute(sql, (facility_id,)

            import model
            from data_access.base_dal import BaseDataAccess
            from typing import Optional

            class GuestDataAccess(BaseDataAccess):
                def __init__(self, db_path: str = None):
                    super().__init__(db_path)

                def create_guest(self, guest: model.Guest):
                    sql = """
                    INSERT INTO Guest(guest_id, first_name, last_name, email, address_id) VALUES (?, ?, ?, ?, ?) 
                    """
                    params = (
                    guest.guest_id if guest else None, guest.first_name, guest.last_name, guest.email, guest.address_id)
                    self.execute(sql, params)

                def read_guest_by_id(self, guest_id: int) -> Optional[model.Guest]:
                    sql = "SELECT guest_id, first_name, last_name, email, address_id FROM Guest WHERE guest_id = ?"
                    result = self.fetchone(sql, (guest_id,))
                    if result:
                        return model.Guest(*result)
                    else:
                        return None

                def update_guest(self, guest: model.Guest):
                    sql = """
                    UPDATE Guest SET first_name = ?, last_name = ?, email = ?, address_id = ? WHERE guest_id = ?
                    """
                    params = (guest.first_name, guest.last_name, guest.email, guest.address_id, guest.guest_id)
                    self.execute(sql, params)

                def delete_guest(self, guest: model.Guest):
                    sql = """
                    DELETE FROM Guest WHERE guest_id = ?
                    """
                    params = (guest.guest_id,)
                    self.execute(sql, params)
                    _, rowcount = self.execute(sql, params)
                    if rowcount == 0:
                        raise LookupError(f"No guest found with id {guest.guest_id}")

                def read_all_guests(self) -> list[model.Guest]:
                    sql = """SELECT guest_id, first_name, last_name, email, address_id FROM Guest"""
                    results = self.fetchall(sql)
                    return [model.Guest(*row) for row in results]
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
              ORDER BY h.hotel_id, r.room_id, b.booking_id
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
                    room = model.Room(room_id=room_id, hotel=hotel, room_number=room_number,
                                      room_type=room_type, price_per_night=price_per_night)
                    room.bookings = []
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

from tkinter.constants import INSERT

import model
from data_access.base_dal import BaseDataAccess
from model.hotel_review import HotelReview


class HotelReviewDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_hotel_review(self, hotel_review: HotelReview):
        if hotel_review is None:
            raise ValueError("Hotel Review wird benötigt.")

        sql = """
              INSERT INTO Hotel_Review (guest_id, hotel_id, booking_id, rating, comment, review_date)
              VALUES (?, ?, ?, ?, ?, ?)
              """
        params = (hotel_review.guest_id, hotel_review.hotel_id, hotel_review.booking_id, hotel_review.rating, hotel_review.comment, hotel_review.review_date)

        last_row_id, _ = self.execute(sql, params)
        hotel_review.review_id = last_row_id
        return hotel_review

    def read_reviews_by_hotel_id(self, hotel_id: int) -> list[HotelReview]:
        sql = """
              SELECT review_id, guest_id, hotel_id, booking_id, rating, comment, review_date
              FROM Hotel_Review
              WHERE hotel_id = ?
              ORDER BY review_date DESC 
              """
        results = self.fetchall(sql, (hotel_id,))
        return [HotelReview(*row) for row in result

import model
from data_access.base_dal import BaseDataAccess
from typing import Optional, List

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def _row_to_invoice(self, row) -> Optional[model.Invoice]:
        if row is None:
            return None
        invoice_id, booking_id, issue_date, total_amount = row
        return model.Invoice(invoice_id, booking_id, issue_date, total_amount)

    def create_invoice(self, invoice: model.Invoice) -> model.Invoice:
        """Create a new invoice entry in the database."""
        if invoice is None:
            raise ValueError("Invoice is required")

        sql = """
         INSERT INTO Invoice (booking_id, issue_date, total_amount)
         VALUES (?, ?, ?)
         """
        params = (invoice.booking_id, invoice.issue_date, invoice.total_amount)
        invoice_id, _ = self.execute(sql, params)
        invoice._Invoice__invoice_id = invoice_id
        return invoice

    def read_invoice_by_id(self, invoice_id: int) -> Optional[model.Invoice]:
        """Read invoice by its ID."""
        sql = """
        SELECT invoice_id, booking_id, issue_date, total_amount
        FROM Invoice
        WHERE invoice_id = ?
        """
        result = self.fetchone(sql, (invoice_id,))
        return self._row_to_invoice(result)

    def update_invoice(self, invoice: model.Invoice):
        """Update invoice fields issue_date and total_amount by invoice and booking ID."""
        if invoice is None:
            raise ValueError("Invoice object is required")

        sql = """
        UPDATE Invoice SET issue_date = ?, total_amount = ? WHERE invoice_id = ? AND booking_id = ?
        """
        params = (invoice.issue_date, invoice.total_amount, invoice.invoice_id, invoice.booking_id)
        last_row_id, row_count = self.execute(sql, params)
        if row_count == 0:
            raise LookupError(f"No invoice found with id {invoice.invoice_id} and booking_id {invoice.booking_id}")

    def delete_invoice(self, invoice: model.Invoice):
        """Delete invoice by invoice_id and booking_id."""
        if invoice is None:
            raise ValueError("Invoice cannot be None")

        sql = """
        DELETE FROM Invoice WHERE invoice_id = ? AND booking_id = ?
        """
        params = (invoice.invoice_id, invoice.booking_id)
        last_row_id, row_count = self.execute(sql, params)
        if row_count == 0:
            raise LookupError(f"No invoice found with id {invoice.invoice_id} and booking_id {invoice.booking_id}")

    def read_all_invoices(self) -> List[model.Invoice]:
        """Read all invoices from the database."""
        sql = "SELECT invoice_id, booking_id, issue_date, total_amount FROM Invoice"
        results = self.fetchall(sql)
        return [self._row_to_invoice(row) for row in results]

    def read_invoice_by_booking_id(self, booking_id: int) -> Optional[model.Invoice]:
        """Read invoice by associated booking_id."""
        if booking_id is None:
            raise ValueError("booking_id wird benötigt.")

        sql = """
        SELECT invoice_id, booking_id, issue_date, total_amount
        FROM Invoice
        WHERE booking_id = ?
        """
        result = self.fetchone(sql, (booking_id,))
        return self._row_to_invoice(result)

from __future__ import annotations
import model
from data_access.base_dal import BaseDataAccess
from typing import List


class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None): super().__init__(db_path)

    def create_new_room(self, hotel_id: int, room_number: int, type_id: int, price_per_night: float) -> model.Room:
        sql = "INSERT INTO Room(hotel_id, room_number, type_id, price_per_night) VALUES (?, ?, ?, ?)"
        last_row_id, _ = self.execute(sql, (hotel_id, room_number, type_id, price_per_night))
        return model.Room(last_row_id, model.Hotel(hotel_id, "", 0, 0), room_number, model.Room_Type(type_id, "", 0), price_per_night)

    def read_room_by_id(self, room_id: int) -> model.Room | None:
        sql = """
            SELECT r.room_id, r.room_number, r.price_per_night,
                   rt.type_id, rt.description, rt.max_guests,
                   h.hotel_id, h.name, h.address_id, h.stars
            FROM Room r
            JOIN Room_Type rt ON r.type_id = rt.type_id
            JOIN Hotel h ON r.hotel_id = h.hotel_id
            WHERE r.room_id = ?
        """
        result = self.fetchone(sql, (room_id,))
        return model.Room(result[0], model.Hotel(result[6], result[7], result[8], result[9]), result[1], model.Room_Type(result[3], result[4], result[5]), result[2]) if result else None

    def read_rooms_by_hotel(self, hotel: model.Hotel) -> list[model.Room]:
        if hotel is None: raise ValueError("hotel kann nicht leer sein.")
        sql = """
            SELECT r.room_id, r.room_number, r.price_per_night,
                   rt.type_id, rt.description, rt.max_guests,
                   h.hotel_id, h.name, h.address_id, h.stars
            FROM Room r
            JOIN Room_Type rt ON r.type_id = rt.type_id
            JOIN Hotel h ON r.hotel_id = h.hotel_id
            WHERE r.hotel_id = ?
        """
        return [model.Room(row[0], model.Hotel(row[6], row[7], row[8], row[9]), row[1], model.Room_Type(row[3], row[4], row[5]), row[2]) for row in self.fetchall(sql, (hotel.hotel_id,))]

    def read_room_details(self, type_id: int) -> List[model.Room]:
        sql = """
            SELECT r.room_id, r.room_number, r.price_per_night,
                   rt.type_id, rt.description, rt.max_guests,
                   h.hotel_id, h.name, h.address_id, h.stars
            FROM Room r
            JOIN Room_Type rt ON r.type_id = rt.type_id
            JOIN Hotel h ON r.hotel_id = h.hotel_id
            WHERE r.type_id = ?
        """
        return [model.Room(row[0], model.Hotel(row[6], row[7], row[8], row[9]), row[1], model.Room_Type(row[3], row[4], row[5]), row[2]) for row in self.fetchall(sql, (type_id,))]
import model
from data_access.base_dal import BaseDataAccess


class RoomFacilitiesDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_facility_to_room(self, room: model.Room, facilities: model.Facilities):
        sql = """
              INSERT INTO Room_Facilities (room_id, facility_id) VALUES (?, ?)
              """
        params = (room.room_id, facilities.facility_id)
        self.execute(sql, params)

    def delete_facility_from_room(self, room: model.Room, facilities: model.Facilities):
        sql = """
              DELETE FROM Room_Facilities WHERE room_id = ? AND facility_id = ?
              """
        params = (room.room_id, facilities.facility_id)
        self.execute(sql, params)

    def read_facilities_by_room_id(self, room: model.Room):
        sql = """
              SELECT f.facility_id, f.facility_name
              FROM Facilities f
                       JOIN Room_Facilities rf ON f.facility_id = rf.facility_id
              WHERE rf.room_id = ? \
              """
        params = (room.room_id,)
        results = self.fetchall(sql, params)

        facilities = []
        if results:
            for row in results:
                facility_id, facility_name = row
                facilities.append(model.Facilities(facility_id, facility_name))

        return facilities

    def read_rooms_by_facility_id(self, facilities: model.facilities):
        sql = """
              SELECT room.room_id, room.room_number, room.price_per_night FROM Room room JOIN Room_Facilities roomfacilities ON room.room_id = roomfacilities.room_id JOIN Room_Type rt ON room.type_id = rt.type_id
              WHERE roomfacilities.facility_id = ?
              """
        params = (facilities.facility_id,)
        results = self.fetchall(sql, params)

        rooms = []
        if results:
            for row in results:
                room_id, room_number, price_per_night, description = row
                rooms.append(model.Room(room_id, room_number, price_per_night, description))

        return rooms

    def has_facility(self, room: model.room, facilities: model.facilities):
        sql = """
              SELECT COUNT(*) FROM Room_Facilities WHERE room_id = ? AND facility_id = ?
              """
        params = (room.room_id, facilities.facility_id)
        result = self.fetchone(sql, params)

        return result[0] > 0 if result else False

    def delete_room_facilities(self, room: model.Room):
        sql = """
              DELETE FROM Room_Facilities WHERE room_id = ?
              """
        params = (room.room_id,)
        self.execute(sql, param

import model

from data_access.base_dal import BaseDataAccess
from typing import Optional

class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_room_type(self, type_id: int, description: str, max_guests: int) -> model.Room_Type:
        #if type_id is None:
           # raise ValueError("Room type ID wird benötigt") -> sollte nicht passieren da autoincrement
        if not description:
            raise ValueError("Room type description wird benötigt")
        if max_guests is None:
            raise ValueError("Max guests wird benötigt")

        sql = """
        INSERT INTO Room_Type (type_id, description, max_guests)
        VALUES (?, ?, ?)
        """
        params = (type_id, description, max_guests)
        self.execute(sql, params)

        return model.Room_Type(type_id=type_id, description=description, max_guests=max_guests)

    def read_room_type_by_id(self, type_id: int) -> Optional[model.Room_Type]:
        if type_id is None:
            raise ValueError("Room type ID wird benötigt")

        sql = """
        SELECT type_id, description, max_guests
        FROM Room_Type
        WHERE type_id = ?
        """
        result = self.fetchone(sql, (type_id,))
        if result:
            type_id, description, max_guests = result
            return model.Room_Type(type_id=type_id, description=description, max_guests=max_guests)
        else:
            return None

    def read_all_room_types(self) -> list[model.Room_Type]:
        sql = """
        SELECT type_id, description, max_guests
        FROM Room_Type
        """
        results = self.fetchall(sql)

        return [
            model.Room_Type(type_id=type_id, description=description, max_guests=max_guests)
            for type_id, description, max_guests in results
        ]

    def update_room_type(self, type_id: int, description: str, max_guests: int):
        if type_id is None:
           raise ValueError("Room type ID wird benötigt")
        sql = """
        UPDATE Room_Type
        SET description = ?, max_guests = ?
        WHERE type_id = ?
        """
        params = (description, max_guests, type_id)
        self.execute(sql, params)

    def delete_room_type(self, type_id: int):
        if type_id is None:
            raise ValueError("Room type ID wird benötigt")

        sql = """
        DELETE FROM Room_Type
        WHERE type_id = ?
        """
        self.execute(sql, (type_id,))


------------------------------------------------------------------------------------

from .booking_manager import BookingManager
from .facilities_manager import FacilitiesManager
from .guest_manager import GuestManager
from .hotel_manager import HotelManager
from .invoice_manager import InvoiceManager
from .room_facilities_manager import RoomFacilitiesManager
from .room_manager import RoomManager
from .room_type_manager import RoomTypeManager
from business_logic.address_manager import AddressManager
from .hotel_review_manager import HotelReviewManager
###

from data_access.address_dal import AddressDataAccess
from model.address import Address

class AddressManager:
    def __init__(self):
        self.dal = AddressDataAccess("database/hotel_reservation_sample.db")

    def create_address(self, address: Address):
        self.dal.create_new_address(address)
        return address
from data_access.booking_dal import BookingDataAccess
from model.room import Room
from model.booking import Booking
from typing import Optional, List
from datetime import datetime


class BookingManager:
    def __init__(self, db_path: str = None):
        self.__dal = BookingDataAccess(db_path)

    def create_booking(self, guest_id: int, room_id: int, check_in_date: str, check_out_date: str, price_per_night: float) -> Booking:
        check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
        num_nights = (check_out - check_in).days
        dynamic_price = self.calculate_dynamic_price(price_per_night, check_in_date)
        total_price = num_nights * dynamic_price

        booking = Booking(
            booking_id=None,
            guest_id=guest_id,
            room_id=room_id,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            is_cancelled=False,
            total_amount=total_price
        )

        return self.__dal.create_booking(booking)

    def calculate_dynamic_price(self, base_price: float, check_in: str) -> float:
        month = check_in.month
        if month in [6, 7, 8, 12]:
            return base_price * 1.3  # Hochsaison
        elif month in [1, 2, 3, 11]:
            return base_price * 0.9  # Nebensaison
        else:
            return base_price

    def read_booking_by_id(self, booking_id: int) -> Optional[Booking]:
        return self.__dal.read_booking_by_id(booking_id)

    def read_all_bookings(self) -> List[Booking]:
        return self.__dal.read_all_bookings()

    def update_booking(self, booking: Booking):
        self.__dal.update_booking(booking)

    def delete_booking(self, booking: Booking):
        self.__dal.delete_booking(booking)

    def cancel_booking(self, booking_id: int):
        booking = self.__dal.read_booking_by_id(booking_id)
        if booking is None:
            raise ValueError("Booking not found.")
        was_cancelled = self.__dal.cancel_booking_by_id(booking_id)

        if not was_cancelled:
            raise ValueError("Booking could not be cancelled.")

        booking.is_cancelled = True
        return booking

    def find_available_room(self, room_type_description: str, check_in: str, check_out: str) -> Optional[Room]:
        return self.__dal.find_available_room(room_type_description, check_in, check_out)

from typing import Optional
from data_access.facilities_dal import FacilityDataAccess
import model


class FacilitiesManager:
    def __init__(self, facilities_dal: FacilityDataAccess):
        self._dal = facilities_dal

    def create_facility(self, facility_id: int, facility_name: str) -> model.Facilities:
        if not facility_name:
            raise ValueError("Facility name wird benötigt")
        return self._dal.create_new_facility(facility_id, facility_name)

    def get_facility_by_id(self, facility_id: int) -> Optional[model.Facilities]:
        return self._dal.read_facility_by_id(facility_id)

    def get_all_facilities(self) -> list[model.Facilities]:
        return self._dal.read_all_facilities()

    def update_facility(self, facility_id: int, facility_name: str):
        if not facility_name:
            raise ValueError("Facility name wird benötigt")
        self._dal.update_facility(facility_id, facility_name)

    def delete_facility(self, facility_id: int):
        self._dal.delete_facility(facility_id)

    def facility_exists(self, facility_id: int) -> bool:
        return self._dal.read_facility_by_id(facility_id) is not None

    def is_name_unique(self, facility_name: str) -> bool:
        all_facilities = self.get_all_facilities()
        return all(f.facility_name != facility_name for f in all_facilities)

    from data_access.guest_dal import GuestDataAccess
    from business_logic.address_manager import AddressManager
    from model.address import Address
    from model.guest import Guest
    from typing import Optional, List

    class GuestManager:
        def __init__(self, db_path: str = None):
            self.__dal = GuestDataAccess(db_path)

        def create_guest(self, first_name: str, last_name: str, email: str, address_id: int) -> Guest:
            guest = Guest(None, first_name, last_name, email, address_id)
            return self.__dal.create_guest(guest)

        def get_guest_by_id(self, guest_id: int) -> Optional[Guest]:
            return self.__dal.read_guest_by_id(guest_id)

        def get_all_guests(self) -> List[Guest]:
            return self.__dal.read_all_guests()

        def update_guest(self, guest: Guest):
            self.__dal.update_guest(guest)

        def delete_guest(self, guest: Guest):
            self.__dal.delete_guest(guest)
import os
#import pandas as pd
import model
from data_access.hotel_dal import HotelDataAccess

#TODO Code für Projekt ergänzen
### Code gemäss Referenzprojekt
class HotelManager:
    def __init__(self, db_path: str = None):
        self.__hotel_dal = HotelDataAccess(db_path)

    def create_hotel(self, hotel: model.Hotel, address: model.Address, room: model.Room):
        return self.__hotel_dal.create_new_hotel(hotel, address, room)

    def read_hotel(self, hotel_id: int):
        return self.__hotel_dal.read_hotel_by_id(hotel_id)

    def read_all_hotels(self) -> list[model.Hotel]:
        return self.__hotel_dal.read_all_hotels()

    #def read_all_hotels_as_df(self) -> pd.DataFrame:
    #    return self.__hotel_dal.read_all_hotels_as_df()

    def read_hotels_by_similar_name(self, name: str) -> list[model.Hotel]:
        return self.__hotel_dal.read_hotels_like_name(name)

    #def read_hotels_by_similar_name_as_df(self, name: str) -> pd.DataFrame:
    #    return self.__hotel_dal.read_hotels_like_name_as_df(name)

    def update_hotel(self, hotel: model.Hotel) -> None:
        self.__hotel_dal.update_hotel(hotel)

    def delete_hotel(self, hotel: model.Hotel) -> None:
        self.__hotel_dal.delete_hotel(hotel)

    # def search_hotel(self, hotel: model.Hotel) -> list[model.Hotel]:
        #return self.__hotel_dal.search_hotel(hotel)

    def read_all_hotels_extended_info(self):
        return self.__hotel_dal.read_all_hotels_extended_info()


import os
#import pandas as pd
from model.hotel_review import HotelReview
from data_access.hotel_review_dal import HotelReviewDataAccess

class HotelReviewManager:
    def __init__(self, db_path: str = None):
        self.__hotel_review_dal = HotelReviewDataAccess(db_path)

    def create_hotel_review(self, hotel_review: HotelReview):
        return self.__hotel_review_dal.create_hotel_review(hotel_review)


    def read_reviews_by_hotel_id(self, hotel_id: int) -> list[HotelReview]:
        return self.__hotel_review_dal.read_reviews_by_hotel_id(hotel_id)



from data_access.invoice_dal import InvoiceDataAccess
from model.invoice import Invoice
from typing import Optional, List

class InvoiceManager:
    def __init__(self, db_path: str = None):
        self.__dal = InvoiceDataAccess(db_path)

    def create_invoice(self, booking_id: int, issue_date: str, total_amount: float) -> Invoice:
        invoice = Invoice(None, booking_id, issue_date, total_amount)
        return self.__dal.create_invoice(invoice)

    def read_invoice_by_id(self, invoice_id: int) -> Optional[Invoice]:
        return self.__dal.read_invoice_by_id(invoice_id)

    def read_all_invoices(self) -> List[Invoice]:
        return self.__dal.read_all_invoices()

    def update_invoice(self, invoice: Invoice):
        self.__dal.update_invoice(invoice)

    def delete_invoice(self, invoice: Invoice):
        self.__dal.delete_invoice(invoice)

    def cancel_invoice_by_booking(self, booking_id: int):

        invoice = self.__dal.read_invoice_by_booking_id(booking_id)
        if invoice is None:
            raise ValueError("Keine rechnung gefunden.")

        was_cancelled = self.__dal.cancel_invoice_by_booking_id(booking_id)

        if not was_cancelled:
            raise ValueError("Rechnung konnte nicht storniert werden.")

        invoice.total_amount = 0.0
        return invoice

    from data_access.room_facilities_dal import RoomFacilitiesDataAccess
    from model.room import Room
    from model.facilities import Facilities
    from typing import List

    class RoomFacilitiesManager:
        def __init__(self, db_path: str = None):
            self.__dal = RoomFacilitiesDataAccess(db_path)

        def add_facility_to_room(self, room: Room, facility: Facilities):
            self.__dal.create_facility_to_room(room, facility)

        def remove_facility_from_room(self, room: Room, facility: Facilities):
            self.__dal.delete_facility_from_room(room, facility)

        def read_facilities_by_room(self, room: Room) -> List[Facilities]:
            return self.__dal.read_facilities_by_room_id(room)

        def read_rooms_by_facility(self, facility: Facilities) -> List[Room]:
            return self.__dal.read_rooms_by_facility_id(facility)

        def has_facility(self, room: Room, facility: Facilities) -> bool:
            return self.__dal.has_facility(room, facility)

        def delete_facilities_from_room(self, room: Room):
            self.__dal.delete_room_facilities(room)

import os
import model
import data_access
from typing import List

#TODO Code für Projekt ergänzen
### Code gemäss Referenzprojekt
class RoomManager():
    def __init__(self) -> None:
        self.__room_dal = data_access.RoomDataAccess()

    def create_room(self, hotel_id: int, room_number: str, type_id: int, price_per_night: float, hotel: model.Hotel = None) -> model.Room:
        return self.__room_dal.create_room(hotel_id, room_number, type_id, price_per_night, hotel)

    def read_hotels_rooms(self, hotel: model.Hotel) -> None:
        return self.__room_dal.read_rooms_by_hotel(hotel)

    def read_room(self, room_id: int) -> model.Room:
        return self.__room_dal.read_room_by_id(room_id)

    def read_room_details(self, type_id: int) -> List[model.Room]:
        return self.__room_dal.read_room_details(type_id)

import model

from data_access.room_type_dal import RoomTypeDataAccess
from typing import Optional


class RoomTypeManager:
    def __init__(self, room_type_dal: RoomTypeDataAccess):
        self._dal = room_type_dal

    def create_room_type(self, type_id: int, description: str, max_guests: int) -> model.Room_Type:
        if max_guests <= 0:
            raise ValueError("Die Anzahl maximaler Gäste muss grösser als 0 sein")
        return self._dal.create_new_room_type(type_id, description, max_guests)

    def get_room_type_by_id(self, type_id: int) -> Optional[model.Room_Type]:
        return self._dal.read_room_type_by_id(type_id)

    def get_all_room_types(self) -> list[model.Room_Type]:
        return self._dal.read_all_room_types()

    def update_room_type(self, type_id: int, description: str, max_guests: int):
        if max_guests <= 0:
            raise ValueError("Max guests must be greater than zero")
        self._dal.update_room_type(type_id, description, max_guests)

    def delete_room_type(self, type_id: int):
        self._dal.delete_room_type(type_id)

    def is_suitable_for_guests(self, type_id: int, guest_count: int) -> bool:
        room_type = self._dal.read_room_type_by_id(type_id)
        if room_type is None:
            return False
        return guest_count <= room_type.max_guests
