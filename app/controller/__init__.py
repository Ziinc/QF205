class Controller():
    def __init__(self):
        # For subdivided controllers, if necessary.
        super().__init__()

    def list_invoices(self):
        """
        1. fetch all invoices from database
        2. calculate factoring info for each
        3. pass invoice data and factoring info to view
        """
        pass

    def get_invoice(self):
        """
        1. fetch single invoice.
        2. calculate factoring info
        3. pass data and factoring info to view
        """
        pass

    def create_invoice(self):
        """
        1. validate single invoice data
        2. store single invoice data

        """
        pass

    def update_invoice(self):
        """
        1. validate single invoice data
        2. store single invoice data
        """
        pass

    def delete_invoice(self):
        """
        1. delete invoice data.
        """
        pass

    def _factor_invoice(self):
        pass
