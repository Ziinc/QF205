import unittest
from app.model.invoice import Invoice
import datetime


class TestInvoiceInit(unittest.TestCase):
    def test_invoice_init(self):
        invoice = Invoice(5, "2012-12-12", 4, 0.80)
        self.assertEqual(invoice.amt, 5)
        self.assertEqual(invoice.date_iso_string, '2012-12-12')
        self.assertEqual(
            invoice.date, datetime.date.fromisoformat('2012-12-12'))

    def test_input_parsing(self):
        try:
            invoice = Invoice("20,200,000", "2012-12-12", 4, 0.80)
            self.assertEqual(invoice.amt, 20200000)
            invoice = Invoice("$20,200,000", "2012-12-12", 4, 0.80)
            self.assertEqual(invoice.amt, 20200000)
            invoice = Invoice("$20,200,000", "2012-12-12", 4, 0.80)
            self.assertEqual(invoice.amt, 20200000)
        except Exception as e:
            self.fail(f"Failed invoice insertion. Error: {e}")

    def test_invoice_init_error(self):
        # check for invoice accepted values
        self.assertRaises(AttributeError, Invoice,
                          None, "2012-12-12", 4, 0.80)
        self.assertRaises(AttributeError, Invoice,
                          "$,5", "2012-12-12", 4, 0.80)
        self.assertRaises(AttributeError, Invoice,
                          "$,5.00", "2012-12-12", 4, 0.80)

        # check invoice datestring
        self.assertRaises(AttributeError, Invoice,
                          5, None, 4, 0.80)
        self.assertRaises(AttributeError, Invoice,
                          5, "12-12-12", 4, 0.80)

        # check credit term
        self.assertRaises(AttributeError, Invoice,
                          5, "2012-12-12", None, 0.80)
        self.assertRaises(AttributeError, Invoice,
                          5, "2012-12-12", 12.2, 0.80)
        self.assertRaises(AttributeError, Invoice,
                          5, "2012-12-12", "12.2", 0.80)

        # Check ltv factor amt
        self.assertRaises(AttributeError, Invoice,
                          5, "2012-12-12", 4, None)
        self.assertRaises(AttributeError, Invoice,
                          5, "2012-12-12", 4, 2)

        # check kwargs
        # check factor_start_date
        self.assertRaises(AttributeError, Invoice,
                          5, "2012-12-12", 4, 0.80, factor_start_date=None)

        # check company name
        self.assertRaises(AttributeError, Invoice,
                          5, "2012-12-12", 4, 0.80, company_name=None)

        self.assertRaises(AttributeError, Invoice,
                          5, "2012-12-12", 4, 0.80, company_name=123)
