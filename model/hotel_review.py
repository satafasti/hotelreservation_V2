from __future__ import annotations
from typing import TYPE_CHECKING

class HotelReview:
    def __init__(self, review_id = None, guest_id = None, hotel_id = None, booking_id = None, rating = None, comment = None, review_date = None):
        self.review_id = review_id
        self.guest_id = guest_id
        self.hotel_id = hotel_id
        self.booking_id = booking_id
        self.rating = rating
        self.comment = comment
        self.review_date = review_date