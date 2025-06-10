from __future__ import annotations

import model
from data_access.base_dal import BaseDataAccess
from typing import Optional

class FacilityDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)



    def read_facility_by_id(self, facility_id: int) -> Optional[model.Facilities]:
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


    def update_facility(self, facility_id: int, facility_name: str) -> model.Facilities:
        if facility_id is None:
           raise ValueError("Facility ID wird benötigt")

        sql = """
        UPDATE Facilities \
        SET facility_name = ?
        WHERE facility_id = ?
        """
        params = (facility_name, facility_id)
        self.execute(sql, params)

    def delete_facility(self, facility_id: int):
        if facility_id is None:
            raise ValueError("Facility ID wird benötigt")

        sql = """
              DELETE \
              FROM Facilities \
              WHERE facility_id = ? \
              """
        self.execute(sql, (facility_id,))


    #Auch in der UI gibt es keine Funktion, um neue Facilities anzulegen. Deshalb wird create_new_facility aktuell nirgendwo verwendet.
    # Das Vorgehen wird im README erwähnt: Man hat teilweise Code für mögliche Erweiterungen beibehalten, ohne ihn in der jetzigen Anwendung zu nutzen.

    # Kurz gesagt: Die Methode wurde implementiert, aber es gibt keine Stelle im Programm, die neue Ausstattungs­einträge anlegt.
    # Sie bleibt für eventuelle Erweiterungen erhalten, kommt aber momentan nicht zum Einsatz.

    # def create_new_facility(self, facility_id: int, facility_name: str) -> model.Facilities:
    #     # if facility_id is None:
    #     #     raise ValueError("Facility ID wird benötigt") -> sollte nicht passieren da autoincrement
    #     if not facility_name:
    #         raise ValueError("Facility name wird benötigt")
    #
    #     sql = """
    #           INSERT INTO Facilities (facility_id, facility_name)
    #           VALUES (?, ?) \
    #           """
    #     params = (facility_id, facility_name)
    #
    #     self.execute(sql, params)
    #
    #     return model.Facilities(facility_id=facility_id, facility_name=facility_name)

    # def read_all_facilities(self) -> list[model.Facilities]:
    #     sql = """
    #           SELECT facility_id, facility_name
    #           FROM Facilities \
    #           """
    #     results = self.fetchall(sql)
    #
    #     return [
    #         model.Facilities(facility_id=facility_id, facility_name=facility_name)
    #         for facility_id, facility_name in results
    #     ]
