from data_access.booking_dal import BookingDataAccess
from model.booking import Booking
from datetime import date
from typing import List


class BookingManager:
    def __init__(self, db_path: str = None):
        self.__dal = BookingDataAccess(db_path)

    def create_booking(self, guest_id: int, room_id: int, check_in_date: date, check_out_date: date, price_per_night: float):
        num_nights = (check_out_date - check_in_date).days
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

    def read_all_bookings(self) -> List[Booking]:
        return self.__dal.read_all_bookings()

    def calculate_dynamic_price(self, base_price: float, check_in: date) -> float:
        month = check_in.month
        if month in [6, 7, 8, 12]:
            return base_price * 1.3  # Hochsaison
        elif month in [1, 2, 3, 11]:
            return base_price * 0.9  # Nebensaison
        else:
            return base_price


    def cancel_booking(self, booking_id: int):
        booking = self.__dal.read_booking_by_id(booking_id)
        if booking is None:
            raise ValueError("Booking not found.")
        was_cancelled = self.__dal.cancel_booking_by_id(booking_id)

        if not was_cancelled:
            raise ValueError("Booking could not be cancelled.")

        booking.is_cancelled = True
        return booking

    def get_checkin_date_if_missing(self):
        print(
            "Damit Ihnen die aktuellen Preise mit Saison-Aufschlägen angezeigt werden, geben Sie bitte ein Check-in Datum ein.")
        check_in_input = input("Gewünschtes Check-in Datum (YYYY-MM-DD) oder Enter für Basispreise: ").strip()
        if check_in_input:
            try:
                from datetime import datetime
                check_in = datetime.strptime(check_in_input, "%Y-%m-%d").date()
                print(f"Check-in Datum gesetzt: {check_in.strftime('%d.%m.%Y')}")
                return check_in
            except ValueError:
                print("Ungültiges Datumsformat. Basispreise werden angezeigt.")
                return None
        else:
            print("Kein Datum eingegeben. Basispreise werden angezeigt.")
            return None

    def get_checkout_date_if_missing(self):
        print("Bitte geben Sie bitte ein Check-Out Datum ein.")
        check_out_input = input("Gewünschtes Check-Out Datum (YYYY-MM-DD) oder Enter für Basispreise: ").strip()
        if check_out_input:
            try:
                from datetime import datetime
                check_out = datetime.strptime(check_out_input, "%Y-%m-%d").date()
                print(f"Check-Out Datum gesetzt: {check_out.strftime('%d.%m.%Y')}")
                return check_out
            except ValueError:
                print("Ungültiges Datumsformat. Basispreise werden angezeigt.")
                return None
        else:
            print("Kein Datum eingegeben. Basispreise werden angezeigt.")
            return None

    def show_total_pricing_summary(self, price_summary):
        if not price_summary or not price_summary['total_days']:
            return

        days = price_summary['total_days']
        print(f"\nPreisübersicht:")
        print(f"Günstigstes Zimmer: {price_summary['min_total']:.2f} CHF")
        if price_summary['min_total'] != price_summary['max_total']:
            print(f"Teuerstes Zimmer: {price_summary['max_total']:.2f} CHF")
        print(f"Preisspanne pro Nacht: {price_summary['min_price']:.2f} - {price_summary['max_price']:.2f} CHF")




#Im Projekt wurde zwar im BookingManager ein ganzer Satz von Methoden definiert – darunter read_booking_by_id, read_all_bookings, update_booking, delete_booking und find_available_room.
#Allerdings greifen die übrigen Komponenten des Systems nicht auf diese Manager-Methoden zu.

#Beispielsweise nutzt die admin_ui in der Funktion read_all_bookings_ui direkt den BookingDataAccess, ohne den BookingManager zu verwenden.
#Ähnlich verhält es sich beim InvoiceManager, der Buchungen direkt über den BookingDataAccess lädt, wenn eine Rechnung erstellt werden soll.

#In der README wird zudem erläutert, dass beim „Neustart“ des Repositories viele ehemals geschriebene Codeblöcke nicht weiterverwendet wurden. Aus Zeitgründen wurden diese nur auskommentiert oder nicht mehr angerührt, damit nichts versehentlich gelöscht wird.
#Die genannten Funktionen im BookingManager waren für die implementierten User Stories letztlich überflüssig und blieben daher ungenutzt.

   #def find_available_room(self, room_type_description: str, check_in: str, check_out: str) -> Optional[Room]:
        #return self.__dal.find_available_room(room_type_description, check_in, check_out)

    #def read_booking_by_id(self, booking_id: int) -> Optional[Booking]:
        #return self.__dal.read_booking_by_id(booking_id)

    #def update_booking(self, booking: Booking):
        #self.__dal.update_booking(Booking)

    #def delete_booking(self, booking: Booking):
        #self.__dal.delete_booking(Booking)

