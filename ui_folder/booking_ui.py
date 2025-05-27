from business_logic.invoice_manager import InvoiceManager
from business_logic.booking_manager import BookingManager
from model.guest import Guest
from model.room import Room

def booking_menu():
    while True:
        print("\n--- Buchungsmenü ---")
        print("1) Zimmer buchen")
        print("2) Buchung stornieren")
        print("0) Zurück")

        auswahl = input("Auswahl: ").strip()

        if auswahl == "1":
            create_booking_ui()
        elif auswahl == "2":
            cancel_booking_ui()
        elif auswahl == "0":
            break
        else:
            print("Ungültige Eingabe.")


#4. Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.
#7. Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann. Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an.
from business_logic.booking_manager import BookingManager
from datetime import datetime

def create_booking_ui():
    print("Zimmerbuchung")

    guest_id = int(input("Geben Sie Ihre Gast-ID ein: "))
    room_id = int(input("Geben Sie die gewünschte Zimmer-ID ein: "))
    check_in = input("Check-in-Datum (YYYY-MM-DD): ").strip()
    check_out = input("Check-out-Datum (YYYY-MM-DD): ").strip()
    price_per_night = float(input("Preis pro Nacht des Zimmers: "))

    check_in_dt = datetime.strptime(check_in, "%Y-%m-%d")
    check_out_dt = datetime.strptime(check_out, "%Y-%m-%d")
    num_nights = (check_out_dt - check_in_dt).days

    manager = BookingManager()
    dynamic_price = manager.calculate_dynamic_price(price_per_night, check_in)
    total_price = dynamic_price * num_nights

    print(f"Saisonpreis pro Nacht: {dynamic_price:.2f} CHF")
    print(f"Gesamtpreis für {num_nights} Nächte: {total_price:.2f} CHF")

    confirm = input("Möchten Sie zu diesem Preis buchen? (j/n): ").strip().lower()
    if confirm != "j":
        print("Buchung abgebrochen.")
        return

    try:
        booking = manager.create_booking(guest_id, room_id, check_in, check_out, price_per_night)
        print(f"Buchung erfolgreich!")
        print(f"Buchungs-ID: {booking.booking_id}")
        print(f"Gesamtbetrag (in DB gespeichert): {booking.total_amount:.2f} CHF\n")
    except Exception as e:
        print(f"Fehler bei der Buchung: {e}")


#6. Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hint: Sorgt für die entsprechende Invoice
def cancel_booking_ui():
    print("Buchung stornieren")
    booking_id = int(input("Bitte geben Sie Ihre Buchungs-ID ein: "))

    booking_manager = BookingManager()
    invoice_manager = InvoiceManager()

    try:
        booking_manager.cancel_booking(booking_id)
        invoice_manager.cancel_invoice_by_booking(booking_id)
        print(f"Ihre Buchung {booking_id} wurde erfolgreich storniert und die Rechnung angepasst.\n")
    except ValueError as e:
        print(f"Fehler: {e}\n")

