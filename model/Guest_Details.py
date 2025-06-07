


class Guest_Details:
    def __init__(self, guest_details_id: int, guest_id: int, age: int, nationality: str,
                 geschlecht: str, familienstand: str):

        if not isinstance(guest_details_id, int):
            raise TypeError("guest_details_id must be an integer")


        if not isinstance(guest_id, int):
            raise TypeError("Guest ID must be an integer")


        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        if age < 0:
            raise ValueError("age must be non-negative")


        if not isinstance(nationality, str):
            raise TypeError("nationality must be a string")
        if not nationality.strip():
            raise ValueError("nationality is required")


        if not isinstance(geschlecht, str):
            raise TypeError("geschlecht must be a string")
        if not geschlecht.strip():
            raise ValueError("geschlecht is required")


        if not isinstance(familienstand, str):
            raise TypeError("familienstand must be a string")
        if not familienstand.strip():
            raise ValueError("familienstand is required")


        self.__guest_details_id: int = guest_details_id
        self.__guest_id: int = guest_id
        self.__age: int = age
        self.__nationality: str = nationality
        self.__geschlecht: str = geschlecht
        self.__familienstand: str = familienstand

    def __repr__(self) -> str:
        return f"Guest_Details(guest_details_id={self.__guest_details_id}, guest_id={self.__guest_id}, age={self.__age})"


    @property
    def guest_details_id(self) -> int:
        return self.__guest_details_id

    @guest_details_id.setter
    def guest_details_id(self, new_guest_details_id: int):
        if not isinstance(new_guest_details_id, int):
            raise TypeError("guest_details_id must be an integer")
        self.__guest_details_id = new_guest_details_id


    @property
    def guest_id(self) -> int:
        return self.__guest_id

    @guest_id.setter
    def guest_id(self, new_guest_id: int):
        if not isinstance(new_guest_id, int):
            raise TypeError("Guest ID must be an integer")
        self.__guest_id = new_guest_id


    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age: int):
        if not isinstance(new_age, int):
            raise TypeError("age must be an integer")
        if new_age < 0:
            raise ValueError("age must be non-negative")
        self.__age = new_age


    @property
    def nationality(self) -> str:
        return self.__nationality

    @nationality.setter
    def nationality(self, new_nationality: str):
        if not isinstance(new_nationality, str):
            raise TypeError("nationality must be a string")
        if not new_nationality.strip():
            raise ValueError("nationality is required")
        self.__nationality = new_nationality


    @property
    def geschlecht(self) -> str:
        return self.__geschlecht

    @geschlecht.setter
    def geschlecht(self, new_geschlecht: str):
        if not isinstance(new_geschlecht, str):
            raise TypeError("geschlecht must be a string")
        if not new_geschlecht.strip():
            raise ValueError("geschlecht is required")
        self.__geschlecht = new_geschlecht


    @property
    def familienstand(self) -> str:
        return self.__familienstand

    @familienstand.setter
    def familienstand(self, new_familienstand: str):
        if not isinstance(new_familienstand, str):
            raise TypeError("familienstand must be a string")
        if not new_familienstand.strip():
            raise ValueError("familienstand is required")
        self.__familienstand = new_familienstand