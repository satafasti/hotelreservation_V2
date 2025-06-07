from data_access.guest_dal import GuestDataAccess
from model.guest import Guest
from typing import Optional, List


class GuestManager:
    def __init__(self, db_path: str = None):
        self.__dal = GuestDataAccess(db_path)

    def create_guest(self, first_name: str, last_name: str, email: str, address_id: int) -> Guest:
        guest = Guest(None, first_name, last_name, email, address_id)
        return self.__dal.create_guest(guest)

    def get_guest_by_email(self, email: str) -> Optional[Guest]:
        return self.__dal.read_guest_by_email(email)

    def get_guest_by_id(self, guest_id: int) -> Optional[Guest]:
        return self.__dal.read_guest_by_id(guest_id)

    def get_all_guests(self) -> List[Guest]:
        return self.__dal.read_all_guests()

    def update_guest(self, guest: Guest) -> None:
         self.__dal.update_guest(guest)

    def delete_guest(self, guest: Guest) -> None:
        self.__dal.delete_guest(guest)


    def get_guest_city_statistics_for_hotel(self, hotel_id: int) -> pd.DataFrame:
        """
        Gibt eine übersichtliche Statistik der Gäste-Herkunftsstädte für ein Hotel als DataFrame zurück.

        Args:
            hotel_id: Die ID des Hotels

        Returns:
            pandas DataFrame mit Spalten: city, count, percentage
        """
        import pandas as pd

        city_counts = self.__dal.get_guest_city_count_by_hotel(hotel_id)

        if not city_counts:
            # Leeres DataFrame mit den erwarteten Spalten zurückgeben
            return pd.DataFrame(columns=['city', 'count', 'percentage'])

        total_guests = sum(count for _, count in city_counts)

        data = [
            {
                'city': city,
                'count': count,
                'percentage': round((count / total_guests) * 100, 1)
            }
            for city, count in city_counts
        ]

        return pd.DataFrame(data)