import unittest
from app.model.invoice import Invoice
import datetime
import app.model.invoice_factoring as inf


class TestInvoiceFactoring(unittest.TestCase):
    def test_amt_to_collect(self):
        invoice = Invoice(100000, "2019-11-08", 30, 0.80,
                          factor_start_date="2019-11-09")
        to_collect = inf.calc_amt_to_collect(invoice, 0.03)
        self.assertEqual(to_collect, 80000.0)

    def test_invoice_staleness(self):
        invoice = Invoice(5, "2012-12-12", 30, 0.80)
        is_stale = inf.check_stale_invoice(invoice)
        self.assertEqual(is_stale, True)
