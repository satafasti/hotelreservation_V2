from data_access.hotel_review_dal import HotelReviewDataAccess

class HotelReviewManager:
    def __init__(self, db_path: str = None):
        self.__hotel_review_dal = HotelReviewDataAccess(db_path)


# Diese Manager-Methoden rufen lediglich die gleichnamigen Funktionen des HotelReviewDataAccess auf. Im UI‑Code werden jedoch die DAL-Objekte direkt verwendet, ohne den Manager einzubinden.
# Beim Erfassen einer Bewertung wird hotel_review_dal.create_hotel_review(hotel_review) aufgerufen und beim Anzeigen der Bewertungen.

    #def create_hotel_review(self, hotel_review: HotelReview):
     #   return self.__hotel_review_dal.create_hotel_review(hotel_review)


    #def read_reviews_by_hotel_id(self, hotel_id: int) -> list[HotelReview]:
     #   return self.__hotel_review_dal.read_reviews_by_hotel_id(hotel_id)