def get_facility_selection(all_facilities):
    selected_facility_ids = []
    if all_facilities:
        add_facilities = input("\nMöchtest du Ausstattung hinzufügen? (ja/nein): ").lower()
        if add_facilities == "ja":
            print("\nVerfügbare Ausstattung:")
            for i, facility in enumerate(all_facilities, 1):
                print(f"{i}. {facility.facility_name}")

            print("\nGib die Nummern der gewünschten Ausstattung ein (durch Komma getrennt, z.B. 1,3,5):")
            print("Oder drücke Enter um keine Ausstattung hinzuzufügen")

            facility_input = input("Auswahl: ").strip()
            if facility_input:
                try:
                    facility_numbers = [int(x.strip()) for x in facility_input.split(",")]
                    for num in facility_numbers:
                        if 1 <= num <= len(all_facilities):
                            selected_facility_ids.append(all_facilities[num - 1].facility_id)

                    if selected_facility_ids:
                        selected_names = [all_facilities[num - 1].facility_name for num in facility_numbers if
                                          1 <= num <= len(all_facilities)]
                        print(f"Ausgewählte Ausstattung: {', '.join(selected_names)}")
                except ValueError:
                    print("Ungültige Eingabe - keine Ausstattung hinzugefügt")
    return selected_facility_ids


def get_room_input():
    room_number = input("Gib eine Zimmernummer ein: ")
    description = input(
        "Gib den Zimmertyp an (Single (max.1), Double (max.2), Suite (max.4), Family Room (max.5), Penthouse (max.6)): ")
    max_guests = int(input("Maximale Anzahl Gäste für das Zimmer: "))
    price_per_night = float(input("Gib den Preis pro Nacht für das Zimmer an: "))
    return room_number, description, max_guests, price_per_night


def get_hotel_choice(matching_hotels):
    if not matching_hotels:
        print("Keine passenden Hotels vorhanden.")
        return None

    try:
        choice = int(input(f"\nHotel-Nummer eingeben (1-{len(matching_hotels)}): "))
        if 1 <= choice <= len(matching_hotels):
            return matching_hotels[choice - 1]
        else:
            print("Ungültige Auswahl.")
            return None
    except ValueError:
        print("Ungültige Eingabe.")
        return None


def show_hotel_info(hotel):
    print(f"\n--- {hotel.name} ---")
    print(f"Adresse: {hotel.address.street}, {hotel.address.zip_code} {hotel.address.city}")
    print(f"Sterne: {hotel.stars}")
    print(f"Verfügbare Zimmer: {len(hotel.rooms)}")


def show_room_info(room, price):
    print(f"  - Zimmer {room.room_number}")
    print(f"    Typ: {room.room_type.description}")
    print(f"    Preis: {price:.2f} CHF/Nacht")
    features = ', '.join(room.features) if hasattr(room, "features") and room.features else "Keine Angaben"
    print(f"    Ausstattung: {features}")