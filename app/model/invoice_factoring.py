import datetime


def calc_amt_to_collect(invoice, interest_pct=0.12):
    """
    Calculates the total interest+principal to collect.
    """
    factor_amt = calc_factor_amt(invoice.amt, invoice.factor_pct)

    # due_date = invoice.factor_start_date + \
    #     datetime.timedelta(days=invoice.credit_term)

    now = datetime.date.today()
    from_factor_start_delta = invoice.factor_start_date - now
    days_from_factor_start = from_factor_start_delta.days
    interest = factor_amt * interest_pct * (days_from_factor_start/360)
    return factor_amt + interest


def calc_factor_amt(invoice_value, ltv):
    """
    Calculates the factor amount for the invoice (a/c rec)
    Amt given to the supplier
    """
    return invoice_value*ltv
    # str_amnt = str(round(factor_amnt))
    # number_of_digits = len(str_amnt)
    # number_to_divide_multiply = 10**number_of_digits
    # round_number = round(factor_amnt/number_to_divide_multiply, 2)
    # return int(round_number*number_to_divide_multiply)


def check_stale_invoice(invoice, staleness_threshold=30):
    """
    Checks the staleness of an invoices

    """
    now = datetime.date.today()
    delta = invoice.date - now
    day_diff = delta.days
    if day_diff <= staleness_threshold:
        return True
    return False
