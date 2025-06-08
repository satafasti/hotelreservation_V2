from data_access.guest_dal import GuestDataAccess
from model.guest import Guest
from typing import Optional, List
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

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

        city_counts = self.__dal.get_guest_city_count_by_hotel(hotel_id)

        if not city_counts:

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

    def get_guest_nationality_statistics_for_hotel(self, hotel_id: int) -> pd.DataFrame:

        nationality_counts = self.__dal.get_guest_nationality_count_by_hotel(hotel_id)

        if not nationality_counts:
            return pd.DataFrame(columns=['nationality', 'count', 'percentage'])

        total_guests = sum(count for _, count in nationality_counts)

        data = [
            {
                'nationality': nationality,
                'count': count,
                'percentage': round((count / total_guests) * 100, 1)
            }
            for nationality, count in nationality_counts
        ]

        return pd.DataFrame(data)


    def get_guest_age_statistics_for_hotel(self, hotel_id: int) -> pd.DataFrame:
        ages = self.__dal.get_guest_age_count_by_hotel(hotel_id)

        jugendliche = 0
        junge_erwachsene = 0
        berufstaetige = 0
        erfahrene = 0
        rentner = 0

        for age, count in ages:
            if age <= 17:
                jugendliche += count
            elif age <= 29:
                junge_erwachsene += count
            elif age <= 49:
                berufstaetige += count
            elif age <= 64:
                erfahrene += count
            else:
                rentner += count

        data = {
            'age_group': ['Jugendliche 0-17', 'Junge Erwachsene 18-29',
                          'Berufstätige 30-49', 'Erfahrene 50-64', 'Rentner 65+'],
            'count': [jugendliche, junge_erwachsene, berufstaetige, erfahrene, rentner]}

        df = pd.DataFrame(data)
        return df

    def guest_city_pie_chart(self, df: pd.DataFrame, title: str = "Gäste-Herkunft"):

        if df.empty:
            print("DataFrame ist leer.")
            return

        df.set_index('city')['count'].plot.pie(
            autopct='%1.1f%%',
            figsize=(8, 8),
            title=title)

        plt.ylabel('')  # Y-Label entfernen
        plt.show()

    def guest_nationality_pie_chart(self, df: pd.DataFrame, title: str = "Gäste-Herkunft nach Nationalitäten"):
        if df.empty:
            print("DataFrame ist leer.")
            return

        df.set_index('nationality')['count'].plot.pie(
            autopct='%1.1f%%',
            figsize=(8, 8),
            title=title
        )

        plt.ylabel('')
        plt.show()

    def guest_age_bar_chart(self, df: pd.DataFrame):

        if df.empty:
            print("Keine Daten zur Anzeige.")
            return

        fig = px.bar(df,
                     x='age_group',
                     y='count',
                     title='Gäste nach Altersgruppen',
                     labels={'age_group': 'Altersgruppen', 'count': 'Anzahl'})

        fig.show()