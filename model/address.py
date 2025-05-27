class Address:
    def __init__(self, address_id: int, street: str, city: str, zip_code: str):

        if address_id is None:
            raise ValueError("Address ID is required")
        if not isinstance(address_id, int):
            raise TypeError("Address ID must be an integer")

        if not street:
            raise ValueError("Street must be provided")
        if not isinstance(street, str):
            raise TypeError("Street must be a string")

        if not city:
            raise ValueError("City must be provided")
        if not isinstance(city, str):
            raise TypeError("City must be a string")

        if not zip_code:
            raise ValueError("zip_code must be provided")
        if not isinstance(zip_code, str):
            raise TypeError("zip_code must be a string")

            
        self.__address_id: int = address_id
        self.__street: str = street
        self.__city: str = city
        self.__zip_code: str = zip_code
    
    @property
    def address_id(self) -> int:
        return self.__address_id
    
    @property
    def street(self) -> str:
        return self.__street
    
    @street.setter
    def street(self, street: str):
        if not street:
            raise ValueError("Street required")
        if not isinstance(street, str):
            raise TypeError("Street must be a string")
        self.__street = street
    
    @property
    def city(self) -> str:
        return self.__city
    
    @city.setter
    def city(self, city: str):
        if not city:
            raise ValueError("City required")
        if not isinstance(city, str):
            raise TypeError("City must be a string")
        self.__city = city
    
    @property
    def zip_code(self) -> str:
        return self.__zip_code
    
    @zip_code.setter
    def zip_code(self, zip_code: str):
        if not zip_code:
            raise ValueError("Zip code required")
        if not isinstance(zip_code, str):
            raise TypeError("Zip code must be a string")
        self.__zip_code = zip_code