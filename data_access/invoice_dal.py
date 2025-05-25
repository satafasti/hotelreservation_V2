from __future__ import annotations

import model
from data_access.base_dal import BaseDAL


class InvoiceDAL(BaseDAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_invoice(self, invoice: model.Invoice): #booking_id kommt aber von Booking
        sql = """
        INSERT INTO Invoice (invoice_id, booking_id, issue_date, total_amount) VALUES (?, ?, ?, ?)
        """
        params = (invoice.invoice_id if invoice else None, invoice.booking_id, invoice.issue_date, invoice.total_amount)
        self.execute(sql, params)

    def show_invoice_by_id(self, invoice: model.Invoice):
        sql = """
        SELECT * FROM Invoice WHERE Invoice.invoice_id = ?
        """
        params = (invoice.invoice_id,)
        result = self.fetch_one(sql, params)
        if result:
            invoice_id, booking_id, issue_date, total_amount = result
            return model.Invoice(invoice_id, booking_id, issue_date, total_amount)
        else:
            return None

    def update_invoice(self, invoice: model.Invoice): #booking_id kommt aber von Booking
        sql = """
        UPDATE Invoice SET issue_date = ?, total_amount = ? WHERE invoice_id = ? AND booking_id = ?
        """
        params = (invoice.issue_date, invoice.total_amount, invoice.invoice_id, invoice.booking_id)
        self.execute(sql, params)

    def delete_invoice(self, invoice: model.Invoice):
        sql = """
        DELETE FROM Invoice WHERE invoice_id = ? AND booking_id = ?
        """
        params = (invoice.invoice_id,invoice.booking_id)
        self.execute(sql, params)

    def show_all_invoices(self):
        sql = "SELECT * FROM Invoice"
        results = self.fetch_all(sql)  # kommt aus BaseDAL
        invoices = []

        for row in results:
            invoice_id, booking_id, issue_date, total_amount = row
            invoices.append(model.Invoice(invoice_id, booking_id, issue_date, total_amount))
        return invoices


