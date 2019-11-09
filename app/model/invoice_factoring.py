

def calc_amt_to_collect(invoice):
    """
    Calculates the total interest+principal to collect.
    """
    pass


def calc_factor_amt():
    """
    Calculates the factor amount for the invoice (a/c rec)
    """
    pass


def check_stale_invoice(invoice_date, staleness_threshold=30):
    """
    Checks the staleness of an invoice

    """
    if staleness_threshold > 30:
        return True

    return False
