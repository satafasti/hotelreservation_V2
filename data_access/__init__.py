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

# Adapter: Wandelt `date`-Objekt in `TEXT` um
sqlite3.register_adapter(date, lambda d: d.isoformat())

# Konverter: Wandelt gespeicherte `TEXT`-Werte wieder in `date`
sqlite3.register_converter("DATE", lambda s: datetime.strptime(s.decode(), "%Y-%m-%d").date())
 ## test