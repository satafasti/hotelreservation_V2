from data_access.guest_dal import GuestDataAccess
from model.guest import Guest
from typing import Optional, List


class GuestManager:
    def __init__(self, db_path: str = None):
        self.__dal = GuestDataAccess(db_path)

    def create_guest(self, first_name: str, last_name: str, email: str, address_id: int) -> Guest:
        guest = Guest(None, first_name, last_name, email, address_id)
        return self.__dal.create_guest(guest)

    def get_guest_by_id(self, guest_id: int) -> Optional[Guest]:
              return self.__dal.read_guest_by_id(guest_id)

    def get_all_guests(self) -> List[Guest]:
              return self.__dal.read_all_guests()

    def update_guest(self, guest: Guest):
             self.__dal.update_guest(guest)

    def delete_guest(self, guest: Guest):
                self.__dal.delete_guest(guest)
