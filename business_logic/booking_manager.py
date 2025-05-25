from datetime import datetime
from model.booking import Booking


def book_room_in_hotel(bookings, guest, room, check_in_date, check_out_date):
    if isinstance(check_in_date, str):
        check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d")
    if isinstance(check_out_date, str):
        check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d")
    num_nights = (check_out_date - check_in_date).days
    total_price = num_nights * room.price_per_night

    new_booking_id = max([b.booking_id for b in bookings], default=0) + 1

    booking = Booking(
        booking_id=new_booking_id,
        check_in_date=check_in_date,
        check_out_date=check_out_date,
        is_cancelled=False,
        total_amount=total_price,
        guest_id=guest.guest_id,
        room_id=room.room_id
    )

    booking.add_guest(guest)
    booking.add_room(room)
    bookings.append(booking)

    print(f"Buchung erfolgreich für {guest.first_name} im Zimmer {room.room_number} vom {check_in_date.date()} bis {check_out_date.date()}. Preis: {total_price:.2f} CHF")

    return booking


class BookingManager:
    def __init__(self):
        self.bookings = []

    def show_all_bookings(self, guests, rooms):
        print("Aktuelle Buchungen:")
        for b in self.bookings:
            guest = next(g for g in guests if g.guest_id == b.guest_id)
            room = next(r for r in rooms if r.room_id == b.room_id)
            print(f" - Gast: {guest.first_name}, Zimmer: {room.room_number}, Zeitraum: {b.check_in_date.date()} – {b.check_out_date.date()}, Betrag: {b.total_amount:.2f} CHF")
