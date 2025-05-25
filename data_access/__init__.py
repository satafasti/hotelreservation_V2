from datetime import date, datetime
import sqlite3

from .base_dal import BaseDAL
from .address_dal import AddressDAL
from .booking_dal import BookingDAL
from .facilities_dal import FacilitiesDAL
from .guest_dal import GuestDAL
from .hotel_dal import HotelDAL
from .invoice_dal import InvoiceDAL
from .room_dal import RoomDAL
from .room_type_dal import RoomTypeDAL
from .room_facilities_dal import RoomFacilitiesDAL

# Adapter: Wandelt `date`-Objekt in `TEXT` um
sqlite3.register_adapter(date, lambda d: d.isoformat())

# Konverter: Wandelt gespeicherte `TEXT`-Werte wieder in `date`
sqlite3.register_converter("DATE", lambda s: datetime.strptime(s.decode(), "%Y-%m-%d").date())
