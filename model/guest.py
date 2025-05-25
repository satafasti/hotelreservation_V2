class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, address_id: int):
        if not guest_id:
            raise ValueError("Guest ID is required")
        if not isinstance(guest_id, int):
            raise TypeError("Guest ID must be an integer")
        if not first_name:
            raise ValueError("First name is required")
        if not isinstance(first_name, str):
            raise TypeError("First name must be a string")
        if not last_name:
            raise ValueError("Last name is required")
        if not isinstance(last_name, str):
            raise TypeError("Last name must be a string")
        if not email:
            raise ValueError("Email is required")
        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        if address_id is not None and not isinstance(address_id, int):
            raise TypeError("Address ID must be an integer")
            
        self.__guest_id: int = guest_id
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__email: str = email
        self.__address_id: int = address_id
    
    @property
    def guest_id(self) -> int:
        return self.__guest_id
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @first_name.setter
    def first_name(self, new_first_name: str):
        if not new_first_name:
            raise ValueError("First name required")
        if not isinstance(new_first_name, str):
            raise TypeError("First name must be a string")
        self.__first_name = new_first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @last_name.setter
    def last_name(self, new_last_name: str):
        if not new_last_name:
            raise ValueError("Last name required")
        if not isinstance(new_last_name, str):
            raise TypeError("Last name must be a string")
        self.__last_name = new_last_name
    
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, new_email: str):
        if not new_email:
            raise ValueError("Email required")
        if not isinstance(new_email, str):
            raise TypeError("Email must be a string")
        self.__email = new_email
        
    @property
    def address_id(self) -> int:
        return self.__address_id
        
    @address_id.setter
    def address_id(self, new_address_id: int):
        if not new_address_id:
            raise ValueError ("Address ID wird benötigt")
        if not isinstance(new_address_id, int):
            raise TypeError("Address ID must be an integer")
        self.__address_id = new_address_id