from business_logic.address_manager import AddressManager
from business_logic.booking_manager import BookingManager
from business_logic.facilities_manager import FacilitiesManager
from business_logic.guest_manager import GuestManager
from business_logic.hotel_manager import HotelManager
from business_logic.invoice_manager import InvoiceManager
from business_logic.room_facilities_manager import RoomFacilitiesManager
from business_logic.room_manager import RoomManager
from business_logic.room_type_manager import RoomTypeManager
from business_logic.hotel_review_manager import HotelReviewManager

from data_access.base_dal import BaseDataAccess
from data_access.address_dal import AddressDataAccess
from data_access.booking_dal import BookingDataAccess
from data_access.facilities_dal import FacilityDataAccess
from data_access.guest_dal import GuestDataAccess
from data_access.hotel_dal import HotelDataAccess
from data_access.invoice_dal import InvoiceDataAccess
from data_access.room_dal import RoomDataAccess
from data_access.room_type_dal import RoomTypeDataAccess
from data_access.room_facilities_dal import RoomFacilitiesDataAccess
from data_access.hotel_review_dal import HotelReviewDataAccess

from model.address import Address
from model.booking import Booking
from model.facilities import Facilities
from model.guest import Guest
from model.hotel import Hotel
from model.invoice import Invoice
from model.room import Room
from model.room_type import Room_Type
from model.hotel_review import HotelReview

# 1. Als Gast möchte ich die verfügbaren Hotels durchsuchen, damit ich dasjenige auswählen kann, welches meinen Wünschen entspricht. Wünsche sind:
# 1.1. Ich möchte alle Hotels in einer Stadt durchsuchen, damit ich das Hotel nach meinem bevorzugten Standort (Stadt) auswählen kann.
# 1.2. Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.
# 1.3. Ich möchte alle Hotels in einer Stadt durchsuchen, die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung).
# 123
# 1.4. Ich möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes ("von" (check_in_date) und "bis" (check_out_date)) Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe.
# 1.5. Ich möchte Wünsche kombinieren können, z.B. die verfügbaren Zimmer zusammen mit meiner Gästezahl und der mindest Anzahl Sterne.
# 1.6. Ich möchte die folgenden Informationen pro Hotel sehen: Name, Adresse, Anzahl der Sterne.

# Funktioniert

def user_search_hotels_from_data():
    from datetime import datetime
    from business_logic.hotel_manager import HotelManager
    import copy

    print("Hotel-Suche: Geben Sie beliebige Kriterien ein (leere Eingaben werden für die Suche nicht berücksichtigt):\n")

    city = input("Stadt: ").strip()
    stars = input("Mindestanzahl Sterne (1-5): ").strip()
    guests = input("Mindestens wie viele Gäste sollen im Zimmer Platz haben?: ").strip()
    check_in = input("Check-in Datum (YYYY-MM-DD): ").strip()
    check_out = input("Check-out Datum (YYYY-MM-DD): ").strip()
    details = input("Möchten Sie nur die Hotelinfos oder auch die Zimmerdetails sehen? (hotel / full): ").strip().lower()

    city = city if city else None
    stars = int(stars) if stars else None
    guests = int(guests) if guests else None
    check_in = datetime.strptime(check_in, "%Y-%m-%d").date() if check_in else None
    check_out = datetime.strptime(check_out, "%Y-%m-%d").date() if check_out else None
    if check_in and check_out and check_out <= check_in:
        print("Ungültiger Zeitraum: Check-out muss nach dem Check-in liegen.")
        return
    if details not in ["hotel", "full"]:
        print("Keine Eingabe, es werden nur Hotelinfos angezeigt.")
        details = "hotel"

    manager = HotelManager()
    all_hotels = manager.read_all_hotels_extended_info()

    matching_hotels = []

    for hotel in all_hotels:
        if city and city.lower() not in hotel.address.city.lower():
            continue
        if stars and hotel.stars < stars:
            continue

        seen_room_ids = set()
        available_rooms = []

        for room in hotel.rooms:
            if room.room_id in seen_room_ids:
                continue
            seen_room_ids.add(room.room_id)

            if guests and room.room_type.max_guests < guests:
                continue

            is_available = True
            if check_in and check_out:
                for booking in getattr(room, "bookings", []):
                    if not booking.is_cancelled:
                        b_in = booking.check_in_date
                        b_out = booking.check_out_date
                        if check_in < b_out and check_out > b_in:
                            is_available = False
                            break

            if not check_in or not check_out:
                is_available = True

            if is_available:
                available_rooms.append(room)

        if available_rooms:
            hotel_copy = copy.deepcopy(hotel)
            hotel_copy.rooms = available_rooms
            matching_hotels.append(hotel_copy)

    if not matching_hotels:
        print("\n Keine passenden Hotels gefunden.")
    else:
        print("\nGefundene Hotels:\n")
        for idx, hotel in enumerate(matching_hotels, start=1):
            address = hotel.address
            full_address = f"{address.street}, {address.zip_code} {address.city}"
            print(f" {idx}. Hotel: {hotel.name}, Adresse: {full_address} ({hotel.stars} Sterne)")
            if details == "full":
                for room in hotel.rooms:
                    print(f"  - Zimmer {room.room_number}, max. Gäste: {room.room_type.max_guests}, Preis: {room.price_per_night:.2f} CHF")

    return matching_hotels, check_in, check_out

results = user_search_hotels_from_data()

user_search_hotels_from_data()

# 2. Als Gast möchte ich Details zu verschiedenen Zimmertypen (Single, Double, Suite usw.), die in einem Hotel verfügbar sind, sehen, einschliesslich der maximalen Anzahl von Gästen für dieses Zimmer, Beschreibung, Preis und Ausstattung, um eine fundierte Entscheidung zu treffen.
# 2.1. Ich möchte die folgenden Informationen pro Zimmer sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung, Ausstattung, Preis pro Nacht und Gesamtpreis.
def read_rooms_by_hotel(self, hotel: model.Hotel) -> list[model.Room]:
    sql = """
    SELECT room_id, room_number, type_id, price_per_night
    FROM Room
    WHERE hotel_id = ?
    """
    if hotel is None:
        raise ValueError("hotel kann nicht leer sein.")

    params = tuple([hotel.hotel_id])
    rooms = self.fetchall(sql, params)
    return [
        model.Room(row[0], hotel)
        for row in rooms
    ]


def read_hotels_like_name(self, name: str) -> list[model.Hotel]:
    sql = """
    SELECT hotel_id, name, stars, address_id FROM Hotel WHERE name LIKE ?
    """
    params = (f"%{name}%",)
    hotels = self.fetchall(sql, params)
    return [model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address_id=address_id)
            for hotel_id, name, stars, address_id in hotels]





user_search_hotels_from_data()
choose_hotel = input("Gib den Namen des Hotels an, welches du möchtest: ")

read_hotels_like_name(choose_hotel)
#read_rooms_by_hotel(choose_hotel)



#print("Es gibt folgende Zimmertypen: \n 1 = Single \n 2 = Double \n 3 = Suite \n 4 = Family Room \n 5 = Penthouse\n")
#type_id = int(input("Zu welchem Zimmertyp möchtest du weitere Informationen?"))
#all_details = room_manager.read_room_details(type_id)
#print(all_details)

# 2.2 User Story

from datetime import datetime
from business_logic.hotel_manager import HotelManager

def show_room_type_details_for_selected_hotel(matching_hotels: list, check_in=None, check_out=None):
    if not matching_hotels:
        print("Es sind keine passenden Hotels vorhanden.")
        return

    try:
        hotel_choice = int(input("\nBitte geben Sie die Nummer des gewünschten Hotels ein (z. B. 1): ").strip())
        if not (1 <= hotel_choice <= len(matching_hotels)):
            print("Ungültige Auswahl.")
            return
    except ValueError:
        print("Ungültige Eingabe.")
        return

    selected_hotel = matching_hotels[hotel_choice - 1]

    print(f"\nZimmerdetails für {selected_hotel.name}:\n")

    for room in selected_hotel.rooms:
        is_available = True
        if check_in and check_out:
            for booking in getattr(room, "bookings", []):
                if not booking.is_cancelled:
                    b_in = booking.check_in_date
                    b_out = booking.check_out_date
                    if check_in < b_out and check_out > b_in:
                        is_available = False
                        break

        if not check_in or not check_out or is_available:
            total_days = (check_out - check_in).days if check_in and check_out else None
            total_price = room.price_per_night * total_days if total_days else None

            print(f"    Zimmer {room.room_number}")
            print(f"    Typ: {room.room_type.description}")
            print(f"    Max. Gäste: {room.room_type.max_guests}")
            print(f"    Preis pro Nacht: {room.price_per_night:.2f} CHF")
            if total_price:
                print(f"    Gesamtpreis für {total_days} Nächte: {total_price:.2f} CHF")

            features = ', '.join(room.features) if hasattr(room, "features") and room.features else "Keine Angaben"
            print(f"    Ausstattung: {features}\n")

results, check_in, check_out = user_search_hotels_from_data()
show_room_type_details_for_selected_hotel(results, check_in, check_out)

# 4. Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.

from datetime import datetime
def create_booking_ui():

    booking_manager = BookingManager()
    hotel_dal = HotelDataAccess()
    room_dal = RoomDataAccess()
    room_type_dal = RoomTypeDataAccess()
    booking_dal = BookingDataAccess()

    try:
        # Schritt 1: Hotel auswählen
        hotels = hotel_dal.read_all_hotels()
        if not hotels:
            print("Keine Hotels verfügbar.")
            return

        print("Verfügbare Hotels:")
        for h in hotels:
            print(f"{h.hotel_id}: {h.name}")

        while True:
            try:
                hotel_id = int(input("Gib die Hotel-ID ein: "))
                hotel = hotel_dal.read_hotel_by_id(hotel_id)
                if hotel:
                    break
                print("Hotel nicht gefunden.")
            except ValueError:
                print("Bitte eine gültige ID eingeben.")

        # Schritt 2: Zimmertyp eingeben
        room_types = room_type_dal.read_all_room_types()
        print("Verfügbare Zimmertypen:")
        for rt in room_types:
            print(f"{rt.type_id}: {rt.description} (max. Gäste: {rt.max_guests})")

        while True:
            try:
                type_id = int(input("Gib die ID des gewünschten Zimmertyps ein: "))
                matching_rooms = [
                    r for r in room_dal.read_room_details(type_id)
                    if r.hotel.hotel_id == hotel_id
                ]
                if matching_rooms:
                    break
                print("Keine Zimmer dieses Typs im gewählten Hotel verfügbar.")
            except ValueError:
                print("Bitte eine gültige ID eingeben.")

        example_room = matching_rooms[0]
        print(
            f"Zimmertyp '{example_room.room_type.description}' kostet "
            f"{example_room.price_per_night} CHF pro Nacht."
        )

        confirm = input(
            "Möchtest du ein solches Zimmer buchen? (ja/nein): "
        ).strip().lower()
        if confirm != "ja":
            print("Buchung abgebrochen.")
            return

        # Schritt 3: Buchungsdaten eingeben
        first_name = input("Vorname: ")
        last_name = input("Nachname: ")
        email = input("E-Mail-Adresse: ")

        def parse_date(prompt: str) -> datetime:
            while True:
                value = input(prompt).strip()
                try:
                    return datetime.strptime(value, "%Y-%m-%d")
                except ValueError:
                    print("Ungültiges Datum, bitte im Format YYYY-MM-DD eingeben.")

        check_in_dt = parse_date("Check-in Datum (YYYY-MM-DD): ")
        check_out_dt = parse_date("Check-out Datum (YYYY-MM-DD): ")

        nights = (check_out_dt - check_in_dt).days
        if nights <= 0:
            print("Das Check-out-Datum muss nach dem Check-in-Datum liegen.")
            return

        guest_manager = GuestManager()
        guest = guest_manager.get_guest_by_email(email)
        if guest:
            print("Bestehender Gast wird verwendet.")
        else:
            guest = guest_manager.create_guest(first_name, last_name, email, address_id=1)

        selected_room = matching_rooms[0]

        booking = booking_manager.create_booking(
            guest_id=guest.guest_id,
            room_id=selected_room.room_id,
            check_in_date=check_in_dt.strftime("%Y-%m-%d"),
            check_out_date=check_out_dt.strftime("%Y-%m-%d"),
            price_per_night=selected_room.price_per_night,
        )

        print("\nBuchung erfolgreich!")
        print(f"- Gast: {first_name} {last_name}")
        print(f"- Hotel: {hotel.name}")
        print(f"- Zimmernummer: {selected_room.room_number}")
        print(
            f"- Zeitraum: {check_in_dt.date()} bis {check_out_dt.date()} ({nights} Nächte)"
        )
        print(f"- Gesamtpreis: {booking.total_amount:.2f} CHF\n")
        print("Wichtiger Hinweis:")
        print(
            "Kostenfreie Stornierung bis 48 Stunden vor Anreise möglich. Danach fällt eine Gebühr von 50% an."
        )

    except Exception as e:
        print("Fehler bei der Buchung:", e)

create_booking_ui()

#5. Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.
def create_invoice_for_guest_ui():
    from business_logic.invoice_manager import InvoiceManager
    from datetime import datetime

    try:
        booking_id_input = input("Bitte geben Sie die Buchungs-ID ein: ").strip()
        booking_id = int(booking_id_input)

        manager = InvoiceManager()
        booking = manager.get_booking_by_id(booking_id)

        if not booking:
            print("Buchung nicht gefunden.")
            return

        if booking.is_cancelled:
            print("Für stornierte Buchungen kann keine Rechnung erstellt werden.")
            return

        # Prüfen, ob Aufenthalt abgeschlossen
        today = datetime.now().date()
        check_out = booking.check_out_date
        if today < check_out:
            print("Die Rechnung kann erst nach abgeschlossenem Aufenthalt erstellt werden.")
            return

        # Rechnung erstellen, falls nicht vorhanden
        if manager.invoice_exists(booking_id):
            invoice = manager.get_invoice_by_booking_id(booking_id)
            print("\nDie Rechnung liegt bereits vor:")
        else:
            invoice = manager.create_invoice_if_not_exists(booking_id)
            print("\n Die Rechnung wurde erfolgreich erstellt:")

        # Rechnung anzeigen
        print(f"Rechnungsnummer: {invoice.invoice_id}")
        print(f"Buchungsnummer:  {invoice.booking_id}")
        print(f"Ausgestellt am:  {invoice.issue_date}")
        print(f"Gesamtbetrag:    {invoice.total_amount:.2f} CHF")


    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine gültige Buchungs-ID ein.")


create_invoice_for_guest_ui()

#6. Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hint: Sorgt für die entsprechende Invoice.
def cancel_booking_ui():
    print("Buchung stornieren")

    try:
        booking_id = int(input("Buchungs-ID eingeben: "))

        booking_manager = BookingManager()
        invoice_manager = InvoiceManager()

        cancelled_booking = booking_manager.cancel_booking(booking_id)

        # Buchungsdaten anzeigen
        print(f"\nStornierte Buchung:")
        print(f"Buchungs-ID: {cancelled_booking.booking_id}")
        print(f"Gast-ID: {cancelled_booking.guest_id}")
        print(f"Zimmer-ID: {cancelled_booking.room_id}")
        print(f"Check-in: {cancelled_booking.check_in_date}")
        print(f"Check-out: {cancelled_booking.check_out_date}")
        print(f"Betrag: {cancelled_booking.total_amount:.2f}")
        print(f"Status: {'Storniert' if cancelled_booking.is_cancelled else 'Aktiv'}")

        try:
            cancelled_invoice = invoice_manager.cancel_invoice_by_booking(booking_id)
            print(f"Rechnung wurde ebenfalls storniert (ID: {cancelled_invoice.invoice_id})")
        except ValueError:
            print("Keine Rechnung vorhanden.")

    except ValueError:
        print("Buchung nicht gefunden.")
    except Exception as e:
        print(f"Fehler: {e}")


cancel_booking_ui()

# 7. Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann.

def choose_hotel_ui():
    hotel_name = input("Gib den Namen ein des Hotels, dass du buchen möchtest: ")
    if not hotel_name:
        print("Kein Hotelname eingegeben.")
        return None

    check_in_input = input("Geben Sie Ihr geplantes Check-in Datum ein (YYYY-MM-DD): ")
    try:
        check_in_date = datetime.strptime(check_in_input, "%Y-%m-%d")
    except ValueError:
        print("Ungültiges Datumsformat. Verwende heutige Preise.")
        check_in_date = datetime.now()

    manager = HotelManager()
    booking_manager = BookingManager()
    all_hotels = manager.read_all_hotels_extended_info()

    found_hotels = []
    for hotel in all_hotels:
        if hotel_name.lower() in hotel.name.lower():
            found_hotels.append(hotel)

    if not found_hotels:
        print(f"Kein Hotel mit dem Namen '{hotel_name}' gefunden.")
        return None
    elif len(found_hotels) == 1:
        selected_hotel = found_hotels[0]
        print(f"Hotel gefunden: {selected_hotel.name}")
    else:
        print(f"Mehrere Hotels gefunden mit '{hotel_name}':")
        for i, hotel in enumerate(found_hotels, 1):
            print(f"{i}. {hotel.name} in {hotel.address.city}")

        while True:
            try:
                choice = int(input(f"Welches Hotel möchten Sie? (1-{len(found_hotels)}): "))
                if 1 <= choice <= len(found_hotels):
                    selected_hotel = found_hotels[choice - 1]
                    break
                else:
                    print(f"Bitte geben Sie eine Zahl zwischen 1 und {len(found_hotels)} ein.")
            except ValueError:
                print("Bitte geben Sie eine gültige Zahl ein.")

    month = check_in_date.month
    if month in [6, 7, 8, 12]:
        season_info = "Hochsaison (+30%)"
        season_factor = 1.3
    elif month in [1, 2, 3, 11]:
        season_info = "Nebensaison (-10%)"
        season_factor = 0.9
    else:
        season_info = "Normale Saison"
        season_factor = 1.0

    print(f"\n--- {selected_hotel.name} ---")
    print(f"Adresse: {selected_hotel.address.street}, {selected_hotel.address.zip_code} {selected_hotel.address.city}")
    print(f"Sterne: {selected_hotel.stars}")
    print(f"Check-in: {check_in_date.strftime('%d.%m.%Y')} ({season_info})")
    print(f"Verfügbare Zimmer: {len(selected_hotel.rooms)}")

    if selected_hotel.rooms:
        print("\nVerfügbare Zimmer mit dynamischen Preisen:")
        total_min_price = float('inf')
        total_max_price = 0

        for room in selected_hotel.rooms:
            base_price = room.price_per_night
            check_in_str = check_in_date.strftime("%Y-%m-%d")  # datetime zu String konvertieren
            dynamic_price = booking_manager.calculate_dynamic_price(base_price, check_in_str)

            if dynamic_price != base_price:
                price_diff = dynamic_price - base_price
                if price_diff > 0:
                    price_info = f"{dynamic_price:.2f} CHF/Nacht (Basis: {base_price:.2f} CHF, +{price_diff:.2f} CHF)"
                else:
                    price_info = f"{dynamic_price:.2f} CHF/Nacht (Basis: {base_price:.2f} CHF, {price_diff:.2f} CHF)"
            else:
                price_info = f"{dynamic_price:.2f} CHF/Nacht"

            print(f"  - Zimmer {room.room_number}: {room.room_type.max_guests} Gäste, {price_info}")

            if dynamic_price < total_min_price:
                total_min_price = dynamic_price
            if dynamic_price > total_max_price:
                total_max_price = dynamic_price

        if total_min_price == total_max_price:
            print(f"\nDynamischer Preis: {total_min_price:.2f} CHF pro Nacht")
        else:
            print(f"\nDynamischer Preisbereich: {total_min_price:.2f} - {total_max_price:.2f} CHF pro Nacht")

        calculate_total = input(
            "\nMöchten Sie den Gesamtpreis für einen bestimmten Zeitraum berechnen? (j/n): ").strip().lower()
        if calculate_total == 'j':
            try:
                nights = int(input("Wie viele Nächte möchten Sie bleiben?: "))
                if nights > 0:
                    print(f"\nGesamtpreis für {nights} Nächte (mit {season_info}):")
                    print(f"  Günstigstes Zimmer: {total_min_price * nights:.2f} CHF")
                    if total_min_price != total_max_price:
                        print(f"  Teuerstes Zimmer: {total_max_price * nights:.2f} CHF")

                    base_min = total_min_price / season_factor
                    base_max = total_max_price / season_factor
                    total_base_min = base_min * nights
                    total_base_max = base_max * nights
                    savings_min = (total_min_price * nights) - total_base_min
                    savings_max = (total_max_price * nights) - total_base_max

                    if savings_min != 0:
                        if savings_min > 0:
                            print(f"  Saison-Aufschlag: +{savings_min:.2f} CHF bis +{savings_max:.2f} CHF")
                        else:
                            print(f"  Saison-Ersparnis: {abs(savings_min):.2f} CHF bis {abs(savings_max):.2f} CHF")
                else:
                    print("Anzahl Nächte muss größer als 0 sein.")
            except ValueError:
                print("Bitte geben Sie eine gültige Zahl ein.")
    else:
        print("Keine verfügbaren Zimmer in diesem Hotel.")

    return selected_hotel


user_search_hotels_from_data()
choose_hotel_ui()

## User Stories mit DB-Schemaänderung

#3. Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.
def hotel_review_ui():
    print("Geben Sie Ihre Bewertung für Ihr Hotel ab. \n")
    hotel_dal = HotelDataAccess()
    hotel_review_dal = HotelReviewDataAccess()

    try:
        guest_id = int(
            input("Ihre Gast-ID: "))  # Annahme, dass diese Information auf der Buchungsbestätigung enthalten ist.
        hotels = hotel_dal.read_all_hotels()
        if not hotels:
            print("Keine Hotels verfügbar.")
            return

        # print("\nVerfügbare Hotels:") => optimalerweise nur effektiv gebuchte Hotels anzeigen
        # for hotel in hotels:
        #    print(f"ID: {hotel.hotel_id} | {hotel.name} ({hotel.stars} Sterne)")

        # Hotel auswählen
        hotel_id = int(input("\nHotel-ID für Bewertung: "))
        selected_hotel = hotel_dal.read_hotel_by_id(hotel_id)

        if selected_hotel is None:
            print("Hotel nicht gefunden.")
            return

        # Buchungs-ID eingeben
        booking_id = int(input("Ihre Buchungs-ID: "))

        # Bewertung eingeben (1-5 Sterne)
        while True:
            try:
                print("Sie können das Hotel mit 1-5 Sternen bewerten.")
                rating = int(input("Bewertung (1-5 Sterne): "))
                if 1 <= rating <= 5:
                    break
                else:
                    print("Bewertung muss zwischen 1 und 5 liegen.")
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")

        # Optional: Kommentar
        print("Sie können einen Kommentar für andere Interessierte hinterlassen.")
        comment = input("Kommentar (optional): ").strip()
        if not comment:
            comment = None

        # Bewertung erstellen und speichern
        hotel_review = model.HotelReview(
            guest_id=guest_id,
            hotel_id=hotel_id,
            booking_id=booking_id,
            rating=rating,
            comment=comment,
            review_date=datetime.now().strftime("%Y-%m-%d")
        )

        hotel_review_dal.create_hotel_review(hotel_review)

        print("\n" + "-" * 30)
        print("Bewertung erfolgreich gespeichert.")
        print(f"Hotel: {selected_hotel.name}")
        print(f"Bewertung: {rating}/5 Sterne")
        if comment:
            print(f"Kommentar: {comment}")
        print(f"Datum der Bewertung: {hotel_review.review_date}")
        print("-" * 30)

    except ValueError:
        print("Ungültige Eingabe. Bitte Zahlen für IDs verwenden.")
    except Exception as e:
        print(f"Fehler beim Speichern der Bewertung: {e}")


hotel_review_ui()

#4. Als Gast möchte ich vor der Buchung Hotelbewertungen lesen, damit ich das beste Hotel auswählen kann.
def view_hotel_reviews_ui():
    print("Hotelbewertungen anzeigen:")

    hotel_dal = HotelDataAccess()
    review_dal = HotelReviewDataAccess()

    try:
        hotel_name = input("Gib den Namen des Hotels an, von dem du Bewertungen sehen möchtest: ")
        manager = HotelManager()
        found_hotels = manager.read_hotels_by_similar_name(hotel_name)

        if found_hotels is None:
            print("Hotel nicht gefunden.")
            return

        for i, hotel in enumerate(found_hotels, 1):
            print(f"{i}. Hotel ID: {hotel.hotel_id}, Hotelname: {hotel.name}, Address ID {hotel.address_id}")

        choice = int(input(f"Wähle Hotel (1-{len(found_hotels)}): "))
        selected_hotel = found_hotels[choice - 1]

        print(f"\nBewertungen für das Hotel: {selected_hotel.name}")
        print("-" * 50)

        reviews = review_dal.read_reviews_by_hotel_id(selected_hotel.hotel_id)

        if not reviews:
            print(f"Noch keine Bewertungen für {selected_hotel.name} vorhanden.")
            return

        # Durchschnittsbewertung berechnen
        total_rating = sum(review.rating for review in reviews)
        avg_rating = total_rating / len(reviews)

        print(f"Durchschnittliche Bewertung: {avg_rating:.1f}/5 ({len(reviews)} Bewertungen)")
        print("-" * 50)

        # Einzelne Bewertungen anzeigen
        for review in reviews:
            stars = "*" * review.rating
            print(f"{stars} ({review.rating}/5) | {review.review_date}")
            if review.comment:
                print(f"Kommentar: {review.comment}")
            print("-" * 50)

    except ValueError:
        print("Ungültige Eingabe.")
    except Exception as e:
        print(f"Fehler beim Laden der Bewertungen: {e}")


view_hotel_reviews_ui()

#6. Als Gast möchte ich meine Buchung mit der von mir bevorzugten Zahlungsmethode bezahlen, damit ich meine Reservierung abschliessen kann.
def pay_booking_ui():
    print("Buchung bezahlen")
    booking_id_input = input("Bitte geben Sie Ihre Buchungs-ID ein: ").strip()

    try:
        booking_id = int(booking_id_input)
    except ValueError:
        print("Ungültige Buchungs-ID.\n")
        return

    booking_manager = BookingManager()
    payment_manager = PaymentManager()

    booking = booking_manager.read_booking_by_id(booking_id)
    if booking is None:
        print("Buchung nicht gefunden.\n")
        return

    print(f"Zu zahlender Betrag: {booking.total_amount:.2f} CHF")
    print("Wählen Sie die Zahlungsmethode:")
    print("1 - Kreditkarte")
    print("2 - PayPal")
    print("3 - Banküberweisung")
    method_choice = input("Bitte wählen (1-3): ").strip()

    methods = {"1": "Kreditkarte", "2": "PayPal", "3": "Banküberweisung"}
    method = methods.get(method_choice)
    if method is None:
        print("Ungültige Auswahl.\n")
        return

    try:
        payment_manager.create_payment(booking.booking_id, booking.total_amount, method)
        print("Vielen Dank für Ihre Zahlung!\n")
    except Exception as e:
        print(f"Fehler bei der Zahlung: {e}\n")
pay_booking_ui()