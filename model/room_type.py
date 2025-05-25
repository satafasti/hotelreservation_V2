class Room_Type:

    def __init__(self, type_id : int, description : str, max_guests : int):
        if not type_id:
            raise ValueError("type_id must be set")
        if not isinstance(type_id, int):
            raise TypeError("type_id must be a int")
        if not description:
            raise ValueError("description must be set")
        if not isinstance(description, str):
            raise TypeError("description must be a str")
        if not max_guests:
            raise ValueError("max_guests must be set")
        if not isinstance(max_guests, int):
            raise TypeError("max_guests must be a int")

        self.__type_id = type_id
        self.__description = description #z.B. Einzelzimmer
        self.__max_guests = max_guests

    @property
    def type_id(self):
        return self.__type_id

    #@room_type_id.setter => Da Autoincrementation von SQL
    #def type_id(self,new_type_id):
        #self.__type_id = new_type_id

    @type_id.deleter #anschauen
    def type_id(self):
        del self.__type_id

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,new_description):
        self.__description = new_description

    @property
    def max_guests(self):
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, new_max_guests):
        self.__max_guests = new_max_guests
        