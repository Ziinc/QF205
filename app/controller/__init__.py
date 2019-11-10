from app.model.invoice import Invoice
import app.model.invoice_factoring as inf


class Controller():
    def __init__(self):
        self._invoices = []

    def list_invoices(self):
        """
        1. fetch all invoices from database
        2. calculate factoring info for each
        3. pass invoice data and factoring info to view
        """
        # iterate over the invoices and calculate the invoicing info for each.
        data = [(x, self._factor_invoice(x)) for x in self._invoices]
        return data

    def get_invoice(self, id):
        """
        finds the first invoice
        1. fetch single invoice.
        2. calculate factoring info
        3. pass data and factoring info to view
        """
        invoice = next((x for x in self._invoices if id == x.id), None)
        if invoice is None:
            # TODO: throw error
            pass
        data = (invoice, self._factor_invoice(invoice))
        return data

    def create_invoice(self, attrs):
        """
        1. validate single invoice data
        2. store single invoice data

        """
        invoice = Invoice(**attrs)
        # TODO: perform invoice checks
        self._invoices.append(invoice)
        return invoice

    def update_invoice(self, id, attrs):
        """
        1. validate single invoice data
        2. store single invoice data
        """
        invoice = next((x for x in self._invoices if id == x.id), None)
        if invoice is None:
            # TODO: throw error
            pass
        invoice.validate_and_update(attrs)
        # return updated invoice
        return invoice

    def delete_invoice(self, id):
        """
        1. delete invoice data.
        """
        self._invoices = [x for x in self._invoices if id != x.id]

    def _factor_invoice(self, x):
        """
        Performs necessary factoring calculations
        """
        return {'amt_to_collect': inf.calc_amt_to_collect(x),
                'is_stale': inf.check_is_stale_invoice(x)}
