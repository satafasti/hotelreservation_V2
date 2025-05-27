
from business_logic.booking_manager import BookingManager
from model.guest import Guest
from model.room import Room

#4. Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.
def create_booking_ui():
    print("📅 Zimmerbuchung")

    guest_id = int(input("Geben Sie Ihre Gast-ID ein: "))
    room_id = int(input("Geben Sie die gewünschte Zimmer-ID ein: "))
    check_in = input("Check-in-Datum (YYYY-MM-DD): ").strip()
    check_out = input("Check-out-Datum (YYYY-MM-DD): ").strip()
    price_per_night = float(input("Preis pro Nacht des Zimmers: "))

    manager = BookingManager()
    try:
        booking = manager.create_booking(guest_id, room_id, check_in, check_out, price_per_night)
        print(f"Buchung erfolgreich!")
        print(f"Buchungs-ID: {booking.booking_id}")
        print(f"Gast-ID: {booking.guest_id}")
        print(f"Zimmer-ID: {booking.room_id}")
        print(f"Zeitraum: {check_in} bis {check_out}")
        print(f"Gesamtbetrag: {booking.total_amount:.2f} CHF\n")
    except Exception as e:
        print(f"Fehler bei der Buchung: {e}")
