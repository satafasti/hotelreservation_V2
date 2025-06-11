from business_logic.address_manager import AddressManager
from business_logic.booking_manager import BookingManager
from business_logic.guest_manager import GuestManager
from business_logic.invoice_manager import InvoiceManager
from business_logic.payment_manager import PaymentManager
from business_logic.room_manager import RoomManager
from business_logic.hotel_manager import HotelManager

from data_access.hotel_dal import HotelDataAccess
from data_access.room_dal import RoomDataAccess
from data_access.room_type_dal import RoomTypeDataAccess
from data_access.hotel_review_dal import HotelReviewDataAccess
from model import Room

from model.address import Address
from model.hotel import Hotel
from model.hotel_review import HotelReview

from datetime import datetime, date

# 1. Als Gast möchte ich die verfügbaren Hotels durchsuchen, damit ich dasjenige auswählen kann, welches meinen Wünschen entspricht. Wünsche sind:
# 1.1. Ich möchte alle Hotels in einer Stadt durchsuchen, damit ich das Hotel nach meinem bevorzugten Standort (Stadt) auswählen kann.
# 1.2. Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.
# 1.3. Ich möchte alle Hotels in einer Stadt durchsuchen, die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung).
# 123
# 1.4. Ich möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes ("von" (check_in_date) und "bis" (check_out_date)) Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe.
# 1.5. Ich möchte Wünsche kombinieren können, z.B. die verfügbaren Zimmer zusammen mit meiner Gästezahl und der mindest Anzahl Sterne.
# 1.6. Ich möchte die folgenden Informationen pro Hotel sehen: Name, Adresse, Anzahl der Sterne.
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
    details = input("Möchten Sie nur die Hotelinfos oder auch die Zimmerdetails sehen? (hotel / vollständig): ").strip().lower()

    city = city if city else None
    stars = int(stars) if stars else None
    guests = int(guests) if guests else None
    check_in = datetime.strptime(check_in, "%Y-%m-%d").date() if check_in else None
    check_out = datetime.strptime(check_out, "%Y-%m-%d").date() if check_out else None
    if check_in and check_out and check_out <= check_in:
        print("Ungültiger Zeitraum: Check-out muss nach dem Check-in liegen.")
        return
    if details not in ["hotel", "vollständig"]:
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
        print("\nKeine passenden Hotels gefunden.")
    else:
        print("\nGefundene Hotels:\n")
        for idx, hotel in enumerate(matching_hotels, start=1):
            address = hotel.address
            full_address = f"{address.street}, {address.zip_code} {address.city}"
            print(f" {idx}. Hotel: {hotel.name}, Adresse: {full_address} ({hotel.stars} Sterne)")
            if details == "vollständig":
                for room in hotel.rooms:
                    print(f"  - Zimmer {room.room_number}, max. Gäste: {room.room_type.max_guests}, Preis: {room.price_per_night:.2f} CHF")

    return matching_hotels, check_in, check_out



# 2. Als Gast möchte ich Details zu verschiedenen Zimmertypen (Single, Double, Suite usw.), die in einem Hotel verfügbar sind, sehen, einschliesslich der maximalen Anzahl von Gästen für dieses Zimmer, Beschreibung, Preis und Ausstattung, um eine fundierte Entscheidung zu treffen.
# 2.1. Ich möchte die folgenden Informationen pro Zimmer sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung, Ausstattung, Preis pro Nacht und Gesamtpreis.
# 2.2. Ich möchte nur die verfügbaren Zimmer sehen, sofern ich meinen Aufenthalt (von - bis) spezifiziert habe.
from datetime import datetime
from business_logic.hotel_manager import HotelManager

def show_room_type_details_for_selected_hotel(matching_hotels: list, check_in=None, check_out=None):
    if not matching_hotels:
        print("Es sind keine passenden Hotels vorhanden.")
        return

    try:
        hotel_choice = int(input("\nBitte geben Sie die Nummer des gewünschten Hotels ein (z.B. 1): ").strip())
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


# 4. Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.
# 6.(DB mit Schemaänderung) Als Gast möchte ich meine Buchung mit der von mir bevorzugten Zahlungsmethode bezahlen, damit ich meine Reservierung abschliessen kann.
def parse_date(prompt: str) -> date:
    while True:
        try:
            return datetime.strptime(input(prompt), "%Y-%m-%d").date()
        except ValueError:
            print("Bitte gib das Datum im Format YYYY-MM-DD ein.")

def create_booking_and_pay_ui():
    booking_manager = BookingManager()
    hotel_dal = HotelDataAccess()
    room_dal = RoomDataAccess()
    room_type_dal = RoomTypeDataAccess()
    payment_manager = PaymentManager()
    address_manager = AddressManager()
    guest_manager = GuestManager()

    try:
        # Hotel wählen
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

        # Zimmertyp wählen
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

        confirm = input("Möchtest du ein solches Zimmer buchen? (ja/nein): ").strip().lower()
        if confirm != "ja":
            print("Buchung abgebrochen.")
            return

        # Gast- und Buchungsdaten
        first_name = input("Vorname: ")
        last_name = input("Nachname: ")
        email = input("E-Mail-Adresse: ")
        street = input("Strasse: ")
        zip_code = input("PLZ: ")
        city = input("Ort: ")

        check_in_dt = parse_date("Check-in Datum (YYYY-MM-DD): ")
        check_out_dt = parse_date("Check-out Datum (YYYY-MM-DD): ")

        nights = (check_out_dt - check_in_dt).days
        if nights <= 0:
            print("Das Check-out-Datum muss nach dem Check-in-Datum liegen.")
            return

        guest = guest_manager.get_guest_by_email(email)
        if guest:
            print("Bestehender Gast wird verwendet.")
        else:
            address = Address(0, street, city, zip_code)
            address = address_manager.create_address(address)
            guest = guest_manager.create_guest(first_name, last_name, email, address.address_id)

        selected_room = matching_rooms[0]

        booking = booking_manager.create_booking(
            guest_id=guest.guest_id,
            room_id=selected_room.room_id,
            check_in_date=check_in_dt,
            check_out_date=check_out_dt,
            price_per_night=selected_room.price_per_night,
        )
        print("\nReservation für!")
        print(f"- Zeitraum: {check_in_dt} bis {check_out_dt} ({nights} Nächte)")
        print(f"- Gesamtpreis: {booking.total_amount:.2f} CHF\n")

          # Zahlung
        print("Wählen Sie die Zahlungsmethode:")
        print("1 - Kreditkarte")
        print("2 - PayPal")
        print("3 - Banküberweisung")
        method_choice = input("Bitte wählen (1-3): ").strip()
        methods = {"1": "Kreditkarte", "2": "PayPal", "3": "Banküberweisung"}
        method = methods.get(method_choice)
        if method is None:
            print("Ungültige Auswahl.")
            return

        payment_manager.create_payment(booking.booking_id, booking.total_amount, method)

        print("\nBuchung erfolgreich!")
        print("Vielen Dank für Ihre Buchung. Wir freuen uns auf Ihren Besuch!\n")
        print(f"- Gast: {first_name} {last_name}")
        print(f"- Hotel: {hotel.name}")
        print(f"- Zimmernummer: {selected_room.room_number}")
        print(f"- Buchungsnummer: {booking.booking_id}")
        print(f"- Zeitraum: {check_in_dt} bis {check_out_dt} ({nights} Nächte)")
        print(f"- Gesamtpreis: {booking.total_amount:.2f} CHF\n")
        print("Wichtiger Hinweis:")
        print("Kostenfreie Stornierung bis 48 Stunden vor Anreise möglich. Danach fällt eine Gebühr von 50% an.")

    except Exception as e:
        print("Fehler bei der Buchung:", e)


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
            print("\nDie Rechnung wurde erfolgreich erstellt:")

        # Rechnung anzeigen
        print(f"Rechnungsnummer: {invoice.invoice_id}")
        print(f"Buchungsnummer:  {invoice.booking_id}")
        print(f"Ausgestellt am:  {invoice.issue_date}")
        print(f"Gesamtbetrag:    {invoice.total_amount:.2f} CHF")


    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine gültige Buchungs-ID ein.")



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


# 7. Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann.

def calculate_saison_room_price(check_in=None, check_out=None, matching_hotels=None):
    hotel_manager = HotelManager()
    room_manager = RoomManager()
    booking_manager = BookingManager()

    hotel = hotel_manager.get_hotel_choice(matching_hotels)
    if not hotel:
        return None

    if check_in is None:
        print("\n" + "-" * 15 + "Reisezeitraum" + "-" * 15)
        check_in = booking_manager.get_checkin_date_if_missing()
    if check_out is None:
        check_out = booking_manager.get_checkout_date_if_missing()

    available_rooms = hotel_manager.get_available_rooms_for_period(hotel, check_in, check_out)
    hotel_manager.show_hotel_info(hotel)

    if not available_rooms:
        print("Keine verfügbaren Zimmer.")
        return None

    price_summary = hotel_manager.calculate_total_pricing_summary(available_rooms, check_in, check_out)

    print("\nZimmerdetails:")
    for room in available_rooms:
        price_info = hotel_manager.calculate_room_pricing(room, check_in)
        room_manager.show_room_info(room, price_info, check_in, check_out)

    booking_manager.show_total_pricing_summary(price_summary)
    return None


results = user_search_hotels_from_data()
matching_hotels, check_in_date, check_out_date = results
calculate_saison_room_price(check_in_date, check_out_date, matching_hotels)



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

        hotel_id = int(input("\nHotel-ID für Bewertung: "))
        selected_hotel = hotel_dal.read_hotel_by_id(hotel_id)

        if selected_hotel is None:
            print("Hotel nicht gefunden.")
            return

        booking_id = int(input("Ihre Buchungs-ID: "))

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

        print("Sie können einen Kommentar für andere Interessierte hinterlassen.")
        comment = input("Kommentar (optional): ").strip()
        if not comment:
            comment = None

        hotel_review = HotelReview(
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

        total_rating = sum(review.rating for review in reviews)
        avg_rating = total_rating / len(reviews)

        print(f"Durchschnittliche Bewertung: {avg_rating:.1f}/5 ({len(reviews)} Bewertungen)")
        print("-" * 50)

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

