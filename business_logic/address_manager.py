from data_access.address_dal import AddressDataAccess
from model.address import Address

class AddressManager:
    def __init__(self, db_path: str = None):
        self.dal = AddressDataAccess(db_path)

    def create_address(self, address: Address):
        self.dal.create_new_address(address)
        return address
