from model import Invoice
from model import Booking
from data_access.invoice_dal import InvoiceDataAccess
from data_access.booking_dal import BookingDataAccess
from typing import Optional


class InvoiceManager:
    def __init__(self, db_path: str = None):
        self.__invoice_dal = InvoiceDataAccess(db_path)
        self.__booking_dal = BookingDataAccess(db_path)

    def cancel_invoice_by_booking(self, booking_id: int):
        invoice = self.__invoice_dal.read_invoice_by_booking_id(booking_id)
        if invoice:
            invoice.total_amount = 0.0
            self.__invoice_dal.update_invoice(invoice)
            return invoice
        return None

    def create_invoice_if_not_exists(self, booking_id: int) -> Invoice:
        if booking_id is None:
            raise ValueError("booking_id wird benötigt.")


        if self.__invoice_dal.invoice_exists_for_booking(booking_id):
            raise Exception(f"Für Buchung {booking_id} existiert bereits eine Rechnung.")


        booking = self.__booking_dal.read_booking_by_id(booking_id)
        if booking is None:
            raise LookupError(f"Buchung mit ID {booking_id} wurde nicht gefunden.")

        if booking.is_cancelled:
            raise ValueError("Für stornierte Buchungen wird keine Rechnung erstellt.")


        invoice = Invoice(
            invoice_id=None,
            booking_id=booking.booking_id,
            issue_date=booking.check_out_date,
            total_amount=booking.total_amount
        )

        return self.__invoice_dal.create_invoice(invoice)

    def get_booking_by_id(self, booking_id: int) -> Optional["Booking"]:
        return self.__booking_dal.read_booking_by_id(booking_id)

    def invoice_exists(self, booking_id: int) -> bool:
        return self.__invoice_dal.invoice_exists_for_booking(booking_id)

    def get_invoice_by_booking_id(self, booking_id: int) -> Optional[Invoice]:
        return self.__invoice_dal.read_invoice_by_booking_id(booking_id)

    # Im Projekt wurde nach einem Neustart ein Grossteil des Codes neu geschrieben. Dabei stellte sich heraus, dass einige der früher implementierten Methoden nicht mehr benötigt wurden. Um versehentliche Löschungen zu vermeiden und aus Zeitgründen wurden sie nur auskommentiert.
    # def create_invoice(self, booking_id: int, issue_date: str, total_amount: float) -> Invoice:
    #     invoice = Invoice(None, booking_id, issue_date, total_amount)
    #     return self.__invoice_dal.create_invoice(invoice)

    # def read_invoice_by_id(self, invoice_id: int) -> Optional[Invoice]:
    #     return self.__invoice_dal.read_invoice_by_id(invoice_id)

    # def read_all_invoices(self) -> List[Invoice]:
    #     return self.__invoice_dal.read_all_invoices()

    # def update_invoice(self, invoice: Invoice):
    #     self.__invoice_dal.update_invoice(invoice)

    # def delete_invoice(self, invoice: Invoice):
    #     self.__invoice_dal.delete_invoice(invoice)
