import model
from data_access.base_dal import BaseDataAccess
from typing import Optional

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_invoice(self, invoice: model.Invoice) -> model.Invoice:
        if invoice is None:
            raise ValueError("Invoice is required")

        sql = """
        INSERT INTO Invoice (booking_id, issue_date, total_amount)
        VALUES (?, ?, ?)
        """
        params = (invoice.booking_id, invoice.issue_date, invoice.total_amount)
        invoice_id, _ = self.execute(sql, params)
        invoice._Invoice__invoice_id = invoice_id
        return invoice

    def update_invoice(self, invoice: model.Invoice):
        if invoice is None:
            raise ValueError("Invoice object is required")

        sql = """
        UPDATE Invoice
        SET issue_date = ?, total_amount = ?
        WHERE invoice_id = ? AND booking_id = ?
        """
        params = (invoice.issue_date, invoice.total_amount, invoice.invoice_id, invoice.booking_id)
        self.execute(sql, params)


    def read_invoice_by_booking_id(self, booking_id: int) -> Optional[model.Invoice]:
        if booking_id is None:
            raise ValueError("booking_id wird benötigt.")

        sql = """
        SELECT invoice_id, booking_id, issue_date, total_amount
        FROM Invoice
        WHERE booking_id = ?
        """
        result = self.fetchone(sql, (booking_id,))
        if result:
            invoice_id, booking_id, issue_date, total_amount = result
            return model.Invoice(invoice_id, booking_id, issue_date, total_amount)
        return None

    def invoice_exists_for_booking(self, booking_id: int) -> bool:
        return self.read_invoice_by_booking_id(booking_id) is not None

    # Im Projekt wurde nach einem Neustart ein Grossteil des Codes neu geschrieben.
    # Dabei stellte sich heraus, dass einige der früher implementierten Methoden
    # nicht mehr benötigt wurden. Um versehentliche Löschungen zu vermeiden und aus
    # Zeitgründen wurden sie nur auskommentiert.

    # def cancel_invoice_by_booking_id(self, booking_id: int) -> bool:
    #     if booking_id is None:
    #         raise ValueError("booking_id ist erforderlich")
    #
    #     sql = """
    #     UPDATE Invoice
    #     SET total_amount = 0
    #     WHERE booking_id = ?
    #     """
    #     params = (booking_id,)
    #     _, row_count = self.execute(sql, params)
    #     return row_count > 0
    #
    # def read_invoice_by_id(self, invoice_id: int) -> Optional[model.Invoice]:
    #     sql = """
    #     SELECT invoice_id, booking_id, issue_date, total_amount
    #     FROM Invoice
    #     WHERE invoice_id = ?
    #     """
    #     result = self.fetchone(sql, (invoice_id,))
    #     if result:
    #         invoice_id, booking_id, issue_date, total_amount = result
    #         return model.Invoice(invoice_id, booking_id, issue_date, total_amount)
    #     return None
    #
    # def read_all_invoices(self) -> List[model.Invoice]:
    #     sql = "SELECT invoice_id, booking_id, issue_date, total_amount FROM Invoice"
    #     results = self.fetchall(sql)
    #     return [
    #         model.Invoice(invoice_id, booking_id, issue_date, total_amount)
    #         for invoice_id, booking_id, issue_date, total_amount in results
    #     ]
    #
    # def delete_invoice(self, invoice: model.Invoice):
    #     if invoice is None:
    #         raise ValueError("Invoice cannot be None")
    #
    #     sql = """
    #     DELETE FROM Invoice
    #     WHERE invoice_id = ? AND booking_id = ?
    #     """
    #     params = (invoice.invoice_id, invoice.booking_id)
    #     _, row_count = self.execute(sql, params)
    #     if row_count == 0:
    #         raise LookupError(f"No invoice found with id {invoice.invoice_id} and booking_id {invoice.booking_id}")
