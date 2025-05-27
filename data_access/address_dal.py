
from data_access.base_dal import BaseDataAccess
import model.address

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_address(self, address: model.Address) -> model.Address:
        sql = """
        INSERT INTO Address (street, city, zip_code) VALUES (?, ?, ?)
        """
        params = (address.street, address.city, address.zip_code)

        last_row_id, row_count = self.execute(sql, params)
        return model.Address(last_row_id, address.street, address.city, address.zip_code)

    def read_address_by_id(self, address_id: int) -> model.Address | None:
        sql = """
        SELECT address_id, street, city, zip_code FROM Address WHERE address_id = ?
        """
        params = (address_id,)
        result = self.fetchone(sql, params)

        if result:
            address_id, street, city, zip_code = result
            return model.Address(address_id, street, city, zip_code)
        return None

    def read_address_by_city(self, city: str) -> list[model.Address]:
        if city is None:
            raise ValueError("city cannot be None")

        sql = """
        SELECT address_id, street, city, zip_code FROM Address WHERE city = ?
        """
        params = (city,)
        results = self.fetchall(sql, params)

        return [
            model.Address(address_id, street, city, zip_code)
            for address_id, street, city, zip_code in results
        ]