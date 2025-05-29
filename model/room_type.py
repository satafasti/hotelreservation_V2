class Room_Type:

    def __init__(self, type_id : int, description : str, max_guests : int):
        if not type_id:
            raise ValueError("type_id must be set")
        if not isinstance(type_id, int):
            raise TypeError("type_id must be a int")
        if not description:
            raise ValueError("Description is required")
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        if not max_guests:
            raise ValueError("max_guests is required")
        if not isinstance(max_guests, int):
            raise TypeError("max_guests must be an integer")

        self.__type_id = type_id
        self.__description = description #z.B. Einzelzimmer
        self.__max_guests = max_guests

    @property
    def type_id(self):
        return self.__type_id

    @room_type_id.setter
    def type_id(self,new_type_id):
        self.__type_id = new_type_id

    @type_id.deleter #sollte nicht benötigt werden, da id alleine eigentlich nie gelöscht werden muss
    def type_id(self):
        del self.__type_id

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,description):
        self.__description = description

    @property
    def max_guests(self):
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, max_guests):
        self.__max_guests = max_guests
        