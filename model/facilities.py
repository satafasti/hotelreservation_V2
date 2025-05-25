class Facilities:

    def __init__(
            self,
            facility_id : int, #Schreibfehler
            facility_name : str,
            ):
    
        self.__facility_id : int = facility_id
        self.__facility_name : str = facility_name

    @property
    def facility_id(self) -> int: #Schreibfehler
        return self.__facility_id


    @property
    def facility_name(self) -> str:
        return self.__facility_name

    @facility_name.setter
    def facility_name(self, facility_name : str):
        if not facility_name:
            raise ValueError ("facility_name required")
        if not isinstance(facility_name , str):
             raise TypeError("facility_name must be a string")
