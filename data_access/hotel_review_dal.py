import model
from data_access.base_dal import BaseDataAccess

class HotelReviewDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_hotel(self, hotel: m