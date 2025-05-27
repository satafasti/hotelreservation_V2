import model
from data_access.base_dal import BaseDataAccess
from typing import Optional

class InvoiceDAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

     #booking_id kommt aber von Booking #invoice Id wurde entfernt, weil wir autoincrement nutzen
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

    def read_invoice_by_id(self, invoice_id: int) -> Optional[model.Invoice]:
        sql = """
        SELECT invoice_id, booking_id, issue_date, total_amount
        FROM Invoice
        WHERE invoice_id = ?
        """
        result = self.fetchone(sql, (invoice_id,))
        if result:
            invoice_id, booking_id, issue_date, total_amount = result
            return model.Invoice(invoice_id, booking_id, issue_date, total_amount)
        return None

    def update_invoice(self, invoice: model.Invoice): #booking_id kommt aber von Booking
        if invoice is None:
            raise ValueError("Invoice object is required")

        sql = """
        UPDATE Invoice SET issue_date = ?, total_amount = ? WHERE invoice_id = ? AND booking_id = ?
        """
        params = (invoice.issue_date, invoice.total_amount, invoice.invoice_id, invoice.booking_id)
        self.execute(sql, params)

    def delete_invoice(self, invoice: model.Invoice):
        if invoice is None:
            raise ValueError("Invoice cannot be None")

        sql = """
        DELETE FROM Invoice WHERE invoice_id = ? AND booking_id = ?
        """
        params = (invoice.invoice_id,invoice.booking_id)
        last_row_id, row_count = self.execute(sql, params)
        if row_count == 0:
            raise LookupError(f"No invoice found with id {invoice.invoice_id} and booking_id {invoice.booking_id}")

    def read_all_invoices(self):
        sql = "SELECT invoice_id, booking_id, issue_date, total_amount FROM Invoice"
        results = self.fetchall(sql)
        return [
            model.Invoice(invoice_id, booking_id, issue_date, total_amount)
            for invoice_id, booking_id, issue_date, total_amount in results
        ]


