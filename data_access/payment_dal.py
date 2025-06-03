import model
from data_access.base_dal import BaseDataAccess
from typing import Optional, List

class PaymentDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_payment(self, payment: model.Payment) -> model.Payment:
        if payment is None:
            raise ValueError("Payment is required")
        sql = """
        INSERT INTO Payment (booking_id, payment_date, amount, payment_method)
        VALUES (?, ?, ?, ?)
        """
        params = (
            payment.booking_id,
            payment.payment_date,
            payment.amount,
            payment.payment_method,
        )
        payment_id, _ = self.execute(sql, params)
        payment._Payment__payment_id = payment_id
        return payment

    def read_payment_by_id(self, payment_id: int) -> Optional[model.Payment]:
        sql = """
        SELECT payment_id, booking_id, payment_date, amount, payment_method
        FROM Payment WHERE payment_id = ?
        """
        result = self.fetchone(sql, (payment_id,))
        if result:
            return model.Payment(*result)
        return None

    def read_payments_by_booking_id(self, booking_id: int) -> List[model.Payment]:
        sql = """
        SELECT payment_id, booking_id, payment_date, amount, payment_method
        FROM Payment WHERE booking_id = ?
        """
        results = self.fetchall(sql, (booking_id,))
        return [model.Payment(*row) for row in results]

    def read_all_payments(self) -> List[model.Payment]:
        sql = "SELECT payment_id, booking_id, payment_date, amount, payment_method FROM Payment"
        results = self.fetchall(sql)
        return [model.Payment(*row) for row in results]