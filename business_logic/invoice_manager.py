from data_access.invoice_dal import InvoiceDataAccess
from model.invoice import Invoice
from typing import Optional, List

class InvoiceManager:
    def __init__(self, db_path: str = None):
        self.__dal = InvoiceDataAccess(db_path)

    def create_invoice(self, booking_id: int, issue_date: str, total_amount: float) -> Invoice:
        invoice = Invoice(None, booking_id, issue_date, total_amount)
        return self.__dal.create_invoice(invoice)

    def read_invoice_by_id(self, invoice_id: int) -> Optional[Invoice]:
        return self.__dal.read_invoice_by_id(invoice_id)

    def read_all_invoices(self) -> List[Invoice]:
        return self.__dal.read_all_invoices()

    def update_invoice(self, invoice: Invoice):
        self.__dal.update_invoice(invoice)

    def delete_invoice(self, invoice: Invoice):
        self.__dal.delete_invoice(invoice)

    def cancel_invoice_by_booking(self, booking_id: int):
        invoice = self.__dal.read_invoice_by_booking_id(booking_id)
        if invoice:
            invoice.total_amount = 0.0
            self.__dal.update_invoice(invoice)
