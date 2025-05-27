class Facilities:

    def __init__(self, facility_id : int, facility_name : str):

        if not facility_name:
            raise ValueError ("facility_name is required")
        if not isinstance(facility_name, str):
             raise TypeError("facility_name must be an string")

        self.__facility_id = facility_id
        self.__facility_name = facility_name

    @property
    def facility_id(self):
        return self.__facility_id

    @property
    def facility_name(self):
        return self.__facility_name

    @facility_name.setter
    def facility_name(self, facility_name: str):
        if not facility_name:
            raise ValueError("facility_name is required")
        if not isinstance(facility_name, str):
            raise TypeError("facility_name must be a string")
        self.__facility_name = facility_name

