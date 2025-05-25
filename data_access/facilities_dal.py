from __future__ import annotations

import model
from data_access.base_dal import BaseDAL


class FacilitiesDAL(BaseDAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)


    def create_facilities(self, facilities: model.Facilities):
        sql = """
        INSERT INTO Facilities (facility_id, facility_name) VALUES (?, ?)
        """
        params = (facilities.facility_id if facilities else None, facilities.facility_name)
        self.execute(sql, params)

    def show_facilities_by_id(self, facilities: model.Facilities):
        sql = """
        SELECT * FROM Facilities WHERE facility_id = ?
        """
        params = (facilities.facility_id,)
        result = self.fetch_one(sql, params)
        if result:
            facility_id, facility_name = result
            return model.Facilities(facility_id, facility_name)
        else:
            return None

    def update_facilities(self, facilities: model.Facilities):
        sql = """
        UPDATE Facilities SET facility_name = ? WHERE facility_id = ?
        """
        params = (facilities.facility_name,facilities.facility_id)
        self.execute(sql, params)

    def delete_facilities(self, facilities: model.Facilities):
        sql = """
        DELETE FROM Facilities WHERE facility_id = ?
        """
        params = (facilities.facility_id,)
        self.execute(sql, params)


