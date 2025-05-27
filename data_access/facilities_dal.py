from __future__ import annotations

import model
from data_access.base_dal import BaseDataAccess

class FacilityDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_facility(self, facility_id: int, facility_name: str) -> model.Facilities:
        if facility_id is None:
            raise ValueError("Facility ID wird benötigt")
        if not facility_name:
            raise ValueError("Facility name wird benötigt")

        sql = """
              INSERT INTO Facilities (facility_id, facility_name)
              VALUES (?, ?) \
              """
        params = (facility_id, facility_name)

        self.execute(sql, params)

        return model.Facilities(facility_id=facility_id, facility_name=facility_name)

    def read_facility_by_id(self, facility_id: int) -> model.Facilities | None:
        if facility_id is None:
            raise ValueError("Facility ID wird benötigt")

        sql = """
        SELECT facility_id, facility_name
        FROM Facilities
        WHERE facility_id = ?
        """
        result = self.fetchone(sql, (facility_id,))
        if result:
            (facility_id, facility_name) = result
            return model.Facilities(facility_id=facility_id, facility_name=facility_name)
        else:
            return None

    def read_all_facilities(self) -> list[model.Facilities]:
        sql = """
              SELECT facility_id, facility_name
              FROM Facilities \
              """
        results = self.fetchall(sql)

        return [
            model.Facilities(facility_id=facility_id, facility_name=facility_name)
            for facility_id, facility_name in results
        ]