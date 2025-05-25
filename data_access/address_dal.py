
import model
from data_access.base_dal import BaseDAL


class AddressDAL(BaseDAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def show_address_by_id(self, address: model.Address):
        sql = """
        SELECT * FROM Address WHERE address_id = ?
        """
        params = (address.address_id,)
        result = self.fetch_one(sql, params)
        if result:
            address_id, street, city, zip_code = result
            return model.Address(address_id, street, city, zip_code)
        else:
            return None


    def update_address(self, address: model.Address):
        sql = """
        UPDATE Address SET street = ?, city = ?, zip_code = ? WHERE address_id = ?
        """
        params = (address.street, address.city, address.zip_code, address.address_id)
        self.execute(sql, params)

    def delete_address(self, address: model.Address):
        sql = """
        DELETE FROM Address WHERE address_id = ?
        """
        params = (address.address_id,)
        self.execute(sql, params)

    def create_address(self, address: model.Address):
        sql = """
        INSERT INTO Address (street, city, zip_code) VALUES (?, ?, ?)
        """
        params = (address.street, address.city, address.zip_code)
        self.execute(sql, params)
