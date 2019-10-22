import unittest
from app.model.invoice import Invoice
from datetime import date


class TestInvoiceInit(unittest.TestCase):
    def test_invoice_init(self):
        invoice = Invoice(5, "2012-12-12")
        self.assertEqual(invoice.amt, 5)
        self.assertEqual(invoice.date_iso_string, '2012-12-12')
        self.assertEqual(invoice.date, date.fromisoformat('2012-12-12'))
