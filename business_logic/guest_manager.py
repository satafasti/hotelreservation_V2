from data_access.guest_dal import GuestDataAccess
from model.guest import Guest
from typing import Optional
import pandas as pd
from datetime import date, datetime
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


    def get_all_guest_details_for_hotel(self, hotel_id: int) -> list[dict]:

        return self.__dal.get_all_guest_details_by_hotel(hotel_id)

    def calculate_age_and_convert_to_dataframe(self, guest_details: list[dict]) -> pd.DataFrame:
        if not guest_details:
            return pd.DataFrame()
        df = pd.DataFrame(guest_details)
        df['age'] = df['birthdate'].apply(self.calculate_age)
        return df

    def calculate_age(self, birthdate) -> int:
        if not birthdate:
            return None
        try:
            if isinstance(birthdate, str):
                birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
            today = date.today()
            return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        except:
            return None

    def create_city_count_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:

        if df.empty or 'city' not in df.columns:
            return pd.DataFrame(columns=['category', 'count'])

        city_counts = df['city'].value_counts().reset_index()
        city_counts.columns = ['category', 'count']
        return city_counts

    def create_nationality_count_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:

        if df.empty or 'nationality' not in df.columns:
            return pd.DataFrame(columns=['category', 'count'])

        nationality_counts = df['nationality'].value_counts().reset_index()
        nationality_counts.columns = ['category', 'count']
        return nationality_counts

    def create_gender_count_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:

        if df.empty or 'gender' not in df.columns:
            return pd.DataFrame(columns=['category', 'count'])

        gender_counts = df['gender'].value_counts().reset_index()
        gender_counts.columns = ['category', 'count']
        return gender_counts

    def create_marital_status_count_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:

        if df.empty or 'marital_status' not in df.columns:
            return pd.DataFrame(columns=['category', 'count'])

        marital_counts = df['marital_status'].value_counts().reset_index()
        marital_counts.columns = ['category', 'count']
        return marital_counts

    def create_age_group_count_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:

        if df.empty or 'age' not in df.columns:
            return pd.DataFrame(columns=['category', 'count'])

        def get_age_group(age):
            if pd.isna(age):
                return 'Unbekannt'
            elif age < 18:
                return 'Jugendliche (0-17)'
            elif age < 30:
                return 'Junge Erwachsene (18-29)'
            elif age < 50:
                return 'Berufstätige (30-49)'
            elif age < 65:
                return 'Erfahrene (50-64)'
            else:
                return 'Rentner (65+)'

        age_groups = df['age'].apply(get_age_group)
        age_group_counts = age_groups.value_counts().reset_index()
        age_group_counts.columns = ['category', 'count']
        return age_group_counts

    def create_universal_pie_chart(self, df: pd.DataFrame, title: str = "Verteilung"):

        if df.empty:
            print("DataFrame ist leer.")
            return

        df.set_index('category')['count'].plot.pie(
            autopct='%1.1f%%',
            figsize=(8, 8),
            title=title)

        plt.ylabel('')
        plt.show()

    def create_universal_bar_chart(self, df: pd.DataFrame, title: str = "Verteilung", xlabel: str = "Kategorie"):
        if df.empty:
            print("Keine Daten zur Anzeige.")
            return

        fig = px.bar(df,
                     x='category',
                     y='count',
                     title=title,
                     labels={'category': xlabel, 'count': 'Anzahl'},
                     color='category')

        fig.show()

    #In business_logic/guest_manager.py sind die Funktionen zur Verwaltung von Gästen zwar implementiert, aber sie werden nirgendwo aufgerufen.
    #m UI-Bereich werden dagegen die Methoden des Data-Access-Layers direkt genutzt. Beispielsweise ruft admin_ui.py beim Aktualisieren eines Gastes guest_dal.update_guest(guest) auf, ohne den GuestManager zu verwenden.
    #Da in den vorhandenen UI-Modulen keine Aufrufe an get_guest_by_id, get_all_guests, update_guest oder delete_guest erfolgen und stattdessen direkt mit dem GuestDataAccess gearbeitet wird, bleiben diese Funktionen im GuestManager ungenutzt.
    #Sie wurden als Schnittstelle vorgesehen, um Datenbankzugriffe zu kapseln, doch die Implementierung greift an vielen Stellen direkt auf den DAL zu.
    #Dadurch kommen die genannten Methoden schlicht nicht zum Einsatz.

    #def get_guest_by_id(self, guest_id: int) -> Optional[Guest]:
        #return self.__dal.read_guest_by_id(guest_id)

    #def get_all_guests(self) -> List[Guest]:
        #return self.__dal.read_all_guests()

    #def update_guest(self, guest: Guest) -> None:
         #self.__dal.update_guest(guest)

    #def delete_guest(self, guest: Guest) -> None:
        #self.__dal.delete_guest(guest)

