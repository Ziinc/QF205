import datetime


def calc_amt_to_collect(invoice, interest_pct=0.12):
    """
    Calculates the total interest+principal to collect.
    Args:
    - invoice (Invoice)
    - interest_pct (float)
    """
    factor_amt = calc_factor_amt(invoice.amt, invoice.factor_pct)

    now = datetime.date.today()
    from_factor_start_delta = now - invoice.factor_start_date
    days_from_factor_start = from_factor_start_delta.days
    interest = factor_amt * interest_pct * (days_from_factor_start/360)
    return factor_amt + interest


def calc_due_date(invoice):
    # due_date = invoice.factor_start_date + \
    #     datetime.timedelta(days=invoice.credit_terms)
    pass


def calc_factor_amt(invoice_value, ltv):
    """
    Calculates the factor amount for the invoice

    Args:
    - invoice_value (float)
    - ltv (float) 
    """
    return invoice_value*ltv


def check_is_stale_invoice(invoice, staleness_threshold=5):
    """
    Checks the staleness of an invoices

    Args:
    - invoice (Invoice)
    - staleness_threshold (int)
    """
    now = datetime.date.today()
    delta = now - invoice.date
    day_diff = delta.days

    if day_diff <= staleness_threshold:

        return False
    return True
