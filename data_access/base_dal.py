import sqlite3
from typing import List, Dict, Any, Optional

class BaseDAL:
    def __init__(self, db_path: str):
        self.__dbpath = db_path
        self.__connection = None
        self.__cursor = None

    def connect(self):
        self.__connection = sqlite3.connect(self.__dbpath)
        self.__cursor = self.__connection.cursor()

    def disconnect(self):
        if self.__connection:
            self.__connection.close()

    def execute(self, query: str, params: tuple = ()):
        self.__cursor.execute(query, params)
        self.__connection.commit()
        return self.__cursor.fetchall()

    def execute_query(self, query: str, params: tuple = ()) -> None:
        try:
            self.__cursor.execute(query, params)
            self.__connection.commit()
        except sqlite3.Error as e:
            print(f"Fehler beim Ausführen der Abfrage: {e}")
            self.__connection.rollback()
            raise

    def fetch_one(self, query: str, params: tuple = ()) -> Optional[tuple]:
        try:
            self.__cursor.execute(query, params)
            return self.__cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Fehler beim Abrufen eines Datensatzes: {e}")
            raise

    def fetch_all(self, query: str, params: tuple = ()) -> List[tuple]:
        try:
            self.__cursor.execute(query, params)
            return self.__cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Fehler beim Abrufen aller Datensätze: {e}")
            raise

