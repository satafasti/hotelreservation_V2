from data_access.payment_dal import PaymentDataAccess
from model.payment import Payment
from datetime import datetime

class PaymentManager:
    def __init__(self, db_path: str = None):
        self.__dal = PaymentDataAccess(db_path)

    def create_payment(self, booking_id: int, amount: float, payment_method: str) -> Payment:
        payment_date = datetime.now().date()
        payment = Payment(None, booking_id, payment_date, amount, payment_method)
        return self.__dal.create_payment(payment)

    # Aktuell sind diese Methoden nicht im Einsatz, werden aber für potenzielle Systemerweiterungen bereitgehalten.
    # def read_payment_by_id(self, payment_id: int) -> Optional[Payment]:
    #     return self.__dal.read_payment_by_id(payment_id)

    # def read_payments_by_booking_id(self, booking_id: int) -> List[Payment]:
    #     return self.__dal.read_payments_by_booking_id(booking_id)

    # def read_all_payments(self) -> List[Payment]:
    #     return self.__dal.read_all_payments()
