from business_logic.hotel_manager import HotelManager

def user_search_hotel():
    # Eingabe vom Nutzer für Suche ohne Datum, braucht es für Suche mit Datum Booking = [] eine Liste damit dadurch iteriert werden kann? Wir haben auch für Booking keine Liste
    print("Hallo - Bitte geben Sie ihre gewünschten Suchkriterien ein. \nSie könne eine Eingabe auch leer lassen, dann wird sie für die Suche nicht beachtet")

    city = input("In Welche Stadt möchten Sie reisen?: ").strip()
    stars = input("Wie viele Sterne soll Ihr Hotel mindestens haben?: ").strip()
    guests = input("Für viele Personen soll das Zimmer sein?: ").strip()
    check_in = input("Wann möchten Sie anreisen?").strip()
    check_out = input("Wann möchten Sie abreisen?").strip()

    stars = int(stars) if stars else None
    guests = int(guests) if guests else None
    check_in = check_in if check_in else None
    check_out = check_out if check_out else None

    manager = HotelManager()

    results = manager.search_hotels(city, stars, guests, check_in, check_out)

    if not results:
        print("Keine passenden Hotels gefunden.")
    else:
        print("\nGefundene Hotels:\n")
        for hotel in results:
            print(f"- Hotelname: {hotel.name}")
            print(f"  Adresse: {hotel.address.street}, {hotel.address.zip_code} {hotel.address.city}")
            print(f"  Sterne: {hotel.stars}\n")


#3 1.4.Ich möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes ("von" (check_in_date) und "bis" (check_out_date)) Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe.


def admin_create_hotel():
    print("Hallo - Bitte erstellen Sie ein neues Hotel.")
    street = input("Gib die Strasse des Hotels ein: ")
    city = input("Gib den Ort des Hotels ein: ")
    zip_code = input("Gib den Zip-Code des Hotels ein: ")
    name = input("Gib den Hotelname ein: ")
    stars = input("Enter Hotel stars: ")
    room_number = input("Enter room number: ")
    description = input("Enter room type description: ")
    max_guests = input("Enter max guests: ")
    price_per_night = input("Enter price per night for the room: ")



    """    def create_hotel(self):
        rooms = []
        ### Angaben für Hoteladresse
        create_new_address = {}
        address_id = input("Enter Address ID: ") #new address_id falls benötigt
        if not address_id:
            raise ValueError("Address ID must be set")
        if not address_id.isdigit():
            raise ValueError("Address ID must be integer")
        create_new_address["address_id"] = int(address_id)
        street = input("Enter the street of the Hotel: ") #new hotel street
        if not street:
            raise ValueError("street must be set")
        create_new_address["street"] = street
        city = input("Enter the city of the Hotel: ") #new hotel city
        if not city:
            raise ValueError("city must be set")
        create_new_address["city"] = city
        zip_code = input("Enter the zip code of the Hotel: ") #new hotel zip_code
        if not zip_code:
            raise ValueError("zip_code must be set")
        create_new_address["zip_code"] = zip_code

        ### Angaben zum Hotel
        create_new_hotel = {}
        hotel_id = input("Enter Hotel ID: ") #wird das benötigt oder wird ID von SQL generiert?
        if not hotel_id:
            raise ValueError("hotel_id must be set")
        if not hotel_id.isdigit():
            raise TypeError("hotel_id must be an integer")
        create_new_hotel["hotel_id"] = int(hotel_id)
        name = input("Enter Hotel Name: ") #new hotel name
        if not name:
            raise ValueError("name must be set")
        create_new_hotel["name"] = name
        stars = input("Enter Hotel stars: ") #new hotel stars
        if not stars:
            raise ValueError("stars must be set")
        if not stars.isdigit():
            raise TypeError("stars must be an integer")
        create_new_hotel["stars"] = int(stars)

        #Angaben zum Raum
        while True:
            create_new_room = {}
            room_id = input("Enter room ID: ") #new room_id
            if not room_id:
                raise ValueError("room_id must be set")
            if not room_id.isdigit():
                raise TypeError("room_id must be an integer")
            create_new_room["room_id"] = int(room_id)
            room_number = input("Enter room number: ")
            if not room_number:
                raise ValueError("room_number must be set")
            if not room_number.isdigit():
                raise TypeError("room_number must be an integer")
            create_new_room["room_number"] = int(room_number)
            price_per_night = input("Enter price per night for the room: ")
            if not price_per_night:
                raise ValueError("price_per_night must be set")
            try:
                create_new_room["price_per_night"] = float(price_per_night)
            except ValueError:
                raise ValueError("price_per_night must be a float")
            description = input("Enter room type description: ")
            max_guests = input("Enter max guests: ")
            if not max_guests.isdigit():
                raise TypeError("max_guests must be an integer")

            room_type = Room_Type(
                type_id=create_new_room["room_id"],
                description=description,
                max_guests=int(max_guests)
            )

            # Neues Room-Objekt erstellen
            add_new_room = Room(
                room_id=create_new_room["room_id"],
                room_number=create_new_room["room_number"],
                price_per_night=create_new_room["price_per_night"],
                description=room_type
            )
            rooms.append(add_new_room)

            more = input("Add another room? (y/n): ")
            if more.lower() != 'y':
                break

            # Neues Hotel-Objekt erstellen
        add_new_hotel = Hotel(
            hotel_id=create_new_hotel["hotel_id"],
            name=create_new_hotel["name"],
            stars=create_new_hotel["stars"],
            address_id=create_new_address["address_id"], # address_id an das Hotel übergeben
            rooms=rooms
        )
        return create_new_hotel["hotel_id"], add_new_hotel


"""