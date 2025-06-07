CREATE TABLE Hotel (
	-- Author: AEP
    hotel_id       INTEGER PRIMARY KEY, 
    name           TEXT NOT NULL,
    stars          INTEGER,
    address_id     INTEGER,
    FOREIGN KEY (address_id) REFERENCES Address(address_id) ON DELETE SET NULL
);

CREATE TABLE Address (
	-- Author: AEP
    address_id     INTEGER PRIMARY KEY,
    street        TEXT NOT NULL,
    city          TEXT NOT NULL,
    zip_code      TEXT
);

CREATE TABLE Guest (
	-- Author: AEP
    guest_id       INTEGER PRIMARY KEY,
    first_name     TEXT NOT NULL,
    last_name      TEXT NOT NULL,
    email          TEXT UNIQUE,
    address_id     INTEGER,
    FOREIGN KEY (address_id) REFERENCES Address(address_id) ON DELETE SET NULL
);

CREATE TABLE Room_Type (
	-- Author: AEP
    type_id        INTEGER PRIMARY KEY,
    description    TEXT NOT NULL UNIQUE, -- E.g., Single, Double, Suite
    max_guests     INTEGER NOT NULL
);

CREATE TABLE Room (
	-- Author: AEP
    room_id        INTEGER PRIMARY KEY,
    hotel_id       INTEGER NOT NULL,
    room_number    TEXT NOT NULL,
    type_id        INTEGER NOT NULL,
    price_per_night REAL NOT NULL,
    FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES Room_Type(type_id) ON DELETE CASCADE
);

-- one-to-many mapping with guest, hotel, room
-- one booking can have only one room, but one room can be part of multiple bookings
-- if two rooms are booked for the same dates, two bookings should be created
-- check availability using business logic
CREATE TABLE Booking (
	-- Author: AEP
    booking_id     INTEGER PRIMARY KEY,
    guest_id       INTEGER NOT NULL,
    room_id        INTEGER NOT NULL,
    check_in_date  DATE NOT NULL,
    check_out_date DATE NOT NULL,
    is_cancelled   BOOLEAN NOT NULL DEFAULT 0, -- 0 = confirmed, 1 = cancelled
    total_amount   REAL,
    FOREIGN KEY (guest_id) REFERENCES Guest(guest_id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES Room(room_id) ON DELETE CASCADE
);


CREATE TABLE Invoice (
	-- Author: AEP
    invoice_id     INTEGER PRIMARY KEY,
    booking_id     INTEGER NOT NULL,
    issue_date     DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_amount   REAL NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id) ON DELETE CASCADE
);

CREATE TABLE Facilities (
	-- Author: AEP
    facility_id   INTEGER PRIMARY KEY,
    facility_name TEXT NOT NULL UNIQUE -- E.g., "Shower", "TV", "WiFi", "Air Conditioning"
);

CREATE TABLE Room_Facilities (
	-- Author: AEP
    room_id       INTEGER NOT NULL,
    facility_id   INTEGER NOT NULL,
    PRIMARY KEY (room_id, facility_id),
    FOREIGN KEY (room_id) REFERENCES Room(room_id) ON DELETE CASCADE,
    FOREIGN KEY (facility_id) REFERENCES Facilities(facility_id) ON DELETE CASCADE
);

CREATE TABLE Hotel_Review (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_id INTEGER NOT NULL,
    hotel_id INTEGER NOT NULL,
    booking_id INTEGER NOT NULL,
    rating INTEGER CHECK(rating >= 1 AND rating <= 5),
    comment TEXT,
    FOREIGN KEY (guest_id) REFERENCES Guest(guest_id),
    FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id),
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id),
    UNIQUE(booking_id)
);

INSERT INTO Address (address_id, street, city, zip_code) VALUES
(1, 'Bahnhofstrasse 1', 'Zürich', '8001'),
(2, 'Rue du Rhône 42', 'Genève', '1204'),
(3, 'Pilatusstrasse 15', 'Luzern', '6003'),
(4, 'Marktgasse 59', 'Bern', '3011'),
(5, 'Freiestrasse 10', 'Basel', '4051');

INSERT INTO Hotel (hotel_id, name, stars, address_id) VALUES
(1, 'Hotel Baur au Lac', 5, 1),
(2, 'Four Seasons Hôtel des Bergues', 5, 2),
(3, 'Grand Hotel National', 5, 3),
(4, 'Bellevue Palace', 5, 4),
(5, 'Les Trois Rois', 5, 5);

INSERT INTO Guest (guest_id, first_name, last_name, email, address_id) VALUES
(1, 'Hans', 'Müller', 'hans.mueller@example.ch', 1),
(2, 'Sophie', 'Meier', 'sophie.meier@example.ch', 2),
(3, 'Luca', 'Rossi', 'luca.rossi@example.ch', 3),
(4, 'Elena', 'Keller', 'elena.keller@example.ch', 4),
(5, 'Marc', 'Weber', 'marc.weber@example.ch', 5);


INSERT INTO Room_Type (type_id, description, max_guests) VALUES 
(1, 'Single', 1),
(2, 'Double', 2),
(3, 'Suite', 4),
(4, 'Family Room', 5),
(5, 'Penthouse', 6);


INSERT INTO Room (room_id, hotel_id, room_number, type_id, price_per_night) VALUES
(1, 1, '101', 1, 250.00),
(2, 1, '102', 2, 400.00),
(3, 2, '201', 3, 650.00),
(4, 3, '301', 4, 900.00),
(5, 4, '401', 5, 1500.00);

INSERT INTO Booking (booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount) VALUES
(1, 1, 1, '2025-06-01', '2025-06-05', 0, 1000.00),
(2, 2, 2, '2025-07-10', '2025-07-15', 0, 2000.00),
(3, 3, 3, '2025-08-20', '2025-08-22', 0, 1300.00),
(4, 4, 4, '2025-09-05', '2025-09-10', 1, 0.00), -- Cancelled booking
(5, 5, 5, '2025-10-01', '2025-10-07', 0, 9000.00);

INSERT INTO Invoice (invoice_id, booking_id, issue_date, total_amount) VALUES
(1, 1, '2025-06-05', 1000.00),
(2, 2, '2025-07-15', 2000.00),
(3, 3, '2025-08-22', 1300.00),
(4, 5, '2025-10-07', 9000.00),
(5, 4, '2025-09-10', 0.00); -- Cancelled booking, no charge

INSERT INTO Facilities (facility_id, facility_name) VALUES
(1, 'WiFi'),
(2, 'TV'),
(3, 'Air Conditioning'),
(4, 'Mini Bar'),
(5, 'Balcony');

INSERT INTO Room_Facilities (room_id, facility_id) VALUES
(1, 1), -- Room 101 has WiFi
(1, 2), -- Room 101 has TV
(2, 1), -- Room 102 has WiFi
(3, 3), -- Room 201 has Air Conditioning
(4, 4); -- Room 301 has Mini Bar

-- INSERT Statements für 20 neue Adressen (IDs 6-25)
INSERT INTO Address (address_id, street, city, zip_code) VALUES
(6, 'Langstrasse 23', 'Zürich', '8004'),
(7, 'Rennweg 7', 'Zürich', '8001'),
(8, 'Quai du Mont-Blanc 19', 'Genève', '1201'),
(9, 'Rue de la Servette 45', 'Genève', '1202'),
(10, 'Alpenquai 12', 'Luzern', '6005'),
(11, 'Hertensteinstrasse 34', 'Luzern', '6004'),
(12, 'Kramgasse 18', 'Bern', '3011'),
(13, 'Junkerngasse 25', 'Bern', '3011'),
(14, 'Steinenvorstadt 31', 'Basel', '4051'),
(15, 'Elisabethenstrasse 14', 'Basel', '4051'),
(16, 'Seefeldstrasse 89', 'Zürich', '8008'),
(17, 'Bahnhofplatz 3', 'St. Gallen', '9000'),
(18, 'Bahnhofstrasse 56', 'Winterthur', '8400'),
(19, 'Via Nassa 28', 'Lugano', '6900'),
(20, 'Hauptgasse 41', 'Thun', '3600'),
(21, 'Promenade 67', 'Davos', '7270'),
(22, 'Dorfstrasse 12', 'Zermatt', '3920'),
(23, 'Bahnhofstrasse 88', 'Interlaken', '3800'),
(24, 'Poststrasse 19', 'Chur', '7000'),
(25, 'Kirchgasse 5', 'Schaffhausen', '8200');

-- INSERT Statements für 20 neue Gäste (IDs 6-25)
INSERT INTO Guest (guest_id, first_name, last_name, email, address_id) VALUES
(6, 'Anna', 'Fischer', 'anna.fischer@example.ch', 6),
(7, 'Michael', 'Schmid', 'michael.schmid@example.ch', 7),
(8, 'Laura', 'Bauer', 'laura.bauer@example.ch', 8),
(9, 'Stefan', 'Wagner', 'stefan.wagner@example.ch', 9),
(10, 'Julia', 'Hofmann', 'julia.hofmann@example.ch', 10),
(11, 'David', 'Zimmermann', 'david.zimmermann@example.ch', 11),
(12, 'Sarah', 'Berger', 'sarah.berger@example.ch', 12),
(13, 'Thomas', 'Lehmann', 'thomas.lehmann@example.ch', 13),
(14, 'Nina', 'Huber', 'nina.huber@example.ch', 14),
(15, 'Florian', 'Schneider', 'florian.schneider@example.ch', 15),
(16, 'Marta', 'Gerber', 'marta.gerber@example.ch', 16),
(17, 'Oliver', 'Brunner', 'oliver.brunner@example.ch', 17),
(18, 'Lisa', 'Steiner', 'lisa.steiner@example.ch', 18),
(19, 'Marco', 'Graf', 'marco.graf@example.ch', 19),
(20, 'Petra', 'Roth', 'petra.roth@example.ch', 20),
(21, 'Simon', 'Frei', 'simon.frei@example.ch', 21),
(22, 'Claudia', 'Wyss', 'claudia.wyss@example.ch', 22),
(23, 'Daniel', 'Gut', 'daniel.gut@example.ch', 23),
(24, 'Sabine', 'Moser', 'sabine.moser@example.ch', 24),
(25, 'Patrick', 'Sommer', 'patrick.sommer@example.ch', 25);

-- CREATE TABLE für Guest_Details
CREATE TABLE Guest_Details (
    guest_details_id INTEGER PRIMARY KEY,
    guest_id INTEGER NOT NULL,
    age INTEGER NOT NULL,
    nationality TEXT NOT NULL,
    geschlecht TEXT NOT NULL CHECK(geschlecht IN ('Männlich', 'Weiblich', 'Divers')),
    familienstand TEXT NOT NULL CHECK(familienstand IN ('Ledig', 'Verheiratet', 'Geschieden', 'Verwitwet')),
    FOREIGN KEY (guest_id) REFERENCES Guest(guest_id) ON DELETE CASCADE
);

-- INSERT Statements für alle 25 Gäste (IDs 1-25)
INSERT INTO Guest_Details (guest_details_id, guest_id, age, nationality, geschlecht, familienstand) VALUES
(1, 1, 45, 'Schweiz', 'Männlich', 'Verheiratet'),
(2, 2, 32, 'Schweiz', 'Weiblich', 'Ledig'),
(3, 3, 38, 'Italien', 'Männlich', 'Verheiratet'),
(4, 4, 29, 'Deutschland', 'Weiblich', 'Ledig'),
(5, 5, 52, 'Schweiz', 'Männlich', 'Geschieden'),
(6, 6, 27, 'Schweiz', 'Weiblich', 'Ledig'),
(7, 7, 41, 'Deutschland', 'Männlich', 'Verheiratet'),
(8, 8, 35, 'Österreich', 'Weiblich', 'Verheiratet'),
(9, 9, 33, 'Frankreich', 'Männlich', 'Ledig'),
(10, 10, 28, 'Schweiz', 'Weiblich', 'Ledig'),
(11, 11, 39, 'Deutschland', 'Männlich', 'Verheiratet'),
(12, 12, 31, 'Schweiz', 'Weiblich', 'Ledig'),
(13, 13, 47, 'Schweiz', 'Männlich', 'Verheiratet'),
(14, 14, 26, 'Italien', 'Weiblich', 'Ledig'),
(15, 15, 34, 'Deutschland', 'Männlich', 'Ledig'),
(16, 16, 42, 'Spanien', 'Weiblich', 'Verheiratet'),
(17, 17, 36, 'Schweiz', 'Männlich', 'Geschieden'),
(18, 18, 30, 'Schweiz', 'Weiblich', 'Verheiratet'),
(19, 19, 44, 'Italien', 'Männlich', 'Verheiratet'),
(20, 20, 37, 'Deutschland', 'Weiblich', 'Geschieden'),
(21, 21, 25, 'Schweiz', 'Männlich', 'Ledig'),
(22, 22, 48, 'Österreich', 'Weiblich', 'Verheiratet'),
(23, 23, 40, 'Schweiz', 'Männlich', 'Verheiratet'),
(24, 24, 43, 'Frankreich', 'Weiblich', 'Geschieden'),
(25, 25, 29, 'Schweiz', 'Männlich', 'Ledig');


INSERT INTO Booking (booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount) VALUES
(6, 6, 1, '2025-06-15', '2025-06-18', 0, 750.00),
(7, 7, 2, '2025-06-20', '2025-06-25', 0, 2000.00),
(8, 8, 3, '2025-07-01', '2025-07-03', 0, 1300.00),
(9, 9, 4, '2025-07-05', '2025-07-08', 0, 2700.00),
(10, 10, 5, '2025-07-12', '2025-07-14', 0, 3000.00),
(11, 11, 1, '2025-07-20', '2025-07-23', 0, 750.00),
(12, 12, 2, '2025-08-01', '2025-08-05', 0, 1600.00),
(13, 13, 3, '2025-08-10', '2025-08-12', 1, 0.00),  -- Storniert
(14, 14, 4, '2025-08-15', '2025-08-20', 0, 4500.00),
(15, 15, 5, '2025-08-25', '2025-08-28', 0, 4500.00),
(16, 16, 1, '2025-09-01', '2025-09-04', 0, 750.00),
(17, 17, 2, '2025-09-08', '2025-09-12', 0, 1600.00),
(18, 18, 3, '2025-09-15', '2025-09-17', 0, 1300.00),
(19, 19, 4, '2025-09-20', '2025-09-25', 1, 0.00),  -- Storniert
(20, 20, 5, '2025-09-28', '2025-10-02', 0, 6000.00),
(21, 21, 1, '2025-10-05', '2025-10-07', 0, 500.00),
(22, 22, 2, '2025-10-10', '2025-10-15', 0, 2000.00),
(23, 23, 3, '2025-10-18', '2025-10-21', 0, 1950.00),
(24, 24, 4, '2025-10-25', '2025-10-28', 0, 2700.00),
(25, 25, 5, '2025-11-01', '2025-11-05', 0, 6000.00),
(26, 1, 2, '2025-11-08', '2025-11-11', 0, 1200.00),
(27, 2, 3, '2025-11-15', '2025-11-18', 0, 1950.00),
(28, 3, 4, '2025-11-20', '2025-11-23', 1, 0.00),  -- Storniert
(29, 4, 5, '2025-11-25', '2025-11-30', 0, 7500.00),
(30, 5, 1, '2025-12-01', '2025-12-04', 0, 750.00),
(31, 6, 2, '2025-12-08', '2025-12-12', 0, 1600.00),
(32, 7, 3, '2025-12-15', '2025-12-18', 0, 1950.00),
(33, 8, 4, '2025-12-20', '2025-12-24', 0, 3600.00),
(34, 9, 5, '2025-12-26', '2025-12-30', 0, 6000.00),
(35, 10, 1, '2026-01-05', '2026-01-08', 0, 750.00);

INSERT INTO Invoice (invoice_id, booking_id, issue_date, total_amount) VALUES
(6, 6, '2025-06-18', 750.00),
(7, 7, '2025-06-25', 2000.00),
(8, 8, '2025-07-03', 1300.00),
(9, 9, '2025-07-08', 2700.00),
(10, 10, '2025-07-14', 3000.00),
(11, 11, '2025-07-23', 750.00),
(12, 12, '2025-08-05', 1600.00),
(13, 13, '2025-08-12', 0.00),  -- Stornierte Buchung, keine Kosten
(14, 14, '2025-08-20', 4500.00),
(15, 15, '2025-08-28', 4500.00),
(16, 16, '2025-09-04', 750.00),
(17, 17, '2025-09-12', 1600.00),
(18, 18, '2025-09-17', 1300.00),
(19, 19, '2025-09-25', 0.00),  -- Stornierte Buchung, keine Kosten
(20, 20, '2025-10-02', 6000.00),
(21, 21, '2025-10-07', 500.00),
(22, 22, '2025-10-15', 2000.00),
(23, 23, '2025-10-21', 1950.00),
(24, 24, '2025-10-28', 2700.00),
(25, 25, '2025-11-05', 6000.00),
(26, 26, '2025-11-11', 1200.00),
(27, 27, '2025-11-18', 1950.00),
(28, 28, '2025-11-23', 0.00),  -- Stornierte Buchung, keine Kosten
(29, 29, '2025-11-30', 7500.00),
(30, 30, '2025-12-04', 750.00),
(31, 31, '2025-12-12', 1600.00),
(32, 32, '2025-12-18', 1950.00),
(33, 33, '2025-12-24', 3600.00),
(34, 34, '2025-12-30', 6000.00),
(35, 35, '2026-01-08', 750.00);