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
from business_logic.payment_manager import PaymentManager


from datetime import datetime
from business_logic.hotel_manager import HotelManager
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
class GuestUI:
    def __init__(self, db_path: str = None):
        self.__hotel_manager = HotelManager(db_path)
        self.__address_manager = AddressManager(db_path)
        self.__guest_manager = GuestManager(db_path)
        self.__invoice_manager = InvoiceManager(db_path)
        self.__payment_manager = PaymentManager(db_path)
        self.__booking_manager = BookingManager(db_path)
        self.__room_manager = RoomManager(db_path)
        self.__room_type_manager = RoomTypeManager(db_path)
        self.__room_facility_manger = RoomFacilitiesManager(db_path)
        self.__hotel_review_manager = HotelReviewManager(db_path)


    def user_search_hotels_from_data(self):
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



    def show_room_type_details_for_selected_hotel(self, matching_hotels: list = None, check_in=None, check_out=None):
        if matching_hotels is None:
            results, check_in, check_out = self.user_search_hotels_from_data()
            matching_hotels = results

        if not matching_hotels:
            print("Es sind keine passenden Hotels vorhanden.")
            return matching_hotels, check_in, check_out, []

        try:
            hotel_choice = int(input("\nBitte geben Sie die Nummer des gewünschten Hotels ein (z.B. 1): ").strip())
            if not (1 <= hotel_choice <= len(matching_hotels)):
                print("Ungültige Auswahl.")
                return matching_hotels, check_in, check_out, []
        except ValueError:
            print("Ungültige Eingabe.")
            return matching_hotels, check_in, check_out, []

        selected_hotel = matching_hotels[hotel_choice - 1]
        available_rooms = []

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


                room_id = getattr(room, 'id', room.room_number)


                room_info = {
                    'id': room_id,
                    'room_number': room.room_number,
                    'room_type': room.room_type.description,
                    'max_guests': room.room_type.max_guests,
                    'price_per_night': room.price_per_night,
                    'total_days': total_days,
                    'total_price': total_price,
                    'features': getattr(room, "features", [])
                }
                available_rooms.append(room_info)

                # Print mit ID
                print(f"    ID: {room_id}")
                print(f"    Zimmer {room.room_number}")
                print(f"    Typ: {room.room_type.description}")
                print(f"    Max. Gäste: {room.room_type.max_guests}")
                print(f"    Preis pro Nacht: {room.price_per_night:.2f} CHF")
                if total_price:
                    print(f"    Gesamtpreis für {total_days} Nächte: {total_price:.2f} CHF")

                features = ', '.join(room.features) if hasattr(room, "features") and room.features else "Keine Angaben"
                print(f"    Ausstattung: {features}\n")

        return matching_hotels, check_in, check_out, available_rooms


# 4. Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.
# 6.(DB mit Schemaänderung) Als Gast möchte ich meine Buchung mit der von mir bevorzugten Zahlungsmethode bezahlen, damit ich meine Reservierung abschliessen kann.
    def parse_date(self, prompt: str) -> date:
        while True:
            try:
                return datetime.strptime(input(prompt), "%Y-%m-%d").date()
            except ValueError:
                print("Bitte gib das Datum im Format YYYY-MM-DD ein.")


    def create_booking_and_pay_ui(self):
        try:

            matching_hotels, check_in, check_out, available_rooms = self.show_room_type_details_for_selected_hotel()

            if not available_rooms:
                print("Keine verfügbaren Zimmer gefunden.")
                return

            print("\nVerfügbare Zimmer:")
            for i, room in enumerate(available_rooms, 1):
                print(
                    f"{i}. ID: {room['id']} - Zimmer {room['room_number']} - {room['room_type']} - {room['price_per_night']:.2f} CHF/Nacht")

            while True:
                try:
                    room_choice = int(input("Wählen Sie ein Zimmer (Nummer): ")) - 1
                    if 0 <= room_choice < len(available_rooms):
                        selected_room_info = available_rooms[room_choice]
                        break
                    print("Ungültige Auswahl.")
                except ValueError:
                    print("Bitte eine gültige Nummer eingeben.")

            print(
                f"\nGewähltes Zimmer: {selected_room_info['room_type']} - {selected_room_info['price_per_night']:.2f} CHF pro Nacht")
            if selected_room_info['total_price']:
                print(f"Gesamtpreis: {selected_room_info['total_price']:.2f} CHF")

            confirm = input("Möchten Sie dieses Zimmer buchen? (ja/nein): ").strip().lower()
            if confirm != "ja":
                print("Buchung abgebrochen.")
                return

            guest_data = self.collect_guest_data()

            booking = self.booking_manager.process_booking_with_payment(
                guest_data=guest_data,
                room_id=selected_room_info['id'],
                check_in_date=check_in,
                check_out_date=check_out,
                price_per_night=selected_room_info['price_per_night']
            )

            if booking:
                self.display_booking_confirmation(booking, guest_data, selected_room_info, check_in, check_out)
            else:
                print("Fehler bei der Buchung.")

        except Exception as e:
            print("Fehler bei der Buchung:", e)

    def collect_guest_data(self):

        first_name = input("Vorname: ")
        last_name = input("Nachname: ")
        email = input("E-Mail-Adresse: ")
        street = input("Strasse: ")
        zip_code = input("PLZ: ")
        city = input("Ort: ")


        print("\nWählen Sie die Zahlungsmethode:")
        print("1 - Kreditkarte")
        print("2 - PayPal")
        print("3 - Banküberweisung")
        method_choice = input("Bitte wählen (1-3): ").strip()
        methods = {"1": "Kreditkarte", "2": "PayPal", "3": "Banküberweisung"}
        payment_method = methods.get(method_choice)

        if payment_method is None:
            raise ValueError("Ungültige Zahlungsmethode gewählt")

        return {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'street': street,
            'zip_code': zip_code,
            'city': city,
            'payment_method': payment_method
        }

    def display_booking_confirmation(self, booking, guest_data, room_info, check_in, check_out):

        nights = (check_out - check_in).days

        print("\nBuchung erfolgreich!")
        print("Vielen Dank für Ihre Buchung. Wir freuen uns auf Ihren Besuch!\n")
        print(f"- Gast: {guest_data['first_name']} {guest_data['last_name']}")
        print(f"- Zimmertyp: {room_info['room_type']}")
        print(f"- Zimmernummer: {room_info['room_number']}")
        print(f"- Buchungsnummer: {booking.booking_id}")
        print(f"- Zeitraum: {check_in} bis {check_out} ({nights} Nächte)")
        print(f"- Gesamtpreis: {booking.total_amount:.2f} CHF")
        print(f"- Zahlungsmethode: {guest_data['payment_method']}\n")
        print("Wichtiger Hinweis:")
        print("Kostenfreie Stornierung bis 48 Stunden vor Anreise möglich. Danach fällt eine Gebühr von 50% an.")

#5. Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.
def create_invoice_for_guest_ui(self):
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
def cancel_booking_ui(self):
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

def choose_hotel_ui(self, check_in=None, check_out=None):
    hotel_name = input("Geben Sie den Hotelnamen ein, dass Sie buchen möchten: ")
    if not hotel_name:
        print("Kein Hotelname eingegeben.")
        return None

    if check_in is None:
        print(
            "Damit Ihnen nur verfügbare Zimmer angezeiget werden, können Sie ein gewünschtes Check-in Datum eingeben.")
        check_in_input = input("Gewünschtes Check-in Datum (YYYY-MM-DD): ")
        try:
            check_in = datetime.strptime(check_in_input, "%Y-%m-%d").date()
        except ValueError:
            print("Ungültiges Datumsformat. Format muss (YYYY-MM-DD) sein.")
            check_in = datetime.now().date()
    else:
        print(f"Check-in Datum bereits gesetzt: {check_in.strftime('%d.%m.%Y')}")

    manager = HotelManager()
    booking_manager = BookingManager()
    all_hotels = manager.read_all_hotels_extended_info()

    found_hotels = []
    for hotel in all_hotels:
        if hotel_name.lower() in hotel.name.lower():
            found_hotels.append(hotel)

    if not found_hotels:
        print(f"Kein Hotel mit dem Namen {hotel_name} gefunden.")
        return None
    elif len(found_hotels) == 1:
        selected_hotel = found_hotels[0]
        print(f"Hotel gefunden: {selected_hotel.name}")
    else:
        print(f"Mehrere Hotels gefunden mit {hotel_name}:")
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

    # Nutzen der existierenden calculate_dynamic_price Funktion
    season_factor = booking_manager.calculate_dynamic_price(1.0, check_in)

    print(f"\n--- {selected_hotel.name} ---")
    print(f"Adresse: {selected_hotel.address.street}, {selected_hotel.address.zip_code} {selected_hotel.address.city}")
    print(f"Sterne: {selected_hotel.stars}")
    print(f"Check-in: {check_in.strftime('%d.%m.%Y')}")
    print(f"Verfügbare Zimmer: {len(selected_hotel.rooms)}")

    if selected_hotel.rooms:
        print("\nVerfügbare Zimmer mit dynamischen Preisen:")
        total_min_price = float('inf')
        total_max_price = 0

        for room in selected_hotel.rooms:
            base_price = room.price_per_night
            dynamic_price = booking_manager.calculate_dynamic_price(base_price, check_in)

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

        if check_out is not None:
            nights = (check_out - check_in).days
            if nights > 0:
                print(f"\nGesamtpreis für {nights} Nächte:")
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
            calculate_total = input(
                "\nMöchten Sie den Gesamtpreis für einen bestimmten Zeitraum berechnen? (ja/nein): ").strip().lower()
            if calculate_total == "ja":
                try:
                    nights = int(input("Wie viele Nächte möchten Sie bleiben?: "))
                    if nights > 0:
                        print(f"\nGesamtpreis für {nights} Nächte:")
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
                        print("Anzahl Nächte muss grösser als 0 sein.")
                except ValueError:
                    print("Bitte geben Sie eine gültige Zahl ein.")
    else:
        print("Keine verfügbaren Zimmer in diesem Hotel.")

    return selected_hotel


    #results = user_search_hotels_from_data()
    #matching_hotels, check_in_date, check_out_date = results

    #if check_in_date is not None and check_out_date is not None:
    #    choose_hotel_ui(check_in_date, check_out_date)
    #elif check_in_date is not None:
    #    choose_hotel_ui(check_in_date)
    #else:
    #   choose_hotel_ui()



## User Stories mit DB-Schemaänderung

#3. Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.
def hotel_review_ui(self):
    print("Geben Sie Ihre Bewertung für Ihr Hotel ab. \n")
    hotel_manager = HotelManager()
    hotel_review_manager = HotelReviewManager()

    try:
        guest_id = int(
            input("Ihre Gast-ID: "))  # Annahme, dass diese Information auf der Buchungsbestätigung enthalten ist.
        hotels = hotel_manager.read_all_hotels()
        if not hotels:
            print("Keine Hotels verfügbar.")
            return

        hotel_id = int(input("\nHotel-ID für Bewertung: "))
        selected_hotel = hotel_manager.read_hotel(hotel_id)

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

        hotel_review_manager.create_hotel_review(hotel_review)

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

    hotel_manager = HotelManager()
    review_manager = HotelReviewManager()

    try:
        hotel_name = input("Gib den Namen des Hotels an, von dem du Bewertungen sehen möchtest: ")
        manager = HotelManager()
        found_hotels = hotel_manager.read_hotels_by_similar_name(hotel_name)

        if found_hotels is None:
            print("Hotel nicht gefunden.")
            return

        for i, hotel in enumerate(found_hotels, 1):
            print(f"{i}. Hotel ID: {hotel.hotel_id}, Hotelname: {hotel.name}, Address ID {hotel.address_id}")

        choice = int(input(f"Wähle Hotel (1-{len(found_hotels)}): "))
        selected_hotel = found_hotels[choice - 1]

        print(f"\nBewertungen für das Hotel: {selected_hotel.name}")
        print("-" * 50)

        reviews = review_manager.read_reviews_by_hotel_id(selected_hotel.hotel_id)

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

