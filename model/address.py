class Address:
    def __init__(self, address_id: int, street: str, city: str, zip_code: str):

        if address_id is None:
            raise ValueError("Address ID ist erforderlich")
        if not isinstance(address_id, int):
            raise TypeError("Address ID muss eine ganze Zahl sein")

        if not street:
            raise ValueError("Street ist erforderlich")
        if not isinstance(street, str):
            raise TypeError("Street muss ein String sein")

        if not city:
            raise ValueError("City ist erforderlich")
        if not isinstance(city, str):
            raise TypeError("City muss ein String sein")

        if not zip_code:
            raise ValueError("zip_code ist erforderlich")
        if not isinstance(zip_code, str):
            raise TypeError("zip_code muss ein String sein")

            
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
            raise ValueError("Street ist erforderlich")
        if not isinstance(street, str):
            raise TypeError("Street muss ein String sein")
        self.__street = street
    
    @property
    def city(self) -> str:
        return self.__city
    
    @city.setter
    def city(self, city: str):
        if not city:
            raise ValueError("City ist erforderlich")
        if not isinstance(city, str):
            raise TypeError("City muss ein String sein")
        self.__city = city
    
    @property
    def zip_code(self) -> str:
        return self.__zip_code
    
    @zip_code.setter
    def zip_code(self, zip_code: str):
        if not zip_code:
            raise ValueError("Zip code ist erforderlich")
        if not isinstance(zip_code, str):
            raise TypeError("Zip code muss ein String sein")
        self.__zip_code = zip_code