from ui_folder.admin_ui import Admin
from ui_folder.guest_ui import GuestUI

admin_ui = Admin()
guest_ui = GuestUI()

def show_menu(options):
    while True:
        for idx, (desc, _) in enumerate(options, start=1):
            print(f"{idx}. {desc}")
        print("0. Zurück")
        choice = input("Auswahl: ").strip()
        if choice == "0":
            return
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                options[idx][1]()
            else:
                print("Ungültige Auswahl.")
        except ValueError:
            print("Bitte eine Zahl eingeben.")


def guest_menu():
    options = [
        ("Hotels suchen", guest_ui.user_search_hotels_from_data),
        ("Verfügbarkeit prüfen", guest_ui.show_room_type_details_for_selected_hotel),
        ("Buchung inkl. Zahlung", guest_ui.create_booking_and_pay_ui),
        ("Rechnung erstellen", guest_ui.create_invoice_for_guest_ui),
        ("Buchung stornieren", guest_ui.cancel_booking_ui),
        ("Hotel wählen mit Preisinformation", guest_ui.choose_hotel_ui()),
        ("Hotel bewerten", guest_ui.hotel_review_ui),
        ("Hotelbewertungen ansehen", guest_ui.view_hotel_reviews_ui),
    ]
    print("\nGäste-Menü:")
    show_menu(options)


def admin_menu():
    options = [
        ("Hotel erstellen", admin_ui.admin_create_hotel_ui),
        ("Hotel löschen", admin_ui.admin_delete_hotel_ui),
        ("Hotelinformationen aktualisieren", admin_ui.update_hotel_details_ui),
        ("Hotelinformationen aktualisiseren mit Adresse", admin_ui.update_hotel_details_without_address_ui),
        ("Alle Buchungen anzeigen", admin_ui.read_all_bookings_ui),
        ("Zimmer mit Ausstattung anzeigen", admin_ui.show_rooms_with_facilities_by_hotel_ui),
        ("Stammdaten verwalten", admin_ui.admin_main_menu_ui),
        ("Demografische Asuwertung der Gäste", admin_ui.demographics_ui)
    ]
    print("\nAdmin-Menü:")
    show_menu(options)


def main():
    while True:
        print("\nHauptmenü:")
        print("1. Gäste-Funktionen")
        print("2. Admin-Funktionen")
        print("0. Beenden")
        choice = input("Auswahl: ").strip()
        if choice == "1":
            guest_menu()
        elif choice == "2":
            admin_menu()
        elif choice == "0":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl.")


if __name__ == "__main__":
    main()