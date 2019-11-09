import datetime


def calc_amt_to_collect(invoice):
    """
    Calculates the total interest+principal to collect.
    """
    pass


def calc_factor_amt(invoice_value, LTV):
    """
    Calculates the factor amount for the invoice (a/c rec)
    Amt given to the supplier
    """
    factor_amnt = invoice_value*(LTV/100)
    str_amnt = str(round(factor_amnt))
    number_of_digits = len(str_amnt)
    number_to_divide_multiply = 10**number_of_digits
    round_number = round(factor_amnt/number_to_divide_multiply, 2)
    return int(round_number*number_to_divide_multiply)


def check_stale_invoice(invoice, staleness_threshold=30):
    """
    Checks the staleness of an invoices

    """
    now = datetime.datetime.now()
    delta = invoice.date - now
    day_diff = delta.days
    if day_diff <= staleness_threshold:
        return True
    return False
