import os
#import pandas as pd
from model.hotel_review import HotelReview
from data_access.hotel_review_dal import HotelReviewDataAccess

class HotelReviewManager:
    def __init__(self, db_path: str = None):
        self.__hotel_review_dal = HotelReviewDataAccess(db_path)

    def create_hotel_review(self, hotel_review: HotelReview):
        return self.__hotel_review_dal.create_hotel_review(hotel_review)


    def read_reviews_by_hotel_id(self, hotel_id: int) -> list[HotelReview]:
        return self.__hotel_review_dal.read_reviews_by_hotel_id(hotel_id)