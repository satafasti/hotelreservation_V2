from data_access.base_dal import BaseDataAccess
from model.hotel_review import HotelReview


class HotelReviewDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_hotel_review(self, hotel_review: HotelReview):
        if hotel_review is None:
            raise ValueError("Hotel Review wird benötigt.")

        sql = """
              INSERT INTO Hotel_Review (guest_id, hotel_id, booking_id, rating, comment, review_date)
              VALUES (?, ?, ?, ?, ?, ?)
              """
        params = (hotel_review.guest_id, hotel_review.hotel_id, hotel_review.booking_id, hotel_review.rating, hotel_review.comment, hotel_review.review_date)

        last_row_id, _ = self.execute(sql, params)
        hotel_review.review_id = last_row_id
        return hotel_review

    def read_reviews_by_hotel_id(self, hotel_id: int) -> list[HotelReview]:
        sql = """
              SELECT review_id, guest_id, hotel_id, booking_id, rating, comment, review_date
              FROM Hotel_Review
              WHERE hotel_id = ?
              ORDER BY review_date DESC 
              """
        results = self.fetchall(sql, (hotel_id,))
        return [HotelReview(*row) for row in results]