from data_access.facilities_dal import FacilityDataAccess
import model


class FacilitiesManager:
    def __init__(self, facilities_dal: FacilityDataAccess):
        self._dal = facilities_dal



    # Die folgenden Facility-Methoden sind aktuell nicht im Einsatz,
    # werden jedoch fuer mögliche Erweiterungen (z.B. ein Admin-Panel)
    # im Code belassen.

    # def create_facility(self, facility_id: int, facility_name: str) -> model.Facilities:
    #     if not facility_name:
    #         raise ValueError("Facility name wird benoetigt")
    #     return self._dal.create_new_facility(facility_id, facility_name)

    # def get_facility_by_id(self, facility_id: int) -> Optional[model.Facilities]:
    #     return self._dal.read_facility_by_id(facility_id)

    # def get_all_facilities(self) -> list[model.Facilities]:
    #     return self._dal.read_all_facilities()

    # def update_facility(self, facility_id: int, facility_name: str):
    #     if not facility_name:
    #         raise ValueError("Facility name wird benoetigt")
    #     self._dal.update_facility(facility_id, facility_name)

    # def delete_facility(self, facility_id: int):
    #     self._dal.delete_facility(facility_id)

    # def facility_exists(self, facility_id: int) -> bool:
    #     return self._dal.read_facility_by_id(facility_id) is not None

    # def is_name_unique(self, facility_name: str) -> bool:
    #     all_facilities = self.get_all_facilities()
    #     return all(f.facility_name != facility_name for f in all_facilities)

    #  def get_all_facilities(self) -> list[model.Facilities]:
    #    return self._dal.read_all_facilities()