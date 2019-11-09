import unittest
from app.model.invoice import Invoice
from app.controller import Controller

create_attrs = {
    'amt': 5,
    'date': "2012-12-12",
    'credit_term': 30,
    'factor_pct': 0.11
}
update_attrs = {
    'amt': 6,
    'date': "2012-12-12",
    'credit_term': 30,
    'factor_pct': 0.11
}


class ControllerTest(unittest.TestCase):
    def test_list_invoices(self):
        con = Controller()
        con.create_invoice(create_attrs)
        invoices = con.list_invoices()
        (invoice, factoring_data) = invoices[0]
        self.assertTrue(isinstance(invoice, Invoice))
        self.assertEqual(invoice.amt, 5)

        # should return a dict
        self.assertTrue(isinstance(factoring_data, dict))

    def test_create_invoice(self):
        con = Controller()
        invoice = con.create_invoice(create_attrs)
        self.assertTrue(isinstance(invoice, Invoice))

        (fetched, factoring_data) = con.get_invoice(invoice.id)
        self.assertTrue(isinstance(fetched, Invoice))
        self.assertEqual(fetched.id, invoice.id)

        self.assertTrue(isinstance(factoring_data, dict))

    def test_update_invoice(self):
        con = Controller()
        invoice = con.create_invoice(create_attrs)

        updated = con.update_invoice(invoice.id, update_attrs)
        self.assertTrue(isinstance(updated, Invoice))
        self.assertEqual(updated.id, invoice.id)
        self.assertEqual(updated.amt, update_attrs["amt"])
