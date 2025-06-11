from data_access.room_facilities_dal import RoomFacilitiesDataAccess
import model
from typing import List

class RoomFacilitiesManager:
    def __init__(self, db_path: str = None):
        self.__dal = RoomFacilitiesDataAccess(db_path)


#neu erstellte Funktionen 11.06.2025
    def add_facility_to_room(self, room: model.Room, facility: model.Facilities):
        self.__dal.create_facility_to_room(room, facility)

    def remove_facility_from_room(self, room: model.Room, facility: model.Facilities):
        self.__dal.delete_facility_from_room(room, facility)

    def read_facilities_by_room(self, room: model.Room) -> List[model.Facilities]:
        return self.__dal.read_facilities_by_room_id(room)

    def read_rooms_by_facility(self, facility: model.Facilities) -> List[model.Room]:
        return self.__dal.read_rooms_by_facility_id(facility)

    def has_facility(self, room: model.Room, facility: model.Facilities) -> bool:
        return self.__dal.has_facility(room, facility)

    def delete_facilities_from_room(self, room: model.Room):
        self.__dal.delete_room_facilities(room)

    def read_all_facilities(self) -> List[model.Facilities]:
        return self.__dal.read_all_facilities()

    def get_facility_selection(self, all_facilities):
        selected_facility_ids = []
        if all_facilities:
            add_facilities = input("\nMöchtest du Ausstattung hinzufügen? (ja/nein): ").lower()
            if add_facilities == "ja":
                print("\nVerfügbare Ausstattung:")
                for i, facility in enumerate(all_facilities, 1):
                    print(f"{i}. {facility.facility_name}")

                print("\nGib die Nummern der gewünschten Ausstattung ein (durch Komma getrennt, z.B. 1,3,5):")
                print("Oder drücke Enter um keine Ausstattung hinzuzufügen")

                facility_input = input("Auswahl: ").strip()
                if facility_input:
                    try:
                        facility_numbers = [int(x.strip()) for x in facility_input.split(",")]
                        for num in facility_numbers:
                            if 1 <= num <= len(all_facilities):
                                selected_facility_ids.append(all_facilities[num - 1].facility_id)

                        if selected_facility_ids:
                            selected_names = [all_facilities[num - 1].facility_name for num in facility_numbers if
                                              1 <= num <= len(all_facilities)]
                            print(f"Ausgewählte Ausstattung: {', '.join(selected_names)}")
                    except ValueError:
                        print("Ungültige Eingabe - keine Ausstattung hinzugefügt")
        return selected_facility_ids